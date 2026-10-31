# -*- coding: utf-8 -*-
"""Advanced practice — generated EN page at /advanced/ and VI page at /vi/advanced/.

Two real URLs rather than a client-side toggle, matching the video library: the
Vietnamese page is Vietnamese in the HTML, so it is indexable and reads correctly
with JavaScript off. The language switch is therefore a plain link between the
two directories.
"""

import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import framework  # noqa: E402

BASE = "https://pro-instcontrol.github.io"
TWIN_PATHS = {"video-library/", "books/", "advanced/"}
SITE = "Instrumentation &amp; Control"
SITE_VI = "Đo lường &amp; Điều khiển"

T = {
    "en": {
        "title": "Advanced practice — beyond the single loop | I&amp;C",
        "desc": "The layer above single-loop instrumentation: cascade and model predictive control, "
                "safety cases with numbers, the field-connectivity standards being rewritten now, and "
                "the total-plant architecture that claims to run from a diaphragm to a boardroom.",
        "skip": "Skip to content",
        "kicker": "Advanced practice",
        "h1": "Where the fundamentals stop being enough",
        "lede": "Every other page here teaches one loop, one instrument, one drawing. This is the layer "
                "above: strategies that need more than one loop, safety cases that need numbers, the "
                "connectivity standards being rewritten while you read this — and the architecture that "
                "claims to carry one number from a diaphragm in the field to a margin in a boardroom.",
        "toc": "On this page",
        "eb_1": "Standards watch",
        "eb_2": "Control strategy",
        "eb_3": "Safety case",
        "eb_4": "Total plant",
        "lang_other": "VI",
        "lang_href": "../vi/advanced/",
        "nav_active": "advanced/",
        "trends_h": "Trends &amp; standards watch",
        "trends_p": "Twelve videos on where field connectivity is actually heading. The short version: "
                    "Ethernet-APL standardised the wire, not the protocol. HART-IP, PROFINET, EtherNet/IP "
                    "and OPC UA FX now share one two-wire cable to the same devices. FOUNDATION Fieldbus "
                    "did not lose to a rival protocol — it lost to the layer underneath it.",
        "card_k": "Video library · 12 videos",
        "card_t": "Open the Trends &amp; standards watch section",
        "card_d": "Ethernet-APL, HART-IP, OPC UA FX, NOA, MTP, OT security, digital twin",
        "card_arrow": "Go to the videos",
        "video_href": "../video-library/#cat-trends",
        "themes": [
            ("Ethernet-APL",
             "10BASE-T1L over two wires: 10 Mbit/s, 1 km trunk, power on the same pair, Ex zone 0/1/2 "
             "with 2-WISE. It replaces the physical layer, nothing above it."),
            ("HART-IP",
             "The cheapest migration for most plants: the same HART devices and workflows, Ethernet "
             "transport instead of a 4–20 mA loop."),
            ("OPC UA FX",
             "Controller-to-controller exchange with a standard data model. The multi-vendor bench demos "
             "matter more than the specification text."),
            ("NOA and MTP",
             "The second channel for monitoring without touching the control network, and modular skids "
             "that integrate without custom engineering."),
            ("OT security",
             "IEC 62443 has moved from a project afterthought to a procurement gate. Segmentation "
             "vocabulary is now expected of instrument engineers."),
            ("Digital twin",
             "Useful where the model is honest about its steady-state assumptions, and quietly wrong "
             "where it is not."),
        ],
        "beyond_h": "Beyond the single loop",
        "beyond_p": "Cascade, feedforward, ratio and model predictive control: what each one buys, what "
                    "it costs to maintain, and why dead time decides whether any of them can help you. "
                    "The control page carries the full treatment, including tuning methods compared "
                    "and the dead-time problem that dominates everything else.",
        "beyond_a": "Control &amp; tuning — the advanced section",
        "paper_h": "Safety cases and the paper trail",
        "paper_p": "The documents that decide whether a plant is allowed to run: LOPA to justify the "
                   "layer, an SRS to specify it, SIL verification to prove it, a cause &amp; effect "
                   "matrix to wire it, and an alarm rationalisation to keep it usable at three in "
                   "the morning.",
        "paper_a": "Functional safety &amp; SIS",
        "paper_b": "Standards reference",
        "plant_h": "The whole plant, from the diaphragm to the boardroom",
        "plant_p": "Every other section here stops at one loop. The total-plant idea is that a single data "
                   "chain runs from a diaphragm in the field to a margin number in a boardroom, and that "
                   "each layer in that chain is only as good as the layer below it. Emerson sells the shape "
                   "as Plantweb; ABB Ability, Siemens Xcelerator, Honeywell Forge and Yokogawa IA2S sell "
                   "the same layers with different logos. The lineage is worth knowing: Emerson introduced "
                   "PlantWeb in 1997 as “the first field-based digital plant architecture” and relaunched "
                   "it in 2016 as a digital ecosystem. The marketing changed twice; the layer model did not.",
        "plant_p2": "The layers are not a vendor invention. They are the only way the physics works out: a "
                    "measurement is made at the diaphragm, converted to a signal, validated somewhere, "
                    "aggregated into a unit, and only then turned into money. What varies between products "
                    "is where each boundary sits, and what survives crossing it.",
        "stack_hdr": ("Layer", "What lives there", "What it hands upward"),
        "plant_layers": [
            ("L1", "Field devices",
             "Smart transmitters, digital valve controllers, analysers, corrosion and acoustic sensors. "
             "HART, FOUNDATION Fieldbus, PROFIBUS, WirelessHART, Ethernet-APL.",
             "The value — plus the device's own opinion of itself: status, diagnostics, valve signature, "
             "sensor fouling."),
            ("L2", "Control &amp; safety",
             "DeltaV, Ovation, safety PLCs. PID, model predictive control embedded in the controller, "
             "cause &amp; effect.",
             "A validated signal (good / bad / uncertain), a manipulated output, and evidence that the "
             "loop can hold setpoint."),
            ("L3", "Operations",
             "Operator stations, engineering tools, historian, device management, alarm rationalisation.",
             "A human decision, an audit trail, and a work order."),
            ("L4", "Site analytics",
             "Asset-monitoring apps, performance software, a data lake on site or in the cloud — both AWS "
             "and Azure are documented.",
             "Health scores, remaining useful life, exceptions ranked by money at risk."),
            ("L5", "Business",
             "Production accounting, planning, maintenance budget, energy.",
             "Throughput, give-away, unplanned-downtime cost — the numbers a manager can act on."),
        ],
        "note_h": "The arithmetic the top layer inherits",
        "note_p": "Emerson's own 2003 white paper on this architecture is unusually specific about where the "
                  "money is. It defines quality as (product produced − lost and rework) ÷ product produced, "
                  "reports that its variability audits found 80% of control loops underperforming, and cites "
                  "a study projecting more than 7% of cost of goods sold from lifting nine areas of control "
                  "practice to best practice — of which 3.3% comes from the first three, all of them "
                  "loop-level: final control element performance and tuning, unit operation control, and "
                  "advanced regulatory control. The vendor wrote the paper, so read the percentages as an "
                  "existence proof rather than a benchmark. The structure of the argument is what matters: "
                  "the saving is created at the bottom and merely counted at the top.",
        "claim_h": "What the vendor claims, and what it is worth",
        "claim_p": "The marketing literature adds the numbers the white paper leaves out: up to 30% saving in "
                   "installed cost, up to 66% improvement in maintenance productivity, at least 2% "
                   "improvement in overall plant efficiency, 20–30% on specific processes. “Up to” and “at "
                   "least” in the same paragraph is the tell — the ranges are unpriced, unnormalised, and "
                   "drawn from the best installations. Two things in that literature are still worth taking "
                   "seriously. The first is the functional decomposition, which is the same five layers under "
                   "other names: leverage field intelligence, connect the plant, control the process, "
                   "optimise the assets. The second is the concession that “incremental gains can be realised "
                   "by implementing any part of this architecture” but that the greatest benefits need the "
                   "complete solution — which is both the honest engineering statement and the commercial "
                   "model.",
        "break_h": "Three things break between the layers",
        "plant_breaks": [
            ("The quality flag.",
             "The same white paper observes that a DCS-centred architecture assumes “any analog signal "
             "between 4 and 20 mA is good”. If the field layer sends a value without its status, every "
             "layer above inherits an unquantified error. DeltaV and Ovation do consume good / bad / "
             "uncertain — but that flag has to survive all the way into the report, or the report is "
             "fiction."),
            ("The calibration state.",
             "A data lake cannot un-drift a transmitter. A remaining-useful-life estimate inherits whatever "
             "the sensor was doing when the model was trained, including the zero shift nobody has looked "
             "at since the last shutdown."),
            ("The boundary itself.",
             "Every layer boundary is where units, timestamps and quality get dropped. OPC UA and MQTT are "
             "the least-bad answer so far; a scheduled CSV export is where architectures go to die quietly."),
        ],
        "plant_close": "So the test of a total-plant proposal is not how many layers it has, or how good the "
                       "dashboard looks. It is whether a number on the top-level screen can be traced, in one "
                       "step, back to a tag, a range, and the date that instrument was last calibrated. If it "
                       "cannot, you have bought a reporting system, not a control system — and the first time "
                       "it is wrong, nobody will be able to say where.",
        "plant_a1": "The measurement chain",
        "plant_a2": "Advanced control",
        "src_h": "Sources and further reading",
        "sources": [
            ("White paper", "Emerson — Improving quality with PlantWeb digital plant architecture",
             "https://www.emerson.com/documents/automation/product-data-sheet-improving-quality-en-41040.pdf",
             "May 2003. The 80% / 7% / 3.3% figures and the 4–20 mA assumption."),
            ("Video", "PlantWeb for the Power Industry",
             "https://videos.emerson.com/detail/video/3768919387001/",
             "The layers explained against a power plant."),
            ("Architecture",
             "AWS reference architecture — Emerson Plantweb Optics Data Lake for health care and life sciences",
             "https://docs.aws.amazon.com/reference-architecture-diagrams/latest/emerson-plantweb-optics-data-lake-hcls/emerson-plantweb-optics-data-lake-hcls.html",
             "How the cloud tier is actually wired: Kinesis, IoT Core, S3, SageMaker."),
            ("Trade press", "Pulp &amp; Paper Canada — Emerson launches Plantweb digital ecosystem",
             "https://www.pulpandpapercanada.com/emerson-launches-plantweb-digital-ecosystem-1100000427/",
             "October 2016. Peter Zornio on the 1997 origin."),
            ("Article",
             "Process Industry Forum — Digital plant architecture and the power of predictive intelligence",
             "https://www.processindustryforum.com/article/digital-plant-architecture-power-predictive-intelligence-improve-plant-performance",
             "The installed-cost and maintenance-productivity claims."),
        ],
        "foot_note": "A bilingual field guide to process instrumentation and control. "
                     "Content is synthesised from ISA, IEC, API and ISO 18674 practice; "
                     "always verify against the current edition of a standard before design use.",
        "foot_built": "Static site · no build step · EN / VI",
    },
    "vi": {
        "title": "Thực hành nâng cao — vượt ra ngoài một vòng | I&amp;C",
        "desc": "Tầng phía trên của đo lường điều khiển một vòng: điều khiển cascade và dự báo mô hình, "
                "hồ sơ an toàn có con số, các tiêu chuẩn kết nối hiện trường đang được viết lại, và kiến "
                "trúc toàn nhà máy vốn nhận chở một con số từ màng đo đến phòng họp.",
        "skip": "Chuyển đến nội dung",
        "kicker": "Thực hành nâng cao",
        "h1": "Nơi kiến thức cơ bản không còn đủ",
        "lede": "Mọi trang khác ở đây dạy một vòng điều khiển, một thiết bị, một bản vẽ. Đây là tầng "
                "phía trên: những chiến lược cần nhiều hơn một vòng, hồ sơ an toàn cần con số, những "
                "tiêu chuẩn kết nối đang được viết lại ngay lúc này — và kiến trúc vốn nhận chở một con "
                "số từ màng đo ngoài hiện trường đến biên lợi nhuận trong phòng họp.",
        "toc": "Trong trang này",
        "eb_1": "Theo dõi tiêu chuẩn",
        "eb_2": "Chiến lược điều khiển",
        "eb_3": "Hồ sơ an toàn",
        "eb_4": "Toàn nhà máy",
        "lang_other": "EN",
        "lang_href": "../../advanced/",
        "nav_active": "advanced/",
        "trends_h": "Xu hướng &amp; theo dõi tiêu chuẩn",
        "trends_p": "Mười hai video về hướng phát triển thực sự của kết nối hiện trường. Bản ngắn: "
                    "Ethernet-APL chuẩn hoá đường dây, không chuẩn hoá giao thức. HART-IP, PROFINET, "
                    "EtherNet/IP và OPC UA FX nay dùng chung một đôi dây tới cùng thiết bị. "
                    "FOUNDATION Fieldbus không thua một giao thức đối thủ — nó thua tầng bên dưới.",
        "card_k": "Thư viện video · 12 video",
        "card_t": "Mở mục Xu hướng &amp; theo dõi tiêu chuẩn",
        "card_d": "Ethernet-APL, HART-IP, OPC UA FX, NOA, MTP, an ninh OT, digital twin",
        "card_arrow": "Đến phần video",
        "video_href": "../../vi/video-library/#cat-trends",
        "themes": [
            ("Ethernet-APL",
             "10BASE-T1L trên hai dây: 10 Mbit/s, trục dài 1 km, cấp nguồn cùng đôi dây, vùng Ex 0/1/2 "
             "với 2-WISE. Nó thay lớp vật lý, không thay gì ở phía trên."),
            ("HART-IP",
             "Đường chuyển đổi rẻ nhất với phần lớn nhà máy: vẫn thiết bị và quy trình HART cũ, "
             "chỉ đổi sang đường truyền Ethernet thay vì vòng 4–20 mA."),
            ("OPC UA FX",
             "Trao đổi controller-với-controller theo mô hình dữ liệu chuẩn. Các demo đa hãng trên "
             "bàn thử có sức nặng hơn phần chữ của đặc tả."),
            ("NOA và MTP",
             "Kênh thứ hai để giám sát mà không đụng mạng điều khiển, và các skid mô-đun tích hợp "
             "được mà không cần lập trình riêng."),
            ("An ninh OT",
             "IEC 62443 đã từ việc làm sau cùng thành điều kiện mua sắm. Vốn từ về phân vùng nay "
             "được coi là chuẩn mực của kỹ sư đo lường."),
            ("Digital twin",
             "Hữu ích khi mô hình trung thực về giả thiết trạng thái ổn định, và âm thầm sai ở chỗ nó "
             "không trung thực."),
        ],
        "beyond_h": "Vượt ra ngoài một vòng",
        "beyond_p": "Cascade, feedforward, điều khiển tỉ lệ và điều khiển dự báo mô hình: mỗi thứ mua "
                    "được gì, tốn gì để duy trì, và vì sao thời gian trễ quyết định chúng có giúp được "
                    "hay không. Trang điều khiển trình bày đầy đủ, gồm so sánh các phương pháp hiệu "
                    "chỉnh và bài toán thời gian trễ chi phối mọi thứ còn lại.",
        "beyond_a": "Điều khiển &amp; hiệu chỉnh — phần nâng cao",
        "paper_h": "Hồ sơ an toàn và giấy tờ",
        "paper_p": "Những tài liệu quyết định nhà máy có được phép chạy hay không: LOPA để biện minh "
                   "cho lớp bảo vệ, SRS để đặc tả, kiểm chứng SIL để chứng minh, ma trận nguyên nhân "
                   "&amp; kết quả để đấu dây, và rà soát báo động để hệ thống còn dùng được lúc ba "
                   "giờ sáng.",
        "paper_a": "An toàn chức năng &amp; SIS",
        "paper_b": "Tham chiếu tiêu chuẩn",
        "plant_h": "Toàn nhà máy, từ màng đo đến phòng họp",
        "plant_p": "Mọi mục khác ở đây dừng lại ở một vòng điều khiển. Ý tưởng toàn nhà máy là: một chuỗi "
                   "dữ liệu duy nhất chạy từ màng đo ngoài hiện trường đến con số biên lợi nhuận trong "
                   "phòng họp, và mỗi tầng trong chuỗi ấy chỉ tốt bằng tầng bên dưới nó. Emerson bán mô "
                   "hình này dưới tên Plantweb; ABB Ability, Siemens Xcelerator, Honeywell Forge và "
                   "Yokogawa IA2S bán đúng những tầng ấy với logo khác. Lịch sử cũng đáng biết: Emerson "
                   "ra mắt PlantWeb năm 1997 như “kiến trúc nhà máy số dựa trên hiện trường” đầu tiên, "
                   "rồi giới thiệu lại năm 2016 thành hệ sinh thái số. Tiếp thị đổi hai lần; mô hình tầng "
                   "thì không.",
        "plant_p2": "Các tầng này không phải phát minh của một hãng. Đó là cách duy nhất để vật lý khớp "
                    "lại: phép đo được thực hiện tại màng, đổi thành tín hiệu, được kiểm chứng ở đâu đó, "
                    "gộp thành một đơn vị công nghệ, rồi mới thành tiền. Khác nhau giữa các sản phẩm là "
                    "ranh giới từng tầng nằm ở đâu, và cái gì sống sót khi đi qua ranh giới đó.",
        "stack_hdr": ("Tầng", "Có gì ở đó", "Chuyển lên trên cái gì"),
        "plant_layers": [
            ("L1", "Thiết bị hiện trường",
             "Bộ truyền thông minh, bộ điều khiển van số, máy phân tích, cảm biến ăn mòn và âm thanh. "
             "HART, FOUNDATION Fieldbus, PROFIBUS, WirelessHART, Ethernet-APL.",
             "Giá trị đo — cộng với ý kiến của chính thiết bị về nó: trạng thái, chẩn đoán, chữ ký van, "
             "màng bám bẩn."),
            ("L2", "Điều khiển &amp; an toàn",
             "DeltaV, Ovation, PLC an toàn. PID, điều khiển dự báo mô hình nhúng trong controller, ma "
             "trận nguyên nhân &amp; kết quả.",
             "Tín hiệu đã kiểm chứng (tốt / hỏng / không chắc), đầu ra điều khiển, và bằng chứng vòng đo "
             "giữ được giá trị đặt."),
            ("L3", "Vận hành",
             "Trạm vận hành, công cụ kỹ thuật, historian, quản lý thiết bị, rà soát báo động.",
             "Quyết định của con người, dấu vết kiểm toán, và một phiếu công việc."),
            ("L4", "Phân tích tại nhà máy",
             "Ứng dụng giám sát tài sản, phần mềm hiệu năng, data lake tại chỗ hoặc trên cloud — cả AWS "
             "và Azure đều có tài liệu.",
             "Điểm sức khỏe tài sản, tuổi thọ còn lại, ngoại lệ xếp theo số tiền gặp rủi ro."),
            ("L5", "Kinh doanh",
             "Kế toán sản lượng, kế hoạch, ngân sách bảo trì, năng lượng.",
             "Sản lượng, lượng hàng cho không, chi phí dừng máy ngoài kế hoạch — con số người quản lý "
             "hành động được."),
        ],
        "note_h": "Phép tính mà tầng trên cùng thừa hưởng",
        "note_p": "Bản white paper năm 2003 của chính Emerson về kiến trúc này cụ thể một cách bất thường "
                  "về chỗ tiền nằm ở đâu. Nó định nghĩa chất lượng là (sản phẩm làm ra − hàng mất và làm "
                  "lại) ÷ sản phẩm làm ra, cho biết các cuộc kiểm toán biến động của hãng thấy 80% vòng "
                  "điều khiển chạy dưới mức, và dẫn một nghiên cứu dự báo tiết kiệm hơn 7% giá vốn hàng "
                  "bán khi đưa chín lĩnh vực thực hành điều khiển lên mức tốt nhất — trong đó 3,3% đến từ "
                  "ba lĩnh vực đầu, tất cả đều ở cấp vòng: hiệu năng và hiệu chỉnh phần tử chấp hành cuối, "
                  "điều khiển đơn vị công nghệ, và điều khiển điều chỉnh nâng cao. Người viết bài là hãng "
                  "bán giải pháp, nên hãy đọc các phần trăm ấy như bằng chứng tồn tại, không phải chuẩn so "
                  "sánh. Cấu trúc lập luận mới là điều đáng giữ: tiền được tạo ra ở dưới cùng và chỉ được "
                  "đếm ở trên cùng.",
        "claim_h": "Hãng nói gì, và những con số ấy đáng bao nhiêu",
        "claim_p": "Tài liệu tiếp thị thêm vào những con số mà white paper để trống: tiết kiệm tới 30% chi "
                   "phí lắp đặt, tới 66% năng suất của nhân viên bảo trì, ít nhất 2% hiệu suất toàn nhà "
                   "máy, 20–30% trên từng quá trình cụ thể. “Tới” và “ít nhất” nằm trong cùng một đoạn là "
                   "dấu hiệu cần chú ý — các khoảng ấy không nêu giá, không chuẩn hoá, và lấy từ những nhà "
                   "máy tốt nhất. Hai điều trong tài liệu đó vẫn đáng coi trọng. Thứ nhất là cách chia theo "
                   "chức năng, cũng chính là năm tầng ấy dưới tên khác: khai thác trí tuệ hiện trường, kết "
                   "nối nhà máy, điều khiển quá trình, tối ưu tài sản. Thứ hai là chỗ hãng thừa nhận “lợi "
                   "ích tăng thêm có thể đạt được khi triển khai bất kỳ phần nào của kiến trúc này”, nhưng "
                   "lợi ích lớn nhất cần giải pháp trọn vẹn — vừa là phát biểu kỹ thuật trung thực, vừa là "
                   "mô hình kinh doanh.",
        "break_h": "Ba thứ đứt giữa các tầng",
        "plant_breaks": [
            ("Cờ chất lượng.",
             "Chính bài white paper ấy nhận xét rằng kiến trúc lấy DCS làm trung tâm coi “mọi tín hiệu "
             "tương tự trong khoảng 4–20 mA là tốt”. Nếu tầng hiện trường gửi lên một giá trị mà không "
             "kèm trạng thái, mọi tầng phía trên thừa hưởng một sai số không định lượng được. DeltaV và "
             "Ovation có đọc cờ tốt / hỏng / không chắc — nhưng cờ đó phải sống sót đến tận báo cáo, nếu "
             "không báo cáo chỉ là hư cấu."),
            ("Trạng thái hiệu chuẩn.",
             "Data lake không khử trôi được một bộ truyền. Ước lượng tuổi thọ còn lại thừa hưởng đúng "
             "những gì cảm biến đang làm lúc mô hình được huấn luyện, kể cả độ lệch điểm không mà không ai "
             "ngó tới từ lần dừng máy trước."),
            ("Bản thân ranh giới.",
             "Mỗi ranh giới tầng là nơi đơn vị đo, dấu thời gian và chất lượng dữ liệu bị đánh rơi. OPC UA "
             "và MQTT là câu trả lời ít tệ nhất hiện nay; một file CSV xuất theo lịch là nơi kiến trúc chết "
             "một cách lặng lẽ."),
        ],
        "plant_close": "Vậy phép thử với một đề xuất toàn nhà máy không phải là nó có bao nhiêu tầng, hay "
                       "bảng điều khiển trông đẹp đến đâu. Mà là: một con số trên màn hình cấp cao nhất có "
                       "truy nguyên được, trong một bước, về một tag, một dải đo, và ngày thiết bị ấy được "
                       "hiệu chuẩn gần nhất hay không. Nếu không, bạn đã mua một hệ thống báo cáo, không "
                       "phải một hệ thống điều khiển — và lần đầu tiên nó sai, sẽ không ai nói được sai ở đâu.",
        "plant_a1": "Chuỗi đo lường",
        "plant_a2": "Điều khiển nâng cao",
        "src_h": "Nguồn và đọc thêm",
        "sources": [
            ("White paper", "Emerson — Improving quality with PlantWeb digital plant architecture",
             "https://www.emerson.com/documents/automation/product-data-sheet-improving-quality-en-41040.pdf",
             "Tháng 5/2003. Các con số 80% / 7% / 3,3% và giả thiết 4–20 mA."),
            ("Video", "PlantWeb for the Power Industry",
             "https://videos.emerson.com/detail/video/3768919387001/",
             "Năm tầng được giải thích trên một nhà máy điện."),
            ("Kiến trúc",
             "AWS reference architecture — Emerson Plantweb Optics Data Lake cho y tế và khoa học đời sống",
             "https://docs.aws.amazon.com/reference-architecture-diagrams/latest/emerson-plantweb-optics-data-lake-hcls/emerson-plantweb-optics-data-lake-hcls.html",
             "Tầng cloud được đấu thật sự thế nào: Kinesis, IoT Core, S3, SageMaker."),
            ("Báo ngành", "Pulp &amp; Paper Canada — Emerson launches Plantweb digital ecosystem",
             "https://www.pulpandpapercanada.com/emerson-launches-plantweb-digital-ecosystem-1100000427/",
             "Tháng 10/2016. Peter Zornio nói về nguồn gốc 1997."),
            ("Bài báo",
             "Process Industry Forum — Digital plant architecture and the power of predictive intelligence",
             "https://www.processindustryforum.com/article/digital-plant-architecture-power-predictive-intelligence-improve-plant-performance",
             "Các tuyên bố về chi phí lắp đặt và năng suất bảo trì."),
        ],
        "foot_note": "Sổ tay song ngữ về thiết bị đo và điều khiển quá trình. "
                     "Nội dung được tổng hợp từ thực tiễn ISA, IEC, API và ISO 18674; "
                     "luôn đối chiếu với bản tiêu chuẩn hiện hành trước khi dùng cho thiết kế.",
        "foot_built": "Trang tĩnh · không cần build · EN / VI",
    },
}


