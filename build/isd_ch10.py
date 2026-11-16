# -*- coding: utf-8 -*-
"""Book 5, Chapter 10 — Subindices of the Chemical Inherent Safety Index
(EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 62–67.  The chapter defines the
chemical subindices: reaction hazards (10.1 — reaction heat for the main and
side reactions with Equation 6 and Table 9, chemical interaction with
Table 10) and hazardous substances (10.2 — flammability Table 11,
explosiveness Table 12, toxic exposure Table 13, corrosiveness Table 14).
The source contains no figures; the chapter is table-driven.
"""

from isd_common import eq, h2, h3, note, p, table

PAGES_SRC = 6            # source pages 62–67
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Subindices of the Chemical Inherent Safety Index"
TITLE_VI = "Chỉ số thành phần của an toàn nội tại hóa học"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 10.</b> enthalpy tạo thành (H<sub>f</sub>) · "
                "J/g — nhiệt phản ứng trên toàn khối lượng phản ứng (kể cả chất "
                "pha loãng) · ma trận EPA (Hatayama và cộng sự, 1980) — phân loại "
                "tương tác hóa học · điểm chớp cháy (flash point) · nhiệt độ sôi · "
                "LEL/UEL — giới hạn nổ dưới/trên (% thể tích) · TLV — ngưỡng phơi "
                "nhiễm 8 giờ (ppm), dựa trên Mond Index (ICI, 1985) · tốc độ ăn mòn "
                "(mm/a) · vật liệu kết cấu: thép carbon / thép không gỉ / vật liệu "
                "đặc biệt.")
    return ("<b>Key terms.</b> heat of formation (H<sub>f</sub>) · J/g — reaction "
            "heat per total reaction mass (diluents included) · EPA matrix "
            "(Hatayama et al., 1980) — chemical-interaction classification · "
            "flash point · boiling point · LEL/UEL — lower/upper explosion limits "
            "(vol %) · TLV — 8-hour Threshold Limit Value (ppm), scoring after the "
            "Mond Index (ICI, 1985) · corrosion rate (mm/a) · construction "
            "materials: carbon steel / stainless steel / special alloys.")


# ---------------------------------------------------------------------------
# Source Table 9 (p. 63): reaction heat subindices IRM and IRS.
_T9 = [
    ("Trung hòa về nhiệt · Thermally neutral &nbsp;(≤ 200 J/g)", "0"),
    ("Phát nhiệt nhẹ · Mildly exothermic &nbsp;(< 600 J/g)", "1"),
    ("Phát nhiệt vừa · Moderately exothermic &nbsp;(< 1200 J/g)", "2"),
    ("Phát nhiệt mạnh · Strongly exothermic &nbsp;(< 3000 J/g)", "3"),
    ("Phát nhiệt cực mạnh · Extremely exothermic &nbsp;(≥ 3000 J/g)", "4"),
]

_T9_EN = [
    ("Thermally neutral (≤ 200 J/g)", "0"),
    ("Mildly exothermic (< 600 J/g)", "1"),
    ("Moderately exothermic (< 1200 J/g)", "2"),
    ("Strongly exothermic (< 3000 J/g)", "3"),
    ("Extremely exothermic (≥ 3000 J/g)", "4"),
]

# Source Table 10 (p. 64): chemical interaction subindex IINT.
_T10 = [
    ("Sinh nhiệt · Heat formation", "1–3"),
    ("Cháy · Fire", "4"),
    ("Tạo khí vô hại, không cháy · Formation of harmless, nonflammable gas", "1"),
    ("Tạo khí độc · Formation of toxic gas", "2–3"),
    ("Tạo khí cháy · Formation of flammable gas", "2–3"),
    ("Nổ · Explosion", "4"),
    ("Trùng hợp nhanh · Rapid polymerization", "2–3"),
    ("Hóa chất độc tan được · Soluble toxic chemicals", "1"),
]

_T10_EN = [
    ("Heat formation", "1–3"),
    ("Fire", "4"),
    ("Formation of harmless, nonflammable gas", "1"),
    ("Formation of toxic gas", "2–3"),
    ("Formation of flammable gas", "2–3"),
    ("Explosion", "4"),
    ("Rapid polymerization", "2–3"),
    ("Soluble toxic chemicals", "1"),
]

