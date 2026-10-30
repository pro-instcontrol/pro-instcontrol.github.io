# -*- coding: utf-8 -*-
"""Education — BCIT Industrial Instrumentation & Process Control Technician.

Publishes the program structure of BCIT's Industrial Instrumentation and
Process Control Technician diploma (School of Energy, full-time, in person)
as a bilingual study guide, with a link to the official BCIT page for the
authoritative course matrix and entrance requirements.

Source: https://www.bcit.ca/programs/industrial-instrumentation-and-process-control-technician-diploma-full-time-2945dipma/
"""

from framework import Page, section_open, section_close, write, render, page_intro

BCIT_URL = ("https://www.bcit.ca/programs/industrial-instrumentation-and-"
            "process-control-technician-diploma-full-time-2945dipma/")

# Curriculum coverage areas — the topic areas the diploma builds across its
# terms (drawn from BCIT's stated program description and the standard
# instrumentation-technician body of knowledge).
COVERAGE = [
    ("Safety, codes & standards",
     "An toàn, quy chuẩn & tiêu chuẩn",
     "Lockout/tagout, hazardous locations, electrical safety, and the codes that "
     "govern instrument installation in industrial plants.",
     "Khóa/dán nhãn, vùng nguy hiểm, an toàn điện và các quy chuẩn chi phối việc "
     "lắp đặt thiết bị đo trong nhà máy."),
    ("Electrical & electronic fundamentals",
     "Cơ sở điện & điện tử",
     "Ohm's law, AC/DC circuits, semiconductors, op-amps and the signal electronics "
     "behind every transmitter and controller.",
     "Định luật Ohm, mạch xoay/chiều, bán dẫn, op-amp và điện tử tín hiệu đằng sau "
     "mọi bộ truyền và bộ điều khiển."),
    ("Measurement: temperature, pressure, flow, level",
     "Đo lường: nhiệt độ, áp suất, lưu lượng, mức",
     "The four core process variables — thermocouples and RTDs, pressure and DP "
     "transmitters, orifice and Coriolis flow, radar and DP level.",
     "Bốn biến quá trình cốt lõi — cặp nhiệt và RTD, truyền áp và DP, lưu lượng lỗ "
     "khoan và Coriolis, mức radar và DP."),
    ("Transducers & signal conditioning",
     "Cảm biến & điều chế tín hiệu",
     "Converting a physical quantity into 4–20 mA, HART, or a fieldbus value — and "
     "linearising, ranging and filtering it.",
     "Chuyển đại lượng vật lý thành 4–20 mA, HART hay giá trị fieldbus — rồi tuyến "
     "tính hóa, đặt dải và lọc."),
    ("Control valves & actuators",
     "Van điều khiển & cơ cấu chấp hành",
     "Valve types, Cv sizing, positioners, and the final control element that turns "
     "a controller output into a physical change.",
     "Các loại van, tính Cv, bộ định vị và phần tử điều khiển cuối biến đầu ra bộ "
     "điều khiển thành thay đổi vật lý."),
    ("PID control & tuning",
     "Điều khiển PID & hiệu chỉnh",
     "Proportional, integral and derivative action, loop stability, and the "
     "practical tuning methods used to make a loop behave.",
     "Tác động tỷ lệ, tích phân và vi phân, ổn định vòng và các phương pháp hiệu "
     "chỉnh thực tế để vòng hoạt động đúng."),
    ("PLCs & automation",
     "PLC & tự động hóa",
     "Programming programmable logic controllers and computerized controls that "
     "run the required function within a manufacturing process.",
     "Lập trình PLC và điều khiển máy tính thực hiện chức năng yêu cầu trong một "
     "quá trình sản xuất."),
    ("Calibration, loop checking & documentation",
     "Hiệu chuẩn, kiểm tra vòng & tài liệu",
     "Bench and field calibration, loop checkout, P&IDs, loop sheets and the records "
     "that prove a measurement is true.",
     "Hiệu chuẩn tại xưởng và hiện trường, kiểm tra vòng, P&ID, phiếu vòng và hồ sơ "
     "chứng minh phép đo là đúng."),
]

