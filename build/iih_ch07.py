# -*- coding: utf-8 -*-
"""Book 8, Chapter 7 - Gas and Liquid Sampling Techniques in Process Industry (EN/VI bilingual).

Source: 3G E-learning LLC, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 257-302 (46 pages), printed pp. 243-288. Chapter
8 ("Control Valves") begins at PDFPAGE 303 and is excluded.  Printed page = PDF
page - 14.

The source order is kept: Introduction; Sampling of Gases and Liquids (Water
Sampling and the sorbent / stabilization tables); Flue Gas Analyzer (types,
gas chromatograph with its instrumental components and detector table, IR
analyzer, thermal conductivity analyzer, paramagnetic analyzer, electrochemical
analyzer, ORSAT apparatus, gravimetry, methanometer, zirconia systems and flue
gas composition); Combustion Analysis of Process Gases in Industry; and
Solid-Fuel-Fired Furnaces with the seven process flow charts and their
typical / limit value tables.  The 44 numbered references on printed pp.
285-287 are kept in source order.  "Citation:" lines are image credits, not
references, and are excluded.

Nine of the eleven data tables were printed as images in the source PDF and
lost their cell text in the OCR dump; their values were read directly from the
printed pages and are reproduced with the source number formats intact.  See
`source_notes` for the complete list of extraction quirks.
"""

