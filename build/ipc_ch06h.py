# -*- coding: utf-8 -*-
"""Chapter 6, continuation of section 6.10.1 and section 6.11 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), decoded text lines 12100-12417, PDF pp. 312-319,
printed pp. 300-307.  Module ``ipc_ch06g`` introduces section 6.10 and the
Figure 6.24 block diagram; this module continues section 6.10.1 with the
measurement unit, controller and feedback operation, then covers section 6.11
on three-element control and the concept of feed forward, including the boiler
drum level example, Figures 6.25 and 6.26, dynamic compensation, the flow
balance equation, and the role of feedback inside a cascade loop.

The real figures are supplied by the ``ipcfig6_c`` supplier, which registers
``fig_f25`` and ``fig_f26`` before this module is imported.  Small
non-overwriting fallbacks are installed only while that supplier is absent.
There are no numbered equations in this span and no tables to reproduce.
"""

import ipcfig6 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _stub_figure(n, title_vi, title_en, aria_vi, aria_en):
    """A minimal, XML-valid fallback used only if the supplier is not ready."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
        'viewBox="0 0 680 250">'
        '<rect width="680" height="250" fill="#ffffff"/>'
        '<rect x="195" y="70" width="290" height="86" rx="6" fill="#eef3fb" '
        'stroke="#1f3a5f" stroke-width="1.2"/>'
        '<text x="340" y="105" text-anchor="middle" font-size="11" '
        'fill="#1f3a5f">Figure 6.%d</text>'
        '<text x="340" y="127" text-anchor="middle" font-size="8.5" '
        'fill="#1f3a5f">%s</text>'
        '<text x="340" y="242" text-anchor="middle" font-size="6.4" '
        'fill="#888888">Hinh 6.%d   /   Figure 6.%d</text>'
        '</svg>'
    ) % (n, title_en, n, n)
    return (svg,
            "Hình 6.%d · %s" % (n, title_vi),
            "Figure 6.%d · %s" % (n, title_en),
            aria_vi, aria_en)


def _stub_f25():
    return _stub_figure(
        25, "Điều khiển ba phần tử mức trống nồi hơi",
        "Three-element boiler drum level control",
        "Sơ đồ điều khiển mức trống nồi hơi với vòng đón đầu và hai vòng phản hồi",
        "Boiler drum level loop with a feed-forward path and two feedback loops")


def _stub_f26():
    return _stub_figure(
        26, "Vòng điều khiển với bộ điều khiển kép đa chức năng",
        "Control loop with a multifunction dual controller",
        "Vòng điều khiển dùng bộ điều khiển kép đa chức năng và ba bộ phát thông minh",
        "Control loop using a multifunction dual controller and three smart transmitters")


if not hasattr(F, "fig_f25"):
    F.fig_f25 = _stub_f25
if not hasattr(F, "fig_f26"):
    F.fig_f26 = _stub_f26


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ------------------------------------- 6.10.1 (continued from module g)

    P(b, lang,
      "Bộ phận đo gồm phần tử cảm biến sơ cấp và bộ phát tín hiệu. Bộ phận kết "
      "hợp này phát hiện sự thay đổi của biến quá trình cần điều khiển, ví dụ "
      "nhiệt độ, áp suất, mức, lưu lượng, v.v., và tạo ra đầu ra điện tỷ lệ "
      "trong dải 4 đến 20 mA một chiều. Bộ cảm biến và bộ phát được lắp gần "
      "quá trình trong môi trường khắc nghiệt, còn bộ điều khiển được lắp "
      "trong phòng điều khiển trung tâm. Tín hiệu biến quá trình được truyền "
      "đến phòng điều khiển bằng cáp phù hợp. Bộ điều khiển có bộ chỉ thị "
      "quá trình tích hợp, hiển thị giá trị của biến quá trình.",
      "The measurement unit consists of a primary sensor element along with a "
      "signal transmitter unit. The combined unit of sensor and transmitter "
      "detects the change in the process variable to be controlled, for "
      "example temperature, pressure, level, flow, etc., and produces a "
      "proportional electrical output in the range of 4 to 20 mA D.C. The "
      "sensor and transmitter unit is installed close to the process in a "
      "harsh atmosphere and the controller is installed inside the central "
      "control room. The process variable signal is transmitted all the way "
      "to the control room by suitable cabling. The controller has an in-built "
      "process indication unit, which indicates the value of the process "
      "variable.")

    P(b, lang,
      "Như quan sát trong sơ đồ, bộ điều khiển gồm bộ phát hiện sai số và bộ "
      "khuếch đại. Bộ phát hiện sai số so sánh giá trị biến quá trình với giá "
      "trị đặt do người vận hành thiết lập và tạo ra tín hiệu sai số tỷ lệ "
      "với hiệu giữa giá trị quá trình và giá trị đặt. Bộ khuếch đại khuếch đại "
      "tín hiệu sai số đến mức có thể tác động phần tử điều khiển cuối cùng. "
      "Đầu ra bộ điều khiển sau khuếch đại nằm trong dải 4 đến 20 mA một "
      "chiều, điều khiển bộ định vị van điện-khí nén, lần lượt tác động phần "
      "tử điều khiển cuối cùng.",
      "As observed in the diagram, the controller unit consists of an error "
      "detector and an amplifier unit. The error detector compares the value "
      "of the process variable with the set value set by the operator and an "
      "error signal is produced, proportional to the difference between the "
      "process value and the set value. The amplifier unit amplifies this "
      "error signal up to a value where it is capable of actuating a final "
      "control element. The controller output after amplification is in the "
      "range of 4 to 20 mA D.C., which operates an electro-pneumatic valve "
      "positioner, which in turn operates the final control element.")

    P(b, lang,
      "Phần tử điều khiển cuối cùng, lại được lắp gần quá trình tại hiện "
      "trường, thay đổi độ mở của nó để đưa biến quá trình về lại giá trị đặt "
      "ban đầu.",
      "The final control element, again installed near the process in the "
      "field, manipulates its opening to bring the process variable back to "
      "its original set value.")

    P(b, lang,
      "Để hiểu hoạt động của hệ thống điều khiển phản hồi điển hình, giả sử "
      "tại một thời điểm nhất định quá trình đang trong điều kiện bình thường "
      "và giá trị biến quá trình bằng đúng giá trị đặt. Nếu xảy ra thay đổi tải "
      "vì bất kỳ lý do gì, điều kiện điều khiển bình thường bị xáo trộn, biến "
      "quá trình đổi giá trị và phát sinh tín hiệu sai số. Sau khi được bộ phát "
      "hiện sai số phát hiện, sai số được đưa tới bộ khuếch đại, tạo ra đầu ra "
      "bộ điều khiển. Đầu ra này tác động phần tử điều khiển cuối cùng để đưa "
      "biến quá trình về giá trị đặt. Quá trình này tiếp diễn không gián đoạn "
      "chừng nào sai số còn tồn tại và cho đến khi biến quá trình trở về giá "
      "trị đặt. Cần lưu ý rằng bộ điều khiển chỉ hành động khi có sai số; nó "
      "không có khả năng dự báo hoạt động tương lai của hệ thống điều khiển. "
      "Mục đích của hệ thống này là giảm thiểu sai số giữa giá trị biến quá "
      "trình và giá trị đặt nhanh nhất có thể với mức dao động nhỏ nhất.",
      "To understand the operation of a typical feedback control system, let "
      "us assume that at a particular instant the process system is under "
      "normal condition and the value of the process variable equals exactly "
      "the set value. Now, if a load change occurs for any reason, the normal "
      "control condition gets disturbed and the process variable changes its "
      "value, resulting in an error signal. The error, after detection by the "
      "error detector, is fed to the amplifier unit, which produces the "
      "controller output. This output operates the final control element to "
      "bring the process variable back to its set value. This operation "
      "continues uninterruptedly till the error exists and the process "
      "variable comes back to the set value. It is to be noted that the "
      "controller comes into action only when there is an error. It is "
      "incapable of predicting the future action of the control system. The "
      "purpose of this control system is to minimise the error between the "
      "process variable and the set value as quickly as possible with a "
      "minimum amount of cycling, that is fluctuation.")

    # ------------------------------------------------------------- 6.11
    H(b, lang,
      "6.11 Điều khiển ba phần tử (khái niệm đón đầu)",
      "6.11 Three-element control (concept of feed forward)", level=2)

    P(b, lang,
      "Hệ thống điều khiển ba phần tử là trường hợp đặc biệt của hệ thống "
      "điều khiển đa phần tử, trong đó nhiều hơn một biến quá trình ảnh hưởng "
      "đến chiến lược điều khiển. Hệ thống này cũng được gọi là hệ thống điều "
      "khiển đón đầu-phản hồi xếp tầng. Thực tế, hệ thống gồm hai bộ điều "
      "khiển hoặc hai kênh điều khiển độc lập nối với nhau theo kiểu xếp "
      "tầng. Một trong hai bộ gọi là bộ điều khiển chính (master), bộ kia là "
      "bộ điều khiển phụ (slave). Hệ thống có một vòng đón đầu, trong đó thay "
      "đổi tải được đưa đón đầu như chỉ số chính để thay đổi biến quá trình "
      "chính nhằm điều khiển quá trình. Hệ thống cũng có hai vòng phản hồi "
      "giám sát độ chính xác của vòng đón đầu, vì hiệu quả của vòng đón đầu "
      "phụ thuộc hoàn toàn vào độ chính xác của phép đo thay đổi tải và của "
      "biến quá trình bị ảnh hưởng.",
      "A three-element control system is a special case of a multi-element "
      "control system where more than one process variable influences the "
      "control strategy. This can also be called a cascaded feed-forward-"
      "feedback control system. The system, in fact, incorporates two "
      "independent controllers or controller files connected together in a "
      "cascade fashion. One of the two controllers is known as the primary or "
      "master controller and the other as the secondary or slave controller. "
      "The system has a feed-forward loop where the load change is fed forward "
      "as the primary index to change the main process variable so as to "
      "control the process. It also has two feedback loops, which monitor the "
      "accuracy of the feed-forward loop, because the effectiveness of a "
      "feed-forward loop depends completely on the accuracy of measurement of "
      "the load change as well as of the affected process variable.")

    P(b, lang,
      "Một vòng phản hồi thuần túy cũng có những hạn chế riêng như sau:",
      "A pure feedback loop also has its own limitations, which are as follows:")

    L(b, lang,
      ["Phải luôn tồn tại một sai số đo được giữa biến quá trình và giá trị "
       "đặt để khởi phát hành động khôi phục, do đó không thể đạt được điều "
       "khiển hoàn hảo. Đó là bản chất của hệ thống phản hồi.",
       "Vòng phản hồi giải quyết bài toán điều khiển bằng phương pháp thử và "
       "sai, vì nó cứ thay đổi đầu ra cho đến khi giá trị biến quá trình và "
       "giá trị đặt bằng nhau. Bộ điều khiển phản hồi không thể biết trước "
       "đầu ra của nó cho một tập điều kiện quá trình đã cho.",
       "Mọi vòng điều khiển phản hồi đều có chu kỳ tự nhiên đặc trưng. Nếu "
       "một nhiễu bắt đầu trong khoảng thời gian ngắn hơn khoảng ba chu kỳ, "
       "không bao giờ đạt được trạng thái ổn định."],
      ["A measurable amount of error between the process variable and the set "
       "value must be present at all times to initiate a restoring action, "
       "hence a perfect control cannot be achieved. This is the nature of a "
       "feedback system.",
       "A feedback loop solves its control problem by trial and error because "
       "it goes on changing the output until the value of the process variable "
       "and the set value are in agreement. It is not possible for a feedback "
       "controller to know its output value for any given set of process "
       "conditions.",
       "All feedback control loops have a characteristic natural period. "
       "Should a disturbance start at an interval less than about three "
       "periods, no steady-state condition can ever be obtained."],
      ordered=True)

    P(b, lang,
      "Trong hệ thống điều khiển xếp tầng, phần tử điều khiển cuối cùng được "
      "tác động thông qua một biến điều khiển trung gian, giá trị thực của "
      "biến này phụ thuộc vào giá trị của biến quá trình chính. Đầu ra của bộ "
      "điều khiển chính được dùng để thay đổi giá trị đặt của bộ điều khiển "
      "phụ. Bộ điều khiển chính có giá trị đặt độc lập. Cả hai bộ điều khiển "
      "đều có đầu vào là tín hiệu đo hoặc biến quá trình, nhưng chỉ bộ điều "
      "khiển phụ cung cấp đầu ra để tác động phần tử điều khiển cuối cùng.",
      "In a cascaded control system, the final control element is operated "
      "through an intermediate controlled variable, the actual value of which "
      "depends upon the value of the primary process variable. The output of "
      "the primary controller is used to manipulate the set value of the "
      "secondary controller. The primary controller has an independent set "
      "value. Both controllers have measurement or process variable inputs, "
      "but it is only the secondary controller which provides the output for "
      "the operation of the final control element.")

    P(b, lang,
      "Hệ thống điều khiển xếp tầng có nhiều ưu điểm như sau:",
      "The cascaded control system enjoys many advantages, which are as follows:")

    L(b, lang,
      ["Các nhiễu phát sinh trong vòng phụ, do bộ điều khiển phụ điều khiển, "
       "được chính bộ điều khiển phụ hiệu chỉnh rất tốt trước khi có xu hướng "
       "ảnh hưởng đến biến quá trình chính.",
       "Vòng phụ làm giảm hiệu quả trễ pha tồn tại trong phần phụ của quá "
       "trình, làm tăng rõ rệt tốc độ đáp ứng của vòng điều khiển chính.",
       "Các biến động độ lợi trong phần phụ của quá trình được khắc phục ngay "
       "trong vòng của chính nó.",
       "Vòng điều khiển phụ hầu như luôn cho phép bộ điều khiển chính thao "
       "tác chính xác biến phụ."],
      ["Disturbances created within the secondary loop, operated by the "
       "secondary controller, are very well corrected by the secondary "
       "controller itself before they tend to influence the primary process "
       "variable.",
       "The secondary loop efficiently reduces the phase lag that exists in "
       "the secondary part of the process, resulting in a marked improvement "
       "in the speed of response of the primary control loop.",
       "Variations in gain existing in the secondary part of the process are "
       "overcome within its own loop.",
       "The secondary control loop allows almost always an exact manipulation "
       "of the secondary variable by the primary controller."],
      ordered=True)

    P(b, lang,
      "Trong điều khiển đón đầu, các yếu tố chính ảnh hưởng đến điều kiện quá "
      "trình được đo và, đối chiếu với giá trị đặt, được dùng để tính toán "
      "đầu ra chính xác nhằm đáp ứng đúng điều kiện. Bất cứ khi nào một nhiễu "
      "xuất hiện, hành động hiệu chỉnh gần như lập tức được khởi động để triệt "
      "tiêu nhiễu trước khi nó ảnh hưởng đến biến quá trình chính. Thực tế, "
      "đón đầu có khả năng điều khiển hoàn hảo; bất chấp độ khó của quá trình, "
      "hiệu năng của nó có thể bị ảnh hưởng lớn bởi độ chính xác của phép đo "
      "các biến. Khi vận hành, hệ thống điều khiển đón đầu liên tục cân bằng "
      "giữa đầu vào thô của quá trình và các biến động tải. Vì vậy, các phép "
      "đo biến quá trình cần thiết liên quan tự nhiên đến phương trình cân "
      "bằng vật chất và năng lượng, và các biến quá trình chính được điều "
      "chỉnh tương ứng.",
      "In feed-forward control the main factors influencing the process "
      "conditions are measured and, with respect to the set value, are used "
      "to calculate the exact output to meet the exact condition. Whenever a "
      "disturbance is initiated, corrective action starts almost immediately "
      "in order to cancel it before it affects the primary process variable. "
      "In fact, feed forward is capable of perfect control; notwithstanding "
      "the difficulty of the process, its performance can be greatly affected "
      "by the accuracy of measurement variables. While in operation, a feed-"
      "forward control system continuously makes the balance between the raw "
      "inputs to the process and the load variations. Therefore, the "
      "measurements of process variables required by the control system are "
      "necessarily related to material and energy balance equations, and the "
      "main process variables are regulated accordingly.")

    P(b, lang,
      "Đặc tính cố hữu của mọi hệ thống quá trình là một lượng vật chất và "
      "năng lượng nhất thiết được tích trữ bên trong quá trình, và hàm lượng "
      "này thay đổi khi đi từ pha này sang pha khác. Sự thay đổi đó có nghĩa "
      "là giải phóng hoặc hấp thụ tạm thời vật chất hoặc năng lượng, cuối cùng "
      "tạo ra hiệu ứng quá độ trên biến quá trình chính nếu không được tính "
      "đến thích hợp trong phép tính cân bằng vật chất và năng lượng ảnh hưởng "
      "đến vòng điều khiển. Thông thường, sau thay đổi tải là một giai đoạn "
      "mất cân bằng động, biểu hiện như sai số quá độ. Trước khi tăng tải cho "
      "quá trình, việc cuối cùng đòi hỏi tăng tốc độ truyền vật chất và năng "
      "lượng, mức hiện có của vật chất và năng lượng phải được nâng lên trước.",
      "It is an inherent characteristic of any process system that some "
      "material and energy are inevitably stored within the process, and the "
      "content varies in passing from one phase to another. This variation "
      "means a momentary release or absorption of material or energy, which "
      "ultimately produces a transient effect in the main process variable "
      "unless it is suitably accounted for in the material and energy balance "
      "calculation affecting the control loop. Normally, a load change is "
      "followed by a period of dynamic imbalance and appears as transient "
      "error. Before increasing the load on the process, which ultimately "
      "requires an increase in the rate of material and energy transfer, the "
      "existing level of material and energy must first be raised.")

    P(b, lang,
      "Nếu không có nỗ lực bổ sung thêm vật chất và năng lượng cho hệ thống, "
      "chính hệ thống sẽ tạm thời nâng mức của nó, biểu hiện bằng sự giảm tạm "
      "thời lượng vật chất và năng lượng rút ra khỏi hệ thống. Kỹ thuật hiệu "
      "chỉnh hiệu ứng quá độ này gọi là bù động, có thể thực hiện rất thành "
      "công bằng bộ đón đầu-trễ. Bộ này có khả năng cung cấp nhiều hơn hoặc "
      "ít hơn lượng vật chất hoặc năng lượng cho quá trình để nâng hoặc hạ thế "
      "năng của quá trình trong lúc thay đổi tải. Yêu cầu nghiêm ngặt nhất đặt "
      "ra cho bộ đón đầu-trễ là độ chính xác trạng thái ổn định. Nếu nó không "
      "lặp lại chính xác hành vi của mình trong giai đoạn ổn định ngay sau một "
      "đáp ứng quá độ, bộ đón đầu-trễ sẽ làm suy giảm hiệu năng của vòng đón "
      "đầu; khi đó tính tuyến tính, khả năng lặp lại và không có trễ đàn hồi "
      "có thể không đạt được.",
      "If no attempt is initiated to add an extra amount of material and "
      "energy to the system, it will itself raise its level temporarily, which "
      "will be reflected as a temporary reduction in the material and energy "
      "withdrawal from the system. The technique of correction of this "
      "transient effect is known as dynamic compensation, which can be "
      "accomplished quite successfully by use of a lead-lag unit. The lead-lag "
      "unit is capable of delivering more as well as less material or energy "
      "to the process to raise and lower its potential during a load change. "
      "The most stringent specification imposed upon a lead-lag unit is its "
      "steady-state accuracy. If it does not repeat its behaviour accurately "
      "during the steady-state condition immediately after a transient "
      "response, the lead-lag unit will degrade the performance of the feed-"
      "forward loop; as a result, linearity, repeatability and freedom from "
      "hysteresis may not remain achievable.")

    P(b, lang,
      "Xét đến giới hạn của điều khiển đón đầu do sai số trong đo hoặc tính "
      "toán, vai trò của các vòng phản hồi trở nên mang tính quyết định theo "
      "nghĩa chúng có khả năng loại bỏ hoàn toàn độ lệch do điều khiển đón đầu "
      "gây ra. Trong thực tế, phần lớn tải điều khiển do chính hệ thống đón "
      "đầu đảm nhận, nhưng hệ thống vẫn rất cần phản hồi trong quá trình "
      "thực thi.",
      "As far as the limitation on feed-forward control due to error in "
      "measurement or computation is concerned, the role of feedback control "
      "loops becomes deterministic in the sense that it is capable of removing "
      "completely the offset caused by the feed-forward control. In practice, "
      "however, most of the control load is carried by the feed-forward system "
      "itself, but feedback is still very much required by the system in its "
      "execution.")

    P(b, lang,
      "Chúng ta có thể xét một ví dụ thực tế về điều khiển ba phần tử để điều "
      "khiển mức trống nồi hơi trong một nhà máy phát điện. Trong nhà máy, đun "
      "sôi nước để tạo hơi là quá trình quan trọng. Điều khiển mức là chức "
      "năng chính trong vận hành nồi hơi hoặc bất kỳ nhà máy tạo hơi nào. Hơi "
      "được dùng để dẫn động các máy nguyên sơ, ví dụ tuabin hơi. Hơi được tạo "
      "ở áp suất và nhiệt độ dưới tới hạn, nhờ đó một mặt phân cách rõ ràng "
      "giữa nước và hơi được xác lập. Mặt phân cách này nằm trong trống nồi "
      "hơi gần đỉnh vỏ nồi hơi. Chức năng chính của trống là cung cấp diện "
      "tích bề mặt và thể tích bên trong để tách hơi ra khỏi nước.",
      "We can consider a practical example of three-element control for "
      "controlling boiler drum level in a power generating station. In a power "
      "station, boiling water to raise steam constitutes an important process. "
      "Control of level is a major function in the operation of a boiler or "
      "any steam generation plant. Steam is used to drive the prime movers, "
      "for example steam turbines. Steam is produced at subcritical pressure "
      "and temperature and thereby a distinct water-steam interface is "
      "defined. This interface is realised in the boiler drum located near the "
      "top of the boiler housing. The main function of the drum is to provide "
      "the surface area as well as the volume inside for carrying out "
      "separation of steam from water.")

    P(b, lang,
      "Các chức năng phụ của trống là:",
      "The secondary functions of the drum are:")

    L(b, lang,
      ["Làm sạch hơi bằng cách tẩy các giọt nước bị cuốn theo và các chất rắn "
       "hòa tan.",
       "Cung cấp không gian cho xử lý nước bên trong và kết nối xả đáy để loại "
       "bỏ nồng độ tạp chất trong nước cấp nồi hơi.",
       "Cung cấp chỗ để thêm nước cấp nồi hơi và kết nối tuần hoàn nước tới "
       "các phần khác nhau của ống nước."],
      ["It purifies the steam by scrubbing the entrained water droplets as "
       "well as dissolved solids.",
       "It provides space for internal water treatment and a blowdown "
       "connection for removal of impurity concentration in the boiler feed "
       "water.",
       "It provides a place for addition of boiler feed water and also a "
       "connection for recirculation of water to different parts of the water "
       "tubes."],
      ordered=True)

    P(b, lang,
      "Nhờ các chức năng này của trống nồi hơi mà mức của nó là biến quá trình "
      "quan trọng. Nếu mức quá cao, nước sẽ tràn vào thiết bị làm sạch hơi; "
      "nước cùng tạp chất bị cuốn theo vào hơi, cuối cùng ảnh hưởng đến cánh "
      "tuabin và gây thêm các vấn đề xói mòn. Nếu mức quá thấp, xử lý nước "
      "không đầy đủ và tuần hoàn nước không đủ; về lâu dài đó là nguyên nhân "
      "gây hỏng ống nồi hơi do quá nhiệt khi thiếu nước trên bề mặt đun sôi. "
      "Thông thường mức trống được giữ trong vòng 50 mm so với giá trị đặt, "
      "với một số dung sai cho các xáo trộn tạm thời.",
      "Due to these functions carried out by the boiler drum, its level is a "
      "critical process variable. If the level is very high, this results in "
      "flooding of water into the steam purification equipment; water along "
      "with impurities is carried over to the steam, which ultimately affects "
      "the turbine blades in addition to other erosion problems. If the level "
      "is very low, this results in deficient water treatment and insufficient "
      "water recirculation functions. In the long run these are the reasons "
      "for boiler tube failure due to overheating in the absence of water on "
      "the boiling surfaces. Normally the drum level is held within 50 mm of "
      "the set value with some tolerance for temporary upsets.")

    P(b, lang,
      "Dù chức năng điều khiển mức được coi là đơn giản, nó trở nên khó khi "
      "chất lỏng đạt đến trạng thái bão hòa. Trong điều kiện nước sôi, các bọt "
      "hơi tồn tại bên dưới mặt phân cách hơi-nước và chiếm thể tích của nước. "
      "Quá trình trở nên động vì có sự chuyển động của bọt đi lên trong các "
      "ống cho đến trống. Trong điều kiện sôi ổn định, vị trí của mặt phân "
      "cách là chỉ số suy luận hợp lý về lượng nước trong ống. Trong điều "
      "kiện quá độ, tức là thay đổi áp suất trong trống và ảnh hưởng của nó "
      "tới mặt phân cách, hoặc thay đổi đầu vào nhiệt, tình hình hoàn toàn "
      "khác. Khi áp suất thay đổi, bọt sẽ xẹp hoặc sinh ra vì khối nước đạt "
      "đến cân bằng nhiệt độ ở áp suất làm việc mới; thể tích của bọt hiện có "
      "cũng thay đổi. Thay đổi đầu vào nhiệt làm thay đổi tốc độ tạo bọt, dẫn "
      "đến thay đổi lưu lượng bọt đi lên ống và lượng nước được nâng và đẩy "
      "lên ống. Tất cả các hiệu ứng này dịch chuyển mức mặt phân cách, do đó "
      "phép đo mức trong điều kiện này vô nghĩa cho đến khi nhiệt được phân "
      "bố đúng khắp hệ thống.",
      "Although the level control function is understood to be simple, it "
      "becomes difficult when the liquid reaches its saturation. Under boiling "
      "conditions of water, steam bubbles exist below the steam-water "
      "interface and these bubbles, having volume, displace water. The process "
      "becomes dynamic because there is movement of bubbles up the tubes all "
      "the way up to the drum. In steady-state boiling conditions the location "
      "of the steam-water interface represents a reasonable inferential index "
      "of the quantity of water inside the tube. Under transient conditions, "
      "that is a change in pressure inside the drum and its effect on the "
      "interface, or a change in heat input, the situation becomes completely "
      "different. On a pressure change, bubbles will collapse or will be "
      "generated since the water mass reaches temperature equilibrium at the "
      "new operating pressure; there is also a change in the volume of existing "
      "bubbles. A change in heat input changes the rate of bubble formation, "
      "which changes the bubble traffic up the tubes and also the quantity of "
      "water supported and pushed up the tubes. All these effects shift the "
      "steam-water interface level, and therefore level measurement in this "
      "condition is meaningless until the heat is properly distributed "
      "throughout.")

    P(b, lang,
      "Về thay đổi tải, trong quá trình này chỉ có hai dạng: thay đổi nhu cầu "
      "hơi và thay đổi đầu vào nhiệt. Các thay đổi tải khác như thay đổi nhiệt "
      "độ nước cấp và thay đổi tốc độ xả đáy ít quan trọng hơn và không được "
      "xét. Nếu xét ảnh hưởng của thay đổi tải đến mức trống đối với nhu cầu "
      "hơi, ta thấy ngay áp suất trên mặt phân cách giảm. Do giảm áp suất, một "
      "lượng nước nhất định bốc thành bọt hơi với thể tích bọt hiện có tăng "
      "lên. Đồng thời hệ thống điều khiển áp suất bắt đầu thêm nhiên liệu, "
      "làm tăng đầu vào nhiệt và tốc độ tạo hơi. Các hiệu ứng này cùng nhau "
      "tạo ra trạng thái dâng lên của mặt phân cách, gọi là SWELL, tức phình "
      "mức. Tương tự, khi nhu cầu giảm, áp suất tăng, bọt xẹp lại, thể tích bọt "
      "giảm; hệ thống điều khiển áp suất giảm nhiên liệu, làm giảm đầu vào "
      "nhiệt và tốc độ tạo hơi. Các hiệu ứng này tạo ra sự sụt giảm mức, gọi "
      "là SHRINK, tức co mức. Phình và co là các hiệu ứng tiêu cực, không hợp "
      "lý theo chiều của thay đổi tải, nhưng là các trạng thái tạm thời và "
      "biến mất ngay khi phân bố nhiệt bình thường qua nước và hơi được thiết "
      "lập và chế độ sôi ổn định trở lại. Tuy nhiên, chúng có thể gây quá nhiệt "
      "hoặc thiếu nhiệt nghiêm trọng.",
      "As far as load changes are concerned, there can be only two forms of "
      "load change in this process: a change in steam demand and a change in "
      "heat input. Other load changes in terms of change in feed-water "
      "temperature and change in the rate of blowdown are of less importance "
      "and are not considered. If we examine the effect of a load change on "
      "drum level with respect to a change in steam demand, we immediately "
      "find that the pressure over the interface decreases. As a result of the "
      "decrease in pressure, a certain amount of water flashes into steam "
      "bubbles with a consequent increase in the volume of existing bubbles. "
      "Simultaneously the pressure control system starts adding more fuel, "
      "resulting in increased heat input and increased steaming rate. These "
      "effects altogether tend to produce a surge condition on the interface, "
      "which is known as SWELL. Similarly, on a decrease in demand, pressure "
      "increases and bubbles collapse; the volume of existing bubbles "
      "decreases. As the pressure control system decreases the fuel supply, "
      "the heat input and consequently the steaming rate decrease. These "
      "effects tend to produce a fall in level, which is known as SHRINK. "
      "Swell and shrink are negative effects which are not logical according "
      "to load changes, but they are temporary conditions and disappear at "
      "once as the normal heat distribution through water and vapour is "
      "established and a more steady boiling condition returns. However, they "
      "can result in severe over-heating and under-heating.")

    P(b, lang,
      "Mục tiêu chính của hệ thống điều khiển mức trống là duy trì mặt phân "
      "cách nước-hơi tại hoặc gần vị trí quy định bên trong trống trong mọi "
      "điều kiện. Tuy nhiên, mức chỉ là biến vận hành và không phải là thước "
      "đo trực tiếp của thay đổi tải. Nhưng vì thay đổi mức do mất cân bằng "
      "dòng khối lượng, mục tiêu thiết kế của hệ thống điều khiển là cung cấp "
      "điều khiển cân bằng khối lượng, tức là hơi chảy ra phải được bù bằng "
      "dòng nước cấp vào nồi hơi. Cân bằng khối lượng chính xác được thể hiện "
      "qua mức trống. Điều khiển này thực hiện bằng cách thay đổi lưu lượng "
      "nước cấp dựa trên thay đổi lưu lượng hơi.",
      "The main objective of the drum level control system is to maintain the "
      "water-system interface at or near the specified location inside the "
      "drum in all conditions. However, level is an operational variable only "
      "and is not a direct measure of a load change. But since a level change "
      "is caused by mass flow unbalance, the design objective for the control "
      "system is to provide control of mass balance, that is the steam flowing "
      "out should be supplemented by feed-water flow into the boiler. The "
      "exact mass balance is indicated by the drum level. This control is "
      "accomplished by changing the feed-water flow on the basis of the steam "
      "flow change.")

    P(b, lang,
      "Cần có sự cân bằng thích hợp giữa tải hơi và lưu lượng nước cấp nồi hơi "
      "vì dao động lưu lượng nước cấp ảnh hưởng đến điều khiển nhiệt độ hơi "
      "cũng như bộ gia nhiệt và bơm nước cấp. Cần lưu ý rằng tồn tại sai số "
      "tĩnh cố hữu và quan hệ pha trong quá độ giữa lưu lượng hơi và lưu lượng "
      "nước cấp. Hệ thống điều khiển mức trống được đề xuất cần bù cho sai số "
      "này cũng như mọi dòng không được tính đến khác như xả đáy và rò rỉ.",
      "A proper balance between the steam load and the boiler feed-water flow "
      "is required because fluctuation in feed-water flow affects the steam "
      "temperature control as well as the feed-water heaters and pumps. It is "
      "to be noted that an inherent static error and a phasing relationship "
      "exist during transients between steam flow and feed-water flow. The "
      "proposed drum level control system is required to compensate for this "
      "error and also for any other unaccounted flow such as blowdown and "
      "leakages.")

    P(b, lang,
      "Điều khiển ba phần tử cho mức trống nồi hơi xét đến ba biến: lưu lượng "
      "hơi, lưu lượng nước cấp và mức trống. Phần tử điều khiển cuối cùng, tức "
      "là van nước cấp, điều khiển dòng nước cấp và chịu ảnh hưởng của cả ba "
      "biến. Bộ điều khiển chính là bộ điều khiển mức trống, với tín hiệu đầu "
      "vào là biến mức trống. Giá trị đặt độc lập được thiết lập ngay trong "
      "bộ điều khiển này. Bộ điều khiển phụ được nối xếp tầng với bộ điều "
      "khiển chính. Giá trị đặt của nó được thiết lập từ xa, tức là đầu ra của "
      "bộ điều khiển chính kết hợp với đầu ra của máy tính lưu lượng "
      "hơi/nước cấp trở thành giá trị đặt cho bộ điều khiển phụ. Lưu lượng "
      "nước cấp trở thành biến quá trình của bộ điều khiển phụ. Vòng đón đầu "
      "dạng lưu lượng hơi-lưu lượng nước cấp được dùng để thay đổi lưu lượng "
      "nước cấp vào hệ thống. Vì vậy, thay đổi tải dạng thay đổi lưu lượng hơi "
      "được đưa đón đầu như chỉ số chính để tác động đến lưu lượng nước cấp. "
      "Hai vòng phản hồi ở đây là bộ điều khiển mức trống và bộ điều khiển "
      "lưu lượng nước cấp. Các vòng phản hồi giám sát độ chính xác của vòng đón "
      "đầu và cung cấp điều khiển cuối cùng cho mặt phân cách nước-hơi bên "
      "trong trống bằng cách tác động van điều khiển nước cấp, như Hình 6.25.",
      "The three-element control for boiler drum level takes into account "
      "three variables: steam flow, feed-water flow and the drum level. The "
      "final control element, that is the feed-water valve, controls the flow "
      "of feed-water and is influenced by all three variables. The primary "
      "controller is the drum level controller, whose signal input is the drum "
      "level variable. The independent set variable is set in this controller "
      "itself. The secondary controller is connected in cascade with the "
      "primary controller. Its set value is set remotely, that is the output "
      "of the primary controller in combination with the steam flow/feed-water "
      "flow computer output becomes the set value for the secondary controller. "
      "The flow of feed-water becomes the process variable for the secondary "
      "controller. The feed-forward loop in the form of steam flow-feed-water "
      "flow is used to change the flow of feed-water to the system. For this, "
      "the load change in the form of a steam flow change is fed forward as the "
      "primary index to affect the feed-water flow. The two feedback control "
      "loops here are the drum level controller and the feed-water flow "
      "controller. The feedback loops monitor the accuracy of the feed-forward "
      "loop and provide final control to the water-steam interface inside the "
      "drum by actuating the feed-water control valve, as shown in Figure 6.25.")

    FIG(b, 25, F.fig_f25(), lang)

    P(b, lang,
      "Bộ phát lưu lượng hơi đo thay đổi tải dưới dạng lưu lượng hơi, sau khi "
      "khai căn bậc hai tín hiệu được gửi đến máy tính lưu lượng nước cấp. "
      "Khai căn bậc hai quan trọng vì tín hiệu lưu lượng phi tuyến "
      "(Lưu lượng ∝ √Chênh áp). Mức trống tương tự được đo và tín hiệu truyền "
      "tới bộ điều khiển chính như biến quá trình, nơi tín hiệu được so sánh "
      "với giá trị đặt. Hiệu chỉnh do bộ điều khiển chính tạo ra được gửi đến "
      "máy tính lưu lượng nước cấp. Máy tính này kết hợp tín hiệu lưu lượng hơi "
      "như tín hiệu tải và tín hiệu đầu ra của bộ điều khiển chính, tạo ra "
      "tín hiệu điểm đặt từ xa cần thiết cho bộ điều khiển phụ.",
      "The steam flow transmitter measures the load change in the form of "
      "steam flow and, after getting it square-rooted, sends it to the feed-"
      "water flow computer. Square-root extraction is important since flow "
      "signals are non-linear (Flow ∝ √Differential Pressure). The drum level "
      "is similarly measured and the signal is transmitted to the primary "
      "controller as the process variable, where it is compared with respect "
      "to the set value. The correction generated by the primary controller is "
      "sent to the feed-water flow computer. The feed-water flow computer "
      "combines the steam flow signal, as the load signal, and the primary "
      "controller output signal and generates the necessary remote set point "
      "signal for the secondary controller.")

    P(b, lang,
      "Do hằng số thời gian nhỏ của trống nồi hơi, điều khiển mức chịu ảnh "
      "hưởng của các thay đổi tải nhanh. Ngoài ra, do độ nhiễu loạn trong hệ "
      "thống, không nên chọn dải tỷ lệ hẹp, vì điều này gây ra những biến động "
      "không cần thiết trong lưu lượng nước cấp, cũng không được chấp nhận "
      "trong công nghiệp. Hệ thống nước cấp chỉ đơn giản thao tác lưu lượng "
      "nước cấp để cân bằng lượng hơi tạo ra và rút ra khỏi trống. Hệ thống "
      "điều khiển giải phương trình sau:",
      "Due to the low time constant of the boiler drum, control of level is "
      "subject to rapid load changes. Also, due to the turbulence prevailing "
      "inside the system, a narrow proportional band is not advisable to "
      "select, since this causes unnecessary variations in the feed-water "
      "flow, which are unacceptable in the industries as well. The feed-water "
      "system simply manipulates feed-water flow to equalise the amount of "
      "steam produced and withdrawn from the drum. The control system solves "
      "the following equation:")

    E(b, lang,
      "W<sub>F</sub> = W<sub>S</sub> + M<sub>C</sub> − 0.5",
      "W<sub>F</sub> = W<sub>S</sub> + M<sub>C</sub> − 0.5")

    P(b, lang,
      "trong đó W<sub>F</sub> và W<sub>S</sub> lần lượt là lưu lượng khối lượng "
      "của nước cấp và hơi lấy ra. M<sub>C</sub> là đầu ra của bộ điều khiển "
      "chính có giá trị bình thường là 0.5, tức là độ lệch 50%. Vì hệ thống "
      "mức trống không tự điều chỉnh, biến quá trình có thể trôi, do đó bộ "
      "điều khiển chính được chọn cho điều khiển hai chế độ, tỷ lệ và tích "
      "phân. Trong giai đoạn ổn định, lưu lượng nước cấp đúng bằng lưu lượng "
      "hơi lấy ra, vì vậy đầu ra của bộ điều khiển chính sẽ làm giảm độ lệch, "
      "với giá trị đặt của bộ điều khiển chính là 50%.",
      "where W<sub>F</sub> and W<sub>S</sub> are the mass flow of feed-water "
      "and steam taken out respectively. M<sub>C</sub> is the output of the "
      "primary controller, which has a normal value of 0.5, that is a 50% bias. "
      "Since the drum level system is not self-regulating, the process variable "
      "can drift; therefore the primary controller is selected for two-mode "
      "control, proportional and integral. During the steady-state period the "
      "feed-water flow is just equivalent to the steam flow out and therefore "
      "the output of the primary controller shrinks the bias, the set value of "
      "the primary controller being at 50%.")

    P(b, lang,
      "Sau thay đổi tải thường là một giai đoạn mất cân bằng động trông như "
      "sai số quá độ. Kỹ thuật hiệu chỉnh mất cân bằng động gọi là bù động và "
      "được thực hiện bằng bộ đón đầu-trễ. Yêu cầu quan trọng nhất của bộ đón "
      "đầu-trễ là độ chính xác trạng thái ổn định. Quan hệ giữa thay đổi thực "
      "tế của lưu lượng nước cấp do một thay đổi nhất định của lưu lượng hơi "
      "lấy ra gây ra không hoàn hảo cả trong trạng thái quá độ lẫn trạng thái "
      "ổn định. Hành động tích phân trong bộ điều khiển phụ được dùng để điều "
      "chỉnh quan hệ pha giữa lưu lượng hơi và lưu lượng nước cấp.",
      "Load changes are normally followed by a period of dynamic imbalance "
      "which looks like transient error. The technique of correction for "
      "dynamic imbalance is called dynamic compensation and is accomplished "
      "by a lead-lag unit. The most important requirement for a lead-lag unit "
      "is its steady-state accuracy. The relation between an actual change in "
      "feed-water flow brought about by a given change in steam flow out is "
      "perfect neither in the transient nor in the steady-state condition. "
      "Integral action in the secondary controller is used to adjust the "
      "phase relation between steam and feed-water flows.")

    P(b, lang,
      "Với sự xuất hiện của bộ điều khiển kép đa chức năng, lập trình được, "
      "dựa trên vi xử lý, toàn bộ quản lý vòng điều khiển có thể do một thiết "
      "bị duy nhất thực hiện. Chỉ cần ba bộ phát thông minh cấu hình từ xa dựa "
      "trên PC, liên lạc bằng giao thức HART, mỗi bộ cho mức trống, lưu lượng "
      "nước cấp và lưu lượng hơi lấy ra. Các chức năng khai căn bậc hai và "
      "tính toán lưu lượng được lập trình bên trong chính bộ điều khiển đa "
      "chức năng. Một bộ định vị van điện-khí nén được dùng cho van điều khiển "
      "lắp trên đường nước cấp. Vòng điều khiển với các thiết bị này được thể "
      "hiện trong Hình 6.26.",
      "With the advent of microprocessor-based, programmable, multifunction, "
      "dual controllers, entire control loop management can be accomplished "
      "by one instrument only. Only three PC-based remote-configurable smart "
      "transmitters, communicating on the HART protocol, are required, one "
      "each for drum level, feed-water flow and steam flow out. The functions "
      "of square rooting as well as flow computation are programmed inside the "
      "multifunction controller itself. An electro-pneumatic valve positioner "
      "is used for the control valve installed on the feed-water line. The "
      "control loop with these instruments is indicated in Figure 6.26.")

    FIG(b, 26, F.fig_f26(), lang)

    return b