# Source Table 11 (p. 65): flammability subindex IFL.
_T11 = [
    ("Không cháy · Nonflammable", "0"),
    ("Cháy được (điểm chớp cháy > 55 °C) · Combustible (flash point > 55 °C)", "1"),
    ("Dễ cháy (điểm chớp cháy ≤ 55 °C) · Flammable (flash point ≤ 55 °C)", "2"),
    ("Rất dễ cháy (điểm chớp cháy < 21 °C) · Easily flammable (flash point < 21 °C)", "3"),
    ("Cực dễ cháy (điểm chớp cháy < 0 °C và nhiệt độ sôi ≤ 35 °C) · "
     "Very flammable (flash point < 0 °C &amp; boiling point ≤ 35 °C)", "4"),
]

_T11_EN = [
    ("Nonflammable", "0"),
    ("Combustible (flash point > 55 °C)", "1"),
    ("Flammable (flash point ≤ 55 °C)", "2"),
    ("Easily flammable (flash point < 21 °C)", "3"),
    ("Very flammable (flash point < 0 °C &amp; boiling point ≤ 35 °C)", "4"),
]

# Source Table 12 (p. 66): explosiveness subindex IEX.
_T12 = [
    ("Không nổ · Non explosive", "0"),
    ("0–20", "1"),
    ("20–45", "2"),
    ("45–70", "3"),
    ("70–100", "4"),
]

_T12_EN = _T12

# Source Table 13 (p. 66): toxic exposure subindex ITOX.
_T13 = [
    ("TLV > 10000 ppm", "0"),
    ("TLV ≤ 10000 ppm", "1"),
    ("TLV ≤ 1000 ppm", "2"),
    ("TLV ≤ 100 ppm", "3"),
    ("TLV ≤ 10 ppm", "4"),
    ("TLV ≤ 1 ppm", "5"),
    ("TLV ≤ 0.1 ppm", "6"),
]

_T13_EN = _T13

# Source Table 14 (p. 67): corrosiveness subindex ICOR.
_T14 = [
    ("Thép carbon · Carbon steel", "0"),
    ("Thép không gỉ · Stainless steel", "1"),
    ("Cần vật liệu tốt hơn · Better material needed", "2"),
]

_T14_EN = [
    ("Carbon steel", "0"),
    ("Stainless steel", "1"),
    ("Better material needed", "2"),
]


def _score_table(rows, header, cap):
    return table(header, rows, cap)


