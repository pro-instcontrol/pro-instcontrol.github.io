# -*- coding: utf-8 -*-
"""Home page."""

from framework import Page, section_open, section_close, write, render

HERO_SVG = """
<svg viewBox="0 60 620 300" role="img" aria-label="Closed control loop: flow transmitter FT-101, controller FIC-101, control valve FV-101">
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#0d7a6f"/>
    </marker>
    <marker id="ahk" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#0b1725"/>
    </marker>
  </defs>

  <!-- process line -->
  <line x1="48" y1="300" x2="572" y2="300" stroke="#0b1725" stroke-width="2.2"/>
  <polygon points="252,300 236,293 236,307" fill="#0b1725"/>

  <!-- orifice / flow element -->
  <line x1="164" y1="288" x2="164" y2="312" stroke="#0b1725" stroke-width="2"/>
  <line x1="176" y1="288" x2="176" y2="312" stroke="#0b1725" stroke-width="2"/>
  <line x1="170" y1="285" x2="170" y2="315" stroke="#0b1725" stroke-width="3.4"/>

  <!-- control valve -->
  <polygon points="420,286 420,314 440,300" fill="#ffffff" stroke="#0b1725" stroke-width="2" stroke-linejoin="round"/>
  <polygon points="440,286 440,314 420,300" fill="#ffffff" stroke="#0b1725" stroke-width="2" stroke-linejoin="round"/>
  <line x1="430" y1="286" x2="430" y2="252" stroke="#0b1725" stroke-width="2"/>
  <path d="M412 252 A18 16 0 0 1 448 252 Z" fill="#ffffff" stroke="#0b1725" stroke-width="2" stroke-linejoin="round"/>

  <!-- impulse line -->
  <line x1="170" y1="300" x2="170" y2="192" stroke="#0b1725" stroke-width="1.6"/>

  <!-- transmitter bubble -->
  <circle cx="170" cy="160" r="32" fill="#ffffff" stroke="#0b1725" stroke-width="2"/>
  <text x="170" y="157" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="17" font-weight="600" fill="#0b1725">FT</text>
  <text x="170" y="173" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="14.5" fill="#22364a">101</text>

  <!-- signal to controller -->
  <line x1="200" y1="160" x2="246" y2="160" stroke="#0d7a6f" stroke-width="1.8" marker-end="url(#ah)"/>

  <!-- controller -->
  <circle cx="282" cy="160" r="36" fill="#ffffff" stroke="#0b1725" stroke-width="2"/>
  <line x1="252" y1="140" x2="312" y2="140" stroke="#0b1725" stroke-width="1.2"/>
  <text x="282" y="162" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="17" font-weight="600" fill="#0b1725">FIC</text>
  <text x="282" y="178" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="14.5" fill="#22364a">101</text>

  <!-- setpoint -->
  <line x1="282" y1="100" x2="282" y2="122" stroke="#a85a06" stroke-width="1.8" marker-end="url(#ah)"/>
  <text x="292" y="97" font-family="'IBM Plex Mono',monospace" font-size="13" fill="#a85a06">SP</text>

  <!-- controller to final element -->
  <path d="M316 160 H430 V236" fill="none" stroke="#0d7a6f" stroke-width="1.8" marker-end="url(#ah)"/>

  <!-- labels -->
  <text x="170" y="336" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="13" fill="#66788d">FE 101</text>
  <text x="430" y="336" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="13" fill="#66788d">FV 101</text>
  <text x="282" y="214" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="12.5" fill="#66788d">controller</text>
  <text x="60" y="288" font-family="'IBM Plex Mono',monospace" font-size="12.5" fill="#66788d">PV</text>
  <text x="474" y="200" font-family="'IBM Plex Mono',monospace" font-size="12.5" fill="#66788d">final element</text>
</svg>
"""


def attr_i18n(pg, en, vi, attr="title"):
    """Register a string for an attribute rather than for element text.

    The iframe title is the only label a screen reader gets for the embedded
    document, so it has to follow the language like every other string; app.js
    writes it through data-i18n-attr instead of replacing innerHTML.
    """
    k = pg.key()
    pg.strings[k] = {"en": en, "vi": vi}
    return 'data-i18n="%s" data-i18n-attr="%s"' % (k, attr)