import iih_common as C
import iihfig7 as F
from iih_common import (eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 46          # PDF pp. 257-302 inclusive (printed pp. 243-288)
BYLINE = "3G E-learning LLC · Illustrated Handbook of Industrial Instrumentation &amp; Control (2018)"
TITLE_EN = "Gas and Liquid Sampling Techniques in Process Industry"
TITLE_VI = "Kỹ thuật lấy mẫu khí và chất lỏng trong công nghiệp"


# ---------------------------------------------------------------------------
# Reference list (source printed pp. 285-287, numbered 1-44).  URLs broken
# across source lines are joined back into single links.  The text of every
# entry otherwise follows the printed source, including OCR damage such as
# "IYONI", "Koratochvil", "E S. Lee" and the mangled query string in ref. 2.
# The single bare ampersand (ref. 2) is XML-escaped.  "Citation:" lines are
# image credits and are not part of this list.
# ---------------------------------------------------------------------------
_REFS = [
    "http://www.globalspec.com/learnmore/manufacturing_process_equipment/"
    "materials_processing_equipment/gas_liquid_solids_samplers",
    "http://www.chromedia.org/chromedia?waxtrapp=fwyqcDsHiemBpdmBlIEcCK"
    "&amp;subNav=msmm yDsHiemBp dmBlIEcCKdB",
    "http://www.wisegeek.com/what-is-a-flue-gas-analyzer.htm",
    "http://instrumentationtools.com/oxygen-analyzer-working-principle/#."
    "WgKbYVuCzIX",
    "http://instrumentationtools.com/oxygen-analyzer-working-principle/#."
    "WgGuUluCzIU",
    "http://www.testo350.com/downloads/Flue_Gas_in_Industry_0981_2773.pdf",
    "https://www.automaatika.ee/pdf/106-510A.pdf",
    "http://www.shimadzu.com/an/ftir/support/ftirtalk/talk9/intro.html",
    "http://asgmt.com/wp-content/uploads/pdf-docs/2012/1/036.pdf",
    "Kevin Harris , Randy Hauer , Dan Potter “Combustibles measurement in "
    "sulfur recovery unit acid gas with a combined nduv/ndir analyzer” "
    "Analysis Division Symposium at ISA AD 2008; http://www.isa.org",
    "Matese. A, Gioli, B., Vaccari F. P., Zaldei A., and Miglietta, F. (2009) "
    "Carbon Dioxide Emissions of the City Center of Firenze, Italy: "
    "Measurement, Evaluation, and Source Partitioning. Journal of Applied "
    "Meteorology and Climatology (48), 1940-1948.",
    "Ocheltree, T. and Loescher H “General procedures for CO2 and H2O "
    "calibration of Infrared Gas Analyzers (IRGA) and Secondary Gas Standards “ "
    "(2010)",
    "Joseph E. Chilton, Charles D. Taylor, and Robert J. Timko “EVALUATION OF "
    "IYONI II METHANOMETERS” National Institute for Occupational Safety and "
    "Health/Pittsburgh Research Lab Pittsburgh, PA USA",
    "Fillmer W. Ruegg and Carl Halpern “Gravimetric Analysis of Exhaust Gas "
    "From Gas Turbine Combustion Chambers” Journal of Research of the "
    "National Bureau of Standards Volume 45,No.2, August 1950",
    "Koratochvil B, Taylor JK. Sampling for chemical analysis. Analytical "
    "Chemistry, 1981, 53:925A.",
    "Oakland JS. Management tools in the manufacture of chemicals: "
    "statistical quality control. Chemistry and Industry, 1981, 16:562–567.",
    "Gy P. Sampling of particulate materials — theory and practice, 2nd "
    "edition. New York, Elsevier, 1979.",
    "Sommer K. Sampling of powders and bulk materials. Heidelberg, "
    "SpringerVerlag, 1986.",
    "Acceptance sampling plans and procedures for the inspection of bulk "
    "materials. Geneva, International Organization for Standardization, 2000. "
    "ISO 10725.",
    "Sampling procedures for inspection by attributes. Procedures for "
    "assessment of stated quality levels. British Standard BS 6001-5:2000. "
    "Geneva, International Organization for Standardization, 1999. ISO 2859-4.",
    "Sampling procedures for inspection by variables. Specification for "
    "single sampling plans indexed by acceptable quality level (AQL) for "
    "lot-by-lot inspection. British Standard BS 6002-1. Geneva, International "
    "Organization for Standardization, 1993. ISO 3951:1989. Sampling "
    "procedures for inspection by attributes.",
    "Sampling schemes indexed by acceptance quality limit for lot-by-lot "
    "inspection. British Standard BS 6001-1. Geneva, International "
    "Organization for Standardization, 1999. ISO 2859-1.",
    "American National Standards Institute/American Society for Quality. "
    "Sampling procedures and tables for inspection by attributes. Washington, "
    "DC, American Society for Quality, 1993. ANSI/ASQCZ1.4-1993.",
    "Methods for sampling chemical products. Introduction and general "
    "principles. British Standard BS 5309-1. London, British Standards "
    "Publishing, 1976.",
    "Methods for sampling chemical products. Sampling of liquids. British "
    "Standard BS 5309-3. London, British Standards Publishing, 1976.",
    "Methods for sampling chemical products. Sampling of solids. British "
    "Standard BS 5309-4. London, British Standards Publishing, 1976.",
    "Ahuja, S. 1984. Overview: Multiple pathways to ultrahigh resolution "
    "chromatography, pp. 1-8. In S. Ahuja, editor. (ed.). Ultrahigh Resolution "
    "Chromatography. ACS Symposium Series 250. American Chemical Society, "
    "Washington, D.C.",
    "Alfheim, I., G. Løfroth, and M. Moller. 1983. Bioassay of extracts of "
    "ambient particulate matter. Environ. Health Perspect. 47:227-238. [PMC "
    "free article] [PubMed]",
    "Alfheim, I., A. Bjorseth, and M. Moller. 1984. Characterization of "
    "microbial mutagens in complex samples--methodology and application. CRC "
    "Crit. Rev. Environ. Control 14:91-150.",
    "Baker, R. A. 1970. Trace organic contaminant concentration by freezing. "
    "IV: Ionic effects. Water Res. 4:559-573.",
    "Barnes, A. J., and W. J. Orville-Thomas. 1980. FT-IR matrix isolation "
    "studies, pp. 157-170. In J. R. Durig, editor. (ed.). Analytical "
    "Applications of FT-IR to Molecular and Biological Systems. D. Reidal, "
    "Dordrecht, Holland. (607 pp.)",
    "Bridbord, K., and J. G. French. 1978. Carcinogenic and mutagenic risks "
    "associated with fossil fuels, pp. 451-463. In E W. Jones and R. I. "
    "Freudenthal, editor. (eds.). Carcinogenesis—A Comprehensive Survey, Vol. "
    "3. Polynuclear Aromatic Hydrocarbons. Raven Press, New York.",
    "Brown, K. W., K. C. Donnelly, J. C. Thomas, P. Davol, and B. R. Scott. "
    "1985. Mutagenicity of three agricultural soils. Sci. Total Environ. "
    "35:799-807.",
    "Brown, S. B. 1980. Introduction to spectroscopy, pp.1-13. In S. B. Brown "
    "(ed.). An Introduction to Spectroscopy for Biochemists. Academic Press, "
    "New York.",
    "Browning, D. R. 1969. Chromatography. McGraw-Hill, New York. (151 pp.)",
    "Brusick, D. J., and R. R. Young. 1982. IERL-RTP Procedures Manual: Level "
    "1 Environmental Assessment, Biological Tests. EPA 600/S8-81-024. Office "
    "of Research and Development, U.S. Environmental Protection Agency, "
    "Washington, D.C. (8 pp.)",
    "Burton, F. G., R. E. Schirmer, D. D. Mahlum, and F. D. Andrew. 1979. "
    "Disposition of process solvent from solvent refined coal in tissues of "
    "the rat after oral dosing. Abstract No. 54. Toxicol. Appl. Pharmacol. "
    "48:A27.",
    "Cantle, J. E. 1982. Atomic Absorption Spectrometry. Elsevier, New York. "
    "(448 pp.)",
    "Carey, A. E., and J. A. Gowen. 1978. PCB’s in Agricultural and Urban "
    "Soil. U.S. Environmental Protection Agency, Washington, D.C. (Available "
    "from NTIS as PB-276 315/9.) (4 pp.)",
    "Case, J. C., and W. G. Fately. 1980. One view of the advantages of "
    "infrared interferometry, pp. 3-10. In J. R. Durig (ed.). Analytical "
    "Applications of FT-IR to Molecular and Biological System. D. Reidel, "
    "Dordrecht, Holland. (607 pp.)",
    "Cerniglia, C. E. 1981. Aromatic hydrocarbons: Metabolism by bacteria, "
    "fungi, and algae, pp. 321-361. In E. Hodgson, J. R. Bend, and R. M. "
    "Philpot, editor. (eds.). Reviews in Biochemical Toxicology. Vol. 3. "
    "Elsevier, New York.",
    "Chan, T. L., E S. Lee, and J.-S. Siak. 1981. Diesel particulate "
    "collection for biological testing: Comparison of electrostatic "
    "precipitation and filtration. Environ. Sci. Technol. 15: 89-93.",
    "Cheng, Y.-S., and H.-C. Yeh. 1979. Particle bounce in cascade impactors. "
    "Environ. Sci. Technol. 13:1392-1396.",
    "Cheng, Y.-S., R. L. Hanson, R. L. Carpenter, C. H. Hobbs. 1984. Use of a "
    "massive volume air sampler to collect fly ash for biological "
    "characterization. J. Air Pollut. Control Assoc. 34:671-674.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> dụng cụ lấy mẫu — sampler · mẫu đại diện — "
                "representative sample · lấy mẫu khí / chất lỏng / chất rắn — gas / "
                "liquid / solid sampling · bẫy pha rắn — solid-phase trapping · chất hấp "
                "phụ — adsorbent · chiết xuất pha rắn (SPE) — solid-phase extraction · "
                "chiết xuất lỏng-lỏng (LLE) — liquid-liquid extraction · ổn định mẫu — "
                "stabilization · làm đông lạnh — cryogenic trapping · máy phân tích khí "
                "thải — flue gas analyzer · sắc ký khí — gas chromatography · khí mang — "
                "carrier gas · cột sắc ký — column · đầu dò — detector · máy phân tích "
                "hồng ngoại — IR gas analyzer · IR không tán sắc — NDIR · độ dẫn nhiệt — "
                "thermal conductivity · katharometer · cầu Wheatstone · thuận từ — "
                "paramagnetic · điện hóa — electrochemical · ORSAT · trọng lượng — "
                "gravimetry · máy đo mêtan — methanometer · zirconia · hệ số không khí — "
                "air value λ · không khí dư — excess air · giản đồ cháy — combustion "
                "diagram · giới hạn cháy — ignition limits · điểm đo — measuring point")
    return ("<b>Key terms.</b> sampler · representative sample · gas / liquid / solid "
            "sampling · solid-phase trapping · adsorbent · solid-phase extraction (SPE) · "
            "liquid-liquid extraction (LLE) · sample stabilization · cryogenic trapping · "
            "flue gas analyzer · gas chromatography · carrier gas · column · detector · "
            "IR gas analyzer · non-dispersive IR (NDIR) · thermal conductivity · "
            "katharometer · Wheatstone bridge · paramagnetic · electrochemical · ORSAT · "
            "gravimetry · methanometer · zirconia · air value λ · excess air · combustion "
            "diagram · ignition limits · measuring point")


def source_notes(lang):
    """Language-aware box for extraction/OCR quirks (never named `note`)."""
    if lang == "vi":
        return note(
            "<b>Ghi chú của người dịch và của quá trình trích xuất.</b> Chương chạy từ trang in "
            "243 đến 288 (PDFPAGE 257–302); chương 8 ở PDFPAGE 303 không được đưa vào. Các dòng "
            "“Ciation:”/“Citation:” trong nguồn là ghi công ảnh, không phải tài liệu tham khảo; "
            "danh mục gồm đúng 44 mục có số, các URL bị gãy dòng được nối lại. Chín trong số mười "
            "một bảng dữ liệu (Table-3 đầu dò GC, Table-2 độ dẫn nhiệt, Table 3, Table 4 và "
            "Table 5–11) được in dạng ảnh nên OCR không giữ lại ô dữ liệu; giá trị được đọc trực "
            "tiếp từ trang in và giữ nguyên định dạng số của nguồn (dấu phẩy thập phân, dấu “…” "
            "cho khoảng, chú thích MW, “als”, “Formel”, “Vinylchloride”, “Dioxines”, “n-C6”, "
            "“C5H11”). Nhiệt độ trong bản dump OCR thành “40C/-100C/200C” nhưng trên trang in "
            "là 4 °C/-10 °C/20 °C; đã dùng giá trị in. Các nét OCR/print được giữ trong bản Anh: "
            "“Ciation”, “nixed”, “shouldbestored”, “Dispersive s IR analyzer”, “excess excess "
            "air value”, “concentration dependant”, “Dilution of with make-up gas”, “e.a.”, "
            "“oulet”, “personell”, “Koratochvil”, “IYONI”, “pct”, “1000C”, “0,03%” và chuỗi "
            "truy vấn bị hỏng của tài liệu 2. “Formel” (bảng 4) và “als” (bảng 5, 8) là từ tiếng "
            "Đức trong nguồn; tiêu đề và nhãn được bản địa hóa, nét gốc được ghi tại đây.")
    return note(
            "<b>Translator and extraction notes.</b> The chapter runs from printed p. 243 to "
            "p. 288 (PDFPAGE 257–302); Chapter 8 at PDFPAGE 303 is excluded. The “Ciation:” / "
            "“Citation:” lines in the source are image credits, not references; the list "
            "contains exactly 44 numbered entries, with line-broken URLs rejoined. Nine of the "
            "eleven data tables (Table-3 GC detectors, Table-2 thermal conductivities, Table 3, "
            "Table 4 and Tables 5–11) were printed as images, so the OCR dump lost every cell "
            "value; the values were read directly from the printed pages and keep the source "
            "number formats (decimal commas, “…” range marks, MW annotations, “als”, “Formel”, "
            "“Vinylchloride”, “Dioxines”, “n-C6”, “C5H11”). Temperatures rendered as "
            "“40C/-100C/200C” in the dump are 4 °C/-10 °C/20 °C on the printed page; the "
            "printed values are used. OCR and print quirks kept in the English text include "
            "“Ciation”, “nixed”, “shouldbestored”, “Dispersive s IR analyzer”, “excess excess "
            "air value”, “concentration dependant”, “Dilution of with make-up gas”, “e.a.”, "
            "“oulet”, “personell”, “Koratochvil”, “IYONI”, “pct”, “1000C”, “0,03%” and the "
            "mangled query string of reference 2. “Formel” (Table 4) and “als” (Tables 5 and "
            "8) are German words in the source; headers and labels are localized and the "
            "original spellings are recorded here.")


# ===========================================================================
def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(v, e):
        b.append(ul(v if vi else e))

    def OL(v, e):
        b.append(ol(v if vi else e))

    def FIG(n, key):
        b.append(fig(n, key))

    def EQ(body, num=""):
        b.append(eq(body, num))

    def TBL(head, rows, cap):
        b.append(table(head, rows, cap))

    # ---------------------------------------------------------------- lead
    b.append(lead(
        "Chương này trình bày kỹ thuật lấy mẫu khí và chất lỏng từ dòng công nghệ, bình chứa và "
        "lò phản ứng; các loại máy phân tích khí thải gồm sắc ký khí, hồng ngoại, độ dẫn nhiệt, "
        "thuận từ, điện hóa, ORSAT và trọng lượng; phép phân tích cháy để tối ưu quá trình; và "
        "các hệ thống lò đốt nhiên liệu rắn, khí, dầu, nhà máy điện than và nhà máy điện khí–hơi."
        if vi else
        "This chapter covers the sampling of gases and liquids from process streams, reactors "
        "and storage vessels; the flue gas analyzer family including gas chromatography, "
        "infrared, thermal conductivity, paramagnetic, electrochemical, ORSAT and gravimetric "
        "methods; combustion analysis for process optimization; and solid-fuel, gas, oil, "
        "coal-fired and combined gas-and-steam firing plants."))
    b.append(source_notes(lang))

    # ---------------------------------------------------------------- 7.1
    H("7.1 Giới thiệu", "7.1 Introduction")
    P("Dụng cụ lấy mẫu khí, mẫu chất lỏng và mẫu chất rắn được dùng để lấy mẫu môi trường từ "
      "dòng công nghệ, lò phản ứng hoặc bình chứa. Quá trình lấy mẫu nhằm thu được mẫu đại diện "
      "cho khí, chất lỏng hoặc chất rắn. Có nhiều loại thiết bị lấy mẫu khác nhau, gồm dụng cụ "
      "lấy mẫu khí, dung môi lỏng và chất rắn. Dụng cụ lấy mẫu khí dùng để xác định chất lượng "
      "của dòng đang chảy và có hai cấu hình: sáu cổng và van ba chiều đơn. Dụng cụ lấy mẫu chất "
      "lỏng dùng để lấy mẫu trong bồn, thùng hoặc vùng nước hở, có các dạng thể tích cố định, "
      "di động và bình xi lanh lỏng. Dụng cụ lấy mẫu chất rắn dùng cho chất rắn đang chảy có thể "
      "bị phân tầng.",
      "Gas samplers, liquid samplers and solids samplers are used to take samples of media from "
      "process streams, reactors or storage vessels. The sampling process is used to obtain "
      "representative samples of gas, liquid or solid. There are many different types of "
      "sampling equipment. Examples include gas samplers, liquid samplers and solids samplers. "
      "A gas sampler is used to determine the quality of a flowing stream and available in two "
      "configurations: six-port and single-valve, three-way. A liquid sampler is used to sample "
      "liquids in tanks, drums, or open waters. Fixed volume, portable and liquid cylinder "
      "samplers are commonly available. A solid sampler is used to sample flowing solids which "
      "may be stratified. Other gas, samplers, liquid samplers and solids samplers are commonly "
      "available.")
    P("Dụng cụ lấy mẫu khí, chất lỏng và chất rắn khác nhau về thông số kỹ thuật và tính năng đặc "
      "biệt. Dụng cụ lấy mẫu khí có độ chính xác cao và cung cấp phương pháp an toàn. Thông số "
      "gồm áp suất (psi), nhiệt độ (°F) và kích cỡ van (in.). Dụng cụ lấy mẫu chất lỏng có điều "
      "khiển nhiệt độ, bộ lọc than và kim có thể thay thế. Một dụng cụ lấy mẫu chất lỏng bằng thép "
      "không gỉ có thể nhúng vào chất lỏng nóng, ăn mòn; van mở bằng tay hoặc tự động để lấy mẫu. "
      "Dụng cụ lấy mẫu chất rắn có ba buồng với kích thước 16,75 in.; 17,875 in. và 18,125 in. "
      "Các thông số quan trọng khác là chiều dài thân (in.), chiều dài lõi (in.) và tổng lượng "
      "mẫu (mL).",
      "Gas samplers, liquid samplers, and solids samplers differ in product specifications and "
      "special features. Gas samplers are highly accurate and provide safe methods for gas "
      "sampling. Specifications include pressure (psi), temperature (°F) and valve size (in.). "
      "Liquid samplers feature temperature control, carbon filters, and replaceable needles. A "
      "liquid sampler that is made of stainless steel can be dipped into a hot, corrosive "
      "liquid. The device’s valves open manually or automatically to obtain a liquid sample. "
      "Solids samplers have three chambers with sizes ranging from 16.75 in. to 17.875 in. to "
      "18.125 in. Other important specifications for a solids sampler are body length (in.), "
      "core length (in.), and total sample quantity (mL).")
    P("Tính năng đặc biệt của từng loại dụng cụ có thể thay đổi theo ứng dụng. Các dụng cụ được "
      "thiết kế và chế tạo để đáp ứng tiêu chuẩn ngành; thiết bị lấy mẫu cần kiểm soát chất lượng "
      "và độ chính xác cao. Một số dụng cụ dùng trong công nghiệp xi măng, nhựa hoặc chế biến "
      "than; số khác dùng trong y tế hoặc dược phẩm. Dụng cụ chuyên dụng còn dùng để tinh chế "
      "sản phẩm, sắc ký và phát hiện sự có mặt của carbon trong nước.",
      "Special features for gas samplers, liquid samplers and solids samplers may vary by "
      "application. Gas samplers, liquid samplers, and solids samplers are designed and "
      "manufactured to meet industry specifications. Sampling equipment needs to provide a high "
      "degree of quality control and accuracy. Some samplers are used in the cement, plastic, or "
      "coal processing industries. Other products are used in medical or pharmaceutical "
      "applications. Specialized gas samplers, liquid samplers and solids samplers are used in "
      "product purification, chromatography, and to detect presence of carbon in water.")

    # ---------------------------------------------------------------- 7.2
    H("7.2 Lấy mẫu khí và chất lỏng", "7.2 Sampling of Gases and Liquids")
    P("Khi lấy mẫu khí và hơi, thể tích của bình chứa hoặc lưu lượng của hệ thống lấy mẫu phải "
      "được biết chính xác, và lưu lượng cần giữ không đổi trong suốt quá trình. Một cách đơn giản "
      "và hiệu quả là dùng bộ hạn lưu ở đầu kim lấy mẫu hoặc dùng ống mao dẫn thủy tinh. Thể tích "
      "bình chứa có thể xác định bằng cách cân bình trước và sau khi lấy mẫu.",
      "The sampling of gases and vapors it is important that the volume of the container or the "
      "flow rate of the sampling system is exactly known. The flow rate should be kept constant "
      "during the sampling procedure. There are a number of possibilities to do this. A simple "
      "and effective way is by using a restrictor at the end of a sampling needle or by using a "
      "glass capillary. The volume of the container can be determined by weighing the container "
      "before and after the sampling.")
    P("<b>Bẫy pha rắn:</b> mẫu khí được dẫn qua ống nhồi chất hấp phụ (ví dụ silica gel, than hoạt "
      "tính) và các chất bị giữ lại được rửa giải bằng dung môi mạnh. Lưu lượng khí là thông số "
      "quyết định hiệu suất bẫy; cần theo dõi sự tạo thành khí dung, quá tải chất hấp phụ và sự "
      "hấp phụ không đảo ngược của các chất phản ứng. Thuốc thử tạo phức có thể cải thiện hiệu "
      "suất bẫy, cũng như kỹ thuật thổi–bẫy (purge and trap).",
      "<b>Solid-phase trapping:</b> Using solid-phase trapping a gaseous sample is passed through "
      "a tube packed with adsorbent (e.g., silica gel, activated carbon) and the trapped "
      "analytes are eluted with a strong solvent. In this approach the gas flow rate is critical "
      "for the trapping efficiency. Important parameters to be watched are aerosol formation, "
      "adsorbent overloading, and irreversible adsorption of reactive analytes. Chemical "
      "complexing reagents may be useful to improve trapping efficiency as well as the purge "
      "and trap technique.")
    P("<b>Bẫy lỏng:</b> mẫu khí được dẫn qua một dung dịch là dung môi tốt cho các chất cần phân "
      "tích và ở lại phía sau; khí thường đi qua dung dịch mà không bị hấp thụ. Lưu lượng phải đủ "
      "thấp để không tạo bọt hoặc khí dung. Có thể thêm tác nhân tạo phức vào dung môi để hỗ trợ "
      "bẫy và hạ nhiệt độ đối với các loài dễ bay hơi.",
      "<b>Liquid trapping:</b> In liquid trapping a gaseous sample is passed through solution, "
      "which is a good solvent for analytes that remain behind. The gas usually passes through "
      "the solution unabsorbed. It is important that the flow rate should be low enough so that "
      "no foams or aerosols are created. Complexing agents may be added to solvent aid trapping "
      "and the temperature can be lowered for very volatile species.")
    P("Mẫu lỏng thường dễ xử lý hơn mẫu khí vì không cần bước hòa tan hoặc chiết xuất; trong nhiều "
      "trường hợp chỉ cần pha loãng bằng dung môi phù hợp. Đối với mẫu lỏng, loại bỏ tạp chất, "
      "cô đặc / pha loãng mẫu và khả năng tương thích với kỹ thuật phân tích cuối cùng là những "
      "đặc điểm quan trọng nhất.",
      "Liquids are frequently easier than gaseous samples because a dissolution or extraction "
      "step is not needed. In many cases dilution with a suitable solvent is sufficient. For "
      "liquid samples the removal of interferences, concentration / dilution of the samples and "
      "compatibility with the final analytical techniques are the most important features.")
    H("7.2.1 Các cách tiếp cận điển hình cho mẫu lỏng", "7.2.1 Typical approaches for liquids", h3)
    U(["<b>Chiết xuất pha rắn (SPE):</b> chất lỏng đi qua pha rắn giữ lại chọn lọc chất phân tích, "
       "sau đó rửa giải bằng dung môi mạnh; cơ chế tương tự sắc ký lỏng. Có nhiều loại chất hấp phụ "
       "và các chế độ pha đảo, pha thường, trao đổi ion, tiếp cận hạn chế (RAM), ái lực miễn dịch "
       "và in phân tử (MIP). SPME và chiết xuất hấp phụ than khuấy (SBSE) là các phát triển mới "
       "không dùng dung môi hữu cơ. SPE có thể xem là cách tiếp cận linh hoạt nhất.",
       "<b>Chiết xuất lỏng–lỏng (LLE):</b> mẫu được phân bổ giữa hai pha không trộn lẫn; chọn dung "
       "môi và điều kiện chiết để chênh lệch độ hòa tan lớn nhất. Cần tránh tạo nhũ; có thể phá nhũ "
       "bằng nhiệt, thêm muối, đổi giá trị KD bằng dung môi hoặc hóa chất khác (đệm chỉnh pH, muối "
       "chỉnh lực ion, tác nhân tạo phức, tác nhân tạo cặp ion). LLE thực hiện bằng phễu chiết cho "
       "ít mẫu hoặc cột nhồi / khay 96 giếng cho nhiều mẫu.",
       "<b>Pha loãng:</b> mẫu được pha loãng bằng dung môi tương thích với dung môi rửa giải của hệ "
       "thống (ví dụ LC) để tránh quá tải cột hoặc đưa tín hiệu vào vùng tuyến tính của đầu dò. "
       "Dung môi không được quá mạnh đối với dung môi rửa giải LC và phải hòa tan được với nó; "
       "“dilute and shoot” là cách điển hình cho mẫu lỏng đơn giản như chế phẩm dược phẩm.",
       "<b>Bay hơi:</b> chất lỏng được loại bỏ bằng gia nhiệt nhẹ ở áp suất khí quyển với không khí "
       "hoặc khí trơ chảy, hoặc dưới chân không. Không bay hơi quá nhanh vì có thể gây sôi bùng và "
       "mất mẫu; mẫu cũng có thể bám thành bình. Nên bay hơi ở nhiệt độ vừa phải với khí trơ (ví dụ "
       "N2), dùng thiết bị bay hơi quay hoặc hệ thống tự động (ví dụ Turbovap).",
       "<b>Chưng cất:</b> mẫu được đun đến nhiệt độ sôi của dung môi, chất phân tích dễ bay hơi cô "
       "đặc trong pha hơi rồi ngưng tụ và thu lại. Cách này chủ yếu dùng cho mẫu dễ bay hơi; nhược "
       "điểm là mẫu có thể phân hủy nếu đun quá cao. Chưng cất chân không dùng cho hợp chất áp suất "
       "hơi thấp, còn chưng cất hơi nước nhẹ nhàng hơn vì nhiệt độ tối đa 100 °C.",
       "<b>Vi lọc (microdialysis):</b> màng bán thấm được đặt giữa hai pha lỏng nước và phân tử "
       "khối lượng thấp chuyển từ pha này sang pha kia theo chênh lệch nồng độ. Cần kỹ thuật làm giàu "
       "như SPE để cô đặc dịch lọc; dùng để khảo sát hóa chất ngoại bào trong mô thực vật, động "
       "vật sống và dịch lên men, có thể ghép trực tiếp với LC.",
       "<b>Đông khô (lyophilization):</b> mẫu nước được đông lạnh rồi loại nước bằng thăng hoa dưới "
       "chân không. Kỹ thuật này dùng cho chất hữu cơ không bay hơi, cô đặc chất vô cơ và xử lý thể "
       "tích mẫu lớn; rủi ro là mất chất phân tích dễ bay hơi."],
      ["<b>Solid-phase extraction (SPE):</b> a liquid is passed through a solid phase, which "
       "selectively retains the analyte. Thereafter, the analyte can be eluted with a strong "
       "solvent. In some cases interferences are retained and analytes allowed passing through "
       "solid phase unretained. The mechanism of SPE is comparable with LC. The advantages of "
       "SPE are that a wide variety of sorbents is available for the selective removal of "
       "inorganic, organic, and biological analytes. The good selectivity and efficiency of SPE "
       "can be explained by the fact that various modes like reversed-phase (RP), normal-phase "
       "(NP), ion-exchange (IE), restricted-access (RAM), Immunoaffinity (IA) and "
       "molecular-imprinting (MIP) can be applied. Techniques like SPME and stir bar sorption "
       "extraction (SBSE) are relatively new developments approaches to perform extraction "
       "procedures without the need for using organic solvents. Furthermore, a number of "
       "different sampling formats allowing off-line, at-line, on-line and in-line sampling "
       "procedures. This means that SPE can be considered to be the most versatile sampling and "
       "sample manipulation approach.",
       "<b>Liquid-liquid Extraction:</b> Still the most popular technique is LLE. In this case "
       "the sample is partitioned between two immiscible phases. The extraction solvent and "
       "extraction conditions are chosen in such a way that a maximum difference in solubility "
       "is obtained. In order to obtain reliable results one should beware of the formation of "
       "emulsions. Possibilities to break them are heat, addition of salt; change of the KD value "
       "by using different solvents or chemicals affecting the equilibrium (such as buffers for "
       "pH adjustment, salts for ionic strength, complexing agents, ion-pairing agents, etc.). "
       "LLE can be performed manually by using a separatory funnel in case a relatively small "
       "number of samples must be analyzed or in an automated way by using packed cartridges or "
       "96-well plates in case larger number of samples must be analyzed.",
       "<b>Dilution:</b> An additional technique is dilution in which the sample is diluted with "
       "a solvent compatible with the eluent of the separation system (e.g. LC) to avoid system "
       "overloading or to be in linear range of detector. For example, to avoid band broadening "
       "the solvent should not be too strong for the LC eluent and should be miscible with LC "
       "eluent; “dilute and shoot” is a typical ST method for simple liquid samples such as "
       "pharmaceutical formulations.",
       "<b>Evaporation:</b> In evaporation the liquid is removed by gentle heating at atmospheric "
       "pressure with flowing air or inert gas or under vacuum. Evaporation should not be "
       "performed too quickly and bumping can result in sample losses. Sample losses can also "
       "occur on the wall of the container. Evaporation should be done at moderate temperatures, "
       "by using an inert gas (e.g. N2) by using a rotary evaporator or an automated system (e.g. "
       "Turbovap).",
       "<b>Distillation:</b> In distillation a sample is heated to the boiling point of the "
       "solvent, and volatile analytes are concentrated in the vapor phase, condensed, and "
       "collected. This approach is mainly used for samples that can easily be volatilized. "
       "Problems are that a sample can decompose if heated too high. This means that vacuum "
       "distillation can be used for low-vapor-pressure compounds, while steam distillation is "
       "rather gentle since maximum temperature is 100 °C.",
       "<b>Microdialysis:</b> Microdialysis is a technique in which a semipermeable membrane is "
       "placed between two aqueous liquid phases and low-molecular weight molecules transfer "
       "from one liquid to the other based on a concentration difference over the membrane. "
       "Enrichment techniques such as SPE are required to concentrate the dialysate. "
       "Microdialysis is used, for example, for the examination of extracellular chemicals in "
       "living plant and animal tissue and in fermentation broths. It has been used on-line with "
       "LC. Dialysis with MWCO membranes can also be used for on-line deproteination of samples.",
       "<b>Lyophilization (freeze-drying):</b> In lyophilization (freeze-drying) an aqueous "
       "sample is frozen and water removed by sublimation under vacuum. This technique can be "
       "used for nonvolatile organics, the concentration of inorganics and large sample volume "
       "can be handled. A potential problem can be the loss of volatile analytes."])

    H("7.2.2 Lấy mẫu nước", "7.2.2 Water Sampling", h3)
    P("Khi lấy mẫu nước, bình chứa phải được xử lý trước: về nguyên tắc chỉ dùng bình polyethylene "
      "hoặc PTFE, rửa và bảo quản trong HNO3 10% trong 2 ngày rồi tráng bằng nước cất hai lần, khử "
      "ion. Sau khi lấy, axit hóa mẫu (thường với 2 mL HNO3 10% hoặc HCl 5 M) sẽ làm giảm hoặc loại "
      "bỏ sự hấp thụ vết và sự thủy phân của nguyên tố vi lượng.",
      "In the case of water sampling it is important that collection containers are pretreated "
      "before the sample can be collected. In principle, only polyethylene or PTFE containers "
      "should be used and they should be washed and stored in 10% of HNO3 for 2 days and rinsed "
      "with double distilled deionised water. Following collection, acidification of the sample "
      "(normally with 2 mL of 10% HNO3 or 5 M HCl) will reduce or eliminate trace element "
      "adsorption and hydrolysis.")
    P("Tùy loại nước mà cần thận trọng riêng. Với nước máy, phải bỏ dòng nước chảy ra đầu tiên vì "
      "nồng độ nguyên tố vi lượng từ ống, mối hàn và mối nối rất cao. Thường cho nước chảy 5–30 phút "
      "trước khi lấy mẫu thật. Hầu hết mẫu nước cần lọc ngay sau khi lấy để loại vi khuẩn, tảo và "
      "hạt lơ lửng; thường dùng màng lọc 0,5 mm. Chất ổn định như axit nitric, hydrochloric và "
      "sulfuric thường được thêm để hạ pH xuống khoảng 1–3,5.",
      "Depending on the type of water precautions must be taken. For the collection of tap "
      "water, the first water running from the tap must be avoided because there will be a high "
      "concentration of trace elements from the pipes, soldering and welds. Normally, sampling "
      "is performed by running the tap for 5 – 30 min, before the actual sample is taken. Most "
      "water samples require filtration immediately after collection to remove bacteria, algae "
      "and particulate matter. In most cases 0.5 mm membrane filters are used. Stabilizing agents "
      "like nitric, hydrochloric and sulphuric acids are frequently added to lower the pH to "
      "about 1 – 3.5.")
    P("Trước khi bảo quản, bình mẫu phải đầy hoàn toàn vì không khí có thể làm biến đổi mẫu về mặt "
      "hóa học hoặc sinh học. Mẫu nước nên bảo quản trong bóng tối, bằng làm lạnh (4 °C) hoặc đông "
      "sâu (-20 °C). Với nước mặt, không được lấy mẫu từ nguồn nước đứng vì chất ô nhiễm từ van, "
      "đầu nối, ống và chất bôi trơn có thể hòa tan vào nước; hệ thống luôn phải xả một thời gian "
      "trước khi lấy mẫu. Vật liệu bình không quá quan trọng nhưng phải đậy kín bằng nắp nhôm hoặc "
      "PTFE để tránh ô nhiễm từ nắp. Lấy mẫu ở nhiệt độ môi trường; với hệ thống áp lực, lưu lượng "
      "lấy mẫu phải từ 500 mL/min trở lên.",
      "Before storage all sample containers should be completely full, because the presence of "
      "air may chemically or biologically alter the sample. Water samples shouldbestored in the "
      "dark, either by refrigeration (4 °C) or by deep-freezing (-20 °C). The most important "
      "problem during the sampling of surface water is that, in principle, no samples may be "
      "taken from a stagnant water source because in those cases contaminants from valves, "
      "connectors, pipes, lubricants, etc. can be dissolved in the water. The system must "
      "therefore always be flushed for a while before taking the sample. The material of the "
      "container, used for storage, normally is not critical. However, the container must be "
      "carefully closed using aluminum or PTFE cap to avoid that pollutants fro the cap will "
      "pollute the sample. It is important that the sampling is performed at the same temperature "
      "as the surroundings. Using pressurized systems the sample must be done at flow rates of "
      "500 mL/min or higher.")
    P("Về nguyên tắc có ba cách lấy mẫu: lẫy tức thời (grab), mẫu tổ hợp (composite) và liên tục. "
      "Dù dùng cách nào, mẫu đại diện vẫn rất quan trọng; các thông số quyết định là tần suất lấy "
      "mẫu, thời điểm lấy và bảo quản mẫu không bị phân hủy hoặc nhiễm bẩn cho đến khi phân tích.",
      "In principle, there are three ways of sampling: grab, composite and continuous. Also in "
      "this case it is of great importance that a representative sample is taken. The most "
      "critical parameters, in this respect are; the sampling frequency, the time point of "
      "sampling and the storage of the sample (without degradation or contamination) until the "
      "actual analysis.")
    U(["<b>Phương pháp tổ hợp</b> trộn các mẫu cá nhân lấy ở những thời điểm khác nhau rồi phân tích. "
       "Kết quả là giá trị trung bình, có thể kém tin cậy với hợp chất không bền. Mẫu nước mặt "
       "thường thu trong 24 giờ, còn mẫu công nghiệp nên lấy ít nhất một chu trình công nghệ đầy đủ.",
       "<b>Lấy mẫu từ hệ thống đang chảy</b> đòi hỏi thể tích mẫu hoàn toàn bằng nhau tại các thời "
       "điểm khác nhau. Nồng độ chất phân tích và lưu lượng hệ thống cũng không được dao động quá "
       "lớn theo thời gian. Thời gian lấy mẫu tối thiểu phụ thuộc vào tốc độ lấy mẫu, nồng độ chất "
       "phân tích và độ nhạy của hệ thống phân tích."],
      ["<b>The composite methods</b> mean that individual samples, taken at different time "
       "points, are nixed and analyzed. The result of measuring a composite sample is a mean "
       "value which can provide less reliable data for non-stabile compounds. Surface water "
       "samples are often collected over a period of 24 h, while the sampling of industrial "
       "processes should be conducted over at least a full process cycle.",
       "<b>Sampling from flowing systems</b> means that it is important that on different time "
       "points samples of the exactly the same volume are taken. In addition it is important "
       "that the concentration of the analytes and flow of the system are fluctuating too much "
       "in time. The minimum time for the sampling procedure depends on: the speed of the "
       "sampling; the concentration of the analytes; the sensitivity of the analytical system."])
    P("Mẫu khí và chất lỏng có thể được bẫy trên chất hấp phụ; quá trình này thường hiệu quả hơn "
      "với khí. Với mẫu nước, một thể tích nhất định (thường 500–1500 mL) được cho chảy qua chất "
      "hấp phụ (ví dụ XAD) nhồi trong cột hoặc hộp nhỏ. Sau khi lấy, chất bị hấp phụ có thể xác "
      "định trực tiếp hoặc gián tiếp. Bảng 1 liệt kê một số chất hấp phụ dùng cho mẫu nước.",
      "Gaseous and liquid samples can be trapped on an adsorbent. This process is normally more "
      "efficient for gases compared with liquids. In the case of water samples a certain volume "
      "of water (usually 500 – 1500 mL) is flushed over the adsorbent (e.g. XAD), which can be "
      "packed in a small cartridge or column. After sampling the adsorbed analyte(s) can be "
      "determined directly or indirectly. In Table 1 an overview is given of some of the "
      "adsorbents that can be used for the sampling of aqueous samples.")
    TBL([C.T("Chất hấp phụ", "Sorbent", lang), C.T("Hợp chất", "Compounds", lang),
         C.T("Ghi chú", "Comments", lang)],
        [
            C.T("Carbon", "Carbon", lang),
            ("Ambersorb XE-340", "CHCl₃, C₅H₁₁, CH₃OH", "Thermal desorption"),
            ("Spherocarb", "Organic compounds", "Desorption with organic solvents"),
            ("Molecular sieves 13X", "N₂O", "Thermal desorption"),
            C.T("Polyme xốp", "Porous polymers", lang),
            ("Chromosorb 106", "CHCl₃, C₅H₁₁, CH₃OH", "Thermal desorption"),
            ("Macroporous polymer", "Aromatic hydrocarbons", "Thermal desorption, ppb level"),
            ("Porapak Q, Chromosorb 101", "Vinylchloride", ""),
            ("Styrene-divinylbenzene copolymer", "Pesticides", ""),
            ("Porous polyurethane foam", "pesticides", ""),
            ("Tenax GC", "", ""),
            ("", "CHCl₃, C₅H₁₁, CH₃OH", "Thermal desorption, ppb level"),
            ("", "Petroleum, n-C₆, acetone", "Recoveries 90-100%, diphenylamine"),
            ("", "Haloform", "Thermal desorption ppb level"),
            ("", "Volatile organic components", ""),
            C.T("Nhựa XAD", "XAD resins", lang),
            ("XAD-2", "Haloform, Dioxines", ""),
            ("XAD-4", "Organic pollutants", "Desorption with organic solvents"),
        ],
        C.T("Bảng 1: Chất hấp phụ dùng để lấy mẫu nước",
           "Table 1: Sorbents for the sampling of aqueous samples", lang))
    P("Mẫu vòi nước đại diện có thể lấy bằng cách xả vòi 10 phút với lưu lượng 500 mL/min để loại "
      "không khí và hạt rắn trong đường ống. Trong lúc xả, nhiệt độ nước cũng ổn định. Để bảo đảm "
      "chất lượng mẫu, nên đo độ dẫn và pH và lấy lượng mẫu đủ lớn để có thể phân tích lặp lại hai "
      "hoặc ba lần nếu cần.",
      "The sampling of a representative tap water sample can be performed by flushing the tap, "
      "first, during 10 min with a flow of 500 mL/min, to remove all the air and solid particles "
      "present in the piping system. A positive feature is that during this flushing the "
      "temperature of the water will be stabilized. In order to guarantee the quality of the "
      "sample the conductivity and the pH should be measured and a sufficiently large sample "
      "should be taken allowing, if necessary, a duplicate or triplicate analysis.")
    P("Nhìn chung bình mẫu phải đầy để tránh bay hơi các chất dễ bay hơi; tuy nhiên trong vận chuyển "
      "có thể chỉ đổ đầy 90% để phù hợp với nhiệt độ. Nhóm phương pháp quan trọng cho lấy mẫu khí "
      "và hơi là kỹ thuật đông lạnh (cryogenic). Lấy mẫu và cô đặc bằng kỹ thuật này giúp mẫu sẵn "
      "sàng cho bước tiếp theo; nhược điểm là khi có nhiều nước có thể mất mẫu do tạo khí dung. "
      "Bảng 2 liệt kê các thuốc thử dùng để đông lạnh nhanh mẫu; nitơ lỏng có thể thay thế không khí "
      "khí quyển.",
      "Normally the sample containers should be completely filled to avoid the volatilization of "
      "volatile compounds. However, during transport it may be necessary to fill a sample "
      "container for only 90% to allow temperatures. An important group of methods for the "
      "sampling of gases and vapors are the cryogenic techniques. Sampling and concentration of "
      "samples using these techniques results in a direct availability of the sample for the next "
      "step in the analytical procedure. A disadvantage can be that in case large volumes of "
      "water are present, sample losses can occur because of aerosol formation. In Table 2 gives "
      "an overview of a number of reagents that can be used for the fast freezing of samples. "
      "Liquid nitrogen can be used to replace atmospheric air.")
    TBL([C.T("Chất phân tích", "Analyte", lang),
         C.T("Ổn định", "Stabilization", lang), C.T("Bảo quản", "Storage", lang)],
        [
            ("Neutral compounds", "pH > 2, thiosulfate", "4 °C, max. 7 days before analysis"),
            ("Carbamates", "pH = 3 (monochloro acetic acid), thiosulfate",
             "-10 °C, max. 28 days before analysis"),
            ("Chlorinated acids", "Thiosulfate", "4 °C, max. 14 days before extraction"),
            ("Chlorinated dioxins and furans", "",
             "20 °C, max. 90 days before extraction"),
            ("Diquat and paraquat", "pH = 2, thiosulfate",
             "4 °C, max. 7 days before extraction, after that 30 days"),
            ("Endothal", "", "4 °C, max. 7 days before analysis"),
            ("Glyphosate", "Thiosulfate", "4 °C, max. 14 days at -10 °C max. 18 months"),
            ("Halo acetic acids", "Ammonium chloride", "4 °C, max. 28 days before extraction"),
            ("Neutral chlorinated compounds", "Chloroform", "4 °C, max. 6 weeks before extraction"),
            ("Organochlor pesticides", "Thiosulfate", "4 °C, max. 7 days before extraction"),
            ("Organophosphor pesticides", "Thiosulfate", "4 °C, max. 14 days before extraction"),
            ("Phenols", "Chloroform / Sulfuric acid", "3 weeks"),
            ("Phenoxyacid herbicides", "pH = 2 (sulfuric acid)", "4 °C, max. 50 days"),
            ("Phenylurea herbicides", "pH 5 – 9", "4 °C, max. 7 days before extraction"),
            ("Phthalates and adipate esters", "Thiosulfate", "4 °C, max. 14 days before extraction"),
            ("PCB’s", "", "4 °C, max. 14 days before extraction"),
            ("PAH’s", "pH < 2, thiosulfate", "4 °C, max. 7 days before extraction"),
            ("Triazines", "pH 5 – 9", "4 °C, max. 7 days before extraction"),
            ("Volatile organic compounds", "Thiosulfate", "4 °C, max. 14 days before extraction"),
        ],
        C.T("Bảng 2: Ổn định các hợp chất hữu cơ",
           "Table 2: Stabilization of organic compounds", lang))
    P("Với huyền phù có thể dùng lọc, ly tâm và lắng: <b>lọc</b> cho chất lỏng qua vật liệu lọc "
      "phù hợp để loại hạt lơ lửng, tránh hấp thụ / hấp phụ không mong muốn; nên lọc dung môi rửa "
      "giải trước khi tách sắc ký hoặc điện di để tránh áp suất ngược và bảo vệ cột. Vật liệu lọc "
      "phải tương thích dung môi; lọc xốp lớn (> 2 mm) cho lưu lượng lớn, lọc xốp nhỏ (< 0,2 mm) "
      "để loại vi khuẩn. <b>Ly tâm</b> đặt mẫu vào thích hợp và quay nhanh rồi gạt phần nước nổi; "
      "đôi khi khó lấy hết chất rắn ra khỏi ống. <b>Lắng</b> để mẫu đứng yên trong bể lắng; tốc độ "
      "lắng phụ thuộc bán kính Stokes, rất chậm và chủ yếu do kích thước hạt quyết định.",
      "The techniques that can be used for suspensions include: filtration, centrifugation and "
      "sedimentation: In filtration a liquid is passed through filter, made of a suitable "
      "material to avoid unwanted absorption / adsorption effects, to remove suspended "
      "particulates. It is highly recommended to prevent backpressure problems and to preserve "
      "the lifetime of separation columns to filter eluents before a chromatographic or "
      "electrophoretic separation. Filter materials must be compatible with the used solvents "
      "and may not dissolve during the experiments. Large porosity (> 2 mm) filters should be "
      "used for maximum flow or small-porosity filters (< 0.2 mm) to remove bacteria. During "
      "centrifugation a sample is placed in suitable container (e.g. tapered centrifuge tube) "
      "and spun at high velocity in an appropriate centrifuge. Subsequently the supernatant "
      "liquid is decanted. The quantitative removal of solid sample from a tube sometimes "
      "presents a practical problem. In sedimentation the sample is allowed to settle when left "
      "undisturbed in a sedimentation tank. The settling rate depends on the Stokes’ radius. It "
      "is an extremely slow process and in particularly the particle size is determining the "
      "settling rate.")

    # ---------------------------------------------------------------- 7.3
    H("7.3 Máy phân tích khí thải", "7.3 Flue Gas Analyzer")
    P("Máy phân tích khí thải là thiết bị giám sát khí thải nhằm mục đích phát thải và hiệu suất. "
      "Đây có thể là thiết bị cầm tay giá rẻ hoặc cụm lớn lắp cố định với ống khói. Thường máy có "
      "bộ nhớ trong lưu các chỉ số khí cho đến khi tải vào máy tính để phân tích thêm. Một số mẫu "
      "lớn nối trực tiếp với máy in để công ty có bản sao dữ liệu.",
      "A flue gas analyzer is an instrument that monitors flue gases for emissions and efficiency "
      "purposes. A flue gas analyzer may be an inexpensive hand-held instrument or a large unit "
      "that is permanently installed with a flue. Typically, an analyzer has an internal memory "
      "system that stores gas readings until the values are loaded into a computer for further "
      "analysis. Some large models are attached directly to printers, so companies can have hard "
      "copies of their data as well.")
    P("Nhìn chung máy được dùng khi đưa đầu dò vào ống khói của lò hơi, lò nung hoặc nguồn cháy "
      "khác. Tùy loại khí cần giám sát hoặc đo mà dùng các máy khác nhau: máy dùng đồng hồ hồng "
      "ngoại, máy đo dữ liệu điện hóa của khí.",
      "Generally, a flue gas analyzer is used when a probe is inserted into the flue of a boiler, "
      "furnace, or other sources of combustion. There are several different analyzers that may be "
      "used, depending on the kind of gas being monitored or measured. For example, some analyzers "
      "use infrared meters, while others measure the electrochemical data of a gas.")
    P("Dù mẫu đầu dò là phổ biến nhất, máy không nhất thiết phải dùng đầu dò: máy có thể bơm khí "
      "từ ống khói qua ống nối tới thiết bị. Cách này thường dùng khi công ty muốn giám sát liên "
      "tục ống khói lớn hoặc không thể đưa đầu dò vào. Đôi khi cần thêm công đoạn để đo chính xác: "
      "khí như hydrochloric hoặc sulphur dioxide cần gia nhiệt ống nối để tránh ngưng tụ trước khi "
      "đo; ngược lại có khí cần làm lạnh bằng bộ làm mát Peltier, làm lạnh bề mặt ống dẫn để loại "
      "hơi ẩm trước khi đo.",
      "Although the probe model is most common, a flue gas analyzer does not necessarily need to "
      "use a probe to monitor the gas in the flue. For example, an analyzer may pump the gas from "
      "the flue through a tube that is connected to the instrument. This is most common when a "
      "company wants to continuously monitor a large flue or if a probe cannot be inserted. "
      "Sometimes, it takes a bit more effort to measure a gas accurately using a flue gas "
      "analyzer. For example, some gases, such as hydrogen chloride or sulfur dioxide, require "
      "that the tube connected to the analyzer be heated. Heating the tube prevents some gases "
      "from condensing into a liquid before they can be measured. In the alternative, some gases "
      "need to be cooled using an instrument called a Peltier cooler. The Peltier cooler cools a "
      "surface, such as the tube transferring the gas to the analyzer, so that any moisture in "
      "the gas will be removed before it is measured.")
    P("Sau khi đo, giá trị thường được biểu thị bằng phần triệu (ppm) hoặc phần trăm. Với số lớn "
      "như khi đo carbon dioxide hay oxygen, dùng phần trăm; với số nhỏ như carbon monoxide, dùng "
      "ppm. Phân tích khí thải phổ biến ở ngành có quy định pháp lý bắt buộc giám sát phát thải, "
      "cũng như nơi doanh nghiệp muốn bảo đảm hiệu quả và trách nhiệm môi trường. Qua dữ liệu, "
      "công ty thấy mình có thải khí độc hại, gây ô nhiễm hay không.",
      "In most cases, after a gas is measured by a flue gas analyzer, a value of measurement is "
      "designated: the value may be in parts per million (ppm) or as a percentage. Typically, if "
      "the numbers are large, such as found when a flue gas analyzer is measuring carbon dioxide "
      "or oxygen, a percentage value will be assigned to it. If the numbers are small, such as "
      "found with the analysis of carbon monoxide, the value will be given in ppm. Flue gas "
      "analysis using a flue gas analyzer is most commonly used in industries where there are "
      "legal mandates directing companies to monitor their emissions. It may also be used in "
      "areas where an industry wants to ensure they are being both efficient and environmentally "
      "conscious. By looking at data, a company can see whether they are emitting harmful gases "
      "into the air, creating pollution, or a variety of other environmental concerns.")

    H("7.3.1 Các loại máy phân tích khí", "7.3.1 Types of Gas Analyzer", h3)
    P("Có nhiều loại máy phân tích khí với nguyên lý làm việc khác nhau. Nhờ nguyên lý hoạt động "
      "khác nhau mà chúng có khả năng xác định các loài khí khác nhau.",
      "There are various types of gas analyzer with their different working principle. Also due "
      "to their different principle of operation they are capable of estimating different species "
      "of gas.")

    H("7.3.2 Sắc ký khí", "7.3.2 Gas Chromatograph", h3)
    P("Sắc ký khí đưa mẫu vào đầu cột sắc ký. Mẫu được dẫn qua cột nhờ dòng pha động là khí trơ. "
      "Bản thân cột chứa pha tĩnh lỏng được hấp phụ trên bề mặt chất rắn trơ.",
      "Gas chromatography involves a sample injected onto the head of the chromatographic column. "
      "The sample is transported through the column by the flow of inert, gaseous mobile phase. "
      "The column itself contains a liquid stationary phase which is adsorbed onto the surface "
      "of an inert solid.")
    FIG(1, F.fig_f01())
    H("7.3.2.1 Cấu phần dụng cụ", "7.3.2.1 Instrumental Components", h4)
    U(["<b>Khí mang:</b> phải trơ về mặt hóa học; thường dùng nitơ, heli, argon và carbon dioxide. "
       "Lựa chọn khí mang thường phụ thuộc đầu dò. Hệ thống khí mang còn có rây phân tử để loại "
       "nước và tạp chất.",
       "<b>Cổng tiêm mẫu:</b> để đạt hiệu suất cột tối ưu, mẫu không được quá lớn và phải đưa vào "
       "cột như một “nút” hơi; tiêm chậm mẫu lớn gây rộng băng và mất độ phân giải. Cách phổ biến "
       "là dùng microkim tiêm mẫu qua màng cao su vào cổng bay hơi nhanh ở đầu cột.",
       "<b>Cột:</b> có hai loại chính là cột nhồi và cột mao quản (ống hở). Cột nhồi chứa vật liệu "
       "nâng rắn trơ tán mịn (thường từ điatomit) phủ pha tĩnh lỏng, dài 1,5–10 m và đường kính "
       "trong 2–4 mm. Cột mao quản đường kính trong vài phần mười milimet, gồm loại phủ thành "
       "(WCOT) hoặc phủ giá đỡ (SCOT).",
       "<b>Nhiệt độ cột:</b> để làm việc chính xác phải kiểm soát nhiệt độ trong vài phần mười độ. "
       "Nhiệt độ tối ưu phụ thuộc điểm sôi của mẫu; theo kinh nghiệm, nhiệt độ cao hơn một chút "
       "điểm sôi trung bình cho thời gian rửa giải 2–30 phút. Nhiệt độ thấp cho độ phân giải tốt "
       "nhưng kéo dài thời gian; với mẫu có dải sôi rộng có thể lập trình nhiệt độ."],
      ["<b>Carrier gas:</b> The carrier gas must be chemically inert. Commonly used gases include "
       "nitrogen, helium, argon, and carbon dioxide. The choice of carrier gas is often dependent "
       "upon the type of detector which is used. The carrier gas system also contains a molecular "
       "sieve to remove water and other impurities.",
       "<b>Sample injection port:</b> For optimum column efficiency, the sample should not be too "
       "large, and should be introduced onto the column as a “plug” of vapor - slow injection of "
       "large samples causes band broadening and loss of resolution. The most common injection "
       "method is where a microsyringe is used to inject sample through a rubber septum into a "
       "flash vapouriser port at the head of the column.",
       "<b>Columns:</b> There are two general types of column, packed and capillary (also known "
       "as open tubular). Packed columns contain a finely divided, inert, solid support material "
       "(commonly based on diatomaceous earth) coated with liquid stationary phase. Most packed "
       "columns are 1.5 - 10m in length and have an internal diameter of 2 - 4mm.Capillary columns "
       "have an internal diameter of a few tenths of a millimeter. They can be one of two types; "
       "wall-coated open tubular (WCOT) or support-coated open tubular (SCOT). Wall-coated columns "
       "consist of a capillary tube whose walls are coated with liquid stationary phase. In "
       "support-coated columns, the inner wall of the capillary is lined with a thin layer of "
       "support material such as diatomaceous earth, onto which the stationary phase has been "
       "adsorbed.",
       "<b>Column temperature:</b> For precise work, column temperature must be controlled to "
       "within tenths of a degree. The optimum column temperature is dependant upon the boiling "
       "point of the sample. As a rule of thumb, a temperature slightly above the average boiling "
       "point of the sample results in an elution time of 2 - 30 minutes. Minimal temperatures "
       "give good resolution, but increase elution times. If a sample has a wide boiling range, "
       "then temperature programming can be useful. The column temperature is increased (either "
       "continuously or in steps) as separation proceeds."])
    P("Có nhiều đầu dò dùng trong sắc ký khí, mỗi loại có độ chọn lọc riêng. Đầu dò không chọn lọc "
      "đáp ứng mọi hợp chất trừ khí mang; đầu dò chọn lọc đáp ứng nhóm hợp chất có tính chất vật lý "
      "hoặc hóa học chung; đầu dò đặc hiệu đáp ứng một hợp chất hóa học duy nhất. Đầu dò cũng chia "
      "thành loại phụ thuộc nồng độ và loại phụ thuộc lưu lượng khối. Tín hiệu đầu dò phụ thuộc nồng "
      "độ thường không phá hủy mẫu và giảm khi pha loãng bằng khí bổ sung; đầu dò phụ thuộc lưu "
      "lượng khối thường phá hủy mẫu, tín hiệu tỷ lệ với tốc độ chất đi vào và không bị ảnh hưởng "
      "bởi khí bổ sung.",
      "Detectors: There are many detectors which can be used in gas chromatography. Different "
      "detectors will give different types of selectivity. A non-selective detector responds to "
      "all compounds except the carrier gas, a selective detector responds to a range of "
      "compounds with a common physical or chemical property and a specific detector responds to "
      "a single chemical compound. Detectors can also be grouped into concentration dependant "
      "detectors and mass flow dependant detectors. The signal from a concentration dependant "
      "detector is related to the concentration of solute in the detector, and does not usually "
      "destroy the sample Dilution of with make-up gas will lower the detectors response. Mass "
      "flow dependant detectors usually destroy the sample, and the signal is related to the rate "
      "at which solute molecules enter the detector. The response of a mass flow dependant "
      "detector is unaffected by make-up gas. Have a look at this tabular summary of common GC "
      "detectors:")
    TBL([C.T("Đầu dò", "Detector", lang), C.T("Kiểu", "Type", lang),
         C.T("Khí hỗ trợ", "Support gases", lang), C.T("Độ chọn lọc", "Selectivity", lang),
         C.T("Giới hạn phát hiện", "Detectability", lang),
         C.T("Dải động", "Dynamic range", lang)],
        [
            ("Flame ionization (FID)", "Mass flow", "Hydrogen and air", "Most organic cpds.",
             "100 pg", "10⁷"),
            ("Thermal conductivity (TCD)", "Concentration", "Reference", "Universal",
             "1 ng", "10⁷"),
            ("Electron capture (ECD)", "Concentration", "Make-up",
             "Halides, nitrates, nitrites, peroxides, anhydrides, organometallics", "50 fg", "10⁵"),
            ("Nitrogen-phosphorus", "Mass flow", "Hydrogen and air", "Nitrogen, phosphorus",
             "10 pg", "10⁶"),
            ("Flame photometric (FPD)", "Mass flow", "Hydrogen and air possibly oxygen",
             "Sulphur, phosphorus, tin, boron, arsenic, germanium, selenium, chromium",
             "100 pg", "10³"),
            ("Photo-ionization (PID)", "Concentration", "Make-up",
             "Aliphatics, aromatics, ketones, esters, aldehydes, amines, heterocyclics, "
             "organosulphurs, some organometallics", "2 pg", "10⁷"),
            ("Hall electrolytic conductivity", "Mass flow", "Hydrogen, oxygen",
             "Halide, nitrogen, nitrosamine, sulphur", "", ""),
        ],
        C.T("Bảng-3: Các đầu dò GC thông dụng", "Table-3: Common GC detectors", lang))

    H("7.3.3 Máy phân tích khí hồng ngoại", "7.3.3 IR Gas Analyzer", h3)
    P("Máy phân tích khí hồng ngoại đo các khí vết bằng cách xác định độ hấp thụ của nguồn sáng "
      "hồng ngoại phát ra qua một mẫu không khí nhất định. Các khí vết trong khí quyển Trái Đất bị "
      "kích thích ở bước sóng riêng trong dải hồng ngoại. Về nguyên lý, kiểm tra mức độ ánh sáng "
      "bị không khí hấp thụ: phân tử khác nhau hấp thụ tần số khác nhau; không khí chứa nhiều một "
      "loại khí sẽ hấp thụ nhiều tần số tương ứng, cho phép cảm biến báo nồng độ cao của phân tử đó.",
      "An infrared gas analyzer measures trace gases by determining the absorption of an emitted "
      "infrared light source through a certain air sample. Trace gases found in the Earth’s "
      "atmosphere get excited under specific wavelengths found in the infrared range. The concept "
      "behind the technology can be understood as testing how much of the light is absorbed by "
      "the air. Different molecules in the air absorb different frequencies of light. Air with "
      "lots of a certain gas will absorb more of a certain frequency, allowing the sensor to "
      "report a high concentration of the corresponding molecule.")
    P("Máy phân tích khí IR gồm hai loại: <b>IR không tán sắc</b> và <b>IR tán sắc</b> (nguồn ghi "
      "“Dispersive s IR analyzer”).",
      "IR Gas analyzer can be of two types: <b>Non-Dispersive IR-Analyzer</b> and <b>Dispersive s "
      "IR analyzer</b>.")
    H("7.3.3.1 Nguyên lý", "7.3.3.1 Principle", h4)
    P("Cấu phần chính gồm nguồn hồng ngoại (đèn), buồng mẫu hoặc ống dẫn sáng, buồng mẫu bước sóng; "
      "nồng độ khí được đo bằng quang-điện theo độ hấp thụ một bước sóng riêng trong dải IR. Ánh "
      "sáng IR đi qua buồng mẫu tới đầu dò; song song có buồng khác chứa khí tham chiếu thường là "
      "nitơ. Trước đầu dò có bộ lọc quang chỉ cho qua bước sóng mà phân tử khí chọn lọc hấp thụ. "
      "Lý tưởng nhất, phân tử khí khác không hấp thụ ở bước sóng này; thực tế CO2 và H2O thường gây "
      "nhạy chéo, nên khó phân tích nồng độ thấp của SO2 và NO2 bằng nguyên lý hồng ngoại. Tín hiệu "
      "IR từ nguồn thường được ngắt nhịp hoặc điều chế để bù tín hiệu nền nhiệt. Cảm biến IR không "
      "tán sắc (NDIR) là thiết bị quang phổ đơn giản thường dùng làm cảm biến khí.",
      "The main components are an infrared source (lamp), a sample chamber or light tube, a "
      "wavelength sample chamber, and gas concentration is measured electro-optically by its "
      "absorption of a specific wavelength in the infrared (IR). The IR light is directed through "
      "the sample chamber towards the detector. In parallel there is another chamber with an "
      "enclosed reference gas, typically nitrogen. The detector has an optical filter in front of "
      "it that eliminates all light except the wavelength that the selected gas molecules can "
      "absorb. Ideally other gas molecules do not absorb light at this wavelength, and do not "
      "affect the amount of light reaching the detector to compensate for interfering components. "
      "For instance, CO2 and H2O often initiate cross sensitivity in the infrared spectrum. As "
      "many measurements in the IR area are cross sensitive to H2O it is difficult to analyze for "
      "instance SO2 and NO2 in low concentrations using the infrared light principle. The IR signal "
      "from the source is usually chopped or modulated so that thermal background signals can be "
      "offset from the desired signal. A non-dispersive infrared sensor (or NDIR) sensor is a "
      "simple spectroscopic device often used as gas")
    FIG(2, F.fig_f02())
    FIG(3, F.fig_f03())

    H("7.3.4 Máy phân tích khí theo độ dẫn nhiệt", "7.3.4 Thermal Conductivity Gas Analyzer", h3)
    P("Mỗi loại khí có khả năng dẫn nhiệt với tốc độ riêng, gọi là độ dẫn nhiệt. Tính chất này "
      "được dùng trong đầu dò độ dẫn nhiệt. Sợi kim loại nóng tiếp xúc với khí chuẩn và khí mẫu; "
      "lượng nhiệt khí mang đi làm thay đổi tốc độ làm nguội và do đó nhiệt độ sợi. Thay đổi nhiệt "
      "độ gây thay đổi điện trở; vì các sợi được mắc trong cầu Wheatstone, thay đổi điện trở được "
      "chuyển thành dòng điện làm tín hiệu đầu ra.",
      "Each gas has the ability to conduct heat at a specific rate. This is known as the thermal "
      "conductivity of the gas. This property is utilized in the thermal Conductivity detector. "
      "Heated metal filaments are exposed to the zero and sample gases. The amount of heat carried "
      "away by the gases changes the rate of cooling of the wire filament and, therefore its "
      "temperature. This temperature change causes a resistance change. Since the filaments are "
      "arranged in a Wheatstone bridge, the resistance change can be converted to an electrical "
      "current that is available as an output signal.")
    H("7.3.4.1 Ứng dụng", "7.3.4.1 Applications", h4)
    P("Máy phân tích độ dẫn nhiệt được dùng rộng rãi trong công nghiệp khi cần phân tích hỗn hợp "
      "hai khí. Phương pháp rất ổn định về độ trôi điểm không và khoảng đo. Ứng dụng gồm hỗn hợp "
      "khí bảo vệ hàn, hỗn hợp đóng gói thực phẩm, hỗn hợp phát hiện rò và khí xử lý nhiệt. Mỗi khí "
      "có độ dẫn nhiệt đã biết; cảm biến dùng bốn sợi đối xứng thay đổi điện trở theo độ dẫn nhiệt "
      "của khí đi qua. Độ dẫn nhiệt của một số khí cho trong bảng 2.",
      "The thermal conductivity analyzer has wide application in industry where it is desirable "
      "to analyze a two gas mixture. The thermal conductivity method is very stable in regards to "
      "span and zero drift. Applications include welding shield gas mixtures, food packaging "
      "mixtures, leak detection mixtures and heat treating atmosphere. Each gas has a known "
      "thermal conductivity. Thermal conductivity is measured with a sensor that employs four "
      "matched filaments that change resistance according to the thermal conductivity of the gas "
      "passing over it. The thermal conductivities of some gases can be found in the table 2 below.")
    TBL([C.T("KHÍ", "GAS", lang), C.T("ĐỘ DẪN NHIỆT", "THERMAL CONDUCTIVITY", lang)],
        [
            ("ACETYLENE", "4.400"), ("AMMONIA", "5.135"), ("ARGON", "3.880"),
            ("CARBON DIOXIDE", "3.393"), ("CARBON MONOXIDE", "5.425"),
            ("CHLORINE", "1.829"), ("ETHANE", "4.303"), ("ETHYLENE", "4.020"),
            ("HELIUM", "33.60"), ("HYDROGEN", "39.60"),
            ("HYDROGEN SULPHIDE", "3.045"), ("METHANE", "7.200"),
            ("NEON", "10.87"), ("NITRIC OXIDE", "5.550"),
            ("NITROUS OXIDE", "5.680"), ("NITROGEN", "3.515"),
            ("OXYGEN", "5.700"), ("SULPHUR DIOXIDE", "1.950"),
        ],
        C.T("Bảng-2: Độ dẫn nhiệt của các khí thông dụng",
           "Table-2: Thermal conductivities of common gases", lang))
    H("7.3.4.2 Nguyên lý hoạt động của phép phân tích độ dẫn nhiệt",
      "7.3.4.2 Principle of Operation for Thermal Conductivity Analysis", h4)
    P("Cảm biến dùng bốn sợi đối xứng thay đổi điện trở theo độ dẫn nhiệt của khí đi qua. Bốn sợi "
      "được mắc theo cấu hình cầu Wheatstone như hình dưới.",
      "The gas analyzer sensor uses four matched filaments that change resistance according to "
      "the thermal conductivity of the gas passing over it. These four filaments are connected in "
      "a Wheatstone Bridge configuration as shown below.")
    FIG(4, F.fig_f04())
    P("Khi cả bốn điện trở bằng nhau, VOUT bằng không và cầu được coi là cân bằng. Khi chỉnh zero, "
      "khí tham chiếu đi qua mọi sợi, điện trở như nhau (vì sợi đối xứng) nên cầu cân bằng. Khi khí "
      "mẫu đi qua một nửa cầu, giá trị V tương ứng với hàm lượng khí mẫu trong khí tham chiếu. Đầu "
      "dò là katharometer bốn phần tử, hai trong khí tham chiếu và hai trong dòng khí mẫu như hình 5.",
      "When all four resistances are the same, VOUT is zero and the bridge is considered balanced. "
      "When zeroing, the reference gas is passed over all the filaments, the resistances will be "
      "the same (because filaments are matched) and the bridge is balanced. When the sample gas is "
      "passed over half of the bridge, then V’s value correlates to the content of the sample gas "
      "in the reference. The detector is a four element Katharometer having two elements situated "
      "in the reference gas and two elements in the sample gas shown in Figure 5 below.")
    FIG(5, F.fig_f05())
    P("Bốn phần tử được nối điện trong mạch cầu và dòng không đổi chạy qua để đốt nóng. Nếu mỗi "
      "phần tử được bao bởi cùng một khí, nhiệt độ và điện trở tương tự nhau nên cầu cân bằng.",
      "The four elements are electronically connected in a bridge circuit and a constant current "
      "is passed through the bridge to heat the elements. If each element is surrounded by the "
      "same gas, then the temperature and hence the resistance of each element will be similar and "
      "the bridge circuit will be balanced.")
    FIG(6, F.fig_f06())
    P("Khi đưa khí cần đo vào dòng mẫu, hai phần tử katharometer trong dòng này bị làm nguội mạnh "
      "hơn hai phần tử trong khí tham chiếu. Mạch cầu mất cân bằng, tạo điện áp tín hiệu liên quan "
      "đến hàm lượng khí đo trong mẫu. Quan hệ này phi tuyến.",
      "When the gas to be measured is introduced into the sample gas stream, the two Katharometer "
      "elements in this gas stream will be cooled to a greater extent than the two elements in "
      "the reference gas. The bridge circuit will be unbalanced, producing a signal voltage "
      "related to the measure gas content of the sample gas. This relationship is non-linear.")
    P("Phép đo so sánh độ dẫn nhiệt của hỗn hợp với khí tham chiếu cho biết hàm lượng khí mẫu. "
      "Hydro có độ dẫn nhiệt lớn gấp khoảng bảy lần nitơ nên thay đổi nhỏ cũng dễ phát hiện; hầu "
      "hết khí thông thường có độ dẫn gần nitơ nên phương pháp khá chọn lọc. Heli là khí duy nhất "
      "khác có độ dẫn tương đương hydro.",
      "Measure the gas sample content of a sample/reference mixture by comparing the thermal "
      "conductivity of the mixture with that of a reference. For example, hydrogen has a thermal "
      "conductivity which is approximately seven times greater than that of nitrogen, so small "
      "changes are readily detected. All other common gases have thermal conductivities similar "
      "to nitrogen so the method of measurement is fairly selective. Helium is the only other gas "
      "with a thermal conductivity comparable with that of hydrogen.")
    U(["Carbon Dioxide", "Oxygen", "Argon", "Methane", "Sulphur Dioxide", "Ammonia"],
      ["Carbon Dioxide", "Oxygen", "Argon", "Methane", "Sulphur Dioxide", "Ammonia"])

    H("7.3.5 Máy phân tích khí loại thuận từ", "7.3.5 Paramagnetic Type Gas Analyzer", h3)
    P("Đây là máy phân tích oxy thuận từ loại quả tạ. Vì độ cảm từ của oxy lớn hơn các khí đồng hành, "
      "phép đo ổn định và không bị các khí đó ảnh hưởng. Đầu dò không có bộ phận gia nhiệt nên phù "
      "hợp đo nồng độ oxy trong khí cháy; hơn nữa không cần khí tham chiếu nên tiết kiệm chi phí "
      "vận hành. Nguyên lý dựa trên tính chất từ mạnh của phân tử oxy, nên phép đo hầu như không bị "
      "ảnh hưởng bởi phân tử có tính từ yếu hơn.",
      "This analyzer is a dumbbell type paramagnetic oxygen analyzer. Because this analyzer is "
      "based on that the magnetic susceptibility of oxygen gas is larger than coexisting gases, "
      "stable measurement is ensured unaffected by coexisting gases. The detector does not have a "
      "heating part such as heater. Therefore, this analyzer is suited for measuring the oxygen "
      "concentration in flammable gas. Further, running cost can be saved since reference gas is "
      "not required. The principle of measurement is dependent on the strong magnetic property of "
      "oxygen molecules. Therefore, measurement is almost unaffected by other molecules weaker in "
      "magnetic property than oxygen.")
    U(["Phù hợp đo oxy trong khí cháy.", "Kích thước nhỏ, dễ thao tác.",
       "Dùng được với nhiều nguồn điện.", "Đầu ra tuyến tính."],
      ["Suited for measuring oxygen in flammable gas.", "Small-sized and easy to handle.",
       "Usable with a wide range of power supplies.", "Output is linear"])
    FIG(7, F.fig_f07())
    P("Trong buồng, hai quả cầu thủy tinh chứa nitơ được treo bằng kim loại chắc chắn. Ban đầu quả "
      "cầu cân bằng trong từ trường không đồng nhất. Khi phân tử oxy có độ cảm từ lớn chảy qua, "
      "chúng bị kéo về vùng từ trường mạnh hơn và đẩy quả cầu ra xa. Độ lệch được phát hiện bằng "
      "nguồn sáng, gương phản xạ và phần tử thu sáng; dòng chạy trong vòng phản hồi được điều khiển "
      "để quả cầu trở về trạng thái cân bằng ban đầu. Dòng phản hồi tỷ lệ với nồng độ oxy, nhờ đó "
      "nồng độ oxy được chuyển thành tín hiệu điện.",
      "In the cell, two glass spheres filled with nitrogen gas are suspended with strong metal. At "
      "first, the spheres are kept in balance in an in homogeneous magnetic field. When oxygen "
      "molecules having a large magnetic susceptibility flow there, the molecules are pulled "
      "toward the stronger magnetic field zone and the spheres are moved away from the zone. The "
      "resulting deviation of the spheres is detected with the light source, reflecting mirror and "
      "light receiving element, and a current is flowed through the feedback loop to control so "
      "that the spheres can return to the initial balanced state. The current flowing through the "
      "feedback loop is proportional to oxygen concentration. Thus, oxygen concentration is "
      "converted into an electric signal.")

    H("7.3.6 Máy phân tích điện hóa", "7.3.6 Electrochemical Analyzer", h3)
    P("Cảm biến khí điện hóa là đầu dò đo nồng độ khí mục tiêu bằng cách oxy hóa hoặc khử khí đó "
      "tại điện cực và đo dòng sinh ra. Bắt đầu nghiên cứu từ năm 1962, ông Naoyoshi Taguchi là "
      "người đầu tiên trên thế giới chế tạo thiết bị bán dẫn có thể phát hiện nồng độ thấp của khí "
      "dễ cháy và khí khử với mạch điện đơn giản. Thiết bị dựa trên công nghệ này thường gọi là TGS "
      "(Taguchi Gas Sensors).",
      "Electrochemical gas sensors are gas detectors that measure the concentration of a target "
      "gas by oxidizing or reducing the target gas at an electrode and measuring the resulting "
      "current. Beginning his research in 1962, Mr. Naoyoshi Taguchi became the first person in "
      "the world to succeed in the development of a semiconductor device which could detect low "
      "concentrations of combustible and reducing gases when used with a simple electrical "
      "circuit. Devices based on this technology are often called “TGS” (Taguchi Gas Sensors).")
    H("7.3.6.1 Cấu tạo", "7.3.6.1 Construction", h4)
    P("Cảm biến chứa hai hoặc ba điện cực, đôi khi bốn, tiếp xúc với chất điện giải. Điện cực thường "
      "chế tạo bằng cách gắn kim loại quý có diện tích bề mặt lớn lên màng xốp kỵ nước. Điện cực làm "
      "việc tiếp xúc cả chất điện giải và không khí cần giám sát, thường qua màng xốp. Chất điện "
      "giải thường dùng nhất là axit khoáng, nhưng một số cảm biến dùng chất điện giải hữu cơ. Điện "
      "cực và vỏ thường bằng nhựa, có lỗ vào khí và tiếp điểm điện.",
      "The sensors contain two or three electrodes, occasionally four, in contact with an "
      "electrolyte. The electrodes are typically fabricated by fixing a high surface area "
      "precious metal on to the porous hydrophobic membrane. The working electrode contacts both "
      "the electrolyte and the ambient air to be monitored usually via a porous membrane. The "
      "electrolyte most commonly used is a mineral acid, but organic electrolytes are also used "
      "for some sensors. The electrodes and housing are usually in a plastic housing which "
      "contains a gas entry hole for the gas and electrical contacts.")
    H("7.3.6.2 Hoạt động", "7.3.6.2 Operation", h4)
    P("Khí khuếch tán vào cảm biến qua mặt sau màng xốp tới điện cực làm việc, tại đây bị oxy hóa "
      "hoặc khử. Phản ứng điện hóa tạo dòng chạy qua mạch ngoài. Ngoài việc đo, khuếch đại và xử lý "
      "tín hiệu, mạch ngoài duy trì điện áp giữa điện cực làm việc và điện cực đối (với cảm biến hai "
      "điện cực) hoặc giữa điện cực làm việc và điện cực tham chiếu (với ba điện cực). Tại điện cực "
      "đối xảy ra phản ứng ngược lại: nếu điện cực làm việc oxy hóa thì điện cực đối khử.",
      "The gas diffuses into the sensor, through the back of the porous membrane to the working "
      "electrode where it is oxidized or reduced. This electrochemical reaction results in an "
      "electric current that passes through the external circuit. In addition to measuring, "
      "amplifying and performing other signal processing functions, the external circuit "
      "maintains the voltage across the sensor between the working and counter electrodes for a "
      "two electrode sensor or between the working and reference electrodes for a three electrode "
      "cell. At the counter electrode an equal and opposite reaction occurs, such that if the "
      "working electrode is an oxidation, then the counter electrode is a reduction.")

    H("7.3.7 Bộ ORSAT", "7.3.7 ORSAT Apparatus", h3)
    P("Bộ phân tích khí ORSAT là thiết bị phòng thí nghiệm dùng để phân tích mẫu khí (thường là khí "
      "thải nhiên liệu hóa thạch) về hàm lượng oxy, carbon monoxide và carbon dioxide. Dù phần lớn "
      "đã được thay bằng kỹ thuật dụng cụ, ORSAT vẫn là phương pháp đo tin cậy và tương đối dễ dùng.",
      "An ORSAT gas analyzer is a piece of laboratory equipment used to analyze a gas sample "
      "(typically fossil fuel flue gas) for its oxygen, carbon monoxide and carbon dioxide "
      "content. Although largely replaced by instrumental techniques, the ORSAT remains a "
      "reliable method of measurement and is relatively simple to use.")
    FIG(8, F.fig_f08())
    H("7.3.7.1 Cấu tạo", "7.3.7.1 Construction", h4)
    P("Bộ gồm chủ yếu burette khí đã hiệu chuẩn có áo nước, nối bằng ống mao dẫn thủy tinh với hai "
      "hoặc ba pipet hấp thụ chứa dung dịch hóa học hấp thụ các khí cần đo. Để an toàn và dễ mang "
      "theo, bộ thường được đóng trong hộp gỗ.",
      "The apparatus consists essentially of a calibrated water-jacketed gas burette connected "
      "by glass capillary tubing to two or three absorption pipettes containing chemical "
      "solutions that absorb the gasses it is required to measure. For safety and portability, "
      "the apparatus is usually encased in a wooden box.")
    P("Các chất hấp thụ gồm:", "The absorbents are:")
    U(["Kali hydroxide (Caustic Potash)", "Pyrogallol kiềm", "Cuprous chloride amonia"],
      ["Potassium Hydroxide (Caustic Potash)", "Alkaline pyrogallol",
       "Ammoniacal Cuprous chloride"])
    P("Đáy burette nối với bình cân bằng để đọc ở áp suất không đổi và chuyển khí qua lại môi "
      "trường hấp thụ. Burette chứa nước hơi axit hóa cùng dấu vết chất chỉ thị hóa học (thường "
      "methyl orange) để tạo màu.",
      "The base of the gas burette is connected to a leveling bottle to enable readings to be "
      "taken at constant pressure and to transfer the gas to and from the absorption media. The "
      "burette contains slightly acidulated water with a trace of chemical indicator (typically "
      "methyl orange) for coloration.")
    H("7.3.7.2 Phương pháp phân tích", "7.3.7.2 Method of Analysis", h4)
    P("Khí cần phân tích được hút vào burette qua hệ thống ống cao su và xả qua lại vài lần; thường "
      "lấy 100 mL để dễ tính toán. Dùng vòi ngăn các burette hấp thụ, chỉnh mực chất lỏng trong bình "
      "và burette về điểm zero. Khí được đưa vào burette caustic potash, để yên khoảng hai phút "
      "rồi rút lại; lặp lại để hấp thụ hoàn toàn. Sau khi cân bằng mực, thể tích khí còn lại cho "
      "biết phần trăm CO2 đã hấp thụ. Lặp kỹ thuật này với oxy dùng pyrogallol và với carbon "
      "monoxide dùng cuprous chloride amonia.",
      "By means of a rubber tubing arrangement, the gas to be analyzed is drawn into the burette "
      "and flushed through several times. Typically, 100mls is withdrawn for ease of calculation. "
      "Using the stopcocks that isolate the absorption burettes, the level of gas in the leveling "
      "bottle and the burette is adjusted to the zero point of the burette. The gas is then "
      "passed into the caustic potash burette, left to stand for about two minutes and then "
      "withdrawn, isolating the remaining gas via the stopcock arrangements. The process is "
      "repeated to ensure full absorption. After leveling the liquid in the bottle and burette, "
      "the remaining volume of gas in the burette indicates the percentage of carbon dioxide "
      "absorbed. The same technique is repeated for oxygen, using the pyrogallol, and carbon "
      "monoxide using the ammoniacal cuprous chloride.")

    H("7.3.8 Phân tích trọng lượng", "7.3.8 Gravimetry Gas Analyzer", h3)
    FIG(9, F.fig_f09())
    P("Có thể xác định tổng carbon và hydro trong chất rắn bằng cách đốt cháy trong oxy tinh khiết, "
      "khô (hình 9). Khí cháy được oxy hóa hoàn toàn thành CO2 và H2O nhờ xúc tác kim loại chuyển "
      "tiếp. Bẫy thứ nhất, phosphorous pentoxide (P2O5), loại toàn bộ nước tạo thành; P2O5 có tính "
      "hút ẩm và là chất hút nước hiệu quả. Bẫy thứ hai chứa ascarite, tức hydroxide natri thấm trên "
      "amian, giữ toàn bộ CO2. Ống thứ ba bảo vệ hai ống kia khỏi nước và CO2 khí quyển chảy ngược. "
      "Sau khi mẫu oxy hóa hoàn toàn, cân các ống để xác định độ tăng khối lượng; phân tích dạng này "
      "đôi khi dùng cho bùn đã sấy, trầm tích, đất và chất hữu cơ hòa tan trong nước.",
      "Total carbon and hydrogen can be determined in a solid by combustion in the presence of "
      "pure, dry oxygen (Figure 9). The combustion gases are oxidized completely to CO2 and H2O "
      "with the aid of a transition metal catalyst. The first trap, phosphorus pentoxide (P2O5), "
      "efficiently removes all water formed. Recall that P2O5 is deliquescent, and an efficient "
      "desiccant. The second contains ascarite, which is sodium hydroxide-impregnated asbestos. "
      "This will trap all of the carbon dioxide. The third tube protects the other two from "
      "backflow of atmospheric water and carbon dioxide. After the sample is completely oxidized, "
      "the tubes are weighed to determine the increase. This type of analysis is sometimes "
      "conducted on dried sludges, sediments, soils, and extracted aquatic organic matter.")

    H("7.3.9 Máy đo mêtan", "7.3.9 Methanometer", h3)
    P("Máy đo mêtan dùng để đo phần trăm mêtan trong không khí hầm lò than và được thiết kế cảnh báo "
      "thợ mỏ về nồng độ nguy hiểm của khí này. Máy đo mêtan điện đầu tiên dùng trong hầm lò được "
      "phát triển năm 1949, gọi là W8, chạy bằng pin đèn cap Edison. Nhiều loại máy điện tử cầm tay "
      "ra đời trên thế giới trong thập niên 1950, nhưng máy độc lập đầu tiên, GP (general purpose), "
      "phải đến năm 1961 mới xuất hiện.",
      "The methanometer is an instrument to measure the percentage of methane in the air in "
      "underground Coal mines and has been designed to alert miners to the presence of "
      "potentially dangerous concentrations of this gas. The first electrical methanometer for "
      "use in coal mines was developed in 1949. It was known as the W8 methanometer and was "
      "powered by an Edison cap lamp battery. Several types of hand held electronic "
      "methanometers were developed around the world during the 1950’s but the first "
      "independently powered instrument, the GP (general purpose) methanometer, was not introduced "
      "until 1961.")
    FIG(10, F.fig_f10())
    P("Khí mêtan rất dễ cháy, cháy rất nhanh khi tiếp xúc oxy. Các vụ cháy mêtan ở khu vực hầm lò "
      "cho thấy cần bảo vệ người lao động tốt hơn. Máy giám sát mêtan cầm tay hiện được một số thợ "
      "mỏ dùng để đo định kỳ tại gương khai thác. Máy là một dạng đầu dò khí mêtan lắp vào đèn cap "
      "và đeo trên mũ, có thể liên tục phát tín hiệu báo động khi nồng độ vượt mức cài đặt.",
      "Methane gases are highly combustible in nature. It burns very quickly when it comes in "
      "contact with oxygen. Methane ignitions that have occurred in mine out by areas indicate "
      "the need to provide better protection to workers. Handheld methane monitors are now used "
      "by some miners to make periodic measurements of methane at the working face. Methanometer "
      "is one of instrument used as methane gas detector which is incorporated into a miner’s cap "
      "lamp and worn on a miner’s helmet can continuously provide an alarm signal whenever "
      "methane levels exceed a set level.")
    P("Các thử nghiệm đánh giá đặc tính của đầu dò bằng cách đo thời gian đáp ứng với mêtan cấp qua "
      "giá hiệu chuẩn hoặc bộ chuyển tiếp, hoặc đặt đầu dò trong buồng thử nghiệm môi trường; hiệu "
      "năng cũng được đánh giá trong đường hầm thử quy mô đầy đủ. Nồng độ mêtan cao nhất trong hầm "
      "than khí thường gần gương khai thác đang hoạt động. Hỗn hợp mêtan trong không khí có thể bắt "
      "lửa khi nồng độ từ 5 đến 15 phần trăm theo thể tích. Mêtan cũng có thể tụ lại ở khu vực phía "
      "sau gương do giải phóng chậm ở nơi thông gió kém, phun khí đột ngột từ vỉa hoặc di cư từ khu "
      "vực đã khai thác.",
      "Tests were conducted to evaluate the performance characteristics of this methane detector "
      "by measuring response times with methane gas supplied through a calibration fixture or "
      "adaptor. Other response time tests were performed with the detector in an environmental "
      "test box. Performance was also evaluated in a full scale test gallery where face methane "
      "emission and underground ventilation. The highest methane concentrations in gassy coal "
      "mines are most likely to occur near active mining faces. Methane in air mixtures can be "
      "ignited if the methane concentrations are between 5 and 15 pct by volume Methane gas can "
      "also accumulate in areas out by the face due to slow liberation in poorly ventilated "
      "areas, a sudden outburst of gas from the seam, or a migration of gas from worked out areas.")
    P("Không yêu cầu giám sát mêtan thường xuyên ở những khu vực đó. Khi làm việc hoặc đi qua, "
      "người lao động có thể phơi nhiễm hỗn hợp mêtan dễ cháy mà không có cảnh báo. Đầu dò được "
      "thiết kế đeo cho thợ mỏ và báo động khi nồng độ vượt ngưỡng định trước, bằng cả tín hiệu "
      "nhìn và âm thanh.",
      "No regular monitoring for methane is required in these areas. When working in or traveling "
      "through these out by areas, workers can be exposed to ignitable mixtures of methane without "
      "any warning. Gas detector is designed to be worn by miners and provide them with an alarm "
      "whenever methane levels exceed a predetermined limit. It is designed to alert them with "
      "both visual and aural alarms when methane concentrations are excessive.")

    H("7.3.10 Hệ thống đo zirconia", "7.3.10 Zirconia Type Measurement System", h3)
    H("7.3.10.1 Hệ thống nồng độ", "7.3.10.1 Concentration Cell System", h4)
    P("Chất điện giải rắn như zirconia có tính dẫn ion oxy ở nhiệt độ cao. Khi gắn điện cực platin "
      "xốp ở hai mặt phần tử zirconia được đốt nóng và đưa khí có nồng độ oxy riêng biệt tiếp xúc "
      "với từng mặt, thiết bị hoạt động như pin nồng độ oxy. Hiện tượng này sinh ra lực điện động "
      "giữa hai điện cực theo phương trình Nernst, tỷ lệ với nồng độ oxy.",
      "A solid electrolyte like zirconia exhibits conductivity of oxygen ions at high temperature. "
      "As shown in the figure, when porous platinum electrodes are attached to both sides of the "
      "zirconia element to be heated up and gases of different partial oxygen concentrations are "
      "brought into contact with the respective surfaces of the zirconia, the device acts as an "
      "oxygen concentration cell. This phenomenon causes an electromotive force to be generated "
      "between both electrodes according to Nernst’s equation. And it is proportional oxygen "
      "concentration.")
    P("<b>Ưu điểm:</b> lắp trực tiếp vào quá trình cháy như ống khói lò hơi, không cần hệ thống lấy "
      "mẫu và đáp ứng nhanh hơn.<br/><b>Nhược điểm:</b> nếu khí mẫu chứa khí dễ cháy sẽ gây sai số "
      "đo (khí thải cháy hoàn toàn hầu như không gây vấn đề).",
      "<b>Advantages:</b> Can be directly installed in a combustion process such as a boiler’s "
      "flue and requires no sampling system, and response is faster.<br/><b>Disadvantages:</b> If "
      "the sample gas contains a flammable gas, a measurement error occurs (combustion exhaust gas "
      "causes almost no problem because it is completely burned).")
    H("7.3.10.2 Loại dòng giới hạn", "7.3.10.2 Limiting Current Type", h4)
    P("Nếu hạn chế dòng oxy vào cathode của phần tử zirconia đốt nóng cao, sẽ có vùng mà dòng không "
      "đổi dù điện áp đặt tăng. Dòng giới hạn này tỷ lệ với nồng độ oxy.",
      "As shown in the figure below, if the flow of oxygen into the cathode of a zirconia element "
      "heated to high temperature is limited, there appears a region where the current becomes "
      "constant even when the applied voltage is increased. This limited current is proportional "
      "to the oxygen concentration.")
    U(["Có thể đo nồng độ oxy vết.", "Chỉ cần hiệu chuẩn phía khoảng đo (không khí)."],
      ["Capable of measuring trace oxygen concentration.",
       "Calibration is required only on the span side (air)."])
    U(["Nếu khí mẫu chứa khí dễ cháy sẽ gây sai số đo.",
       "Bụi làm tắc lỗ khuếch tán khí phía cathode; phải lắp bộ lọc ở công đoạn trước."],
      ["If the sample gas contains a flammable gas, a measurement error occurs.",
       "The presence of dust causes clogging of the gas diffusion holes on the cathode side; a "
       "filter must be installed in a preceding stage."])

    H("7.3.11 Khí thải và thành phần khí thải", "7.3.11 Exhaust (Flue) Gas and Exhaust Gas Composition", h3)
    P("Khí thải sinh ra trong quá trình cháy được gọi là khí lò hoặc khí ống khói. Thành phần phụ "
      "thuộc loại nhiên liệu và điều kiện cháy, ví dụ giá trị tỷ lệ không khí. Nhiều thành phần là "
      "chất ô nhiễm không khí và phải được loại bỏ hoặc giảm thiểu bằng quy trình làm sạch đặc biệt "
      "trước khi thải ra khí quyển theo quy định của chính phủ. Khí ở trạng thái ban đầu gọi là khí "
      "thô, sau làm sạch gọi là khí sạch.",
      "Exhaust gas generated through combustion processes is called flue gas or stack gas. Its "
      "composition depends on the type of fuel and the combustion conditions, e.g. the air ratio "
      "value. Many flue gas components are air pollutants and must therefore, due to governmental "
      "regulations be eliminated or minimized by special cleaning procedures before the gas is "
      "released to the atmosphere. The exhaust gas in its original status is called raw gas, after "
      "cleaning it is called clean gas.")
    P("<b>Nitơ (N2)</b> là thành phần chính (79% thể tích) của không khí, không màu, không mùi, "
      "không vị; đi vào lò cùng không khí cháy nhưng không tham gia trực tiếp vào quá trình cháy. "
      "Nó đóng vai trò vật liệu ballast và mang nhiệt thải ra khí quyển. Tuy nhiên, một lượng nhỏ "
      "nitơ từ không khí cháy, cùng nitơ từ nhiên liệu, gây hình thành oxit nitơ nguy hiểm.",
      "<b>Nitrogen (N2)</b> is the main constituent (79 Vol. %) of air. This colorless, odorless "
      "and tasteless gas is fed to the combustion as part of the combustion air but is not "
      "involved directly in the combustion process. It acts as ballast material and carrier of "
      "wasted heat and is released again into the atmosphere. However, minor quantities of this "
      "combustion air related nitrogen are, together with the nitrogen released from the fuel, "
      "responsible for the formation of the dangerous nitrogen oxides")
    P("<b>Carbon dioxide (CO2)</b> là khí không màu, không mùi, hơi chua; sinh ra trong mọi quá trình "
      "cháy kể cả hô hấp. Khả năng lọc bức xạ nhiệt khiến nó góp phần đáng kể vào hiệu ứng nhà kính. "
      "Trong không khí nồng độ CO2 là 0,03%; trên 15% gây mất ý thức ngay lập tức.",
      "<b>Carbon Dioxide (CO2)</b> is a colorless and odorless gas with a slightly sour taste. It "
      "is produced during all combustion processes including respiration. It contributes "
      "considerably to the greenhouse effect through its ability to filter heat radiation. In "
      "ambient air CO2 concentration is 0,03%; at concentrations of over 15% loss of consciousness "
      "will occur immediately.")
    P("<b>Hơi nước (độ ẩm)</b> được tạo thành khi hydro trong nhiên liệu phản ứng với oxy; cùng với "
      "độ ẩm của nhiên liệu và không khí cháy, tồn tại dưới dạng hơi ẩm ở nhiệt độ cao hoặc ngưng tụ "
      "ở nhiệt độ thấp. <b>Oxy (O2)</b> phần không bị tiêu thụ còn lại trong khí thải, là thước đo "
      "hiệu suất cháy, dùng xác định thông số cháy và làm giá trị tham chiếu.",
      "<b>Water Vapor (Humidity)</b> — the hydrogen contained in the fuel will react with oxygen "
      "and form water (H2O). This, together with the water content of the fuel and the combustion "
      "air, exists either as flue gas humidity (at higher temperatures) or as condensate (at lower "
      "temperatures). <b>Oxygen (O2)</b> — the portion of oxygen that has not been consumed by the "
      "combustion process remains as part of the flue gas and is a measure for the efficiency of "
      "the combustion. It is used for the determination of combustion parameters and acts also as "
      "reference value.")
    P("<b>Carbon monoxide (CO)</b> là khí độc không màu, không mùi, chủ yếu sinh ra khi cháy không "
      "hoàn toàn nhiên liệu hóa thạch. Ngoài trời CO ít nguy hiểm vì phản ứng nhanh với oxy thành "
      "CO2, nhưng trong nhà hoặc không gian kín rất nguy hiểm: nồng độ chỉ 700 ppm trong không khí "
      "thở gây tử vong trong vài giờ! Ngưỡng nơi làm việc là 50 ppm.",
      "<b>Carbon Monoxide (CO)</b> is a colorless, odorless, toxic gas. It is formed predominantly "
      "during incomplete combustion of fossil fuels and other materials containing carbon. "
      "Outdoors in ambient conditions CO is not very dangerous for human beings because of its "
      "fast reaction to CO2 with oxygen. However, indoors or within enclosed spaces it must be "
      "considered as very dangerous, as at concentrations of only 700 ppm in the breathing air it "
      "will lead to death within a few hours! The working place threshold value is 50 ppm.")
    P("<b>Oxit nitơ (NO và NO2, ký hiệu chung NOx)</b> hình thành khi nitơ trong nhiên liệu và, ở "
      "nhiệt độ cao, nitơ trong không khí cháy phản ứng với oxy tạo nitơ oxit; NO tiếp tục phản ứng "
      "trong ống khói hoặc khí quyển thành NO2. Cả hai đều độc; NO2 là độc tố phổi nguy hiểm và "
      "góp phần tạo ozone dưới ánh sáng mặt trời. Công nghệ SCR (Selective Catalytic Reaction) được "
      "dùng để làm sạch NOx, ngoài ra có biện pháp cấp khí từng giai đoạn để giảm hình thành oxit "
      "nitơ ngay trong quá trình cháy.",
      "<b>Oxides of nitrogen (NO and NO2, sum formula NOx)</b> — In combustion processes nitrogen "
      "of the fuel and, at high temperatures, also of the combustion air reacts to a certain "
      "amount with oxygen of the combustion air and forms first nitric oxide (fuel-NO and "
      "thermal-NO). This NO will react with oxygen already in the stack and/or later on in the "
      "atmosphere and form the dangerous nitrogen dioxide (NO2). Both oxides are toxic! "
      "Specifically NO2 is a dangerous lung poison and contributes, in connection with sun light, "
      "to the formation of ozone. Extensive technologies are used to clean flue gases from NOx, "
      "e.g the Selective Catalytic Reaction (SCR) process. In addition to that, special measures "
      "(e.g. staged air supply) have been developed to reduce the formation of nitrogen oxides "
      "already during combustion process.")
    P("<b>Sulphur dioxide (SO2)</b> là khí độc, không màu, mùi hăng, sinh ra khi oxy hóa sulphur "
      "trong nhiên liệu; ngưỡng nơi làm việc 5 ppm. Với nước hoặc hơi ngưng tụ tạo axit sulfurous "
      "(H2SO3) và axit sulfuric (H2SO4), gây hư hại thiên nhiên và công trình (mưa axit). Công nghệ "
      "rửa khí dùng để loại oxit sulphur.",
      "<b>Sulfur Dioxide (SO2)</b> is a colorless, toxic gas with a pungent smell. It is formed "
      "through oxidation of sulfur that is present in the fuel. The working place threshold limit "
      "value is 5 ppm. Together with water or condensate sulfurous acid (H2SO3) and sulfuric acid "
      "(H2SO4) are formed, both of which are responsible for various damages to e.g. nature and "
      "buildings (acid rain). Scrubbing technologies are used to clean flue gases from sulfur "
      "oxides.")
    P("<b>Hydrogen sulphide (H2S)</b> là khí độc, mùi rất rõ dù nồng độ rất thấp (khoảng 2,5 µg/m³); "
      "có trong dầu thô và khí tự nhiên nên hiện diện ở nhà máy lọc dầu và khí đốt, cũng như một số "
      "quá trình công nghiệp khác và trong xúc tác xe cơ giới do cháy không hoàn toàn. H2S được loại "
      "khỏi khí thải bằng chuyển hóa thành SO2 qua hấp thụ hoặc, với lượng lớn, phản ứng thành sulphur "
      "nguyên tố (quá trình Claus).",
      "<b>Hydrogen Sulfide (H2S)</b> is a toxic and, even at very low concentrations (appr. 2,5 "
      "µg/m3 ), very odorous gas. It is a component of crude oil and natural gas and is therefore "
      "present in refineries and Natural Gas plants but also generated during some other "
      "industrial processes and, as product of an incomplete combustion, in catalysts of motor "
      "vehicles. H2S is removed from exhaust gases by conversion to SO2 through certain absorption "
      "processes or, for larger quantities, through reaction to elemental sulfur (Claus process).")
    P("<b>Hydrocarbon (CxHy hoặc HC)</b> là nhóm hợp chất gồm hydro và carbon, quan trọng nhất trong "
      "hóa hữu cơ, có trong dầu thô, khí tự nhiên và than. Phát thải xảy ra trong sản xuất, sử dụng "
      "và thải bỏ sản phẩm hydrocarbon; dung môi, nhựa, sơn, nhiên liệu xe là ví dụ. CxHy cũng sinh "
      "ra từ cháy không hoàn toàn như cháy rừng và thuốc lá, góp phần vào hiệu ứng nhà kính. Có "
      "hàng ngàn hợp chất gồm methane (CH4), butane (C4H10), benzene (C6H6) và hợp chất gây ung thư "
      "như benzo[a]pyrene. Tổng hydrocarbon dễ bay hơi trong khí thải thường gọi là “total "
      "hydrocarbon” và là giá trị được quy định, đo trong kiểm soát phát thải.",
      "<b>Hydrocarbons (CxHy or HC)</b> are an extensive group of chemical compounds that are "
      "composed of hydrogen and carbon. CxHy are the most important substances in organic "
      "chemistry; in nature they are contained in crude oil, natural gas, and coal. Emissions may "
      "occur during production of Hydrocarbon products (e.g. in refineries) as well as during "
      "their use and disposal. Other examples include solvents, plastics, varnish, vehicle fuels "
      "etc. Sources of CxHy emissions are also formed through incomplete combustion processes e.g. "
      "forest fires and cigarettes as well. Hydrocarbon emissions also contribute to the "
      "greenhouse effect. Hydrocarbons include thousands of compounds, methane (CH4), butane "
      "C4H10), benzene (C6H6), and also carcinogenic compounds such as benzo[a]pyrene. The total "
      "amount of volatile hydrocarbons in a flue gas is often described as “total hydrocarbon”. "
      "In emission control normally the value of “total hydrocarbon” is specified and measured.")
    P("<b>Axit hydrocyanic (HCN)</b>, còn gọi axit prussic, là chất lỏng rất độc với điểm sôi chỉ "
      "25,6 °C; có thể có trong khí thải của nhà máy đốt. <b>Ammonia (NH3)</b> liên quan đến khí "
      "thải ở nhà máy khử nitơ SCR: được cấp với lượng chính xác để tách oxit nitơ thành nitơ và "
      "nước; phần không tiêu thụ tiếp tục được khử, nồng độ trong khí sạch thường dưới 2 mg/m³.",
      "<b>Hydrocyanic Acid (HCN)</b> known also as prussic acid is a very toxic liquid with a "
      "boiling point of only 25,6 °C; it may exist in flue gases of incineration plants. "
      "<b>Ammonia (NH3)</b> is relevant in flue gases in connection with denitrification plants "
      "using the SCR process. It is fed to the flue gas in exact quantities and causes a reaction "
      "that splits the nitrogen oxides into nitrogen and water. The unconsumed portion of ammonia "
      "is further reduced; its concentration in the clean gas is normally below 2 mg/m3.")
    P("<b>Halogen hidro (HCl, HF)</b> có thể hình thành khi đốt than hoặc rác thải, tạo axit ăn mòn "
      "trong môi trường ẩm; gần như được loại hoàn toàn khỏi khí thải bằng rửa khí. <b>Chất rắn "
      "(bụi, bồ hóng)</b> có nguồn gốc thành phần không cháy của nhiên liệu rắn hoặc lỏng: oxit "
      "silica, nhôm, calci với than, hoặc sunfat của các nguyên tố với dầu nặng. Bụi nguy hiểm vì "
      "hạt có thể phủ chất độc hoặc gây ung thư.",
      "<b>Hydrogen Halides (HCl, HF)</b> — From combustion of coal and/or waste material the "
      "formation of the hydrogen halides HCl and HF may result which form aggressive acids in "
      "humid atmospheres. These compounds are eliminated almost totally from the flue gas through "
      "scrubbing processes. <b>Solids (dust, soot)</b> — Solid pollutants in flue gases originate "
      "from the incombustible components of solid or liquid fuels. These include oxides of silica, "
      "aluminum, and calcium in case of coal, or sulfates of different elements in case of heavy "
      "fuel oil. Dust is dangerous for human beings as dust particles may be covered with toxic "
      "and/or carcinogenic substances.")

    # ---------------------------------------------------------------- 7.4
    H("7.4 Phân tích cháy khí công nghệ trong công nghiệp",
      "7.4 Combustion Analysis of Process Gases in Industry")
    P("Phân tích cháy (tức kỹ thuật đo để phân tích thành phần khí cháy) là công cụ không thể "
      "thiếu để điều khiển quá trình tin cậy và kinh tế trong hầu hết mọi ngành. Mọi quá trình "
      "cháy đều liên quan đến sản xuất và xử lý vật liệu. Hình 11 cho thấy các đoạn của quá trình "
      "cháy từ cấp nhiên liệu và không khí cháy vào lò, bản thân sự cháy với nhiều quá trình liên "
      "quan, đến làm sạch khí thải và kiểm soát phát thải.",
      "Combustion analysis (i.e. measuring technology for analyzing combustion gas compositions) "
      "is an indispensable tool for reliable and economical process control in almost all "
      "industries. All combustion processes are concerned with production and material treatment "
      "processes. Fig. 11 shows the various segments of a combustion process from feed of fuel and "
      "combustion air to the furnace, the combustion itself with the variety of connected "
      "processes, up to flue gas cleaning and emission control.")
    FIG(11, F.fig_f11())
    P("Máy phân tích khí được các nhà sản xuất cung cấp với nhiều dạng; dựa trên các nguyên lý đo "
      "khác nhau, thường tối ưu cho phân tích một thành phần nhất định. Máy được dùng rộng rãi để "
      "phân tích khí cháy, trong đó kiểm soát phát thải chỉ là một lĩnh vực. Các ứng dụng sau đã "
      "được thiết lập:",
      "Gas analyzers are offered in great variety by many manufacturers. Analyzers are based on "
      "different measuring principles, mostly optimized for the analysis of certain components. "
      "Gas analyzers are extensively utilized in industry for the analysis of combustion gases "
      "with the area of emission control being just one field of application. The following "
      "applications are well established:")
    U(["Đo chỉnh và bảo trì để nâng cấp nhà máy, xác định bất ổn định của quá trình, kiểm tra sau "
       "sửa chữa hoặc chuẩn bị cho đo theo quy định.",
       "Đo quá trình để tối ưu cháy, phân tích nhiên liệu, không khí cháy và khí cháy nhằm giảm chi "
       "phí nhiên liệu, tăng hiệu suất hoặc kéo dài tuổi thọ nhà máy; cũng liên quan kiểm soát phát "
       "thải vì vận hành tối ưu thường làm giảm phát thải.",
       "Đo quá trình để điều khiển bầu khí khống chế trong lò hoặc lò nung chuyên biệt cho các "
       "quá trình như nung (ví dụ xi măng), thiêu kết hoặc xử lý bề mặt.",
       "Đo quá trình và phát thải để kiểm soát chức năng của thiết bị làm sạch khí thải.",
       "Đo phát thải tại ống khói để giám sát giá trị chất ô nhiễm và bảo đảm tuân thủ quy định."],
      ["Adjustment and service measurements for general plant upgrade purposes, for localization "
       "of process instabilities, for checks after repair work or as preparation in advance of "
       "regulatory measurements.",
       "Process measurements for combustion optimization analyzing fuel, combustion air and "
       "combustion gases in order e.g. to reduce fuel costs, to improve plant efficiency or to "
       "extend the lifetime of the plant. These applications are also related to emission control "
       "(see below) because optimized plant operation normally will cause a reduction of emission "
       "levels.",
       "Process measurements for control of a defined gas atmosphere in special furnaces or kilns "
       "for processes such as burning (e.g. cement), sintering or surface treatment.",
       "Process and emission measurements for function control of flue gas cleaning installations.",
       "Emission measurements at the stack to monitor the emission values of pollutants and to "
       "ensure compliance with the official regulations."])

    H("7.4.1 Phân tích khí để tối ưu cháy", "7.4.1 Gas Analysis for Combustion Optimization", h3)
    P("Những đóng góp chính cho tối ưu cháy là:", "Major contributions to combustion optimization are made by:")
    U(["Thành phần nhiên liệu và không khí cháy", "Quy trình đánh lửa và nhiệt độ cháy",
       "Chi tiết thiết kế đầu đốt và buồng đốt", "Tỷ lệ nhiên liệu/không khí"],
      ["Composition of fuel and combustion air", "Ignition procedure and combustion temperature",
       "Details of burner and combustion chamber design", "The fuel/air ratio"])
    P("Với nhà máy và nhiên liệu đã cho, tỷ lệ nhiên liệu/không khí cháy tối ưu (giá trị ex.air) "
      "được xác định từ kết quả phân tích khí nhờ giản đồ cháy (hình 12). Trên giản đồ, nồng độ CO, "
      "CO2 và O2 được biểu diễn theo giá trị không khí dư. Đường ứng với cháy lý tưởng không dư "
      "khí (ex.air=1) nằm giữa; về bên phải không khí dư tăng, về bên trái là thiếu không khí "
      "(ex.air<1).",
      "For a given plant and a given fuel the optimum fuel/combustion air ratio (ex.air value) can "
      "be determined from gas analysis results using the combustion diagram, see fig. 12. In this "
      "diagram the concentration of the gas components CO, CO2 and O2 are displayed in function of "
      "the excess excess air value. The line representing ideal combustion without any excess air "
      "(ex.air=1) is in the center of the diagram; to the right the excess air value increases; "
      "air deficiency (ex.air<1).")
    FIG(12, F.fig_f12())
    P("Giản đồ cháy cho thông tin sau:", "The combustion diagram provides the following information:")
    H("Vùng bên trái với ex.air<1 (thiếu không khí)",
      "Left area with ex.air<1 (deficiency of air)", h4)
    U(["Có CO vì không đủ oxy để oxy hóa hết CO thành CO2; CO có thể nguy hiểm cho người nếu rò rỉ.",
       "Khi hàm lượng oxy tăng, nồng độ CO giảm do oxy hóa thành CO2 và CO2 tăng tương ứng. Phản ứng "
       "dừng tại hoặc ngay trên ex.air=1, CO về không và CO2 đạt cực đại.",
       "Oxy hầu như không hiện diện ở vùng này vì toàn bộ oxy cấp vào được tiêu thụ ngay để oxy hóa "
       "CO thành CO2."],
      ["CO exist because there is not enough oxygen available to oxidize all CO to CO2. Note: CO "
       "may be dangerous to people when it escapes through leaks.",
       "With increasing oxygen content the CO concentration decreases through oxidation to CO2; "
       "CO2 concentration increases accordingly. This reaction will be stopped at or slightly "
       "above ex.air=1, CO will be zero and CO2 reach its maximum value.",
       "Oxygen is not or almost not present in this area because all oxygen supplied to the system "
       "is consumed immediately to oxidize CO to CO2"])
    H("Vùng bên phải với ex.air>1 (dư không khí)",
      "Right area with ex.air>1 (excess of air)", h4)
    U(["O2 tăng vì lượng oxy cấp cùng thể tích không khí cháy tăng không còn được tiêu thụ cho oxy "
       "hóa (CO gần như bằng không). Thực tế vẫn cần một lượng dư nhất định để cháy hoàn toàn do "
       "phân bố không khí không đồng đều trong buồng đốt. Kích thước hạt nhiên liệu cũng ảnh hưởng: "
       "hạt càng nhỏ tiếp xúc với oxy càng nhiều và cần ít không khí dư hơn.",
       "CO2 giảm lại so với cực đại tại ex.air=1 do hiệu ứng pha loãng của thể tích không khí cháy "
       "tăng, vốn hầu như không chứa CO2."],
      ["Here O2 increases because the amount of oxygen supplied as part of the increasing volume "
       "of combustion air is no longer consumed for oxidation (CO is almost zero). Practically, "
       "however, some amount of air (oxygen) excess is required for complete combustion because "
       "of the inhomogeneous distribution of air (oxygen) in the combustion chamber. Furthermore "
       "the fuel particle size influences combustion: the smaller the particles, the more contact "
       "between fuel and oxygen will be and the less excess air (oxygen) will be required.",
       "CO2 will decrease again relatively to the maximum value at ex.air=1 because of the dilution "
       "effect caused by the increasing volume of combustion air which itself carries almost no "
       "CO2."])
    P("Khoảng không khí dư tối ưu của một nhà máy xác định được từ nồng độ CO2 và CO (riêng CO2 "
      "không đủ vì đường có cực đại); hiện nay thường dùng phương pháp O2. Vị trí điểm lấy mẫu có "
      "thể khác nhau tùy thiết kế và đơn vị vận hành. Các hàm trên giản đồ được chứng minh bằng phép "
      "đốt than cứng trong bảng 3.",
      "The optimum range of excess air for a particular combustion plant can be determined from "
      "the concentration values of CO2 and CO (CO2 alone is not definite due to the curve "
      "maximum). Currently the O2-method is more often used. Sampling point locations may differ "
      "from plant to plant depending on the plant design and plant operator. The functions shown "
      "in the combustion diagram are substantiated for the combustion of hard coal in table 3:")
    TBL([C.T("Hệ số không khí λ", "Air value λ", lang),
         C.T("Không khí dư [%]", "Excess air [%]", lang),
         C.T("Hàm lượng oxy [%] (khí thải khô)", "Oxygen content [%] (dry flue gas)", lang)],
        [
            ("0,9", C.T("Thiếu không khí", "Air deficiency", lang),
             C.T("Thiếu oxy", "Oxygen deficiency", lang)),
            ("1,0", "0", "0"),
            ("1,1", "10%", "2"),
            ("1,2", "20%", "3,5"),
            ("1,3", "30%", "4,8"),
            ("1,4", "40%", "6,2"),
        ],
        C.T("Bảng 3: Hệ số không khí, không khí dư và hàm lượng oxy trong quá trình đốt than cứng",
           "Table 3: Air value, excess air and oxygen content for the combustion process of hard coal",
           lang))
    P("Ngoài giảm phát thải, tối ưu cháy ở mức không khí dư hiệu quả nhất còn nhằm tiết kiệm nhiên "
      "liệu. Theo kinh nghiệm và tài liệu đã công bố, giảm dư oxy 1 điểm phần trăm, ví dụ từ 4,5% "
      "xuống 3,5%, tăng hiệu suất nhà máy 1%. Với chi phí nhiên liệu 15 triệu USD mỗi tháng của "
      "một nhà máy điện cỡ trung, tiết kiệm 30.000 USD mỗi tháng nếu nhờ phân tích khí tin cậy mà "
      "vận hành gần hơn 0,2 điểm phần trăm đến giá trị không khí dư tối ưu. Tiết kiệm tương tự khi "
      "phát hiện và loại bỏ sớm sai lệch ngắn hạn nhờ giám sát khí liên tục.",
      "Optimization of a combustion process through plant operation at the most effective excess "
      "air level has, besides reduction of emission levels, the objective of saving fuel costs. "
      "Based on experience and documented in the literature is the fact, that reduction of oxygen "
      "excess of 1%-point, e.g. from 4,5% to 3,5%, will improve the efficiency of the combustion "
      "plant by 1%. With fuel costs of $ 15 Mio. per month for a middle sized power station this "
      "results in monthly cost savings of $ 30.000 if, by means of reliable gas analysis, the "
      "plant can be operated at only 0,2%-point closer to the optimal excess air value than "
      "before! Similar savings are possible if short time deviations from optimum operation "
      "conditions are recognized and eliminated early by using gas analysis continuously")

    H("7.4.2 Phân tích cháy để điều khiển quá trình",
      "7.4.2 Combustion Analysis for Process Control", h3)
    H("7.4.2.1 Nhà máy cháy cho quá trình nung",
      "7.4.2.1 Combustion Plant for Firing Processes", h4)
    P("Khác với nhà máy lò hơi quen thuộc, nhà máy nung có đặc điểm tiếp xúc trực tiếp giữa ngọn "
      "lửa, khí nóng và vật liệu hoặc phôi gia công cần xử lý nhiệt. Nhiệt và bầu khí cụ thể mà "
      "vật liệu tiếp xúc gây ra các bước nhất định trong quá trình sản xuất. Sản xuất clinker xi "
      "măng là ví dụ điển hình:",
      "A process firing plant, in contrast to the well-known boiler plants, is characterized by "
      "a direct contact between the flame and the hot firing gases and a material or work pieces "
      "that shall be treated thermally. The heat as well as the specific atmosphere to which the "
      "material is exposed causes certain steps in their production process. Production of cement "
      "clinker is a good example for such a firing process:")
    U(["Nguyên liệu ẩm được nghiền và sấy bằng khí thải nóng; bột liệu đã lắng được đốt nóng tới "
       "800 °C bằng khí nóng ngược chiều.",
       "CO2 bị đẩy ra khỏi bột liệu ở khoảng 950 °C trong lò nung calciner qua quá trình nung đa "
       "cấp (khử axit).",
       "Cuối cùng bột liệu cùng phụ gia được thiêu kết trong lò ở khoảng 1400 °C."],
      ["The moist raw material is crushed and dried using hot off gases The precipitated raw meal "
       "is heated up to 800 °C by hot gases in counter-current",
       "CO2 is driven off the raw meal at appr. 950 °C in the calcinator through a multi-stage "
       "firing process (de-acidification)",
       "The raw meal together with additives is finally sintered in the kiln at appr. 1400 °C."])
    P("Phân tích cháy tại các vị trí này cung cấp thông tin quan trọng về giá trị không khí dư, "
      "phát hiện và tính toán dòng khí giả, và lập cân bằng cho từng bước riêng. Điều này đặc biệt "
      "quan trọng cho hiệu năng calciner (đo CO2 và O2) vì mức calcination thiếu có thể gây rối loạn "
      "đáng kể trong vận hành lò.",
      "Combustion analysis at these locations provides critical information with regard to excess "
      "air values, to detect and calculate false air flows and to perform balances for each step "
      "separately. It is critical for the calcinator performance (measurement of CO2 and O2) "
      "because a deficient level of calcination can cause considerable malfunctions in kiln "
      "operation")
    P("Trong quá trình nung, chất từ vật liệu được xử lý có thể thoát vào khí “nung” làm tăng tốc độ "
      "phát thải. Đôi khi ngược lại, thành phần gồm cả chất ô nhiễm chuyển từ khí sang vật liệu sản "
      "phẩm hoặc vào chất được chuẩn bị riêng (ví dụ xỉ). Ví dụ ngành xi măng hoặc vôi: sulphur của "
      "nhiên liệu chuyển thành SO2 vào sản phẩm thay vì thải ra khí quyển. Ngược lại, trong sản xuất "
      "thủy tinh hoặc gạch, SO2 thoát từ vật liệu làm tăng đáng kể phát thải. Một ví dụ khác là hàm "
      "lượng CO tăng trong quá trình vật liệu và khí nóng tiếp xúc ngược chiều, như lò quay. Kim loại "
      "nặng có thể đi vào vật liệu nung (xi măng, vôi) hoặc thoát vào khí thải (thủy tinh, luyện kim).",
      "During firing processes substances from the treated material may be released into the "
      "“firing” gas and thus increase the emission rate of the flue gas. In some cases, however, "
      "components including pollutants may be transferred from the gas into either the production "
      "material or into substances (e.g. slag) especially provided for this purpose. An example "
      "is the cement or lime industry where the sulfur of the fuel is transferred as SO2 to the "
      "product instead of being released to the atmosphere. Inversely during glass or brick "
      "production SO2 will escape from the material and increase the level of emission "
      "considerably. Another example is an increased CO content in processes where material and "
      "hot gases are in contact in counter-current, e.g. in rotating kilns. Heavy metals may be "
      "either integrated into the burnt material (cement, lime) or released from the material into "
      "the flue gas (glass or metal industry).")
    P("Bằng đo các thông số cháy, thiết kế lò, hướng ngọn lửa, nhiệt độ lò và cấp không khí cháy, "
      "có thể giảm phát thải do quá trình; máy phân tích khí di động cung cấp thông tin cần thiết.",
      "By measuring combustion parameters furnace design, flame guidance, furnace temperature and "
      "combustion air supply, the emissions caused by the process can be reduced. For that "
      "portable gas analyzers provide the necessary information.")
    H("7.4.2.2 Lò công nghiệp", "7.4.2.2 Industrial Furnaces", h4)
    P("Lò công nghiệp dùng để sản xuất hơi và nước nóng hoặc đốt nóng vật liệu dẫn nhiệt khác; cũng "
      "gồm lò dùng chuyển đổi vật liệu như ở nhà máy lọc dầu hoặc lò coke. Công suất thường ở dải "
      "MW. Phân tích cháy trong ứng dụng này nhằm tối ưu cháy, kiểm soát thiết bị làm sạch khí thải "
      "và giám sát phát thải chất ô nhiễm.",
      "Industrial furnaces are used to produce steam and hot water or to heat up other heat "
      "carrier materials. Industrial furnaces also include those that are used for material "
      "conversion e.g. in refineries or coke oven plants. Heat output of industrial furnaces "
      "normally is in the MW range. Combustion analysis in this application are for combustion "
      "optimization, control of flue gas cleaning installation and monitoring of the pollutant "
      "emissions.")
    H("7.4.2.3 Xử lý bề mặt nhiệt hóa học", "7.4.2.3 Thermochemical Surface Treatment", h4)
    P("Xử lý bề mặt nhiệt hóa học là quy trình gia nhiệt nhằm biến đổi tính chất bề mặt của chi tiết "
      "hoặc phôi bằng khuếch tán: vật tiếp xúc bầu khí nóng, nguyên tố khuếch tán từ khí vào hoặc ra "
      "khỏi vật liệu. Bao gồm tôi thép hoặc sấy lớp sơn, vecni trong công nghiệp gốm. Quá trình đặc "
      "trưng bởi loại và nồng độ nguyên tố (nitơ cho thấm nitơ, crom cho mạ crom) và nhiệt độ "
      "(400–1400 °C). Lò có nhiều thiết kế cho chạy liên tục hoặc theo mẻ. Phân tích khí giúp tối "
      "ưu vận hành (giảm chi phí, an toàn) và kiểm soát bầu khí riêng của quá trình (chất lượng sản "
      "phẩm kể cả tài liệu theo ISO 9000 ff.). Thành phần đo phổ biến nhất là O2, CO, CO2 và SO2.",
      "Thermochemical surface treatment is a heating procedure with the objective to modify the "
      "property of the surface of parts or work pieces etc. by means of diffusion processes. The "
      "parts are exposed to a hot gas atmosphere with certain elements diffusing from the gas into "
      "or out of the material. This includes steel hardening or the process of stoving colors or "
      "lacquer in the ceramic industry. Thermochemical processes are characterized by species and "
      "concentration of the used elements (e.g. nitrogen for nitrating, chrome for chrome plating) "
      "and process temperatures (400 up to 1400 °C). Furnaces are available in very different "
      "design for continuous flow or batch operation. Gas analysis is used to achieve optimum "
      "plant operation (cost reduction, safety) and for controlling the process-specific gas "
      "atmosphere (product quality including documentation according to ISO 9000 ff.). The most "
      "common measuring components are O2, CO, CO2 and SO2")
    H("7.4.2.4 Đo an toàn", "7.4.2.4 Safety Measurements", h4)
    P("Ứng dụng của phân tích khí còn gồm đo để bảo vệ người và nhà máy khỏi khí dễ cháy, nổ hoặc "
      "độc. Giám sát CO là mối quan tâm chính trong bầu khí nhà máy, trong xưởng nghiền than hoặc "
      "silô bột than (phát hiện sớm cháy âm ỉ) hoặc cùng lọc tĩnh điện để tránh tạo hỗn hợp khí nổ "
      "trong bộ lọc. Tương tự là giám sát nồng độ nguy hiểm của mêtan hoặc khí nổ khác.",
      "Process applications of gas analysis also include measuring tasks which are performed to "
      "protect persons and plants from combustible, explosive or toxic gases. Monitoring CO is the "
      "main concern in plant atmospheres, in coal mills or coal powder silos (to detect "
      "smouldering fire in time) or, in connection with the use of electrostatic filters, to avoid "
      "the formation of explosive gas mixtures in the filter. Similar applications are monitoring "
      "of plants for dangerous concentrations of methane or other explosive gases.")
    TBL([C.T("Chất cháy", "Combustible substances", lang),
         C.T("Công thức", "Formula", lang),
         C.T("Giới hạn cháy trong không khí (Vol. %), thấp — T=20 °C, p=1 bar",
             "Ignition limits in air (Vol. %), low — T=20 °C, p=1 bar", lang),
         C.T("Giới hạn cháy trong không khí (Vol. %), cao — T=20 °C, p=1 bar",
             "Ignition limits in air (Vol. %), high — T=20 °C, p=1 bar", lang)],
        [
            ("Ammonia", "NH₃", "15,0", "28,0"),
            ("Carbon monoxide", "CO", "12,5", "74"),
            ("Hydrogen", "H₂", "4,0", "75,6"),
            ("Methane", "CH₄", "5,0", "15,0"),
            ("Propane", "C₃H₈", "2,1", "9,5"),
            ("Butane", "C₄H₁₀", "1,5", "8,5"),
            ("Acetylene", "C₂H₂", "1,5", "82,5"),
        ],
        C.T("Bảng 4: Giới hạn cháy của các khí dễ cháy",
           "Table 4: Ignition limits of combustible gases", lang))
    P("Trong phân tích khí thường dùng cảm biến chuyên biệt để xác định chất cháy trong hỗn hợp; "
      "tuy cảm biến chỉ phát hiện tổng của mọi thành phần cháy. Vì vậy khi giám sát hỗn hợp theo "
      "giới hạn cháy dưới, khoảng đo của máy phải chỉnh theo thành phần có giới hạn cháy thấp nhất.",
      "A special measuring sensor is typically used in gas analysis to determine combustibles in "
      "gas mixtures. However, this sensor only detects the sum of all combustible components. "
      "Therefore, when monitoring a gas mixture for its lower ignition limit, the measuring range "
      "of the analyzer should be adjusted according to the combustible component with the lowest "
      "ignition limit.")

    # ---------------------------------------------------------------- 7.5
    H("7.5 Lò đốt nhiên liệu rắn", "7.5 Solid-Fuel-Fired Furnaces")
    H("7.5.1 Lò đốt nhiên liệu rắn", "7.5.1 Solid-Fuel-Fired Furnaces", h3)
    P("Lò đốt nhiên liệu rắn là một phần của nhà máy đốt để sinh nhiệt bằng cách đốt nhiên liệu rắn "
      "như than cứng, than nâu, gỗ... Nhiên liệu được nghiền hoặc xay rồi cấp vào đầu đốt. Quá trình "
      "cháy diễn ra trong buồng đốt trên giường cố định hoặc giường lưu hóa, hoặc trong hỗn hợp bụi "
      "nhiên liệu/không khí. Không khí cháy được cấp bằng quạt, đôi khi đã trộn với bột than.",
      "Solid-fuel-fired furnaces are part of firing plants to generate heat energy by burning "
      "solid fuels such as hard coal, brown coal, wood etc. The fuel is crushed or ground and then "
      "fed to the burner. Combustion occurs in a combustion chamber on a fixed or fluidized bed "
      "or in a fuel dust/air mixture. The combustion air is supplied through a fan, sometimes "
      "already mixed with powdered coal.")
    P("Ứng dụng của phân tích khí:", "Use of Gas Analysis:")
    U(["Chỉnh tối ưu các cấu phần của nhà máy", "Xác định cân bằng năng lượng",
       "Giám sát nồng độ phát thải để tuân thủ quy định"],
      ["Optimum adjustment of the plant components", "Determination of the energy balance",
       "Monitoring emission concentrations for compliance with regulations"])
    FIG(13, F.fig_f13())
    H("Vị trí điểm đo và nhiệm vụ phân tích", "Measuring Point Locations and Analysis Tasks", h4)
    U(["MP 1 tại cửa ra lò để chỉnh đầu đốt tối ưu (giảm chi phí nhiên liệu, tăng lợi nhuận), nhận "
       "diện các túi CO và bảo đảm độ tin cậy vận hành.",
       "MP 2 trong khí sạch tại ống khói để giám sát phát thải (tuân thủ quy định)."],
      ["MP 1 at the furnace outlet for optimum burner adjustment (reduced fuel costs, "
       "profitability), identification of CO pockets, reliability of plant operation",
       "MP 2 in the clean gas at the stack for emission monitoring (compliance with regulations)"])
    TBL([C.T("Thành phần đo", "Measured component", lang),
         C.T("Giá trị điển hình MP 1", "Typical values MP 1", lang),
         C.T("Giá trị giới hạn MP 2", "Limit values MP 2", lang)],
        [
            ("CO", "150 ... 170 mg/m³", "250 mg/m³"),
            ("NO", "", "-"),
            ("NO₂", "", "-"),
            (C.T("NOₓ (dưới dạng NO₂)", "NOₓ (as NO₂)", lang), "650 ... 750 mg/m³",
             "200 mg/m³ (>300 MW)\n400 mg/m³ (50-300 MW)"),
            ("SO₂", "25 ... 35 mg/m³",
             "400 mg/m³ (>300 MW)\n2000 mg/m³ (100-300 MW)"),
            ("O₂", "7%",
             "5% (slag tap furnace)\n6% (dry furnace)\n7% (fluidized bed furnace)"),
            ("Humidity", "", "-"),
            ("Gas flow", "", "-"),
            ("Flue gas temperature", "250 °C", "-"),
        ],
        C.T("Bảng 5: Giá trị điển hình và giới hạn của nhà máy đốt nhiên liệu rắn",
           "Table 5: Typical and limit values of a solid fuel firing plant", lang))

    H("7.5.2 Lò đốt khí", "7.5.2 Gas-fired Furnaces", h3)
    P("Lò đốt khí là một phần của nhà máy đốt sinh nhiệt bằng nhiên liệu khí như khí tự nhiên, khí "
      "công nghiệp, khí lò cao. Loại lò này cho quá trình cháy gần như không phát thải và không cặn. "
      "Cấp nhiên liệu và không khí cháy qua cửa gió hoặc, ở nhà máy lớn, đầu đốt áp suất cao.",
      "Gas-fired furnaces are part of firing plants to generate heat energy by burning gaseous "
      "fuel such as natural gas, industrial gas, blast furnace gas e.a. Such furnaces provide a "
      "combustion that is almost free of emissions and residues. The supply of fuel and combustion "
      "air is done by vents or, in larger plants, by high pressure burners.")
    P("Ứng dụng của phân tích khí:", "Use of Gas Analysis:")
    U(["Chỉnh tối ưu các cấu phần của nhà máy", "Lập cân bằng năng lượng",
       "Giám sát nồng độ phát thải để tuân thủ quy định"],
      ["Optimum adjustment of the plant components", "Provision of the energy balance",
       "Monitoring emission concentrations for compliance with regulations"])
    FIG(14, F.fig_f14())
    H("Vị trí điểm đo và nhiệm vụ phân tích", "Measuring Point Locations and Analysis Tasks", h4)
    U(["MP 1 tại cửa ra lò để chỉnh đầu đốt tối ưu (giảm chi phí nhiên liệu, tăng lợi nhuận).",
       "MP 2 trong khí sạch tại ống khói để giám sát phát thải (tuân thủ quy định)."],
      ["MP 1 at the furnace outlet for optimum burner adjustment (reduced fuel costs, "
       "profitability)",
       "MP 2 in the clean gas at the stack for emission monitoring (compliance with regulations)"])
    TBL([C.T("Thành phần đo", "Measured component", lang),
         C.T("Giá trị điển hình MP 1", "Typical values MP 1", lang),
         C.T("Giá trị giới hạn MP 2", "Limit values MP 2", lang)],
        [
            ("CO", "0 ... 5 ppm", "100 mg/m³"),
            ("CO₂", "9 ... 11% (control value)", ""),
            ("NO", "30 ... 50 ppm", ""),
            ("NO₂", "0 ... 2 ppm", ""),
            ("NOₓ", "", "200 mg/m³"),
            ("SO₂", "", "5 mg/m³ (liquified gas)\n1700 mg/m³ (crude oil gas)"),
            ("O₂", "2 ... 3%", "3% (reference value)"),
            ("Flue gas temperature", "180 °C", ""),
        ],
        C.T("Bảng 6: Giá trị điển hình và giới hạn của nhà máy đốt khí",
           "Table 6: Typical and limit values of a gas fuelled firing plant", lang))

    H("7.5.3 Nhà máy turbine khí", "7.5.3 Gas Turbine Plants", h3)
    P("Turbine khí cố định ban đầu được phát triển làm động cơ máy bay và chủ yếu dùng dẫn máy "
      "phát điện. Hệ thống dùng phát điện phụ tải và thường cùng lò hơi phế nhiệt để sinh cả nhiệt. "
      "Thành phần khí thải rất giống lò đốt khí. Tại Đức khí thải phải tuân quy định TI Air về "
      "chất ô nhiễm. Ngoài khí tự nhiên còn dùng khí bãi rác hoặc khí sinh học.",
      "Stationary gas turbines were originally developed as air craft engines and are applied "
      "preferably to drive generators. Installations are used to generate peak load electrical "
      "power and often, together with a waste heat boiler, to generate also heat energy. The flue "
      "gas composition is very similar to that of gas fired furnaces. In Germany the flue gas "
      "must, regarding the content of pollutants, comply with the regulations of the TI Air. "
      "Besides natural gas also landfill gas or biogas is used as fuel.")
    P("Ứng dụng của phân tích khí:", "Use of Gas Analysis:")
    U(["Giám sát phát thải turbine để vận hành tối ưu",
       "Giám sát nồng độ phát thải để tuân thủ quy định"],
      ["Monitoring the turbine emission for optimum operation",
       "Monitoring emission concentrations for compliance with regulations"])
    FIG(15, F.fig_f15())
    H("Vị trí điểm đo và nhiệm vụ phân tích", "Measuring Point Locations and Analysis Tasks", h4)
    U(["MP 1 tại cửa ra turbine để giám sát phát thải (vận hành tối ưu).",
       "MP 2 tại ống khói để giám sát phát thải (tuân thủ quy định)."],
      ["MP 1 at the turbine oulet for monitoring the turbine emission (optimum operation)",
       "MP 2 at the stack for emission monitoring (compliance with regulations)"])
    TBL([C.T("Thành phần đo", "Measured component", lang),
         C.T("Giá trị điển hình MP 1", "Typical values MP 1", lang),
         C.T("Giá trị giới hạn MP 2", "Limit values MP 2", lang)],
        [
            ("O₂", "15 ... 18%", "15% (Reference value)"),
            ("NOₓ", "25 ... 60 ppm", "300 ... 350 mg/m³"),
            ("CO", "0 ... 30 ppm", "100 mg/m³"),
            ("CO₂", "", ""),
            ("Dust", "", ""),
            ("Flue gas temp.", "300 ... 400 °C", ""),
            ("Gas flow", "", ""),
            ("Humidity", "", ""),
        ],
        C.T("Bảng 7: Giá trị điển hình và giới hạn của nhà máy turbine khí",
           "Table 7: Typical and limit values of a gas turbine plant", lang))

    H("7.5.4 Lò đốt dầu", "7.5.4 Oil-fired Furnaces", h3)
    P("Lò đốt dầu là một phần của nhà máy đốt sinh nhiệt bằng dầu các chất lượng khác nhau. Nhiên "
      "liệu (dầu) và không khí cháy được đầu đốt phun vào buồng đốt dưới dạng hỗn hợp. Dầu cháy "
      "gần như không cặn và lượng bụi khí thải rất thấp.",
      "Oil-fired furnaces are part of firing plants that generate heat energy by burning oil of "
      "different quality. Fuel (oil) and combustion air are sprayed as a mixture into the "
      "combustion chamber by the burner. Oil is burned with almost no residues and the amount of "
      "flue dust is very low.")
    P("Ứng dụng của phân tích khí:", "Use of Gas Analysis:")
    U(["Chỉnh tối ưu các cấu phần của nhà máy", "Xác định cân bằng năng lượng",
       "Giám sát nồng độ phát thải để tuân thủ quy định"],
      ["Optimum adjustment of plant components", "Determination of energy balance",
       "Monitoring emission concentrations for compliance with regulations"])
    FIG(16, F.fig_f16())
    H("Vị trí điểm đo và nhiệm vụ phân tích", "Measuring Point Locations and Analysis Tasks", h4)
    U(["MP 1 tại cửa ra lò để chỉnh đầu đốt tối ưu (giảm chi phí, tăng lợi nhuận) và lập cân bằng "
       "năng lượng.",
       "MP 2 tại ống khói để giám sát phát thải (tuân thủ quy định)."],
      ["MP 1 at the furnace outlet for optimum burner adjustment (fuel cost reduction, "
       "profitability) and for energy balance determination",
       "MP 2 at the stack for emission monitoring (compliance with regulations)"])
    TBL([C.T("Thành phần đo", "Measured components", lang),
         C.T("Giá trị điển hình MP 1", "Typical values MP 1", lang),
         C.T("Giá trị giới hạn MP 2", "Limit values MP 2", lang)],
        [
            ("O₂", "2,5 ... 3,5%", "3%"),
            ("CO", "0 ... 5 ppm", "175 mg/m³"),
            ("CO₂", "13 ... 15%", "Control value"),
            ("NO", "50 ... 150 ppm", "-"),
            ("NO₂", "0 ... 5 ppm", "-"),
            (C.T("NOₓ (dưới dạng NO₂)", "NOₓ (as NO₂)", lang), "",
             "150 mg/m³ (>300 MW)\n300 mg/m³ (50-300 MW)"),
            ("SO₂", "50 ... 100 ppm",
             "400 mg/m³ (>300 MW)\n1700 mg/m³ (100-300 MW)"),
            ("Humidity", "", "-"),
            ("Gas flow", "", "-"),
            ("Flue gas temp.", "200 °C", "-"),
        ],
        C.T("Bảng 8: Giá trị điển hình và giới hạn của nhà máy đốt dầu",
           "Table 8: Typical and limit values of an oil-fired combustion plant", lang))

    H("7.5.5 Nhà máy điện than", "7.5.5 Coal-fired Power Station", h3)
    P("Nhà máy điện than thuộc nhóm nhà máy nhiệt điện sinh điện (dạng năng lượng thứ cấp) từ than "
      "làm nguồn năng lượng sơ cấp. Dùng cả than cứng và than nâu. Than được nghiền, sấy và xay trong "
      "máy xay; cùng không khí cháy đã gia nhiệt, bột than được phun vào lò và cháy ở khoảng 1000 °C. "
      "Lò được bao bởi máy phát hơi gồm hệ thống ống dày đặc có nước lò chảy qua; nước được đốt nóng "
      "tạo hơi tươi áp suất khoảng 200 bar để dẫn turbine. Khí thải thoát khỏi lò đi qua nhiều thiết "
      "bị rửa khí rồi thải qua ống khói. Hơi sau turbine được làm nguội thành nước và cấp lại vào "
      "hệ thống lò hơi.",
      "Coal-fired power stations belong to the group of thermal power stations that generate "
      "electricity (secondary energy form) from coal as primary energy source. Hard coal as well "
      "as brown coal are used as fuel. The coal is crushed, dried, and ground in a mill. Together "
      "with preheated combustion air the powdered coal is blasted into the furnace and burned at "
      "temperatures of appr. 1000 °C. The furnace is surrounded by the steam generator which "
      "comprises a tightly packed pipe system with boiler water flowing through. The water is "
      "heated up and thus fresh steam is generated with a pressure of appr. 200 bar to drive a "
      "turbine. The flue gases escape from the furnace, pass through different gas scrubbers and "
      "are released into the atmosphere through the stack. The steam, after leaving the turbine, "
      "is cooled down to water and recharged into the boiler system again.")
    P("Ứng dụng của phân tích khí:", "Use of Gas Analysis:")
    U(["Chỉnh tối ưu các cấu phần của nhà máy (giảm chi phí nhiên liệu, tăng lợi nhuận vận hành)",
       "Kiểm soát hiệu năng thiết bị làm sạch khí",
       "Giám sát nồng độ phát thải để tuân thủ quy định",
       "An toàn cho người và nhà máy (giám sát CO)"],
      ["Optimum adjustment of plant components (fuel cost reduction, profitability of the plant "
       "operation)", "Performance control of the gas cleaning units",
       "Monitoring emission concentrations for compliance with regulations",
       "Safety of personell and plant (CO monitoring)"])
    FIG(17, F.fig_f17())
    H("Vị trí điểm đo và nhiệm vụ phân tích", "Measuring Point Locations and Analysis Tasks", h4)
    U(["MP 1 tại lò để kiểm soát cháy ổn định và hệ số không khí, nhận diện ổ CO và bảo đảm vận hành "
       "tin cậy.",
       "MP 2 tại cửa ra lò để điều khiển và tối ưu cháy (tăng lợi nhuận).",
       "MP 3 tại thiết bị khử nitơ để kiểm soát hiệu năng.",
       "MP 4 tại ống khói để giám sát phát thải (tuân thủ quy định)."],
      ["MP 1 at the furnace for controlling constant combustion and air value, identification of "
       "CO nests and providing reliable operation",
       "MP 2 at the furnace outlet for combustion control and optimization (profitability)",
       "MP 3 at the denitrification plant for performance control",
       "MP 4 at the stack for emission monitoring (compliance with regulations)"])
    TBL([C.T("Thành phần đo", "Measured components", lang),
         C.T("Điển hình MP 1", "Typical values MP 1", lang),
         C.T("Điển hình MP 2", "Typical values MP 2", lang),
         C.T("Điển hình MP 3", "Typical values MP 3", lang),
         C.T("Giới hạn MP 4", "Limit values MP 4", lang)],
        [
            ("O₂", "5 ... 9%", "5 ... 9%", "", "5 ... 7%"),
            ("CO", "10 ... 5000 ppm", "10 ... 5000 ppm", "", "250 mg/m³"),
            ("CO₂", "", "15 ... 18%", "", ""),
            ("NOₓ", "", "500 ... 600 ppm", "", "200 mg/m³"),
            ("SO₂", "", "500 ... 2000 ppm", "", "400 mg/m³"),
            ("Dust", "", "2 ... 20 g/m³", "", "50 mg/m³"),
            ("Flue gas temp.", "ca. 1000 °C", "ca. 1000 °C", "", ""),
            ("Humidity", "", "10 ... 15%", "", ""),
        ],
        C.T("Bảng 9: Giá trị điển hình và giới hạn của nhà máy điện than",
           "Table 9: Typical and limit values of a coal-fired power station", lang))

    H("7.5.6 Nhà máy điện kết hợp nhiệt và điện",
      "7.5.6 Combined Heating and Power Stations", h3)
    P("Nhà máy điện kết hợp (block-type) là động cơ khí hoặc diesel cố định sản xuất điện và nhiệt "
      "đồng thời theo nguyên lý liên kết nhiệt/điện. Có thể lắp gần người tiêu dùng, phù hợp khu "
      "dân cư và tòa nhà công cộng. Máy phát do turbine khí hoặc động cơ đốt trong dẫn; nhiệt thu "
      "từ khí thải và nước làm mát. Ngoài dầu diesel, nhiên liệu ưu tiên là khí tự nhiên hoặc khí "
      "bãi rác; công suất 15 kW đến 30 MW.",
      "Combined heating and power stations (block-type power stations) are stationary gas or "
      "diesel engines that produce electricity and heat simultaneously in accordance with the "
      "principle of the heat/power link. They can easily be installed very close to a consumer "
      "and are suitable for use in residential premises and public buildings. Generators driven "
      "by gas turbines or combustion engines are used for electricity generation; the heat energy "
      "is gained be using the waste heat contained in the exhaust gas and the cooling water of the "
      "engines or turbines. Preferred fuel, besides diesel oil, is natural or landfill gas; the "
      "output of such a power station is in the range of 15 kW to 30 MW.")
    P("Ứng dụng của phân tích khí:", "Use of Gas Analysis:")
    U(["Chỉnh tối ưu động cơ dẫn (tiết kiệm nhiên liệu, giảm phát thải)",
       "Kiểm soát hiệu năng chất xúc tác",
       "Giám sát phát thải để tuân thủ quy định"],
      ["Optimum adjustment of the driving engine (Economic fuel consumption, emission reduction)",
       "Performance control of the catalyst",
       "Emission monitoring for compliance with regulations"])
    FIG(18, F.fig_f18())
    H("Vị trí điểm đo và nhiệm vụ phân tích", "Measuring Point Locations and Analysis Tasks", h4)
    U(["MP 1 giữa động cơ và chất xúc tác để chỉnh động cơ và kiểm soát hiệu suất xúc tác.",
       "MP 2 sau chất xúc tác để kiểm soát hiệu suất và giám sát phát thải (tuân thủ quy định)."],
      ["MP 1 between engine and catalyst for engine adjustment and catalyst efficiency control",
       "MP 2 behind the catalyst for catalyst efficiency control and emission monitoring "
       "(compliance with regulations)"])
    TBL([C.T("Thành phần đo", "Measured component", lang),
         C.T("MP 1 — khí tự nhiên", "MP 1 natural gas", lang),
         C.T("MP 1 — khí bãi rác", "MP 1 landfill gas", lang),
         C.T("MP 1 — dầu", "MP 1 oil", lang)],
        [
            ("O₂", "8%", "5 ... 6%", "8 ... 10%"),
            ("NO", "100 ... 300 ppm", "100 ... 500 ppm", "800 ... 1000 ppm"),
            ("NO₂", "30 ... 60 ppm", "90 ... 110 ppm", "10 ... 20ppm"),
            ("CO", "20 ... 40 ppm", "350 ... 450 ppm", "450 ... 550 ppm"),
            ("CO₂", "10%", "13%", "7 ... 8%"),
            ("SO₂", "", "30 ppm", "30 ... 50 ppm"),
        ],
        C.T("Bảng 10: Giá trị điển hình tại MP 1 của nhà máy điện block-type",
           "Table 10: Typical values for a block-type power station at MP 1", lang))
    TBL([C.T("Thành phần đo", "Measured component", lang),
         C.T("Loại động cơ", "Type of engine", lang),
         C.T("Giới hạn MP 2", "MP 2 Limit values", lang)],
        [
            ("CO", "Natural gas", "650 mg/m³"),
            ("NO+NO₂", "Diesel engine <3 MW", "4000 mg/m³"),
            ("NO+NO₂", "Diesel engine >3 MW", "2000 mg/m³"),
            ("NO+NO₂", "Other 4-cycles", "500 mg/m³"),
            ("NO+NO₂", "Other 4-cycles", "800 mg/m³"),
            ("O₂", "Reference value", "5 Vol.%"),
            ("SO₂", "According to DIN 51603", ""),
        ],
        C.T("Bảng 11: Giới hạn của động cơ nhà máy điện kết hợp (MP 2)",
           "Table 11: Limit values for combined power station engines (MP 2)", lang))

    H("7.5.7 Nhà máy điện khí và hơi kết hợp",
      "7.5.7 Combined Gas and Steam Power Station", h3)
    P("Ở nhà máy điện khí và hơi kết hợp, nhiên liệu hóa thạch được đốt với hiệu suất cao và phát "
      "thải thấp nhờ kết hợp tối ưu turbine khí và turbine hơi trong một hệ thống. Có nhiều cách "
      "kết hợp: thường turbine khí chạy bằng khí tự nhiên hoặc dầu, khí thải nóng tạo hơi áp suất "
      "cao dẫn turbine hơi; trong trường hợp khác khí thải từ lò than áp lực dẫn turbine khí.",
      "In combined gas and steam power stations fossil fuels are burned (for electricity "
      "generation) with high efficiency and low emission level by an optimum combination of gas "
      "and steam turbines in one plant. Different combinations are in use; very often a gas "
      "turbine is operated primarily with natural gas or fuel oil, the hot exhaust gases generate "
      "high pressure steam for driving a steam turbine. In other cases the exhaust gases of a "
      "pressure-loaded coal firing plant drives a gas turbine.")
    P("Ứng dụng của phân tích khí:", "Use of Gas Analysis:")
    U(["Chỉnh đầu đốt tối ưu (giảm chi phí nhiên liệu và phát thải)",
       "Giám sát phát thải (tuân thủ quy định)"],
      ["Optimum burner adjustment (Fuel cost and emission reduction)",
       "Emission monitoring (Compliance with regulations)"])
    FIG(19, F.fig_f19())
    P("Vị trí điểm đo và nhiệm vụ phân tích: MP 1 tại cửa ra đầu đốt để tối ưu cháy và phát thải; "
      "MP 2 tại ống khói để giám sát phát thải và tuân thủ quy định.",
      "Measuring Point Locations and Analysis Tasks: MP 1 at the burner outlet for combustion and "
      "emission optimization; MP 2 at the stack for emission monitoring (compliance with "
      "regulations).")

    # ---------------------------------------------------------------- refs
    b.append(refs(_REFS))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
