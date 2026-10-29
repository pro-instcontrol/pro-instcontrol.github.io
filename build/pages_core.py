# -*- coding: utf-8 -*-
"""Fundamentals + instrument reference pages."""

from framework import Page, section_open, section_close, write, render, page_intro


# --------------------------------------------------------------------------
# FUNDAMENTALS
# --------------------------------------------------------------------------
def build_fundamentals():
    pg = Page(
        "fundamentals.html",
        "fun",
        "Fundamentals — the measurement chain | I&amp;C Field Guide",
        "Cơ bản — chuỗi đo lường | Sổ tay I&amp;C",
        "How a physical variable becomes a control signal: sensor, transmitter, 4–20 mA, "
        "accuracy vocabulary, calibration and the installation rules that decide whether "
        "the number is true.",
        "Cách một đại lượng vật lý trở thành tín hiệu điều khiển: cảm biến, bộ truyền, "
        "4–20 mA, thuật ngữ độ chính xác, hiệu chuẩn và các quy tắc lắp đặt.",
    )

    body = page_intro(
        pg,
        "From a physical quantity to a number you can trust",
        "Từ đại lượng vật lý đến con số đáng tin",
        "Every control loop begins with a measurement that is already imperfect. Understanding where "
        "the imperfection enters — and how it is expressed — is what separates a specification that "
        "works from one that only looks precise.",
        "Mọi vòng điều khiển đều bắt đầu bằng một phép đo vốn đã không hoàn hảo. Hiểu được sai số "
        "xâm nhập ở đâu — và được diễn đạt thế nào — là điều phân biệt một bản chỉ định hiệu quả với "
        "một bản chỉ định chỉ trông có vẻ chính xác.",
        [
            ("chain", "The chain", "Chuỗi đo"),
            ("signals", "Signal standards", "Tiêu chuẩn tín hiệu"),
            ("why", "Why 4–20 mA", "Vì sao 4–20 mA"),
            ("accuracy", "The vocabulary of error", "Từ vựng về sai số"),
            ("env", "Environment &amp; certification", "Môi trường &amp; chứng nhận"),
            ("install", "Installation rules", "Quy tắc lắp đặt"),
        ],
    )

    # 01 chain
    body += section_open("01", "The chain", "Chuỗi đo", pg, "chain")
    body += """
<div class="grid c4">
  <div class="card"><span class="n">01</span><h3>%s</h3><p>%s</p></div>
  <div class="card"><span class="n">02</span><h3>%s</h3><p>%s</p></div>
  <div class="card"><span class="n">03</span><h3>%s</h3><p>%s</p></div>
  <div class="card"><span class="n">04</span><h3>%s</h3><p>%s</p></div>
</div>
<div class="mt24">
%s
</div>
<div class="note mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h3("Sensor", "Cảm biến"),
        pg.p(
            "The element in contact with the process that converts a physical effect into a "
            "measurable one — a diaphragm deflection, a resistance change, a voltage.",
            "Phần tử tiếp xúc với quá trình, biến một hiệu ứng vật lý thành hiệu ứng đo được — "
            "độ võng màng, sự thay đổi điện trở, một điện áp.",
        ),
        pg.h3("Transducer", "Bộ chuyển đổi"),
        pg.p(
            "Converts that intermediate effect into an electrical quantity. Often the same silicon "
            "or ceramic body as the sensor; the boundary between the two is practical, not physical.",
            "Chuyển hiệu ứng trung gian thành đại lượng điện. Thường cùng một thân silic hoặc gốm "
            "với cảm biến; ranh giới giữa hai phần là quy ước thực hành, không phải vật lý.",
        ),
        pg.h3("Transmitter", "Bộ truyền tín hiệu"),
        pg.p(
            "Linearises, compensates for temperature, applies damping, and drives a standard signal "
            "onto the wires. This is the device you specify, tag and calibrate.",
            "Tuyến tính hóa, bù nhiệt độ, đặt hằng số làm mượt, và đưa tín hiệu chuẩn ra dây. Đây là "
            "thiết bị bạn chỉ định, gắn thẻ và hiệu chuẩn.",
        ),
        pg.h3("Input &amp; decision", "Đầu vào &amp; quyết định"),
        pg.p(
            "An analogue input card digitises the signal; the controller compares it with the setpoint "
            "and computes an output. From here the value is data, not physics.",
            "Mô-đun đầu vào tương tự số hóa tín hiệu; bộ điều khiển so sánh với giá trị đặt và tính "
            "đầu ra. Từ đây giá trị là dữ liệu, không còn là vật lý.",
        ),
        pg.p(
            "Each stage adds its own error. A transmitter specified at ±0.075&nbsp;% of span mounted on a "
            "manifold with a 2&nbsp;m uninsulated impulse line will not deliver ±0.075&nbsp;% to the "
            "controller — the installation, not the datasheet, sets the real accuracy.",
            "Mỗi khâu đều thêm sai số của nó. Một bộ truyền đạt ±0,075&nbsp;% dải đo nhưng lắp trên "
            "manifold có 2&nbsp;m ống xung không bọc cách nhiệt sẽ không mang ±0,075&nbsp;% đến bộ điều "
            "khiển — chính cách lắp đặt, chứ không phải datasheet, quyết định độ chính xác thực.",
            "small dim",
        ),
        pg.span("Practical consequence", "Hệ quả thực tế"),
        pg.p(
            "Specify the loop, not the device. Write the accuracy requirement against the variable the "
            "operator actually needs — flow in t/h at the normal operating point, not pressure in bar at "
            "full scale.",
            "Hãy chỉ định cả vòng đo, không chỉ thiết bị. Viết yêu cầu độ chính xác theo đúng biến mà "
            "người vận hành cần — lưu lượng t/h tại điểm làm việc bình thường, không phải áp suất bar "
            "tại thang đo đầy.",
        ),
    )
    body += section_close()

    # 02 signals
    body += section_open("02", "Signal standards", "Tiêu chuẩn tín hiệu", pg, "signals")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
    <tr><td><strong>4–20 mA</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>0–10 V</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>HART</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>PROFIBUS PA</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>FOUNDATION Fieldbus H1</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>Modbus RTU / TCP</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>OPC UA</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>Ethernet-APL</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>WirelessHART</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>
  </tbody>
</table>
</div>
""" % (
        pg.h2("Nine ways to move a number", "Chín cách truyền một con số"),
        pg.p(
            "The analogue current loop still carries most of the world's process data, but it is no "
            "longer the only option. Choose by distance, environment, diagnostics requirement and "
            "whether the device needs to be configured remotely.",
            "Vòng dòng điện tương tự vẫn mang phần lớn dữ liệu quá trình trên thế giới, nhưng không còn "
            "là lựa chọn duy nhất. Hãy chọn theo khoảng cách, môi trường, yêu cầu chẩn đoán và việc "
            "thiết bị có cần cấu hình từ xa hay không.",
        ),
        pg.th("Standard", "Tiêu chuẩn"),
        pg.th("Type", "Loại"),
        pg.th("Reach", "Khoảng cách"),
        pg.th("Where it fits", "Phù hợp khi"),
        pg.td("Analogue, 2-wire", "Tương tự, 2 dây"),
        pg.td("km, twisted pair", "km, cáp xoắn"),
        pg.td("Default for anything safety-relevant or simple; fault band per NAMUR NE&nbsp;43.", "Mặc định cho mọi thứ đơn giản hoặc liên quan an toàn; dải báo lỗi theo NAMUR NE&nbsp;43."),
        pg.td("Analogue, 3/4-wire", "Tương tự, 3/4 dây"),
        pg.td("&lt; 30 m", "&lt; 30 m"),
        pg.td("Panel and skid wiring where both ends share a ground; not for field runs.", "Đấu dây trong tủ và skid khi hai đầu chung mass; không dùng cho tuyến hiện trường."),
        pg.td("Hybrid: 4–20 mA + FSK", "Lai: 4–20 mA + FSK"),
        pg.td("~1 km on the loop", "~1 km trên chính vòng"),
        pg.td("Configuration and diagnostics without extra cable — the usual compromise.", "Cấu hình và chẩn đoán không cần thêm cáp — giải pháp thỏa hiệp thường dùng."),
        pg.td("Digital fieldbus", "Fieldbus số"),
        pg.td("1.9 km per segment", "1,9 km mỗi segment"),
        pg.td("Ex areas, many devices per segment, profile-based interchangeability.", "Khu vực Ex, nhiều thiết bị mỗi segment, thay thế theo profile."),
        pg.td("Digital fieldbus", "Fieldbus số"),
        pg.td("1.9 km per segment", "1,9 km mỗi segment"),
        pg.td("Control in the field — PID can run in the device, not the host.", "Điều khiển tại hiện trường — PID chạy trong thiết bị, không cần host."),
        pg.td("Protocol over serial / Ethernet", "Giao thức trên serial / Ethernet"),
        pg.td("Site-wide", "Toàn nhà máy"),
        pg.td("Power meters, analysers, package units. Ubiquitous, but no standard device profile.", "Đồng hồ điện, máy phân tích, thiết bị trọn gói. Phổ biến nhưng không có profile thiết bị chuẩn."),
        pg.td("Protocol over Ethernet", "Giao thức trên Ethernet"),
        pg.td("Site / enterprise", "Nhà máy / doanh nghiệp"),
        pg.td("Vendor-neutral data to SCADA, MES and historians; built-in security model.", "Dữ liệu trung lập về SCADA, MES và historian; có mô hình bảo mật tích hợp."),
        pg.td("Digital, 2-wire Ethernet", "Số, Ethernet 2 dây"),
        pg.td("1 km, trunk + spurs", "1 km, trục + nhánh"),
        pg.td("New plants wanting Ethernet speed into Zone 0/1 without fibre.", "Nhà máy mới cần tốc độ Ethernet vào vùng Zone 0/1 mà không dùng cáp quang."),
        pg.td("Wireless mesh, 2.4 GHz", "Mesh không dây, 2,4 GHz"),
        pg.td("Hundreds of metres, multi-hop", "Hàng trăm mét, đa bước"),
        pg.td("Retrofit and monitoring points where cabling costs more than the instrument.", "Cải tạo và điểm quan trắc nơi chi phí đi cáp lớn hơn thiết bị."),
    )
    body += section_close()

    # 03 why 4-20
    body += section_open("03", "Why 4–20 mA survived", "Vì sao 4–20 mA tồn tại", pg, "why")
    body += """
<div class="g-2-1">
  <div>
    %s
    %s
    <div class="note warn">
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
        pg.h2("A live zero, a broken wire, and no voltage drop", "Điểm không sống, dây đứt, và không sụt áp"),
        pg.p(
            "The loop is a current source. Current is the same at every point in a series circuit, so a "
            "50&nbsp;Ω sense resistor at the far end reads the same value regardless of how much copper "
            "the signal travelled through. Voltage signals cannot say that — they lose a little at every "
            "joint.",
            "Vòng đo là một nguồn dòng. Dòng điện như nhau tại mọi điểm trong mạch nối tiếp, nên điện "
            "trở cảm biến 50&nbsp;Ω ở đầu xa đọc cùng một giá trị bất kể tín hiệu đã đi qua bao nhiêu "
            "đồng. Tín hiệu điện áp không làm được vậy — chúng mất một ít ở mỗi mối nối.",
        ),
        pg.span("Watch the fault band", "Cẩn thận dải báo lỗi"),
        pg.p(
            "Starting the scale at 4&nbsp;mA instead of 0 gives a <em>live zero</em>: a genuine zero "
            "reading draws 4&nbsp;mA, so 0&nbsp;mA can only mean a broken wire or a dead transmitter. "
            "That single design choice is why a technician can diagnose a loop with a multimeter and no "
            "diagnostic software.",
            "Bắt thang đo từ 4&nbsp;mA thay vì 0 tạo ra <em>điểm không sống</em>: giá trị không thật sự "
            "tiêu thụ 4&nbsp;mA, nên 0&nbsp;mA chỉ có thể là dây đứt hoặc bộ truyền hỏng. Chính lựa chọn "
            "thiết kế đó giúp kỹ thuật viên chẩn đoán vòng đo bằng một đồng hồ vạn năng, không cần phần "
            "mềm.",
        )
        + pg.p(
            "NAMUR NE&nbsp;43 reserves the region below 3.6&nbsp;mA and above 21.0&nbsp;mA for fault "
            "signalling. A transmitter configured to saturate at 20&nbsp;mA for a real over-range reading "
            "will be indistinguishable from a failure unless both ends agree on the convention.",
            "NAMUR NE&nbsp;43 dành vùng dưới 3,6&nbsp;mA và trên 21,0&nbsp;mA cho báo lỗi. Một bộ truyền "
            "đặt bão hòa tại 20&nbsp;mA khi vượt dải thật sẽ không phân biệt được với hư hỏng, trừ khi "
            "hai đầu thống nhất quy ước.",
        ),
        pg.span("Loop arithmetic", "Số học vòng đo"),
        pg.h3("Sizing a 2-wire loop", "Tính toán vòng 2 dây"),
        pg.td("Supply", "Nguồn"),
        pg.td("24 V DC nominal (19–30 V usable)", "24 V DC danh định (19–30 V khả dụng)"),
        pg.td("Minimum", "Tối thiểu"),
        pg.td("Transmitter needs ≈ 12–17 V to operate", "Bộ truyền cần ≈ 12–17 V để hoạt động"),
        pg.td("Budget", "Ngân sách áp"),
        pg.td("V<sub>supply</sub> − 12 V ≥ I<sub>max</sub> × (R<sub>wire</sub> + R<sub>sense</sub>)", "V<sub>nguồn</sub> − 12 V ≥ I<sub>max</sub> × (R<sub>dây</sub> + R<sub>cảm biến</sub>)"),
        pg.td("Sense resistor", "Điện trở cảm biến"),
        pg.td("250 Ω gives 1–5 V for 4–20 mA", "250 Ω cho 1–5 V với 4–20 mA"),
    )
    body += section_close()

    # 04 accuracy vocabulary
    body += section_open("04", "The vocabulary of error", "Từ vựng về sai số", pg, "accuracy")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>
    <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>
  </tbody>
</table>
</div>
<div class="note">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Eight words that decide whether the number is true", "Tám từ quyết định con số có đúng không"),
        pg.p(
            "Instrument datasheets are written in a private dialect. These are the terms that actually "
            "change a specification — and the traps hidden inside each.",
            "Datasheet thiết bị được viết bằng một thứ tiếng riêng. Đây là những thuật ngữ thực sự làm "
            "thay đổi bản chỉ định — và cái bẫy nằm trong mỗi từ.",
        ),
        pg.th("Term", "Thuật ngữ"),
        pg.th("What it means", "Ý nghĩa"),
        pg.th("The trap", "Cái bẫy"),
        pg.span("Accuracy", "Độ chính xác"),
        pg.span("Closeness of the indicated value to the true value, under reference conditions.", "Mức gần đúng của giá trị chỉ thị so với giá trị thật, trong điều kiện chuẩn."),
        pg.span("% of span is not % of reading. At 20&nbsp;% of span, ±0.5&nbsp;% span becomes ±2.5&nbsp;% of reading.", "% dải đo không phải % giá trị đọc. Tại 20&nbsp;% dải, ±0,5&nbsp;% dải thành ±2,5&nbsp;% giá trị đọc."),
        pg.span("Repeatability", "Độ lặp lại"),
        pg.span("Spread of readings for the same input, approached from the same direction.", "Độ phân tán của kết quả với cùng đầu vào, tiếp cận từ cùng một phía."),
        pg.span("Usually much better than accuracy — quoting it instead of accuracy is a classic move.", "Thường tốt hơn nhiều so với độ chính xác — trích dẫn nó thay cho độ chính xác là chiêu quen thuộc."),
        pg.span("Hysteresis", "Độ trễ"),
        pg.span("Difference between up-scale and down-scale readings at the same input.", "Chênh lệch giữa giá trị đọc khi tăng và khi giảm tại cùng đầu vào."),
        pg.span("Mechanical linkages and valve packing dominate; invisible on a bench calibration.", "Cơ cấu cơ khí và đệm van chi phối; không thấy được khi hiệu chuẩn trên bàn."),
        pg.span("Drift", "Độ trôi"),
        pg.span("Change in zero and span over time, usually per year, at reference conditions.", "Thay đổi điểm không và dải đo theo thời gian, thường tính mỗi năm, ở điều kiện chuẩn."),
        pg.span("Drift sets the calibration interval. A ±0.1&nbsp;%/yr device is a different asset from ±0.02&nbsp;%/5&nbsp;yr.", "Độ trôi quyết định chu kỳ hiệu chuẩn. Thiết bị ±0,1&nbsp;%/năm là tài sản khác với ±0,02&nbsp;%/5&nbsp;năm."),
        pg.span("Dead band", "Dải chết"),
        pg.span("Input change that produces no output change at all.", "Thay đổi đầu vào không tạo ra bất kỳ thay đổi đầu ra nào."),
        pg.span("In a control valve this is stiction, and it is the most common cause of a cycling loop.", "Với van điều khiển đây là ma sát tĩnh, nguyên nhân phổ biến nhất của vòng dao động."),
        pg.span("Resolution", "Độ phân giải"),
        pg.span("Smallest change the device can distinguish.", "Thay đổi nhỏ nhất thiết bị phân biệt được."),
        pg.span("A 12-bit input card resolves 1 part in 4096 of span — often coarser than the transmitter.", "Card đầu vào 12 bit phân giải 1/4096 dải — thường thô hơn bản thân bộ truyền."),
        pg.span("Response time", "Thời gian đáp ứng"),
        pg.span("Time to reach 63&nbsp;% (T63) or 90&nbsp;% (T90) of a step change.", "Thời gian đạt 63&nbsp;% (T63) hoặc 90&nbsp;% (T90) của một thay đổi bậc thang."),
        pg.span("Damping is often set to hide noise — and it adds dead time to the loop.", "Hằng số làm mượt thường được đặt để che nhiễu — và nó thêm thời gian trễ cho vòng."),
        pg.span("Turndown / rangeability", "Tỷ số điều chỉnh"),
        pg.span("Ratio of maximum to minimum usable measurement within stated accuracy.", "Tỷ số giữa giá trị lớn nhất và nhỏ nhất còn dùng được trong độ chính xác công bố."),
        pg.span("An orifice is 3:1–5:1; a Coriolis meter can be 100:1. This decides low-flow performance.", "Lỗ khoan là 3:1–5:1; Coriolis có thể 100:1. Điều này quyết định hiệu năng ở lưu lượng thấp."),
        pg.span("Adding errors", "Cộng sai số"),
        pg.p(
            "Independent random errors combine as the square root of the sum of squares; systematic "
            "errors add directly. Do not average a datasheet accuracy with an installation error and call "
            "it the loop accuracy — treat the installation term as systematic and add it.",
            "Các sai số ngẫu nhiên độc lập cộng theo căn bậc hai tổng bình phương; sai số hệ thống cộng "
            "trực tiếp. Đừng lấy trung bình độ chính xác datasheet với sai số lắp đặt rồi gọi đó là độ "
            "chính xác của vòng — hãy coi sai số lắp đặt là hệ thống và cộng thẳng.",
        ),
    )
    body += section_close()

    # 05 environment
    body += section_open("05", "Environment &amp; certification", "Môi trường &amp; chứng nhận", pg, "env")
    body += """
