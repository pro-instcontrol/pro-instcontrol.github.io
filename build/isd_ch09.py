# -*- coding: utf-8 -*-
"""Book 5, Chapter 9 — The Weighting between Subindices of the Inherent
Safety Index (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 60–61.  The chapter explains why
and how the subindices can be weighted (Equations 3–5 with weighting factors,
in-house standard weighting), and presents Table 8 — the subindex symbols and
score ranges — together with their rationale from the expert inquiry of
Edwards et al. (1996) summarised by Lawrence (1996).
"""

from isd_common import eq, fig, h2, note, p, table
import isdfig as F

PAGES_SRC = 2            # source pages 60–61
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "The Weighting between Subindices"
TITLE_VI = "Trọng số giữa các chỉ số thành phần"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 9.</b> trọng số (weighting factor) — hệ "
                "số nhân điều chỉnh điểm chuẩn của chỉ số thành phần · phạm vi "
                "điểm (score domain/range) — khoảng 0–N của từng chỉ số · điều "
                "trả lời chuyên gia — khảo sát 8 chuyên gia an toàn quá trình "
                "(Edwards và cộng sự, 1996; tổng hợp bởi Lawrence, 1996) · "
                "Isbl / Osbl — trong/ngoài giới hạn thiết bị (inside/outside "
                "battery limits) · trọng số nội bộ chuẩn hóa (standardized "
                "in-house weighting).")
    return ("<b>Key terms.</b> weighting factor — a multiplier adjusting the "
            "standard score of a subindex · score domain/range — the 0–N "
            "interval of each subindex · expert inquiry — 8 process-safety "
            "experts surveyed (Edwards et al., 1996; summarised by Lawrence, "
            "1996) · Isbl / Osbl — inside/outside battery limits · "
            "standardized in-house weighting.")


# ---------------------------------------------------------------------------
# Source Table 8 (p. 61): the inherent safety subindices and their scores.
_D = '<span style="color:#bbb">—</span>'

_T8 = [
    "Chỉ số an toàn nội tại hóa học, I<sub>CI</sub>",
    ("Nhiệt phản ứng chính · Heat of main reaction", "I<sub>RM</sub>", "0–4"),
    ("Nhiệt phản ứng phụ · Heat of side reaction, max", "I<sub>RS</sub>", "0–4"),
    ("Tương tác hóa học · Chemical interaction", "I<sub>INT</sub>", "0–4"),
    ("Khả cháy · Flammability", "I<sub>FL</sub>", "0–4"),
    ("Khả nổ · Explosiveness", "I<sub>EX</sub>", "0–4"),
    ("Phơi nhiễm độc · Toxic exposure", "I<sub>TOX</sub>", "0–6"),
    ("Khả ăn mòn · Corrosiveness", "I<sub>COR</sub>", "0–2"),
    "Chỉ số an toàn nội tại quá trình, I<sub>PI</sub>",
    ("Tồn kho · Inventory", "I<sub>I</sub>", "0–5"),
    ("Nhiệt độ quá trình · Process temperature", "I<sub>T</sub>", "0–4"),
    ("Áp suất quá trình · Process pressure", "I<sub>p</sub>", "0–4"),
    ("An toàn thiết bị Isbl · Equipment safety Isbl", "I<sub>EQ</sub>", "0–4"),
    ("An toàn thiết bị Osbl · Equipment safety Osbl", "I<sub>EQ</sub>", "0–3"),
    ("Cấu trúc quá trình an toàn · Safe process structure",
     "I<sub>ST</sub>", "0–5"),
]

_T8_EN = [
    "Chemical inherent safety index, I<sub>CI</sub>",
    ("Heat of main reaction", "I<sub>RM</sub>", "0–4"),
    ("Heat of side reaction, max", "I<sub>RS</sub>", "0–4"),
    ("Chemical interaction", "I<sub>INT</sub>", "0–4"),
    ("Flammability", "I<sub>FL</sub>", "0–4"),
    ("Explosiveness", "I<sub>EX</sub>", "0–4"),
    ("Toxic exposure", "I<sub>TOX</sub>", "0–6"),
    ("Corrosiveness", "I<sub>COR</sub>", "0–2"),
    "Process inherent safety index, I<sub>PI</sub>",
    ("Inventory", "I<sub>I</sub>", "0–5"),
    ("Process temperature", "I<sub>T</sub>", "0–4"),
    ("Process pressure", "I<sub>p</sub>", "0–4"),
    ("Equipment safety Isbl", "I<sub>EQ</sub>", "0–4"),
    ("Equipment safety Osbl", "I<sub>EQ</sub>", "0–3"),
    ("Safe process structure", "I<sub>ST</sub>", "0–5"),
]


