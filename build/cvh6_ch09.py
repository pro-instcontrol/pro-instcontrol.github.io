# -*- coding: utf-8 -*-
"""Book 7c, Chapter 9 - Standards and Approvals (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 192-209.
This is a standards reference chapter: control valve standards from API,
ASME, CEN, FCI, ISA, IEC, MSS and NACE; product approvals for hazardous
(classified) locations; the Class/Division and Zone classification systems,
equipment groups and subgroups, types and levels of protection and EPL;
temperature codes; nomenclature and marking examples; protection techniques
and enclosure ratings. Seven numbered figures are redrawn as vector tables
and diagrams in `cvh6fig9.py` and placed in numbered order at their logical
prose points.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import fig, h2, h3, h4, lead, note, p, ul
import cvh6fig9 as F9

PAGES_SRC = 18         # source printed pp. 192-209 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Standards and Approvals"
TITLE_VI = "Tiêu chuẩn và phê duyệt"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> standard — tiêu chuẩn · approval — phê duyệt · "
            "hazardous (classified) location — vị trí nguy hiểm (đã phân loại) · explosive gas "
            "atmosphere — khí quyển khí dễ nổ · explosive dust atmosphere — khí quyển bụi dễ nổ · "
            "ignition hazard assessment — đánh giá nguy cơ đánh lửa · approval agency — tổ chức "
            "phê duyệt · certification scheme — hệ thống chứng nhận · Class/Division System — hệ "
            "thống phân loại Class/Division · Zone System — hệ thống phân loại theo vùng · class — "
            "loại · division — khu vực · group — nhóm · equipment group — nhóm thiết bị · "
            "subgroup — nhóm con · type of protection — kiểu bảo vệ · level of protection — mức "
            "độ bảo vệ · EPL (Equipment Protection Level) — mức bảo vệ thiết bị · Ex i — an toàn "
            "nội tại · Ex d — vỏ chống cháy lan · Ex e — an toàn tăng cường · Ex n — loại n · "
            "Ex p — cấp áp bảo vệ · Ex t — vỏ chống bụi · temperature code — mã nhiệt độ · "
            "T code — mã T · maximum surface temperature — nhiệt độ bề mặt tối đa · "
            "intrinsically safe — an toàn nội tại · explosion-proof — chống nổ · flame-proof — "
            "chống cháy lan · non-incendive — không gây đánh lửa · dust ignition-proof — chống "
            "đánh lửa bụi · NEC — quy định điện quốc gia Hoa Kỳ · CEC — quy định điện Canada · "
            "ATEX — Chỉ thị thiết bị chống nổ của Liên minh Châu Âu · enclosure rating — xếp "
            "hạng vỏ bọc · IP code — mã bảo vệ xâm nhập · ingress — sự xâm nhập")
    return (
        "<b>Key terms in this chapter.</b> standard · approval · hazardous (classified) location · "
        "explosive gas atmosphere · explosive dust atmosphere · ignition hazard assessment · "
        "approval agency · certification scheme · Class/Division System · Zone System · class · "
        "division · group · equipment group · subgroup · type of protection · level of protection "
        "· EPL (Equipment Protection Level) · Ex i (intrinsic safety) · Ex d (flame-proof "
        "enclosure) · Ex e (increased safety) · Ex n (type n) · Ex p (pressurization) · Ex t "
        "(dust enclosure) · temperature code · T code · maximum surface temperature · "
        "intrinsically safe · explosion-proof · flame-proof · non-incendive · dust ignition-proof "
        "· NEC (National Electric Code) · CEC (Canadian Electric Code) · ATEX Directive · "
        "enclosure rating · IP code · ingress")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Trên cùng một trang in 202, Hình 9.2 và Hình 9.3 có "
            "<i>chú thích giống hệt nhau</i>: «Zones vs. Equipment Protection Levels». Ở đây cả hai "
            "chú thích đều giữ nguyên cụm từ gốc nhưng bổ sung câu phân biệt (bảng ánh xạ vùng - EPL "
            "so với sơ đồ tần suất - EPL) và ghi rõ sự trùng lặp. (2) Hình 9.1 in các dòng nhóm bụi "
            "là «IIC, IIB, IIA» y hệt các dòng nhóm khí, dù văn bản mục 9.3.4.2 mô tả nhóm con bụi "
            "là IIIA, IIIB, IIIC; ở đây giữ nguyên chữ in. (3) Các nhãn EPL trong Hình 9.3 bị OCR "
            "xáo trộn thành «Ga Daa b c» kèm các chữ rời rạc «b», «c»; ở đây trình bày lại thành các "
            "cặp Gc/Dc, Gb/Db, Ga/Da. (4) Trong mục 9.1.6, mục «60534-4, Part 4: Inspection and "
            "routine testing» bị mất ký tự bullet trong bản dump; ở đây vẫn đưa vào danh sách như "
            "một mục bình thường. (5) Tiêu đề mục 9.1.7 trong nguồn là «Manufacturers "
            "Standardization Society (MSS)» và mục 9.2.1 là «Hazardous Location Approvals and "
            "Definitions»; ở đây giữ nguyên cách gọi đó. (6) Ký tự bullet của PDF bị OCR thành «» "
            "và đôi khi đứng lạc sau cùng một mục; ở đây thay bằng danh sách gạch đầu dòng bình "
            "thường. (7) Ở Hình 9.5, các ô nhóm lặp lại bị gộp trong bản dump và chú thích hình nằm "
            "xen giữa danh sách ví dụ đánh dấu; ở đây các ô được mở rộng và hình được đặt cuối mục "
            "9.5.4. Tại Hình 9.6, bốn dấu X của dòng «Corrosion» không căn cột rõ trong bản dump; "
            "chúng được đặt dưới các cột Type 3X, 3RX, 3SX và 4X. (8) Một số lỗi chính tả và ngữ "
            "pháp được giữ nguyên ở bản Anh và hiệu đính trong bản Việt: «subjected too», "
            "«damaged from external ice formation», «a open, short, or ground», «glisonite», "
            "«500um», «103 Ωm» (viết lại là 10³ Ω·m), «Division1» và «Class I,II,III». "
            "(9) Nguồn không có bảng dữ liệu hay phương trình nào nằm ngoài các hình; toàn bộ bảng "
            "trong chương là nội dung của Hình 9.1 đến Hình 9.7, nên ở đây không tạo bảng hay "
            "phương trình mới. (10) Hình trong bản in là bảng và bản vẽ; ở đây vẽ lại dạng vector "
            "dễ đọc, không phải hình gốc.")
    return (
        "<b>Source notes.</b> (1) On printed p. 202, Figures 9.2 and 9.3 carry the <i>identical</i> "
        "caption «Zones vs. Equipment Protection Levels». Both captions here retain that source "
        "wording but add a distinguishing clause (zone-to-EPL table versus frequency-to-EPL "
        "matrix) and state the duplication. (2) Figure 9.1 prints the dust rows as «IIC, IIB, "
        "IIA», exactly like the gas rows, although section 9.3.4.2 describes dust subgroups "
        "IIIA, IIIB and IIIC; the printed letters are kept. (3) The EPL labels of Figure 9.3 are "
        "jumbled by the OCR into «Ga Daa b c» with stray «b» and «c»; they are presented here as "
        "the pairs Gc/Dc, Gb/Db and Ga/Da. (4) In section 9.1.6 the entry «60534-4, Part 4: "
        "Inspection and routine testing» loses its bullet glyph in the dump; it is still listed "
        "as a normal entry. (5) The source heading of 9.1.7 reads «Manufacturers Standardization "
        "Society (MSS)» and that of 9.2.1 reads «Hazardous Location Approvals and Definitions»; "
        "that wording is retained. (6) The PDF bullet glyph is misread as «» and sometimes "
        "strands at the end of an entry; it is rendered here as a normal bulleted list. (7) In "
        "Figure 9.5 repeated group cells are collapsed in the dump and the caption is "
        "interspersed in the marking-example list; the cells are expanded here and the figure is "
        "placed at the end of section 9.5.4. In Figure 9.6 the four X marks of the «Corrosion» "
        "row have no clear column alignment in the dump; they are placed under the 3X, 3RX, 3SX "
        "and 4X columns. (8) Several spelling and grammar quirks are retained in English and "
        "corrected in Vietnamese: «subjected too», «damaged from external ice formation», "
        "«a open, short, or ground», «glisonite», «500um», «103 Ωm» (rendered as 10³ Ω·m), "
        "«Division1» and «Class I,II,III». (9) The source has no data tables or equations outside "
        "the figures; every table in the chapter is the content of Figures 9.1 through 9.7, so "
        "no new table or equation is introduced here. (10) Figures are tables and line drawings "
        "in print; they are redrawn here as legible vectors, not the original images.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def B(v, e):
        b.append(ul(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn, lang))

    def N(v, e):
        b.append(note(v if vi else e))

    # ------------------------------------------------------------ lead
    b.append(lead(
        "Chương này là tài liệu tham khảo về các tiêu chuẩn áp dụng cho van điều khiển và về phê "
        "duyệt sản phẩm dùng ở vị trí nguy hiểm: hệ thống phân loại Class/Division và Zone, nhóm "
        "và nhóm con thiết bị, kiểu và mức độ bảo vệ, mức bảo vệ thiết bị (EPL), mã nhiệt độ, cách "
        "đặt tên và ví dụ đánh dấu, kỹ thuật bảo vệ và xếp hạng vỏ bọc."
        if vi else
        "This chapter is a reference on the standards applicable to control valves and on product "
        "approvals for hazardous locations: the Class/Division and Zone classification systems, "
        "equipment groups and subgroups, types and levels of protection, equipment protection "
        "levels (EPL), temperature codes, nomenclature and marking examples, protection "
        "techniques, and enclosure ratings."))
    N(note_terms("vi"), note_terms("en"))

    # ------------------------------------------------------------ 9.1
    H("9.1 Tiêu chuẩn van điều khiển", "9.1 Control Valve Standards")
    P("Nhiều tiêu chuẩn áp dụng cho van điều khiển. Các tiêu chuẩn quốc tế và toàn cầu ngày càng "
      "quan trọng đối với các công ty tham gia thị trường toàn cầu. Sau đây là danh sách các quy "
      "phạm và tiêu chuẩn đã hoặc sẽ có vai trò quan trọng trong thiết kế và ứng dụng van điều "
      "khiển.",
      "Numerous standards are applicable to control valves. International and global standards "
      "are becoming increasingly important for companies that participate in global markets. "
      "Following is a list of codes and standards that have been or will be important in the "
      "design and application of control valves.")

    H("9.1.1 Viện Dầu khí Hoa Kỳ (API)",
      "9.1.1 American Petroleum Institute (API)", h3)
    B([
        "Spec 6D, Quy định kỹ thuật van đường ống (van cổng, van cắm, van bi và van một chiều)",
        "598, Kiểm tra và thử nghiệm van",
        "607, Thử nghiệm cháy đối với van quay một phần có đế mềm",
        "609, Van bướm kiểu tai và kiểu kẹp",
    ], [
        "Spec 6D, Specification for Pipeline Valves (Gate, Plug, Ball, and Check Valves)",
        "598, Valve Inspection and Testing",
        "607, Fire Test for Soft-Seated Quarter-Turn Valves",
        "609, Lug- and Wafer-Type Butterfly Valves",
    ])

    H("9.1.2 Hiệp hội Kỹ sư Cơ khí Hoa Kỳ (ASME)",
      "9.1.2 American Society of Mechanical Engineers (ASME)", h3)
    B([
        "B16.1, Mặt bích ống gang và phụ kiện có mặt bích",
        "B16.4, Phụ kiện ren bằng gang xám",
        "B16.5, Mặt bích ống và phụ kiện có mặt bích (dùng cho thép, hợp kim gốc niken và các "
        "hợp kim khác)",
        "B16.10, Kích thước mặt đối mặt và đầu đối đầu của van (xem tiêu chuẩn ISA về kích "
        "thước của hầu hết van điều khiển)",
        "B16.24, Mặt bích ống hợp kim đồng và phụ kiện có mặt bích",
        "B16.25, Đầu hàn giáp mối",
        "B16.34, Van - có mặt bích, ren và đầu hàn",
        "B16.42, Mặt bích ống gang dẻo và phụ kiện có mặt bích",
        "B16.47, Mặt bích thép đường kính lớn (NPS 26 đến NPS 60)",
    ], [
        "B16.1, Cast Iron Pipe Flanges and Flanged Fittings",
        "B16.4, Gray Iron Threaded Fittings",
        "B16.5, Pipe Flanges and Flanged Fittings (for steel, nickel-based alloys, and other "
        "alloys)",
        "B16.10, Face-to-Face and End-to-End Dimensions of Valves (see ISA standards for "
        "dimensions for most control valves)",
        "B16.24, Cast Copper Alloy Pipe Flanges and Flanged Fittings",
        "B16.25, Butt Welded Ends",
        "B16.34, Valves - Flanged, Threaded, and Welding End",
        "B16.42, Ductile Iron Pipe Flanges and Flanged Fittings",
        "B16.47, Large Diameter Steel Flanges (NPS 26 through NPS 60)",
    ])

    H("9.1.3 Ủy ban Tiêu chuẩn hóa Châu Âu (CEN)",
      "9.1.3 European Committee for Standardization (CEN)", h3)

    H("9.1.3.1 Tiêu chuẩn van công nghiệp Châu Âu",
      "9.1.3.1 European Industrial Valve Standards", h4)
    B([
        "EN 19, Đánh dấu",
        "EN 558-1, Kích thước mặt đối mặt và tâm đối mặt của van kim loại dùng trong hệ thống "
        "ống có mặt bích - Phần 1: Van ký hiệu PN",
        "EN 558-2, Kích thước mặt đối mặt và tâm đối mặt của van kim loại dùng trong hệ thống "
        "ống có mặt bích - Phần 2: Van ký hiệu Class",
        "EN 593, Van bướm",
        "EN 736-1, Thuật ngữ - Phần 1: Định nghĩa các loại van",
        "EN 736-2, Thuật ngữ - Phần 2: Định nghĩa các bộ phận của van",
        "EN 736-3, Thuật ngữ - Phần 3: Định nghĩa thuật ngữ",
        "EN 1349, Van điều khiển công nghiệp",
        "EN 12266-1, Thử nghiệm van - Phần 1: Phép thử, quy trình thử và tiêu chí chấp nhận",
        "EN 12516-1, Độ bền thiết kế vỏ - Phần 1: Phương pháp lập bảng cho van thép",
        "EN 12516-2, Độ bền thiết kế vỏ - Phần 2: Phương pháp tính toán cho van thép",
        "EN 12516-3, Độ bền thiết kế vỏ - Phần 3: Phương pháp thử nghiệm",
        "EN 12627, Thiết kế đầu hàn giáp mối",
        "EN 12760, Thiết kế đầu hàn ổ cắm",
        "EN 12982, Kích thước đầu đối đầu của van có đầu hàn giáp mối",
    ], [
        "EN 19, Marking",
        "EN 558-1, Face-to-Face and Center-to-Face Dimensions of Metal Valves for Use in Flanged "
        "Pipe Systems - Part 1: PN-Designated Valves",
        "EN 558-2, Face-to-Face and Center-to-Face Dimensions of Metal Valves for Use in Flanged "
        "Pipe Systems - Part 2: Class-Designated Valves",
        "EN 593, Butterfly valves",
        "EN 736-1, Terminology - Part 1: Definition of Types of Valves",
        "EN 736-2, Terminology - Part 2: Definition of Components of Valves",
        "EN 736-3, Terminology - Part 3: Definition of Terms",
        "EN 1349, Industrial Process Control Valves",
        "EN 12266-1, Testing of Valves - Part 1: Tests, Test Procedures and Acceptance Criteria",
        "EN 12516-1, Shell Design Strength - Part 1: Tabulation Method for Steel Valves",
        "EN 12516-2, Shell Design Strength - Part 2: Calculation Method for Steel Valves",
        "EN 12516-3, Shell Design Strength - Part 3: Experimental Method",
        "EN 12627, Butt Weld-End Design",
        "EN 12760, Socket Weld-End Design",
        "EN 12982, End-to-End Dimensions for Butt Weld-End Valves",
    ])

    H("9.1.3.2 Tiêu chuẩn vật liệu Châu Âu",
      "9.1.3.2 European Material Standards", h4)
    B([
        "EN 10213-1, Điều kiện kỹ thuật giao hàng của thép đúc dùng cho áp lực - Phần 1: Quy định chung",
        "EN 10213-2, Điều kiện kỹ thuật giao hàng của thép đúc dùng cho áp lực - Phần 2: Mác thép "
        "dùng ở nhiệt độ phòng và nhiệt độ cao",
        "EN 10213-3, Điều kiện kỹ thuật giao hàng của thép đúc dùng cho áp lực - Phần 3: Mác thép "
        "dùng ở nhiệt độ thấp",
        "EN 10213-4, Điều kiện kỹ thuật giao hàng của thép đúc dùng cho áp lực - Phần 4: Mác thép "
        "austenit và austeno-ferit",
        "EN 10222-2, Điều kiện kỹ thuật giao hàng của thép rèn dùng cho áp lực - Phần 2: Thép "
        "ferit và martensit dùng ở nhiệt độ cao",
        "EN 10222-3, Điều kiện kỹ thuật giao hàng của thép rèn dùng cho áp lực - Phần 3: Thép "
        "nikel dùng ở nhiệt độ thấp",
        "EN 10222-4, Điều kiện kỹ thuật giao hàng của thép rèn dùng cho áp lực - Phần 4: Thép hạt mịn",
        "EN 10222-5, Điều kiện kỹ thuật giao hàng của thép rèn dùng cho áp lực - Phần 5: Thép "
        "austenit, martensit và austeno-ferit",
    ], [
        "EN 10213-1, Technical conditions of delivery of steel castings for pressure purposes - "
        "Part 1: General",
        "EN 10213-2, Technical conditions of delivery of steel castings for pressure purposes - "
        "Part 2: Steel grades for use at room temperature and elevated temperatures",
        "EN 10213-3, Technical conditions of delivery of steel castings for pressure purposes - "
        "Part 3: Steel grades for use at low temperatures",
        "EN 10213-4, Technical conditions of delivery of steel castings for pressure purposes - "
        "Part 4: Austenitic and austeno-ferritic steel grades",
        "EN 10222-2, Technical conditions of delivery of steel forgings for pressure purposes - "
        "Part 2: Ferritic and martensitic steels for use at elevated temperatures",
        "EN 10222-3, Technical conditions of delivery of steel forgings for pressure purposes - "
        "Part 3: Nickel steel for low temperature",
        "EN 10222-4, Technical conditions of delivery of steel forgings for pressure purposes - "
        "Part 4: Fine grain steel",
        "EN 10222-5, Technical conditions of delivery of steel forgings for pressure purposes - "
        "Part 5: Austenitic martensitic and austeno-ferritic stainless steel",
    ])

    H("9.1.3.3 Tiêu chuẩn mặt bích Châu Âu",
      "9.1.3.3 European Flange Standards", h4)
    B([
        "EN 1092-1, Phần 1: Mặt bích thép ký hiệu PN",
        "EN 1092-2, Phần 2: Mặt bích gang ký hiệu PN",
        "EN 1759-1, Phần 1: Mặt bích thép ký hiệu Class",
    ], [
        "EN 1092-1, Part 1: Steel flanges PN designated",
        "EN 1092-2, Part 2: Cast iron flanges PN designated",
        "EN 1759-1, Part 1: Steel flanges Class designated",
    ])

    H("9.1.4 Viện Kiểm soát Chất lưu (FCI)",
      "9.1.4 Fluid Controls Institute (FCI)", h3)
    B(["70-2, Độ rò rỉ đế van điều khiển"],
      ["70-2, Control Valve Seat Leakage"])

    H("9.1.5 Hiệp hội Thiết bị Đo lường Hoa Kỳ (ISA)",
      "9.1.5 Instrument Society of America (ISA)", h3)
    B([
        "S51.1, Thuật ngữ thiết bị đo quy trình",
        "75.01.01, Phương trình dòng chảy để tính cỡ van điều khiển",
        "75.02.01, Quy trình thử công suất van điều khiển",
        "75.05.01, Thuật ngữ",
        "75.07, Đo trong phòng thí nghiệm tiếng ồn khí động do van điều khiển sinh ra",
        "75.08.01, Kích thước mặt đối mặt của thân van điều khiển kiểu globe có mặt bích tích "
        "phân (Class ANSI 125, 150, 250, 300 và 600)",
        "75.08.02, Kích thước mặt đối mặt của van điều khiển không mặt bích (Class ANSI 150, 300 "
        "và 600)",
        "75.08.03, Kích thước mặt đối mặt của van điều khiển kiểu globe có đầu hàn ổ cắm và đầu "
        "ren (Class 150, 300, 600, 900, 1500 và 2500)",
        "75.08.04, Kích thước mặt đối mặt của van điều khiển kiểu globe có đầu hàn giáp mối "
        "(Class 4500)",
        "75.08.05, Kích thước mặt đối mặt của van điều khiển kiểu globe có đầu hàn giáp mối (Class "
        "ANSI 150, 300, 600, 900, 1500 và 2500)",
        "75.08.06, Kích thước mặt đối mặt của thân van điều khiển kiểu globe có mặt bích (Class "
        "ANSI 900, 1500 và 2500)",
        "75.08.07, Kích thước mặt đối mặt của van điều khiển kiểu globe có mặt bích rời (Class "
        "150, 300 và 600)",
        "75.08.08, Kích thước mặt đối tâm của thân van điều khiển góc kiểu globe có mặt bích "
        "(Class 150, 300 và 600)",
        "75.08.09, Kích thước mặt đối mặt của van điều khiển không mặt bích có thân trượt (Class "
        "150, 300 và 600)",
        "75.11.01, Đặc tính lưu lượng vốn có và khả năng điều chỉnh của van điều khiển",
        "75.13.01, Phương pháp đánh giá hiệu năng của bộ định vị với tín hiệu đầu vào tương tự",
        "75.17, Dự báo tiếng ồn khí động của van điều khiển",
        "75.19.01, Thử áp lực thủy van điều khiển",
        "75.26.01, Thu thập và báo cáo dữ liệu chẩn đoán van điều khiển",
        "RP75.23, Cân nhắc khi đánh giá hiện tượng xâm thực trong van điều khiển",
    ], [
        "S51.1, Process Instrumentation Terminology",
        "75.01.01, Flow Equations for Sizing Control Valves",
        "75.02.01, Control Valve Capacity Test Procedures",
        "75.05.01, Terminology",
        "75.07, Laboratory Measurement of Aerodynamic Noise Generated by Control Valves",
        "75.08.01, Face-to-Face Dimensions for Integral Flanged Globe-Style Control Valve Bodies "
        "(ANSI Classes 125, 150, 250, 300, and 600)",
        "75.08.02, Face-to-Face Dimensions for Flangeless Control Valves (ANSI Classes 150, 300, "
        "and 600)",
        "75.08.03, Face-to-Face Dimensions for Socket Weld End and Screwed-End Globe-Style Control "
        "Valves (Classes 150, 300, 600, 900, 1500, and 2500)",
        "75.08.04, Face-to-Face Dimensions for Butt Weld-End Globe-Style Control Valves (Class 4500)",
        "75.08.05, Face-to-Face Dimensions for Butt Weld-End Globe-Style Control Valves (ANSI "
        "Classes 150, 300, 600, 900, 1500, and 2500)",
        "75.08.06, Face-to-Face Dimensions for Flanged Globe-Style Control Valve Bodies (ANSI "
        "Classes 900, 1500, and 2500)",
        "75.08.07, Face-to-Face Dimensions for Separable Flanged Globe-Style Control Valves "
        "(Classes 150, 300, and 600)",
        "75.08.08, Face-to-Centerline Dimensions for Flanged Globe-Style Angle Control Valve "
        "Bodies (Classes 150, 300, and 600)",
        "75.08.09, Face-to-Face Dimensions for Sliding-Stem Flangeless Control Valves (Classes "
        "150, 300, and 600)",
        "75.11.01, Inherent Flow Characteristic and Rangeability of Control Valves",
        "75.13.01, Method of Evaluating the Performance of Positioners with Analog Input Signals",
        "75.17, Control Valve Aerodynamic Noise Prediction",
        "75.19.01, Hydrostatic Testing of Control Valves",
        "75.26.01, Control Valve Diagnostic Data Acquisition and Reporting",
        "RP75.23, Considerations for Evaluating Control Valve Cavitation",
    ])

    H("9.1.6 Ủy ban Điện kỹ thuật Quốc tế (IEC)",
      "9.1.6 International Electrotechnical Commission (IEC)", h3)
    P("Hầu hết tiêu chuẩn của Ủy ban Điện kỹ thuật Quốc tế (IEC) cho van điều khiển, trong đó có "
      "nhiều tiêu chuẩn dựa trên tiêu chuẩn ISA, đã được tái xuất bản thành tiêu chuẩn EN và dùng "
      "tiền tố EN. IEC khuyến khích các ủy ban quốc gia áp dụng các tiêu chuẩn này và rút bỏ các "
      "tiêu chuẩn quốc gia tương ứng. Các tiêu chuẩn IEC ngày càng được nhà sản xuất và bên mua "
      "sử dụng. Dưới đây là danh sách tiêu chuẩn IEC về van điều khiển công nghiệp (dãy 60534).",
      "The majority of International Electrotechnical Commission (IEC) standards for control "
      "valves, several of which are based on ISA standards, have been re-published as EN standards "
      "and utilize an EN prefix. The IEC encourages national committees to adopt them and to "
      "withdraw any corresponding national standards. IEC standards are increasingly being "
      "applied by manufacturers and purchasers. Below is a list of IEC industrial process control "
      "valve standards (60534 series).")
    B([
        "60534-1, Phần 1: Thuật ngữ van điều khiển và các cân nhắc chung",
        "60534-2-1, Phần 2: Lưu lượng - Mục một: Phương trình tính cỡ cho dòng chất lưu không nén "
        "được trong điều kiện lắp đặt",
        "60534-2-3, Phần 2-3: Lưu lượng - Mục ba: Quy trình thử nghiệm",
        "60534-2-4, Phần 2-4: Lưu lượng - Mục bốn: Đặc tính lưu lượng vốn có và khả năng điều chỉnh",
        "60534-4, Phần 4: Kiểm tra và thử nghiệm định kỳ",
        "60534-5, Phần 5: Đánh dấu",
        "60534-6-1, Phần 6: Chi tiết lắp đặt để gắn bộ định vị vào cơ cấu chấp hành van điều "
        "khiển - Mục 1: Lắp bộ định vị trên cơ cấu chấp hành tuyến tính",
        "60534-6-2, Phần 6-2: Chi tiết lắp đặt để gắn bộ định vị vào cơ cấu chấp hành van điều "
        "khiển - Mục 2: Lắp bộ định vị trên cơ cấu chấp hành quay",
        "60534-7, Phần 7: Bảng dữ liệu van điều khiển",
        "60534-8-1, Phần 8-1: Cân nhắc về tiếng ồn - Mục một: Đo tiếng ồn trong phòng thí nghiệm "
        "do dòng khí động chảy qua van điều khiển",
        "60534-8-2, Phần 8-2: Cân nhắc về tiếng ồn - Mục hai: Đo tiếng ồn trong phòng thí nghiệm "
        "do dòng chất lưu động lực chảy qua van điều khiển",
        "60534-8-3, Phần 8-3: Cân nhắc về tiếng ồn - Mục ba: Phương pháp dự báo tiếng ồn khí động "
        "của van điều khiển",
        "60534-8-4, Phần 8-4: Cân nhắc về tiếng ồn - Mục bốn: Dự báo tiếng ồn do dòng chất lưu "
        "động lực",
    ], [
        "60534-1, Part 1: Control valve terminology and general considerations",
        "60534-2-1, Part 2: Flow capacity - Section One: Sizing equations for incompressible fluid "
        "flow under installed conditions",
        "60534-2-3, Part 2-3: Flow capacity - Section Three: Test procedures",
        "60534-2-4, Part 2-4: Flow capacity - Section Four: Inherent flow characteristics and "
        "rangeability",
        "60534-4, Part 4: Inspection and routine testing",
        "60534-5, Part 5: Marking",
        "60534-6-1, Part 6: Mounting details for attachment of positioners to control valve "
        "actuators - Section 1: Positioner mounting on linear actuators",
        "60534-6-2, Part 6-2: Mounting details for attachment of positioners to control valve "
        "actuators - Section 2: Positioner mounting on rotary actuators",
        "60534-7, Part 7: Control valve data sheet",
        "60534-8-1, Part 8-1: Noise considerations - Section One: Laboratory measurement of noise "
        "generated by aerodynamic flow through control valves",
        "60534-8-2, Part 8-2: Noise considerations - Section Two: Laboratory measurement of noise "
        "generated by hydrodynamic flow through control valves",
        "60534-8-3, Part 8-3: Noise considerations - Section Three: Control valve aerodynamic "
        "noise prediction method",
        "60534-8-4, Part 8-4: Noise considerations - Section Four: Prediction of noise generated "
        "by hydrodynamic flow",
    ])

    H("9.1.7 Hiệp hội Tiêu chuẩn hóa Nhà sản xuất (MSS)",
      "9.1.7 Manufacturers Standardization Society (MSS)", h3)
    B([
        "SP-6, Bề mặt hoàn thiện tiêu chuẩn cho mặt tiếp xúc của mặt bích ống và mặt bích đầu nối "
        "của van và phụ kiện",
        "SP-25, Hệ thống đánh dấu tiêu chuẩn cho van, phụ kiện, mặt bích và khớp nối",
        "SP-44, Mặt bích ống thép đường ống",
        "SP-67, Van bướm",
        "SP-68, Van bướm áp suất cao có thiết kế lệch tâm",
        "SP-147, Tiêu chuẩn chất lượng cho thép đúc dùng trong van thép Class tiêu chuẩn",
    ], [
        "SP-6, Standard Finishes for Contact Faces of Pipe Flanges and Connecting End Flanges of "
        "Valves and Fittings",
        "SP-25, Standard Marking System for Valves, Fittings, Flanges and Unions",
        "SP-44, Steel Pipe Line Flanges",
        "SP-67, Butterfly Valves",
        "SP-68, High-Pressure Butterfly Valves with Offset Design",
        "SP-147, Quality Standard for Steel Castings used in Standard Class Steel Valves",
    ])

    H("9.1.8 NACE International",
      "9.1.8 NACE International", h3)
    B([
        "NACE MR0175/ISO 15156, Công nghiệp dầu khí và khí tự nhiên - Vật liệu dùng trong môi "
        "trường chứa H2S trong khai thác dầu và khí",
        "NACE MR0175-2002, Vật liệu kim loại chống nứt do ứng suất sunfua dùng cho thiết bị mỏ dầu",
        "NACE MR0103/ISO 17945, Công nghiệp dầu khí, hóa dầu và khí tự nhiên - Vật liệu kim loại "
        "chống nứt do ứng suất sunfua trong môi trường lọc dầu ăn mòn",
        "NACE MR0103, Vật liệu chống nứt do ứng suất sunfua trong môi trường lọc dầu ăn mòn",
        "NACE RP0472, Phương pháp và biện pháp ngăn ngừa nứt mối hàn thép cacbon trong quá trình "
        "vận hành trong môi trường lọc dầu ăn mòn",
    ], [
        "NACE MR0175/ISO 15156, Petroleum and Natural Gas Industries - Materials for Use in "
        "H2S-Containing Environments in Oil and Gas Production",
        "NACE MR0175-2002, Sulfide Stress Corrosion Cracking-Resistant Metallic Materials for Oil "
        "Field Equipment",
        "NACE MR0103/ISO 17945, Petroleum, Petrochemical and Natural Gas Industries - Metallic "
        "Materials Resistant to Sulfide Stress Cracking in Corrosive Petroleum Refining Environments",
        "NACE MR0103, Materials Resistant to Sulfide Stress Cracking in Corrosive Petroleum "
        "Refining Environments",
        "NACE RP0472, Methods and Controls to Prevent In-Service Environmental Cracking of Carbon "
        "Steel Weldments in Corrosive Petroleum Refining Environments",
    ])

    # ------------------------------------------------------------ 9.2
    H("9.2 Phê duyệt sản phẩm cho vị trí nguy hiểm (đã phân loại)",
      "9.2 Product Approvals for Hazardous (Classified) Locations")
    P("<b>Tuyên bố miễn trừ:</b> Thông tin trong các mục sau nhằm cung cấp cái nhìn tổng quát về "
      "phân loại khu vực nguy hiểm, các kiểu kỹ thuật bảo vệ liên quan và xếp hạng vỏ bọc. Thông "
      "tin này chỉ nhằm mục đích học tập và không được dùng thay cho bất kỳ nguồn hay tài liệu "
      "quản lý nào khác.",
      "<b>DISCLAIMER:</b> The information contained in the following sections is to provide a "
      "broad overview of hazardous area classifications, types of protection techniques involved, "
      "and enclosure ratings. This information is for educational purposes and should not be used "
      "in place of any other source or governing documents.")

    H("9.2.1 Phê duyệt và định nghĩa về vị trí nguy hiểm",
      "9.2.1 Hazardous Location Approvals and Definitions", h3)
    P("Bất cứ khi nào thiết bị van điều khiển, cả cơ khí lẫn điện, được dùng trong khí quyển khí "
      "dễ nổ hoặc khi có mặt khí quyển bụi dễ nổ, điều cần thiết là phải tiến hành đánh giá nguy cơ "
      "đánh lửa. Cuộc đánh giá này xác định các nguồn đánh lửa tiềm ẩn sẽ hiện diện hoặc hoạt động "
      "do thiết bị trong suốt vòng đời dự kiến của nó. Việc nắm rõ các nguồn đánh lửa này là tối "
      "quan trọng nhằm giảm thiểu rủi ro cháy nổ phát sinh từ chúng.",
      "Whenever control valve equipment, both mechanical and electrical, is to be used in an "
      "explosive gas atmosphere or in the presence of an explosive dust atmosphere, it is "
      "essential that an ignition hazard assessment be carried out. The assessment identifies the "
      "potential ignition sources that will be present or active by the equipment over its "
      "expected lifetime. Knowledge of these ignition sources is paramount in order to minimize "
      "the risk of an explosion or fire from them.")
    B([
        "<b>Khí quyển khí dễ nổ:</b> Hỗn hợp không khí, trong điều kiện khí quyển, với các chất "
        "dễ cháy ở dạng khí hoặc hơi, sau khi bị đánh lửa cho phép sự lan truyền tự duy trì.",
        "<b>Khí quyển bụi dễ nổ:</b> Hỗn hợp không khí, trong điều kiện khí quyển, với các chất "
        "dễ cháy ở dạng bụi, sợi hoặc mảnh bay, sau khi bị đánh lửa cho phép sự lan truyền tự duy trì.",
        "<b>Vị trí (hoặc khu vực) nguy hiểm:</b> Khu vực mà trong đó khí quyển khí dễ nổ hoặc khí "
        "quyển bụi dễ nổ (hoặc cả hai) được dự kiến hiện diện với số lượng đủ lớn đến mức cần các "
        "biện pháp phòng ngừa đặc biệt cho việc chế tạo, lắp đặt và sử dụng thiết bị.",
        "<b>Tổ chức phê duyệt:</b> Tổ chức, công ty hoặc cơ quan có thẩm quyền cấp, cho phép hoặc "
        "chứng nhận một số sự kiện nhất định, thường ở dạng giấy chứng nhận.",
        "<b>Hệ thống chứng nhận:</b> Nhóm hoặc sự đồng thuận của các tổ chức phê duyệt cùng thống "
        "nhất vận hành theo một hệ thống quy tắc và quy định chung. Ví dụ gồm Liên minh Châu Âu, "
        "Liên minh Kinh tế Á - Âu, Hệ thống IECEx, Tổ chức các Quốc gia Vịnh, v.v.",
    ], [
        "<b>Explosive Gas Atmosphere:</b> Mixture of air, under atmospheric conditions, of "
        "flammable substances in the form of a gas or vapor, which, after ignition permits "
        "self-sustaining propagation.",
        "<b>Explosive Dust Atmosphere:</b> Mixture of air, under atmospheric conditions, of "
        "flammable substances in the form of a dust, fiber, or flyings, which, after ignition "
        "permits self-sustaining propagation.",
        "<b>Hazardous Location (or area):</b> An area in which an explosive gas atmosphere or "
        "explosive dust atmosphere (or both) is expected to be present in sufficient quantities "
        "as to require special precautions for the construction, installation, and use of the "
        "equipment.",
        "<b>Approval Agency:</b> An organization, company, or bureau who has the authority to "
        "grant, authorize, or make an attestation to certain facts, usually in the form a "
        "certificate.",
        "<b>Certification Schemes:</b> A group or consensus of approval agencies who agree to "
        "operate under a unified system of rules and regulations. Examples include, the European "
        "Union, Eurasia Economic Union, IECEx Scheme, Gulf States Organization, etc.",
    ])

    # ------------------------------------------------------------ 9.3
    H("9.3 Hệ thống phân loại", "9.3 Classification Systems")
    P("Có hai hệ thống phân loại dùng để phân loại khu vực nguy hiểm: Hệ thống Class/Division và "
      "Hệ thống Zone. Hệ thống Class/Division thường được dùng ở Hoa Kỳ và Canada, tuy nhiên các "
      "công trình lắp đặt mới có thể dùng Hệ thống Zone. Các nơi còn lại trên thế giới nói chung "
      "dùng Hệ thống Zone.",
      "There are two classification systems used to classify hazardous areas, the "
      "Class/Division System and the Zone System. The Class/Division system is generally used in "
      "the United States and Canada, however new installations may use the Zone system. The rest "
      "of the world generally uses the Zone system.")

    H("9.3.1 Hệ thống Class/Division", "9.3.1 Class/Division System", h3)
    P("Theo Hệ thống Class/Division, vị trí (hoặc khu vực) nguy hiểm được phân loại theo class, "
      "division và group.",
      "Hazardous locations (or area) per the Class/Division System are classified according to "
      "the class, division, and group.")
    P("Class xác định bản chất chung của vật liệu nguy hiểm trong khí quyển xung quanh.",
      "Class: The class defines the general nature of the hazardous material in the surrounding "
      "atmosphere.")
    B([
        "Class I: Vị trí có khí hoặc hơi dễ cháy hiện diện hoặc có thể hiện diện trong không khí "
        "với số lượng đủ để tạo thành hỗn hợp nổ hoặc dễ đánh lửa.",
        "Class II: Vị trí nguy hiểm do có mặt bụi dễ cháy.",
        "Class III: Vị trí có thể có mặt sợi hoặc mảnh bay dễ đánh lửa, nhưng khó có thể lơ lửng "
        "trong không khí với số lượng đủ để tạo thành hỗn hợp dễ đánh lửa.",
    ], [
        "Class I: Locations in which flammable gases or vapors are, or may be, present in the air "
        "in quantities sufficient to produce explosive or ignitable mixtures.",
        "Class II: Locations that are hazardous because of the presence of combustible dusts.",
        "Class III: Locations in which easily ignitable fibers or flyings may be present, but not "
        "likely to be in suspension in air in sufficient quantities to produce ignitable mixtures.",
    ])
    P("Division xác định xác suất (khả năng) vật liệu nguy hiểm hiện diện ở nồng độ có thể đánh "
      "lửa trong khí quyển xung quanh.",
      "Division: The division defines the probability (likelihood) of hazardous material being "
      "present in an ignitable concentration in the surrounding atmosphere.")
    B([
        "Division I: Vị trí mà ở đó nồng độ dễ đánh lửa của vật liệu nguy hiểm tồn tại trong điều "
        "kiện vận hành bình thường (liên tục, gián đoạn hoặc theo chu kỳ) hoặc thường xuyên do "
        "sửa chữa, bảo trì hoặc do rò rỉ. Xác suất cao.",
        "Division 2: Vị trí được cho là nguy hiểm chỉ trong tình huống bất thường. Xác suất thấp.",
    ], [
        "Division I: Locations in which ignitable concentrations of the hazardous material exist "
        "under normal operating conditions (continuously, intermittently, or periodically) or "
        "frequently because of repair, maintenance operations, or because of leakage. A high "
        "probability.",
        "Division 2: Locations that are presumed to be hazardous only in an abnormal situation. "
        "A low probability.",
    ])
    P("Group xác định đặc tính nổ của hỗn hợp không khí với khí, hơi hoặc bụi của vật liệu cụ thể "
      "liên quan. Nhóm A, B, C và D áp dụng cho Class I, trong khi Nhóm E, F và G áp dụng cho "
      "Class II.",
      "Group: The group defines the explosive characteristic of the air mixtures of gases, "
      "vapors, or dust of the specific material involved. Groups A, B, C, and D apply to Class I "
      "whereas Groups E, F, and G apply to Class II.")
    B([
        "Nhóm A: Acetylene.",
        "Nhóm B: Khí quyển có giá trị khe hở an toàn thử nghiệm tối đa (MESG) nhỏ hơn hoặc bằng "
        "0,45 mm hoặc tỷ lệ dòng đánh lửa tối thiểu (tỷ lệ MIC) nhỏ hơn hoặc bằng 0,40. Ví dụ gồm "
        "hydro, butadiene, ethylene oxide, acrolein và khí formaldehyde.",
        "Nhóm C: Khí quyển có giá trị khe hở an toàn thử nghiệm (MESG) lớn hơn 0,45 mm nhưng nhỏ "
        "hơn hoặc bằng 0,75 mm hoặc tỷ lệ dòng đánh lửa tối thiểu (tỷ lệ MIC) lớn hơn 0,40 nhưng "
        "nhỏ hơn hoặc bằng 0,80. Ví dụ gồm ethylene, diethyl ether, methyl ether, propyl ether, "
        "nitromethane và hydrazine.",
        "Nhóm D: Khí quyển có giá trị khe hở an toàn thử nghiệm (MESG) lớn hơn 0,75 mm hoặc tỷ lệ "
        "dòng đánh lửa tối thiểu (tỷ lệ MIC) lớn hơn 0,80. Ví dụ gồm propane, khí tự nhiên, "
        "methane, ammonia, benzene, acetone và butane.",
        "Nhóm E: Khí quyển chứa bụi kim loại dễ cháy như nhôm, magie và các hợp kim thương mại của "
        "chúng.",
        "Nhóm F: Khí quyển chứa bụi cacbon dễ cháy có chứa 8% hoặc nhiều hơn chất bay hơi bị giữ "
        "lại, như bụi than đen, than hoặc coke.",
        "Nhóm G: Khí quyển chứa bụi dễ cháy không thuộc Nhóm E hoặc Nhóm F. Các loại bụi điển hình "
        "gồm bột mì, tinh bột, ngũ cốc, gỗ, nhựa và hóa chất.",
    ], [
        "Group A: Acetylene.",
        "Group B: Atmospheres whose maximum experimental safe gap (MESG) value is less than or "
        "equal to 0.45mm or a minimum igniting current ratio (MIC ratio) less than or equal to "
        "0.40. Examples include: hydrogen, butadiene, ethylene oxide, acrolein, and formaldehyde gas.",
        "Group C: Atmospheres whose experimental safe gap (MESG) value is greater than 0.45mm but "
        "less than or equal to 0.75mm or minimum igniting current ratio (MIC ratio) greater than "
        "0.40 but less than or equal to 0.80. Examples include: ethylene, diethyl ether, methyl "
        "ether, propyl ether, nitromethane, and hydrazine.",
        "Group D: Atmospheres whose experimental safe gap (MESG) value is greater than 0.75mm or a "
        "minimum igniting current ratio (MIC ratio) greater than 0.80. Examples include: propane, "
        "natural gas, methane, ammonia, benzene, acetone, and butane.",
        "Group E: Atmospheres containing combustible metallic dusts, such as aluminum, magnesium, "
        "and their commercial alloys.",
        "Group F: Atmospheres containing combustible carbonaceous dusts with 8% or more trapped "
        "volatiles, such as carbon black, coal, or coke dust.",
        "Group G: Atmospheres containing combustible dusts not included in Group E or Group F. "
        "Typical dusts include flour, starch, grain, wood, plastic, and chemicals.",
    ])
    P("Mọi thiết bị điện phải được thử nghiệm, đánh dấu và phê duyệt cho vị trí nguy hiểm cụ thể "
      "mà nó dự định sử dụng, ví dụ class, division và group trong Hệ thống Class/Division. Có "
      "những ngoại lệ cho quy định này, có thể tìm thấy trong các phương pháp đấu dây của Quy định "
      "Điện Quốc gia (NEC) hoặc Quy định Điện Canada (CEC).",
      "All electrical equipment must be tested, marked, and approved for the particular hazardous "
      "location it is intended to be used in, e.g. class, division, and group, in the "
      "Class/Division System. There are exceptions to this rule, which can be found in the wiring "
      "practices of the National Electric Code (NEC) or Canadian Electric Code (CEC).")

    H("9.3.2 Hệ thống Zone", "9.3.2 Zone System", h3)
    P("Theo Hệ thống Zone, vị trí nguy hiểm được phân loại theo tần suất xuất hiện và thời gian "
      "tồn tại của khí quyển nổ. Các Zone 0, 1 và 2 liên quan đến khí quyển khí dễ nổ, trong khi "
      "các Zone 20, 21 và 22 liên quan đến khí quyển bụi dễ nổ.",
      "Hazardous locations per the Zone System are classified according to the frequency of the "
      "occurrence and the duration of an explosive atmosphere. Zones 0, 1, and 2 pertain to "
      "explosive gas atmospheres, whereas Zones 20, 21, and 22 pertain to explosive dust "
      "atmospheres.")
    B([
        "Zone 0: Khí quyển khí dễ nổ hiện diện liên tục, hoặc trong thời gian dài, hoặc thường "
        "xuyên.",
        "Zone 1: Khí quyển khí dễ nổ có khả năng xuất hiện theo chu kỳ hoặc thỉnh thoảng trong "
        "vận hành bình thường.",
        "Zone 2: Khí quyển khí dễ nổ ít có khả năng xuất hiện trong vận hành bình thường, nhưng "
        "nếu có thì chỉ tồn tại trong thời gian ngắn.",
        "Zone 20: Khí quyển bụi dễ nổ hiện diện liên tục, hoặc trong thời gian dài, hoặc thường "
        "xuyên.",
        "Zone 21: Khí quyển bụi dễ nổ có khả năng xuất hiện theo chu kỳ hoặc thỉnh thoảng trong "
        "vận hành bình thường.",
        "Zone 22: Khí quyển bụi dễ nổ ít có khả năng xuất hiện trong vận hành bình thường, nhưng "
        "nếu có thì chỉ tồn tại trong thời gian ngắn.",
    ], [
        "Zone 0: An explosive gas atmosphere that is present continuously, or for long periods, "
        "or frequently.",
        "Zone 1: An explosive gas atmosphere that is likely to occur periodically or occasionally "
        "in normal operation.",
        "Zone 2: An explosive gas atmosphere that is not likely to occur in normal operation, but "
        "if does occur, it will exist for a short period only.",
        "Zone 20: An explosive dust atmosphere that is present continuously, or for long periods, "
        "or frequently.",
        "Zone 21: An explosive dust atmosphere that is likely to occur periodically or "
        "occasionally in normal operation.",
        "Zone 22: An explosive dust atmosphere that is not likely to occur in normal operation, "
        "but if does occur, it will exist for a short period only.",
    ])
    P("Cần lưu ý rằng việc gán số phân loại vùng chỉ giải quyết khả năng xuất hiện của môi "
      "trường nổ. Nó không quy định bản chất nổ hay đặc tính vật liệu của khí, hơi hoặc bụi cụ thể "
      "liên quan. Lý tưởng nhất là đặt mọi thiết bị bên ngoài các vùng này, nhưng điều đó không "
      "thực tế. Vì vậy, thiết bị dự định dùng trong các vùng này được thử nghiệm, đánh dấu và phê "
      "duyệt sao cho bản chất nổ và đặc tính vật liệu được xem xét đầy đủ. Điều này được thực hiện "
      "bằng cách chia thiết bị thành các nhóm, nhóm con, kiểu bảo vệ đã dùng, mức độ bảo vệ đã "
      "dùng, gán mức bảo vệ thiết bị (EPL) và mã nhiệt độ, được thảo luận tiếp theo.",
      "It is important to note that the assignment of a zone classification number only addresses "
      "the likelihood of an explosive environment. It does not specify the explosive nature or "
      "the material characteristics of the specific gas, vapors, or dusts involved. Ideally, all "
      "equipment would be placed outside of these zones, but that is not realistic. Thus equipment "
      "intended for use in these zones is tested, marked, and approved such that the explosive "
      "nature and material characteristics are fully considered. This is done by dividing the "
      "equipment into groups, subgroups, the type of protection used, the level of protection "
      "used, assignment of an equipment protection level (EPL), and a temperature code, discussed "
      "next.")

    H("9.3.3 Nhóm thiết bị", "9.3.3 Equipment Groups", h3)
    P("Thiết bị được xếp vào các nhóm sau theo các định nghĩa sau.",
      "Equipment is organized into the following groups according to the following definitions.")
    B([
        "Nhóm I: Thiết bị dự định dùng trong hầm lò có nguy cơ khí methane (firedamp).",
        "Nhóm II: Thiết bị dự định dùng trong khí quyển khí dễ nổ ngoài hầm lò.",
        "Nhóm III: Thiết bị dự định dùng trong khí quyển bụi dễ nổ.",
    ], [
        "Group I: Equipment that is intended for use in mines susceptible to firedamp.",
        "Group II: Equipment that is intended for use in explosive gas atmospheres other than "
        "mines.",
        "Group III: Equipment that is intended for use in explosive dust atmospheres.",
    ])

    H("9.3.4 Nhóm con thiết bị", "9.3.4 Equipment Subgroups", h3)
    P("Nhóm thiết bị I không có nhóm con. Chỉ Nhóm thiết bị II và Nhóm thiết bị III được chia nhỏ "
      "hơn theo bản chất nổ của khí quyển khí và khí quyển bụi tương ứng mà chúng dự định sử "
      "dụng. Sau số nhóm là chữ cái A, B hoặc C theo các định nghĩa dưới đây.",
      "Equipment Group I has no subgroup. Only equipment Group II and Group III are subdivided "
      "further according to the explosive nature of the gas atmosphere and dust atmospheres, "
      "respectively, for which it is intended to be used in. The group number is followed by "
      "either the letter A, B, or C according to the below definitions.")

    H("9.3.4.1 Nhóm II (thường gọi là “Nhóm khí”)",
      "9.3.4.1 Group II (Commonly referred to as the “Gas Group”)", h4)
    B([
        "IIA: Khí quyển có giá trị khe hở an toàn thử nghiệm (MESG) lớn hơn hoặc bằng 0,9 mm hoặc "
        "tỷ lệ dòng đánh lửa tối thiểu (tỷ lệ MIC) lớn hơn 0,80. Ví dụ gồm propane.",
        "IIB: Khí quyển có giá trị khe hở an toàn thử nghiệm (MESG) lớn hơn 0,5 mm nhưng nhỏ hơn "
        "0,9 mm hoặc tỷ lệ dòng đánh lửa tối thiểu (tỷ lệ MIC) lớn hơn hoặc bằng 0,45 nhưng nhỏ "
        "hơn hoặc bằng 0,80. Ví dụ gồm ethylene.",
        "IIC: Khí quyển có giá trị khe hở an toàn thử nghiệm (MESG) nhỏ hơn hoặc bằng 0,5 mm hoặc "
        "tỷ lệ dòng đánh lửa tối thiểu (tỷ lệ MIC) nhỏ hơn 0,45. Ví dụ gồm hydrogen.",
    ], [
        "IIA: Atmospheres whose experimental safe gap (MESG) value is greater than or equal to "
        "0.9mm or a minimum igniting current ratio (MIC ratio) greater than 0.80. Examples "
        "include: propane",
        "IIB: Atmospheres whose experimental safe gap (MESG) value is greater than 0.5mm but less "
        "than 0.9mm or a minimum igniting current ratio (MIC ratio) greater than or equal to 0.45 "
        "but less than or equal to 0.80. Examples include: ethylene",
        "IIC: Atmospheres whose experimental safe gap (MESG) value is less than or equal to 0.5mm "
        "or a minimum igniting current ratio (MIC ratio) less than 0.45. Examples include: hydrogen",
    ])

    H("9.3.4.2 Nhóm III (thường gọi là “Nhóm bụi”)",
      "9.3.4.2 Group III (Commonly referred to as the “Dust Group”)", h4)
    B([
        "IIIA: Khí quyển chứa mảnh bay hoặc sợi dễ cháy, gồm cả hạt rắn nói chung lớn hơn 500 µm "
        "theo kích thước danh nghĩa. Ví dụ gồm rayon, bông, sisal, jute, gai dầu và sợi cacao.",
        "IIIB: Khí quyển chứa bụi không dẫn điện có điện trở suất lớn hơn 10³ Ω·m. Ví dụ gồm nylon, "
        "bột mì, than gỗ hoạt tính, than, coke và glisonite.",
        "IIIC: Khí quyển chứa bụi dẫn điện có điện trở suất nhỏ hơn hoặc bằng 10³ Ω·m. Ví dụ gồm "
        "nhôm và magie.",
    ], [
        "IIIA: Atmospheres containing combustible flyings or fibers including solid particles that "
        "are generally greater than 500um in nominal size. Examples include: rayon, cotton, sisal, "
        "jute, hemp, cocoa fiber.",
        "IIIB: Atmospheres containing non-conductive dust whose electrical resistivity is greater "
        "than 103 Ωm. Examples include: nylon, wheat flour, charcoal (activated), coal, coke, "
        "glisonite",
        "IIIC: Atmospheres containing conductive dust whose electrical resistivity is less than "
        "or equal to 103 Ωm. Examples include: aluminum, magnesium",
    ])
    P("Thiết bị được đánh dấu IIB phù hợp cho các ứng dụng yêu cầu thiết bị Nhóm IIA. Tương tự, "
      "thiết bị được đánh dấu IIC phù hợp cho các ứng dụng yêu cầu thiết bị Nhóm IIB hoặc Nhóm "
      "IIA. Cũng vậy, thiết bị được đánh dấu IIIB phù hợp cho các ứng dụng yêu cầu thiết bị Nhóm "
      "IIIA. Tương tự, thiết bị được đánh dấu IIIC phù hợp cho các ứng dụng yêu cầu thiết bị Nhóm "
      "IIIB hoặc Nhóm IIIA. Xem Hình 9.1.",
      "Equipment marked as IIB is suitable for applications requiring Group IIA equipment. "
      "Similarly, equipment marked as IIC is suitable for applications requiring Group IIB or "
      "Group IIA equipment. Likewise, equipment marked as IIIB is suitable for applications "
      "requiring Group IIIA equipment. Similarly, equipment marked as IIIC is suitable for "
      "applications requiring Group IIIB or Group IIIA equipment. See Figure 9.1.")
    FIG(1, F9.fig_f9_01())

    H("9.3.5 Kiểu bảo vệ", "9.3.5 Type of Protection", h3)

    H("9.3.5.1 Thiết bị điện", "9.3.5.1 Electrical Equipment", h4)
    P("Có nhiều kỹ thuật và phương pháp có thể áp dụng cho thiết bị điện để tránh đánh lửa khí "
      "quyển nổ xung quanh. Gần như tất cả các kỹ thuật và phương pháp này đều được đặt tên cụ thể "
      "cùng với một chữ cái viết thường biểu thị kiểu bảo vệ của nó trên biển đánh dấu. Cần lưu ý "
      "là không phải kiểu bảo vệ nào cũng phù hợp cho cả khí quyển khí lẫn khí quyển bụi. Các kỹ "
      "thuật và phương pháp bảo vệ, theo tên và chữ cái được gán, cùng với khí quyển nổ mà chúng "
      "có thể dùng (ghi trong ngoặc) như sau:",
      "There are many techniques and methods which can be applied to electrical equipment in "
      "order to avoid ignition of the surrounding explosive atmosphere. Nearly all of these "
      "techniques and methods have been given a specific name along with a lower case letter "
      "which signify its type of protection in its marking plate. It is important to note that "
      "not all types of protections are suitable for both gas and dust atmospheres. The type of "
      "protection techniques and methods, by name and its assigned letter, along with which "
      "explosive atmosphere they can be used in (denoted in parenthesis) are as follows:")
    B([
        "<b>An toàn nội tại - Ex i (khí và bụi):</b> Kiểu bảo vệ dựa trên việc hạn chế năng lượng "
        "điện bên trong thiết bị và của dây dẫn liên kết tiếp xúc với khí quyển nổ (khí hoặc bụi) "
        "ở mức thấp hơn mức có thể gây đánh lửa do tia lửa hoặc do hiệu ứng nhiệt. Thiết bị được "
        "chế tạo sao cho các mạch không an toàn nội tại không ảnh hưởng xấu đến các mạch an toàn "
        "nội tại.",
        "<b>Vỏ chống cháy lan - Ex d (khí):</b> Kiểu bảo vệ trong đó các bộ phận có khả năng "
        "đánh lửa khí quyển khí dễ nổ được đặt trong một vỏ có khả năng chịu được áp suất phát "
        "sinh trong một vụ nổ bên trong hỗn hợp dễ nổ và ngăn không cho vụ nổ lan ra khí quyển "
        "khí dễ nổ bao quanh vỏ.",
        "<b>Đóng gói kín - Ex m (khí và bụi):</b> Kiểu bảo vệ trong đó các bộ phận có khả năng "
        "đánh lửa khí quyển nổ (khí hoặc bụi) do tia lửa hoặc nhiệt được bao kín trong một hợp "
        "chất hoặc vỏ phi kim khác có độ bám dính sao cho không thể đánh lửa khí quyển nổ trong "
        "điều kiện vận hành hoặc lắp đặt.",
        "<b>An toàn tăng cường - Ex e (khí):</b> Kiểu bảo vệ áp dụng cho thiết bị điện trong đó "
        "các biện pháp bổ sung được áp dụng nhằm tăng cường an toàn chống lại khả năng nhiệt độ "
        "quá cao và sự xuất hiện của hồ quang và tia lửa trong vận hành bình thường hoặc trong "
        "điều kiện bất thường quy định.",
        "<b>Loại n - Ex n (khí):</b> Kiểu bảo vệ áp dụng cho thiết bị điện sao cho trong vận hành "
        "bình thường và trong một số điều kiện bất thường quy định, thiết bị không có khả năng "
        "đánh lửa khí quyển khí dễ nổ xung quanh.",
        "<b>Cấp áp bảo vệ - Ex p (khí và bụi):</b> Kiểu bảo vệ ngăn ngừa sự xâm nhập của khí "
        "quyển nổ bên ngoài vào một vỏ bằng cách duy trì bên trong vỏ một khí bảo vệ có áp suất "
        "cao hơn áp suất khí quyển bên ngoài.",
        "<b>Nhúng dầu - Ex o (khí):</b> Kiểu bảo vệ trong đó thiết bị điện hoặc một phần thiết "
        "bị điện được nhúng trong chất lỏng bảo vệ sao cho khí quyển khí dễ nổ có thể hiện diện "
        "phía trên chất lỏng hoặc bên ngoài vỏ không bị đánh lửa.",
        "<b>Lấp đầy bột - Ex q (khí):</b> Kiểu bảo vệ trong đó các bộ phận có khả năng đánh lửa "
        "khí quyển khí dễ nổ được cố định tại vị trí và được bao quanh hoàn toàn bằng vật liệu "
        "lấp đầy để ngăn đánh lửa khí quyển khí dễ nổ bên ngoài.",
        "<b>Vỏ bọc - Ex t (bụi):</b> Kiểu bảo vệ trong đó mọi thiết bị điện được bảo vệ bằng một "
        "vỏ bọc để tránh đánh lửa lớp bụi hoặc đám bụi và hạn chế nhiệt độ bề mặt.",
        "<b>Bảo vệ đặc biệt - Ex s (khí và bụi):</b> Kiểu bảo vệ cho phép thiết kế một sản phẩm "
        "không thể tuân thủ đầy đủ các kiểu bảo vệ được công nhận khác, hoặc khi các tiêu chuẩn "
        "cho các kiểu bảo vệ được công nhận không bao quản các điều kiện vận hành yêu cầu.",
    ], [
        "<b>Intrinsic Safety - Ex i (gas and dust):</b> A type of protection based on the restriction "
        "of electrical energy within the equipment and of interconnecting wiring exposed to the "
        "explosive atmosphere (gas or dust) to a level below that which can cause ignition by "
        "either sparking or heating effects. Equipment is constructed so that the "
        "non-intrinsically-safe circuits cannot adversely affect the intrinsically-safe circuits.",
        "<b>Flame-Proof Enclosure - Ex d (gas):</b> A type of protection in which the parts capable "
        "of igniting an explosive gas atmosphere are provided with an enclosure which can "
        "withstand the pressure developed during an internal explosion of an explosive mixture and "
        "which prevents the transmission of the explosion to the explosive gas atmosphere "
        "surrounding the enclosure.",
        "<b>Encapsulation - Ex m (gas and dust):</b> A type of protection in which the parts capable "
        "of igniting an explosive atmosphere (gas or dust) by either sparking or heating are "
        "enclosed in a compound or other non-metallic enclosure with adhesion in such a way that "
        "the explosive atmosphere cannot be ignited under operating or installation conditions.",
        "<b>Increased Safety - Ex e (gas):</b> A type of protection applied to electrical equipment "
        "in which additional measures are applied so as to give increased security against the "
        "possibility of excessive temperatures and of the occurrence of arcs and sparks in normal "
        "service or under specified abnormal conditions.",
        "<b>Type n - Ex n (gas):</b> A type of protection applied to electrical equipment such "
        "that in normal operation and in certain specified abnormal conditions, it is not capable "
        "of igniting a surrounding explosive gas atmosphere.",
        "<b>Pressurization - Ex p (gas and dust):</b> A type of protection of guarding against the "
        "ingress of the external explosive atmosphere into an enclosure by maintaining a "
        "protective gas therein at a pressure above that of the external atmosphere.",
        "<b>Oil Immersion - Ex o (gas):</b> A type of protection in which the electrical equipment "
        "or parts of the electrical equipment are immersed in a protective liquid is such a way "
        "that an explosive gas atmosphere which may be above the liquid or outside the enclosure "
        "cannot be ignited.",
        "<b>Powder Filling - Ex q (gas):</b> A type of protection in which the parts capable of "
        "igniting an explosive gas atmosphere are fixed in position and completely surrounded by "
        "filling material to prevent ignition of an external explosive gas atmosphere.",
        "<b>Enclosure - Ex t (dust):</b> A type of protection whereby all electrical equipment is "
        "protected by an enclosure to avoid ignition of a dust layer or cloud and to limit surface "
        "temperatures.",
        "<b>Special Protection - Ex s (gas and dust):</b> A type of protection that allows for the "
        "design of a product that cannot comply in full with other recognized types of protection "
        "or where the standards for the recognized types of protection do not cover the required "
        "operating conditions.",
    ])

    H("9.3.5.2 Thiết bị không điện",
      "9.3.5.2 Non-Electrical Equipment", h4)
    P("Hầu hết thiết bị điện thường chứa các nguồn đánh lửa hiệu quả phải được xử lý bằng một "
      "trong các phương pháp bảo vệ đã mô tả ở trên. Tuy nhiên, điều này không đúng với hầu hết "
      "thiết bị cơ khí. Thực tế, vận hành bình thường của hầu hết thiết bị cơ khí trong các thông "
      "số thiết kế sẽ không dẫn đến đánh lửa khí quyển nổ. Trong các tình huống xét đến sự cố, "
      "nhiều thiết bị cơ khí có thể được thiết kế sao cho các sự cố đó không trở thành nguồn đánh "
      "lửa nhờ lựa chọn đúng các biện pháp kết cấu đã được kiểm chứng.",
      "Most electrical equipment often contains effective ignition sources that must be dealt "
      "with by one of the protection methods previously described. However, this is not true for "
      "most mechanical equipment. In fact, normal operation of most mechanical equipment within "
      "its design parameters will not lead to ignition of an explosive atmosphere. In situations "
      "where malfunctions are considered, much of the mechanical equipment can be designed such "
      "that these malfunctions do not become an ignition source by a proper choice of well-tried "
      "constructional measures.")
    P("Các biện pháp bảo vệ đánh lửa sau đây cho thiết bị không điện, theo tên và chữ cái được "
      "gán, đã được công nhận.",
      "The following types of ignition protection measures for non-electrical equipment, by name "
      "and its assigned letter, have been recognized.")
    B([
        "<b>Vỏ hạn chế dòng chảy - Ex fr:</b> Kiểu bảo vệ đánh lửa trong đó việc làm kín hiệu quả "
        "và các mối nối khớp chặt có thể giảm sự xâm nhập của khí quyển nổ để hình thành bên trong "
        "vỏ. Cần tính đến chênh lệch áp suất và thay đổi nhiệt độ.",
        "<b>Vỏ chống cháy lan - Ex d:</b> Kiểu bảo vệ đánh lửa trong đó các bộ phận có khả năng "
        "đánh lửa khí quyển khí dễ nổ được đặt trong một vỏ có khả năng chịu được áp suất phát "
        "sinh trong một vụ nổ bên trong hỗn hợp dễ nổ và ngăn không cho vụ nổ lan ra khí quyển "
        "khí dễ nổ bao quanh vỏ.",
        "<b>An toàn kết cấu - Ex c:</b> Kiểu bảo vệ đánh lửa trong đó các biện pháp kết cấu được "
        "áp dụng để phòng ngừa khả năng đánh lửa từ bề mặt nóng, tia lửa và nén đoạn nhiệt do các "
        "bộ phận chuyển động tạo ra, kể cả khi xảy ra sự cố.",
        "<b>Kiểm soát nguồn đánh lửa - Ex b:</b> Kiểu bảo vệ đánh lửa trong đó các cảm biến tích "
        "hợp phát hiện sớm một hoạt động của thiết bị có khả năng gây đánh lửa và vì vậy khởi "
        "động các biện pháp kiểm soát trước khi nguồn đánh lửa tiềm ẩn trở thành nguồn đánh lửa "
        "hiệu quả.",
        "<b>Cấp áp bảo vệ - Ex p:</b> Kiểu bảo vệ đánh lửa ngăn ngừa sự xâm nhập của khí quyển nổ "
        "bên ngoài vào một vỏ bằng cách duy trì bên trong vỏ một khí bảo vệ có áp suất cao hơn áp "
        "suất khí quyển bên ngoài.",
        "<b>Nhúng chất lỏng - Ex k:</b> Kiểu bảo vệ đánh lửa trong đó các nguồn đánh lửa được làm "
        "bất hoạt bằng cách nhúng trong chất lỏng hoặc bằng cách làm ẩm liên tục bằng một màng "
        "chất lỏng.",
    ], [
        "<b>Flow Restricting Enclosure - Ex fr:</b> A type of ignition protection where effective "
        "sealing and closely matched joints can reduce the ingress of the explosive atmosphere to "
        "form inside the enclosure. Pressure differentials and changes in temperature need to be "
        "taken into account.",
        "<b>Flame-Proof Enclosure - Ex d:</b> A type of ignition protection in which the parts "
        "capable of igniting an explosive gas atmosphere are provided with an enclosure which can "
        "withstand the pressure developed during an internal explosion of an explosive mixture and "
        "which prevents the transmission of the explosion to the explosive gas atmosphere "
        "surrounding the enclosure.",
        "<b>Constructional Safety - Ex c:</b> A type of ignition protection in which constructional "
        "measures are applied so as to protect against the possibility of ignition from hot "
        "surfaces, sparks, and adiabatic compression generated by moving parts, including "
        "malfunctions.",
        "<b>Control of Ignition Sources - Ex b:</b> A type of ignition protection whereby integral "
        "sensors detect an impending operation of the equipment likely to cause an ignition and "
        "therefore initiate control measures before a potential ignition source becomes an "
        "effective ignition source.",
        "<b>Pressurization - Ex p:</b> A type of ignition protection of guarding against the ingress "
        "of the external explosive atmosphere into an enclosure by maintaining a protective gas "
        "therein at a pressure above that of the external atmosphere.",
        "<b>Liquid Immersion - Ex k:</b> A type of ignition protection where ignition sources are "
        "rendered inactive by immersion in a liquid or by the constant moistening using a liquid "
        "film.",
    ])

    H("9.3.6 Mức độ bảo vệ", "9.3.6 Level of Protection", h3)
    P("Tùy theo kiểu bảo vệ đã dùng cho thiết bị, một chữ cái (hoặc chữ cái phụ) về mức độ bảo vệ "
      "là a, b, c hoặc không có chữ cái nào sẽ được gán. Chữ cái mức độ bảo vệ, nếu được gán, đứng "
      "ngay sau chữ cái kiểu bảo vệ và được gọi là mức độ bảo vệ của thiết bị cho kiểu bảo vệ cụ "
      "thể đang dùng. Chữ cái mức độ bảo vệ biểu thị khả năng thiết bị trở thành nguồn đánh lửa. "
      "Một lần nữa, cần nhấn mạnh rằng mức độ bảo vệ được gán (a, b, c hoặc không có) phụ thuộc "
      "hoàn toàn vào kiểu bảo vệ áp dụng cho thiết bị. Lý do là không phải kiểu bảo vệ nào cũng "
      "có thể đạt mức bảo vệ rất cao hoặc thậm chí cao, không trở thành nguồn đánh lửa trong các "
      "sự cố hiếm hoi hoặc dự kiến. Ngoài ra, mức độ bảo vệ được gán có liên hệ rất chặt chẽ với "
      "xếp hạng EPL tổng thể của thiết bị (thảo luận sau).",
      "Depending upon the type of protection employed by the equipment, a level of protection "
      "letter (or sub-letter) of either an a, b, c, or no letter at all will be assigned. The level "
      "of protection letter, if assigned, immediately follows the type of protection letter and "
      "is referred to as the equipment's level of protection for that specific type of protection "
      "being used. The level of protection letter denotes the likelihood of the equipment becoming "
      "a source of ignition. Again, it is important to emphasize that the level of protection (a, "
      "b, c, or none) assigned depends strictly upon the type of protection being applied to the "
      "equipment. The reason for this is because not all types of protection can be made to afford "
      "a very high or even a high level of protection which will not become a source of ignition "
      "in rare or expected malfunctions. Additionally, the level of protection assigned correlates "
      "very closely to the equipment's overall EPL rating (discussed later).")
    P("Dù không được định nghĩa rõ ràng, chữ cái mức độ bảo vệ có thể được hiểu chung như sau:",
      "Although not explicitly defined the level of protection letter can be generalized as "
      "follows:")
    B([
        "a: Mức độ bảo vệ rất cao.",
        "b: Mức độ bảo vệ cao.",
        "c hoặc không có chữ cái: Mức độ bảo vệ tăng cường.",
    ], [
        "a: A very high level of protection.",
        "b: A high level of protection.",
        "c or none: An enhanced level of protection.",
    ])
    P("Việc gán mức độ bảo vệ được phép cho từng kiểu bảo vệ của thiết bị điện như sau:",
      "The assignment of a level of protection allowed for a given type of protection for "
      "electrical equipment is as follows:")
    B([
        "Ex i - An toàn nội tại: Ex ia, Ex ib, Ex ic",
        "Ex d - Chống cháy lan: Ex da, Ex db, Ex dc",
        "Ex m - Đóng gói kín: Ex ma, Ex mb, Ex mc",
        "Ex e - An toàn tăng cường: Ex eb, Ex ec",
        "Ex n - Loại n: Không gán chữ cái mức độ bảo vệ cho kiểu bảo vệ này. Kiểu bảo vệ này chỉ "
        "phù hợp cho vị trí Zone 2",
        "Ex p - Cấp áp bảo vệ: Ex pxb, Ex pyb, Ex pzc",
        "Ex o - Nhúng dầu: Ex ob, Ex oc",
        "Ex q - Lấp đầy bột: Không gán chữ cái mức độ bảo vệ cho kiểu bảo vệ này. Kiểu bảo vệ này "
        "chỉ phù hợp cho vị trí Zone 1 và Zone 2",
        "Ex t - Vỏ chống bụi: Ex ta, Ex tb, Ex tc",
        "Ex s - Bảo vệ đặc biệt: Ex sa, Ex sb, Ex sc",
    ], [
        "Ex i - Intrinsic Safety: Ex ia, Ex ib, Ex ic",
        "Ex d - Flame-Proof: Ex da, Ex db, Ex dc",
        "Ex m - Encapsulation: Ex ma, Ex mb, Ex mc",
        "Ex e - Increased Safety: Ex eb, Ex ec",
        "Ex n - Type n: A level of protection letter is not assigned for this type of protection. "
        "This type of protection is only suitable for Zone 2 locations",
        "Ex p - Pressurization: Ex pxb, Ex pyb, Ex pzc",
        "Ex o - Oil Immersion: Ex ob, Ex oc",
        "Ex q - Powder Filling: A level of protection letter is not assigned for this type of "
        "protection. This type of protection is only suitable for Zone 1 and Zone 2 locations.",
        "Ex t - Dust Enclosure: Ex ta, Ex tb, Ex tc",
        "Ex s - Special Protection: Ex sa, Ex sb, Ex sc",
    ])

    H("9.3.7 Mức bảo vệ thiết bị (EPL)",
      "9.3.7 Equipment Protection Level (EPL)", h3)
    P("Xếp hạng EPL là sự gán cho thiết bị dựa trên khả năng trở thành nguồn đánh lửa của nó trong "
      "khí quyển khí dễ nổ hoặc khí quyển bụi dễ nổ, kể cả hầm lò.",
      "An EPL rating is an equipment assignment based upon its likelihood of becoming a source of "
      "ignition in either an explosive gas atmosphere or an explosive dust atmosphere, including "
      "mines.")
    B([
        "EPL Ma: Thiết bị lắp đặt trong hầm lò có nguy cơ khí firedamp, có mức độ bảo vệ rất cao, "
        "khó có thể trở thành nguồn đánh lửa trong vận hành bình thường, trong sự cố dự kiến hoặc "
        "trong sự cố hiếm hoi.",
        "EPL Mb: Thiết bị lắp đặt trong hầm lò có nguy cơ khí firedamp, có mức độ bảo vệ cao, khó "
        "có thể trở thành nguồn đánh lửa trong vận hành bình thường hoặc trong sự cố dự kiến.",
        "EPL Ga: Thiết bị dùng cho khí quyển khí dễ nổ, có mức độ bảo vệ rất cao, không phải là "
        "nguồn đánh lửa trong vận hành bình thường, trong sự cố dự kiến hoặc trong sự cố hiếm hoi.",
        "EPL Gb: Thiết bị dùng cho khí quyển khí dễ nổ, có mức độ bảo vệ cao, không phải là nguồn "
        "đánh lửa trong vận hành bình thường hoặc trong sự cố dự kiến.",
        "EPL Gc: Thiết bị dùng cho khí quyển khí dễ nổ, có mức độ bảo vệ tăng cường, không phải là "
        "nguồn đánh lửa trong vận hành bình thường và có thể có thêm một số bảo vệ để đảm bảo nó "
        "duy trì không hoạt động như một nguồn đánh lửa.",
        "EPL Da: Thiết bị dùng cho khí quyển bụi dễ nổ, có mức độ bảo vệ rất cao, không phải là "
        "nguồn đánh lửa trong vận hành bình thường, trong sự cố dự kiến hoặc trong sự cố hiếm hoi.",
        "EPL Db: Thiết bị dùng cho khí quyển bụi dễ nổ có mức độ bảo vệ cao, không phải là nguồn "
        "đánh lửa trong vận hành bình thường hoặc trong sự cố dự kiến.",
        "EPL Dc: Thiết bị dùng cho khí quyển bụi dễ nổ, có mức độ bảo vệ tăng cường, không phải là "
        "nguồn đánh lửa trong vận hành bình thường và có thể có thêm một số bảo vệ để đảm bảo nó "
        "duy trì không hoạt động như một nguồn đánh lửa.",
    ], [
        "EPL Ma: Equipment for installation in mines susceptible to firedamp, having a very high "
        "level of protection which is unlikely to become an ignition source in normal operation, "
        "during expected malfunctions, or during rare malfunctions.",
        "EPL Mb: Equipment for installation in mines susceptible to firedamp, having a high level "
        "of protection which is unlikely to become an ignition source in normal operation or "
        "during expected malfunctions.",
        "EPL Ga: Equipment for explosive gas atmospheres having a very high level of protection "
        "which is not a source of ignition in normal operation, during expected malfunctions, or "
        "during rare malfunctions.",
        "EPL Gb: Equipment for explosive gas atmospheres having a high level of protection which "
        "is not a source of ignition in normal operation or during expected malfunctions.",
        "EPL Gc: Equipment for explosive gas atmospheres having an enhanced level of protection "
        "which is not a source of ignition in normal operation and may have some additional "
        "protection to ensure that it remains inactive as an ignition source.",
        "EPL Da: Equipment for explosive dust atmospheres having a very high level of protection "
        "which is not a source of ignition in normal operation, during expected malfunctions, or "
        "during rare malfunctions.",
        "EPL Db: Equipment for explosive dust atmospheres have a high level of protection which is "
        "not a source of ignition in normal operation or during expected malfunctions.",
        "EPL Dc: Equipment for explosive dust atmospheres having an enhanced level of protection "
        "which is not a source of ignition in normal operation and may have some additional "
        "protection to ensure that it remains inactive as an ignition source.",
    ])
    P("Mối quan hệ mặc định giữa các vùng và mức bảo vệ thiết bị (EPL) được tóm tắt trong Hình 9.2 "
      "và Hình 9.3.",
      "The default relationship between zones and equipment protection levels (EPLs) can be "
      "summarized in the Figures 9.2 and 9.3.")
    FIG(2, F9.fig_f9_02())
    FIG(3, F9.fig_f9_03())

    # ------------------------------------------------------------ 9.4
    H("9.4 Mã nhiệt độ", "9.4 Temperature Code")
    P("Nếu khí quyển khí dễ nổ tiếp xúc với một bề mặt nóng đáng kể, khả năng đánh lửa rất dễ xảy "
      "ra ngay cả khi không có tia lửa hoặc ngọn lửa. Điều kiện để một bề mặt nóng đánh lửa khí "
      "quyển khí dễ nổ phụ thuộc vào diện tích bề mặt, nhiệt độ và nhóm khí cụ thể liên quan. Để "
      "thuận tiện cho việc phân loại và đánh dấu, các mã nhiệt độ được định nghĩa trong Hình 9.4.",
      "If an explosive gas atmosphere comes into contact with a significantly hot surface, an "
      "ignition is likely to take place in the absence of a spark or flame being present. The "
      "conditions under which a hot surface will ignite the explosive gas atmosphere depends on "
      "its surface area, temperature, and the specific gas group involved. For ease of "
      "classification and marking purposes, temperature codes are defined in Figure 9.4.")
    FIG(4, F9.fig_f9_04())
    P("Thiết bị đã được thử nghiệm sẽ nhận một mã nhiệt độ cho biết nhiệt độ bề mặt tối đa mà thiết "
      "bị đạt được. Bất kể hệ thống phân loại nào đang được dùng, nhiệt độ bề mặt tối đa có thể ở "
      "bên trong hoặc bên ngoài thiết bị, tùy thuộc vào kiểu bảo vệ được áp dụng.",
      "Equipment that has been tested receives a temperature code that indicates the maximum "
      "surface temperature attained by the equipment. Regardless of which classification system "
      "is being used, the maximum surface temperature may be internal or external to the "
      "equipment which is determined by the type of protection being employed.")
    P("Khí quyển bụi dễ nổ có đặc tính rất khác khí quyển khí, tuy nhiên chúng cũng có thể bị đánh "
      "lửa bởi bề mặt nóng. Các ràng buộc bổ sung đối với sự đánh lửa của khí quyển bụi dễ nổ gồm "
      "nhưng không giới hạn ở nồng độ bụi trong khí quyển, sự phân tán bụi, độ dày của lớp bụi, "
      "v.v. Thiết bị dùng cho khí quyển bụi dễ nổ được đánh dấu nhiệt độ bề mặt tối đa trên biển "
      "đánh dấu chứ không dùng mã nhiệt độ.",
      "Explosive dust atmospheres have very different characteristics than gas atmospheres, "
      "however they can also be ignited by a hot surface. The additional constraints for ignition "
      "of an explosive dust atmosphere include, but are not limited to, the atmospheric dust "
      "concentration, dust dispersion, thickness of dust layers, etc. Equipment for explosive "
      "dust atmospheres are marked with the maximum surface temperature on its marking plate and "
      "not with a temperature code.")
    P("Đối với thiết bị điều khiển quá trình (như van), nhiệt độ bề mặt tối đa phụ thuộc rất nhiều "
      "vào chất lưu, nhiệt độ không khí môi trường, lựa chọn vật liệu chế tạo và hình học vật lý "
      "của thiết bị. Trong hầu hết trường hợp, chỉ người dùng cuối mới biết đúng điều kiện vận "
      "hành thực tế mà thiết bị phải chịu. Vì vậy, thiết bị như vậy được đánh dấu 'TX', báo cho "
      "người dùng cuối biết nhiệt độ bề mặt tối đa phụ thuộc vào điều kiện vận hành. Việc thêm "
      "nhiệt vào bất kỳ đường ống quy trình nào có thể dẫn vào khí quyển nổ phải được cân nhắc "
      "và đánh giá cẩn thận.",
      "For process control equipment (such as valves), the maximum surface temperature greatly "
      "depends upon the fluid, the ambient air temperature, the choice of materials used in its "
      "construction, and its physical geometry. In most cases, only the end user will know the "
      "true operating conditions that the equipment will be subjected too. Therefore, such "
      "equipment is marked ‘TX’ which signifies to the end user that the maximum surface "
      "temperature of the equipment is dependent upon operating conditions. Adding heat to any "
      "process pipeline which could enter an explosive atmosphere must be carefully considered "
      "and evaluated.")

    # ------------------------------------------------------------ 9.5
    H("9.5 Cách đặt tên", "9.5 Nomenclature", h3)

    H("9.5.1 Hệ thống Class/Division",
      "9.5.1 Class/Division System", h4)
    P("Trong Hệ thống Class/Division, không có tên hay thuật ngữ chính thức để mô tả một xếp hạng "
      "class hoặc division nhất định. Tuy nhiên, ngành công nghiệp sử dụng rộng rãi các thuật ngữ "
      "sau để liên kết chúng với một xếp hạng class hoặc division cụ thể:",
      "In the Class/Division System there is no formal name or term used to describe a given class "
      "or division rating. However, the industry widely uses the following terms to associate "
      "them to a given class or division rating;")
    B([
        "Chống nổ - Class I Division 1",
        "Không gây đánh lửa - Class I Division 2",
        "Chống đánh lửa bụi - Class II Division 1",
        "Thiết bị IS (thiết bị an toàn nội tại) - Class I Division 1 hoặc Class I, II, III Division 1",
    ], [
        "Explosion-Proof - Class I Division 1",
        "Non-Incendive - Class I Division 2",
        "Dust Ignition-Proof - Class II Division 1",
        "IS Equipment (Intrinsically-Safe equipment) - Class I Division 1 or Class I, II, III "
        "Division 1",
    ])
    P("Thiết bị an toàn nội tại (hoặc apparatus) là thiết bị đặc biệt ở chỗ năng lượng bị giới "
      "hạn và có thể được phê duyệt chỉ cho khí quyển khí hoặc cho cả khí quyển khí lẫn bụi. Thiết "
      "bị an toàn nội tại luôn được đánh giá là thuộc vị trí Division 1.",
      "Intrinsically-safe equipment (or apparatus) is unique in that energy is limited and can be "
      "approved for just gas atmospheres or for both gas and dust atmospheres. Intrinsically-safe "
      "equipment is always evaluated as being in a Division 1 location.")

    H("9.5.2 Hệ thống Zone", "9.5.2 Zone System", h4)
    P("Trong Hệ thống Zone, một chữ cái viết thường biểu thị kiểu bảo vệ đã áp dụng cho thiết bị. "
      "Tên gọi liên kết với một kiểu bảo vệ nhất định được xác định rõ. Xem phần kiểu bảo vệ để "
      "có mô tả.",
      "In the Zone System, a lower case letter represents the type of protection that has been "
      "applied to the equipment. The name associated to a given type of protection is well "
      "defined. Refer to the type of protection for a description.")

    H("9.5.3 Phương pháp đấu dây", "9.5.3 Wiring Practices", h4)
    P("Không thể nhấn mạnh đủ rằng cả thiết bị lẫn phương pháp đấu dây liên quan trong quá trình "
      "lắp đặt đều then chốt trong việc phòng ngừa cháy nổ ở vị trí nguy hiểm. Các phương pháp "
      "đấu dây sau được sử dụng rộng rãi.",
      "It cannot be emphasized enough that both the equipment and its associated wiring practice "
      "during installation are critical in preventing explosions in hazardous locations. The "
      "following wiring practices are widely used.")
    B([
        "Quy định Điện Quốc gia (NEC) - Hoa Kỳ",
        "Các Điều 500 đến 504 đề cập đến các công trình lắp đặt dùng Hệ thống Class/Division",
        "Các Điều 505 đến 506 đề cập đến các công trình lắp đặt dùng Hệ thống Zone",
        "Quy định Điện Canada (CEC) - Canada",
        "Mục 18 đề cập đến các công trình lắp đặt dùng Hệ thống Zone",
        "Mục J đề cập đến các công trình lắp đặt dùng Hệ thống Class/Division",
        "IEC 60079-14 (Thiết kế, lựa chọn và lắp đặt hệ thống điện) - Toàn cầu",
        "Đề cập đến các công trình lắp đặt điện theo Hệ thống Zone",
    ], [
        "National Electric Code (NEC) - U.S.",
        "Articles 500 to 504 address installations that use the Class/Division System",
        "Articles 505 to 506 address installations that use the Zone System",
        "Canadian Electric Code (CEC) - Canada",
        "Section 18 address installations that use the Zone System",
        "Section J address installations use the Class/Division System",
        "IEC 60079-14 (Electrical installations design, selection, and erection) - Worldwide",
        "Addresses electrical installations per the Zone System",
    ])

    H("9.5.4 Liên minh Châu Âu (EU) - Chỉ thị ATEX 2014/34/EU",
      "9.5.4 European Union (EU) - ATEX Directive 2014/34/EU", h4)
    P("Theo Chỉ thị ATEX, chỉ tồn tại hai nhóm thiết bị, ba category thiết bị và hai môi trường "
      "khí quyển nổ.",
      "Per the ATEX Directive, there exist only two equipment groups, three equipment categories, "
      "and two explosive atmosphere environments.")
    P("<b>Nhóm:</b>", "<b>Group:</b>")
    B([
        "Nhóm I: Thiết bị dùng trong hầm lò ngầm có nguy cơ khí firedamp",
        "Nhóm II: Thiết bị dùng ở nơi khác ngoài hầm lò",
    ], [
        "Group I: Equipment for use in underground mines susceptible to firedamp",
        "Group II: Equipment for use in places other than mines",
    ])
    P("<b>Category:</b>", "<b>Category:</b>")
    B([
        "Category 1: Thiết bị được thiết kế để đảm bảo mức độ bảo vệ rất cao",
        "Category 2: Thiết bị được thiết kế để đảm bảo mức độ bảo vệ cao",
        "Category 3: Thiết bị được thiết kế để đảm bảo mức độ bảo vệ bình thường (trung bình hoặc "
        "tăng cường)",
    ], [
        "Category 1: Equipment designed to ensure a very high level of protection",
        "Category 2: Equipment designed to ensure a high level of protection",
        "Category 3: Equipment designed to ensure a normal (moderate or enhanced) level of "
        "protection",
    ])
    P("<b>Môi trường:</b>", "<b>Environment:</b>")
    B([
        "G: Thiết bị dự định dùng trong khí quyển khí dễ nổ",
        "D: Thiết bị dự định dùng trong khí quyển bụi dễ nổ",
    ], [
        "G: Equipment intended for use in explosive gas atmospheres",
        "D: Equipment intended for use in explosive dust atmospheres",
    ])
    P("Đối với thiết bị được phê duyệt theo ATEX, các đánh dấu ATEX bổ sung sau đây phải xuất hiện "
      "trên thiết bị ngoài các yêu cầu đánh dấu chung.",
      "For ATEX approved equipment the following additional ATEX marking shall appear on the "
      "equipment in addition to the general marking requirements.")
    B([
        "Biểu tượng bảo vệ chống nổ",
        "Nhóm thiết bị - I hoặc II",
        "Category thiết bị - 1, 2 hoặc 3",
        "Môi trường - G hoặc D",
    ], [
        "Explosion protection symbol",
        "Equipment Group - I or II",
        "Equipment Category - 1 or 2 or 3",
        "Environment - G or D",
    ])
    P("Hình 9.5 minh họa mối quan hệ giữa xếp hạng nhóm thiết bị IEC và định nghĩa về xếp hạng "
      "nhóm thiết bị của Chỉ thị ATEX.",
      "Figure 9.5 illustrates the relationship between the IEC equipment group ratings versus the "
      "ATEX Directive's definition of equipment group ratings.")
    FIG(5, F9.fig_f9_05())

    H("9.5.5 Ví dụ đánh dấu", "9.5.5 Marking Examples", h4)
    P("<b>Class/Division</b>", "<b>Class/Division</b>")
    B([
        "CL I DIV 1 GP BCD: Phê duyệt chống nổ cho Class I Division 1, các Nhóm B, C, D",
        "CL 1 DIV 2 GP ABCD: Phê duyệt không gây đánh lửa cho Class I Division 2, các Nhóm A, B, "
        "C, D",
        "I.S. CL I DIV 1 GP ABCD: Phê duyệt an toàn nội tại (Hoa Kỳ) cho khí quyển khí thuộc các "
        "Nhóm A, B, C, D",
        "I.S. CL I,II,III DIV 1 GP ABCDEFG: Phê duyệt an toàn nội tại (Hoa Kỳ) cho khí quyển khí "
        "và bụi thuộc mọi Nhóm",
        "Ex ia INTRINSICALLY SAFE CL I DIV 1 GP CD: Phê duyệt an toàn nội tại (Canada) cho khí "
        "quyển khí thuộc các Nhóm C, D",
        "CL I,II,III DIV 2 GP ABCDEFG: Phê duyệt chỉ có giá trị cho các vị trí Division 2, cả khí "
        "lẫn bụi",
    ], [
        "CL I DIV 1 GP BCD: Explosion-Proof approval for Class I Division 1 for Groups B, C, D",
        "CL 1 DIV 2 GP ABCD: Non-Incendive approval for Class I Division 2 for Groups A, B, C, D",
        "I.S. CL I DIV 1 GP ABCD: Intrinsically-safe approval (USA) for gas atmospheres of Groups "
        "A, B, C, D",
        "I.S. CL I,II,III DIV 1 GP ABCDEFG: Intrinsically-safe approval (USA) for gas and dust "
        "atmospheres for all Groups",
        "Ex ia INTRINSICALLY SAFE CL I DIV 1 GP CD: Intrinsically-safe approval (Canada) for gas "
        "atmospheres of Groups C, D",
        "CL I,II,III DIV 2 GP ABCDEFG: An approval that is only good for Division 2 locations both "
        "gas and dust",
    ])
    P("<b>Zone</b>", "<b>Zone</b>")
    B([
        "Class I Zone 0 AEx ia IIB T4 Ga: Phê duyệt Zone của Hoa Kỳ dùng an toàn nội tại với mức "
        "độ bảo vệ rất cao cho nhóm khí IIB, có mã nhiệt độ T4 và xếp hạng EPL là Ga.",
        "Ex db IIC T5 Gb với II 2 G: Phê duyệt ATEX dùng kỹ thuật chống cháy lan với mức độ bảo "
        "vệ cao cho nhóm khí IIC, có mã nhiệt độ T5 và EPL là Gb.",
        "Ex ia IIC T6 Ga: Phê duyệt an toàn nội tại với mức độ bảo vệ rất cao, phù hợp cho nhóm "
        "khí IIC, có mã nhiệt độ T6 và EPL là Ga.",
        "Ex e mb IIB T4 Gb: Thiết bị dùng an toàn tăng cường và đóng gói kín với mức độ bảo vệ "
        "cao, phù hợp cho nhóm khí IIB, có mã nhiệt độ T4 và EPL là Gb.",
    ], [
        "Class I Zone 0 AEx ia IIB T4 Ga: A USA Zone approval utilizing intrinsic safety with a "
        "very high level of protection for gas group IIB whose temperature code is T4 with an EPL "
        "rating of Ga.",
        "Ex db IIC T5 Gb with II 2 G: An ATEX approval utilizing flame-proof techniques with I "
        "high level of protection suitable for gas group IIC whose temperature code is T5 with an "
        "EPL of Gb.",
        "Ex ia IIC T6 Ga: An intrinsically-safe approval with a very high level of protection "
        "suitable for gas group IIC with a temperature code of T6 and an EPL of Ga.",
        "Ex e mb IIB T4 Gb: Equipment that utilizes increased safety and encapsulation with a high "
        "level of protection suitable for gas group IIB with a temperature code of T4 and an EPL "
        "of Gb.",
    ])

    # ------------------------------------------------------------ 9.6
    H("9.6 Kỹ thuật và phương pháp bảo vệ",
      "9.6 Protection Techniques and Methods")
    P("Liên quan đến các kỹ thuật và phương pháp bảo vệ khác nhau dùng cho thiết bị, hai điểm sau "
      "rất quan trọng:",
      "With regards to the various protection techniques and methods used in equipment, the "
      "following two points are very important:")
    B([
        "Mỗi kỹ thuật và phương pháp bảo vệ là riêng biệt cho khí quyển khí, khí quyển bụi hoặc cho "
        "cả hai.",
        "Mỗi kỹ thuật và phương pháp bảo vệ khác nhau ở mức độ bảo vệ mà nó có thể cung cấp, ví dụ "
        "rất cao, cao hoặc tăng cường.",
    ], [
        "Each protection technique and method is unique for either a gas atmosphere, a dust "
        "atmosphere or both.",
        "Each protection technique and method differs on the level of protection it can provide, "
        "e.g. very high, high, or enhanced.",
    ])

    H("9.6.1 Kỹ thuật chống nổ hoặc chống cháy lan",
      "9.6.1 Explosion-Proof or Flame-Proof Technique", h3)
    P("Phù hợp cho khí quyển khí - Class I Division 1 (hoặc 2), Zone 1 (hoặc 2). Kiểu bảo vệ này "
      "dùng một vỏ có khả năng chịu được sự nổ của khí hoặc hơi bên trong và ngăn sự truyền của "
      "khí nóng dễ đánh lửa ra bên ngoài vỏ, nơi có thể có khí quyển khí dễ nổ. Nói một cách đơn "
      "giản, hãy chứa vụ nổ bên trong vỏ và ngăn đánh lửa khí quyển khí dễ nổ bên ngoài.",
      "Suitable for gas atmospheres - Class I Division 1 (or 2), Zone 1 (or 2). This type of "
      "protection utilizes an enclosure capable of withstanding an explosive gas or vapor within "
      "it and prevents the transmission of ignitable hot gases outside the enclosure, which may "
      "be surrounded by an explosive gas atmosphere. In simple terms, contain the explosion within "
      "the enclosure and prevent ignition of the explosive gas atmosphere outside it.")
    P("<b>Ưu điểm</b>", "<b>Advantages</b>")
    B([
        "Người dùng quen thuộc với kỹ thuật này và hiểu nguyên lý cùng ứng dụng của nó.",
        "Thiết kế vỏ chắc chắn bảo vệ các linh kiện bên trong của thiết bị.",
        "Vỏ chống nổ thường cũng chống thời tiết.",
    ], [
        "Users are familiar with the technique and understand its principles and applications.",
        "Sturdy housing design provides protection to the internal components of the equipment.",
        "An explosion-proof housing is usually weatherproof as well.",
    ])
    P("<b>Nhược điểm</b>", "<b>Disadvantages</b>")
    B([
        "Phải cắt điện mạch hoặc làm cho vị trí không còn nguy hiểm trước khi tháo nắp vỏ.",
        "Mở nắp trong khu vực nguy hiểm sẽ làm mất toàn bộ khả năng bảo vệ.",
        "Nhìn chung kỹ thuật này đòi hỏi vỏ bắt bulông hoặc ren nặng.",
        "Dải nhiệt độ môi trường mở rộng cần các hệ số an toàn bổ sung mà thiết kế có thể không "
        "đáp ứng được.",
        "Để duy trì xếp hạng chống nổ và giảm tích tụ áp suất, cần dùng Seal ống dẫn hoặc cáp "
        "chống nổ.",
    ], [
        "Circuits must be de-energized or the location rendered non-hazardous before housing "
        "covers can be removed.",
        "Opening of a cover in a hazardous area voids all protection.",
        "Generally, this technique requires use of heavy bolted or screwed enclosures.",
        "Extended ambient temperature ranges require additional safety factors that the design "
        "may not be able to accommodate.",
        "To maintain the explosion-proof rating and reduce pressure piling, conduit seals or "
        "explosion-proof cabling is necessary.",
    ])

    H("9.6.2 Kỹ thuật an toàn nội tại",
      "9.6.2 Intrinsically-Safe Technique", h3)
    P("Phù hợp cho khí quyển khí hoặc bụi - Class I Division 1 (hoặc Class II,III Division1), Zone "
      "0 (hoặc 1 hoặc 2), Zone 20 (hoặc 21 hoặc 22). Kiểu bảo vệ này hoạt động bằng cách hạn chế "
      "sự giải phóng năng lượng điện hoặc năng lượng nhiệt có sẵn trong mạch và thiết bị ở mức "
      "không đủ để đánh lửa một khí quyển nổ cụ thể. Thiết bị được thiết kế cho các nhóm khí và "
      "bụi cụ thể, cùng với các mức độ bảo vệ khác nhau, có xét đến điều kiện bình thường và bất "
      "thường (ngoại trừ thiết bị Class/Division luôn được đánh giá là Division 1).",
      "Suitable for gas or dust atmospheres - Class I Division 1 (or Class II,III Division1), Zone "
      "0 (or 1 or 2), Zone 20 (or 21 or 22). This type of protection operates by limiting the "
      "release of electrical energy or thermal energy available in the circuits and equipment to "
      "levels that are incapable of igniting a specific explosive atmosphere. Equipment is "
      "designed for specific gas and dust groups, along with varying levels of protection, which "
      "considers normal and abnormal conditions (except for class/division equipment which is "
      "always evaluated as Division 1).")
    P("<b>Ưu điểm</b>", "<b>Advantages</b>")
    B([
        "Không cần bảo vệ nặng cho dây dẫn hiện trường nên chi phí thấp hơn.",
        "Linh hoạt hơn vì kỹ thuật này cho phép dùng các linh kiện đơn giản như công tắc, tiếp điểm "
        "đóng, cặp nhiệt điện, RTD và các thiết bị khác không tích lũy năng lượng mà không cần "
        "chứng nhận.",
        "Bảo trì và sửa chữa tại hiện trường dễ dàng hơn. Không cần cắt điện trước khi điều chỉnh "
        "hoặc hiệu chuẩn thiết bị hiện trường. Hệ thống vẫn an toàn ngay cả khi thiết bị hỏng vì "
        "mức năng lượng quá thấp để đánh lửa hỗn hợp dễ đánh lửa nhất. Thiết bị chẩn đoán và hiệu "
        "chuẩn phải có phê duyệt phù hợp cho khu vực nguy hiểm.",
    ], [
        "Heavy protection of the field wiring is not necessary and offers lower cost.",
        "Greater flexibility is offered since this technique permits simple components, such as "
        "switches, contact closures, thermocouples, RTDs, and other non-energy storing instruments "
        "to be used without certification.",
        "Field maintenance and repair is easier. There is no need to remove power before "
        "adjustment or calibration of the field equipment. The system remains safe even if the "
        "equipment is damaged because the energy level is too low to ignite the most easily "
        "ignitable mixture. Diagnostic and calibration equipment must have the appropriate "
        "approvals for the hazardous area.",
    ])
    P("<b>Nhược điểm</b>", "<b>Disadvantages</b>")
    B([
        "Kỹ thuật này yêu cầu dùng rào an toàn nội tại để giới hạn điện áp, dòng điện và công suất "
        "giữa khu vực nguy hiểm và khu vực an toàn nhằm tránh phát sinh tia lửa hoặc điểm nóng "
        "trong mạch thiết bị.",
        "Người dùng cần nắm vững kỹ thuật này và các phương pháp đấu dây liên quan.",
        "Ứng dụng tiêu thụ năng lượng cao không phù hợp với kỹ thuật này vì năng lượng bị giới hạn "
        "tại nguồn (rào). Kỹ thuật này chỉ dùng cho ứng dụng công suất thấp như mạch DC, bộ định "
        "vị điện - khí nén, bộ chuyển đổi điện - khí nén, bộ chuyển đổi tín hiệu, v.v.",
    ], [
        "This technique requires the use of an intrinsically-safe barrier to limit the voltage, "
        "current, and power between the hazardous area and safe area to avoid development of "
        "sparks or hot spots in the circuitry of the equipment.",
        "Users need to be comfortable with this technique and the wiring practices associated "
        "with it.",
        "High energy consumption applications are not applicable to this technique because the "
        "energy is limited at the source (barrier). This technique is limited to low power "
        "applications such as DC circuits, electro-pneumatic positioners, electro-pneumatic "
        "converters, transducers, etc.",
    ])

    H("9.6.3 Kỹ thuật không gây đánh lửa hoặc loại n",
      "9.6.3 Non-Incendive or Type n Technique", h3)
    P("Phù hợp cho khí quyển khí - Class I Division 2, Zone 2. Đây là kiểu bảo vệ trong đó thiết "
      "bị không có khả năng, trong điều kiện vận hành bình thường, gây đánh lửa do bất kỳ hồ quang, "
      "tia lửa hoặc hiệu ứng nhiệt nào bên trong thiết bị. Kiểu bảo vệ này cũng áp dụng cho thiết "
      "bị có chứa hồ quang hoặc tia lửa, miễn là chúng được bảo vệ bằng một trong các cách quy "
      "định trong tiêu chuẩn.",
      "Suitable for gas atmospheres - Class I Division 2, Zone 2. A type of protection in which "
      "the equipment is incapable, under normal operating conditions, of causing an ignition due "
      "to any arcs, sparks, or thermal effects within the equipment. This type of protection also "
      "applies to equipment which does contain arcs or sparks, provided they are protected by one "
      "of the ways specified in the standard.")
    P("<b>Ưu điểm</b>", "<b>Advantages</b>")
    B([
        "Thiết bị được thiết kế sao cho không tạo hồ quang hay tia lửa, cũng không phát triển nhiệt "
        "độ cao.",
        "Thiết bị nói chung có chi phí thấp hơn các kiểu bảo vệ khác vì không cần vỏ chống nổ hay "
        "rào giới hạn năng lượng.",
        "Đối với ứng dụng Class I Division 2, nếu nối vào mạch không gây đánh lửa, người dùng được "
        "phép dùng bất kỳ phương pháp đấu dây thông thường nào.",
    ], [
        "Equipment is designed such that it does not produce any arcs or sparks, nor does it "
        "develop any high temperatures.",
        "Equipment is generally lower cost than the other types of protections because there is "
        "no need for explosion-proof housings or energy limiting barriers.",
        "For Class I Division 2 applications, if connected to a non-incendive circuit, the user is "
        "allowed to use any ordinary wiring practice.",
    ])
    P("<b>Nhược điểm</b>", "<b>Disadvantages</b>")
    B([
        "Kỹ thuật này chỉ giới hạn cho ứng dụng Division 2 hoặc Zone 2.",
        "Đối với ứng dụng Class I Division 2, dây dẫn hiện trường phải được bảo vệ tốt.",
        "Mạch không gây đánh lửa là chi phí bổ sung cho người dùng cuối vì phải giới hạn năng "
        "lượng ở mức an toàn trong trường hợp dây dẫn hiện trường bị hở, ngắn mạch hoặc chạm đất.",
    ], [
        "This technique is limited to Division 2 or Zone 2 applications.",
        "For Class I Division 2 applications, the field wiring must be well protected.",
        "Non-incendive circuits are an additional expense to the end user because it must limit "
        "the energy to safe levels in the event of a open, short, or ground of the field wiring.",
    ])

    H("9.6.4 An toàn tăng cường", "9.6.4 Increased Safety", h3)
    P("Phù hợp cho môi trường khí - Zone 1 (hoặc 2). Kiểu bảo vệ này áp dụng cho thiết bị điện "
      "hoặc linh kiện Ex trong đó các biện pháp bổ sung được áp dụng để tăng cường an toàn chống "
      "lại khả năng nhiệt độ quá cao và sự xuất hiện của hồ quang và tia lửa. Chỉ phù hợp cho "
      "thiết bị không chứa linh kiện gây đánh lửa (hồ quang hoặc tia lửa) trong vận hành bình "
      "thường. Ví dụ gồm hộp đấu dây, hộp nối, v.v. Kỹ thuật này thường dùng phối hợp với thiết bị "
      "được phê duyệt chống cháy lan.",
      "Suitable for gas environments - Zone 1 (or 2). This type of protection applies to "
      "electrical equipment or Ex components in which additional measures are applied to give "
      "increased security against the possibility of excessive temperatures and against the "
      "occurrence of arcs and sparks. This protection is only suitable for equipment that does "
      "not contain any incendive devices (arcs or sparks) during normal operation. Examples "
      "include: terminal boxes, junction boxes, etc. This is commonly used in conjunction with "
      "flame-proof approved equipment.")
    P("<b>Ưu điểm</b>", "<b>Advantages</b>")
    B([
        "Vỏ an toàn tăng cường có xếp hạng ít nhất là IP54.",
        "Lắp đặt và bảo trì dễ dàng hơn vỏ chống cháy lan.",
        "Kỹ thuật này giảm đáng kể chi phí dây dẫn so với vỏ chống cháy lan.",
    ], [
        "Increased safety enclosures provide at least an IP54 enclosure rating.",
        "Installation and maintenance are easier than flame-proof enclosures.",
        "This technique offers significantly reduced wiring costs over flame-proof enclosures.",
    ])
    P("<b>Nhược điểm</b>", "<b>Disadvantages</b>")
    B(["Kỹ thuật này bị hạn chế về thiết bị có thể dùng. Thường chỉ dùng cho các apparatus như hộp "
       "đấu dây và các khoang.",
       ],
      ["This technique is limited in the apparatus for which it can be used. It is normally used "
       "for apparatuses, such as terminal boxes and compartments."])
    # The source has a single disadvantage item; rebuild the list with exactly one.
    b[-1] = ul(["Kỹ thuật này bị hạn chế về thiết bị có thể dùng. Thường chỉ dùng cho các apparatus "
               "như hộp đấu dây và các khoang."]
               if vi else
               ["This technique is limited in the apparatus for which it can be used. It is "
                "normally used for apparatuses, such as terminal boxes and compartments."])

    H("9.6.5 Chống đánh lửa bụi hoặc vỏ chống bụi",
      "9.6.5 Dust Ignition-Proof or Enclosure Dust-Proof", h3)
    P("Phù hợp cho khí quyển bụi - Class II Division 1 (hoặc 2), Zone 20 (hoặc 21 hoặc 22). Kiểu "
      "bảo vệ này tạo ra một vỏ loại trừ được lượng bụi đủ gây đánh lửa và không cho phép hồ "
      "quang, tia lửa hoặc nhiệt sinh ra bên trong vỏ gây đánh lửa khí quyển bụi bên ngoài dù ở "
      "dạng lơ lửng trong không khí hay dạng lớp.",
      "Suitable for dust atmospheres - Class II Division 1 (or 2), Zone 20 (or 21 or 22). This "
      "type of protection results in an enclosure that will exclude ignitable amounts of dust and "
      "will not permit arcs, sparks, or heat otherwise generated inside the enclosure to cause an "
      "ignition of the exterior dust atmosphere in atmospheric suspension or in layers.")
    P("<b>Ưu điểm</b>", "<b>Advantages</b>")
    B([
        "Lắp đặt không cần rào, trong khi thiết bị an toàn nội tại dùng cho bụi thì cần.",
        "Có thể dùng trong ứng dụng năng lượng cao.",
    ], [
        "Installation does not require a barrier, whereas intrinsically-safe equipment for dust "
        "does.",
        "Can be used in high-energy applications.",
    ])
    P("<b>Nhược điểm</b>", "<b>Disadvantages</b>")
    B(["Một số apparatus nhất định có thể chỉ có an toàn nội tại là lựa chọn duy nhất."],
      ["Certain apparatuses may be such that intrinsic safety is the only option."])

    # ------------------------------------------------------------ 9.7
    H("9.7 Xếp hạng vỏ bọc", "9.7 Enclosure Ratings")
    P("Vỏ của thiết bị điện thường được thử nghiệm để xác định khả năng ngăn sự xâm nhập của chất "
      "lỏng và bụi. Các tiêu chuẩn xếp hạng vỏ bọc được dùng rộng rãi nhất là NEMA 250 và UL 50 "
      "(Hoa Kỳ), CSA C22.2 No. 94 (Canada) và IEC 60529 (toàn cầu). Tiêu chuẩn UL 50 và CSA "
      "C22.2 No. 94 về cơ bản tương tự NEMA 250 về xếp hạng.",
      "Enclosures of electrical equipment are often tested to determine their ability to prevent "
      "the ingress of liquids and dusts. The most widely used enclosure rating standards are NEMA "
      "250 and UL 50 (United States), CSA C22.2 No. 94 (Canada), and IEC 60529 (worldwide). "
      "Standard UL 50 and CSA C22.2 No. 94 closely parallels standard NEMA 250 with regards to "
      "ratings.")
    P("Một số xếp hạng vỏ bọc phổ biến hơn được định nghĩa trong NEMA 250 cho vị trí không phân "
      "loại (vị trí chung) như sau:",
      "Some of the more common enclosure ratings as defined in NEMA 250 for unclassified "
      "locations (general locations) are as follows:")
    B([
        "Type 3 - Vỏ trong nhà hoặc ngoài nhà, chống mưa, chống bụi, chống đóng băng: Dùng trong "
        "nhà hoặc ngoài nhà chủ yếu để bảo vệ ở mức độ nhất định khỏi bụi bẩn rơi xuống, bụi bay "
        "theo gió, mưa, mưa đá, tuyết và hư hại do băng hình thành bên ngoài vỏ.",
        "Type 3X - Vỏ trong nhà hoặc ngoài nhà, chống mưa, chống bụi, chống đóng băng, chống ăn "
        "mòn: Dùng trong nhà hoặc ngoài nhà chủ yếu để bảo vệ ở mức độ nhất định khỏi bụi bẩn rơi "
        "xuống, bụi bay theo gió, mưa, mưa đá, tuyết, hư hại do băng hình thành bên ngoài vỏ và "
        "sự ăn mòn.",
        "Type 3R - Vỏ trong nhà hoặc ngoài nhà, chống mưa (hoặc chống thấm mưa), chống đóng băng: "
        "Dùng trong nhà hoặc ngoài nhà chủ yếu để bảo vệ ở mức độ nhất định khỏi bụi bẩn rơi "
        "xuống, mưa, mưa đá, tuyết và hư hại do băng hình thành bên ngoài vỏ.",
        "Type 3RX - Vỏ trong nhà hoặc ngoài nhà, chống mưa (hoặc chống thấm mưa), chống đóng "
        "băng, chống ăn mòn: Dùng trong nhà hoặc ngoài nhà chủ yếu để bảo vệ ở mức độ nhất định "
        "khỏi bụi bẩn rơi xuống, mưa, mưa đá, tuyết, hư hại do băng hình thành bên ngoài vỏ và sự "
        "ăn mòn.",
        "Type 3S - Vỏ trong nhà hoặc ngoài nhà, chống mưa, chống bụi, chống băng: Dùng trong nhà "
        "hoặc ngoài nhà chủ yếu để bảo vệ ở mức độ nhất định khỏi bụi bẩn rơi xuống, bụi bay theo "
        "gió, mưa, mưa đá, tuyết và cho phép vận hành các cơ cấu bên ngoài khi có băng phủ.",
        "Type 3SX - Vỏ trong nhà hoặc ngoài nhà, chống mưa, chống bụi, chống băng, chống ăn mòn: "
        "Dùng trong nhà hoặc ngoài nhà chủ yếu để bảo vệ ở mức độ nhất định khỏi bụi bẩn rơi "
        "xuống, bụi bay theo gió, mưa, mưa đá, tuyết, cho phép vận hành các cơ cấu bên ngoài khi "
        "có băng phủ và chống ăn mòn.",
        "Type 4 - Vỏ trong nhà hoặc ngoài nhà, chống mưa, chống nước, chống bụi, chống đóng băng: "
        "Dùng trong nhà hoặc ngoài nhà chủ yếu để bảo vệ ở mức độ nhất định khỏi bụi bẩn rơi "
        "xuống, bụi bay theo gió, mưa, mưa đá, tuyết, nước bắn, nước phun từ vòi và hư hại do băng "
        "hình thành bên ngoài vỏ.",
        "Type 4X - Vỏ trong nhà hoặc ngoài nhà, chống mưa, chống nước, chống bụi, chống đóng "
        "băng, chống ăn mòn: Dùng trong nhà hoặc ngoài nhà chủ yếu để bảo vệ ở mức độ nhất định "
        "khỏi bụi bẩn rơi xuống, bụi bay theo gió, mưa, mưa đá, tuyết, nước bắn, nước phun từ vòi, "
        "hư hại do băng hình thành bên ngoài vỏ và sự ăn mòn.",
    ], [
        "Type 3 - Indoor or outdoor enclosure, rain-tight, dust-tight, ice-resistant: Intended for "
        "indoor or outdoor use primarily to provide a degree of protection against falling dirt, "
        "windblown dust, rain, sleet, snow, and damage from external ice formation on the enclosure.",
        "Type 3X - Indoor or outdoor enclosure, rain-tight, dust-tight, ice-resistant, "
        "corrosion-resistant: Intended for indoor or outdoor use primarily to provide a degree of "
        "protection against falling dirt, windblown dust, rain, sleet, snow, damage from external "
        "ice formation on the enclosure, and corrosion.",
        "Type 3R - Indoor or outdoor enclosure, rainproof (or rain-tight), ice-resistant: Intended "
        "for indoor or outdoor use primarily to provide a degree of protection against falling "
        "dirt, rain, sleet, snow, and damage from external ice formation on the enclosure.",
        "Type 3RX - Indoor or outdoor enclosure, rainproof (or rain-tight), ice-resistant, "
        "corrosion-resistant: Intended for indoor or outdoor use primarily to provide a degree of "
        "protection against falling dirt, rain, sleet, snow, damage from external ice formation on "
        "the enclosure, and corrosion.",
        "Type 3S - Indoor or outdoor enclosure, rain-tight, dust-tight, ice-proof: Intended for "
        "indoor or outdoor use primarily to provide a degree of protection against falling dirt, "
        "windblown dust, rain, sleet, snow, and to provide for operation of external mechanisms "
        "when ice laden.",
        "Type 3SX - Indoor or outdoor enclosure, rain-tight, dust-tight, ice-proof, "
        "corrosion-resistant: Intended for indoor or outdoor use primarily to provide a degree of "
        "protection against falling dirt, windblown dust, rain, sleet, snow, and to provide for "
        "operation of external mechanisms when ice laden, and corrosion.",
        "Type 4 - Indoor or outdoor enclosure, rain-tight, water-tight, dust-tight, ice-resistant: "
        "Intended for indoor or outdoor use primarily to provide a degree of protection against "
        "falling dirt, windblown dust, rain, sleet, snow, splashing water, hose-directed water, and "
        "damage from external ice formations on the enclosure.",
        "Type 4X - Indoor or outdoor enclosure, rain-tight, water-tight, dust-tight, "
        "ice-resistant, corrosion-resistant: Intended for indoor or outdoor use primarily to "
        "provide a degree of protection against falling dirt, windblown dust, rain, sleet, snow, "
        "splashing water, hose-directed water, damage from external ice formations on the "
        "enclosure, and corrosion.",
    ])
    P("NEMA 250 cũng định nghĩa xếp hạng vỏ bọc cho vị trí đã phân loại như sau:",
      "NEMA 250 also defines enclosure ratings for classified locations as follows:")
    B([
        "Type 7 - Vỏ trong nhà, được phê duyệt Class I Division 1: Dùng trong nhà cho ứng dụng "
        "chống nổ.",
        "Type 8 - Vỏ trong nhà hoặc ngoài nhà, được phê duyệt Class I Division 1, chống mưa, "
        "chống đóng băng: Dùng trong nhà hoặc ngoài nhà cho ứng dụng chống nổ và bảo vệ ở mức độ "
        "nhất định khỏi mưa, mưa đá, tuyết và hư hại do băng hình thành bên ngoài vỏ.",
        "Type 9 - Vỏ trong nhà, được phê duyệt Class II Division 1: Dùng trong nhà cho ứng dụng "
        "chống đánh lửa bụi.",
    ], [
        "Type 7 - Indoor enclosure, Class I Division 1 approved: Intended for indoor use in "
        "explosion-proof applications.",
        "Type 8 - Indoor or outdoor enclosure, Class I Division 1 approved, rain-tight, "
        "ice-resistant: Intended for indoor or outdoor use in explosion-proof applications and "
        "which provides a degree of protection from rain, sleet, snow, and damaged from external "
        "ice formation on the enclosure.",
        "Type 9 - Indoor enclosure, Class II Division 1 approved: Intended for indoor use in dust "
        "ignition-proof applications.",
    ])
    P("Các xếp hạng NEMA cho vị trí đã phân loại thường bị hiểu nhầm. Rõ ràng là xếp hạng NEMA 7 "
      "hoặc NEMA 8 về cơ bản giống như Class I Division 1. Xếp hạng NEMA 9 về cơ bản giống như "
      "Class II Division 1. Theo NEC và CEC, mọi thiết bị phải được đánh dấu phù hợp với class, "
      "division và group mà nó đã đạt được. Do đó, sản phẩm chỉ được đánh dấu NEMA 7, NEMA 8 hoặc "
      "NEMA 9 mà không có đánh dấu bổ sung xác định class, division hoặc group thì không được "
      "chấp nhận và không được phép. Hầu hết tổ chức phê duyệt đều không khuyến khích dùng NEMA 7, "
      "NEMA 8 hoặc NEMA 9 vì lý do này và không cho phép sử dụng.",
      "The NEMA ratings for classified locations are often misunderstood. It should be apparent "
      "that a NEMA 7 or NEMA 8 rating is essentially the same as that for Class I Division 1. A "
      "NEMA 9 rating is essentially the same as that for Class II Division 1. Per the NEC and "
      "CEC, all equipment must be appropriately marked for the class, division, and group that it "
      "has obtained. Therefore, a product marked as NEMA 7, NEMA 8, or NEMA 9 alone without any "
      "additional marking identifying its class, division, or group is unacceptable and not "
      "allowed. Most approval agencies discourage the use of applying NEMA 7, NEMA 8, or NEMA 9 "
      "for this very reason and do not allow it.")
    P("Vỏ được thử nghiệm theo IEC 60529 được phép mang mã Bảo vệ xâm nhập (IP) quy định xếp hạng "
      "của nó. Mã IP gồm các chữ «IP» theo sau là hai chữ số đặc trưng cho mức độ phù hợp đã đạt "
      "được. Chữ số thứ nhất biểu thị mức độ bảo vệ chống tiếp xúc hoặc tiếp cận của người với "
      "phần mang điện, chống tiếp xúc của người với bộ phận chuyển động bên trong vỏ, và chống "
      "xâm nhập của vật lạ rắn. Chữ số thứ hai biểu thị mức độ bảo vệ của vỏ chống sự xâm nhập "
      "của nước. Xem Hình 9.7 để biết thêm thông tin.",
      "Enclosures that are tested to IEC 60529 are allowed to carry an Ingress Protection (IP) "
      "code that specifies its rating. The IP code consists of the letters ‘IP’ followed by two "
      "characteristic numerals the degree of conformity obtained. The first numeral indicates "
      "the degree of protection against human contact with or approach to live parts, human "
      "contact with moving parts inside the enclosure, and ingress of solid foreign body objects. "
      "The second numeral indicates the degree of protection provided by the enclosure against "
      "the ingress of water. See Figure 9.7 for more information.")
    FIG(6, F9.fig_f9_06())
    FIG(7, F9.fig_f9_07())

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 9 chiếm tr. 192–209 của bản in (18 trang) trong Emerson, Control Valve Handbook, ấn "
      "bản 6 (2020). Nội dung gồm bảy mục 9.1–9.7: tiêu chuẩn van điều khiển, phê duyệt sản phẩm "
      "cho vị trí nguy hiểm, hệ thống phân loại, mã nhiệt độ, cách đặt tên, kỹ thuật bảo vệ và xếp "
      "hạng vỏ bọc. Bảy hình được vẽ lại dạng vector và đặt theo thứ tự số tại vị trí văn bản hợp "
      "lý.",
      "Chapter 9 occupies printed pp. 192-209 (18 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains seven sections, 9.1-9.7: control valve standards, product "
      "approvals for hazardous locations, classification systems, temperature codes, "
      "nomenclature, protection techniques, and enclosure ratings. The seven numbered figures "
      "are redrawn as vectors and placed in numbered order at their logical prose points.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 Emerson "
      "Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 Emerson "
      "Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