<div class="grid c3">
  <div class="card">
    <span class="n">IP</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <span class="n">Ex</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <span class="n">SIL</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
</div>
<div class="note mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h3("Ingress protection", "Cấp bảo vệ"),
        pg.p(
            "IEC 60529: first digit is solids, second is water. IP66/IP67 for washdown and outdoor; "
            "IP54 is not an outdoor rating in monsoon climates.",
            "IEC 60529: chữ số đầu là vật rắn, chữ số sau là nước. IP66/IP67 cho rửa trôi và ngoài trời; "
            "IP54 không phải cấp ngoài trời ở khí hậu gió mùa.",
        ),
        pg.h3("Hazardous area", "Khu vực nguy hiểm"),
        pg.p(
            "IEC 60079 zoning: Zone 0/1/2 for gas, 20/21/22 for dust. Intrinsic safety (Ex&nbsp;ia) suits "
            "loops; flameproof (Ex&nbsp;d) suits high-power field devices. Entity parameters must match "
            "the barrier.",
            "Phân vùng IEC 60079: Zone 0/1/2 cho khí, 20/21/22 cho bụi. An toàn tia lửa (Ex&nbsp;ia) phù "
            "hợp vòng đo; vỏ chống cháy nổ (Ex&nbsp;d) phù hợp thiết bị công suất lớn. Thông số entity "
            "phải khớp với barrier.",
        ),
        pg.h3("Functional safety", "An toàn chức năng"),
        pg.p(
            "IEC 61508 defines SIL 1–4; IEC 61511 applies it to process SIS. A SIL rating is a property "
            "of the whole loop — sensor, logic solver, final element and proof-test interval — never of "
            "one device alone.",
            "IEC 61508 định nghĩa SIL 1–4; IEC 61511 áp dụng cho SIS trong quá trình. Cấp SIL là thuộc "
            "tính của cả vòng — cảm biến, bộ xử lý logic, phần tử chấp hành và chu kỳ kiểm chứng — "
            "không bao giờ của riêng một thiết bị.",
        ),
        pg.span("Also check", "Cũng cần kiểm tra"),
        pg.p(
            "Ambient temperature range, EMC per IEC 61000, wetted-material compatibility, process "
            "temperature at the diaphragm, and whether the local display is readable at &minus;5&nbsp;°C "
            "in the morning.",
            "Dải nhiệt độ môi trường, EMC theo IEC 61000, tương thích vật liệu ướt, nhiệt độ quá trình "
            "tại màng, và liệu màn hình tại chỗ có đọc được ở &minus;5&nbsp;°C vào buổi sáng.",
        ),
    )
    body += section_close()

    # 06 installation
    body += section_open("06", "Installation decides the answer", "Lắp đặt quyết định kết quả", pg, "install")
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
<div class="nextprev">
  <a href="index.html"><span class="k">%s</span>%s</a>
  <a href="instruments.html" style="text-align:right"><span class="k">%s</span>%s</a>
