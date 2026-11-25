# -*- coding: utf-8 -*-
"""Chapter 6, sections 6.8-6.10.1 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 303-312, printed pp. 291-300, decoded
text lines 11690-12099. Covers the electronic controller (error detector,
amplifier and RC network), the pneumatic controller (old model, miniature
design, manual loading station), the comparison between the two controller
types, the selection of a control technique and the automatic process
control system, with Figures 6.19-6.24.

The printed figures are images in the PDF, so the page renders were consulted
for their labels and numeric values. The `ipcfig6_c` supplier is authored in
parallel; simple but valid 5-tuple fallbacks are installed below only for
figure numbers not yet registered, and never replace a real supplier callable.
No numbered equations occur in this source span.
"""

import ipcfig6 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
_STUB_LABELS = {
    19: ("Error detector with zener-stabilised 1.25 V supply",
         "Bộ phát hiện sai số với nguồn ổn áp zener 1,25 V"),
    20: ("Operational amplifier input and feedback capacitor network",
         "Mạng tụ đầu vào và phản hồi của bộ khuếch đại thuật toán"),
    21: ("Old-model pneumatic controller with four bellows",
         "Bộ điều khiển khí nén kiểu cũ với bốn buồng khí"),
    22: ("Miniature pneumatic controller block diagram",
         "Sơ đồ khối bộ điều khiển khí nén thu nhỏ"),
    23: ("Control module with floating disc and four bellows",
         "Mô-đun điều khiển với đĩa nổi và bốn buồng khí"),
    24: ("Automatic process control system block diagram",
         "Sơ đồ khối hệ thống điều khiển quá trình tự động"),
}


def _stub(n):
    en, vi = _STUB_LABELS[n]
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
        'viewBox="0 0 680 250"><rect width="680" height="250" '
        'fill="#ffffff"/><rect x="110" y="80" width="460" height="90" '
        'fill="#eef3fb" stroke="#1f3a5f" stroke-width="1.2"/>'
        '<text x="340" y="112" text-anchor="middle" font-size="13" '
        'fill="#1f3a5f">Figure 6.%d</text>'
        '<text x="340" y="138" text-anchor="middle" font-size="11" '
        'fill="#1f3a5f">%s</text>'
        '<text x="340" y="225" text-anchor="middle" font-size="8" '
        'fill="#888888">Hinh 6.%d / Figure 6.%d</text></svg>'
        % (n, en, n, n))
    return (svg,
            "Hình 6.%d · %s" % (n, vi),
            "Figure 6.%d · %s" % (n, en),
            vi, en)