def reader_block(pg):
    """The two source documents behind the next section, read in place.

    comparison.html and geotechnical.html argue the two sides of the dividing
    line. Embedding them here keeps the reader on the page while they check the
    claim, and gives both pages the inbound link they lost when they came out
    of the reading chain. ?embed=1 strips the site chrome inside the frame;
    data-embed lets app.js rebuild the src in the reader's language.
    """
    return """
<section class="sec alt" id="read-inline">
  <div class="wrap">
    <div class="sec-head">
      %s
      %s
    </div>
    <div class="reader">
      <input type="radio" name="reader-pick" id="r-cmp" checked>
      <input type="radio" name="reader-pick" id="r-geo">
      <div class="reader-tabs">
        <label for="r-cmp">%s</label>
        <label for="r-geo">%s</label>
      </div>
      <div class="pane p-cmp">
        <div class="pane-bar">
          %s
          %s
        </div>
        <iframe src="comparison.html?embed=1" data-embed="comparison.html" loading="lazy"
                title="Process control vs geotechnical monitoring" %s></iframe>
      </div>
      <div class="pane p-geo">
        <div class="pane-bar">
          %s
          %s
        </div>
        <iframe src="geotechnical.html?embed=1" data-embed="geotechnical.html" loading="lazy"
                title="Geotechnical monitoring" %s></iframe>
      </div>
    </div>
  </div>
</section>
""" % (
        pg.h2("Read the two documents here", "Đọc trực tiếp hai tài liệu"),
        pg.p(
            "The next section draws the line between the two disciplines. Both source pages are "
            "open below, in this page — scroll inside the frame, or open the full page if you want "
            "the navigation around it.",
            "Phần tiếp theo vạch ranh giới giữa hai ngành. Cả hai trang gốc được mở ngay bên dưới, "
            "trong chính trang này — cuộn trong khung, hoặc mở trang đầy đủ nếu muốn có menu "
            "điều hướng.",
        ),
        pg.span("Comparison", "So sánh"),
        pg.span("Geotechnical", "Địa kỹ thuật"),
        pg.span(
            "Process control vs geotechnical monitoring — the full comparison",
            "Điều khiển quá trình vs quan trắc địa kỹ thuật — bản đầy đủ",
            "pane-t",
        ),
        pg.a("comparison.html", "Open full page &nearr;", "Mở trang đầy đủ &nearr;", "pane-open"),
        attr_i18n(
            pg,
            "Process control vs geotechnical monitoring — the full comparison",
            "Điều khiển quá trình vs quan trắc địa kỹ thuật — bản đầy đủ",
        ),
        pg.span(
            "Geotechnical monitoring — instruments, ISO 18674, field reality",
            "Quan trắc địa kỹ thuật — thiết bị, ISO 18674, thực tế hiện trường",
            "pane-t",
        ),
        pg.a("geotechnical.html", "Open full page &nearr;", "Mở trang đầy đủ &nearr;", "pane-open"),
        attr_i18n(
            pg,
            "Geotechnical monitoring — instruments, ISO 18674, field reality",
            "Quan trắc địa kỹ thuật — thiết bị, ISO 18674, thực tế hiện trường",
        ),
    )


