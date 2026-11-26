# -*- coding: utf-8 -*-
"""Chapter 8, section 8.1 "Introduction" (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 353-355, printed pp. 341-343, decoded
text lines 13599-13717. Figures 8.1 and 8.2 are embedded in printed order.

Printed wording anomalies are preserved in the EN text; the VI text follows
the intended meaning. The `ipcfig8` callables are used when present; for the
two figures embedded here a non-overwriting fallback is installed only if
the real supplier has not registered them yet.
"""

import ipcfig8 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _fallback_fig(n):
    """Minimal genuine vector redraw used only until the supplier appears."""
    def _t(x, y, s, size=7.4):
        return ('<text x="%s" y="%s" text-anchor="middle" font-size="%s" '
                'fill="#1f3a5f">%s</text>' % (x, y, size, s))

    def _b(x, y, w, h, label):
        lines = str(label).split("\n")
        o = ['<rect x="%d" y="%d" width="%d" height="%d" rx="2" '
             'fill="#eef3fb" stroke="#1f3a5f" stroke-width="1.1"/>'
             % (x, y, w, h)]
        y0 = y + h / 2.0 - (len(lines) - 1) * size0 * 0.56 + size0 * 0.35
        for i, ln in enumerate(lines):
            o.append(_t(x + w / 2.0, y0 + i * size0 * 1.15, ln))
        return "".join(o)

    def _ar(x1, y1, x2, y2):
        return ('<path d="M%d %d L%d %d" fill="none" stroke="#1f3a5f" '
                'stroke-width="1.3" marker-end="url(#ipc8a%d)"/>' % (x1, y1, x2, y2, n))

    size0 = 7.4
    o = ['<defs><marker id="ipc8a%d" viewBox="0 0 8 8" refX="7" refY="4" '
         'markerWidth="6" markerHeight="6" orient="auto">'
         '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>' % n]
    if n == 1:
        for x, label in ((36, "Measurement\nsystems"),
                         (276, "Display\ndevices"),
                         (516, "Control\nactions")):
            o.append(_b(x, 36, 128, 40, label))
        o.append(_ar(164, 56, 276, 56))
        o.append(_ar(404, 56, 516, 56))
        for x, label in ((36, "Smart functions; remote\ncalibration adjustment\nand programming"),
                         (276, "Programmable recorder\nand indication functions"),
                         (516, "Fast and precise control\nactions with programmable\nfunctions")):
            o.append(_b(x, 116, 128, 72, label))
        cap_vi = ("Sơ đồ ba khối đo lường, hiển thị và điều khiển của hệ "
                  "thống thiết bị đo dựa trên vi xử lý")
        cap_en = ("Block diagram of the three functional blocks of "
                  "microprocessor-based instrumentation")
        alt_vi = "Ba khối đo lường, hiển thị và điều khiển"
        alt_en = "Measurement, display and control blocks"
    else:
        o.append(_b(36, 40, 150, 40, "Microprocessor"))
        o.append(_b(236, 40, 170, 40, "Memory with\nstored program\nand data"))
        o.append(_b(486, 40, 158, 40, "I/O interface"))
        for x, label in ((486, "Parallel I/O\ndevices"), (578, "Serial I/O\ndevices")):
            o.append(_b(x, 152, 72, 36, label))
        for y, label in ((120, "Address Bus"), (156, "Control Bus"), (192, "Data Bus")):
            o.append('<path d="M200 %d L650 %d" fill="none" stroke="#1f3a5f" '
                     'stroke-width="1.2"/>' % (y, y))
            o.append(_t(266, y - 5, label))
        cap_vi = ("Sơ đồ vi tính gồm bộ vi xử lý, bộ nhớ và I/O trên các bus "
                  "địa chỉ, điều khiển, dữ liệu")
        cap_en = ("Microcomputer with microprocessor, memory and I/O on "
                  "address, control and data buses")
        alt_vi = "Vi tính với bộ vi xử lý, bộ nhớ và các thiết bị I/O"
        alt_en = "Microcomputer with a microprocessor, memory and I/O devices"
    svg = ('<svg viewBox="0 0 680 250" role="img" aria-label="%s">%s</svg>'
           % (alt_en, "".join(o)))
    return (svg, cap_vi, cap_en, alt_vi, alt_en)


for _n in (1, 2):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _fallback_fig(_n)))


