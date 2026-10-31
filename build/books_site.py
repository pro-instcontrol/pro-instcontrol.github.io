"""Generate /books/ and /vi/books/ — the library index in the taichikb style.

Reads library/catalog.json (194 works) and writes static HTML.
"""
import os, json, html, re, datetime, hashlib, unicodedata
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
CAT = os.path.join(ROOT, "library", "catalog.json")

# PDFs are hosted as GitHub Release assets (repo is too small for ~2 GB).
RELEASE_TAG = "library-pdfs"
RELEASE_BASE = ("https://github.com/pro-instcontrol/pro-instcontrol.github.io"
                "/releases/download/" + RELEASE_TAG + "/")
PDF_ROOT = "D:/Process Control and Automation"

# --- keep only English / Vietnamese works -------------------------------
_FOREIGN = re.compile(
    r"\b(impianti|impianto|regolazione|termici|impiantistica|anàlisi|"
    r"automatització|aplicacions|pràctiques|exercicis|mètodes|instrumentació|"
    r"interferències|autòmats|descripció|dels|amb|diseño|elementos|estudio|"
    r"automatismos|eléctricos|regulación|fórmulas|simbología|messtechnik|"
    r"regelung|régulation|mesure|automatique)\b", re.I)


def is_foreign(w):
    """True for clearly non-English / non-Vietnamese catalogue works.

    The catalogue is English with a Vietnamese translation layer; the only
    foreign titles are Catalan / Spanish / Italian / Korean imports.
    """
    t = w.get("title") or ""
    if _FOREIGN.search(t):
        return True
    # Italian "IMPIANTI INDUSTRIALI/x impianti" subfolder (English works can
    # sit directly under IMPIANTI INDUSTRIALI, so match the subfolder only).
    for d in w.get("docs", []):
        p = d.get("path") or ""
        if re.search(r"(^|/)x impianti/", p, re.I) or re.search(r"/impianti/", p, re.I):
            return True
    for ch in t:
        if ord(ch) > 127 and unicodedata.category(ch).startswith("L"):
            return True
    return False


def pdf_asset_name(path):
    """Deterministic, collision-safe release-asset filename for a PDF path."""
    h = hashlib.sha1(path.encode("utf-8")).hexdigest()[:16]
    base = os.path.basename(path).rsplit(".", 1)[0]
    slug = re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-")[:40] or "doc"
    return "%s__%s.pdf" % (slug, h)


def pdf_url(path):
    return RELEASE_BASE + pdf_asset_name(path)

# ---------------------------------------------------------------- shelves
# eight shelves, each grouping several catalogue domains
SHELVES = [
    ("measurement", "Measurement & Sensors", "Đo lường & Cảm biến",
     "Instrumentation, sensing elements, flow and analysis — the front end of every loop.",
     "Thiết bị đo, phần tử cảm biến, lưu lượng và phân tích — đầu vào của mọi vòng điều khiển.",
     ["instruments", "sensors", "flow", "analyzers"], "#9a3412"),
    ("control", "Control & Theory", "Điều khiển & Lý thuyết",
     "Feedback theory, PID practice and the final element that actually moves the process.",
     "Lý thuyết hồi tiếp, thực hành PID và phần tử chấp hành thực sự tác động lên quá trình.",
     ["theory", "process", "valves"], "#0f766e"),
    ("systems", "Automation & Systems", "Tự động hóa & Hệ thống",
     "PLCs, DCS and SCADA, industrial networks, wiring practice and plant software.",
     "PLC, DCS và SCADA, mạng công nghiệp, thực hành đấu dây và phần mềm nhà máy.",
     ["plc", "dcs", "networks", "automation", "electrical"], "#1e40af"),
    ("safety", "Safety & Power", "An toàn & Nguồn",
     "Functional safety, hazardous area, and the control of boilers and power plant.",
     "An toàn chức năng, vùng nguy hiểm, và điều khiển lò hơi cùng nhà máy điện.",
     ["safety", "power"], "#991b1b"),
    ("plant", "Plant & Machinery", "Nhà máy & Máy móc",
     "Process equipment, rotating machinery, drives and robotics.",
     "Thiết bị công nghệ, máy quay, truyền động và robot.",
     ["machinery", "equipment"], "#78350f"),
    ("foundations", "Standards & Foundations", "Tiêu chuẩn & Cơ sở",
     "Codes, symbol standards, and the science underneath the measurement.",
     "Quy chuẩn, tiêu chuẩn ký hiệu, và nền tảng khoa học bên dưới phép đo.",
     ["standards", "fundamentals"], "#374151"),
    ("courses", "Courses & Training", "Giáo trình & Đào tạo",
     "Structured teaching material: PLC courses, tutorials and university coursework.",
     "Tài liệu giảng dạy có cấu trúc: khóa PLC, bài hướng dẫn và giáo trình đại học.",
     ["training"], "#6d28d9"),
    ("press", "Magazines & Reference", "Tạp chí & Tham khảo",
     "Trade press, vendor literature and miscellany worth keeping.",
     "Báo ngành, tài liệu nhà sản xuất và các tài liệu lẻ còn giá trị.",
     ["trade", "misc"], "#525252"),
]