def _t8_table(rows, lang):
    if lang == "vi":
        header = ("Chỉ số thành phần", "Ký hiệu", "Điểm")
        cap = "Bảng 8 · Các chỉ số thành phần của an toàn nội tại."
    else:
        header = ("Subindex", "Symbol", "Score")
        cap = "Table 8 · Inherent safety subindices."
    prepped = []
    for r in rows:
        if isinstance(r, str):
            prepped.append('<b style="color:#1f5f8b">%s</b>' % r)
        else:
            prepped.append(r)
    return table(header, prepped, cap)


def body_vi():
    b = []

    b.append(h2("9. Trọng số giữa các chỉ số thành phần của chỉ số an toàn "
                "nội tại",
                "9. The Weighting between Subindices of Inherent Safety Index"))

    b.append(p("Mọi dự án thiết kế quá trình đều là duy nhất. Số lượng và loại "
               "các phương án quá trình có thể lựa chọn rất khác nhau. Hơn nữa, "
               "nhà thiết kế có thể <b>đề cao các yếu tố an toàn khác nhau tùy "
               "chính sách công ty và bài toán cụ thể</b>. Vì vậy các chỉ số "
               "thành phần của ISI có thể được gán trọng số cho phù hợp với tình "
               "huống mới. Cách thực hiện là đưa <b>các hệ số trọng số vào "
               "Phương trình 3–5</b> và qua đó điều chỉnh điểm chuẩn của Bảng 8. "
               "Nếu nhà thiết kế muốn dùng ISI với các hệ số trọng số đã thay "
               "đổi, anh ta phải áp dụng cùng cách tiếp cận cho <b>tất cả</b> "
               "các phương án của mình để bảo đảm mọi phương án được so sánh "
               "trên cùng một cơ sở."))
    b.append(eq("I<sub>TI</sub> = I<sub>CI</sub> + I<sub>PI</sub> &nbsp;&nbsp;"
                "(Phương trình 3, có thể thêm hệ số trọng số w<sub>i</sub>)",
                ""))

    b.append(p("Cũng có thể điều chỉnh ISI cho khớp chính sách công ty bằng cách "
               "ban hành một <b>trọng số nội bộ chuẩn hóa</b> — được mọi nhân "
               "viên sử dụng thống nhất."))

    b.append(p("Trong Bảng 8, <b>phạm vi điểm thay đổi từ chỉ số thành phần này "
               "sang chỉ số khác</b>. Độ rộng của phạm vi phản ánh tầm quan "
               "trọng của chỉ số đó đối với an toàn nhà máy. Lựa chọn này dựa "
               "trên cuộc khảo sát của Edwards và cộng sự (1996): <b>tám chuyên "
               "gia</b> từ các lĩnh vực khác nhau của an toàn quá trình được "
               "hỏi về những khía cạnh an toàn nội tại mà họ cho là liên quan "
               "nhất. Các chuyên gia vừa nêu tên các tham số mà họ coi là thiết "
               "yếu cho đánh giá an toàn nội tại, vừa cho điểm mỗi tham số để "
               "thể hiện tầm quan trọng tương đối của nó."))

    b.append(p("Lawrence (1996) tổng hợp câu trả lời của các chuyên gia và tính "
               "điểm tổng cho từng tham số. Theo bản tổng hợp này, <b>các tham "
               "số quan trọng nhất đối với an toàn nội tại là tồn kho và độc "
               "tính</b>. Các yếu tố quan trọng khác, theo thứ tự, là độ bền "
               "hóa học (chemical stability), nhiệt độ, áp suất, khả cháy và "
               "khả nổ — được mọi chuyên gia coi là thiết yếu. Điểm chớp cháy "
               "và phản ứng phụ cũng khá quan trọng."))

    b.append(p("Chúng tôi đã tận dụng kết quả đánh giá chuyên gia này cùng "
               "phán đoán của mình để xác định các phạm vi điểm trong Bảng 8. "
               "<b>Phạm vi rộng hơn nghĩa là ảnh hưởng lớn hơn đến an toàn nhà "
               "máy.</b> Trong phương pháp của chúng tôi, độc tính và tồn kho "
               "được chấm là quan trọng nhất (điểm tối đa 6 và 5). Điều này "
               "phù hợp với đánh giá chuyên gia, ngoại trừ cấu trúc quá trình "
               "an toàn — vốn không được nhóm chuyên gia đề cập đến. Hầu hết "
               "các chỉ số còn lại được cho điểm 4; cũng phù hợp với đánh giá "
               "chuyên gia, trừ việc các chuyên gia không xét đến an toàn thiết "
               "bị. Sự vắng mặt của an toàn thiết bị và cấu trúc quá trình an "
               "toàn trong đánh giá chuyên gia có lẽ do các chuyên gia được cho "
               "một danh sách từ khóa để nhận xét, và danh sách này không chứa "
               "từ khóa nào về thiết bị hay cấu hình quá trình (Lawrence, "
               "1996)."))

    b.append(p("Ăn mòn được xếp thấp nhất (2) trong ISI, vì nó thường có thể "
               "khống chế bằng <b>lựa chọn vật liệu kết cấu phù hợp</b> — điều "
               "các chuyên gia cũng ghi nhận."))

    b.append(_t8_table(_T8, "vi"))

    b.append(fig(1, F.fig_c09_weights()))

    b.append(note("Chỉ số tối đa lý thuyết của chỉ số hóa học là 28 "
                  "(4+4+4+4+4+6+2) và của chỉ số quá trình là 22 "
                  "(5+4+4+4+3+5); tổng tối đa I<sub>TI</sub> = 50. Giá trị thấp "
                  "hơn nghĩa là quá trình an toàn nội tại hơn."))

    return "".join(b)


