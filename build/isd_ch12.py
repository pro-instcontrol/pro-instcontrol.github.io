# -*- coding: utf-8 -*-
"""Book 5, Chapter 12 — Case Study: Acetic Acid Process (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 91–94.  The chapter applies the
Inherent Safety Index to a 100 000 t/a methanol-carbonylation acetic acid
process: Figure 7 (flowsheet, redrawn) and the safety analyses of the two
ISBL steps — the reaction section (Table 26, I_TI = 29) and the distillation
train (Table 27, I_TI = 19).
"""

from isd_common import fig, h2, note, p, table
import isdfig as F

PAGES_SRC = 4            # source pages 91–94
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Case Study — Acetic Acid Process"
TITLE_VI = "Nghiên cứu tình huống — Quá trình axit axetic"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 12.</b> cacbonyl hóa methanol — phản ứng "
                "MeOH + CO tạo axit axetic · chất xúc tác rhodium iodocarbonyl · "
                "phần phản ứng vs chuỗi chưng cất · axit propionic — phản ứng "
                "phụ · axit hydriodic (HI) · methyl iodide · Hastelloy — hợp kim "
                "kết cấu chịu ăn mòn · I<sub>TI</sub> — tổng chỉ số an toàn nội "
                "tại (giá trị thấp = an toàn hơn).")
    return ("<b>Key terms.</b> methanol carbonylation — the MeOH + CO reaction "
            "forming acetic acid · rhodium iodocarbonyl catalyst · reaction "
            "section vs distillation train · propionic acid — side reaction · "
            "hydriodic acid (HI) · methyl iodide · Hastelloy — corrosion-"
            "resistant construction alloy · I<sub>TI</sub> — the total inherent "
            "safety index (lower = safer).")


_D = '<span style="color:#bbb">—</span>'

# Source Table 26 (p. 93): reaction section analysis.
_T26 = [
    "Chỉ số an toàn nội tại hóa học · Chemical inherent safety index",
    ("Nhiệt phản ứng chính · Heat of main reaction", "~ 300 J/g", "1"),
    ("Nhiệt phản ứng phụ, tối đa · Heat of side reaction, max", "~ 1000 J/g", "2"),
    ("Khả cháy, khả nổ, độc tính — tổng lớn nhất cho CO · Flammability, "
     "explosiveness, toxicity — maximum sum for CO", _D, "10"),
    ("Khả ăn mòn — thép không gỉ / Hastelloy · Corrosiveness — stainless "
     "steel / Hastelloy", _D, "2"),
    ("Tương tác hóa học — xấu nhất: methanol – axit hydriodic · Chemical "
     "interaction — worst: methanol – hydriodic acid", _D, "4"),
    ("Σ", _D, "19"),
    "Chỉ số an toàn nội tại quá trình · Process inherent safety index",
    ("Tồn kho · Inventory", "100 t/h", "3"),
    ("Nhiệt độ quá trình, tối đa · Process temperature, max", "175 °C", "2"),
    ("Áp suất quá trình, tối đa · Process pressure, max", "30 bar", "2"),
    ("An toàn thiết bị — máy nén khí cấp · Safety of equipment — feed-gas "
     "compressor", _D, "3"),
    ("Σ", _D, "10"),
    ("Tổng chỉ số an toàn nội tại · Total inherent safety index", _D, "29"),
]

