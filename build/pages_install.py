# -*- coding: utf-8 -*-
"""Installation, hazardous area and commissioning."""

from framework import Page, section_open, section_close, write, render, page_intro

TAP_SVG = """
<svg viewBox="0 0 680 272" role="img" aria-label="Correct tapping point and impulse line slope for gas service and for liquid service">
  <defs>
    <marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#0b1725"/>
    </marker>
  </defs>

  <!-- ============ GAS ============ -->
  <text x="24" y="24" font-family="'IBM Plex Mono',monospace" font-size="9.5" letter-spacing="1.4" fill="#0a5f56">GAS &#183; TAP AT THE TOP</text>

  <rect x="24" y="120" width="276" height="16" fill="#eef3f8" stroke="#0b1725" stroke-width="1.2"/>
  <line x1="60" y1="128" x2="120" y2="128" stroke="#0b1725" stroke-width="1.3" marker-end="url(#fl)"/>

  <path d="M110 120 L160 74" fill="none" stroke="#0d7a6f" stroke-width="1.8"/>
  <circle cx="110" cy="120" r="3" fill="#0d7a6f"/>
  <circle cx="172" cy="66" r="16" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <text x="172" y="70" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9.5" font-weight="600" fill="#0b1725">PT</text>

  <text x="24" y="200" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#66788d">transmitter above the pipe</text>
  <text x="24" y="214" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#0a5f56">condensate drains back down</text>

  <line x1="328" y1="40" x2="328" y2="230" stroke="#ccd7e3" stroke-width="1" stroke-dasharray="3 5"/>

  <!-- ============ LIQUID ============ -->
  <text x="356" y="24" font-family="'IBM Plex Mono',monospace" font-size="9.5" letter-spacing="1.4" fill="#0a5f56">LIQUID &#183; TAP AT THE SIDE</text>

  <rect x="356" y="120" width="276" height="16" fill="#eef3f8" stroke="#0b1725" stroke-width="1.2"/>
  <line x1="392" y1="128" x2="452" y2="128" stroke="#0b1725" stroke-width="1.3" marker-end="url(#fl)"/>

  <path d="M430 136 L480 182" fill="none" stroke="#0d7a6f" stroke-width="1.8"/>
  <circle cx="430" cy="136" r="3" fill="#0d7a6f"/>
  <circle cx="492" cy="194" r="16" fill="#fff" stroke="#0b1725" stroke-width="1.7"/>
  <text x="492" y="198" text-anchor="middle" font-family="'IBM Plex Mono',monospace" font-size="9.5" font-weight="600" fill="#0b1725">PT</text>

  <text x="356" y="244" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#66788d">transmitter below the pipe</text>
  <text x="356" y="258" font-family="'IBM Plex Mono',monospace" font-size="8.5" fill="#0a5f56">gas bubbles rise back up</text>
</svg>
"""

TAPS = [
    ("Gas and air", "Top of the pipe, never the bottom.",
     "Downward to the transmitter, so condensate runs back.",
     "A liquid slug sitting on the diaphragm.",
     "Khí và không khí", "Đỉnh ống, không bao giờ đáy ống.",
     "Dốc xuống về phía bộ truyền, để nước ngưng chảy ngược.",
     "Một khối chất lỏng đọng trên màng."),
    ("Liquid", "Side of the pipe, not the bottom where solids settle.",
     "Upward to the transmitter, so gas vents back.",
     "A gas pocket that never fills.",
     "Chất lỏng", "Thành ống, không phải đáy nơi cặn lắng.",
     "Dốc lên về phía bộ truyền, để khí thoát ngược.",
     "Một túi khí không bao giờ đầy."),
    ("Steam", "Side of the pipe, into a pigtail siphon.",
     "Horizontal run, then down to the transmitter.",
     "Live steam on the diaphragm — the siphon exists to keep condensate there.",
     "Hơi nước", "Thành ống, vào ống xoắn xi-phông.",
     "Đoạn ngang, rồi xuống bộ truyền.",
     "Hơi sống tác động lên màng — ống xi-phông tồn tại để giữ nước ngưng ở đó."),
    ("Slurry and dirty service", "Side, with a diaphragm seal or a continuous purge.",
     "Upward to the transmitter, with a flush connection.",
     "Solids settling in a dead leg and setting like concrete.",
     "Bùn và môi chất bẩn", "Thành ống, với màng niêm hoặc sục rửa liên tục.",
     "Dốc lên về phía bộ truyền, có điểm xả rửa.",
     "Cặn lắng trong nhánh chết rồi đông cứng như bê tông."),
    ("Vacuum", "Top of the pipe.",
     "Downward, with a short run.",
     "Air drawn in through a leaking fitting — the loop then reads a mixture.",
     "Chân không", "Đỉnh ống.",
     "Dốc xuống, đoạn ngắn.",
     "Không khí bị hút vào qua mối nối rò — vòng đo đọc hỗn hợp."),
]

