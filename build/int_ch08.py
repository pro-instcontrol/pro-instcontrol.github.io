# -*- coding: utf-8 -*-
"""CSIA Guide Vol. 1 — Chapter 8: Appendix A, types of control systems
integrators and control system providers (printed pages 39–49).

Carries all ten "Typical Project Mix of Services" donut charts, redrawn as
true vectors by `intfig.pie()`.
"""
import intfig as F
from int_common import T, fig, h2, h3, lead, note, ol, p, quote, table, ul

PAGES_SRC = 11
BYLINE = "CSIA · Guide Vol. 1 (2000) · Appendix A"

CSI_INTRO = (
    "Trọng tâm là dịch vụ kỹ thuật giá trị gia tăng trong các giải pháp tích hợp "
    "phức tạp. <b>Tỷ lệ doanh thu từ dịch vụ tích hợp so với phần cứng lớn hơn "
    "61%</b>, không tính doanh thu xây lắp. Tổ chức này cung cấp dải dịch vụ "
    "đầy đủ cho giải pháp điều khiển và/hoặc thông tin tích hợp: tư vấn, thiết "
    "kế, thi công, quản lý dự án, phát triển, chạy thử, đặc tả, lắp ráp tủ điện "
    "và dây nối, đào tạo, thử nghiệm, hỗ trợ liên tục.",
    "The focus is value-added engineering services in complex integrated "
    "solutions. <b>Revenue from integration services versus hardware is greater "
    "than 61%</b>, not inclusive of construction revenue. These organisations "
    "deliver a full range of services for integrated control and/or information "
    "solutions: consulting, design, construction, project management, "
    "development, commissioning, specifications, panel wire & assembly, "
    "training, testing and ongoing support.",
)

CSI_TYPES = [
    ("Design/Build Integrator/Services", "Thiết kế / thi công trọn gói", 1,
     ("Thiết kế–thi công trọn gói thiết bị và hệ thống tự động hóa; ngành kỹ thuật "
      "gồm công nghệ, cơ khí, điện, điều khiển; quản lý dự án đa ngành từ ý "
      "tưởng đến chạy thử, kể cả thi công.",
      "Turn-key design/build of automation equipment and systems; process, "
      "mechanical, electrical and control disciplines; multi-discipline project "
      "management from concept to commissioning, including construction.")),
    ("Control Systems Integrator/Services", "Hệ thống điều khiển / dịch vụ", 2,
     ("Tập trung vào hệ thống điều khiển và thông tin tích hợp phức tạp tại phân "
      "xưởng; ngành kỹ thuật gồm công nghệ (kiến thức), điện, điều khiển và thông "
      "tin. Quản lý dự án đa ngành, cung cấp hỗ trợ lắp đặt và/hoặc quản lý thi "
      "công điện.",
      "Focuses on complex shop-floor integrated control and information systems; "
      "process knowledge, electrical, control and information disciplines. "
      "Multi-discipline project management, installation support and/or "
      "management of electrical construction.")),
    ("Manufacturing Execution Systems Integrator/Services",
     "Hệ thống điều hành sản xuất (MES)", 3,
     ("Tập trung vào hệ thống điều hành sản xuất tích hợp phức tạp tại phân "
      "xưởng; ngành kỹ thuật chủ yếu là công nghệ thông tin, có thêm hiểu biết "
      "về SCADA. Quản lý dự án từ ý tưởng đến chạy thử; hỗ trợ liên tục và quản "
      "trị hệ thống là phần mở rộng điển hình.",
      "Focuses on complex shop-floor integrated manufacturing execution systems; "
      "the discipline is mainly information technology with some SCADA "
      "knowledge. Project management from concept to commissioning; ongoing "
      "support and system administration are typical extensions.")),
    ("Information Technology (IT) Systems Integration/Services",
     "Tích hợp hệ thống CNTT", 4,
     ("Dịch vụ trọn vẹn cho các hệ thống CNTT tích hợp truyền thống; ngành kỹ "
      "thuật chủ yếu là công nghệ thông tin, có thêm hiểu biết về MES. Hỗ trợ "
      "liên tục, quản trị hệ thống và thuê ngoài (outsourcing) là phần mở rộng "
      "điển hình.",
      "Complete services for traditional integrated IT systems; mainly "
      "information technology with some MES knowledge. Ongoing support, system "
      "administration and outsourcing are typical extensions.")),
]

