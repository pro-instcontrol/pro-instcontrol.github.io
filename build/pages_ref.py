# -*- coding: utf-8 -*-
"""Geotechnical monitoring + standards index."""

from framework import Page, section_open, section_close, write, render, page_intro

ISO_ROWS = [
    ("1", "2015", "General rules", "Quy tắc chung",
     "The framework: objectives, uncertainty, reporting, and how the other parts fit together.",
     "Khung chung: mục tiêu, độ bất định, báo cáo, và cách các phần khác liên kết."),
    ("2", "2016", "Displacements along a line: extensometers", "Chuyển vị dọc một tuyến: extensometer",
     "Settlement or heave measured along an axis, resolved by combining with Part 3.",
     "Lún hoặc trồi đo dọc một trục, xác định đầy đủ khi kết hợp với Phần 3."),
    ("3", "2017", "Displacements across a line: inclinometers", "Chuyển vị ngang tuyến: đầu đo nghiêng",
     "Lateral displacement profile with depth — the standard tool for slope and wall movement.",
     "Profil chuyển vị ngang theo chiều sâu — công cụ chuẩn cho mái dốc và tường chắn."),
    ("4", "2020", "Pore water pressure: piezometers", "Áp lực nước lỗ rỗng: piezometer",
     "Measurement of u, the variable that governs effective stress and therefore strength.",
     "Đo u, biến quyết định ứng suất hiệu quả và do đó quyết định sức kháng."),
    ("5", "2019", "Stress change: total pressure cells", "Thay đổi ứng suất: cảm biến áp tổng",
     "Total stress against a structure or in fill; combined with Part 4 gives effective stress.",
     "Ứng suất tổng lên kết cấu hoặc trong đất đắp; kết hợp Phần 4 cho ứng suất hiệu quả."),
    ("6", "draft", "Settlement: hydraulic settlement systems", "Lún: hệ thống lún thủy lực",
     "Settlement of large fills and structures where direct access is impossible.",
     "Lún của nền đắp lớn và kết cấu nơi không thể tiếp cận trực tiếp."),
    ("7", "2025", "Strain: strain gauges", "Biến dạng: tenxơmet",
     "Strain in structural members, rock bolts and concrete.",
     "Biến dạng trong cấu kiện kết cấu, neo đá và bê tông."),
    ("8", "2023", "Loads: load cells", "Tải trọng: cảm biến lực",
     "Anchor, strut and cable loads measured directly as force.",
     "Tải neo, thanh chống và cáp đo trực tiếp dưới dạng lực."),
]