# ------------------------------------------------------- descriptions
# keyed by a lowercase substring of the work title -> (en, vi)
DESC = {
    "measurement, instrumentation and sensors handbook": (
        "The reference work of the field: 101 chapters by different authors, from the characteristics "
        "of instrumentation through every measured variable to signal processing and displays. "
        "Being translated into Vietnamese, chapter by chapter.",
        "Công trình tham khảo của ngành: 101 chương do nhiều tác giả viết, từ đặc tính thiết bị đo qua "
        "mọi đại lượng đo đến xử lý tín hiệu và hiển thị. Đang được dịch sang tiếng Việt theo từng chương."),
    "industrial information technology handbook": (
        "Zurawski's CRC handbook on the IT layer of industrial systems — fieldbus, middleware, "
        "agent technology and enterprise integration. Dense, academic, and still the clearest map of the stack.",
        "Sổ tay CRC của Zurawski về tầng công nghệ thông tin trong hệ công nghiệp — fieldbus, middleware, "
        "công nghệ tác tử và tích hợp doanh nghiệp. Đặc, hàn lâm, và vẫn là bản đồ rõ nhất của chồng giao thức."),
    "ip_industrial process measurement": (
        "Fifteen-part course text on industrial process measurement: sensors, transmitters, "
        "installation practice and the reasoning behind each choice.",
        "Giáo trình mười lăm phần về đo lường quá trình công nghiệp: cảm biến, transmitter, "
        "thực hành lắp đặt và lý do đằng sau mỗi lựa chọn."),
    "process industrial instruments and control handbook": (
        "McMillan and Considine's McGraw-Hill handbook. The practical American reference — "
        "how instruments behave in a plant rather than on a datasheet.",
        "Sổ tay McGraw-Hill của McMillan và Considine. Tài liệu tham khảo thực dụng kiểu Mỹ — "
        "thiết bị hành xử trong nhà máy ra sao, chứ không phải trên datasheet."),
    "instrumentation reference book 3e": (
        "Boyes' Newnes reference. Broad, well-organised, and the book most engineers actually "
        "reach for when they need one answer quickly.",
        "Sách tham khảo Newnes của Boyes. Bao quát, có tổ chức tốt, và là cuốn kỹ sư thực sự "
        "hay với tay lấy khi cần một câu trả lời nhanh."),
    "instrumentation and sensors for the food industry": (
        "Kress-Rogers on measurement in food processing, where hygiene, cleanability and "
        "certification constrain the sensor as much as the process does.",
        "Kress-Rogers về đo lường trong chế biến thực phẩm, nơi vệ sinh, khả năng làm sạch và "
        "chứng nhận ràng buộc cảm biến chặt như chính quá trình."),
    "practical instrumentation for automation and process control": (
        "A short, practical primer. Less theory than the handbooks and more of what to do on Monday morning.",
        "Sách nhập môn ngắn gọn, thực dụng. Ít lý thuyết hơn các sổ tay và nhiều việc-phải-làm hơn."),
    "doe fundamentals handbook - instrumentation and control - volume 2": (
        "US Department of Energy training handbook. Written for nuclear facility operators, "
        "which is why the explanations are unusually plain and the diagrams unusually good.",
        "Sổ tay đào tạo của Bộ Năng lượng Hoa Kỳ. Viết cho nhân viên vận hành hạt nhân, nên "
        "giải thích lạ thường mà rõ ràng và hình vẽ lạ thường mà tốt."),
    "fundamentals handbook - instrumentation and control": (
        "The DOE fundamentals series — instrumentation, control, and the physics behind them, "
        "at the level of a competent technician rather than a specialist.",
        "Bộ sách cơ bản của DOE — thiết bị đo, điều khiển và vật lý đằng sau, ở mức một kỹ thuật viên "
        "giỏi chứ không phải chuyên gia hẹp."),
    "standard isa - instrumentation symbols and identification": (
        "ISA-5.1: the symbol and tag-number standard every P&ID in the English-speaking world is drawn to. "
        "Short, and worth knowing by heart.",
        "ISA-5.1: tiêu chuẩn ký hiệu và đánh số thẻ mà mọi P&ID trong thế giới nói tiếng Anh đều vẽ theo. "
        "Ngắn, và đáng thuộc lòng."),
    "pressure relief valve engineering handbook": (
        "Sizing and selection of relief devices — the one final element that must work without power, "
        "without a signal, and without maintenance.",
        "Tính chọn và lựa chọn thiết bị xả áp — phần tử chấp hành duy nhất phải làm việc không cần điện, "
        "không cần tín hiệu và không cần bảo dưỡng."),
    "control systems - w. bolton": (
        "Bolton's undergraduate text. The clearest first pass through Laplace, transfer functions "
        "and closed-loop behaviour for someone who has not met them before.",
        "Giáo trình đại học của Bolton. Lần đầu tiên rõ ràng nhất đi qua Laplace, hàm truyền và "
        "hành vi vòng kín cho người chưa từng gặp."),
    "modern control engineering ee392": (
        "University of Washington course notes. State space, observability and pole placement, "
        "taught as engineering rather than as mathematics.",
        "Ghi chú bài giảng Đại học Washington. Không gian trạng thái, quan sát được và xếp cực, "
        "dạy như kỹ thuật chứ không như toán."),
    "automatic control systems 9th edition": (
        "Kuo's classic. The standard American undergraduate treatment, with the worked examples "
        "that make root locus and Nyquist finally click.",
        "Sách kinh điển của Kuo. Cách trình bày đại học chuẩn mực của Mỹ, với các ví dụ giải sẵn "
        "khiến quỹ đạo nghiệm và Nyquist cuối cùng cũng sáng ra."),
    "control theory and design - p. colaneri": (
        "Colaneri et al., a more rigorous European treatment — linear systems, robustness and design "
        "as one continuous argument.",
        "Colaneri và cộng sự, cách tiếp cận châu Âu chặt chẽ hơn — hệ tuyến tính, độ bền vững và "
        "thiết kế như một lập luận liền mạch."),
    "elsevier - advanced control engineering": (
        "Burns' advanced text: state-space design, optimal and adaptive control, with the plant "
        "modelling kept honest.",
        "Sách nâng cao của Burns: thiết kế không gian trạng thái, điều khiển tối ưu và thích nghi, "
        "với mô hình đối tượng được giữ trung thực."),
    "automatic flight control systems": (
        "Aerospace control, included because flight control solved redundancy, voting and "
        "fault tolerance decades before process plants did.",
        "Điều khiển hàng không, có mặt vì điều khiển bay đã giải bài toán dự phòng, bỏ phiếu và "
        "chịu lỗi trước nhà máy công nghệ hàng chục năm."),
    "practical process control": (
        "Cecil Smith on tuning and troubleshooting. The book to read when a loop misbehaves at 2 a.m. "
        "and the theory is not helping.",
        "Cecil Smith về hiệu chỉnh và xử lý sự cố. Cuốn sách để đọc khi một vòng điều khiển "
        "giở chứng lúc 2 giờ sáng và lý thuyết không giúp được gì."),
    "process control systems (shinskey)": (
        "Shinskey. Opinionated, quantitative, and right about more than most. Feedback, feedforward "
        "and the economics of control.",
        "Shinskey. Có quan điểm, định lượng, và đúng nhiều hơn phần lớn. Hồi tiếp, điều khiển "
        "bù trước và bài toán kinh tế của điều khiển."),
    "principles and practice of automatic process control": (
        "Smith and Corripio. The standard graduate-level treatment of process dynamics, "
        "controller design and the hardware that implements it.",
        "Smith và Corripio. Cách trình bày chuẩn bậc sau đại học về động học quá trình, "
        "thiết kế bộ điều khiển và phần cứng thực thi."),
    "luyben w. l.": (
        "Luyben's process modelling and simulation text — how to build a dynamic model you can "
        "actually tune against.",
        "Sách mô hình hóa và mô phỏng quá trình của Luyben — cách dựng một mô hình động "
        "mà thực sự hiệu chỉnh được."),
    "essentials of process control": (
        "A compact McGraw-Hill treatment, aimed at chemical engineers who need control to serve "
        "the process rather than the other way round.",
        "Bản trình bày McGraw-Hill cô đọng, dành cho kỹ sư hóa cần điều khiển phục vụ quá trình, "
        "chứ không phải ngược lại."),
    "pid control loop": (
        "A short working note on the PID loop: what each term does, and what goes wrong when "
        "they are tuned against each other.",
        "Ghi chú ngắn về vòng PID: mỗi thành phần làm gì, và điều gì hỏng khi chúng được "
        "hiệu chỉnh chống lại nhau."),
    "pid explained": (
        "Plain-language PID. Useful precisely because it does not assume a Laplace transform.",
        "PID bằng ngôn ngữ đơn giản. Hữu ích chính vì không giả định người đọc biết biến đổi Laplace."),
    "control valve handbook": (
        "The Fisher control valve handbook — sizing, cavitation, noise, and the actuator mechanics "
        "that decide whether the loop can actually be controlled.",
        "Sổ tay van điều khiển Fisher — tính chọn, xâm thực, tiếng ồn, và cơ cấu chấp hành "
        "quyết định vòng điều khiển có điều khiển được hay không."),
    "valve selection handbook": (
        "Zappe's engineering guide to choosing a valve for a duty, with the fluid behaviour and "
        "failure modes behind each choice.",
        "Hướng dẫn kỹ thuật của Zappe về chọn van cho một nhiệm vụ, cùng hành vi lưu chất và "
        "các kiểu hỏng đằng sau mỗi lựa chọn."),
    "flow equations for sizing control valves": (
        "ISA's sizing equations. Short, normative, and the basis for every vendor's sizing software.",
        "Các phương trình tính chọn của ISA. Ngắn, mang tính quy chuẩn, và là cơ sở cho mọi "
        "phần mềm tính chọn của nhà sản xuất."),
    "flow measurement handbook": (
        "A practical guide to flowmeter selection and installation — where most flow error is "
        "created long before the electronics see the signal.",
        "Hướng dẫn thực hành chọn và lắp đặt lưu lượng kế — nơi phần lớn sai số lưu lượng "
        "được sinh ra từ rất lâu trước khi điện tử nhìn thấy tín hiệu."),
    "flowmeter handbook": (
        "Vendor-neutral survey of flowmeter types, with the application table that makes it useful.",
        "Khảo sát trung lập các loại lưu lượng kế, kèm bảng ứng dụng khiến nó hữu ích."),
    "multiphase metering": (
        "Multiphase flow measurement for oil and gas, where the mixture is the problem and "
        "the meter is only part of the answer.",
        "Đo lưu lượng đa pha cho dầu khí, nơi hỗn hợp chính là vấn đề và đồng hồ chỉ là "
        "một phần của câu trả lời."),
    "power-plant control and instrumentation": (
        "Boiler and HRSG control from the inside: drum level, combustion, feedwater and the "
        "interlocks that keep them in order.",
        "Điều khiển lò hơi và HRSG từ bên trong: mức bao hơi, cháy, nước cấp và các khóa liên động "
        "giữ chúng đúng thứ tự."),
    "safety instrumented systems": (
        "Gruhn and Cheddie on SIS design, analysis and justification — the SIL lifecycle as "
        "engineering work rather than paperwork.",
        "Gruhn và Cheddie về thiết kế, phân tích và luận chứng SIS — vòng đời SIL như công việc "
        "kỹ thuật chứ không phải giấy tờ."),
    "exprotection global-america-basics": (
        "Explosion protection across the IEC and North American systems: zones against divisions, "
        "and why the two do not map cleanly.",
        "Bảo vệ chống nổ theo cả hệ IEC và Bắc Mỹ: zone so với division, và vì sao hai hệ "
        "không ánh xạ sạch sang nhau."),
    "inherent safety in process plant design": (
        "A VTT dissertation on measuring inherent safety by index — minimise, substitute, moderate, "
        "simplify, made quantitative.",
        "Luận án VTT về đo lường an toàn nội tại bằng chỉ số — tối thiểu hóa, thay thế, tiết chế, "
        "đơn giản hóa, được lượng hóa."),
    "industrial data communication": (
        "The book behind most fieldbus courses: physical layer, protocols, and how industrial "
        "networks differ from office networks.",
        "Cuốn sách đằng sau hầu hết các khóa fieldbus: tầng vật lý, giao thức, và mạng công nghiệp "
        "khác mạng văn phòng ở đâu."),
    "fe_fieldbus, devicenet and industrial ethernet": (
        "A structured course on fieldbus, DeviceNet and industrial Ethernet, with the wiring and "
        "termination details that decide whether it works.",
        "Giáo trình có cấu trúc về fieldbus, DeviceNet và Ethernet công nghiệp, kèm chi tiết đấu dây "
        "và kết cuối quyết định nó có chạy hay không."),
    "automation body of knowledge": (
        "ISA's Automation Body of Knowledge — the profession's own definition of what an automation "
        "engineer is expected to know, in 42 chapters.",
        "Automation Body of Knowledge của ISA — định nghĩa của chính nghề về những gì một kỹ sư "
        "tự động hóa phải biết, trong 42 chương."),
    "newnes - programmable controllers": (
        "Parr's introduction to programmable controllers, from relay logic to ladder programming, "
        "written before the field became software-first.",
        "Sách nhập môn của Parr về bộ điều khiển khả trình, từ logic relay đến lập trình ladder, "
        "viết trước khi ngành chuyển hẳn sang phần mềm."),
    "plc programming methods and applications": (
        "Programming methods with the worked examples that make ladder, function block and "
        "structured text comparable.",
        "Các phương pháp lập trình với ví dụ giải sẵn giúp so sánh được ladder, function block "
        "và structured text."),
    "1856177513 programmable logic controllers": (
        "A full PLC text from the Newnes IDC series — hardware, programming, and the industrial "
        "context the controller lives in.",
        "Giáo trình PLC đầy đủ thuộc loạt Newnes IDC — phần cứng, lập trình, và bối cảnh công nghiệp "
        "mà bộ điều khiển sống trong đó."),
    "newnes industrial control wiring guide": (
        "Mercer's wiring guide: panel layout, terminal numbering, cable schedules and the conventions "
        "that let someone else maintain your work.",
        "Hướng dẫn đấu dây của Mercer: bố trí tủ, đánh số đầu cực, bảng cáp và các quy ước "
        "để người khác bảo trì được công việc của bạn."),
    "newnes - sensors & transducers": (
        "Sinclair's introduction to sensing elements — the physics of each family, with the "
        "circuits that make them usable.",
        "Sách nhập môn của Sinclair về phần tử cảm biến — vật lý của từng họ, cùng mạch điện "
        "để dùng được chúng."),
    "design of automatic machinery": (
        "Machine design for automated production: mechanisms, indexing, and the kinematics that "
        "decide cycle time.",
        "Thiết kế máy cho sản xuất tự động: cơ cấu, phân độ, và động học quyết định thời gian chu trình."),
    "robotics designing mechanisms": (
        "Mechanism design for robots — linkages, degrees of freedom and the geometry that "
        "constrains what a machine can reach.",
        "Thiết kế cơ cấu cho robot — khâu, bậc tự do và hình học ràng buộc tầm với của máy."),
    "citectscada quickstart": (
        "A Vietnamese-language Citect SCADA quickstart — one of the few operator-interface texts "
        "in the library written for Vietnamese readers.",
        "Hướng dẫn nhanh Citect SCADA bằng tiếng Việt — một trong số ít tài liệu giao diện vận hành "
        "trong thư viện viết cho người đọc Việt."),
    "process engineering equipment handbook": (
        "A 49-part equipment handbook: vessels, exchangers, pumps, valves and the mechanical "
        "detail the instrument has to live with.",
        "Sổ tay thiết bị 49 phần: bình, thiết bị trao đổi nhiệt, bơm, van và chi tiết cơ khí "
        "mà thiết bị đo phải sống chung."),
    "fuzzy systems engineering": (
        "Fuzzy control from theory to implementation — useful where the process model is a "
        "sentence rather than an equation.",
        "Điều khiển mờ từ lý thuyết đến triển khai — hữu ích khi mô hình quá trình là một câu "
        "nói chứ không phải một phương trình."),
    "intelligent control system": (
        "Neural, fuzzy and evolutionary approaches to control, collected as a survey of what "
        "the field tried in the 1990s.",
        "Các tiếp cận nơ-ron, mờ và tiến hóa cho điều khiển, tập hợp như một khảo sát những gì "
        "ngành đã thử trong thập niên 1990."),
    "transactions vol": (
        "Omega Press Transactions — collected sensor and measurement papers, valuable mainly "
        "for the practical detail the journals left out.",
        "Transactions của Omega Press — tuyển tập bài báo về cảm biến và đo lường, giá trị chủ yếu "
        "ở chi tiết thực hành mà tạp chí bỏ qua."),
    "control magazine": (
        "Control magazine, the US process-automation trade monthly. Useful as a record of what "
        "the industry was arguing about in the mid-2000s.",
        "Tạp chí Control, nguyệt san tự động hóa quá trình của Mỹ. Hữu ích như một ghi chép về "
        "điều ngành đang tranh luận giữa thập niên 2000."),
    "foundationfb": (
        "Foundation Fieldbus whitepapers — the vendor-side argument for the protocol, in the "
        "words of the people selling it.",
        "Các whitepaper Foundation Fieldbus — lập luận từ phía nhà sản xuất cho giao thức này, "
        "bằng chính lời của người bán nó."),
}

