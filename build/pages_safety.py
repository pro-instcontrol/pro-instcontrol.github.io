# -*- coding: utf-8 -*-
"""Safety instrumented systems: SIL, PFDavg, proof test, independence."""

from framework import Page, section_open, section_close, write, render, page_intro

INDEP_SVG = """
<svg viewBox="0 0 680 300" role="img" aria-label="A shared transmitter feeding both the basic control system and the safety system, compared with two separate transmitters">
  <defs>
    <marker id="sg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#66788d"/>
    </marker>
    <marker id="st" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#0d7a6f"/>
    </marker>
  </defs>

  <!-- ============ LEFT: shared device ============ -->
  <text x="24" y="24" font-family="'IBM Plex Mono',monospace" font-size="10" letter-spacing="1.5" fill="#b03a2e">SHARED DEVICE</text>

  <rect x="24" y="64" width="120" height="40" rx="5" fill="#fff" stroke="#0b1725" stroke-width="1.6"/>
  <text x="84" y="89" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10.5" fill="#0b1725">BPCS</text>

  <rect x="176" y="64" width="120" height="40" rx="5" fill="#fff" stroke="#0b1725" stroke-width="1.6"/>
  <text x="236" y="89" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10.5" fill="#0b1725">SIS</text>

  <line x1="24" y1="252" x2="316" y2="252" stroke="#0b1725" stroke-width="2"/>
  <polygon points="170,252 158,247 158,257" fill="#0b1725"/>

  <circle cx="110" cy="206" r="18" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <text x="110" y="210" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10" font-weight="600" fill="#0b1725">PT</text>
  <line x1="110" y1="252" x2="110" y2="224" stroke="#0b1725" stroke-width="1.4"/>

  <path d="M110 188 V152 H84 V106" fill="none" stroke="#66788d" stroke-width="1.5" marker-end="url(#sg)"/>
  <path d="M110 152 H236 V106" fill="none" stroke="#0d7a6f" stroke-width="1.5" marker-end="url(#st)"/>

  <circle cx="110" cy="152" r="3.4" fill="#b03a2e"/>
  <text x="122" y="146" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#b03a2e">one failure point</text>
  <text x="24" y="286" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#b03a2e">one device, one failure mode, both functions lost</text>

  <line x1="340" y1="40" x2="340" y2="270" stroke="#ccd7e3" stroke-width="1" stroke-dasharray="3 5"/>

  <!-- ============ RIGHT: separate devices ============ -->
  <text x="364" y="24" font-family="'IBM Plex Mono',monospace" font-size="10" letter-spacing="1.5" fill="#0a5f56">SEPARATE DEVICES</text>

  <rect x="364" y="64" width="120" height="40" rx="5" fill="#fff" stroke="#0b1725" stroke-width="1.6"/>
  <text x="424" y="89" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10.5" fill="#0b1725">BPCS</text>

  <rect x="516" y="64" width="120" height="40" rx="5" fill="#fff" stroke="#0b1725" stroke-width="1.6"/>
  <text x="576" y="89" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10.5" fill="#0b1725">SIS</text>

  <line x1="364" y1="252" x2="656" y2="252" stroke="#0b1725" stroke-width="2"/>
  <polygon points="500,252 488,247 488,257" fill="#0b1725"/>

  <circle cx="424" cy="206" r="18" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <text x="424" y="210" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10" font-weight="600" fill="#0b1725">PT</text>
  <line x1="424" y1="252" x2="424" y2="224" stroke="#0b1725" stroke-width="1.4"/>
  <path d="M424 188 V106" fill="none" stroke="#66788d" stroke-width="1.5" marker-end="url(#sg)"/>

  <circle cx="576" cy="206" r="18" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <text x="576" y="210" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="10" font-weight="600" fill="#0b1725">PT</text>
  <line x1="576" y1="252" x2="576" y2="224" stroke="#0b1725" stroke-width="1.4"/>
  <path d="M576 188 V106" fill="none" stroke="#0d7a6f" stroke-width="1.5" marker-end="url(#st)"/>

  <text x="364" y="286" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#0a5f56">two devices, two failure paths, independence by construction</text>
</svg>
"""

