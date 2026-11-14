# -*- coding: utf-8 -*-
"""ANSI/ISA-5.1 — Chapter 2: Definitions (§3)."""
from isa51_common import T, h2, h3, lead, note, p, table, ul

PAGES_SRC = 4
BYLINE = "ANSI/ISA-5.1-1984 (R1992) · §3"

# (English term, Vietnamese term, English definition, Vietnamese definition)
TERMS = [
    ("Accessible", "Truy cập được",
     "A device or function an operator can use or see in order to perform control actions, e.g. set-point changes, auto-manual transfer or on-off actions.",
     "Thiết bị hoặc chức năng mà người vận hành có thể dùng hoặc nhìn thấy để thực hiện thao tác điều khiển: đổi giá trị đặt, chuyển tự động/thủ công, đóng-cắt."),
    ("Alarm", "Báo động",
     "A device or function that signals an abnormal condition by an audible or visible discrete change, or both, intended to attract attention. A device that merely opens or closes a circuit is properly called a switch (level switch, flow switch, …); it is an alarm only if it itself contains the alarm function.",
     "Thiết bị hoặc chức năng báo hiệu một trạng thái bất thường bằng thay đổi rời rạc về âm thanh hoặc ánh sáng nhằm gây chú ý. Thiết bị chỉ đóng/cắt mạch phải gọi là công tắc (công tắc mức, công tắc lưu lượng…); chỉ gọi là báo động khi bản thân nó chứa chức năng báo động."),
    ("Assignable", "Có thể gán",
     "A feature permitting a signal to be channelled from one device to another without switching, patching or wiring changes.",
     "Đặc tính cho phép định tuyến tín hiệu từ thiết bị này sang thiết bị khác mà không cần chuyển mạch, đấu nối lại hay thay dây."),
    ("Auto-manual station", "Trạm tự động–thủ công",
     "Synonym for control station.", "Tên gọi khác của trạm điều khiển (control station)."),
    ("Balloon", "Bóng (balloon)",
     "Synonym for bubble.", "Tên gọi khác của vòng tròn ký hiệu (bubble)."),
    ("Behind the panel", "Sau bảng điều khiển",
     "A location within the area containing the instrument panel, its associated rack-mounted hardware, or enclosed within the panel. Such devices are not accessible for the operator's normal use; broadly equivalent to 'not normally accessible to the operator'.",
     "Vị trí nằm trong khu vực chứa bảng thiết bị, phần cứng lắp rack liên quan, hoặc nằm bên trong bảng. Các thiết bị này không truy cập được khi vận hành bình thường; hiểu rộng là «không thường xuyên truy cập được»."),
    ("Binary", "Nhị phân",
     "A signal or device having only two discrete positions or states. In its simplest sense (binary vs analog) it denotes an on-off or high-low state, i.e. one that does not represent a continuously varying quantity.",
     "Tín hiệu hoặc thiết bị chỉ có hai vị trí/trạng thái rời rạc. Theo nghĩa đơn giản nhất (đối lập với tương tự) là trạng thái đóng-cắt hoặc cao-thấp, tức không biểu diễn đại lượng biến đổi liên tục."),
    ("Board", "Bảng",
     "Synonym for panel.", "Tên gọi khác của bảng điều khiển (panel)."),
    ("Bubble", "Vòng tròn ký hiệu",
     "The circular symbol used to denote and identify the purpose of an instrument or function; it may contain a tag number. Synonym for balloon.",
     "Ký hiệu hình tròn dùng để biểu diễn và nhận dạng mục đích của một thiết bị hoặc chức năng; có thể chứa số thẻ. Còn gọi là balloon."),
    ("Computing device", "Thiết bị tính toán",
     "A device or function that performs one or more calculations and/or logic operations and transmits one or more resulting output signals. Sometimes called a computing relay.",
     "Thiết bị hoặc chức năng thực hiện một hay nhiều phép tính và/hoặc phép logic rồi phát một hay nhiều tín hiệu ra. Đôi khi gọi là relay tính toán."),
    ("Configurable", "Có thể cấu hình",
     "A device or system whose functional characteristics can be selected or rearranged by programming or other methods; rewiring is excluded.",
     "Thiết bị hoặc hệ thống có đặc tính chức năng được chọn hoặc sắp xếp lại bằng lập trình hay cách khác; không tính thay dây nối."),
    ("Controller", "Bộ điều khiển",
     "A device whose output varies to regulate a controlled variable in a specified manner. It may be a self-contained analog or digital instrument or the equivalent in a shared-control system. An automatic controller responds to a measured process variable; a manual controller is a manual loading station. A controller may be integral with other loop elements.",
     "Thiết bị có tín hiệu ra thay đổi để điều chỉnh biến được điều khiển theo một quy luật xác định. Có thể là thiết bị tương tự/số độc lập hoặc chức năng tương đương trong hệ thống điều khiển dùng chung. Bộ điều khiển tự động đáp ứng biến quá trình đo được; bộ thủ công là trạm nạp tay. Có thể tích hợp với phần tử khác của vòng lặp."),
    ("Control station", "Trạm điều khiển",
     "A manual loading station that also switches between manual and automatic control modes of a loop; also called an auto-manual station. The operator interface of a distributed control system may be regarded as one.",
     "Trạm nạp tay có thêm chức năng chuyển giữa chế độ thủ công và tự động của vòng lặp; gọi khác là trạm tự động–thủ công. Giao diện người vận hành của hệ thống điều khiển phân tán cũng có thể coi là một trạm điều khiển."),
    ("Control valve", "Van điều khiển",
     "A device, other than a common hand-actuated on-off valve or a self-actuated check valve, that directly manipulates the flow of one or more fluid process streams. 'Hand control valve' should be limited to hand-actuated valves used for throttling or requiring instrument identification.",
     "Thiết bị — không phải van đóng-cắt bằng tay thông thường hay van một chiều tự lực — trực tiếp điều tiết lưu chất của một hay nhiều dòng công nghệ. Tên «van điều khiển tay» chỉ dùng cho van tay tiết lưu hoặc van cần nhận dạng như một thiết bị đo."),
    ("Converter", "Bộ chuyển đổi",
     "A device that receives information in one form of instrument signal and transmits an output signal in another form. An instrument that changes a sensor output into a standard signal is a transmitter, not a converter (TE connects to TT, not TY). 'Transducer' is too general for this use.",
     "Thiết bị nhận thông tin dưới một dạng tín hiệu và phát ra tín hiệu dạng khác. Thiết bị đổi tín hiệu cảm biến thành tín hiệu chuẩn là bộ truyền (transmitter), không phải bộ chuyển đổi (TE nối với TT, không phải TY). Thuật ngữ «transducer» quá tổng quát cho trường hợp này."),
    ("Digital", "Số",
     "A signal or device that uses binary digits to represent continuous values or discrete states.",
     "Tín hiệu hoặc thiết bị dùng chữ số nhị phân để biểu diễn giá trị liên tục hoặc trạng thái rời rạc."),
    ("Distributed control system", "Hệ thống điều khiển phân tán",
     "A system which, while functionally integrated, consists of subsystems that may be physically separate and remotely located from one another.",
     "Hệ thống dù tích hợp về chức năng nhưng gồm các phân hệ có thể đặt tách rời và ở xa nhau."),
    ("Final control element", "Phần tử chấp hành cuối",
     "The device that directly controls the value of the manipulated variable of a control loop; often a control valve.",
     "Thiết bị trực tiếp điều khiển giá trị biến bị tác động của vòng lặp; thường là van điều khiển."),
    ("Function", "Chức năng",
     "The purpose of, or an action performed by, a device.", "Mục đích của một thiết bị hoặc hành động do thiết bị thực hiện."),
    ("Identification", "Nhận dạng",
     "The sequence of letters or digits, or both, used to designate an individual instrument or loop.",
     "Chuỗi chữ cái, chữ số hoặc cả hai dùng để chỉ một thiết bị hay một vòng lặp cụ thể."),
    ("Instrument", "Thiết bị (đo/điều khiển)",
     "A device used directly or indirectly to measure and/or control a variable. It includes primary elements, final control elements, computing devices and electrical devices such as annunciators, switches and pushbuttons. It does not apply to internal component parts (a receiver bellows or a resistor).",
     "Thiết bị dùng trực tiếp hoặc gián tiếp để đo và/hoặc điều khiển một biến. Bao gồm phần tử sơ cấp, phần tử chấp hành cuối, thiết bị tính toán và thiết bị điện như bảng báo động, công tắc, nút nhấn. Không áp dụng cho linh kiện bên trong (ống thổi thu, điện trở)."),
    ("Instrumentation", "Thiết bị đo lường (hệ thống)",
     "A collection of instruments, or their application, for observation, measurement, control or any combination of these.",
     "Tập hợp các thiết bị, hoặc việc ứng dụng chúng, nhằm quan sát, đo lường, điều khiển hoặc kết hợp các mục đích đó."),
    ("Local", "Tại chỗ",
     "An instrument that is neither in nor on a panel or console, nor mounted in a control room; commonly near a primary element or a final control element. 'Field' is often used synonymously.",
     "Thiết bị không nằm trong/trên bảng hay tủ điều khiển, cũng không lắp trong phòng điều khiển; thường đặt gần phần tử sơ cấp hoặc phần tử chấp hành cuối. Hay dùng từ «field» tương đương."),
    ("Local panel", "Bảng tại chỗ",
     "A panel that is not the central or main panel, commonly near plant subsystems or sub-areas. Not to be confused with 'local instrument'.",
     "Bảng không phải bảng trung tâm/chính, thường đặt gần phân hệ hoặc phân khu nhà máy. Không nhầm với «thiết bị tại chỗ»."),
    ("Loop", "Vòng lặp",
     "Two or more instruments or control functions arranged so that signals pass from one to another for measurement and/or control of a process variable.",
     "Hai hay nhiều thiết bị/chức năng được bố trí để tín hiệu truyền từ cái này sang cái kia nhằm đo và/hoặc điều khiển một biến quá trình."),
    ("Manual loading station", "Trạm nạp tay",
     "A device or function with a manually adjustable output used to actuate one or more remote devices. It does not switch between manual and automatic modes; it may have integral indicators, lights or other features. Also called manual station or manual loader.",
     "Thiết bị/chức năng có tín hiệu ra chỉnh bằng tay để tác động một hay nhiều thiết bị ở xa. Không chuyển chế độ thủ công/tự động; có thể tích hợp đồng hồ, đèn… Còn gọi là manual station, manual loader."),
    ("Measurement", "Phép đo",
     "The determination of the existence or the magnitude of a variable.",
     "Việc xác định sự tồn tại hoặc độ lớn của một biến."),
    ("Monitor", "Thiết bị giám sát",
     "A general, rather unspecific term for an instrument or instrument system used to measure or sense the status or magnitude of variables in order to derive useful information; it may mean analyser, indicator or alarm. Also used as a verb.",
     "Thuật ngữ tổng quát, khá không cụ thể, chỉ thiết bị/hệ thống đo hoặc cảm nhận trạng thái hay độ lớn của biến để rút ra thông tin hữu ích; có thể mang nghĩa máy phân tích, đồng hồ chỉ thị hoặc báo động. Cũng dùng như động từ."),
    ("Monitor light", "Đèn giám sát",
     "Synonym for pilot light.", "Tên gọi khác của đèn báo trạng thái (pilot light)."),
    ("Panel", "Bảng điều khiển",
     "A structure carrying a group of instruments, housing the operator–process interface and chosen to have a unique designation; it may consist of sections, cubicles, consoles or desks. Synonym for board.",
     "Kết cấu mang một nhóm thiết bị, chứa giao diện người vận hành–quá trình và được chọn có ký hiệu riêng; có thể gồm nhiều đoạn, tủ, bàn Console. Còn gọi là board."),
    ("Panel-mounted", "Lắp trên bảng",
     "An instrument mounted on a panel or console and accessible for the operator's normal use. A function normally accessible to the operator in a shared-display system is the equivalent.",
     "Thiết bị lắp trên bảng/tủ điều khiển và truy cập được khi vận hành bình thường. Chức năng thường truy cập được trong hệ thống hiển thị dùng chung được coi là tương đương."),
    ("Pilot light", "Đèn báo trạng thái",
     "A light indicating which of a number of normal conditions of a system or device exists; unlike an alarm light, which indicates an abnormal condition. Also called monitor light.",
     "Đèn chỉ ra đang có điều kiện bình thường nào trong số nhiều điều kiện của hệ thống/thiết bị; khác đèn báo động vốn chỉ trạng thái bất thường. Còn gọi là monitor light."),
    ("Primary element", "Phần tử sơ cấp",
     "Synonym for sensor.", "Tên gọi khác của cảm biến (sensor)."),
    ("Process", "Quá trình",
     "Any operation or sequence of operations involving a change of energy, state, composition, dimension or other properties definable with respect to a datum.",
     "Mọi thao tác hoặc chuỗi thao tác làm thay đổi năng lượng, trạng thái, thành phần, kích thước hay tính chất khác có thể định nghĩa theo một chuẩn."),
    ("Process variable", "Biến quá trình",
     "Any variable property of a process. In this standard the term applies to all variables other than instrument signals.",
     "Mọi thuộc tính biến đổi của quá trình. Trong tiêu chuẩn này, thuật ngữ chỉ mọi biến trừ tín hiệu của thiết bị đo."),
    ("Program", "Chương trình",
     "A repeatable sequence of actions that defines the status of outputs as a fixed relationship to a set of inputs.",
     "Chuỗi hành động lặp lại được, xác định trạng thái các tín hiệu ra theo một quan hệ cố định với một tập tín hiệu vào."),
    ("Programmable logic controller", "Bộ điều khiển logic khả trình (PLC)",
     "A controller, usually with multiple inputs and outputs, that contains an alterable program.",
     "Bộ điều khiển, thường có nhiều ngõ vào và ra, chứa một chương trình có thể thay đổi được."),
    ("Relay", "Relay / rơ-le",
     "A device that passes information on unchanged or in modified form; often used to mean computing device, though the latter is preferred. Also specifically an electric, pneumatic or hydraulic switch actuated by a signal.",
     "Thiết bị truyền tiếp thông tin không đổi hoặc đã biến đổi; thường dùng thay cho «thiết bị tính toán» dù nên dùng tên sau. Cũng chỉ riêng công tắc điện, khí nén hoặc thủy lực được tác động bằng tín hiệu."),
    ("Scan", "Quét",
     "To sample, in a predetermined manner, each of a number of variables intermittently; often to ascertain a variable's state or value, and possibly associated with recording or alarming.",
     "Lấy mẫu luân phiên từng biến trong một tập theo trình tự định trước; thường để xác định trạng thái/giá trị biến, có thể đi kèm ghi và báo động."),
    ("Sensor", "Cảm biến",
     "The part of a loop or instrument that first senses the value of a process variable and assumes a corresponding, predetermined and intelligible state or output. It may be separate from or integral with another loop element. Also called detector or primary element.",
     "Bộ phận của vòng lặp hay thiết bị đầu tiên cảm nhận giá trị biến quá trình và chuyển sang trạng thái/tín hiệu ra tương ứng, xác định trước, đọc được. Có thể tách rời hoặc tích hợp với phần tử khác. Còn gọi là detector, primary element."),
    ("Set point", "Giá trị đặt",
     "An input variable that sets the desired value of the controlled variable; it may be set manually, automatically or by program, and is expressed in the same units as the controlled variable.",
     "Biến vào xác lập giá trị mong muốn của biến được điều khiển; có thể đặt bằng tay, tự động hoặc theo chương trình, và dùng cùng đơn vị với biến được điều khiển."),
    ("Shared controller", "Bộ điều khiển dùng chung",
     "A controller containing preprogrammed algorithms that are usually accessible, configurable and assignable; it permits a number of process variables to be controlled by a single device.",
     "Bộ điều khiển chứa giải thuật lập trình sẵn, thường truy cập, cấu hình và gán được; cho phép một thiết bị điều khiển nhiều biến quá trình."),
    ("Shared display", "Hiển thị dùng chung",
     "The operator interface device (usually a video screen) used to display process control information from a number of sources at the operator's command.",
     "Thiết bị giao diện người vận hành (thường là màn hình) dùng để hiển thị thông tin điều khiển quá trình từ nhiều nguồn theo yêu cầu của người vận hành."),
    ("Switch", "Công tắc",
     "A device that connects, disconnects, selects or transfers one or more circuits and is not designated as a controller, relay or control valve. Also used as a verb for the functions performed.",
     "Thiết bị nối, ngắt, chọn hoặc chuyển một hay nhiều mạch, không được gọi là bộ điều khiển, relay hay van điều khiển. Cũng dùng làm động từ chỉ chức năng thực hiện."),
    ("Test point", "Điểm thử",
     "A process connection to which no instrument is permanently connected but which is intended for temporary or intermittent connection of an instrument.",
     "Điểm nối vào quá trình không có thiết bị nào gắn cố định, nhưng dùng để nối thiết bị tạm thời hoặc định kỳ."),
    ("Transducer", "Bộ biến đổi (transducer)",
     "A general term for a device that receives information as one or more physical quantities, modifies the information and/or its form if required, and produces a resultant output signal. Depending on application it may be a primary element, transmitter, relay, converter or other device; being unspecific, its use for specific applications is not recommended.",
     "Thuật ngữ tổng quát chỉ thiết bị nhận thông tin dưới dạng một hay nhiều đại lượng vật lý, sửa đổi thông tin và/hoặc dạng nếu cần, rồi phát tín hiệu ra. Tùy ứng dụng có thể là phần tử sơ cấp, bộ truyền, relay, bộ chuyển đổi… Vì không cụ thể, không nên dùng cho ứng dụng xác định."),
    ("Transmitter", "Bộ truyền tín hiệu",
     "A device that senses a process variable through a sensor and has an output whose steady-state value varies only as a predetermined function of that variable; the sensor may or may not be integral with it.",
     "Thiết bị cảm nhận biến quá trình qua cảm biến và có tín hiệu ra ở trạng thái ổn định chỉ biến đổi theo một hàm xác định trước của biến đó; cảm biến có thể tích hợp hoặc không."),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Bubble</em> — vòng tròn ký hiệu thiết bị/chức "
        "năng. · <em>Loop</em> — vòng lặp gồm hai hay nhiều thiết bị truyền tín hiệu. · "
        "<em>Sensor / primary element</em> — phần tử sơ cấp, cảm biến. · <em>Final control "
        "element</em> — phần tử chấp hành cuối. · <em>Set point</em> — giá trị đặt.",
        "<b>Key terms.</b> <em>Bubble</em> — the circular instrument/function symbol. · "
        "<em>Loop</em> — two or more instruments passing signals between them. · "
        "<em>Sensor / primary element</em> — the first element to sense a process variable. · "
        "<em>Final control element</em> — the device that manipulates the process. · "
        "<em>Set point</em> — the desired value of the controlled variable.", lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731
    b.append(lead(A(
        "Điều 3 định nghĩa toàn bộ từ vựng nền tảng của tiêu chuẩn. Các định nghĩa ở đây có "
        "hiệu lực để hiểu tiêu chuẩn; các thuật ngữ được in nghiêng trong một định nghĩa cũng "
        "được định nghĩa tại chính điều này. Muốn xem kỹ hơn, tiêu chuẩn dẫn tới ISA-51.1 và "
        "bộ tiêu chuẩn ISA-75.",
        "Clause 3 defines the standard's entire foundational vocabulary. These definitions "
        "apply for the purpose of understanding the standard, and terms italicised within a "
        "definition are also defined here. For a fuller treatment the standard refers to "
        "ISA-51.1 and the ISA-75 series.")))
    b.append(h2(A("Bảng thuật ngữ", "Glossary"),
                A("§3 — Định nghĩa", "§3 — Definitions")))
    b.append(p(A(
        "Bảng dưới đây giữ nguyên thuật ngữ tiếng Anh của tiêu chuẩn (vì chúng là gốc của các "
        "mã chữ cái ở Bảng 1) và đưa ra tên tiếng Việt tương ứng cùng định nghĩa đầy đủ.",
        "The table keeps the standard's English headwords — they are the source of the letter "
        "codes in Table 1 — and gives the Vietnamese equivalent together with the full "
        "definition.")))
    rows = []
    for en, vi, den, dvi in TERMS:
        rows.append([en, vi, dvi if lang == "vi" else den])
    b.append(table(
        [A("Thuật ngữ (EN)", "Term (EN)"), A("Tiếng Việt", "Vietnamese"),
         A("Định nghĩa", "Definition")],
        rows,
        A("%d thuật ngữ theo điều 3 của ANSI/ISA-5.1-1984 (R1992)." % len(TERMS),
          "%d terms from clause 3 of ANSI/ISA-5.1-1984 (R1992)." % len(TERMS))))

    b.append(h2(A("Hai phân biệt dễ nhầm", "Two distinctions worth keeping"),
                A("Những cặp dễ nhầm", "Commonly confused pairs")))
    b.append(ul([
        A("<b>Báo động ↔ công tắc.</b> Thiết bị chỉ đóng/cắt mạch là công tắc mức, công tắc "
          "lưu lượng…; chỉ gọi là báo động khi chính thiết bị đó chứa chức năng báo động.",
          "<b>Alarm ↔ switch.</b> A device that merely opens or closes a circuit is a level "
          "switch, flow switch and so on; it is an alarm only if it contains the alarm function."),
        A("<b>Bộ truyền ↔ bộ chuyển đổi.</b> Đổi tín hiệu cảm biến thành tín hiệu chuẩn là "
          "<em>transmitter</em> (TT), còn <em>converter</em> (TY) đổi từ dạng tín hiệu này "
          "sang dạng tín hiệu khác.",
          "<b>Transmitter ↔ converter.</b> Converting a sensor output to a standard signal is "
          "a <em>transmitter</em> (TT); a <em>converter</em> (TY) changes one form of "
          "instrument signal into another."),
        A("<b>Đèn báo trạng thái ↔ đèn báo động.</b> Pilot light chỉ điều kiện "
          "<em>bình thường</em>; alarm light chỉ điều kiện <em>bất thường</em>.",
          "<b>Pilot light ↔ alarm light.</b> A pilot light indicates which <em>normal</em> "
          "condition exists; an alarm light indicates an <em>abnormal</em> condition."),
        A("<b>Tại chỗ ↔ sau bảng.</b> «Local» là ngoài bảng/phòng điều khiển, thường gần cảm "
          "biến hoặc van; «behind the panel» là trong khu vực bảng, không truy cập được khi "
          "vận hành bình thường.",
          "<b>Local ↔ behind the panel.</b> «Local» means outside the panel/control room, "
          "usually near a sensor or valve; «behind the panel» means within the panel area and "
          "not accessible for normal operator use."),
    ]))
    b.append(note(A(
        "<b>Đọc tiếp.</b> Các định nghĩa này là chìa khóa để hiểu Bảng 1 (chữ cái nhận dạng) "
        "ở Chương 4 và các tờ ký hiệu ở Chương 6: chữ cái <b>E</b> là «Sensor (Primary "
        "Element)», <b>T</b> là «Transmit», <b>V</b> là «Valve, Damper, Louver», <b>Z</b> là "
        "«Driver, Actuator, Unclassified Final Control Element».",
        "<b>Where this leads.</b> These definitions are the key to Table 1 (identification "
        "letters) in Chapter 4 and to the symbol sheets in Chapter 6: <b>E</b> is «Sensor "
        "(Primary Element)», <b>T</b> is «Transmit», <b>V</b> is «Valve, Damper, Louver», "
        "<b>Z</b> is «Driver, Actuator, Unclassified Final Control Element».")))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
