# -*- coding: utf-8 -*-
"""Book 9, Chapter 11 (part A) — byline note, ABSTRACT, keywords and the
opening of INTRODUCTION (EN/VI bilingual).

Source: ppic_raw.txt lines 7167-7299 (PDF pp. 271-275, printed pp. 255-259).
The printed title, chapter number, authors and affiliations are rendered by
the page shell, so this module does not repeat title markup; the byline
material appears only as a source note. Bracketed citations [1]-[18] are kept
inline; no reference list is emitted here. FIG 1 and FIG 2 are embedded at
the points indicated by the source. There are no tables or equations here.
"""
import ppicfig11 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


# ---------------------------------------------------------------------------
# Non-overwriting fallbacks for the two figures embedded in this section.
# The supplier modules are authored in parallel; never replace a real callable.
def _fig_fallback(n, title, cap_vi, cap_en):
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 360" '
        'role="img" aria-label="%s"><rect x="1" y="1" width="678" height="358" '
        'fill="#f7f9fc" stroke="#9aa7b8"/><text x="340" y="176" '
        'text-anchor="middle" font-size="18" fill="#1f3555">%s</text>'
        '<text x="340" y="206" text-anchor="middle" font-size="13" '
        'fill="#5a6b80">Figure 11.%d</text></svg>' % (title, title, n)
    )
    return (svg, cap_vi, cap_en, cap_vi, cap_en)


if not hasattr(F, "fig_f01"):
    F.fig_f01 = lambda: _fig_fallback(
        1, "MHTGR-based NSSM",
        "Hình 11.1 · Sơ đồ NSSM dùng MHTGR",
        "Figure 11.1 · Schematic view of an MHTGR-based NSSM")
if not hasattr(F, "fig_f02"):
    F.fig_f02 = lambda: _fig_fallback(
        2, "Micro-grid",
        "Hình 11.2 · Vi lưới điện từ năng lượng hạt nhân và quang điện",
        "Figure 11.2 · A micro-grid constituted by nuclear fission and "
        "photovoltaic energy")


