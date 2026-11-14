# -*- coding: utf-8 -*-
"""Book 4, Chapter 5 — Valve Sizing and Selection, U.S.C.S. Units (EN/VI bilingual)."""

from prv_common import p, h2, h3, ul, note, eq

PAGES_SRC = 10
BYLINE = "Crosby Valve Inc. · Technical Document TP-V300"
TITLE_EN = "Valve Sizing and Selection — U.S.C.S. Units"
TITLE_VI = "Định cỡ và lựa chọn van — Đơn vị USCS"


# ---- equation helpers (self-contained, no global CSS dependency) -------------
def _sq(x):
    return '&#8730;<span style="border-top:1px solid currentColor;padding:0 .18rem;">%s</span>' % x

def _fr(num, den):
    return ('<span style="display:inline-block;text-align:center;vertical-align:middle;'
            'margin:0 .3rem;">'
            '<span style="display:block;border-bottom:1px solid currentColor;padding:0 .4rem;">%s</span>'
            '<span style="display:block;padding:0 .4rem;">%s</span></span>' % (num, den))

def _sub(x):
    return '<sub>%s</sub>' % x


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 5.</b> MAWP — áp suất làm việc cực đại cho phép · "
                "quá áp (overpressure) — vượt áp suất thiết lập · áp suất ngược (back pressure): "
                "chép lên (superimposed) / tạo ra (built-up) · diện tích xả hiệu dụng (effective "
                "discharge area) · hệ số hiệu năng K = 0.975 · K_b, K_sh, K_n, K_w, K_v — hệ số "
                "hiệu chỉnh · áp lực thử chênh lệch nguội (CDTP) · hệ số năng lực kết hợp.")
    return ("<b>Key terms.</b> MAWP — maximum allowable working pressure · overpressure — above "
            "set pressure · back pressure: superimposed / built-up · effective discharge area · "
            "discharge coefficient K = 0.975 · K_b, K_sh, K_n, K_w, K_v — correction factors · "
            "cold differential test pressure (CDTP) · combination capacity factor.")


