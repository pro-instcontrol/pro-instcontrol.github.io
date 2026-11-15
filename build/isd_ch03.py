# -*- coding: utf-8 -*-
"""Book 5, Chapter 3 — Evaluation of Safety (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 16–18.  Two source figures:
Figure 2 (p. 17, Suokas & Kakko 1993 safety/risk analysis flowchart) and
Figure 3 (p. 18, CCPS 1992 9x12 techniques-vs-life-cycle dot matrix).  Both
were redrawn as vectors in `isdfig.py` from page renders.

Note: the printed p. 16 repeats the "Some safety analysis techniques ..."
paragraph twice (a printing error in the original).  The translation keeps it
once; the duplication is recorded in the source note below.
"""

from isd_common import (fig, h2, h3, note, p, table, ul)
import isdfig as F

PAGES_SRC = 3           # source pages 16–18
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Evaluation of Safety"
TITLE_VI = "Đánh giá an toàn"


# ---- Source-derived tables -------------------------------------------------
def _t_steps(lang):
    """The eight boxes of Figure 2, in main-flow order."""
    steps = [
        ("SYSTEM DEFINITION", "Định nghĩa hệ thống"),
        ("HAZARD IDENTIFICATION", "Nhận diện mối nguy"),
        ("ACCIDENT MODELLING", "Mô hình hóa tai nạn"),
        ("ESTIMATION OF ACCIDENT FREQUENCIES", "Ước lượng tần suất tai nạn"),
        ("ESTIMATION OF ACCIDENT CONSEQUENCES", "Ước lượng hệ quả tai nạn"),
        ("RISK ESTIMATION", "Ước lượng rủi ro"),
        ("DOCUMENTATION OF THE RESULTS", "Lập hồ sơ kết quả"),
        ("SYSTEM CHANGES", "Thay đổi hệ thống (nhánh phản hồi)"),
    ]
    if lang == "vi":
        hdr = ["Bước", "Nhãn trong Hình 2", "Nghĩa tiếng Việt"]
        cap = ("Tám hộp của Hình 2 theo trình tự dòng chính; <i>SYSTEM CHANGES</i> là "
               "nhánh phản hồi, không phải một bước tuần tự.")
    else:
        hdr = ["Step", "Label in Figure 2", "Vietnamese gloss"]
        cap = ("The eight boxes of Figure 2 in main-flow order; <i>SYSTEM CHANGES</i> is "
               "the feedback branch, not a sequential step.")
    rows = [(str(i + 1), en, vi) for i, (en, vi) in enumerate(steps)]
    return table(hdr, rows, caption=cap, cls="tbl wide")


