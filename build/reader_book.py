# -*- coding: utf-8 -*-
"""Generic reader landing-page generator for any book in the library.

Usage:
    python reader_book.py            # renders every BOOKS entry below
    python reader_book.py sis        # renders only the 'sis' book

Each book is a SPEC dict (see BOOKS).  The generator mirrors the
taichikb.github.io/books reader structure and the styling in
books/assets/library.css.  Chapter 1 (and any other translated chapter)
must already exist as a reader page under:

    vi/books/read/<slug>/<chap-slug>/index.html
    books/read/<slug>/<chap-slug>/index.html
"""
import os

from books_site import MARK, NAV_EN, NAV_VI, esc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Book specifications
# ---------------------------------------------------------------------------
BOOKS = {
    "sis": {
        "slug": "safety-instrumented-systems-design-analysis-justification",
        "title_en": "Safety Instrumented Systems — Design, Analysis, and Justification",
        "title_vi": "Hệ thống đo lường an toàn — Thiết kế, phân tích và biện minh",
        "byline_en": "Paul Gruhn, P.E., CFSE & Harry L. Cheddie, P.Eng., CFSE · ISA, 2006 (2nd ed.)",
        "byline_vi": "Paul Gruhn, P.E., CFSE & Harry L. Cheddie, P.Eng., CFSE · ISA, 2006 (bản 2)",
        "pages": 320,
        "files": 19,
        "first_en": ("ch01-introduction",
                     "Introduction"),
        "first_vi": ("ch01-introduction",
                     "Giới thiệu"),
        "chapters": {
            1: ("Introduction", "Giới thiệu"),
            2: ("Design Lifecycle", "Vòng đời thiết kế"),
            3: ("Process Control vs. Safety Control", "Điều khiển quá trình so với điều khiển an toàn"),
            4: ("Protection Layers", "Các lớp bảo vệ"),
            5: ("Developing the Safety Requirement Specifications", "Xây dựng đặc tả yêu cầu an toàn"),
            6: ("Determining the Safety Integrity Level (SIL)", "Xác định mức toàn vẹn an toàn (SIL)"),
            7: ("Choosing a Technology", "Lựa chọn công nghệ"),
            8: ("Initial System Evaluation", "Đánh giá hệ thống ban đầu"),
            9: ("Issues Relating to Field Devices", "Các vấn đề liên quan đến thiết bị trường"),
            10: ("Engineering a System", "Thiết kế kỹ thuật một hệ thống"),
            11: ("Installing a System", "Lắp đặt hệ thống"),
            12: ("Functional Testing", "Thử nghiệm chức năng"),
            13: ("Managing Changes to a System", "Quản lý thay đổi hệ thống"),
            14: ("Justification for a Safety System", "Biện minh cho hệ thống an toàn"),
            15: ("SIS Design Checklist", "Danh mục kiểm tra thiết kế SIS"),
            16: ("Case Study", "Nghiên cứu tình huống"),
        },
        "done": {1: "ch01-introduction", 2: "ch02-design-lifecycle",
                 3: "ch03-process-control-vs-safety-control",
                 4: "ch04-protection-layers",
                 5: "ch05-developing-the-safety-requirement-specifications",
                 6: "ch06-determining-the-safety-integrity-level",
                 7: "ch07-choosing-a-technology",
                 8: "ch08-initial-system-evaluation",
                 9: "ch09-issues-relating-to-field-devices",
                 10: "ch10-engineering-a-system",
                 11: "ch11-installing-a-system",
                 12: "ch12-functional-testing",
                 13: "ch13-managing-changes-to-a-system",
                 14: "ch14-justification-for-a-safety-system",
                 15: "ch15-sis-design-checklist",
                 16: "ch16-case-study"},
        "copyright_en": "Original text © 2006 ISA — The Instrumentation, Systems, and Automation Society",
        "copyright_vi": "Bản gốc © 2006 ISA — Hiệp hội Đo lường, Hệ thống và Tự động hóa",
        "lede_en": ("The practical “how-to” on specifying, analysing, designing, installing and "
                    "justifying safety instrumented systems — from the difference between process "
                    "control and safety control through to lifecycle management. The Vietnamese "
                    "translation proceeds chapter by chapter."),
        "lede_done_en": ("The practical “how-to” on specifying, analysing, designing, installing and "
                         "justifying safety instrumented systems — from the difference between process "
                         "control and safety control through to lifecycle management. The Vietnamese "
                         "translation is complete: all sixteen chapters."),
        "lede_vi": ("Cuốn sách thực hành “cách làm” về xác định, phân tích, thiết kế, lắp đặt và "
                    "biện minh cho các hệ thống đo lường an toàn — từ sự khác biệt giữa điều khiển "
                    "quá trình và điều khiển an toàn cho đến quản lý vòng đời. Bản dịch tiếng Việt "
                    "thực hiện theo từng chương."),
        "lede_done_vi": ("Cuốn sách thực hành “cách làm” về xác định, phân tích, thiết kế, lắp đặt và "
                         "biện minh cho các hệ thống đo lường an toàn — từ sự khác biệt giữa điều "
                         "khiển quá trình và điều khiển an toàn cho đến quản lý vòng đời. Bản dịch "
                         "tiếng Việt đã hoàn tất: đủ mười sáu chương."),
        "policy_en": ("<b>About this copy.</b> The 19 PDF files are held in the local library "
                      "catalogue and are not republished here. This page is the online contents "
                      "map: what each chapter covers and which chapters already have a Vietnamese "
                      "translation."),
        "policy_done_en": ("<b>About this copy.</b> The 19 PDF files are held in the local library "
                           "catalogue and are not republished here. This page is the online contents "
                           "map: what each chapter covers, with a link to the Vietnamese translation "
                           "of all sixteen chapters."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> 19 tệp PDF được lưu trong thư viện cục bộ và "
                      "không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội "
                      "dung từng chương và những chương nào đã có bản dịch tiếng Việt."),
        "policy_done_vi": ("<b>Cách đọc bản dịch.</b> 19 tệp PDF được lưu trong thư viện cục bộ và "
                           "không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội "
                           "dung từng chương, kèm liên kết tới bản dịch tiếng Việt của cả mười sáu "
                           "chương."),
        "note_en": "Figures follow the original numbering where the source chapter contains them.",
        "note_vi": "Hình ảnh giữ nguyên số hiệu của bản gốc tại những chương có hình.",
    },

    "pc": {
        "slug": "pc-process-control",
        "title_en": "Practical Process Control for Engineers and Technicians",
        "title_vi": "Điều khiển quá trình thực hành dành cho kỹ sư và kỹ thuật viên",
        "byline_en": "Wolfgang Altmann · IDC Technologies (Version 3.02)",
        "byline_vi": "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)",
        "pages": 1008,
        "files": 35,
        "first_en": ("ch01-introduction",
                     "Introduction"),
        "first_vi": ("ch01-introduction",
                     "Giới thiệu"),
        "chapters": {
            1: ("Introduction", "Giới thiệu"),
            2: ("Process Measurement and Transducers", "Đo lường quá trình và cảm biến"),
            3: ("Basic Principles of Control Valves and Actuators", "Nguyên lý cơ bản của van điều khiển và cơ cấu chấp hành"),
            4: ("Fundamentals of Control Systems", "Các nguyên lý cơ bản của hệ thống điều khiển"),
            5: ("Stability and Control Modes of Closed Loops", "Ổn định và các mode điều khiển vòng kín"),
            6: ("Digital Control Principles", "Các nguyên lý điều khiển số"),
            7: ("Real and Ideal P.I.D. Controllers", "Bộ điều khiển PID thực và lý tưởng"),
            8: ("Tuning of PID Controllers in Open and Closed Loop", "Tìm điểm làm việc bộ điều khiển PID"),
            9: ("Controller Output Modes, Equations and Cascade Control", "Các mode đầu ra, phương trình và điều khiển bậc thang"),
            10: ("Concepts and Applications of Feedforward Control", "Khái niệm và ứng dụng điều khiển theo hướng"),
            11: ("Combined Feedback and Feedforward Control", "Kết hợp phản hồi và theo hướng"),
            12: ("Long Process Dead-Time and the Smith Predictor", "Trễ chết dài và bộ dự đoán Smith"),
            13: ("Basic Principles of Fuzzy Logic and Neural Networks", "Nguyên lý cơ bản của lô-gic mờ và mạng nơ-ron"),
            14: ("Self-Tuning Intelligent Control and SPC", "Tự chỉnh định, điều khiển thông minh và SPC"),
        },
        "appendices": [
            ("A", "Some Laplace Transform Pairs", "Một số cặp biến đổi Laplace"),
            ("B", "Block Diagram Transformation Theorems", "Các định lý biến đổi sơ đồ khối"),
            ("C", "Detail Display", "Hiển thị chi tiết"),
            ("D", "Auxiliary Display", "Hiển thị phụ trợ"),
            ("E", "Configuring a Tuning Exercise in a Controller", "Cấu hình bài tập tìm điểm trong bộ điều khiển"),
            ("F", "Installation of Simulation Software", "Cài đặt phần mềm mô phỏng"),
            ("G", "Operation of Simulation Software", "Vận hành phần mềm mô phỏng"),
            ("H", "Configuration", "Cấu hình"),
            ("I", "General Syntax of Configuration Commands", "Cú pháp chung của lệnh cấu hình"),
            ("J", "Configuration Commands", "Các lệnh cấu hình"),
            ("K", "Algorithms", "Các thuật toán"),
            ("L", "Background Graphics Design", "Thiết kế đồ họa nền"),
            ("M", "Configuration Example", "Ví dụ cấu hình"),
        ],
        "done": {1: "ch01-introduction",
                 2: "ch02-process-measurement-and-transducers",
                 3: "ch03-basic-principles-of-control-valves-and-actuators",
                 4: "ch04-fundamentals-of-control-systems",
                 5: "ch05-stability-and-control-modes-of-closed-loops",
                 6: "ch06-digital-control-principles",
                 7: "ch07-real-and-ideal-pid-controllers",
                 8: "ch08-tuning-of-pid-controllers",
                 9: "ch09-output-modes-equations-and-cascade-control",
                 10: "ch10-concepts-and-applications-of-feedforward-control",
                 11: "ch11-combined-feedback-and-feedforward-control",
                 12: "ch12-long-dead-time-and-the-smith-predictor",
                 13: "ch13-basic-principles-of-fuzzy-logic-and-neural-networks",
                 14: "ch14-self-tuning-intelligent-control-and-statistical-process-control"},
        "copyright_en": "Original text © IDC Technologies Pty Ltd",
        "copyright_vi": "Bản gốc © IDC Technologies Pty Ltd",
        "lede_en": ("A hands-on training manual covering process dynamics, measurement, valves, "
                    "control modes, PID tuning, feedforward, fuzzy logic and statistical process "
                    "control. The Vietnamese translation proceeds chapter by chapter; figures are "
                    "redrawn as vectors so they stay legible on a phone."),
        "lede_done_en": ("A hands-on training manual covering process dynamics, measurement, valves, "
                         "control modes, PID tuning, feedforward, fuzzy logic and statistical process "
                         "control. The Vietnamese translation is complete — all fourteen chapters — "
                         "and every figure is redrawn as a vector so it stays legible on a phone."),
        "lede_vi": ("Giáo trình thực hành về động học quá trình, đo lường, van, các mode điều khiển, "
                    "tìm điểm PID, theo hướng, lô-gic mờ và điều khiển thống kê quá trình. Bản dịch "
                    "tiếng Việt thực hiện theo từng chương; hình được vẽ lại bằng vector để rõ nét "
                    "trên điện thoại."),
        "lede_done_vi": ("Giáo trình thực hành về động học quá trình, đo lường, van, các mode điều "
                         "khiển, tìm điểm PID, theo hướng, lô-gic mờ và điều khiển thống kê quá "
                         "trình. Bản dịch tiếng Việt đã hoàn tất — đủ mười bốn chương — và toàn bộ "
                         "hình được vẽ lại bằng vector để rõ nét trên điện thoại."),
        "policy_en": ("<b>About this copy.</b> The 35 PDF files are held in the local library "
                      "catalogue and are not republished here. This page is the online contents "
                      "map: what each chapter covers and which chapters already have a Vietnamese "
                      "translation."),
        "policy_done_en": ("<b>About this copy.</b> The 35 PDF files are held in the local library "
                           "catalogue and are not republished here. This page is the online contents "
                           "map: what each chapter covers, with a link to the Vietnamese translation "
                           "of every one of the fourteen chapters."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> 35 tệp PDF được lưu trong thư viện cục bộ và "
                      "không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội "
                      "dung từng chương và những chương nào đã có bản dịch tiếng Việt."),
        "policy_done_vi": ("<b>Cách đọc bản dịch.</b> 35 tệp PDF được lưu trong thư viện cục bộ và "
                           "không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội "
                           "dung từng chương, kèm liên kết tới bản dịch tiếng Việt của cả mười bốn "
                           "chương."),
        "note_en": "Figures follow the original numbering (Ch.1 alone has Figures 1.1–1.12).",
        "note_vi": "Hình ảnh giữ nguyên số hiệu bản gốc (riêng Chương 1 có Hình 1.1–1.12).",
    },

    "bolton": {
        "slug": "control-systems-bolton",
        "title_en": "Control Systems",
        "title_vi": "Hệ thống điều khiển",
        "byline_en": "W. Bolton · Newnes, 2002",
        "byline_vi": "W. Bolton · Newnes, 2002",
        "pages": 184,
        "files": 1,
        "first_en": ("ch01-control-systems",
                     "Control systems"),
        "first_vi": ("ch01-control-systems",
                     "Hệ thống điều khiển"),
        "chapters": {
            1: ("Control systems", "Hệ thống điều khiển"),
            2: ("System models", "Mô hình hệ thống"),
            3: ("System response", "Đáp ứng hệ thống"),
            4: ("System parameters", "Các thông số hệ thống"),
            5: ("Frequency response", "Đáp ứng tần số"),
            6: ("Nyquist diagrams", "Biểu đồ Nyquist"),
            7: ("Controllers", "Bộ điều khiển"),
        },
        "done": {1: "ch01-control-systems", 2: "ch02-system-models", 3: "ch03-system-response", 4: "ch04-system-parameters", 5: "ch05-frequency-response", 6: "ch06-nyquist-diagrams", 7: "ch07-controllers"},
        "copyright_en": "Original text © 2002 W. Bolton, published by Newnes (Elsevier)",
        "copyright_vi": "Bản gốc © 2002 W. Bolton, Nhà xuất bản Newnes (Elsevier)",
        "lede_en": ("An introduction to the basic principles of control engineering and how they are "
                    "used to model system behaviour — written in everyday language with the minimum of "
                    "mathematics. The Vietnamese translation proceeds chapter by chapter; every figure "
                    "is redrawn as a vector so it stays legible on a phone."),
        "lede_done_en": ("An introduction to the basic principles of control engineering and how they are "
                         "used to model system behaviour. The Vietnamese translation is complete — all "
                         "seven chapters — and every figure is redrawn as a vector."),
        "lede_vi": ("Giới thiệu các nguyên lý cơ bản của kỹ thuật điều khiển và cách chúng được dùng để "
                    "mô hình hóa hành vi hệ thống — viết bằng ngôn ngữ đời thường, dùng ít toán học "
                    "nhất có thể. Bản dịch tiếng Việt thực hiện theo từng chương; mọi hình ảnh đều được "
                    "vẽ lại bằng vector để rõ nét trên điện thoại."),
        "lede_done_vi": ("Giới thiệu các nguyên lý cơ bản của kỹ thuật điều khiển và cách chúng được dùng "
                         "để mô hình hóa hành vi hệ thống. Bản dịch tiếng Việt đã hoàn tất — đủ bảy "
                         "chương — và mọi hình ảnh đều được vẽ lại bằng vector."),
        "policy_en": ("<b>About this copy.</b> The single source PDF is held in the local library "
                      "catalogue and is not republished here. This page is the online contents map: what "
                      "each chapter covers and which chapters already have a Vietnamese translation."),
        "policy_done_en": ("<b>About this copy.</b> The single source PDF is held in the local library "
                           "catalogue and is not republished here. This page is the online contents map: "
                           "what each chapter covers, with a link to the Vietnamese translation of every "
                           "chapter."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn duy nhất được lưu trong thư viện cục bộ "
                      "và không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội dung "
                      "từng chương và những chương nào đã có bản dịch tiếng Việt."),
        "policy_done_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn duy nhất được lưu trong thư viện cục "
                           "bộ và không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: "
                           "nội dung từng chương, kèm liên kết tới bản dịch tiếng Việt của mọi chương."),
        "note_en": "Figures follow the original numbering (e.g. Figure 1.1, Figure 4.3).",
        "note_vi": "Hình ảnh giữ nguyên số hiệu bản gốc (ví dụ Hình 1.1, Hình 4.3).",
    },

    "isa51": {
        "slug": "isa-5-1-instrumentation-symbols",
        "title_en": "Instrumentation Symbols and Identification",
        "title_vi": "Ký hiệu và nhận dạng thiết bị đo",
        "byline_en": "ANSI/ISA-5.1-1984 (R1992) · ISA",
        "byline_vi": "ANSI/ISA-5.1-1984 (R1992) · ISA",
        "pages": 72,
        "files": 1,
        "first_en": ("ch01-purpose-and-scope", "Purpose and scope"),
        "first_vi": ("ch01-purpose-and-scope", "Mục đích và phạm vi"),
        "chapters": {
            1: ("Purpose and scope", "Mục đích và phạm vi"),
            2: ("Definitions", "Định nghĩa"),
            3: ("Outline of the identification system", "Khái quát hệ thống nhận dạng"),
            4: ("Table 1 — Identification letters", "Bảng 1 — Chữ cái nhận dạng"),
            5: ("Tables 2 and 3 — Letter combinations and function blocks",
                "Bảng 2 và 3 — Tổ hợp chữ cái và khối chức năng"),
            6: ("Drawings — instrument and function symbols",
                "Bản vẽ — ký hiệu thiết bị và chức năng"),
            7: ("Drawings — worked examples", "Bản vẽ — ví dụ minh họa"),
        },
        "done": {1: "ch01-purpose-and-scope", 2: "ch02-definitions",
                 3: "ch03-identification-system", 4: "ch04-identification-letters",
                 5: "ch05-letter-combinations-function-blocks",
                 6: "ch06-instrument-symbols", 7: "ch07-worked-examples"},
        "copyright_en": ("Original standard © 1984, reaffirmed 1992, "
                         "Instrument Society of America (ANSI/ISA-5.1-1984 R1992)"),
        "copyright_vi": ("Tiêu chuẩn gốc © 1984, tái xác nhận 1992, "
                         "Instrument Society of America (ANSI/ISA-5.1-1984 R1992)"),
        "lede_en": ("The standard that gives process instrumentation its common language: tag numbers, "
                    "identification letters, instrument bubbles, line symbols, valve and actuator "
                    "symbols, and worked P&ID examples. The Vietnamese translation proceeds chapter by "
                    "chapter; every drawing sheet is reproduced as a true vector so it stays sharp on "
                    "a phone."),
        "lede_done_en": ("The standard that gives process instrumentation its common language: tag "
                         "numbers, identification letters, instrument bubbles, line symbols, valve "
                         "and actuator symbols, and worked P&ID examples. The Vietnamese translation "
                         "is complete — all seven chapters and all 41 vector drawing sheets."),
        "lede_vi": ("Tiêu chuẩn tạo nên ngôn ngữ chung cho thiết bị đo trong công nghiệp quá trình: số "
                    "thẻ, chữ cái nhận dạng, vòng tròn ký hiệu thiết bị, ký hiệu đường tín hiệu, ký "
                    "hiệu van và cơ cấu chấp hành, cùng các ví dụ sơ đồ P&ID. Bản dịch tiếng Việt "
                    "thực hiện theo từng chương; mọi tờ ký hiệu đều được tái tạo bằng vector thật để "
                    "rõ nét trên điện thoại."),
        "lede_done_vi": ("Tiêu chuẩn tạo nên ngôn ngữ chung cho thiết bị đo trong công nghiệp quá "
                         "trình: số thẻ, chữ cái nhận dạng, vòng tròn ký hiệu thiết bị, ký hiệu đường "
                         "tín hiệu, ký hiệu van và cơ cấu chấp hành, cùng các ví dụ sơ đồ P&ID. Bản "
                         "dịch tiếng Việt đã hoàn tất — đủ bảy chương và toàn bộ 41 tờ ký hiệu vector."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library catalogue "
                      "and is not republished here. This page is the online contents map: what each "
                      "chapter covers and which chapters already have a Vietnamese translation."),
        "policy_done_en": ("<b>About this copy.</b> The source PDF is held in the local library "
                           "catalogue and is not republished here. This page is the online contents "
                           "map: what each chapter covers, with a link to the Vietnamese translation "
                           "of every chapter."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ và "
                      "không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội dung "
                      "từng chương và những chương nào đã có bản dịch tiếng Việt."),
        "policy_done_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ và "
                           "không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội "
                           "dung từng chương, kèm liên kết tới bản dịch tiếng Việt của mọi chương."),
        "note_en": ("Sheet numbering follows the standard's clauses 5.4 and 6.2–6.12; "
                    "Figure 1 is the tag-number diagram in clause 4.1."),
        "note_vi": ("Số hiệu tờ ký hiệu đi theo các điều 5.4 và 6.2–6.12 của tiêu chuẩn; "
                    "Hình 1 là sơ đồ số thẻ ở điều 4.1."),
    },
    "int": {
        "slug": "working-with-an-integrator-guide",
        "title_en": "Working with a Control Systems Integrator",
        "title_vi": "Làm việc với nhà tích hợp hệ thống điều khiển",
        "byline_en": "Control System Integrators Association · Guide Vol. 1, 2000",
        "byline_vi": "Hiệp hội các nhà tích hợp hệ thống điều khiển · Tập 1, 2000",
        "pages": 69,
        "files": 1,
        "first_en": ("ch01-general", "General — CSIA and the CSI"),
        "first_vi": ("ch01-general", "Khái quát — CSIA và CSI"),
        "chapters": {
            1: ("General — CSIA and the CSI",
                "Khái quát — CSIA và nhà tích hợp hệ thống điều khiển"),
            2: ("Decision analysis tool — the eight steps",
                "Công cụ phân tích quyết định — tám bước"),
            3: ("Performance scoring, levels and the sample table",
                "Chấm điểm hiệu năng, phân cấp và bảng mẫu"),
            4: ("CSIA registration and General Management criteria",
                "Đăng ký CSIA và tiêu chí Quản lý chung"),
            5: ("Human Resources and Project Management criteria",
                "Tiêu chí Nhân sự và Quản lý dự án"),
            6: ("Quality, Financial and Business Development criteria",
                "Tiêu chí Chất lượng, Tài chính và Phát triển kinh doanh"),
            7: ("Technical qualifications, experience, services and risk",
                "Năng lực kỹ thuật, kinh nghiệm, dịch vụ và rủi ro"),
            8: ("Appendix A — Types of integrators and providers",
                "Phụ lục A — Các loại nhà tích hợp và nhà cung cấp"),
            9: ("Appendix B — Kepner-Tregoe decision analysis worksheet",
                "Phụ lục B — Phiếu phân tích quyết định Kepner-Tregoe"),
        },
        "done": {1: "ch01-general", 2: "ch02-decision-analysis-tool",
                 3: "ch03-scoring-and-levels",
                 4: "ch04-registration-and-general-management",
                 5: "ch05-human-and-project-management",
                 6: "ch06-quality-financial-business",
                 7: "ch07-technical", 8: "ch08-integrator-types",
                 9: "ch09-decision-worksheet"},
        "copyright_en": ("Original guide © 2000 Control System Integrators "
                         "Association (CSIA), Volume 1, Rev. 00"),
        "copyright_vi": ("Bản gốc © 2000 Hiệp hội các nhà tích hợp hệ thống điều khiển "
                         "(CSIA), Tập 1, Rev. 00"),
        "lede_en": ("The CSIA's client-side guide to choosing a control systems integrator: "
                    "what a CSI is, a Kepner-Tregoe decision analysis tool, seven families "
                    "of qualification criteria, and a taxonomy of provider types with ten "
                    "service-mix charts. The Vietnamese translation proceeds chapter by "
                    "chapter; every chart and table is redrawn as a vector."),
        "lede_done_en": ("The CSIA's client-side guide to choosing a control systems "
                         "integrator: what a CSI is, a Kepner-Tregoe decision analysis tool, "
                         "seven families of qualification criteria, and a taxonomy of "
                         "provider types. The Vietnamese translation is complete — all nine "
                         "chapters and all 35 vector figures."),
        "lede_vi": ("Hướng dẫn của CSIA dành cho khách hàng khi lựa chọn nhà tích hợp hệ "
                    "thống điều khiển: CSI là gì, công cụ phân tích quyết định Kepner-Tregoe, "
                    "bảy nhóm tiêu chí đánh giá năng lực và hệ thống phân loại nhà cung cấp "
                    "kèm mười biểu đồ cơ cấu dịch vụ. Bản dịch tiếng Việt thực hiện theo "
                    "từng chương; mọi biểu đồ và bảng đều được vẽ lại bằng vector."),
        "lede_done_vi": ("Hướng dẫn của CSIA dành cho khách hàng khi lựa chọn nhà tích hợp "
                         "hệ thống điều khiển: CSI là gì, công cụ phân tích quyết định "
                         "Kepner-Tregoe, bảy nhóm tiêu chí đánh giá và hệ thống phân loại "
                         "nhà cung cấp. Bản dịch tiếng Việt đã hoàn tất — đủ chín chương "
                         "và toàn bộ 35 hình vector."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library "
                      "catalogue and is not republished here. This page is the online contents "
                      "map: what each chapter covers and which chapters already have a "
                      "Vietnamese translation."),
        "policy_done_en": ("<b>About this copy.</b> The source PDF is held in the local "
                           "library catalogue and is not republished here. This page is the "
                           "online contents map: what each chapter covers, with a link to the "
                           "Vietnamese translation of every chapter."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ "
                      "và không được đăng lại tại đây. Trang này là bản đồ mục lục trực "
                      "tuyến: nội dung từng chương và những chương nào đã có bản dịch "
                      "tiếng Việt."),
        "policy_done_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện "
                           "cục bộ và không được đăng lại tại đây. Trang này là bản đồ mục "
                           "lục trực tuyến: nội dung từng chương, kèm liên kết tới bản dịch "
                           "tiếng Việt của mọi chương."),
        "note_en": ("The guide has no numbered figures; the ten Appendix A service-mix "
                    "donut charts and all scoring tables are redrawn as vectors."),
        "note_vi": ("Tập sách không có hình được đánh số; mười biểu đồ cơ cấu dịch vụ ở "
                    "Phụ lục A và toàn bộ bảng chăm điểm đều được vẽ lại bằng vector."),
    },
    "prv": {
        "slug": "pressure-relief-valve-engineering-handbook",
        "title_en": "Pressure Relief Valve Engineering Handbook",
        "title_vi": "Cẩm nang kỹ thuật van xả áp lực",
        "byline_en": "Crosby Valve Inc. · Technical Document TP-V300, 1997",
        "byline_vi": "Crosby Valve Inc. · Tài liệu kỹ thuật TP-V300, 1997",
        "pages": 93,
        "files": 1,
        "first_en": ("ch01-introduction", "Introduction to the Crosby Engineering Handbook"),
        "first_vi": ("ch01-introduction", "Giới thiệu Cẩm nang kỹ thuật Crosby"),
        "chapters": {
            1: ("Introduction to the Crosby Engineering Handbook",
                "Giới thiệu Cẩm nang kỹ thuật Crosby"),
            2: ("Fundamentals of Pressure Relief Valve Design",
                "Nguyên lý cơ bản thiết kế van xả áp"),
            3: ("Terminology",
                "Thuật ngữ"),
            4: ("Codes and Standards — Summary",
                "Tiêu chuẩn và quy code — Tóm tắt"),
            5: ("Valve Sizing and Selection — U.S.C.S. Units",
                "Định cỡ và lựa chọn van — Đơn vị USCS"),
            6: ("Valve Sizing and Selection — Metric Units",
                "Định cỡ và lựa chọn van — Đơn vị hệ mét"),
            7: ("Engineering Support Information",
                "Thông tin hỗ trợ kỹ thuật"),
            8: ("Appendix — ASME Section VIII, Division 1 Excerpts",
                "Phụ lục — Trích dẫn ASME Section VIII, Division 1"),
        },
        "done": {1: "ch01-introduction", 2: "ch02-fundamentals", 3: "ch03-terminology",
                 4: "ch04-codes-standards", 5: "ch05-sizing-uscs"},
        "copyright_en": ("Original handbook © 1997 Crosby Valve Inc. (an FMC Corporation "
                         "subsidiary), Technical Document TP-V300"),
        "copyright_vi": ("Bản gốc © 1997 Crosby Valve Inc. (công ty con của FMC Corporation), "
                         "Tài liệu kỹ thuật TP-V300"),
        "lede_en": ("Crosby's 93-page engineering handbook on pressure relief valves: design "
                    "fundamentals, terminology, the governing codes and standards, USCS and "
                    "metric sizing equations, and a set of engineering-support charts. The "
                    "Vietnamese translation proceeds chapter by chapter; every sizing chart and "
                    "valve diagram is redrawn as a vector."),
        "lede_done_en": ("Crosby's 93-page engineering handbook on pressure relief valves: design "
                         "fundamentals, terminology, the governing codes and standards, USCS and "
                         "metric sizing equations, and a set of engineering-support charts. The "
                         "Vietnamese translation is in progress — completed chapters link to their "
                         "translation."),
        "lede_vi": ("Cẩm nang kỹ thuật 93 trang của Crosby về van xả áp lực: nguyên lý thiết kế, "
                    "thuật ngữ, các tiêu chuẩn và quy code chi phối, phương trình định cỡ theo "
                    "đơn vị USCS và hệ mét, cùng các biểu đồ hỗ trợ kỹ thuật. Bản dịch tiếng Việt "
                    "thực hiện theo từng chương; mọi biểu đồ định cỡ và sơ đồ van đều được vẽ "
                    "lại bằng vector."),
        "lede_done_vi": ("Cẩm nang kỹ thuật 93 trang của Crosby về van xả áp lực: nguyên lý thiết "
                         "kế, thuật ngữ, các tiêu chuẩn chi phối, phương trình định cỡ USCS và hệ "
                         "mét, cùng các biểu đồ hỗ trợ kỹ thuật. Bản dịch tiếng Việt đang thực "
                         "hiện — các chương đã hoàn tất có liên kết tới bản dịch."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library "
                      "catalogue and is not republished here. This page is the online contents "
                      "map: what each chapter covers and which chapters already have a "
                      "Vietnamese translation."),
        "policy_done_en": ("<b>About this copy.</b> The source PDF is held in the local library "
                           "catalogue and is not republished here. This page is the online "
                           "contents map: what each chapter covers, with a link to the "
                           "Vietnamese translation of every completed chapter."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ "
                      "và không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: "
                      "nội dung từng chương và những chương nào đã có bản dịch tiếng Việt."),
        "policy_done_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục "
                           "bộ và không được đăng lại tại đây. Trang này là bản đồ mục lục trực "
                           "tuyến: nội dung từng chương, kèm liên kết tới bản dịch tiếng Việt của "
                           "mọi chương đã hoàn tất."),
        "note_en": ("The source is a scanned-print vendor handbook; valve cutaway diagrams and "
                    "sizing coefficient charts are redrawn as vectors from the rendered pages."),
        "note_vi": ("Nguồn là cẩm nang nhà cung cấp dạng in; các sơ đồ cắt van và biểu đồ hệ "
                    "số định cỡ được vẽ lại bằng vector từ các trang đã render."),
    },
}


