# -*- coding: utf-8 -*-
"""ANSI/ISA-5.1 — Chapter 4: Table 1, Identification letters (§§5, 5.1–5.2)."""
from isa51_common import T, h2, h3, lead, note, ol, p, table, ul

PAGES_SRC = 5
BYLINE = "ANSI/ISA-5.1-1984 (R1992) · §5, Bảng 1 / Table 1"

# Each cell is a (Vietnamese, English) pair; "" means "not defined".
# columns: letter, first-letter, modifier, readout/passive, output, modifier
ROWS = [
    ("A", ("Phân tích (5,19)", "Analysis (5,19)"), ("", ""),
     ("Báo động", "Alarm"), ("", ""), ("", "")),
    ("B", ("Đầu đốt, buồng đốt", "Burner, Combustion"),
     ("Tùy chọn người dùng (1)", "User's Choice (1)"),
     ("Tùy chọn người dùng (1)", "User's Choice (1)"),
     ("Tùy chọn người dùng (1)", "User's Choice (1)"),
     ("Tùy chọn người dùng (1)", "User's Choice (1)")),
    ("C", ("Tùy chọn người dùng (1)", "User's Choice (1)"), ("", ""), ("", ""),
     ("Điều khiển (13)", "Control (13)"), ("", "")),
    ("D", ("Tùy chọn người dùng (1)", "User's Choice (1)"),
     ("Vi phân (4)", "Differential (4)"), ("", ""), ("", ""), ("", "")),
    ("E", ("Điện áp", "Voltage"), ("", ""),
     ("Cảm biến (phần tử sơ cấp)", "Sensor (Primary Element)"), ("", ""), ("", "")),
    ("F", ("Lưu lượng", "Flow Rate"),
     ("Tỷ lệ (Fraction) (4)", "Ratio (Fraction) (4)"), ("", ""), ("", ""), ("", "")),
    ("G", ("Tùy chọn người dùng (1)", "User's Choice (1)"), ("", ""),
     ("Kính quan sát (9)", "Glass, Viewing Device (9)"), ("", ""), ("", "")),
    ("H", ("Bằng tay", "Hand"), ("", ""), ("", ""), ("", ""),
     ("Cao (7,15,16)", "High (7,15,16)")),
    ("I", ("Dòng điện", "Current (Electrical)"), ("", ""),
     ("Chỉ thị (10)", "Indicate (10)"), ("", ""), ("", "")),
    ("J", ("Công suất", "Power"), ("Quét (7)", "Scan (7)"), ("", ""), ("", ""), ("", "")),
    ("K", ("Thời gian, lịch thời gian", "Time, Time Schedule"),
     ("Tốc độ thay đổi theo thời gian (4,21)", "Time Rate of Change (4,21)"), ("", ""),
     ("Trạm điều khiển (22)", "Control Station (22)"), ("", "")),
    ("L", ("Mức", "Level"), ("", ""), ("Đèn (11)", "Light (11)"), ("", ""),
     ("Thấp (7,15,16)", "Low (7,15,16)")),
    ("M", ("Tùy chọn người dùng (1)", "User's Choice (1)"),
     ("Tức thời (4)", "Momentary (4)"), ("", ""), ("", ""),
     ("Trung gian (7,15)", "Middle, Intermediate (7,15)")),
    ("N", ("Tùy chọn người dùng (1)", "User's Choice (1)"), ("", ""),
     ("Tùy chọn người dùng (1)", "User's Choice (1)"),
     ("Tùy chọn người dùng (1)", "User's Choice (1)"),
     ("Tùy chọn người dùng (1)", "User's Choice (1)")),
    ("O", ("Tùy chọn người dùng (1)", "User's Choice (1)"), ("", ""),
     ("Lỗ tiết lưu, cản trở", "Orifice, Restriction"), ("", ""), ("", "")),
    ("P", ("Áp suất, chân không", "Pressure, Vacuum"), ("", ""),
     ("Điểm nối (thử)", "Point (Test) Connection"), ("", ""), ("", "")),
    ("Q", ("Lượng", "Quantity"), ("Tích phân, cộng dồn (4)", "Integrate, Totalize (4)"),
     ("", ""), ("", ""), ("", "")),
    ("R", ("Bức xạ", "Radiation"), ("", ""), ("Ghi (17)", "Record (17)"), ("", ""), ("", "")),
    ("S", ("Tốc độ, tần số", "Speed, Frequency"), ("An toàn (8)", "Safety (8)"),
     ("", ""), ("Công tắc (13)", "Switch (13)"), ("", "")),
    ("T", ("Nhiệt độ", "Temperature"), ("", ""), ("", ""),
     ("Truyền tín hiệu (18)", "Transmit (18)"), ("", "")),
    ("U", ("Đa biến (6)", "Multivariable (6)"), ("", ""),
     ("Đa chức năng (12)", "Multifunction (12)"),
     ("Đa chức năng (12)", "Multifunction (12)"),
     ("Đa chức năng (12)", "Multifunction (12)")),
    ("V", ("Dao động, phân tích cơ khí (19)", "Vibration, Mechanical Analysis (19)"),
     ("", ""), ("", ""), ("Van, cánh chắn, cánh gió (13)", "Valve, Damper, Louver (13)"),
     ("", "")),
    ("W", ("Khối lượng, lực", "Weight, Force"), ("", ""), ("Ống bảo vệ (Well)", "Well"),
     ("", ""), ("", "")),
    ("X", ("Chưa phân loại (2)", "Unclassified (2)"), ("Trục X", "X Axis"),
     ("Chưa phân loại (2)", "Unclassified (2)"),
     ("Chưa phân loại (2)", "Unclassified (2)"),
     ("Chưa phân loại (2)", "Unclassified (2)")),
    ("Y", ("Sự kiện, trạng thái, hiện diện (20)", "Event, State or Presence (20)"),
     ("Trục Y", "Y Axis"), ("", ""),
     ("Relay, tính toán, chuyển đổi (13,14,18)", "Relay, Compute, Convert (13,14,18)"),
     ("", "")),
    ("Z", ("Vị trí, kích thước", "Position, Dimension"), ("Trục Z", "Z Axis"), ("", ""),
     ("Cơ cấu chấp hành, phần tử chấp hành cuối chưa phân loại",
      "Driver, Actuator, Unclassified Final Control Element"), ("", "")),
]

