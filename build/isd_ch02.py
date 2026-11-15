# -*- coding: utf-8 -*-
"""Book 5, Chapter 2 — Safety (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 14–15.  The whole chapter is one
page of prose plus Figure 1 on p. 15.  That figure's labels have no Unicode
text layer in the PDF (only glyph names), so the wording was recovered by
decoding the glyph codes and checking a render of p. 15; see `isdfig.fig_f01`.
"""

from isd_common import (eq, fig, h2, h3, note, p, table, ul)
import isdfig as F

PAGES_SRC = 2           # source pages 14–15
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Safety"
TITLE_VI = "An toàn"


# ---- Source-derived tables -------------------------------------------------
def _t_losses(lang):
    """The five loss categories listed on p. 14."""
    if lang == "vi":
        hdr = ["Dạng tổn thất", "Diễn giải"]
        rows = [
            ("Hư hỏng thiết bị", "thiệt hại vật chất trên thiết bị nhà máy"),
            ("Mất sản xuất", "gián đoạn hoặc sụt giảm sản lượng"),
            ("Thiệt hại môi trường", "tác động ra bên ngoài ranh giới nhà máy"),
            ("Thương tích", "tổn thất về người, không tử vong"),
            ("Tử vong", "tổn thất nặng nhất về người"),
        ]
        cap = ("Các dạng tổn thất có thể xảy ra trong một nhà máy quá trình "
               "(nguyên bản tr. 14).")
    else:
        hdr = ["Kind of loss", "Gloss"]
        rows = [
            ("Damage to equipment", "physical damage to plant equipment"),
            ("Loss of production", "interrupted or reduced output"),
            ("Environmental damage", "impact beyond the plant boundary"),
            ("Injury", "harm to people, non-fatal"),
            ("Death", "the most severe harm to people"),
        ]
        cap = "Kinds of loss in a process plant (source p. 14)."
    return table(hdr, rows, caption=cap, cls="tbl wide")


def _t_methods(lang):
    """The eight labels of Figure 1, in top-to-bottom order."""
    if lang == "vi":
        hdr = ["Thứ tự", "Phương pháp nhận diện (trái)",
               "Phương pháp đánh giá (phải)"]
        rows = [
            ("1", "Hiển nhiên — <i>Obvious</i>", "Hiển nhiên — <i>Obvious</i>"),
            ("2", "Xem điều gì xảy ra — <i>See what happens</i>",
             "Kinh nghiệm — <i>Experience</i>"),
            ("3", "Danh mục kiểm tra — <i>Check list</i>",
             "Quy tắc thực hành — <i>Codes of practice</i>"),
            ("4", "Hazop — phân tích mối nguy và khả năng vận hành",
             "Phân tích mối nguy — <i>Hazard analysis (Hazan)</i>"),
        ]
        cap = ("Các nhãn của Hình 1 theo thứ tự từ trên xuống; thuật ngữ gốc được "
               "giữ nguyên để đối chiếu với bản vẽ. Hai cột không phải ánh xạ một-một.")
    else:
        hdr = ["Order", "Identifying hazards (left)", "Assessing hazards (right)"]
        rows = [
            ("1", "Obvious", "Obvious"),
            ("2", "See what happens", "Experience"),
            ("3", "Check list", "Codes of practice"),
            ("4", "Hazop", "Hazard analysis (Hazan)"),
        ]
        cap = ("The labels of Figure 1 in top-to-bottom order; source wording kept "
               "verbatim. The two columns are not a one-to-one mapping.")
    return table(hdr, rows, caption=cap, cls="tbl wide")


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 2.</b> safety — an toàn · hazard — mối nguy · "
                "risk — rủi ro · loss — tổn thất · consequence — hệ quả · "
                "probability — xác suất · accident prevention — phòng ngừa tai nạn · "
                "Hazop — phân tích mối nguy và khả năng vận hành · Hazan — phân tích "
                "mối nguy · check list — danh mục kiểm tra · codes of practice — quy tắc "
                "thực hành · limitation of effects — giới hạn hệ quả.")
    return ("<b>Key terms.</b> safety · hazard — a condition with the potential to "
            "cause injury or damage · risk — the possibility of loss · consequence / "
            "probability — the two measurable parameters of risk · accident prevention · "
            "Hazop / Hazan · check list · codes of practice · limitation of effects.")


