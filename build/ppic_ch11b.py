# -*- coding: utf-8 -*-
"""Book 9 (PPIC), Chapter 11, section 2.

DYNAMIC MODEL AND PROBLEM FORMULATION — source lines 7300-7397.
Bilingual prose is supplied as separate VI/EN literals; equations 1-16 are
language-neutral and are taken from ppic_ch11_eqa.EQ by key.
"""
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS
from ppic_ch11_eqa import EQ as EA


def section(lang):
    b = []

    H(b, lang,
      "MÔ HÌNH ĐỘNG VÀ XÁC LẬP BÀI TOÁN",
      "DYNAMIC MODEL AND PROBLEM FORMULATION", level=2)

    P(b, lang,
      "Trong mục này, mô hình không gian trạng thái phi tuyến dùng cho thiết kế "
      "điều khiển công suất được trình bày trước tiên. Sau đó, sau khi giới "
      "thiệu khái niệm ổn định nhờ đầu vào (ISS), bài toán lý thuyết cần giải "
      "quyết ở mục tiếp theo được đặt ra.",
      "In this section, the nonlinear state-space model for power-level design "
      "is firstly given. Then, after introducing the concept of input-to-stable "
      "stability (ISS), the theoretic problem to be solved in the next section "
      "is raised.")

    H(b, lang,
      "Mô hình không gian trạng thái phi tuyến để thiết kế điều khiển",
      "Nonlinear State-Space Model for Control Design", level=3)

    P(b, lang,
      "Từ Hình 1, MHTGR và OTSG trong một NSSM được bố trí cạnh nhau và được "
      "nối với nhau bằng một ống dẫn khí ngang đồng trục nóng/lạnh. Heli lạnh "
      "đi vào máy thổi khí được lắp đặt ở phần trên của OTSG và được tăng áp "
      "trước khi chảy vào ống dẫn khí lạnh. Heli lạnh đi vào các kênh bên trong "
      "gương phản xạ bên từ dưới lên trên để làm mát gương phản xạ, rồi đi qua "
      "giường viên nhiên liệu từ trên xuống dưới, nơi nó được đốt nóng đến "
      "nhiệt độ rất cao. Heli nóng rời buồng nóng bên trong gương phản xạ đáy, "
      "sau đó chảy vào phía sơ cấp của OTSG, nơi nó được làm nguội thành heli "
      "lạnh bằng cách truyền nhiệt sang dòng nước/hơi nước phía thứ cấp.",
      "From Figure 1, the MHTGR and the OTSG in one NSSM are arranged side by "
      "side, and are connected with each other by a horizontal coaxial hot/cold "
      "gas duct. Cold helium enters the blower that is mounted on the upper "
      "part of the OTSG, and is pressurized before flowing into the cold gas "
      "duct. The cold helium enters the channels inside the side-reflector from "
      "bottom to top for cooling the reflector, and then passes through the "
      "pebble-bed from top to bottom where it is heated to a very high "
      "temperature. The hot helium leaves the hot chamber inside the bottom "
      "reflector, and then flows into the OTSG primary side where it is cooled "
      "to be the cold helium by transferring its heat to the secondary "
      "water/steam flow.")

    P(b, lang,
      "Bằng cách áp dụng động học điểm với một nhóm neutron trễ tương đương, "
      "xét đến hiệu ứng phản hồi nhiệt độ của lõi lò phản ứng gồm cả giường "
      "viên nhiên liệu và gương phản xạ, và dựa trên định luật bảo toàn năng "
      "lượng nhiệt, mô hình động dùng cho thiết kế điều khiển có thể được viết "
      "như [15,18]:",
      "By adopting point kinetics with one equivalent delayed neutron group, "
      "by considering the temperature feedback effect of the reactor core "
      "composed of both the pebble-bed and reflector, and based upon the "
      "conservation law of thermal energy, the dynamic model for control design "
      "can be written as [15,18]:")
    E(b, lang, EA[1], EA[1], num="1")

    P(b, lang, "trong đó:", "where:")

    E(b, lang, EA[2], EA[2], num="2")

    P(b, lang,
      "n<sub>r</sub> là công suất neutron tương đối; c<sub>r</sub> là nồng độ "
      "tương đối của tiền chất neutron trễ; β là phần suất của neutron trễ; "
      "Λ là thời gian sống hiệu dụng của neutron tức thì; ρ<sub>r</sub> là độ "
      "phản ứng do các thanh điều khiển tạo ra; λ là hằng số phân rã phóng xạ "
      "hiệu dụng của tiền chất neutron trễ; T<sub>R</sub> và α<sub>R</sub> lần "
      "lượt là nhiệt độ và hệ số phản hồi độ phản ứng của lõi lò phản ứng được "
      "cấu thành bởi cả các phần tử nhiên liệu và gương phản xạ; "
      "T<sub>R,m</sub> là giá trị cân bằng ban đầu của T<sub>R</sub>; P<sub>0</sub> "
      "là công suất nhiệt định mức; T<sub>H</sub> là nhiệt độ trung bình của "
      "heli trong vòng sơ cấp, T<sub>S</sub> là nhiệt độ trung bình của chất làm "
      "mát ở phía thứ cấp của OTSG; Ω<sub>P</sub> là hệ số truyền nhiệt giữa "
      "heli và lõi lò phản ứng; Ω<sub>S</sub> là hệ số truyền nhiệt giữa hai "
      "phía của OTSG; μ<sub>R</sub> và μ<sub>H</sub> lần lượt là tổng nhiệt dung "
      "của lõi lò phản ứng và của dòng heli bên trong vòng sơ cấp; M<sub>S</sub> "
      "là lưu lượng khối nhân với nhiệt dung của dòng nước/hơi nước thứ cấp; "
      "hằng số G<sub>r</sub> là giá trị vi phân của thanh điều khiển; "
      "h<sub>r</sub> là vị trí tổng của thanh điều khiển; v<sub>r</sub> là tín "
      "hiệu tốc độ thanh điều khiển được thiết kế. Ở đây, cần lưu ý rằng "
      "α<sub>R</sub> được bảo đảm là âm nhờ thiết kế vật lý của MHTGR.",
      "n<sub>r</sub> is the relative neutron power; c<sub>r</sub> is the "
      "relative concentration of the delayed neutron precursor; β is the "
      "fraction of the delayed neutrons; Λ is the effective prompt neutron "
      "life time; ρ<sub>r</sub> is the reactivity provided by the control rods; "
      "λ is the effective radioactive decay constant of the delayed neutron "
      "precursor; T<sub>R</sub> and α<sub>R</sub> are respectively the "
      "temperature and reactivity feedback coefficient of the reactor core "
      "constituted by both the fuel elements and the reflector; "
      "T<sub>R,m</sub> is the initial equilibrium value of T<sub>R</sub>; "
      "P<sub>0</sub> is the rated thermal power; T<sub>H</sub> is the average "
      "helium temperature of the primary loop, T<sub>S</sub> is the average "
      "coolant temperature of the OTSG secondary side; Ω<sub>P</sub> is the "
      "heat transfer coefficient between the helium and the reactor core; "
      "Ω<sub>S</sub> is the heat transfer coefficient between the two sides of "
      "the OTSG; μ<sub>R</sub> and μ<sub>H</sub> is respectively the total heat "
      "capacities of the reactor core and helium flow inside the primary loop; "
      "M<sub>S</sub> is the mass flowrate times the heat capacity of the "
      "secondary water/steam flow; constant G<sub>r</sub> is the differential "
      "worth of the control rod; h<sub>r</sub> is total control rod position; "
      "v<sub>r</sub> is the designed control rod speed signal. Here, it is "
      "worthy to be noted that α<sub>R</sub> is guaranteed to be negative by "
      "the physical design of the MHTGR.")

    P(b, lang,
      "Độ lệch của n<sub>r</sub>, c<sub>r</sub>, T<sub>R</sub>, T<sub>H</sub>, "
      "T<sub>S</sub> và h<sub>r</sub> so với các giá trị cân bằng tương ứng, "
      "tức là n<sub>r0</sub>, c<sub>r0</sub>, T<sub>R0</sub>, T<sub>H0</sub>, "
      "T<sub>S0</sub> và h<sub>r0</sub>, được định nghĩa như sau:",
      "Define deviations of n<sub>r</sub>, c<sub>r</sub>, T<sub>R</sub>, "
      "T<sub>H</sub>, T<sub>S</sub>, and h<sub>r</sub> from their equilibrium "
      "values, i.e., n<sub>r0</sub>, c<sub>r0</sub>, T<sub>R0</sub>, "
      "T<sub>H0</sub>, T<sub>S0</sub> and h<sub>r0</sub> as:")
    E(b, lang, EA[3], EA[3], num="3")

    P(b, lang,
      "Vì δT<sub>S</sub> có thể được triệt tiêu tốt bằng bộ điều khiển nhiệt độ "
      "hơi nước phía thứ cấp, người ta giả định rằng:",
      "Since δT<sub>S</sub> can be well eliminated by the secondary steam "
      "temperature controller, it is assumed that:")
    E(b, lang, EA[4], EA[4], num="4")

    P(b, lang, "Sau đó, định nghĩa:", "Then, define:")
    E(b, lang, EA[5], EA[5], num="5")
    E(b, lang, EA[6], EA[6], num="6")
    E(b, lang, EA[7], EA[7], num="7")

    P(b, lang, "và:", "and:")
    E(b, lang, EA[8], EA[8], num="8")

    P(b, lang,
      "trong đó x là vectơ trạng thái của NSSM; [x<sup>T</sup> ξ]<sup>T</sup> "
      "cấu thành vectơ trạng thái của toàn hệ thống; u là đầu vào điều khiển, "
      "y là đầu ra đo được của hệ thống.",
      "where x is the state-vector of the NSSM; [x<sup>T</sup> ξ]<sup>T</sup> "
      "constitutes the state-vector of the whole system; u is the control "
      "input, y is the measured system output.")

    P(b, lang,
      "Dựa trên giả định và định nghĩa nêu trên, mô hình không gian trạng thái "
      "phi tuyến dùng cho thiết kế điều khiển có thể được viết như sau:",
      "Based on the above assumption and definition, the nonlinear state-space "
      "model for control design can be written as:")
    E(b, lang, EA[9], EA[9], num="9")

    P(b, lang, "trong đó:", "where:")
    E(b, lang, EA[10], EA[10], num="10")
    E(b, lang, EA[11], EA[11], num="11")

    P(b, lang, "và:", "and:")
    E(b, lang, EA[12], EA[12], num="12")

    H(b, lang,
      "Xác lập bài toán lý thuyết",
      "Theoretic Problem Formulation", level=3)

    P(b, lang,
      "Trước khi đặt bài toán lý thuyết, định nghĩa về ổn định nhờ đầu vào "
      "(ISS) được giới thiệu.",
      "Before giving the theoretic problem, the definition of input-to-state "
      "stability (ISS) is introduced.")

    P(b, lang,
      "<b>Định nghĩa 1 [19].</b> Xét một hệ phi tuyến",
      "<b>Definition 1 [19].</b> Consider a nonlinear system")
    E(b, lang, EA[13], EA[13], num="13")

    P(b, lang,
      "trong đó z ∈ R<sup>n</sup> và v ∈ R<sup>m</sup> lần lượt là trạng thái và "
      "nhiễu, còn F là hàm Lipschitz địa phương theo z và v. Hệ (13) được gọi "
      "là ổn định nhờ đầu vào khi và chỉ khi tồn tại một hàm U trơn, xác định "
      "dương và không bị chặn xuyên tâm, cùng các hàm σ và ω thuộc lớp "
      "K<sub>∞</sub>, sao cho:",
      "where z ∈ R<sup>n</sup> and v ∈ R<sup>m</sup> are the state and "
      "disturbance respectively, and F is locally Lipschiz in z and v. System "
      "(13) is said to be input-to-state stable if and only if there is a "
      "smooth positive definite radially unbounded function U and class "
      "K<sub>∞</sub> function σ and ω so that:")
    E(b, lang, EA[14], EA[14], num="14")

    P(b, lang,
      "Ở đây, một hàm φ được gọi là thuộc lớp K<sub>∞</sub> nếu nó tăng "
      "nghiêm ngặt, φ(0) = 0 và φ(r)→∞ khi r→∞.",
      "Here, a function φ is said to be class K<sub>∞</sub> if it is strictly "
      "increasing, φ(0) = 0, and φ(r)→∞ when r→∞.")

    P(b, lang,
      "<b>Nhận xét 1.</b> Từ phương trình (14), rõ ràng là:",
      "<b>Remark 1.</b> From Equation (14), it is clear that:")

    P(b, lang,
      "nếu ‖z‖ ≥ σ<sup>−1</sup>ω(‖v‖), từ đó ta thấy Định nghĩa 1 mô tả tính "
      "bền vững của hệ (13) đối với nhiễu v.",
      "if ‖z‖ ≥ σ<sup>−1</sup>ω(‖v‖), from which we can see that Definition 1 "
      "describes the robustness of system (13) relative to disturbance v.")

    P(b, lang,
      "Động lực của việc đưa vào định nghĩa ISS là để xử lý tác động bất lợi do "
      "bão hòa đầu vào điều khiển gây ra. Để bù trừ bão hòa đầu vào điều khiển "
      "và sự bất định tham số, bài toán lý thuyết cần giải quyết được tóm tắt "
      "như sau.",
      "The motivation of introduce the definition of ISS is to deal with the "
      "negative effect caused by control input saturation. For compensating "
      "the control input saturation and parameter uncertainty, the theoretical "
      "problem to be solved is summarized as follows.")

    P(b, lang,
      "<b>Bài toán 1.</b> Làm thế nào để thiết kế một bộ điều khiển phản hồi "
      "đầu ra thích ứng bão hòa:",
      "<b>Problem 1.</b> How to design a saturated adaptive output feedback "
      "control:")
    E(b, lang, EA[15], EA[15], num="15")

    P(b, lang,
      "cho hệ (9) sao cho hệ vòng lặp kín tương ứng ổn định nhờ đầu vào, và:",
      "of system (9) so that the corresponding closed-loop system is "
      "input-to-state stable, and:")
    E(b, lang, EA[16], EA[16], num="16")

    P(b, lang,
      "trong đó u<sub>min</sub> là một hằng số âm, còn u<sub>max</sub> là một "
      "hằng số dương.",
      "where u<sub>min</sub> is a negative constant, and u<sub>max</sub> is a "
      "positive constant.")

    return b
