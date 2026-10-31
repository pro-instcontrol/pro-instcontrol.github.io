# -*- coding: utf-8 -*-
"""The monthly most-read lists Control Engineering publishes as "hot topics".

Each entry is one monthly post: a ranked top-10 by Google Analytics pageviews,
harvested from the archived copies on controleng.com (the live site is behind
Cloudflare, so the Wayback snapshots are the source of record). Titles and
blurbs are the publisher's; the Vietnamese is a translation, and the short
"angle" line under each month heading is this site's own reading, not theirs.

Window: October 2025 to September 2026 — the twelve months before the build.
March to July 2026 have no archived list; Control Engineering rolls some months
together (its August post covers June and July), and the October and November
2025 captures are incomplete. Those gaps are stated on the page rather than
papered over.

PRESS is the second publisher, and deliberately not the same kind of thing:
Automation.com Monthly, harvested from its public issue pages. There is no rank
there to reproduce — an issue is what an editor commissioned — so the section
says so instead of implying an order. InTech, the ISA magazine, is not a source:
it ended with its October 2024 issue, and the ISA terms forbid feeding its
material to a model.
"""

MONTHS = [
    {
        "slug": "september-2026",
        "en": "September 2026",
        "vi": "Tháng 9/2026",
        "angle_en": "The clearest month of the year: an open-standard PLC story at "
                    "number one, PID gap control at four, and two of the top ten are "
                    "Engineering Leaders profiles.",
        "angle_vi": "Tháng rõ ràng nhất trong năm: một bài về tiêu chuẩn mở cho PLC đứng "
                    "đầu, điều khiển khoảng PID ở vị trí thứ tư, và hai trong mười bài là "
                    "chân dung Engineering Leaders.",
        "src": "https://www.controleng.com/control-engineering-hot-topics-september-2026/",
        "items": [
            {"n": 1,
             "t_en": "Understand IEC 61131-10 to more easily transfer PLC applications",
             "t_vi": "Hiểu IEC 61131-10 để chuyển ứng dụng PLC dễ dàng hơn",
             "b_en": "As automation systems evolve and become increasingly complex, IEC 61131-10 "
                     "represents an important step toward a more flexible and open automation "
                     "ecosystem, allowing organizations to leverage existing engineering knowledge "
                     "while adapting to evolving technology requirements.",
             "b_vi": "Khi hệ tự động hóa ngày càng phức tạp, IEC 61131-10 là một bước quan trọng "
                     "hướng tới hệ sinh thái tự động hóa mở và linh hoạt hơn, cho phép tổ chức tận "
                     "dụng kiến thức kỹ thuật sẵn có trong khi vẫn thích ứng với yêu cầu công nghệ "
                     "đang thay đổi.",
             "href": "https://www.controleng.com/understand-iec-61131-10-to-more-easily-transfer-plc-applications/"},
            {"n": 2,
             "t_en": "Research: How industrial AI is impacting the plant floor",
             "t_vi": "Nghiên cứu: AI công nghiệp đang tác động thế nào đến sàn nhà máy",
             "b_en": "New Control Engineering research shows that while implementation is ramping "
                     "up, engineers remain cautious, prioritizing proven use cases like predictive "
                     "maintenance over the AI hype cycle.",
             "b_vi": "Nghiên cứu mới của Control Engineering cho thấy dù việc triển khai đang tăng "
                     "nhanh, kỹ sư vẫn thận trọng, ưu tiên những ca dùng đã được chứng minh như bảo "
                     "trì dự báo hơn là cơn sốt AI.",
             "href": "https://www.controleng.com/research-how-industrial-ai-is-impacting-the-plant-floor/"},
            {"n": 3,
             "t_en": "Engineering Leaders Under 40: The Class of 2026",
             "t_vi": "Engineering Leaders Under 40: Lớp 2026",
             "b_en": "Meet the 35 rising professionals whose expertise is helping solve problems, "
                     "strengthen operations and develop the industry's next generation of talent.",
             "b_vi": "Gặp gỡ 35 chuyên gia trẻ đang giúp giải quyết vấn đề, củng cố vận hành và "
                     "phát triển thế hệ nhân lực kế tiếp của ngành.",
             "href": "https://www.controleng.com/engineering-leaders-under-40-the-class-of-2026/"},
            {"n": 4,
             "t_en": "PID spotlight, part 31: What is PID gap control?",
             "t_vi": "PID spotlight, phần 31: Điều khiển khoảng PID là gì?",
             "b_en": "How do you make a PID controller ignore small deviations while still "
                     "responding to large deviations? What is a gap algorithm? Which algorithms "
                     "work with which systems?",
             "b_vi": "Làm sao để bộ điều khiển PID bỏ qua các sai lệch nhỏ mà vẫn đáp ứng với sai "
                     "lệch lớn? Thuật toán khoảng là gì? Thuật toán nào hợp với hệ nào?",
             "href": "https://www.controleng.com/pid-spotlight-part-31-what-is-pid-gap-control/"},
            {"n": 5,
             "t_en": "Using AI and autonomous control to unlock financial value from energy data",
             "t_vi": "Dùng AI và điều khiển tự hành để khai thác giá trị tài chính từ dữ liệu năng lượng",
             "b_en": "By combining energy management, contextualized data, AI analytics and "
                     "autonomous control, manufacturers can turn energy from an overhead cost into "
                     "a lever for operational and financial performance.",
             "b_vi": "Kết hợp quản lý năng lượng, dữ liệu có ngữ cảnh, phân tích AI và điều khiển tự "
                     "hành, nhà sản xuất có thể biến năng lượng từ chi phí cố định thành đòn bẩy cho "
                     "hiệu quả vận hành và tài chính.",
             "href": "https://www.controleng.com/using-ai-and-autonomous-control-to-unlock-financial-value-from-energy-data/"},
            {"n": 6,
             "t_en": "Can robots do general manufacturing tasks? Toyota Research Institute asks",
             "t_vi": "Robot có làm được việc sản xuất phổ thông? Toyota Research Institute đặt câu hỏi",
             "b_en": "How much data do industrial robots need to learn to respond to variable "
                     "challenges without specific, traditional programming for each?",
             "b_vi": "Robot công nghiệp cần bao nhiêu dữ liệu để học cách đáp ứng các thách thức "
                     "thay đổi mà không phải lập trình riêng cho từng việc?",
             "href": "https://www.controleng.com/can-robots-do-general-manufacturing-tasks-toyota-research-institute-asks/"},
            {"n": 7,
             "t_en": "2026 Engineering Leader Under 40: Joshua Jagnanan, 37",
             "t_vi": "Engineering Leader Under 40 2026: Joshua Jagnanan, 37 tuổi",
             "b_en": "As product manager for low-voltage adjustable-speed drives at Toshiba "
                     "International Corporation, Joshua combines technical depth, operational "
                     "leadership and customer focus to drive engineering and business results. He "
                     "leads a team of associate product managers and application engineers, "
                     "strengthening execution through training, onboarding, dashboards, standard "
                     "operating procedures and quoting-quality improvements.",
             "b_vi": "Là quản lý sản phẩm mảng biến tần hạ áp tại Toshiba International Corporation, "
                     "Joshua kết hợp chiều sâu kỹ thuật, năng lực lãnh đạo vận hành và sự tập trung "
                     "vào khách hàng để thúc đẩy kết quả kỹ thuật và kinh doanh. Anh dẫn dắt một "
                     "nhóm quản lý sản phẩm và kỹ sư ứng dụng, củng cố việc thực thi qua đào tạo, "
                     "hội nhập, bảng điều khiển, quy trình chuẩn và cải thiện chất lượng báo giá.",
             "href": "https://www.controleng.com/2026-engineering-leader-under-40-joshua-jagnanan-37/"},
            {"n": 8,
             "t_en": "2026 Engineering Leader Under 40: Chandradhar Prasad, 38",
             "t_vi": "Engineering Leader Under 40 2026: Chandradhar Prasad, 38 tuổi",
             "b_en": "Within less than a year of joining NIKO Engineering as principal engineer, "
                     "Chandra has delivered complex, high-impact engineering at the intersection of "
                     "power systems, control automation and energy innovation. Leading the MK20 "
                     "geothermal reinjection pumping station upgrade \u2014 a technically demanding "
                     "project involving new variable-frequency drive (VFD) design and integration, "
                     "custom interface board design, cascading PID control systems and unmanned "
                     "automation \u2014 demonstrates his technical depth and versatility.",
             "b_vi": "Chưa đầy một năm sau khi gia nhập NIKO Engineering với vai trò kỹ sư chính, "
                     "Chandra đã thực hiện những công việc kỹ thuật phức tạp và có tác động lớn ở "
                     "giao điểm của hệ thống điện, tự động hóa điều khiển và đổi mới năng lượng. Việc "
                     "dẫn dắt nâng cấp trạm bơm tái phun địa nhiệt MK20 \u2014 một dự án đòi hỏi thiết kế "
                     "và tích hợp biến tần mới, thiết kế bo mạch giao tiếp riêng, hệ điều khiển PID "
                     "tầng bậc và tự động hóa không người \u2014 cho thấy chiều sâu kỹ thuật và sự đa "
                     "năng của anh.",
             "href": "https://www.controleng.com/2026-engineering-leader-under-40-chandradhar-prasad-38/"},
            {"n": 9,
             "t_en": "Beyond 10% yield: Rebuild drug discovery as a controlled process",
             "t_vi": "Vượt mốc hiệu suất 10%: Xây lại việc tìm thuốc như một quá trình được điều khiển",
             "b_en": "About 9 of 10 drug candidates that enter clinical trials are not approved, "
                     "wasting time and investment. Advanced organoids and organ-on-chip systems "
                     "offer more realistic models of human tissues, metabolism and disease. Learn "
                     "what automated manufacturing is teaching drug discovery.",
             "b_vi": "Khoảng 9 trong 10 ứng viên thuốc vào thử nghiệm lâm sàng không được phê duyệt, "
                     "lãng phí thời gian và đầu tư. Organoid tiên tiến và hệ lab-on-chip cho mô hình "
                     "mô người, chuyển hóa và bệnh thực tế hơn. Xem sản xuất tự động hóa đang dạy gì "
                     "cho việc tìm thuốc.",
             "href": "https://www.controleng.com/beyond-10-yield-rebuild-drug-discovery-as-a-controlled-process/"},
            {"n": 10,
             "t_en": "Why you need to let go of these five simulation myths",
             "t_vi": "Vì sao cần bỏ năm lầm tưởng về mô phỏng",
             "b_en": "As automation amplifies the consequences of even small changes, simulation "
                     "provides a zero-risk environment to understand cause and effect "
                     "relationships, and to eliminate surprises before they impact safety or "
                     "production.",
             "b_vi": "Khi tự động hóa khuếch đại hậu quả của cả những thay đổi nhỏ, mô phỏng mang "
                     "lại môi trường không rủi ro để hiểu quan hệ nhân quả và loại bỏ bất ngờ trước "
                     "khi chúng ảnh hưởng đến an toàn hay sản xuất.",
             "href": "https://www.controleng.com/why-you-need-to-let-go-of-these-five-simulation-myths/"},
        ],
    },
    {
        "slug": "august-2026",
        "en": "August 2026",
        "vi": "Tháng 8/2026",
        "angle_en": "A month of overlap: four of these ten also appear in September's list, "
                    "which is what a most-read list looks like when an article keeps being read.",
        "angle_vi": "Một tháng chồng lấn: bốn trong mười bài này cũng xuất hiện trong danh sách "
                    "tháng 9, đúng như dáng vẻ của một bảng xếp hạng khi một bài cứ tiếp tục được đọc.",
        "src": "https://www.controleng.com/control-engineering-hot-topics-august-2026/",
        "items": [
            {"n": 1,
             "t_en": "Why you need to let go of these five simulation myths",
             "t_vi": "Vì sao cần bỏ năm lầm tưởng về mô phỏng",
             "b_en": "As automation amplifies the consequences of even small changes, simulation "
                     "provides a zero-risk environment to understand cause and effect "
                     "relationships, and to eliminate surprises before they impact safety or "
                     "production.",
             "b_vi": "Khi tự động hóa khuếch đại hậu quả của cả những thay đổi nhỏ, mô phỏng mang "
                     "lại môi trường không rủi ro để hiểu quan hệ nhân quả và loại bỏ bất ngờ trước "
                     "khi chúng ảnh hưởng đến an toàn hay sản xuất.",
             "href": "https://www.controleng.com/why-you-need-to-let-go-of-these-five-simulation-myths"},
            {"n": 2,
             "t_en": "Control Engineering hot topics: June 2026",
             "t_vi": "Control Engineering hot topics: Tháng 6/2026",
             "b_en": "From the 2026 Salary Survey results to AI-enabled autonomous systems, explore "
                     "June and July's most-read stories on Control Engineering.",
             "b_vi": "Từ kết quả Khảo sát Lương 2026 đến các hệ tự hành có AI, xem những bài được đọc "
                     "nhiều nhất tháng 6 và 7 trên Control Engineering.",
             "href": "https://www.controleng.com/control-engineering-hot-topics-june-2026"},
            {"n": 3,
             "t_en": "New hubs and added floor space set up next-wave output",
             "t_vi": "Trung tâm mới và diện tích bổ sung chuẩn bị cho làn sóng sản xuất kế tiếp",
             "b_en": "Endress+Hauser said the projects add testing, staging, repair and calibration "
                     "capacity while reducing off-site storage across U.S. partner campuses.",
             "b_vi": "Endress+Hauser cho biết các dự án bổ sung năng lực thử nghiệm, trung chuyển, "
                     "sửa chữa và hiệu chuẩn, đồng thời giảm lưu kho ngoài tại các cơ sở đối tác ở Mỹ.",
             "href": "https://www.controleng.com/new-hubs-and-added-floor-space-set-up-next-wave-output"},
            {"n": 4,
             "t_en": "Deciphering pump curves: How to size control valves",
             "t_vi": "Giải mã đường đặc tính bơm: Cách chọn cỡ van điều khiển",
             "b_en": "Control valve sizing data can often be estimated without direct measurement "
                     "of pressure or flow.",
             "b_vi": "Dữ liệu chọn cỡ van điều khiển thường có thể ước lượng mà không cần đo trực "
                     "tiếp áp suất hay lưu lượng.",
             "href": "https://www.controleng.com/deciphering-pump-curves-how-to-size-control-valves"},
            {"n": 5,
             "t_en": "Eight ways machine vision and AI are improving automotive manufacturing",
             "t_vi": "Tám cách thị giác máy và AI đang cải thiện sản xuất ô tô",
             "b_en": "Industrial artificial intelligence helps machine vision provide more effective "
                     "vehicle inspection systems in eight ways including higher quality, more "
                     "effective automation and easier commissioning.",
             "b_vi": "AI công nghiệp giúp thị giác máy mang lại hệ thống kiểm tra xe hiệu quả hơn "
                     "theo tám cách, gồm chất lượng cao hơn, tự động hóa hiệu quả hơn và chạy thử "
                     "dễ hơn.",
             "href": "https://www.controleng.com/eight-ways-machine-vision-and-ai-are-improving-automotive-manufacturing"},
            {"n": 6,
             "t_en": "More answers about how to integrate new HMI or SCADA with existing automation",
             "t_vi": "Thêm giải đáp về tích hợp HMI hoặc SCADA mới với hệ tự động hóa hiện hữu",
             "b_en": "Get even more answers from the instructors of the Aug. 13 RCEP Control "
                     "Engineering webcast, \u201cHow to integrate new HMI or SCADA with existing "
                     "automation,\u201d archived for a year.",
             "b_vi": "Xem thêm giải đáp từ giảng viên khóa webcast RCEP ngày 13/8 của Control "
                     "Engineering, \u201cCách tích hợp HMI hoặc SCADA mới với hệ tự động hóa hiện "
                     "hữu\u201d, được lưu trữ một năm.",
             "href": "https://www.controleng.com/more-answers-about-how-to-integrate-new-hmi-or-scada-with-existing-automation"},
            {"n": 7,
             "t_en": "PID spotlight, part 30: How to shape PID controller response for integrating processes",
             "t_vi": "PID spotlight, phần 30: Định hình đáp ứng PID cho quá trình tích phân",
             "b_en": "When you change your level controller setpoint the response upsets your "
                     "process. What is the best technique to shape the response to your needs?",
             "b_vi": "Khi bạn đổi điểm đặt của bộ điều khiển mức, đáp ứng làm xáo trộn quá trình. "
                     "Kỹ thuật nào tốt nhất để định hình đáp ứng theo nhu cầu?",
             "href": "https://www.controleng.com/pid-spotlight-part-30-how-to-shape-pid-controller-response-integrating-processes"},
            {"n": 8,
             "t_en": "Five fast answers on digital transformation for controls, instrumentation",
             "t_vi": "Năm câu trả lời nhanh về chuyển đổi số cho điều khiển và thiết bị đo",
             "b_en": "It's not just digital versus analog instrumentation and controls. Digital "
                     "transformation means better connections among engineering, operations and "
                     "maintenance teams, unlocking the technical debt trapped in older automation "
                     "systems.",
             "b_vi": "Không chỉ là thiết bị đo và điều khiển số so với tương tự. Chuyển đổi số nghĩa "
                     "là kết nối tốt hơn giữa kỹ thuật, vận hành và bảo trì, gỡ món nợ kỹ thuật mắc "
                     "kẹt trong hệ tự động hóa cũ.",
             "href": "https://www.controleng.com/five-fast-answers-on-digital-transformation-for-controls-instrumentation"},
            {"n": 9,
             "t_en": "PID spotlight, part 31: What is PID gap control?",
             "t_vi": "PID spotlight, phần 31: Điều khiển khoảng PID là gì?",
             "b_en": "How do you make a PID controller ignore small deviations while still "
                     "responding to large deviations? What is a gap algorithm? Which algorithms "
                     "work with which systems?",
             "b_vi": "Làm sao để bộ điều khiển PID bỏ qua các sai lệch nhỏ mà vẫn đáp ứng với sai "
                     "lệch lớn? Thuật toán khoảng là gì? Thuật toán nào hợp với hệ nào?",
             "href": "https://www.controleng.com/pid-spotlight-part-31-what-is-pid-gap-control"},
            {"n": 10,
             "t_en": "Research: How industrial AI is impacting the plant floor",
             "t_vi": "Nghiên cứu: AI công nghiệp đang tác động thế nào đến sàn nhà máy",
             "b_en": "New Control Engineering research shows that while implementation is ramping "
                     "up, engineers remain cautious, prioritizing proven use cases like predictive "
                     "maintenance over the AI hype cycle.",
             "b_vi": "Nghiên cứu mới của Control Engineering cho thấy dù việc triển khai đang tăng "
                     "nhanh, kỹ sư vẫn thận trọng, ưu tiên những ca dùng đã được chứng minh như bảo "
                     "trì dự báo hơn là cơn sốt AI.",
             "href": "https://www.controleng.com/research-how-industrial-ai-is-impacting-the-plant-floor"},
        ],
    },
    {
        "slug": "february-2026",
        "en": "February 2026",
        "vi": "Tháng 2/2026",
        "angle_en": "The most varied month: three podcast episodes, a research retrospective "
                    "and a C++ piece for machine controllers. The annual 2025 roundup appears "
                    "here as an article in its own right.",
        "angle_vi": "Tháng đa dạng nhất: ba tập podcast, một bài nhìn lại nghiên cứu và một bài "
                    "về C++ cho bộ điều khiển máy. Bản tổng kết năm 2025 xuất hiện ở đây như một "
                    "bài viết độc lập.",
        "src": "https://www.controleng.com/control-engineering-hot-topics-february-2026/",
        "items": [
            {"n": 1,
             "t_en": "How to use C++, datasets for motion control programming",
             "t_vi": "Dùng C++ và dataset cho lập trình điều khiển chuyển động",
             "b_en": "As machine controllers take on more responsibility beyond traditional control "
                     "tasks, systems are expected to handle motion control, data processing and "
                     "decisions in one platform. How can control architectures enable advanced "
                     "functionality on the controller? How does integrated programming help "
                     "real-time performance and system design?",
             "b_vi": "Khi bộ điều khiển máy đảm nhận nhiều việc hơn ngoài điều khiển truyền thống, hệ "
                     "thống được kỳ vọng xử lý điều khiển chuyển động, xử lý dữ liệu và ra quyết định "
                     "trên một nền tảng. Kiến trúc điều khiển có thể bật chức năng nâng cao trên bộ "
                     "điều khiển thế nào? Lập trình tích hợp giúp gì cho hiệu năng thời gian thực và "
                     "thiết kế hệ thống?",
             "href": "https://www.controleng.com/how-to-use-c-datasets-for-motion-control-programming/"},
            {"n": 2,
             "t_en": "Ctrl+Alt+Mfg Ep. 9: When cyberattacks go physical, with Ian Bramson of Black &amp; Veatch",
             "t_vi": "Ctrl+Alt+Mfg tập 9: Khi tấn công mạng trở thành tấn công vật lý, với Ian Bramson (Black &amp; Veatch)",
             "b_en": "Why clean builds, supply-chain visibility, AI-driven defense and a "
                     "back-to-basics approach are becoming essential for securing industrial "
                     "operations.",
             "b_vi": "Vì sao xây dựng sạch, minh bạch chuỗi cung ứng, phòng thủ bằng AI và quay về "
                     "cơ bản đang trở nên thiết yếu để bảo vệ vận hành công nghiệp.",
             "href": "https://www.controleng.com/podcast/ctrlaltmfg-ep-9-when-cyberattacks-go-physical-with-ian-bramson-of-black-veatch/"},
            {"n": 3,
             "t_en": "Use software-defined control to get smarter, faster, more agile manufacturing",
             "t_vi": "Dùng điều khiển định nghĩa bằng phần mềm để sản xuất thông minh, nhanh và linh hoạt hơn",
             "b_en": "Software-defined control is revolutionizing process manufacturing by enabling "
                     "the use of server and virtualization technologies to deliver greater "
                     "computing power, which can provide AI-driven insights, advanced analytics and "
                     "improved real-time decision-making.",
             "b_vi": "Điều khiển định nghĩa bằng phần mềm đang thay đổi sản xuất quá trình bằng cách "
                     "dùng máy chủ và công nghệ ảo hóa để có năng lực tính toán lớn hơn, phục vụ hiểu "
                     "biết dẫn dắt bởi AI, phân tích nâng cao và ra quyết định thời gian thực tốt hơn.",
             "href": "https://www.controleng.com/use-software-defined-control-to-get-smarter-faster-more-agile-manufacturing/"},
            {"n": 4,
             "t_en": "Why thoughtful integration beats quick AI fixes in MES",
             "t_vi": "Vì sao tích hợp có tính toán thắng bản vá AI nhanh trong MES",
             "b_en": "As life sciences manufacturers turn to AI to streamline recipe creation and "
                     "simplify complex Manufacturing Execution System (MES) environments, a "
                     "measured, strategic approach \u2014 rooted in a trusted automation ecosystem \u2014 "
                     "will deliver greater long-term value than hastily adopted bolt-on solutions.",
             "b_vi": "Khi nhà sản xuất ngành khoa học sự sống dùng AI để đơn giản hóa việc tạo công "
                     "thức và môi trường MES phức tạp, một cách tiếp cận có tính toán và chiến lược "
                     "\u2014 dựa trên hệ sinh thái tự động hóa đáng tin cậy \u2014 sẽ mang lại giá trị dài "
                     "hạn lớn hơn giải pháp gắn ngoài vội vã.",
             "href": "https://www.controleng.com/why-thoughtful-integration-beats-quick-ai-fixes-in-mes/"},
            {"n": 5,
             "t_en": "How to leverage cloud analytics to maximize industrial data",
             "t_vi": "Tận dụng phân tích đám mây để khai thác tối đa dữ liệu công nghiệp",
             "b_en": "Improving collaboration, cloud and hybrid analytics platforms help adopters "
                     "gain a competitive advantage by reducing information technology (IT) "
                     "overhead, ensuring regulatory compliance and standardizing operations across "
                     "entire enterprises.",
             "b_vi": "Nền tảng phân tích đám mây và lai giúp người dùng có lợi thế cạnh tranh bằng "
                     "cách giảm chi phí công nghệ thông tin, bảo đảm tuân thủ quy định và chuẩn hóa "
                     "vận hành trên toàn doanh nghiệp.",
             "href": "https://www.controleng.com/how-to-leverage-cloud-analytics-to-maximize-industrial-data/"},
            {"n": 6,
             "t_en": "Research: Hot topics in Control Engineering for 2025",
             "t_vi": "Nghiên cứu: Các chủ đề nóng của Control Engineering năm 2025",
             "b_en": "The most-read Control Engineering stories of 2025, ranked by Google Analytics "
                     "pageviews, reflect reader interest in automation fundamentals, AI, "
                     "cybersecurity and open systems.",
             "b_vi": "Những bài được đọc nhiều nhất trên Control Engineering năm 2025, xếp theo lượt "
                     "xem Google Analytics, phản ánh quan tâm của bạn đọc với kiến thức cơ bản về tự "
                     "động hóa, AI, an ninh mạng và hệ mở.",
             "href": "https://www.controleng.com/research-hot-topics-in-control-engineering-for-2025/"},
            {"n": 7,
             "t_en": "Ctrl+Alt+Mfg Ep. 7: Digital twins explained \u2014 how virtual plants are transforming manufacturing",
             "t_vi": "Ctrl+Alt+Mfg tập 7: Giải thích bản sao số \u2014 nhà máy ảo đang thay đổi sản xuất thế nào",
             "b_en": "Insights from E Tech Group's Matt Wise and Cole Switzer on scaling digital "
                     "twins, building the data backbone and turning simulation into measurable ROI.",
             "b_vi": "Góc nhìn của Matt Wise và Cole Switzer (E Tech Group) về mở rộng bản sao số, "
                     "xây xương sống dữ liệu và biến mô phỏng thành ROI đo được.",
             "href": "https://www.controleng.com/podcast/ctrlaltmfg-ep-7-digital-twins-explained-how-virtual-plants-are-transforming-manufacturing-with-matt-wise-and-cole-switzer-e-tech-group/"},
            {"n": 8,
             "t_en": "State of Automation 2026: Which technologies give early adopters the edge?",
             "t_vi": "State of Automation 2026: Công nghệ nào cho người đi trước lợi thế?",
             "b_en": "What are early automation adopter benefits? Examine State of Automation 2026 "
                     "analytics and emerging technologies in Control Engineering's research report.",
             "b_vi": "Lợi ích của người áp dụng tự động hóa sớm là gì? Xem phân tích State of "
                     "Automation 2026 và các công nghệ mới nổi trong báo cáo nghiên cứu của Control "
                     "Engineering.",
             "href": "https://www.controleng.com/think-again-about-state-of-automation-2026/"},
            {"n": 9,
             "t_en": "Digital transformation in print manufacturing: from manual processes to smart production",
             "t_vi": "Chuyển đổi số trong sản xuất in: từ quy trình thủ công đến sản xuất thông minh",
             "b_en": "How a traditional print production process modernized into a smart, scalable "
                     "system that reduced errors, improved traceability and increased throughput.",
             "b_vi": "Một quy trình sản xuất in truyền thống đã hiện đại hóa thành hệ thống thông "
                     "minh, mở rộng được, giảm lỗi, cải thiện truy xuất nguồn gốc và tăng năng suất.",
             "href": "https://www.controleng.com/digital-transformation-in-print-manufacturing-from-manual-processes-to-smart-production/"},
            {"n": 10,
             "t_en": "Ctrl+Alt+Mfg Ep. 8: Inside the 2026 State of Automation Report",
             "t_vi": "Ctrl+Alt+Mfg tập 8: Bên trong Báo cáo State of Automation 2026",
             "b_en": "Data from Control Engineering's latest research reveals where automation is "
                     "delivering real ROI, why adoption is growing more cautious, and how "
                     "manufacturers are balancing efficiency, risk and workforce challenges.",
             "b_vi": "Dữ liệu từ nghiên cứu mới nhất của Control Engineering cho thấy tự động hóa "
                     "đang tạo ROI thật ở đâu, vì sao việc áp dụng thận trọng hơn, và nhà sản xuất "
                     "đang cân bằng hiệu quả, rủi ro và thách thức nhân lực ra sao.",
             "href": "https://www.controleng.com/podcast/ctrlaltmfg-ep-8-inside-the-2026-state-of-automation-report-with-mark-hoske-control-engineering/"},
        ],
    },
    {
        "slug": "january-2026",
        "en": "January 2026",
        "vi": "Tháng 1/2026",
        "angle_en": "PID opens the year at number one, and the security argument shifts from "
                    "\u201cbuy a product\u201d to \u201czero trust does not fit a plant floor\u201d.",
        "angle_vi": "PID mở đầu năm ở vị trí số một, và lập luận an ninh chuyển từ \u201cmua một sản "
                    "phẩm\u201d sang \u201czero trust không hợp với sàn nhà máy\u201d.",
        "src": "https://www.controleng.com/control-engineering-hot-topics-january-2026/",
        "items": [
            {"n": 1,
             "t_en": "PID spotlight, part 22: Can I tune a noisy PID controller?",
             "t_vi": "PID spotlight, phần 22: Có hiệu chỉnh được bộ PID nhiễu không?",
             "b_en": "If I have a noisy process, can I still use the same tuning methods? Can I get "
                     "good tuning despite noise, and if not, what can I do to compensate?",
             "b_vi": "Nếu quá trình nhiễu, tôi có còn dùng được các phương pháp hiệu chỉnh đó? Có thể "
                     "hiệu chỉnh tốt dù có nhiễu không, và nếu không thì bù bằng cách nào?",
             "href": "https://www.controleng.com/pid-spotlight-part-22-can-i-tune-a-noisy-pid-controller/"},
            {"n": 2,
             "t_en": "Introduction to control software engineering, better automation designs",
             "t_vi": "Nhập môn kỹ thuật phần mềm điều khiển, thiết kế tự động hóa tốt hơn",
             "b_en": "Control software engineers seek control system solutions well beyond computer "
                     "software programming. Understand seven critical phases of the software "
                     "engineering workflow for control system design, and its worst enemy.",
             "b_vi": "Kỹ sư phần mềm điều khiển tìm giải pháp hệ thống vượt xa lập trình máy tính "
                     "thông thường. Hiểu bảy giai đoạn then chốt của quy trình kỹ thuật phần mềm cho "
                     "thiết kế hệ điều khiển \u2014 và kẻ thù lớn nhất của nó.",
             "href": "https://www.controleng.com/introduction-to-control-software-engineering-better-automation-designs/"},
            {"n": 3,
             "t_en": "How to use C++, datasets for motion control programming",
             "t_vi": "Dùng C++ và dataset cho lập trình điều khiển chuyển động",
             "b_en": "As machine controllers take on more responsibility beyond traditional control "
                     "tasks, systems are expected to handle motion control, data processing and "
                     "decisions in one platform. How does integrated programming help real-time "
                     "performance and system design?",
             "b_vi": "Khi bộ điều khiển máy đảm nhận nhiều việc hơn ngoài điều khiển truyền thống, hệ "
                     "thống được kỳ vọng xử lý điều khiển chuyển động, xử lý dữ liệu và ra quyết định "
                     "trên một nền tảng. Lập trình tích hợp giúp gì cho hiệu năng thời gian thực và "
                     "thiết kế hệ thống?",
             "href": "https://www.controleng.com/how-to-use-c-datasets-for-motion-control-programming/"},
            {"n": 4,
             "t_en": "Automation's front line: 2026 System Integrator Giants expand capabilities",
             "t_vi": "Tuyến đầu tự động hóa: System Integrator Giants 2026 mở rộng năng lực",
             "b_en": "Average revenue per firm rises about 30% as integrators broaden skills in "
                     "data, cybersecurity and robotics.",
             "b_vi": "Doanh thu bình quân mỗi công ty tăng khoảng 30% khi các đơn vị tích hợp mở rộng "
                     "kỹ năng về dữ liệu, an ninh mạng và robot.",
             "href": "https://www.controleng.com/2026-system-integrator-giants-expand-capabilities/"},
            {"n": 5,
             "t_en": "Why zero trust fails on the plant floor \u2014 and what actually works in OT",
             "t_vi": "Vì sao zero trust thất bại trên sàn nhà máy \u2014 và điều gì thực sự hiệu quả trong OT",
             "b_en": "IT-driven zero-trust frameworks break down in decentralized, high-pressure "
                     "manufacturing environments. Here's how to build security strategies that fit "
                     "the realities of industrial operations.",
             "b_vi": "Khung zero trust do IT dẫn dắt sụp đổ trong môi trường sản xuất phân tán, áp lực "
                     "cao. Đây là cách xây chiến lược bảo mật phù hợp với thực tế vận hành công nghiệp.",
             "href": "https://www.controleng.com/why-zero-trust-fails-on-the-plant-floor-and-what-actually-works-in-ot/"},
            {"n": 6,
             "t_en": "Control Engineering hot topics: November 2025",
             "t_vi": "Control Engineering hot topics: Tháng 11/2025",
             "b_en": "The top articles in Control Engineering this month covered topics like PID "
                     "tuning, DCS migration and the 2026 System Integrators of the Year.",
             "b_vi": "Những bài nổi bật trên Control Engineering tháng này gồm hiệu chỉnh PID, di trú "
                     "DCS và System Integrators of the Year 2026.",
             "href": "https://www.controleng.com/control-engineering-hot-topics-november-2025/"},
            {"n": 7,
             "t_en": "Three ways industrial AI enhances traditional control systems",
             "t_vi": "Ba cách AI công nghiệp nâng cao hệ điều khiển truyền thống",
             "b_en": "Artificial intelligence (AI) enables context-aware decision-making, adaptive "
                     "learning and predictive optimization to extend the value of traditional "
                     "automation frameworks.",
             "b_vi": "AI cho phép ra quyết định có ngữ cảnh, học thích nghi và tối ưu dự báo để mở "
                     "rộng giá trị của các khung tự động hóa truyền thống.",
             "href": "https://www.controleng.com/three-ways-industrial-ai-enhances-traditional-control-systems/"},
            {"n": 8,
             "t_en": "Latest automation mergers, December 2025: Controls, digital twins, robotics",
             "t_vi": "Thương vụ tự động hóa mới nhất, tháng 12/2025: điều khiển, bản sao số, robot",
             "b_en": "The Bundy Group reported 18 automation transactions in its December 2025 "
                     "summary reports, including transactions involving Agile Robots, Averna, "
                     "Flowserve and SPX Flow.",
             "b_vi": "Bundy Group báo cáo 18 thương vụ tự động hóa trong bản tổng hợp tháng 12/2025, "
                     "gồm các thương vụ liên quan Agile Robots, Averna, Flowserve và SPX Flow.",
             "href": "https://www.controleng.com/latest-automation-mergers-december-2025-controls-digital-twins-robotics/"},
            {"n": 9,
             "t_en": "Inside look: Automation ecosystem products, software, cybersecurity, AI",
             "t_vi": "Góc nhìn bên trong: sản phẩm, phần mềm, an ninh mạng và AI của hệ sinh thái tự động hóa",
             "b_en": "Hardware, software, products, applications, motion control, cybersecurity and "
                     "artificial intelligence updates provided for automation ecosystems. See "
                     "photos, examples and videos.",
             "b_vi": "Cập nhật về phần cứng, phần mềm, sản phẩm, ứng dụng, điều khiển chuyển động, an "
                     "ninh mạng và AI cho hệ sinh thái tự động hóa. Kèm ảnh, ví dụ và video.",
             "href": "https://www.controleng.com/inside-look-automation-ecosystem-products-software-cybersecurity-ai/"},
            {"n": 10,
             "t_en": "Ctrl+Alt+Mfg Ep. 6: Digital transformation \u2014 hype, reality and what's next",
             "t_vi": "Ctrl+Alt+Mfg tập 6: Chuyển đổi số \u2014 cơn sốt, thực tế và điều gì tiếp theo",
             "b_en": "A year-end look at how AI, simulation, edge computing and a rapidly evolving "
                     "workforce are reshaping digital transformation strategies and real-world "
                     "operations on the plant floor.",
             "b_vi": "Góc nhìn cuối năm về cách AI, mô phỏng, điện toán biên và lực lượng lao động "
                     "đang thay đổi nhanh đang định hình lại chiến lược chuyển đổi số và vận hành "
                     "thực tế trên sàn nhà máy.",
             "href": "https://www.controleng.com/podcast/ctrlaltmfg-ep-6-digital-transformation-hype-reality-whats-next-with-mike-ouellette-engineering-com/"},
        ],
    },
    {
        "slug": "december-2025",
        "en": "December 2025",
        "vi": "Tháng 12/2025",
        "angle_en": "A top ten that is really a top eight: three of the ten entries are the "
                    "same award \u2014 System Integrator of the Year \u2014 counted once as the "
                    "announcement and twice as the category profiles. Strip the duplication and "
                    "the month's actual subject is the integrator business.",
        "angle_vi": "Một top 10 thực chất chỉ là top 8: ba trong mười mục là cùng một giải "
                    "\u2014 System Integrator of the Year \u2014 được tính một lần là thông báo "
                    "và hai lần là chân dung theo hạng doanh thu. Bỏ phần trùng lặp, chủ đề thật "
                    "của tháng là nghề tích hợp hệ thống.",
        "src": "https://www.controleng.com/control-engineering-hot-topics-december-2025/",
        "items": [
            {"n": 1,
             "t_en": "System Integrator of the Year, 2026",
             "t_vi": "System Integrator of the Year 2026",
             "b_en": "Omnicon (under $20 million), Vertech ($20 million to $40 million) and Thermo "
                     "Systems (over $40 million) received recognition from Control Engineering and "
                     "Plant Engineering in this 19th annual award.",
             "b_vi": "Omnicon (dưới 20 triệu USD), Vertech (20\u201340 triệu USD) và Thermo Systems "
                     "(trên 40 triệu USD) được Control Engineering và Plant Engineering vinh danh "
                     "trong giải thưởng thường niên lần thứ 19 này.",
             "href": "https://www.controleng.com/system-integrator-of-the-year-2026/"},
            {"n": 2,
             "t_en": "2026 System Integrator of the Year: Mission-critical power, data center",
             "t_vi": "System Integrator of the Year 2026: điện nguồn trọng yếu và trung tâm dữ liệu",
             "b_en": "Thermo Systems wins in the over $40 million in system integration revenue "
                     "category, aiming to drive customer success through reliability.",
             "b_vi": "Thermo Systems thắng ở hạng doanh thu tích hợp hệ thống trên 40 triệu USD, "
                     "lấy độ tin cậy làm cách để mang lại thành công cho khách hàng.",
             "href": "https://www.controleng.com/2026-system-integrator-of-the-year-mission-critical-power-data-center/"},
            {"n": 3,
             "t_en": "2026 System Integrator of the Year: Chocolate, oil and gas automation",
             "t_vi": "System Integrator of the Year 2026: tự động hóa ngành chocolate, dầu khí",
             "b_en": "Omnicon is the winner in the under $20 million in system integration revenue "
                     "category.",
             "b_vi": "Omnicon thắng ở hạng doanh thu tích hợp hệ thống dưới 20 triệu USD.",
             "href": "https://www.controleng.com/2026-system-integrator-of-the-year-chocolate-oil-and-gas-automation/"},
            {"n": 4,
             "t_en": "State of Automation 2025 research: Year-end insights, guidance",
             "t_vi": "Nghiên cứu State of Automation 2025: nhận định và định hướng cuối năm",
             "b_en": "The Control Engineering survey and report, State of Industrial Automation "
                     "2025, created opportunities for additional coverage during the year on "
                     "automation, controls and instrumentation, supporting the survey results and "
                     "trends revealed in the report.",
             "b_vi": "Khảo sát và báo cáo State of Industrial Automation 2025 của Control Engineering "
                     "đã mở ra các bài viết bổ trợ trong năm về tự động hóa, điều khiển và thiết bị "
                     "đo, củng cố kết quả khảo sát và xu hướng mà báo cáo nêu ra.",
             "href": "https://www.controleng.com/state-of-automation-2025-research-year-end-insights-guidance/"},
            {"n": 5,
             "t_en": "Ctrl+Alt+Mfg Ep. 4: Making digital transformation real with Alicia Lomas",
             "t_vi": "Ctrl+Alt+Mfg tập 4: Biến chuyển đổi số thành hiện thực cùng Alicia Lomas",
             "b_en": "Systems leader Alicia Lomas explains how to turn \u201cdigital "
                     "transformation\u201d from a buzzword into measurable wins by starting with real "
                     "problems, adding context to data and pairing software talent with controls "
                     "expertise.",
             "b_vi": "Lãnh đạo hệ thống Alicia Lomas giải thích cách biến \u201cchuyển đổi số\u201d từ "
                     "một khẩu hiệu thành kết quả đo được: bắt đầu từ vấn đề thật, thêm ngữ cảnh cho "
                     "dữ liệu, và ghép nhân lực phần mềm với chuyên môn điều khiển.",
             "href": "https://www.controleng.com/podcast/ctrlaltmfg-ep-4-making-digital-transformation-real-with-alicia-lomas-lomas-manufacturing/"},
            {"n": 6,
             "t_en": "Introduction to control software engineering, better automation designs",
             "t_vi": "Nhập môn kỹ thuật phần mềm điều khiển, thiết kế tự động hóa tốt hơn",
             "b_en": "Control software engineers seek control system solutions well beyond computer "
                     "software programming. Understand seven critical phases of the software "
                     "engineering workflow for control system design, and its worst enemy.",
             "b_vi": "Kỹ sư phần mềm điều khiển tìm giải pháp hệ thống vượt xa lập trình máy tính "
                     "thông thường. Hiểu bảy giai đoạn then chốt của quy trình kỹ thuật phần mềm cho "
                     "thiết kế hệ điều khiển \u2014 và kẻ thù lớn nhất của nó.",
             "href": "https://www.controleng.com/introduction-to-control-software-engineering-better-automation-designs/"},
            {"n": 7,
             "t_en": "Why zero trust fails on the plant floor \u2014 and what actually works in OT",
             "t_vi": "Vì sao zero trust thất bại trên sàn nhà máy \u2014 và điều gì thực sự hiệu quả trong OT",
             "b_en": "IT-driven zero-trust frameworks break down in decentralized, high-pressure "
                     "manufacturing environments. Here's how to build security strategies that fit "
                     "the realities of industrial operations.",
             "b_vi": "Khung zero trust do IT dẫn dắt sụp đổ trong môi trường sản xuất phân tán, áp lực "
                     "cao. Đây là cách xây chiến lược bảo mật phù hợp với thực tế vận hành công nghiệp.",
             "href": "https://www.controleng.com/why-zero-trust-fails-on-the-plant-floor-and-what-actually-works-in-ot/"},
            {"n": 8,
             "t_en": "Scaling OT cybersecurity to meet modern manufacturing challenges",
             "t_vi": "Mở rộng an ninh mạng OT để đáp ứng thách thức sản xuất hiện đại",
             "b_en": "Rockwell Automation unveils the SecureOT solution suite, combining tools and "
                     "managed services for end-to-end protection.",
             "b_vi": "Rockwell Automation giới thiệu bộ giải pháp SecureOT, kết hợp công cụ và dịch vụ "
                     "quản lý để bảo vệ đầu-cuối.",
             "href": "https://www.controleng.com/scaling-ot-cybersecurity-to-meet-modern-manufacturing-challenges/"},
            {"n": 9,
             "t_en": "New facility strengthens manufacturing education and research",
             "t_vi": "Cơ sở mới củng cố đào tạo và nghiên cứu sản xuất",
             "b_en": "Arizona State University's new ISTB 12 building supports training, research and "
                     "industry collaboration in advanced manufacturing.",
             "b_vi": "Tòa nhà ISTB 12 mới của Đại học Bang Arizona hỗ trợ đào tạo, nghiên cứu và hợp "
                     "tác công nghiệp trong sản xuất tiên tiến.",
             "href": "https://www.controleng.com/new-facility-strengthens-manufacturing-education-and-research/"},
            {"n": 10,
             "t_en": "Latest automation mergers, October 2025: Robotics, industrial interoperability",
             "t_vi": "Thương vụ tự động hóa mới nhất, tháng 10/2025: robot và khả năng tương tác công nghiệp",
             "b_en": "The Bundy Group reported 32 automation transactions in its October 2025 "
                     "summary reports, including transactions involving ABB Robotics, Caterpillar "
                     "and the Object Management Group.",
             "b_vi": "Bundy Group báo cáo 32 thương vụ tự động hóa trong bản tổng hợp tháng 10/2025, "
                     "gồm các thương vụ liên quan ABB Robotics, Caterpillar và Object Management Group.",
             "href": "https://www.controleng.com/latest-automation-mergers-october-2025-robotics-industrial-interoperability/"},
        ],
    },
    {
        "slug": "november-2025",
        "en": "November 2025",
        "vi": "Tháng 11/2025",
        "angle_en": "Migration month. DCS migration at three, brownfield integration risk at "
                    "eight, controls upgrade at ten \u2014 three entries describing the same "
                    "decision from three angles. Only eight of ten positions survive in the "
                    "archive; ranks one and two are missing from the capture, so the list starts "
                    "at three.",
        "angle_vi": "Tháng của di trú. Di trú DCS ở vị trí ba, rủi ro tích hợp brownfield ở vị trí "
                    "tám, nâng cấp hệ điều khiển ở vị trí mười \u2014 ba bài mô tả cùng một quyết "
                    "định từ ba góc nhìn. Bản lưu chỉ giữ được tám trong mười vị trí; hạng một và "
                    "hai bị thiếu, nên danh sách bắt đầu từ hạng ba.",
        "src": "https://www.controleng.com/control-engineering-hot-topics-november-2025/",
        "items": [
            {"n": 3,
             "t_en": "The challenges of legacy systems and benefits of new technology in DCS migration",
             "t_vi": "Thách thức của hệ cũ và lợi ích của công nghệ mới trong di trú DCS",
             "b_en": "How one chemical plant navigated a complex control system upgrade to improve "
                     "safety, efficiency and future readiness.",
             "b_vi": "Một nhà máy hóa chất đã đi qua cuộc nâng cấp hệ điều khiển phức tạp thế nào để "
                     "cải thiện an toàn, hiệu quả và mức sẵn sàng cho tương lai.",
             "href": "https://www.controleng.com/the-challenges-of-legacy-systems-and-benefits-of-new-technology-in-dcs-migration/"},
            {"n": 4,
             "t_en": "2026 System Integrator of the Year: Mission-critical power, data center",
             "t_vi": "System Integrator of the Year 2026: điện nguồn trọng yếu và trung tâm dữ liệu",
             "b_en": "Thermo Systems wins in the over $40 million in system integration revenue "
                     "category, aiming to drive customer success through reliability.",
             "b_vi": "Thermo Systems thắng ở hạng doanh thu tích hợp hệ thống trên 40 triệu USD, "
                     "lấy độ tin cậy làm cách để mang lại thành công cho khách hàng.",
             "href": "https://www.controleng.com/2026-system-integrator-of-the-year-mission-critical-power-data-center/"},
            {"n": 5,
             "t_en": "More answers about how to select the right controller type",
             "t_vi": "Thêm câu trả lời về cách chọn đúng loại bộ điều khiển",
             "b_en": "System integration experts answer more questions from \u201cHow to select the "
                     "right controller type for the automation application\u201d, a Sept. 25 Control "
                     "Engineering webcast, than webcast time allowed.",
             "b_vi": "Các chuyên gia tích hợp hệ thống trả lời thêm những câu hỏi từ webcast ngày 25/9 "
                     "của Control Engineering, \u201cChọn đúng loại bộ điều khiển cho ứng dụng tự "
                     "động hóa\u201d, vượt quá thời lượng webcast cho phép.",
             "href": "https://www.controleng.com/more-answers-about-how-to-select-the-right-controller-type/"},
            {"n": 6,
             "t_en": "New facility strengthens manufacturing education and research",
             "t_vi": "Cơ sở mới củng cố đào tạo và nghiên cứu sản xuất",
             "b_en": "Arizona State University's new ISTB 12 building supports training, research and "
                     "industry collaboration in advanced manufacturing.",
             "b_vi": "Tòa nhà ISTB 12 mới của Đại học Bang Arizona hỗ trợ đào tạo, nghiên cứu và hợp "
                     "tác công nghiệp trong sản xuất tiên tiến.",
             "href": "https://www.controleng.com/new-facility-strengthens-manufacturing-education-and-research/"},
            {"n": 7,
             "t_en": "System Integrator of the Year, 2026",
             "t_vi": "System Integrator of the Year 2026",
             "b_en": "Omnicon (under $20 million), Vertech ($20 million to $40 million) and Thermo "
                     "Systems (over $40 million) received recognition from Control Engineering and "
                     "Plant Engineering in this 19th annual award.",
             "b_vi": "Omnicon (dưới 20 triệu USD), Vertech (20\u201340 triệu USD) và Thermo Systems "
                     "(trên 40 triệu USD) được Control Engineering và Plant Engineering vinh danh "
                     "trong giải thưởng thường niên lần thứ 19 này.",
             "href": "https://www.controleng.com/system-integrator-of-the-year-2026/"},
            {"n": 8,
             "t_en": "7 ways to mitigate brownfield automation integration risks",
             "t_vi": "7 cách giảm rủi ro tích hợp tự động hóa trên nền cũ (brownfield)",
             "b_en": "Smart automation integration requires even smarter planning. Here are the key "
                     "considerations to make sure your next facility automation and controls upgrade "
                     "is a success.",
             "b_vi": "Tích hợp tự động hóa thông minh đòi hỏi kế hoạch còn thông minh hơn. Đây là những "
                     "điểm cần cân nhắc để lần nâng cấp tự động hóa và điều khiển tới đây thành công.",
             "href": "https://www.controleng.com/7-ways-to-mitigate-brownfield-automation-integration-risks/"},
            {"n": 9,
             "t_en": "Motor and Drives 2025 study: What improvements buyers want",
             "t_vi": "Nghiên cứu Motor and Drives 2025: người mua muốn cải thiện gì",
             "b_en": "Most would be open to trying other brands of motors and drives, but easier "
                     "programming and configuration are needed, says Control Engineering research.",
             "b_vi": "Phần lớn sẵn sàng thử thương hiệu động cơ và biến tần khác, nhưng cần lập trình "
                     "và cấu hình dễ hơn, theo nghiên cứu của Control Engineering.",
             "href": "https://www.controleng.com/motor-and-drives-2025-study-what-improvements-buyers-want/"},
            {"n": 10,
             "t_en": "How a controls system upgrade boosts your plant's efficiency",
             "t_vi": "Nâng cấp hệ điều khiển giúp nhà máy hiệu quả hơn thế nào",
             "b_en": "Upgrading a plant's controls system can significantly boost efficiency and "
                     "extend the life of existing equipment, rather than requiring full equipment "
                     "replacement.",
             "b_vi": "Nâng cấp hệ điều khiển có thể tăng đáng kể hiệu quả và kéo dài tuổi thọ thiết bị "
                     "hiện có, thay vì phải thay toàn bộ thiết bị.",
             "href": "https://www.controleng.com/how-a-controls-system-upgrade-boosts-your-plants-efficiency/"},
        ],
    },
    {
        "slug": "october-2025",
        "en": "October 2025",
        "vi": "Tháng 10/2025",
        "angle_en": "The oldest month in the window, and the worst preserved: the archive keeps "
                    "only four of the ten positions. What survives is still the thread this site "
                    "follows \u2014 the Shell refinery running software-defined automation \u2014 "
                    "which is the same argument the /advanced section reads in detail.",
        "angle_vi": "Tháng cũ nhất trong cửa sổ khảo sát và cũng được lưu giữ kém nhất: bản lưu chỉ "
                    "còn bốn trong mười vị trí. Phần còn lại vẫn đúng mạch mà site này theo dõi "
                    "\u2014 nhà máy lọc dầu Shell chạy tự động hóa định nghĩa bằng phần mềm \u2014 "
                    "cũng chính là lập luận được đọc kỹ trong mục /advanced.",
        "src": "https://www.controleng.com/control-engineering-hot-topics-october-2025/",
        "items": [
            {"n": 1,
             "t_en": "Powerful new site expands transformer capacity in South Carolina",
             "t_vi": "Cơ sở mới mở rộng năng lực chế tạo máy biến áp tại Nam Carolina",
             "b_en": "Eaton will invest $340M in its Jonesville facility, creating 700 jobs and "
                     "expanding U.S. production of three-phase transformers.",
             "b_vi": "Eaton sẽ đầu tư 340 triệu USD vào cơ sở Jonesville, tạo 700 việc làm và mở rộng "
                     "sản xuất máy biến áp ba pha tại Mỹ.",
             "href": "https://www.controleng.com/powerful-new-site-expands-transformer-capacity-in-south-carolina/"},
            {"n": 2,
             "t_en": "Powering progress: Meet the 2025 Engineering Leaders Under 40",
             "t_vi": "Tiếp sức tiến bộ: gặp gỡ Engineering Leaders Under 40 2025",
             "b_en": "Celebrating 35 engineering professionals who are driving transformation, "
                     "mentorship and excellence across the industrial landscape.",
             "b_vi": "Tôn vinh 35 chuyên gia kỹ thuật đang thúc đẩy chuyển đổi, dẫn dắt thế hệ sau và "
                     "sự xuất sắc trên toàn bộ bức tranh công nghiệp.",
             "href": "https://www.controleng.com/powering-progress-meet-the-2025-engineering-leaders-under-40/"},
            {"n": 3,
             "t_en": "Shell modernizes refinery control with software-defined automation",
             "t_vi": "Shell hiện đại hóa điều khiển nhà máy lọc dầu bằng tự động hóa định nghĩa phần mềm",
             "b_en": "Schneider Electric demonstrates how the hardware-agnostic distributed "
                     "intelligence of its EcoStruxure Automation Expert platform is creating a "
                     "flexible control architecture for manufacturers.",
             "b_vi": "Schneider Electric trình bày cách trí tuệ phân tán không phụ thuộc phần cứng của "
                     "nền tảng EcoStruxure Automation Expert đang tạo ra kiến trúc điều khiển linh "
                     "hoạt cho nhà sản xuất.",
             "href": "https://www.controleng.com/shell-modernizes-refinery-control-with-software-defined-automation/"},
            {"n": 7,
             "t_en": "How to create a physical AI security, safety framework",
             "t_vi": "Cách xây khung an ninh và an toàn cho AI vật lý",
             "b_en": "Explore the security and safety aspects of the emerging field known as physical "
                     "artificial intelligence. As physical AI evolves from concept to reality, "
                     "understanding its implications for human safety and security becomes critical.",
             "b_vi": "Khám phá khía cạnh an ninh và an toàn của lĩnh vực đang nổi gọi là AI vật lý. Khi "
                     "AI vật lý đi từ khái niệm ra thực tế, việc hiểu hệ quả của nó với an toàn và an "
                     "ninh con người trở nên trọng yếu.",
             "href": "https://www.controleng.com/how-to-create-a-physical-ai-security-safety-framework/"},
        ],
    },
]