AREA = [
    ("Zone 0", "An explosive atmosphere is present continuously, or for more than 1 000 hours a year.",
     "Zone 0", "Khí cháy hiện diện liên tục, hoặc hơn 1 000 giờ mỗi năm."),
    ("Zone 1", "Likely to occur in normal operation — roughly 10 to 1 000 hours a year.",
     "Zone 1", "Có khả năng xuất hiện trong vận hành bình thường — khoảng 10 đến 1 000 giờ mỗi năm."),
    ("Zone 2", "Unlikely, and only for short periods — under 10 hours a year.",
     "Zone 2", "Khó xảy ra, và chỉ trong thời gian ngắn — dưới 10 giờ mỗi năm."),
    ("Group IIA", "Propane. The least easily ignited of the surface gas groups.",
     "Nhóm IIA", "Propan. Nhóm khí bề mặt khó bắt cháy nhất."),
    ("Group IIB", "Ethylene. The middle group, and where most refinery hydrogen-free service sits.",
     "Nhóm IIB", "Etylen. Nhóm trung gian, nơi phần lớn dịch vụ lọc dầu không có hydro nằm."),
    ("Group IIC", "Hydrogen and acetylene. The most easily ignited — and the group that shrinks the allowable cable length.",
     "Nhóm IIC", "Hydro và axetylen. Dễ bắt cháy nhất — và là nhóm làm giảm chiều dài cáp cho phép."),
    ("T1 to T6", "Maximum surface temperature: 450, 300, 200, 135, 100 and 85 &deg;C.",
     "T1 đến T6", "Nhiệt độ bề mặt tối đa: 450, 300, 200, 135, 100 và 85 &deg;C."),
    ("Ex ia", "Intrinsically safe, remains safe with two faults. The only concept that permits Zone 0.",
     "Ex ia", "An toàn tia lửa, vẫn an toàn với hai hư hỏng. Khái niệm duy nhất cho phép Vùng 0."),
    ("Ex ib", "Intrinsically safe with one fault. Permits Zone 1.",
     "Ex ib", "An toàn tia lửa với một hư hỏng. Cho phép Vùng 1."),
    ("Ex d", "Flameproof enclosure — it lets the explosion happen inside and does not let it out.",
     "Ex d", "Vỏ chống cháy nổ — cho phép nổ bên trong và không để nó thoát ra."),
    ("Ex e", "Increased safety — no sparks or hot surfaces in normal operation.",
     "Ex e", "An toàn tăng cường — không có tia lửa hay bề mặt nóng trong vận hành bình thường."),
    ("Ex n", "Non-sparking, for Zone 2 only.",
     "Ex n", "Không phát tia lửa, chỉ cho Vùng 2."),
]

