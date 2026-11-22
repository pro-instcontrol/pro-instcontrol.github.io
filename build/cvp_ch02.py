# -*- coding: utf-8 -*-
"""Book 7, Chapter 2 — Why Not Use a Speed-Controlled Pump? (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed., printed pp. 9–11 (PDF pp. 17–19).
No figures in this chapter. Three references.
"""
from cvp_common import (h2, h3, note, p, refs, ul)

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Why Not Use a Speed-Controlled Pump?"
TITLE_VI = "Tại sao không dùng bơm điều chỉnh tốc độ?"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 2.</b> bơm điều chỉnh tốc độ (speed-controlled pump) · "
                "bộ truyền tốc độ thay đổi (variable-speed drive) · ổ đĩa tần số thay đổi "
                "(VFD) · hệ số hiệu suất · cột áp (head) · tổn thất áp suất · entropy · "
                "van phục hồi áp suất cao (high-recovery valve) · định cỡ van · vùng chết "
                "của van.")
    return ("<b>Key terms.</b> speed-controlled pump · variable-speed drive · variable "
            "frequency drive (VFD) · converter efficiency · pump head · pressure drop · "
            "entropy · high-recovery valve · valve sizing · valve deadband.")


def body_vi():
    b = []
    b.append(h2("Lời giải “thoạt nhìn là hoàn hảo”",
                "The seemingly ideal solution"))
    b.append(p("Khi phương tiện điều khiển điện tử tốc độ của động cơ điện xuất hiện vào giữa "
               "những năm 1970, một ý nghĩ lập tức nảy ra: tại sao không thay đổi tốc độ hay "
               "số vòng quay của bơm để điều khiển lưu lượng chất lỏng trong hệ thống điều "
               "khiển quá trình? Giải pháp thoạt nhìn là hoàn hảo này đã khiến chủ nhân của "
               "một công ty dầu lớn mua lại một công ty điện tử lớn."))
    b.append(p("Than ôi, mọi thứ không đơn giản như vậy. Thứ nhất, việc định cỡ van điều "
               "khiển hiện đại, cộng với sự xuất hiện của van điều khiển quay có lưu lượng "
               "vốn lớn hơn, đã dẫn đến việc dùng bơm có cột áp thấp hơn — và do đó "
               "<b>ít “lãng phí” năng lượng hơn</b>, tức tổn thất áp suất qua van điều "
               "khiển. Năng lượng có vẻ “bị lãng phí” với ta vì tác dụng tiết lưu của van "
               "là một quá trình nhiệt động không thuận nghịch, làm <b>tăng entropy</b> của "
               "chất lưu; năng lượng trong chất lưu vì thế ở trạng thái thấp hơn, ít hữu "
               "dụng hơn. Nói thực tế, ta tiêu thụ nhiều điện năng hơn mức cần thiết. (Xem "
               "Chương 6, “Van phục hồi áp suất cao”, để biết giải pháp thay thế.)"))

    b.append(h2("Hiệu suất của bộ biến đổi tốc độ",
                "Converter efficiency"))
    b.append(p("Tiếc là việc giảm tốc độ của bơm do động cơ điện dẫn động không tiết kiệm "
               "như tưởng tượng ban đầu. Sau khi lưu lượng giảm, phần lớn năng lượng tiết "
               "kiệm được ở bơm lại chuyển thành <b>nhiệt vô ích trong chính động cơ</b>. "
               "Hầu hết các lập luận tiết kiệm năng lượng chỉ tập trung vào công suất tiết "
               "kiệm tại động cơ điện, nhưng lại <b>quên mất hiệu suất thấp của bộ biến đổi "
               "dòng hoặc điện áp</b> — có thể thấp tới 10% khi động cơ chạy tốc độ thấp "
               "[1, 2]. (Để kiểm chứng tổn thất nhiệt, chỉ cần nhìn vỏ tản nhiệt có gân của "
               "bộ biến đổi.)"))
    b.append(p("Ổ đĩa tần số thay đổi (VFD) có hiệu suất từ <b>70% đến 75%</b> ở mức 40% "
               "tốc độ bơm tối đa. Ổ đĩa điện áp thay đổi còn tệ hơn — hiệu suất ở 40% tốc "
               "độ chỉ khoảng <b>20%</b>. Điều này chắc chắn triệt tiêu mọi khoản tiết kiệm "
               "có được nhờ cột áp bơm thấp hơn."))

    b.append(h2("Khi nào lập luận kinh tế mới đứng vững?",
                "When do the economic arguments hold?"))
    b.append(p("Lập luận kinh tế cho bơm điện điều chỉnh tốc độ chỉ đứng vững trong những "
               "hệ thống mà bơm <b>được cố tình chọn quá lớn</b>, bắt van điều khiển phải "
               "giảm khoảng 30% cột áp sẵn có ở lưu lượng định mức. Đó đơn giản là "
               "<b>định cỡ van kém</b>. Tỷ lệ đúng chỉ nên là <b>5% đến 10%</b> (xem Chương "
               "5, “Định cỡ van dễ dàng”). Cần nhớ rằng ở một số đường ống, tổn thất áp suất "
               "qua van chỉ bằng <b>1/2% tổng áp suất hệ thống</b> ở lưu lượng lớn nhất! Một "
               "lợi thế của bơm điều chỉnh tốc độ tồn tại khi <b>áp suất tĩnh của hệ thống "
               "tương đối thấp và lưu lượng tương đối không đổi</b>. Tuy nhiên đây là trường "
               "hợp hiếm."))
    b.append(p("Những lập luận khác <b>chống lại</b> việc điều chỉnh tốc độ điện của bơm [3]:"))
    b.append(ul([
        "vốn đầu tư cao (trung bình gấp đôi giá của một van);",
        "hiệu năng động kém so với van cỡ nhỏ và trung bình;",
        "yêu cầu bảo trì cao hơn;",
        "giới hạn lưu lượng tối thiểu do sinh nhiệt trong chất lỏng được bơm.",
    ]))

    b.append(h2("Vẫn có chỗ cho bơm điều chỉnh tốc độ",
                "There are still applications for speed control"))
    b.append(p("Dù tôi có vẻ tiêu cực về chủ đề này, vẫn có những ứng dụng mà bơm hay quạt "
               "điều chỉnh tốc độ được ưu tiên — chẳng hạn khi bơm một chất lỏng ăn mòn mạnh "
               "(và động học quá trình cho phép). Khi đó ta tránh được chi phí của một van "
               "hợp kim đặc biệt. Cũng có thể lập luận tương tự cho chất lưu nguy hiểm như "
               "kim loại nóng chảy. Điều khiển tốc độ có thể cải thiện hiệu năng vòng điều "
               "khiển nhờ <b>không có vùng chết của van</b> trong các ứng dụng như điều "
               "khiển áp suất lò hơi (điều khiển tốc độ quạt cấp không khí cháy)."))
    b.append(p("Đôi khi sự kết hợp giữa <b>điều chỉnh tốc độ bơm</b> (bằng điện tử hoặc bằng "
               "cơ khí như puly có thể chỉnh) và một <b>van điều khiển</b> lại có lợi để "
               "phối hợp cột áp bơm với yêu cầu lý tưởng của quá trình. Các hệ thống như "
               "vậy được dùng, chẳng hạn, trong hệ thống trao đổi nhiệt dòng chảy tầng tại "
               "nhà máy chế tạo chip."))
    b.append(p("Có một lập luận hoàn toàn khác nếu việc điều chỉnh tốc độ bơm dùng "
               "<b>nguồn năng lượng khác</b> thay vì điện năng tương đối đắt. Có thể viện "
               "dẫn các bơm dẫn động bằng động cơ diesel để điều khiển áp suất trong đường "
               "ống dầu, hoặc dùng hơi nước trong nhà máy điện để cấp cho bơm nước cấp dẫn "
               "động bằng tua-bin, thay thế cho các van điều khiển trước đây."))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(refs([
        "H. D. Baumann, “Control Valve versus Variable-Speed Pump,” <i>Chemical "
        "Engineering</i> (June 29, 1981): 81–84.",
        "B. G. Lipták, <i>Instrument Engineers' Handbook: Process Control and "
        "Optimization</i>, 4th ed. (Boca Raton, FL: Taylor &amp; Francis, 2005): 1465.",
        "W. R. Wood, “Beware of Pitfalls When Applying Variable Frequency Drives,” "
        "<i>Power</i> (February 1987): 47–49.",
    ]))
    b.append(note("Nguyên bản có một lỗi chính tả ở đoạn về tổn thất nhiệt; bản dịch hiệu "
                  "theo nghĩa đúng là “bộ biến đổi dòng hoặc điện áp”."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 2 chiếm tr. 9–11 của ấn bản in (PDF tr. 17–19). Nguyên bản không có "
               "hình vẽ trong chương này; ba tài liệu tham khảo được giữ nguyên."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("The seemingly ideal solution", "Lời giải “thoạt nhìn là hoàn hảo”"))
    b.append(p("When the means to electronically control the speed of an electric motor "
               "became available in the mid-1970s, a thought immediately occurred: Why not "
               "vary the speed or number of revolutions of pumps in order to control the "
               "flow rate of liquids in process control systems? This seemingly ideal "
               "solution led the owners of a major oil company to purchase a large "
               "electronics company."))
    b.append(p("Alas, things did not turn out to be that simple. For one thing, modern "
               "sizing of control valves, coupled with the introduction of rotary control "
               "valves with higher inherent flow capacities, led to the use of pumps with "
               "smaller head pressures and therefore less “waste” of energy, that is, a "
               "pressure drop across the control valve. Energy seems “wasted” to us because "
               "the throttling action of a valve is a thermodynamically non-reversible "
               "process and, therefore, increases the “entropy” of the fluid; thus, the "
               "energy within the fluid is at a lower, less available state. In practical "
               "terms, we consume more electric power than we should. As an alternative, "
               "see Chapter 6, “High-Recovery Valves.”"))

    b.append(h2("Converter efficiency", "Hiệu suất của bộ biến đổi tốc độ"))
    b.append(p("Unfortunately, reducing the speed of an electric motor-driven pump was not "
               "as economical as first thought. Following a flow reduction, most of the "
               "energy savings at the pump is converted into useless heat within the motor. "
               "Most energy-saving arguments center around the power saved at the electric "
               "motor. However, these arguments invariably omit the low efficiency of the "
               "current or voltage converters, which can be as low as 10% at low motor "
               "speed [1, 2]. (To verify heat loss, one can look at the ribbed converter "
               "housings.)"))
    b.append(p("Variable frequency drives have efficiencies of between 70% and 75% at 40% "
               "of maximum pump speed. Variable voltage drives are even worse — the "
               "efficiency at 40% speed is as low as 20%. This certainly would negate any "
               "savings derived from lower pump head."))

    b.append(h2("When do the economic arguments hold?",
                "Khi nào lập luận kinh tế mới đứng vững?"))
    b.append(p("Economic arguments for speed-controlled electric motor-driven pumps can be "
               "made only in systems where the pump is deliberately oversized, forcing the "
               "control valve to reduce perhaps 30% of the available pump head pressure at "
               "the rated flow rate. This is simply bad control valve sizing. It should be "
               "only 5% to 10% (see Chapter 5, “Valve Sizing Made Easy”). Keep in mind that "
               "in certain pipelines the control valve pressure drop is as low as 1/2% of "
               "the total system pressure at maximum flow rate! An advantage for "
               "speed-controlled pumps exists where the static pressure of the system is "
               "relatively low and the flow is relatively constant. However, this is a rare "
               "occurrence."))
    b.append(p("Other arguments against electric speed control of pumps [3] are"))
    b.append(ul([
        "high capital investment (averages twice the price of a valve),",
        "poor dynamic performance compared to small- and medium-sized valves,",
        "higher maintenance requirements, and",
        "limitation on minimum flow due to heat generation in the pumped liquid.",
    ]))

    b.append(h2("There are still applications for speed control",
                "Vẫn có chỗ cho bơm điều chỉnh tốc độ"))
    b.append(p("While I might seem to be negative on this subject, there are indeed "
               "applications in which a speed-controlled pump or fan is preferred; for "
               "example, if you pump a highly corrosive fluid (and where process dynamics "
               "allow). Here the expense of a special alloy valve can be avoided. Other "
               "cases can be made for dangerous fluids such as molten metal. Speed control "
               "can improve control loop performance due to the absence of valve deadband "
               "on applications such as boiler pressure control (fan speed control of "
               "forced combustion air)."))
    b.append(p("Sometimes the combination of pump speed adjustment (either electronically "
               "or by mechanical means such as adjustable pulleys) and a control valve can "
               "be beneficial to match the pump head to ideal process requirements. Such "
               "systems are used, for example, in laminar flow heat exchange systems in "
               "chip production plants."))
    b.append(p("Quite another argument can be made if the pump speed control is through "
               "energy sources other than relatively expensive electricity. A case can be "
               "made for the diesel engine-driven pumps used to control pressure in oil "
               "pipelines or for utilizing steam in a power plant to feed turbine-driven "
               "feedwater pumps replacing the former control valves."))

    b.append(h3("References", "Tài liệu tham khảo"))
    b.append(refs([
        "H. D. Baumann, “Control Valve versus Variable-Speed Pump,” <i>Chemical "
        "Engineering</i> (June 29, 1981): 81–84.",
        "B. G. Lipták, <i>Instrument Engineers' Handbook: Process Control and "
        "Optimization</i>, 4th ed. (Boca Raton, FL: Taylor &amp; Francis, 2005): 1465.",
        "W. R. Wood, “Beware of Pitfalls When Applying Variable Frequency Drives,” "
        "<i>Power</i> (February 1987): 47–49.",
    ]))
    b.append(note("The printed page contains a small wording slip in the heat-loss "
                  "sentence; the translation follows the intended meaning — “current or "
                  "voltage converters”."))
    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 2 occupies printed pp. 9–11 (PDF pp. 17–19). The source has no "
               "figures in this chapter; all three references are retained."))
    return "".join(b)