def page_url(lang):
    return BASE + ("/vi/advanced/" if lang == "vi" else "/advanced/")


def head(lang, prefix):
    t = T[lang]
    css = prefix + "assets/style.css?v=%s" % framework.ASSET_VER
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": page_url(lang) + "#page",
                "url": page_url(lang),
                "name": html.unescape(t["title"]),
                "description": html.unescape(t["desc"]),
                "inLanguage": "vi-VN" if lang == "vi" else "en",
                "isPartOf": {"@type": "WebSite", "name": "Instrumentation & Control",
                             "url": BASE + "/"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Instrumentation & Control",
                     "item": BASE + "/"},
                    {"@type": "ListItem", "position": 2,
                     "name": "Advanced practice" if lang == "en" else "Thực hành nâng cao",
                     "item": page_url(lang)},
                ],
            },
        ],
    }
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canon)s">
<link rel="alternate" hreflang="en" href="%(base)s/advanced/">
<link rel="alternate" hreflang="vi" href="%(base)s/vi/advanced/">
<link rel="alternate" hreflang="x-default" href="%(base)s/advanced/">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Instrumentation &amp; Control">
<meta property="og:locale" content="%(locale)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="%(prefix)sassets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%(css)s">
<script type="application/ld+json">%(ld)s</script>
</head>
<body>
<a class="skip" href="#main">%(skip)s</a>
""" % {
        "lang": "vi" if lang == "vi" else "en",
        "title": t["title"],
        "desc": html.escape(html.unescape(t["desc"]), quote=True),
        "canon": page_url(lang),
        "base": BASE,
        "locale": "vi_VN" if lang == "vi" else "en_US",
        "prefix": prefix,
        "css": css,
        "ld": json.dumps(ld, ensure_ascii=False, separators=(",", ":")),
        "skip": t["skip"],
    }


def topbar(lang, prefix):
    t = T[lang]
    active = t["nav_active"]
    items = []
    for href, en, vi in framework.NAV:
        label = en if lang == "en" else vi
        cls = "nav-link active" if href == active else "nav-link"
        base = prefix + ("vi/" if lang == "vi" and href in TWIN_PATHS else "")
        items.append('<a class="%s" href="%s%s">%s</a>' % (cls, base, href, label))
    nav_html = "\n      ".join(items)
    brand = SITE if lang == "en" else SITE_VI
    tag = "Field Guide" if lang == "en" else "Sổ tay hiện trường"
    return """<header class="topbar">
  <div class="wrap bar">
    <a class="brand" href="%(prefix)sindex.html" aria-label="Home">
      <span class="mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="30" height="30" fill="none">
          <rect x="1" y="1" width="30" height="30" rx="8" stroke="currentColor" stroke-width="1.5" opacity=".35"/>
          <path d="M7 22h6l3-12 3 12h6" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
          <circle cx="16" cy="10" r="2.2" fill="currentColor"/>
        </svg>
      </span>
      <span class="brand-txt"><strong>%(brand)s</strong><em>%(tag)s</em></span>
    </a>
    <nav class="nav" id="nav">
      %(nav)s
    </nav>
    <div class="bar-right">
      <a class="lang" href="%(other)s" aria-label="Switch language">
        <span class="lang-opt on">%(cur)s</span><span class="lang-sep">/</span><span class="lang-opt">%(oth)s</span>
      </a>
      <button class="burger" id="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav">
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>
<main id="main">
""" % {
        "prefix": prefix,
        "brand": brand,
        "tag": tag,
        "nav": nav_html,
        "other": t["lang_href"],
        "cur": "EN" if lang == "en" else "VI",
        "oth": t["lang_other"],
    }


def hero(lang):
    t = T[lang]
    return """<section class="sec adv-hero">
  <div class="wrap">
    <div class="eyebrow"><span class="num">00</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h1 class="adv-h1">%s</h1>
    <p class="lede adv-lede">%s</p>
  </div>
