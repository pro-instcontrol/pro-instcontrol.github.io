# -*- coding: utf-8 -*-
"""Chapter 4, "Telemetry", section 4.2 "Cable Telemetry" start (EN/VI bilingual).

Source: Janardan Prasad, M. N. Jayaswal and Vishnu Priye, *Instrumentation and
Process Control* (I.K. International, 2019), PDF pp. 220-224, printed pp.
208-212, decoded text lines 8307-8514.  Covered here are the voltage-versus-
current choice, the intrinsically safe zener barrier, normal-mode and common-
mode noise, and UTP and STP twisted-pair construction.  The three source
figures (4.3-4.5) are redrawn as vectors in the `ipcfig4_a` supplier module
and placed where the text refers to them.  Units use literal Unicode.
"""

import ipcfig4 as F
from ipc_ch04_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ---------------------------------------------------------------- 4.2
    H(b, lang,
      "4.2 Đo từ xa bằng cáp (hệ thống đường dây cố định)",
      "4.2 Cable Telemetry (Landline System)")

    P(b, lang,
      "Như ta có thể hiểu, dạng đơn giản nhất của đo từ xa trong tín hiệu điện "
      "là dạng truyền qua cáp trực tiếp. Trong hệ thống này, các loại cáp tín "
      "hiệu hoặc cáp điều khiển khác nhau được sử dụng. Các loại cáp được dùng "
      "gồm:",
      "As we can understand the simplest form of telemetry in the electrical "
      "signalling is of direct cable transmission type. In this system "
      "different types of signal cable or control cable are used. The cables "
      "used are of the following types:")

    L(b, lang,
      ["Dây dẫn đồng nhiều lõi (tiết diện ≤ 1,5 mm²)",
       "Cáp tín hiệu xoắn đôi",
       "Cáp đồng trục",
       "Cáp sợi quang"],
      ["Multicore copper conductor ( ≤ 1.5 mm² cross-section)",
       "Twisted pair signal cable",
       "Coaxial cable",
       "Fibre optic cable"],
      ordered=True)

    # ------------------------------------------------------------ 4.2 (i)
    H(b, lang, "(i) Dây dẫn đồng nhiều lõi", "(i) Multicore copper conductor", level=3)

    P(b, lang,
      "Cáp đồng nhiều lõi có thể có số lõi từ 2 đến 19, hoặc thậm chí nhiều "
      "hơn, được bó lại với nhau một cách có hệ thống. Khi chỉ quan tâm đến "
      "một biến tín hiệu, cáp hai lõi là đủ; còn với nhiều hơn một biến thì "
      "cần thêm nhiều đôi dây. Thông thường cáp được bọc PVC với lớp cách "
      "điện mỏng vì mức điện áp tín hiệu rất thấp. Đôi khi cáp cũng có thể "
      "được bọc giáp, nhưng chỉ vì lý do cơ học. Cần bọc giáp khi đường đi "
      "của cáp nằm ở những khu vực có nguy cơ hư hỏng bên trong nhà máy. Cáp "
      "dùng cho đường đi ngầm cần có lớp phủ PVC dày hơn để tăng tuổi thọ, "
      "ngoài việc bọc giáp.",
      "Multicore copper cable can have a number of cores starting from 2 to 19 "
      "or even more put together in systematic manner. When one variable "
      "signalling is concerned, two-core cable is sufficient and for more than "
      "one variable, more pairs become essential. Ordinarily the cable is PVC "
      "coated having smaller value insulation because the signal voltage level "
      "is very low. Sometimes it can be armoured as well for mechanical reasons "
      "only. Armouring is required when the routing of cable is through "
      "damaging areas inside the plant. Cables used for underground routing "
      "are required to have thick outer PVC coating for longer life in "
      "addition to armouring.")

    P(b, lang,
      "Việc chọn một loại cáp đo từ xa cụ thể còn phụ thuộc vào loại tín hiệu "
      "được chọn. Về cơ bản, tín hiệu truyền đi có thể là xoay chiều (A.C.) "
      "cũng như một chiều (D.C.), ở dạng điện áp hoặc dạng dòng điện. Các yếu "
      "tố thiết kế thay đổi theo đó. Trong khi các bộ chuyển đổi hoặc bộ phát "
      "đặt tại hiện trường của nhà máy (tiếp xúc trực tiếp với quá trình "
      "thực), thì các thiết bị thu lại được đặt bên trong phòng điều khiển "
      "trung tâm, nơi luôn được điều hòa không khí tập trung. Đầu ra của bộ "
      "phát dưới dạng tín hiệu điện được truyền về phòng điều khiển, có thể "
      "ở khoảng cách vài trăm mét đến thậm chí vài trăm kilômét. Với những "
      "khoảng cách như vậy, không thể truyền ở nền xoay chiều mức thấp, vì "
      "tín hiệu A.C. mức thấp gần như luôn bị ảnh hưởng bởi các từ trường "
      "tạp. Trong trường hợp D.C. mức thấp, nhiễu can thiệp có thể được loại "
      "bỏ bằng bộ lọc phù hợp. Tín hiệu D.C. mức cao vẫn là lựa chọn tốt hơn.",
      "Selection of a particular type of cable telemetry depends upon the type "
      "of signal selected as well. Basically, the signals for transmission can "
      "be of A.C. as well as D.C. type in either voltage form or current form. "
      "Design considerations change accordingly whereas transducers/transmitters "
      "are located in the plant field (in contact with the real process), the "
      "receiver instruments are located inside a central control room, which "
      "happens to be invariably centrally air-conditioned. The transmiter "
      "output in the form of electrical signal is transmitted to the control "
      "room, which can be in the range of a few hundreds of metres away to even "
      "a few hundreds of kilometres away. For such distances, transmission "
      "cannot be done on low level A.C. base because low-level A.C. signals are "
      "almost always affected by stray magnetic fields. In case of low-level "
      "D.C., the interfering noise signal can be removed by suitable filters. "
      "The high-level D.C. signal is still the better choice.")

    P(b, lang,
      "Trong hệ thống tín hiệu A.C., dịch pha là vấn đề thường gặp. Việc bù "
      "dịch pha trong hệ thống thiết bị đòi hỏi mạch phức tạp, làm cho toàn "
      "bộ hệ thống trở nên đắt đỏ hơn, trong khi ở hệ thống tín hiệu D.C. thì "
      "hoàn toàn không phải xem xét đến vấn đề này.",
      "In A.C. signalling system, phase shift is a common problem. Compensation "
      "for phase shift in instrumentation system requires complicated circuitry "
      "making the entire system altogether more expensive whereas in D.C. "
      "signalling system, there is no such consideration at all.")

    P(b, lang,
      "Trong hệ thống tín hiệu D.C., khuếch đại D.C. khá phức tạp và cho kết "
      "quả không mấy thỏa mãn. Ngược lại, khuếch đại tín hiệu A.C. thì đơn "
      "giản và cho kết quả rất thỏa mãn.",
      "In D.C. signalling system, D.C. amplification is quite complicated and "
      "not so satisfactory result is obtained. A.C. signal amplification, on "
      "the other hand, is simple and quite satisfactory result is obtained.")

    P(b, lang,
      "Các tín hiệu dùng để vận hành bộ định vị van điện-khí nén trong các "
      "vòng điều khiển quá trình cần được chuyển thành lực. Điều này có thể "
      "thực hiện bằng cách cho dòng D.C. chạy trực tiếp qua một cuộn dây treo "
      "trong từ trường. Trong hệ thống tín hiệu A.C., trước hết phải chỉnh "
      "lưu dòng A.C.",
      "The signals, which are used for operation of electro-pneumatic valve "
      "positioner in the process control loops, the signals are required to be "
      "converted into force, which can be done by directly passing a D.C. "
      "through a coil suspended in a magnetic field. In case of A.C. signal "
      "system, the A.C. has to be rectified first.")

    P(b, lang,
      "Trong các ngành công nghiệp chế biến, hầu hết mọi vị trí lắp đặt thiết "
      "bị đều là khu vực nguy hiểm. Vì vậy, tín hiệu D.C. mức năng lượng thấp "
      "được chọn để sử dụng trong những môi trường như vậy. Việc lựa chọn "
      "này giúp giảm thiểu năng lượng tích lũy trong bầu khí quyển dễ nổ, làm "
      "cho hệ thống trở nên an toàn nội tại. Hệ thống an toàn nội tại là hệ "
      "thống mà mức năng lượng cần để đốt cháy hỗn hợp dễ nổ thấp hơn rất "
      "nhiều so với mức cần thiết để gây nổ. Nhờ đó, khả năng xảy ra nổ được "
      "loại trừ hoàn toàn.",
      "In process industries, almost all locations of instrument installations "
      "are hazardous. Therefore, low energy level D.C. signals are selected "
      "for use in such environments. Selection of this signal minimizes the "
      "stored energy in the explosive atmosphere and thus making the system "
      "intrinsically safe. An intrinsically safe system is that system where "
      "the energy level for igniting the explosive mixture is very less than "
      "is required to initiate the explosions. Hence, the possibility of "
      "explosion is completely removed.")

    P(b, lang,
      "Tuy nhiên, vì các thiết bị hiện trường được nối với phòng điều khiển "
      "bằng cáp đồng và hệ thống cấp nguồn thông thường (110 V D.C. hoặc 110 "
      "V A.C.) có mức cao hơn, nên việc nối nhầm các nguồn này vào thiết bị "
      "hiện trường có thể đưa điện áp cao tới thiết bị và gây nổ bất ngờ. "
      "Tình huống ngoài ý muốn này được ngăn ngừa hiệu quả bằng cách đặt các "
      "rào an toàn điện tử giữa dây dẫn hiện trường và dây dẫn phòng điều "
      "khiển. Theo cách bố trí này, mọi cáp đi từ phòng điều khiển đến thiết "
      "bị hiện trường đều phải đi qua một rào riêng biệt. Tương tự, mọi cáp "
      "mang tín hiệu từ phía hiện trường đều phải đi qua rào trước khi vào "
      "thiết bị trong phòng điều khiển.",
      "But since the field instruments are connected to control room through "
      "copper cable and the normal power supply system (110 volt D.C. or 110 "
      "volt A.C.) is of higher order, an accidental connection of these supply "
      "systems to field instruments can send the higher voltage to the field "
      "instruments and thus triggering explosion all of a sudden. Such "
      "accidental situation is successfully prevented by putting electronic "
      "safety barriers in between the field and the control room wiring. In "
      "this arrangement, all the cables going to cater the field instruments "
      "from the control room are made to pass through individual barrier. In "
      "the same way, all the signal carrying cables coming from the field side "
      "are made to pass through barrier before entering the control room "
      "instruments.")

    P(b, lang,
      "Chức năng của các rào này là cách ly hệ thống này khỏi hệ thống kia "
      "bằng cách ngắt kết nối vật lý, để không có điện áp cao nào có thể "
      "truyền tới thiết bị hiện trường trong bất kỳ tình huống nào.",
      "The function of these barriers are to isolate one system from the other "
      "by physical disconnection so that no higher voltages can go to field "
      "instruments during any eventuality.")

    P(b, lang,
      "Một rào an toàn điện tử gọi là rào zener đôi khi cũng được thể hiện "
      "như trong Hình 4.3. Đây là thiết bị thụ động, cho tín hiệu đi từ đầu "
      "này sang đầu kia mà không làm suy giảm cường độ tín hiệu. Rào gồm ba "
      "điện trở và hai đi-ốt zener được nối như sơ đồ. Các điện trở hạn dòng, "
      "còn các zener hạn áp. Chỉ dùng một zener là đủ cho hoạt động của rào, "
      "nhưng người ta dùng thêm một zener nữa để đạt dự phòng 100%, nghĩa là "
      "khi một zener hỏng ngoài ý muốn thì zener còn lại vẫn bảo vệ. Việc "
      "dùng cầu chì có thông số chính xác (được tính toán phù hợp) giúp rào "
      "trở nên kinh tế hơn. Dòng định mức của cầu chì thấp hơn của rào, để "
      "cầu chì sẽ đứt trước khi zener bị hư hỏng và mất tác dụng. Cách bố trí "
      "như vậy cũng tăng tuổi thọ của rào zener và tránh phải thay thế thường "
      "xuyên. Một cầu chì (cầu chì thủy tinh) rẻ hơn nhiều so với một rào.",
      "An electronic safety barrier called zener barrier also sometimes has "
      "been shown in Figure 4.3. This is a passive device and allows the signal "
      "to pass from one end to the other without any loss of signal strength. "
      "The barrier consist of three resistances and two zener diodes connected "
      "as shown in the diagram. The resistances limit the current and the "
      "zeners limit the voltage. Use of only one zener is sufficient for "
      "operation of the barrier but one more zener is used for obtaining 100% "
      "redundancy, i.e. the accidental failure of one can be safeguarded by the "
      "other one. The use of a fuse of accurate specification (to be calculated "
      "appropriately) makes the barrier economical. The current capacity of the "
      "fuse is lower than barrier so that before zener is damaged and becomes "
      "out of service the fuse should blow. By making the arrangement like "
      "this, the life of zener barrier is also increased and frequent "
      "replacement is avoided. A fuse (glass fuse) is much cheaper than a "
      "barrier.")
    FIG(b, 3, F.fig_f03(), lang)

    P(b, lang,
      "Hơn nữa, trong hệ thống đo từ xa bằng cáp, xét đến việc chọn điện áp "
      "hay dòng điện, thì hệ thống đo từ xa điện áp cần mạch có chất lượng "
      "đặc biệt hơn so với hệ thống đo từ xa dòng điện. Yêu cầu về tỷ số tín "
      "hiệu trên nhiễu rất nghiêm ngặt. Vì mức công suất của hệ thống điện áp "
      "trong hầu hết các trường hợp đều thấp, mạch đo từ xa bị ảnh hưởng bởi "
      "nhiễu can thiệp có độ lớn thường tương đương với tín hiệu.",
      "Further in cable telemetry system, as far as choice of voltage or current "
      "are concerned, a voltage telemetry system needs more special quality "
      "circuit than do a current telemetry system. The requirement of "
      "signal-to-noise ratio is stringent. Since the power level of a voltage "
      "system in almost all the cases are low, telemetry circuit is affected by "
      "interfering noise which are of normally same magnitude as the signal.")

    P(b, lang,
      "Mặt khác, các hệ thống đo từ xa dòng điện có khả năng phát triển mức "
      "điện áp cao hơn so với hệ thống điện áp. Nhờ đặc tính này, nhiễu điện "
      "áp do nhiệt, do cảm ứng hoặc các loại khác không ảnh hưởng tới tín "
      "hiệu. Tuy nhiên, dòng rò vốn có của hệ thống có thể gây ra một số sai "
      "số. Hệ thống đo từ xa tín hiệu dòng điện đắt hơn hệ thống đo từ xa tín "
      "hiệu điện áp vì yêu cầu bộ khuếch đại mức cao. Dù vậy, có thể dùng "
      "thiết bị thu giá rẻ với hệ thống tín hiệu dòng điện. Các thiết bị thu "
      "trong trường hợp này có thể nối tiếp với nhau mà không tương tác lẫn "
      "nhau. Đây là một ưu điểm bổ sung của hệ thống đo từ xa dòng điện. "
      "Trong khi đó, ở hệ thống đo từ xa điện áp, việc nối song song các "
      "thiết bị thu đòi hỏi phải xem xét cả trở kháng nguồn.",
      "The current telemetry systems, on the other hand, are capable of "
      "developing higher level voltages than do the voltage system. Due to "
      "this characteristic, there is no effect of thermal or inductive or "
      "other type of noise voltage on the signal. However, the leakage current, "
      "inherent to such system can introduce some error. The current signal "
      "telemetry systems are more expensive than voltage signal telemetry "
      "system because of high-level amplifier requirement. However, a cheap "
      "receiver instrument can be used with current signal telemetry system. "
      "The receiver instruments in this case can be connected in series "
      "without any interaction amongst them. This is an additional advantage "
      "of a current telemetry system. However, in case of voltage telemetry "
      "system, parallel connections of receiver instruments necessitate "
      "consideration of source impe-dance as well.")

    P(b, lang,
      "Hoạt động đúng đắn của các bộ điều khiển điện tử phụ thuộc vào hoạt "
      "động đúng đắn của các bộ khuếch đại thuật toán, vốn cần tín hiệu ở "
      "dạng điện áp. Điện áp này được tạo ra từ tín hiệu dòng điện bằng cách "
      "cho dòng điện đi qua một điện trở chính xác 62,5 ôm. Tín hiệu D.C. 4 "
      "đến 20 mA tạo ra điện áp trong khoảng 0,25 đến 1,25 V, được đưa tới "
      "các bộ điều khiển điện tử.",
      "Proper functioning of electronic controllers depend upon proper "
      "operation of operational amplifiers which require a signal in voltage "
      "form. This voltage is developed from the current signal by passing the "
      "current signal across a precision resistor of 62.5 ohms. A 4 to 20 "
      "mAmps. D.C. signal develops voltage in the range of 0.25 volt to 1.25 "
      "volt, which is applied to the electronic controllers.")

    P(b, lang,
      "Như đã thảo luận ở trên, để vận hành bộ định vị van điện-khí nén, tín "
      "hiệu dạng dòng điện là phù hợp nhất, vì nó tạo ra lực cần thiết chỉ "
      "bằng cách đi qua một cuộn dây đặt trong từ trường. Để vận hành với tín "
      "hiệu dạng điện áp, điện trở của cuộn dây cần được giữ không đổi; "
      "tuy nhiên, muốn vậy cần có bố trí bù nhiệt độ.",
      "For operation of electro-pneumatic valve positioner, as discussed "
      "earlier, signal in current form is most suitable because it develops "
      "the required force when simply passed through a coil placed in a "
      "magnetic field. For operation with signal in voltage form, the coil "
      "resistance needs to be kept constant however, for this a temperature "
      "compensation arrangement is needed.")

    P(b, lang,
      "Nếu điện trở của dây dẫn cáp thay đổi trong quá trình truyền tín hiệu, "
      "tín hiệu điện áp cũng bị ảnh hưởng. Mặt khác, nếu tín hiệu ở dạng dòng "
      "điện thì hoàn toàn không bị ảnh hưởng.",
      "If at all the resistance of the cable conductor during signal "
      "transmission varies, voltage signal also gets affected. On the other "
      "hand, if the signal is available in current form there is absolutely no "
      "effect.")

    P(b, lang,
      "Các hệ thống đo từ xa hiện đại xử lý tín hiệu mức thấp và có trở kháng "
      "đầu vào cao. Trong tình huống này, truyền tín hiệu trở nên nhạy cảm "
      "hơn với các nhiễu can thiệp từ bên ngoài, tức là nhiễu.",
      "Modern telemetry systems handle low-level signals and possess high "
      "input impedance. In such situation signal transfer becomes more "
      "sensitive to outside interferences i.e. noise.")

    P(b, lang,
      "Nếu cáp tín hiệu đi qua khu vực có từ trường biến đổi (do cáp nguồn "
      "hoặc máy biến áp cao áp gây ra), một điện áp cảm ứng có thể chồng lên "
      "tín hiệu ban đầu. Hiện tượng này được gọi là nhiễu điện từ. Một hiệu "
      "ứng tương tự cũng xảy ra do hiệu điện thế tạo ra qua tụ điện ghép "
      "nối. Trong trường hợp này, điện áp cảm ứng 50 Hz cũng được chồng lên "
      "tín hiệu và được gọi là nhiễu tĩnh điện. Một dạng nhiễu tĩnh điện khác "
      "phát sinh do sự hiện diện của cáp nhiều lõi, trong đó dòng xoay chiều "
      "trong một đôi dây cảm ứng điện áp nhiễu lên đôi dây kề cận vì ghép "
      "nối điện dung. Dạng nhiễu này cũng được gọi là nhiễu xuyên kênh. Ba "
      "dạng tín hiệu nhiễu này gọi chung là nhiễu chế độ thường; điện áp "
      "nhiễu này cộng vào tín hiệu ban đầu và do đó gây sai số đáng kể. Điện "
      "áp nhiễu như vậy có thể tới 10 mV, vì vậy cần có biện pháp thích hợp "
      "để loại bỏ. Bộ lọc được dùng cho mục đích này. Việc chọn lọc cần "
      "cẩn thận, vì trong khi loại bỏ điện áp nhiễu, bộ lọc cũng có tác động "
      "tiêu cực là làm giảm mức đáp ứng. Do đó cần có sự thỏa hiệp.",
      "If the signal cable is passing through an area where varying magnetic "
      "field (due to power cable or high voltage transformer) is present, an "
      "induced voltage can be superimposed upon the original signal. This is "
      "called electromagnetic noise. A similar effect is expected due to the "
      "potential difference created through the coupling capacitor. In this "
      "case also an induced voltage of 50 Hz is superimposed on the signal and "
      "is called electrostatic noise. Another form of electrostatic noise is "
      "generated due to the presence of multicore cable wherein an alternating "
      "current in one pair induces noise voltage on adjacent pair because of "
      "capacitive coupling. This form of noise is also known as cross talk. "
      "These three forms of noise signals together called normal mode noise, "
      "this noise voltage adds to the original signal and thus contributes "
      "significant error. Such noise voltage can go upto 10 millivolt and "
      "therefore, suitable arrangement is to be made for removal of this. "
      "Filters are used for this purpose. Careful selection of filter is "
      "necessary because while rejecting noise voltage, filters have negative "
      "effect also in the form of reduced response level. Thus, a compromise "
      "is called for.")

    P(b, lang,
      "Một dạng nhiễu điển hình khác, thường được gọi là nhiễu chế độ chung, "
      "phát sinh khi một cực của hệ thống tín hiệu được nối đất và cực kia "
      "được ghép nối điện dung với mạch đo. Một vòng đo lường được nối đất "
      "tại hai điểm có hiệu điện thế cũng có khả năng phát sinh nhiễu chế độ "
      "chung. Dạng nhiễu này có thể đạt tới hơn 5 V (ở 50 Hz) hoặc khoảng "
      "đó. Các thiết bị thu có đầu vào vi sai loại bỏ được loại nhiễu này. "
      "Khi tín hiệu milivôn từ cặp nhiệt điện được gửi qua dây nối dài có "
      "trở kháng khác nhau, nhiễu chế độ chung được chuyển thành nhiễu chế "
      "độ thường. Tuy nhiên, hiện tượng này dễ dàng được loại bỏ bằng cách "
      "nối đất cặp nhiệt điện.",
      "Another typical noise popularly known as common mode noise is produced, "
      "when one terminal of a signal system is grounded and the other one is "
      "coupled to the measurement circuit capacitively. An instrumentation "
      "loop grounded at two points having a potential difference also is "
      "capable of developing common mode noise. This form of noise can reach "
      "upto over 5 volt (at 50 Hz) or so. Receiver instruments having "
      "differential input arrangement eliminates this type of noise. When "
      "millivolt signals from thermocouples are sent through extension wires "
      "having different impedances, the common mode noise is converted to "
      "normal mode. This is, however, eliminated easily by grounding the "
      "thermocouples.")

    P(b, lang,
      "Phần lớn vấn đề nhiễu trong hệ thống đo từ xa bằng cáp là do thiết kế "
      "cáp kém. Cáp tín hiệu xoắn đôi (sẽ thảo luận ở phần sau) là lựa chọn "
      "tuyệt vời để tự động loại bỏ nhiễu ở mức độ cao. Một điểm quan trọng "
      "nữa là cáp nguồn A.C. và cáp tín hiệu D.C. không nên đi chung một "
      "đường. Đi riêng hai loại cáp này sẽ tránh được sự phát sinh nhiễu ở "
      "mức tối đa có thể.",
      "Majority of the noise problem in a cable telemetry system is due to "
      "poor cable design. A twisted pair signal cable (to be discussed next) "
      "is an excellent choice for high degree of noise rejection "
      "automatically. Another important point is that A.C. power and D.C. "
      "signal cable should not pass through the same route. Separate route for "
      "these two different cables shall avoid generation of noise to the "
      "maximum extent possible.")

    P(b, lang,
      "Vì điện cảm và điện dung là những đặc tính tích trữ năng lượng của "
      "cáp, giá trị thực của chúng là yếu tố quan trọng trong quyết định "
      "thiết kế cáp cho mục đích đo từ xa. Giá trị điện cảm và điện dung "
      "tăng lên khi chiều dài cáp tăng. Đồng thời, điện trở của cáp cũng "
      "tăng theo, do đó có thể phần nào bù đắp ảnh hưởng của đặc tính tích "
      "trữ năng lượng của điện cảm. Tương tự, điện trở cách điện giữa hai "
      "dây dẫn giảm khi chiều dài tăng, và vì thế kiểm soát đặc tính tích trữ "
      "năng lượng của điện dung. Một cáp được thiết kế bình thường có thể có "
      "điện dung 0,1 µF cho mỗi kilômét chiều dài cáp. Tương tự, một cáp đồng "
      "trục được thiết kế bình thường (sẽ thảo luận sau) có thể có điện dung "
      "khoảng 50 pF cho mỗi kilômét cáp. Mặt khác, điện cảm có thể thay đổi "
      "trong khoảng 0,6 đến 1,4 mH cho mỗi kilômét đối với cáp điều khiển "
      "thông thường. Đối với cáp có lớp che chắn, tức là cáp đồng trục, giá "
      "trị có thể nằm trong khoảng 0,17 đến 0,61 mH cho mỗi kilômét cáp.",
      "Since inductance and capacitance are energy storing characteristics of "
      "a cable, their actual values constitute important consideration in "
      "cable design decision for telemetry purposes. The values of inductance "
      "and capacitance increase as the length of the cable increases. At the "
      "same time resistance of the cable also increases in the same way and "
      "therefore, can compensate to some extent the effect of energy storing "
      "behaviour of the inductance. In similar way, the insulation resistance "
      "between two conductors decrease as length is increased and thus "
      "controls the energy storing behaviour of the capacitance. A normally "
      "designed cable can have 0.1 microfarad of capacitance per kilometre of "
      "cable length. Similary a normally designed coaxial cable (to be "
      "discussed later) can have about 50 picofarad of capacitance per "
      "kilometre of cable length. Inductance, on the other hand, can vary in "
      "between 0.6 and 1.4 millihenry per kilometre length for ordinary control "
      "cable. For screened cable, i.e. coaxial cable the value can be anything "
      "between 0.17 and 0.61 millihenry per kilometre of cable length.")

    P(b, lang,
      "Trong đo từ xa bằng cáp cho tín hiệu thiết bị, kích thước của mỗi sợi "
      "dây trong cấu trúc nhiều sợi cũng phần lớn được cố định, vào khoảng "
      "0,2 milimét (đường kính). Dòng nóng chảy của loại cáp được chọn này "
      "không vượt quá 3,5 A.",
      "In cable telemetry for instrumentation signal, the size of individual "
      "strand in a multistrand construction is also more or less, fixed and "
      "that comes to be approximately 0.2 millimetre (in diameter). The fusing "
      "current rating of such a selected cable is not more that 3.5 ampere.")

    # ------------------------------------------------------------ 4.2 (ii)
    H(b, lang, "(ii) Cáp tín hiệu xoắn đôi", "(ii) Twisted pair signal cable", level=3)

    P(b, lang,
      "Khi hai dây đồng được cách điện riêng biệt được xoắn lại với nhau theo "
      "hình xoắn ốc, ta có một đôi dây xoắn. Khi nhiều đôi dây như vậy được bó "
      "lại với nhau, người ta dùng một vỏ bảo vệ để gom chúng lại, thuận tiện "
      "cho việc đi dây. Việc xoắn ngăn không cho các dây can nhiễu lẫn nhau, "
      "nhờ đó tín hiệu không bị nhiễu. Truyền tín hiệu cả hai dạng (tương tự "
      "lẫn số) đều có thể thực hiện với đôi dây xoắn. Tuy nhiên, băng thông "
      "phụ thuộc vào tiết diện dây và khoảng cách cần truyền. Băng thông có "
      "thể được định nghĩa là dải tần số (mang tín hiệu) có thể đi qua một "
      "kênh (trong trường hợp này là cáp điều khiển) một cách thoải mái mà "
      "không bị tổn hao.",
      "When two independently insulated copper wires are twisted together in "
      "the shape of a helix, it is known as a twisted pair. When many pairs of "
      "such cable are bunched together, a protective sheath is used for "
      "putting them together for the ease of routing. Twisting prevented from "
      "interfering them with each other and signals thus stay noiseless. Both "
      "(analog as well as digital) types of transmission is possible with "
      "twisted pair. The bandwidth, however, shall depend upon cross-section of "
      "the wire and the distance to be transmitted. Bandwidth can be defined "
      "as range of frequencies (carrying signal) which can pass comfortably "
      "without loss through a channel (in this case, the channel is control "
      "cable).")

    P(b, lang,
      "Cáp tín hiệu xoắn đôi nói chung có hai loại: Đôi dây xoắn không che "
      "chắn (UTP) và Đôi dây xoắn có che chắn (STP). Việc dùng cáp UTP chỉ "
      "hạn chế ở những khu vực hoàn toàn không có khả năng bị nhiễu điện từ "
      "hoặc nhiễu khác, chẳng hạn môi trường văn phòng và những nơi tương "
      "tự. Ngược lại, cáp STP là loại phù hợp nhất cho môi trường công "
      "nghiệp, nơi các nhiễu từ bên ngoài là yếu tố quyết định trong lựa "
      "chọn. Hình 4.4 và Hình 4.5 lần lượt cho thấy hai loại cáp này.",
      "Twisted pair signal cable can be of two varieties, in general, i.e. "
      "Unshielded Twisted Pair (UTP) and Shielded Twisting Pair (STP). Use of "
      "UTP cable is restricted to areas where there is no possibility of "
      "electromagnetic or other interferences at all such as office "
      "environment and other similar locations. The STP cable, on the other "
      "hand, is the most suitable one for the industrial enviroment where the "
      "outside interferences are the deciding factor for selection. Figures "
      "4.4 and 4.5 show these two cables respectively.")
    FIG(b, 4, F.fig_f04(), lang)
    FIG(b, 5, F.fig_f05(), lang)

    P(b, lang,
      "Việc bố trí lớp che chắn trong cáp STP cùng với cách nối chúng qua "
      "đầu nối mạng LAN kiểu có che chắn làm cho cáp STP đắt hơn cáp UTP.",
      "Provision of shielding arrangement in STP and their connection "
      "arrangement through shielded-style LAN (Local Area Network) connector "
      "make the STP more expensive than the UTP.")

    return b