def _t_techniques(lang):
    """The twelve technique labels of Figure 3, with expansions."""
    rows = [
        ("Safety Review", "Safety review", "Rà soát an toàn"),
        ("Checklist", "Check list review", "Danh mục kiểm tra"),
        ("Relative Ranking", "Relative ranking of hazards", "Xếp hạng tương đối"),
        ("PHA", "Preliminary Hazard Analysis", "Phân tích mối nguy sơ bộ"),
        ("What-If", "What-if analysis", "Phân tích «điều gì nếu»"),
        ("What-if/Checklist", "What-if combined with a check list",
         "«Điều gì nếu» kết hợp danh mục kiểm tra"),
        ("HAZOP", "Hazard and Operability Study (Ch. 4)",
         "Phân tích mối nguy và khả năng vận hành"),
        ("FMEA", "Failure Modes and Effects Analysis",
         "Phân tích dạng hỏng và ảnh hưởng"),
        ("Fault Tree", "Fault tree analysis", "Phân tích cây sự cố"),
        ("Event Tree", "Event tree analysis", "Phân tích cây sự kiện"),
        ("CCA", "Cause-Consequence Analysis", "Phân tích nguyên nhân – hệ quả"),
        ("HRA", "Human Reliability Analysis", "Phân tích độ tin cậy con người"),
    ]
    if lang == "vi":
        hdr = ["Ký hiệu", "Tiếng Anh (tên đầy đủ)", "Nghĩa tiếng Việt"]
        cap = ("Mười hai kỹ thuật ở Hình 3 (CCPS, 1992); các tên viết tắt được giải "
               "nghĩa theo Bảng ký hiệu tr. 9–10 và chương 4.")
    else:
        hdr = ["Label", "Full name / expansion", "Vietnamese gloss"]
        cap = ("The twelve techniques of Figure 3 (CCPS, 1992); abbreviations expanded "
               "from the List of symbols (pp. 9–10) and Chapter 4.")
    return table(hdr, rows, caption=cap, cls="tbl wide")


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 3.</b> safety evaluation — đánh giá an toàn · "
                "safety analysis — phân tích an toàn · accident contributor — yếu tố góp "
                "phần gây tai nạn · preventative action — hành động phòng ngừa · "
                "risk estimation — ước lượng rủi ro · accident modelling — mô hình hóa tai "
                "nạn · plant localization — lựa chọn địa điểm nhà máy · life cycle — vòng "
                "đời · safety standard — tiêu chuẩn an toàn · HAZOP / PHA / FMEA / CCA / HRA.")
    return ("<b>Key terms.</b> safety evaluation · safety analysis — a systematic "
            "examination of structure and functions · accident contributor · preventative "
            "action · risk estimation · accident modelling · plant localization · plant "
            "life cycle · analysis levels · safety standards · HAZOP / PHA / FMEA / CCA / HRA.")


