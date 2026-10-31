# -*- coding: utf-8 -*-
"""Process — what a process is, the three sectors of an economy, and the
control / instrumentation / IT-OT / AI stack that runs the secondary sector.

Bilingual (EN / VI), matching the site's paired-string convention. The page is
an orientation layer: it frames the rest of the field guide (Fundamentals,
Control, Applications, Safety) in the wider economy.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import (Page, section_open, section_close, write, render,
                       page_intro, bullets)

# ---------------------------------------------------------------------------
# Two inline diagrams (English labels; illustrative, not translatable text).
# ---------------------------------------------------------------------------

VALUECHAIN_SVG = """
<svg viewBox="0 0 680 250" role="img" aria-label="From ore to product">
  <defs>
    <marker id="ar" markerWidth="9" markerHeight="9" refX="6" refY="3"
            orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L6,3 L0,6 Z" fill="#0a5f56"/>
    </marker>
  </defs>
  <!-- Primary band -->
  <rect x="0" y="14" width="680" height="34" rx="8" fill="#eef3f8"/>
  <text x="14" y="36" font-size="13" font-weight="600" fill="#0a5f56">PRIMARY &#183; extract &amp; harvest</text>
  <text x="430" y="36" font-size="12" fill="#66788d">ore &#183; crude oil &#183; crops &#183; timber</text>
  <!-- conversion chain -->
  <g font-size="11.5" font-family="Inter, sans-serif">
    <rect x="14"  y="74" width="116" height="58" rx="9" fill="#fff" stroke="#ccd7e3"/>
    <text x="72"  y="100" text-anchor="middle" font-weight="600" fill="#0b1725">Mine &amp; crush</text>
    <text x="72"  y="118" text-anchor="middle" fill="#66788d">concentrate</text>

    <rect x="162" y="74" width="116" height="58" rx="9" fill="#fff" stroke="#ccd7e3"/>
    <text x="220" y="100" text-anchor="middle" font-weight="600" fill="#0b1725">Smelt / refine</text>
    <text x="220" y="118" text-anchor="middle" fill="#66788d">primary metal</text>

    <rect x="310" y="74" width="116" height="58" rx="9" fill="#fff" stroke="#ccd7e3"/>
    <text x="368" y="100" text-anchor="middle" font-weight="600" fill="#0b1725">Form &amp; shape</text>
    <text x="368" y="118" text-anchor="middle" fill="#66788d">sheet / bar</text>

    <rect x="458" y="74" width="116" height="58" rx="9" fill="#fff" stroke="#ccd7e3"/>
    <text x="516" y="100" text-anchor="middle" font-weight="600" fill="#0b1725">Components</text>
    <text x="516" y="118" text-anchor="middle" fill="#66788d">discrete mfg</text>

    <rect x="596" y="74" width="70"  height="58" rx="9" fill="#e6f4f2" stroke="#0d7a6f"/>
    <text x="631" y="100" text-anchor="middle" font-weight="600" fill="#0a5f56">Product</text>
    <text x="631" y="118" text-anchor="middle" fill="#66788d">good</text>

    <line x1="130" y1="103" x2="160" y2="103" stroke="#0a5f56" stroke-width="2" marker-end="url(#ar)"/>
    <line x1="278" y1="103" x2="308" y2="103" stroke="#0a5f56" stroke-width="2" marker-end="url(#ar)"/>
    <line x1="426" y1="103" x2="456" y2="103" stroke="#0a5f56" stroke-width="2" marker-end="url(#ar)"/>
    <line x1="574" y1="103" x2="594" y2="103" stroke="#0a5f56" stroke-width="2" marker-end="url(#ar)"/>
  </g>
  <!-- Secondary label -->
  <rect x="0" y="60" width="680" height="92" rx="10" fill="none" stroke="#0d7a6f" stroke-dasharray="4 4"/>
  <text x="14" y="150" font-size="12" font-weight="600" fill="#0d7a6f">SECONDARY &#183; manufacture &amp; convert</text>
  <!-- Tertiary band -->
  <rect x="0" y="170" width="680" height="62" rx="8" fill="#fdf3e4"/>
  <text x="14" y="194" font-size="13" font-weight="600" fill="#a85a06">TERTIARY &#183; services</text>
  <text x="14" y="216" font-size="12" fill="#66788d">transport &#183; finance &#183; retail &#183; IT &#183; maintenance &#183; the finished good is sold, financed and serviced here</text>