</div>
""" % (
        pg.h2("Six rules that survive every project", "Sáu quy tắc đúng trong mọi dự án"),
        pg.p(
            "A correct device installed wrongly reads wrongly forever. These are the failures that show "
            "up in commissioning, not in the datasheet.",
            "Thiết bị đúng mà lắp sai sẽ đọc sai mãi mãi. Đây là những lỗi xuất hiện khi chạy thử, "
            "không phải trong datasheet.",
        ),
        pg.h3("Flow: respect the straight run", "Lưu lượng: tôn trọng đoạn thẳng"),
        pg.p(
            "ISO 5167 asks for 5–10 D upstream and 2–5 D downstream for an orifice, depending on the "
            "upstream fitting. A 90° elbow two diameters upstream biases the reading by a few percent "
            "forever.",
            "ISO 5167 yêu cầu 5–10 D phía trước và 2–5 D phía sau với lỗ khoan, tùy phụ kiện phía "
            "trước. Một khuỷu 90° cách hai đường kính sẽ làm lệch kết quả vài phần trăm vĩnh viễn.",
        ),
        pg.h3("Temperature: immerse past the tip", "Nhiệt độ: ngập qua đầu cảm biến"),
        pg.p(
            "A thermowell must reach far enough into the flow that the sensing element sees the process, "
            "not the well wall. Too short and you measure the pipe, with a time constant of minutes "
            "instead of seconds.",
            "Ống bảo vệ nhiệt phải cắm đủ sâu vào dòng chảy để phần tử cảm nhận thấy quá trình, không "
            "phải thành ống. Quá ngắn, bạn đo chính đường ống, với hằng số thời gian hàng phút thay vì giây.",
        ),
        pg.h3("Pressure: slope the impulse line", "Áp suất: tạo độ dốc ống xung"),
        pg.p(
            "Slope towards the process for gas, away for liquid, so condensate or gas bubbles drain and "
            "do not sit on the diaphragm. Add a condensate pot for steam and keep both legs at the same "
            "temperature.",
            "Dốc về phía quá trình với khí, dốc ra xa với chất lỏng, để nước ngưng hoặc bọt khí thoát ra "
            "và không đọng trên màng. Thêm bình ngưng cho hơi và giữ hai nhánh cùng nhiệt độ.",
        ),
        pg.h3("Level: the reference leg is a measurement", "Mức: nhánh tham chiếu cũng là phép đo"),
        pg.p(
            "On a closed tank the low-pressure leg is a second measurement. If it is wet and its density "
            "changes with ambient temperature, the level reading drifts with the weather.",
            "Với bình kín, nhánh áp thấp là một phép đo thứ hai. Nếu nhánh ướt và khối lượng riêng thay "
            "đổi theo nhiệt độ môi trường, kết quả đo mức sẽ trôi theo thời tiết.",
        ),
        pg.h3("Wiring: shield one end only", "Đấu dây: chỉ nối đất một đầu vỏ chống nhiễu"),
        pg.p(
            "Grounding both ends creates a loop that picks up every drive in the plant. Ground at the "
            "cabinet, leave the field end floating, and separate signal from power in the tray.",
            "Nối đất hai đầu tạo vòng nhiễu thu mọi biến tần trong nhà máy. Nối đất tại tủ, để đầu hiện "
            "trường hở, và tách cáp tín hiệu khỏi cáp động lực trong máng.",
        ),
        pg.h3("Commission: prove the loop end to end", "Chạy thử: chứng minh cả vòng từ đầu đến cuối"),
        pg.p(
            "Inject at the sensor, read at the HMI, and record the deviation. Loop checking is not a "
            "formality — it is the only moment when the whole chain is verified at once.",
            "Bơm tín hiệu tại cảm biến, đọc tại HMI, và ghi lại độ lệch. Kiểm tra vòng không phải thủ tục "
            "hình thức — đó là lúc duy nhất toàn bộ chuỗi được kiểm chứng cùng lúc.",
        ),
        pg.span("Back", "Quay lại"),
        pg.span("Overview", "Tổng quan"),
        pg.span("Next", "Tiếp"),
        pg.span("Instrument reference", "Danh mục thiết bị"),
    )
    body += section_close()

    write("fundamentals.html", render(pg, body, "fundamentals.html"))


# --------------------------------------------------------------------------
# INSTRUMENTS
# --------------------------------------------------------------------------
ROWS = [
    # fam, name_en, name_vi, principle_en, principle_vi, acc, best_en, best_vi, watch_en, watch_vi
    ("pressure", "Bourdon tube gauge", "Áp kế ống Bourdon",
     "Elastic deformation of a curved tube straightens under pressure.",
     "Ống cong biến dạng đàn hồi và duỗi thẳng dưới áp suất.",
     "±0.5–1.0 % FS", "Local indication, utilities, pump discharge.", "Chỉ thị tại chỗ, tiện ích, đầu đẩy bơm.",
     "No signal output; fatigue under vibration.", "Không có tín hiệu ra; mỏi do rung."),
    ("pressure", "Piezoresistive transmitter", "Bộ truyền áp điện trở",
     "Silicon diaphragm with an implanted strain-gauge bridge.",
     "Màng silic với cầu điện trở áp điện trở cấy ion.",
     "±0.1–0.25 % span", "General process pressure, OEM, low cost.", "Áp suất quá trình thông thường, OEM, chi phí thấp.",
     "Temperature error at the diaphragm; overpressure shifts zero.", "Sai số nhiệt tại màng; quá áp làm lệch điểm không."),
    ("pressure", "Capacitive DP transmitter", "Bộ truyền áp vi sai điện dung",
     "Capacitance change as a diaphragm deflects between two plates.",
     "Điện dung thay đổi khi màng võng giữa hai bản cực.",
     "±0.05–0.1 % span", "Flow, level and density — the workhorse of the plant.", "Lưu lượng, mức và khối lượng riêng — thiết bị chủ lực.",
     "Zero drift, impulse-line effects, static-pressure error.", "Trôi điểm không, ảnh hưởng ống xung, sai số áp tĩnh."),
    ("pressure", "Piezoelectric sensor", "Cảm biến áp điện",
     "Charge generated by quartz or ceramic under mechanical stress.",
     "Điện tích sinh ra từ thạch anh hoặc gốm dưới ứng suất cơ học.",
     "±1 % FS", "Fast dynamic pressure: engines, blast, water hammer.", "Áp suất động nhanh: động cơ, nổ, va đập thủy lực.",
     "Cannot hold a static reading — charge leaks away.", "Không giữ được giá trị tĩnh — điện tích rò dần."),

    ("temperature", "Pt100 RTD, 3- or 4-wire", "Pt100 RTD, 3 hoặc 4 dây",
     "Platinum resistance rises predictably with temperature (α = 0.00385/°C).",
     "Điện trở bạch kim tăng có quy luật theo nhiệt độ (α = 0,00385/°C).",
     "±0.15 °C (class A)", "Accuracy-critical loops, −200 to 600 °C.", "Vòng cần chính xác, −200 đến 600 °C.",
     "Lead resistance in 2-wire; self-heating in still fluid.", "Điện trở dây dẫn ở 2 dây; tự nóng trong môi trường tĩnh."),
    ("temperature", "Thermocouple type K", "Cặp nhiệt điện loại K",
     "Seebeck emf from a junction of two dissimilar metals.",
     "Suất điện động Seebeck từ mối nối hai kim loại khác nhau.",
     "±2.5 °C or 0.75 %", "Wide range, fast response, rugged and cheap.", "Dải rộng, đáp ứng nhanh, bền và rẻ.",
     "Cold-junction compensation, ageing drift, EMF pickup.", "Bù nhiệt độ mối nối lạnh, trôi do lão hóa, thu nhiễu."),
    ("temperature", "Thermocouple type S / R / B", "Cặp nhiệt điện loại S / R / B",
     "Platinum-rhodium junctions for very high temperature.",
     "Mối nối bạch kim-rhodium cho nhiệt độ rất cao.",
     "±1.5 °C", "Furnaces, kilns, glass above 1200 °C.", "Lò nung, lò thủy tinh trên 1200 °C.",
     "Expensive, low sensitivity, needs a high-gain input.", "Đắt, độ nhạy thấp, cần đầu vào hệ số khuếch đại cao."),
    ("temperature", "Thermistor (NTC)", "Nhiệt điện trở (NTC)",
     "Semiconductor resistance falls steeply with temperature.",
     "Điện trở bán dẫn giảm mạnh theo nhiệt độ.",
     "±0.2 °C", "HVAC, battery packs, narrow bands with high resolution.", "HVAC, pack pin, dải hẹp với độ phân giải cao.",
     "Strongly non-linear; limited to a narrow range.", "Rất phi tuyến; chỉ dùng trong dải hẹp."),
    ("temperature", "Infrared pyrometer", "Hỏa kế hồng ngoại",
     "Radiance in a waveband, converted via emissivity.",
     "Bức xạ trong một dải bước sóng, quy đổi qua độ phát xạ.",
     "±1 % of reading", "Moving targets, rotating kilns, non-contact.", "Vật thể chuyển động, lò quay, không tiếp xúc.",
     "Emissivity assumption dominates the error.", "Giả thiết độ phát xạ chi phối toàn bộ sai số."),

    ("flow", "Orifice plate + DP", "Lỗ khoan + áp vi sai",
     "Bernoulli: differential pressure across a restriction ∝ flow².",
     "Bernoulli: áp vi sai qua tiết lưu ∝ lưu lượng².",
     "±0.6–1.5 % of reading", "Steam, gas, large lines, low capital cost.", "Hơi, khí, tuyến lớn, chi phí đầu tư thấp.",
     "Permanent pressure loss; needs straight run; edge wear.", "Tổn thất áp vĩnh viễn; cần đoạn thẳng; mòn cạnh."),
    ("flow", "Coriolis mass meter", "Đồng hồ khối lượng Coriolis",
     "Coriolis force twists a vibrating tube in proportion to mass flow.",
     "Lực Coriolis làm xoắn ống rung tỷ lệ với lưu lượng khối.",
     "±0.1–0.2 % of reading", "Custody transfer, density, viscous or two-phase fluids.", "Giao nhận, khối lượng riêng, chất lỏng nhớt hoặc hai pha.",
     "Cost, size limits, sensitive to entrained gas.", "Chi phí, giới hạn kích cỡ, nhạy với bọt khí."),
    ("flow", "Magnetic flowmeter", "Đồng hồ điện từ",
     "Faraday induction: conductive fluid moving through a field generates an emf.",
     "Cảm ứng Faraday: chất lỏng dẫn điện chuyển động trong từ trường sinh suất điện động.",
     "±0.2–0.5 % of reading", "Water, slurry, pulp; no obstruction, no pressure loss.", "Nước, bùn, bột giấy; không cản dòng, không tổn thất áp.",
     "Fluid must be conductive; liner erosion; empty-pipe noise.", "Chất lỏng phải dẫn điện; mòn lót; nhiễu khi ống rỗng."),
    ("flow", "Vortex shedding meter", "Đồng hồ xoáy",
     "Frequency of vortices shed behind a bluff body ∝ velocity.",
     "Tần số xoáy sau vật cản tỷ lệ với vận tốc.",
     "±0.75–1.0 % of reading", "Steam and gas where maintenance access is poor.", "Hơi và khí nơi khó bảo trì.",
     "Low-flow cut-off; vibration is read as flow.", "Ngưỡng cắt lưu lượng thấp; rung bị đọc thành lưu lượng."),
    ("flow", "Ultrasonic transit-time", "Siêu âm thời gian truyền",
     "Difference in transit time upstream vs downstream.",
     "Chênh lệch thời gian truyền xuôi và ngược dòng.",
     "±0.5–1.0 % of reading", "Clamp-on retrofit, large water pipes.", "Kẹp ngoài cải tạo, ống nước lớn.",
     "Needs a developed profile; entrained gas breaks it.", "Cần profile phát triển; bọt khí làm sai."),
    ("flow", "Turbine meter", "Đồng hồ tuabin",
     "Rotor speed proportional to velocity.",
     "Tốc độ rôto tỷ lệ với vận tốc.",
     "±0.25–0.5 % of reading", "Clean liquids, hydrocarbon transfer.", "Chất lỏng sạch, chuyển nhượng hydrocarbon.",
     "Bearing wear; viscosity sensitivity.", "Mòn ổ trục; nhạy với độ nhớt."),
    ("flow", "Thermal mass meter", "Đồng hồ khối lượng nhiệt",
     "Heat carried away from a heated element by the gas.",
     "Nhiệt lấy đi từ phần tử đốt nóng bởi dòng khí.",
     "±1–2 % FS", "Combustion air, low gas flows, compressed air.", "Khí cháy, lưu lượng khí thấp, khí nén.",
     "Depends on gas composition and specific heat.", "Phụ thuộc thành phần khí và nhiệt dung riêng."),

    ("level", "DP / hydrostatic", "Áp vi sai / thủy tĩnh",
     "ρgh across a fixed height.",
     "ρgh trên một chiều cao xác định.",
     "±0.1–0.5 % of span", "Closed tanks, clean liquids, interface with a second tap.", "Bình kín, chất lỏng sạch, mặt phân cách với điểm đo thứ hai.",
     "Density change reads as level change; wet reference leg.", "Thay đổi khối lượng riêng bị đọc thành thay đổi mức; nhánh tham chiếu ướt."),
    ("level", "Radar (FMCW)", "Radar (FMCW)",
     "Frequency-modulated sweep; distance from the echo delay.",
     "Quét điều tần; khoảng cách từ độ trễ phản hồi.",
     "±3–10 mm", "Tanks, silos, solids, no contact with the product.", "Bồn, silo, vật rắn, không tiếp xúc sản phẩm.",
     "Foam, low dielectric constant, condensation on the antenna.", "Bọt, hằng số điện môi thấp, ngưng tụ trên anten."),
    ("level", "Guided wave radar (TDR)", "Radar sóng dẫn (TDR)",
     "Pulse reflection along a probe; time of flight gives level.",
     "Phản hồi xung dọc que dò; thời gian truyền cho ra mức.",
     "±3–10 mm", "Interface measurement, small tanks, stilling wells.", "Đo mặt phân cách, bồn nhỏ, giếng tiêu năng.",
     "Build-up on the probe; probe length limits range.", "Bám cặn trên que dò; chiều dài que giới hạn dải đo."),
    ("level", "Ultrasonic", "Siêu âm",
     "Echo time from the liquid surface to the transducer.",
     "Thời gian phản hồi từ mặt chất lỏng đến đầu dò.",
     "±0.25 % FS", "Water, sumps, open channels.", "Nước, hố thu, kênh hở.",
     "Foam, vapour, temperature gradients in the vapour space.", "Bọt, hơi, gradient nhiệt trong khoảng không phía trên."),
    ("level", "Capacitance", "Điện dung",
     "Dielectric change between probe and wall.",
     "Thay đổi hằng số điện môi giữa que dò và thành bồn.",
     "±1 % FS", "Small tanks, interface, aggressive liquids with the right coating.", "Bồn nhỏ, mặt phân cách, chất lỏng ăn mòn với lớp phủ phù hợp.",
     "Coating mimics a full tank; needs re-calibration on product change.", "Lớp bám giả như bồn đầy; cần hiệu chuẩn lại khi đổi sản phẩm."),
    ("level", "Load cell / weigh system", "Cảm biến tải / cân",
     "Total weight of vessel and contents by force.",
     "Tổng khối lượng bình và chất chứa bằng phép đo lực.",
     "±0.05 % FS", "Silos, hoppers, reactors where mass is the real variable.", "Silo, phễu, thiết bị phản ứng nơi khối lượng là biến thật.",
     "Piping and structure binding; thermal expansion.", "Đường ống và kết cấu gây kẹt; giãn nở nhiệt."),

    ("analytical", "pH / ORP", "pH / ORP",
     "Potential of a glass electrode against a reference.",
     "Điện thế điện cực thủy tinh so với điện cực so sánh.",
     "±0.02 pH", "Water treatment, chemical reaction, effluent.", "Xử lý nước, phản ứng hóa học, nước thải.",
     "Reference poisoning, fouling, calibration drift within days.", "Nhiễm độc điện cực so sánh, bám cặn, trôi hiệu chuẩn trong vài ngày."),
    ("analytical", "Conductivity", "Độ dẫn điện",
     "Cell resistance between two electrodes, temperature-compensated.",
     "Điện trở tế bào giữa hai điện cực, có bù nhiệt độ.",
     "±1 % FS", "Demineralised water, CIP concentration, leak detection.", "Nước khử khoáng, nồng độ CIP, phát hiện rò rỉ.",
     "Polarisation at high concentration; temperature compensation error.", "Phân cực ở nồng độ cao; sai số bù nhiệt."),
    ("analytical", "Dissolved oxygen", "Oxy hòa tan",
     "Luminescent quenching or galvanic cell.",
     "Dập tắt huỳnh quang hoặc tế bào galvanic.",
     "±0.1 ppm", "Aeration control, aquaculture, boiler feedwater.", "Điều khiển sục khí, nuôi trồng thủy sản, nước cấp lò hơi.",
     "Membrane fouling; flow dependence.", "Bám cặn màng; phụ thuộc lưu lượng."),
    ("analytical", "Gas analyser (NDIR / paramagnetic)", "Máy phân tích khí (NDIR / thuận từ)",
     "Infrared absorption or oxygen paramagnetism.",
     "Hấp thụ hồng ngoại hoặc tính thuận từ của oxy.",
     "±1–2 % FS", "Combustion trim, emissions, safety interlocks.", "Hiệu chỉnh cháy, khí thải, khóa liên động an toàn.",
     "Cross-sensitivity; sample conditioning is half the system.", "Nhạy chéo; hệ tiền xử lý mẫu chiếm nửa hệ thống."),

    ("final", "Globe valve + pneumatic actuator", "Van cầu + cơ cấu khí nén",
     "Plug position throttles the seat; spring-return fails safe.",
     "Vị trí nút van tiết lưu qua đế; lò xo hồi về an toàn.",
     "±1 % with positioner", "Most throttling loops: flow, pressure, temperature.", "Hầu hết vòng tiết lưu: lưu lượng, áp suất, nhiệt độ.",
     "Cavitation and noise at high ΔP; stiction if oversized.", "Xâm thực và ồn khi ΔP lớn; ma sát tĩnh nếu chọn quá lớn."),
    ("final", "Segmented ball / V-notch", "Van bi phân đoạn / V-notch",
     "Rotary shear action with a characterised opening.",
     "Tác động cắt quay với tiết diện đặc trưng.",
     "±1 %", "Slurry, pulp, dirty service needing a straight path.", "Bùn, bột giấy, môi trường bẩn cần đường thẳng.",
     "Dead band from packing; torque rises with solids.", "Dải chết do đệm; mô-men tăng khi có hạt rắn."),
    ("final", "Butterfly valve", "Van bướm",
     "Rotating disc in the bore.",
     "Đĩa quay trong lòng van.",
     "±2 %", "Large lines, low cost, on/off with occasional throttling.", "Tuyến lớn, chi phí thấp, đóng/mở và đôi khi tiết lưu.",
     "Cavitation and disc erosion; poor authority near closed.", "Xâm thực và mòn đĩa; độ phân giải kém gần vị trí đóng."),
    ("final", "Variable frequency drive", "Biến tần",
     "Motor speed controls pump or fan output by the affinity laws.",
     "Tốc độ động cơ điều khiển bơm/quạt theo định luật đồng dạng.",
     "±0.5 %", "Energy saving on pumps and fans; soft start.", "Tiết kiệm năng lượng bơm quạt; khởi động êm.",
     "Harmonics, low-speed torque, bearing currents.", "Sóng hài, mô-men ở tốc độ thấp, dòng ổ trục."),
    ("final", "Solenoid valve", "Van điện từ",
     "Coil moves a plunger — two states only.",
     "Cuộn dây dịch chuyển pittông — chỉ hai trạng thái.",
     "n/a (on/off)", "Shutdown, pilots, sequence logic.", "Cắt an toàn, van mồi, logic trình tự.",
     "No throttling; coil burnout if continuously energised.", "Không tiết lưu được; cháy cuộn nếu cấp điện liên tục."),
]


def build_instruments():
    pg = Page(
        "instruments.html",
        "ins",
        "Instrument reference — pressure, temperature, flow, level, analytical | I&amp;C",
        "Danh mục thiết bị — áp suất, nhiệt độ, lưu lượng, mức, phân tích | I&amp;C",
        "A filterable reference of process instruments: measurement principle, typical accuracy, "
        "best application and the characteristic failure mode for each.",
        "Danh mục thiết bị đo có bộ lọc: nguyên lý đo, độ chính xác điển hình, ứng dụng tốt nhất và "
        "kiểu hư hỏng đặc trưng.",
    )

    rows_html = []
    for (fam, n_en, n_vi, p_en, p_vi, acc, b_en, b_vi, w_en, w_vi) in ROWS:
        rows_html.append(
            '<tr data-fam="%s" data-s="%s %s">'
            "<td><strong>%s</strong></td><td>%s</td><td><code>%s</code></td><td>%s</td><td>%s</td></tr>"
            % (
                fam,
                (n_en + " " + p_en + " " + b_en + " " + w_en).lower(),
                (n_vi + " " + p_vi + " " + b_vi + " " + w_vi).lower(),
                pg.span(n_en, n_vi),
                pg.span(p_en, p_vi),
                acc,
                pg.span(b_en, b_vi),
                pg.span(w_en, w_vi),
            )
        )
    rows_html = "\n    ".join(rows_html)
    pg.strings["ins.ph"] = {"en": "Search instruments…", "vi": "Tìm thiết bị…"}

    body = page_intro(
        pg,
        "The instrument reference",
        "Danh mục thiết bị đo",
        "Thirty-one devices, five families, one table. Filter by family or search for a term in either "
        "language. Accuracy figures are typical order-of-magnitude values for a competent industrial "
        "device — always take the vendor datasheet for design.",
        "Ba mươi mốt thiết bị, năm họ, một bảng. Lọc theo họ hoặc tìm một thuật ngữ bằng cả hai ngôn ngữ. "
        "Các giá trị độ chính xác là mức điển hình cho một thiết bị công nghiệp tốt — luôn dùng "
        "datasheet nhà sản xuất khi thiết kế.",
        [("table", "The reference table", "Bảng tra thiết bị"),
         ("select", "Selection logic", "Logic chọn thiết bị")],
    )

    body += """
