# -*- coding: utf-8 -*-
"""Hot topics — generated EN page at /hot-topics/ and VI page at /vi/hot-topics/.

Two real URLs rather than a client-side toggle, matching /advanced/, /books/ and
/the video library: the Vietnamese page is Vietnamese in the HTML, so it is
indexable and reads correctly with JavaScript off.

The content is a year of Control Engineering's monthly most-read lists, from
build/hot_data.py. Nothing here is invented: the ranks, titles and summaries are
the publisher's, the monthly "angle" line is this site's reading of them, and the
months the archive does not have are stated as gaps rather than filled.
"""

import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import framework  # noqa: E402
import hot_data  # noqa: E402

BASE = "https://pro-instcontrol.github.io"
SITE = "Instrumentation &amp; Control"
SITE_VI = "Đo lường &amp; Điều khiển"

T = {
    "en": {
        "title": "Hot topics — a year of what the industry read | I&amp;C",
        "desc": "Twelve months of Control Engineering's most-read lists collected in one place: "
                "the articles that held attention across the year, the subjects that keep coming "
                "back, and the five months the archive does not have.",
        "skip": "Skip to content",
        "kicker": "Trade press",
        "h1": "What the industry actually read",
        "lede": "Every month Control Engineering publishes its ten most-read articles, ranked by "
                "pageviews. One list is a snapshot of a week's attention. Twelve of them, laid end "
                "to end, show which subjects keep coming back — and which only looked important the "
                "week they were published.",
        "toc": [
            ("method", "How the list is built"),
            ("months", "The months"),
            ("reading", "What a year shows"),
            ("press", "The other magazine"),
            ("here", "Read further here"),
        ],
        "lang_other": "VI",
        "lang_href": "../vi/hot-topics/",
        "nav_active": "hot-topics/",

        # 01 method
        "eb_1": "Method",
        "m_h": "How this list is built",
        "m_p1": "The source is the monthly <em>hot topics</em> post on controleng.com. Its ranks "
                "are Google Analytics pageviews for that month, so the list measures attention and "
                "not merit: a vendor announcement with a strong headline can outrank a careful "
                "tutorial, and a two-year-old article that search keeps serving can reappear "
                "beside news from last week.",
        "m_p2": "The text was harvested from archived copies of those posts, because the live site "
                "refuses scripted requests. Titles and summaries are the publisher's, translated; "
                "the sentence under each month heading is ours, and says what that month looks "
                "like once you have seen the others.",
        "m_note_h": "The archive does not have twelve months",
        "m_note_p": "Control Engineering does not always publish a list, and the Wayback Machine "
                    "does not always capture the ones it does. Five of the twelve months in this "
                    "window have no archived post at all — March to July 2026 — and the August "
                    "2026 post is titled <em>June 2026</em> because it covers June and July "
                    "together. October 2025 survives with four of ten positions, November 2025 "
                    "with eight. A year should hold a hundred and twenty ranked slots; sixty-two "
                    "exist. Nothing below is estimated to fill a hole.",
        "cov_legend": "Coverage, newest first",
        "cov_full": "complete",
        "cov_partial": "partial capture",
        "cov_gap": "no archived post",
        "earlier_k": "Before the window",
        "earlier_p": "The archive also holds these, and they are linked rather than reprinted:",

        # 02 months
        "eb_2": "The record",
        "mo_h": "Seven months, sixty-two positions",
        "mo_p": "Newest first, as published. The ranks are the publisher's; where a month is "
                "incomplete the numbering jumps, and it is left that way rather than renumbered.",
        "mo_src": "Original post",
        "mo_full": "all 10",
        "mo_partial": "partial",

        # 03 reading
        "eb_3": "Reading the year",
        "rd_h": "What twelve months of most-read lists actually shows",
        "obs": [
            ("Half the list is nine articles counted twice",
             "Sixty-two ranked positions resolve to fifty-three distinct articles. Nine pieces "
             "were read enough in one month to appear again the next: the PID gap-control column, "
             "the simulation-myths piece, the industrial-AI survey, the C++ motion-control "
             "article, the control-software-engineering introduction, the zero-trust argument, "
             "the System Integrator of the Year announcement and its Thermo Systems profile, and "
             "the Arizona State manufacturing building. A most-read list is a rolling window, not "
             "a fresh sample."),
            ("A tutorial series holds a sixth of the year",
             "Four of the sixty-two positions belong to one column: <em>PID spotlight</em>, at "
             "part 22 in January and parts 30 and 31 in August and September. Nine instalments "
             "across eight months, and the readership followed every one. Nothing else in the "
             "year — no product launch, no acquisition, no award — repeats like that. The lesson "
             "is uncomfortable for anyone who thinks trade publishing runs on news: the most "
             "reliable draw is a working engineer explaining one mechanism at a time."),
            ("Award copy is a sixth of the list",
             "Ten of the sixty-two positions are award announcements or honoree profiles: System "
             "Integrator of the Year five times, Engineering Leaders Under 40 four times, the "
             "Integrator Giants once. In December the top three are the same award — the "
             "announcement, then two category profiles — so that month's list is really a top "
             "eight. This is not a complaint about the publisher; it is what a readership does. "
             "People read about their peers, and about their competitors' projects, before they "
             "read about a control strategy."),
            ("Security is the only subject that never leaves, and it has changed register",
             "Five positions across four months: zero trust on the plant floor in December and "
             "again in January, a vendor OT suite in December, a podcast on cyberattacks that "
             "turn physical in February, and a framework for physical-AI safety in October. The "
             "argument has moved from <em>IT frameworks do not fit OT</em> to <em>the consequence "
             "is now mechanical</em>. That is the same shift the safety page here records, where "
             "NIS2 and the Cyber Resilience Act turned security from a project decision into a "
             "legal one."),
            ("Migration is where the money is",
             "November alone carries DCS migration at three, brownfield integration risk at "
             "eight and controls-system upgrade at ten — three entries describing one decision "
             "from three angles. Nobody reads about a new loop; everybody reads about the upgrade "
             "they are about to be asked to justify."),
            ("What is not on the list",
             "No functional-safety standard. No calibration. No SIL verification, no proof-test "
             "interval, no orifice-plate sizing. Outside the PID series there is almost no loop "
             "mathematics at all. A most-read list is not a curriculum, and the absence is the "
             "useful part: the subjects that decide whether a plant runs safely are read by a "
             "small, specific audience, in ones and twos, not in tens of thousands. That gap is "
             "why the technical pages here are longer than a trade article and shorter than a "
             "standard."),
        ],
        "rd_close": "Read these lists as a market signal, not a syllabus. What the industry is "
                    "curious about this year is architecture, security, careers and the cost of "
                    "standing still. What it is not curious about, at least not in public, is the "
                    "arithmetic inside the loop.",

        # 04 press
        "eb_4": "Second publisher",
        "pr_h": "The other magazine, and a different measurement",
        "pr_p1": "Control Engineering ranks by pageviews. Automation.com Monthly has no such table: "
                "an issue is the set of features an editor commissioned, and its order is the order "
                "of the magazine. Reprinting those titles as a second top ten would invent a ranking "
                "that does not exist, so they are listed unranked, issue by issue — and the "
                "difference is the point. One list measures what readers chose; the other measures "
                "what an editor thought they should read.",
        "pr_p2": "Eight issues are used, from June/July 2025 to October 2026. The source marks some "
                "cards <em>Sponsored By</em> a named company; those are advertising and are excluded, "
                "as are editor's messages and topical roundups. What is left is the editorial core "
                "of each issue, with the source's own summary under each title.",
        "pr_note_h": "Why there is no InTech here",
        "pr_note_p": "InTech was the ISA's magazine and it ended with the October 2024 issue — the "
                    "last two years of it do not exist to collect. The 2025 issues on automation.com "
                    "are largely ISA-sponsored InTech material, and those cards are excluded on the "
                    "same rule as vendor placements. Nothing here comes from isa.org: the society's "
                    "terms do not permit its material to be processed by a model.",
        "pr_items": "features",
        "pr_src": "Issue page",

        # 05 here
        "eb_5": "On this site",
        "hr_h": "Where these subjects are taken further",
        "hr_p": "The same stories, followed to the engineering instead of the announcement.",
        "hr_hdr": ["Subject in the list", "Where it is worked out here"],
        "hr_rows": [
            ("IEC 61131-10 and PLC portability",
             '<a href="%(p)scontrol.html#platform">control.html#platform</a> — the five languages '
             'were standardised, the file was not'),
            ("PID gap control, noise and setpoint gap",
             '<a href="%(p)scontrol.html#deadtime">control.html#deadtime</a> — the other clamp on '
             'controller gain, and the accepted loss'),
            ("PID tuning from first principles",
             '<a href="%(p)scontrol.html#tuning">control.html#tuning</a> — the methods compared, '
             'with a simulator that has no noise source'),
            ("Software-defined control",
             '<a href="%(p)sadvanced/#sdc">advanced/#sdc</a> — four benefits, split into two '
             'engineering claims and two procurement claims'),
            ("Industry 4.0 and the data fabric",
             '<a href="%(p)sadvanced/#i40">advanced/#i40</a> — the springboard, and the silo it '
             'has not removed'),
            ("DCS migration and the total-plant layer stack",
             '<a href="%(p)sadvanced/#plant">advanced/#plant</a> — where a migration decision '
             'actually sits'),
            ("Zero trust, OT security and which standard applies",
             '<a href="%(p)ssafety.html#sil">safety.html#sil</a> — 61508 as the umbrella, and '
             'NIS2 as a legal requirement'),
            ("Simulation and the response of a real loop",
             '<a href="%(p)scontrol.html#sim">control.html#sim</a> — dead time, gain and what a '
             'model has to admit'),
        ],
        "src_h": "Sources",
        "src_note": "Every monthly post linked above, plus the Control Engineering research "
                    "roundup for 2025, which appears as an article in its own right in February.",
        "foot_prev": "Video library",
        "foot_next": "Fundamentals of measurement",
        "foot_note": "A bilingual field guide to process instrumentation and control. "
                     "Quotations are attributed; commentary is this site's own.",
        "foot_built": "Static site · no build step · EN / VI",
    },
    "vi": {
        "title": "Chủ đề nóng — một năm ngành đọc gì | Đo lường &amp; Điều khiển",
        "desc": "Mười hai tháng danh sách bài đọc nhiều nhất của Control Engineering gom về một "
                "chỗ: những bài giữ được sự chú ý suốt năm, những chủ đề cứ quay lại, và năm "
                "tháng bản lưu không có.",
        "skip": "Chuyển đến nội dung",
        "kicker": "Báo ngành",
        "h1": "Ngành thực sự đã đọc gì",
        "lede": "Mỗi tháng Control Engineering công bố mười bài được đọc nhiều nhất, xếp theo lượt "
                "xem. Một danh sách là ảnh chụp sự chú ý của một tuần. Mười hai danh sách nối lại "
                "cho thấy chủ đề nào cứ quay về — và chủ đề nào chỉ có vẻ quan trọng trong tuần nó "
                "được đăng.",
        "toc": [
            ("method", "Cách lập danh sách"),
            ("months", "Các tháng"),
            ("reading", "Một năm nói lên gì"),
            ("press", "Tờ báo còn lại"),
            ("here", "Đọc tiếp ở đây"),
        ],
        "lang_other": "EN",
        "lang_href": "../../hot-topics/",
        "nav_active": "hot-topics/",

        "eb_1": "Phương pháp",
        "m_h": "Danh sách này được lập thế nào",
        "m_p1": "Nguồn là bài <em>hot topics</em> hằng tháng trên controleng.com. Thứ hạng là lượt "
                "xem Google Analytics của tháng đó, nên danh sách đo sự chú ý chứ không đo giá "
                "trị: một thông cáo nhà cung cấp với tiêu đề hấp dẫn có thể xếp trên một bài "
                "hướng dẫn cẩn thận, và một bài hai năm tuổi mà công cụ tìm kiếm vẫn phục vụ có "
                "thể hiện ra cạnh tin của tuần trước.",
        "m_p2": "Nội dung được lấy từ bản lưu của các bài đó, vì trang gốc từ chối truy vấn tự "
                "động. Tiêu đề và tóm tắt là của nhà xuất bản, được dịch; câu nhận định dưới mỗi "
                "tiêu đề tháng là của site này, và nói tháng đó trông ra sao khi đã nhìn các "
                "tháng khác.",
        "m_note_h": "Bản lưu không có đủ mười hai tháng",
        "m_note_p": "Control Engineering không phải tháng nào cũng đăng danh sách, và Wayback "
                    "Machine không phải lúc nào cũng lưu được những tháng có đăng. Năm trong mười "
                    "hai tháng của cửa sổ này hoàn toàn không có bài lưu — tháng 3 đến tháng "
                    "7/2026 — và bài tháng 8/2026 mang tiêu đề <em>tháng 6/2026</em> vì nó gộp "
                    "tháng 6 và tháng 7. Tháng 10/2025 chỉ còn bốn trong mười vị trí, tháng "
                    "11/2025 còn tám. Một năm lẽ ra có 120 vị trí; chỉ tồn tại 62. Không có chỗ "
                    "nào bên dưới được ước lượng để lấp chỗ trống.",
        "cov_legend": "Mức độ lưu trữ, mới nhất trước",
        "cov_full": "đầy đủ",
        "cov_partial": "lưu một phần",
        "cov_gap": "không có bài lưu",
        "earlier_k": "Trước cửa sổ khảo sát",
        "earlier_p": "Bản lưu cũng còn những tháng này; chỉ dẫn liên kết, không in lại:",

        "eb_2": "Bản ghi",
        "mo_h": "Bảy tháng, sáu mươi hai vị trí",
        "mo_p": "Mới nhất trước, đúng như khi công bố. Thứ hạng là của nhà xuất bản; ở tháng thiếu, "
                "số thứ tự nhảy, và được giữ nguyên như vậy thay vì đánh số lại.",
        "mo_src": "Bài gốc",
        "mo_full": "đủ 10",
        "mo_partial": "một phần",

        "eb_3": "Đọc cả năm",
        "rd_h": "Mười hai tháng danh sách đọc nhiều thực sự cho thấy gì",
        "obs": [
            ("Một nửa danh sách là chín bài được đếm hai lần",
             "Sáu mươi hai vị trí rút lại còn năm mươi ba bài khác nhau. Chín bài được đọc đủ "
             "nhiều trong một tháng để tháng sau xuất hiện lại: bài về điều khiển khoảng PID, bài "
             "về năm lầm tưởng mô phỏng, khảo sát AI công nghiệp, bài C++ cho điều khiển chuyển "
             "động, bài nhập môn kỹ thuật phần mềm điều khiển, lập luận zero trust, thông báo "
             "System Integrator of the Year cùng chân dung Thermo Systems, và tòa nhà sản xuất "
             "của Đại học Bang Arizona. Một danh sách đọc nhiều là cửa sổ trượt, không phải mẫu "
             "mới."),
            ("Một loạt bài hướng dẫn chiếm một phần sáu của năm",
             "Bốn trong sáu mươi hai vị trí thuộc về một chuyên mục: <em>PID spotlight</em>, phần "
             "22 vào tháng 1 và phần 30, 31 vào tháng 8 và tháng 9. Chín kỳ trong tám tháng, và "
             "độc giả theo hết. Không có gì khác trong năm — không ra mắt sản phẩm, không thương "
             "vụ, không giải thưởng — lặp lại được như vậy. Bài học hơi khó chịu cho ai nghĩ báo "
             "ngành sống bằng tin: thứ hút người đọc bền nhất là một kỹ sư đang làm việc, giải "
             "thích từng cơ chế một."),
            ("Bài giải thưởng chiếm một phần sáu danh sách",
             "Mười trong sáu mươi hai vị trí là thông báo giải thưởng hoặc chân dung người được "
             "vinh danh: System Integrator of the Year năm lần, Engineering Leaders Under 40 bốn "
             "lần, Integrator Giants một lần. Tháng 12, ba vị trí đầu là cùng một giải — thông "
             "báo, rồi hai chân dung theo hạng doanh thu — nên danh sách tháng đó thực chất là "
             "top 8. Đây không phải lời phàn nàn về nhà xuất bản; đó là cách độc giả hành xử. "
             "Người ta đọc về đồng nghiệp và về dự án của đối thủ trước khi đọc về một chiến lược "
             "điều khiển."),
            ("An ninh là chủ đề duy nhất không rời đi, và giọng điệu đã đổi",
             "Năm vị trí trong bốn tháng: zero trust trên sàn nhà máy vào tháng 12 và lặp lại "
             "tháng 1, một bộ giải pháp OT của nhà cung cấp tháng 12, một podcast về tấn công "
             "mạng biến thành tấn công vật lý tháng 2, và một khung an toàn cho AI vật lý tháng "
             "10. Lập luận đã chuyển từ <em>khung IT không hợp với OT</em> sang <em>hậu quả giờ "
             "là cơ học</em>. Đó cũng là dịch chuyển mà trang an toàn của site này ghi lại, nơi "
             "NIS2 và Cyber Resilience Act biến an ninh từ một quyết định dự án thành một nghĩa "
             "vụ pháp lý."),
            ("Di trú là nơi có tiền",
             "Chỉ riêng tháng 11 đã có di trú DCS ở vị trí ba, rủi ro tích hợp brownfield ở vị "
             "trí tám và nâng cấp hệ điều khiển ở vị trí mười — ba bài mô tả cùng một quyết định "
             "từ ba góc. Không ai đọc về một vòng điều khiển mới; ai cũng đọc về lần nâng cấp mà "
             "họ sắp phải biện minh."),
            ("Điều không có trong danh sách",
             "Không có tiêu chuẩn an toàn chức năng. Không có hiệu chuẩn. Không có thẩm tra SIL, "
             "không có chu kỳ kiểm chứng, không có tính toán tấm orifice. Ngoài loạt PID, gần như "
             "không có toán vòng điều khiển nào. Danh sách đọc nhiều không phải đề cương, và "
             "chính phần vắng mặt mới hữu ích: những chủ đề quyết định nhà máy có vận hành an "
             "toàn hay không được đọc bởi một nhóm nhỏ, cụ thể, từng người một, không phải hàng "
             "chục nghìn. Khoảng trống đó là lý do các trang kỹ thuật ở đây dài hơn một bài báo "
             "ngành và ngắn hơn một tiêu chuẩn."),
        ],
        "rd_close": "Hãy đọc những danh sách này như tín hiệu thị trường, không như đề cương. Điều "
                    "ngành tò mò trong năm nay là kiến trúc, an ninh, nghề nghiệp và cái giá của "
                    "việc đứng yên. Điều ngành không tò mò — ít nhất là không công khai — là phần "
                    "số học bên trong vòng điều khiển.",

        # 04 press
        "eb_4": "Nhà xuất bản thứ hai",
        "pr_h": "Tờ tạp chí còn lại, và một cách đo khác",
        "pr_p1": "Control Engineering xếp theo lượt xem. Automation.com Monthly không có bảng như "
                "vậy: một số báo là tập bài mà biên tập viên đặt làm, và thứ tự của nó là thứ tự "
                "trên trang. In lại những tiêu đề đó thành một top 10 thứ hai sẽ là bịa ra một thứ "
                "hạng không tồn tại, nên chúng được liệt kê ở đây không xếp hạng, theo từng số — và "
                "chính sự khác biệt đó mới đáng nói: một danh sách đo điều độc giả chọn, danh sách "
                "kia đo điều biên tập viên cho là nên đọc.",
        "pr_p2": "Tám số được dùng, từ tháng 6–7/2025 đến tháng 10/2026. Nguồn đánh dấu một số thẻ "
                "là <em>Sponsored By</em> kèm tên đơn vị; đó là quảng cáo nên được loại, cùng với "
                "thư tòa soạn và mục điểm tin. Phần còn lại là lõi biên tập của mỗi số, kèm tóm tắt "
                "của chính nguồn dưới mỗi tiêu đề.",
        "pr_note_h": "Vì sao ở đây không có InTech",
        "pr_note_p": "InTech là tạp chí của ISA và đã dừng ở số tháng 10/2024 — hai năm gần nhất của "
                    "nó không tồn tại để sưu tầm. Các số 2025 trên automation.com phần lớn là bài "
                    "InTech do ISA bảo trợ, và những thẻ đó bị loại theo cùng quy tắc với bài của "
                    "nhà cung cấp. Không có nội dung nào ở đây lấy từ isa.org: điều khoản của hiệp "
                    "hội không cho phép đưa tài liệu của họ vào một mô hình.",
        "pr_items": "bài",
        "pr_src": "Trang số báo",

        # 05 here
        "eb_5": "Trên site này",
        "hr_h": "Những chủ đề này được đi sâu ở đâu",
        "hr_p": "Cùng những câu chuyện đó, đi tới chỗ kỹ thuật thay vì dừng ở thông cáo.",
        "hr_hdr": ["Chủ đề trong danh sách", "Được làm rõ ở đây"],
        "hr_rows": [
            ("IEC 61131-10 và tính khả chuyển của PLC",
             '<a href="%(p)scontrol.html#platform">control.html#platform</a> — năm ngôn ngữ đã '
             'được chuẩn hóa, tệp thì không'),
            ("Điều khiển khoảng PID, nhiễu và khoảng đặt",
             '<a href="%(p)scontrol.html#deadtime">control.html#deadtime</a> — chốt chặn còn lại '
             'lên hệ số khuếch đại, và mất mát được chấp nhận'),
            ("Hiệu chỉnh PID từ nguyên lý",
             '<a href="%(p)scontrol.html#tuning">control.html#tuning</a> — các phương pháp so sánh '
             'cạnh nhau, kèm bộ mô phỏng không có nguồn nhiễu'),
            ("Điều khiển định nghĩa bằng phần mềm",
             '<a href="%(p)sadvanced/#sdc">advanced/#sdc</a> — bốn lợi ích, tách thành hai tuyên '
             'bố kỹ thuật và hai tuyên bố mua sắm'),
            ("Industry 4.0 và lớp dữ liệu",
             '<a href="%(p)sadvanced/#i40">advanced/#i40</a> — bàn đạp, và cái silo nó chưa dỡ '
             'được'),
            ("Di trú DCS và chồng tầng toàn nhà máy",
             '<a href="%(p)sadvanced/#plant">advanced/#plant</a> — quyết định di trú thực sự nằm ở '
             'đâu'),
            ("Zero trust, an ninh OT và tiêu chuẩn nào được viện dẫn",
             '<a href="%(p)ssafety.html#sil">safety.html#sil</a> — 61508 là ô che, và NIS2 là '
             'nghĩa vụ pháp lý'),
            ("Mô phỏng và đáp ứng của một vòng thực",
             '<a href="%(p)scontrol.html#sim">control.html#sim</a> — thời gian chết, hệ số '
             'khuếch đại và điều một mô hình phải thừa nhận'),
        ],
        "src_h": "Nguồn",
        "src_note": "Mọi bài hằng tháng được liên kết ở trên, cùng bản tổng hợp nghiên cứu 2025 "
                    "của Control Engineering — xuất hiện như một bài độc lập vào tháng 2.",
        "foot_prev": "Thư viện video",
        "foot_next": "Cơ bản về đo lường",
        "foot_note": "Sổ tay song ngữ về thiết bị đo và điều khiển quá trình. Trích dẫn đều ghi "
                     "nguồn; phần bình luận là của site này.",
        "foot_built": "Trang tĩnh · không cần build · EN / VI",
    },
}