LIFECYCLE = [
    ("Hazard and risk assessment",
     "The tolerable risk target for each hazard — a number, not an adjective.",
     "Đánh giá mối nguy và rủi ro",
     "Mục tiêu rủi ro chấp nhận được cho từng mối nguy — một con số, không phải tính từ."),
    ("Allocate the protection layers",
     "How much risk reduction the SIS must supply, and how much the relief valve, the dike and the procedure supply.",
     "Phân bổ các lớp bảo vệ",
     "Mức giảm rủi ro mà SIS phải cung cấp, và mức mà van xả, bờ bao và quy trình cung cấp."),
    ("Safety requirements specification",
     "The SIF list: function, SIL, response time, proof test interval, and the safe state.",
     "Đặc tả yêu cầu an toàn",
     "Danh mục SIF: chức năng, SIL, thời gian đáp ứng, chu kỳ thử nghiệm chứng minh, và trạng thái an toàn."),
    ("Design and engineering",
     "Architecture, device selection, common-cause measures, and the PFD calculation that proves the number.",
     "Thiết kế và kỹ thuật",
     "Kiến trúc, chọn thiết bị, biện pháp chống nguyên nhân chung, và phép tính PFD chứng minh con số."),
    ("Installation, commissioning, validation",
     "Evidence that the system as installed meets the specification — not that it was specified correctly.",
     "Lắp đặt, chạy thử, thẩm định",
     "Bằng chứng rằng hệ đã lắp đáp ứng đặc tả — không phải rằng đặc tả đã đúng."),
    ("Operation and maintenance",
     "Proof tests, bypass registers, failure tracking, and the discipline to keep all three.",
     "Vận hành và bảo trì",
     "Thử nghiệm chứng minh, sổ theo dõi bỏ qua, ghi nhận hư hỏng, và kỷ luật để giữ cả ba."),
    ("Modification",
     "Management of change. The phase most often skipped, and the one that invalidates every calculation above.",
     "Sửa đổi",
     "Quản lý thay đổi. Giai đoạn hay bị bỏ qua nhất, và là giai đoạn vô hiệu hóa mọi phép tính ở trên."),
    ("Decommissioning",
     "Removal without leaving a hazard that the SIS was quietly holding back.",
     "Ngừng hoạt động",
     "Tháo dỡ mà không để lại mối nguy mà SIS đang âm thầm ngăn giữ."),
]

BPCS_VS_SIS = [
    ("Purpose", "Keep the process inside its normal band.",
     "Act only when the process leaves its safe limits.",
     "Mục đích", "Giữ quá trình trong dải bình thường.",
     "Chỉ tác động khi quá trình vượt giới hạn an toàn."),
    ("At rest", "Running, modulating, visible on the trend.",
     "Dormant. Watching, and doing nothing at all.",
     "Khi bình thường", "Đang chạy, điều biến, hiện trên đồ thị.",
     "Nằm im. Theo dõi, và không làm gì cả."),
    ("Action", "Continuous and analogue — a valve moves a little.",
     "Discrete and final — a valve closes.",
     "Tác động", "Liên tục và tương tự — van dịch chuyển một chút.",
     "Rời rạc và dứt khoát — van đóng lại."),
    ("Failure direction", "Fail to the last value, or to a default the process tolerates.",
     "Fail to the de-energised, safe state — by design, on loss of power.",
     "Hướng hư hỏng", "Giữ giá trị cuối, hoặc về mặc định mà quá trình chịu được.",
     "Về trạng thái an toàn khi mất điện — theo thiết kế."),
    ("Optimised for", "Availability. An unnecessary trip costs money.",
     "Integrity. An unnecessary trip is annoying; a missing one is fatal.",
     "Tối ưu cho", "Tính sẵn sàng. Một lần dừng máy không cần thiết tốn tiền.",
     "Tính toàn vẹn. Dừng máy nhầm thì phiền; bỏ sót thì chết người."),
    ("How it is proven", "Continuously, by the operator watching the trend.",
     "By proof test at an interval, and by a calculation nobody reads twice.",
     "Cách chứng minh", "Liên tục, do người vận hành theo dõi đồ thị.",
     "Bằng thử nghiệm chứng minh theo chu kỳ, và một phép tính ít ai đọc lại."),
    ("Governing standard", "ISA-101, ISA-18.2, IEC 61131-3.",
     "IEC 61511, with IEC 61508 for the devices.",
     "Tiêu chuẩn chi phối", "ISA-101, ISA-18.2, IEC 61131-3.",
     "IEC 61511, cùng IEC 61508 cho thiết bị."),
]

SIL_ROWS = [
    ("SIL 4", "10<sup>-5</sup> – 10<sup>-4</sup>", "10 000 – 100 000", "10<sup>-9</sup> – 10<sup>-8</sup>",
     "Rarely claimed in process plant. If a risk graph sends you here, question the graph."),
    ("SIL 3", "10<sup>-4</sup> – 10<sup>-3</sup>", "1 000 – 10 000", "10<sup>-8</sup> – 10<sup>-7</sup>",
     "Common for high-pressure shutdown, furnace management, overfill on a volatile tank."),
    ("SIL 2", "10<sup>-3</sup> – 10<sup>-2</sup>", "100 – 1 000", "10<sup>-7</sup> – 10<sup>-6</sup>",
     "The working level of most process SIFs."),
    ("SIL 1", "10<sup>-2</sup> – 10<sup>-1</sup>", "10 – 100", "10<sup>-6</sup> – 10<sup>-5</sup>",
     "Often satisfied by a single well-tested device and a disciplined proof test."),
]

