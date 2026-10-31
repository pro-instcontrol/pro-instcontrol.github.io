"""Add the Control Engineering eBook series to the library catalogue.

Eighteen themed ebooks published by Control Engineering (CFE Media) between
spring 2025 and January 2026. They were harvested from controleng.com/ebooks/,
whose PDFs sit on the publisher's CloudFront bucket rather than behind the
site's Cloudflare gate, so each file downloads directly.

The works land on the "press" shelf (domain "trade") beside Control Magazine,
which is where the rest of the trade press already lives. Each gets its own
catalogue id, so /books/work/<id>/ is stable and gives the reader both a
read-in-browser and a download link.

Run before uploading the PDFs and rebuilding the site:

    python build/add_ebooks.py

Then upload each PDF to the library-pdfs release under the asset name this
script prints, e.g.

    gh release upload library-pdfs "<pdf>" --clobber
"""

import io
import json
import os
import re

from pypdf import PdfReader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "library", "catalog.json")

# the catalogue's declared root; the eBooks live in their own folder under it
EBOOK_DIR = "D:/Process Control and Automation/Control Engineering eBooks"

# (filename, title, pages-order-free description en, description vi)
# Titles carry the publisher and edition so the set reads as a series on the
# shelf while staying searchable by topic.
BOOKS = [
    ("2025_CE_ProcessInstrumentationSensors_eBook_V8.pdf",
     "Process Instrumentation & Sensors — Control Engineering eBook, Spring 2025",
     "Centralised monitoring for plant-wide visibility, sustainability analytics, quantum-sensing "
     "sensitivity, cybersecurity for level measurement, and a practical piece on the deadtime that "
     "hampers process control.",
     "Giám sát tập trung để có tầm nhìn toàn nhà máy, phân tích cho tính bền vững, độ nhạy cảm biến "
     "lượng tử, an ninh mạng cho đo mức, và bài viết thực hành về thời gian trễ (deadtime) cản trở "
     "điều khiển quá trình."),
    ("2025-CE_MechatronicsMotionControl_eBook_V5.pdf",
     "Mechatronics & Motion Control — Control Engineering eBook, Spring 2025",
     "Motor control from energy efficiency to cost, cutting changeover time, exponential gains from "
     "automation and I/O, Cartesian systems in OEM machines, and six trends in robotic picking.",
     "Điều khiển động cơ từ hiệu quả năng lượng đến chi phí, giảm thời gian chuyển đổi sản phẩm, lợi "
     "ích cấp số nhân từ tự động hóa và I/O, hệ Cartesian trong máy của OEM, và sáu xu hướng của robot gắp."),
    ("2025_CE-PE_PLCs_eBook_V18.pdf",
     "PLCs — Control Engineering eBook, Summer 2025",
     "Energy-efficient manufacturing, micro PLCs with IIoT capability, MES strategy, unshackling "
     "industrial data access, systems integration for facility performance, and programming advice "
     "from the Control Engineering webcast.",
     "Sản xuất tiết kiệm năng lượng, PLC mini có khả năng IIoT, chiến lược MES, mở lối truy cập dữ "
     "liệu công nghiệp, tích hợp hệ thống để nâng hiệu suất nhà máy, và lời khuyên lập trình từ "
     "webcast của Control Engineering."),
    ("2025-CE_ControlSystems_eBook_V8.pdf",
     "Control Systems — Control Engineering eBook, Summer 2025",
     "Practical advice for automation programmers, multidimensional arrays in SCADA, signal "
     "conditioning and isolated conditioners, the state of automation in 2025, new SCADA "
     "functionality, and the 100-controller ExxonMobil open process automation insight.",
     "Lời khuyên thực hành cho người lập trình tự động hóa, mảng đa chiều trong SCADA, điều kiện hóa "
     "tín hiệu và bộ điều kiện cách ly, hiện trạng tự động hóa 2025, chức năng SCADA mới, và góc nhìn "
     "về 100 bộ điều khiển trong dự án tự động hóa mở của ExxonMobil."),
    ("2025_CE_MotorsDrives_eBook_V25.pdf",
     "Motors & Drives — Control Engineering eBook, Summer 2025",
     "University robotics design awards, ABB's robotics spin-off, how to choose or troubleshoot a "
     "variable frequency drive, integrator advice from Automate 2025, and the measured benefits of "
     "software in the drive train.",
     "Giải thưởng thiết kế robot sinh viên, việc ABB tách mảng robot, cách chọn và xử lý sự cố biến "
     "tần, lời khuyên từ hệ thống tích hợp tại Automate 2025, và lợi ích đo được của phần mềm trong "
     "chuỗi truyền động."),
    ("2025-CE_OilGasEngineering_eBook_V5.pdf",
     "Oil & Gas Engineering — Control Engineering eBook, Summer 2025",
     "Multi-scale tribology modelling, entrained gas management in Coriolis meters and what it means "
     "for midstream leak risk, over-greasing and grease contamination as causes of failure, robot "
     "safety standards, and industrial networking trends.",
     "Mô hình ma sát học đa thang, quản lý bọt khí trong lưu lượng kế Coriolis và ý nghĩa với rủi ro "
     "rò rỉ đường ống trung nguồn, bôi mỡ quá mức và nhiễm bẩn mỡ như nguyên nhân hỏng hóc, tiêu "
     "chuẩn an toàn robot, và xu hướng mạng công nghiệp."),
    ("2025-CE_SCADA_eBook_V27-3.pdf",
     "SCADA & HMI — Control Engineering eBook, Summer 2025",
     "The largest of the set. What makes an HMI excel on the plant floor, what SCADA is and where it "
     "is going, six Toyota SCADA requirements and how to select KPIs, forty years from DOS to .NET, "
     "and nine modernisation trends.",
     "Dày nhất trong bộ. Điều gì làm một HMI xuất sắc trên sàn nhà máy, SCADA là gì và đang đi đâu, "
     "sáu yêu cầu SCADA của Toyota và cách chọn KPI, bốn mươi năm từ DOS đến .NET, và chín xu hướng "
     "hiện đại hóa."),
    ("2025-CE-PE_AI-MachineLearning_eBook_V16.pdf",
     "AI & Machine Learning — Control Engineering eBook, Summer 2025",
     "The role of AI in connected automation platforms, what to consider before buying an edge "
     "computer, running a local LLM with RAG on an OnLogic Karbon 804, AI video analytics, and using "
     "AI to improve manufacturing operations.",
     "Vai trò của AI trong các nền tảng tự động hóa kết nối, những điều cần cân nhắc trước khi mua "
     "máy tính biên, chạy LLM cục bộ với RAG trên OnLogic Karbon 804, phân tích video bằng AI, và "
     "dùng AI để cải thiện vận hành sản xuất."),
    ("2025-CE_EdgeCloudComputing_eBook_V4.pdf",
     "Edge & Cloud Computing — Control Engineering eBook, Winter 2025",
     "Edge-to-cloud industrial architectures, the hardware blueprint where AI meets the edge, "
     "physical AI and collaborative automation, networking systems that transform the digital "
     "landscape, and industrial PCs for plant-floor compute.",
     "Kiến trúc công nghiệp từ biên đến đám mây, bản thiết kế phần cứng nơi AI gặp biên, AI vật lý và "
     "tự động hóa cộng tác, hệ thống mạng làm thay đổi cục diện số, và IPC cho tính toán tại sàn nhà máy."),
    ("2025-CE_IIoT-Cloud_eBook_V28.pdf",
     "IIoT & Cloud — Control Engineering eBook, Winter 2025",
     "Edge-to-cloud architectures, seven ways SCADA software advances IIoT when done right, the "
     "communications groundwork for modern manufacturing, Shell's software-defined refinery control, "
     "and a roundtable on Industry 4.0.",
     "Kiến trúc từ biên đến đám mây, bảy cách phần mềm SCADA thúc đẩy IIoT nếu làm đúng, nền tảng "
     "truyền thông cho sản xuất hiện đại, điều khiển nhà máy lọc dầu bằng phần mềm định nghĩa của "
     "Shell, và tọa đàm về Công nghiệp 4.0."),
    ("2025-CE_VisionSystems_eBook_V13.pdf",
     "Vision Systems — Control Engineering eBook, Winter 2025",
     "Vision and drone autonomy for inspection and safety, what machine vision is, model training and "
     "compact cameras, open platforms against proprietary vision systems, AI-based perception, and the "
     "Automate 2025 vision standards update.",
     "Thị giác và drone tự hành cho kiểm tra và an toàn, máy thị giác là gì, huấn luyện mô hình và "
     "camera compact, nền tảng mở so với hệ thống độc quyền, nhận thức dựa trên AI, và cập nhật tiêu "
     "chuẩn thị giác tại Automate 2025."),
    ("2025-CE-PE_PainPointsDiscreteManufacturing_eBook_V8.pdf",
     "Pain Points & Solutions in Discrete Manufacturing — Control Engineering eBook, Winter 2025",
     "TSN for machine design performance and precision, quick torque tool integration, bringing AI "
     "into process manufacturing, closing the skills gap with connected technology, and AI-based "
     "condition monitoring for asset management.",
     "TSN cho hiệu năng và độ chính xác khi thiết kế máy, tích hợp dụng cụ siết lực nhanh, đưa AI vào "
     "sản xuất quá trình, thu hẹp khoảng cách kỹ năng bằng công nghệ kết nối, và giám sát tình trạng "
     "dựa trên AI cho quản lý tài sản."),
    ("2025_CE_CybersecuritySmartFactories_eBook_V5.pdf",
     "Cybersecurity in Smart Factories — Control Engineering eBook, Fall 2025",
     "OT and IoT cybersecurity as a marriage of digital factories and security practice, networking "
     "trends, a blueprint for resilient operations, what US manufacturers report, and three "
     "sector-specific considerations for AI and security.",
     "An ninh mạng OT và IoT như sự kết hợp giữa nhà máy số và thực hành bảo mật, xu hướng mạng, bản "
     "thiết kế cho vận hành kiên cường, điều các nhà sản xuất Mỹ báo cáo, và ba cân nhắc theo ngành cho "
     "AI và bảo mật."),
    ("2025-CE-PLE_DigitalTransformation_eBook_V19.pdf",
     "Digital Transformation — Control Engineering eBook, Fall 2025",
     "A practical approach to industrial IoT and device management, virtual commissioning and digital "
     "twins, whether you are ready for a Unified Namespace, resilience in process controls, and "
     "hazards in automated manufacturing systems.",
     "Cách tiếp cận thực dụng với IIoT và quản lý thiết bị, chạy thử ảo và bản sao số, liệu bạn đã sẵn "
     "sàng cho Unified Namespace, tính kiên cường trong điều khiển quá trình, và các mối nguy trong hệ "
     "thống sản xuất tự động."),
    ("2025-CE_Robotics_eBook_V22.pdf",
     "Robotics — Control Engineering eBook, Fall 2025",
     "Maintenance trends a panel of experts expects, repairing automotive paint lines with robots and "
     "machine vision, AI and machine learning in asset management, the 2025 robotics awards, and what "
     "Automate 2025 showed about cobots, AMRs and humanoids.",
     "Xu hướng bảo trì theo nhóm chuyên gia, sửa chữa dây sơn ô tô bằng robot và máy thị giác, AI và "
     "học máy trong quản lý tài sản, giải thưởng robot 2025, và những gì Automate 2025 cho thấy về "
     "cobot, AMR và robot hình người."),
    ("2025_CE_SecuringIIoT_eBook_V4.pdf",
     "Securing the IIoT — Control Engineering eBook, Fall 2025",
     "Why zero trust fails in OT and what to do instead, data diodes against AI-generated threats, "
     "draft software-security guidelines, a physical AI security and safety framework, and the "
     "professional strain on security practitioners.",
     "Vì sao zero trust thất bại trong OT và nên làm gì thay thế, data diode trước các mối đe dọa do "
     "AI tạo ra, dự thảo hướng dẫn an ninh phần mềm, khung an ninh và an toàn cho AI vật lý, và áp lực "
     "nghề nghiệp của người làm bảo mật."),
    ("2025_ICSPulse_CriticalInfrastructure_eBook_V14.pdf",
     "Protecting Critical Infrastructure — Control Engineering eBook, Fall 2025",
     "The Slammer worm at Davis-Besse in 2003, mitigating the Salt Typhoon telecom intrusion, a "
     "year-long utility intrusion found in a new report, AI and security in oil and energy, and why "
     "interdependent infrastructure demands proactive risk management.",
     "Sâu Slammer tại nhà máy hạt nhân Davis-Besse năm 2003, giảm thiểu xâm nhập viễn thông Salt "
     "Typhoon, một vụ xâm nhập kéo dài cả năm trong hệ thống tiện ích, AI và an ninh trong dầu khí - "
     "năng lượng, và vì sao hạ tầng phụ thuộc lẫn nhau đòi hỏi quản trị rủi ro chủ động."),
    ("2026_CE-StateOfAutomation_V2.pdf",
     "2026 State of Industrial Automation — Control Engineering research report",
     "The January 2026 research report: survey results and analysis of where automation spend is "
     "going. Control systems and motors and drives lead, with 54% of respondents investing in each, "
     "broken out for manufacturers, vendors, integrators and policymakers.",
     "Báo cáo nghiên cứu tháng 1/2026: kết quả khảo sát và phân tích dòng tiền đầu tư tự động hóa. Hệ "
     "điều khiển và động cơ - truyền động dẫn đầu, mỗi hạng mục có 54% người trả lời đầu tư, dữ liệu "
     "tách riêng cho nhà sản xuất, nhà cung cấp, tích hợp hệ thống và nhà hoạch định chính sách."),
]


