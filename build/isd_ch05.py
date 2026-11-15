# -*- coding: utf-8 -*-
"""Book 5, Chapter 5 — Limitations of the Existing Safety Analysis Methods in
Conceptual Process Design (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 25–30.  A short prose argument on
pp. 25–26 followed by two full-page tables: Table 2 (pp. 27–28) and Table 3
(pp. 29–30).  The chapter contains NO figures in the source; the two vector
graphics in `isdfig.py` (`fig_c05_curves`, `fig_c05_gap`) are explicitly
labelled editorial schematics drawn from the prose and the two tables.
"""

from isd_common import (fig, h2, h3, note, p, table)
import isdfig as F

PAGES_SRC = 6           # source pages 25–30
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Limitations of Existing Methods in Conceptual Process Design"
TITLE_VI = "Hạn chế của các phương pháp hiện có trong thiết kế sơ bộ"


def _pick(pair, lang):
    """Select the Vietnamese (0) or English (1) member of a content pair."""
    return pair[0] if lang == "vi" else pair[1]


def _bl(items):
    """Render a source bullet list inside a table cell."""
    return "<br>".join("• " + x for x in items)


# ---- Source-derived Table 2 (pp. 27–28) -----------------------------------
# Each row is (stage, documents, information, suitable analyses); every member
# is a (vi, en) pair.  Bullet cells are pairs of lists; the analyses cell is a
# pair of HTML strings because "Laboratory screening and testing" is a heading
# followed by its own bullet list in the printed table.
_T2 = [
    (
        ("Nghiên cứu và phát triển quá trình<br><i>Process R&amp;D</i>",
         "Process R&amp;D"),
        ([
            "rà soát tài liệu",
            "rà soát bằng sáng chế",
            "báo cáo nghiên cứu",
            "báo cáo quy mô bàn thí nghiệm và pilot",
            "phác thảo sơ đồ dòng",
        ], [
            "literature review",
            "patent review",
            "research reports",
            "bench scale &amp; pilot reports",
            "sketch of flow sheet",
        ]),
        ([
            "hóa chất và đặc tính của chúng",
            "phản ứng hóa học và tương tác giữa chúng",
            "nhiệt động học",
            "tính chất vật lý",
            "khái niệm quá trình sơ bộ",
        ], [
            "chemicals and their characteristics",
            "chemical reactions and interactions",
            "thermodynamics",
            "physical properties",
            "preliminary process concept",
        ]),
        ("<b>Sàng lọc và thử nghiệm trong phòng thí nghiệm</b><br>"
         "• đối với hóa chất (độc tính, tính không bền, tính nổ)<br>"
         "• đối với phản ứng (khả năng nổ)<br>"
         "• đối với tạp chất<br>"
         "• thử nghiệm trên nhà máy pilot",
         "<b>Laboratory screening and testing</b><br>"
         "• for chemicals (toxicity, instability, explosibility)<br>"
         "• for reactions (explosibility)<br>"
         "• for impurities<br>"
         "• Pilot plant tests"),
    ),
    (
        ("Thiết kế sơ bộ<br><i>Predesign (Conceptual design)</i>",
         "Predesign<br><i>(Conceptual design)</i>"),
        ([
            "sơ đồ dòng",
            "P&amp;ID sơ bộ (pid sơ bộ)",
            "nghiên cứu khả thi",
            "hướng dẫn vận hành sơ bộ",
        ], [
            "flow sheet",
            "preliminary pid",
            "feasibility study",
            "preliminary operation instructions",
        ]),
        ([
            "cân bằng vật chất",
            "cân bằng năng lượng",
            "khái niệm quá trình",
            "điều kiện vận hành",
            "phác thảo mặt bằng",
        ], [
            "material balance",
            "energy balance",
            "process concept",
            "operating conditions",
            "sketch of layout",
        ]),
        ("<b>ISI, PIIS</b><br>(mức thô; Chỉ số cháy và nổ Dow F&amp;E, "
         "Chỉ số Mond, Hazop)",
         "<b>ISI, PIIS</b><br>(coarse; Dow F&amp;E Index, Mond Index, Hazop)"),
    ),
    (
        ("Thiết kế cơ bản<br><i>Basic engineering</i>",
         "Basic engineering"),
        ([
            "sơ đồ dòng cuối cùng",
            "P&amp;ID cuối cùng (PID cuối cùng)",
            "phiếu dữ liệu cho thiết bị, đường ống, thiết bị đo, v.v.",
            "hướng dẫn vận hành",
            "mặt bằng sơ bộ",
        ], [
            "final flow sheets",
            "final PID",
            "data sheets for equipment, piping, instruments etc.",
            "operating instructions",
            "preliminary layout",
        ]),
        ([
            "dữ liệu quá trình cho thiết bị, đường ống và thiết bị đo",
            "quy trình vận hành, khởi động và dừng máy",
            "mặt bằng sơ bộ",
        ], [
            "process data on equipment, piping and instruments",
            "operating, start-up and shut-down procedures",
            "preliminary layout",
        ]),
        ("Chỉ số cháy và nổ Dow F&amp;E, Chỉ số Mond, Hazop, Hazan, "
         "cây sự cố (Fault tree), RISKAT",
         "Dow F&amp;E Index, Mond Index, Hazop, Hazan, Fault tree, RISKAT"),
    ),
    (
        ("Thiết kế chi tiết<br><i>Detailed engineering</i>",
         "Detailed engineering"),
        ([
            "chỉ dẫn kỹ thuật thiết bị",
            "chỉ dẫn kỹ thuật đường ống",
            "chỉ dẫn kỹ thuật thiết bị đo",
            "chỉ dẫn kỹ thuật điện",
            "chỉ dẫn kỹ thuật điều khiển",
            "chỉ dẫn kỹ thuật xây lắp",
        ], [
            "equipment specifications",
            "piping specifications",
            "instrument specifications",
            "electrical specifications",
            "control specifications",
            "construction specifications",
        ]),
        ([
            "dữ liệu thiết kế chi tiết cho thiết bị, đường ống, thiết bị đo, "
            "điều khiển, điện, xây lắp, v.v.",
            "mặt bằng",
        ], [
            "detailed engineering data for equipment, piping, instruments, "
            "controls, electrical, constructions etc.",
            "layout",
        ]),
        ("Hazop, Chỉ số cháy và nổ Dow F&amp;E, Chỉ số Mond, cây sự cố",
         "Hazop, Dow F&amp;E Index, Mond Index, Fault tree"),
    ),
    (
        ("Mua sắm / Chế tạo / Xây lắp<br><i>Procurement, Fabrication, "
         "Construction</i>",
         "Procurement<br>Fabrication<br>Construction"),
        ([
            "tài liệu của nhà cung cấp và chế tạo",
            "biên bản kiểm tra",
            "tài liệu thay đổi tại hiện trường",
        ], [
            "vendor and fabrication documents",
            "inspection reports",
            "field change documents",
        ]),
        ([
            "dữ liệu của nhà cung cấp về thiết bị",
            "dữ liệu 'hoàn công' ('as built')",
        ], [
            "vendor data on equipment",
            "'as built' data",
        ]),
        ("What-If, Checklist (danh mục kiểm tra)",
         "What-If, Checklist"),
    ),
    (
        ("Khởi động<br><i>Start-up</i>", "Start-up"),
        (["tài liệu khởi động và chạy thử"],
         ["start-up and test-run documents"]),
        ([
            "dữ liệu về hiệu năng quá trình",
            "kinh nghiệm vận hành ban đầu",
        ], [
            "data on process performance",
            "first operation experience",
        ]),
        ("What-If, Checklist (danh mục kiểm tra)",
         "What-If, Checklist"),
    ),
    (
        ("Vận hành<br><i>Operation</i>", "Operation"),
        (["báo cáo vận hành"], ["operation reports"]),
        ([
            "dữ liệu vận hành",
            "kinh nghiệm vận hành",
        ], [
            "operation data",
            "operation experience",
        ]),
        ("Hazop, Chỉ số cháy và nổ Dow F&amp;E, Chỉ số Mond, cây sự cố",
         "Hazop, Dow F&amp;E Index, Mond Index, Fault tree"),
    ),
]


