# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 3: Performance scoring, levels and the sample
criteria/analysis table, §§2.3–2.5 (pp. 7–10)."""
import intfig as F
from int_common import T, fig, h2, h3, lead, note, ol, p, quote, table, ul

PAGES_SRC = 4
BYLINE = "CSIA · Guide Vol. 1 (2000) · §§2.3–2.5"

SCALE = [
    ("0", ("Không có bằng chứng về chính sách, thực hành hay «hệ thống» tiêu chuẩn "
           "nào được thiết lập, và không có bằng chứng về công việc đã được khởi "
           "động trong lĩnh vực này.",
           "No evidence of policy, practice or standards “systems” in place, and "
           "no evidence of any work being initiated in this area.")),
    ("1", ("Đã khởi động các «phần tử» chính sách / thực hành / tiêu chuẩn cơ bản. "
           "Triển khai, đào tạo và tài liệu hóa chưa có hoặc chỉ ở mức tối thiểu.",
           "Basic policy, practice or standards “elements” initiated. "
           "Implementation, training and documentation do not exist or are "
           "minimal.")),
    ("2", ("Các phần tử cơ bản mới triển khai một phần. Đào tạo, tài liệu và/hoặc "
           "hồ sơ còn tối thiểu, chưa đầy đủ; hiệu quả chưa được chứng minh thỏa "
           "đáng.",
           "Basic elements partially implemented. Training, documentation and/or "
           "records are minimal and incomplete; effectiveness is not being "
           "satisfactorily demonstrated.")),
    ("3", ("Chính sách / thực hành / tiêu chuẩn cơ bản đã triển khai phần lớn, có "
           "tài liệu hỗ trợ. «Hệ thống» có thể coi là tối thiểu đạt yêu cầu, nhưng "
           "còn chỗ cải tiến.",
           "Basic policy, practice or standards mostly implemented with supporting "
           "documentation. “Systems” can be considered minimally adequate, with "
           "opportunities for improvement.")),
    ("4", ("Các phần tử ở mức cao hơn đã triển khai với tài liệu hỗ trợ tốt. Hiểu "
           "biết về «hệ thống» tốt và được áp dụng đồng đều. Hiệu quả tốt nhưng "
           "chưa phải lúc nào cũng thể hiện rõ; có nỗ lực cải tiến liên tục nhưng "
           "chưa chứng minh được.",
           "Higher elements implemented with good supporting documentation. "
           "Knowledge of the “system” is good and uniformly applied. "
           "Effectiveness is good but not always evident; continual improvement "
           "is strived for but not demonstrated.")),
    ("5", ("Chính sách / thực hành / tiêu chuẩn ở mức cao được cân nhắc kỹ, lập tài "
           "liệu và triển khai đến mức có thể gọi là xuất sắc. Hiệu quả thể hiện rõ "
           "và cải tiến liên tục đang được chứng minh.",
           "Higher policy, practice or standards are well thought out, documented "
           "and implemented to the point of outstanding. Effectiveness is evident "
           "and continual improvement is being demonstrated.")),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Điểm hiệu năng</em> — thang 0–5 "
        "đánh giá mức trưởng thành của chính sách / thực hành / tiêu chuẩn. · "
        "<em>Cấp CSI</em> — Level 1 / 2 / 3 phân theo doanh thu, số nhân sự và tỷ "
        "lệ kỹ sư. · <em>Suggested Performance Maximum</em> — điểm trần gợi ý. · "
        "<em>Good Score</em> — điểm «tốt» gợi ý theo từng cấp. · <em>GO / NO GO</em> "
        "— kết quả sàng lọc theo tiêu chí «phải». · <em>Trung bình ba người "
        "chấm</em> — cơ sở tính điểm hiệu năng trong bảng mẫu.",
        "<b>Key terms.</b> <em>Performance score</em> — the 0–5 maturity scale for "
        "policy / practice / standards. · <em>CSI level</em> — Level 1 / 2 / 3 by "
        "annual sales, headcount and engineer ratio. · <em>Suggested Performance "
        "Maximum</em> — the recommended ceiling score. · <em>Good Score</em> — the "
        "recommended “good” score for each level. · <em>GO / NO GO</em> — the "
        "must-screening outcome. · <em>Three-judge average</em> — the basis of the "
        "performance score in the sample table.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Nếu chương 2 đưa ra <em>quy trình</em>, chương 3 đưa ra <em>thước đo</em>. "
        "Ba điều cuối của phần 2 lần lượt định nghĩa thang điểm hiệu năng 0–5 "
        "(2.3), ba cấp quy mô CSI (2.4) và bảng tiêu chí / phân tích mẫu (2.5) — "
        "bảng mà toàn bộ điều 4 và Phụ lục B đều quy về. Đây cũng là chương có "
        "nhiều bảng nhất của tập sách.",
        "If Chapter 2 supplies the <em>process</em>, Chapter 3 supplies the "
        "<em>yardstick</em>. The last three clauses of §2 define the 0–5 "
        "performance scale (2.3), the three CSI size levels (2.4) and the sample "
        "criteria/analysis table (2.5) — the table to which all of §4 and Appendix "
        "B refer. It is also the most table-heavy chapter in the volume.")))

    # ------------------------------------------------------------- 2.3 scale
    b.append(h2(A("2.3 · Thang điểm hiệu năng 0–5",
                  "2.3 · Performance scoring of alternatives"),
                A("Một thang, sáu mức", "One scale, six levels")))
    b.append(p(A(
        "Người dùng <b>có thể tự định nghĩa</b> hệ thống chấm điểm giúp những người "
        "ra quyết định đánh giá công bằng và nhất quán. CSIA đưa ra hệ thống dưới "
        "đây «để tham khảo» — không bắt buộc. Điểm then chốt của điều này là lời "
        "thừa nhận rất thực tế của tác giả:",
        "The user <b>may define</b> a scoring system that helps decision makers "
        "evaluate candidates fairly and consistently. The CSIA offers the system "
        "below “for your edification” — it is not mandatory. The key point of this "
        "clause is the authors' very practical admission:")))
    b.append(quote(A(
        "«Vì dải tiêu chí rất rộng, bất kỳ một hệ thống chấm điểm nào cũng sẽ có "
        "những lúc khó áp dụng cho tiêu chí đang xét. Người ra quyết định nên dùng "
        "phán đoán tốt nhất của mình rồi tiếp tục.»",
        "«Since the range of criteria is so broad, any one scoring system will "
        "have its moments of questionable applicability to the criteria in "
        "question. The decision-maker(s) should use their best judgment and move "
        "on.»"),
        A("CSIA Guide, Volume 1, điều 2.3, trang 7",
          "CSIA Guide, Volume 1, §2.3, page 7")))
    b.append(fig(1, F.fig_score_scale()))
    b.append(table(
        [A("Điểm", "Score"), A("Ý nghĩa ngắn", "Short meaning")],
        [[n, A(s_vi.split(".")[0] + ".", s_en.split(".")[0] + ".")]
         for n, (s_vi, s_en) in SCALE],
        A("Rút gọn từ bảng mô tả gốc ở điều 2.3; mô tả đầy đủ có trong Hình 3.1.",
          "Condensed from the §2.3 description table; full wording is in Figure 3.1.")))
    b.append(ul([
        A("Mức <b>0–2</b> chủ yếu nói về <em>sự hiện diện</em> của chính sách và "
          "tài liệu; mức <b>3</b> là ngưỡng «tối thiểu đạt yêu cầu».",
          "Levels <b>0–2</b> are mostly about the <em>existence</em> of policy and "
          "documentation; level <b>3</b> is the “minimally adequate” threshold."),
        A("Mức <b>4–5</b> chuyển sang <em>hiệu quả và cải tiến liên tục</em>: 4 có "
          "nỗ lực nhưng chưa chứng minh được, 5 đã chứng minh được.",
          "Levels <b>4–5</b> shift to <em>effectiveness and continual "
          "improvement</em>: 4 strives but has not demonstrated, 5 has "
          "demonstrated."),
        A("Cách phân mức này giải thích tại sao điều 4 hỏi đi hỏi lại «có tài liệu "
          "hóa không», «có đào tạo không», «có đo lường cải tiến không».",
          "This grading explains why §4 repeatedly asks “is it documented”, “is "
          "there training”, “is improvement measured”."),
    ]))

    # ------------------------------------------------------------ 2.4 levels
    b.append(h2(A("2.4 · Ba cấp phân loại CSI", "2.4 · CSIA classification levels"),
                A("So sánh cùng tiêu chí ở quy mô khác nhau",
                  "Compare like with like across sizes")))
    b.append(p(A(
        "«Các CSI lớn hơn cần nhiều hạ tầng kinh doanh hơn các CSI nhỏ hơn. Để bù "
        "trừ cho vấn đề này, chúng tôi gợi ý đánh giá CSI theo cấp.» Đây là lý do "
        "bảng chấm điểm có ba cột điểm gợi ý riêng cho Level 1 / 2 / 3 — đừng so "
        "một xưởng 12 người với một công ty 80 kỹ sư bằng cùng một điểm trần.",
        "“Larger CSIs require more business infrastructure than smaller ones. To "
        "compensate for this issue, we suggest evaluating CSIs by level.” That is "
        "why the scoring table carries three separate suggested-score columns for "
        "Level 1 / 2 / 3 — do not compare a twelve-person shop with an "
        "eighty-engineer firm against the same ceiling.")))
    b.append(fig(2, F.fig_levels()))
    b.append(note(A(
        "<b>Cách dùng trong bảng.</b> Điều 2.2 hướng dẫn chọn «Suggested "
        "Performance Maximum / Pick Level 1, 2 or 3» cho phù hợp với cấp của CSI "
        "được đánh giá. Khi so sánh các CSI <em>khác cấp</em>, hãy chọn số phù hợp "
        "nhất với yêu cầu của khách hàng cho từng tiêu chí. Điều 2.5 cũng nhắc lại "
        "lời này trong phần NOTE.",
        "<b>How to use it in the table.</b> §2.2 directs you to select the "
        "appropriate “Suggested Performance Maximum / Pick Level 1, 2 or 3” for "
        "the level of CSI being evaluated. When comparing CSIs <em>at different "
        "levels</em>, pick the number that best fits the client's requirements for "
        "those criteria. §2.5 repeats this in its NOTE.")))

    # ---------------------------------------------------------- 2.5 sample
    b.append(h2(A("2.5 · Bảng tiêu chí / phân tích mẫu",
                  "2.5 · The “Sample” Criteria / Analysis Table"),
                A("Bảng trung tâm của toàn bộ tập sách",
                  "The volume's central table")))
    b.append(p(A(
        "Bảng trải dài hai trang (9–10) với các cột: số hiệu tiêu chí (khớp số "
        "hiệu điều ở mục 4.0), cột «Musts M», trọng số mong muốn 1–10, điểm trần "
        "gợi ý, điểm «Good», ba cột điểm gợi ý theo cấp, rồi các cột CSI A*, "
        "CSI B*, CSI C*. Cuối mỗi nhóm là dòng SECTION TOTAL và cuối bảng là GRAND "
        "TOTAL. Chỗ trống được chừa sẵn để khách hàng điền tiêu chí riêng.",
        "The table spans two pages (9–10) with columns for the criterion number "
        "(matching the §4.0 clause numbers), a “Musts M” column, want weights "
        "1–10, suggested maximum, “Good” score, three level-specific suggested "
        "scores, and CSI A*, CSI B*, CSI C* score columns. Each group ends with a "
        "SECTION TOTAL row and the table ends with a GRAND TOTAL. Blank rows are "
        "provided for client-specific criteria.")))
    b.append(fig(3, F.fig_sample_table()))
    b.append(ol([
        A("<b>Số hiệu tiêu chí</b> trong bảng chính là số điều ở mục 4.0 — ví dụ "
          "<code>4.1.1 A</code> là «Defined/Clear Strategic Objectives». Vì vậy "
          "bảng và phần giải thích tiêu chí phải được đọc cùng nhau.",
          "<b>Criterion numbers in the table are §4.0 clause numbers</b> — e.g. "
          "<code>4.1.1 A</code> is “Defined/Clear Strategic Objectives”. The table "
          "and the criteria explanations must therefore be read together."),
        A("<b>Có thể bỏ qua phần lớn điều 4.</b> Nguyên văn: «Người dùng có thể bỏ "
          "qua các mục 4.1 đến 4.6.5 của bảng phân tích nếu CSI được đánh giá đã "
          "đăng ký CSIA!» — xem điều 3.0. Đây là lối tắt thực tế quan trọng nhất "
          "của tập sách.",
          "<b>Much of §4 can be skipped.</b> Verbatim: “Users may wish to skip "
          "Section 4.1 through 4.6.5 of analysis table if the CSI being evaluated "
          "is CSIA Registered!” — see §3.0. This is the volume's most important "
          "practical shortcut."),
        A("<b>Phiếu trống</b> được cung cấp tại Phụ lục B; dấu sao (*) đánh dấu "
          "các cột do người dùng tự điền.",
          "<b>A blank form</b> is supplied in Appendix B; the asterisk (*) marks "
          "columns the user fills in."),
    ]))
    b.append(note(A(
        "<b>Ghi chú của bảng mẫu.</b> «Ba người đánh giá đã chấm điểm hiệu năng "
        "của CSI A, CSI B và CSI C. Trong mẫu này, CSI C đã không vượt qua vòng "
        "sàng lọc «musts».» Vì thế cột CSI C chỉ còn các giá trị GO / NO GO mà "
        "không có tổng điểm.",
        "<b>Note on the sample.</b> “Three resources judged performance of CSI A, "
        "CSI B and CSI C. In this sample, CSI C did not pass the screen for "
        "‘musts’.” That is why the CSI C column contains only GO / NO GO values "
        "and no total score.")))

    # ------------------------------------------------------- averaging
    b.append(h2(A("Cách đọc ba con số trong một ô",
                  "Reading the three numbers in one cell"),
                A("Ví dụ 1,2,2 → (4)", "The 1,2,2 → (4) example")))
    b.append(fig(4, F.fig_three_judges()))
    b.append(p(A(
        "Đây là phần dễ hiểu nhầm nhất của bảng mẫu, nên bản gốc giải thích riêng. "
        "Với tiêu chí 4.1.1 A, ba người chấm CSI A lần lượt cho 1, 2 và 2 điểm. "
        "Tổng 5 chia 3 được 1,66, <b>làm tròn lên thành 2</b>. Nhân với trọng số "
        "mong muốn của người dùng (2) được <b>4</b> — chính là số trong ngoặc đơn. "
        "Cột «TOTAL» của từng nhóm vì thế không phải tổng của ba điểm riêng lẻ, mà "
        "là tổng của các tích đã nhân trọng số.",
        "This is the sample table's most easily misread part, so the source "
        "explains it separately. For criterion 4.1.1 A, three judges score CSI A "
        "as 1, 2 and 2. The sum 5 divided by 3 is 1.66, <b>rounded up to 2</b>. "
        "Multiplying by the user's want weight (2) gives <b>4</b> — the number in "
        "parentheses. A group's TOTAL column is therefore not the sum of the three "
        "raw scores but the sum of the weighted products.")))
    b.append(table(
        [A("Thành phần", "Component"), A("Giá trị", "Value"),
         A("Ý nghĩa", "Meaning")],
        [
            [A("Ba người chấm", "Three judges"), "1, 2, 2",
             A("Điểm hiệu năng riêng lẻ", "Individual performance scores")],
            [A("Trung bình", "Average"), "5 / 3 = 1,66 → 2",
             A("Làm tròn lên", "Rounded up")],
            [A("Trọng số", "User want weight"), "2",
             A("Từ cột User Wants Weights", "From the User Wants Weights column")],
            [A("Tích", "Product"), "2 × 2 = 4",
             A("Số ghi trong ngoặc đơn", "Number shown in parentheses")],
        ],
        A("Ví dụ tính điểm cho tiêu chí 4.1.1 A theo điều 2.2.",
          "Scoring calculation for criterion 4.1.1 A, from §2.2.")))
    b.append(note(A(
        "<b>Đọc tiếp.</b> Chương 4 bắt đầu phần tiêu chí với đăng ký CSIA và Quản "
        "lý chung; chương 9 quay lại bảng này với phiếu trống Phụ lục B và các "
        "dòng tổng kết mẫu (347 / 190 / 172).",
        "<b>Where next.</b> Chapter 4 opens the criteria section with CSIA "
        "registration and General Management; Chapter 9 returns to this table "
        "with the blank Appendix B worksheet and the sample totals "
        "(347 / 190 / 172).")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