ARCH = [
    ("1oo1", "The single device trips.",
     "&lambda;<sub>DU</sub> &times; TI / 2", "Low",
     "SIL 1 with a good device; the honest starting point for every calculation.",
     "Một thiết bị tác động.",
     "&lambda;<sub>DU</sub> &times; TI / 2", "Thấp",
     "SIL 1 với thiết bị tốt; điểm khởi đầu trung thực cho mọi phép tính."),
    ("1oo2", "Either device trips. Either one can also trip it wrongly.",
     "Second order in &lambda;<sub>DU</sub> &times; TI, plus the &beta; floor", "High",
     "SIL 3 sensors and shutdown valves — the redundancy everyone specifies.",
     "Một trong hai thiết bị tác động. Mỗi thiết bị cũng có thể tác động nhầm.",
     "Bậc hai theo &lambda;<sub>DU</sub> &times; TI, cộng với sàn &beta;", "Cao",
     "Cảm biến và van chặn đạt SIL 3 — kiểu dự phòng ai cũng chỉ định."),
    ("2oo2", "Both devices must trip.",
     "&lambda;<sub>DU</sub> &times; TI — worse than 1oo1", "Very low",
     "High availability, poor safety. Rarely used for a protective function.",
     "Cả hai thiết bị phải cùng tác động.",
     "&lambda;<sub>DU</sub> &times; TI — kém hơn 1oo1", "Rất thấp",
     "Sẵn sàng cao, an toàn kém. Ít dùng cho chức năng bảo vệ."),
    ("2oo3", "Two of the three must agree.",
     "Second order, plus the &beta; floor", "Moderate",
     "Where a spurious trip is expensive but the hazard is real — compressors, large valves.",
     "Hai trong ba thiết bị phải đồng thuận.",
     "Bậc hai, cộng với sàn &beta;", "Trung bình",
     "Nơi dừng máy nhầm tốn kém nhưng mối nguy là thật — máy nén, van lớn."),
]

PROOF = [
    ("6 months", "0.5&times;", "Two shutdowns a year, twice the paperwork."),
    ("1 year", "1&times;", "The default in most specifications, for no better reason than the turnaround."),
    ("2 years", "2&times;", "Twice the risk, half the labour. Defensible only with high proof test coverage."),
    ("5 years", "5&times;", "Five times the risk for identical hardware. The devices did not get worse; the test interval did."),
]

SHARED = [
    ("The transmitter",
     "One device feeds both the BPCS and the SIS. One diaphragm, one electronics stack, one failure mode — and the SIS learns nothing the BPCS did not already know.",
     "Bộ truyền",
     "Một thiết bị cấp tín hiệu cho cả BPCS và SIS. Một màng, một mạch điện tử, một kiểu hư hỏng — và SIS không biết gì hơn BPCS."),
    ("The impulse line",
     "Two transmitters, one tapping point. A plugged line blinds both, and both read a frozen value that looks entirely plausible.",
     "Ống xung",
     "Hai bộ truyền, một điểm lấy áp. Một ống bị tắc làm mù cả hai, và cả hai đọc một giá trị đóng băng trông hoàn toàn hợp lý."),
    ("The power supply",
     "A single 24 V feed, or a single UPS, takes both systems down together. Independence has to reach the source.",
     "Nguồn cấp",
     "Một nguồn 24 V duy nhất, hoặc một UPS duy nhất, hạ cả hai hệ cùng lúc. Tính độc lập phải với tới tận nguồn."),
    ("The I/O card",
     "Two channels on the same card share a multiplexer, a reference and a power rail. Two channels is not two paths.",
     "Card vào ra",
     "Hai kênh trên cùng một card dùng chung bộ ghép kênh, một chuẩn và một ray nguồn. Hai kênh không phải hai đường."),
    ("The engineer",
     "The same person configures the BPCS and the SIS, using the same laptop, from the same backup. The most common cause of common cause.",
     "Con người",
     "Cùng một người cấu hình BPCS và SIS, bằng cùng một laptop, từ cùng một bản sao lưu. Nguyên nhân chung phổ biến nhất."),
]

FAILURES = [
    ("The bypass that stayed in",
     "A trip is inhibited for a two-day maintenance job. The job finishes, the bypass does not. Nobody owns the register, so the SIS is off for a year and every document still says SIL 2.",
     "Lệnh bỏ qua còn nguyên",
     "Một khóa liên động bị vô hiệu hóa hai ngày để bảo trì. Việc xong, lệnh bỏ qua thì không. Không ai quản sổ theo dõi, nên SIS tắt suốt một năm và mọi tài liệu vẫn ghi SIL 2."),
    ("The plugged impulse line",
     "The transmitter is healthy, the signal is in range, the diagnostics report nothing. It is reading the pressure from last Tuesday. A frozen value is indistinguishable from a steady process.",
     "Ống xung bị tắc",
     "Bộ truyền khỏe, tín hiệu trong dải, chẩn đoán không báo gì. Nó đang đọc áp suất từ thứ Ba tuần trước. Một giá trị đóng băng không phân biệt được với một quá trình ổn định."),
    ("The valve that never moved",
     "The proof test injects a signal at the logic solver and watches the input card respond. The valve is never stroked. The seat, the stem and the actuator — where most dangerous failures live — are untested.",
     "Van không hề dịch chuyển",
     "Thử nghiệm chứng minh bơm tín hiệu tại bộ xử lý và xem card đầu vào phản hồi. Van không hề được hành trình. Đế van, trục van và cơ cấu chấp hành — nơi chứa phần lớn hư hỏng nguy hiểm — không được kiểm tra."),
    ("The trip nobody wanted",
     "A poorly chosen setpoint produces three spurious trips in commissioning. Operations asks for it to be disabled. The SIS was technically correct and practically deleted.",
     "Lần tác động không ai muốn",
     "Một giá trị đặt chọn kém gây ba lần dừng máy nhầm khi chạy thử. Vận hành yêu cầu vô hiệu hóa. SIS đúng về kỹ thuật và bị xóa trên thực tế."),
    ("The setpoint above the relief valve",
     "The SIF trips at a pressure the relief valve already handles, so it never acts. It passes every proof test because the test injects a signal, not a process condition.",
     "Giá trị đặt cao hơn van xả",
     "SIF tác động ở áp suất mà van xả đã xử lý, nên nó không bao giờ hoạt động. Nó qua mọi lần thử nghiệm vì phép thử bơm tín hiệu, không tạo điều kiện quá trình."),
    ("The calculation that was never repeated",
     "The loop was re-instrumented, the transmitter changed, the proof test interval doubled for a turnaround. The PFD calculation still reflects the original design and still says SIL 2.",
     "Phép tính không bao giờ được làm lại",
     "Vòng đo được thay thiết bị, bộ truyền đổi, chu kỳ thử nghiệm tăng gấp đôi vì đợt đại tu. Phép tính PFD vẫn phản ánh thiết kế ban đầu và vẫn ghi SIL 2."),
]

