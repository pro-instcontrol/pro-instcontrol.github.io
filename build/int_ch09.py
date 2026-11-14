# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 9: Appendix B, the blank Kepner-Tregoe decision
analysis worksheet (printed pages 50–60), plus the book's closing summary."""
import intfig as F
from int_common import (T, fig, h2, h3, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 11
BYLINE = "CSIA · Guide Vol. 1 (2000) · Appendix B"


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Phiếu phân tích quyết định</em> — "
        "bảng trống để khách hàng tự điền tiêu chí, «musts», trọng số và điểm. · "
        "<em>User Musts «M»</em> — cột đánh dấu điều kiện bắt buộc. · <em>User "
        "Wants Weights (1–10)</em> — trọng số mong muốn. · <em>Suggested Good "
        "Score / Performance Maximum</em> — điểm tốt và điểm trần gợi ý. · "
        "<em>SECTION TOTAL / GRAND TOTAL</em> — tổng theo nhóm và tổng toàn bảng. "
        "· <em>NO GO</em> — ứng viên bị loại từ vòng «musts», không tính tổng điểm.",
        "<b>Key terms.</b> <em>Decision analysis worksheet</em> — the blank form "
        "clients fill with their own criteria, musts, weights and scores. · "
        "<em>User Musts «M»</em> — the mandatory-condition column. · <em>User "
        "Wants Weights (1–10)</em> — the desired-criterion weights. · "
        "<em>Suggested Good Score / Performance Maximum</em> — recommended "
        "target and ceiling scores. · <em>SECTION TOTAL / GRAND TOTAL</em> — "
        "group and overall totals. · <em>NO GO</em> — a candidate eliminated at "
        "the musts screen, with no total score.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Phụ lục B là <em>phiếu làm việc</em>: cùng một bảng như ví dụ ở điều "
        "2.5 nhưng bỏ hết số liệu minh họa, chỉ giữ lại cấu trúc cột, số hiệu "
        "tiêu chí và các điểm gợi ý theo cấp. Nó in trên mười một trang cuối của "
        "tập sách để khách hàng có thể photocopy hoặc sao chép vào bảng tính và "
        "tự điền. Chương này khép lại Tập 1 bằng cách giải thích cách dùng phiếu "
        "và nối nó trở lại với toàn bộ quy trình.",
        "Appendix B is the <em>working form</em>: the same table as the §2.5 "
        "sample with all illustrative numbers removed, leaving only the column "
        "structure, criterion numbers and level-specific suggested scores. It "
        "occupies the volume's final eleven pages so clients can photocopy it or "
        "rebuild it in a spreadsheet. This chapter closes Volume 1 by explaining "
        "how to use the form and tying it back to the whole process.")))

    # ------------------------------------------------------------- worksheet
    b.append(h2(A("Cấu trúc của phiếu trống", "Structure of the blank worksheet"),
                A("Bảy nhóm cột", "Seven column groups")))
    b.append(fig(1, F.fig_blank_worksheet()))
    b.append(table(
        [A("Cột", "Column"), A("Ai điền", "Filled by"),
         A("Nội dung", "Content")],
        [
            [A("CRITERIA", "CRITERIA"), A("Có sẵn", "Pre-printed"),
             A("Số hiệu tiêu chí khớp với điều 4.0, kèm các hàng A–D để trống.",
               "Criterion numbers matching §4.0, with blank A–D rows.")],
            [A("User Musts «M»", "User Musts «M»"), A("Khách hàng", "Client"),
             A("Đánh M cho điều kiện tiên quyết; GO / NO GO khi sàng lọc.",
               "Mark M for a prerequisite; GO / NO GO when screening.")],
            [A("User Wants Weights (1–10)", "User Wants Weights (1–10)"),
             A("Khách hàng", "Client"),
             A("Trọng số tương đối của từng tiêu chí mong muốn.",
               "Relative weight of each desired criterion.")],
            [A("Suggested Performance Maximum / Good Score",
               "Suggested Performance Maximum / Good Score"),
             A("CSIA", "CSIA"),
             A("Điểm trần và điểm «tốt» gợi ý; trong phiếu trống đã điền sẵn "
               "các giá trị 2/3/4 cho nhiều tiêu chí.",
               "Recommended ceiling and “good” values; the blank form already "
               "carries 2/3/4 for many criteria.")],
            [A("CSIA Suggested Performance Score per Level",
               "CSIA Suggested Performance Score per Level"),
             A("CSIA", "CSIA"),
             A("Ba cột Level 3 / 2 / 1 theo điều 2.4; chọn cấp bằng dấu «X».",
               "Three Level 3 / 2 / 1 columns per §2.4; mark the level with «X».")],
            [A("CSI A / B / C Performance Score (0–5)",
               "CSI A / B / C Performance Score (0–5)"),
             A("Khách hàng", "Client"),
             A("Điểm của từng ứng viên; ô trống để ghi ba người chấm và tích có "
               "trọng số.",
               "Scores per candidate; blank cells for three judges and the "
               "weighted product.")],
            [A("SECTION TOTAL / GRAND TOTAL",
               "SECTION TOTAL / GRAND TOTAL"),
             A("Khách hàng", "Client"),
             A("Tổng theo từng nhóm 4.x, kèm tỷ lệ % so với GOAL SCORE.",
               "Totals for each 4.x group, with a % against the GOAL SCORE.")],
        ],
        A("Bản đồ các cột của phiếu Phụ lục B và ví dụ điều 2.5.",
          "Column map of the Appendix B worksheet and the §2.5 sample.")))
    b.append(p(A(
        "Mỗi trang của Phụ lục B lặp lại đúng dòng tiêu đề: «Item numbers "
        "correspond to section numbers in Section 4.0 explaining criteria» và "
        "«User Weight × Avg. Perf. Score = Total». Đây là lý do phiếu không thể "
        "dùng độc lập — nó là <b>khung trống</b> cần điền từ điều 2 (quy trình), "
        "điều 4 (tiêu chí) và dữ liệu thực tế của từng ứng viên.",
        "Every Appendix B page repeats the same header lines: “Item numbers "
        "correspond to section numbers in Section 4.0 explaining criteria” and "
        "“User Weight × Avg. Perf. Score = Total”. That is why the form cannot be "
        "used on its own — it is an <b>empty frame</b> to be filled from §2 "
        "(process), §4 (criteria) and the real data for each candidate.")))

    # --------------------------------------------------------------- totals
    b.append(h2(A("Đọc các dòng tổng kết", "Reading the totals rows"),
                A("Từ ví dụ điều 2.5", "From the §2.5 example")))
    b.append(fig(2, F.fig_totals()))
    b.append(ol([
        A("<b>GOAL SCORE = 347.</b> Tổng của cột «Suggested Performance Maximum» "
          "cho cả nhóm Quản lý chung; nó là 100% để quy đổi.",
          "<b>GOAL SCORE = 347.</b> The sum of the “Suggested Performance "
          "Maximum” column for the whole General Management group; it is the "
          "100% reference."),
        A("<b>CSI A = 190 (55%), CSI B = 172 (50%).</b> Dù CSI B thắng trong ví "
          "đơn giản ở điều 2.2, trong bảng đầy đủ CSI A lại cao hơn — một lời "
          "nhắc rằng kết quả phụ thuộc vào <em>bộ tiêu chí và trọng số</em> "
          "khách hàng chọn.",
          "<b>CSI A = 190 (55%), CSI B = 172 (50%).</b> Although CSI B wins the "
          "simple §2.2 example, in the full table CSI A ranks higher — a "
          "reminder that the outcome depends on the <em>criteria and weights</em> "
          "the client chooses."),
        A("<b>CSI C = NO GO.</b> Không có tổng điểm vì đã bị loại ở vòng musts. "
          "Cột «GRAND TOTAL» vì thế ghi «NO GO» thay vì một con số.",
          "<b>CSI C = NO GO.</b> No total is computed because it was eliminated "
          "at the musts screen; the GRAND TOTAL therefore reads “NO GO” rather "
          "than a number."),
    ]))
    b.append(note(A(
        "<b>Đừng nhầm hai ví dụ.</b> Điều 2.2 dùng một ví dụ rút gọn chỉ với hai "
        "tiêu chí (tỷ lệ nghỉ việc, kinh nghiệm ứng dụng) để dạy phép tính; điều "
        "2.5 dùng bảng đầy đủ với hàng chục tiêu chí. Hai ví dụ không được thiết "
        "kế để cho cùng một người thắng — chúng minh họa hai mức độ chi tiết "
        "khác nhau của cùng một phương pháp.",
        "<b>Do not conflate the two examples.</b> §2.2 uses a two-criterion "
        "toy example (turnover, application experience) to teach the arithmetic; "
        "§2.5 uses the full table with dozens of criteria. They were not "
        "designed to produce the same winner — they illustrate two levels of "
        "detail of one method.")))

    # ------------------------------------------------------------- how to use
    b.append(h2(A("Quy trình dùng phiếu từ A đến Z",
                  "Using the worksheet end to end"),
                A("Tám bước, một tờ giấy", "Eight steps, one sheet")))
    b.append(ol([
        A("Viết câu phát biểu quyết định lên đầu phiếu (bước 1, điều 2.2).",
          "Write the decision statement at the top of the form (§2.2 step 1)."),
        A("Điền tiêu chí riêng của khách hàng vào các hàng A–D / «User Defined» "
          "(bước 2; các điều 4.1.6, 4.2.3, 4.3.7, 4.4.5, 4.5.6, 4.6.4).",
          "Add client-specific criteria into the A–D / “User Defined” rows "
          "(step 2; §§4.1.6, 4.2.3, 4.3.7, 4.4.5, 4.5.6, 4.6.4)."),
        A("Đánh M cho các điều kiện «phải» (bước 3).",
          "Mark M against the must criteria (step 3)."),
        A("Gán trọng số 1–10 cho các «mong muốn» (bước 4).",
          "Assign 1–10 weights to the wants (step 4)."),
        A("Đánh dấu «X» vào cột Level 1 / 2 / 3 phù hợp (điều 2.4).",
          "Mark «X» in the appropriate Level 1 / 2 / 3 column (§2.4)."),
        A("Sàng lọc GO / NO GO qua musts; gạch tên ứng viên bị loại (bước 5).",
          "Screen GO / NO GO through the musts and strike out eliminated "
          "candidates (step 5)."),
        A("Cho ba người chấm độc lập, lấy trung bình làm tròn lên, nhân trọng số, "
          "cộng dồn thành SECTION TOTAL và GRAND TOTAL (bước 6).",
          "Have three judges score independently, round the average up, multiply "
          "by the weight, and sum to SECTION TOTAL and GRAND TOTAL (step 6)."),
        A("Ghi rủi ro và biện pháp quản lý ra lề, rồi mới ra quyết định (bước "
          "7–8). Giữ lại phiếu đã điền làm hồ sơ giải trình được.",
          "Record risks and mitigations in the margin, then decide (steps 7–8). "
          "Keep the completed sheet as a defensible audit record."),
    ]))

    # -------------------------------------------------------------- closing
    b.append(h2(A("Khép lại Tập 1", "Closing Volume 1"),
                A("Sáu phần, một quyết định có thể bảo vệ được",
                  "Six parts, one defensible decision")))
    b.append(fig(3, F.fig_closing_map()))
    b.append(p(A(
        "Tập 1 đi từ chỗ hiểu thị trường (điều 1), qua cách cấu trúc quyết định "
        "(điều 2), lối tắt đăng ký (điều 3), bảy nhóm tiêu chí (điều 4), hệ "
        "phân loại nhà cung cấp (Phụ lục A) đến tờ phiếu để ghi lại mọi phán "
        "đoán (Phụ lục B). Giá trị bền vững nhất của nó không phải là một con số "
        "điểm, mà là <b>một quyết định có thể giải trình được</b>: tiêu chí nào "
        "được chọn, ai nặng hơn ai, ai chấm, rủi ro nào đã được chấp nhận và do "
        "ai quản lý.",
        "Volume 1 moves from understanding the market (§1), through structuring "
        "the decision (§2), the registration shortcut (§3), the seven criteria "
        "families (§4), the provider taxonomy (Appendix A), to the sheet that "
        "records every judgment (Appendix B). Its lasting value is not a score "
        "but <b>a defensible decision</b>: which criteria were chosen, how they "
        "were weighted, who scored them, and which risks were accepted and "
        "owned by whom.")))
    b.append(ul([
        A("<b>Tập 2 tiếp nối</b> với phát triển yêu cầu chào giá (RFP), đánh giá "
          "hồ sơ dự thầu và quản lý triển khai dự án — đúng hai mục đích còn lại "
          "nêu ở phần INTRODUCTION.",
          "<b>Volume 2 continues</b> with RFP development, proposal evaluation "
          "and project implementation management — exactly the two remaining "
          "purposes stated in the INTRODUCTION."),
        A("<b>Không có khuyến nghị kỹ thuật nào</b> được ngầm định từ các ví dụ; "
          "bộ tài liệu không bao quát mọi trường hợp và người dùng chịu trách "
          "nhiệm về tiêu chí của chính mình.",
          "<b>No technical recommendation is implied</b> by any example; the "
          "documents are not all-encompassing and users are responsible for "
          "their own criteria."),
        A("<b>Bản dịch này</b> trình bày toàn bộ văn bản quy phạm song ngữ "
          "Anh–Việt, vẽ lại 35 hình / bảng dưới dạng vector, và giữ nguyên số "
          "hiệu điều để đối chiếu với bản gốc © 2000 CSIA.",
          "<b>This translation</b> renders the full normative prose bilingually "
          "in English and Vietnamese, redraws all 35 figures and tables as "
          "vectors, and keeps the original clause numbers for cross-reference "
          "with the © 2000 CSIA source."),
    ]))
    b.append(refs([
        A("Điều 1 — <a href=\"../ch01-general/\">chương 1</a>: CSIA, định nghĩa "
          "CSI, tín điều và lời cảnh báo.",
          "§1 — <a href=\"../ch01-general/\">Chapter 1</a>: CSIA, the CSI "
          "definition, beliefs and the disclaimer."),
        A("Điều 2 — <a href=\"../ch02-decision-analysis-tool/\">chương 2</a> và "
          "<a href=\"../ch03-scoring-and-levels/\">chương 3</a>: tám bước, thang "
          "0–5, ba cấp và bảng mẫu.",
          "§2 — <a href=\"../ch02-decision-analysis-tool/\">Chapter 2</a> and "
          "<a href=\"../ch03-scoring-and-levels/\">Chapter 3</a>: eight steps, "
          "the 0–5 scale, three levels and the sample table."),
        A("Điều 3–4 — <a href=\"../ch04-registration-and-general-management/\">"
          "chương 4</a> đến <a href=\"../ch07-technical/\">chương 7</a>: đăng ký "
          "và bảy nhóm tiêu chí.",
          "§§3–4 — <a href=\"../ch04-registration-and-general-management/\">"
          "Chapter 4</a> to <a href=\"../ch07-technical/\">Chapter 7</a>: "
          "registration and the seven criteria families."),
        A("Phụ lục A — <a href=\"../ch08-integrator-types/\">chương 8</a>: mười "
          "biểu đồ cơ cấu dịch vụ.",
          "Appendix A — <a href=\"../ch08-integrator-types/\">Chapter 8</a>: "
          "ten service-mix charts."),
    ]))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
