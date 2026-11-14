# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 6: Quality Management (§4.4), Financial
Management (§4.5) and Business Development (§4.6), printed pages 24–32."""
import intfig as F
from int_common import T, fig, h2, h3, lead, note, ol, p, quote, table, ul

PAGES_SRC = 9
BYLINE = "CSIA · Guide Vol. 1 (2000) · §§4.4–4.6"

FIN = [
    ("4.5.1", ("Các thước đo hiệu năng tài chính",
               "Measures of Financial Performance"), [
        ("A", ("Hệ thống tài chính theo GAAP", "GAAP Financial System in Operation"),
         ("Có hệ thống tài chính đang vận hành, cung cấp vết kiểm toán dễ theo "
          "dõi để xác minh mọi hồ sơ tài chính theo GAAP không?",
          "Are financial systems in operation providing an easy-to-follow audit "
          "trail for verification of all financial records using GAAP?")),
        ("B", ("Phương pháp / báo cáo kế toán kịp thời",
               "Timely Accounting Methods / Reports"),
         ("Phương pháp kế toán (tiền mặt hay dồn tích) có tương ứng với các báo "
          "cáo tài chính được lập kịp thời và định kỳ không?",
          "Do accounting methods (cash or accrual basis) correspond with "
          "financial reports generated in a timely, periodic manner?")),
    ]),
    ("4.5.2", ("Hoạch định tài chính", "Financial Planning"), [
        ("A", ("Dự báo dòng tiền theo hạn mức tín dụng / tiền mặt",
               "Cash Flow Forecast Requirements via Credit/Cash"),
         ("Dự báo dòng tiền có dựa trên nhu cầu hiện tại và tương lai liên quan "
          "đến các hạn mức tín dụng và tiền mặt không?",
          "Is the cash flow forecast based on current and future requirements "
          "as related to lines of credit and cash?")),
    ]),
    ("4.5.3", ("Thủ tục lập hóa đơn", "Billing Procedures"), [
        ("A", ("Thủ tục thay đổi để lập hóa đơn đúng",
               "Change Procedures in Place for Proper Billing"),
         ("Có thủ tục bảo đảm các thay đổi phạm vi và phần việc bổ sung được lập "
          "hóa đơn đúng không?",
          "Are procedures in place to ensure changes in scope and additions are "
          "billed properly?")),
        ("B", ("Hóa đơn được kiểm tra độ chính xác / tuân thủ",
               "Invoices Checked for Accuracy/Compliance"),
         ("Hóa đơn có được kiểm tra độ chính xác, sự tuân thủ hợp đồng gốc và "
          "tính phù hợp trước khi gửi khách hàng không?",
          "Are invoices checked for accuracy, compliance to the original "
          "contract and suitability before being sent to the client?")),
        ("C", ("Phương pháp giám sát % hoàn thành / WIP",
               "Monitoring Method for % Completion/WIP"),
         ("Việc giám sát tỷ lệ hoàn thành và công việc đang dở có được thực hiện "
          "một cách hệ thống và nhất quán không?",
          "Are percent completion and work in progress monitored in a "
          "systematic and consistent manner?")),
        ("D", ("Theo dõi công nợ phải thu, xử lý nợ quá hạn",
               "A/R Monitored with Overdue Accounts Pursued"),
         ("Các khoản phải thu có được theo dõi, phân loại theo tuổi nợ và các "
          "tài khoản quá hạn có được đôn đốc ở mức cần thiết không?",
          "Is A/R monitored and aged, with overdue accounts pursued with the "
          "necessary level of aggressiveness?")),
    ]),
    ("4.5.4", ("Báo cáo tài chính dự án", "Project Financial Reporting"), [
        ("A", ("Hệ thống kiểm soát / tính giá thành dự án",
               "Project Control Job Cost System"),
         ("CSI có hệ thống kiểm soát / tính giá thành dự án phù hợp với quy mô và "
          "mức độ tham gia của dự án không?",
          "Does the CSI have a project control / job cost system to match "
          "project size and level of project involvement?")),
        ("B", ("Báo cáo giá thành được rà soát kịp thời",
               "Timely Review Job Cost System Reports"),
         ("Các báo cáo của hệ thống giá thành có được lập và rà soát trong khung "
          "thời gian có ý nghĩa không?",
          "Are job cost system reports generated and reviewed in a meaningful "
          "time frame?")),
        ("C", ("Yêu cầu dự báo chi phí đến khi hoàn thành",
               "Does Job Cost Require Forecast-to-Complete"),
         ("Hệ thống giá thành có yêu cầu một bản dự báo chi phí đến khi hoàn "
          "thành không?",
          "Does the job cost system require a forecast-to-complete?")),
    ]),
    ("4.5.5", ("Chính sách thuế", "Tax Policy"), [
        ("A", ("Thuế bán hàng / sử dụng được thu, nộp và lưu hồ sơ",
               "Sales/Use Taxes Collected/Paid with Records"),
         ("Thuế bán hàng và thuế sử dụng có được thu, nộp và lưu hồ sơ đúng "
          "không?",
          "Are sales and use taxes collected and paid, with proper records "
          "maintained?")),
        ("B", ("Thuế lương nộp đúng hạn, đúng thủ tục",
               "Payroll Taxes Paid in Timely and Proper Manner"),
         ("Thuế lương có được nộp đúng hạn và kê khai đúng không?",
          "Are payroll taxes paid in a timely manner and properly filed?")),
        ("C", ("Thuế liên bang được ước tính và nộp theo quy định",
               "Federal Taxes Estimated/Paid as Required"),
         ("Thuế liên bang có được ước tính và nộp theo yêu cầu không?",
          "Are federal taxes estimated and paid as required?")),
    ]),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>GAAP</em> — Generally Acceptable "
        "Accounting Procedures, các nguyên tắc kế toán được chấp nhận chung. · "
        "<em>WIP</em> — work in progress, công việc đang dở. · <em>A/R</em> — "
        "accounts receivable, khoản phải thu. · <em>Job cost / forecast-to-complete</em> "
        "— tính giá thành dự án / dự báo chi phí đến khi hoàn thành. · "
        "<em>Hold harmless clause</em> — điều khoản miễn trừ trách nhiệm. · "
        "<em>Intellectual property ownership</em> — quyền sở hữu tài sản trí tuệ "
        "đối với phần mềm ứng dụng.",
        "<b>Key terms.</b> <em>GAAP</em> — Generally Acceptable Accounting "
        "Procedures. · <em>WIP</em> — work in progress. · <em>A/R</em> — accounts "
        "receivable. · <em>Job cost / forecast-to-complete</em> — project cost "
        "system and the estimate of cost still to be incurred. · <em>Hold "
        "harmless clause</em> — a clause shifting liability away from one party. "
        "· <em>Intellectual property ownership</em> — ownership of the "
        "application software delivered.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Ba nhóm tiêu chí này kiểm tra <em>sức khỏe của chính tổ chức cung cấp "
        "dịch vụ</em>: hệ thống chất lượng, kỷ luật tài chính và cách công ty "
        "giành được công việc. Chúng chiếm các trang 24–32 và cũng là phần cuối "
        "của phạm vi đăng ký CSIA (§§4.1–4.6). Điều 4.7 — nhóm kỹ thuật — nằm "
        "ngoài phạm vi đăng ký và được tách sang chương 7.",
        "These three criteria families test the <em>health of the supplying "
        "organisation itself</em>: its quality system, financial discipline and "
        "how it wins work. They span pages 24–32 and complete the scope of CSIA "
        "registration (§§4.1–4.6). §4.7 — the technical family — falls outside "
        "the registration scope and is covered separately in Chapter 7.")))

    # ----------------------------------------------------------------- 4.4
    b.append(h2(A("4.4 · Quản lý chất lượng", "4.4 · Quality Management"),
                A("Năm nhóm, một vòng lặp", "Five groups, one loop")))
    b.append(fig(1, F.fig_quality_loop()))
    b.append(table(
        [A("Điều", "Clause"), A("Nhóm", "Group"),
         A("Câu hỏi tiêu biểu", "Representative question")],
        [
            ["4.4.1", A("Lãnh đạo", "Leadership"),
             A("CSI có tổ chức các cuộc họp về chất lượng không?",
               "Does the CSI conduct meetings on quality?")],
            ["4.4.2", A("Trao đổi hiệu quả", "Effective Communication"),
             A("Thông tin chất lượng có được truyền đạt rõ ràng trong tổ chức "
               "không?",
               "Is quality information clearly communicated across the firm?")],
            ["4.4.3", A("Cải tiến liên tục, đo lường được",
                        "Continuous, Measurable Improvements"),
             A("CSI có kiểm chứng và lập hồ sơ rằng khách hàng hài lòng với dự "
               "án không?",
               "Does the CSI verify and document that the client is satisfied "
               "with the project?")],
            ["4.4.4", A("Dịch vụ khách hàng", "Customer Service"),
             A("Có quy trình xử lý khiếu nại và theo đuổi đến khi vấn đề được "
               "giải quyết theo sự hài lòng của khách hàng không?",
               "Is there an established complaint procedure, with follow-through "
               "to ensure resolution to the customer's satisfaction?")],
            ["4.4.5", A("Do người dùng tự định nghĩa", "User Defined"),
             A("Bốn hàng trống A–D cho tiêu chí riêng của khách hàng.",
               "Four blank A–D rows for client-specific criteria.")],
        ],
        A("Năm nhóm tiêu chí của điều 4.4, rút gọn từ trang 24–25.",
          "The five §4.4 criteria groups, condensed from pages 24–25.")))
    b.append(note(A(
        "<b>Vang lại tín điều.</b> «Nỗ lực chất lượng sinh lợi hơn khi hướng vào "
        "phòng ngừa thay vì sửa lỗi» (chương 1) giải thích vì sao 4.4.3 đòi "
        "<em>kiểm chứng và lập hồ sơ</em> sự hài lòng, thay vì chỉ hỏi có nhận "
        "khiếu nại hay không. Đây cũng chính là khác biệt giữa điểm 4 và điểm 5 "
        "trong thang 0–5 của điều 2.3: cải tiến liên tục phải được "
        "<em>chứng minh</em>.",
        "<b>The belief echoes here.</b> “Quality efforts are more productive when "
        "directed toward prevention rather than correction” (Chapter 1) explains "
        "why 4.4.3 requires satisfaction to be <em>verified and documented</em> "
        "rather than merely asking whether complaints are received. It is also "
        "exactly the difference between scores 4 and 5 on the §2.3 scale: "
        "continual improvement must be <em>demonstrated</em>.")))

    # ----------------------------------------------------------------- 4.5
    b.append(h2(A("4.5 · Quản lý tài chính", "4.5 · Financial Management"),
                A("Quản trị, kiểm soát, báo cáo và hoạch định",
                  "Manage, control, report and plan")))
    b.append(p(A(
        "«Các khía cạnh tài chính và kế toán của CSI cần tập trung vào những "
        "phương tiện cụ thể để quản lý, kiểm soát, báo cáo và hoạch định nguồn "
        "tài chính của công ty.» Sáu nhóm con đi từ hệ thống kế toán, hoạch định, "
        "lập hóa đơn, báo cáo giá thành dự án, thuế, đến phần tự định nghĩa.",
        "“The financial and accounting aspects of the control systems integrator "
        "should focus on the specific means required to manage, control, report, "
        "and plan the company's financial resources.” Six sub-groups run from "
        "the accounting system, planning, billing, project financial reporting "
        "and tax policy to a user-defined tail.")))
    b.append(fig(2, F.fig_financial_map()))
    for num, (h_vi, h_en), rows in FIN:
        b.append(h3(A("%s · %s" % (num, h_vi), "%s · %s" % (num, h_en))))
        b.append(table(
            [A("Mục", "Item"), A("Tiêu chí", "Criterion"),
             A("Câu hỏi cần hỏi", "Question to ask")],
            [[r[0], A(r[1][0], r[1][1]), A(r[2][0], r[2][1])] for r in rows],
            A("Các câu hỏi gợi ý của điều %s." % num,
              "Suggested questions from clause %s." % num)))
    b.append(p(A(
        "Điều 4.5.6 (User Defined) khép nhóm bằng bốn hàng trống A–D. Các câu hỏi "
        "về WIP, % hoàn thành và dự báo chi phí đến khi hoàn thành đặc biệt đáng "
        "chú ý với khách hàng: chúng là tín hiệu sớm cho thấy một dự án đang "
        "vượt ngân sách trước khi hóa đơn tiếp theo tới.",
        "§4.5.6 (User Defined) closes the family with four blank A–D rows. The "
        "WIP, percent-completion and forecast-to-complete questions are "
        "especially valuable to clients: they are early signals that a project "
        "is overrunning before the next invoice arrives.")))

    # ----------------------------------------------------------------- 4.6
    b.append(h2(A("4.6 · Phát triển kinh doanh", "4.6 · Business Development"),
                A("Sống còn, nhưng đừng quá đà", "Essential, but not overzealous")))
    b.append(quote(A(
        "«Một chương trình phát triển kinh doanh hiệu quả là cần thiết cho sự tồn "
        "vong của mọi CSI. Cơ hội mới phải đến với nhịp độ tương đối ổn định và "
        "với những điều khoản đem lại sự ổn định tài chính. Đồng thời, việc quảng "
        "bá quá hăng hái có thể làm xáo trộn các mặt khác trong hoạt động của "
        "CSI.»",
        "«An effective business development program is required for the survival "
        "of every control systems integrator. New opportunities must be "
        "forthcoming at a reasonably steady rate and on terms that will provide "
        "the control systems integrator with financial stability. At the same "
        "time, overly zealous promotion can disrupt other aspects of a control "
        "systems integrator's practice.»"),
        A("CSIA Guide, Volume 1, điều 4.6, trang 29",
          "CSIA Guide, Volume 1, §4.6, page 29")))
    b.append(fig(3, F.fig_business_flow()))
    b.append(table(
        [A("Điều", "Clause"), A("Nhóm", "Group"),
         A("Câu hỏi tiêu biểu", "Representative question")],
        [
            ["4.6.1", A("Thực hành phát triển kinh doanh",
                        "Business Development Practices"),
             A("Tài liệu tiếp thị có phản ánh đúng công ty và năng lực, không gây "
               "hiểu sai cho khách hàng không? Hồ sơ năng lực cá nhân có chính "
               "xác không? Quan hệ với đại diện / VAR / đối tác có được định "
               "nghĩa rõ không?",
               "Do marketing materials accurately represent the company and its "
               "capabilities? Are individual resumes accurate and consistent? "
               "Are relationships with representatives, VARs and partners "
               "clearly defined?")],
            ["4.6.2", A("Xây dựng hồ sơ chào giá", "Development of Proposals"),
             A("Khi nào và tại sao công ty nói «không»? Có hướng dẫn xác định "
               "phạm vi công việc / cung ứng chính xác không? Có chuẩn ước tính "
               "và định giá, cùng chính sách rà soát phê duyệt nội bộ không?",
               "When and why does the firm say “no”? Are there guidelines for "
               "defining the precise scope of work and supply? Do estimating and "
               "pricing standards exist, along with an administrative review "
               "and approval policy?")],
            ["4.6.3", A("Đàm phán và ký kết hợp đồng",
                        "Negotiating and Contracting"),
             A("Có bộ chứng từ thương mại chuẩn (điều khoản, chính sách lập hóa "
               "đơn, bảo hành) được dùng thường xuyên và được tư vấn pháp lý rà "
               "soát không? Các hợp đồng do khách hàng soạn có được rà soát điều "
               "khoản phân bổ trách nhiệm bất lợi (hold harmless, chấm dứt, giới "
               "hạn trách nhiệm, giải quyết tranh chấp) không?",
               "Are standard commercial documents used regularly and reviewed "
               "by legal counsel? Are client-prepared RFPs, contracts and purchase "
               "orders reviewed for wording that unfairly allocates liability "
               "(hold harmless, termination, warranty, limitation of liability, "
               "dispute resolution)?")],
            ["4.6.4", A("Do người dùng tự định nghĩa", "User Defined"),
             A("Các hàng trống cho tiêu chí riêng của khách hàng.",
               "Blank rows for client-specific criteria.")],
        ],
        A("Bốn nhóm tiêu chí của điều 4.6, rút gọn từ trang 29–31.",
          "The four §4.6 criteria groups, condensed from pages 29–31.")))
    b.append(ol([
        A("<b>Quyền sở hữu phần mềm.</b> 4.6.3 D và E hỏi riêng về điều khoản "
          "hợp đồng quản lý rủi ro trách nhiệm khi bàn giao tệp điện tử và các "
          "thay đổi chương trình cho khách hàng, và điều khoản nêu rõ quyền sở "
          "hữu phần mềm ứng dụng. Với dự án tự động hóa, đây thường là điểm "
          "đàm phán khó nhất.",
          "<b>Software ownership.</b> 4.6.3 D and E ask specifically for "
          "contract language managing the liability risk of delivering "
          "electronic files and program changes, and for language stating "
          "ownership of application software. On automation projects this is "
          "often the hardest negotiation point."),
        A("<b>Hợp đồng dễ hiểu, không có chi phí ẩn.</b> 4.6.3 C nêu yêu cầu này "
          "tách biệt — một tiêu chí về sự minh bạch, không chỉ về pháp lý.",
          "<b>Straightforward contracts without hidden costs.</b> 4.6.3 C states "
          "this as a standalone requirement — a transparency criterion, not "
          "merely a legal one."),
        A("<b>Phần việc của Tập 2.</b> 4.6.2 mới chỉ dừng ở nội bộ CSI; việc phát "
          "triển RFP và đánh giá hồ sơ dự thầu từ phía khách hàng thuộc Tập 2 "
          "của bộ hướng dẫn.",
          "<b>Volume 2's job.</b> 4.6.2 stays inside the CSI; developing the RFP "
          "and evaluating proposals from the client's side belongs to Volume 2."),
    ]))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