TRIGGER = [
    ("Set by", "LOPA, a risk graph, or a corporate risk matrix — a documented method.",
     "Engineering judgement, consequence, and the cost of being wrong.",
     "Do đâu mà có", "LOPA, biểu đồ rủi ro, hoặc ma trận rủi ro của công ty — một phương pháp có tài liệu.",
     "Đánh giá kỹ thuật, hậu quả, và chi phí của việc sai."),
    ("Expressed as", "A probability of failure on demand, per demand.",
     "A value and a colour: green, amber, red.",
     "Biểu diễn bằng", "Xác suất hư hỏng khi có yêu cầu, theo mỗi lần yêu cầu.",
     "Một giá trị và một màu: xanh, vàng, đỏ."),
    ("Verified by", "A PFD calculation plus a proof test with stated coverage.",
     "A reading round, a trend, and a review meeting.",
     "Được kiểm chứng bằng", "Phép tính PFD cộng với thử nghiệm chứng minh có độ bao phủ xác định.",
     "Một lượt đọc, một đồ thị, và một cuộc họp xem xét."),
    ("Failure that matters", "Dangerous undetected — the loop is silent and looks healthy.",
     "Drift, a lost cable, a sensor that reads plausible nonsense.",
     "Hư hỏng đáng lo", "Nguy hiểm không phát hiện được — vòng im lặng và trông vẫn khỏe.",
     "Trôi, mất cáp, cảm biến đọc ra số vô nghĩa nhưng hợp lý."),
    ("Independence", "Formally required from the BPCS, and audited.",
     "Usually absent: the same technician reads both systems.",
     "Tính độc lập", "Được yêu cầu chính thức so với BPCS, và được đánh giá.",
     "Thường không có: cùng một kỹ thuật viên đọc cả hai hệ."),
    ("Change control", "Management of change, revalidation, and a new calculation.",
     "A note in the next monitoring report, if anyone remembers.",
     "Kiểm soát thay đổi", "Quản lý thay đổi, thẩm định lại, và một phép tính mới.",
     "Một ghi chú trong báo cáo quan trắc sau, nếu có ai nhớ."),
]