# works with a Vietnamese translation in progress: title-substring -> (level, total, done)
TRANSLATED = {
    "measurement, instrumentation and sensors handbook": ("progress", 101, 4),
    "safety instrumented systems - design, analysis, and justification": ("progress", 16, 2),
    "pc_process control": ("progress", 14, 2),
}

HANDBOOK_SLUG = "the-measurement-instrumentation-and-sensors-handbook"

# title-substring -> reader slug (for the "open the book" card link)
BOOK_SLUG = {
    "measurement, instrumentation and sensors handbook": HANDBOOK_SLUG,
    "safety instrumented systems - design, analysis, and justification":
        "safety-instrumented-systems-design-analysis-justification",
    "pc_process control": "pc-process-control",
}


def num(n, lang):
    return format(n, ",d").replace(",", "." if lang == "vi" else ",")


def esc(s):
    return html.escape(s or "", quote=True)


def load():
    cat = json.load(open(CAT, encoding="utf-8"))
    dom = {d["id"]: d for d in cat["domains"]}
    # keep only English / Vietnamese works
    cat["works"] = [w for w in cat["works"] if not is_foreign(w)]
    works = cat["works"]
    by_shelf = {s[0]: [] for s in SHELVES}
    shelf_of = {}
    for sid, _, _, _, _, doms, _ in SHELVES:
        for d in doms:
            shelf_of[d] = sid
    for w in works:
        sid = shelf_of.get(w["domain"], "press")
        by_shelf[sid].append(w)
    for sid in by_shelf:
        by_shelf[sid].sort(key=lambda w: (-w["pages"], w["title"].lower()))
    return cat, dom, by_shelf


