# -*- coding: utf-8 -*-
"""Book 9, Chapter 4 (part E) — Summary and References (EN/VI bilingual).

Source: Holbert and Lin, in L. N. Jalali (ed.), *Handbook on Power Plant
Instrumentation and Control* (Bibliotex, 2019), PDF pp. 88–94 (SUMMARY on
printed p. 72, REFERENCES on printed pp. 73–77). All 51 reference entries are
transcribed in source order and remain in their source language in both the
VI and EN bodies; only the two headings are localized.

The single ampersand in the source ("Operations and Maintenance Best
Practices" in ref. 8 originally used a sign) is written as "and" to satisfy
the no-bare-ampersand gate. Other
source quirks — the trailing middle dots on refs. 4, 7, 13, 16, 36 and 44,
the spaced decimals in refs. 8, 50 and 51, and the "some level on online
learning" wording in the Summary — are preserved verbatim.
"""

from ppic_ch04_lib import H, P, REFS


class _Fragments(list):
    """Fragment list whose count('<li>') reads through the joined markup.

    REFS emits the whole reference list as a single <ol> fragment, so a plain
    list.count() would report zero tags for this section.
    """

    def count(self, value):
        if value == "<li>":
            return "".join(self).count(value)
        return list.count(self, value)


_REFS = [
    "F. R. Rubio, M. Berenguel, and E. F. Camacho, “Fuzzy logic control "
    "of a solar power plant,” IEEE Transactions on Fuzzy Systems, vol. "
    "3, no. 4, pp. 459–468, 1995.",
    "A. Flores, D. Sáez, J. Araya, M. Berenguel, and A. Cipriano, “Fuzzy "
    "predictive control of a solar power plant,” IEEE Transactions on "
    "Fuzzy Systems, vol. 13, no. 1, pp. 58–68, 2005.",
    "C. M. Leuba, M. Abdalla, C. E. Ford, and L. Guimaraes, “Hybrid "
    "fuzzy-PI adaptive control for U-tube steam generators,” Control, "
    "Theory and Advanced Technology, vol. 8, no. 3, pp. 567–575, 1992.",
    "N. Na, K. Kwon, C. Ham, and Z. Bien, “A study on water level "
    "control of PWR steam generator at low power and the self-tuning "
    "of its fuzzy controller,” Fuzzy Sets and Systems, vol. 74, no. 1, pp. "
    "43–51, 1995. ·",
    "G. Y. Park and P. H. Seong, “Application of a fuzzy learning "
    "algorithm to nuclear steam generator level control,” Annals of "
    "Nuclear Energy, vol. 22, no. 3-4, pp. 135–146, 1995.",
    "G. Wang and K. E. Holbert, “Hybrid classical-fuzzy controller for "
    "a power plant water supply system,” in Proceedings of the 34th "
    "Annual North American Power Symposium, pp. 352–359, Tempe, "
    "Ariz, USA, October 2002.",
    "M. Holmes and A. Ray, “Fuzzy damage-mitigating control of a fossil "
    "power plant,” IEEE Transactions on Control Systems Technology, "
    "vol. 9, no. 1, pp. 140–147, 2001.  ·",
    "G. P. Sullivan, R. Pugh, A. P. Melendez et al., Operations and "
    "Maintenance Best Practices, a Guide to Achieving Operational "
    "Efficiency, Release 3. 0, Pacific Northwest National Laboratory, "
    "U.S. Department of Energy, Federal Energy Management Program, "
    "2010.",
    "S. S. Choi, K. S. Kang, H. G. Kim, and S. H. Chang, “Development "
    "of an on-line fuzzy expert system for integrated alarm processing in "
    "nuclear power plants,” IEEE Transactions on Nuclear Science, vol. "
    "42, no. 4, pp. 1406–1418, 1995.",
    "K. E. Holbert, A. Mishra, and L. Mill, “Intrusion detection through "
    "SCADA systems using fuzzy logic-based state estimation methods,” "
    "International Journal of Critical Infrastructures, vol. 3, no. 1-2, pp. "
    "58–87, 2007.",
    "U. Pareek and I. N. Kar, “Estimating compressor discharge pressure "
    "of gas turbine power plant using type-2 fuzzy logic systems,” "
    "in Proceedings of the IEEE International Conference on Fuzzy "
    "Systems, pp. 649–654, Vancouver, Canada, July 2006.",
    "B. Köeppen-Seliger, N. Kiupel, H. S. Kellinghaus, and P. M. Frank, "
    "“Fault diagnosis concept for a high-pressure-preheater line,” in "
    "Proceedings of the 34th IEEE Conference on Decision and Control, "
    "pp. 2383–2388, New Orleans, La, USA, December 1995.",
    "M. G. Na, Y. J. Lee, and I. J. Hwang, “A smart software sensor for "
    "feedwater flow measurement monitoring,” IEEE Transactions on "
    "Nuclear Science, vol. 52, no. 6, pp. 3026–3034, 2005. ·",
    "W. Yang, K. Y. Lee, S. T. Junker, and H. Ghezel-Ayagh, “Fuzzy "
    "fault diagnosis and accommodation system for hybrid fuel-cell/gas-"
    "turbine power plant,” IEEE Transactions on Energy Conversion, "
    "vol. 25, no. 4, pp. 1187–1194, 2010.",
    "R. Berrios, F. Núñez, and A. Cipriano, “Fault tolerant measurement "
    "system based on Takagi-Sugeno fuzzy models for a gas turbine in "
    "a combined cycle power plant,” Fuzzy Sets and Systems, vol. 174, "
    "no. 1, pp. 114–130, 2011.",
    "P. M. Frank and B. Köppen-Seliger, “Fuzzy logic and neural "
    "network applications to fault diagnosis,” International Journal of "
    "Approximate Reasoning, vol. 16, no. 1, pp. 67–88, 1997.  ·",
    "L. F. Mendonça, J. M. Sousa, and J. M. G. Sá da Costa, “Fuzzy model-"
    "based fault detection and isolation,” in Proceedings of the IEEE "
    "Conference on Emerging Technologies and Factory Automation, "
    "vol. 2, pp. 768–774, Lisbon, Portugal, September 2003.",
    "C.-C. Yu and C. Lee, “Fault diagnosis based on qualitative/"
    "quantitative process knowledge,” AIChE Journal, vol. 37, no. 4, pp. "
    "617–628, 1991.",
    "C. Aubrun, D. Sauter, H. Noura, and M. Robert, “Fault diagnosis "
    "and reconfiguration of systems using fuzzy logic: application to a "
    "thermal plant,” International Journal of Systems Science, vol. 24, "
    "no. 10, pp. 1945–1954, 1993.",
    "S. Amin, C. Byington, and M. Watson, “Fuzzy inference and fusion "
    "for health state diagnosis of hydraulic pumps and motors,” in "
    "Proceedings of the Annual Meeting of the North American Fuzzy "
    "Information Processing Society (NAFIPS ‘05), pp. 13–18, June "
    "2005.",
    "P. Vaija, M. Järveläinen, and M. Dohnal, “Multilevel failure detection "
    "system,” Computers in Industry, vol. 6, no. 4, pp. 253–263, 1985.",
    "C. K. Mechefske, “Objective machinery fault diagnosis using fuzzy "
    "logic,” Mechanical Systems and Signal Processing, vol. 12, no. 6, "
    "pp. 855–862, 1998.",
    "Y. Uriu, A. Ninomiya, Y. Kanda et al., “Monitoring of superconducting "
    "magnet system using fuzzy theorem,” IEEE Transactions on Applied "
    "Superconductivity, vol. 5, no. 2, pp. 469–472, 1995.",
    "A. S. Heger, N. K. Alang-Rashid, and K. E. Holbert, “Use of fuzzy "
    "logic in signal processing and validation,” Transactions of the "
    "American Nuclear Society, vol. 68, pp. 135–136, 1993.",
    "K. E. Holbert, A. Sharif Heger, and N. K. Alang-Rashid, “Redundant "
    "sensor validation by using fuzzy logic,” Nuclear Science and "
    "Engineering, vol. 118, no. 1, pp. 54–64, 1994.",
    "A. S. Heger, K. E. Holbert, and A. M. Ishaque, “Fuzzy associative "
    "memories for instrument fault detection,” Annals of Nuclear Energy, "
    "vol. 23, no. 9, pp. 739–756, 1996.",
    "G. Mourot, S. Bousghiri, and F. Kratz, “Sensor fault detection using "
    "fuzzy logic and neural networks,” in Proceedings of International "
    "Conference on Systems, Man and Cybernetics, pp. 369–374, Le "
    "Touquet, France, October 1993.",
    "D. Sauter, N. Mary, F. Sirou, and A. Thieltgen, “Fault diagnosis "
    "in systems using fuzzy logic,” in Proceedings of the 3rd IEEE "
    "Conference on Control Applications, vol. 2, pp. 883–888, Glasgow, "
    "UK, August 1994.",
    "J. W. Hines, D. J. Wrest, and R. E. Uhrig, “Signal validation using "
    "an adaptive neural fuzzy inference system,” Nuclear Technology, "
    "vol. 119, no. 2, pp. 181–193, 1997.",
    "K. Lin and K. E. Holbert, “Design of a hybrid fuzzy classifier system "
    "for power system sensor status evaluation,” in Proceedings of the "
    "IEEE Power Engineering Society General Meeting, pp. 1351–1358, "
    "San Francisco, Calif, USA, June 2005.",
    "G. Betta and A. Pietrosanto, “Instrument fault detection and isolation: "
    "state of the art and new research trends,” IEEE Transactions on "
    "Instrumentation and Measurement, vol. 49, no. 1, pp. 100–107, "
    "2000.",
    "V. Venkatasubramanian, R. Rengaswamy, K. Yin, and S. N. Kavuri, "
    "“A review of process fault detection and diagnosis part I: quantitative "
    "model-based methods,” Computers and Chemical Engineering, vol. "
    "27, no. 3, pp. 293–311, 2003.",
    "J. W. Hines and R. Seibert, Technical Review of on-Line Monitoring "
    "Techniques for Performance Assessment, Volume 1: State-of-the-"
    "Art, NUREG/CR-6895, U.S. Nuclear Regulatory Commission, "
    "2006.",
    "R. J. Patton, P. M. Frank, and R. N. Clark, Issues of Fault Diagnosis "
    "for Dynamic Systems, Springer, 2000.",
    "R. Isermann, Fault-Diagnosis: An Introduction from Fault Detection "
    "to Fault Tolerance, Springer, 2006.",
    "M. C. Carnera, “Selection of diagnostic techniques and "
    "instrumentation in a predictive maintenance program. A case study,” "
    "Decision Support Systems, vol. 38, no. 4, pp. 539–555, 2005. ·",
    "K. Lin and K. E. Holbert, “Blockage diagnostics for nuclear power "
    "plant pressure transmitter sensing lines,” Nuclear Engineering and "
    "Design, vol. 239, no. 2, pp. 365–372, 2009.",
    "K. Lin and K. E. Holbert, “Void diagnostics in liquid-filled pressure "
    "sensing lines,” Progress in Nuclear Energy, vol. 52, no. 5, pp. 503–"
    "511, 2010.",
    "K. Lin and K. E. Holbert, “Pressure sensing line diagnostics in "
    "nuclear power plants,” in Nuclear Power, P. V. Tsvetkov, Ed., chapter "
    "7, pp. 97–122, Sciyo, Rijeka, Croatia, 2010.",
    "K. E. Holbert and B. R. Upadhyaya, “Integrated signal validation "
    "system for nuclear power plants,” Nuclear Technology, vol. 92, no. "
    "3, pp. 411–427, 1990.",
    "R. J. Patton and J. Chen, “Review of parity space approaches to fault "
    "diagnosis,” in Proceedings of the IFAC Fault Detection, Supervision "
    "and Safety for Technical Processes, pp. 65–81, September 1991.",
    "D. G. Luenberger, “Introduction to observers,” IEEE Transactions "
    "on Automatic Control, vol. AC-16, no. 6, pp. 596–602, 1971.",
    "R. N. Clark, “Dedicated observer approach to instrument failure "
    "detection,” in Proceedings of the 18th IEEE Conference on Decision "
    "and Control including the Symposium on Adaptive Processes, pp. "
    "237–241, December 1979.",
    "J. C. Deckert, M. N. Desai, J. J. Deyst, and A. S. Willsky, “F-8 "
    "DFBW sensor failure identification using analytic redundancy,” "
    "IEEE Transactions on Automatic Control, vol. AC-22, no. 5, pp. "
    "795–803, 1977. ·",
    "R. N. Clark and B. Campbell, “Instrument fault detection in a "
    "pressurized water reactor pressurizer,” Nuclear Technology, vol. 56, "
    "no. 1, pp. 23–32, 1982.",
    "A. S. Willsky and H. L. Jones, “A generalized likelihood ratio "
    "approach to state estimation in linear systems subject to abrupt "
    "changes,” in Proceedings of the IEEE Conference on Decision and "
    "Control, pp. 846–853, 1974.",
    "J. L. Tylee, “On-line failure detection in nuclear power plant "
    "instrumentation,” IEEE Transactions on Automatic Control, vol. "
    "AC-28, no. 3, pp. 406–415, 1983.",
    "S. Narasimhan and R. S. H. Mah, “Generalized likelihood ratios "
    "for gross error identification in dynamic processes,” AIChE Journal, "
    "vol. 34, no. 8, pp. 1321–1331, 1988.",
    "K. E. Holbert and H. M. Hashemian, “Instrument calibration "
    "reduction using signal validation,” Transactions of the American "
    "Nuclear Society, vol. 69, pp. 372–373, 1993.",
    "K. E. Holbert and X. Wang, “Power plant diagnostic information "
    "fusion using fuzzy logic,” in Proceedings of the World Automation "
    "Congress Intelligent Automation and Soft Computing, vol. 1, pp. "
    "ISIAC044. 1–ISIAC044. 6, Anchorage, Alaska, USA, May 1998.",
    "X. Wang and K. E. Holbert, “A fuzzy logic enhanced fault diagnostic "
    "system,” in Proceedings of the Maintenance and Reliability "
    "Conference (MARCON ‘97), vol. 2, pp. 92. 01–92. 15, Knoxville, "
    "Tenn, USA, May 1997.",
]