# ---------------------------------------------------------------- section
def section(lang):
    b = []

    H(b, lang, "8.1 Giới thiệu", "8.1 Introduction")

    P(b, lang,
      "Điện tử thông thường đã thâm nhập vào lĩnh vực thiết bị đo và điều "
      "khiển từ rất sớm, bắt đầu từ ống chân không và sau đó là bóng bán dẫn "
      "ở dạng ban đầu. Máy tính chuyên dụng dựa trên điện tử thông thường đã "
      "được phát triển trong Chiến tranh thế giới thứ hai, nhưng nhanh chóng "
      "các nhà thiết kế nhận ra bản chất đa dụng của cỗ máy kỳ diệu mà họ "
      "tạo ra. Chiếc máy tính này cùng những máy tính ra đời sau đó đều dựa "
      "trên ý tưởng đổi mới về chương trình được lưu trữ và tổ chức dữ liệu, "
      "được gọi là kiến trúc John Von Neumann để vinh danh người thiết kế.",
      "Conventional electronics entered the field of instrumentation and "
      "control long back starting from vacuum tubes and later on transistors "
      "in their original form. Conventional electronic-based dedicated "
      "computer was developed during world war II but soon the designer came "
      "to know the general-purpose nature of the wonder machine they "
      "designed. This computer and the successive computers that came into "
      "existence, later on are all based upon the innovative concept of "
      "stored program and data organization, which was called John Von "
      "Neumann architecture in the honour of the designer.")

    P(b, lang,
      "Đây là cách phân loại hệ thống máy tính của Von Neumann; cách phân "
      "loại kia được gọi là phân loại Flynn. Chính John Von Neumann, với nỗ "
      "lực đổi mới của mình, là người đầu tiên trình bày khái niệm Chương "
      "trình được lưu trữ và đồng thời mô tả tính chất đa dụng của máy tính. "
      "Ngay cả ngày nay, đa số máy tính vẫn dựa trên kiến trúc cơ bản này. "
      "Hạn chế duy nhất của những máy tính được thiết kế ban đầu là CPU "
      "(Bộ xử lý trung tâm) được cấu tạo từ nhiều linh kiện.",
      "This is Von Neumanns classification of computer system, the other "
      "classification is called Flynns classification. It was the innovative "
      "effort of John Von Neumann who for the first time presented the Stored "
      "Program concept and described the general-purpose nature of the "
      "computer as well. Even today the majority of the computers are based "
      "upon this basic architecture. The only limitation of the earlier "
      "designed computer was that CPU (Central Processing Unit) was made of "
      "many components.")

    P(b, lang,
      "Sau đó, một sự đổi mới khác lại xuất hiện, vẫn dựa hoàn toàn trên khái "
      "niệm chương trình được lưu trữ nhưng đã tích hợp gần như toàn bộ các "
      "thành phần của CPU trên một chip IC (mạch tích hợp). Toàn bộ chức năng "
      "của CPU được triển khai trên chip IC LSI (tích hợp quy mô lớn) và được "
      "gọi là bộ vi xử lý. Việc thiết kế bộ vi xử lý là một bước tiến lớn "
      "hướng tới thu nhỏ kích thước và tăng tính đa dụng. Đặc tính nổi bật "
      "của bộ vi xử lý là khả năng lập trình, và chính điều này làm cho nó "
      "trở thành một thiết bị mang tính tổng quát hơn. Sự kết hợp giữa thu "
      "nhỏ kích thước và khả năng lập trình hấp dẫn đến mức hầu hết các thiết "
      "bị gia dụng lẫn thiết bị giải trí đều được tự động hóa bằng bộ vi xử lý.",
      "Then another innovative changes came into existence based upon the "
      "same stored Program concept altogether but integrated almost all the "
      "components of the CPU on a single IC chip (Integrated Circuit Chip). "
      "The complete CPU functioning was implemented on LSI (large-scale "
      "integration) IC chip and was called as Microprocessor. The design of "
      "microprocessor was a great step towards miniaturisation as well as "
      "more generalization. The great characteristics of a microprocessor is "
      "its programmability and that makes it a more general item. The "
      "characteristics of miniaturization and programmability put together "
      "was so attractive that almost all domestic as well as entertainment "
      "appliances were automated by using microprocessor.")

    P(b, lang,
      "Các chức năng cụ thể của bộ vi xử lý là: (i) xử lý dữ liệu, (ii) các "
      "phép toán toán học và (iii) các phép toán luận lý. Ba chức năng này rất "
      "quan trọng vì bất kỳ bài toán nào cũng có thể được giải quyết bằng "
      "cách kết hợp cả ba. Hầu hết mọi thao tác thực tế về cơ bản đều liên "
      "quan đến một hoặc tất cả các chức năng này.",
      "The specific functions of a microprocessor are: (i) Data processing, "
      "(ii) mathematical operations, and (iii) logical operations. These "
      "three functions are very important because any problem can be solved "
      "by combining these three functions. Almost all practical operations "
      "involve essentially either or all of these functions.")

    P(b, lang,
      "Trong lĩnh vực thiết bị đo và điều khiển, bộ vi xử lý đã thâm nhập "
      "ngay sau khi ra đời. Trên thực tế, cả ba chức năng của bộ vi xử lý đều "
      "được sử dụng trong thiết bị đo. Vì vậy, chúng ta định nghĩa: bất kỳ sơ "
      "đồ thiết bị đo nào sử dụng bộ vi xử lý để thực hiện các thao tác đo, "
      "hiển thị và điều khiển đều được gọi là hệ thống thiết bị đo dựa trên "
      "vi xử lý. Như chúng ta đã biết, có ba khối chức năng cơ bản xác định "
      "toàn bộ hệ thống thiết bị đo như thể hiện trong Hình 8.1.",
      "As far as the field of instrumentation and control is concerned, "
      "microprocessor entered this field immediately after its birth. In "
      "fact, all three functions of microprocessor is utilized in "
      "instrumentation. Thus, we define that in any instrumentation scheme "
      "where a microprocessor has been invariably employed for carrying out "
      "measurement, display and control operations is known as "
      "microprocessor-based instrumentation system. As we are aware, there "
      "are three basic functional blocks which define the complete "
      "instrumentation system as shown in Figure 8.1.")

    FIG(b, 1, F.fig_f01(), lang)

    L(b, lang,
      ["Hệ thống đo: tính năng thông minh; điều chỉnh hiệu chuẩn từ xa và "
       "các thao tác lập trình khác.",
       "Thiết bị hiển thị: chức năng máy ghi và chỉ thị có thể lập trình.",
       "Tác động điều khiển: tạo ra các tác động điều khiển nhanh và chính "
       "xác với các chức năng lập trình."],
      ["Measurement systems: smart functions; remote calibration adjustment "
       "and other programming operations.",
       "Display devices: programmable recorder and indication functions.",
       "Control actions: generation of fast and precise control actions with "
       "programmable functions."],
      ordered=False)

    P(b, lang,
      "Hệ thống đo là thao tác khởi đầu chính của hệ thống, và giá trị đo "
      "được hiển thị hoặc ghi lại trên các thiết bị hiển thị. Đối với sơ đồ "
      "thiết bị đo hở, như vậy là hoàn tất chức năng của một thao tác công "
      "nghệ cụ thể. Nhưng đối với sơ đồ kín, việc tạo ra tác động điều khiển "
      "mong muốn (dựa trên giá trị đo được hiển thị) và đưa tác động đó vào "
      "quá trình thông qua các phần tử điều khiển cuối phù hợp là cần thiết.",
      "The measurement system constitutes the primary initiating operation "
      "of the system and the measured value is displayed or recorded on the "
      "display devices. For an open loop instrumentation scheme, this "
      "completes the function for a particular process operation. But for a "
      "closed loop scheme, the generation of desired control action (based "
      "upon measured display) and its incorporation into the process through "
      "suitable final control elements becomes necessary.")

    P(b, lang,
      "Việc dùng bộ vi xử lý trong hệ thống đo bổ sung các tính năng thông "
      "minh ngoài việc cung cấp tùy chọn hiệu chuẩn từ xa cũng như mọi thao "
      "tác lập trình khác theo yêu cầu. Các chức năng thông minh trong hệ "
      "thống đo bao gồm điều hòa tín hiệu số cùng với khả năng truyền tín "
      "hiệu tương tự ở dạng 4 đến 20 mA. Điều hòa tín hiệu số bao gồm hiệu "
      "chỉnh theo sự thay đổi nhiệt độ môi trường, tuyến tính hóa và bù trừ "
      "các thay đổi áp suất tĩnh trong quá trình. Trong khi truyền tín hiệu "
      "tương tự 4 đến 20 mA, một tín hiệu tương đương ở dạng số cũng chạy "
      "đồng thời trên cùng một cáp mà không gây nhiễu lẫn nhau.",
      "Use of microprocessor in measurement system adds smart features in "
      "addition to providing remote calibration options as well as other "
      "programming operations whatsoever required. Smart functions in a "
      "measurement system includes digital signal conditioning with the "
      "availability of analog signal transmission in 4 to 20 mAmps form. "
      "Digital signal conditioning includes correction in ambient "
      "temperature variation, linearisation and compensation in static "
      "pressure variations in the process. On the way of 4 to 20 mAmps analog "
      "signal transmission equivalent signal in the digital form also run "
      "simultaneously on the same cable without interfering each other.")

    P(b, lang,
      "Tùy chọn hiệu chuẩn từ xa cung cấp các phương pháp hiệu chuẩn lại cũng "
      "như kiểm tra lại và thay đổi dải hiệu chuẩn từ giao diện người vận "
      "hành đặt trong phòng điều khiển trung tâm hoặc bằng bộ truyền thông "
      "HART từ bất kỳ đâu trong hiện trường. Các tiện ích lập trình cho phép "
      "lập trình cho hệ thống đo thực hiện bất kỳ thao tác nào mà hệ thống "
      "có khả năng thực hiện.",
      "Remote calibration option provides methods for recalibration as well "
      "as rechecking, changing calibration ranges from the operator "
      "interface located inside the central control room or by means of HART "
      "communicator from anywhere in the field. Programming facilities allow "
      "to program the measurement system for any operation, the system is "
      "capable of performing as such.")

    P(b, lang,
      "Việc dùng bộ vi xử lý trong thiết bị hiển thị làm tăng hiệu quả hiển "
      "thị cũng như tốc độ đáp ứng. Trong hệ thống ghi, bộ vi xử lý thực hiện "
      "các phép toán luận lý ngoài việc tuyến tính hóa.",
      "Use of microprocessor in display device increases the effectiveness "
      "of display as well as speed of response. In a recording system, "
      "microprocessor performs logical operation in addition to "
      "linearisation.")

    P(b, lang,
      "Chi tiết kiến trúc của bộ vi xử lý không bao gồm các thiết bị ngoại vi "
      "như bộ nhớ, hệ thống I/O, bus ngoài, v.v. Khi một bộ vi xử lý được "
      "tích hợp với các thiết bị ngoại vi kể trên, nó trở thành một vi tính "
      "như thể hiện trong Hình 8.2.",
      "The architectural details of microprocessor does not include the "
      "peripherals like memory, I/O system, external bus, etc. When a "
      "microprocessor is integrated with above peripherals, they take the "
      "form of a microcomputer as shown in Figure 8.2.")

    FIG(b, 2, F.fig_f02(), lang)

    P(b, lang,
      "Khi một bộ vi xử lý được tích hợp với bộ nhớ (chứa chương trình và dữ "
      "liệu được lưu trữ) cũng như các thiết bị I/O, về cơ bản trên một chip "
      "IC duy nhất, và được chuyên dụng cho các ứng dụng điều khiển, thì tập "
      "hợp đó được gọi là bộ vi điều khiển đơn trạm. Bộ vi điều khiển này tạo "
      "ra các tác động điều khiển cần thiết nhờ các phép toán toán học và "
      "luận lý sau khi xử lý dữ liệu đầu vào từ hệ thống đo. Dữ liệu đầu ra của "
      "bộ điều khiển sau đó được xử lý và gửi tới phần tử điều khiển cuối để "
      "chuẩn hóa các nhiễu loạn của quá trình bằng cách thay đổi các thông "
      "số công nghệ.",
      "When a microprocessor is integrated with memory (having stored "
      "program and data) as well as I/O devices essentially on a single IC "
      "chip and is dedicated for control applications, the combination is "
      "known as single station micro-controller. This microcontroller "
      "generates necessary control actions by the help of mathematical and "
      "logical operations after processing the input data from the "
      "measurement system. The controller output data is then processed and "
      "sent to final control element for normalizing the process disturbances "
      "by manipulating the process parameters.")

    return b