GT_ROWS = [
    ("Vibrating wire piezometer", "Piezometer dây rung",
     "Tensioned steel wire; pressure changes its natural frequency.",
     "Dây thép căng; áp suất làm thay đổi tần số dao động riêng.",
     "±0.1 % FS", "Pore pressure in dams, embankments, retaining walls.",
     "Áp lực nước lỗ rỗng trong đập, nền đắp, tường chắn.",
     "Lightning and cable damage; temperature correction needed.",
     "Sét và hỏng cáp; cần hiệu chỉnh nhiệt độ."),
    ("Standpipe piezometer", "Piezometer ống đứng",
     "Water level in a tube read with a dip meter.",
     "Mực nước trong ống đọc bằng đầu dò hạ mực.",
     "±10 mm", "Simple, verifiable, long-term installations.",
     "Đơn giản, kiểm chứng được, lắp đặt dài hạn.",
     "Slow response in low-permeability soil; manual reading.",
     "Đáp ứng chậm trong đất ít thấm; đọc thủ công."),
    ("In-place inclinometer", "Đầu đo nghiêng cố định",
     "Chain of tilt sensors grouted in a casing.",
     "Chuỗi cảm biến nghiêng chèn vữa trong ống.",
     "±0.02 mm/m", "Real-time lateral movement, automatic alarms.",
     "Chuyển vị ngang thời gian thực, cảnh báo tự động.",
     "Cost per borehole; alignment and zero reference.",
     "Chi phí mỗi lỗ khoan; căn chỉnh và mốc zero."),
    ("Inclinometer probe", "Đầu đo nghiêng di động",
     "Servo-accelerometer traversed down a grooved casing.",
     "Gia tốc kế servo kéo dọc ống có rãnh.",
     "±2 mm / 25 m", "Periodic profiles; the baseline method.",
     "Profil định kỳ; phương pháp cơ bản.",
     "Labour-intensive; casing deviation; access.",
     "Tốn nhân công; ống bị lệch; khó tiếp cận."),
    ("Magnetic extensometer", "Extensometer nam châm",
     "Magnet rings along a borehole, located by a reed switch probe.",
     "Vòng nam châm dọc lỗ khoan, định vị bằng đầu dò tiếp điểm từ.",
     "±1 mm", "Settlement and heave with depth in fill and soft ground.",
     "Lún và trồi theo chiều sâu trong đất đắp và đất yếu.",
     "Magnets can slip; reference head settlement.",
     "Nam châm có thể trượt; mốc chuẩn bị lún."),
    ("Rod extensometer / MPBX", "Extensometer thanh / MPBX",
     "Rods anchored at several depths, read at the collar.",
     "Các thanh neo ở nhiều độ sâu, đọc tại miệng lỗ.",
     "±0.05 mm", "Tunnel convergence, rock displacement, precise short spans.",
     "Hội tụ hầm, chuyển vị đá, nhịp ngắn cần chính xác.",
     "Installation skill; rod buckling; limited depth.",
     "Tay nghề lắp đặt; thanh bị oằn; giới hạn chiều sâu."),
    ("Total pressure cell", "Cảm biến áp tổng",
     "Flat cell measuring total stress at a soil–structure interface.",
     "Tấm phẳng đo ứng suất tổng tại mặt tiếp xúc đất–kết cấu.",
     "±0.5 % FS", "Stress on tunnel linings, retaining walls, dam cores.",
     "Ứng suất lên vỏ hầm, tường chắn, lõi đập.",
     "Arching and placement disturb the stress field.",
     "Hiệu ứng vòm và cách đặt làm nhiễu trường ứng suất."),
    ("Load cell", "Cảm biến lực",
     "Strain-gauged or vibrating-wire body in series with the load path.",
     "Thân đo biến dạng hoặc dây rung nối tiếp trong đường truyền lực.",
     "±0.1 % FS", "Anchor loads, strut loads, tieback testing.",
     "Tải neo, tải thanh chống, thí nghiệm neo.",
     "Eccentric loading; temperature; calibration in situ is hard.",
     "Tải lệch tâm; nhiệt độ; hiệu chuẩn tại chỗ khó."),
    ("Crack meter", "Đầu đo khe nứt",
     "LVDT or vibrating wire across a joint.",
     "LVDT hoặc dây rung bắc qua khe.",
     "±0.02 mm", "Joints, cracks, contact grouting.",
     "Khe nối, vết nứt, chèn vữa tiếp xúc.",
     "Mounting stiffness; thermal movement of the structure.",
     "Độ cứng mối gắn; chuyển vị nhiệt của kết cấu."),
    ("Tiltmeter", "Đầu đo nghiêng bề mặt",
     "MEMS or servo pendulum measuring rotation.",
     "MEMS hoặc con lắc servo đo góc quay.",
     "±0.001°", "Rotation of walls, towers, machinery foundations.",
     "Góc quay của tường, tháp, nền máy.",
     "Drift; mounting plane must be real.",
     "Trôi; mặt gắn phải đúng thực tế."),
    ("Robotic total station", "Máy toàn đạc tự động",
     "Angle and distance to prisms, measured on a schedule.",
     "Đo góc và khoảng cách tới gương, theo lịch.",
     "±1 mm + 1 ppm", "Surface displacement over large areas, automatic.",
     "Chuyển vị bề mặt trên diện rộng, tự động.",
     "Sight lines, refraction, prism damage.",
     "Tia ngắm, khúc xạ, gương bị hỏng."),
    ("InSAR", "InSAR",
     "Radar interferometry between satellite passes.",
     "Giao thoa radar giữa các lần vệ tinh bay qua.",
     "±5 mm / yr", "Regional screening where no ground access exists.",
     "Sàng lọc vùng rộng nơi không thể tiếp cận.",
     "Vegetation, geometry, only line-of-sight displacement.",
     "Thực vật, hình học, chỉ đo được chuyển vị theo tia nhìn."),
]

