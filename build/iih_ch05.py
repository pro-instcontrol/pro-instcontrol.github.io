# -*- coding: utf-8 -*-
"""Book 8, Chapter 5 - Measurement of Flow Rate (EN/VI bilingual).

Source: 3G E-learning LLC, *Illustrated Handbook of Industrial Instrumentation
and Control* (2018), PDF pp. 181-216 (36 pages), printed pp. 167-202.  Chapter
6 ("Mechanical Flow Meters") begins at PDFPAGE 217 and is excluded.

The source order is kept: Introduction; Basic Concept of Flow Measurement
(Units of Flow, Turbulent Flow, Discharge Coefficient, Flow Coefficient);
Differential Pressure Meter (Orifice Plate with principle, types, machining,
materials and taps; Venturi Tubes with construction, long and short forms,
types and installation; Flow Nozzle; Dall Tube Flow Meters); Pitot tube; and
the 57 numbered references.  Display equations lost or garbled by the OCR are
reconstructed from the printed symbol definitions and flagged in the notes.
The "Citation:" lines are image credits and are not part of the reference list.
"""

import iih_common as C
import iihfig5 as F
from iih_common import (eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 36          # PDF pp. 181-216 inclusive (printed pp. 167-202)
BYLINE = "3G E-learning LLC · Illustrated Handbook of Industrial Instrumentation &amp; Control (2018)"
TITLE_EN = "Measurement of Flow Rate"
TITLE_VI = "Đo lưu lượng"


# ---------------------------------------------------------------------------
# Reference list (source printed pp. 198-202, numbered 1-57).  The text of
# every entry follows the printed source, including OCR damage such as
# "ad Jolivet", "va- pors", "de- velopments", "Synposiumon FlowCIts" and the
# stray unnumbered "Dijstelbergen" line left between entries 7 and 8 (kept in
# entry 7).  Bare ampersands in publisher names are XML-escaped.
# ---------------------------------------------------------------------------
_REFS = [
    "A.Bhalerao, C-F Westin, and R. Kikinis. Unwrapping phase artifacts in 3d "
    "phase contrast angiograms. In Proceedings of 1st Joint Meeting of "
    "CVRMED/MRCAS '97, Grenoble, France, 1997.",
    "A.Herment, O. Mousseaux, E. ad Jolivet, A. DeCesare, F. Frouin, A. "
    "Todd-Pokrpoek, and J. Bittoun. Improved estimation of velocity and flow "
    "rate using regularized three-point phase-contrast velocimetry. Magnetic "
    "Resonance in Medicine, 44(1):122-128, 2000.",
    "Almquist, C.W., D.B. Hansen, and P.A. March, Pressure-Time Flow Rate in "
    "Low Head Hydro, Proceedings, Symposium on Fundamentals and Advancements "
    "in Hydraulic Measurements and Experimentation, Buffalo NY, 1994.",
    "American Society of Mechanical Engineers, Performance Test Codes - "
    "Hydraulic Turbines and Turbine Mode of Pump/Turbines, revision, "
    "Performance Test Code 18, New York NY, 1992.",
    "American Society of Mechanical Engineers, Fluid Meters, Their Theory and "
    "Application, H.S. Bean, editor, sixth edition revised, Research Committee "
    "on Fluid Meters, New York, 1983.",
    "Bos, M.G., Discharge Measurement Structures, ILRI Publication 20, Third "
    "Revised Edition, Wageningen, The Netherlands, 1989.",
    "British Standards Institution, B.S. 1042, Flow Measurement, 1943. "
    "[Stray unnumbered source line: Dijstelbergen, H.H., Gas Meters, In: "
    "Developments In Flow]",
    "Curtis W. Chen and Howard A. Zebker. Two-dimensional phase unwrapping with "
    "use of statistical models for cost functions in nonlinear optimization. "
    "Journal of the Optical Society of America A: Optical Image Science and "
    "Visualisation, 18(2):338-351, 2001.",
    "Furness, R.A., Developments in Pipeline Instrumentation, in Measurement "
    "and Control, No. 20, pp. 25-28, 1987.",
    "G.H. Glover and E. Schneider. Three-point dixon technique for true "
    "water/fat decomposition with b0 inhomogeneity correction. Magnetic "
    "Resonance in Medicine, 18(371-383), 1991.",
    "G.L. Nayler, D. B. Firmin, and D.B. Longmore. Blood flow imaging by CINE "
    "magnetic resonance. Journal of Computer Assisted Tomography, 10:715-722, 1986.",
    "G.S. Sobering, Y. Shiferaw, P. van Gelderen, and C.T.W. Moonen. "
    "Quantitative measurement of the phase error for a simple and rapid "
    "phase-unwrapping algorithm. In Proc. International Soc. of Magnetic "
    "Resonance in Medicine, 1995.",
    "Gibson, N.R., The Gibson Method and Apparatus for Measuring the Flow of "
    "Water in Closed Conduits, In: Transactions of the American Society of "
    "Mechanical Engineers, vol. 45, p. 343, 1923.",
    "Greve, F.W., Measuring of Pipe Flow by the Coordinate Method, Purdue "
    "Engineering Experiment Station, Bulletin 32, 1928.",
    "Hobbs, M., Inside the Orifice Plate, Process Engineering, London, vol. "
    "68(2), pp. 33, 35, 1987.",
    "Humphreys, J.S., Improving the Performance of Those Orifice Plates, "
    "Process Engineering (London), vol. 68(2), pp. 37, 39, 41, 1987.",
    "Igor P. Gurov and Denis V. Sheynihovich. Interferometric data analysis "
    "based on markov nonlinear filtering methodology. Journal of the Optical "
    "Society of America A: Optical Image Science and Visualisation, 17(1):21-27, 2000.",
    "International Organization for Standardization, Measurement of Fluid Flow "
    "in Closed Conduits: Velocity Area Method Using Pitot Tubes, ISO 3966, "
    "First Edition, Zurich, Switzerland, 1977.",
    "International Organization for Standardization, Measurement of Fluid Flow "
    "in Closed Conduits: Velocity Area Method Using Pitot Tubes, ISO 5167-1, 1991.",
    "J. R. Panell, Fluid velocity and pressure. Edward Arnold &amp; Co., London, "
    "135 p. (1924).",
    "J. W. McBain, The sorption of gases and va- pors by solids. E. Routledge "
    "&amp; Sons, London, 577 p. (1932)",
    "Jason N. Vestal and Eric A Bridge. A Quantitative Approach to Selecting "
    "Nozzle Flow Rate and Stream, Part 1. (Fire Engineering, October 1, 2010)",
    "Jason N. Vestal and Eric A Bridge. A Quantitative Approach to Selecting "
    "Nozzle Flow Rate and Stream, Part 2. (Fire Engineering, January 1, 2011)",
    "Jerry Knapp, Tim Pillsworth, and Christopher Flatley. Nozzle Tests Prove "
    "Fireground Realities, Part 1. (Fire Engineering, February 2003)",
    "Jerry Knapp, Tim Pillsworth, and Christopher Flatley. Nozzle Tests Prove "
    "Fireground Realities, Part 2. (Fire Engineering, September 2003)",
    "Jerry Knapp, Tim Pillsworth, and Christopher Flatley. Nozzle Tests Prove "
    "Fireground Realities, Part 3. (Fire Engineering, February 2004)",
    "Jerzy Szumowski, William R. Coshow, Fang Li, and Stephen F. WQuinn. Phase "
    "unwrapping in the three-point dixon method for fat suppression mr "
    "imaging. Radiology, 192(2):555-561, 1994.",
    "Klett, Tim. Fire Notes: Stretching and Operating the First Line. "
    "(Indianapolis, IN Fire Department Training Network, 2004)",
    "L. Dunoyer, Vacuum practice. Translation by J. H. Smith, D. Van Nostrand "
    "Co., New York, 228 p. (1926).",
    "Lawrence, F.E., and P.L. Braunworth, Fountain Flow of Water in Vertical "
    "Pipes, In: Transactions of the American Society of Civil Engineers, "
    "vol. 57, pp. 265-306, 1906.",
    "Leon Axel and Daniel Morton. Correction of phase wrapping in magnetic "
    "resonance imaging Medical Physics, 16(2):284-287, 1989.",
    "Li An, Qing-San Xiang, and Sofia Chavez. A fast implementation of the "
    "minimum spanning tree method for phase unwrapping. IEEE Trans. on Medical "
    "Imaging, 19(8):805-808, 2000.",
    "M. Benedick &amp; C. Williams, Engineering de- velopments in the gaseous "
    "diffusion process. McGraw-Hill Book Co., New York, 129 p. (1949)",
    "Mark Hedley and Dov Rosenfeld. A new two-dimensional phase unwrapping "
    "algorithm for mri images. Magnetic Resonance in Medicine, 24(1):177-181, 1992.",
    "McGrail, David. Firefighting Operations in High-rise and Standpipe "
    "Equipped Buildings. (Tulsa, Oklahoma, Pennwell Corporation, 2007)",
    "Measurement, R.W.W. Scott (editor), 1982, chapter 5, pp. 129-170, Applied "
    "Science Publishers, London. 333 p., 1982.",
    "Natural Resources Conservation Service, National Engineering Handbook, "
    "Part 623, Section 15 (pipe coordinates), Chapter 9, Measurement of "
    "Irrigation Water, 1962a.",
    "Natural Resources Conservation Service, National Engineering Handbook, "
    "Part 623, Section 15, Chapter 5, Furrow Irrigation, 1962b.",
    "Neng H. Ching, Dov Rosenfeld, and Michael Braun. Two-dimensional phase "
    "unwrapping using a minimum spanning tree algorithm. IEEE Trans. on Image "
    "Processing, 1(3):355-365, 1992.",
    "P. Jezzard and R.S. Balaban. Correction for geometric distortion in echo "
    "planar images from B0 field variations. Magnetic Resonance in Medicine, "
    "34:65-73, 1995.",
    "P. Munger, G.R. Crelier, and T.M. Peters. An inverse problem approach to "
    "the correction of distortion in epi images. IEEE Trans. on Medical Imaging, "
    "19(7):681-689, 2000.",
    "Q.S. Xiang. Temporal phase unwrapping for CINE velocity imaging. Magnetic "
    "Resonance in Medicine, 5(5):529-534, 1995.",
    "R. M. Weisskoff and T. L. Davis. Correcting gross distotion on echo planar "
    "images. In Proc. International Soc. of Magnetic Resonance in Medicine, "
    "page 4515, Berlin, 1992.",
    "Rainer Krämer and Otmar Loffeld. Phase unwrapping for sar interferometry "
    "with kalman filters. In Proceedings of the EUSAR'96 Conference, pages "
    "165-169, 1996.",
    "Replogle, J.A., and B.T. Wahlin, Venturi Meter Construction for Plastic "
    "Irrigation Pipelines, Proceedings, Applied Engineering in Agriculture, "
    "American Society of Agricultural Engineers, 10(1):21-26, 1994.",
    "Richman, Harold. Engine Company Fireground Operations 2nd Edition. "
    "(Quincy, MA National Fire Protection Association, 1986)",
    "Rohwer, C., Discharge of Pipes Flowing Partly Full, Civil Engineering, "
    "American Society of Civil Engineers, 1943.",
    "S. J. Gregg, The absorption of gases by solids. Methuen's Monographs on "
    "Chemical Subjects, Van Nostrand Co., New York, 120 p. (1934).",
    "S. Moon-Ho Song, Sandy Napel, Norbert J. Pelc, and Gary H. Glover. Phase "
    "unwrapping of MR phase images using poisson equation. IEEE Trans. on "
    "Image Processing, 4(5):667-676, 1995.",
    "Scott, V.E., and C.E. Houston, Measuring Irrigation Water, Circular 473, "
    "California Agricultural Experiment Station, University of California, 1959.",
    "Summers, J.B., Flow Characteristics of 8-, 10-, 12-, and 18-Inch Concrete "
    "Fresno Irrigation Meters, Hydraulic Laboratory Report No. HYD-340, Bureau "
    "of Reclamation, Denver CO, 1952.",
    "Summers, J.B., Hydraulic Investigations of the Consolidated Irrigation "
    "District Venturi-Type Meters, Hydraulic Laboratory Report No. HYD-341, "
    "Bureau of Reclamation, Denver CO, 1953.",
    "T. R. Judge and P. J. Bryanston-Cross. A review of phase unwrapping "
    "techniques in fringe analysis. Optics and Lasers in Engineering, 21:199-239, 1994.",
    "Vanleer, B.R., The California Pipe Method of Water Measurement, "
    "Engineering News Record, August 3, 1922, and August 21, 1924.",
    "White, R., and McMurtrie, The Vortex Shedding Flowmeter, Paper 2-16-187, "
    "Synposiumon FlowCIts Measurement and Control in Science and Industry, 1971.",
    "Yi Wang, Debiao Li, and Mark Haacke. A new phase unwrapping method for "
    "water and fat separation in inhomogeneous fields. In Proc. International "
    "Soc. of Magnetic Resonance in Medicine, 1995.",
    "Zhi-Pei Liang. A model-based method for phase unwrapping. IEEE Trans. on "
    "Medical Imaging, 15(6):893-897, 1996.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> lưu lượng — flow rate · đo lưu lượng — flow "
                "measurement · lưu lượng thể tích / trọng lượng — volumetric / weight rate · "
                "chất lỏng không nén / nén được — incompressible / compressible · STP · NTP · "
                "dòng chảy rối — turbulent flow · dòng chảy tầng — laminar flow · hệ số lưu "
                "lượng Cd — discharge coefficient · hệ số dòng chảy K — flow coefficient · "
                "hệ số tiến tốc độ — velocity approach factor · đồng hồ chênh áp — differential "
                "pressure (DP) meter · tấm lỗ — orifice plate · vena contracta · mặt bích — "
                "flange · cổ họng — throat · ống Venturi — Venturi tube · buồng nhận áp — "
                "annular chamber · vòi phun — flow nozzle · ống Dall — Dall tube · ống Pitot — "
                "Pitot tube · áp suất dừng — stagnation pressure · áp suất động — dynamic "
                "pressure · đầu dò tĩnh — static tap")
    return ("<b>Key terms.</b> flow rate · flow measurement · volumetric / weight rate · "
            "incompressible / compressible fluid · STP · NTP · turbulent flow · laminar flow · "
            "discharge coefficient Cd · flow coefficient K · velocity approach factor · "
            "differential pressure (DP) meter · orifice plate · vena contracta · flange · "
            "throat · Venturi tube · annular chamber · flow nozzle · Dall tube · Pitot tube · "
            "stagnation pressure · dynamic pressure · static tap")


def source_notes(lang):
    """Language-aware box for extraction/OCR quirks (never named `note`)."""
    if lang == "vi":
        return note(
            "<b>Ghi chú của người dịch và của quá trình trích xuất.</b> Nhiều phương trình "
            "được in dạng hình trong nguồn đã bị OCR làm mất hoặc xáo trộn thân công thức; "
            "các dạng chuẩn được dựng lại từ định nghĩa ký hiệu in kèm và được ghi rõ tại "
            "chỗ trong hộp “Thân công thức bị mất”. Các nét OCR được giữ nguyên trong văn "
            "bản Anh gồm “venacontracta”, “The flow rate.is”, “F is known as the plater”, "
            "“slettite coating”, “lithcote lined”, “Synposiumon FlowCIts”, “va- pors”, "
            "“de- velopments”, chú thích Hình 9 kết thúc bằng “tg”, và việc định nghĩa d, D "
            "bị đảo ở mục Concentric so với mục Types of Orifice Plates. Số phương trình "
            "(2) lặp lại hai lần trong bản in và được bảo lưu. Các dòng “Citation:” là ghi "
            "công ảnh, không phải tài liệu tham khảo; danh mục gồm đúng 57 mục có số, với "
            "dòng lạc đề của Dijstelbergen được giữ trong mục 7. Nguồn cũng có mô tả Dall "
            "tube về áp suất cao/thấp dường như đảo so với cấu tạo; văn bản được giữ như in. "
            "Chương bắt đầu ở trang in 167 và kết thúc ở trang in 202; chương 6 ở PDFPAGE 217 "
            "không được đưa vào.")
    return note(
            "<b>Translator and extraction notes.</b> Several displayed equations were printed "
            "as images and the OCR lost or scrambled their formula bodies; the standard forms "
            "reconstructed from the printed symbol definitions are flagged in place in the "
            "“Formula bodies lost” box. OCR quirks kept in the English text include "
            "“venacontracta”, “The flow rate.is”, “F is known as the plater”, “slettite "
            "coating”, “lithcote lined”, “Synposiumon FlowCIts”, “va- pors”, "
            "“de- velopments”, the Figure 9 caption ending in “tg”, and the swapped "
            "definitions of d and D in the Concentric subsection relative to Types of Orifice "
            "Plates. Equation number (2) appears twice in the printed source and is preserved. "
            "The “Citation:” lines are image credits, not references; the list contains exactly "
            "57 numbered entries, with the stray Dijstelbergen line kept inside entry 7. The "
            "source description of the Dall tube also appears to reverse the high- and "
            "low-pressure locations; the text is kept as printed. The chapter runs from "
            "printed p. 167 to p. 202; Chapter 6 at PDFPAGE 217 is excluded.")


def formula_notes(lang):
    """One box covering every displayed equation lost or garbled by the OCR."""
    if lang == "vi":
        return note(
            "<b>Thân công thức bị mất khi trích xuất.</b> Các dạng chuẩn được dựng lại từ định "
            "nghĩa ký hiệu: hệ số lưu lượng C = q<sub>actual</sub>/q<sub>ideal</sub>; hệ số "
            "dòng chảy K = C<sub>d</sub>/√(1 − β<sup>4</sup>) với hệ số tiến tốc độ "
            "M<sub>va</sub> = 1/√(1 − β<sup>4</sup>); phương trình áp kế chênh áp "
            "Q = K·A·√(2gh(ρ<sub>m</sub> − ρ<sub>f</sub>)/ρ<sub>f</sub>) và đổi mật độ "
            "Q<sub>s</sub> = Q·√(ρ<sub>f</sub>/ρ<sub>s</sub>); phương trình Bernoulli dạng "
            "Q = A·V<sub>avg</sub> cùng đẳng thức cột áp giữa hai mặt cắt; lưu lượng khối "
            "W = K·A·ρ·√(2gh) và K = C/√(1 − β<sup>4</sup>); lưu lượng ống Dall "
            "v = K·√(DP); vận tốc ống Pitot v = √(2gh) và v<sub>actual</sub> = "
            "C<sub>v</sub>·√(2gh). Số hiệu (2) bị lặp được giữ nguyên.")
    return note(
            "<b>Formula bodies lost in extraction.</b> The standard forms reconstructed from "
            "the printed symbol definitions are: the discharge coefficient "
            "C = q<sub>actual</sub>/q<sub>ideal</sub>; the flow coefficient "
            "K = C<sub>d</sub>/√(1 − β<sup>4</sup>) with velocity approach factor "
            "M<sub>va</sub> = 1/√(1 − β<sup>4</sup>); the differential-manometer relation "
            "Q = K·A·√(2gh(ρ<sub>m</sub> − ρ<sub>f</sub>)/ρ<sub>f</sub>) and the density "
            "conversion Q<sub>s</sub> = Q·√(ρ<sub>f</sub>/ρ<sub>s</sub>); the Bernoulli pair "
            "Q = A·V<sub>avg</sub> with the head balance between two sections; the mass-flow "
            "equation W = K·A·ρ·√(2gh) and K = C/√(1 − β<sup>4</sup>); the Dall-tube "
            "relation v = K·√(DP); and the Pitot-tube velocities v = √(2gh) and "
            "v<sub>actual</sub> = C<sub>v</sub>·√(2gh). The duplicated equation number (2) is "
            "kept as printed.")


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
        "Chương này trình bày phép đo lưu lượng của chất rắn, chất lỏng và chất khí theo hai "
        "cách cơ bản: theo thể tích hoặc theo trọng lượng. Sau khái niệm và đơn vị, chương đi "
        "vào đồng hồ chênh áp với tấm lỗ, ống Venturi, vòi phun, ống Dall và ống Pitot, kèm "
        "nguyên lý, cấu tạo, lắp đặt, ưu và nhược điểm."
        if vi else
        "This chapter covers the measurement of the flow of solids, liquids and gases in two "
        "basic ways: on a volumetric basis and on a weight basis. After the concept and units "
        "of flow, it turns to differential pressure meters - the orifice plate, Venturi tube, "
        "flow nozzle, Dall tube and Pitot tube - with their principles, construction, "
        "installation, advantages and disadvantages."))
    b.append(source_notes(lang))

    # ---------------------------------------------------------------- 5.1
    H("5.1 Giới thiệu", "5.1 Introduction")
    P("Đo lưu lượng công nghiệp gồm đo lưu lượng của chất rắn, chất lỏng và chất khí. Có hai "
      "cách cơ bản để đo lưu lượng: một theo thể tích và một theo trọng lượng. Chất rắn thường "
      "được đo theo trọng lượng hoặc khối lượng trên một đơn vị thời gian; rất hiếm khi đo "
      "chất rắn theo thể tích. Chất lỏng được đo theo lưu lượng thể tích hoặc lưu lượng trọng "
      "lượng. Chất khí thường được đo theo lưu lượng thể tích.",
      "Industrial flow measurements include measuring of flow rate of solids, liquids and gases. "
      "There are two basic ways of measuring flow; one on volumetric basis and the other on "
      "weight basis. Solid materials are measured in terms of either weight per unit time or mass "
      "per unit time. Very rarely solid quantity is measured in terms of volume. Liquids are "
      "measured either in volume rate or in weight rate. Gases are normally measured in volume rate.")
    P("Chất lỏng được phân thành hai loại: không nén được và nén được. Chất ở pha lỏng không nén "
      "được, còn chất ở pha khí thì nén được. Chất lỏng chiếm cùng một thể tích ở các áp suất "
      "khác nhau, trong khi chất khí chiếm thể tích khác nhau ở các áp suất khác nhau. Điều này "
      "phải được lưu ý khi hiệu chuẩn đồng hồ lưu lượng. Các phép đo ở điều kiện thực tế cần "
      "được quy đổi về nhiệt độ và áp suất chuẩn — STP (0°C và 760 mm Hg) — hoặc về nhiệt độ và "
      "áp suất danh nghĩa — NTP (20°C và 760 mm Hg).",
      "Fluids are classified into two types, namely incompressible and compressible. Fluids in "
      "liquid phase are incompressible whereas fluids in gaseous phase are compressible. Liquid "
      "occupies the same volume at different pressures whereas gases occupy different volumes at "
      "different pressures. This point has to be taken care of while calibrating the flow meters. "
      "The measurements taken at actual conditions should be converted either to Standard "
      "temperature (0°C) and pressure (760 mm Hg) base (STP base) or to Normal temperature (20°C) "
      "and pressure (760 mm Hg) base (NTP base).")
    P("Lưu lượng liên quan đến chuyển động của chất lỏng hoặc chất khí qua một loại kênh dẫn "
      "hoặc đường ống. Bên cạnh việc đo tốc độ chuyển động, lưu lượng thường còn gồm phân tích "
      "lượng năng lượng hoặc công được tạo ra khi chất chuyển động về phía trước. Đo lưu lượng "
      "giúp xác định mức độ hiệu quả của các hệ thống trong việc điều khiển dòng chảy của một "
      "chất qua một kênh hoặc hệ thống nhất định.",
      "A flow rate has to do with the movement of a liquid or gas through some type of channel or "
      "pipe. Along with measuring the speed of the movement, flow rates often include analysis of "
      "the amount of energy or work that is created as the substance moves forward. Measuring "
      "flow rates can aid in determining how effective different systems are in terms of "
      "controlling the flow of a substance through a given channel or system.")
    P("Lưu lượng nước quan trọng trong nhiều môi trường. Hệ thống nước đô thị dùng phép đo này "
      "để bảo đảm các bơm đẩy nước qua mạng kênh dẫn duy trì áp suất lưu lượng ở mức chấp nhận "
      "được. Đến lượt nó, điều này bảo đảm mỗi điểm nối trên hệ thống nhận được dòng chảy ổn "
      "định, đủ dùng nhưng không quá cao gây mòn và hư hỏng quá mức trong ống hay tại các điểm "
      "phân phối nước. Việc kiểm tra định kỳ lưu lượng tại các điểm chiến lược cho phép điều "
      "chỉnh thiết bị duy trì dòng chảy khi cần.",
      "Water flow rates are important in many settings. Municipal water systems utilize "
      "measurements of this type to make sure the pumps that move water through the network of "
      "channels are maintaining an acceptable level of flow rate pressure. This in turn helps to "
      "ensure that each connection along the system receives a steady flow that is adequate but "
      "not so high that excess wear and tear occurs within the pipes of the channel or at the "
      "various points where the water is dispersed. By routinely checking the flow rates at "
      "strategic points along the system, it is possible to adjust the equipment used to "
      "maintain the flow when and as needed.")
    P("Lưu lượng khí hoặc không khí cũng quan trọng trong nhiều môi trường, kể cả nhà máy sản "
      "xuất. Bằng cách điều khiển dòng khí nén đi qua hệ thống, có thể giữ áp suất ở mức cho "
      "phép công nhân dùng ống hơi để vệ sinh máy móc sản xuất. Điều này cũng đúng với hệ thống "
      "dùng một loại khí tự nhiên làm nhiên liệu. Điều chỉnh lưu lượng không khí cho các thiết "
      "bị đó không chỉ bảo đảm thiết bị chạy hiệu quả mà còn giúp công nhân sử dụng an toàn.",
      "Gas or air flow rates are also important in a number of settings, including manufacturing "
      "plants. By controlling the flow of pressurized air through a system, it is possible to "
      "maintain that pressure at a level that allows workers to use air hoses in cleaning "
      "production machinery. The same is true with systems that utilize some type of natural gas "
      "as a type of fuel. Regulating the air flow rates for those devices not only ensures the "
      "equipment works efficiently, but also that workers can use the equipment safely.")
    P("Bơm chữa cháy là một ví dụ khác về thiết bị mà việc đo lưu lượng rất quan trọng. Duy trì "
      "đúng áp suất dòng chảy quan trọng cho việc cung cấp một dòng nước hiệu quả để dập tòa "
      "nhà đang cháy hoặc tình huống tương tự. Nếu áp suất nước giảm dưới mức chấp nhận được, "
      "dòng nước sẽ yếu đi và lính cứu hỏa có thể phải tiến lại gần đám cháy hơn. Điều này lại "
      "đặt người đang dập lửa vào tình huống rủi ro hơn và có thể dẫn đến tổn thất thêm tính mạng.",
      "Fire pumps are another example of equipment where measuring flow rates is very important. "
      "Maintaining the right flow pressure is important to the task of supplying an efficient "
      "stream of water to deal with a burning building or similar situation. Should the water "
      "pressure fall below acceptable levels, the stream of water will not be as strong, and fire "
      "fighters may have to move closer to the blaze. This in turn places the individuals "
      "attempting to extinguish the fire at greater risk and could lead to additional loss of life.")
    P("Lưu lượng không phải lúc nào cũng được điều khiển bằng bơm và thiết bị. Trong một số ứng "
      "dụng, ý tưởng là quan sát dòng chảy tự nhiên của nước trong một môi trường nhất định. Ví "
      "dụ, các chuyên gia nông nghiệp quan sát lưu lượng nước ngầm khi nó di chuyển giữa các "
      "tầng đất khác nhau để xác định tốc độ thấm hút của các hợp phần đất. Thông tin này có giá "
      "trị vì giúp xác định đất có khả năng nuôi dưỡng các loại thực vật khác nhau hay không, "
      "xét theo khả năng giữ độ ẩm cần thiết để nuôi cây.",
      "Flow rates are not always controlled with the use of pumps and equipment. In some "
      "applications, the idea is to observe the natural flow of water within a given setting. For "
      "example, agricultural experts will observe the flow rate of ground water as it moves "
      "between different soil levels as a means of determining the rate of absorption by "
      "different types of soil compounds. This information is valuable, in that it aids in "
      "determining if the soil is capable of sustaining various types of plant life, in terms of "
      "the ability of the soil to maintain the moisture needed to nourish the plants.")

    # ---------------------------------------------------------------- 5.2
    H("5.2 Khái niệm cơ bản về đo lưu lượng", "5.2 Basic Concept of Flow Measurement")
    P("Đo lưu lượng là thực hành xác định lượng vật chất chảy qua một hệ thống nhất định, thường "
      "là đường ống hoặc ống dẫn. Điều này thường được thực hiện bằng đồng hồ lưu lượng lắp "
      "trực tiếp trong đường ống. Đo lưu lượng được dùng rộng rãi từ nhà máy hóa chất đến hệ "
      "thống điều hòa không khí thương mại. Loại đồng hồ cần dùng cho một ứng dụng cụ thể phụ "
      "thuộc vào tính chất của chất được đo.",
      "Flow measurement is the practice of determining the amount of material flowing through a "
      "specified system, usually a pipe or duct. This typically is accomplished with an inline "
      "flow meter. Flow measurement is used extensively in applications ranging from chemical "
      "plants to commercial air conditioning systems. The type of flow meter required for any "
      "particular application will depend on the properties of the measured substance.")
    P("Lĩnh vực đo lưu lượng vô cùng đa dạng và sâu rộng, là một trong những chủ đề trung tâm của "
      "nghiên cứu hiện tượng vận chuyển. Đo lưu lượng của một chất có thể đơn giản như đo sự "
      "thay đổi mức của một bình công đoạn, hoặc phức tạp như đo điện áp cảm ứng qua một chất "
      "lỏng dẫn điện chuyển động trong từ trường. Dù đo lưu lượng thường nói về vật chất trong "
      "ống hoặc ống dẫn, nó cũng có thể chỉ dòng chảy của chất rắn hoặc dòng vật chất đi qua "
      "các hệ thống như mạng lưới giao thông hay lòng sông.",
      "The field of flow measurement is incredibly diverse and far-reaching, and it is one of the "
      "central subjects of transport phenomena studies. Measuring the flow rate of a substance "
      "can be as simple as measuring the change in level of a process tank or as complicated as "
      "measuring the inducted voltage across a conductive fluid moving in a magnetic field. "
      "Although flow measurement usually refers to material in pipes or ducts, it also can refer "
      "to the flow of solids or the flow of material through systems such as traffic grids or "
      "riverbeds.")
    P("Đo trực tiếp lưu lượng của khí hoặc chất lỏng đòi hỏi dùng đồng hồ lưu lượng. Có nhiều "
      "loại đồng hồ lưu lượng, gồm đồng hồ tấm lỗ, đồng hồ tuabin, đồng hồ Venturi, đồng hồ "
      "siêu âm và đồng hồ điện từ, chỉ kể một vài loại. Trong hầu hết các ngành công nghiệp "
      "chế biến hóa chất, đồng hồ tấm lỗ là loại phổ biến nhất nhờ cấu tạo đơn giản và chi phí "
      "thấp.",
      "Directly measuring the flow rate of a gas or liquid requires the use of a flow meter. "
      "There are many types of flow meters, including orifice meters, turbine meters, Venturi "
      "meters, ultrasonic meters and electromagnetic flow meters, to name a few. In most chemical "
      "process industries, orifice meters are the most popular type of flow meters because of "
      "their simplicity and low cost.")
    P("Đồng hồ tấm lỗ và đồng hồ Venturi hoạt động theo nguyên lý Bernoulli, hay cụ thể hơn là "
      "mối quan hệ giữa lưu lượng của vật chất và độ sụt áp mà vật chất chịu qua đồng hồ. Đồng hồ "
      "tuabin liên hệ số vòng quay của một tuabin bên trong trong một khoảng thời gian nhất định "
      "với dòng chất lỏng đi qua cánh. Đồng hồ điện từ dùng định luật Faraday để liên hệ vận tốc "
      "chất lỏng với điện áp cảm ứng trên từ trường trong chất lỏng.",
      "Orifice meters and Venturi meters operate on Bernoulli's principle, or more specifically, "
      "the relationship between the flow rate of the material and the pressure drop that the "
      "material experiences across the meter. Turbine meters correlate the number of rotations "
      "that an internal turbine makes in a set amount of time to the flow of the fluid passing "
      "over the blades. Electromagnetic flow meters utilize Faraday's law to correlate fluid "
      "velocity with induced voltage over a magnetic field in the fluid.")
    P("Tất cả các phương pháp đo lưu lượng này đều có thể bị hạn chế, tùy vào bản chất của chất "
      "đo. Ví dụ, đồng hồ điện từ chỉ làm việc với chất lỏng dẫn điện. Đồng hồ có bộ phận chuyển "
      "động, như đồng hồ tuabin, không được khuyến nghị cho vật liệu mài mòn hoặc ăn mòn. Hệ "
      "thống bất thường có thể cần đồng hồ và phép tính đặc biệt hoặc lai.",
      "All of these methods of flow measurement might be subject to limitations, depending on "
      "the nature of the measured fluid. For example, an electromagnetic flow meter will work "
      "only on an electrically conductive fluid. Meters that have moving parts, such as turbine "
      "meters, are not recommended for abrasive or corrosive materials. Unusual systems might "
      "require unique or hybrid flow meters and calculations.")
    P("Kết quả đo lưu lượng có thể được cải thiện bằng các hệ số hiệu chỉnh hoặc bù. Các hệ số "
      "này thường dùng để bù cho nhiệt độ, áp suất và khối lượng phân tử khác biệt đáng kể so "
      "với thiết kế cơ sở của dòng chất lỏng. Hệ số bù thường được áp dụng trong các phép tính "
      "của hệ thống điều khiển phân tán (DCS) trong môi trường công nghiệp hóa chất.",
      "Calculated flow measurements can be improved with the use of correction or compensation "
      "factors. These factors are often used to compensate for temperatures, pressures and "
      "molecular weights that differ significantly from the design basis of the fluid flow. "
      "Compensation factors are often applied in the calculations of the distributed control "
      "system (DCS) in a chemical process setting.")

    # ------------------------------------------------ 5.2.1 Units of Flow
    H("5.2.1 Đơn vị lưu lượng", "Units of Flow", h3)
    P("Đơn vị dùng để mô tả lưu lượng có thể thuộc nhiều loại, tùy vào cách mà quy trình cụ thể "
      "cần thông tin.",
      "The units used to describe the flow measured can be of several types depending on how the "
      "specific process needs the information.")
    U(["Chất rắn: thường biểu thị theo lưu lượng trọng lượng như tấn/giờ, kg/phút, v.v.",
       "Chất lỏng: biểu thị cả theo lưu lượng trọng lượng lẫn lưu lượng thể tích. Ví dụ: "
       "tấn/giờ, kg/phút, lít/giờ, lít/phút, m3/giờ, v.v.",
       "Chất khí: biểu thị theo lưu lượng thể tích ở NTP hoặc STP, như Std m3/giờ, Nm3/giờ, v.v.",
       "Hơi nước: biểu thị theo lưu lượng trọng lượng như tấn/giờ, kg/phút, v.v."],
      ["Solids: Normally expressed in weight rate like Tonnes/hour, Kg/minute etc.",
       "Liquids: Expressed both in weight rate and in volume rate. Examples: Tonnes/hour, "
       "Kg/minute, litres/hour, litres/minute, m3/hour etc.",
       "Gases: Expressed in volume rate at NTP or STP like Std m3/hour, Nm3/hour etc.",
       "Steam: Expressed in weight rate like Tonnes/hour, Kg/minutes etc."])
    P("Mật độ hơi nước ở các nhiệt độ và áp suất khác nhau thì thay đổi. Vì vậy phép đo được "
      "quy đổi thành lưu lượng trọng lượng của nước dùng để tạo ra hơi nước tại điểm đo.",
      "Steam density at different temperatures and pressures vary. Hence the measurement is "
      "converted into weight rate of water which is used to produce steam at the point of measurement.")

    # ------------------------------------------------ 5.2.2 Turbulent Flow
    H("5.2.2 Dòng chảy rối", "Turbulent Flow", h3)
    P("Dòng chảy rối là loại dòng chảy của chất lỏng (khí hoặc lỏng) trong đó chất lỏng chịu "
      "những dao động hoặc trộn lẫn không đều, trái ngược với dòng chảy tầng, nơi chất lỏng "
      "chuyển động theo những đường đi hay lớp êm ái. Trong dòng rối, tốc độ của chất lỏng tại "
      "một điểm liên tục thay đổi cả về độ lớn lẫn hướng. Dòng gió và sông nói chung là rối "
      "theo nghĩa này, dù dòng chảy nhẹ nhàng. Không khí hoặc nước xoáy và tạo xoáy cục bộ "
      "trong khi toàn bộ khối chuyển động theo một hướng nhất định.",
      "Turbulent flow is a type of fluid (gas or liquid) flow in which the fluid undergoes "
      "irregular fluctuations, or mixing, in contrast to laminar flow, in which the fluid moves "
      "in smooth paths or layers. In turbulent flow the speed of the fluid at a point is "
      "continuously undergoing changes in both magnitude and direction. The flow of wind and "
      "rivers is generally turbulent in this sense, even if the currents are gentle. The air or "
      "water swirls and eddies while its overall bulk moves along a specific direction.")
    P("Hầu hết các loại dòng chảy chất lỏng đều là rối, ngoại trừ dòng tầng ở mép trước của vật "
      "rắn chuyển động tương đối so với chất lỏng, hoặc rất gần bề mặt rắn như thành trong của "
      "đường ống, hoặc trong trường hợp chất lỏng có độ nhớt cao chảy chậm qua kênh nhỏ. Các "
      "ví dụ thường gặp gồm dòng máu trong động mạch, vận chuyển dầu qua đường ống, dòng dung "
      "nham, dòng khí quyển và dòng hải dương, dòng chảy qua bơm và tuabin, cùng dòng chảy ở "
      "đuôi thuyền và quanh đầu cánh máy bay.",
      "Most kinds of fluid flow are turbulent, except for laminar flow at the leading edge of "
      "solids moving relative to fluids or extremely close to solid surfaces, such as the inside "
      "wall of a pipe, or in cases of fluids of high viscosity (relatively great sluggishness) "
      "flowing slowly through small channels. Common examples of turbulent flow are blood flow in "
      "arteries, oil transport in pipelines, lava flow, atmosphere and ocean currents, the flow "
      "through pumps and turbines, and the flow in boat wakes and around aircraft-wing tips.")
    P("Dòng chảy rối là hệ thống dòng chảy đặc trưng bởi những thay đổi tính chất không có trật "
      "tự. Nó có thể gồm bất kỳ đặc điểm nào sau đây:",
      "Turbulent flow is a type of flow system characterized by disorganized property changes. "
      "This can include any of the following:")
    U(["Đối lưu động lượng cao", "Khuếch tán động lượng thấp",
       "Biến đổi nhanh vận tốc và áp suất"],
      ["High momentum convection", "Low momentum diffusion",
       "Quick velocity and pressure variation"])
    P("Sự gia tăng dòng chảy rối thường do các hố rỗ và các kiểu hình học khác nhanh chóng dẫn "
      "đến tốc độ ăn mòn cao hơn, cuối cùng phát triển thành rò rỉ. Sự hiện diện của độ rối tăng "
      "lên báo hiệu sự xói mòn sắp xảy ra. Vì thế, các ngành công nghiệp, đặc biệt là những "
      "ngành liên quan đến hệ thống đường ống và máy móc, phải loại trừ được nguy cơ hư hỏng "
      "liên quan đến dòng chảy rối.",
      "An increase in turbulent flow is usually caused by pitting and other patterns that rapidly "
      "lead to elevated corrosion rates that eventually develop into leaks. The presence of "
      "increased turbulence signifies impending erosion. Thus, it is vital that industries, "
      "especially those that deal with piping systems and machinery, must be able to rule out "
      "the risk of damage associated with turbulent flow.")
    P("Độ rối có các đặc điểm sau:", "Turbulence has the following features:")
    U(["Nguồn năng lượng liên tục, vì độ rối tiêu hao rất nhanh",
       "Dòng chảy không đều hoặc hỗn loạn, cần được xử lý thống kê",
       "Độ khuếch tán tăng hoặc trộn lẫn nhanh chất lỏng, làm tăng vận chuyển khối lượng, "
       "năng lượng và động lượng"],
      ["Consistent energy source, since turbulence dissipates quickly",
       "Irregular or chaotic flows, which should be treated statistically",
       "Increased diffusivity or fast mixing of fluids responsible for improved mass rate, "
       "energy and momentum"])
    P("Khi độ rối tăng lên, hư hỏng có thể xảy ra. Ăn mòn xói mòn là sản phẩm của môi trường hóa "
      "học khắc nghiệt và bề mặt có vận tốc chất lỏng cao. Như vậy, hư hỏng có thể là kết quả "
      "của dòng chất lỏng chảy nhanh vào một vật đứng yên như van dầu và ống, hoặc trong một số "
      "trường hợp là tác động nhanh của một vật vào chất lỏng không chuyển động, như chân vịt "
      "khuấy nước. Bề mặt bị ăn mòn xói mòn do dòng rối thường sạch, khác với bề mặt bị các loại "
      "ăn mòn khác. Ăn mòn xói mòn liên quan chặt chẽ đến dòng chảy rối và thường thấy trong "
      "môi trường công nghiệp nơi dòng rối được dùng để duy trì dòng chất lỏng.",
      "When there is increased turbulent flow, damage may follow. Erosion corrosion is a product "
      "of a harsh chemical environment and surfaces with high fluid velocities. Thus, the damage "
      "can be an outcome of rapid flow of fluid on a motionless object like oil valves and pipes. "
      "In some cases, corrosion results from the rapid action of a particular object to "
      "non-moving fluid, like when propellers churn water. Surfaces that have gone through "
      "erosion corrosion caused by high turbulence flow are typically clean, unlike with "
      "surfaces affected by other corrosion types. Erosion corrosion is closely related to "
      "turbulent flow and is usually found in industrial settings involving turbulent flow to "
      "maintain flow of fluids.")
    P("Ăn mòn xói mòn do dòng chảy rối nhanh có thể được ngăn ngừa bằng hợp kim cứng hơn, chẳng "
      "hạn lớp phủ hàn hoặc lớp phủ phun ngọn lửa. Bảo vệ đầy đủ khỏi tác động của dòng chảy rối "
      "cực cao là rất quan trọng cho hoạt động hiệu quả.",
      "Erosion corrosion caused by rapid turbulent flow can be prevented using harder alloys, "
      "such as welded facings or those that are flame sprayed. Ample protection against the "
      "effects of extremely high turbulent flow is crucial in efficient operations.")

    # ------------------------------------------------ 5.2.3 Discharge Coeff.
    H("5.2.3 Hệ số lưu lượng Cd", "Discharge Coefficient (Cd)", h3)
    P("Hệ số lưu lượng là tỷ số giữa lưu lượng thực tế qua một vòi phun hoặc lỗ và lưu lượng "
      "lý thuyết. Thường gọi là hệ số xả, nó liên quan đến dòng chảy và tổn thất áp suất qua "
      "vòi phun và lỗ trong hệ thống chất lỏng hoặc cơ học chất lỏng. Ký hiệu là “Cd” và là một "
      "số không thứ nguyên.",
      "Discharge Coefficient is the ratio of actual discharge through a nozzle or orifice to the "
      "theoretical discharge. Commonly known as coefficient of discharge, it is related to the "
      "flow and pressure loss through nozzles and the orifices in the fluid systems or fluid "
      "mechanics. It is denoted by “Cd” and is a dimensionless number.")
    P("Trong cơ học chất lỏng, hệ số xả là tỷ số giữa lưu lượng khối tại đầu ra của vòi phun và "
      "lưu lượng của vòi phun lý tưởng trong điều kiện dòng chảy lý tưởng.",
      "In fluid mechanics, coefficient of discharge is the ratio of mass flow rate at the "
      "nozzle's discharge end to that of the ideal nozzle working in ideal flow conditions.")
    P("Hệ số xả C được định nghĩa là tỷ số giữa lưu lượng thể tích thực tế và lưu lượng thể tích "
      "lý tưởng.", "Discharge coefficient, C is defined as the ratio between actual volumetric "
      "flow rate and ideal volumetric flow rate.")
    EQ("C = q<sub>actual</sub> / q<sub>ideal</sub>")
    U(["q<sub>actual</sub> = lưu lượng thể tích thực tế",
       "q<sub>ideal</sub> = lưu lượng thể tích lý thuyết"],
      ["q<sub>actual</sub> = Actual volumetric flow rate",
       "q<sub>ideal</sub> = Ideal volumetric flow rate. (Theoretical)"])

    # ------------------------------------------------ 5.2.4 Flow Coeff K
    H("5.2.4 Hệ số dòng chảy K", "Flow Coefficient (K)", h3)
    P("Hệ số dòng chảy, hay hệ số lưu lượng, là thước đo tương đối mức độ cho chất lỏng đi qua "
      "một thiết bị. Phép đo được thực hiện cho một độ mở xác định với độ sụt áp 1 p.s.i. Cũng "
      "có thể định nghĩa nó là lượng nước chảy qua một van trong một phút. Hệ số dòng chảy cung "
      "cấp quy tắc chung hay tiêu chuẩn để so sánh năng lực của các van khác nhau hoặc việc "
      "chọn kích cỡ van.",
      "Flow Coefficient or coefficient of flow is the relative measure of allowing a fluid "
      "through a device. It is done for a specified opening with a pressure drop of 1 p.s.i. We "
      "can also define it as the amount of water that flows through a valve in one minute. The "
      "flow coefficient provides the general rule or a standard to compare the capacities of "
      "different valves or sizing of valves.")
    EQ("K = C<sub>d</sub> / √(1 − β<sup>4</sup>) = C<sub>d</sub> · M<sub>va</sub>,"
       "  M<sub>va</sub> = 1 / √(1 − β<sup>4</sup>)", "(2)")
    U(["K = hệ số dòng chảy",
       "C<sub>d</sub> = hệ số lưu lượng",
       "β = tỷ số đường kính = d/D",
       "M<sub>va</sub> = hệ số tiến tốc độ (velocity approach factor)"],
      ["K = Flow coefficient",
       "Cd = discharge coefficient",
       "β = ratio of diameters = d/D",
       "Mva = velocity approach factor"])
    FIG(1, F.fig_f01())
    P("Đo lưu lượng chất lỏng bằng tấm lỗ và áp kế chênh áp như Hình 1 đòi hỏi phải tính đến "
      "ảnh hưởng của chất lỏng lên chất lỏng trong áp kế. Hơn nữa, chênh áp tại tấm lỗ thường "
      "được biểu thị bằng chiều cao cột chất lỏng.",
      "Measuring fluid flow with an orifice and differential pressure manometer as shown in "
      "figure 1, requires that the effect of the fluid over the manometer liquid be taken into "
      "account. Furthermore, the pressure differential at the orifice is usually expressed in "
      "liquid-column height.")
    EQ("Q = K · A · √(2 g h (ρ<sub>m</sub> − ρ<sub>f</sub>) / ρ<sub>f</sub>)", "(2)")
    U(["h = chênh áp tại chỗ thu hẹp, tính theo chiều cao cột chất lỏng",
       "ρ<sub>m</sub> = trọng lượng riêng của chất lỏng trong áp kế",
       "ρ<sub>f</sub> = trọng lượng riêng của chất lỏng phía trên chất lỏng áp kế"],
      ["h = differential at restriction, liquid column height",
       "mρ m = weight density of manometer fluid",
       "fρ = weight density of fluid over the manometer fluid"])
    P("Cuối cùng, nếu lưu lượng cần được quy về nhiệt độ phòng điều khiển, nơi mật độ chất lỏng "
      "là ρ<sub>s</sub>, thì từ phương trình (1) và (2):",
      "Finally if the flow rate is to be converted at the control room temperature at which the "
      "fluid density is sρ, then from equations (1) and (2).")
    EQ("Q<sub>s</sub> = Q · √(ρ<sub>f</sub> / ρ<sub>s</sub>)")
    b.append(formula_notes(lang))

    # ---------------------------------------------------------------- 5.3
    H("5.3 Đồng hồ đo lưu lượng chênh áp", "5.3 Differential Pressure Meter")
    P("Đồng hồ lưu lượng chênh áp, còn gọi là đồng hồ DP, tạo ra sự thay đổi tiết diện ngang "
      "trong ống dẫn, làm vận tốc của chất lỏng thay đổi. Sự thay đổi vận tốc xảy ra bất cứ khi "
      "nào có thay đổi tiết diện dòng chảy; nghĩa là khi vận tốc giảm thì áp suất tăng. Đồng hồ "
      "chênh áp có thể dùng làm đồng hồ lưu lượng chất lỏng hoặc chất khí; tuy nhiên, một đồng "
      "hồ đơn không thể được cấu hình để đo cả hai pha lỏng và khí.",
      "Differential pressure flow meters, also known as DP flow meters, create a cross sectional "
      "change in the flow tube, which causes the velocity of the flowing fluid to change. A change "
      "in velocity occurs whenever there is a change in flow cross-section; i.e., with a decrease "
      "in velocity, an increase in pressure occurs. Differential pressure flow meters can be used "
      "as liquid flow meters or gas flow meters; however, a single flow meter may not be "
      "configured to measure both liquid and gas phases.")
    EQ("Q = A · V<sub>avg</sub>;  "
       "P<sub>1</sub>/(ρ g) + V<sub>1</sub><sup>2</sup>/(2 g) + z<sub>1</sub> = "
       "P<sub>2</sub>/(ρ g) + V<sub>2</sub><sup>2</sup>/(2 g) + z<sub>2</sub>")
    U(["Q = lưu lượng thể tích",
       "A = diện tích tiết diện ngang dòng chảy",
       "V = mật độ chất lỏng ở nhiệt độ và áp suất công đoạn",
       "V<sub>avg</sub> = vận tốc trung bình của chất lỏng; P = áp suất tĩnh",
       "ρ = mật độ chất lỏng",
       "g = gia tốc do trọng lực",
       "z = độ cao cột chất lỏng tính từ một mốc tham chiếu"],
      ["Q = the volumetric flow rate",
       "A = flow in the cross sectional area",
       "V = fluid density at the process temperature and pressure",
       "Vavg = the average fluid velocity P = static pressure",
       "ρ = fluid density",
       "g = acceleration due to gravity",
       "z = elevation on head of the fluid from a reference datum"])
    P("<b>Lưu ý:</b> Trong hai phương trình trên, Q và V<sub>avg</sub> là các ẩn số. Khi tìm "
      "được V<sub>avg</sub>, có thể suy ra lưu lượng thể tích Q.",
      "<b>Note:</b> In these two equations Q and Vavg are unknowns. Upon finding Vavg, the "
      "volumetric flow rate Q can be obtained.")

    # --------------------------------------------- 5.3.1 Orifice Plate
    H("5.3.1 Tấm lỗ", "Orifice Plate", h3)
    P("Đồng hồ tấm lỗ là thiết bị đo lưu lượng dạng cột áp phổ biến nhất. Một tấm lỗ được đặt "
      "trong đường ống và chênh áp qua nó được đo.",
      "An Orifice flow meter is the most common head type flow measuring device. An orifice plate "
      "is inserted in the pipeline and the differential pressure across it is measured.")
    P("Đây là thiết bị đo lưu lượng chất lỏng trong ống. Tấm lỗ thường là tấm kim loại tròn có "
      "một lỗ ở giữa. Bản thân tấm thường được kẹp giữa hai đầu của hai ống có mặt bích trên hệ "
      "thống cần đo lưu lượng.",
      "It is a device that measures the flow rate of fluid in a pipe. Orifice plates typically "
      "are round metal plates with a hole in the middle. The plate itself is usually sandwiched "
      "between the ends of two flanged pipes on the system in which flow is to be measured.")
    P("Tấm lỗ có thể làm từ nhiều vật liệu khác nhau, tùy vào chất lỏng được đo. Thép carbon "
      "thường dùng cho hydrocarbon; thép không gỉ chủ yếu dùng cho chất lỏng ăn mòn hơn. Tương "
      "thích hóa học rất quan trọng vì ăn mòn có thể ảnh hưởng xấu đến hiệu năng.",
      "Orifice plates can be made of several different materials, and the material of "
      "construction will depend on the fluid being measured. Carbon steel is commonly used for "
      "hydrocarbons. Stainless steel is used mainly for more corrosive fluids. Chemical "
      "compatibility is important because corrosion can negatively impact performance.")
    P("Lỗ hay cổng của tấm lỗ thường có một mặt sắc và một mặt vát. Mặt sắc phải đặt ở phía đầu "
      "vào của ống, mặt vát ở phía đầu ra. Tấm lỗ phải được lắp đúng chiều vì hình học của mặt "
      "đóng vai trò lớn trong cách chất lỏng đi qua lỗ.",
      "The hole, or bore, in an orifice plate usually has a sharp side and a beveled side. The "
      "sharp side of the plate should be on the inlet side of the pipe. The beveled side is on "
      "the outlet side of the pipe. The orifice plate must be installed in the proper direction; "
      "the side geometry plays a large role in how the fluid passes through the orifice.")
    P("Tấm lỗ đo lưu lượng bằng cách liên hệ áp suất và vận tốc của chất lỏng ở phía vào và phía "
      "ra. Chất lỏng phía vào bị ép đi qua cổng. Ngay sau khi qua lỗ, chất lỏng đạt điểm hội tụ "
      "cực đại gọi là vena contracta. Tại đây vận tốc và áp suất khác với ở phía vào của ống. "
      "Sự khác biệt về áp suất và vận tốc được dùng để tính lưu lượng theo nguyên lý Bernoulli.",
      "An orifice plate measures flow by relating the pressures and velocities of the fluid at "
      "the inlet and outlet sides of the plate. The fluid on the inlet side is forced to pass "
      "through the orifice bore. Shortly after passing through the orifice, the fluid reaches a "
      "point of maximum convergence, known as the venacontracta. At this point, the velocity and "
      "the pressure of the fluid are different from what they were in the inlet side of the pipe. "
      "The differences in the pressure and velocity are used to calculate the flow rate through "
      "Bernoulli's principle.")
    P("Để đo chênh áp, các ống nhỏ — đôi khi gọi là “chân” — được lắp ở phía vào và phía ra của "
      "tấm và nối với đồng hồ chênh áp. Các ống này phải sạch sẽ, không có mảnh vụn hay chất "
      "lỏng nặng đọng lại. Vật liệu khác với chất lỏng được đo trong các ống chân sẽ làm giảm "
      "độ chính xác của phép đo chênh áp.",
      "To measure the differential pressure, small pipes - sometimes known as “legs” - are "
      "installed on the inlet and outlet sides of the plate and are connected to a differential "
      "pressure meter. These pipes must be free of debris or heavy fluid buildup. Material other "
      "than the fluid being measured in the pipe legs will hurt the accuracy of the differential "
      "pressure measurement.")
    P("Tấm lỗ thường được dùng trong đo lưu lượng chất lỏng vì tương đối rẻ, dễ lắp, dễ bảo trì "
      "và được hiểu rõ trong công nghiệp chế biến hóa chất. Tấm lỗ không có bộ phận chuyển động "
      "cần bảo trì. Độ chính xác điển hình của đồng hồ tấm lỗ vào khoảng 90-95%. Một nhược điểm "
      "là chúng có thể gây sụt áp vĩnh viễn lớn trong hệ thống đường ống.",
      "Orifice plates are commonly used for fluid flow measurements because they are relatively "
      "cheap, easy to install, easy to maintain and well understood in the chemical processing "
      "industry. Orifice plates do not have moving parts to maintain. The typical accuracy of an "
      "orifice meter can be expected to range from 90-95 %. One of the downsides of orifice meters "
      "is that they can introduce large permanent pressure drops in a piping system.")

    H("Nguyên lý hoạt động", "Principle of Operation", h4)
    P("Tấm lỗ đặt trong đường ống làm tăng vận tốc dòng chảy và giảm áp suất tương ứng. Kiểu "
      "dòng chảy cho thấy tiết diện ngang giảm hiệu quả sau tấm lỗ, với vận tốc cực đại và áp "
      "suất cực tiểu tại vena contracta.",
      "The orifice plate inserted in the pipeline causes an increase in flow velocity and a "
      "corresponding decrease in pressure. The flow pattern shows an effective decrease in cross "
      "section beyond the orifice plate, with a maximum velocity and minimum pressure at the "
      "venacontracta.")
    P("Kiểu dòng chảy và cạnh trước sắc của tấm lỗ tạo ra nó (Hình 2) có tầm quan trọng lớn. Cạnh "
      "sắc tạo ra tiếp xúc gần như thuần túy dạng đường giữa tấm và dòng chảy hiệu quả, với lực "
      "cản ma sát chất lỏng-kim loại không đáng kể tại ranh giới.",
      "The flow pattern and the sharp leading edge of the orifice plate (Figure 2) which produces "
      "it are of major importance. The sharp edge results in an almost pure line contact between "
      "the plate and the effective flow, with the negligible fluid-to-metal friction drag at the "
      "boundary.")
    FIG(2, F.fig_f02())
    P("Phương trình cơ bản được cho như sau:", "The basic equation are given as")
    EQ("W = K · A · ρ · √(2 g h)")
    U(["V = vận tốc chất lỏng", "Q = lưu lượng thể tích", "W = lưu lượng khối",
       "A = diện tích tiết diện ngang của ống",
       "h = chênh áp cột chất lỏng qua phần tử thu hẹp",
       "g = gia tốc do trọng lực", "ρ = mật độ chất lỏng đang chảy"],
      ["V= velocity of fluid", "Q= volume flow rate", "W= mass flow rate",
       "A= cross section area of pipe",
       "h= differential head pressure across the restriction element",
       "g= acceleration due to gravity", "ρ = density of flowing fluid"])
    EQ("K = C / √(1 − β<sup>4</sup>) = a constant")
    U(["C = hệ số lưu lượng",
       "β = d<sub>i</sub>/D = đường kính phần thu hẹp / đường kính ống"],
      ["Where C= discharge coefficient",
       "di d diameter ratio D ameter of pipeβ = = ="])

    H("Các loại tấm lỗ", "Types of Orifice Plates", h4)
    P("Dạng đơn giản nhất của tấm lỗ là một tấm kim loại mỏng có lỗ tròn cạnh vuông, cạnh sắc "
      "hoặc cạnh tròn.",
      "The simplest form of orifice plate consists of a thin metal sheet, having in it a square "
      "edged or a sharp edged or round edged circular hole.")
    P("Có ba loại tấm lỗ, gồm:", "There are three types of orifice plates namely")
    U(["Đồng tâm", "Lệch tâm", "Dạng đoạn"],
      ["Concentric", "Eccentric and", "Segmental type"])
    P("Hình 3 cho thấy hai góc nhìn khác nhau của ba loại tấm lỗ.",
      "Figure 3 shows two different views of the three types of Orifice plate")
    FIG(3, F.fig_f03())
    P("Loại đồng tâm dùng cho chất lỏng sạch. Khi đo chất bẩn, bùn và chất lỏng chứa chất rắn, "
      "dùng loại lệch tâm hoặc dạng đoạn sao cho cạnh dưới của lỗ trùng với đáy bên trong của "
      "ống. Điều này cho phép chất rắn đi qua không bị cản trở. Tấm lỗ được đặt vào đường ống "
      "chính giữa hai mặt bích kề nhau, đường kính ngoài của tấm được tiện để vừa trong các bulông "
      "mặt bích. Mặt bích được bắt vít hoặc hàn vào ống.",
      "The concentric type is used for clean fluids. In metering dirty fluids, slurries and fluids "
      "containing solids, eccentric or segmental type is used in such a way that its lower edge "
      "coincides with the inside bottom of the pipe. This allows the solids to flow through "
      "without any obstruction. The orifice plate is inserted into the main pipeline between "
      "adjacent flanges, the outside diameters of the plate being turned to fit within the flange "
      "bolts. The flanges are either screwed or welded to the pipes.")

    H("Đồng tâm", "Concentric", h4)
    P("Thiết kế đơn giản nhất là lỗ đồng tâm. Loại này được chế tạo bằng cách gia công một lỗ "
      "thẳng chính xác ở giữa một tấm kim loại mỏng. Nhìn từ mặt cắt thấy các cạnh sắc (góc 90°) "
      "tại lỗ. Nhãn chữ trên “cánh” của tấm lỗ thường xác định phía thượng lưu, nhưng với tấm lỗ "
      "cạnh vuông thì điều đó không quan trọng. Tấm cũng được làm từ vật liệu khác như nickel, "
      "monel, đồng phosphor, v.v. để chịu tác động ăn mòn của chất lỏng.",
      "The simplest design of orifice plate is the concentric orifice. This type of orifice plate "
      "is manufactured by machining a precise, straight hole in the middle of a thin metal plate. "
      "Looking at a side view of a concentric orifice plate reveals sharp edges (90° corners) at "
      "the hole. A text label printed on the “paddle” of any orifice plate customarily identifies "
      "the upstream side of that plate, but in the case of the square-edged orifice plate it does "
      "not matter. It is also made from other materials such as nickel, monel, phosphor bronze, "
      "etc. to withstand the corrosive effect of the fluid.")
    P("Chiều dày của tấm tại mép lỗ không được vượt quá bất kỳ giá trị nào sau đây: D/50; d/8; "
      "(D−d)/8. Trong đó d = đường kính trong của ống và D = đường kính lỗ hay cổng (định nghĩa "
      "này bị đảo so với mục Types of Orifice Plates và được giữ nguyên như bản in).",
      "The plate thickness at the orifice edge should not exceed any of the following: D/50; d/8; "
      "(D-d)/8. Where d = the pipe internal diameter, D = the orifice diameter or bore (a "
      "definition reversed relative to Types of Orifice Plates and kept as printed).")
    P("<b>Ứng dụng:</b> chủ yếu dùng cho chất lỏng đồng nhất sạch, chất khí và chất lỏng không nhớt.",
      "<b>Application:</b> Used primarily for clean homogeneous liquids, gases, non-viscous fluids.")

    H("Lệch tâm", "Eccentric", h4)
    P("Ở đây lỗ được đặt lệch tâm để các phần không mong muốn của chất lỏng đi qua lỗ thay vì đọng "
      "lại trên mặt thượng lưu. Với dòng khí, lỗ nên lệch xuống dưới để giọt lỏng hoặc hạt rắn dễ "
      "đi qua. Với dòng lỏng, lỗ nên lệch lên trên để bọt khí đi qua và lệch xuống dưới để chất "
      "rắn nặng đi qua. Cách khác là khoan một lỗ nhỏ gần mép tấm, ngang bằng đường kính trong "
      "của ống; nếu lỗ hướng lên để cho bọt hơi đi qua gọi là lỗ thông hơi (vent hole), nếu hướng "
      "xuống cho giọt lỏng hoặc chất rắn đi qua gọi là lỗ xả (drain hole).",
      "Here the hole is located off-center to allow the undesired portions of the fluid to pass "
      "through the orifice rather than build up on the upstream face. For gas flows, the hole "
      "should be offset downward, so any liquid droplets or solid particles may easily pass "
      "through. For liquid flows, the hole should be offset upward to allow gas bubbles to pass "
      "through and offset downward to allow heavy solids to pass through. An alternative to "
      "offsetting or re-shaping the bore hole of an orifice plate is to simply drill a small hole "
      "near the edge of the plate, flush with the inside diameter of the pipe, allowing undesired "
      "substances to pass through the plate rather than collect on the upstream side. If such a "
      "hole is oriented upward to pass vapor bubbles, it is called a vent hole. If the hole is "
      "oriented downward to pass liquid droplets or solids, it is called a drain hole.")
    P("<b>Ứng dụng:</b> dùng đo lưu lượng chất lỏng chứa chất rắn và bùn; cũng dùng cho hơi và "
      "khí có hiện tượng ngưng tụ.",
      "<b>Application:</b> Used for measurement of flow for fluids containing solids and slurries. "
      "It is also used for vapors and gases where condensation is present.")

    H("Dạng đoạn", "Segmental type", h4)
    P("Loại tấm lỗ lệch tâm thứ hai gọi là tấm lỗ dạng đoạn, trong đó lỗ không tròn mà chỉ là một "
      "đoạn của một đường tròn đồng tâm. Như thiết kế lệch tâm, lỗ dạng đoạn nên lệch xuống dưới "
      "trong ứng dụng dòng khí và lệch lên hoặc xuống trong ứng dụng dòng lỏng tùy loại vật liệu "
      "không mong muốn trong dòng chảy.",
      "The second off-center orifice plate type is called the segmental orifice plate, where the "
      "hole is not circular but rather just a segment of a concentric circle. As with the "
      "eccentric orifice plate design, the segmental hole should be offset downward in gas flow "
      "applications and either upward or downward in liquid flow applications depending on the "
      "type of undesired material(s) in the flow stream.")
    P("<b>Ứng dụng:</b> chủ yếu dùng cho bùn hoặc khí rất bẩn khi dòng chảy có thể chứa tạp chất "
      "nặng hơn chất lỏng.",
      "<b>Application:</b> This type is used primarily for slurries or extremely dirty gases where "
      "the flow may contain impurities heavier than the fluid.")

    H("Phương pháp gia công lỗ", "Machining Methods of Orifices", h4)
    P("Gia công tấm lỗ tùy thuộc vào mục đích sử dụng cụ thể. Ba loại trong Hình 4 giải thích các "
      "phương pháp gia công.",
      "Machining of the orifice plate depends on its specific use. Three types shown in figure 4 "
      "explains the machining methods.")
    FIG(4, F.fig_f04())
    P("Loại 1 và 2 rất thường dùng và F được gọi là the plater. Hai loại này dễ chế tạo và dễ "
      "tái tạo, trong khi loại 3 thì không. Chiều dày t được chọn để chịu được lực uốn cong. Loại "
      "1 còn giảm tổn thất áp suất. Loại 3, gọi là lỗ cạnh góc tư (quadrant edged orifice), dùng "
      "cho chất lỏng nhớt hơn khi cần hiệu chỉnh cho số Reynolds thấp và độ nhớt.",
      "Types 1 and 2 are very commonly used and F is known as the plater. These two are easier to "
      "manufacture and are easily reproducible while type 3 is not. Thickness t as chosen to "
      "withstand the buckling forces. Type 1 has also reduced pressure losses. Type 3, known as "
      "the quadrant edged orifice, is used for more viscous fluids where corrections for low "
      "Reynolds number and viscosity are necessary.")

    H("Vật liệu chọn cho tấm lỗ", "Materials Chosen For Orifices", h4)
    P("Vật liệu chọn cho tấm lỗ là bất kỳ vật liệu cứng nào không gỉ và không bị ăn mòn. Điều sống "
      "cốt là vật liệu không được ăn mòn trong chất lỏng được đo, nếu không mép lỗ sẽ hư hỏng đến "
      "mức cản trở đặc tính dòng chảy và độ chính xác của phép đo. Nên chọn vật liệu có hệ số giãn "
      "nở nhiệt đã biết. Các vật liệu thường dùng là thép không gỉ, Monel, đồng phosphor, thủy "
      "tinh, gốm, nhựa, đồng thau, đồng, nhôm và tantalum.",
      "The material chosen for orifice plate is of any rigid material of non-rusting and "
      "noncorrodible. It is vital that the material should not corrode in the fluid being "
      "metered. Otherwise the edge of the orifice will get damaged to a sufficient extend to "
      "interfere with the character of the flow and the accuracy of the measurement. We should "
      "choose a material whose coefficient of Thermal expansion is known. The common materials "
      "used are Stainless steel, Monel, Phosphor bronze, Glass, Ceramics, Plastics, Brass, Copper, "
      "Aluminium and Tantalum.")

    H("Vị trí các điểm lấy áp", "Position of Taps in Orifice", h4)
    P("Dòng chất lỏng tiếp tục co lại sau khi rời khỏi lỗ và có đường kính nhỏ nhất tại vena "
      "contracta. Vì thế áp suất chất lỏng tiếp tục giảm sau khi rời lỗ.",
      "The area of the fluid stream continues to contract after the stream has left the orifice "
      "and it has a minimum diameter at the venacontracta. The pressure of the fluid therefore "
      "continue to fall after leaving the orifice.")
    P("Có sự giảm nhẹ áp suất trong đoạn tiến đến lỗ và áp suất tĩnh đạt cực tiểu khoảng một đường "
      "kính ống trước tấm lỗ. Sau đó áp suất tăng gần mặt của tấm lỗ. Rồi có sự giảm đột ngột khi "
      "chất lỏng đi qua lỗ, nhưng áp suất cực tiểu chỉ đạt được khi tới vena contracta. Sau vena "
      "contracta, áp suất tĩnh phục hồi nhanh.",
      "There is a slight fall in pressure in the approach section and the static pressure is at a "
      "minimum about one pipe diameter before the orifice plate. The pressure of the fluid then "
      "rises near the face of the orifice. There is then a sudden fall of pressure as the fluid "
      "passes through the orifice, but the minimum pressure is not attained until the "
      "venacontracta is reached. Beyond the venacontracta, there is a rapid recovery in the "
      "static pressure.")
    P("Do ma sát và tiêu hao năng lượng trong độ rối, áp suất hạ lưu cực đại luôn nhỏ hơn áp suất "
      "thượng lưu. Tổn thất áp suất gây ra này phụ thuộc vào chênh áp và tăng khi tỷ số lỗ giảm "
      "đối với một lưu lượng nhất định.",
      "Owing to friction and dissipation of energy in turbulence, the maximum downstream pressure "
      "is always lesser than the upstream pressure. The pressure loss so caused depends upon the "
      "differential pressure and increases as the orifice ratio decreases for a given rate of flow.")
    P("Chênh áp thu được với tấm lỗ cũng phụ thuộc vào vị trí của các điểm lấy áp. Các điểm cần "
      "lưu ý khi bố trí điểm lấy áp là:",
      "The differential pressure obtained with an orifice plate will also depend upon the position "
      "of the pressure taps. The points to be observed while locating the taps are:")
    U(["Chúng ở cùng vị trí so với mặt phẳng của lỗ cho mọi kích cỡ ống.",
       "Điểm lấy áp được đặt ở vị trí mà độ dốc của đường cong áp suất là nhỏ nhất [OCR: “is at "
       "least”], để sai số nhỏ về vị trí điểm lấy áp ít ảnh hưởng đến giá trị áp suất quan sát "
       "[OCR: “effort”].",
       "Vị trí điểm lấy áp khi lắp đặt giống với vị trí dùng trong đánh giá các hệ số mà phép "
       "tính dựa trên đó."],
      ["They are in the same position relative to the plane of the orifice for all pipe sizes.",
       "The tap is located at a position for which the slope of the pressure profile is at least, "
       "so that slight errors in tap position will have less effort on the value of the observed "
       "pressure.",
       "The tap location in the installation is identical with that used in evaluation of the "
       "coefficients on which the calculation is based."])
    P("Hình 5 cho thấy vị trí các điểm lấy áp với tấm lỗ.",
      "Figure 5 shows the location of Pressure taps with Orifice plate.")
    FIG(5, F.fig_f05())
    P("Có năm vị trí thông thường cho các điểm lấy áp chênh áp:",
      "There are five common locations for the differential pressure taps:")
    U(["Điểm lấy áp mặt bích", "Điểm lấy áp vena contracta", "Điểm lấy áp bán kính",
       "Điểm lấy áp toàn dòng hay ống", "Điểm lấy áp góc"],
      ["Flange taps", "Venacontracta taps", "Radius taps",
       "Full flow or pipe taps", "Corner taps"])

    H("Điểm lấy áp mặt bích", "Flange taps", h4)
    P("Chủ yếu dùng cho kích cỡ ống từ 50 mm trở lên, đường tâm cách mặt tấm lỗ 25 mm. Không dùng "
      "được cho ống có đường kính dưới 35 mm vì vena contracta có thể ở gần tấm lỗ hơn 25 mm.",
      "They are predominantly used for pipe sizes 50 mm and larger and the centerlines are 25 mm "
      "from the orifice plate surface. They cannot be used for pipe size of less than 35 mm "
      "diameter. Since the venacontracta may be closer than 25 mm from the orifice plate.")
    H("Điểm lấy áp vena contracta", "Venacontracta taps", h4)
    P("Các điểm này dùng một điểm lấy áp thượng lưu cách tấm lỗ một đường kính ống và một điểm "
      "hạ lưu đặt tại điểm áp suất cực tiểu. Điểm lấy áp vena contracta thường giới hạn ở kích "
      "cỡ ống 150 mm hoặc lớn hơn, tùy vào cấp và kích thước mặt bích.",
      "These taps use an upstream tap located one pipe diameter upstream of the orifice plate, and "
      "a downstream tap located at the point of minimum pressure. Venacontracta taps normally "
      "limited to pipe size 150 mm or large depending upon the flange rating and dimensions.")
    H("Điểm lấy áp bán kính", "Radius taps", h4)
    P("Với d1 = D và d2 = 1/2 D, các điểm này tương tự điểm lấy áp vena contracta, chỉ khác là "
      "điểm hạ lưu đặt tại nửa đường kính ống. Chúng thường được coi là tốt hơn vì đơn giản hóa "
      "kích thước vị trí lấy áp và không thay đổi theo tỷ số β của tấm lỗ.",
      "Radius taps. d1 = D and d2 = 1/2 D. These are similar to venacontracta taps except that "
      "downstream tap is located at one half pipe diameter. These are generally considered "
      "superior to the venacontracta tap because they simplify the pressure tap location "
      "dimensions and do not vary with changes in orifice β ratio.")
    H("Điểm lấy áp ống", "Pipe taps", h4)
    P("Điểm lấy áp ống đặt cách tấm lỗ 2,5 đường kính ống ở thượng lưu (d1 = 2,5D) và 8 đường "
      "kính ở hạ lưu (d2 = 8D). Vì khoảng cách xa tấm lỗ, vị trí chính xác không quá quan trọng, "
      "nhưng ảnh hưởng của độ nhám ống và sai lệch kích thước lại nghiêm trọng hơn.",
      "Pipe taps are located 2.5 pipe diameters upstream (d1 = 2.5D) and 8 diameters downstream "
      "(d 2 = 8D) from the orifice plate. Because of the distance from the orifice, exact location "
      "is not critical, but the effects of pipe roughness, dimensional inconsistencies and so on "
      "are more severe.")
    H("Điểm lấy áp góc", "Corner taps", h4)
    P("Các điểm này giống điểm lấy áp mặt bích về nhiều mặt, chỉ khác là áp suất được đo tại "
      "“góc” giữa tấm lỗ và thành ống. Chúng dùng cho đường kính dưới 50 mm.",
      "These taps are similar in many respects to flange taps, except that the pressure is "
      "measured at the ‘Corner’ between the orifice plate and the pipe wall. These are used for "
      "diameters of less than 50 mm.")

    # --------------------------------------------- 5.3.2 Venturi Tubes
    H("5.3.2 Ống Venturi", "Venturi Tubes", h3)
    P("Lưu lượng tỷ lệ với căn bậc hai của chênh áp do các chỗ thu hẹp trong ống tạo ra [OCR: "
      "“The flow rate.is”]. Ống Venturi là thiết bị tạo chênh áp dựa trên định lý Bernoulli. "
      "Hiệu năng và phép tính nói chung tương tự như tấm lỗ. Ở các thiết bị này có tiếp xúc liên "
      "tục giữa dòng chất lỏng và bề mặt của thiết bị chính.",
      "The flow rate.is proportional to the square root of pressure difference, produced by the "
      "restrictions in pipe. Venturi tubes are differential pressure producers, based on "
      "Bernoulli's Theorem. General performance and calculations are similar to those for orifice "
      "plates. In these devices, there is a continuous contact between the fluid flow and the "
      "surface of the primary device.")

    H("Cấu tạo", "Construction", h4)
    P("Ống Venturi được dùng khi tổn thất áp suất vĩnh viễn là yếu tố quan trọng nhất và khi cần "
      "độ chính xác cực đại trong đo chất lỏng có độ nhớt cao. Nó gồm:",
      "A venturi tube is used where permanent pressure loss is of prime importance, and where "
      "maximum accuracy is desired in the measurement of high viscous fluids. It consists of")
    U(["Một đoạn vào thẳng có cùng đường kính với ống, nơi đặt điểm lấy áp cao;",
       "Một đoạn vào hình côn hội tụ, nơi tiết diện dòng chảy giảm và cột vận tốc tăng còn cột "
       "áp suất giảm;",
       "Một cổ họng hình trụ, nơi đặt điểm lấy áp thấp trong vùng vận tốc không tăng cũng không "
       "giảm;",
       "Một côn phục hồi giãn ra, nơi vận tốc giảm và cột vận tốc đã giảm được phục hồi thành "
       "cột áp suất. Các điểm lấy áp đặt cách côn vào một phần tư đến một nửa đường kính ống ở "
       "thượng lưu và tại giữa đoạn cổ họng."],
      ["A straight inlet section of the same diameter as the pipe in which the high pressure tap "
       "is located,",
       "A converging conical inlet section in which the cross-section of the stream decreases "
       "and the velocity head and decrease of pressure head,",
       "A cylindrical throat which provides for the low pressure tap location of the decreased "
       "pressure in an area where flow velocity is neither increasing nor decreasing, and",
       "A diverging recovery cone in which velocity decreases and the decreased velocity head is "
       "recovered as pressure head. The pressure taps are located one-quarter to one-half pipe "
       "diameter up-stream of the inlet cone and at the middle of the throat section."])

    H("Cấu tạo Venturi cổ điển: dạng dài", "Classic Venturi Construction: [Long Form Venturi]", h4)
    P("Thiết bị gồm một đoạn vào hình trụ bằng đường kính ống; một đoạn côn hội tụ làm giảm "
      "diện tích tiết diện, khiến vận tốc tăng với cột vận tốc tăng tương ứng và cột áp suất "
      "giảm; một đoạn cổ họng hình trụ nơi vận tốc không đổi để đo cột áp suất đã giảm; và một "
      "côn phục hồi giãn ra, nơi vận tốc giảm và gần như toàn bộ cột áp suất ban đầu được phục "
      "hồi. Phần cột áp không phục hồi được thường gọi là tổn thất cột áp (head loss).",
      "It consists of a cylindrical inlet section equal to the pipe diameter; a converging "
      "conical section in which the cross sectional area decreases causing the velocity to "
      "increase with a corresponding increase in the velocity head and a decrease in the pressure "
      "head; a cylindrical throat section where the velocity is constant so that the decreased "
      "pressure head can be measured; and a diverging recovery cone where the velocity decreases "
      "and almost all of the original pressure head is recovered. The unrecovered pressure head "
      "is commonly called as head loss.")
    FIG(6, F.fig_f06())
    P("Venturi cổ điển luôn được chế tạo với thân bằng gang và đoạn cổ họng bằng đồng hoặc thép "
      "không gỉ. Tại điểm giữa cổ họng, 6 đến 8 điểm lấy áp nối cổ họng với một buồng vòng "
      "(annular chamber) để lấy trung bình áp suất cổ họng. Diện tích tiết diện của buồng bằng "
      "1,5 lần diện tích của các điểm lấy áp. Vì không có chuyển động của chất lỏng trong buồng "
      "vòng, áp suất cảm nhận thuần túy là áp suất tĩnh. Thường có 4 điểm từ bề mặt ngoài của "
      "venturi vào buồng vòng, được lệch so với các điểm lấy áp bên trong; áp suất cổ họng được "
      "đo qua các điểm này.",
      "The classic venturi is always manufactured with a cast iron body and a bronze or stainless "
      "steel throat section. At the midpoint of the throat, 6 to 8 pressure taps connect the "
      "throat to an annular chamber so the throat pressure is averaged. The cross sectional area "
      "of the chamber is 1.5 times the cross sectional area of the taps. Since there is no "
      "movement of fluid in the annular chamber, the pressure sensed is strictly static pressure. "
      "Usually 4 taps from the external surface of the venturi into the annular chamber are made. "
      "These are offset from the internal pressure taps. It is through these taps that throat "
      "pressure is measured.")

    H("Ống Venturi dạng ngắn", "Short Form Venturi Tubes", h4)
    P("Trong nỗ lực giảm chi phí và chiều dài lắp đặt, nhà sản xuất đã phát triển thế hệ thứ hai "
      "là ống Venturi dạng ngắn như Hình 7.",
      "In an effort to reduce costs and laying length, manufactures developed a second generation, "
      "or short-form venturi tubes shown in figure 7.")
    FIG(7, F.fig_f07())
    P("Có hai khác biệt chính trong thiết kế này: buồng vòng bên trong được thay bằng một điểm "
      "lấy áp đơn, hoặc trong một số trường hợp là buồng lấy trung bình áp suất ngoài; và góc côn "
      "phục hồi tăng từ 7° lên 21°. Ống Venturi dạng ngắn có thể chế tạo từ gang hoặc hàn từ "
      "nhiều vật liệu tương thích với ứng dụng.",
      "There were two major differences in this design. The internal annular chamber was replaced "
      "by a single pressure tap or in some cases an external pressure averaging chamber, and the "
      "recovery cone angle was increased from 7° to 21°. The short form venturi tubes can be "
      "manufactured from cast iron or welded from a variety of materials compatible with the "
      "application.")
    P("Các điểm lấy áp đặt cách côn vào một phần tư đến một nửa đường kính ống ở thượng lưu và tại "
      "giữa cổ họng. Đôi khi dùng vòng đo áp (piezometer ring) để đo chênh áp. Vòng này gồm vài "
      "lỗ trong mặt phẳng của các vị trí lấy áp. Mỗi nhóm lỗ được nối với nhau trong một vòng "
      "hình vòng để cho áp suất trung bình.",
      "The pressure taps are located one-quarter to one-half pipe diameter upstream of the inlet "
      "cone and at the middle of the throat section. A piezometer ring is sometimes used for "
      "differential pressure measurement. This consists of several holes in the plane of the tap "
      "locations. Each set of holes is connected together in an annular ring to give an average "
      "pressure.")
    P("Venturi nối vòng đo áp không phù hợp với hệ thống thổi rửa dùng cho bùn và chất lỏng bẩn, "
      "vì chất thổi có xu hướng đi tắt tới lỗ lấy áp gần nhất. Kết nối vòng đo áp thường chỉ dùng "
      "cho ống rất lớn hoặc khi cần áp suất trung bình chính xác nhất để bù cho biến đổi của "
      "phân bố thủy lực của chất lỏng. Do đó, khi cần đo chất bẩn và dùng điểm lấy áp vòng đo, "
      "nên dùng cảm biến kín lắp bằng phẳng với thành ống và thành trong của cổ họng.",
      "Venturis with piezometer connections are unsuitable for use with purge systems used for "
      "slurries and dirty fluids since the purging fluid tends to short circuit to the nearest tap "
      "holes. Piezometer connections are normally used only on very large tubes or where the most "
      "accurate average pressure is desired to compensate for variations in the hydraulic profile "
      "of the flowing fluid. Therefore, when it is necessary to meter dirty fluids and use "
      "piezometer taps, sealed sensors which mount flush with the pipe and throat inside wall "
      "should be used.")
    P("Venturi có điểm lấy áp đơn có thể được thổi rửa theo cách thông thường khi dùng với chất "
      "lỏng bẩn. Vì ống Venturi không có chỗ thay đổi đột ngột về đường nét, không có góc sắc và "
      "không có phần nhô ra, nó thường được dùng để đo bùn và chất lỏng bẩn có xu hướng đóng hoặc "
      "làm tắc thiết bị chính.",
      "Single pressure tap venturis can be purged in the normal manner when used with dirty "
      "fluids. Because the venturi tube has no sudden changes in contour, no sharp corners, and no "
      "projections, it is often used to measure slurries and dirty fluids which tend to build up "
      "on or clog of the primary devices.")

    H("Các loại ống Venturi", "Types of Venturi Tubes", h4)
    P("Venturi được chế tạo ở một số dạng, gồm:", "Venturis are built in several forms. These include")
    U(["Ống Venturi dạng dài tiêu chuẩn hay cổ điển",
       "Dạng ngắn biến đổi với côn ra được rút ngắn",
       "Dạng lệch tâm để xử lý pha hỗn hợp hoặc giảm tích tụ vật liệu nặng",
       "Dạng chữ nhật dùng trong ống dẫn"],
      ["A standard long-form or classic venturi tube",
       "A modified short form where the outlet cone is shortened",
       "An eccentric form to handle mixed phases or to minimize buildup of heavy materials",
       "A rectangular form used in duct work"])

    H("Lắp đặt ống Venturi", "Installation of Venturi Tubes", h4)
    P("Ống Venturi có thể lắp ở bất kỳ vị trí nào cho phù hợp với yêu cầu của ứng dụng và đường "
      "ống. Hạn chế duy nhất là với chất lỏng thì venturi luôn phải đầy. Các điểm lấy áp có van "
      "tuân theo cùng hướng dẫn lắp đặt như tấm lỗ.",
      "A venturi tube may be installed in any position to suit the requirements of the application "
      "and piping. The only limitation is that with liquids the venturi is always full. The valved "
      "pressure taps will follow the same installation guidelines as for orifice plates.")
    P("Nên dùng cánh chỉnh lưu (straightening vanes) ở thượng lưu của venturi để giảm chiều dài "
      "đoạn ống vào. Vị trí lắp cánh chỉnh lưu cần có tối thiểu hai đường kính ống ở thượng lưu "
      "và hai đường kính ở hạ lưu trước khi vào venturi. Không có hạn chế về cấu hình đường ống "
      "phía sau venturi, ngoại trừ một van không được đặt gần hơn hai đường kính.",
      "It is recommended that the use of straightening vanes upstream of the venturi to reduce the "
      "inlet pipe length. The vane installation should have a minimum of two diameters upstream "
      "and two diameters downstream before entering the venturi. There is no limitation on piping "
      "configuration downstream of the venturi except that a value should be no closer than two "
      "diameters.")

    # --------------------------------------------- 5.3.3 Flow Nozzle
    H("5.3.3 Vòi phun lưu lượng", "Flow Nozzle", h3)
    P("Vòi phun lưu lượng dùng cho đo dòng chảy vận tốc cao, nơi sự xói mòn hoặc hiện tượng sôi "
      "hơi (cavitation) có thể làm mòn hoặc hư tấm lỗ. Đồng hồ vòi phun được bắt giữa các mặt "
      "bích của ống dẫn chất lỏng. Áp suất thượng lưu và hạ lưu được ghi nhận bằng cảm biến chênh "
      "áp để tính lưu lượng. Tổn thất áp suất vĩnh viễn ở mức tương đương tấm lỗ, nhưng có thêm "
      "khả năng xử lý chất lỏng bẩn và mài mòn. Một bộ truyền chênh áp được dùng để đo áp suất "
      "giữa vòi phun và dòng chảy trong ống. Công nghệ đồng hồ chênh áp dạng này có thể chế tạo "
      "để đo cả khí lẫn chất lỏng.",
      "The flow nozzle is used for high velocity flow measurement where erosion or cavitation "
      "could wear or damage an orifice plate. Nozzle meter is bolted between flanges of pipe "
      "carrying the fluid. The pressures on upstream and downstream are noted by using a "
      "differential pressure sensor for the calculation of flow rate. Permanent pressure loss is "
      "on the same level as an orifice, with the added ability to handle dirty and abrasive "
      "fluids. A differential pressure transmitter is used to measure pressure between the nozzle "
      "and the pipe flow stream. This type of differential pressure flowmeter technology can be "
      "constructed to measure either gas or liquids.")

    H("Vòi phun dạng mặt bích", "Flange Type Flow Nozzle", h4)
    P("Vòi phun là đoạn hội tụ nhẵn xả dòng chảy song song với trục của ống hạ lưu. Đầu hạ lưu "
      "của vòi phun gần giống một ống ngắn và có đường kính bằng vena contracta của một tấm lỗ "
      "cùng năng lực. Vì vậy tỷ số đường kính của vòi phun nhỏ hơn hoặc hệ số dòng chảy của nó lớn "
      "hơn. Phục hồi áp suất tốt hơn tấm lỗ. Hình 8 cho thấy vòi phun dạng mặt bích.",
      "The Flow nozzle is a smooth, convergent section that discharges the flow parallel to the "
      "axis of the downstream pipe. The downstream end of a nozzle approximates a short tube and "
      "has the diameter of the venacontracta of an orifice of equal capacity. Thus the diameter "
      "ratio for a nozzle is smaller or its flow coefficient is larger. Pressure recovery is "
      "better than that of an orifice. Figure 8 shows a flow nozzle of flange type.")
    FIG(8, F.fig_f08())

    H("Các thiết kế khác nhau của vòi phun", "Different Designs of Flow Nozzle", h4)
    P("Vòi phun thường làm bằng đồng, thép không gỉ, đồng thanh hoặc monel. Chúng thường được mạ "
      "crom. Đôi khi lớp phủ slettite được dùng để tăng khả năng chống mài mòn [OCR: “slettite”].",
      "Flow nozzles are usually made of gun metals, stainless steel, bronze or monel metal. They "
      "are frequently chromium plated. Sometimes slettite coating is provided to have abrasion "
      "resistance.")
    P("Các điểm lấy áp có thể là vòng hình vòng với các khe mở vào ống ở mỗi bên mặt bích của vòi "
      "phun, hoặc là các lỗ đơn khoan xuyên qua mặt bích của ống gần mặt bích vòi phun.",
      "The pressure tappings may take the form of annular rings with slots opening into the main "
      "at each side of the flange of the nozzle or of single holes drilled through the flange of "
      "the main close to the nozzle flange.")
    P("Vòi phun không phù hợp để đo chất lỏng nhớt. Nó có thể được lắp vào một đường ống có sẵn "
      "mà không gặp nhiều khó khăn.",
      "It is not suitable for metering viscous liquids. It may be installed in an existing main "
      "without great difficulty.")
    FIG(9, F.fig_f09())
    P("Ưu điểm:", "Advantages:")
    U(["Tổn thất áp suất vĩnh viễn thấp hơn tấm lỗ.",
       "Phù hợp với chất lỏng chứa chất rắn lắng đọng.",
       "Được chấp nhận rộng rãi cho dòng hơi ở áp suất và nhiệt độ cao."],
      ["Permanent pressure loss lower than that for an orifice plate.",
       "It is suitable for fluids containing solids that settle.",
       "It is widely accepted for high pressure and temperature steam flow."])
    P("Nhược điểm:", "Disadvantages:")
    U(["Chi phí cao hơn tấm lỗ.",
       "Chỉ giới hạn ở kích cỡ ống trung bình.",
       "Cần bảo trì nhiều hơn (phải tháo một đoạn ống để kiểm tra hoặc lắp đặt)."],
      ["Cost is higher than orifice plate.",
       "It is limited to moderate pipe sizes.",
       "It requires more maintenance. (It is necessary to remove a section of pipe to inspect or "
       "install it)."])

    # --------------------------------------------- 5.3.4 Dall Tube
    H("5.3.4 Đồng hồ ống Dall", "Dall Tube Flow Meters", h3)
    P("Đây là một phần tử chính dạng thu hẹp khác dùng đo lưu lượng. Nó là dạng rút gọn hoặc biến "
      "đổi của đồng hồ Venturi. Chênh áp của ống Dall nằm trung gian giữa tấm lỗ và ống Venturi.",
      "It is another restriction type primary element for flow measurement. It is a shortened/ "
      "modified form of a Venturi meter. The differential pressure of Dall tube is midway of the "
      "orifice and venturi tube.")
    P("Nó gồm hai đoạn với góc côn tương đối lớn. Đoạn vào thẳng ngắn sau đó là sự giảm đường kính "
      "đột ngột. Một khe hở hình vòng hẹp ngăn đoạn vào ngắn và đoạn ra giãn ra. Cổ họng được tạo "
      "bởi một khe theo chu vi nằm giữa côn vào và côn ra. Áp suất cao hơn được đo tại vùng khe "
      "tròn và áp suất thấp hơn được đo ở thượng lưu [mô tả của nguồn có vẻ đảo và được giữ "
      "nguyên — xem Construction and Working bên dưới]. Thường có lớp phủ lithium để tránh ăn mòn "
      "thiết bị bởi chất lỏng.",
      "It consists of two sections, with relativity large cone angle. The short straight inlet "
      "followed by an abrupt decrease in diameter. A narrow annular slit separates the short inlet "
      "and divergent outlet. The throat is formed by a circumstantial slit located between the "
      "inlet and outlet cones. The higher pressure is measured at circular slit area, and lower "
      "pressure is measured at upstream. Typically a lithium coating is provided to avoid "
      "corrosion of the device by the fluids.")
    P("Chênh áp do ống Dall tạo ra lớn hơn nhiều, gần gấp đôi so với đồng hồ Venturi có cùng đường "
      "kính thượng lưu và cổ họng với cùng tổn thất cột áp. Nó gây tổn thất áp suất rất thấp so "
      "với các phần tử chênh áp khác. Có thể phục hồi tới 95% chênh áp.",
      "The differential pressure produced by Dall tube is much higher, nearly doubled to that of "
      "Venturi meter having the same upstream and throat diameters with the same net head loss. It "
      "causes a very low-pressure loss compared to other differential pressure flow elements. Up "
      "to 95% Differential pressure can be recovered.")

    H("Cấu tạo và hoạt động", "Construction and Working", h4)
    P("Đây là phiên bản biến đổi của ống Venturi. Nó tạo chênh áp lớn với áp suất thấp nhỏ hơn "
      "ống Venturi thông thường. Ảnh chụp và sơ đồ của ống Dall được chỉ ra trong Hình 10.",
      "It is a modified version of venturi tube. It produces large differential pressure with low "
      "pressure less than the conventional venturi tube. The photographic view and schematic "
      "sketch of the dall tube are shown in figure 10.")
    FIG(10, F.fig_f10())
    P("Ống gồm thân dạng đoạn ngắn có mặt bích với đoạn vào thẳng ngắn kết thúc bằng sự giảm "
      "đường kính đột ngột hay vai vào (inlet shoulder). Tiếp theo là một đoạn thu hẹp hình côn và "
      "đoạn ra giãn ra được ngăn bằng một khe hở hình vòng hẹp. Điểm lấy áp cao là một lỗ khoan "
      "xuyên thân tiếp tuyến với vai vào. Điểm lấy áp thấp được khoan xuyên thân để nối với một "
      "khe vòng ở cổ họng. Vai vào ngay trước đoạn thu hẹp có rất ít ảnh hưởng đến tổn thất áp "
      "suất vĩnh viễn. Côn ra làm giảm vận tốc dòng chảy, giúp tăng phục hồi áp suất.",
      "It consists of a flanged spool piece body with a short, straight inlet section terminating "
      "in an abrupt decrease in diameter or inlet shoulder. This is followed by a conical "
      "restriction and a diverting outlet separated by a narrow annular gap. The high pressure "
      "tap is a hole drilled through the body tangent to the inlet shoulder. The low pressure tap "
      "is drilled through the body so as to connect with an annular slot in the throat. The inlet "
      "shoulder immediately preceding the restriction has little effect on permanent pressure "
      "loss. The outlet cone causes a decrease in flow velocity that provides an increase in "
      "pressure recovery.")
    P("Ống không phù hợp đo chất lỏng chứa chất rắn có thể lắng trong khe cổ họng. Ống Dall dùng "
      "đo lưu lượng nước, nước thải, không khí và hơi. Ống thường đúc bằng đồng; với kích cỡ 450 "
      "mm trở lên dùng gang chất lượng cao. Khi cần bảo vệ chống ăn mòn, ống có thể được phủ "
      "lithcote [OCR: “lithcote lined”].",
      "It is not suitable for measuring the flow of fluids containing solids which could settle "
      "out in the throat slot. The Dall tube is used for water, sewage, air and steam flow "
      "measurement. The Dall tubes are normally cast in gun metal. But for 450 mm and larger "
      "sizes, high grade cast iron is used. When it is required to protect the tube from "
      "corrosion, it may be lithcote lined.")
    P("Dall Flow Tube có tỷ số áp suất tạo ra trên áp suất mất lớn hơn ống Venturi. Nó nhỏ gọn hơn "
      "và thường dùng trong ứng dụng lưu lượng lớn. Ống gồm đoạn vào thẳng ngắn sau đó là sự giảm "
      "đột ngột đường kính trong. Đoạn này gọi là vai vào, tiếp theo là côn vào hội tụ và côn ra "
      "giãn ra; hai côn được ngăn bằng một khe hoặc khoảng hở. Áp suất thấp đo tại cổ họng có khe "
      "(vùng giữa hai côn). Áp suất cao đo tại mép thượng lưu của vai vào.",
      "Dall Flow Tube has a higher ratio of pressure developed to pressure lost than the venturi "
      "flow tube. It is more compact and is commonly used in large flow applications. The tube "
      "consists of a short, straight inlet section followed by an abrupt decrease in the inside "
      "diameter of the tube. This section, called the inlet shoulder, is followed by the "
      "converging inlet cone and a diverging exit cone. The two cones are separated by a slot or "
      "gap between the two cones. The low pressure is measured at the slotted throat (area between "
      "the two cones). The high pressure is measured at the upstream edge of the inlet shoulder.")
    P("Ống Dall có sẵn ở kích cỡ trung bình đến rất lớn. Ở kích cỡ lớn, chi phí thường thấp hơn "
      "ống Venturi. Loại ống này có tổn thất áp suất khoảng 5%. Lưu lượng và độ sụt áp liên hệ "
      "như trong phương trình.",
      "The dall flow tube is available in medium to very large sizes. In the large sizes, the cost "
      "is normally less than that of a venturi flow tube. This type of flow tube has a pressure "
      "loss of about 5%. Flow rate and pressure drop are related as shown in Equation")
    EQ("v = K · √(DP)")
    U(["v = lưu lượng thể tích",
       "K = hằng số suy ra từ các thông số cơ khí của phần tử chính",
       "DP = chênh áp"],
      ["v = volumetric flow rate",
       "K= constant derived from the mechanical parameters of the primary elements",
       "DP= differential pressure"])
    P("Ưu điểm:", "Advantages:")
    U(["Tổn thất cột áp thấp", "Chiều dài lắp đặt ngắn",
       "Có sẵn với nhiều vật liệu chế tạo"],
      ["Low head loss", "Short lying length",
       "It is available in numerous materials of construction"])
    P("Nhược điểm:", "Disadvantages:")
    U(["Chênh áp nhạy với nhiễu loạn ở thượng lưu.",
       "Cần nhiều đoạn ống thẳng hơn ở phần tiến đến.",
       "Không được xem xét cho đo dòng nước cấp nóng."],
      ["Pressure difference is sensitive to up-stream disturbances.",
       "More straight pipe required in the approach pipe length.",
       "It is not considered for measuring flow of hot feed water."])
    H("Các loại ống Dall", "Types of Dall Tube", h4)
    P("Ống Dall khác nhau về phương pháp chế tạo để phù hợp với một ứng dụng cụ thể. Các loại là:",
      "Dall tube differs in the method of construction to suit a particular application. The types are")
    U(["Ống Dall dạng tuyến tính", "Ống Dall dạng đường cong",
       "Đoạn chèn Dall ngắn", "Đoạn chèn Dall dài",
       "Ống Dall nước thải", "Ống Dall chế tạo"],
      ["Linear type Dall tube", "Contour Dall tube", "Dall short insert",
       "Dall long insert", "Sewage Dall tube", "Fabricated Dall tube"])

    # --------------------------------------------- 5.3.5 Pitot tube
    H("5.3.5 Ống Pitot", "Pitot tube", h3)
    P("Ống Pitot được dùng để xác định áp suất động của dòng không khí và từ đó xác định vận tốc "
      "bay của máy bay. Ban đầu nó được dùng để xác định tốc độ của nước trong sông.",
      "It is used to determine the dynamic pressure of the air flow and subsequently, the airspeed "
      "of the plane. It was initially used to determine the speed of water in a river.")
    P("Ống Pitot dùng để xác định sự khác biệt giữa áp suất tĩnh, động và tổng của một chất lỏng. "
      "Chất lỏng về cơ bản là chất lỏng hoặc chất khí đang chảy. Ví dụ, nước chảy trong sông hay "
      "các phân tử oxy chuyển động trong gió đều được coi là chất lỏng.",
      "The pitot tube is used to determine the difference between static, dynamic, and total "
      "pressure of a fluid. A fluid is basically a liquid or a gas that flows. For example, the "
      "water flowing in a river or the oxygen molecules moving in the wind are considered fluids.")
    P("Một ống Pitot điển hình gồm một thiết bị nằm trong đường đi của dòng chất lỏng. Khi chất "
      "lỏng chảy qua ống, một áp suất được tạo ra và được đo. Ống không có đầu ra nên chất lỏng "
      "dừng lại, và áp suất dừng của nó, còn gọi là áp suất tổng, được xác định.",
      "A typical pitot tube consists of a device that is situated in the path of the fluid. As the "
      "fluid flows through the tube, a pressure is created which is measured. The tube does not "
      "have an outlet so the fluid comes to a rest, and its stagnation pressure, which is also "
      "called the total pressure, is determined.")
    P("Để tính vận tốc bay của máy bay, cũng phải xác định áp suất tĩnh của chất lỏng. Áp suất tĩnh "
      "là áp suất tạo ra từ chất lỏng đang chuyển động. Áp suất này thu được qua ống pitot-static, "
      "gồm một ống thứ hai có các lỗ ở hai bên.",
      "In order to calculate the airspeed of a plane, the static pressure of the fluid must also "
      "be determined. Static pressure is the pressure created from the moving fluid. This is "
      "obtained through a pitot-static tube, which consists of a second tube with holes on the sides.")
    P("Sau khi xác định áp suất tĩnh, lấy nó trừ đi áp suất dừng. Phép tính này cho áp suất động "
      "của chất lỏng. Với thông tin này, có thể xác định vận tốc bay của máy bay.",
      "Once the static pressure is determined, it is subtracted from the stagnation pressure. This "
      "calculation provides the dynamic pressure of the fluid. With this information, the airspeed "
      "of the plane can be determined.")
    P("Ống Pitot lần đầu được Henri Pitot dùng để đo tốc độ của sông Seine. Ông nghiên cứu dòng "
      "nước ở các độ sâu khác nhau. Kết quả dường như bác bỏ quan niệm nước chảy nhanh hơn ở độ "
      "sâu lớn hơn.",
      "The pitot tube was first utilized by Henri Pitot to measure the speed of the Seine River. "
      "He studied the flow of water at various depths. His findings seemed to disprove the notion "
      "that water flowed faster at deeper depths.")
    P("Thường thì ống Pitot được gắn vào cánh hoặc thân máy bay. Nó cần được kiểm tra thường "
      "xuyên để bảo đảm hoạt động đúng. Bất kỳ sự cố nào cũng có thể cho số đọc vận tốc bay sai.",
      "Typically, the pitot tube is attached to the wing or the fuselage of the plane. It needs to "
      "be checked on a regular basis to ensure it is working properly. Any malfunction can cause "
      "an incorrect reading of the airspeed.")
    P("Một nguyên nhân làm ống Pitot hoạt động không đúng là đóng băng. Đóng băng là vấn đề nghiêm "
      "trọng có thể làm hư hỏng dụng cụ trên máy bay. Cần có quy trình chống đóng băng định kỳ để "
      "đảm bảo ống Pitot đo đúng áp suất liên quan đến dòng không khí quanh máy bay.",
      "One cause of an improperly functioning pitot is ice formation. Icing is a serious problem "
      "that can result in damage to the instruments on the plane. Regular deicing procedures are "
      "required to ensure that the pitot is correctly measuring the pressures associated with the "
      "airflow around the plane.")

    H("Cấu tạo ống Pitot", "Construction of pitot tube", h4)
    P("Về cơ bản đây là dụng cụ đo vận tốc chất lỏng, cũng có thể dùng đo lưu lượng chất lỏng và "
      "khí. Nó gồm hai ống rỗng cảm nhận áp suất tại những vị trí khác nhau trong ống dẫn. Các "
      "ống rỗng này có thể lắp riêng trong ống hoặc lắp cùng nhau trong một vỏ thành một thiết bị "
      "duy nhất. Một ống đo áp suất dừng hay áp suất va, ống kia chỉ đo áp suất tĩnh, thường ở "
      "thành ống.",
      "It is basically a fluid velocity measuring instrument that can also be used for flow "
      "measurement of liquids and gases. It consists of two hollow tubes that sense pressure at "
      "different places within the pipe. This hollow tubes can be mounted separately in a pipe or "
      "installing together in one casing as a single device. One tube measures the stagnation or "
      "impact pressure and another tube measures only static pressure usually at the wall of the pipe.")

    H("Nguyên lý hoạt động của ống Pitot", "Working principle of Pitot tube", h4)
    P("Khi một vật rắn được đặt ở giữa và đứng yên trong đường ống có chất lỏng chảy, vận tốc của "
      "chất lỏng bắt đầu giảm (đồng thời áp suất chất lỏng tăng do năng lượng động chuyển thành "
      "năng lượng áp suất) vì sự hiện diện của vật. Ngay phía trước vật rắn, vận tốc trở về không. "
      "Điểm này gọi là điểm dừng (stagnation point).",
      "When a solid body is kept centrally, and stationery in a pipeline with flowing fluid, the "
      "velocity of the fluid starts reducing (at the same time the pressure fluid increases due to "
      "the conversion of kinetic energy into pressure energy) due to the presence of the body. At "
      "directly in front of the solid body, the velocity becomes zero. This point is known as the "
      "stagnation point.")
    P("Phương trình vận tốc được suy ra bằng cách áp dụng nguyên lý Bernoulli; phương trình cuối "
      "cùng được cho bên dưới.",
      "The equation of velocity is derived by applying Bernoulli's principle; the final equation "
      "is given below")
    EQ("v = √(2 g h)")
    P("g = gia tốc do trọng lực.", "g = acceleration due to gravity")
    EQ("v<sub>actual</sub> = C<sub>v</sub> · √(2 g h)")
    P("C<sub>v</sub> = hệ số của ống Pitot.", "Cv = Coefficient of pitot tube")

    H("Ứng dụng của ống Pitot", "Applications of pitot tube", h4)
    P("Ống Pitot được dùng trong các dòng tiện ích khi không cần độ chính xác cao. Nó được dùng "
      "trong hệ thống ống và kênh dẫn không khí, trong máy bay để đo vận tốc dòng không khí, và "
      "để lập bản đồ phân bố vận tốc trong kênh hoặc ống dẫn.",
      "The pitot tube is used in utility streams where high accuracy is not necessary. It is used "
      "in the air duct and pipe system. It is used in aircraft to measure air flow velocity. They "
      "are used for mapping flow profile in a channel or duct.")

    P("Ưu điểm:", "Advantages:")
    P("Có một số ưu điểm của ống Pitot, chẳng hạn:",
      "There are some advantages of pitot tube, such as:")
    U(["Kinh tế khi lắp đặt",
       "Không chứa bộ phận chuyển động; điều này giảm thiểu tổn thất ma sát.",
       "Dễ lắp đặt. Nhờ kích thước nhỏ, có thể đưa vào dòng chất lỏng mà không cần ngắt dòng.",
       "Tổn thất áp suất rất nhỏ.",
       "Có thể lắp dễ dàng trong môi trường cực đoan, điều kiện nhiệt độ và áp suất cao.",
       "Một số loại cũng có thể tháo dễ dàng khỏi đường ống."],
      ["Economical to install",
       "Do not contain moving parts; this minimizes the frictional loss.",
       "Easy to install. Due to its small size, It can introduce to fluid flow without shutting "
       "down the flow.",
       "Loss of pressure is very small.",
       "Can be easily installed in extreme environment, high temperature and pressure conditions",
       "Some types can also be easily removed from the pipeline."])
    P("Nhược điểm của ống Pitot:", "Disadvantages of pitot tubes:")
    P("Có một số nhược điểm của ống Pitot, chẳng hạn:",
      "There are some disadvantages of pitot tubes, such as:")
    U(["Độ nhạy thấp và độ chính xác kém. Nó cần dòng chảy vận tốc cao.",
       "Không phù hợp cho chất lỏng bẩn hoặc dính như nước thải.",
       "Độ nhạy bị nhiễu bởi hướng dòng chảy.",
       "Ống Pitot có ứng dụng hạn chế trong công nghiệp vì dễ bị tắc bởi vật lạ trong chất lỏng.",
       "Không có tiêu chuẩn hóa cho ống Pitot.",
       "Thay đổi phân bố vận tốc có thể gây sai số đáng kể. Do phân bố vận tốc thay đổi, nó tạo "
       "chênh áp rất nhỏ khó đo."],
      ["Low sensitivity and Poor accuracy. It requires high-velocity flow.",
       "Not suitable for dirty or sticky fluid like sewage disposal.",
       "Sensitivity disturbed by flow direction",
       "Pitot tubes have found limited applications in industries because they can easily become "
       "clogged with foreign materials in the liquid.",
       "There is no standardization for pitot tube",
       "Change in velocity profile may cause significant errors. Due to change in velocity profile, "
       "it develops a very low differential pressure which is difficult to measure."])

    # ---------------------------------------------------------------- refs
    H("Tài liệu tham khảo", "References")
    b.append(refs(_REFS))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