# Source Table 27 (p. 94): distillation train analysis.
_T27 = [
    "Chỉ số an toàn nội tại hóa học · Chemical inherent safety index",
    ("Nhiệt phản ứng chính — không phản ứng · Heat of main reaction — no "
     "reaction", _D, "0"),
    ("Nhiệt phản ứng phụ, tối đa — không phản ứng phụ · Heat of side "
     "reaction, max — no side reactions", _D, "0"),
    ("Khả cháy, khả nổ, độc tính — tổng lớn nhất cho axit axetic · "
     "Flammability, explosiveness, toxicity — maximum sum for acetic acid",
     _D, "7"),
    ("Khả ăn mòn — thép không gỉ / Hastelloy · Corrosiveness — stainless "
     "steel / Hastelloy", _D, "2"),
    ("Tương tác hóa học — xấu nhất: methyl iodide – axit hydriodic · Chemical "
     "interaction — worst: methyl iodide – hydriodic acid", _D, "4"),
    ("Σ", _D, "13"),
    "Chỉ số an toàn nội tại quá trình · Process inherent safety index",
    ("Tồn kho · Inventory", "100 t/h", "3"),
    ("Nhiệt độ quá trình, tối đa · Process temperature, max", "155 °C", "2"),
    ("Áp suất quá trình, tối đa · Process pressure, max", "4 bar", "0"),
    ("An toàn thiết bị — tháp chưng cất · Safety of equipment — distillation "
     "tower", _D, "1"),
    ("Σ", _D, "6"),
    ("Tổng chỉ số an toàn nội tại · Total inherent safety index", _D, "19"),
]


def _analysis_table(rows, header, cap):
    prepped = []
    for r in rows:
        if isinstance(r, str):
            prepped.append('<b style="color:#1f5f8b">%s</b>' % r)
        else:
            prepped.append(r)
    return table(header, prepped, cap)