STD = [
    ("ISA", "ANSI/ISA-5.1-2022", "Instrumentation symbols and identification",
     "Instrumentation symbols and identification", "Tag numbers, line symbols, loop identification on a P&amp;ID.",
     "Ký hiệu và nhận dạng thiết bị đo trên P&amp;ID."),
    ("ISA", "ANSI/ISA-101.01-2015", "Human-machine interfaces for process automation",
     "Giao diện người–máy cho tự động hóa quá trình", "HMI design, hierarchy, situational awareness.",
     "Thiết kế HMI, phân cấp, nhận thức tình huống."),
    ("ISA", "ANSI/ISA-18.2-2016", "Management of alarm systems",
     "Quản lý hệ thống cảnh báo", "Alarm rationalisation, KPIs, shelving, flood suppression.",
     "Hợp lý hóa cảnh báo, KPI, tạm ẩn, chống ngập cảnh báo."),
    ("ISA", "ANSI/ISA-88 / ISA-95", "Batch control / enterprise-control integration",
     "Điều khiển mẻ / tích hợp doanh nghiệp–điều khiển", "Recipe models; the level 0–4 architecture.",
     "Mô hình công thức; kiến trúc mức 0–4."),
    ("IEC", "IEC 61131-3", "Programmable controller languages",
     "Ngôn ngữ bộ điều khiển khả trình", "LD, FBD, ST, IL, SFC — the languages every PLC implements.",
     "LD, FBD, ST, IL, SFC — ngôn ngữ mọi PLC đều có."),
    ("IEC", "IEC 61508 / 61511", "Functional safety, and SIS for the process industry",
     "An toàn chức năng và SIS cho công nghiệp quá trình", "SIL determination, lifecycle, proof testing.",
     "Xác định SIL, vòng đời, kiểm chứng định kỳ."),
    ("IEC", "IEC 60079 / 60529", "Explosive atmospheres / ingress protection",
     "Khí quyển nổ / cấp bảo vệ", "Zone classification, Ex protection concepts, IP codes.",
     "Phân vùng, khái niệm bảo vệ Ex, mã IP."),
    ("IEC", "IEC 60751 / 60584", "Platinum resistance thermometers / thermocouples",
     "Nhiệt kế điện trở bạch kim / cặp nhiệt điện", "Tolerances classes, emf tables, colour codes.",
     "Cấp dung sai, bảng suất điện động, mã màu."),
    ("API", "API RP 551", "Process measurement instrumentation",
     "Thiết bị đo quá trình", "Installation practice for the common measuring instruments (2nd ed. 2016).",
     "Thực hành lắp đặt các thiết bị đo thông dụng (bản 2, 2016)."),
    ("API", "API RP 552 / 553 / 554 / 555", "Transmission systems / valves / I&amp;C / analysers",
     "Hệ truyền tín hiệu / van / I&amp;C / máy phân tích", "The four-part refinery instrumentation set.",
     "Bộ bốn tiêu chuẩn thiết bị đo cho nhà máy lọc dầu."),
    ("API", "API RP 2350", "Overfill prevention for storage tanks",
     "Chống tràn bồn chứa", "Independent high-high level protection and proof testing.",
     "Bảo vệ mức cao-cao độc lập và kiểm chứng định kỳ."),
    ("ISO", "ISO 5167", "Flow by pressure differential devices",
     "Lưu lượng bằng thiết bị chênh áp", "Orifice, nozzle and venturi geometry and discharge coefficients.",
     "Hình học và hệ số lưu lượng lỗ khoan, nozzle, venturi."),
    ("ISO", "ISO 18674-1 to -8", "Geotechnical monitoring by field instrumentation",
     "Quan trắc địa kỹ thuật bằng thiết bị hiện trường", "The monitoring series: general rules, displacement, pore pressure, stress, load, strain.",
     "Bộ tiêu chuẩn quan trắc: quy tắc chung, chuyển vị, áp lực nước, ứng suất, tải, biến dạng."),
    ("CEN", "EN 1997-1 §2.7", "Eurocode 7 — the observational method",
     "Eurocode 7 — phương pháp quan trắc", "Requires acceptable limits, predictions, monitoring and a pre-planned response.",
     "Yêu cầu giới hạn chấp nhận, dự báo, quan trắc và phản ứng định trước."),
    ("ISO", "ISO 22475-1 / 22476 / 22477", "Sampling, in-situ testing, testing of structures",
     "Lấy mẫu, thí nghiệm tại chỗ, thí nghiệm kết cấu", "The investigation standards that precede instrumentation.",
     "Các tiêu chuẩn khảo sát đi trước công tác quan trắc."),
    ("NAMUR", "NE 43 / NE 107", "Signal level for fault information / self-monitoring",
     "Mức tín hiệu báo lỗi / tự chẩn đoán", "3.6–21.0 mA fault band; diagnostic classification.",
     "Dải báo lỗi 3,6–21,0 mA; phân loại chẩn đoán."),
]