def build():
    pg = Page(
        "safety.html",
        "saf",
        "Safety instrumented systems — SIL, proof test and independence | I&amp;C",
        "Hệ thống an toàn SIS — SIL, thử nghiệm chứng minh và tính độc lập",
        "How a safety instrumented function is specified, verified and quietly defeated: what SIL "
        "actually bounds, why redundancy stops at the common-cause floor, why the proof test interval "
        "is the dominant term, and why a monitoring trigger value is not a SIL.",
        "Cách một chức năng an toàn được đặc tả, kiểm chứng và bị vô hiệu hóa một cách âm thầm: SIL "
        "thực sự giới hạn điều gì, vì sao dự phòng dừng lại ở sàn nguyên nhân chung, vì sao chu kỳ thử "
        "nghiệm là số hạng chi phối, và vì sao một ngưỡng quan trắc không phải là SIL.",
    )

    body = page_intro(
        pg,
        "The loop that is supposed to do nothing",
        "Vòng đo lẽ ra không làm gì cả",
        "A control loop earns its keep every second. A safety loop earns its keep once, on the worst "
        "day of the plant's life, and is judged entirely on that one moment. Everything about how it "
        "is specified follows from that asymmetry.",
        "Một vòng điều khiển kiếm sống mỗi giây. Một vòng an toàn kiếm sống đúng một lần, vào ngày tồi "
        "tệ nhất của nhà máy, và bị đánh giá hoàn toàn bằng khoảnh khắc đó. Mọi thứ về cách nó được đặc "
        "tả đều suy ra từ sự bất đối xứng này.",
        [
            ("dormant", "The loop that sleeps", "Vòng luôn ngủ"),
            ("sil", "What SIL bounds", "SIL giới hạn điều gì"),
            ("arch", "Where integrity comes from", "Toàn vẹn đến từ đâu"),
            ("proof", "The proof test", "Thử nghiệm chứng minh"),
            ("indep", "Independence", "Tính độc lập"),
            ("fail", "How they fail", "Chúng hỏng thế nào"),
            ("trigger", "Not a trigger value", "Không phải một ngưỡng"),
        ],
    )

    # ---------------- 01 dormant ----------------
    body += section_open("01", "The loop that sleeps", "Vòng luôn ngủ", pg, "dormant")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("Two systems on the same pipe, optimised for opposite things",
             "Hai hệ trên cùng một đường ống, tối ưu cho hai điều trái ngược"),
        pg.p(
            "The basic process control system exists to keep the plant running. The safety instrumented "
            "system exists to stop it. They share a process connection and nothing else — and the moment "
            "they share more than that, the safety function inherits the control system's failure modes.",
            "Hệ điều khiển quá trình cơ bản tồn tại để giữ nhà máy chạy. Hệ thống an toàn tồn tại để dừng "
            "nó. Hai hệ chia sẻ một điểm đấu nối quá trình và không chia sẻ gì khác — và ngay khi chúng "
            "chia sẻ nhiều hơn thế, chức năng an toàn thừa hưởng các kiểu hư hỏng của hệ điều khiển.",
        ),
        pg.th("Aspect", "Khía cạnh"),
        pg.th("Basic control (BPCS)", "Điều khiển cơ bản (BPCS)"),
        pg.th("Safety instrumented (SIS)", "An toàn (SIS)"),
    )
    for aspect, b, s, aspect_vi, b_vi, s_vi in BPCS_VS_SIS:
        body += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            pg.span(aspect, aspect_vi),
            pg.span(b, b_vi),
            pg.span(s, s_vi),
        )
    body += """
  </tbody>
</table>
</div>
<div class="note warn mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.span("The word that does the damage", "Từ gây ra hậu quả"),
        pg.p(
            "&ldquo;Redundant&rdquo; is not a synonym for &ldquo;independent&rdquo;. Two transmitters on "
            "one impulse line are redundant and not independent. One transmitter on two I/O cards is "
            "neither. Independence is a property of the whole path — sensor, cable, card, power, "
            "software, and the person who configured it.",
            "&ldquo;Dự phòng&rdquo; không đồng nghĩa với &ldquo;độc lập&rdquo;. Hai bộ truyền trên một "
            "ống xung là dự phòng và không độc lập. Một bộ truyền trên hai card vào ra thì không được cả "
            "hai. Tính độc lập là thuộc tính của toàn bộ đường đi — cảm biến, cáp, card, nguồn, phần mềm, "
            "và cả người đã cấu hình nó.",
        ),
    )
    body += section_close()

    # ---------------- 02 SIL ----------------
    body += section_open("02", "What SIL bounds", "SIL giới hạn điều gì", pg, "sil")
    body += """