def page_url(lang):
    return BASE + ("/vi/hot-topics/" if lang == "vi" else "/hot-topics/")


def head(lang, prefix):
    t = T[lang]
    css = prefix + "assets/style.css?v=%s" % framework.ASSET_VER
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
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
                     "name": "Hot topics" if lang == "en" else "Chủ đề nóng",
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
<link rel="alternate" hreflang="en" href="%(base)s/hot-topics/">
<link rel="alternate" hreflang="vi" href="%(base)s/vi/hot-topics/">
<link rel="alternate" hreflang="x-default" href="%(base)s/hot-topics/">
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
    nav_html = "\n      ".join(
        '<a class="%s" href="%s">%s</a>' % (cls, href, label)
        for cls, href, label in framework.nav_links(lang, prefix, active)
    )
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


def hero(lang, prefix):
    t = T[lang]
    toc = "".join('<li><a href="#%s">%s</a></li>' % (a, l) for a, l in t["toc"])
    return """<section class="sec adv-hero">
  <div class="wrap">
    <div class="eyebrow"><span class="num">00</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h1 class="adv-h1">%s</h1>
    <p class="lede adv-lede">%s</p>
    <ul class="hot-cov">%s</ul>
  </div>
</section>
""" % (t["kicker"], t["h1"], t["lede"], toc)