def build_geotechnical():
    pg = Page(
        "geotechnical.html",
        "geo",
        "Geotechnical monitoring — instruments, ISO 18674, field reality",
        "Quan trắc địa kỹ thuật — thiết bị, ISO 18674, thực tế hiện trường",
        "How geotechnical instrumentation works: vibrating wire sensors, piezometers, inclinometers, "
        "extensometers, load cells, the ISO 18674 series, and why the loop stays open.",
        "Cách thiết bị địa kỹ thuật hoạt động: cảm biến dây rung, piezometer, đầu đo nghiêng, "
        "extensometer, cảm biến lực, bộ ISO 18674, và vì sao vòng điều khiển để hở.",
    )

    body = page_intro(
        pg,
        "Measuring the ground without moving it",
        "Đo đất mà không làm nó dịch chuyển",
        "Geotechnical instrumentation answers a different question from process instrumentation. Not "
        "&ldquo;what is the value now?&rdquo; but &ldquo;is this structure behaving as we predicted?&rdquo; "
        "— a question with a baseline, a rate, and a consequence.",
        "Thiết bị địa kỹ thuật trả lời một câu hỏi khác với thiết bị đo quá trình. Không phải "
        "&ldquo;giá trị bây giờ là bao nhiêu?&rdquo; mà &ldquo;kết cấu này có đang hành xử như dự "
        "báo không?&rdquo; — một câu hỏi có mốc chuẩn, có tốc độ, và có hậu quả.",
        [
            ("why", "Why monitor", "Vì sao quan trắc"),
            ("iso", "The ISO 18674 series", "Bộ ISO 18674"),
            ("sensors", "Sensor families", "Các họ cảm biến"),
            ("vw", "Why vibrating wire", "Vì sao dây rung"),
            ("field", "Field reality", "Thực tế hiện trường"),
        ],
    )

    # 01 why
    body += section_open("01", "Why monitor", "Vì sao quan trắc", pg, "why")
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
    </div>
  </div>
