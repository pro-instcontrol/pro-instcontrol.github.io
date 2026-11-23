# -*- coding: utf-8 -*-
"""Book 8, Chapter 6 - Mechanical Flow Meters (EN/VI bilingual).

Source: 3G E-learning LLC, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 217-256 (40 pages), printed pp. 203-242.  Chapter
7 ("Gas and Liquid Sampling Techniques in Process Industry") begins at
PDFPAGE 257 and is excluded.  Printed page = PDF page - 14.

The source order is kept: Introduction; Competency of Mechanical Flow Meters
(theory of fixed-restriction variable-head flowmeters, incompressible and
compressible flow, Reynolds number, discharge and flow coefficients);
Operations of Mechanical Flow Meters (positive displacement meters and pumps,
reciprocating and nutating-disc meters, oscillating piston meters, oval gear
meters, turbine meters, variable-area, electromagnetic and ultrasonic meters);
and the 46 numbered references on printed pp. 239-241.  All 25 displayed
equations were printed as images and their formula bodies were lost by the
OCR; standard forms reconstructed from the printed symbol definitions are
flagged in place and in the formula box.  The "Citation:" lines are image
credits, not references, and are excluded from the reference list.  Source
Figure 7 has only a bare caption; it is described from the adjacent bypass
installation text.
"""