def method(lang, prefix):
    t = T[lang]
    chips = []
    for ym, en, vi, state, slug in hot_data.COVERAGE:
        label = en if lang == "en" else vi
        if slug:
            chips.append('<li><a class="is-%s" href="#%s">%s</a></li>' % (state, slug, label))
        else:
            chips.append('<li><span class="is-%s" title="%s">%s</span></li>'
                         % (state, t["cov_gap"], label))
    earlier = " ".join(
        '<a href="%s" rel="noopener">%s</a>' % (href, en if lang == "en" else vi)
        for en, vi, href in hot_data.EARLIER
    )
    return """<section class="sec adv-sec" id="method">
  <div class="wrap">
    <div class="eyebrow"><span class="num">01</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p1)s</p>
    <p class="adv-p">%(p2)s</p>
    <div class="adv-note">
      <b>%(nh)s</b>
      <p>%(np)s</p>
    </div>
    <h3 class="adv-h3">%(legend)s</h3>
    <ul class="hot-cov">%(chips)s</ul>
    <p class="hot-earlier"><span class="k">%(ek)s</span>%(ep)s %(earlier)s</p>
  </div>
</section>
""" % {
        "eb": t["eb_1"],
        "h": t["m_h"],
        "p1": t["m_p1"],
        "p2": t["m_p2"],
        "nh": t["m_note_h"],
        "np": t["m_note_p"],
        "legend": t["cov_legend"],
        "chips": "".join(chips),
        "ek": t["earlier_k"],
        "ep": t["earlier_p"],
        "earlier": earlier,
    }


