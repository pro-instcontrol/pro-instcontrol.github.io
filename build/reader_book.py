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
                 4: "ch04-codes-standards", 5: "ch05-sizing-uscs", 6: "ch06-sizing-metric",
                 7: "ch07-engineering-support", 8: "ch08-asme-appendix"},
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
                         "metric sizing equations, engineering-support charts, and the ASME "
                         "Section VIII excerpts. The Vietnamese translation is complete — all "
                         "eight chapters link to their translation."),
        "lede_vi": ("Cẩm nang kỹ thuật 93 trang của Crosby về van xả áp lực: nguyên lý thiết kế, "
                    "thuật ngữ, các tiêu chuẩn và quy code chi phối, phương trình định cỡ theo "
                    "đơn vị USCS và hệ mét, cùng các biểu đồ hỗ trợ kỹ thuật. Bản dịch tiếng Việt "
                    "thực hiện theo từng chương; mọi biểu đồ định cỡ và sơ đồ van đều được vẽ "
                    "lại bằng vector."),
        "lede_done_vi": ("Cẩm nang kỹ thuật 93 trang của Crosby về van xả áp lực: nguyên lý thiết "
                         "kế, thuật ngữ, các tiêu chuẩn chi phối, phương trình định cỡ USCS và hệ "
                         "mét, các biểu đồ hỗ trợ kỹ thuật, cùng phần trích dẫn ASME Section VIII. "
                         "Bản dịch tiếng Việt đã hoàn thành — cả tám chương đều có liên kết tới "
                         "bản dịch."),
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
    # Book 5 — VTT Publications 384 (1999). EN -> VI only. The 129-page thesis
    # splits into 15 numbered chapters plus a references unit (pp. 121-129).
    "isd": {
        "slug": "inherent-safety-in-process-plant-design",
        "title_en": "Inherent Safety in Process Plant Design — An Index-Based Approach",
        "title_vi": "An toàn nội tại trong thiết kế nhà máy quá trình — Phương pháp chỉ số",
        "byline_en": "Anna-Mari Heikkilä · VTT Publications 384, Technical Research Centre of Finland, 1999",
        "byline_vi": "Anna-Mari Heikkilä · VTT Publications 384, Trung tâm Nghiên cứu Kỹ thuật Phần Lan, 1999",
        "pages": 129,
        "files": 1,
        "first_en": ("ch01-introduction", "Introduction"),
        "first_vi": ("ch01-introduction", "Giới thiệu"),
        "chapters": {
            1: ("Introduction", "Giới thiệu"),
            2: ("Safety", "An toàn"),
            3: ("Evaluation of Safety", "Đánh giá an toàn"),
            4: ("Some Safety Analysis Methods for Process Plant Design",
                "Một số phương pháp phân tích an toàn trong thiết kế nhà máy quá trình"),
            5: ("Limitations of Existing Methods in Conceptual Process Design",
                "Hạn chế của các phương pháp hiện có trong thiết kế sơ bộ"),
            6: ("Inherent Safety", "An toàn nội tại"),
            7: ("Factors Representing Inherent Safety in Preliminary Design",
                "Các yếu tố đại diện an toàn nội tại trong thiết kế sơ bộ"),
            8: ("Inherent Safety Index", "Chỉ số an toàn nội tại"),
            9: ("Weighting between Subindices", "Trọng số giữa các chỉ số thành phần"),
            10: ("Subindices of Chemical Inherent Safety Index",
                 "Chỉ số thành phần của an toàn nội tại hóa học"),
            11: ("Subindices for Process Inherent Safety Index",
                 "Chỉ số thành phần của an toàn nội tại quá trình"),
            12: ("Case Study — Acetic Acid Process",
                 "Nghiên cứu tình huống — Quá trình axit axetic"),
            13: ("Case-Based Reasoning for Safety Evaluation",
                 "Suy luận dựa trên tình huống trong đánh giá an toàn"),
            14: ("Index Application in Computerized Process Synthesis",
                 "Ứng dụng chỉ số trong tổng hợp quá trình trên máy tính"),
            15: ("Conclusions", "Kết luận"),
            16: ("References", "Tài liệu tham khảo"),
        },
        "done": {1: "ch01-introduction", 2: "ch02-safety",
                 3: "ch03-evaluation-of-safety",
                 4: "ch04-safety-analysis-methods",
                 5: "ch05-limitations-of-existing-methods",
                 6: "ch06-inherent-safety",
                 7: "ch07-safety-factors",
                 8: "ch08-safety-index",
                 9: "ch09-weighting",
                 10: "ch10-chemical-subindices",
                 11: "ch11-process-subindices",
                 12: "ch12-case-study",
                 13: "ch13-cbr",
                 14: "ch14-synthesis",
                 15: "ch15-conclusions",
                 16: "ch16-references"},
        "copyright_en": ("Original thesis © 1999 Anna-Mari Heikkilä / Technical Research "
                         "Centre of Finland (VTT), VTT Publications 384"),
        "copyright_vi": ("Luận văn gốc © 1999 Anna-Mari Heikkilä / Trung tâm Nghiên cứu Kỹ "
                         "thuật Phần Lan (VTT), VTT Publications 384"),
        "lede_en": ("Anna-Mari Heikkilä's VTT thesis on inherent safety: rather than "
                    "controlling hazards with add-on protective systems, an inherently "
                    "safer plant avoids them by using less hazardous materials and "
                    "operations. The work builds the Inherent Safety Index for conceptual "
                    "chemical process design, splits it into chemical and process "
                    "subindices, evaluates process structure by case-based reasoning, and "
                    "uses the index as a fitness function in genetic optimisation. The "
                    "Vietnamese translation proceeds chapter by chapter; every figure, "
                    "flowsheet and scoring table is redrawn as a vector."),
        "lede_done_en": ("Anna-Mari Heikkilä's VTT thesis on inherent safety and the "
                         "Inherent Safety Index for conceptual chemical process design. "
                         "The Vietnamese translation is complete — all sixteen units "
                         "link to their translation."),
        "lede_vi": ("Luận văn VTT của Anna-Mari Heikkilä về an toàn nội tại: thay vì khống "
                    "chế mối nguy bằng các hệ thống bảo vệ bổ sung, một nhà máy an toàn nội "
                    "tại <i>tránh</i> mối nguy ngay từ khâu dùng hóa chất và thao tác ít nguy "
                    "hiểm hơn. Công trình xây dựng Chỉ số An toàn Nội tại cho thiết kế hóa "
                    "chất sơ bộ, tách thành các chỉ số thành phần hóa học và quá trình, đánh "
                    "giá cấu trúc quá trình bằng suy luận dựa trên tình huống, rồi dùng chỉ "
                    "số làm hàm thích nghi trong tối ưu di truyền. Bản dịch tiếng Việt thực "
                    "hiện theo từng chương; mọi hình vẽ, sơ đồ dòng và bảng chấm điểm đều "
                    "được vẽ lại bằng vector."),
        "lede_done_vi": ("Luận văn VTT của Anna-Mari Heikkilä về an toàn nội tại và Chỉ số "
                         "An toàn Nội tại cho thiết kế quá trình hóa chất sơ bộ. Bản dịch "
                         "tiếng Việt đã hoàn thành — cả mười sáu đơn vị đều có liên kết "
                         "tới bản dịch."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library "
                      "catalogue and is not republished here. This page is the online contents "
                      "map: what each chapter covers and which chapters already have a "
                      "Vietnamese translation."),
        "policy_done_en": ("<b>About this copy.</b> The source PDF is held in the local library "
                           "catalogue and is not republished here. This page is the online "
                           "contents map: what each chapter covers, with a link to the "
                           "Vietnamese translation of every chapter."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ "
                      "và không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: "
                      "nội dung từng chương và những chương nào đã có bản dịch tiếng Việt."),
        "policy_done_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện "
                           "cục bộ và không được đăng lại tại đây. Trang này là bản đồ mục "
                           "lục trực tuyến: nội dung từng chương, kèm liên kết tới bản dịch "
                           "tiếng Việt của mọi chương."),
        "note_en": ("The thesis has 13 numbered figures and 30 scoring tables; both are "
                    "redrawn as vectors from the source text layer, with the original "
                    "index formulas set as equations."),
    },
    # Book 6 — Smith & Zappe, Valve Selection Handbook, 5th ed. (Elsevier 2004).
    # EN -> VI only. 387 book pages split into 21 site units; long chapters
    # (Fundamentals, Manual Valves, PRVs, Rupture Discs) run as parts.
    "vsh": {
        "slug": "valve-selection-handbook",
        "title_en": "Valve Selection Handbook — Engineering Fundamentals for Selecting Manual Valves, Check Valves, Pressure Relief Valves and Rupture Discs",
        "title_vi": "Cẩm nang Lựa chọn Van — Cơ sở kỹ thuật chọn van chặn tay, van một chiều, van an toàn áp suất và đĩa nứt vỡ",
        "byline_en": "Peter Smith & R. W. Zappe · 5th edition, Gulf Professional Publishing / Elsevier, 2004",
        "byline_vi": "Peter Smith & R. W. Zappe · Ấn bản thứ 5, Gulf Professional Publishing / Elsevier, 2004",
        "pages": 387,
        "files": 1,
        "first_en": ("ch01-introduction", "Introduction"),
        "first_vi": ("ch01-introduction", "Giới thiệu"),
        "chapters": {
            1: ("Introduction", "Giới thiệu"),
            2: ("Fundamentals I — Fluid Tightness and Sealing Mechanism",
                "Cơ sở I — Độ kín chất lỏng và cơ chế làm kín"),
            3: ("Fundamentals II — Seatings, Gaskets and Stem Seals",
                "Cơ sở II — Chỗ kín, gioăng đệm và gioăng trục van"),
            4: ("Fundamentals III — Flow Through Valves",
                "Cơ sở III — Dòng chảy qua van"),
            5: ("Manual Valves I — Functions, Selection and Globe Valves",
                "Van tay I — Chức năng, lựa chọn và van toàn cầu"),
            6: ("Manual Valves II — Piston and Parallel Gate Valves",
                "Van tay II — Van pít-tông và van cửa song song"),
            7: ("Manual Valves III — Wedge Gate Valves",
                "Van tay III — Van cửa nêm"),
            8: ("Manual Valves IV — Plug Valves",
                "Van tay IV — Van phích (plug)"),
            9: ("Manual Valves V — Ball Valves",
                "Van tay V — Van bi"),
            10: ("Manual Valves VI — Butterfly and Pinch Valves",
                 "Van tay VI — Van bướm và van kẹp (pinch)"),
            11: ("Manual Valves VII — Diaphragm and Stainless Steel Valves",
                 "Van tay VII — Van màng và van thép không gỉ"),
            12: ("Check Valves", "Van một chiều"),
            13: ("Pressure Relief Valves I — Direct-Loaded",
                 "Van an toàn áp suất I — Tải trực tiếp"),
            14: ("Pressure Relief Valves II — Pilot-Operated and Operational Behavior",
                 "Van an toàn áp suất II — Điều khiển bằng pilot và hành vi vận hành"),
            15: ("Rupture Discs I — Types and Construction",
                 "Đĩa nứt vỡ I — Kiểu loại và kết cấu"),
            16: ("Rupture Discs II — Selection and Applications",
                 "Đĩa nứt vỡ II — Lựa chọn và ứng dụng"),
            17: ("Sizing Pressure Relief Devices",
                 "Định cỡ thiết bị giải áp"),
            18: ("Actuators", "Cơ cấu chấp hành (actuator)"),
            19: ("Double Block and Bleed Ball Valves",
                 "Van bi chặn kép và xả (double block & bleed)"),
            20: ("Mechanical Locking Devices for Valves",
                 "Thiết bị khóa cơ khí cho van"),
            21: ("Appendices — Abbreviations, Standards, SI Units and Glossary",
                 "Phụ lục — Viết tắt, tiêu chuẩn, hệ đơn vị SI và thuật ngữ"),
        },
        "done": {1: "ch01-introduction",
                 2: "ch02-fluid-tightness-and-sealing",
                 3: "ch03-seatings-gaskets-stem-seals",
                 4: "ch04-flow-through-valves",
                 5: "ch05-manual-valves-selection-globe",
                 6: "ch06-piston-parallel-gate-valves",
                 7: "ch07-wedge-gate-valves",
                 8: "ch08-plug-valves",
                 9: "ch09-ball-valves",
                 10: "ch10-butterfly-pinch-valves",
                 11: "ch11-diaphragm-stainless-steel-valves",
                 12: "ch12-check-valves",
                 13: "ch13-prv-direct-loaded",
                 14: "ch14-prv-pilot-operated",
                 15: "ch15-rupture-discs-construction",
                 16: "ch16-rupture-discs-selection",
                 17: "ch17-sizing-pressure-relief-devices",
                 18: "ch18-actuators",
                 19: "ch19-double-block-and-bleed",
                 20: "ch20-mechanical-locking-devices",
                 21: "ch21-appendices"},
        "copyright_en": ("Original book © 2004 Elsevier Inc. (Gulf Professional Publishing), "
                         "ISBN 0-7506-7717-1"),
        "copyright_vi": ("Sách gốc © 2004 Elsevier Inc. (Gulf Professional Publishing), "
                         "ISBN 0-7506-7717-1"),
        "lede_en": ("The standard industry reference on valve selection: how the sealing "
                    "mechanism, flow behaviour (pressure loss, cavitation, waterhammer, "
                    "noise) and closure-member kinematics of each valve family drive the "
                    "choice for a given process service. Covers manual valves (globe, "
                    "gate, plug, ball, butterfly, pinch, diaphragm), check valves, "
                    "pressure relief valves, rupture discs, sizing, actuators, double "
                    "block & bleed, and mechanical locking. The Vietnamese translation "
                    "proceeds unit by unit; every cutaway and chart is redrawn as a "
                    "vector."),
        "lede_vi": ("Tài liệu tham chiếu công nghiệp kinh điển về lựa chọn van: cơ chế "
                    "làm kín, hành vi dòng chảy (tổn thất áp suất, xâm thực, waterhammer, "
                    "tiếng ồn) và động học phần đóng của từng họ van quyết định lựa chọn "
                    "cho một dịch vụ quá trình cụ thể. Bao gồm van tay (cầu, cửa, phích, "
                    "bi, bướm, pinch, màng), van một chiều, van an toàn áp suất, đĩa nứt "
                    "vỡ, định cỡ, cơ cấu chấp hành, chặn kép & xả, và khóa cơ khí. Bản "
                    "dịch tiếng Việt thực hiện theo từng đơn vị; mọi hình cắt và biểu đồ "
                    "đều được vẽ lại bằng vector."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library "
                      "catalogue and is not republished here. This page is the online contents "
                      "map: what each unit covers and which units already have a "
                      "Vietnamese translation."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ "
                      "và không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: "
                      "nội dung từng đơn vị và những đơn vị nào đã có bản dịch tiếng Việt."),
        "note_en": ("The source book carries 243 numbered figures — manufacturer cutaways, "
                    "seat-detail drawings and sizing charts. Each redrawn figure is a "
                    "simplified vector schematic that keeps the topology and labels of "
                    "the original; sizing coefficient charts are re-plotted from their "
                    "tabulated data."),
        "note_vi": ("Sách gốc có 243 hình đánh số — hình cắt của nhà sản xuất, chi tiết "
                    "chỗ kín và biểu đồ định cỡ. Mỗi hình vẽ lại là một sơ đồ vector rút "
                    "gọn giữ nguyên cấu trúc và nhãn của bản gốc; các biểu đồ hệ số định "
                    "cỡ được vẽ lại từ dữ liệu bảng tương ứng."),
    },
    # Book 7 — Hans D. Baumann, *Control Valve Primer: A User's Guide*,
    # 5th ed. (ISA / Wiley, 2011). 204 pp, 32 short chapters, 56 figures.
    "cvp": {
        "slug": "control-valve-primer-baumann",
        "title_en": "Control Valve Primer — A User's Guide, 5th Edition",
        "title_vi": "Sổ tay van điều khiển — Hướng dẫn người dùng, ấn bản 5",
        "byline_en": "Hans D. Baumann · ISA / Wiley, 5th edition, 2011",
        "byline_vi": "Hans D. Baumann · ISA / Wiley, ấn bản 5, 2011",
        "pages": 204,
        "files": 1,
        "first_en": ("ch01-what-is-a-control-valve-and-how-does", "What Is a Control Valve and How Does It Affect My Control Loop?"),
        "first_vi": ("ch01-what-is-a-control-valve-and-how-does", "Van điều khiển là gì và nó ảnh hưởng thế nào đến vòng điều khiển?"),
        "chapters": {
            1: ("What Is a Control Valve and How Does It Affect My Control Loop?",
                "Van điều khiển là gì và nó ảnh hưởng thế nào đến vòng điều khiển?"),
            2: ("Why Not Use a Speed-Controlled Pump?",
                "Tại sao không dùng bơm điều chỉnh tốc độ?"),
            3: ("What Valve Type Shall I Choose?",
                "Nên chọn loại van nào?"),
            4: ("The Self-Acting Regulator: Why Not?",
                "Bộ điều chỉnh tự tác dụng: tại sao không?"),
            5: ("Valve Sizing Made Easy",
                "Định cỡ van dễ dàng"),
            6: ("High-Recovery Valves",
                "Van phục hồi áp suất cao"),
            7: ("Sizing and Selection—Let the Computer Do It All!",
                "Định cỡ và lựa chọn — để máy tính lo hết!"),
            8: ("What About Fail-Safe?",
                "Về an toàn khi mất điện (fail-safe)?"),
            9: ("Why Most People Choose “Equal Percentage” as a Flow Characteristic",
                "Vì sao hầu hết chọn đặc tính lưu lượng “phần trăm bằng nhau”"),
            10: ("Valve Positioners",
                "Bộ định vị van"),
            11: ("The Mystery of Line Pressure-Produced Valve Stem Forces, or Selecting the Correct Actuator Size",
                "Ẩn số lực thân van do áp suất đường ống, hay chọn đúng kích thước cơ cấu chấp hành"),
            12: ("How to Install a Control Valve",
                "Lắp đặt van điều khiển thế nào"),
            13: ("How Good Is the Valve I Purchased?",
                "Van mình mua tốt đến đâu?"),
            14: ("When Do I Need to “Hard Face” the Valve Trim and Other Questions Concerning Valve Material",
                "Khi nào cần “phủ cứng” bộ lót van và các câu hỏi khác về vật liệu van"),
            15: ("Cavitation",
                "Xâm thực"),
            16: ("Concern for the Environment",
                "Quan tâm đến môi trường"),
            17: ("Will My Valve Be Too Noisy?",
                "Van của tôi có quá ồn không?"),
            18: ("The ABC Method for Gases",
                "Phương pháp ABC cho chất khí"),
            19: ("The Graphical ABC Method for Gases",
                "Phương pháp ABC đồ thị cho chất khí"),
            20: ("Methods of Aerodynamic Valve Noise Reduction",
                "Phương pháp giảm tiếng ồn khí động học của van"),
            21: ("The ABC Method for Estimating Hydrodynamic Sound Level",
                "Phương pháp ABC ước tính mức âm thanh thủy động"),
            22: ("Graphical Estimation of Noise Produced by Turbulence and Cavitation of Liquids",
                "Ước tính đồ thị tiếng ồn do nhiễu loạn và xâm thực chất lỏng"),
            23: ("Flashing",
                "Bay hơi nháy (flashing)"),
            24: ("Avoiding Leaky Valve Stem Packing",
                "Tránh rò rỉ bao bình thân van"),
            25: ("Seat Leakage and Seat Materials",
                "Rò rỉ chỗ ngồi và vật liệu chỗ ngồi"),
            26: ("Valves for Sanitary or Aseptic Service",
                "Van cho dịch vụ vệ sinh hoặc vô trùng"),
            27: ("Sixteen Commandments: What You Shall Not Do!",
                "Mười sáu điều răn: những gì không được làm!"),
            28: ("Electric versus Pneumatic Actuators",
                "Cơ cấu chấp hành điện so với khí nén"),
            29: ("Saving Energy",
                "Tiết kiệm năng lượng"),
            30: ("The Bus System to the Rescue, or What the Future May Bring",
                "Hệ thống bus tới giải cứu, hay tương lai sẽ mang lại gì"),
            31: ("Thinking “Green” and Saving Metal",
                "Tư duy “xanh” và tiết kiệm kim loại"),
            32: ("Pipe Vibration Due to Sound",
                "Rung đường ống do âm thanh"),
        },
        "done": {
            1: "ch01-what-is-a-control-valve-and-how-does",
            2: "ch02-why-not-use-a-speed-controlled-pump",
            3: "ch03-what-valve-type-shall-i-choose",
            4: "ch04-the-self-acting-regulator-why-not",
        },
        "copyright_en": "Original work © 2011 Hans D. Baumann, published by ISA / John Wiley & Sons.",
        "copyright_vi": "Bản gốc © 2011 Hans D. Baumann, do ISA / John Wiley & Sons xuất bản.",
        "lede_en": ("Hans Baumann's primer is the ISA classic on control valves: a user-oriented, question-and-answer walk through valve types, sizing, cavitation, noise, actuators, positioners and digital fieldbus control. The fifth edition adds mathematical modelling of cavitation, smart positioners and loop-performance evaluation. The Vietnamese translation proceeds chapter by chapter; every figure is redrawn as a vector."),
        "lede_vi": ("Sổ tay của Hans Baumann là tác phẩm kinh điển của ISA về van điều khiển: cách tiếp cận hỏi–đáp hướng người dùng qua các loại van, định cỡ, xâm thực, tiếng ồn, cơ cấu chấp hành, bộ định vị và điều khiển fieldbus số. Ấn bản thứ năm bổ sung mô hình hóa toán học về xâm thực, bộ định vị thông minh và đánh giá hiệu năng vòng điều khiển. Bản dịch tiếng Việt tiến hành từng chương; mọi hình đều được vẽ lại bằng vector."),
        "lede_done_en": ("All 32 chapters of Baumann's Control Valve Primer are now available in English and Vietnamese, with every figure redrawn as a vector."),
        "lede_done_vi": ("Toàn bộ 32 chương Sổ tay van điều khiển của Baumann đã có bản tiếng Anh và tiếng Việt, với mọi hình được vẽ lại bằng vector."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library catalogue and is not republished here; this is the online contents map with links to the chapters that already have a Vietnamese translation."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ và không được đăng lại tại đây; đây là bản đồ mục lục trực tuyến, với liên kết đến các chương đã có bản dịch tiếng Việt."),
        "note_en": ("The 5th edition carries 56 numbered figures — valve cutaways, sizing charts, flow characteristics, noise and cavitation diagrams. Each is redrawn as a simplified vector schematic keeping the topology and labels of the original."),
        "note_vi": ("Ấn bản thứ năm có 56 hình đánh số — hình cắt van, biểu đồ định cỡ, đặc tính dòng chảy, sơ đồ tiếng ồn và xâm thực. Mỗi hình được vẽ lại thành sơ đồ vector rút gọn, giữ nguyên cấu trúc và nhãn của bản gốc."),
    },
    # Book 7b — Guy Borden Jr. (ed.), Paul G. Friedmann (style ed.), *Control Valves*,
    # ISA Practical Guides for Measurement and Control (1998). The local source is a
    # 12-page scan of Chapter 5 "Control Valve Actuators" (printed pp. 93-103).
    "bcv": {
        "slug": "control-valves-borden-practical-guide",
        "title_en": "Control Valves — Control Valve Actuators (ISA Practical Guides)",
        "title_vi": "Van điều khiển — Cơ cấu chấp hành van (Sổ tay Thực hành ISA)",
        "byline_en": "Guy Borden, Jr., Editor · Paul G. Friedmann, Style Editor · ISA, 1998",
        "byline_vi": "Guy Borden, Jr., biên tập · Paul G. Friedmann, biên tập viên phong cách · ISA, 1998",
        "pages": 12,
        "files": 1,
        "first_en": ("ch05-control-valve-actuators", "Control Valve Actuators"),
        "first_vi": ("ch05-control-valve-actuators", "Cơ cấu chấp hành van điều khiển"),
        "chapters": {
            5: ("Control Valve Actuators", "Cơ cấu chấp hành van điều khiển"),
        },
        "done": {5: "ch05-control-valve-actuators"},
        "copyright_en": "Original chapter © 1998 ISA — Instrumentation, Systems, and Automation Society.",
        "copyright_vi": "Chương gốc © 1998 ISA — Hội Tự động hóa, Đo lường và Điều khiển.",
        "lede_en": ("Chapter 5 of the ISA Practical Guides volume on control valves: how a control valve actuator works, signal and power sources, the principal actuator styles, and the accessories — positioners, limit switches, position transmitters, solenoid valves, air regulators and volume boosters — that turn a valve into a controllable final element."),
        "lede_vi": ("Chương 5 của tập Sổ tay Thực hành ISA về van điều khiển: cơ cấu chấp hành hoạt động thế nào, nguồn tín hiệu và nguồn năng lượng, các kiểu cơ cấu chấp hành chính, và các phụ tùng — bộ định vị, công tắc hành trình, bộ phát tín hiệu vị trí, van điện từ, bộ điều áp và bộ tăng lưu lượng khí — biến một van thành phần tử chấp hành có thể điều khiển được."),
        "lede_done_en": ("The ISA actuator chapter is available in English and Vietnamese."),
        "lede_done_vi": ("Chương về cơ cấu chấp hành của ISA đã có bản tiếng Anh và tiếng Việt."),
        "policy_en": ("<b>About this copy.</b> The local source is a 12-page scan of a single chapter; the original PDF is not republished here."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Nguồn địa phương là bản quét 12 trang của một chương duy nhất; tệp PDF gốc không được đăng lại tại đây."),
        "note_en": ("The source is image-only; the text was transcribed from the scanned pages. Figures are redrawn as vector schematics."),
        "note_vi": ("Nguồn chỉ có hình ảnh; văn bản được chép lại từ các trang quét. Các hình được vẽ lại thành sơ đồ vector."),
    },
    # Book 7c — Emerson, *Control Valve Handbook*, 6th ed. (2020).
    # 355 pp, 15 chapters; the current vendor reference.
    "cvh6": {
        "slug": "control-valve-handbook-emerson-6th",
        "title_en": "Control Valve Handbook — 6th Edition",
        "title_vi": "Sổ tay Van điều khiển — Ấn bản 6",
        "byline_en": "Emerson Flow Controls · 6th edition, 2020",
        "byline_vi": "Emerson Flow Controls · ấn bản 6, 2020",
        "pages": 355,
        "files": 1,
        "first_en": ("ch01-introduction-to-control-valves", "Introduction to Control Valves"),
        "first_vi": ("ch01-introduction-to-control-valves", "Giới thiệu về van điều khiển"),
        "chapters": {
            1: ("Introduction to Control Valves", "Giới thiệu về van điều khiển"),
            2: ("Control Valve Performance", "Hiệu năng van điều khiển"),
            3: ("Valve and Actuator Types", "Các loại van và cơ cấu chấp hành"),
            4: ("Control Valve Accessories", "Phụ tùng van điều khiển"),
            5: ("Control Valve Sizing", "Định cỡ van điều khiển"),
            6: ("Special and Severe Service Control Valves", "Van điều khiển cho dịch vụ đặc biệt và khắc nghiệt"),
            7: ("Steam Conditioning", "Điều hòa hơi"),
            8: ("Installation and Maintenance", "Lắp đặt và bảo trì"),
            9: ("Standards and Approvals", "Tiêu chuẩn và phê duyệt"),
            10: ("Isolation Valves", "Van cô lập"),
            11: ("Sustainability", "Bền vững"),
            12: ("Safety Instrumented Systems", "Hệ thống an toàn bằng thiết bị"),
            13: ("Engineering Data", "Dữ liệu kỹ thuật"),
            14: ("Pipe Data", "Dữ liệu đường ống"),
            15: ("Conversions and Equivalents", "Chuyển đổi và tương đương"),
        },
        "done": {1: "ch01-introduction-to-control-valves",
                 2: "ch02-control-valve-performance",
                 3: "ch03-valve-and-actuator-types",
                 4: "ch04-control-valve-accessories",
                 5: "ch05-control-valve-sizing",
                 6: "ch06-special-severe-service-valves",
                 7: "ch07-steam-conditioning",
                 8: "ch08-installation-and-maintenance",
                 9: "ch09-standards-and-approvals",
                 10: "ch10-isolation-valves",
                 11: "ch11-sustainability",
                 12: "ch12-safety-instrumented-systems",
                 13: "ch13-engineering-data",
                 14: "ch14-pipe-data",
                 15: "ch15-conversions-and-equivalents"},
        "copyright_en": "Original work © 2020 Emerson Flow Controls.",
        "copyright_vi": "Bản gốc © 2020 Emerson Flow Controls.",
        "lede_en": ("The current sixth edition of Emerson’s Control Valve Handbook — the vendor reference covering valve performance and variability, sizing, accessories and digital controllers, severe service, steam conditioning, installation, standards, isolation valves, sustainability and safety instrumented systems."),
        "lede_vi": ("Ấn bản thứ sáu hiện hành của Sổ tay Van điều khiển Emerson — tài liệu tham khảo của nhà sản xuất, trình bày hiệu năng và độ biến thiên của van, định cỡ, phụ tùng và bộ điều khiển số, dịch vụ khắc nghiệt, điều hòa hơi, lắp đặt, tiêu chuẩn, van cô lập, bền vững và hệ thống an toàn bằng thiết bị."),
        "lede_done_en": ("All 15 chapters of the Emerson Control Valve Handbook, 6th edition, are available in English and Vietnamese."),
        "lede_done_vi": ("Toàn bộ 15 chương Sổ tay Van điều khiển Emerson, ấn bản 6, đã có bản tiếng Anh và tiếng Việt."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library catalogue and is not republished here; this is the online contents map with links to chapters that have a Vietnamese translation."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ và không được đăng lại; đây là bản đồ mục lục trực tuyến với liên kết tới các chương đã có bản dịch tiếng Việt."),
        "note_en": ("The handbook carries a large number of illustrated figures — valve cutaways, sizing charts and installation details. Each redrawn figure is a simplified vector schematic keeping the topology and labels of the original."),
        "note_vi": ("Sổ tay có rất nhiều hình minh họa — hình cắt van, biểu đồ định cỡ và chi tiết lắp đặt. Mỗi hình vẽ lại là sơ đồ vector rút gọn giữ nguyên cấu trúc và nhãn của bản gốc."),
    },
    "iih": {
        "slug": "illustrated-handbook-industrial-instrumentation-control",
        "title_en": "Illustrated Handbook of Industrial Instrumentation & Control",
        "title_vi": "Sổ tay minh họa về Thiết bị đo và Điều khiển Công nghiệp",
        "byline_en": "3G E-learning LLC · 2018",
        "byline_vi": "3G E-learning LLC · 2018",
        "pages": 348,
        "files": 1,
        "first_en": ("ch01-measurement-of-temperature", "Measurement of Temperature"),
        "first_vi": ("ch01-measurement-of-temperature", "Đo nhiệt độ"),
        "chapters": {
            1: ("Measurement of Temperature", "Đo nhiệt độ"),
            2: ("Measurement of Pressure", "Đo áp suất"),
            3: ("Measurement of Level", "Đo mức"),
            4: ("pH Measurement", "Đo pH"),
            5: ("Measurement of Flow Rate", "Đo lưu lượng"),
            6: ("Mechanical Flow Meters", "Lưu lượng kế cơ khí"),
            7: ("Gas and Liquid Sampling Techniques in Process Industry",
                "Kỹ thuật lấy mẫu khí và chất lỏng trong công nghiệp"),
            8: ("Control Valves", "Van điều khiển"),
        },
        "done": {1: "ch01-measurement-of-temperature",
                 2: "ch02-measurement-of-pressure",
                 3: "ch03-measurement-of-level",
                 4: "ch04-ph-measurement",
                 5: "ch05-measurement-of-flow-rate",
                 6: "ch06-mechanical-flow-meters"},
        "copyright_en": "Original work © 2018 3G E-learning LLC.",
        "copyright_vi": "Bản gốc © 2018 3G E-learning LLC.",
        "lede_en": ("A 3G E-learning illustrated handbook covering the measurement of temperature, pressure, level, pH and flow, mechanical flow meters, gas and liquid sampling in the process industry, and control valves — an accessible visual companion for instrument technicians."),
        "lede_vi": ("Sổ tay minh họa của 3G E-learning trình bày đo nhiệt độ, áp suất, mức, pH và lưu lượng, lưu lượng kế cơ khí, lấy mẫu khí và chất lỏng trong công nghiệp, và van điều khiển — tài liệu trực quan dễ đọc cho kỹ thuật viên thiết bị đo."),
        "lede_done_en": ("All 8 chapters of the Illustrated Handbook of Industrial Instrumentation & Control are available in English and Vietnamese."),
        "lede_done_vi": ("Toàn bộ 8 chương Sổ tay minh họa về Thiết bị đo và Điều khiển Công nghiệp đã có bản tiếng Anh và tiếng Việt."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library catalogue and is not republished here; this is the online contents map with links to chapters that have a Vietnamese translation."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ và không được đăng lại; đây là bản đồ mục lục trực tuyến với liên kết tới các chương đã có bản dịch tiếng Việt."),
        "note_en": ("The handbook is heavily illustrated with photographs and small schematic figures. Each redrawn figure is a simplified vector keeping the topology and labels of the original."),
        "note_vi": ("Sổ tay có rất nhiều ảnh chụp và sơ đồ nhỏ. Mỗi hình vẽ lại là một vector rút gọn giữ nguyên cấu trúc và nhãn của bản gốc."),
    },
    "ppic": {
        "slug": "handbook-power-plant-instrumentation-control",
        "title_en": "Handbook on Power Plant Instrumentation and Control",
        "title_vi": "Sổ tay Thiết bị đo và Điều khiển Nhà máy Điện",
        "byline_en": "L. N. Jalali (ed.) · Bibliotex, 2019",
        "byline_vi": "L. N. Jalali (biên tập) · Bibliotex, 2019",
        "pages": 308,
        "files": 1,
        "first_en": ("ch01-catalytic-reduction-of-dissolved-oxygen",
                     "The Effect of Different Parameters on the Efficiency of the Catalytic Reduction of Dissolved Oxygen"),
        "first_vi": ("ch01-catalytic-reduction-of-dissolved-oxygen",
                     "Ảnh hưởng của các thông số khác nhau đến hiệu quả khử xúc tác oxy hòa tan"),
        "chapters": {
            1: ("The Effect of Different Parameters on the Efficiency of the Catalytic Reduction of Dissolved Oxygen",
                "Ảnh hưởng của các thông số khác nhau đến hiệu quả khử xúc tác oxy hòa tan"),
            2: ("Advanced Measuring (Instrumentation) Methods for Nuclear Installations: A Review",
                "Phương pháp đo tiên tiến cho các cơ sở hạt nhân: Tổng quan"),
            3: ("Study of Control Strategy of the Converter in Solar Photovoltaic Power System",
                "Nghiên cứu chiến lược điều khiển bộ chuyển đổi trong hệ thống điện mặt trời quang điện"),
            4: ("Nuclear Power Plant Instrumentation Fault Detection Using Fuzzy Logic",
                "Phát hiện lỗi thiết bị đo trong nhà máy điện hạt nhân bằng logic mờ"),
            5: ("Analysis of the Spatial Separation Effects of Thorium/Uranium Fuels in Block-Type HTRs",
                "Phân tích ảnh hưởng của sự phân tách không gian của nhiên liệu thôri/urani trong lò HTR dạng khối"),
            6: ("Developments of Power System Protection and Control",
                "Phát triển bảo vệ và điều khiển hệ thống điện"),
            7: ("Spatial Aspects of Environmental Impact of Power Plants",
                "Khía cạnh không gian của tác động môi trường của nhà máy điện"),
            8: ("Optimization and Damping Performance of a Coal-Fired Power Plant Building Equipped with Multiple Coal Bucket Dampers",
                "Tối ưu hóa và hiệu năng giảm chấn của nhà máy điện than có nhiều bộ giảm chấn phễu than"),
            9: ("Predictive Maintenance Based on Control Charts Applied at Thermoelectric Power Plant",
                "Bảo trì dự đoán dựa trên biểu đồ kiểm soát áp dụng tại nhà máy nhiệt điện"),
            10: ("Models for the Reliability Analysis of Digital Instrumentation and Control Systems for Nuclear Power Plants",
                 "Mô hình phân tích độ tin cậy của hệ thống thiết bị đo và điều khiển số cho nhà máy điện hạt nhân"),
            11: ("Saturated Adaptive Output-Feedback Power-Level Control for Modular High Temperature Gas-Cooled Reactors",
                 "Điều khiển công suất thích ứng bão hòa phản hồi đầu ra cho lò phản ứng làm mát bằng khí nhiệt độ cao dạng module"),
        },
        "done": {1: "ch01-catalytic-reduction-of-dissolved-oxygen"},
        "copyright_en": "Original work © 2019 Bibliotex; individual chapters © their authors, Creative Commons.",
        "copyright_vi": "Bản gốc © 2019 Bibliotex; từng chương © tác giả tương ứng, giấy phép Creative Commons.",
        "lede_en": ("An edited volume on power plant instrumentation and control: dissolved-oxygen reduction, advanced nuclear measurement methods, photovoltaic converters, fuzzy fault detection, thorium/uranium fuels, wide-area protection, environmental impact, coal-plant damping, predictive maintenance, digital I&C reliability and reactor power-level control."),
        "lede_vi": ("Tuyển tập về thiết bị đo và điều khiển nhà máy điện: khử oxy hòa tan, phương pháp đo hạt nhân tiên tiến, bộ chuyển đổi quang điện, phát hiện lỗi logic mờ, nhiên liệu thôri/urani, bảo vệ diện rộng, tác động môi trường, giảm chấn nhà máy than, bảo trì dự đoán, độ tin cậy I&C số và điều khiển công suất lò phản ứng."),
        "lede_done_en": ("All 11 chapters of the Handbook on Power Plant Instrumentation and Control are available in English and Vietnamese."),
        "lede_done_vi": ("Toàn bộ 11 chương Sổ tay Thiết bị đo và Điều khiển Nhà máy Điện đã có bản tiếng Anh và tiếng Việt."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library catalogue and is not republished here; chapters are published under Creative Commons and this is the online contents map with links to chapters that have a Vietnamese translation."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ và không được đăng lại; các chương được xuất bản theo giấy phép Creative Commons, đây là bản đồ mục lục trực tuyến với liên kết tới các chương đã có bản dịch tiếng Việt."),
        "note_en": ("This is an edited research volume: each chapter has its own authors and reference list. Figures are redrawn as simplified vectors retaining source topology and labels."),
        "note_vi": ("Đây là tuyển tập nghiên cứu: mỗi chương có tác giả và danh mục tài liệu tham khảo riêng. Hình vẽ được dựng lại dạng vector rút gọn, giữ nguyên cấu trúc và nhãn của bản gốc."),
    },
    "ipc": {
        "slug": "instrumentation-and-process-control",
        "title_en": "Instrumentation and Process Control",
        "title_vi": "Thiết bị đo và Điều khiển Quá trình",
        "byline_en": "Janardan Prasad · M. N. Jayaswal · Vishnu Priye · I.K. International, 2019",
        "byline_vi": "Janardan Prasad · M. N. Jayaswal · Vishnu Priye · I.K. International, 2019",
        "pages": 403,
        "files": 1,
        "first_en": ("ch01-transducers-i", "Transducers – I"),
        "first_vi": ("ch01-transducers-i", "Bộ chuyển đổi – I"),
        "chapters": {
            1: ("Transducers – I", "Bộ chuyển đổi – I"),
            2: ("Transducers – II", "Bộ chuyển đổi – II"),
            3: ("Transducers – III", "Bộ chuyển đổi – III"),
            4: ("Telemetry", "Đo từ xa"),
            5: ("Signal Conditioning and Data Acquisition System",
                "Xử lý tín hiệu và Hệ thống thu thập dữ liệu"),
            6: ("Process Control", "Điều khiển quá trình"),
            7: ("Display Devices and Recorders", "Thiết bị hiển thị và Máy ghi"),
            8: ("Microprocessor Based Instrumentation System",
                "Hệ thống thiết bị đo dựa trên vi xử lý"),
        },
        "done": {1: "ch01-transducers-i"},
        "copyright_en": "Original work © 2019 I.K. International Pvt. Ltd., New Delhi.",
        "copyright_vi": "Bản gốc © 2019 I.K. International Pvt. Ltd., New Delhi.",
        "lede_en": ("A graduate-level textbook on industrial instrumentation: transducers for pressure, displacement, temperature, flow and level; telemetry; signal conditioning and data acquisition; PID control; recorders; and microprocessor-based instrumentation, PLCs and DCS."),
        "lede_vi": ("Giáo trình bậc đại học về thiết bị đo công nghiệp: bộ chuyển đổi cho áp suất, chuyển vị, nhiệt độ, lưu lượng và mức; đo từ xa; xử lý tín hiệu và thu thập dữ liệu; điều khiển PID; máy ghi; và thiết bị đo vi xử lý, PLC và DCS."),
        "lede_done_en": ("All 8 chapters of Instrumentation and Process Control are available in English and Vietnamese."),
        "lede_done_vi": ("Toàn bộ 8 chương Thiết bị đo và Điều khiển Quá trình đã có bản tiếng Anh và tiếng Việt."),
        "policy_en": ("<b>About this copy.</b> The source PDF is held in the local library catalogue and is not republished here; this is the online contents map with links to chapters that have a Vietnamese translation."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> Tệp PDF nguồn được lưu trong thư viện cục bộ và không được đăng lại; đây là bản đồ mục lục trực tuyến với liên kết tới các chương đã có bản dịch tiếng Việt."),
        "note_en": ("The source PDF stores body text as glyph codes; a decoding pass recovered the prose into `work/ipc_decoded.txt`. Figures are redrawn as simplified vectors retaining source topology and labels."),
        "note_vi": ("Tệp PDF nguồn lưu văn bản dưới dạng mã glyph; một bước giải mã đã khôi phục nội dung sang `work/ipc_decoded.txt`. Hình vẽ được dựng lại dạng vector rút gọn giữ nguyên cấu trúc và nhãn của bản gốc."),
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
    _first_done = spec["done"].get(1, spec["first_en"][0])
    chap_href_vi = "/vi/books/read/%s/%s/" % (slug, _first_done)
    chap_href_en = "/books/read/%s/%s/" % (slug, _first_done)

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