def build():
    pg = Page(
        "index.html",
        "idx",
        "Process Instrumentation &amp; Control — a bilingual field guide",
        "Đo lường &amp; Điều khiển Quá trình — sổ tay song ngữ",
        "A bilingual English/Vietnamese field guide to process instrumentation and control: "
        "measurement principles, instrument selection, PID tuning, and how process control "
        "differs from geotechnical monitoring.",
        "Sổ tay song ngữ Anh/Việt về thiết bị đo và điều khiển quá trình: nguyên lý đo, "
        "chọn thiết bị, hiệu chỉnh PID, và khác biệt với quan trắc địa kỹ thuật.",
    )

    hero = """
<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-copy">
      <span class="kicker"><span class="dot"></span>%s</span>
      %s
      %s
      <div class="hero-cta">
        <a class="btn btn-p" href="fundamentals.html">%s <span class="arw">&rarr;</span></a>
      </div>
    </div>
    <div class="figure">
      %s
      <div class="figcap">%s</div>
    </div>
  </div>
</section>
""" % (
        pg.span("Process · Control · Monitoring", "Quá trình · Điều khiển · Quan trắc", "kicker-txt"),
        pg.el(
            "h1",
            "Measure the process.<span class=\"thin\">Then close the loop.</span>",
            "Đo lường quá trình.<span class=\"thin\">Rồi khép kín vòng điều khiển.</span>",
        ),
        pg.p(
            "A working field guide to the instruments that sense pressure, temperature, flow, "
            "level and composition — and to the loops that decide what to do about the reading. "
            "Written for the engineer who specifies, installs and tunes, in English and Vietnamese.",
            "Sổ tay thực hành về các thiết bị đo áp suất, nhiệt độ, lưu lượng, mức và thành phần — "
            "cùng những vòng điều khiển quyết định phải làm gì với kết quả đo. Dành cho kỹ sư "
            "khảo sát, lắp đặt và hiệu chỉnh, bằng tiếng Anh và tiếng Việt.",
            "lede",
        ),
        pg.span("Start with the fundamentals", "Bắt đầu từ kiến thức cơ bản"),
        HERO_SVG,
        pg.span(
            "One loop, three jobs: sense (FT-101), decide (FIC-101), act (FV-101) — over a 4–20 mA signal.",
            "Một vòng, ba nhiệm vụ: cảm nhận (FT-101), quyết định (FIC-101), tác động (FV-101) — qua tín hiệu 4–20 mA.",
        ),
    )

    stats = """
<div class="wrap" style="padding-top:0;padding-bottom:0">
<div class="stats">
  <div class="stat"><b>4–20 mA</b>%s</div>
  <div class="stat"><b>P · T · F · L · A</b>%s</div>
  <div class="stat"><b>P / I / D</b>%s</div>
  <div class="stat"><b>ISO 18674</b>%s</div>
</div>
</div>
""" % (
        pg.span("live-zero analogue signal", "tín hiệu tương tự có điểm không sống"),
        pg.span("five measurement families", "năm họ phép đo"),
        pg.span("three terms, one loop", "ba số hạng, một vòng điều khiển"),
        pg.span("the geotechnical counterpart", "đối tượng địa kỹ thuật tương ứng"),
    )

    body = hero + stats

    # ---- 01 what it is
    body += section_open("01", "The discipline", "Ngành kỹ thuật", pg, "what")
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
  <div>
    <div class="card">
      %s
      <h3>%s</h3>
      %s
    </div>
  </div>
