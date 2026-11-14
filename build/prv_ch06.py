# -*- coding: utf-8 -*-
"""Book 4, Chapter 6 — Valve Sizing and Selection, Metric Units (EN/VI bilingual)."""

from prv_common import p, h2, h3, ul, note, eq

PAGES_SRC = 10
BYLINE = "Crosby Valve Inc. · Technical Document TP-V300"
TITLE_EN = "Valve Sizing and Selection — Metric Units"
TITLE_VI = "Định cỡ và lựa chọn van — Đơn vị hệ mét"


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
        return ("<b>Thuật ngữ chương 6.</b> kPag — kilopascal gauge · kPaa — kilopascal tuyệt "
                "đối · MAWP — áp suất làm việc cực đại cho phép · quá áp — vượt áp suất thiết lập · "
                "áp suất ngược (chép lên / tạo ra) · diện tích xả hiệu dụng (mm²) · K = 0,975 · "
                "K_b, K_sh, K_n, K_w, K_v — các hệ số hiệu chỉnh · CDTP — áp lực thử chênh lệch "
                "nguội · hệ số năng lực kết hợp.")
    return ("<b>Key terms.</b> kPag — kilopascal gauge · kPaa — kilopascal absolute · MAWP — "
            "maximum allowable working pressure · overpressure — above set pressure · back pressure "
            "(superimposed / built-up) · effective discharge area (mm²) · K = 0.975 · K_b, K_sh, "
            "K_n, K_w, K_v — correction factors · CDTP — cold differential test pressure · "
            "combination capacity factor.")