# The twelve months of the window, newest first, and what the archive actually
# holds: "full" = all ten positions, "partial" = some, "gap" = no archived post.
COVERAGE = [
    ("2026-09", "Sep 2026", "T9/2026", "full", "september-2026"),
    ("2026-08", "Aug 2026", "T8/2026", "full", "august-2026"),
    ("2026-07", "Jul 2026", "T7/2026", "gap", None),
    ("2026-06", "Jun 2026", "T6/2026", "gap", None),
    ("2026-05", "May 2026", "T5/2026", "gap", None),
    ("2026-04", "Apr 2026", "T4/2026", "gap", None),
    ("2026-03", "Mar 2026", "T3/2026", "gap", None),
    ("2026-02", "Feb 2026", "T2/2026", "full", "february-2026"),
    ("2026-01", "Jan 2026", "T1/2026", "full", "january-2026"),
    ("2025-12", "Dec 2025", "T12/2025", "full", "december-2025"),
    ("2025-11", "Nov 2025", "T11/2025", "partial", "november-2025"),
    ("2025-10", "Oct 2025", "T10/2025", "partial", "october-2025"),
]

# Monthly posts from before the window that the archive does have, for a reader
# who wants to go further back. Linked, not reprinted: this page stops at the
# twelve months the section is about.
EARLIER = [
    ("September 2025", "Tháng 9/2025",
     "https://www.controleng.com/control-engineering-hot-topics-september-2025/"),
    ("August 2025", "Tháng 8/2025",
     "https://www.controleng.com/control-engineering-hot-topics-august-2025/"),
    ("June 2025", "Tháng 6/2025",
     "https://www.controleng.com/control-engineering-hot-topics-june-2025/"),
    ("April 2025", "Tháng 4/2025",
     "https://www.controleng.com/control-engineering-hot-topics-april-2025/"),
    ("March 2025", "Tháng 3/2025",
     "https://www.controleng.com/control-engineering-hot-topics-march-2025/"),
    ("February 2025", "Tháng 2/2025",
     "https://www.controleng.com/control-engineering-hot-topics-february-2025/"),
]

