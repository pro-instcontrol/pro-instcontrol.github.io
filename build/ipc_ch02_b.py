# -*- coding: utf-8 -*-
"""Chapter 2, section 2.2-2.2.2 (first half), EN/VI bilingual.

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 82-98, printed pp. 70-86, decoded lines
2924-3518.  Covers 2.2 "Transducers and Measurement of Pressure", 2.2.1
"Introduction", the pressure-unit look-up Table 2.1, and the first half of
2.2.2 "Classification of Pressure Measurement System" through Figure 2.21.
Figures 2.6-2.21 are redrawn by `ipcfig2`; equations are rendered with
standard mathematical notation because the PDF text layer scatters glyphs.
"""

import ipcfig2 as F
from ipc_ch02_lib import H, P, L, E, FIG, TBL, NOTE


# Table 2.1 transcribed from printed p. 71 (PDF p. 83).  Row labels are unit
# symbols and the numeric body is language-neutral; only headers/captions are
# localized.  Exponents and the two anomalous cells (x 10^-2, x 10^-3) follow
# the printed table exactly.
_TBL21 = [
    ["Kp/cm² / Kgf/cm² at", "1", "10⁴", "98066.5", "0.9807", "0.96784", "14.2233"],
    ["Kp/m²", "10⁻⁴", "1", "9.80665", "0.9807 × 10⁻⁴", "0.96784 × 10⁻⁴", "0.1422 × 10⁻²"],
    ["N/m²", "1.0197 × 10⁻⁵", "0.101972 × 10⁻⁵", "1", "10⁻⁵", "0.987 × 10⁻⁵", "0.145 × 10⁻³"],
    ["Bar", "1.01972", "10197.2", "10⁵", "1", "0.98692", "14.5038"],
    ["atm", "1.03323", "10332", "1.0133 × 10⁵", "1.01325", "1", "14.696"],
    ["PSIG", "0.07031", "70307", "6894.76", "0.06895", "0.6805", "1"],
]

_HEAD21_VI = ["Đơn vị", "Kp/cm² · Kgf/cm² at", "Kp/m²", "N/m²", "Bar", "Atm.", "PSIg."]
_HEAD21_EN = ["Unit", "Kp/cm² · Kgf/cm² at", "Kp/m²", "N/m²", "Bar", "Atm.", "PSIg."]


