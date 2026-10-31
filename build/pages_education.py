# -*- coding: utf-8 -*-
"""Education — BCIT (Canada) and HUST SEEE EE-E8 (Vietnam) programs.

Bilingual study map of two control/automation programs, with the HUST
curriculum published course-by-course and related library books linked.

Sources:
  BCIT: https://www.bcit.ca/programs/industrial-instrumentation-and-process-control-technician-diploma-full-time-2945dipma/
  HUST: https://seee.hust.edu.vn/vi/dao-tao/ee-e8/  (EN: /en/dao-tao/ee-e8/)
"""

import os
import sys
import html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import books_site as lib  # noqa: E402
from framework import (Page, section_open, section_close, write, render,  # noqa: E402
                       page_intro, bullets)

BCIT_URL = ("https://www.bcit.ca/programs/industrial-instrumentation-and-"
            "process-control-technician-diploma-full-time-2945dipma/")
HUST_URL_VI = "https://seee.hust.edu.vn/vi/dao-tao/ee-e8/"
HUST_URL_EN = "https://seee.hust.edu.vn/en/dao-tao/ee-e8/"

_cat, _dom, _ = lib.load()
BOOKS = {w["id"]: w["title"] for w in _cat["works"]}


def esc(s):
    return html.escape(s or "", quote=True)


def book_link(bid, limit=48):
    """Small inline link to a library work, or '' if the id is absent."""
    if bid is None or bid not in BOOKS:
        return ""
    t = BOOKS[bid]
    short = t if len(t) <= limit else t[:limit - 1].rstrip() + "…"
    return ('<a href="/books/work/%d/" style="text-decoration:none;">📚 %s</a>'
            % (bid, esc(short)))


# ---------------------------------------------------------------------------
# BCIT Industrial Instrumentation & Process Control Technician diploma.
# Course codes, titles and credits follow a completed BCIT transcript; the order
# is the term sequence the courses were taken in. Books are library work ids.
BCIT_TERMS = [
    ("Term 1 — DC fundamentals and instrumentation basics",
     "Kỳ 1 — Điện một chiều và cơ sở thiết bị đo",
     [
         ("INST 1000", "Điện một chiều", "DC Electricity", "6", 124),
         ("INST 1001", "Tài liệu, ký hiệu thiết bị đo &amp; CAD",
          "Instrumentation Documentation, Symbols &amp; CAD", "4", 57),
         ("INST 1103", "Cơ sở thiết bị đo", "Instrumentation Fundamentals", "6", 180),
         ("INST 2000", "Điện xoay chiều &amp; transistor",
          "AC Electricity &amp; Transistors", "7", 124),
         ("INST 2001", "Nguồn cấp &amp; khuếch đại thuật toán",
          "Power Supplies &amp; Op-Amps", "7", 124),
     ]),
    ("General studies — maintenance management",
     "Giáo dục đại cương — quản lý bảo trì",
     [
         ("PEMA 1000", "Quản lý bảo trì: nhập môn",
          "Maintenance Management: Introduction", "1", None),
     ]),
    ("Term 2 — temperature, PLCs and process control",
     "Kỳ 2 — nhiệt độ, PLC và điều khiển quá trình",
     [
         ("INST 2107", "Thiết bị đo &amp; đo nhiệt độ",
          "Temperature Instruments &amp; Measurement", "6", 32),
         ("INST 3112", "PLC &amp; HMI", "PLCs &amp; HMI", "8", 138),
         ("INST 3117", "Bộ điều khiển tương tự &amp; vi xử lý",
          "Analog &amp; Microprocessor Controllers", "8", 136),
         ("INST 3121", "Điều khiển quá trình &amp; hệ điều khiển",
          "Process Control &amp; Control Systems", "8", 142),
     ]),
    ("Term 3 — pressure, flow, level and final elements",
     "Kỳ 3 — áp suất, lưu lượng, mức và phần tử chấp hành",
     [
         ("INST 2112", "Thiết bị đo &amp; đo áp suất",
          "Pressure Instruments &amp; Measurement", "8", 146),
         ("INST 2116", "Thiết bị đo &amp; đo lưu lượng",
          "Flow Instruments &amp; Measurement", "6", 76),
         ("INST 2121", "Thiết bị đo mức &amp; khối lượng riêng",
          "Level &amp; Density Instruments &amp; Measurement", "6", 111),
         ("INST 2123", "Van điều khiển &amp; bộ định vị",
          "Control Valves &amp; Positioners", "8", 188),
         ("INST 2125", "Hệ thống thủy lực", "Hydraulic Systems", "2", 140),
     ]),
    ("Term 4 — analysis, digital logic, DCS and boilers",
     "Kỳ 4 — phân tích, logic số, DCS và lò hơi",
     [
         ("INST 3106", "Thiết bị phân tích &amp; điều khiển",
          "Analytical Instruments &amp; Control", "6", 101),
         ("INST 3110", "FET, thyristor &amp; logic số",
          "FETs &amp; Thyristors, Digital Logic", "6", 113),
         ("INST 3124", "Hệ điều khiển phân tán", "Distributed Control Systems", "6", 71),
         ("INST 3128", "Điều khiển lò hơi &amp; Foundation Fieldbus",
          "Boiler Control &amp; Foundation Fieldbus", "6", 141),
         ("INST 3130", "Độ nhớt/độ đặc, pha trộn đường ống &amp; điều khiển mẻ",
          "Viscosity/Consistency, Pipeline Blending &amp; Batch Control", "6", 100),
     ]),
]