def body_vi():
    b = []

    b.append(h2("10. Chỉ số thành phần của chỉ số an toàn nội tại hóa học",
                "10. Subindices of Chemical Inherent Safety Index"))

    b.append(p("Chỉ số an toàn nội tại hóa học xét các mối nguy liên quan đến "
               "<b>tính chất hóa học của các chất trong quá trình</b>. Chỉ số "
               "được chia thành các chỉ số thành phần cho <b>mối nguy phản "
               "ứng</b> và <b>chất nguy hiểm</b>."))

    # ---- 10.1 ----------------------------------------------------------------
    b.append(h3("10.1 Các chỉ số thành phần của mối nguy phản ứng",
                "10.1 Subindices of Reaction Hazards"))

    b.append(p("ISI xét cả phản ứng chính và những phản ứng phụ diễn ra trong "
               "lò phản ứng và có ý nghĩa. Nó cũng xét tương tác hóa học — thứ "
               "mô tả các phản ứng ngoài ý muốn có thể diễn ra giữa các chất "
               "hóa học trong nhà máy."))

    b.append(h3("10.1.1 Chỉ số nhiệt phản ứng chính",
                "10.1.1 Reaction Heat Subindex for the Main Reaction"))

    b.append(p("Vì mức độ bạo lực có thể của phản ứng nằm ở nhiệt tỏa ra và "
               "nhiệt độ có thể đạt được, <b>biến thiên năng lượng trong phản "
               "ứng</b> được chọn để thể hiện an toàn phản ứng trong ISI. Cách "
               "tiếp cận này khả thi vì enthalpy tạo thành đã được biết đối với "
               "phần lớn các chất."))
    b.append(p("Nhiệt tỏa ra hoặc hấp thụ trong quá trình được mô tả bởi "
               "Phương trình 6 cho điều kiện thể tích không đổi và quá trình "
               "đẳng áp. Khi xác định chỉ số thành phần I<sub>RM</sub>, nhiệt "
               "phản ứng của phản ứng chính được tính cho <b>toàn bộ khối lượng "
               "phản ứng</b> (tức cả chất phản ứng lẫn chất pha loãng) để tính "
               "đến nhiệt dung của hệ thống — phần hấp thụ một phần năng lượng "
               "tỏa ra:"))
    b.append(eq("ΔH<sub>r</sub> = Σ(H<sub>f</sub>)<sub>sản phẩm</sub> − "
                "Σ(H<sub>f</sub>)<sub>chất phản ứng</sub>", "(6)"))
    b.append(p("Về mặt an toàn, điều quan trọng là biết phản ứng phát nhiệt đến "
               "mức nào. Phân loại của King (1990): phản ứng <b>phát nhiệt cực "
               "mạnh</b> (≥ 3000 J/g), <b>phát nhiệt mạnh</b> (< 3000 J/g), "
               "<b>phát nhiệt vừa</b> (< 1200 J/g), <b>phát nhiệt nhẹ</b> "
               "(< 600 J/g), <b>trung hòa về nhiệt</b> (≤ 200 J/g) hoặc "
               "<b>thu nhiệt</b>. Các giá trị này cũng được dùng để xác định "
               "điểm của I<sub>RS</sub> (Bảng 9). Nếu có nhiều phản ứng chính "
               "(ví dụ phản ứng chuỗi), điểm I<sub>RM</sub> xác định trên tổng "
               "phản ứng; nếu có nhiều lò phản ứng, điểm xác định trên lò có "
               "nhiệt tỏa lớn nhất."))
    b.append(_score_table(_T9, ("Nhiệt phản ứng / toàn khối lượng phản ứng",
                                "Điểm"),
              "Bảng 9 · Xác định các chỉ số nhiệt phản ứng I<sub>RM</sub> và "
              "I<sub>RS</sub>."))

    b.append(h3("10.1.2 Chỉ số nhiệt phản ứng phụ",
                "10.1.2 Reaction Heat Subindex for the Side Reactions"))

    b.append(p("Chỉ số I<sub>RS</sub> được xác định tương tự I<sub>RM</sub>. "
               "Nhiệt phản ứng của từng phản ứng phụ có thể xảy ra được tính "
               "theo Phương trình 6 cho toàn khối lượng phản ứng (kể cả chất pha "
               "loãng); cùng thang điểm như phản ứng chính (Bảng 9). "
               "<b>Giá trị nhiệt phản ứng lớn nhất trong các phản ứng phụ</b> "
               "được dùng để xác định I<sub>RS</sub>."))

    b.append(h3("10.1.3 Chỉ số tương tác hóa học",
                "10.1.3 Chemical Interaction Subindex"))

    b.append(p("Tương tác hóa học xét các phản ứng ngoài ý muốn của các chất "
               "quá trình với vật liệu trong khu vực nhà máy. Những phản ứng "
               "này không được kỳ vọng diễn ra trong lò phản ứng nên không nằm "
               "trong chỉ số phản ứng phụ. ISI đã sử dụng <b>ma trận của EPA</b> "
               "(Hatayama và cộng sự, 1980) để phân loại mối nguy của tương tác "
               "hóa học; <b>tương tác xấu nhất</b> giữa các chất hiện diện trong "
               "khu vực nhà máy được dùng trong tính toán."))
    b.append(p("Trong Bảng 10, giới hạn điểm của I<sub>INT</sub> từ 0 đến 4. "
               "<b>Cháy và nổ</b> được coi là hệ quả nguy hiểm nhất (điểm 4). "
               "Điểm cho việc tạo <b>khí độc hoặc khí cháy</b> phụ thuộc lượng "
               "và mức hại của khí (điểm 2–3); <b>càng nhiều nhiệt sinh ra, điểm "
               "càng cao</b> (1–3). <b>Trùng hợp nhanh</b> được chấm theo tốc độ "
               "trùng hợp (2–3). Hóa chất độc tan được và tạo khí vô hại, không "
               "cháy được coi là ít hại hơn — điểm 1."))
    b.append(_score_table(_T10, ("Tương tác hóa học", "Điểm I<sub>INT</sub>"),
              "Bảng 10 · Xác định chỉ số tương tác hóa học I<sub>INT</sub>."))

    # ---- 10.2 ----------------------------------------------------------------
    b.append(h3("10.2 Các chỉ số thành phần cho chất nguy hiểm",
                "10.2 Subindices for Hazardous Substances"))

    b.append(p("Các chỉ số khả cháy, khả nổ và phơi nhiễm độc (I<sub>FL</sub>, "
               "I<sub>EX</sub>, I<sub>TOX</sub>) được xác định <b>cho từng "
               "chất</b> hiện diện trong quá trình; các giá trị này được cộng "
               "riêng cho từng chất và <b>tổng lớn nhất</b> được dùng làm giá "
               "trị chỉ số thành phần. Chỉ số khả ăn mòn được xác định trên cơ "
               "sở vật liệu ăn mòn nhất trong quá trình."))

    b.append(h3("10.2.1 Chỉ số khả cháy", "10.2.1 Flammability Subindex"))

    b.append(p("Chỉ số khả cháy mô tả tính dễ cháy của chất lỏng, ví dụ trong "
               "trường hợp rò rỉ. Khả cháy của chất lỏng được đo bằng <b>điểm "
               "chớp cháy</b> và <b>nhiệt độ sôi</b>; phân loại dựa trên chỉ "
               "dẫn của EU (Pyötsiä, 1994): không cháy, cháy được, dễ cháy, rất "
               "dễ cháy và cực dễ cháy (Bảng 11)."))
    b.append(_score_table(_T11, ("Khả cháy", "Điểm I<sub>FL</sub>"),
              "Bảng 11 · Xác định chỉ số khả cháy I<sub>FL</sub>."))

    b.append(h3("10.2.2 Chỉ số khả nổ", "10.2.2 Explosiveness Subindex"))

    b.append(p("Trong ISI, khả nổ được xét qua một tính chất hóa học không trùng "
               "hoàn toàn với mối nguy nổ của quá trình nhưng có thể làm ước tính "
               "cháy. Chỉ số khả nổ mô tả <b>xu hướng của khí tạo hỗn hợp nổ với "
               "không khí</b>. Khoảng nổ — biểu thị bằng % thể tích hơi nhiên "
               "liệu trong không khí — là khoảng nồng độ mà hỗn hợp hơi/khí với "
               "không khí sẽ cháy khi được kích giữ; ngọn lửa lan truyền nếu hỗn "
               "hợp nằm trong khoảng nổ. Giới hạn dưới ký hiệu <b>LEL</b>, giới "
               "hạn trên <b>UEL</b>. Mô hình này là ước lượng thô nhưng hữu ích "
               "khi phần lớn tính chất hóa học không có sẵn. Khả nổ được xác định "
               "bởi hiệu UEL − LEL của chất, chia thành bốn nấc (Bảng 12)."))
    b.append(_score_table(_T12, ("Khả nổ (UEL − LEL), % thể tích",
                                 "Điểm I<sub>EX</sub>"),
              "Bảng 12 · Xác định chỉ số khả nổ I<sub>EX</sub>."))

    b.append(h3("10.2.3 Chỉ số phơi nhiễm độc", "10.2.3 Toxic Exposure Subindex"))

    b.append(p("Mối nguy sức khỏe do hóa chất gây ra được thể hiện qua chỉ số "
               "phơi nhiễm độc I<sub>TOX</sub>. Đánh giá dựa trên <b>giá trị "
               "ngưỡng TLV</b> vì dữ liệu TLV có sẵn cho phần lớn các chất trong "
               "công nghiệp quá trình. TLV thể hiện giới hạn phơi nhiễm có hại "
               "trong thời gian ngưỡng 8 giờ; <b>TLV càng thấp (chất càng độc) "
               "thì giá trị chỉ số càng cao</b>. Việc dùng TLV cùng thời gian "
               "ngưỡng là quan trọng để kết quả so sánh được. Giới hạn điểm "
               "trong Bảng 13 dựa trên Mond Index (ICI, 1985)."))
    b.append(_score_table(_T13, ("Giới hạn độc (ppm)", "Điểm I<sub>TOX</sub>"),
              "Bảng 13 · Xác định chỉ số phơi nhiễm độc I<sub>TOX</sub>."))

    b.append(h3("10.2.4 Chỉ số khả ăn mòn", "10.2.4 Corrosiveness Subindex"))

    b.append(p("Vật liệu ăn mòn gồm ví dụ axit, anhydrid axit và kiềm. Các vật "
               "liệu này thường ăn mòn đường ống, bình chứa và thiết bị quá "
               "trình, có thể dẫn đến <b>mất containment (rò rỉ chất chứa)</b> và tiếp theo là cháy, nổ "
               "hoặc xả độc. Mối nguy rò rỉ phụ thuộc tính chất chất lỏng: một "
               "số chất lỏng ăn mòn bay hơi được, cháy được, độc, một số phản "
               "ứng dữ dội với hơi nước. Axit và kiềm mạnh gây bỏng và tổn "
               "thương mắt cho nhân viên."))
    b.append(p("Ăn mòn thường được đo bằng <b>tốc độ ăn mòn mm/a</b>; vật liệu "
               "được chọn sao cho phần dự trữ ăn mòn không bị vượt quá trong "
               "tuổi thọ thiết bị. Tuy nhiên, tốc độ ăn mòn không phải lúc nào "
               "cũng biết được ở khâu thiết kế sơ bộ, dù loại vật liệu thô "
               "thường đã được dự kiến. Vì nhu cầu vật liệu tốt hơn phần lớn "
               "cho thấy điều kiện ăn mòn khắc nghiệt hơn, phân loại theo loại "
               "vật liệu kết cấu có thể hợp lý. Trong ISI, khả ăn mòn được xác "
               "định trên cơ sở <b>vật liệu kết cấu yêu cầu</b> (Bảng 14): thép "
               "carbon đủ → 0; thép không gỉ → 1; vật liệu đặc biệt → 2. Ước "
               "tính thực hiện cho từng dòng quá trình và <b>trường hợp xấu "
               "nhất</b> cho giá trị cuối."))
    b.append(_score_table(_T14, ("Vật liệu kết cấu yêu cầu", "Điểm I<sub>COR</sub>"),
              "Bảng 14 · Xác định chỉ số khả ăn mòn I<sub>COR</sub>."))

    b.append(note("Tổng điểm của các chỉ số hóa học theo Bảng 9–14 tạo thành "
                  "I<sub>CI</sub> theo Phương trình 4 (Chương 8): "
                  "I<sub>RM,max</sub> + I<sub>RS,max</sub> + I<sub>INT,max</sub> "
                  "+ (I<sub>FL</sub> + I<sub>EX</sub> + I<sub>TOX</sub>)<sub>max</sub> "
                  "+ I<sub>COR,max</sub>, với tối đa 28 điểm."))

    return "".join(b)