def section(lang):
    b = []

    # ------------------------------------------------------------------ 2.2
    H(b, lang, "2.2 Bộ chuyển đổi và phép đo áp suất",
      "2.2 Transducers and Measurement of Pressure", level=2)
    H(b, lang, "2.2.1 Mở đầu", "2.2.1 Introduction", level=3)

    P(b, lang,
      "Trái Đất được bao quanh bởi một đại dương không khí gọi là khí quyển. Chính trọng lượng "
      "của không khí này tạo ra áp suất khí quyển trên trái đất và tác động lên toàn bộ bề mặt "
      "trái đất. Vì trái đất phần lớn chứa đầy nước, nước được cung cấp cho chúng ta dưới áp "
      "suất. Tương tự, tính lưu động của mọi chất lỏng đều là nhờ áp suất, do đó áp suất là một "
      "điều kiện thiết yếu và phổ quát của mọi quá trình.",
      "Planet Earth is surrounded by atmospheric ocean called air. This air due to its weight "
      "creates atmospheric pressure on the earth and acts on the entire earth. Since the earth "
      "is mostly filled with water, the water is supplied to us under pressure. Similarly, "
      "fluidity of all kinds are due to pressure and therefore, pressure is an essential "
      "universal processing condition.")

    P(b, lang,
      "Khái niệm biến áp suất có thể được hiểu như tác động của một lực chống lại một lực khác "
      "có xu hướng đối kháng. Nó có bản chất của một sức đẩy được phân bổ đều trên một bề mặt "
      "hoặc bên trong một bình chứa kín. Người ta đo nó bằng lực trên một đơn vị diện tích. Các "
      "đơn vị áp suất khác nhau được chỉ ra trên bảng tra cứu chuyển đổi đơn vị Bảng 2.1.",
      "Concept of pressure variable may be conceived as the action of a force against another "
      "one having opposing activity. It has the nature of a thrust distributed equally over a "
      "surface or within a closed container. It can be measured as force per unit area. "
      "Different units of pressure have been indicated on unit transfer look-up Table 2.1.")

    P(b, lang,
      "Để đo áp suất người ta có thể lấy hai điểm quy chiếu. Một là số không tuyệt đối, chỉ tồn "
      "tại trong chân không hoàn hảo. Áp suất đo từ điểm quy chiếu này gọi là áp suất tuyệt đối. "
      "Điểm quy chiếu kia chính là khí quyển. Tuy nhiên, khó khăn với điểm quy chiếu khí quyển "
      "là nó thay đổi theo độ cao so với mực nước biển và cũng theo sự thay đổi điều kiện thời "
      "tiết của trái đất, tức là điều kiện khí áp. Áp suất tại hoặc gần mực nước biển được lấy "
      "là 14.7 psia (pound trên inch vuông) hoặc 760 mm cột thủy ngân tuyệt đối.",
      "For the measurement of pressure two reference points can be taken. One is absolute zero, "
      "which will exist only in a perfect vacuum. Pressures measured from this reference point "
      "are called absolute pressure. The other reference point can be the atmosphere itself. "
      "The difficulty with atmospheric reference point, however, is that it varies according to "
      "altitude with respect to sea level and also according to changes in weather conditions of "
      "the earth, i.e. barometric conditions. Pressure at or near sea level is taken as 14.7 "
      "psia (pounds per square inch) or 760 mm. of mercury column absolute.")

    TBL(b, lang, _HEAD21_VI, _HEAD21_EN, _TBL21,
        caption_vi="Bảng 2.1 — Bảng tra cứu chuyển đổi đơn vị áp suất.",
        caption_en="Table 2.1 — Unit Transfer Look-up Table.")

    NOTE(b, lang,
         "<b>Chú giải.</b> Kp/cm² = kg-weight/cm² · Kgf/cm² = kg-force/cm² · at = atmô kỹ thuật · "
         "atm = atmô vật lý · N/m² = Newton/m² · Bar = kg/cm².",
         "<b>Legend.</b> Kp/cm² = kg-weight/cm² · Kgf/cm² = kg-force/cm² · at = Technical "
         "atmosphere · atm = Physical atmosphere · N/m² = Newton/m² · Bar = kg/cm².")

    P(b, lang,
      "Khi dùng áp suất khí quyển làm quy chiếu, áp suất cao hơn áp suất khí quyển được gọi là "
      "áp suất đo (psig) hay áp suất dương (+ve). Áp suất thấp hơn khí quyển được gọi là chân "
      "không hay áp suất âm (ve). Chân không nên được hiểu là đi xuống từ áp suất khí quyển.",
      "When we use atmospheric pressure as the reference, the pressure above that of the "
      "atmosphere is referred as gage pressure (psig) or positive (+ve) pressure. Pressures below "
      "atmosphere are referred as vacuum or negative (ve) pressure. A vacuum should be "
      "understood as going down from atmospheric pressure.")

    P(b, lang,
      "Áp suất đo là thước đo ứng suất bên trong bình chứa và xu hướng rò rỉ của chất lỏng. Thực "
      "chất nó là một trường hợp riêng của áp suất chênh lệch. Ưu điểm của phép đo áp suất tuyệt "
      "đối thay vì áp suất đo là nó loại bỏ các sai số do biến động khí áp.",
      "The gage pressure is a measure of stress within a vessel and the tendency of the fluids "
      "to leak out. It is really a special case of differential pressure. The advantage of "
      "making absolute pressure measurement rather than gage pressure is that it eliminates "
      "errors introduced by barometric variations.")

    # --------------------------------------------------------------- 2.2.2
    H(b, lang, "2.2.2 Phân loại hệ thống đo áp suất",
      "2.2.2 Classification of Pressure Measurement System", level=3)

    P(b, lang, "Nhìn chung, hệ thống đo áp suất được phân thành ba loại:",
      "Broadly, the pressure measurement system can be classified into three categories:")
    L(b, lang,
      ["(i) Manomet,", "(ii) Thiết bị đo áp suất trực tiếp và", "(iii) Thiết bị đo áp suất gián tiếp."],
      ["(i) Manometers,", "(ii) Direct pressure-measurement devices and",
       "(iii) Indirect pressure-measurement devices."])

    # ------------------------------------------------------- (i) Manometers
    H(b, lang, "(i) Manomet", "(i) Manometers", level=4)
    P(b, lang,
      "Manomet được xem là các thiết bị đo áp suất cơ bản và vì vậy được dùng làm dụng cụ chuẩn. "
      "Chúng cũng có thể được gọi là thiết bị đo áp suất cân bằng trọng lực vì đo áp suất bằng "
      "cách cân bằng với trọng lực của cột chất lỏng. Chất lỏng dùng trong manomet (gọi là chất "
      "lỏng manomet) thường là nước hoặc thủy ngân, hoặc bất kỳ chất lỏng nào có mật độ nằm giữa "
      "hai chất đó. Yêu cầu chính của chất lỏng là không độc, không ăn mòn, ổn định, không dễ "
      "đông cứng và không trộn lẫn với chất lỏng cần đo áp suất. Manomet là cảm biến ướt, khác "
      "với các phần tử đo khác. Mọi manomet đều đo áp suất quy chiếu theo khí quyển, do đó áp "
      "suất chỉ thị của chúng là áp suất đo.",
      "Manometers are supposed to be the basic pressure measurement devices and therefore, these "
      "are used as standard instrument. These can be called gravity-balance pressure measurement "
      "devices as well since they measure the pressures by balancing against the gravitational "
      "force of liquid heads. The liquid to be used in the manometer (called manometer liquid) "
      "can be water or mercury in general or can be any other liquid having density in between. "
      "The main requirements for the liquids are that they should be non-toxic, non-corrosive, "
      "stable, should not freeze easily and should not mix with the fluid of which the pressure "
      "is to be measured. Manometers are wet sensors in contrast to other measuring elements. "
      "All manometers measure pressure with reference to atmosphere and therefore, these "
      "indicated pressures are gage pressure.")

    P(b, lang, "Có ba loại manomet chính:", "There are mainly three types of manometers:")
    L(b, lang,
      ["(i) Manomet chữ U,", "(ii) Manomet kiểu bể và", "(iii) Manomet nghiêng."],
      ["(i) U-tube manometers,", "(ii) Well type manometers, and", "(iii) Inclined manometers."])

    # -------------------------------------------------- (i) U-tube manometer
    H(b, lang, "(i) Manomet chữ U", "(i) U-tube manometer", level=4)
    P(b, lang,
      "Manomet chữ U là loại đơn giản và đa dụng nhất. Trong manomet này, chất lỏng được đổ vào "
      "ống (bằng thủy tinh) và khi cả hai nhánh đều hở ra khí quyển, chỉ có áp suất khí quyển "
      "tác động. Vì áp suất khí quyển tác động trên hai nhánh là bằng nhau, chất lỏng manomet sẽ "
      "có chiều cao bằng nhau ở cả hai nhánh. Khi một áp suất nhỏ được đặt vào một nhánh và nhánh "
      "kia vẫn hở ra khí quyển, mức chất lỏng ở nhánh hở sẽ dâng lên. Độ dâng của chiều cao hiệu "
      "dụng cho biết độ lớn của áp suất đặt vào. Quan hệ toán học tính áp suất P theo chiều cao "
      "cột chất lỏng h trong nhánh như sau:",
      "U-tube manometer is the simplest and the most versatile manometer. In this manometer, "
      "liquid is put inside the tube (made of glass) and when both the legs are open to "
      "atmosphere, only atmospheric pressure works on them. Since the atmospheric pressure "
      "working on both the legs are equal, the manometer liquid shall be showing equal height on "
      "both the legs. Now when a small pressure is applied on one of the legs and the other one "
      "is left open to atmosphere, there will be a rise in the liquid level in the leg which is "
      "open to the atmosphere. The rise in effective height is indicative of the amount of "
      "pressure applied. The mathematical relation which calculates the pressure P in terms of "
      "height h of the liquid column inside the leg is as follows:")

    FIG(b, 6, F.fig_f06(), lang)
    E(b, lang, "P = ρh", "P = ρh", num="2.1")
    P(b, lang, "trong đó ρ là mật độ của chất lỏng manomet.",
      "where ρ is the density of the manometer liquid.")

    P(b, lang,
      "Hình 2.6 cho thấy manomet chữ U dùng chất lỏng manomet có mật độ ρ. Áp suất P1 được đặt "
      "vào nhánh trái, nhánh phải hở ra khí quyển (gọi áp suất này là P2). Cần lưu ý rằng trước "
      "khi đặt áp suất P1, chiều cao chất lỏng manomet ở hai nhánh là như nhau. Sự chênh lệch "
      "chiều cao h chỉ phát sinh do áp suất P1. Như vậy, áp suất ròng trên manomet là (P1 − P2), "
      "được cho bởi:",
      "Figure 2.6 shows a U-tube manometer in which manometer liquid of density ρ has been used "
      "for measurement. The pressure P1 has been applied on the left leg and the right leg is "
      "open to atmosphere (let this pressure be P2). It should be noted here that before "
      "application of pressure P1 the manometer-liquid-height was same on both the legs. The "
      "difference in the manometer-liquid-height h has come due to application of pressure P1 "
      "only. Thus, the net pressure on the manometer shall be (P1 - P2), which will be given by:")

    E(b, lang, "(P1 − P2) = ρh", "(P1 - P2) = ρh", num="2.2")

    P(b, lang, "<b>Ưu điểm</b>", "<b>Advantages</b>")
    L(b, lang,
      ["(i) Cấu trúc đơn giản,", "(ii) Độ chính xác cao,", "(iii) Khả năng lặp lại tốt,",
       "(iv) Có nhiều loại chất lỏng manomet để lựa chọn,", "(v) Dùng làm dụng cụ chuẩn sơ cấp."],
      ["(i) Simple construction,", "(ii) High accuracy,", "(iii) Good repeatability,",
       "(iv) Wide range of manometer liquids are available,",
       "(v) Used as primary standard instrument."])

    P(b, lang, "<b>Nhược điểm</b>", "<b>Disadvantages</b>")
    L(b, lang,
      ["(i) Thiếu tính cơ động,", "(ii) Cần căn chỉnh mức,",
       "(iii) Trở nên nguy hiểm khi dùng thủy ngân làm chất lỏng manomet,",
       "(iv) Tiếp xúc với khí quyển,",
       "(v) Nếu đường kính ống chữ U dùng nhỏ, sẽ xuất hiện sai số đọc do meniscus."],
      ["(i) Lack of portability,", "(ii) Need of levelling,",
       "(iii) Becomes hazardous when mercury is used as manometer liquid,",
       "(iv) Exposed to atmosphere,",
       "(v) If diameter of the U-tube used is small, then the reading error shall be observed "
       "due to meniscus."])

    P(b, lang,
      "Phạm vi ứng dụng là từ 0 đến 150 inch (3750 mm) khi chất lỏng manomet là nước và đến áp "
      "suất làm việc 400 psig. Có thể mở rộng phạm vi ứng dụng bằng cách dùng thủy ngân làm chất "
      "lỏng manomet.",
      "Range of application is from 0 to 150 inches (3750 mm.) when the manometer liquid used is "
      "water and upto 400 psig operating pressure. The range of application can be increased by "
      "use of mercury as manometer liquid.")

    # --------------------------------------------- (ii) Well-type manometer
    H(b, lang, "(ii) Manomet kiểu bể", "(ii) Well-type manometer", level=4)
    P(b, lang,
      "Manomet kiểu bể được cho thấy trên Hình 2.7. Nguyên lý cơ bản của manomet kiểu bể cũng "
      "giống manomet chữ U, nhưng cấu trúc hoàn toàn khác. Để tiện đọc, đôi khi người ta gắn "
      "thước đo trực tiếp đã chia theo chiều cao hoặc áp suất (P1 − P2) ở nhánh phải. Áp suất "
      "được đặt vào phía bể. Mọi phân tích áp dụng cho manomet chữ U cũng áp dụng cho manomet "
      "kiểu bể.",
      "The well-type manometer has been shown in Figure 2.7. Basic principle of the well-type "
      "manometer is same as U-type manometer, but the construction is completely different. A "
      "direct measurement scale graduated in terms of height or pressure (P1 - P2) is sometimes "
      "fixed on the right leg for ease of taking reading. The pressure is applied on well side. "
      "All other discussions applicable to U-tube manometer are applied with well-type manometer "
      "as well.")

    FIG(b, 7, F.fig_f07(), lang)

    # -------------------------------------------- (iii) Inclined manometer
    H(b, lang, "(iii) Manomet nghiêng", "(iii) Inclined manometer", level=4)
    P(b, lang,
      "Manomet nghiêng được cho thấy trên Hình 2.8. Trong loại này, nhánh hở ra khí quyển để so "
      "sánh không thẳng đứng mà nghiêng một góc θ so với trục ngang. Độ dịch chuyển thẳng đứng "
      "h của chất lỏng do áp suất chênh lệch hiệu dụng (P1 − P2) được cho bởi:",
      "The inclined manometer has been shown on Figure 2.8. In this manometer the leg which is "
      "open to atmosphere for comparison in not vertical, but inclined at an angle θ with "
      "respect to horizontal axis. The vertical displacement h of the fluid due to effective "
      "differential pressure (P1 - P2) is given by:")

    FIG(b, 8, F.fig_f08(), lang)
    E(b, lang, "h = hx sinθ", "h = hx sinθ", num="2.3")
    P(b, lang,
      "trong đó hx là quãng đường chất lỏng đi lên trong ống. Nhờ manomet nghiêng mà phép đo áp "
      "suất thấp được thực hiện chính xác và dễ dàng hơn.",
      "where hx is the distance travelled by the fluid up the tube. By the help of inclined "
      "manometer, measurement of low pressures can be accomplished more accurately and easily.")

    P(b, lang,
      "Phép đo áp suất bằng manomet luôn quy chiếu theo áp suất khí quyển. Nếu nhánh áp suất "
      "(P2) được rút chân không, ta cũng có thể đo áp suất tuyệt đối. Baromet là một dạng "
      "manomet đặc biệt với một nhánh chân không và nhánh kia chịu áp suất khí quyển.",
      "Measurement of pressure with manometer is always referenced to atmospheric pressure. If "
      "the pressure leg (P2) is evacuated, then it is possible to measure absolute pressure as "
      "well. A barometer is special type of manometer with a vacuum in one leg and atmospheric "
      "pressure on the other leg.")

    # --------------------------------- (ii) Direct pressure-measurement devices
    H(b, lang, "(ii) Thiết bị đo áp suất trực tiếp",
      "(ii) Direct pressure-measurement devices", level=4)
    P(b, lang,
      "Trong nhóm này, có thể đo áp suất đo từ 0 milimet cột nước (0 mm WC) đến 1300 kg/cm2 "
      "(giá trị thực tế) bằng các áp kế lắp trực tiếp. Dải đo được chia thành ba nhóm con:",
      "Under this category, measurement of gage pressure ranging from zero millimetre of water "
      "column (0 mm WC) to 1300 kg/cm2 (practical figure) is possible by employing direct "
      "mounted pressure gages. The range of measurement can be divided into three subcategories:")
    L(b, lang,
      ["(a) Áp kế,", "(b) Áp kế thu và", "(c) Áp kế milimet."],
      ["(a) Pressure gage,", "(b) Receiver gage, and", "(c) Millimetre gage."])

    P(b, lang,
      "Ở nhóm con (a), nhiều dải áp kế khác nhau được thiết kế và chế tạo như sau:",
      "Under subcategory (a), different ranges of pressure gages are designed and fabricated "
      "which are as follows:")
    L(b, lang,
      ["0 đến 2.5 kg/cm2; 0 đến 6 kg/cm2; 0 đến 10 kg/cm2; 0 đến 16 kg/cm2; 0 đến 25 kg/cm2; "
       "0 đến 60 kg/cm2;",
       "0 đến 160 kg/cm2; 0 đến 250 kg/cm2; 0 đến 400 kg/cm2; và các dải cao hơn đến 1300 kg/cm2."],
      ["0 to 2.5 kg/cm2; 0 to 6 kg/cm2; 0 to 10 kg/cm2; 0 to 16 kg/cm2; 0 to 25 kg/cm2; "
       "0 to 60 kg/cm2;",
       "0 to 160 kg/cm2; 0 to 250 kg/cm2; 0 to 400 kg/cm2; and higher ranges upto 1300 kg/cm2."])

    P(b, lang,
      "Ở nhóm con (b), chỉ một dải duy nhất được thiết kế là 0.2 đến 1.0 kg/cm2. Dải này dùng "
      "để đo cả tín hiệu đầu ra của bộ phát và của bộ điều khiển dạng khí nén.",
      "Under subcategory (b), only one range is designed and that is 0.2 to 1.0 kg/cm2. This is "
      "used for measurement of transmitter as well as controller output signals in pneumatic "
      "form.")

    P(b, lang,
      "Ở nhóm con (c), các áp kế dải rất thấp được thiết kế và chế tạo. Chúng được dùng làm áp "
      "kế hiệu chuẩn và cũng dùng để đo áp suất dương (draft) trong hệ thống lò hơi phát hơi.",
      "Under subcategory (c), very low range gages are designed and fabricated. These gages are "
      "used as calibration gages and also used for measurement of positive draft in steam "
      "generating boiler system.")

    P(b, lang,
      "Nhìn chung, áp kế thu cũng như áp kế có dải đến 400 kg/cm2 thường được chế tạo từ phần tử "
      "ống Bourdon dạng C. Áp kế thu cũng được chế tạo từ phần tử ống sóng. Hình 2.9 cùng Hình "
      "2.10 cho thấy dạng nhìn ngoài và bên trong của các áp kế dùng phần tử Bourdon dạng C.",
      "Generally, receiver gages as well as pressure gages of upto 400 kg/cm2 ranges are "
      "generally made of C-type bourdon tube element. Receiver gages are made of bellows element "
      "also. The Figure 2.9 along with Figure 2.10 shows external and internal view of such "
      "pressure gages where a C-type bourdon element has been used.")

    FIG(b, 9, F.fig_f09(), lang)

    P(b, lang,
      "Áp suất của quá trình được đưa vào đầu hở của ống Bourdon. Hệ thống hoạt động theo nguyên "
      "lý cân bằng chuyển động. Ảnh hưởng của cân bằng chuyển động khi có áp suất được thấy ở đầu "
      "kín, tức đầu tự do của ống Bourdon, dưới dạng dịch chuyển góc. Sự dịch chuyển góc này là "
      "kết quả của việc ống Bourdon mở ra khi có áp suất quá trình. Chuyển động góc này chỉ cỡ "
      "vài độ được truyền tới cụm cung–bánh răng nhỏ, nơi nó được khuếch đại. Kim chỉ thị được "
      "gắn trên bánh răng nhỏ. Kim chuyển động ngược lại với lực cản của lò xo tóc. Liên kết "
      "chỉnh được, cung và bánh răng nhỏ đều làm bằng đồng thau hoặc đồng phosphor.",
      "The process pressure is applied at the open end of the bourdon tube. The system works on "
      "motion balance principle. The effect of motion balance on application of pressure is seen "
      "at the closed end, i.e. free end of the bourdon tube in terms of angular displacement. The "
      "angular displacement is the result of uncoiling of bourdon tube due to application of "
      "process pressure. This angular movement, which is of the order of a few degrees only is "
      "transferred to the sector-pinion combination where it gets amplified. The pointer for "
      "indication is fixed on the pinion. The pointer moves against the controlling force of "
      "hairspring. The adjustable link, the sector and the pinion are all made of either brass "
      "or phosphor bronze.")

    FIG(b, 10, F.fig_f10(), lang)

    P(b, lang,
      "Vỏ của loại áp kế này làm bằng gang đúc, đồng thau ép và thép. Đôi khi cũng dùng vỏ nhựa "
      "phenolic vì loại này bền, chống ăn mòn, nhẹ và lại rẻ.",
      "The casings of this type of pressure gage are made of cast iron, pressed brass and steel. "
      "Phenolic plastic casing is also sometimes used since this is strong, corrosion resistant, "
      "light in weight and also inexpensive.")

    H(b, lang, "Ứng dụng của áp kế/áp kế thu", "Application of Pressure/Receiver Gages", level=4)
    P(b, lang,
      "Ứng dụng của áp kế/áp kế thu chỉ giới hạn trong đo tại hiện trường. Do sự phát triển của "
      "bảng điều khiển tập trung hiện nay, mọi thiết bị chỉ thị, ghi và điều khiển từ xa đều đặt "
      "trong phòng điều khiển. Nhưng áp kế/áp kế thu lắp đặt bên ngoài phòng điều khiển vẫn được "
      "người vận hành quan tâm và chú ý cho đến ngày nay.",
      "Application of pressure/receiver gage is restricted to field measurement only. Due to the "
      "development of centralized control panel nowadays all remote indicating, recording and "
      "controlling instruments are located inside the control room. But pressure/receiver gages "
      "installed outside the control rooms enjoy the importance and attention of the operating "
      "personnels even today.")

    P(b, lang,
      "Trong ứng dụng thông thường, áp kế được lắp như thường lệ nhờ kết nối NPT ¼ inch hoặc ½ "
      "inch (Nominal Pipe Thread). Trong ứng dụng mà áp kế chịu rung cơ khí, các cung làm bằng "
      "bakelite chịu rung tốt hơn loại chuẩn làm bằng đồng thau hoặc đồng phosphor. Trong ứng "
      "dụng đo áp suất của chất lỏng do bơm bánh răng tốc độ cao và bơm định lượng áp suất cao "
      "đẩy, biên độ rung có thể nhỏ nhưng tần số rất cao. Rung tần số cao phá hủy cơ cấu cơ khí "
      "của áp kế và vì vậy phải được giảm chấn. Cần chú ý ngay trong khâu thiết kế và chế tạo "
      "bằng cách điền glycerene (glycerin) vào vỏ áp kế để triệt tiêu rung. Một cách rẻ tiền "
      "khác là tiết lưu van cô lập đầu tiên (van lấy mẫu) của hệ thống lắp đặt áp kế. Áp suất "
      "chênh lệch tạo ra qua lỗ của van lấy mẫu sẽ triệt tiêu rung do dòng chảy không tầng của "
      "chất lỏng.",
      "In normal application, the pressure gage is installed as usual with the help of ¼ inch or "
      "½ inch NPT (Nominal Pipe Thread) connection. In application where the gage is subject to "
      "mechanical vibration, sectors made of bakelite to withstand the vibration in a better way "
      "than do the standard one which is made of brass or phosphor bronze. In applications to "
      "measure the pressure of a liquid delivered by high-speed gear pump and high-pressure "
      "dosing pump, amplitude of vibration may be low, but frequency is very high. The high "
      "frequency vibration is destructive to the mechanical system of the pressure gage and "
      "therefore, have to be damped out. Care should be taken during design and manufacturing "
      "itself by filling the casing of the pressure gage with glycerene so that the vibration is "
      "damped out. Another inexpensive method is to throttle the first isolation valve "
      "(tapping valve) of the pressure gage installation system. The differential pressure, so "
      "created, across the orifice of the tapping valve damps out the vibration due to "
      "non-laminar flow of the fluid.")

    H(b, lang, "Hiệu chỉnh các sai số trong áp kế",
      "Calibration adjustments for Errors in pressure gages", level=4)
    P(b, lang,
      "Nói chung có bốn loại sai số thường gặp ở áp kế:",
      "In general, there are four different kinds of errors encountered with pressure gages:")
    L(b, lang,
      ["(a) Hệ số nhân,", "(b) Góc lệch,", "(c) Khe hở và", "(d) Chuyển động mất."],
      ["(a) Multiplication", "(b) Angularity", "(c) Backlash", "(d) Lost motion."])

    P(b, lang, "<b>(a) Hệ số nhân</b>", "<b>(a) Multiplication</b>")
    P(b, lang,
      "Sự phù hợp của chuyển động kim so với chuyển động đầu mút gọi là hệ số nhân. Thông số này "
      "xác định dải đo của áp kế, từ đó điều chỉnh giá trị đọc ở đầu trên thang. Hệ số nhân của "
      "áp kế có dải 0 đến 100 kg/cm2 có thể cao tới 16:1. Sai số hệ số nhân được hiệu chỉnh bằng "
      "cách thay đổi chiều dài cần phân đoạn. Nếu giá trị đọc cao hơn, cần tăng chiều dài cần "
      "phân đoạn làm cho giá trị đọc thang giảm. Ngược lại, khi đọc thấp thì giảm chiều dài cần "
      "phân đoạn để có giá trị đọc cao hơn.",
      "Matching of pointer movement with respect to tip movement is called multiplication. This "
      "fixes up the span of the pressure gage thereby making adjustment for top scale reading. "
      "Multiplication for the pressure gages under the range of 0 to 100 kg/cm2 can be as high as "
      "16:1. Multiplication error is corrected by varying the length of segment lever. If the "
      "reading is on the higher side, the length of the segment lever should be increased "
      "resulting in lowering of scale reading. To the contrary when it reads low the length of "
      "the segment lever should be decreased to obtain higher reading.")

    P(b, lang, "<b>(b) Góc lệch</b>", "<b>(b) Angularity</b>")
    P(b, lang,
      "Đôi khi sai số đọc lại xuất hiện ở giữa thang. Đó gọi là góc lệch. Lỗi này xảy ra khi "
      "chuyển động thẳng được đổi thành chuyển động góc nhờ cơ cấu cần đơn. Dù không thể loại bỏ "
      "hoàn toàn sai số góc lệch, điều chỉnh thanh liên kết có thể giảm thiểu ảnh hưởng của nó. "
      "Nếu dụng cụ đọc thấp ở giữa thang, tăng chiều dài thanh liên kết để đọc cao hơn. Nếu đọc "
      "cao, giảm chiều dài thanh liên kết để đọc thấp hơn.",
      "Sometimes the error in reading may be found in the middle of the scale. This is called "
      "angularity. This is caused when rectilinear motion is converted to angular motion by "
      "means of single lever arrangement. While complete elimination of angularity error is "
      "impossible, adjustment in link can, however, minimize the effect. If the instrument reads "
      "low at mid-scale, the link length is increased to make it read high. If the reading is "
      "high, the link length is decreased to make it read low.")

    P(b, lang,
      "Việc điều chỉnh thanh liên kết cũng như cần phân đoạn để khử sai số là vấn đề thử và sai, "
      "dựa trên kinh nghiệm cá nhân. Tuy nhiên, các điều chỉnh này có xu hướng làm xáo trộn lẫn "
      "nhau và khi kết hợp cũng làm xáo trộn cả vị trí số không của thang. Vị trí số không lại "
      "được kiểm tra và chỉnh lại bằng vít chỉnh số không.",
      "Adjustments in link as well as segment lever for eliminating the error is a matter of "
      "trial and error and is based on individual experience. These adjustments, however, tend "
      "to upset each other and in combination they will upset the zero setting of the scale as "
      "well. The zero setting is again checked and adjusted by means of zero setting screw.")

    P(b, lang, "<b>(c) Khe hở</b>", "<b>(c) Backlash</b>")
    P(b, lang,
      "Do hoạt động lặp đi lặp lại của hệ thống bánh răng, các răng có thể bị mòn (hao mòn tự "
      "nhiên), sinh ra khe hở ở các răng. Hiện tượng này gọi là khe hở. Cách xử lý là đại tu, thay "
      "bánh răng và hiệu chuẩn lại dụng cụ.",
      "Due to repeated operation of gear-system, the teeth may get eroded (normal wear and tear) "
      "thereby producing play in gear teeth. This phenomena is called backlash. The solution to "
      "this problem is overhauling, replacement of gear and recalibration of the instrument.")

    P(b, lang, "<b>(d) Chuyển động mất</b>", "<b>(d) Lost motion</b>")
    P(b, lang,
      "Sai số do chuyển động mất liên quan đến ma sát ở ổ trục. Cách xử lý lại là đại tu, lắp lại "
      "và hiệu chuẩn lại.",
      "The error encountered due to lost motion is related to friction in the spindle bearings. "
      "The solution to this problem is again overhauling, refixing and recalibration.")

    H(b, lang, "Áp kế milimet", "Millimeter Gages", level=4)
    P(b, lang,
      "Đây là các áp kế dải thấp. Chúng được chế tạo từ phần tử dạng xoắn ốc, ống Bourdon, nang "
      "hoặc ống sóng. Các áp kế dải thấp này thường dùng để đo tổn thất áp suất gió (draft) từ "
      "đầu ra của quạt gió cưỡng bức đến buồng đốt của lò hơi. Dải thường gặp gồm 0 đến 4000 mm "
      "(dương) cột nước quy chiếu theo khí quyển và cũng từ 220 mm (âm) cột nước đến số không.",
      "These are low range gages. These are made of spiral type, bourdon tube, capsule or "
      "bellows elements. These low range gages are generally used for measurement of draft loss "
      "starting from Induced Draft Fan discharge to combustion chamber of the boiler. The usual "
      "ranges include 0 to 4000 mm (positive) of water column with respect to atmosphere and "
      "also from 220 mm (negative) of water column to zero.")

    P(b, lang,
      "Một phần tử rất nhạy khác dùng chế tạo áp kế milimet là màng ngăn mềm (slack diaphragm). "
      "Màng ngăn mềm dùng một lò xo đã hiệu chuẩn để cân bằng tác động của áp suất quá trình cần "
      "đo như trên Hình 2.11.",
      "Another very sensitive element used for manufacture of millimeter gages is slack "
      "diaphragm. Slack diaphragm uses a calibrated spring to balance the action of process "
      "pressure to be measured as shown in Figure 2.11.")

    P(b, lang,
      "Như ta thấy, các phần tử sơ cấp dùng chế tạo áp kế dải thấp có bản chất mỏng manh và đáp "
      "ứng nhạy vì chúng phải làm việc với áp suất cực thấp.",
      "As we observe the primary elements used for manufacture of low range gages are delicate "
      "in nature and sensitive in response because these are to be operated upon by extremely "
      "low pressure.")

    FIG(b, 11, F.fig_f11(), lang)

    H(b, lang, "Áp kế áp suất tuyệt đối", "Absolute Pressure Gage", level=4)
    P(b, lang,
      "Áp suất quan sát được quy chiếu theo chân không là áp suất tuyệt đối. Trong tính toán "
      "thông thường, áp suất tuyệt đối được tính bằng cách cộng áp suất khí quyển vào áp suất "
      "đo đã đo được. Để đo trực tiếp, người ta dùng cấu trúc cho trên Hình 2.12.",
      "The observed pressure with reference to vacuum is absolute pressure. In normal "
      "calculation, the absolute pressure is calculated by adding the atmospheric pressure to "
      "the measured gage pressure. For direct measurement purposes, the construction indicated "
      "on Figure 2.12 is utilized.")

    FIG(b, 12, F.fig_f12(), lang)

    P(b, lang,
      "Trong cấu trúc này, một bộ nang đã được rút chân không được gắn cứng bên trong một buồng "
      "kín khí. Chất lỏng quá trình đi vào qua đầu nối có khớp nén chống rò. Vì các nang được "
      "rút chân không hoàn toàn, áp suất đo được theo cách này chính là áp suất tuyệt đối của "
      "chất lỏng quá trình.",
      "In this arrangement, a set of evacuated capsules are fixed rigidly inside an airtight "
      "chamber. The process fluid is entered through the inlet connection having a leak-proof "
      "compression fittings. Since the capsules are completely evacuated, the measured pressure, "
      "in this way is the absolute pressure of the process fluid.")

    P(b, lang,
      "Một cấu trúc khác dùng hệ thống hai ống sóng cũng có thể đo áp suất tuyệt đối như Hình "
      "2.13. Ở đây một ống sóng được rút chân không và chất lỏng quá trình đi vào qua ống sóng "
      "kia. Chuyển động chênh lệch được chỉ thị như áp suất tuyệt đối của chất lỏng.",
      "In another arrangement, a twin-bellows system can also be utilized for measurement of "
      "absolute pressure as shown in Figure 2.13. Here one of the bellows is evacuated and the "
      "process fluid is entered through the second bellows. The differential movement is "
      "indicated as absolute pressure of the fluid.")

    FIG(b, 13, F.fig_f13(), lang)

    H(b, lang, "Áp kế màng ngăn", "Diaphragm Gages", level=4)
    P(b, lang,
      "Có những điều kiện quá trình mà áp kế thiết kế và chế tạo thông thường không làm việc "
      "được:",
      "There are process conditions where a normally designed and fabricated gage fails to "
      "operate. These are:")
    L(b, lang,
      ["(i) Chất lỏng quá trình làm tắc phần tử cảm biến,",
       "(ii) Chất lỏng cần đo có tính ăn mòn mạnh và vật liệu chống ăn mòn quá đắt nên không chọn "
       "được,",
       "(iii) Chất lỏng bị đông cứng do thay đổi đột ngột điều kiện môi trường."],
      ["(i) When a process fluid clogs the sensing element,",
       "(ii) Fluid under measurement is strongly corrosive in nature and the material available "
       "to fight the corrosion is too expensive to be selected,",
       "(iii) When the fluid freezes due to sharp change in ambient condition."])

    P(b, lang,
      "Để đáp ứng các điều kiện trên, người ta dùng phớt hóa chất trong áp kế. Phớt hóa chất "
      "hiệu quả nhất làm bằng một màng ngăn mỏng, dẻo đóng vai trò phần tử tách giữa chất lỏng và "
      "phần tử đo. Không gian phía trên màng ngăn được lấp đầy hoàn toàn bằng chất lỏng không nén "
      "được, đã chọn lọc phù hợp và ổn định theo nhiệt độ. Các chất lỏng này có thể là glycerene, "
      "dầu hoặc chất lỏng silicone không chứa bọt khí. Áp kế màng ngăn như vậy được cho trên "
      "Hình 2.14.",
      "To meet the above conditions chemical seals are utilized in the gage. The most effective "
      "chemical seal is made of a thin flexible diaphragm which acts as separating member "
      "between fluid and the element. The space above the diaphragm is completely filled with "
      "properly selected, temperature stable non-compressible liquid. These liquids can be "
      "glycerene, oil or silicone fluid free from air droplets. Such a diaphragm gage has been "
      "shown on Figure 2.14.")

    FIG(b, 14, F.fig_f14(), lang)

    H(b, lang, "Áp kế phớt thể tích", "Volumetric Seal Gages", level=4)
    P(b, lang,
      "Đây là một dạng đặc biệt của áp kế màng ngăn. Phớt màng ngăn và phần tử áp kế được tách "
      "nhau bằng một đoạn ống mao dẫn bằng kim loại. Cả ống mao dẫn lẫn toàn bộ phần tử áp kế đều "
      "chứa đầy chất lỏng làm kín. Thiết kế phớt thể tích cho phép đặt điểm lắp đặt tách rời điểm "
      "đo, tạo môi trường không rung cho các bộ phận của áp kế.",
      "This is a special version of a diaphragm gage. The diaphragm seal and the gage element are "
      "separated by means of a metallic capillary tubing. The capillary tubing as well as the "
      "entire gage element are all filled with sealing fluid. The volumetric seal design allows "
      "installation point to be separated from the measurement point, which presents vibration "
      "free atmosphere for the gage components.")

    P(b, lang,
      "Kết nối lắp đặt cho phần tử màng ngăn trong áp kế màng ngăn hoặc áp kế phớt thể tích có "
      "thể kiểu mặt bích hoặc kiểu hàn ổ cắm như Hình 2.14 và Hình 2.15. Với áp kế phớt thể "
      "tích, ba thanh kim loại mỏng có lỗ nhỏ được bố trí như hình để cố định áp kế vào tường "
      "hoặc giá đỡ.",
      "Installation connection for the diaphragm element in case of diaphragm gages or "
      "volumetric seal gages can be of flange type or socket weld type as shown in Figures 2.14 "
      "and 2.15. In case of volumetric seal gages, three small holed thin metallic strips are "
      "provided as shown for fixing the gage in a wall or on a fixing stand.")

    FIG(b, 15, F.fig_f15(), lang)

    # ------------------------------- (iii) Indirect measurement devices
    H(b, lang, "(iii) Thiết bị đo gián tiếp", "(iii) Indirect measurement devices", level=4)
    P(b, lang,
      "Mọi loại hệ thống truyền áp suất đều thuộc nhóm này. Nhóm được gọi là gián tiếp vì áp "
      "suất ở đây được đo bằng kỹ thuật suy luận và được chỉ thị dưới dạng tín hiệu đầu ra chuẩn. "
      "Tín hiệu tương tự đầu ra chuẩn đó là 0.2 đến 1.0 kg/cm2 (dạng khí nén khi môi trường là "
      "không khí dụng cụ) hoặc 4 đến 20 mAmps D.C. (dạng điện tử), thu được bằng cách dùng các "
      "phần tử bộ chuyển đổi khác nhau cùng hệ thống cấp nguồn cần thiết. Các loại bộ phát sau "
      "sẽ được thảo luận tại đây:",
      "All types of pressure transmitting systems fall under this category. The category is "
      "called indirect because the pressure in this is measured by inferential techniques and is "
      "indicated in terms of standard output signal. This standard output analog signal being "
      "0.2 to 1.0 kg/cm2 (pneumatic type when the medium used is instrument air) or 4 to 20 "
      "mAmps D.C. (electronic type) are obtained by employing different transducer element along "
      "with required supply system. Following types of transmitters shall be discussed here:")
    L(b, lang,
      ["(a) Bộ phát áp suất khí nén,", "(b) Bộ phát áp suất căng kế điện,",
       "(c) Bộ phát áp suất điện dung,", "(d) Bộ phát áp suất cảm ứng biến đổi,",
       "(e) Bộ phát áp suất tần số cộng hưởng,", "(f) Bộ phát số và", "(g) Bộ phát thông minh."],
      ["(a) Pneumatic pressure transmitter,", "(b) Electrical strain gage transmitter,",
       "(c) Capacitance pressure transmitter,", "(d) Variable inductance pressure transmitter,",
       "(e) Resonant frequency pressure transmitter,", "(f) Digital transmitter,",
       "(g) Smart transmitter."])

    H(b, lang, "(a) Bộ phát áp suất khí nén", "(a) Pneumatic pressure transmitter", level=4)
    P(b, lang,
      "Hệ thống cánh van–vòi phun kết hợp với hệ thống phản hồi khí nén như đã nêu ở trên là trái "
      "tim của bộ phát khí nén. Hoạt động tổng thể của bộ phát được cho trên Hình 2.16. Áp suất "
      "quá trình đặt lên nang màng định vị cánh van nối với thanh lực tới vòi phun. Áp suất ngược "
      "sinh ra được rơle khí nén khuếch đại và xuất hiện ở đầu ra (0.2 đến 1.0 kg/cm2 dạng khí "
      "nén) như tín hiệu đo của áp suất đặt vào. Đầu ra này cũng được đưa song song tới ống sóng "
      "phản hồi để đưa thanh lực về trạng thái cân bằng. Bất kỳ thay đổi nào của áp suất đặt vào "
      "làm mất cân bằng thanh lực và tín hiệu đầu ra tỷ lệ lại xuất hiện.",
      "Flapper-nozzle system combined with pneumatic feedback system as described earlier is the "
      "heart of pneumatic transmitter. The overall functioning of this transmitter has been "
      "shown in Figure 2.16. The process pressure applied on the diaphragm capsule positions the "
      "flapper connected to the force bar to the nozzle. The resulting back pressure is amplified "
      "by the pneumatic relay and appear as output (0.2 to 1.0 kg/cm2 pneumatic) as a measurement "
      "signal for the applied pressure. This output is also applied parallely to the feedback "
      "bellows to bring the force bar under equilibrium. Any change in applied pressure upsets "
      "this equilibrium of the force bar and a proportional output will once again appear.")

    FIG(b, 16, F.fig_f16(), lang)

    P(b, lang,
      "Hoạt động khuếch đại của rơle khí nén cũng phụ thuộc vào áp suất ngược ở vòi phun. Áp suất "
      "ngược được đưa vào một phía của màng rơle, đẩy màng sang trái. Chuyển động này định vị lại "
      "quả bóng và tăng luồng khí tới cổng ra của rơle khí nén. Điều này làm tăng áp suất đầu ra, "
      "áp suất này tác động lên diện tích bề mặt van. Áp suất đầu ra tiếp tục tăng cho đến khi "
      "áp suất trên van đủ tạo lực bằng với lực của áp suất vòi phun tác động lên màng. Lực ở hai "
      "phía màng bằng nhau dẫn đến trạng thái cân bằng của màng, van và đế van. Điều này được cho "
      "trên Hình 2.17.",
      "Functioning of pneumatic relay for amplification is also dependent upon nozzle "
      "backpressure. The backpressure is applied on one side of the relay diaphragm moving it to "
      "the left. This movement repositions the ball and increases the airflow to the output port "
      "of the pneumatic relay. This increases the output pressure, which is applied to the valve "
      "surface area. The output pressure goes on increasing until this pressure on valve is "
      "enough to create a force equal to that of the nozzle pressure acting on the diaphragm. The "
      "force on both sides of the diaphragm are equal which results in equilibrium of the "
      "diaphragm, valve and seat. This has been shown in Figure 2.17.")

    FIG(b, 17, F.fig_f17(), lang)

    P(b, lang,
      "Khi cánh van rời xa vòi phun làm giảm áp suất ngược, quả bóng dịch sang phải làm giảm "
      "tiết diện giữa cổng cấp và cổng ra. Điều này làm giảm áp suất đầu ra. Đầu ra tiếp tục giảm "
      "cho đến khi lực do áp suất đầu ra cân bằng áp suất vòi phun.",
      "When flapper moves away from the nozzle, decreasing the backpressure, the ball is on to "
      "right decreasing restriction between supply and output ports. This results in decrease in "
      "output pressure. This output goes on decreasing until force due to output pressure "
      "balances the nozzle pressure.")

    P(b, lang,
      "Hệ số khuếch đại của bộ khuếch đại khí nén nằm trong khoảng 1.2 đến 20. Vì lực phản hồi "
      "ngược chiều với áp suất đặt vào, người ta gọi đó là phản hồi âm. Chỉnh số không của tín "
      "hiệu đo được thực hiện bằng vít chỉnh quy chiếu, còn chỉnh dải đo bằng bánh xe dải. Độ "
      "chính xác 1% của dải hiệu chuẩn là đạt được, bao gồm cả tuyến tính, trễ và khả năng lặp "
      "lại.",
      "The gain of pneumatic amplifier ranges from 1.2 to 20. Since the feedback force is in "
      "opposition to the applied pressure, it is said to be negative feedback. Zero adjustment "
      "in the measurement signal is done by reference adjustment screw whereas a span adjustment "
      "is done by the range wheel. Accuracy of 1% of calibrated span is obtainable which "
      "includes linearity, hysteresis and repeatability.")

    H(b, lang, "(b) Bộ phát áp suất căng kế điện",
      "(b) Electrical strain gage transmitter", level=4)
    P(b, lang,
      "Hệ thống đo của loại bộ phát điện tử vòng hở này dùng nguyên lý cơ bản là sự thay đổi điện "
      "trở. Phần tử bộ chuyển đổi cơ bản của bộ phát này là căng kế dán. Sự thay đổi điện trở theo "
      "áp suất quá trình cần đo rất nhỏ nhưng chính xác, làm cho phép đo hoàn toàn tuyến tính. Sự "
      "thay đổi điện trở được đo bằng mạch cầu Wheatstone một chiều. Hình 2.18 cho thấy mạch đo "
      "điển hình của một bộ phát đo áp suất. Mỗi nhánh của cầu chứa một phần tử nhạy biến dạng "
      "(một vài phần tử có thể là giả). Nếu ban đầu cầu được coi là cân bằng, sự thay đổi áp suất "
      "sẽ làm mất cân bằng cầu. Điện áp mất cân bằng Delta V được cho bởi:",
      "The measuring systems of this type of open loop electronic transmitter utilizes the "
      "basic system of change in resistance. The basic transducer element for this transmitter is "
      "the bonded strain gage element. The change in resistance with respect to process pressure "
      "to be measured shall be very small but precise, making the measurement operation "
      "completely linear. The change in resistance is measured by a D.C. Wheatstones bridge "
      "circuit. Figure 2.18 shows a typical measurement circuit for a pressure measuring "
      "transmitter. Each arm of the bridge contains a strain-sensitive element (a few of these "
      "may be dummy as well). If it is considered to be balanced initially, a change in pressure "
      "shall result in unbalance of the bridge. The unbalance voltage Delta V shall be given by:")

    FIG(b, 18, F.fig_f18(), lang)
    E(b, lang,
      "Delta V = (Eb/Ro) [(ΔR₁ + ΔR₃) − (ΔR₂ + ΔR₄)]",
      "Delta V = (Eb/Ro) [(ΔR₁ + ΔR₃) − (ΔR₂ + ΔR₄)]", num="2.4")
    P(b, lang,
      "trong đó Ro là điện trở ban đầu của mỗi phần tử (giống nhau cho tất cả); Rt là điện trở "
      "dùng bù nhiệt độ; Rc là điện trở dùng bù điện trở đầu cuối.",
      "where Ro is the initial resistance of each element (being same for all); Rt is the "
      "resistance for temperature compensation; Rc is the resistance for terminal resistance "
      "compensation.")

    P(b, lang,
      "Sơ đồ đơn giản của bộ phát căng kế như vậy được cho trên Hình 2.19. Áp suất tăng đặt vào "
      "cổng áp suất cao tạo ra lực làm thay đổi biến dạng trên phần tử cảm biến (cụm lực căng kế "
      "cùng dây nối). Điện áp đầu ra kết quả tỷ lệ với áp suất đặt vào được bộ khuếch đại đầu vào "
      "cảm nhận, bộ này điều khiển bộ điều chỉnh dòng đầu ra. Chỉnh dải đo đặt hệ số khuếch đại "
      "vòng kín của bộ khuếch đại đầu vào, từ đó đặt dải đo của dụng cụ. Chỉnh số không thiết lập "
      "dòng chuẩn số không là 4 mAmps D.C. tại giới hạn dưới yêu cầu của dải đo.",
      "A simplified diagram of such strain gage transmitter has been shown on Figure 2.19. An "
      "increase in pressure applied on high-pressure port develops a force, which changes the "
      "strain on the sensing element (strain gage force unit along with connecting wire). The "
      "resulting voltage output which shall be proportional to applied pressure is sensed by "
      "input amplifier that drives the output current regulator. The span adjustment sets the "
      "closed loop gain of input amplifier. This in turn sets the measurement span of the "
      "instrument. The zero adjustment establishes the zero reference current to 4 mAmps D.C. at "
      "the required lower range limit.")

    FIG(b, 19, F.fig_f19(), lang)

    P(b, lang, "Các vấn đề gặp phải ở bộ phát căng kế:",
      "Problems encountered with strain gage transducers")
    L(b, lang,
      ["(i) Đặc tính áp suất–biến dạng và đặc tính biến dạng–điện trở nhìn chung có tuyến tính "
       "kém. Các đặc tính này trở nên hoàn toàn không đạt yêu cầu nhất là ở vùng áp suất chênh "
       "lệch thấp khi đo lưu lượng nhỏ,",
       "(ii) Cần bù nhiệt độ để xử lý sự biến đổi phi tuyến của giá trị điện trở do thay đổi "
       "nhiệt độ, việc này vừa phức tạp vừa tốn kém."],
      ["(i) Pressure-strain characteristic as well as strain-resistance characteristic, in "
       "general, have poor linearity. These characteristics become completely unsatisfactory "
       "especially in the region of low differential pressure for measurement of low flow,",
       "(ii) Temperature compensation is required to deal with the non-linear variation in "
       "resistance value due to change in temperature, which becomes complicated as well as "
       "expensive."])
    P(b, lang,
      "Những vấn đề này đã được khắc phục bằng cách thiết kế bộ phát kiểu điện dung.",
      "These problems have been removed by designing capacitance type transmitter.")

    H(b, lang, "(c) Bộ phát áp suất điện dung",
      "(c) Capacitance pressure transmitter", level=4)
    P(b, lang,
      "Bộ phát kiểu điện dung thuộc dạng thiết kế theo cấu trúc, trong khi bộ phát kiểu căng kế "
      "thuộc dạng theo tính chất vật lý. Nguyên lý hoạt động cơ bản của bộ phát áp suất điện dung "
      "nằm ở việc đo sự thay đổi điện dung của bộ chuyển đổi điện dung do chuyển động của phần tử "
      "áp suất gây ra khi có áp suất đặt vào. Trong hệ thống đo như vậy, hai bản cực tụ điện được "
      "bố trí với một khe hở giữa chúng, một mạch dao động được đặt để cấp năng lượng cho phần tử "
      "cảm biến và một mạch phát hiện điện dung được dùng để nhận biết sự thay đổi giá trị điện "
      "dung. Phần tử cảm biến được cho trên Hình 2.20, còn mạch dao động cùng mạch phát hiện điện "
      "dung được cho trên Hình 2.21.",
      "The capacitance type transmitter belongs to structural type of design whereas strain gage "
      "type transmitter is from physical property type. The basic operating principle for "
      "capacitance pressure transmitter lies in the measurement of change in capacitance of "
      "capacitive transducer resulting from the movement of a pressure element due to applied "
      "pressure. In such a measurement system, two capacitor plates are arranged with a gap "
      "between them, an oscillator circuit is placed to energise the sensing element and a "
      "capacitance detecting circuit is used to detect the change in capacitance value. Sensing "
      "element has been shown in Figure 2.20 and the oscillator circuit along with capacitance "
      "detecting circuit has been shown in Figure 2.21.")

    P(b, lang,
      "Trong khi chế tạo phần tử cảm biến, cần đặt một lượng sức căng ban đầu xác định lên màng "
      "cảm biến để có đặc tính tuyến tính giữa áp suất đặt vào (cần đo) và độ võng kết quả. Màng "
      "mỏng cần sức căng ban đầu lớn. Phần tử cảm biến được chế tạo sao cho sức căng ban đầu đã "
      "đặt có độ ổn định trong thời gian dài. Buồng đo nơi đặt màng cảm biến được lấp đầy hoàn "
      "toàn bằng dầu silicon từ màng cảm biến đến màng cách ly. Cấu trúc này gọi là cấu trúc buồng "
      "nổi và được thiết kế để giảm thiểu hư hỏng do quá áp và sự trôi hiệu chuẩn do áp suất tĩnh "
      "và nhiệt độ.",
      "During construction of sensing element, specific amount of initial tension is required to "
      "be put to the sensing diaphragm to have linear characteristic between applied pressure "
      "(to be measured) and resulting deflection. Thin diaphragm needs large initial tension. "
      "The sensing element is constructed in such a way that the initial tension which has been "
      "put shall have stability over a long period of time. The measuring chamber where sensing "
      "diaphragm is located is filled with silicone oil completely from the sensing diaphragm to "
      "isolating diaphragm. This type of construction is called floating cell construction and "
      "is designed to minimize damage due to overpressure effect and calibration drift due to "
      "static pressure effect and temperature effect.")

    FIG(b, 20, F.fig_f20(), lang)

    P(b, lang,
      "Khi áp suất cần đo được đặt vào màng cảm biến, dầu silicon bị nén và độ võng của màng cảm "
      "biến được phát hiện dưới dạng thay đổi điện dung. Nếu vô tình có một lượng quá áp đặt vào, "
      "nó chỉ ảnh hưởng tới màng cách ly. Cấu trúc buồng nổi chứa dầu silicon cùng với áp suất "
      "tĩnh không làm thay đổi sức căng ban đầu đã đặt cho màng cảm biến, do đó không có sự thay "
      "đổi hiệu chuẩn.",
      "When the pressure to be measured is applied to the sensing diaphragm the silicone oil gets "
      "pressurized and the deflection of the sensing diaphragm is detected in terms of change in "
      "capacitance. If some amount of overpressure gets applied accidentally, it affects the "
      "isolating diaphragm only. The floating cell construction filled with silicone oil together "
      "with the static pressure do not change the initial tension provided to the sensing "
      "diaphragm and therefore, there is no change in calibration.")

    P(b, lang,
      "Trong mạch dao động và mạch phát hiện điện dung, nguồn xoay chiều cần thiết có tần số từ "
      "50 đến 100 kHz do bộ dao động cung cấp. Tín hiệu từ mạch dao động được ghép sang thân bộ "
      "phát qua phần tử cảm biến bằng điện dung. Điện dung giữa phần tử cảm biến và bản cực tụ "
      "điện được chuyển thành tín hiệu đầu ra chuẩn 4 đến 20 mAmps (D.C.). Hình 2.21 là sơ đồ "
      "khối của một bộ phát áp suất điện dung thực tế. Trong hoạt động thực tế, áp suất đặt lên "
      "các màng cách ly được truyền tới dầu silicon. Dầu truyền áp suất tới màng cảm biến đặt ở "
      "tâm cảm biến. Màng cảm biến hoạt động như một phần tử lò xo được căng, võng ra khi có áp "
      "suất đặt vào. Độ dịch chuyển của màng cảm biến cỡ 0.1 milimet tỷ lệ trực tiếp với áp suất "
      "đặt vào như Hình 2.22.",
      "In the oscillator and the capacitance detecting circuit, required A.C. supply of "
      "frequency between 50 and 100 kHz is given by the oscillator. The signal from the "
      "oscillator circuit is coupled to the transmitter body capacitively through the sensing "
      "element. The capacitance between the sensing element and the capacitor plate is converted "
      "to 4 to 20 mAmps (D.C.) standard output signal. Figure 2.21 represents a block diagram of "
      "a practical capacitance type pressure transmitter. During actual operation, the applied "
      "pressure on the isolating diaphragms is transmitted to the silicone oil. The oil transmits "
      "the pressure to the sensing diaphragm located at the centre of the sensor. The sensing "
      "diaphragm functions as a stretched spring element that deflects in response to applied "
      "pressure. The displacement of the sensing diaphragm which is of the order of 0.1 "
      "millimetre is directly proportional to applied pressure as shown in the Figure 2.22.")

    FIG(b, 21, F.fig_f21(), lang)

    return "".join(b)