def num(n, lang):
    return format(n, ",d").replace(",", "." if lang == "vi" else ",")


def header(lang, switch_href):
    nav = NAV_EN if lang == "en" else NAV_VI
    links = []
    for href, label in nav:
        cls = ' class="active"' if href.endswith("books/") else ""
        links.append('<a href="%s"%s>%s</a>' % (href, cls, esc(label)))
    if lang == "en":
        links.append('<a href="%s" class="lang-switch">VI</a>' % switch_href)
    else:
        links.append('<a href="%s" class="lang-switch">EN</a>' % switch_href)
    brand_home = "/" if lang == "en" else "/?lang=vi"
    return ('<header class="site-header"><a href="%s" class="brand">%s'
            '<span>Pro InstControl</span></a><nav class="site-nav">%s</nav></header>'
            % (brand_home, MARK, "".join(links)))


def head(lang, title, desc):
    return ('<!doctype html><html lang="%s"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><meta name="description" content="%s">'
            '<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,'
            'wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" '
            'rel="stylesheet"><link rel="stylesheet" href="/books/assets/library.css">'
            '</head><body>' % (lang, esc(title), esc(desc)))


def footer(lang, spec):
    txt = (("Thư viện Pro InstControl · Bản dịch không chính thức, dùng cho mục đích học tập · "
            if lang == "vi" else
            "Pro InstControl Library · Unofficial study copy · ")
           + (spec["copyright_vi"] if lang == "vi" else spec["copyright_en"]))
    return '<footer class="site-footer"><p>%s</p></footer></body></html>' % esc(txt)