for _n in range(19, 25):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _stub(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ------------------------------------------------------------- 6.8
    H(b, lang, "6.8 Bộ điều khiển điện tử",
      "6.8 Electronic controller")

    P(b, lang,
      "Bộ điều khiển điện tử là một thiết bị điện tử gồm các bộ phận sau: "
      "(i) bộ phát hiện sai số, (ii) bộ khuếch đại và (iii) mạch mạng RC.",
      "An electronic controller is an electronic instrument consisting of "
      "the following components: (i) an error detector unit, (ii) an "
      "amplifier unit and (iii) an RC network circuit.")

    P(b, lang,
      "Bộ điều khiển nhận tín hiệu đầu vào của quá trình dưới dạng dòng một "
      "chiều 4 đến 20 mA từ các bộ phát lắp tại hiện trường và cung cấp tín "
      "hiệu điều khiển đầu ra cũng ở dạng dòng một chiều 4 đến 20 mA, cuối "
      "cùng dùng để điều khiển phần tử điều khiển cuối cùng đặt tại hiện "
      "trường. Dải tín hiệu đầu ra có khả năng điều khiển phần tử điều khiển "
      "cuối cùng có trở kháng lên tới 1500 Ω.",
      "It takes the process input signal as a 4 to 20 mA DC signal from "
      "field-mounted transmitters and provides a control output, also a 4 "
      "to 20 mA DC signal, which ultimately operates the final control "
      "element located in the field. The output range is capable of driving "
      "a final control element having an impedance of up to 1500 ohms.")

    P(b, lang,
      "Tín hiệu khởi phát hoạt động của bộ điều khiển thực chất là tín hiệu "
      "sai số (hiệu giữa tín hiệu biến quá trình đầu vào và giá trị cài "
      "đặt), được tạo ra trong bộ phát hiện sai số như thể hiện trên Hình "
      "6.19. Bộ phát hiện sai số gồm một điện trở đầu vào chính xác (trị số "
      "62,5 Ω ± 0,1%) và một chiết áp chính xác dùng để chỉnh giá trị cài "
      "đặt. Bộ nguồn cung cấp điện áp chuẩn 1,25 V một chiều cho chiết áp "
      "chỉnh giá trị cài đặt như trên hình. Dòng tín hiệu đầu vào được biến "
      "đổi thành tín hiệu điện áp (0,25 V đến 1,25 V một chiều) nhờ điện trở "
      "chính xác. Điện áp giá trị cài đặt và điện áp biến quá trình tạo ra "
      "điện áp sai số. Sự thay đổi giá trị cài đặt được thực hiện bằng cách "
      "chỉnh chiết áp. Điện áp sai số (từ −1 V đến +1 V) được đưa tới bộ "
      "khuếch đại.",
      "The signal that initiates controller operation is the error signal "
      "(the difference between the process input variable signal and the "
      "set value), which is generated in an error detector unit as shown in "
      "Figure 6.19. The error detector consists of a precision input "
      "resistor (62.5 ohms ± 0.1%) and a precision potentiometer used as the "
      "set-value adjustment unit. The power supply unit supplies a standard "
      "voltage of 1.25 V DC to the set-value adjusting potentiometer, as "
      "shown. The input signal current is converted into a voltage signal "
      "(0.25 V to 1.25 V DC) by the precision resistor. The set-value voltage "
      "and the process-variable voltage generate the error voltage. The set "
      "value is varied by adjusting the potentiometer. The error voltage "
      "(−1 V to +1 V) is applied to the amplifier.")

    FIG(b, 19, F.fig_f19(), lang)

    P(b, lang,
      "Điện áp sai số mang dấu âm hay dương tùy vào tín hiệu đầu vào biến "
      "quá trình cao hơn hay thấp hơn tín hiệu giá trị cài đặt. Thông "
      "thường, khi hai tín hiệu này bằng nhau thì hai kim chỉ thị trùng "
      "khớp và không có tín hiệu sai số. Bộ khuếch đại nâng tín hiệu này lên "
      "mức đủ để điều khiển phần tử điều khiển cuối cùng. Mạch mạng RC cho "
      "phép bộ khuếch đại tạo ra các dạng đáp ứng điều khiển khác nhau cần "
      "thiết cho vòng lặp. Với hằng số thời gian thay đổi, mạch mạng RC tạo "
      "ra các tác động điều khiển khác nhau bằng cách thay đổi phản hồi. "
      "Phản hồi âm làm giảm độ lợi của hệ thống và tuyến tính hóa hệ thống, "
      "giúp tăng độ ổn định nhưng đồng thời làm giảm độ nhạy của hệ thống.",
      "The error voltage is negative or positive depending on whether the "
      "process-variable input signal is above or below the set-value signal. "
      "Typically, when the two signals are equal, the two pointers coincide "
      "and there is no error signal. The amplifier unit raises this signal "
      "to a level sufficient to operate the final control element. The RC "
      "network circuit enables the amplifier unit to create the various "
      "forms of control response required by the loop. Having variable time "
      "constants, the RC network produces different control actions by "
      "changing the feedback. Negative feedback reduces the gain of the "
      "system and linearises the system; this helps to increase stability "
      "but at the same time decreases the sensitivity of the system.")

    P(b, lang,
      "Mạch khuếch đại thuật toán trên Hình 6.20 là mạch cơ bản cho các tác "
      "động điều khiển điện tử. Mạch gồm một mạng đầu vào và một mạng phản "
      "hồi. Dòng của mạng đầu vào nạp cho tụ đầu vào Cin, còn dòng phản hồi "
      "nạp cho tụ phản hồi Cfb. Khi cả hai tụ được nạp bằng nhau thì không "
      "có dòng chảy. Dòng trôi đầu vào rất nhỏ (không đáng kể) giữ cho bộ "
      "khuếch đại hoạt động. Trong trạng thái này, dù chỉ tăng nhẹ dòng tín "
      "hiệu đầu vào cũng nạp thêm cho tụ Cin và sinh ra dòng phản hồi bắt "
      "đầu nạp cho tụ Cfb. Điều này có nghĩa là dòng phản hồi liên tục bám "
      "theo dòng tín hiệu sai số đầu vào, do đó phản ứng của mạch khuếch đại "
      "gần như tức thời. Vì hai dòng này luôn xấp xỉ bằng nhau, điện tích "
      "trên hai tụ luôn giữ nguyên và vì thế điểm nối của hai tụ gần như "
      "luôn ở thế đất.",
      "The operational amplifier circuit shown in Figure 6.20 is the basic "
      "circuit for electronic controller actions. It consists of an input "
      "network and a feedback network. The input-network current charges the "
      "input capacitor Cin, while the feedback current charges the feedback "
      "capacitor Cfb. When both capacitors are equally charged, no current "
      "flows. A slight input floating current, insignificant in value, keeps "
      "the amplifier alive. In this condition, even a slight increase in the "
      "input signal current charges Cin and produces a feedback current that "
      "begins to charge Cfb. This means the feedback current constantly "
      "tracks the error signal input current, so the reaction of the "
      "amplifier circuit is almost instantaneous. Since the two currents "
      "remain more or less equal, the charges on the capacitors stay the "
      "same and therefore the junction point of the two capacitors almost "
      "always remains at ground potential.")

    FIG(b, 20, F.fig_f20(), lang)

    # ------------------------------------------------------------- 6.9
    H(b, lang, "6.9 Bộ điều khiển khí nén",
      "6.9 Pneumatic controller")

    P(b, lang,
      "Nhìn lại lịch sử phát triển của bộ điều khiển, một điểm rất đáng "
      "ngạc nhiên là van điều khiển bằng màng (từ thế kỷ XIX) lại là thiết "
      "bị đầu tiên trong dòng này được coi là gần giống nhất với một bộ "
      "điều khiển (thực chất là một bộ điều khiển hở). Loại sau này được gọi "
      "là 'bộ điều khiển mù' này về cơ bản là một thiết bị lắp tại hiện "
      "trường, nhỏ gọn, thực hiện cả việc đo lường (theo một cách) lẫn điều "
      "khiển quá trình. Đến thế kỷ XX, các bộ phát khí nén ra đời, cho phép "
      "chuyển toàn bộ cụm điều khiển từ trạm lắp tại hiện trường đến trạm "
      "điều khiển bố trí tập trung để thực hiện điều khiển từ xa. Thế kỷ này "
      "chứng kiến nhiều bước phát triển trong lĩnh vực bộ điều khiển khí nén "
      "và cuối cùng đã đi tới loại bộ điều khiển thu nhỏ cấp cao (kích "
      "thước mặt trước 6″ × 3″), vẫn còn hiệu quả trong một số nhà máy chế "
      "biến cũ. Tuy nhiên, hiện nay bộ điều khiển điện tử đang thay thế bộ "
      "điều khiển khí nén, thiết bị này đang dần bị loại bỏ và có thể một "
      "ngày sẽ chỉ còn là chuyện lịch sử.",
      "Looking back historically at controllers, it is surprising to "
      "conclude that a diaphragm-actuated valve, dating from the nineteenth "
      "century, was the first device in this line to be regarded as the "
      "closest analogue of a controller (in effect an open-loop controller). "
      "Later called the 'blind controller', it was essentially a field-mounted, "
      "compact object that performed both the measurement (in one way) and "
      "the control of the process. In the twentieth century, pneumatic "
      "transmitters appeared, making it possible to move the entire "
      "controller physically from the field mounting station to a centrally "
      "located control station for remote operation. This century saw many "
      "facets of development in the pneumatic controller field, finally "
      "settling on a high level of miniature controller (front size 6″ × 3″), "
      "which is still effective in some older processing plants. Nowadays, "
      "however, the electronic controller is taking the place of the "
      "pneumatic controller, which is being slowly phased out; a day may "
      "come when it becomes a matter of history only.")

    P(b, lang,
      "Hình 6.21 thể hiện thiết kế cơ bản của một mẫu bộ điều khiển khí nén "
      "cũ. Trong mẫu này có bốn buồng khí (bellows) được bố trí như trên "
      "hình. Bộ phát lắp tại hiện trường gửi tín hiệu biến quá trình (dưới "
      "dạng 0,2 đến 1,0 kg/cm²) tới buồng biến quá trình (PV). Bộ chỉnh giá "
      "trị cài đặt gửi tín hiệu giá trị cài đặt tới buồng giá trị cài đặt "
      "(SV). Hai tín hiệu này được so sánh và một tác động hiệu chỉnh dưới "
      "dạng tín hiệu đầu ra khí nén được tạo ra nhờ cánh flap và cụm vòi "
      "phun – rơ le tăng áp (booster relay-cum-nozzle). Tín hiệu đầu ra, "
      "trước khi đi điều khiển phần tử điều khiển cuối cùng, còn được đưa "
      "tới buồng tác động tích phân lại (RA) qua bộ tiết lưu đặt lại (reset "
      "restrictor) như trên sơ đồ. Tín hiệu đầu ra này cũng được gửi tới "
      "buồng phản hồi (FB) qua bộ vi phân. Ở các bộ điều khiển sau này được "
      "cải tiến hơn, bộ vi phân được đưa vào đường tín hiệu đầu vào đo "
      "lường; chúng ta sẽ thảo luận dạng đó sau.",
      "Figure 6.21 shows the very basic design of an old model of pneumatic "
      "controller. In this model there are four bellows arranged as shown. "
      "The field-mounted transmitter sends the process-variable signal input "
      "(in the form of 0.2 to 1.0 kg/cm²) to the process-variable (PV) "
      "bellows. A set-value regulation unit sends the set-value signal to "
      "the set-value (SV) bellows. These two signals are compared, and a "
      "corrective action in the form of a pneumatic output signal is "
      "generated by the flapper and the booster relay-cum-nozzle assembly. "
      "On its way to operate the final control element, the output signal is "
      "also sent to the reset-action (RA) bellows through the reset "
      "restrictor unit, as shown in the diagram. This output signal is sent "
      "to the feedback (FB) bellows as well, through the derivative unit. "
      "In later controllers of comparatively improved design, the derivative "
      "units were placed in the measurement input line; that form is "
      "discussed a little later.")

    FIG(b, 21, F.fig_f21(), lang)

    P(b, lang,
      "Tạo tác động vi phân thông qua đường đầu ra có những hạn chế rõ rệt. "
      "Theo cách này, tác động vi phân tương tác với các đáp ứng tỷ lệ và "
      "tích phân lại và thực chất đi theo đáp ứng tỷ lệ. Vì vậy nó không có "
      "khả năng ngăn ngừa vượt quá (overshoot) trong giai đoạn khởi động "
      "hoặc khi có nhiễu động lớn.",
      "Achieving derivative action through the output system presents some "
      "obvious limitations. In this approach, the derivative action "
      "interacts with the proportional and reset responses and actually "
      "follows the proportional response. Hence it is not capable of "
      "preventing overshoot during start-up or during large disturbances.")

    P(b, lang,
      "Sơ đồ khối trên Hình 6.22 cho thấy thiết kế của một bộ điều khiển khí "
      "nén thu nhỏ (dạng thiết kế hiện đại nhất thời đó trong dòng bộ điều "
      "khiển khí nén). Nhìn chung, thiết kế này gồm sáu bộ phận chức năng "
      "được lắp trong một vỏ duy nhất, bố trí lắp phẳng trên bảng điều khiển "
      "trung tâm. Bộ phận chính có cặp kim chỉ thị (một cho giá trị cài đặt, "
      "một cho biến quá trình) thực chất chứa cả sáu bộ phận, được thể hiện "
      "rời rạc trên sơ đồ.",
      "The block diagram in Figure 6.22 shows the design of a miniature "
      "pneumatic controller, the most modern design of its time in the "
      "pneumatic controller line. In general, this design has altogether six "
      "functional components assembled in one housing, arranged for flush "
      "mounting on a central control panel. The main unit with the "
      "twin-indicator arrangement (one indicator for the set value and the "
      "other for the process variable) in fact houses all six components, "
      "which are shown scattered in the diagram.")

    FIG(b, 22, F.fig_f22(), lang)

    P(b, lang,
      "Cơ cấu giá trị cài đặt thiết lập giá trị cài đặt (được chỉ thị trên "
      "hệ thống kim đôi) thông qua một núm chỉnh đặt ở bên ngoài thân bộ "
      "điều khiển để người vận hành thao tác dễ dàng. Tín hiệu biến quá "
      "trình đến trực tiếp từ bộ phát lắp tại hiện trường trong quá trình. "
      "Bộ vi phân cộng thêm vào tín hiệu biến quá trình trước khi tín hiệu "
      "này vào mô-đun điều khiển. Như ta thấy, trong thiết kế này bộ vi phân "
      "được đưa vào đường đầu vào biến quá trình chứ không phải đường đầu ra "
      "điều khiển.",
      "The set-value mechanism fixes the set value (indicated on the "
      "twin-indicator system) by means of an adjusting knob located outside "
      "the controller unit, for ease of operation by the operator. The "
      "process-variable input comes directly from the field-mounted "
      "transmitter installed in the process. The derivative unit adds to "
      "the process-variable signal before it enters the control module. As "
      "can be seen, in this design the derivative units have been added in "
      "the process-variable input line and not in the control output line.")

    P(b, lang,
      "Mô-đun điều khiển là trái tim của bộ điều khiển này, gồm tổ hợp bốn "
      "buồng khí làm việc (cần thiết cho mọi thiết kế bộ điều khiển khí nén "
      "tự động) như trên Hình 6.23. Bốn buồng khí tác động động học lên một "
      "đĩa nổi, đĩa này giữ các buồng ở trạng thái cân bằng đối với điểm tựa "
      "và đồng thời đóng vai trò là cánh flap của hệ thống. Việc chỉnh dải "
      "tỷ lệ (proportional band) được thực hiện qua thanh điểm tựa. Tác động "
      "điều khiển tổng hợp tạo ra tín hiệu đầu ra đưa tới phần tử điều khiển "
      "cuối cùng, được lắp gần quá trình.",
      "The control module is the heart of this controller, with a combination "
      "of four working bellows (essential for any automatic pneumatic "
      "controller design), as shown in Figure 6.23. Four bellows dynamically "
      "bear upon a floating disc, which keeps them in equilibrium with "
      "respect to the fulcrum and also acts as the flapper of the system. "
      "Adjustment of the proportional band is carried out through the "
      "fulcrum bar. The combined controller action generates the output, "
      "which is fed to the final control element installed near the process.")

    FIG(b, 23, F.fig_f23(), lang)

    L(b, lang,
      ["FB – buồng phản hồi (feedback bellows).",
       "PV – buồng biến quá trình (process variable bellows).",
       "SV – buồng giá trị cài đặt (set value bellows).",
       "RA – buồng tác động tích phân lại (reset action bellows)."],
      ["FB – feedback bellows.",
       "PV – process variable bellows.",
       "SV – set value bellows.",
       "RA – reset action bellows."])

    P(b, lang,
      "Trạm nạp tay (manual loading station) điều chỉnh và cung cấp tín hiệu "
      "đầu ra bằng tay để điều khiển phần tử điều khiển cuối cùng trong "
      "trường hợp tín hiệu tự động từ mô-đun điều khiển bị lỗi do chính nó, "
      "hoặc khi người vận hành chủ động chuyển sang điều khiển tay để bảo "
      "trì bộ phát lắp tại hiện trường. Trạm nạp tay cũng thực hiện chuyển "
      "đổi bằng thao tác chuyển mạch giữa chế độ điều khiển tay và tự động. "
      "Bộ cân bằng tự động (auto balance unit) là một bộ điều khiển nổi, "
      "theo dõi tín hiệu đầu ra hiện có (từ mô-đun điều khiển hoặc từ trạm "
      "nạp tay) và tạo ra tín hiệu còn lại (tín hiệu không có sẵn), nhờ đó "
      "chuyển đổi không giật (bumpless transfer) có thể diễn ra giữa hai chế "
      "độ. Nếu bộ điều khiển đang ở chế độ tự động, bộ cân bằng tự động đặt "
      "tín hiệu đầu ra tay sao cho khi chuyển sang chế độ tay, đầu ra lập "
      "tức đi thẳng tới phần tử điều khiển cuối cùng. Trường hợp ngược lại "
      "cũng tương tự.",
      "The manual loading station regulates and provides a manual output "
      "signal for operating the final control element if the automatic "
      "signal from the control module fails because of a fault in the module "
      "itself, or when the controller is intentionally operated manually to "
      "carry out maintenance on the field-mounted transmitter. The manual "
      "loading station also performs change-over by switching between manual "
      "and automatic control. The auto-balance unit is a floating controller "
      "that tracks the available output signal (from either the control "
      "module or the manual loading station) and generates the other one "
      "(the one not available), so that a bumpless transfer can take place "
      "between the manual and automatic options. If the controller is on "
      "automatic, the auto-balance unit positions the manual output so that "
      "when the controller is switched to manual, the output goes straight "
      "to the final control element. The reverse case is similar.")

    P(b, lang,
      "Cuối cùng là một kim chỉ thị đầu ra nhỏ, thực chất chỉ thị tín hiệu "
      "đầu ra đi tới phần tử điều khiển cuối cùng nhưng có thể được hiểu là "
      "vị trí mở thực tế của phần tử đó. Tất cả các bộ phận của các bộ điều "
      "khiển khí nén nêu trên đều dễ dàng thay thế khi bảo trì; đó là ưu "
      "điểm lớn nhất của loại bộ điều khiển này.",
      "Finally there is a small output indicator, which in fact indicates "
      "the output signal going to the final control element but can be "
      "interpreted as the actual opening position of the final control "
      "element. All the components of the pneumatic controllers described "
      "above are easily replaceable for maintenance work; this is their "
      "greatest advantage.")

    # ----------------------------------------------------------- 6.9.1
    H(b, lang, "6.9.1 So sánh bộ điều khiển điện tử và bộ điều khiển khí nén",
      "6.9.1 Comparison between electronic and pneumatic controllers",
      level=3)

    P(b, lang,
      "Ngày nay, nhu cầu về kỹ thuật điều khiển tốt hơn và tiên tiến hơn đã "
      "tăng lên mạnh mẽ nhằm nâng cao năng suất, hạ chi phí sản xuất, cải "
      "thiện và đồng nhất chất lượng sản phẩm, đồng thời tăng cường an toàn "
      "cho người vận hành. Những điều này trở nên dễ dàng nhờ sự ra đời của "
      "bộ điều khiển điện tử, cho chất lượng điều khiển tốt hơn so với bộ "
      "điều khiển khí nén. Tính ưu việt của bộ điều khiển điện tử so với bộ "
      "điều khiển khí nén được so sánh theo các đặc tính sau:",
      "Nowadays, the demand for better and more improved control techniques "
      "has grown strongly, aiming at higher productivity, lower production "
      "cost, improved and more uniform product quality, and greater security "
      "and safety for operating personnel. These goals have become easily "
      "attainable thanks to the introduction of the electronic controller, "
      "which provides better control than its pneumatic counterpart. The "
      "superiority of the electronic controller over the pneumatic one can "
      "be compared on the following characteristics:")

    L(b, lang,
      ["Độ tin cậy. Bộ điều khiển điện tử được chế tạo từ các linh kiện bán "
       "dẫn có tuổi thọ dài hơn cả thiết bị mà chúng điều khiển. Không có bộ "
       "phận cơ khí nên không xảy ra hỏng hóc vì lý do cơ khí như mỏi, quán "
       "tính của các chi tiết cơ khí và các vấn đề tương tự. Theo các nghiên "
       "cứu độ tin cậy và kinh nghiệm thực tế với thiết bị điện tử bán dẫn, "
       "chúng chỉ có khả năng hỏng trong giai đoạn đầu của thời gian thử "
       "tải; một khi qua giai đoạn quan trọng đó, độ tin cậy cực kỳ cao được "
       "đảm bảo. Ngược lại, bộ điều khiển khí nén cần bảo trì nhiều hơn nên "
       "kém hiệu quả hơn. Khả năng rò rỉ trong hệ thống khí gây ra vấn đề "
       "lớn trong tác động điều khiển khi có quá trình chuyển tiếp; vấn đề "
       "này có thể nghiêm trọng đến mức hệ thống không đạt được trạng thái "
       "ổn định.",
       "Tốc độ đáp ứng. Vì không có bộ phận chuyển động, độ trễ do quán tính "
       "và các đặc tính cơ khí khác giữa tín hiệu lệnh và hành động hiệu "
       "chỉnh thường không đáng kể. Bằng cách thiết kế cẩn thận và chọn "
       "linh kiện phù hợp, tổng thời gian trễ chỉ còn vài microgiây. Đối với "
       "bộ điều khiển khí nén được thiết kế tốt nhất, độ trễ này tính bằng "
       "mili-giây.",
       "Chi phí. Nhờ công nghệ điện tử ngày càng tiến bộ, chi phí giảm đáng "
       "kể và sẽ còn giảm hơn nữa trong tương lai gần. Đối với các nhà máy "
       "quy mô lớn, chi phí lắp đặt hệ thống điện tử còn giảm thêm. Bộ điều "
       "khiển khí nén rẻ hơn bộ điều khiển điện tử, nhưng về lâu dài bộ "
       "điều khiển điện tử có thể lại rẻ hơn vì ngày càng phải thay thế "
       "nhiều bộ điều khiển khí nén.",
       "Tiêu thụ công suất. Mức tiêu thụ công suất của bộ điều khiển điện "
       "tử thấp và đồng đều, không cần bố trí đặc biệt hay bổ sung; việc "
       "bảo trì hệ thống nguồn cũng không đòi hỏi thêm thiết bị. Ngược lại, "
       "bộ điều khiển khí nén cần một hệ thống cấp khí dụng cụ hoàn chỉnh "
       "gồm máy nén khí dụng cụ (tốt nhất là loại piston có điều khiển công "
       "suất), hệ thống sấy bằng gel silica (có cơ chế tái sinh tự động) "
       "cùng các thiết bị và điều khiển liên quan, chưa kể hệ thống đường "
       "ống khổng lồ để đưa khí dụng cụ tới mọi vị trí. Vì vậy cần thêm công "
       "suất để chạy máy nén liên tục và các thiết bị khác.",
       "Độ chính xác. Bộ điều khiển điện tử có độ chính xác ± 0,25%, trong "
       "khi bộ điều khiển khí nén được thiết kế tốt nhất chỉ đạt ± 0,5%.",
       "Khả năng bảo trì. Đặc tính này xấp xỉ như nhau ở hai loại bộ điều "
       "khiển. Theo nguyên lý cấu trúc module, các cụm và cụm con dạng cắm "
       "được lắp vào và tháo ra dễ dàng để bảo trì. Với thiết kế module, "
       "ngay cả việc thay thế cũng thực hiện được mà không làm gián đoạn "
       "hoạt động của quá trình.",
       "Đóng gói. Tiêu chí thiết kế về đóng gói thiết bị đã được cải thiện "
       "đáng kể trong những năm gần đây. Các vỏ thiết bị cỡ lớn đã được thu "
       "nhỏ lại, kích thước trở nên thu nhỏ hoặc siêu thu nhỏ để chứa các bo "
       "mạch module. Mật độ thiết bị trên bảng điều khiển cũng giảm, giúp "
       "dành thêm không gian cho các thiết bị khác cung cấp nhiều thông tin "
       "hơn về tình trạng quá trình. Đặc tính này cũng như nhau ở hai loại "
       "bộ điều khiển.",
       "Vấn đề an toàn. Bộ điều khiển khí nén thường an toàn hơn trong bầu "
       "khí quyển dễ nổ, vốn phổ biến ở hầu hết các ngành công nghiệp quá "
       "trình. Bộ điều khiển điện tử có thể không phù hợp cho khu vực nguy "
       "hiểm, nhưng hiện nay vấn đề này đã được giải quyết triệt để nhờ "
       "cung cấp rào an toàn điện tử (electronic safety barrier), cô lập "
       "khu vực dễ nổ với khu vực an toàn.",
       "Khả năng tương thích với máy tính. Bộ điều khiển điện tử có khả năng "
       "tương thích máy tính rất tốt. Chỉ cần một hệ thống chuyển đổi "
       "tương tự-số cho tín hiệu tương tự và tín hiệu từ bộ chuyển đổi có "
       "thể đưa thẳng vào máy tính để xử lý tiếp, ví dụ giám sát và thu thập "
       "dữ liệu. Bộ điều khiển khí nén trước hết cần một bộ chuyển đổi "
       "khí-điện, chuyển tín hiệu khí nén 0,2 đến 1,0 kg/cm² thành tín hiệu "
       "điện tương đương là dòng 4 đến 20 mA một chiều. Tín hiệu điện này "
       "sau đó được chuyển sang dạng số để tương thích với máy tính. Khả "
       "năng tương thích máy tính dẫn đến các dạng điều khiển tiên tiến hơn "
       "như điều khiển thích ứng hoặc điều khiển tối ưu."],
      ["Reliability. Electronic controllers are made of semiconductor "
       "devices whose life is longer even than the equipment they control. "
       "The absence of mechanical parts means there is no failure due to "
       "mechanical causes such as fatigue, inertia of moving parts and "
       "similar problems. Based on reliability studies and on working "
       "experience with semiconductor equipment, such devices are liable to "
       "fail only during the initial operating period of test loading; once "
       "that critical period is over, extremely high reliability is "
       "guaranteed. The pneumatic controller, on the other hand, needs more "
       "maintenance and is therefore relatively inefficient. The possibility "
       "of leakage in the air system creates a larger problem in the control "
       "action during transient conditions, so serious that the control may "
       "not be able to reach a steady-state condition.",
       "Speed of response. Since there are no moving parts, the delays caused "
       "by inertia and other mechanical characteristics between the command "
       "signal and the corrective action are usually insignificant. By "
       "careful design and proper selection of components, the total delay "
       "has been reduced to only a few microseconds. In the best-designed "
       "pneumatic controllers such delays are in milliseconds.",
       "Cost. With ever-improving electronics technology, the reduction in "
       "cost is considerable and will go further down in the near future. "
       "For larger process plants there is a further reduction in the "
       "installation cost of electronic systems. Pneumatic controllers are "
       "cheaper than electronic controllers, but in the long run electronic "
       "controllers may prove cheaper as more and more replacements are "
       "needed.",
       "Power consumption. The power consumption of an electronic controller "
       "is considerably lower and uniform, requiring no special or extra "
       "arrangement; maintenance of the power supply system likewise needs "
       "no extra provision. Pneumatic controllers, however, require a "
       "complete instrument air supply system comprising an instrument air "
       "compressor (preferably a reciprocating type with capacity control), "
       "a silica gel drying system (with automatic regeneration of the silica "
       "gel) and other connected equipment and controls, in addition to an "
       "extensive piping system to make instrument air available at every "
       "corner. Extra power is therefore needed to run the compressor "
       "continuously and for the other equipment.",
       "Accuracy. Electronic controllers have an accuracy of ± 0.25%, whereas "
       "pneumatic controllers of the best design have an accuracy of only "
       "± 0.5%.",
       "Maintainability. This characteristic is more or less equally "
       "available in both controller types. With the modular concept of "
       "construction, plug-in assemblies and sub-assemblies are fixed in "
       "easily and taken out easily for maintenance. In the modular design "
       "concept, even replacement is possible without disturbing process "
       "operation.",
       "Packaging. The design criteria for equipment packaging have improved "
       "considerably in recent years. Large instrument cases have been "
       "reduced and sizes have become miniature or sub-miniature to house "
       "modular boards. The density of instruments on the control panel has "
       "likewise been reduced, so that more space becomes available for "
       "other equipment that can provide still more information about the "
       "process condition. This characteristic is also common to both "
       "controller types.",
       "Safety consideration. Pneumatic controllers are normally safer in "
       "the potentially explosive atmosphere prevailing in most process "
       "industries. An electronic controller may not be suitable for an "
       "explosive area; nowadays, however, this problem has been completely "
       "solved by providing an electronic safety barrier that isolates the "
       "explosive area from the safe area.",
       "Computer compatibility. Electronic controllers have excellent "
       "computer compatibility. Only an analog-to-digital conversion system "
       "is needed for the analog signal, and the converter output can be fed "
       "directly to the computer for further processing, for example "
       "supervisory control and data acquisition. A pneumatic controller "
       "first needs a pneumatic-to-electric converter that converts the 0.2 "
       "to 1.0 kg/cm² pneumatic signal into the equivalent electrical signal "
       "of 4 to 20 mA DC. This electrical signal is then converted into "
       "digital form to make it computer compatible. Computer compatibility "
       "leads to more advanced forms of control system, such as adaptive "
       "control or optimal control."],
      ordered=True)

    # ------------------------------------------------------------- 6.10
    H(b, lang, "6.10 Lựa chọn kỹ thuật điều khiển",
      "6.10 Selection of control technique")

    P(b, lang,
      "Việc lựa chọn một kỹ thuật điều khiển phù hợp mà vẫn kinh tế là quyết "
      "định khó khăn nhất đối với một hệ thống điều khiển quá trình tự động. "
      "Cần có sự thỏa hiệp giữa chất lượng điều khiển mong muốn và tính kinh "
      "tế của hệ thống được chọn. Hệ thống điều khiển được chọn phải đáp "
      "ứng được dung sai thiết kế của quá trình, và mức độ tinh vi của điều "
      "khiển không được vượt quá mức cần thiết, nếu không chi phí sẽ tăng "
      "lên một cách không cần thiết.",
      "Selecting a suitable yet economical control technique is the most "
      "difficult decision to be made for an automatic process control "
      "system. A compromise is called for between the expected control "
      "quality and the economy of the selected control system. The control "
      "system chosen should meet the process design tolerance, and the "
      "control refinement should not be more than just required, otherwise "
      "the cost becomes unnecessarily excessive.")

    P(b, lang,
      "Nhìn chung, chi phí đầu tư cho một hệ thống điều khiển được đánh giá "
      "theo những gì hệ thống đó cần thực hiện. Đôi khi chất lượng điều "
      "khiển cần thiết bị hy sinh để giảm chi phí đầu tư ban đầu, điều này "
      "hoàn toàn không mong muốn vì về lâu dài nó thường dẫn đến phương án "
      "tốn kém hơn do tăng bảo trì và mất thời gian sản xuất. Khi chọn một "
      "kỹ thuật điều khiển cụ thể, hai yếu tố chính phải được xem xét không "
      "thiên vị: mất thời gian sản xuất và chi phí bảo trì. Hai yếu tố này "
      "quan trọng hơn chi phí ban đầu.",
      "In general, the expenditure incurred for a control system is "
      "evaluated in terms of what it is required to accomplish. Sometimes "
      "the quality of control needed is sacrificed to minimise the initial "
      "cost; this is not at all desirable because in the long run it often "
      "leads to a more costly proposition owing to increased maintenance and "
      "loss of production time. In selecting a particular control technique, "
      "two prime factors must be considered without bias: loss of production "
      "time and maintenance cost. These are more critical than the initial "
      "cost.")

    P(b, lang,
      "Tuổi thọ dự kiến của một hệ thống điều khiển thường trên mười năm, vì "
      "vậy ý nghĩa của chi phí ban đầu là rất nhỏ. Một điểm nữa là nếu phân "
      "tích tình huống và môi trường làm việc bên trong nhà máy, một kỹ "
      "thuật điều khiển tinh vi hoặc phức tạp có thể không tăng hiệu suất "
      "chút nào. Đó là vì các kỹ thuật như vậy thường chỉ có lợi khi có người "
      "vận hành lành nghề cao và nhân viên bảo trì trình độ cao trong nhà "
      "máy. Do đó, kinh nghiệm và mức độ tận tâm của những người này phải "
      "được xem xét trước khi chọn kỹ thuật điều khiển bậc cao cho nhà máy.",
      "In general, the expected life of a control system is more than ten "
      "years, so the significance of the initial cost is very small. Another "
      "point is that if we analyse the situation and the working environment "
      "inside a process plant, a sophisticated or complex control technique "
      "may not increase the efficiency at all. Such techniques are usually "
      "advantageous only when high-grade skilled operators and high-grade "
      "maintenance personnel are available in the plant. Therefore the "
      "experience and sincerity level of such personnel must be examined "
      "before selecting a higher-order control technique for the plant.")

    P(b, lang,
      "Mỗi chế độ điều khiển có thể phù hợp với các quá trình có một tổ hợp "
      "đặc trưng riêng. Cần nhớ rằng chế độ điều khiển đơn giản nhất đáp ứng "
      "được yêu cầu được coi là lựa chọn tốt nhất. Xét về kinh tế và kết quả "
      "tốt nhất có thể, áp dụng điều khiển quá phức tạp cuối cùng chỉ làm "
      "tăng chi phí mà không cho kết quả thỏa mãn, đôi khi còn góp phần gây "
      "ra đặc tính không mong muốn của quá trình và loại bỏ sản phẩm.",
      "Each mode of control can be made suitable for processes having "
      "certain typical combinations of basic characteristics. It should be "
      "kept in mind that the simplest mode of control that can serve the "
      "purpose is the best choice without any prejudice. As far as economy "
      "and the best possible results are concerned, applying a comparatively "
      "complicated control ultimately results in higher cost without "
      "delivering a satisfactory result, and may sometimes even contribute "
      "to undesirable characteristics of the process and to product "
      "rejection.")

    P(b, lang,
      "Trong thiết kế điều khiển quá trình cẩn thận, khi chọn dải tỷ lệ hẹp, "
      "thường không cần tác động tích phân chút nào. Trong điều kiện này, hệ "
      "thống điều khiển áp dụng các hiệu chỉnh lớn cho độ lệch và độ lệch "
      "tĩnh (offset) không tồn tại ngay cả khi tải thay đổi. Về tác động vi "
      "phân, việc áp dụng nó làm giảm các trễ dài. Do đó, với điều khiển các "
      "biến quá trình thay đổi nhanh như lưu lượng hoặc áp suất, tác động vi "
      "phân thực chất có thể làm tăng sai số thay vì hiệu chỉnh. Khi đo lưu "
      "lượng bằng thiết bị kiểu chênh áp, đáp ứng của nó với dòng chảy thay "
      "đổi nhanh (ví dụ dòng xung đến từ bơm hoặc máy nén kiểu piston) là "
      "quá nhanh và đáp ứng này được truyền nhanh tới bộ điều khiển. Tác "
      "động vi phân, nếu có, sẽ tăng tốc hành động hiệu chỉnh theo các xung "
      "lưu lượng, dẫn đến đóng mở nhanh phần tử điều khiển cuối cùng (dao "
      "động van điều khiển) và cuối cùng là hỏng hóc.",
      "In careful process control design, when a narrow proportional band is "
      "selected, integral action is generally not required at all. Under "
      "this condition the control system applies large corrections for "
      "deviations and offset does not exist even with load changes. As far "
      "as derivative action is concerned, its application reduces long lags. "
      "Therefore, for controlling rapidly changing process variables such as "
      "flow or pressure, derivative action may actually result in increased "
      "error instead of making a correction. When flow is measured by "
      "differential-pressure instruments, its response to rapidly changing "
      "flow (for example pulsating flow from reciprocating pumps or "
      "compressors) is too fast and this response is quickly transmitted to "
      "the controller. Derivative action, if present, accelerates the "
      "corrective action in response to the flow pulsations, resulting in "
      "rapid opening and closing of the final control element (fluctuation "
      "of the control valve) and its eventual failure.")

    P(b, lang,
      "Một lượng đáng kể kinh nghiệm công nghiệp và thiết kế trong lĩnh vực "
      "này có thể rất hữu ích khi chọn chế độ điều khiển cho một biến quá "
      "trình. Chế độ điều khiển tỷ lệ được chọn cho quá trình có tốc độ phản "
      "ứng nhanh hoặc trung bình và thời gian chết hoặc trễ truyền nhỏ hoặc "
      "trung bình, trong trường hợp thay đổi tải nói chung nhỏ và chậm. Áp "
      "suất và mức chất lỏng, là các quá trình một dung lượng, thường thuộc "
      "nhóm chế độ điều khiển này. Khi thay đổi tải rất chậm và quá trình có "
      "dung lượng không đáng kể, trễ truyền và thời gian chết nhỏ, chế độ tỷ "
      "lệ cộng tích phân (PI) là giải pháp tốt nhất. Các vòng điều khiển lưu "
      "lượng thuộc nhóm này. Cuối cùng, chế độ tỷ lệ-cộng-tích phân-cộng-vi "
      "phân (PID) phù hợp nhất cho quá trình có hai hoặc nhiều hơn hai dung "
      "lượng với trễ truyền và thời gian chết lớn, khi thay đổi tải lớn và "
      "rất thường xuyên. Hệ thống điều khiển nhiệt độ nổi tiếng thuộc nhóm "
      "này.",
      "Considerable industrial and design experience in the field can be very "
      "helpful when selecting a particular mode of control for a process "
      "variable. Proportional control is selected for a process having a "
      "fast or medium reaction rate and small or moderate dead time or "
      "transfer lag, where load changes in particular are small and slow. "
      "Pressure and liquid level, being single-capacitance processes, "
      "generally fall under this control mode. Where load changes are "
      "considerably slow and the process has negligible capacitance, small "
      "transfer lag and dead time, proportional-plus-integral control is the "
      "best solution. Flow control loops come under this category. Finally, "
      "proportional-plus-integral-plus-derivative (PID) control is best "
      "suited to a process having two or more capacitances with large "
      "transfer lag as well as dead time, when load changes are quite large "
      "and very frequent. The well-known temperature control system falls "
      "under this category.")

    P(b, lang,
      "Như đã thấy trong thảo luận, các vòng điều khiển áp suất và mức dùng "
      "điều khiển tỷ lệ khi thay đổi tải vừa nhỏ vừa chậm, nhưng nhiều quá "
      "trình đang trải qua thay đổi tải lớn hơn và nhanh hơn. Các vòng này "
      "cần thiết đến chế độ điều khiển tỷ lệ cộng tích phân để loại bỏ độ "
      "lệch tĩnh gây ra.",
      "As seen in the discussion, pressure and level control loops use "
      "proportional control where load changes are both small and slow, but "
      "many processes are going through comparatively large load changes at "
      "a faster rate. Such loops essentially need proportional-plus-integral "
      "control and thus eliminate the offset caused.")

    # ----------------------------------------------------------- 6.10.1
    H(b, lang, "6.10.1 Hệ thống điều khiển quá trình tự động",
      "6.10.1 Automatic process control system", level=3)

    P(b, lang,
      "Chức năng cần thiết của hệ thống điều khiển quá trình tự động là dẫn "
      "các nguồn lực sẵn có trong chính quá trình sao cho đảm bảo hoạt động "
      "ổn định của thiết bị (kết quả cuối cùng về cơ bản là biến quá trình "
      "được duy trì ở mức mong muốn). Như ta hiểu, hệ thống điều khiển tự "
      "động về cơ bản là hệ thống kín phản hồi, trong đó năng lượng đầu vào "
      "của hệ thống cần là một hàm nào đó của đầu ra. Các phần tử cần thiết "
      "trong một hệ thống điều khiển điển hình kiểu phản hồi được thể hiện "
      "trên Hình 6.24.",
      "The required function of an automatic process control system is to "
      "channelise the driving forces available in the process itself so that "
      "stable operation of the unit can be assured (the end result being "
      "essentially the process variable maintained at the desired level). As "
      "we understand it, an automatic control system is essentially a "
      "feedback closed-loop system in which the input energy to the system "
      "is required to be some function of the output. The required elements "
      "in a typical feedback control system are shown in Figure 6.24.")

    FIG(b, 24, F.fig_f24(), lang)

    P(b, lang,
      "Trong sơ đồ khối này, phần tử phát hiện sai số cùng với bộ khuếch đại "
      "điều khiển thực chất là cụm bộ điều khiển. Tương tự, phần tử cảm biến "
      "sơ cấp cùng với bộ phát có thể được gọi là phương tiện đo lường. Quá "
      "trình là phần quan trọng nhất của toàn hệ thống vì nó cần thực hiện "
      "các chức năng nhất định và được xác định rõ. Thực chất, chính sự bổ "
      "sung năng lượng làm cho quá trình phản ứng như cách nó phản ứng và "
      "nhờ đó hoạt động mong muốn diễn ra một cách nhẹ nhàng.",
      "In this block diagram, the error-detecting element together with the "
      "control amplifier is in fact the controller unit. Similarly, the "
      "primary sensing element together with the transmitter can be called "
      "the measurement means. The process is the most important part of the "
      "entire system because it is required to perform certain desired and "
      "well-defined functions. In fact, it is the addition of energy that "
      "causes the process to react the way it does, and as a result the "
      "desired operation takes place silently.")

    return b