COMMISSION = [
    ("Loop check", "The right sensor reaches the right point in the system.",
     "Inject at the sensor, read at the operator screen, and confirm the tag — not just the value.",
     "Kiểm tra vòng", "Cảm biến đúng đi đến đúng điểm trong hệ thống.",
     "Bơm tín hiệu tại cảm biến, đọc trên màn hình vận hành, và xác nhận đúng tag — không chỉ đúng giá trị."),
    ("Five-point calibration", "Linearity and hysteresis, up and down.",
     "0, 25, 50, 75 and 100 per cent, ascending then descending. A one-direction check hides hysteresis entirely.",
     "Hiệu chuẩn năm điểm", "Tính tuyến tính và độ trễ, cả chiều lên và xuống.",
     "0, 25, 50, 75 và 100 phần trăm, tăng rồi giảm. Kiểm tra một chiều che giấu hoàn toàn độ trễ."),
    ("As-found and as-left", "Whether the device drifted, and by how much.",
     "Record before you adjust. Without an as-found record there is no trend, and no argument with the vendor.",
     "Trước và sau hiệu chỉnh", "Thiết bị có trôi không, và trôi bao nhiêu.",
     "Ghi lại trước khi điều chỉnh. Không có số liệu trước hiệu chỉnh thì không có xu hướng, và không có căn cứ tranh luận với nhà sản xuất."),
    ("Zero at line pressure", "For DP level: the wet leg is full and the zero is trimmed in service.",
     "A wet leg trimmed at atmospheric pressure reads wrong the moment the vessel is pressurised.",
     "Zero tại áp suất làm việc", "Với đo mức bằng DP: nhánh ướt đầy và zero được hiệu chỉnh khi đang vận hành.",
     "Nhánh ướt hiệu chỉnh ở áp suất khí quyển sẽ đọc sai ngay khi bình có áp."),
    ("Impulse line fill and vent", "No gas pocket, no condensate slug, no air in a liquid line.",
     "Vent at the high point, drain at the low point, then re-zero.",
     "Nạp và xả ống xung", "Không túi khí, không khối ngưng, không khí trong đường lỏng.",
     "Xả ở điểm cao, tháo ở điểm thấp, rồi đặt lại zero."),
    ("Alarm and trip test", "The setpoint that actually acts, not the one in the database.",
     "Drive the value past the setpoint and confirm the action, the annunciation and the time stamp.",
     "Kiểm tra cảnh báo và khóa", "Giá trị đặt thực sự tác động, không phải giá trị trong cơ sở dữ liệu.",
     "Đẩy giá trị vượt ngưỡng và xác nhận hành động, thông báo và dấu thời gian."),
]

FAILURES = [
    ("The tapping point in the wrong place",
     "A pressure tap two diameters downstream of a bend sees a distorted profile; a temperature sensor in a dead leg sees the pipe wall, not the fluid. The device is accurate and the number is wrong.",
     "Điểm lấy áp sai chỗ",
     "Điểm lấy áp cách khúc quanh hai đường kính thấy mặt cắt bị xáo trộn; cảm biến nhiệt trong nhánh chết thấy thành ống, không thấy lưu chất. Thiết bị chính xác và con số sai."),
    ("The impulse line that plugged",
     "Process fluid freezes, polymerises or settles in a line that is too long, too narrow, or has a dead leg. The transmitter keeps reading the last pressure it saw, with no diagnostic to say so.",
     "Ống xung bị tắc",
     "Lưu chất đông lại, polyme hóa hoặc lắng trong một tuyến quá dài, quá hẹp, hoặc có nhánh chết. Bộ truyền tiếp tục đọc áp suất cuối cùng nó thấy, không có chẩn đoán nào báo."),
    ("The shield grounded at both ends",
     "A shield earthed at both ends is a loop antenna with a current in it. The noise it injects is often worse than the noise it was fitted to reject.",
     "Vỏ bọc nối đất hai đầu",
     "Vỏ bọc nối đất hai đầu là một vòng ăng-ten có dòng chạy trong đó. Nhiễu nó đưa vào thường tệ hơn nhiễu nó được lắp để chống."),
    ("The wet leg that boiled",
     "A wet leg on a hot vessel loses its reference column and the level reads high, always high, and plausibly. Nobody notices until the vessel overfills.",
     "Nhánh ướt bị sôi",
     "Nhánh ướt trên bình nóng mất cột tham chiếu và mức đọc cao, luôn cao, và trông hợp lý. Không ai nhận ra cho đến khi bình tràn."),
    ("The IS calculation that ignored the cable",
     "The barrier and the transmitter match; the cable was never entered into the calculation. In IIC service a few hundred metres of ordinary cable can exceed the allowable inductance.",
     "Phép tính IS bỏ qua cáp",
     "Barrier và bộ truyền khớp nhau; cáp chưa bao giờ được đưa vào phép tính. Trong dịch vụ IIC, vài trăm mét cáp thường có thể vượt quá điện cảm cho phép."),
    ("The loop check that tested the wrong tag",
     "Two transmitters were swapped at the marshalling cabinet during a modification. Every check passes because every check confirms the signal arrives — not that it arrives from the right place.",
     "Kiểm tra vòng nhầm tag",
     "Hai bộ truyền bị đấu nhầm tại tủ đấu dây trong một lần sửa đổi. Mọi phép kiểm tra đều đạt vì chúng xác nhận tín hiệu đến — không xác nhận nó đến từ đúng chỗ."),
]