<div class="sec-head">
  %s
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("A number attached to a function, not to a device",
             "Một con số gắn với chức năng, không phải với thiết bị"),
        pg.p(
            "SIL is the risk reduction a safety function must deliver, expressed as the probability "
            "that it fails to act when demanded. Low demand means the function is asked to work less "
            "than once a year — which is the case for almost every process trip.",
            "SIL là mức giảm rủi ro mà một chức năng an toàn phải mang lại, biểu diễn bằng xác suất nó "
            "không tác động khi được yêu cầu. Nhu cầu thấp nghĩa là chức năng được yêu cầu ít hơn một lần "
            "mỗi năm — đó là trường hợp của gần như mọi khóa bảo vệ trong quá trình.",
        ),
        pg.p(
            "Read the table as a budget, not a badge. A SIL 2 function may fail to act once in a "
            "hundred demands; whether that is acceptable depends on what happens next, which is a "
            "question for the risk assessment, not for the instrument engineer alone.",
            "Hãy đọc bảng này như một ngân sách, không phải một huy hiệu. Một chức năng SIL 2 có thể "
            "không tác động một lần trong một trăm lần yêu cầu; liệu điều đó chấp nhận được hay không phụ "
            "thuộc vào điều gì xảy ra tiếp theo — đó là câu hỏi cho đánh giá rủi ro, không chỉ cho kỹ sư "
            "thiết bị.",
        ),
        pg.th("Level", "Mức"),
        pg.th("PFD<sub>avg</sub> · low demand", "PFD<sub>avg</sub> · nhu cầu thấp"),
        pg.th("Risk reduction", "Giảm rủi ro"),
        pg.th("PFH · high demand", "PFH · nhu cầu cao"),
    )
    for lvl, pfd, rrf, pfh, note in SIL_ROWS:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            pg.span(lvl, lvl),
            pg.span(pfd, pfd),
            pg.span(rrf, rrf),
            pg.span(pfh, pfh),
        )
    body += """
  </tbody>
</table>
</div>
<div class="note warn mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.span("The most expensive misunderstanding in the discipline", "Hiểu lầm tốn kém nhất của ngành"),
        pg.p(
            "A SIL 3 transmitter does not make a SIL 3 loop. The SIL belongs to the function, which is "
            "the sensor, the logic solver, the final element and the proof test regime taken together. "
            "The final element is usually the weakest of the four — a shutdown valve that has never been "
            "stroked is a SIL 3 device with an unknown PFD.",
            "Một bộ truyền SIL 3 không tạo ra một vòng SIL 3. SIL thuộc về chức năng, tức là cảm biến, bộ "
            "xử lý, phần tử chấp hành và chế độ thử nghiệm chứng minh, gộp lại. Phần tử chấp hành thường "
            "là mắt yếu nhất trong bốn — một van chặn chưa từng được hành trình là thiết bị SIL 3 với PFD "
            "chưa biết.",
        ),
    )
    body += section_close()

    # ---------------- 03 architecture ----------------
    body += section_open("03", "Where integrity comes from", "Toàn vẹn đến từ đâu", pg, "arch")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="formula">
  <i>%s</i><br>
  PFD<sub>avg</sub>(1oo1) = &lambda;<sub>DU</sub> &times; TI / 2<br>
  <i>%s</i><br>
  PFD<sub>floor</sub> = &beta; &times; &lambda;<sub>DU</sub> &times; TI / 2<br>
  <span class="r">%s</span>
</div>
<div class="tbl-wrap mt24">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("Redundancy buys orders of magnitude, until &beta; sets the floor",
             "Dự phòng mua được nhiều bậc độ lớn, cho đến khi &beta; đặt sàn"),
        pg.p(
            "A single device fails dangerously at a rate &lambda;<sub>DU</sub> per hour and is only "
            "tested every TI hours, so on average it spends half the interval failed and undetected. "
            "Redundancy attacks that term — but two devices that share a diaphragm, a power supply or "
            "an engineer can fail together, and that fraction &beta; cannot be voted away.",
            "Một thiết bị đơn hư hỏng nguy hiểm với tốc độ &lambda;<sub>DU</sub> mỗi giờ và chỉ được "
            "kiểm tra mỗi TI giờ, nên trung bình nó ở trạng thái hư hỏng mà không bị phát hiện trong nửa "
            "khoảng đó. Dự phòng tấn công số hạng này — nhưng hai thiết bị dùng chung màng, nguồn, hoặc "
            "một kỹ sư có thể hỏng cùng lúc, và phần &beta; đó không thể bỏ phiếu để loại trừ.",
        ),
        pg.span("One device, tested once per interval:", "Một thiết bị, kiểm tra một lần mỗi chu kỳ:"),
        pg.span("Shared causes are not voted away:", "Nguyên nhân chung không bị bỏ phiếu loại trừ:"),
        pg.span("Redundancy only shrinks the (1 &minus; &beta;) part.",
                "Dự phòng chỉ thu nhỏ phần (1 &minus; &beta;)."),
        pg.th("Architecture", "Kiến trúc"),
        pg.th("Trips when", "Tác động khi"),
        pg.th("PFD shape", "Dạng PFD"),
        pg.th("Spurious trips", "Tác động nhầm"),
        pg.th("Where it is used", "Dùng ở đâu"),
    )
    for arch, when, shape, spur, use, when_vi, shape_vi, spur_vi, use_vi in ARCH:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            pg.span(arch, arch),
            pg.span(when, when_vi),
            pg.span(shape, shape_vi),
            pg.span(spur, spur_vi),
            pg.span(use, use_vi),
        )
    body += """
  </tbody>
</table>
</div>
<div class="note mt24">
  <span class="lbl">%s</span>
  %s
  <p>%s</p>
</div>
""" % (
        pg.span("Worked example", "Ví dụ tính toán"),
        pg.p(
            "Take &lambda;<sub>DU</sub> = 5 &times; 10<sup>-7</sup> per hour and a one-year proof test "
            "interval of 8 760 hours. A single device gives PFD = 5 &times; 10<sup>-7</sup> &times; "
            "8 760 / 2 = 2.2 &times; 10<sup>-3</sup>, which is SIL 2.",
            "Lấy &lambda;<sub>DU</sub> = 5 &times; 10<sup>-7</sup> mỗi giờ và chu kỳ thử nghiệm một năm "
            "là 8 760 giờ. Một thiết bị đơn cho PFD = 5 &times; 10<sup>-7</sup> &times; 8 760 / 2 = "
            "2,2 &times; 10<sup>-3</sup>, tức SIL 2.",
        ),
        pg.p(
            "Duplicate it with &beta; = 0.1 and the floor is 0.1 &times; 2.2 &times; 10<sup>-3</sup> = "
            "2.2 &times; 10<sup>-4</sup> — SIL 3, and no further redundancy helps. Raise &beta; to 0.2 "
            "and the floor doubles to 4.4 &times; 10<sup>-4</sup>. The second device bought one level; "
            "the shared power supply took it back.",
            "Nhân đôi thiết bị với &beta; = 0,1 và sàn là 0,1 &times; 2,2 &times; 10<sup>-3</sup> = "
            "2,2 &times; 10<sup>-4</sup> — SIL 3, và không dự phòng thêm nào giúp được. Tăng &beta; lên "
            "0,2 thì sàn tăng gấp đôi thành 4,4 &times; 10<sup>-4</sup>. Thiết bị thứ hai mua được một "
            "mức; nguồn dùng chung lấy lại mức đó.",
        ),
    )
    body += section_close()

    # ---------------- 04 proof test ----------------
    body += section_open("04", "The proof test", "Thử nghiệm chứng minh", pg, "proof")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("The interval is the term you actually control",
             "Chu kỳ là số hạng bạn thực sự kiểm soát"),
        pg.p(
            "PFD is linear in the proof test interval. Nobody can change the device's failure rate once "
            "it is on the pipe, but anybody can decide how often it gets tested — and that decision "
            "moves the number just as far.",
            "PFD tỷ lệ tuyến tính với chu kỳ thử nghiệm chứng minh. Không ai đổi được tốc độ hư hỏng của "
            "thiết bị khi nó đã lắp lên tuyến, nhưng ai cũng quyết định được tần suất kiểm tra — và quyết "
            "định đó dịch chuyển con số xa tương đương.",
        ),
        pg.th("Interval", "Chu kỳ"),
        pg.th("PFD relative to one year", "PFD so với một năm"),
        pg.th("What it really costs", "Cái giá thật"),
    )
    for interval, mult, cost in PROOF:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>" % (
            pg.span(interval, interval),
            pg.span(mult, mult),
            pg.span(cost, cost),
        )
    body += """
  </tbody>
