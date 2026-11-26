# -*- coding: utf-8 -*-
"""Book 7, Chapter 28 - Electric versus Pneumatic Actuators /
Cơ cấu chấp hành điện so với khí nén (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
167-169 (PDF pp. 163-165; printed = PDF + 4). Three printed pages: six
application bullets for electric actuators, four electric actuator types,
a discussion of why pneumatic actuators still dominate, two references.
No figures, tables or equations.
"""
from cvp_common import h2, h3, note, ol, p, refs, ul

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Electric versus Pneumatic Actuators"
TITLE_VI = "Cơ cấu chấp hành điện so với khí nén"

_REFS = [
    "Béla G. Lipták, Instrument Engineers’ Handbook, Vol. 1, Process Measurement "
    "and Analysis, 4th ed. (Boca Raton, FL: CRC Press, 2003): 1824.",
    "Kevin M. Hynes, “Electric Actuators Optimize Valve Response,” Power "
    "Engineering (July 1988).",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 28.</b> cơ cấu chấp hành điện · cơ cấu chấp hành khí "
                "nén · băng chết (deadband) · độ phân giải hành trình · khí dụng cụ · "
                "lực động tác dụng lên thân van · mô-men khởi động (breakaway torque) · "
                "tác động an toàn / fail-safe · vị trí hiện tại (“as is”) · mô tơ xoay "
                "chiều (AC) · bộ bánh răng · cơ chế tịnh tiến · đai ốc ren · trục dẫn · "
                "chu kỳ làm việc · đầu ra tuyến tính / đầu ra quay · mô tơ bước một chiều "
                "(DC) · mạch khuếch đại · cơ cấu điện–thủy lực · dầu được bơm · bơm theo "
                "yêu cầu · lò xo hồi vị · máy gia nhiệt phụ · bước rời rạc · cuộn điện "
                "điều tiết (modulating solenoid) · phần ứng · lõi sắt · tín hiệu điện áp "
                "thay đổi · bộ lồng cân bằng áp suất · HART · Foundation Fieldbus · "
                "PROFIBUS · màng cao su có lò xo · gợn sóng tín hiệu · bộ chuyển đổi I/P · "
                "thể tích không khí · tụ điện · vòng điều khiển mất ổn định · nhiễu điện")
    return ("<b>Key terms.</b> electric actuator · pneumatic actuator · deadband · travel "
            "resolution · instrument air · dynamic forces on the valve stem · breakaway "
            "torque · fail-safe action · “as is” position · alternating current (AC) motor "
            "· internal gear drive · reciprocating drive mechanism · rotating threaded nut "
            "· spindle · duty cycle · linear / rotary power output · direct current (DC) "
            "stepping motor · amplifying circuit · electric-hydraulic actuator · pumped oil "
            "· on-demand pump · return spring · auxiliary heater · discrete steps · "
            "modulating solenoid · armature · iron core · variable voltage signal · "
            "pressure-balanced trim · HART · Foundation Fieldbus · PROFIBUS · spring-loaded "
            "rubber diaphragm · signal ripple · I/P transducer · air volume · capacitor · "
            "loop instability · electrical noise")