def describe(w, lang):
    t = w["title"].lower()
    for key, (en, vi) in DESC.items():
        if key in t:
            return en if lang == "en" else vi
    # factual fallback
    if lang == "vi":
        bits = []
        if w["ndocs"] > 1:
            bits.append("%d tệp" % w["ndocs"])
        if w["pages"]:
            bits.append("%s trang" % num(w["pages"], "vi"))
        return "Tài liệu trong thư viện — " + (", ".join(bits) if bits else "một tệp PDF") + "."
    bits = []
    if w["ndocs"] > 1:
        bits.append("%d files" % w["ndocs"])
    if w["pages"]:
        bits.append("%s pages" % num(w["pages"], "en"))
    return "Held in the library — " + (", ".join(bits) if bits else "a single PDF") + "."


def card(w, lang, dom):
    t = w["title"]
    meta_bits = [dom[w["domain"]][lang]]
    if w["pages"]:
        meta_bits.append("%s %s" % (num(w["pages"], lang), "trang" if lang == "vi" else "pages"))
    if w["ndocs"] > 1:
        meta_bits.append("%d %s" % (w["ndocs"], "tệp" if lang == "vi" else "files"))
    meta = " · ".join(meta_bits)

    flag = ""
    key = t.lower()
    for k, (level, total, done) in TRANSLATED.items():
        if k in key:
            if lang == "vi":
                lab = "🟠 Đang dịch · %d/%d chương" % (done, total)
            else:
                lab = "🟠 Translating · %d of %d chapters" % (done, total)
            flag = '<span class="translated-flag" data-level="%s">%s</span>' % (level, lab)
            break

    # Every card is clickable: translated works open the reader; all others
    # open their own catalogue detail page (books/work/<id>/).
    rslug = None
    for bk, bslug in BOOK_SLUG.items():
        if bk in key:
            rslug = bslug
            break

    if rslug:
        href = (("/vi/books/read/%s/" if lang == "vi" else "/books/read/%s/") % rslug)
        foot_lbl = "Đọc bản dịch →" if lang == "vi" else "Open the book →"
    else:
        href = (("/vi/books/work/%d/" if lang == "vi" else "/books/work/%d/") % w["id"])
        foot_lbl = "Xem chi tiết →" if lang == "vi" else "View details →"

    title_html = '<a href="%s">%s</a>' % (href, esc(t))
    footer = '<div class="card-footer"><span>%s</span></div>' % foot_lbl

    return (
        '<div class="card" data-shelf="%(sid)s" data-text="%(txt)s">'
        '<span class="card-meta">%(meta)s</span>'
        '<h3>%(title)s</h3>%(flag)s<p>%(desc)s</p>%(footer)s</div>'
        % {"sid": w["_shelf"], "txt": esc((t + " " + meta).lower()), "meta": esc(meta),
           "title": title_html, "flag": flag, "desc": esc(describe(w, lang)),
           "footer": footer}
    )