</table>
</div>
<div class="g-2-1 mt24">
  <div>
    %s
    %s
    %s
  </div>
  <div class="card">
    <span class="n">%s</span>
    <h3>%s</h3>
    <div class="spec" style="margin-top:12px">
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
    </div>
  </div>
</div>
""" % (
        pg.h3("Coverage decides what the interval is worth", "Độ bao phủ quyết định giá trị của chu kỳ"),
        pg.p(
            "A proof test does not test the function; it tests the part of the function the test "
            "reaches. That fraction is the proof test coverage, and whatever it misses behaves as if "
            "it had never been tested at all.",
            "Một thử nghiệm chứng minh không kiểm tra chức năng; nó kiểm tra phần chức năng mà phép thử "
            "với tới. Phần đó là độ bao phủ, và phần bị bỏ sót hành xử như thể chưa từng được kiểm tra.",
        ),
        pg.p(
            "For a shutdown valve, a test that injects a signal at the logic solver and watches the "
            "input card change state proves the wiring and nothing else. The seat, the stem, the "
            "spring return and the actuator — where most dangerous failures actually live — are "
            "untouched. A partial stroke test is better and still incomplete: it exercises the "
            "movement but not the closure.",
            "Với van chặn, một phép thử bơm tín hiệu tại bộ xử lý và xem card đầu vào đổi trạng thái chỉ "
            "chứng minh phần dây dẫn và không gì khác. Đế van, trục van, lò xo hồi vị và cơ cấu chấp hành "
            "— nơi phần lớn hư hỏng nguy hiểm thực sự nằm — không bị chạm tới. Thử hành trình một phần "
            "thì tốt hơn và vẫn chưa đủ: nó kiểm tra chuyển động nhưng không kiểm tra việc đóng kín.",
        ),
        pg.span("Coverage", "Độ bao phủ"),
        pg.h3("What the test reaches", "Phép thử với tới đâu"),
        pg.td("Loop powered, signal injected", "Cấp vòng, bơm tín hiệu"),
        pg.td("Wiring and logic only — the lowest useful coverage.", "Chỉ dây dẫn và logic — mức thấp nhất còn có ích."),
        pg.td("Partial stroke", "Hành trình một phần"),
        pg.td("Movement and position feedback; not the seat.", "Chuyển động và phản hồi vị trí; không gồm đế van."),
        pg.td("Full stroke to seat", "Hành trình đầy tới đế"),
        pg.td("The closure itself, which is what the trip needs.", "Chính việc đóng kín, thứ mà lần tác động cần đến."),
    )
    body += section_close()

    # ---------------- 05 independence ----------------
    body += section_open("05", "Independence", "Tính độc lập", pg, "indep")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="figure">
  %s
  <div class="figcap">%s</div>
</div>
""" % (
        pg.h2("A wiring diagram, not an intention", "Một sơ đồ đấu dây, không phải một ý định"),
        pg.p(
            "IEC 61511 requires the safety function to be independent of the control function. The "
            "requirement is easy to state, cheap to draw, and routinely defeated by a shared terminal "
            "block that nobody documented.",
            "IEC 61511 yêu cầu chức năng an toàn phải độc lập với chức năng điều khiển. Yêu cầu này dễ "
            "phát biểu, rẻ để vẽ, và thường bị vô hiệu hóa bởi một hộp đấu dây dùng chung mà không ai ghi "
            "lại.",
        ),
        INDEP_SVG,
        pg.span(
            "Left: one transmitter, two consumers — the safety function inherits every failure of the "
            "control loop. Right: separate devices, separate paths, independence you can point at.",
            "Trái: một bộ truyền, hai nơi dùng — chức năng an toàn thừa hưởng mọi hư hỏng của vòng điều "
            "khiển. Phải: thiết bị riêng, đường riêng, tính độc lập chỉ tay vào được.",
        ),
    )

    body += """
<div class="sec-head mt40">
  %s
  %s
</div>
<div class="grid c2">
""" % (
        pg.h3("Five things that are shared without anyone deciding to share them",
             "Năm thứ bị dùng chung mà không ai quyết định dùng chung"),
        pg.p(
            "Each of these appears on a real project as a cost saving. Each of them reduces &beta; "
            "resistance to zero and quietly converts a redundant architecture into a single point of "
            "failure.",
            "Mỗi thứ dưới đây xuất hiện trong một dự án thực tế như một khoản tiết kiệm. Mỗi thứ đưa khả "
            "năng chống &beta; về không và âm thầm biến một kiến trúc dự phòng thành một điểm hỏng duy nhất.",
        ),
    )
    for title, text, title_vi, text_vi in SHARED:
        body += '<div class="card"><h3>%s</h3><p>%s</p></div>' % (
            pg.span(title, title_vi),
            pg.span(text, text_vi),
        )
    body += """
</div>
""" % ()
    body += section_close()

    # ---------------- 06 failures ----------------
    body += section_open("06", "How they fail", "Chúng hỏng thế nào", pg, "fail")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="grid c3">