</div>
""" % (
        pg.h2("The observational method, in four requirements", "Phương pháp quan trắc, bốn yêu cầu"),
        pg.p(
            "EN 1997-1 §2.7 allows a design to be adjusted during construction, but only if four things "
            "exist before work starts: acceptable limits of behaviour, a prediction of what will happen, "
            "a monitoring programme that can detect the difference, and a response prepared in advance "
            "for when it does.",
            "EN 1997-1 §2.7 cho phép điều chỉnh thiết kế trong quá trình thi công, nhưng chỉ khi có đủ "
            "bốn thứ trước khi khởi công: giới hạn hành vi chấp nhận được, dự báo điều sẽ xảy ra, một "
            "chương trình quan trắc đủ phát hiện khác biệt, và phản ứng chuẩn bị trước cho khi khác biệt "
            "xuất hiện.",
        ),
        pg.p(
            "Notice what is missing from that list: instruments are the third item. The first two are "
            "engineering judgement, and the fourth is a management decision. A monitoring system without "
            "a threshold and a response is data collection, not risk management.",
            "Hãy để ý điều gì không có trong danh sách: thiết bị là mục thứ ba. Hai mục đầu là phán đoán "
            "kỹ thuật, mục thứ tư là quyết định quản lý. Một hệ quan trắc không có ngưỡng và phản ứng chỉ "
            "là thu thập dữ liệu, không phải quản lý rủi ro.",
        ),
        pg.span("The rule that matters", "Quy tắc quan trọng"),
        pg.p(
            "Rate of change catches failure earlier than absolute value. A wall moving 2 mm/month is a "
            "different object from a wall that moved 2 mm and stopped — even though both read 2 mm.",
            "Tốc độ thay đổi phát hiện hư hỏng sớm hơn giá trị tuyệt đối. Một bức tường dịch 2 mm/tháng "
            "là đối tượng khác với bức tường đã dịch 2 mm rồi dừng lại — dù cả hai cùng đọc 2 mm.",
        ),
        pg.p(
            "This is why every serious monitoring programme reports velocity as well as displacement, and "
            "why the trigger values are usually written as both a magnitude and a rate.",
            "Đó là lý do mọi chương trình quan trắc nghiêm túc đều báo cáo cả vận tốc và chuyển vị, và vì "
            "sao các giá trị kích hoạt thường được viết dưới cả dạng độ lớn và tốc độ.",
            "small dim",
        ),
        pg.span("Four requirements", "Bốn yêu cầu"),
        pg.h3("What the standard asks", "Tiêu chuẩn yêu cầu gì"),
        pg.td("1. Limits", "1. Giới hạn"),
        pg.td("Acceptable limits of behaviour, agreed before construction.", "Giới hạn hành vi chấp nhận được, thống nhất trước thi công."),
        pg.td("2. Prediction", "2. Dự báo"),
        pg.td("A range of behaviour, from the design model.", "Một dải hành vi, từ mô hình thiết kế."),
        pg.td("3. Monitoring", "3. Quan trắc"),
        pg.td("A programme able to detect deviation from the prediction.", "Chương trình đủ phát hiện sai lệch so với dự báo."),
        pg.td("4. Response", "4. Phản ứng"),
        pg.td("A pre-planned action if the limits are approached.", "Hành động định trước nếu tiến gần giới hạn."),
    )
    body += section_close()

    # 02 ISO 18674
    body += section_open("02", "The ISO 18674 series", "Bộ tiêu chuẩn ISO 18674", pg, "iso")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("Eight parts, one vocabulary", "Tám phần, một từ vựng"),
        pg.p(
            "ISO/TC 182 is standardising geotechnical monitoring part by part. Knowing which part covers "
            "which quantity is the fastest way to read a foreign specification.",
            "ISO/TC 182 đang tiêu chuẩn hóa quan trắc địa kỹ thuật theo từng phần. Biết phần nào bao phủ "
            "đại lượng nào là cách nhanh nhất để đọc một bản chỉ định lạ.",
        ),
        pg.th("Part", "Phần"),
        pg.th("Year", "Năm"),
        pg.th("Quantity measured", "Đại lượng đo"),
        pg.th("What it covers", "Nội dung"),
    )
    for num, year, t_en, t_vi, d_en, d_vi in ISO_ROWS:
        body += "<tr><td><strong>%s</strong></td><td><code>%s</code></td><td>%s</td><td>%s</td></tr>" % (
            num, year, pg.span(t_en, t_vi), pg.span(d_en, d_vi)
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
        pg.span("Edition check", "Kiểm tra phiên bản"),
        pg.p(
            "Part 6 is still a draft at the time of writing and Part 7 was published in 2025 — always "
            "confirm the current edition before citing a part number in a specification.",
            "Phần 6 vẫn còn là dự thảo tại thời điểm viết và Phần 7 được công bố năm 2025 — luôn xác nhận "
            "bản hiện hành trước khi viện dẫn số phần trong một bản chỉ định.",
        ),
    )
    body += section_close()

    # 03 sensors
    body += section_open("03", "The sensor families", "Các họ cảm biến", pg, "sensors")
    body += """