<section class="sec" id="table" style="padding-top:36px;border-top:0">
  <div class="wrap">
    <div class="pills">
      <button class="pill on" data-fam="all">%s</button>
      <button class="pill" data-fam="pressure">%s</button>
      <button class="pill" data-fam="temperature">%s</button>
      <button class="pill" data-fam="flow">%s</button>
      <button class="pill" data-fam="level">%s</button>
      <button class="pill" data-fam="analytical">%s</button>
      <button class="pill" data-fam="final">%s</button>
    </div>
    <div class="searchbar">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>
      <input id="inst-search" type="search" placeholder="Search instruments…" data-i18n-attr="placeholder" data-i18n="ins.ph">
      <span class="count" id="inst-count"></span>
    </div>
    <div class="tbl-wrap" id="inst-table">
      <table class="tbl">
        <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
        <tbody>
    %s
        </tbody>
      </table>
    </div>
  </div>
</section>
""" % (
        pg.span("All", "Tất cả"),
        pg.span("Pressure", "Áp suất"),
        pg.span("Temperature", "Nhiệt độ"),
        pg.span("Flow", "Lưu lượng"),
        pg.span("Level", "Mức"),
        pg.span("Analytical", "Phân tích"),
        pg.span("Final elements", "Phần tử chấp hành"),
        pg.th("Instrument", "Thiết bị"),
        pg.th("Principle", "Nguyên lý"),
        pg.th("Accuracy", "Độ chính xác"),
        pg.th("Best for", "Phù hợp nhất"),
        pg.th("Watch out", "Lưu ý"),
        rows_html,
    )

    body += section_open("01", "Selection logic", "Logic chọn thiết bị", pg, "select")
    body += """