def _t_table2(lang):
    """Table 2, pp. 27–28 — safety analysis methods by design phase."""
    if lang == "vi":
        hdr = ["Giai đoạn thiết kế", "Tài liệu được lập",
               "Thông tin có được", "Một số phân tích an toàn phù hợp"]
        cap = ("Bảng 2 (nguyên bản tr. 27–28) — các phương pháp phân tích an "
               "toàn trong những giai đoạn khác nhau của thiết kế nhà máy quá "
               "trình. Giữ nguyên cấu trúc bốn cột và toàn bộ nội dung của "
               "nguyên bản; dòng tiếp nối ở tr. 28 được gộp vào hàng "
               "<i>Thiết kế cơ bản</i>.")
    else:
        hdr = ["Design stage", "Documents produced", "Information produced",
               "Some suitable safety analyses"]
        cap = ("Table 2 (source pp. 27–28) — safety analysis methods in the "
               "different phases of process plant design. The original "
               "four-column structure and all of its content are kept; the "
               "continuation row on p. 28 is folded into the "
               "<i>Basic engineering</i> row.")
    rows = []
    for stage, docs, info, an in _T2:
        rows.append((_pick(stage, lang),
                     _bl(_pick(docs, lang)),
                     _bl(_pick(info, lang)),
                     _pick(an, lang)))
    return table(hdr, rows, caption=cap, cls="tbl wide")