# ---------------------------------------------------------------------------
# HUST EE-E8 curriculum. (code, vi, en, credits, book_id_or_None)
HUST_FOUNDATION = [
    ("MI1016", "Giải tích I", "Calculus I", "4", None),
    ("MI1036", "Đại số", "Algebra", "4", None),
    ("IT1016", "Tin học đại cương", "Introduction to Computer Science", "3", None),
    ("MI1026", "Giải tích II", "Calculus II", "4", None),
    ("MI1046", "Phương trình vi phân và chuỗi", "Differential Equations and Series", "3", None),
    ("PH1016", "Vật lý đại cương I", "Physics I", "4", None),
    ("MI2036", "Xác suất thống kê và tín hiệu ngẫu nhiên",
     "Probability, Statistics and Random Signals", "3", None),
    ("MI2044", "Phương pháp tính", "Numerical Methods", "2", None),
    ("PH1026", "Vật lý đại cương II", "Physics II", "4", None),
]

HUST_CORE = [
    ("EE1026E", "Nhập môn ngành Kỹ thuật điều khiển và Tự động hóa",
     "Introduction to Control Engineering and Automation", "2", None),
    ("EE2001E", "Tín hiệu và hệ thống", "Signals and Systems", "3", None),
    ("EE2021E", "Lý thuyết mạch điện I", "Electrical Circuits I", "3", None),
    ("EE3030E", "Nguyên lý trường điện từ", "Electromagnetic Fields Theory", "3", None),
    ("EE2110E", "Thiết kế điện tử", "Electronic Design", "3", None),
    ("EE3140E", "Máy điện", "Basic Electrical Machine", "3", None),
    ("EE3288E", "Lý thuyết điều khiển tuyến tính", "Linear Control Theory", "3", 27),
    ("EE3410E", "Điện tử công suất", "Power Electronics", "3", None),
    ("EE2130E", "Thiết kế hệ thống số", "Digital System Design", "3", None),
    ("EE3110E", "Kỹ thuật đo lường", "Sensors and Instrumentation", "3", 180),
    ("EE3491E", "Kỹ thuật lập trình", "Techniques of Programming", "2", None),
    ("EE2022E", "Lý thuyết mạch điện II", "Electrical Circuits II", "3", None),
    ("EE3816E", "Đồ án I", "Project I", "2", None),
    ("EE3480E", "Vi xử lý và kiến trúc máy tính",
     "Microprocessor and Computer Architecture", "3", None),
    ("EE3510E", "Truyền động điện", "Electrical Drives", "3", None),
    ("EE3826E", "Đồ án II", "Project II", "2", None),
    ("EE3424E", "Hệ thống cung cấp điện", "Power Distribution System", "3", None),
]

HUST_SPEC = [
    ("EE4221E", "Điều khiển logic và PLC", "Logic Control and PLC", "3", 4),
    ("EE3550E", "Điều khiển quá trình", "Process Control", "3", 116),
    ("EE4435E", "Hệ thống điều khiển số", "Digital Control Systems", "3", 46),
    ("EE4335E", "Trí tuệ nhân tạo trong hệ thống tự động hóa",
     "Artificial Intelligence in Automation Systems", "2", 83),
    ("EE3601E", "Hệ thống đo và điều khiển công nghiệp",
     "Industrial Instrumentation and Control System", "3", 141),
    ("EE4251E", "Thiết kế hệ thống nhúng", "Embedded System Design", "3", None),
    ("EE4331E", "Điều khiển Điện tử công suất", "Power Electronics Control", "3", None),
    ("EE4343E", "Robot và phương tiện tự hành", "Robotics and Autonomous Vehicles", "2", 161),
    ("EE4166E", "Điều khiển hệ thống năng lượng tái tạo",
     "Control of Renewable Energy Systems", "2", None),
]

HUST_PRACTICUM = [
    ("EE3916E", "Thực tập kỹ thuật", "Engineering Practicum", "2", None),
    ("EE4906E", "Đồ án tốt nghiệp cử nhân", "Bachelor's Project", "6", None),
    ("EE4922E", "Đồ án nghiên cứu Cử nhân", "Bachelor's Research Project", "8", None),
]

HUST_POLITICAL = [
    ("SSH1111", "Triết học Mác - Lênin", "Philosophy of Marxism and Leninism", "3", None),
    ("SSH1121", "Kinh tế chính trị Mác - Lênin",
     "Political Economics of Marxism and Leninism", "2", None),
    ("EM1170", "Pháp luật đại cương", "Introduction to the Legal Environment", "2", None),
    ("SSH1131", "Chủ nghĩa xã hội khoa học", "Scientific Socialism", "2", None),
    ("SSH1141", "Lịch sử Đảng cộng sản Việt Nam",
     "History of the Vietnamese Communist Party", "2", None),
    ("SSH1151", "Tư tưởng Hồ Chí Minh", "Ho Chi Minh Ideology", "2", None),
]

HUST_SUPPORT = [
    ("EE2023", "Technical Writing and Presentation", "Technical Writing and Presentation", "3", None),
    ("CH2021", "Đổi mới sáng tạo và khởi nghiệp", "Innovation and Entrepreneurship", "2", None),
    ("ED3220E", "Kỹ năng mềm", "Soft Skills", "2", None),
    ("ED3280", "Tâm lý học ứng dụng", "Applied Psychology", "2", None),
    ("EM1010", "Quản trị học đại cương", "Introduction to Management", "2", None),
    ("EM1180", "Văn hóa kinh doanh và tinh thần khởi nghiệp",
     "Business Culture and Entrepreneurship", "2", None),
    ("ET3262", "Tư duy công nghệ và thiết kế kỹ thuật",
     "Technology and Technical Design Thinking", "2", None),
    ("ME3123", "Thiết kế mỹ thuật công nghiệp", "Industrial Design", "2", None),
    ("ME3124", "Thiết kế quảng bá sản phẩm", "Product Promotion Design", "2", None),
]