# ---------------------------------------------------------------------------
def body_vi():
    b = []

    b.append(h2("Khái niệm an toàn", "The concept of safety"))
    b.append(p("Theo Kharbanda và Stallworthy (1988), <b>an toàn là một khái niệm bao "
               "trùm nhận diện mối nguy, đánh giá rủi ro và phòng ngừa tai nạn</b>. An "
               "toàn phải luôn được đặt lên hàng đầu và giữ nguyên vị trí đó, bất chấp "
               "chi phí. Thiết kế tốt và sự tính trước thường có thể mang lại mức an "
               "toàn cao hơn với chi phí thấp hơn."))
    b.append(p("Định nghĩa này gom ba hoạt động vào một khái niệm: trước hết phải biết "
               "mối nguy ở đâu, sau đó ước lượng rủi ro do nó gây ra, rồi mới tìm cách "
               "ngăn tai nạn. Chương này thiết lập các định nghĩa nền tảng — an toàn, "
               "rủi ro, mối nguy — để chương 3 đi vào việc đánh giá an toàn."))

    b.append(h2("Rủi ro và hai thông số đo được",
                "Risk and its two measurable parameters"))
    b.append(p("Thước đo an toàn được biết đến nhiều nhất là <b>rủi ro</b>, được định "
               "nghĩa là khả năng xảy ra tổn thất (Taylor, 1994). Vấn đề về nhận thức "
               "rủi ro có thể được nhìn nhận như một sự thất bại của truyền thông và của "
               "quản lý (Kharbanda và Stallworthy, 1988). Theo Chartered Insurance "
               "Institute (1974), rủi ro là <b>xác suất toán học của một sự kiện không "
               "mong muốn được xác định, xảy ra trong những hoàn cảnh xác định hoặc "
               "trong một khoảng thời gian xác định</b>."))
    b.append(p("Trong một nhà máy quá trình, tổn thất có thể là hư hỏng thiết bị, mất "
               "sản xuất, thiệt hại môi trường, cũng như thương tích hoặc tử vong. Rủi ro "
               "liên quan đến <b>hai thông số đo được</b> (Taylor, 1994): <b>hệ quả</b> "
               "(consequence) và <b>xác suất</b> (probability). Một số sự kiện có khả "
               "năng xảy ra cao hơn các sự kiện khác, nhưng hệ quả duy nhất của một "
               "chuỗi sự kiện thì không thể dự đoán được."))
    b.append(_t_losses("vi"))

    b.append(h2("Mối nguy", "Hazards"))
    b.append(p("<b>Mối nguy là một điều kiện có tiềm năng gây thương tích hoặc hư hỏng</b> "
               "(Heinrich, 1968). Một quá trình hóa chất thường có nhiều mối nguy tiềm "
               "ẩn, và mỗi mối nguy trong số đó đều tác động đến rủi ro tổng của quá "
               "trình (Hendershot, 1995):"))
    b.append(ul([
        "độc tính và khả năng phản ứng của nguyên liệu và sản phẩm trung gian;",
        "năng lượng giải phóng từ các phản ứng hóa học;",
        "nhiệt độ cao;",
        "áp suất cao;",
        "lượng vật liệu được sử dụng, v.v.",
    ]))
    b.append(p("Theo đuổi an toàn phần lớn là công việc <b>nhận diện mối nguy</b>, "
               "<b>loại bỏ chúng ở nơi có thể</b>, hoặc nếu không được thì <b>bảo vệ "
               "khỏi hệ quả của chúng</b>. Thường phải có đồng thời hai mối nguy mới "
               "gây nên một tai nạn lớn."))

    b.append(h2("Hình 1 — nhận diện và đánh giá mối nguy",
                "Figure 1 — identifying and assessing hazards"))
    b.append(p("Trong Hình 1, Kletz (1992a) trình bày các kỹ thuật <b>nhận diện mối "
               "nguy</b> và các kỹ thuật <b>đánh giá</b> những mối nguy đó. Từ hộp "
               "<i>HAZARDS</i> ở giữa, bốn phương pháp tỏa sang trái và bốn phương "
               "pháp tỏa sang phải; đầu mũi tên hướng ra ngoài, từ mối nguy tới từng "
               "cách tiếp cận. Hai nhánh cùng bắt đầu từ mức hiển nhiên rồi đi dần "
               "tới các phương pháp có cấu trúc hơn — danh mục kiểm tra, Hazop, quy "
               "tắc thực hành và phân tích mối nguy định lượng (Hazan)."))
    b.append(fig(1, F.fig_f01()))
    b.append(_t_methods("vi"))
    b.append(note("Lưu ý kỹ thuật: phần chữ trong Hình 1 của nguyên bản không có lớp "
                  "văn bản Unicode — tệp PDF chỉ lưu các tên glyph dạng <i>/G30/G48/…</i>. "
                  "Các nhãn trong bản vẽ lại được phục hồi bằng cách giải mã mã glyph và "
                  "đối chiếu với ảnh render trang 15, nên vẫn giữ nguyên cách viết của "
                  "Kletz, kể cả <i>Check list</i> và <i>Hazop</i>."))

    b.append(h2("Tối thiểu hóa rủi ro toàn quá trình",
                "Minimising total process risk"))
    b.append(p("Trong thực tế, mục đích chính của thiết kế nhà máy quá trình là "
               "<b>tối thiểu hóa rủi ro tổng của quá trình</b> nhằm giới hạn hệ quả. Ở "
               "đây rủi ro là <b>tích của xác suất xảy ra sự cố và hệ quả có thể có của "
               "sự cố đó</b> — một cách viết gọn của định nghĩa hai thông số nêu trên:"))
    b.append(eq("<i>R</i> = <i>P</i> × <i>C</i>"))
    b.append(p("với <i>P</i> là xác suất xảy ra sự cố và <i>C</i> là hệ quả có thể có "
               "của sự cố. Công thức này là cách trình bày biên tập lại câu văn của "
               "nguyên bản, không phải một phương trình được đánh số trong sách."))
    b.append(p("Chính <b>việc giới hạn hệ quả bằng các nguyên lý an toàn nội tại</b> là "
               "điều được đánh giá trong luận văn này. Nói cách khác, thay vì chỉ giảm "
               "<i>P</i> bằng hệ thống bảo vệ lắp thêm, cách tiếp cận của tác giả tác "
               "động vào chính nguồn gốc của <i>C</i> — hóa chất, tồn lượng và cấu "
               "trúc quá trình — ngay từ giai đoạn thiết kế sơ bộ."))
    b.append(note("Điểm mấu chốt: an toàn = nhận diện mối nguy + đánh giá rủi ro + "
                  "phòng ngừa tai nạn; rủi ro = xác suất × hệ quả; mối nguy là điều "
                  "kiện có tiềm năng gây hại. Chương 1 đã chỉ ra vì sao các hệ thống bổ "
                  "sung muộn làm tăng chi phí vòng đời — chương 3 sẽ rà soát cách an "
                  "toàn được đánh giá, trước khi chương 6 định nghĩa an toàn nội tại."))

    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 2 chiếm tr. 14–15 của VTT Publications 384 (1999): toàn bộ văn "
               "bản nằm trên tr. 14, còn Hình 1 được xếp riêng trên tr. 15. Các tài "
               "liệu được trích dẫn trong chương gồm Kharbanda và Stallworthy (1988), "
               "Taylor (1994), Chartered Insurance Institute (1974), Heinrich (1968), "
               "Hendershot (1995) và Kletz (1992a); danh mục đầy đủ nằm ở phần Tài liệu "
               "tham khảo (tr. 121–129)."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội "
               "dung gốc © 1999 Anna-Mari Heikkilä / VTT (VTT Publications 384).</i>"))
    return "".join(b)