<div class="grid c3">
  <div class="card">
    <span class="n">01</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <span class="n">02</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <span class="n">03</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <span class="n">04</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <span class="n">05</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
  <div class="card">
    <span class="n">06</span>
    <h3>%s</h3>
    <p>%s</p>
  </div>
</div>
<div class="note mt24">
  <span class="lbl">%s</span>
  %s
</div>
<div class="nextprev">
  <a href="fundamentals.html"><span class="k">%s</span>%s</a>
  <a href="control.html" style="text-align:right"><span class="k">%s</span>%s</a>
</div>
""" % (
        pg.h3("Start from the variable", "Bắt đầu từ biến đo"),
        pg.p(
            "Range, normal operating point and required resolution come first. A meter specified on "
            "line size rather than flow range is the most common expensive mistake.",
            "Dải đo, điểm làm việc bình thường và độ phân giải cần thiết phải đến trước. Chọn đồng hồ "
            "theo cỡ ống thay vì theo dải lưu lượng là lỗi tốn kém phổ biến nhất.",
        ),
        pg.h3("Then the fluid", "Rồi đến chất lỏng/khí"),
        pg.p(
            "Conductivity, viscosity, solids, entrained gas, corrosivity and temperature decide which "
            "principles are even possible before accuracy is discussed.",
            "Độ dẫn, độ nhớt, hạt rắn, bọt khí, tính ăn mòn và nhiệt độ quyết định nguyên lý nào còn khả "
            "thi trước khi bàn đến độ chính xác.",
        ),
        pg.h3("Then the environment", "Rồi đến môi trường"),
        pg.p(
            "Hazardous area classification, ambient temperature, vibration, washdown and access for "
            "calibration. A brilliant instrument you cannot reach is a liability.",
            "Phân vùng nguy hiểm, nhiệt độ môi trường, rung, rửa trôi và khả năng tiếp cận để hiệu chuẩn. "
            "Một thiết bị tuyệt vời nhưng không thể tiếp cận là một gánh nặng.",
        ),
        pg.h3("Then turndown", "Rồi đến tỷ số điều chỉnh"),
        pg.p(
            "Check accuracy at the minimum flow you actually need, not at full scale. Orifice turndown is "
            "3:1–5:1; Coriolis can be 100:1; that difference is often the whole business case.",
            "Kiểm tra độ chính xác tại lưu lượng nhỏ nhất thực sự cần, không phải tại thang đầy. Lỗ khoan "
            "có tỷ số 3:1–5:1; Coriolis có thể 100:1; khác biệt đó thường là toàn bộ bài toán kinh tế.",
        ),
        pg.h3("Then the loop it sits in", "Rồi đến vòng điều khiển chứa nó"),
        pg.p(
            "A control loop needs speed and repeatability more than absolute accuracy. A custody "
            "measurement needs the opposite. The same fluid can justify two different devices.",
            "Vòng điều khiển cần tốc độ và độ lặp lại hơn là độ chính xác tuyệt đối. Đo giao nhận cần "
            "điều ngược lại. Cùng một chất lỏng có thể biện minh cho hai thiết bị khác nhau.",
        ),
        pg.h3("Finally the lifecycle", "Cuối cùng là vòng đời"),
        pg.p(
            "Calibration interval, spare parts, local service and whether the diagnostics are readable "
            "by the people who will actually maintain it.",
            "Chu kỳ hiệu chuẩn, phụ tùng, dịch vụ tại chỗ và liệu chẩn đoán có đọc được bởi chính những "
            "người sẽ bảo trì thiết bị.",
        ),
        pg.span("A note on accuracy claims", "Ghi chú về công bố độ chính xác"),
        pg.p(
            "Vendors quote the best number under reference conditions. Compare like with like: % of span "
            "against % of reading, at the same ambient temperature, with the same turndown. A 0.05&nbsp;% "
            "claim at 10:1 turndown is a different device from a 0.05&nbsp;% claim at 1:1.",
            "Nhà sản xuất công bố con số tốt nhất trong điều kiện chuẩn. Hãy so sánh cùng loại: % dải đo "
            "với % giá trị đọc, cùng nhiệt độ môi trường, cùng tỷ số điều chỉnh. Một công bố 0,05&nbsp;% "
            "ở tỷ số 10:1 là thiết bị khác với công bố 0,05&nbsp;% ở 1:1.",
        ),
        pg.span("Back", "Quay lại"),
        pg.span("Fundamentals", "Kiến thức cơ bản"),
        pg.span("Next", "Tiếp"),
        pg.span("Control &amp; tuning", "Điều khiển &amp; hiệu chỉnh"),
    )
    body += section_close()

    write("instruments.html", render(pg, body, "instruments.html"))
