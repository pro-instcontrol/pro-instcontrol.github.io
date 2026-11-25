# -*- coding: utf-8 -*-
"""Book 9, Chapter 5 (part A) — chapter opening: Abstract, Keywords and
Introduction (EN/VI bilingual).

Source: Ming Ding and Jie Huang, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 95–97,
printed pp. 79–81. The printed chapter title and byline are rendered by the
page shell in `ppic_ch05.py`; this module starts with the ABSTRACT heading.
The closing sentences of the Introduction continue past the decoded-text
line boundary (source lines 2478–2581) so the paragraph is not left broken.
No figures, tables or numbered equations occur in this source range.
"""
import ppicfig5 as F  # noqa: F401  (shared figure registry import style)
from ppic_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 5."""
    b = []

    # ---------------------------------------------------------------- ABSTRACT
    H(b, lang, "TÓM TẮT", "ABSTRACT", level=2)
    P(b, lang,
      "Với sự phát triển nhanh chóng của năng lượng hạt nhân, thori đang thu hút "
      "sự chú ý nhờ trữ lượng phong phú và các đặc tính vật lý xuất sắc. So với "
      "lò nước nhẹ, lò phản ứng khí nóng nhiệt độ cao kiểu khối (HTR) là lựa chọn "
      "tốt hơn cho nhiên liệu gốc thori vì đạt cháy sâu cao hơn và phổ neutron "
      "cứng hơn. Khi sử dụng thori trong lò HTR dạng khối, thành phần và sự phân "
      "bố không gian của nhiên liệu thori/urani là hai yếu tố quyết định hiệu "
      "năng hạt nhân. Bốn mức tách không gian của nhiên liệu thori/urani — không "
      "tách, tách ở cấp TRISO, tách ở cấp kênh và tách ở cấp khối — được định "
      "nghĩa cho lò HTR kiểu khối chạy nhiên liệu thori. Sơ đồ tính toán hai bước "
      "đã được dùng để thu được các đặc tính neutron, gồm tồn kho ban đầu của "
      "U‐235, hệ số nhân hiệu dụng và tỷ lệ chuyển đổi trung bình. Dựa trên các "
      "dữ liệu này, chi phí chu trình nhiên liệu của các mức tách không gian khác "
      "nhau có thể được tính bằng phương pháp chi phí vòng đời san đều như một "
      "hàm của hàm lượng thori. Chi phí chu trình nhiên liệu thay đổi theo cùng "
      "xu hướng với tồn kho ban đầu của U‐235 trong lõi lò, bởi tồn kho này quyết "
      "định 70% tổng chi phí. Khi hàm lượng thori không đổi, tồn kho ban đầu của "
      "U‐235 giảm khi mức tách không gian tăng, vì hiệu ứng tự che chắn không gian "
      "được tăng cường bởi mức tách cao hơn.",
      "With the rapid development of nuclear energy, thorium has been gaining "
      "attention because of its abundant reserves and excellent physical "
      "properties. Compared with light-water reactors, block-type high "
      "temperature gas cooled reactors (HTRs) are a better choice for "
      "thorium-based fuel for higher burnup and harder neutron spectrum. When "
      "using thorium in block-type HTRs, the composition and spatial "
      "distribution of thorium/uranium fuels are two determined factors of "
      "nuclear performance. Four spatial separation levels of thorium/uranium "
      "fuels, no separation level, TRISO level, channel level, and block level, "
      "are defined for the block-type thorium-fueled HTRs. A two-step "
      "calculation scheme was used to obtain the neutronic performance, "
      "including the initial inventory of U-235, effective multiplication "
      "factor, and average conversion ratio. Based on these data, the fuel "
      "cycle cost of different spatial separation levels can be calculated by "
      "the levelized lifetime cost method as a function of thorium content. "
      "The fuel cycle cost changes with the same trend as the initial inventory "
      "of U-235 in the reactor cores because the latter determines 70% of the "
      "total cost. When the thorium content is constant, the initial inventory "
      "of U-235 decreases with the increase of the spatial separation level "
      "because spatial self-shielding effect is strengthened by the latter.")

    # ---------------------------------------------------------------- KEYWORDS
    P(b, lang,
      "<b>Từ khóa:</b> hiệu ứng tách không gian, Th/U MOX, khái niệm hạt "
      "giống–tấm chắn (S&#38;B), khái niệm S&#38;B cho toàn bộ cụm nhiên liệu (WASB), "
      "lò HTR dạng khối, phân tích chi phí chu trình nhiên liệu",
      "<b>Keywords:</b> spatial separation effects, Th/U MOX, seed-and-blanket "
      "concept, whole assembly seed-and-blanket concept, block-type HTRs, fuel "
      "cycle cost analysis")

    # ------------------------------------------------------------ INTRODUCTION
    H(b, lang, "GIỚI THIỆU", "INTRODUCTION", level=2)
    P(b, lang,
      "Trong giai đoạn giữa thập niên 1950 đến giữa thập niên 1970, một số loại "
      "nhiên liệu MOX Th/U khác nhau, ví dụ (Th,U)O₂ hoặc (Th,U)C₂, đã được thử "
      "nghiệm và sử dụng làm nhiên liệu trong lò phản ứng khí nóng nhiệt độ cao "
      "(HTR), như AVR và THTR ở Đức [1] và Fort St. Vrain ở Hoa Kỳ [2]. Ba lý do "
      "chính đã thúc đẩy việc trình diễn chu trình nhiên liệu Th‐U vào thời điểm "
      "đó. Thứ nhất, so với urani đã biết, thori phong phú gấp ba lần trong tự "
      "nhiên. Thứ hai, Th‐232 có tiềm năng hấp dẫn để sinh hiệu quả U‐233 có khả "
      "năng phân hạch trong phổ neutron nhiệt. U‐233 cũng được coi là tốt nhất so "
      "với hai đồng vị phân hạch phổ biến khác là U‐235 và Pu‐239, trong phổ "
      "neutron nhiệt hoặc siêu nhiệt, xét về mặt neutron học, vì số neutron phân "
      "hạch trên mỗi neutron bị hấp thụ cao hơn 10–20% so với U‐235 và Pu‐239. "
      "Cuối cùng, vào giai đoạn đầu phát triển năng lượng hạt nhân, người ta tin "
      "rằng tài nguyên urani không đủ để hỗ trợ phát triển công nghiệp hạt nhân "
      "quy mô lớn.",
      "During the mid-1950s to the mid-1970s, some different types of Th/U MOX "
      "fuels, for example (Th,U)O₂ or (Th,U)C₂, were tested and used as fuels "
      "in high-temperature gas-cooled reactors (HTRs), like AVR and THTR in "
      "Germany [1] and Fort St. Vrain in the USA [2]. Three main reasons "
      "inspired them to demonstrate Th-U fuel cycle at that time. First, "
      "compared with kwon uranium, thorium is three times more abundant in "
      "nature. Second, Th-232 has an attractive potential for breeding to "
      "fissile U-233 efficiently in thermal neutron spectrum. U-233 is also "
      "considered as the best compared with other two common fissile isotopes, "
      "U-235 and Pu-239, in epithermal or thermal spectrum from neutronic point "
      "of view because the number of fission neutrons per neutron absorbed is "
      "10–20% higher than that of U-235 and Pu-239. Finally, uranium resources "
      "were believed to be insufficient to support the development of nuclear "
      "industries on a large scale at the early period of nuclear energy "
      "development.")
    P(b, lang,
      "Ngoài lò HTR, thori đã là nhiên liệu hạt nhân đáng chú ý cho nhiều ứng "
      "dụng lò phản ứng khác nhau [3], chẳng hạn lò muối nóng chảy (MSR) và lò "
      "làm mát bằng nước. Đặc biệt, kết hợp với nhiên liệu muối nóng chảy trong "
      "MSR, thori được dùng như một thành phần cần thiết của nhiên liệu "
      '"tiêu chuẩn" nhằm chuyển hóa thậm chí sinh Th‐232 thành U‐233 từ thập '
      "niên 1970 đến giữa thập niên 1980. Trong 20 năm qua, tiềm năng của thori "
      "đã được mở rộng sang quản lý chất thải phóng xạ và đốt cháy plutoni [4]. "
      "Trong ứng dụng này, Th‐232 được coi là đồng vị sinh sản tốt hơn U‐238 vì "
      "sự phá hủy ròng plutoni lớn hơn khi plutoni cấp vũ khí hoặc cấp lò phản "
      "ứng được đốt trong các lò phản ứng hạt nhân khác nhau. Hơn nữa, các lò "
      "chạy nhiên liệu thori tạo ra ít chất thải phóng xạ sống lâu hơn so với lò "
      "chạy nhiên liệu urani.",
      "Besides HTRs, thorium has been an interesting nuclear fuel for various "
      "reactor applications [3], such as molten-salt reactors (MSRs) and "
      "water-cooled reactors. Especially, combined with molten-salt fuel in "
      "MSRs, thorium was used as a necessary composition of the \"standard\" "
      "fuel aiming to converse and even breed Th-232 to U-233 from the 1970s "
      "to mid-1980s. In past 20 years, the potential of thorium has been "
      "extended to radioactive waste management and plutonium incineration "
      "[4]. In this application, Th-232 is considered as a better fertile "
      "isotope than U-238 because of a larger net destruction of plutonium, "
      "when weapon-grade or reactor-grade plutonium is burned in various "
      "nuclear reactors. Furthermore, thorium-fueled reactors generate less "
      "long-lived radioactive wastes than uranium-fueled ones.")
    P(b, lang,
      "Kết hợp với mục đích thương mại và quy mô ứng dụng tiềm năng, lò nước nhẹ "
      "(LWR) là lựa chọn tự nhiên về mặt lò phản ứng trong những năm gần đây vì "
      "có rất nhiều LWR trên khắp thế giới. Khái niệm hạt giống–tấm chắn (S&#38;B) "
      "đã được nhóm MIT xem xét lại cho ứng dụng trong LWR [5, 6]. Các khái niệm "
      "này bắt nguồn từ cấu hình S&#38;B và được phát triển cho chương trình ứng "
      "dụng lò nhân giống nước tiên tiến (AWBA), đồng thời được thử nghiệm "
      "trong lò nhân giống nước nhẹ (LWBR) tại Shippingport từ năm 1977 đến 1982 "
      "[7]. Nghiên cứu tiếp theo về LWR chạy nhiên liệu thori đã được Radkowsky "
      "và Galperin tiến hành [8]. Nhóm MIT đề xuất các cụm nhiên liệu không đồng "
      "nhất quy mô nhỏ và khái niệm S&#38;B cho toàn bộ cụm nhiên liệu (WASB). Hơn "
      "nữa, so với nghiên cứu trước đây, công trình gần đây của MIT đều dựa trên "
      "urani làm giàu thấp nhằm tăng khả năng chống phổ biến vũ khí hạt nhân.",
      "Combined with the commercial purpose and potential application scale, "
      "light-water reactors (LWRs) are a natural choice from the reactor point "
      "of view in recent years because of a large amount of LWRs all over the "
      "world. The seed-and-blanket (S&#38;B) concept has been reexamined for LWR "
      "application by the MIT group [5, 6]. The concepts originate from S&#38;B "
      "configuration and were developed for the advanced water breeder "
      "application (AWBA) program and tested in the light water breeder "
      "reactor (LWBR) at Shippingport from 1977 to 1982 [7]. Further work on "
      "thorium-fueled LWRs has been pursued by Radkowsky and Galperin [8]. The "
      "MIT group proposed the micro-heterogeneous fuel assemblies and the "
      "whole assembly seed-and-blanket (WASB) concept. Moreover, compared with "
      "the past research, the recent MIT work is all based on low-enriched "
      "uranium for proliferation resistance.")
    P(b, lang,
      "Do giới hạn cháy sâu của LWR (thường 50 GWd/tHM), một số nghiên cứu cho "
      "thấy tiềm năng của thori trong LWR bị hạn chế, và lò HTR là lựa chọn tốt "
      "hơn cho nhiên liệu gốc thori nhờ cháy sâu cao hơn và phổ neutron cứng hơn. "
      "Gần đây, khái niệm khối nhiên liệu S&#38;B đã được đưa vào U-battery [9], một "
      "lò HTR nhỏ có tuổi thọ dài, và GT-MHR thương mại [10], cũng như các lò "
      "nhiệt độ cao tiên tiến (AHTR) [11] dùng muối lỏng áp suất thấp (Flibe) làm "
      "chất làm mát, cho phép thiết kế lò công suất cao (ví dụ 2400–4000 MWth), "
      "nhiệt độ cao (850–950 °C) với khả năng an toàn hoàn toàn thụ động và sản "
      "xuất điện hoặc hydro một cách kinh tế.",
      "Because of the burnup limit of LWRs (usually 50 GWd/tHM), some research "
      "showed that the potential of thorium is limited in LWRs, and HTRs are a "
      "better choice for thorium-based fuel for higher burnup and harder "
      "neutron spectrum. Recently, the concept of S&#38;B fuel blocks has been "
      "introduced to the U-battery [9], a small long-life HTR, and a "
      "commercial-level GT-MHR [10], as well as advanced high-temperature "
      "reactors (AHTRs) [11] with low-pressure liquid-salt (Flibe) as coolant, "
      "which enables the design of a high-power (e.g., 2400–4000 MWth), "
      "high-temperature (850–950°C) reactor with fully passive safety "
      "capability and the economic production of electricity or hydrogen.")
    P(b, lang,
      "Các nghiên cứu trước đây đã chỉ ra rằng sự phân bố không gian của nhiên "
      "liệu thori và urani là yếu tố rất quan trọng đối với hiệu năng của lò chạy "
      "nhiên liệu thori, đồng thời đề xuất một số khái niệm thú vị về S&#38;B và "
      "WASB. Thực tế, các khái niệm khác nhau tương ứng với các mức tách không "
      "gian khác nhau của nhiên liệu thori/urani. Chương này cố gắng phân tích "
      "một cách hệ thống ảnh hưởng của sự tách không gian giữa nhiên liệu "
      "thori/urani đến hiệu năng hạt nhân của lò HTR dạng khối và đánh giá định "
      "lượng sự khác biệt bằng chi phí chu trình nhiên liệu. Phần thứ hai sẽ mô "
      "tả lò phản ứng, khối nhiên liệu và các mô hình tính toán, gồm mô hình tính "
      "vận chuyển có cháy sâu và mô hình chi phí chu trình nhiên liệu. Phần thứ "
      "ba sẽ trình bày kết quả tính toán của bốn mức tách không gian khác nhau và "
      "thảo luận sự khác biệt giữa chúng. Phần cuối sẽ kết luận chương.",
      "The past studies have shown the distribution of thorium and uranium "
      "fuels in space is a very important factor for the performance of "
      "thorium-fueled reactors and have proposed some interesting concepts of "
      "S&#38;B and WASB. Actually, the different concepts represent different "
      "separation levels of thorium/uranium fuels in space. The chapter tries "
      "to systematically analyze the spatial separation effects of "
      "thorium/uranium fuels on the nuclear performance of block-type HTRs and "
      "to quantitatively evaluate the difference by fuel cycle cost. The "
      "second section will describe the reactor, fuel block, and the "
      "calculation models, including the transport calculation model with "
      "burnup and fuel cycle cost model. The third section will present the "
      "calculation results of four different spatial separation levels and "
      "discuss the difference among them. The final section will conclude the "
      "chapter.")

    return b