</svg>
"""

OTIT_SVG = """
<svg viewBox="0 0 680 320" role="img" aria-label="IT and OT convergence">
  <defs>
    <marker id="ar2" markerWidth="9" markerHeight="9" refX="6" refY="3"
            orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L6,3 L0,6 Z" fill="#1d4ed8"/>
    </marker>
    <marker id="ar3" markerWidth="9" markerHeight="9" refX="6" refY="3"
            orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L6,3 L0,6 Z" fill="#0a5f56"/>
    </marker>
  </defs>
  <g font-family="Inter, sans-serif" font-size="12">
    <!-- IT side -->
    <rect x="40" y="20" width="600" height="60" rx="9" fill="#eef3f8" stroke="#ccd7e3"/>
    <text x="56" y="42" font-weight="600" fill="#1d4ed8">IT &#183; Information Technology</text>
    <text x="56" y="62" fill="#66788d">ERP &#183; data lake &#183; business intelligence &#183; planning &#183; cybersecurity</text>

    <rect x="40" y="92" width="600" height="46" rx="9" fill="#f7f9fc" stroke="#ccd7e3"/>
    <text x="56" y="119" fill="#0b1725">MES / production management (the bridge)</text>

    <!-- convergence line -->
    <line x1="40" y1="150" x2="640" y2="150" stroke="#a85a06" stroke-width="2" stroke-dasharray="6 5"/>
    <text x="500" y="144" font-size="11" font-weight="600" fill="#a85a06">convergence</text>

    <!-- OT side -->
    <rect x="40" y="160" width="600" height="46" rx="9" fill="#f7f9fc" stroke="#ccd7e3"/>
    <text x="56" y="187" fill="#0b1725">Supervisory control &#183; SCADA / DCS / HMI</text>

    <rect x="40" y="218" width="600" height="46" rx="9" fill="#f7f9fc" stroke="#ccd7e3"/>
    <text x="56" y="245" fill="#0b1725">Controllers &#183; PLC / SIS (safety) / loop tuning</text>

    <rect x="40" y="276" width="600" height="34" rx="9" fill="#e6f4f2" stroke="#0d7a6f"/>
    <text x="56" y="298" font-weight="600" fill="#0a5f56">OT &#183; Operational Technology &#183; field devices (sensors &amp; actuators) on the process</text>

    <!-- data flow arrows -->
    <line x1="340" y1="80" x2="340" y2="160" stroke="#1d4ed8" stroke-width="2" marker-end="url(#ar2)"/>
    <text x="346" y="124" font-size="10.5" fill="#1d4ed8">data up</text>
    <line x1="360" y1="160" x2="360" y2="80" stroke="#0a5f56" stroke-width="2" marker-end="url(#ar3)"/>
    <text x="366" y="138" font-size="10.5" fill="#0a5f56">setpoints down</text>
  </g>