_SUMMARY_VI = (
    "Bảo trì dự báo có thể thực hiện mà không làm gián đoạn vận hành của nhà máy. "
    "Xử lý tín hiệu chịu lỗi dựa trên logic mờ có thể giúp người vận hành nhà máy điện "
    "đạt được mục tiêu vận hành hệ thống phức tạp hiệu quả, hiệu suất cao và an toàn. "
    "Giám sát tình trạng thiết bị dựa trên logic mờ được trình bày nhằm cải thiện khả năng "
    "giám sát và chẩn đoán hiện đại cho các quy trình công nghiệp nói chung. Tính khả thi "
    "của công nghệ này được chứng minh thông qua phân tích dữ liệu cảm biến thu được từ "
    "các hệ thống lò phản ứng đang vận hành. Công nghệ này có nhiều ứng dụng liên ngành "
    "ngoài các nhà máy phát điện, bao gồm nhà máy chế biến hóa chất, đường cao tốc và "
    "tàu vũ trụ/máy bay. Về lâu dài, FLDM có thể được bổ sung một mức độ học trực tuyến "
    "nào đó, có thể được tăng cường bằng dữ liệu nhập từ người vận hành [50, 51]."
)

_SUMMARY_EN = (
    "Predictive maintenance can be achieved without disturbing the plant "
    "operation. Fault-tolerant signal processing based on fuzzy logic can "
    "help power plant operators meet the goal of effective, efficient, and safe "
    "operation of complex systems. Fuzzy logic-based condition monitoring "
    "is described for improving state-of-the-art monitoring and diagnostic "
    "capabilities for general industrial processes. Its feasibility is shown through "
    "the analysis of sensor data obtained from operating reactor systems. Such "
    "technology has multidisciplinary applications besides electric generating "
    "stations, including chemical processing plants, highways, and air/space "
    "craft. In the longer term, FLDM could be provided with some level on "
    "online learning which might be augmented by operator input [50, 51]."
)


def section(lang):
    """Return the bilingual HTML fragments for the Summary and References."""
    b = _Fragments()
    H(b, lang, "Tóm lược", "Summary")
    P(b, lang, _SUMMARY_VI, _SUMMARY_EN)
    H(b, lang, "Tài liệu tham khảo", "References")
    REFS(b, lang, _REFS)
    return b