def build():
    pg = Page(
        "install.html",
        "ins",
        "Installation and hazardous area — making the reading true | I&amp;C",
        "Lắp đặt và vùng nguy hiểm — làm cho kết quả đo trung thực",
        "How installation decides whether an instrument's number is true: tapping point and impulse "
        "line rules, hazardous area zones, gas groups and temperature classes, the intrinsic safety "
        "entity concept with a cable-length calculation, grounding and shielding, and the commissioning "
        "checks that catch what the datasheet cannot.",
        "Cách lắp đặt quyết định con số của thiết bị có trung thực hay không: quy tắc điểm lấy áp và ống "
        "xung, phân vùng nguy hiểm, nhóm khí và cấp nhiệt độ, nguyên lý thực thể của an toàn tia lửa kèm "
        "phép tính chiều dài cáp, nối đất và bọc chống nhiễu, và các bước kiểm tra chạy thử mà datasheet "
        "không thể thay thế.",
    )

    body = page_intro(
        pg,
        "The datasheet describes a device on a bench",
        "Datasheet mô tả một thiết bị trên bàn thử",
        "Every accuracy figure you were quoted was measured with a clean pressure source, a short "
        "connection and a stable ambient temperature. On the plant you inherit a tapping point somebody "
        "chose at 4 p.m. on a Friday, forty metres of impulse line, and a shield grounded at both ends. "
        "This page is about the gap between the two.",
        "Mọi con số độ chính xác bạn được báo giá đều đo với nguồn áp sạch, kết nối ngắn và nhiệt độ môi "
        "trường ổn định. Tại nhà máy, bạn thừa hưởng một điểm lấy áp ai đó chọn lúc 4 giờ chiều thứ Sáu, "
        "bốn mươi mét ống xung, và một vỏ bọc nối đất hai đầu. Trang này nói về khoảng cách giữa hai "
        "điều đó.",
        [
            ("tap", "Where the number is decided", "Con số được quyết định ở đâu"),
            ("area", "Hazardous area", "Vùng nguy hiểm"),
            ("is", "Intrinsic safety", "An toàn tia lửa"),
            ("ground", "Grounding and shielding", "Nối đất và chống nhiễu"),
            ("commission", "Commissioning", "Chạy thử"),
            ("failures", "How installations fail", "Lắp đặt hỏng thế nào"),
        ],
    )

    # ---------------- 01 tapping ----------------
    body += section_open("01", "Where the number is decided", "Con số được quyết định ở đâu", pg, "tap")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="figure">
  %s
  <div class="figcap">%s</div>