def body_vi():
    b = []
    b.append(p("Phần này của Cẩm nang kỹ thuật van xả áp Crosby giúp người dùng định cỡ và lựa "
               "chọn van xả áp khi các thông số hệ thống được biểu diễn bằng hệ đơn vị USCS "
               "(United States Customary System). Các công thức và hệ số hiệu chỉnh trong cẩm "
               "nang được xây dựng bởi Crosby và các đơn vị khác trong ngành, phản ánh công nghệ "
               "định cỡ tiên tiến nhất, và phù hợp với ASME Section VIII cùng API RP 520."))
    b.append(p("Các công thức dùng để tính diện tích xả hiệu dụng tối thiểu cần thiết để van xả "
               "được lưu lượng chất lưu tại điều kiện xả dự kiến. Từ đó chọn kích cỡ và kiểu van "
               "có diện tích danh nghĩa lớn hơn hoặc bằng diện tích tính toán. Diện tích hiệu "
               "dụng của van Crosby được liệt kê ở trang 7-30 và 7-31. Việc chọn và định cỡ van "
               "là trách nhiệm của kỹ sư hệ thống và người sử dụng thiết bị cần bảo vệ; không "
               "được dựa trên các điều kiện giả định tùy tiện hay thông tin không đầy đủ."))
    b.append(note("Lưu ý: Crosby cung cấp phần mềm CROSBY-SIZE để định cỡ van xả áp (xem trang "
                  "1-1 hoặc liên hệ đại diện Crosby địa phương)."))

    # ---- Required sizing data -------------------------------------------------
    b.append(h2("Dữ liệu định cỡ cần thiết", "Required Sizing Data"))
    b.append(p("Dưới đây là danh sách các điều kiện vận hành cần cung cấp để định cỡ và chọn van "
               "xả áp một cách đúng đắn."))
    b.append(h3("Tính chất chất lưu", "Fluid Properties"))
    b.append(ul([
        "Chất lưu và trạng thái (fluid and state)",
        "Khối lượng phân tử (molecular weight)",
        "Độ nhớt (viscosity)",
        "Tỷ trọng — chất lỏng tham chiếu nước, khí tham chiếu không khí (specific gravity)",
        "Tỷ số nhiệt dung riêng k (ratio of specific heats)",
        "Hệ số nén Z (compressibility factor)",
    ]))
    b.append(h3("Điều kiện vận hành", "Operating Conditions"))
    b.append(ul([
        "Áp suất vận hành (psig tối đa)",
        "Nhiệt độ vận hành (°F tối đa)",
        "Áp suất làm việc cực đại cho phép (MAWP, psig)",
    ]))
    b.append(h3("Điều kiện xả", "Relieving Conditions"))
    b.append(ul([
        "Lưu lượng xả cần thiết — khí (lb/hr), khí (scfm), chất lỏng (gpm)",
        "Áp suất thiết lập (set pressure, psig)",
        "Tỷ lệ quá áp cho phép (% overpressure)",
        "Áp suất ngược chép lên (superimposed back pressure, psig) — chỉ rõ không đổi hay biến thiên",
        "Áp suất ngược tạo ra (built-up back pressure, psig)",
        "Nhiệt độ xả (relieving temperature, °F)",
    ]))

    # ---- Gas / vapor, lb/hr ---------------------------------------------------
    b.append(h2("Định cỡ khí và hơi — quá áp 10% (lb/hr)",
                "Gas and Vapor Sizing — 10% Overpressure (lb/hr)"))
    b.append(p("Công thức dùng cho khí và hơi (trừ hơi nước) khi lưu lượng biểu diễn dưới dạng "
               "lưu lượng khối lượng, pound trên giờ. Các hệ số hiệu chỉnh tính đến áp suất ngược, "
               "độ nén được và dòng chảy dưới tới hạn."))
    b.append(eq('A = ' + _fr('W ' + _sq('T Z'),
                             'C K P' + _sub('1') + ' K' + _sub('b') + ' ' + _sq('M')), "5.1"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu cần thiết, in²",
        "W — lưu lượng xả cần thiết, lb/hr",
        "T — nhiệt độ tuyệt đối tại đầu vào van, °R = °F + 460",
        "Z — hệ số nén (Hình F7-1, trang 7-2); dùng Z = 1.0 nếu không biết",
        "C — hệ số từ tỷ số nhiệt dung riêng (Bảng T7-7, trang 7-26); dùng C = 315 nếu không biết",
        "K — hệ số hiệu năng hiệu dụng, K = 0.975",
        "K_b — hệ số hiệu chỉnh áp suất ngược (Bảng T7-1 trang 7-3 cho van thường; Hình F7-2 "
        "trang 7-5 cho van buồng bellows/Series BP; van pilot xem trang 7-4)",
        "M — khối lượng phân tử (Bảng T7-7, trang 7-26)",
        "P" + _sub("1") + " — áp suất xả tuyệt đối, psia = áp suất thiết lập + quá áp + áp khí quyển",
    ]))
    b.append(h3("Ví dụ 1 — Áp suất ngược khí quyển", "Example 1 — Atmospheric Back Pressure"))
    b.append(p("Chất lưu: khí tự nhiên; lưu lượng: 5.900 lb/hr; áp suất thiết lập: 210 psig; quá "
               "áp: 10%; nhiệt độ xả: 120°F; khối lượng phân tử: 19,0. Với T = 580°R, P₁ = 245,7 "
               "psia, C = 344, K_b = 1,0 (khí quyển) tính được A = 0,396 in². Chọn van cỡ "
               "1-1/2G2-1/2 Style JOS-15, nắp Type J — van \"G\" (0,503 in²) là cỡ nhỏ nhất đáp "
               "ứng. Vật liệu tiêu chuẩn thỏa mãn (khí tự nhiên)."))
    b.append(h3("Ví dụ 2 — Áp suất ngược chép lên không đổi",
                "Example 2 — Superimposed Constant Back Pressure"))
    b.append(p("Giữ nguyên Ví dụ 1 nhưng có áp suất ngược chép lên không đổi 195 psig. Tỷ lệ áp "
               "suất ngược = (195 + 14,7)/(210 + 21 + 14,7) = 85,3%; nội suy Bảng T7-1 được K_b = "
               "0,76. Tính lại A = 0,520 in². Chọn van thường Style JOS cỡ 1-1/2H3 JOS-15, nắp "
               "Type J. Áp lực thử chênh lệch nguội (CDTP) = áp suất thiết lập − áp suất ngược "
               "chép lên = 15 psig; dưới thực tế van mở tại 210 psig (= 15 + 195)."))
    b.append(h3("Ví dụ 3 — Áp suất thiết lập dưới 30 psig",
                "Example 3 — Set Pressure Below 30 psig"))
    b.append(p("Theo ASME VIII, van có áp suất thiết lập < 30 psig dùng quá áp tối đa 3 psi. "
               "Chất lưu: khí (cần tem UV); lưu lượng: 500 lb/hr; áp suất thiết lập: 20 psig; "
               "quá áp: 3 psi; T = 530°R; P₁ = 37,7 psia. Tính A = 0,163 in². Chọn van Crosby "
               "Series 900 1\"×1-1/2\" lỗ N°7 (0,196 in²), đòn bẩy Type D — Model 972103M-D."))
    b.append(h3("Ví dụ 4 — Áp suất ngược chép lên biến thiên",
                "Example 4 — Variable Superimposed Back Pressure"))
    b.append(p("Khi van chịu áp suất ngược biến thiên, áp suất thiết lập sẽ bị ảnh hưởng trừ khi "
               "dùng van cân bằng buồng bellows hoặc Series BP. Chất lưu: khí (tem UV); lưu "
               "lượng: 280 lb/hr; T = 600°R; P₁ = 78,5 psia; K_b lấy từ Bảng F7-2 cho BP-Omni = "
               "0,650. Tính A = 0,072 in². Chọn Series BP 3/4\"×1\" lỗ 0,074 in², đòn bẩy Type D "
               "— Model BP51701M-D."))

    # ---- Gas / vapor, scfm ----------------------------------------------------
    b.append(h2("Định cỡ khí và hơi — quá áp 10% (scfm)",
                "Gas and Vapor Sizing — 10% Overpressure (scfm)"))
    b.append(p("Công thức dùng cho khí và hơi khi lưu lượng biểu diễn dưới dạng lưu lượng thể "
               "tích, scfm. Các hệ số hiệu chỉnh tính đến áp suất ngược, độ nén được và dòng "
               "chảy dưới tới hạn."))
    b.append(eq('A = ' + _fr('SCFM ' + _sq('T G Z'),
                             '1.175 C K P' + _sub('1') + ' K' + _sub('b')), "5.2"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, in²",
        "SCFM — lưu lượng xả cần thiết, standard cubic feet/min",
        "T — nhiệt độ tuyệt đối, °R = °F + 460",
        "G — tỷ trọng khí hoặc hơi so với không khí",
        "Z — hệ số nén (Hình F7-1); Z = 1,0 nếu không biết",
        "C — hệ số từ tỷ số nhiệt dung riêng (Bảng T7-7); C = 315 nếu không biết",
        "K = 0,975; K_b — hệ số hiệu chỉnh áp suất ngược (như trên)",
        "P" + _sub("1") + " — áp suất xả tuyệt đối, psia",
    ]))
    b.append(h3("Ví dụ 1 — Áp suất ngược tạo ra biến thiên",
                "Example 1 — Built-up Variable Back Pressure"))
    b.append(p("Chất lưu: khí ethylene; lưu lượng: 12.000 scfm; áp suất thiết lập: 170 psig; quá "
               "áp: 10%; áp suất ngược: 0–75 psig; T = 660°R; G = 0,968. Tỷ lệ áp suất ngược = "
               "75/170 = 44,1%; K_b = 0,899 (van bellows, Hình F7-2). Van thường: A = 4,282 in² "
               "→ chọn van \"N\" (4,34 in²), Model 4N6 JBS-15, nắp Type L. Van pilot Style JPV: "
               "hiệu năng không bị áp suất ngược ảnh hưởng nên K_b không áp dụng (trừ dòng dưới "
               "tới hạn), A = 3,849 in² → chọn 4N6 JPV-15."))

    # ---- Steam ----------------------------------------------------------------
    b.append(h2("Định cỡ hơi nước — quá áp 10% (lb/hr)",
                "Steam Sizing — 10% Overpressure (lb/hr)"))
    b.append(p("Công thức dựa trên công thức thực nghiệm Napier cho dòng hơi. Các hệ số hiệu chỉnh "
               "tính đến quá nhiệt, áp suất ngược và dòng dưới tới hạn. ASME yêu cầu thêm hệ số "
               "K_n khi áp suất xả P₁ vượt 1.500 psia."))
    b.append(eq('A = ' + _fr('W', '51.5 K P' + _sub('1') + ' K' + _sub('sh')
                             + ' K' + _sub('n') + ' K' + _sub('b')), "5.3"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, in²",
        "W — lưu lượng xả cần thiết, lb/hr",
        "K = 0,975",
        "P" + _sub("1") + " — áp suất xả tuyệt đối, psia",
        "K_sh — hệ số quá nhiệt (Bảng T7-2, trang 7-8); K_sh = 1,00 cho hơi bão hòa",
        "K_n — hơi khô bão hòa khi áp suất thiết lập > 1.500 psia (Hình F7-4, trang 7-6)",
        "K_b — hệ số hiệu chỉnh áp suất ngược (như trên)",
    ]))
    b.append(h3("Ví dụ 1 — Hơi bão hòa", "Example 1 — Saturated Steam"))
    b.append(p("Lưu lượng: 21.500 lb/hr; áp suất thiết lập: 225 psig; quá áp: 10%; P₁ = 262,2 "
               "psia. Tính A = 1,633 in² → chọn van \"K\" (1,838 in²), Model 3K4 JOS-15, đòn "
               "bẩy Type C. Vật liệu tiêu chuẩn thỏa mãn."))
    b.append(h3("Ví dụ 2 — Hơi quá nhiệt", "Example 2 — Superheated Steam"))
    b.append(p("Lưu lượng: 108.500 lb/hr; nhiệt độ xả: 750°F; áp suất thiết lập: 532 psig; P₁ = "
               "599,9 psia. Hệ số quá nhiệt K_sh = 0,844 (trang 7-8). Tính A = 4,268 in² → chọn "
               "van \"N\" (4,34 in²), Model 4N6 JOS-46, đòn bẩy Type C, lò xo thép hợp kim."))
    b.append(h3("Ví dụ 3 — Hơi bão hòa tại áp suất xả > 1.500 psig",
                "Example 3 — Saturated Steam > 1500 psig"))
    b.append(p("Lưu lượng: 88.000 lb/hr; áp suất thiết lập: 2.750 psig; P₁ = 3.039,7 psia. Hệ số "
               "K_n = 1,155 (Hình F7-4). Tính A = 0,499 in² → chọn van \"G\" (0,503 in²), Model "
               "2G3 JOS-76, đòn bẩy Type C, lò xo thép hợp kim."))

    # ---- Liquid, spring loaded ------------------------------------------------
    b.append(h2("Định cỡ chất lỏng — van lò xo (Spring Loaded)",
                "Liquid Sizing — Spring Loaded Valves"))
    b.append(p("Công thức áp dụng cho các kiểu JLT-JOS, JLT-JBS, Series 900 và Series BP, dùng "
               "năng lực được chứng nhận bởi National Board theo ASME Section VIII. Không cho "
               "phép định cỡ với quá áp dưới 10%."))
    b.append(eq('A = ' + _fr('GPM ' + _sq('G'),
                             '28.14 K' + _sub('w') + ' K' + _sub('v') + ' ' + _sq('ΔP')), "5.4"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, in²",
        "G — tỷ trọng chất lỏng tại điều kiện chảy",
        "GPM — lưu lượng xả cần thiết, gallon Mỹ/phút tại nhiệt độ chảy",
        "ΔP — chênh áp (psi) = áp suất thiết lập + quá áp − áp suất ngược",
        "K_v — hệ số hiệu chỉnh độ nhớt (trang 7-7)",
        "K_w — hệ số hiệu chỉnh áp suất ngược cho van bellows/Series BP (Hình F7-3, trang 7-5)",
    ]))
    b.append(h3("Ví dụ 1 — Chất lỏng (gpm)", "Example 1 — Liquid, gpm"))
    b.append(p("Chất lưu: natri trisunfat; lưu lượng: 125 gpm; áp suất thiết lập: 100 psig; quá "
               "áp: 10%; áp suất ngược: 0–30 psig (tạo ra); T = 60°F; G = 1,23. K_w = 0,866 "
               "(Hình F7-3), ΔP = 80 psi. Tính A = 0,636 in² → chọn van \"H\" (0,785 in²). Vì áp "
               "suất ngược tạo ra > 10% nên cần van bellows Style JBS; Model 1-1/2H3 JLT-JBS-15, "
               "nắp Type J."))
    b.append(h3("Ví dụ 2 — Chất lỏng (gpm)", "Example 2 — Liquid, gpm"))
    b.append(p("Chất lưu: dầu thầu dầu (castor oil); lưu lượng: 100 gpm; áp suất thiết lập: 210 "
               "psig; quá áp: 10%; áp suất ngược: 35 psig (không đổi); G = 0,96. K_w = 1,0, "
               "ΔP = 196 psi. Tính A = 0,249 in² → chọn van Series 900 OMNI-TRIM lỗ \"8\" (0,307 "
               "in²). Áp suất ngược không đổi nên dùng van thường JOS hoặc Series 900; Model "
               "981105M-A."))

    # ---- Liquid, pilot operated ----------------------------------------------
    b.append(h2("Định cỡ chất lỏng — van vận hành pilot (Style JPVM)",
                "Liquid Sizing — Pilot Operated Valves (Style JPVM)"))
    b.append(note("Van pilot Style JPVM cho chất lỏng có năng lực lớn hơn 30% so với van lò xo "
                  "trim lỏng, cho phép dùng van nhỏ hơn. Nên giữ độ nhớt ≤ 300 SSU (khi đó K_v = "
                  "1,0). Xem trang 7-25 về dòng hai pha."))
    b.append(eq('A = ' + _fr('GPM ' + _sq('G'), '36.81 K' + _sub('v') + ' ' + _sq('ΔP')), "5.5"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, in²",
        "G — tỷ trọng chất lỏng tại điều kiện chảy",
        "GPM — lưu lượng xả cần thiết, gallon Mỹ/phút tại nhiệt độ chảy",
        "ΔP — chênh áp (psi) = áp suất thiết lập + quá áp − áp suất ngược",
        "K_v — hệ số hiệu chỉnh độ nhớt (trang 7-7)",
    ]))
    b.append(h3("Ví dụ 1 — Chất lỏng GPM, van Style JPVM",
                "Example 1 — Liquid GPM, Crosby Style JPVM"))
    b.append(p("Chất lưu: natri trisunfat; lưu lượng: 125 GPM; áp suất thiết lập: 100 psig; quá "
               "áp: 10%; áp suất ngược: 0–30 psig; G = 1,23; K_v = 1,0; ΔP = 80 psi. Tính A = "
               "0,421 in² → chọn van \"G\" (0,503 in²), Model 1-1/2G3 Style JPVM-15."))

    # ---- Multiple valves ------------------------------------------------------
    b.append(h2("Định cỡ nhiều van", "Multiple Valve Sizing"))
    b.append(p("Khi dùng nhiều van xả áp: một van đặt tại hoặc dưới MAWP, các van còn lại có thể "
               "đặt cao hơn đến 5% MAWP. Tổng diện tích cần thiết tính với quá áp 16% hoặc 4 psi "
               "(lấy giá trị lớn hơn). Khi xét đến hỏa hoạn, xem định cỡ van chất lỏng trong điều "
               "kiện cháy (trang 7-17)."))
    b.append(h3("Ví dụ 1 — Khí tự nhiên", "Example 1 — Natural Gas"))
    b.append(p("MAWP: 210 psig; lưu lượng: 5.900 lb/hr; áp suất thiết lập: 210 psig; quá áp: 16%; "
               "T = 580°R; M = 19,0. P₁ = 258,3 psia. Tính A = 0,376 in² → chọn hai van lỗ \"E\" "
               "(mỗi lỗ 0,196 in², tổng 0,392 in²): một van đặt tại MAWP = 210 psig, một đặt tại "
               "105% MAWP = 220,5 psig. Model 1E2 JOS-15-J."))
    b.append(h3("Ví dụ 2 — Khí", "Example 2 — Air"))
    b.append(p("Lưu lượng: 150.000 lb/hr; áp suất thiết lập: 200 psig; quá áp: 16%; T = 610°R; "
               "M = 28,97; P₁ = 246,7 psia; C = 356. Tính A = 8,038 in². Chọn hai van lỗ \"N\" "
               "(mỗi lỗ 4,340 in², tổng 8,680 in²). Model 4N6 JOS-15-J."))

    # ---- Combination devices --------------------------------------------------
    b.append(h2("Thiết bị kết hợp (đĩa đứt + van xả áp)",
                "Combination Devices (Rupture Disc + Relief Valve)"))
    b.append(p("Năng lực xả định mức của van xả áp kết hợp với đĩa đứt bằng năng lực của van nhân "
               "với hệ số năng lực kết hợp (combination capacity factor) để tính đến tổn thất dòng "
               "do đĩa đứt. Khi không có hệ số đã thử nghiệm cho tổ hợp cụ thể, dùng hệ số 0,9. "
               "Các hệ số được thử nghiệm được tập hợp trong ấn phẩm NB-18 của National Board."))
    b.append(h3("Ví dụ 1 — Khí/hơi, lưu lượng khối lượng (lb/hr)",
                "Example 1 — Gas/Vapor Mass Flow (lb/hr)"))
    b.append(p("Chất lưu: khí tự nhiên; lưu lượng: 7.400 lb/hr; áp suất thiết lập: 210 psig; quá "
               "áp: 10%; T = 580°R; M = 19,0; P₁ = 245,7 psia; C = 344. Tính A = 0,496 in². Với "
               "đĩa đứt hệ số 0,9, diện tích yêu cầu = 0,496/0,9 = 0,551 in² → cần van lỗ \"H\" "
               "(0,785 in²), tăng một cỡ. Nếu dùng đĩa đứt cụ thể có hệ số kết hợp ≥ 0,986 với van "
               "Crosby thì không cần tăng cỡ (xem NB-18, Mục IV)."))
    return "".join(b)


