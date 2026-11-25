# -*- coding: utf-8 -*-
"""Book 9, Chapter 7 (part E) - Figure 7.2, Table 7.6 and the summary of
significant strategic impacts (EN/VI).

Source: work/ppic_raw.txt, absolute lines 4088-4177 (PDF pp. 154-157,
printed pp. 138-141). Figure 7.2 and Table 7.6 are raster images in the PDF;
every rank code, objective number and explanation below is transcribed from
the page renders p154.png-p156.png. The source has no numbered equations.

Figure 7.2 is supplied by ``ppicfig7``. A neutral bilingual placeholder keeps
section() callable before the supplier module is integrated; any callable
already registered by the real supplier is left untouched.
"""
try:
    import ppicfig7 as F
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

from ppic_ch07_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

if not hasattr(F, "fig_f72"):
    _STUB_SVG = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 110" '
        'role="img"><rect x="1" y="1" width="678" height="108" rx="6" '
        'fill="#f4f6fa" stroke="#9aa7bd"/>'
        '<text x="340" y="45" text-anchor="middle" '
        'style="font:14px Helvetica,sans-serif;fill:#24364f">'
        'Examples of the presentation of obtained results in the form of '
        'graph</text>'
        '<text x="340" y="77" text-anchor="middle" '
        'style="font:12px Helvetica,sans-serif;fill:#5a6b82">'
        'Hình 7.2 / Figure 7.2</text></svg>'
    )
    _STUB_F72 = (
        _STUB_SVG,
        "Hình 7.2 · Ví dụ về cách trình bày kết quả thu được dưới dạng đồ thị",
        "Figure 7.2 · Examples of the presentation of obtained results in the "
        "form of graph",
        "Hai biểu đồ thanh ngang 3-D so sánh cường độ tác động của các mục "
        "tiêu SEA cho hai phương án xây dựng nhà máy điện.",
        "Two 3-D horizontal bar charts comparing the impact intensity of the "
        "SEA goals for two power-plant construction options.")
    setattr(F, "fig_f72", lambda _t=_STUB_F72: _t)

# ------------------------------------------------------------- Table 7.6
# Printed Table 6: identification and evaluation of strategically significant
# impacts, with explanations. The two-level head is flattened into four
# columns; group labels are strings -> rendered as full-width group rows by
# C.table(). Merged priority/explanation cells are filled only on the first
# row of each group, exactly as in the printed table.
_T76_HEAD_VI = ["Ưu tiên chiến lược", "Mục tiêu SEA", "Xếp hạng",
                "Giải thích lý do"]
_T76_HEAD_EN = ["Strategic priorities", "SEA objective", "Rank",
                "Reasons explanation"]

