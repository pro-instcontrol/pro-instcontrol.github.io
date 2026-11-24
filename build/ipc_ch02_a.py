# -*- coding: utf-8 -*-
"""Chapter 2, "Transducers - II", section 2.1 "Elements of Instrumentation System"
(EN/VI bilingual).

Source: Janardan Prasad, M. N. Jayaswal and Vishnu Priye, *Instrumentation and
Process Control* (I.K. International, 2019), PDF pp. 75-82, printed pp. 63-70,
decoded text lines 2633-2923.  The five source figures (2.1-2.5) are redrawn
as vectors in the `ipcfig2` supplier modules and placed where the text refers
to them.  Units are written with literal Unicode superscripts; the English
body retains the source wording quirks, the Vietnamese body uses the accepted
technical meaning.
"""

import ipcfig2 as F
from ipc_ch02_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ---------------------------------------------------------------- 2.1
    H(b, lang,
      "2.1 Các phần tử của hệ thống thiết bị",
      "2.1 Elements of Instrumentation System")

    P(b, lang,
      "Như chúng ta đã biết, dụng cụ đo là mắt của bất kỳ nhà máy chế biến nào. "
      "Người vận hành quá trình chỉ quan sát được trạng thái của quá trình thông qua "
      "các dụng cụ đo. Tương tự, hệ thống đo lường và điều khiển là trái tim của bất "
      "kỳ nhà máy chế biến nào. Không một thao tác nào có thể thực hiện được nếu "
      "thiếu hệ thống thiết bị phù hợp.",
      "As we know, instruments are eyes of any processing plant. Process operators "
      "visualize the status of the process through instruments only. Similarly, "
      "instrumentation and control systems are the heart of any processing plant. "
      "No operation can be made possible without proper instrumentation systems.")

    P(b, lang,
      "Trong những năm trước đây, việc điều khiển quá trình về cơ bản là thủ công, "
      "thông qua các van điều tiết được lắp đặt phù hợp và vận hành bằng tay. Nhưng "
      "ngày nay, hầu hết các hệ thống điều khiển quá trình đều tự động. Rất ít hệ "
      "thống điều khiển quá trình còn vận hành bằng tay. Dù là điều khiển tự động "
      "hay thủ công, các tác động điều khiển cuối cùng vẫn chỉ được thực hiện thông "
      "qua các van điều khiển vận hành bằng khí nén. Như vậy, van điều khiển hay "
      "phần tử điều khiển cuối là phần tử cơ bản và quan trọng nhất trong bất kỳ "
      "hệ thống thiết bị nào.",
      "In earlier days, control of processes were basically manual through suitably "
      "installed and manually operated regulating valves. But nowadays majority of "
      "the process controls are automatic. Very few process controls work through "
      "manual control. Whatever may be the form of controls, automatic or manual, "
      "the final control actions are to be performed through pneumatically operated "
      "control valves only. Thus, control valve or the final control element is the "
      "basic and the all important element in any instrumentation system.")

    P(b, lang,
      "Nhìn chung, trong bất kỳ hệ thống thiết bị nào cũng có thể có một số hoặc "
      "tất cả các bộ phận, phần tử sau:",
      "In any instrumentation system, a few or all of the following components or "
      "elements shall be present, in general:")

    L(b, lang,
      ["Bộ phát", "Thiết bị thu", "Bộ điều khiển", "Phần tử điều khiển cuối",
       "Thiết bị phụ trợ"],
      ["Transmitter", "Receiver instrument", "Controller", "Final control element",
       "Instrument accessories"],
      ordered=True)

    P(b, lang,
      "Hình 2.1 cho thấy hệ thống hoàn chỉnh dưới dạng sơ đồ khối.",
      "Figure 2.1 shows the complete system in a block diagram form.")
    FIG(b, 1, F.fig_f01(), lang)

    # -------------------------------------------------------------- 2.1 (i)
    H(b, lang, "(i) Bộ phát", "(i) Transmitter", level=3)
    P(b, lang,
      "Đây là phần tử đầu tiên, gồm cảm biến sơ cấp và bộ chuyển đổi. Nó được lắp "
      "đặt trước phần tử điều khiển cuối. Nó đo biến quá trình và biến đổi biến đó "
      "thành dạng thích hợp, tức là 0,2 đến 1,0 kg/cm² đối với hệ thống tín hiệu "
      "khí nén hoặc 4 đến 20 mA một chiều (DC) đối với hệ thống tín hiệu điện. "
      "Nhìn chung, bộ phát có ba loại chính:",
      "This is the very first element, which consists of primary sensor and the "
      "transducer. This is installed before the final control element. This will "
      "measure the process variable and will transform the same into suitable form, "
      "i.e. 0.2 to 1.0 kg/cm² in case of pneumatic signal system or 4 to 20 mAmps. "
      "D.C. in case of electrical signal system. In general, transmitters are "
      "available in three different varieties:")
    L(b, lang,
      ["Loại khí nén", "Loại điện/điện tử", "Loại thông minh"],
      ["Pneumatic type", "Electrical/Electronic type", "Smart type"],
      ordered=True)
    P(b, lang,
      "Trong đó hệ thống cảm nhận sơ cấp cơ bản vẫn không đổi; chính phần bộ "
      "chuyển đổi thứ cấp của hệ thống quyết định các loại khác nhau. Khi hoạt "
      "động của bộ chuyển đổi hoàn toàn là khí nén, bộ phát được gọi là loại khí "
      "nén. Nhưng khi nó hoạt động bằng điện, cho đầu ra dưới dạng 4 đến 20 mA "
      "một chiều (DC), nó được gọi là loại điện tử.",
      "Wherein the basic primary sensing system remains the same, it is the "
      "secondary transducer part of the system that decides the different varieties. "
      "When the operation of the transducer is fully pneumatic, the transmitter "
      "shall be called the pneumatic one. But when it is operated electrically "
      "giving output in terms of 4 to 20 mAmps. D.C., it shall be called an "
      "electronic type.")
    P(b, lang,
      "Mặt khác, bộ phát thông minh chẳng qua là dạng cải tiến của bộ phát điện tử "
      "hiện có. Vì vậy, các đặc tính phi tuyến vốn có của sự thay đổi biến quá trình "
      "được tuyến tính hóa bằng điện ngay trong bản thân bộ phát, và đầu ra được "
      "trình bày dưới dạng đầu ra tuyến tính. Ngoài ra, ảnh hưởng của các nhiễu động "
      "bên ngoài lên đầu ra, tức là tiếng ồn, rung động, thay đổi môi trường xung "
      "quanh, v.v., cũng được bù trừ tốt. Như chúng ta đã biết, những điều này trở "
      "nên khả thi nhờ tích hợp phần tử vi xử lý bên trong bộ phát. Đó là lý do "
      "đôi khi nó còn được gọi là bộ phát vi xử lý.",
      "Smart transmitter, on the other hand, is nothing but an improved form of "
      "existing electronic transmitter. Hence, the inherent non-linear "
      "characteristics of the process variable changes are linearised "
      "electronically in the transmitter itself and the output is presented in the "
      "form of linear output. Also the effect of external disturbances on output, "
      "i.e. noise, vibration, ambient changes, etc. are well compensated. As we "
      "know these are possible by incorporating microprocessor element inside the "
      "transmitter. That is why, it is sometimes called microprocessor transmitter "
      "as well.")

    # ------------------------------------------------------------- 2.1 (ii)
    H(b, lang, "(ii) Thiết bị thu", "(ii) Receiver instruments", level=3)
    P(b, lang,
      "Thiết bị thu là thiết bị đa dụng, vì nó nhận tín hiệu từ bộ phát để chỉ thị, "
      "ghi chép, điều khiển hoặc các mục đích khác. Tín hiệu tác động cơ bản của "
      "thiết bị thu vẫn không đổi, tức là 0,2 đến 1,0 kg/cm² (khí nén) hoặc 4 đến "
      "20 mA một chiều (DC) (điện) cho hầu hết mọi loại biến đo. Nếu biến đo là lưu "
      "lượng chất lỏng, thang đo được chia theo mét khối chuẩn/giờ. Tương tự, nếu "
      "biến đo là áp suất, thang đo được chia theo kg/cm². Nhưng nếu biến đo là mức "
      "của một bình chứa, thang đo được biểu diễn theo phần trăm chiều cao của "
      "bình, tức là 0%, 25%, 50%, v.v. Do đó, cùng một thiết bị thu có thể dùng cho "
      "bất kỳ biến đo nào chỉ bằng cách đổi thang đo, vì tín hiệu khởi phát từ mọi "
      "dạng biến đo đều như nhau.",
      "Receiver instrument is a generalized instrument since it receives the "
      "transmitter signal for indicating, recording, controlling or other purposes. "
      "The basic actuating signal for the receiver instruments remains same, i.e. "
      "0.2 to 1.0 kg/cm² (pneumatic) or 4 to 20 mAmps. D.C. (electrical) for almost "
      "all types of measurement variables. If the measurement variable is fluid "
      "flow, then the scale shall be marked in normalmetre cube/hour. Similarly, if "
      "the measurement variable is pressure, then the scale shall be marked in "
      "kg/cm². But if the measurement variable is level of a tank, then the scale "
      "shall be in terms of percentage of the tank height, i.e. 0%, 25%, 50%, etc. "
      "Hence, the same receiver instrument can be used for any measurement variable "
      "by only changing the scale, since the initiating signal from all form of "
      "measurement variable is same.")
    P(b, lang,
      "Loại thiết bị thu lại dựa trên loại bộ phát mà nó được nối tới để nhận tín "
      "hiệu đo khởi phát. Như vậy, thiết bị thu chỉ có hai loại, tức là loại khí "
      "nén và loại điện/điện tử.",
      "Types of receiver instrument is again based on types of transmitter to which "
      "these are connected for obtaining initiating measurement signal. Thus, "
      "receiver instrument can be of two types only, i.e. pneumatic type and "
      "electrical/ electronic type.")
    P(b, lang,
      "Thiết bị thu có thể ở dạng chỉ thị hoặc ghi chép. Dạng chỉ thị chỉ cho giá "
      "trị tức thời của biến đo, trong khi dạng ghi chép trình bày bản ghi trong "
      "một khoảng thời gian được quy định theo yêu cầu. Việc ghi chép được thực "
      "hiện bằng một cây bút chứa mực khô chậm, đặt nhẹ trên giấy biểu đồ (dạng "
      "dải, dạng tròn hoặc dạng xếp nếp). Giấy biểu đồ thường được di chuyển với "
      "tốc độ không đổi là 1/3 vòng/giờ. Đường cong vẽ ra theo cách này cho thấy "
      "sự biến đổi thực tế của giá trị biến đo trong một khoảng thời gian xác định.",
      "Receiver instrument can be in the form of indicating as well as recording. "
      "The indicating form shall give the instantaneous value of the measurement "
      "variable only whereas the recording form shall present record for a period "
      "to be specified as required. Recording is carried out by means of a pen "
      "filled with slow drying ink placed lightly on a chart paper (strip, circular "
      "or fanfold). The chart paper is moved at a constant speed of 1/3 revolution "
      "per hour, usually. The curve traced in this way shows the actual variation "
      "in the value of the measurement variable for a definite period of time.")

    # ------------------------------------------------------------ 2.1 (iii)
    H(b, lang, "(iii) Bộ điều khiển", "(iii) Controller", level=3)
    P(b, lang,
      "Trong hệ thống thiết bị, các tác động điều khiển được tạo ra bởi phần tử "
      "thường gọi là bộ điều khiển. Tác động điều khiển được tạo ra phụ thuộc vào "
      "sự thay đổi của biến đo so với giá trị cài đặt của nó. Giá trị cài đặt do "
      "người thiết kế quá trình quyết định theo yêu cầu của quá trình. Mặt khác, "
      "sự thay đổi của biến đo phụ thuộc vào các yếu tố sau:",
      "In the instrumentation systems, control actions are generated by the "
      "element, commonly known as controller. The control action generated depends "
      "upon the change in measurement variable with respect to its set value. The "
      "set value is decided by the process designer as per the process requirement. "
      "The change in measurement variable, on the other hand, is dependent upon "
      "the following factors:")
    L(b, lang,
      ["Nhiễu động từ phía nguồn cấp trong quá trình", "Biến đổi ở phía tải",
       "Thay đổi môi trường"],
      ["Supply side disturbances in the process", "Load side variations",
       "Environmental changes"],
      ordered=True)
    P(b, lang,
      "Sự thay đổi của biến đo có thể có các dạng sau:",
      "The changes in measurement variable can be of the following type:")
    L(b, lang,
      ["Thay đổi đột ngột", "Thay đổi với tốc độ không đổi theo thời gian",
       "Thay đổi tỉ lệ với bình phương của thời gian", "Thay đổi dạng xung"],
      ["Sudden changes", "Constant rate of changes with respect to time",
       "Changes proportional to square of the time", "Impulsive changes"],
      ordered=True)
    P(b, lang,
      "Theo đó, yêu cầu về các tác động hoặc chế độ điều khiển do phần tử điều "
      "khiển tạo ra có thể thuộc các loại sau:",
      "Accordingly the requirement of control actions/modes to be generated by the "
      "controller element can be of the following types:")
    L(b, lang,
      ["Điều khiển bật-tắt", "Điều khiển tỉ lệ", "Điều khiển tích phân",
       "Điều khiển vi phân"],
      ["On-off control", "Proportional control", "Integral control",
       "Derivative control"],
      ordered=True)
    P(b, lang,
      "Ngoài việc dùng một chế độ đơn lẻ, người ta còn kết hợp hai hoặc ba chế độ "
      "tùy theo loại nhiễu động cần điều khiển. Một bộ điều khiển tốt với sự kết "
      "hợp chế độ phù hợp cho các kết quả sau nhằm đáp ứng tiêu chuẩn đánh giá "
      "hiệu năng điều khiển:",
      "In addition to single mode implementation, a combination of two or three "
      "modes are also implemented depending upon the types of disturbances to be "
      "controlled. A good controller with proper combination of modes provides "
      "following results to meet the evaluation criteria of the control "
      "performance:")
    L(b, lang,
      ["Độ lệch nhỏ nhất sau một nhiễu động",
       "Khoảng thời gian ngắn nhất trước khi trở về giá trị cài đặt",
       "Độ lệch bù nhỏ nhất do thay đổi điều kiện vận hành"],
      ["Minimum deviation following a disturbance",
       "Minimum time interval before return to set value",
       "Minimum offset due to changes in operating conditions"],
      ordered=True)
    P(b, lang,
      "Đáp ứng tốt nhất của một biến được điều khiển, do một bộ điều khiển hoàn "
      "hảo tạo ra, là sự suy giảm biên độ sau một nhiễu động như thể hiện trong "
      "Hình 2.2.",
      "The best response of a controlled variable, provided by a perfect "
      "controller is amplitude decay following a disturbance as shown in Figure "
      "2.2.")
    FIG(b, 2, F.fig_f02(), lang)
    P(b, lang,
      "Trong khi các tác động điều khiển cơ bản vẫn giữ nguyên, việc phân loại bộ "
      "điều khiển phụ thuộc vào cách tạo ra tác động và môi trường hoạt động. Dựa "
      "trên quan điểm này, bộ điều khiển có thể thuộc các loại sau:",
      "While basic control actions remaining same, classification of controller "
      "depends upon how the actions are generated and what is the medium of "
      "operation. Based on this concept, the controllers can be of the following "
      "types:")
    L(b, lang,
      ["Bộ điều khiển khí nén", "Bộ điều khiển thủy lực",
       "Bộ điều khiển điện tử tương tự", "Bộ điều khiển điện tử số"],
      ["Pneumatic controller", "Hydraulic controller",
       "Analog electronic controller", "Digital electronic controller"],
      ordered=True)
    P(b, lang,
      "Trong bộ điều khiển khí nén, các tác động được tạo ra bằng khí nén, trong "
      "đó hệ thống vách-còi phun (flapper-nozzle) nổi tiếng kết hợp với tác động "
      "phản hồi được sử dụng. Ở đây, tín hiệu đầu vào và đầu ra cơ bản có dạng "
      "0,2 đến 1,0 kg/cm², nguồn cấp khí nén tiêu chuẩn là khí thiết bị ở 1,4 "
      "kg/cm².",
      "In pneumatic controller, actions are generated pneumatically wherein the "
      "well-known flapper-nozzle system combined with feedback action is employed. "
      "Here the basic input and output signals are in the form of 0.2 to 1.0 "
      "kg/cm² itself, the standard pneumatic supply system being instrument air "
      "at 1.4 kg/cm².")
    P(b, lang,
      "Mặt khác, trong bộ điều khiển thủy lực, hệ thống được vận hành bằng chất "
      "lỏng dầu mỏ không nén được và không phản ứng. Tuy nhiên, áp suất của nguồn "
      "cấp tiêu chuẩn trong trường hợp này là 6 kg/cm², vì nó phải vận hành thiết "
      "bị có công suất lớn hơn đòi hỏi nhiều năng lượng hơn. Đầu ra của bộ điều "
      "khiển thay đổi từ 1 kg/cm² đến 4,5 kg/cm².",
      "In hydraulic controller, on the other hand, the system is operated upon by "
      "non-compressible and non-reactive petroleum fluid. Pressure of the standard "
      "supply system, however, in this case is 6 kg/cm² since it has to operate "
      "higher capacity equipment which require more power for their operations. "
      "The output of the controller varies from 1 kg/cm² to 4.5 kg/cm² for this.")
    P(b, lang,
      "Trong bộ điều khiển điện tử tương tự, các tác động được tạo ra nhờ sự kết "
      "hợp của các phần tử mạch thụ động với bộ khuếch đại thuật toán. Ở đây, cả "
      "đầu vào lẫn đầu ra đều có dạng 4 đến 20 mA một chiều (DC). Nguồn cấp tiêu "
      "chuẩn là 110 V xoay chiều (AC). Ngoài ra, bộ điều khiển còn có thể cung "
      "cấp nguồn 24 V một chiều (DC) cho các bộ phát lắp tại hiện trường.",
      "In analog electronic controller, the actions are generated by means of "
      "combination of passive circuit elements along with operational amplifier. "
      "Here the input as well as output are in the form of 4 to 20 mAmps. D.C. "
      "The standard supply system is 110 volt A.C. In addition to this, the "
      "controller can provide a 24 volt D.C. supply system to the field mounted "
      "transmitters as well.")
    P(b, lang,
      "Mặt khác, trong bộ điều khiển điện tử số, các tác động được thực hiện ở "
      "dạng nhị phân. Một bộ điều khiển số chứa tất cả các phần tử của một máy tính "
      "số, ví dụ hệ thống vi xử lý, hệ thống nhớ, hệ thống vào/ra, v.v. Tất cả các "
      "chỉ thị liên quan đến bộ điều khiển số đều ở dạng thập phân. Điểm tốt nhất "
      "của bộ điều khiển số là tính năng chẩn đoán, bên cạnh nhiều yếu tố quan "
      "trọng khác.",
      "In digital electronic controller, on the other hand, the actions are "
      "performed in binary form. A digital controller incorporates all the "
      "elements of a digital computer e.g. microprocessor system, memory system, "
      "input/output system, etc. All the indications pertaining to digital "
      "controller are in decimal form. The best part of a digital controller is "
      "its diagnoistic feature in addition to its many other important factors.")

    # ------------------------------------------------------------- 2.1 (iv)
    H(b, lang, "(iv) Phần tử điều khiển cuối", "(iv) Final control elements", level=3)
    P(b, lang,
      "Nhiệm vụ của phần tử điều khiển cuối trong hệ thống thiết bị là đưa biến "
      "quá trình trở lại trạng thái ổn định sau một nhiễu động của hệ thống. Nó "
      "được đặt trên đường ống sau bộ phát như thể hiện trong Hình 2.1. Nó cản "
      "trở dòng chảy của chất lỏng quá trình nếu lưu lượng vượt quá giới hạn điểm "
      "cài đặt. Nó cho phép nhiều chất lỏng đi qua hơn nếu lưu lượng có xu hướng "
      "giảm dưới giới hạn cài đặt.",
      "The job of a final control element in an instrumentation system is to bring "
      "back the process variable to stable condition following a system disturbance. "
      "This is placed on the line after the transmitter as shown in Figure 2.1. It "
      "obstructs the flow of process fluid if the flow crosses the set point limit. "
      "It allows more fluid to pass through, if the flow tends to go below the set "
      "limit.")
    P(b, lang,
      "Tùy theo loại dòng chảy cần điều khiển, phần tử điều khiển cuối có thể có "
      "ba loại:",
      "Depending upon the type of flow to be controlled, the final control "
      "elements can be of three types:")
    L(b, lang,
      ["Van điều khiển tác động bằng khí nén",
       "Cửa gió (damper) tác động bằng xi lanh khí nén",
       "Cửa gió (damper) tác động bằng xi lanh thủy lực"],
      ["Pneumatically actuated control valve",
       "Pneumatic cylinder actuated dampers",
       "Hydraulic cylinder actuated dampers"],
      ordered=True)
    P(b, lang,
      "Dựa trên thể tích dòng chảy khối lượng cần điều khiển, phần tử điều khiển "
      "cuối có thể là van hoặc cửa gió (damper). Trong khi van luôn được vận hành "
      "bằng bộ truyền động khí nén, thì cửa gió có thể được vận hành bằng cả xi "
      "lanh khí nén lẫn xi lanh thủy lực. Việc lựa chọn loại phần tử điều khiển "
      "cuối (van hay cửa gió) phụ thuộc vào loại tác động điều khiển mà quá trình "
      "yêu cầu. Đối với các ứng dụng điều khiển quá trình tinh vi, người ta chọn "
      "van điều khiển; còn đối với các ứng dụng điều tiết thô và cả dòng chảy lớn "
      "ở áp suất thấp, cửa gió là lựa chọn hiển nhiên. Để điều khiển tinh hơn, bộ "
      "phận bên trong của van điều khiển (gọi là trim, hay đế và nút van) cần có "
      "hình dạng riêng. Các hình dạng này xác định loại van, ví dụ van tuyến tính, "
      "van phần trăm bằng nhau hoặc van mở nhanh. Các đường cong đặc tính chi "
      "tiết của ba loại van này được thể hiện trong Hình 2.3.",
      "Based on the volume of mass flow to be controlled, the final control "
      "element can be valves or dampers. Whereas valves are invariably pneumatic "
      "actuator operated, dampers are pneumatic as well as hydraulic cylinder "
      "operated. Selection of type of final control elements (valves or dampers) "
      "depends upon the type of control action required by the process. For "
      "sophisticated process control applications, control valves are selected and "
      "for coarse regulating applications and also for large flow at lower "
      "pressure, dampers are the obvious choice. For finer control, the control "
      "valve internals (called trim or seat and plug) should have specific contour. "
      "These contours define the type of valves e.g. linear valve, equal percentage "
      "valve or quick opening valve. The detailed characteristic curves of these "
      "three types of valves have been shown in Figure 2.3.")
    FIG(b, 3, F.fig_f03(), lang)

    # ------------------------------------------------------------- 2.1 (v)
    H(b, lang, "(v) Thiết bị phụ trợ", "(v) Instrument accessories", level=3)
    P(b, lang,
      "Ngoài bốn phần tử cơ bản nêu trên, còn có các phần tử khác gọi là phụ trợ, "
      "nhưng có yêu cầu quan trọng như nhau. Đó là:",
      "In addition to above four basic elements, there are other elements called "
      "accessories, but have the same importance requirementwise. These are:")
    L(b, lang,
      ["Trạm nạp tự động/thủ công", "Thiết bị chuyển mạch dự phòng (bypass)",
       "Rơ le khóa (lock-up relay)", "Bộ đổi dòng sang khí nén",
       "Bộ lọc/điều áp khí (air set)", "Bộ định vị van"],
      ["Auto/manual loading station", "Bypass unit", "Lock-up relay",
       "Current to pneumatic converter", "Air set", "Valve positioner"],
      ordered=True)

    H(b, lang, "(a) Trạm nạp tự động-thủ công",
      "(a) Auto-manual loading station", level=4)
    P(b, lang,
      "Trong điều kiện vận hành bình thường, bộ điều khiển có thể bị hỏng ở chế độ "
      "tự động. Trong trường hợp đó, việc bố trí cho hệ thống vận hành ở chế độ "
      "thủ công trở thành yêu cầu tất yếu. Cách bố trí như vậy được gọi là trạm "
      "nạp tự động/thủ công. Thường thì thiết bị này là bộ phận cố hữu của bộ "
      "điều khiển, nhưng đôi khi nó là một thiết bị độc lập. Khi một bộ điều "
      "khiển tín hiệu được nối tới một số phần tử điều khiển cuối, có thể cần đưa "
      "một số phần tử điều khiển cuối sang điều khiển thủ công trong khi các "
      "phần tử còn lại vẫn ở chế độ tự động. Tác động này không thể thực hiện từ "
      "bộ điều khiển. Vì vậy, cần bổ sung một trạm tự động/thủ công được lắp giữa "
      "bộ điều khiển và phần tử điều khiển cuối. Cách bố trí này cho phép vận hành "
      "độc lập phần tử điều khiển cuối ở bất cứ nơi nào cần thiết. Cách bố trí "
      "được thể hiện trong Hình 2.4.",
      "In normal operating conditions, a controller may fail to operate on "
      "automatic mode. In such circumstances, an arrangement for operation of "
      "system on manual becomes the obvious requirement. Such an arrangement is "
      "known as auto/manual loading station. Normally this unit is an integral "
      "part of a controller, but sometimes it is an independent unit. When a signal "
      "controller is connected to a number of final control elements it may be "
      "required to put some of the final control elements on manual control whereas "
      "others remaining on automatic mode. This action cannot be performed from "
      "controller. Hence, an additional auto/manual station is required to be "
      "incorporated in between the controller and the final control element. This "
      "arrangement allows independent operation of the final control element "
      "wherever required. The arrangement has been shown in Figure 2.4.")
    FIG(b, 4, F.fig_f04(), lang)

    H(b, lang, "(b) Thiết bị chuyển mạch dự phòng",
      "(b) Bypass unit", level=4)
    P(b, lang,
      "Đôi khi bộ điều khiển chính đang vận hành có thể bị hư hỏng và cần bảo trì "
      "ngay lập tức. Trong trường hợp đó, để tiếp tục vận hành không bị gián "
      "đoạn, một bộ điều khiển tương tự làm dự phòng đã được chuẩn bị ngay từ "
      "giai đoạn thiết kế. Để chuyển đổi từ bộ điều khiển chính sang bộ dự phòng, "
      "cần có cơ chế chuyển đổi tại bảng điều khiển. Thiết bị này được gọi là "
      "thiết bị bypass.",
      "Sometimes main control unit, which is in operation, may become faulty and "
      "need immediate maintenance. In such circumstances, for continuance of "
      "uninterrupted operation, a similar control unit as standby is made available "
      "in the design stage itself. For changing over from main control unit to "
      "standby unit, a changeover mechanism is required at the control panel. This "
      "unit is called a bypass unit.")

    H(b, lang, "(c) Bộ lọc/điều áp khí", "(c) Air set", level=4)
    P(b, lang,
      "Bộ lọc/điều áp khí được dùng để cấp khí cho các thiết bị vận hành bằng khí "
      "nén, tức là bộ phát, van điều khiển và cửa gió (damper). Loại khí này gọi "
      "là khí thiết bị. Khí thiết bị phải được lọc trước khi đưa vào thiết bị. "
      "Sau đó, nó phải được điều chỉnh ở áp suất quy định, tức là 1,4 kg/cm² cho "
      "bộ phát và/hoặc 4,5 kg/cm² cho van điều khiển và cửa gió. Bộ lọc/điều áp "
      "khí là sự kết hợp giữa bộ lọc khí và bộ điều áp. Một vòi xả nhỏ được bố trí "
      "để xả bụi và các hạt khác lắng đọng ở đáy bộ lọc/điều áp. Một đồng hồ áp "
      "suất chỉ thị cũng được lắp trên đường đầu ra để quan sát áp suất đã được "
      "điều chỉnh chính xác. Áp suất đầu ra yêu cầu được điều chỉnh bằng núm tròn "
      "nằm ở phía trên của bộ lọc/điều áp. Hệ thống được thể hiện trong Hình 2.5.",
      "An air set is employed for providing air supply to the pneumatically "
      "operated instruments, i.e. transmitters, control valves and dampers. The air "
      "is called instrument air. The instrument air has to be filtered first before "
      "applying to the instrument. Then it has to be regulated/adjusted at the "
      "specified pressure, i.e. 1.4 kg/cm² for transmitter and/or 4.5 kg/cm² for "
      "control valves and dampers. The air set is a combination of air filter and "
      "regulator. A small drain cock is provided for flushing the dust and other "
      "particles settled at the bottom of the air set. An indicating pressure gage "
      "is also installed in the output line for visualizing the correct regulated "
      "pressure. The outlet pressure required is regulated by means of a circular "
      "knob located on the top of the air set. The system has been shown in Figure "
      "2.5.")
    FIG(b, 5, F.fig_f05(), lang)

    H(b, lang, "(d) Bộ định vị van", "(d) Valve positioner", level=4)
    P(b, lang,
      "Nhiệm vụ của bộ định vị van là định vị van điều khiển một cách chính xác "
      "theo tín hiệu điều khiển nhận được từ phần tử điều khiển. Việc định vị van "
      "điều khiển có thể không chính xác do độ trễ (hysteresis) gây ra bởi ma sát "
      "và các đặc tính phi tuyến của bộ truyền động. Đôi khi lực do bộ truyền động "
      "tạo ra có thể không đủ để khắc phục sự cản trở do dòng chất lỏng tạo ra. "
      "Những hạn chế này có thể được giảm thiểu bằng cách dùng bộ định vị van. Nó "
      "cung cấp công suất đầy đủ cho bộ truyền động để định vị đúng cách.",
      "The job of a valve positioner is to position the control valve accurately "
      "with respect to the control signal obtained from the controller element. "
      "The positioning of control valve may not be accurate due to hysteresis which "
      "is caused by friction and non-linear characteristics of the actuator. "
      "Sometimes the force generated by the actuator may not be sufficient to "
      "overcome the opposition created by the fluid flow. These limitations can be "
      "minimized by using a valve positioner. It provides sufficient power to the "
      "actuator for proper positioning.")
    P(b, lang,
      "Một bộ định vị van tạo thành một hệ thống vòng lặp kín. Nó cung cấp lực bổ "
      "sung thông qua một liên kết phản hồi, vốn là yếu tố cần thiết để triển khai "
      "hệ thống vòng lặp kín.",
      "A valve positioner constitutes a closed loop system. It provides additional "
      "force through a feedback linkage which is essential for a closed loop system "
      "implementation.")

    H(b, lang, "(e) Bộ đổi dòng sang khí nén",
      "(e) Current to pneumatic converter", level=4)
    P(b, lang,
      "Bộ điều khiển điện tử cung cấp tín hiệu điều khiển 4 đến 20 mA một chiều "
      "(DC), vốn không thể vận hành van điều khiển khí nén ở dạng nguyên thủy của "
      "nó. Do đó, cần thêm một thiết bị để định vị van. Thiết bị này phải đổi tín "
      "hiệu điện sang dạng khí nén (0,2 đến 1,0 kg/cm²). Thiết bị này gọi là bộ "
      "đổi điện-khí nén. Nó đã được thảo luận chi tiết trong Chương 1.",
      "Electronic controller makes available 4 to 20 mAmps. D.C. control signal "
      "which is incapable of operating a pneumatic control valve in its original "
      "form. Consequently an additional equipment shall be required to position "
      "the valve. This equipment shall convert the electrical signal to pneumatic "
      "(0.2 to 1.0 kg/cm²) form. This equipment is called electro-pneumatic "
      "converter. This has been discussed in Chapter 1 in detail.")

    H(b, lang, "(f) Rơ le khóa", "(f) Lock-up relay", level=4)
    P(b, lang,
      "Trong nhà máy quá trình, khí thiết bị là mạng sống của hệ thống. Sự mất "
      "khí thiết bị có thể gây thiệt hại nghiêm trọng. Dù mọi nỗ lực đều được "
      "thực hiện để tránh mất khí thiết bị, vẫn có thể đưa các thay đổi vào giai "
      "đoạn thiết kế nhằm giảm thiểu mối nguy an toàn do dòng khí thiết bị không "
      "tránh khỏi gây ra.",
      "In process plant, instrument air is the lifeline of the system. The failure "
      "of instrument air can create havoc. While every effort is made to avoid "
      "instrument air failure, changes in design stages can be incorporated to "
      "minimize safety hazard created by unavoidable instrument airflow.")
    P(b, lang,
      "Một tiêu chuẩn thiết kế đề xuất chọn van điều khiển theo kiểu mất khí thì "
      "mở hoặc mất khí thì đóng, cho phù hợp với yêu cầu của quá trình trong điều "
      "kiện mất khí thiết bị. Một quan niệm thiết kế khác quy định lắp rơ le khóa "
      "trên mỗi van điều khiển như vậy có nguy cơ an toàn. Trong điều kiện mất khí "
      "thiết bị, rơ le khóa chặn khí thiết bị đầu vào bên trong bộ truyền động "
      "van, nhờ đó van điều khiển giữ nguyên vị trí hiện tại cho đến khi khí "
      "thiết bị được phục hồi. Các dịch vụ do rơ le khóa cung cấp rất quan trọng "
      "đối với một hệ thống cụ thể mà ở đó yêu cầu các van điều khiển phải luôn "
      "mở trong điều kiện mất khí thiết bị vì lý do an toàn.",
      "One design criterion suggests to select control valve, air fail to open or "
      "air fail to close, to suit the process requirement under instrument air "
      "failure condition. Another design concept dictates to install a lock-up "
      "relay on every such control valve which constitute safety hazard. Under "
      "instrument air failure condition, the lock-up relay blocks the incoming "
      "instrument air inside the valve actuator and thus the control valve remains "
      "in its existing position till resumption of instrument air. The services "
      "provided by the lock-up relay is very important for a particular system "
      "where it is required that control valves should remain open under "
      "instrument air failure condition for safety requirement.")

    return "".join(b)