import iih_common as C
import iihfig6 as F
from iih_common import (eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 40          # PDF pp. 217-256 inclusive (printed pp. 203-242)
BYLINE = "3G E-learning LLC · Illustrated Handbook of Industrial Instrumentation &amp; Control (2018)"
TITLE_EN = "Mechanical Flow Meters"
TITLE_VI = "Đồng hồ đo lưu lượng cơ khí"


# ---------------------------------------------------------------------------
# Reference list (source printed pp. 239-241, numbered 1-46).  URLs broken
# across source lines are joined back into single links.  The text of every
# entry otherwise follows the printed source, including OCR damage such as
# "Dulsseker", "Van Hareveld", "fluidflow", "Eight Edition" and "Datasheet©".
# Bare ampersands (ref. 38) are XML-escaped.  "Citation:" lines are image
# credits and are not part of this list.
# ---------------------------------------------------------------------------
_REFS = [
    "http://www.wisegeek.com/what-is-a-flow-meter.htm",
    "https://www.saylor.org/site/wp-content/uploads/2011/04/Pump.pdf",
    "http://www.mecholic.com/2017/05/nutating-disc-flow-meter-working.html",
    "https://www.badgermeter.com/technologies/nutating-disc-meters/",
    "https://www.engineersedge.com/instrumentation/nutating_disk_displacment_meter.htm",
    "http://accurateflowmeters.com/a/pdf/Nutating%20Disc%20Flowmeter.pdf",
    "http://www.brainkart.com/article/Flow-Measurements_5865/",
    "http://instrumentationtools.com/oval-gear-flow-meter-working-principle/#.WgKYGVuCzIU",
    "http://www.wisegeek.com/what-is-an-electromagnetic-flowmeter.htm",
    "http://www.wisegeek.net/what-is-a-variable-area-flow-meter.htm",
    "https://instrumentationtools.com/turbine-flow-meter-working-principle/#.WgKdNFuCzIU",
    "https://crossinstrumentation.com/blog/oval-gear-meters-dos-and-donts-oval-gear-meter-installations",
    "http://instrumentationtools.com/electromagnetic-flow-meters-working-principle/#.WgKpqVuCzIU",
    "http://www.wisegeek.net/what-is-an-ultrasonic-flow-meter.htm",
    "https://www.omega.co.uk/literature/transactions/volume4/T9904-08-MECH.html",
    "L.K. Spink, 'Principles and Practice of Flow Meter Engineering', Ninth "
    "Edition, The Foxboro Company, Foxboro, Massachusetts. USA. 1978.",
    "R.W. Miller, 'Flow Measurement Engineering Handbook', Second Edition, "
    "McGraw-Hill Publishing Company, 1989.",
    "Bernoulli, Daniel 'Hydrodynamica', Sive de viribus et motibus fluidorum "
    "commentarii, Strasbourg, Johann Reinhold Dulsseker, 1738",
    "Thürlemann, B. 'Methode zur elektrischen Geschwindigkeitsmessung in "
    "Flüssigkeiten.' (Method of Electrical Velocity Measurement in Liquids), "
    "Helv. Phys. Acta 14, pp. 383-419, 1941.",
    "J. A. Shercliff, 'The Theory of Electromagnetic Flow-Measurement', "
    "Cambridge University Press, 1962.",
    "Roger C. Baker, 'Flow Measurement Handbook: Industrial Designs, Operating "
    "Principles, Performance, and Applications', 2nd Edition, Cambridge "
    "University Press, 2000.",
    "E. Loy Upp, Paul J. LaNasa, 'Fluid Flow Measurement: A Practical Guide to "
    "Accurate Flow Measurement', 2nd Edition, Gulf Professional Publishing, 2002.",
    "Dr. Jesse Yoder, 'The Paradigm Case Method of Selecting Flowmeters', "
    "Flow Research, Inc. 2007.",
    "United Kingdom Patent, GB1263614, Published 1972-02-16, Eastech (US) "
    "1,263,614. 'Measuring fluid-flow. Eastech Inc. May 21, 1969 (May 27, "
    "1968), No.25939/69. Heading G1R.",
    "United Kingdom Patent, GB19730015259 19730329 1387380 Measuring "
    "fluidflow Yokogawa Electric Works Ltd, 29 March 1973 (27 April 1972) "
    "15259/73. Heading G1R.",
    "Appendix A. Chapter 5, Section 5.3.4, 2009.",
    "Honeywell, 'SMV 3000 Smart Multivariable Transmitter', Technical "
    "Information, 34-SM-03-01, 2009.",
    "Rosemount 3095 MultiVariable Mass Flow Transmitter, Product Specification "
    "Sheet: 00815-0100-4716, Rev AA, August 2005",
    "ABB, '267CS Multivariable Transmitters', Product Specification Sheet: "
    "Data Sheet, SS/267CS/269CS, 2007.",
    "Appendix A. Chapter 5, Section 5.17.1, 2009.",
    "Rosemount 1595 Conditioning Orifice Plate, Product Data Sheet: "
    "00813-0100-4828, Rev EB, 2007.",
    "F. Cascetta, 'Short history of flowmetering', Published by Elsevier "
    "Science Ltd., Copyright © 1995.",
    "M. Mohitpour, J. Szabo, T. Van Hareveld, 'Pipeline Operation and "
    "Maintenance – a practical approach', ASME Press, USA, 2005.",
    "Krohne, 'Altosonic V 5 - Beam ultrasonic flowmeter for custody transfer "
    "of liquid hydrocarbons', Technical Datasheet© Krohne 7.02330.23.00, 04/2006.",
    "Rheonik, 'RHM 160 - 12 Coriolis Mass Flowmeter', Page 5 of 5, v6, April 2006.",
    "Krohne, 'Optimass bulk flowmeter', Datasheet:4000228103, 03/2009",
    "Appendix A. Chapter 9, 2009.",
    "Gas Processors Suppliers Association (GPSA), 'Engineering Data Book', "
    "FPS version, Volume I &amp; II, Sections 1-26, 1998.",
    "Agar Corporation, 'Not All Multiphase Flowmeters Are Created Equal', "
    "Revision 7, 2004.",
    "Masahiro Tanaka, Kosuke Hayashi, Akio Tomiyama, 'Hybrid multiphase-flow "
    "simulation of bubble-driven flow in complex geometry using an immersed "
    "boundary approach', Multiphase Science and Technology, Volume 21, 2009.",
    "John M. Campbell, 'Gas conditioning and processing. Volume 1: The Basic "
    "Principles', Chapter 9, Multiphase Flow Measurement, Eight Edition, "
    "February 2004.",
    "Dr. Atef Al-Allah, 'Field experience to optimize gas lift well operations', "
    "Academic Focus, Egypt Oil, Issue 10, October 2007.",
    "'Market Prospects for Multiphase Technology', THERMIE Programme action "
    "No: HC 6.3, The Petroleum Science and Technology Institute PSTI, For the "
    "European Commission Offshore Technology Park, Directorate-General for "
    "Energy (DG XVII), 1998.",
    "Mohammed N. Al-Khamis and Abdulaziz F. Al-Bassam, (Saudi Aramco); Zaki "
    "Bakhteyar and Muhammad N. Aftab, (Schlumberger) 'Evaluation of "
    "PhaseWatcher Multiphase Flow Meter (MPFM) Performance in Sour "
    "Environments', Offshore Technology Conference, Copyright 2008.",
    "Phase Dynamics, Inc. http://www.phasedynamics.com/technic.html#faq1",
    "Weatherford, 'Red Eye® 2G Water-cut Meter', Brochure 5313.00, 2008.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> đồng hồ đo lưu lượng — flow meter · lưu lượng thể tích / "
                "lưu lượng khối — volumetric / mass flow · chất lỏng không nén / nén được — "
                "incompressible / compressible fluid · đồng hồ thể tích — positive displacement "
                "meter · bơm thể tích — positive displacement pump · bơm piston qua lại — "
                "reciprocating pump · đồng hồ piston qua lại — reciprocating piston meter · "
                "đồng hồ đĩa dao động — nutating disc (disk) meter · đồng hồ piston dao động — "
                "oscillating piston meter · đồng hồ bánh răng oval — oval gear meter · đồng hồ "
                "tuabin — turbine flow meter · đồng hồ diện tích thay đổi — variable area flow "
                "meter · đồng hồ điện từ — electromagnetic (mag) flow meter · đồng hồ siêu âm — "
                "ultrasonic flow meter · phương trình liên tục — continuity equation · định luật "
                "Bernoulli — Bernoulli's theorem · hệ số lưu lượng Cd — discharge coefficient · "
                "hệ số dòng chảy K — flow coefficient · hệ số tiến tốc độ Mva — velocity approach "
                "factor · tỉ lệ beta β — beta ratio · số Reynolds Re — Reynolds number · "
                "hệ số giãn nở Y — expansion factor · enthalpy · vena contracta · bộ đếm — "
                "totalizer/register · lưới lọc — strainer · đường vòng — bypass line")
    return ("<b>Key terms.</b> flow meter · volumetric / mass flow · incompressible / compressible "
            "fluid · positive displacement meter · positive displacement pump · reciprocating pump · "
            "reciprocating piston meter · nutating disc (disk) meter · oscillating piston meter · "
            "oval gear meter · turbine flow meter · variable area flow meter · electromagnetic "
            "(mag) flow meter · ultrasonic flow meter · continuity equation · Bernoulli's theorem · "
            "discharge coefficient Cd · flow coefficient K · velocity approach factor Mva · beta "
            "ratio β · Reynolds number Re · expansion factor Y · enthalpy · vena contracta · "
            "totalizer/register · strainer · bypass line")


def source_notes(lang):
    """Language-aware box for extraction/OCR quirks (never named `note`)."""
    if lang == "vi":
        return note(
            "<b>Ghi chú của người dịch và của quá trình trích xuất.</b> Tất cả 25 phương trình "
            "trình bày trong nguồn đều được in dạng hình; OCR đã làm mất toàn bộ thân công thức "
            "và chỉ giữ lại số hiệu cùng định nghĩa ký hiệu. Các dạng chuẩn dựng lại được ghi rõ "
            "trong hộp “Thân công thức bị mất” và tại chỗ. Những nét OCR được giữ nguyên trong "
            "bản Anh gồm: câu bị gãy “into the discharge pipe or A positive displacement pump”, "
            "“owing fluid” và “fluid ow rate” (mất “fl”), “Avantages”, “Heance”, “matering”, "
            "“Dispertions”, “2040C”, “offset by?” (phân số bị mất), “interferance”, “be-comes”, "
            "“pro-vides”, “0.8 ≤ 1.0”, “on the most common calibration methods”, “vertical flow "
            "meter”, “fluidflow”, “Dulsseker”, “Van Hareveld” và “Eight Edition”. Các dòng "
            "“Citation:” là ghi công ảnh, không phải tài liệu tham khảo; danh mục gồm đúng 46 mục "
            "có số, các URL bị gãy dòng được nối lại. Hình 7 chỉ có chú thích trần, nội dung mô tả "
            "được suy từ đoạn văn về lắp đặt đường vòng bypass. Chương bắt đầu ở trang in 203 và "
            "kết thúc ở trang in 242; chương 7 ở PDFPAGE 257 không được đưa vào.")
    return note(
            "<b>Translator and extraction notes.</b> All 25 displayed equations were printed as "
            "images; the OCR lost every formula body and kept only the equation numbers and the "
            "printed symbol definitions. Standard forms reconstructed from those definitions are "
            "flagged in the “Formula bodies lost” box and in place. OCR quirks kept in the English "
            "text include the broken sentence “into the discharge pipe or A positive displacement "
            "pump”, “owing fluid” and “fluid ow rate” (lost “fl”), “Avantages”, “Heance”, "
            "“matering”, “Dispertions”, “2040C”, “offset by?” (lost fraction), “interferance”, "
            "“be-comes”, “pro-vides”, “0.8 ≤ 1.0”, “on the most common calibration methods”, "
            "“vertical flow meter”, “fluidflow”, “Dulsseker”, “Van Hareveld” and “Eight "
            "Edition”. The “Citation:” lines are image credits, not references; the list contains "
            "exactly 46 numbered entries, with line-broken URLs rejoined. Source Figure 7 has only "
            "a bare caption; its description is taken from the adjacent bypass-installation text. "
            "The chapter runs from printed p. 203 to p. 242; Chapter 7 at PDFPAGE 257 is excluded.")


def formula_notes(lang):
    """One box covering every displayed equation lost or garbled by the OCR."""
    if lang == "vi":
        return note(
            "<b>Thân công thức bị mất khi trích xuất.</b> Các dạng chuẩn được dựng lại từ định nghĩa "
            "ký hiệu in kèm: (1) Bernoulli P₁/(ρg) + V₁²/(2g) + Z₁ = P₂/(ρg) + V₂²/(2g) + Z₂; "
            "(2) h = (V₂² − V₁²)/(2g); (3) Q = A₁V₁ = A₂V₂; (4) Q_ideal = A₂√[2gh/(1 − β⁴)]; "
            "(5)–(7) V = K₁√(2gh), Q = K₁A√(2gh), W = K₁Aρ√(2gh); (8) β = d/D; "
            "(9) Re = ρVD/µ; (10) C = q_actual/q_ideal; (11) K = Cd/√(1 − β⁴) với M_va = "
            "1/√(1 − β⁴); (12) Q = KA√[2gh(ρ_m − ρ_f)/ρ_f]; (13) Qs = Q√(ρ_f/ρ_s); "
            "(14)–(15) cân bằng năng lượng và enthalpy; (16) H₁ − H₂ = [K/(K − 1)]R(T₁ − T₂); "
            "(17) W = AV/v; (18) lưu lượng khí lý tưởng qua lỗ; (19)–(20) khai triển quanh "
            "P₂/P₁ ≈ 1 và W = CA√[2gρ₁(P₁ − P₂)]; (21)–(22) hệ số giãn nở Y; (23) hiệu chỉnh "
            "độ ẩm; (24) thể tích riêng v = yRT/P; (25) Q_b = Q₁(v_b/v₁)(M_b/M₁). Phương trình "
            "xung tuabin f = n_p·Q/T_p cũng được dựng lại.")
    return note(
            "<b>Formula bodies lost in extraction.</b> The standard forms reconstructed from the "
            "printed symbol definitions are: (1) Bernoulli P1/(ρg) + V1²/(2g) + Z1 = P2/(ρg) + "
            "V2²/(2g) + Z2; (2) h = (V2² − V1²)/(2g); (3) Q = A1V1 = A2V2; (4) "
            "Q_ideal = A2√[2gh/(1 − β⁴)]; (5)-(7) V = K1√(2gh), Q = K1A√(2gh), "
            "W = K1Aρ√(2gh); (8) β = d/D; (9) Re = ρVD/µ; (10) C = q_actual/q_ideal; "
            "(11) K = Cd/√(1 − β⁴) with Mva = 1/√(1 − β⁴); (12) "
            "Q = KA√[2gh(ρm − ρf)/ρf]; (13) Qs = Q√(ρf/ρs); (14)-(15) the energy balance and "
            "enthalpy forms; (16) H1 − H2 = [K/(K − 1)]R(T1 − T2); (17) W = AV/v; (18) ideal-gas "
            "flow through an orifice; (19)-(20) expansion about P2/P1 ≈ 1 and "
            "W = CA√[2gρ1(P1 − P2)]; (21)-(22) the expansion factor Y; (23) the moisture "
            "correction; (24) specific volume v = yRT/P; (25) Qb = Q1(vb/v1)(Mb/M1). The turbine "
            "pulse relation f = np·Q/Tp is likewise reconstructed.")


# ===========================================================================
def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(v, e):
        b.append(ul(v if vi else e))

    def OL(v, e):
        b.append(ol(v if vi else e))

    def FIG(n, key):
        b.append(fig(n, key))

    def EQ(body, num=""):
        b.append(eq(body, num))

    def TBL(head, rows, cap):
        b.append(table(head, rows, cap))

    # ---------------------------------------------------------------- lead
    b.append(lead(
        "Chương này trình bày đồng hồ đo lưu lượng cơ khí: cách phân loại theo thể tích hay khối "
        "lượng, cơ sở đo đầu áp thay đổi với đoạn thu hẹt (phương trình liên tục, định luật "
        "Bernoulli, số Reynolds, hệ số Cd và K, dòng chất nén được), rồi các dạng đồng hồ thể "
        "tích, tuabin, diện tích thay đổi, điện từ và siêu âm."
        if vi else
        "This chapter covers mechanical flow meters: how flow is expressed on a volumetric or mass "
        "basis, the basis of variable-head meters with a fixed restriction (the continuity equation, "
        "Bernoulli's theorem, Reynolds number, the Cd and K coefficients, and compressible flow), and "
        "then positive-displacement, turbine, variable-area, electromagnetic and ultrasonic meters."))
    b.append(source_notes(lang))

    # ---------------------------------------------------------------- 6.1
    H("6.1 Giới thiệu", "6.1 Introduction")
    P("Đồng hồ đo lưu lượng là thiết bị dùng để đo chất lỏng hoặc chất khí chảy qua nó. Kết quả "
      "trả về có thể được biểu thị bằng một trong hai giá trị đo: lưu lượng thể tích hoặc lưu lượng khối. "
      "Chỉ số của đồng hồ thể tích được tính theo đơn vị riêng của ngành và ứng dụng — gallon, "
      "lít hoặc inch khối trên giây — trong khi đồng hồ lưu lượng khối thể hiện phép đo bằng pound "
      "hoặc kilogram trên giây. Có nhiều phân loại đồng hồ đo lưu lượng chung, mỗi loại gồm nhiều "
      "biến thể. Đồng hồ được dùng để đo nguồn cung cấp khí và chất lỏng trong nhiều ngành và ứng "
      "dụng như nhà máy sản xuất, nhà máy bia, bệnh viện và hệ thống cấp nước sinh hoạt hoặc công "
      "nghiệp.",
      "A flow meter is a device used to measure fluid or gas moving through it. The results returned "
      "by the meter may be expressed in one of two measurement values: volumetric flow or mass flow. "
      "Flow meter readings are returned in area- and application-specific units, with volumetric types "
      "producing readings in gallons, liters or cubic inches per second, while mass flow meters express "
      "their measurement in pounds or kilograms per second. There are several different general flow "
      "meter-type classifications, each of which is represented by a range of variants. Flow meters are "
      "used to meter the supply of gases and fluids in a wide range of industries and applications such "
      "as manufacturing plants, breweries, hospitals and domestic or industrial water supplies.")
    P("Việc đo lưu lượng khí và chất lỏng là chức năng thiết yếu trong điều khiển quá trình công "
      "nghiệp, hệ thống tính tiền cho người tiêu dùng và điều trị y tế. Các phép đo này thường "
      "thực hiện bằng cách lắp đồng hồ nối tiếp với đường dẫn chất lỏng hoặc khí. Đồng hồ sau đó "
      "theo dõi dòng vật liệu qua chúng nhờ tác động của nhiều cơ chế khác nhau. Kết quả tính toán "
      "có thể hiển thị ngay trên đồng hồ hoặc gửi qua đầu ra điện tử tới màn hình từ xa hoặc cơ sở "
      "lưu trữ dữ liệu. Dù mọi đồng hồ đều đo dòng vật liệu thời gian thực đi qua cụm của nó, chúng "
      "vẫn chia thành hai loại riêng biệt. Cả hai loại dùng đơn vị đo khác nhau, lại thay đổi theo "
      "vị trí địa lý hoặc ngành công nghiệp. Đồng hồ lưu lượng khối đo khối lượng hoặc trọng lượng "
      "vật chất của chất lỏng hay khí đi qua hệ thống. Đồng hồ lưu lượng thể tích đo thể tích vật "
      "chất chảy. Do khí có thể nén, lưu lượng của chúng thường được biểu thị bằng foot khối thực "
      "tế hoặc mét khối chuẩn trên giây.",
      "The metering of the flow of gases and fluids is an essential function in industrial process "
      "control, consumer billing systems and medical treatments. These measurements are typically "
      "achieved by placing a flow meter in series with the fluid or gas feed line. These meters then "
      "monitor the flow of material through them via the action of several different types of "
      "mechanisms. The calculated results may then be displayed on the meter itself or sent via an "
      "electronic output to a remote display or data storage facility. Although all flow meters "
      "measure real-time material flow across their assemblies, they do fall into two distinct types. "
      "Both types of flow meter use different types of measurement units which, in themselves, differ "
      "according to global locations or industry types. Mass flow meters measure the physical mass or "
      "weight of the fluid or gas passing through the system. Volumetric flow meters measure the "
      "physical volume of material flow. Due to the compressibility of gases, their flow rates are "
      "often expressed as actual cubic feet or standard cubic meters per second.")
    P("Cơ chế đồng hồ đo lưu lượng cũng được xếp thành nhiều nhóm riêng gồm loại cơ khí, áp suất, "
      "quang học và nhiệt. Đồng hồ multi-jet, bánh xe Pelton và đồng hồ Woltmann đều là loại cơ khí, "
      "phụ thuộc vào chuyển động của một bộ cánh chèo, cánh xoắn ốc hoặc cánh quạt để đo dòng "
      "vật liệu. Đồng hồ áp suất dùng ống Venturi, ống pilot và tấm lỗ để đo chênh áp dùng tính "
      "lưu lượng. Đồng hồ quang học dùng laser và đầu dò quang để đo ánh sáng tán xạ. Đồng hồ nhiệt "
      "dùng hệ thống phần tử gia nhiệt và cảm biến nhiệt độ để tính chênh nhiệt độ tĩnh và đang chảy, "
      "kết hợp với đặc tính vật liệu đã biết để suy ra giá trị lưu lượng.",
      "Flow meter mechanisms are also grouped into several distinct categories including mechanical, "
      "pressure, optical and thermal types. The multiple-jet, Pelton wheel and Woltmann meters are all "
      "mechanical flow meter types which depend on the movement of a set of paddles, helical blades or "
      "impellers to measure the material flow. Pressure flow meters utilize venturis, pilot tubes and "
      "orifice plates to measure the pressure differentials used to calculate flow rates. Optical flow "
      "meters use lasers and photo detectors to measure dispersed light to calculate their flow "
      "results. Thermal meters make use of a system of heater elements and temperature sensors to "
      "calculate static and flowing temperature differentials in conjunction with known material "
      "characteristics to extrapolate flow values.")
    P("Các thiết bị đo lưu lượng này là bộ phận thiết yếu của nhiều ứng dụng điều khiển quá trình "
      "công nghiệp đòi hỏi giá trị cấp liệu chính xác. Trong những ứng dụng đó, đồng hồ thường giao "
      "tiếp với bộ điều khiển quá trình để chỉnh lưu nguyên liệu hoặc sản phẩm cuối. Đồng hồ cũng "
      "được dùng rộng rãi để tính toán mức tiêu thụ nước và khí của hộ gia đình và công nghiệp nhằm "
      "mục đích thu phí.",
      "These flow metering devices are an essential part of many industrial process control "
      "applications where exacting material feed values is required. In these applications, the flow "
      "meter will typically interface with process controllers to adjust the flow of raw materials or "
      "end products. The flow meter is also widely used to calculated domestic and industrial consumer "
      "usage of water and gas for billing purposes.")

    # ---------------------------------------------------------------- 6.2
    H("6.2 Năng lực của đồng hồ đo lưu lượng cơ khí",
      "6.2 Competency of Mechanical Flow Meters")
    P("Đồng hồ đo lưu lượng dạng đầu áp thay đổi với đoạn thu hẹt cố định dùng các cảm biến khác "
      "nhau như tấm lỗ, ống Venturi, vòi phun, ống Pitot, ống Dall; đồng hồ định lượng như đồng hồ "
      "thể tích; và đồng hồ lưu lượng khối — đó là những loại phổ biến của đồng hồ đo lưu lượng cơ khí.",
      "Fixed restriction variable head type flow meters using different sensors like orifice plate, "
      "venturi tube, flow nozzle, pitot tube, dall tube, quantity meters like positive displacement "
      "meters, mass flow meters are the popular types of mechanical flow meters.")

    # ---------------- 6.2.1 Theory of Fixed Restriction Variable Head Type
    H("Lý thuyết về đồng hồ dạng đầu áp thay đổi với đoạn thu hẹt cố định",
      "Theory of Fixed Restriction Variable Head Type Flowmeters", h3)
    P("Ở đồng hồ dạng đầu áp thay đổi, người ta thường đưa một đoạn thu hẹt có kích thước đã biết vào "
      "đường ống; hệ quả là xuất hiện tổn thất cột áp hay sụt áp tại đoạn thu hẹt khi vận tốc dòng "
      "tăng. Đo độ sụt áp này chính là thước đo lưu lượng.",
      "In the variable head type flow meters, a restriction of known dimensions is generally "
      "introduced into pipeline, consequently there occurs a head loss or pressure drop at the "
      "restriction with increase in the flow velocity. Measurement of this pressure drop is an "
      "indication of the flow rate.")
    FIG(1, F.fig_f01())
    P("Phép đo đầu áp bắt nguồn từ định lý Bernoulli, theo đó trong một dòng chảy, tổng cột áp "
      "áp suất, cột áp vận tốc và cột áp độ cao tại một điểm bằng tổng của chúng tại điểm khác "
      "theo chiều dòng cộng với tổn thất do ma sát giữa hai điểm. Cột áp vận tốc được định nghĩa "
      "là khoảng cách thẳng đứng mà chất lỏng phải rơi để đạt được vận tốc đã cho. Cột áp áp suất "
      "là khoảng cách thẳng đứng mà một cột chất lỏng đang chảy dâng lên trong ống hở đầu do áp "
      "suất tĩnh. Nói chung người ta giả thiết hệ thống dòng một chiều. Sơ đồ của hệ thống như vậy "
      "với một đoạn thu hẹt trong đường ống được cho trong Hình 1.",
      "Head—type flow measurement derives from Bernoulli's theorem which states that in a flowing "
      "stream, the sum of the pressure head, the velocity head and the elevation head at one point "
      "is equal to their sum at another point in the direction of flow plus the loss due to friction "
      "between the two points. Velocity head is defined as the vertical distance through which a liquid "
      "would fall to attain a given velocity. Pressure head is the vertical distance which a column of "
      "the flowing liquid would rise in an open-ended tube as a result of the static pressure. In "
      "general, a one—dimensional flow system is assumed. The schematic representation of such a system "
      "with a restriction in the pipeline is shown in Fig.1.")

    # -------------------- Flow of Incompressible Fluids in Pipes
    H("Dòng chất lỏng không nén trong ống", "Flow of Incompressible Fluids in Pipes", h4)
    P("Mặt cắt 1 là vị trí của điểm lấy áp thượng lưu và mặt cắt 2 là vị trí hạ lưu. Các ký hiệu "
      "T, A, ρ, V, P và Z lần lượt biểu thị Nhiệt độ, Tiết diện, Mật độ, Vận tốc dòng, Áp suất và "
      "Độ cao đường tâm. Nếu độ cao này rất nhỏ sao cho Z₂ − Z₁ có thể bỏ qua, phương trình "
      "Bernoulli cho dòng không nén (ρ₁ = ρ₂), không ma sát và thích ứng được viết là",
      "Section-1 is the position of upstream tap and Section-2 that for downstream. The terms T, A, ρ, "
      "V, P and Z represent Temperature, Area, Density, Stream velocity, Pressure and Central line "
      "elevation respectively. If this elevation is quite small such that Z2 – Z1 is negligible, the "
      "Bernoulli's equation for an incompressible (ρ1 = ρ2) frictionless and adaptive flow is written as")
    EQ("P<sub>1</sub>/(ρ g) + V<sub>1</sub><sup>2</sup>/(2 g) + Z<sub>1</sub> = "
       "P<sub>2</sub>/(ρ g) + V<sub>2</sub><sup>2</sup>/(2 g) + Z<sub>2</sub>", "1")
    P("trong đó g = gia tốc trọng trường, suy ra",
      "where g = acceleration due to gravity, giving")
    EQ("(P<sub>1</sub> − P<sub>2</sub>)/(ρ g) = (V<sub>2</sub><sup>2</sup> − "
       "V<sub>1</sub><sup>2</sup>)/(2 g) = h", "2")
    P("Phương trình liên tục cho loại dòng này là",
      "The continuity equation for this type of flow is")
    EQ("Q = A<sub>1</sub> V<sub>1</sub> = A<sub>2</sub> V<sub>2</sub>", "3")
    P("trong đó Q = lưu lượng thể tích tính bằng m³/s.",
      "where Q = volume flow rate in m3/sec.")
    P("Kết hợp các phương trình (2) và (3) và biến đổi, ta được",
      "Combining equations (2) and (3) and manipulating, one gets")
    EQ("Q = A<sub>2</sub> √[2 g h / (1 − (A<sub>2</sub>/A<sub>1</sub>)<sup>2</sup>)]", "4")
    P("với β = d/D xuất hiện qua (A₂/A₁)² = β⁴. Đây là phương trình lưu lượng thể tích lý tưởng.",
      "where β = d/D enters through (A2/A1)² = β⁴. This is equation for the ideal volume flow rate.")
    P("Với điều kiện dòng thực có tổn thất ma sát, cần hiệu chỉnh công thức này. Bên cạnh đó, "
      "tiết diện dòng nhỏ nhất không nằm tại đoạn thu hẹt mà ở một điểm hơi xuôi dòng, gọi là "
      "‘Venacontracta’. Điểm này lại phụ thuộc vào lưu lượng. Trong khi vị trí lấy áp cố định, vị "
      "trí vận tốc cực đại thay đổi khi lưu lượng thay đổi.",
      "For actual flow conditions with frictional losses present, a correction to this formula is "
      "necessary. Besides, the minimum area of flow channel occurs not at the restriction but at some "
      "point slightly downstream, known as the ‘Venacontracta’. This in turn depends on the flow rate. "
      "While the tapping positions are fixed, the position of maximum velocity changes with changing "
      "flow rate.")
    P("Các phương trình cơ bản là:",
      "The basic equations are :")
    EQ("V = K<sub>1</sub> √(2 g h)", "5")
    EQ("Q = K<sub>1</sub> A √(2 g h)", "6")
    EQ("W = K<sub>1</sub> A ρ √(2 g h)", "7")
    U(["V = vận tốc chất lỏng", "Q = lưu lượng thể tích", "W = lưu lượng khối",
       "A = tiết diện ngang của ống", "h = cột áp chênh giữa hai điểm đo",
       "ρ = mật độ chất lỏng đang chảy",
       "K₁ = hằng số gồm tỉ lệ giữa tiết diện ống và tiết diện vòi phun hoặc đoạn thu hẹt khác"],
      ["V = Velocity of Fluid", "Q = Volume flow rate", "W = Mass flow rate",
       "A = Cross-sectional area of the pipe", "h = differential head between points of measurement",
       "ρ = density of the flowing fluid",
       "K1 = Constant which includes ratio of cross-sectional area of pipe to cross-sectional area "
       "of nozzle or other restrictions"])
    P("Tỉ lệ Beta. Hầu hết đồng hồ đầu áp đều dựa vào một đoạn thu hẹt trên đường dòng để tạo ra "
      "sự thay đổi vận tốc. Với ống tròn thông thường, tỉ lệ Beta là tỉ lệ giữa đường kính đoạn thu "
      "hẹt và đường kính trong của ống.",
      "β Ratio. Most variable head meters depend on a restriction in the flow path to produce a change "
      "in velocity. For the usual circular pipe, the Beta ratio is the ratio between the diameter of "
      "the restriction and the inside diameter of the pipe.")
    EQ("β = d/D", "8")
    U(["d = đường kính đoạn thu hẹt", "D = đường kính trong của ống"],
      ["d = diameter of the restriction", "D = inside diameter of the pipe"])

    # -------------------- Reynolds Number
    H("Số Reynolds", "Reynolds Number", h4)
    P("Trong thực tế, vận tốc dòng tại bất kỳ mặt cắt nào cũng tiến về không trong lớp biên sát "
      "thành ống và thay đổi theo đường kính. Phân bố vận tốc này có ảnh hưởng đáng kể tới quan hệ "
      "giữa vận tốc dòng và chênh áp sinh ra trong đồng hồ đầu áp.",
      "In practice, flow velocity at any cross section approaches zero in the boundary layer adjacent "
      "to the pipe wall and varies across the diameter. This flow velocity profile has a significant "
      "effect on the relationship between flow velocity and pressure difference developed in the head "
      "meters.")
    P("Ngài Osborne Reynolds đã đề xuất một tỉ số không thứ nguyên duy nhất gọi là số Reynolds, làm "
      "tiêu chí mô tả hiện tượng này. Số đó, ký hiệu Re, được biểu thị là",
      "Sir Osborne Reynolds proposed single, dimensionless ratio known as Reynolds number, as a "
      "criterion to describe this phenomenon. This number, Re, is expressed as")
    EQ("Re = ρ V D / µ", "9")
    U(["V = vận tốc", "D = đường kính đường ống", "ρ = mật độ", "µ = độ nhớt tuyệt đối"],
      ["V = velocity", "D = Diameter of the pipeline", "ρ = density", "µ = absolute viscosity"])
    P("Số Reynolds biểu thị tỉ lệ giữa lực quán tính và lực nhớt. Ở số Reynolds rất nhỏ, lực nhớt "
      "chiếm ưu thế và lực quán tính rất ít tác dụng. Ở số Reynolds lớn, lực quán tính chiếm ưu thế "
      "và hiệu ứng nhớt trở nên không đáng kể.",
      "Reynolds number expresses the ratio of inertial forces to viscous forces. At a very low Reynolds "
      "number, viscous forces predominate and inertial forces have little effect. At high Reynolds number, "
      "inertial forces predominate and viscous effects become negligible.")

    # -------------------- Discharge Coefficient
    H("Hệ số lưu lượng Cd", "Discharge Coefficient (Cd)", h4)
    P("Hệ số lưu lượng C được định nghĩa là tỉ lệ giữa lưu lượng thể tích thực tế và lưu lượng thể "
      "tích lý tưởng.",
      "Discharge coefficient, C is defined as the ratio between actual volumetric flow rate and ideal "
      "volumetric flow rate.")
    EQ("C = q<sub>actual</sub> / q<sub>ideal</sub>", "10")
    U(["q<sub>actual</sub> = lưu lượng thể tích thực tế",
       "q<sub>ideal</sub> = lưu lượng thể tích lý tưởng (lý thuyết)"],
      ["q actual = Actual volumetric flow rate",
       "qideal = Ideal volumetric flow rate. (Theoretical)"])

    # -------------------- Flow Coefficient
    H("Hệ số dòng chảy K", "Flow Coefficient (K)", h4)
    EQ("K = C<sub>d</sub> / (1 − β<sup>4</sup>)<sup>1/2</sup>", "11")
    U(["K = hệ số dòng chảy", "Cd = hệ số lưu lượng", "β = tỉ lệ đường kính = d/D"],
      ["K = Flow coefficient", "Cd = discharge coefficient", "β = ratio of diameters = d/D"])
    P("trong đó 1/(1 − β⁴)^(1/2) được gọi là hệ số tiến tốc độ (tức vận tốc tại mặt cắt A1) Mva.",
      "where 1/(1 − β4)1/2 is known as velocity approach factor (that is velocity at section-A1) Mva.")
    FIG(2, F.fig_f02())
    P("Đo dòng chất lỏng bằng tấm lỗ và áp kế chênh áp như Hình 2 đòi hỏi phải tính đến ảnh hưởng "
      "của chất lỏng lên dung dịch áp kế. Hơn nữa, chênh áp tại tấm lỗ thường được biểu thị bằng "
      "chiều cao cột chất lỏng. Khi đó",
      "Measuring fluid flow with an orifice and differential pressure manometer as shown in Fig 2, "
      "requires that the effect of the fluid over the manometer liquid be taken into account. "
      "Furthermore, the pressure differential at the orifice is usually expressed in liquid-column "
      "height. Then")
    EQ("Q = K A √[2 g h (ρ<sub>m</sub> − ρ<sub>f</sub>) / ρ<sub>f</sub>]", "12")
    U(["h = chênh áp tại đoạn thu hẹt, tính theo chiều cao cột chất lỏng",
       "ρ<sub>m</sub> = trọng lượng riêng của dung dịch áp kế",
       "ρ<sub>f</sub> = trọng lượng riêng của chất lỏng phía trên dung dịch áp kế"],
      ["h = differential at restriction, liquid column height",
       "ρm = weight density of manometer fluid",
       "ρf = weight density of fluid over the manometer fluid"])
    P("Cuối cùng, nếu lưu lượng cần được quy về nhiệt độ phòng điều khiển, nơi mật độ chất lỏng là "
      "ρs, thì từ các phương trình (4), (11) và (12),",
      "Finally if the flow rate is to be converted at the control room temperature at which the fluid "
      "density is ρs, then from equations (4), (11) and (12).")
    EQ("Q<sub>s</sub> = Q √(ρ<sub>f</sub> / ρ<sub>s</sub>)", "13")
    b.append(formula_notes(lang))

    # -------------------- Flow of Compressible Fluids in Pipes
    H("Dòng chất lỏng nén được trong ống", "Flow of Compressible Fluids in Pipes", h4)
    P("Nếu chất lỏng nén được, có thể thu được lưu lượng nếu coi khí là lý tưởng và dòng là đoạn "
      "nhiệt. Quan hệ giữa áp suất và vận tốc khi chất nén chảy qua tấm lỗ được tìm từ định luật "
      "bảo toàn năng lượng như dùng trong nhiệt động học. Giả thiết không có dòng nhiệt tới hoặc "
      "từ chất lỏng, không có công ngoài tác dụng lên hoặc bởi chất lỏng, và bỏ qua hiệu độ cao "
      "rất nhỏ (Z₁ − Z₂), ta có",
      "If the fluid is compressible, a flow rate can be obtained if the gas is considered ideal and "
      "the flow is considered adiabatic. The relation between pressure and velocity for flow of a "
      "compressible fluid through an orifice can be found from the law of conservation of energy as "
      "employed in thermodynamics. Assuming no heat flow to or from the fluid and no external work "
      "done on or by the fluid and neglecting the very small datum level difference (Z1 – Z2), we have")
    EQ("E<sub>1</sub> + P<sub>1</sub> v<sub>1</sub> + V<sub>1</sub><sup>2</sup>/(2 J) + "
       "g Z<sub>1</sub>/J = E<sub>2</sub> + P<sub>2</sub> v<sub>2</sub> + "
       "V<sub>2</sub><sup>2</sup>/(2 J) + g Z<sub>2</sub>/J", "14")
    U(["E = năng lượng phân tử bên trong của chất lỏng",
       "J = đương lượng công của nhiệt",
       "v = thể tích riêng của chất lỏng"],
      ["E = internal molecular energy of fluid", "J = work equivalent of heat",
       "v = Specific volume of fluid"])
    P("Dùng định nghĩa enthalpy H cho",
      "Employing the definition of enthalpy H gives")
    EQ("H<sub>1</sub> + V<sub>1</sub><sup>2</sup>/(2 J) + g Z<sub>1</sub>/J = "
       "H<sub>2</sub> + V<sub>2</sub><sup>2</sup>/(2 J) + g Z<sub>2</sub>/J", "15")
    P("Với khí lý tưởng và nhiệt dung riêng không đổi,",
      "For an ideal gas and if specific heats are constant,")
    EQ("H<sub>1</sub> − H<sub>2</sub> = [K/(K − 1)] R (T<sub>1</sub> − T<sub>2</sub>) = "
       "[K/(K − 1)] (P<sub>1</sub> v<sub>1</sub> − P<sub>2</sub> v<sub>2</sub>)", "16")
    U(["K = tỉ lệ nhiệt dung riêng = Cp/Cv", "R = hằng số khí của khí đã cho",
       "T = nhiệt độ tuyệt đối"],
      ["K = ratio of specific heats = Cp/Cv", "R = gas constant for a given gas",
       "T = absolute temperature"])
    P("Từ phương trình liên tục (bảo toàn khối lượng),",
      "From the equation of continuity (conservation of mass).")
    EQ("W = A V / v = ρ A V", "17")
    P("trong đó W là lưu lượng khối.", "where W is the mass flow rate.")
    P("Kết hợp các phương trình trên và biến đổi, ta thu được quan hệ cho dòng khí lý tưởng.",
      "Combining the foregoing equations and manipulating, we get the relation for flow of ideal gases.")
    EQ("W = C A √{ [2 g K/(K − 1)] (P<sub>1</sub>/v<sub>1</sub>) "
       "[ (P<sub>2</sub>/P<sub>1</sub>)<sup>2/K</sup> − "
       "(P<sub>2</sub>/P<sub>1</sub>)<sup>(K+1)/K</sup> ] }", "18")
    P("Tuy nhiên, áp kế đo (P₁ − P₂) chứ không đo P₂/P₁, vì vậy cần chuyển phương trình (18) sao "
      "cho W là hàm của (P₁ − P₂). Viết P₂/P₁ = 1 − x sao cho x = 1 − (P₂/P₁). Nhìn chung với "
      "dòng khí thì P₂/P₁ rất gần với đơn vị, sao cho x rất gần với không.",
      "Manometer, however, measures (P1 – P2) and not P2/P1, therefore, it is necessary to convert the "
      "equation (18) such that W is a function of (P1 – P2). Write P2/P1 = 1 – x such that x = 1 – "
      "(P2/P1). In general, for gas flow P2/P1 is very close to unity such that x is very close to zero.")
    P("Do đó,", "Hence,")
    EQ("(P<sub>2</sub>/P<sub>1</sub>)<sup>2/K</sup> − "
       "(P<sub>2</sub>/P<sub>1</sub>)<sup>(K+1)/K</sup> ≈ "
       "[(K − 1)/K] · (P<sub>1</sub> − P<sub>2</sub>)/P<sub>1</sub>", "19")
    P("Dùng phương trình (19), phương trình (18) được biến đổi thành",
      "using equation (19), equation (18) is modified to")
    EQ("W = C A √[2 g ρ<sub>1</sub> (P<sub>1</sub> − P<sub>2</sub>)]", "20")
    P("trong đó C là hệ số lưu lượng.", "where C is the discharge coefficient.")
    P("Để tính nhanh, người ta định nghĩa thêm một thông số gọi là hệ số giãn nở rational Y, bằng "
      "tỉ lệ giữa lưu lượng nén được và lưu lượng không nén được tính theo phương trình (20).",
      "For quick calculation an additional parameter known as the rational expansion factor Y is "
      "defined as the ratio of the compressible flow rate to the incompressible rate given by equation (20).")
    P("Bằng cách xác định lưu lượng khối của chất không nén rồi nhân với Y, có thể tìm lưu lượng "
      "của chất nén; Y được biểu diễn là",
      "By determining the mass flow rate for incompressible fluids and multiplying with Y, flow rate "
      "for compressible fluids can be found out and Y can be easily shown as")
    EQ("Y = √{ [K τ<sup>2/K</sup>/(K − 1)] · "
       "[1 − τ<sup>(K−1)/K</sup>] / (1 − τ) },  %s τ = P<sub>2</sub>/P<sub>1</sub>"
       % ("với" if lang == "vi" else "with"), "21")
    P("Thay vì tính Y từ phương trình (21), người ta dùng các quan hệ thực nghiệm cho kết quả tốt "
      "với một số giá trị hạn chế của P₂/P₁, chẳng hạn 0.8 ≤ 1.0.",
      "Instead of calculating Y from the equation (21) empirical relations are suggested which give "
      "good results for limited (P2/P1) values, such as 0.8 ≤ 1.0.")
    EQ("Y = 1 − (0.41 + 0.35 β<sup>4</sup>) (P<sub>1</sub> − P<sub>2</sub>)/(K P<sub>1</sub>)", "22")
    P("Khi khí chứa hơi ẩm, cần một hiệu chỉnh nữa để tính đúng mật độ của hơi.",
      "When the gas contains moisture, as further correction is required to account correctly for "
      "the density of the vapor.")
    EQ("S<sub>w</sub> = S (P − P<sub>v</sub>)/P + S<sub>v</sub> P<sub>v</sub>/P", "23")
    U(["P<sub>v</sub> = áp suất hơi (tuyệt đối)",
       "S<sub>v</sub> = trọng lực riêng của hơi quy về không khí ở cùng áp suất và nhiệt độ",
       "S = trọng lực riêng của khí", "P = áp suất của khí"],
      ["Pv = Vapour pressure (abs)",
       "Sv = Vapour specific gravity referred to air at the same pressure and temperature",
       "S = Specific gravity of the gas", "P = Pressure of the gas"])
    P("Thể tích riêng của khí được tìm từ",
      "The specific volume of the gas may be found from")
    EQ("v = y R T / P", "24")
    U(["y = hệ số nén", "R = hằng số khí"],
      ["y = compressibility factor", "R = gas constant"])
    P("Phương trình lưu lượng cho khí là",
      "The flow equation for gases is")
    EQ("Q<sub>b</sub> = Q<sub>1</sub> (v<sub>b</sub>/v<sub>1</sub>) "
       "(M<sub>b</sub>/M<sub>1</sub>)", "25")
    U(["v<sub>b</sub> = thể tích riêng của khí ở điều kiện chuẩn",
       "v<sub>1</sub> = thể tích riêng của khí ở điều kiện thượng lưu",
       "M<sub>1</sub> = hệ số ẩm ở điều kiện thượng lưu",
       "M<sub>b</sub> = hệ số ẩm ở điều kiện chuẩn"],
      ["v b = Specific volume of gas at base condition",
       "v1 = specific volume of gas at upstream conditions",
       "M1 = Moisture factor at upstream conditions",
       "Mb = Moisture factor at base conditions"])

    # ---------------------------------------------------------------- 6.3
    H("6.3 Vận hành của đồng hồ đo lưu lượng cơ khí",
      "6.3 Operations of Mechanical Flow Meters")
    P("Đồng hồ điện từ đang dần thay thế các thiết kế đồng hồ cơ khí truyền thống. Dù cả hai đều đo "
      "dòng chất lỏng trong ống, chúng làm việc theo những cách khác nhau.",
      "Magnetic flow meters are increasingly taking the place of traditional mechanical flow meter "
      "designs. While they both measure the flow of a liquid in a pipe, they do so in different ways.")
    P("Đồng hồ cơ khí phổ biến nhất được đưa vào trong ống và dùng tuabin, bánh xe hoặc cánh chèo để "
      "đo vận tốc, rồi tính lưu lượng thể tích nhờ biết diện tích mặt cắt của ống lắp đặt. Loại phổ "
      "biến nhất trong các đồng hồ cơ khí kể trên dùng một tuabin quay khi dòng nước tác dụng lực "
      "lên cánh. Độ quay của tuabin tỉ lệ với vận tốc chất lỏng đi qua nó. Khi biết vận tốc, có thể "
      "tính lưu lượng.",
      "The most common mechanical flow meters are inserted into a pipe and use a turbine, wheel or "
      "paddle to measure velocity and then calculate volumetric flow by knowing the cross section area "
      "of the pipe in which they are installed. The most common type of the above listed mechanical "
      "flow meters utilizes a turbine that rotates as the flow of water applies a force to the blades. "
      "The rotation of the turbine is proportional to the velocity of the fluid moving past it. Once "
      "the velocity is known, the flow can be calculated.")
    P("Các đồng hồ cơ khí khác dùng cùng nguyên lý cơ khí cơ bản để đo lưu lượng. Chúng làm việc "
      "hiệu quả nhất khi dùng trong ống đầy và ở khu vực có dòng ổn định, ít hoặc không có nhiễu "
      "loạn. Đồng hồ cơ khí chạy được với mọi loại chất lỏng, nhưng dễ bị tắc và suy giảm hiệu "
      "năng do chất rắn tích tụ trên cánh tuabin. Chúng cũng chiếm một phần dòng chảy và cần bảo "
      "trì định kỳ cho bánh răng và các bộ phận chuyển động.",
      "Other mechanical meters use the same basic mechanical principles to measure flow. They operate "
      "most effectively when used in a full pipe and in an area with stable flow and little-to-no "
      "turbulence. Mechanical flow meters will operate in all types of liquids, but are prone to "
      "clogging and deteriorating performance due to solids accumulating on the turbine blades. They "
      "also obstruct a portion of the flow and require regular maintenance of the gears and moving parts")

    # -------------------- Positive Displacement Meter
    H("Đồng hồ đo thể tích", "Positive Displacement Meter", h3)
    P("Đồng hồ lưu lượng thể tích được dùng để đo và điều khiển tốc độ chuyển động của chất lỏng "
      "hoặc khí. Ví dụ, đồng hồ thể tích được dùng trong thiết bị y tế để điều khiển đầu ra của "
      "hóa chất hoặc thuốc, hoặc trong thiết bị chế biến thực phẩm cần độ chính xác hệ thống. "
      "Đồng hồ chia chất khí hoặc chất lỏng cần đo thành từng gói thể tích bằng nhau gọi là parcel, "
      "được đếm khi đi qua đồng hồ. Đồng hồ thể tích có hai bộ phận chính: một buồng làm ngừng dòng "
      "khí hoặc chất lỏng, và một cơ chế chỉ cho một lượng xác định đi qua tại một thời điểm. Lưu "
      "lượng qua đồng hồ phụ thuộc vào số gói được phép đi qua cùng lúc.",
      "A positive displacement flow meter is used to measure and control the rate at which a fluid or "
      "gas is moving. For example, displacement flow meters are used in medical devices that control "
      "the output of a chemical or medication or in food-processing devices that need systematic "
      "precision. A flow meter divides the gas or fluid being measured into individual packets of "
      "equal volume, called parcels, that are counted as they pass through the meter. A displacement "
      "meter has two main parts: a chamber that stops the flow of the gas or liquid and a mechanism "
      "that allows only a specific amount to pass through at a time. The flow rate of the gas or fluid "
      "through the displacement meter depends on how many of the parcels are allowed to pass through "
      "at one time.")
    P("Có hai loại chính của đồng hồ lưu lượng thể tích. Loại thứ nhất gọi là đồng hồ thể tích chỉ "
      "cảm biến. Đây là một dạng công tắc giải phóng một lượng thể tích nhất định của chất lỏng hoặc "
      "khí mà không kèm thông tin gì thêm. Loại thứ hai được xem là hệ thống cảm biến hoàn chỉnh, "
      "gồm giao diện người dùng hoặc màn hình cung cấp thêm thông tin về áp suất vận hành, mật độ "
      "chất lỏng hoặc khí và phần trăm sai số của thiết bị. Một số đồng hồ còn có thể kèm báo động "
      "hoặc lịch sử lưu lượng.",
      "There are two main types of positive displacement flow meters. The first is called a sensor-only "
      "displacement flow meter. This type of displacement meter is a type of switch that releases a "
      "certain amount of volume of the liquid or gas without any additional information. The second "
      "type of meter is considered to be a complete sensor system, and it includes a user interface or "
      "a display that gives the user more information about the operating pressure, the density of the "
      "fluid or gas and the percent accuracy of the device. Some displacement flow meters might also "
      "include alarms or flow history information.")
    P("Bộ phận đo của đồng hồ thể tích có thể dùng nhiều công nghệ. Đồng hồ bánh răng dùng các bánh "
      "răng quay ăn khớp để mở van tại các khoảng bằng nhau sao cho đúng kích thước và thể tích gói "
      "chất đi qua. Đồng hồ xoáy tính vận tốc chất lỏng hoặc khí bằng cách xác định tần suất các mảnh "
      "vật liệu thử rơi vào dòng. Loại phổ biến nhất dùng thiết bị gọi là đồng hồ đĩa dao động "
      "(nutating disc). Trong các đồng hồ này, áp suất của gói chất làm quay một đĩa bên trong đồng "
      "hồ, và bộ đếm theo dõi số vòng đĩa đã quay để điều khiển lưu lượng.",
      "The metering portion of the displacement meter can operate with a variety of technologies. Gear "
      "meters use rotating, interlocking gears to turn the valve at equal intervals so that the correct "
      "parcel size and volume flows through. Vortex meters actually calculate the velocity of the gas "
      "or liquid by determining how frequently pieces of a test material shed into the flow. The most "
      "common type of displacement meter uses a device called a nutating disc meter. In these "
      "displacement flow meters, the pressure of the parcel rotates a disc inside the meter, and a "
      "counter keeps track of how many rotations the disc has made as a means of controlling the flow.")
    P("Đồng hồ lưu lượng thể tích có cả mẫu tương tự và kỹ thuật số. Mẫu tương tự có thể có tín hiệu "
      "đầu ra dạng sine, xung hoặc tần số AM/FM. Mẫu kỹ thuật số thường dùng giao thức RS232, RS422 "
      "hoặc RS485. Cũng có mẫu dùng giao thức song song với bus giao diện đa năng (GPIB).",
      "Positive displacement flow meters are available in both analog and digital models. Analog "
      "models can have output signals in sine wave, pulse wave or AM or FM frequencies. Digital models "
      "are commonly made with Recommended Standard 232 (RS232), RS422 or RS485 protocols. A parallel "
      "protocol model with a general-purpose interface bus (GPIB) also is available.")

    # -------------------- Positive Displacement pump
    H("Bơm thể tích", "Positive Displacement pump", h3)
    P("Bơm thể tích làm chất lỏng chuyển động bằng cách bẫy một lượng cố định rồi ép (đẩy) thể tích "
      "đó vào ống xả, hoặc bơm thể tích có buồng giãn ra ở phía hút và buồng co lại ở phía xả. "
      "Chất lỏng chảy vào bơm khi buồng phía hút giãn ra và chảy ra ở cổng xả khi buồng co lại. "
      "Thể tích là không đổi cho mỗi chu kỳ vận hành.",
      "A positive displacement pump causes a fluid to move by trapping a fixed amount of it then "
      "forcing (displacing) that trapped volume into the discharge pipe or A positive displacement "
      "pump has an expanding cavity on the suction side and a decreasing cavity on the discharge side. "
      "Liquid flows into the pump as the cavity on the suction side expands and the liquid flows out of "
      "the discharge as the cavity collapses. The volume is constant given each cycle of operation.")
    P("Bơm thể tích được phân loại tiếp theo cơ chế dùng để chuyển chất lỏng:",
      "A positive displacement pump can be further classified according to the mechanism used to "
      "move the fluid:")
    P("Dạng quay, bánh răng trong, vít, khối con thoi, cánh mềm hoặc cánh trượt, piston ngoại vi, "
      "rễ vít xoắn (ví dụ bơm Wendelkolben) hoặc bơm chân không vòng chất lỏng. Bơm quay thể tích "
      "dùng nguyên lý quay để chuyển chất lỏng. Chân không do sự quay của bơm tạo ra sẽ bắt và hút "
      "chất lỏng. Bơm quay rất hiệu quả vì tự loại bỏ không khí khỏi đường ống, không cần xì khí "
      "thủ công.",
      "Rotary-type, internal gear, screw, shuttle block, flexible vane or sliding vane, circumferential "
      "piston, helical twisted roots (e.g. the Wendelkolben pump) or liquid ring vacuum pumps. Positive "
      "displacement rotary pumps are pumps that move fluid using the principles of rotation. The vacuum "
      "created by the rotation of the pump captures and draws in the liquid. Rotary pumps are very "
      "efficient because they naturally remove air from the lines, eliminating the need to bleed the "
      "air from the lines manually.")
    P("Bơm quay thể tích cũng có điểm yếu. Do bản chất của bơm, khe hở giữa bộ phận quay và mép ngoài "
      "phải rất nhỏ, đòi hỏi bơm quay chậm và đều. Nếu chạy ở tốc độ cao, chất lỏng sẽ gây mòn. Bơm "
      "quay bị mòn dần sẽ có khe hở rộng ra, cho chất lỏng trượt qua và làm giảm hiệu suất.",
      "Positive displacement rotary pumps also have their weaknesses. Because of the nature of the "
      "pump, the clearance between the rotating pump and the outer edge must be very close, requiring "
      "that the pumps rotate at a slow, steady speed. If rotary pumps are operated at high speeds, the "
      "fluids will cause erosion. Rotary pumps that experience such erosion eventually show signs of "
      "enlarged clearances, which allow liquid to slip through and detract from the efficiency of the pump.")
    P("Bơm quay thể tích gồm ba loại chính. Bơm bánh răng là loại đơn giản nhất, gồm hai bánh răng đặt "
      "cạnh nhau ăn khớp. Hai bánh quay tách ra, tạo dòng bẫy chất lỏng giữa các răng và vỏ, rồi "
      "nhả chất ở phía xả khi răng ăn khớp và quay tiếp. Nhiều răng nhỏ duy trì dòng liên tục, trong "
      "khi ít răng lớn hơn có xu hướng xả theo từng đợt ngắn, giật cục.",
      "Positive displacement rotary pumps can be grouped into three main types. Gear pumps are the "
      "simplest type of rotary pumps, consisting of two gears laid out side-by-side with their teeth "
      "enmeshed. The gears turn away from each other, creating a current that traps fluid between the "
      "teeth on the gears and the outer casing, eventually releasing the fluid on the discharge side of "
      "the pump as the teeth mesh and go around again. Many small teeth maintain a constant flow of "
      "fluid, while fewer, larger teeth create a tendency for the pump to discharge fluids in short, "
      "pulsing gushes.")
    P("Bơm vít là loại phức tạp hơn, gồm hai hoặc ba vít có ren ngược chiều — một vít quay cùng chiều "
      "kim đồng hồ, vít kia ngược lại. Mỗi vít lắp trên trục song song; các trục cũng có bánh răng "
      "ăn khớp để quay cùng nhau và giữ vị trí. Sự quay của vít và trục hút chất lỏng qua bơm. Như "
      "các dạng bơm quay khác, khe hở giữa bộ phận chuyển động và vỏ bơm là rất nhỏ.",
      "Screw pumps are a more complicated type of rotary pumps, featuring two or three screws with "
      "opposing thread that is, one screw turns clockwise, and the other counterclockwise. The screws "
      "are each mounted on shafts that run parallel to each other; the shafts also have gears on them "
      "that mesh with each other in order to turn the shafts together and keep everything in place. The "
      "turning of the screws, and consequently the shafts to which they are mounted, draws the fluid "
      "through the pump. As with other forms of rotary pumps, the clearance between moving parts and "
      "the pump's casing is minimal.")
    P("Bơm cánh chuyển động là loại thứ ba, gồm rôto hình trụ được bao trong vỏ cùng hình dạng. Khi "
      "rôto quay, các cánh bẫy chất lỏng giữa rôto và vỏ, hút chất qua bơm.",
      "Moving vane pumps are the third type of rotary pumps, consisting of a cylindrical rotor encased "
      "in a similarly shaped housing. As the rotor turns, the vanes trap fluid between the rotor and "
      "the casing, drawing the fluid through the pump.")
    P("Dạng qua lại, ví dụ bơm piston hoặc bơm màng. Bơm thể tích có buồng giãn ra ở phía hút và buồng "
      "co lại ở phía xả. Chất lỏng vào bơm khi buồng hút giãn ra và ra ở cổng xả khi buồng co lại. "
      "Thể tích không đổi cho mỗi chu kỳ. Bơm thể tích chia thành hai nhóm chính:",
      "Reciprocating-type, for example, piston or diaphragm pumps. Positive displacement pumps have an "
      "expanding cavity on the suction side and a decreasing cavity on the discharge side. Liquid flows "
      "into the pumps as the cavity on the suction side expands and the liquid flows out of the discharge "
      "as the cavity collapses. The volume is constant given each cycle of operation. The positive "
      "displacement pumps can be divided into two main classes")
    U(["Qua lại", "Quay"], ["Reciprocating", "Rotary"])
    P("Nguyên lý thể tích áp dụng cho dù bơm là",
      "The positive displacement principle applies whether the pump is a")
    U(["Bơm thùy quay", "Bơm buồng tiến triển", "Bơm bánh răng quay", "Bơm piston",
       "Bơm màng", "Bơm vít", "Bơm bánh răng", "Bơm thủy lực", "Bơm cánh",
       "Bơm tái sinh (ngoại vi)", "Bơm nhu động"],
      ["Rotary lobe pump", "Progressive cavity pump", "Rotary gear pump", "Piston pump",
       "Diaphragm pump", "Screw pump", "Gear pump", "Hydraulic pump", "Vane pump",
       "Regenerative (peripheral) pump", "Peristaltic Pump"])
    P("Khác với bơm ly tâm hoặc bơm động quay, bơm thể tích tạo cùng một lưu lượng ở một tốc độ đã "
      "cho (RPM) bất kể áp suất xả.",
      "Positive displacement pumps, unlike centrifugal or roto-dynamic pumps, will produce the same "
      "flow at a given speed (RPM) no matter what the discharge pressure.")
    P("Bơm thể tích là “máy dòng không đổi”.",
      "Positive displacement pumps are “constant flow machines”")
    P("Không được vận hành bơm thể tích khi van ở phía xả đóng, vì bơm không có cột áp ngắt như bơm "
      "ly tâm. Bơm chạy với van xả đóng sẽ tiếp tục tạo dòng cho đến khi áp suất đường xả tăng tới "
      "mức đường ống vỡ hoặc bơm hư hỏng nặng — hoặc cả hai. Vì vậy cần một van an toàn/xả áp ở phía "
      "xả. Van xả có thể ở trong hoặc ở ngoài. Nhà sản xuất thường có tùy chọn cung cấp van an toàn "
      "bên trong. Nhìn chung van trong chỉ nên dùng như biện pháp an toàn dự phòng; nên dùng van xả "
      "ngoài lắp trên đường xả có đường về phía hút hoặc bể cấp.",
      "A positive displacement pump must not be operated against a closed valve on the discharge side "
      "of the pump because it has no shut-off head like centrifugal pumps. A positive displacement pump "
      "operating against a closed discharge valve, will continue to produce flow until the pressure in "
      "the discharge line are increased until the line bursts or the pump is severely damaged - or "
      "both. A relief or safety valve on the discharge side of the positive displacement pump is "
      "therefore necessary. The relief valve can be internal or external. The pump manufacturer "
      "normally has the option to supply internal relief or safety valves. The internal valve should "
      "in general only be used as a safety precaution, an external relief valve installed in the "
      "discharge line with a return line back to the suction line or supply tank is recommended.")

    # -------------------- Reciprocating pumps
    H("Bơm qua lại", "Reciprocating pumps", h3)
    P("Bơm qua lại điển hình là", "Typical reciprocating pumps are")
    U(["Bơm piston chìm (plunger)", "Bơm màng"], ["Plunger pumps", "Diaphragm pumps"])
    P("Bơm plunger gồm một xi lanh với plunger qua lại bên trong. Van hút và van xả lắp ở đầu xi "
      "lanh. Ở hành trình hút, plunger lùi lại và van hút mở, hút chất lỏng vào xi lanh. Ở hành "
      "trình tiến, plunger đẩy chất lỏng qua van xả. Chỉ với một xi lanh, dòng chất lỏng thay đổi "
      "từ cực đại khi plunger đi qua vị trí giữa đến zero khi plunger ở hai đầu. Nhiều năng lượng "
      "bị lãng phí khi chất lỏng được gia tốc trong hệ thống ống. Dao động và “búa nước” có thể là "
      "vấn đề nghiêm trọng. Nhìn chung các vấn đề này được bù bằng cách dùng hai hoặc nhiều xi lanh "
      "không làm việc cùng pha. Ở bơm màng, plunger ép dầu thủy lực dùng để uốn màng trong xi lanh "
      "bơm. Van màng được dùng để bơm chất nguy hại và độc hại. Một ví dụ về bơm thể tích piston "
      "là bơm xà phòng tay thông thường.",
      "A plunger pump consists of a cylinder with a reciprocating plunger in it. The suction and "
      "discharge valves are mounted in the head of the cylinder. In the suction stroke the plunger "
      "retracts and the suction valves open causing suction of fluid into the cylinder. In the forward "
      "stroke the plunger pushes the liquid out of the discharge valve. With only one cylinder the "
      "fluid flow varies between maximum flow when the plunger moves through the middle positions, and "
      "zero flow when the plunger is at the end positions. A lot of energy is wasted when the fluid is "
      "accelerated in the piping system. Vibration and “water hammer” may be a serious problem. In "
      "general the problems are compensated for by using two or more cylinders not working in phase "
      "with each other. In diaphragm pumps, the plunger pressurizes hydraulic oil which is used to "
      "flex a diaphragm in the pumping cylinder. Diaphragm valves are used to pump hazardous and toxic "
      "fluids. An example of the piston displacement pump is the common hand soap pump.")

    # -------------------- Reciprocating piston
    H("Piston qua lại", "Reciprocating piston", h3)
    P("Động cơ qua lại, còn gọi là động cơ piston, thường là động cơ nhiệt (dù cũng có động cơ qua "
      "lại khí nén và thủy lực) dùng một hoặc nhiều piston qua lại để chuyển áp suất thành chuyển "
      "động quay.",
      "A reciprocating engine, also often known as a piston engine, is typically a heat engine "
      "(although there are also pneumatic and hydraulic reciprocating engines) that uses one or more "
      "reciprocating pistons to convert pressure into a rotating motion.")
    FIG(3, F.fig_f03())
    P("Đồng hồ piston qua lại là cũ nhất trong các đồng hồ thể tích. Nó được dùng rộng rãi trong "
      "công nghiệp dầu khí. Cấu tạo rất giống piston và xi lanh của động cơ hơi nước qua lại. Đồng "
      "hồ gồm một xi lanh gang lắp piston, như Hình 3. Hai van trượt gắn ở cổng vào và cổng ra. Chất "
      "lỏng cần đo vào qua cổng vào, đẩy piston sang trái cho tới khi xi lanh đầy và piston ở vị trí "
      "cực trái. Lúc đó một rò rỉ ngoài làm cả hai van trượt dịch chuyển, chất lỏng vào xi lanh bên "
      "trái đẩy piston sang vị trí cực phải. Khi xi lanh đầy, van trượt lại dịch và chu kỳ lặp lại. "
      "Cánh tay ngoài của van trượt dẫn động bộ đếm cho tổng lượng chất đã đi qua đồng hồ. Thay vì "
      "một piston, loại đồng hồ này thường gồm nhiều piston cùng làm việc trên một trục khuỷu "
      "giữa. Đồng hồ bơm qua lại có nhiều dạng như đồng hồ đa piston, đồng hồ piston tác động kép, "
      "van quay và van trượt ngang. Độ chính xác của các đồng hồ này từ ±0,2 đến ±0,3%.",
      "The reciprocating piston meter is the oldest of the positive displacement meters. It is widely "
      "used in petroleum industry. It is very similar in construction to a reciprocating steam engine "
      "piston and cylinder. It consists of a cast iron cylinder fitted with a piston, as shown in Fig. "
      "3. Two slide valves are attached at the inlet and outlet ports. The fluid to be measured enters "
      "through the inlet forcing the piston to the left until the cylinder is full and piston is in its "
      "extreme left position. At this point, an external leakage causes both slide valves to move and "
      "thus the liquid enters the left cylinder forcing the piston to its extreme right position. When "
      "the cylinder be-comes full, the slide valves again move and the cycle is repeated. The external "
      "arm of the slide valve drives a counter which pro-vides a total of the fluid quantity that has "
      "passed through the meter. Instead of one piston, a number of pistons operating on a center crank "
      "are generally incorporated with this type of meter. Reciprocating pump meters are available in "
      "many forms such as multi-piston meters, double-acting piston meters, rotary valves, and "
      "horizontal slide valves. The accuracy of these meters are from ±0.2 to ±0.3%.")
    P("Trong đồng hồ piston qua lại minh họa bằng Hình 4, piston cho chất lỏng đi xen kẽ qua từng đầu "
      "xi lanh từ cổng vào tới cổng ra; van trượt điều khiển hai cổng và vận hành bộ đếm. Loại đồng "
      "hồ này thường gồm nhiều piston làm việc trên trục khuỷu giữa. Với lưu lượng nhỏ, chênh áp "
      "rất nhỏ, người ta chọn piston đường kính lớn và hành trình ngắn với ma sát tối thiểu. Độ "
      "chính xác của đồng hồ này trong vòng 0,5%.",
      "In the reciprocating piston meter shown schematically in Fig. 4, the reciprocating piston passes "
      "the liquid alternately through each end of the cylinder from the inlet to the outlet and also "
      "the slide valve which controls the inlet and outlet ports and operates the counter. A number of "
      "piston operations on a center crank are generally incorporated in this type of meter. For low "
      "flow, the differential pressure is small, for which large diameter pistons and small piston "
      "strokes are chosen with minimum of friction. Accuracy of this flow meter is within 0.5%.")
    FIG(4, F.fig_f04())
    H("Ưu điểm", "Advantages", h4)
    P("Ưu điểm của đồng hồ piston qua lại là: (i) độ chính xác cao; (ii) vật liệu chế tạo không bị "
      "giới hạn.",
      "The advantages of reciprocating piston meters are: (i) Its accuracy is high. (ii) Construction "
      "materials are not limited in reciprocating piston meters.")
    H("Hạn chế", "Limitations", h4)
    P("Hạn chế của đồng hồ piston qua lại là:",
      "The limitations of reciprocating piston meters are:")
    U(["(i) Chi phí tương đối cao.",
       "(ii) Dễ bị rò rỉ.",
       "(iii) Chất lỏng bẩn gây vấn đề.",
       "(iv) Cần chi phí bảo trì cao.",
       "(v) Chỉ dùng cho lưu lượng trung bình.",
       "(vi) Tạo dòng xung khi đo chất lỏng."],
      ["(i)  Their cost is relatively high.",
       "(ii)  They are subject to leakage.",
       "(iii)  Problems are created by dirty fluids.",
       "(iv)  It requires high maintenance cost.",
       "(v)  It is restricted to moderate flow rates.",
       "(vi)  It produces pulsating flow when used for liquid measurement."])

    # -------------------- Nutating disc meter
    H("Đồng hồ đĩa dao động", "Nutating disc meter", h3)
    P("Đồng hồ đĩa dao động là loại phổ biến và chính xác nhất trong các đồng hồ thể tích. Nguyên "
      "lý hoạt động đơn giản và đáng tin cậy cho nước chảy vào buồng, làm đĩa dao động (nutate). Mỗi "
      "lần đĩa dao động tương ứng một lượng nước cố định, nên tổng lưu lượng được tính bằng tổng số "
      "lần dao động.",
      "Nutating disc meters are the most common and accurate type of positive displacement meters. The "
      "simple and reliable operating principle allows water to flow into the chamber, which causes the "
      "disc to nutate. Each disc nutation represents a fixed quantity of water, so the total flow is "
      "calculated by the total number of nutations.")
    P("Hình trên cho thấy sơ đồ đồng hồ đĩa dao động. Đồng hồ gồm buồng gia công chính xác, một bi "
      "tâm, đĩa di động và cơ chế đếm. Đĩa liên kết với bi/quả cầu lắp trong buồng. Một chốt nhỏ gắn "
      "vào bi để chuyển chuyển động dao động/quay lệch tâm của bi thành chuyển động quay của trục. "
      "Đĩa được bản lề tại tâm hình học và được phép dao động hoặc lắc trong một buồng thiết kế "
      "riêng. Khe hở được kiểm soát giữa đĩa và buồng bảo đảm làm kín và rò rỉ tối thiểu.",
      "Above figure shows the schematic diagram of nutating disc meter. It consists of a precision "
      "machined chamber, a center ball, movable disc, and counter mechanism. The disc is integral to "
      "the ball/sphere mounted inside the chamber. A small pin is fastened to the ball to convert "
      "nutating motion/ eccentric spinning motion of the ball into rotary motion of the shaft. The disc "
      "is pivoted at the geometric center, and it is allowed to nutate or wobble in a specially "
      "designed chamber. The controlled clearance between the disc and chamber ensures the proper "
      "sealing and minimum leakage.")
    P("Đĩa chia buồng thành hai thể tích bằng nhau. Trong hình trên, nước vào phía trái của đĩa lắp "
      "lệch tâm. Áp suất chất lỏng đưa đĩa vào chuyển động, làm lượng chất vào phía trái buồng được "
      "đẩy ra qua cổng ra. Khi đĩa và bi lắc, chúng tạo một hình nón với đỉnh tại tâm hình học; "
      "chuyển động này được chốt gắn trên bi chuyển thành chuyển động quay của trục. Chuyển động của "
      "đĩa sau đó truyền qua cam và hệ bánh răng tới bộ tổng hoặc bộ phát xung. Mỗi chu kỳ dao động "
      "hoàn chỉnh của đĩa được cơ chế đếm ghi nhận và có thể hiệu chuẩn trực tiếp theo thể tích chất "
      "lỏng nhận vào hoặc xả ra. Mỗi vòng quay của đĩa biểu thị sự đi qua của một thể tích chất lỏng "
      "cố định. Có thể thêm nhiều phụ kiện thứ cấp thực hiện chức năng bổ sung cho cơ chế cơ bản này, "
      "ví dụ thiết bị đặt lại số đếm.",
      "The disc divides the chamber into two equal volume. In above fig, water enters at the left side "
      "of the eccentrically mounted disc. The liquid pressure sets the disc in motion, results in the "
      "quantity of liquid that enters left side of the chamber will be rolled out through the outlet. "
      "When the disc and ball wobble it generate a cone with the apex at geometric center, this motion "
      "is getting translated into a rotary motion of shaft by the pin fastened to the ball. The movement "
      "of the disc is then transmitted by the cam and gear train to the totalizer or pulse transmitter. "
      "Each complete cycle of nutation of the disc will be counted by the counter mechanism which can "
      "be directly calibrated in terms of volume of liquid received or discharged. Each revolution of "
      "disc indicates the passage of fixed volume of fluid. A variety of secondary accessories, which "
      "perform additional functions, can be added to this fundamental mechanism. For example, Count "
      "resetting device.")
    P("Đồng hồ này, còn gọi là đồng hồ đĩa (disk meter), được dùng rộng rãi cho cấp nước dân cư. Cụm "
      "chuyển động tách chất lỏng thành các phần tử gồm một đĩa có khe hướng tâm với ổ bi tích hợp "
      "và một chốt trục. Hình 5 cho thấy đồng hồ dạng đĩa dao động.",
      "This meter, also known as disk meter, is used extensively for residential water service. The "
      "moving assembly, which separates the fluid into increments consists of an assembly of a "
      "radially slotted disk with an integral ball bearing and an axial pin. Fig. 5 shows the nutating "
      "disk type meter.")
    FIG(5, F.fig_f05())
    P("Bộ phận này lắp vào và chia buồng đo thành bốn thể tích: hai ở phía trên đĩa ở phía vào và hai "
      "ở phía dưới đĩa ở phía ra. Khi chất lỏng cố chảy qua đồng hồ, sụt áp từ đầu vào tới đầu ra làm "
      "đĩa lắc hoặc dao động, và mỗi chu kỳ cho một thể tích bằng thể tích buồng đo trừ đi thể tích "
      "cụm đĩa. Đầu chốt trục chuyển động theo vòng tròn dẫn động một cam nối với hệ bánh răng và bộ "
      "đếm tổng.",
      "This part fits into and divides the metering chamber into four volumes, two above the disk on the "
      "inlet side and two below the disk on the outlet side. As the liquid attempts to flow through the "
      "meter, the pressure drop from inlet to outlet causes the disk to wobble or nutate, and for each "
      "cycle to display a volume equal to the volume of the metering chamber minus the volume of the "
      "disk assembly. The end of the axial pin, which moves in a circular motion, drives a cam that is "
      "connected to a gear train and the totalizing register.")
    P("Độ sai: ±1 đến 2%. Dải nhiệt độ: –150 đến 120°C. Áp suất làm việc tối đa: 10 kg/cm².",
      "Inaccuracy : ± 1 to 2%. Temperature range : – 150 to 120°C. Max working pressure : 10 kg/cm2.")
    H("Ứng dụng", "Application", h4)
    U(["Kiểm soát thể tích chính xác chất lỏng công nghiệp là nhu cầu kinh tế do giá trị cao của các "
       "sản phẩm này. Thiết kế và vật liệu của đồng hồ thể tích phải phù hợp với điều kiện vận hành "
       "và tính chất của chất lỏng đo.",
       "Đồng hồ thể tích đĩa dao động RRF đáp ứng mọi yêu cầu đó, dùng cho nhiên liệu dầu như dầu "
       "lò, dầu diesel nhẹ, diesel tốc độ cao, dầu hỏa..., và các chất lỏng cuối như dung môi, axit, "
       "hỗn dịch, sơn, mật rỉ và nhựa đường nóng.",
       "Đồng hồ RRF có cỡ từ ½” đến 6”, công suất 5 đến 12.000 lít/giờ, độ nhớt tới 12.000 cP, "
       "phù hợp từ nước và carbon tetrachloride đến mật rỉ đặc và nhựa đường. Thiết kế chịu áp tới "
       "50 kg/cm² và nhiệt độ tới 2040C (OCR).",
       "Đồng hồ chất lỏng RRF dùng cho nhiều mục đích đo và điều khiển như bốc xếp xe tăng và xe "
       "tải, xác định chi phí, tìm hiệu suất thiết bị...",
       "Với thay đổi vật liệu chế tạo, đồng hồ có thể đo bất kỳ chất lỏng sạch nào, dù ăn mòn hay "
       "không ăn mòn."],
      ["An accurate volumetric control of industrial liquids is an economic necessity in view of the "
       "high value of these products. The design and material of volumetric meters must be adapted to "
       "the particular operating condition and the properties of the measured liquids.",
       "RRF Nutating Disc P.D. meter meet all these requirements. They are used for Petroleum fuel such "
       "as: Furnace Oil, Light Diesel Oil, High Speed Diesel, Kerosene etc. and final liquids such as "
       "Solvents, Acids, Dispertions, Paint, Molasses, and Tar Hot Water etc.",
       "RRF meters, available in size ½ “ to 6” covering capacities from 5 to 12,000 litres per hour, "
       "viscosity rating upto 12,000 CpS provide for liquids from water and Carbon Tetra Chloride to "
       "thick Molasses and Road Tar. It is Suitable for operating pressures upto 50 kgs/cm2 and "
       "temperatures upto 2040C.",
       "RRF liquid meters are used for a multitude of matering and control purpose e.g. loading/unloading "
       "of tankers and lorries, determine costs, finding out efficiency of equipment etc.",
       "With change in materials of construction, the meter can be used for measurement of any clean "
       "liquid, whether corrosive or non- corrosive."])
    H("Thiết kế và vận hành", "Design &amp; Operation", h4)
    P("Thiết kế dựa trên nguyên lý thể tích đã được chứng minh quốc tế: đĩa dao động cô lập một thể "
      "tích chất lỏng cố định và truyền chuyển động tới bộ tổng qua cấu trúc chắc chắn. Vì vậy đồng "
      "hồ dùng cho ứng dụng công nghiệp nặng. Do đĩa có tác động lăn, tổn thất cột áp rất nhỏ, nên "
      "đồng hồ chạy tốt với cột áp trọng lực hoặc ở phía hút và phía xả của bơm.",
      "The meter design is based on internationally proven positive displacement nutating disc isolates "
      "a fixed volume of liquid and the motion is transmitted to the totaliser through sturdy in "
      "construction and operating. Heance these meters are used for heavy duty industrial applications. "
      "Since the disk has a rolling actions, it causes a very low head loss in the flow of the liquid. "
      "Hence these meters can easily work on gravity head or on suction side and delivery of the pump.")
    H("Đặc điểm chính", "Major Features", h4)
    U(["Độ chính xác và khả năng lặp lại cao với sụt áp thấp.",
       "Vật liệu chế tạo có thể thay đổi cho phù hợp chất lỏng đo.",
       "Dải đo rộng cho các độ nhớt khác nhau — phù hợp độ nhớt cao.",
       "Dễ tháo rời và vệ sinh mà không cần tháo đồng hồ khỏi đường ống."],
      ["High accuracy and repeatability with low pressure drop.",
       "Materials of construction changeable to suit the measured liquid.",
       "Large metering range for varying viscosities – suitable for high viscosities.",
       "Easy dismantling and cleaning without removing the meter from the pipe work."])

    # -------------------- Oscillating piston meter
    H("Đồng hồ piston dao động", "Oscillating piston meter", h3)
    P("Đồng hồ piston dao động giống đồng hồ đĩa dao động, khác ở chỗ bộ phận đo là một vòng chia "
      "(split ring) chỉ dao động trong một mặt phẳng. Đồng hồ gồm một hình trụ có khe dao động quanh "
      "một cầu ngăn giữa cổng vào và cổng ra. Hình 6 cho thấy chu kỳ vận hành. Trình tự đo bắt đầu ở "
      "vị trí 1 (Hình 6), piston ở vị trí trung tính. Chất lỏng vào qua cổng vào đẩy piston sang đầu "
      "trái và làm nó lăn xuống (ngược chiều kim đồng hồ) như vị trí 2. Chuyển động này ép chất lỏng "
      "phía trái piston ra qua cổng ra. Ở vị trí 2, hầu hết bề mặt piston chịu tác động của dòng vào "
      "và bị đẩy thẳng đứng xuống như vị trí 3; chất lỏng vào khoảng giữa buồng trong và thành trong "
      "của piston để tạo chuyển động liên tục êm. Sự quay của piston truyền qua một màng tới hệ bánh "
      "răng và bộ đếm.",
      "The oscillating piston meter is similar to the nutating disc meter except that the measurement "
      "device is a split ring which oscillates in one plane only. It consists of a slotted cylinder "
      "which oscillates about a dividing bridge that separates the inlet port from the outlet port. "
      "Figure 6 shows the operational cycle of the meter. The measuring sequence starts with the "
      "position 1 (Fig. 6) where the piston is in the neutral position. Fluid enters through the inlet "
      "port into the chamber and forces the piston to the left end causing it to roll downward "
      "(counter-clockwise) as in position 2. This movement of the piston forces the liquid in the left "
      "side of the piston to be discharged through the outlet port. At position 2, most of the piston "
      "surface is under the influence of incoming fluid and is driven vertically downward as shown in "
      "position 3, and liquid enters the space between the inner chamber and the inside wall of the "
      "piston to give a continuous smooth motion to the piston. The rotation of the piston is "
      "transmitted through a diaphragm to the gear train and register.")
    FIG(6, F.fig_f06())
    P("Ngoài cấp nước dân cư, loại đồng hồ này còn xử lý được chất lỏng sạch có độ nhớt và chất ăn "
      "mòn. Nhìn chung dùng cho đường ống nhỏ cỡ 50 mm hoặc nhỏ hơn để đo lưu lượng thấp. Độ chính "
      "xác trong khoảng ±1%. Giá phụ thuộc vào kích cỡ và vật liệu chế tạo.",
      "This type of meter, in addition to the residential water purposes, has the capacity of handling "
      "clean viscous and corrosive liquids. Generally, oscillating piston meters are used in small "
      "pipelines of sizes 50 mm or smaller to measure low flow rates. The accuracy of this type of "
      "meter is in the range of ±1%. Cost of this meter depends upon size and materials of construction.")
    H("Avantages", "Avantages", h4)
    P("Ưu điểm của đồng hồ piston dao động (giữ nguyên tiêu đề “Avantages” từ nguồn):",
      "The advantages of oscillating piston meter are (the source heading “Avantages” is kept):")
    U(["(i) Độ chính xác tốt, nhất là ở lưu lượng thấp.",
       "(ii) Dễ áp dụng cho hệ thống định lượng chất lỏng tự động.",
       "(iii) Khả năng lặp lại tốt.",
       "(iv) Dễ lắp đặt và bảo trì.",
       "(v) Chi phí trung bình."],
      ["(i)  Its accuracy is good especially at low flow rates.",
       "(ii)  It can be easily applied to automatic liquid batching system.",
       "(iii)  It has good repeatability.",
       "(iv)  It is easy to install and maintain.",
       "(v)  Its cost is moderate."])

    # -------------------- Oval gear meters
    H("Đồng hồ bánh răng oval", "Oval gear meters", h3)
    P("Đồng hồ lưu lượng bánh răng oval là đồng hồ thể tích (PD) cơ khí truyền thống, được OVAL "
      "Corporation của Nhật Bản sáng chế hơn 50 năm trước và hiện dùng rộng rãi. Đồng hồ đo lưu "
      "lượng bằng cách dùng rôto có bánh răng cho một thể tích chất lỏng đã biết đi qua thân.",
      "Oval gear flow meters are traditional, mechanical, positive displacement (PD) flow meters, first "
      "invented more than 50 years ago by OVAL Corporation of Japan and now widely used for flow "
      "metering applications. Oval gear meters measure flow by employing a geared rotor to pass known "
      "volumes of a fluid through a housing.")
    P("Một cặp bánh răng được chỉnh rất chính xác trong vỏ tạo thành bộ phận đo. Môi chất chảy vào "
      "làm cặp bánh quay. Chuyển động quay được quét bằng cảm biến không tiếp xúc. Vì mỗi răng tạo "
      "một xung, độ phân giải rất cao; ngay cả thể tích nhỏ nhất cũng được đo hoặc định lượng chính "
      "xác. Bộ đo có hai đầu dò lệch nhau theo chu vi một phần ? của bước răng (phân số bị mất trong "
      "OCR) để tạo tín hiệu tần số hai kênh tỉ lệ dòng. Xử lý tín hiệu thích hợp cho độ phân giải lớn "
      "hơn và khả năng xác định chiều dòng. Về cơ bản, độ chính xác tăng khi độ nhớt của môi chất tăng.",
      "A very precisely adjusted gear pair within the casing forms the measuring element. The inflowing "
      "medium causes the gear pair to rotate. The rotary motion is scanned by contactless sensors. "
      "Since each individual tooth generates a pulse, this results in a very high resolution. "
      "Consequently, even the smallest volumes can be measured or dosed precisely. The measurement unit "
      "contains two pick-offs that are circumferentially offset by? of a tooth pitch to generate a 2 "
      "channel flow-proportional frequency signal. Suitable processing of the signal provides a greater "
      "resolution and the option to identify the flow direction. Basically, the measurement accuracy "
      "increases with increase in viscosity of the media.")
    P("Bộ phận đo gồm hai bánh oval chính xác có răng được chất lỏng chảy qua làm quay. Số vòng quay "
      "là thước đo chính xác thể tích. Yêu cầu bảo trì và hiệu chuẩn lại rất ít vì không có bộ phận "
      "chuyển động tiếp xúc. Đồng hồ bánh răng thường được chọn thay vì Coriolis vì độ chính xác và "
      "độ bền trong môi trường khắc nghiệt, nơi Coriolis dễ bị nhiễu (interferance) do thay đổi áp "
      "suất, nhiệt độ và hao mòn chung.",
      "The measuring element of an oval gear meter consists of two toothed precision oval wheels which "
      "are driven by the fluid passing through the unit. The number of revolutions is an exact measure "
      "of the volume. Maintenance and recalibration requirements are minimal because of the lack of "
      "moving parts. Often, the gear meter is selected over the Coriolis because of its accuracy and "
      "longevity in harsh environments where the Coriolis is susceptible to interferance from pressure "
      "or temperature changes and general wear.")
    H("Ứng dụng thông thường của đồng hồ bánh răng oval",
      "Oval Gear Flow Meters – Common Applications", h4)
    U(["Sản xuất hóa chất: xút, kali hydroxit, axit acetic, nước khử khoáng.",
       "Công nghiệp thực phẩm: dung dịch đường, xi-rô, dầu, sốt, đồ uống, mật ong, mật rỉ, sữa, nước "
       "trái cây, sô-cô-la, rượu, ethanol và lớp phủ.",
       "Dược phẩm: rượu, xi-rô, glycerin và lớp phủ.",
       "Mỹ phẩm: dầu gội, gel, nước hoa và kem.",
       "Dầu khí: nhiên liệu, chất bôi trơn và dẫn xuất dầu mỏ.",
       "Nước và nước thải: hóa chất, fluoride và axit.",
       "Giấy và bột giấy: sáp, nước hoa, thuốc nhuộm và axit.",
       "In ấn: dung môi và mực.",
       "Ô tô: dầu hộp, glycol, chất làm lạnh độ nhớt thấp và dầu thủy lực.",
       "Dệt may: thuốc nhuộm, chất tẩy và hóa chất.",
       "Dầu mỏ: dầu, xăng, biodiesel, phụ gia và dầu hỏa.",
       "Sơn: sơn gốc dung môi và gốc latex.",
       "Đóng tàu: dầu bôi trơn, nhiên liệu, dầu hàng hải.",
       "Khai khoáng: dầu, nhiên liệu, chất bôi trơn.",
       "Kim loại: dầu gia nhiệt, nhiên liệu, dầu.",
       "Keo dán: keo gốc nước acrylic, dung môi, chất tẩy rửa."],
      ["Chemical Production: caustic soda, potassium hydroxide, acetic acid, demineralized water",
       "Food Industry: sugar solutions, syrups, oils, sauces, beverages, honey, molasses, milk products, "
       "juices, chocolate, alcohol, ethanol and coatings",
       "Pharmaceutical Industry: alcohols, syrups, glycerines and coatings",
       "Cosmetics Industry: shampoos, gels, perfumes and creams",
       "Oil and Gas Industry: fuels, lubricants and petro-derivatives",
       "Water and Wastewater Industry: chemicals, fluoride and acids",
       "Pulp and Paper Industries: wax finishes, perfumes, dyes and acids in the pulp and paper industries",
       "Printing: solvents and inks",
       "Automotive: transmission fluid, glycol, low viscosity climatization liquids and hydraulic oil",
       "Textiles: dyes, bleach and chemicals",
       "Petroleum Industry: oils, gasoline, biodiesel, additives and kerosene",
       "Paint: solvent and latex based paints",
       "Shipbuilding: lubricating oil, fuels ,marine oil",
       "Mining Industry: oils, fuels, lubricants",
       "Metal Industry: heating oil, fuels, oils",
       "Glue Industry: acrylic water based glue, solvents, cleaning agents"])
    H("Chiều dòng", "Flow Direction", h4)
    P("Đồng hồ bánh răng oval dạng xung đo được theo hai chiều, đo dòng theo hướng bất kỳ mà không "
      "phân biệt chiều thực của dòng. Đồng hồ dạng cơ chỉ đo một chiều và chiều đó được ghi trên thân "
      "đồng hồ. Không tuân theo hướng lắp sẽ làm bộ đếm cơ chạy ngược. Chạy ngược kéo dài có thể gây "
      "hư hỏng vĩnh viễn cơ chế đếm cơ.",
      "Pulse-Type Oval Gear meters are bi-directional and will measure flow in either direction, without "
      "distinguishing the actual direction of the flow. Mechanical-Type Oval Gear meters can only measure "
      "flow in one direction and that direction will be indicated on the body of the meter. Failure to "
      "adhere to the orientation on a mechanical flow meter will cause the mechanical counter to operate "
      "in reverse. Reverse operation for an extended period of time may cause permanent damage to the "
      "mechanical counter mechanism.")
    H("Cấu tạo đường ống", "Piping Construction", h4)
    P("Để tránh hư hỏng đồng hồ, nên cân nhắc các điểm sau khi thiết kế hoặc thi công hệ thống ống:",
      "To avoid damage to your flow meter it is recommended that the following points be considered "
      "when designing/constructing your piping system:")
    U(["Không bao giờ lắp đồng hồ bánh răng oval cỡ trung hoặc lớn ở phía hút của bơm. Có thể thiết kế "
       "hệ thống để đồng hồ cỡ nhỏ (3/8” hoặc nhỏ hơn) chạy an toàn và chính xác ở phía hút.",
       "Áp suất và nhiệt độ hệ thống phải nằm trong giới hạn an toàn. Lắp đồng hồ phía trước van "
       "điều khiển hoặc van ngắt. Áp suất ngược do van tạo ra có lợi cho độ chính xác.",
       "Với lắp đặt thẳng đứng, chất lỏng phải đi từ dưới lên trên để đồng hồ luôn đầy và tránh giữ "
       "khí. Đường ống thiết kế sao cho đồng hồ luôn đầy chất lỏng; ống vào và ống ra cao hơn mọi "
       "đường ống xung quanh.",
       "Mọi đường ống quanh đồng hồ phải được đỡ tốt tại chỗ nối với đồng hồ, đặc biệt với đồng hồ "
       "2” và lớn hơn.",
       "Không nên cho đồng hồ xả trực tiếp ra khí quyển, điều này ảnh hưởng xấu đến độ chính xác."],
      ["Never install a medium or large capacity Oval Gear meters on the suction side of a pump. "
       "Systems can be designed to safely and accurately operate a small Oval Gear meter on suction "
       "(3/8” size or smaller meter).",
       "System pressure and temperature must stay within safe limits. Install Oval Gear meters upstream "
       "of a flow control or shut-off valve. The back pressure provided by the valve will be beneficial "
       "to system accuracy.",
       "For vertical installations the liquid should travel from bottom to top. This will ensure that "
       "the flow meter remains full of liquid, and will stop air entrapment in the meter. Piping should "
       "be designed so that the flow meter is full of liquid at all times. The inlet and outlet piping "
       "for the flow meter should be higher than all surrounding piping.",
       "All piping surrounding your flow meter should be well supported where the piping joins to the "
       "flow meter. This is very important with 2” and larger flow meters.",
       "Operating a flow meter directly discharging to atmosphere is not advisable, and will be "
       "detrimental to accuracy."])
    P("Nếu đồng hồ lắp giữa hai van ngắt, cần lắp van giảm áp hoặc khớp giãn nhiệt để bảo vệ khỏi áp "
      "suất cao do thay đổi nhiệt độ. Luôn cần một đường vòng (xem Hình 7): đường này cô lập đồng hồ "
      "và lưới lọc khỏi đường chính, cho phép vệ sinh lưới nhanh chóng và bảo trì, sửa chữa dễ dàng.",
      "If your flow meter is installed between two shutoff valves, it will be necessary to install "
      "pressure relief valves, or thermal expansion joints to protect from high pressure due to "
      "temperature change. It is always important to provide a bypass line (see figure 7). This "
      "provides isolation of the flow meter and strainer from the main process line. This allows quick "
      "and easy cleaning of the strainer. This allows easy maintenance and repairs on your flow meter.")
    FIG(7, F.fig_f07())
    H("Lọc và lưới lọc", "Filtration and Straining", h4)
    P("Phải bảo đảm chất lỏng sạch, không có hạt lạ để bảo vệ đồng hồ bánh răng oval. Hạt rắn có thể "
      "có trong hệ thống từ nhiều nguồn:",
      "You must be sure your liquid is clean and 100% free of foreign particles to properly protect an "
      "Oval Gear meter. Solid particles to be present in a system from many sources:")
    U(["Bụi lắng đọng trên bồn chứa không kín.",
       "Mòn các thiết bị cơ khí thượng lưu như bơm hoặc máy khuấy.",
       "Hạt kim loại lớn từ cắt hoặc hàn khi lắp đặt mới hoặc cải tạo."],
      ["Dust settling on an unsealed storage tanks",
       "Wear on upstream mechanical devices such as pumps or mixers",
       "Large metal particles from cutting or welding on new or modified installations"])
    P("Nên lắp bộ lọc hoặc lưới lọc ở phía vào của mọi đồng hồ bánh răng oval.",
      "You should install a filter or strainer on the inlet side of any Oval Gear meter.")
    U(["Đồng hồ nhỏ 1/8” đến 3/8” (4 mm đến 8 mm): dùng lưới 200 mesh.",
       "Đồng hồ trung bình 1/2” đến 2” (15 mm đến 50 mm): dùng lưới 100 mesh.",
       "Đồng hồ lớn 3” đến 4” (80 mm đến 100 mm): dùng lưới 40 mesh."],
      ["Small Oval Gear meters, 1/8” to 3/8” (4 mm to 8 mm), require a 200 mesh strainer.",
       "Medium Oval Gear meters, 1/2” to 2” (15 mm to 50 mm), require a 100 mesh strainer.",
       "Large Oval Gear meters, 3” to 4” (80 mm to 100 mm), require a 40 mesh strainer."])
    P("Lưới kiểu Y là lựa chọn phổ biến nhất vì nhẹ nhất, nhỏ nhất và kinh tế nhất, đồng thời gây tổn "
      "thất áp suất tối thiểu.",
      "The Y-type strainer is the most common choice as it is the lightest, smallest, and most "
      "economical of the strainer types available. It also produces minimal pressure loss.")
    H("Loại bỏ không khí", "Air Elimination", h4)
    P("Cần lưu ý là đồng hồ bánh răng oval không phân biệt được chất lỏng và chất khí. Bọt khí hoặc "
      "hơi trong chất lỏng gây sai số và có thể gây hư hỏng nghiêm trọng cho đồng hồ.",
      "It’s very important point to note that Oval Gear meters cannot differentiate between liquid and "
      "gas. The presence of air bubbles or vapor in your liquid will cause measurement errors. Air "
      "bubbles or vapor can also cause major damage to your flow meter.")
    P("Nếu không tránh được không khí hoặc hơi trong chất lỏng độ nhớt thấp, nên dùng Bộ lọc tách khí "
      "(AES), luôn lắp phía trước đồng hồ. AES bắt và xả được lượng lớn không khí khi cấp liệu ban đầu. "
      "Với chất lỏng độ nhớt lớn (>100 cP) hoặc khi cần tách nhiều không khí, dùng AES công suất lớn "
      "lắp ngay sau bồn tách khí; bồn này cho chất nhớt thời gian thoát khí hoặc hơi trước khi vào đồng hồ.",
      "If air or vapor in your low viscosity liquid, cannot be avoided, an Air Eliminator Strainer (AES) "
      "is recommended. The AES should always be installed upstream of the Oval Gear meters. The AES is "
      "capable of capturing and venting large amounts of air that are found with the initial filling of "
      "the system. For large viscosity liquids (> 100cP), or where large amounts of air have to be "
      "removed from the flow stream, a large capacity AES is required. The large AES should be installed "
      "immediately downstream of a large capacity air separator tank. The air separator tank provides "
      "the necessary time for viscous liquids to release the entrained air or vapor prior to entering "
      "the flow meter.")
    H("Quy trình khởi động", "Start-Up Procedures", h4)
    P("Nguyên nhân phổ biến nhất gây hư đồng hồ bánh răng oval là quy trình khởi động không đúng sau "
      "lắp đặt hoặc cải tạo, hoặc sau thời gian dài ngừng hoạt động. Đường ống mới hoặc cải tạo thường "
      "chứa nhiều không khí.",
      "The most common cause of damage to an Oval Gear meter is improper start-up procedure after "
      "installation or modification, or after long periods of shutdown. New or modified piping is "
      "generally full of large volumes of air.")
    P("Đồng hồ mới lắp KHÔNG được chạy cho đến khi đường ống được xả sạch hoàn toàn vật lạ. Vật lạ "
      "thường gặp trong ống mới là xỉ hàn, bụi mài, băng keo/hợp chất làm kín hoặc gỉ bề mặt. Nếu có "
      "đường vòng, dễ dàng cô lập đồng hồ để xả phần lớn đường ống.",
      "The newly installed meter must NOT be run until the piping is completely flushed of foreign "
      "materials. The most common foreign matter that is present in new or modified piping is welding "
      "slag, grinding dust, sealing tape/ compound, or surface rust. If your meter has been installed "
      "with a bypass line it will be easy to isolate your flow meter from the remainder of the system "
      "in order to flush out the majority of the piping.")
    P("Nếu không có đường vòng, giải pháp tốt nhất là thay đồng hồ bằng một đoạn ống trong suốt thời "
      "gian xả. Sau khi khởi động và trong giai đoạn chạy ban đầu, nên kiểm tra định kỳ lưới lọc đầu vào.",
      "If you have not installed a bypass line around your flow meter, the best solution is to replace "
      "your meter with a spool piece for the duration of the flushing procedure. Following the start-up "
      "procedure, and during the period of initial operation, it is recommended that the inlet strainer "
      "on your flow meter be inspected regularly.")
    H("Bảo trì và vệ sinh", "Maintenance and Cleaning", h4)
    P("Đồng hồ bánh răng oval là thiết bị cơ khí nên bị hao mòn trong thời gian hoạt động. Để tối đa "
      "khả năng sẵn sàng và giảm thời gian dừng hệ thống, nên áp dụng chương trình bảo trì và kiểm tra "
      "định kỳ. Mức hao mòn bình thường phụ thuộc vào nhiều yếu tố:",
      "Oval Gear meters are a mechanical device, and as such are subject to some wear and tear over "
      "their operational life. In order to maximize the operational availability of your meter, and "
      "reduce system downtime, a periodic maintenance and inspection program should be implemented. The "
      "amount of normal wear that the meter will experience will depend on several factors.")
    U(["Lưu lượng", "Nhiệt độ quá trình", "Độ sạch của chất lỏng", "Khả năng bôi trơn của chất lỏng",
       "Thời gian chạy liên tục"],
      ["Flow Rate", "Process Temperature", "Fluid Cleanliness", "Fluid Lubricity",
       "Continuous Duty Run Time"])
    P("Trước khi bảo trì, bảo đảm các hạng mục sau đã hoàn tất:",
      "Before beginning any flow meter maintenance, ensure the following items have been completed:")
    U(["Đường ống và đồng hồ đã ngừng, giảm áp và xả hết chất lỏng.",
       "Các báo động, đầu ra điều khiển... đã được cô lập không ảnh hưởng quá trình.",
       "Nguồn điện/điện áp cấp cho đồng hồ đã được cô lập và/hoặc ngắt."],
      ["The flow line and flow meter have been shut down, de-pressurized and drained of all liquids",
       "Associated alarms, control outputs, etc., have been isolated so as not to affect the process",
       "Any power supply/voltage supplied to the meter have been isolated and/or shut down"])
    P("Bảo trì và kiểm tra định kỳ nên thực hiện mỗi 6 đến 12 tháng, nhất là lắp đặt trong điều kiện "
      "khắc nghiệt, có biến động nhiệt độ lớn hoặc chạy trên 80% công suất liên tục tối đa trong thời "
      "gian dài. Với hệ thống cần CIP (vệ sinh tại chỗ), quy trình rửa không được vượt thông số vận "
      "hành; tăng nhiệt độ nhanh hơn 50°F (10°C) mỗi phút có thể hư đầu ra công tắc reed. Cần kiểm tra "
      "tương thích hóa học của dung dịch rửa với vật liệu chế tạo đồng hồ.",
      "Periodic maintenance and inspection should occur every 6 to 12 months, especially for installations "
      "in harsh conditions. Specifically in applications with: Large Temperature Variations; Long periods "
      "flows greater than 80% of the meters maximum continuous flow rating. For any installations that "
      "require CIP (clean in place) it is important that the cleaning or flushing procedures do not "
      "exceed the advertised operating specifications. CIP cleaning procedures that increase system "
      "temperature at a rate greater than 50°F (10°C) per minute may damage the reed switch output. "
      "Chemical compatibility of cleaning solutions should be checked against the flow meter materials "
      "of construction.")
    H("Hiệu chuẩn", "Calibration", h4)
    P("Mỗi đồng hồ được hiệu chuẩn riêng tại nhà máy và kèm chứng chỉ ghi số xung trên một đơn vị thể "
      "tích (đồng hồ đầu ra xung) hoặc sai số đọc danh định (đồng hồ cơ). Hiệu chuẩn nhà máy dùng "
      "phương pháp đồng hồ chuẩn với Castrol Diesel Calibration Fluid 4113. Với chất lỏng có đặc tính "
      "gần giống chất này, có tính bôi trơn và độ nhớt 3–100 cP, hệ số hiệu chuẩn nhà máy không làm "
      "giảm hiệu năng. Với chất có độ nhớt hoặc khả năng bôi trơn khác biệt đáng kể (<1 cP hoặc "
      ">1000 cP), nên hiệu chuẩn lại trên chính chất sẽ đo.",
      "Each flow meter is individually calibrated at the factory and then supplied with a calibration "
      "certificate showing the number of pulses per unit volume (for a pulse output meter) or the "
      "nominal reading error (for mechanical meters). Factory calibrations are done using the master "
      "meter method, using Castrol Diesel Calibration Fluid 4113. For measurement of any liquids "
      "significantly similar to Diesel Calibration Fluid 4113, that is lubricating and with a viscosity "
      "of between 3-100cP, there will be no loss of flow meter performance when using the factory "
      "calibration factor. For any liquids where the viscosity or the lubricity of the liquid varies "
      "significantly from the factory calibration liquid (viscosity less than 1cP, or greater than "
      "1000cP), it is advisable to recalibrate your flow meter on the liquid that will be measured.")
    P("Với hiệu chuẩn tại hiện trường, cần xem xét độ chính xác của quy trình và của chuẩn thể tích: "
      "quy trình kém kiểm soát hoặc chuẩn không rõ sai số cho kết quả kém; mỗi quy trình nên chạy ít "
      "nhất 2 phút để giảm ảnh hưởng của dòng khởi động và ngừng.",
      "For any field calibration of your Oval Gear meter it is important to consider the accuracy of "
      "your calibration procedure, and of your volume standard: Calibration of your Oval Gear meter "
      "using a poorly controlled procedure, or using a volume standard of unknown accuracy will "
      "produce poor results. Any calibration procedure should be run for at least 2 minutes in order "
      "to reduce the impact of start-up and shut-down flows on your readings.")
    P("Các chuẩn thể tích có thể dùng cho hiệu chuẩn hiện trường:",
      "Possible volume standards that can be used for field calibrations are:")
    U(["Cân — dù là một trong những phương pháp phổ biến nhất, cũng có thể là một trong những phương "
       "pháp kém chính xác nhất. Cân phải được hiệu chuẩn gần đây và có vạch chia tinh vi để đạt độ bất "
       "định đo yêu cầu.",
       "Đồng hồ chuẩn — phương pháp đồng hồ chuẩn là chuẩn thể tích phổ biến nhất để hiệu chuẩn nhà "
       "máy đồng hồ PD nhờ độ chính xác và tính thực tiễn.",
       "Thùng thể tích hiệu chuẩn — thường được coi là phương pháp ít phổ biến và thực tiễn nhất; "
       "trớ trêu thay lại là chính xác nhất."],
      ["Scales - Although this is on the most common calibration methods, it can also be one of the "
       "least accurate. Scales must be recently calibrated to ensure accuracy, and must have fine "
       "graduations in order to achieve the required measurement uncertainty.",
       "Master Meter -  The master meter method is the most common volume standard used for factory "
       "calibration of PD flow meters, which is due to its accuracy and practicality.",
       "Volumetric Calibration Container -  This method is typically considered to be the least common, "
       "most impractical method. Ironically, it’s also the most accurate."])

    # -------------------- Turbine Flow Meters
    H("Đồng hồ lưu lượng tuabin", "Turbine Flow Meters", h3)
    P("Tóm tắt: đồng hồ là loại tuabin đo thể tích. Chất lỏng chảy (owing fluid trong OCR) tác động "
      "lên rôto có cánh làm nó quay với vận tốc góc tỉ lệ với lưu lượng chất (ow rate). Vận tốc góc "
      "của rôto tạo tín hiệu điện (dạng sine AC) trong đầu thu. Tổng của tín hiệu xung liên quan "
      "trực tiếp tới tổng lưu lượng; tần số tín hiệu liên quan trực tiếp tới lưu lượng. Rôto có cánh "
      "là bộ phận chuyển động duy nhất của đồng hồ.",
      "Brief Summary: The flowmeter is a volumetric measuring turbine type. The owing fluid engages the "
      "vaned rotor causing it to rotate at an angular velocity proportional to the fluid ow rate. The "
      "angular velocity of the rotor results in the generation of an electrical signal (AC sine wave "
      "type) in the pickup. The summation of the pulsing electrical signal is related directly to total "
      "flow. The frequency of the signal relates directly to flow rate. The vaned rotor is the only "
      "moving part of the flowmeter.")
    P("Đồng hồ tuabin (tuabin hướng trục) được Reinhard Woltman sáng chế và là đồng hồ chính xác, đáng "
      "tin cậy cho chất lỏng và khí. Đồng hồ gồm một ống dẫn với đầu nối ở hai đầu và một rôto nhiều "
      "cánh tự do quay bằng từ tính (cánh quạt) lắp bên trong, thẳng hàng với dòng chảy. Rôto được đỡ "
      "bởi trục tựa trên các giá lắp bên trong. Các giá trong đồng hồ Process Automatics còn đóng vai "
      "trò bộ chỉnh thẳng dòng, ổn định dòng và giảm tác động xấu của nhiễu loạn. Giá cũng chứa ổ mở "
      "độc đáo, cho phép môi chất đo bôi trơn các bạc — kéo dài tuổi thọ đồng hồ. Giá được giữ bằng "
      "vòng hãm (circlip) ở hai đầu.",
      "The Turbine flow meter (axial turbine) was invented by Reinhard Woltman and is an accurate and "
      "reliable flow meter for liquids and gases. It consists of a flow tube with end connections and a "
      "magnetic multi bladed free spinning rotor (impeller) mounted inside; in line with the ow. The "
      "rotor is supported by a shaft that rests on internally mounted supports. The Supports in Process "
      "Automatics Turbine Flow Meters are designed to also act as flow straightners, stabilizing the "
      "flow and minimizing negative effects of turbulence. The Supports also house the unique open "
      "bearings; allowing for the measured media to lubricate the bushes – prolonging the flow meters "
      "life span. The Supports are fastened by locking rings (circlips) on each end.")
    P("Đồng hồ tuabin chủ yếu dùng để đo chất lỏng và khí ở lưu lượng rất thấp. Đồng hồ đơn giản trong "
      "Hình 8 cho tín hiệu đầu ra dạng tần số thay đổi tuyến tính với lưu lượng thể tích trong dải đã "
      "định. Toàn bộ chất cần đo vào đồng hồ rồi đi qua rôto. Chất đi qua làm rôto quay với vận tốc góc "
      "tỉ lệ với vận tốc tuyến tính của chất. Vì vậy lưu lượng thể tích tuyến tính trong giới hạn đã cho.",
      "The turbine flow meter is mainly used for the purpose of measurement of liquid and gas at very "
      "low flow rates. A simple turbine flow meter shown in Fig. 8, provides a frequency output signal "
      "that varies linearly with volumetric flow rate over specified flow ranges. The entire fluid to "
      "be measured enters the flow meter, then passes through a rotor. The fluid passing through the "
      "rotor causes it to turn with an angular velocity that is proportional to the fluid linear "
      "velocity. Therefore, the volumetric flow rate is linear within the given limits of flow rate.")
    FIG(8, F.fig_f08())
    P("Xét đồng hồ tuabin điển hình trong Hình 9, gồm rôto nhiều cánh (bánh tuabin) lắp vuông góc với "
      "trục dòng chất lỏng. Rôto được đỡ bằng ổ bi hoặc ổ bạc trên trục được giữ trong vỏ đồng hồ "
      "bởi một giá đỡ. Rôto quay tự do quanh trục.",
      "Let us consider a typical Turbine flow meter shown in Fig. 9, which consists of a multibladed "
      "rotor (turbine wheel) which is mounted at right angles to the axis of the flowing fluid. The "
      "rotor is supported by ball or sleeve bearings on a shaft which is retained in the flow meter "
      "housing by a shaft-support. The rotor is rotating freely about its axis.")
    FIG(9, F.fig_f09())
    H("Nguyên lý làm việc", "Working", h4)
    P("Chất lỏng chảy đập vào cánh tuabin (rôto), truyền lực lên bề mặt cánh làm rôto quay. Ở tốc độ "
      "quay ổn định, tốc độ rôto tỉ lệ trực tiếp với vận tốc chất lỏng, do đó với lưu lượng thể tích. "
      "Ở hầu hết đồng hồ, tốc độ quay được giám sát bằng cuộn cảm từ tính lắp ở ngoài vỏ. Cuộn gồm nam "
      "châm vĩnh cửu với dây quấn đặt gần rôto nhưng bên ngoài kênh dẫn. Mỗi cánh rôto đi qua cuộn tạo "
      "một xung điện áp đo lưu lượng; tổng số xung cho tổng lưu lượng. Bằng kỹ thuật số, các xung điện "
      "áp được cộng, hiệu và xử lý để có đặc tính sai số zero từ bộ phát xung tới đầu đọc chất lỏng.",
      "The flowing fluid impinges on the blades of turbine (rotor), imparting a force to the blade surface "
      "which causes the rotation of the rotor. At a steady rotational speed, the speed of the rotor is "
      "directly proportional to the fluid velocity, and hence to volumetric flow rate. The speed of "
      "rotation is monitored in most of the meters by a magnetic pick-up coil, which is fitted to the "
      "outside of the meter housing. The magnetic pick-up coil consists of a permanent magnet with coil "
      "windings which is mounted in close proximity to the rotor but external to the fluid channel. As "
      "each rotor blade passes the magnetic pick-up coil, it generates a voltage pulse which is a "
      "measure of the flow rate, and the total number of pulses give a measure of the total flow. By "
      "digital techniques, the electrical voltage pulses can be totaled, differenced and manipulated so "
      "that a zero error characteristic of digital handling is provided from the electrical pulse "
      "generator to the fluid readout.")
    P("Số xung tạo ra được cho bởi",
      "The number of pulses generated is given as")
    EQ("f = n<sub>p</sub> Q / T<sub>p</sub>")
    U(["n<sub>p</sub> = xung trên một đơn vị thể tích",
       "T<sub>p</sub> = hằng số thời gian tính bằng phút",
       "Q = lưu lượng thể tích", "f = tần số tính bằng Hz"],
      ["n p = pulses per volume unit", "Tp = time constant in minutes",
       "Q = Volumetric flow rate", "f = frequency in Hz."])
    P("Đồng hồ tuabin có cỡ từ 6,35 mm đến 650 mm và dải lưu lượng chất lỏng từ 100 cm³ đến trên 50 m³.",
      "The turbine meters are available in sizes ranging from 6.35 mm to 650 mm and liquid flow ranges "
      "from 100 cubic centimeter to over 50 cubic meters.")
    H("Ưu điểm", "Advantages", h4)
    OL(["Độ chính xác tốt hơn [±0,25% đến ±0,5%].",
        "Khả năng lặp lại xuất sắc [±0,25% đến ±0,02%] và dải đo (10:1 và 20:1).",
        "Sụt áp khá thấp.",
        "Dễ lắp đặt và bảo trì.",
        "Khả năng chịu nhiệt độ và áp suất tốt.",
        "Có thể bù cho sự thay đổi độ nhớt."],
       ["1.  Better Accuracy [± 0.25% to ± 0.5%].",
        "2.  It provides excellent repeatability [± 0.25% to ± 0.02%] and range ability (10 : 1 and 20 : 1).",
        "3.  It has fairly low pressure drop.",
        "4.  It is easy to install and maintain.",
        "5.  It has good temperature and pressure ratings.",
        "6.  It can be compensated for viscosity variation."])
    H("Nhược điểm", "Disadvantages", h4)
    OL(["Chi phí cao.",
        "Ứng dụng hạn chế cho bùn.",
        "Không phù hợp chất lỏng không bôi trơn.",
        "Không giữ được hiệu chuẩn ban đầu trong thời gian rất dài, cần hiệu chuẩn lại định kỳ.",
        "Nhạy với thay đổi độ nhớt của chất lỏng đi qua.",
        "Nhạy với nhiễu loạn dòng.",
        "Do ma sát ổ bi cao ở đồng hồ nhỏ, không được ưu tiên cho lưu lượng thấp."],
       ["1.  High cost.",
        "2.  It has limited use for slurry applications.",
        "3.  It is not suitable for non-lubricating fluids.",
        "4.  They cannot maintain its original calibration over a very long period and therefore "
        "periodical recalibration is necessary.",
        "5.  They are sensitive to changes in the viscosity of the liquid passing through the meters.",
        "6.  They are sensitive to flow disturbances.",
        "7.  Due to high bearing friction is possible in small meters, they are not preferred well for "
        "low flow rates."])
    H("Ứng dụng", "Applications", h4)
    P("Đồng hồ tuabin được dùng rộng rãi cho mục đích quân sự, đặc biệt hữu ích trong hệ thống pha trộn "
      "của ngành dầu khí. Chúng hiệu quả trong hàng không và các ứng dụng trên máy bay để đo nhiên "
      "liệu năng lượng và dòng chất đông lạnh (cryogenic).",
      "The turbine meters are widely used for military applications. They are particularly useful in "
      "blending systems for the petroleum industry. They are effective in aerospace and air borne "
      "applications for energy-fuel and cryogenic flow measurements.")

    # -------------------- Variable Area Flow meter
    H("Đồng hồ lưu lượng diện tích thay đổi", "Variable Area Flow meter", h3)
    P("Đồng hồ diện tích thay đổi là dạng chuyên biệt thiết kế để xác định áp suất của khí hoặc chất "
      "lỏng trong hệ thống đường ống, thường dùng trong môi trường khoa học và công nghiệp. Có hai "
      "thiết kế phổ biến hiện nay dù hoạt động rất giống nhau.",
      "A variable area flow meter is a specialized form of flow meter designed to determine the pressure "
      "of a gas or liquid in a piping system. They are commonly used in scientific and industrial "
      "settings. There are two popular designs that are in use today, though they function in a very "
      "similar way.")
    P("Dạng cổ nhất là thiết bị hình nón bằng thủy tinh hoặc nhựa trong suốt gọi là đồng hồ đọc trực "
      "tiếp. Đầu nhỏ của nón đưa vào hệ thống ống, đầu rộng có nắp hướng lên. Khi ống đầy chất lỏng "
      "hoặc khí, chất vào đồng hồ; một hạt nhỏ bên trong ống thuỷ tinh dâng lên hoặc rơi xuống theo "
      "cường độ áp suất và các vạch trên thành ống cho phép đọc chính xác.",
      "The oldest form of variable area flow meter is a cone-shaped device made of glass or clear plastic "
      "called a direct reading flow meter. The narrow end of the cone is put into the pipe system with "
      "the wide, sealed end face up. When the pipes fill with a liquid or a gas it enters the meter. A "
      "small bead inside the glass meter rises or falls with the strength of the pressure, and markings "
      "on the side of the glass allow a person to get an accurate reading.")
    P("Dạng đọc trực tiếp vẫn được dùng phổ biến nhưng có nhược điểm: khá lớn và hoạt động nhờ trọng "
      "lực nên đầu rộng phải hướng lên mới cho kết quả đúng — không phải lúc nào cũng thực tế trong "
      "hệ thống ống nhỏ hoặc kín. Ngoài ra nếu chất lỏng để lại cặn trên thuỷ tinh thì phải thay hoặc vệ sinh.",
      "The direct reading version of a variable area flow meter is still commonly used. This meter has "
      "some drawbacks, though. It is somewhat large, and it works using gravity, so the wide end must be "
      "facing up for an accurate reading. This is not always practical in a small or enclosed piping "
      "system. Also, if the fluid being measured leaves residue on the glass, it will have to be replaced "
      "or cleaned.")
    P("Nếu những vấn đề trên đáng lo, có các phiên bản mới hơn. Một loại làm việc được trong không gian "
      "chật và không cần trọng lực là đồng hồ tương quan, dùng hạt từ tính và lò xo đo áp suất trong "
      "ống. Khi áp suất tăng, hạt ép vào lò xo; lò xo truyền áp suất tới màn hình số.",
      "If any of these issues is a concern, there are other more recently-invented versions of variable "
      "area flow meters. One type that can work in tight spaces and doesn’t require gravity for readings "
      "is a correlated flow meter. These use a magnetic bead and a spring to measure the amount of "
      "pressure in a tube. As the pressure increases, the bead is pressed against the spring. Then, the "
      "spring conveys the amount of pressure it is receiving to a digital screen.")
    P("Nhược điểm của loại tương quan là khó đọc hơn loại hình nón và không dùng đơn vị đo thông thường "
      "trên màn hình. Sau khi hiện một số, người đọc phải dùng biểu đồ chuyển sang đơn vị mét hoặc "
      "imperial. Hệ thống này cũng cho kết quả không chính xác nếu nhiệt độ chất lỏng quá cao hoặc quá thấp.",
      "The drawback to the correlated version of the variable area flow meter is that it is more "
      "difficult to read than the cone shaped variety. It also doesn’t use common measuring units on the "
      "display screen. After the correlated flow meter displays a number, the reader must then use a "
      "chart to convert this number to a metric or imperial measurement. Also, this system does not give "
      "accurate readings if the fluid’s temperature is too high or too low.")
    P("Nếu chất lỏng có thể làm hư cả hai loại trên, có thể dùng đồng hồ cánh vane: đặt một đĩa trong "
      "dòng ống nối với thân di động. Chuyển động của đĩa và thân được đầu dò chuyển động cảm nhận để "
      "xác định áp suất. Nhược điểm là loại này phức tạp hơn và cần bảo trì nhiều hơn.",
      "If the fluid to be measured may damage either of the meters, another type of variable area flow "
      "meter called a vane meter can be used. These meters put a disk in the flow of a pipe. This disk "
      "is connected to a movable stem. The motions of the disk and stem are sensed by a motion detector "
      "which measures them and determines the pressure. A drawback is that the vane meter is more "
      "complicated than the other types and requires more maintenance.")
    P("Dù mọi đồng hồ diện tích thay đổi đều có nhược điểm, chúng tương đối đơn giản, giá phải chăng và "
      "được dùng phổ biến. Có thể mua đồng hồ phức tạp hơn với giá cao hơn. Cơ sở của tất cả là nguyên "
      "lý tạo một sự cản nhẹ đối với dòng chảy để xác định cường độ của nó.",
      "Although every variable area flow meter has drawbacks, they are also relatively simple, "
      "affordable, and commonly used. More complicated meters can be purchased for higher prices. The "
      "basis for all of them is the principle of providing slight resistance to a flow in order to "
      "determine its strength.")

    # -------------------- Electromagnetic flow meters
    H("Đồng hồ đo lưu lượng điện từ", "Electromagnetic flow meters", h3)
    P("Đồng hồ điện từ, còn gọi là magmeter, đo tốc độ dòng chất lỏng — hoặc chất rắn lơ lửng trong "
      "chất lỏng — qua ống. Thường dùng trong xử lý nước thải, chế biến thực phẩm và y tế. Chúng dựa "
      "vào độ dẫn điện của chất lỏng, dung dịch hoặc bùn — khi đi qua từ trường tạo tín hiệu điện "
      "dùng để đo lưu lượng thể tích.",
      "An electromagnetic flowmeter, also known as a magmeter, is a tool that measures the rate of flow "
      "of a liquid — or solids suspended in a liquid — through a pipe. Often, such flowmeters are used in "
      "the wastewater treatment, food processing, and medical industries. They generally rely on the "
      "conductivity of the liquid, solution, or slurry that they are measuring — as it passes through a "
      "magnetic field and generates an electric signal — which can be used to measure flow of volume.")
    P("Vì chất phải có độ dẫn điện mới đo được bằng đồng hồ điện từ, các dụng cụ này chỉ chiếm khoảng "
      "20% tổng số đồng hồ dùng. Các loại khác gồm đồng hồ xoáy và đồng hồ siêu âm. Tuy nhiên đồng hồ "
      "điện từ thường không xâm lấn và nhìn chung không cản đáng kể dòng chảy để đo. Chúng cũng thiết "
      "kế rất đơn giản, gần như không bộ phận chuyển động nên ít bảo trì và không thường phải thay thế.",
      "Since a substance has to have electrical conductivity to be measured by an electromagnetic "
      "flowmeter, these tools only account for approximately 20% of all meters used. Other types include "
      "the vortex flowmeter and the ultrasonic flowmeter. An electromagnetic flowmeter, however, is often "
      "non-invasive and generally does not appreciably restrict flow in order to measure it. Also, these "
      "devices tend to be very simply designed, with almost no moving parts, so they require little "
      "maintenance and do not often have to be replaced.")
    P("Vào những năm 1830, Michael Faraday đã công bố khoa học làm nền tảng cho phát minh đồng hồ điện "
      "từ. Ông phát hiện chất dẫn điện chuyển động trong từ trường tạo ra tín hiệu điện. Các phát triển "
      "sau đó cho phép giải mã tín hiệu này bằng các phép tính khoa học để xác định vận tốc dòng.",
      "In the 1830s, Michael Faraday revealed the science that would make the invention of the "
      "electromagnetic flowmeter possible. He discovered that a substance that conducts electricity and "
      "moves through a magnetic field produces an electric signal. Further developments led to the "
      "ability to interpret this signal, via various scientific calculations, to determine flow velocity.")
    P("Có vài cấu hình khác nhau. Đôi khi điện cực nhô vào trong ống dẫn chất đo; cuộn ở ngoài ống tạo "
      "từ trường, điện cực thu điện được tạo ra. Chừng nào điện cực không đóng cặn từ chất đo thì chúng "
      "làm việc tốt.",
      "There are a few different of configurations of electromagnetic flowmeters. They sometimes have "
      "electrodes that protrude into the pipe through which the measured substance flows. Coils on the "
      "outside of the pipe produce the magnetic field, while the electrodes pick up the electricity "
      "generated. As long as the electrodes do not build up a coating from the substance being measured, "
      "they work well.")
    P("Một dạng khác hoàn toàn không xâm lấn ống: điện cực chỉ đặt ở bề mặt ngoài, cuộn vẫn tạo từ "
      "trường. Ưu điểm là chất lỏng không bao giờ phủ điện cực; đồng hồ cũng dùng được cho hệ ống kín "
      "đòi hỏi giữ độ sạch và vệ sinh.",
      "Another kind of electromagnetic flowmeter is completely non-invasive to the pipe. In this type, "
      "the electrodes are placed just on its exterior and the coils still generate a magnetic field. One "
      "advantage of this is that the liquid that it is measuring never coats the electrodes. Also, these "
      "flowmeters can be used on closed piping systems, which are sometimes necessary to maintain purity "
      "and sanitation.")
    P("Khi dùng đồng hồ điện từ, phải nối đất đúng cách, nếu không nó sẽ bắt nhiễu điện (noise) và chỉ "
      "số sai. Đây là vấn đề đặc biệt với ống nhựa vì thường sinh tĩnh điện. Tuỳ thiết kế đồng hồ và "
      "đường ống mà dùng cấu hình nối đất khác nhau.",
      "When an electromagnetic flowmeter is utilized, it must be properly grounded. Otherwise, it can "
      "pick up electrical interference, often referred to as noise, and the flow reading will not be "
      "accurate. This can be a particular problem when pipes are plastic, because they typically "
      "generate static electricity. Various grounding configurations are employed, depending on "
      "flowmeter and piping design.")

    # -------------------- Ultrasonic flow meters
    H("Đồng hồ lưu lượng siêu âm", "Ultrasonic flow meters", h3)
    P("Đồng hồ siêu âm đo vận tốc chất lỏng trong ống bằng sóng âm. Hữu ích khi phép đo phải thực hiện "
      "mà không làm gián đoạn vật lý dòng trong ống. Rất phù hợp đo chất có thể hư đồng hồ khác do nhiệt "
      "độ cực cao hoặc tính ăn mòn. Thiết bị này cũng cho phép đo chính xác hơn các đồng hồ hiện có.",
      "An ultrasonic flow meter is a way to measure the velocity of a fluid in a tube using sound waves. "
      "These meters are useful in situations where the measurement must be done in a way that doesn’t "
      "physically disrupt the flow of fluid in the tube. They are well-suited for measuring the flow of "
      "a substance that might damage other types of flow meters due to its extreme temperature or "
      "corrosive properties. This device also allows for more precise measurements than other available "
      "flow meters do.")
    P("Cách làm việc là gửi sóng âm qua hệ thống ống, rồi đo thời gian sóng phản xạ về bộ phát. Đồng hồ "
      "dùng thời gian từ lúc phát đến lúc nhận echoes để xác định vận tốc chất lỏng trong ống.",
      "The way an ultrasonic flow meter works is by sending sound waves through a pipe system. Next, it "
      "measures the amount of time it takes them to reflect back to the sender. The flow meter is then "
      "able to interpret the amount of time that has passed from the transmission of the sound to "
      "receiving the echo of the sound to determine the velocity of the fluid moving inside of the pipes.")
    P("Đồng hồ siêu âm được ưa chuộng nhờ độ chính xác và ít bảo trì. Hầu hết đồng hồ khác theo cấu tạo "
      "phải can thiệp vào dòng mới đọc được: đưa dụng cụ vào ống hoặc tạo một sự chắn nhẹ — có thể làm "
      "thay đổi không mong muốn vận tốc trong ống.",
      "Ultrasonic flow meters are favored because of their precision and low maintenance. Most other "
      "flow meters by their construction need to interfere with the flow in order to get a reading. They "
      "may insert a measuring tool into the pipe, or they may create a slight blockage of the flow in "
      "order to gain a reading. This slight blockage could create an unwanted change in the velocity "
      "within the tube.")
    P("Có nhiều ưu điểm nữa của đồng hồ siêu âm so với đồng hồ khác. Đồng hồ truyền thống, như đồng hồ "
      "đứng (vertical flow meter trong OCR), lớn và cần đặt đúng vị trí mới đọc được. Để vạch đọc rõ, "
      "phải vệ sinh và/hoặc thay chúng thường xuyên hơn đồng hồ siêu âm.",
      "There are a number of other advantages of the ultrasonic flow meter over other flow meters. "
      "Traditional flow meters, such as the vertical flow meter, are large and require exact placement "
      "in order to give a reading. In order for the markings to be readable, these flow meters need to "
      "be cleaned and/or replaced on a more frequent basis than an ultrasonic flow meter.")
    P("Công nghệ siêu âm thường dùng trong nhiều ứng dụng khác để tạo phép đo và hình ảnh; độ chính xác "
      "rất cao và tác động lên đối tượng đủ nhỏ để dùng trong y tế. Nhu cầu ngày càng tăng làm đồng hồ "
      "siêu âm ngày càng phải chăng. Những ưu điểm đó cho thấy chúng sẽ dần thay thế các mẫu khác. Có "
      "thể mua đồng hồ siêu âm trực tuyến và nhiều nhà sản xuất kèm dịch vụ lắp đặt khi mua.",
      "Ultrasonic technology is commonly used in other applications to create measurements and images. "
      "It is incredibly accurate and its effect on the subject being studied is minimal enough to be used "
      "in medical procedures. Increased demand for ultrasonic technology, including the kind used in an "
      "ultrasonic flow meter, means that it is becoming more affordable. The advantages these devices "
      "offer over other flow meters suggest that they will eventually replace the other models. An "
      "ultrasonic flow meter can be purchased online, and many manufacturers offer installation service "
      "with purchase.")

    # ---------------------------------------------------------------- refs
    H("Tài liệu tham khảo", "References")
    b.append(refs(_REFS))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