def head(lang, title, desc):
    return (
        '<!doctype html><html lang="%s"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>%s</title><meta name="description" content="%s">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
        '<link rel="stylesheet" href="/books/assets/library.css">'
        '</head><body>' % (lang, esc(title), esc(desc))
    )


def reader_slug_for(title):
    key = (title or "").lower()
    for bk, bslug in BOOK_SLUG.items():
        if bk in key:
            return bslug
    return None


def work_page(lang, w, dom):
    """Catalogue detail page for one work, so every card opens on click."""
    vi = lang == "vi"
    t = w["title"]
    domain = (dom.get(w["domain"]) or {}).get(lang, w["domain"])
    rslug = reader_slug_for(t)
    crumb_home = "/vi/books/" if vi else "/books/"
    crumb_lbl = "Sách" if vi else "Books"

    bits = [domain]
    if w.get("pages"):
        bits.append("%s %s" % (num(w["pages"], lang), "trang" if vi else "pages"))
    if w.get("ndocs", 1) > 1:
        bits.append("%d %s" % (w["ndocs"], "tệp" if vi else "files"))
    if w.get("year"):
        bits.append(str(w["year"]))
    meta = " · ".join(bits)
    desc = describe(w, lang)

    docs = w.get("docs") or []
    docs_html = ""
    pdf_btns = ""
    if docs:
        rows = []
        for d in docs:
            dtitle = d.get("title") or d.get("path") or "—"
            dpages = d.get("pages") or 0
            p = d.get("path") or ""
            rlink = ""
            if p and p.lower().endswith(".pdf"):
                u = pdf_url(p)
                rlink = (' · <a href="%s" target="_blank" rel="noopener">%s</a>'
                         ' · <a href="%s" download>%s</a>'
                         % (u, "đọc" if vi else "read", u, "tải" if vi else "download"))
            rows.append('<li><span class="t">%s</span><span class="st">%s %s%s</span></li>'
                        % (esc(dtitle), num(dpages, lang), "trang" if vi else "pages", rlink))
        docs_html = ('<h2>%s</h2><ul class="toc-list">%s</ul>'
                     % ("Tệp trong thư viện" if vi else "Files in the library",
                        "".join(rows)))
        pdf_paths = [d.get("path") for d in docs
                     if (d.get("path") or "").lower().endswith(".pdf")]
        if pdf_paths:
            u0 = pdf_url(pdf_paths[0])
            rpage = ("/vi/books/reader/?u=" if vi else "/books/reader/?u=") + quote(u0, safe="")
            pdf_btns = (
                '<p style="display:flex;gap:.7rem;flex-wrap:wrap;margin:1.1rem 0;">'
                '<a href="' + rpage + '" '
                'style="display:inline-block;padding:.55rem .95rem;border:1.5px solid #000;'
                'border-radius:6px;font-weight:600;text-decoration:none;color:#000;'
                'background:#fffdf7;">' + ("📖 Đọc PDF" if vi else "📖 Read PDF") + '</a>'
                '<a href="' + u0 + '" download '
                'style="display:inline-block;padding:.55rem .95rem;border:1.5px solid #000;'
                'border-radius:6px;font-weight:600;text-decoration:none;color:#fff;'
                'background:#000;">' + ("⬇ Tải PDF" if vi else "⬇ Download PDF") + '</a>'
                '</p>'
            )

    reader_html = ""
    if rslug:
        rhref = ("/vi/books/read/%s/" if vi else "/books/read/%s/") % rslug
        reader_html = ('<p class="lead"><a href="%s"><strong>%s</strong></a></p>'
                       % (rhref, "Mở bản dịch →" if vi else "Open the book →"))

    policy = ("<b>Cách đọc.</b> Tệp PDF được lưu trong kho phát hành của trang (GitHub Release). "
              "Bấm <b>Đọc PDF</b> để xem trong trình duyệt hoặc <b>Tải PDF</b> để lưu bản sao."
              if vi else
              "<b>About this copy.</b> The PDF is hosted in the site's GitHub Release library. "
              "Use <b>Read PDF</b> to view it in the browser, or <b>Download PDF</b> to save a copy.")

    body = (
        '<main><article class="intranet-content reader">'
        '<div class="reader-hero">'
        '<div class="breadcrumb"><a href="' + crumb_home + '">' + esc(crumb_lbl) + '</a> · '
        + esc(domain) + '</div>'
        '<h1>' + esc(t) + '</h1>'
        '<div class="meta-line">' + esc(meta) + '</div>'
        '</div>'
        '<div class="prose">'
        '<p class="lead">' + esc(desc) + '</p>'
        '<div class="note">' + policy + '</div>'
        + pdf_btns +
        reader_html +
        docs_html +
        '<div class="chapter-nav"><a href="' + crumb_home + '"><span class="k">← '
        + ("Thư viện" if vi else "Library") + '</span>'
        + esc("Tất cả sách" if vi else "All books") + '</a></div>'
        '</div></article></main>'
    )
    title = "%s · Pro InstControl %s" % (t, "Thư viện" if vi else "Library")
    other = ("/books/work/%d/" if vi else "/vi/books/work/%d/") % w["id"]
    return (head(lang, title, desc) + header(lang, switch_href=other)
            + body + footer(lang))


