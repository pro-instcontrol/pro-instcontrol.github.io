# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 5: Human Resources (§4.2) and Project Management
(§4.3), printed pages 17–23."""
import intfig as F
from int_common import T, fig, h2, h3, lead, note, ol, p, quote, table, ul

PAGES_SRC = 7
BYLINE = "CSIA · Guide Vol. 1 (2000) · §§4.2–4.3"

HR = [
    ("4.2.1", ("Hành chính nhân sự", "Administration"), [
        ("A", ("Mô tả công việc được thiết lập và sử dụng",
               "Job Descriptions Established/Utilized"),
         ("CSI có mô tả công việc được thiết lập, được truyền đạt hiệu quả tới nhân "
          "viên và thể hiện trong hồ sơ nhân viên không?",
          "Does the CSI have established job descriptions effectively "
          "communicated to the employee and reflected in the employee files?")),
        ("B", ("Theo dõi định lượng tỷ lệ nghỉ việc",
               "Employee Turnover Rate — Quantitatively Track"),
         ("Tỷ lệ nghỉ việc của nhân viên là bao nhiêu?",
          "What is the employee turnover rate?")),
        ("C", ("Thực thi nơi làm việc không có chất gây nghiện",
               "Enforce a Drug-Free Workplace"),
         ("CSI có thực thi chính sách nơi làm việc không có ma túy không?",
          "Does the CSI enforce a drug-free workplace?")),
    ]),
    ("4.2.2", ("Tuyển dụng", "Recruiting"), [
        ("A", ("Chính sách tuyển dụng chuẩn", "Standard Policy for Recruiting"),
         ("CSI có chính sách chuẩn cho phương pháp tuyển dụng nhân viên mới "
          "không? Chính sách đã được rà soát tuân thủ mọi quy định hiện hành "
          "chưa? Nhân viên mới được hỏi ý kiến cải tiến quy trình chưa?",
          "Does the CSI have a standard policy for methods of recruiting new "
          "employees? Has it been reviewed for compliance with all applicable "
          "regulations? Are recently hired employees asked for suggestions to "
          "improve the process?")),
    ]),
]

PM = [
    ("4.3.1", ("Lập kế hoạch và phương pháp luận dự án",
               "Project Planning and Methodologies"), [
        "Assignment of Qualified Team Personnel  ·  Phân bổ nhân sự dự án có năng lực",
        "Project Information Review / Approval for Client Expectations  ·  Rà soát và phê duyệt thông tin dự án theo kỳ vọng khách hàng",
        "Project Change Documentation with Client Approval  ·  Lưu hồ sơ thay đổi có phê duyệt của khách hàng",
        "Assigned Personnel Time Commitment  ·  Cam kết thời gian của nhân sự được phân bổ",
        "Key Personnel Briefed on Overall Scope  ·  Nhân sự chủ chốt được phổ biến toàn bộ phạm vi",
        "Project Management Via Plans and Schedules  ·  Quản lý bằng kế hoạch và tiến độ",
        "Risk Management Process / Involves Client  ·  Quy trình quản lý rủi ro có sự tham gia của khách hàng",
    ]),
    ("4.3.2", ("Tiêu chuẩn thiết kế", "Design Standards"), [
        "Promote Development of Standard Design Technique  ·  Thúc đẩy kỹ thuật thiết kế chuẩn, cập nhật",
        "Software Standards Used Consistently and Improved  ·  Chuẩn phát triển phần mềm được dùng nhất quán và cải tiến",
        "Project Execution Methodology Used and Improved  ·  Phương pháp luận thực thi dự án được tuân thủ và cải tiến",
    ]),
    ("4.3.3", ("Quy trình chất lượng dự án", "Project Quality Procedures"), [
        "Verify / Document Deliverables  ·  Kiểm chứng và lập hồ sơ các sản phẩm bàn giao đáp ứng yêu cầu khách hàng",
    ]),
    ("4.3.4", ("Tài liệu hóa", "Documentation"), [
        "Emphasize Accurate / Documented Communications  ·  Nhấn mạnh trao đổi chính xác, có hồ sơ",
        "Prepare Project Manuals for Project Execution  ·  Lập và dùng sổ tay dự án khi thực thi",
        "Method to Track / Store Project Materials  ·  Phương pháp theo dõi, lưu trữ tài liệu dự án và tài liệu đang dở",
    ]),
    ("4.3.5", ("Thử nghiệm và triển khai", "Testing and Implementation"), [
        "Factory / Site acceptance test procedures  ·  Quy trình nghiệm thu tại xưởng và tại hiện trường",
        "Commissioning and start-up practices  ·  Thực hành chạy thử và đưa vào vận hành",
    ]),
    ("4.3.6", ("Đào tạo an toàn trên dự án", "Safety Training on Projects"), [
        "Note: special care should be given to safety and security issues  ·  Lưu ý: cần đặc biệt quan tâm đến an toàn và an ninh",
    ]),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Turnover rate</em> — tỷ lệ nghỉ "
        "việc; một trong những tiêu chí ví dụ xuyên suốt điều 2. · <em>Scope</em> "
        "— phạm vi công việc. · <em>Deliverables</em> — sản phẩm bàn giao. · "
        "<em>WIP / in-progress documents</em> — công việc / tài liệu đang dở. · "
        "<em>Methodology</em> — phương pháp luận thực thi; điều 4.3 nhấn mạnh "
        "<em>không phán xét</em> phương pháp, chỉ kiểm tra nó có được lập hồ sơ và "
        "tuân thủ không.",
        "<b>Key terms.</b> <em>Turnover rate</em> — one of the running example "
        "criteria from §2. · <em>Scope</em> — the work to be done. · "
        "<em>Deliverables</em> — the items handed over. · <em>WIP / in-progress "
        "documents</em> — unfinished work and documents. · <em>Methodology</em> "
        "— execution method; §4.3 stresses it does <em>not judge</em> the "
        "method, only whether it is documented and followed.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Hai nhóm tiêu chí tiếp theo đi sâu vào <em>con người</em> và <em>cách một "
        "dự án được điều hành</em>. Điều 4.2 mở đầu bằng một nhận định rất dứt "
        "khoát: tài sản quý nhất của bất kỳ công ty nào là chính những nhân viên "
        "thực hiện công việc. Điều 4.3 dài hơn và đưa ra nguyên tắc quan trọng "
        "nhất của toàn bộ tiêu chí dự án: <b>không phán xét phương pháp luận, chỉ "
        "kiểm tra nó có được ghi lại và tuân thủ hay không</b>.",
        "The next two criteria families go into <em>people</em> and <em>how a "
        "project is run</em>. §4.2 opens with a blunt observation: the most "
        "valuable asset any company has is the employees who perform the work. "
        "§4.3 is longer and states the single most important principle of the "
        "project criteria: <b>it does not judge the methodology, only whether "
        "that methodology is documented and followed</b>.")))

    # ----------------------------------------------------------------- 4.2
    b.append(h2(A("4.2 · Nhân sự", "4.2 · Human Resources"),
                A("Bốn mối quan tâm", "Four concerns")))
    b.append(fig(1, F.fig_hr_tree()))
    b.append(p(A(
        "«Quản lý nhân sự là một thành phần sống còn của một nhà tích hợp hệ "
        "thống điều khiển thành công.» Bản gốc liệt kê bốn mối quan tâm: "
        "<b>tuân thủ yêu cầu pháp lý, quy trình tuyển dụng, phát triển nhân viên "
        "và chương trình giữ chân</b>. Đây cũng là nhóm gắn trực tiếp với ví dụ "
        "«low turnover rate» (trọng số 7) trong các bước chấm điểm ở điều 2.2.",
        "“The management of human resources is a vital component of a successful "
        "control systems integrator.” The source lists four concerns: "
        "<b>meeting legal requirements, the recruitment process, employee "
        "development and retention programs</b>. This is also the family directly "
        "tied to the “low turnover rate” example (weight 7) in the §2.2 scoring "
        "steps.")))
    for num, (h_vi, h_en), rows in HR:
        b.append(h3(A("%s · %s" % (num, h_vi), "%s · %s" % (num, h_en))))
        b.append(table(
            [A("Mục", "Item"), A("Tiêu chí", "Criterion"),
             A("Câu hỏi cần hỏi", "Question to ask")],
            [[r[0], A(r[1][0], r[1][1]), A(r[2][0], r[2][1])] for r in rows],
            A("Các câu hỏi gợi ý của điều %s." % num,
              "Suggested questions from clause %s." % num)))
    b.append(h3(A("4.2.3 · Do người dùng tự định nghĩa",
                  "4.2.3 · User Defined")))
    b.append(p(A(
        "Bốn hàng trống A–D. Trong thực tế, đây là nơi khách hàng thường đưa vào "
        "yêu cầu về chứng chỉ chuyên môn, đào tạo an toàn bắt buộc tại nhà máy, "
        "hoặc cơ chế kiểm tra lý lịch đối với nhân sự làm việc tại khu vực hạn "
        "chế.",
        "Four blank rows A–D. In practice this is where clients commonly add "
        "professional certification requirements, mandatory site safety "
        "training, or background-check arrangements for staff working in "
        "restricted areas.")))

    # ----------------------------------------------------------------- 4.3
    b.append(h2(A("4.3 · Quản lý dự án", "4.3 · Project Management"),
                A("Nguyên tắc không phán xét phương pháp",
                  "The no-judgment principle")))
    b.append(quote(A(
        "«Mục đích không phải là phán xét bản thân phương pháp luận, mà là bảo đảm "
        "rằng các phương pháp luận được lập thành hồ sơ và được tuân thủ, trong "
        "tương quan với phạm vi dự án.»",
        "«The purpose is not to judge the actual methodology, but to ensure the "
        "methodologies are documented and followed as related to the project "
        "scope.»"),
        A("CSIA Guide, Volume 1, điều 4.3, trang 19",
          "CSIA Guide, Volume 1, §4.3, page 19")))
    b.append(p(A(
        "Phạm vi được nêu rất rộng: độ rõ ràng của phạm vi công việc, mức độ kỹ "
        "càng của kế hoạch, cấu trúc đội dự án, thực hành / tiêu chuẩn, phương "
        "pháp luận thực thi, tài liệu hóa, quy trình chất lượng, thử nghiệm và "
        "chạy thử. Bảy nhóm con dưới đây đi theo đúng trình tự vòng đời dự án.",
        "The stated scope is broad: clarity of scope, thoroughness of work "
        "planning, project team structure, practices/standards, project "
        "execution methodologies, documentation, quality procedures, testing "
        "and commissioning. The seven sub-groups below follow the project "
        "lifecycle in order.")))
    b.append(fig(2, F.fig_project_lifecycle()))
    for num, (h_vi, h_en), items in PM:
        b.append(h3(A("%s · %s" % (num, h_vi), "%s · %s" % (num, h_en))))
        b.append(ul([A("· " + s.split("  ·  ")[1] if "  ·  " in s else s,
                       "· " + s.split("  ·  ")[0] if "  ·  " in s else s)
                     for s in items]))
    b.append(h3(A("4.3.7 · Do người dùng tự định nghĩa",
                  "4.3.7 · User Defined")))
    b.append(note(A(
        "<b>Câu hỏi có chủ đích kép.</b> Nhiều câu ở 4.3.1 hỏi cả về bản thân quy "
        "trình <em>và</em> về sự tham gia của khách hàng — phê duyệt yêu cầu chức "
        "năng, phê duyệt thay đổi về tiến độ / chi phí / khối lượng công việc, và "
        "quy trình quản lý rủi ro có khách hàng tham gia. Đây là cách tiêu chuẩn "
        "biến «quản lý dự án» thành một quan hệ hai chiều có thể kiểm chứng.",
        "<b>Questions with a double edge.</b> Several 4.3.1 questions ask both "
        "about the process itself <em>and</em> about client involvement — "
        "approval of functional requirements, approval of schedule / cost / "
        "work changes, and a risk-management procedure that involves the client. "
        "This is how the standard turns “project management” into a verifiable "
        "two-way relationship.")))
    b.append(ul([
        A("<b>Gắn với điều 2.3.</b> «Có tài liệu hóa và có tuân thủ không» chính "
          "là ranh giới giữa mức 2 và mức 3 của thang điểm hiệu năng.",
          "<b>Link to §2.3.</b> “Documented and followed” is precisely the "
          "boundary between level 2 and level 3 on the performance scale."),
        A("<b>Gắn với điều 4.7.4.</b> Quy trình quản lý rủi ro ở 4.3.1 G là tiền "
          "đề để bước 7 của điều 2.2 (đánh giá rủi ro) có dữ liệu mà dùng.",
          "<b>Link to §4.7.4.</b> The 4.3.1 G risk-management procedure supplies "
          "the evidence that step 7 of §2.2 needs."),
        A("<b>An toàn và an ninh.</b> Điều 4.3.6 kèm lưu ý in đậm: «Special care "
          "should be given to safety and security issues» — vang lại tín điều "
          "«mọi tai nạn đều có thể phòng tránh» ở chương 1.",
          "<b>Safety and security.</b> §4.3.6 carries a bold note: “Special care "
          "should be given to safety and security issues” — echoing the "
          "“all accidents are preventable” belief in Chapter 1."),
    ]))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
