# -*- coding: utf-8 -*-
"""Book 7, Chapter 4 — The Self-Acting Regulator: Why Not? (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
21-23 (PDF pp. 28-30). One source figure (4-1) and two references.
"""
from cvp_common import (fig, h2, h3, note, p, refs)
import cvpfig as F

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "The Self-Acting Regulator: Why Not?"
TITLE_VI = "Bộ điều chỉnh tự tác dụng: tại sao không?"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 4.</b> bộ điều chỉnh tự tác dụng (self-acting "
                "regulator) · bộ điều chỉnh giảm áp (pressure-reducing regulator) · bộ "
                "điều chỉnh áp suất ngược (backpressure regulator) · cảm biến quá trình · "
                "bộ lọc–giảm áp khí (air set) · bộ định vị van (valve positioner) · đáp ứng "
                "tần số · dải điều tiết (rangeability) · dải tỷ lệ (proportional band) · "
                "tác dụng reset · kiểu tác dụng trực tiếp / điều khiển thí điểm (direct / "
                "pilot-operated) · màng (diaphragm) · hệ số lưu lượng C<sub>v</sub> · khí "
                "đệm (blanketing gas) · gia nhiệt bằng hơi (steam tracing) · áp suất đột "
                "biến (surge pressure) · ống dẫn áp hạ lưu (sensing line) · rung cộng "
                "hưởng · hỏng mỏi (fatigue failure).")
    return ("<b>Key terms.</b> self-acting regulator · pressure-reducing regulator · "
            "backpressure regulator · process sensor · air set · valve positioner · "
            "frequency response · rangeability · proportional band · reset action · "
            "direct / pilot-operated · diaphragm · C<sub>v</sub> flow coefficient · "
            "blanketing gas · steam tracing · surge pressure · sensing line · resonant "
            "vibration · fatigue failure.")