def course_table(pg, rows):
    out = ('<div class="tbl-wrap mt24"><table class="tbl"><thead><tr>'
           '<th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>'
           % (pg.th("Code", "Mã"), pg.th("Course", "Học phần"),
              pg.th("Credits", "TC"), pg.th("Related book", "Sách liên quan")))
    for code, vi, en, cr, bid in rows:
        out += ('<tr><td><code>%s</code></td><td>%s</td><td>%s</td><td>%s</td></tr>'
                % (code, pg.span(en, vi), cr, book_link(bid) or "—"))
    return out + "</tbody></table></div>"


# Control, October 2026 — "Train for the plant you operate, not for the classroom"
TRAINING_GAPS = [
    (("Consumption gap.", "Khoảng trống khai thác."),
     ("Facilities still run analog — and in places pneumatic — controls even where "
      "more than 95% of field devices are digitally native, because usability was "
      "prioritised over optimisation. The HART diagnostics are already paid for and "
      "left unused, because nobody trained the technicians to implement them through "
      "installation, maintenance and troubleshooting.",
      "Nhà máy vẫn chạy điều khiển tương tự — có nơi còn khí nén — ngay cả khi hơn "
      "95% thiết bị hiện trường đã là số, vì tính dễ dùng được đặt trên tối ưu hoá. "
      "Chẩn đoán HART đã được trả tiền và bỏ đó không dùng, vì không ai huấn luyện kỹ "
      "thuật viên triển khai chúng qua lắp đặt, bảo trì và xử lý sự cố.")),
    (("Design gap.", "Khoảng trống thiết kế."),
     ("You cannot expect top-quartile performance from assets that were never "
      "engineered to support it — especially when training is booked as an "
      "unnecessary expense rather than a lifecycle performance investment. The "
      "decisions taken at the design phase get paid for several times over.",
      "Không thể đòi hiệu năng nhóm dẫn đầu từ những tài sản chưa từng được thiết kế "
      "để đạt mức đó — nhất là khi huấn luyện bị ghi như một khoản chi không cần "
      "thiết thay vì một khoản đầu tư cho hiệu năng vòng đời. Những quyết định ở "
      "khâu thiết kế rồi sẽ bị trả giá nhiều lần.")),
    (("Performance gap.", "Khoảng trống hiệu năng."),
     ("Nearly a quarter of manufacturing losses — unplanned shutdowns, scrap, "
      "slowdowns — trace back to inadequate training. Repeat failures are most often "
      "gaps in troubleshooting and in system-wide procedural understanding, and an "
      "understaffed, undertrained plant burns the time that should have gone to "
      "root-cause work.",
      "Gần một phần tư tổn thất sản xuất — dừng máy ngoài kế hoạch, hàng loại, chạy "
      "chậm — bắt nguồn từ huấn luyện không đủ. Hỏng hóc lặp lại thường là lỗ hổng về "
      "xử lý sự cố và về hiểu quy trình ở phạm vi toàn hệ thống; nhà máy thiếu người "
      "và thiếu huấn luyện thì đốt mất đúng quãng thời gian lẽ ra dành cho việc tìm "
      "nguyên nhân gốc.")),
    (("Skills gap.", "Khoảng trống kỹ năng."),
     ("A quarter of the industrial workforce is over 55 and only 8% is under 25. On "
      "the current trajectory, roughly half of those critical roles will not be "
      "filled.",
      "Một phần tư lực lượng lao động công nghiệp trên 55 tuổi và chỉ 8% dưới 25. Với "
      "quỹ đạo hiện nay, khoảng một nửa số vị trí trọng yếu ấy sẽ không có người.")),
    (("Training gap.", "Khoảng trống huấn luyện."),
     ("Adult Learning Theory research consistently shows 70% of traditional "
      "classroom instruction is forgotten within 24 hours, and 90% of new knowledge "
      "can fade within a week without hands-on reinforcement for students to revisit "
      "and use those skills.",
      "Nghiên cứu về lý thuyết học tập của người trưởng thành cho thấy 70% nội dung "
      "giảng trên lớp bị quên trong vòng 24 giờ, và 90% kiến thức mới có thể phai "
      "trong một tuần nếu không có thực hành củng cố để học viên quay lại và dùng "
      "những kỹ năng đó.")),
]

TRAINING_ASKS = [
    (("Your loop drawings are the curriculum.", "Bản vẽ vòng của bạn chính là giáo trình."),
     ("If the training package does not open with the P&amp;ID of the unit the "
      "learner actually works on, it is teaching a plant that does not exist.",
      "Nếu bộ tài liệu huấn luyện không mở đầu bằng P&amp;ID của đúng phân xưởng mà "
      "học viên đang làm, nó đang dạy một nhà máy không tồn tại.")),
    (("The diagnostics you configured are the exercise.",
      "Chẩn đoán bạn đã cấu hình chính là bài tập."),
     ("HART status, valve signature, sensor drift: these are the abnormal situations "
      "worth rehearsing, and they are already sitting in your instrument database.",
      "Trạng thái HART, chữ ký van, độ trôi cảm biến: đó là những tình huống bất "
      "thường đáng đem ra tập, và chúng đã nằm sẵn trong cơ sở dữ liệu thiết bị của "
      "bạn.")),
    (("Hours are not competence.", "Số giờ không phải năng lực."),
     ("If nobody on the shift can explain what a drifting zero does to a material "
      "balance, the training did not happen — whatever the logbook says.",
      "Nếu không ai trong ca giải thích được một điểm không bị trôi sẽ làm gì với cân "
      "bằng vật chất, thì buổi huấn luyện đó đã không xảy ra — bất kể sổ ghi thế nào.")),
]


