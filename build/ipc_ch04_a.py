# -*- coding: utf-8 -*-
"""Chapter 4, "Telemetry", section 4.1 "Introduction" (EN/VI bilingual).

Source: Janardan Prasad, M. N. Jayaswal and Vishnu Priye, *Instrumentation and
Process Control* (I.K. International, 2019), PDF pp. 216-219, printed pp.
204-207, decoded text lines 8150-8306.  The two source figures (4.1-4.2) are
redrawn as vectors in the `ipcfig4_a` supplier module and placed where the
text refers to them.  Units use literal Unicode superscripts; the English
body follows the source wording, the Vietnamese body uses the accepted
technical reading.
"""

import ipcfig4 as F
from ipc_ch04_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ---------------------------------------------------------------- 4.1
    H(b, lang,
      "4.1 Giới thiệu",
      "4.1 Introduction")

    P(b, lang,
      "Đo từ xa gồm hai phần: tele (truyền đi xa) và metering (đo lường). Tele "
      "nghĩa là truyền tín hiệu đi một khoảng cách, tức là ở vị trí xa, còn "
      "metering nghĩa là phép đo. Theo cách hiểu này, đo từ xa có thể được định "
      "nghĩa là các kỹ thuật đo lường từ xa và truyền tín hiệu.",
      "Telemetry consists of two parts: tele and metering. Tele means distance "
      "transmission, that is, a remote location, and metering means measurement. "
      "In this way, telemetry can be defined as remote measurement techniques "
      "and transmission.")

    P(b, lang,
      "Các phép đo thực hiện ở vị trí xa ít có ý nghĩa nếu không được truyền tới "
      "người quan sát đặt ở một địa điểm trung tâm để phân tích. Điều này có "
      "nghĩa là có một khoảng cách đáng kể giữa các thiết bị đo đặt xa và các "
      "thiết bị phân tích đặt tại trung tâm. Khoảng cách đó có thể chỉ là vài "
      "mét hoặc lớn tới hàng nghìn kilômét. Nhận xét này cũng cho thấy phương "
      "pháp truyền tín hiệu ẩn chứa ngay trong định nghĩa về đo từ xa. Phương "
      "pháp truyền sẽ đơn giản hơn với khoảng cách nhỏ và phức tạp hơn với "
      "khoảng cách lớn.",
      "The measurements, which are remote, are of little importance unless they "
      "are transmitted to the observer for analysis located at some central "
      "place. This means there is a considerable gap between the remotely "
      "located measurement instruments and the centrally located analysis "
      "instruments. This gap can be as low as a few metres or as high as "
      "thousands of kilometres. This discussion points towards the existence "
      "of transmission methods as well, which is hidden inside the definition "
      "of telemetry. The methods of transmission shall be simpler for low "
      "distances and complex for higher distances.")

    P(b, lang,
      "Trong khi kỹ thuật đo vẫn là như nhau, tức là dùng các loại bộ chuyển đổi, "
      "bộ phát khác nhau, thì các phương pháp truyền tín hiệu phù hợp cần "
      "được xem xét kỹ lưỡng.",
      "While the measurement techniques happen to be the same, that is, "
      "different types of transducers, transmitters and so on, the suitable "
      "transmission methods applied need to be examined thoroughly.")

    P(b, lang,
      "Xét về mặt logic, khái niệm đo từ xa dường như phát triển từ hiện tượng "
      "telepathy (cảm ứng từ xa) hoặc cơ chế truyền tin điện tín (telegraph), "
      "vốn từng được dùng phổ biến trong bưu điện và nhiều nơi tương tự. Phương "
      "pháp này rất phổ biến và hữu ích như một hệ thống gửi thông tin cho cả "
      "mục đích quân sự lẫn công việc dân sự. Về sau, điều khiển quá trình cũng "
      "sử dụng các kỹ thuật này để đạt hiệu năng tối ưu. Xu hướng áp dụng các "
      "kỹ thuật truyền thông khác nhau, ví dụ truyền thông vệ tinh để điều "
      "khiển tàu vũ trụ hoặc điều khiển thiết bị quân sự nhằm cải thiện điều "
      "khiển quá trình, vẫn tiếp tục được theo đuổi.",
      "Logically it seems that the concept of telemetry has evolved from "
      "telepathy or telegraphic messaging mechanism, which were in earlier use "
      "in post offices and other similar places. The method was very much "
      "popular and useful also as an information sending system for military "
      "purposes as well as domestic affairs. Later on process control also "
      "utililized these techniques for optimum performance of the process. "
      "This trend of adopting different communication techniques, e.g. "
      "satellite communication techniques for spacecraft control or military "
      "equipment controls for the purpose of process control improvement, are "
      "still being followed.")

    P(b, lang,
      "Vì vậy, phạm vi định nghĩa của đo từ xa có thể được điều chỉnh để bao "
      "gồm cả phương pháp truyền tín hiệu đo (cũng như tín hiệu điều khiển hoặc "
      "bất kỳ dữ liệu nào khác) từ một đầu đến đầu kia của hệ thống thiết bị. "
      "Truyền trạng thái của các biến quá trình tại các mỏ dầu đến trạm điều "
      "khiển trung tâm, truyền tín hiệu giám sát tình trạng từ đầu này đến đầu "
      "kia của một hệ thống cung ứng dầu thô đường dài, hay truyền các tín hiệu "
      "thông tin mang trạng thái lỗi, sự thay đổi mức điện áp, tần số, biến "
      "động tải hoặc tình trạng cung cấp không đủ cho hệ thống truyền tải điện "
      "năng qua các liên kết lưới điện là một số ví dụ điển hình về hệ thống "
      "đo từ xa điều khiển quá trình đáng tin cậy nhất.",
      "Thus, the scope of definition of telemetry can be modified to include "
      "the method of transmission of the measurement signal (also control "
      "signals or any other data) from one end to the other end of an "
      "instrumentation system. Transmission of status of process variables at "
      "the oilfields to the central control station, transmission of "
      "condition-monitoring signals from one end to the other on a long "
      "distance supply system of crude oil, and transmission of information "
      "signals containing status of fault conditions or changes in voltage "
      "level or frequency or load variations or insufficient supply for an "
      "electrical power transmission system through grid interconnections are "
      "some of the examples of most reliable process control telemetry system.")

    P(b, lang,
      "Phương pháp truyền tín hiệu được chọn phụ thuộc vào loại môi trường đo "
      "hoặc điều khiển. Nhìn chung, chúng ta quan tâm đến ba loại môi trường "
      "đo hoặc điều khiển: khí nén, thủy lực và điện. Ngày nay còn xuất hiện "
      "loại môi trường tín hiệu thứ tư gọi là quang. Trong hệ thống này, phần "
      "truyền tín hiệu chỉ dùng ánh sáng, vì vậy để hệ thống hoạt động đúng, "
      "tín hiệu ban đầu phải được biến đổi sang dạng quang. Cũng theo cách "
      "đó, sau khi truyền đi, tín hiệu quang lại phải được biến đổi ngược về "
      "dạng ban đầu. Việc truyền tín hiệu quang được thực hiện qua cáp sợi "
      "quang.",
      "Methods adopted for signal transmission depend upon the type of "
      "measurement or control media selected. In general, we are concerned "
      "with three types of measurement or control media, e.g. pneumatic, "
      "hydraulic and electrical. Nowadays a fourth type of signalling medium "
      "has also come into existence, which is called optical type. In this "
      "system, the signal transmission part is only optical and therefore, for "
      "this system to work properly, the original signal has to be transformed "
      "into optical form. In the same way, after transmission, this optical "
      "signal has to be transformed back to the original form. The transmission "
      "of optical signal is carried out through optical fibre cables.")

    # ------------------------------------------------------------ 4.1 (i)
    H(b, lang, "Đo từ xa khí nén", "Pneumatic remote measurement", level=3)

    P(b, lang,
      "Đo từ xa bằng khí nén được thực hiện bởi các bộ chuyển đổi hoặc bộ phát "
      "vận hành bằng khí nén. Các bộ phát này hoạt động dựa trên hệ thống "
      "vách-còi phun (flapper-nozzle) nổi tiếng đã được mô tả ở phần trước. "
      "Vách-còi được nối với phần cảm biến của hệ thống phát. Chuyển động do sự "
      "thay đổi của biến quá trình được vách-còi tiếp nhận. Chuyển động của "
      "vách-còi đối với vòi phun tạo ra đầu ra khí nén tỷ lệ với đáp ứng của "
      "cảm biến. Tín hiệu khí nén này, đại diện cho biến sơ cấp, được truyền "
      "đến phòng điều khiển đặt tại trung tâm, nơi lắp đặt các thiết bị khác "
      "để xử lý tiếp tín hiệu khí nén.",
      "The pneumatic remote measurement is performed by pneumatically operated "
      "transducers or transmitters. The working of these transmitters is based "
      "upon the most popular flapper-nozzle system which has already been "
      "described in earlier discussion. The flapper is connected to the sensor "
      "part of the transmitter system. The movement due to the variation in "
      "process variable is taken up by the flapper. The movement of the flapper "
      "against the nozzle develops pneumatic output proportional to the sensor "
      "response. This pneumatic output signal, which is representative of "
      "primary variable, is to be transmitted to the centrally located control "
      "room where other instruments are also installed for carrying out further "
      "processing of the pneumatic signals.")

    P(b, lang,
      "Hệ thống tín hiệu khí nén tương ứng với nguồn khí khô tiêu chuẩn 1,4 "
      "kg/cm² và tín hiệu đo hoặc điều khiển được tạo ra trong khoảng 0,2 đến "
      "1,0 kg/cm². Mọi dạng chỉ thị, máy ghi, bộ điều khiển khí nén v.v. đều "
      "hoạt động bằng dạng tín hiệu này. Hệ thống khí nén rất phổ biến nói "
      "chung cho đến năm 2000, và trong một số trường hợp là hệ thống thiết bị "
      "duy nhất đáng tin cậy đã được thời gian kiểm chứng. Ngày nay hệ thống "
      "này đã được thay bằng hệ thống điện tử, nhưng vẫn còn hoạt động ở một "
      "số nhà máy chế biến cũ nơi việc thay thế tỏ ra không kinh tế. Hơn nữa, "
      "các phần tử điều khiển cuối thông thường là van điều khiển hoặc cửa gió "
      "vận hành bằng khí nén vẫn đang hoạt động và sẽ tiếp tục như vậy trong "
      "nhiều năm tới. Vì vậy, nhu cầu đối với hệ thống khí nén, dù tương đối "
      "ít hơn, vẫn sẽ tiếp tục.",
      "Pneumatic signalling system corresponds to a standard dry air supply "
      "system of 1.4 kg/cm² and a generated measurement or control signal in "
      "the form of 0.2 to 1.0 kg/cm². All forms of pneumatic indicators, "
      "recorders, controllers, etc. are operated by this form of signal only. "
      "The pneumatic system have been very popular, in general, till 2000 A.D., "
      "and in some cases have been the only reliable and the time-proven "
      "instrumentation system. Nowadays this system has been replaced by "
      "electronic system, but is still in operation in some of the older "
      "process plants where the replacement would have proved uneconomical "
      "otherwise. Moreover, the final control elements which are conventional "
      "pneumatically operated control valves or dampers are still in operation "
      "and continue to be like that in years to come. Therefore, the "
      "requirement of pneumatic system, though comparatively less, shall "
      "continue.")

    # ------------------------------------------------------------ 4.1 (ii)
    H(b, lang, "Tín hiệu thủy lực", "Hydraulic signalling", level=3)

    P(b, lang,
      "Hệ thống tín hiệu thủy lực hoàn toàn là hiện tượng cục bộ. Chẳng hạn, "
      "hệ thống truyền dẫn dùng để điều khiển thủy lực tua-bin và các động cơ "
      "chính tốc độ cao tương tự chỉ liên quan đến truyền tín hiệu quãng đường "
      "ngắn. Hệ thống truyền thủy lực quãng đường ngắn có đặc điểm là tổn thất "
      "áp suất không đáng kể, ít phải bảo trì đường ống và dễ quan sát trực "
      "tiếp bởi người vận hành hiện trường.",
      "The hydraulic signalling system is entirely a local phenomenon. For "
      "instance, the system of transmission for hydraulic control of turbine "
      "and other similar high-speed prime movers are related to short distance "
      "transmission. The short distance hydraulic transmission system is "
      "characterized by negligible pressure less, less maintenance involved in "
      "lines, easy visual monitoring by field operators, etc.")

    P(b, lang,
      "Trong hệ thống thủy lực, nguồn cung cấp tiêu chuẩn nói chung là áp suất "
      "dầu điều khiển 6 kg/cm², còn tín hiệu đầu ra tương ứng với dải tiêu "
      "chuẩn từ 1,2 đến 4,2 kg/cm². Tín hiệu đầu ra thủy lực này vận hành "
      "nhiều thiết bị thủy lực nối với hệ thống điều khiển tua-bin, ví dụ bộ "
      "điều tốc, van vào hơi, van ra nước ngưng và van ngắt nhanh. Vì hệ thống "
      "thủy lực không phải là hệ thống truyền tín hiệu đường dài và liên quan "
      "rất ít đến đo từ xa, nên chúng ta không tiếp tục thảo luận thêm.",
      "In the hydraulic system, the standard supply is the control oil "
      "pressure of 6 kg/cm² in general and the output signal corresponds to a "
      "range from 1.2 to 4.2 kg/cm² standard. This hydraulic output signal "
      "operates a number of hydraulic equipment connected to turbine control "
      "systems, e.g. governor, steam inlet valve, condensate outlet valve, "
      "quick closing trip valve, etc. Since the hydraulic system is not at all "
      "a long transmission system and involves less telemetry, the discussion "
      "shall not continue any more.")

    # ----------------------------------------------------------- 4.1 (iii)
    H(b, lang, "Tín hiệu điện", "Electrical signalling", level=3)

    P(b, lang,
      "Hệ thống truyền tín hiệu cuối cùng là loại điện, là loại quan trọng "
      "nhất hiện nay. Hầu như toàn bộ tín hiệu đo và điều khiển hiện nay đều "
      "là điện. Trong trường hợp này, các hệ thống cung cấp thiết bị không "
      "gián đoạn tiêu chuẩn gồm ba loại: 110 V một chiều (DC), 110 V xoay "
      "chiều (AC) và 24 V một chiều.",
      "The last transmission system is the electrical type, which is the most "
      "important nowadays. Almost all measurement and control signalling are "
      "now is electrical. In this case, the standard uninterrupted "
      "instrumentation supply system are of three types: 110 volts D.C., 110 "
      "volts A.C. and 24 volts D.C.")

    P(b, lang,
      "Trong ba hệ thống đó, 110 V DC luôn được dùng cho mạch liên khóa dựa "
      "trên rơ le cơ điện, vốn cũng đang dần bị loại bỏ và thay bằng hệ thống "
      "liên khóa cổng logic hoặc hệ thống điều khiển logic lập trình được "
      "(PLC) (sẽ được mô tả ở chương thích hợp). Nguồn 110 V AC cấp cho tất cả "
      "bộ điều khiển, máy ghi, thiết bị chỉ thị và các thiết bị thu khác đặt "
      "trong phòng điều khiển trung tâm. Nguồn 24 V DC cấp cho tất cả bộ phát "
      "đặt ở hiện trường ngoài trời của một nhà máy chế biến. Như đã mô tả ở "
      "phần trước, nguồn điện áp thấp được dùng để giảm thiểu các nguy cơ an "
      "toàn do sự hiện diện của hỗn hợp hoặc khí dễ nổ tại hiện trường. Điện "
      "áp thấp làm cho bộ phát trở thành hệ thống an toàn nội tại.",
      "Out of these three systems, 110 volts D.C. is invariably used for "
      "electro-mechanical relay based interlocking circuit which also are "
      "being phased out slowly and are being replaced by logic gate "
      "interlocking system or programmable logic control (PLC) system (these "
      "shall be described in appropriate chapter). The 110 volt A.C. supply is "
      "employed to all the controllers, recorders, indicators or other "
      "receiver instruments, which are located inside the central control "
      "room. The 24 volts D.C. supply is supplied to all the remote "
      "transmitters located in the outdoor field of a process plant. As has "
      "been described earlier, the low voltage supply system is used to "
      "minimize safety related hazards due to the presence of explosive "
      "mixture or gases in the field. Low voltage makes the transmitter an "
      "intrinsically safe system.")

    NOTE(b, lang,
      "Hệ thống an toàn nội tại là hệ thống có năng lượng sẵn có không đủ để "
      "đốt cháy hỗn hợp hoặc khí dễ nổ tại hiện trường. Đầu ra của các bộ phát "
      "lắp tại hiện trường này có dạng 4 đến 20 mA và phải được truyền về "
      "phòng điều khiển trung tâm để xử lý tiếp.",
      "An intrinsically safe system is that system which has insufficient "
      "amount of energy available to ignite an explosive mixture or gases in "
      "the field. Output of these field mounted transmitters which is in the "
      "form of 4 to 20 mAmps has to be transmitted to the central control room "
      "for further processing.")

    P(b, lang,
      "Trong hệ thống đo từ xa khí nén, đầu ra tín hiệu khí nén của tất cả bộ "
      "phát trong một khu vực nhất định được dẫn về một hộp đấu nối bằng các "
      "ống đồng hoặc ống thép không gỉ AISI 304 riêng biệt, thường có đường "
      "kính ngoài 6 mm. Ống kim loại được dùng thay cho ống PVC để tránh hư "
      "hỏng ống PVC do nguyên nhân cơ học.",
      "In pneumatic telemetry system, pneumatic signal output of all the "
      "transmitters located in one particular area are brought to a junction "
      "box by means of individual copper or AISI 304 stainless steel tubing of "
      "normally 6 mm O.D. Metal tubes are used in place of PVC tube to avoid "
      "damage of PVC tube due to mechanical causes.")

    P(b, lang,
      "Hình 4.1 cho thấy các ống tín hiệu riêng lẻ từ hiện trường được đấu nối "
      "bên trong hộp đấu nối khí nén.",
      "Figure 4.1 shows the individual field signal tubes terminated inside "
      "the pneumatic junction box.")
    FIG(b, 1, F.fig_f01(), lang)

    P(b, lang,
      "Việc đấu nối các ống tín hiệu khí nén vào hộp đấu nối (làm bằng hợp kim "
      "nhôm) được thực hiện bằng các khớp nén có kích thước phù hợp (làm bằng "
      "đồng thau hoặc thép không gỉ AISI 304). Từ hộp đấu nối hiện trường, một "
      "bó ống khí nén PVC nhiều lõi được dẫn ngầm suốt đường đến phòng điều "
      "khiển trung tâm. Bó ống nhiều lõi này được bọc vỏ PVC, gia cố giáp và "
      "cuối cùng quấn băng PVC từ bên ngoài để chống hư hỏng cơ học và các hư "
      "hỏng khác. Bó ống có thể có 7 lõi, 14 lõi hoặc 19 lõi, nghĩa là có 7, "
      "14 hoặc 19 ống độc lập tương ứng được ghép lại thành một bó hoàn chỉnh. "
      "Vì vậy, bó 19 lõi có thể đảm nhận 19 tín hiệu khí nén khác nhau giữa "
      "phòng điều khiển trung tâm và hiện trường.",
      "The termination of these pneumatic signal tubings into the junction box "
      "(made of aluminium casting) are done by means of compression fittings "
      "of appropriate sizes (made of brass or AISI 304 stainless steel). Now "
      "from the field junction box, a multicored, PVC pneumatic tube bunch is "
      "run underground all the way up-to the central control room. This "
      "multicored tube bundle is PVC sheathed, armoured and finally PVC tape "
      "wound from the outside to protect against mechanical and other damages. "
      "This tube bundle can have 7-core, 14-core or 19-core (this means there "
      "are 7, 14 or 19 independent tubes respectively which have been put "
      "together to make the complete bundle). Therefore, a 19-cored tube bundle "
      "is capable of handling 19 different pneumatic signals between the "
      "central control room and the field.")

    P(b, lang,
      "Ở đầu phòng điều khiển, bó ống nhiều lõi mang tất cả tín hiệu khác "
      "nhau được đấu vào một bảng đầu cuối (TB) chung đặt gần mặt sau của "
      "bảng điều khiển như Hình 4.2. Việc đấu nối này lại được thực hiện bằng "
      "các khớp nén cùng kích thước và loại như đã dùng tại hộp đấu nối. Từ "
      "bảng đầu cuối, các kết nối mang tín hiệu này được dẫn đến từng thiết bị "
      "(phía sau) bằng ống đồng và khớp nén bằng đồng thau.",
      "In the control room end, the multicored tube bundle carrying all "
      "different signals is terminated at common tube Terminal Board (TB) "
      "located near the back of the control panel as shown in Figure 4.2. "
      "This termination is again accomplished by means of compression fittings "
      "of same size and type that have been used on the junction box. From the "
      "TB, these signal-carrying connections are brought to individual "
      "instrument (back side) by means of copper tubings and brass fittings.")

    FIG(b, 2, F.fig_f02(), lang)

    P(b, lang,
      "Đo từ xa khí nén chỉ giới hạn trong một cơ sở công nghiệp nhất định, "
      "tức là giữa khu vực hiện trường của nhà máy và phòng điều khiển trung "
      "tâm của nó (tối đa một kilômét). Nhưng đối với hệ thống đo từ xa cần "
      "phủ khoảng cách lớn hơn một kilômét, nên dùng truyền tín hiệu dạng điện. "
      "Xét về tối ưu hóa, tín hiệu điện vẫn kinh tế ngay cả trong trường hợp "
      "đã chọn tín hiệu khí nén. Việc chọn tín hiệu khí nén chủ yếu là do sự "
      "hiện diện của hệ thống thiết bị khí nén; vì vậy, ở nơi hệ thống thiết "
      "bị khí nén đã được thay bằng hệ thống điện tử, mọi hệ thống tín hiệu "
      "đều là loại điện.",
      "Pneumatic telemetry is limited to within a particular industrial "
      "establishment i.e. between a plant field area and its central control "
      "room (within one kilometre maximum). But for a telemetry system to "
      "cover long distance beyond one kilometre, signal transmission in "
      "electrical form is advisable. As far as optimization is concerned, "
      "electrical signalling is economical even in the cases where pneumatic "
      "signalling has been selected. Selection of pneumatic signalling is "
      "primarily due to the presence of pneumatic instrumentation system and "
      "therefore, where pneumatic instrumentation systems have been replaced "
      "by electronic systems, all signalling systems are of electrical type "
      "only.")

    P(b, lang,
      "Nói chung, đo từ xa dùng tín hiệu điện gồm hai loại: đo từ xa bằng cáp "
      "và đo từ xa RF. Hai loại này nói chung đều có thể ở dạng tương tự hoặc "
      "số.",
      "Telemetry for electrical signalling in broad sense are of two types: "
      "Cable telemetry and R.F telemetry. These two altogether can be of analog "
      "as well as digital varieties.")

    return b