</section>
""" % (t["kicker"], t["h1"], t["lede"])


def trends(lang, prefix):
    t = T[lang]
    items = "".join(
        '<li><b>%s</b><span>%s</span></li>' % (html.escape(k), d) for k, d in t["themes"]
    )
    return """<section class="sec adv-sec" id="trends">
  <div class="wrap">
    <div class="eyebrow"><span class="num">01</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <a class="adv-card" href="%s">
      <span class="adv-card-k">%s</span>
      <span class="adv-card-t">%s</span>
      <span class="adv-card-d">%s</span>
      <span class="adv-card-go">%s <span aria-hidden="true">&rarr;</span></span>
    </a>
    <ul class="adv-themes">%s</ul>
  </div>
</section>
""" % (t["eb_1"], t["trends_h"], t["trends_p"], t["video_href"],
       t["card_k"], t["card_t"], t["card_d"], t["card_arrow"], items)


def beyond(lang, prefix):
    t = T[lang]
    return """<section class="sec adv-sec" id="beyond">
  <div class="wrap">
    <div class="eyebrow"><span class="num">02</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <p class="adv-link"><a href="%scontrol.html#advanced">%s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % (t["eb_2"], t["beyond_h"], t["beyond_p"], prefix, t["beyond_a"])


def paper(lang, prefix):
    t = T[lang]
    return """<section class="sec adv-sec" id="paper">
  <div class="wrap">
    <div class="eyebrow"><span class="num">03</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <p class="adv-link"><a href="%ssafety.html">%s <span aria-hidden="true">&rarr;</span></a>
      <a href="%sstandards.html">%s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % (t["eb_3"], t["paper_h"], t["paper_p"], prefix, t["paper_a"], prefix, t["paper_b"])


def plant(lang, prefix):
    t = T[lang]
    hdr = "".join("<span>%s</span>" % h for h in t["stack_hdr"])
    rows = "".join(
        '<li><span class="adv-stack-l">%s</span>'
        '<span class="adv-stack-b"><b>%s</b><span>%s</span></span>'
        '<span class="adv-stack-a">%s</span></li>' % (lvl, name, desc, adds)
        for lvl, name, desc, adds in t["plant_layers"]
    )
    breaks = "".join("<li><b>%s</b> %s</li>" % (h, p) for h, p in t["plant_breaks"])
    srcs = "".join(
        '<li><span class="tag">%s</span><a href="%s" rel="noopener">%s</a> — %s</li>'
        % (tag, href, label, note)
        for tag, label, href, note in t["sources"]
    )
    return """<section class="sec adv-sec" id="plant">
  <div class="wrap">
    <div class="eyebrow"><span class="num">04</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p)s</p>
    <p class="adv-p">%(p2)s</p>
    <ol class="adv-stack">
      <li class="adv-stack-h">%(hdr)s</li>
      %(rows)s
    </ol>
    <div class="adv-note">
      <b>%(note_h)s</b>
      <p>%(note_p)s</p>
    </div>
    <h3 class="adv-h3">%(claim_h)s</h3>
    <p class="adv-p">%(claim_p)s</p>
    <h3 class="adv-h3">%(break_h)s</h3>
    <ul class="adv-list">%(breaks)s</ul>
    <p class="adv-p adv-close">%(close)s</p>
    <p class="adv-link"><a href="%(prefix)sfundamentals.html">%(a1)s <span aria-hidden="true">&rarr;</span></a>
      <a href="%(prefix)scontrol.html#advanced">%(a2)s <span aria-hidden="true">&rarr;</span></a></p>
    <h3 class="adv-h3">%(src_h)s</h3>
    <ul class="adv-src">%(srcs)s</ul>
  </div>
