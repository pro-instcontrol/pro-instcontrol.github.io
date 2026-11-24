# -*- coding: utf-8 -*-
"""Book 9, Chapter 2 (part B) - Advanced Measuring (Instrumentation)
Methods for Nuclear Installations: A Review (EN/VI bilingual).

Source: L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and
Control* (Bibliotex, 2019), PDF pp. 35-41, printed pp. 19-25: NUCLEAR FUEL
CYCLE and SAFEGUARDS AND HOMELAND SECURITY.  Figures 4 and 5 are redrawn as
vectors in `ppicfig2.py`; captions come from there.
"""

from ppic_common import h2, h3, p, fig  # noqa: F401
import ppicfig2 as F


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

    # ------------------------------------------------------- NUCLEAR FUEL CYCLE
    H("CHU TRÌNH NHIÊN LIỆU HẠT NHÂN", "NUCLEAR FUEL CYCLE")

    # ------------------------------ Nuclear Fuel Cycle Instrumentation
    H("Thiết bị đo lường trong chu trình nhiên liệu hạt nhân",
      "Nuclear Fuel Cycle Instrumentation", h3)
    P(
        "Chu trình nhiên liệu hạt nhân gồm các bước ở giai đoạn đầu (front end), "
        "đó là chuẩn bị nhiên liệu; các bước trong giai đoạn khai thác, trong đó "
        "nhiên liệu được sử dụng trong quá trình vận hành lò phản ứng; và các "
        "bước ở giai đoạn cuối (back end), cần thiết để quản lý, chứa đựng an "
        "toàn và tái chế hoặc xử lý nhiên liệu hạt nhân đã qua sử dụng. Các "
        "thiết bị đo lường có thể đo quá trình tái chế nhiên liệu hạt nhân, "
        "nhiên liệu hạt nhân trong bể, cụm nhiên liệu đã chiếu xạ, thông lượng "
        "tích phân theo năng lượng tuyệt đối và phổ năng lượng của phản "
        "neutrino được phát ra, với cảm biến sợi quang được áp dụng, đầu dò "
        "germani độ phân giải cao, liều kế alanine và phổ năng lượng.",
        "The nuclear fuel cycle consists of steps in the front end, which are "
        "the preparation of the fuel, steps in the service period, in which the "
        "fuel is used during reactor operation, and steps in the back end, "
        "which are necessary to safely manage, contain, and either reprocess or "
        "dispose of spent nuclear fuel. The instrumentations can measure nuclear "
        "fuel reprocessing, nuclear fuel in-pool, spent fuel assembly, the "
        "absolute energy-integrated flux and the energy spectrum of anti-neutrinos "
        "emitted adopted optical fiber sensor, high-resolution germanium "
        "detector, alanine dosimeters, and energy spectrum."
    )
    P(
        "Một khung các chỉ số hiệu năng, kết hợp với mô hình lò phản ứng tập "
        "trung bậc nhất để xác định cân bằng số lượng nuclide, có thể được dùng "
        "để định lượng những ưu và nhược điểm nêu trên cho nhiều tổ hợp khác "
        "nhau giữa lò phản ứng và chu trình nhiên liệu hạt nhân [21]. Khung này "
        "gồm các chỉ số như tái chế nhiên liệu, hiệu suất nhiên liệu, độ độc "
        "của nhiên liệu đã qua sử dụng và khả năng chống phổ biến vũ khí hạt "
        "nhân. Tái chế nhiên liệu hạt nhân đòi hỏi mức axit cao cần được kiểm "
        "soát nhanh và chính xác nhằm tối ưu hóa quá trình chiết tách và hiệu "
        "suất thu hồi [22].",
        "A framework of performance metrics, which coupled with a first-order "
        "lumped reactor model to determine nuclide population balances, can be "
        "used to quantify the aforementioned cons and pros for a range of "
        "different reactor and nuclear fuel cycle combinations [21]. The "
        "framework includes metrics such as fuel reprocessing, fuel efficiency, "
        "spent fuel toxicity, and proliferation resistance. Nuclear fuel "
        "reprocessing requires high acidity levels that should be rapidly and "
        "accurately controlled in order to optimize extraction process and "
        "yields efficiency [22]."
    )
    P(
        "Một cảm biến sợi quang mới dựa trên màng sol-gel pha tạp chỉ thị nhạy "
        "axit đã được phát triển nhằm cải thiện việc giám sát từ xa và trực "
        "tuyến chu trình nhiên liệu hạt nhân. Hệ thống dựa trên một vỏ bọc có "
        "thể chìm ngập, chứa đầu dò germani độ phân giải cao, cho phép đo "
        "nhiên liệu hạt nhân trong bể [23]. Hệ thống có thể được vận chuyển tới "
        "bể lưu trữ nhiên liệu của bất kỳ nhà máy điện hạt nhân nào để đo "
        "trong bể trong thời gian dừng lò bảo trì.",
        "A new optical fiber sensor based on a sol-gel film doped with an "
        "acid-sensitive indicator has been developed to improve remote and "
        "on-line monitoring of the nuclear fuel cycle. The system is based on a "
        "submergible housing, containing a high-resolution germanium detector, "
        "allowing for the measurement of nuclear fuel in-pool [23]. The system "
        "can be transported to any nuclear power plant's fuel storage pool for "
        "in-pool measurements during outage."
    )
    P(
        "Phép đo bức xạ từ một cụm nhiên liệu hạt nhân đã chiếu xạ dựa trên việc "
        "sử dụng các đầu dò thụ động, chẳng hạn như đầu dò vết cho bức xạ neutron "
        "và liều kế alanine cho bức xạ gamma [24]. Battaglieri và cộng sự trình "
        "bày hiệu năng dự kiến của một đầu dò mới nhằm đo phổ năng lượng và "
        "thông lượng tích phân theo năng lượng tuyệt đối của phản neutrino do "
        "chu trình nhiên liệu của một nhà máy điện hạt nhân phát ra [25].",
        "The measurement of radiation from a spent nuclear fuel assembly is "
        "based on usage of passive detectors, such as track detectors for "
        "neutron radiation and alanine dosimeters for gamma radiation [24]. "
        "Battaglieri et al. presented the expected performance of a new detector "
        "to measure the energy spectrum and the absolute energy-integrated flux "
        "of antineutrinos emitted by an unclear power plant fuel cycle [25]."
    )

    # --------------------------- Measurement Methods for Nuclear Fuel Cycle
    H("Phương pháp đo lường trong chu trình nhiên liệu hạt nhân",
      "Measurement Methods for Nuclear Fuel Cycle", h3)
    P(
        "Một mô tả khác về chu trình nhiên liệu hạt nhân gồm chế tạo phần tử "
        "nhiên liệu lò phản ứng và chuẩn bị nhiên liệu, chu trình vật liệu "
        "nhiên liệu hạt nhân, thành phần của thanh nhiên liệu, tái chế nhiên "
        "liệu lò phản ứng nhanh, định lượng nhiên liệu đã qua sử dụng, xử lý "
        "nhiên liệu đã qua sử dụng, và quá trình chế tạo và tái chế nhiên liệu "
        "hạt nhân. Tất cả các bước này có thể được đo bằng kỹ thuật hấp thụ "
        "neutron, phương pháp phát hiện tia gamma năng lượng cao phát ra, "
        "phương pháp DFT, phương pháp âm thanh không phá hủy, kỹ thuật đo độ "
        "dẫn, kỹ thuật truyền siêu âm, công nghệ luyện kim nhiệt, kỹ thuật đo "
        "không phá hủy, quang phổ gamma photon, v.v.",
        "Another description of the nuclear fuel cycle includes manufacture of "
        "reactor fuel element and fuel preparation, nuclear fuel materials "
        "cycle, the composition of fuel rod, reprocessing of fast reactor fuel, "
        "assaying spent fuel, processing spent fuel, the process of nuclear "
        "fuel fabrication and reprocessing. All of these steps can be measured "
        "by neutron absorption technique, detection of high energy gammarays "
        "emitted methods, DFT methods, nondestructive acoustic method, conduct "
        "metric technique, ultrasonic transmission technique, pyrometallurgical "
        "technology, nondestructive assay technique, photon gamma spectrometry, "
        "and so forth."
    )
    P(
        "Một phương pháp không phá hủy dựa trên kỹ thuật hấp thụ neutron đã được "
        "phát triển để phân tích kiểm soát quá trình hàm lượng 235U trong chế "
        "tạo phần tử nhiên liệu lò phản ứng [26]. Perret và Jordan áp dụng một "
        "kỹ thuật mới để đo nhiên liệu tồn dư của các sự phân hạt sau khi chiếu "
        "xạ lại ở công suất thấp [27]. Kỹ thuật này dựa trên việc phát hiện các "
        "tia gamma năng lượng cao do neutron trễ và các sản phẩm phân hạt có "
        "chu kỳ bán rã ngắn phát ra. Liu và cộng sự đã xem xét tình trạng mô "
        "phỏng chu trình vật liệu nhiên liệu hạt nhân bằng Thuyết Mật độ Chức "
        "năng (DFT) từ nguyên lý đầu [28]. Mô phỏng DFT từ nguyên lý đầu đã trở "
        "thành một phương pháp chặt chẽ về định lượng, được sử dụng rộng rãi để "
        "nghiên cứu chu trình vật liệu hạt nhân.",
        "A nondestructive method based on a neutron absorption technique has "
        "been developed for the process-control analysis of 235U in manufacture "
        "of reactor fuel element [26]. Perret and Jordan applied a novel "
        "technique to measure the pent fuel of fissions after reirradiation at "
        "low power [27]. This technique is based on the detection of high energy "
        "gamma rays emitted by delayed neutrons and short-lived fission "
        "products. Liu et al. reviewed the state of first-principles Density "
        "Functional Theory (DFT) modeling of nuclear fuel materials cycle [28]. "
        "The first-principles modeling of DFT has emerged as a quantitatively "
        "rigorous method which was widely used to study nuclear materials cycle."
    )
    P(
        "Rosenkrantz và cộng sự phát triển một phương pháp âm thanh không phá "
        "hủy cho phép tiếp cận dễ dàng thành phần và áp suất của hỗn hợp khí "
        "bên trong ở buồng trên của một thanh nhiên liệu tiêu chuẩn [29]. "
        "Subbuthai và cộng sự thử nghiệm kỹ thuật đo độ dẫn để xác định pha thứ "
        "ba, một pha hình thành do pha hữu cơ bị tách trong trường hợp sự cố "
        "vận hành [30]. Kamei và Serizawa quan tâm đến một phát triển mới của "
        "kỹ thuật truyền siêu âm để đo dòng màng [31]. Kỹ thuật này dùng một "
        "gương phản xạ quay, có khả năng đo phân bố không gian theo thời gian "
        "của độ dày màng lỏng quanh một thanh nhiên liệu hạt nhân mô phỏng.",
        "Rosenkrantz et al. developed a nondestructive acoustic method that "
        "gives an easy access to the composition and the pressure of the "
        "internal gas mixture in the upper plenum of a standard fuel rod [29]. "
        "Subbuthai et al. tested a conductometric technique for determination of "
        "the third phase, a phase formed by splitting of organic phase during "
        "malfunction in operation [30]. Kamei and Serizawa concerned with a new "
        "development of ultrasonic transmission technique for film flow "
        "measurements [31]. The technique adopted a rotating reflector, capable "
        "of measuring time-dependent spatial distribution of liquid film "
        "thickness around a simulated nuclear fuel rod."
    )
    P(
        "Inoue đề xuất công nghệ luyện kim nhiệt, một trong những phương pháp "
        "tiềm năng cho chu trình nhiên liệu hạt nhân trong tương lai [32]. Công "
        "nghệ chính là tinh luyện điện để tách U và Pu, có thể áp dụng cho "
        "nhiên liệu oxit thông qua quá trình khử cũng như cho nhiên liệu kim "
        "loại.",
        "Inoue proposed pyrometallurgical technology which is one of potential "
        "devices for future nuclear fuel cycle [32]. The main technology is "
        "electrorefining for U and Pu separation, which can be applied on oxide "
        "fuels through reduction process as well as metal fuels."
    )
    P(
        "Phương pháp quang học có tầm quan trọng đối với đo lường trong chu "
        "trình nhiên liệu hạt nhân. Normand và cộng sự giới thiệu một khái "
        "niệm mới về hệ thống thiết bị đo hạt nhân [33]. Hệ thống đo mới này "
        "có thể thực hiện phép đo trong điều kiện neutron hoạt động, đặc biệt "
        "là gắn dấu thời gian, cũng như quang phổ gamma photon. Hệ thống đo "
        "được phát triển này nhằm tối ưu hóa chu trình nhiên liệu hạt nhân.",
        "Optical method is important to the measurement of nuclear fuel cycle. "
        "Normand et al. introduced a new concept of nuclear instrumentation "
        "system [33]. This new measurement system could make measurements in "
        "active neutron condition, especially time stamping, as well as photon "
        "gamma spectrometry. This development measurement system aims to "
        "optimize nuclear fuel cycle."
    )
    P(
        "Badawy và EI-Gammal đo các viên nhiên liệu chu trình uranium làm giàu "
        "thấp cho một lò phản ứng hạt nhân bằng kỹ thuật định lượng không phá "
        "hủy thụ động [34]. Phương pháp này dùng máy quang phổ tia gamma với "
        "đầu dò germani độ phân giải cao. Phép đo dựa trên việc đo một đỉnh tia "
        "gamma đặc trưng nhất định của U235 trong các viên nhiên liệu hạt nhân.",
        "Badawy and EI-Gammal measured the low enriched uranium fuel cycle "
        "pellets for a nuclear reactor by a passive nondestructive assay "
        "technique [34]. The method adopted a high-resolution germanium detector "
        "gamma-ray spectrometer. It is based on the measurement of a certain "
        "characteristic gamma-rays peak of the U235 in the nuclear fuel pellets."
    )
    P(
        "Gavron và cộng sự phân tích khả năng tiềm năng của việc dùng công nghệ "
        "máy quang phổ chậm chì trong định lượng nhiên liệu đã qua sử dụng [35]. "
        "Das và cộng sự mô tả việc phát triển một phương pháp quang phổ để xác "
        "định hàm lượng vết U(VI) trong quá trình tái chế và hậu xử lý chế tạo "
        "nhiên liệu hạt nhân trong các ngành công nghiệp sạch [36].",
        "Gavron et al. analyzed the potential capability of using lead slowing "
        "down spectrometer technology in assaying spent fuel [35]. Das et al. "
        "described the development of a spectrophotometric method for trace "
        "level determination of U(VI) during the reprocessing and postprocessing "
        "of nuclear fuel fabrication in clear industries [36]."
    )
    P(
        "Hawari và cộng sự đánh giá tính khả thi của phép định lượng quang phổ "
        "tia gamma thụ động như một cách xác định độ cháy trực tuyến cho nhiên "
        "liệu của Lò phản ứng giường viên nhiên liệu module (MPBR) [37]. Sơ đồ "
        "được thể hiện trong Hình 4.",
        "Hawari et al. assessed the feasibility of passive gamma-ray "
        "spectrometry assay as an approach for on-line burnup determination for "
        "nuclear fuel of the Modular Pebble Bed Reactor (MPBR) [37]. The sketch "
        "is shown in Figure 4."
    )
    FIG(4)
    P(
        "Meier và cộng sự minh họa việc sử dụng giàn thử nghiệm áp suất cao có "
        "thể tiếp cận quang học kết hợp với các phương pháp thử quang học như "
        "một phần của quá trình phát triển khái niệm cháy phun nhiên liệu "
        "nghèo. Các kỹ thuật tạo ảnh và dựa trên laser được dùng để đặc trưng "
        "hóa chuẩn bị nhiên liệu, nhiệt độ, giải phóng nhiệt và chu trình "
        "nhiên liệu hạt nhân [38].",
        "Meier et al. illustrated the utilizations of optically accessible "
        "high-pressure sector test rig in combination with optical test methods "
        "as part of the development process of a fuel lean injection combustion "
        "concept. Imaging and laser-based techniques are used to characterize "
        "fuel preparation, temperature, heat release, and nuclear fuel cycle "
        "[38]."
    )

    # ------------------------------------- SAFEGUARDS AND HOMELAND SECURITY
    H("KIỂM SOÁT HẠT NHÂN VÀ AN NINH QUỐC GIA",
      "SAFEGUARDS AND HOMELAND SECURITY")
    P(
        "Trong phần này, nhiều thiết bị đo lường và phương pháp đo hạt nhân cho "
        "các ứng dụng môi trường an toàn và an ninh sẽ được thảo luận. Gần đây, "
        "các thiết bị đo lường và phương pháp đo hạt nhân chủ yếu gồm kỹ thuật "
        "định lượng không phá hủy (NDA), đầu dò bán dẫn nhiệt độ (TS), đầu dò "
        "Na/I, đầu dò xenon áp suất cao (HPXe), đầu dò nhấp nháy nhựa, thuật "
        "toán lập trình di truyền, thiết bị phòng thí nghiệm hóa phân tích tự "
        "động và thiết bị đo mức chất lỏng/kiểm kê chống can thiệp — hệ thống "
        "có thể được dùng để bảo đảm kiểm soát hạt nhân và an ninh quốc gia.",
        "In this section, many nuclear instrumentations and measurement methods "
        "for safe and secure environmental applications will be discussed. "
        "Recently, the mainly nuclear instrumentations and measurement methods "
        "include Nondestructive Assay (NDA) techniques, Temperature Semiconductor "
        "(TS) detector, Na/I detector, High Pressure xenon (HPXe) detector, "
        "plastic scintillator, genetic programming algorithm, automated "
        "analytical chemistry laboratory instrumentation and tamper-resistant "
        "liquid level/accountability instrumentation, system, which can be used "
        "for guarantee safeguards and homeland security."
    )
    P(
        "Kiểm soát hạt nhân phụ thuộc một phần vào việc kiểm chứng vật liệu hạt "
        "nhân bằng NDA. Thông thường, Cơ quan Năng lượng Nguyên tử Quốc tế "
        "(IAEA) dựa vào cả kỹ thuật NDA dựa trên neutron và tia gamma cho các "
        "phép đo kiểm chứng. Các phép kiểm chứng này có thể mang tính định tính "
        "hoặc định lượng. Belian và cộng sự mô tả các kỹ thuật dùng để hiệu "
        "chuẩn thiết bị NDA bằng phương pháp Monte Carlo (MC) và báo cáo kết "
        "quả của các lần hiệu chuẩn đó [39].",
        "Nuclear safeguards rely, in part, on NDA verification of nuclear "
        "material. Typically, the International Atomic Energy Agency (IAEA) "
        "relies on both neutron and gamma ray-based NDA techniques for "
        "verification measurements. These verifications can be either "
        "qualitative or quantitative. Belian et al. described the techniques "
        "used to calibrate NDA instrumentation using Monte Carlo (MC) methods "
        "and reported the outcome of these calibrations [39]."
    )
    P(
        "Peter và cộng sự phác thảo cách tiếp cận thiết bị kiểm soát truyền "
        "thống và các nỗ lực nhằm kiểm chứng tính đúng đắn của thông tin về "
        "vật liệu và cơ sở hạt nhân đã khai báo, chủ yếu gồm kiểm kê vật liệu, "
        "đo thành phần vật liệu và kiểm tra vỏ bọc chứa đựng [40]. Các công nghệ "
        "đo truyền thống để phát hiện vật liệu đã khai báo gồm NDA, chủ yếu là "
        "phương pháp đo neutron và gamma, Hệ thống giám sát bức xạ không người "
        "trực tiếp (URMSs) và các hệ thống đo và giám sát khác.",
        "Peter et al. outlined the traditional safeguards instrumentation "
        "approach and efforts that aim at verifying the correctness of "
        "information about declared nuclear materials and facilities, mainly "
        "including materials accountancy, materials composition measurements, "
        "and containment verification [40]. The traditional measurement "
        "technologies for detection of declared materials consist of NDA, which "
        "include primarily neutron and gamma measurement methods, Unattended "
        "Radiation Monitoring Systems (URMSs), other measurement and monitoring "
        "systems."
    )
    P(
        "LaFleur và cộng sự trình bày một kỹ thuật NDA gọi là Đo mật độ cộng "
        "hưởng neutron tự thăm dò (SINRD), hiện đang được phát triển tại Phòng "
        "thí nghiệm Quốc gia Los Alamos (LANL) nhằm cải tiến các phép đo kiểm "
        "soát hạt nhân hiện có cho cụm nhiên liệu lò phản ứng nước nhẹ (LWR) "
        "[41]. East và cộng sự mô tả bốn hệ thống được phát triển tại Phòng "
        "thí nghiệm Khoa học Los Alamos (LASL) để phân tích không phá hủy vật "
        "liệu nhiên liệu hạt nhân [42]. Họ dùng máy tính nhỏ hoặc máy tính lập "
        "trình được để phân tích dữ liệu và kiểm soát phép đo.",
        "LaFleur et al. presented an NDA technique called Self-Interrogation "
        "Neutron Resonance Densitometry (SINRD) which is currently being "
        "developed at Los Alamos National Laboratory (LANL) to improve existing "
        "nuclear safeguards measurements for Light Water Reactor (LWR) fuel "
        "assemblies [41]. East et al. described four systems developed at the "
        "Los Alamos Scientific Laboratory (LASL) for nondestructive analysis of "
        "nuclear fuel materials [42]. They utilized either minicomputers or a "
        "programmable calculator for data analysis and measurement control."
    )
    P(
        "Một vấn đề quan trọng trong kiểm soát hạt nhân là kiểm chứng dữ liệu do "
        "đơn vị vận hành khai báo về nhiên liệu hạt nhân đã qua sử dụng. Nhiều "
        "kỹ thuật đã được giao cho mục đích này. Một cách tiếp cận không phá "
        "hủy được dùng trong đo bức xạ gamma từ các cụm nhiên liệu hạt nhân đã "
        "chiếu xạ. Với kỹ thuật này, các thông số như độ cháy và thời gian làm "
        "nguội có thể được tính toán hoặc kiểm chứng.",
        "An important issue in nuclear safeguards is verification of "
        "operator-declared data of spent nuclear fuel. Various techniques have "
        "been assigned for this purpose. A nondestructive approach is used in "
        "the measurement of gamma radiation from spent nuclear fuel assemblies. "
        "By this technique, parameters such as burnup and cooling time can be "
        "calculated or verified."
    )
    P(
        "Willman và cộng sự dùng tia gamma từ 137Cs, 134Cs và 154Eu để xác định "
        "tính nhất quán của thông tin do đơn vị vận hành khai báo [43]. "
        "Khusainov và cộng sự phát triển một máy quang phổ gamma di động với "
        "đầu dò TS độc đáo hoạt động gần nhiệt độ phòng nhằm lấp khoảng trống "
        "này [44]. Swoboda và cộng sự nghiên cứu một đầu dò gamma quang phổ mới "
        "có khả năng dùng trong thiết bị nhận dạng đồng vị phóng xạ cầm tay. "
        "Đầu dò Na/I tiêu chuẩn, gọi là như vậy, được so sánh với các đầu dò "
        "nhấp nháy và đầu dò TS nhiệt độ phòng mới khác [45].",
        "Willman et al. utilized gamma rays from 137Cs, 134Cs, and 154Eu to "
        "determine the consistency of operator-declared information [43]. "
        "Khusainov et al. developed a portable gamma spectrometer with a "
        "unique, near room TS detector to close this gap [44]. Swoboda et al. "
        "investigated a new spectral gamma detector for potential use in "
        "hand-held radioisotope identification devices. The so-called standard "
        "Na/I detector is compared with other new scintillation and room TS "
        "detectors [45]."
    )
    P(
        "Đã có nhu cầu kéo dài về một hệ thống đầu dò tia gamma nhiệt độ phòng "
        "có hiệu suất cao và độ phân giải thỏa đáng cho các ứng dụng kiểm soát "
        "hạt nhân [46]. Đầu dò HPXe có độ phân giải, hiệu suất, khả năng chống "
        "bức xạ nội tại và độ ổn định nhiệt độ, có thể là ứng viên phù hợp cho "
        "ứng dụng rộng rãi trong kiểm soát hạt nhân. Wang và cộng sự dùng hai "
        "mẫu plutonium có thành phần đồng vị đã biết và nhiều chuẩn uranium "
        "tia gamma để trình bày thông tin tia gamma từ các đầu dò Germani độ "
        "tinh khiết cao (HPGe) dạng triệt tiêu và một đầu dò dạng phẳng [47].",
        "There has been a long-standing need for a room-temperature gamma-ray "
        "detector system with high efficiency and adequate resolution for "
        "nuclear safeguards applications [46]. The HPXe detector offers "
        "resolution, efficiency, intrinsic radiation resistance, and "
        "temperature stability, which can be a viable candidate for extensive "
        "application in nuclear safeguards. Wang et al. utilized two plutonium "
        "samples of known isotopic content and a broad range of gamma-ray "
        "uranium standards to show the gamma ray information from suppressed "
        "and one planar High Purity Germanium (HPGe) detectors [47]."
    )
    P(
        "Các phép đo kiểm soát hạt nhân chủ động dựa trên tương quan thời gian "
        "giữa tia gamma nhanh và các neutron phóng xạ từ cùng một sự phân hạt "
        "đang trở thành một kỹ thuật hữu ích. Marseguerra và cộng sự báo cáo "
        "kết quả dùng nguồn 252Cf để hiệu chuẩn đầu dò nhấp nháy nhựa trong các "
        "thí nghiệm kiểm soát hạt nhân [48].",
        "Active nuclear safeguards measurements that rely on the time "
        "correlation between fast gamma rays and neutrons radioactive from the "
        "same fission are becoming a useful technique. Marseguerra et al. "
        "reported the results of using a 252Cf source for the calibration of a "
        "plastic scintillator in nuclear safeguards experiments [48]."
    )
    P(
        "Pozzi và Segovia trình bày một phương pháp ước tính khối lượng mẫu "
        "uranium oxit dựa trên phép đo phân tích nhiễu do nguồn 252Cf điều "
        "khiển [49]. Kết quả thí nghiệm cho thấy khối lượng mẫu có thể được dự "
        "đoán thành công bằng thuật toán lập trình di truyền. Vermaercke và "
        "cộng sự cùng Frazzini lần lượt thảo luận phép đo rất nhanh và chính "
        "xác hàm lượng plutonium và uranium trong vật liệu hạt nhân [50, 51]. "
        "Thiết bị gồm máy chuẩn độ coulomb dòng không đổi và máy chuẩn độ trọng "
        "lượng để đo uranium, cùng hệ thống coulomb thế kiểm soát để đo "
        "plutonium.",
        "Pozzi and Segovia presented a method to estimate the mass of uranium "
        "oxide samples based on 252Cf source-driven noise-analysis measurements "
        "[49]. The experiments results showed that the mass of the samples can "
        "be successfully predicted using a genetic programming algorithm. "
        "Vermaercke et al. and Frazzini discussed a highly rapid and precise "
        "measurement of the plutonium and uranium content of nuclear materials, "
        "respectively [50, 51]. The instrumentation includes a constant-current "
        "coulometric titrator and gravimetric titrator for uranium measurements "
        "and a controlled-potential coulometry system for plutonium measurements."
    )
    P(
        "Họ đã tạo ra Đánh giá An toàn Xác suất (PSA), được chứng minh là phương "
        "pháp hiệu quả cho phân tích an toàn và các quyết định dựa trên rủi ro "
        "[52]. Lu và Jiang trình bày tổng quan về ứng dụng của PSA trong ba "
        "lĩnh vực của hệ thống Đo lường và Điều khiển (IC) kỹ thuật số tại nhà "
        "máy điện hạt nhân [53].",
        "They invented Probabilistic Safety Assessment (PSA) that has proved to "
        "be an effective method for safety analysis and risk-based decisions "
        "[52]. Lu and Jiang provided an overview of PSA applications in three "
        "areas of digital Instrumentation and Control (IC) systems in nuclear "
        "power plants [53]."
    )
    P(
        "Giám sát bức xạ là một trong các phương pháp chẩn đoán cho phép đo "
        "kiểm soát hạt nhân, được dùng để chống trộm cắp Vật liệu hạt nhân đặc "
        "biệt (SNM) bởi người đi bộ rời khỏi khu vực tiếp cận SNM [54].",
        "Radiation monitoring is one of the diagnosis methods for nuclear "
        "safeguards measurements which is used to protect against the theft of "
        "Special Nuclear Materials (SNM) by pedestrians departing from SNM "
        "access areas [54]."
    )
    P(
        "Letourneau và cộng sự xem xét đầu dò Nucifer, tập trung phát triển các "
        "kỹ thuật kiểm soát mới cho thế hệ lò phản ứng tiếp theo [55]. Thông "
        "lượng lớn neutrino thoát ra từ lò phản ứng hạt nhân mang thông tin về "
        "hai đại lượng đáng quan tâm đối với kiểm soát hạt nhân là công suất lò "
        "và tồn lượng vật liệu phân hạch [56].",
        "Letourneau et al. reviewed the Nucifer detector which is interested in "
        "developing new safeguard techniques for next generation new reactors "
        "[55]. The large flux of neutrinos that leaves a nuclear reactor carries "
        "information about two quantities of interest for nuclear safeguard for "
        "reactor power and fissile inventory [56]."
    )
    P(
        "Cabrera-Palmer và cộng sự đã chứng minh rằng giám sát lò phản ứng hạt "
        "nhân dựa trên phản neutrino là khả thi khi dùng một đầu dò khối lập "
        "phương tương đối nhỏ chế từ chất nhấp nháy lỏng pha gadolinium, đặt "
        "cách lò phản ứng nước áp lực (PWR) hàng chục mét [57]. Sơ đồ được thể "
        "hiện trong Hình 5. Parsons và Wells đã thử nghiệm và phát triển một "
        "hệ thống thiết bị đo mức chất lỏng chống can thiệp cho công tác kiểm "
        "soát [58]. Các thử nghiệm của họ chứng minh độ chính xác của phép đo "
        "mức chất lỏng dùng kỹ thuật phản xạ miền thời gian (TDR) và độ chính "
        "xác của phép đo chênh lệch nhiệt độ và áp suất dùng đầu dò cảm biến mức "
        "chất lỏng thiết kế riêng.",
        "Cabrera-Palmer et al. have demonstrated the antineutrino-based nuclear "
        "reactor monitoring was feasible when using a relatively small cubic "
        "scale detector made of gadolinium loaded liquid scintillator at tens "
        "of meters standoff from a Pressurized Water Reactor (PWR) [57]. The "
        "sketch is shown in Figure 5. Parsons and Wells tested and developed a "
        "tamper-resistant liquid level instrumentation system for safeguards "
        "[58]. Their testing demonstrated the accuracy of liquid level "
        "measurement using Time Domain Reflectometry (TDR) techniques and the "
        "accuracy of differential temperature and pressure measurements "
        "utilizing a custom-designed liquid level sensor probe."
    )
    FIG(5)

    return b