def body_en():
    b = []

    b.append(h2("9. The Weighting between Subindices of Inherent Safety Index",
                "9. Trọng số giữa các chỉ số thành phần"))

    b.append(p("All process design projects are unique. The number and the "
               "type of the possible process alternatives vary. Also, process "
               "designers may <b>emphasize the safety factors differently "
               "according to the company policy and the problem in hand</b>. "
               "Thus the subindices of the ISI can be weighted to fit the new "
               "situations. This can be done by introducing <b>weighting "
               "factors to Equations 3–5</b> and thereby modifying the standard "
               "scores of Table 8. If the process designer prefers to use the "
               "ISI with changed weighting factors, he must use the same "
               "approach to <b>all</b> his alternatives to make sure that all "
               "the alternatives are compared on the same basis."))
    b.append(eq("I<sub>TI</sub> = I<sub>CI</sub> + I<sub>PI</sub> &nbsp;&nbsp;"
                "(Eq. 3, extendable with weighting factors w<sub>i</sub>)",
                ""))

    b.append(p("It is also possible to fit the ISI into the company policy by "
               "generating a <b>standardized in-house weighting</b> which is "
               "then used by all employees."))

    b.append(p("In Table 8 the <b>score domain varies from one subindex to "
               "another</b>. The range of the scores reflects the importance of "
               "the specific subindex to the plant safety. This choice was made "
               "on the basis of the inquiry of Edwards et al. (1996): <b>eight "
               "experts</b> from different fields of process safety were asked "
               "which inherent safety aspects they considered most relevant. "
               "The experts both named the parameters which they considered "
               "essential for assessing inherent safety and gave a score for "
               "each parameter to represent its relative importance."))

    b.append(p("Lawrence (1996) summarized the answers of the experts and "
               "calculated the total scores for each parameter. According to "
               "this summary, <b>the most important parameters for inherent "
               "safety were inventory and toxicity</b>. Other important "
               "factors were, in this order, chemical stability, temperature, "
               "pressure, flammability and explosiveness, which were considered "
               "to be essential by all experts. Also flash points and side "
               "reactions were quite important."))

    b.append(p("We have utilized the results of this expert assessment with our "
               "own judgement to obtain the score ranges in Table 8. <b>A wider "
               "range means greater impact on the plant safety.</b> In our "
               "method toxicity and inventory are scored to be the most "
               "significant to the inherent safety (max scores 6 and 5). This "
               "is in agreement with the expert assessment, except the safe "
               "process structure, which was not included at all by the group "
               "of experts. Most other subindices were given score 4 — also in "
               "agreement with the expert assessment, except that the experts "
               "did not consider equipment safety at all. The absence of "
               "equipment safety and safe process structure in the expert "
               "assessment is probably because the experts were given a list "
               "of keywords they were asked to comment on. This list did not "
               "include any equipment- or process-configuration-oriented "
               "keywords (Lawrence, 1996)."))

    b.append(p("Corrosion was given the lowest ranking (2) in the ISI, since "
               "it can usually be controlled by a <b>proper choice of "
               "construction materials</b> — a point also recognized by the "
               "experts."))

    b.append(_t8_table(_T8_EN, "en"))

    b.append(fig(1, F.fig_c09_weights()))

    b.append(note("The theoretical maximum of the chemical index is 28 "
                  "(4+4+4+4+4+6+2) and that of the process index 22 "
                  "(5+4+4+4+3+5); the total maximum I<sub>TI</sub> = 50. A "
                  "lower value means an inherently safer process."))

    return "".join(b)