""" % (
        pg.h2("Six ways a safety system stops being one",
             "Sáu cách một hệ an toàn không còn là hệ an toàn"),
        pg.p(
            "Almost none of these are device failures. The hardware is usually fine. What fails is the "
            "regime around it — the register, the test, the setpoint, the assumption that the "
            "calculation still describes the plant.",
            "Gần như không có trường hợp nào là hỏng thiết bị. Phần cứng thường vẫn tốt. Cái hỏng là chế "
            "độ bao quanh nó — sổ theo dõi, phép thử, giá trị đặt, và giả định rằng phép tính vẫn mô tả "
            "đúng nhà máy.",
        ),
    )
    for title, text, title_vi, text_vi in FAILURES:
        body += '<div class="card"><h3>%s</h3><p>%s</p></div>' % (
            pg.span(title, title_vi),
            pg.span(text, text_vi),
        )
    body += """
</div>
""" % ()
    body += section_close()

    # ---------------- 07 trigger ----------------
    body += section_open("07", "Not a trigger value", "Không phải một ngưỡng", pg, "trigger")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("Why a monitoring threshold is not a safety function",
             "Vì sao một ngưỡng quan trắc không phải một chức năng an toàn"),
        pg.p(
            "The comparison page argues that geotechnical monitoring leaves the loop open on purpose. "
            "The same argument explains why a trigger value cannot be handed a SIL: there is no "
            "actuator to make the function act, so there is nothing whose failure probability could be "
            "calculated.",
            "Trang so sánh lập luận rằng quan trắc địa kỹ thuật cố ý để vòng hở. Lập luận đó cũng giải "
            "thích vì sao không thể gán SIL cho một ngưỡng: không có cơ cấu chấp hành để chức năng tác "
            "động, nên không có gì để tính xác suất hư hỏng.",
        ),
        pg.th("Compared on", "So sánh theo"),
        pg.th("SIL target", "Mục tiêu SIL"),
        pg.th("Geotechnical trigger", "Ngưỡng địa kỹ thuật"),
    )
    for aspect, a, b, aspect_vi, a_vi, b_vi in TRIGGER:
        body += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            pg.span(aspect, aspect_vi),
            pg.span(a, a_vi),
            pg.span(b, b_vi),
        )
    body += """
  </tbody>
</table>
</div>
<div class="note mt24">
  <span class="lbl">%s</span>
  %s
</div>
<div class="note warn mt24">
  <span class="lbl">%s</span>
  %s
</div>
<div class="nextprev">
  <a href="control.html"><span class="k">%s</span>%s</a>
  <a href="tools.html" style="text-align:right"><span class="k">%s</span>%s</a>
</div>
""" % (
        pg.span("Where the two do meet", "Nơi hai thứ thực sự gặp nhau"),
        pg.p(
            "A geotechnical measurement can still be part of a safety function — a piezometer that "
            "trips a dewatering pump, a slope extensometer that closes a pipeline valve. In that case "
            "the sensor is one link in a function that does have an actuator, and the function can "
            "carry a SIL. What cannot carry a SIL is the measurement alone, or the threshold on a "
            "dashboard.",
            "Một phép đo địa kỹ thuật vẫn có thể là một phần của chức năng an toàn — đầu đo áp lực nước "
            "tác động bơm hạ mực nước, máy đo chuyển vị mái dốc đóng van tuyến ống. Khi đó cảm biến là "
            "một mắt trong chức năng có cơ cấu chấp hành, và chức năng đó có thể mang SIL. Thứ không thể "
            "mang SIL là phép đo đơn lẻ, hoặc một ngưỡng trên bảng điều khiển.",
        ),
        pg.span("If you take one thing from this page", "Nếu chỉ nhớ một điều từ trang này"),
        pg.p(
            "Ask for the proof test procedure before you accept the SIL claim. The certificate "
            "describes a device on a bench; the procedure describes what will actually happen on your "
            "plant, at three in the morning, by the technician who is on shift.",
            "Hãy yêu cầu quy trình thử nghiệm chứng minh trước khi chấp nhận tuyên bố SIL. Giấy chứng "
            "nhận mô tả một thiết bị trên bàn thử; quy trình mô tả điều thực sự sẽ xảy ra tại nhà máy của "
            "bạn, lúc ba giờ sáng, bởi kỹ thuật viên đang trực.",
        ),
        pg.span("Back", "Quay lại"),
        pg.span("Control &amp; tuning", "Điều khiển &amp; hiệu chỉnh"),
        pg.span("Next", "Tiếp"),
        pg.span("Tools", "Công cụ"),
    )
    body += section_close()

    write("safety.html", render(pg, body, "safety.html"))
