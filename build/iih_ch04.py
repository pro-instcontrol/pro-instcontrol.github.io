# -*- coding: utf-8 -*-
"""Book 8, Chapter 4 - pH Measurement (EN/VI bilingual).

Source: 3G E-learning LLC, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 143-180 (38 pages incl. title page), printed
pp. 130-166.  The chapter begins with the classical glass/reference electrode
chain, the Nernst response, electrode selection and maintenance, the pH meter,
buffers and the TI amplifier/circuit material, then — abruptly, under the same
running header — switches to viscosity measurement, turbidity measurement and
conductivity measurement.

The source figures are numbered, but Figure 21 is skipped and Figure 20's
caption is blank; the figures are therefore placed as 1..20, 22, 23 in source
order.  Prose is translated in full; the OCR quirks are kept in the English
text where legible and explained in two translator notes.  Formula bodies that
the extraction lost are reconstructed from the printed symbol definitions and
flagged in place.  The three tables whose bodies the OCR dropped were
transcribed from the rendered PDF pages.
"""

import iih_common as C
import iihfig4 as F
from iih_common import (eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 38          # PDF pp. 143-180 inclusive (printed pp. 130-166)
BYLINE = "3G E-learning LLC · Illustrated Handbook of Industrial Instrumentation &amp; Control (2018)"
TITLE_EN = "pH Measurement"
TITLE_VI = "Đo pH"


# ---------------------------------------------------------------------------
# Reference list (source printed pp. 164-166).  The text of every numbered
# entry is kept as printed, including the split 5/6 entry and the mangled
# author strings.  Bare ampersands in publisher names are XML-escaped.
# ---------------------------------------------------------------------------
_REFS = [
    "S.P.L. Sørensen, Comptes-Rendus des Travaux du Laboratoire de Carlsberg "
    "8me Volume 1re Livraison, Copenhague, 1909.",
    "R.G. Bates, Determination of pH, Wiley, New York, 1965.",
    "Hans Bjarne Christensen, Arne Salomon and Gert Kokholm, International pH "
    "Scales and Certification of pH, Anal. Chem. vol. 63, no. 18, 885A - 891A, 1991.",
    "T. A. Litovitz and C. M. Davis, Structural and shear relaxation in liquids, "
    "in W. P. Mason (ed.), Physical Acoustics: Principles and Methods, Vol. II. "
    "Part A, Properties of Gases, Liquids and Solutions, New York: Academic "
    "Press, 1965, 281-349.",
    "Y. Bottinga and P. Richet, Silicate melts: The “anomalous” pressure "
    "dependence of the viscosity,",
    "Geochim. Cosmochim. Acta, 59, 2725-2731, 1995.",
    "J. Ferguson and Z. Kemblowski, Applied Fluid Rheology, New York: Elsevier, 1991.",
    "R. W. Whorlow, Rheological Techniques, 2nd ed., New York: Ellis Horwood, 1992.",
    "K. Walters, Rheometry, London: Chapman and Hall, 1975.",
    "J. M. Dealy, Rheometers for Molten Plastics, New York: Van Nostrand Reinhold, 1982.",
    "J. R. Van Wazer, J. W. Lyons, K. Y. Kim, and R. E. Colwell, Viscosity and "
    "Flow Measurement, New York: Interscience, 1963.",
    "C. W. Macosko, Rheology: Principles, Measurements, and Applications, "
    "New York: VCH, 1994.",
    "W. A. Wakeham, A. Nagashima, and J. V. Sengers (eds.), Measurement of the "
    "Transport Properties of Fluids, Oxford, UK: Blackwell Scientific, 1991.",
    "J. A. Himenez and M. Kostic, A novel computerized viscometer/rheometer, "
    "Rev. Sci. Instrum., 65(1), 229-241, 1994.",
    "DIN 53018 (Part 1 and 2), 53019, German National Standards.",
    "Marks’ Standard Handbooks for Mechanical Engineers, New York: McGraw-Hill, 1978.",
    "ASTM D445-71 standard.",
    "W. D. Kingery, Viscosity in Property Measurements at High Temperatures, "
    "New York: John Wiley &amp; Sons, 1959.",
    "H. Faxen, Die Bewegung einer Starren Kugel Langs der Achsee eines mit Zaher "
    "Flussigkeit Gefullten Rohres: Arkiv for Matematik, Astronomi och Fysik, "
    "27(17), 1-28, 1923.",
    "F. Gui and T. F. Irvine Jr., Theoretical and experimental study of the "
    "falling cylinder viscometer, Int. J. Heat and Mass Transfer, 37(1), 41-50, 1994.",
    "N. A. Park and T. F. Irvine Jr., Falling cylinder viscometer end correction "
    "factor, Rev. Sci. Instrum., 66(7), 3982-3984, 1995.",
    "G. E. LeBlanc and R. A. Secco, High pressure stokes’ viscometry: a new "
    "in-situ technique for sphere velocity determination, Rev. Sci. Instrum., "
    "66(10), 5015-5018, 1995.",
    "R. Clift, J. R. Grace, and M. E. Weber, Bubbles, Drops, and Particles, "
    "San Diego: Academic Press, 1978.",
    "M. Coutanceau and P. Thizon, Wall effect on the bubble behavior in highly "
    "viscous liquids, J. Fluid Mech., 107, 339-373, 1981.",
    "R. Roscoe, Viscosity determination by the oscillating vessel method I: "
    "theoretical considerations, Proc. Phys. Soc., 72, 576-584, 1958.",
    "T. Iida and R. I. L. Guthrie, The Physical Properties of Liquid Metals, "
    "Oxford, UK: Clarendon Press, 1988.",
    "H. J. McSkimin, Ultrasonic methods for measuring the mechanical properties "
    "of liquids and solids, in W.P. Mason (ed.), Physical Acoustics: Principles "
    "and Methods, Vol. I Part A, Properties of Gases, Liquids and Solutions, "
    "New York: Academic Press, 1964, 271-334.",
    "P. Nasch, M. H. Manghnani, and R. A. Secco, A modified ultrasonic "
    "interferometer for sound velocity measurements in molten metals and alloys, "
    "Rev. Sci. Instrum., 65, 682-688, 1994.",
    "K. W. Katahara, C. S. Rai, M. H. Manghnani, and J. Balogh, An interferometric "
    "technique for measuring velocity and attenuation in molten rocks, "
    "J. Geophys. Res., 86, 11779-11786, 1981.",
    "Bates RG (1973) Determination of pH: theory and practice, 2nd ed. London: "
    "John Wiley &amp; Sons.",
    "Bergveld Em IrP (2003) ISFET, theory and practice. In: Proceedings of IEEE "
    "sensor conference, pp. 1–26. Toronto: IEEE.",
    "Boron WF and Boulpaep EL (2005) Medical physiology: a cellular and molecular "
    "approach. Philadelphia, PA: Elsevier/Saunders.",
    "Buck RP, Rondinini S, Covington AK, et al. (2002) Measurement of pH. "
    "Definition, standards, and procedures (IUPAC Recommendations 2002). "
    "Pure and Applied Chemistry 74(11): 2169–2200.",
    "Covington AK, Bates RG, and Durst RA (1985) Definition of pH scales, standard "
    "reference values, measurement of pH and related terminology. Pure and Applied "
    "Chemistry 57(3): 531–542.",
    "Janata J and Janata J (2009) Principles of chemical sensors. In: Modern "
    "analytical chemistry, 2nd ed. Dordrecht, Heidelberg, London, NY: Springer "
    "Science &amp; Business Media.",
    "Mendham J, Denney RC, Barnes JD, and Thomas MJK (2000a) Determination of pH. "
    "In: Vogel’s quantitative chemical analysis, 6th ed. New York: Prentice Hall.",
    "Mendham J, Denney RC, Barnes JD, and Thomas MJK (2000b) The glass electrode. "
    "In: Vogel’s quantitative chemical analysis, 6th ed. New York: Prentice Hall.",
    "Myers RJ (2010) One-hundred years of pH. Journal of Chemical Education 87: 30–32.",
    "Prichard E and Lawn R (2003) Practical laboratory skills training guides. "
    "In: Prichard E (ed.) Valid analytical measurement series, vol. 175. London: "
    "Royal Society of Chemistry.",
    "Westcott CC (1978) pH measurements. Michigan: Academic Press.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> pH · tính axit / kiềm — acidic / alkaline · "
                "nồng độ ion hydro — hydrogen ion concentration · logarit — logarithm · "
                "điện cực chỉ thị / tham chiếu — indicator / reference electrode · "
                "điện cực kết hợp — combined electrode · màng thuỷ tinh — glass membrane · "
                "thế nối tiếp chất lỏng — liquid junction potential · cầu muối — salt bridge · "
                "KCl bão hoà — saturated KCl · calomel · Ag/AgCl · điện thế — potential · "
                "phương trình Nernst — Nernst equation · độ nhạy — sensitivity · điểm không — "
                "zero point · máy đo pH — pH meter · dung dịch đệm — buffer solution · "
                "bù nhiệt độ — temperature compensation · trở kháng đầu vào — input "
                "impedance · dòng thiên vị — bias current · độ nhớt — viscosity · "
                "độ nhớt động / động học — dynamic / kinematic viscosity · ứng suất cắt — "
                "shear stress · nhớt kế — viscometer · độ đục — turbidity · "
                "độ đục nephhelometric — NTU · ống đo độ đục — turbidity tube · "
                "độ dẫn — conductivity · hằng số cell — cell constant.")
    return ("<b>Key terms.</b> pH · acidic / alkaline · hydrogen ion concentration · "
            "logarithm · indicator / reference electrode · combined electrode · glass "
            "membrane · liquid junction potential · salt bridge · saturated KCl · "
            "calomel · Ag/AgCl · potential · Nernst equation · sensitivity · zero point · "
            "pH meter · buffer solution · temperature compensation · input impedance · "
            "bias current · viscosity · dynamic / kinematic viscosity · shear stress · "
            "viscometer · turbidity · NTU · turbidity tube · conductivity · cell constant.")


def source_notes(lang):
    """Language-aware box for extraction/running-header quirks (never named `note`)."""
    if lang == "vi":
        return note(
            "<b>Ghi chú của người dịch và của quá trình trích xuất.</b> Tiêu đề chạy ở đầu "
            "trang vẫn ghi “pH Measurement” ngay cả khi nội dung đã chuyển sang độ nhớt, độ đục "
            "và độ dẫn; tiêu đề này được giữ nguyên trong bản in. Bản OCR làm mất chỉ số trên "
            "và chỉ số dưới (ví dụ 10<sup>8</sup> Ω, 10<sup>-12</sup> A, H<sub>2</sub>, "
            "Hg<sub>2</sub>Cl<sub>2</sub>), để hở dấu ngoặc kép quanh “neutral.” và tạo ra các "
            "nhãn lạc đề như “Figure 30.1”, “Figure 197.1.4-a”, “Eq. (7.1.4)”; những chỗ đó "
            "được giữ lại trong văn bản tiếng Anh. Số phương trình bị lặp trong bản in — (3) và "
            "(7) mỗi số xuất hiện hai lần — và được bảo lưu. Các dòng “Citation:” là ghi công "
            "hình ảnh, không phải tài liệu tham khảo; các URL có nội dung tiếng nước ngoài cũng "
            "chỉ là ghi công ảnh, không thuộc danh mục tài liệu. Một số mã token ('5TU', "
            "'bottonz', 'RENOVO•N', 'RENOVO•X', 'KCl•L', '(JTLJ)') và câu bị nối ở phần ống đo "
            "độ đục được tái hiện nguyên dạng. Những thân công thức bị mất khi trích xuất được "
            "dựng lại theo định nghĩa ký hiệu in kèm và được ghi rõ tại chỗ.")
    return note(
            "<b>Translator and extraction notes.</b> The running header continues to read "
            "“pH Measurement” throughout the viscosity, turbidity and conductivity sections; "
            "the heading has not been changed here. The OCR lost superscripts and subscripts "
            "(e.g. 10<sup>8</sup> Ω, 10<sup>-12</sup> A, H<sub>2</sub>, Hg<sub>2</sub>Cl<sub>2</sub>), "
            "left the quote around “neutral.” unclosed, and produced stray labels such as "
            "“Figure 30.1”, “Figure 197.1.4-a” and “Eq. (7.1.4)”; these are kept in the English "
            "text where they occur. Equation numbers are duplicated in the printed source — "
            "(3) and (7) each appear twice — and are preserved. The “Citation:” lines are "
            "image credits, not prose references; the foreign-language URL credits are like-"
            "wise not part of the reference list. A few tokens ('5TU', 'bottonz', "
            "'RENOVO•N', 'RENOVO•X', 'KCl•L', '(JTLJ)') and a run-on sentence at the turbidity "
            "tube are reproduced as printed. Formula bodies lost in extraction are "
            "reconstructed from the surrounding symbol definitions and flagged in place.")


def figure_notes(lang):
    """Short bilingual note about the absent Figure 21 and blank Figure 20 caption."""
    if lang == "vi":
        return note(
            "<b>Về các hình.</b> Bản in bỏ qua Hình 21: văn bản ở trang 159 có nhắc đến "
            "“figure 21” nhưng không có hình nào được in. Chú thích của Hình 20 cũng để trống "
            "trong bản gốc. Vì vậy các hình được đánh số 1–20, 22, 23 theo đúng thứ tự nguồn.")
    return note(
            "<b>On the figures.</b> The printed chapter skips Figure 21: the prose on p. 159 "
            "refers to “figure 21”, but no such figure is printed. Figure 20's caption is "
            "blank in the source. The figures are therefore numbered 1–20, 22 and 23 here, "
            "in source order.")


def formula_notes(lang):
    """One box covering every formula body lost in extraction."""
    if lang == "vi":
        return note(
            "<b>Thân công thức bị mất khi trích xuất.</b> Ở các phương trình in dạng hình "
            "trong nguồn, bản OCR chỉ giữ lại phần ký hiệu giải thích. Các dạng chuẩn được dựng "
            "lại từ các ký hiệu đó gồm: biểu thức pH theo nhiệt độ sau phương trình Nernst; "
            "hàm truyền (1) của điện cực pH; độ nhạy theo nhiệt độ (2); phương trình bi cầu rơi; "
            "ứng suất cắt (5); lực cản nhớt / mô-men (6); lực Stokes (7); phương trình "
            "Hagen–Poiseuille (9) và biểu thức độ nhớt động học rút gọn (7, số thứ hai). "
            "Các số hiệu trùng (3) và (7) được giữ nguyên như bản in.")
    return note(
            "<b>Formula bodies lost in extraction.</b> Where the source printed a displayed "
            "equation as an image, the OCR retained only the symbol definitions. The standard "
            "forms reconstructed from those definitions are: the temperature expression for "
            "pH after the Nernst equation; the pH-electrode transfer function (1); sensitivity "
            "versus temperature (2); the falling-sphere equation; rotating-cylinder shear "
            "stress (5); viscous drag / torque (6); Stokes resisting force (7); the "
            "Hagen–Poiseuille equation (9); and the simplified kinematic-viscosity expression "
            "(7, second occurrence). Duplicate equation numbers (3) and (7) are kept as printed.")


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
        "Chương này mở đầu bằng phép đo pH: khái niệm, chuỗi điện cực, cấu tạo và lựa chọn "
        "điện cực, bảo trì, máy đo pH, dung dịch đệm và các mạch khuếch đại cho điện cực pH. "
        "Sau đó, dưới cùng một tiêu đề chạy, nội dung đột ngột chuyển sang đo độ nhớt, đo độ đục "
        "và đo độ dẫn."
        if vi else
        "This chapter opens with pH measurement: the concept, the electrode chain, electrode "
        "construction and selection, maintenance, the pH meter, buffers and amplifier circuits "
        "for pH electrodes. It then switches, abruptly and under the same running header, to "
        "viscosity measurement, turbidity measurement and conductivity measurement."))
    b.append(source_notes(lang))

    # ---------------------------------------------------------------- 4.1
    H("4.1 Giới thiệu", "4.1 Introduction")
    P("Phép đo pH (potential of Hydrogen — tiềm năng của hydro) cho biết một dung dịch là axit "
      "hay kiềm (còn gọi là base). Nếu dung dịch chứa lượng phân tử axit và kiềm bằng nhau, pH "
      "được coi là trung tính. Nước rất mềm thường có tính axit, trong khi nước rất cứng thường "
      "có tính kiềm, dù những hoàn cảnh bất thường vẫn có thể gây ra ngoại lệ. Thang pH là thang "
      "logarit chạy từ 0,0 đến 14,0, với 7,0 là trung tính. Số đọc nhỏ hơn 7,0 cho thấy dung dịch "
      "axit, còn số đọc cao hơn cho thấy dung dịch kiềm hoặc base. Một số chất cực đoan có thể "
      "cho giá trị dưới 0 hoặc trên 14, nhưng hầu hết nằm trong thang đo.",
      "A pH (potential of Hydrogen) measurement reveals if a solution is acidic or alkaline "
      "(also base or basic). If the solution has an equal amount of acidic and alkaline "
      "molecules, the pH is considered neutral. Very soft water is commonly acidic, while very "
      "hard water is commonly alkaline, though unusual circumstances can result in exceptions. "
      "The pH scale is logarithmic and runs from 0.0 to 14.0 with 7.0 being neutral. Readings "
      "less than 7.0 indicate acidic solutions, while higher readings indicate alkaline or base "
      "solutions. Some extreme substances can score lower than 0 or greater than 14, but most "
      "fall within the scale.")
    P("Thang logarit có nghĩa là giữa hai số nguyên liên tiếp trên thang có sự khác biệt gấp "
      "mười lần. Một dung dịch axit có chỉ số 4,0 biểu thị mức tăng gấp mười lần số phân tử axit "
      "so với dung dịch 5,0. Độ chênh về axit giữa dung dịch 4,0 và dung dịch 6,0 lớn gấp 100 "
      "lần (10x10). Axit clohydric hay axit muriatic là dung dịch cực kỳ ăn mòn nằm ở đầu cực "
      "đoan của thang axit. Hoá chất này thường được dùng để hạ pH của nước có tính kiềm cao, "
      "ví dụ trong xử lý bể bơi và bể cá. Chỉ một lượng nhỏ axit clohydric là đủ, so với lượng "
      "nước được xử lý.",
      "A logarithmic scale means that there is a ten-fold difference between each successive "
      "full number on the scale. An acidic solution reading 4.0 represents a ten-fold increase "
      "in acidic molecules over a 5.0 solution. The acidic difference between a 4.0 solution "
      "and a 6.0 solution is 100 times greater (10x10). Hydrochloric acid or muriatic acid is "
      "an extremely caustic solution that sits at the extreme end of the acidic scale. This "
      "chemical is often used to lower the pH of highly alkaline water, such as in the treatment "
      "of swimming pools and aquariums. Only small amounts of hydrochloric acid are required, "
      "relative to the amount of water being treated.")
    P("Ở mức thấp của thang axit, khoảng 1,5 – 2,0, là axit dạ dày hay axit tiêu hoá giúp chúng "
      "ta tiêu hoá thức ăn. Nước cola có chỉ số 2,5, thậm chí còn axit hơn giấm ở khoảng 3,0! "
      "Có thể cũng ngạc nhiên khi biết bia hơi chua hơn một chút so với mưa axit, còn cà phê thì "
      "chỉ kém chua hơn một chút. Nước tinh khiết có pH trung tính và nước bọt của con người "
      "dao động gần trung tính, trong khi máu chúng ta hơi kiềm. Nước biển nằm trong khoảng 7,7 "
      "đến 8,3 trên thang đo, còn các sản phẩm như xà phòng rửa tay, amonia và nước tẩy có chỉ "
      "số cao ở đầu kiềm, chạy từ 9,0 – 12,5. Baking soda hay natri bicarbonat có tính kiềm cao "
      "thường được dùng để tăng tính base cho nước axit.",
      "Also low on the acidic scale at 1.5 – 2.0 is gastric acid, or stomach acids that help "
      "us digest food. Colas come in at 2.5, even more acidic than vinegar at about 3.0! It "
      "might also be surprising to learn that beer is slightly more acidic than acid rain, and "
      "coffee only slightly less acidic. Pure water has a neutral pH and human saliva hovers "
      "close to neutral, while our blood is slightly alkaline. Seawater hits the scale between "
      "7.7 and 8.3, and products like hand soap, ammonia and bleach score high on the alkaline "
      "scale running from 9.0 – 12.5. Highly alkaline baking soda or sodium bicarbonate is "
      "often used to increase the base of acidic water.")
    P("Người nuôi cá cảnh dựa rất nhiều vào các phép đo liên quan để chăm sóc cá đúng cách. "
      "Các khối nước lớn như hồ và đại dương có rất ít biến động pH, khiến cá không chịu được "
      "sự thay đổi đột ngột. Thực vật phân huỷ, thức ăn thừa cho cá và cả chất thải của cá đều có "
      "xu hướng tạo axit trong bể cá, trong khi một số loại đá và vỏ sò có thể liên tục giải "
      "phóng lượng nhỏ calci, làm tăng tính kiềm. Do xử lý nước bằng hoá chất và các yếu tố khác, "
      "nước máy ở nhiều thành phố lớn tại Mỹ có xu hướng kiềm với pH gần 8,0. Dù uống nước máy "
      "có tính kiềm không gây hại, chất lượng nước máy suy giảm qua các năm đã khiến nhiều người "
      "chọn bộ lọc gắn vòi hoặc bình lọc để loại bỏ clo, chloramine, thuốc trừ sâu và các chất "
      "khác. Những bộ lọc này không làm thay đổi pH của nước.",
      "Aquarists rely heavily on related measurements for proper fish keeping. Large bodies of "
      "water such as lakes and oceans have very little pH fluctuation , making fish intolerant "
      "of swings. Decaying plants, left over fish food and even fish waste all have a tendency "
      "to create acidity in an aquarium, while certain types of rocks and shells can "
      "continuously release trace amounts of calcium, boosting alkalinity. Due to chemical "
      "water treatment and other factors, tap water in many large cities throughout the U.S. "
      "tends to be alkaline with a pH close to 8.0. Though drinking tap water with alkalinity is "
      "not harmful, the declining quality of tap water over the years has resulted in many "
      "people opting for faucet or pitcher filters to remove chlorine, chloramines, pesticides "
      "and other substances. These filters do not alter the pH of the water.")

    # ---------------------------------------------------------------- 4.2
    H("4.2 Khái niệm đo pH", "4.2 Concept of pH Measurements")
    P("Cũng như kilomet là đơn vị đo quãng đường và giờ là đơn vị đo thời gian, đơn vị pH đo "
      "mức độ axit hoặc tính base của một dung dịch. Nói chính xác hơn, pH là phép đo nồng độ "
      "ion hydro, [H+]. Mọi dung dịch nước đều có thể đo để xác định giá trị pH. Giá trị này nằm "
      "trong khoảng 0 đến 14. Giá trị dưới 7 thể hiện tính axit, giá trị trên 7 thể hiện tính "
      "base (còn gọi là kiềm hoặc ăn mòn). Vì 7 là điểm giữa của thang đo, nó không axit cũng "
      "không base; người ta gọi nó là “neutral.",
      "Just as the kilometer is a measure of distance and the hour is a measure of time, the pH "
      "unit measures the degree of acidity or basicity of a solution. To be more exact, pH is "
      "the measurement of the hydrogen ion concentration, [H+]. Every aqueous solution can be "
      "measured to determine its pH value. This value ranges from 0 to 14 pH. Values below 7 pH "
      "exhibit acidic properties. Values above 7 pH exhibit basic (also known as caustic or "
      "alkaline) properties. Since 7 pH is the center of the measurement scale, it is neither "
      "acidic nor basic, it is called “neutral.")

    # ------------------------------------------------ 4.2.1 The electrode chain
    H("4.2.1 Chuỗi điện cực", "The electrode chain", h3)
    P("pH được đo bằng một hệ gồm hai điện cực: điện cực chỉ thị và điện cực tham chiếu. Hai "
      "điện cực này thường được ghép thành một — điện cực kết hợp. Khi cả hai được nhúng vào "
      "dung dịch, một pin galvanic nhỏ được thiết lập. Điện thế phát sinh phụ thuộc vào cả hai "
      "điện cực. Điều kiện đo lý tưởng là chỉ điện thế của điện cực chỉ thị thay đổi theo pH, "
      "còn điện thế của điện cực tham chiếu giữ không đổi.",
      "pH is measured using a setup with two electrodes: the indicator electrode and the "
      "reference electrode. These two electrodes are often combined into one - a combined "
      "electrode. When the two electrodes are immersed in a solution, a small galvanic cell is "
      "established. The potential developed is dependent on both electrodes. Ideal measuring "
      "conditions exist when only the potential of the indicator electrode changes in response "
      "to varying pH, while the potential of the reference electrode remains constant.")
    P("Điện áp đo được có thể được biểu diễn bằng phương trình Nernst như sau:",
      "The measured voltage can be expressed by the Nernst equation in the following way:")
    EQ("E = E<sub>ind</sub> − E<sub>ref</sub> = E′<sub>T</sub> − (R·T/F)·ln a<sub>H+</sub>")
    U(["E = điện áp đo được (mV) — Measured voltage (mV)",
       "E<sub>ind</sub> = điện áp của điện cực chỉ thị (mV) — Voltage of indicator electrode (mV)",
       "E<sub>ref</sub> = điện áp của điện cực tham chiếu (mV) — Voltage of reference electrode (mV)",
       "E′<sub>T</sub> = hằng số phụ thuộc nhiệt độ (mV) — Temperature dependent constant (mV)",
       "R = hằng số khí (8,3144 J/K) — Gas Constant (8.3144 J/K)",
       "T = nhiệt độ tuyệt đối (K) — Absolute Temperature (K)",
       "F = hằng số Faraday (96485 C) — Faraday’s constant (96485 C)"],
      ["E = Measured voltage (mV)",
       "E<sub>ind</sub> = Voltage of indicator electrode (mV)",
       "E<sub>ref</sub> = Voltage of reference electrode (mV)",
       "E′<sub>T</sub> = Temperature dependent constant (mV)",
       "R = Gas Constant (8.3144 J/K)",
       "T = Absolute Temperature (K)",
       "F = Faraday’s constant (96485 C)"])
    P("Khi dùng logarit cơ số mười, công thức có thể viết thành:",
      "By using the base ten logarithm, the formula can be written as:")
    EQ("E = E′<sub>T</sub> − 2.303·(R·T/F)·log a<sub>H+</sub>")
    EQ("pH = −log a<sub>H+</sub>")
    P("Bằng cách đưa định nghĩa pH = −log a<sub>H+</sub> vào, pH có thể được biểu diễn ở nhiệt "
      "độ T như sau:",
      "By introducing the pH definition as pH = -log a<sub>H+</sub>, pH can be expressed at "
      "the temperature T as follows:")
    EQ("E = S·R′·T·(pH° − pH),  R′ = 2.303·R/F = 0.1984 mV/K,  "
       "pH = pH° − E/(S·R′·T)")
    P("Trong đó R′ = hằng số 0,1984 mV/K; S là độ nhạy, hệ số hiệu chỉnh tính đến việc đáp ứng "
      "của điện cực có thể khác giá trị lý thuyết; và pH° là pH không, được định nghĩa là giá "
      "trị pH mà tại đó điện thế đo bằng không. Hình 1 minh hoạ rằng pH° thay đổi theo nhiệt độ "
      "và một độ dốc khác sẽ được quan sát.",
      "where R’ = constant = 0.1984 mV/K; S = sensitivity, a correction factor which takes into "
      "account that the electrode response may differ from the theoretical value; and pH° = "
      "zero pH which is defined as the pH value at which the measured potential is zero. Figure "
      "1 illustrates that the pH° will change with temperature and that another slope will be "
      "observed.")
    b.append(formula_notes(lang))
    FIG(1, F.fig_f01())
    P("Hình 1 cho thấy quan hệ mV/pH ở hai nhiệt độ khác nhau.",
      "Figure 1 shows the mV/pH relation at two different temperatures.")
    b.append(figure_notes(lang))

    # ------------------------------------------------ 4.2.2 Electrode construction
    H("4.2.2 Cấu tạo điện cực", "Electrode construction", h3)
    P("Cấu tạo của điện cực chỉ thị thuỷ tinh và điện cực tham chiếu có thể làm theo nhiều cách. "
      "Một điện cực thuỷ tinh điển hình và một điện cực tham chiếu calomel điển hình được cho "
      "xem ở dưới đây.",
      "The construction of glass indicator electrodes and reference electrodes can be made in "
      "various ways. A typical glass electrode and a typical calomel reference electrode are "
      "shown below.")
    FIG(2, F.fig_f02())
    P("Cả thành phần của thuỷ tinh nhạy pH trong điện cực thuỷ tinh lẫn thành phần của dung dịch "
      "bên trong điện cực đều ảnh hưởng đến điện thế sẽ phát sinh. Đáp ứng của điện cực là điện "
      "áp phát sinh giữa mặt trong và mặt ngoài của màng. Điện áp này tỷ lệ với sự khác biệt pH "
      "giữa dung dịch bên trong và mẫu. Đáp ứng do sự trao đổi ion ở cả hai bề mặt của màng trương "
      "nở giữa các ion của thuỷ tinh và các ion H+ của dung dịch — một sự trao đổi ion được kiểm "
      "soát bởi nồng độ H+ trong cả hai dung dịch. Vì cấu trúc của màng thuỷ tinh có thể không "
      "đồng nhất, một điện thế bất đối xứng có thể phát sinh ngay cả khi pH ở hai bên bằng nhau.",
      "Both the composition of the glass electrode’s pH-sensitive glass and the composition of "
      "the glass electrode’s inner solution have an influence on the potential which will "
      "develop. The response of the electrode is the voltage developed between the inside and "
      "outside of the membrane. This voltage is proportional to the difference in pH in the "
      "inner solution and in the sample. The response is caused by an exchange at both surfaces "
      "of the swollen membrane between the ions of the glass and the H+ ions of the solution - "
      "an ion exchange which is controlled by the concentration of H+ in both solutions. As the "
      "structure of the glass membrane may not be uniform, an asymmetry potential may develop "
      "even if pH is the same on both sides.")
    P("Điện cực tham chiếu là điện cực bạc/bạc clorua bão hoà (Ag/AgCl), trong đó hai thành phần "
      "và KCl được bọc trong một ống màu đỏ. Ống màu đỏ bảo vệ khỏi tác hại của ánh sáng. Tiếp "
      "xúc với buồng được thực hiện bằng dây platin và Ag/AgCl được bao quanh bởi dung dịch KCl "
      "bão hoà. Tiếp nối chất lỏng, tức là tiếp xúc với dung dịch đo, được thực hiện qua một chốt "
      "gốm xốp. Điện thế phát sinh được xác định bởi tích độ tan của bạc clorua và nồng độ của "
      "dung dịch KCl, vì thế nó là hằng số. Có thể tạo cấu tạo điện cực tương tự bằng thuỷ ngân và "
      "thuỷ ngânơ clorua (calomel). Những điện cực như vậy không phù hợp với nhiệt độ thay đổi "
      "hoặc nhiệt độ trên 60°C.",
      "The reference electrode is a saturated silver/silver chloride electrode (Ag/AgCl) where "
      "the two components and the KCl are encapsulated in a red tube. The red tubing affords "
      "protection from the harmful effects of light. Contact with the chamber is made by means "
      "of a platinum wire and the Ag/AgCl is surrounded by a saturated solution of KCl. The "
      "liquid junction, i.e. contact to the measuring solution, is achieved through a porous "
      "ceramic pin. The potential which occurs is determined by the solubility product of the "
      "silver chloride and the concentration of the KCl solution and is therefore constant. A "
      "similar electrode construction can be made using mercury and mercurous chloride "
      "(calomel) instead. Such electrodes are not suitable for varying temperatures or "
      "temperatures above 60°C.")
    P("Điện thế của điện cực tham chiếu phải độc lập với dung dịch mẫu. Tình huống lý tưởng này "
      "xảy ra nếu mọi vận chuyển trong chốt xốp chỉ liên quan đến các ion K+ và Cl-, và nếu chúng "
      "di chuyển với cùng tốc độ. Đó là trường hợp của hầu hết mẫu trong khoảng pH 1 đến 13 và khi "
      "dùng dung dịch cầu muối KCl bão hoà hoặc 3 M. Sự lệch khỏi điều kiện tối ưu này tạo ra cái "
      "gọi là thế nối tiếp chất lỏng. Điện cực Red Rod luôn phải dùng KCl bão hoà.",
      "The potential of the reference electrode should be independent of the sample solution. "
      "This ideal situation will occur if all transport in the porous pin only involves the K+ "
      "and Cl- ions, and if they move at the same speed. This is the case in most samples in the "
      "pH range 1 to 13 and when a saturated or 3 M KCl salt-bridge solution is used. Deviation "
      "from this optimal situation creates the so-called liquid junction potential. Red Rod "
      "electrodes should always used saturated KCl.")
    P("Bảng 1 liệt kê các thế nối tiếp chất lỏng trong những mẫu khác nhau thu được khi dùng KCl "
      "bão hoà làm dung dịch cầu muối. Sự phụ thuộc của thế nối tiếp chất lỏng vào thành phần mẫu, "
      "đặc biệt là vào pH, là rõ rệt.",
      "Table 1 lists the liquid junction potentials in different samples obtained with "
      "saturated KCl as the salt-bridge solution. The liquid junction potential’s dependence "
      "on sample composition and especially on pH is obvious.")
    TBL(["Mẫu", "Thế nối tiếp chất lỏng"] if vi else
        ["Sample", "Liquid Junction Potential"],
        [["1M HCl", "14.1 mV"],
         ["0.1M HCl", "4.6 mV"],
         ["0.01M HCl", "3.0 mV"],
         ["0.1M KCl", "1.8 mV"],
         ["pH 1.68 buffer", "3.3 mV"],
         ["pH 4.01 buffer", "2.6 mV"],
         ["pH 4.65 buffer", "3.1 mV"],
         ["pH 7.00 buffer", "1.9 mV"],
         ["pH 10.01 buffer", "1.8 mV"],
         ["0.01M NaOH", "2.3 mV"],
         ["0.1M NaOH", "-0.4 mV"],
         ["1M NaOH", "-8.6 mV"]],
        "Bảng 1: Thế nối tiếp chất lỏng trong các mẫu khác nhau" if vi else
        "Table 1: Liquid junction potentials in different samples")
    P("Bảng dưới đây cho thấy độ dẫn tương đương (λ) ở độ pha loãng vô hạn của các ion thường "
      "dùng trong dung dịch cầu muối. Độ dẫn bằng nhau của cation và anion, dùng làm thước đo độ "
      "linh động của chúng, cho thế nối tiếp chất lỏng thấp nhất.",
      "The table below shows the equivalent conductivity in infinitely diluted solutions (λ) "
      "of the ions commonly used in salt-bridge solutions. Equal conductivity of the cation "
      "and anion, used as a measure of their mobility, results in the lowest liquid junction "
      "potentials.")
    TBL(["Cation", "λ", "Anion", "λ"],
        [["Li+", "38.7", "CH<sub>3</sub>COO−", "40.9"],
         ["Na+", "50.1", "ClO<sub>4</sub>−", "67.4"],
         ["K+", "73.5", "NO<sub>3</sub>−", "71.5"],
         ["NH<sub>4</sub>+", "73.6", "Cl−", "76.4"],
         ["", "", "Br−", "78.1"],
         ["", "", "½ SO<sub>4</sub>−−", "80.0"],
         ["H+", "349.8", "OH−", "198.3"]],
        "Bảng 2: Độ dẫn tương đương của các ion ở độ pha loãng vô hạn "
        "(S · cm²/equivalent) ở 25°C" if vi else
        "Table 2: Equivalent conductivity of ions in infinite "
        "dilutions (S · cm²/equivalent) at 25°C")

    # ---------------------------------------------------------------- 4.3
    H("4.3 Các loại điện cực", "4.3 Electrode types")
    FIG(3, F.fig_f03())
    P("Hình 3 cho thấy các điện cực thuỷ tinh khác nhau cho các ứng dụng khác nhau.",
      "Figure 3 shows different glass electrodes for different applications.")

    # --------------------------------------------- Glass electrodes
    H("4.3.1 Điện cực thuỷ tinh", "Glass electrodes", h3)
    P("Các loại được chỉ ra trong Hình 3 là ví dụ về điện cực thuỷ tinh. Tuy nhiên, điện cực thuỷ "
      "tinh có sẵn với nhiều hình dạng và chiều dài khác nhau để phù hợp với nhiều ứng dụng. Có "
      "những điện cực rất mỏng, loại mũi nhọn, điện cực có màng phẳng để đo bề mặt và vân vân. "
      "Hình dạng, kích thước và kiểu của điện cực bên trong có thể thay đổi, cũng như thành phần "
      "thuỷ tinh của màng.",
      "The types shown in Figure 3 are examples of glass electrodes. However, glass electrodes "
      "are available in a number of different shapes and lengths to fit a wide range of "
      "applications. There are very thin electrodes, spear types, electrodes with a flat "
      "membrane for surface measurements and so forth. The shape, size and type of the inner "
      "electrode can vary, as can the glass composition of the membrane.")
    P("Thành phần của thuỷ tinh nhạy pH sẽ quyết định phần lớn thời gian đáp ứng và độ nhạy của "
      "điện cực đối với các ion khác ngoài H+. Ion natri và lithi, và ở mức thấp hơn là ion kali, "
      "có thể gây nhiễu ở giá trị pH cao (> pH 11). Điều này thường được gọi là sai số muối hay "
      "sai số kiềm. Nếu có nhiều ion natri và ít ion hydro, chúng có thể thâm nhập vào lớp bề mặt "
      "thuỷ tinh trương nở. Điều này có nghĩa là điện cực sẽ cảm nhận nồng độ ion cao hơn và do đó "
      "máy đo pH sẽ cho giá trị pH quá thấp. Hai nhược điểm của điện cực thuỷ tinh là dung dịch đo "
      "có thể làm hỏng màng thuỷ tinh và màng thuỷ tinh rất dễ vỡ.",
      "The composition of the pH-sensitive glass will, to a large extent, determine the "
      "electrode’s response time and its sensitivity to ions other than H+. Sodium and lithium "
      "ions and, to a lesser extent, potassium ions, may interfere at high pH values (> pH 11). "
      "This is normally called the salt or alkaline error. If there is an abundance of sodium "
      "ions and few hydrogen ions, they may penetrate into the swollen glass surface layer. "
      "This means that the electrode will sense a higher ion concentration and therefore a pH "
      "value which is too low will be obtained by the pH meter. Two disadvantages of glass "
      "electrodes are that measuring solutions can damage the glass membrane and that the glass "
      "membrane is easily broken.")
    P("Có thể dùng các giải pháp thay thế cho điện cực thuỷ tinh nhưng chúng ít được dùng vì có "
      "nhược điểm khác, ví dụ thời gian đáp ứng dài. Điện cực antimon là giải pháp thay thế được "
      "dùng rộng rãi nhất. Lớp oxit mỏng hình thành trên bề mặt kim loại antimon nhạy với pH.",
      "Alternatives to the glass electrode are available but are seldom used as they have other "
      "drawbacks, e.g. a long response time. The antimony electrode is the most widely used "
      "alternative. The thin oxide layer formed on the surface of the antimony metal is "
      "sensitive to pH.")

    # --------------------------------------------- Reference electrodes
    H("4.3.2 Điện cực tham chiếu", "Reference electrodes", h3)
    P("Có nhiều loại điện cực tham chiếu khác nhau. Những khác biệt này liên quan đến: cấu tạo "
      "vật lý của tiếp nối chất lỏng; thành phần của dung dịch cầu muối; và thành phần "
      "điện hoá của điện cực. Loại tiếp nối chất lỏng phổ biến nhất được tạo bởi một chốt xốp. "
      "Tuy nhiên, tuỳ ứng dụng mà có thể dùng các loại khác: tiếp nối gốm hình vòng, tiếp nối dạng "
      "bọc (sleeve) hoặc tiếp nối hở qua một ống thuỷ tinh mỏng. Những loại này bảo đảm dòng chảy "
      "ra cao hơn của dung dịch cầu muối, có lợi khi đo trong dung dịch có cường độ ion rất cao "
      "hoặc rất thấp. Một số dung dịch đệm và mẫu, ví dụ đệm tris và bùn, cũng yêu cầu các loại "
      "tiếp nối chất lỏng này. Bốn loại tiếp nối chất lỏng được chỉ ra trong Hình 4, kèm dòng KCl "
      "điển hình cho mỗi loại.",
      "A number of different reference electrodes are available. These variations relate to: "
      "the physical construction of the liquid junction; the composition of the salt-bridge "
      "solution; the electrode’s electrochemical composition. The most common type of liquid "
      "junction is formed by a porous pin. However, depending on the application, other types "
      "can be used: circular ceramic junctions, sleeve junctions or an open junction through a "
      "thin glass tube. These will ensure a higher outflow of salt-bridge solution which is "
      "beneficial when measuring in solutions of very high or very low ionic strength. Certain "
      "buffers and samples, for example, tris buffer and slurry also require these types of "
      "liquid junctions. Four different liquid junctions are shown in Figure 4. The typical "
      "outflow of KCl salt-bridge solution for each type is also stated.")
    FIG(4, F.fig_f04())
    P("Không nên dùng KCl làm dung dịch cầu muối nếu:",
      "KCl should not be used as the salt-bridge solution if:")
    U(["nó sẽ gây nhiễu với dung dịch đo;",
       "có nguy cơ tiếp nối chất lỏng bị tắc do kết tủa;",
       "nó không trộn lẫn được với mẫu."],
      ["it will interfere with the measuring solution",
       "if there is a risk that the liquid junction will become blocked due to precipitation",
       "if it is immiscible with the sample."])
    P("Có thể dùng hai giải pháp thay thế: hệ tiếp nối kép, tức là với cầu muối thứ hai không chứa "
      "KCl, hoặc có thể dùng hệ điện cực biến tính. Hệ dùng thuỷ ngânơ sunfat và kali sunfat là một "
      "ví dụ. Bảng 3 cho cái nhìn tổng quan về một số tổ hợp.",
      "Two alternatives are available: a double junction system, i.e. with a second salt-bridge "
      "which does not contain KCl, or a modified electrode system can be used. A system with "
      "mercurous sulfate and potassium sulfate is one example. An overview of some of the "
      "combinations is provided in Table 3.")
    TBL(["Loại điện cực tham chiếu",
         "Dung dịch cầu muối",
         "Thế so với điện cực H<sub>2</sub> chuẩn",
         "Thế so với calomel bão hoà"] if vi else
        ["Type of reference electrode",
         "Salt-bridge solution(s)",
         "Potential vs. standard H<sub>2</sub> electrode",
         "Potential vs. sat. calomel electrode"],
        [["Hg/Hg<sub>2</sub>Cl<sub>2</sub>", "sat. KCl", "244 mV", "0 mV"],
         ["Ag/AgCl", "sat. KCl", "200 mV", "-44 mV"],
         ["Hg/Hg<sub>2</sub>SO<sub>4</sub>", "sat. K<sub>2</sub>SO<sub>4</sub>", "640 mV", "408 mV"],
         ["Calomel", "sat. LiCl", "~200 mV", "~-45 mV"],
         ["Hg/Hg<sub>2</sub>Cl<sub>2</sub>", "sat. KCl/KNO<sub>3</sub>", "244 mV", "~0 mV"]],
        "Bảng 3: Thế của các điện cực tham chiếu khác nhau" if vi else
        "Table 3: Potentials for different reference electrodes")

    # --------------------------------------------- Combined electrodes
    H("4.3.3 Điện cực kết hợp", "Combined electrodes", h3)
    P("Vì thao tác với một điện cực dễ hơn với hai điện cực, điện cực kết hợp (một thân) rất phổ "
      "biến. Điện cực thuỷ tinh chỉ thị và điện cực tham chiếu đơn giản được lắp vào cùng một "
      "thực thể vật lý. Điều này giúp bảo đảm hai điện cực có cùng nhiệt độ khi hoạt động.",
      "Since it is easier to handle one electrode instead of two, combined electrodes (single "
      "stem) are very popular. The indicating glass electrode and the reference electrode are "
      "simply built into a single physical entity. This helps to ensure that the two electrodes "
      "have the same temperature during operation.")
    P("Điện cực kết hợp với chuỗi điện cực đối xứng là cấu tạo tối ưu để có được sự bằng nhiệt độ "
      "giữa hai điện cực. Ở những điện cực này, điện cực bên trong của điện cực thuỷ tinh cùng loại "
      "(Ag/AgCl) và có cùng kích thước với điện cực tham chiếu, và dung dịch bên trong giống "
      "nhau nhất có thể (bão hoà KCl).",
      "Combined electrodes with symmetrical electrode chains are the optimal construction for "
      "obtaining temperature equality in the two electrodes. In these electrodes the inner "
      "electrode of the glass electrode is the same type (Ag/AgCl) and has the same dimensions "
      "as the reference electrode, and the inner solutions are as identical as possible "
      "(saturated with KCl).")

    # ---------------------------------------------------------------- 4.4
    H("4.4 Lựa chọn đúng điện cực", "4.4 Choosing the right electrode")
    P("Việc chọn đúng kích thước vật lý khá đơn giản vì kích thước mẫu và bình chứa mẫu sẽ quyết "
      "định loại nên dùng. Nếu các điện cực được dùng trong điều kiện khắc nghiệt, loại có thân "
      "nhựa và nắp bảo vệ sẽ phù hợp. Những phép đo thực hiện trực tiếp trên bề mặt yêu cầu điện "
      "cực màng phẳng, vân vân.",
      "Choosing the right physical dimensions is straightforward as the sample size and sample "
      "vessel will dictate the type you should use. If the electrodes are to be used under harsh "
      "conditions, types with a plastic stem and protection cap will be suitable. Measurements "
      "which are to be performed directly on a surface require a flat electrode and so forth.")
    FIG(5, F.fig_f05())
    P("Hình 5 minh hoạ việc chọn đúng điện cực tham chiếu cho các điều kiện đo khác nhau.",
      "Figure 5 illustrates selection of the correct reference electrode for different "
      "measuring conditions.")
    P("Các phép đo ở nhiệt độ cao hạn chế lựa chọn điện cực vì chỉ một số hệ điện hoá nhất định "
      "chịu được nhiệt độ cao. Ví dụ điện cực calomel không chịu được nhiệt độ trên 60°C. Tuy "
      "nhiên, một số điện cực tham chiếu Ag/AgCl có thể dùng thay. Phạm vi nhiệt độ sử dụng cũng "
      "có thể bị hạn chế tuỳ vào vật liệu chế tạo điện cực. Nhiệt độ thấp kéo dài thời gian đáp "
      "ứng. Thời gian đáp ứng dài thường do màng có điện trở cao, xảy ra ở màng nhỏ hoặc dày và "
      "ở thành phần thuỷ tinh chịu kiềm.",
      "Measurements at high temperatures restrict your choice of electrodes as only certain "
      "electrochemical systems can withstand higher temperatures. Calomel electrodes, for "
      "example, cannot withstand temperatures above 60°C. However, certain Ag/AgCl reference "
      "electrodes can be used instead. The temperature range used may also be restricted "
      "depending on what the electrode is made of. Low temperature prolongs the response time "
      "of the electrodes. Long response times are often caused by membranes with high electric "
      "resistance which occurs in small or thick membranes and in glass compositions which are "
      "alkali-resistant.")
    P("pH cao và nồng độ muối cao đòi hỏi điện cực có màng thuỷ tinh chịu kiềm. Trong mọi trường "
      "hợp khác, nên dùng điện cực có thành phần thuỷ tinh tiêu chuẩn. Khi đo trong nhũ tương hoặc "
      "dung dịch béo, điều quan trọng là chọn đúng loại tiếp nối chất lỏng. Cũng quan trọng là "
      "tiếp nối dễ làm mới và dễ làm sạch. Vì vậy có thể khuyên dùng tiếp nối chất lỏng hở hoặc "
      "tiếp nối dạng bọc. Trong một số trường hợp các loại này cũng dùng được cho phép đo trong "
      "dung dịch không nước. Tuy nhiên, dung dịch cầu muối chứa lithi clorua thường được ưu tiên. "
      "LiCl tan được trong nhiều môi trường hữu cơ, trong khi KCl có độ tan rất hạn chế.",
      "High pH and high salt concentrations call for electrodes with alkali-resistant glass "
      "membranes. In all other cases, an electrode with a standard glass composition should be "
      "used. When measuring in emulsions or fatty solutions, it is important to select the "
      "correct type of liquid junction. It is also important that the junction is easy to renew "
      "and clean. Open liquid junctions or sleeve junctions can therefore be recommended. These "
      "types can in some cases also be used for measurements in non-aqueous solutions. However, "
      "a salt-bridge solution containing lithium chloride is often preferable. LiCl is soluble "
      "in many organic media whereas KCl has a very limited solubility.")
    P("Nếu có nguy cơ clorua gây nhiễu hoặc nhiễm bẩn, phải dùng điện cực tham chiếu có hệ tham "
      "chiếu không chứa clorua (ví dụ Hg/Hg<sub>2</sub>SO<sub>4</sub> với cầu muối K<sub>2</sub>SO<sub>4</sub>) "
      "hoặc điện cực tham chiếu có cấu tạo cầu muối kép. Đo pH trong nước tinh khiết và các dung "
      "dịch khác có cường độ ion thấp có thể gây vấn đề. Dù phải tránh nhiễm bẩn dung dịch đo, "
      "một dòng KCl khá cao là cần thiết để giảm thiểu thế nối tiếp chất lỏng. Vì vậy nên dùng "
      "tiếp nối có vòng hình khuyên. Cũng có thể dùng tiếp nối dạng bọc dù thế nối tiếp của nó "
      "kém ổn định hơn. Dung dịch cường độ ion cao và một số dung dịch đệm cũng yêu cầu dòng chảy "
      "ra cao để bảo đảm vận chuyển ion trong tiếp nối vẫn do ion KCl chi phối. Nên dùng tiếp nối "
      "chất lỏng hở và tiếp nối dạng bọc. Đo có độ chính xác cao đôi khi được hỗ trợ bằng tiếp nối "
      "chất lỏng hở với dòng chảy ra nhỏ và được kiểm soát.",
      "If there is a risk that chloride will interfere/contaminate, a reference electrode with "
      "a chloride-free reference system must be used (e.g. Hg/ Hg 2SO4 with K 2SO4 salt-bridge), "
      "or a reference electrode with a double salt-bridge construction. Measuring pH in pure "
      "water and other solutions with low ionic strength can pose problems. Although "
      "contamination of the measuring solution must be avoided, a fairly high outflow of KCl is "
      "necessary to minimise the liquid junction potential. Junctions with annular rings are "
      "therefore recommended. Sleeve junctions can also be used although their junction "
      "potential is less stable. High ionic strength solutions and certain buffers also require "
      "a high outflow to ensure that the ionic transport in the junction is still dominated by "
      "the KCl ions. Open liquid junctions and sleeve junctions are recommended (figure 3). High "
      "precision measurements can sometimes be facilitated by using open liquid junctions with a "
      "controlled and small outflow.")

    # ---------------------------------------------------------------- 4.5
    H("4.5 Bảo trì điện cực", "4.5 Electrode maintenance")
    P("Bảo trì điện cực đúng cách bảo đảm:",
      "Proper electrode maintenance ensures:")
    U(["đáp ứng nhanh hơn;",
       "phép đo tin cậy hơn;",
       "tuổi thọ dài hơn."],
      ["a faster response",
       "more reliable measurements",
       "a longer lifetime."])
    P("Điện cực thuỷ tinh và điện cực tham chiếu có yêu cầu bảo trì khác nhau và vì thế sẽ được "
      "mô tả riêng. Thông tin về điện cực thuỷ tinh và tham chiếu cũng áp dụng cho điện cực kết "
      "hợp. Bộ dụng cụ bảo trì điện cực GK ANNEX của Radiometer Analytical chứa mọi thứ cần thiết "
      "để bảo trì điện cực thuỷ tinh cũng như điện cực kết hợp và tham chiếu với KCl bão hoà làm "
      "dung dịch cầu muối.",
      "The glass electrode and the reference electrode have different maintenance requirements "
      "and will therefore be described separately. The information concerning glass and "
      "reference electrodes also applies to combined electrodes. The GK ANNEX Electrode "
      "Maintenance Kit from Radiometer Analytical contains all the items necessary for "
      "maintaining glass electrodes plus combined and reference electrodes with saturated KCl "
      "as the salt-bridge solution.")

    # --------------------------------------------- Glass electrode (maintenance)
    H("4.5.1 Điện cực thuỷ tinh", "Glass electrode", h3)
    P("Màng thuỷ tinh luôn phải sạch. Với phép đo trong dung dịch nước, rửa bằng nước cất thường "
      "là đủ. Rửa điện cực bằng dung dịch tẩy nhẹ một lần mỗi tuần, chẳng hạn RENOVO•N của "
      "Radiometer Analytical, sẽ có lợi. Những phép đo thực hiện trong dung dịch chứa chất béo "
      "hoặc protein cần chất tẩy mạnh hơn, ví dụ dung dịch natri hypochlorit kiềm. RENOVO•X được "
      "phát triển để đáp ứng các yêu cầu này.",
      "The glass membrane must always be clean. For measurements in aqueous solutions, rinsing "
      "with distilled water will often suffice. Rinsing the electrode with a mild detergent "
      "solution once a week, such as Radiometer Analytical’s RENOVO•N, will be beneficial. "
      "Measurements performed in solutions containing fat or protein require stronger cleaning "
      "agents, e.g. alkaline hypochlorite solution. RENOVO•X has been developed to meet these "
      "requirements.")
    P("Điện cực thuỷ tinh nên được cất trong nước cất hoặc trong dung dịch đệm yếu axit giữa các "
      "lần đo. Dùng kéo dài dung dịch kiềm mạnh, hoặc thậm chí dung dịch axit flohydric yếu, sẽ "
      "giảm nghiêm trọng tuổi thọ điện cực vì màng thuỷ tinh sẽ dần bị hoà tan. Quá trình này "
      "xảy ra nhanh hơn ở nhiệt độ cao. Để cất qua đêm, điện cực kết hợp nên được cất trong dung "
      "dịch nạp lại. Nếu không dùng điện cực trong hai tuần trở lên, nên cất khô. Nhớ ngâm điện "
      "cực thật kỹ trước khi dùng. Không được để bọt khí bị kẹt quanh điện cực tham chiếu bên "
      "trong, vì có thể cho kết quả không ổn định. Gõ nhẹ điện cực hoặc lắc nó theo vòng tròn "
      "bằng dây cáp. Nếu bọt khí bị kẹt bởi tinh thể KCl, có thể cần gia nhẹ điện cực đến tối đa "
      "60°C trong bể nước.",
      "The glass electrode should be stored in distilled water or in a weak acidic buffer "
      "between measurements. Prolonged use of strong alkaline solutions or even weak solutions "
      "of hydrofluoric acid will severely reduce the lifetime of the electrode as the glass "
      "membrane will gradually be dissolved. This occurs more rapidly at high temperatures. "
      "For overnight storage, combined electrodes should be stored in refilling solution. If "
      "the electrode is not to be used for 2 weeks or more, dry storage is recommended. Remember "
      "to soak the electrode well before use No air bubbles must be trapped around the inner "
      "reference electrode as unstable readings may result. Tap the electrode gently or swing it "
      "in circles by its cable. If the air bubbles are trapped by KCl crystals, heating the "
      "electrode gently to max. 60°C in a water bath may also prove necessary.")
    P("Để tạo lớp thuỷ tinh trương nở ổn định quanh thuỷ tinh nhạy pH, điện cực thuỷ tinh mới hoặc "
      "cất khô phải được ngâm trong nước cất hoặc đệm axit vài giờ trước khi dùng. Thời gian đáp "
      "ứng bình thường đạt được sau khoảng 24 giờ, dù điện cực nhỏ có thể cần ngâm lâu hơn. Nếu "
      "cần đo trước thời gian này, nên hiệu chuẩn lại thường xuyên vì điện thế bị trôi. Nếu đáp "
      "ứng của điện cực thuỷ tinh trở nên chậm chạp, ăn mòn nhẹ lớp thuỷ tinh ngoài có thể giúp "
      "ích. Cách xử lý được khuyến nghị (chỉ thực hiện khi các biện pháp khác thất bại) gồm 1 "
      "phút trong dung dịch ammonium bifluoride 20%, sau đó 15 giây trong axit clohydric 6 M. "
      "Phải thận trọng khi thực hiện vì có nguy cơ tạo axit flohydric. Sau đó rửa sạch điện cực "
      "và ngâm 24 giờ trong nước hoặc dung dịch đệm axit.",
      "To establish a stable, swollen, glass layer around the pH-sensitive glass, new or "
      "dry-stored glass electrodes have to be soaked in distilled water or an acidic buffer for "
      "some hours before use. Normal response times will be achieved after approx. 24 hours, "
      "although a longer soaking period may be needed for small electrodes. If measurements are "
      "needed before this time, calibrations should be repeated often due to drifting potentials. "
      "If the response of a glass electrode has become sluggish, slight etching of the outer "
      "glass layer may help. The recommended treatment (which should only be performed when "
      "other measures have failed) consists of 1 minute in 20% ammonium bifluoride solution "
      "followed by 15 seconds in 6 M hydrochloric acid. Care should be exercised when carrying "
      "out this treatment as the risk of the formation of hydrofluoric acid is present. The "
      "electrode should then be thoroughly rinsed and soaked for 24 hours in water or in an "
      "acidic buffer solution.")
    P("Trong dung dịch nước, chức năng của điện cực thuỷ tinh phụ thuộc vào sự thuỷ hoá (trương "
      "nở) của lớp thuỷ tinh diễn ra trên bề mặt thuỷ tinh nhạy pH trong lúc ngâm và đo. Tuy "
      "nhiên, vẫn có thể đo trong dung dịch không nước hoặc một phần không nước miễn là điện cực "
      "được cấp nước lại thường xuyên, tức là ngâm trong nước hoặc đệm axit. Giữa các lần đo trong "
      "dung môi không nước không trộn được với nước và trước khi ngâm, điện cực trước hết nên được "
      "rửa bằng dung môi trộn được với cả nước lẫn dung môi đó, rồi cuối cùng rửa bằng nước. Vì "
      "dòng cực nhỏ đi qua điện cực thuỷ tinh, cáp, phích cắm và đầu nối phải được giữ sạch và "
      "khô nếu muốn có kết quả tin cậy.",
      "In aqueous solutions, the function of the glass electrode depends on the hydration "
      "(swelling) of the glass layer which takes place on the surface of the pH-sensitive glass "
      "during soaking and measurement. However, measurements in non-aqueous or partly "
      "non-aqueous solutions are also possible as long as the electrode is frequently "
      "rehydrated, i.e. soaked in water or an acidic buffer. Between measurements in a "
      "non-aqueous solvent which is immiscible with water and before soaking, the electrode "
      "should first be rinsed with a solvent which is miscible with both water and the solvent "
      "before finally rinsing with water. Because of the extremely small currents which pass "
      "through the glass electrode, the cable, plug and connector must be kept clean and dry if "
      "reliable measurements are to be obtained.")
    P("Tuổi thọ của điện cực thuỷ tinh phụ thuộc vào nhiều yếu tố và vì thế mang tính cá nhân cao. "
      "Bảo trì tốt kéo dài tuổi thọ, trong khi nhiệt độ cao, dung dịch kiềm, ăn mòn lặp lại và "
      "bảo trì không đúng cách làm giảm tuổi thọ điện cực. Tuy nhiên, thành phần của màng thuỷ tinh "
      "vẫn dần suy giảm ngay cả khi cất khô. Như một hướng dẫn, điện cực thuỷ tinh tiêu chuẩn dùng "
      "bình thường có thể bền một đến hai năm.",
      "The lifetime of a glass electrode depends on a number of factors and is therefore highly "
      "individual. Good maintenance will prolong the lifetime whereas high temperatures, "
      "alkaline solutions, repeated etchings and improper maintenance will reduce the "
      "electrode’s lifetime. However, the composition of the glass membrane will gradually "
      "deteriorate even during dry storage. As a guide, standard glass electrodes in normal use "
      "can last for a year or two.")

    # --------------------------------------------- Reference electrode (maintenance)
    H("4.5.2 Điện cực tham chiếu", "Reference electrode", h3)
    P("Cũng quan trọng là giữ điện cực tham chiếu sạch. Trên thực tế, hầu hết sự cố điện cực đều "
      "bắt nguồn từ điện cực tham chiếu. Có thể rửa nó bằng cùng dung dịch dùng cho điện cực thuỷ "
      "tinh. Điện cực tham chiếu luôn phải gần đầy dung dịch cầu muối. Thường dùng kali clorua nồng "
      "độ cao.",
      "It is also important that the reference electrode is kept clean. As a matter of fact, "
      "most electrode problems can be traced to the reference electrode. It can be rinsed in the "
      "same solutions as those used for the glass electrode. The reference electrode must always "
      "be nearly filled with salt-bridge solution. Potassium chloride in a high concentration "
      "is normally used.")
    FIG(6, F.fig_f06())
    P("Điện cực calomel và điện cực red rod của Radiometer Analytical yêu cầu dung dịch kali "
      "clorua bão hoà (KCl•L). Điều này có nghĩa là luôn phải có tinh thể KCl trong dung dịch cầu "
      "muối. Điện cực tham chiếu đặc biệt cho dung dịch không chứa clorua hoặc dung dịch không "
      "nước đương nhiên phải được nạp dung dịch thích hợp — thường là kali sunfat và lithi "
      "clorua. Điện cực tham chiếu có cầu muối kép chứa kali clorua ở cầu trong và một muối phù "
      "hợp ở cầu ngoài (nồng độ cao KNO<sub>3</sub>, NH<sub>4</sub>NO<sub>3</sub> và Li-Acetate là "
      "một số dung dịch hay dùng nhất).",
      "Calomel and red rod electrodes from Radiometer Analytical require saturated potassium "
      "chloride solution (KCl•L). This means that KCl crystals should always be present in the "
      "salt-bridge solution. The special reference electrodes for chloride-free solutions or for "
      "non-aqueous solutions should, of course, be filled with the appropriate solution. This "
      "will normally be potassium sulfate and lithium chloride respectively. Reference "
      "electrodes with a double salt-bridge contain potassium chloride in the inner one and a "
      "suitable salt in the outer one (high concentrations of KNO 3, NH4NO3 and Li-Acetate are "
      "some of the most often used solutions).")
    P("Nếu điện cực tham chiếu không được đậy nắp và cất khô, tốt nhất nên cất nó trong cốc đựng "
      "dung dịch cầu muối. Tuy nhiên, cần nhớ khả năng bò lan của dung dịch KCl đậm đặc. Hướng "
      "dòng chảy trong điện cực tham chiếu luôn phải từ điện cực tới dung dịch đo. Vì dòng một "
      "chiều này chỉ đạt được một phần, nên thay dung dịch cầu muối thường xuyên, ví dụ một "
      "tháng một lần. Tiếp nối chất lỏng với sợi hoặc chốt gốm đôi khi bị tắc do kết tinh (ví dụ "
      "KCl). Nếu ngâm trong dung dịch KCl không giải quyết được, nâng nhiệt độ tới mức tối đa "
      "cho phép của hệ tham chiếu thường có ích. Có thể xảy ra các dạng tắc khác, ví dụ kết tủa "
      "màu đen của bạc clorua hoặc thuỷ ngân sunfat trong chốt xốp. Dùng nhẹ giấy nhám đôi khi "
      "loại được kết tủa. Trường hợp khác có thể dùng phương pháp hoá học như ngâm điện cực vài "
      "giờ trong dung dịch axit thiourea (1 M thiourea trong 0,1 M HCl).",
      "If the reference electrode is not capped and stored dry, it should preferably be stored "
      "in a beaker containing salt-bridge solution. The ability of concentrated KCl solutions "
      "to creep should, however, be kept in mind. The direction of flow in the reference "
      "electrode should always be from the electrode to the measuring solution. As this one-way "
      "flow can only be partly achieved, the salt-bridge solution should be changed regularly, "
      "e.g. once a month. Liquid junctions with fibres or ceramic pins can occasionally become "
      "blocked due to crystallisation (e.g. of KCl). If soaking in KCl solution does not solve "
      "the problem, raising the temperature to the maximum allowable for the reference system "
      "will often help. Other types of blockage can also occur, for example, in the form of a "
      "precipitate (black) of silver chloride or mercury sulfide in the porous pin. Gentle use "
      "of abrasive paper can sometimes remove the precipitate. In other cases, chemical "
      "procedures such as soaking the electrode for a few hours in an acidic solution of "
      "thiourea (1 M thiourea in 0.1 M HCl) can be used.")
    P("Sự cố cũng có thể do bọt khí bị kẹt. Gõ nhẹ điện cực để loại bỏ. Nếu cách này không hết, "
      "nhúng thân điện cực vào dung dịch cầu muối và gia đến 60°C. Tuổi thọ của điện cực tham "
      "chiếu cũng phụ thuộc vào bảo trì, đặc biệt là vùng tiếp nối chất lỏng không bị tắc. "
      "Không được để điện cực khô và luôn phải nạp dung dịch cầu muối đúng và không nhiễm bẩn. "
      "Trong hầu hết trường hợp có thể đạt tuổi thọ hai năm trở lên. Nếu làm theo các khuyến "
      "nghị trên, quá trình hiệu chuẩn đúng nên diễn ra dễ dàng. Nếu không, nên thay hoặc kiểm tra "
      "kỹ điện cực. Có thể kiểm tra thời gian đáp ứng trong lúc hiệu chuẩn. Giá trị pH thu được "
      "trong mỗi trong hai dung dịch đệm phải ổn định trong khoảng một phút, nếu không tình trạng "
      "điện cực kém. Rất nên ghi lại pH không và độ nhạy sau mỗi lần hiệu chuẩn, vì sự lệch lớn "
      "giữa hai lần hiệu chuẩn cho thấy có vấn đề.",
      "A malfunction can also be caused by trapped air bubbles. These bubbles can be removed by "
      "gently tapping the electrode. If this does not alleviate the problem, the electrode shaft "
      "should be dipped in salt-bridge solution and heated to 60°C. The lifetime of reference "
      "electrodes also depends on maintenance and especially on the liquid junction zone not "
      "becoming blocked. The electrode must never dry out and should therefore always be filled "
      "with the proper and uncontaminated, salt-bridge solution. A lifetime of 2 years or more "
      "is, in most cases, obtainable. If the above recommendations have been followed, a proper "
      "calibration should be able to be performed easily. If this is not the case, the electrodes "
      "should be exchanged or examined more closely. The response time of the electrodes can be "
      "checked during a calibration. The pH reading obtained in each of the two buffers should "
      "be stable within approx. one minute, otherwise the electrode’s condition is poor. It is "
      "strongly recommended that the zero pH and sensitivity are noted down after each "
      "calibration since a large deviation from one calibration to the next indicates that "
      "there is a problem.")

    # ---------------------------------------------------------------- 4.6
    H("4.6 Máy đo pH", "4.6 The pH meter")
    P("Máy đo pH đo hiệu điện thế (tính bằng mV) giữa các điện cực và chuyển nó thành số đọc pH. "
      "Để có kết quả đúng, bộ khuếch đại đầu vào và mạch chuyển đổi phải đáp ứng một số yêu cầu. "
      "Cấu tạo chính của máy đo pH có thể thấy trong sơ đồ đơn giản dưới đây.",
      "A pH meter measures the potential difference (in mV) between the electrodes and converts "
      "it to a display of pH. In order to obtain a correct measurement, the input amplifier and "
      "the converting circuit must meet certain requirements. The principal construction of a "
      "pH meter can be seen in the simplified diagram below.")
    FIG(7, F.fig_f07())
    P("Hiệu điện thế giữa điện cực tham chiếu và điện cực thuỷ tinh được khuếch đại trong bộ "
      "khuếch đại mV trước khi bộ chuyển đổi A/D đưa tín hiệu tới bộ vi xử lý để tính toán kết "
      "quả. Vì điện cực thuỷ tinh thường có điện trở trong cỡ 10<sup>8</sup> Ω, điện trở đầu vào "
      "R<sub>i</sub> của bộ khuếch đại phải cao hơn đáng kể; cần giá trị 10<sup>12</sup>. Cùng lý "
      "do đó, bộ khuếch đại cũng không được cho dòng chạy qua điện cực thuỷ tinh, vì điều này tạo "
      "điện thế sai và thậm chí có thể làm nhiễu điện cực. Dòng đầu cuối hay dòng thiên vị, "
      "I<sub>term</sub>, do đó phải dưới 10<sup>-12</sup> A.",
      "The potential difference between the reference electrode and the glass electrode is "
      "amplified in the mV amplifier before the A/D converter feeds the signal to the "
      "microprocessor for result calculation. As the glass electrode typically has an inner "
      "resistance of the order of 108 Ω, the amplifier’s input resistance, Ri , must be "
      "considerably higher. A value of 1012 is required. For the same reason it is also "
      "important that the amplifier does not send any current through the glass electrode as "
      "this will give an error potential and could even disturb the electrode. The so-called "
      "terminal or bias current, Iterm, should therefore be below 10-12A.")
    P("Khi R<sub>i</sub> lớn hơn nhiều R<sub>g</sub>, I<sub>term</sub> = 10<sup>-12</sup> A và "
      "R<sub>g</sub> = 10<sup>8</sup> Ω, sai số gây ra được tính theo định luật Ohm:",
      "When Ri >> R g, Iterm = 10-12 A and Rg = 108Ω, the error introduced can be calculated "
      "according to Ohm’s Law:")
    EQ("V<sub>error</sub> = 10<sup>-12</sup> A · 10<sup>8</sup> Ω = 10<sup>-4</sup> V = 0.1 mV")
    P("Để có kết quả tin cậy và nhất quán, bộ khuếch đại và các mạch khác phải có hệ số nhiệt "
      "độ nhỏ, tức là ảnh hưởng của sự thay đổi nhiệt độ phải được kiểm soát.",
      "To attain reliable and consistent results, the amplifier and other circuits must have a "
      "small temperature coefficient, i.e. the influence of temperature variations must be "
      "under control.")
    P("Thông thường kết quả được hiển thị dạng số, dù vẫn còn một vài máy đo pH dùng kim chỉ. "
      "Thuật ngữ máy đo pH analog hoặc digital thường được dùng để phân biệt hai dạng hiển thị "
      "này. Tuy nhiên, nó cũng được dùng để phân biệt mạch chuyển đổi điều khiển dạng analog hay "
      "digital. Trong máy đo pH analog, chỉnh pH không và độ nhạy được thực hiện bằng điện trở "
      "chỉnh được (núm vặn) và hệ số khuếch đại nằm dưới sự điều khiển thủ công trực tiếp. Tín "
      "hiệu sau đó đi qua bộ chuyển đổi A/D, đầu ra là tín hiệu số để hiển thị. Ở máy đo pH "
      "digital, bộ khuếch đại làm việc trong cùng điều kiện mọi lúc và nối trực tiếp với bộ "
      "chuyển đổi A/D. Đầu ra của bộ chuyển đổi được xử lý bởi mạch số (vi xử lý), rồi pH tính "
      "toán được hiển thị. Dùng cảm biến nhiệt độ cho cả hiệu chỉnh nhiệt độ lẫn hiển thị nhiệt "
      "độ. Với hệ vi xử lý, phần mềm thường tự nhận diện dung dịch đệm hiệu chuẩn và thậm chí tự "
      "kiểm soát độ ổn định của tín hiệu điện cực.",
      "Normally, the result is displayed in numeric form although a few pH meters with pointers "
      "are still available. The term analog or digital pH meters is often used to distinguish "
      "between these two forms of display. However, it is also used to differentiate between "
      "control convert circuitry in analog or digital form. In an analog pH meter, the "
      "adjustment of zero pH and sensitivity is carried out using adjustable resistances (dials) "
      "and the amplification factor is under direct manual control. The signal is then sent "
      "through an A/D converter. The output is a digital signal for the numeric display. In a "
      "digital pH meter, the amplifier works under the same conditions all the time and is "
      "directly connected to an A/D converter. The converter’s output is then manipulated by "
      "digital circuitry (microprocessor-based) and the calculated pH is then displayed. Use of "
      "a temperature sensor provides both temperature correction and a temperature display. For "
      "microprocessor systems, the software will often provide automatic recognition of the "
      "calibration buffers and even automatic stability control of the electrode signal.")
    P("Để tránh nhiễu, nên kiểm tra các điểm sau:",
      "To avoid interference, the following points should be checked:")
    U(["Tiếp địa đúng cách cho mọi loại máy đo pH sẽ giảm nhiều vấn đề liên quan đến tín hiệu "
       "điện cực nhiễu.",
       "Nếu máy đo pH là một phần của hệ đo lớn hơn, tất cả thiết bị nên nối cùng một điểm.",
       "Nếu ổ cắm điện tường không có tiếp địa phù hợp, phải dùng dây tiếp địa riêng.",
       "Cáp điện cực không nên đi song song với dây nguồn vì có thể bắt nhiễu.",
       "Nếu dung dịch đo được nối đất (ví dụ qua ống hoặc máy khuấy), mạch máy đo pH phải được "
       "cô lập khỏi đất và việc nối với thiết bị khác (ví dụ máy ghi hoặc máy in) phải thực hiện "
       "rất cẩn thận (cần cô lập galvanic). Nếu không, có nguy cơ lớn dòng chạy qua điện cực tham "
       "chiếu, làm nhiễu phép đo và gây hư hỏng không thể sửa."],
      ["Proper grounding of all types of pH meters will alleviate a lot of problems related to "
       "noisy electrode signals.",
       "If the pH meter is part of a larger measuring system, all the instruments should be "
       "connected to the same point.",
       "If the wall power outlet does not include a proper ground, a separate grounding lead "
       "must be used.",
       "The electrode cables should not run parallel to power lines as they may pick up noise.",
       "If the measuring solution is grounded (e.g. through pipes or stirrers), the pH meter "
       "circuitry must be isolated from ground and connection to other instruments (e.g. "
       "recorders or printers) should be performed with great care (galvanic insulation is "
       "required). Otherwise there is a great risk of current being passed through the "
       "reference electrode, disturbing the measurement and causing irreparable damage."])
    FIG(8, F.fig_f08())
    P("Hình 8 cho thấy máy đo pH/ion PHM240 dùng cho phép đo pH độ chính xác cao.",
      "Figure 8 shows the PHM240 pH/Ion Meter for high-precision pH measurements.")

    # ---------------------------------------------------------------- 4.7
    H("4.7 Dung dịch đệm", "4.7 Buffers")
    P("Cần hiệu chuẩn để phối hợp máy đo pH với các điện cực. Vì mục đích này, phải dùng dung "
      "dịch có pH được biết chính xác. Dung dịch như vậy phải có độ nhạy nhất định đối với sự "
      "nhiễm bẩn nhẹ bởi các loài axit hoặc kiềm, tức là phải có khả năng đệm. Thuật ngữ dung dịch "
      "đệm hay đệm bắt nguồn từ đây.",
      "A calibration is required to match the pH meter to the electrodes. For this purpose a "
      "solution with a precisely known pH has to be used. Such a solution must have a certain "
      "insensitivity to being lightly contaminated with acid or alkaline species, i.e. it must "
      "have a buffering capacity. This is where the terms buffer solution or buffer originate "
      "from.")
    P("Hoá chất dùng trong dung dịch đệm phải tinh khiết và ổn định, giá trị pH được xác định rõ "
      "và thế nối tiếp chất lỏng phải có độ lớn giống như của mẫu chưa biết. Vì những yêu cầu này "
      "mâu thuẫn một phần, người ta đã phát triển hai loại dung dịch đệm: dung dịch đệm kỹ thuật "
      "có khả năng đệm cao và dung dịch đệm IUPAC/NIST có khả năng đệm thấp hơn. Tuy nhiên, loại "
      "sau phù hợp trực tiếp với định nghĩa pH, bảo đảm độ chính xác tốt hơn, và các dung dịch "
      "đệm khác nhau trong dãy có mức độ nhất quán cao.",
      "The chemicals used in buffer solutions must be pure and stable, the pH values should be "
      "well-defined and the liquid junction potential should be the same size as the one for the "
      "unknown sample solutions. As these requirements partly contradict each other, two kinds "
      "of buffer solutions have been developed: the so-called technical buffers with a high "
      "buffer capacity and IUPAC/NIST buffers with a lower buffer capacity. The latter ones are, "
      "however, directly in accordance with the pH definition thus ensuring better accuracy, "
      "and the different buffers in the series have a high degree of consistency.")
    FIG(9, F.fig_f09())
    P("Vấn đề thế nối tiếp chất lỏng thay đổi là rất nhỏ đối với mẫu dung dịch thông thường, pha "
      "loãng. Vì thế dung dịch đệm của Radiometer Analytical dựa trên khái niệm này. Cần nói "
      "thêm trong liên hệ này là dung dịch đệm Radiometer Analytical được xác định bằng hệ đo "
      "điện cực hydro. Dung dịch đệm Radiometer Analytical truy vết trực tiếp tới hệ đo điện cực "
      "hydro tại một trong số ít Phòng thí nghiệm Chính (bao gồm NIST và Radiometer Medical A/S).",
      "The problem of varying liquid junction potentials is minimal as regards normal, diluted "
      "sample solutions. Radiometer Analytical buffers are therefore based on this concept. It "
      "should be mentioned in this connection that the Radiometer Analytical buffers are "
      "defined using the hydrogen electrode measuring setup. Radiometer Analytical buffers are "
      "directly traceable to the hydrogen electrode measuring setup at one of the few Primary "
      "Laboratories (including NIST and Radiometer Medical A/S).")
    P("Các dung dịch đệm dùng hiện nay đã phát triển qua nhiều năm. Tuy nhiên, điều thú vị là "
      "chính S.P.L. Sorensen đã đề xuất nhiều trong số đó. R.G. Bates (từng làm việc tại Cục "
      "Tiêu chuẩn Quốc gia) đã nghiên cứu một số dung dịch đệm và chính công trình của ông là nền "
      "tảng cho dãy dung dịch đệm IUPAC/NIST hiện hành. Dãy gồm 10 dung dịch đệm được liệt kê cùng "
      "với sự phụ thuộc nhiệt độ của giá trị pH. Sự phụ thuộc nhiệt độ có thể biểu diễn bằng công "
      "thức pH = A/T + B + C·T + D·T², trong đó T là nhiệt độ theo Kelvin. Các hệ số A, B, C và D "
      "cũng được liệt kê cho từng dung dịch đệm.",
      "The buffers used today have evolved over the years. However, it is interesting to note "
      "that it was actually S.P.L. Sorensen who proposed many of them. R.G. Bates (formerly "
      "employed at the National Bureau of Standards) has made research on a number of buffers "
      "and it is his work which forms the basis of the current series of IUPAC/NIST buffers. The "
      "series consists of 10 buffers which are listed, together with the temperature dependency "
      "of the pH values. The temperature dependency of the buffers can be expressed using the "
      "formula: pH = A/T + B + C • T + D •T2 , where T is the temperature in Kelvin. The "
      "coefficients A, B, C and D are also listed for each buffer.")
    EQ("pH = A/T + B + C·T + D·T<sup>2</sup>   (T tính theo Kelvin / T in Kelvin)")
    P("Dung dịch đệm độ chính xác cao chỉ có độ ổn định hạn chế. Vì thế nên dùng chúng trong thời "
      "gian ngắn, tuỳ vào độ chính xác yêu cầu. Dung dịch trong chai đã mở (dĩ nhiên là đã đậy "
      "nắp) chỉ bền trong thời gian có hạn. Chính các dung dịch đệm kiềm gây nhiều vấn đề nhất vì "
      "chúng hấp thụ carbon dioxide từ không khí. Do đó, ngay cả dung dịch đệm trong chai nhựa mỏng "
      "chưa mở cũng có thời hạn sử dụng tương đối ngắn. Để bảo vệ tốt nhất và thời hạn dài, chai "
      "nhựa dày đặt trong hộp thiếc là giải pháp tối ưu. Cần thêm một lượng nhỏ chất diệt khuẩn để "
      "tránh sự phát triển vi sinh, vì một số dung dịch đệm là môi trường nuôi cấy tuyệt vời. Mặt "
      "khác, nên tránh thêm các chất khác vì chúng có thể làm nhiễu giá trị pH hoặc độ ổn định của "
      "dung dịch. Một số hợp chất màu có thể gây vấn đề vì chúng ảnh hưởng xấu đến tiếp nối chất "
      "lỏng.",
      "High precision buffers have only a limited stability. It is therefore recommended that "
      "they are used within a short period of time, depending though on how precise your "
      "measurements have to be. A solution in an opened (but, of course, capped) bottle will "
      "only last for a limited period of time. It is the alkaline buffers which pose most "
      "problems because they absorb carbon dioxide from the atmosphere. Therefore, even buffers "
      "in unopened, thin, plastic bottles have a relatively short shelf life. For the best "
      "protection and long shelf life, thick, plastic bottles placed in tins are the optimal "
      "solution. Addition of small amounts of germicide is necessary in order to avoid "
      "microbiological growth as several of the buffers are excellent culture media. On the "
      "other hand, addition of other substances should be avoided as they could disturb the pH "
      "value or the stability of the solution. Some colour compounds may cause problems as they "
      "have an adverse effect on the liquid junction.")

    # ---------------------------------------------------------------- 4.8
    H("4.8 Bộ khuếch đại cho điện cực pH", "4.8 Amplifiers for pH electrodes")
    P("Điện cực pH hiện đại là điện cực kết hợp gồm hai phần chính: điện cực thuỷ tinh và điện cực "
      "tham chiếu như trong Hình 10. pH về cơ bản được xác định bằng cách đo hiệu điện thế giữa "
      "hai điện cực này. Ở đầu điện cực là màng mỏng, một loại thuỷ tinh đặc biệt có khả năng trao "
      "đổi ion. Chính phần tử này cảm nhận nồng độ ion hydro của dung dịch thử. Điện thế điện cực "
      "tham chiếu không đổi và được tạo bởi phần tử bên trong của điện cực tham chiếu tiếp xúc với "
      "dung dịch nạp tham chiếu được giữ ở pH seven.",
      "The modern pH electrode is a combination electrode composed of two main parts: a glass "
      "electrode and a reference electrode as shown in Figure 10. pH is determined essentially "
      "by measuring the voltage difference between these two electrodes. At the tip of the "
      "electrode is the thin membrane that is a specific type of glass that is capable of ion "
      "exchange. It is this element that senses the hydrogen ion concentration of the test "
      "solution. The reference electrode potential is constant and is produced by the reference "
      "electrode internal element in contact with the reference-fill solution that is kept at a "
      "pH of seven.")
    FIG(10, F.fig_f10())
    P("Hình 10 cho thấy điện cực thuỷ tinh pH điển hình.",
      "Figure 10 shows a typical pH glass electrode.")

    # ---------------------------------------------------------------- 4.9
    H("4.9 Đặc tính điện cực pH", "4.9 pH Electrode Characteristics")
    P("Khi thiết kế với điện cực pH, cũng như với mọi cảm biến, điều quan trọng là hiểu đặc tính "
      "cảm biến và cách chúng ảnh hưởng đến một ứng dụng cụ thể. Những đặc tính này gồm cảm biến "
      "chủ động hay thụ động, đơn cực hay lưỡng cực, và đầu ra là điện áp hay dòng. Cũng nên xét "
      "độ nhạy, tính tuyến tính, phạm vi toàn thang và trở kháng nguồn của cảm biến.",
      "When designing with a pH electrode, as with any sensor, it is important to understand "
      "the sensor characteristics and how they affect a specific application. These "
      "characteristics include whether the sensor is active or passive, unipolar or bipolar, and "
      "whether it has a voltage or current output. Sensor sensitivity, linearity, full scale "
      "range, and source impedance should also be considered.")
    P("Điện cực pH là cảm biến thụ động, nghĩa là không cần nguồn kích thích (điện áp hoặc dòng). "
      "Vì đầu ra của điện cực có thể dao động lên trên và xuống dưới điểm tham chiếu, nó được xếp "
      "loại cảm biến lưỡng cực. Nó cho đầu ra điện áp phụ thuộc tuyến tính vào pH của dung dịch đang "
      "đo. Trở kháng nguồn của điện cực pH rất cao vì bóng thuỷ tinh mỏng có điện trở lớn, thường "
      "trong khoảng 10 MΩ đến 1000 MΩ. Điều này có nghĩa điện cực chỉ có thể được giám sát bằng "
      "thiết bị đo trở kháng cao. Hàm truyền của điện cực pH là:",
      "The pH electrode is a passive sensor, which means no excitation source (voltage or "
      "current) is required. Because the electrode’s output can swing above and below the "
      "reference point, it is classified as a bipolar sensor. It produces a voltage output that "
      "is linearly dependent upon the pH of the solution being measured. The source impedance of "
      "a pH electrode is very high because the thin glass bulb has a large resistance that is "
      "typically in the range of 10 MΩ to 1000 MΩ. This means that the electrode can only be "
      "monitored by a high-impedance measuring device. The transfer function of the pH electrode "
      "is:")
    EQ("pH(X) = pH(S) + (E<sub>S</sub> − E<sub>X</sub>)·F / [R·T·ln(10)]", "(1)")
    P("Trong đó pH(X) là pH của dung dịch chưa biết; pH(S) = 7 là pH của dung dịch chuẩn; E<sub>S</sub> "
      "là điện thế tại điện cực tham chiếu hoặc chuẩn; E<sub>X</sub> là điện thế tại điện cực đo pH; "
      "F là hằng số Faraday = 9,6485309·10<sup>4</sup> C·mol<sup>-1</sup>; R là hằng số khí "
      "phổ dụng = 8,314510 J·K<sup>-1</sup>·mol<sup>-1</sup>; và T là nhiệt độ theo Kelvin.",
      "where pH(X) = pH of unknown solution(X); pH(S) = pH of standard solution = 7; ES = "
      "Electric potential at reference or standard electrode; EX = Electric potential at "
      "pH-measuring electrode; F is the Faraday constant = 9.6485309*104 C mol -1, R is the "
      "universal gas constant = 8.314510 J K-1 mol-1, and T is the temperature in Kelvin.")
    P("Hàm truyền trong Hình 11 và Hình 12 cho thấy khi pH của dung dịch tăng, điện áp do điện cực "
      "đo pH tạo ra giảm.",
      "The transfer function in Figure 11 and Figure 12 shows that as the pH of the solution "
      "increases, the voltage produced by the pH-measuring electrode decreases.")
    FIG(11, F.fig_f11())
    FIG(12, F.fig_f12())
    P("Điều quan trọng cần lưu ý là độ nhạy của điện cực pH thay đổi theo nhiệt độ. Nhìn vào hàm "
      "truyền cho thấy độ nhạy tăng tuyến tính theo nhiệt độ theo Phương trình 2:",
      "It is important to note that a pH electrode’s sensitivity varies over temperature. "
      "Looking at the pH-electrode transfer function shows that the sensitivity linearly "
      "increases with temperature according to Equation 2:")
    EQ("RT·ln(10)/F   or   0.000198·T   V/pH", "(2)")
    P("Điều này dẫn đến phạm vi đầu ra toàn thang của cảm biến phụ thuộc vào nhiệt độ. Ví dụ ở "
      "25°C, độ nhạy điện cực là 59,16 mV/pH và đầu ra dao động từ −7pH x −59,16 mV/pH = "
      "+414,12 mV (pH 0, axit mạnh) đến +7 pH x −59,16 mV/pH = −414,12 mV (pH 14, base mạnh). "
      "Tuy nhiên, nếu nhiệt độ dung dịch tăng lên 100°C, đầu ra dao động từ −7pH x −74,04 mV/pH "
      "= +518,29 mV xuống +7pH x −74,04 mV/pH = −518,29 mV. Vì hành vi này, việc biết nhiệt độ "
      "dung dịch đang đo và bù cho phép đo là rất quan trọng.",
      "This results in a sensor output full-scale range that is dependent on the temperature. "
      "For example, at 25°C, electrode sensitivity is 59.16 mV/pH and the output of the "
      "electrode will swing from -7pH x -59.16 mV/pH = +414.12 mV (pH 0 strong acid) to +7 pH x "
      "-59.16 mV/pH = -414.12 mV (pH 14 strong base). However, if the measured solution "
      "temperature is increased to 100°C, the output will swing from -7pH x - 74.04 mV/pH = "
      "+518.29 mV down to +7pH x -74.04 mV/pH = -518.29 mV. Due to this behavior, it is critical "
      "to know the temperature of the solution being measured and compensate the measurement "
      "accordingly.")
    P("Một điện cực lý tưởng ở 25°C sẽ cho 0 mV khi đặt trong dung dịch có pH bảy. Dĩ nhiên điện "
      "cực thực tế không lý tưởng và sẽ có số đọc thực tế khác 0 mV. Sự khác biệt này gọi là sai "
      "số điểm không (offset error) của điện cực. Như đã nói, độ nhạy của điện cực lý tưởng ở 25°C "
      "là 59,16 mV trên mỗi đơn vị pH. Bất kỳ sai lệch nào so với giá trị lý tưởng này được gọi là "
      "sai số độ dải (span error). Những sai số này cần được tính đến thông qua hiệu chuẩn nếu "
      "yêu cầu độ chính xác hệ thống cao.",
      "An ideal electrode at 25°C will produce 0 mV when placed in a solution with a pH of "
      "seven. Of course, real-world electrodes are not ideal and will have an actual reading "
      "that varies from 0 mV. This variation is called the electrode’s offset error. As stated "
      "previously, the sensitivity of an ideal electrode at 25°C is 59.16 mV per pH unit. Any "
      "variation from this ideal value is specified as the electrode’s span error. These errors "
      "will need to be accounted for through calibration if high system accuracy is required.")

    # ---------------------------------------------------------------- 4.10
    H("4.10 Mạch điện cực pH tối ưu", "4.10 An Optimum pH-Electrode Circuit")
    P("Các đặc tính cảm biến quan trọng nêu trên cần được tính đến để thiết kế mạch điều hoà tín "
      "hiệu cảm biến sao cho nó được các thành phần khác (như ADC, vi điều khiển và vân vân) dọc "
      "đường tín hiệu sử dụng trung thực. Thứ nhất, vì điện cực pH tạo tín hiệu lưỡng cực và hầu "
      "hết ứng dụng dùng nguồn đơn, tín hiệu phải được dời mức. Thứ hai, do trở kháng cao của điện "
      "cực, cần một bộ đệm đầu vào trở kháng cao. Cuối cùng, phải biết nhiệt độ dung dịch đang đo "
      "để bù cho sự thay đổi độ nhạy theo nhiệt độ. Mạch trong Hình 13 giải quyết cả ba thách thức. "
      "Bộ khuếch đại U1 dời điện cực pH thêm 512 mV. Điều này đạt được bằng cách dùng nguồn tham "
      "chiếu chuẩn vi công suất low-dropout LM4140A-1.0 của TI cho điện áp chính xác 1,024 V. "
      "Điện áp này được chia đôi thành 512 mV nhờ bộ chia điện trở 10 kΩ. Đầu ra của U1 ở cấu hình "
      "unity-gain phân cực điện cực tham chiếu với cùng điện áp 512 mV ở trở kháng thấp. Điện cực "
      "đo pH tạo điện áp chồng lên điện áp phân cực 512 mV này. Hiệu ứng là mạch dời tín hiệu "
      "lưỡng cực của điện cực pH thành tín hiệu đơn cực dùng trong hệ nguồn đơn.",
      "The important sensor characteristics described need to be accounted for in order to "
      "design a circuit that will condition the sensor signal so that it can be faithfully "
      "utilized by other components (such as an ADC, microcontroller, and so forth) along the "
      "signal path. First, because the pH electrode produces a bipolar signal and most "
      "applications operate on a single supply, the signal will have to be level shifted. "
      "Second, due to the high impedance of the electrode, a high-input impedance buffer will be "
      "required. Finally, the temperature of the measured solution must be known in order to "
      "compensate for the electrode’s sensitivity variation over temperature. The circuit in "
      "Figure 13 solves all three design challenges. Amplifier U1 offsets the pH electrode by "
      "512 mV. This is achieved by using TI’s LM4140A-1.0 precision micro-power low-dropout "
      "voltage reference that produces an accurate 1.024 V. That voltage is divided in half to "
      "equal 512 mV by the 10 kΩ resistor divider. The output of amplifier U1 that is set up in a "
      "unity-gain configuration biases the reference electrode of the pH electrode with the same "
      "voltage, 512 mV, at low impedance. The pH-measuring electrode produces a voltage that "
      "rides on top of this 512 mV bias voltage. In effect, the circuit shifts the bipolar "
      "pH-electrode signal to a unipolar signal for use in a single-supply system.")
    FIG(13, F.fig_f13())
    P("Bộ khuếch đại thứ hai U2 được thiết lập ở cấu hình unity-gain và đệm đầu ra của điện cực pH. "
      "Một lần nữa, bộ đệm trở kháng đầu vào cao giữa điện cực và thiết bị đo cho phép mạch giao "
      "tiếp với nhiều loại thiết bị đo hơn, kể cả những thiết bị có trở kháng đầu vào thấp hơn. "
      "Trong hầu hết ứng dụng, điện áp đầu ra của điện cực pH đủ cao để dùng mà không cần khuếch "
      "đại thêm. Nếu cần khuếch đại, mạch này dễ dàng chỉnh sửa bằng cách thêm điện trở tăng ích "
      "cho U2. Cảm biến nhiệt độ chính xác LM35 của TI được thêm vào mạch để đo nhiệt độ dung "
      "dịch, từ đó hiệu chỉnh sự thay đổi độ nhạy do nhiệt độ, cho phép đo pH được bù nhiệt chính "
      "xác. Mạch cho hàm truyền:",
      "The second amplifier U2 is set up in a unity-gain configuration and buffers the output "
      "of the pH electrode. Again, a high-input impedance buffer between the pH electrode and "
      "the measurement instrument allows the circuit to interface with a greater variety of "
      "measurement instruments including those with lower input impedance. In most applications, "
      "the output voltage of the pH electrode is high enough to use without additional "
      "amplification. If amplification is required, this circuit can easily be modified by "
      "adding gain resistors to U2. TI’s LM35 precision centigrade temperature sensor is added "
      "to the circuit to measure the temperature of the solution so that adjustments are made "
      "for the variance in sensitivity due to temperature. This will result in an accurate "
      "temperature-corrected pH measurement. The circuit results in the transfer function:")
    EQ("V<sub>OUT</sub> = V<sub>pH</sub> + 512 mV", "(3)")
    P("Ví dụ, nếu đo nước amonia gia dụng (NH<sub>3</sub>) ở nhiệt độ phòng (25°C) có pH điển "
      "hình 11,5, điện áp do điện cực pH tạo ra là −266 mV, cho điện áp đầu ra 246 mV.",
      "For example, if room temperature (25°C) household ammonia (NH3 ) that has a typical pH "
      "of 11.5 were measured, the voltage produced by the pH electrode would be -266 mV "
      "resulting in an output voltage of 246 mV.")

    # ---------------------------------------------------------------- 4.11
    H("4.11 Lựa chọn bộ khuếch đại", "4.11 Amplifier Selection")
    P("Những thách thức thiết kế riêng của điện cực pH đòi hỏi chọn bộ khuếch đại không làm suy "
      "giảm hiệu năng tổng của hệ. Tốt nhất là bắt đầu bằng việc hiểu thông số bộ khuếch đại nào "
      "đóng góp nhiều nhất vào sai số điện áp trong ứng dụng điện cực pH. Thông số quan trọng "
      "nhất là dòng thiên vị đầu vào (input-bias current), vì dù rất nhỏ, dòng này cũng tạo sai "
      "số điện áp lớn khi đưa vào trở kháng rất cao của điện cực pH.",
      "The specific design challenges of the pH electrode impose the need to select an amplifier "
      "that does not degrade the overall system performance. It is best to start with an "
      "understanding of what amplifier parameters contribute most to the voltage error in a "
      "pH-electrode application. The most significant parameter to consider is the amplifier’s "
      "input-bias current. This is because even a small input-bias current can produce a large "
      "voltage error when injected into the very high impedance of a pH electrode.")
    P("Vì vậy op-amp LMP7721 PowerWise™ của TI — bộ khuếch đại chính xác có dòng thiên vị đầu vào "
      "được bảo đảm thấp nhất trong ngành — là lựa chọn tự nhiên. Công nghệ mới đang chờ cấp bằng "
      "sáng chế cho mạch bù dòng thiên vị đầu vào đạt dòng cực thấp chỉ 3 fA. Công nghệ này cũng "
      "duy trì thông số bảo đảm 20 fA ở nhiệt độ phòng và 900 fA ở 85°C trên toàn phạm vi điện áp "
      "chế độ chung đầu vào của bộ khuếch đại. Với dòng thiên vị rất thấp như vậy, bất kỳ dòng rò "
      "ký sinh trên PCB nào chạm tới chân đầu vào của thiết bị đều có thể ảnh hưởng xấu đáng kể "
      "đến độ chính xác hệ thống. LMP7721 giảm thiểu ảnh hưởng này nhờ bố trí chân đặc biệt cô lập "
      "đầu vào khỏi chân nguồn và chân đầu ra. Như Hình 14 cho thấy, bố trí chân độc đáo này giúp "
      "dễ bảo vệ (guard) đầu vào của LMP7721 và đạt hiệu năng hệ thống tối ưu.",
      "That makes TI’s LMP7721 PowerWise™ op amp, which is the industry’s lowest assured "
      "input-bias-current precision amplifier, a natural fit. The latest patent-pending "
      "technology of input-bias-current cancellation amplifier circuitry achieves a remarkably "
      "low input-bias-current of only 3 fA. This technology also maintains ensured specifications "
      "of 20 fA at room temperature and 900 fA at 85°C over the entire input common-mode voltage "
      "range of the amplifier. With such a low input-bias current, any PCB parasitic-leakage "
      "current that reaches the input pins of the device could have a significant adverse effect "
      "on system accuracy. The LMP7721 amplifier minimizes this effect with a special pinout that "
      "isolates the amplifier’s input from the power supply and output pins. As Figure 14 shows, "
      "this unique pinout makes it easy to guard the LMP7721 amplifier’s input and achieve "
      "optimal system performance.")
    FIG(14, F.fig_f14())
    P("Các thông số khác cần xem xét là điện áp bù đầu vào và độ trôi điện áp bù. Trong mạch điện "
      "cực pH nêu trên, mọi điện áp bù của bộ khuếch đại đều được cộng vào điện áp bù của cảm "
      "biến pH hai lần. Bộ khuếch đại dời mức (U1) cộng điện áp bù trực tiếp vào điện cực tham "
      "chiếu, có chức năng chính là giữ không đổi. Trên hết, bộ khuếch đại đệm (U2) cộng điện áp "
      "bù riêng "
      "của nó vào đầu ra của điện cực đo pH. Những điện áp bù này ảnh hưởng lớn hơn lên hệ thống "
      "nếu quyết định cần tăng ích cho bộ khuếch đại. Với điện áp bù DC thấp (tối đa 150 µV ở 25°C) "
      "và độ trôi điện áp bù thấp (1,5 µV/°C), LMP7721 cho phép nhà thiết kế đạt phép đo pH chính "
      "xác nhất. Là một phần của dòng sản phẩm PowerWise của TI, op-amp LMP7721 có tích băng thông "
      "tăng ích rộng đáng chú ý 17 MHz mà chỉ tiêu thụ 1,3 mA. Băng thông rộng này cùng hệ số "
      "khuếch đại vòng hở cao 120 dB cho phép điều hoà tín hiệu chính xác. Với những thông số đó, "
      "LMP7721 có hiệu năng vượt trội trong mạch điện cực pH.",
      "Other amplifier parameters that need to be considered are amplifier input-offset voltage "
      "and input-offset drift. In the pH-electrode circuit described above, any amplifier offset "
      "voltage is added to the pH sensor offset twofold. The level-shifting amplifier (U1) adds "
      "offset directly to the pH-reference electrode whose main function is to stay constant. On "
      "top of that, the buffer amplifier (U2) adds its individual offset voltage to the output of "
      "the pH-measuring electrode. These offsets will have a greater impact on the system if it "
      "is decided that amplifier gain is required. With low DC-offset voltage (150 µV maximum at "
      "25°C) and low offset-voltage drift (1.5 µV/°C), the LMP7721 amplifier allows a designer to "
      "achieve the most accurate pH measurements. As part of TI’s PowerWise products, the "
      "LMP7721 op amp provides the remarkably wide gain bandwidth product of 17 MHz while "
      "consuming only 1.3 mA of current. This wide gain bandwidth along with the high open loop "
      "gain of 120 dB enables accurate signal conditioning. With these specifications, the "
      "LMP7721 op amp has the performance to excel in pH-electrode circuits.")
    P("Điện cực pH là cảm biến lưỡng cực phụ thuộc nhiệt độ có trở kháng nguồn rất lớn. Những thách "
      "thức thiết kế này được xử lý bằng dời mức và bù nhiệt độ trong mạch điện cực pH nguồn đơn. "
      "Khi chọn bộ khuếch đại dùng trong mạch này, điều quan trọng là hiểu rằng dùng bộ khuếch đại "
      "có dòng thiên vị thấp là tối quan trọng. Chọn bộ khuếch đại có dòng thiên vị cực thấp như "
      "LMP7721 Power Wise của TI, khuếch đại chính xác dòng thiên vị 3 fA, là lựa chọn tốt nhất.",
      "The pH electrode is a temperature-dependent bipolar sensor that has a very large source "
      "impedance. These design challenges are handled with level shifting and temperature "
      "compensation in a single-supply pH-electrode circuit. When deciding on an amplifier to use "
      "in this circuit, it is important to understand that using an amplifier with a low bias "
      "current is of utmost importance. Selecting an amplifier with ultra-low bias current such "
      "as TI’s Power Wise LMP7721 3 fA input-bias-current precision amplifier is the best choice.")

    # ---------------------------------------------------------------- 4.12
    H("4.12 Đo độ nhớt", "4.12 Viscosity Measurement")
    P("Một tính chất cơ học quan trọng của chất lỏng là độ nhớt. Các hệ và ứng dụng vật lý đa "
      "dạng như dòng chảy trong ống, dòng máu, bôi trơn các bộ phận động cơ, động học của giọt "
      "mưa, phun núi lửa, phát sinh từ trường hành tinh và sao — chỉ kể một vài — đều liên quan "
      "đến dòng chất lỏng và được kiểm soát ở một mức nào đó bởi độ nhớt. Độ nhớt được định nghĩa "
      "là ma sát bên trong của chất lỏng. Bản chất vi mô của ma sát bên trong trong chất lỏng tương "
      "tự như khái niệm vĩ mô về ma sát cơ học trong hệ một vật thể chuyển động trên mặt phẳng "
      "đứng yên. Năng lượng phải được cung cấp (1) để khắc phục trạng thái quán tính của vật thể "
      "và mặt phẳng bị khóa do độ nhám bề mặt, và (2) để khởi động và duy trì chuyển động của vật "
      "thể trên mặt phẳng. Trong chất lỏng, năng lượng phải được cung cấp (1) để tạo các đơn vị "
      "chảy nhớt bằng cách phá vỡ liên kết giữa nguyên tử và phân tử, và (2) để làm các đơn vị đó "
      "chuyển động tương đối với nhau. Sự kháng của chất lỏng đối với việc tạo ra và chuyển động "
      "của các đơn vị chảy là do độ nhớt, chỉ biểu lộ khi có chuyển động được thiết lập trong chất "
      "lỏng. Vì độ nhớt liên quan đến vận chuyển khối lượng với một vận tốc nhất định, đáp ứng "
      "nhớt được gọi là quá trình vận chuyển động lượng.",
      "An important mechanical property of fluids is viscosity. Physical systems and "
      "applications as diverse as fluid flow in pipes, the flow of blood, lubrication of engine "
      "parts, the dynamics of raindrops, volcanic eruptions, planetary and stellar magnetic field "
      "generation, to name just a few, all involve fluid flow and are controlled to some degree "
      "by fluid viscosity. Viscosity is defined as the internal friction of a fluid. The "
      "microscopic nature of internal friction in a fluid is analogous to the macroscopic concept "
      "of mechanical friction in the system of an object moving on a stationary planar surface. "
      "Energy must be supplied (1) to overcome the inertial state of the interlocked object and "
      "plane caused by surface roughness, and (2) to initiate and sustain motion of the object "
      "over the plane. In a fluid, energy must be supplied (1) to create viscous flow units by "
      "breaking bonds between atoms and molecules, and (2) to cause the flow units to move "
      "relative to one another. The resistance of a fluid to the creation and motion of flow "
      "units is due to the viscosity of the fluid, which only manifests itself when motion in "
      "the fluid is set up. Since viscosity involves the transport of mass with a certain "
      "velocity, the viscous response is called a momentum transport process.")
    P("Vận tốc của các đơn vị chảy trong chất lỏng thay đổi tuỳ vị trí. Xét một chất lỏng giữa hai "
      "bản song song đặt gần nhau như Hình 15. Một lực F tác dụng lên bản trên kéo chất lỏng ở gần "
      "bản đó theo hướng của F. Lực tác dụng được truyền tới các lớp chất lỏng bên dưới, mỗi lớp "
      "liên kết với lớp dẫn động ở trên nhưng với cường độ giảm dần. Kết quả là vận tốc của mỗi "
      "lớp chất lỏng giảm dần, như các vector vận tốc giảm dần trong “Figure 30.1”, khi xa bản "
      "trên. Trong hệ này, lực tác dụng gọi là lực cắt (khi tác dụng trên một diện tích thì gọi là "
      "ứng suất cắt), và tốc độ biến dạng của chất lỏng, minh hoạ bởi gradient vận tốc dU<sub>x</sub>/dz, "
      "gọi là tốc độ biến dạng cắt.",
      "The velocity of flow units within the fluid will vary, depending on location. Consider a "
      "liquid between two closely spaced parallel plates as shown in Figure 15. A force, F, "
      "applied to the top plate causes the fluid adjacent to the upper plate to be dragged in the "
      "direction of F. The applied force is communicated to neighboring layers of fluid below, "
      "each coupled to the driving layer above, but with diminishing magnitude. This results in "
      "the progressive decrease in velocity of each fluid layer, as shown by the decreasing "
      "velocity vector in Figure 30.1, away from the upper plate. In this system, the applied "
      "force is called a shear (when applied over an area it is called a shear stress), and the "
      "resulting deformation rate of the fluid, as illustrated by the velocity gradient "
      "dU x/dz, is called the shear strain rate.")
    FIG(15, F.fig_f15())
    P("Biểu thức toán học mô tả đáp ứng nhớt của hệ dưới ứng suất cắt đơn giản là:",
      "The mathematical expression describing the viscous response of the system to the shear "
      "stress is simply:")
    EQ("τ<sub>zx</sub> = η·dU<sub>x</sub>/dz = η·γ̇<sub>zx</sub>", "(4)")
    P("Trong đó τ<sub>zx</sub> là ứng suất cắt, lực trên một đơn vị diện tích tác dụng lên bản "
      "trên theo hướng x (và do đó bằng lực trên một đơn vị diện tích do chất lỏng tác dụng lên "
      "bản trên theo hướng x, giả sử có lớp biên không trượt tại giao diện chất lỏng–bản trên); "
      "dU<sub>x</sub>/dz là gradient của vận tốc x theo hướng z trong chất lỏng; và η là hệ số "
      "độ nhớt. Ở đây, vì quan tâm đến lực cắt tạo chuyển động chất lỏng, η được gọi cụ thể hơn "
      "là độ nhớt động cắt. Trong cơ học chất lỏng, khuếch tán động lượng là mô tả hữu ích hơn "
      "về độ nhớt, khi chuyển động của chất lỏng được xét mà không nhắc đến lực. Loại độ nhớt "
      "này gọi là độ nhớt động học, ν, được suy ra bằng cách chia độ nhớt động cho ρ, khối lượng "
      "riêng:",
      "where τzx, the shear stress, is the force per unit area exerted on the upper plate in the "
      "x-direction (and hence is equal to the force per unit area exerted by the fluid on the "
      "upper plate in the x-direction under the assumption of a no-slip boundary layer at the "
      "fluid–upper plate interface); dU x /dz is the gradient of the x-velocity in the z-direction "
      "in the fluid; and η is the coefficient of viscosity. In this case, because one is "
      "concerned with a shear force that produces the fluid motion, η is more specifically called "
      "the shear dynamic viscosity. In fluid mechanics, diffusion of momentum is a more useful "
      "description of viscosity where the motion of a fluid is considered without reference to "
      "force. This type of viscosity is called the kinematic viscosity, ν, and is derived by "
      "dividing dynamic viscosity by ρ, the mass density:")
    EQ("ν = η / ρ")
    P("Định nghĩa độ nhớt theo Phương trình 4 chỉ đúng với dòng chảy tầng (tức là xếp lớp hoặc "
      "dạng tấm) hoặc dòng chảy streamline như Hình 15, và đề cập đến độ nhớt phân tử hay độ nhớt "
      "nội tại. Độ nhớt phân tử là tính chất của vật liệu phụ thuộc vi mô vào độ bàn liên kết và "
      "được đặc trưng vĩ mô là khả năng kháng chảy của chất lỏng. Khi dòng chảy rối, khuếch tán "
      "động lượng gồm các đóng góp nhớt từ chuyển động, đôi khi gọi là độ nhớt xoáy, bên cạnh độ "
      "nhớt nội tại. Độ nhớt của hệ rối có thể cao gấp 10<sup>6</sup> lần độ nhớt của hệ tầng, "
      "tuỳ số Reynolds.",
      "The definition of viscosity by Equation 4 is valid only for laminar (i.e., layered or "
      "sheet-like) or streamline flow as depicted in Figure 15, and it refers to the molecular "
      "viscosity or intrinsic viscosity. The molecular viscosity is a property of the material "
      "that depends microscopically on bond strengths, and is characterized macroscopically as "
      "the fluid’s resistance to flow. When the flow is turbulent, the diffusion of momentum is "
      "comprised of viscous contributions from the motion, sometimes called the eddy viscosity, "
      "in addition to the intrinsic viscosity. Viscosities of turbulent systems can be as high "
      "as 106 times greater than viscosities of laminar systems, depending on the Reynolds number.")
    P("Độ nhớt phân tử được tách thành độ nhớt cắt và độ nhớt thể tích hay khối, η<sub>v</sub>, "
      "tuỳ loại biến dạng. Độ nhớt cắt là thước đo khả năng kháng dòng đẳng thể tích trong một "
      "trường cắt, trong khi độ nhớt thể tích là thước đo khả năng kháng dòng thể tích trong một "
      "trường ứng suất ba chiều. Với hầu hết chất lỏng, kể cả chất lỏng liên kết hydro, liên kết "
      "yếu hoặc không liên kết, chất lỏng polyme và kim loại lỏng, η/η<sub>v</sub> ≈ 1, gợi ý cơ "
      "chế nhớt cắt và cấu trúc liên quan chặt chẽ với nhau.",
      "Molecular viscosity is separated into shear viscosity and bulk or volume viscosity, ηv, "
      "depending on the type of strain involved. Shear viscosity is a measure of resistance to "
      "isochoric flow in a shear field, whereas volume viscosity is a measure of resistance to "
      "volumetric flow in a three-dimensional stress field. For most liquids, including hydrogen "
      "bonded, weakly associated or unassociated, and polymeric liquids as well as liquid metals, "
      "η/ηv ≈ 1, suggesting that shear and structural viscous mechanisms are closely related")
    P("Độ nhớt cắt của hầu hết chất lỏng giảm theo nhiệt độ và tăng theo áp suất, ngược lại với "
      "đáp ứng tương ứng của chất khí. Tăng nhiệt độ thường gây giãn nở và giảm tương ứng độ bàn "
      "liên kết chất lỏng, từ đó giảm ma sát bên trong. Áp suất gây giảm thể tích và tăng tương ứng "
      "độ bàn liên kết, từ đó tăng ma sát bên trong. Trong hầu hết tình huống, kể cả ứng dụng kỹ "
      "thuật, ảnh hưởng của nhiệt độ chiếm ưu thế hơn tác động đối kháng của áp suất. Tuy nhiên, "
      "trong bối cảnh bên trong hành tinh, nơi không thể bỏ qua ảnh hưởng của áp suất, áp suất "
      "kiểm soát độ nhớt đến mức — tuỳ thành phần — có thể gây những thay đổi căn bản trong cấu "
      "trúc phân tử của chất lỏng, dẫn đến độ nhớt giảm bất thường khi áp suất tăng.",
      "The shear viscosity of most liquids decreases with temperature and increases with "
      "pressure, which is opposite to the corresponding responses for gases. An increase in "
      "temperature usually causes expansion and a corresponding reduction in liquid bond "
      "strength, which in turn reduces the internal friction. Pressure causes a decrease in "
      "volume and a corresponding increase in bond strength, which in turn enhances the internal "
      "friction. For most situations, including engineering applications, temperature effects "
      "dominate the antagonistic effects of pressure. However, in the context of planetary "
      "interiors where the effects of pressure cannot be ignored, pressure controls the viscosity "
      "to the extent that, depending on composition, it can cause fundamental changes in the "
      "molecular structure of the fluid that can result in an anomalous viscosity decrease with "
      "increasing pressure.")

    # --------------------------------------------- Rotating Cylinder Viscometer
    H("4.12.1 Nhớt kế trục quay", "Rotating Cylinder Viscometer", h3)
    P("Thiết bị gồm hai trục đồng tâm được treo đồng trục như Hình 16. Khe hở hình vành khăn hẹp "
      "giữa hai trục được lấp bằng chất lỏng cần đo độ nhớt. Trục ngoài có cơ chế quay, còn trục "
      "trong cố định và có cơ chế đo mô-men và góc quay. Khi trục ngoài quay, mô-men được truyền "
      "qua màng chất lỏng mỏng giữa hai trục tới phần tử trong đứng yên. Gọi r<sub>1</sub> và "
      "r<sub>2</sub> là bán kính trục trong và trục ngoài, h là độ sâu ngâm của trục trong trong "
      "chất lỏng và t (= r<sub>2</sub> − r<sub>1</sub>) là khe hở vành khăn. Xét N là tốc độ quay "
      "tính bằng rpm, ta có thể viết biểu thức ứng suất cắt (τ) từ định nghĩa độ nhớt (µ):",
      "It consists of two co-axial cylinders suspended coaxially as shown in the Figure 16. The "
      "narrow annular space between the cylinders is filled with a liquid for which the viscosity "
      "needs to be measured. The outer cylinder has the provision to rotate while the inner "
      "cylinder is a fixed one and has the provision to measure the torque and angular rotation. "
      "When the outer cylinder rotates, the torque is transmitted to the inner stationary member "
      "through the thin liquid film formed between the cylinders. Let r 1 and r 2 be the radii of "
      "inner and outer cylinders, h be the depth of immersion in the inner cylinder in the "
      "liquid and t(=r2-r1) is the annular gap between the cylinders. Considering N as the speed "
      "of rotation of the cylinder in rpm, one can write the expression of shear stress (τ ) from "
      "the definition of viscosity (µ ), as given below;")
    EQ("τ = µ·du/dy = µ·(2π·r<sub>2</sub>·N)/(60·t)", "(5)")
    P("Ứng suất cắt này gây lực cản nhớt trong chất lỏng, có thể tính bằng cách đo mô-men qua cơ "
      "chế bố trí ở trục trong.",
      "This shear stress induces viscous drag in the liquid that can be calculated by measuring "
      "the toque through the mechanism provided in the inner cylinder.")
    EQ("µ = 15·t·T / (π<sup>2</sup>·r<sub>1</sub><sup>2</sup>·r<sub>2</sub>·h·N) "
       "= T/(C·N)", "(6)")
    P("Ở đây C là một đại lượng không đổi đối với một nhớt kế cho trước.",
      "Here, C is a constant quantity for a given viscometer.")
    FIG(16, F.fig_f16())

    # --------------------------------------------- Falling Sphere Viscometer
    H("4.12.2 Nhớt kế bi cầu rơi", "Falling Sphere Viscometer", h3)
    P("Thiết bị gồm một thùng dài tiết diện không đổi chứa chất lỏng cần đo độ nhớt. Vì độ nhớt "
      "phụ thuộc mạnh vào nhiệt độ, thùng này được đặt trong bể nhiệt độ không đổi như Hình 17.",
      "It consists of a long container of constant area filled with a liquid whose viscosity has "
      "to be measured. Since the viscosity depends strongly with the temperature, so this "
      "container is kept in a constant temperature bath as shown in Figure 17.")
    FIG(17, F.fig_f17())
    P("Một quả cầu hình cầu hoàn toàn nhẵn được thả rơi thẳng đứng trong chất lỏng nhờ trọng lượng "
      "của chính nó (W). Quả cầu tăng tốc bên trong chất lỏng cho đến khi hợp lực hướng xuống bằng "
      "không, tức là trọng lượng chìm (F<sub>B</sub>) bằng lực cản (F<sub>R</sub>) cho bởi định "
      "luật Stokes. Sau điểm đó, quả cầu chuyển động với vận tốc ổn định gọi là vận tốc cuối. "
      "Phương trình chuyển động có thể viết như dưới đây:",
      "A perfectly smooth spherical ball is allowed to fall vertically through the liquid by "
      "virtue of its own weight (W). The ball will accelerate inside the liquid, until the net "
      "downward force is zero i.e. the submerged weight of the ball (F B) is equal to the "
      "resisting force (FR) given by Stokes’ law. After this point, the ball will move at steady "
      "velocity which is known as terminal velocity. The equation of motion may be written as "
      "below;")
    EQ("F<sub>B</sub> + F<sub>R</sub> = W = π·D<sup>3</sup>·w<sub>l</sub>/6 + "
       "F<sub>R</sub> = π·D<sup>3</sup>·w<sub>s</sub>/6", "(3)")
    P("Trong đó w<sub>l</sub> và w<sub>s</sub> lần lượt là trọng lượng riêng của chất lỏng và của "
      "quả cầu. Nếu quả cầu có đường kính D và chuyển động với vận tốc rơi không đổi V trong chất "
      "lỏng có độ nhớt µ, dùng định luật Stokes ta viết được biểu thức lực cản (F<sub>R</sub>).",
      "where, wl and ws are the specific weights of the liquid and the ball, respectively. If "
      "the spherical ball has the diameter D that moves at constant fall velocity V in a fluid "
      "having viscosity µ , then using Stokes’ law, one can write the expression for resisting "
      "force (F R ) .")
    EQ("F<sub>R</sub> = 3π · µ · D · V", "(7)")
    P("Thay “Eq. (7.1.4)” vào Phương trình (6) và giải theo µ,",
      "Substituting Eq. (7.1.4) in Eq. (6) and solving for µ ,")
    EQ("µ = D<sup>2</sup>·(w<sub>s</sub> − w<sub>l</sub>)/(18·V)", "(8)")
    P("Vận tốc rơi không đổi có thể tính bằng cách đo thời gian (t) quả cầu rơi qua một quãng "
      "đường (L). Cần lưu ý rằng nhớt kế bi cầu rơi chỉ áp dụng cho số Reynolds dưới 0,1 để thành "
      "thành không ảnh hưởng đến vận tốc rơi.",
      "The constant fall velocity can be calculated by measuring the time (t) taken by the ball "
      "to fall through a distance (L). It should be noted here that the falling sphere viscometer "
      "is applicable for the Reynolds number below 0.1 so that wall will not have any effect on "
      "the fall velocity.")

    # --------------------------------------------- Capillary Tube Viscometer
    H("4.12.3 Nhớt kế ống mao dẫn", "Capillary Tube Viscometer", h3)
    P("Loại nhớt kế này dựa trên dòng chảy tầng qua một ống tròn. Nó có một ống tròn gắn nằm ngang "
      "vào bình chứa chất lỏng cần đo. Một cột áp thích hợp (h<sub>f</sub>) được tạo cho chất lỏng "
      "để nó chảy tự do qua ống mao dẫn có chiều dài nhất định (L) vào bình thu như Hình 18. Lưu "
      "lượng (Q) của chất lỏng có trọng lượng riêng w<sub>l</sub> được đo qua lưu lượng thể tích "
      "trong bình. Phương trình Hagen–Poiseuille cho dòng tầng có thể dùng để tính độ nhớt (µ).",
      "This type of viscometer is based on laminar flow through a circular pipe. It has a "
      "circular tube attached horizontally to a vessel filled with a liquid whose viscosity has "
      "to be measured. Suitable head (hf ) is provided to the liquid so that it can flow freely "
      "through the capillary tube of certain length (L) into a collection tank as shown in Figure "
      "18. The flow rate (Q) of the liquid having specific weight wl can be measured through the "
      "volume flow rate in the tank. The HagenPoiseuille equation for laminar flow can be applied "
      "to calculate the viscosity (µ ) of the liquid.")
    EQ("µ = π·R<sup>4</sup>·w<sub>l</sub>·h<sub>f</sub>/(8·Q·L)", "(9)")
    FIG(18, F.fig_f18())

    # --------------------------------------------- Saybolt and Redwood
    H("4.12.4 Nhớt kế Saybolt và Redwood", "Saybolt and Redwood Viscometer", h3)
    P("Nhược điểm chính của nhớt kế ống mao dẫn là sai số do sự thay đổi tổn thất cột áp và các "
      "thông số khác. Tuy nhiên, công thức Hagen–Poiseuille vẫn áp dụng được bằng cách thiết kế "
      "nhớt kế kiểu chảy ra (efflux) hoạt động theo nguyên lý chảy dưới trọng lực thẳng đứng của "
      "chất lỏng nhớt qua một ống mao dẫn. Nhớt kế Saybolt có buồng hình trụ thẳng đứng chứa "
      "đầy chất lỏng cần đo (Figure 197.1.4-a). Buồng được bao quanh bởi bể nhiệt độ không đổi "
      "và một ống mao dẫn (dài 12 mm, đường kính 1,75 mm) gắn thẳng đứng ở đáy buồng. Để đo, nút "
      "ở đáy ống được rút ra và thời gian để 60 ml chất lỏng chảy ra được ghi lại, gọi là giây "
      "Saybolt. Vì vậy Phương trình (8) được dùng để tính lưu lượng Q bằng cách ghi thời gian "
      "(giây Saybolt) thu được 60 ml chất lỏng trong bình đong. Để tính độ nhớt động học ν, thu "
      "được biểu thức rút gọn:",
      "The main disadvantage of the capillary tube viscometer is the errors that arise due to "
      "the variation in the head loss and other parameters. However, the Hagen-Poiseuille formula "
      "can be still applied by designing a efflux type viscometer that works on the principle of "
      "vertical gravity flow of a viscous liquid through a capillary tube. The Saybolt viscometer "
      "has a vertical cylindrical chamber filled with liquid whose viscosity is to be measured "
      "(Figure 197.1.4-a). It is surrounded by a constant temperature bath and a capillary tube "
      "(length 12mm and diameter 1.75mm) is attached vertically at the bottom of the chamber. For "
      "measurement of viscosity, the stopper at the bottom of the tube is removed and time for "
      "60ml of liquid to flow is noted which is named as Saybolt seconds. So, Equation (8) can be "
      "used for the flow rate (Q) is calculated by recording the time (Saybolt seconds) for "
      "collection of 60ml of liquid in the measuring flask. For calculation purpose of kinematic "
      "viscosity (ν), the simplified expression is obtained as below;")
    EQ("ν = C<sub>1</sub>·t − C<sub>2</sub>/t", "(7)")
    P("Nhớt kế Redwood là một nhớt kế kiểu chảy ra khác (Hình 19-b) hoạt động theo cùng nguyên lý "
      "với Saybolt. Ở đây nút được thay bằng một lỗ nhỏ và giây Redwood được định nghĩa là thời "
      "gian để 50 ml chất lỏng chảy qua lỗ. Có thể viết biểu thức tương tự cho nhớt kế Redwood. "
      "Nhìn chung cả hai nhớt kế đều dùng để so sánh độ nhớt của các chất lỏng khác nhau. Vì vậy "
      "giá trị độ nhớt của chất lỏng có thể thu được bằng cách so sánh với thời gian của chất "
      "lỏng có độ nhớt đã biết.",
      "A Redwood viscometer is another efflux type viscometer (Figure 19-b) that works on the "
      "same principle of Saybolt viscometer. Here, the stopper is replaced with an orifice and "
      "Redwood seconds is defined for collection of 50ml of liquid to flow out of orifice. Similar "
      "expressions can be written for Redwood viscometer. In general, both the viscometers are "
      "used to compare the viscosities of different liquid. So, the value of viscosity of the "
      "liquid may be obtained by comparison with value of time for the liquid of known viscosity.")
    FIG(19, F.fig_f19())

    # --------------------------------------------- Capillary type
    H("4.12.5 Phép đo độ nhớt kiểu mao dẫn", "Capillary type of viscosity measurements", h3)
    P("Trong các phương pháp đo độ nhớt chất lỏng, phương pháp cổ điển của Poiseuille vẫn là "
      "tiêu chuẩn và nhớt kế dựa trên kỹ thuật này gọi là nhớt kế mao dẫn. Khi chất lỏng chảy qua "
      "ống có đường kính nhỏ 2R như Hình 20, thì với một kênh chảy hình vành có bề dày hướng kính "
      "dr ở khoảng cách r từ đường tâm, phương trình độ nhớt được cho bởi,",
      "Of the different methods of viscosity measurement for liquids the classical method due "
      "to Poiseuille is still the standard and the viscometer based on this technique is known as "
      "the capillary viscometer. When the liquid flows through a tube of small diameter 2R as "
      "shown in figure 20, then for an annular flow channel of radial thickness dr at a distance "
      "r from the central line, the viscosity equation is given by,")
    FIG(20, F.fig_f20())
    P("Trong đó v là vận tốc và P là hiệu áp suất qua ống dài l.",
      "Where, v – Velocity; P – Pressure difference across the tube of length l.")
    EQ("−π·2r·l·dr = µ·π·2r·dv")
    P("Lấy tích phân trong giới hạn r từ r = 0 đến R và v từ v = 0 đến v, ta được Phương trình "
      "Hagen–Poiseuille dạng chuẩn và lưu lượng thể tích:",
      "Integrating in the limits r = 0 to r = R and corresponding v = 0 to v gives the standard "
      "Hagen–Poiseuille form and the volume flow rate:")
    EQ("Q = π·P·R<sup>4</sup>/(8·µ·l),  µ = π·P·R<sup>4</sup>/(8·Q·l)")
    b.append(note(
        ("<b>Cuộc dẫn xuất bị OCR làm hỏng (trang in 158–159).</b> "
         "Các dòng dưới đây được giữ nguyên từ bản trích xuất thay vì sửa lại: " if vi else
         "<b>OCR-garbled derivation (source pp. 158–159).</b> "
         "The following lines are retained verbatim from the extraction rather than silently corrected: ")
        + "<pre style=\"white-space:pre-wrap;font-size:.8rem;margin:.4em 0\">"
        "2r P dv\n"
        "2 rl dr\n"
        "−π =µπ\n"
        "Where, v – Velocity\n"
        "\n"
        "Integrating in the limits rr R= → and corresponding vv 0= →\n"
        "Rv\n"
        "r0\n"
        "R2\n"
        "0\n"
        "v\n"
        "r\n"
        "22\n"
        "22\n"
        "Pr.dr .dv2l\n"
        "Pr [v]2l 2\n"
        "P (R r ) (0 v)4l\n"
        "Pv (R r )4l\n"
        "− = µ\n"
        "− =µ\n"
        "\n"
        "− − =µ−\n"
        "= −µ\n"
        "∫∫\n"
        "Volume flow rate,\n"
        "R\n"
        "v o\n"
        "R 22\n"
        "v o\n"
        "R 23\n"
        "r\n"
        "R24\n"
        "2\n"
        "o\n"
        "Q v.2 r.dr\n"
        "PQ .(R r ).2 r.dr4l\n"
        "P .2 (R .r r ).dr4l\n"
        "2P r rR4l 2 4\n"
        "= π\n"
        "= −ππ\n"
        "=π−π\n"
        "π= −µ \n"
        "∫\n"
        "∫\n"
        "∫\n"
        "4\n"
        "v\n"
        "PRQ 8l π= µ\n"
        "\n"
        "Hence absolute viscosity is given by,\n"
        "4\n"
        "v\n"
        "PR\n"
        "8Q l\n"
        "πµ=</pre>"))
    P("Phương pháp mao dẫn đã được dùng thành công trong các nhà máy lọc dầu để đo độ nhớt của "
      "sản phẩm dầu mỏ. Sơ đồ bố trí được chỉ trong “figure 21” — bản in nhắc đến hình này nhưng "
      "không in hình. Đây là phương pháp liên tục: chất lỏng được ép với vận tốc không đổi qua ống "
      "mao dẫn (ống ma sát). Độ giảm áp qua hai đầu ống được đo bằng Bộ truyền áp suất vi sai "
      "(DPT) kiểu cân bằng lực khí nén. Đồng hồ có thể hiệu chuẩn trực tiếp theo độ nhớt. Phương "
      "pháp đo được độ nhớt từ 10<sup>-3</sup> poise đến 3000 poise, dùng được ở áp suất tĩnh "
      "cao và phù hợp cho chỉ thị và điều khiển từ xa.",
      "The capillary method has been successfully used in refineries for measuring viscosities "
      "of petroleum products. The schematic arrangement is shown in figure 21. This is a "
      "continuous method. The liquid is forced at a constant velocity through the capillary "
      "(friction tube). The pressure drops across the ends of the tube is measured by a "
      "pneumatic force balance type Differential Pressure Transmitter (DPT). The indicator can "
      "be directly calibrated in viscosity. This method can measure viscosity from 10-3 poise to "
      "3000 poise. It is usable at high static pressures and is suitable for remote indication "
      "and control.")

    # ---------------------------------------------------------------- 4.13
    H("4.13 Đo độ đục", "4.13 Turbidity measurement")
    P("Độ đục là mức độ đục của nước. Nó có thể thay đổi từ một dòng sông đầy bùn và cát, nơi "
      "không thể nhìn xuyên qua nước (độ đục cao), đến nước suối có vẻ hoàn toàn trong (độ đục "
      "thấp). Độ đục có thể do: cát, bùn và đất; vi khuẩn và các mầm bệnh khác; kết tủa hoá học.",
      "Turbidity is the amount of cloudiness in the water. This can vary from a river full of mud "
      "and silt where it would be impossible to see through the water (high turbidity), to a "
      "spring water which appears to be completely clear (low turbidity). Turbidity can be caused "
      "by: silt, sand and mud; bacteria and other germs; chemical precipitates.")
    U(["Cát, bùn và đất;", "Vi khuẩn và các mầm bệnh khác;", "Kết tủa hoá học."],
      ["Silt, sand and mud ;", "Bacteria and other germs;", "Chemical precipitates."])
    P("Điều rất quan trọng là đo độ đục của nguồn nước sinh hoạt, vì các nguồn này thường trải qua "
      "một số dạng xử lý nước có thể bị ảnh hưởng bởi độ đục. Ví dụ, trong mùa mưa khi bùn và cát "
      "bị cuốn vào sông suối, độ đục cao có thể nhanh chóng làm tắc bộ lọc và khiến chúng ngừng "
      "hoạt động hiệu quả. Độ đục cao cũng làm đầy bể và ống bằng bùn cát, và có thể làm hỏng van "
      "và vòi. Ở nơi nước được khử trùng bằng clo, ngay cả độ đục khá thấp cũng ngăn clo tiêu "
      "diệt mầm bệnh trong nước một cách hiệu quả.",
      "It is very important to measure the turbidity of domestic water supplies, as these "
      "supplies often undergo some type of water treatment which can be affected by turbidity. "
      "For example, during the rainy season when mud and silt are washed into rivers and streams, "
      "high turbidity can quickly block filters and stop them from working effectively. High "
      "turbidity will also fill tanks and pipes with mud and silt, and can damage valves and taps. "
      "Where chlorination of water is practised, even quite low turbidity will prevent the "
      "chlorine killing the germs in the water efficiently.")
    P("Một số hệ xử lý, như bể lắng, bể keo tụ và bộ lọc sỏi thô, được thiết kế để loại bỏ độ "
      "đục. Điều quan trọng với người vận hành cả hệ lớn lẫn nhỏ là biết các hệ này hoạt động tốt "
      "như thế nào. Đo độ đục của nước trước và sau mỗi phần của hệ có thể cho người vận hành biết "
      "cần bảo trì hoặc vệ sinh ở đâu.",
      "Some treatment systems, such as sedimentors, coagulators and gravel prefilters are "
      "designed to remove turbidity. It is important for operators of both large and small "
      "treatment systems to know how well these systems are working. Measuring the turbidity of "
      "the water before and after each part of the system can tell the operator where "
      "maintenance or cleaning is needed.")

    # --------------------------------------------- Measuring turbidity
    H("4.13.1 Đo độ đục", "Measuring turbidity", h3)
    P("Độ đục có thể đo bằng máy đo độ đục điện tử hoặc ống đo độ đục. Cả hai phương pháp đều có "
      "ưu và nhược điểm, như dưới đây. Độ đục thường được đo bằng đơn vị độ đục nephhelometric "
      "(NTU) hoặc đơn vị độ đục Jackson (JTLJ), tuỳ phương pháp đo; hai đơn vị này xấp xỉ bằng nhau.",
      "Turbidity can be measured using either an electronic turbidity meter or a turbidity tube. "
      "Both methods have advantages and disadvantages, as shown below. Turbidity is usually "
      "measured in nephelometric turbidity units (NTU) or Jackson turbidity units (JTLJ), "
      "depending on the method used for measurement. The two units are roughly equal.")

    # --------------------------------------------- Turbidity meter
    H("4.13.2 Máy đo độ đục", "Turbidity meter", h3)
    P("Có nhiều loại máy đo độ đục điện tử khác nhau. Ưu và nhược điểm như sau:",
      "There are many different types of electronic turbidity meter available. Their advantages "
      "and disadvantages are as follows:")
    P("<b>Ưu điểm / Advantages</b>", "<b>Advantages</b>")
    U(["rất chính xác, đặc biệt hữu ích để đo độ đục rất thấp (dưới 5TU)."],
      ["very accurate, and especially useful for measuring very low turbidities (less than 5TU)"])
    P("<b>Nhược điểm / Disadvantages</b>", "<b>Disadvantages</b>")
    U(["chi phí cao;", "cần nguồn điện (điện lưới hoặc pin);", "dễ bị hỏng."],
      ["high cost", "need power supply (mains or battery)", "easily damaged"])
    P("Không thể đưa ra hướng dẫn chung về cách sử dụng ở đây. Bạn nên tham khảo hướng dẫn của "
      "nhà sản xuất về việc sử dụng và bảo trì các máy này. Hình 22 cho một ví dụ về máy đo độ đục "
      "điện tử.",
      "It is impossible to give general guidelines on their use here. You should refer to "
      "manufacturers’ instructions for use and maintenance of these meters. Figure 22 shows an "
      "example of an electronic turbidity meter.")
    FIG(22, F.fig_f22())

    # --------------------------------------------- Turbidity tube
    H("4.13.3 Ống đo độ đục", "Turbidity tube", h3)
    P("Ưu và nhược điểm của ống đo độ đục như sau:",
      "The advantages and disadvantages of the turbidity tube are as follows:")
    P("<b>Ưu điểm / Advantages</b>", "<b>Advantages</b>")
    U(["thiết kế đơn giản;", "chi phí thấp;", "không dễ hỏng."],
      ["simple design", "low cost", "not easily damaged"])
    P("<b>Nhược điểm / Disadvantages</b>", "<b>Disadvantages</b>")
    U(["không đo được độ đục rất thấp (mức tối thiểu thường là 5TU);",
       "kém chính xác hơn."],
      ["cannot measure very low turbidities (usual minimum is 5TU)", "less precise"])
    P("Vì ống đo độ đục dễ dùng, hướng dẫn được đưa ra dưới đây. Tuy nhiên, nên tham khảo hướng "
      "dẫn đi kèm với ống bạn đang dùng.A turbidity tube is shown in Figure 23",
      "Since the turbidity tube is simple to use, instructions are given below. It is, however, "
      "recommended that you refer to the instructions provided with the tube that you are "
      "using.A turbidity tube is shown in Figure 23")
    FIG(23, F.fig_f23())
    P("Để đo độ đục của mẫu nước bằng ống đo độ đục:",
      "To measure the turbidity of a water sample using a turbidity tube :")
    OL(["Nếu ống gồm hai phần, đẩy hai phần lại với nhau, bảo đảm chúng khớp vuông góc.",
        "Lấy một mẫu nước từ nguồn nước.",
        "Cầm ống bằng một tay gần đáy và nhìn vào đầu mở, để đầu ở cách mắt khoảng 10 đến 20 "
        "centimet, sao cho bạn nhìn rõ vòng tròn màu đen,",
        "dấu chéo hoặc vật mờ ở đáy ống.",
        "Rót từ từ mẫu nước vào ống, chờ bọt khí nổi lên nếu cần, cho đến khi vạch ở đáy ống vừa "
        "biến mất.",
        "Ngừng rót và nhìn mức nước trong ống. Với ống có thang độ đục ghi trên thành, đọc số "
        "tại vạch gần nhất với mức nước — đó là độ đục của nước. Nếu ống không có thang, đo "
        "khoảng cách từ bottonz của ống tới mức nước bằng thước dây rồi tra cứu hoặc tính độ đục "
        "theo hướng dẫn đi kèm ống.",
        "Sau khi dùng, rửa ống bằng nước sạch và cất hai phần của ống nơi không bị hư hỏng."],
       ["Where the tube is in two parts, push the two parts together; making sure that they fit "
        "squarely.",
        "Take a sample of water from the water source. .",
        "Hold the tube in one hand near the bottom and look into the open end with your head "
        "about 10 to 20 centimetres above the tube, so that you can clearly see the black circle,",
        "cross or other murk on the bottom of the tube.",
        "Slowly pour the water sample into the tube, waiting for air bubbles to rise if "
        "necessary, until the mark on the bottom of the tube just disappears.",
        "Stop pouring the water sample into the tube and look at the level of water in the tube. "
        "For turbidity tubes which have a turbidity scale marked on the side, read the number on "
        "the nearest line to the water level. This is the turbidity of the water. I f the tube "
        "does not have a scale marked, measure the distance from the bottonz of the tube to the "
        "water level with a tape measure and look up or calculate the turbidity of the water "
        "sample using the instructions provided with the tube.",
        "After use, wash the tube in clean water and store the two parts of the tube where they "
        "cannot be damaged."])

    # --------------------------------------------- Turbidity guidelines
    H("4.13.4 Hướng dẫn độ đục cho nước uống", "Turbidity guidelines for drinking water", h3)
    P("Đối với nguồn nước uống, nên cân nhắc các hướng dẫn sau:",
      "For drinking water supplies, the following guidelines should be taken into "
      "consideration:")
    U(["Nước uống nên có độ đục 5 NTU/JTU hoặc thấp hơn. Độ đục trên 5 NTU/JTU sẽ được người dùng "
       "nhận thấy và có thể khiến họ từ chối nguồn nước.",
       "Nơi nước được khử clo, độ đục nên dưới 5 NTU/JTU và tốt nhất là dưới 1 NTU/JTU để quá "
       "trình khử clo có hiệu quả."],
      ["Drinking water should have a turbidity of 5 NTU/JTU or less. Turbidity of more than 5 "
       "NTU/JTU would be noticed by users and may cause rejection of the supply.",
       "Where water is chlorinated, turbidity should be less than 5 NTU/JTU and preferably less "
       "than 1 NTU/JTU for chlorination to be effective."])

    # ---------------------------------------------------------------- 4.14
    H("4.14 Đo độ dẫn", "4.14 Conductivity measurement")
    P("Phép đo độ dẫn chỉ có thể thực hiện sau khi hiệu chuẩn, vì giá trị hằng số cell được dùng "
      "để tính độ dẫn.",
      "Conductivity measurements can only be performed after calibration, as the cell constant "
      "value is used to calculate the conductivity.")

    # --------------------------------------------- Low conductivity
    H("4.14.1 Đo độ dẫn thấp (nước tinh khiết)", "Low conductivity measurements (pure water)", h3)
    P("Một trong những ứng dụng chính của phép đo độ dẫn thấp là kiểm tra chất lượng nước tinh "
      "khiết. Các phòng thí nghiệm dược phẩm có nghĩa vụ tuân thủ quy định do các dược điển quốc "
      "gia đặt ra. Ví dụ, phụ lục lần thứ năm của Dược điển Hoa Kỳ (USP) quy định các nguyên tắc "
      "kiểm tra chất lượng nước tinh khiết hoặc nước khử ion hoàn toàn dùng sản xuất các sản phẩm "
      "tiêm.",
      "One of the main applications of low conductivity measurements is checking the quality of "
      "pure water. Pharmaceutical laboratories are obliged to respect regulations laid down by "
      "national pharmacopoeias, for example the 5th supplement of the United States "
      "Pharmacopoeia (USP) lays down rules for checking the quality of pure water or fully "
      "deionised water used for the production of injection products.")

    # --------------------------------------------- Principle of pure water
    H("4.14.2 Nguyên lý đo nước tinh khiết", "Principle of pure water measurements", h3)
    H("4.14.2.1 Theo USP", "According to USP", h4)
    P("Độ dẫn phụ thuộc một phần vào pH, nhiệt độ và lượng carbon dioxide trong khí quyển đã hoà "
      "tan trong nước tạo thành ion (độ dẫn nội tại). Độ dẫn cũng phụ thuộc vào các ion clorua, "
      "natri và amoni được coi là tạp chất của nước (độ dẫn ngoại lai). Độ dẫn (nội tại và ngoại "
      "lai) của nước được đo và so sánh với các giá trị trong bảng để đánh giá nước có phù hợp "
      "cho ứng dụng dược phẩm hay không. Nếu mẫu không đạt Giai đoạn 1, phải thực hiện thêm các "
      "phép thử (Giai đoạn 2 và 3) để xác định giá trị độ dẫn quá cao là do yếu tố nội tại hay do "
      "ion ngoại lai. Yêu cầu chính là hằng số cell phải được biết với độ bất định tốt hơn ±2%.",
      "The conductivity partly depends on the pH, the temperature and the amount of atmospheric "
      "carbon dioxide, which has been dissolved in the water to form ions (intrinsic "
      "conductivity). The conductivity also depends on the chloride, sodium and ammonium ions "
      "considered as water impurities (extraneous conductivity). The conductivity (intrinsic and "
      "extraneous) of the water is measured and compared to values listed in a table to evaluate "
      "if the studied water is suitable or not for use in pharmaceutical applications. If the "
      "sample fails Stage 1, additional tests have to be performed (Stages 2 and 3) in order to "
      "determine if the excessive conductivity value is due to intrinsic factors or extraneous "
      "ions. The main requirement is that the cell constant be known with an uncertainty better "
      "than ±2%.")
    H("4.14.2.2 Theo Dược điển Châu Âu", "According to the European Pharmacopoeia", h4)
    P("Cell gồm hai bản platin song song ở khoảng cách xác định. Nó được đặt trong vỏ thuỷ tinh "
      "với hai đầu nối ống cho phép đo ở chế độ dòng chảy. Cell được hiệu chuẩn bằng dung dịch "
      "chuẩn độ dẫn 26,6 µS/cm ở 20°C, có thể truy vết tới NIST1). Mọi phép đo được thực hiện "
      "bằng máy đo độ dẫn chính xác dùng dòng xoay chiều tần số thấp.",
      "The cell consists of two parallel platinum plates at a defined distance. It is confined "
      "within a glass jacket with two pipe connectors enabling measurement in flow mode. This "
      "cell is calibrated using a conductivity standard of 26.6 µS/cm at 20°C, which is "
      "traceable to NIST1). All measurements are made with a precision conductivity meter using "
      "AC current at a low frequency.")
    H("4.14.2.3 Đo độ dẫn cao", "High conductivity measurements", h4)
    P("Đo độ dẫn cao được thực hiện khi mẫu là dung dịch nước có nồng độ rất cao các loài phân li, "
      "tức là muối, axit và base. Phương pháp độ dẫn dùng để kiểm soát nồng độ của dung dịch tinh "
      "hoặc hỗn hợp. Ví dụ, trong nhà máy sản xuất axit hoặc base đậm đặc, phương pháp độ dẫn được "
      "ưu tiên hơn phép đo pH.",
      "High conductivity measurements are performed when samples are water solutions, highly "
      "concentrated in dissociated species, i.e. salts, acids and bases. The conductivity method "
      "is used to control the concentration of pure or mixed solutions. For example, the "
      "conductivity method is preferred to pH measurements in production plants of concentrated "
      "acids or bases.")

    # ---------------------------------------------------------------- refs
    H("Tài liệu tham khảo", "References")
    b.append(refs(_REFS))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
