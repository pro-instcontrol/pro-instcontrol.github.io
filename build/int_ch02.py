# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 2: Decision analysis tool, §§2.1–2.2 (pp. 3–6)."""
import intfig as F
from int_common import T, fig, h2, h3, lead, note, ol, p, table, ul

PAGES_SRC = 4
BYLINE = "CSIA · Guide Vol. 1 (2000) · §§2.1–2.2"

STEPS = [
    ("1", ("Phát biểu quyết định", "State the Decision"),
     ("Viết một câu ngắn mô tả kết quả mong muốn của quyết định. Ví dụ của bản gốc: "
      "«Chọn một CSI phù hợp nhất với nhu cầu của chúng ta».",
      "Write a short statement describing the intended result of a decision. The "
      "guide's example: “Select a CSI that best fits our needs”.")),
    ("2", ("Xây dựng tiêu chí", "Develop Criteria"),
     ("Nhận diện các tiêu chí sẽ ảnh hưởng đến lựa chọn. Ví dụ: doanh số trên "
      "X,X triệu USD; tỷ lệ nghỉ việc thấp; kinh nghiệm ứng dụng. Điều 4.0 đưa "
      "ra bộ tiêu chí gợi ý của CSIA.",
      "Identify criteria that will influence the choice. Examples: over $X.XM in "
      "sales; low turnover rate; application experience. §4.0 sets out the CSIA's "
      "suggested criteria.")),
    ("3", ("Phân loại «phải» (M) và «mong muốn»", "Classify into Musts (M) and Wants"),
     ("Xác định vai trò của từng tiêu chí: «phải» là điều kiện tiên quyết dạng "
      "đạt / không đạt, «mong muốn» là tiêu chí để so sánh mức độ tốt. Ví dụ: "
      "doanh số trên X,X triệu USD đánh dấu M.",
      "Determine the role each criterion plays: a must is a pass/fail prerequisite, "
      "a want is a criterion for comparing degrees of goodness. Example: over "
      "$X.XM in sales is marked M.")),
    ("4", ("Gán trọng số cho «mong muốn» (1–10)", "Weigh the Wants (1–10)"),
     ("Gán giá trị tương đối cho các tiêu chí mong muốn. Ví dụ: tỷ lệ nghỉ việc "
      "thấp = 7; kinh nghiệm ứng dụng = 9. Tiêu chí «phải» không có trọng số.",
      "Assign relative values to the want criteria. Example: low turnover rate = 7; "
      "application experience = 9. Must criteria carry no weight.")),
    ("5", ("Sàng lọc ứng viên qua «phải»", "Screen candidates through the Musts"),
     ("Kiểm tra từng ứng viên có đáp ứng mọi điều kiện «phải» không. Trong ví dụ, "
      "CSI A và CSI B đạt (GO), CSI C có doanh số dưới ngưỡng (NO GO) và bị loại "
      "khỏi quá trình.",
      "Check whether each candidate meets every must. In the example CSI A and "
      "CSI B pass (GO); CSI C falls below the sales threshold (NO GO) and is "
      "dropped from further consideration.")),
    ("6", ("Đánh giá và chấm điểm theo «mong muốn»",
           "Evaluate and score candidates against the Wants"),
     ("Đánh giá mức độ đáp ứng tương đối (0–5), rồi nhân với trọng số. Bản gốc "
      "cho CSI A: 7×4 = 28 và 9×3 = 27, tổng 55; CSI B: 7×3 = 21 và 9×4 = 36, "
      "tổng 57.",
      "Rate relative performance (0–5) and multiply by the weight. The guide gives "
      "CSI A: 7×4 = 28 and 9×3 = 27, total 55; CSI B: 7×3 = 21 and 9×4 = 36, "
      "total 57.")),
    ("7", ("Đánh giá rủi ro cần quản lý", "Assess risks for the client to manage"),
     ("Mọi quan hệ hợp tác đều có rủi ro mà khách hàng phải quản lý. Hãy nhận "
      "diện rủi ro và đánh giá khả năng quản lý chúng. Gợi ý của bản gốc: điểm "
      "hiệu năng thấp có thể là dấu hiệu rủi ro.",
      "Every partnership involves risk the client must manage. Identify the risks "
      "and evaluate your ability to manage them. The guide's hint: a low "
      "performance score could indicate risk.")),
    ("8", ("Ra quyết định", "Make decision"),
     ("Chọn CSI có <b>sự cân bằng tốt nhất</b> giữa việc đáp ứng tiêu chí (TỔNG "
      "ĐIỂM) và mức rủi ro chấp nhận được, có thể quản lý được. Điểm cao nhất "
      "không tự động đồng nghĩa với lựa chọn đúng.",
      "Select the CSI with the <b>best balance</b> between meeting the criteria "
      "(TOTAL SCORE) and acceptable, manageable risks. The highest score is not "
      "automatically the right choice.")),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Phân tích quyết định</em> — phương "
        "pháp nêu rõ tiêu chí, phân loại, gán trọng số và chấm điểm để đi tới kết "
        "luận. · <em>Kepner-Tregoe® (KT®)</em> — phương pháp luận gốc được CSIA "
        "dùng lại có cho phép. · <em>Must / Want</em> — tiêu chí bắt buộc (M, "
        "đạt / không đạt) / tiêu chí mong muốn (có trọng số 1–10). · "
        "<em>GO / NO GO</em> — đạt / bị loại ở bước sàng lọc. · <em>Trọng số × "
        "điểm hiệu năng</em> — phép tính tạo ra tổng điểm.",
        "<b>Key terms.</b> <em>Decision analysis</em> — stating criteria, "
        "classifying, weighting and scoring to reach a conclusion. · "
        "<em>Kepner-Tregoe® (KT®)</em> — the methodology the CSIA reuses with "
        "permission. · <em>Must / Want</em> — mandatory criterion (M, pass/fail) "
        "/ desired criterion (weighted 1–10). · <em>GO / NO GO</em> — pass or "
        "elimination at the screening step. · <em>Weight × performance</em> — the "
        "product that produces the total score.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Điều 2 là trái tim của Tập 1. Nó đưa ra một <em>công cụ phân tích quyết "
        "định</em> để thiết lập tiêu chí, xếp hạng mức độ quan trọng và tổ chức "
        "việc đánh giá theo những bước có cấu trúc. Phương pháp được lấy từ "
        "Kepner-Tregoe® (KT®), được in lại với sự cho phép của Kepner-Tregoe, Inc. "
        "Chương này đi hết tám bước; chương 3 tiếp tục với thang điểm, các cấp CSI "
        "và bảng phân tích mẫu.",
        "Clause 2 is the heart of Volume 1. It offers a <em>decision analysis "
        "tool</em> for establishing criteria, classifying their relative "
        "importance and organising evaluation into structured steps. The method "
        "derives from Kepner-Tregoe® (KT®) and is reprinted with the permission of "
        "Kepner-Tregoe, Inc. This chapter walks through all eight steps; Chapter 3 "
        "continues with the scoring scale, CSI levels and the sample analysis "
        "table.")))

    # ------------------------------------------------------------- objective
    b.append(h2(A("2.1 · Công cụ phân tích dùng để làm gì?",
                  "2.1 · What the analysis tool is for"),
                A("Ba mục tiêu", "Three objectives")))
    b.append(ol([
        A("<b>Nêu rõ tiêu chí</b> làm cơ sở của quyết định, thay vì để chúng ngầm "
          "định.",
          "<b>Plainly state the criteria</b> on which a decision will be based, "
          "rather than leaving them implicit."),
        A("<b>Gán trọng số tương đối</b> (phân loại) theo mức độ quan trọng của "
          "từng tiêu chí đối với người ra quyết định.",
          "<b>Assign a relative weight</b> (classify) reflecting how important "
          "each criterion is to the decision maker(s)."),
        A("<b>Cung cấp cấu trúc</b> để đi qua quy trình đánh giá / lựa chọn một "
          "cách logic, và <b>phương pháp chấm điểm nhất quán</b> để đi tới kết luận.",
          "<b>Provide a structure</b> for a logical evaluation/selection process "
          "and a <b>consistent scoring method</b> for reaching a conclusion."),
    ]))
    b.append(note(A(
        "Bản gốc chèn một lời nhắc ngay dưới phần này: «Điều 2.5 cung cấp một "
        "bảng dễ dùng để tổ chức việc đánh giá và chấm điểm», và «phương pháp "
        "phân tích quyết định gợi ý trong điều này dựa trên phương pháp luận "
        "Kepner-Tregoe®». Phiếu trống tương ứng nằm ở Phụ lục B.",
        "The source inserts two reminders here: “Section 2.5 provides an "
        "easy-to-use table to organize evaluation and scoring”, and “The "
        "suggested decision analysis tool outlined in this section is based on the "
        "Kepner-Tregoe® decision analysis methodology”. The matching blank form is "
        "in Appendix B.")))

    # --------------------------------------------------------------- 8 steps
    b.append(h2(A("2.2 · Tám bước có cấu trúc", "2.2 · The eight structured steps"),
                A("Từ câu phát biểu đến quyết định", "From a statement to a decision")))
    b.append(fig(1, F.fig_decision_steps()))
    for n, (h_vi, h_en), (s_vi, s_en) in STEPS:
        b.append(h3(A("%s · %s" % (n, h_vi), "%s · %s" % (n, h_en))))
        b.append(p(A(s_vi, s_en)))

    # ---------------------------------------------------------- classification
    b.append(h2(A("Phân loại, sàng lọc và chấm điểm",
                  "Classification, screening and scoring"),
                A("Ba ví dụ được vẽ lại", "Three worked examples redrawn")))
    b.append(fig(2, F.fig_musts_wants()))
    b.append(fig(3, F.fig_screen()))
    b.append(fig(4, F.fig_score_worked()))
    b.append(table(
        [A("Bước", "Step"), A("Dữ liệu vào", "Input"), A("Kết quả", "Output")],
        [
            ["3–4", A("Tiêu chí thô", "Raw criteria"),
             A("Danh sách M và các mong muốn có trọng số 1–10",
               "A list of M items and wants weighted 1–10")],
            ["5", A("Ứng viên × tiêu chí M", "Candidates × musts"),
             A("Danh sách rút gọn (GO), loại NO GO",
               "A shortlist (GO), with NO GO candidates removed")],
            ["6", A("Điểm hiệu năng 0–5 × trọng số", "Performance 0–5 × weight"),
             A("Tổng điểm từng ứng viên", "A total score per candidate")],
            ["7–8", A("Tổng điểm + rủi ro", "Total score + risk"),
             A("Lựa chọn có thể bảo vệ được", "A defensible choice")],
        ],
        A("Bản đồ luồng dữ liệu của tám bước, tổng hợp từ điều 2.2.",
          "Data-flow map of the eight steps, summarised from §2.2.")))

    # ------------------------------------------------------ multiple judges
    b.append(h2(A("Nhiều người cùng chấm", "When several people judge"),
                A("Quy tắc ba người đánh giá", "The three-resource rule")))
    b.append(p(A(
        "Bảng mẫu ở điều 2.5 dùng <b>ba người đánh giá</b> cho mỗi CSI. Các con số "
        "trong cột CSI A*, CSI B*, CSI C* (ví dụ <code>1,2,2</code>) là ba điểm "
        "riêng lẻ; số trong ngoặc đơn là điểm hiệu năng — <em>trung bình của ba "
        "điểm, làm tròn lên, rồi nhân với trọng số mong muốn của người dùng</em>. "
        "Ví dụ cho tiêu chí 4.1.1 A: 1 + 2 + 2 = 5; 5/3 = 1,66 → 2; trọng số "
        "2 × 2 = 4. Xem chương 3 để có sơ đồ tính toán đầy đủ.",
        "The §2.5 sample table uses <b>three judges</b> per CSI. The numbers in "
        "the CSI A*, CSI B*, CSI C* columns (for example <code>1,2,2</code>) are "
        "three individual scores; the number in parentheses is the performance "
        "score — <em>the average of the three, rounded up, multiplied by the "
        "user's want weight</em>. For criterion 4.1.1 A: 1 + 2 + 2 = 5; 5/3 = "
        "1.66 → 2; weight 2 × 2 = 4. Chapter 3 carries the full calculation "
        "diagram.")))
    b.append(ul([
        A("<b>Nhất quán quan trọng hơn độ chính xác giả tạo.</b> Điều 2.3 sẽ nói "
          "thẳng: vì dải tiêu chí rất rộng, bất kỳ hệ thống chấm điểm nào cũng có "
          "lúc khó áp dụng; người ra quyết định nên dùng phán đoán tốt nhất rồi "
          "tiếp tục.",
          "<b>Consistency beats false precision.</b> §2.3 says it plainly: because "
          "the range of criteria is so broad, any one scoring system will have "
          "moments of questionable applicability; decision makers should use "
          "their best judgment and move on."),
        A("<b>Điểm thấp là tín hiệu rủi ro.</b> Ở bước 7, bản gốc gợi ý xem xét "
          "lại đặc tả kỹ thuật khi kinh nghiệm ứng dụng chỉ ở mức «vừa đủ», và "
          "đòi cam kết nhân sự chủ chốt khi tỷ lệ nghỉ việc hơi cao.",
          "<b>A low score is a risk signal.</b> At step 7 the guide suggests "
          "reviewing the specification carefully where application experience is "
          "marginal, and securing commitment of key project resources where "
          "turnover is borderline high."),
        A("<b>Không suy ra khuyến nghị kỹ thuật.</b> Các ví dụ chỉ minh họa cách "
          "dùng ký hiệu và tiêu chí; việc chọn một sơ đồ minh họa không có nghĩa "
          "là CSIA khuyến nghị phương pháp đo hay điều khiển đó.",
          "<b>No technical recommendation is implied.</b> The examples only "
          "illustrate the use of the criteria; choosing one illustrative scheme "
          "does not mean the CSIA recommends that measurement or control method."),
    ]))
    b.append(note(A(
        "<b>Ghi nhận bản quyền.</b> Phần cuối điều 2.2 ghi rõ: «Được in lại với sự "
        "cho phép của Kepner-Tregoe, Inc., Princeton, New Jersey. Bảo lưu mọi "
        "quyền». Kepner-Tregoe là công ty tư vấn và đào tạo quản lý quốc tế. Bản "
        "dịch này trình bày lại nội dung để học tập, không thay thế tài liệu gốc.",
        "<b>Crediting the source.</b> The end of §2.2 states: “Reprinted with the "
        "permission of Kepner-Tregoe, Inc., Princeton, New Jersey. All Rights "
        "Reserved”. Kepner-Tregoe is an international management training and "
        "consulting firm. This translation restates the material for study and "
        "does not replace the original.")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
