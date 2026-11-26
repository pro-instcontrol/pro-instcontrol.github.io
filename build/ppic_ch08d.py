# -*- coding: utf-8 -*-
"""Chapter 8, Shaking Table Test (EN/VI bilingual).

Source: decoded lines 4819-4935 of ``work/ppic_raw.txt`` (PDF pp. 179-185,
printed pp. 163-169), with the section headings and the opening of the test
-model paragraph from lines 4801-4818 and the Table 2 caption on PDF p. 186.
Covers the 1:30 model, similarity requirements, the optimized CBD parameters
(beta = 0.2, Delta = 0.12, xi_d = 0.05), CBD construction, the three CBDs and
their free-vibration attenuation. Figures 2-8, Table 2 and equations (18)-(23).
"""

import ppicfig8 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS

# The vector-figure suppliers may not be integrated yet.  Install neutral,
# non-overwriting fallbacks so that section() is callable during a partial
# build; a real registered fig_fNN() always wins.
def _fig_stub(n, caption_vi, caption_en, alt_vi, alt_en, label):
    from ppicfig8_common import _b, _mk
    tup = _mk(n, _b(30, 50, 620, 60, label), caption_en, caption_vi,
              alt_vi, alt_en)
    return lambda: tup


for _n, _cvi, _cen, _avi, _aen, _label in (
    (2, "Mô hình thí nghiệm bàn rung và kết cấu có CBD1-3",
        "Shaking-table test model and dimensioned structure with CBD1-3",
        "Mô hình thí nghiệm và bố trí CBD", "Test model and CBD layout",
        "Shaking-table model / three coal bucket dampers"),
    (3, "Chế độ dao động kiểm soát chính của kết cấu",
        "Main vibration control mode of the subject structure",
        "Biến dạng tầng ba tại vị trí phễu than", "Third-layer deformation",
        "First short-axis mode of the model"),
    (4, "Hàm truyền của kết cấu với và không có CBD tối ưu",
        "Transfer function of the structure with and without optimal CBDs",
        "Đỉnh cộng hưởng giảm khi có CBD", "Reduced resonance peak",
        "Transfer functions with / without optimal CBDs"),
    (5, "Quan hệ giữa hàm mục tiêu, độ lệch tần số và tỷ lệ cản",
        "Objective function versus frequency deviation and damping ratio",
        "Hàm mục tiêu theo độ lệch tần số và tỷ lệ cản",
        "Objective function surfaces",
        "Objective function at optimal frequency coverage"),
    (6, "Sơ đồ nguyên lý của bộ giảm chấn phễu than",
        "Schematic diagram of a coal bucket damper",
        "Thanh treo, phễu thép, dầm và đầu nối", "Hangers, bucket, beam",
        "Coal bucket damper components"),
    (7, "Các bộ giảm chấn phễu than trong mô hình thí nghiệm",
        "Coal bucket dampers used in the shaking table test model",
        "Mô hình cơ khí, cấu tạo và bố trí CBD", "CBD details and layout",
        "Simplified model, detailed structure and layout"),
    (8, "Đường suy giảm dao động tự do của CBD1-3",
        "Free vibration attenuation curve for CBD1-3",
        "Dao động tự do của ba CBD", "Free attenuation of three CBDs",
        "Manual-excitation free vibration attenuation"),
):
    _name = "fig_f%02d" % _n
    if not hasattr(F, _name):
        setattr(F, _name, _fig_stub(_n, _cvi, _cen, _avi, _aen, _label))

# --------------------------------------------------------------- Table 2
# Printed column order (PDF p. 186): CBD, mass optimal/identified (kg),
# frequency optimal/identified (Hz), damping ratio optimal/identified.
_T2_HEAD_VI = [
    "CBD", "Khối lượng — tối ưu (kg)", "Khối lượng — nhận diện (kg)",
    "Tần số — tối ưu (Hz)", "Tần số — nhận diện (Hz)",
    "Tỷ lệ cản — tối ưu", "Tỷ lệ cản — nhận diện",
]
_T2_HEAD_EN = [
    "CBD", "Mass — optimal (kg)", "Mass — identified (kg)",
    "Frequency — optimal (Hz)", "Frequency — identified (Hz)",
    "Damping ratio — optimal", "Damping ratio — identified",
]
_T2_ROWS = [
    ["1", "140", "140", "15.83", "18.02", "0.05", "0.066"],
    ["2", "140", "140", "19.88", "20.35", "0.05", "0.076"],
    ["3", "140", "140", "17.86", "18.34", "0.05", "0.05"],
    ["Mean", "140", "140", "17.86", "18.90", "0.05", "0.064"],
]
_T2_ROWS_VI = [["Trung bình"] + r[1:] if r[0] == "Mean" else r for r in _T2_ROWS]