def body_en():
    b = []
    b.append(p("This section of the Crosby Pressure Relief Valve Engineering Handbook is designed "
               "to assist the user in the sizing and selection of pressure relief valves when "
               "system parameters are expressed in U.S.C.S. units. The basic formulae and capacity "
               "correction factors reflect current state-of-the-art technology and are consistent "
               "with the requirements of ASME Section VIII and API Recommended Practice 520."))
    b.append(p("The sizing formulae calculate the required effective discharge area for a valve "
               "that will flow the required volume of system fluid at the anticipated relieving "
               "conditions; the valve size and style are then selected to have a nominal effective "
               "area equal to or greater than the calculated value. Effective areas for Crosby "
               "valves are listed on pages 7-30 and 7-31. Valve selection and sizing is the "
               "responsibility of the system engineer and the user; it must not be based on "
               "arbitrarily assumed conditions or incomplete information."))
    b.append(note("Crosby offers the CROSBY-SIZE computer program for sizing pressure relief "
                  "valves (see page 1-1 or contact your local Crosby Representative)."))

    # ---- Required sizing data -------------------------------------------------
    b.append(h2("Required Sizing Data", "Dữ liệu định cỡ cần thiết"))
    b.append(p("The following is a suggested list of service conditions which must be provided in "
               "order to properly size and select a pressure relief valve."))
    b.append(h3("Fluid Properties", "Tính chất chất lưu"))
    b.append(ul([
        "Fluid and state",
        "Molecular weight",
        "Viscosity",
        "Specific gravity — liquid referred to water, gas referred to air",
        "Ratio of specific heats, k",
        "Compressibility factor, Z",
    ]))
    b.append(h3("Operating Conditions", "Điều kiện vận hành"))
    b.append(ul([
        "Operating pressure (psig maximum)",
        "Operating temperature (°F maximum)",
        "Maximum allowable working pressure, MAWP (psig)",
    ]))
    b.append(h3("Relieving Conditions", "Điều kiện xả"))
    b.append(ul([
        "Required relieving capacity — gas or vapor (lb/hr), gas or vapor (scfm), liquid (gpm)",
        "Set pressure (psig)",
        "Allowable overpressure (%)",
        "Superimposed back pressure (psig) — specify constant or variable",
        "Built-up back pressure (psig)",
        "Relieving temperature (°F)",
    ]))

    # ---- Gas / vapor, lb/hr ---------------------------------------------------
    b.append(h2("Gas and Vapor Sizing — 10% Overpressure (lb/hr)",
                "Định cỡ khí và hơi — quá áp 10% (lb/hr)"))
    b.append(p("This formula is used for gases and vapor (except steam) when required flow is "
               "expressed as a mass flow rate, pounds per hour. Correction factors account for the "
               "effects of back pressure, compressibility and subcritical flow."))
    b.append(eq('A = ' + _fr('W ' + _sq('T Z'),
                             'C K P' + _sub('1') + ' K' + _sub('b') + ' ' + _sq('M')), "5.1"))
    b.append(ul([
        "A — minimum required effective discharge area, in²",
        "W — required relieving capacity, lb/hr",
        "T — absolute temperature at the valve inlet, °R = °F + 460",
        "Z — compressibility factor (Figure F7-1, page 7-2); use Z = 1.0 if unknown",
        "C — coefficient from the ratio of specific heats (Table T7-7, page 7-26); use C = 315 "
        "if unknown",
        "K — effective coefficient of discharge, K = 0.975",
        "K_b — capacity correction factor for back pressure (Table T7-1 page 7-3 for conventional "
        "valves; Figure F7-2 page 7-5 for bellows/Series BP; pilot valves see page 7-4)",
        "M — molecular weight of the gas or vapor (Table T7-7, page 7-26)",
        "P" + _sub("1") + " — relieving pressure, psia = set pressure + overpressure + atmospheric",
    ]))
    b.append(h3("Example 1 — Atmospheric Back Pressure", "Ví dụ 1 — Áp suất ngược khí quyển"))
    b.append(p("Fluid: Natural Gas; capacity: 5,900 lb/hr; set pressure: 210 psig; overpressure: "
               "10%; relieving temp: 120°F; molecular weight: 19.0. With T = 580°R, P₁ = 245.7 "
               "psia, C = 344, K_b = 1.0 (atmospheric), A = 0.396 in². Select a 1-1/2G2-1/2 Style "
               "JOS-15 with Type J cap — the \"G\" orifice (0.503 in²) is the smallest that flows "
               "the required capacity. Standard materials are satisfactory (natural gas)."))
    b.append(h3("Example 2 — Superimposed Constant Back Pressure",
                "Ví dụ 2 — Áp suất ngược chép lên không đổi"))
    b.append(p("Same as Example 1 but with a superimposed constant back pressure of 195 psig. "
               "Back-pressure percentage = (195 + 14.7)/(210 + 21 + 14.7) = 85.3%; interpolating "
               "Table T7-1 gives K_b = 0.76. Recomputed A = 0.520 in². Select a conventional Style "
               "JOS valve, 1-1/2H3 JOS-15 with Type J cap. The cold differential test pressure "
               "(CDTP) = set pressure − superimposed back pressure = 15 psig; under service the "
               "valve opens at 210 psig (= 15 + 195)."))
    b.append(h3("Example 3 — Set Pressure Below 30 psig", "Ví dụ 3 — Áp suất thiết lập dưới 30 psig"))
    b.append(p("ASME Section VIII specifies a maximum allowable overpressure of 3 psi for set "
               "pressures below 30 psig. Fluid: air (UV stamp required); capacity: 500 lb/hr; set "
               "pressure: 20 psig; overpressure: 3 psi; T = 530°R; P₁ = 37.7 psia. A = 0.163 in². "
               "Select a 1\"×1-1/2\" Crosby Series 900 valve with a No. 7 (0.196 in²) orifice, "
               "Type D lifting lever — Model 972103M-D."))
    b.append(h3("Example 4 — Variable Superimposed Back Pressure",
                "Ví dụ 4 — Áp suất ngược chép lên biến thiên"))
    b.append(p("When a relief valve is exposed to variable back pressure, its set pressure is "
               "affected unless a balanced bellows or Series BP valve is selected. Fluid: air (UV "
               "stamp); capacity: 280 lb/hr; T = 600°R; P₁ = 78.5 psia; K_b from Table F7-2 for "
               "BP-Omni = 0.650. A = 0.072 in². Select a 3/4\"×1\" Series BP with a 0.074 in² "
               "orifice, Type D lever — Model BP51701M-D."))

    # ---- Gas / vapor, scfm ----------------------------------------------------
    b.append(h2("Gas and Vapor Sizing — 10% Overpressure (scfm)",
                "Định cỡ khí và hơi — quá áp 10% (scfm)"))
    b.append(p("This formula is used for gases and vapor when required flow is expressed as a "
               "volumetric flow rate, scfm. Correction factors account for back pressure, "
               "compressibility and subcritical flow."))
    b.append(eq('A = ' + _fr('SCFM ' + _sq('T G Z'),
                             '1.175 C K P' + _sub('1') + ' K' + _sub('b')), "5.2"))
    b.append(ul([
        "A — minimum required effective discharge area, in²",
        "SCFM — required relieving capacity, standard cubic feet per minute",
        "T — absolute temperature at the valve inlet, °R = °F + 460",
        "G — specific gravity of the gas or vapor (relative to air)",
        "Z — compressibility factor (Figure F7-1); use Z = 1.0 if unknown",
        "C — coefficient from the ratio of specific heats (Table T7-7); use C = 315 if unknown",
        "K = 0.975; K_b — capacity correction factor for back pressure (as above)",
        "P" + _sub("1") + " — relieving pressure, psia",
    ]))
    b.append(h3("Example 1 — Built-up Variable Back Pressure",
                "Ví dụ 1 — Áp suất ngược tạo ra biến thiên"))
    b.append(p("Fluid: Ethylene Gas; capacity: 12,000 scfm; set pressure: 170 psig; overpressure: "
               "10%; back pressure: 0–75 psig; inlet temp: 200°F; specific gravity: 0.968. Back "
               "pressure percentage = 75/170 = 44.1%; K_b = 0.899 (bellows style, Figure F7-2). "
               "Standard valve: A = 4.282 in² → select an \"N\" orifice (4.34 in²), Model 4N6 "
               "JBS-15, Type L cap. Pilot Style JPV: its performance is unaffected by back "
               "pressure, so K_b is not applicable (except for subcritical flow); A = 3.849 in² → "
               "select a 4N6 JPV-15."))

    # ---- Steam ----------------------------------------------------------------
    b.append(h2("Steam Sizing — 10% Overpressure (lb/hr)",
                "Định cỡ hơi nước — quá áp 10% (lb/hr)"))
    b.append(p("This formula is based on the empirical Napier formula for steam flow. Correction "
               "factors account for superheat, back pressure and subcritical flow. An additional "
               "factor K_n is required by ASME when the relieving pressure (P₁) is above 1500 psia."))
    b.append(eq('A = ' + _fr('W', '51.5 K P' + _sub('1') + ' K' + _sub('sh')
                             + ' K' + _sub('n') + ' K' + _sub('b')), "5.3"))
    b.append(ul([
        "A — minimum required effective discharge area, in²",
        "W — required relieving capacity, lb/hr",
        "K = 0.975",
        "P" + _sub("1") + " — relieving pressure, psia",
        "K_sh — superheat correction factor (Table T7-2, page 7-8); K_sh = 1.00 for saturated steam",
        "K_n — dry saturated steam at set pressures above 1500 psia (Figure F7-4, page 7-6)",
        "K_b — capacity correction factor for back pressure (as above)",
    ]))
    b.append(h3("Example 1 — Saturated Steam", "Ví dụ 1 — Hơi bão hòa"))
    b.append(p("Capacity: 21,500 lb/hr; set pressure: 225 psig; overpressure: 10%; P₁ = 262.2 "
               "psia. A = 1.633 in² → select a \"K\" orifice (1.838 in²), Model 3K4 JOS-15 with "
               "Type C lifting lever. Standard materials are satisfactory."))
    b.append(h3("Example 2 — Superheated Steam", "Ví dụ 2 — Hơi quá nhiệt"))
    b.append(p("Capacity: 108,500 lb/hr; relieving temp: 750°F; set pressure: 532 psig; P₁ = "
               "599.9 psia. Superheat correction K_sh = 0.844 (page 7-8). A = 4.268 in² → select "
               "an \"N\" orifice (4.34 in²), Model 4N6 JOS-46 with Type C lever and alloy steel "
               "spring."))
    b.append(h3("Example 3 — Saturated Steam at Relieving Pressure > 1500 psig",
                "Ví dụ 3 — Hơi bão hòa tại áp suất xả > 1.500 psig"))
    b.append(p("Capacity: 88,000 lb/hr; set pressure: 2,750 psig; P₁ = 3,039.7 psia. Capacity "
               "correction K_n = 1.155 (Figure F7-4). A = 0.499 in² → select a \"G\" orifice "
               "(0.503 in²), Model 2G3 JOS-76 with Type C lever and alloy steel spring."))

    # ---- Liquid, spring loaded ------------------------------------------------
    b.append(h2("Liquid Sizing — Spring Loaded Valves",
                "Định cỡ chất lỏng — van lò xo (Spring Loaded)"))
    b.append(p("This formula applies to Styles JLT-JOS, JLT-JBS, Series 900 and Series BP, using "
               "capacities certified by the National Board of Boiler and Pressure Vessel "
               "Inspectors per ASME Section VIII. Sizing with this formulation is not permitted "
               "for overpressures less than 10%."))
    b.append(eq('A = ' + _fr('GPM ' + _sq('G'),
                             '28.14 K' + _sub('w') + ' K' + _sub('v') + ' ' + _sq('ΔP')), "5.4"))
    b.append(ul([
        "A — minimum required effective discharge area, in²",
        "G — specific gravity of the liquid at flowing conditions",
        "GPM — required relieving capacity, U.S. gallons per minute at flowing temperature",
        "ΔP — differential pressure (psi) = set pressure + overpressure − back pressure",
        "K_v — flow correction factor due to viscosity (page 7-7)",
        "K_w — capacity correction factor for back pressure on bellows or Series BP valves "
        "(Figure F7-3, page 7-5)",
    ]))
    b.append(h3("Example 1 — Liquid, gpm", "Ví dụ 1 — Chất lỏng (gpm)"))
    b.append(p("Fluid: Sodium Trisulfate; capacity: 125 gpm; set pressure: 100 psig; overpressure: "
               "10%; built-up back pressure: 0–30 psig; temp: 60°F; G = 1.23. K_w = 0.866 (Figure "
               "F7-3), ΔP = 80 psi. A = 0.636 in² → select an \"H\" orifice (0.785 in²). Because "
               "built-up back pressure exceeds 10%, a bellows Style JBS is required; Model "
               "1-1/2H3 JLT-JBS-15 with Type J cap."))
    b.append(h3("Example 2 — Liquid, gpm", "Ví dụ 2 — Chất lỏng (gpm)"))
    b.append(p("Fluid: Castor Oil; capacity: 100 gpm; set pressure: 210 psig; overpressure: 10%; "
               "constant back pressure: 35 psig; G = 0.96. K_w = 1.0, ΔP = 196 psi. A = 0.249 in² "
               "→ select a Series 900 OMNI-TRIM valve with an \"8\" orifice (0.307 in²). Because "
               "the back pressure is constant a conventional Style JOS or Series 900 may be used; "
               "Model 981105M-A."))

    # ---- Liquid, pilot operated ----------------------------------------------
    b.append(h2("Liquid Sizing — Pilot Operated Valves (Style JPVM)",
                "Định cỡ chất lỏng — van vận hành pilot (Style JPVM)"))
    b.append(note("Crosby Style JPVM pilot operated valves may be used on liquid service and "
                  "provide 30% greater capacity than spring loaded valves with liquid trim, "
                  "permitting a smaller valve. Viscosity should be no greater than 300 SSU (then "
                  "K_v = 1.0 may be used). See page 7-25 for two-phase flow."))
    b.append(eq('A = ' + _fr('GPM ' + _sq('G'), '36.81 K' + _sub('v') + ' ' + _sq('ΔP')), "5.5"))
    b.append(ul([
        "A — minimum required effective discharge area, in²",
        "G — specific gravity of the liquid at flowing conditions",
        "GPM — required relieving capacity, U.S. gallons per minute at flowing temperature",
        "ΔP — differential pressure (psi) = set pressure + overpressure − back pressure",
        "K_v — flow correction factor due to viscosity (page 7-7)",
    ]))
    b.append(h3("Example 1 — Liquid GPM, Crosby Style JPVM",
                "Ví dụ 1 — Chất lỏng GPM, van Style JPVM"))
    b.append(p("Fluid: Sodium Trisulfate; capacity: 125 GPM; set pressure: 100 psig; overpressure: "
               "10%; built-up back pressure: 0–30 psig; G = 1.23; K_v = 1.0; ΔP = 80 psi. A = "
               "0.421 in² → select a \"G\" orifice (0.503 in²), Model 1-1/2G3 Style JPVM-15."))

    # ---- Multiple valves ------------------------------------------------------
    b.append(h2("Multiple Valve Sizing", "Định cỡ nhiều van"))
    b.append(p("When multiple pressure relief valves are used, one valve shall be set at or below "
               "the MAWP and the remaining valve(s) may be set up to 5% over the MAWP. The total "
               "required area is calculated on an overpressure of 16% or 4 psi, whichever is "
               "greater. For fire exposure refer to liquid relief valve sizing under fire "
               "conditions (page 7-17)."))
    b.append(h3("Example 1 — Natural Gas", "Ví dụ 1 — Khí tự nhiên"))
    b.append(p("MAWP: 210 psig; capacity: 5,900 lb/hr; set pressure: 210 psig; overpressure: 16%; "
               "T = 580°R; molecular weight: 19.0. P₁ = 258.3 psia. A = 0.376 in² → select two "
               "\"E\" orifice valves (0.196 in² each, total 0.392 in²): one set at MAWP = 210 "
               "psig and one at 105% MAWP = 220.5 psig. Model 1E2 JOS-15-J."))
    b.append(h3("Example 2 — Air", "Ví dụ 2 — Khí"))
    b.append(p("Capacity: 150,000 lb/hr; set pressure: 200 psig; overpressure: 16%; T = 610°R; "
               "molecular weight: 28.97; P₁ = 246.7 psia; C = 356. A = 8.038 in². Select two \"N\" "
               "orifice valves (4.340 in² each, total 8.680 in²). Model 4N6 JOS-15-J."))

    # ---- Combination devices --------------------------------------------------
    b.append(h2("Combination Devices (Rupture Disc + Relief Valve)",
                "Thiết bị kết hợp (đĩa đứt + van xả áp)"))
    b.append(p("The rated relieving capacity of a pressure relief valve in combination with a "
               "rupture disc is equal to the capacity of the relief valve multiplied by a "
               "combination capacity factor to account for flow losses attributed to the rupture "
               "disc. When a tested combination factor for the specific rupture disc and relief "
               "valve is not available, a factor of 0.9 may be used. Tested factors are compiled "
               "by the National Board in NB-18."))
    b.append(h3("Example 1 — Gas/Vapor Mass Flow (lb/hr)",
                "Ví dụ 1 — Khí/hơi, lưu lượng khối lượng (lb/hr)"))
    b.append(p("Fluid: Natural Gas; capacity: 7,400 lb/hr; set pressure: 210 psig; overpressure: "
               "10%; T = 580°R; molecular weight: 19.0; P₁ = 245.7 psia; C = 344. A = 0.496 in². "
               "With a rupture disc combination factor of 0.9 the required area = 0.496/0.9 = "
               "0.551 in² → an \"H\" orifice (0.785 in²) is needed, one size larger. If a specific "
               "rupture disc with a combination factor of 0.986 or higher (with Crosby valves) is "
               "used, a larger size may not be necessary (see NB-18, Section IV)."))
    return "".join(b)