CSP_TYPES = [
    ("Control Systems Provider (CSP)", "Nhà cung cấp hệ thống điều khiển", 5,
     ("Dùng kỹ thuật ứng dụng giá trị gia tăng để <em>hỗ trợ bán sản phẩm</em> "
      "thành một giải pháp hoàn chỉnh hơn. Tỷ lệ doanh thu từ dịch vụ tích hợp so "
      "với phần cứng <b>thường nhỏ hơn 61%</b>, không tính doanh thu xây lắp. "
      "Trọng tâm là bán thiết bị, phần cứng và/hoặc phần mềm, kèm dải dịch vụ "
      "kỹ thuật ứng dụng đầy đủ.",
      "Uses value-added application engineering to <em>facilitate the sale of "
      "products</em> into a more complete solution. Revenue from integration "
      "services versus hardware is <b>usually less than 61%</b>, not inclusive "
      "of construction revenue. The focus is selling equipment, hardware "
      "and/or software products alongside a full range of application "
      "engineering services.")),
    ("Equipment Solutions Provider", "Nhà cung cấp giải pháp thiết bị", 6,
     ("Bán các thiết bị được tùy biến riêng, kèm dịch vụ kỹ thuật để tùy biến; "
      "ngành kỹ thuật gồm công nghệ, cơ khí, điện và điều khiển; quản lý dự án "
      "đa ngành từ ý tưởng đến chạy thử.",
      "Sells customised pieces of equipment with the engineering to customise "
      "them; process, mechanical, electrical and control disciplines; "
      "multi-discipline project management from concept to commissioning.")),
    ("Control Solutions Provider", "Nhà cung cấp giải pháp điều khiển", 7,
     ("Bán phần cứng hoặc phần mềm điều khiển được tùy biến, kèm dịch vụ kỹ "
      "thuật giá trị gia tăng; ngành kỹ thuật gồm cơ điện, điện và điều khiển. "
      "Hỗ trợ bảo hành là phần mở rộng điển hình.",
      "Sells customised control hardware or software products with value-added "
      "engineering; electro-mechanical, electrical and control disciplines. "
      "Warranty support is a typical extension.")),
    ("Control Panel Shop Provider", "Xưởng tủ điện điều khiển", 8,
     ("Tỷ trọng mua phần cứng / phần mềm lớn nhất trong toàn bộ Phụ lục A "
      "(55%), cộng 15% tủ điện / trạm — phản ánh đúng mô hình kinh doanh thiên "
      "về chế tạo và cung ứng vật lý.",
      "The largest hardware/software purchase share in all of Appendix A (55%), "
      "plus 15% panels/stations — accurately reflecting a business weighted "
      "toward physical fabrication and supply.")),
    ("Construction / Control Systems Provider",
     "Nhà cung cấp thi công / hệ thống điều khiển", 9,
     ("Thi công chiếm 30% cơ cấu, quản lý dự án 12% — kiểu nhà cung cấp có dấu "
      "ấn xây lắp rõ nhất trong nhóm CSP, nhưng vẫn dưới ngưỡng 61% doanh thu "
      "dịch vụ tích hợp.",
      "Construction accounts for 30% of the mix and project management 12% — "
      "the most construction-heavy CSP type, yet still below the 61% "
      "integration-services threshold.")),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>CSI</em> — Control Systems "
        "Integrator; doanh thu dịch vụ tích hợp <b>&gt; 61%</b>. · <em>CSP</em> "
        "— Control System(s) Provider; doanh thu dịch vụ tích hợp <b>&lt; 61%</b>, "
        "trọng tâm là bán sản phẩm. · <em>Ngưỡng 61%</em> — không tính doanh thu "
        "xây lắp. · <em>MES / SCADA</em> — hệ thống điều hành sản xuất / thu thập "
        "dữ liệu và giám sát. · <em>Project mix of services</em> — cơ cấu tỷ "
        "trọng doanh thu theo từng nhóm dịch vụ trong một dự án điển hình.",
        "<b>Key terms.</b> <em>CSI</em> — Control Systems Integrator; integration "
        "services <b>&gt; 61%</b> of revenue. · <em>CSP</em> — Control System(s) "
        "Provider; integration services <b>&lt; 61%</b>, focused on selling "
        "products. · <em>The 61% threshold</em> — construction revenue excluded. "
        "· <em>MES / SCADA</em> — manufacturing execution systems / supervisory "
        "control and data acquisition. · <em>Project mix of services</em> — the "
        "revenue share of each service group in a typical project.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Phụ lục A ra đời để gỡ một sự nhầm lẫn đã được nêu ngay từ điều 1.2: "
        "«phần lớn CSI tiến hóa từ một dịch vụ đơn lẻ đến dải dịch vụ đầy đủ và "
        "mang nhiều diện mạo khác nhau, gây nhầm lẫn cho thị trường». Phụ lục "
        "này xếp mọi tổ chức thành <em>kiểu</em> theo <b>tỷ lệ doanh thu từ dịch "
        "vụ tích hợp so với phần cứng</b>, với ngưỡng 61%, và minh họa mỗi kiểu "
        "bằng một biểu đồ cơ cấu dịch vụ điển hình. Cả mười biểu đồ đều được vẽ "
        "lại dưới dạng vector trong chương này.",
        "Appendix A exists to clear up a confusion flagged as early as §1.2: "
        "“most CSIs evolve out of singular services to a full range of services "
        "and take on many different looks along the way, confusing the "
        "marketplace”. It positions every organisation into a <em>type</em> by "
        "the <b>share of revenue from integration services versus hardware</b>, "
        "using a 61% threshold, and illustrates each with a typical project "
        "service-mix chart. All ten charts are redrawn as vectors in this "
        "chapter.")))
    b.append(fig(1, F.fig_taxonomy()))
    b.append(note(A(
        "<b>Không có kiểu nào tốt hơn kiểu nào.</b> Nguyên văn ở mục 2 và lặp lại "
        "ở mục 4: «Không có kiểu nào tốt hay xấu hơn kiểu nào! Khách hàng tự "
        "quyết định kiểu — hay tổ hợp các kiểu — nào phù hợp nhất với nhu cầu của "
        "mình». Hầu hết các CSI / CSP là <em>tổ hợp</em> của nhiều kiểu, không "
        "thuần một kiểu.",
        "<b>No type is better than another.</b> Verbatim in sections 2 and 4: "
        "“No type is better or worse than another! It is up to the client to "
        "decide which type or combination of types best fits their needs”. Most "
        "CSIs / CSPs are a <em>combination</em> of several types rather than a "
        "pure one.")))

    # ------------------------------------------------------------- 1. CSI
    b.append(h2(A("1 · Control Systems Integrator (CSI)",
                  "1 · Control Systems Integrator (CSI)"),
                A("Ngưỡng trên 61%", "Above the 61% threshold")))
    b.append(p(A(CSI_INTRO[0], CSI_INTRO[1])))
    b.append(fig(2, F.pie(0)))
    b.append(table(
        [A("Nhóm", "Group"), A("Ngưỡng doanh thu dịch vụ", "Services revenue"),
         A("Trọng tâm", "Focus")],
        [
            ["CSI", "&gt; 61%",
             A("Dịch vụ kỹ thuật giá trị gia tăng, giải pháp tích hợp phức tạp",
               "Value-added engineering services, complex integrated solutions")],
            ["CSP", "&lt; 61%",
             A("Bán thiết bị / phần cứng / phần mềm, kèm kỹ thuật ứng dụng",
               "Selling equipment, hardware and/or software with application "
               "engineering")],
        ],
        A("Hai nhánh chính của Phụ lục A; doanh thu xây lắp bị loại khỏi phép tính.",
          "The two main branches of Appendix A; construction revenue is excluded "
          "from the calculation.")))

    # ------------------------------------------------------- 2. CSI types
    b.append(h2(A("2 · Các kiểu CSI", "2 · Types of Control Systems Integrators"),
                A("Bốn kiểu, bốn biểu đồ", "Four types, four charts")))
    b.append(p(A(
        "«Các thị trường (phân khúc) khác nhau đặt ra những đòi hỏi khác nhau về "
        "trọng tâm, ngành kỹ thuật và cơ cấu dịch vụ. Dưới đây là một số kiểu "
        "CSI, không theo thứ tự ưu tiên nào.»",
        "“Different markets (segments) place different demands on focus, "
        "engineering disciplines and mix of services. Below are several types of "
        "CSI's in no particular order.”")))
    n = 2
    for en, vi, pie_idx, (s_vi, s_en) in CSI_TYPES:
        n += 1
        b.append(h3(A("· %s" % vi, "· %s" % en)))
        b.append(p(A(s_vi, s_en)))
        b.append(fig(n, F.pie(pie_idx)))

    # ------------------------------------------------------------- 3. CSP
    b.append(h2(A("3 · Control Systems Provider (CSP)",
                  "3 · Control System Provider (CSP)"),
                A("Dưới ngưỡng 61%", "Below the 61% threshold")))
    n += 1
    en, vi, pie_idx, (s_vi, s_en) = CSP_TYPES[0]
    b.append(p(A(s_vi, s_en)))
    b.append(fig(n, F.pie(pie_idx)))
    b.append(ul([
        A("Dải dịch vụ được liệt kê ở mục 3: tư vấn, thiết kế, hỗ trợ lắp đặt, "
          "quản lý dự án, phát triển, hỗ trợ khởi động, đặc tả, lắp ráp tủ điện "
          "và dây nối, đào tạo, thi công, thử nghiệm, hỗ trợ bảo hành.",
          "Services listed in section 3: consulting, design, installation "
          "support, project management, development, start-up assistance, "
          "specifications, panel wire & assembly, training, construction, "
          "testing and warranty support."),
        A("So với CSI, cơ cấu của CSP dịch hẳn sang <em>Purchase Equipment / "
          "Hardware / Software</em> (30%) và <em>Installation</em> (20%).",
          "Compared with a CSI, the CSP mix shifts markedly toward "
          "<em>Purchase Equipment / Hardware / Software</em> (30%) and "
          "<em>Installation</em> (20%)."),
    ]))

    # ------------------------------------------------------- 4. CSP types
    b.append(h2(A("4 · Các kiểu CSP", "4 · Types of CSPs"),
                A("Bốn kiểu, bốn biểu đồ", "Four types, four charts")))
    for en, vi, pie_idx, (s_vi, s_en) in CSP_TYPES[1:]:
        n += 1
        b.append(h3(A("· %s" % vi, "· %s" % en)))
        b.append(p(A(s_vi, s_en)))
        b.append(fig(n, F.pie(pie_idx)))

    # ------------------------------------------------------------- 5 and 6
    b.append(h2(A("5–6 · Các nhóm còn lại", "5–6 · The remaining groups"),
                A("Ngoài hai nhánh chính", "Beyond the two main branches")))
    b.append(table(
        [A("Mục", "Section"), A("Tên", "Name"),
         A("Ghi chú của bản gốc", "Source note")],
        [
            ["5", A("Other Control System Integrators",
                    "Các nhà tích hợp hệ thống điều khiển khác"),
             A("Được liệt kê như một nhóm riêng, không có biểu đồ cơ cấu dịch vụ "
               "riêng trong Phụ lục A.",
               "Listed as a separate group without its own service-mix chart in "
               "Appendix A.")],
            ["6", A("Other System Integrators",
                    "Các nhà tích hợp hệ thống khác"),
             A("Bao gồm «Other Commercial» — các nhà tích hợp thương mại khác.",
               "Includes “Other Commercial” — other commercial integrators.")],
        ],
        A("Hai mục cuối của Phụ lục A (trang 49).",
          "The final two Appendix A entries (page 49).")))
    b.append(p(A(
        "<b>Đọc biểu đồ đúng cách.</b> Các nhãn dạng <code>&lt;5%</code>, "
        "<code>&lt;10%</code> hay <code>&lt;1%</code> là <em>giới hạn trên</em>, "
        "không phải giá trị chính xác. Để vẽ lại thành hình tròn, mỗi giá trị "
        "«nhỏ hơn» được lấy bằng chính ngưỡng đó và toàn bộ dãy được chuẩn hóa "
        "về 100%; vì thế góc của các múi mang tính minh họa, còn con số in trong "
        "chú giải được giữ nguyên đúng như bản gốc. Chú thích này cũng được ghi "
        "ngay dưới mỗi hình.",
        "<b>Reading the charts correctly.</b> Labels such as <code>&lt;5%</code>, "
        "<code>&lt;10%</code> and <code>&lt;1%</code> are <em>upper bounds</em>, "
        "not exact values. To redraw them as a donut, each “less than” value is "
        "taken at its bound and the series is normalised to 100%; the slice "
        "angles are therefore illustrative while the printed legend figures "
        "remain verbatim from the source. This note is repeated beneath every "
        "figure.")))
    b.append(note(A(
        "<b>Liên ngược với điều 4.7.3.</b> Chính mục «Type of Services» ở trang "
        "37 dẫn người đọc sang Phụ lục A này: «Phụ lục A thảo luận về CSI theo "
        "loại dịch vụ và tỷ lệ doanh thu từ dịch vụ». Hai chương vì thế nên được "
        "đọc cặp — chương 7 hỏi CSI <em>có</em> những dịch vụ gì, chương 8 cho "
        "thấy các dịch vụ đó <em>chiếm tỷ trọng bao nhiêu</em> ở từng mô hình "
        "kinh doanh.",
        "<b>Linking back to §4.7.3.</b> The “Type of Services” clause on page 37 "
        "points directly here: “Appendix A discusses CSIs by types of services "
        "and percent of revenue derived from services”. The two chapters should "
        "be read as a pair — Chapter 7 asks <em>which</em> services a CSI offers, "
        "Chapter 8 shows <em>how heavily each weighs</em> in each business "
        "model.")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