<div class="sec-head">
  %s
  %s
</div>
<div class="tbl-wrap">
<table class="tbl">
  <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
  <tbody>
""" % (
        pg.h2("Twelve instruments that watch a structure", "Mười hai thiết bị canh một kết cấu"),
        pg.p(
            "The working set, from the ubiquitous vibrating-wire piezometer to satellite radar. "
            "Resolution figures are typical for a competent installation, not best-case laboratory values.",
            "Bộ thiết bị thực dụng, từ piezometer dây rung phổ biến đến radar vệ tinh. Các giá trị độ phân "
            "giải là mức điển hình cho một lắp đặt tốt, không phải giá trị tốt nhất trong phòng thí nghiệm.",
        ),
        pg.th("Instrument", "Thiết bị"),
        pg.th("Principle", "Nguyên lý"),
        pg.th("Resolution", "Độ phân giải"),
        pg.th("Best for", "Phù hợp nhất"),
        pg.th("Watch out", "Lưu ý"),
    )
    for n_en, n_vi, p_en, p_vi, acc, b_en, b_vi, w_en, w_vi in GT_ROWS:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td><code>%s</code></td><td>%s</td><td>%s</td></tr>" % (
            pg.span(n_en, n_vi), pg.span(p_en, p_vi), acc, pg.span(b_en, b_vi), pg.span(w_en, w_vi)
        )
    body += """
  </tbody>
</table>
</div>
""" % ()
    body += section_close()

    # 04 VW vs 4-20
    body += section_open("04", "Why vibrating wire", "Vì sao dây rung", pg, "vw")
    body += """
<div class="sec-head">
  %s
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
  </tbody>
</table>
</div>
<div class="note mt24">
  <span class="lbl">%s</span>
  %s