# (Vietnamese note, English note) — the 22 notes of §5.1
NOTES = [
    ("Chữ «tùy chọn người dùng» dùng cho nghĩa chưa liệt kê nhưng lặp lại nhiều lần trong một "
     "dự án. Chữ đó có thể mang một nghĩa ở vị trí chữ đầu và nghĩa khác ở vị trí chữ tiếp "
     "theo; chỉ cần định nghĩa một lần trong bảng chú giải của dự án. Ví dụ N có thể là "
     "«mô đun đàn hồi» khi đứng đầu và «dao động ký» khi đứng sau.",
     "A «user's choice» letter covers unlisted meanings used repetitively in a particular "
     "project. It may have one meaning as a first-letter and another as a succeeding-letter; "
     "the meanings need only be defined once in a project legend. N, for example, may mean "
     "«modulus of elasticity» as a first-letter and «oscilloscope» as a succeeding-letter."),
    ("Chữ chưa phân loại <b>X</b> dùng cho nghĩa không liệt kê, chỉ xuất hiện một lần hoặc "
     "phạm vi hạn hẹp; nó có thể có nhiều nghĩa ở cả hai vị trí. Trừ khi đi với ký hiệu đặc "
     "thù, nghĩa của X nên được định nghĩa <em>bên ngoài</em> vòng tròn ký hiệu. XR-2 có thể "
     "là máy ghi ứng suất, XX-4 là dao động ký ứng suất.",
     "The unclassified letter <b>X</b> covers unlisted meanings used only once or to a limited "
     "extent; it may take any number of meanings in either position. Except with distinctive "
     "symbols, its meanings are expected to be defined <em>outside</em> a tagging bubble on a "
     "flow diagram. XR-2 may be a stress recorder, XX-4 a stress oscilloscope."),
    ("Dạng ngữ pháp của nghĩa chữ tiếp theo được phép biến đổi: «indicate» có thể đọc là "
     "indicator / indicating, «transmit» là transmitter / transmitting…",
     "The grammatical form of succeeding-letter meanings may be modified as required: "
     "«indicate» may read indicator / indicating, «transmit» transmitter / transmitting, etc."),
    ("Bất kỳ chữ đầu nào đi cùng chữ bổ nghĩa <b>D</b> (vi phân), <b>F</b> (tỷ lệ), "
     "<b>M</b> (tức thời), <b>K</b> (tốc độ thay đổi theo thời gian), <b>Q</b> (tích "
     "phân/cộng dồn), hoặc tổ hợp của chúng, đều tạo ra một <em>biến đo mới, riêng biệt</em>; "
     "cả tổ hợp được coi là một thực thể chữ đầu. Vì vậy TDI và TI chỉ hai biến khác nhau: "
     "nhiệt độ vi phân và nhiệt độ.",
     "Any first-letter combined with modifiers <b>D</b> (differential), <b>F</b> (ratio), "
     "<b>M</b> (momentary), <b>K</b> (time rate of change), <b>Q</b> (integrate/totalize) or "
     "any combination of them represents a <em>new, separate measured variable</em>, and the "
     "combination is treated as one first-letter entity. Thus TDI and TI indicate two "
     "different variables: differential temperature and temperature."),
    ("Chữ đầu <b>A</b> (phân tích) bao trùm mọi phép phân tích không do một chữ «tùy chọn "
     "người dùng» mô tả; loại phân tích cụ thể được định nghĩa bên ngoài vòng tròn ký hiệu.",
     "First-letter <b>A</b> (analysis) covers all analyses not described by a «user's choice» "
     "letter; the type of analysis is expected to be defined outside a tagging bubble."),
    ("Dùng chữ đầu <b>U</b> cho «đa biến» thay vì ghép nhiều chữ đầu là tùy chọn; nên dùng "
     "tiết chế các ký hiệu biến không cụ thể như U.",
     "Use of first-letter <b>U</b> for «multivariable» in lieu of a combination of "
     "first-letters is optional; nonspecific variable designators such as U should be used "
     "sparingly."),
    ("Các từ bổ nghĩa «cao», «thấp», «trung gian» và «quét» là tùy chọn.",
     "The modifying terms «high», «low», «middle»/«intermediate» and «scan» are optional."),
    ("Từ «an toàn» chỉ áp dụng cho phần tử sơ cấp bảo vệ khẩn cấp và phần tử chấp hành cuối "
     "bảo vệ khẩn cấp. Van tự lực xả lưu chất để giữ áp không vượt mức mong muốn vẫn là "
     "<b>PCV</b> kiểu chống áp ngược, dù van không dùng trong vận hành bình thường. Nhưng "
     "nếu van được thiết kế để bảo vệ trước điều kiện khẩn cấp (nguy hiểm cho người và/hoặc "
     "thiết bị, không dự kiến xảy ra bình thường) thì gọi là <b>PSV</b> — bất kể cấu tạo là "
     "van an toàn, van xả hay van an toàn-xả. Đĩa vỡ ký hiệu <b>PSE</b>.",
     "The term «safety» applies only to emergency protective primary elements and emergency "
     "protective final control elements. A self-actuated valve that prevents a fluid system "
     "operating above a desired pressure by bleeding fluid is a back-pressure-type <b>PCV</b>, "
     "even if not normally used. But a valve intended to protect against emergency conditions "
     "(hazardous to personnel and/or equipment, not expected to arise normally) is a <b>PSV</b> "
     "— regardless of whether its construction makes it a safety, relief or safety-relief "
     "valve. A rupture disc is <b>PSE</b>."),
    ("Chức năng thụ động <b>G</b> áp dụng cho thiết bị cho cái nhìn không hiệu chuẩn, như "
     "kính quan sát và màn hình camera.",
     "The passive function <b>G</b> applies to instruments or devices providing an "
     "uncalibrated view, such as sight glasses and television monitors."),
    ("«Chỉ thị» thường chỉ việc đọc một phép đo thực — tương tự hoặc số. Với trạm nạp tay, nó "
     "có thể chỉ mặt số hay giá trị đặt, tức giá trị của biến khởi tạo.",
     "«Indicate» normally applies to the analog or digital readout of an actual measurement. "
     "For a manual loader it may denote the dial or setting indication, i.e. the value of the "
     "initiating variable."),
    ("Đèn báo trạng thái thuộc một vòng lặp được gắn thẻ bằng một chữ đầu theo sau là chữ "
     "<b>L</b>: đèn báo hết thời gian là <b>KQL</b>. Đèn không thuộc vòng lặp cũng gắn tương "
     "tự — đèn báo động cơ đang chạy có thể là <b>EL</b> (điện áp là biến đo) hoặc <b>YL</b> "
     "(giám sát trạng thái). Không dùng <b>XL</b> cho đèn động cơ vì loại này thường rất "
     "nhiều; có thể dùng chữ tùy chọn M, N, O nếu đã định nghĩa trước (khi dùng M phải rõ là "
     "không viết tắt cho «motor» mà cho một trạng thái được giám sát).",
     "A pilot light in an instrument loop is designated by a first-letter followed by "
     "succeeding-letter <b>L</b>: a light indicating an expired time period is <b>KQL</b>. A "
     "light outside a loop is designated the same way — a motor running light may be <b>EL</b> "
     "(voltage as the measured variable) or <b>YL</b> (operating status monitored). <b>XL</b> "
     "should not be used for motor running lights because they are commonly numerous; "
     "user's-choice letters M, N or O may be used once defined (with M, make clear it stands "
     "for a monitored state, not «motor»)."),
    ("Dùng chữ tiếp theo <b>U</b> cho «đa chức năng» thay vì ghép nhiều chữ chức năng là tùy "
     "chọn; nên dùng tiết chế ký hiệu chức năng không cụ thể này.",
     "A succeeding-letter <b>U</b> for «multifunction» instead of a combination of "
     "functional letters is optional; this nonspecific designator should be used sparingly."),
    ("Một thiết bị nối, ngắt hay chuyển một hoặc nhiều mạch có thể là công tắc, relay, bộ "
     "điều khiển ON-OFF hoặc van điều khiển tùy ứng dụng. Nếu nó tác động dòng lưu chất công "
     "nghệ và không phải van chặn ON-OFF bằng tay thì là <b>van điều khiển</b>; dùng sai khi "
     "gán <b>CV</b> cho thứ không phải van điều khiển tự lực. Với các ứng dụng khác: công tắc "
     "nếu thao tác bằng tay; công tắc hoặc bộ điều khiển ON-OFF nếu tự động và là thiết bị "
     "đầu tiên trong vòng lặp («switch» thường dùng cho báo động, đèn, chọn lựa, liên khóa, "
     "an toàn; «controller» cho điều khiển vận hành bình thường); <b>relay</b> nếu tự động "
     "nhưng không phải thiết bị đầu tiên, tức bị tác động bởi công tắc hay bộ điều khiển "
     "ON-OFF.",
     "A device that connects, disconnects or transfers circuits may be a switch, relay, "
     "ON-OFF controller or control valve depending on application. If it manipulates a fluid "
     "process stream and is not a hand-actuated ON-OFF block valve, it is a <b>control valve</b>; "
     "using succeeding-letters <b>CV</b> for anything other than a self-actuated control "
     "valve is incorrect. Otherwise: a switch if hand-actuated; a switch or ON-OFF controller "
     "if automatic and the first such device in a loop («switch» for alarm, pilot light, "
     "selection, interlock or safety; «controller» for normal operating control); a "
     "<b>relay</b> if automatic but not the first such device, i.e. actuated by a switch or "
     "ON-OFF controller."),
    ("Các chức năng gắn với chữ tiếp theo <b>Y</b> cần được định nghĩa bên ngoài vòng tròn "
     "ký hiệu khi xét là cần thiết. Không cần định nghĩa khi chức năng đã tự rõ, như van "
     "điện từ trên đường tín hiệu lưu chất.",
     "Functions associated with succeeding-letter <b>Y</b> are expected to be defined outside "
     "a bubble when further definition is needed. No definition is needed when the function "
     "is self-evident, as for a solenoid valve in a fluid signal line."),
    ("Các từ bổ nghĩa «cao», «thấp», «trung gian» ứng với <em>giá trị của biến đo</em>, không "
     "phải giá trị tín hiệu, trừ khi có ghi chú khác. Báo động mức cao lấy từ tín hiệu bộ "
     "truyền mức tác động ngược vẫn là <b>LAH</b>, dù báo động kích hoạt khi tín hiệu tụt "
     "xuống mức thấp. Các từ này có thể kết hợp (xem điều 6.9A).",
     "The modifying terms «high», «low» and «middle»/«intermediate» refer to values of the "
     "<em>measured variable</em>, not of the signal, unless otherwise noted. A high-level "
     "alarm derived from a reverse-acting level transmitter signal is still <b>LAH</b>, even "
     "though it actuates when the signal falls to a low value. The terms may be combined "
     "(see clause 6.9A)."),
    ("Với vị trí của van và thiết bị đóng-mở khác, «cao» nghĩa là van đang ở hoặc tiến tới "
     "<em>vị trí mở hoàn toàn</em>, «thấp» là đang ở hoặc tiến tới <em>vị trí đóng hoàn "
     "toàn</em>.",
     "Applied to valve and other open-close device positions, «high» denotes the valve in or "
     "approaching the <em>fully open</em> position and «low» the <em>fully closed</em> "
     "position."),
    ("Từ «ghi» áp dụng cho mọi hình thức lưu trữ thông tin vĩnh viễn cho phép truy xuất bằng "
     "bất kỳ cách nào.",
     "The word «record» applies to any form of permanent storage of information permitting "
     "retrieval by any means."),
    ("Về cách dùng «transmitter» và «converter», xem các định nghĩa ở điều 3.",
     "For «transmitter» versus «converter», see the definitions in clause 3."),
    ("Chữ đầu <b>V</b>, «dao động hoặc phân tích cơ khí», đảm nhiệm trong giám sát máy móc "
     "vai trò mà chữ <b>A</b> đảm nhiệm cho phép phân tích tổng quát. Trừ dao động, biến "
     "quan tâm cần được định nghĩa bên ngoài vòng tròn ký hiệu.",
     "First-letter <b>V», «vibration or mechanical analysis», performs for machinery "
     "monitoring the duty that <b>A</b> performs for more general analyses. Except for "
     "vibration, the variable of interest is expected to be defined outside the tagging bubble."),
    ("Chữ đầu <b>Y</b> dùng khi đáp ứng điều khiển hay giám sát được dẫn dắt bởi <em>sự "
     "kiện</em>, không phải bởi thời gian hay lịch thời gian. Ở vị trí này Y còn có thể chỉ "
     "sự hiện diện hoặc trạng thái.",
     "First-letter <b>Y</b> is intended when control or monitoring responses are "
     "<em>event-driven</em> rather than time- or schedule-driven. In this position it can also "
     "signify presence or state."),
    ("Chữ bổ nghĩa <b>K</b> đi cùng chữ đầu như L, T, W chỉ <em>tốc độ thay đổi theo thời "
     "gian</em> của biến đo/khởi tạo. Chẳng hạn <b>WKIC</b> có thể là bộ điều khiển tốc độ "
     "giảm khối lượng.",
     "Modifying-letter <b>K</b> combined with a first-letter such as L, T or W signifies the "
     "<em>time rate of change</em> of the measured or initiating variable. <b>WKIC</b>, for "
     "instance, may represent a rate-of-weight-loss controller."),
    ("Chữ tiếp theo <b>K</b> là tùy chọn của người dùng để chỉ trạm điều khiển, trong khi "
     "chữ tiếp theo <b>C</b> dùng cho bộ điều khiển tự động hoặc thủ công (xem điều 3).",
     "Succeeding-letter <b>K</b> is a user's option for designating a control station, while "
     "succeeding-letter <b>C</b> describes automatic or manual controllers (see clause 3)."),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Chữ đầu</em> — biến đo/biến khởi tạo. · "
        "<em>Chữ tiếp theo</em> — chức năng đọc, thụ động hoặc chức năng ra. · <em>Chữ bổ "
        "nghĩa</em> — D, F, M, K, Q, H, L, M. · <em>Tùy chọn người dùng</em> — chữ B, C, D, "
        "G, M, N, O dành cho nghĩa riêng của từng dự án. · <em>X</em> — chưa phân loại.",
        "<b>Key terms.</b> <em>First-letter</em> — the measured or initiating variable. · "
        "<em>Succeeding-letters</em> — readout, passive or output functions. · <em>Modifying "
        "letters</em> — D, F, M, K, Q, H, L, M. · <em>User's choice</em> — letters B, C, D, "
        "G, M, N, O reserved for project-specific meanings. · <em>X</em> — unclassified.",
        lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731
    pick = lambda cell: cell[0] if lang == "vi" else cell[1]  # noqa: E731

    b.append(lead(A(
        "Điều 5 định nghĩa các «viên gạch» của hệ thống nhận dạng dưới dạng bảng tra cứu ngắn "
        "gọn. Bảng 1 — cùng 22 chú thích ở điều 5.1 — giải thích từng chữ cái dùng làm định "
        "danh chức năng theo quy tắc của điều 4.2.",
        "Clause 5 defines the building blocks of the identification and symbolic representation "
        "system in a concise, easily referenced form. Table 1 — together with the 22 notes in "
        "clause 5.1 — defines and explains each letter used as a functional identifier under "
        "the rules of clause 4.2.")))

    b.append(h2(A("Bảng 1 · Chữ cái nhận dạng", "Table 1 · Identification letters"),
                A("Bảng tra cứu chữ cái", "The letter lookup table")))
    b.append(p(A(
        "Số trong ngoặc đơn dẫn tới chú thích giải thích tương ứng ở điều 5.1 (được dịch đầy "
        "đủ ngay dưới bảng). Cột 2 là nghĩa khi chữ đứng <em>đầu</em>; cột 4–5 là nghĩa khi "
        "chữ đứng <em>sau</em>; cột 3 và 6 là nghĩa bổ nghĩa.",
        "Numbers in parentheses refer to the explanatory notes in clause 5.1 (translated in "
        "full below the table). Column 2 gives the meaning as a <em>first-letter</em>; columns "
        "4–5 as <em>succeeding-letters</em>; columns 3 and 6 are modifier meanings.")))
    rows = [[r[0]] + [pick(c) or "—" for c in r[1:]] for r in ROWS]
    b.append(table(
        [A("Chữ", "Letter"),
         A("Biến đo / khởi tạo", "Measured or initiating variable"),
         A("Bổ nghĩa", "Modifier"),
         A("Chức năng đọc / thụ động", "Readout or passive function"),
         A("Chức năng ra", "Output function"),
         A("Bổ nghĩa", "Modifier")],
        rows,
        A("Bảng 1 — Chữ cái nhận dạng. Số trong ngoặc dẫn tới chú thích điều 5.1.",
          "Table 1 — Identification Letters. Numbers in parentheses refer to notes in 5.1.")))

    b.append(h2(A("5.1 · 22 chú thích cho Bảng 1", "5.1 · Twenty-two notes for Table 1"),
                A("Giải thích chính thức", "The official explanations")))
    b.append(p(A(
        "Các chú thích này không phải bình luận thêm mà là một phần của tiêu chuẩn: chúng quyết "
        "định ranh giới dùng chữ, đặc biệt là các trường hợp dễ dùng sai như PSV/PCV, "
        "switch/controller/relay hay LAH lấy từ tín hiệu đảo ngược.",
        "These notes are not commentary but part of the standard: they decide the boundaries "
        "of letter usage, especially easily misused cases such as PSV/PCV, "
        "switch/controller/relay, or an LAH derived from a reverse-acting signal.")))
    b.append(ol([A(vi, en) for vi, en in NOTES]))

    b.append(h2(A("Cách đọc nhanh một số thẻ", "Reading a tag at a glance"),
                A("Ví dụ ghép chữ", "Worked letter combinations")))
    b.append(table(
        [A("Số thẻ", "Tag"), A("Giải mã", "Decoding")],
        [
            ["TIC-103", A("T = nhiệt độ · I = chỉ thị · C = điều khiển · 103 = vòng lặp",
                          "T = temperature · I = indicate · C = control · 103 = loop")],
            ["TDAL-21", A("T + D = nhiệt độ vi phân · A = báo động · L = thấp",
                          "T + D = differential temperature · A = alarm · L = low")],
            ["PSV-5", A("P = áp suất · S = an toàn · V = van (van xả an toàn)",
                        "P = pressure · S = safety · V = valve (pressure safety valve)")],
            ["PCV-5", A("P = áp suất · C = điều khiển · V = van (van điều khiển tự lực)",
                        "P = pressure · C = control · V = valve (self-actuated control valve)")],
            ["FV-2A / FV-2B", A("Hai van lưu lượng trong cùng vòng lặp 2, phân biệt bằng hậu tố",
                                "Two flow valves in the same loop 2, distinguished by suffix")],
            ["WKIC", A("W + K = tốc độ thay đổi khối lượng · I = chỉ thị · C = điều khiển",
                       "W + K = rate of weight change · I = indicate · C = control")],
        ],
        A("Ví dụ áp dụng các quy tắc 4.2, 4.3 và các chú thích 4, 8, 13, 21.",
          "Examples applying clauses 4.2, 4.3 and notes 4, 8, 13 and 21.")))
    b.append(note(A(
        "<b>Tiếp theo.</b> Chương 5 đưa Bảng 2 (các tổ hợp chữ điển hình) và Bảng 3 (khối "
        "chức năng SAMA); Chương 6 bắt đầu phần bản vẽ với toàn bộ tờ ký hiệu của điều 6.",
        "<b>Next.</b> Chapter 5 gives Table 2 (typical letter combinations) and Table 3 (SAMA "
        "function blocks); Chapter 6 begins the drawings with every symbol sheet of clause 6.")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
