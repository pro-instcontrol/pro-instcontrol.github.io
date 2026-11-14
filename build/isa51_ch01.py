# -*- coding: utf-8 -*-
"""ANSI/ISA-5.1 — Chapter 1: Purpose and scope (preface, §§1–2)."""
import isa51fig as F
from isa51_common import T, fig, h2, h3, lead, note, ol, p, table, ul

PAGES_SRC = 9
BYLINE = "ANSI/ISA-5.1-1984 (R1992) · ISA"
_LANG = ["vi"]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Tiêu chuẩn đồng thuận</em> — tiêu chuẩn "
        "được xây dựng bằng sự đồng thuận của nhiều bên, không phải quy định bắt buộc. · "
        "<em>Nhận dạng (identification)</em> — chuỗi chữ cái và/hoặc chữ số dùng để chỉ một "
        "thiết bị hoặc một vòng lặp. · <em>Ký hiệu (symbol)</em> — hình vẽ biểu diễn thiết bị "
        "hoặc chức năng trên sơ đồ. · <em>Vòng lặp (loop)</em> — tập hợp hai hay nhiều thiết bị "
        "truyền tín hiệu cho nhau để đo và/hoặc điều khiển.",
        "<b>Key terms.</b> <em>Consensus standard</em> — a standard developed by agreement "
        "among interested parties rather than imposed by regulation. · <em>Identification</em> "
        "— the sequence of letters and/or digits that designates one instrument or loop. · "
        "<em>Symbol</em> — the graphic that depicts an instrument or function on a diagram. · "
        "<em>Loop</em> — two or more instruments or functions passing signals between them to "
        "measure and/or control a variable.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "ANSI/ISA-5.1 là tiêu chuẩn tạo ra <em>ngôn ngữ chung</em> cho thiết bị đo và điều "
        "khiển trong công nghiệp quá trình. Chương này trình bày mục đích, phạm vi áp dụng và "
        "cách tiêu chuẩn tự định vị: một công cụ truyền thông, không phải một quy định bắt buộc.",
        "ANSI/ISA-5.1 is the standard that gives process instrumentation its <em>common "
        "language</em>. This chapter sets out its purpose, its scope, and how the document "
        "positions itself: a tool for communication, not a mandatory regulation.")))

    b.append(h2(A("Về tiêu chuẩn này", "About this standard"),
                A("Tiêu chuẩn và tiền đề", "The standard and its background")))
    b.append(p(A(
        "Tiêu chuẩn <b>ANSI/ISA-5.1-1984 (R1992) — Instrumentation Symbols and "
        "Identification</b> được tái xác nhận ngày 13 tháng 7 năm 1992; trước đó mang ký hiệu "
        "ANSI/ISA-S5.1-1984 (R1992). Tiêu chuẩn do Ủy ban SP5.1 của ISA biên soạn, với "
        "R. Mulley làm chủ tịch. Lời nói đầu (và các phụ lục, chú thích) chỉ mang tính thông "
        "tin, không phải một phần của tiêu chuẩn.",
        "<b>ANSI/ISA-5.1-1984 (R1992) — Instrumentation Symbols and Identification</b> was "
        "reaffirmed on 13 July 1992; it was formerly designated ANSI/ISA-S5.1-1984 (R1992). "
        "It was prepared by ISA Committee SP5.1, chaired by R. Mulley. The preface, footnotes "
        "and appendices are included for information only and are not part of the standard.")))
    b.append(p(A(
        "ISA xây dựng tiêu chuẩn này nhằm tiến tới sự <b>thống nhất</b> trong lĩnh vực thiết bị "
        "đo. Một cách truyền thông muốn có giá trị thực thì phải có một ngôn ngữ chung; tiêu "
        "chuẩn cung cấp nền tảng cho ngôn ngữ đó. Khi được tích hợp thành hệ thống, các ký "
        "hiệu và cách gọi tên ở đây tạo thành một ngôn ngữ chuyên biệt, cô đọng, truyền tải "
        "khái niệm, sự kiện, ý định, chỉ dẫn và tri thức về hệ thống đo lường và điều khiển.",
        "ISA prepared the standard in pursuit of <b>uniformity</b> in instrumentation. "
        "Communication presupposes a common language — or is at least greatly helped by one — "
        "and the standard supplies its foundation. Integrated into a system, its symbols and "
        "designations form a concise, dedicated language that communicates concepts, facts, "
        "intent, instructions and knowledge about measurement and control systems.")))
    b.append(note(A(
        "<b>Tiêu chuẩn đồng thuận.</b> Đây là tiêu chuẩn đồng thuận, không phải tiêu chuẩn bắt "
        "buộc. Điểm mạnh là có thể dùng rộng rãi, liên ngành; điểm yếu là thường không đủ cụ "
        "thể cho các yêu cầu riêng của từng nhóm chuyên môn. Ký hiệu và cách nhận dạng dùng "
        "làm công cụ hình thành khái niệm, công cụ thiết kế, phương tiện giảng dạy và phương "
        "tiện truyền thông trên mọi loại tài liệu kỹ thuật, mua sắm, thi công và bảo trì.",
        "<b>A consensus standard.</b> This is a consensus standard, not a mandatory one. Its "
        "strength is broad, interdisciplinary applicability; its weakness is that it is often "
        "not specific enough for the special requirements of a particular interest group. The "
        "symbols and designations serve as conceptualising aids, design tools, teaching devices "
        "and a concise means of communication on technical, engineering, procurement, "
        "construction and maintenance documents.")))

    b.append(h2(A("1 · Mục đích", "1 · Purpose"),
                A("Mục đích của tiêu chuẩn", "Purpose of the standard")))
    b.append(p(A(
        "Mục đích của tiêu chuẩn là <b>thiết lập một phương thức thống nhất để chỉ định thiết "
        "bị đo và hệ thống thiết bị đo dùng cho đo lường và điều khiển</b>. Để đạt được điều "
        "đó, tiêu chuẩn đưa ra một hệ thống chỉ định gồm hai thành phần: <em>ký hiệu</em> và "
        "<em>mã nhận dạng</em>.",
        "The purpose of the standard is to <b>establish a uniform means of designating "
        "instruments and instrumentation systems used for measurement and control</b>. To that "
        "end it presents a designation system comprising two parts: <em>symbols</em> and an "
        "<em>identification code</em>.")))
    b.append(p(A(
        "Bản sửa đổi này mở rộng ký hiệu, cách nhận dạng và định nghĩa cho những khái niệm "
        "trước đây chưa được mô tả — điển hình là <em>hiển thị/điều khiển dùng chung</em>, "
        "<em>điều khiển phân tán</em> và <em>điều khiển khả trình</em>. Các định nghĩa được "
        "nới rộng vì ở các hệ thống mới, những chức năng tương tự thường không còn gắn với một "
        "thiết bị nhận dạng riêng biệt, nhưng vẫn phải được hình thành khái niệm và được gọi "
        "tên. Phương pháp sơ đồ chức năng của SAMA được dùng để mô tả khối chức năng và ký "
        "hiệu chức năng; ký hiệu đường nhị phân mới và chữ cái đầu <b>Y</b> (biến khởi tạo "
        "dạng sự kiện / trạng thái / hiện diện) được đưa vào để phục vụ công nghiệp chế biến "
        "mẻ.",
        "This revision adds symbols, identification and definitions for concepts not previously "
        "described — notably <em>shared display/control</em>, <em>distributed control</em> and "
        "<em>programmable control</em>. Definitions were broadened because, in newer systems, "
        "equivalent functions are frequently no longer tied to a uniquely identifiable "
        "instrument yet still have to be conceptualised and named. The SAMA method of "
        "functional diagramming was adopted for function blocks and function designators; new "
        "binary line symbols and the first-letter <b>Y</b> (an initiating variable classed as "
        "an event, presence or state) were introduced for the batch-processing industries.")))

    b.append(h2(A("2 · Phạm vi áp dụng", "2 · Scope"),
                A("Phạm vi và giới hạn", "Scope and limits")))
    b.append(h3(A("2.1 · Quy định chung", "2.1 · General"),
                A("Nhu cầu khác nhau của người dùng", "Different user needs")))
    b.append(p(A(
        "Nhu cầu về thủ tục của các nhóm người dùng là khác nhau. Tiêu chuẩn thừa nhận các nhu "
        "cầu đó — miễn là chúng phù hợp với mục tiêu của tiêu chuẩn — bằng cách đưa ra <em>các "
        "phương pháp ký hiệu thay thế</em>, kèm nhiều ví dụ về cách bổ sung thông tin hoặc "
        "đơn giản hóa ký hiệu tùy ý.",
        "The procedural needs of different users differ. The standard recognises those needs, "
        "where consistent with its objectives, by providing <em>alternative symbolism "
        "methods</em>, together with examples of adding information or simplifying the "
        "symbolism as desired.")))
    b.append(p(A(
        "Ký hiệu thiết bị công nghệ <b>không</b> thuộc phạm vi tiêu chuẩn này; chúng chỉ được "
        "vẽ kèm để minh họa việc áp dụng ký hiệu thiết bị đo.",
        "Process-equipment symbols are <b>not</b> part of this standard; they appear only to "
        "illustrate applications of instrumentation symbols.")))

    b.append(h3(A("2.2 · Ngành áp dụng", "2.2 · Application to industries"),
                A("Các ngành phù hợp", "Suitable industries")))
    b.append(p(A(
        "Tiêu chuẩn phù hợp cho công nghiệp hóa chất, dầu khí, phát điện, điều hòa không khí, "
        "luyện kim và nhiều ngành công nghiệp quá trình khác. Một số lĩnh vực như thiên văn "
        "học, hàng hải và y học dùng thiết bị chuyên biệt rất khác với thiết bị quá trình "
        "công nghiệp thông thường; tiêu chuẩn không được xây dựng riêng cho các lĩnh vực đó, "
        "nhưng được kỳ vọng là đủ linh hoạt để đáp ứng nhiều nhu cầu của chúng.",
        "The standard is suitable for the chemical, petroleum, power-generation, air-"
        "conditioning and metal-refining industries, and numerous other process industries. "
        "Fields such as astronomy, navigation and medicine use highly specialised instruments "
        "quite unlike conventional industrial process instruments. No specific effort was made "
        "to meet their requirements, but the standard is expected to be flexible enough for "
        "many of their needs.")))

    b.append(h3(A("2.3 · Hoạt động áp dụng", "2.3 · Application to work activities"),
                A("Những tài liệu nào dùng tiêu chuẩn", "Which documents use it")))
    b.append(p(A(
        "Tiêu chuẩn dùng được ở bất cứ đâu cần tham chiếu tới một thiết bị hoặc một chức năng "
        "của hệ thống điều khiển, nhằm ký hiệu hóa và nhận dạng. Các trường hợp điển hình:",
        "The standard applies whenever any reference to an instrument or control-system "
        "function is required for symbolisation and identification. Typical uses:")))
    b.append(ul([
        A("Phác thảo thiết kế; ví dụ giảng dạy.", "Design sketches; teaching examples."),
        A("Bài báo kỹ thuật, tài liệu và thảo luận chuyên môn.",
          "Technical papers, literature and discussions."),
        A("Sơ đồ hệ thống thiết bị đo, sơ đồ vòng lặp, sơ đồ logic.",
          "Instrumentation system diagrams, loop diagrams, logic diagrams."),
        A("Mô tả chức năng.", "Functional descriptions."),
        A("Sơ đồ dòng: công nghệ, cơ khí, kỹ thuật, hệ thống, đường ống (P&ID).",
          "Flow diagrams: process, mechanical, engineering, systems, piping and instrumentation."),
        A("Bản vẽ thi công; chỉ dẫn kỹ thuật, đơn đặt hàng, bảng kê và các danh mục khác.",
          "Construction drawings; specifications, purchase orders, manifests and other lists."),
        A("Nhận dạng (gắn thẻ) thiết bị và chức năng điều khiển.",
          "Identification (tagging) of instruments and control functions."),
        A("Hướng dẫn, bản vẽ và hồ sơ lắp đặt, vận hành, bảo trì.",
          "Installation, operating and maintenance instructions, drawings and records."),
    ]))
    b.append(p(A(
        "Mục tiêu là: bất kỳ ai có kiến thức quá trình ở mức hợp lý, khi đọc một tài liệu mô "
        "tả đo lường và điều khiển quá trình, đều hiểu được quá trình được đo và điều khiển "
        "bằng cách nào — <b>không cần</b> kiến thức chuyên sâu của chuyên gia thiết bị đo.",
        "The intent is that anyone with a reasonable amount of process knowledge who reviews a "
        "document depicting process measurement and control can understand how the process is "
        "measured and controlled — <b>without</b> the detailed knowledge of an instrumentation "
        "specialist.")))

    b.append(h3(A("2.4–2.6 · Mức độ chi tiết", "2.4–2.6 · Extent of detail"),
                A("Phạm vi nhận dạng", "How far identification goes")))
    b.append(ul([
        A("<b>2.4</b> · Áp dụng cho mọi lớp thiết bị đo và điều khiển quá trình — không chỉ "
          "thiết bị rời rạc mà cả các chức năng tương đương trong hệ thống gọi là hiển thị "
          "dùng chung, điều khiển dùng chung, điều khiển phân tán, điều khiển bằng máy tính.",
          "<b>2.4</b> · Applicable to all classes of process measurement and control "
          "instrumentation — not only discrete instruments but also the analogous functions of "
          "systems termed shared display, shared control, distributed control and computer control."),
        A("<b>2.5</b> · Tiêu chuẩn nhận dạng và ký hiệu hóa các <em>chức năng then chốt</em> "
          "của thiết bị. Chi tiết hơn nên nằm trong tiêu chuẩn kỹ thuật, phiếu dữ liệu hoặc "
          "tài liệu dành cho người cần chi tiết đó.",
          "<b>2.5</b> · The standard identifies and symbolises the <em>key functions</em> of an "
          "instrument. Finer detail belongs in a specification, data sheet or other document "
          "intended for those who need it."),
        A("<b>2.6</b> · Tiêu chuẩn bao phủ việc nhận dạng một thiết bị và mọi thiết bị/chức "
          "năng khác cùng vòng lặp. Người dùng tự do bổ sung nhận dạng theo số serial, số tổ "
          "máy, số khu vực, số nhà máy hoặc cách khác.",
          "<b>2.6</b> · The standard covers the identification of an instrument and of all "
          "other instruments or control functions associated with it in a loop. The user is "
          "free to add identification by serial number, unit, area, plant or other means."),
    ]))

    b.append(h2(A("Cấu trúc của toàn bộ tiêu chuẩn", "How the standard is organised"),
                A("Bản đồ các điều khoản", "Map of the clauses")))
    b.append(table(
        [A("Điều", "Clause"), A("Nội dung", "Subject"), A("Chương của bản dịch", "Reader chapter")],
        [
            [A("1–2", "1–2"), A("Mục đích và phạm vi", "Purpose and scope"), A("Chương 1", "Chapter 1")],
            [A("3", "3"), A("Định nghĩa", "Definitions"), A("Chương 2", "Chapter 2")],
            [A("4", "4"), A("Khái quát hệ thống nhận dạng; Hình 1", "Outline of the identification system; Figure 1"), A("Chương 3", "Chapter 3")],
            [A("5.1–5.2", "5.1–5.2"), A("Chú thích và Bảng 1 — chữ cái nhận dạng", "Notes and Table 1 — identification letters"), A("Chương 4", "Chapter 4")],
            [A("5.3–5.4", "5.3–5.4"), A("Bảng 2, Bảng 3 — tổ hợp chữ và khối chức năng", "Tables 2 and 3 — letter combinations and function blocks"), A("Chương 5", "Chapter 5")],
            [A("6.1–6.8", "6.1–6.8"), A("Bản vẽ: ký hiệu đường, thiết bị, van, cơ cấu chấp hành, phần tử sơ cấp", "Drawings: line, instrument, valve, actuator and primary-element symbols"), A("Chương 6", "Chapter 6")],
            [A("6.9–6.12", "6.9–6.12"), A("Bản vẽ: ví dụ chức năng, tổ hợp, mức độ chi tiết", "Drawings: function examples, combinations, degree of detail"), A("Chương 7", "Chapter 7")],
        ],
        A("Bản đồ các điều khoản của ANSI/ISA-5.1-1984 (R1992) và chương tương ứng trong bản dịch.",
          "Clause map of ANSI/ISA-5.1-1984 (R1992) and the corresponding chapter of this translation.")))
    b.append(p(A(
        "Hai chương cuối tái tạo <b>toàn bộ 37 tờ ký hiệu</b> của điều 6 dưới dạng vector: "
        "không phải ảnh chụp màn hình, mà là các đường vẽ được chuyển đổi trực tiếp từ lệnh "
        "vẽ của tệp PDF nguồn, nên phóng to vẫn sắc nét.",
        "The last two chapters reproduce <b>all 37 symbol sheets</b> of clause 6 as true "
        "vectors — not screenshots, but paths converted directly from the source PDF's drawing "
        "operators, so they stay sharp at any zoom.")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