</div>
""" % (
        pg.h2("Frequency beats current when the cable is long", "Tần số thắng dòng điện khi cáp dài"),
        pg.p(
            "A vibrating-wire sensor outputs a frequency, not a voltage. Cable resistance, connector "
            "corrosion and junction resistance barely affect a frequency measurement — which is why the "
            "technology survives in boreholes where a 4–20 mA transmitter would drift within a year.",
            "Cảm biến dây rung xuất ra tần số, không phải điện áp. Điện trở cáp, ăn mòn đầu nối và điện "
            "trở mối nối hầu như không ảnh hưởng đến phép đo tần số — đó là lý do công nghệ này tồn tại "
            "trong các lỗ khoan, nơi một bộ truyền 4–20 mA sẽ trôi trong vòng một năm.",
        ),
        pg.p(
            "The cost is speed. The wire must be plucked and allowed to settle before the frequency can be "
            "counted, so a reading takes a second or more. That is fine for a slope and useless for a "
            "control loop.",
            "Cái giá là tốc độ. Dây phải được kích và chờ ổn định trước khi đếm được tần số, nên một lần "
            "đọc mất một giây hoặc hơn. Điều đó ổn với mái dốc và vô dụng với vòng điều khiển.",
        ),
        pg.th("Aspect", "Khía cạnh"),
        pg.th("Vibrating wire", "Dây rung"),
        pg.th("4–20 mA transmitter", "Bộ truyền 4–20 mA"),
        pg.span("Output", "Đầu ra"),
        pg.span("Frequency (Hz), squared to pressure", "Tần số (Hz), bình phương để ra áp suất"),
        pg.span("Current, linear with the variable", "Dòng điện, tuyến tính với biến đo"),
        pg.span("Cable length", "Chiều dài cáp"),
        pg.span("Kilometres, resistance does not matter", "Kilômét, điện trở không ảnh hưởng"),
        pg.span("Limited by loop supply voltage", "Giới hạn bởi điện áp cấp cho vòng"),
        pg.span("Reading speed", "Tốc độ đọc"),
        pg.span("About 1 s per channel", "Khoảng 1 giây mỗi kênh"),
        pg.span("Continuous, milliseconds", "Liên tục, mili giây"),
        pg.span("Power", "Nguồn"),
        pg.span("Very low; battery and solar viable", "Rất thấp; pin và mặt trời khả thi"),
        pg.span("Loop-powered, 24 V", "Cấp qua vòng, 24 V"),
        pg.span("Long-term stability", "Ổn định dài hạn"),
        pg.span("Excellent — the reason it is buried", "Rất tốt — lý do nó được chôn"),
        pg.span("Good, but needs recalibration access", "Tốt, nhưng cần tiếp cận để hiệu chuẩn"),
        pg.span("Diagnostics", "Chẩn đoán"),
        pg.span("Minimal; a failed wire reads zero or garbage", "Tối thiểu; dây hỏng đọc ra zero hoặc rác"),
        pg.span("Rich: NAMUR NE 107 status, HART variables", "Phong phú: trạng thái NAMUR NE 107, biến HART"),
        pg.span("The reading is Hz²", "Kết quả đọc là Hz²"),
        pg.p(
            "Most vibrating-wire sensors are calibrated as pressure or displacement against frequency "
            "squared, with a polynomial that includes a temperature term from the built-in thermistor. "
            "Skipping the temperature correction is the most common source of a slow, believable drift.",
            "Hầu hết cảm biến dây rung được hiệu chuẩn theo áp suất hoặc chuyển vị dựa trên bình phương "
            "tần số, với đa thức có số hạng nhiệt độ từ nhiệt điện trở tích hợp. Bỏ qua hiệu chỉnh nhiệt "
            "độ là nguồn phổ biến nhất của một độ trôi chậm và trông rất hợp lý.",
        ),
    )
    body += section_close()

    # 05 field reality
    body += section_open("05", "Field reality", "Thực tế hiện trường", pg, "field")
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
        pg.h2("Six ways a monitoring system fails", "Sáu cách hệ quan trắc thất bại"),
        pg.p(
            "Almost none of them are the sensor. In practice the failure is mechanical, electrical or "
            "procedural — and it usually happens quietly.",
            "Gần như không phải do cảm biến. Trong thực tế hư hỏng là cơ khí, điện hoặc quy trình — và "
            "thường xảy ra một cách âm thầm.",
        ),
        pg.h3("Lightning", "Sét"),
        pg.p(
            "A long cable in an open site is an antenna. One strike takes out the logger and every sensor "
            "on the segment. Surge protection and a single-point earth are not optional.",
            "Một tuyến cáp dài trên bãi trống là một anten. Một tia sét hạ logger và toàn bộ cảm biến "
            "trên segment. Chống sét lan truyền và nối đất một điểm không phải tùy chọn.",
        ),
        pg.h3("Grout and borehole quality", "Chất lượng vữa và lỗ khoan"),
        pg.p(
            "A piezometer surrounded by a poor grout seal measures the grout, not the ground. The error is "
            "systematic, stable, and invisible in the data.",
            "Một piezometer được bao bởi vữa bịt kém sẽ đo vữa, không phải đất. Sai số mang tính hệ thống, "
            "ổn định, và không nhìn thấy được trong dữ liệu.",
        ),
        pg.h3("Cable damage", "Hỏng cáp"),
        pg.p(
            "Excavators, rodents, UV and settlement. Route cables in conduit, leave slack loops at "
            "settlement joints, and record the route while it is still visible.",
            "Máy đào, gặm nhấm, tia UV và lún. Đi cáp trong ống, để vòng dự trữ tại khe lún, và ghi lại "
            "tuyến khi còn nhìn thấy được.",
        ),
        pg.h3("Reference instability", "Mốc chuẩn không ổn định"),
        pg.p(
            "Every relative measurement needs a fixed reference. If the reference head settles, the whole "
            "profile shifts and the movement looks real.",
            "Mọi phép đo tương đối cần một mốc cố định. Nếu đầu chuẩn bị lún, toàn bộ profil dịch chuyển "
            "và chuyển vị trông như thật.",
        ),
        pg.h3("Silent data loss", "Mất dữ liệu âm thầm"),
        pg.p(
            "A logger that stops reporting is obvious. A logger reporting the last value repeatedly is "
            "not. Add a heartbeat, a timestamp check and a rate-of-change sanity test.",
            "Logger ngừng gửi thì rõ ràng. Logger lặp lại giá trị cuối thì không. Hãy thêm tín hiệu nhịp "
            "tim, kiểm tra dấu thời gian và phép thử hợp lý theo tốc độ thay đổi.",
        ),
        pg.h3("Nobody reads it", "Không ai đọc"),
        pg.p(
            "The most common failure of all. If the dashboard has no named owner and no review cadence, "
            "the data is a cost, not a control.",
            "Kiểu hư hỏng phổ biến nhất. Nếu bảng điều khiển không có người phụ trách và không có nhịp "
            "xem xét, dữ liệu là chi phí, không phải biện pháp kiểm soát.",
        ),
    )
    body += section_close()

    write("geotechnical.html", render(pg, body, "geotechnical.html"))


def build_standards():
    pg = Page(
        "standards.html",
        "std",
        "Standards index — ISA, IEC, API, ISO 18674 | I&amp;C Field Guide",
        "Danh mục tiêu chuẩn — ISA, IEC, API, ISO 18674",
        "The standards that govern process instrumentation and control, and geotechnical monitoring, "
        "with what each one actually controls.",
        "Các tiêu chuẩn chi phối thiết bị đo và điều khiển quá trình, và quan trắc địa kỹ thuật, "
        "kèm nội dung thực sự của từng tiêu chuẩn.",
    )

    body = """