def section(lang):
    b = []

    H(b, lang, "Thí nghiệm bàn rung", "Shaking Table Test", level=2)
    H(b, lang, "Mô hình thí nghiệm", "Test Model", level=3)

    P(b, lang,
      "Mô hình thí nghiệm được đơn giản hóa để có các đặc tính động cơ bản "
      "giống như một nhà máy điện than. Mô hình là khung bê tông cốt thép "
      "bốn tầng với ba phễu than bố trí ở tầng ba. Kết cấu được thiết kế "
      "theo Tiêu chuẩn thiết kế chống động đất Trung Quốc [35]. Cường độ "
      "phòng chống là 8 độ (0,2g), và chu kỳ đặc trưng của địa điểm là 0,40 s. "
      "Cột khung có tiết diện 60 × 105 mm, dầm khung ngang có tiết diện "
      "60 × 60 mm, và dầm khung dọc có tiết diện 60 × 105 mm. Tất cả các "
      "cấu kiện của khung nhà máy đều làm bằng bê tông C10; kích thước cụ "
      "thể của mô hình thí nghiệm và sơ đồ cốt thép tiết diện kết cấu được "
      "cho trong Hình 2. Mô hình thí nghiệm được chế tạo với tỷ lệ 1:30. "
      "Các hệ số tương đồng khác được xác định theo lý thuyết tương đồng "
      "và cho trong Bảng 1. Một khối lượng bổ sung 800 kg được đưa vào mỗi "
      "tầng từ tầng một đến tầng ba, và khối lượng bổ sung 200 kg được thêm "
      "vào tầng bốn để mô phỏng sự hiện diện của tải trọng kết cấu. Các "
      "khối lượng bổ sung này được bố trí đều trên mỗi tầng. Cộng với "
      "khối lượng của bản thân kết cấu, tổng khối lượng của mô hình thí "
      "nghiệm là 4122 kg. Trong tổng số đó, 420 kg ở tầng ba chiếm khối "
      "lượng của các phễu than, tức khoảng 10,2% tổng trọng lượng của kết cấu.",
      "The current test model is simplified to provide the same basic "
      "structural dynamic characteristics as a coal-fired power plant. The "
      "test model is a four-story reinforced concrete frame structure with "
      "three coal buckets arranged at the third story. The structure is "
      "designed according to the Chinese Seismic Design Code [35]. The "
      "fortification intensity is 8 degrees (0.2g), and the site "
      "characteristic period is 0.40 s. The frame columns consist of "
      "60 × 105 mm sections, the transverse frame beams are 60 × 60 mm "
      "sections, and the longitudinal frame beams are 60 × 105 mm sections. "
      "All components of the power plant frame are constructed of C10 "
      "concrete, and the specific dimensions of the test model and the "
      "structural section reinforcement diagrams are provided in Figure 2. "
      "The test model is constructed to a 1:30 scale. Other similarity "
      "coefficients are determined according to similarity theory and are "
      "given in Table 1. An additional mass of 800 kg is included on each "
      "of the first to third stories, and an additional mass of 200 kg is "
      "added to the fourth story to replicate the presence of structure "
      "loading. These additional masses are uniformly arranged on each "
      "story. Including the mass of the structure, the total mass of the "
      "test model is 4122 kg. Of this total mass, 420 kg on the third layer "
      "accounts for the mass of the coal buckets, or about 10.2% of the "
      "total weight of the structure.")
    FIG(b, 2, F.fig_f02(), lang)

    H(b, lang, "Thông số và thiết kế của CBD", "CBD Parameters and Design",
      level=3)

    P(b, lang,
      "Trước hết, các đặc tính động của kết cấu được xác định, sau đó các "
      "thông số thiết kế của CBD được xác định theo phương pháp trình bày "
      "chi tiết trong Mục 2.1. Để thuận tiện cho việc bố trí thiết bị, hướng "
      "trục ngắn đã được chọn là hướng tải trong thí nghiệm. Theo đó, chế "
      "độ hình thứ nhất theo trục ngắn của kết cấu được chọn làm chế độ "
      "kiểm soát chính. Trước hết, một mô hình phân tích phần tử hữu hạn "
      "(FEA) bằng SAP2000 của kết cấu khi chưa có CBD được xây dựng, và các "
      "đặc tính động chính của kết cấu được thu bằng phân tích chế độ. Chế "
      "độ dao động kiểm soát chính của kết cấu được thể hiện trong Hình 3. "
      "Trong biến dạng chế độ của kết cấu, các chuyển vị tại vị trí các "
      "phễu than được chọn làm biến dạng tầng ba.",
      "The dynamic characteristics of the structure were first obtained, and "
      "then the design parameters of the CBDs were determined according to "
      "the method detailed in Section 2.1. In order to facilitate the "
      "arrangement of equipment, the short-axis direction was selected as "
      "the loading direction in the test. Accordingly, the first, "
      "short-axis mode of the structure was chosen as the main control mode. "
      "First, an SAP2000 finite element analysis (FEA) model of the structure "
      "without CBDs was constructed, and the main dynamic characteristics of "
      "the structure were obtained by modal analysis. The main vibration "
      "control mode of the structure is shown in Figure 3. In the deformation "
      "of structure mode, the displacements where the coal buckets located "
      "are selected as the third-layer deformation.")
    FIG(b, 3, F.fig_f03(), lang)

    P(b, lang,
      "Theo hàm mục tiêu và các thông số đặc tính động của chế độ kiểm soát "
      "chính, các thông số thiết kế tối ưu của CBD được xác định bằng thuật "
      "toán số với kết quả sau: βₒₚₜ = 0,2, Δₒₚₜ = 0,12 và ξdₒₚₜ = 0,05. "
      "Hình 4 mô tả hàm truyền của chế độ đã xác định của kết cấu với và "
      "không có CBD, được thiết kế theo quy trình tối ưu hóa nêu trên. Hai "
      "đường cong cắt nhau tại các điểm P và Q, nằm giữa là vùng làm việc "
      "kiểm soát giảm chấn [36]. Dải tần số của vùng làm việc là 17,715–"
      "22,065 Hz.",
      "According to the objective function and the dynamic characteristic "
      "parameters of the main control mode, the optimal design parameters of "
      "the CBDs were determined by numerical algorithm with the following "
      "results: βₒₚₜ = 0.2, Δₒₚₜ = 0.12, and ξdₒₚₜ = 0.05. Figure 4 depicts "
      "the transfer function of the specified mode of the structure with and "
      "without CBDs, designed based on the above optimization procedure. The "
      "two curves intersect at points P and Q, between which is the damping "
      "control operating range [36]. The frequency range of the operating "
      "range is 17.715–22.065 Hz.")
    FIG(b, 4, F.fig_f04(), lang)

    P(b, lang,
      "Dưới mức phủ tần số tối ưu, βₒₚₜ = 0,2, sự biến đổi không gian của "
      "giá trị hàm mục tiêu theo tỷ lệ cản ξd và độ lệch tần số Δ được thể "
      "hiện trong Hình 5. Độ lệch của giá trị hàm mục tiêu nhỏ hơn 5% khi "
      "các yêu cầu của (17) được thỏa mãn, được lấy làm yêu cầu thiết kế "
      "như sau:",
      "Under the optimal frequency coverage rate, βₒₚₜ = 0.2, the spatial "
      "variation of the objective function value with the damping ratio ξd "
      "and frequency deviation Δ is shown in Figure 5. The deviation rate of "
      "the objective function value is less than 5% when the requirements of "
      "(17) are satisfied, which are taken as the design requirements such "
      "that")

    E(b, lang,
      "Δₒₚₜ − 0,05 < Δ < Δₒₚₜ + 0,05;   ξdₒₚₜ − 0,02 < ξd < ξdₒₚₜ + 0,02",
      "Δₒₚₜ − 0.05 < Δ < Δₒₚₜ + 0.05;   ξdₒₚₜ − 0.02 < ξd < ξdₒₚₜ + 0.02",
      num="18")
    FIG(b, 5, F.fig_f05(), lang)

    P(b, lang,
      "Như thể hiện trong Hình 6, một CBD chủ yếu gồm các thanh treo, một "
      "phễu than bằng thép, các phần tử đàn hồi và bộ giảm chấn. Các thanh "
      "treo chịu trọng lượng của CBD và đồng thời cung cấp độ cứng dao động. "
      "CBD được nối ngang với các cột khung bằng các phần tử đàn hồi và bộ "
      "giảm chấn. Tần số của CBD được điều chỉnh bằng cách thay đổi độ cứng "
      "của các phần tử đàn hồi. Khi CBD và các cột khung chuyển động tương "
      "đối với nhau, bộ giảm chấn tạo ra lực cản tăng cường để hạn chế phạm "
      "vi chuyển động. Yêu cầu thiết kế về tỷ lệ cản của CBD được đáp ứng "
      "bằng cách điều chỉnh các thông số của phần tử giảm chấn.",
      "As shown in Figure 6, a CBD mainly consists of hanger rods, a steel "
      "coal bucket, elastic elements, and dampers. The hanger rods support "
      "the weight of the CBD and simultaneously provide oscillating "
      "stiffness. The CBD is horizontally connected to the frame columns by "
      "the elastic elements and dampers. The frequency of the CBD is "
      "adjusted by adjusting the stiffness of the elastic elements. When the "
      "CBD and the frame columns move relative to one another, the dampers "
      "provide enhanced damping force to limit the range of movement. The "
      "design requirements of the CBD damping ratio are met by adjusting "
      "the parameters of the damping elements.")
    FIG(b, 6, F.fig_f06(), lang)

    P(b, lang,
      "Các CBD dùng trong thí nghiệm bàn rung có cấu tạo tương tự thiết bị "
      "minh họa trong Hình 6. Phần tử đàn hồi là một dầm đơn giản làm bằng "
      "tấm thép, như trong Hình 7. Độ cứng biến dạng ngang của mỗi CBD được "
      "cung cấp bởi độ cứng đung đưa và độ cứng biến dạng của dầm đơn giản "
      "này. Hình 7(a) mô tả mô hình cơ khí đơn giản hóa của hệ CBD, cho các "
      "phương trình động sau trong trường hợp góc đung đưa nhỏ:",
      "The CBDs used in the shaking table test are of similar construction "
      "to the device illustrated in Figure 6. The elastic element is a simply "
      "supported beam made of steel plate, as shown in Figure 7. The "
      "horizontal deformation stiffness of each CBD is provided by the "
      "swinging stiffness and deformation stiffness of this simply supported "
      "beam. Figure 7(a) depicts a simplified mechanical model of the CBD "
      "system, yielding the following dynamic equations in the case of a "
      "small swing angle:")

    E(b, lang,
      "M = −mgh sin θ − kh² sin θ cos θ,",
      "M = −mgh sin θ − kh² sin θ cos θ,",
      num="19")
    E(b, lang, "M = Jβ,", "M = Jβ,", num="20")

    P(b, lang,
      "trong đó M là mô-men của lực, m là khối lượng treo, g là gia tốc "
      "trọng trường, h là chiều cao treo, θ là góc đung đưa, k = 48EI/l³ là "
      "độ cứng biến dạng đàn hồi của dầm đơn giản, E và I lần lượt là mô-đun "
      "Young và mô-men quán tính của tiết diện, J = mh² là mô-men quán tính "
      "của con lắc, và β = d²θ/dt² là gia tốc góc của CBD. Phiên bản đơn "
      "giản hóa của (19) có thể viết như sau:",
      "where M is the moment of force, m is the suspended mass, g is the "
      "gravitational acceleration, h is the height of suspension, θ is the "
      "swing angle, k = 48EI/l³ is the elastic deformation stiffness of the "
      "simply supported beam, E and I are Young's modulus and section moment "
      "of inertia, respectively, J = mh² is the moment of inertia of a "
      "pendulum, and β = d²θ/dt² is the angular acceleration of the CBD. The "
      "simplified version of (19) can then be written as follows:")

    E(b, lang,
      "d²θ/dt² + (g/h) sin θ + (k/m) sin θ cos θ = 0.",
      "d²θ/dt² + (g/h) sin θ + (k/m) sin θ cos θ = 0.",
      num="21")

    P(b, lang, "Và khi góc đung đưa nhỏ, kết quả là",
      "And when the swing angle is small, the result is")

    E(b, lang, "ω = √(g/h + k/m).", "ω = √(g/h + k/m).", num="22")

    P(b, lang,
      "Cấu tạo chi tiết của các CBD dùng trong thí nghiệm bàn rung được thể "
      "hiện trong Hình 7(b). Phễu than được nâng lên cấp kết cấu của nó và "
      "nối vào điểm giữa nhịp của tấm thép. Các liên kết dầm đơn giản được "
      "cung cấp bởi các đầu nối đặc biệt. Góc trên bên trái của Hình 7(b) "
      "cho thấy các đầu nối này, gồm lỗ cố định và lỗ rãnh. Một đầu của tấm "
      "thép được nối bằng đinh tán qua các lỗ cố định, tạo liên kết bản lề, "
      "và đầu kia được nối bằng đinh tán qua các lỗ rãnh, tạo liên kết con "
      "lăn. Tất cả các đầu nối đều được cố định vào đáy cột khung. Trong thí "
      "nghiệm bàn rung, ba CBD được bố trí trong mô hình thí nghiệm như "
      "trong Hình 7(c). Theo yêu cầu thiết kế về tỷ lệ tần số, tần số của "
      "các CBD được xác định, sau đó độ cứng biến dạng của dầm đơn giản, "
      "tính theo (23), được xác định. Yêu cầu về độ cứng được đáp ứng bằng "
      "cách thay đổi kích thước tiết diện của tấm thép, như trong Hình 7(b):",
      "The detailed construction of the CBDs used in the shaking table test "
      "is shown in Figure 7(b). The coal bucket is hoisted to its structural "
      "level and connected to the midspan of the steel plate. The simply "
      "supported beam constraints are provided by special connectors. The "
      "upper left corner of Figure 7(b) shows these connectors, which consist "
      "of fixed holes and slotted holes. One end of the steel plate is "
      "connected by rivets through the fixed holes, providing a pinned "
      "connection, and the other end of the steel plate is connected by "
      "rivets through slotted holes, providing a roller connection. All "
      "connectors are fixed to the bottom of the frame column. In the "
      "shaking table test, three CBDs were arranged in the test model as "
      "shown in Figure 7(c). According to the design requirements dictated "
      "by the frequency ratio, the frequencies of the CBDs were determined, "
      "and then the deformation stiffness of the simply supported beam, "
      "calculated using (23), was determined. The stiffness requirement was "
      "met by changing the section size of the steel plate, which is shown "
      "in Figure 7(b):")

    E(b, lang, "k = m(λ²ω² − g/h).", "k = m(λ²ω² − g/h).", num="23")
    FIG(b, 7, F.fig_f07(), lang)

    P(b, lang,
      "Đặc tính dao động của các CBD được thu bằng thí nghiệm kích thích "
      "thủ công. Với một dao động ban đầu cho trước, độ suy giảm dao động "
      "tự do của ba CBD được thể hiện trong Hình 8. Các thông số tối ưu và "
      "nhận diện của ba CBD được cho trong Bảng 2. Khoảng tỷ lệ tần số giữa "
      "ba CBD có phần khác với giả định lý thuyết, nhưng độ phủ tần số về "
      "cơ bản phù hợp với yêu cầu thiết kế tối ưu. Đáng chú ý là biên độ "
      "dao động của CBD ảnh hưởng đến tỷ lệ cản của chúng. Nhìn chung, biên "
      "độ dao động càng lớn thì tỷ lệ cản càng cao. Vì tỷ lệ cản của CBD "
      "duy trì trong khoảng 0,05 đến 0,076, có thể coi các thông số tổng thể "
      "đáp ứng yêu cầu thiết kế tối ưu. Nhìn chung, các thông số thí nghiệm "
      "đáp ứng yêu cầu của tính toán mục tiêu.",
      "The vibration characteristics of the CBDs were obtained through a "
      "manual excitation test. At a given initial vibration, the resulting "
      "free vibration attenuations of the three CBDs are as shown in Figure "
      "8. The optimal and identified parameters of the three CBDs are shown "
      "in Table 2. The frequency ratio intervals between the three CBDs are "
      "somewhat different from the theoretical assumption, but the frequency "
      "coverage is basically consistent with the optimal design requirements. "
      "Notably, the vibration amplitude of the CBDs will affect the damping "
      "ratio of the CBDs. Generally, the greater the vibration amplitude, the "
      "bigger the damping ratio. Because the damping ratio of the CBDs is "
      "maintained between 0.05 and 0.076, the overall parameters can be "
      "considered to meet the optimal design requirements. As a whole, the "
      "experiment parameters meet the requirements of the target calculation.")

    TBL(b, lang, _T2_HEAD_VI, _T2_HEAD_EN,
        _T2_ROWS_VI if lang == "vi" else _T2_ROWS,
        caption_vi="Bảng 8.2 · Thông số của ba bộ giảm chấn phễu than.",
        caption_en="Table 8.2 · Parameters of the three coal bucket dampers.")
    FIG(b, 8, F.fig_f08(), lang)

    return b