def body_en():
    b = []

    b.append(h2("10. Subindices of Chemical Inherent Safety Index",
                "10. Chỉ số thành phần của chỉ số an toàn nội tại hóa học"))

    b.append(p("The Chemical Inherent Safety Index deals with the hazards "
               "related to <b>the chemical properties of the substances in the "
               "process</b>. The Index has been divided into subindices for "
               "<b>reaction hazards</b> and <b>hazardous substances</b>."))

    # ---- 10.1 ----------------------------------------------------------------
    b.append(h3("10.1 Subindices of Reaction Hazards",
                "10.1 Các chỉ số thành phần của mối nguy phản ứng"))

    b.append(p("The Inherent Safety Index (ISI) deals with both the main "
               "reaction(s) and those side reactions taking place in the "
               "reactor which are meaningful. It also deals with chemical "
               "interaction, which describes unintentional chemical reactions "
               "that can take place among the chemicals in the plant."))

    b.append(h3("10.1.1 Reaction Heat Subindex for the Main Reaction",
                "10.1.1 Chỉ số nhiệt phản ứng chính"))

    b.append(p("Since the possible violence of reactions lies in the heat "
               "liberated and the temperature which may be reached, <b>the "
               "energy change during the reaction</b> has been selected to "
               "present the reaction safety in the ISI. This is a feasible "
               "approach since the formation enthalpies are known for most "
               "substances."))
    b.append(p("The enthalpy released or absorbed in a process can be described "
               "by Equation 6 for constant-volume conditions and an isobaric "
               "process. While determining the safety subindex I<sub>RM</sub>, "
               "the heat release of the main reaction is calculated for the "
               "<b>total reaction mass</b> (i.e. both the reactants and the "
               "diluents are included) to take account of the heat capacity of "
               "the system, which absorbs part of the energy released:"))
    b.append(eq("ΔH<sub>r</sub> = Σ(H<sub>f</sub>)<sub>products</sub> − "
                "Σ(H<sub>f</sub>)<sub>reactants</sub>", "(6)"))
    b.append(p("From the safety point of view it is important to know how "
               "exothermic the reaction is. The classification used by King "
               "(1990): the reaction is <b>extremely exothermic</b> "
               "(≥ 3000 J/g), <b>strongly exothermic</b> (< 3000 J/g), "
               "<b>moderately exothermic</b> (< 1200 J/g), <b>mildly "
               "exothermic</b> (< 600 J/g), <b>thermally neutral</b> "
               "(≤ 200 J/g) or <b>endothermic</b>. These values are also used "
               "for determining the scores of I<sub>RS</sub> (Table 9). If "
               "there are several main reactions, for instance a series "
               "reaction, the score of I<sub>RM</sub> is determined on the "
               "basis of the total reaction; if there are several reactors in "
               "the process, the score is determined on the reactor with the "
               "greatest heat release."))
    b.append(_score_table(_T9_EN, ("Heat of reaction / total reaction mass", "Score"),
              "Table 9 · Determination of the reaction heat subindices "
              "I<sub>RM</sub> and I<sub>RS</sub>."))

    b.append(h3("10.1.2 Reaction Heat Subindex for the Side Reactions",
                "10.1.2 Chỉ số nhiệt phản ứng phụ"))

    b.append(p("The subindex I<sub>RS</sub> of the heat of side reactions is "
               "determined in a similar way to I<sub>RM</sub>. The heat release "
               "for each possible side reaction is calculated according to "
               "Equation 6 for the full reaction mass including diluents; the "
               "same safety scores as for the main reaction are used (Table 9). "
               "<b>The greatest heat-of-reaction value of all side reactions</b> "
               "is used for determining I<sub>RS</sub>."))

    b.append(h3("10.1.3 Chemical Interaction Subindex",
                "10.1.3 Chỉ số tương tác hóa học"))

    b.append(p("Chemical interaction considers the unwanted reactions of the "
               "process substances with materials in the plant area. These "
               "reactions are not expected to take place in the reactor and "
               "are therefore not covered by the side-reaction subindex. The "
               "ISI has utilized <b>EPA's matrix</b> (Hatayama et al., 1980) "
               "to classify the hazards of chemical interaction; <b>the worst "
               "interaction</b> between the substances present in the plant "
               "area is used in the calculations."))
    b.append(p("In Table 10 the score limits for I<sub>INT</sub> range from 0 "
               "to 4. <b>Fire and explosion</b> are considered the most "
               "hazardous consequences of an interaction (score 4). The score "
               "value for the formation of <b>toxic or flammable gas</b> "
               "depends on the amount and harmfulness of the gas (score 2–3); "
               "likewise, <b>the more heat is formed, the higher the score</b> "
               "(1–3). <b>Rapid polymerization</b> is valued on the basis of "
               "the polymerization rate (2–3). Soluble toxic chemicals and the "
               "formation of harmless, nonflammable gases are considered less "
               "harmful — score 1."))
    b.append(_score_table(_T10_EN, ("Chemical interaction", "Score of I<sub>INT</sub>"),
              "Table 10 · Determination of the chemical interaction subindex "
              "I<sub>INT</sub>."))

    # ---- 10.2 ----------------------------------------------------------------
    b.append(h3("10.2 Subindices for Hazardous Substances",
                "10.2 Các chỉ số thành phần cho chất nguy hiểm"))

    b.append(p("The flammability, explosiveness and toxic exposure subindices "
               "(I<sub>FL</sub>, I<sub>EX</sub>, I<sub>TOX</sub>) are "
               "determined <b>for each substance</b> present in the process. "
               "These indices are summed for every substance separately and "
               "<b>the maximum sum</b> is used as the subindex value. The "
               "corrosiveness subindex is determined on the basis of the most "
               "corrosive material in the process."))

    b.append(h3("10.2.1 Flammability Subindex", "10.2.1 Chỉ số khả cháy"))

    b.append(p("The flammability subindex describes the flammability of liquids "
               "e.g. in the case of a leakage. Flammability of liquids is "
               "measured by their <b>flash points</b> and <b>boiling points</b>. "
               "The classification used is based on the EU directive (Pyötsiä, "
               "1994): substances are divided into non-combustible, combustible, "
               "flammable, easily flammable and very flammable (Table 11)."))
    b.append(_score_table(_T11_EN, ("Flammability", "Score of I<sub>FL</sub>"),
              "Table 11 · Determination of the flammability subindex "
              "I<sub>FL</sub>."))

    b.append(h3("10.2.2 Explosiveness Subindex", "10.2.2 Chỉ số khả nổ"))

    b.append(p("In the ISI the explosiveness is considered through a chemical "
               "property which is not directly the same as the process "
               "explosion hazard, but can serve as a fire estimate. The "
               "explosiveness subindex describes <b>the tendency of a gas to "
               "form an explosive mixture with air</b>. Explosive ranges, "
               "expressed in per cent by volume of fuel vapour in air, are the "
               "concentration ranges in which a vapour/gas mixture with air "
               "will burn when ignited; flame propagation occurs if a mixture "
               "within its explosive range is ignited. The range is indicated "
               "by the <b>LEL</b> (lower explosive limit) and <b>UEL</b> "
               "(upper explosive limit). This model is a coarse estimation but "
               "useful when most chemical properties are not available. The "
               "explosiveness is determined by the difference UEL − LEL of the "
               "substance, divided into four steps (Table 12)."))
    b.append(_score_table(_T12_EN, ("Explosiveness (UEL − LEL), vol %",
                                    "Score of I<sub>EX</sub>"),
              "Table 12 · Determination of the explosiveness subindex "
              "I<sub>EX</sub>."))

    b.append(h3("10.2.3 Toxic Exposure Subindex", "10.2.3 Chỉ số phơi nhiễm độc"))

    b.append(p("Health hazards caused by chemicals are represented by the toxic "
               "exposure subindex I<sub>TOX</sub>. The evaluation is based on "
               "<b>Threshold Limit Values (TLV)</b>, because TLV data is readily "
               "available for most substances in the process industry. TLV "
               "values express the harmful exposure limits of substances in the "
               "threshold time of 8 hours; <b>the lower the TLV (the more toxic "
               "the substance), the higher the index value</b>. It is important "
               "to use TLVs with the same threshold time so that the results "
               "are comparable. The score limits in Table 13 are based on the "
               "Mond Index (ICI, 1985)."))
    b.append(_score_table(_T13_EN, ("Toxic limit (ppm)", "Score of I<sub>TOX</sub>"),
              "Table 13 · Determination of the toxic exposure subindex "
              "I<sub>TOX</sub>."))

    b.append(h3("10.2.4 Corrosiveness Subindex", "10.2.4 Chỉ số khả ăn mòn"))

    b.append(p("Corrosive materials include e.g. acids, acid anhydrides and "
               "alkalies. Such materials often corrode pipes, vessels and other "
               "process equipment, which may result in a <b>loss of "
               "containment</b> and a subsequent fire, explosion or toxic "
               "release. Danger from leaks depends on the properties of the "
               "fluids: some corrosive fluids are volatile, flammable and "
               "toxic; some react violently with moisture. Strong acids and "
               "alkalies cause burns and eye damage to personnel."))
    b.append(p("Corrosion is usually measured as <b>corrosion rates mm/a</b>; "
               "the material is selected so that the corrosion allowance is not "
               "exceeded during the lifetime of the equipment. However, the "
               "corrosion rates are not always known during predesign, though a "
               "rough type of construction material is often anticipated. Since "
               "the need for a better material most often indicates more "
               "corrosive conditions, a classification based on the type of "
               "construction material can be justified. In the ISI, "
               "corrosiveness is determined on the basis of the <b>required "
               "construction material</b> (Table 14): if carbon steel is enough, "
               "the index value is 0; for stainless steel 1; for all special "
               "materials 2. The estimation is made for each process stream "
               "separately, and <b>the worst case</b> gives the final index "
               "value."))
    b.append(_score_table(_T14_EN, ("Construction material required",
                                    "Score of I<sub>COR</sub>"),
              "Table 14 · Determination of the corrosiveness subindex "
              "I<sub>COR</sub>."))

    b.append(note("The chemical subindex scores of Tables 9–14 assemble into "
                  "I<sub>CI</sub> per Equation 4 (Chapter 8): "
                  "I<sub>RM,max</sub> + I<sub>RS,max</sub> + I<sub>INT,max</sub> "
                  "+ (I<sub>FL</sub> + I<sub>EX</sub> + I<sub>TOX</sub>)<sub>max</sub> "
                  "+ I<sub>COR,max</sub>, with a maximum of 28 points."))

    return "".join(b)