# ---- Source-derived Table 3 (pp. 29–30) -----------------------------------
# Group-header rows are strings so `table()` renders them with colspan=3,
# exactly as the method-name bands span the printed table.
_T3 = [
    (
        ("<i>Chỉ số nguy hiểm cháy và nổ Dow (Dow, 1987)</i>",
         "<i>Dow Fire &amp; Explosion Hazard Index (Dow, 1987)</i>"),
        ([
            "tự phản ứng (tính không bền)",
            "phản ứng với nước",
            "tính dễ cháy hoặc khả năng cháy",
            "bản chất nhiệt của phản ứng",
            "vật liệu độc hại",
            "tính chất bụi",
            "tốc độ ăn mòn",
        ], [
            "self-reactivity (instability)",
            "reactivity with water",
            "flammability or combustibility",
            "thermal nature of reaction",
            "toxic materials",
            "dust properties",
            "corrosion rate",
        ]),
        ([
            "mặt bằng tổng thể nhà máy",
            "sơ đồ dòng quá trình",
            "loại quá trình",
            "vận hành trong hoặc gần vùng dễ cháy, áp suất, nhiệt độ, lượng "
            "vật liệu, rò rỉ tại mối nối và đệm kín, loại thiết bị",
            "bảo vệ chống tổn thất (= điều khiển quá trình, cô lập vật liệu, "
            "chống cháy, đê bao chắn)",
        ], [
            "a plot plan of the plant",
            "a process flow sheet",
            "type of process",
            "in or near flammable range, pressure, temperature, quantity of "
            "materials, leakage - joints and packing, equipment types",
            "loss protection (= process control, material isolation, fire "
            "protection, diking)",
        ]),
    ),
    (
        ("<i>Chỉ số Mond (Lees, 1996)</i>",
         "<i>Mond Index (Lees, 1996)</i>"),
        ([
            "khả năng phản ứng của vật liệu",
            "độ nhạy bắt lửa",
            "tự sinh nhiệt và trùng hợp",
            "phân hủy nổ",
            "biến đổi vật lý",
            "độc tính",
        ], [
            "reactivity of materials",
            "ignition sensitivity",
            "spontaneous heating and polymerization",
            "explosive decomposition",
            "physical changes",
            "toxicity",
        ]),
        ([
            "loại quá trình",
            "vận chuyển vật liệu",
            "điều kiện quá trình (p, T, ăn mòn/xói mòn, v.v.)",
            "khoảng cách mặt bằng",
        ], [
            "type of process",
            "material transfer",
            "process conditions ( p, T, corrosion/erosion, etc.)",
            "layout distances",
        ]),
    ),
    (
        ("<i>Chỉ số nguyên mẫu an toàn nội tại (Edwards and Lawrence, 1993)</i>",
         "<i>Prototype Index of Inherent Safety (Edwards and Lawrence, 1993)</i>"),
        ([
            "tính dễ cháy",
            "tính nổ",
            "độc tính",
        ], [
            "flammability",
            "explosiveness",
            "toxicity",
        ]),
        ([
            "tồn lượng",
            "nhiệt độ",
            "áp suất",
            "hiệu suất",
        ], [
            "inventory",
            "temperature",
            "pressure",
            "yield",
        ]),
    ),
    (
        ("<i>Phân tích mối nguy và khả năng vận hành (Kletz, 1992)</i>",
         "<i>Hazard and Operability Analysis (Kletz, 1992)</i>"),
        ([
            "các phản ứng",
            "tính dễ cháy",
            "độc tính",
            "điểm chớp cháy",
            "điều kiện phản ứng",
            "các tính chất vật lý và hóa học khác của vật liệu",
        ], [
            "reactions",
            "flammability",
            "toxicity",
            "flash point",
            "reaction conditions",
            "other physical and chemical properties of materials",
        ]),
        ([
            "sơ đồ dòng và P&amp;ID",
            "nhiệt độ, áp suất, lưu lượng, mức, thành phần",
        ], [
            "flowsheets and PIDs",
            "temperature, pressure, flow, level, composition",
        ]),
    ),
]

