# -*- coding: utf-8 -*-
"""Process vs geotechnical comparison page."""

from framework import Page, section_open, section_close, write, render, page_intro

SPLIT_SVG = """
<svg viewBox="0 0 680 330" role="img" aria-label="Closed control loop on a pipe compared with an open geotechnical monitoring loop">
  <defs>
    <marker id="c1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#0d7a6f"/>
    </marker>
    <marker id="c2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#0b1725"/>
    </marker>
    <pattern id="hatch" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#ccd7e3" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- ============ LEFT: closed loop ============ -->
  <text x="24" y="26" font-family="'IBM Plex Mono',monospace" font-size="10" letter-spacing="1.6" fill="#0a5f56">CLOSED LOOP</text>
  <text x="24" y="42" font-family="'IBM Plex Mono',monospace" font-size="9" fill="#66788d">the system corrects itself</text>

  <!-- pipe -->
  <line x1="24" y1="252" x2="300" y2="252" stroke="#0b1725" stroke-width="2"/>
  <polygon points="150,252 138,246 138,258" fill="#0b1725"/>

  <!-- valve -->
  <polygon points="246,240 246,264 264,252" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <polygon points="264,240 264,264 246,252" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <line x1="255" y1="240" x2="255" y2="216" stroke="#0b1725" stroke-width="1.6"/>
  <path d="M241 216 A14 12 0 0 1 269 216 Z" fill="#fff" stroke="#0b1725" stroke-width="1.6"/>

  <!-- transmitter -->
  <line x1="90" y1="252" x2="90" y2="172" stroke="#0b1725" stroke-width="1.4"/>
  <circle cx="90" cy="148" r="24" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <text x="90" y="152" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" font-weight="600" fill="#0b1725">FT</text>

  <!-- controller -->
  <rect x="146" y="126" width="76" height="44" rx="5" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <text x="184" y="145" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="11" font-weight="600" fill="#0b1725">PID</text>
  <text x="184" y="158" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="8" fill="#66788d">controller</text>

  <!-- signals -->
  <line x1="114" y1="148" x2="144" y2="148" stroke="#0d7a6f" stroke-width="1.6" marker-end="url(#c1)"/>
  <path d="M222 148 H255 V214" fill="none" stroke="#0d7a6f" stroke-width="1.6" marker-end="url(#c1)"/>
  <text x="255" y="286" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#66788d">valve moves, PV returns</text>

  <!-- ============ divider ============ -->
  <line x1="330" y1="18" x2="330" y2="312" stroke="#ccd7e3" stroke-width="1" stroke-dasharray="3 5"/>

  <!-- ============ RIGHT: open loop ============ -->
  <text x="356" y="26" font-family="'IBM Plex Mono',monospace" font-size="10" letter-spacing="1.6" fill="#a85a06">OPEN LOOP</text>
  <text x="356" y="42" font-family="'IBM Plex Mono',monospace" font-size="9" fill="#66788d">a person closes it, slowly</text>

  <!-- ground -->
  <rect x="356" y="190" width="176" height="104" fill="#f7f9fc" stroke="#ccd7e3" stroke-width="1"/>
  <rect x="356" y="190" width="176" height="104" fill="url(#hatch)" opacity=".8"/>
  <line x1="356" y1="190" x2="532" y2="190" stroke="#66788d" stroke-width="1.6"/>

  <!-- borehole + sensor -->
  <line x1="404" y1="190" x2="404" y2="272" stroke="#0b1725" stroke-width="1.4"/>
  <rect x="398" y="248" width="12" height="14" fill="#a85a06" stroke="#0b1725" stroke-width="1"/>
  <text x="386" y="286" font-family="'IBM Plex Mono',monospace" font-size="9" fill="#66788d">PZ</text>

  <!-- cable -->
  <path d="M404 248 V158 H448" fill="none" stroke="#0b1725" stroke-width="1.4"/>

  <!-- logger -->
  <rect x="448" y="138" width="80" height="40" rx="4" fill="#fff" stroke="#0b1725" stroke-width="1.6"/>
  <text x="488" y="156" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9.5" fill="#0b1725">logger</text>
  <text x="488" y="168" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="8" fill="#66788d">1/day</text>

  <!-- engineer -->
  <line x1="528" y1="158" x2="556" y2="158" stroke="#0b1725" stroke-width="1.4" marker-end="url(#c2)"/>
  <rect x="556" y="138" width="82" height="40" rx="4" fill="#fff" stroke="#0b1725" stroke-width="1.6"/>
  <text x="597" y="156" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9.5" fill="#0b1725">engineer</text>
  <text x="597" y="168" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="8" fill="#66788d">review</text>

  <!-- action -->
  <line x1="597" y1="178" x2="597" y2="216" stroke="#0b1725" stroke-width="1.4" marker-end="url(#c2)"/>
  <rect x="556" y="216" width="82" height="40" rx="4" fill="#fff" stroke="#0b1725" stroke-width="1.6"/>
  <text x="597" y="234" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9" fill="#0b1725">site action</text>
  <text x="597" y="246" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="8" fill="#66788d">stop, dewater</text>

  <!-- slow return, dashed -->
  <path d="M556 236 H532" fill="none" stroke="#a85a06" stroke-width="1.3" stroke-dasharray="4 3" marker-end="url(#c2)"/>
  <text x="470" y="312" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#a85a06">no actuator on the ground itself</text>
</svg>
"""