def body_vi():
    b = []
    b.append(p("Phần này hỗ trợ tính diện tích xả hiệu dụng tối thiểu cần thiết để van xả được lưu "
               "lượng chất lưu tại điều kiện xả dự kiến khi các thông số hệ thống biểu diễn bằng "
               "đơn vị mét (SI). Từ đó chọn kích cỡ và kiểu van có diện tích danh nghĩa lớn hơn "
               "hoặc bằng diện tích tính toán. Các giải thích chi tiết và ví dụ minh họa cho định "
               "cỡ USCS xem Chương 5."))
    b.append(p("Diện tích hiệu dụng của van Crosby được liệt kê ở trang 7-30 và 7-31. Các công "
               "thức và hệ số hiệu chỉnh phản ánh công nghệ định cỡ tiên tiến nhất, phù hợp ASME "
               "Section VIII và API RP 520. Việc chọn và định cỡ van là trách nhiệm của kỹ sư hệ "
               "thống và người sử dụng; không được dựa trên điều kiện giả định hay thông tin "
               "không đầy đủ."))

    # ---- Required sizing data -------------------------------------------------
    b.append(h2("Dữ liệu định cỡ cần thiết", "Required Sizing Data"))
    b.append(p("Dưới đây là danh sách các điều kiện vận hành cần cung cấp để định cỡ và chọn van "
               "xả áp đúng đắn."))
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
        "Áp suất vận hành (kPag tối đa)",
        "Nhiệt độ vận hành (°C tối đa)",
        "Áp suất làm việc cực đại cho phép (MAWP, kPag)",
    ]))
    b.append(h3("Điều kiện xả", "Relieving Conditions"))
    b.append(ul([
        "Lưu lượng xả cần thiết — khí (kg/hr), khí (Sm³/min), chất lỏng (liter/minute)",
        "Áp suất thiết lập (set pressure, kPag)",
        "Tỷ lệ quá áp cho phép (%)",
        "Áp suất ngược chép lên (kPag) — chỉ rõ không đổi hay biến thiên",
        "Áp suất ngược tạo ra (kPag)",
        "Nhiệt độ xả (°C)",
    ]))

    # ---- Gas / vapor, kg/hr ---------------------------------------------------
    b.append(h2("Định cỡ khí và hơi — quá áp 10% (kg/hr)",
                "Gas and Vapor Sizing — 10% Overpressure (kg/hr)"))
    b.append(p("Công thức dùng cho khí và hơi (trừ hơi nước) khi lưu lượng biểu diễn dưới dạng "
               "lưu lượng khối lượng, kilogram trên giờ. Kết quả tính bằng milimét vuông (mm²)."))
    b.append(eq('A = ' + _fr('13160 W ' + _sq('T Z'),
                             'C K P' + _sub('1') + ' K' + _sub('b') + ' ' + _sq('M')), "6.1"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, mm²",
        "W — lưu lượng xả cần thiết, kg/hr",
        "T — nhiệt độ tuyệt đối tại đầu vào van, K = °C + 273",
        "Z — hệ số nén (Hình F7-1); Z = 1,0 nếu không biết",
        "C — hệ số từ tỷ số nhiệt dung riêng (Bảng T7-7); C = 315 nếu không biết",
        "K = 0,975",
        "K_b — hệ số hiệu chỉnh áp suất ngược (Bảng T7-1; Hình F7-2 cho bellows/Series BP)",
        "M — khối lượng phân tử (Bảng T7-7)",
        "P" + _sub("1") + " — áp suất xả tuyệt đối, kPaa = áp suất thiết lập + quá áp + khí quyển (101 kPa)",
    ]))
    b.append(h3("Ví dụ 1 — Áp suất ngược khí quyển", "Example 1 — Atmospheric Back Pressure"))
    b.append(p("Khí tự nhiên; 2.675 kg/hr; 1450 kPag; 10%; 50°C; M = 19. T = 323 K, P₁ = 1696 "
               "kPaa, A = 255 mm². Chọn 1-1/2G2-1/2 Style JOS-15, nắp Type J (lỗ \"G\" 325 mm²). "
               "Vật liệu tiêu chuẩn thỏa mãn."))
    b.append(h3("Ví dụ 2 — Áp suất ngược chép lên không đổi",
                "Example 2 — Superimposed Constant Back Pressure"))
    b.append(p("Như Ví dụ 1 nhưng áp suất ngược chép lên 1345 kPag. Tỷ lệ áp suất ngược = (1345 + "
               "101)/(1450 + 145 + 101) = 85,3%; K_b = 0,76. A = 335 mm². Chọn 1-1/2H3 JOS-15, "
               "nắp Type J (lỗ \"H\" 506 mm²). CDTP = 105 kPag; dưới thực tế van mở tại 1450 kPag "
               "(= 105 + 1345)."))
    b.append(h3("Ví dụ 3 — Áp suất thiết lập dưới 30 psig (207 kPag)",
                "Example 3 — Set Pressure Below 30 psig (207 kPag)"))
    b.append(p("ASME VIII quy định quá áp tối đa 3 psi (20,7 kPa) khi áp suất thiết lập < 30 psig. "
               "Khí (tem UV); 227 kg/hr; 138 kPag; 20,7 kPa; T = 294 K; P₁ = 259,7 kPaa. A tính "
               "được (lỗ N°7 126 mm²). Chọn Series 900 1\"×1-1/2\" — Model 972103M-D."))
    b.append(h3("Ví dụ 4 — Áp suất ngược chép lên biến thiên",
                "Example 4 — Variable Superimposed Back Pressure"))
    b.append(p("Khí (tem UV); 127 kg/hr; 400 kPag; áp suất ngược 0–140 kPag; 60°C; T = 333 K; "
               "P₁ = 541 kPaa; K_b = 0,650 (Bảng F7-2 cho BP-Omni). A = 46,42 mm². Chọn Series "
               "BP 3/4\"×1\" lỗ 47,74 mm² — Model BP51701M-D."))

    # ---- Gas / vapor, Sm3/min -------------------------------------------------
    b.append(h2("Định cỡ khí và hơi — quá áp 10% (Sm³/min)",
                "Gas and Vapor Sizing — 10% Overpressure (Sm³/min)"))
    b.append(p("Công thức dùng cho khí và hơi khi lưu lượng biểu diễn dưới dạng lưu lượng thể "
               "tích, Sm³/min. Kết quả tính bằng mm²."))
    b.append(eq('A = ' + _fr('179400 Q ' + _sq('T G Z'),
                             'C K P' + _sub('1') + ' K' + _sub('b')), "6.2"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, mm²",
        "Q — lưu lượng xả cần thiết, Sm³/min",
        "T — nhiệt độ tuyệt đối, K = °C + 273",
        "G — tỷ trọng khí so với không khí",
        "Z — hệ số nén (Hình F7-1); Z = 1,0 nếu không biết",
        "C — hệ số từ tỷ số nhiệt dung riêng (Bảng T7-7); C = 315 nếu không biết",
        "K = 0,975; K_b — hệ số hiệu chỉnh áp suất ngược",
        "P" + _sub("1") + " — áp suất xả tuyệt đối, kPaa",
    ]))
    b.append(h3("Ví dụ — Áp suất ngược tạo ra biến thiên",
                "Example — Built-up Variable Back Pressure"))
    b.append(p("Khí ethylene; 326 Sm³/min; 1170 kPag; 10%; 93°C; G = 0,968. T = 366 K, P₁ = 1388 "
               "kPaa, K_b = 0,896 (bellows, Hình F7-2). Van thường: A = 2662 mm² → 4N6 JBS-15, "
               "nắp Type L. Van pilot JPV: K_b không áp dụng, A = 2386 mm² → 4N6 JPV-15."))

    # ---- Steam ----------------------------------------------------------------
    b.append(h2("Định cỡ hơi nước — quá áp 10% (kg/hr)",
                "Steam Sizing — 10% Overpressure (kg/hr)"))
    b.append(p("Công thức dựa trên công thức thực nghiệm Napier cho dòng hơi, kết quả tính bằng "
               "mm². ASME yêu cầu thêm K_n khi P₁ vượt 10.340 kPaa."))
    b.append(eq('A = ' + _fr('190.4 W', 'K P' + _sub('1') + ' K' + _sub('sh')
                             + ' K' + _sub('n') + ' K' + _sub('b')), "6.3"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, mm²",
        "W — lưu lượng xả cần thiết, kg/hr",
        "K = 0,975",
        "P" + _sub("1") + " — áp suất xả tuyệt đối, kPaa",
        "K_sh — hệ số quá nhiệt (Bảng T7-2); K_sh = 1,00 cho hơi bão hòa",
        "K_n — hơi khô bão hòa khi áp suất thiết lập > 10.346 kPaa (Hình F7-4)",
        "K_b — hệ số hiệu chỉnh áp suất ngược",
    ]))
    b.append(h3("Ví dụ 1 — Hơi bão hòa", "Example 1 — Saturated Steam"))
    b.append(p("9.750 kg/hr; 1550 kPag; P₁ = 1806 kPaa. A = 1054 mm² → 3K4 JOS-15, đòn bẩy Type "
               "C (lỗ \"K\" 1186 mm²)."))
    b.append(h3("Ví dụ 2 — Hơi quá nhiệt", "Example 2 — Superheated Steam"))
    b.append(p("49.200 kg/hr; 400°C; 3670 kPag; P₁ = 4138 kPaa; K_sh = 0,844. A = 2751 mm² → "
               "4N6 JOS-46, đòn bẩy Type C, lò xo thép hợp kim."))
    b.append(h3("Ví dụ 3 — Hơi bão hòa tại áp suất xả > 1500 psig (103 Barg)",
                "Example 3 — Saturated Steam > 1500 psig (103 Barg)"))
    b.append(p("39.900 kg/hr; 18.960 kPag; P₁ = 20.957 kPaa; K_n = 1,154. A = 322 mm² → 2G3 "
               "JOS-H-76, đòn bẩy Type C, lò xo thép hợp kim."))

    # ---- Liquid, spring loaded ------------------------------------------------
    b.append(h2("Định cỡ chất lỏng — van lò xo (Spring Loaded)",
                "Liquid Sizing — Spring Loaded Valves"))
    b.append(p("Công thức áp dụng cho JLT-JOS, JLT-JBS, Series 900 và Series BP theo ASME "
               "Section VIII. Không định cỡ với quá áp dưới 10%. Kết quả tính bằng mm²."))
    b.append(eq('A = ' + _fr('15.9 Q ' + _sq('G'),
                             'K' + _sub('w') + ' K' + _sub('v') + ' ' + _sq('ΔP')), "6.4"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, mm²",
        "Q — lưu lượng xả cần thiết, liter/minute tại nhiệt độ chảy",
        "G — tỷ trọng chất lỏng tại điều kiện chảy",
        "ΔP — chênh áp (kPa) = áp suất thiết lập + quá áp − áp suất ngược",
        "K_v — hệ số hiệu chỉnh độ nhớt (trang 7-7)",
        "K_w — hệ số hiệu chỉnh áp suất ngược cho van bellows/Series BP (Hình F7-3)",
    ]))
    b.append(h3("Ví dụ 1 — Chất lỏng (liter/min)", "Example 1 — Liquid, liters/minute"))
    b.append(p("Natri trisunfat; 475 L/min; 690 kPag; áp suất ngược 0–207 kPag; G = 1,23; K_w = "
               "0,866; ΔP = 552 kPa. A = 412 mm² → lỗ \"H\" 506 mm². Vì áp suất ngược tạo ra > "
               "10% nên cần bellows Style JBS; Model 1-1/2H3 JLT-JBS-15, nắp Type J."))
    b.append(h3("Ví dụ 2 — Chất lỏng (liter/min)", "Example 2 — Liquid, liters/minute"))
    b.append(p("Dầu thầu dầu; 380 L/min; 1450 kPag; áp suất ngược 240 kPag (không đổi); G = "
               "0,96; K_w = 1,0; ΔP = 1355 kPa. A = 160,8 mm² → Series 900 OMNI-TRIM lỗ \"8\" "
               "198 mm² — Model 981105M-A."))

    # ---- Liquid, pilot operated ----------------------------------------------
    b.append(h2("Định cỡ chất lỏng — van vận hành pilot (Style JPVM)",
                "Liquid Sizing — Pilot Operated Valves (Style JPVM)"))
    b.append(note("Van pilot Style JPVM cho chất lỏng có năng lực lớn hơn 30% so với van lò xo "
                  "trim lỏng. Nên giữ độ nhớt ≤ 300 SSU (khi đó K_v = 1,0). Xem trang 7-25 về "
                  "dòng hai pha."))
    b.append(eq('A = ' + _fr('12.16 Q ' + _sq('G'), 'K' + _sub('v') + ' ' + _sq('ΔP')), "6.5"))
    b.append(ul([
        "A — diện tích xả hiệu dụng tối thiểu, mm²",
        "Q — lưu lượng xả cần thiết, liter/minute tại nhiệt độ chảy",
        "G — tỷ trọng chất lỏng tại điều kiện chảy",
        "ΔP — chênh áp (kPa) = áp suất thiết lập + quá áp − áp suất ngược",
        "K_v — hệ số hiệu chỉnh độ nhớt (trang 7-7)",
    ]))
    b.append(h3("Ví dụ — Chất lỏng L/min, van Style JPVM",
                "Example — Liquid L/min, Crosby Style JPVM"))
    b.append(p("Natri trisunfat; 475 L/min; 690 kPag; G = 1,23; K_v = 1,0; ΔP = 552 kPa. A = "
               "273 mm² → lỗ \"G\" 325 mm², Model 1-1/2G3 Style JPVM-15."))

    # ---- Multiple valves ------------------------------------------------------
    b.append(h2("Định cỡ nhiều van", "Multiple Valve Sizing"))
    b.append(p("Một van đặt tại hoặc dưới MAWP, các van còn lại đến 5% MAWP. Tổng diện tích tính "
               "với quá áp 16% hoặc 27,58 kPa (lấy giá trị lớn hơn). Xét hỏa hoạn xem trang 7-17."))
    b.append(h3("Ví dụ 1 — Khí tự nhiên", "Example 1 — Natural Gas"))
    b.append(p("MAWP: 1450 kPag; 2675 kg/hr; 1450 kPag; 16%; 50°C; M = 19. P₁ = 1783 kPaa. A = "
               "242,7 mm² → hai van lỗ \"E\" (126 mm² mỗi lỗ); một tại MAWP = 1450 kPag, một tại "
               "105% MAWP = 1522 kPag. Model 1E2 JOS-15-J."))
    b.append(h3("Ví dụ 2 — Khí", "Example 2 — Air"))
    b.append(p("68.038,9 kg/hr; 1379 kPag; 16%; 66°C; T = 339 K; C = 356; P₁ = 1701 kPaa. A = "
               "5188 mm² → hai van lỗ \"N\" (2800 mm² mỗi lỗ, tổng 5600 mm²). Model 4N6 JOS-15-J."))

    # ---- Combination devices --------------------------------------------------
    b.append(h2("Thiết bị kết hợp (đĩa đứt + van xả áp)",
                "Combination Devices (Rupture Disc + Relief Valve)"))
    b.append(p("Năng lực xả định mức của van kết hợp đĩa đứt bằng năng lực van nhân với hệ số "
               "năng lực kết hợp. Khi không có hệ số đã thử, dùng 0,9. Các hệ số thử nghiệm tập "
               "hợp trong NB-18 của National Board."))
    b.append(h3("Ví dụ 1 — Khí/hơi, lưu lượng khối lượng (kg/hr)",
                "Example 1 — Gas/Vapor Mass Flow (kg/hr)"))
    b.append(p("Khí tự nhiên; 3350 kg/hr; 1450 kPag; 10%; 50°C; M = 19,0; A = 319,9 mm². Với đĩa "
               "đứt hệ số 0,9, diện tích yêu cầu = 319,9/0,9 = 355,4 mm² → cần lỗ \"H\" 506 mm², "
               "tăng một cỡ. Nếu đĩa đứt cụ thể có hệ số ≥ 0,986 thì không cần tăng cỡ (xem "
               "NB-18, Mục IV)."))
    return "".join(b)