def build():
    pg = Page(
        "education.html",
        "edu",
        "Education — BCIT & HUST control/automation programs | I&C Field Guide",
        "Giáo dục — Chương trình BCIT & HUST về điều khiển/tự động hóa | Sổ tay I&C",
        "Two control and automation programs mapped: BCIT's Industrial "
        "Instrumentation and Process Control Technician diploma and HUST's "
        "EE-E8 Control Engineering and Automation advanced program — with the "
        "curriculum and related library books.",
        "Hai chương trình điều khiển và tự động hóa được lập bản đồ: diploma Kỹ "
        "thuật viên Thiết bị đo và Điều khiển Quá trình của BCIT và chương trình "
        "tiên tiến EE-E8 Kỹ thuật Điều khiển - Tự động hóa của HUST — kèm chương "
        "trình học và sách liên quan trong thư viện.",
    )

    body = page_intro(
        pg,
        "Education — two control &amp; automation programs",
        "Giáo dục — hai chương trình điều khiển &amp; tự động hóa",
        "A bilingual study map of two programs that teach the field this site "
        "documents: BCIT's Industrial Instrumentation and Process Control "
        "Technician diploma (Canada) and HUST's EE-E8 Control Engineering and "
        "Automation advanced program (Vietnam). Each curriculum is linked to "
        "related books in the library.",
        "Bản đồ học tập song ngữ của hai chương trình dạy lĩnh vực mà trang này ghi "
        "chép: diploma Kỹ thuật viên Thiết bị đo và Điều khiển Quá trình của BCIT "
        "(Canada) và chương trình tiên tiến EE-E8 Kỹ thuật Điều khiển - Tự động hóa "
        "của HUST (Việt Nam). Mỗi chương trình được liên kết tới sách liên quan "
        "trong thư viện.",
        [
            ("programs", "Programs at a glance", "Chương trình trong một cái nhìn"),
            ("bcit", "BCIT — overview", "BCIT — tổng quan"),
            ("bcit-cur", "BCIT — curriculum &amp; books", "BCIT — chương trình &amp; sách"),
            ("hust", "HUST EE-E8 — overview", "HUST EE-E8 — tổng quan"),
            ("hust-found", "HUST — foundation &amp; core", "HUST — đại cương &amp; cơ sở"),
            ("hust-spec", "HUST — specialization &amp; practicum", "HUST — chuyên ngành &amp; tốt nghiệp"),
            ("hust-cond", "HUST — supporting &amp; conditions", "HUST — bổ trợ &amp; điều kiện"),
            ("official", "Official pages &amp; entry", "Trang chính thức &amp; đầu vào"),
            ("training", "Training &amp; the plant", "Huấn luyện &amp; nhà máy"),
            ("why", "Why it matters here", "Vì sao quan trọng ở đây"),
        ],
    )

    # 01 programs
    body += section_open("01", "Programs at a glance", "Chương trình trong một cái nhìn",
                         pg, "programs")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Two routes into the same trade", "Hai con đường vào cùng một nghề")
    body += pg.p(
        "BCIT trains instrumentation technicians to install, calibrate and maintain "
        "field instruments and PLCs. HUST's EE-E8 trains control and automation "
        "engineers across control theory, electronics, drives and intelligent "
        "systems. Both converge on the loops, signals and standards this guide covers.",
        "BCIT đào tạo kỹ thuật viên thiết bị đo lắp đặt, hiệu chuẩn và bảo trì thiết "
        "bị hiện trường cùng PLC. EE-E8 của HUST đào tạo kỹ sư điều khiển và tự động "
        "hóa qua lý thuyết điều khiển, điện tử, truyền động và hệ thống thông minh. "
        "Cả hai cùng hội tụ ở các vòng, tín hiệu và tiêu chuẩn mà sổ tay này đề cập.")
    body += "</div><div class=\"grid c2\">"
    body += ("<div class=\"card\"><h3>%s</h3><p>%s</p><p>%s</p></div>"
             % (pg.span("BCIT — Industrial Instrumentation &amp; Process Control Technician",
                        "BCIT — Kỹ thuật viên Thiết bị đo &amp; Điều khiển Quá trình"),
                pg.span("Diploma · full-time · in person · School of Energy, Canada",
                        "Diploma · toàn thời gian · trực tiếp · Trường Năng lượng, Canada"),
                pg.span("Half hands-on; field instruments, PLCs, calibration and tuning.",
                        "Một nửa thực hành; thiết bị hiện trường, PLC, hiệu chuẩn và hiệu chỉnh.")))
    body += ("<div class=\"card\"><h3>%s</h3><p>%s</p><p>%s</p></div>"
             % (pg.span("HUST EE-E8 — Control Engineering &amp; Automation",
                        "HUST EE-E8 — Kỹ thuật Điều khiển &amp; Tự động hóa"),
                pg.span("Advanced program · 4 years · 132 credits · ASIIN accredited, Vietnam",
                        "Chương trình tiên tiến · 4 năm · 132 TC · kiểm định ASIIN, Việt Nam"),
                pg.span("English-taught; control theory, electronics, drives, robotics, AI.",
                        "Dạy bằng tiếng Anh; lý thuyết điều khiển, điện tử, truyền động, robot, AI.")))
    body += "</div>"
    body += section_close()

    # 02 BCIT overview
    body += section_open("02", "BCIT — overview", "BCIT — tổng quan", pg, "bcit")
    body += "<div class=\"sec-head\">"
    body += pg.h2("A trade, taught hands-on", "Một nghề, dạy bằng thực hành")
    body += pg.p(
        "The program provides a foundation in the industrial instrumentation trade, "
        "with practical experience in applying, installing, repairing, calibrating "
        "and tuning measurement and control instruments. Delivery is in person, and "
        "half of the program is hands-on with industry-standard equipment.",
        "Chương trình xây nền tảng nghề thiết bị đo công nghiệp, với trải nghiệm thực "
        "hành trong ứng dụng, lắp đặt, sửa chữa, hiệu chuẩn và hiệu chỉnh thiết bị đo "
        "và điều khiển. Học trực tiếp tại trường, một nửa chương trình là thực hành "
        "với thiết bị chuẩn công nghiệp.")
    body += "</div><div class=\"grid c3\">"
    for en, vi, d_en, d_vi in [
        ("Credential", "Văn bằng", "Diploma, full-time", "Diploma, toàn thời gian"),
        ("School", "Trường", "School of Energy, BCIT", "Trường Năng lượng, BCIT"),
        ("Delivery", "Hình thức", "In person; half hands-on", "Trực tiếp; một nửa thực hành"),
    ]:
        body += "<div class=\"card\"><h3>%s</h3><p>%s</p></div>" % (
            pg.span(en, vi), pg.span(d_en, d_vi))
    body += "</div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Facilities &amp; pathway", "Cơ sở &amp; lộ trình"),
        pg.p(
            "Practical work happens in the Spartan Controls Centre for Energy "
            "Education and Research — two common unit operations and a steam plant. "
            "Graduates work as instrumentation and control technicians and can enter "
            "an apprenticeship at an advanced level with an industry sponsor.",
            "Thực hành diễn ra tại Trung tâm Spartan Controls về Giáo dục và Nghiên "
            "cứu Năng lượng — hai công đoạn đơn vị phổ biến và một nhà máy hơi. Sinh "
            "viên tốt nghiệp làm kỹ thuật viên thiết bị đo và điều khiển, có thể vào "
            "học việc ở bậc nâng cao với nhà tài trợ trong ngành."))
    body += section_close()

    # 03 BCIT curriculum & books
    body += section_open("03", "BCIT — curriculum &amp; books",
                         "BCIT — chương trình &amp; sách", pg, "bcit-cur")
    body += "<div class=\"sec-head\">"
    body += pg.h2("The course record, term by term", "Chương trình học, theo từng kỳ")
    body += pg.p(
        "Twenty courses, 116 credits: the diploma builds from DC electricity and "
        "documentation through every measured variable to PLCs, DCS, boilers and "
        "batch control. Every course below is paired with the library book that "
        "covers it; BCIT publishes the official course matrix on its program page.",
        "Hai mươi học phần, 116 tín chỉ: chương trình đi từ điện một chiều và tài "
        "liệu kỹ thuật, qua từng đại lượng đo, tới PLC, DCS, lò hơi và điều khiển "
        "mẻ. Mỗi học phần dưới đây được ghép với cuốn sách trong thư viện bao trùm "
        "nội dung đó; BCIT công bố ma trận môn học chính thức trên trang chương trình.")
    body += "</div>"
    for t_en, t_vi, rows in BCIT_TERMS:
        body += "<h3 class=\"mt24\">%s</h3>" % pg.span(t_en, t_vi)
        body += course_table(pg, rows)
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("About the course list", "Về danh sách học phần"),
        pg.p(
            "Codes, titles and credits are taken from a BCIT transcript for the "
            "Industrial Instrumentation &amp; Process Control Technician diploma, "
            "so the term grouping reflects one student's path rather than a fixed "
            "cohort timetable. Book pairings are editorial: each one is the closest "
            "match in the library, not a BCIT-prescribed text.",
            "Mã, tên và số tín chỉ lấy từ bảng điểm BCIT của chương trình Kỹ thuật "
            "viên Thiết bị đo &amp; Điều khiển Quá trình, nên cách nhóm theo kỳ phản "
            "ánh lộ trình của một sinh viên chứ không phải thời khóa biểu cố định. "
            "Việc ghép sách mang tính biên tập: mỗi cuốn là bản gần nhất trong thư "
            "viện, không phải giáo trình BCIT quy định."))
    body += section_close()

    # 04 HUST overview
    body += section_open("04", "HUST EE-E8 — overview", "HUST EE-E8 — tổng quan",
                         pg, "hust")
    body += "<div class=\"sec-head\">"
    body += pg.h2("An advanced, English-taught program", "Chương trình tiên tiến, dạy bằng tiếng Anh")
    body += pg.p(
        "EE-E8 is HUST's Advanced Program in Control Engineering and Automation, "
        "taught in English and accredited by ASIIN (international). It trains "
        "engineers to master modern control, robotics and automation technology, "
        "following international standards for a global career.",
        "EE-E8 là Chương trình tiên tiến về Kỹ thuật Điều khiển và Tự động hóa của "
        "HUST, dạy bằng tiếng Anh và đạt kiểm định quốc tế ASIIN. Chương trình đào "
        "tạo kỹ sư làm chủ công nghệ điều khiển, robot và tự động hóa hiện đại, bám "
        "chuẩn quốc tế để làm việc trong môi trường toàn cầu.")
    body += "</div><div class=\"grid c3\">"
    for en, vi, d_en, d_vi in [
        ("Program", "Chương trình", "EE-E8 · Advanced Program", "EE-E8 · Chương trình tiên tiến"),
        ("Duration &amp; credits", "Thời gian &amp; tín chỉ", "4 years · 132 credits",
         "4 năm · 132 TC"),
        ("Accreditation", "Kiểm định", "ASIIN (2023–2028)", "ASIIN (2023–2028)"),
    ]:
        body += "<div class=\"card\"><h3>%s</h3><p>%s</p></div>" % (
            pg.span(en, vi), pg.span(d_en, d_vi))
    body += "</div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("11 programme learning outcomes (PLO)", "11 chuẩn đầu ra (PLO)"),
        pg.p(
            "The PLOs span mathematics and science; electrical, electronics, "
            "instrumentation and control foundations; design and optimisation of "
            "automatic systems; modelling and big-data solutions; modern software "
            "tools; data analysis and AI; English communication (TOEIC 600); "
            "critical thinking and lifelong learning; multidisciplinary teamwork; "
            "professional ethics and international standards; and research project "
            "management.",
            "Các PLO bao gồm toán và khoa học; nền tảng điện, điện tử, đo lường và "
            "điều khiển; thiết kế và tối ưu hệ tự động; mô hình hóa và giải pháp dữ "
            "liệu lớn; công cụ phần mềm hiện đại; phân tích dữ liệu và AI; giao tiếp "
            "tiếng Anh (TOEIC 600); tư duy phản biện và tự học suốt đời; làm việc "
            "nhóm đa ngành; đạo đức nghề nghiệp và tiêu chuẩn quốc tế; và quản lý dự "
            "án nghiên cứu."))
    body += section_close()

    # 05 HUST foundation & core
    body += section_open("05", "HUST — foundation &amp; core",
                         "HUST — đại cương &amp; cơ sở", pg, "hust-found")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Mathematics, science and the engineering core",
                  "Toán, khoa học và cốt lõi ngành")
    body += pg.p(
        "31 credits of mathematics and basic science, then 47 credits of core "
        "engineering — circuits, electronics, machines, drives, control theory and "
        "measurement. Courses with a matching book show it in the last column.",
        "31 TC toán và khoa học cơ bản, rồi 47 TC cốt lõi ngành — mạch điện, điện "
        "tử, máy điện, truyền động, lý thuyết điều khiển và đo lường. Môn có sách "
        "phù hợp được ghi ở cột cuối.")
    body += "</div>"
    body += ("<h3 style=\"margin:1.4rem 0 .4rem\">%s <span style=\"font-weight:400;color:#888;font-size:.8rem\">· 31 TC</span></h3>"
             % pg.span("Mathematics &amp; basic science", "Toán và khoa học cơ bản"))
    body += course_table(pg, HUST_FOUNDATION)
    body += ("<h3 style=\"margin:1.4rem 0 .4rem\">%s <span style=\"font-weight:400;color:#888;font-size:.8rem\">· 47 TC</span></h3>"
             % pg.span("Core engineering", "Cơ sở và cốt lõi ngành"))
    body += course_table(pg, HUST_CORE)
    body += section_close()

    # 06 HUST specialization & practicum
    body += section_open("06", "HUST — specialization &amp; practicum",
                         "HUST — chuyên ngành &amp; tốt nghiệp", pg, "hust-spec")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Choose a module, then graduate", "Chọn một mô đun, rồi tốt nghiệp")
    body += pg.p(
        "Students choose one 24-credit specialization module (control and "
        "automation, or power/embedded/robotics tracks), then complete 16 credits "
        "of practicum and graduation project.",
        "Sinh viên chọn một mô đun chuyên ngành 24 TC (điều khiển và tự động hóa, "
        "hoặc hướng điện/embbeded/robot), rồi hoàn thành 16 TC thực tập và đồ án tốt "
        "nghiệp.")
    body += "</div>"
    body += ("<h3 style=\"margin:1.4rem 0 .4rem\">%s <span style=\"font-weight:400;color:#888;font-size:.8rem\">· 24 TC</span></h3>"
             % pg.span("Specialization module", "Mô đun chuyên ngành"))
    body += course_table(pg, HUST_SPEC)
    body += ("<h3 style=\"margin:1.4rem 0 .4rem\">%s <span style=\"font-weight:400;color:#888;font-size:.8rem\">· 16 TC</span></h3>"
             % pg.span("Practicum &amp; graduation", "Thực tập &amp; tốt nghiệp"))
    body += course_table(pg, HUST_PRACTICUM)
    body += section_close()

    # 07 HUST supporting & conditions
    body += section_open("07", "HUST — supporting &amp; conditions",
                         "HUST — bổ trợ &amp; điều kiện", pg, "hust-cond")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Supporting knowledge and conditions",
                  "Kiến thức bổ trợ và điều kiện")
    body += pg.p(
        "Alongside the technical core, the program includes political theory and law "
        "(13 credits), supporting knowledge (9 credits), plus English (18 units), "
        "physical education and national-defence education.",
        "Bên cạnh cốt lõi kỹ thuật, chương trình gồm lý luận chính trị và pháp luật "
        "(13 TC), kiến thức bổ trợ (9 TC), cùng tiếng Anh (18 đơn vị), giáo dục thể "
        "chất và giáo dục quốc phòng – an ninh.")
    body += "</div>"
    body += ("<h3 style=\"margin:1.4rem 0 .4rem\">%s <span style=\"font-weight:400;color:#888;font-size:.8rem\">· 13 TC</span></h3>"
             % pg.span("Political theory &amp; law", "Lý luận chính trị &amp; pháp luật"))
    body += course_table(pg, HUST_POLITICAL)
    body += ("<h3 style=\"margin:1.4rem 0 .4rem\">%s <span style=\"font-weight:400;color:#888;font-size:.8rem\">· 9 TC</span></h3>"
             % pg.span("Supporting knowledge", "Kiến thức bổ trợ"))
    body += course_table(pg, HUST_SUPPORT)
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Also required", "Yêu cầu khác"),
        pg.p(
            "English (18 units: IELTS skills, grammar, communication), physical "
            "education (5 credits) and national-defence education (4 units) are "
            "required but carry no credit toward the 132 total.",
            "Tiếng Anh (18 đơn vị: kỹ năng IELTS, ngữ pháp, giao tiếp), giáo dục thể "
            "chất (5 TC) và giáo dục quốc phòng – an ninh (4 đơn vị) là bắt buộc "
            "nhưng không tính vào tổng 132 TC."))
    body += section_close()

    # 08 official
    body += section_open("08", "Official pages &amp; entry", "Trang chính thức &amp; đầu vào",
                         pg, "official")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Check the source before applying", "Kiểm tra nguồn trước khi đăng ký")
    body += pg.p(
        "Entrance requirements, intakes, tuition and the full course matrix are "
        "maintained by each institution. Open the official pages to confirm current "
        "details.",
        "Yêu cầu đầu vào, đợt tuyển sinh, học phí và ma trận môn học đầy đủ do mỗi "
        "trường quản lý. Mở trang chính thức để xác nhận thông tin hiện hành.")
    body += "</div>"
    body += ("<div class=\"hero-cta\" style=\"display:flex;gap:.8rem;flex-wrap:wrap\">"
             "<a class=\"btn btn-p\" href=\"%s\" target=\"_blank\" rel=\"noopener\">%s</a>"
             "<a class=\"btn btn-p\" href=\"%s\" target=\"_blank\" rel=\"noopener\">%s</a>"
             "<a class=\"btn\" href=\"%s\" target=\"_blank\" rel=\"noopener\">%s</a></div>"
             % (BCIT_URL, pg.span("BCIT program page &rarr;", "Trang chương trình BCIT &rarr;"),
                HUST_URL_VI, pg.span("HUST EE-E8 (VI) &rarr;", "HUST EE-E8 (VI) &rarr;"),
                HUST_URL_EN, pg.span("HUST EE-E8 (EN) &rarr;", "HUST EE-E8 (EN) &rarr;")))
    body += section_close()

    # 09 training — Control, October 2026, "Other Voices"
    body += section_open("09", "From the trade press", "Từ báo ngành", pg, "training")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Train for the plant you operate, not for the classroom",
                  "Huấn luyện cho nhà máy bạn vận hành, không phải cho lớp học")
    body += pg.p(
        "You would not board an aircraft whose pilot had never touched a simulator. "
        "Luke Bicklein and Chris Helbling of Experitec argue in Control's October "
        "2026 Other Voices column that this is effectively the standard of practice "
        "across much of industrial manufacturing today — and that what separates "
        "aviation from the plant is not equipment, but how seriously the "
        "responsibility is codified into training.",
        "Bạn sẽ không lên một chiếc máy bay mà phi công chưa từng chạm vào buồng lái "
        "mô phỏng. Luke Bicklein và Chris Helbling của Experitec lập luận trên "
        "chuyên mục Other Voices của Control số tháng 10/2026 rằng đó lại đúng là "
        "chuẩn mực thực hành ở phần lớn ngành sản xuất công nghiệp hiện nay — và "
        "thứ tách hàng không khỏi nhà máy không phải thiết bị, mà là mức độ nghiêm "
        "túc mà trách nhiệm ấy được thể chế hoá vào việc huấn luyện.")
    body += "</div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("The comparison", "Phép so sánh"),
        pg.p("“You wouldn't board an airplane whose pilot never touched a flight "
             "simulator. Yet, that's effectively the standard of practice across "
             "much of the industrial manufacturing sector today.”",
             "“Bạn sẽ không lên một chiếc máy bay mà phi công chưa từng chạm vào "
             "buồng lái mô phỏng. Vậy mà đó lại đúng là chuẩn mực thực hành ở phần "
             "lớn ngành sản xuất công nghiệp hiện nay.”"))
    body += "<h3 class=\"mt24\">%s</h3>" % pg.span(
        "Two professions, two attitudes to proof", "Hai nghề, hai thái độ với bằng chứng")
    body += pg.p(
        "Put an airline cockpit and a processing plant control room side by side and "
        "the parallels are striking: both demand split-second judgment from people "
        "carrying enormous responsibility for human safety, capital assets, "
        "environmental stewardship and brand reputation. Where the two diverge is in "
        "how that responsibility is codified. Aviation institutionalised recurring "
        "training and mandatory proficiency checks, so crews are prepared for "
        "abnormal situations before they arise in service. Manufacturers are left "
        "interpreting OSHA expectations that lack clear certification guidelines and "
        "enforcement.",
        "Đặt buồng lái máy bay cạnh phòng điều khiển nhà máy chế biến, các điểm tương "
        "đồng rất rõ: cả hai đều đòi hỏi phán đoán trong tích tắc từ những người mang "
        "trách nhiệm lớn với an toàn con người, tài sản vốn, môi trường và uy tín "
        "thương hiệu. Chỗ hai nghề rẽ nhau là cách trách nhiệm ấy được thể chế hoá. "
        "Hàng không đã thể chế hoá huấn luyện định kỳ và các kỳ kiểm tra năng lực bắt "
        "buộc, để tổ bay được chuẩn bị cho tình huống bất thường trước khi chúng xảy "
        "ra trong khai thác. Người sản xuất thì phải tự diễn giải các yêu cầu của "
        "OSHA — vốn thiếu hướng dẫn chứng nhận rõ ràng và thiếu cả cơ chế cưỡng chế.")
    body += "<h3 class=\"mt24\">%s</h3>" % pg.span(
        "The numbers are not close", "Những con số không hề sát nhau")
    body += pg.p(
        "Operators log an average of 20 training hours a year against a recommended "
        "minimum of 60 from multiple industrial bodies, and the hours actually "
        "completed keep trending down. Fewer than half of plant operators today are "
        "formally trained on a digital twin or an operator training system — the "
        "direct analogue of the flight simulator, and the only place where "
        "abnormal-situation training can happen without consequence.",
        "Vận hành viên ghi nhận trung bình 20 giờ huấn luyện mỗi năm, so với mức tối "
        "thiểu 60 giờ mà nhiều tổ chức ngành khuyến nghị, và số giờ thực hoàn thành "
        "vẫn đang giảm. Chưa tới một nửa số vận hành viên nhà máy hiện nay được huấn "
        "luyện chính quy trên digital twin hoặc hệ thống huấn luyện vận hành (OTS) — "
        "thứ tương đương trực tiếp của buồng lái mô phỏng, và là nơi duy nhất có thể "
        "huấn luyện tình huống bất thường mà không phải trả giá.")
    body += "<h3 class=\"mt24\">%s</h3>" % pg.span("Five gaps that compound",
                                                   "Năm khoảng trống cộng dồn")
    body += bullets(pg, TRAINING_GAPS)
    body += "<h3 class=\"mt24\">%s</h3>" % pg.span("What actually works",
                                                   "Cái gì thực sự hiệu quả")
    body += pg.p(
        "Classroom instruction paired with hands-on reinforcement — not one in place "
        "of the other — and room to fail safely. The 3Ds of training, describe, "
        "demonstrate, do, forge the muscle memory; scenario-based training "
        "consistently beats sequential, step-by-step instruction because it layers "
        "deductive reasoning on top of practice, and that is the difference between a "
        "troubleshooter and someone chasing symptoms. It is the same reason pilots "
        "log more simulator hours than flight hours.",
        "Giảng trên lớp đi kèm thực hành củng cố — không phải cái này thay cái kia — "
        "và phải có chỗ cho phép sai một cách an toàn. Ba chữ D của huấn luyện — mô "
        "tả, làm mẫu, tự làm — tạo nên phản xạ; huấn luyện theo tình huống luôn thắng "
        "chỉ dẫn tuần tự từng bước, vì nó xếp thêm năng lực suy luận diễn dịch lên "
        "trên phần thực hành, và đó chính là khác biệt giữa người xử lý sự cố thật và "
        "người chỉ chạy theo triệu chứng. Cũng vì lẽ đó phi công ghi nhiều giờ bay mô "
        "phỏng hơn giờ bay thật.")
    body += pg.p(
        "Experitec turned those principles into the Performance Learning Platform: a "
        "factory on wheels. A working miniature process — pumps moving fluid through "
        "real equipment, pressure, temperature, level and flow instruments measuring "
        "it, control valves manipulating it, a modern control system closing the "
        "loops, and the asset-management, calibration and diagnostic tools the "
        "learner will meet in a real plant. It began as internal onboarding for young "
        "engineers, then was extended to manufacturers and educators chasing the same "
        "outcome.",
        "Experitec biến những nguyên tắc ấy thành Performance Learning Platform: một "
        "“nhà máy trên bánh xe”. Một quá trình thu nhỏ nhưng chạy thật — bơm đẩy lưu "
        "chất qua thiết bị thật, thiết bị đo áp suất, nhiệt độ, mức và lưu lượng đo "
        "chính quá trình ấy, van điều khiển tác động lên nó, một hệ điều khiển hiện "
        "đại khép các vòng, cùng những công cụ quản lý tài sản, hiệu chuẩn và chẩn "
        "đoán mà học viên sẽ gặp trong nhà máy thật. Ban đầu nó là chương trình hội "
        "nhập nội bộ cho kỹ sư trẻ, rồi được mở rộng cho các nhà sản xuất và cơ sở "
        "đào tạo cùng theo đuổi kết quả ấy.")
    body += pg.p(
        "The evidence that this matters is not in the survey data but in the "
        "schedule. Ask any outage manager how many days are added to loop checkouts "
        "because field devices were left out of service. That is a training failure "
        "surfacing as a turnaround overrun — and it is fixed by practice, not by "
        "another slide deck.",
        "Bằng chứng cho thấy điều này quan trọng không nằm trong số liệu khảo sát mà "
        "nằm ở tiến độ. Hỏi bất kỳ quản đốc đại tu nào xem có bao nhiêu ngày bị cộng "
        "thêm vào phần kiểm tra vòng vì thiết bị hiện trường bị bỏ ngoài vận hành. Đó "
        "là một thất bại huấn luyện hiện ra dưới dạng một lần đại tu vượt tiến độ — "
        "và nó chỉ được sửa bằng thực hành, không bằng thêm một bộ slide.")
    body += "<h3 class=\"mt24\">%s</h3>" % pg.span(
        "What this asks of the people who own the loops",
        "Điều này đặt ra gì cho người chịu trách nhiệm các vòng điều khiển")
    body += bullets(pg, TRAINING_ASKS)
    body += ("<ul class=\"adv-src\"><li><span class=\"tag\">Trade press</span>"
             "<a href=\"https://www.controlglobal.com/\" rel=\"noopener\">%s</a> — %s</li></ul>" % (
                 pg.span("Control — “Train for the plant you operate, not for the "
                         "classroom”, Luke Bicklein and Chris Helbling, Other Voices",
                         "Control — “Train for the plant you operate, not for the "
                         "classroom”, Luke Bicklein và Chris Helbling, Other Voices"),
                 pg.span("October 2026, pp. 10–11. The aviation comparison, the "
                         "20-versus-60 hours, the five gaps, the 3Ds, and the "
                         "Performance Learning Platform.",
                         "Tháng 10/2026, tr. 10–11. Phép so sánh với hàng không, 20 so "
                         "với 60 giờ, năm khoảng trống, ba chữ D, và Performance "
                         "Learning Platform.")))
    body += section_close()

    # 10 why
    body += section_open("10", "Why it matters here", "Vì sao quan trọng ở đây",
                         pg, "why")
    body += "<div class=\"sec-head\">"
    body += pg.h2("The same loops, studied formally", "Cùng những vòng, được học bài bản")
    body += pg.p(
        "Every topic on this site — measurement, transducers, valves, PID, PLCs, "
        "safety — is what these two programs teach in a structured way. Use the "
        "field guide to revise the theory, and the programs to see how it is taught, "
        "practised and assessed.",
        "Mọi chủ đề trên trang này — đo lường, cảm biến, van, PID, PLC, an toàn — "
        "đều là nội dung hai chương trình này dạy một cách bài bản. Dùng sổ tay để "
        "ôn lý thuyết, và các chương trình để xem cách dạy, thực hành và đánh giá.")
    body += "</div>"
    body += "<div class=\"nextprev\">"
    body += "<a href=\"applications.html\"><span class=\"k\">%s</span>%s</a>" % (
        pg.span("Back", "Quay lại"), pg.span("Applications", "Ứng dụng"))
    body += "<a href=\"index.html\" style=\"text-align:right\"><span class=\"k\">%s</span>%s</a>" % (
        pg.span("Next", "Tiếp"), pg.span("Home", "Trang chủ"))
    body += "</div>"
    body += section_close()

    write("education.html", render(pg, body, "education.html"))