</svg>
"""


def card(pg, h_en, h_vi, b_en, b_vi):
    return ('<div class="card"><h3>%s</h3><p>%s</p></div>'
            % (pg.span(h_en, h_vi), pg.span(b_en, b_vi)))


def build():
    pg = Page(
        "process.html",
        "prc",
        "What is a process? — economy, control & AI | I&C Field Guide",
        "Quá trình là gì? — kinh tế, điều khiển & AI | Sổ tay I&C",
        "A process turns inputs into something more valuable. This page places "
        "that idea in the economy — primary industries extract ore and raw "
        "materials, secondary industries turn them into products, tertiary "
        "industries provide services — and shows why process control, "
        "instrumentation, IT/OT and AI are what let the secondary sector run "
        "safely, efficiently and at scale.",
        "Một quá trình biến đầu vào thành thứ có giá trị hơn. Trang này đặt ý "
        "niệm ấy vào nền kinh tế — công nghiệp sơ cấp khai thác quặng và nguyên "
        "liệu thô, công nghiệp thứ cấp biến chúng thành sản phẩm, công nghiệp "
        "thứ ba cung cấp dịch vụ — và chỉ ra vì sao điều khiển quá trình, thiết "
        "bị đo, IT/OT và AI là những thứ giúp khu vực thứ cấp vận hành an toàn, "
        "hiệu quả và ở quy mô lớn.",
    )

    body = page_intro(
        pg,
        "What is a process?",
        "Quá trình là gì?",
        "A process is any coordinated sequence of operations that turns inputs "
        "into a more valuable output. Place that idea in the economy — where "
        "primary industries pull ore and raw materials out of the ground, "
        "secondary industries forge them into products, and tertiary industries "
        "provide the services around them — and you see exactly where process "
        "control, instrumentation, IT/OT and AI earn their keep.",
        "Quá trình là bất kỳ chuỗi thao tác phối hợp nào biến đầu vào thành đầu "
        "ra có giá trị hơn. Đặt ý niệm ấy vào nền kinh tế — nơi công nghiệp sơ "
        "cấp kéo quặng và nguyên liệu thô từ lòng đất lên, công nghiệp thứ cấp "
        "rèn chúng thành sản phẩm, và công nghiệp thứ ba cung cấp các dịch vụ "
        "xung quanh — bạn sẽ thấy rõ điều khiển quá trình, thiết bị đo, IT/OT "
        "và AI phát huy giá trị ở đâu.",
        [
            ("what", "What is a process?", "Quá trình là gì?"),
            ("sectors", "Three sectors of an economy",
             "Ba khu vực của nền kinh tế"),
            ("valuechain", "From ore to product", "Từ quặng đến sản phẩm"),
            ("need", "Why the secondary sector needs control",
             "Vì sao khu vực thứ cấp cần điều khiển"),
            ("instrumentation", "Instrumentation: the senses",
             "Thiết bị đo: các giác quan"),
            ("control", "Process control: the reflexes",
             "Điều khiển quá trình: phản xạ"),
            ("otit", "IT and OT: two worlds, one plant",
             "IT và OT: hai thế giới, một nhà máy"),
            ("bi", "Business intelligence", "Trí tuệ kinh doanh"),
            ("ai", "AI in the loop", "AI trong vòng lặp"),
            ("path", "Where to read next", "Đọc tiếp ở đâu"),
        ],
    )

    # 01 what -----------------------------------------------------------------
    body += section_open("01", "What is a process?", "Quá trình là gì?", pg, "what")
    body += "<div class=\"sec-head\">"
    body += pg.h2("A process turns inputs into something more valuable",
                  "Quá trình biến đầu vào thành thứ có giá trị hơn")
    body += pg.p(
        "A process is a coordinated set of activities, machines, materials and "
        "people that converts inputs into outputs of greater value. The inputs "
        "are raw materials, energy, information and labour; the outputs are "
        "products, by-products and services. A refinery turning crude oil into "
        "fuel, a furnace turning ore into steel, a dairy pasteurising milk, and "
        "a plant bottling water are all processes.",
        "Quá trình là một tập hợp phối hợp các hoạt động, máy móc, vật liệu và "
        "con người biến đầu vào thành đầu ra có giá trị hơn. Đầu vào là nguyên "
        "liệu thô, năng lượng, thông tin và sức lao động; đầu ra là sản phẩm, "
        "sản phẩm phụ và dịch vụ. Một nhà máy lọc dầu biến dầu thô thành nhiên "
        "liệu, một lò cao biến quặng thành thép, một cơ sở chế biến sữa tiệt "
        "trùng sữa, và một nhà máy đóng chai nước đều là những quá trình.")
    body += "</div><div class=\"grid c3\">"
    body += card(
        pg, "Inputs", "Đầu vào",
        "Raw materials, energy, information and labour that enter the process.",
        "Nguyên liệu thô, năng lượng, thông tin và sức lao động đi vào quá trình.")
    body += card(
        pg, "Transformation", "Biến đổi",
        "Physical, chemical or biological operations that change the material.",
        "Các thao tác vật lý, hóa học hoặc sinh học làm thay đổi vật liệu.")
    body += card(
        pg, "Outputs", "Đầu ra",
        "Products, by-products and services of greater value than the inputs.",
        "Sản phẩm, sản phẩm phụ và dịch vụ có giá trị lớn hơn đầu vào.")
    body += "</div>"
    body += pg.p(
        "Two families are worth separating. <b>Discrete manufacturing</b> makes "
        "countable units you can point at — cars, phones, bearings — assembled "
        "from parts. <b>Process manufacturing</b> makes things you measure by "
        "mass, volume, flow or energy — chemicals, fuels, metals, foods, "
        "pharmaceuticals, cement, paper. This field guide is about the second "
        "family: the <b>process industries</b>, where the product is a stream "
        "rather than a stack of parts.",
        "Có hai nhánh đáng tách biệt. <b>Sản xuất rời rạc</b> tạo ra những đơn "
        "vị đếm được — ô tô, điện thoại, bạc đạn — lắp từ các chi tiết. <b>Sản "
        "xuất quá trình</b> tạo ra những thứ bạn đo bằng khối lượng, thể tích, "
        "lưu lượng hay năng lượng — hóa chất, nhiên liệu, kim loại, thực phẩm, "
        "dược phẩm, xi măng, giấy. Sổ tay này nói về nhánh thứ hai: các <b>ngành "
        "công nghiệp quá trình</b>, nơi sản phẩm là một dòng chứ không phải một "
        "chồng chi tiết.")
    body += pg.p(
        "Within process manufacturing, <b>continuous</b> processes run without "
        "stop — a refinery or a power plant — while <b>batch</b> processes make "
        "a defined quantity then clean and reset — a pharmaceutical campaign or "
        "a food recipe. Both live or die on measurement and control.",
        "Trong sản xuất quá trình, các quá trình <b>liên tục</b> chạy không "
        "ngừng — một nhà máy lọc dầu hay nhiệt điện — còn các quá trình <b>mẻ</b> "
        "sản xuất một lượng định trước rồi vệ sinh và reset — một đợt dược phẩm "
        "hay một công thức thực phẩm. Cả hai sống còn nhờ đo lường và điều khiển.")
    body += section_close()

    # 02 sectors --------------------------------------------------------------
    body += section_open("02", "Three sectors of an economy",
                         "Ba khu vực của nền kinh tế", pg, "sectors")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Where does a \"process\" live in the economy?",
                  "“Quá trình” nằm ở đâu trong nền kinh tế?")
    body += pg.p(
        "Economists sort production into sectors. The classic three-sector model "
        "puts extraction first, manufacturing second, and services third. The "
        "conversion steps — where raw material becomes product — sit almost "
        "entirely in the second sector, and that is where process control is "
        "born.",
        "Các nhà kinh tế chia sản xuất thành các khu vực. Mô hình ba khu vực cổ "
        "điển đặt khai thác lên đầu, chế tạo ở giữa, và dịch vụ cuối cùng. Những "
        "bước chuyển đổi — nơi nguyên liệu trở thành sản phẩm — gần như nằm trọn "
        "trong khu vực thứ hai, và đó là nơi điều khiển quá trình ra đời.")
    body += "</div>"

    rows = [
        ("Primary", "Sơ cấp",
         "Extract and harvest natural resources from the earth, sea and land.",
         "Khai thác và thu hoạch tài nguyên thiên nhiên từ đất, biển và rừng.",
         "Mining, oil &amp; gas extraction, agriculture, forestry, fishing, quarrying",
         "Khai khoáng, khai thác dầu khí, nông nghiệp, lâm nghiệp, thủy sản, khai đá",
         "Ore, crude oil, crops, timber, fish, minerals",
         "Quặng, dầu thô, mùa màng, gỗ, cá, khoáng vật",
         "Supplies the feedstock — the raw material the other sectors convert.",
         "Cung cấp nguyên liệu thô — thứ các khu vực khác chuyển đổi."),
        ("Secondary", "Thứ cấp",
         "Transform raw materials into finished and semi-finished goods.",
         "Biến nguyên liệu thô thành hàng hóa hoàn thiện và bán thành phẩm.",
         "Process industries (metals, chemicals, food, cement, paper, pharma) + discrete manufacturing, utilities, construction",
         "Các ngành quá trình (kim loại, hóa chất, thực phẩm, xi măng, giấy, dược) + sản xuất rời rạc, tiện ích, xây dựng",
         "Metals, fuels, plastics, food, medicines, vehicles, buildings",
         "Kim loại, nhiên liệu, nhựa, thực phẩm, dược phẩm, xe cộ, công trình",
         "This is where processes and process control overwhelmingly live.",
         "Đây là nơi các quá trình và điều khiển quá trình tập trung áp đảo."),
        ("Tertiary", "Thứ ba",
         "Provide services rather than physical goods.",
         "Cung cấp dịch vụ thay vì hàng hóa hữu hình.",
         "Transport, logistics, retail, finance, healthcare, IT, education, maintenance",
         "Vận tải, logistics, bán lẻ, tài chính, y tế, IT, giáo dục, bảo trì",
         "Mobility, capital, care, software, knowledge",
         "Vận chuyển, vốn, chăm sóc, phần mềm, tri thức",
         "Moves, finances and services the output; hosts most IT and data.",
         "Vận chuyển, tài trợ và phục vụ đầu ra; chứa phần lớn IT và dữ liệu."),
    ]
    body += ('<div class="tbl-wrap mt24"><table class="tbl"><thead><tr>'
             '<th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>'
             % (pg.th("Sector", "Khu vực"),
                pg.th("Role", "Vai trò"),
                pg.th("Typical activities", "Hoạt động điển hình"),
                pg.th("Examples", "Ví dụ"),
                pg.th("Process angle", "Góc nhìn quá trình")))
    for s_en, s_vi, r_en, r_vi, a_en, a_vi, e_en, e_vi, p_en, p_vi in rows:
        body += ('<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                 % (pg.span(s_en, s_vi), pg.span(r_en, r_vi),
                    pg.span(a_en, a_vi), pg.span(e_en, e_vi),
                    pg.span(p_en, p_vi)))
    body += "</tbody></table></div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Beyond three", "Ngoài ba khu vực"),
        pg.p(
            "Some models add a <b>quaternary</b> sector (research, development, "
            "data and knowledge work) and a <b>quinary</b> sector (non-profit "
            "and government). Automation, AI and most of this site's IT/OT story "
            "sit in the quaternary layer that increasingly cuts across all three.",
            "Một số mô hình thêm khu vực <b>thứ tư</b> (nghiên cứu, phát triển, "
            "dữ liệu và tri thức) và khu vực <b>thứ năm</b> (phi lợi nhuận và "
            "chính phủ). Tự động hóa, AI và phần lớn câu chuyện IT/OT của sổ tay "
            "này nằm ở tầng thứ tư, ngày càng xuyên suốt cả ba khu vực."))
    body += section_close()

    # 03 value chain ----------------------------------------------------------
    body += section_open("03", "From ore to product", "Từ quặng đến sản phẩm",
                         pg, "valuechain")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Follow one gram of iron",
                  "Theo dõi một gam sắt")
    body += pg.p(
        "Take steel. Iron ore is dug from the ground (primary). It is crushed and "
        "concentrated, then smelted in a blast furnace and refined into molten "
        "iron and steel (secondary). The steel is cast and rolled into sheet and "
        "coil, stamped into body panels, and assembled into a vehicle (still "
        "secondary, now discrete). The finished car is then sold, financed, "
        "insured, fuelled and serviced (tertiary). Every conversion step between "
        "the mine and the showroom is a <b>process</b> — and each one has to be "
        "measured and held under control.",
        "Hãy lấy thép làm ví dụ. Quặng sắt được đào từ lòng đất (sơ cấp). Nó "
        "được nghiền và tuyển, rồi nấu luyện trong lò cao và tinh luyện thành "
        "gang và thép nóng chảy (thứ cấp). Thép được đúc và cán thành tấm và "
        "cuộn, dập thành tấm vỏ, và lắp ráp thành ô tô (vẫn là thứ cấp, nay "
        "thành rời rạc). Chiếc xe hoàn thiện sau đó được bán, tài trợ, bảo hiểm, "
        "cung cấp nhiên liệu và bảo dưỡng (thứ ba). Mỗi bước chuyển đổi từ mỏ "
        "đến showroom đều là một <b>quá trình</b> — và mỗi bước đều phải được "
        "đo lường và giữ trong tầm kiểm soát.")
    body += "</div>"
    body += "<div class=\"fig mt24\">%s</div>" % VALUECHAIN_SVG
    body += pg.p(
        "The same shape repeats everywhere. Bauxite becomes alumina, then "
        "aluminium, then foil and cans. Crude oil becomes fuels and plastics. "
        "Milk becomes yoghurt; grain becomes flour and bread. In every case the "
        "value is created in the <b>secondary</b> conversion, and the tertiary "
        "sector is what delivers it to the people who use it.",
        "Hình dạng ấy lặp lại ở khắp nơi. Quặng bô-xít thành alumin, rồi nhôm, "
        "rồi màng và lon. Dầu thô thành nhiên liệu và nhựa. Sữa thành sữa chua; "
        "ngũ cốc thành bột và bánh mì. Trong mọi trường hợp, giá trị được tạo ra "
        "ở bước chuyển đổi <b>thứ cấp</b>, và khu vực thứ ba là thứ đưa nó đến "
        "người sử dụng.")
    body += section_close()

    # 04 need ----------------------------------------------------------------
    body += section_open("04", "Why the secondary sector needs control",
                         "Vì sao khu vực thứ cấp cần điều khiển", pg, "need")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Without instruments you are blind; without control you are passive",
                  "Không thiết bị đo là mù; không điều khiển là thụ động")
    body += pg.p(
        "A modern process runs at pressures, temperatures and chemistries that "
        "are hostile to people and to the equipment itself. It moves tonnes per "
        "minute and burns energy by the megawatt. The margin between a good day "
        "and a hazardous, wasteful one is held by two disciplines working "
        "together: <b>instrumentation</b> (knowing what the process is doing) "
        "and <b>process control</b> (making it do what you want).",
        "Một quá trình hiện đại vận hành ở áp suất, nhiệt độ và hóa học có hại "
        "cho con người và cho chính thiết bị. Nó di chuyển hàng tấn mỗi phút và "
        "tiêu năng lượng cả megawatt. Khoảng cách giữa một ngày tốt và một ngày "
        "nguy hiểm, lãng phí được giữ bởi hai kỷ luật phối hợp: <b>thiết bị đo</b> "
        "(biết quá trình đang làm gì) và <b>điều khiển quá trình</b> (khiến nó "
        "làm điều bạn muốn).")
    body += "</div>"
    body += "<ul class=\"adv-list\">"
    need = [
        (("Consistency &amp; quality at scale", "Nhất quán &amp; chất lượng ở quy mô lớn"),
         ("A process that drifts makes off-spec product by the trainload. Control "
          "holds every batch to the same setpoint.",
          "Quá trình chệch hướng sẽ tạo ra sản phẩm không đạt chuẩn từng đoàn "
          "tàu. Điều khiển giữ mọi mẻ ở cùng một điểm đặt.")),
        (("Safety", "An toàn"),
         ("Flammable, toxic and pressurised material demands that limits are "
          "respected automatically, not by luck.",
          "Vật liệu dễ cháy, độc và chịu áp đòi hỏi các giới hạn được tôn trọng "
          "tự động, không phải nhờ may mắn.")),
        (("Efficiency &amp; yield", "Hiệu quả &amp; năng suất"),
         ("Every percent of raw material or energy saved at scale is real money "
          "and real carbon.",
          "Mỗi phần trăm nguyên liệu hay năng lượng tiết kiệm được ở quy mô lớn "
          "là tiền thật và carbon thật.")),
        (("Compliance", "Tuân thủ"),
         ("Environmental, safety and product standards are enforced with "
          "auditable records that only an instrumented process can produce.",
          "Các tiêu chuẩn môi trường, an toàn và sản phẩm được thực thi bằng hồ "
          "sơ có thể kiểm toán — thứ chỉ quá trình có thiết bị đo mới tạo ra.")),
        (("Economics", "Kinh tế"),
         ("Margins in process industries are thin; control protects them against "
          "upset, waste and unplanned shutdown.",
          "Biên lợi nhuận trong các ngành quá trình rất mỏng; điều khiển bảo vệ "
          "chúng trước sự cố, lãng phí và dừng máy ngoài kế hoạch.")),
    ]
    for (b_en, b_vi), (s_en, s_vi) in need:
        body += "<li>%s %s</li>" % (pg.el("b", b_en, b_vi), pg.span(s_en, s_vi))
    body += "</ul>"
    body += section_close()

    # 05 instrumentation -----------------------------------------------------
    body += section_open("05", "Instrumentation: the senses",
                         "Thiết bị đo: các giác quan", pg, "instrumentation")
    body += "<div class=\"sec-head\">"
    body += pg.h2("You cannot control what you cannot measure",
                  "Không đo được thì không điều khiển được")
    body += pg.p(
        "Instrumentation is the process's senses. A sensor detects a physical "
        "quantity — temperature, pressure, flow, level, composition, position — "
        "and a transmitter turns it into a signal the system can read, "
        "traditionally 4–20 mA, increasingly digital fieldbus. That signal "
        "feeds controllers, recorders and historians. Without it, the operator "
        "is guessing.",
        "Thiết bị đo là các giác quan của quá trình. Một cảm biến phát hiện một "
        "đại lượng vật lý — nhiệt độ, áp suất, lưu lượng, mức, thành phần, vị trí "
        "— và một bộ truyền tín hiệu biến nó thành tín hiệu hệ thống có thể đọc, "
        "truyền thống là 4–20 mA, nay ngày càng là fieldbus số. Tín hiệu ấy nuôi "
        "các bộ điều khiển, bộ ghi và cơ sở dữ liệu lịch sử. Thiếu nó, vận hành "
        "viên chỉ đang đoán.")
    body += "</div>"
    body += ("<div class=\"hero-cta\"><a class=\"btn btn-p\" href=\"fundamentals.html\">%s</a>"
             "<a class=\"btn\" href=\"instruments.html\">%s</a></div>"
             % (pg.span("Read: Fundamentals of measurement &rarr;",
                        "Đọc: Cơ bản về đo lường &rarr;"),
                pg.span("Browse: 31 instruments &rarr;",
                        "Xem: 31 thiết bị đo &rarr;")))
    body += section_close()

    # 06 control -------------------------------------------------------------
    body += section_open("06", "Process control: the reflexes",
                         "Điều khiển quá trình: phản xạ", pg, "control")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Measure, compare, act, repeat", "Đo, so sánh, tác động, lặp lại")
    body += pg.p(
        "Control closes the loop. The system measures the process value "
        "(PV), compares it to the target setpoint (SP), computes the error, and "
        "drives an actuator — a valve, pump or drive — to correct it. A PID "
        "controller does this continuously; feedback corrects what already "
        "happened, feedforward anticipates what is about to. DCS, PLC and SCADA "
        "are the execution layer that runs these loops across a whole plant.",
        "Điều khiển khép kín vòng lặp. Hệ thống đo giá trị quá trình (PV), so "
        "sánh với điểm đặt mục tiêu (SP), tính sai lệch, và điều khiển một phần "
        "tử chấp hành — van, bơm hay truyền động — để hiệu chỉnh. Bộ điều khiển "
        "PID làm việc này liên tục; phản hồi hiệu chỉnh những gì đã xảy ra, tiền "
        "phản hồi dự báo những gì sắp xảy ra. DCS, PLC và SCADA là tầng thực thi "
        "chạy các vòng ấy trên khắp nhà máy.")
    body += "</div>"
    body += ("<div class=\"hero-cta\"><a class=\"btn btn-p\" href=\"control.html\">%s</a>"
             "<a class=\"btn\" href=\"applications.html\">%s</a></div>"
             % (pg.span("Read: Control &amp; tuning &rarr;",
                        "Đọc: Điều khiển &amp; hiệu chỉnh &rarr;"),
                pg.span("See: Applications by sector &rarr;",
                        "Xem: Ứng dụng theo ngành &rarr;")))
    body += section_close()

    # 07 IT / OT -------------------------------------------------------------
    body += section_open("07", "IT and OT: two worlds, one plant",
                         "IT và OT: hai thế giới, một nhà máy", pg, "otit")
    body += "<div class=\"sec-head\">"
    body += pg.h2("The line between the office and the furnace is dissolving",
                  "Ranh giới giữa văn phòng và lò nung đang tan biến")
    body += pg.p(
        "<b>Operational Technology (OT)</b> is the hardware and software that "
        "senses and changes the physical world — sensors, actuators, PLCs, DCS, "
        "SCADA and safety systems, living close to the process. <b>Information "
        "Technology (IT)</b> is what computes, stores, networks and runs the "
        "business — servers, databases, ERP, planning and analytics. For decades "
        "they hardly spoke. Now data flows up from OT to IT for visibility, and "
        "optimised setpoints flow back down — the two worlds converge.",
        "<b>Công nghệ vận hành (OT)</b> là phần cứng và phần mềm cảm nhận và thay "
        "đổi thế giới vật lý — cảm biến, chấp hành, PLC, DCS, SCADA và hệ thống "
        "an toàn, nằm sát quá trình. <b>Công nghệ thông tin (IT)</b> là thứ tính "
        "toán, lưu trữ, kết nối mạng và vận hành doanh nghiệp — máy chủ, cơ sở "
        "dữ liệu, ERP, lập kế hoạch và phân tích. Suốt nhiều thập kỷ chúng hầu "
        "như không nói chuyện với nhau. Giờ đây dữ liệu chảy từ OT lên IT để có "
        "tầm nhìn, và các điểm đặt tối ưu chảy ngược xuống — hai thế giới hội "
        "tụ.")
    body += "</div>"
    body += "<div class=\"fig mt24\">%s</div>" % OTIT_SVG
    body += pg.p(
        "That convergence is mapped by the ISA-95 / Purdue model: enterprise "
        "systems on top (IT), manufacturing execution in the middle, and "
        "supervisory, control and field layers below (OT). The benefit is "
        "visibility and optimisation across the whole plant. The cost is a "
        "broader attack surface — so segmentation, least privilege and patching "
        "matter as much as the control loops themselves.",
        "Sự hội tụ ấy được mô tả bởi mô hình ISA-95 / Purdue: hệ thống doanh "
        "nghiệp ở trên (IT), điều hành sản xuất ở giữa, và các tầng giám sát, "
        "điều khiển và hiện trường ở dưới (OT). Lợi ích là tầm nhìn và tối ưu "
        "xuyên suốt nhà máy. Cái giá là một bề mặt tấn công rộng hơn — nên phân "
        "đoạn mạng, quyền tối thiểu và vá lỗi quan trọng ngang với chính các vòng "
        "điều khiển.")
    body += section_close()

    # 08 business intelligence ------------------------------------------------
    body += section_open("08", "Business intelligence", "Trí tuệ kinh doanh",
                         pg, "bi")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Turning the flood of process data into decisions",
                  "Biến cơn lũ dữ liệu quá trình thành quyết định")
    body += pg.p(
        "An instrumented plant produces a deluge of time-series data — every "
        "tag, every second. A <b>historian</b> stores it; <b>business "
        "intelligence</b> turns it into meaning. Dashboards and KPIs — overall "
        "equipment effectiveness, yield, energy intensity, throughput, quality "
        "and emissions — let managers see a plant the way an operator sees a "
        "loop. Trend analysis finds slow drift before it becomes a failure; "
        "benchmarking spreads the best unit's practice to the rest.",
        "Một nhà máy có thiết bị đo tạo ra một cơn lũ dữ liệu chuỗi thời gian — "
        "mọi tag, mọi giây. Một <b>cơ sở dữ liệu lịch sử</b> lưu trữ nó; <b>trí "
        "tuệ kinh doanh</b> biến nó thành ý nghĩa. Các bảng điều khiển và KPI — "
        "hiệu suất thiết bị tổng thể, năng suất, cường độ năng lượng, sản lượng, "
        "chất lượng và phát thải — cho phép quản lý nhìn nhà máy như vận hành "
        "viên nhìn một vòng. Phân tích xu hướng tìm ra sự trôi chậm trước khi nó "
        "thành sự cố; so sánh chuẩn lan truyền cách làm tốt nhất của một tổ đến "
        "phần còn lại.")
    body += "</div>"
    body += pg.p(
        "BI is the bridge between OT and the business. It pulls production, "
        "inventory and cost from the plant floor up into ERP, and moves planning "
        "back down. The maturity path runs from reactive (answering alarms) to "
        "predictive (reading trends) to prescriptive (recommending the move) — "
        "and AI is what accelerates the last two steps.",
        "Trí tuệ kinh doanh là cây cầu giữa OT và doanh nghiệp. Nó kéo sản xuất, "
        "tồn kho và chi phí từ sàn nhà máy lên ERP, và đẩy kế hoạch ngược xuống. "
        "Lộ trình trưởng thành đi từ bị động (trả lời báo động) sang dự báo (đọc "
        "xu hướng) rồi sang chỉ định (đề xuất hành động) — và AI là thứ tăng tốc "
        "hai bước cuối.")
    body += section_close()

    # 09 AI ------------------------------------------------------------------
    body += section_open("09", "AI in the loop", "AI trong vòng lặp", pg, "ai")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Intelligence is moving from the dashboard to the actuator",
                  "Trí tuệ đang chuyển từ bảng điều khiển sang phần tử chấp hành")
    body += pg.p(
        "Artificial intelligence earns its place where patterns are too subtle "
        "or too numerous for a fixed rule. On a process plant that means "
        "predictive maintenance from vibration and temperature history, soft "
        "sensors that estimate variables too expensive to measure directly, "
        "anomaly and fault detection, setpoint and recipe optimisation, "
        "production scheduling, quality prediction, and increasingly autonomous "
        "advanced control built on model predictive control and reinforcement "
        "learning.",
        "Trí tuệ nhân tạo phát huy giá trị ở nơi các mẫu hình quá tinh tế hoặc "
        "quá nhiều để một quy tắc cố định gánh vác. Trên một nhà máy quá trình, "
        "điều đó có nghĩa là bảo trì dự đoán từ lịch sử rung động và nhiệt độ, "
        "các cảm biến mềm ước tính những đại lượng quá đắt để đo trực tiếp, phát "
        "hiện dị thường và lỗi, tối ưu điểm đặt và công thức, lập lịch sản xuất, "
        "dự báo chất lượng, và ngày càng là điều khiển tự chủ nâng cao dựa trên "
        "điều khiển dự báo theo mô hình và học tăng cường.")
    body += "</div>"
    body += ("<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>"
             % (pg.span("Keep safety independent", "Giữ an toàn độc lập"),
                pg.p(
                    "AI advises and optimises; it must not become the last line "
                    "of defence. A Safety Instrumented System (SIS) stays "
                    "separate, independent and certified to its SIL — the model "
                    "can suggest, the SIS still protects. Trust also depends on "
                    "data quality, validation before deployment, and "
                    "explainability when a recommendation sends an actuator.",
                    "AI tư vấn và tối ưu; nó không được trở thành lớp phòng thủ "
                    "cuối cùng. Hệ thống an toàn (SIS) vẫn tách biệt, độc lập và "
                    "được chứng nhận theo SIL của nó — mô hình có thể đề xuất, "
                    "SIS vẫn bảo vệ. Niềm tin cũng phụ thuộc vào chất lượng dữ "
                    "liệu, kiểm chứng trước triển khai, và khả năng giải thích "
                    "khi một đề xuất sai khiến một phần tử chấp hành.")))
    body += "<div class=\"hero-cta\"><a class=\"btn btn-p\" href=\"safety.html\">%s</a>" \
            "<a class=\"btn\" href=\"glossary.html\">%s</a></div>" % (
        pg.span("Read: Safety instrumented systems &rarr;",
                "Đọc: Hệ thống an toàn &rarr;"),
        pg.span("Define the terms &rarr;", "Định nghĩa thuật ngữ &rarr;"))
    body += section_close()

    # 10 path ----------------------------------------------------------------
    body += section_open("10", "Where to read next", "Đọc tiếp ở đâu", pg, "path")
    body += "<div class=\"sec-head\">"
    body += pg.h2("This page is the doorway", "Trang này là cửa ngõ")
    body += pg.p(
        "Everything above is the context for the rest of the field guide. Open "
        "Fundamentals to learn how instruments measure, Control to see how loops "
        "hold a setpoint, Applications to tour the seven process sectors, and "
        "Safety to understand the system that watches over all of it.",
        "Mọi thứ ở trên là bối cảnh cho phần còn lại của sổ tay. Mở Cơ bản để "
        "học cách thiết bị đo lường, Điều khiển để thấy các vòng giữ điểm đặt, "
        "Ứng dụng để tham quan bảy ngành quá trình, và An toàn để hiểu hệ thống "
        "giám sát tất cả những thứ đó.")
    body += "</div>"
    body += ("<div class=\"hero-cta\">"
             "<a class=\"btn btn-p\" href=\"fundamentals.html\">%s</a>"
             "<a class=\"btn\" href=\"control.html\">%s</a>"
             "<a class=\"btn\" href=\"applications.html\">%s</a>"
             "<a class=\"btn\" href=\"safety.html\">%s</a></div>"
             % (pg.span("Fundamentals &rarr;", "Cơ bản &rarr;"),
                pg.span("Control &rarr;", "Điều khiển &rarr;"),
                pg.span("Applications &rarr;", "Ứng dụng &rarr;"),
                pg.span("Safety &rarr;", "An toàn &rarr;")))
    body += section_close()

    write("process.html", render(pg, body, "process.html"))