def build_reader(lang):
    """In-site PDF reader: embeds a PDF URL (?u=) in an iframe with fallback."""
    vi = lang == "vi"
    switch = "/books/reader/" if vi else "/vi/books/reader/"
    title = "Đọc PDF" if vi else "PDF reader"
    crumb = ('<a href="/vi/books/">Sách</a> · Đọc PDF' if vi
             else '<a href="/books/">Books</a> · PDF reader')
    note = ("Trình đọc PDF trong trang. Nếu tệp không hiển thị, hãy "
            "<a href=\"#\" id=\"open-tab\">mở trong tab mới</a>."
            if vi else
            "In-page PDF reader. If the file does not display, "
            "<a href=\"#\" id=\"open-tab\">open it in a new tab</a>.")
    js = """
(function(){
  var u = new URLSearchParams(location.search).get('u') || '';
  var frame = document.getElementById('pdf-frame');
  var msg = document.getElementById('pdf-msg');
  var openTab = document.getElementById('open-tab');
  if(!u){ msg.textContent = '%s'; frame.style.display='none'; return; }
  frame.src = 'https://docs.google.com/gview?embedded=true&url=' + encodeURIComponent(u);
  openTab.href = u; openTab.target = '_blank'; openTab.rel = 'noopener';
})();
""" % ("Chưa chỉ định tệp PDF." if vi else "No PDF specified.")
    body = (
        '<main><article class="intranet-content reader">'
        '<div class="reader-hero"><div class="breadcrumb">' + crumb + '</div>'
        '<h1>' + ("Đọc PDF" if vi else "PDF reader") + '</h1></div>'
        '<div class="prose">'
        '<p id="pdf-msg">' + note + '</p>'
        '<iframe id="pdf-frame" title="PDF" '
        'style="width:100%;height:82vh;border:1px solid #ddd;border-radius:8px;"></iframe>'
        '</div></article></main>'
        '<script>' + js + '</script>'
    )
    return (head(lang, title, title) + header(lang, switch_href=switch)
            + body + footer(lang))


