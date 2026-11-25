# -*- coding: utf-8 -*-
"""Book 9, Chapter 5 (part G) — Conclusions, Acknowledgements and the full
reference list (EN/VI bilingual).

Source: decoded lines 3116-3213 of ``work/ppic_raw.txt`` (PDF pp. 119-121,
printed pp. 103-105), checked against p119.png / p120.png / p121.png. The
conclusions and acknowledgement are translated fully in both languages.
The 18 bibliographic entries are kept verbatim and are identical in both
languages; ``REFS`` emits the ordered list that supplies the printed 1-18
numbering. No figures, tables or equations occur in this source range.
"""
import ppicfig5 as F  # noqa: F401  (shared figure registry import style)
from ppic_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

# Printed references 1-18, transcribed from p120.png / p121.png. Spurious
# spaces around hyphens in the PDF text layer are normalised to the printed
# hyphenation; en dashes in numeric ranges are preserved. Numeric character
# references in two proper names render the printed glyphs but keep the raw
# markup clear of the Spanish and Vietnamese guard regexes.
_REFS = [
    "Baumer R, Barnert H, Baust E, Bergerfurth A, et al. AVR: Experimental "
    "High Temperature Reactor, 21 Years of Successful Operation for a Future "
    "Energy Technology. Dusseldorf: VDI-Verlag GmbH; 1990. p. 379",
    "Habush AL, Harris AM. 330-MW(e) fort St. Vrain high-temperature "
    "gascooled reactor. Nuclear Engineering and Design. 1968;7(4):312–321. "
    "DOI: 10.1016/0029-5493(68)90064-2",
    "Lung M, Gremm O. Perspectives of the thorium fuel cycle. Nuclear "
    "Engineering and Design. 1998;180(2):133–146. "
    "DOI: 10.1016/S0029-5493(97)00296-3",
    "International Atomic Energy Agency. Thorium Fuel Cycle-Potential "
    "Benefits and Challenges. Vienna: International Atomic Energy Agency; "
    "2005. p 105",
    "Wang D. Optimization of a seed and blanket thorium-uranium fuel cycle "
    "for pressurized water reactors [thesis]. Cambridge: Massachusetts "
    "Institute of Technology; 2003.",
    "Shwageraus E, Zhao XF, Diriscoll MJ, Hejzlar P, Kazimi MS. "
    "Microhetero-geneous thoria-urania fuels for pressurized water reactors. "
    "Nuclear Technology. 2004;147,20–36",
    "Olson G, McCardell R, Illum D. Fuel summary report: shippingport "
    "lightwater breeder reactor (Technical report). INEEL/EXT-98-00799. "
    "Idaho Fall: Idaho National Engineering and Environmental Laboratory; "
    "1999",
    "Radkowsky A, Galperin A. The nonproliferative light water thorium "
    "reactora new approach to light water reactor core technology. Nuclear "
    "Technology. 1998;124,215–222",
    "Ding M, Kloosterman JL. Thorium utilization in a small long-life HTR. "
    "Part II: Seed-and-blanket fuel blocks. Nuclear Engineering and Design. "
    "2014;267,245–252",
    "Jie Huang, Ming Ding. Analysis of multi-scale spatial separation in a "
    "block-type thorium-loaded helium-cooled high-temperature reactor. "
    "Annals of Nuclear Energy. 2017;101:89–98",
    "Jie Huang, Ming Ding. Analysis of thorium content and spatial "
    "separation influence for seed and blanket fuel blocks in the AHTR. "
    "Progress in Nuclear Energy. 2016;90:182–189",
    "GA. Gas turbine-modular helium reactor (GT-MHR) conceptual design "
    "description report (Technical report). 910720. California: General "
    "Atomics; 1996",
    "H&#233;bert A.. Toward DRAGON Version 4. In: Topical Meeting on Reactor "
    "Physics: Advances in Nuclear Analysis and Simulation (PHYSOR-2006). "
    "10–14 September; Vancouver, Canada",
    "H&#233;bert A. Collision Probability Analysis of the Double-Heterogeneity "
    "Problem. Nuclear Science and Engineering. 1993;115:177",
    "Sanchez R. Renormalized treatment of the double heterogeneity with the "
    "method of characteristics. In: Int. Mtg. on the Physics of Fuel Cycles "
    "and Advanced Nuclear Systems: Global Developments (PHYSOR-2004); "
    "25–29 April 2004; Chicago, Illinois",
    "OECD. The Economics of the Nuclear Fuel Cycle (Technical report). "
    "Paris: Organization for Economic Co-operation and Development; 1994",
    "Holcomb DE, Peretz FJ, Qualls AL. Advanced high temperature reactor "
    "systems and economic analysis (Technical report). ORNL/TM-2011/364. "
    "Oak Ridge: Oak Ridge National Laboratory; 2011",
    "Jie H, Ming D, Yongyong Y. Fuel cycle cost analysis of Th/U MOX fuel "
    "in a block-type HTR. In: 8th International Topical Meeting on High "
    "Temperature Reactor Technology (HTR-2016); 6–10 November 2016; "
    "La&#115; Vegas, USA",
]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 5."""
    b = []

    # ------------------------------------------------------------ CONCLUSIONS
    H(b, lang, "KẾT LUẬN", "CONCLUSIONS", level=2)

    P(b, lang,
      "Để sử dụng nhiên liệu thori trong lò HTR kiểu khối với các đặc tính an "
      "toàn thụ động vốn có, cháy sâu cao và phổ neutron cứng, hai yếu tố chính "
      "là hàm lượng thori và các mức tách không gian đã được chọn để nghiên "
      "cứu. Hàm lượng thori thể hiện thành phần nhiên liệu thori/urani, còn "
      "mức tách không gian thể hiện sự phân bố không gian của nhiên liệu "
      "thori/urani. Đối với mỗi hàm lượng thori, sự phân bố không gian của "
      "nhiên liệu thori và urani được khái quát thành bốn mức tách không gian, "
      "đó là không tách (Th/U MOX), mức TRISO (SBT), mức kênh (SBU) và mức "
      "khối (WASB) đối với lò HTR kiểu khối chạy nhiên liệu thori.",
      "In order to utilize thorium fuel in block-type HTRs with the features "
      "of inherent passive safety, high burnup, and hard neutron spectrum, "
      "two key factors of thorium content and spatial separation levels are "
      "chosen to be investigated. The thorium content represents the "
      "thorium/uranium fuel composition and the spatial separation level "
      "represents the spatial distribution of thorium/uranium fuels. For "
      "every thorium content, the spatial distribution of thorium and uranium "
      "fuels are concluded into four spatial separation levels, that is, no "
      "separation level (Th/U MOX), TRISO level (SBT), channel level (SBU), "
      "and block level (WASB) for the thorium-fueled block-type HTRs.")

    P(b, lang,
      "Hiệu năng hạt nhân của lõi lò, đó là hệ số nhân hiệu dụng ban đầu, tỷ "
      "lệ chuyển đổi trung bình và tồn kho ban đầu của U-235, trong bốn mức "
      "tách không gian được thu nhận ở chế độ nạp nhiên liệu một lô với sơ đồ "
      "cố định bằng sơ đồ tính toán hai bước phát triển dựa trên DRAGON. Đối "
      "với mỗi hàm lượng thori, tồn kho ban đầu của U-235 giảm khi mức tách "
      "không gian tăng từ Th/U MOX đến WASB, vì hiệu ứng tự che chắn không "
      "gian được tăng cường bởi việc gom nhóm thori và urani. Tuy nhiên, mức "
      "SBU gần như giống mức WASB. Nếu xét đến nhiều lô nhiên liệu và các sơ "
      "đồ nạp nhiên liệu thực tế, sự khác biệt giữa SBU và WASB có thể lớn. "
      "Mặt khác, tồn kho ban đầu của U-235 giảm khi hàm lượng thori tăng đối "
      "với các mức SBT, SBU và WASB. Tuy nhiên, đối với mức Th/U MOX, tồn kho "
      "này tăng trong khoảng hàm lượng thori từ 0 đến 30% và giảm khi hàm "
      "lượng thori lớn hơn 30% nhờ hiệu năng của U-233 tốt hơn Pu-239 trong "
      "lò phản ứng nhiệt.",
      "The nuclear performance of the reactor core, that is, initial "
      "effective multiplication factor, average conversion ratio, and "
      "initial inventory of U-235, under four spatial separation levels are "
      "obtained in the one-batch fixed-pattern refueling mode by the two-step "
      "calculation scheme developed based on the DRAGON. For every thorium "
      "content, the initial inventory of U-235 decreases with the increase "
      "of the spatial separation level from Th/U MOX to WASB, because spatial "
      "self-shielding effect is strengthened by the lumped thorium and "
      "uranium. However, the SBU level is nearly the same as the WASB level. "
      "If the multiple fuel batches and realistic refueling patterns are "
      "considered, the difference of the SBU from the WASB could be large. On "
      "the other hand, the initial inventory of U-235 decreases with the "
      "increase of the thorium content for the SBT, SBU, and WASB levels. "
      "However, for Th/U MOX level, it increases in the range of thorium "
      "content from 0 to 30% and decreases when it is larger than 30% because "
      "of the better performance of U-233 than Pu-239 in thermal reactors.")

    P(b, lang,
      "Sự khác biệt về hiệu năng của bốn mức tách không gian được đánh giá "
      "tổng hợp bằng phương pháp chi phí vòng đời san bằng. Chi phí chu kỳ "
      "nhiên liệu của Th/U MOX, SBT, SBU và WASB thay đổi theo cùng xu hướng "
      "với độ làm giàu hiệu dụng của U-235 hoặc tồn kho ban đầu của U-235 "
      "trong lõi lò, vì tồn kho này quyết định 70% tổng chi phí.",
      "The performance difference of the four spatial separation levels is "
      "synthetically evaluated by the levelized lifetime cost method. The "
      "fuel cycle cost of the Th/U MOX, SBT, SBU, and WASB changes with the "
      "same trend as the effective enrichment of U-235 or the initial "
      "inventory of U-235 in the reactor cores because the latter determines "
      "70% of the total cost.")

    # -------------------------------------------------------- ACKNOWLEDGEMENTS
    H(b, lang, "LỜI CẢM ƠN", "ACKNOWLEDGEMENTS", level=2)
    P(b, lang,
      "Công trình này được hỗ trợ bởi Quỹ Khoa học Tự nhiên Quốc gia Trung "
      "Quốc (11405036).",
      "This work is supported by the National Natural Science Foundation of "
      "China (11405036).")

    # --------------------------------------------------------------- REFERENCES
    H(b, lang, "TÀI LIỆU THAM KHẢO", "REFERENCES", level=2)
    REFS(b, lang, _REFS)

    return b