def month_block(lang, m):
    t = T[lang]
    items = []
    for it in m["items"]:
        items.append(
            '<li><span class="hot-n">%d</span><div>'
            '<a class="hot-t" href="%s" rel="noopener">%s</a>'
            '<span class="hot-b">%s</span></div></li>'
            % (it["n"], it["href"], it["t_" + lang], it["b_" + lang])
        )
    n = len(m["items"])
    if n == 10:
        badge = '<span class="hot-count">%s</span>' % t["mo_full"]
    else:
        badge = '<span class="hot-count warn">%d / 10 &middot; %s</span>' % (n, t["mo_partial"])
    return """  <section class="hot-month" id="%(slug)s">
    <div class="wrap">
      <div class="hot-mh">
        <h2>%(name)s</h2>
        %(badge)s
        <a class="hot-src" href="%(src)s" rel="noopener">%(src_label)s &rarr;</a>
      </div>
      <p class="hot-angle">%(angle)s</p>
      <ol class="hot-list">%(items)s</ol>
    </div>
  </section>
""" % {
        "slug": m["slug"],
        "name": m["en"] if lang == "en" else m["vi"],
        "badge": badge,
        "src": m["src"],
        "src_label": t["mo_src"],
        "angle": m["angle_" + lang],
        "items": "".join(items),
    }