MATRIX = [
    ("group", "Purpose", "Mục đích"),
    ("Primary objective",
     "Hold a variable at a target, continuously.",
     "Detect and quantify change, reliably.",
     "Giữ một biến ở giá trị đích, liên tục.",
     "Phát hiện và định lượng thay đổi, đáng tin cậy."),
    ("Success looks like",
     "PV inside the band, offset eliminated, no oscillation.",
     "Trend below threshold, no surprise, decision made in time.",
     "PV nằm trong dải, hết offset, không dao động.",
     "Xu hướng dưới ngưỡng, không bất ngờ, quyết định kịp thời."),
    ("Who decides",
     "The controller, every scan — milliseconds.",
     "An engineer or geologist, on a review cycle — days.",
     "Bộ điều khiển, mỗi chu kỳ quét — mili giây.",
     "Kỹ sư hoặc địa chất, theo chu kỳ xem xét — ngày."),

    ("group", "The system", "Hệ thống"),
    ("Physical scale",
     "Centimetres to tens of metres: a pipe, a vessel, a column.",
     "Metres to kilometres: a slope, a dam, a tunnel alignment.",
     "Từ xentimét đến vài chục mét: đường ống, bình chứa, cột.",
     "Từ mét đến kilômét: mái dốc, đập, tuyến hầm."),
    ("Boundary conditions",
     "Known and engineered — geometry is on a drawing.",
     "Inferred from a few boreholes; uncertainty is the design input.",
     "Đã biết và do con người tạo ra — hình học có trên bản vẽ.",
     "Suy ra từ vài lỗ khoan; bất định chính là đầu vào thiết kế."),
    ("Dominant time constant",
     "Seconds to minutes.",
     "Days to years.",
     "Từ giây đến phút.",
     "Từ ngày đến năm."),
    ("Model quality",
     "Adequate for tuning; first-order plus dead time is often enough.",
     "Poor. The observational method replaces the model with measurement.",
     "Đủ để hiệu chỉnh; bậc một có trễ thường là đủ.",
     "Kém. Phương pháp quan trắc thay mô hình bằng chính phép đo."),

    ("group", "The loop", "Vòng điều khiển"),
    ("Paradigm",
     "Closed loop. Measurement feeds back into action automatically.",
     "Open loop. Measurement feeds a decision, and a person acts.",
     "Vòng kín. Kết quả đo tự động quay lại thành tác động.",
     "Vòng hở. Kết quả đo dẫn đến quyết định, và con người hành động."),
    ("Actuator",
     "Valve, damper, VFD, heater — continuously modulated.",
     "None on the structure. The &ldquo;actuator&rdquo; is construction: stop, dewater, strut, evacuate.",
     "Van, cánh gió, biến tần, gia nhiệt — điều biến liên tục.",
     "Không có trên kết cấu. &ldquo;Cơ cấu chấp hành&rdquo; là thi công: dừng, hạ mực nước, chống đỡ, sơ tán."),
    ("Setpoint equivalent",
     "A number the loop holds indefinitely.",
     "A threshold that triggers a response — green / amber / red.",
     "Một con số mà vòng giữ vô thời hạn.",
     "Một ngưỡng kích hoạt phản ứng — xanh / vàng / đỏ."),
    ("Correction rate",
     "Continuous, 100 ms to a few seconds.",
     "Discrete and slow: a reading round, a report, a site instruction.",
     "Liên tục, 100 ms đến vài giây.",
     "Rời rạc và chậm: một lượt đọc, một báo cáo, một chỉ dẫn hiện trường."),

    ("group", "Measurement", "Đo lường"),
    ("Typical variables",
     "Pressure, temperature, flow, level, composition.",
     "Displacement, pore pressure, load, strain, tilt, settlement.",
     "Áp suất, nhiệt độ, lưu lượng, mức, thành phần.",
     "Chuyển vị, áp lực nước lỗ rỗng, tải trọng, biến dạng, nghiêng, lún."),
    ("Sensor location",
     "Wetted, in-line, accessible — replaceable in an hour.",
     "Grouted into a borehole or embedded in concrete — often unrecoverable.",
     "Tiếp xúc môi trường, trên tuyến, tiếp cận được — thay trong một giờ.",
     "Chèn vữa trong lỗ khoan hoặc đúc trong bê tông — thường không thể thu hồi."),
    ("Accuracy target",
     "0.1–1 % of span, traceable to a standard.",
     "0.1–1 mm, 0.1 kPa — repeatability and stability matter more than absolute accuracy.",
     "0,1–1 % dải đo, truy xuất được về chuẩn.",
     "0,1–1 mm, 0,1 kPa — độ lặp lại và độ ổn định quan trọng hơn độ chính xác tuyệt đối."),
    ("Sampling interval",
     "100 ms – 1 s.",
     "1 minute – 1 day, often 1–4 readings per day.",
     "100 ms – 1 s.",
     "1 phút – 1 ngày, thường 1–4 lần đọc mỗi ngày."),
    ("Service life",
     "5–15 years, maintained and recalibrated.",
     "Project life: 10–50 years, sealed, often with no access.",
     "5–15 năm, được bảo trì và hiệu chuẩn lại.",
     "Vòng đời dự án: 10–50 năm, kín, thường không tiếp cận được."),

    ("group", "Engineering", "Kỹ thuật"),
    ("Governing standards",
     "ISA-5.1, IEC 61131-3, IEC 61511, API RP 551 / 554.",
     "ISO 18674-1 to -8, EN 1997-1 §2.7, ISO 22475-1.",
     "ISA-5.1, IEC 61131-3, IEC 61511, API RP 551 / 554.",
     "ISO 18674-1 đến -8, EN 1997-1 §2.7, ISO 22475-1."),
    ("Calibration",
     "Bench calibration, 1–2 year cycle, adjustable zero and span.",
     "Field check against a readout unit; the sensor may not be removable at all.",
     "Hiệu chuẩn trên bàn, chu kỳ 1–2 năm, điều chỉnh được zero và span.",
     "Kiểm tra tại hiện trường bằng bộ đọc; cảm biến có thể không tháo ra được."),
    ("Failure consequence",
     "Off-spec product, trip, emissions — recoverable.",
     "Undetected movement, then collapse — not recoverable.",
     "Sản phẩm sai quy cách, dừng máy, phát thải — có thể khắc phục.",
     "Chuyển vị không được phát hiện, rồi sụp đổ — không thể khắc phục."),
    ("Redundancy",
     "Voting for safety integrity: 1oo2, 2oo3.",
     "Duplicate sensors, or a second method that measures the same thing differently.",
     "Bỏ phiếu để đảm bảo toàn vẹn an toàn: 1oo2, 2oo3.",
     "Cảm biến dự phòng, hoặc phương pháp thứ hai đo cùng đại lượng theo cách khác."),
    ("Cost driver",
     "Device, installation labour, engineering hours.",
     "Drilling, access, cable route, and longevity of an unrecoverable sensor.",
     "Thiết bị, nhân công lắp đặt, giờ kỹ thuật.",
     "Khoan, tiếp cận, tuyến cáp, và tuổi thọ của cảm biến không thể thu hồi."),
]

