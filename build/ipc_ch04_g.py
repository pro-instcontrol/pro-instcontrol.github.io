# -*- coding: utf-8 -*-
"""Chapter 4, "Telemetry", sections 4.6-4.7 plus examples and exercise (EN/VI).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 236-240, printed pp. 224-228, decoded text
lines 8956-9127. Covered here are RF telemetry and sensor networks, telemetry in
the electrical power system (block diagram Figure 4.30), the four worked
Examples 4.1-4.4 with their printed arithmetic, and the 15-question exercise.
Example 4.1 keeps the printed numbers and result in English; the Vietnamese
uses the clearer sign convention. Example 4.4's last arithmetic is printed on
PDF p. 240 and is included here.
"""

import ipcfig4 as F
from ipc_ch04_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ---------------------------------------------------------------- 4.6
    H(b, lang, "4.6 Đo từ xa RF", "4.6 RF Telemetry")

    P(b, lang,
      "Đo từ xa RF, hay đo từ xa tần số vô tuyến, là một dạng đo từ xa không "
      "dây dùng sóng tần số vô tuyến để truyền tín hiệu. Dải tần dùng để truyền "
      "được phân bổ theo các tiêu chuẩn do cơ quan quản lý có thẩm quyền lựa "
      "chọn cho mục đích này.",
      "RF telemetry or radio frequency telemetry is a kind of wireless "
      "telemetry, which uses radio frequency waves for its transmission. "
      "Frequency range for transmission is allocated as per the standards "
      "selected for the purpose by the appropriate regulating authority.")

    P(b, lang,
      "Đặc tính cơ bản của sóng vô tuyến ở tần số thấp là chúng xuyên qua vật "
      "cản rất dễ dàng và đi được quãng đường rất dài không bị gián đoạn, với "
      "cường độ không đổi. Ở tần số cao, sóng trở nên có hướng và vì thế bị "
      "phản xạ ngay khi gặp vật cản. Cần chọn dải tần thích hợp cho việc sử "
      "dụng thực tế, nếu không thì phải dùng các trạm lặp.",
      "The basic characteristic of a radio wave at low frequency is that it "
      "penetrates through obstacles very easily and travels through very long "
      "distances uninterruptedly with equal intensity. But at high frequency "
      "it becomes directional and therefore, gets reflected back wherever it "
      "strikes an obstacle. The range of frequency for practical use is to be "
      "selected accordingly otherwise repeaters have to be used.")

    P(b, lang,
      "Tất cả các kỹ thuật điều chế đã mô tả ở phần trước đều được áp dụng cho "
      "đo từ xa RF. Tuy nhiên, cần hiểu rõ rằng đo từ xa RF chỉ được dùng trong "
      "những trường hợp đã biết chắc rằng việc dùng đo từ xa bằng đường dây "
      "cáp sẽ khó khăn do điều kiện địa lý không thuận lợi của tuyến đường, ví "
      "dụ đại dương, sa mạc, rừng rậm rộng lớn, cao nguyên rộng, v.v.",
      "All forms of modulation techniques described in earlier discussion "
      "shall be applied to the RF telemetry as well. However, it should be "
      "understood clearly that the RF telemetry is applied only in the cases "
      "where it is known that the use of land line telemetry is going to be "
      "difficult because of unfavorable geographical conditions of the route, "
      "e.g. ocean, desert, vast jungle, large plateau, etc.")

    P(b, lang,
      "Ngày nay, những tiến bộ mới nhất trong công nghệ cảm biến công suất "
      "thấp đã tạo ra các cảm biến rất nhỏ, gọi là nút cảm biến. Khi nhiều nút "
      "như vậy được nối với nhau một cách có hệ thống, một mạng cảm biến được "
      "hình thành, có khả năng đo nhiều biến độc lập trong môi trường kín hoặc "
      "hở, từ đó xác định đầy đủ trạng thái của hệ thống trong môi trường đó. "
      "Các hệ thống đo này còn gồm những phần tử mạng cảm biến khác và có khả "
      "năng liên lạc với trạm điều khiển trung tâm qua đo từ xa RF. Trong hệ "
      "thống này, vệ tinh liên lạc đặt ở quỹ đạo địa tĩnh cũng tham gia vào "
      "liên lạc. Hệ thống có thể dùng cho mục đích quân sự để theo dõi sự hiện "
      "diện của quân đội, thiết bị nguy hiểm, đạn dược và các dịch vụ khẩn cấp "
      "khác ở những vị trí khó khăn; cũng dùng cho các phát hiện về môi trường "
      "như theo dõi động vật và chim quý hiếm, báo động cháy rừng và lũ lụt đột "
      "ngột, nghiên cứu chất ô nhiễm trong đất và khí quyển, và cả nghiên cứu "
      "sinh lý con người. Hệ thống này đang dần trở nên phổ biến, cho phép "
      "giám sát ngày càng nhiều tình huống khó khăn một cách dễ dàng. Dù một số "
      "nút cảm biến bị hỏng hoặc ngừng hoạt động, toàn bộ hệ thống vẫn không "
      "bị ảnh hưởng và các tín hiệu đo cần thiết vẫn tiếp tục đến trạm điều "
      "khiển trung tâm để phân tích.",
      "Nowadays, the latest advancement in low power sensor technology has "
      "created tiny sensors, which are called sensor nodes. Several such nodes "
      "when connected together systematically, a sensor network is formed, "
      "which is capable of measuring many independent variables in a closed or "
      "open environment that will completely define the system prevailing in "
      "that particular environment. These measurement systems comprises of "
      "other sensor network elements as well and are capable of communicating "
      "with the central control station through RF telemetry. In this system, "
      "the communication satellite positioned at geostationary orbit also "
      "takes part in the communication. This system can be used for military "
      "purposes to monitor the presence of troops, lethal equipment, "
      "ammunition and other emergency services in difficult locations, also "
      "for environmental findings, e.g. tracking of rare animals and birds, "
      "forest fire and sudden flood alarming situation, soil and atmospheric "
      "pollutants research work and also for human physiological study. This "
      "system is slowly becoming so popular that more and more difficult "
      "situations are being monitored so easily through this system. Even if "
      "some of the sensor nodes have become defective or have gone otherwise "
      "out of order, the overall systems do not get affected and the required "
      "measurement signals continue to reach the central control station for "
      "analysis.")

    # ---------------------------------------------------------------- 4.7
    H(b, lang, "4.7 Đo từ xa trong hệ thống điện",
      "4.7 Telemetry in Electrical Power System")

    P(b, lang,
      "Mạng lưới hệ thống điện gồm các tổ máy phát (GU), trạm biến áp tăng áp "
      "nội bộ (SUS), hệ thống truyền tải điện áp cao (HVTS), các trạm lưới điện "
      "(GS) và cuối cùng là trạm biến áp tiện ích gồm hệ thống giảm áp phân "
      "phối (SDS), như sơ đồ khối trong Hình 4.30.",
      "Electrical power system network comprise generating units (GU) and "
      "in-house step-up substation (SUS), high voltage transmission system "
      "(HVTS), grid stations (GS) and lastly utility substation consisting of "
      "distribution step-down system (SDS) as shown in the block diagram "
      "(Figure 4.30).")

    FIG(b, 30, F.fig_f30(), lang)

    P(b, lang,
      "Mạng lưới điện là xương sống của hệ thống truyền tải và cung cấp điện "
      "của mọi quốc gia. Các tổ máy phát được nối với nhau thông qua các liên "
      "kết của mạng lưới. Nhờ đó, sự gián đoạn của một tổ máy ở bất kỳ khu vực "
      "nào cũng có thể được xử lý bởi một tổ máy đang chạy khác có công suất dư "
      "qua mạng lưới hiện hữu. Ngay cả khi không có công suất dư sẵn có, công "
      "suất đó có thể được phát từ một tổ máy dự phòng nóng nếu được chỉ đạo "
      "phù hợp. Để thực hiện được chức năng đặc thù này cần một hệ thống đo "
      "lường và điều khiển được thiết kế cẩn thận, hoạch định kỹ lưỡng. Đo từ "
      "xa trong hệ thống điện kết nối hệ thống đo lường và điều khiển này với "
      "hệ thống kia trong toàn mạng, nhằm điều khiển hiệu quả việc phát điện, "
      "truyền tải và phân phối.",
      "Grid network is the backbone of electrical power transmission and "
      "supply system of any country. Generating units are interconnected to "
      "one another through grid system interconnect. In this way any "
      "interruption in one of the generating unit in any part of the country "
      "can be well taken care of by another running unit having surplus power "
      "through existing grid network. Even if there is no surplus power "
      "readily available, it can be generated by any hot standby generating "
      "unit if instructed properly. For carrying such typical function a "
      "carefully designed and thoroughly planned instrumentation system is "
      "required. Telemetry in power system connects one instrumentation system "
      "of the entire network to the other for effective control of generation, "
      "transmission and distribution.")

    P(b, lang,
      "May mắn là những thay đổi đột ngột về tải, bất kỳ sự cố nào trong mạng "
      "truyền tải và phân phối, hay ngay cả vấn đề ở tổ máy phát đều được phản "
      "ánh ngay lập tức qua sự thay đổi của điện áp và tần số. Đó là đặc điểm "
      "điển hình của hệ thống điện. Tuy nhiên, đo từ xa còn được dùng để tìm "
      "sự cố thực tế và vị trí của sự cố, cũng như thực hiện hành động khắc "
      "phục tự động cần thiết. Những lần giám sát này cũng có thể tiến hành "
      "thủ công bằng cách truyền tin qua điện thoại giữa các trạm với nhau hoặc "
      "trực tiếp với tổ máy phát. Các đường dây điện thoại cần thiết đôi khi là "
      "đường dây thuê riêng, còn gọi là đường dây nóng. Nhờ truyền tin qua "
      "đường dây nóng, việc giám sát và chia sẻ tải được điều khiển thích hợp "
      "và ngay lập tức.",
      "It is fortunate that sudden load changes, any fault condition in the "
      "transmission and distribution network or even problem in generating "
      "units can be reflected immediately in terms of changes in voltage and "
      "frequency. This is a typical characteristic of electrical power system. "
      "However Telemetry is also used , for finding the actual fault and the "
      "location of fault and for implementing the required automatic corrective "
      "action. These monitorings can be done manually also by suitable "
      "telephone message passing from one station to the other or to the "
      "generating unit directly. The required telephone lines can be leased "
      "lines sometimes called hot lines. By telephone messaging through hot "
      "lines monitoring and load sharing can be controlled properly and "
      "immediately.")

    P(b, lang,
      "Dù việc khắc phục được thực hiện tự động hay thủ công, người ta vẫn dùng "
      "các phương thức truyền dẫn đã mô tả trong chương này hoặc các chương "
      "trước. Ở đây, các tín hiệu đo về cơ bản là điện áp, dòng điện và tần số. "
      "Sự sụt hoặc tăng đột ngột của điện áp do thay đổi ở phía sau, sự giảm "
      "hoặc dòng điện tăng mạnh, hay sự thay đổi tần số được đo bằng thiết bị "
      "phù hợp thông qua máy biến áp dòng (CT) và máy biến áp điện áp (PT) được "
      "lắp đặt cho mục đích này. Các tín hiệu đo này trở thành tín hiệu khởi "
      "động cho cả điều khiển thủ công lẫn tự động. Chúng được truyền đến trạm "
      "điều khiển, từ đó tín hiệu khắc phục cần thiết có thể được khởi động "
      "bằng tay hoặc tự động.",
      "Whether the correction is implemented automatically or manually all "
      "the methods of transmission systems described in this chapter or "
      "earlier are utilized. Here the measurement signals are essentially "
      "voltage, current and frequency. Sudden drop or rise in voltage due to "
      "downstream changes or decrease or heavy rush of current or changes in "
      "frequency are measured by suitable instruments through current and "
      "potential transformers installed for the purpose. These measurement "
      "signals become initiating signals for manual as well as automatic "
      "control. These signals are transmitted to the control station from where "
      "the necessary correction signal can be initiated manually or "
      "automatically.")

    P(b, lang,
      "Hầu hết các dạng điều khiển này áp dụng cho mạng lưới điện thực chất là "
      "thủ công. Có một lý do cụ thể cho lựa chọn điều khiển thủ công: điều "
      "khiển thủ công không can thiệp vào điều khiển của tổ máy phát. Vì vậy, "
      "điều khiển hệ thống truyền tải thông qua hệ thống đo lường tại trạm biến "
      "áp được giữ trong một ranh giới riêng, còn hệ thống điều khiển của tổ "
      "máy phát (gồm điều khiển lò hơi và điều khiển tuabin) được giữ trong "
      "ranh giới riêng khác. Sự tương tác giữa hai ranh giới này hoàn toàn là "
      "thủ công. Việc giải quyết bài toán điều khiển phát sinh từ việc hợp "
      "nhất điều khiển tự động của hai ranh giới là đề tài của nhiều bài báo "
      "trên thế giới. Tuy nhiên, ít nhất là ở Ấn Độ, điều đó chưa từng được thử "
      "trong thực tế.",
      "Most of these types of controls applicable for power system networks "
      "are in fact manual. There is a specific reason for selecting manual "
      "control. The manual control does not interfere with the generating unit "
      "control. Therefore, the transmission system control through substation "
      "instrumentation is kept under one boundary whereas the control "
      "instrumentation of generating unit (consisting of boiler control and "
      "turbine control) is kept under separate boundary. Interaction between "
      "these two boundaries is purely manual. The solution of control problem "
      "(arising out of merging the automatic control of two boundaries) are "
      "the subject of many papers worldwide. But these have never been tried "
      "to in practice, at least in India.")

    # ------------------------------------------------------------ Examples
    H(b, lang, "Ví dụ", "Examples")

    # Example 4.1
    H(b, lang, "Ví dụ 4.1", "Example 4.1", level=3)
    P(b, lang,
      "Trong hệ thống truyền bằng sợi quang, công suất quang đầu vào là −12 dBm "
      "và công suất đầu ra là −18 dBm. Nếu chiều dài sợi là 600 mét, hãy tính "
      "độ suy hao?",
      "In an optical fibre transmission system the input optical power is "
      "−12 dBm and the output power is −18 dBm. If the fibre length is 600 "
      "metres, find the attenuation?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "Suy hao tổng = P_vào − P_ra = −12 − (−18) = 6 dB. Độ suy hao trên mỗi "
      "kilomet chiều dài:",
      "Attenuation per kilometre length")
    E(b, lang,
      "(−12 − (−18))/(600/1000) = 6/0.6 = 10 dB/km.",
      "(18 − 12)/(600/1000) = 6/0.6 = 10 dB/km. Ans.")

    # Example 4.2
    H(b, lang, "Ví dụ 4.2", "Example 4.2", level=3)
    P(b, lang,
      "Nếu tần số truyền tín hiệu quang là 10 Megahertz và khoảng cách cần "
      "truyền chỉ là 600 mét, băng thông tối thiểu yêu cầu của sợi quang là "
      "bao nhiêu?",
      "If the signal transmission frequency for an optical signal is 10 "
      "Megahertz and distance to be transmitted is 600 metres only, what is "
      "the minimum bandwidth required for the fibre?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "Băng thông yêu cầu:", "The required bandwidth,")
    E(b, lang,
      "= 10 × 600/1000 = 6 MHz-km.",
      "= 10 × 600/1000 = 6 MHz-km.")

    # Example 4.3
    H(b, lang, "Ví dụ 4.3", "Example 4.3", level=3)
    P(b, lang,
      "Khi dùng kỹ thuật điều chế mã xung (PCM), một mã mức 7 chữ số đã được "
      "truyền. Nếu băng thông tín hiệu là 2 KHz, hãy tìm băng thông kênh sóng "
      "mang tối thiểu cần thiết?",
      "Through pulse code modulation (PCM) technique, a 7-digit level code "
      "has been transmitted. If the signal bandwidth is 2 KHz, find the "
      "minimum carrier channel bandwidth required?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "Yêu cầu băng thông cho trường hợp này được cho bởi:",
      "Bandwidth requirement for such a situation is given by:")
    E(b, lang, "BW = N f₀", "BW = N f₀")
    E(b, lang, "= 7 × 2 KHz = 14 KHz.", "= 7 × 2 KHz = 14 KHz. Ans.")

    # Example 4.4 (final arithmetic continues on PDF p. 240)
    H(b, lang, "Ví dụ 4.4", "Example 4.4", level=3)
    P(b, lang,
      "Với kỹ thuật PCM, hãy tìm số mức lượng tử hóa của bộ mã hóa 8 chữ số. "
      "Cũng hãy tìm dải đo của bộ mã hóa nếu mỗi mức tương ứng 1 volt. Nếu tín "
      "hiệu thực có giá trị 134.2 volt, hãy tính sai số lượng tử hóa trong "
      "điều chế.",
      "For PCM technique, find the quantization level for an 8-digit encoder. "
      "Find also the range of the encoder if each level represents 1 volt. If "
      "the actual signal is of the value of 134.2 volts, find quantization "
      "error in modulation.")
    H(b, lang, "Lời giải", "Solution", level=4)
    E(b, lang,
      "Số mức lượng tử hóa = 2⁸ = 256",
      "Quantization level = N⁸ = 2⁸ = 256")
    E(b, lang,
      "Dải đo của bộ mã hóa = (2⁸ − 1) × giá trị của mỗi mức",
      "Range of the encoder = (N⁸ − 1) × value of each level")
    E(b, lang,
      "= (2⁸ − 1) × 1 = 255 volt.",
      "= (2⁸ − 1) × 1 = 255 volt.")
    P(b, lang,
      "Giá trị điện áp ở dạng nhị phân:",
      "The value of voltage in binary form shall be,")
    E(b, lang, "01000110 = 134", "01000110 = 134")
    P(b, lang, "Vì vậy, sai số gặp phải", "Hence, the error encountered")
    E(b, lang,
      "= (134.2 − 134)/134.2 × 100 = 0.15% (xấp xỉ).",
      "= (134.2 − 134)/134.2 × 100 = 0.15% (app.) Ans.")

    # ------------------------------------------------------------ Exercise
    H(b, lang, "Bài tập", "Exercise")
    L(b, lang,
      ["Định nghĩa đo từ xa. Vì sao tín hiệu thủy lực nhìn chung là hiện tượng "
       "mang tính địa phương?",
       "Mô tả chi tiết đo từ xa khí nén với sự trợ giúp của sơ đồ đường dây khí "
       "nén.",
       "Vì sao nguồn một chiều 24 V được chọn cho các bộ phát tại hiện trường "
       "trong đo từ xa điện?",
       "So sánh hệ thống tín hiệu xoay chiều và một chiều.",
       "Hệ thống an toàn nội tại là gì? Hệ thống đó được triển khai như thế "
       "nào với sự trợ giúp của rào cách ly trong hệ thống đo từ xa bằng cáp?",
       "Làm thế nào để chuyển tín hiệu đầu ra dạng dòng sang dạng điện áp?",
       "Sự khác biệt giữa nhiễu chế độ thường và nhiễu chế độ chung trong đo từ "
       "xa bằng cáp là gì? Nguyên nhân chính gây ra nhiễu là gì?",
       "Cáp đồng trục là gì? Cáp này vượt trội hơn cáp UTP hoặc STP thông "
       "thường ở điểm nào?",
       "Cáp sợi quang là gì? Những vấn đề gặp phải với cáp đồng đã dẫn đến "
       "việc lựa chọn cáp sợi quang là gì?",
       "Những yếu tố chính nào ảnh hưởng đến độ bền tổng thể của sợi quang?",
       "Mô tả cấu tạo đầy đủ của cáp sợi quang bằng sơ đồ cắt bổ.",
       "Những yêu cầu đối với một sợi cáp quang hoàn hảo là gì?",
       "Cáp ghép là gì?",
       "Mô tả đo từ xa số. Đo từ xa xung là gì? Những lợi ích của PCM là gì?",
       "Mô tả hệ thống đo từ xa RF với sự trợ giúp của sơ đồ."],
      ["Define telemetry. Why hydraulic signalling is a local phenomenon in "
       "general?",
       "Describe pneumatic telemetry in detail with the help of sketch of "
       "pneumatic cabling.",
       "Why 24 volt D.C. supply system is selected for field transmitters "
       "under electrical telemetry?",
       "Make comparison between A.C. and D.C. signalling system.",
       "What is intrinsically safe system? How it is implemented with the help "
       "of barrier under cable telemetry system?",
       "How an output signal in the current form converted into voltage form?",
       "What is the difference between normal mode noise and common mode noise "
       "in cable telemetry? What is main reason behind the noise generation?",
       "What is a co-axial cable? How is it superior to ordinary UTP or STP "
       "cable?",
       "What is fibre optic cable? What were the problems encountered with "
       "copper cable that led to selection of fibre optic cable?",
       "What are the primary factors that affect the overall strength of "
       "fibre?",
       "Describe complete view of an optical fibre cable with the help of a "
       "cut-view sketch.",
       "What are the requirements of a perfect optical fibre cable?",
       "What is a composite cable?",
       "Describe digital telemetry. What is pulse telemetry? What are the "
       "benefits of PCM?",
       "Describe an RF telemetry system with the help of a sketch."],
      ordered=True)

    return b