# ("GRP", vi label, en label)
# ("PRI", vi priority, en priority, [(objective, rank), ...], vi reason, en reason)
_T76_GROUPS = [
    ("GRP", "HỆ THỐNG NĂNG LƯỢNG", "ENERGY SYSTEM"),
    ("PRI",
     "Tái thiết các nhà máy nhiệt điện theo Chỉ thị về các nhà máy đốt lớn",
     "Reconstruction of thermal power plants pursuant to the Large "
     "Combustion Plants Directive",
     [("1", "R+3 / S"), ("2", "R+3 / L"), ("21", "R+3 / S")],
     "Người ta dự kiến chất lượng cuộc sống của người dân sẽ được cải thiện "
     "đáng kể ở cấp vùng thông qua giảm phát thải các chất ô nhiễm không khí "
     "và giảm tác động tiêu cực đến chất lượng nước. Việc áp dụng công nghệ "
     "tiên tiến trong các nhà máy nhiệt điện sẽ góp phần vào điều này.",
     "It is expected that people's quality of life will be significantly "
     "improved at the regional level by reducing emissions of ambient air "
     "pollutants and reducing negative impacts on water quality. The "
     "introduction of cutting edge technologies in thermal power plants will "
     "contribute to this."),
    ("PRI",
     "Phát triển các nhà máy nhiệt điện than mới có công suất 700MW vào năm "
     "2025 (350MW vào năm 2020)",
     "Development of new coal-fired thermal power plants of capacity of "
     "700MW by 2025 (350MW by 2020)",
     [("15", "N+3 / P"), ("17", "N+2 / S"), ("21", "R+2 / S")],
     "Dự kiến sẽ có những tác động tích cực đáng kể, thúc đẩy tăng trưởng "
     "kinh tế và giảm sự phụ thuộc vào nhập khẩu năng lượng thông qua việc "
     "sử dụng công nghệ mới trong quy trình sản xuất.",
     "Significant positive effects are expected, which will spur economic "
     "growth and reduce dependence on energy imports by using new "
     "technologies in production processes."),
    ("PRI",
     "Xây dựng nhà máy thủy điện tích năng 'Bistrica' và/hoặc nhà máy thủy "
     "điện tích năng 'Djerdap 3'",
     "Construction of the \u201cBistrica\u201d reversible hydropower plant "
     "and/or \u201cDjerdap 3\u201d reversible hydropower plant",
     [("3", "I-3 / S"), ("4", "I-2 / L"), ("6", "I-2 / S"),
      ("8", "N-2 / P"), ("15", "N+2 / P"), ("17", "N+3 / S"),
      ("18", "I-2 / S"), ("19", "N+3 / S"), ("21", "N+3 / S")],
     "Chắc chắn sẽ có các tác động xuyên biên giới tiêu cực đến chế độ thủy "
     "văn của các dòng nước nơi nhà máy thủy điện được xây dựng, điều này "
     "cũng có thể gây mất đất rừng và đất nông nghiệp ở thượng lưu điểm lấy "
     "nước (đập). Việc xây dựng nhà máy thủy điện có thể gây tác động thị "
     "giác đến chất lượng cảnh quan, nhưng cũng gây tác động đến đa dạng "
     "sinh học. Các tác động tích cực liên quan đến thúc đẩy tăng trưởng "
     "kinh tế, giảm phụ thuộc vào nhập khẩu năng lượng, tăng tỷ trọng điện "
     "năng sản xuất từ năng lượng tái tạo và đưa công nghệ sạch vào sản "
     "xuất điện.",
     "There will definitely be negative transboundary impacts on hydrological "
     "regime of watercourses on which hydropower plant will be built, which "
     "may also cause the loss of forest and agricultural lands upstream of "
     "water intake (dam). Construction of the hydropower plant could have "
     "visual impact on landscape quality, but also impact on biodiversity. "
     "Positive impacts relate to spurring economic growth, reduction in "
     "dependence on energy imports, increase in the share of power produced "
     "from renewable energy, and introduction of clean technologies in "
     "electricity production."),
    ("GRP", "NGUỒN NĂNG LƯỢNG TÁI TẠO", "RENEWABLE ENERGY SOURCES"),
    ("PRI",
     "Tăng tỷ trọng điện năng được sản xuất từ năng lượng tái tạo",
     "Increase in the share of power produced from renewable energy",
     [("1", "N+3 / L"), ("3", "I-2 / L"), ("8", "I-2 / P"),
      ("19", "N+3 / S"), ("21", "N+2 / S")],
     "Các tác động tích cực dự kiến sẽ góp phần giảm ô nhiễm không khí có hại "
     "bằng cách tăng sử dụng năng lượng tái tạo, tức là áp dụng công nghệ "
     "sạch trong quy trình sản xuất điện. Một số dự án có thể gây tác động "
     "tiêu cực đến một số tài nguyên thiên nhiên nhất định (tác động của "
     "các nhà máy thủy điện nhỏ đến nguồn nước) và đa dạng sinh học (tác "
     "động của các trang trại gió đến động vật chim và dơi).",
     "The expected positive effects will contribute to reducing harmful air "
     "pollution by increasing renewable energy use, i.e. by introducing clean "
     "technologies in electricity production processes. Certain projects can "
     "have negative effects on certain natural resources (effects of small "
     "hydropower plants on water resources) and biodiversity (effects of "
     "wind farms on ornithological fauna and chiropters)."),
    ("PRI",
     "Phát triển các nhà máy thủy điện (HPP) và nhà máy thủy điện nhỏ (SHPP)",
     "Development of HPPs and SHPPs",
     [("1", "R+3 / Lk"), ("3", "I-2 / L"), ("8", "I-2 / P"),
      ("19", "N+3 / S"), ("21", "N+2 / S"), ("3", "R-2 / P"),
      ("9", "N-3 / P"), ("17", "N+2 / S"), ("19", "N-2 / P"),
      ("21", "N-2 / P")],
     "Các tác động tích cực dự kiến sẽ góp phần giảm ô nhiễm không khí có hại "
     "bằng cách tăng sử dụng năng lượng tái tạo, tức là áp dụng công nghệ "
     "sạch trong quy trình sản xuất điện. Các tác động tiêu cực đến chế độ "
     "thủy văn của các dòng nước nơi chúng sẽ được xây dựng có khả năng xảy "
     "ra. Các nhà máy thủy điện. Những tác động này sẽ đặc biệt rõ rệt trong "
     "quá trình xây dựng các nhà máy thủy điện có nhà máy đặt ở chân đập và "
     "trong quá trình xây dựng các nhà máy thủy điện nhỏ do tạo ra một hồ "
     "nhân tạo ở thượng lưu đập, cũng như trong trường hợp nhiều nhà máy "
     "thủy điện và nhà máy thủy điện nhỏ được lên kế hoạch trên cùng một "
     "dòng nước (tác động tích lũy và cộng hưởng). Các tác động tích cực mang "
     "tính quốc gia liên quan đến các ví dụ về công nghệ sạch, nguồn năng "
     "lượng tái tạo và giảm phụ thuộc năng lượng thông qua khai thác tiềm "
     "năng thủy năng đáng kể chắc chắn sẽ xảy ra.",
     "The expected positive effects will contribute to reducing harmful air "
     "pollution by increasing renewable energy use, i.e. by introducing clean "
     "technologies in electricity production processes. The negative impacts "
     "on the hydrological regime of watercourses on which they will be built "
     "are likely to happen. Hydroelectric power plants. These impacts will be "
     "particularly pronounced during the construction of HPPs with "
     "powerhouse at the toe of the dam and during the construction of SHPPs "
     "as a result of creating an artificial lake upstream from the dam, as "
     "well as in cases when several HPPs and SHPPs are planned on the same "
     "watercourse (cumulative and synergistic impacts). The positive impacts "
     "of national character that relate to the examples of clean technologies, "
     "renewable energy sources and reduced energy dependence by using "
     "significant hydro-energy potentials are certain to happen."),
]