def done_for(lang, spec):
    """Per-language 'done' map; falls back to the shared 'done' map.

    Used so a chapter can be marked translated in one language (e.g. the
    Vietnamese translation-in-progress) without claiming it exists in the
    other language where the reader page has not been built yet.
    """
    return spec.get("done_%s" % lang) or spec.get("done", {})


def toc(lang, spec):
    out = []
    base = ("/books/read/%s/" if lang == "en" else "/vi/books/read/%s/") % spec["slug"]
    chapters = spec["chapters"]
    done = done_for(lang, spec)
    total = len(chapters)
    ndone = len(done)
    rows = []
    for c in sorted(chapters):
        cen, cvi = chapters[c]
        label = cen if lang == "en" else cvi
        if c in done:
            url = "%s%s/" % (base, done[c])
            rows.append(
                '<li class="done"><span class="n">%d</span>'
                '<span class="t"><a href="%s">%s</a></span>'
                '<span class="st"><a href="%s">%s</a></span></li>'
                % (c, url, esc(label), url,
                   "translated" if lang == "en" else "đã dịch"))
        else:
            rows.append('<li><span class="n">%d</span>'
                        '<span class="t">%s</span><span class="st">%s</span></li>'
                        % (c, esc(label),
                           "pending" if lang == "en" else "chờ dịch"))
    meta = ("%d chapters · %d translated" % (total, ndone)) if lang == "en" \
        else ("%d chương · %d đã dịch" % (total, ndone))
    out.append('<h3>%s</h3>'
               '<div style="font-size:.76rem;letter-spacing:.08em;text-transform:uppercase;'
               'color:#888;margin:-.2rem 0 .2rem;">%s</div>'
               '<ul class="toc-list">%s</ul>'
               % (("Chapters" if lang == "en" else "Các chương"),
                  esc(meta), "".join(rows)))
    # appendices
    if "appendices" in spec:
        arows = []
        for letter, en, vi in spec["appendices"]:
            label = en if lang == "en" else vi
            arows.append('<li><span class="n">%s</span><span class="t">%s</span>'
                         '<span class="st">%s</span></li>'
                         % (esc(letter), esc(label),
                            "pending" if lang == "en" else "chờ dịch"))
        out.append('<h3>%s</h3><ul class="toc-list">%s</ul>'
                   % (("Appendices" if lang == "en" else "Phụ lục"),
                      "".join(arows)))
    return "".join(out)