</div>
<div class="sec-head mt40">
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("Half the error is installed, not manufactured",
             "Một nửa sai số đến từ lắp đặt, không từ chế tạo"),
        pg.p(
            "A pressure transmitter does not measure pressure; it measures the pressure at the end of "
            "its impulse line. A temperature sensor does not measure the fluid; it measures its own "
            "sheath, which is trying to reach the fluid. The installation is the measurement.",
            "Một bộ truyền áp không đo áp suất; nó đo áp suất ở cuối ống xung của nó. Một cảm biến nhiệt "
            "không đo lưu chất; nó đo chính vỏ bảo vệ của nó, thứ đang cố đạt tới nhiệt độ lưu chất. Lắp "
            "đặt chính là phép đo.",
        ),
        TAP_SVG,
        pg.span(
            "The rule is the same in both cases: slope the line so that whatever should not be there "
            "returns to the pipe. Gas service keeps condensate out; liquid service keeps gas out.",
            "Quy tắc giống nhau trong cả hai trường hợp: dốc ống để bất cứ thứ gì không nên có đều quay "
            "về đường ống. Dịch vụ khí loại bỏ nước ngưng; dịch vụ lỏng loại bỏ khí.",
        ),
        pg.h3("Tapping point rules by service", "Quy tắc điểm lấy áp theo dịch vụ"),
        pg.th("Service", "Dịch vụ"),
        pg.th("Tap position", "Vị trí lấy áp"),
        pg.th("Impulse line", "Ống xung"),
        pg.th("What you are avoiding", "Điều bạn đang tránh"),
    )
    for svc, pos, line, avoid, svc_vi, pos_vi, line_vi, avoid_vi in TAPS:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            pg.span(svc, svc_vi),
            pg.span(pos, pos_vi),
            pg.span(line, line_vi),
            pg.span(avoid, avoid_vi),
        )
    body += """
  </tbody>
</table>
</div>
<div class="note mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.span("Short is a specification, not a preference", "Ngắn là một yêu cầu kỹ thuật, không phải sở thích"),
        pg.p(
            "Every metre of impulse line adds lag and adds a place for the process to settle. A DP flow "
            "loop with a thirty-metre line answers in tens of seconds and cannot be tuned for a fast "
            "disturbance, however good the transmitter. Specify the run length, then design the layout "
            "to meet it — not the other way round.",
            "Mỗi mét ống xung thêm độ trễ và thêm một chỗ để quá trình lắng đọng. Một vòng đo lưu lượng "
            "DP với tuyến ba mươi mét đáp ứng trong hàng chục giây và không thể hiệu chỉnh cho nhiễu "
            "nhanh, dù bộ truyền tốt đến đâu. Hãy chỉ định chiều dài tuyến, rồi bố trí theo nó — không "
            "phải ngược lại.",
        ),
    )
    body += section_close()

    # ---------------- 02 hazardous area ----------------
    body += section_open("02", "Hazardous area", "Vùng nguy hiểm", pg, "area")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("Four questions, in this order", "Bốn câu hỏi, theo thứ tự này"),
        pg.p(
            "A hazardous area classification is not a single label. It is a zone, a gas group, a "
            "temperature class and a protection concept, and a device is only suitable when all four "
            "agree. Reading a nameplate is the easy part; knowing which four things you are reading is "
            "the part that gets missed.",
            "Phân loại vùng nguy hiểm không phải một nhãn duy nhất. Nó gồm vùng, nhóm khí, cấp nhiệt độ "
            "và khái niệm bảo vệ, và một thiết bị chỉ phù hợp khi cả bốn điều khớp nhau. Đọc nhãn thiết bị "
            "là phần dễ; biết mình đang đọc bốn thứ gì mới là phần hay bị bỏ sót.",
        ),
        pg.th("Term", "Thuật ngữ"),
        pg.th("What it tells you", "Nó cho bạn biết điều gì"),
    )
    for term, meaning, term_vi, meaning_vi in AREA:
        body += "<tr><td><strong>%s</strong></td><td>%s</td></tr>" % (
            pg.span(term, term_vi),
            pg.span(meaning, meaning_vi),
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
        pg.span("The mistake that survives inspection", "Sai sót vẫn qua được kiểm tra"),
        pg.p(
            "A device rated for a lower gas group is not made safe by installing it carefully. IIC "
            "equipment works in IIA service; IIA equipment in IIC service is a hazard that no amount of "
            "correct wiring fixes. The same applies to temperature class: a T4 device in a T6 "
            "requirement is a hot surface with a certificate that does not cover it.",
            "Một thiết bị chỉ định cho nhóm khí thấp hơn không trở nên an toàn bằng cách lắp đặt cẩn thận. "
            "Thiết bị IIC dùng được trong dịch vụ IIA; thiết bị IIA trong dịch vụ IIC là mối nguy mà mọi "
            "cách đấu dây đúng cũng không sửa được. Điều tương tự với cấp nhiệt độ: thiết bị T4 trong yêu "
            "cầu T6 là một bề mặt nóng với giấy chứng nhận không bao phủ nó.",
        ),
    )
    body += section_close()

    # ---------------- 03 intrinsic safety ----------------
    body += section_open("03", "Intrinsic safety", "An toàn tia lửa", pg, "is")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="formula">
  <i>%s</i><br>
  U<sub>o</sub> &le; U<sub>i</sub> &nbsp;&nbsp; I<sub>o</sub> &le; I<sub>i</sub> &nbsp;&nbsp; P<sub>o</sub> &le; P<sub>i</sub><br>
  <i>%s</i><br>
  C<sub>o</sub> &ge; C<sub>i</sub> + C<sub>cable</sub> &nbsp;&nbsp;&nbsp; L<sub>o</sub> &ge; L<sub>i</sub> + L<sub>cable</sub><br>
  <span class="r">%s</span>
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
      <div><dt>%s</dt><dd>%s</dd></div>
      <div><dt>%s</dt><dd>%s</dd></div>
    </div>
  </div>
</div>
""" % (
        pg.h2("The entity concept: match the numbers, then the cable",
             "Nguyên lý thực thể: khớp các con số, rồi đến cáp"),
        pg.p(
            "Intrinsic safety works by limiting the energy that can reach the hazardous area, so that "
            "no spark and no hot surface can ignite the atmosphere. It is the only protection concept "
            "that allows work on a live circuit, and the only one that permits Zone 0.",
            "An toàn tia lửa hoạt động bằng cách giới hạn năng lượng có thể tới vùng nguy hiểm, để không "
            "tia lửa và không bề mặt nóng nào có thể đốt cháy môi trường. Đây là khái niệm bảo vệ duy nhất "
            "cho phép làm việc trên mạch đang có điện, và duy nhất cho phép Vùng 0.",
        ),
        pg.span("The barrier output must not exceed the device input:", "Đầu ra của barrier không được vượt đầu vào thiết bị:"),
        pg.span("And the cable has to be counted, not assumed:", "Và cáp phải được tính, không được giả định:"),
        pg.span("The cable is part of the circuit. Half of all IS mistakes are made here.",
                "Cáp là một phần của mạch. Một nửa số sai sót IS xảy ra ở đây."),
        pg.h3("Simple apparatus", "Thiết bị đơn giản"),
        pg.p(
            "An RTD, a thermocouple, a switch or a junction box stores almost no energy, so it needs no "
            "certificate of its own — it is defined as simple apparatus. It still has a capacitance and "
            "an inductance, they are just small enough that nobody writes them down. On a long cable run "
            "with a tight inductance limit, that assumption is worth checking.",
            "Một RTD, cặp nhiệt điện, công tắc hay hộp nối lưu trữ gần như không năng lượng, nên nó không "
            "cần giấy chứng nhận riêng — nó được định nghĩa là thiết bị đơn giản. Nó vẫn có điện dung và "
            "điện cảm, chỉ là nhỏ đến mức không ai ghi lại. Trên một tuyến cáp dài với giới hạn điện cảm "
            "chặt, giả định đó đáng để kiểm tra.",
        ),
        pg.p(
            "The same applies to the transmitter: Ci and Li are on its certificate, usually in "
            "nanofarads and microhenries, and they are subtracted from what the cable is allowed to use.",
            "Điều tương tự với bộ truyền: Ci và Li có trên giấy chứng nhận của nó, thường tính bằng "
            "nanofara và microhenry, và chúng bị trừ khỏi phần cáp được phép dùng.",
        ),
        pg.span("Worked example", "Ví dụ tính toán"),
        pg.h3("A 4–20 mA loop in IIC service", "Một vòng 4–20 mA trong dịch vụ IIC"),
        pg.td("Transmitter", "Transmitter"),
        pg.td("C<sub>i</sub> = 5 nF, L<sub>i</sub> = 0", "C<sub>i</sub> = 5 nF, L<sub>i</sub> = 0"),
        pg.td("Barrier, IIC", "Barrier, IIC"),
        pg.td("C<sub>o</sub> = 100 nF, L<sub>o</sub> = 1 mH", "C<sub>o</sub> = 100 nF, L<sub>o</sub> = 1 mH"),
        pg.td("Cable", "Cáp"),
        pg.td("120 pF/m, 1.0 &micro;H/m", "120 pF/m, 1,0 &micro;H/m"),
        pg.td("By capacitance", "Theo điện dung"),
        pg.td("(100 &minus; 5) nF / 0.12 nF/m = 792 m", "(100 &minus; 5) nF / 0,12 nF/m = 792 m"),
        pg.td("By inductance", "Theo điện cảm"),
        pg.td("1 000 &micro;H / 1.0 &micro;H/m = 1 000 m", "1 000 &micro;H / 1,0 &micro;H/m = 1 000 m"),
    )
    body += section_close()

    # ---------------- 04 grounding ----------------
    body += section_open("04", "Grounding and shielding", "Nối đất và chống nhiễu", pg, "ground")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="grid c2">
  <div class="card">
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <h3>%s</h3>
    <p>%s</p>
  </div>