CAREERS = [
    ("Instrumentation & control technician",
     "Kỹ thuật viên thiết bị đo & điều khiển",
     "Install, maintain, calibrate and troubleshoot field instruments and control "
     "systems across manufacturing and process industries.",
     "Lắp đặt, bảo trì, hiệu chuẩn và xử lý sự cố thiết bị đo hiện trường và hệ "
     "điều khiển trong nhiều ngành sản xuất và chế biến."),
    ("Advanced apprenticeship entry",
     "Vào nghề học việc ở bậc nâng cao",
     "Graduates can transition into an apprenticeship at an advanced level with an "
     "industry sponsor.",
     "Sinh viên tốt nghiệp có thể chuyển vào chương trình học việc ở bậc nâng cao "
     "với nhà tài trợ trong ngành."),
    ("Job-ready, hands-on",
     "Sẵn sàng làm việc, thực hành",
     "Half the program is hands-on with industry-standard equipment, so graduates "
     "arrive ready for the plant floor.",
     "Một nửa chương trình là thực hành với thiết bị chuẩn công nghiệp, nên sinh "
     "viên tốt nghiệp sẵn sàng cho sàn nhà máy."),
]


def build():
    pg = Page(
        "education.html",
        "edu",
        "Education — BCIT Industrial Instrumentation & Process Control | I&C Field Guide",
        "Giáo dục — BCIT Kỹ thuật viên Thiết bị đo & Điều khiển Quá trình | Sổ tay I&C",
        "The BCIT Industrial Instrumentation and Process Control Technician diploma "
        "— what the program covers, how it is taught, and where it leads. A study "
        "map for the field this site documents.",
        "Chương trình diploma Kỹ thuật viên Thiết bị đo và Điều khiển Quá trình của "
        "BCIT — chương trình dạy gì, dạy thế nào và dẫn tới đâu. Bản đồ học tập cho "
        "lĩnh vực mà trang này ghi chép.",
    )

    body = page_intro(
        pg,
        "BCIT Industrial Instrumentation &amp; Process Control Technician",
        "Kỹ thuật viên Thiết bị đo &amp; Điều khiển Quá trình — BCIT",
        "A full-time, in-person diploma from BCIT's School of Energy that builds a "
        "foundation in the industrial instrumentation trade: applying, installing, "
        "repairing, calibrating and tuning the measurement and control instruments "
        "used in industrial manufacturing.",
        "Chương trình diploma toàn thời gian, học trực tiếp tại Trường Năng lượng "
        "BCIT, xây nền tảng nghề thiết bị đo công nghiệp: ứng dụng, lắp đặt, sửa "
        "chữa, hiệu chuẩn và hiệu chỉnh các thiết bị đo và điều khiển dùng trong "
        "sản xuất công nghiệp.",
        [
            ("overview", "Program at a glance", "Chương trình trong một cái nhìn"),
            ("coverage", "Curriculum coverage", "Nội dung chương trình"),
            ("facilities", "Facilities", "Cơ sở thực hành"),
            ("careers", "Careers &amp; pathway", "Nghề nghiệp &amp; lộ trình"),
            ("apply", "Official page &amp; entry", "Trang chính thức &amp; đầu vào"),
            ("why", "Why it matters here", "Vì sao quan trọng ở đây"),
        ],
    )

    # 01 overview
    body += section_open("01", "Program at a glance", "Chương trình trong một cái nhìn",
                         pg, "overview")
    body += "<div class=\"sec-head\">"
    body += pg.h2("A trade, taught hands-on", "Một nghề, dạy bằng thực hành")
    body += pg.p(
        "The program provides a foundation in the industrial instrumentation trade, "
        "with practical, hands-on experience in applying, installing, repairing, "
        "calibrating and tuning measurement and control instruments. Delivery is in "
        "person, and half of the program's duration is dedicated to hands-on work "
        "with industry-standard equipment.",
        "Chương trình xây nền tảng nghề thiết bị đo công nghiệp, với trải nghiệm thực "
        "hành trong ứng dụng, lắp đặt, sửa chữa, hiệu chuẩn và hiệu chỉnh thiết bị đo "
        "và điều khiển. Học trực tiếp tại trường, và một nửa thời lượng dành cho thực "
        "hành với thiết bị chuẩn công nghiệp.")
    body += "</div>"
    body += "<div class=\"grid c3\">"
    for en, vi, d_en, d_vi in [
        ("Credential", "Văn bằng", "Diploma, full-time", "Diploma, toàn thời gian"),
        ("School", "Trường", "School of Energy, BCIT", "Trường Năng lượng, BCIT"),
        ("Delivery", "Hình thức", "In person; half hands-on",
         "Trực tiếp; một nửa thực hành"),
    ]:
        body += "<div class=\"card\"><h3>%s</h3><p>%s</p></div>" % (
            pg.span(en, vi), pg.span(d_en, d_vi))
    body += "</div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("What students do", "Sinh viên làm gì"),
        pg.p(
            "Students install and maintain field instruments that are part of "
            "large-scale manufacturing systems — digital, electronic, pneumatic or "
            "hydraulic devices — and learn to program the computerized controls and "
            "programmable logic controllers (PLCs) that perform the required function "
            "within manufacturing.",
            "Sinh viên lắp đặt và bảo trì thiết bị đo hiện trường thuộc các hệ sản xuất "
            "quy mô lớn — thiết bị số, điện tử, khí nén hoặc thủy lực — và học lập "
            "trình điều khiển máy tính cùng PLC thực hiện chức năng yêu cầu trong sản "
            "xuất."))
    body += section_close()

    # 02 coverage
    body += section_open("02", "Curriculum coverage", "Nội dung chương trình",
                         pg, "coverage")
    body += "<div class=\"sec-head\">"
    body += pg.h2("The body of knowledge, term by term", "Khối kiến thức, theo từng kỳ")
    body += pg.p(
        "Across its terms the diploma builds the instrumentation technician's core "
        "competencies — from electrical fundamentals and the four process variables "
        "through valves, PID control, PLCs and calibration. BCIT publishes the exact "
        "course matrix, course codes and credit values on the official program page.",
        "Qua các kỳ, chương trình xây các năng lực cốt lõi của kỹ thuật viên thiết bị "
        "đo — từ cơ sở điện và bốn biến quá trình, qua van, điều khiển PID, PLC và "
        "hiệu chuẩn. BCIT công bố ma trận môn học, mã môn và số tín chỉ chính xác trên "
        "trang chương trình chính thức.")
    body += "</div>"
    body += "<div class=\"grid c2\">"
    for en, vi, d_en, d_vi in COVERAGE:
        body += "<div class=\"card\"><h3>%s</h3><p>%s</p></div>" % (
            pg.span(en, vi), pg.span(d_en, d_vi))
    body += "</div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Authoritative source", "Nguồn chính thức"),
        pg.p(
            "This is a study summary, not the official calendar. For the current "
            "course matrix, credits and entrance requirements, use the official BCIT "
            "program page linked below.",
            "Đây là bản tóm tắt học tập, không phải lịch học chính thức. Để có ma trận "
            "môn học, số tín chỉ và yêu cầu đầu vào hiện hành, hãy dùng trang chương "
            "trình chính thức của BCIT ở liên kết bên dưới."))
    body += section_close()

    # 03 facilities
    body += section_open("03", "Facilities", "Cơ sở thực hành", pg, "facilities")
    body += "<div class=\"sec-head\">"
    body += pg.h2("The Spartan Controls Centre", "Trung tâm Spartan Controls")
    body += pg.p(
        "Practical learning happens in the Spartan Controls Centre for Energy "
        "Education and Research — a world-class facility with two common unit "
        "operations and a steam plant, giving students realistic loops to instrument, "
        "calibrate and control.",
        "Việc học thực hành diễn ra tại Trung tâm Spartan Controls về Giáo dục và "
        "Nghiên cứu Năng lượng — cơ sở đẳng cấp thế giới với hai công đoạn đơn vị phổ "
        "biến và một nhà máy hơi, cho sinh viên những vòng thực tế để gắn thiết bị, "
        "hiệu chuẩn và điều khiển.")
    body += "</div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Why it matters", "Vì sao quan trọng"),
        pg.p(
            "A steam plant and real unit operations let students see the loops this "
            "site documents in action — drum level, combustion, flow and temperature "
            "control — rather than only on paper.",
            "Một nhà máy hơi và các công đoạn thực cho sinh viên thấy những vòng mà "
            "trang này ghi chép hoạt động thực tế — mức nước trống, cháy, lưu lượng và "
            "nhiệt độ — chứ không chỉ trên giấy."))
    body += section_close()

    # 04 careers
    body += section_open("04", "Careers &amp; pathway", "Nghề nghiệp &amp; lộ trình",
                         pg, "careers")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Where graduates go", "Sinh viên tốt nghiệp đi đâu")
    body += pg.p(
        "Graduates pursue employment as technicians in the instrumentation and "
        "control field across diverse industries, and can transition into an "
        "apprenticeship at an advanced level with an industry sponsor.",
        "Sinh viên tốt nghiệp làm kỹ thuật viên trong lĩnh vực thiết bị đo và điều "
        "khiển ở nhiều ngành, và có thể chuyển vào chương trình học việc ở bậc nâng "
        "cao với nhà tài trợ trong ngành.")
    body += "</div>"
    body += "<div class=\"grid c3\">"
    for en, vi, d_en, d_vi in CAREERS:
        body += "<div class=\"card\"><h3>%s</h3><p>%s</p></div>" % (
            pg.span(en, vi), pg.span(d_en, d_vi))
    body += "</div>"
    body += section_close()

    # 05 apply
    body += section_open("05", "Official page &amp; entry", "Trang chính thức &amp; đầu vào",
                         pg, "apply")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Apply through BCIT", "Đăng ký qua BCIT")
    body += pg.p(
        "Entrance requirements, intake dates, tuition and the full course matrix are "
        "maintained by BCIT. Open the official program page to check the current "
        "details before applying.",
        "Yêu cầu đầu vào, ngày nhập học, học phí và ma trận môn học đầy đủ do BCIT "
        "quản lý. Mở trang chương trình chính thức để kiểm tra thông tin hiện hành "
        "trước khi đăng ký.")
    body += "</div>"
    body += ("<div class=\"hero-cta\"><a class=\"btn btn-p\" href=\"%s\" "
             "target=\"_blank\" rel=\"noopener\">%s</a></div>"
             % (BCIT_URL, pg.span("Open the official BCIT program page &rarr;",
                                  "Mở trang chương trình BCIT chính thức &rarr;")))
    body += section_close()

    # 06 why
    body += section_open("06", "Why it matters here", "Vì sao quan trọng ở đây",
                         pg, "why")
    body += "<div class=\"sec-head\">"
    body += pg.h2("The same loops, studied formally", "Cùng những vòng, được học bài bản")
    body += pg.p(
        "Every topic on this site — measurement, transducers, valves, PID, safety — "
        "is what this diploma teaches in a structured, hands-on program. Use the "
        "field guide to revise the theory, and the BCIT program to see how it is "
        "taught and assessed.",
        "Mọi chủ đề trên trang này — đo lường, cảm biến, van, PID, an toàn — đều là "
        "nội dung chương trình diploma này dạy một cách bài bản, thực hành. Dùng sổ "
        "tay để ôn lý thuyết, và chương trình BCIT để xem cách dạy và đánh giá.")
    body += "</div>"
    body += "<div class=\"nextprev\">"
    body += "<a href=\"applications.html\"><span class=\"k\">%s</span>%s</a>" % (
        pg.span("Back", "Quay lại"), pg.span("Applications", "Ứng dụng"))
    body += "<a href=\"index.html\" style=\"text-align:right\"><span class=\"k\">%s</span>%s</a>" % (
        pg.span("Next", "Tiếp"), pg.span("Home", "Trang chủ"))
    body += "</div>"
    body += section_close()

    write("education.html", render(pg, body, "education.html"))