def body_en():
    b = []
    b.append(p("This section is provided to assist in calculating the required effective area of a "
               "pressure relief valve that will flow the required volume of system fluid at "
               "anticipated relieving conditions when system parameters are expressed in metric "
               "units. The valve size and style are then selected to have a nominal effective "
               "area equal to or greater than the calculated value. Detailed explanations and "
               "examples for U.S.C.S. sizing are in Chapter 5."))
    b.append(p("Effective areas for Crosby valves are shown on pages 7-30 and 7-31. The basic "
               "formulae and capacity correction factors reflect current state-of-the-art "
               "technology and are consistent with ASME Section VIII and API RP 520. Valve "
               "selection and sizing is the responsibility of the system engineer and the user and "
               "must not be based on arbitrarily assumed conditions or incomplete information."))

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
        "Operating pressure (kPag maximum)",
        "Operating temperature (°C maximum)",
        "Maximum allowable working pressure, MAWP (kPag)",
    ]))
    b.append(h3("Relieving Conditions", "Điều kiện xả"))
    b.append(ul([
        "Required relieving capacity — gas or vapor (kg/hr), gas or vapor (Sm³/min), liquid (liter/minute)",
        "Set pressure (kPag)",
        "Allowable overpressure (%)",
        "Superimposed back pressure (kPag) — specify constant or variable",
        "Built-up back pressure (kPag)",
        "Relieving temperature (°C)",
    ]))

    # ---- Gas / vapor, kg/hr ---------------------------------------------------
    b.append(h2("Gas and Vapor Sizing — 10% Overpressure (kg/hr)",
                "Định cỡ khí và hơi — quá áp 10% (kg/hr)"))
    b.append(p("This formula is used for gases and vapor (except steam) when required flow is "
               "expressed as a mass flow rate, kilograms per hour. The area is in square "
               "millimeters (mm²)."))
    b.append(eq('A = ' + _fr('13160 W ' + _sq('T Z'),
                             'C K P' + _sub('1') + ' K' + _sub('b') + ' ' + _sq('M')), "6.1"))
    b.append(ul([
        "A — minimum required effective discharge area, mm²",
        "W — required relieving capacity, kg/hr",
        "T — absolute temperature at the valve inlet, K = °C + 273",
        "Z — compressibility factor (Figure F7-1); use Z = 1.0 if unknown",
        "C — coefficient from the ratio of specific heats (Table T7-7); use C = 315 if unknown",
        "K = 0.975",
        "K_b — capacity correction factor for back pressure (Table T7-1; Figure F7-2 for bellows/Series BP)",
        "M — molecular weight of the gas or vapor (Table T7-7)",
        "P" + _sub("1") + " — relieving pressure, kPaa = set pressure + overpressure + atmospheric (101 kPa)",
    ]))
    b.append(h3("Example 1 — Atmospheric Back Pressure", "Ví dụ 1 — Áp suất ngược khí quyển"))
    b.append(p("Natural Gas; 2,675 kg/hr; set pressure: 1450 kPag; overpressure: 10%; 50°C; "
               "molecular weight: 19. T = 323 K, P₁ = 1696 kPaa, A = 255 mm². Select a 1-1/2G2-1/2 "
               "Style JOS-15 with Type J cap (the \"G\" orifice is 325 mm²). Standard materials "
               "are satisfactory."))
    b.append(h3("Example 2 — Superimposed Constant Back Pressure",
                "Ví dụ 2 — Áp suất ngược chép lên không đổi"))
    b.append(p("Same as Example 1 but with a superimposed constant back pressure of 1345 kPag. "
               "Back-pressure percentage = (1345 + 101)/(1450 + 145 + 101) = 85.3%; K_b = 0.76. "
               "A = 335 mm². Select a 1-1/2H3 Style JOS-15 with Type J cap (the \"H\" orifice is "
               "506 mm²). CDTP = 105 kPag; under service the valve opens at 1450 kPag (= 105 + "
               "1345)."))
    b.append(h3("Example 3 — Set Pressure Below 30 psig (207 kPag)",
                "Ví dụ 3 — Áp suất thiết lập dưới 30 psig (207 kPag)"))
    b.append(p("ASME Section VIII specifies a maximum allowable overpressure of 3 psi (20.7 kPa) "
               "for set pressures below 30 psig. Air (UV stamp); 227 kg/hr; set pressure: 138 "
               "kPag; overpressure: 20.7 kPa; T = 294 K; P₁ = 259.7 kPaa. A fits the No. 7 (126 "
               "mm²) orifice. Select a 1\"×1-1/2\" Series 900 valve — Model 972103M-D."))
    b.append(h3("Example 4 — Variable Superimposed Back Pressure",
                "Ví dụ 4 — Áp suất ngược chép lên biến thiên"))
    b.append(p("Air (UV stamp); 127 kg/hr; set pressure: 400 kPag; back pressure: 0–140 kPag; "
               "60°C; T = 333 K; P₁ = 541 kPaa; K_b = 0.650 (Table F7-2 for BP-Omni). A = 46.42 "
               "mm². Select a 3/4\"×1\" Series BP with a 47.74 mm² orifice — Model BP51701M-D."))

    # ---- Gas / vapor, Sm3/min -------------------------------------------------
    b.append(h2("Gas and Vapor Sizing — 10% Overpressure (Sm³/min)",
                "Định cỡ khí và hơi — quá áp 10% (Sm³/min)"))
    b.append(p("This formula is used for gases and vapor when required flow is expressed as a "
               "volumetric flow rate, Sm³/min. The area is in mm²."))
    b.append(eq('A = ' + _fr('179400 Q ' + _sq('T G Z'),
                             'C K P' + _sub('1') + ' K' + _sub('b')), "6.2"))
    b.append(ul([
        "A — minimum required effective discharge area, mm²",
        "Q — required relieving capacity, standard cubic meters per minute (Sm³/min)",
        "T — absolute temperature, K = °C + 273",
        "G — specific gravity of the gas or vapor (relative to air)",
        "Z — compressibility factor (Figure F7-1); use Z = 1.0 if unknown",
        "C — coefficient from the ratio of specific heats (Table T7-7); use C = 315 if unknown",
        "K = 0.975; K_b — capacity correction factor for back pressure",
        "P" + _sub("1") + " — relieving pressure, kPaa",
    ]))
    b.append(h3("Example — Built-up Variable Back Pressure",
                "Ví dụ — Áp suất ngược tạo ra biến thiên"))
    b.append(p("Ethylene Gas; 326 Sm³/min; set pressure: 1170 kPag; overpressure: 10%; 93°C; "
               "specific gravity: 0.968. T = 366 K, P₁ = 1388 kPaa, K_b = 0.896 (bellows style, "
               "Figure F7-2). Standard valve: A = 2662 mm² → select a 4N6 JBS-15, Type L cap. "
               "Pilot Style JPV: K_b is not applicable, A = 2386 mm² → select a 4N6 JPV-15."))

    # ---- Steam ----------------------------------------------------------------
    b.append(h2("Steam Sizing — 10% Overpressure (kg/hr)",
                "Định cỡ hơi nước — quá áp 10% (kg/hr)"))
    b.append(p("This formula is based on the empirical Napier formula for steam flow (area in "
               "mm²). An additional factor K_n is required by ASME when the relieving pressure "
               "(P₁) is above 10,340 kPaa."))
    b.append(eq('A = ' + _fr('190.4 W', 'K P' + _sub('1') + ' K' + _sub('sh')
                             + ' K' + _sub('n') + ' K' + _sub('b')), "6.3"))
    b.append(ul([
        "A — minimum required effective discharge area, mm²",
        "W — required relieving capacity, kg/hr",
        "K = 0.975",
        "P" + _sub("1") + " — relieving pressure, kPaa",
        "K_sh — superheat correction factor (Table T7-2); K_sh = 1.00 for saturated steam",
        "K_n — dry saturated steam at set pressures above 10,346 kPaa (Figure F7-4)",
        "K_b — capacity correction factor for back pressure",
    ]))
    b.append(h3("Example 1 — Saturated Steam", "Ví dụ 1 — Hơi bão hòa"))
    b.append(p("9,750 kg/hr; set pressure: 1550 kPag; P₁ = 1806 kPaa. A = 1054 mm² → select a "
               "\"K\" orifice (1186 mm²), Model 3K4 JOS-15 with Type C lever."))
    b.append(h3("Example 2 — Superheated Steam", "Ví dụ 2 — Hơi quá nhiệt"))
    b.append(p("49,200 kg/hr; relieving temp: 400°C; set pressure: 3670 kPag; P₁ = 4138 kPaa; "
               "K_sh = 0.844. A = 2751 mm² → select a 4N6 JOS-46 with Type C lever and alloy "
               "steel spring."))
    b.append(h3("Example 3 — Saturated Steam at Relieving Pressure > 1500 psig (103 Barg)",
                "Ví dụ 3 — Hơi bão hòa tại áp suất xả > 1500 psig (103 Barg)"))
    b.append(p("39,900 kg/hr; set pressure: 18,960 kPag; P₁ = 20,957 kPaa; K_n = 1.154. A = 322 "
               "mm² → select a \"G\" orifice (325 mm²), Model 2G3 JOS-H-76 with Type C lever and "
               "alloy steel spring."))

    # ---- Liquid, spring loaded ------------------------------------------------
    b.append(h2("Liquid Sizing — Spring Loaded Valves",
                "Định cỡ chất lỏng — van lò xo (Spring Loaded)"))
    b.append(p("This formula applies to Styles JLT-JOS, JLT-JBS, Series 900 and Series BP, per "
               "ASME Section VIII. Sizing is not permitted for overpressures less than 10%. The "
               "area is in mm²."))
    b.append(eq('A = ' + _fr('15.9 Q ' + _sq('G'),
                             'K' + _sub('w') + ' K' + _sub('v') + ' ' + _sq('ΔP')), "6.4"))
    b.append(ul([
        "A — minimum required effective discharge area, mm²",
        "Q — required relieving capacity, liters per minute at flowing temperature",
        "G — specific gravity of the liquid at flowing conditions",
        "ΔP — differential pressure (kPa) = set pressure + overpressure − back pressure",
        "K_v — flow correction factor due to viscosity (page 7-7)",
        "K_w — capacity correction factor for back pressure on bellows or Series BP valves (Figure F7-3)",
    ]))
    b.append(h3("Example 1 — Liquid, liters/minute", "Ví dụ 1 — Chất lỏng (liter/min)"))
    b.append(p("Sodium Trisulfate; 475 L/min; set pressure: 690 kPag; built-up back pressure: "
               "0–207 kPag; G = 1.23; K_w = 0.866; ΔP = 552 kPa. A = 412 mm² → select an \"H\" "
               "orifice (506 mm²). Because built-up back pressure exceeds 10%, a bellows Style JBS "
               "is required; Model 1-1/2H3 JLT-JBS-15 with Type J cap."))
    b.append(h3("Example 2 — Liquid, liters/minute", "Ví dụ 2 — Chất lỏng (liter/min)"))
    b.append(p("Castor Oil; 380 L/min; set pressure: 1450 kPag; constant back pressure: 240 kPag; "
               "G = 0.96; K_w = 1.0; ΔP = 1355 kPa. A = 160.8 mm² → select a Series 900 "
               "OMNI-TRIM valve with an \"8\" orifice (198 mm²) — Model 981105M-A."))

    # ---- Liquid, pilot operated ----------------------------------------------
    b.append(h2("Liquid Sizing — Pilot Operated Valves (Style JPVM)",
                "Định cỡ chất lỏng — van vận hành pilot (Style JPVM)"))
    b.append(note("Crosby Style JPVM pilot operated valves may be used on liquid service and "
                  "provide 30% greater capacity than spring loaded valves with liquid trim. "
                  "Viscosity should be no greater than 300 SSU (then K_v = 1.0 may be used). See "
                  "page 7-25 for two-phase flow."))
    b.append(eq('A = ' + _fr('12.16 Q ' + _sq('G'), 'K' + _sub('v') + ' ' + _sq('ΔP')), "6.5"))
    b.append(ul([
        "A — minimum required effective discharge area, mm²",
        "Q — required relieving capacity, liters per minute at flowing temperature",
        "G — specific gravity of the liquid at flowing conditions",
        "ΔP — differential pressure (kPa) = set pressure + overpressure − back pressure",
        "K_v — flow correction factor due to viscosity (page 7-7)",
    ]))
    b.append(h3("Example — Liquid L/min, Crosby Style JPVM",
                "Ví dụ — Chất lỏng L/min, van Style JPVM"))
    b.append(p("Sodium Trisulfate; 475 L/min; set pressure: 690 kPag; G = 1.23; K_v = 1.0; ΔP = "
               "552 kPa. A = 273 mm² → select a \"G\" orifice (325 mm²), Model 1-1/2G3 Style "
               "JPVM-15."))

    # ---- Multiple valves ------------------------------------------------------
    b.append(h2("Multiple Valve Sizing", "Định cỡ nhiều van"))
    b.append(p("When multiple pressure relief valves are used, one valve shall be set at or below "
               "the MAWP and the remaining valve(s) may be set up to 5% over the MAWP. The total "
               "required area is calculated on an overpressure of 16% or 27.58 kPa, whichever is "
               "greater. For fire exposure refer to page 7-17."))
    b.append(h3("Example 1 — Natural Gas", "Ví dụ 1 — Khí tự nhiên"))
    b.append(p("MAWP: 1450 kPag; 2,675 kg/hr; set pressure: 1450 kPag; overpressure: 16%; 50°C; "
               "molecular weight: 19.0. P₁ = 1783 kPaa. A = 242.7 mm² → select two \"E\" orifice "
               "valves (126 mm² each); one set at MAWP = 1450 kPag and one at 105% MAWP = 1522 "
               "kPag. Model 1E2 JOS-15-J."))
    b.append(h3("Example 2 — Air", "Ví dụ 2 — Khí"))
    b.append(p("68,038.9 kg/hr; set pressure: 1379 kPag; overpressure: 16%; 66°C; T = 339 K; C = "
               "356; P₁ = 1701 kPaa. A = 5188 mm² → select two \"N\" orifice valves (2800 mm² "
               "each, total 5600 mm²). Model 4N6 JOS-15-J."))

    # ---- Combination devices --------------------------------------------------
    b.append(h2("Combination Devices (Rupture Disc + Relief Valve)",
                "Thiết bị kết hợp (đĩa đứt + van xả áp)"))
    b.append(p("The rated relieving capacity of a pressure relief valve in combination with a "
               "rupture disc is equal to the capacity of the relief valve multiplied by a "
               "combination capacity factor. When a tested factor is not available, a factor of "
               "0.9 may be used. Tested factors are compiled by the National Board in NB-18."))
    b.append(h3("Example 1 — Gas/Vapor Mass Flow (kg/hr)",
                "Ví dụ 1 — Khí/hơi, lưu lượng khối lượng (kg/hr)"))
    b.append(p("Natural Gas; 3,350 kg/hr; set pressure: 1450 kPag; overpressure: 10%; 50°C; "
               "molecular weight: 19.0; A = 319.9 mm². With a rupture disc combination factor of "
               "0.9 the required area = 319.9/0.9 = 355.4 mm² → an \"H\" orifice (506 mm²) is "
               "needed, one size larger. If a specific rupture disc with a combination factor of "
               "0.986 or higher is used, a larger size may not be necessary (see NB-18, Section "
               "IV)."))
    return "".join(b)