# ---------------------------------------------------------------------------
# The other magazine: Automation.com Monthly, harvested from the public issue
# pages on automation.com (no login, no paywall). There are no ranks here and
# there is no pageview count to rank: these are the features an editor
# commissioned for the issue, which is a different measurement from a
# most-read table. Cards the source marks 'Sponsored By <name>' are excluded,
# as are editor's messages and roundups.
#
# InTech, the ISA magazine, ended with its October 2024 issue and is not used:
# the 2025 issues here are largely ISA-sponsored InTech material, and those
# cards are excluded on the same rule as vendor placements.
# ---------------------------------------------------------------------------

PRESS = [
    {
        "slug": "acm-2026-10",
        "en": "October 2026",
        "vi": "Tháng 10/2026",
        "kicker_en": "OT cybersecurity annual",
        "kicker_vi": "Số thường niên về an ninh OT",
        "src": "https://www.automation.com/article/automation.com-monthly-october-2026",
        "items": [
            {"t_en": "Securing America’s Water Systems: From Malicious Cyber Activity to Measurable Risk Reduction",
             "t_vi": "Bảo vệ hệ thống nước của Mỹ: từ hoạt động tấn công mạng đến giảm thiểu rủi ro đo được",
             "b_en": "Recent incidents have accelerated efforts to help water utilities improve their cybersecurity posture. One of the most significant is Project Watershed 250.",
             "b_vi": "Những sự cố gần đây đã thúc đẩy các nỗ lực giúp ngành nước cải thiện thế phòng thủ mạng. Một trong những nỗ lực đáng kể nhất là Project Watershed 250.",
             "href": "https://www.automation.com/article/securing-america-s-water-systems-from-malicious-cyber-activity"},
            {"t_en": "A Practical Path to Post-Quantum Readiness in Operational Technology",
             "t_vi": "Lộ trình thực tế để sẵn sàng hậu lượng tử trong OT",
             "b_en": "How to develop an OT cybersecurity roadmap to transition to PQC algorithms designed to resist quantum-computer-enabled decryption.",
             "b_vi": "Cách xây dựng lộ trình an ninh mạng OT để chuyển sang các thuật toán PQC, vốn được thiết kế chống lại việc giải mã bằng máy tính lượng tử.",
             "href": "https://www.automation.com/article/a-practical-path-post-quantum-readiness-operational-technology"},
            {"t_en": "A Backup Is Not a Recovery Plan: Measuring What It Really Takes To Restore OT After an Incident",
             "t_vi": "Sao lưu không phải là kế hoạch phục hồi: đo xem thực sự cần gì để khôi phục OT sau sự cố",
             "b_en": "In addition to a successful backup, nine conditions determine whether OT recovery takes hours, days or weeks.",
             "b_vi": "Ngoài một bản sao lưu thành công, chín điều kiện quyết định việc khôi phục OT mất vài giờ, vài ngày hay vài tuần.",
             "href": "https://www.automation.com/article/a-backup-not-a-recovery-plan-measuring-what-takes-to-restore-ot-after-incident"},
            {"t_en": "Exploring Gateway Architectures for Quantum-Safe Industrial Networks",
             "t_vi": "Khảo sát kiến trúc gateway cho mạng công nghiệp an toàn lượng tử",
             "b_en": "Operational technology systems are not ready for the recent NIST cybersecurity standards. Given the constraints, cryptographic processing at network boundaries rather than on endpoints may be the answer.",
             "b_vi": "Hệ OT chưa sẵn sàng cho các tiêu chuẩn an ninh mạng mới của NIST. Trong giới hạn hiện có, xử lý mật mã nên đặt ở biên mạng thay vì trên từng thiết bị đầu cuối.",
             "href": "https://www.automation.com/article/exploring-gateway-architectures-quantum-safe-industrial-networks"},
            {"t_en": "The Cyber Resilience Act: Compliance Starts with Product Security, Not Documentation",
             "t_vi": "Cyber Resilience Act: tuân thủ bắt đầu từ an ninh sản phẩm, không phải giấy tờ",
             "b_en": "Implementing the CRA is an opportunity to achieve higher levels of product security maturity by actively anticipating and preparing to address security issues that may arise throughout a product’s lifecycle.",
             "b_vi": "Triển khai CRA là cơ hội đạt mức trưởng thành an ninh sản phẩm cao hơn, bằng cách chủ động lường trước và chuẩn bị xử lý những vấn đề an ninh có thể phát sinh suốt vòng đời.",
             "href": "https://www.automation.com/article/the-cyber-resilience-act-compliance-starts-product-security-not-documentation"},
            {"t_en": "Cybersecurity Strategies for Managing End-of-Life Industrial IoT Devices",
             "t_vi": "Chiến lược an ninh mạng cho thiết bị IIoT hết vòng đời",
             "b_en": "Organizations that establish strong life cycle management practices position themselves to adapt as threats evolve and technology advances.",
             "b_vi": "Tổ chức xây dựng được thực hành quản lý vòng đời vững chắc sẽ ở thế chủ động thích ứng khi mối đe dọa thay đổi và công nghệ tiến lên.",
             "href": "https://www.automation.com/article/cybersecurity-strategies-managing-end-life-industrial-iot-devices"},
        ],
    },
    {
        "slug": "acm-2026-09",
        "en": "September 2026",
        "vi": "Tháng 9/2026",
        "kicker_en": "Process automation & instrumentation",
        "kicker_vi": "Tự động hóa quá trình & thiết bị đo",
        "src": "https://www.automation.com/article/automation.com-monthly-september-2026",
        "items": [
            {"t_en": "When Automation Changes the Job, Who Is Still Qualified to Do It?",
             "t_vi": "Khi tự động hóa thay đổi công việc, ai còn đủ năng lực làm?",
             "b_en": "Plant leaders should be able to answer four questions: What work changed? Who is affected? What evidence demonstrates readiness? What event will trigger another assessment?",
             "b_vi": "Lãnh đạo nhà máy cần trả lời được bốn câu hỏi: việc gì đã thay đổi, ai bị ảnh hưởng, bằng chứng nào cho thấy đã sẵn sàng, và sự kiện nào sẽ buộc phải đánh giá lại.",
             "href": "https://www.automation.com/article/when-automation-changes-job-who-still-qualified-do-it"},
            {"t_en": "Are We Over-Automating? How to Decide Where Automation Actually Adds Value",
             "t_vi": "Có phải đang tự động hóa quá mức? Cách quyết định nơi tự động hóa thực sự tạo giá trị",
             "b_en": "The goal isn’t to automate everything that can be automated. It’s to make deliberate investments that leave the operation safer, more reliable and more productive than it was before.",
             "b_vi": "Mục tiêu không phải tự động hóa mọi thứ có thể, mà là đầu tư có chủ đích để vận hành an toàn hơn, tin cậy hơn và năng suất hơn trước.",
             "href": "https://www.automation.com/article/over-automating-how-decide-where-automation-adds-value"},
            {"t_en": "Automation Does Not Scale Judgment Unless You Transfer the Judgment",
             "t_vi": "Tự động hóa không mở rộng được phán đoán nếu không chuyển giao chính phán đoán đó",
             "b_en": "Why AI-enabled workflows fail when organizations automate the visible task but leave the human decision logic behind.",
             "b_vi": "Vì sao quy trình có AI thất bại khi tổ chức tự động hóa phần việc nhìn thấy được nhưng bỏ lại phía sau logic quyết định của con người.",
             "href": "https://www.automation.com/article/automation-does-not-scale-judgment-unless-you-transfer-the-judgment"},
            {"t_en": "Rethinking Continuous Process Verification with Advanced Analytics",
             "t_vi": "Nghĩ lại về thẩm tra quá trình liên tục với phân tích nâng cao",
             "b_en": "Companies are evolving from static reports to living models by strengthening their data backbone with advanced analytics and AI platforms.",
             "b_vi": "Các công ty đang chuyển từ báo cáo tĩnh sang mô hình sống, bằng cách củng cố trục dữ liệu với phân tích nâng cao và nền tảng AI.",
             "href": "https://www.automation.com/article/rethinking-continuous-process-verification-advanced-analytics"},
            {"t_en": "Ask the Automation Pros: What University Projects Are Needed to Support Process Control?",
             "t_vi": "Hỏi chuyên gia tự động hóa: cần những đồ án đại học nào để hỗ trợ điều khiển quá trình?",
             "b_en": "Like a lot of things in engineering and construction, it’s hard to teach everything and risky not to, but getting it right the first time saves time and money.",
             "b_vi": "Như nhiều việc trong kỹ thuật và xây dựng, dạy hết mọi thứ là khó, bỏ sót lại rủi ro; nhưng làm đúng ngay từ đầu thì tiết kiệm thời gian và tiền.",
             "href": "https://www.automation.com/article/ask-the-automation-pros-what-university-projects-needed-support-process-control"},
        ],
    },
    {
        "slug": "acm-2026-06",
        "en": "June 2026",
        "vi": "Tháng 6/2026",
        "kicker_en": "IIoT & digital transformation",
        "kicker_vi": "IIoT & chuyển đổi số",
        "src": "https://www.automation.com/article/automation.com-monthly-june-2026",
        "items": [
            {"t_en": "Predictive Maintenance: Using Displacement Sensors for Real-Time Condition Monitoring",
             "t_vi": "Bảo trì dự báo: dùng cảm biến dịch chuyển để giám sát tình trạng theo thời gian thực",
             "b_en": "Learn how laser, eddy and other displacement sensors work and how they plug into IIoT PdM systems. They’re game changers on the shop floor.",
             "b_vi": "Cảm biến laser, cảm biến dòng xoáy và các loại cảm biến dịch chuyển khác hoạt động thế nào, và mắc vào hệ bảo trì dự báo của IIoT ra sao.",
             "href": "https://www.automation.com/article/displacement-sensors-real-time-condition-monitoring"},
            {"t_en": "Converting Smart Digital Valve Controller Investments into Profits",
             "t_vi": "Biến khoản đầu tư bộ điều khiển van số thông minh thành lợi nhuận",
             "b_en": "If your maintenance staff find themselves overwhelmed, and if unexpected control valve failures are costing the plant money and production, it may be time to take full advantage of the smart DVCs and communication networks that likely already exist in your facility.",
             "b_vi": "Nếu nhân sự bảo trì quá tải và những lần hỏng van điều khiển bất ngờ đang làm mất tiền và sản lượng, có thể đã đến lúc tận dụng hết dữ liệu chẩn đoán mà thiết bị vẫn đang tạo ra.",
             "href": "https://www.automation.com/article/converting-smart-digital-valve-controller-investments-profits"},
            {"t_en": "Consistent Changeovers and Predictable Performance with Industrial AI",
             "t_vi": "Đổi sản phẩm ổn định và hiệu năng dự đoán được nhờ AI công nghiệp",
             "b_en": "By embedding industrial AI directly into changeover workflows, manufacturers are significantly reducing variability, which is increasing process stability, accelerating time to insight, improving quality and driving more consistent and predictable production runs.",
             "b_vi": "Nhúng AI công nghiệp trực tiếp vào quy trình đổi sản phẩm giúp nhà sản xuất giảm mạnh độ biến thiên, nhờ đó tăng độ ổn định của quá trình và rút ngắn thời gian chuyển đổi.",
             "href": "https://www.automation.com/article/consistent-changeovers-predictable-performance-industrial-ai"},
            {"t_en": "Compliant But Vulnerable: Why Cyber Resilience Is No Longer a Privilege",
             "t_vi": "Tuân thủ mà vẫn dễ tổn thương: vì sao khả năng phục hồi mạng không còn là đặc quyền",
             "b_en": "Morocco’s critical infrastructure operators are pushing toward digitalization. Beyond checking compliance boxes, what does it mean to have a facility that is truly cyber resilient?",
             "b_vi": "Các đơn vị hạ tầng trọng yếu của Morocco đang đẩy nhanh số hóa. Ngoài việc đánh dấu vào ô tuân thủ, một nhà máy thực sự có khả năng phục hồi mạng nghĩa là gì?",
             "href": "https://www.automation.com/article/compliant-but-vulnerable-why-cyber-resilience-no-longer-privilege"},
        ],
    },
    {
        "slug": "acm-2026-05",
        "en": "May 2026 (Trends)",
        "vi": "Tháng 5/2026 (xu hướng)",
        "kicker_en": "11th annual trends issue",
        "kicker_vi": "Số xu hướng thường niên lần thứ 11",
        "src": "https://www.automation.com/article/automation.com-monthly-may-2026-annual-trends",
        "items": [
            {"t_en": "Industry 5.0: The Digital Journey of Enterprise-Wide Intelligence",
             "t_vi": "Industry 5.0: hành trình số hướng tới trí tuệ toàn doanh nghiệp",
             "b_en": "The quest for optimization begins with digital connectivity, unlocking opportunities for insight generation, automated modeling and predictive maintenance, all essential for productivity in today’s demanding process environments.",
             "b_vi": "Cuộc tìm kiếm tối ưu bắt đầu từ kết nối số, mở ra cơ hội tạo hiểu biết, mô hình hóa tự động và bảo trì dự báo.",
             "href": "https://www.automation.com/article/industry-5-digital-journey-enterprise-wide-intelligence"},
            {"t_en": "The Industrial Orchestration Layer: Empowering Shop Floor Intelligence",
             "t_vi": "Lớp điều phối công nghiệp: trao năng lực cho trí tuệ trên sàn nhà máy",
             "b_en": "As a secure and deterministic bridge between stochastic AI models and physical machinery, the industrial orchestration layer empowers manufacturers to safely automate real-time decision-making while ensuring safe operations.",
             "b_vi": "Là cầu nối an toàn và tất định giữa các mô hình AI mang tính ngẫu nhiên với máy móc vật lý, lớp điều phối công nghiệp cho phép dùng AI mà không mất tính tất định của điều khiển.",
             "href": "https://www.automation.com/article/industrial-orchestration-layer-shop-floor-intelligence"},
            {"t_en": "Manufacturing's AI Moment: The Tech Powering the Workforce to Take the Next Industrial Leap",
             "t_vi": "Khoảnh khắc AI của sản xuất: công nghệ tiếp sức cho lực lượng lao động",
             "b_en": "Here's how manufacturers translate AI investment into real-world gains on the shop floor.",
             "b_vi": "Đây là cách nhà sản xuất chuyển khoản đầu tư AI thành kết quả thực tế trên sàn nhà máy.",
             "href": "https://www.automation.com/article/manufacturing-ai-moment-tech-powering-workforce-next-industrial-leap"},
            {"t_en": "Logistics Industry Trends: Software-Layer Solutions and Resilience Planning",
             "t_vi": "Xu hướng ngành logistics: giải pháp ở lớp phần mềm và hoạch định khả năng phục hồi",
             "b_en": "The software layer is connecting data, automation, labor management, slotting and exception handling.",
             "b_vi": "Lớp phần mềm đang nối dữ liệu, tự động hóa, quản lý nhân lực, sắp xếp vị trí hàng và xử lý ngoại lệ thành một khối.",
             "href": "https://www.automation.com/article/logistics-industry-trends-software-layer-solutions-resilience-planning"},
        ],
    },
    {
        "slug": "acm-2026-02",
        "en": "February 2026",
        "vi": "Tháng 2/2026",
        "kicker_en": "IIoT & digital transformation",
        "kicker_vi": "IIoT & chuyển đổi số",
        "src": "https://www.automation.com/article/automation.com-monthly-february-2026",
        "items": [
            {"t_en": "Architecting a Resilient MES",
             "t_vi": "Thiết kế kiến trúc MES có khả năng phục hồi",
             "b_en": "Edge-native reference architectures can keep deterministic control local while using the cloud for analytics, while avoiding vendor lock-in.",
             "b_vi": "Kiến trúc tham chiếu thuần biên giữ điều khiển tất định tại chỗ trong khi dùng đám mây cho phân tích, đồng thời tránh bị khóa vào một nhà cung cấp.",
             "href": "https://www.automation.com/article/architecting-resilient-mes"},
            {"t_en": "How AI Is Transforming Industrial Automation Software Development",
             "t_vi": "AI đang thay đổi việc phát triển phần mềm tự động hóa công nghiệp thế nào",
             "b_en": "AI is becoming a strategic differentiator in industrial automation; those who learn to apply it effectively will shape the next generation of industrial projects.",
             "b_vi": "AI đang trở thành yếu tố khác biệt chiến lược trong tự động hóa công nghiệp; ai biết áp dụng hiệu quả sẽ định hình thế hệ phần mềm công nghiệp kế tiếp.",
             "href": "https://www.automation.com/article/how-ai-transforming-industrial-automation-software-development"},
        ],
    },
    {
        "slug": "acm-2026-01",
        "en": "January 2026",
        "vi": "Tháng 1/2026",
        "kicker_en": "Process automation & instrumentation",
        "kicker_vi": "Tự động hóa quá trình & thiết bị đo",
        "src": "https://www.automation.com/article/automation.com-monthly-january-2026",
        "items": [
            {"t_en": "Real-time Corrosion and Erosion Monitoring Enhances Maintenance Planning",
             "t_vi": "Giám sát ăn mòn và xói mòn theo thời gian thực cải thiện kế hoạch bảo trì",
             "b_en": "Ultrasonic corrosion and erosion monitoring instruments provide plant personnel with asset integrity information that facilitates proactive maintenance.",
             "b_vi": "Thiết bị giám sát ăn mòn và xói mòn bằng siêu âm cung cấp cho nhân sự nhà máy thông tin về toàn vẹn tài sản, giúp chuyển sang bảo trì chủ động.",
             "href": "https://www.automation.com/article/real-time-corrosion-erosion-monitoring-enhances-maintenance-planning"},
            {"t_en": "Cryogenic Precision: Measuring Nitrogen Flow With Coriolis Mass Flow Meters",
             "t_vi": "Độ chính xác ở nhiệt độ cryo: đo lưu lượng nitơ bằng lưu lượng kế khối lượng Coriolis",
             "b_en": "Coriolis mass flow meters measure mass directly and remain accurate regardless of temperature, pressure or state.",
             "b_vi": "Lưu lượng kế khối lượng Coriolis đo trực tiếp khối lượng và vẫn chính xác bất kể nhiệt độ, áp suất hay trạng thái.",
             "href": "https://www.automation.com/article/cryogenic-precision-measuring-nitrogen-flow"},
        ],
    },
    {
        "slug": "acm-2025-11",
        "en": "November/December 2025",
        "vi": "Tháng 11–12/2025",
        "kicker_en": "AI in operations",
        "kicker_vi": "AI trong vận hành",
        "src": "https://www.automation.com/article/automation.com-monthly-november-december-2025",
        "items": [
            {"t_en": "Autonomous AI Software for Manufacturing Has Arrived",
             "t_vi": "Phần mềm AI tự hành cho sản xuất đã đến",
             "b_en": "Industrial AI deployments can successfully augment human capabilities with the right software applied to specific problems.",
             "b_vi": "Triển khai AI công nghiệp có thể bổ trợ năng lực con người một cách hiệu quả, với điều kiện chọn đúng phần mềm cho đúng bài toán.",
             "href": "https://www.automation.com/article/success-manufacturing-ai"},
            {"t_en": "Case Study: AI-Driven Data Reduces Refinery Maintenance Costs",
             "t_vi": "Nghiên cứu tình huống: dữ liệu dẫn dắt bởi AI giảm chi phí bảo trì nhà máy lọc dầu",
             "b_en": "A large petrochemical producer deploys an asset performance management solution with AI-driven diagnostics.",
             "b_vi": "Một nhà sản xuất hóa dầu lớn triển khai giải pháp quản lý hiệu năng tài sản với chẩn đoán dẫn dắt bởi AI.",
             "href": "https://www.automation.com/article/case-study-ai-driven-data-reduces-refinery-maintenance-costs"},
        ],
    },
    {
        "slug": "acm-2025-06",
        "en": "June/July 2025",
        "vi": "Tháng 6–7/2025",
        "kicker_en": "Plant systems & operations",
        "kicker_vi": "Hệ thống nhà máy & vận hành",
        "src": "https://www.automation.com/article/automation-com-monthly-june-july-2025-issue",
        "items": [
            {"t_en": "IoT-Enabled Self-Healing in Network Devices",
             "t_vi": "Tự phục hồi nhờ IoT trong thiết bị mạng",
             "b_en": "Edge computing, machine learning algorithms and centralized management platforms work in tandem to ensure industrial systems keep running.",
             "b_vi": "Điện toán biên, thuật toán học máy và nền tảng quản lý tập trung phối hợp với nhau để hệ thống công nghiệp vẫn chạy liên tục.",
             "href": "https://www.automation.com/article/iot-enabled-self-healing-network-devices"},
            {"t_en": "Unlocking Smarter Manufacturing",
             "t_vi": "Mở ra sản xuất thông minh hơn",
             "b_en": "Use this three-stage blueprint to ensure success when rethinking industrial operations.",
             "b_vi": "Một bản thiết kế ba giai đoạn để bảo đảm thành công khi tái cấu trúc vận hành công nghiệp.",
             "href": "https://www.automation.com/article/unlocking-smarter-manufacturing"},
            {"t_en": "How to Get Maximum Value From Your MES",
             "t_vi": "Khai thác tối đa giá trị từ MES",
             "b_en": "Follow best practices when implementing a manufacturing execution system.",
             "b_vi": "Những thực hành tốt nhất khi triển khai hệ thống điều hành sản xuất (MES).",
             "href": "https://www.automation.com/article/how-get-maximum-value-mes"},
            {"t_en": "How Artificial Intelligence is Transforming Manufacturing",
             "t_vi": "AI đang thay đổi ngành sản xuất thế nào",
             "b_en": "Embedding AI systems into products makes AI accessible and usable for a wide range of users.",
             "b_vi": "Nhúng hệ thống AI vào sản phẩm giúp AI trở nên dễ tiếp cận và dùng được với nhiều nhóm người dùng.",
             "href": "https://www.automation.com/article/how-ai-transforming-manufacturing"},
            {"t_en": "Remote Operations Need Peak-Performance Batteries",
             "t_vi": "Vận hành từ xa cần pin hoạt động ở hiệu suất cao nhất",
             "b_en": "Expert recommendations can help optimize the supply of power to wireless devices in remote locations.",
             "b_vi": "Khuyến nghị của chuyên gia giúp tối ưu cấp nguồn cho thiết bị không dây ở những vị trí xa.",
             "href": "https://www.automation.com/article/remote-operations-need-peak-performance-batteries"},
        ],
    },
]
