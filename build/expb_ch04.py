# -*- coding: utf-8 -*-
"""Reader unit 4 of R. STAHL, *Basics of Explosion Protection* --
"Environmental Protection and Ingress Protection" /
"Bảo vệ môi trường và chỉ số IP".

Printed A7-A8 (PDF pp. 8-9): the three enclosure comparison tables with
all printed footnotes, and the two-digit IP ingress-protection chart.
"""
from expb_common import p, lead, h2, h3, h4, ul, ol, note, table, fig

import expbfig04 as F

PAGES_SRC = 2
BYLINE = "R. STAHL · Basics of Explosion Protection (Innovative Explosion Protection)"
TITLE_EN = "Environmental Protection and Ingress Protection"
TITLE_VI = "Bảo vệ môi trường và chỉ số IP"

# ---------------------------------------------------------------- table 4-1
_IN_HDR_VI = ["Mức độ bảo vệ chống lại các điều kiện môi trường sau",
              "1*", "2*", "4", "4x", "5", "6", "6P", "12", "12K", "13"]
_IN_HDR_EN = ["Provides A Degree Of Protection Against The Following "
              "Environmental Conditions",
              "1*", "2*", "4", "4x", "5", "6", "6P", "12", "12K", "13"]
_IN_CELLS = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["-", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["-", "-", "x", "x", "-", "x", "x", "x", "x", "x"],
    ["-", "-", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["-", "-", "x", "x", "-", "x", "x", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "x", "x", "x"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "x"],
    ["-", "-", "-", "x", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "x", "x", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
]
_IN_LAB_VI = [
    "Tiếp xúc ngẫu nhiên với thiết bị bên trong",
    "Bụi bẩn rơi xuống",
    "Chất lỏng rơi xuống và văng nhẹ",
    "Bụi, xơ vải, sợi và mảnh bay lơ lửng**",
    "Bụi, xơ vải, sợi và mảnh bay lơ lửng lắng đọng**",
    "Nước phun xịt và văng",
    "Thấm dầu và chất làm mát",
    "Phun và văng dầu, chất làm mát",
    "Tác nhân ăn mòn",
    "Ngâm ngập tạm thời thỉnh thoảng",
    "Ngâm ngập kéo dài thỉnh thoảng",
]
_IN_LAB_EN = [
    "Incidental contact with the enclosed equipment",
    "Falling dirt",
    "Falling liquids and light splashing",
    "Circulation dust, lint, fibers, and flyings**",
    "Settling airborne dust, lint, fibers, and flyings**",
    "Hosedown and splashing water",
    "Oil and coolant seepage",
    "Oil and coolant spraying and splashing",
    "Corrosive agents",
    "Occasional temporary submersion",
    "Occasional prolonged submersion",
]
_CAP_IN_VI = (
    "Bảng 4-1. So sánh ứng dụng cụ thể của vỏ bọc cho vị trí trong nhà không nguy "
    "hiểm (bản in A7). * Các vỏ bọc này có thể thông gió. Tuy nhiên, Type 1 có thể "
    "không bảo vệ khỏi các hạt bụi bẩn nhỏ rơi xuống khi thông gió được bố trí ở "
    "phía trên vỏ bọc. ** Những sợi và mảnh bay này là vật liệu không nguy hiểm và "
    "không được coi là sợi dễ cháy hoặc mảnh bay dễ cháy Class III. Đối với sợi dễ "
    "cháy hoặc mảnh bay dễ cháy Class III, xem National Electrical Code®, Article 500.")
_CAP_IN_EN = (
    "Table 4-1. Comparison of Specific Applications of Enclosures for Indoor "
    "Non-Hazardous Locations (printed A7). * These enclosures may be ventilated. "
    "However, Type 1 may not provide protection against small particles of falling "
    "dirt when ventilation is provided in the enclosure top. ** These fibers and "
    "flyings are nonhazardous materials and are not considered as Class III type "
    "ignitable fibers or combustible flyings. For Class III type ignitable fibers "
    "or combustible flyings see the National Electrical Code®, Article 500.")

# --------------------------------------------------------------- table 4-2
_OUT_HDR_VI = ["Mức độ bảo vệ chống lại các điều kiện môi trường sau",
               "3*", "3R***", "3S", "4", "4X", "6", "6P"]
_OUT_HDR_EN = ["Provides A Degree Of Protection Against The Following "
               "Environmental Conditions",
               "3*", "3R***", "3S", "4", "4X", "6", "6P"]
# Blank cells in the last column are retained exactly as printed.
_OUT_CELLS = [
    ["x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["-", "-", "x", "-", "-", "-", ""],
    ["x", "-", "x", "x", "x", "x", ""],
    ["-", "-", "-", "x", "x", "x", ""],
    ["-", "-", "-", "-", "x", "-", ""],
    ["-", "-", "-", "-", "-", "x", ""],
    ["-", "-", "-", "-", "-", "-", "x"],
]
_OUT_LAB_VI = [
    "Tiếp xúc ngẫu nhiên với thiết bị bên trong",
    "Mưa, tuyết, mưa tuyết*",
    "Mưa tuyết**",
    "Bụi bay theo gió",
    "Phun nước dạng vòi",
    "Tác nhân ăn mòn",
    "Ngâm ngập tạm thời thỉnh thoảng",
    "Ngâm ngập kéo dài thỉnh thoảng",
]
_OUT_LAB_EN = [
    "Incidental contact with the enclosed equipment",
    "Rain, snow, sleet*",
    "Sleet**",
    "Windblown dust",
    "Hosedown",
    "Corrosive agents",
    "Occasional temporary submersion",
    "Occasional prolonged submersion",
]
_CAP_OUT_VI = (
    "Bảng 4-2. So sánh ứng dụng cụ thể của vỏ bọc cho vị trí ngoài trời không nguy "
    "hiểm (bản in A7). * Cơ cấu vận hành bên ngoài không cần hoạt động khi vỏ bọc "
    "bị phủ băng. ** Cơ cấu vận hành bên ngoài vẫn hoạt động được khi vỏ bọc bị phủ "
    "băng. ***Các vỏ bọc này có thể thông gió. Các ô trống trong cột 6P được giữ "
    "nguyên như bản in.")
_CAP_OUT_EN = (
    "Table 4-2. Comparison of Specific Applications of Enclosures for Outdoor "
    "Non-Hazardous Locations (printed A7). * External operating mechanisms are not "
    "required to operate when the enclosure is ice covered. ** External operating "
    "mechanisms are operable when the enclosure is ice covered. ***These enclosures "
    "may be ventilated. Blank cells in the 6P column are retained from the print.")

# --------------------------------------------------------------- table 4-3
_HAZ_HDR_VI = ["Mức độ bảo vệ chống lại bầu khí quyển thường chứa khí, hơi và bụi "
               "nguy hiểm***", "Class", "A", "B", "C", "D", "E", "F", "10"]
_HAZ_HDR_EN = ["Provides a Degree of Protection Against Atmospheres Typically "
               "Containing Hazardous Gases, Vapors, and Dusts***",
               "Class", "A", "B", "C", "D", "E", "F", "10"]
_HAZ_GRP_VI = ("Loại vỏ bọc: NEMA 7 &amp; 8, nhóm Class I** · "
               "NEMA 9 &amp; 10, nhóm Class II**")
_HAZ_GRP_EN = ("Type of Enclosure: NEMA 7 &amp; 8, Class I Groups** · "
               "NEMA 9 &amp; 10, Class II Groups**")
_HAZ_CELLS = [
    ["Acetylene", "I", "x", "-", "-", "-", "-", "-", "-"],
    ["Hydrogen, manufactured gases", "I", "-", "x", "-", "-", "-", "-", "-"],
    ["Diethyl ether, ethylene, cyclopropane", "I", "-", "-", "x", "-", "-", "-", "-"],
    # The printed table leaves this wrapped-label row without a Class or marks.
    ["Gasoline, hexane, butane, naphtha, propane, acetone", "", "", "", "", "", "", "", ""],
    ["Toluene, isoprene", "I", "-", "-", "-", "x", "-", "-", "-"],
    ["Metal dusts", "II", "-", "-", "-", "x", "-", "-", "-"],
    ["Carbon black, coal dust, coke dust", "II", "-", "-", "-", "-", "x", "-", "-"],
    ["Flour, starch, grain dust", "II", "-", "-", "-", "-", "-", "x", "-"],
    ["Fibers, flyings", "III", "-", "-", "-", "-", "-", "x", "-"],
    ["Methane with or without coal dust", "MSHA", "-", "-", "-", "-", "-", "-", "x"],
]
_HAZ_LAB_VI = [
    "Axetilen",
    "Hydro, khí chế tạo",
    "Ete dietyl, etylen, xyclopropan",
    "Xăng, hexan, butan, naphta, propan, axeton",
    "Toluene, isopren",
    "Bụi kim loại",
    "Bột than, bụi than, bột coke",
    "Bột mì, tinh bột, bụi ngũ cốc",
    "Sợi, mảnh bay",
    "Methane có hoặc không có bụi than",
]
_CAP_HAZ_VI = (
    "Bảng 4-3. So sánh ứng dụng cụ thể của vỏ bọc cho vị trí trong nhà nguy hiểm "
    "(đã phân loại) (bản in A7). * Do đặc tính của khí, hơi hoặc bụi, một sản phẩm "
    "phù hợp cho một Class hoặc Group có thể không phù hợp cho Class hoặc Group "
    "khác, trừ khi được ghi nhãn như vậy trên sản phẩm. ** Đối với sợi dễ cháy hoặc "
    "mảnh bay dễ cháy Class III, xem National Electrical Code® Article 500. ***Để "
    "có danh sách đầy đủ chất lỏng, khí hoặc hơi dễ cháy, xem NFPA 497 - 1997 "
    "(Recommended Practice for the Classification of Flammable Liquids. Gases, or "
    "Vapors and of Hazardous (Classified) Locations for Electrical installations "
    "in Chemical Process Areas và NFPA 325 - 1994 (Fire Hazard Properties of "
    "Flammable Liquids. Gases, and Volatile Solids). Tham khảo thêm NFPA 499 -1997 "
    "Classifications of Combustible Dusts and of Hazardous (Classified) Locations "
    "for Electrical installations in Chemical Process Areas.")
_CAP_HAZ_EN = (
    "Table 4-3. Comparison of Specific Applications of Enclosures for Indoor "
    "Hazardous (Classified) Locations (printed A7). * Due to the characteristics of "
    "the gas, vapor, or dust, a product suitable for one Class or Group may not be "
    "suitable for any other Class or Group unless so marked on the product. ** For "
    "Class III type ignitable fibers or combustible flyings refer to the National "
    "Electrical Code® Article 500. ***For a complete listing of flammable liquids, "
    "gases, or vapors refer to NFPA 497 - 1997 (Recommended Practice for the "
    "Classification of Flammable Liquids. Gases, or Vapors and of Hazardous "
    "(Classified) Locations for Electrical installations in Chemical Process Areas "
    "and NFPA 325 - 1994 (Fire Hazard Properties of Flammable Liquids. Gases, and "
    "Volatile Solids). Reference also NFPA 499 -1997 Classifications of Combustible "
    "Dusts and of Hazardous (Classified) Locations for Electrical installations in "
    "Chemical Process Areas.")


def _haz_rows(lang):
    labels = _HAZ_LAB_VI if lang == "vi" else [r[0] for r in _HAZ_CELLS]
    rows = [_HAZ_GRP_VI if lang == "vi" else _HAZ_GRP_EN]
    for lab, cells in zip(labels, _HAZ_CELLS):
        rows.append([lab] + cells[1:])
    return rows


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 4.</b> bảo vệ môi trường · vỏ bọc NEMA / CSA · "
                "vị trí không nguy hiểm trong nhà / ngoài trời · vị trí nguy hiểm "
                "(đã phân loại) · incidental contact · falling dirt · windblown dust "
                "· hosedown · corrosive agents · submersion · MSHA · Class I Groups "
                "A–D · Class II Groups E–G · Class III · NFPA 497 - 1997 · NFPA 325 "
                "- 1994 · NFPA 499 -1997 · National Electrical Code® Article 500 · "
                "Ingress Protection (IP) · IEC 60 529 · chữ số thứ nhất / thứ hai · "
                "vật thể rắn · nước · dust tight")
    return ("<b>Key terms.</b> environmental protection · NEMA / CSA enclosure · "
            "indoor non-hazardous location · outdoor non-hazardous location · "
            "hazardous (classified) location · incidental contact · falling dirt · "
            "windblown dust · hosedown · corrosive agents · submersion · MSHA · "
            "Class I Groups A-D · Class II Groups E-G · Class III · NFPA 497 - 1997 "
            "· NFPA 325 - 1994 · NFPA 499 -1997 · National Electrical Code® Article "
            "500 · Ingress Protection (IP) · IEC 60 529 · first / second digit · "
            "solid objects · water · dust tight")


def body_vi():
    b = []
    b.append(h2(TITLE_VI, TITLE_EN))
    b.append(lead("Bảo vệ môi trường mô tả khả năng của vỏ bọc trong việc ngăn bụi "
                  "bẩn, nước, băng giá và các tác nhân ăn mòn xâm nhập. Trang A7 so "
                  "sánh các ứng dụng cụ thể của vỏ bọc; trang A8 giải thích mã IP "
                  "hai chữ số."))

    b.append(h3("So sánh vỏ bọc cho vị trí không nguy hiểm",
                "Comparison of Enclosures for Non-Hazardous Locations"))
    b.append(p("Bảng sau liệt kê mức độ bảo vệ mà từng loại vỏ bọc cung cấp cho các "
               "điều kiện môi trường trong nhà, với \"x\" biểu thị có bảo vệ và "
               "\"-\" biểu thị không có."))
    b.append(table(_IN_HDR_VI,
                   [[lab] + cells for lab, cells in zip(_IN_LAB_VI, _IN_CELLS)],
                   caption=_CAP_IN_VI))
    b.append(p("Đối với vị trí ngoài trời, tiêu chí gồm mưa, tuyết, mưa tuyết, bụi "
               "bay theo gió, phun nước và ngâm ngập. Các ô trống trong cột 6P được "
               "giữ nguyên như bản in."))
    b.append(table(_OUT_HDR_VI,
                   [[lab] + cells for lab, cells in zip(_OUT_LAB_VI, _OUT_CELLS)],
                   caption=_CAP_OUT_VI))

    b.append(h3("So sánh vỏ bọc cho vị trí nguy hiểm (đã phân loại)",
                "Comparison of Enclosures for Hazardous (Classified) Locations"))
    b.append(p("Bảng cuối cùng xếp các loại vỏ bọc theo nhóm khí và bụi, từ "
               "Acetylene đến Methane with or without coal dust, trong đó cột "
               "MSHA đề cập đến Mine Safety and Health Administration."))
    b.append(table(_HAZ_HDR_VI, _haz_rows("vi"), caption=_CAP_HAZ_VI))

    b.append(h3("Chỉ số bảo vệ xâm nhập (IP)", "Ingress Protection (IP)"))
    b.append(p("IEC dùng thuật ngữ \"Ingress Protection\" để xác định sự bảo vệ môi "
               "trường của một thiết bị. Thuật ngữ này được định nghĩa trong IEC "
               "Standard 60 529; sơ đồ sau minh họa mã hai chữ số được sử dụng."))
    b.append(p("Hệ thống phân loại IP dùng một con số để biểu thị mức độ bảo vệ của "
               "thiết bị chống sự xâm nhập của bụi và nước. Chữ số thứ nhất (0–6) "
               "cho mức bảo vệ chống vật thể rắn; chữ số thứ hai (0–8) cho mức bảo "
               "vệ chống nước."))
    b.append(fig(1, F.fig_f401()))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Cả ba bảng trên trang A7 đều "
                  "được chép lại đầy đủ, kể cả các chú thích * , ** và *** , các "
                  "ô trống trong cột 6P và hàng \"Gasoline, hexane, butane, naphtha, "
                  "propane, acetone\" không có Class hay dấu x. Hình 4-1 được vẽ lại "
                  "dạng vector từ trang A8 với mô tả tiếng Anh nguyên văn cho chữ số "
                  "thứ nhất 0–6 và thứ hai 0–8, kèm bản dịch tiếng Việt."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. "
               "Nội dung gốc © R. STAHL, Inc.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2(TITLE_EN, TITLE_EN))
    b.append(lead("Environmental protection describes the ability of an enclosure "
                  "to keep dirt, dust, water, ice and corrosive agents out. Printed "
                  "A7 compares specific enclosure applications; printed A8 explains "
                  "the two-digit IP code."))

    b.append(h3("Comparison of Enclosures for Non-Hazardous Locations",
                "Comparison of Enclosures for Non-Hazardous Locations"))
    b.append(p("The following table lists the degree of protection each enclosure "
               "type provides against indoor environmental conditions, with \"x\" "
               "meaning protection is provided and \"-\" meaning it is not."))
    b.append(table(_IN_HDR_EN,
                   [[lab] + cells for lab, cells in zip(_IN_LAB_EN, _IN_CELLS)],
                   caption=_CAP_IN_EN))
    b.append(p("For outdoor locations the criteria include rain, snow, sleet, "
               "windblown dust, hosedown and submersion. Blank cells in the 6P "
               "column are retained from the print."))
    b.append(table(_OUT_HDR_EN,
                   [[lab] + cells for lab, cells in zip(_OUT_LAB_EN, _OUT_CELLS)],
                   caption=_CAP_OUT_EN))

    b.append(h3("Comparison of Enclosures for Hazardous (Classified) Locations",
                "Comparison of Enclosures for Hazardous (Classified) Locations"))
    b.append(p("The final table groups enclosures by gas and dust group, from "
               "Acetylene to Methane with or without coal dust, with the MSHA "
               "column referring to the Mine Safety and Health Administration."))
    b.append(table(_HAZ_HDR_EN, _haz_rows("en"), caption=_CAP_HAZ_EN))

    b.append(h3("Ingress Protection (IP)", "Ingress Protection (IP)"))
    b.append(p("The IEC uses the term \"Ingress Protection\" to identify the "
               "environmental protection of a device. This is defined in IEC "
               "Standard 60 529 and the chart below illustrates the two-digit code "
               "used."))
    b.append(p("The IP classification system designates, by means of a number, the "
               "degree of protection provided by a device against ingress of dust "
               "and water. The first number (0-6) is the degree of protection "
               "against solid objects; the second number (0-8) is the degree of "
               "protection against water."))
    b.append(fig(1, F.fig_f401()))
    b.append(note("<b>Source quirks.</b> All three tables on printed A7 are "
                  "reproduced in full, including footnotes *, ** and ***, the blank "
                  "cells in the 6P column, and the \"Gasoline, hexane, butane, "
                  "naphtha, propane, acetone\" row which has no Class or mark in "
                  "the print. Figure 4-1 is redrawn as a vector from printed A8 with "
                  "the exact printed English descriptions for first digit 0-6 and "
                  "second digit 0-8, plus Vietnamese translations."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © R. STAHL, Inc.</i>"))
    return "".join(b)