def body_vi():
    b = []
    b.append(h2("Cơ cấu chấp hành điện so với khí nén",
                "Electric versus Pneumatic Actuators"))
    b.append(p("Tại sao không dùng cơ cấu chấp hành điện? Việc ứng dụng chúng đã là một "
               "mục tiêu khó đạt trong suốt 40 năm qua. Năm 1965, khi cơ cấu chấp hành điện "
               "bắt đầu được sử dụng, một công ty nghiên cứu thị trường lớn đã dự báo rằng "
               "85% tất cả van điều khiển sẽ vận hành bằng điện vào năm 1975! Than ôi, điều "
               "đó đã không xảy ra. Cơ cấu chấp hành điện vẫn chiếm chưa tới 5% tổng số. "
               "Đó là chuyện về dự báo xu hướng thị trường."))
    b.append(h3("Khi nào cơ cấu chấp hành điện có lợi thế",
                "Where electric actuators offer advantages"))
    b.append(p("Tuy nhiên, có những ứng dụng mà cơ cấu chấp hành điện có lợi thế so với "
               "cơ cấu chấp hành khí nén [1, 2]:"))
    b.append(ul([
        "Những nơi cần định vị chính xác mà không có băng chết (độ phân giải hành trình "
        "lên tới 0,02% là có sẵn).",
        "Những nơi ở vị trí xa và không có khí dụng cụ.",
        "Để khắc phục các lực động lớn tác dụng lên thân van.",
        "Những nơi cần lực thân van lớn (thường đi kèm với đáp ứng tần số thấp).",
        "Van có ma sát đệm thân van lớn hoặc mô-men khởi động cao.",
        "Những nơi van phải giữ nguyên vị trí hiện tại (“as is”) khi mất điện.",
    ]))
    b.append(h3("Các kiểu cơ cấu chấp hành điện chính",
                "Major electric actuator types"))
    b.append(p("Hiện có các kiểu cơ cấu chấp hành điện chính sau."))
    b.append(ul([
        "<b>Cơ cấu chấp hành điện – bánh răng (electric gear drive).</b> Thường dùng mô tơ "
        "xoay chiều (AC) trên 1000 vòng/phút; số vòng của mô tơ được giảm dần qua bộ bánh "
        "răng bên trong xuống dưới 10 vòng/phút và — đối với cơ chế truyền động tịnh tiến — "
        "kết thúc ở một đai ốc ren xoay làm thanh trục chuyển động lên và xuống. Loại này "
        "tương đối rẻ và chịu được dải nhiệt độ rộng, nhưng không chịu được vòng điều khiển "
        "mất ổn định (xem phần thảo luận sau). Cần lưu ý rằng chu kỳ làm việc có thể chỉ "
        "bằng 25% hành trình định mức. Thiết bị có đầu ra công suất tuyến tính hoặc quay "
        "(mô-men tới 5000 ft × lb).",
        "<b>Cơ cấu chấp hành mô tơ bước (stepping motor).</b> Các thiết bị này dùng mô tơ "
        "bước một chiều (DC), có thể định vị tới 1 trên 5000 bước với mạch khuếch đại phù "
        "hợp. Ưu điểm là định vị chính xác hơn và mô tơ có thể bị kẹt mà không cháy. Tuy "
        "nhiên, chúng đắt hơn một chút và bị hạn chế về lực đẩy hoặc mô-men vì không có mô "
        "tơ bước cỡ lớn.",
        "<b>Cơ cấu chấp hành điện–thủy lực (electric-hydraulic).</b> Các thiết bị này dùng "
        "nguồn năng lượng trung gian (dầu được bơm) để đẩy piston lên và xuống. Dầu được "
        "bơm liên tục hoặc bơm theo yêu cầu bằng một bơm do mô tơ bước dẫn động. Chúng khá "
        "bền nhưng tiêu thụ nhiều điện hơn, đắt hơn, cần máy gia nhiệt phụ để làm việc ở "
        "nhiệt độ môi trường thấp và cần bảo trì nhiều hơn các cơ cấu chấp hành điện khác. "
        "Các mẫu tiên tiến hơn dùng mô tơ bước để bơm dầu theo từng bước rời rạc; điều này "
        "làm thiết bị bền hơn. Một ưu điểm nữa là, giống cơ cấu khí nén, chúng có chu kỳ "
        "làm việc 100% và piston có thể được lắp lò xo hồi vị, nhờ đó tạo tác động an toàn "
        "(fail-safe). Cuối cùng, chúng tiêu thụ ít điện hơn kiểu bơm liên tục.",
        "<b>Cuộn điện điều tiết (modulating solenoid).</b> Các cơ cấu này dùng cuộn điện "
        "công suất thấp, có lò xo hồi vị và phần ứng khá dài. Thân van được gắn vào một lõi "
        "sắt trượt lên và xuống trong lõi của cuộn dây theo tín hiệu điện áp thay đổi từ mạch "
        "điều khiển. Vì công suất tương đối thấp, các thiết bị này dùng kiểu bộ lồng cân "
        "bằng áp suất (pressure-balanced trim). Chúng khá phổ biến trong hệ thống sưởi và "
        "điều hòa không khí.",
    ]))
    b.append(p("Hầu hết cơ cấu chấp hành hiện có đều có thể điều khiển số qua HART, "
               "Foundation Fieldbus hoặc PROFIBUS. Khi so sánh độ phức tạp tiềm ẩn của các "
               "thiết bị này với một màng cao su đơn giản có lò xo, lý do cơ cấu chấp hành "
               "khí nén vẫn chiếm ưu thế trở nên hiển nhiên."))
    b.append(h3("Vì sao khí nén được ưu tiên",
                "Why pneumatic actuators are preferred"))
    b.append(p("Các lý do khác khiến cơ cấu chấp hành khí nén được ưu tiên hơn loại điện "
               "là chi phí thấp hơn, độ tin cậy cao hơn, ít cồng kềnh và nhẹ hơn, cùng đáp "
               "ứng tần số cao hơn (ở kích cỡ nhỏ). Một yếu tố nữa là khả năng tự động có "
               "tác động an toàn nhờ màng lò xo và một số cơ cấu piston (van đóng an toàn "
               "hoặc mở an toàn khi mất tín hiệu — fail close hoặc fail open)."))
    b.append(p("Một lý do quan trọng nhưng ít được nhận ra là khả năng chống chịu rất tốt "
               "của cơ cấu khí nén đối với những nhiễu loạn nhỏ trong tín hiệu bộ điều "
               "khiển, có thể do vòng điều khiển hơi mất ổn định hoặc thậm chí do nhiễu điện. "
               "Dù một bộ chuyển đổi I/P nhạy truyền qua một gợn sóng với biên độ khoảng "
               "±0,01 psi và tần số, ví dụ, 2 Hz, thể tích không khí tương đối lớn chứa "
               "trong cơ cấu khí nén vẫn hấp thụ hoàn toàn gợn sóng đó mà không gây ra dù "
               "chỉ một chuyển động nhỏ của thân van. Theo thuật ngữ điện, buồng màng khí "
               "nén hoạt động như một tụ điện lớn!"))
    b.append(p("Ngược lại, những gợn sóng tín hiệu như vậy có thể gây chết người cho cơ cấu "
               "điện kiểu bánh răng. Ở đây mô tơ phản ứng ngay lập tức (giả sử bộ khuếch "
               "đại có băng chết thấp), gây ra chuyển động qua lại nhẹ của trục mô tơ và "
               "các bánh răng. Điều này thường khiến một răng bánh răng liên tục ăn khớp "
               "và đổi tải ở cả hai chiều. Sau khoảng một triệu chu kỳ như vậy, răng đó và "
               "toàn bộ cơ cấu chấp hành sẽ hỏng chỉ trong vài tuần hoặc vài tháng."))
    b.append(refs(_REFS))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm ba trang in (167–169; trang in "
                  "= trang PDF + 4), không có hình, bảng hay phương trình. Các con số và "
                  "đơn vị gốc (85%, 5%, 0,02%, 1000 rpm, 10 rpm, 25%, 5000 ft × lb, 1 trên "
                  "5000 bước, ±0,01 psi, 2 Hz, 100%) được giữ nguyên, với dấu thập phân "
                  "được Việt hóa thành dấu phẩy. Cụm “discreet steps” trong nguyên bản "
                  "được giữ nguyên ở bản tiếng Anh. Bản tiếng Việt thêm bản dịch thuật ngữ "
                  "trong ngoặc để người đọc dễ đối chiếu."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © 2011 Hans D. Baumann, do ISA / John Wiley &amp; Sons xuất bản.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Electric versus Pneumatic Actuators",
                "Electric versus Pneumatic Actuators"))
    b.append(p("Why not use electric actuators? Their use has been an elusive goal for the "
               "past 40 years. In 1965, when electric actuators started to be used, a major "
               "market research company predicted that 85% of all control valves would be "
               "electrically operated by 1975! Alas, this did not happen. Electric actuators "
               "still represent less than 5% of the total. So much for forecasting market "
               "trends."))
    b.append(h3("Where electric actuators offer advantages",
                "Where electric actuators offer advantages"))
    b.append(p("However, there are applications where electric actuators offer advantages "
               "over pneumatic actuators [1, 2]:"))
    b.append(ul([
        "Where precise positioning with no deadband is required (actuators with up to "
        "0.02% of travel resolutions are available).",
        "Where there are requirements in remote locations and no instrument air is "
        "available.",
        "To overcome severe dynamic forces acting on a valve stem.",
        "Where high stem forces are required (usually coupled with a low-frequency "
        "response).",
        "For valves having high packing friction, or breakaway torque.",
        "Where the valve must fail in the “as is” position on power failure.",
    ]))
    b.append(h3("Major electric actuator types", "Major electric actuator types"))
    b.append(p("The following major electric actuator types are available."))
    b.append(ul([
        "<b>Electric gear drive actuators.</b> These actuators typically utilize "
        "alternating current (AC) motors over 1000 rpm where the motor revolutions are "
        "gradually reduced to less than 10 rpm by internal gear drives ending—in the case "
        "of reciprocating drive mechanisms—in a rotating threaded nut that moves the "
        "spindle up and down. These actuators are reasonably inexpensive and can withstand "
        "wide temperature ranges but do not tolerate unstable control loops (see later "
        "discussion). Note that the duty cycle may be as low as 25% of rated travel. These "
        "devices have either linear or rotary power output (up to 5000 ft × lb torque).",
        "<b>Stepping motor actuators.</b> These devices use direct current (DC) stepping "
        "motors that can be positioned with up to 1 in 5000 steps by suitable amplifying "
        "circuits. The advantages are more precise positioning, and the motor can be "
        "stalled without burning out. However, they are somewhat more expensive and are "
        "limited in thrust or torque due to the unavailability of large stepping motors.",
        "<b>Electric-hydraulic actuators.</b> These devices use an intermediary power "
        "source (pumped oil) to drive a piston up and down. The oil is either pumped "
        "continuously or pumped on demand by a stepping-motor-driven pump. These devices "
        "are fairly rugged but consume more power, cost more, require auxiliary heaters to "
        "work in low ambient temperatures, and need more maintenance than other electric "
        "actuators. More advanced models use stepping motors to pump oil in discreet steps. "
        "This makes the device more rugged. Other advantages are that, like pneumatic "
        "actuators, they offer a 100% duty cycle and their pistons can be fitted with a "
        "return spring, thus providing fail-safe action. Finally, they require less power "
        "consumption than continuously pumping models.",
        "<b>Modulating solenoids.</b> These actuators employ a spring-loaded, low-power "
        "solenoid with a rather long armature. The valve stem is attached to an iron core "
        "that slides up and down the core of the wound armature following a variable voltage "
        "signal from a control circuit. These devices have relatively low power and "
        "therefore use pressure-balanced trim designs. They are somewhat common in heating "
        "and air-conditioning systems.",
    ]))
    b.append(p("Most available actuators can be digitally controlled using either HART, "
               "Foundation Fieldbus, or PROFIBUS architecture. When comparing the implied "
               "complexity of such devices to a simple spring-loaded rubber diaphragm, it "
               "becomes obvious why the pneumatic actuator still dominates."))
    b.append(h3("Why pneumatic actuators are preferred",
                "Why pneumatic actuators are preferred"))
    b.append(p("Other reasons pneumatic actuators are preferred over electric actuators "
               "are lower cost, more reliability, less bulk and weight, and higher frequency "
               "response (in smaller sizes). Another factor is the automatic availability of "
               "the fail-safe action provided by a spring diaphragm and some piston "
               "actuators (fail open or fail close of the valve)."))
    b.append(p("One important but seldom recognized reason is the excellent resistance of "
               "pneumatic actuators to minor upsets in the controller signal, which can be "
               "caused by a slight loop instability or even electrical noise. Even if a "
               "ripple is passed through by a responsive I/P transducer, at an amplitude of "
               "perhaps ±0.01 psi of signal change and a frequency of, say, 2 Hz, these are "
               "completely absorbed by the relatively large air volume contained in a "
               "pneumatic actuator without causing so much as a tiny stem movement. In "
               "electrical terms, the pneumatic diaphragm case acts as a large capacitor!"))
    b.append(p("In contrast, such signal ripples can be deadly in a gear-type electric "
               "actuator. Here, the motor will respond instantly (assuming a low deadband "
               "amplifier) causing a slight back-and-forth movement of the motor stem and "
               "the gears. This typically makes one tooth in a gear constantly engage and "
               "change the load in both directions. After perhaps a million such cycles, "
               "that tooth and the actuator are gone in a matter of weeks or months."))
    b.append(refs(_REFS))
    b.append(note("<b>Source quirks.</b> The chapter spans three printed pages (167–169; "
                  "printed = PDF + 4), with no figures, tables or equations. All original "
                  "numbers and units (85%, 5%, 0.02%, 1000 rpm, 10 rpm, 25%, 5000 ft × lb, "
                  "1 in 5000 steps, ±0.01 psi, 2 Hz, 100%) are retained verbatim; the "
                  "Vietnamese page renders decimal points as commas. The original wording "
                  "“discreet steps” is retained here."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 2011 Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)