</div>
""" % (
        pg.h2("Instrumentation is a loop, not a list", "Thiết bị đo là một vòng, không phải một danh mục"),
        pg.p(
            "Process instrumentation and control (I&amp;C) is the engineering of <strong>measurement plus "
            "action</strong>. A transmitter on its own is only half a discipline: the value it produces "
            "has to travel to a controller, be compared with a target, and drive a final element that "
            "changes the process. Take away any one of those three links and you no longer have control — "
            "you have a reading.",
            "Đo lường và điều khiển quá trình (I&amp;C) là kỹ thuật của <strong>đo lường cộng với "
            "tác động</strong>. Một bộ truyền tín hiệu đứng riêng chỉ là một nửa của ngành: giá trị đo "
            "phải đi đến bộ điều khiển, được so sánh với giá trị đích, rồi điều khiển một phần tử chấp "
            "hành làm thay đổi quá trình. Thiếu một trong ba mắt xích đó, bạn không còn điều khiển — "
            "bạn chỉ còn một con số.",
        ),
        pg.p(
            "That is why the same word, <em>instrument</em>, means something quite different in "
            "geotechnical engineering, where the loop is deliberately left open and a human being "
            "occupies the place of the controller. The comparison section takes that difference apart "
            "properly; here it is enough to notice that control requires something to control.",
            "Đó là lý do cùng một từ, <em>thiết bị đo</em>, lại mang nghĩa khác trong địa kỹ thuật, nơi "
            "vòng điều khiển được cố ý để hở và con người giữ vị trí của bộ điều khiển. Phần so sánh sẽ "
            "mổ xẻ khác biệt này; ở đây chỉ cần lưu ý: muốn điều khiển thì phải có thứ gì đó để điều khiển.",
        ),
        pg.span("Rule of thumb", "Quy tắc thực hành"),
        pg.p(
            "If you cannot name the manipulated variable, you are designing a monitoring system — "
            "however many transmitters it contains.",
            "Nếu bạn không gọi được tên của biến điều khiển, bạn đang thiết kế một hệ quan trắc — "
            "dù nó có bao nhiêu bộ truyền tín hiệu đi nữa.",
        ),
        pg.span("Level 0 → 4", "Mức 0 → 4"),
        pg.h3("Where the work sits", "Công việc nằm ở đâu"),
        pg.p(
            "Most I&amp;C scope lives between the process connection and the operator screen — "
            "ISA-95 levels 0 to 3.",
            "Phần lớn phạm vi I&amp;C nằm giữa điểm đấu nối quá trình và màn hình vận hành — "
            "các mức 0 đến 3 của ISA-95.",
        ),
    )
    body += section_close()

    # ---- 02 five families
    body += section_open("02", "Measurement families", "Các họ phép đo", pg, "families")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="grid c3">
  <a class="card" href="instruments.html#pressure">
    <span class="n">P</span>
    <h3>%s</h3>
    <p>%s</p>
    <span class="more">%s &rarr;</span>
  </a>
  <a class="card" href="instruments.html#temperature">
    <span class="n">T</span>
    <h3>%s</h3>
    <p>%s</p>
    <span class="more">%s &rarr;</span>
  </a>
  <a class="card" href="instruments.html#flow">
    <span class="n">F</span>
    <h3>%s</h3>
    <p>%s</p>
    <span class="more">%s &rarr;</span>
  </a>
  <a class="card" href="instruments.html#level">
    <span class="n">L</span>
    <h3>%s</h3>
    <p>%s</p>
    <span class="more">%s &rarr;</span>
  </a>
  <a class="card" href="instruments.html#analytical">
    <span class="n">A</span>
    <h3>%s</h3>
    <p>%s</p>
    <span class="more">%s &rarr;</span>
  </a>
  <a class="card" href="instruments.html#final">
    <span class="n">&#9654;</span>
    <h3>%s</h3>
    <p>%s</p>
    <span class="more">%s &rarr;</span>
  </a>
</div>
""" % (
        pg.h2("Five ways to describe a process", "Năm cách mô tả một quá trình"),
        pg.p(
            "Almost every process variable an operator cares about falls into one of five families. "
            "Each has a dominant technology, a characteristic failure mode, and a set of installation "
            "rules that decide whether the number on the screen is true.",
            "Gần như mọi biến quá trình mà người vận hành quan tâm đều thuộc một trong năm họ. Mỗi họ "
            "có một công nghệ chủ đạo, một kiểu hư hỏng đặc trưng, và những quy tắc lắp đặt quyết định "
            "con số trên màn hình có đúng hay không.",
        ),
        pg.span("Pressure", "Áp suất"),
        pg.span(
            "Gauge, absolute and differential. The foundation of flow, level and density measurement.",
            "Áp kế, áp suất tuyệt đối và áp suất vi sai. Nền tảng của đo lưu lượng, mức và khối lượng riêng.",
        ),
        pg.span("Explore pressure", "Xem về áp suất"),
        pg.span("Temperature", "Nhiệt độ"),
        pg.span(
            "RTDs for accuracy, thermocouples for range and speed. The most common loop in any plant.",
            "RTD cho độ chính xác, cặp nhiệt điện cho dải rộng và tốc độ. Vòng đo phổ biến nhất trong nhà máy.",
        ),
        pg.span("Explore temperature", "Xem về nhiệt độ"),
        pg.span("Flow", "Lưu lượng"),
        pg.span(
            "The hardest variable to measure well. Orifice, magnetic, Coriolis, vortex, ultrasonic.",
            "Biến khó đo chính xác nhất. Lỗ khoan, điện từ, Coriolis, xoáy, siêu âm.",
        ),
        pg.span("Explore flow", "Xem về lưu lượng"),
        pg.span("Level", "Mức"),
        pg.span(
            "Hydrostatic, radar, guided wave, capacitance. Interface detection is the hard part.",
            "Thủy tĩnh, radar, sóng dẫn, điện dung. Phần khó nhất là phát hiện mặt phân cách.",
        ),
        pg.span("Explore level", "Xem về mức"),
        pg.span("Analytical", "Phân tích"),
        pg.span(
            "pH, conductivity, oxygen, moisture and gas composition — where quality is measured directly.",
            "pH, độ dẫn, oxy, độ ẩm và thành phần khí — nơi chất lượng được đo trực tiếp.",
        ),
        pg.span("Explore analytical", "Xem về phân tích"),
        pg.span("Final elements", "Phần tử chấp hành"),
        pg.span(
            "Control valves, actuators, positioners and variable-speed drives — the muscles of the loop.",
            "Van điều khiển, cơ cấu chấp hành, bộ định vị và biến tần — phần cơ bắp của vòng điều khiển.",
        ),
        pg.span("Explore final elements", "Xem về phần tử chấp hành"),
    )
    body += section_close()

    # ---- the two source documents, read in place
    body += reader_block(pg)

    # ---- 03 the line
    body += section_open("03", "The dividing line", "Ranh giới phân chia", pg, "line")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="versus">
  <div class="a">
    <span class="tagline">%s</span>
    <h3>%s</h3>
    <ul>
      %s
      %s
      %s
      %s
    </ul>
  </div>
  <div class="b">
    <span class="tagline">%s</span>
    <h3>%s</h3>
    <ul>
      %s
      %s
      %s
      %s
    </ul>
  </div>
