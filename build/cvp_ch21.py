# -*- coding: utf-8 -*-
"""Book 7, Chapter 21 - The ABC Method for Estimating Hydrodynamic Sound Level
(EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
133-135 (PDF pp. 133-135). Three printed pages, one table (Table 21-1), no
figures and no numbered equations. The OCR text layer garbles the printed
formulas; the printed forms were transcribed from page renders of all three
pages, including the radical in E = 45 (1/√X_Fz) and the four-entry Globe
Valve row of Table 21-1.
"""
from cvp_common import eq, h2, h3, note, p, table

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "The ABC Method for Estimating Hydrodynamic Sound Level"
TITLE_VI = "Phương pháp ABC ước tính mức âm thanh thủy động"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 21.</b> phương pháp ABC (ABC method) · "
                "mức âm thanh thủy động (hydrodynamic sound level) · tiếng ồn "
                "khí động học (aerodynamic phenomena) · chất lưu rối "
                "(turbulent fluid) · số Reynolds · xâm thực (cavitation) · "
                "bắt đầu xâm thực (incipient cavitation) · hóa hơi (flashing) · "
                "đế van (seat) · van một cổng ra (single-outlet ported valve) · "
                "van cầu (globe valve) · van có đường chảy thẳng (line-of-sight "
                "valve) · bộ lót nhiều cổng (multiported trim) · điện trở mắc "
                "nối tiếp (resistance-in-series) · hệ số lưu lượng Cᵥ · hệ số "
                "phục hồi áp suất F_L · hệ số bắt đầu xâm thực X_Fz · áp suất "
                "hơi P_v · tỷ số áp suất X · Xy tại xâm thực cực đại · số mũ E · "
                "hệ số kiểu van r_w · mức áp suất âm thanh L_pAe1m · dBA · "
                "đường kính ống D · độ dày ống (pipe schedule) · khối lượng "
                "riêng chất lỏng ρ_liq · tốc độ âm c_liq · psi tuyệt đối (psia)")
    return ("<b>Key terms.</b> ABC method · hydrodynamic sound level · "
            "aerodynamic phenomena · turbulent fluid · Reynolds number · "
            "cavitation · incipient cavitation · flashing · seat · "
            "single-outlet ported valve · globe valve · line-of-sight valve · "
            "multiported trim · resistance-in-series trim · flow coefficient "
            "Cᵥ · pressure recovery factor F_L · coefficient of incipient "
            "cavitation X_Fz · liquid vapor pressure P_v · pressure ratio X · "
            "Xy at maximum cavitation · exponent E · valve type modifier r_w · "
            "sound pressure level L_pAe1m · dBA · pipe diameter D · pipe "
            "schedule · liquid density ρ_liq · speed of sound c_liq · psia")