</div>
""" % (
        pg.h2("A shield is an antenna until you decide which end is ground",
             "Vỏ bọc là một ăng-ten cho đến khi bạn quyết định đầu nào là đất"),
        pg.p(
            "Shielding and grounding are the same problem seen twice. The shield must intercept the "
            "interference and carry it away; the signal reference must be a single point, or the "
            "difference between two points becomes a signal of its own.",
            "Chống nhiễu và nối đất là cùng một vấn đề nhìn hai lần. Vỏ bọc phải chặn nhiễu và mang nó "
            "đi; chuẩn tín hiệu phải là một điểm duy nhất, nếu không chênh lệch giữa hai điểm trở thành "
            "một tín hiệu của riêng nó.",
        ),
        pg.h3("Ground the shield at one end", "Nối đất vỏ bọc ở một đầu"),
        pg.p(
            "Normally the control-room end. Grounding both ends creates a loop, and a loop in a "
            "varying magnetic field carries a current — the shield then injects the noise it was "
            "installed to remove.",
            "Thường là đầu phòng điều khiển. Nối đất hai đầu tạo ra một vòng, và vòng trong từ trường "
            "biến thiên sẽ mang dòng — vỏ bọc khi đó đưa vào chính loại nhiễu nó được lắp để loại bỏ.",
        ),
        pg.h3("One reference point per loop", "Một điểm chuẩn cho mỗi vòng"),
        pg.p(
            "A 4–20 mA loop should be earthed in exactly one place. Two earths at different potentials "
            "put a current through the signal return that no filter will remove.",
            "Một vòng 4–20 mA chỉ nên nối đất đúng một chỗ. Hai điểm đất khác điện thế đưa dòng chạy qua "
            "đường hồi tín hiệu mà không bộ lọc nào loại bỏ được.",
        ),
        pg.h3("Isolate rather than bond", "Cách ly thay vì đấu chung"),
        pg.p(
            "Where two earths cannot be made equal — separate buildings, an earthed tank, a remote "
            "structure — a galvanic isolator breaks the loop instead of trying to win the argument.",
            "Khi không thể làm hai điểm đất bằng nhau — nhà khác nhau, bình chứa đã nối đất, kết cấu xa — "
            "một bộ cách ly galvanic phá vòng thay vì cố thắng cuộc tranh luận.",
        ),
        pg.h3("Never use the shield as a return", "Không bao giờ dùng vỏ bọc làm đường hồi"),
        pg.p(
            "The shield is not a conductor. Using it as a signal return puts the entire interference "
            "current of the cable in series with your measurement.",
            "Vỏ bọc không phải dây dẫn. Dùng nó làm đường hồi đặt toàn bộ dòng nhiễu của cáp nối tiếp với "
            "phép đo của bạn.",
        ),
        pg.h3("Separate power and signal", "Tách nguồn và tín hiệu"),
        pg.p(
            "Run signal cable in its own tray. Where it must cross power cable, cross at ninety degrees; "
            "parallel runs couple capacitance, and long parallel runs couple a lot of it.",
            "Đi cáp tín hiệu trong máng riêng. Nơi buộc phải cắt cáp nguồn, hãy cắt vuông góc; chạy song "
            "song gây ghép điện dung, và chạy song song dài thì ghép rất nhiều.",
        ),
        pg.h3("Bond before you improve the earth", "Đấu đẳng thế trước khi cải thiện điện trở đất"),
        pg.p(
            "Most noise problems are potential differences between two earthed points, not a bad rod. "
            "Bonding the structures together removes the difference; driving a deeper rod usually just "
            "moves it.",
            "Phần lớn vấn đề nhiễu là chênh lệch điện thế giữa hai điểm đã nối đất, không phải cọc đất "
            "tồi. Đấu đẳng thế các kết cấu với nhau loại bỏ chênh lệch; đóng cọc sâu hơn thường chỉ làm "
            "nó dịch đi.",
        ),
    )
    body += section_close()

    # ---------------- 05 commissioning ----------------
    body += section_open("05", "Commissioning", "Chạy thử", pg, "commission")
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
        pg.h2("Six checks that catch what the datasheet cannot",
             "Sáu bước kiểm tra bắt được điều datasheet không thể"),
        pg.p(
            "Commissioning is not a formality between installation and handover. It is the only point "
            "where the installed system is tested as a system, and the last point where a mistake is "
            "cheap.",
            "Chạy thử không phải thủ tục giữa lắp đặt và bàn giao. Đó là điểm duy nhất hệ đã lắp được kiểm "
            "tra như một hệ thống, và là điểm cuối cùng mà một sai sót còn rẻ.",
        ),
        pg.th("Check", "Bước kiểm tra"),
        pg.th("What it proves", "Nó chứng minh điều gì"),
        pg.th("How to do it properly", "Cách làm đúng"),
    )
    for check, proves, how, check_vi, proves_vi, how_vi in COMMISSION:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>" % (
            pg.span(check, check_vi),
            pg.span(proves, proves_vi),
            pg.span(how, how_vi),
        )
    body += """
  </tbody>