</div>
<div class="mt24">
  %s
</div>
""" % (
        pg.h2("Small and controllable, or large and watchful", "Nhỏ và điều khiển được, hay lớn và cần quan sát"),
        pg.p(
            "Both disciplines hang instruments on a structure and read numbers. The difference is what "
            "happens next — and it is not a matter of taste, it follows from the physics of the system "
            "being measured.",
            "Cả hai ngành đều gắn thiết bị lên một kết cấu và đọc số. Khác biệt nằm ở bước tiếp theo — "
            "và đó không phải chuyện sở thích, mà xuất phát từ bản chất vật lý của hệ được đo.",
        ),
        pg.span("Closed loop · acts", "Vòng kín · tác động"),
        pg.span("Process instrumentation &amp; control", "Đo lường &amp; điều khiển quá trình"),
        pg.li(
            "<strong>Bounded system.</strong> A pipe, a vessel, a heat exchanger — geometry and "
            "boundary conditions are known and drawn.",
            "<strong>Hệ có biên xác định.</strong> Một đường ống, một bình chứa, một thiết bị trao đổi "
            "nhiệt — hình học và điều kiện biên đã biết và được vẽ ra.",
        ),
        pg.li(
            "<strong>Fast.</strong> Time constants from seconds to minutes; a loop can be tuned in an afternoon.",
            "<strong>Nhanh.</strong> Hằng số thời gian từ giây đến phút; một vòng có thể hiệu chỉnh trong một buổi.",
        ),
        pg.li(
            "<strong>An actuator exists.</strong> A valve, a damper, a drive — something that can be moved "
            "to change the variable.",
            "<strong>Có cơ cấu chấp hành.</strong> Một van, một cánh gió, một biến tần — thứ có thể dịch "
            "chuyển để thay đổi biến quá trình.",
        ),
        pg.li(
            "<strong>Goal: hold.</strong> Keep PV at SP despite disturbance, within a stated band.",
            "<strong>Mục tiêu: giữ.</strong> Giữ PV ở SP bất chấp nhiễu động, trong một dải cho phép.",
        ),
        pg.span("Open loop · observes", "Vòng hở · quan sát"),
        pg.span("Geotechnical monitoring", "Quan trắc địa kỹ thuật"),
        pg.li(
            "<strong>Natural system.</strong> A slope, a dam foundation, a tunnel — geometry inferred from "
            "a handful of boreholes.",
            "<strong>Hệ tự nhiên.</strong> Một mái dốc, nền đập, đường hầm — hình học suy ra từ vài lỗ khoan.",
        ),
        pg.li(
            "<strong>Slow.</strong> Time constants from days to years; the monitoring campaign outlives "
            "the project team.",
            "<strong>Chậm.</strong> Hằng số thời gian từ ngày đến năm; chiến dịch quan trắc sống lâu hơn đội dự án.",
        ),
        pg.li(
            "<strong>No actuator.</strong> You cannot throttle a hillside. There is nothing to move, so "
            "there is nothing to tune.",
            "<strong>Không có cơ cấu chấp hành.</strong> Không thể &ldquo;van hóa&rdquo; một mái dốc. "
            "Không có gì để dịch chuyển thì cũng không có gì để hiệu chỉnh.",
        ),
        pg.li(
            "<strong>Goal: know.</strong> Detect change early, compare with a threshold, trigger a decision.",
            "<strong>Mục tiêu: biết.</strong> Phát hiện thay đổi sớm, so với ngưỡng, kích hoạt một quyết định.",
        ),
        pg.p(
            "The rest of this guide treats the first column as its main subject and keeps the second "
            "column in view, because most real projects — dams, tailings facilities, tunnels, pipelines "
            "through unstable ground — need both at once, and the two are usually specified by people "
            "who do not share a vocabulary.",
            "Phần còn lại của sổ tay lấy cột thứ nhất làm chủ đề chính và vẫn theo dõi cột thứ hai, vì "
            "hầu hết dự án thực tế — đập, bãi quặng đuôi, đường hầm, tuyến ống qua vùng đất yếu — cần "
            "cả hai cùng lúc, và hai bên thường do những người không dùng chung từ vựng chỉ định.",
            "small dim",
        ),
    )
    body += section_close()

    # ---- 04 how to use
    body += section_open("04", "How to use this guide", "Cách dùng sổ tay", pg, "how")
    body += """
