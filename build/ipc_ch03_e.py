# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III", section 3.3 "Measurement of Flow"
(EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 169-174, printed pp. 157-162,
decoded text lines 6411-6684.  This module covers the start of 3.3,
3.3.1 Introduction and 3.3.2 "Derivation of Universal Flow Formula".
Figures 3.31 and 3.32 are taken from the shared ``ipcfig3`` registry.
The decoded text garbles the Bernoulli and continuity steps; equations
(3.11)-(3.19) are reconstructed with standard notation from the printed
page images, preserving the 1 ft3 / 62.4 lbm worked example and every
printed constant.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # --------------------------------------------------------------- 3.3
    H(b, lang, "3.3 Đo lưu lượng", "3.3 Measurement of Flow")

    # ------------------------------------------------------------- 3.3.1
    H(b, lang, "3.3.1 Mở đầu", "3.3.1 Introduction", level=3)

    P(b, lang,
      "Đồng hồ đo lưu lượng là thiết bị đo tốc độ dòng chảy hoặc số lượng của "
      "chất lưu đang chuyển động trong kênh mở hoặc đường ống kín. Đây là một "
      "trong bốn biến công nghệ cơ bản của bất kỳ ngành công nghiệp nào, bởi vì "
      "phép đo và điều khiển dòng chảy chất lưu là yếu tố thiết yếu để vận hành "
      "trơn tru các nhà máy công nghệ.",
      "Flow meter is a device that measures the rate of flow/quantity of a moving "
      "fluid in an open/closed channel/pipe. This is one of the four basic process "
      "variables of any process industry because measurement and control of fluid "
      "flow is the essential feature for smooth operation of the process plants.")

    P(b, lang,
      "Các thiết bị chính của đồng hồ đo lưu lượng, lắp bên ngoài hoặc bên trong "
      "đường ống, tạo ra tín hiệu đo tỷ lệ với lưu lượng và thay đổi theo sự "
      "tương tác của chất lưu với thiết bị chính. Các thiết bị phụ của đồng hồ đo "
      "lưu lượng đáp ứng tín hiệu nhận được từ thiết bị chính và chuyển đổi tín "
      "hiệu đó thành các chỉ thị thích hợp hoặc tạo ra tín hiệu đầu ra tỷ lệ để "
      "xử lý tiếp.",
      "Flow meter primary devices, mounted externally or internally on the pipeline "
      "produce measurement signal proportional to flow which vary according to "
      "interaction of the fluid to the primary device. Flow meter secondary devices "
      "respond to the signal obtained from the primary device and convert these to "
      "suitable displays or present a proportional output signal for further "
      "manipulations.")

    P(b, lang,
      "Các thiết bị chính gồm tấm chắn, đường ống thượng lưu hoặc hạ lưu, thiết bị "
      "chỉnh lưu dòng và chi tiết lấy tín hiệu. Bộ truyền áp suất chênh, van đa tụ "
      "và mặt bích hoặc phụ kiện, ống dẫn hoặc dây dẫn kết nối, cùng hệ thống cấp "
      "khí nén hoặc điện cần thiết đều là các thành phần của thiết bị phụ.",
      "Primary devices include orifice, upstream/downstream piping, flow conditioners "
      "and tapping details. The differential pressure transmitter, manifold valves "
      "and flanges/fittings, connecting tubing or wiring, required pneumatic or "
      "electrical supply system are all elements of secondary devices.")

    P(b, lang,
      "Về cơ bản, lưu lượng được đo theo hai cách: một là dạng lưu lượng tức thời, "
      "tức là lưu lượng trên một đơn vị thời gian, và hai là dạng tổng thể tích "
      "dòng chảy hoặc tổng khối lượng dòng chảy trong một khoảng thời gian xác định.",
      "Basically flow is measured in two ways, one in the form of flow rate, i.e. "
      "flow per unit time and the second in the form of total volume flow or total "
      "mass flow for a specified duration.")

    P(b, lang,
      "Trong phép đo lưu lượng công nghệ, nhiều thuộc tính của chất lưu được xem "
      "xét, ví dụ số Reynolds, độ nhớt, khối lượng riêng, trọng lực riêng, khả năng "
      "nén, nhiệt độ, áp suất, vận tốc chất lưu, v.v. Kiểu dòng chảy, tức là tầng "
      "hay rối, được quyết định bởi số Reynolds. Số Reynolds (Rd) là lực quán tính "
      "trên một đơn vị lực nhớt của bất kỳ dòng chất lưu nào. Với dòng tầng, Rd lên "
      "tới 2100, còn với dòng rối có thể từ 4000 đến 1000,000. Vận tốc của chất lưu "
      "tại điểm mà đặc tính dòng tầng vừa kết thúc và mức khởi đầu của dòng rối sắp "
      "bắt đầu được gọi là vận tốc tới hạn. Nhìn chung, đặc tính dòng chảy về bản "
      "chất đầy rẫy sự rối.",
      "In the measurement of process flow, many properties of the fluids are taken "
      "into account, e.g. Reynold number, viscosity, density, specific gravity, "
      "compressibility, temperature, pressure, fluid velocity, etc. Type of flow "
      "i.e. laminar or turbulent is decided by Reynold number. Reynold number (Rd) "
      "is 'Inertia force per unit viscous force' for any fluid flow stream. For "
      "laminar flow Rd is upto 2100 and for turbulent flow it can be from 4000 to "
      "1000,000. The velocity of fluid where characteristic of laminar flow just "
      "ends and initial level of turbulence is about to start is called critical "
      "velocity. Flow characteristics, in general, are full of turbulence in nature.")

    P(b, lang,
      "Khả năng đo dải của dòng tầng thường là 100:1, nhưng trong trường hợp dòng "
      "rối nói chung chỉ bị hạn chế ở 4:1. Áp suất chênh do tấm chắn tạo ra tỷ lệ "
      "thuận trực tiếp với lưu lượng đối với dòng tầng, và độ chính xác đo đáng kể "
      "trên toàn bộ dải của thang đo. Nhưng với dòng rối thì quan hệ hoàn toàn "
      "khác. Ở đây lưu lượng tỷ lệ với căn bậc hai của áp suất chênh. Rõ ràng, độ "
      "chính xác đo không thể được xác định ở đầu dưới của thang đo, nơi thang đo "
      "bị co lại so với đầu trên. Độ chính xác của cách bố trí này có thể đạt trong "
      "khoảng ± 0,5 đến 1,0 %.",
      "Measurement rangeability of laminar flow is usually 100:1 but in case of "
      "turbulent flow, it is generally restricted to 4:1. Differential pressure "
      "created by an orifice is directly proportional to flow rate for laminar flow "
      "and accuracy of measurement is significant for whole of the range of scale. "
      "But in case of turbulent flow, the relation is completely different. The "
      "flow rate here is proportional to the square root of differential pressure. "
      "Obviously, the accuracy of measurement cannot be ascertained in the lower "
      "range of the measurement scale where the scale gets shrinked with respect to "
      "upper scale. Accuracy of measurement for such an arrangement can be expected "
      "in the range of ± 0.5 to 1.0%.")

    # ------------------------------------------------------------- 3.3.2
    H(b, lang, "3.3.2 Suy luận công thức lưu lượng tổng quát",
      "3.3.2 Derivation of Universal Flow Formula", level=3)

    P(b, lang,
      "Bất cứ khi nào dòng chất lưu đi qua một chỗ thu hẹp, mặt cắt ngang hiệu dụng "
      "của dòng bị giảm, dẫn đến tăng vận tốc và do đó tăng động năng, kèm theo sự "
      "mất tương ứng năng lượng áp suất. Sự mất hoặc giảm áp suất có thể được suy ra "
      "như một thước đo lưu lượng; xem Hình 3.31.",
      "Whenever a flow stream passes through a restriction, the effective cross-section "
      "of the stream is reduced resulting in increase in velocity and hence the kinetic "
      "energy at a corresponding loss of pressure energy. The loss or drop in pressure "
      "can be inferred as a measure of flow, refer to the Figure 3.31.")

    # Figure suppliers are prepared by a separate module; include each figure
    # as soon as the shared registry exposes it.
    if hasattr(F, "fig_f31"):
        FIG(b, 31, F.fig_f31(), lang)

    P(b, lang,
      "Nếu dòng chất lưu song song với kênh (vận tốc dòng ở đây được coi là giá trị "
      "trung bình trên toàn kênh) thì dòng được gọi là dòng song song hoặc dòng nhớt "
      "(không có chuyển động cắt ngang của dòng chất lưu). Loại dòng này chỉ xảy ra "
      "khi vận tốc chất lưu thấp hoặc với chất lỏng có độ nhớt cao.",
      "If the fluid stream is parallel to the channel (flow velocity here is considered "
      "averaged through the channel) the flow is said to be streamlined or viscous "
      "(no motion of fluid stream across the stream). Such flow occurs only at low "
      "fluid velocity or with high viscosity liquids.")

    P(b, lang,
      "Nếu vận tốc dòng bị tăng lên, kiểu dòng chảy bị nhiễu loạn và kết quả là một "
      "số phần của dòng cũng có thể có thành phần vận tốc cắt ngang kênh. Sự thay đổi "
      "vận tốc ngang này có thể thấy từ mức rất nhỏ đến những xoáy dữ dội. Loại dòng "
      "liên quan đến hiệu ứng này được gọi là dòng rối. Tác động xoáy của dòng rối "
      "đôi khi có thể trở nên nhanh đến mức đường đi của chất lưu trở thành xoắn ốc; "
      "khi đó có thể gọi là dòng xoáy. Hiệu ứng này có thể được giảm thiểu bằng các "
      "cánh chấn lưu lắp trong đường dòng. Loại dòng phổ biến nhất là dòng rối, vì "
      "vậy các phân tích ở đây chỉ liên quan đến loại này. Những nhiễu loạn của dòng "
      "rối, trong đó áp suất và vận tốc đều thay đổi nhanh, cũng có thể được giảm "
      "thiểu bằng cách lắp một bình chứa có dung tích lớn. Tuy nhiên, để đạt độ chính "
      "xác đo thực tế, sự dao động lưu lượng tới ± 20 % vẫn được chấp nhận theo tiêu "
      "chuẩn công nghiệp.",
      "If the flow velocity in raised the flow pattern gets disturbed and as a result "
      "some part of the stream might acquire velocity components across the channel "
      "as well. Such change in the transverse velocity is seen from a very small "
      "amount to violent swirlings. The type of flow associated with this effect is "
      "named as turbulent flow. The swirling action associated with the turbulent "
      "flow at times may become so rapid that the flow path of the fluid become "
      "helical. This may be called swirling flow. This effect may be minimized by "
      "means of dampening vanes installed in the flow path. The most general type "
      "of flow is the turbulent one and therefore, the treatments shall be related "
      "to that only. The disturbances in case of the turbulent flow where pressure "
      "as well as velocity change fast can be minimized by installing a reservoir "
      "of large capacity as well. For practical measurement accuracy, flow "
      "fluctuation upto the extent of ± 20% however, is acceptable as industry "
      "standards.")

    P(b, lang,
      "Xem Hình 3.32 và giả sử 1 ft³ thể tích chất lỏng có khối lượng riêng "
      "ρ₁ = 62,4 lbm/ft³ đi qua mặt cắt được chỉ ra trong sơ đồ.",
      "Refer to Figure 3.32, and assume that 1 ft³ volume of liquid having density "
      "ρ₁ = 62.4 lbm/ft³ cross the section indicated in the diagram.")

    if hasattr(F, "fig_f32"):
        FIG(b, 32, F.fig_f32(), lang)

    P(b, lang,
      "Trong giả thiết này, chủ yếu có ba loại năng lượng liên quan:",
      "In this assumption mainly three kinds of energy are involved:")

    L(b, lang,
      ["(i) Năng lượng thế = ρ₁Z₁g (trong đó Z₁ là chiều cao so với một mốc tham "
       "chiếu và g là gia tốc trọng trường)",
       "(ii) Năng lượng động = ½ρ₁V₁² (trong đó V₁ là vận tốc tại đầu vào)",
       "(iii) Năng lượng áp suất = p₁v₁ (trong đó p₁ và v₁ lần lượt là áp suất và "
       "thể tích tại đầu vào)"],
      ["(i) Potential Energy = ρ₁Z₁g (where Z₁ is the height with respect to a "
       "reference and g is acceleration due to gravity)",
       "(ii) Kinetic Energy = ½ρ₁V₁² (where V₁ is velocity at inlet end)",
       "(iii) Pressure energy = p₁v₁ (where p₁ and v₁ are inlet pressure and "
       "volume respectively)"],
      ordered=True)

    P(b, lang,
      "Tất cả các biến này sẽ biểu diễn giá trị ở điều kiện đầu ra khi chỉ số được "
      "dùng là 2.",
      "All these variables shall represent that of outlet condition when the subscript "
      "used shall be 2.")

    P(b, lang,
      "Trong giả thiết trên, có thể có các dạng năng lượng khác, ví dụ nhiệt năng và "
      "ma sát (cuối cùng cũng tự chuyển thành nhiệt). Trở lực do ma sát trong dòng "
      "chất lưu cũng có thể được biểu diễn bằng độ nhớt, một tính chất vật lý của "
      "chất lỏng đang chuyển động. Độ nhớt được biểu diễn bằng POISE, tương ứng với "
      "dynes/cm² trên một đơn vị gradient vận tốc qua lớp nằm giữa thành ống và chất "
      "lỏng đang chảy. Một chất lưu đang chuyển động có độ nhớt tuyệt đối bằng 1 "
      "poise khi một lực 1 dyne tác dụng có xu hướng dịch chuyển một mặt phẳng có "
      "diện tích mặt cắt ngang 1 cm² với vận tốc 1 cm/giây, song song với một mặt "
      "phẳng tham chiếu đặt cách mặt phẳng chuyển động 1 cm. Ảnh hưởng của nhiệt độ "
      "đến độ nhớt rất rõ rệt. Khi nhiệt độ tăng thì độ nhớt của chất lỏng giảm, "
      "nhưng với khí thì tác động lại ngược lại. Chính độ nhớt là phước lành ngụy "
      "trang chịu trách nhiệm duy nhất việc dập tắt dao động do các khúc cong và van "
      "trên đường ống tạo ra.",
      "In above assumption, there may be other forms of energy, e.g. heat energy, "
      "friction (which also is ultimately converted to heat itself). The resistance "
      "due to friction in fluid flow can also be represented in terms of viscosity, "
      "a physical property of liquid in motion. It is expressed as POISE which can "
      "be represented as dynes/cm² per unit of velocity gradient across the layer "
      "between the pipe and the flowing liquid. A fluid in motion shall have an "
      "absolute viscosity of 1 poise when an applied force of 1 dyne tends to move "
      "a plane of cross-sectional area 1 cm² at a velocity of 1 cm/sec., parallel "
      "to a reference plane placed 1 cm away from the moving plane. The effect of "
      "temperature on viscosity is marked. As the temperature is increased, "
      "viscosity is decreased for a liquid, but for gas the effect is just the "
      "reverse. It is the viscosity which is blessing in disguise that is solely "
      "responsible for suppression of pulsation created by pipeline bends and valves.")

    P(b, lang,
      "Xét 1 pound chất lưu đi vào đường ống qua đầu vào và nếu không có sự tích tụ "
      "nào xảy ra thì lượng chất lưu đó sẽ đi qua hoàn toàn đầu ra. Vì vậy, ta có "
      "thể viết,",
      "Consider 1 pound of fluid entering the pipe through inlet and if no "
      "accumulation is perceived, the quantity shall cross through the outlet "
      "completely. Hence, we can write,")

    E(b, lang,
      "1 × Z₁ × g + ½ × 1 × V₁² + p₁v₁ + I₁ = 1 × Z₂ × g + ½ × 1 × V₂² + p₂v₂ + I₂",
      "1 × Z₁ × g + ½ × 1 × V₁² + p₁v₁ + I₁ = 1 × Z₂ × g + ½ × 1 × V₂² + p₂v₂ + I₂",
      num="3.11")

    P(b, lang,
      "(trong đó I₁ và I₂ là năng lượng bên trong tại đầu vào và đầu ra, tương "
      "ứng) hay, sau khi chia cho đơn vị khối lượng, Z₁g + V₁²/2 + p₁v₁ + I₁ = "
      "Z₂g + V₂²/2 + p₂v₂ + I₂.",
      "(where I₁ and I₂ are internal energy at the inlet and the outlet "
      "respectively) or, after dividing by the unit mass, Z₁g + V₁²/2 + p₁v₁ + I₁ "
      "= Z₂g + V₂²/2 + p₂v₂ + I₂.")

    P(b, lang,
      "Nếu nhiệt độ của hệ không đổi thì năng lượng bên trong cũng không đổi. Do "
      "đó, Z₁g + V₁²/2 + p₁v₁ = Z₂g + V₂²/2 + p₂v₂.",
      "If the temperature of the system remains same, then internal energy becomes "
      "same. Hence, Z₁g + V₁²/2 + p₁v₁ = Z₂g + V₂²/2 + p₂v₂.")

    P(b, lang,
      "Để áp dụng phương trình này cho chất lỏng, ta có thể giả thiết v₁ = v₂ = "
      "1/ρ₁ = 1/ρ₂ = 1/ρ (vì chất lỏng không nén được nên khối lượng riêng và thể "
      "tích riêng không đổi). Do đó phương trình có dạng Z₁g + V₁²/2 + p₁/ρ = "
      "Z₂g + V₂²/2 + p₂/ρ, hay Z₁ + V₁²/(2g) + p₁/(ρg) = Z₂ + V₂²/(2g) + p₂/(ρg).",
      "To apply this equation for a liquid, we can assume that v₁ = v₂ = 1/ρ₁ = "
      "1/ρ₂ = 1/ρ (since the liquid is incompressible and hence density and "
      "specific volume remain constant). Hence, the equation takes the form Z₁g + "
      "V₁²/2 + p₁/ρ = Z₂g + V₂²/2 + p₂/ρ, or Z₁ + V₁²/(2g) + p₁/(ρg) = Z₂ + "
      "V₂²/(2g) + p₂/(ρg).")

    P(b, lang,
      "Bây giờ, vì (Z₁ + p₁/(ρg)) − (Z₂ + p₂/(ρg)) tương đương với h, cột áp chênh "
      "được tạo ra, nên (V₂² − V₁²)/(2g) = h, hay",
      "Now since (Z₁ + p₁/(ρg)) − (Z₂ + p₂/(ρg)) is equivalent to h, the "
      "differential head created and therefore, (V₂² − V₁²)/(2g) = h, or")

    E(b, lang, "V₂² − V₁² = 2gh", "V₂² − V₁² = 2gh", num="3.12")

    P(b, lang,
      "Dựa trên phương trình dòng chất lỏng này, lưu lượng thể tích trên giây Q qua "
      "mặt cắt được cho bởi Q = A₁V₁ = A₂V₂, hay V₁ = A₂V₂/A₁. Thay vào phương trình "
      "3.12 ta có V₂² − V₁² = V₂² − V₂² × A₂²/A₁² = V₂²[1 − A₂²/A₁²] = 2gh. Đặt "
      "A₂/A₁ = m; suy ra V₂²(1 − m²) = 2gh, hay",
      "Based on this equation of liquid flow, the volumetric flow per second Q "
      "through the section is given by Q = A₁V₁ = A₂V₂, or V₁ = A₂V₂/A₁. Putting "
      "this in equation 3.12 we have V₂² − V₁² = V₂² − V₂² × A₂²/A₁² = "
      "V₂²[1 − A₂²/A₁²] = 2gh. Now A₂/A₁ = m (say); hence V₂²(1 − m²) = 2gh, or")

    E(b, lang, "V₂ = √(2gh)/√(1 − m²)", "V₂ = √(2gh)/√(1 − m²)", num="3.13")

    P(b, lang,
      "Biểu thức 1/√(1 − m²) được gọi là hệ số vận tốc tiến đến và được ký hiệu là "
      "E, do đó phương trình 3.13 trở thành V₂ = E√(2gh), và vì thế,",
      "The expression 1/√(1 − m²) is known as velocity of approach factor and is "
      "designated as E, and so the equation 3.13 takes the form of V₂ = E√(2gh), "
      "and thus,")

    E(b, lang, "Q = A₂V₂ = A₂E√(2gh) ft³/sec",
      "Q = A₂V₂ = A₂E√(2gh) ft³/sec", num="3.14")

    E(b, lang, "Mass flow = w = ρQ = ρA₂E√(2gh) pounds/sec",
      "Mass flow = w = ρQ = ρA₂E√(2gh) pounds/sec", num="3.15")

    P(b, lang,
      "Khi suy luận biểu thức trên, ảnh hưởng của độ nhớt đã bị bỏ qua. Do đó lưu "
      "lượng tính toán sẽ có sai số. Do quán tính của chất lưu, sự co thắt của dòng "
      "vẫn tiếp tục ngay cả sau khi đi qua tấm chắn. Hiệu ứng này làm giảm ảo mặt "
      "cắt ngang phía hạ lưu tại áp suất P₂, nên cũng đưa sai số vào phép tính. Để "
      "hiệu chỉnh theo hai yếu tố này, một hằng số C (hệ số lưu lượng) được đưa vào "
      "công thức lưu lượng. Vì vậy,",
      "In deriving the above expression, the effect of viscosity was neglected. So "
      "the calculated flow shall have error. Due to inertia of the fluid contraction "
      "in the stream continues even after crossing the orifice. This effect creates "
      "virtual reduction in downstream cross-section at pressure P₂. This also "
      "introduces error in calculation. For effecting correction due to these two "
      "considerations a constant C (discharge coefficient) is introduced into the "
      "flow formula. Hence,")

    E(b, lang, "Q = CA₂E√(2gh)", "Q = CA₂E√(2gh)", num="3.16")

    P(b, lang, "và", "and")

    E(b, lang, "W = ρQ = ρCA₂E√(2gh)", "W = ρQ = ρCA₂E√(2gh)", num="3.17")

    P(b, lang,
      "Một xét đoạn quan trọng khác trong suy luận công thức lưu lượng là số "
      "Reynolds (Rd). Về mặt khái niệm, số Reynolds liên quan đến kiểu dòng chảy "
      "qua tấm chắn. Nếu hai tấm chắn cùng thiết kế khi lắp đặt đúng cách là tương "
      "đồng về hình học (kiểu dòng chảy giống nhau) thì chúng cũng tương đồng về "
      "động lực học và do đó có cùng số Reynolds. Về mặt toán học, số Reynolds được "
      "cho bởi:",
      "Another important consideration in derivation of flow formula is the Reynold "
      "number (Rd). Conceptually, the Reynold number is related to flow pattern of "
      "the orifice. If the two orifices of same design when installed properly are "
      "geometrically similar (flow pattern same), they are dynamically similar as "
      "well and hence have the same Reynold number. Mathematically, the Reynold "
      "number is given by:")

    E(b, lang, "Rd = dVρ/η", "Rd = dVρ/η", num="3.18")

    P(b, lang,
      "trong đó d là đường kính của chỗ thắt, V là vận tốc, ρ là khối lượng riêng "
      "và η là độ nhớt.",
      "where d is the diameter of the throat, V the velocity, ρ the density and η "
      "the viscosity.")

    P(b, lang,
      "Trong trường hợp chất lưu nén được, tức là khí, còn một hiệu chỉnh nữa cho "
      "sự giãn nể thể tích được áp dụng, ký hiệu là ε₀. Trong tính toán thông "
      "thường, ε₀ và hiệu chỉnh do số Reynolds được gộp lại như sau: ε₀ × hiệu "
      "chỉnh Rd = Z. Do đó, công thức lưu lượng cuối cùng trở thành,",
      "In case of compressible fluid, i.e. gases, yet another correction for "
      "volumetric expansion is applied which can be designated as ε₀. In normal "
      "calculation, ε₀ and correction due to Reynold number are taken together as "
      "follows: ε₀ × Rd correction = Z. Hence, the final flow formula becomes,")

    E(b, lang, "Q = CA₂ZE√(2gh)", "Q = CA₂ZE√(2gh)", num="3.19")

    P(b, lang,
      "áp dụng cho cả khí lẫn hơi quá nhiệt.",
      "for gas as well as superheated stream.")

    return b