def section(lang):
    b = []

    # --------------------------------------------------------- byline source note
    NOTE(b, lang,
      "<b>Ghi chú nguồn.</b> Tác giả thuộc Viện Công nghệ Năng lượng Hạt nhân "
      "và Năng lượng Mới, Đại học Thanh Hoa, Bắc Kinh 100084, Trung Quốc, và "
      "Phòng Thí nghiệm Trọng điểm về Kỹ thuật và An toàn Lò phản ứng Tiên "
      "tiến, Bộ Giáo dục Trung Quốc, Bắc Kinh 100084, Trung Quốc.",
      "<b>Source note.</b> The author is with the Institute of Nuclear and "
      "New Energy Technology, Tsinghua University, Beijing 100084, China, "
      "and the Key Laboratory of Advanced Reactor Engineering and Safety, "
      "Ministry of Education of China, Beijing 100084, China.")

    # ---------------------------------------------------------------- ABSTRACT
    H(b, lang, "TÓM TẮT", "ABSTRACT", level=2)
    P(b, lang,
      "Các lò phản ứng module nhỏ (Small Modular Reactors, SMRs) là những lò "
      "phản ứng phân hạch hạt nhân có công suất điện đầu ra nhỏ hơn 300 MWe. "
      "Nhờ các đặc tính an toàn vốn có, lò phản ứng làm mát bằng khí nhiệt độ "
      "cao dạng module (Modular High Temperature Gas-cooled Reactor, MHTGR) "
      "được xem là một trong những ứng viên tốt nhất để xây dựng các nhà máy "
      "điện hạt nhân dựa trên SMR với mức độ an toàn cao và tính cạnh tranh "
      "về kinh tế. Điều khiển mức công suất có vai trò then chốt trong việc "
      "cung cấp khả năng thích ứng với lưới điện cho mọi loại SMR. Thường thì, "
      "trong động lực học của nhà máy dựa trên SMR tồn tại tính phi tuyến, "
      "sự bất định tham số và sự bão hòa đầu vào điều khiển. Xuất phát từ "
      "thực tế này, bài báo đề xuất một bộ điều khiển mức công suất thích ứng "
      "bão hòa phản hồi đầu ra mới cho MHTGR.",
      "Small modular reactors (SMRs) are those nuclear fission reactors with "
      "electrical output powers of less than 300 MWe. Due to its inherent "
      "safety features, the modular high temperature gas-cooled reactor "
      "(MHTGR) has been seen as one of the best candidates for building "
      "SMR-based nuclear plants with high safety-level and economical "
      "competitive power. Power-level control is crucial in providing "
      "grid-appropriation for all types of SMRs. Usually, there exists "
      "nonlinearity, parameter uncertainty and control input saturation in "
      "the SMR-based plant dynamics. Motivated by this, a novel saturated "
      "adaptive output-feedback power-level control of the MHTGR is proposed "
      "in this paper.")
    P(b, lang,
      "Bộ luật điều khiển mới xây dựng này có các ưu điểm: hình thức tương "
      "đối gọn, khả năng thích ứng mạnh với sự bất định tham số và khả năng "
      "bù bão hòa đầu vào điều khiển; lần lượt đạt được nhờ xây dựng các hàm "
      "Lyapunov dựa trên ectropy dịch chuyển của động lực học neutron và của "
      "nhiệt thủy lực lò phản ứng, đưa ra thuật toán chỉnh định trực tuyến cho "
      "các tham số bộ điều khiển và đề xuất một bộ bù bão hòa đầu vào điều "
      "khiển. Được chứng minh về mặt lý thuyết rằng tính ổn định đầu vào-trạng "
      "thái (Input-to-State Stability, ISS) có thể được bảo đảm cho hệ thống "
      "vòng lặp kín tương ứng. Để kiểm chứng các kết quả lý thuyết, chiến lược "
      "điều khiển mới này sau đó được áp dụng cho điều khiển cơ động công suất "
      "dải rộng của MHTGR trong nhà máy HTR-PM. Kết quả mô phỏng số cho thấy "
      "không chỉ mối quan hệ giữa hiệu năng điều chỉnh và giới hạn bão hòa đầu "
      "vào điều khiển mà còn cả tính khả thi của việc áp dụng bộ luật điều "
      "khiển thích ứng bão hòa này trong thực tế.",
      "This newly-built control law has the virtues of having relatively "
      "neat form, of being strong adaptive to parameter uncertainty and of "
      "being able to compensate control input saturation, which are given by "
      "constructing Lyapunov functions based upon the shifted-ectropies of "
      "neutron kinetics and reactor thermal-hydraulics, giving an online "
      "tuning algorithm for the controller parameters and proposing a control "
      "input saturation compensator respectively. It is proved theoretically "
      "that input-to-state stability (ISS) can be guaranteed for the "
      "corresponding closed-loop system. In order to verify the theoretical "
      "results, this new control strategy is then applied to the large-range "
      "power maneuvering control for the MHTGR of the HTR-PM plant. Numerical "
      "simulation results show not only the relationship between regulating "
      "performance and control input saturation bound but also the feasibility "
      "of applying this saturated adaptive control law practically.")

    P(b, lang,
      "<b>Từ khóa:</b> lò phản ứng module nhỏ, lò phản ứng làm mát bằng khí "
      "nhiệt độ cao dạng module (MHTGR), khả năng thích ứng với lưới điện, "
      "điều chỉnh công suất thích ứng phi tuyến, bù bão hòa đầu vào",
      "<b>Keywords:</b> small modular reactor, modular high-temperature "
      "gas-cooled reactor (MHTGR), grid-appropriation, nonlinear adaptive "
      "power-level regulation, input saturation compensation")

    # ------------------------------------------------------------ INTRODUCTION
    H(b, lang, "GIỚI THIỆU", "INTRODUCTION", level=2)

    # Nuclear fission energy and small modular reactors
    H(b, lang,
      "Năng lượng hạt nhân và các lò phản ứng module nhỏ",
      "Nuclear fission energy and small modular reactors", level=3)
    P(b, lang,
      "Năng lượng phân hạch hạt nhân là một dạng năng lượng sạch thiết yếu, "
      "có thể đóng vai trò quan trọng trong việc đáp ứng nhu cầu năng lượng "
      "ngày càng tăng của thế giới. An toàn là vấn đề quan trọng nhất đối với "
      "sự phát triển của ngành công nghiệp năng lượng phân hạch hạt nhân, dẫn "
      "đến sự cần thiết phải phát triển các lò phản ứng có đặc tính an toàn "
      "vốn có. Các lò phản ứng module nhỏ (Small Modular Reactors, SMRs) là "
      "những lò phản ứng phân hạch hạt nhân có công suất điện đầu ra nhỏ hơn "
      "300 MWe. Nhờ mật độ công suất thấp và nhiệt dung lớn, một số SMR có "
      "các đặc tính an toàn vốn có — đây là đặc tính tiên tiến nhất của các "
      "nhà máy dựa trên SMR so với các nhà máy điện hạt nhân thông thường, "
      "bảo vệ các SMR này khỏi các nguy cơ nóng chảy lõi, phát tán phóng xạ và "
      "Tai nạn Mất chất làm mát (Loss of Coolant Accidents, LOCAs) [1,2]. Các "
      "SMR có thể mang lại thiết kế module đơn giản hơn, an toàn hơn và chuẩn "
      "hóa nhờ chế tạo tại nhà máy, với vốn đầu tư ban đầu nhỏ hơn và thời "
      "gian xây dựng ngắn hơn, và đã được Cơ quan Năng lượng Nguyên tử Quốc "
      "tế (International Atomic Energy Agency, IAEA) xem là một xu hướng "
      "phát triển của năng lượng hạt nhân. Các SMR có thể có lợi trong việc "
      "cung cấp điện cho các vùng sâu vùng xa không có hạ tầng truyền tải hay "
      "phân phối, trong việc phát điện tại chỗ cho các trung tâm dân cư lớn, "
      "và trong việc phù hợp với các ứng dụng cụ thể như nguồn nhiệt cho các "
      "khu công nghiệp. Thông qua việc áp dụng sơ đồ đa module, tức là nhiều "
      "SMR cùng cấp hơi cho một tổ máy tua-bin/máy phát, các đặc tính an toàn "
      "vốn có có thể được áp dụng cho các nhà máy điện lớn với công suất danh "
      "định bất kỳ mong muốn.",
      "Nuclear fission energy is a crucial type of clean energy that can play "
      "an important role in meeting the world's increasing energy needs. "
      "Safety is the most important issue to the development of the nuclear "
      "fission energy industry, which leads to the necessity of developing "
      "nuclear reactors with inherent safety features. Small modular reactors "
      "(SMRs) are those nuclear fission reactors with electrical output "
      "powers of less than 300 MWe. Due to the low power density and large "
      "heat capacity, some SMRs have inherent safety features which are the "
      "most advanced feature of these SMR-based plants relative to those "
      "conventional nuclear plants and protect these SMRs from the hazards of "
      "core-melting, radiological release and Loss of Coolant Accidents "
      "(LOCAs) [1,2]. SMRs can offer simpler, safer and standardized modular "
      "design by factory-building, smaller initial capital investment, and "
      "shorter construction period, and have been viewed by International "
      "Atomic Energy Agency (IAEA) as a developing trend in nuclear energy. "
      "SMRs could be beneficial in providing electric power to remote areas "
      "without transmission or distribution infrastructure, in generating "
      "local power for a large population center and in being viable for "
      "specific applications such as heat sources for industrial complexes. "
      "Through adopting a multi-modular scheme, i.e., multiple SMRs providing "
      "steam for one turbine/generator set, the inherent safety features can "
      "be applicable to large power plants of any desired power rating.")

    FIG(b, 1, F.fig_f01(), lang)

    # MHTGR-based nuclear steam supplying module
    H(b, lang,
      "Mô-đun cung cấp hơi hạt nhân dựa trên MHTGR",
      "The MHTGR-based nuclear steam supplying module", level=3)
    P(b, lang,
      "Lò phản ứng làm mát bằng khí nhiệt độ cao dạng module (Modular High "
      "Temperature Gas-cooled Reactor, MHTGR) như HTR-Module do Đức thiết kế "
      "[3], dùng helium làm chất làm mát và than chì làm cả chất điều hòa lẫn "
      "vật liệu kết cấu, là một SMR điển hình nổi tiếng với các đặc tính an "
      "toàn vốn có mạnh mẽ [3,4]. Một mô-đun cung cấp hơi hạt nhân dựa trên "
      "MHTGR (Nuclear Steam Supplying Module, NSSM) gồm một MHTGR giường than "
      "một vùng, một máy phát hơi một lần chạy dạng cuộn ống xoắn ốc "
      "(Once-Through Steam Generator, OTSG) bố trí song song với MHTGR và một "
      "số đường ống kết nối — là nền tảng của nhà máy điện hạt nhân hai module "
      "HTR-PM do Viện Công nghệ Năng lượng Hạt nhân và Năng lượng Mới phát "
      "triển và đang được xây dựng tại Đại học Thanh Hoa [5,6] — được thể "
      "hiện trong Hình 1.",
      "The modular high temperature gas-cooled reactor (MHTGR) such as the "
      "HTR-Module designed in Germany [3], which uses helium as coolant and "
      "graphite as both moderator and structural materials, is a typical well "
      "known SMR with strong inherent safety features [3,4]. An MHTGR-based "
      "nuclear steam supplying module (NSSM) composed of a one-zone pebble-bed "
      "MHTGR, a helical-coil once-through steam generator (OTSG) arranged "
      "side-by-side with the MHTGR and some connecting pipes, which is the "
      "basis of the two-modular nuclear plant HTR-PM developed by the Institute "
      "of Nuclear and New Energy Technology and under construction at Tsinghua "
      "University [5,6] is shown in Figure 1.")

    # Micro-grids with load-following SMRs
    H(b, lang,
      "Vi lưới điện với các SMR có khả năng theo dõi tải",
      "Micro-grids with load-following SMRs", level=3)
    P(b, lang,
      "Các SMR có khả năng theo dõi tải thì phù hợp với lưới điện, có thể được "
      "dùng kết hợp với các nguồn năng lượng tái tạo như quang điện "
      "(Photovoltaic, PV) và gió để xây dựng các vi lưới điện có các ưu điểm: "
      "cung cấp điện liên tục, không cần tiếp nhiên liệu phân hạch hạt nhân "
      "thường xuyên và khả năng khử muối nước biển [7] cùng sản xuất hydro "
      "[8]. Hình 2 cho thấy một vi lưới điện điển hình được cấu thành từ một "
      "nhà máy điện hạt nhân dựa trên MHTGR và một nhà máy PV, từ đó có thể "
      "thấy nhiệt do MHTGR sinh ra không chỉ được dùng để phát điện theo tín "
      "hiệu yêu cầu do lưới điện cấp trên và công suất đầu ra của nhà máy PV "
      "cùng xác định, mà còn có thể được dùng để khử muối nước biển.",
      "SMRs with load-following capability are grid-appropriate, which can be "
      "utilized to incorporate with renewable energy sources such as "
      "photovoltaic (PV) and wind to build micro-grids having the virtues of "
      "persistent power supply, free refueling of nuclear fission fuels and "
      "capability of seawater desalination [7] and hydrogen production [8]. "
      "Figure 2 shows a typical micro-grid constituted by an MHTGR-based "
      "nuclear plant and a PV plant, from which we can see that the heat "
      "produced by the MHTGR can be not only utilized to produce electricity "
      "according to the demand signal determined by both the upper-level grid "
      "and outlet power of the PV plant but also can be applied for sea-water "
      "desalination.")

    FIG(b, 2, F.fig_f02(), lang)

    # Prior nonlinear and adaptive power-level control studies
    H(b, lang,
      "Các nghiên cứu trước về điều khiển công suất phi tuyến và thích ứng",
      "Prior studies on nonlinear and adaptive power-level control", level=3)
    P(b, lang,
      "Vì các đặc tính an toàn vốn có làm tăng cường cả tính phi tuyến động "
      "lực học lẫn sự bất định tham số vốn có ở mọi lò phản ứng phân hạch, nên "
      "để thực hiện chức năng theo dõi tải, việc phát triển điều khiển mức "
      "công suất thích ứng phi tuyến cho các SMR vừa cần thiết trong thực tế "
      "vừa có ý nghĩa về mặt học thuật. Cho đến nay, đã có một số hướng tiếp "
      "cận đầy hứa hẹn trong thiết kế điều khiển mức công suất phi tuyến và "
      "thích ứng. Trong lĩnh vực điều khiển lò phản ứng phi tuyến, Shtessel đã "
      "đề xuất một bộ điều chỉnh mức công suất phi tuyến dựa trên điều khiển "
      "trượt và kỹ thuật quan sát cho lò phản ứng không gian TOPAZ II [9]. "
      "Etchepareborda và Eliasi đã đề xuất các phương pháp thiết kế điều "
      "khiển dự báo mô hình phi tuyến (Nonlinear Model Predictive Control, "
      "NMPC) để điều chỉnh mức công suất của các lò phản ứng nước áp lực "
      "(Pressurized Water Reactors, PWRs) [10,11,12]. Dong đã thiết kế một bộ "
      "điều khiển mức công suất tiêu tán phản hồi đầu ra động cho MHTGR [13] "
      "bằng kỹ thuật backstepping [14]. Dựa trên cách tiếp cận thiết kế điều "
      "khiển dựa trên cơ sở vật lý, Dong đã đề xuất một bộ luật điều khiển mức "
      "công suất phản hồi đầu ra động phi tuyến cho MHTGR [15].",
      "Since the inherent safety features intensify both the dynamic "
      "nonlinearity and parameter uncertainty that every fission reactor has, "
      "in order to realize the load-following function, it is practically "
      "necessary and academically meaningful to develop nonlinear adaptive "
      "power-level control for SMRs. Until now, there have been some promising "
      "approaches in the nonlinear and adaptive power-level control design. "
      "In the nonlinear reactor control field, Shtessel proposed a nonlinear "
      "power-level regulator based on sliding mode control and observation "
      "techniques for space reactor TOPAZ II [9]. Etchepareborda and Eliasi "
      "proposed nonlinear model predictive control (NMPC) design methods for "
      "power-level regulation of pressurized water reactors (PWRs) "
      "[10,11,12]. Dong designed a dynamic output feedback dissipation "
      "power-level controller for MHTGRs [13] by using a backstepping "
      "technique [14]. Based on the physically-based control design approach, "
      "Dong proposed a nonlinear dynamic output-feedback power-level control "
      "law for MHTGRs [15].")
    P(b, lang,
      "Trong lĩnh vực thiết kế điều khiển lò phản ứng thích ứng, Park đã trình "
      "bày một bộ điều khiển mức công suất tỷ lệ-tích phân "
      "(Proportional-Integral, PI) với hệ số phản hồi được chỉnh bởi một luật "
      "thích ứng, và chiến lược điều khiển này làm cho hệ thống vòng lặp kín "
      "không chỉ ổn định mà còn thích ứng được với phản hồi độ phản ứng chưa "
      "được mô hình hóa [16]. Arab-Alibeik đã thiết kế một bộ điều khiển mức "
      "công suất thích ứng bằng mạng nơ-ron nhân tạo (Artificial Neural "
      "Network, ANN) đầu vào thuận [17] cho các PWR, và ANN tương ứng được "
      "huấn luyện trực tuyến. Dong đã đề xuất một bộ điều khiển mức công suất "
      "phản hồi đầu ra có bù ANN cho MHTGR [18], và ANN tương ứng chỉ là một "
      "mạng perceptron đa lớp (Multi-Layer Perceptron, MLP) được huấn luyện "
      "trực tuyến bằng một thuật toán do yêu cầu bảo đảm ổn định vòng lặp kín "
      "toàn cục.",
      "In the field of adaptive reactor control design, Park presented a "
      "proportional-integral (PI) power-level controller with feedback gains "
      "adjusted by an adaptive law, and this control strategy makes the "
      "closed-loop system to be not only stable but also adaptive to the "
      "unmodeled reactivity feedback [16]. Arab-Alibeik designed an adaptive "
      "power-level controller by using a feedforward artificial neural network "
      "(ANN) [17] for the PWRs, and the corresponding ANN is trained online. "
      "Dong proposed an ANN-compensated output feedback power-level controller "
      "for MHTGRs [18], and the corresponding ANN is a just multi-layer "
      "perceptron (MLP) that is trained online by an algorithm given by the "
      "need of guaranteeing globally closed-loop stability.")

    # Motivation and contribution of this paper
    H(b, lang,
      "Động lực và đóng góp của bài báo",
      "Motivation and contribution of this paper", level=3)
    P(b, lang,
      "Mặc dù có thể đạt được khả năng thích ứng mạnh dựa trên ANN, nhưng việc "
      "triển khai các bộ điều khiển lò phản ứng thích ứng phi tuyến có bù ANN "
      "phức tạp hơn nhiều so với các luật điều khiển dạng PID được sử dụng "
      "rộng rãi. Hơn nữa, phần lớn các hệ thống điều khiển lò phản ứng thực tế "
      "đều có phần tử bão hòa trong kênh đầu vào điều khiển. Vì vậy, việc "
      "thiết kế các luật điều khiển mức công suất thích ứng đơn giản cho MHTGR "
      "có xét đến bão hòa đầu vào điều khiển là rất cần thiết. Trong bài báo "
      "này, một bộ điều khiển mức công suất thích ứng bão hòa phản hồi đầu ra "
      "mới được trình bày, bộ điều khiển này không chỉ thích ứng được với sự "
      "biến động của các thông số vật lý và nhiệt thủy lực mà còn bù được bão "
      "hòa đầu vào điều khiển. Được chứng minh về mặt lý thuyết rằng bộ điều "
      "khiển thích ứng bão hòa phản hồi đầu ra này có thể bảo đảm tính ổn định "
      "đầu vào-trạng thái (Input-to-State Stability, ISS) cho hệ thống vòng "
      "lặp kín. Hơn nữa, bộ điều khiển mới xây dựng này đơn giản khi triển khai "
      "trong thực tế, và mô phỏng số cho thấy nó có thể cung cấp hiệu năng "
      "điều chỉnh mức công suất thỏa mãn.",
      "Though strong adaptation ability can be realized based on ANNs, "
      "however the implementation of ANN-compensated nonlinear adaptive "
      "reactor controllers is much more complicated than that of the widely "
      "utilized PID-like control laws. Moreover, there exists saturation "
      "element in the control input channel of almost all the practical "
      "reactor control systems. Therefore, it is very necessary to design a "
      "simple adaptive power-level control laws for the MHTGR by considering "
      "control input saturation. In this paper, a novel saturated adaptive "
      "output-feedback power-level control is presented, which can not only "
      "be adaptive to the perturbation of the physical and thermal-hydraulic "
      "parameters but also compensate the control input saturation. It is "
      "proved theoretically that this saturated adaptive output-feedback "
      "controller can guarantee input-to-state stability (ISS) for the "
      "closed-loop system. Furthermore, this newly-built control is simple "
      "for practical implementation, and numerical simulation show that it "
      "can provide satisfactory power-level regulating performance.")

    return b