<div class="grid c4">
  <div class="card">
    <span class="n">01</span>
    <h3>%s</h3>
    <p>%s</p>
    <a class="more" href="fundamentals.html">%s &rarr;</a>
  </div>
  <div class="card">
    <span class="n">02</span>
    <h3>%s</h3>
    <p>%s</p>
    <a class="more" href="instruments.html">%s &rarr;</a>
  </div>
  <div class="card">
    <span class="n">03</span>
    <h3>%s</h3>
    <p>%s</p>
    <a class="more" href="control.html">%s &rarr;</a>
  </div>
  <div class="card">
    <span class="n">04</span>
    <h3>%s</h3>
    <p>%s</p>
    <a class="more" href="safety.html">%s &rarr;</a>
  </div>
</div>
""" % (
        pg.h3("Learn the signal chain", "Hiểu chuỗi tín hiệu"),
        pg.p(
            "Start with how a physical quantity becomes a number on a screen, and where accuracy is lost "
            "on the way.",
            "Bắt đầu từ việc một đại lượng vật lý trở thành con số trên màn hình, và độ chính xác bị mất ở đâu trên đường đi.",
        ),
        pg.span("Fundamentals", "Kiến thức cơ bản"),
        pg.h3("Choose the instrument", "Chọn thiết bị"),
        pg.p(
            "Use the filterable reference to compare principle, accuracy and failure mode for each family.",
            "Dùng bảng tra có bộ lọc để so sánh nguyên lý, độ chính xác và kiểu hư hỏng của từng họ.",
        ),
        pg.span("Instrument reference", "Danh mục thiết bị"),
        pg.h3("Close the loop", "Khép kín vòng điều khiển"),
        pg.p(
            "Tune a simulated loop, then read how PID terms interact with dead time and process lag.",
            "Hiệu chỉnh một vòng mô phỏng, rồi đọc cách các số hạng PID tương tác với thời gian trễ và quán tính.",
        ),
        pg.span("Control &amp; tuning", "Điều khiển &amp; hiệu chỉnh"),
        pg.h3("Prove it fails safe", "Chứng minh nó hỏng an toàn"),
        pg.p(
            "Then read how a safety function is specified, verified and quietly defeated — and why a "
            "SIL belongs to a loop, not to a device.",
            "Rồi đọc cách một chức năng an toàn được đặc tả, kiểm chứng và bị vô hiệu hóa âm thầm — và "
            "vì sao SIL thuộc về một vòng đo, không phải một thiết bị.",
        ),
        pg.span("Safety systems", "Hệ thống an toàn"),
    )
    body += section_close()

    write("index.html", render(pg, body, "index.html"))