MARK = ('<svg viewBox="0 0 200 200" aria-hidden="true">'
        '<circle cx="100" cy="100" r="96" fill="#fff" stroke="#000" stroke-width="4"/>'
        '<circle cx="100" cy="100" r="68" fill="none" stroke="#000" stroke-width="1.6" '
        'stroke-dasharray="1.5 9"/>'
        '<path d="M100 26 A74 74 0 0 1 174 100" fill="none" stroke="#000" stroke-width="7"/>'
        '<line x1="100" y1="100" x2="143" y2="57" stroke="#000" stroke-width="5" '
        'stroke-linecap="round"/><circle cx="100" cy="100" r="10" fill="#000"/></svg>')

NAV_EN = [("/", "Home"), ("/books/", "Books"), ("/fundamentals.html", "Fundamentals"),
          ("/instruments.html", "Instruments"), ("/install.html", "Install"),
          ("/control.html", "Control"), ("/applications.html", "Applications"),
          ("/safety.html", "Safety"), ("/tools.html", "Tools"),
          ("/comparison.html", "Comparison"), ("/geotechnical.html", "Geotech"),
          ("/standards.html", "Standards"), ("/glossary.html", "Glossary"),
          ("/education.html", "Education")]
NAV_VI = [("/?lang=vi", "Trang chủ"), ("/vi/books/", "Sách"),
          ("/fundamentals.html?lang=vi", "Cơ bản"), ("/instruments.html?lang=vi", "Thiết bị"),
          ("/install.html?lang=vi", "Lắp đặt"), ("/control.html?lang=vi", "Điều khiển"),
          ("/applications.html?lang=vi", "Ứng dụng"), ("/safety.html?lang=vi", "An toàn"),
          ("/tools.html?lang=vi", "Công cụ"), ("/comparison.html?lang=vi", "So sánh"),
          ("/geotechnical.html?lang=vi", "Địa kỹ thuật"),
          ("/standards.html?lang=vi", "Tiêu chuẩn"), ("/glossary.html?lang=vi", "Thuật ngữ"),
          ("/education.html?lang=vi", "Giáo dục")]


def header(lang, active_books=True, switch_href=None):
    nav = NAV_EN if lang == "en" else NAV_VI
    links = []
    for href, label in nav:
        cls = ' class="active"' if (active_books and href.endswith("books/")) else ""
        links.append('<a href="%s"%s>%s</a>' % (href, cls, esc(label)))
    if switch_href is None:
        switch_href = "/vi/books/" if lang == "en" else "/books/"
    if lang == "en":
        links.append('<a href="%s" class="lang-switch">VI</a>' % switch_href)
    else:
        links.append('<a href="%s" class="lang-switch">EN</a>' % switch_href)
    brand_home = "/" if lang == "en" else "/?lang=vi"
    return (
        '<header class="site-header">'
        '<a href="%s" class="brand">%s<span>Pro InstControl</span></a>'
        '<nav class="site-nav">%s</nav></header>'
        % (brand_home, MARK, "".join(links)))


def footer(lang):
    """Library pages carry no footer by design."""
    return ""