ASPECT_VI = {
    "Primary objective": "Mục tiêu chính",
    "Success looks like": "Thành công trông ra sao",
    "Who decides": "Ai quyết định",
    "Physical scale": "Quy mô vật lý",
    "Boundary conditions": "Điều kiện biên",
    "Dominant time constant": "Hằng số thời gian trội",
    "Model quality": "Chất lượng mô hình",
    "Paradigm": "Mô hình điều khiển",
    "Actuator": "Cơ cấu chấp hành",
    "Setpoint equivalent": "Tương đương giá trị đặt",
    "Correction rate": "Tần suất hiệu chỉnh",
    "Typical variables": "Biến đo điển hình",
    "Sensor location": "Vị trí cảm biến",
    "Accuracy target": "Mục tiêu độ chính xác",
    "Sampling interval": "Chu kỳ lấy mẫu",
    "Service life": "Tuổi thọ phục vụ",
    "Governing standards": "Tiêu chuẩn chi phối",
    "Calibration": "Hiệu chuẩn",
    "Failure consequence": "Hậu quả hư hỏng",
    "Redundancy": "Dự phòng",
    "Cost driver": "Yếu tố chi phí",
}

TRAPS = [
    ("Instrument",
     "A transmitter with a standardised output you can wire into a control system.",
     "A sensor plus a readout, often vibrating wire, read on a campaign basis.",
     "Một bộ truyền có đầu ra chuẩn hóa, đấu được vào hệ điều khiển.",
     "Một cảm biến cộng bộ đọc, thường loại dây rung, đọc theo đợt."),
    ("Accuracy",
     "Percent of span, under reference conditions, traceable.",
     "Percent of full scale, dominated by installation and grout, rarely traceable.",
     "Phần trăm dải đo, trong điều kiện chuẩn, truy xuất được.",
     "Phần trăm thang đầy, bị chi phối bởi lắp đặt và vữa, hiếm khi truy xuất được."),
    ("Drift",
     "Zero and span drift, corrected at the next calibration.",
     "Slow sensor drift over years, often never corrected because the sensor is buried.",
     "Trôi zero và span, được hiệu chỉnh ở lần hiệu chuẩn sau.",
     "Trôi chậm của cảm biến qua nhiều năm, thường không bao giờ được hiệu chỉnh vì cảm biến bị chôn."),
    ("Alarm",
     "An ISA-18.2 rationalised alarm with a defined response time.",
     "A threshold notification in a three-tier trigger-action plan.",
     "Một cảnh báo được hợp lý hóa theo ISA-18.2 với thời gian đáp ứng xác định.",
     "Một thông báo ngưỡng trong kế hoạch ngưỡng–hành động ba cấp."),
    ("Loop",
     "A closed control loop with a controller and a final element.",
     "A reading round: the route a technician walks with a readout unit.",
     "Một vòng điều khiển kín với bộ điều khiển và phần tử chấp hành.",
     "Một lượt đọc: tuyến kỹ thuật viên đi với bộ đọc."),
    ("Range",
     "The 4–20 mA span, set by the configured LRV and URV.",
     "The physical measurement range of the sensor, fixed at manufacture.",
     "Dải 4–20 mA, do LRV và URV cấu hình quyết định.",
     "Dải đo vật lý của cảm biến, cố định từ khi sản xuất."),
]