_T3_OTHER_HAZOP = (
    "• được thực hiện bởi một nhóm, ví dụ kỹ sư thiết kế và kỹ sư quá trình, "
    "chuyên gia thiết bị đo, nhà hóa học nghiên cứu và chủ tịch đoàn độc lập",
    "• carried out by a team of e.g. design and process engineer, instrument "
    "expert, research chemist and independent chairman",
)


def _t_table3(lang):
    """Table 3, pp. 29–30 — information required for the Chapter 4 methods."""
    if lang == "vi":
        hdr = ["Yêu cầu về hóa chất", "Yêu cầu về quá trình và thiết bị",
               "Yêu cầu khác"]
        blank = "<i>(trống trong nguyên bản)</i>"
        cap = ("Bảng 3 (nguyên bản tr. 29–30) — thông tin cần thiết cho các "
               "phương pháp phân tích an toàn. Các dòng tên phương pháp trải "
               "rộng cả ba cột như trong nguyên bản; hàng <i>Chỉ số Mond</i> "
               "bị ngang trang được gộp lại.")
    else:
        hdr = ["Chemical requirements", "Process and equipment requirements",
               "Other requirements"]
        blank = "<i>(blank in the source)</i>"
        cap = ("Table 3 (source pp. 29–30) — information required for safety "
               "analysis methods. The method-name bands span all three columns "
               "as in the original; the <i>Mond Index</i> row, split across "
               "the page break, is merged here.")
    rows = []
    for idx, (band, chem, proc) in enumerate(_T3):
        rows.append(_pick(band, lang))
        other = _pick(_T3_OTHER_HAZOP, lang) if idx == 3 else blank
        rows.append((_bl(_pick(chem, lang)),
                     _bl(_pick(proc, lang)),
                     other))
    return table(hdr, rows, caption=cap, cls="tbl wide")


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 5.</b> thiết kế sơ bộ / predesign — giai "
                "đoạn thiết kế khái niệm · ISI — Chỉ số An toàn Nội tại "
                "(Chương 8) · PIIS — Chỉ số Nguyên mẫu An toàn Nội tại "
                "(Chương 4) · Dow F&amp;E — Chỉ số cháy và nổ Dow · Mond "
                "Index — Chỉ số Mond · Hazop — phân tích mối nguy và khả năng "
                "vận hành · What-If / Checklist — phương pháp nhận diện mối "
                "nguy · Hazan — phân tích rủi ro định lượng · RISKAT · "
                "P&amp;ID — sơ đồ đường ống và thiết bị đo.")
    return ("<b>Key terms.</b> predesign / conceptual design · ISI — Inherent "
            "Safety Index (Chapter 8) · PIIS — Prototype Index of Inherent "
            "Safety (Chapter 4) · Dow F&amp;E Index · Mond Index · Hazop — "
            "Hazard and Operability Analysis · What-If / Checklist · Hazan · "
            "RISKAT · Fault tree · P&amp;ID.")