def build_index(lang):
    cat, dom, by_shelf = load()
    total = sum(len(v) for v in by_shelf.values())
    pages = sum(w["pages"] for v in by_shelf.values() for w in v)

    # stamp shelf id on works for the card filter
    for sid, ws in by_shelf.items():
        for w in ws:
            w["_shelf"] = sid

    if lang == "vi":
        title = "Thư Viện Sách Kỹ Thuật Đo Lường & Điều Khiển"
        tagline = "Sách, tiêu chuẩn và giáo trình về thiết bị đo, điều khiển quá trình và tự động hóa"
        lede = ("Danh mục %d tác phẩm trong thư viện làm việc — %s trang tài liệu kỹ thuật, "
                "xếp thành tám kệ, tìm kiếm trực tiếp, kèm bản dịch tiếng Việt đang thực hiện."
                % (total, num(pages, "vi")))
        ph = "Tìm theo tên sách, tác giả, lĩnh vực (vd: Shinskey, van điều khiển, PLC, SIL…)"
        all_lbl, jump_lbl, showing = "Tất cả", "Tới kệ:", "tác phẩm"
        empty_t, empty_p, reset = "Không tìm thấy sách", "Thử từ khóa khác hoặc bỏ bộ lọc.", "Xóa bộ lọc"
    else:
        title = "Measurement & Control Library"
        tagline = "Books, standards and course material on instrumentation and automatic control"
        lede = ("%d works held in the working library — %s pages of technical material, "
                "arranged on eight shelves with live search, plus the Vietnamese translation "
                "now under way." % (total, num(pages, "en")))
        ph = "🔍 Search titles, authors, subjects (e.g. Shinskey, control valve, PLC, SIL…)"
        all_lbl, jump_lbl, showing = "All", "Jump to:", "works"
        empty_t, empty_p, reset = "No books found", "Try another keyword or clear the filters.", "Clear filters"

    pills = ['<button class="cat-pill active" data-filter="all">%s<span class="n">%d</span></button>'
             % (esc(all_lbl), total)]
    opts = ['<option value="all">%s</option>' % esc(all_lbl)]
    for sid, en, vi, _, _, _, _ in SHELVES:
        n = len(by_shelf[sid])
        if not n:
            continue
        name = en if lang == "en" else vi
        pills.append('<button class="cat-pill" data-filter="%s">%s<span class="n">%d</span></button>'
                     % (sid, esc(name), n))
        opts.append('<option value="shelf-%s">%s (%d)</option>' % (sid, esc(name), n))

    sections = []
    for sid, en, vi, sub_en, sub_vi, _, colour in SHELVES:
        ws = by_shelf[sid]
        if not ws:
            continue
        name = en if lang == "en" else vi
        sub = sub_en if lang == "en" else sub_vi
        cards = "".join(card(w, lang, dom) for w in ws)
        sections.append(
            '<section class="section" id="shelf-%s">'
            '<div class="section-title"><h2>%s</h2><span class="sub">%s</span></div>'
            '<div class="card-grid">%s</div></section>'
            % (sid, esc(name), esc(sub), cards))

    body = (
        '<main><article class="intranet-content">'
        '<section class="hero">'
        '<span class="taiji-large">%s</span>'
        '<h1>%s</h1>'
        '<p class="tagline">%s</p>'
        '<p class="lede">%s</p>'
        '</section>'
        '<div class="library-control-bar" id="library-controls">'
        '<div class="search-input-wrapper">'
        '<span class="search-icon">⌕</span>'
        '<input type="text" id="book-search-input" placeholder="%s" autocomplete="off" spellcheck="false">'
        '<button type="button" id="search-clear-btn" style="display:none;" aria-label="clear">✕</button>'
        '</div>'
        '<div class="search-stats-bar">'
        '<span class="stats-counter"><strong id="visible-count">%d</strong> / %d %s</span>'
        '<span class="quick-jump-dropdown-wrap"><label for="category-jump-select">%s</label>'
        '<select id="category-jump-select">%s</select></span>'
        '</div>'
        '<div class="category-filter-pills">%s</div>'
        '</div>'
        '%s'
        '<div class="no-results-box" id="no-results" style="display:none;">'
        '<h3>%s</h3><p>%s</p>'
        '<button class="reset-filter-btn" id="reset-filters">%s</button></div>'
        '</article></main>'
        % (MARK, esc(title), esc(tagline), esc(lede), esc(ph),
           total, total, esc(showing), esc(jump_lbl), "".join(opts), "".join(pills),
           "".join(sections), esc(empty_t), esc(empty_p), esc(reset))
    )

    js = """
(function(){
  var cards = [].slice.call(document.querySelectorAll('.card[data-shelf]'));
  var q = document.getElementById('book-search-input');
  var clearBtn = document.getElementById('search-clear-btn');
  var pills = [].slice.call(document.querySelectorAll('.cat-pill'));
  var countEl = document.getElementById('visible-count');
  var noRes = document.getElementById('no-results');
  var sel = document.getElementById('category-jump-select');
  var filter = 'all';

  function apply(){
    var term = (q.value || '').trim().toLowerCase();
    var shown = 0;
    cards.forEach(function(c){
      var okShelf = (filter === 'all' || c.dataset.shelf === filter);
      var okText = !term || c.dataset.text.indexOf(term) >= 0;
      var ok = okShelf && okText;
      c.style.display = ok ? '' : 'none';
      if (ok) shown++;
    });
    document.querySelectorAll('.section').forEach(function(s){
      var vis = s.querySelectorAll('.card[data-shelf]:not([style*="display: none"])').length;
      s.style.display = vis ? '' : 'none';
    });
    countEl.textContent = shown;
    noRes.style.display = shown ? 'none' : 'block';
    clearBtn.style.display = term ? 'block' : 'none';
  }

  q.addEventListener('input', apply);
  clearBtn.addEventListener('click', function(){ q.value = ''; apply(); q.focus(); });
  pills.forEach(function(p){
    p.addEventListener('click', function(){
      pills.forEach(function(x){ x.classList.remove('active'); });
      p.classList.add('active');
      filter = p.dataset.filter;
      apply();
    });
  });
  document.getElementById('reset-filters').addEventListener('click', function(){
    q.value = ''; filter = 'all';
    pills.forEach(function(x){ x.classList.toggle('active', x.dataset.filter === 'all'); });
    apply();
  });
  sel.addEventListener('change', function(){
    if (sel.value === 'all') { window.scrollTo({top:0, behavior:'smooth'}); return; }
    var t = document.getElementById(sel.value);
    if (t) t.scrollIntoView({behavior:'smooth', block:'start'});
  });
})();
"""

    return (
        '<!doctype html><html lang="%s"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>%s</title>'
        '<meta name="description" content="%s">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
        '<link rel="stylesheet" href="/books/assets/library.css">'
        '</head><body>%s%s%s<script>%s</script></body></html>'
        % (lang, esc(title), esc(tagline), header(lang), body, footer(lang), js)
    )


def main():
    for lang, out in (("en", os.path.join(ROOT, "books", "index.html")),
                      ("vi", os.path.join(ROOT, "vi", "books", "index.html"))):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        page = build_index(lang)
        open(out, "w", encoding="utf-8").write(page)
        print("wrote %s  %.0f kB" % (os.path.relpath(out, ROOT), len(page) / 1024))

    # In-site PDF reader pages (EN + VI)
    for lang in ("en", "vi"):
        pair = ("vi/books/reader/index.html" if lang == "vi"
                else "books/reader/index.html")
        path = os.path.join(ROOT, *pair.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(build_reader(lang))
    print("wrote reader pages")

    # One catalogue detail page per work, so every card opens on click.
    cat, dom, _ = load()
    n = 0
    for lang in ("en", "vi"):
        for w in cat["works"]:
            pair = ("vi/books/work/%d/index.html" if lang == "vi"
                    else "books/work/%d/index.html") % w["id"]
            path = os.path.join(ROOT, *pair.split("/"))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(work_page(lang, w, dom))
            n += 1
    print("wrote %d work detail pages" % n)


if __name__ == "__main__":
    main()