def body_vi():
    b = []

    b.append(h2("12. Nghiên cứu tình huống", "12. Case Study"))

    b.append(p("Là nghiên cứu tình huống, một quá trình sản xuất <b>axit "
               "axetic</b> được đưa ra. Axit axetic được sản xuất bằng "
               "<b>cacbonyl hóa methanol pha lỏng</b>: axit axetic hình thành "
               "từ phản ứng giữa methanol và carbon monoxide, được xúc tác bởi "
               "chất xúc tác <b>rhodium iodocarbonyl</b>. Sơ đồ quá trình cho "
               "ở Hình 7."))

    b.append(fig(1, F.fig_c12_flowsheet()))

    b.append(p("Phản ứng cacbonyl hóa methanol diễn ra trong lò phản ứng (1) "
               "ở khoảng <b>175 °C và 30 bar</b>. Khí từ lò phản ứng (1) được "
               "dẫn tới bộ tách (2), nơi tách phần ngưng được khỏi CO và khí "
               "trơ. Pha khí sau đó được dẫn tới tháp rửa (3), nơi các hợp chất "
               "hữu cơ được loại bỏ bằng methanol. Dòng thoát của bộ tách (2) "
               "được tuần hoàn về lò phản ứng cùng dòng methanol từ tháp rửa "
               "(3). Chất lỏng từ lò phản ứng (1) được dẫn tới cột chưng cất "
               "(4) để tách đầu nhẹ và đầu nặng — cả hai đều được tuần hoàn về "
               "lò phản ứng (1). Dòng lấy bên axit axetic từ bộ tách đầu nhẹ "
               "(4) được dẫn tới cột sấy (5) để loại nước. Đáy cột sấy (5) "
               "chứa axit axetic khô được dẫn tới cột sản phẩm (6), nơi loại "
               "bỏ các sản phẩm phụ nặng; phần đỉnh axit axetic được dẫn tới "
               "cột tinh chế (7) để tinh chế cuối."))

    b.append(p("Các chất hóa học trong quá trình đều <b>cháy được và/hoặc "
               "độc</b> ở các mức khác nhau; các dòng quá trình tạo ra các "
               "mối nguy khác nhau tùy loại và lượng hóa chất chứa trong đó. "
               "Công suất của quá trình là <b>100 000 t/a axit axetic</b>."))

    b.append(p("Cho phân tích so sánh an toàn, ISBL của quá trình axit axetic "
               "được chia thành hai phần: <b>phần phản ứng</b> (lò phản ứng, "
               "bộ tách, tháp rửa) và <b>chuỗi chưng cất</b>; cả hai được xử lý "
               "riêng trong phân tích. Kết quả trình bày ở Bảng 26 cho phần "
               "phản ứng và Bảng 27 cho chuỗi chưng cất."))

    b.append(p("Nhiệt của phản ứng chính và phản ứng phụ được tính theo "
               "Phương trình 6 cho toàn bộ tồn kho lỏng. Với phản ứng chính, "
               "nhiệt phản ứng khoảng <b>300 J/g</b>; sự hình thành axit "
               "propionic cho nhiệt phản ứng phụ tối đa khoảng <b>1000 J/g</b>. "
               "Chất nguy hiểm nhất trong quá trình là <b>carbon monoxide</b>, "
               "xuất hiện trong phần phản ứng. Vật liệu kết cấu cần cả thép "
               "không gỉ lẫn <b>Hastelloy</b> — Hastelloy cho điểm 2. Tương tác "
               "hóa học nguy hiểm nhất có thể xảy ra giữa <b>methanol và axit "
               "hydriodic</b> trong phần phản ứng, tạo nhiệt và thậm chí cháy — "
               "điểm 4. Tồn kho của quá trình là <b>100 tấn</b> khi tính cả bảy "
               "bình với thời gian lưu một giờ. Nhiệt độ quá trình tối đa là "
               "<b>175 °C</b> ở lò phản ứng; áp suất cao nhất là <b>30 bar</b> "
               "trong phần phản ứng. An toàn thiết bị được xác định bởi máy nén "
               "khí cấp CO (điểm 3); lò phản ứng thường cho điểm 2 và lò phản "
               "ứng nguy hiểm cao điểm 3 (Bảng 23). Chỉ số cấu trúc quá trình "
               "an toàn cho quá trình axit axetic được thảo luận chi tiết hơn "
               "ở mục 13.2."))
    b.append(_analysis_table(
        _T26,
        ("Phần phản ứng · Reaction section", "Cơ sở", "Điểm"),
        "Bảng 26 · Phân tích an toàn cho phần phản ứng của quá trình axit axetic."))

    b.append(p("Tổng chỉ số an toàn nội tại của phần phản ứng <b>cao hơn</b> "
               "so với chuỗi chưng cất. Do đó <b>chuỗi chưng cất an toàn nội "
               "tại hơn phần phản ứng</b>, vì:"))
    b.append(("<ul>"
              "<li>Trong chuỗi chưng cất không có phản ứng tiềm năng, ngoại trừ "
              "tương tác tiềm năng.</li>"
              "<li>Chất nguy hiểm nhất là carbon monoxide — chỉ xuất hiện trong "
              "phần phản ứng.</li>"
              "<li>Áp suất quá trình cao hơn trong phần phản ứng.</li>"
              "<li>An toàn thiết bị kém hơn trong phần phản ứng do máy nén khí "
              "cấp và lò phản ứng.</li>"
              "</ul>"))
    b.append(_analysis_table(
        _T27,
        ("Chuỗi chưng cất · Distillation train", "Cơ sở", "Điểm"),
        "Bảng 27 · Phân tích an toàn cho chuỗi chưng cất của quá trình axit axetic."))

    b.append(note("So sánh: phần phản ứng I<sub>TI</sub> = 29 (hóa học 19 + "
                  "quá trình 10) so với chuỗi chưng cất I<sub>TI</sub> = 19 "
                  "(hóa học 13 + quá trình 6). Các điểm khác biệt chính nằm ở "
                  "nhiệt phản ứng, CO, áp suất và thiết bị (máy nén, lò phản "
                  "ứng)."))

    return "".join(b)


