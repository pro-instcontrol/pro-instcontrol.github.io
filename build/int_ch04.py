# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 4: CSIA registration (§3), criteria intro and
General Management (§4.1), printed pages 11–16."""
import intfig as F
from int_common import T, fig, h2, h3, lead, note, ol, p, quote, table, ul

PAGES_SRC = 6
BYLINE = "CSIA · Guide Vol. 1 (2000) · §3, §4.1"

GM = [
    ("4.1.1", ("Quản lý chiến lược", "Strategic Management"), [
        ("A", ("Định nghĩa / làm rõ mục tiêu chiến lược",
               "Defined / Clear Strategic Objectives"),
         ("CSI có rõ ràng về mục đích, mục tiêu chiến lược và mục tiêu của mình "
          "không? Có tuyên bố sứ mệnh hay tầm nhìn không?",
          "Is the CSI clear about its purpose, strategic objectives and goals? "
          "Does it have a mission or vision statement?")),
        ("B", ("Mục tiêu ngắn hạn được theo dõi định kỳ",
               "Regularly Monitored Short Range Objectives"),
         ("Các mục tiêu ngắn hạn có được thiết lập định kỳ và hiệu quả có được "
          "giám sát không?",
          "Are short-range objectives regularly established and performance "
          "monitored?")),
        ("C", ("Kế hoạch chuyển giao quyền sở hữu / quản lý",
               "Formulated Owner/Management Transition"),
         ("Có kế hoạch chuyển giao quyền sở hữu và quản lý được xây dựng và ai "
          "cũng hiểu không (tức là quy hoạch người kế nhiệm)?",
          "Is there a formulated and understood plan for ownership and "
          "management transition (succession planning)?")),
    ]),
    ("4.1.2", ("Cơ cấu tổ chức", "Organizational Structure"), [
        ("A", ("Sơ đồ / cơ cấu tổ chức", "Organization Chart / Structure"),
         ("Có cơ cấu tổ chức được hiểu rõ không? Cơ cấu đó có ổn định không?",
          "Is there a well-understood organisational structure? Is it stable?")),
        ("B", ("Sổ tay thủ tục văn phòng", "Office Procedures Manual"),
         ("CSI có sổ tay thủ tục văn phòng không?",
          "Does the CSI have an Office Procedures manual?")),
    ]),
    ("4.1.3", ("Cơ sở vật chất và thiết bị", "Facilities and Equipment"), [
        ("A", ("Thiết bị văn phòng / hiện trường cần thiết, được bảo trì",
               "Necessary Office/Field Equipment Available/Maintained"),
         ("Thiết bị văn phòng và hiện trường cần thiết có sẵn và được bảo trì tốt "
          "không?",
          "Is necessary office and field equipment available and well maintained?")),
        ("B", ("Lưu trữ dự án kỹ thuật / lịch sử",
               "Technical/Historical Project Archive"),
         ("CSI có duy trì một kho lưu trữ tập trung với tài liệu kỹ thuật, hồ sơ và "
          "các dự án lịch sử được sắp xếp để truy xuất không?",
          "Does the CSI maintain a central filing facility with technical "
          "literature, documents and historical projects arranged for retrieval?")),
    ]),
    ("4.1.4", ("Quản lý hệ thống máy tính", "Computer System Management"), [
        ("A", ("Chính sách hệ thống máy tính được lập thành văn bản",
               "Documented Computer System Policy"),
         ("Có chính sách viết bằng văn bản cho hệ thống máy tính không — phần mềm "
          "được phép, quyền giám sát, thủ tục bảo trì, bảo hiểm, an ninh?",
          "Is there a written policy for its computer systems: allowable "
          "software, monitoring rights, maintenance procedures, insurance "
          "coverage and security?")),
        ("B", ("Nhân viên hiểu rằng sao chép phần mềm trái phép là vi phạm",
               "Unauthorized SW Copying Violation Understanding"),
         ("Nhân viên có hiểu rằng sao chép phần mềm trái phép vi phạm thỏa thuận "
          "với nhà cung cấp phần mềm và là tội hình sự không?",
          "Do employees understand that unauthorized software copying violates "
          "the CSI's agreement with the software provider and is a felony?")),
        ("C", ("Quản lý chứng từ mua phần mềm", "Software Purchase Proof Management"),
         ("Ban quản lý có lưu giữ chứng từ mua cho mọi phần mềm đã mua không?",
          "Does management maintain proof of purchase for all software purchases?")),
        ("D", ("Hệ thống sao lưu thông tin đầy đủ",
               "Adequate Backup System for Information"),
         ("Có hệ thống sao lưu đầy đủ không (hằng ngày, lưu trữ ngoài trụ sở, "
          "người phụ trách, luân chuyển phương tiện sao lưu)?",
          "Is there an adequate backup system — daily, off-site storage, an "
          "assigned person and rotated backup media?")),
        ("E", ("Duy trì thư viện hỗ trợ phần mềm", "Maintain Software Support Library"),
         ("CSI có duy trì thư viện phần mềm (CAD, chương trình PLC, chương trình "
          "máy tính) cho người dùng nội bộ không?",
          "Does the CSI maintain a library of software (CAD, PLC programs, "
          "computer programs) for internal users?")),
        ("F", ("Hướng dẫn chuyển giao giấy phép phần mềm",
               "Software License Transfer Practice Guideline"),
         ("Có quy thực hành ghi nhận việc tuân thủ các hướng dẫn cần thiết để "
          "chuyển giấy phép phần mềm cho khách hàng đúng thỏa thuận của nhà sản "
          "xuất không?",
          "Is there a practice for documenting compliance with the guidelines "
          "needed to pass software licences to customers in accordance with the "
          "manufacturer's licence agreement?")),
    ]),
    ("4.1.5", ("Bảo hiểm tổn thất", "Loss Insurance"), [
        ("A", ("Bảo hiểm đầy đủ cho CSI và khách hàng",
               "Adequate Insurance / CSI & Client"),
         ("Công ty có mua bảo hiểm đầy đủ không (trách nhiệm chung, tài sản, tai "
          "nạn, trộm cắp, ô tô, bồi thường lao động, hệ thống máy tính, vận "
          "chuyển thiết bị)?",
          "Does the firm carry adequate insurance — general liability, property, "
          "casualty, theft, auto, workers' compensation, computer systems and "
          "hardware/equipment transport?")),
        ("B", ("Bảo hiểm nhân sự chủ chốt / mua lại cổ phần",
               "Key Man and/or Buyout Insurance"),
         ("Công ty có mua bảo hiểm nhân sự chủ chốt và/hoặc bảo hiểm mua lại cho "
          "chủ sở hữu / nhân sự then chốt không?",
          "Does the firm carry key-man and/or buyout insurance on owners and/or "
          "key staff?")),
        ("C", ("Công việc được ủy quyền bằng hợp đồng", "Work Contractually Authorized"),
         ("Công việc do CSI thực hiện có được ủy quyền bằng hợp đồng không?",
          "Is the work done by the CSI contractually authorized?")),
        ("D", ("Theo dõi WIP / % hoàn thành",
               "WIP / % Complete Performance Tracking"),
         ("Ban quản lý có nhận các chỉ số hiệu năng then chốt kịp thời không? Có "
          "giám sát tỷ lệ hoàn thành không?",
          "Does management receive key performance indicators in a timely "
          "fashion? Do they monitor percent completion?")),
        ("E", ("Bảo hiểm sai sót và thiếu sót", "Errors and Omissions"),
         ("Công ty có mua bảo hiểm sai sót và thiếu sót đầy đủ khi được yêu cầu "
          "không?",
          "Does the firm carry adequate errors and omissions insurance when "
          "required?")),
    ]),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Registration</em> — đăng ký CSIA "
        "sau kiểm toán của bên thứ ba độc lập. · <em>Audit</em> — kiểm toán theo "
        "tiêu chí Best Practices & Benchmarks. · <em>Suggested criteria</em> — "
        "bộ câu hỏi gợi ý ở điều 4, không phải bài kiểm tra đạt / trượt. · "
        "<em>User Defined</em> — các hàng A–D để khách hàng tự thêm tiêu chí. · "
        "<em>GAAP / WIP</em> — nguyên tắc kế toán được chấp nhận chung / công "
        "việc đang dở (sẽ gặp ở chương 6).",
        "<b>Key terms.</b> <em>Registration</em> — CSIA recognition following an "
        "independent third-party audit. · <em>Audit</em> — assessment against "
        "the Best Practices & Benchmarks criteria. · <em>Suggested criteria</em> "
        "— the §4 question set, not a pass/fail test. · <em>User Defined</em> — "
        "blank A–D rows for client-added criteria. · <em>GAAP / WIP</em> — "
        "generally accepted accounting procedures / work in progress (Chapter 6).",
        lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Đây là điểm chuyển của tập sách: từ <em>cách quyết định</em> sang "
        "<em>nội dung cần quyết định</em>. Điều 3 đưa ra một lối tắt — nếu CSI đã "
        "đăng ký CSIA, khách hàng có thể bỏ qua phần lớn bảng phân tích. Điều 4 "
        "sau đó liệt kê bảy nhóm tiêu chí gợi ý, bắt đầu bằng Quản lý chung. Cần "
        "nhớ: các mục trong điều 4 là <b>câu hỏi</b> để khách hàng tự cân nhắc, "
        "không phải danh mục bắt buộc phải đạt.",
        "This is the volume's turning point: from <em>how to decide</em> to "
        "<em>what to decide about</em>. §3 offers a shortcut — if a CSI is CSIA "
        "Registered, the client may skip much of the analysis table. §4 then "
        "lists seven families of suggested criteria, starting with General "
        "Management. Remember: the §4 items are <b>questions</b> for the client "
        "to weigh, not a mandatory pass list.")))

    # ------------------------------------------------------------ section 3
    b.append(h2(A("3 · Chương trình đăng ký CSIA", "3 · CSIA Registration Program"),
                A("Kiểm toán độc lập thay cho tự đánh giá",
                  "Independent audit instead of self-assessment")))
    b.append(fig(1, F.fig_registration_flow()))
    b.append(ol([
        A("<b>Đánh giá nhanh.</b> Đăng ký CSIA cung cấp cho khách hàng phương pháp "
          "hiệu quả để đánh giá một CSI ngay lập tức. Tiêu chí đăng ký được xây "
          "dựng chung bởi CSI, khách hàng và nhà sản xuất để phản ánh yêu cầu của "
          "các bên liên quan đến triển khai hệ thống điều khiển.",
          "<b>Immediate evaluation.</b> CSIA registration gives the client an "
          "effective method for immediate evaluation of a CSI. The criteria were "
          "jointly developed by CSIs, clients and manufacturers to reflect the "
          "requirements of the parties involved in implementing control systems."),
        A("<b>Bên thứ ba độc lập.</b> Một tổ chức bên thứ ba độc lập thực hiện "
          "cuộc kiểm toán đăng ký dựa trên tiêu chí Best Practices & Benchmarks.",
          "<b>Independent third party.</b> An independent third-party "
          "organisation conducts the registration audit of a CSI against the "
          "CSIA Best Practices and Benchmarks criteria."),
        A("<b>Danh sách công khai.</b> Những hội viên đạt đăng ký được liệt kê trên "
          "website của CSIA (www.controlsys.org).",
          "<b>Public register.</b> Members who successfully achieve registration "
          "are identified on the CSIA website (www.controlsys.org)."),
        A("<b>Giảm nỗ lực, chi phí và rủi ro.</b> Đăng ký giúp nhận diện ngay "
          "những CSI đã đạt một thước đo ngành đã được thiết lập.",
          "<b>Less effort, cost and risk.</b> Registration identifies those CSIs "
          "that have met an established industry metric."),
        A("<b>Phạm vi tiêu chí.</b> Tiêu chí đăng ký bao gồm Quản lý chung, Nhân "
          "sự & Phát triển chuyên môn, Quản lý dự án, Quản lý chất lượng, Quản lý "
          "tài chính và Phát triển kinh doanh — tức <b>các điều 4.1 đến 4.6</b>.",
          "<b>Scope of the criteria.</b> Registration addresses General "
          "Management, Human Resources & Professional Development, Project "
          "Management, Quality Management, Financial Management and Business "
          "Development — i.e. <b>§§4.1 through 4.6</b>."),
    ]))
    b.append(quote(A(
        "«Người dùng có thể bỏ qua các mục 4.1 đến 4.6.5 của bảng phân tích nếu "
        "CSI được đánh giá đã đăng ký CSIA!»",
        "«Users may wish to skip Section 4.1 through 4.6.5 of analysis table if "
        "the CSI being evaluated is CSIA Registered!»"),
        A("CSIA Guide, Volume 1, điều 2.5, trang 8",
          "CSIA Guide, Volume 1, §2.5, page 8")))

    # ------------------------------------------------------------ section 4
    b.append(h2(A("4 · Bộ tiêu chí gợi ý", "4 · Suggested criteria"),
                A("Bảy nhóm, hàng chỗ trống cho khách hàng",
                  "Seven families, with blank rows for the client")))
    b.append(p(A(
        "Điều 4 «phác thảo các tiêu chí gợi ý mà khách hàng nên cân nhắc trong "
        "quá trình ra quyết định lựa chọn». Ngay dưới tiêu đề, bản gốc chừa chỗ "
        "trống và ghi chú: «Khách hàng có thể dùng chỗ trống để thêm tiêu chí và "
        "định nghĩa của riêng mình». Mỗi nhóm con vì thế đều kết thúc bằng một "
        "mục <em>User Defined</em> với các hàng A, B, C, D để tự điền.",
        "§4 “outlines the suggested criteria that the client should take into "
        "consideration during the selection decision-making process”. Immediately "
        "below the heading the source leaves blank space with the note: “Clients "
        "can use blank space to add their own criteria and definitions”. Every "
        "sub-group therefore ends with a <em>User Defined</em> item carrying "
        "blank A, B, C, D rows.")))
    b.append(fig(2, F.fig_criteria_map()))
    b.append(note(A(
        "<b>Đọc bảng chấm điểm cùng với điều 4.</b> Số hiệu trong cột đầu của bảng "
        "mẫu (điều 2.5) và phiếu trống (Phụ lục B) chính là số điều ở đây. "
        "<code>4.1.1 A</code> trong bảng tương ứng với câu hỏi «Defined/Clear "
        "Strategic Objectives» bên dưới.",
        "<b>Read the scoring table together with §4.</b> The numbers in the first "
        "column of the §2.5 sample table and the Appendix B blank form are these "
        "clause numbers. <code>4.1.1 A</code> in the table corresponds to the "
        "“Defined/Clear Strategic Objectives” question below.")))

    # ------------------------------------------------------------- 4.1
    b.append(h2(A("4.1 · Quản lý chung", "4.1 · General Management"),
                A("Mục đích, kế hoạch dài hạn, mục tiêu",
                  "Purpose, long-range plans, objectives and goals")))
    b.append(p(A(
        "Lời dẫn của điều 4.1 (và lặp lại ở 4.1.1) xác định phạm vi: các tiêu chí "
        "gắn với <b>mục đích, kế hoạch dài hạn, mục tiêu và mục tiêu vận hành</b> "
        "của CSI. Sáu nhóm con trải từ chiến lược, cơ cấu tổ chức, cơ sở vật "
        "chất, quản trị hệ thống máy tính, bảo hiểm, đến phần tự định nghĩa.",
        "The 4.1 introduction (repeated at 4.1.1) sets the scope: criteria "
        "associated with the CSI's <b>purpose, long-range plans, objectives and "
        "goals</b>. Six sub-groups run from strategy, organisational structure, "
        "facilities, computer-system management and insurance to a user-defined "
        "tail.")))
    for num, (h_vi, h_en), rows in GM:
        b.append(h3(A("%s · %s" % (num, h_vi), "%s · %s" % (num, h_en))))
        b.append(table(
            [A("Mục", "Item"), A("Tiêu chí", "Criterion"),
             A("Câu hỏi cần hỏi", "Question to ask")],
            [[r[0], A(r[1][0], r[1][1]), A(r[2][0], r[2][1])] for r in rows],
            A("Các câu hỏi gợi ý của điều %s." % num,
              "Suggested questions from clause %s." % num)))
    b.append(h3(A("4.1.6 · Do người dùng tự định nghĩa",
                  "4.1.6 · User Defined")))
    b.append(p(A(
        "Bản gốc để trống bốn hàng A–D. Đây là nơi khách hàng đưa vào các yêu cầu "
        "đặc thù mà tập sách không thể bao quát — ví dụ chứng nhận an toàn thông "
        "tin, yêu cầu nội địa hóa, hay tiêu chuẩn ngành riêng. Phần cảnh báo ở "
        "trang i nhắc rằng chính người dùng chịu trách nhiệm về các tiêu chí này.",
        "The source leaves four blank rows A–D. This is where clients insert the "
        "project-specific requirements the guide cannot cover — for example "
        "information-security certification, localisation requirements or a "
        "sector-specific standard. The disclaimer on page i reminds us that "
        "users are solely responsible for their own criteria.")))
    b.append(ul([
        A("<b>Chủ đề lặp lại: tài liệu hóa.</b> Sổ tay thủ tục, chính sách máy tính "
          "bằng văn bản, chứng từ mua phần mềm, lưu trữ dự án — tất cả đều hỏi «có "
          "ghi lại không?», đúng với thang điểm 0–5 ở điều 2.3.",
          "<b>Recurring theme: documentation.</b> Procedures manual, written "
          "computer policy, software purchase proofs, project archive — all ask "
          "“is it recorded?”, matching the 0–5 scale in §2.3."),
        A("<b>Chủ đề lặp lại: tính liên tục.</b> Quy hoạch người kế nhiệm, sao lưu "
          "ngoài trụ sở, bảo hiểm nhân sự chủ chốt và bảo hiểm sai sót & thiếu "
          "sót đều là câu hỏi về khả năng sống sót của nhà cung cấp trong suốt "
          "vòng đời dự án.",
          "<b>Recurring theme: continuity.</b> Succession planning, off-site "
          "backups, key-man insurance and errors & omissions cover are all "
          "questions about the supplier's ability to survive the project "
          "lifecycle."),
        A("<b>Ranh giới với điều 2.4.</b> Các CSI lớn cần nhiều hạ tầng hơn; vì "
          "vậy cùng một câu hỏi nhưng điểm «Good» gợi ý khác nhau theo Level 1 / "
          "2 / 3.",
          "<b>Link back to §2.4.</b> Larger CSIs need more infrastructure, so "
          "the same question carries a different suggested “Good” score at "
          "Level 1 / 2 / 3."),
    ]))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