# ---------------------------------------------------------------------------
def body_vi():
    b = []

    b.append(h2("Thiếu chi tiết quá trình",
                "The absence of process details"))
    b.append(p("Việc <b>thiếu các chi tiết của quá trình làm cho công tác xem "
               "xét an toàn trở nên khó khăn</b>. Tri thức về quá trình được "
               "mở rộng song song với tiến độ thiết kế quá trình. Các phương "
               "pháp phân tích an toàn hiện có <b>cần lượng thông tin khác "
               "nhau</b>, vì thế chúng phù hợp với những giai đoạn khác nhau "
               "của thiết kế nhà máy quá trình (xem Hình 3 ở chương 3). Chẳng "
               "hạn, hầu hết các phương pháp định lượng hiện có chỉ dùng được "
               "<b>kể từ giai đoạn nhà máy pilot</b>, khi đã có đủ thông tin "
               "(Koivisto, 1996)."))

    b.append(h2("Nhận diện mối nguy đòi hỏi kiến thức, kinh nghiệm và sự "
                "linh hoạt",
                "Hazard identification demands knowledge, experience and "
                "flexibility"))
    b.append(p("<b>What-if, danh mục kiểm tra (checklists) và Hazop</b> là "
               "những công cụ nhận diện mối nguy được phổ biến rộng rãi. "
               "Tuy nhiên, như Bollinger et al. (1996) đã chỉ ra, việc dùng "
               "bất kỳ kỹ thuật nào trong số này đều <b>đòi hỏi kiến thức, "
               "kinh nghiệm và sự linh hoạt</b>. Không có một bộ câu hỏi, một "
               "bộ từ khóa hay một danh mục có tính áp đặt nào đủ để bao phủ "
               "<b>mọi quá trình, mọi mối nguy và mọi nhóm dân cư bị ảnh "
               "hưởng</b>."))
    b.append(p("Bollinger et al. cho rằng sẽ rất có lợi nếu <b>hoàn thiện các "
               "kỹ thuật đo lường định lượng, chẳng hạn các chỉ số an toàn</b>, "
               "và <b>hội tụ về một bộ chỉ số duy nhất được chấp nhận rộng "
               "rãi</b>. Đây chính là hướng mà các chương tiếp theo của luận "
               "văn đi theo."))

    b.append(h2("Ba phương pháp ở chương 4 cần quá nhiều dữ liệu",
                "The three Chapter 4 methods demand too much data"))
    b.append(p("<b>Chỉ số Dow, Chỉ số Mond và Hazop</b> được trình bày ở "
               "chương 4 đều được dùng rộng rãi để đánh giá an toàn nhà máy "
               "quá trình. Chúng bao phủ tốt những rủi ro và mối nguy hiện hữu "
               "trên một nhà máy hóa chất. Tuy nhiên, để hoàn thành các phân "
               "tích đó cần <b>rất nhiều thông tin chi tiết</b>. Ở giai đoạn "
               "sớm của thiết kế quá trình, phần lớn chi tiết cần thiết vẫn "
               "chưa được biết; vì vậy <b>các phương pháp vừa nêu không thể áp "
               "dụng trực tiếp ở chế độ đầy đủ</b>."))
    b.append(p("<b>Bảng 2</b> thể hiện thông tin được tạo ra ở từng giai đoạn "
               "thiết kế. Ở giai đoạn thiết kế sơ bộ, thông tin có được chỉ "
               "giới hạn ở <b>nguyên liệu, sản phẩm, phụ phẩm, công suất sơ "
               "bộ, các pha chính của quá trình và khoảng giá trị thô của điều "
               "kiện quá trình (nhiệt độ và áp suất)</b>. Thế nhưng chính ở "
               "giai đoạn này, <b>những thay đổi vì an toàn lại mang lại lợi "
               "ích lớn nhất</b>, bởi chưa có gì được xây dựng hay đặt hàng và "
               "nhờ đó không cần đến các cải tạo tốn kém."))
    b.append(fig(1, F.fig_c05_curves()))

    b.append(h2("Bảng 2 — Phương pháp phân tích an toàn theo giai đoạn thiết "
                "kế",
                "Table 2 — Safety analysis methods in the different phases of "
                "process plant design"))
    b.append(p("Bảng 2 của nguyên bản (tr. 27–28) liệt kê, cho mỗi giai đoạn, "
               "tài liệu được lập, thông tin có được và những phân tích an "
               "toàn phù hợp. Đáng chú ý là hàng <b>Thiết kế sơ bộ</b>: chỉ có "
               "ISI và PIIS được nêu không kèm điều kiện, còn Chỉ số Dow, "
               "Chỉ số Mond và Hazop chỉ dùng được ở mức thô."))
    b.append(_t_table2("vi"))
    b.append(note("Chi tiết cần lưu ý (nhận xét biên tập): Bảng 2 bị ngang "
                  "trang giữa tr. 27 và tr. 28. Dòng tiếp nối đầu tr. 28 "
                  "(<i>instruments etc.; operating instructions; preliminary "
                  "layout</i>) thuộc hàng <i>Basic engineering</i> và đã được "
                  "gộp vào hàng đó trong bản dịch. Nguyên bản còn lặp "
                  "<i>preliminary layout</i> ở cả cột tài liệu lẫn cột thông "
                  "tin của cùng một hàng; bản dịch giữ nguyên sự lặp này."))

    b.append(h2("Bảng 3 — Thông tin mà các phương pháp đòi hỏi",
                "Table 3 — Information required for safety analysis methods"))
    b.append(p("<b>Bảng 3</b> (tr. 29–30) trình bày yêu cầu thông tin của các "
               "phương pháp phân tích an toàn đã khảo sát ở chương 4. Đặt cạnh "
               "Bảng 2, bảng này cho thấy khoảng cách giữa <b>thứ mình có</b> "
               "và <b>thứ phương pháp chi tiết cần</b>: Dow, Mond và Hazop đòi "
               "hỏi mặt bằng, sơ đồ dòng, P&amp;ID, dữ liệu vận hành và — với "
               "Hazop — cả một đội chuyên gia."))
    b.append(_t_table3("vi"))
    b.append(note("Chi tiết cần lưu ý (nhận xét biên tập): trong nguyên bản, "
                  "cột <i>Other requirements</i> để trống ở ba phương pháp Dow, "
                  "Mond và PIIS; bản dịch ghi rõ điều đó thay vì tự bổ sung "
                  "nội dung. Hàng <i>Mond Index</i> bị ngang trang — bốn dòng "
                  "cuối (<i>physical changes; toxicity; layout distances</i>) "
                  "nằm ở tr. 30 — đã được gộp vào cùng một hàng."))
    b.append(fig(2, F.fig_c05_gap()))

    b.append(h2("Kết luận: chỉ số an toàn nội tại cho thiết kế sơ bộ",
                "Conclusion: inherent safety indices for predesign"))
    b.append(p("So sánh <b>thông tin có được</b> (Bảng 2) với <b>thông tin cần "
               "thiết</b> (Bảng 3) cho thấy các <b>phương pháp chỉ số an toàn "
               "nội tại</b>, như <b>PIIS</b> (chương 4) hay <b>ISI</b> (chương "
               "8), là những phương pháp <b>phù hợp nhất trong giai đoạn thiết "
               "kế sơ bộ</b>. So với các phương pháp chi tiết hơn, chúng có "
               "<b>yêu cầu thông tin thấp</b>. Lý do là các chỉ số này được "
               "phát triển đúng cho những tình huống mà <b>phần lớn dữ liệu về "
               "quá trình vẫn còn thiếu</b> — đồng thời rơi đúng vào giai đoạn "
               "mà một thay đổi thiết kế còn rẻ và còn có ảnh hưởng lớn nhất."))
    b.append(p("Chương 6 sẽ đi tiếp từ kết luận này sang khái niệm <b>an toàn "
               "nội tại</b>; chương 8 dựng nên <b>Chỉ số An toàn Nội tại "
               "(ISI)</b> từ chính những thông số ít ỏi mà Bảng 2 cho phép biết "
               "trước khi có P&amp;ID."))

    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 5 chiếm tr. 25–30 của VTT Publications 384 (1999): lập "
               "luận ở tr. 25–26, Bảng 2 ở tr. 27–28 và Bảng 3 ở tr. 29–30. "
               "<b>Nguyên bản không có hình vẽ nào trong chương này</b>; hai "
               "sơ đồ D và E là sơ đồ biên tập dựng lại từ văn bản và hai bảng, "
               "đã được ghi rõ trong chú thích của từng hình."))
    b.append(p("Tài liệu được trích dẫn: Koivisto (1996), Bollinger et al. "
               "(1996), Dow (1987), Lees (1996), Edwards và Lawrence (1993), "
               "Kletz (1992); danh mục đầy đủ ở phần Tài liệu tham khảo "
               "(tr. 121–129)."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. "
               "Nội dung gốc © 1999 Anna-Mari Heikkilä / VTT (VTT Publications "
               "384).</i>"))
    return "".join(b)


