# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 7: Technical qualifications, project experience,
types of services and risk considerations, §4.7 (printed pages 33–38)."""
import intfig as F
from int_common import T, fig, h2, h3, lead, note, ol, p, quote, table, ul

PAGES_SRC = 6
BYLINE = "CSIA · Guide Vol. 1 (2000) · §4.7"

TYPICAL_SERVICES = [
    ("A", "Consulting", "Tư vấn"),
    ("B", "Project Management", "Quản lý dự án"),
    ("C", "Specification/Design", "Đặc tả / Thiết kế"),
    ("D", "Software Development/Test", "Phát triển / Thử nghiệm phần mềm"),
    ("E", "Procurement", "Mua sắm, đấu thầu thiết bị"),
    ("F", "Panel Fabrication", "Chế tạo tủ điện"),
    ("G", "Construction/Installation", "Thi công / Lắp đặt"),
    ("H", "Commissioning/Training", "Chạy thử / Đào tạo"),
    ("I", "On-Going Support", "Hỗ trợ liên tục"),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Comfort level</em> — mức độ tin "
        "cậy / thoải mái mang tính vô hình nhưng rất quan trọng với khách hàng. · "
        "<em>Partnering</em> — quan hệ hợp tác chặt giúp dự án hiệu quả dần theo "
        "thời gian. · <em>In-house vs outsourced</em> — tự làm hay thuê ngoài. · "
        "<em>Application experience</em> — kinh nghiệm ứng dụng, tiêu chí ví dụ "
        "có trọng số 9 ở điều 2.2. · <em>Type of services</em> — dải dịch vụ CSI "
        "cung cấp, cũng là cơ sở phân loại ở Phụ lục A.",
        "<b>Key terms.</b> <em>Comfort level</em> — the intangible but important "
        "degree of trust a client feels. · <em>Partnering</em> — a close working "
        "relationship that makes projects more effective as it matures. · "
        "<em>In-house vs outsourced</em> — performed by the CSI itself or "
        "subcontracted. · <em>Application experience</em> — the weighted-9 "
        "example criterion from §2.2. · <em>Type of services</em> — the range of "
        "services a CSI offers, also the basis of the Appendix A taxonomy.",
        lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Điều 4.7 là nhóm tiêu chí cuối cùng, dài nhất trong phần kỹ thuật và "
        "<b>nằm ngoài phạm vi đăng ký CSIA</b> — lối tắt ở điều 3 chỉ cho bỏ qua "
        "các mục 4.1 đến 4.6.5. Bốn nhóm con lần lượt là năng lực kỹ thuật "
        "(4.7.1), kinh nghiệm dự án (4.7.2), loại dịch vụ (4.7.3) và cân nhắc rủi "
        "ro (4.7.4). Chương này cũng nối thẳng trở lại bước 7–8 của công cụ phân "
        "tích quyết định.",
        "§4.7 is the last criteria family, the longest technical one, and "
        "<b>outside the scope of CSIA registration</b> — the §3 shortcut only "
        "permits skipping §§4.1–4.6.5. Its four sub-groups are technical "
        "qualifications (4.7.1), project experience (4.7.2), type of services "
        "(4.7.3) and risk considerations (4.7.4). It also links straight back to "
        "steps 7–8 of the decision analysis tool.")))

    # --------------------------------------------------------------- 4.7.1
    b.append(h2(A("4.7.1 · Năng lực kỹ thuật", "4.7.1 · Technical Qualifications"),
                A("Bốn lĩnh vực kinh nghiệm", "Four areas of experience")))
    b.append(fig(1, F.fig_technical_domains()))
    b.append(p(A(
        "Cấu trúc lặp lại ở bốn nhóm A–D rất đáng chú ý: mỗi nhóm đều mở đầu bằng "
        "«Kinh nghiệm trước đó của CSI về <em>phần cứng / phần mềm / ứng dụng / "
        "ngành</em> có thể được tận dụng để nâng tầm dự án, tăng giá trị và giảm "
        "rủi ro». Cùng một bộ ba câu hỏi được dùng cho cả bốn nhóm: kinh nghiệm "
        "và đào tạo có còn cập nhật không, có năng lực hỗ trợ nội bộ không, và có "
        "đủ nhân sự có kinh nghiệm không.",
        "The structure repeats across all four groups A–D: each opens with "
        "“Previous CSI <em>hardware / software / application / industry</em> "
        "experience can be leveraged to enhance the project, add value and "
        "reduce risk”. The same three follow-up questions are used for each: is "
        "the training and experience current, are there in-house support "
        "capabilities, and are enough experienced resources available?")))
    b.append(table(
        [A("Nhóm", "Group"), A("Câu hỏi cốt lõi", "Core question")],
        [
            ["A", A("Năng lực và kinh nghiệm tổng thể về các nền tảng điều khiển; "
                    "đặc biệt lưu ý an toàn và an ninh (NOTE trong bản gốc).",
                    "Overall capability and experience with control platforms; "
                    "the source adds a NOTE to give special care to safety and "
                    "security issues.")],
            ["B  Hardware", A("Dịch vụ, năng lực, đào tạo và kinh nghiệm với phần "
                              "cứng chuẩn của khách hàng; có thiết bị lập trình "
                              "và giao tiếp chuyên dụng nội bộ không?",
                              "Services, capabilities, training and experience "
                              "with the client's standard hardware; are special "
                              "programmers and interface equipment available "
                              "in-house?")],
            ["C  Software", A("Tương tự cho phần mềm chuẩn của khách hàng, kể cả "
                              "bộ công cụ phát triển và thiết bị chuyên dụng.",
                              "The same for the client's standard software, "
                              "including development packages and special "
                              "programmers.")],
            ["D  Industry", A("Kinh nghiệm trong ngành của khách hàng; có quen "
                              "thuộc với quy định và tiêu chuẩn ngành không; có "
                              "tham gia tích cực các hội / tổ chức chuyên môn "
                              "không?",
                              "Past experience in the client's industry; "
                              "familiarity with industry regulations and "
                              "standards; active membership in relevant "
                              "industrial societies and professional bodies?")],
            ["E–F", A("Hàng trống do người dùng tự định nghĩa.",
                      "Blank user-defined rows.")],
        ],
        A("Bốn nhóm câu hỏi kỹ thuật ở điều 4.7.1, trang 33–35.",
          "The four §4.7.1 technical question groups, pages 33–35.")))

    # --------------------------------------------------------------- 4.7.2
    b.append(h2(A("4.7.2 · Kinh nghiệm dự án", "4.7.2 · Project Experience"),
                A("Bốn góc nhìn, trong đó có một góc vô hình",
                  "Four angles, one of them intangible")))
    b.append(ol([
        A("<b>Comfort level (B).</b> «Một tiêu chí vô hình nhưng rất quan trọng là "
          "mức độ tin cậy bạn cảm nhận về công ty và đội ngũ của họ.» Bản gốc nêu "
          "năm câu tự hỏi: tôi có tin tưởng CSI này không? Tôi có tự tin vào họ "
          "không? Họ có cư xử chuyên nghiệp trong suốt quá trình không? Tính cách "
          "của những người chủ chốt có hợp với nhân sự của tôi không? Họ có giữ "
          "lời hứa không?",
          "<b>Comfort level (B).</b> “An intangible, yet very important, "
          "qualification is the level of comfort you feel about the firm and its "
          "staff.” The source poses five questions: do I trust this CSI? Do I "
          "have confidence in them? Have they acted professionally throughout? "
          "Are the key players' personalities compatible with my staff? Do they "
          "meet their commitments?"),
        A("<b>General experience (C).</b> Lịch sử dự án và năng lực nguồn lực quan "
          "trọng cho cả việc đánh giá lẫn sự thành công của dự án: kinh nghiệm "
          "triển khai, quản lý, điều phối nguồn lực; quy mô dự án điển hình tính "
          "bằng tiền, thời gian và nhân lực; và khả năng cung cấp nhiều tham chiếu "
          "— cùng chất lượng của các tham chiếu đó.",
          "<b>General experience (C).</b> Past project history and resource "
          "capability matter both to the evaluation and to project success: "
          "experience of implementation, project management and resource "
          "coordination; typical project size in dollars, time and resources; "
          "and the ability to provide multiple references — plus how good those "
          "references are."),
        A("<b>Relationships (D).</b> Quan hệ hợp tác (partnering) giúp CSI làm "
          "việc chặt chẽ với khách hàng trong phát triển và cải tiến dự án, trao "
          "đổi thông tin và tận dụng kinh nghiệm; dự án càng về sau càng «hiệu "
          "quả và hiệu năng». Câu hỏi đặt ra cho quan hệ với các khách hàng khác, "
          "với nhà cung cấp và với các thành viên tiềm năng khác của đội dự án.",
          "<b>Relationships (D).</b> Partnering enables the CSI to work closely "
          "with the client on project development and enhancement, "
          "communications and leveraging experience, making projects more "
          "“effective and efficient” as the relationship progresses. The guide "
          "asks about relationships with other clients, with vendors and with "
          "other potential project team members."),
        A("<b>Safety and security (A).</b> Ngay đầu điều 4.7.2, bản gốc in một lưu "
          "ý riêng: «Special care should be given to safety and security issues».",
          "<b>Safety and security (A).</b> At the very start of §4.7.2 the source "
          "prints a standalone note: “Special care should be given to safety and "
          "security issues”."),
    ]))

    # --------------------------------------------------------------- 4.7.3
    b.append(h2(A("4.7.3 · Loại dịch vụ", "4.7.3 · Type of Services"),
                A("Dải dịch vụ và câu hỏi đi kèm",
                  "The service range and the questions that follow")))
    b.append(quote(A(
        "«CSI cung cấp những dải dịch vụ rất khác nhau. Khách hàng nên rà soát các "
        "dịch vụ mình cần và đánh giá CSI tương ứng. Một CSI có thể cung cấp dải "
        "dịch vụ đầy đủ, bao phủ được nhiều nhu cầu hơn của dự án, sẽ hiệu quả "
        "hơn.»",
        "«CSIs provide a varying range of services. A client should review the "
        "services they require and assess the CSI accordingly. A CSI that can "
        "provide a full range of services to encompass more of the project needs "
        "should be more effective.»"),
        A("CSIA Guide, Volume 1, điều 4.7.3, trang 37",
          "CSIA Guide, Volume 1, §4.7.3, page 37")))
    b.append(table(
        [A("Mục", "Ref"), A("Dịch vụ điển hình (bản gốc)", "Typical service (source)"),
         A("Tiếng Việt", "Vietnamese")],
        [[r[0], r[1], r[2]] for r in TYPICAL_SERVICES],
        A("Danh mục A–I trong điều 4.7.3; các mục J–L để trống cho khách hàng.",
          "The A–I list in §4.7.3; items J–L are left blank for the client.")))
    b.append(p(A(
        "Với <b>mỗi dịch vụ bắt buộc</b>, bản gốc yêu cầu đánh giá bảy câu: dải "
        "dịch vụ cụ thể là gì; bao nhiêu năm kinh nghiệm cho từng dịch vụ; có bao "
        "nhiêu nhân sự cho từng dịch vụ; chứng chỉ và giấy phép cần thiết có đủ "
        "không; thực hành và tiêu chuẩn ngành có được tuân thủ không; dịch vụ nào "
        "tự làm, dịch vụ nào thuê ngoài; và các dịch vụ thuê ngoài do liên minh "
        "đã thiết lập hay nhà thầu phụ thực hiện, quan hệ đó được quản lý thế "
        "nào. Một dòng cuối dẫn sang <a href=\"../ch08-integrator-types/\">"
        "Phụ lục A</a>: «Phụ lục A phân loại CSI theo loại dịch vụ và tỷ lệ doanh "
        "thu từ dịch vụ».",
        "For <b>each required service</b> the source asks seven questions: what "
        "is the range of specific services; how many years of experience per "
        "service; how many resources per service; are required certifications "
        "and licences in place; are industry practices and standards followed; "
        "which services are in-house versus outsourced; and are outsourced "
        "services performed by established alliances or subcontractors, and how "
        "is the relationship managed. A final line points to "
        "<a href=\"../ch08-integrator-types/\">Appendix A</a>: it discusses CSIs "
        "by type of service and percent of revenue derived from services.")))

    # --------------------------------------------------------------- 4.7.4
    b.append(h2(A("4.7.4 · Cân nhắc rủi ro", "4.7.4 · Risk Considerations"),
                A("Điểm cao nhất không tự động thắng",
                  "The highest score does not automatically win")))
    b.append(fig(2, F.fig_risk_balance()))
    b.append(p(A(
        "Điều này khép lại vòng lặp với bước 7–8 của điều 2.2. Trong ví dụ gốc, "
        "CSI B có tổng điểm cao hơn (57 so với 55) nhưng tiềm ẩn rủi ro tỷ lệ "
        "nghỉ việc hơi cao — cần <b>đạt cam kết về nhân sự chủ chốt của dự "
        "án</b>. CSI A thấp điểm hơn nhưng kinh nghiệm ứng dụng chỉ ở mức vừa đủ "
        "— cần <b>rà soát đặc tả kỹ thuật cẩn thận</b>. Quyết định cuối cùng "
        "thuộc về CSI có sự cân bằng tốt nhất giữa tổng điểm và rủi ro chấp nhận "
        "được, có thể quản lý được.",
        "This closes the loop with steps 7–8 of §2.2. In the guide's example CSI "
        "B has the higher total (57 versus 55) but carries a borderline-high "
        "turnover risk — calling for <b>commitment of key project resources</b>. "
        "CSI A scores lower but has marginal application experience — calling "
        "for <b>a careful review of the specification</b>. The final choice goes "
        "to the CSI with the best balance of total score and acceptable, "
        "manageable risk.")))
    b.append(ul([
        A("<b>Điểm thấp là tín hiệu, không phải án tử.</b> Điều 2.2 gợi ý «low "
          "performance score could indicate risk» — cần điều tra, không cần loại "
          "ngay.",
          "<b>A low score is a signal, not a verdict.</b> §2.2 suggests “low "
          "performance score could indicate risk” — investigate rather than "
          "eliminate outright."),
        A("<b>Rủi ro phải được ghi tên và giao người quản lý.</b> Một rủi ro không "
          "có biện pháp quản lý không phải «rủi ro chấp nhận được» theo nghĩa của "
          "tiêu chuẩn.",
          "<b>Risks must be named and owned.</b> A risk with no mitigation is not "
          "an “acceptable risk” in the standard's sense."),
        A("<b>Kết nối với điều 4.3.1 G.</b> Quy trình quản lý rủi ro có sự tham "
          "gia của khách hàng là nơi các biện pháp này được lập hồ sơ.",
          "<b>Link to §4.3.1 G.</b> The client-involving risk-management "
          "procedure is where these mitigations get documented."),
    ]))
    b.append(note(A(
        "<b>Kết thúc phần tiêu chí.</b> Điều 4.7.4 là mục cuối cùng của điều 4. "
        "Trang 39 mở Phụ lục A với hệ thống phân loại nhà tích hợp / nhà cung cấp "
        "và mười biểu đồ cơ cấu dịch vụ — nội dung của chương 8.",
        "<b>End of the criteria.</b> §4.7.4 is the last item in §4. Page 39 opens "
        "Appendix A with the integrator/provider taxonomy and its ten "
        "service-mix charts — the subject of Chapter 8.")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