def months(lang, prefix):
    t = T[lang]
    body = "".join(month_block(lang, m) for m in hot_data.MONTHS)
    return """<section class="sec adv-sec" id="months" style="padding-bottom:0">
  <div class="wrap">
    <div class="eyebrow"><span class="num">02</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p)s</p>
  </div>
%(body)s
</section>
""" % {"eb": t["eb_2"], "h": t["mo_h"], "p": t["mo_p"], "body": body}


def reading(lang, prefix):
    t = T[lang]
    parts = []
    for h, p in t["obs"]:
        parts.append('    <h3 class="adv-h3">%s</h3>\n    <p class="adv-p">%s</p>' % (h, p))
    return """<section class="sec adv-sec" id="reading">
  <div class="wrap">
    <div class="eyebrow"><span class="num">03</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
%(obs)s
    <p class="adv-p adv-close">%(close)s</p>
  </div>
</section>
""" % {"eb": t["eb_3"], "h": t["rd_h"], "obs": "\n".join(parts), "close": t["rd_close"]}


def press(lang, prefix):
    """The second publisher. Unranked on purpose: an issue has an order, not a rank."""
    t = T[lang]
    blocks = []
    for iss in hot_data.PRESS:
        items = "".join(
            '<li><div><a class="hot-t" href="%s" rel="noopener">%s</a>'
            '<span class="hot-b">%s</span></div></li>'
            % (it["href"], it["t_" + lang], it["b_" + lang])
            for it in iss["items"]
        )
        blocks.append("""  <section class="hot-press" id="%s">
    <div class="wrap">
      <div class="hot-mh">
        <h3>%s</h3>
        <span class="hot-count">%d %s</span>
        <a class="hot-src" href="%s" rel="noopener">%s &rarr;</a>
      </div>
      <p class="hot-angle">%s</p>
      <ul class="hot-list hot-plain">%s</ul>
    </div>
  </section>
""" % (iss["slug"], iss["en"] if lang == "en" else iss["vi"], len(iss["items"]),
       t["pr_items"], iss["src"], t["pr_src"], iss["kicker_" + lang], items))
    return """<section class="sec adv-sec" id="press" style="padding-bottom:0">
  <div class="wrap">
    <div class="eyebrow"><span class="num">04</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p1)s</p>
    <p class="adv-p">%(p2)s</p>
    <div class="adv-note">
      <b>%(nh)s</b>
      <p>%(np)s</p>
    </div>
  </div>
%(body)s
</section>
""" % {
        "eb": t["eb_4"],
        "h": t["pr_h"],
        "p1": t["pr_p1"],
        "p2": t["pr_p2"],
        "nh": t["pr_note_h"],
        "np": t["pr_note_p"],
        "body": "".join(blocks),
    }


