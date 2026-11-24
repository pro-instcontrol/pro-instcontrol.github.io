# -*- coding: utf-8 -*-
"""Book 9, Chapter 2 (part A) - Advanced Measuring (Instrumentation)
Methods for Nuclear Installations: A Review (EN/VI bilingual).

Source: L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and
Control* (Bibliotex, 2019), PDF pp. 29-35, printed pp. 13-19: ABSTRACT,
INTRODUCTION, NUCLEAR POWER REACTORS and its two subsections.  The three
figures are redrawn as vectors in `ppicfig2.py`; captions come from there.
"""

from ppic_common import h2, h3, p, fig, note  # noqa: F401
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

    # ------------------------------------------------------------------ ABSTRACT
    H("TÓM TẮT", "ABSTRACT")
    P(
        "Công nghệ hạt nhân đã được sử dụng rộng rãi trên thế giới. Nghiên cứu về đo "
        "lường trong các cơ sở hạt nhân bao gồm nhiều khía cạnh, như lò phản ứng hạt "
        "nhân, chu trình nhiên liệu hạt nhân, an toàn và an ninh, tai nạn hạt nhân, "
        "công tác xử lý sau sự cố, phân tích và các ứng dụng môi trường. Trong những "
        "thập kỷ gần đây, nhiều thiết bị và kỹ thuật đo lường tiên tiến đã được áp "
        "dụng rộng rãi trong các cơ sở hạt nhân. Bài báo này chủ yếu giới thiệu sự "
        "phát triển của các phương pháp đo lường (thiết bị đo) cho các cơ sở hạt "
        "nhân và các ứng dụng của những thiết bị và phương pháp này.",
        "The nuclear technology has been widely used in the world. The research of "
        "measurement in nuclear installations involves many aspects, such as nuclear "
        "reactors, nuclear fuel cycle, safety and security, nuclear accident, after "
        "action, analysis, and environmental applications. In last decades, many "
        "advanced measuring devices and techniques have been widely applied in "
        "nuclear installations. This paper mainly introduces the development of the "
        "measuring (instrumentation) methods for nuclear installations and the "
        "applications of these instruments and methods."
    )

    # -------------------------------------------------------------- INTRODUCTION
    H("GIỚI THIỆU", "INTRODUCTION")
    P(
        "Trong thập kỷ qua, công nghệ hạt nhân đã phát triển nhanh chóng và trở nên "
        "quan trọng hơn đối với xã hội loài người cùng với sự phát triển của khoa "
        "học và công nghệ. Công nghệ hạt nhân có nhiều ưu điểm, chẳng hạn như không "
        "phát thải carbon, độc lập năng lượng và an toàn. Hiện nay, các cơ sở hạt "
        "nhân phổ biến hơn bao giờ hết. Do đó, cùng với sự phát triển nhanh chóng và "
        "ứng dụng rộng rãi của công nghệ hạt nhân, nhiều công nghệ mới đã xuất hiện "
        "nhằm đảm bảo độ tin cậy và an toàn, trong đó các thiết bị và kỹ thuật đo "
        "lường có thể đo và giám sát chính xác các cơ sở hạt nhân có tầm quan trọng "
        "đặc biệt.",
        "In last decade, nuclear technology has developed rapidly and became more "
        "important to human society with the development of science and technology. "
        "Nuclear technology has many advantages, such as zero carbon emissions, "
        "energy independence, and safety. At present, nuclear installations are more "
        "prevalent than ever before. Therefore, with the rapid development and wide "
        "applications of nuclear technology, many new technologies have been "
        "emerging to guarantee its reliability and safety, where measuring devices "
        "and techniques that can exactly measure and monitor the nuclear "
        "installations show particular importance."
    )
    P(
        "Bài báo này là một bài tổng quan về những tiến bộ trong các lĩnh vực trọng "
        "tâm của công nghệ đo lường (thiết bị đo) có ứng dụng trong các cơ sở hạt "
        "nhân. Các thiết bị được sử dụng trong các cơ sở hạt nhân chủ yếu bao gồm "
        "nhiều loại đầu dò, cảm biến và đồng hồ đo. Các phương pháp đo lường trong "
        "công nghệ hạt nhân phần lớn bao gồm các phương pháp đo không phá hủy. Bài "
        "báo trình bày nhiều thiết bị và phương pháp đo lường được sử dụng rộng "
        "rãi trong lò phản ứng điện hạt nhân, chu trình nhiên liệu hạt nhân, kiểm "
        "soát hạt nhân và an ninh quốc gia, tai nạn hạt nhân, công tác sau sự cố và "
        "phân tích.",
        "This paper is a review of advances in measuring (instrumentation) technology "
        "focus areas that have applications in nuclear installations. The instruments "
        "used in nuclear installations mainly include multifarious detectors, "
        "sensors, and meters. The measurement methods for nuclear technology mostly "
        "consist of all kinds of nondestructive measurement methods. The paper "
        "presents various instruments and measurement methods which are widely used "
        "in nuclear power reactors, nuclear fuel cycle, safeguards and homeland "
        "security, nuclear accident, after action, and analysis."
    )

    # ---------------------------------------------------- NUCLEAR POWER REACTORS
    H("LÒ PHẢN ỨNG ĐIỆN HẠT NHÂN", "NUCLEAR POWER REACTORS")

    # --------------------------------- Nuclear Power Reactors Instrumentations
    H("Thiết bị đo lường trong lò phản ứng điện hạt nhân",
      "Nuclear Power Reactors Instrumentations", h3)
    P(
        "Trong phần này, các thiết bị đo dùng để đo phân hạt neutron, liều neutron, "
        "thông lượng, tốc độ phân hạt trong lò và nhiệt độ được thảo luận. Ở đây, "
        "các thiết bị bao gồm đầu dò Micro-Me-gas, nhiệt kế nhiễu, bộ đếm tỷ lệ "
        "tương đương mô, cặp nhiệt điện nhiệt độ cao, đầu dò nhấp nháy lỏng, máy "
        "quang phổ, cảm biến sợi quang, buồng phân hạt Uranium, buồng phân hạt "
        "Plutonium, Đầu dò neutron tự cấp nguồn, buồng Ionization, Đầu dò gamma tự "
        "cấp nguồn, nhiệt lượng kế vi phân, Nhiệt kế Gamma và Cảm biến sợi quang, "
        "v.v.",
        "In this section, instrumentations to measuring the neutron fission, the "
        "neutron dose, the flux, the reactor fission rate, and temperature are "
        "discussed. Here instrumentations contain Micro-Me-gas detectors, noise "
        "thermometer, tissue equivalent proportional counter, high-temperature "
        "thermocouples, liquid scintillation detector, spectrometers, optical fiber "
        "sensors, Uranium Fission chamber, Plutonium Fission chamber, Self-Powered "
        "Neutron Detector, Ionization chamber, Self-Powered Gamma Detector, "
        "Differential calorimeter, Gamma Thermometer, and Optical Fiber Sensors, "
        "and so forth."
    )
    P(
        "Một bố trí thí nghiệm mới tại cơ sở n_TOF của Hội đồng Châu Âu về Nghiên cứu "
        "Hạt nhân (Conseil Europeen pour la Recherche Nucleaire - CERN) đã được xây "
        "dựng và thử nghiệm bởi Guerrero và cộng sự, cho phép đo đồng thời các phản "
        "ứng neutron, phân hạt do neutron gây ra và bắt giữ neutron bằng cách kết "
        "hợp một Máy đo nhiệt lượng hấp thụ toàn phần 4π (4π Total Absorption "
        "Calorimeter - TAC) với một số đầu dò Micro-Me-gas (MMGAS) [1]. Sơ đồ được "
        "thể hiện trong Hình 1.",
        "A new set-up at the Conseil Europeen pour la Recherche Nucleaire (CERN) "
        "n_TOF facility has been built and tested by Guerrero et al. which allowed "
        "measuring simultaneously neutron, induced fission and capture reactions by "
        "combining a 4π Total Absorption Calorimeter (TAC) with several Micro-Me-gas "
        "(MMGAS) detectors [1]. The sketch is shown in Figure 1."
    )
    FIG(1)
    P(
        "Bolshakova và cộng sự đã thảo luận các vấn đề trong việc chế tạo thiết bị "
        "đo dùng để đo các cảm biến từ trường bán dẫn trong quá trình chiếu xạ bằng "
        "neutron trong lò phản ứng hạt nhân, đến mức thông lượng tương tự như thông "
        "lượng neutron tại vị trí cảm biến trạng thái ổn định trong lò thử nghiệm "
        "nhiệt hạch quốc tế [2]. Họ đã sử dụng bộ đếm tỷ lệ tương đương mô để đo "
        "liều neutron và suất liều tương đương, và máy quang phổ đa cầu được dùng "
        "để đo phân bố năng lượng [3].",
        "Bolshakova et al. discussed the issues of creating the instrumentation for "
        "measured the semiconductor magnetic field sensors during their irradiation "
        "with neutrons in nuclear reactors up to fluences similar to neutron "
        "fluences in steady-state sensor locations in international thermonuclear "
        "experimental reactor [2]. They used the tissue equivalent proportional "
        "counter to measure the neutron dose and dose equivalent rates, and the "
        "multisphere spectrometers were used in measurement of energy distributions "
        "[3]."
    )
    P(
        "Fourmentel và cộng sự đã thực hiện nhiều công trình để đo chính xác hơn "
        "thông lượng photon, nhiệt lượng hạt nhân và thông lượng neutron trong lò "
        "phản ứng [4]. Các thiết bị đo thông lượng photon bằng hai loại cảm biến "
        "khác nhau (buồng Ionization và Đầu dò gamma tự cấp nguồn), nhiệt lượng hạt "
        "nhân bằng hai thiết bị khác nhau (nhiệt lượng kế vi phân và Nhiệt kế "
        "Gamma), và thông lượng neutron bằng ba loại cảm biến khác nhau (buồng phân "
        "hạt Uranium, buồng phân hạt Plutonium và Đầu dò neutron tự cấp nguồn).",
        "Fourmentel et al. did a lot of work to measure more accurately photon flux, "
        "nuclear heating, and neutron flux in the reactor [4]. The devices measure "
        "the photon flux by two different sensors (Ionization chamber and "
        "Self-Powered Gamma Detector), the nuclear heating by two different ones "
        "(Differential calorimeter and Gamma Thermometer), and the neutron flux by "
        "three different kinds of sensors (Uranium Fission chamber, Plutonium "
        "Fission chamber and Self Powered Neutron Detector)."
    )
    P(
        "Một kỹ thuật then chốt trong các cơ sở hạt nhân là giám sát nhiệt độ. Brixy "
        "đã sử dụng nhiệt kế nhiễu để đo nhiệt độ trong lò phản ứng hạt nhân [5]. "
        "Nhiệt kế nhiễu dựa trên định lý Nyquist, được dùng để xác định nhiệt độ "
        "tuyệt đối. Cả hai điện trở đều có điện áp nhiễu, một điện trở ở nhiệt độ "
        "chưa biết, điện trở kia ở nhiệt độ phòng. So sánh với tỷ số của các điện "
        "trở, khi điện áp nhiễu từ hai điện trở khớp nhau, tỷ số nhiệt độ tuyệt đối "
        "của chúng được xác định.",
        "A key technique in nuclear installations is monitoring of temperature. Brixy "
        "used the noise thermometer to measure the temperature in nuclear reactors "
        "[5]. The noise thermometer rooted in the Nyquist theorem which is used to "
        "determine absolute temperatures. Both of the two resistors have noise "
        "voltages, one at the unknown temperature, the other at room temperature. "
        "Compared with the ratio of the resistances, when the noise voltages from "
        "the two resistors are matching, the ratio of their absolute temperatures "
        "is determined."
    )
    P(
        "Bily và Sklenka đã thiết kế một thiết bị đo mới để đo các hiệu ứng nhiệt "
        "trên lò phản ứng huấn luyện gọi là VR-1 [6].",
        "Bily and Sklenka designed a new instrumentation for measurement of thermal "
        "effects on the training reactor which called VR-1 [6]."
    )
    P(
        "Rempe và cộng sự đã đối chiếu các loại cảm biến sẵn có để hỗ trợ đo chiếu "
        "xạ trong lò và các cảm biến hiện có tại Lò thử nghiệm tiên tiến (Advanced "
        "Test Reactor - ATR) [7]. Những thành tựu từ nỗ lực triển khai công nghệ "
        "cảm biến mới rất đáng chú ý, với việc mô tả các cảm biến nhiệt và độ dẫn "
        "nhiệt mới hiện có cho người sử dụng ATR. Sơ đồ được thể hiện trong Hình 2.",
        "Rempe et al. contrasted the types of sensors available to support in-pile "
        "irradiations measurement and those sensors available to Advanced Test "
        "Reactor (ATR) currently [7]. Accomplishments from new sensor technology "
        "deployment efforts are remarkable by describing new thermal and temperature "
        "conductivity sensors available to ATR users now. The sketch is shown in "
        "Figure 2."
    )
    FIG(2)
    P(
        "Những tiến bộ vượt bậc đạt được trong thập kỷ qua trong hiểu biết về vật lý "
        "neutrino cơ bản đã cho phép chúng ta đưa vào sử dụng việc phát hiện tín "
        "hiệu phản neutrino từ lò phản ứng để phục vụ công tác điều tra tự động và "
        "không xâm lấn nhà máy điện hạt nhân. Porta và cộng sự đã trình bày thí "
        "nghiệm NUCIFER, sử dụng một đầu dò nhấp nháy lỏng pha gadolinium (Gd) 1 "
        "tấn được lắp đặt cách lõi lò phản ứng vài chục mét để đo hàm lượng "
        "Plutonium và công suất nhiệt [8]. Thiết kế của một đầu dò khối nhỏ như "
        "vậy tập trung vào khả năng loại bỏ nhiễu nền tốt và hiệu suất phát hiện "
        "cao.",
        "The major superiority obtained over the last decade in the understanding of "
        "fundamental neutrino physics allowed us to put into use the detection of "
        "reactor antineutrino signals to automatic and nonintrusive nuclear power "
        "plant investigates. Porta et al. presented the NUCIFER experiment, which "
        "used a 1-ton Gd-doped liquid scintillator detector to be installed a few "
        "10 m from a reactor core for measurements of its Plutonium content and "
        "thermal power [8]. The design of such a small bulk detector has been "
        "focused on good background rejection and high detection efficiency."
    )
    P(
        "Việc thẩm định tiên tiến các cặp nhiệt điện nhiệt độ cao đổi mới, đặc biệt "
        "dành cho ứng dụng trong lò, đã được Villard và cộng sự thiết kế [9]. Loại "
        "cặp nhiệt điện mới này dựa trên các phần tử nhiệt điện niobi và molypden, "
        "gần như không thay đổi dưới thông lượng neutron nhiệt ngay cả trong môi "
        "trường hạt nhân khắc nghiệt, trong khi các loại cặp nhiệt điện nhiệt độ "
        "cao điển hình như Loại C hoặc Loại S bị thay đổi đáng kể do sai lệch gây "
        "ra bởi biến dạng vật liệu trong cùng điều kiện.",
        "The advanced qualification of innovative high-temperature thermocouples "
        "specifically for in-pile applications was designed by Villard et al. [9]. "
        "This new kind of thermocouple was based on niobium thermoelements and "
        "molybdenum, which persisted nearly unchanged by thermal neutron flux even "
        "though under harsh nuclear environments, whereas Type C or Type S as "
        "typical high-temperature thermocouples is changed by significant drifts "
        "caused by material deformations under the same conditions."
    )
    P(
        "Vấn đề then chốt khác cho các chương trình chiếu xạ tiên tiến trong lò "
        "phản ứng nghiên cứu hạt nhân là đo tại chỗ, đặc biệt trong Lò thử nghiệm "
        "vật liệu (Material Testing Reactors - MTR). Về triển vọng này, Cảm biến sợi "
        "quang (Optical Fiber Sensors - OFSs) là một lựa chọn tốt. OFS có thể cung "
        "cấp các đặc tính nổi bật mang lại ưu điểm vốn có so với các phương pháp "
        "cảm biến truyền thống. Một điều kiện ban đầu để phát triển OFS là đảm bảo "
        "sự hấp thụ do bức xạ (Radiation-Induced Absorption - RIA) của ánh sáng "
        "trong sợi không vượt quá ngưỡng định trước. Cheymol và cộng sự đã báo cáo "
        "kết quả của một nghiên cứu chiếu xạ kéo dài, thực hiện trên nhiều loại "
        "sợi, bao gồm sợi chế độ đơn (Single Mode - SM), sợi đa chế độ (Multimode - "
        "MM) và sợi có lõi rỗng dải tần quang tử (Photonic Band Gap - PBG) [10]. "
        "Đối với ứng dụng của Giao thoa kế Fabry-Perot sợi quang (Fiber Optic "
        "Fabry-Perot Interferometer - FOFPI) trong đo sự thay đổi áp suất tại các "
        "lò nước của nhà máy điện hạt nhân, các cảm biến thông minh có thể góp phần "
        "cải thiện an toàn và độ ổn định đo lường dài hạn [11]. Thuật toán tự hiệu "
        "chuẩn của cảm biến áp suất dựa trên thực tế rằng chiều dài buồng FOFPI phụ "
        "thuộc vào áp suất khi phổ của nguồn quang không đổi đang được xem xét. Kết "
        "quả cho thấy việc chế tạo phần tử nhạy FOFPI dựa trên công nghệ xếp lớp "
        "phân tử mang lại sự cải thiện đáng kể chất lượng của đồng hồ đo.",
        "The other key issue for advanced irradiation programs in nuclear research "
        "reactors is in situ measurement, especially in Material Testing Reactors "
        "(MTR). With the prospective, Optical Fiber Sensors (OFSs) is a good choice. "
        "OFS can provide unique feature substantial properties that bring intrinsic "
        "advantages over conventional sensing approaches. An initial condition for "
        "the development of OFS ensures that the Radiation-Induced Absorption (RIA) "
        "of the light in the fiber does not exceed a predefined threshold. Cheymol "
        "et al. reported the results of a long-lasting irradiation investigation, "
        "which carried out various fibers, including Single Mode (SM) fibers and "
        "Multimode (MM) and hollow core Photonic Band Gap (PBG) fibers [10]. for "
        "application of a Fiber Optic Fabry-Perot Interferometer (FOFPI) for "
        "measurements of the pressure variation in water reactors of nuclear power "
        "plants, the intelligent sensors could contribute to improving their safety "
        "and long-term metrological stability [11]. The algorithm of self-calibration "
        "of the pressure sensor based on the fact that the length of the FOFPI "
        "cavity depends on the pressure at a constant spectrum of an optical source "
        "is considered. It is shown that manufacturing of an FOFPI-sensitive "
        "element based on a molecular layering nanotechnology provides for "
        "substantial enhancement of the quality of the gauge."
    )

    # ------------------------------- Nuclear Power Reactors Measurement Methods
    H("Phương pháp đo lường trong lò phản ứng điện hạt nhân",
      "Nuclear Power Reactors Measurement Methods", h3)
    P(
        "Trong phần này, các phương pháp đo lường trong lò phản ứng điện hạt nhân "
        "được thảo luận. Ở đây, các phương pháp đo lường bao gồm phương pháp lá "
        "indi, phát hiện vết hạt nhân trạng thái rắn, kỹ thuật thời gian bay, "
        "phương pháp truyền sóng vi ba, đo liều quang học, quang phổ khối gia tốc, "
        "quang phổ gamma và giao thoa kế quét bước sóng, v.v. Các phương pháp đo "
        "lường này có thể được dùng để đo thông lượng neutron, tốc độ phân hạt "
        "trong lò, năng lượng tuyệt đối của neutron lạnh, cường độ trường bức xạ, "
        "suất liều kích thích điện tử, dịch chuyển nguyên tử, thông lượng neutron "
        "nhiệt và phân hạt bay hơi.",
        "In this section, nuclear power reactors measurement methods are discussed. "
        "Here measurement methods contain indium foils methods, solid state nuclear "
        "track detection, time-of-flight technique, microwave propagation methods, "
        "optical dosimetry, accelerator mass spectrometry, gamma spectrometry and "
        "swept wavelength interferometry, and so forth. These measurement methods "
        "can be used to measure neutron flux, reactor fission rate, absolute energy "
        "of cold neutrons, radiation field intensity, electronic excitation dose "
        "rate, atomic displacement, thermal neutron flux, and volatile fission."
    )
    P(
        "Papastefanou đã báo cáo phép đo suất phản xạ albedo của nước và thông lượng "
        "neutron nhiệt bằng lá indi, cùng với việc phân tích hệ số nhân, chiều dài "
        "giảm, khuếch đại neutron, chiều dài di chuyển và các thông số của lò phản "
        "ứng hạt nhân [12]. Li và cộng sự đã mô tả nguyên lý và phương pháp đo tốc "
        "độ phân hạt của lò phản ứng bằng phát hiện vết hạt nhân trạng thái rắn và "
        "trình bày kết quả đo cho lò phản ứng hạt nhân nguồn neutron thu nhỏ [13]. "
        "Phương pháp này có ưu điểm so với các phương pháp vật lý khác vì tránh "
        "được giả định xấp xỉ của một số phương pháp khác trong đo tốc độ phân hạt.",
        "Papastefanou reported the measurement of albedo of water and neutron flux "
        "for thermal neutrons with indium foils and the analyses of multiplication "
        "factor, relaxation length, neutron amplification, migration length, and "
        "parameters of the nuclear reactor [12]. Li et al. described the measurement "
        "principle and method of fission rate of nuclear reactor by solid-state "
        "nuclear track detection and showed the measurement result for miniature "
        "neutron source nuclear reactor [13]. This method has advantage over other "
        "physics method which avoided the approximate supposition of some other "
        "method in fission rate measurement."
    )
    P(
        "Laurie và cộng sự đã tổng hợp dữ liệu thu được từ các thử nghiệm chiếu xạ "
        "trước đó dưới dạng dữ liệu cặp nhiệt điện [14]. Khentout và Meftah đã "
        "trình bày phương pháp đo tại cơ sở nhiễu xạ neutron của lò điện hạt nhân "
        "Es-Salam và đo năng lượng tuyệt đối của neutron lạnh tại cơ sở tán xạ góc "
        "nhỏ của lò điện hạt nhân NUR bằng kỹ thuật thời gian bay [15].",
        "Laurie et al. summed up data collected from previous irradiation tests in "
        "terms of thermocouple data [14]. Khentout and Meftah presented a method for "
        "measuring the neutron diffraction facility at the Es-Salam nuclear power "
        "reactor and the absolute energy of cold neutrons at the small angle "
        "scattering facility of the NUR nuclear power reactor using the time-of-"
        "flight technique [15]."
    )
    P(
        "Bhattacharya và cộng sự đã báo cáo một nghiên cứu về đo cường độ trường "
        "bức xạ trong lõi của lò phản ứng hạt nhân xung, sử dụng sự truyền vi ba qua "
        "một loại khí hiếm được lựa chọn phù hợp đặt trong lò điện hạt nhân [16].",
        "Bhattacharya et al. reported an investigation of the radiation field "
        "intensity measurement in the core of a pulsed nuclear reactor using "
        "microwave propagation through an appropriately chosen noble gas placed "
        "within the nuclear power reactor [16]."
    )
    P(
        "Meirav và cộng sự đã sử dụng phương pháp quang phổ khối gia tốc, được áp "
        "dụng để đo nồng độ của sản phẩm phân hạt bay hơi có chu kỳ bán rã dài "
        "trong Bể nhiên liệu đã chiếu xạ (Irradiated Fuel Bay - IFB) của một lò "
        "điện hạt nhân và hệ thống Vận chuyển nhiệt chính (Primary Heat Transport - "
        "PHT) [17].",
        "Meirav et al. used the method of accelerator mass spectrometry which is "
        "applied to the measurements of concentrations of the long-lived volatile "
        "fission product in the Irradiated Fuel Bay (IFB) of a nuclear power reactor "
        "and (Primary Heat Transport PHT) system [17]."
    )
    P(
        "Coulon và cộng sự đã sử dụng quang phổ gamma để giám sát công suất của Lò "
        "phản ứng nhanh natri thế hệ thứ tư (Sodium Fast Reactor - SFR) [18]. Mô "
        "phỏng cho thấy có thể giám sát công suất với độ chính xác cao và thời gian "
        "đáp ứng ngắn bằng cách đo các nguồn phát gamma trễ được tạo ra trong natri "
        "lỏng. Suất tạo nguồn phát gamma trong lõi lò được tính toán bằng dữ liệu "
        "kỹ thuật và hạt nhân như mật độ nguyên tử, phổ neutron, vận tốc natri và "
        "thiết diện neutron tới của các phản ứng phân hạt, cũng như các phản ứng "
        "hoạt hóa natri tạo ra nguồn phát gamma.",
        "Coulon et al. used gamma spectrometry to monitor the fourth generation "
        "Sodium Fast Reactor (SFR) nuclear power [18]. Simulation showed that power "
        "monitoring in high accuracy and with short response time is possible "
        "measuring delayed gamma emitters produced in the liquid sodium. Gamma "
        "emitter production rate in the reactor core was calculated with technical "
        "and nuclear data as atomic densities, neutron spectra, sodium velocity and "
        "incident neutron cross-sections of fission reactions, and also sodium "
        "activation reactions producing gamma emitters."
    )
    P(
        "Sang và cộng sự đã báo cáo các ứng dụng của Giao thoa kế quét bước sóng "
        "(Swept Wavelength Interferometry - SWI) trong đo nhiệt độ phân bố bằng sợi "
        "quang trong lò phản ứng hạt nhân, cảm biến gồm 2 đoạn sợi quang chế độ đơn "
        "[19]. Sơ đồ được thể hiện trong Hình 3.",
        "Sang et al. reported the applications of Swept Wavelength Interferometry "
        "(SWI) to distributed fiber-optic temperature measurements in a nuclear "
        "reactor, the sensors consisted of 2 segments of single mode optical fibers "
        "[19]. The sketch is shown in Figure 3."
    )
    FIG(3)
    P(
        "Yarovoi và cộng sự đã áp dụng thiết bị hologram trong chẩn đoán kết cấu của "
        "nhà máy điện hạt nhân. Có khả năng ứng dụng kỹ thuật giao thoa và kỹ thuật "
        "hologram trong điều kiện của nhà máy điện hạt nhân [20].",
        "Yarovoi et al. applied the holographic equipment in diagnosis of NPP "
        "construction. There is a possibility of application of interference and "
        "holographic technique in condition of NPP [20]."
    )

    return b