def build():
    pg = Page(
        "comparison.html",
        "cmp",
        "Process control vs geotechnical monitoring — the real difference | I&amp;C",
        "Điều khiển quá trình vs quan trắc địa kỹ thuật — khác biệt thực sự",
        "A structured comparison of process instrumentation and control against geotechnical "
        "monitoring: closed loop versus open loop, small controllable systems versus large "
        "structures, and where the two disciplines meet.",
        "So sánh có hệ thống giữa đo lường điều khiển quá trình và quan trắc địa kỹ thuật: vòng kín "
        "so với vòng hở, hệ nhỏ điều khiển được so với kết cấu lớn, và nơi hai ngành gặp nhau.",
        embeddable=True,
    )

    body = page_intro(
        pg,
        "Two disciplines, one word",
        "Hai ngành, một từ",
        "Both put instruments on a structure and read numbers. One of them then does something about "
        "it, automatically and continuously. The other writes a report. That difference is not "
        "cultural — it follows from whether the system has a controllable input.",
        "Cả hai đều gắn thiết bị lên một kết cấu và đọc số. Một bên sau đó tự động làm gì đó với con số "
        "ấy, liên tục. Bên kia viết báo cáo. Khác biệt đó không phải văn hóa — nó xuất phát từ việc hệ "
        "có đầu vào điều khiển được hay không.",
        [
            ("matrix", "The comparison matrix", "Bảng so sánh"),
            ("why", "Why the loop stays open", "Vì sao vòng để hở"),
            ("hybrid", "Where the two meet", "Nơi hai ngành gặp nhau"),
            ("vocab", "Vocabulary traps", "Bẫy thuật ngữ"),
            ("practice", "In practice", "Thực tiễn"),
        ],
    )
    body += """
<section class="sec" style="padding-top:44px">
  <div class="wrap">
    <div class="figure">
      %s
      <div class="figcap">%s</div>
    </div>
  </div>
</section>
""" % (
        SPLIT_SVG,
        pg.span(
            "Left: the loop closes itself. Right: the loop is closed by a person, days later.",
            "Trái: vòng tự khép kín. Phải: vòng được khép bởi con người, nhiều ngày sau.",
        ),
    )

    # matrix
    body += section_open("01", "The matrix", "Bảng so sánh", pg, "matrix")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl matrix">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("Twenty-one lines that separate the disciplines", "Hai mươi mốt dòng phân tách hai ngành"),
        pg.p(
            "Read down a column to understand one discipline; read across a row to see the trade-off. "
            "The first column stays pinned while you scroll on a narrow screen.",
            "Đọc theo cột để hiểu một ngành; đọc theo hàng để thấy sự đánh đổi. Cột đầu được ghim lại "
            "khi cuộn trên màn hình hẹp.",
        ),
        pg.th("Aspect", "Khía cạnh"),
        pg.th("Process I&amp;C", "Đo lường &amp; điều khiển quá trình"),
        pg.th("Geotechnical monitoring", "Quan trắc địa kỹ thuật"),
    )

    for row in MATRIX:
        if row[0] == "group":
            body += '<tr class="rowh"><td colspan="3">%s</td></tr>' % pg.span(row[1], row[2])
        else:
            body += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                pg.span(row[0], ASPECT_VI.get(row[0], row[0])),
                pg.span(row[1], row[3]),
                pg.span(row[2], row[4]),
            )
    body += """
  </tbody>
</table>
</div>
""" % ()
    body += section_close()

    # why control needs controllability
    body += section_open("02", "Why the loop stays open", "Vì sao vòng để hở", pg, "why")
    body += """
<div class="g-2-1">
  <div>
    %s
    %s
    %s
    <div class="note">
      <span class="lbl">%s</span>
      %s
    </div>
  </div>
  <div class="card">
    <span class="n">%s</span>
    <h3>%s</h3>
    <div class="spec" style="margin-top:12px">
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
    </div>
  </div>
</div>
""" % (
        pg.h2("Four conditions for closing a loop", "Bốn điều kiện để khép kín một vòng"),
        pg.p(
            "Feedback control is only possible when four conditions hold at once. A geotechnical "
            "structure typically satisfies the first two and fails the third — and that failure is "
            "structural, not a matter of better instruments.",
            "Điều khiển phản hồi chỉ khả thi khi bốn điều kiện đồng thời thỏa mãn. Một kết cấu địa kỹ "
            "thuật thường thỏa hai điều kiện đầu và không thỏa điều kiện thứ ba — và sự thiếu hụt đó mang "
            "tính cấu trúc, không phải chuyện thiết bị tốt hơn.",
        ),
        pg.p(
            "The fourth condition is the one engineers forget. Feedback needs a response that is fast "
            "relative to how often you can act. If the ground takes three weeks to respond to a change in "
            "excavation rate, a controller correcting every second is not controlling anything — it is "
            "guessing, and it will be wrong for three weeks.",
            "Điều kiện thứ tư là điều kỹ sư hay quên. Phản hồi cần một đáp ứng đủ nhanh so với tần suất "
            "bạn có thể tác động. Nếu nền đất mất ba tuần mới đáp ứng với thay đổi tốc độ đào, một bộ "
            "điều khiển hiệu chỉnh mỗi giây không điều khiển được gì — nó đang đoán, và nó sẽ sai trong "
            "ba tuần.",
        ),
        pg.span("The useful exception", "Ngoại lệ hữu ích"),
        pg.p(
            "When the geotechnical variable is slow but the actuator is fast — a dewatering pump, a "
            "pressure relief gate, a pipeline block valve — the loop can genuinely close. Those are the "
            "hybrid cases in the next section.",
            "Khi biến địa kỹ thuật chậm nhưng cơ cấu chấp hành nhanh — bơm hạ mực nước, cửa xả áp, van "
            "chặn tuyến ống — vòng thực sự có thể khép kín. Đó là những trường hợp lai ở phần tiếp theo.",
        ),
        pg.span("Four tests", "Bốn phép thử"),
        pg.h3("Can this be controlled?", "Có điều khiển được không?"),
        pg.td("1. Observable", "1. Quan sát được"),
        pg.td("The variable can be measured fast enough to matter.", "Biến đo được đủ nhanh để có ý nghĩa."),
        pg.td("2. Controllable", "2. Điều khiển được"),
        pg.td("An input exists that changes the variable.", "Tồn tại đầu vào làm thay đổi biến đó."),
        pg.td("3. Authority", "3. Đủ thẩm quyền"),
        pg.td("The actuator can move the variable against the expected disturbance.", "Cơ cấu chấp hành đủ sức dịch chuyển biến trước nhiễu dự kiến."),
        pg.td("4. Stability", "4. Ổn định"),
        pg.td("The response is monotonic and fast relative to the correction interval.", "Đáp ứng đơn điệu và đủ nhanh so với chu kỳ hiệu chỉnh."),
    )
    body += section_close()

    # hybrid
    body += section_open("03", "Where the two meet", "Nơi hai ngành gặp nhau", pg, "hybrid")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="grid c3">
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
</div>
""" % (
        pg.h2("Six places where a monitoring signal becomes a control signal", "Sáu nơi tín hiệu quan trắc trở thành tín hiệu điều khiển"),
        pg.p(
            "Real projects rarely respect the boundary. In each of these, a geotechnical measurement "
            "drives a process action — sometimes automatically, sometimes through a procedure.",
            "Dự án thực tế hiếm khi tôn trọng ranh giới. Ở mỗi trường hợp dưới đây, một phép đo địa kỹ "
            "thuật dẫn đến một hành động quá trình — đôi khi tự động, đôi khi qua quy trình.",
        ),
        pg.h3("Dewatering control", "Điều khiển hạ mực nước"),
        pg.p(
            "Piezometers in the excavation read pore pressure; the pump speed follows it. This is a "
            "genuine closed loop with a geotechnical sensor and a process actuator — the clearest hybrid "
            "in practice.",
            "Đầu đo áp lực nước trong hố đào đọc áp lực lỗ rỗng; tốc độ bơm đi theo. Đây là vòng kín thực "
            "sự với cảm biến địa kỹ thuật và cơ cấu chấp hành quá trình — ví dụ lai rõ nhất trong thực tế.",
        ),
        pg.h3("Tailings storage facility", "Bãi quặng đuôi"),
        pg.p(
            "The decant system is process control; the phreatic surface and beach width are geotechnical "
            "monitoring. A rising phreatic line should change the operating setpoint — usually it changes "
            "a monthly report instead.",
            "Hệ tháo nước là điều khiển quá trình; mặt nước ngầm và chiều rộng bãi là quan trắc địa kỹ "
            "thuật. Một đường bão hòa dâng lên đáng lẽ phải đổi giá trị đặt vận hành — thường thì nó chỉ "
            "đổi một báo cáo tháng.",
        ),
        pg.h3("Dam and levee", "Đập và đê"),
        pg.p(
            "Seepage weirs and piezometers detect internal erosion; relief valves and gates control the "
            "water level. Instrumentation on both sides of the same structure, usually specified by "
            "different teams in different formats.",
            "Đập tràn đo thấm và đầu đo áp lực phát hiện xói ngầm; van xả và cửa van điều khiển mực nước. "
            "Thiết bị ở hai bên của cùng một kết cấu, thường do các nhóm khác nhau chỉ định theo định "
            "dạng khác nhau.",
        ),
        pg.h3("Pipeline geohazard", "Tai biến địa chất tuyến ống"),
        pg.p(
            "Slope movement or strain monitoring on a buried pipeline can trigger a block valve or a "
            "pressure reduction automatically. Slow loop, real actuator, real consequence.",
            "Quan trắc chuyển dịch mái dốc hoặc biến dạng trên tuyến ống chôn có thể tự động kích hoạt van "
            "chặn hoặc giảm áp. Vòng chậm, cơ cấu chấp hành thật, hậu quả thật.",
        ),
        pg.h3("Tunnel boring", "Đào hầm bằng TBM"),
        pg.p(
            "Face pressure and slurry density are controlled in seconds — pure process control. Surface "
            "settlement is measured in days — pure geotechnical monitoring. The two must be read "
            "together, and usually are not.",
            "Áp lực gương đào và tỷ trọng dung dịch được điều khiển trong vài giây — điều khiển quá trình "
            "thuần túy. Lún bề mặt được đo theo ngày — quan trắc địa kỹ thuật thuần túy. Hai thứ phải được "
            "đọc cùng nhau, và thường thì không.",
        ),
        pg.h3("Structural health monitoring", "Quan trắc sức khỏe kết cấu"),
        pg.p(
            "Strain, tilt and acceleration on a bridge or wind turbine. Continuous data, automated alarms "
            "— monitoring in form, but with the data rate of control. The missing piece is still the "
            "actuator.",
            "Biến dạng, nghiêng và gia tốc trên cầu hoặc tuabin gió. Dữ liệu liên tục, cảnh báo tự động "
            "— hình thức là quan trắc, nhưng tốc độ dữ liệu như điều khiển. Mảnh còn thiếu vẫn là cơ cấu "
            "chấp hành.",
        ),
    )
    body += section_close()

    # vocabulary traps
    body += section_open("04", "Vocabulary traps", "Bẫy thuật ngữ", pg, "vocab")
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
        pg.h2("Six words that mean different things", "Sáu từ mang nghĩa khác nhau"),
        pg.p(
            "Most coordination failures between the two disciplines are linguistic. The same word appears "
            "in both specifications with different definitions, and nobody notices until commissioning.",
            "Phần lớn lỗi phối hợp giữa hai ngành là do ngôn ngữ. Cùng một từ xuất hiện trong cả hai bản "
            "chỉ định với định nghĩa khác nhau, và không ai nhận ra cho đến khi chạy thử.",
        ),
        pg.th("Word", "Từ"),
        pg.th("In process I&amp;C it means", "Trong I&amp;C quá trình nghĩa là"),
        pg.th("In geotechnical monitoring it means", "Trong quan trắc địa kỹ thuật nghĩa là"),
    )
    for w, a, b, a_vi, b_vi in TRAPS:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>" % (
            pg.span(w, w),
            pg.span(a, a_vi),
            pg.span(b, b_vi),
        )
    body += """
  </tbody>
