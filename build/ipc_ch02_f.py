# -*- coding: utf-8 -*-
"""Chapter 2, section F: Acceleration, Torque, 12 worked examples, Exercise.

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), work/ipc_decoded.txt lines 4479-4996, PDF pp.
122-135 / printed pp. 110-123.  Covers subsection 2.3.3 "Acceleration",
subsection 2.3.4 "Torque", the twelve worked Examples 2.1-2.12 and the
eleven-question Exercise.  Figures 2.49-2.58 and equations (2.11)-(2.20)
are inserted in source order.  The printed equations survive the PDF only as
scattered glyphs and are reconstructed with standard notation; the printed
numerical answers are preserved throughout.
"""
import ipcfig2 as F
from ipc_ch02_lib import H, P, L, E, FIG, TBL, NOTE

# Keep section() callable even before the vector figure suppliers register
# their tuples.  Real registered accessors always take precedence.
for _n in range(49, 59):
    _attr = "fig_f%02d" % _n
    if not hasattr(F, _attr):
        setattr(F, _attr,
                (lambda _n=_n: ("<svg></svg>", "Hình 2.%d" % _n,
                                "Figure 2.%d" % _n, "", "")))


def section(lang):
    b = []

    # ---------------------------------------------------------------- 2.3.3
    H(b, lang, "2.3.3 Gia tốc", "2.3.3 Acceleration", level=3)
    P(b, lang,
      "Như chúng ta đã biết, chuyển vị, vận tốc và gia tốc là ba trạng thái khác nhau của một hệ "
      "thống dưới tác động của rung động cơ khí. Trạng thái ổn định theo một hướng nhất định tại "
      "một thời điểm nhất định là chuyển vị. Sự thay đổi của chuyển vị theo thời gian theo đường "
      "thẳng là vận tốc tuyến tính. Chuyển vị góc theo thời gian hay số vòng quay theo thời gian "
      "là vận tốc góc hay tốc độ. Tương tự, vận tốc thay đổi theo thời gian là gia tốc. Cả ba đều "
      "có thể suy ra từ phép đo rung động, vì vậy một thiết bị cảm nhận rung động có thể xác định "
      "cả ba biến số.",
      "As is known to us, the displacement, velocity or acceleration are all different conditions "
      "of a system under the influence of mechanical vibration. A steady state condition in a "
      "particular direction at a particular instant of time is displacement. A variation in the "
      "displacement with respect to time in straight line is linear velocity. An angular "
      "displacement with respect to time or revolution with respect to time is angular velocity "
      "or speed. Similarly variable velocity with respect to time is acceleration. All three can "
      "be derived from the measurement of vibration, therefore, a vibration-sensing device can "
      "determine all the three variables.")
    P(b, lang,
      "Ba biến số này liên hệ với nhau theo thời gian sao cho chuyển vị có thể được vi phân liên "
      "tiếp để nhận vận tốc và gia tốc. Tương tự, gia tốc có thể được tích phân để nhận vận tốc "
      "và chuyển vị.",
      "These three variables are so related to one-another with respect to time that the "
      "displacement can be differentiated successfully to obtain velocity as well as "
      "acceleration. Similarly, acceleration can be integrated to obtain velocity as well as "
      "displacement.")
    P(b, lang,
      "Để đo gia tốc, hệ thống phổ biến nhất là gia tốc kế địa chấn (seismic accelerometer). "
      "Chúng ta đã thảo luận cấu trúc lò xo–khối lượng địa chấn trong hệ thống đo vận tốc. Nguyên "
      "lý cơ bản cũng như quan hệ giữa tỷ lệ cản và tần số tự nhiên không cản được áp dụng ở đây. "
      "Dựa trên lý thuyết cơ bản này, chúng ta sẽ xét bốn cấu trúc khác nhau để đo gia tốc: (i) gia "
      "tốc kế chiết áp, (ii) gia tốc kế căng kế dán, (iii) gia tốc kế LVDT và (iv) gia tốc kế áp "
      "điện.",
      "For measurement of acceleration, the most popular system is the seismic accelerometer. We "
      "have already discussed the seismic spring-mass arrangement in the velocity measurement "
      "system. The basic principle as well as the relation for damping ratio and undamped natural "
      "frequency shall apply here also. Based on this basic theory, we shall discuss four "
      "different arrangements for measurement of acceleration: (i) Potentiometric accelerometer, "
      "(ii) Bonded strain gage accelerometer, (iii) LVDT accelerometer, and (iv) Piezoelectric "
      "accelerometer.")

    H(b, lang, "(i) Gia tốc kế chiết áp", "(i) Potentiometric accelerometer", level=4)
    P(b, lang,
      "Trong hệ thống này, một khối lượng địa chấn được nối với một chiết áp có cần tiếp điểm "
      "(wiper). Chuyển động tương đối của khối lượng địa chấn so với giá đỡ của bộ chuyển đổi "
      "được chiết áp cảm nhận và cho ra điện áp tỷ lệ như Hình 2.49.",
      "In this system a seismic mass, which is connected to a potentiometer is equipped with a "
      "wiper. The motion of the seismic mass relative to the support of the transducer is sensed "
      "by the potentiometer and a proportional voltage output is obtained from the potentiometer "
      "as shown in Figure 2.49.")
    FIG(b, 49, F.fig_f49(), lang)
    P(b, lang,
      "Ưu điểm của hệ thống này chỉ có một là cấu trúc rất đơn giản. Nhược điểm là tần số tự "
      "nhiên rất thấp (dưới 100 Hz) và độ phân giải cũng rất thấp.",
      "Advantage of such a system is only one and that is the simplicity in construction. The "
      "disadvantages being very low natural frequency (less than 100 Hz) and also very low "
      "resolution.")

    H(b, lang, "(ii) Gia tốc kế căng kế dán", "(ii) Bonded strain gage accelerometer", level=4)
    P(b, lang,
      "Đây cũng là một thiết bị rất đơn giản như Hình 2.50. Biến dạng do rung động của tổ hợp "
      "khối lượng và dầm công xôn tỷ lệ với gia tốc và được đo qua đầu ra của căng kế. Chuyển vị "
      "x của khối lượng m có thể viết là:",
      "This is also a very simple device as shown in Figure 2.50. Strain developed by the "
      "vibration of the mass and cantilever combination is proportional to acceleration and is "
      "measured by the strain gage output. The displacement x of the mass m can be expressed as:")
    FIG(b, 50, F.fig_f50(), lang)
    E(b, lang, "x = Fd · L³ / (3 · E · I)", "x = Fd · L³ / (3 · E · I)", num="2.11")
    P(b, lang,
      "trong đó Fd là lực làm lệch tác dụng lên khối lượng, L là chiều dài dầm công xôn, E là mô-đun "
      "đàn hồi Young và I là mô-men quán tính của cấu trúc dầm công xôn.",
      "where Fd is the deflecting force on the mass, L is the length of the cantilever, E is the "
      "Youngs modulus of elasticity and I is moment of inertia of the cantilever structure.")
    P(b, lang,
      "Hệ số lò xo Ks của hệ thống được cho bởi:",
      "Now spring constant Ks of the system is given by:")
    E(b, lang, "Ks = Fd / x = 3 · E · I / L³", "Ks = Fd / x = 3 · E · I / L³", num="2.12")
    P(b, lang,
      "Do đó, tần số tự nhiên không cản Wn của hệ thống là:",
      "Hence, undamped natural frequency Wn of the system is given by:")
    E(b, lang, "Wn = √(Ks / m) = √(3 · E · I / (m · L³))",
      "Wn = √(Ks / m) = √(3 · E · I / (m · L³))", num="2.13")
    P(b, lang,
      "Biến dạng ε được cho bởi:",
      "The strain ε is given by:")
    E(b, lang, "ε = σ / E = Fd · L · t / (2 · E · I)",
      "ε = σ / E = Fd · L · t / (2 · E · I)", num="2.14")
    P(b, lang,
      "trong đó t là chiều dày của cấu trúc dầm công xôn.",
      "where t is the thickness of the cantilever structure.")
    FIG(b, 51, F.fig_f51(), lang)
    P(b, lang,
      "Có thể tạo một cấu trúc khác có tần số tự nhiên cao hơn bằng cách đặt một giá đỡ cứng cho "
      "khối lượng địa chấn. Ưu điểm bổ sung của giá đỡ cứng (Hình 2.51) là nó vừa tạo tác dụng lò "
      "xo vừa tạo tác dụng cản. Giá đỡ này cũng cung cấp không gian để lắp căng kế đo biến dạng "
      "kết quả.",
      "An alternative arrangement for obtaining higher natural frequency can be made by providing "
      "a solid support to the seismic mass. Additional advantage of the solid support (as shown "
      "in Figure 2.51) is that it provides spring as well as damping action. The support also "
      "provides space for installation of strain gage for measurement of resultant strain.")

    H(b, lang, "(iii) Gia tốc kế LVDT", "(iii) LVDT accelerometer", level=4)
    P(b, lang,
      "Trong gia tốc kế LVDT, lõi của LVDT chính là khối lượng địa chấn của hệ thống. Hai đầu của "
      "khối lượng địa chấn được gắn vào khung đỡ thông qua tổ hợp lưỡng rung và thanh như Hình "
      "2.52.",
      "In LVDT accelerometer, the core of the LVDT constitutes the seismic mass of the system. "
      "Both ends of the seismic mass are attached to the supporting frame through vibration reed "
      "and rod combination as shown in Figure 2.52.")
    FIG(b, 52, F.fig_f52(), lang)
    P(b, lang,
      "Tổ hợp lưỡng rung và thanh cũng tạo tác dụng lò xo. Tín hiệu đầu ra e0 tỷ lệ với biên độ "
      "rung động. Ưu điểm của hệ thống này là đạt được tần số tự nhiên rất cao và độ phân giải "
      "cũng tốt hơn.",
      "The combination of reed and the rod provide spring action as well. The output signal e0 is "
      "proportional to the amplitude of the vibration. Advantage of this system is that a very "
      "high natural frequency is obtainable by this. Also the resolution is better.")

    H(b, lang, "(iv) Gia tốc kế áp điện", "(iv) Piezoelectric accelerometer", level=4)
    P(b, lang,
      "Trong gia tốc kế áp điện, người ta dùng tinh thể áp điện nhạy lực, do đó nó trở thành hệ "
      "thống bộ chuyển đổi chủ động không cần nguồn phụ. Bộ chuyển đổi biến lực tỷ lệ với gia tốc "
      "tác dụng lên khối lượng thành tín hiệu điện. Lực Fa trước hết sinh điện tích qe cho bởi "
      "quan hệ:",
      "In piezoelectric accelerometer a force-sensitive piezoelectric crystal is employed and "
      "therefore, it becomes an active transducer system that does not require auxiliary power "
      "supply. The transducer converts the force proportional to acceleration acting on the mass "
      "into electrical signal. The force Fa first of all generates an electrical charge qe, which "
      "is given by the relation:")
    E(b, lang, "qe = Kc · Fa", "qe = Kc · Fa", num="2.15")
    P(b, lang,
      "trong đó Kc là hằng số độ nhạy điện tích của tinh thể.",
      "where Kc is charge sensitivity constant of the crystal.")
    P(b, lang,
      "Điện áp đầu ra eo được cho bởi:",
      "The voltage output eo is given by:")
    E(b, lang, "eo = qe / Cp", "eo = qe / Cp", num="2.16")
    P(b, lang,
      "trong đó Cp là điện dung của tinh thể. Khi thay qe vào quan hệ trên, biểu thức của eo trở "
      "thành:",
      "where Cp is the capacitance offered by the crystal. When the value of qe is put in the "
      "above relation, the expression for eo becomes:")
    E(b, lang, "eo = (Kc / Cp) · Fa = (Kc · m / Cp) · (d²y / dt²)",
      "eo = (Kc / Cp) · Fa = (Kc · m / Cp) · (d²y / dt²)", num="2.17")
    P(b, lang,
      "với Fa = m · d²y/dt². Như Hình 2.53, tinh thể áp điện được đặt dưới khối lượng địa chấn, "
      "tựa vào một lò xo nặng. Dưới tác động của gia tốc, khối lượng địa chấn gây ứng suất lên "
      "tinh thể và cho điện áp đầu ra eo. Ưu điểm của hệ thống là kích thước nhỏ và tần số tự "
      "nhiên cao (100 kHz). Nhược điểm là không dùng được cho ứng dụng tần số thấp.",
      "where Fa = m · d²y/dt². As shown in Figure 2.53, the piezoelectric crystal is positioned "
      "under the seismic mass against a heavy spring. Under the influence of acceleration, the "
      "seismic mass stresses the crystal and as a result voltage output eo is obtained. Advantages "
      "of the system are small size and also higher natural frequency (100 KHz). Disadvantage is "
      "that it cannot be employed for low frequency application.")
    FIG(b, 53, F.fig_f53(), lang)

    # ---------------------------------------------------------------- 2.3.4
    H(b, lang, "2.3.4 Mô-men xoắn", "2.3.4 Torque", level=3)
    P(b, lang,
      "Mô-men xoắn là hiệu ứng quay của một lực khi tác dụng tiếp tuyến. Sự quay của cánh cửa "
      "trong nhà quanh bản lề là ví dụ về tạo mô-men xoắn. Như vậy, mô-men xoắn được định nghĩa là "
      "mô-men vặn làm xoắn hoặc có xu hướng xoắn một vật cứng. Chuyển động kết quả, tính theo "
      "chuyển vị góc, được dùng để đo mô-men xoắn.",
      "Torque is the rotational effect of a force when applied tangentially. The rotation of a "
      "household door with respect to its hinge is an example of creation of torque. Thus, the "
      "torque can be defined as torsional twisting moment that twists or tends to twist a rigid "
      "body. The resultant motion, which is in terms of angular displacement, can be employed for "
      "measurement of torque.")
    P(b, lang,
      "Nhiều phương pháp đã được nghĩ ra để đo mô-men xoắn, gồm: (a) máy đo mô-men xoắn kiểu ứng "
      "suất, (b) máy đo mô-men xoắn điện, và (c) máy đo mô-men xoắn dynamometer.",
      "Many methods have been devised for measurement of torque, which fall under. (a) Stress type "
      "torque meter, (b) Electrical torque meter, and (c) Dynamometer torque meter.")

    H(b, lang, "(a) Máy đo mô-men xoắn kiểu ứng suất",
      "(a) Stress type torque meter", level=4)
    P(b, lang,
      "Máy đang quay khi hoạt động chịu ứng suất xoắn trên trục quay. Điều này tạo biến dạng kéo "
      "và biến dạng nén trên trục ở góc ± 45°. Hai biến dạng chính này (kéo và nén) có độ lớn bằng "
      "nhau nhưng ngược dấu. Chúng tỷ lệ với mô-men xoắn Tg tạo ra chúng. Quan hệ gần đúng giữa "
      "Tg và biến dạng ε là:",
      "Rotating machine while in action experiences torsional stress on the rotating shaft. This "
      "creates tensile as well as compressive strain on the shaft at an angle of ± 45°. These two "
      "principal strains (tensile and compressive) are of equal magnitude but of opposite "
      "polarity. These strains are proportional to torque Tg producing the strains. The "
      "approximate relation between Tg and strain ε is given by:")
    E(b, lang, "Tg = 0.196 · E · ε · d₀³ / (1 + ν)",
      "Tg = 0.196 · E · ε · d₀³ / (1 + ν)", num="2.18")
    P(b, lang,
      "trong đó E là mô-đun đàn hồi Young và d₀ là đường kính của trục quay. Các biến dạng này "
      "được đo chính xác bằng bốn căng kế dán có độ nhạy cao đặt ở góc 45° so với trục quay như "
      "Hình 2.54. Tổ hợp bốn căng kế dán này được nối vào mạch cầu Wheatstone để đo. Căng kế 1, "
      "2 cảm nhận biến dạng kéo, căng kế 3, 4 cảm nhận biến dạng nén.",
      "where E is Young's modulus of elasticity, do is the diameter of rotating shaft. These can "
      "be measured accurately by four numbers of highly sensitive bonded strain gage placed at an "
      "angle of 45° with respect to the rotating shaft axis as shown in Figure 2.54. This "
      "combination of four numbers of bonded strain gages are connected to a Wheatstone bridge "
      "network for measurement. The strain gages 1,2 are for sensing tensile strain and that of "
      "3, 4 are for sensing compressive strain.")
    FIG(b, 54, F.fig_f54(), lang)
    P(b, lang,
      "Việc sử dụng thiết bị này bị giới hạn trong khoảng 2000 đến 6000 vòng/phút do hạn chế rõ "
      "rệt của tổ hợp vòng trượt và chổi than. Một loại máy đo mô-men xoắn kiểu ứng suất khác có "
      "thể thiết kế dùng máy biến áp quay và bộ dao động, hoàn toàn không tiếp xúc và dùng được "
      "cho máy quay tốc độ cao hơn.",
      "Use of this instrument is limited in between 2000 and 6000 RPM due to obvious limitation "
      "created by slip ring and brush combination. Another stress type torque meter can be "
      "designed using rotating transformer and oscillator, which is completely contactless and "
      "can be used for higher speed rotating machines.")

    H(b, lang, "(b) Máy đo mô-men xoắn điện", "(b) Electrical torque meter", level=4)
    P(b, lang,
      "Trong nhóm này chúng ta xét ba biến thể thiết kế dựa theo loại đầu dò: (i) dùng máy phát "
      "A.C. làm đầu dò, (ii) dùng cảm biến tiệm cận làm đầu dò, và (iii) dùng cảm biến quang làm "
      "đầu dò.",
      "Under this category we shall discuss three different design variations based upon the "
      "type of detector used. These are: (i) Use of A.C. generator as detector, (ii) Use of "
      "proximity sensor as detector, and (iii) Use of optical sensor as detector.")

    H(b, lang, "(i) Dùng máy phát A.C. làm đầu dò",
      "(i) Using A.C. generator as detector", level=4)
    P(b, lang,
      "Hai bánh răng cách nhau một khe hở đủ lớn được lắp trên trục quay. Hai máy phát A.C. được "
      "ghép riêng với hai hệ bánh răng này. Các máy phát A.C. cấp điện cho cuộn sơ cấp của một bộ "
      "máy biến áp mắc ngược pha. Điện áp vì thế thường triệt tiêu nhau, nhưng do hiệu ứng xoắn "
      "của trục nên sự triệt tiêu không hoàn toàn. Hiệu điện áp này cảm ứng điện áp vào cuộn thứ "
      "cấp. Vì điện áp cảm ứng là kết quả của hiệu ứng xoắn, nó tỷ lệ với mô-men xoắn. Toàn bộ hệ "
      "thống thể hiện trong Hình 2.55.",
      "Two gears separated by a gap of sufficient length are arranged on a rotating shaft. Two "
      "A.C. generators are coupled separately to these gear systems. These A.C. generators supply "
      "power to the primary windings of a transformer-set connected in phase opposition. The "
      "voltages thus are normally cancelled but due to torsion effect of the shaft, incomplete "
      "cancellation results. This difference induces a voltage in secondary of the transformers. "
      "Since this induced voltage is a result of torsional effect, this is proportional to torque. "
      "The entire system has been shown in Figure 2.55.")
    FIG(b, 55, F.fig_f55(), lang)
    P(b, lang,
      "Ưu điểm của cấu trúc này phụ thuộc vào đặc tính cơ của vật liệu trục, ví dụ độ đàn hồi phải "
      "đủ lớn để tạo khác biệt pha lớn về điện áp phát ra, cỡ 10 đến 15 độ. Nhược điểm là phương "
      "pháp này không chính xác lắm và không hiệu chuẩn tĩnh được.",
      "Advantages obtainable from this arrangement depend upon the mechanical characteristics of "
      "the shaft material, e.g. elasticity which should be sufficient to create large phase "
      "difference in the generated voltage of the order of 10 to 15 degrees. Disadvantages are "
      "that this is not a much accurate method of measurement and also static calibration is not "
      "possible.")

    H(b, lang, "(ii) Dùng cảm biến tiệm cận làm đầu dò",
      "(ii) Using proximity sensor as detector", level=4)
    P(b, lang,
      "Trong một phương án khác của phương pháp điện, có thể dùng cảm biến tiệm cận thay máy phát "
      "A.C. như Hình 2.56. Cảm biến tiệm cận về cơ bản là bộ thu từ tính, tạo chuỗi xung điện theo "
      "sự quay của hệ bánh răng. Sự khác biệt pha do tải trên trục quay được bộ phát hiện pha cảm "
      "nhận và tỷ lệ với mô-men xoắn. Đây là phương pháp chính xác hơn.",
      "In another scheme under electrical method, proximity sensor can be employed in place of "
      "A.C. generator as shown in Figure 2.56. Proximity sensors are essentially magnetic "
      "pick-ups, which generate series of electrical pulses with respect to rotation of the gear "
      "system. Phase difference created due to load on rotating shaft is sensed by the phase "
      "detector, which is proportional to torque. This is comparatively more accurate method.")
    FIG(b, 56, F.fig_f56(), lang)

    H(b, lang, "(iii) Dùng cảm biến quang làm đầu dò",
      "(iii) Using optical sensor as detector", level=4)
    P(b, lang,
      "Trong phương án này, các xung được tạo bởi tổ hợp LED–photo transistor như Hình 2.57. Sự "
      "khác biệt nhỏ về truyền ánh sáng do tải trên trục giữa hai đĩa có khe cắt gắn trên chu vi "
      "trục quay được bộ phát hiện quang cảm nhận. Đầu ra của cảm biến tỷ lệ với mô-men xoắn. Đây "
      "cũng là phương pháp đo rất chính xác.",
      "In this scheme, the pulses are generated by LED-photo transistor combination as shown "
      "Figure 2.57. A slight difference in light propagation created by the load on the shaft "
      "between two slotted discs fixed on the periphery of the rotating shaft is sensed by the "
      "photo detector. The sensor output is proportional to the torque. This is also a very "
      "accurate method of measurement.")
    FIG(b, 57, F.fig_f57(), lang)

    H(b, lang, "(c) Máy đo mô-men xoắn dynamometer",
      "(c) Dynamometer torque meter", level=4)
    P(b, lang,
      "Phương pháp này dùng hệ truyền dây đai. Trong hệ truyền dây đai, sự chênh lệch lực căng dây "
      "được cân bằng hiệu quả bằng một khối lượng đặt phù hợp. Cấu trúc như vậy thể hiện trong "
      "Hình 2.58.",
      "This method employs belt transmission system. In belt transmission system, difference in "
      "belt tension can be balanced effectively by a suitably placed mass. Such an arrangement "
      "has been shown in Figure 2.58.")
    FIG(b, 58, F.fig_f58(), lang)
    P(b, lang,
      "Lực căng tổng hợp do T1 và T2 tác dụng lên hệ cần đòn bẩy quay quanh A được cân bằng bởi "
      "khối lượng M. Mô-men xoắn tổng hợp do T1 và T2 là (T₂ − T₁) · 2l, với l là chiều dài AB "
      "trong hình. Tương tự, mô-men xoắn cân bằng do khối lượng M là Mg · d₀, với g là gia tốc "
      "trọng trường và d₀ là khoảng cách từ khối lượng đến điểm quay.",
      "The resultant tension due to T1 and T2 is acting on the lever system pivoted at A is being "
      "counter-balanced by the mass M. The resultant torque due to tension T1 and T2 is given by "
      "(T₂ − T₁) · 2l, where l is the length AB as shown in the diagram. Similarly the balancing "
      "torque created by the mass M is given by Mg · d₀ where g is the acceleration due to gravity "
      "and d₀ is the distance between the mass and the pivot.")
    P(b, lang, "Ở trạng thái cân bằng:", "At equilibrium condition,")
    E(b, lang, "(T₂ − T₁) · 2l = Mg · d₀", "(T₂ − T₁) · 2l = Mg · d₀", num="2.19")
    P(b, lang,
      "Mô-men xoắn đầu ra được tìm từ quan hệ:",
      "Output torque can be found out by the relation,")
    E(b, lang, "Tout = (T₂ − T₁) · r = Mg · d₀ · r / (2 · l)",
      "Tout = (T₂ − T₁) · r = Mg · d₀ · r / (2 · l)", num="2.20")

    # ---------------------------------------------------------------- examples
    H(b, lang, "Ví dụ", "Examples", level=3)
    P(b, lang,
      "<b>Ví dụ 2.1.</b> Một áp kế đọc giá trị áp suất là 3,7 kg/cm². Nếu áp suất khí quyển tại "
      "nơi đo là 1,0 kg/cm² thì áp suất tuyệt đối là bao nhiêu?",
      "<b>Example 2.1.</b> A pressure measuring gage reads a value of pressure as 3.7 kg/cm2. If "
      "the atmospheric pressure at the place of measurement happens to be 1.0 kg/cm2, then what "
      "is the absolute pressure?")
    P(b, lang,
      "<b>Lời giải.</b> Vì áp kế chỉ áp suất tương đối (Pg) của hệ thống là 3,7 kg/cm². Áp suất "
      "tuyệt đối = Pg + Patm. Ở đây áp suất khí quyển Patm = 1,0 kg/cm². Vậy áp suất tuyệt đối = "
      "3,7 + 1,0 = 4,7 kg/cm² A.",
      "<b>Solution.</b> Since the pressure gage indicates gage pressure (Pg) of the system which "
      "is = 3.7 kg/cm2. Now absolute pressure = Pg + Patm. Here, atmospheric pressure Patm = 1.0 "
      "kg/cm2. ∴ Absolute pressure = 3.7 + 1.0 = 4.7 kg/cm2 A.")
    P(b, lang,
      "<b>Ví dụ 2.2.</b> Tính áp suất do cột nước cao 1 mm tạo ra.",
      "<b>Example 2.2.</b> Calculate the value of pressure exerted by a column of water of 1 mm.")
    P(b, lang,
      "<b>Lời giải.</b> Như đã biết, cột nước 10 mét tạo áp suất 1,0 kg/cm². Nếu xét một khối lập "
      "phương cạnh 10 m thì thể tích là 10 × 10 × 10 = 1000 m³ và diện tích mặt đáy là 100 m² chịu "
      "áp lực của 1000 m³ nước. Vì vậy 10 m cột nước (WC) ≈ 1 kg/cm², hay 10.000 mm WC ≈ 1 kg/cm², "
      "suy ra 1 mm WC = 1/10.000 = 10⁻⁴ kg/cm².",
      "<b>Solution.</b> As we know, a 10 metre water column exerts a pressure of 1.0 kg/cm2 i.e. "
      "if we consider a cube of 10 metre side each; we have a volume of 10 × 10 × 10 = 1000 cubic "
      "metre and a surface area of 100 square metre upon which the pressure created by 1000 cubic "
      "meter water shall act. Hence, 10 metre of water column (WC) ≈ 1 kg/cm2. or 10,000 "
      "millimetre (mm) of WC ≈ 1 kg/cm2. or 1 mm WC = 1/10,000 = 10⁻⁴ kg/cm2.")
    P(b, lang,
      "<b>Ví dụ 2.3.</b> Tính áp suất do cột nước cao 1 inch tạo ra.",
      "<b>Example 2.3.</b> Calculate the value of pressure exerted by a column of water of 1 inch.")
    P(b, lang,
      "<b>Lời giải.</b> Ta biết 1 foot khối nước nặng 62,342 pound. Trọng lượng này tác dụng lên "
      "diện tích 1 foot vuông (ft²), tương đương 144 inch vuông (in²). Vì vậy áp suất trên 144 in² "
      "là 62,342/144 = 0,433 psi (pound trên in²). Áp suất này tương đương cột nước 1 ft hay 12 "
      "inch. Do đó 0,433/12 = 0,036 psi trên mỗi inch. Vậy 1 inch WC ≈ 0,036 psi.",
      "<b>Solution.</b> We know that 1 cubic foot of water weighs 62.342 pounds. This weight acts "
      "on a surface area of 1 square foot (ft2), which is equivalent to 144 square inches (in2). "
      "Hence, pressure acting on 144 in2, = 62.342 pounds / 144 in2 = 0.433 psi (pounds per in2). "
      "This pressure is equivalent to a water column of 1 foot (ft) or 12 inches. Hence, "
      "0.433/12 inch psi = 0.036 psi per inch. Thus, 1 inch of WC ≈ 0.036 psi.")
    P(b, lang,
      "<b>Ví dụ 2.4.</b> Áp suất 40 psi tác dụng vào áp kế thủy ngân. Trọng số riêng của thủy ngân "
      "là 13,6. Tìm độ dịch chuyển của thủy ngân trong áp kế.",
      "<b>Example 2.4.</b> A pressure of 40 psi is applied to a mercury manometer. The specific "
      "gravity of mercury is 13.6. Find the displacement of mercury inside the manometer.")
    P(b, lang,
      "<b>Lời giải.</b> Ta biết 0,036 psi là áp suất do dịch chuyển 1 inch cột nước, nên áp suất "
      "Ps (psi) do dịch chuyển x inch chất lỏng có trọng số riêng ρ là Ps = x · 0,036 · ρ. Suy ra "
      "độ dịch chuyển x = 40/(0,036 · 13,6) = 81,7 inch.",
      "<b>Solution.</b> We know that 0.036 psi is the pressure created by the displacement of 1 "
      "inch of water column, therefore, the pressure (Ps) in psi created by displacement of x inch "
      "of liquid of specific gravity ρ shall be given by: Ps = x · 0.036 · ρ. ∴ Displacement x = "
      "40 psi / (0.036 psi × 13.6) = 81.7 inches.")
    P(b, lang,
      "<b>Ví dụ 2.5.</b> Một nhánh của áp kế chữ U chứa nước được nối với bơm chân không và không "
      "khí được hút sạch hoàn toàn. Nhánh kia hở ra khí quyển. Độ dịch chuyển của nước quan sát "
      "được là 34 feet. Hãy tính áp suất khí quyển.",
      "<b>Example 2.5.</b> One leg of a U-tube manometer water filled type is connected to a "
      "vacuum pump and the air is completely evacuated. The other leg is open to atmosphere. The "
      "displacement in water observed is 34 feet, calculate the atmospheric pressure.")
    P(b, lang,
      "<b>Lời giải.</b> Như đã biết, 1 ft WC ≈ 0,433 psi. Vì vậy 34 ft WC ≈ 34 × 0,433 = 14,722 "
      "psi. Vậy áp suất khí quyển = 14,722 psi.",
      "<b>Solution.</b> As we know, 1 ft WC ≈ 0.433 psi, Hence, 34 ft WC ≈ 34 × 0.433 = 14.722 "
      "psi. Thus, atmospheric pressure = 14.722 psi.")
    P(b, lang,
      "<b>Ví dụ 2.6.</b> Áp kế thủy ngân đọc áp suất bằng psi. Nếu trọng số riêng của thủy ngân là "
      "13,6, hãy tìm chiều dài thang tuyến tính biểu diễn 1 psi.",
      "<b>Example 2.6.</b> A mercury manometer reads pressure in psi. If specific gravity of "
      "mercury is 13.6, find the linear scale length representing 1 psi.")
    P(b, lang,
      "<b>Lời giải.</b> Ta biết 1 psi = 27,7 inch (cột nước). Thang đo là 27,7/13,6 = 2,036 inch. "
      "Vậy 2,036 inch biểu diễn 1 psi.",
      "<b>Solution.</b> We know, 1 psi = 27.7 inches. The scale shall be; 27.7/13.6 = 2.036 "
      "inches. Hence, 2.036 inches shall represent 1 psi.")
    P(b, lang,
      "<b>Ví dụ 2.7.</b> Một bộ phát áp suất được lắp thấp hơn 40 feet so với mức của bình hơi "
      "trong nhà máy. Tìm độ triệt tiêu zero cần thiết để bù sai số do cột tĩnh 40 feet gây ra.",
      "<b>Example 2.7.</b> A pressure-measuring transmitter has been mounted 40 feet below the "
      "level of a steam drum in a boiler house. Find the zero suppression required to compensate "
      "for the error introduced by the hydrostatic head of 40 feet.")
    P(b, lang,
      "<b>Lời giải.</b> 1 ft WC ≈ 0,433 psi. Áp suất do 40 feet WC = 0,433 × 40 = 17,32 psi. Áp "
      "suất 17,32 phải được trừ vào số đọc, hoặc có thể chỉnh bằng lò xo chỉnh triệt tiêu zero "
      "nếu có trong bộ phát.",
      "<b>Solution.</b> 1 ft of WC ≈ 0.433 psi. The pressure created by 40 feet WC = 0.433 × 40 "
      "= 17.32 psi. The pressure 17.32 must be deducted from the indicated reading or may be "
      "adjusted by means of zero suppression adjustment spring if installed in the transmitter.")
    P(b, lang,
      "<b>Ví dụ 2.8.</b> Đầu ra của LVDT được nối với vôn kế 10 volt qua bộ khuếch đại hệ số 300. "
      "Vôn kế có thang 100 vạch và độ đọc được đến 1/5 vạch. Điện áp 2 mV xuất hiện ở cọc LVDT khi "
      "lõi dịch chuyển 0,5 mm. Tìm: (i) độ nhạy của LVDT và của toàn hệ thống, và (ii) độ phân giải "
      "của máy.",
      "<b>Example 2.8.</b> The output of a LVDT is connected to a 10 volt voltmeter through an "
      "amplifier of gain 300. The voltmeter has a scale of 100 divisions and the readability of "
      "the scale is upto 1/5 of a division. An output of 2 mV appears across the terminals of the "
      "LVDT, when the core is displaced through a distance of 0.5 mm. Find out the: (i) Sensitivity "
      "of LVDT and also of entire set-up, and (ii) Resolution of the instrument.")
    P(b, lang,
      "<b>Lời giải.</b> Ở đây điện áp ra Vo = 2 mV và dịch chuyển d = 0,5 mm. (i) Độ nhạy của LVDT "
      "= Vo/d = 2 mV / 0,5 mm = 4 mV/mm. Độ nhạy của toàn hệ thống = hệ số khuếch đại × độ nhạy "
      "của LVDT = 300 × 4 mV/mm = 1200 mV/mm. (ii) 1 vạch thang = 10 V / 100 = 100 mV. Điện áp "
      "nhỏ nhất đọc được = (1/5) × 100 mV = 20 mV. Độ phân giải = 20 mV / (1200 mV/mm) = 0,0167 "
      "mm.",
      "<b>Solution.</b> Here LVDT output Vo = 2 mV and the displacement d = 0.5 mm. (i) Hence, "
      "sensitivity of LVDT = Vo/d = 2 mV / 0.5 mm = 4 mV/mm. Also sensitivity of entire set-up, = "
      "Amplification factor × Sensitivity of the LVDT. = 300 × 4 mV/mm = 1200 mV/mm. (ii) 1 scale "
      "division = 10 V / 100 = 100 mV. Minimum voltage read on the voltmeter = (1/5) × 100 mV = "
      "20 mV. Resolution = 20 mV / (1200 mV/mm) = 0.0167 mm.")
    P(b, lang,
      "<b>Ví dụ 2.9.</b> Gia tốc kế địa chấn có khối lượng 0,07 kg và hằng số lò xo 2,8 × 10³ N/m "
      "có dịch chuyển cực đại ± 0,029 m. Tìm gia tốc cực đại và tần số tự nhiên.",
      "<b>Example 2.9.</b> A seismic mass accelerometer of seismic mass of 0.07 kg and spring "
      "constant of 2.8 × 10³ N/m has maximum displacement of ± 0.029 metre. Find the maximum "
      "acceleration and natural frequency.")
    P(b, lang,
      "<b>Lời giải.</b> Ta biết vận tốc góc Wn = √(Kc/M), với Kc là hằng số lò xo và M là khối "
      "lượng. Vì vậy Wn = √(2,8 × 10³ / 0,07) = 200 rad/s. Gia tốc cực đại am = Wn² · d, với d là "
      "độ dịch chuyển. Vì vậy am = (200)² × 0,029 = 1160 m/s². Tần số tự nhiên fn = Wn/(2π) = "
      "200/(2π) = 31,85 Hz.",
      "<b>Solution.</b> We know that the angular velocity Wn is given by, Wn = √(Kc/M) where Kc "
      "is the spring constant and M is mass. Hence, Wn = √(2.8 × 10³ / 0.07) = 200 rad/sec. "
      "Maximum acceleration am is given by, am = Wn² · d where d is displacement. Hence, am = "
      "(200)² × 0.029 = 1160 metre/sec2. Natural frequency fn = Wn/(2π) = 200/(2π) = 31.85 Hz.")
    P(b, lang,
      "<b>Ví dụ 2.10.</b> Một trục thép mềm (M.S.) nối động cơ với tải có mô-men không đổi. Một "
      "căng kế lá có điện trở 120 Ω và hệ số gage 2 được dán trên trục, với trục căng kế tạo góc "
      "45° so với trục trục như hình vẽ. Mô-đun trượt của thép là 80 × 10⁹ N/m², bán kính trục 15 "
      "mm và độ biến đổi điện trở căng kế do tải là 0,24 Ω. Tìm mô-men tải.",
      "<b>Example 2.10.</b> An M.S. (Mild Steel) shaft is used to connect a motor drive to a "
      "constant load torque. A foil strain gage having a resistance of 120 Ω and gage factor 2 is "
      "mounted on the shaft with its axis as shown in the diagram (at 45° to the shaft axis). The "
      "shear modulus of steel is 80 × 10⁹ N/m2, the shaft radius 15 mm and the change in strain "
      "gage resistance due to load is 0.24 Ω. Find the load torque.")
    P(b, lang,
      "<b>Lời giải.</b> Một mặt vuông cạnh L bị biến dạng thành hình bình hành do biến dạng cắt α. "
      "Nếu góc cắt là α thì độ thay đổi chiều dài đường chéo là (L · √2/2) · α, với chiều dài "
      "đường chéo là L · √2. Vì vậy biến dạng đường chéo ε = ΔL/L = α · √2/2 ≈ α/2. Mặt khác ΔR/R "
      "= G · ε = 2 × (α/2) = α. Suy ra α = ΔR/R = 0,24/120 = 2 × 10⁻³ radian. Mô-men xoắn T = "
      "(π · Gs · r³/2) · α, với Gs là mô-đun trượt của thép. = (π × 80 × 10⁹ × (15 × 10⁻³)³ / 2) "
      "× 2 × 10⁻³ = 847,8 Nm.",
      "<b>Solution.</b> A square shape surface of side having length L gets deformed into a shape "
      "of parallelogram due to strain as shown on the diagram. If the angle of shear is α then the "
      "change in length shall be (L · √2/2) · α where the length of diagonal of square is L · √2. "
      "Hence, diagonal strain ε = ΔL/L = α · √2/2 ≈ α/2. But ΔR/R = G · ε = 2 × (α/2) = α. ∴ α = "
      "ΔR/R = 0.24/120 = 2 × 10⁻³ radians. Torque T = (π · Gs · r³/2) × α, where Gs is the shear "
      "modulus of steel. = (π × 80 × 10⁹ × (15 × 10⁻³)³ / 2) × 2 × 10⁻³ = 847.8 Nm.")
    P(b, lang,
      "<b>Ví dụ 2.11.</b> Một đĩa lắp trên trục máy có 12 điểm đánh dấu. Số lần chớp chiếu lên đĩa "
      "của đèn stroboscope là 6000 lần trong một phút. Tìm tốc độ máy nếu đĩa trông đứng yên và có "
      "một hình ảnh duy nhất của 12 điểm. Nếu đĩa trông chuyển động về phía trước theo chiều quay "
      "với 10 rpm, hãy tìm tốc độ của đĩa.",
      "<b>Example 2.11.</b> A disc mounted on the shaft of a machine has 12 marked points. The "
      "number of flashes projected on to the disc by a stroboscope is 6000 in one minute. Find the "
      "speed of the machine if the disc appears stationary and has single image of 12 points. If "
      "the disc appears to move forward in the direction of rotation at 10 rpm, find the speed of "
      "the disc.")
    P(b, lang,
      "<b>Lời giải.</b> Ở đây tốc độ máy N cho bởi N = F/n, với F là số lần chớp trong một phút và "
      "n là số điểm đánh dấu. Vì vậy N = 6000/12 = 500 rpm. Khi đĩa có vẻ chuyển động theo chiều "
      "quay, tốc độ máy là 500 + 10 = 510 rpm.",
      "<b>Solution.</b> Here the speed of the machine N is given by, N = F/n where F is number of "
      "flashes in one minute and n is number of marked point. ∴ N = 6000/12 = 500 rpm. When the "
      "disc appears to move in the direction of rotation, the speed of the machine becomes, 500 + "
      "10 = 510 rpm.")
    P(b, lang,
      "<b>Ví dụ 2.12.</b> Một LVDT chạy A.C. được cấp điện áp vào 10 volt. Nếu sự thay đổi đầu ra "
      "nằm trong khoảng −7,1 đến +7,1 cho dịch chuyển lõi từ −10 mm đến +10 mm, hãy tìm: (a) điện "
      "áp đầu ra khi lõi dịch từ −6 mm đến +8 mm, và (b) điện áp đầu ra khi lõi ở −5 mm từ vị trí "
      "zero.",
      "<b>Example 2.12.</b> An A.C. operated LVDT is supplied by an input voltage of 10 volt. If "
      "the variation in output ranges from −7.1 to +7.1 for the core displacement between −10 mm "
      "and +10 mm, find: (a) Output voltage Vs. Core displacement varies from −6 mm to +8 mm? (b) "
      "Output voltage when the core is at −5 mm from the zero position?")
    P(b, lang,
      "<b>Lời giải.</b> (a) Dịch chuyển từ −10 mm đến +10 mm cho đầu ra từ −7,1 đến +7,1 V, nên dịch "
      "chuyển −6 mm cho đầu ra −(6/10) × 7,1 = −4,26 V. Dịch chuyển +8 mm cho đầu ra +(8/10) × 7,1 "
      "= 5,68 V. (b) Dịch chuyển 5 mm từ vị trí zero cho đầu ra −(5/10) × 7,1 = −3,55 V.",
      "<b>Solution.</b> (a) Displacement from −10 mm to +10 mm produces voltage output between "
      "−7.1 and +7.1 and hence −6 mm displacement shall produce an output of −(6/10) × 7.1 = "
      "−4.26 volt. A displacement of +8 mm shall produce an output of +(8/10) × 7.1 = 5.68 volt. "
      "(b) Displacement of 5 mm from zero position shall produce an output of −(5/10) × 7.1 = "
      "−3.55 volt.")

    # ---------------------------------------------------------------- exercise
    H(b, lang, "Bài tập", "Exercise", level=3)
    L(b, lang,
      ["Mô tả hệ thống đo cơ bản của áp suất bằng áp kế chữ U. Áp kế nghiêng là gì? Nó khác áp kế "
       "chữ U thế nào?",
       "Mô tả áp kế ống Bourdon bằng sơ đồ. Hiện tượng rơ (backlash) trong áp kế là gì? Nó gây sai "
       "số trong số đọc như thế nào?",
       "Có những loại sai số nào gặp trong áp kế? Biện pháp khắc phục để triệt tiêu sai số là gì?",
       "Bộ phát áp suất khí nén hoạt động thế nào? Những hạn chế của bộ phát khí nén là gì?",
       "Bộ phát áp suất điện khác bộ phát khí nén thế nào? Lợi ích của bộ phát điện là gì?",
       "Bộ phát thông minh là gì? Nó khác bộ phát thông thường thế nào? Dùng bộ truyền HART để hiệu "
       "chuẩn bộ phát thông minh ra sao?",
       "Mô tả nguyên lý hoạt động của bộ chuyển đổi dịch chuyển.",
       "LVDT hoạt động thế nào? Giải thích chi tiết bằng sơ đồ.",
       "Chuyển vị, vận tốc và gia tốc liên hệ với nhau thế nào? Phép đo các đại lượng này được thực "
       "hiện ra sao?",
       "Giải thích nguyên lý cơ bản của đầu dò địa chấn (seismic pick-up).",
       "Có những phương pháp nào để đo mô-men xoắn? Giải thích chi tiết một phương pháp bất kỳ."],
      ["Describe the basic measurement system of pressure by means of U-tube manometer. What is an "
       "inclined manometer? How is it different from that of U-tube manometer?",
       "Describe Bourdon tube pressure gage with the help of a sketch. What is backlash in a "
       "pressure gage? How does it introduce error in the reading?",
       "What are different types of errors encountered in a pressure gage? What are the remedial "
       "measures adopted to eliminate the error?",
       "How does a pneumatic pressure transmitter function? What are the limitations of a "
       "pneumatic transmitter?",
       "How an electronic pressure transmitter is different from the pneumatic transmitter? What "
       "are the benefits of an electronic transmitter?",
       "What is a smart transmitter? How is it different from conventional transmitter? How a "
       "HART communicator is used for calibration of a smart transmitter?",
       "Describe the working principle of a displacement transducer.",
       "How does a LVDT work? Explain in detail with the help of a sketch.",
       "How displacement, velocity and acceleration are related to one another? How measurement of "
       "these are implemented?",
       "Explain the basic principle of a seismic pick-up.",
       "What are the different methods for measurement of torque? Explain any one method in "
       "detail."],
      ordered=True, start=1)

    return "".join(b)