def body_en():
    b = []

    b.append(h2("The concept of safety", "Khái niệm an toàn"))
    b.append(p("According to Kharbanda and Stallworthy (1988), <b>safety is a concept "
               "covering hazard identification, risk assessment and accident "
               "prevention</b>. Safety should always come first and remain so despite "
               "of costs. Good design and forethought can often bring increased safety "
               "at less cost."))
    b.append(p("The definition folds three activities into one idea: first know where "
               "the hazards are, then estimate the risk they create, and only then set "
               "out to prevent the accident. This chapter establishes the working "
               "definitions — safety, risk, hazard — that Chapter 3 builds on when it "
               "turns to the evaluation of safety."))

    b.append(h2("Risk and its two measurable parameters",
                "Rủi ro và hai thông số đo được"))
    b.append(p("The best known measure for safety is <b>risk</b>, defined as the "
               "possibility of loss (Taylor, 1994). The problem of awareness of risk "
               "can be seen as one of failure of communication and of mismanagement "
               "(Kharbanda and Stallworthy, 1988). Risk by the Chartered Insurance "
               "Institute (1974) is <b>the mathematical probability of a specified "
               "undesired event occurring, in specified circumstances or within a "
               "specified period</b>."))
    b.append(p("In a process plant the losses may be such as damage to equipment, a "
               "loss of production or an environmental damage as well as an injury or "
               "a death. Risk involves <b>two measurable parameters</b> (Taylor, 1994): "
               "<b>consequence</b> and <b>probability</b>. Some events are more "
               "probable to occur than others, but a unique consequence of the sequence "
               "of events cannot be predicted."))
    b.append(_t_losses("en"))

    b.append(h2("Hazards", "Mối nguy"))
    b.append(p("<b>A hazard is a condition with the potential of causing an injury or "
               "a damage</b> (Heinrich, 1968). A chemical process normally has a "
               "number of potential hazards, each of which impacts the overall process "
               "risk (Hendershot, 1995):"))
    b.append(ul([
        "raw material and intermediate toxicity and reactivity;",
        "energy release from chemical reactions;",
        "high temperatures;",
        "high pressures;",
        "the quantity of material used, etc.",
    ]))
    b.append(p("A pursuit of safety is largely a matter of <b>identifying hazards</b>, "
               "<b>eliminating them where possible</b> or otherwise <b>protecting "
               "against their consequences</b>. Often two hazards need to be present "
               "simultaneously to cause a major accident."))

    b.append(h2("Figure 1 — identifying and assessing hazards",
                "Hình 1 — nhận diện và đánh giá mối nguy"))
    b.append(p("In Figure 1 Kletz (1992a) has presented the techniques for "
               "<b>identifying hazards</b> and the techniques for <b>assessing</b> those "
               "hazards. From the central <i>HAZARDS</i> box four methods fan out to "
               "the left and four to the right; the arrowheads point outwards, from the "
               "hazard towards each approach. Both branches start from what is obvious "
               "and move towards more structured methods — check lists, Hazop, codes of "
               "practice and quantitative hazard analysis (Hazan)."))
    b.append(fig(1, F.fig_f01()))
    b.append(_t_methods("en"))
    b.append(note("Technical note: the lettering in the source Figure 1 has no Unicode "
                  "text layer — the PDF stores only glyph names such as "
                  "<i>/G30/G48/…</i>. The labels in this redraw were recovered by "
                  "decoding those glyph codes and cross-checking against a render of "
                  "p. 15, so Kletz's wording is kept verbatim, including "
                  "<i>Check list</i> and <i>Hazop</i>."))

    b.append(h2("Minimising total process risk",
                "Tối thiểu hóa rủi ro toàn quá trình"))
    b.append(p("In practice the main purpose of process plant design is to <b>minimize "
               "the total process risk for the limitation of effects</b>. Here risk is "
               "<b>the product of the probability of an incident to happen and the "
               "possible consequences of that incident</b> — a compact rendering of the "
               "two-parameter definition above:"))
    b.append(eq("<i>R</i> = <i>P</i> × <i>C</i>"))
    b.append(p("where <i>P</i> is the probability of the incident and <i>C</i> its "
               "possible consequences. This is an editorial restatement of the source "
               "sentence, not a numbered equation in the book."))
    b.append(p("It is precisely <b>the limitation of effects by the means of inherent "
               "safety principles</b> that is evaluated in this thesis. In other words, "
               "rather than reducing only <i>P</i> with add-on protective systems, the "
               "author's approach acts on the origin of <i>C</i> itself — the chemicals, "
               "the inventory and the process structure — at the earliest design stage."))
    b.append(note("In short: safety = hazard identification + risk assessment + "
                  "accident prevention; risk = probability × consequence; a hazard is "
                  "a condition with the potential to cause harm. Chapter 1 showed why "
                  "late add-on systems raise lifetime costs; Chapter 3 reviews how "
                  "safety is evaluated, before Chapter 6 defines inherent safety."))

    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 2 occupies pp. 14–15 of VTT Publications 384 (1999): all of the "
               "prose is on p. 14, with Figure 1 placed on its own on p. 15. The works "
               "cited in the chapter are Kharbanda and Stallworthy (1988), Taylor "
               "(1994), the Chartered Insurance Institute (1974), Heinrich (1968), "
               "Hendershot (1995) and Kletz (1992a); the full bibliography is in the "
               "References unit (pp. 121–129)."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © 1999 Anna-Mari Heikkilä / VTT (VTT Publications 384).</i>"))
    return "".join(b)