def _t76_rows(lang):
    """Flatten the printed table into rows for C.table()."""
    vi = lang == "vi"
    rows = []
    for g in _T76_GROUPS:
        if g[0] == "GRP":
            rows.append(g[1] if vi else g[2])
            continue
        _, pri_vi, pri_en, cells, why_vi, why_en = g
        pri = pri_vi if vi else pri_en
        why = why_vi if vi else why_en
        for i, (obj, rank) in enumerate(cells):
            rows.append([pri if i == 0 else "", obj, rank,
                         why if i == 0 else ""])
    return rows


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 7."""
    b = []

    FIG(b, 2, F.fig_f72(), lang)

    P(b, lang,
      "Việc đánh giá các ưu tiên chiến lược trong Chiến lược liên quan đến "
      "nhà máy điện, được phân tích chi tiết trong SEA, được trình bày tiếp "
      "theo đây.",
      "The evaluation of strategic priorities in the Strategy that relate to "
      "power plants, and which were elaborated in the SEA, is presented "
      "further herein.")

    P(b, lang,
      "Một bảng được lập dựa trên các tiêu chí đã được thông qua để xác định "
      "các tác động có ý nghĩa chiến lược (Bảng 3) và kết quả của đánh giá đa "
      "tiêu chí được trình bày dưới dạng ma trận (Bảng 5). Bảng xác định các "
      "ưu tiên chiến lược dẫn đến các tác động có ý nghĩa chiến lược (tích "
      "cực và tiêu cực) đối với chất lượng môi trường và các yếu tố phát "
      "triển bền vững, cụ thể là các mục tiêu SEA, đồng thời xếp hạng các "
      "tác động được xác định theo cách đó (Bảng 6).",
      "A table was formed based on the adopted criteria for determining the "
      "strategically significant impacts (Table 3) and results of the "
      "multi-criteria evaluation presented in the form of matrices (Table 5). "
      "The table identifies the strategic priorities that imply "
      "strategically significant impacts (positive and negative) on the "
      "environmental quality and elements of sustainable development, namely "
      "on the SEA goals, and determine the rank of impacts identified in such "
      "a way (Table 6).")

    TBL(b, lang, _T76_HEAD_VI, _T76_HEAD_EN, _t76_rows(lang),
        caption_vi="Bảng 7.6 · Xác định và đánh giá các tác động có ý nghĩa "
                   "chiến lược kèm giải thích [34]",
        caption_en="Table 7.6 · Identification and evaluation of "
                   "strategically significant impacts with explanations [34]")

    H(b, lang, "Tóm tắt các tác động chiến lược quan trọng",
      "Summary of Significant Strategic Impacts", level=3)

    P(b, lang,
      "Dựa trên kết quả đánh giá mức độ quan trọng của tác động được thể hiện "
      "trong Bảng 6, có thể kết luận rằng Chiến lược tạo ra một số lượng đáng "
      "kể các tác động môi trường quan trọng về mặt chiến lược, cả tích cực "
      "lẫn tiêu cực. Điều này hoàn toàn không đáng ngạc nhiên, bởi ý tưởng "
      "chính của Chiến lược là xây dựng một khái niệm phát triển ngành năng "
      "lượng dựa trên nguyên tắc phòng ngừa và bảo vệ tích cực môi trường "
      "cùng các yếu tố chính của nó, từ đó cũng cải thiện sức khỏe con người "
      "thông qua việc giảm vĩnh viễn mức độ tiếp xúc với ô nhiễm không khí "
      "phát sinh từ hoạt động của các nhà máy nhiệt điện vận hành với công "
      "nghệ không phù hợp.",
      "On the basis of the evaluation of impact significance shown in Table "
      "6, it can be concluded that the Strategy produces significant number "
      "of strategically important, both positive and negative, environmental "
      "impacts. This is not at all surprising considering that the main idea "
      "of the Strategy was to create a concept of development of an energy "
      "sector which would rely in all of its segments on the principles of "
      "the prevention and active protection of the environment, its main "
      "factors, thus also on the improvement of human health by primarily "
      "permanently reducing the exposure to air pollution resulting from the "
      "operation of thermal power plants operating with inadequate "
      "technologies.")

    P(b, lang,
      "Các tác động tiêu cực được xác định của Chiến lược là kết quả của sự "
      "phát triển ngành năng lượng vốn, tại Cộng hòa Serbia cũng như ở các "
      "quốc gia khác, chủ yếu dựa vào các tiềm năng năng lượng hiện có. Những "
      "tác động tiêu cực quan trọng nhất là kết quả của hoạt động của các "
      "nhà máy nhiệt điện, cụ thể là kết quả của việc khai thác than bề mặt "
      "cần thiết cho hoạt động của chúng. Trong bối cảnh này, các tác động "
      "lên các yếu tố môi trường chính (không khí, nước, đất và đa dạng sinh "
      "học), cũng như tác động lên cảnh quan, nổi bật về tầm quan trọng. Các "
      "tác động lên các yếu tố xã hội do việc mở rộng các mỏ lộ thiên, dẫn "
      "đến một phần thậm chí toàn bộ các khu định cư phải được chuyển đến một "
      "địa điểm hoàn toàn mới, có ý nghĩa đặc biệt.",
      "The identified negative impacts of the Strategy are the result of "
      "development in the energy sector which, in the Republic of Serbia "
      "like in other countries, dominantly relies on the existing energy "
      "potentials. The most important negative impacts are the result of "
      "thermal power plant operations, namely the result of the surface coal "
      "exploitation necessary for their operation. In this context, the "
      "impacts of the main environmental factors (air, water, soil and "
      "biodiversity), as well as impacts on landscape, stand out by their "
      "importance. The impacts on social factors as the result of extension "
      "of open-pit mines, due to which parts or even entire settlements are "
      "moved to completely new location, are of special importance.")

    P(b, lang,
      "Hầu hết các tác động đã nêu không phân bố rộng về mặt không gian, "
      "nhưng dù sao chúng vẫn được đánh giá là có tầm quan trọng chiến lược "
      "do cường độ tác động được đánh giá, như thể hiện trong Bảng 6.",
      "Most of the mentioned impacts are not significantly spatially "
      "dispersed, but, nevertheless, they were assessed as being of strategic "
      "importance due to the assessed impact intensity, as shown in Table 6.")

    P(b, lang,
      "Một số hệ quả tiêu cực cũng được dự kiến do việc xây dựng nhà máy thủy "
      "điện tích năng 'Bistrica' và/hoặc xây dựng nhà máy thủy điện tích năng "
      "'Djerdap 3', những công trình sẽ gây tác động tiêu cực đến chế độ thủy "
      "văn của các dòng nước nơi chúng được lên kế hoạch xây dựng, cũng như "
      "đến đa dạng sinh học và hệ động vật cá, đồng thời gây ra những thay "
      "đổi có thể xảy ra trong việc sử dụng đất nông nghiệp và đất rừng.",
      "Certain negative implications are also expected due to the "
      "construction of the \u2018Bistrica\u2019 HPP and/or construction of "
      "the \u2018Djerdap 3\u2019 reversible HPP, which would have negative "
      "effects on hydrological regime of watercourses on which their "
      "construction is planned, as well as on biodiversity and ichthyofauna, "
      "and will cause possible changes in the use of agricultural and forest "
      "lands.")

    P(b, lang,
      "Bằng cách chấp nhận các quy định của Công ước Espoo [56] và Nghị định "
      "thư Kiev [57], Cộng hòa Serbia có nghĩa vụ thông báo cho các quốc gia "
      "láng giềng về các dự án có thể gây tác động xuyên biên giới. Theo Công "
      "ước Espoo về Đánh giá tác động môi trường trong bối cảnh xuyên biên "
      "giới (Công ước Espoo), tác động xuyên biên giới được định nghĩa là "
      "tất cả các tác động (tích cực và tiêu cực) của một hoạt động hoặc dự "
      "án nhất định ảnh hưởng đến môi trường thuộc thẩm quyền của quốc gia "
      "khác. Việc thực hiện các quy định của Công ước Espoo đòi hỏi các cơ "
      "quan liên quan của các quốc gia láng giềng phải cung cấp thông tin về "
      "các hoạt động đã được lên kế hoạch và tác động môi trường của chúng, "
      "để quốc gia chịu ảnh hưởng có thể tham gia vào việc đưa ra các quyết "
      "định tối ưu về hoạch định và triển khai trong tương lai các hoạt động "
      "đó.",
      "By accepting the provisions of the Espoo Convention [56] and Kiev "
      "Protocol [57], the Republic of Serbia is obligated to notify the "
      "neighbouring countries on the projects that could have transboundary "
      "impacts. According to the Espoo Convention on Environmental Impact "
      "Assessment in a Transboundary Context (Espoo Convention), the "
      "transboundary impacts are defined as all impacts (positive and "
      "negative) of a certain activity or a project that affect the "
      "environment under the jurisdiction of another country. The "
      "implementation of the Espoo Convention provisions implies that the "
      "relevant institutions of the neighbouring countries should provide "
      "information on the planned activities and their environmental impacts "
      "so that the affected country could participate in making optimum "
      "decisions on planning and future realization of such activities.")

    P(b, lang,
      "Ngoài các dự án được xác định trong Chiến lược có thể gây tác động "
      "xuyên biên giới, chẳng hạn như các dự án RHPP 'Bistrica' và/hoặc RHPP "
      "'Djerdap 3', tác động môi trường xuyên biên giới còn có thể phát sinh "
      "từ việc triển khai các dự án sau:",
      "In addition to the projects defined by the Strategy that could have "
      "transboundary impacts, such as the RHPP \u2018Bistrica\u2019 and/or "
      "RHPP \u2018Djerdap 3\u2019 projects, the transboundary environmental "
      "impacts can also occur as the result of the realization of the "
      "following projects:")

    L(b, lang,
      ["Các trang trại gió — tác động xuyên biên giới có thể xảy ra đối với "
       "động vật bay (động vật chim và dơi) tại biên giới giữa Serbia và "
       "Romania (thực tế là tất cả các dự án trang trại gió dự kiến xây dựng "
       "ở phía đông bắc của Cộng hòa Serbia);",
       "Các nhà máy thủy điện nhỏ trên các dòng nước xuyên biên giới (thực "
       "tế là các dòng nước chảy từ lãnh thổ Cộng hòa Serbia sang lãnh thổ "
       "các nước láng giềng) — tác động bất lợi có thể xảy ra đối với sinh "
       "vật đáy và hệ động vật cá tại biên giới với Montenegro, Bosnia và "
       "Herzegovina và Romania;",
       "Các dự án nhà máy nhiệt điện than — tác động có thể xảy ra đối với "
       "chất lượng không khí và các dòng sông quốc tế."],
      ["Wind farms—possible transboundary impacts on the flying fauna "
       "(ornithological fauna and chiropters) on the border between Serbia "
       "and Romania (actually, all wind farm projects planned to be built in "
       "the north-eastern part of the Republic of Serbia);",
       "Small hydropower plants on transboundary watercourses (actually, the "
       "watercourses flowing from the territory of the Republic of Serbia "
       "into the territory of the neighbouring countries)—possible adverse "
       "impacts on benthonic organisms and ichthyofauna on boundaries with "
       "Montenegro, B&amp;H and Romania;",
       "Coal-fired power plant projects—possible impacts on the air quality "
       "and international rivers."])

    P(b, lang,
      "Không xác định được hoạt động nào khác dự kiến có thể gây ra các tác "
      "động xuyên biên giới có tầm quan trọng chiến lược.",
      "Other planed activities that can imply the transboundary impacts of "
      "strategic importance have not been identified.")

    P(b, lang,
      "Ngoài các tác động bất lợi, thông qua việc sử dụng phương pháp MCE khi "
      "thực hiện SEA cho Chiến lược, một loạt tác động tích cực có ý nghĩa "
      "chiến lược cũng đã được xác định:",
      "In addition to the adverse impacts, by using the MCE method in "
      "carrying out the SEA for the Strategy, a whole series of "
      "strategically significant positive impacts were also identified:")

    L(b, lang,
      ["Chất lượng môi trường: các tác động tích cực đến chất lượng của các "
       "yếu tố môi trường chính (không khí, nước và đất) và giảm phát thải "
       "khí nhà kính (GHG) thông qua tăng sử dụng năng lượng tái tạo (RES) và "
       "sử dụng công nghệ sạch trong các nhà máy nhiệt điện theo Chỉ thị "
       "2001/80/EC về việc hạn chế phát thải của một số chất ô nhiễm vào không "
       "khí từ các nhà máy đốt lớn và theo Chỉ thị 2010/75/EU về phát thải "
       "công nghiệp đối với các dự án mới; rút bỏ tất cả các nhà máy nhiệt điện "
       "có công suất phát điện dưới 300 MW; việc thực hiện một loạt biện pháp "
       "tiết kiệm năng lượng sẽ góp phần sử dụng năng lượng hợp lý hơn, tức là "
       "giảm lượng năng lượng phải sản xuất ra cho cùng một lượng năng lượng "
       "cần đáp ứng; cải thiện các quy định pháp lý trong lĩnh vực năng lượng "
       "và hài hòa hóa chúng với các quy định của EU; phát triển các thể chế để "
       "thực hiện các quy định pháp lý được cải thiện liên quan đến giảm ô "
       "nhiễm môi trường và các yếu tố môi trường chính;"],
      ["Environmental quality: positive impacts on the quality of main "
       "environmental factors (air, water and soil) and reduction of "
       "greenhouse gas (GHG) emissions by increasing the use of RES and the "
       "use of clean technologies in thermal power plants in accordance with "
       "Directive 2001/80/EC on the limitation of emissions of certain "
       "pollutants into the air from large combustion plants and with the "
       "Directive 2010/75/EU on industrial emissions for new projects; "
       "withdrawal of all thermal power plants with generating capacity less "
       "than 300 MW; the implementation of a whole set of energy-efficiency "
       "measures will contribute to more rational energy use, that is, "
       "reducing the production of the required amount of energy for the same "
       "amount of required energy; the improvement of legal regulations in the "
       "area of energy and their harmonization with the EU regulations; the "
       "development of institutions for the implementation of improved legal "
       "regulations related to the environmental pollution reduction and main "
       "environmental factors;"])

    return b