</section>
""" % {
        "eb": t["eb_4"],
        "h": t["plant_h"],
        "p": t["plant_p"],
        "p2": t["plant_p2"],
        "hdr": hdr,
        "rows": rows,
        "note_h": t["note_h"],
        "note_p": t["note_p"],
        "claim_h": t["claim_h"],
        "claim_p": t["claim_p"],
        "break_h": t["break_h"],
        "breaks": breaks,
        "close": t["plant_close"],
        "prefix": prefix,
        "a1": t["plant_a1"],
        "a2": t["plant_a2"],
        "src_h": t["src_h"],
        "srcs": srcs,
    }


def footer(lang, prefix):
    t = T[lang]
    brand = SITE if lang == "en" else SITE_VI
    return """</main>
<footer class="foot">
  <div class="wrap foot-in">
    <div class="foot-l">
      <span class="brand-mini">%s</span>
      <p>%s</p>
    </div>
    <div class="foot-r">
      <span class="mono">%s</span>
      <a class="mono" href="https://github.com/pro-instcontrol" rel="noopener">github.com/pro-instcontrol</a>
    </div>
  </div>
</footer>
<script>
(function(){var b=document.getElementById("burger");if(!b)return;
b.addEventListener("click",function(){var o=document.body.classList.toggle("menu-open");
b.setAttribute("aria-expanded",o?"true":"false");});})();
</script>
</body>
</html>
""" % (brand, t["foot_note"], t["foot_built"])


def build_lang(lang, path, prefix):
    body = head(lang, prefix)
    body += topbar(lang, prefix)
    body += hero(lang)
    body += trends(lang, prefix)
    body += beyond(lang, prefix)
    body += paper(lang, prefix)
    body += plant(lang, prefix)
    body += footer(lang, prefix)
    framework.write(path, framework.tidy(body))
    return path


def main():
    a = build_lang("en", os.path.join("advanced", "index.html"), "../")
    b = build_lang("vi", os.path.join("vi", "advanced", "index.html"), "../../")
    print("  %-28s advanced page (en)" % a)
    print("  %-28s advanced page (vi)" % b)


if __name__ == "__main__":
    main()