def body_vi():
    b = []
    b.append(h2("Tuyên bố miễn trừ", "Disclaimer"))

    b.append(p("<b>Tuyên bố miễn trừ.</b> Phương pháp đề xuất chỉ hợp lệ với "
               "van điều khiển có một cổng ra, chẳng hạn van cầu hoặc van có "
               "đường chảy thẳng, với chất lưu rối (Rev > 10.000). Lưu ý: xâm "
               "thực, dù phổ biến nhất với nước, cũng có thể xảy ra với các "
               "chất lưu khác như dầu thô."))
    b.append(p("Các bộ lót giảm ồn như bộ lót nhiều cổng hay dạng điện trở mắc "
               "nối tiếp được trình bày trong Chương 20."))
    b.append(p("Tương tự như phương pháp ABC cho chất khí, phương pháp này "
               "không chỉ dự đoán tiếng ồn của chất lưu rối mà còn dự đoán "
               "chính xác các nguồn âm bổ sung do chất lưu bị xâm thực phát "
               "ra (thực chất là hiện tượng khí động học)."))
    b.append(p("Đường kính ống phía sau van D tính bằng inch (D = d / 25.4 nếu "
               "d tính bằng mm), P₁ tính bằng psia (bara × 14.5), P₂ tính bằng "
               "psia (bara × 14.5)."))
    b.append(eq("D = d / 25.4  (d tính bằng mm)"))
    b.append(eq("P₁ [psia] = p [bara] × 14.5;  P₂ [psia] = p [bara] × 14.5"))

    b.append(h3("Dữ liệu cần có", "Input Needed"))
    b.append(p("Cᵥ = hệ số lưu lượng (trong điều kiện vận hành)."))
    b.append(p("F_L = hệ số phục hồi áp suất khi không có bộ khuếch tán, tại "
               "vị trí hành trình thực tế."))
    b.append(p("X_Fz = hệ số bắt đầu xâm thực (xem Bảng 21-1)."))
    b.append(p("P_v = áp suất hơi của chất lỏng, tính bằng psia."))
    b.append(p("r_w = hệ số kiểu van (bằng 3 đối với van cầu)."))

    b.append(h3("Tính toán ban đầu", "Initial Calculations"))
    b.append(eq("X = (P₁ − P₂) / (P₁ − P_v)"))
    b.append(eq("Xy = X tại xâm thực cực đại = (1 + X_Fz) / 2"))
    b.append(eq("E = số mũ = 45 (1/√X_Fz)"))

    b.append(h3("Các bước tính toán", "Calculation Steps"))
    b.append(eq("A = 8 log(D) + 12 log(Cᵥ/D²) + 4  dB"))
    b.append(p("Trong đó A được tính bằng dB, với D là đường kính ống tính "
               "bằng inch."))
    b.append(eq("B = 35 log(P₁) − 35 (đơn vị Mỹ), hoặc 35 log(14.5 p) − 35 "
                "nếu p tính bằng bara"))
    b.append(eq("c₁ = 30 log(10X),  X cực đại = F_L²"))
    b.append(p("Phương trình này cho mức ồn rối, tính bằng dBA tại 1 m."))
    b.append(eq("c₂ = 60 log(X / X_Fz)  nếu X cao hơn X_Fz nhưng thấp hơn Xy"))
    b.append(eq("c₂ = 60 log(Xy / X_Fz)  nếu X cao hơn Xy; nếu không thì dùng zero"))
    b.append(p("Giá trị này xác định mức âm tăng dần do xâm thực, tính bằng dB."))
    b.append(eq("c₃ = E log(X / Xy)  nếu X lớn hơn Xy; nếu không thì dùng zero"))
    b.append(p("Giá trị này biểu thị mức âm giảm dần do xâm thực, tính bằng dB."))
    b.append(eq("C = c₁ + c₂ − c₃  dBA"))
    b.append(eq("L_pAe1m = A + B + C − r_w  dBA tại 1 m, cộng thêm các hệ số "
                "hiệu chỉnh"))

    b.append(p("Các hệ số X_Fz được lấy từ Bảng 21-1 dưới đây."))
    b.append(table(
        ["Cᵥ/D² (D tính bằng inch)", "3", "6", "9", "12", "15", "18", "21",
         "24", "27", "30"],
        [["Cᵥ/d² × 10³ (mm)", "4.64", "9.3", "14", "18.6", "23.3", "28",
          "32.6", "37.2", "42", "54"],
         ["Van cầu, nút parabol", "0.78", "0.68", "0.49", "0.30", "", "",
          "", "", "", ""],
         ["Van bướm", "0.45", "0.30", "0.23", "0.21", "0.20", "0.19",
          "0.18", "0.17", "0.16", "0.15"],
         ["Van bi phân đoạn", "0.46", "0.30", "0.22", "0.20", "0.18", "0.17",
          "0.15", "0.13", "0.12", "0.19"]],
        "Bảng 21-1. Bảng tra cứu các hệ số X_Fz."))

    b.append(h3("Các hệ số hiệu chỉnh", "Modifiers"))
    b.append(eq("Schedule 40 = 0;  schedule 80 = −3 dB;  schedule 160 = −6 dB"))
    b.append(p("Đối với chất lỏng khác nước, cộng thêm:"))
    b.append(eq("20 log[(62.5 / ρ_liq) + 25 log(4750 / c_liq)]"))
    b.append(p("Trong đó ρ_liq là khối lượng riêng của chất lỏng đã chọn "
               "(lb/ft³), còn c_liq là tốc độ âm của chất lỏng đã chọn (ft/s)."))
    b.append(p("Đối với vật liệu ống khác thép, cộng thêm:"))
    b.append(eq("20 log(7800 / ρ_material)"))
    b.append(p("Trong đó ρ_material là khối lượng riêng của vật liệu đã chọn, "
               "tính bằng kg/m³."))

    b.append(h3("Ví dụ", "Example"))
    b.append(p("Một van bướm 6 inch (150 mm) lắp trong ống 6 inch có các số "
               "liệu sau:"))
    b.append(eq("Cᵥ = 180        A = 8 log(6) + 12 log(5) + 4 = 18.6 dB"))
    b.append(eq("P₁ = 115 psia   B = 35 log(115) − 35 = 37.1 dB"))
    b.append(eq("P₂ = 46 psia    c₁ = 30 log(10X) vì X nhỏ hơn F_L² = 23.4 dB"))
    b.append(eq("F_L = 0.9       c₂ = 60 log(0.60 / 0.3) = 18 dB"))
    b.append(eq("X_Fz = 0.3      c₃ = zero vì X ≤ Xy"))
    b.append(eq("Cᵥ/D² = 5       C = c₁ + c₂ − c₃ = 41.4 dB"))
    b.append(eq("P_v = 0.4 psia  vì X nhỏ hơn Xy"))
    b.append(eq("Xy = (1 + 0.3) / 2 = 0.65"))
    b.append(eq("X = 0.6"))
    b.append(eq("L_pAe1m = A + B + C = 18.6 + 37.1 + 41.4 = 97.1 dBA"))
    b.append(p("[Số liệu thử nghiệm cho 94 dBA.]"))

    b.append(h3("Các điểm thử nghiệm bổ sung", "Additional Test Points"))
    b.append(p("Xem Hình 22-1, 22-2 và 22-3 trong Chương 22, «Ước tính đồ thị "
               "tiếng ồn do dòng rối và xâm thực của chất lỏng»."))
    b.append(eq("X = 0.3,  ước tính 70 dBA,  thử nghiệm = 66 dBA"))
    b.append(eq("X = 0.8,  ước tính 92.1 dBA,  thử nghiệm = 91 dBA"))
    b.append(p("Ở đây phải phân biệt giữa tiếng ồn do dòng chảy rối (chỉ quan "
               "trọng khi dùng ống lớn) và tiếng ồn do xâm thực. Loại sau "
               "phổ biến hơn và có thể tạo mức âm vượt quá 90 dBA ngay cả với "
               "van chỉ 1 in."))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR xáo trộn các "
                  "phương trình; các dạng in trên trang 134 đã được đọc lại "
                  "từ ảnh trang nguồn, kể cả dấu căn trong E = 45 "
                  "(1/√X_Fz). (2) Trong Bảng 21-1, dòng Van cầu, nút parabol "
                  "chỉ có bốn số liệu in và sáu ô trống còn lại được giữ "
                  "nguyên để bảng giữ được 11 cột. Giá trị cuối cùng 0,19 "
                  "của dòng Van bi phân đoạn cũng được giữ theo bản in. "
                  "(3) Giữ nguyên cách đặt ngoặc trong biểu thức chất lỏng "
                  "khác nước, dù về mặt thứ nguyên có vẻ bất thường. (4) Giá "
                  "trị độ dày ống của chất lỏng là −3/−6 dB, không phải giá "
                  "trị −4/−8 dB của chất khí trong Chương 18. (5) Bảng số "
                  "liệu của ví dụ được in thành hai cột có gạch kẻ; bản dịch "
                  "chuyển mỗi dòng thành một phương trình không đánh số, "
                  "không tạo thêm bảng thứ hai. (6) Chương này có đúng một "
                  "bảng, không có hình và không có phương trình đánh số."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 21 chiếm các trang in 133–135 của ấn bản in (PDF tr. "
               "133–135, nên số trang in trùng số trang PDF). Nguyên bản gồm "
               "tuyên bố miễn trừ, danh sách dữ liệu cần có, các phép tính ban "
               "đầu, các bước tính toán, Bảng 21-1, phần hệ số hiệu chỉnh, ví "
               "dụ van bướm 6 inch, hai điểm thử nghiệm bổ sung và đoạn kết "
               "phân biệt tiếng ồn dòng rối với tiếng ồn xâm thực — tất cả đều "
               "được giữ lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Disclaimer", "Disclaimer"))

    b.append(p("<b>Disclaimer.</b> The proposed method is valid only for "
               "single-outlet ported control valves such as globe or "
               "line-of-sight valves with turbulent fluid (Rev > 10.000). "
               "Note: Cavitation, while most common with water, can also "
               "happen with other fluids such as crude oil."))
    b.append(p("Noise reduction trim such as multiported trims or "
               "resistance-in-series types are covered in Chapter 20."))
    b.append(p("Similar to the ABC method for gases, this method not only "
               "predicts turbulent liquid sound but it also can accurately "
               "predict additional sound sources produced by cavitating "
               "liquids (actually aerodynamic phenomena)."))
    b.append(p("Pipe diameter downstream of valve D in inches (D = d / 25.4 "
               "if d is in mm), P₁ in psia (bara × 14.5), P₂ in psia (bara × "
               "14.5)."))
    b.append(eq("D = d / 25.4  (d in mm)"))
    b.append(eq("P₁ [psia] = p [bara] × 14.5;  P₂ [psia] = p [bara] × 14.5"))

    b.append(h3("Input Needed", "Input Needed"))
    b.append(p("Cᵥ = flow coefficient (at operating conditions)."))
    b.append(p("F_L = pressure recovery coefficient without expander at "
               "actual travel position."))
    b.append(p("X_Fz = coefficient of incipient cavitation (see Table 21-1)."))
    b.append(p("P_v = liquid vapor pressure in psia."))
    b.append(p("r_w = valve type modifier (3 for globe valves)."))

    b.append(h3("Initial Calculations", "Initial Calculations"))
    b.append(eq("X = (P₁ − P₂) / (P₁ − P_v)"))
    b.append(eq("Xy = X at maximum cavitation = (1 + X_Fz) / 2"))
    b.append(eq("E = exponent = 45 (1/√X_Fz)"))

    b.append(h3("Calculation Steps", "Calculation Steps"))
    b.append(eq("A = 8 log(D) + 12 log(Cᵥ/D²) + 4  dB"))
    b.append(p("where A is in dB and D is the pipe diameter in inches."))
    b.append(eq("B = 35 log(P₁) − 35 for US, or 35 log(14.5 p) − 35 if p is "
                "in bara"))
    b.append(eq("c₁ = 30 log(10X),  X maximum = F_L²"))
    b.append(p("This equation gives the turbulent sound level in dBA at 1 m."))
    b.append(eq("c₂ = 60 log(X / X_Fz)  if X is above X_Fz but below Xy"))
    b.append(eq("c₂ = 60 log(Xy / X_Fz)  if X is above Xy; otherwise use zero"))
    b.append(p("This defines the increasing cavitation sound level in dB."))
    b.append(eq("c₃ = E log(X / Xy)  if X is larger than Xy; otherwise use zero"))
    b.append(p("This denotes a decreasing cavitation sound level in dB."))
    b.append(eq("C = c₁ + c₂ − c₃  dBA"))
    b.append(eq("L_pAe1m = A + B + C − r_w  dBA at 1 m, plus modifiers"))

    b.append(p("The X_Fz factors are tabulated in Table 21-1 below."))
    b.append(table(
        ["Cᵥ/D² (D in inches)", "3", "6", "9", "12", "15", "18", "21", "24",
         "27", "30"],
        [["Cᵥ/d² × 10³ (mm)", "4.64", "9.3", "14", "18.6", "23.3", "28",
          "32.6", "37.2", "42", "54"],
         ["Globe Valve, Parabolic Plug", "0.78", "0.68", "0.49", "0.30", "",
          "", "", "", "", ""],
         ["Butterfly Valve", "0.45", "0.30", "0.23", "0.21", "0.20", "0.19",
          "0.18", "0.17", "0.16", "0.15"],
         ["Segmented Ball Valve", "0.46", "0.30", "0.22", "0.20", "0.18",
          "0.17", "0.15", "0.13", "0.12", "0.19"]],
        "Table 21-1. Tabulation of X_Fz factors."))

    b.append(h3("Modifiers", "Modifiers"))
    b.append(eq("Schedule 40 = 0;  schedule 80 = −3 dB;  schedule 160 = −6 dB"))
    b.append(p("For liquids other than water, add:"))
    b.append(eq("20 log[(62.5 / ρ_liq) + 25 log(4750 / c_liq)]"))
    b.append(p("where ρ_liq is the density of the chosen liquid (lb/ft³) and "
               "c_liq is the speed of sound of the chosen liquid (ft/s)."))
    b.append(p("For pipe materials other than steel, add:"))
    b.append(eq("20 log(7800 / ρ_material)"))
    b.append(p("where ρ_material is the density of the chosen material, in "
               "kg/m³."))

    b.append(h3("Example", "Example"))
    b.append(p("A 6-inch (150 mm) butterfly valve in a 6-inch pipe has the "
               "following data:"))
    b.append(eq("Cᵥ = 180        A = 8 log(6) + 12 log(5) + 4 = 18.6 dB"))
    b.append(eq("P₁ = 115 psia   B = 35 log(115) − 35 = 37.1 dB"))
    b.append(eq("P₂ = 46 psia    c₁ = 30 log(10X) because X is less than "
                "F_L² = 23.4 dB"))
    b.append(eq("F_L = 0.9       c₂ = 60 log(0.60 / 0.3) = 18 dB"))
    b.append(eq("X_Fz = 0.3      c₃ = zero because X ≤ Xy"))
    b.append(eq("Cᵥ/D² = 5       C = c₁ + c₂ − c₃ = 41.4 dB"))
    b.append(eq("P_v = 0.4 psia  because X is smaller than Xy"))
    b.append(eq("Xy = (1 + 0.3) / 2 = 0.65"))
    b.append(eq("X = 0.6"))
    b.append(eq("L_pAe1m = A + B + C = 18.6 + 37.1 + 41.4 = 97.1 dBA"))
    b.append(p("[Test data showed 94 dBA.]"))

    b.append(h3("Additional Test Points", "Additional Test Points"))
    b.append(p("See Figures 22-1, 22-2, and 22-3 in Chapter 22, “Graphical "
               "Estimation of Noise Produced by Turbulence and Cavitation of "
               "Liquids.”"))
    b.append(eq("X = 0.3,  Est. 70 dBA,  test = 66 dBA"))
    b.append(eq("X = 0.8,  Est. 92.1 dBA,  test = 91 dBA"))
    b.append(p("Here we have to distinguish between noise produced by "
               "turbulent flow (only important if large pipes are involved) "
               "and noise produced by cavitation. The latter is more common "
               "and can create sound levels in excess of 90 dBA even with "
               "valves as small as 1 in."))

    b.append(note("<b>Source note.</b> (1) The OCR text layer garbles the "
                  "equations; the printed forms on p. 134 were read from the "
                  "page render, including the radical in E = 45 "
                  "(1/√X_Fz). (2) In Table 21-1 the Globe Valve, Parabolic "
                  "Plug row carries only four printed numbers; the six "
                  "remaining cells are left empty so the table keeps its "
                  "11-column shape. The last entry 0.19 of the Segmented "
                  "Ball Valve row is also kept as printed. (3) The bracket "
                  "placement in the expression for liquids other than water "
                  "is preserved even though it looks dimensionally unusual. "
                  "(4) The liquid pipe-schedule modifiers are −3/−6 dB, not "
                  "the −4/−8 dB gas values of Chapter 18. (5) The example "
                  "numbers are printed as a ruled two-column data block; "
                  "each line is carried here as an unnumbered equation, so "
                  "no second table is introduced. (6) The chapter has "
                  "exactly one table, no figures and no numbered equations."))
    b.append(h3("About the source", "About the source"))
    b.append(p("Chapter 21 occupies printed pp. 133–135 of the book (PDF pp. "
               "133–135, so printed and PDF page numbers coincide). The "
               "source consists of the disclaimer, the input list, the "
               "initial calculations, the calculation steps, Table 21-1, the "
               "modifiers, the 6-inch butterfly valve example, the two "
               "additional test points and the closing paragraph "
               "distinguishing turbulent-flow noise from cavitation noise, "
               "all of which are retained."))
    return "".join(b)
