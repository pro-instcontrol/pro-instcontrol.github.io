# -*- coding: utf-8 -*-
"""Book 9, Chapter 2 (part C) - Advanced Measuring (Instrumentation)
Methods for Nuclear Installations: A Review (EN/VI bilingual).

Source: L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and
Control* (Bibliotex, 2019), PDF pp. 41-54, printed pp. 25-38: NUCLEAR
ACCIDENT, AFTER ACTION, AND ANALYSIS; CONCLUSIONS; ACKNOWLEDGMENTS;
REFERENCES.  Figures 6 and 7 are redrawn as vectors in `ppicfig2.py`;
captions come from there.
"""

from ppic_common import h2, h3, p, fig, refs, note  # noqa: F401
import ppicfig2 as F


_REFS = [
    "C. Guerrero, E. Berthoumieux, D. Cano-Ott, F. Gunsing, E. Mendoza, "
    "and S. Andriamonje, “A new set-up for the simultaneous measurement of "
    "neutro-induced capture and fission reactions,” in Proceedings of the 2nd "
    "International Conference on Advancements in Nuclear Instrumentation "
    "Measurement Methods and Their Applications (ANIMMA’11), Ghent, "
    "Belgium, June 2011.",
    "I. Bolshakova, V. Chekanov, I. Duran et al., “Methods and "
    "instrumentation for investigating hall sensors during their irradiation "
    "in nuclear research reactors,” in Proceedings of the 1st International "
    "Conference on Advancements in Nuclear Instrumentation, Measurement "
    "Methods and Their Applications (ANIMMA’09), Marseille, France, June 2009.",
    "R. I. Scherpelz and J. E. Tanner, “Neutron measurements at nuclear "
    "power reactors [55],” Nuclear Instruments and Methods in Physics "
    "Research A, vol. 476, no. 1-2, pp. 400–404, 2002.",
    "D. Fourmentel, J.-F. Villard, A. Lyoussi et al., “Combined analysis "
    "of neutron and photon flux measurements for the Jules Horowitz reactor "
    "core mapping,” in Proceedings of the 2nd International Conference on "
    "Advancements in Nuclear Instrumentation, Measurement Methods and Their "
    "Applications (ANIMMA’11), Ghent, Belgium, June 2011.",
    "H. G. Brixy, “Temperature measurement in nuclear reactors by noise "
    "thermometry,” Nuclear Instruments and Methods, vol. 97, no. 1, "
    "pp. 75–80, 1971.",
    "T. Bily and L. Sklenka, “Neutronic design of instrumentation for "
    "thermal effects measurement on VR-1 reactor,” in Proceedings of the 1st "
    "International Conference on Advancements in Nuclear Instrumentation, "
    "Measurement Methods and Their Applications (ANIMMA’09), Marseille, "
    "France, June 2009.",
    "J. L. Rempe, D. L. Knudson, J. E. Daw et al., “Enhanced in-pile "
    "instrumentation at the advanced test reactor,” in Proceedings of the "
    "2nd International Conference on Advancements in Nuclear Instrumentation, "
    "Measurement Methods and Their Applications (ANIMMA’11), Ghent, "
    "Belgium, June 2011.",
    "A. Porta, V. M. Bui, M. Cribier et al., “Reactor neutrino detection "
    "for non-proliferation with the NUCIFER experiment,” IEEE Transactions "
    "on Nuclear Science, vol. 57, no. 5, pp. 2732–2739, 2010.",
    "J. F. Villard, S. Fourrez, D. Fourmentel, and A. Legrand, “Improving "
    "high-temperature measurements in nuclear reactors with Mo/Nb "
    "thermocouples,” International Journal of Thermophysics, vol. 29, no. 5, "
    "pp. 1848–1857, 2008.",
    "G. Cheymol, B. Brichard, and J. F. Villard, “Fibre optics for "
    "metrology in nuclear research reactors applications to dimensional "
    "measurements,” in Proceedings of the 1st International Conference on "
    "Advancements in Nuclear Instrumentation, Measurement Methods and Their "
    "Applications (ANIMMA’09), Marseille, France, June 2009.",
    "G. Y. Buimistriuc and A. M. Rogov, “Intelligent fiber optic "
    "pressure sensor for measurements in extreme conditions,” in Proceedings "
    "of the 1st International Conference on Advancements in Nuclear "
    "Instrumentation, Measurement Methods and Their Applications "
    "(ANIMMA’09), Marseille, France, June 2009.",
    "C. Papastefanou, “Measurement of neutron flux and albedo of water "
    "for thermal neutrons with foils of indium in a subcritical nuclear "
    "reactor,” Journal of Radioanalytical and Nuclear Chemistry, vol. 261, "
    "no. 3, pp. 671–678, 2004.",
    "Y. G. Li, Y. Q. Shi, Y. B. Zhang, and P. Xia, “Reactor fission rate "
    "measurement for miniature neutron source reactor by solid state nuclear "
    "track detector,” Radiation Measurements, vol. 34, no. 1–6, "
    "pp. 589–591, 2001.",
    "M. Laurie, M. A. Fütterer, J. M. Lapetite, S. Fourrez, and R. "
    "MoriceNew, “new temperature monitoring devices for high-temperature "
    "irradiation experiments in the high flux reactor petten,” Nuclear "
    "Science, vol. 58, pp. 2319–2324, 2011.",
    "N. Khentout and B. Meftah, “Design and realization of a measurement "
    "system of cold neutron speeds by TOF method,” in Proceedings of the 1st "
    "International Conference on Advancements in Nuclear Instrumentation, "
    "Measurement Methods and Their Applications (ANIMMA’09), Marseille, "
    "France, June 2009.",
    "A. K. Bhattacharya, J. T. Verdeyen, F. T. Adler, and L. Goldstein, "
    "“Measurement of the local radiation field in a nuclear reactor by "
    "microwave interferometric techniques,” Nuclear Instruments and Methods, "
    "vol. 95, no. 2, pp. 313–325, 1971.",
    "O. Meirav, M. Adam, E. Boaretto et al., “Measurements of 129I in a "
    "nuclear power reactor by accelerator mass spectrometry,” International "
    "Journal of Radiation Applications and Instrumentation A, vol. 43, "
    "no. 11, pp. 1420–1424, 1992.",
    "R. Coulon, S. Normand, G. Ban et al., “Sodium fast reactor power "
    "monitoring using 20F tagging agent,” in Proceedings of the 1st "
    "International Conference on Advancements in Nuclear Instrumentation, "
    "Measurement Methods and Their Applications (ANIMMA’09), Marseille, "
    "France, June 2009.",
    "A. K. Sang, M. E. Froggatt, D. K. Gifford, S. T. Kreger, and B. D. "
    "Dickerson, “One centimeter spatial resolution temperature measurements "
    "in a nuclear reactor using Rayleigh scatter in optical fiber,” IEEE "
    "Sensors Journal, vol. 8, no. 7, pp. 1375–1380, 2008.",
    "L. K. Yarovoi, L. Y. Robur, A. V. Gnatovsky, and E. P. Vdalov, "
    "“holographic equipment for testing the construction of the nuclear "
    "power plant,” in Proceedings of the 4th Regional Meeting, 1997.",
    "S. D. Eastham, D. J. Coates, and G. T. Parks, “A novel method for "
    "rapid comparative quantitative analysis of nuclear fuel cycles,” "
    "Annals of Nuclear Energy, vol. 42, pp. 80–88, 2012.",
    "M. H. Noiré, L. Couston, E. Douarre, D. Pouyat, C. Bouzon, and P. "
    "Marty, “A new sol-gel derived optical fiber sensor for high acidity "
    "measurements: application in nuclear fuel reprocessing,” Journal of "
    "Sol-Gel Science and Technology, vol. 17, no. 2, pp. 131–136, 2000.",
    "I. Matsson, B. Grapengiesser, and B. Andersson, “LOKET-a gamma-ray "
    "spectroscopy system for in-pool measurements of thermal power "
    "distribution in irradiated nuclear fuel,” Nuclear Instruments and "
    "Methods in Physics Research A, vol. 569, no. 3, pp. 872–882, 2006.",
    "L. Viererbl, Z. Lahodová, A. Voljanskij et al., “Measurement of "
    "gamma and neutron radiations inside spent fuel assemblies with passive "
    "detectors,” Nuclear Instruments and Methods in Physics Research A, "
    "vol. 652, no. 1, pp. 90–93, 2011.",
    "M. Battaglieri, R. de Vita, G. Firpo et al., “An anti-neutrino "
    "detector to monitor nuclear reactor’s power and fuel composition,” "
    "Nuclear Instruments and Methods in Physics Research A, vol. 617, "
    "no. 1–3, pp. 209–213, 2010.",
    "P. F. Peck, “Control analysis of 235U in nuclear fuel by a neutron "
    "absorption method,” Journal of Radioanalytical Chemistry, vol. 48, "
    "no. 1-2, pp. 73–82, 1979.",
    "G. Perret and K. A. Jordan, “On the combination of delayed neutron "
    "and delayed gamma techniques for fission rate measurement in nuclear "
    "fuel,” in Proceedings of the 2nd International Conference on "
    "Advancements in Nuclear Instrumentation, Measurement Methods and Their "
    "Applications (ANIMMA’11), Ghent, Belgium, June 2011.",
    "X. Y. Liu, D. A. Andersson, and B. P. Uberuaga, “First-principles "
    "DFT modeling of nuclear fuel materials,” Journal of Materials Science, "
    "vol. 47, no. 21, pp. 7367–7384, 2012.",
    "E. Rosenkrantz, J. Y. Ferrandis, G. Leveque, and D. Baron, "
    "“Ultrasonic measurement of gas pressure and composition for nuclear "
    "fuel rods,” Nuclear Instruments and Methods in Physics Research A, "
    "vol. 603, no. 3, pp. 504–509, 2009.",
    "S. Subbuthai, P. Sahoo, R. Ananthanarayanan, A. Nageswara Rao, and "
    "R. V. Subba Rao, “Feasibility studies for the detection of third phase "
    "during reprocessing of fast reactor fuel,” Journal of Radioanalytical "
    "and Nuclear Chemistry, vol. 291, no. 2, pp. 879–883, 2012.",
    "T. Kamei and A. Serizawa, “Measurement of 2-dimensional local "
    "instantaneous liquid film thickness around simulated nuclear fuel rod "
    "by ultrasonic transmission technique,” Nuclear Engineering and Design, "
    "vol. 184, no. 2-3, pp. 349–362, 1998.",
    "T. Inoue, “Actinide recycling by pyro-process with metal fuel FBR "
    "for future nuclear fuel cycle system,” Progress in Nuclear Energy, "
    "vol. 40, no. 3-4, pp. 547–554, 2002.",
    "S. Normand, V. Kondrasov, G. Corre, and C. Passard, “PING: a new "
    "approach for nuclear fuel cycle instrumentation,” in Proceedings of the "
    "1st International Conference on Advancements in Nuclear Instrumentation, "
    "Measurement Methods and Their Applications (ANIMMA’09), Marseille, "
    "France, June 2009.",
    "I. Badawy and W. A. EI-Gammal, “Measurement of low enriched uranium "
    "fuel pellets,” in Proceedings of the 16th National Conference on Radio "
    "Science, Cairo, Egypt, February 1999.",
    "A. Gavron, L. E. Smith, and J. J. Ressler, “Analysis of spent fuel "
    "assemblies using a lead slowing down spectrometer,” Nuclear Instruments "
    "and Methods in Physics Research A, vol. 602, no. 2, pp. 581–587, 2009.",
    "S. K. Das, C. S. Kedari, and S. C. Tripathi, “Spectrophotometric "
    "determination of trace amount of uranium (VI) in different aqueous and "
    "organic streams of nuclear fuel processing using "
    "2-(5-bromo-2-pyridylazo-5-diethylaminophenol),” Journal of "
    "Radioanalytical and Nuclear Chemistry, vol. 285, no. 3, pp. 675–681, 2010.",
    "A. I. Hawari, J. Chen, B. J. Su, and Z. X. Zhao, “Assessment of "
    "on-line burnup monitoring of pebble bed reactor fuel using passive "
    "gamma-ray spectrometry,” IEEE Transactions on Nuclear Science, "
    "vol. 49, no. 3, pp. 1249–1253, 2002.",
    "U. Meier, J. Heinze, L. Lange, C. Hassa, L. Rackwitz, and T. Doerr, "
    "“Characterisation of the combustion performance of low emission fuel "
    "injectors with laser measurements,” CEAS Aeronautical Journal, vol. 3, "
    "no. 1, pp. 45–53, 2012.",
    "A. P. Belian, L. C. Bourva, S. C. Kane, and A. R. Lebrun, “The use "
    "of Monte Carlo techniques for the calibration of IAEA safeguards "
    "instrumentation,” in Proceedings of the 1st International Conference on "
    "Advancements in Nuclear Instrumentation, Measurement Methods and Their "
    "Applications (ANIMMA’09), Marseille, France, June 2009.",
    "N. Peter, M. Koskelo, and M. Stein, “The role of the nuclear "
    "industry in advancing safeguards instrumentation,” in Proceedings of "
    "the 1st International Conference on Advancements in Nuclear "
    "Instrumentation, Measurement Methods and Their Applications "
    "(ANIMMA’09), Marseille, France, June 2009.",
    "A. M. Lafleur, W. S. Charlton, H. O. Menlove, and M. T. Swinhoe, "
    "“Comparison of fresh fuel experimental measurements to MCNPX "
    "calculations using self-interrogation neutron resonance densitometry,” "
    "Nuclear Instruments and Methods in Physics Research A, vol. 680, "
    "pp. 168–178, 2012.",
    "L. V. East, E. R. Martin, T. L. Atwell, R. H. Augustson, and H. O. "
    "Menlove, “Automated nondestructive assay instrumentation for nuclear "
    "materials safeguards,” Nuclear Science, vol. 22, no. 1, pp. 739–743, 1975.",
    "C. Willman, A. Håkansson, O. Osifo, A. Bäcklin, and S. J. Svärd, "
    "“Nondestructive assay of spent nuclear fuel with gamma-ray "
    "spectroscopy,” Annals of Nuclear Energy, vol. 33, no. 5, pp. 427–438, 2006.",
    "A. K. Khusainov, T. A. Antonova, V. V. Lysenko et al., “High "
    "resolution, portable gamma spectrometer not requiring liquid nitrogen "
    "cooling for field use for nuclear security and safeguards applications,” "
    "in Proceedings of the Nuclear Science Symposium Conference, Dresden, "
    "Germany, October 2008.",
    "M. Swoboda, R. Arlt, V. Gostilo et al., “Spectral gamma detectors "
    "for hand-held radioisotope identification devices (RIDs) for nuclear "
    "security applications,” in Proceedings of the Nuclear Science "
    "Symposium, Medical Imaging Conference, Symposium on Nuclear Power "
    "Systems and the 14th International Workshop on Room Temperature "
    "Semiconductor X- and Gamma-Ray Detectors, pp. 4296–4302, Rome, Italy, "
    "October 2004.",
    "D. H. Beddingfield, A. Beyerle, P. A. Russo, K. Ianakiev, D. T. Vo, "
    "and V. Dmitrenko, “High-pressure xenon ion chambers for gamma-ray "
    "spectroscopy in nuclear safeguards,” Nuclear Instruments and Methods in "
    "Physics Research A, vol. 505, no. 1-2, pp. 474–477, 2003.",
    "T. F. Wang, S. M. Horne, R. A. Henderson, K. E. Roberts, and D. K. "
    "Vogt, “Exploring simultaneous single and coincident gamma-ray "
    "measurements for U/Pu assay in safeguards,” in Proceedings of the 2nd "
    "International Conference on Advancements in Nuclear Instrumentation, "
    "Measurement Methods and Their Applications (ANIMMA’11), Ghent, "
    "Belgium, June 2011.",
    "M. Marseguerra, E. Padovani, and S. A. Pozzi, “Use of the MCNP-"
    "Polimi code for time-correlation safeguards measurements,” Progress in "
    "Nuclear Energy, vol. 43, no. 1–4, pp. 305–311, 2003.",
    "S. A. Pozzi and J. Segovia, “ 252Cf source-correlated transmission "
    "measurements and genetic programming for nuclear safeguards,” Nuclear "
    "Instruments and Methods in Physics Research A, vol. 491, no. 1-2, "
    "pp. 326–341, 2002.",
    "P. Vermaercke, F. F. Arboccò, L. Sneyers, A. Leal, and M. "
    "Bruggeman, “Environmental monitoring for safeguards using "
    "k0-standardised neutron activation analysis,” in Proceedings of the "
    "1st International Conference on Advancements in Nuclear Instrumentation, "
    "Measurement Methods and Their Applications (ANIMMA’09), Marseille, "
    "France, June 2009.",
    "T. L. Frazzini, “Application of automated analytical instrumentation "
    "to the determination of uranium and plutonium for nuclear safeguards "
    "measurements,” IEEE Transactions on Nuclear Science, vol. 29, no. 1, "
    "pp. 866–868, 1981.",
    "Thomas H. Smith, Ronald J. Hall, and L. Donald Williams, “Analytic "
    "methods for fuel-cycle safety studies,” IEEE Transactions on "
    "Reliability, vol. R-25, no. 3, pp. 184–190, 1976.",
    "L. Lu and J. Jiang, “Probabilistic safety assessment for "
    "instrumentation and control systems in nuclear power plants: an "
    "overview,” Journal of Nuclear Science and Technology, vol. 41, no. 3, "
    "pp. 323–330, 2004.",
    "P. E. Fehlaul, “Integrated neutrod gamma-ray portal monitors for "
    "nuclear safeguards,” Nuclear Science, vol. 41, no. 4, pp. 922–926, 1994.",
    "A. Letourneau, V.-M. Bui, M. Cribier et al., “Nucifer: a small "
    "electron-antineutrino detector for fundamental and safeguard studies,” "
    "in 2nd International Conference on Advancements in Nuclear "
    "Instrumentation, Measurement Methods and Their Applications "
    "(ANIMMA’11), Ghent, Belgium, June 2011.",
    "R. Baskaran, V. Subramanian, J. Misra, R. Indira, P. Chellapandi, "
    "and B. Raj, “Aerosol characterization and measurement techniques "
    "towards SFR safety studies,” in Proceedings of the 1st International "
    "Conference on Advancements in Nuclear Instrumentation, Measurement "
    "Methods and Their Applications (ANIMMA’09), Marseille, France, June 2009.",
    "B. Cabrera-Palmer, D. Reyna, L. Sadler et al., “Advances towards "
    "readily deployable antineutrino detectors for reactor monitoring and "
    "safeguards,” in Proceedings of the 1st International Conference on "
    "Advancements in Nuclear Instrumentation, Measurement Methods and Their "
    "Applications (ANIMMA’09), Marseille, France, June 2009.",
    "B. B. Parsons and J. L. Wells, “Tamper and radiation resistant "
    "instrumentation for safeguarding special nuclear material,” IEEE "
    "Transactions on Nuclear Science, vol. NS-24, no. 1, pp. 616–620, 1976.",
    "S. H. Lee, Y. G. No, M. G. Na, K. I. Ahn, and S. Y. Park, "
    "“Diagnostics of loss of coolant accidents using SVC and GMDH models,” "
    "IEEE Transactions on Nuclear Science, vol. 58, no. 1, pp. 267–276, 2011.",
    "M. Große, M. Steinbrück, J. Stuckert, A. Kastner, and B. "
    "Schillinger, “Application of neutron radiography to study material "
    "processes during hypothetical severe accidents in nuclear reactors,” "
    "Journal of Materials Science, vol. 47, no. 18, pp. 6505–6512, 2012.",
    "M. G. Na, W. S. Park, and D. H. Lim, “Detection and diagnostics of "
    "loss of coolant accidents using support vector machines,” IEEE "
    "Transactions on Nuclear Science, vol. 55, no. 1, pp. 628–636, 2008.",
    "M. G. Na, S. H. Shin, S. M. Lee et al., “Prediction of major "
    "transient scenarios for severe accidents of nuclear power plants,” IEEE "
    "Transactions on Nuclear Science, vol. 51, no. 2, pp. 313–321, 2004.",
    "W. K. Lu and B. Zhao, “Preliminary evaluation of the effect of "
    "several management measures for the station blackout severe accident of "
    "the pressurized water reactor nuclear power plant,” in Proceedings of "
    "the International Conference on Information Systems for Crisis Response "
    "and Management (ISCRAM’11), pp. 455–460, Harbin, China, November 2011.",
    "D. Patterson, “Application of a computerised alarm-analysis system "
    "to a nuclear power station,” Electrical Engineers, vol. 115, no. 12, "
    "pp. 1858–1864, 1968.",
    "S. W. Cheon, S. H. Chang, H. Y. Chung, and Z. N. Bien, “Application "
    "of neural networks to multiple alarm processing and diagnosis in nuclear "
    "power plants,” IEEE Transactions on Nuclear Science, vol. 40, no. 1, "
    "pp. 11–20, 1993.",
    "S. S. Choi, K. S. Kang, H. G. Kim, and S. H. Chang, “Development of "
    "an on-line fuzzy expert system for integrated alarm processing in "
    "nuclear power plants,” IEEE Transactions on Nuclear Science, vol. 42, "
    "no. 4, pp. 1406–1418, 1995.",
    "S. W. Cheon, S. H. Chang, and H. Y. Chung, “Development strategies "
    "of an expert system for multiple alarm processing and diagnosis in "
    "nuclear power plants,” IEEE Transactions on Nuclear Science, vol. 40, "
    "no. 1, pp. 21–30, 1993.",
    "G. Ducros, S. Bernard, M. P. Ferroud-Plattet, and O. Ichim, “Use of "
    "gamma spectrometry for measuring fission product releases during a "
    "simulated PWR severe accident: application to the VERDON experimental "
    "program,” in Proceedings of the 1st International Conference on "
    "Advancements in Nuclear Instrumentation, Measurement Methods and Their "
    "Applications (ANIMMA’09), Marseille, France, June 2009.",
    "K. Mitev, R. T. sibranski, V. Avramov et al., “Measurements of 133I, "
    "134Cs and 137Cs In environmental samples in Bulgaria after the Fukushima "
    "accident,” in Proceedings of the Nuclear Science Symposium and Medical "
    "Imaging Conference, Valencia, Spain, October 2011.",
    "S. Endo, S. Kimura, T. Takatsuji, K. Nanasawa, T. Imanaka, and K. "
    "Shizuma, “Measurement of soil contamination by radionuclides due to the "
    "Fukushima Dai-ichi nuclear power plant accident and associated estimated "
    "cumulative external dose estimation,” Journal of Environmental "
    "Radioactivity, vol. 111, pp. 18–27, 2012.",
    "H. Amano, M. Akiyama, B. Chunlei et al., “Radiation measurements in "
    "the Chiba Metropolitan Area and radiological aspects of fallout from the "
    "Fukushima Dai-ichi nuclear power plants accident,” Journal of "
    "Environmental Radioactivity, vol. 111, pp. 42–52, 2012.",
    "F. Perrot, P. Hubert, C. Marquet et al., “Evidence of 131I and "
    "134,137Cs activities in Bordeaux, France due to the Fukushima nuclear "
    "accident,” Journal of Environmental Radioactivity, vol. 114, pp. 61–65, 2012.",
    "M. Paul, D. Fink, G. Hollos, A. Kaufman, W. Kutschera, and M. "
    "Magaritz, “Measurement of 129I concentrations in the environment after "
    "the Chernobyl reactor accident,” Nuclear Instruments and Methods in "
    "Physics Research B, vol. 29, no. 1-2, pp. 341–345, 1987.",
    "J. Gasparro, M. Hult, K. Komura et al., “Measurements of 60Co in "
    "spoons activated by neutrons during the JCO criticality accident at "
    "Tokai-mura in 1999,” Journal of Environmental Radioactivity, vol. 73, "
    "no. 3, pp. 307–321, 2004.",
    "V. A. Nikolaev, “Application of SSNTDs to investigations of "
    "radiation accident after-effects,” Radiation Measurements, vol. 25, "
    "no. 1–4, pp. 337–345, 1995.",
    "C. Bernhardsson, I. Zvonova, C. Rääf, and S. Mattsson, "
    "“Measurements of long-term external and internal radiation exposure of "
    "inhabitants of some villages of the Bryansk region of Russia after the "
    "Chernobyl accident,” Science of the Total Environment, vol. 409, no. 22, "
    "pp. 4811–4817, 2011.",
]