# ---------------------------------------------------------------------------
def body_vi():
    b = []

    b.append(h2("Mức an toàn bắt buộc", "A required level of safety"))
    b.append(p("An toàn của một nhà máy quá trình phải đạt một <b>mức bắt buộc nhất "
               "định</b>. Đó là do các yêu cầu pháp luật chung, hình ảnh công ty, và cả lý "
               "do kinh tế: một nhà máy không an toàn không thể có lợi nhuận vì mất sản "
               "xuất và mất vốn. Vì vậy <b>an toàn phải ảnh hưởng đến các quyết định thiết "
               "kế ngay từ những khoảnh khắc đầu tiên của dự án</b>."))
    b.append(p("Đây chính là điểm mà chương 1 đã đặt ra và chương 2 đã định nghĩa: nếu "
               "an toàn chỉ được xét khi thiết kế đã gần xong, mọi biện pháp còn lại đều là "
               "hệ thống lắp thêm, với chi phí vòng đời đi kèm."))

    b.append(h2("Phân tích an toàn", "Safety analysis"))
    b.append(p("Đánh giá an toàn thường được thực hiện bằng <b>các phương pháp phân tích "
               "an toàn</b>. Phân tích an toàn là <b>sự khảo sát có hệ thống cấu trúc và "
               "chức năng của một hệ thống quá trình</b>, nhằm nhận diện các yếu tố tiềm "
               "ẩn góp phần gây tai nạn, đánh giá rủi ro do chúng tạo ra và tìm ra các "
               "biện pháp giảm rủi ro (Koivisto, 1996)."))
    b.append(p("Điều quan trọng nhất là <b>toàn bộ vòng đời của nhà máy quá trình đều có "
               "thể được đánh giá về an toàn</b>. Các phân tích an toàn và rủi ro ước lượng "
               "xác suất để một rủi ro xuất hiện, và các quyết định về hành động phòng ngừa "
               "cần thiết được đưa ra <b>sau khi có kết quả phân tích</b>. Mục tiêu của "
               "ước lượng rủi ro là hỗ trợ ra quyết định về <b>địa điểm đặt nhà máy, các "
               "phương án quá trình thay thế và mặt bằng nhà máy</b>."))
    b.append(p("Suokas và Kakko (1993) đã trình bày các bước của một phân tích an toàn và "
               "rủi ro trong Hình 2. Phân tích an toàn và rủi ro có thể tiến hành ở "
               "<b>nhiều mức độ</b>; mức độ dừng phân tích phụ thuộc vào <b>độ phức tạp "
               "của đối tượng cần phân tích và tiềm năng rủi ro</b>."))

    b.append(h2("Hình 2 — các bước phân tích an toàn và rủi ro",
                "Figure 2 — steps of a safety and risk analysis"))
    b.append(p("Sơ đồ đi từ định nghĩa hệ thống xuống nhận diện mối nguy, rồi mô hình hóa "
               "tai nạn. Từ đó dòng tách thành <b>hai nhánh song song</b> — ước lượng tần "
               "suất tai nạn và ước lượng hệ quả tai nạn — trước khi gộp lại ở ước lượng "
               "rủi ro và khép kín bằng lập hồ sơ kết quả. Ở bên trái, hộp <i>SYSTEM "
               "CHANGES</i> (thay đổi hệ thống) nhận các mũi tên phản hồi từ những giai "
               "đoạn trung gian, rồi vừa đưa ngược về định nghĩa hệ thống, vừa đi tới hồ "
               "sơ kết quả: kết quả phân tích làm thay đổi chính hệ thống đang được phân "
               "tích."))
    b.append(fig(2, F.fig_f02()))
    b.append(_t_steps("vi"))

    b.append(h2("Hình 3 — kỹ thuật đánh giá mối nguy theo vòng đời",
                "Figure 3 — techniques over the plant life cycle"))
    b.append(p("Một số kỹ thuật phân tích an toàn và cách dùng điển hình của chúng được "
               "trình bày trong Hình 3 theo CCPS (1992). Có thể thấy <b>các phương pháp "
               "đánh giá mối nguy này cùng nhau phủ khá tốt nhu cầu của toàn bộ vòng đời "
               "nhà máy quá trình</b>. Tuy nhiên đây <b>không phải một danh sách đầy đủ</b> "
               "— còn những phương pháp khác có thể áp dụng, như sẽ thấy ở chương 5."))
    b.append(fig(3, F.fig_f03()))
    b.append(_t_techniques("vi"))
    b.append(note("Đọc ma trận (nhận xét biên tập, suy từ Hình 3 chứ không phải văn bản "
                  "của tác giả): chấm đen là <b>thường dùng</b>, chấm rỗng là <b>ít dùng "
                  "hoặc không phù hợp</b>. Trong 12 kỹ thuật, chỉ <i>What-If</i> được đánh "
                  "dấu thường dùng ở cả 9 giai đoạn; ngược lại, chỉ giai đoạn <i>Mở rộng "
                  "hoặc cải hoán</i> (Expansion or Modification) dùng phổ biến cả 12 kỹ "
                  "thuật. Hai đầu của vòng đời — nghiên cứu phát triển và dừng hoạt động — "
                  "là nơi ít kỹ thuật được dùng thường xuyên nhất (3 và 4 trên 12)."))

    b.append(h2("Tiêu chuẩn an toàn", "Safety standards"))
    b.append(p("Cũng có nhiều <b>tiêu chuẩn về an toàn</b> ghi lại kinh nghiệm và quy định "
               "quy trình chuẩn cho nhiều tình huống lặp lại, tương tự nhau. Nhìn chung "
               "chúng phù hợp với các quy định địa phương và quốc gia, cũng như với thực "
               "hành chuẩn của các hiệp hội kỹ thuật lớn (Koivisto, 1996)."))
    b.append(p("Khó khăn khi dùng tiêu chuẩn nằm ở:"))
    b.append(ul([
        "<b>số lượng có hạn</b> của các tiêu chuẩn;",
        "<b>chính bản chất của chúng</b> là kinh nghiệm đã được chấp nhận rộng rãi và đã "
        "được thiết lập — vì thế <b>các phát minh mới không thể đáp ứng ngay</b> các tiêu "
        "chuẩn này;",
        "các vấn đề phát sinh khi người ta <b>phụ thuộc quá mức</b> hoặc đặt <b>kỳ vọng "
        "phi lý</b> vào tiêu chuẩn an toàn.",
    ]))
    b.append(p("Giới hạn này là một phần của lý do luận văn tìm đến một chỉ số dùng được "
               "ngay trong thiết kế sơ bộ: khi quá trình còn mới, kinh nghiệm đã chuẩn hóa "
               "chưa đủ để làm căn cứ đánh giá."))
    b.append(note("Điểm mấu chốt: an toàn phải được đưa vào quyết định thiết kế ngay từ "
                  "đầu; phân tích an toàn là khảo sát có hệ thống, có thể dừng ở nhiều mức "
                  "tùy độ phức tạp và tiềm năng rủi ro; Hình 2 cho quy trình, Hình 3 cho "
                  "bản đồ kỹ thuật theo vòng đời; tiêu chuẩn hóa kinh nghiệm thì hữu ích "
                  "nhưng có hạn. Chương 4 sẽ lần lượt xem Dow, Mond, Hazop và PIIS, và "
                  "chương 5 nêu các hạn chế của chúng trong thiết kế sơ bộ — chính là "
                  "khoảng trống mà Chỉ số An toàn Nội tại lấp đầy."))

    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 3 chiếm tr. 16–18 của VTT Publications 384 (1999): văn bản chính "
               "ở tr. 16, Hình 2 và đoạn về tiêu chuẩn ở tr. 17, Hình 3 ở tr. 18. Ở bản in "
               "gốc, đoạn bắt đầu bằng <i>“Some safety analysis techniques and their typical "
               "use…”</i> được <b>in lặp hai lần</b> trên tr. 16; bản dịch chỉ giữ một lần. "
               "Cả hai hình đều được vẽ lại dạng vector từ ảnh render các trang gốc, với "
               "nhãn tiếng Anh giữ nguyên theo nguyên bản."))
    b.append(p("Tài liệu được trích dẫn: Koivisto (1996), Suokas và Kakko (1993), CCPS "
               "(1992); danh mục đầy đủ ở phần Tài liệu tham khảo (tr. 121–129)."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội "
               "dung gốc © 1999 Anna-Mari Heikkilä / VTT (VTT Publications 384).</i>"))
    return "".join(b)