def body_en():
    b = []

    b.append(h2("12. Case Study", "12. Nghiên cứu tình huống"))

    b.append(p("As a case study, an <b>acetic acid process</b> has been given. "
               "Acetic acid is produced by a liquid-phase <b>methanol "
               "carbonylation</b>: acetic acid is formed by the reaction "
               "between methanol and carbon monoxide, catalysed by a rhodium "
               "iodocarbonyl catalyst. The process diagram is shown in "
               "Figure 7."))

    b.append(fig(1, F.fig_c12_flowsheet()))

    b.append(p("The methanol carbonylation reaction is carried out in the "
               "reactor (1) at about <b>175 °C and 30 bar</b>. Gases from the "
               "reactor (1) are led to the separator (2), where condensables "
               "are separated from the carbon monoxide and inerts. The gas "
               "phase is then led to the scrubber (3), where organics are "
               "removed using methanol. The effluent stream of the separator "
               "(2) is recycled to the reactor with the methanol stream from "
               "the scrubber (3). Liquid from the reactor (1) is led to the "
               "distillation column (4) for the separation of light and heavy "
               "ends, both of which are recycled back to the reactor (1). The "
               "acetic acid side-draw from the light-ends separator (4) is led "
               "to the drying column (5) for water removal. The bottoms of the "
               "drying column (5), containing dry acetic acid, are led to the "
               "product column (6) where any heavy by-products are removed; "
               "the acetic acid overhead is then led to the finishing column "
               "(7) for final purification."))

    b.append(p("The chemical substances in the process are all <b>flammable "
               "and/or toxic</b> in varying degrees; the process streams pose "
               "different hazards according to the type and quantity of "
               "chemicals present. The capacity of the process is "
               "<b>100 000 t/a acetic acid</b>."))

    b.append(p("For the safety comparison analysis, the ISBL of the acetic "
               "acid process was divided into two steps: the <b>reaction "
               "section</b> (reactor, separator, scrubber) and the "
               "<b>distillation train</b>. Both steps were handled separately "
               "during the analysis. The results are presented in Table 26 for "
               "the reaction section and in Table 27 for the distillation "
               "train."))

    b.append(p("The heats of the main and side reactions are calculated by "
               "Equation 6 for the whole liquid inventory. For the main "
               "reaction the heat is about <b>300 J/g</b>; the formation of "
               "propionic acid gives the maximum heat of side reaction, about "
               "<b>1000 J/g</b>. The most dangerous chemical in this process "
               "is <b>carbon monoxide</b>, which appears in the reaction "
               "section. As construction material, both stainless steel and "
               "<b>Hastelloy</b> are needed — Hastelloy gives the score value "
               "2. The most dangerous chemical interaction may appear between "
               "<b>methanol and hydriodic acid</b> in the reaction section, "
               "resulting in heat formation and even a fire — score 4. The "
               "inventory in the process is <b>100 tonnes</b> when all seven "
               "vessels have been calculated together with a one-hour "
               "residence time. The maximum process temperature is <b>175 °C</b> "
               "in the reactor; the highest process pressure is <b>30 bar</b> "
               "in the reaction section. The equipment safety is determined by "
               "the CO feed-gas compressor (score 3); an ordinary reactor gives "
               "score 2 and a high-hazard reactor score 3 (Table 23). The Safe "
               "Process Structure Subindex for the acetic acid process is "
               "discussed in more detail in Chapter 13.2."))
    b.append(_analysis_table(
        _T26,
        ("Reaction section", "Basis", "Score"),
        "Table 26 · Safety analysis for the reaction section of the acetic "
        "acid process."))

    b.append(p("The total inherent safety index for the reaction section is "
               "<b>higher</b> than for the distillation train. Consequently "
               "<b>the distillation train is inherently safer than the "
               "reaction section</b>, since:"))
    b.append(("<ul>"
              "<li>In the distillation train there are no potential reactions, "
              "except potential interaction.</li>"
              "<li>The most dangerous chemical, carbon monoxide, appears only "
              "in the reaction section.</li>"
              "<li>The process pressure is higher in the reaction section.</li>"
              "<li>The equipment safety is worse in the reaction section due "
              "to the feed-gas compressor and the reactor.</li>"
              "</ul>"))
    b.append(_analysis_table(
        _T27,
        ("Distillation train", "Basis", "Score"),
        "Table 27 · Safety analysis for the distillation train of the acetic "
        "acid process."))

    b.append(note("Comparison: reaction section I<sub>TI</sub> = 29 (chemical "
                  "19 + process 10) vs distillation train I<sub>TI</sub> = 19 "
                  "(chemical 13 + process 6). The key differences lie in the "
                  "reaction heats, CO, pressure and equipment (compressor, "
                  "reactor)."))

    return "".join(b)
