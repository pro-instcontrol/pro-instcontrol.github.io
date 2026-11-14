# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 1: General, CSIA and the definition of a CSI.

Covers the guide's introduction, purpose and disclaimer (pp. i–vii), the ten
CSIA beliefs, the Best Practices & Benchmarks mission and objectives, and
§§1.1–1.2 (printed pages 1–2).
"""
import intfig as F
from int_common import T, fig, h2, h3, lead, note, ol, p, quote, refs, table, ul

PAGES_SRC = 11
BYLINE = "CSIA · Guide Vol. 1 (2000) · Introduction and §1"


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>CSIA</em> — Hiệp hội các nhà tích "
        "hợp hệ thống điều khiển (Control System Integrators Association). · "
        "<em>CSI</em> — nhà tích hợp hệ thống điều khiển, tổ chức kỹ thuật giá trị "
        "gia tăng độc lập. · <em>Best Practices & Benchmarks</em> — chương trình "
        "thực hành tốt và chuẩn đối sánh. · <em>Registration</em> — đăng ký / công "
        "nhận CSIA sau kiểm toán độc lập. · <em>Client</em> — khách hàng, bên thuê "
        "tích hợp; trong bản dịch này giữ phân biệt với <em>customer</em> (người "
        "sử dụng cuối).",
        "<b>Key terms.</b> <em>CSIA</em> — Control System Integrators Association. · "
        "<em>CSI</em> — Control Systems Integrator, an independent value-added "
        "engineering organisation. · <em>Best Practices & Benchmarks</em> — the "
        "CSIA self-evaluation and industry-benchmark programme. · "
        "<em>Registration</em> — CSIA recognition after an independent audit. · "
        "<em>Client</em> — the party procuring integration services, distinguished "
        "here from the end customer.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Tập 1 của bộ hướng dẫn CSIA không phải sách kỹ thuật điều khiển, mà là "
        "<em>sổ tay ra quyết định</em> dành cho bên mua dịch vụ tích hợp. Nó trả lời "
        "ba câu hỏi: một CSI là gì, làm sao đánh giá và chọn một CSI, và nên dùng "
        "những tiêu chí nào. Chương mở đầu này đặt nền tảng: mục đích của bộ tài "
        "liệu, tín điều và sứ mệnh của hiệp hội, cùng định nghĩa chính thức về CSI.",
        "Volume 1 of the CSIA guide is not a control-engineering textbook but a "
        "<em>decision handbook for the buyer</em>. It answers three questions: what "
        "a CSI is, how to evaluate and select one, and which criteria to use. This "
        "opening chapter lays the groundwork: the purpose of the documents, the "
        "association's beliefs and mission, and the formal definition of a CSI.")))

    # ------------------------------------------------------------- purpose
    b.append(h2(A("Mục đích của bộ tài liệu", "Purpose of the documents"),
                A("Ba mục tiêu, hai tập", "Three purposes, two volumes")))
    b.append(p(A(
        "Lời giới thiệu nêu ba mục đích lớn. Đáng chú ý là chỉ mục đích thứ nhất "
        "thuộc Tập 1; hai mục đích còn lại được giao cho Tập 2. Vì vậy khi đọc Tập "
        "1, cần nhớ rằng đây là <b>phần lựa chọn và đánh giá</b>, không phải phần "
        "viết đề xuất yêu cầu chào giá (RFP) hay quản trị triển khai dự án.",
        "The introduction states three major purposes. Only the first belongs to "
        "Volume 1; the other two are assigned to Volume 2. Reading Volume 1, it is "
        "worth remembering that this is the <b>evaluation and selection</b> part, "
        "not the request-for-proposal (RFP) development or project-implementation "
        "management part.")))
    b.append(table(
        [A("Tập", "Volume"), A("Mục đích", "Purpose")],
        [
            [A("Tập 1", "Volume 1"),
             A("Cung cấp cho khách hàng phương pháp xác định tiêu chí để đánh giá "
               "và lựa chọn một nhà tích hợp hệ thống điều khiển.",
               "Provide the client with a method of identifying criteria to evaluate "
               "and select a Control Systems Integrator.")],
            [A("Tập 2", "Volume 2"),
             A("Cung cấp phương pháp và hướng dẫn hiệu quả để xây dựng yêu cầu chào "
               "giá (RFP) và đánh giá các hồ sơ dự thầu.",
               "Provide the client with an effective method and guideline for "
               "developing a Request for Proposal and evaluating the proposals.")],
            [A("Tập 2", "Volume 2"),
             A("Đề xuất phương pháp quản lý triển khai dự án hiệu quả hơn.",
               "Provide a suggested method to more effectively manage project "
               "implementation.")],
        ],
        A("Theo phần INTRODUCTION, trang i của bản gốc.",
          "From the INTRODUCTION, page i of the source.")))
    b.append(note(A(
        "<b>Tài liệu được xây dựng bởi cả ba phía.</b> Chuyên gia từ các công ty, nhà "
        "sản xuất thiết bị và chính các CSI đã cùng xây dựng Chương trình Đăng ký & "
        "Tiêu chí và bộ Hướng dẫn này (gọi chung là «Documents»). Vì vậy các tiêu "
        "chí ở điều 4 phản ánh yêu cầu của <em>nhiều bên</em> tham gia triển khai "
        "hệ thống điều khiển, chứ không chỉ góc nhìn của nhà cung cấp.",
        "<b>The documents were written by all three sides.</b> Industry "
        "professionals from user companies, product manufacturers and control "
        "systems integrators jointly developed the Registration Program & Criteria "
        "and this Guide (collectively, the “Documents”). The §4 criteria therefore "
        "reflect the requirements of <em>several parties</em> involved in "
        "implementing control systems, not only the supplier's point of view.")))

    # ------------------------------------------------------------ disclaimer
    b.append(h2(A("Giới hạn trách nhiệm", "Limits of responsibility"),
                A("Nguyên văn lời cảnh báo", "The warning, verbatim")))
    b.append(quote(A(
        "«NGƯỜI SỬ DỤNG TÀI LIỆU HOÀN TOÀN CHỊU TRÁCH NHIỆM VỀ TIÊU CHÍ RIÊNG "
        "CỦA MÌNH TRONG VIỆC ĐÁNH GIÁ, LỰA CHỌN, XÂY DỰNG VÀ SOẠN THẢO YÊU CẦU "
        "CHÀO GIÁ, MUA DỊCH VỤ CSI, QUẢN LÝ VÀ TRIỂN KHAI DỰ ÁN. CSIA VÀ CÁC BÊN "
        "THAM GIA KHÔNG ĐƯA RA BẤT KỲ CAM KẾT HAY BẢO HÀNH NÀO, DÙ RÕ RÀNG HAY "
        "NGẦM ĐỊNH.»",
        "«THE USERS OF THE DOCUMENTS ARE SOLELY RESPONSIBLE FOR THEIR OWN CRITERIA "
        "FOR THE EVALUATION, SELECTION, DEVELOPMENT AND DRAFTING OF THE REQUEST "
        "FOR PROPOSAL, PROCUREMENT OF CONTROL SYSTEMS INTEGRATOR SERVICES, "
        "MANAGEMENT AND IMPLEMENTATION OF PROJECTS. THE CSIA AND ITS PARTICIPANTS "
        "DO NOT MAKE OR OFFER REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED, "
        "OF ANY KIND.»"),
        A("CSIA Guide, Volume 1, trang i (viết hoa trong bản gốc)",
          "CSIA Guide, Volume 1, page i (capitalised in the original)")))
    b.append(p(A(
        "Hai câu ngay trước đoạn cảnh báo quan trọng không kém: bộ tài liệu "
        "<b>không bao quát mọi trường hợp</b> và không thể được trông cậy một mình "
        "để xét đến mọi yêu cầu đặc thù của một dự án hay một công ty. Đây là công "
        "cụ, không phải danh mục kiểm tra bắt buộc — chủ đề sẽ quay lại ở điều "
        "2.3 và điều 4.4.10.",
        "The two sentences immediately before that warning matter just as much: "
        "the documents are <b>NOT ALL ENCOMPASSING</b> and cannot reasonably or "
        "solely be relied upon to cover every unique requirement of a project or "
        "company. They are a tool, not a mandatory checklist — a theme that recurs "
        "in §2.3 and §4.4.10.")))

    # --------------------------------------------------------------- beliefs
    b.append(h2(A("Tín điều, sứ mệnh và mục tiêu", "Beliefs, mission and objectives"),
                A("Phần mở đầu của chương trình chuẩn đối sánh",
                  "The benchmarking programme's front matter")))
    b.append(p(A(
        "Trước khi vào các tiêu chí, bản gốc dành bốn trang (iv–vii) cho nền tảng "
        "văn hóa chất lượng của hiệp hội: mười tín điều, một tuyên bố sứ mệnh, năm "
        "mục tiêu và danh sách những người đóng góp. Đây không phải trang trí. Các "
        "tín điều giải thích <em>tại sao</em> điều 4 lại hỏi về phòng ngừa hơn là "
        "sửa lỗi, về đào tạo an toàn, về cải tiến có đo lường và về tuân thủ quy "
        "định.",
        "Before any criteria appear, the source devotes four pages (iv–vii) to the "
        "association's quality culture: ten beliefs, a mission statement, five "
        "objectives and an acknowledgements list. These are not decoration. The "
        "beliefs explain <em>why</em> §4 asks about prevention rather than "
        "correction, safety training, measurable improvement and regulatory "
        "compliance.")))
    b.append(fig(1, F.fig_mission()))
    b.append(fig(2, F.fig_objectives()))
    b.append(fig(3, F.fig_beliefs()))
    b.append(ul([
        A("<b>Khách hàng cuối là trọng tâm</b> và là người thụ hưởng cuối cùng của "
          "mọi nỗ lực.",
          "<b>The end customer must be the focus</b> and ultimate beneficiary of "
          "our efforts."),
        A("<b>Phòng ngừa hiệu quả hơn sửa lỗi</b> — nỗ lực chất lượng sinh lợi hơn "
          "khi hướng vào ngăn ngừa.",
          "<b>Prevention is more productive than correction</b> — quality efforts "
          "pay off more when directed at prevention."),
        A("<b>Con người là nguồn lực lớn nhất</b>: tri thức, kỹ năng, sáng tạo và "
          "năng suất.",
          "<b>People are the greatest resource</b>: knowledge, skill, creativity "
          "and productivity."),
        A("<b>Mọi tai nạn đều có thể phòng tránh</b>; mọi nhân viên có quyền được "
          "làm việc trong môi trường an toàn — gốc của tiêu chí 4.3.6.",
          "<b>All accidents are preventable</b>; every employee has the right to a "
          "safe working environment — the root of criterion 4.3.6."),
        A("<b>Chuẩn đối sánh nâng tầm ngành</b> — dùng benchmark sẽ nâng chuẩn mực "
          "xuất sắc của cả ngành và thị trường phục vụ.",
          "<b>Benchmarks raise the industry's standard</b> — their use lifts the "
          "standard of excellence across the industry and its markets."),
    ]))

    # ------------------------------------------------------------- section 1
    b.append(h2(A("1.1 · CSIA là gì?", "1.1 · What is CSIA?"),
                A("Ba vai trò", "Three roles")))
    b.append(ol([
        A("<b>Diễn đàn của ngành.</b> CSIA là tổ chức hàng đầu dành riêng cho ngành "
          "tích hợp hệ thống điều khiển, cung cấp cho hội viên một diễn đàn trao đổi "
          "về các vấn đề kinh doanh, tiếp thị và kỹ thuật.",
          "<b>Industry forum.</b> CSIA is the premier organisation dedicated to the "
          "control systems integration industry, giving members a unique forum for "
          "education and discussion of the business, marketing and technical "
          "issues they face."),
        A("<b>Quảng bá năng lực.</b> CSIA hỗ trợ hội viên bằng cách giới thiệu năng "
          "lực, thành tích và tính chuyên nghiệp của các CSI với người dùng, nhà "
          "cung cấp, truyền thông và các nhóm ngành nghề liên quan.",
          "<b>Promoting capability.</b> CSIA supports its members by promoting the "
          "capabilities, accomplishments and professionalism of CSIs to users, "
          "vendors, media and related trade, technical and industry groups."),
        A("<b>Chuẩn đối sánh và đăng ký.</b> CSIA cung cấp «Best Practices & "
          "Benchmarks» để các CSI tự đánh giá và cải tiến liên tục, đồng thời chính "
          "thức <em>đăng ký</em> những CSI đã được kiểm toán và đáp ứng các tiêu chí "
          "then chốt (xem <a href=\"../ch04-registration-and-general-management/\">"
          "chương 4</a>).",
          "<b>Benchmarks and registration.</b> CSIA provides Best Practices & "
          "Benchmarks so CSIs can evaluate and continuously improve themselves, and "
          "officially <em>registers</em> CSIs that have been audited and meet key "
          "criteria (see <a href=\"../ch04-registration-and-general-management/\">"
          "Chapter 4</a>)."),
    ]))

    # ------------------------------------------------------------- section 1.2
    b.append(h2(A("1.2 · Định nghĩa CSI", "1.2 · Definition of a CSI"),
                A("Định nghĩa chính thức", "The formal definition")))
    b.append(quote(A(
        "«Nhà tích hợp hệ thống điều khiển (CSI) là một tổ chức kỹ thuật giá trị gia "
        "tăng độc lập — hoặc một bộ phận độc lập về lợi nhuận / lỗ — tập trung vào "
        "hệ thống điều khiển công nghiệp, hệ thống điều hành sản xuất và tự động hóa "
        "nhà máy, đòi hỏi tri thức ứng dụng và chuyên môn kỹ thuật trong bán hàng, "
        "thiết kế, triển khai, lắp đặt, chạy thử và hỗ trợ.»",
        "«A Control Systems Integrator (CSI) is an independent (or an independent "
        "profit/loss division) value-added engineering organization that focuses on "
        "industrial control systems, manufacturing execution systems and plant "
        "automation that requires application knowledge and technical expertise "
        "for sales, design, implementation, installation, commissioning and "
        "support.»"),
        A("CSIA Guide, Volume 1, điều 1.2, trang 1",
          "CSIA Guide, Volume 1, §1.2, page 1")))
    b.append(fig(4, F.fig_csi_services()))
    b.append(p(A(
        "Bản gốc nhấn mạnh rằng <b>phần lớn CSI tiến hóa từ một dịch vụ đơn lẻ đến "
        "một dải dịch vụ đầy đủ</b>, và trong quá trình đó mang nhiều «diện mạo» "
        "khác nhau — chính điều này gây nhầm lẫn cho thị trường. Phụ lục A ra đời "
        "để gỡ nhầm lẫn đó: nó xếp các CSI và nhà cung cấp thành «kiểu» theo tỷ lệ "
        "doanh thu từ dịch vụ tích hợp so với phần cứng, với ngưỡng <b>61%</b>. "
        "Xem <a href=\"../ch08-integrator-types/\">chương 8</a>.",
        "The source stresses that <b>most CSIs evolve from a single service into a "
        "full range of services</b>, taking on many different appearances along the "
        "way — and it is precisely this that confuses the marketplace. Appendix A "
        "exists to remove that confusion: it groups CSIs and providers into "
        "“types” by the share of revenue derived from integration services versus "
        "hardware, using a <b>61%</b> threshold. See "
        "<a href=\"../ch08-integrator-types/\">Chapter 8</a>.")))
    b.append(refs([
        A("Điều 2 — Công cụ phân tích quyết định: <a href=\"../ch02-decision-analysis-tool/\">chương 2</a>.",
          "§2 — Decision analysis tool: <a href=\"../ch02-decision-analysis-tool/\">Chapter 2</a>."),
        A("Điều 4 — Bảy nhóm tiêu chí gợi ý: <a href=\"../ch04-registration-and-general-management/\">chương 4</a> đến chương 7.",
          "§4 — Seven suggested-criteria families: <a href=\"../ch04-registration-and-general-management/\">Chapter 4</a> through Chapter 7."),
        A("Phụ lục A — Phân loại nhà tích hợp / nhà cung cấp: <a href=\"../ch08-integrator-types/\">chương 8</a>.",
          "Appendix A — Integrator/provider taxonomy: <a href=\"../ch08-integrator-types/\">Chapter 8</a>."),
        A("Phụ lục B — Phiếu phân tích quyết định trống: <a href=\"../ch09-decision-worksheet/\">chương 9</a>.",
          "Appendix B — Blank decision-analysis worksheet: <a href=\"../ch09-decision-worksheet/\">Chapter 9</a>."),
    ]))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