def body_vi():
    b = []
    b.append(h2("Một hệ thống điều khiển hoàn chỉnh trong một thiết bị",
                "A complete control system in one device"))
    b.append(p("Bộ điều chỉnh tự tác dụng là một hệ thống điều khiển hoàn chỉnh, tương đối "
               "rẻ tiền, kết hợp cảm biến quá trình, bộ điều khiển và van điều khiển trong "
               "cùng một thiết bị. Đáng buồn là thị phần của thiết bị này đang tàn lụi vì "
               "bị lãng quên hoàn toàn. Nếu được sử dụng đúng cách, bộ điều chỉnh có thể "
               "thay thế van điều khiển trong ít nhất 25% số vòng điều khiển. Tuy nhiên, "
               "chúng hiếm khi được quy định trong một vòng quá trình, vì kỹ sư thiết bị "
               "đo lường không quen thuộc với chúng. Thế nhưng hầu như bộ định vị van nào "
               "cũng đi kèm với bộ lọc–giảm áp khí (air set) của riêng nó, và đó chẳng qua "
               "chính là một bộ điều chỉnh áp suất khí độc lập."))

    b.append(h2("Ưu điểm", "Advantages"))
    b.append(p("Bộ điều chỉnh có một số ưu điểm ngoài chi phí [1]. Chúng có đáp ứng tần số "
               "rất tốt (thực tế là trong vài mili-giây), dải điều tiết rộng, tiết kiệm "
               "không gian, thường không bị rò rỉ thân van và không cần khí nén hay điện "
               "để hoạt động. Ở đây, chính chất lưu công nghệ — có thể là chênh áp qua van "
               "hoặc chênh lệch nhiệt độ — cung cấp năng lượng cần thiết để vận hành van."))

    b.append(h2("Nhược điểm và giới hạn", "Disadvantages and limitations"))
    b.append(p("Các nhược điểm gồm: dải tỷ lệ cố định (thường là 25% với kiểu tác dụng trực "
               "tiếp và 5% với kiểu điều khiển thí điểm), không có tác dụng reset (tích "
               "phân), kích cỡ và cấp áp suất hạn chế, và lựa chọn vật liệu cùng kiểu nối "
               "đầu hạn chế. Chỉ số C<sub>v</sub> tối đa thường chỉ bằng khoảng một nửa của "
               "van điều khiển, nhưng vẫn đủ cho các lắp đặt theo cỡ đường ống."))

    b.append(h2("An toàn: khi màng bị hỏng thì sao?",
                "Safety: what if the diaphragm fails?"))
    b.append(p("Một lưu ý quan trọng về an toàn là các bộ điều chỉnh kiểu giảm áp, có lò xo, "
               "sẽ mở hoàn toàn nếu màng vận hành bị hỏng! Vì vậy, điều quan trọng là phải "
               "đảm bảo đường ống hạ lưu chịu được điều kiện áp suất thượng lưu; nếu "
               "không, phải lắp một van an toàn ở hạ lưu có khả năng xử lý lưu lượng tối đa "
               "của bộ điều chỉnh. Các bộ điều chỉnh áp suất ngược (backpressure) có lò xo "
               "(xem Hình 4-1) sẽ đóng khi màng hỏng, do đó nên lắp một thiết bị dự phòng "
               "tương tự để bảo vệ hệ thống đường ống thượng lưu."))
    b.append(fig(1, F.fig_f41()))
    b.append(p("Dù vậy, khi ứng dụng đòi hỏi điều khiển đơn giản cho khí đệm (blanketing "
               "gas) trong bình chứa, gia nhiệt bằng hơi cho đường ống dầu thô, hoặc các "
               "vòng phụ khác, bộ điều chỉnh nên được cân nhắc nghiêm túc [2]. Ví dụ, bộ "
               "điều chỉnh giảm áp được dùng rộng rãi trong hệ thống phân phối khí tự "
               "nhiên. Chúng cũng có thể là lời giải cho những ứng dụng mà phản ứng nhanh "
               "với sự nhiễu loạn của quá trình là bắt buộc. Những thiết bị này thường "
               "được gọi là bộ điều chỉnh áp suất ngược. Ở đây, bộ điều chỉnh đóng vai trò "
               "như một van an toàn. Một ứng dụng điển hình là điều khiển áp suất đột biến "
               "(surge pressure) trong đường ống."))

    b.append(h2("Một lời cảnh báo: mất ổn định", "A caution: instability"))
    b.append(p("Bộ điều chỉnh độc lập có thể gây mất ổn định trong một số điều kiện dòng "
               "chảy nhất định. Điều này có thể dẫn đến rung cộng hưởng của các bộ phận "
               "chuyển động, lần lượt gây hỏng mỏi cho các màng kim loại."))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(refs([
        "R. L. Moore, “The Use and Misuse of Pressure Regulators,” <i>Instrumentation "
        "Technology</i> (March 1969): 52–56.",
        "H. D. Baumann, “Regulator or Control Valve,” <i>ISA Journal</i> (December "
        "1965): 51–52.",
    ]))
    b.append(note("Nguyên bản có một số dấu gạch nối khi xuống dòng (“com-bines”, "
                  "“regula-tors”, “oth-erwise”, “back-pressure”). Chú thích Hình 4-1 mô tả "
                  "bộ điều chỉnh giảm áp, nhưng văn bản lại viện dẫn hình này trong đoạn "
                  "nói về bộ điều chỉnh áp suất ngược; bản dịch giữ nguyên cách viện dẫn "
                  "của tác giả. Ống dẫn áp hạ lưu được vẽ dạng sơ đồ trong bản vẽ lại dù "
                  "nguyên bản ghi là “not shown”."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 4 chiếm tr. in 21–23 của ấn bản in (PDF tr. 28–30). Nguyên bản có "
               "một hình (Hình 4-1) và hai tài liệu tham khảo; cả hai đều được giữ nguyên. "
               "Hình được vẽ lại dạng vector."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("A complete control system in one device",
                "Một hệ thống điều khiển hoàn chỉnh trong một thiết bị"))
    b.append(p("The self-acting regulator is a relatively inexpensive, complete control "
               "system that combines the process sensor, the controller, and the control "
               "valve all in one. Sadly, the market share of this device is dying out from "
               "sheer neglect. Properly utilized, regulators could replace control valves "
               "in at least 25% of all control loops. However, they are seldom specified "
               "in a process loop because of the instrument engineer's unfamiliarity with "
               "them. Yet almost every valve positioner comes with its own air set, which "
               "is nothing but a self-contained air pressure regulator."))

    b.append(h2("Advantages", "Ưu điểm"))
    b.append(p("Regulators offer several advantages in addition to cost [1]. They provide "
               "an excellent frequency response (in virtually milliseconds), offer "
               "excellent rangeability, are space saving, usually have no stem leakage, "
               "and do not require air or electricity to operate. Here, the process fluid "
               "itself, perhaps the differential pressure across the valve or a temperature "
               "differential, provides the necessary energy to operate the valve."))

    b.append(h2("Disadvantages and limitations", "Nhược điểm và giới hạn"))
    b.append(p("The disadvantages are fixed proportional band (typically 25% for direct "
               "and 5% for pilot-operated models), no reset action, limited sizes and "
               "pressure ratings, and limited choice of materials and end connections. "
               "The maximum C<sub>v</sub> rating is usually about one-half that of a "
               "control valve, which is still adequate for line-size installations."))

    b.append(h2("Safety: what if the diaphragm fails?",
                "An toàn: khi màng bị hỏng thì sao?"))
    b.append(p("An important safety consideration is the fact that spring-loaded, "
               "pressure-reducing types of regulators will open fully if the operating "
               "diaphragm fails! It is therefore important to make sure the downstream "
               "piping can withstand upstream pressure conditions; otherwise, a downstream "
               "relief valve that can handle the maximum flow of the regulator must be "
               "installed. Spring-loaded, backpressure regulators (see Figure 4-1) will "
               "close on diaphragm failure; therefore, it is advised to install a similar "
               "backup for protection of the upstream piping system."))
    b.append(fig(1, F.fig_f41()))
    b.append(p("Nevertheless, when the application calls for simple control of a blanketing "
               "gas in a tank, the steam tracing of a crude oil pipe, or other secondary "
               "loop applications, regulators should be given serious consideration [2]. "
               "For example, pressure-reducing regulators are widely used in natural gas "
               "distribution systems. They may also be the answer to applications where a "
               "fast reaction to a process upset is a must. These are typically called "
               "back pressure regulators. Here a regulator is acting like a safety relief "
               "valve. One typical application is for surge pressure control in pipelines."))

    b.append(h2("A caution: instability", "Một lời cảnh báo: mất ổn định"))
    b.append(p("Self-contained regulators can cause instability under certain flow "
               "conditions. This can lead to resonant vibration of the moving parts which, "
               "in turn, can create fatigue failure of metal diaphragms."))

    b.append(h3("References", "Tài liệu tham khảo"))
    b.append(refs([
        "R. L. Moore, “The Use and Misuse of Pressure Regulators,” <i>Instrumentation "
        "Technology</i> (March 1969): 52–56.",
        "H. D. Baumann, “Regulator or Control Valve,” <i>ISA Journal</i> (December "
        "1965): 51–52.",
    ]))
    b.append(note("The printed pages contain several line-break hyphenations (“com-bines”, "
                  "“regula-tors”, “oth-erwise”, “back-pressure”). The Figure 4-1 caption "
                  "describes a pressure-reducing regulator, yet the prose cites the figure "
                  "in the passage about backpressure regulators; the translation retains "
                  "the author's citation. The downstream sensing line is drawn "
                  "schematically in the redraw although the source caption marks it "
                  "“not shown”."))
    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 4 occupies printed pp. 21-23 (PDF pp. 28-30). The source has one "
               "figure (Figure 4-1) and two references; both are retained. The figure is "
               "redrawn as a vector."))
    return "".join(b)