def body_en():
    b = []

    b.append(h2("The absence of process details",
                "Thiếu chi tiết quá trình"))
    b.append(p("<b>The absence of process details complicates the safety "
               "considerations.</b> The knowledge is extended at the same time "
               "with the progress of process design. Existing safety analysis "
               "methods <b>need a different amount of information</b>. "
               "Therefore they are suitable for different stages of the process "
               "plant design (see Figure 3 in Chapter 3). For instance, most "
               "existing quantitative methods can be used <b>first in the pilot "
               "plant phase</b> when there is enough information (Koivisto, "
               "1996)."))

    b.append(h2("Hazard identification demands knowledge, experience and "
                "flexibility",
                "Nhận diện mối nguy đòi hỏi kiến thức, kinh nghiệm và sự "
                "linh hoạt"))
    b.append(p("<b>The What-if, the checklists and Hazop</b> are well "
               "publicized hazard identification tools. But as Bollinger et "
               "al. (1996) have pointed out, the use of any of these techniques "
               "<b>demands knowledge, experience and flexibility</b>. No "
               "prescriptive set of questions or key words or list is "
               "sufficient to cover <b>all processes, hazards and all impacted "
               "populations</b>."))
    b.append(p("Bollinger et al. find that <b>refinement of the quantitative "
               "measurement techniques such as safety indices</b>, and "
               "<b>convergence to a single set of accepted indices</b>, would "
               "be beneficial. This is precisely the direction taken by the "
               "chapters that follow."))

    b.append(h2("The three Chapter 4 methods demand too much data",
                "Ba phương pháp ở chương 4 cần quá nhiều dữ liệu"))
    b.append(p("<b>The Dow and Mond Indices and Hazop</b> presented in Chapter "
               "4 are widely used for the safety evaluations of process plants. "
               "They cover well those risks and hazards existing on a chemical "
               "plant. However, <b>a lot of detailed information is needed</b> "
               "to complete those analyses. In the early stage of process "
               "design many of the required process details are still unknown. "
               "Therefore the presented safety analysis methods are <b>not "
               "directly applicable in their full mode</b>."))
    b.append(p("<b>Table 2</b> represents the information produced in "
               "different design stages. In the preliminary design phase the "
               "available information is limited to <b>raw materials, "
               "products, by-products, rough capacity, main phases of process "
               "and a rough range of process conditions (temperature and "
               "pressure)</b>. However, in this phase of a plant design the "
               "<b>changes for safety will be most profitable</b>, since "
               "nothing has been built or ordered yet and thus no expensive "
               "modifications are needed."))
    b.append(fig(1, F.fig_c05_curves()))

    b.append(h2("Table 2 — Safety analysis methods in the different phases of "
                "process plant design",
                "Bảng 2 — Phương pháp phân tích an toàn theo giai đoạn thiết "
                "kế"))
    b.append(p("Table 2 of the source (pp. 27–28) lists, for each design "
               "stage, the documents produced, the information produced and "
               "some suitable safety analyses. The <b>Predesign</b> row is the "
               "telling one: only ISI and PIIS are named without a qualifier, "
               "whereas the Dow Index, the Mond Index and Hazop are offered "
               "only in coarse mode."))
    b.append(_t_table2("en"))
    b.append(note("Detail worth noticing (editorial observation): Table 2 "
                  "breaks across pp. 27–28. The continuation row at the top of "
                  "p. 28 (<i>instruments etc.; operating instructions; "
                  "preliminary layout</i>) belongs to <i>Basic engineering</i> "
                  "and is folded into that row here. The printed table also "
                  "repeats <i>preliminary layout</i> in both the documents and "
                  "the information column of that same row; the translation "
                  "keeps the repetition."))

    b.append(h2("Table 3 — Information required for safety analysis methods",
                "Bảng 3 — Thông tin mà các phương pháp đòi hỏi"))
    b.append(p("<b>Table 3</b> (pp. 29–30) presents the information "
               "requirements of the safety analysis methods of Chapter 4. Read "
               "beside Table 2, it exposes the gap between <b>what is "
               "available</b> and <b>what the detailed methods require</b>: "
               "Dow, Mond and Hazop want plot plans, flow sheets, P&amp;IDs, "
               "operating data and — for Hazop — an expert team as well."))
    b.append(_t_table3("en"))
    b.append(note("Detail worth noticing (editorial observation): in the "
                  "source, the <i>Other requirements</i> column is empty for "
                  "Dow, Mond and PIIS; the translation marks this explicitly "
                  "rather than inventing content. The <i>Mond Index</i> row is "
                  "split by the page break — its last four items "
                  "(<i>physical changes; toxicity; layout distances</i>) sit on "
                  "p. 30 — and has been merged into a single row here."))
    b.append(fig(2, F.fig_c05_gap()))

    b.append(h2("Conclusion: inherent safety indices for predesign",
                "Kết luận: chỉ số an toàn nội tại cho thiết kế sơ bộ"))
    b.append(p("It can be seen by comparing the <b>information available</b> "
               "(Table 2) and the <b>information requirements</b> (Table 3) "
               "that the <b>inherent safety index methods</b>, such as "
               "<b>PIIS</b> (Ch. 4) or <b>ISI</b> (Ch. 8), are the <b>most "
               "suitable methods in the predesign phase</b>. They have "
               "<b>low information requirements</b> compared to more detailed "
               "methods. This is because they have been developed for the "
               "situations where <b>much of the process data is still "
               "missing</b> — and they land exactly in the phase where a design "
               "change is still cheap and still has the greatest leverage."))
    b.append(p("Chapter 6 picks up from this conclusion with the concept of "
               "<b>inherent safety</b>; Chapter 8 builds the <b>Inherent "
               "Safety Index (ISI)</b> from precisely the few parameters that "
               "Table 2 makes available before a P&amp;ID exists."))

    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 5 occupies pp. 25–30 of VTT Publications 384 (1999): "
               "the argument on pp. 25–26, Table 2 on pp. 27–28 and Table 3 "
               "on pp. 29–30. <b>The source contains no figures in this "
               "chapter</b>; Figures D and E are editorial schematics "
               "reconstructed from the prose and the two tables, and are "
               "labelled as such in their captions."))
    b.append(p("Works cited: Koivisto (1996), Bollinger et al. (1996), Dow "
               "(1987), Lees (1996), Edwards and Lawrence (1993), Kletz "
               "(1992); the full bibliography is in the References unit "
               "(pp. 121–129)."))
    b.append(p("<i>This is an unofficial translation for study purposes. "
               "Original content © 1999 Anna-Mari Heikkilä / VTT (VTT "
               "Publications 384).</i>"))
    return "".join(b)