def body_en():
    b = []

    b.append(h2("A required level of safety", "Mức an toàn bắt buộc"))
    b.append(p("It is required that the safety of a process plant fulfills a certain "
               "<b>required level</b>. This is because of general legal requirements, "
               "company image, and also due to economic reasons, since an unsafe plant "
               "cannot be profitable due to losses of production and capital. Thus "
               "<b>safety should influence design decisions from the first moments of the "
               "design project</b>."))
    b.append(p("This is exactly the point Chapter 1 raised and Chapter 2 defined: if safety "
               "is only considered once the design is nearly finished, the only measures "
               "left are add-on systems, with the lifetime costs they bring."))

    b.append(h2("Safety analysis", "Phân tích an toàn"))
    b.append(p("Safety evaluation is usually done by <b>safety analyses methods</b>. "
               "Safety analysis is <b>a systematic examination of the structure and "
               "functions of a process system</b> aimed at identifying potential accident "
               "contributors, evaluating the risk presented by them and finding "
               "risk-reducing measures (Koivisto, 1996)."))
    b.append(p("It is most important that <b>the whole life cycle of a process plant can be "
               "evaluated on safety</b>. Safety and risk analyses evaluate the probability "
               "of a risk to appear, and the decisions of necessary preventative actions are "
               "made <b>after results of an analysis</b>. The aim of the risk estimation is "
               "to support the decision making on <b>plant localization, alternative "
               "processes and plant layout</b>."))
    b.append(p("Suokas and Kakko (1993) have introduced steps of a safety and risk "
               "analysis in Figure 2. The safety and risk analysis can be done on "
               "<b>several levels</b>. The level on which the analysis is stopped depends "
               "on <b>the complexity of the object for analysis and the risk potential</b>."))

    b.append(h2("Figure 2 — steps of a safety and risk analysis",
                "Hình 2 — các bước phân tích an toàn và rủi ro"))
    b.append(p("The flow runs from system definition down through hazard identification "
               "to accident modelling. There it splits into <b>two parallel branches</b> — "
               "estimation of accident frequencies and estimation of accident consequences "
               "— before converging on risk estimation and closing with documentation of "
               "the results. On the left, the <i>SYSTEM CHANGES</i> box receives feedback "
               "arrows from intermediate stages and then both loops back to system "
               "definition and forwards to documentation: the results of the analysis "
               "change the very system being analysed."))
    b.append(fig(2, F.fig_f02()))
    b.append(_t_steps("en"))

    b.append(h2("Figure 3 — techniques over the plant life cycle",
                "Hình 3 — kỹ thuật đánh giá mối nguy theo vòng đời"))
    b.append(p("Some safety analysis techniques and their typical use are presented in "
               "Figure 3 as given by CCPS (1992). It can be seen that together these hazard "
               "evaluation methods <b>cover well the needs of the life cycle of a process "
               "plant</b>. However this is <b>not a complete list</b> but also some other "
               "methods are applicable as seen in Chapter 5."))
    b.append(fig(3, F.fig_f03()))
    b.append(_t_techniques("en"))
    b.append(note("Reading the matrix (editorial observation derived from Figure 3, not "
                  "from the author's prose): a filled dot means <b>commonly used</b>, a "
                  "hollow dot <b>rarely used or inappropriate</b>. Of the twelve "
                  "techniques, only <i>What-If</i> is marked commonly used in all nine "
                  "phases; conversely, only <i>Expansion or Modification</i> commonly uses "
                  "all twelve. The two ends of the life cycle — research &amp; development and "
                  "decommissioning — have the fewest commonly used techniques (3 and 4 of "
                  "12)."))

    b.append(h2("Safety standards", "Tiêu chuẩn an toàn"))
    b.append(p("There also exist many <b>standards on safety</b> that document the "
               "experience and define standard procedure for many recurring and similar "
               "situations. They generally conform to local and national regulations as "
               "well as to the standard practices of major engineering societies "
               "(Koivisto, 1996)."))
    b.append(p("Difficulties in the use of standards are:"))
    b.append(ul([
        "their <b>limited number</b>;",
        "their <b>very nature</b>, which is commonly accepted established experience — "
        "obviously <b>new inventions cannot immediately meet these standards</b>;",
        "problems that arise when <b>undue reliance and unreasonable expectations</b> "
        "have been created regarding safety standards.",
    ]))
    b.append(p("That limitation is part of why the thesis looks for an index usable at the "
               "very beginning of design: when a process is new, standardized experience "
               "is not yet available as a basis for evaluation."))
    b.append(note("In short: safety must enter design decisions from the first moment; "
                  "safety analysis is a systematic examination that can stop at several "
                  "levels depending on complexity and risk potential; Figure 2 gives the "
                  "process, Figure 3 the technique map across the life cycle; standards "
                  "codify experience but have limits. Chapter 4 reviews Dow, Mond, Hazop "
                  "and PIIS, and Chapter 5 sets out their limitations in conceptual "
                  "design — the gap the Inherent Safety Index is built to fill."))

    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 3 occupies pp. 16–18 of VTT Publications 384 (1999): the main "
               "prose is on p. 16, Figure 2 and the standards paragraph on p. 17, and "
               "Figure 3 on p. 18. In the printed original, the paragraph beginning "
               "<i>“Some safety analysis techniques and their typical use…”</i> is "
               "<b>duplicated</b> on p. 16; the translation keeps it once. Both figures "
               "were redrawn as vectors from page renders, with the English labels kept "
               "verbatim from the source."))
    b.append(p("Works cited: Koivisto (1996), Suokas and Kakko (1993), CCPS (1992); the "
               "full bibliography is in the References unit (pp. 121–129)."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © 1999 Anna-Mari Heikkilä / VTT (VTT Publications 384).</i>"))
    return "".join(b)