<section class="sec" style="padding-top:56px">
  <div class="wrap">
    <div class="sec-head">
      %s
      %s
    </div>
    <div class="tbl-wrap">
      <table class="tbl">
        <thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>
        <tbody>
""" % (
        pg.h1("The standards that actually decide things", "Những tiêu chuẩn thực sự quyết định"),
        pg.p(
            "Not an exhaustive list — the ones that change a drawing, a tag number, a test or a sign-off. "
            "Editions move; confirm the current one before you cite it in a specification.",
            "Không phải danh sách đầy đủ — chỉ những tiêu chuẩn làm thay đổi một bản vẽ, một số thẻ, một "
            "phép thử hoặc một biên bản nghiệm thu. Các bản tiêu chuẩn luôn cập nhật; hãy xác nhận bản "
            "hiện hành trước khi viện dẫn trong chỉ định.",
            "lede wide",
        ),
        pg.th("Body", "Tổ chức"),
        pg.th("Standard", "Tiêu chuẩn"),
        pg.th("Title", "Tên"),
        pg.th("What it governs", "Nội dung chi phối"),
    )
    for body_, num, t_en, t_vi, d_en, d_vi in STD:
        body += "<tr><td><code>%s</code></td><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>" % (
            body_, num, pg.span(t_en, t_vi), pg.span(d_en, d_vi)
        )
    body += """
        </tbody>
      </table>
    </div>
    <div class="note mt24">
      <span class="lbl">%s</span>
      %s
    </div>
    <div class="nextprev">
      <a href="geotechnical.html"><span class="k">%s</span>%s</a>
      <a href="glossary.html" style="text-align:right"><span class="k">%s</span>%s</a>
    </div>
  </div>
</section>
""" % (
        pg.span("Reading order", "Thứ tự đọc"),
        pg.p(
            "Start with ISA-5.1 if you have to draw or read a P&amp;ID; IEC 61131-3 if you have to program; "
            "IEC 61511 if anything you touch can hurt someone; API RP 551 if you have to install it; "
            "ISO 18674-1 if you have to watch a structure.",
            "Bắt đầu với ISA-5.1 nếu bạn phải vẽ hoặc đọc P&amp;ID; IEC 61131-3 nếu bạn phải lập trình; "
            "IEC 61511 nếu bất cứ thứ gì bạn chạm vào có thể gây thương tích; API RP 551 nếu bạn phải "
            "lắp đặt; ISO 18674-1 nếu bạn phải quan trắc một kết cấu.",
        ),
        pg.span("Back", "Quay lại"),
        pg.span("Geotechnical monitoring", "Quan trắc địa kỹ thuật"),
        pg.span("Next", "Tiếp"),
        pg.span("Glossary", "Thuật ngữ"),
    )

    write("standards.html", render(pg, body, "standards.html"))
