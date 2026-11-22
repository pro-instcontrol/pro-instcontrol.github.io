# -*- coding: utf-8 -*-
"""Book 8, Chapter 2 - Measurement of Pressure (EN/VI bilingual).

Source: 3G E-learning LLC, *Illustrated Handbook of Industrial Instrumentation
& Control* (2018), PDF pp. 61-96 (36 pages), printed pp. 47-82.  The chapter
covers the concept of pressure measurement, liquid column and Bourdon gauges,
McLeod, radiometer-effect, ionisation, thermal-conductivity and electronic
sensors, high-pressure cells, and vacuum measurement.  Its 21 numbered source
figures (Figure 1 - Figure 21) are redrawn as vectors in `iihfig2.py` and
placed where the source captions occur.  Prose is translated in full; the
image-only equations are rendered with readable symbols and recorded as
source quirks at the end.
"""

import iih_common as C
import iihfig2 as F2
from iih_common import (eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 36          # PDF pp. 61-96 inclusive (printed pp. 47-82)
BYLINE = "3G E-learning LLC · Illustrated Handbook of Industrial Instrumentation & Control (2018)"
TITLE_EN = "Measurement of Pressure"
TITLE_VI = "Đo áp suất"


# ---------------------------------------------------------------------------
# Reference list (source printed pp. 81-82).  Citation text is kept as printed.
# ---------------------------------------------------------------------------
_REFS = [
    "S. Dushman, J.M. Lafferty: “SCIENTIFIC FOUNDATION OF VACUUM TECHNIQUE”, John Wiley and Sons, "
    "Inc. New York, London, 1962",
    "J.M. Lafferty (ed.): “FOUNDATIONS OF VACUUM SCIENCE AND TECHNOLOGY”, John Wiley &amp; Sons, "
    "Inc. New York, Toronto 1997",
    "B. van Zyl: Check on the Linearity of a Capacitance Diaphragm Manometer between 10⁻⁴ and "
    "10⁻¹ Torr, Rev. Sci. Instrum. 47 (1976) 9, 1214",
    "Catalogue of the company LEYBOLD AG, HV 300, Part A1, date of publication: 05/92, pages 18 "
    "and 76/77",
    "H. McLeod, Apparatus for Measurement of Low Pressures of Gas, Phil. Mag. 48 (1874), 110",
    "R. Jurgeit, C. Hartung: Vorrichtung zur kontinuierlichen Messung von Gasdrücken. "
    "Wirtschaftspatent der DDR WP G 01 L/197067 Nr. 130850 vom 25 01 1977, erteilt am 3 5 1978",
    "R. Jurgeit, Dissertation, Technische Universität Dresden, 1981",
    "Chr. Edelmann: Stand und Entwicklungstendenzen der Totaldruckmessung in der Vakuumtechnik. "
    "Vakuum-Techn. 34 (1985) 6, 162 - 180",
    "R. Jaeckel: “Kleinste Drucke, ihre Messung und Erzeugung”, Springer-Verlag, Berlin "
    "Heidelberg 1952",
    "F. T. Holmes: Rev. Sci. Instr. (1937), 444",
    "J. K. Fremerey: High Vacuum Friction Manometer, J. Vacuum Sci. Technol. 9 (1972) 108",
    "T. Kobayashi, H. Hojo, M. Ono: Gas Concentration Analysis with a Quartz Friction Vacuum "
    "Gauge. Vacuum 47 (1996) 6/8, 479 – 483",
    "M. Ono, M. Hirata, K. Kokubun, H. Murakami: Quartz Friction Vacuum Gauge for Pressure Range "
    "from 0.001 to 1000 Torr. J. Vac. Sci. Technol. A 4 (1986) 3, 1728 – 1731",
    "M. Pirani. Ber. Dt. Phys. Ges. 4 (1906), 686 [13] E. Ja. Badinter, B.K. Zalewskii, I. G. "
    "Starusch: A Miniaturised Thermo-electric Pressure Gauge (in Russian), Prib. Tekh. Eksp. "
    "(1980), 248 – 250",
    "W. Gorski, A. Smiech: Convection Vacuum Gauge for Use between 10⁻³ and 760 Torr, Le Vide "
    "No. 169 (1974), 221",
    "J.B. Huang, Q. Y. Tong: Constant Temperature Integrated Vacuum Sensor, Electron Lett. 24 "
    "(1988) 23, 1429 – 1430",
    "M. Knudsen: Ein absolutes Manometer. Ann. Phys. 32 (1910) 809 –842",
    "H. Klumb, H. Schwarz: Über ein absolutes Manometer zur Messung niedrigster Drücke, Z. Phys. "
    "122 (1944), 418 J. Lucas, T. Goto: A Pressure Gauge Utilising the Electron Diffusion Process "
    "and Microcomputer Control, Vacuum 34 (1984) 785 – 789",
    "Chr. Edelmann: Vakuum-Meßverfahren und Vakuum-Meßeinrichtung, Deutsches Patentamt, 02.12.1998",
    "Chr. Edelmann: Vakuum-Meßeinrichtung, Deutsches Markenamt, angemeldet 02.12.1998",
    "Chr. Edelmann, R. Kauert, St. Wilfert: Anwendung der Elektronendriftgeschwindigkeit zur "
    "Druckmessung, Frühjahrstagung der Deutschen Phys. Ges. Münster, 1999",
    "N.A. Kapzow: “Elektrische Vorgänge in Gasen und im Vakuum” (German translation from Russian), "
    "VEB Deutscher Verlag der Wissenschaften Berlin 1955",
    "J. Hjelmgren, Dynamic measurement of pressure – A literature survey, SP Report 2002:34, "
    "Swedish National Testing and Research Institute, 2002.",
    "S. A. Whitmore, Formulation of a general technique for predicting pneumatic attenuation "
    "errors in airborne pressure sensing devices, NASA TM 100430, 1988.",
    "S. A. Whitmore, W. T. Lindsey, R. E. Curry, G. B. Gilyard, Experimental characterization of the "
    "effects of pneumatic tubing on unsteady pressure measurements, NASA TM 4171, 1990.",
    "S. A. Whitmore, Pneumatic distorsion compensation for aircraft surface pressure sensing "
    "devices, Journal of Aircraft 28(12), 1991, pps. 828-836.",
    "O. K. Rediniotis, M. M. Pathak, A simple technique for frequency-response enhancment of "
    "miniature pressure probes, AIAA Journal 37(7), 1999, pps. 897-899.",
    "A. Yoshida, Y. Tamura, T. Kurita, Effects of bends in a tubing system for pressure "
    "measurement, Journal of Wind Engineering and Industrial Aerodynamics 89, 2001, pps. "
    "1701-1716.",
    "T. Lokar, A. Smrečnik, I. Bajsić, Generating dynamic pressure with loudspeakers, 16th IMEKO "
    "World Congress (Vienna, 25-28. Sept. 2000), Austrian Society for Measurement and Automation, "
    "Vienna, 2000, pps. 109-113.",
    "T. Žagar, J. Kutin, I. Bajsić, The effect of connecting-tube dimensions on dynamic "
    "characteristics of pressure measurement systems, Ventil 11(3), 2005, pps. 161-165 "
    "(in Slovene).",
    "R. D. Blevins, Formulas for natural frequency and mode shape, Kreiger, Malabar, 1995.",
    "E. Naudascher, D. Rockwell, Flow-induced vibrations. An engineering guide, A.A. Balkema, "
    "Rotterdam, 1994.",
    "M. L. Chugani, A. R. Samant, M. Cerna, LabVIEW signal processing, Prentice-Hall, New York, 1998.",
    "T. D. Burton, Introduction to dynamic systems analysis, McGraw-Hill, New York, 1994.",
    "NIST (http://physics.nist.gov/Pubs/SP811/sec07.html#7.4)",
    "[Was: «fluidengineering.co.nr/Manometer.htm». At 1/2010 that took me to bad link. Types of "
    "fluid Manometers]",
    "Techniques of high vacuum (http://www.tau.ac.il/~phchlab/experiments/vacuum/"
    "Techniques_of_high_vacuum/Vacuum5.html)",
    "Beckwith, Thomas G.; Roy D. Marangoni and John H. Lienhard V (1993). “Measurement of Low "
    "Pressures”. Mechanical Measurements",
    "(Fifth ed.). Reading, MA: Addison-Wesley. pp. 591–595. ISBN 0-201-56947-7.",
    "The Engine Indicator Canadian Museum of Making (http://www.archivingindustry.com/Indicator/"
    "discspring.htm)",
    "Boyes, Walt (2008). Instrumentation Reference Book, Fourth Edition. Butterworth-Heinemann. "
    "pp. 1312.",
    "Product brochure from Schoonover, Inc (http://www.schoonoverinc.com/PDFs/Sky%20Brochure.pdf)",
    "VG Scienta (http://www.vacgen.com/asp/catalogue.asp?url=http://www.vacgen.com/catalogue/"
    "section-8/page08_03.htm&amp;frame=1)",
    "Robert M. Besançon, ed (1990). “Vacuum Techniques” (3rd ed.). Van Nostrand Reinhold, New "
    "York. pp. 1278–1284. ISBN 0-442-00522-9.",
    "http://www.komar.org/faq/manometer/",
    "http://www.upscale.utoronto.ca/PVB/Harrison/Manometer/Manometer.html",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> áp suất — pressure · đồng hồ áp suất — pressure gauge · "
                "thiết bị đo chân không — vacuum gauge · ống chữ U — U tube · manometer — "
                "manometer · ống Bourdon — Bourdon tube · đồng hồ McLeod — McLeod gauge · "
                "hiệu ứng phóng xạ nhiệt — radiometer effect · hệ số thích ứng — accommodation "
                "coefficient · ion hóa — ionisation · catốt nóng/lạnh — hot/cold cathode · "
                "dẫn nhiệt — thermal conductivity · strain gage — strain gage · điện dung — "
                "capacitance · mô đun khối — bulk modulus · barometer — barometer · torr — torr.")
    return ("<b>Key terms.</b> pressure · pressure gauge · vacuum gauge · U tube · manometer · "
            "Bourdon tube · McLeod gauge · radiometer effect · accommodation coefficient · "
            "ionisation · hot/cold cathode · thermal conductivity · strain gage · capacitance · "
            "bulk modulus · barometer · torr.")


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

    def FIG(n, fn):
        b.append(fig(n, fn))

    def EQ(body):
        b.append(eq(body))

    # ---------------------------------------------------------------- lead
    b.append(lead(
        "Chương này khảo sát phép đo áp suất: khái niệm áp suất tĩnh và động, đồng hồ cột chất "
        "lỏng và ống Bourdon, đồng hồ McLeod và đồng hồ ion hóa, cảm biến nhiệt và điện tử, tế bào "
        "áp suất cao, cùng phép đo chân không barometer và các dải đo."
        if vi else
        "This chapter surveys pressure measurement: static and dynamic pressure, liquid column "
        "and Bourdon gauges, McLeod and ionisation gauges, thermal and electronic sensors, "
        "high-pressure cells, and vacuum measurement with the barometer and gauge ranges."))

    # ---------------------------------------------------------------- 2.1
    H("2.1 Giới thiệu", "2.1 Introduction")
    P("Áp suất được định nghĩa là lực trên một đơn vị diện tích mà một chất lỏng tác dụng lên môi "
      "trường xung quanh nó. Áp suất P là hàm của lực F và diện tích A:",
      "Pressure is defined as force per unit area that a fluid exerts on its surroundings. "
      "Pressure, P, is a function of force, F, and area, A:")
    EQ("P = F/A")
    P("Đơn vị SI của áp suất là pascal (N/m²), nhưng các đơn vị thường gặp khác gồm pound trên "
      "inch vuông (psi), atmotphe (atm), bar, inch thủy ngân (in. Hg), milimet thủy ngân "
      "(mm Hg) và torr.",
      "The SI unit for pressure is the pascal (N/m2), but other common units of pressure include "
      "pounds per square inch (psi), atmospheres (atm), bars, inches of mercury (in. Hg), "
      "millimeters of mercury (mm Hg), and torr.")
    P("Một phép đo áp suất có thể được mô tả là tĩnh hoặc động. Áp suất trong các trường hợp "
      "không có chuyển động là áp suất tĩnh. Ví dụ về áp suất tĩnh gồm áp suất của không khí "
      "trong bóng bay hoặc của nước trong chậu. Thường thì chuyển động của chất lỏng làm thay đổi "
      "lực tác dụng lên môi trường xung quanh. Ví dụ, giả sử áp suất nước trong một ống khi đóng "
      "vòi là 40 pound trên inch vuông (lực trên đơn vị diện tích). Nếu mở vòi, áp suất giảm "
      "xuống giá trị thấp hơn khi nước chảy ra. Một phép đo áp suất kỹ phải ghi rõ hoàn cảnh "
      "thực hiện phép đo. Nhiều yếu tố gồm dòng chảy, độ nén của chất lỏng và các ngoại lực có thể "
      "ảnh hưởng đến áp suất.",
      "A pressure measurement can be described as either static or dynamic. The pressure in cases "
      "with no motion is static pressure. Examples of static pressure include the pressure of the "
      "air inside a balloon or water inside a basin. Often, the motion of a fluid changes the "
      "force applied to its surroundings. For example, say the pressure of water in a hose with "
      "the nozzle closed is 40 pounds per square inch (force per unit area). If you open the "
      "nozzle, the pressure drops to a lower value as you pour out water. A thorough pressure "
      "measurement must note the circumstances under which it is made. Many factors including "
      "flow, compressibility of the fluid, and external forces can affect pressure.")

    # ---------------------------------------------------------------- 2.2
    H("2.2 Khái niệm đo áp suất", "2.2 Concept of Measurement Pressure")
    P("Nhiều kỹ thuật đã được phát triển để đo áp suất và chân không. Dụng cụ dùng đo áp suất "
      "được gọi là đồng hồ áp suất (pressure gauge) hoặc đồng hồ chân không (vacuum gauge).",
      "Many techniques have been developed for the measurement of pressure and vacuum. Instruments "
      "used to measure pressure are called pressure gauges or vacuum gauges.")
    P("Manometer cũng có thể chỉ một thiết bị đo áp suất, thường giới hạn ở các áp suất gần áp "
      "suất khí quyển. Thuật ngữ manometer thường được dùng riêng cho các dụng cụ thủy tĩnh cột "
      "chất lỏng.",
      "A manometer could also be referring to a pressure measuring instrument, usually limited to "
      "measuring pressures near to atmospheric. The term manometer is often used to refer "
      "specifically to liquid column hydrostatic instruments.")
    P("Đồng hồ chân không dùng để đo áp suất trong chân không — được chia tiếp thành hai loại con "
      "là chân không cao và chân không thấp (đôi khi gồm cả chân không cực cao). Dải áp suất áp "
      "dụng của nhiều kỹ thuật đo chân không có sự chồng lấp. Do đó, bằng cách kết hợp nhiều loại "
      "đồng hồ khác nhau, có thể đo liên tục áp suất hệ thống từ 10 mbar xuống tới 10⁻¹¹ mbar.",
      "A vacuum gauge is used to measure the pressure in a vacuum—which is further divided into "
      "two subcategories: high and low vacuum (and sometimes ultra-high vacuum). The applicable "
      "pressure range of many of the techniques used to measure vacuums have an overlap. Hence, "
      "by combining several different types of gauge, it is possible to measure system pressure "
      "continuously from 10 mbar down to 10⁻¹¹ mbar.")

    H("Đồng hồ cột chất lỏng (ống chữ U)", "Liquid column gauge (U tube)", h3)
    P("Đồng hồ cột chất lỏng gồm một cột chất lỏng thẳng đứng trong ống mà hai đầu tiếp xúc với "
      "các áp suất khác nhau. Cột chất lỏng dâng lên hoặc hạ xuống cho đến khi trọng lượng của nó "
      "cân bằng với chênh áp giữa hai đầu ống. Một dạng rất đơn giản là ống chữ U đựng đầy một nửa "
      "chất lỏng, một đầu nối tới vùng cần đo trong khi áp suất chuẩn (có thể là áp suất khí quyển "
      "hoặc chân không) được đặt ở đầu kia. Chênh lệch mức chất lỏng biểu thị áp suất tác dụng.",
      "Liquid column gauges consist of a vertical column of liquid in a tube whose ends are "
      "exposed to different pressures. The column will rise or fall until its weight is in "
      "equilibrium with the pressure differential between the two ends of the tube. A very simple "
      "version is a U shaped tube half-full of liquid, one side of which is connected to the "
      "region of interest while the reference pressure (which might be the atmospheric pressure "
      "or a vacuum) is applied to the other. The difference in liquid level represents the "
      "applied pressure.")
    P("Dù có thể dùng bất kỳ chất lỏng nào, thủy ngân được ưu tiên vì mật độ cao (13,534 g/cm³) "
      "và áp suất hơi thấp. Với chênh áp nhỏ nhưng cao hơn nhiều áp suất hơi của nước, người ta "
      "thường dùng nước (và “mét nước” là đơn vị áp suất phổ biến). Chiều cao cột chất lỏng tuân "
      "theo phương trình thủy tĩnh:",
      "Although any fluid can be used, mercury is preferred for its high density (13.534 g/cm3) "
      "and low vapour pressure. For low pressure differences well above the vapour pressure of "
      "water, water is commonly used (and 'meters of water' is a common pressure unit). The "
      "hydrostatic relation for the column is:")
    EQ("P = γ·h")
    FIG(1, F2.fig_f01())

    H("Đồng hồ Bourdon", "Bourdon gauge", h3)
    P("Đồng hồ áp suất Bourdon dùng nguyên lý một ống dẹt có xu hướng chuyển sang mặt cắt ngang "
      "tròn hơn khi chịu áp suất. Dù sự thay đổi mặt cắt này khó nhận thấy, chuyển động của vật "
      "liệu ống được phóng đại bằng cách uốn ống thành hình chữ C, thậm chí thành hình ốc xoắn, "
      "để toàn bộ ống có xu hướng duỗi thẳng hoặc mở ra một cách đàn hồi khi chịu áp.",
      "The Bourdon pressure gauge uses the principle that a flattened tube tends to change to a "
      "more circular cross-section when pressurized. Although this change in cross-section may "
      "be hardly noticeable, the displacement of the material of the tube is magnified by forming "
      "the tube into a C shape or even a helix, such that the entire tube tends to straighten out "
      "or uncoil, elastically, as it is pressurized.")
    FIG(2, F2.fig_f02())
    P("Trong thực tế, một ống mỏng dẹt, bịt kín một đầu được nối ở đầu rỗng với một ống cố định "
      "chứa áp suất chất lỏng cần đo. Khi áp suất tăng, đầu bịt kín dịch chuyển theo một cung, "
      "chuyển động này được biến thành sự quay của một (đoạn) bánh răng nhờ một liên kết thường "
      "có thể chỉnh được. Một bánh răng nhỏ đường kính nhỏ nằm trên trục kim, nên chuyển động "
      "được phóng đại thêm nhờ tỉ số bánh răng. Vị trí của mặt đồng hồ phía sau kim, vị trí ban "
      "đầu của trục kim, chiều dài và vị trí ban đầu của liên kết — tất cả tạo ra các cách hiệu "
      "chỉnh để kim chỉ đúng dải áp suất mong muốn cho các biến thiên của bản thân ống Bourdon.",
      "In practice, a flattened thin-wall, closed-end tube is connected at the hollow end to a "
      "fixed pipe containing the fluid pressure to be measured. As the pressure increases, the "
      "closed end moves in an arc, and this motion is converted into the rotation of a (segment "
      "of a) gear by a connecting link which is usually adjustable. A small diameter pinion gear "
      "is on the pointer shaft, so the motion is magnified further by the gear ratio. The "
      "positioning of the indicator card behind the pointer, the initial pointer shaft position, "
      "the linkage length and initial position, all provide means to calibrate the pointer to "
      "indicate the desired range of pressure for variations in the behaviour of the Bourdon tube "
      "itself.")
    P("Ống Bourdon đo áp suất gauge (áp suất tương đối so với khí quyển), trái với áp suất "
      "tuyệt đối; chân không được cảm nhận như chuyển động ngược chiều. Khi áp suất đo dao động "
      "nhanh, chẳng hạn đồng hồ đặt gần bơm pittông, người ta thường dùng một lỗ tiết lưu trong "
      "đường nối để tránh mòn không cần thiết cho bánh răng và cho kết đọc trung bình; khi toàn "
      "bộ đồng hồ chịu rung cơ học, có thể đổ đầy dầu hoặc glycerin vào cả vỏ, gồm cả kim và mặt "
      "đồng hồ. Đồng hồ chất lượng cao hiện điển hình có độ chính xác ±2% dải đo, còn đồng hồ "
      "đặc biệt độ chính xác cao có thể đạt 0,1% toàn thang.",
      "Bourdon tubes measure gage pressure, relative to ambient atmospheric pressure, as opposed "
      "to absolute pressure; vacuum is sensed as a reverse motion. When the measured pressure is "
      "rapidly pulsing, such as when the gauge is near a reciprocating pump, an orifice restriction "
      "in the connecting pipe is frequently used to avoid unnecessary wear on the gears and "
      "provide an average reading; when the whole gauge is subject to mechanical vibration, the "
      "entire case including the pointer and indicator card can be filled with an oil or "
      "glycerin. Typical high-quality modern gauges provide an accuracy of ±2% of span, and a "
      "special high-precision gauge can be as accurate as 0.1% of full scale.")

    H("Đồng hồ McLeod", "McLeod gauge", h3)
    P("Hoạt động của đồng hồ McLeod dựa trên phương trình cơ bản của Boyle. Với p và V lần lượt "
      "là áp suất và thể tích, các chỉ số 1 và 2 biểu thị điều kiện ban đầu và cuối:",
      "The working of McLeod Gauge is based on Boyles fundamental equation. Where p and V refer "
      "to pressure and volume respectively and subscripts 1 and 2 refer to initial and final "
      "conditions:")
    EQ("p<sub>1</sub>·V<sub>1</sub> = p<sub>2</sub>·V<sub>2</sub>")
    P("Đồng hồ McLeod thông thường làm bằng thủy tinh. Nó gồm mao dẫn C, bình cầu B và bình chứa "
      "thủy ngân nối với đầu dưới của ống thủy tinh sao cho có thể nâng hạ bình này.",
      "Conventional McLeod gauge is made of glass. It consists of the capillary C, bulb B and the "
      "mercury sump which is connected to the lower end of the glass tube such that it can be "
      "moved up and down.")
    P("Áp suất cần đo (áp suất chưa biết) được nối với đầu trên của phần thủy tinh. Khi mức thủy "
      "ngân trong đồng hồ nằm dưới vạch cắt F, áp suất chưa biết lấp đầy đồng hồ gồm bình B và "
      "mao dẫn C. Khi nâng bình thủy ngân, mức trong đồng hồ dâng lên và khi tới vạch cắt F, một "
      "thể tích khí biết trước ở áp suất cần đo bị giam trong bình B và mao dẫn C.",
      "The pressure to be measured (the unknown pressure) is connected to the upper end of the "
      "glass part. When the mercury level in the gauge is below the cut off F, the unknown "
      "pressure fills the gauge including the bulb B and capillary C. When the mercury sump is "
      "moved up, the level in the gauge rises and when it reaches the cut off F a known volume "
      "of gas at pressure to be measured is trapped in bulb B and capillary C.")
    FIG(3, F2.fig_f03())

    H("Đồng hồ ion hóa", "Ionization gauge", h3)
    P("Đồng hồ ion hóa là loại nhạy nhất cho áp suất rất thấp (chân không cao, còn gọi là “cứng”). "
      "Chúng cảm nhận áp suất gián tiếp bằng cách đo các ion điện tạo ra khi khí bị bắn phá bởi "
      "electron. Khí có mật độ thấp hơn tạo ra ít ion hơn. Độ hiệu chỉnh của đồng hồ ion không ổn "
      "định và phụ thuộc vào bản chất khí đo, vốn không phải lúc nào cũng biết rõ. Có thể hiệu "
      "chỉnh chúng so với đồng hồ McLeod ổn định hơn và không phụ thuộc vào thành phần hóa học.",
      "Ionization gauges are the most sensitive gauges for very low pressures (high vacuums, AKA "
      "'hard' vacuums). They sense pressure indirectly by measuring the electrical ions produced "
      "when the gas is bombarded with electrons. Fewer ions will be produced by lower density "
      "gases. The calibration of an ion gauge is unstable and dependent on the nature of the "
      "gases being measured, which is not always known. They can be calibrated against a McLeod "
      "gauge which is much more stable and independent of chemistry.")
    P("Sự phát xạ nhiệt điện tạo ra các electron va chạm với nguyên tử khí và sinh ion dương. Các "
      "ion bị hút về một điện cực phân cực thích hợp gọi là collector. Dòng trong collector tỉ lệ "
      "với tốc độ ion hóa, là hàm của áp suất trong hệ thống. Vì vậy, đo dòng collector cho biết "
      "áp suất khí. Có vài loại phụ của đồng hồ ion hóa.",
      "Thermionic emission generate electrons, which collide with gas atoms and generate positive "
      "ions. The ions are attracted to a suitably biased electrode known as the collector. The "
      "current in the collector is proportional to the rate of ionization, which is a function of "
      "the pressure in the system. Hence, measuring the collector current gives the gas pressure. "
      "There are several sub-types of ionization gauge.")
    P("Dải hữu ích: 10⁻¹⁰ − 10⁻³ torr (xấp xỉ 10⁻⁸ − 10⁻¹ Pa). Hầu hết đồng hồ ion có hai loại: "
      "catốt nóng và catốt lạnh; có loại thứ ba nhạy hơn và đắt hơn gọi là đồng hồ rô-to quay "
      "(spinning rotor gauge), nhưng không được bàn ở đây.",
      "Useful range: 10-10 - 10-3 torr (roughly 10-8 - 10-1 Pa). Most ion gauges come in two types: "
      "hot cathode and cold cathode, a third type exists which is more sensitive and expensive "
      "known as a spinning rotor gauge, but is not discussed here.")
    P("Ở loại catốt nóng, một dây đốt nóng bằng điện tạo chùm electron. Các electron đi qua đồng "
      "hồ và ion hóa phân tử khí xung quanh. Ion sinh ra được thu ở một điện cực âm. Dòng phụ "
      "thuộc vào số ion, mà số ion lại phụ thuộc áp suất trong đồng hồ. Đồng hồ catốt nóng chính "
      "xác từ 10⁻³ Torr đến 10⁻¹⁰ Torr. Nguyên lý của loại catốt lạnh giống nhau, chỉ khác là "
      "electron được tạo ra trong một sự phóng điện cao áp. Đồng hồ catốt lạnh chính xác từ 10⁻² "
      "Torr đến 10⁻⁹ Torr.",
      "In the hot cathode version an electrically heated filament produces an electron beam. The "
      "electrons travel through the gauge and ionize gas molecules around them. The resulting "
      "ions are collected at a negative electrode. The current depends on the number of ions, "
      "which depends on the pressure in the gauge. Hot cathode gauges are accurate from 10⁻³ "
      "Torr to 10⁻¹⁰ Torr. The principle behind cold cathode version is the same, except that "
      "electrons are produced in a discharge created by a high voltage electrical discharge. "
      "Cold Cathode gauges are accurate from 10⁻² Torr to 10⁻⁹ Torr.")
    P("Hiệu chỉnh đồng hồ ion rất nhạy với hình học cấu tạo, thành phần hóa học của khí đo, sự ăn "
      "mòn và các lớp lắng đọng bề mặt. Hiệu chỉnh có thể bị vô hiệu nếu đồng hồ bị kích hoạt ở "
      "áp suất khí quyển hoặc chân không thấp. Thành phần khí ở chân không cao thường không đoán "
      "trước được, nên phải dùng thêm máy phổ khối cùng với đồng hồ ion để đo chính xác.",
      "Ionization gauge calibration is very sensitive to construction geometry, chemical "
      "composition of gases being measured, corrosion and surface deposits. Their calibration "
      "can be invalidated by activation at atmospheric pressure or low vacuum. The composition "
      "of gases at high vacuums will usually be unpredictable, so a mass spectrometer must be "
      "used in conjunction with the ionization gauge for accurate measurement.")
    P("Đồng hồ ion hóa catốt nóng về cơ bản gồm ba điện cực hoạt động như một triode, trong đó "
      "catốt là dây đốt. Ba điện cực là một collector (bản thu), một dây đốt và một lưới. Dòng "
      "collector được đo bằng picoampere nhờ một thiết bị đo điện (electrometer). Điện áp dây "
      "đốt so với đất thường ở mức 30 volt, trong khi điện áp lưới là 180–210 V DC, trừ khi có "
      "tính năng bắn phá electron tùy chọn bằng cách đốt nóng lưới, khi đó điện áp có thể tới "
      "khoảng 565 volt. Đồng hồ ion phổ biến nhất là đồng hồ Bayard-Alpert catốt nóng, với bộ thu "
      "ion nhỏ nằm bên trong lưới. Vỏ thủy tinh có lỗ mở tới chân không có thể bao quanh các điện "
      "cực, nhưng thường thì đồng hồ dạng trần (Nude Gauge) được đưa trực tiếp vào buồng chân "
      "không, các chân dẫn xuyên qua một tấm gốm trên thành buồng. Đồng hồ catốt nóng có thể hư "
      "hỏng hoặc mất hiệu chỉnh nếu tiếp xúc áp suất khí quyển, thậm chí chân không thấp, khi còn "
      "nóng. Các phép đo của đồng hồ ion hóa catốt nóng luôn có tính logarithm.",
      "A hot cathode ionization gauge is mainly composed of three electrodes all acting as a "
      "triode, where the cathode is the filament. The three electrodes are a collector or plate, "
      "a filament, and a grid. The collector current is measured in picoamps by an electrometer. "
      "The filament voltage to ground is usually at a potential of 30 volts while the grid "
      "voltage at 180–210 volts DC, unless there is an optional electron bombardment feature, "
      "by heating the grid which may have a high potential of approximately 565 volts. The most "
      "common ion gauge is the hot cathode Bayard-Alpert gauge, with a small ion collector inside "
      "the grid. A glass envelope with an opening to the vacuum can surround the electrodes, but "
      "usually the Nude Gauge is inserted in the vacuum chamber directly, the pins being fed "
      "through a ceramic plate in the wall of the chamber. Hot cathode gauges can be damaged or "
      "lose their calibration if they are exposed to atmospheric pressure or even low vacuum "
      "while hot. The measurements of a hot cathode ionization gauge are always logarithmic.")
    P("Electron do dây đốt phát ra đi qua lưới nhiều lần theo chuyển động qua lại trước khi cuối "
      "cùng vào lưới. Trong các chuyển động này, một số electron va chạm với phân tử khí tạo thành "
      "một cặp gồm một ion và một electron (ion hóa do electron). Số ion này tỉ lệ với mật độ phân "
      "tử khí nhân với dòng electron phát ra từ dây đốt, và các ion đổ vào collector tạo thành "
      "dòng ion. Vì mật độ phân tử khí tỉ lệ với áp suất, áp suất được suy ra bằng cách đo dòng ion.",
      "Electrons emitted from the filament move several times in back and forth movements around "
      "the grid before finally entering the grid. During these movements, some electrons collide "
      "with a gaseous molecule to form a pair of an ion and an electron (Electron ionization). "
      "The number of these ions is proportional to the gaseous molecule density multiplied by the "
      "electron current emitted from the filament, and these ions pour into the collector to "
      "form an ion current. Since the gaseous molecule density is proportional to the pressure, "
      "the pressure is estimated by measuring the ion current.")
    P("Độ nhạy áp suất thấp của đồng hồ catốt nóng bị giới hạn bởi hiệu ứng quang điện. Electron "
      "đập vào lưới sinh tia X gây nhiễu quang điện trong collector ion. Điều này giới hạn dải "
      "của đồng hồ catốt nóng cũ ở 10⁻⁸ Torr và của Bayard-Alpert ở khoảng 10⁻¹⁰ Torr. Các dây "
      "bổ sung ở điện thế catốt nằm trong đường ngắm giữa collector ion và lưới ngăn ngừa hiệu "
      "ứng này.",
      "The low pressure sensitivity of hot cathode gauges is limited by the photoelectric effect. "
      "Electrons hitting the grid produce x-rays that produce photoelectric noise in the ion "
      "collector. This limits the range of older hot cathode gauges to 10⁻⁸ Torr and the "
      "Bayard-Alpert to about 10⁻¹⁰ Torr. Additional wires at cathode potential in the line of "
      "sight between the ion collector and the grid prevent this effect.")
    P("Trong loại dạng chiết (extraction type), ion không bị hút bởi một dây mà bởi một hình nón "
      "mở. Vì ion không “quyết định” được phần nào của hình nón sẽ đập vào, chúng đi qua lỗ và "
      "tạo thành chùm ion. Chùm ion này có thể được đưa tới:",
      "In the extraction type the ions are not attracted by a wire, but by an open cone. As the "
      "ions cannot decide which part of the cone to hit, they pass through the hole and form an "
      "ion beam. This ion beam can be passed on to a")
    U(["Faraday cup (cốc Faraday) / Faraday cup",
       "Máy dò đĩa vi kênh với cốc Faraday / Microchannel plate detector with Faraday cup",
       "Máy phân tích khối bốn cực với cốc Faraday / Quadrupole mass analyzer with Faraday cup",
       "Máy phân tích khối bốn cực với máy dò đĩa vi kênh và cốc Faraday / Quadrupole mass "
       "analyzer with Microchannel plate detector Faraday cup",
       "Thấu kính ion và điện áp gia tốc hướng tới mục tiêu để tạo súng phun / ion lens and "
       "acceleration voltage directed at a target to form a sputter gun. Trong trường hợp này, "
       "một van cho khí vào lồng lưới / In this case a valve lets gas into the grid-cage."],
      ["Faraday cup",
       "Microchannel plate detector with Faraday cup",
       "Quadrupole mass analyzer with Faraday cup",
       "Quadrupole mass analyzer with Microchannel plate detector Faraday cup",
       "ion lens and acceleration voltage and directed at a target to form a sputter gun. In this "
       "case a valve lets gas into the grid-cage."])

    # ---------------------------------------------------------------- 2.3
    H("2.3 Đồng hồ hiệu ứng phóng xạ nhiệt", "2.3 Radiometer-Effect Gauges")
    P("Hiệu ứng nhiệt phân tử được Crookes chứng minh bằng thực nghiệm năm 1873 đã được Knudsen "
      "dùng năm 1910 để đo áp suất. Để giải thích hiệu ứng này, xét hai bản song song phẳng 1 và 2 "
      "có cùng diện tích nhưng ở nhiệt độ khác nhau T1 và T2.",
      "The thermal molecular pressure experimentally demonstrated by Crookes in 1873 was used by "
      "Knudsen in 1910 for the measurement of pressures. To explain this effect we consider two "
      "planeparallel plates 1 and 2 with the same area but different temperatures T1 and T2.")
    FIG(4, F2.fig_f04())
    P("Khoảng cách d giữa hai bản có thể nhỏ so với đường tự do trung bình Λ, sao cho d &lt; Λ/10. "
      "Giả sử T1 &gt; T2 (T2 cũng có thể là nhiệt độ môi trường), các hạt khí đi từ bản 1 tới bản "
      "2 có va chạm mạnh hơn các hạt đi từ môi trường tới mặt kia của bản 2. Do đó, có vẻ như hai "
      "mặt của bản 2 chịu các áp suất khác nhau. Chênh áp của chúng có thể tính bằng các định luật "
      "nổi tiếng của thuyết động học chất khí theo phương trình sau:",
      "The distance d between the two plates may be small compared with the mean free path "
      "length Λ, so that d &lt; Λ/10. Assuming T1 &gt; T2 (T2 may also be the temperature of the "
      "surroundings) gas particles travelling from plate 1 to plate 2 have a higher impact than "
      "gas particles coming from the surroundings to the other side of plate 2. Thus, different "
      "pressures seem to act onto the two sides of plate 2. Their difference can be calculated "
      "with the help of the known laws of the kinetic theory of gases by the following equation:")
    EQ("Δp = (p/2)·[√(T<sub>2</sub>/T<sub>1</sub>)·(2−α<sub>1</sub>)/α<sub>1</sub> "
       "− (2−α<sub>2</sub>)/α<sub>2</sub>]   (1)")
    P("trong đó α1 và α2 lần lượt là hệ số thích ứng (accommodation coefficients) của bản 1 và "
      "bản 2.",
      "where α1 and α2 are the accommodation coefficients of the plate 1 and 2 respectively.")
    P("Theo Hình 5, có thể treo bản 2 theo cách dùng trong galvanometer. Chênh áp gây chuyển động "
      "cho bản 2. Mô-men đàn hồi của sợi treo cố gắng bù lại mô-men do chênh áp ở hai mặt bản 2 "
      "gây ra. Như vậy, ở trạng thái cân bằng, sự xoắn của bản 2 cho biết áp suất.",
      "According to Figure 5 one can suspend plate 2 in the manner used for galvanometers. The "
      "pressure difference effects movement of plate 2. The elastic moment of the suspension "
      "tries to compensate the momentum caused by the pressure difference at the two sides of "
      "plate 2. Thus, in the equilibrium the torsion of plate 2 indicates the pressure.")
    FIG(5, F2.fig_f05())
    FIG(6, F2.fig_f06())
    P("Theo Phương trình 1, phương pháp đo áp suất này không phụ thuộc vào loại khí. Một số phiên "
      "bản của thiết bị có giới hạn áp suất thấp khoảng 10⁻⁸ mbar. Vì đồng hồ loại này rất nhạy "
      "với rung động và va chạm, hiện không được dùng trong công nghiệp.",
      "According to Equation 1 this method of pressure measurement is independent of the kind of "
      "gas. Some versions of this equipment have a low-pressure limit of about 10⁻⁸ mbar. Because "
      "this type of gauge is very sensitive to vibrations and impact it is not used "
      "industrially today")

    # ---------------------------------------------------------------- 2.4
    H("2.4 Cảm biến áp suất điện tử", "2.4 Electronic pressure sensors")
    P("Cảm biến áp suất đo áp suất, thường là của chất khí hoặc chất lỏng. Nói chung cảm biến áp "
      "suất hoạt động như một bộ chuyển đổi (transducer); nó tạo tín hiệu điện như hàm của áp "
      "suất tác dụng. Dù có nhiều loại bộ chuyển đổi áp suất, một trong những loại phổ biến nhất "
      "là bộ chuyển đổi dựa trên strain gage. Việc biến áp suất thành tín hiệu điện được thực hiện "
      "nhờ biến dạng vật lý của các strain gage dán vào màng của bộ chuyển đổi. Áp suất tác dụng "
      "làm màng bị lệch, gây biến dạng cho các gage. Biến dạng này tạo ra sự thay đổi điện trở "
      "tỉ lệ với áp suất.",
      "A pressure sensor measures pressure, typically of gases or liquids. A pressure sensor "
      "usually acts as a transducer; it generates an electronic signal as a function of the "
      "pressure imposed. Although there are various types of pressure transducers, one of the "
      "most common is the strain-gage base transducer. The conversion of pressure into an "
      "electrical signal is achieved by the physical deformation of strain gages which are "
      "bonded into the diaphragm of the pressure transducer. Pressure applied to the pressure "
      "transducer produces a deflection of the diaphragm which introduces strain to the gages. "
      "The strain will produce an electrical resistance change proportional to the pressure.")
    FIG(7, F2.fig_f07())

    H("Hiệu chỉnh", "Calibration", h3)
    P("Hiệu chỉnh là sự so sánh giữa các phép đo — một phép đo có độ lớn hoặc độ đúng biết trước "
      "được thực hiện hoặc thiết lập bằng thiết bị này, và một phép đo khác được thực hiện theo "
      "cách tương tự nhất có thể với thiết bị thứ hai. Thiết bị có độ đúng biết trước hoặc được "
      "gán cho gọi là chuẩn (standard).",
      "Calibration is a comparison between measurements - one of known magnitude or correctness "
      "made or set with one device and another measurement made in as similar a way as possible "
      "with a second device. The device with the known or assigned correctness is called the "
      "standard.")
    P("Quá trình hiệu chỉnh bắt đầu từ thiết kế của thiết bị đo cần hiệu chỉnh. Thiết kế phải có "
      "khả năng “giữ hiệu chỉnh” trong suốt khoảng thời gian hiệu chỉnh. Nói cách khác, thiết kế "
      "phải có khả năng cho các phép đo “nằm trong dung sai kỹ thuật” khi dùng trong các điều kiện "
      "môi trường đã nêu trong một khoảng thời gian hợp lý.",
      "The calibration process begins with the design of the measuring instrument that needs to "
      "be calibrated. The design has to be able to 'hold a calibration' through its calibration "
      "interval. In other words, the design has to be capable of measurements that are 'within "
      "engineering tolerance' when used within the stated environmental conditions over some "
      "reasonable period of time.")
    P("Giả sử bạn có một đồng hồ Bourdon cũ, thang đo không chính xác — nhưng bản thân thiết bị "
      "vẫn hoạt động. Sau quá trình hiệu chỉnh, đồng hồ có thể dùng lại với độ chính xác cao vì "
      "hiệu chỉnh thiết lập được mối quan hệ giữa giá trị “đọc” và “thật” là preal = f(pread), "
      "ví dụ dưới dạng “biểu đồ hiệu chỉnh”.",
      "Suppose that one owns an old Bourdon gauge, whose scale is inaccurate – yet the device "
      "itself is working. After a calibration process the gauge can be used again with high "
      "accuracy as the calibration results in a relationship between the 'read' and 'real' value "
      "as preal=f(pread), e.g. in the form of a 'calibration diagram'.")

    H("Đo lưu lượng", "Measuring flow rate", h3)
    H("Bình đo (xô và đồng hồ bấm giờ)", "Metering tank (bucket-and-stopwatch)", h4)
    P("Có lẽ cách đơn giản nhất để đo lưu lượng thể tích là đo thời gian cần để lấp đầy một bình "
      "có thể tích biết trước. Ví dụ đơn giản là dùng một cái xô thể tích biết được chất đầy chất "
      "lỏng. Đồng hồ bấm giờ được khởi động khi dòng chảy bắt đầu và dừng khi xô tràn. Thể tích "
      "chia cho thời gian cho lưu lượng:",
      "Perhaps the simplest way to measure volumetric flow is to measure how long it takes to "
      "fill a known volume container. A simple example is using a bucket of known volume, filled "
      "by a fluid. The stopwatch is started when the flow starts, and stopped when the bucket "
      "overflows. The volume divided by the time gives the flow:")
    EQ("Q = α·Δm/Δt")
    U(["α [dm³/mm] là hằng số của bình, bằng thể tích của một lượng chất lỏng cao 1 mm trong bình / "
       "α [dm3/mm] is the constant of the tank being the volume of a 1 mm high quantity of liquid "
       "in the tank",
       "Δm [mm] là độ dâng của mức chất lỏng / Δm [mm] is the rising of the level",
       "Δt [s] là thời gian dâng / Δt [s] is the time taken for rising"],
      ["α [dm3/mm] is the constant of the tank being the volume of a 1 mm high quantity of liquid "
       "in the tank",
       "Δm [mm] is the rising of the level",
       "Δt [s] is the time taken for rising"])
    H("Tấm lỗ đo (orifice plate)", "Orifice plate", h4)
    P("Tấm lỗ đo (metering orifice) là một tấm có lỗ xuyên qua, được đặt trong dòng chảy; nó làm "
      "thắt hẹp dòng, và đo chênh áp qua chỗ thắt hẹp cho biết lưu lượng.",
      "An orifice plate (metering orifice) is a plate with a hole through it, placed in the flow; "
      "it constricts the flow, and measuring the pressure differential across the constriction "
      "gives the flow rate.")
    FIG(8, F2.fig_f08())
    P("Căn bậc hai của chênh áp đo được tỉ lệ với lưu lượng:",
      "The square root of measured pressure difference is proportional to the flow rate:")
    EQ("Q = K·√(Δp)")
    P("trong đó K là hằng số (cách tính của nó được các tiêu chuẩn mô tả).",
      "where K is constant (its computation is described by standards).")

    # ---------------------------------------------------------------- 2.5
    H("2.5 Đồng hồ dẫn nhiệt", "2.5 Thermal conductivity gauges")
    P("Nguyên lý làm việc của đồng hồ dẫn nhiệt là ở áp suất thấp, nhiệt lượng mất đi của một vật "
      "bị nóng qua dẫn nhiệt bởi các phân tử phụ thuộc vào áp suất. Điều này chỉ đúng trong một "
      "dải áp suất nhất định.",
      "The working principle of thermal conductivity gauges is that at low pressures heat lost "
      "by a heated object by conduction through molecules will depend on pressure. This is valid "
      "only for certain pressure range.")
    P("Khi đường tự do trung bình tương đương với kích thước của đầu đo, nhiệt mất đi từ dây nóng "
      "trong đầu đo gồm (i) dẫn qua các dây nối, (ii) bức xạ ra môi trường và (iii) dẫn qua các "
      "phân tử.",
      "When the mean free path is comparable with the dimensions of the gauge head the heat loss "
      "from a heated wire in the gauge head will be by (i) conduction through leads (ii) "
      "radiation to surroundings (iii) conduction through molecules.")
    FIG(9, F2.fig_f09())
    P("Dải của đồng hồ dẫn nhiệt từ mm Hg đến 10⁻³ mm Hg. Ở áp suất cao hơn, nhiệt mất từ dây "
      "nóng không nhạy với sự thay đổi áp suất. Ở áp suất thấp hơn, nhiệt mất theo (i) và (ii) "
      "trở nên đáng kể hơn. Có hai loại đồng hồ thermocouple.",
      "The range of thermal conductivity gauges is from mm of Hg to 10⁻³mmHg. At higher pressures, "
      "heat loss from the heated wire is insensitive to the pressure change. At lower pressure "
      "heat loss by (i) and (ii) become more significant. There are two kinds of the "
      "thermocouple gauges.")
    H("Đồng hồ Pirani", "Pirani gauge", h4)
    P("Đo sự thay đổi điện trở của dây nóng khi dây mất nhiệt cho các phân tử khí trong đầu đo. "
      "Trong trường hợp này đồng hồ được gọi là đồng hồ Pirani.",
      "Measures change in resistance of the heated wire when it looses heat to the gas molecules "
      "in the gauge head. In this case the gauge is called pirani gauge.")
    H("Đồng hồ thermocouple", "Thermocouple gauge", h4)
    P("Thay vì đo điện trở, một cặp nhiệt điện được giữ tiếp xúc với dây nóng và nhiệt độ của dây "
      "được đo trực tiếp như thước đo áp suất.",
      "Instead of measuring electrical resistance, a thermocouple is kept in contact with the "
      "heated wire and the temperature of the wire is directly measured as a measure of pressure.")
    FIG(10, F2.fig_f10())

    # ---------------------------------------------------------------- 2.6
    H("2.6 Đồng hồ ion hóa catốt nóng", "2.6 Hot cathode ionisation gauges")
    P("Ở mức chân không cao hơn, phép đo áp suất dùng đồng hồ ion hóa (Ionisation gauges). Chúng "
      "hoạt động trên nguyên lý ion hóa khí nhờ electron do một dây đốt nóng phát ra. Năng lượng "
      "động học mà một electron thu được khi đi qua hiệu điện thế V volt có giá trị bằng V·e, "
      "trong đó e là điện tích của electron. Khi năng lượng này vượt quá một giá trị tới hạn tương "
      "ứng với thế ion hóa Vi, va chạm giữa phân tử và electron có thể tạo ion dương. Các electron "
      "có vận tốc tương đối cao khi đập vào phân tử khí đẩy một electron ra khỏi phân tử, để lại "
      "điện tích dương. Với các khí như N2, O2 thì Vi ≈ 15 volt. Việc đo các ion tạo ra là thước "
      "đo áp suất. Electron được tăng tốc bởi một trường điện và các ion dương tạo ra được thu "
      "lại. Số ion dương tạo ra phụ thuộc vào số phân tử, do đó phụ thuộc vào áp suất.",
      "At higher levels of vacuum, the measurement of pressure is by using Ionisation gauges. They "
      "operate on the principle of ionising the gas by means of electrons emitted by a heated "
      "filament. The kinetic energy acquired by an electron in passing through a potential "
      "difference of V volts corresponds to a value equal to V*e where e is the charge of the "
      "electron. When this energy exceeds a certain critical value corresponding to the "
      "ionization potential Vi, there is a possibility that collisions between molecules and "
      "electrons will result in the formation of +ve ions. The relatively high velocity electrons "
      "on hitting a gas molecule drives an electron out of it leaving it positively charged. For "
      "gases such as N2, O2 etc, Vi is ~ 15volts. The measurement of the ions produced is a measure "
      "of the pressure. The electrons are speeded up by an electric field and +ve ions produced "
      "are collected. The number of +ve ions formed will depend on the number of molecules and "
      "therefore on the pressure.")
    EQ("E = V·e")
    FIG(11, F2.fig_f11())
    P("Đồng hồ gồm một catốt, lưới anode và một bản âm. Bản âm có điện thế khoảng −10 V so với "
      "catốt. Electron do catốt nóng (dây đốt) phát ra được tăng tốc bởi trường điện, còn ion "
      "dương tạo ra được bản âm thu lại.",
      "The gauge consists of a cathode, grid anode and a negative plate. The negative plate is at "
      "~10V negative with respect to the cathode. The electrons emitted by the hot cathode "
      "(filament) are speeded up by the electric field and the positive ions produced are "
      "collected by the negative plate.")
    H("Đồng hồ ion hóa catốt lạnh (Penning)", "Cold cathode ionisation gauge (Penning gauge)", h4)
    P("Đồng hồ này cũng hoạt động theo nguyên lý ion hóa. Ion dương do electron tạo ra và dòng do "
      "các ion này tạo ra cho biết áp suất. Electron được bắn ra từ catốt lạnh làm bằng zirconium "
      "hoặc thorium nhờ phóng điện. Đồng hồ gồm hai bản catốt và một anode dạng vòng. Điện thế "
      "khoảng 2 kV được đặt giữa các điện cực.",
      "This gauge also works on the ionization principle. Positive ions are produced by the "
      "electrons and current due to these ions gives a measure of the pressure. Electrons are "
      "ejected from a cold cathode of Zirconium, Thorium by electric discharge. The gauge consists "
      "of two plate cathodes and a ring anode. A potential difference of ~2KV is applied across "
      "the electrodes.")
    P("Quãng đường đi của electron được kéo dài hơn nhiều. Các electron thứ cấp được cho đi theo "
      "đường xoắn ốc trước khi tới anode. Điều này được thực hiện nhờ một từ trường. Các cực từ "
      "được bố trí sao cho từ thông với các đường sức tác dụng vuông góc với hai bản catốt.",
      "The travel of electrons is made over a much longer distance. The secondary electrons are "
      "made to travel in helical paths before reaching the anode. This is accomplished by a "
      "magnetic field. Magnetic poles are kept such that the flux with lines of force is applied "
      "perpendicular to the two cathodes.")
    FIG(12, F2.fig_f12())

    # ---------------------------------------------------------------- 2.7
    H("2.7 Đồng hồ Pirani", "2.7 PIRANI'S GAUGE")
    P("Đồng hồ Pirani gồm một dây đốt kim loại (thường là platinum) treo trong một ống nối với hệ "
      "thống cần đo chân không. Kết nối thường được thực hiện bằng khớp thủy tinh mài hoặc đầu nối "
      "kim loại có bích, được làm kín bằng vòng chữ O. Dây đốt được nối vào một mạch điện, từ đó "
      "sau khi hiệu chỉnh có thể đọc áp suất.",
      "The Pirani gauge consists of a metal filament (usually platinum) suspended in a tube which "
      "is connected to the system whose vacuum is to be measured. Connection is usually made "
      "either by a ground glass joint or a flanged metal connector, sealed with an o-ring. The "
      "filament is connected to an electrical circuit from which, after calibration, a pressure "
      "reading may be taken.")
    P("Một dây dẫn (dây đốt platinum) nóng lên khi dòng điện chạy qua. Dây này treo trong khí sẽ "
      "mất nhiệt cho khí khi các phân tử va chạm vào dây và lấy đi nhiệt. Khi áp suất khí giảm "
      "(nhờ bơm chân không), số phân tử giảm tương ứng, độ dẫn của môi trường giảm và dây mất "
      "nhiệt chậm hơn. Đo nhiệt mất đi là chỉ thị gián tiếp của áp suất.",
      "A conducting wire (platinum filament) gets heated when electric current flows through it. "
      "This wire suspended in a gas will lose heat to the gas as its molecules collide with the "
      "wire and remove heat. As the gas pressure is reduced (by the vacuum pumps) the number of "
      "molecules present will fall proportionately, the conductivity of the surrounding media "
      "will fall and the wire will lose heat more slowly. Measuring the heat loss is an indirect "
      "indication of pressure.")
    P("Điện trở của dây thay đổi theo nhiệt độ, nên đo điện trở cũng cho biết nhiệt độ của dây. "
      "Sự thay đổi điện trở của dây đốt được xác định bằng cầu đo. Độ thay đổi điện trở của dây "
      "Pirani, sau hiệu chỉnh, trở thành thước đo áp suất tác dụng.",
      "The electrical resistance of the wire varies with its temperature, so the measurement of "
      "resistance also indicates the temperature of wire. Now the change in resistance of the "
      "filament is determined using the bridge. This change in resistance of the pirani gauge "
      "filament becomes a measure of the applied pressure when calibrated")
    P("Trong nhiều hệ thống, dây được duy trì ở điện trở không đổi R bằng cách điều khiển dòng I "
      "chạy qua dây. Điện trở có thể được đặt bằng mạch cầu. Công suất cung cấp cho dây là I²·R, "
      "và công suất đó được truyền sang khí. Do đó, dòng cần thiết để đạt được cân bằng này là "
      "thước đo chân không.",
      "In many systems, the wire is maintained at a constant resistance R by controlling the "
      "current I through the wire. The resistance can be set using a bridge circuit. The power "
      "delivered to the wire is I 2 R, and the same power is transferred to the gas. The current "
      "required to achieve this balance is therefore a measure of the vacuum.")
    EQ("P = I²·R")
    P("Đồng hồ có thể dùng cho áp suất từ 0,5 Torr đến 10⁻³ Torr. Độ dẫn nhiệt và nhiệt dung của "
      "khí có thể ảnh hưởng đến kết đọc, vì vậy thiết bị có thể cần hiệu chỉnh trước khi có kết "
      "quả chính xác. Để đo áp suất thấp hơn, người ta dùng các thiết bị khác chẳng hạn đồng hồ "
      "Penning.",
      "The gauge may be used for pressures between 0.5 Torr to 10⁻³ Torr. The thermal "
      "conductivity and heat capacity of the gas may affect the readout from the meter, and "
      "therefore the apparatus may need calibrating before accurate readings are obtainable. "
      "For lower pressure measurement other instruments such as a Penning gauge are used.")

    # ---------------------------------------------------------------- 2.8
    H("2.8 Đồng hồ chân không Penning", "2.8 Penning Vacuum Guage")
    P("Đồng hồ Penning là đồng hồ ion hóa catốt lạnh gồm hai điện cực anode và catốt. Hình trụ "
      "ngoài của đồng hồ là catốt và ở nhiệt độ phòng. Anode gồm một dây tungsten đặt ở giữa ống. "
      "Hiệu điện thế khoảng 2 đến 3 kV được đặt giữa anode và catốt qua các điện trở hạn dòng. "
      "Một từ trường được đưa vào vuông góc với mặt phẳng điện cực nhờ nam châm vĩnh cửu có từ "
      "trường khoảng 800 gauss, làm tăng dòng ion hóa.",
      "The Penning gauge is a cold cathode type ionisation gauge consisting of two electrodes "
      "anode and cathode. The outer cylinder of the gauge is the cathode and is at room "
      "temperature. The anode consists of a tungsten wire mounted in the center of the tube A "
      "potential difference of about 2 to 3 KV is applied between anode and cathode through "
      "current limiting resistors. A magnetic field is introduced at right angles to the plane "
      "of the electrodes by a permanent magnet having nearly 800 gauss magnetic field which will "
      "increase the ionisation current.")
    P("Electron phát ra từ catốt (thân đầu đo) bị từ trường đặt vuông góc với mặt phẳng điện cực "
      "làm lệch hướng và đi theo đường xoắn ốc trước khi tới vòng anode. Nhờ đi đường rất dài, "
      "electron ion hóa khí do va chạm ngay cả ở áp suất thấp. Các electron thứ cấp do ion hóa "
      "tạo ra tự chúng dao động tương tự và tốc độ ion hóa tăng nhanh. Cuối cùng electron bị anode "
      "bắt giữ và trạng thái cân bằng đạt được khi số electron tạo ra mỗi giây do ion hóa bằng "
      "tổng dòng ion dương tới catốt và dòng electron tới anode. Dòng nhỏ này được hiệu chỉnh để "
      "cho biết áp suất khí, và vì thế cho biết áp suất buồng mà đồng hồ được nối vào.",
      "The electrons emitted from the cathode (gauge head body) of the gauge head are deflected by "
      "means of magnetic field applied at right angles to the plane of the electrodes and are "
      "made to take helical path before reaching the anode loop. Thus following very long path, "
      "the electrons ionize the gas by collision, even at low pressures. The secondary electrons "
      "produced by ionisation themselves perform similar oscillations and the rate of ionisation "
      "increases rapidly. Eventually, the electrons are captured by the anode and equilibrium is "
      "reached when the number of electrons produced per second by ionisation is the sum of "
      "positive ion current to the cathode and the electron current to the anode. This small "
      "current is calibrated to give a measure of the pressure of the gas and hence the chamber "
      "to which it is attached.")

    H("2.9 Đồng hồ manometer cân bằng vòng", "2.9 Ring Balance Manometers")
    P("Các đồng hồ này được dùng rộng rãi ở châu Âu nhưng chỉ được chấp nhận hạn chế tại Hoa Kỳ. "
      "Ứng dụng và nguyên lý hoạt động của chúng giống với đồng hồ chuông ngược (inverted bell "
      "meters). Một vòng ống tạo thành trong mặt phẳng thẳng đứng được trục tại tâm, và chênh áp "
      "làm vòng quay. Mô-men chống lại được tạo bởi một trọng lượng gắn vào vòng.",
      "These meters have been widely used in Europe but have found limited acceptance in the "
      "United States. Their application and operating principles are the same as those of the "
      "inverted bell meters. A tubing ring formed in the vertical plane is pivoted at its central "
      "axis, and the pressure differential rotates this ring. The opposing torque is developed by "
      "a weight attached to the ring.")
    P("Tùy theo thiết kế và chất lỏng làm đầy, dải nhỏ nhất của các thiết bị này là 0,2 in. H2O "
      "(0,05 kPa) và dải lớn nhất là 500 in. H2O (125 kPa). Tùy theo áp suất chuẩn dùng, chúng "
      "có thể phát hiện áp suất tuyệt đối hoặc gần khí quyển. Dù vỏ có thể chịu tới 6000 PSIG "
      "(41 MPa), chênh áp giữa áp suất chuẩn và áp suất quá trình phải thấp hơn giới hạn đó, nếu "
      "không chất lỏng làm kín sẽ bị thổi bay. Ở áp suất cao, các kết nối mềm ở đầu dẫn cũng trở "
      "thành nguồn sai số và cần bảo trì liên tục.",
      "Depending on the design and the filling fluid used, the minimum span for these units is "
      "0.2 in. H2O (0.05 kPa) and the maximum span is 500 in. H2O (125 kPa). Depending on the "
      "reference pressure used, it can detect absolute or nearatmospheric pressures. Although "
      "the housings can withstand up to 6000 PSIG (41 MPa), the pressure differential between "
      "reference and process pressure should be below that limit, which would cause the sealing "
      "fluid to be blown out. Also at high pressures the flexible connections at the sensing "
      "leads become a source of errors and require constant maintenance.")

    # ---------------------------------------------------------------- 2.10
    H("2.10 Đồng hồ và công tắc áp suất", "2.10 Pressure gauges and switches")
    P("Phương pháp cơ khí đo áp suất đã được biết đến hàng thế kỷ. Ống manometer chữ U là một "
      "trong những thiết bị chỉ thị áp suất đầu tiên. Ban đầu các ống này làm bằng thủy tinh và "
      "thang được thêm vào khi cần. Nhưng manometer lớn, cồng kềnh và không phù hợp để tích hợp "
      "vào các vòng điều khiển tự động. Vì vậy, manometer thường được dùng trong phòng thí nghiệm "
      "hoặc làm thiết bị chỉ thị tại chỗ. Tùy theo áp suất chuẩn dùng, chúng có thể chỉ áp suất "
      "tuyệt đối, gauge hoặc chênh áp.",
      "Mechanical methods of measuring pressure have been known for centuries. U-tube "
      "manometers were among the first pressure indicators. Originally, these tubes were made of "
      "glass, and scales were added to them as needed. But manometers are large, cumbersome, and "
      "not well suited for integration into automatic control loops. Therefore, manometers are "
      "usually found in the laboratory or used as local indicators. Depending on the reference "
      "pressure used, they could indicate absolute, gauge, and differential pressure.")
    P("Bộ chuyển đổi chênh áp thường được dùng trong đo lưu lượng, nơi chúng đo chênh áp qua "
      "venturi, lỗ đo hoặc một phần tử chính khác. Chênh áp phát hiện liên quan tới vận tốc dòng "
      "và do đó tới lưu lượng thể tích. Nhiều tính năng của bộ phát áp suất hiện đại có nguồn gốc "
      "từ bộ chuyển đổi chênh áp. Thậm chí có thể coi bộ phát chênh áp là mẫu hình cho mọi bộ "
      "chuyển đổi áp suất.",
      "Differential pressure transducers often are used in flow measurement where they can "
      "measure the pressure differential across a venturi, orifice, or other type of primary "
      "element. The detected pressure differential is related to flowing velocity and therefore "
      "to volumetric flow. Many features of modern pressure transmitters have come from the "
      "differential pressure transducer. In fact, one might consider the differential pressure "
      "transmitter the model for all pressure transducers.")
    P("Áp suất “gauge” được định nghĩa tương đối với điều kiện khí quyển. Ở những nơi trên thế "
      "giới còn dùng đơn vị Anh, áp suất gauge được ký hiệu bằng cách thêm chữ “g” vào đơn vị. "
      "Vì vậy đơn vị “pound trên inch vuông gauge” được viết tắt là psig. Khi dùng đơn vị SI, "
      "nên thêm “gauge” vào đơn vị, chẳng hạn “Pa gauge.” Khi cần đo áp suất tuyệt đối, mốc "
      "tham chiếu là chân không hoàn toàn và tên “pound trên inch vuông tuyệt đối” được viết tắt "
      "là psia.",
      "'Gauge' pressure is defined relative to atmospheric conditions. In those parts of the "
      "world that continue to use English units, gauge pressure is indicated by adding a 'g' to "
      "the units descriptor. Therefore, the pressure unit 'pounds per square inch gauge' is "
      "abbreviated psig. When using SI units, it is proper to add 'gauge' to the units used, such "
      "as 'Pa gauge.' When pressure is to be measured in absolute units, the reference is full "
      "vacuum and the abbreviation for 'pounds per square inch absolute' is psia.")
    P("Thường thì các thuật ngữ đồng hồ áp suất, cảm biến, bộ chuyển đổi và bộ phát được dùng "
      "thay thế cho nhau. Đồng hồ áp suất thường chỉ một thiết bị chỉ thị tự chứa biến áp suất "
      "quá trình phát hiện thành chuyển động cơ học của kim. Bộ chuyển đổi áp suất có thể kết hợp "
      "phần tử cảm biến của đồng hồ với bộ chuyển đổi cơ–điện hoặc cơ–khí nén và nguồn cấp. Bộ "
      "phát áp suất là một gói đo áp suất chuẩn gồm ba thành phần cơ bản: bộ chuyển đổi áp suất, "
      "nguồn cấp của nó và bộ điều hòa tín hiệu/phát lại chuyển tín hiệu của bộ chuyển đổi thành "
      "tín hiệu đầu ra chuẩn hóa.",
      "Often, the terms pressure gauge, sensor, transducer, and transmitter are used "
      "interchangeably. The term pressure gauge usually refers to a self-contained indicator that "
      "converts the detected process pressure into the mechanical motion of a pointer. A pressure "
      "transducer might combine the sensor element of a gauge with a mechanical-to-electrical or "
      "mechanical-to-pneumatic converter and a power supply. A pressure transmitter is a "
      "standardized pressure measurement package consisting of three basic components: a pressure "
      "transducer, its power supply, and a signal conditioner/retransmitter that converts the "
      "transducer signal into a standardized output.")
    P("Bộ phát áp suất có thể gửi áp suất quá trình cần đo bằng tín hiệu khí nén tương tự (3-15 "
      "psig), điện tương tự (4-20 mA DC) hoặc điện số. Khi bộ chuyển đổi được nối trực tiếp với "
      "hệ thống thu thập dữ liệu số và đặt xa phần cứng thu thập, tín hiệu điện áp cao được ưu "
      "tiên. Các tín hiệu này phải được bảo vệ khỏi nhiễu điện từ và nhiễu tần số vô tuyến "
      "(EMI/RFI) khi đi quãng đường dài.",
      "Pressure transmitters can send the process pressure of interest using an analog pneumatic "
      "(3-15 psig), analog electronic (4-20 mA dc), or digital electronic signal. When "
      "transducers are directly interfaced with digital data acquisition systems and are located "
      "at some distance from the data acquisition hardware, high output voltage signals are "
      "preferred. These signals must be protected against both electromagnetic and radio "
      "frequency interference (EMI/RFI) when traveling longer distances.")
    P("Các thuật ngữ liên quan đến hiệu năng của bộ chuyển đổi áp suất cũng cần được định nghĩa. "
      "Độ chính xác của bộ chuyển đổi là mức độ phù hợp của giá trị đo với một chuẩn được chấp "
      "nhận, thường expressed as a percentage of full scale or of the actual reading. Với thiết "
      "bị phần trăm toàn thang, sai số tăng khi giá trị đo tuyệt đối giảm. Độ lặp lại là mức độ "
      "khớp nhau giữa nhiều phép đo liên tiếp cùng một biến. Tính tuyến tính cho biết đầu ra "
      "tăng tuyến tính tốt thế nào khi áp suất tăng. Sai số trễ (hysteresis) mô tả hiện tượng cùng "
      "một áp suất quá trình cho các tín hiệu đầu ra khác nhau tùy theo áp suất được tiếp cận từ "
      "phía thấp hơn hay cao hơn.",
      "Pressure transducer performance-related terms also require definition. Transducer accuracy "
      "refers to the degree of conformity of the measured value to an accepted standard. It is "
      "usually expressed as a percentage of either the full scale or of the actual reading of the "
      "instrument. In case of percent-full-scale devices, error increases as the absolute value of "
      "the measurement drops. Repeatability refers to the closeness of agreement among a number "
      "of consecutive measurements of the same variable. Linearity is a measure of how well the "
      "transducer output increases linearly with increasing pressure. Hysteresis error describes "
      "the phenomenon whereby the same process pressure results in different output signals "
      "depending upon whether the pressure is approached from a lower or higher pressure.")

    # ---------------------------------------------------------------- 2.11
    H("2.11 Từ cơ khí sang điện tử", "2.11 From Mechanical to Electronic")
    P("Những đồng hồ áp suất đầu tiên dùng phần tử mềm làm cảm biến. Khi áp suất thay đổi, phần "
      "tử mềm dịch chuyển và chuyển động này được dùng để quay kim trước mặt số. Trong các cảm "
      "biến áp suất cơ khí này, ống Bourdon, màng hoặcbellows phát hiện áp suất quá trình và gây "
      "chuyển động tương ứng.",
      "The first pressure gauges used flexible elements as sensors. As pressure changed, the "
      "flexible element moved, and this motion was used to rotate a pointer in front of a dial. "
      "In these mechanical pressure sensors, a Bourdon tube, a diaphragm, or a bellows element "
      "detected the process pressure and caused a corresponding movement.")
    P("Ống Bourdon có dạng chữ C và mặt cắt oval, một đầu nối với áp suất quá trình (Hình 13 A). "
      "Đầu kia bịt kín và nối với cơ cấu kim hoặc bộ phát. Để tăng độ nhạy, phần tử ống Bourdon "
      "có thể kéo dài thành dạng xoắn ốc hoặc ốc vít (Hình 13 B và 13 C). Điều này tăng chiều "
      "dài góc hữu dụng, do đó tăng chuyển động ở đầu ống, lần lượt làm tăng độ phân giải của bộ "
      "chuyển đổi.",
      "A Bourdon tube is C-shaped and has an oval cross-section with one end of the tube "
      "connected to the process pressure (Figure 13 A). The other end is sealed and connected to "
      "the pointer or transmitter mechanism. To increase their sensitivity, Bourdon tube "
      "elements can be extended into spirals or helical coils (Figures 13 B and 13 C). This "
      "increases their effective angular length and therefore increases the movement at their "
      "tip, which in turn increases the resolution of the transducer.")
    FIG(13, F2.fig_f13())
    FIG(14, F2.fig_f14())
    P("Họ phần tử cảm biến áp suất mềm cũng gồm bellows và màng (Hình 14). Màng được ưa dùng vì "
      "cần ít không gian hơn và vì chuyển động (hoặc lực) chúng tạo ra đủ để vận hành bộ chuyển "
      "đổi điện tử. Chúng cũng có sẵn trong nhiều vật liệu cho các ứng dụng ăn mòn.",
      "The family of flexible pressure sensor elements also includes the bellows and the "
      "diaphragms (Figure 14). Diaphragms are popular because they require less space and because "
      "the motion (or force) they produce is sufficient for operating electronic transducers. "
      "They also are available in a wide range of materials for corrosive service applications.")
    P("Sau những năm 1920, hệ thống điều khiển tự động phát triển và đến những năm 1950, bộ phát "
      "áp suất cùng phòng điều khiển tập trung trở nên phổ biến. Vì vậy, đầu tự do của ống "
      "Bourdon (bellows hoặc màng) không còn phải nối với kim tại chỗ mà phục vụ việc biến áp "
      "suất quá trình thành tín hiệu phát đi (điện hoặc khí nén). Ban đầu, liên kết cơ học được "
      "nối với bộ phát áp suất khí nén, thường tạo tín hiệu đầu ra 3-15 psig để truyền đi hàng "
      "trăm feet, hoặc xa hơn nhờ bộ lặp tăng áp. Sau đó, khi điện tử thể rắn chín muồi và khoảng "
      "cách truyền tăng lên, bộ phát áp suất trở thành điện tử. Các thiết kế đầu tiên tạo đầu ra "
      "điện áp DC (10-50 mV; 1-5 V; 0-100 mV), nhưng sau được chuẩn hóa thành tín hiệu dòng DC "
      "4-20 mA.",
      "After the 1920s, automatic control systems evolved, and by the 1950s pressure transmitters "
      "and centralized control rooms were commonplace. Therefore, the free end of a Bourdon tube "
      "(bellows or diaphragm) no longer had to be connected to a local pointer, but served to "
      "convert a process pressure into a transmitted (electrical or pneumatic) signal. At first, "
      "the mechanical linkage was connected to a pneumatic pressure transmitter, which usually "
      "generated a 3-15 psig output signal for transmission over distances of several hundred "
      "feet, or even farther with booster repeaters. Later, as solid state electronics matured and "
      "transmission distances increased, pressure transmitters became electronic. The early "
      "designs generated dc voltage outputs (10-50 mV; 1-5 V; 0-100 mV), but later were "
      "standardized as 4-20 mA dc current output signals.")
    P("Do những hạn chế cố hữu của thiết bị cơ học cân bằng chuyển động, trước hết thiết bị cân "
      "bằng lực và sau đó bộ chuyển đổi áp suất thể rắn được đưa vào sử dụng. Những strain gage "
      "dây không dán đầu tiên xuất hiện cuối những năm 1930. Trong thiết bị này, sợi dây được gắn "
      "vào một cấu trúc chịu biến dạng và điện trở của dây bị biến dạng được đo. Thiết kế này vốn "
      "không ổn định và không giữ được hiệu chỉnh. Cũng có vấn đề xuống cấp của lớp kết dính giữa "
      "sợi dây và màng, cùng sai số trễ do biến dạng nhiệt đàn hồi trong dây.",
      "Because of the inherent limitations of mechanical motion-balance devices, first the "
      "force-balance and later the solid state pressure transducer were introduced. The first "
      "unbonded-wire strain gages were introduced in the late 1930s. In this device, the wire "
      "filament is attached to a structure under strain, and the resistance in the strained wire "
      "is measured. This design was inherently unstable and could not maintain calibration. "
      "There also were problems with degradation of the bond between the wire filament and the "
      "diaphragm, and with hysteresis caused by thermoelastic strain in the wire.")
    P("Cuộc tìm kiếm cảm biến áp suất và biến dạng tốt hơn trước hết dẫn đến strain gage màng "
      "mỏng dán (bonded thin-film), cuối cùng là strain gage bán dẫn khuếch tán (diffused "
      "semiconductor). Những loại này ban đầu được phát triển cho ngành ô tô, nhưng ngay sau đó "
      "chuyển sang lĩnh vực chung đo và truyền áp suất trong mọi ứng dụng công nghiệp và khoa học. "
      "Cảm biến áp suất bán dẫn nhạy, rẻ, chính xác và lặp lại tốt.",
      "The search for improved pressure and strain sensors first resulted in the introduction "
      "of bonded thin-film and finally diffused semiconductor strain gages. These were first "
      "developed for the automotive industry, but shortly thereafter moved into the general "
      "field of pressure measurement and transmission in all industrial and scientific "
      "applications. Semiconductor pressure sensors are sensitive, inexpensive, accurate and "
      "repeatable.")
    P("Nhiều bộ phát áp suất khí nén vẫn đang hoạt động, đặc biệt trong ngành hóa dầu. Nhưng khi "
      "hệ thống điều khiển ngày càng tập trung và máy tính hóa, các thiết bị này đã được thay "
      "bằng bộ phát điện tương tự và gần đây là bộ phát điện số.",
      "Many pneumatic pressure transmitters are still in operation, particularly in the "
      "petrochemical industry. But as control systems continue to become more centralized and "
      "computerized, these devices have been replaced by analog electronic and, more recently, "
      "digital electronic transmitters.")
    FIG(15, F2.fig_f15())

    # ---------------------------------------------------------------- 2.12
    H("2.12 Các loại bộ chuyển đổi", "2.12 Transducer Types")
    P("Hình 15 cung cấp định hướng tổng quát cho nhà khoa học hoặc kỹ sư đối mặt với nhiệm vụ "
      "chọn một thiết bị phát hiện áp suất trong số nhiều thiết kế có sẵn. Bảng này cho thấy dải "
      "áp suất và chân không mà các loại cảm biến khác nhau có thể phát hiện, cùng loại tham "
      "chiếu bên trong (chân không hoặc áp suất khí quyển) nếu có.",
      "Figure 15 provides an overall orientation to the scientist or engineer who might be faced "
      "with the task of selecting a pressure detector from among the many designs available. "
      "This table shows the ranges of pressures and vacuums that various sensor types are capable "
      "of detecting and the types of internal references (vacuum or atmospheric pressure) used, "
      "if any.")
    P("Vì bộ chuyển đổi áp suất điện tử hữu ích nhất cho thu thập và điều khiển dữ liệu công nghiệp "
      "và phòng thí nghiệm, nguyên lý hoạt động cùng ưu và nhược điểm của từng loại được trình "
      "bày kỹ hơn trong mục này.",
      "Because electronic pressure transducers are of greatest utility for industrial and "
      "laboratory data acquisition and control applications, the operating principles and pros "
      "and cons of each of these is further elaborated in this section.")
    FIG(16, F2.fig_f16())

    H("Strain gage", "Strain Gage", h3)
    P("Khi strain gage được dùng để đo độ lệch của màng đàn hồi hoặc ống Bourdon, nó trở thành "
      "một thành phần trong bộ chuyển đổi áp suất. Bộ chuyển đổi áp suất loại strain gage được dùng "
      "rộng rãi.",
      "When a strain gage is used to measure the deflection of an elastic diaphragm or Bourdon "
      "tube, it becomes a component in a pressure transducer. Strain gage-type pressure "
      "transducers are widely used.")
    P("Bộ chuyển đổi strain gage được dùng cho áp suất dải hẹp và cho phép đo chênh áp. Về cơ bản, "
      "strain gage được dùng để đo dịch chuyển của màng đàn hồi do chênh áp qua màng. Các thiết "
      "bị này phát hiện áp suất gauge nếu cổng áp suất thấp để hở ra khí quyển, hoặc chênh áp nếu "
      "nối với hai áp suất quá trình. Nếu phía áp suất thấp là chân không được bịt kín làm tham "
      "chiếu, bộ phát hoạt động như bộ phát áp suất tuyệt đối.",
      "Strain-gage transducers are used for narrow-span pressure and for differential pressure "
      "measurements. Essentially, the strain gage is used to measure the displacement of an "
      "elastic diaphragm due to a difference in pressure across the diaphragm. These devices can "
      "detect gauge pressure if the low pressure port is left open to the atmosphere or "
      "differential pressure if connected to two process pressures. If the low pressure side is "
      "a sealed vacuum reference, the transmitter will act as an absolute pressure transmitter.")
    P("Bộ chuyển đổi strain gage có sẵn cho dải áp suất thấp tới 3 inch nước đến cao tới 200.000 "
      "psig (1400 MPa). Độ sai nằm trong khoảng 0,1% dải đo đến 0,25% toàn thang. Các nguồn sai "
      "bổ sung có thể là trôi 0,25% toàn thang trong sáu tháng và ảnh hưởng nhiệt độ 0,25% toàn "
      "thang cho mỗi 1000°F.",
      "Strain gage transducers are available for pressure ranges as low as 3 inches of water to "
      "as high as 200,000 psig (1400 MPa). Inaccuracy ranges from 0.1% of span to 0.25% of full "
      "scale. Additional error sources can be a 0.25% of full scale drift over six months and a "
      "0.25% full scale temperature effect per 1000o F.")

    H("Điện dung", "Capacitance", h3)
    P("Bộ chuyển đổi áp suất điện dung ban đầu được phát triển để dùng trong nghiên cứu chân "
      "không thấp. Sự thay đổi điện dung này do chuyển động của phần tử màng gây ra (Hình 17). "
      "Màng thường bằng kim loại hoặc thạch anh mạ kim loại, một mặt tiếp xúc áp suất quá trình, "
      "mặt kia tiếp xúc áp suất chuẩn. Tùy loại áp suất, bộ chuyển đổi điện dung có thể là loại "
      "tuyệt đối, gauge hoặc chênh áp.",
      "Capacitance pressure transducers were originally developed for use in low vacuum "
      "research. This capacitance change results from the movement of a diaphragm element "
      "(Figure 17). The diaphragm is usually metal or metal-coated quartz and is exposed to the "
      "process pressure on one side and to the reference pressure on the other. Depending on the "
      "type of pressure, the capacitive transducer can be either an absolute, gauge, or "
      "differential pressure transducer.")
    FIG(17, F2.fig_f17())
    P("Thép không gỉ là vật liệu màng phổ biến nhất, nhưng cho dịch vụ ăn mòn, các hợp kim thép "
      "giàu niken như Inconel hoặc Hastelloy cho hiệu năng tốt hơn. Tantalum cũng được dùng cho "
      "ứng dụng ăn mòn mạnh, nhiệt độ cao. Như một trường hợp đặc biệt, màng bạc có thể dùng để "
      "đo áp suất của clo, flo và các halogen khác ở trạng thái nguyên tố.",
      "Stainless steel is the most common diaphragm material used, but for corrosive service, "
      "high-nickel steel alloys, such as Inconel or Hastelloy, give better performance. Tantalum "
      "also is used for highly corrosive, high temperature applications. As a special case, "
      "silver diaphragms can be used to measure the pressure of chlorine, fluorine, and other "
      "halogens in their elemental state.")
    P("Trong cảm biến áp suất điện dung, một dao động tần số cao, điện áp cao được dùng để nạp "
      "các điện cực cảm biến. Trong thiết kế tụ hai bản, chuyển động của màng giữa hai bản được "
      "phát hiện như chỉ thị của sự thay đổi áp suất quá trình.",
      "In a capacitance-type pressure sensor, a high-frequency, high-voltage oscillator is used "
      "to charge the sensing electrode elements. In a two-plate capacitor sensor design, the "
      "movement of the diaphragm between the plates is detected as an indication of the changes "
      "in process pressure.")
    P("Như Hình 17, độ lệch của màng gây thay đổi điện dung được cầu đo phát hiện. Mạch này có thể "
      "hoạt động ở chế độ cân bằng hoặc không cân bằng. Ở chế độ cân bằng, điện áp đầu ra được đưa "
      "vào đầu dò null và các nhánh tụ được thay đổi để giữ cầu ở trạng thái null. Vì vậy, ở chế "
      "độ cân bằng, chính thiết lập null là thước đo áp suất quá trình. Khi hoạt động ở chế độ "
      "không cân bằng, phép đo áp suất quá trình liên quan tới tỉ số giữa điện áp đầu ra và điện "
      "áp kích thích.",
      "As shown in Figure 17, the deflection of the diaphragm causes a change in capacitance "
      "that is detected by a bridge circuit. This circuit can be operated in either a balanced "
      "or unbalanced mode. In balanced mode, the output voltage is fed to a null detector and the "
      "capacitor arms are varied to maintain the bridge at null. Therefore, in the balanced mode, "
      "the null setting itself is a measure of process pressure. When operated in unbalanced "
      "mode, the process pressure measurement is related to the ratio between the output voltage "
      "and the excitation voltage.")
    P("Thiết kế tụ một bản cũng phổ biến. Trong thiết kế này, bản nằm phía sau màng và điện dung "
      "thay đổi là hàm của độ lệch màng. Vì vậy, điện dung phát hiện được là chỉ thị của áp suất "
      "quá trình. Điện dung được đổi thành tín hiệu dòng một chiều hoặc điện áp có thể đọc trực "
      "tiếp bằng đồng hồ bảng hoặc thẻ I/O vi xử lý.",
      "Single-plate capacitor designs are also common. In this design, the plate is located on "
      "the back side of the diaphragm and the variable capacitance is a function of deflection of "
      "the diaphragm. Therefore, the detected capacitance is an indication of the process "
      "pressure. The capacitance is converted into either a direct current or a voltage signal "
      "that can be read directly by panel meters or microprocessor-based input/output boards.")
    P("Bộ chuyển đổi áp suất điện dung phổ biến một phần nhờ dải đo rộng, từ chân không cao ở "
      "dải micron đến 10.000 psig (70 MPa). Chênh áp thấp tới 0,01 inch nước có thể đo dễ dàng. "
      "Và so với bộ chuyển đổi strain gage, chúng trôi ít hơn. Thiết kế tốt hơn có độ chính xác "
      "trong vòng 0,1% giá trị đọc hoặc 0,01% toàn thang. Ảnh hưởng nhiệt độ điển hình là 0,25% "
      "toàn thang cho mỗi 1000°F.",
      "Capacitance pressure transducers are widespread in part because of their wide rangeability, "
      "from high vacuums in the micron range to 10,000 psig (70 MPa). Differential pressures as "
      "low as 0.01 inches of water can readily be measured. And, compared with strain gage "
      "transducers, they do not drift much. Better designs are available that are accurate to "
      "within 0.1% of reading or 0.01% of full scale. A typical temperature effect is 0.25% of "
      "full scale per 1000¡ F.")
    P("Cảm biến điện dung thường được dùng làm chuẩn phụ, đặc biệt trong ứng dụng chênh áp thấp "
      "và áp suất tuyệt đối thấp. Chúng cũng đáp ứng rất nhanh vì quãng đường màng phải dịch "
      "chỉ vài micron. Cảm biến điện dung mới hơn chống ăn mòn tốt hơn và ít nhạy với điện dung "
      "lạc và rung động, vốn từng gây “rung số đọc” ở thiết kế cũ.",
      "Capacitance-type sensors are often used as secondary standards, especially in low-"
      "differential and low-absolute pressure applications. They also are quite responsive, "
      "because the distance the diaphragm must physically travel is only a few microns. Newer "
      "capacitance pressure transducers are more resistant to corrosion and are less sensitive "
      "to stray capacitance and vibration effects that used to cause 'reading jitters' in older "
      "designs.")

    # ---------------------------------------------------------------- 2.13
    H("2.13 Bộ chuyển đổi đo áp suất cực cao", "2.13 Very high pressure measurements transducers")
    P("Thuật ngữ “áp suất cao” là tương đối, cũng như mọi phép đo áp suất. Ý nghĩa thực sự của "
      "nó phụ thuộc nhiều vào ngành cụ thể đang bàn. Trong chế tạo kim cương tổng hợp, áp suất "
      "phản ứng thông thường khoảng 100.000 psig (6.900 bar) trở lên, trong khi một số máy đùn "
      "sợi và nhựa hoạt động ở 10.000 psig (690 bar). Thế nhưng ở nhà máy bình thường, áp suất "
      "vượt quá 1.000 psig (69 bar) đã được coi là cao.",
      "The term 'high pressure' is relative, as, in fact, are all pressure measurements. What "
      "the term actually means depends greatly on the particular industry one is talking about. "
      "In synthetic diamond manufacturing, for example, normal reaction pressure is around "
      "100,000 psig (6,900 bars) or more, while some fiber and plastic extruders operate at "
      "10,000 psig (690 bars). Yet, in the average plant, pressures exceeding 1,000 psig (69 bars) "
      "are considered high.")
    P("Trong ứng dụng máy đùn, áp suất cao đi kèm nhiệt độ cao và vật liệu dính dễ bịt kín mọi "
      "khoang mà chúng lọt vào. Vì vậy, cảm biến áp suất máy đùn được lắp bằng phẳng với đường "
      "kính trong của ống và thường được làm mát liên tục.",
      "In extruder applications, high pressures are accompanied by high temperatures, and sticky "
      "materials are likely to plug all cavities they might enter. Therefore, extruder pressure "
      "sensors are inserted flush with the inner diameter of the pipe and are usually "
      "continuously cooled.")
    FIG(18, F2.fig_f18())
    H("Thiết kế áp suất cao", "High Pressure Designs", h3)
    P("Trong bộ lặp nút (Hình 18A), màng có thể phát hiện áp suất máy đùn tới 10.000 psig và hoạt "
      "động ở nhiệt độ tới 8000°F (4300°C) nhờ thiết kế tự làm mát. Nó hoạt động theo cân bằng "
      "lực trực tiếp giữa áp suất quá trình P1 tác dụng lên màng cảm biến và áp suất tín hiệu khí "
      "đầu ra P2 tác dụng lên màng cân bằng. Áp suất khí đầu ra tỉ lệ nghịch với diện tích hai "
      "màng. Nếu tỉ lệ diện tích màng là 200:1, áp suất quá trình tăng 1.000 psig sẽ làm tín hiệu "
      "khí đầu ra tăng 5 psig.",
      "In the case of the button repeater (Figure 18A), the diaphragm can detect extruder "
      "pressures up to 10,000 psig and can operate at temperatures up to 8000¡F (4300¡C) because "
      "of its self-cooling design. It operates on direct force balance between the process "
      "pressure (P1) acting on the sensing diaphragm and the pressure of the output air signal "
      "(P2) acting on the balancing diaphragm. The pressure of the output air signal follows the "
      "process pressure in inverse ratio to the areas of the two diaphragms. If the diaphragm "
      "area ratio is 200:1, a 1,000-psig increase in process pressure will raise the air output "
      "signal by 5 psig.")
    P("Bộ lặp nút có thể được vặn vào một khớp nối ¼ inch trong ống xả máy đùn sao cho màng thép "
      "không gỉ 316 của nó được lắp bằng phẳng với thành trong của ống. Tự làm mát được đảm bảo "
      "nhờ dòng khí khí cụ liên tục.",
      "The button repeater can be screwed into a ¼-in. coupling in the extruder discharge pipe in "
      "such a way that its 316 stainless steel diaphragm is inserted flush with the inside of "
      "the pipe. Self-cooling is provided by the continuous flow of instrument air.")
    P("Một cảm biến áp suất cao cơ khí khác dùng phần tử Bourdon ốc vít (Hình 18B). Thiết bị này "
      "có thể gồm tới hai mươi vòng và đo áp suất vượt xa 10.000 psig. Vật liệu chuẩn của phần tử "
      "là thép không gỉ chịu lực nặng, sai số đo khoảng 1% dải đo. Cảm biến ống Bourdon ốc vít "
      "chống quá tải tốt và phù hợp dịch vụ áp suất dao động, nhưng phải được bảo vệ khỏi tắc "
      "nghẽn. Có thể dùng phần tử làm kín kiểu màng nút áp suất cao, cũng được xếp hạng cho dịch "
      "vụ 10.000 psig.",
      "Another mechanical high pressure sensor uses a helical Bourdon element (Figure 18B). This "
      "device may include as many as twenty coils and can measure pressures well in excess of "
      "10,000 psig. The standard element material is heavy-duty stainless steel, and the "
      "measurement error is around 1% of span. Helical Bourdon tube sensors provide high "
      "overrange protection and are suitable for fluctuating pressure service, but must be "
      "protected from plugging. This protection can be provided by high-pressure, button "
      "diaphragm-type chemical seal elements that also are rated for 10,000-psig service.")
    P("Một cải tiến của thiết kế Hình 18B phát hiện chuyển động đầu ống bằng quang học, không cần "
      "liên kết cơ học. Điều này mong muốn vì sai số do ma sát liên kết. Trong các thiết bị đó, "
      "có cả diode tham chiếu để bù cho sự lão hóa nguồn sáng, thay đổi nhiệt độ và bụi bẩn tích "
      "tụ trên quang học. Vì chuyển động của cảm biến thường nhỏ (0,02 in.), độ trễ và sai số lặp "
      "lại thường không đáng kể. Các thiết bị này có sẵn để đo áp suất tới 60.000 psig.",
      "An improvement on the design shown in Figure 18 B detects tip motion optically, without "
      "requiring any mechanical linkage. This is desirable because of errors introduced by "
      "linkage friction. In such units, a reference diode also is provided to compensate for the "
      "aging of the light source, for temperature variations, and for dirt build-up on the "
      "optics. Because the sensor movement is usually small (0.02 in.), both hysteresis and "
      "repeatability errors typically are negligible. Such units are available for measuring "
      "pressures up to 60,000 psig.")
    P("Bàn cân chết (deadweight tester) cũng được dùng làm chuẩn chính khi hiệu chỉnh cảm biến áp "
      "suất cao (Hình 18C). Thiết bị tạo áp suất chuẩn thử khi một trọng vật được NIST chứng nhận "
      "đặt lên diện tích piston đã biết, áp áp suất tương ứng lên chất lỏng làm đầy. NIST nhận "
      "thấy ở áp suất trên 40.000 psig, độ chính xác của phép thử khoảng 1,5 phần trong 10.000. "
      "Độ sai điển hình của bàn cân chết công nghiệp là 1 phần trong 1.000 hay 0,1%.",
      "Deadweight testers also are used as primary standards in calibrating high-pressure "
      "sensors (Figure 18 C). The tester generates a test reference pressure when an "
      "NIST-certified weight is placed on a known piston area, which imposes a corresponding "
      "pressure on the filling fluid. NIST has found that at pressures exceeding 40,000 psig, "
      "the precision of their test is about 1.5 parts in 10,000. Typical inaccuracy of an "
      "industrial deadweight tester is 1 part in 1,000 or 0.1%.")
    P("Trong lĩnh vực cảm biến điện tử đo áp suất cao, strain gage là không có đối thủ. Cảm biến "
      "strain gage phát hiện áp suất trên 100.000 psig và cho độ chính xác 0,1% dải đo hoặc 0,25% "
      "toàn thang. Bù nhiệt độ và hiệu chỉnh lại định kỳ là mong muốn vì thay đổi nhiệt độ "
      "1000°F hoặc trôi sáu tháng cũng gây sai số thêm 0,25%. Các cảm biến điện tử khác (điện dung, "
      "potentiometric, inductive, reluctive) cũng có thể đo áp suất tới 10.000 psig, nhưng không "
      "loại nào lên cao bằng strain gage.",
      "In the area of electronic sensors for high-pressure measurement, the strain gage is without "
      "equal. Strain gage sensors can detect pressures in excess of 100,000 psig and can provide "
      "measurement precision of 0.1% of span or 0.25% of full scale. Temperature compensation and "
      "periodic recalibration are desirable because a 1000oF temperature change or six months of "
      "drift can also produce an additional 0.25% error. Other electronic sensors (capacitance, "
      "potentiometric, inductive, reluctive) are also capable of detecting pressures up to "
      "10,000 psig, but none can go as high as the strain gage.")

    H("Áp suất rất cao", "Very High Pressures", h3)
    P("Tế bào mô đun khối gồm một đầu dò thép rỗng hình trụ bịt kín ở đầu trong và có thân nhô ra "
      "ở đầu ngoài (Hình 19). Khi chịu áp suất quá trình, đầu dò bị nén, đầu dò dịch sang phải do "
      "sự co khối đẳng hướng và thân dịch xa hơn ra ngoài. Chuyển động của thân sau đó được đổi "
      "thành kết đọc áp suất. Độ trễ và độ nhạy nhiệt của thiết bị tương tự cảm biến phần tử đàn "
      "hồi khác. Ưu điểm chính là đáp ứng nhanh và an toàn: về thực tế thiết bị không bị hỏng. "
      "Tế bào mô đun khối đo được áp suất tới 200.000 psig với sai số 1% đến 2% toàn dải.",
      "The bulk modulus cell consists of a hollow cylindrical steel probe closed at the inner end "
      "with a projecting stem on the outer end (Figure 19). When exposed to a process pressure, "
      "the probe is compressed, the probe tip is moved to the right by the isotropic contraction, "
      "and the stem moves further outward. This stem motion is then converted into a pressure "
      "reading. The hysteresis and temperature sensitivity of this unit is similar to that of "
      "other elastic element pressure sensors. The main advantages of this sensor are its fast "
      "response and safety: in effect, the unit is not subject to failure. The bulk modulus cell "
      "can detect pressures up to 200,000 psig with 1% to 2% full span error.")
    FIG(19, F2.fig_f19())
    P("Trong thiết kế áp suất cao khác, dây Manganin, vàng–crom, platinum hoặc chì được quấn ốc "
      "vít quanh lõi. Điện trở của các vật liệu dây này thay đổi tỉ lệ với áp suất tác dụng lên "
      "bề mặt chúng. Chúng tương đối không nhạy với thay đổi nhiệt độ. Quan hệ áp suất–điện trở "
      "của Manganin là dương, tuyến tính và đáng kể. Có thể có tế bào Manganin cho dải áp suất "
      "tới 400.000 psig với độ chính xác 0,1% đến 0,5% toàn thang. Hạn chế chính của tế bào "
      "Manganin là tính mong manh, dễ hư hỏng do xung áp hoặc hiệu ứng độ nhớt.",
      "In another high-pressure design, Manganin, gold-chromium, platinum, or lead wire sensors "
      "are wound helically on a core. The electrical resistance of these wire materials will "
      "change in proportion to the pressure experienced on their surfaces. They are reasonably "
      "insensitive to temperature variations. The pressure-resistance relationship of Manganin is "
      "positive, linear, and substantial. Manganin cells can be obtained for pressure ranges up "
      "to 400,000 psig and can provide 0.1% to 0.5% of full scale measurement precision. The main "
      "limitation of the Manganin cell is its delicate nature, making it vulnerable to damage "
      "from pressure pulsations or viscosity effects.")
    P("Một số chất rắn hóa lỏng dưới áp suất cao. Hiện tượng đổi trạng thái này cũng có thể dùng "
      "làm chỉ thị áp suất quá trình. Ví dụ, bismuth hóa lỏng ở khoảng 365.000 đến 375.000 psig "
      "và khi hóa lỏng cũng co thể tích. Các vật liệu khác như thủy ngân có đặc tính tương tự và "
      "có thể dùng để báo hiệu áp suất đã đạt tới một giá trị nhất định.",
      "Some solids liquefy under high pressures. This change-of-state phenomenon also can be used "
      "as an indication of process pressure. Bismuth, for example, liquefies at between 365,000 "
      "and 375,000 psig and, when it does, it also contracts in volume. Other materials such as "
      "mercury have similar characteristics, and can be used to signal that the pressure has "
      "reached a particular value.")

    # ---------------------------------------------------------------- 2.14
    H("2.14 Đo chân không", "2.14 Vacuum Measurement")
    P("Kỹ sư lần đầu quan tâm đến đo chân không vào những năm 1600, khi họ nhận thấy bơm không "
      "thể nâng nước cao hơn khoảng 30 ft. Công tước xứ Tuscany ở Italy đã ủy nhiệm Galileo điều "
      "tra “vấn đề” này. Galileo, cùng với những người khác, cũng nghĩ ra nhiều thí nghiệm để "
      "khảo sát tính chất của không khí. Trong các công cụ dùng cho những thí nghiệm đó có piston "
      "để đo lực và barometer nước (cao khoảng 34 ft.) để đo áp suất chân không.",
      "Engineers first became interested in vacuum measurements in the 1600s, when they noted the "
      "inability of pumps to raise water more than about 30 ft. The Duke of Tuscany in Italy "
      "commissioned Galileo to investigate the 'problem.' Galileo, among others, also devised a "
      "number of experiments to investigate the properties of air. Among the tools used for these "
      "experiments were pistons to measure force and a water barometer (about 34 ft. tall) to "
      "measure vacuum pressure.")
    FIG(20, F2.fig_f20())
    H("Hoạt động", "Operation", h3)
    P("Sau khi Galileo mất năm 1642, Evangelista Torricelli tiếp tục công việc liên quan đến chân "
      "không và phát minh barometer thủy ngân (Hình 20). Ông phát hiện khí quyển tác dụng lực "
      "14,7 pound trên inch vuông (psi) và rằng, bên trong một ống hoàn toàn rỗng, áp suất đủ "
      "nâng cột thủy ngân cao 29,9 in. (760 mm). Vì vậy chiều cao cột thủy ngân là thước đo trực "
      "tiếp áp suất khí quyển.",
      "After Galileo's death in 1642, Evangelista Torricelli carried on the work of "
      "vacuum-related investigation and invented the mercury barometer (Figure 20). He discovered "
      "that the atmosphere exerts a force of 14.7 lb. per square in. (psi) and that, inside a "
      "fully evacuated tube, the pressure was enough to raise a column of mercury to a height of "
      "29.9 in. (760 mm). The height of a mercury column is therefore a direct measure of the "
      "atmospheric pressure.")
    FIG(21, F2.fig_f21())
    P("Năm 1644, nhà toán học người Pháp Blaise Pascal yêu cầu một nhóm người leo núi mang "
      "barometer lên dãy Alps và chứng minh áp suất không khí giảm theo độ cao. Áp suất khí quyển "
      "trung bình ở mực nước biển có thể cân bằng chiều cao cột thủy ngân 760 mm, và áp suất này "
      "được định nghĩa là một Atmotphe chuẩn. Giá trị bằng 1/760 atmotphe được gọi là torr, để "
      "vinh danh Torricelli. Năm 1872, McLeod phát minh đồng hồ phát hiện chân không McLeod, đo "
      "áp suất khí bằng cách đo thể tích hai lần — một lần ở áp suất thấp chưa biết và lần khác "
      "ở áp suất chuẩn cao hơn. Thể tích mới dưới áp suất cao đó là chỉ thị của áp suất tuyệt "
      "đối ban đầu. Các phiên bản đồng hồ McLeod vẫn tiếp tục được dùng đến ngày nay làm chuẩn "
      "hiệu chỉnh đồng hồ chân không.",
      "In 1644, French mathematician Blaise Pascal asked a group of mountaineers to carry a "
      "barometer into the Alps and proved that air pressure decreases with altitude. The average "
      "barometric pressure at sea level can balance the height of a 760 mm mercury column, and "
      "this pressure is defined as a standard Atmosphere. The value for 1/760th of an atmosphere "
      "is called a torr, in honor of Torricelli. In 1872, McLeod invented the McLeod vacuum "
      "detector gauge, which measures the pressure of a gas by measuring its volume twice, once "
      "at the unknown low pressure and again at a higher reference pressure. The pressurized new "
      "volume is then an indication of the initial absolute pressure. Versions of the McLeod "
      "Gauge continue to be used today as a standard for calibrating vacuum gauges.")
    H("Ứng dụng", "Applications", h3)
    P("Đồng hồ chân không đang dùng ngày nay thuộc ba nhóm chính: cơ khí, nhiệt và ion hóa. Dải "
      "áp suất của chúng được cho trong Hình 21. Nhìn chung, với dịch vụ chân không cao (khoảng "
      "10⁻⁶ torr), dùng đồng hồ catốt lạnh hoặc đồng hồ Bayard-Alpert catốt nóng đều phù hợp. "
      "Cả hai đều không đặc biệt chính xác hay ổn định và đều cần hiệu chỉnh thường xuyên.",
      "Vacuum gauges in use today fall into three main categories: mechanical, thermal, and "
      "ionization. Their pressure ranges are given in Figure 21. In general, for high vacuum "
      "services (around 10⁻⁶ torr), either cold cathode or Bayard-Alpert hot cathode gauges are "
      "suitable. Neither is particularly accurate or stable, and both require frequent "
      "calibration.")
    P("Với chân không ở dải millitorr (cần cho ứng dụng phún xạ), có thể cân nhắc đồng hồ ion catốt "
      "nóng. Để đo chính xác hơn trong dải trung gian này, capacitance manometer là lựa chọn tốt. "
      "Với ứng dụng chân không trung gian (giữa 10⁻⁴ và 10⁻² torr), capacitance manometer là tốt "
      "nhất về hiệu năng nhưng cũng đắt nhất. Đồng hồ rẻ nhất là loại thermocouple, nhưng sai số "
      "của nó lớn nhất. Đồng hồ Pirani số có thể là giải pháp dung hòa tốt, với độ chính xác nằm "
      "giữa cảm biến điện dung và cảm biến thermocouple.",
      "For vacuums in the millitorr range (required for sputtering applications), one might "
      "consider a hot cathode ion gauge. For more accurate measurements in this intermediate "
      "range, the capacitance manometer is a good choice. For intermediate vacuum applications "
      "(between 10⁻⁴ and 10⁻² torr), capacitance manometers are the best in terms of "
      "performance, but are also the most expensive. The lowest priced gauge is the thermocouple "
      "type, but its error is the greatest. Digital Pirani gauges can represent a good compromise "
      "solution, with accuracy between that of capacitance and thermocouple sensors.")
    P("Với chân không thấp (áp suất cao hơn) giữa khí quyển và 10⁻² torr, ống Bourdon, bellows, "
      "strain gage chủ động và cảm biến điện dung đều phù hợp.",
      "For low vacuums (higher pressures) between atmospheric and 10⁻² torr, Bourdon tubes, "
      "bellows, active strain gages, and capacitance sensors are all suitable.")

    # ---------------------------------------------------------------- 2.15
    H("2.15 Tài liệu tham khảo", "2.15 References")
    b.append(refs(_REFS))

    # ---------------------------------------------------------------- about
    H("Về nguồn tài liệu", "About the source", h3)
    P("Chương 2 chiếm PDF tr. 61-96 (36 trang), tương ứng tr. 47-82 của bản in; PAGES_SRC = 36. "
      "Các mục theo mục lục là Introduction, Concept of Measurement Pressure, Ionization gauge, "
      "Radiometer-Effect Gauges, Electronic pressure sensors, Measuring flow rate, Thermal "
      "conductivity gauges, Pressure Gauges and Switches, From Mechanical to Electronic, Very High "
      "Pressure Measurements Transducers, Vacuum Measurement và References. Nguyên bản có đúng 21 "
      "hình đánh số Figure 1 - Figure 21; tất cả được vẽ lại dạng vector trong iihfig2.py với nhãn "
      "và số gọi chi tiết.",
      "Chapter 2 occupies PDF pp. 61-96 (36 pages), corresponding to printed pp. 47-82; "
      "PAGES_SRC = 36. Its sections are Introduction, Concept of Measurement Pressure, Ionization "
      "gauge, Radiometer-Effect Gauges, Electronic pressure sensors, Measuring flow rate, Thermal "
      "conductivity gauges, Pressure Gauges and Switches, From Mechanical to Electronic, Very High "
      "Pressure Measurements Transducers, Vacuum Measurement and References. The source contains "
      "exactly 21 numbered figures, Figure 1 - Figure 21; all are redrawn as vectors in "
      "iihfig2.py with their labels and callouts.")
    b.append(note(
        ("<b>Đặc điểm của nguyên bản.</b> Các dòng “Citation:” trong nguồn là ghi chú nguồn ảnh, "
        "không phải prose, nên không được dịch; nhiều hình trong số đó chỉ có dòng Citation mà "
        "không có tiêu đề. Phương trình áp suất bức xạ (Equation 1, với hệ số thích ứng α1, α2) "
        "và phương trình thủy tĩnh P = γh, cùng các phương trình đo lưu lượng và công suất "
        "Pirani, chỉ hiện dưới dạng ảnh trong nguồn; chúng được trình bày lại bằng ký hiệu dễ đọc "
        "và có thể là cách diễn đạt gần đúng. Nguồn có một số lỗi chính tả và lỗi OCR được giữ "
        "nguyên trong bản Anh (ví dụ “Guage”, “planeparallel”, “looses”, “electrons” thay cho "
        "“electron”, “nearatmospheric”, “distorsion”, “enhancment”, “Guage” trong Penning Vacuum "
        "Guage), trong khi bản Việt dùng nghĩa đúng. Một vài biểu tượng toán học trong bản in bị "
        "lỗi mã hóa (chẳng hạn ký tự độ trong “1000¡ F”) được thể hiện bằng “°F” ở cả hai bản.")
        if vi else
        "<b>Source quirks.</b> The 'Citation:' lines in the source are image credits, not prose, "
        "and are not translated; some images carry only a Citation line and no caption. The "
        "radiometer pressure equation (Equation 1, with accommodation coefficients α1, α2), the "
        "hydrostatic equation P = γh, and the flow and Pirani-power equations appear as images in "
        "the source; they are rendered here with readable symbols and may be approximate "
        "reconstructions. A number of source typos and OCR artifacts are kept in the English "
        "text (e.g. 'Guage', 'planeparallel', 'looses', 'electrons' where 'electron' is meant, "
        "'nearatmospheric', 'distorsion', 'enhancment', and 'Guage' in 'Penning Vacuum Guage'), "
        "while the Vietnamese uses the intended meaning. Some corrupted degree symbols in the "
        "print (e.g. '1000¡ F') are shown as '°F' in both versions."))
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2018 "
      "3G E-learning LLC.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2018 "
      "3G E-learning LLC.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")