</table>
</div>
""" % ()
    body += section_close()

    # ---------------- 06 failures ----------------
    body += section_open("06", "How installations fail", "Lắp đặt hỏng thế nào", pg, "failures")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="grid c3">
""" % (
        pg.h2("Six failures that pass every inspection",
             "Sáu hư hỏng vẫn qua mọi lần kiểm tra"),
        pg.p(
            "None of these leaves a mark on a certificate. Each of them produces a number that looks "
            "like a measurement, which is worse than producing no number at all.",
            "Không trường hợp nào để lại dấu vết trên giấy chứng nhận. Mỗi trường hợp tạo ra một con số "
            "trông như kết quả đo, và điều đó tệ hơn là không có con số nào.",
        ),
    )
    for title, text, title_vi, text_vi in FAILURES:
        body += '<div class="card"><h3>%s</h3><p>%s</p></div>' % (
            pg.span(title, title_vi),
            pg.span(text, text_vi),
        )
    body += """
</div>
<div class="note warn mt24">
  <span class="lbl">%s</span>
  %s
</div>
<div class="nextprev">
  <a href="instruments.html"><span class="k">%s</span>%s</a>
  <a href="control.html" style="text-align:right"><span class="k">%s</span>%s</a>
</div>
""" % (
        pg.span("The cheapest hour in the project", "Giờ rẻ nhất trong dự án"),
        pg.p(
            "Walk the installation before the insulation is closed and the trays are covered. An "
            "afternoon with a drawing, a tape measure and the person who will maintain the loop finds "
            "more than a week of troubleshooting after start-up — and it is the only review where the "
            "fix is a bracket rather than a shutdown.",
            "Hãy đi kiểm tra công trình trước khi đóng cách nhiệt và đậy máng cáp. Một buổi chiều với bản "
            "vẽ, thước dây và người sẽ bảo trì vòng đo tìm được nhiều hơn một tuần xử lý sự cố sau khi "
            "chạy máy — và đó là lần xem xét duy nhất mà cách sửa là một cái giá đỡ, không phải một lần "
            "dừng nhà máy.",
        ),
        pg.span("Back", "Quay lại"),
        pg.span("Instrument reference", "Danh mục thiết bị"),
        pg.span("Next", "Tiếp"),
        pg.span("Control &amp; tuning", "Điều khiển &amp; hiệu chỉnh"),
    )
    body += section_close()

    write("install.html", render(pg, body, "install.html"))