def doc_entry(path, title):
    full = path.replace("/", os.sep)
    pages, head = 0, ""
    try:
        reader = PdfReader(full)
        pages = len(reader.pages)
        head = re.sub(r"\s+", " ", reader.pages[0].extract_text() or "")[:400]
    except Exception as exc:                       # noqa: BLE001 - metadata only
        print("  ! could not read %s: %s" % (os.path.basename(path), exc))
    return {"path": path, "title": title, "pages": pages,
            "bytes": os.path.getsize(full), "copies": [], "head": head}


def main():
    cat = json.load(io.open(CAT, encoding="utf-8"))
    by_title = {w["title"]: w for w in cat["works"]}
    next_id = max(w["id"] for w in cat["works"]) + 1
    added = updated = 0

    for fname, title, en, vi in BOOKS:
        path = "%s/%s" % (EBOOK_DIR, fname)
        if not os.path.exists(path.replace("/", os.sep)):
            print("  ! missing file, skipped: %s" % fname)
            continue
        doc = doc_entry(path, title)
        work = by_title.get(title)
        if work is None:
            work = {"id": next_id, "title": title, "dir": EBOOK_DIR,
                    "domain": "trade", "why": 7, "docs": [], "ndocs": 0,
                    "pages": 0, "bytes": 0, "year": None, "copies": 0, "head": ""}
            next_id += 1
            cat["works"].append(work)
            added += 1
        else:
            updated += 1
        work["docs"] = [doc]
        work["desc"] = {"en": en, "vi": vi}
        work["ndocs"] = 1
        work["pages"] = doc["pages"]
        work["bytes"] = doc["bytes"]
        work["head"] = doc["head"]
        work["year"] = 2026 if "2026" in title else 2025
        print("work %-3d %3dp %s" % (work["id"], work["pages"], title[:62]))

    cat["root"] = "D:/Process Control and Automation"
    cat["totals"]["works"] = len(cat["works"])
    io.open(CAT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cat, ensure_ascii=False, indent=1))
    print("\nadded %d, updated %d — catalogue now has %d works"
          % (added, updated, len(cat["works"])))


if __name__ == "__main__":
    main()