def build(lang, spec):
    vi = lang == "vi"
    slug = spec["slug"]
    switch = ("/books/read/%s/" if vi else "/vi/books/read/%s/") % slug
    title = spec["title_vi"] if vi else spec["title_en"]
    desc = (spec["lede_vi"] if vi else spec["lede_en"])[0:160]
    crumb = ("<a href=\"/vi/books/\">Sách</a> · Mục lục sách" if vi
             else "<a href=\"/books/\">Books</a> · Book contents")
    byline = spec["byline_vi"] if vi else spec["byline_en"]
    total = len(spec["chapters"])
    ndone = len(done_for(lang, spec))
    meta = ("%s chương · %s trang · %s tệp PDF"
            % (num(total, lang), num(spec["pages"], lang), spec["files"])) if vi \
        else ("%s chapters · %s pages · %s PDF files"
              % (num(total, lang), num(spec["pages"], lang), spec["files"]))
    if ndone >= total:
        flag = ('<span class="translated-flag" data-level="full">🟢 Đã dịch đầy đủ · %d/%d chương</span>'
                % (ndone, total) if vi else
                '<span class="translated-flag" data-level="full">🟢 Fully translated · %d of %d '
                'chapters</span>' % (ndone, total))
    else:
        flag = ('<span class="translated-flag" data-level="progress">🟠 Đang dịch · %d/%d chương</span>'
                % (ndone, total) if vi else
                '<span class="translated-flag" data-level="progress">🟠 Translating · %d of %d '
                'chapters</span>' % (ndone, total))
    # A finished book must not describe itself as still being translated: the
    # lede and the "about this copy" note have a completion variant that wins
    # when every chapter is done.
    sfx = "_done_vi" if vi else "_done_en"
    lede = (spec["lede" + sfx] if ndone >= total and "lede" + sfx in spec
            else spec["lede_vi"] if vi else spec["lede_en"])
    policy = (spec["policy" + sfx] if ndone >= total and "policy" + sfx in spec
              else spec["policy_vi"] if vi else spec["policy_en"])
    read = ("Đọc Chương 1 →" if vi else "Read the Vietnamese Chapter 1 →")
    h2 = "Bản đồ chương" if vi else "Chapter map"
    note2 = spec["note_vi"] if vi else spec["note_en"]
    pct = "%.0f%% hoàn thành" % (100.0 * ndone / total) if vi \
        else "%.0f%% complete" % (100.0 * ndone / total)

    chap_slug, chap_title = (spec["first_vi"] if vi else spec["first_en"])
    chap_href_vi = "/vi/books/read/%s/%s/" % (slug, spec["done"][1])
    chap_href_en = "/books/read/%s/%s/" % (slug, spec["done"][1])

    body = (
        '<main><article class="intranet-content reader">'
        '<div class="reader-hero">'
        '<div class="breadcrumb">%s</div>'
        '<h1>%s</h1>'
        '<p class="byline">%s</p>'
        '<div class="meta-line">%s</div>'
        '</div>'
        '<div class="prose">'
        '%s'
        '<div class="progress-bar"><i style="width:%d%%"></i></div>'
        '<p style="font-size:.78rem;color:#888;letter-spacing:.06em;text-transform:uppercase;'
        'margin:-.8rem 0 1.6rem;">%s</p>'
        '<p class="lead">%s</p>'
        '<div class="note">%s</div>'
        '<p><a href="%s"><strong>%s</strong></a></p>'
        '<h2>%s</h2>'
        '%s'
        '<div class="note">%s</div>'
        '<div class="chapter-nav">'
        '<a href="%s"><span class="k">← %s</span>%s</a>'
        '<a href="%s" style="text-align:right;"><span class="k">%s</span>%s</a>'
        '</div>'
        '</div></article></main>'
        % (crumb, esc(title), esc(byline), esc(meta),
           flag, max(1, round(100.0 * ndone / total)), pct,
           lede, policy,
           (chap_href_vi if vi else chap_href_en), read,
           h2, toc(lang, spec), note2,
           "/vi/books/" if vi else "/books/",
           "Thư viện" if vi else "Library",
           esc("Tất cả sách" if vi else "All books"),
           chap_href_vi if vi else chap_href_en,
           "Chương 1 →" if vi else "Chapter 1 →",
           esc(chap_title))
    )
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang, spec)


def main():
    import sys
    wanted = sys.argv[1:] or list(BOOKS)
    for key in wanted:
        spec = BOOKS[key]
        for lang in ("en", "vi"):
            pair = ("vi/books/read/%s/index.html" if lang == "vi"
                    else "books/read/%s/index.html") % spec["slug"]
            path = os.path.join(ROOT, *pair.split("/"))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            page = build(lang, spec)
            open(path, "w", encoding="utf-8").write(page)
            print("wrote %s  %d kB" % (path, len(page) // 1024))
        # quick checks on the vi page
        page = build("vi", spec)
        print("--- %s checks ---" % key)
        print("toc rows:", page.count('<li class="done"') + page.count('<li><span class="n"'))
        print("done rows:", page.count('class="done"'))
        print("chapters:", len(spec["chapters"]))


if __name__ == "__main__":
    main()