def here(lang, prefix):
    t = T[lang]
    rows = "".join(
        "<tr><td><strong>%s</strong></td><td>%s</td></tr>"
        % (k, v % {"p": prefix}) for k, v in t["hr_rows"]
    )
    srcs = "".join(
        '<li><span class="tag">%s</span><a href="%s" rel="noopener">%s</a></li>'
        % (("Monthly list" if lang == "en" else "Danh sách tháng"), m["src"],
           m["en"] if lang == "en" else m["vi"])
        for m in hot_data.MONTHS
    ) + "".join(
        '<li><span class="tag">%s</span><a href="%s" rel="noopener">%s</a></li>'
        % (("Issue" if lang == "en" else "Số báo"), i["src"],
           i["en"] if lang == "en" else i["vi"])
        for i in hot_data.PRESS
    )
    return """<section class="sec adv-sec" id="here">
  <div class="wrap">
    <div class="eyebrow"><span class="num">05</span><span class="line"></span><span class="eyebrow-label">%(eb)s</span></div>
    <h2 class="adv-h2">%(h)s</h2>
    <p class="adv-p">%(p)s</p>
    <div class="tbl-wrap"><table class="tbl adv-tbl"><thead><tr><th>%(h1)s</th><th>%(h2)s</th></tr></thead>
      <tbody>%(rows)s</tbody></table></div>
    <h3 class="adv-h3">%(src_h)s</h3>
    <ul class="adv-src">%(srcs)s</ul>
    <p class="adv-p">%(src_note)s</p>
    %(chain)s
  </div>
</section>
""" % {
        "eb": t["eb_5"],
        "h": t["hr_h"],
        "p": t["hr_p"],
        "h1": t["hr_hdr"][0],
        "h2": t["hr_hdr"][1],
        "rows": rows,
        "src_h": t["src_h"],
        "srcs": srcs,
        "src_note": t["src_note"],
        "chain": framework.nextprev_plain(lang, "hot-topics/", prefix,
                                          cls="nextprev hot-foot"),
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
    body += hero(lang, prefix)
    body += method(lang, prefix)
    body += months(lang, prefix)
    body += reading(lang, prefix)
    body += press(lang, prefix)
    body += here(lang, prefix)
    body += footer(lang, prefix)
    framework.write(path, framework.tidy(body))
    return path


def main():
    a = build_lang("en", os.path.join("hot-topics", "index.html"), "../")
    b = build_lang("vi", os.path.join("vi", "hot-topics", "index.html"), "../../")
    print("  %-28s hot topics page (en)" % a)
    print("  %-28s hot topics page (vi)" % b)


if __name__ == "__main__":
    main()
