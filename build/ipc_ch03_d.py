# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III", section 3.2 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 157-168, printed pp. 145-156,
decoded text lines 5877-6410.  This module continues the special
thermocouple discussion (superheater metal and quick-immersion types), then
covers 3.2.1 "Typical Thermocouple Connections", 3.2.2 "Accuracy
Consideration", 3.2.3 "Development of Potentiometric Temperature Recording
System" and the radiation/pyrometry material.  Figures 3.21-3.30 come from
the shared ``ipcfig3`` registry.  Printed equations (3.8)-(3.10) are
reconstructed with standard notation from the page images; the garbled
glyphs for lambda, sigma, beta, T_b and e are restored with their printed
meaning.  The English body keeps source wording quirks, the Vietnamese body
uses the accepted technical meaning.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ------------------------------------------- 3.1.5 (cont.): 3 and 4
    P(b, lang,
      "Kích thước của b tay nắm bằng kim loại dạng chữ nhật thường là 3″ × 2″. "
      "Đầu cong dạng vòng cung chữ nhật được hàn vào bề mặt kim loại của bộ quá "
      "nhiệt sao cho bám chặt lấy bề mặt này. Vì diện tích bề mặt tiếp xúc "
      "khoảng 6 inch vuông là khá lớn nên đáp ứng của phép đo sẽ nhanh hơn. "
      "Đầu đo cặp nhiệt điện dạng chèn, được cách điện bằng khoáng chất, rất "
      "dài, có thể tới 6 mét hoặc hơn nữa (cấu trúc dạng mao dẫn), chiều dài "
      "phụ thuộc vào khoảng cách thực tế giữa điểm đo và vị trí lắp đặt đầu "
      "cặp nhiệt điện (nằm ngoài lò). Việc tăng chiều dài của đầu đo làm cặp "
      "nhiệt điện đắt hơn, nhưng an toàn và tính kinh tế của ống quá nhiệt là "
      "những yêu cầu bắt buộc nên thiết kế tổng thể vẫn trở nên hợp lý về "
      "kinh tế.",
      "The size of the rectangular metallic grip is normally 3″ × 2″. The "
      "rectangular arc shaped tip is welded onto the superheater metal so that "
      "it grips the surface of the metal. Since the area of grip being "
      "approximately 6 square inches is quite large, the response of the "
      "measurement shall be faster. The thermocouple inset which is mineral "
      "insulated is very long, may be 6 metre or even more (capillary-like "
      "construction), the length being dependent upon the actual distance "
      "between the point of measurement and the installation point where the "
      "thermocouple head shall be installed (out of the furnace). The increased "
      "length of the thermocouple inset makes the thermocouple costly but the "
      "safety and the economy of the superheater tube are such requirements "
      "that overall design becomes economic.")
    FIG(b, 21, F.fig_f21(), lang)

    H(b, lang, "(4) Cặp nhiệt điện nhúng nhanh",
      "(4) Quick immersion thermocouple", level=4)

    P(b, lang,
      "Nhiệt độ của thép lỏng được đo bằng cặp nhiệt điện nhúng nhanh. Trong "
      "cặp nhiệt điện này, phần tử đo thuộc nhóm platin/rhodi loại R. Cặp "
      "nhiệt điện được bảo vệ bằng vỏ silica dạng thủy tinh. Vỏ này đủ bền để "
      "chịu được ứng suất cơ học và đủ mỏng để có thời gian đáp ứng 15 giây. "
      "Đáng tiếc là mỗi vỏ chỉ dùng cho một lần đo tại chỗ, và lần đo tiếp "
      "theo phải dùng một vỏ mới.",
      "The temperature of liquid steel is measured by quick immersion "
      "thermocouple. In this thermocouple, the element is of R-type from "
      "platinum/rhodium group. The thermocouple is protected by means of "
      "vitreous silica sheathing. The sheath is strong enough to withstand "
      "the mechanical stress and the thickness of the sheath is small enough "
      "to have response time of 15 seconds. It is unfortunate that one sheath "
      "is used for every spot measurement and for next measurement a new "
      "sheath has to be utilized.")

    P(b, lang,
      "Thân của cụm cặp nhiệt điện được làm bằng ống thép. Một đầu của cụm, nơi "
      "đặt đầu cặp nhiệt điện, được uốn cong để dễ nhúng. Phần này được phủ "
      "vật liệu chịu lửa hoặc than chì để bảo vệ thêm cho ống. Vật liệu cách "
      "điện dùng cho mục đích này là sứ nhôm (aluminous porcelain), còn gần "
      "điểm nối nóng dùng alumina. Đầu cặp nhiệt điện và một inch dây dẫn "
      "thêm được để hở không cách điện nhằm tăng tốc độ đáp ứng.",
      "The body of the thermocouple assembly is made of steel tube. One end of "
      "the assembly where the tip of the thermocouple is located is bent over "
      "for easy immersion. This portion is covered with refractory or graphite "
      "material for extra protection for the tube. The thermocouple insulation "
      "used for this purpose is aluminous porcelain and near the hot junction "
      "alumina is used. The tip of the thermocouple and one inch extra wire is "
      "left uninsulated to increase the speed of response.")

    P(b, lang,
      "Cụm cặp nhiệt điện không được có bất kỳ dấu vết dầu hoặc mỡ nào, nếu "
      "không cặp nhiệt điện sẽ hư hỏng ngay khi nhúng vào thép lỏng, thậm chí "
      "trước khi lấy số đo. Đó là do sự có mặt của các vết lưu huỳnh. Phương "
      "pháp này đã đo được nhiệt độ tới 1700 °C trong quá trình luyện thép.",
      "The thermocouple assembly must not possess any trace of oil or grease, "
      "otherwise the thermocouple will be spoiled the moment it is dipped into "
      "the liquid steel before even the measurement is taken. This is because "
      "of the presence of traces of sulphur. This method has been successful "
      "for measurement of temperature upto 1700°C during steel making process.")

    # ------------------------------------------------------------- 3.2.1
    H(b, lang, "3.2.1 Các kết nối điển hình của cặp nhiệt điện",
      "3.2.1 Typical Thermocouple Connections", level=3)

    P(b, lang,
      "Ngoài bốn loại cặp nhiệt điện đặc biệt nêu trên được chế tạo cho những "
      "mục đích riêng, còn có các bài toán đo điển hình khác không đòi hỏi cấu "
      "tạo đặc biệt mà đòi hỏi cách kết nối đặc biệt. Đó là đo nhiệt độ trung "
      "bình và đo nhiệt độ chênh lệch. Loại thứ nhất hữu ích để biết nhiệt độ "
      "tổng thể của một ống dẫn lớn, ví dụ ống dẫn khí cháy vào lò hơi trong "
      "nhà máy hơi, và nhiệt độ khí thải ở cuối đường ống gần ống khói. Loại "
      "thứ hai hữu ích để đo sự chênh lệch nhiệt độ giữa dầu nặng và hơi "
      "nguyên tử hóa trong mạch khởi động của hệ thống đầu đốt và hệ thống "
      "thổi quét trong nhà máy hơi. Hình 3.22 cho thấy cách bố trí để đo "
      "nhiệt độ trung bình.",
      "In addition to the above four types of special thermocouples "
      "constructed for specific purposes, there are other typical measurement "
      "problems which call for not special construction but special "
      "connection. These are measurement of average temperature and "
      "differential temperature. The former is useful for knowing the overall "
      "temperature of a large duct, e.g. combustion air inlet duct in steam "
      "boiler house and final outlet flue gas temperature near the chimney. "
      "The latter is useful for measurement of temperature difference between "
      "heavy oil and the atomizing steam in start-up circuit of burner "
      "atomizing and scavenging system in steam boiler house. Figure 3.22 "
      "shows the arrangement for average measurement.")
    FIG(b, 22, F.fig_f22(), lang)

    P(b, lang,
      "Để đo trung bình, có thể dùng bất kỳ số lượng cặp nhiệt điện nào. Dùng "
      "càng nhiều cặp nhiệt điện thì phép đo càng có tính đại diện. Để đo "
      "chính xác, điện trở của tất cả các cặp nhiệt điện cộng với điện trở "
      "của các mạch dây nối dài phải giống nhau. Vì điện trở của cặp nhiệt "
      "điện thực tế thay đổi theo nhiệt độ và chiều dài dây nối dài cũng thay "
      "đổi, nên ảnh hưởng của những thay đổi này được giảm thiểu bằng cách "
      "dùng điện trở triệt tiêu. Giá trị của điện trở triệt tiêu phải lớn "
      "(khoảng 1500 ôm) so với sự thay đổi điện trở liên quan. Để ngăn dòng "
      "vòng nối đất, không nên nối đất cặp nhiệt điện. Kết nối song song các "
      "cặp nhiệt điện để đo nhiệt độ trung bình có ưu điểm là đặc tính hiệu "
      "chuẩn của thiết bị thu nhận vẫn giống như đối với một cặp nhiệt điện "
      "đơn lẻ.",
      "For average measurement, any number of thermocouples can be used. More "
      "number of thermocouples used, more representative measurement can be "
      "obtained. For accurate measurement, the resistance of all thermocouples "
      "taken together with that of the extension wire circuits should be "
      "identical. Since the resistance of the actual thermocouple shall vary "
      "with temperature and also the lengths of the extension wire, the effect "
      "of these variations are minimized by using swamping resistor. The value "
      "of swamping resistor shall be high (approximately 1500 ohms) with "
      "respect to change in resistance involved. To prevent ground loop current "
      "flow, grounding of thermocouple should be avoided. Parallel connection "
      "of thermocouples for measurement of average temperature is advantageous "
      "since the calibration of receiver instrument is same as that for a "
      "single thermocouple.")

    P(b, lang,
      "Tương tự, hai cặp nhiệt điện có thể được nối như trong Hình 3.23 để đo "
      "nhiệt độ chênh lệch giữa hai quá trình. Một lần nữa, hai cặp nhiệt điện "
      "phải giống hệt nhau về mọi mặt cùng với các dây nối dài (cùng vật "
      "liệu).",
      "Similarly, two thermocouples may be connected as shown in Figure 3.23 "
      "to measure differential temperature between two processes. Again the "
      "two thermocouples must be similar in all respect along with their "
      "extension wires (of same material).")
    FIG(b, 23, F.fig_f23(), lang)

    P(b, lang,
      "Khi hoạt động, sức điện động do hai cặp nhiệt điện phát ra đối kháng "
      "nhau. Trong trạng thái này, nếu nhiệt độ của hai quá trình bằng nhau "
      "thì sức điện động thuần bằng không. Mặt khác, nếu tồn tại nhiệt độ "
      "chênh lệch thì sức điện động phát ra tỷ lệ với nhiệt độ chênh lệch đó.",
      "While in operation, the emf developed by the two thermocouples oppose "
      "each other. In this condition if the temperature of the two processes "
      "is equal, then the net emf developed shall be zero. If, on the other "
      "hand, a differential temperature exists, then the emf developed shall "
      "be proportional to the differential temperature.")

    P(b, lang,
      "Có thể trang bị cho thiết bị chỉ thị nhiệt độ thang đo zero ở giữa nếu "
      "điều kiện công nghệ yêu cầu, nếu không thì thang đo thường là đủ để "
      "hiển thị. Với phép đo này không cần bù điểm nối tham chiếu cho thiết "
      "bị. Ngoài ra cũng không yêu cầu nối đất cặp nhiệt điện. Nhưng điện trở "
      "của cả hai cặp nhiệt điện phải bằng nhau.",
      "The temperature indicator can be provided with center zero scale if "
      "process conditions demand, else a normal scale is sufficient to provide "
      "the indication. For this measurement, there is no need of reference "
      "junction compensation for the instrument. Also grounding of thermocouple "
      "is not required. But the resistance of both the thermocouples should be "
      "same.")

    H(b, lang, "(iii) Nhiệt trở", "(iii) Thermistors", level=4)

    P(b, lang,
      "Như đã thảo luận trước đó, nhiệt trở được chế tạo từ vật liệu bán dẫn "
      "và có cả hệ số nhiệt độ điện trở dương lẫn âm (PTC và NTC). Nhiệt trở "
      "có đặc tính NTC được dùng cho mục đích đo nhiệt độ.",
      "As we have discussed earlier, the thermistors are made of semiconductor "
      "materials and have positive as well as negative temperature coefficient "
      "of resistance (PTC and NTC). Thermistors having NTC behaviour are used "
      "for temperature measurement purposes.")

    P(b, lang,
      "Vì là thiết bị bán dẫn, nó dẫn điện hoàn toàn giống như transistor. Do "
      "đặc tính NTC (điện trở giảm khi nhiệt độ tăng), dòng chảy qua nó tỷ lệ "
      "trực tiếp với nhiệt độ cần đo. Vì hệ số nhiệt độ điện trở của nhiệt trở "
      "lớn hơn nhiều so với phần tử RTD tương ứng nên nó nhạy hơn RTD. Do đó, "
      "những nơi yêu cầu đáp ứng nhanh và đo chính xác, nhiệt trở là lựa chọn "
      "lý tưởng. Giá trị điện trở của nhiệt trở lớn hơn 10.000 ôm, trong khi "
      "của RTD chỉ 100 ôm. Nhưng dải làm việc của nhiệt trở lại quá hẹp vì "
      "quan hệ giữa điện trở và nhiệt độ không tuyến tính. Tuy nhiên, nếu "
      "nhiệt trở được dùng trong dải nhiệt độ làm việc quy định thì nó cho "
      "hiệu năng ổn định và lặp lại được. Đó là lý do nó được dùng trong hệ "
      "thống ngắt tủ lạnh gia đình.",
      "Being a solid state device, it conducts exactly like transistors. "
      "Because of its NTC behaviour (decrease in resistance due to rise in "
      "temperature), the current flow through it is directly proportional to "
      "the temperature being measured. Since the temperature coefficient of "
      "resistance of thermistor is large with respect to its counterpart RTD "
      "element, it is more sensitive than RTD. Therefore, where fast response "
      "and precise measurement are required, thermistors are the ideal "
      "selection. Resistance value of a thermistor is more than 10,000 ohms "
      "but that of RTD is only 100 ohms. But range of operation of thermistor "
      "is too narrow because of its non-linear relationship between resistance "
      "and temperature. However, if the thermistor is applied within its "
      "normally specified range of application then it provides stable and "
      "repeatable performance. That is why, this is used in domestic "
      "refrigerator cut-off system.")

    P(b, lang,
      "Giống như RTD, ở đây không cần cấu tạo ba dây hoặc bốn dây vì giá trị "
      "điện trở danh định của nhiệt trở rất lớn so với điện trở dây dẫn.",
      "As in RTD, there is no need of 3-wire or 4-wire construction system in "
      "this case because the nominal resistance value of thermistor is very "
      "high with respect to lead wire resistance.")

    P(b, lang,
      "Đối với thiết bị đọc kết quả, cần phải tuyến tính hóa vì đặc tính "
      "không tuyến tính của nhiệt trở. Mạch chia điện áp đơn giản trong Hình "
      "3.24 thực hiện việc tuyến tính hóa quan hệ giữa điện áp và nhiệt độ. "
      "Có thể thêm nhiều hơn một nhiệt trở vào mạch này để đạt được sự "
      "tuyến tính hóa chính xác hơn.",
      "As far as readout instrument is concerned, linearization is required "
      "to be done because of non-linear behaviour of thermistor. The simplest "
      "voltage divider circuit shown in Figure 3.24 does this job of "
      "linearising the voltage vs. temperature relationship. More than one "
      "thermistor can be added to this circuit to achieve more accurate "
      "linearization.")
    FIG(b, 24, F.fig_f24(), lang)

    H(b, lang, "Đặc điểm cấu tạo", "Constructional Features", level=4)

    P(b, lang,
      "Cấu tạo tiêu chuẩn của nhiệt trở có nhiều hình dạng và kích thước "
      "khác nhau, ví dụ dạng hạt, dạng đĩa, dạng vòng đệm và dạng thanh. Các "
      "cấu tạo này cùng với dây dẫn nối kèm được minh họa trong Hình 3.25.",
      "Standard construction of thermistors has different shapes and size e.g. "
      "beads type, discs type, washers type and rods type. These different "
      "constructionalong with their attached leads have been shown in Figure "
      "3.25.")
    FIG(b, 25, F.fig_f25(), lang)

    P(b, lang,
      "Ở cấu tạo dạng hạt, hạt thường được bọc trong vỏ thủy tinh. Ở cấu tạo "
      "dạng đĩa, dây dẫn có thể được chế tạo thêm với các bề mặt mạ kim loại "
      "để tạo thành hệ thống kẹp trượt, hoặc thậm chí có thể hàn vào mạch đo. "
      "Ngược lại, nhiệt trở dạng vòng đệm có lỗ ở giữa nhờ đó có thể lắp bằng "
      "chốt bắt cùng với một số nhiệt trở khác. Để tạo kết nối điện, các bề "
      "mặt tiếp xúc được mạ kim loại như minh họa. Nhiệt trở dạng thanh là "
      "một thanh dài với một cặp dây dẫn gắn theo trục hoặc theo phương xuyên "
      "tâm.",
      "In beads type of construction, the bead is usually enclosed in glass "
      "cover. In disc type construction, leads can be fabricated with metal "
      "plated faces as well to make it slide-clipped type of system or even "
      "can be soldered in the measurement circuit. The washer thermistor, on "
      "the other hand, is having center hole and hence can be installed by "
      "means of mounting studs along with a number of other thermistors. For "
      "making electrical connection, the contact faces are metal plated as "
      "shown. A rod thermistor is a long stick-like object with a pair of "
      "leads attached axially or radially.")

    # ------------------------------------------------------------- 3.2.2
    H(b, lang, "3.2.2 Xét đến độ chính xác", "3.2.2 Accuracy Consideration",
      level=3)

    P(b, lang,
      "Vấn đề phổ biến nhất liên quan đến độ chính xác khi đo bằng nhiệt trở "
      "là khả năng thay thế lẫn nhau. Đường cong điện trở theo nhiệt độ của "
      "nhiệt trở phụ thuộc vào thành phần vật liệu. Thành phần vật liệu chế "
      "tạo rất khó kiểm soát, do đó dung sai yêu cầu có thể không duy trì "
      "được. Tuy nhiên, việc lựa chọn sản phẩm đạt yêu cầu từ một lô sản xuất "
      "được thực hiện cẩn thận, nhờ đó có thể đạt được dung sai trong khoảng "
      "0,1 °C trên một dải nhiệt độ quy định.",
      "The most common problem associated with accuracy of measurement by "
      "thermistor is its interchangeability. The resistance vs. temperature "
      "curve of thermistor is dependant upon material composition. The material "
      "of construction is practically difficult to monitor and therefore, "
      "required tolerance may not be maintained. However, selection of "
      "required product from a manufactured batch is done carefully and "
      "thereby a tolerance within 0.1 °C over a particular specified range of "
      "temperature can be achieved.")

    P(b, lang,
      "Đường cong dung sai cho thấy dải ổn định từ 20 °C đến 85 °C. Đường cong "
      "này được thể hiện trong Hình 3.26.",
      "The tolerance curve indicates a stable range of 20°C to 85°C. The curve "
      "has been shown in Figure 3.26.")
    FIG(b, 26, F.fig_f26(), lang)

    P(b, lang,
      "Một vấn đề khác gặp phải trong hệ thống đo bằng nhiệt trở là tự gia "
      "nhiệt. Vấn đề gia nhiệt trong trường hợp này lớn hơn so với hệ thống "
      "đo RTD vì giá trị điện trở cao. Để khắc phục, điện áp áp lên nhiệt trở "
      "phải thấp.",
      "Another problem encountered in thermistor system of measurement is due "
      "to self-heating. The heating problem in this case is more than is "
      "encountered in case of RTD measurement system because of high resistance "
      "value. To counter this the voltage applied to thermistor should be low.")

    P(b, lang,
      "Nhiễm bẩn bề mặt nhiệt trở cũng ảnh hưởng đến độ chính xác do tạo ra "
      "hiệu ứng phân nhánh. Nếu một số hạt nhỏ của chip nhiệt trở bị mất do "
      "hư hỏng cơ học thì điện trở thay đổi, làm ảnh hưởng đến độ chính xác "
      "của phép đo.",
      "Surface contamination of thermistor also affects accuracy by creating "
      "shunting effect. If some small particles from the thermistor chip are "
      "lost due to physical damage, the resistance gets changed thereby "
      "affecting the accuracy of measurement.")

    P(b, lang,
      "Hàn dây nối dài vào dây dẫn của nhiệt trở có thể tạo ra sai số. Nếu "
      "vật liệu hàn khuếch tán vào dây dẫn thì có thể tạo ra hiệu ứng cặp "
      "nhiệt điện, sinh ra sức điện động nhiệt và do đó gây sai số đo. Vì vậy, "
      "mối hàn phải không bị ảnh hưởng bởi nhiệt độ.",
      "Soldering of extension wire to thermistor lead wire can create error. "
      "If solder material gets diffused into the lead, then it can create "
      "thermocouple effect resulting in production of thermal emf and hence "
      "measurement error. Hence, the soldering should be thermally immune.")

    # ------------------------------------------------------------- 3.2.3
    H(b, lang,
      "3.2.3 Phát triển hệ thống ghi nhiệt độ kiểu đo thế",
      "3.2.3 Development of Potentiometric Temperature Recording System",
      level=3)

    P(b, lang,
      "Hệ thống ghi nhiệt độ liên tục đã trải qua nhiều giai đoạn phát "
      "triển. Trước đây người ta dùng các hệ thống ghi kiểu cơ cấu kim chỉ "
      "thị hoặc cuộn dây chuyển động, hoạt động theo nguyên lý cơ bản của thiết "
      "bị nam châm vĩnh cửu và cuộn dây chuyển động (PMMC). Các máy ghi này "
      "vẫn còn được dùng ở một số nhà máy công nghệ cũ. Hạn chế của chúng là "
      "trở kháng đầu vào thấp và độ nhạy kém.",
      "Continuous temperature recording system has passed through several "
      "phases of its development. Earlier, deflection or moving coil type of "
      "recording systems were in use which operated on the basic principle of "
      "permanent magnet moving coil (PMMC) instrument. These recorders, "
      "however, are still in use in some of the older process plants. "
      "Limitations of these recorders have been inferior input impedance and "
      "poor sensitivity.")

    P(b, lang,
      "Máy ghi kiểu đo thế về cơ bản là hệ thống cân bằng, giúp nâng cao "
      "hiệu năng tổng thể của hệ thống ghi. Nguyên lý hoạt động cơ bản giống "
      "với chiết áp tự cân bằng. Gần đây đây có lẽ là cách bố trí đa năng nhất "
      "trong lĩnh vực hệ thống đo thế dùng cho nhiệt độ.",
      "Potentiometric recorder which is basically a null type system improves "
      "overall performance of the recording system. Basic operation is similar "
      "to self-balancing potentiometer. Off late this has been probably the "
      "most versatile arrangement in the field of potentiometric measurement "
      "system for temperature.")

    P(b, lang,
      "Trong vài thập kỷ gần đây, hầu hết các hệ thống vừa đo vừa ghi nhiệt độ "
      "đều dùng cách bố trí này vì vận hành đơn giản và đáp ứng nhanh. Sơ đồ "
      "được thể hiện trong Hình 3.27.",
      "For the last few decades, almost all temperature measurement-cum-"
      "recording systems utilizes this arrangement for simplicity of operation "
      "and also fast response. The scheme has been shown in Figure 3.27.")
    FIG(b, 27, F.fig_f27(), lang)

    P(b, lang,
      "Trong hệ thống hở của cặp nhiệt điện, độ lệch của hệ thống "
      "galvanômet là kết quả của điện thế mất cân bằng phát sinh trên dây "
      "trượt của mạch đo thế. Nhưng hệ thống vừa đo vừa ghi nhiệt độ kiểu đo "
      "thế là hệ thống kín. Điện thế mất cân bằng thu được được dùng để tự động "
      "đưa chiết áp về một thiết lập mới nhờ cơ cấu động cơ servo như minh "
      "họa. Tại điểm cân bằng mới, điện thế chưa biết do cặp nhiệt điện cùng "
      "hệ dây trượt tạo ra bằng với điện thế chuẩn áp lên dây trượt.",
      "In an open loop system of thermocouple response, the deflection in "
      "galvanometer system is the result of out of balance potential produced "
      "across the slide-wire of the potentiometric circuit. But the "
      "potentiometric measurement-cum-recording system of temperature is a "
      "closed loop system. The out of balance potential so obtained is "
      "utilized here to balance the potentiometer to a new setting "
      "automatically by means of servomotor mechanism as shown. At the new "
      "balance point, the unknown potential produced by thermocouple-cum-"
      "slidewire system equals the standard potential applied across the "
      "slide-wire.")

    P(b, lang,
      "Hình 3.28 cho thấy chi tiết bên trong của cách bố trí mạch dây trượt "
      "chiết áp. Rất nhiều điện trở đã được dùng trong mạch để bù nhiệt độ môi "
      "trường.",
      "Figure 3.28 shows the internal details of the potentiometer-slide-wire "
      "circuit arrangement. The too many resistances have been used in the "
      "circuit for the sake of Ambient Temperature Compensation.")
    FIG(b, 28, F.fig_f28(), lang)

    P(b, lang,
      "Sự thay đổi nhiệt độ môi trường có hai ảnh hưởng:",
      "The change in ambient temperature has two effects:")
    L(b, lang,
      ["Điện trở của cuộn dây thiết bị sẽ thay đổi.",
       "Nhiệt độ môi trường tăng, tức là nhiệt độ điểm nối lạnh tăng, sẽ làm "
       "giảm sức điện động của cặp nhiệt điện. Sự giảm này bằng với sức điện "
       "động của một cặp nhiệt điện có một điểm nối ở nhiệt độ môi trường và "
       "điểm nối kia ở nhiệt độ mà thiết bị đã được hiệu chuẩn trước đó."],
      ["The resistance of instrument coil will change.",
       "Increase in ambient, i.e. increase in cold junction temperature will "
       "decrease the emf of thermocouple. This decrease will be equal to the "
       "emf of a thermocouple with one junction at ambient and another at "
       "which the instrument have been calibrated previously."],
      ordered=True)

    P(b, lang,
      "Ảnh hưởng thứ nhất được giảm thiểu bằng cách dùng điện trở ổn định "
      "chế tạo từ manganin có độ thay đổi điện trở rất nhỏ theo nhiệt độ. Để "
      "giảm thiểu ảnh hưởng thứ hai, cách làm thông thường là dùng các kỹ "
      "thuật bù nhiệt độ môi trường. Vì vậy, người ta bố trí cộng thêm lượng "
      "sức điện động đã bị giảm. Mạch kết hợp cặp nhiệt điện và dây trượt "
      "(Hình 3.28) có ba điện trở bằng manganin và điện trở thứ tư bằng niken "
      "có hệ số nhiệt độ cao. Điện thế mất cân bằng do thay đổi môi trường "
      "được cộng vào sức điện động của cặp nhiệt điện. Ở đây R2 (điện trở "
      "chỉnh zero), R3 (điện trở chỉnh dải) và R5 làm bằng manganin có hệ số "
      "nhiệt độ nhỏ, còn R4 làm bằng niken có hệ số nhiệt độ cao.",
      "The first effect is minimized by using a ballast resistance made of "
      "manganin having negligible change in resistance with respect to "
      "temperature. To minimize the second effect, the usual practice is to "
      "use ambient temperature compensation techniques. For this, arrangement "
      "is made to add the amount of emf which has been reduced. The "
      "thermocouple slide-wire combination circuit (shown in Figure 3.28) have "
      "three resistances of manganin and fourth resistance of nickel having "
      "high temperature coefficient. The out of balance potential due to "
      "ambient change shall be added to thermocouple emf. Here R2 (zero "
      "adjustment resistance), R3 (span adjustment resistance) and R5 are made "
      "of manganin having small temperature coefficient and R4 is made of "
      "nickel having high temperature coefficient.")

    P(b, lang,
      "Khi nhiệt độ của thiết bị tăng, sức giảm điện áp trên R4 tăng lên. Điểm "
      "X trở nên ít dương hơn so với điểm P, làm cho điểm cân bằng Y dịch về "
      "phía thang đo trên. Điều này có tác dụng như thể một điện thế nhỏ được "
      "cộng vào sức điện động hiện có của cặp nhiệt điện, tạo ra hiệu ứng bù "
      "cho sự tăng nhiệt độ môi trường. Nếu có thể đặt R4 tại chính vị trí "
      "của điểm nối lạnh thực tế của cặp nhiệt điện và quan hệ nhiệt độ - sức "
      "điện động của cặp nhiệt điện là tuyến tính thì hiệu ứng bù này có thể "
      "chính xác hơn.",
      "When the temperature of the instrument increases, the potential drop "
      "across R4 shall increases. The point X shall thus become less positive "
      "with respect to P, driving the point of balance Y towards upper scale. "
      "This has the effect as if a small potential has been added to the "
      "existing emf of the thermocouple, thus creating compensating effect to "
      "the increase in ambient temperature. If the resistance R4 can be put "
      "somehow at the same point where the effective cold junction of the "
      "thermocouple exists and temperature-emf relationship of thermocouple is "
      "linear then this compensating effect can be made more accurate.")

    P(b, lang,
      "Điện trở phân nhánh Rs nối song song qua dây trượt được dùng để đưa "
      "tổng điện trở của mạng về một giá trị phù hợp. Ví dụ, tổng điện trở của "
      "mạng mà mạch trên được vẽ ra là 1400 ôm.",
      "The shunting resistance Rs connected across the slide-wire has been "
      "used to bring the overall resistance of the network to a suitable "
      "value. For instance, the overall resistance of the network for which "
      "the above circuit has been drawn has a value of 1400 ohms.")

    P(b, lang,
      "Đầu ra DC của hệ thống trước hết được chuyển sang AC bằng mạch chuyển "
      "đổi. Tín hiệu AC thu được được khuếch đại qua hai cấp. Ở một số thiết "
      "kế, khuếch đại hai cấp là cần thiết để đáp ứng yêu cầu công suất cao "
      "cho hoạt động của động cơ servo. Tín hiệu đã khuếch đại được đưa vào "
      "cuộn điều khiển của động cơ servo AC. Động cơ servo thay đổi vị trí "
      "dưới tác động của điện áp cuộn điều khiển so với điện áp cuộn tham "
      "chiếu. Động cơ servo được nối cơ học với tiếp điểm trượt chuyển động "
      "trên chiết áp để tìm điểm cân bằng. Điểm cân bằng là điểm mà hai điện "
      "thế bằng nhau chính xác. Khi đạt được điểm cân bằng, chuyển động của "
      "tiếp điểm trượt dừng lại và cơ cấu in được kích hoạt. Cơ cấu in này "
      "đồng bộ với cơ cấu công tắc chọn đối với máy ghi nhiều điểm. Tuy nhiên, "
      "cơ cấu phức tạp như vậy hoàn toàn không cần thiết đối với máy ghi một "
      "điểm.",
      "The D.C. output of the system is first converted to A.C. by the "
      "convertor circuit. The A.C. signal so obtained is amplified in two "
      "stages. Two-stage amplification in some of the designs is required to "
      "meet the high level power requirement for the operation of servomotor. "
      "The amplified signal is applied to the control winding of the A.C. "
      "servomotor. The servomotor changes its position by the action of "
      "control winding voltage with respect to reference winding voltage. The "
      "servomotor is mechanically coupled to the sliding contact which moves "
      "on the potentiometer to find a balance point. The balance point is a "
      "point where two potentials become exactly equal. When the balance point "
      "is achieved, the movement of sliding contact stops and a printing "
      "mechanism is triggered. This printing mechanism is synchronized with "
      "respect to selector switch mechanism for a multipoint temperature "
      "recorder. Such complicated mechanism is, however, not at all required "
      "in a single point temperature recorder.")

    P(b, lang,
      "Công tắc chọn quay quanh trục và chọn một điểm cụ thể, tức là một cặp "
      "nhiệt điện cụ thể, để đo nhiệt độ. Sức điện động do cặp nhiệt điện đó "
      "sinh ra đi qua chu trình đo, khuếch đại và cân bằng như đã mô tả, cuối "
      "cùng kích hoạt cơ cấu in. Cơ cấu in thực hiện nhiều chức năng: in một "
      "dấu chấm là bản ghi của điểm đo nhiệt độ cụ thể và in số thứ tự của "
      "điểm đó theo từng điểm một. Các chức năng khác như ngày, giờ cũng được "
      "tích hợp để in theo chu kỳ, ví dụ sau mỗi giờ.",
      "The selector switch rotates at its axis and selects a particular point, "
      "i.e. a particular thermocouple for measurement of temperature. The emf "
      "produced by the particular thermocouple goes through measurement, "
      "amplification and balancing sequence as described and finally triggers "
      "the printing mechanism. The printing mechanism consists of multi-"
      "function operation that prints a dot which is the record of the "
      "particular measurement point of temperature and it prints the serial "
      "number of the point as well one-by-one. Other function such as date, "
      "time, etc. are also incorporated for printing once in a while say after "
      "every one hour or so.")

    P(b, lang,
      "Giấy ghi là giấy dạng cuộn. Giấy được động cơ kéo giấy dẫn động với tốc "
      "độ cố định. Ngoài ra còn có hai động cơ công suất nhỏ khác. Một là động "
      "cơ chọn điểm, chọn lần lượt từng điểm (mỗi điểm nối với một cặp nhiệt "
      "điện). Động cơ này cũng dẫn động cơ cấu in thông qua các bộ bánh răng. "
      "Động cơ thứ hai là động cơ cân bằng, tức là động cơ servo. Khi một điểm "
      "đã được chọn, điểm thứ hai không được chọn cho đến khi chu trình chọn "
      "đo ghi cho điểm đã chọn hoàn tất.",
      "The paper upon which the recording takes place is a roll type chart. "
      "The chart paper is driven by a chart drive motor at fixed speed. In "
      "addition to this there are two more fractional horse power motors. One "
      "is called selector motor that selects the multipoint (one point "
      "connected to one thermocouple) one-by-one. This motor runs the printing "
      "mechanism as well through different gear combination. The second motor "
      "is the balancing motor, i.e. servomotor. When a particular point has "
      "been selected, the selection of second point is not taken up unless the "
      "selection-cum-measurement-cum-recording cycle for the point already "
      "selected is completed.")

    P(b, lang,
      "Ở một số máy ghi nhiệt độ công nghiệp (ví dụ máy ghi J.N. Marshall kiểu "
      "clear span), động cơ cân bằng hay động cơ servo không phải loại chạy "
      "liên tục. Các máy này dùng động cơ tuyến tính để thực hiện việc cân "
      "bằng. Trong hệ thống này, hai nam châm vĩnh cửu đặt song song nhau được "
      "bố trí giữa một thanh sắt thẳng và một tấm sắt mềm phẳng. Một cuộn dây "
      "gọi là cuộn điều khiển, được cấp điện bằng tín hiệu DC mất cân bằng của "
      "chiết áp, được quấn quanh thanh sắt và có thể chuyển động tuyến tính "
      "dọc theo thanh trong từ trường do cặp nam châm vĩnh cửu tạo ra. Khi tín "
      "hiệu DC từ chiết áp áp lên cuộn điều khiển thì xảy ra chuyển động tuyến "
      "tính, vì thế nó được gọi là động cơ servo tuyến tính. Hướng của chuyển "
      "động tuyến tính được đổi bằng cách đổi cực tính của tín hiệu điều "
      "khiển. Cuộn điều khiển tựa lên dây trượt chống lại tác động của lò xo. "
      "Ưu điểm của động cơ điều khiển này là dễ bảo trì, đáp ứng nhanh hơn và "
      "độ chính xác cao hơn so với động cơ servo thông thường. Hình 3.29 cho "
      "thấy cách bố trí của động cơ tuyến tính.",
      "In some of the industrial temperature recorders (e.g., clear span J.N. "
      "Marshall recorder) the balancing motor/servomotor is not of the "
      "continuous type. They use linear motor for carrying out the balancing "
      "job. In this system two permanent magnets which are fixed parallel to "
      "one another are arranged in between a straight iron rod and a soft iron "
      "flat piece. A coil, which is called control coil and which is energized "
      "by the potentiometer out of balance DC signal is wound around the iron "
      "rod and is free to move linearly along the rod in the magnetic field "
      "created by the pair of permanent magnets. When the D.C. signal from the "
      "potentiometer is applied to this control coil, linear movement results "
      "and that is why it is known as linear servomotor. The direction of this "
      "linear movement is changed by changing the polarity of the control "
      "signal. The control coil rests on the slide-wire against the action of "
      "a spring. Advantages of this control motor is easy maintenance, faster "
      "response and higher accuracy with respect to conventional servomotor. "
      "Figure 3.29 shows the arrangement of a linear motor.")
    FIG(b, 29, F.fig_f29(), lang)

    P(b, lang,
      "Máy ghi nhiệt độ hiện đại (ví dụ hàng của Yokogawa) dùng động cơ servo "
      "DC không chổi than được thiết kế riêng để thực hiện cân bằng. Trong "
      "trường hợp này không cần mạch chuyển đổi vì khuếch đại đo lường hiệu "
      "năng cao khuếch đại trực tiếp tín hiệu của chiết áp.",
      "The modern temperature recorder (e.g., Yokogawa make) uses especially "
      "designed D.C. brushless servomotor for carrying out balancing "
      "operation. In that case there is no need of convertor circuit because "
      "high performance instrumentation amplifier amplifies the potentiometer "
      "signal directly.")

    P(b, lang,
      "Cho các thao tác ghi, người ta dùng nhiều loại bút và mực. Bút nỉ dùng "
      "một lần hoặc bút máy vẽ được dùng trong các máy ghi hiện đại. Chúng "
      "được đặt trong hộp băng sáu màu và được cố chắc trên đầu in di động.",
      "For recording operations, several types of pen and ink sets are used. "
      "Disposable felt pens or plotter pens are used nowadays in modern "
      "recorders. These are placed in a six-colour ribbon cassette and securely "
      "fixed on the moving printing head.")

    H(b, lang, "(c) Phương pháp bức xạ", "(c) Radiation Method", level=4)

    P(b, lang,
      "Bức xạ nhiệt là thuộc tính cơ bản của mọi vật liệu. Đó là một quá trình "
      "liên tục. Quá trình này chỉ ngừng khi vật liệu được đưa đến điều kiện "
      "nhiệt độ tuyệt đối, vì trong điều kiện đó các hạt chứa trong vật liệu "
      "hoàn toàn không chuyển động.",
      "Thermal radiation is a basic property of any material. It is a "
      "continuous process in nature. It ceases only when the material is "
      "brought under absolute temperature condition because in this condition "
      "there is no movement at all of the particles contained in the material.")

    P(b, lang,
      "Phương pháp đo nhiệt độ bằng bức xạ được dùng rất hiệu quả khi môi "
      "trường ăn mòn và mài mòn hoặc khi vật nằm bên trong lò, ví dụ một thỏi "
      "kim loại nóng ở trạng thái nóng chảy. Phương pháp này được áp dụng để đo "
      "nhiệt độ trên điểm vàng, tức là 1063 °C, và các thang được chấp nhận "
      "quốc tế thực chất chỉ dựa trên phần này của dải đo. Thang đo trên "
      "1063 °C dựa trên bức xạ nhìn thấy được (đơn sắc) đến 3900 °C. Biểu "
      "thức sau liên hệ thang đo của bức xạ nhìn thấy được đơn sắc từ 1063 °C "
      "đến 3900 °C.",
      "Radiation method of temperature measurement system is used very "
      "effectively when the medium is corrosive and abrasive or the object is "
      "inside a furnace, e.g. an ingot of hot metal which is in molten state "
      "etc. This method is applied to measure the temperature above the gold "
      "point i.e. 1063°C and internationally accepted scales are in fact based "
      "for this portion of the range only. The scale above that of 1063°C is "
      "based upon visible radiation (monochromatic) upto 3900°C. The following "
      "expression relates scale of measurement of monochromatic visible "
      "radiation from 1063°C to 3900°C.")

    E(b, lang,
      "log_e(I_v/I_b) = (C₂/λ_v)[1/1336 − 1/(T_b + 273)]",
      "log_e(I_v/I_b) = (C₂/λ_v)[1/1336 − 1/(T_b + 273)]", num="3.8")

    P(b, lang,
      "Trong đó I_v là bức xạ nhìn thấy được (đơn sắc) có bước sóng λ_v tính "
      "bằng cm do một vật đen tuyệt đối ở nhiệt độ T_b phát ra, I_b là bức xạ "
      "do vật đen tuyệt đối phát ra tại điểm vàng, và giá trị hằng số C₂ được "
      "giả thiết là 1,4384 cm-độ.",
      "where I_v is the visible radiation (monochromatic) of wavelength λ_v cm "
      "emitted by a black body at temperature T_b, I_b is the radiation "
      "emitted by the black body at gold point and the value of constant C₂ is "
      "assumed to be 1.4384 cm-degree.")

    P(b, lang,
      "Khi một vật được nung nóng, màu của nó thay đổi vì sự phân bố năng lượng "
      "bức xạ giữa các bước sóng khác nhau thay đổi theo nhiệt độ. Ở 500 °C vật "
      "có màu đỏ, à 1100 °C màu cam và trên 1400 °C màu trắng. Ở nhiệt độ này "
      "vật phát ra tất cả các màu trong quang phổ nhìn thấy được. Kỹ thuật đo "
      "bằng pyromet bức xạ dựa trên việc đo năng lượng bức xạ do các vật nóng "
      "phát ra giữa các bước sóng 0,1 micron và 10 micron (1 micron bằng 10⁻³ "
      "mm). Cường độ và bước sóng của bức xạ phụ thuộc vào khả năng phát xạ "
      "và nhiệt độ của vật nóng.",
      "When a body is heated it changes colour because the distribution of "
      "radiation energy amongst different wavelengths changes as the "
      "temperature varies. At temperature 500°C, the body is red, orange at "
      "1100°C and white above 1400°C. At this temperature the body radiates all "
      "colours in the visible spectrum. Radiation pyrometer measurement "
      "techniques are based upon measurement of radiation energy emitted by "
      "hot bodies between the wavelengths 0.1 micron and 10 micron (1 micron "
      "equals 10⁻³ mm.) The intensity and wavelength of the radiation is "
      "dependent upon the emittance and temperature of the hot bodies.")

    P(b, lang,
      "Giống như bước sóng, khả năng phát xạ cũng thay đổi từ vật này sang vật "
      "khác, do đó người ta đã thiết lập một chuẩn làm tham chiếu cho mục đích "
      "hiệu chuẩn các pyromet. Đó là vật đen tuyệt đối, được coi là bộ phát "
      "hoàn hảo vì nó hấp thụ tất cả nhiệt và sau đó phát nhiệt đó lại thành "
      "năng lượng bức xạ. Do đó vật đen tuyệt đối có khả năng hấp thụ bằng đơn "
      "vị và vì thế độ phát xạ của nó cũng bằng đơn vị. Mọi vật khác đều có "
      "khả năng hấp thụ và độ phát xạ nhỏ hơn đơn vị.",
      "Like wavelength, emittance also varies from one body to another, and "
      "therefore, a standard has been devised as reference for calibration "
      "purposes of the pyrometers. This is black body which is considered a "
      "perfect emitter since it absorbs all heat and emits that later on as "
      "radiation energy. Consequently, the black body has absorption strength "
      "as unity and therefore, its emissivity is also unity. All other bodies "
      "have absorption strength as well as emissivity less than unity.")

    P(b, lang,
      "Trong thực tế có thể tạo ra vật đen tuyệt đối bằng một buồng lớn có "
      "nhiệt độ không đổi với một lỗ mở rất nhỏ. Một tia năng lượng bức xạ đi "
      "vào buồng qua lỗ mở sẽ bị phản xạ lại nhiều lần bên trong và khi nó "
      "tiếp cận lại gần lỗ mở thì đã bị hấp thụ hoàn toàn. Vì buồng hoạt động như "
      "một vật đen tuyệt đối nên nó không nóng cũng không lạnh.",
      "A black body can be realized in practice as a large enclosure having a "
      "constant temperature with a very small opening. A ray of radiation "
      "energy entering the enclosure through the opening is reflected back a "
      "number of times inside and by the time it tries to reach near the "
      "opening, it is completely absorbed. Since the enclosure acts as a "
      "black body, it is neither hot nor cold.")

    P(b, lang,
      "Tổng năng lượng E_t do một vật đen tuyệt đối hoàn hảo phát ra mỗi giây "
      "trên mỗi centimet vuông được cho bởi:",
      "The total energy E_t radiated per second per square centimetre by a "
      "perfect black body is given by:")
    E(b, lang, "E_t = σ T_b⁴", "E_t = σ T_b⁴", num="3.9")

    P(b, lang,
      "Trong đó T_b là nhiệt độ tuyệt đối và σ là hằng số Stefan-Boltzmann. "
      "Giá trị của σ là 5,672 × 10⁻¹² oat/cm²·giây·độ⁴.",
      "where T_b is the absolute temperature and σ is the Stefan-Boltzmann "
      "constant. The value of σ is 5.672 × 10⁻¹² watts/cm² sec degree⁴.")

    P(b, lang,
      "Tuy nhiên, đối với một bước sóng cụ thể, năng lượng bức xạ có thể tỷ lệ "
      "với T_b⁵ thay vì T_b⁴, nhưng đối với mọi hệ thống đo thực tế, biểu "
      "thức 3.9 được áp dụng.",
      "However, for a particular wavelength, radiation energy can be "
      "proportional to T_b⁵ instead of T_b⁴, but for all practical measurement "
      "system, the expression 3.9 is applied.")

    H(b, lang, "Hệ thống đo thực tế", "Practical Measurement System", level=4)

    P(b, lang,
      "Hệ thống đo thực tế về cơ bản gồm ba phần:",
      "The practical measurement system consists mainly of three parts:")
    L(b, lang,
      ["Thấu kính cảm biến nhận bức xạ từ vật nóng.",
       "Bộ đầu dò chuyển bức xạ thành tín hiệu điện tương ứng.",
       "Bộ chỉ thị cuối cùng chỉ thị nhiệt độ theo tín hiệu điện."],
      ["(i) Sensing lens which receives the radiation from the hot body.",
       "(ii) Detector unit which converts the radiation into proportional "
       "electrical signal.",
       "(iii) Indicator unit which finally indicates the temperature in terms "
       "of electrical signal."],
      ordered=True)

    P(b, lang,
      "Có tất cả năm loại pyromet hoạt động theo nguyên lý nêu trên. Chúng sẽ "
      "được mô tả lần lượt.",
      "There are altogether five different pyrometers which work on the above "
      "principle. These shall be described one-by-one.")

    H(b, lang, "(i) Pyromet bề mặt Land", "(i) Land surface pyrometer", level=4)

    P(b, lang,
      "Khi vật nóng cần đo nhiệt độ bằng pyromet để hở thì lý thuyết áp dụng "
      "được gọi là lý thuyết pyromet bề mặt Land. Rõ ràng chức năng chính của "
      "phương pháp đo này là hệ số hiệu chỉnh áp dụng do sự khác nhau về độ "
      "phát xạ giữa bề mặt hở và vật đen tuyệt đối hoàn hảo.",
      "When the hot body of which the temperature has to be measured by the "
      "pyrometer is open, the theory applied is called land surface pyrometer "
      "theory. Obviously the main function for this method of measurement is "
      "the correction factor applied due to difference in emissivity of the "
      "open surface and that of the perfect black body.")

    P(b, lang,
      "Bức xạ từ bề mặt nóng được làm cho gần giống bức xạ vật đen tuyệt đối "
      "hơn bằng cách đặt một gương phản xạ lõm lên bề mặt. Nếu hệ số phản xạ "
      "của gương là β thì cường độ bức xạ I_e đi qua lỗ nhỏ trên gương được "
      "cho bởi:",
      "The radiation from the hot surface is made to approximate much more "
      "close to black body radiation by placing a concave reflector on the "
      "surface. If the reflectivity of the reflector is β, then the intensity "
      "of radiation I_e passing through the small opening on the reflector is "
      "given by:")
    E(b, lang,
      "I_e = [e / (1 − β(1 − e))] σ T_b⁴",
      "I_e = [e / (1 − β(1 − e))] σ T_b⁴", num="3.10")

    P(b, lang,
      "Trong đó e là độ phát xạ của bề mặt nóng. Bằng cách áp dụng hệ thống "
      "này, độ phát xạ hiệu dụng của bề mặt nóng tăng gần 60 %, tức là từ 0,6 "
      "lên 0,96.",
      "where e is the emissivity of the hot surface. By applying this system, "
      "effective emissivity of the hot surface is increased by almost 60%, "
      "i.e. from 0.6 to 0.96.")

    H(b, lang, "(ii) Pyromet quang học", "(ii) Optical pyrometer", level=4)

    P(b, lang,
      "Pyromet quang học (còn gọi là pyromet độ sáng) phụ thuộc vào sự điều "
      "chỉnh của con người khi nhìn qua cửa sổ ngắm. Đó là lý do nó được thiết "
      "kế để làm việc trong một dải bước sóng bức xạ rất hẹp (chỉ trong ánh "
      "sáng nhìn thấy được). Một kính lọc quang học được dùng để thu được "
      "bước sóng mong muốn. Pyromet quang học dùng kính lọc đỏ vì kính này "
      "phát qua rất hiệu quả mọi bước sóng trên 0,63 micron và chặn tất cả các "
      "bước sóng nhỏ hơn. Điều này là do độ nhạy của mắt người bắt đầu giảm "
      "trên 0,63 micron bước sóng bức xạ. Vì vậy kính lọc đỏ cùng với mắt "
      "người đóng vai trò như một bộ lọc thông dải (loại quang học) cho bước "
      "sóng bức xạ đi vào thiết bị.",
      "Optical pyrometer (also called brightness pyrometer) is dependent upon "
      "human adjustment as seen by the eyes through the viewing windows. This "
      "is the reason that it is designed to work for a very narrow bandwidth "
      "of radiation wavelength (within visible light only). An optical filter "
      "is used to obtain the desired wavelength. Optical pyrometer uses a red "
      "filter since it radiates all wavelengths above 0.63 micron very "
      "effectively and blocks all the smaller wavelengths. This is because the "
      "sensitivity of human eyes starts decreasing above 0.63 micron "
      "wavelength of radiation. Hence the red filter together with human eye "
      "act as a bandpass filter (optical type) for the wavelength of radiation "
      "that enters the instrument.")

    P(b, lang,
      "Cấu hình cơ bản của một pyromet thực dùng để đo nhiệt độ ngọn lửa bên "
      "trong lò công nghiệp được thể hiện trong Hình 3.30. Thấu kính vật kính "
      "hội tụ bức xạ do vật nóng phát ra lên đèn. Chính cái đèn cũng phát ra "
      "bức xạ, đó là bức xạ tham chiếu. Dòng đèn được cấp bởi mạch đo. Vật nóng "
      "được nhìn qua thấu kính hiển vi và xuất hiện như nền phía sau cái đèn. "
      "Độ sáng của đèn được điều chỉnh bằng cách thay đổi dòng đèn cho đến khi "
      "đèn biến mất trên nền. Trong trạng thái này dòng đèn tỷ lệ với bức xạ do "
      "vật nóng phát ra. Vì dòng đèn đã được hiệu chuẩn theo nhiệt độ của một "
      "vật đen tuyệt đối nên dòng đo được cho biết nhiệt độ của vật nóng.",
      "The basic configuration of a practical pyrometer used to measure the "
      "temperature of flame inside the process boiler has been shown in Figure "
      "3.30. The object lens focuses the radiation emitted by the hot body on "
      "to the lamp. The lamp itself emits radiation which is the reference "
      "radiation. The lamp current is supplied by the measuring circuit. The "
      "hot body is seen through microscopic lens and appears as background "
      "behind the lamp. The brightness of lamp is adjusted by varying the lamp "
      "current until lamp disappears from the background. In this condition "
      "lamp current is proportional to radiation emitted by the hot body. "
      "Since the lamp current has been calibrated against the temperature of "
      "a black body, measured current provides temperature indication of the "
      "hot body.")
    FIG(b, 30, F.fig_f30(), lang)

    P(b, lang,
      "Phiên bản tự động của pyromet bức xạ này dùng một đầu dò quang thay cho "
      "mắt người. Ánh sáng từ vật nóng đi qua thấu kính vật kính và hội tụ lên "
      "một gương (bộ điều chế) dao động nhanh, lần lượt cho bức xạ năng lượng "
      "từ vật nóng và từ đèn đi tới một kính lọc. Kính lọc cho bức xạ năng "
      "lượng có bước sóng chọn lọc từ vật nóng cũng như từ đèn tới đầu dò "
      "quang. Sau khi so sánh hai năng lượng bức xạ, đầu dò quang điều chỉnh "
      "chúng để cân bằng bằng hệ thống cân bằng null. Dòng đèn đã điều chỉnh "
      "cho biết nhiệt độ của vật nóng. Vì dòng đèn được điều chỉnh liên tục "
      "nên cách bố trí này có thể ghi nhiệt độ liên tục của một quá trình. "
      "Pyromet quang học là thiết bị đa năng, độ tin cậy và độ chính xác của nó "
      "đều thỏa mãn.",
      "The automatic version of this radiation pyrometer uses a photodetector "
      "in place of human eye. The light from the hot body enters through object "
      "lens and focuses onto a mirror (modulator) that oscillates at faster "
      "speed and allows the radiation energy from the hot body and the lamp "
      "alternately to a filter. The filter allows radiation energy of selected "
      "wavelength from the hot body as well as lamp the photodetector. The "
      "photodetector after comparing the two radiation energy adjusts these "
      "radiation to equalize by using a null-balance system. The adjusted lamp "
      "current provides temperature indication of the hot body. Since the lamp "
      "current is adjusted continuously, this arrangement can record "
      "temperature continuously of a process. Optical pyrometer is a versatile "
      "instrument. Its performance reliability and accuracy are satisfactory.")

    H(b, lang, "(iii) Pyromet bức xạ toàn phần",
      "(iii) Total radiation pyrometer", level=4)

    P(b, lang,
      "Pyromet bức xạ toàn phần không dành riêng cho một dải bước sóng cụ thể "
      "vì về cơ bản nó không phải là thiết bị quang học chỉ đáp ứng trong dải "
      "nhìn thấy được. Thực tế pyromet bức xạ toàn phần đáp ứng với mọi bước "
      "sóng vì phép đo liên quan đến hiệu ứng gia nhiệt của toàn bộ bức xạ. Do "
      "đó, bất kỳ sự tổn hao bức xạ nào cũng có thể cho kết quả sai. Ví dụ, một "
      "số bức xạ bị lọc bởi các cửa sổ thủy tinh mà bức xạ đi qua đó. Tương "
      "tự, bất kỳ vật cản trên đường đi, chẳng hạn hơi hoặc khói giữa vật nóng "
      "và đầu dò pyromet, có thể gây suy giảm một số bước sóng của bức xạ.",
      "Total radiation pyrometer is not specific for any particular wavelength "
      "range because it is not basically optical instrument that responds only "
      "to a visible range. In fact total radiation pyrometer responds to all "
      "wavelengths because measurement is related to the heating effect of the "
      "total radiation. Hence, any loss of radiation whatsoever can give "
      "erroneous results. For instance some radiations are filtered out by the "
      "glass windows through which the radiations are allowed to pass. Similarly, "
      "any obstructions in the path such as vapours or fumes present in between "
      "the hot body and the pyrometer detector can result in attenuation effect "
      "to certain wavelength of the radiation.")

    P(b, lang,
      "Trong cách bố trí thực tế dùng trong công nghiệp, bức xạ do vật nóng "
      "phát ra đi qua một thấu kính và hội tụ lên một phần tử nhạy nhiệt đóng "
      "vai trò đầu dò. Đầu dò được dùng là một chùm cặp nhiệt, tức "
      "là số lượng cặp nhiệt điện nối với nhau để cộng các sức điện động do từng "
      "cặp nhiệt điện sinh ra. Thiết bị chỉ thị nhiệt độ được nối vào mạch của "
      "chùm cặp nhiệt và chỉ thị nhiệt độ của vật nóng.",
      "In practical arrangement used in the industry, radiation emitted by the "
      "hot body passes through a lens and focuses onto a heat-sensitive "
      "element which works as a detector. The detector used is a thermopile "
      "(It is the number of thermocouples connected together to add-up the emfs "
      "produced by the individual thermocouple.) The temperature indicator is "
      "connected to the thermopile circuit and indicates the temperature of "
      "the hot body.")

    P(b, lang,
      "Trong thiết kế này, đầu dò nhiệt là như nhau nhưng các bộ phận quang "
      "học khác nhau theo từng dải nhiệt độ. Đối với đo nhiệt độ cao dùng thấu "
      "kính thủy tinh, đối với dải nhiệt độ trung bình dùng thấu kính thạch "
      "anh, còn nhiệt độ thấp dùng gương thường. Pyromet bức xạ toàn phần "
      "hoạt động theo định luật Stefan-Boltzmann như đã nêu ở trên.",
      "In this design, thermal detector is the same but optical components are "
      "different for different temperature ranges. For high temperature "
      "measurement, lenses made of glass are used, for medium temperature "
      "ranges, quartz lenses are used and for lower temperature, ordinary "
      "mirrors are used. The total radiation pyrometer works on the "
      "Stefan-Boltzmann law as described earlier.")

    P(b, lang,
      "Sai số do suy giảm bức xạ bởi vật cản như đã mô tả được khắc phục bằng "
      "cách dùng pyromet quang học để hiệu chuẩn pyromet bức xạ toàn phần trong "
      "điều kiện làm việc thực tế.",
      "The error presented due to attenuation of radiation by obstruction as "
      "described above is overcome by using an optical pyrometer for "
      "calibrating the total radiation pyrometer under actual operating "
      "conditions.")

    P(b, lang,
      "Phiên bản Tinsley của pyromet bức xạ toàn phần đo nhiệt độ của các vật "
      "nhỏ chuyển động nhanh, ví dụ nhiệt độ của dải thép hẹp trong nhà máy "
      "thép. Một phiên bản khác gọi là Brown Low Range Radiamatic Unit đo "
      "nhiệt độ bề mặt của vật chuyển động ở dải thấp (50 °C đến 175 °C). Trong "
      "hệ thống này, ảnh của vật được hội tụ qua thấu kính fluor canxi lên một "
      "chùm cặp nhiệt nhạy và nhiệt độ được đo bằng mạch đo thế.",
      "Tinsley version of total radiation pyrometer measures the temperature of "
      "small objects moving at high speed, e.g. temperature of narrow steel "
      "strip in a steel plant. Another version called Brown Low Range "
      "Radiamatic Unit measures surface temperature of a moving object in the "
      "lower range (50°C to 175°C). In this system an image of the object is "
      "focused through calcium fluoride lens into a sensitive thermopile and "
      "the temperature is measured by potentiometric circuit.")

    H(b, lang, "(iv) Pyromet tỷ lệ", "(iv) Ratio pyrometer", level=4)

    P(b, lang,
      "Pyromet tỷ lệ được dùng để đo nhiệt độ bề mặt. Thiết bị dùng đầu dò "
      "photon để đo bức xạ ở hai bước sóng khác nhau trong vùng nhìn thấy "
      "được. Nhiệt độ được suy ra từ tỷ lệ của hai bức xạ đã đo này.",
      "Ratio pyrometer is used for measurement of surface temperature. The "
      "instrument uses a photon detector for measurement of radiation of two "
      "different wavelengths in visible regions. The temperature is inferred "
      "from the ratio of these two measured radiations.")

    P(b, lang,
      "Nguyên lý của pyromet tỷ lệ dựa trên thực tế là bức xạ ở một bước sóng "
      "tăng theo nhiệt độ với tốc độ khác với bức xạ ở bước sóng khác.",
      "The principle of ratio pyrometer is based upon the fact that the "
      "radiation at one wavelength increases with temperature at a different "
      "rate from radiation at another wavelength.")

    P(b, lang,
      "Trong cách bố trí thực tế, hai bước sóng khác nhau của bức xạ được tạo "
      "bởi một bánh xe lọc quay. Bánh xe lọc quay gồm các cửa sổ đỏ và cửa sổ "
      "xanh. Cửa sổ đỏ chỉ cho qua bước sóng đỏ, cửa sổ xanh chỉ cho qua bước "
      "sóng xanh. Khi bánh xe quay, đầu dò lần lượt tiếp xúc với bức xạ bước "
      "sóng đỏ và xanh. Các xung của hai bước sóng thu được được khuếch đại, "
      "tách riêng và so sánh về biên độ. Tỷ lệ thu được tỷ lệ với nhiệt độ của "
      "vật nóng.",
      "In practical arrangement of the system, the two different wavelengths "
      "of radiation are provided by a rotating wheel filter. The rotating "
      "wheel filter consists of red windows and blue windows. Red windows "
      "allow red wavelength and blue windows allow blue wavelength only. As "
      "the rotation continues, the detector is faced with alternate red and "
      "blue wavelength of radiation. The resulting pulse of the two wavelengths "
      "are amplified, separated and compared in amplitude. The ratio so "
      "obtained is proportional to temperature of the hot body.")

    P(b, lang,
      "Các cách bố trí thực tế khác cũng có sẵn trên thị trường nhưng tất cả "
      "đều cùng nguyên lý và đo nhiệt độ với độ chính xác gần như nhau.",
      "Other practical arrangements are also available in the market but all "
      "share the same principle and measure the temperature to almost same "
      "accuracy.")

    H(b, lang, "(v) Pyromet quang điện", "(v) Photoelectric pyrometer", level=4)

    P(b, lang,
      "Pyromet quang điện gồm chủ yếu một tế bào quang điện và một hệ thống "
      "quang học. Tế bào quang điện gồm một đĩa bằng sắt, được phủ một mặt "
      "bằng lớp nhạy sáng selenium.",
      "The photoelectric pyrometer consists of mainly a photocell and an "
      "optical system. The photocell consists of a disc made of iron, coated "
      "on one side with a photosensitive layer of selenium.")

    P(b, lang,
      "Hệ thống quang học gồm một thấu kính. Trong thiết bị hoàn chỉnh, tế bào "
      "quang điện và thấu kính được lắp cùng nhau. Bức xạ từ vật nóng được "
      "hướng qua thấu kính tới tế bào quang điện nhờ các tấm chắn đặt giữa "
      "thấu kính và tế bào. Tế bào quang điện được trang bị một điện trở phân "
      "nhánh thay đổi được. Trong khi lắp đặt, điện trở phân nhánh được chỉnh "
      "để hiệu chỉnh độ phát xạ của bề mặt bức xạ. Dòng do tế bào quang điện "
      "sinh ra tỷ lệ với nhiệt độ của vật nóng.",
      "The optical system consists of a lens. In the complete instrument, the "
      "photocell and the lens are put together. The radiation from the hot body "
      "is directed through lens to the photocell by means of the stops put "
      "between the lens and the photocell. The photocell is provided with a "
      "variable shunt resistance. During installation, the shunt resistance is "
      "adjusted for making correction in the emissivity of the radiating "
      "surface. The current produced by the photocell is proportional to the "
      "temperature of the hot body.")

    P(b, lang,
      "Toàn bộ thiết bị được đặt trong áo nước làm mát. Một ống thép chịu "
      "nhiệt đường kính khoảng 50 mm được đưa ra trước áo nước. Khí nén đã lọc "
      "được đưa qua ống này để tạo đường quang học không có khói và các vật "
      "cản tương tự. Một ống nối dài cũng được lắp trước thấu kính để bảo vệ "
      "thấu kính khỏi dầu và hơi ẩm.",
      "The complete instrument is enclosed in a water jacket. A heat-resistant "
      "steel tube of approximately 50 mm diameter projected before the water "
      "jacket. Filtered and compressed air is passed through this tube that "
      "provides an optical path free from fumes and other similar obstructions. "
      "An extension tube is fitted before the lens as well to protect the lens "
      "from oil and moisture.")

    return b