def section(lang):
    """Return the bilingual HTML chunks for this part of Chapter 2."""
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def FIG(n):
        b.append(fig(n, getattr(F, "fig_f2%d" % n)()))

    # --------------------------- NUCLEAR ACCIDENT, AFTER ACTION, AND ANALYSIS
    H("TAI NẠN HẠT NHÂN, HẬU XỬ LÝ VÀ PHÂN TÍCH",
      "NUCLEAR ACCIDENT, AFTER ACTION, AND ANALYSIS")
    P(
        "Tai nạn hạt nhân là điều rùng rợn đối với nhân loại, vì vậy chúng "
        "ta cần tích cực ngăn ngừa tai nạn hạt nhân và phân tích thiệt hại "
        "do tai nạn hạt nhân gây ra. Có nhiều thiết bị và phương pháp đo "
        "lường khác nhau được dùng để chẩn đoán điều kiện sự cố, giám sát "
        "và báo động thiết bị hạt nhân trong điều kiện sự cố, và phân tích "
        "tai nạn hạt nhân. Các phương pháp thiết bị và đo lường gồm Phân loại "
        "Vectơ Hỗ trợ (SVC), Phương pháp Nhóm xử lý Dữ liệu (GMDH), Máy Vectơ "
        "Hỗ trợ (SVM), Hồi quy Vectơ Hỗ trợ (SVR), Mạng nơ-ron Xác suất "
        "(PNN), Thuật toán Mạng Lan truyền Ngược (BPNA), Hệ thống Lọc và "
        "Chẩn đoán Báo động (AFDS), Phổ kế Gamma (GS), Phổ kế Khối lượng "
        "Gia tốc (AMS), Đầu dò Vết Hạt nhân Thể rắn (SSNTD), v.v.",
        "Nuclear accident is bloodcurdling for humanity, so we should "
        "positively prevent the nuclear accidents and analyse the damage "
        "caused by nuclear accident. There are different measuring devices "
        "and methods used for diagnosing accidental conditions, monitoring "
        "and alarming of nuclear equipment in accidental conditions, and "
        "analysis of nuclear accident. Instruments and measurements methods "
        "consist of Support Vector Classification (SVC), Group Method of "
        "Data Handling (GMDH), Support Vector Machines (SVM), Support Vector "
        "Regression (SVR), Probabilistic Neural Network (PNN), Back "
        "Propagation Network Algorithm (BPNA), Alarm Filtering and "
        "Diagnostic System (AFDS), Gamma Spectrometry (GS), Accelerator Mass "
        "Spectrometry (AMS), Solid State Nuclear Track Detectors (SSNTD), "
        "and so forth."
    )
    P(
        "Là một biện pháp quản lý hiệu quả các tai nạn nghiêm trọng tại nhà "
        "máy điện hạt nhân, việc xác định và chẩn đoán các sự kiện khởi phát "
        "tai nạn trong một khoảng thời gian ngắn là rất quan trọng [59]. "
        "Mục tiêu chính của nhiều hệ thống là chẩn đoán Sự cố Mất chất làm "
        "mát (LOCA) sử dụng các kỹ thuật trí tuệ nhân tạo như GMDH và SVC. "
        "Chụp chiếu neutron (NR) đã được áp dụng để nghiên cứu hành vi của "
        "thanh điều khiển và vỏ bọc nhiên liệu hạt nhân trong quá trình oxy "
        "hóa bằng hơi nước ở nhiệt độ giữa 1123 và 1673 K trong điều kiện "
        "tai nạn hạt nhân nghiêm trọng [60]. Các người vận hành nhà máy điện "
        "hạt nhân chỉ được cung cấp thông tin một phần trong suốt tai nạn, "
        "hoặc họ có thể không có đủ thời gian để phân tích dữ liệu dù được "
        "cung cấp lượng thông tin đáng kể, nên rất khó cho người vận hành "
        "dự đoán diễn biến của LOCA.",
        "As a means of effectively managing severe accidents at nuclear "
        "power plants, it is important to identify and diagnose accident "
        "initiating events within a short time interval [59]. The main "
        "objective of many systems was the diagnosis of the Loss of Coolant "
        "Accidents (LOCA) which uses artificial intelligence techniques, "
        "such as GMDH and SVC. Neutron Radiography (NR) was applied for "
        "investigations of control rod behaviour and nuclear fuel cladding "
        "during steam oxidation at temperatures between 1123 and 1673 K "
        "under severe nuclear accident conditions [60]. Nuclear plant "
        "operators are provided with only partial information during the "
        "accident or they may have insufficient time to analyze the data "
        "despite being provided with considerable information, so it is very "
        "difficult for operators to predict the progression of LOCA."
    )
    P(
        "Na và cộng sự đã dùng SVM để xác định vị trí vỡ của LOCA và dự đoán "
        "kích thước vết vỡ bằng SVC và SVR [61]. Na và cộng sự thiết kế một "
        "PNN đã được áp dụng hiệu quả cho các bài toán phân loại nhằm phân "
        "loại tai nạn thành các nhóm sự kiện ban đầu như LOCA, Mất điện "
        "toàn bộ trạm (SBO), Mất hoàn toàn nước cấp (TLOFW), và Vỡ ống sinh "
        "hơi (SGTR). Họ cũng thiết kế một Mạng nơ-ron Mờ (FNN) để nhận diện "
        "các kịch bản tai nạn nghiêm trọng chính sau các sự kiện khởi phát "
        "[62]. Sơ đồ được thể hiện trong Hình 6.",
        "Na et al. used SVM to identify the break location of an LOCA and "
        "predict the break size using the SVC and SVR [61]. Na et al. "
        "designed a PNN that has been applied well to the classification "
        "problems in order to classify accidents into groups of original "
        "events such as LOCA, Station Blackout (SBO), Total Loss of "
        "Feedwater (TLOFW), and Steam Generator Tube Rupture (SGTR). They "
        "also designed a Fuzzy Neural Network (FNN) to identify their major "
        "serious accident scenarios after the initiating events [62]. The "
        "sketch is shown in Figure 6."
    )
    FIG(6)
    P(
        "Gần đây, tai nạn Fukushima cho thấy Mất điện toàn bộ trạm (SBO) là "
        "nguyên nhân quan trọng gây tai nạn nghiêm trọng hư hại lõi và phát "
        "thải phóng xạ [63]. Patterson và Sc đã mô tả phân tích báo động gọi "
        "là Hệ thống Máy tính Kỹ thuật số (DCS), được lắp đặt và hiện đang "
        "vận hành tại lò phản ứng điện hạt nhân Oldbury [64]. Cheon và cộng "
        "sự báo cáo nghiên cứu khả thi của hệ thống xử lý và chẩn đoán đa "
        "báo động dùng Mạng nơ-ron (NNs) [65]. BPNA được áp dụng để huấn "
        "luyện các mẫu báo động đa dạng nhằm nhận diện hư hỏng trong hệ thống "
        "Bơm nước làm mát lò phản ứng (RCP). Khả năng ánh xạ tổng quát của NN "
        "cho phép nhận diện hư hỏng dễ dàng. Một hệ thống chuyên gia mờ trực "
        "tuyến gọi là AFDS đã được mô tả nhằm cung cấp cho người vận hành "
        "hình ảnh báo động sống động và thông tin hư hỏng rộng khắp của hệ "
        "thống trong các trạng thái bất thường thông qua chẩn đoán và lọc "
        "báo động [66]. Cheon và cộng sự mô tả chiến lược phát triển của một "
        "hệ thống chuyên gia nguyên mẫu gọi là Hệ thống Chuyên gia cho Chẩn "
        "đoán và Xử lý Đa báo động (ESMADP) để chẩn đoán và xử lý đa báo động "
        "trong nhà máy điện hạt nhân [67]. Sơ đồ được thể hiện trong Hình 7. "
        "Hệ thống này được thiết kế để hỗ trợ người vận hành chẩn đoán sự cố "
        "nhà máy điện hạt nhân và nhanh chóng xác định một báo động nguyên "
        "nhân chi phối trong số nhiều báo động được kích hoạt.",
        "Recently, the Fukushima accident showed the Station Blackout (SBO) "
        "is an important cause of core damage severe accident and "
        "radiological releases [63]. Patterson and Sc described the alarm "
        "analysis called Digital Computer System (DCS) which has been "
        "installed and is now operating in nuclear power reactor at Oldbury "
        "[64]. Cheon et al. reported the feasibility study of multiple alarm "
        "diagnosis and processing system using Neural Networks (NNs) [65]. "
        "The BPNA is applied to the training of multiple alarm patterns for "
        "the identification of faults in a Reactor Coolant Pump (RCP) system. "
        "The general mapping capability of the NN enables to identify a "
        "fault easily. An on-line fuzzy expert system, called AFDS, was "
        "described to provide the operators with vivid alarm photograph and "
        "system extensive failure information during anomalous states "
        "through alarm diagnosis and filtering [66]. Cheon et al. described "
        "the development strategies of a prototype expert system, called "
        "Expert System for Multiple Alarm Diagnosis and Processing (ESMADP) "
        "for multiple alarm diagnosis and processing in nuclear power plants "
        "[67]. The sketch is shown in Figure 7. This system is designed to "
        "assist operators to diagnose the nuclear power plant malfunction "
        "and to identify a dominating causal alarm among multiple fired "
        "alarms quickly."
    )
    FIG(7)
    P(
        "Sự phát thải các Sản phẩm Phân hạt (FPs) đóng vai trò then chốt "
        "trong nguồn phát thải ra môi trường; sự phát thải FP từ Lò phản ứng "
        "nước áp lực (PWR) trong một tai nạn nghiêm trọng giả định là mục "
        "tiêu chính trong đánh giá an toàn lò phản ứng hạt nhân. Phổ kế "
        "gamma là công cụ chính dùng để định lượng sự phát thải FP ra môi "
        "trường. Ducros và cộng sự áp dụng thiết bị phổ kế gamma trực tuyến "
        "để nghiên cứu mẫu nhiên liệu và đo động học phát thải FP trong các "
        "thí nghiệm, cùng với bàn quét gamma chuyên tính toán cân bằng FP sau "
        "thử nghiệm [68]. Mitev và cộng sự báo cáo kết quả đo 131I, 134Cs và "
        "137Cs trong các mẫu môi trường sau tai nạn Fukushima tại Bulgaria "
        "[69]. Các phép đo được thực hiện bằng lấy mẫu không khí thể tích "
        "lớn trên bộ lọc sol khí bằng sợi thủy tinh; kết quả cho thấy nồng "
        "độ 131I nằm trong khoảng 31–2240 ut Bq/m3, nồng độ 134Cs và 137Cs "
        "lần lượt nằm trong khoảng 33–456 ut Bq/m3 và 38–637 ut Bq/m3. Ngoài "
        "ra, Endo và cộng sự tiến hành lấy mẫu đất ở giai đoạn sớm của tai "
        "nạn Nhà máy điện hạt nhân Fukushima Dai-ichi (FDNPP) [70]. Họ dùng "
        "đầu dò Ge để xác định và đo các chất ô nhiễm phóng xạ trong đất gồm "
        "129mTe, 129Te, 131I, 132Te, 132I, 134Cs, 136Cs, 137Cs, 140Ba và "
        "140La. Kết quả cho thấy một lượng lớn chất phóng xạ đã được thải ra "
        "môi trường sau tai nạn hạt nhân Fukushima. Amano và cộng sự thu "
        "thập mẫu không khí và nước máy hàng ngày ngay sau sự cố hạt nhân "
        "Fukushima và đo độ phóng xạ của chúng bằng phổ kế gamma [71]. Perrot "
        "và cộng sự thực hiện các phép đo phổ kế gamma nền thấp về hoạt độ "
        "của 137Cs, 131I và 134I bằng đầu dò HPGe tại nền tảng prisma đặt "
        "tại phòng thí nghiệm Centre d'Etudes Nucléaires de Bordeaux "
        "Gradignan (CENBG) ở Bordeaux, Pháp [72].",
        "The release of Fission Products (FPs) plays a critical role in the "
        "source term of the environment FP from a Pressurized Water Reactor "
        "(PWR) during a hypothetical severe accident is a major target in "
        "nuclear reactor safety assessment. Gamma spectrometry is the main "
        "tool used to quantify FP releases from environment. Ducros et al. "
        "applied the on-line gamma spectrometry equipment to investigate "
        "fuel samples and measure FP release kinetics during the experiments, "
        "and the gamma scanning bench devoted to calculate the FP balances "
        "after the test [68]. Mitev et al. reported the results from "
        "measurements of 131I, 134Cs, and 137Cs of environmental samples "
        "after the Fukushima accident in Bulgaria [69]. Measurements were "
        "performed by high volume air sampling on glass fiber aerosol "
        "filters the consequence showed 131I concentrations are in the range "
        "of 31–2240 ut Bq/m3, 134Cs and 137Cs concentrations are in the range "
        "of 33–456 ut Bq/m3 and 38–637 ut Bq/m3, respectively. Also, Endo et "
        "al. carried out soil sampling consequence at an early stage of the "
        "Fukushima Dai-ichi Nuclear Power Plant (FDNPP) accident [70]. They "
        "used Ge detector to identify and measure radioactive contaminants "
        "in soil including 129mTe, 129Te, 131I, 132Te, 132I, 134Cs, 136Cs, "
        "137Cs, 140Ba, and 140La. The consequence showed large amounts of "
        "radioactive substances were released into the environment after the "
        "Fukushima nuclear accident. Amano et al. collected daily samples of "
        "air and tap water starting directly after the Fukushima nuclear "
        "incident and measured their radioactivity by gamma spectrometry "
        "[71]. Perrot et al. performed the low background gamma spectrometry "
        "measurements 137Cs, 131I and 134I activities with HPGe detectors at "
        "the prisma platform located at the Centre d'Etudes Nucléaires de "
        "Bordeaux Gradignan (CENBG) laboratory in Bordeaux, France [72]."
    )
    P(
        "Tai nạn lò phản ứng hạt nhân Chernobyl xảy ra ngày 26 tháng 4 năm "
        "1986 được biết đến rộng rãi là đã đưa một loạt lượng lớn nuclide "
        "phóng xạ vào khí quyển. Paul và cộng sự đo nồng độ của nuclide "
        "phóng xạ sống lâu 129I trong các mẫu môi trường thu thập tại Israel "
        "và châu Âu sau tai nạn lò phản ứng hạt nhân [73]. Các phép đo được "
        "thực hiện bằng Máy gia tốc Pelletron Rehovot (RPA) và Phổ kế Khối "
        "lượng Gia tốc (AMS). Gasparro và cộng sự mô tả các phép đo quang phổ "
        "tia γ thực hiện tại một loạt phòng thí nghiệm ngầm nhằm mục đích "
        "đo 60Co hơn 2 năm sau sự kiện tới hạn của lò phản ứng hạt nhân "
        "Chernobyl [74]. Kết quả đo cho thấy thông lượng neutron xác định từ "
        "hoạt độ của 60Co phù hợp với các phép đo trước đó dùng các nuclide "
        "phóng xạ sống ngắn 59Fe và 51Cr. Nikolaev áp dụng nhiều phương pháp "
        "và thiết bị vết để nghiên cứu diễn biến sau các tai nạn bức xạ tại "
        "lò phản ứng hạt nhân Chernobyl. Họ dùng SSNTD để đo nhiễm bẩn trong "
        "không khí, nước, đất, đối tượng sinh học và các đối tượng khác của "
        "các nuclide phóng xạ tia α, cũng như để ước tính liều neutron bằng "
        "liều kế sự cố [75]. Ngoài ra, Bernhardsson và cộng sự thảo luận về "
        "sự biến đổi và khác biệt của phơi nhiễm bức xạ bên trong và bên "
        "ngoài của cư dân một số ngôi làng ở vùng Bryansk của Nga gần "
        "Chernobyl [76].",
        "The Chernobyl nuclear reactor accident which occurred on April 26, "
        "1986 is well known to have injected into the atmosphere a pulse of "
        "a large number of radionuclides. Paul et al. measured the "
        "concentrations of the long-lived radionuclide 129I in environmental "
        "samples collected in Israel and Europe after the nuclear reactor "
        "accident [73]. The measurements were performed by Rehovot Pelletron "
        "Accelerator (RPA) and Accelerator Mass Spectrometry (AMS). Gasparro "
        "et al. described γ-ray spectrometry measurements undertaken in a "
        "range of underground laboratories for the purpose of measuring 60Co "
        "more than 2 years after the Chernobyl nuclear reactor criticality "
        "event [74]. The measurements consequence showed that neutron fluence "
        "determined from 60Co activity is in agreement with previous "
        "measurements using the short-lived radionuclides 59Fe and 51Cr. "
        "Nikolaev applied many track methods and devices to investigate the "
        "conduct after Chernobyl nuclear reactor radiation accidents. They "
        "used SSNTD for the measurements of contamination in air, water, "
        "soil, biological and other objects of α-ray radionuclides, as well "
        "as for estimation of neutron doses by means of accident dosimeters "
        "[75]. In addition, Bernhardsson et al. discussed the variations and "
        "differences of the internal and external radiation exposure of the "
        "inhabitants of several villages in the Bryansk region of Russia "
        "nearby Chernobyl [76]."
    )

    # ------------------------------------------------------------ CONCLUSIONS
    H("KẾT LUẬN", "CONCLUSIONS")
    P(
        "Trong bài báo này, các phương pháp đo lường tiên tiến và thiết bị "
        "đo lường cho các cơ sở hạt nhân được xem xét. Việc phát triển các "
        "phương pháp đo lường (thiết bị đo) cho các cơ sở hạt nhân và các "
        "ứng dụng của những thiết bị và phương pháp này được trình bày. "
        "Nhiều thiết bị và phương pháp đo lường được dùng trong mọi mặt của "
        "công nghệ hạt nhân, cụ thể là lò phản ứng điện hạt nhân, chu trình "
        "nhiên liệu hạt nhân, kiểm soát hạt nhân và an ninh quốc gia, tai nạn "
        "hạt nhân, hậu xử lý và phân tích, được thảo luận chi tiết. Các thiết "
        "bị chủ yếu gồm mọi loại đầu dò, nhiệt kế, bộ đếm, cặp nhiệt điện, "
        "máy quang phổ, cảm biến sợi quang, buồng đo và calo kế. Các phương "
        "pháp đo lường chủ yếu gồm nhiều phương pháp đo không tiếp xúc dựa "
        "trên quang học, điện tử và từ tính.",
        "In this paper, the advanced measurement methods and instrumentation "
        "for nuclear installations are reviewed. The development of the "
        "measuring (instrumentation) methods for nuclear installations and "
        "the applications of these instruments and methods are presented. "
        "Various instruments and measurement methods used in all aspects of "
        "nuclear technology, that is, nuclear power reactors, nuclear fuel "
        "cycle, safeguards and homeland security, nuclear accident, after "
        "action, and analysis, are discussed in detail. The instruments "
        "mainly include all kinds of detectors, thermometers, counters, "
        "thermocouples, spectrometers, fiber sensors, chambers, and "
        "calorimeter. The measurement methods mostly consist of various "
        "noncontact measurement methods based on optics, electrons, and "
        "magnetics."
    )

    # --------------------------------------------------------- ACKNOWLEDGMENTS
    H("LỜI CẢM ƠN", "ACKNOWLEDGMENTS")
    P(
        "Công trình này được hỗ trợ bởi Quỹ Khoa học Tự nhiên Quốc gia Trung "
        "Quốc (11272368), bởi Dự án Quỹ Khoa học Tự nhiên của CQ CSTC "
        "(2010BB2087), và bởi Dự án Quỹ Khoa học Tự nhiên của Ủy ban Giáo dục "
        "Trùng Khánh (CQEC, KJ110822).",
        "This work was supported by the National Natural Science Foundation "
        "of China (11272368), by the Natural Science Foundation Project of "
        "CQ CSTC (2010BB2087), and by the Natural Science Foundation Project "
        "of Chongqing Education Commission (CQEC, KJ110822)."
    )

    # --------------------------------------------------------------- REFERENCES
    H("TÀI LIỆU THAM KHẢO", "REFERENCES")
    b.append(refs(_REFS))

    return b
