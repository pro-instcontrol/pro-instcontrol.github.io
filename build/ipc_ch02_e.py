# -*- coding: utf-8 -*-
"""Chapter 2, section 2.3.2 "Velocity" (EN/VI bilingual).

Source: Janardan Prasad, M. N. Jayaswal and Vishnu Priye, *Instrumentation and
Process Control* (I.K. International, 2019), PDF pp. 113-121 (printed pp.
101-109), decoded lines 4155-4478.  The source text layer keeps many OCR
artifacts; printed equations are rendered with standard mathematical notation
and the source quirks are retained in the English prose.
"""
import ipcfig2 as F
from ipc_ch02_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    H(b, lang, "2.3.2 Vận tốc", "2.3.2 Velocity", level=3)

    P(b, lang,
      "Đo vận tốc, tuyến tính hay quay, là một khía cạnh quan trọng trong thiết kế máy quay. Vận "
      "tốc có thể được đo bằng dịch chuyển tuyến tính trên một đơn vị thời gian. Sau khi đo dịch "
      "chuyển tuyến tính bằng bộ chuyển đổi vị trí, vận tốc có thể được suy ra bằng điện tử. Việc "
      "dùng mạch vi phân của khuếch đại thuật toán tạo ra hàm phụ thuộc thời gian của dịch chuyển. "
      "Tín hiệu có thể được hiệu chỉnh theo từng giai đoạn để tạo ra tín hiệu vận tốc. Tương tự, "
      "vận tốc cao hơn có thể được đo bằng dịch chuyển góc trên một đơn vị thời gian, rồi nếu cần "
      "thì được đổi sang vận tốc tuyến tính bằng phương pháp quy đổi thông thường.",
      "Measurement of velocity, linear or rotational, constitutes an important aspect in rotating "
      "machine design. Velocity can be measured in terms of linear displacement per unit time. "
      "After measurement of linear displacement by means of a position transducer, the velocity "
      "can be derived electronically. Use of operational amplifier differentiator circuit produces "
      "time-dependent function of displacement. The signal can be corrected in stages to produce "
      "velocity signal. Higher velocity, similarly can be measured in terms of angular displacement "
      "per unit time and then if required, is converted to linear velocity by usual method of "
      "conversion.")

    P(b, lang,
      "Bộ chuyển đổi đo vận tốc nói chung thuộc ba loại:",
      "Velocity measurement transducers are generally of three types:")
    L(b, lang,
      ["(a) Bộ chuyển đổi đo vận tốc tương đối.",
       "(b) Bộ chuyển đổi đo vận tốc tuyệt đối, và",
       "(c) Bộ chuyển đổi đo vận tốc góc."],
      ["(a) Relative velocity measurement transducer,",
       "(b) Absolute velocity measurement transducer, and",
       "(c) Angular velocity measurement transducer."])

    P(b, lang,
      "Trong hệ đo vận tốc tương đối, còn được gọi chung là bộ chuyển đổi vận tốc theo nghĩa thông "
      "thường, phép đo được thực hiện đối với một mốc cố định. Một điểm cân bằng của hệ đo được gắn "
      "vào một điểm cố định chọn trong không gian. Điểm kia được gắn vào vật thể cần đo vận tốc.",
      "In relative velocity measurement system, which is also called velocity transducer in general "
      "sense, the measurement is carried out with respect to a fixed reference. One equilibrium "
      "point of the measurement system is attached to a fixed point selected in space. The other "
      "one is attached to the object whose velocity has to be measured.")

    P(b, lang,
      "Mặt khác, với hệ đo vận tốc tuyệt đối, được gọi là bộ chuyển đổi địa chấn, điểm cân bằng duy "
      "nhất là đế của bố trí lò xo-khối thông thường. Đế của hệ này được gắn vào điểm cần đo vận tốc "
      "nên không có mốc cố định nào được thiết lập. Tuy nhiên, từ chuyển động đo được đối với đế của "
      "hệ, có thể thu được vận tốc tuyệt đối của vật đang xét. Những ví dụ thường gặp của loại đo "
      "vận tốc này là vận tốc của cánh máy bay trong hoạt động bay và vận tốc tự nhiên của một cây "
      "cầu tĩnh.",
      "On the other hand, with absolute velocity measurement system, which is named seismic "
      "transducers, the only equilibrium point is the base of the conventional spring-mass "
      "arrangement. The base of this system is attached to the point whose velocity has to be "
      "measured and no fixed reference can thus be made available. However, from the motion "
      "measured with respect to the base of the system, it is possible to obtain absolute velocity "
      "of the object under consideration. Usual examples of this category of velocity measurement "
      "constitute velocity of aircraft wing during flight operation and the natural velocity of a "
      "static bridge.")

    # ------------------------------------------------ (a) Relative velocity
    H(b, lang, "(a) Bộ chuyển đổi đo vận tốc tương đối",
      "(a) Relative Velocity Measurement Transducers", level=4)

    P(b, lang,
      "Tuy nhiên, đo vận tốc tương đối theo nghĩa trực tiếp có thể thực hiện bằng hai phương pháp "
      "cơ bản:",
      "Measurement of relative velocity, in direct sense, however, can be implemented by two basic "
      "methods:")
    L(b, lang,
      ["(i) Phương pháp nam châm di động, và",
       "(ii) Phương pháp cuộn dây di động."],
      ["(i) Moving magnet method and",
       "(ii) Moving coil method."])

    P(b, lang,
      "Trong phương pháp này, nguyên lý cảm ứng cơ bản được áp dụng, theo đó nếu một dây dẫn được "
      "quay hoặc chuyển động trong từ trường tĩnh, một suất điện động sẽ được cảm ứng tỉ lệ với "
      "chuyển động đó. Theo cách này, nếu ta sắp xếp cho nam châm chuyển động và giữ cuộn dây hay "
      "dây dẫn đứng yên, thì phương pháp được gọi là Phương pháp nam châm di động. Mặt khác, khi "
      "cuộn dây hay dây dẫn được cho chuyển động trong khi hệ từ được giữ yên, phương pháp được gọi "
      "là Phương pháp cuộn dây di động. Hai phương pháp này dựa trên phương trình toán học cơ bản "
      "sau:",
      "In this method, the basic principle of induction is utilized which states that if a "
      "conductor is rotated or moved in a static magnetic field, an emf is induced which shall be "
      "proportional to the movement. In this way, if we can arrange to move the magnet and keep the "
      "coil or conductor standstill, the method is called Moving Magnet Method. On the other hand, "
      "when the coil or conductor is allowed to move keeping the magnetic system steady, the method "
      "is called Moving Coil Method. These two methods are based on the fundamental mathematical "
      "equation:")
    E(b, lang, "E = Blv sinθ volt", "E = Blv sinθ volt", num="2.8")
    P(b, lang,
      "Trong đó E là suất điện động cảm ứng; B là mật độ từ thông tính bằng Wb/m²; l là chiều dài "
      "hiệu dụng của dây dẫn hoặc của cuộn dây tính bằng mét; v là vận tốc tương đối của cuộn "
      "dây/nam châm tính bằng mét/giây; và θ là góc chuyển động của cuộn dây so với hướng của từ "
      "trường.",
      "Where E is induced emf; B flux density in Wb/m2; l the effective length of the conductor or "
      "the coil in metre; v the relative velocity of the coil/magnet in metre/sec and θ being the "
      "angle of coil movement with respect to the direction of field.")

    P(b, lang,
      "Một bố trí cơ bản kiểu nam châm di động dùng để thiết kế bộ chuyển đổi vận tốc được thể hiện "
      "trong Hình 2.40. Phần tử cảm biến về bản chất là một thanh (gắn với nam châm), được nối cứng "
      "với thiết bị chính có vận tốc cần đo. Phần tử cảm biến này chuyển động bên trong khe hở "
      "không gian của cuộn dây, từ đó cảm ứng suất điện động trong cuộn dây đứng yên. Suất điện động "
      "được cảm ứng sẽ tỉ lệ với vận tốc của phần gắn nam châm.",
      "A basic moving magnet type of arrangement used for designing a velocity transducer has been "
      "shown in Figure 2.40. The sensing element is essentially a rod (attached to the magnet), "
      "which is coupled rigidly to the main equipment whose velocity has to be measured. This "
      "sensing element moves inside the air gap/space of the coil and thereby induces emf in the "
      "stationary coil. The emf so induced shall be proportional to the velocity of the magnet "
      "attachment.")
    FIG(b, 40, F.fig_f40(), lang)

    P(b, lang,
      "Tương tự, một bố trí kiểu cuộn dây di động được thể hiện trong Hình 2.41. Với bố trí này, "
      "chuyển động của chính cuộn dây được hình dung bên trong từ trường, theo chiều ngược lại. Do "
      "đó, phần tử cảm biến, ở đây là cuộn dây, được nối với thiết bị chính có vận tốc cần đo. Trong "
      "trường hợp này, đầu ra suất điện động cảm ứng tỉ lệ với vận tốc của cuộn dây.",
      "In the same way, a moving coil type of arrangement has been shown in Figure 2.41. With this "
      "arrangement the movement of coil itself is conceptualized inside the magnetic field to the "
      "contrary. Therefore, the sensing element, which is the coil here is to be connected to the "
      "main equipment of which the velocity is to be measured. The induced emf output shall be "
      "proportional to the velocity of the coil in this case.")
    FIG(b, 41, F.fig_f41(), lang)

    P(b, lang,
      "Ưu điểm của hệ nam châm di động nằm ở cấu trúc đơn giản, yêu cầu bảo trì tối thiểu (gần như "
      "không cần bảo trì), suất điện động cảm ứng tuyến tính theo sự thay đổi vận tốc và cuối cùng "
      "nhưng không kém quan trọng là giá thành rẻ. Nhược điểm là những nhiễu loạn trong hoạt động "
      "do từ trường tản, đáp ứng tần số hạn chế và không dùng được để đo rung.",
      "Advantages of moving magnet system lie in its simple construction, requires minimum "
      "maintenance (more or less maintenance free), induced emf being linear with respect to "
      "velocity change and last but not the least it is inexpensive. Disadvantages being "
      "disturbances in performance due to stray field, limited frequency response and inaccessible "
      "for vibration measurement.")

    P(b, lang,
      "Tương tự, ưu điểm của hệ cuộn dây di động là bố trí có thể dễ dàng được đặt trong một vỏ "
      "chống từ để bảo vệ nó khỏi từ trường tản.",
      "In the same way, the advantage of moving coil system is that the arrangement can be encased "
      "easily in an anti-magnetic enclosure to protect it from stray field.")

    P(b, lang,
      "Nhược điểm duy nhất của bố trí này là bảo trì trở nên khó khăn.",
      "The only disadvantage with this arrangement is that the maintenance becomes difficult.")

    # ------------------------------------------------ (b) Absolute velocity
    H(b, lang, "(b) Bộ chuyển đổi đo vận tốc tuyệt đối",
      "(b) Absolute Velocity Measurement Transducer", level=4)

    P(b, lang,
      "Như đã nói ở trên, phép đo vận tốc tuyệt đối có thể thực hiện bằng bộ chuyển đổi địa chấn. "
      "Bố trí tuyệt đối cơ bản được thể hiện trong Hình 2.42. Bố trí này thường được gọi là hệ lò "
      "xo-khối địa chấn một bậc tự do. Bậc tự do của một hệ về bản chất liên quan đến số biến đặc "
      "trưng xác định hoàn toàn vị trí của hệ tại bất kỳ thời điểm nào. Chẳng hạn, vĩ độ, kinh độ "
      "và độ cao xác định hoàn toàn vị trí của một vật thể đang chuyển động. Tuy nhiên, vị trí của "
      "một đoàn tàu hỏa chỉ được xác định bằng kinh độ, còn vị trí của một chiếc thuyền trôi tự do "
      "trên mặt nước được xác định bằng cả kinh độ lẫn vĩ độ. Tương tự, để xác định vị trí của một "
      "máy bay đang bay trên không, chúng ta cần cả ba đặc trưng, tức là kinh độ, vĩ độ và độ cao. "
      "Do đó chúng ta kết luận rằng bậc tự do của các vật thể nêu trên lần lượt là một, hai và ba.",
      "As indicated earlier, the absolute velocity measurement can be carried out by means of "
      "seismic transducer. The basic absolute arrangement has been shown in Figure 2.42. This "
      "arrangement is popularly known as single degree-of-freedom seismic spring-mass system. "
      "Degree-of-freedom of a system is essentially related to a number of characteristic variables "
      "that define the position of the system completely at any particular instant. For instance, "
      "the latitude, longitude and altitude define the position of a moving object completely. "
      "However, position of a railway train shall be defined by longitude only, the position of a "
      "boat freely running on water surface, on the other hand, shall be defined by longitude as "
      "well as latitude. Similarly, for defining the position of an aeroplane flying in air we "
      "shall require all the three characteristics, i.e. longitude, latitude and altitude. "
      "Consequently we conclude that the degree-of-freedom of above-mentioned objects are one, two "
      "and three respectively.")
    FIG(b, 42, F.fig_f42(), lang)

    P(b, lang,
      "Hệ thể hiện trong Hình 2.42 gồm một khối lượng m, một lò xo có hằng số ks và một bố trí giảm "
      "chấn (xi lanh thủy lực) có hằng số kd. Bố trí được lắp trên một giá đỡ. Khối lượng m chỉ tự "
      "do chuyển động theo một trục vuông góc với giá đỡ. Phương trình chuyển động của hệ như sau "
      "có thể được mô tả bằng:",
      "The system indicated in Figure 2.42 consists of a mass m, a spring of constant ks and a "
      "damping arrangement (dash-pot) having constant kd. The arrangement is installed on a "
      "support. The mass m is free to move only in one axis that is normal to the support. The "
      "equation of motion of such a system can be described by:")
    E(b, lang, "d²x/dt² + 2Gωₙ·dx/dt + ωₙ²x = d²y/dt²",
      "d²x/dt² + 2Gωₙ·dx/dt + ωₙ²x = d²y/dt²", num="2.9")
    P(b, lang,
      "trong đó x và y lần lượt là dịch chuyển của khối lượng và của giá đỡ; d²x/dt² và d²y/dt² lần "
      "lượt là gia tốc của khối lượng và của giá đỡ; G bằng kd/(2√(ks·m)) là tỉ số giảm chấn; và ωₙ "
      "bằng √(ks/m) là tần số tự nhiên không giảm chấn.",
      "where x and y are the displacement of mass and the support respectively, d²x/dt² and "
      "d²y/dt² are the acceleration of the mass and the support respectively, G which is equal to "
      "kd/(2√(ks·m)) is the damping ratio and ωn that equals √(ks/m) is the undamped natural "
      "frequency.")

    P(b, lang,
      "Trong bố trí này, bộ phận giảm chấn, thực chất là một xi lanh chứa chất lỏng nhớt chất lượng "
      "cao, làm tăng dải tần số mà hệ có thể hoạt động. Bố trí này biến chuyển động tuyệt đối y của "
      "giá đỡ thành chuyển động x của khối lượng so với giá đỡ. Vì vậy, trong phép đo thực tế, "
      "chuyển động của khối lượng m được đo so với giá đỡ. Để làm điều này, một bộ chuyển đổi đo "
      "vận tốc tương đối dùng chiết áp điện trở hoặc bố trí thay thế khác được nối giữa khối lượng "
      "m và giá đỡ.",
      "In this arrangement, the damping unit, which is in fact a dashpot filled with viscous fluid "
      "of fine quality, increases the range of frequency over which the system can operate. This "
      "arrangement transforms the absolute movement y of the support into the movement x of the "
      "mass relative to the support. In actual measurement therefore, the movement of the mass m is "
      "measured relative to the support. For this a relative velocity measuring transducer using "
      "resistance potentiometer or other alternative arrangement is connected in between the mass "
      "m and the support.")

    # ----------------------------------------------- (c) Angular velocity
    H(b, lang, "(c) Bộ chuyển đổi đo vận tốc góc",
      "(c) Angular Velocity Measurement Transducer", level=4)

    P(b, lang,
      "Để đo vận tốc góc, bố trí được dùng phải được gắn vật lý vào trục quay của thiết bị chính và "
      "có thể thu được một điện áp tỉ lệ với tốc độ bằng cách dùng hệ thích hợp. Dựa trên điện áp "
      "đầu ra thu được (một chiều hay xoay chiều), hai loại tốc kế có thể được thiết kế:",
      "For measurement of angular velocity, the arrangement used has to be physically attached to "
      "the rotating shaft of the main equipment and a voltage proportional to speed may be obtained "
      "by employing suitable system. Based upon the voltage output obtained (D.C. or A.C.), two "
      "types of tachometers can be designed:")
    L(b, lang,
      ["(i) Tốc kế máy phát một chiều,",
       "(ii) Tốc kế máy phát xoay chiều."],
      ["(i) D.C. Generator Tachometer,",
       "(ii) A.C. Generator Tachometer."])

    P(b, lang,
      "Trong trường hợp tốc kế máy phát một chiều, nguyên lý làm việc thường dùng của máy phát một "
      "chiều được áp dụng. Phần rôto được nối cơ khí với máy chính có tốc độ cần đo. Sự quay của "
      "rôto trong từ trường của nam châm vĩnh cửu sinh ra suất điện động tỉ lệ trực tiếp với tích "
      "của từ thông và tốc độ như thể hiện trên Hình 2.43. Vì từ thông do nam châm vĩnh cửu tạo ra "
      "là không đổi, suất điện động cảm ứng sẽ chỉ tỉ lệ với tốc độ. Suất điện động này là một "
      "chiều, có thể được đo bằng vôn kế PMMC (Nam châm vĩnh cửu - Cuộn dây di động) có thang đo "
      "được hiệu chuẩn trực tiếp theo tốc độ.",
      "In case of D.C. generator tachometer, the usual principle of D.C. generator working is "
      "employed. The armature proper is coupled mechanically with the main machine whose speed is "
      "to be measured. The rotation of armature in presence of permanent magnet field generates emf "
      "directly proportional to the product of flux and speed as shown on Figure 2.43. Since the "
      "flux due to permanent magnet is constant, the emf induced will be proportional to speed "
      "only. This emf being a D.C. one, can be measured by a PMMC (Permanent Magnet Moving Coil) "
      "voltmeter having the scale calibration is terms of speed directly.")
    FIG(b, 43, F.fig_f43(), lang)

    P(b, lang,
      "Ưu điểm của bố trí này nằm ở cấu trúc và vận hành đơn giản nên được dùng rộng rãi. Điện áp "
      "đầu ra có cỡ milivôn, là 10 mV/rpm, nên rất dễ đo bằng PMMC. Chiều quay của thiết bị chính "
      "cũng có thể xác định bằng cách kiểm tra cực tính của điện áp đầu ra.",
      "Advantages of this arrangement lie in its simple construction and operation and hence widely "
      "used. The output voltage is in milivolt being 10 mv/rpm and hence is measured by PMMC easily. "
      "The direction of rotation of the main equipment can also be found out by checking the "
      "polarity of the output voltage.")

    P(b, lang,
      "Nhược điểm thường giống như của máy một chiều. Cổ góp và chổi than cần bảo trì định kỳ. Sai "
      "số xuất hiện khi dòng rôto tăng, làm méo từ trường.",
      "The disadvantages are usually similar to that of a D.C. machine. Commutator and brushes need "
      "periodic maintenance. Error is introduced by increase in armature current, which distorts "
      "the field.")

    P(b, lang,
      "Tốc kế kiểu máy phát xoay chiều thực chất là một máy phát nhỏ. Từ trường kích thích cần thiết "
      "do nam châm vĩnh cửu hoặc nam châm điện gắn trên rôto của tốc kế tạo ra, và rôto này được nối "
      "cơ khí với trục của máy chính. Ở chiều ngược lại, cuộn dây được quấn trên stato. Sự quay của "
      "rôto cảm ứng điện áp xoay chiều trong cuộn stato, có biên độ và tần số tỉ lệ với tốc độ. Điện "
      "áp xoay chiều này có thể được chỉnh lưu trước khi đưa tới chỉ thị PMMC được hiệu chuẩn theo "
      "tốc độ. Hình 2.44 cho thấy bố trí này.",
      "A.C. generator type tachometer is in fact a small alternator. The necessary field for "
      "excitation is produced either by permanent magnet or electric magnet mounted on the rotor of "
      "the tachometer and this rotor is coupled mechanically to the shaft of the main machine. The "
      "coil on the other hand is wound on the stator. The rotation of the rotor induces an A.C. "
      "voltage in the stater coil, amplitude and frequency of which is proportional to the speed. "
      "This A.C. voltage can be rectified before sending it to a PMMC indicator which is calibrated "
      "in terms of speed. Figure 2.44 shows this arrangement.")
    FIG(b, 44, F.fig_f44(), lang)

    P(b, lang,
      "Một ưu điểm của bố trí này là vấn đề bảo trì do cổ góp và chổi than gây ra được loại bỏ hoàn "
      "toàn.",
      "One advantage of this arrangement is that the maintenance problem created due to commutator "
      "and brushes are completely removed.")

    P(b, lang,
      "Nhược điểm là ở tốc độ quay rất thấp, điện áp đầu ra trở nên rất nhỏ nên gợn sóng không được "
      "bộ lọc RC làm phẳng. Điều này gây sai số trong phép đo ở tốc độ thấp. Tuy nhiên, để giảm "
      "thiểu ảnh hưởng này, có thể thiết kế số cực lớn hơn trên rôto để tần số đầu ra tăng ngay cả "
      "ở tốc độ thấp.",
      "The disadvantage is that at very low rotational speed, the output voltage becomes very low "
      "and so ripples are not smoothened out by the RC-filter. This causes error in measurement on "
      "low speed. To minimize this effect however, larger number of poles can be designed on the "
      "rotor so the frequency of the output is increased even at low speed.")

    # --------------------------------------- Industrial RPM measurement
    H(b, lang, "Hệ đo RPM công nghiệp", "Industrial RPM Measurement System", level=4)

    P(b, lang,
      "Hệ đang xét là một bố trí điển hình để đo RPM của các máy tốc độ cao. Bố trí này được dùng "
      "rộng rãi để đo RPM của tổ máy tua-bin-máy phát, máy nén ly tâm dẫn động bằng tua-bin và nhiều "
      "tổ hợp khác.",
      "The system under consideration is a typical arrangement for measurement of RPM of high-speed "
      "machines. This arrangement is widely used to measure the RPM of turbine-alternator unit, "
      "turbo-driven centrifugal compressor and many other combinations.")

    P(b, lang,
      "Hệ gồm một nam châm được gắn vào trục quay và vì thế cấu thành bộ phận không thể tách rời của "
      "trục. Một cuộn dây lấy tín hiệu được bọc phù hợp trong một vỏ và đặt cách nam châm vài "
      "milimet. Hệ cáp che chắn (có thể là cáp đồng trục) nối cuộn lấy tín hiệu với chỉ thị RPM. "
      "Chỉ thị RPM có thể được lắp gần máy và/hoặc bên trong phòng điều khiển trung tâm.",
      "The system consists of a magnet, which is attached to the rotating shaft and therefore, "
      "constitutes integral part of the shaft. A pick-up coil suitably encapsulated in a housing "
      "is placed a few millimetre away from the magnet. A shielded cable (may be coaxial) system "
      "connects the pick-up coil to the RPM indicator. The RPM indicator may be installed near the "
      "machine and/or inside a central control room.")

    P(b, lang,
      "Khi nam châm quay cùng trục, nó sinh ra điện áp dạng sin trong cuộn lấy tín hiệu. Tần số của "
      "sóng sin tỉ lệ với tốc độ quay (RPM). Bộ điện tử, thực chất là một phần của bộ chỉ thị RPM, "
      "đổi đầu ra sóng sin thành điện áp có đỉnh phẳng. Điện áp này nạp cho tụ điện qua chỉ thị RPM "
      "trong nửa chu kỳ dương. Tụ điện xả trong nửa chu kỳ âm. Đồng hồ chỉ dòng nạp, tỉ lệ với tần "
      "số. Trong loại hệ này, số đọc dòng ở thang đo đầy đủ xấp xỉ 300 miliampe. Hệ được thể hiện "
      "trong Hình 2.45 và đã được dùng rất thành công để đo tốc độ tới 8000 RPM.",
      "When the magnet rotates along with the shaft, it generates a sine wave voltage in the "
      "pick-up coil. The frequency of the sine wave is proportional to the speed of rotation (RPM). "
      "The electronic unit, which is in fact a part of the RPM indicator unit, converts the sine "
      "wave output into a flat-topped voltage. This voltage charges the capacitor through the RPM "
      "indicator during the positive half cycle. The capacitor discharges during the negative half "
      "cycle. The meter indicates the charging current, which is proportional to the frequency. In "
      "this type of system the full-scale current reading is nearly 300 milliamperes. The system "
      "has been shown in Figure 2.45 and has been applied to measure speed upto 8000 RPM very "
      "successfully.")
    FIG(b, 45, F.fig_f45(), lang)

    P(b, lang,
      "Hệ này đã được lắp đặt trên máy nén ly tâm dẫn động bằng tua-bin dùng để nén nitơ tại Nhà máy "
      "Phân bón Sindri và đã chạy liên tục trong suốt 26 năm, chỉ cần bảo trì nhỏ trong các đợt đại "
      "tu hằng năm.",
      "This system has been installed on turbine-driven centrifugal compressor for nitrogen "
      "compression in Sindri Fertilizer Plant and has worked uninterru-ptively for a period of 26 "
      "years with minor maintenance works during annual overhauling.")

    P(b, lang,
      "Khi tốc độ đặc biệt cao (11000 RPM trở lên, tới 15000), như trường hợp máy nén hỗn hợp tổng "
      "hợp (gồm 3 phần hydrogen và 1 phần nitơ) trong cùng nhà máy, một bố trí khác đã được áp dụng "
      "rất thành công. Một bánh răng cực với số răng cố định được nối cơ khí vào trục chính. Tỉ số "
      "truyền, là tỉ số giữa số răng trên bánh răng cực và số răng trên trục chính, trở thành hệ số "
      "nhân của chỉ thị RPM.",
      "When the speed is exceptionally high (11000 RPM or more upto 15000), as is the case with "
      "synthesis mixture (consisting of 3 parts of hydrogen and 1 part of nitrogen) compressor in "
      "the same plant, another arrangement has been applied very successfully. A pole wheel with "
      "fixed number of gear teeth is connected mechanically to the main shaft. The gear ratio, "
      "which is the ratio of number of teeth on pole wheel to the number of teeth on the main shaft "
      "becomes the multiplying factor of the RPM indicator.")

    P(b, lang,
      "Khi bánh răng cực quay trước bộ phát Ferrostate (bộ chuyển đổi tốc độ), đầu ra của mạch phụ "
      "cấp một điện áp xoay chiều. Mỗi chu kỳ của điện áp xoay chiều này tương ứng với việc một cực "
      "của bánh răng đi qua đầu lấy tín hiệu của bộ chuyển đổi.",
      "When the pole wheel rotates in front of the ferrostate transmitter (speed transducer), the "
      "output of the supplementary circuit shall supply an A.C. voltage. Each cycle of this A.C. "
      "voltage shall correspond to the passing of one pole of the pole wheel before the transducer "
      "pick-up.")

    P(b, lang,
      "Độ lớn của điện áp truyền đi phụ thuộc vào khoảng cách d₀, kích thước bánh răng cực, nhiệt độ "
      "môi trường và hằng số mạch. Do đó, độ lớn của điện áp truyền đi Vg, tỉ lệ với khoảng cách khe "
      "hở d₀, được cho bởi:",
      "The magnitude of the transmitted voltage depends on the distance do; pole wheel size, "
      "ambient temperature and circuit constant. Thus, the magnitude of transmitted voltage Vg, "
      "which is proportional to the gap distance do shall be given by:")
    E(b, lang, "Vg = K/d₀", "Vg = K/d₀")
    FIG(b, 46, F.fig_f46(), lang)
    FIG(b, 47, F.fig_f47(), lang)
    NOTE(b, lang,
      "Giá trị thông thường của d₀ ban đầu là 0,4 milimet.",
      "The usual value of do is 0.4 millimetre initially.")

    P(b, lang,
      "trong đó K là hằng số tỉ lệ và phụ thuộc vào kích thước bánh răng cực, nhiệt độ môi trường và "
      "hằng số mạch. Hình 2.46 cho thấy sơ đồ nguyên lý của hệ, trong khi Hình 2.47 cho thấy điện áp "
      "đầu ra do mạch điện tử phụ tạo ra theo khoảng cách khe hở d₀ (milimet). Hệ này cũng đã chạy "
      "tốt trong suốt 26 năm qua, chỉ với những sửa đổi nhỏ.",
      "where K is constant of proportionality and depends upon the pole wheel size, ambient "
      "temperature and circuit constant. Figure 2.46 shows the schematic view of the system whereas "
      "Figure 2.47 shows the output voltage produced by the supplementary electronic circuit with "
      "respect to gap distance d0 (millimetre). This system has also been running successfully for "
      "the last 26 years with minor modifications only.")

    # -------------------------------------------- Stroboscope/Strobometer
    H(b, lang, "Stroboscope/Strobometer (đèn nháy đo tốc độ)",
      "Stroboscope/Strobometer", level=4)

    P(b, lang,
      "Strobometer là một thiết bị khác để đo tốc độ của một thiết bị quay. Trong phương pháp này, "
      "không bộ phận nào của strobometer tiếp xúc trực tiếp với thiết bị chính. Thiết bị gồm một "
      "nguồn sáng nháy có tần số thay đổi. Để đo tốc độ của thiết bị quay, ánh sáng trước hết được "
      "chiếu tới một điểm xác định nằm trên thiết bị. Nếu tần số nháy thấp hơn một chút so với tốc "
      "độ quay của thiết bị chính, thiết bị sẽ có vẻ quay chậm theo cùng chiều. Nhưng nếu tần số "
      "nháy cao hơn một chút, thiết bị sẽ có vẻ quay chậm theo chiều ngược lại.",
      "Strobometer is yet another device to measure the speed of a rotating equipment. In this "
      "method no part of the strobometer comes into the direct contact of the main equipment. This "
      "consist of a flash light source of variable frequency. For measuring the speed of the "
      "rotating equipment, light is primarily focused on to a specific point located at the "
      "equipment. If the focusing rate is slightly less than the rotational speed of the main "
      "equipment, the equipment shall appear to be rotating slowly in the same direction. But if "
      "the flashing rate is slightly less, the same shall appear to be rotating slowly in the "
      "opposite direction.")

    P(b, lang,
      "Khi tần số nháy khớp với tốc độ quay của thiết bị, thiết bị sẽ có vẻ đứng yên. Tại thời điểm "
      "đó, giá trị tốc độ quay bằng giá trị tần số. Do đó, số chu kỳ trên giây tương đương với số "
      "vòng quay trên giây.",
      "Now when the flashing rate matches with the speed of rotation of the equipment, the "
      "equipment shall appear to be standstill. At this point of manoeuvring, the value of rotational "
      "speed shall be equal to the value of frequency. Hence, the number of cycles per second shall "
      "be equivalent to the number of revolutions per second.")

    P(b, lang,
      "Thiết bị hoặc trục quay đang xét có một số điểm (gọi là n) được đánh dấu trên bề mặt. Nếu tần "
      "số nháy là F mỗi phút, thì bước của điểm P được cho bởi P = πD/n, với D là đường kính của "
      "trục.",
      "The equipment or rotating shaft under consideration shall have a number of points (say n) "
      "marked on its surface. If the flashing speed is F per minute, then pitch of the point P "
      "shall be given by P = πD/n (D is diameter of the shaft),")

    P(b, lang,
      "Tương tự, quãng đường mà trục chính đi được trong hai lần nháy liên tiếp bằng πDN/F, với N là "
      "tốc độ của thiết bị chính. Vì quãng đường này bằng bước của điểm, ta có πDN/F = πD/n, hay N "
      "tỉ lệ thuận với F khi n cố định:",
      "In the same way, the distance covered by the main shaft during two successive flashes equals "
      "πDN/F (N is speed of the main equipment). Now since this equals to the pitch and hence: "
      "πDN/F = πD/n or N is proportional to F (where n is fixed)")
    E(b, lang, "N ∝ F (với n cố định)", "N ∝ F (where n is fixed)", num="2.10")

    P(b, lang,
      "Bề ngoài của strobometer được thể hiện trong Hình 2.48. Bên trong thiết bị chứa hệ thống "
      "nạp/xả của ống khí kết hợp với một bộ dao động tạo ra các chùm sáng nháy đều đặn. Một thang "
      "đo đã hiệu chuẩn đặt ở phía trên thiết bị đọc trực tiếp tốc độ theo RPM. Một cơ cấu chỉnh tay "
      "đặt tần số của tốc độ nháy bằng với tốc độ quay của trục chính hoặc bất cứ tốc độ nào.",
      "The outer view of a strobometer has been shown in Figure 2.48. The inside of the equipment "
      "contains a gas tube charging/discharging system in combination with an oscillator that "
      "creates systematic flashes of light. A calibrated scale located on the top of the equipment "
      "reads speed in RPM directly. A manual adjustment device sets the frequency of the flashing "
      "speed equal to the speed of rotation of the main shaft or whatever it may be.")
    FIG(b, 48, F.fig_f48(), lang)

    P(b, lang,
      "Những ưu điểm chính của strobometer là tính đơn giản và là bố trí tốt nhất để kiểm tra nhanh "
      "tốc độ của một máy. Vì không cần bất cứ bộ phận gắn thêm nào, đây là lựa chọn tốt để đo tốc "
      "độ của một thiết bị không thể tiếp cận.",
      "Main advantages of a strobometer are its simplicity and the best arrangement for "
      "spot-checking of speed of a machine. Since it does not need any attachment, this is a good "
      "option to measure the speed of an equipment which is inaccessible.")

    P(b, lang,
      "Nhược điểm phát sinh từ hạn chế cố hữu của bộ dao động tần số thay đổi, vốn không phải lúc nào "
      "cũng cung cấp được tần số cố định.",
      "Disadvantages are imposed due to inherent limitation of variable frequency oscillator, which "
      "cannot always deliver fixed frequency.")

    return "".join(b)