</table>
</div>
""" % ()
    body += section_close()

    # practical
    body += section_open("05", "What this means in practice", "Ý nghĩa thực tiễn", pg, "practice")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="grid c2">
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
  <div class="card"><h3>%s</h3><p>%s</p></div>
</div>
<div class="note warn mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Six rules that follow from the matrix", "Sáu quy tắc rút ra từ bảng so sánh"),
        pg.p(
            "These are the mistakes that appear when the two disciplines are mixed without noticing the "
            "difference.",
            "Đây là những lỗi xuất hiện khi hai ngành bị trộn lẫn mà không nhận ra khác biệt.",
        ),
        pg.h3("Do not put a process transmitter in a borehole", "Đừng đặt bộ truyền quá trình trong lỗ khoan"),
        pg.p(
            "A DP transmitter needs a clean impulse line and occasional access. Grouted into a borehole it "
            "will drift, then fail, and you will not be able to remove it.",
            "Bộ truyền áp vi sai cần ống xung sạch và thỉnh thoảng tiếp cận được. Chèn vữa vào lỗ khoan, "
            "nó sẽ trôi, rồi hỏng, và bạn không thể tháo ra.",
        ),
        pg.h3("Do not put a vibrating-wire sensor in a fast loop", "Đừng đặt cảm biến dây rung trong vòng nhanh"),
        pg.p(
            "VW sensors are stable, not fast. Their reading interval is seconds to minutes; a control loop "
            "that needs 100 ms cannot use one.",
            "Cảm biến dây rung ổn định, nhưng không nhanh. Chu kỳ đọc là giây đến phút; vòng điều khiển "
            "cần 100 ms không dùng được.",
        ),
        pg.h3("Specify stability, not just accuracy", "Chỉ định độ ổn định, không chỉ độ chính xác"),
        pg.p(
            "In a buried sensor, drift over five years matters more than a tenth of a percent on day one. "
            "Ask for the long-term stability figure and the temperature coefficient.",
            "Với cảm biến bị chôn, độ trôi trong năm năm quan trọng hơn một phần mười phần trăm ở ngày "
            "đầu. Hãy yêu cầu con số ổn định dài hạn và hệ số nhiệt độ.",
        ),
        pg.h3("Assume some sensors will be lost", "Giả định một số cảm biến sẽ mất"),
        pg.p(
            "Install spares in the same borehole, or a second method that measures the same quantity "
            "differently. Redundancy in monitoring means independence, not duplication.",
            "Lắp dự phòng trong cùng lỗ khoan, hoặc dùng phương pháp thứ hai đo cùng đại lượng theo cách "
            "khác. Dự phòng trong quan trắc nghĩa là độc lập, không phải trùng lặp.",
        ),
        pg.h3("Cable is the weakest link", "Cáp là mắt xấu nhất"),
        pg.p(
            "Lightning, rodents, excavation and UV destroy more geotechnical data than sensor failure. "
            "Budget for surge protection and route discipline, not just instruments.",
            "Sét, gặm nhấm, đào bới và tia UV phá hủy dữ liệu địa kỹ thuật nhiều hơn là hỏng cảm biến. "
            "Hãy dự trù kinh phí cho chống sét lan truyền và kỷ luật tuyến cáp, không chỉ cho thiết bị.",
        ),
        pg.h3("Write the trigger-action plan first", "Viết kế hoạch ngưỡng–hành động trước"),
        pg.p(
            "A threshold without an action is decoration. Decide who does what, at which value, within "
            "which time — before the first sensor is installed.",
            "Một ngưỡng không kèm hành động chỉ là trang trí. Hãy quyết định ai làm gì, ở giá trị nào, "
            "trong bao lâu — trước khi lắp cảm biến đầu tiên.",
        ),
        pg.span("The expensive mistake", "Sai lầm tốn kém"),
        pg.p(
            "Specifying control-grade hardware for a monitoring job, or monitoring-grade hardware for a "
            "control job, produces a system that works on paper and fails in service. The first is "
            "wasteful; the second is dangerous.",
            "Chỉ định thiết bị cấp điều khiển cho một bài toán quan trắc, hoặc thiết bị cấp quan trắc cho "
            "một bài toán điều khiển, tạo ra hệ thống đúng trên giấy và hỏng khi vận hành. Trường hợp đầu "
            "lãng phí; trường hợp sau nguy hiểm.",
        ),
    )
    body += section_close()

    write("comparison.html", render(pg, body, "comparison.html"))
