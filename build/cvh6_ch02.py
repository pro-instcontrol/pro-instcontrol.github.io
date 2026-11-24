# -*- coding: utf-8 -*-
"""Book 7c, Chapter 2 - Control Valve Performance (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 34-53.
The chapter examines dynamic valve performance - deadband, response time,
actuator and positioner design, installed gain, valve style and sizing - and
connects those factors to process variability, economic results and the
ValveLink Signature Series maintenance program. All ten numbered source
figures (2.1-2.10) are redrawn as vector schematics in `cvh6fig.py` and
placed at the points where the source captions occur.
"""

from cvh6_common import (fig, h2, h3, lead, note, p, table, ul)
import cvh6fig as F

PAGES_SRC = 20          # source printed pp. 34-53 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Control Valve Performance"
TITLE_VI = "Hiệu năng của van điều khiển"


def note_terms(lang):
    """A one-line glossary box in the style of Chapter 1."""
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> process variability — biến thiên quá trình · "
                "deadband — vùng chết · backlash — độ hở · shaft wind-up — xoắn trục · "
                "dead time — thời gian chết · dynamic time — thời gian động · T63 — thời gian "
                "đạt 63% đáp ứng · inherent characteristic — đặc tính vốn có · installed "
                "characteristic — đặc tính dòng lắp đặt · installed gain — khuếch đại lắp đặt · "
                "loop gain — khuếch đại vòng · control range — dải điều khiển · "
                "control valve assembly — cụm van điều khiển · positioner — bộ định vị · "
                "Signature Series — chuỗi chữ ký hiệu năng · ValveLink — phần mềm chẩn đoán.")
    return ("<b>Key terms in this chapter.</b> process variability · deadband · backlash · "
            "shaft wind-up · dead time · dynamic time · T63 · inherent characteristic · "
            "installed characteristic · installed gain · loop gain · control range · "
            "control valve assembly · positioner · Signature Series · ValveLink.")


def response_time_table(lang):
    """Reproduce the source table attached to Figure 2.4, in both languages."""
    vi = lang == "vi"
    head = (["Van", "Bước (%)", "T(d) (giây)", "T63 (giây)"] if vi else
            ["Valve", "Step size (%)", "T(d) (s)", "T63 (s)"])
    op = "Mở" if vi else "Opening"
    cl = "Đóng" if vi else "Closing"
    nr = "Không đáp ứng" if vi else "NR"
    groups = [
        ("Valve A (Fisher V150HD/1052(33)/3610J)",
         [(op + " 2", "0.25", "0.34"), (cl + " -2", "0.50", "0.74"),
          (op + " 5", "0.16", "0.26"), (cl + " -5", "0.22", "0.42"),
          (op + " 10", "0.19", "0.33"), (cl + " -10", "0.23", "0.46")]),
        ("Valve B",
         [(op + " 2", "5.61", "7.74"), (cl + " -2", "0.46", "1.67"),
          (op + " 5", "1.14", "2.31"), (cl + " -5", "1.04", "2"),
          (op + " 10", "0.42", "1.14"), (cl + " -10", "0.41", "1.14")]),
        ("Valve C",
         [(op + " 2", "4.4", "5.49"), (cl + " -2", nr, nr),
          (op + " 5", "5.58", "7.06"), (cl + " -5", "2.16", "3.9"),
          (op + " 10", "0.69", "1.63"), (cl + " -10", "0.53", "1.25")]),
    ]
    rows = []
    for group, items in groups:
        rows.append(group)
        rows.extend(items)
    cap = ("Số liệu thử nghiệm Hình 2.4: van cỡ 4 inch, ENTECH SPEC.; NR = không đáp ứng."
           if vi else
           "Figure 2.4 test data: 4 inch valve, ENTECH SPEC.; NR = No Response.")
    return table(head, rows, caption=cap)


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def B(v, e):
        b.append(ul(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn, lang))

    def N(v, e):
        b.append(note(v if vi else e))

    # ------------------------------------------------------------ lead
    b.append(lead(
        "Chương này xem xét các yếu tố quyết định hiệu năng động của cụm van điều khiển — "
        "vùng chết, thời gian đáp ứng, đặc tính lắp đặt và kích cỡ van — và cách các yếu tố "
        "đó ảnh hưởng đến biến thiên quá trình, kết quả kinh tế và công tác bảo trì."
        if vi else
        "This chapter examines the factors that determine the dynamic performance of a control "
        "valve assembly - deadband, response time, installed characteristics and valve sizing - "
        "and how they affect process variability, economic results and maintenance."))
    N(note_terms("vi"), note_terms("en"))

    # ------------------------------------------------------------ opening
    P("Trong môi trường kinh doanh năng động ngày nay, các nhà sản xuất chịu áp lực kinh tế "
      "cực lớn. Toàn cầu hóa thị trường tạo ra áp lực mạnh nhằm giảm chi phí sản xuất để cạnh "
      "tranh với chi phí nhân công và nguyên liệu thấp hơn của các nước đang phát triển. Các "
      "công ty quốc tế cạnh tranh với nhau để cung cấp sản phẩm chất lượng cao nhất và tối đa "
      "hóa năng suất nhà máy với ít nguồn lực hơn, đồng thời đáp ứng nhu cầu luôn thay đổi của "
      "khách hàng. Những thách thức tiếp thị này phải được đáp ứng, nhưng vẫn tuân thủ đầy đủ "
      "các chính sách công cộng và quy định.",
      "In today's dynamic business environment, manufacturers are under extreme economic "
      "pressures. Market globalization is resulting in intense pressures to reduce manufacturing "
      "costs to compete with lower wages and raw material costs of emerging countries. "
      "Competition exists between international companies to provide the highest quality "
      "products and to maximize plant throughputs with fewer resources; all while meeting "
      "ever-changing customer needs. These marketing challenges must be met, although fully "
      "complying with public and regulatory policies.")

    # ------------------------------------------------------------ 2.1
    H("2.1 Biến thiên quá trình", "2.1 Process Variability")
    P("Để mang lại lợi nhuận chấp nhận được cho cổ đông, các nhà lãnh đạo công nghiệp quốc tế "
      "nhận thấy họ phải giảm chi phí nguyên liệu và phế liệu đồng thời tăng năng suất. Giảm "
      "biến thiên quá trình trong các quy trình sản xuất thông qua áp dụng công nghệ điều "
      "khiển quá trình được công nhận là phương pháp hiệu quả để cải thiện lợi nhuận và đáp "
      "ứng áp lực cạnh tranh toàn cầu.",
      "To deliver acceptable returns to their shareholders, international industry leaders are "
      "realizing they must reduce raw material and scrap costs while increasing productivity. "
      "Reducing process variability in the manufacturing processes through the application of "
      "process control technology is recognized as an effective method to improve financial "
      "returns and meet global competitive pressures.")
    P("Mục tiêu cơ bản của một công ty là kiếm lợi nhuận thông qua sản xuất sản phẩm chất "
      "lượng. Sản phẩm chất lượng tuân thủ một tập hợp các đặc tính kỹ thuật. Bất kỳ sai lệch "
      "nào so với đặc tính đã thiết lập đều có nghĩa là mất lợi nhuận do dùng quá nhiều vật "
      "liệu, chi phí xử lý lại hoặc sản phẩm bị bỏ đi. Do đó, cải thiện điều khiển quá trình "
      "mang lại tác động tài chính lớn. Giảm biến thiên quá trình nhờ điều khiển tốt hơn cho "
      "phép tối ưu hóa quy trình và tạo ra sản phẩm đúng ngay từ lần đầu.",
      "The basic objective of a company is to make a profit through the production of a quality "
      "product. A quality product conforms to a set of specifications. Any deviation from the "
      "established specification means lost profit due to excessive material use, reprocessing "
      "costs, or wasted product. Thus, a large financial impact is obtained through improving "
      "process control. Reducing process variability through better process control allows "
      "optimization of the process and the production of products right the first time.")
    P("Sự không đồng nhất vốn có của nguyên liệu và của các quá trình sản xuất là nguyên nhân "
      "chung gây biến thiên, làm cho biến quá trình dao động cả phía trên lẫn phía dưới điểm "
      "đặt. Một quá trình đang được điều khiển, chỉ với các nguyên nhân biến thiên thông "
      "thường, thường tuân theo phân phối chuẩn hình chuông.",
      "The non-uniformity inherent in the raw materials and processes of production are common "
      "causes of variation that produce a variation of the process variable both above and below "
      "the set point. A process that is in control, with only the common causes of variation "
      "present, typically follows a bell-shaped normal distribution.")
    FIG(1, F.fig_f21())
    P("Một dải giá trị suy ra thống kê trên phân phối này, gọi là dải +/-2 sigma, mô tả độ "
      "phân tán của các sai lệch biến quá trình so với điểm đặt. Dải này chính là biến thiên "
      "của quá trình. Nó là thước đo mức độ chặt chẽ mà quá trình được điều khiển. Biến thiên "
      "quá trình là thước đo chính xác độ chặt chẽ của điều khiển và được biểu thị bằng phần "
      "trăm của điểm đặt.",
      "A statistically derived band of values on this distribution, called the +/-2 sigma band, "
      "describes the spread of process variable deviations from the set point. This band is the "
      "variability of the process. It is a measure of how tightly the process is being "
      "controlled. Process variability is a precise measure of tightness of control and is "
      "expressed as a percentage of the set point.")
    P("Ví dụ, nếu một sản phẩm phải đáp ứng giới hạn dưới xác định, điểm đặt cần được thiết lập "
      "ở giá trị cao hơn giới hạn dưới đó hai sigma. Làm vậy đảm bảo mọi sản phẩm tạo ra có "
      "giá trị nằm bên phải giới hạn dưới đều đáp ứng đặc tính chất lượng.",
      "If a product must meet a certain lower limit specification, for example, the set point "
      "needs to be established at a 2 sigma value above this lower limit. Doing so will ensure "
      "that all the product produced at values to the right of the lower limit will meet the "
      "quality specification.")
    P("Tuy nhiên, vấn đề là tiền bạc và nguồn lực đang bị lãng phí khi một tỷ lệ lớn sản phẩm "
      "được chế tạo ở mức cao hơn nhiều so với mức yêu cầu của đặc tính (xem phân phối trên "
      "trong Hình 2.1).",
      "The problem, however, is that money and resources are being wasted by making a large "
      "percentage of the product to a level much greater than required by the specification "
      "(see upper distribution in Figure 2.1).")
    P("Giải pháp mong muốn nhất là giảm độ phân tán của sai lệch quanh điểm đặt bằng cách dùng "
      "van điều khiển có thể tạo sigma nhỏ hơn (xem phân phối dưới trong Hình 2.1).",
      "The most desirable solution is to reduce the spread of the deviation about the set point "
      "by using a control valve that can produce a smaller sigma (see the lower distribution in "
      "Figure 2.1).")
    P("Giảm biến thiên quá trình là chìa khóa để đạt được mục tiêu kinh doanh. Hầu hết công ty "
      "nhận ra điều này, và không hiếm khi họ chi hàng trăm nghìn đô la cho thiết bị đo để giải "
      "quyết vấn đề giảm biến thiên quá trình. Đáng tiếc là van điều khiển thường bị bỏ qua "
      "trong nỗ lực này vì người ta chưa nhận ra tác động của nó tới hiệu năng động. Các nghiên "
      "cứu sâu về vòng điều khiển cho thấy tới 80% vòng không làm tốt việc giảm biến thiên quá "
      "trình. Hơn nữa, van điều khiển được xác định là nguyên nhân chính gây ra vấn đề này vì "
      "nhiều lý do.",
      "Reducing process variability is a key to achieving business goals. Most companies realize "
      "this, and it is not uncommon for them to spend hundreds of thousands of dollars on "
      "instrumentation to address the problem of process variability reduction. Unfortunately, "
      "the control valve is often overlooked in this effort because its impact on dynamic "
      "performance is not realized. Extensive studies of control loops indicate as many as 80% "
      "of the loops did not do an adequate job of reducing process variability. Furthermore, the "
      "control valve was found to be a major contributor to this problem for a variety of reasons.")
    P("Để kiểm chứng hiệu năng, nhà sản xuất phải thử sản phẩm trong điều kiện quá trình động. "
      "Các phép thử này thường được thực hiện trong phòng thí nghiệm dòng chảy, với điều khiển "
      "vòng kín thực tế (Hình 2.2). Đánh giá cụm van điều khiển trong điều kiện vòng kín là cách "
      "duy nhất để đo đúng hiệu năng biến thiên. Số liệu hiệu năng vòng kín chứng minh có thể "
      "giảm đáng kể biến thiên quá trình bằng cách chọn đúng van điều khiển cho ứng dụng.",
      "To verify performance, manufacturers must test their products under dynamic process "
      "conditions. These are typically performed in a flow lab in actual closed-loop control "
      "(Figure 2.2). Evaluating control valve assemblies under closed-loop conditions provides "
      "the only true measure of variability performance. Closed-loop performance data proves "
      "significant reductions in process variability can be achieved by choosing the right "
      "control valve for the application.")
    FIG(2, F.fig_f22())
    P("Khả năng giảm biến thiên quá trình của van điều khiển phụ thuộc vào nhiều yếu tố. Không "
      "thể chỉ xem xét một thông số riêng lẻ. Nghiên cứu trong ngành đã chỉ ra rằng các đặc "
      "điểm thiết kế cụ thể của phần tử điều khiển cuối cùng, gồm van, cơ cấu chấp hành và bộ "
      "định vị, rất quan trọng để đạt được điều khiển quá trình tốt trong điều kiện động. Quan "
      "trọng nhất là cụm van điều khiển phải được tối ưu hoặc phát triển như một chỉnh thể. Các "
      "bộ phận van không được thiết kế như một cụm hoàn chỉnh thường không cho hiệu năng động "
      "tốt nhất.",
      "The ability of control valves to reduce process variability depends upon many factors. "
      "More than one isolated parameter must be considered. Research within the industry has "
      "found the particular design features of the final control element, including the valve, "
      "actuator, and positioner, are very important in achieving good process control under "
      "dynamic conditions. Most importantly, the control valve assembly must be optimized or "
      "developed as a unit. Valve components not designed as a complete assembly typically do "
      "not yield the best dynamic performance.")
    P("Một số yếu tố thiết kế quan trọng nhất gồm:",
      "Some of the most important design considerations include:")
    B(["Vùng chết.",
       "Thiết kế cơ cấu chấp hành và bộ định vị.",
       "Thời gian đáp ứng của van.",
       "Kiểu van và đặc tính hóa.",
       "Kích cỡ van."],
      ["Deadband.",
       "Actuator and positioner design.",
       "Valve response time.",
       "Valve type and characterization.",
       "Valve sizing."])
    P("Mỗi đặc điểm thiết kế này sẽ được xem xét trong chương này để làm rõ thế nào là một "
      "thiết kế van vượt trội.",
      "Each of these design features will be considered in this chapter to provide insight into "
      "what constitutes a superior valve design.")

    # ------------------------------------------------------------ 2.1.1
    H("2.1.1 Vùng chết", "2.1.1 Deadband")
    P("Vùng chết là nguyên nhân chính gây biến thiên quá trình quá mức. Cụm van điều khiển có "
      "thể là nguồn vùng chết chính trong một vòng thiết bị đo vì nhiều lý do như ma sát, độ hở, "
      "xoắn trục, vùng chết của relay hoặc van trượt, v.v.",
      "Deadband is a major contributor to excess process variability. Control valve assemblies "
      "can be a primary source of deadband in an instrumentation loop due to a variety of causes "
      "such as friction, backlash, shaft wind-up, relay or spool valve dead zone, etc.")
    P("Vùng chết là hiện tượng chung trong đó một dải hoặc miền giá trị đầu ra bộ điều khiển "
      "(CO) không tạo ra thay đổi trong biến quá trình đo được (PV) khi tín hiệu đầu vào đổi "
      "chiều. Khi xảy ra nhiễu tải, biến quá trình (PV) lệch khỏi điểm đặt. Sai lệch này khởi "
      "phát hành động hiệu chỉnh thông qua bộ điều khiển và ngược trở lại quá trình. Tuy nhiên, "
      "một thay đổi ban đầu của đầu ra bộ điều khiển có thể không tạo ra thay đổi hiệu chỉnh "
      "tương ứng trong biến quá trình. Chỉ khi đầu ra bộ điều khiển thay đổi đủ để đi qua vùng "
      "chết thì biến quá trình mới thay đổi tương ứng.",
      "Deadband is a general phenomenon where a range or band of controller output (CO) values "
      "fail to produce a change in the measured process variable (PV) when the input signal "
      "reverses direction. When a load disturbance occurs, the process variable (PV) deviates "
      "from the set point. This deviation initiates a corrective action through the controller "
      "and back through the process. However, an initial change in controller output can produce "
      "no corresponding corrective change in the process variable. Only when the controller "
      "output has changed enough to progress through the deadband does a corresponding change "
      "in the process variable occur.")
    P("Bất cứ khi nào đầu ra bộ điều khiển đổi chiều, tín hiệu điều khiển phải đi qua vùng chết "
      "trước khi có bất kỳ thay đổi hiệu chỉnh nào của biến quá trình. Sự hiện diện của vùng "
      "chết trong quá trình đảm bảo sai lệch của biến quá trình so với điểm đặt phải tăng lên "
      "cho đến khi đủ lớn để vượt qua vùng chết. Chỉ khi đó hành động hiệu chỉnh mới có thể "
      "xảy ra.",
      "Any time the controller output reverses direction, the controller signal must pass "
      "through the deadband before any corrective change in the process variable will occur. "
      "The presence of deadband in the process ensures the process variable deviation from the "
      "set point will have to increase until it is big enough to get through the deadband. Only "
      "then can a corrective action occur.")
    FIG(3, F.fig_f23())

    # ------------------------------------------------------------ 2.1.1.1
    H("2.1.1.1 Nguyên nhân của vùng chết", "2.1.1.1 Causes of Deadband", h3)
    P("Vùng chết có nhiều nguyên nhân, trong đó ma sát và độ hở (backlash) trong van điều "
      "khiển, cùng với sự xoắn trục (shaft wind-up) ở van quay và vùng chết của relay, là những "
      "dạng thường gặp hơn. Vì hầu hết hành động điều khiển trong điều khiển điều chỉnh là các "
      "thay đổi nhỏ (1% hoặc nhỏ hơn), một van điều khiển có vùng chết quá lớn có thể thậm chí "
      "không đáp ứng với nhiều thay đổi nhỏ này. Một van được thiết kế tốt nên đáp ứng với tín "
      "hiệu 1% hoặc nhỏ hơn để giảm hiệu quả biến thiên quá trình. Tuy nhiên, không hiếm van có "
      "vùng chết tới 5% hoặc hơn. Trong một cuộc kiểm toán nhà máy gần đây, 30% số van có vùng "
      "chết vượt quá 4%. Hơn 65% vòng được kiểm toán có vùng chết lớn hơn 2%.",
      "Deadband has many causes, but friction and backlash in the control valve, along with "
      "shaft wind-up in rotary valves, and relay dead zone are some of the more common forms. "
      "Because most control actions for regulatory control consist of small changes (1% or "
      "less), a control valve with excessive deadband might not even respond to many of these "
      "small changes. A well-engineered valve should respond to signals of 1% or less to provide "
      "effective reduction in process variability. However, it is not uncommon for some valves "
      "to exhibit deadband as great as 5% or more. In a recent plant audit, 30% of the valves had "
      "deadbands in excess of 4%. Over 65% of the loops audited had deadbands greater than 2%.")

    # ------------------------------------------------------------ 2.1.1.2
    H("2.1.1.2 Ảnh hưởng của vùng chết", "2.1.1.2 Effects of Deadband", h3)
    P("Hình 2.3 cho thấy tác động kết hợp của vùng chết có thể lớn đến thế nào. Sơ đồ này biểu "
      "diễn phép thử vòng hở của ba van điều khiển khác nhau trong điều kiện quá trình bình "
      "thường. Các van được đặt trước một chuỗi tín hiệu bước từ 0,5% đến 10%. Thử nghiệm bước "
      "trong điều kiện có dòng chảy là cần thiết vì nó cho phép đánh giá hiệu năng của toàn bộ "
      "cụm van, thay vì chỉ cụm cơ cấu chấp hành của van như thường thấy trong hầu hết các phép "
      "thử băng.",
      "Figure 2.3 shows just how dramatic the combined effects of deadband can be. This diagram "
      "represents an open-loop test of three different control valves under normal process "
      "conditions. The valves are subjected to a series of step inputs which range from 0.5% to "
      "10%. Step tests under flowing conditions are essential because they allow the performance "
      "of the entire valve assembly to be evaluated, rather than just the valve actuator "
      "assembly as would be the case under most bench test conditions.")

    # ------------------------------------------------------------ 2.1.1.3
    H("2.1.1.3 Thử nghiệm hiệu năng", "2.1.1.3 Performance Tests", h3)
    P("Một số phép thử hiệu năng trên cụm van chỉ so sánh hành trình thân cơ cấu chấp hành với "
      "tín hiệu đầu vào. Cách này gây hiểu lầm vì bỏ qua hiệu năng của chính cái van. Điều quan "
      "trọng là đo hiệu năng động của van trong điều kiện có dòng chảy để có thể so sánh thay "
      "đổi của biến quá trình với thay đổi của tín hiệu đầu vào cụm van. Việc chỉ thân van thay "
      "đổi theo tín hiệu đầu vào ít có ý nghĩa, vì nếu không có thay đổi tương ứng của biến được "
      "điều khiển thì sẽ không có sự hiệu chỉnh nào cho biến quá trình.",
      "Some performance tests on a valve assembly compare only the actuator stem travel versus "
      "the input signal. This is misleading because it ignores the performance of the valve "
      "itself. It is critical to measure dynamic performance of a valve under flowing conditions "
      "so the change in process variable can be compared to the change in valve assembly input "
      "signal. It matters little if only the valve stem changes in response to a change in valve "
      "input because if there is no corresponding change in the controlled variable, there will "
      "be no correction to the process variable.")
    P("Trong cả ba phép thử (Hình 2.3), chuyển động của thân cơ cấu chấp hành bám khá chính xác "
      "theo thay đổi của tín hiệu đầu vào. Mặt khác, có sự khác biệt rõ rệt về khả năng thay đổi "
      "lưu lượng theo tín hiệu đầu vào của mỗi van. Với van A, biến quá trình (lưu lượng) đáp ứng "
      "tốt với tín hiệu đầu vào thấp tới 0,5. Van B cần thay đổi tín hiệu đầu vào tới 5% trước "
      "khi bắt đầu đáp ứng chính xác từng bước. Van C còn tệ hơn, cần thay đổi tín hiệu tới 10% "
      "mới bắt đầu đáp ứng. Khả năng cải thiện biến thiên quá trình của van B và C rất kém.",
      "In all three valve tests (Figure 2.3), the actuator stem motion changes fairly faithfully "
      "in response to the input signal changes. On the other hand, there is a dramatic difference "
      "in each of the valve's ability to change the flow in response to an input signal change. "
      "For Valve A, the process variable (flow rate) responds well to input signals as low as "
      "0.5. Valve B requires input signal changes as great as 5% before it begins responding "
      "faithfully to each of the input signal steps. Valve C is considerably worse, requiring "
      "signal changes as great as 10% before it begins to respond faithfully to each of the "
      "input signal steps. The ability of either Valve B or C to improve process variability is "
      "very poor.")

    # ------------------------------------------------------------ 2.1.1.4
    H("2.1.1.4 Ma sát", "2.1.1.4 Friction", h3)
    P("Ma sát là nguyên nhân chính gây vùng chết trong van điều khiển. Van quay thường rất dễ "
      "chịu ma sát do tải đế van cao cần thiết để đóng kín với một số thiết kế gioăng. Vì ma "
      "sát gioăng lớn và độ cứng của bộ truyền động kém, trục van bị xoắn và không truyền "
      "chuyển động tới phần tử điều khiển. Kết quả là một van quay được thiết kế không đúng cách "
      "có thể có vùng chết đáng kể, rõ ràng gây hại cho biến thiên quá trình.",
      "Friction is a major cause of deadband in control valves. Rotary valves are often very "
      "susceptible to friction caused by the high seat loads required to obtain shutoff with "
      "some seal designs. Because of the high seal friction and poor drive train stiffness, the "
      "valve shaft winds up and does not translate motion to the control element. As a result, "
      "an improperly designed rotary valve can exhibit significant deadband that clearly has a "
      "detrimental effect on process variability.")
    P("Nhà sản xuất thường bôi trơn gioăng van quay trong khi chế tạo, nhưng chỉ sau vài trăm "
      "chu kỳ lớp bôi trơn này bị mòn. Ngoài ra, tải do áp suất cũng gây mòn gioăng. Kết quả là "
      "ma sát van có thể tăng 400% hoặc hơn đối với một số thiết kế. Điều này cho thấy kết luận "
      "hiệu năng gây hiểu lầm có thể xuất hiện khi đánh giá sản phẩm bằng số liệu kiểu băng "
      "trước khi mô-men xoắn ổn định. Van B và C (Hình 2.3) cho thấy tác động tàn phá của hệ số "
      "mô-men ma sát cao hơn đó tới hiệu năng van.",
      "Manufacturers usually lubricate rotary valve seals during manufacture, but after only a "
      "few hundred cycles this lubrication wears off. In addition, pressure-induced loads also "
      "cause seal wear. As a result, the valve friction can increase by 400% or more for some "
      "valve designs. This illustrates the misleading performance conclusions that can result "
      "from evaluating products using bench-type data before the torque has stabilized. Valves B "
      "and C (Figure 2.3) show the devastating effect these higher friction torque factors can "
      "have on a valve's performance.")
    P("Ma sát đệm (packing friction) là nguồn ma sát chính ở van thân trục trượt. Ở các loại van "
      "này, ma sát đo được có thể thay đổi đáng kể giữa các kiểu van và cách bố trí đệm.",
      "Packing friction is the primary source of friction in sliding-stem valves. In these types "
      "of valves, the measured friction can vary significantly between valve styles and packing "
      "arrangements.")
    P("Kiểu cơ cấu chấp hành cũng có tác động sâu sắc tới ma sát của cụm van điều khiển. Nhìn "
      "chung, cơ cấu chấp hành lò xo-màng đóng góp ít ma sát hơn cơ cấu chấp hành piston. Một ưu "
      "điểm khác của cơ cấu lò xo-màng là đặc tính ma sát đồng đều hơn theo thời gian. Ma sát của "
      "cơ cấu piston có thể tăng đáng kể theo sử dụng khi bề mặt dẫn hướng và vòng O-ring bị "
      "mòn, chất bôi trơn hỏng và elastomer xuống cấp. Do đó, để đảm bảo hiệu năng tốt liên tục, "
      "cơ cấu chấp hành piston cần bảo trì thường xuyên hơn cơ cấu lò xo-màng. Nếu không bảo "
      "trì, biến thiên quá trình có thể xấu đi đáng kể mà người vận hành không hay biết.",
      "Actuator style also has a profound impact on control valve assembly friction. Generally, "
      "spring-and-diaphragm actuators contribute less friction to the control valve assembly than "
      "piston actuators. An additional advantage of spring-and-diaphragm actuators is that their "
      "frictional characteristics are more uniform with age. Piston actuator friction probably "
      "will increase significantly with use as guide surfaces and as the O-rings wear, lubrication "
      "fails, and the elastomer degrades. Thus, to ensure continued good performance, maintenance "
      "is required more often for piston actuators than for spring-and-diaphragm actuators. If "
      "that maintenance is not performed, process variability can suffer dramatically without "
      "the operator's knowledge.")
    P("Độ hở (backlash) gây gián đoạn chuyển động khi thiết bị đổi chiều. Độ hở thường xảy ra ở "
      "bộ truyền bánh răng các cấu hình khác nhau. Cơ cấu chấp hành bánh răng - thanh răng "
      "(rack-and-pinion) đặc biệt dễ có vùng chết do độ hở. Một số kết nối trục van cũng có tác "
      "động vùng chết. Kết nối then spline nói chung có vùng chết nhỏ hơn nhiều so với trục then "
      "khóa hoặc thiết kế double-D.",
      "Backlash results in a discontinuity of motion when the device changes direction. Backlash "
      "commonly occurs in gear drives of various configurations. Rack-and-pinion actuators are "
      "particularly prone to deadband due to backlash. Some valve shaft connections also exhibit "
      "deadband effects. Spline connections generally have much less deadband than keyed shafts "
      "or double-D designs.")
    P("Dù ma sát có thể giảm đáng kể nhờ thiết kế van tốt, hiện tượng này rất khó loại bỏ hoàn "
      "toàn. Một van điều khiển được thiết kế tốt nên loại bỏ gần như hoàn toàn vùng chết do độ "
      "hở và xoắn trục. Để có hiệu năng tốt nhất trong giảm biến thiên quá trình, tổng vùng chết "
      "của toàn cụm van nên là 1% hoặc nhỏ hơn. Lý tưởng nhất là thấp tới 0,25%.",
      "While friction can be reduced significantly through good valve design, it is a difficult "
      "phenomenon to eliminate entirely. A well-engineered control valve should be able to "
      "virtually eliminate deadband due to backlash and shaft wind-up. For best performance in "
      "reducing process variability, the total deadband for the entire valve assembly should be "
      "1% or less. Ideally, it should be as low as 0.25%.")

    # ------------------------------------------------------------ 2.1.2
    H("2.1.2 Thiết kế cơ cấu chấp hành và bộ định vị",
      "2.1.2 Actuator and Positioner Design")
    P("Thiết kế cơ cấu chấp hành và bộ định vị phải được xem xét cùng nhau. Sự kết hợp của hai "
      "thiết bị này ảnh hưởng lớn đến hiệu năng tĩnh (vùng chết), cũng như đáp ứng động của cụm "
      "van điều khiển và tổng mức tiêu thụ khí của thiết bị đi kèm van.",
      "Actuator and positioner design must be considered together. The combination of these two "
      "pieces of equipment greatly affects the static performance (deadband), as well as the "
      "dynamic response of the control valve assembly and the overall air consumption of the "
      "valve instrumentation.")
    P("Bộ định vị được dùng với hầu hết các ứng dụng van điều khiển được chỉ định hiện nay. Bộ "
      "định vị cho phép đáp ứng chính xác của cụm van, cũng như chẩn đoán trực tuyến khi dùng "
      "với hệ thống điều khiển kỹ thuật số thông thường. Với sự nhấn mạnh ngày càng tăng vào "
      "hiệu năng kinh tế của điều khiển quá trình, nên cân nhắc dùng bộ định vị cho mọi ứng dụng "
      "van mà tối ưu hóa quá trình là quan trọng.",
      "Positioners are used with the majority of control valve applications specified today. "
      "Positioners allow for precise valve assembly response, as well as online diagnostics when "
      "used with a conventional digital control system. With the increasing emphasis upon "
      "economic performance of process control, positioners should be considered for every valve "
      "application where process optimization is important.")
    P("Có thể coi bộ định vị là thiết bị có khuếch đại tỷ lệ cao. Khi kết hợp với cơ cấu chấp "
      "hành và van, cụm van lý tưởng sẽ hoạt động như hệ bậc nhất hoặc bậc hai dưới tới hạn, tùy "
      "theo cách sử dụng và hiệu năng mong muốn. Bộ điều khiển van kỹ thuật số có thêm các thông "
      "số chỉnh như khuếch đại vi phân, chủ yếu để loại bỏ đặc tính không mong muốn và chỉnh cụm "
      "van theo hiệu năng mong muốn. Nhiều bộ định vị cũng có khả năng tích phân để loại bỏ sai "
      "lệch giữa điểm đặt và vị trí van. Trong hầu hết tình huống điều khiển quá trình, có thể "
      "tắt tính năng này để tránh khả năng hình thành dao động quá trình chậm, vì sai lệch giữa "
      "vị trí van và điểm đặt thường do bộ điều khiển quá trình xử lý.",
      "A positioner can be thought of as a high proportional gain device. When combined with an "
      "actuator and valve, the assembly will ideally behave like a first order or underdamped "
      "second order system, depending on use and intended performance. A digital valve controller "
      "has additional tuning parameters, such as derivative gain, which largely exist to remove "
      "undesirable characteristics and further tune the assembly to the desired performance. Many "
      "positioners also include an integral capability to remove any offsets between valve set "
      "point and position. Under most process control situations, this feature can be turned off "
      "to avoid the possibility of forming slow process oscillations, as the offset between valve "
      "position and set point is typically handled by the process controller.")
    P("Khi bộ định vị phát hiện thay đổi điểm đặt, nó phải có khả năng cấp thể tích khí lớn cho "
      "cơ cấu chấp hành, để cụm van chuyển động kịp thời và có kiểm soát. Khả năng này đến từ bộ "
      "định vị khuếch đại cao và là chức năng của bộ tăng áp khí nén tích hợp bên trong bộ định "
      "vị. Bộ tăng áp khí nén này thường gồm relay hoặc van trượt (spool valve).",
      "Once a change in the set point has been detected by the positioner, the positioner must be "
      "capable of supplying a large volume of air to the actuator, making the assembly move in a "
      "timely and controlled action. This ability comes from the high-gain positioner and is a "
      "function of integrated pneumatic booster within the positioner. This pneumatic booster is "
      "typically comprised of a relay or spool valve.")
    P("Các bộ định vị hai cấp hiệu năng cao điển hình dùng relay khí nén. Relay được ưa chuộng vì "
      "có thể cho khuếch đại cao, mang lại hiệu năng động xuất sắc với mức tiêu thụ khí ổn định "
      "thấp. Ngoài ra, chúng ít bị nhiễm bẩn bởi chất lỏng hơn. Thêm vào đó, một số cơ cấu chấp "
      "hành lớn hoặc có ma sát cao có thể dùng bộ tăng áp ngoài để đáp ứng thông số như tốc độ "
      "hành trình.",
      "Typical high-performance, two-stage positioners use pneumatic relays. Relays are preferred "
      "because they can provide high gain that gives excellent dynamic performance with low "
      "steady-state air consumption. In addition, they are less subject to fluid contamination. "
      "In addition, some large or high-friction actuators may use additional external boosters to "
      "meet specifications, such as stroking speed.")
    P("Thiết kế bộ định vị tiếp tục được cải tiến bằng giảm tiêu thụ khí và nâng cao khả năng "
      "chẩn đoán cho người dùng. Ngoài ra, các tính năng đã được bổ sung để hỗ trợ yêu cầu an "
      "toàn ngày càng cao của ngành, chẳng hạn hệ thống thiết bị an toàn (SIS) và van số được "
      "tối ưu.",
      "Positioner designs are continuing to improve by decreasing air consumption and advancing "
      "the diagnostic capabilities accessible to users. In addition, features have been added to "
      "support advancing industry safety requirements such as safety instrumented systems (SIS) "
      "and optimized digital valves.")

    # ------------------------------------------------------------ 2.1.3
    H("2.1.3 Thời gian đáp ứng của van", "2.1.3 Valve Response Time")
    P("Để điều khiển tối ưu nhiều quá trình, điều quan trọng là van phải tới vị trí cụ thể nhanh "
      "chóng. Đáp ứng nhanh với thay đổi tín hiệu nhỏ (1% hoặc nhỏ hơn) là một trong những yếu tố "
      "quan trọng nhất để cung cấp điều khiển quá trình tối ưu. Trong điều khiển tự động, điều "
      "chỉnh, phần lớn thay đổi tín hiệu nhận được từ bộ điều khiển là thay đổi vị trí nhỏ. Nếu "
      "cụm van điều khiển có thể đáp ứng nhanh các thay đổi nhỏ này, biến thiên quá trình sẽ được "
      "cải thiện.",
      "For optimum control of many processes, it is important that the valve reach a specific "
      "position quickly. A quick response to small signal changes (1% or less) is one of the most "
      "important factors in providing optimum process control. In automatic, regulatory control, "
      "the bulk of the signal changes received from the controller are for small changes in "
      "position. If a control valve assembly can quickly respond to these small changes, process "
      "variability will be improved.")
    P("Thời gian đáp ứng của van được đo bằng thông số gọi là T63. T63 là thời gian tính từ lúc "
      "bắt đầu thay đổi tín hiệu đầu vào đến lúc đầu ra đạt 63% của thay đổi tương ứng. Nó gồm "
      "cả thời gian chết của cụm van, là thời gian tĩnh, và thời gian động của cụm van. Thời gian "
      "động đo thời gian cơ cấu chấp hành mất để tới mốc 63% sau khi bắt đầu chuyển động.",
      "Valve response time is measured by a parameter called T63. T63 is the time measured from "
      "initiation of the input signal change to when the output reaches 63% of the corresponding "
      "change. It includes both the valve assembly dead time, which is a static time, and the "
      "dynamic time of the valve assembly. The dynamic time is a measure of how long the actuator "
      "takes to get to the 63% point once it starts moving.")

    H("2.1.3.1 Thời gian chết", "2.1.3.1 Dead Time", h3)
    P("Vùng chết, dù phát sinh từ ma sát trong thân van và cơ cấu chấp hành hay từ bộ định vị, "
      "có thể ảnh hưởng đáng kể đến thời gian chết của cụm van. Điều quan trọng là giữ thời gian "
      "chết càng nhỏ càng tốt, vì nó có thể là yếu tố hạn chế độ ổn định của quá trình. Nhìn "
      "chung, thời gian chết không nên vượt quá một phần ba tổng thời gian đáp ứng của van. Tuy "
      "nhiên, mối quan hệ tương đối giữa thời gian chết và hằng số thời gian của quá trình là "
      "then chốt. Nếu cụm van nằm trong vòng nhanh, nơi hằng số thời gian quá trình tiệm thời "
      "gian chết, thời gian chết có thể ảnh hưởng mạnh đến hiệu năng vòng. Trên các vòng nhanh "
      "này, điều cực kỳ quan trọng là chọn thiết bị điều khiển có thời gian chết nhỏ nhất có "
      "thể.",
      "Deadband, whether it comes from friction in the valve body and actuator or from the "
      "positioner, can significantly affect the dead time of the valve assembly. It is important "
      "to keep the dead time as small as possible, as this can be a limiting factor for process "
      "stability. Generally, dead time should be no more than one-third of the overall valve "
      "response time. However, the relative relationship between the dead time and the process "
      "time constant is critical. If the valve assembly is in a fast loop where the process time "
      "constant approaches the dead time, the dead time can dramatically affect loop performance. "
      "On these fast loops, it is critical to select control equipment with dead time as small as "
      "possible.")
    P("Ngoài ra, dưới góc độ chỉnh vòng, thời gian chết nên tương đối nhất quán ở cả hai chiều "
      "hành trình của van. Một số thiết kế cụm van có thể có thời gian chết dài gấp ba đến năm "
      "lần ở một chiều so với chiều kia. Hành vi này thường do đặc tính bất đối xứng của thiết "
      "kế bộ định vị gây ra, và có thể hạn chế nghiêm trọng khả năng chỉnh vòng để đạt hiệu năng "
      "tổng thể tốt nhất.",
      "Also, from a loop tuning point of view, it is important that the dead time be relatively "
      "consistent in both stroking directions of the valve. Some valve assembly designs can have "
      "dead times that are three to five times longer in one stroking direction than the other. "
      "This type of behavior is typically induced by the asymmetric behavior of the positioner "
      "design, and it can severely limit the ability to tune the loop for best overall "
      "performance.")

    H("2.1.3.2 Thời gian động", "2.1.3.2 Dynamic Time", h3)
    P("Sau khi thời gian chết trôi qua và van bắt đầu đáp ứng, phần còn lại của thời gian đáp "
      "ứng đến từ thời gian động của cụm van. Thời gian động này chủ yếu được xác định bởi đặc "
      "tính động của sự kết hợp bộ định vị và cơ cấu chấp hành. Hai bộ phận này phải được phối "
      "hợp cẩn thận để giảm thiểu tổng thời gian đáp ứng của van. Ví dụ, trong cụm van khí nén, "
      "bộ định vị phải có độ khuếch đại đủ để giảm thiểu thời gian động. Độ khuếch đại này chủ "
      "yếu đến từ tầng khuếch đại công suất trong bộ định vị. Nói cách khác, relay hoặc van trượt "
      "của bộ định vị có thể cấp thể tích khí lớn cho cơ cấu chấp hành nhanh đến đâu, thời gian "
      "đáp ứng của van sẽ nhanh đến đó. Tuy nhiên, bộ khuếch đại công suất khuếch đại cao này ít "
      "tác động đến thời gian chết trừ khi có vùng chết được thiết kế có chủ đích trong nó để "
      "giảm tiêu thụ khí tĩnh. Đương nhiên, thiết kế cơ cấu chấp hành ảnh hưởng đáng kể đến thời "
      "gian động. Ví dụ, thể tích buồng khí cơ cấu chấp hành cần lấp đầy càng lớn thì thời gian "
      "đáp ứng của van càng chậm.",
      "Once the dead time has passed and the valve begins to respond, the remainder of the valve "
      "response time comes from the dynamic time of the valve assembly. This dynamic time will be "
      "determined primarily by the dynamic characteristics of the positioner and actuator "
      "combination. These two components must be carefully matched to minimize the total valve "
      "response time. In a pneumatic valve assembly, for example, the positioner must have a gain "
      "to minimize the dynamic time of the valve assembly. This gain comes mainly from the power "
      "amplifier stage in the positioner. In other words, the faster the positioner relay or spool "
      "valve can supply a large volume of air to the actuator, the faster the valve response time "
      "will be. However, this high-gain power amplifier will have little effect on the dead time "
      "unless it has some intentional deadband designed into it to reduce static air consumption. "
      "Of course, the design of the actuator significantly affects the dynamic time. For example, "
      "the greater the volume of the actuator air chamber to be filled, the slower the valve "
      "response time.")

    H("2.1.3.3 Giải pháp", "2.1.3.3 Solutions", h3)
    P("Lúc đầu, có vẻ giải pháp là giảm thiểu thể tích cơ cấu chấp hành và tối đa hóa khuếch đại "
      "công suất động của bộ định vị, nhưng thực tế không đơn giản như vậy. Đây có thể là sự kết "
      "hợp nguy hiểm về mặt ổn định. Vì sự kết hợp bộ định vị và cơ cấu chấp hành tự là một vòng "
      "phản hồi, có thể làm độ khuếch đại của vòng này quá cao đối với thiết kế cơ cấu chấp hành "
      "đang dùng, khiến cụm van rơi vào dao động không ổn định. Ngoài ra, giảm thể tích cơ cấu "
      "chấp hành ảnh hưởng bất lợi đến tỷ số lực đẩy trên ma sát, làm tăng vùng chết của cụm van "
      "và dẫn đến tăng thời gian chết.",
      "At first, it might appear that the solution would be to minimize the actuator volume and "
      "maximize the positioner dynamic power gain, but it is really not that easy. This can be a "
      "dangerous combination of factors from a stability point of view. Recognizing that the "
      "positioner/actuator combination is its own feedback loop, it is possible to make the "
      "positioner/actuator loop gain too high for the actuator design being used, causing the "
      "valve assembly to go into an unstable oscillation. In addition, reducing the actuator "
      "volume has an adverse affect on the thrust-to-friction ratio, which increases the valve "
      "assembly deadband, resulting in increased dead time.")
    FIG(4, F.fig_f24())
    b.append(response_time_table(lang))
    P("Nếu tỷ số lực đẩy trên ma sát tổng thể không đủ cho một ứng dụng cụ thể, một lựa chọn là "
      "tăng khả năng lực đẩy của cơ cấu chấp hành bằng dùng cơ cấu chấp hành cỡ lớn hơn hoặc tăng "
      "áp suất cấp cho cơ cấu chấp hành. Tỷ số lực đẩy trên ma sát cao hơn này làm giảm vùng chết, "
      "giúp giảm thời gian chết của cụm van. Tuy nhiên, cả hai phương án đều có nghĩa là cần cấp "
      "thể tích khí lớn hơn cho cơ cấu chấp hành. Sự đánh đổi là có thể gây tác động xấu đến thời "
      "gian đáp ứng của van thông qua tăng thời gian động.",
      "If the overall thrust-to-friction ratio is not adequate for a given application, one "
      "option is to increase the thrust capability of the actuator by using the next size "
      "actuator or by increasing the pressure to the actuator. This higher-to-friction ratio "
      "reduces deadband, which should help to reduce the dead time of the assembly. However, both "
      "of these alternatives mean that a greater volume of air needs to be supplied to the "
      "actuator. The trade off is a possible detrimental effect on the valve response time "
      "through increased dynamic time.")
    P("Một cách giảm thể tích buồng khí cơ cấu chấp hành là dùng cơ cấu chấp hành piston thay vì "
      "lò xo-màng, nhưng đây không phải là thuốc chữa bách bệnh. Cơ cấu piston thường có khả năng "
      "lực đẩy cao hơn cơ cấu lò xo-màng, nhưng cũng có ma sát cao hơn, có thể gây vấn đề về thời "
      "gian đáp ứng. Để đạt lực đẩy cần thiết với cơ cấu piston, thường cần dùng áp suất khí cao "
      "hơn so với cơ cấu màng vì piston có diện tích nhỏ hơn. Điều này có nghĩa cần cấp thể tích "
      "khí lớn hơn, kéo theo tác động xấu đến thời gian động. Ngoài ra, cơ cấu piston với nhiều "
      "bề mặt dẫn hướng hơn có xu hướng ma sát cao hơn do khó căn chỉnh vốn có, cộng với ma sát từ "
      "vòng O-ring. Các vấn đề ma sát này cũng có xu hướng tăng theo thời gian. Dù vòng O-ring "
      "ban đầu tốt đến đâu, vật liệu elastomer này sẽ xuống cấp theo thời gian do mòn và các "
      "điều kiện môi trường. Tương tự, mòn bề mặt dẫn hướng tăng ma sát và chất bôi trơn sẽ cạn "
      "kiệt. Những vấn đề ma sát này dẫn đến vùng chết lớn hơn ở cơ cấu piston, làm tăng thời "
      "gian đáp ứng của van thông qua tăng thời gian chết.",
      "One way to reduce the actuator air chamber volume is to use a piston actuator rather than "
      "a spring-and-diaphragm actuator, but this is not a panacea. Piston actuators usually have "
      "higher thrust capability than spring-and-diaphragm actuators, but they also have higher "
      "friction, which can contribute to problems with valve response time. To obtain the "
      "required thrust with a piston actuator, it is usually necessary to use a higher air "
      "pressure than with a diaphragm actuator, because the piston typically has a smaller area. "
      "This means that a larger volume of air needs to be supplied with its attendant ill effects "
      "on the dynamic time. In addition, piston actuators, with their greater number of guide "
      "surfaces, tend to have higher friction due to inherent difficulties in alignment, as well "
      "as friction from the O-ring. These friction problems also tend to increase over time. "
      "Regardless of how good the O-rings are initially, these elastomeric materials will degrade "
      "with time due to wear and other environmental conditions. Likewise, wear on the guide "
      "surfaces will increase the friction, and depletion of the lubrication will occur. These "
      "friction problems result in a greater piston actuator deadband, which will increase the "
      "valve response time through increased dead time.")

    H("2.1.3.4 Áp suất cấp", "2.1.3.4 Supply Pressure", h3)
    P("Áp suất cấp khí thiết bị cũng có thể có tác động đáng kể đến hiệu năng động của cụm van. "
      "Ví dụ, nó có thể ảnh hưởng mạnh đến độ khuếch đại của bộ định vị, cũng như tổng mức tiêu "
      "thụ khí.",
      "Instrument supply pressure can also have a significant impact on dynamic performance of "
      "the valve assembly. For example, it can dramatically affect the positioner gain, as well "
      "as overall air consumption.")
    P("Bộ định vị khuếch đại cố định nói chung được tối ưu cho một áp suất cấp cụ thể. Tuy nhiên, "
      "độ khuếch đại này có thể thay đổi gấp hai lần hoặc hơn trong một dải áp suất cấp nhỏ. Ví "
      "dụ, bộ định vị được tối ưu cho áp suất cấp 20 psig có thể thấy độ khuếch đại giảm một nửa "
      "khi áp suất cấp tăng lên 35 psig.",
      "Fixed-gain positioners have generally been optimized for a particular supply pressure. "
      "This gain, however, can vary by a factor of two or more over a small range of supply "
      "pressures. For example, a positioner that has been optimized for a supply pressure of 20 "
      "psig might find its gain cut in half when the supply pressure is boosted to 35 psig.")
    P("Áp suất cấp cũng ảnh hưởng đến thể tích khí cung cấp cho cơ cấu chấp hành, quyết định tốc "
      "độ. Nó cũng liên quan trực tiếp đến tiêu thụ khí. Một lần nữa, bộ định vị van trượt khuếch "
      "đại cao có thể tiêu thụ tới năm lần lượng khí cần thiết so với bộ định vị hai cấp hiệu "
      "năng cao dùng relay ở tầng khuếch đại công suất.",
      "Supply pressure also affects the volume of air delivered to the actuator, which determines "
      "speed. It is also directly linked to air consumption. Again, high-gain spool valve "
      "positioners can consume up to five times the amount of air required for more efficient "
      "high-performance, two-stage positioners that use relays for the power amplification stage.")

    H("2.1.3.5 Giảm thiểu thời gian chết", "2.1.3.5 Minimizing Dead Time", h3)
    P("Để giảm thiểu thời gian chết của cụm van, cần giảm thiểu vùng chết của cụm van, dù phát "
      "sinh từ ma sát trong thiết kế gioăng van, ma sát đệm, xoắn trục, cơ cấu chấp hành hay "
      "thiết kế bộ định vị. Như đã nêu, ma sát là nguyên nhân chính gây vùng chết trong van điều "
      "khiển. Với các kiểu van quay, xoắn trục cũng có thể đóng góp đáng kể vào vùng chết. Kiểu "
      "cơ cấu chấp hành cũng có tác động sâu sắc đến ma sát của cụm van điều khiển. Nhìn chung, "
      "trong thời gian dài, cơ cấu chấp hành lò xo-màng đóng góp ít ma sát hơn cơ cấu piston. Như "
      "đã đề cập, điều này do ma sát tăng từ vòng O-ring piston, các vấn đề lệch trục và bôi trơn "
      "bị hỏng.",
      "To minimize the valve assembly dead time, minimize the deadband of the valve assembly, "
      "whether it comes from friction in the valve seal design, packing friction, shaft wind-up, "
      "actuator, or positioner design. As indicated, friction is a major cause of deadband in "
      "control valves. On rotary valve styles, shaft wind-up can also contribute significantly "
      "to deadband. Actuator style also has a profound impact on control valve assembly friction. "
      "Generally, spring-and-diaphragm actuators contribute less friction to the control valve "
      "assembly than piston actuators over an extended time. As mentioned, this is caused by the "
      "increasing friction from the piston O-ring, misalignment problems, and failed lubrication.")
    P("Thiết kế bộ định vị với độ khuếch đại cao có thể tạo khác biệt đáng kể trong giảm vùng "
      "chết. Điều này cũng cải thiện đáng kể độ phân giải của cụm van. Các cụm van có vùng chết và "
      "độ phân giải 1% hoặc nhỏ hơn không còn đủ cho nhiều nhu cầu giảm biến thiên quá trình. Nhiều "
      "quá trình yêu cầu cụm van có vùng chết và độ phân giải thấp tới 0,25%, đặc biệt khi cụm van "
      "lắp trong vòng quá trình nhanh.",
      "Having a positioner design with high gain can make a significant difference in reducing "
      "deadband. This can also make a significant improvement in the valve assembly resolution. "
      "Valve assemblies with deadband and resolution of 1% or less are no longer adequate for "
      "many process variability reduction needs. Many processes require the valve assembly to "
      "have deadband and resolution as low as 0.25%, especially where the valve assembly is "
      "installed in a fast process loop.")

    H("2.1.3.6 Thời gian đáp ứng của van", "2.1.3.6 Valve Response Time", h3)
    P("Một trong những điều bất ngờ từ nhiều nghiên cứu ngành về thời gian đáp ứng của van là sự "
      "thay đổi trong cách nghĩ về cơ cấu chấp hành lò xo-màng so với cơ cấu piston. Từ lâu, ngành "
      "quá trình có quan niệm sai rằng cơ cấu chấp hành piston nhanh hơn cơ cấu lò xo-màng. Nghiên "
      "cứu đã chứng minh điều này không đúng với thay đổi tín hiệu nhỏ.",
      "One of the surprising things to come out of many industry studies on valve response time "
      "has been the change in thinking about spring-and-diaphragm actuators versus piston "
      "actuators. It has long been a misconception in the process industry that piston actuators "
      "are faster than spring-and-diaphragm actuators. Research has shown this to be untrue for "
      "small signal changes.")
    P("Quan niệm sai này phát sinh từ nhiều năm kinh nghiệm thử van theo thời gian hành trình. "
      "Phép thử thời gian hành trình thường được thực hiện bằng cách cho cụm van chịu thay đổi "
      "bước 100% trong tín hiệu đầu vào và đo thời gian cụm van hoàn thành toàn bộ hành trình theo "
      "một chiều.",
      "This mistaken belief arose from many years of experience with testing valves for stroking "
      "time. A stroking time test is normally conducted by subjecting the valve assembly to a "
      "100% step change in the input signal and measuring the time it takes the valve assembly to "
      "complete its full stroke in either direction.")
    P("Dù van dùng cơ cấu piston thường có thời gian hành trình nhanh hơn hầu hết van dùng lò "
      "xo-màng, phép thử này không phản ánh hiệu năng van trong tình huống điều khiển quá trình "
      "điển hình, vì trong ứng dụng điều khiển quá trình thông thường, van hiếm khi phải chạy hết "
      "dải hành trình. Thường van chỉ cần đáp ứng trong dải thay đổi vị trí từ 0,25% đến 2%. Thử "
      "nghiệm van sâu rộng cho thấy cụm van lò xo-màng liên tục vượt trội van dùng cơ cấu piston ở "
      "thay đổi tín hiệu nhỏ, đại diện hơn cho ứng dụng điều khiển quá trình điều chỉnh. Ma sát "
      "cao hơn trong cơ cấu piston là một yếu tố khiến chúng kém nhạy với tín hiệu nhỏ hơn cơ cấu "
      "lò xo-màng.",
      "Although piston-actuated valves usually do have faster stroking times than most "
      "spring-and-diaphragm actuated valves, this test does not indicate valve performance in a "
      "typical process control situation, where in normal process control applications, the valve "
      "is rarely required to stroke through its full operating range. Typically, the valve is "
      "only required to respond within a range of 0.25% to 2% change in valve position. Extensive "
      "testing of valves has shown that spring-and-diaphragm valve assemblies consistently "
      "outperform piston actuated valves on small signal changes, which are more representative "
      "of regulatory process control applications. Higher friction in the piston actuator is one "
      "factor that plays a role in making them less responsive to small signals than "
      "spring-and-diaphragm actuators.")
    P("Chọn đúng sự kết hợp van, cơ cấu chấp hành và bộ định vị không dễ. Đó không đơn giản là "
      "tìm sự kết hợp tương thích về mặt vật lý. Cần áp dụng phán đoán kỹ thuật tốt vào thực hành "
      "tính cỡ và lựa chọn cụm van để đạt hiệu năng động tốt nhất cho vòng. Hình 2.4 cho thấy sự "
      "khác biệt rõ rệt về thời gian chết và tổng thời gian đáp ứng T63 do khác biệt trong thiết "
      "kế cụm van.",
      "Selecting the proper valve, actuator, and positioner combination is not easy. It is not "
      "simply a matter of finding a combination that is physically compatible. Good engineering "
      "judgment must go into the practice of valve assembly sizing and selection to achieve the "
      "best dynamic performance from the loop. Figure 2.4 shows the dramatic differences in dead "
      "time and overall T63 response time caused by differences in valve assembly design.")

    # ------------------------------------------------------------ 2.1.4
    H("2.1.4 Kiểu van và đặc tính hóa", "2.1.4 Valve Type and Characterization")
    P("Kiểu van được dùng và kích cỡ van có thể có tác động lớn đến hiệu năng của cụm van điều "
      "khiển trong hệ thống. Dù van phải đủ lớn để cho dòng yêu cầu đi qua trong mọi tình huống "
      "có thể xảy ra, một van quá lớn cho ứng dụng lại gây hại cho tối ưu hóa quá trình.",
      "The style of valve used and the sizing of the valve can have a large impact on the "
      "performance of the control valve assembly in the system. While a valve must be of "
      "sufficient size to pass the required flow under all possible contingencies, a valve that "
      "is too large for the application is a detriment to process optimization.")
    P("Khả năng dòng của van cũng liên quan đến kiểu van thông qua đặc tính vốn có của van. Đặc "
      "tính vốn có là quan hệ giữa khả năng dòng của van và hành trình van khi chênh áp qua van "
      "được giữ không đổi. Thường các đặc tính này được vẽ trên đường cong có trục hoành là phần "
      "trăm hành trình dù trục tung là phần trăm dòng (hoặc Cv). Vì dòng van là hàm của cả hành "
      "trình và chênh áp qua van, theo truyền thống người ta tiến hành thử đặc tính vốn có ở chênh "
      "áp không đổi. Đây không phải là tình huống bình thường trong thực tế, nhưng nó cung cấp "
      "cách có hệ thống để so sánh thiết kế đặc tính của van này với van khác.",
      "Flow capacity of the valve is also related to the style of valve through the inherent "
      "characteristic of the valve. The inherent characteristic is the relationship between the "
      "valve flow capacity and the valve travel when the differential pressure drop across the "
      "valve is held constant. Typically, these characteristics are plotted on a curve where the "
      "horizontal axis is labeled in percent travel although the vertical axis is labeled as "
      "percent flow (or Cv). Since valve flow is a function of both the valve travel and the "
      "pressure drop across the valve, it is traditional to conduct inherent valve characteristic "
      "tests at a constant pressure drop. This is not a normal situation in practice, but it "
      "provides a systematic way of comparing one valve characteristic design to another.")
    P("Trong điều kiện cụ thể là chênh áp không đổi, dòng van chỉ còn là hàm của hành trình van và "
      "thiết kế vốn có của trim van. Các đặc tính này được gọi là đặc tính dòng vốn có của van. "
      "Các đặc tính điển hình thử theo cách này có tên là tuyến tính, phần trăm bằng nhau và mở "
      "nhanh.",
      "Under the specific conditions of constant pressure drop, the valve flow becomes only a "
      "function of the valve travel and the inherent design of the valve trim. These "
      "characteristics are called the inherent flow characteristic of the valve. Typical valve "
      "characteristics conducted in this manner are named linear, equal-percentage, and "
      "quick-opening.")
    P("Tỷ số giữa sự thay đổi gia số của dòng van (đầu ra) và gia số tương ứng của hành trình van "
      "(đầu vào) gây ra thay đổi dòng đó được định nghĩa là khuếch đại van. Khuếch đại van vốn có "
      "bằng (Thay đổi dòng)/(Thay đổi hành trình), tức là độ dốc của đường cong đặc tính vốn có.",
      "The ratio of the incremental change in valve flow (output) to the corresponding increment "
      "of valve travel (input) which caused the flow change is defined as the valve gain. "
      "Inherent valve gain equals (Change in Flow)/(Change in Travel), the slope of the inherent "
      "characteristic curve.")
    P("Đặc tính tuyến tính có khuếch đại van vốn có không đổi trong toàn dải, đặc tính mở nhanh có "
      "khuếch đại lớn nhất ở đầu dưới của dải hành trình. Với van phần trăm bằng nhau, khuếch đại "
      "vốn có lớn nhất ở độ mở lớn nhất.",
      "The linear characteristic has a constant inherent valve gain throughout its range, and "
      "the quick-opening characteristic has an inherent valve gain that is the greatest at the "
      "lower end of the travel range. The greatest inherent valve gain for the equal-percentage "
      "valve is at the largest valve opening.")
    P("Đặc tính vốn có là hàm vốn có của hình học đường dòng van và không thay đổi chừng nào "
      "chênh áp được giữ không đổi. Nhiều thiết kế van, đặc biệt van bi quay, van bướm và van nút "
      "lệch tâm, có đặc tính vốn có không dễ thay đổi. Tuy nhiên, hầu hết van cầu có thể chọn lồng "
      "hoặc nút van có thể thay thế để sửa đặc tính dòng vốn có.",
      "Inherent valve characteristic is an inherent function of the valve flow passage geometry "
      "and does not change as long as the pressure drop is held constant. Many valve designs, "
      "particularly rotary ball valves, butterfly valves, and eccentric plug valves, have "
      "inherent characteristics, which cannot be easily changed. However, most globe valves have "
      "a selection of valve cages or plugs that can be interchanged to modify the inherent flow "
      "characteristic.")
    P("Hiểu đặc tính vốn có của van thì hữu ích, nhưng đặc tính quan trọng hơn cho mục đích tối "
      "ưu hóa quá trình là đặc tính dòng lắp đặt của toàn quá trình, gồm van và mọi thiết bị khác "
      "trong vòng. Đặc tính dòng lắp đặt được định nghĩa là quan hệ giữa dòng qua van và đầu vào "
      "cụm van khi van được lắp trong một hệ thống cụ thể và chênh áp qua van được phép thay đổi "
      "tự nhiên thay vì giữ không đổi. Hình 2.5 minh họa đặc tính dòng lắp đặt như vậy ở đường "
      "cong phía trên. Dòng trong hình này liên quan đến hành trình van quen thuộc hơn là đầu vào "
      "cụm van.",
      "Knowledge of the inherent valve characteristic is useful, but the more important "
      "characteristic for purposes of process optimization is the installed flow characteristic "
      "of the entire process, including the valve and all other equipment in the loop. The "
      "installed flow characteristic is defined as the relationship between the flow through the "
      "valve and the valve assembly input when the valve is installed in a specific system, and "
      "the pressure drop across the valve is allowed to change naturally, rather than being held "
      "constant. An illustration of such an installed flow characteristic is shown in the upper "
      "curve of Figure 2.5. The flow in this figure is related to the more familiar valve travel "
      "rather than valve assembly input.")
    FIG(5, F.fig_f25())

    H("2.1.4.1 Khuếch đại lắp đặt", "2.1.4.1 Installed Gain", h3)
    P("Khuếch đại lắp đặt, thể hiện ở đường cong dưới của Hình 2.5, là đồ thị độ dốc của đường "
      "cong trên tại từng điểm. Đường cong đặc tính dòng lắp đặt có thể thu được trong điều kiện "
      "phòng thí nghiệm bằng cách đưa toàn bộ vòng vào vận hành ở một điểm đặt danh định và không "
      "có nhiễu tải. Vòng được đưa về chế độ tay, sau đó dòng được đo và ghi lại khi đầu vào cụm "
      "van được điều khiển tay qua toàn dải hành trình. Đồ thị kết quả là đường cong đặc tính dòng "
      "lắp đặt ở phần trên Hình 2.5. Độ dốc của đường dòng này sau đó được tính tại từng điểm và "
      "vẽ thành khuếch đại lắp đặt như phần dưới Hình 2.5.",
      "Installed gain, shown in the lower curve of Figure 2.5, is a plot of the slope of the upper "
      "curve at each point. Installed flow characteristic curves can be obtained under laboratory "
      "conditions by placing the entire loop in operation at some nominal set point and with no "
      "load disturbances. The loop is placed in manual operation, and the flow is then measured "
      "and recorded as the input to the control valve assembly is manually driven through its "
      "full travel range. A plot of the results is the installed flow characteristic curve shown "
      "in the upper part of Figure 2.5. The slope of this flow curve is then evaluated at each "
      "point on the curve and plotted as the installed gain as shown in the lower part of Figure "
      "2.5.")
    P("Có thể thực hiện đo tại hiện trường khuếch đại quá trình lắp đặt tại một điểm vận hành "
      "bằng thử bước vòng hở (Hình 2.3). Khuếch đại quá trình lắp đặt tại bất kỳ điều kiện vận "
      "hành nào đơn giản là tỷ số giữa phần trăm thay đổi của đầu ra (dòng) và phần trăm thay đổi "
      "của tín hiệu đầu vào cụm van.",
      "Field measurements of the installed process gain can also be made at a single operating "
      "point using open-loop step tests (Figure 2.3). The installed process gain at any operating "
      "condition is simply the ratio of the percent change in output (flow) to the percent change "
      "in valve assembly input signal.")
    P("Lý do đặc trưng hóa khuếch đại van vốn có thông qua các thiết kế trim khác nhau là để bù "
      "cho các thay đổi khuếch đại khác trong vòng điều khiển. Mục tiêu cuối là duy trì khuếch đại "
      "vòng hợp lý đồng đều trên toàn dải vận hành, để duy trì đặc tính dòng lắp đặt tương đối "
      "tuyến tính cho quá trình. Vì cách đo của nó, đặc tính dòng lắp đặt và khuếch đại lắp đặt "
      "biểu diễn trong Hình 2.5 thực chất là đặc tính dòng và khuếch đại lắp đặt của toàn quá "
      "trình.",
      "The reason for characterizing inherent valve gain through various valve trim designs is "
      "to provide compensation for other gain changes in the control loop. The end goal is to "
      "maintain a loop gain, which is reasonably uniform over the entire operating range, to "
      "maintain a relatively linear installed flow characteristic for the process. Because of the "
      "way it is measured, the installed flow characteristic and installed gain represented in "
      "Figure 2.5 are really the installed gain and flow characteristic for the entire process.")
    P("Thông thường, khuếch đại của thiết bị được điều khiển thay đổi theo dòng. Ví dụ, khuếch đại "
      "của bình áp lực có xu hướng giảm theo lưu lượng. Trong trường hợp này, kỹ sư điều khiển quá "
      "trình có thể muốn dùng van phần trăm bằng nhau có khuếch đại tăng theo dòng. Lý tưởng nhất "
      "là hai quan hệ ngược này cân bằng nhau để cho đặc tính dòng lắp đặt tuyến tính hơn cho toàn "
      "quá trình.",
      "Typically, the gain of the unit being controlled changes with flow. For example, the gain "
      "of a pressure vessel tends to decrease with throughput. In this case, the process control "
      "engineer would then likely want to use an equal-percentage valve that has an increasing "
      "gain with flow. Ideally, these two inverse relationships should balance out to provide a "
      "more linear installed flow characteristic for the entire process.")

    H("2.1.4.2 Khuếch đại vòng", "2.1.4.2 Loop Gain", h3)
    P("Về lý thuyết, một vòng được chỉnh để hiệu năng tối ưu tại một điều kiện dòng ở điểm đặt. "
      "Khi dòng thay đổi quanh điểm đặt đó, mong muốn giữ khuếch đại vòng càng không đổi càng tốt "
      "để duy trì hiệu năng tối ưu. Nếu thay đổi khuếch đại vòng do đặc tính vốn có của van không "
      "bù chính xác cho thay đổi khuếch đại của thiết bị được điều khiển, sẽ có sự thay đổi "
      "khuếch đại vòng do thay đổi khuếch đại quá trình lắp đặt. Kết quả là tối ưu hóa quá trình "
      "trở nên khó hơn. Cũng có nguy cơ khuếch đại vòng thay đổi đủ lớn gây mất ổn định, chu trình "
      "giới hạn hoặc khó khăn động khác.",
      "Theoretically, a loop is tuned for optimum performance at some set point flow condition. "
      "As the flow varies about that set point, it is desirable to keep the loop gain as constant "
      "as possible to maintain optimum performance. If the loop gain change, due to the inherent "
      "valve characteristic, does not exactly compensate for the changing gain of the unit being "
      "controlled, then there will be a variation in the loop gain due to variation in the "
      "installed process gain. As a result, process optimization becomes more difficult. There is "
      "also a danger that the loop gain might change enough to cause instability, limit cycling, "
      "or other dynamic difficulties.")
    P("Khuếch đại vòng không nên thay đổi quá 4:1; nếu không, hiệu năng động của vòng suy giảm "
      "không chấp nhận được. Không có gì ma thuật về tỷ số cụ thể này; nó chỉ là tỷ số mà nhiều "
      "người thực hành điều khiển đồng ý là tạo ra dải biên khuếch đại chấp nhận được trong hầu "
      "hết vòng điều khiển quá trình.",
      "Loop gain should not vary more than 4:1; otherwise, the dynamic performance of the loop "
      "suffers unacceptably. There is nothing magic about this specific ratio; it is simply one "
      "which many control practitioners agree produces an acceptable range of gain margins in "
      "most process control loops.")
    P("Nguyên tắc này là cơ sở cho thông số kỹ thuật giới hạn khuếch đại EnTech sau (từ Control "
      "Valve Dynamic Specification, Phiên bản 3.0, tháng 11 năm 1998, EnTech Control Inc., "
      "Toronto, Ontario, Canada): Khuếch đại quá trình vòng = 1,0 (% dải của bộ phát)/(% đầu ra "
      "bộ điều khiển); Dải danh định: 0,5 - 2,0 (Lưu ý tỷ số 4:1).",
      "This guideline forms the basis for the following EnTech gain limit specification (from "
      "Control Valve Dynamic Specification, Version 3.0, November 1998, EnTech Control Inc., "
      "Toronto, Ontario, Canada): Loop Process Gain = 1.0 (% of Transmitter Span)/(% Controller "
      "Output); Nominal Range: 0.5-2.0 (Note 4-to-1 Ratio).")
    P("Định nghĩa này về quá trình vòng bao gồm mọi thiết bị trong cấu hình vòng, trừ bộ điều "
      "khiển. Nói cách khác, tích của khuếch đại của các thiết bị như cụm van điều khiển, bộ trao "
      "đổi nhiệt, bình áp lực hoặc hệ thống khác được điều khiển, bơm, bộ phát... chính là khuếch "
      "đại quá trình. Vì van là một phần của quá trình vòng theo định nghĩa này, điều quan trọng "
      "là chọn kiểu và kích cỡ van tạo ra đặc tính dòng lắp đặt đủ tuyến tính để nằm trong giới "
      "hạn khuếch đại quy định trên dải vận hành của hệ thống. Nếu bản thân van có quá nhiều thay "
      "đổi khuếch đại, sẽ ít linh hoạt hơn trong chỉnh bộ điều khiển. Thực hành tốt là giữ càng "
      "nhiều khuếch đại vòng ở bộ điều khiển càng tốt.",
      "This definition of the loop process includes all the devices in the loop configuration "
      "except the controller. In other words, the product of the gains of such devices as the "
      "control valve assembly, the heat exchanger, pressure vessel, or other system being "
      "controlled, the pump, the transmitter, etc. is the process gain. Because the valve is part "
      "of the loop process as defined here, it is important to select a valve style and size that "
      "will produce an installed flow characteristic that is sufficiently linear to stay within "
      "the specified gain limits over the operating range of the system. If too much gain "
      "variation occurs in the control valve itself, it leaves less flexibility in adjusting the "
      "controller. It is good practice to keep as much of the loop gain in the controller as "
      "possible.")
    P("Dù tỷ số 4:1 về thay đổi khuếch đại trong vòng được chấp nhận rộng rãi, không phải ai cũng "
      "đồng ý với giới hạn 0,5 đến 2,0. Một số chuyên gia ngành lập luận dùng giới hạn khuếch đại "
      "quá trình vòng từ 0,2 đến 0,8, vẫn là 4:1. Nguy cơ tiềm ẩn khi dùng dải khuếch đại giảm này "
      "là đầu dưới của dải có thể gây dao động van lớn trong vận hành bình thường. Thực hành vận "
      "hành tốt là giữ dao động van dưới khoảng 5%. Tuy nhiên, cũng có nguy cơ nếu khuếch đại quá "
      "lớn. Vòng có thể dao động thậm chí mất ổn định nếu khuếch đại vòng quá cao tại một điểm nào "
      "đó của hành trình. Để đảm bảo hiệu năng động tốt và ổn định vòng trong dải điều kiện vận "
      "hành rộng, chuyên gia ngành khuyến nghị thiết kế thiết bị vòng sao cho khuếch đại quá trình "
      "nằm trong khoảng 0,5 đến 2,0.",
      "Although the 4:1 ratio of gain change in the loop is widely accepted, not everyone agrees "
      "with the 0.5 to 2.0 gain limits. Some industry experts have made a case for using loop "
      "process gain limits from 0.2 to 0.8, which is still 4:1. The potential danger inherent in "
      "using this reduced gain range is that the low end of the gain range could result in large "
      "valve swings during normal operation. It is good operating practice to keep valve swings "
      "below about 5%. However, there is also a danger in letting the gain get too large. The "
      "loop can become oscillatory or even unstable if the loop gain gets too high at some point "
      "in the travel. To ensure good dynamic performance and loop stability over a wide range of "
      "operating conditions, industry experts recommend that loop equipment be engineered so the "
      "process gain remains within the range of 0.5 to 2.0.")

    H("2.1.4.3 Tối ưu hóa quá trình", "2.1.4.3 Process Optimization", h3)
    P("Tối ưu hóa quá trình đòi hỏi chọn kiểu và kích cỡ van giữ khuếch đại quá trình trong dải "
      "giới hạn đã chọn trên tập điều kiện vận hành rộng nhất có thể. Vì giảm biến thiên quá trình "
      "phụ thuộc rất nhiều vào duy trì khuếch đại lắp đặt đồng đều, dải mà van có thể vận hành "
      "trong giới hạn khuếch đại chấp nhận được được gọi là dải điều khiển của van.",
      "Process optimization requires a valve style and size be chosen that will keep the process "
      "gain within the selected gain limit range over the widest possible set of operating "
      "conditions. Because minimizing process variability is so dependent on maintaining a "
      "uniform installed gain, the range over which a valve can operate within the acceptable "
      "gain specification limits is known as the control range of the valve.")
    FIG(6, F.fig_f26())
    P("Dải điều khiển của van thay đổi mạnh theo kiểu van. Hình 2.6 so sánh van bướm cỡ đường ống "
      "với van cầu cỡ đường ống. Van cầu có dải điều khiển rộng hơn nhiều van bướm. Các kiểu khác "
      "như van bi rãnh V và van nút lệch tâm thường nằm giữa hai dải này.",
      "The control range of a valve varies dramatically with valve style. Figure 2.6 shows a "
      "line-size butterfly valve compared to a line-size globe valve. The globe valve has a much "
      "wider control range than the butterfly valve. Other valve styles, such as V-notch ball "
      "valves and eccentric plug valves generally fall somewhere between these two ranges.")
    P("Vì van bướm thường có dải điều khiển hẹp nhất, chúng thường phù hợp nhất cho ứng dụng tải "
      "cố định. Ngoài ra, chúng phải được tính cỡ cẩn thận để hiệu năng tối ưu ở tải cố định.",
      "Because butterfly valves typically have the narrowest control range, they are generally "
      "best suited for fixed-load applications. In addition, they must be carefully sized for "
      "optimal performance at fixed loads.")
    P("Nếu đặc tính vốn có của van có thể chọn để bù chính xác cho thay đổi khuếch đại hệ thống "
      "theo dòng, người ta mong khuếch đại quá trình lắp đặt (đường dưới) về cơ bản là đường "
      "thẳng ở giá trị 1,0. Đáng tiếc là sự khớp khuếch đại chính xác như vậy hiếm khi khả thi do "
      "hạn chế thực tế trong cung cấp vô số đặc tính trim van vốn có. Ngoài ra, một số kiểu van "
      "như bướm và bi không có lựa chọn trim cho phép dễ dàng thay đổi đặc tính vốn có.",
      "If the inherent characteristic of a valve could be selected to exactly compensate for the "
      "system gain change with flow, one would expect the installed process gain (lower curve) to "
      "be essentially a straight line at a value of 1.0. Unfortunately, such a precise gain match "
      "is seldom possible due to the logistical limitations of providing an infinite variety of "
      "inherent valve trim characteristics. In addition, some valve styles, such as butterfly and "
      "ball valves, do not offer trim alternatives that allow easy change of the inherent valve "
      "characteristic.")
    P("Có thể giảm bớt tình trạng này bằng dùng tỷ lệ phi tuyến giữa điểm đặt van và vị trí. Kỹ "
      "thuật này hiệu chỉnh lại tín hiệu đầu vào van bằng cách lấy tín hiệu điều khiển tuyến tính "
      "và dùng bảng giá trị được lập trình sẵn để tạo đầu vào van cần thiết nhằm đạt đặc tính van "
      "mong muốn. Kỹ thuật này đôi khi được gọi là đặc tính hóa đường thuận hoặc đặc tính hóa "
      "điểm đặt.",
      "This condition can be alleviated by use of non-linear scaling between valve set point and "
      "position. This technique recalibrates the valve input signal by taking the linear "
      "controller signal and using a pre-programmed table of values to produce the valve input "
      "required to achieve the desired valve characteristic. This technique is sometimes referred "
      "to as forward path or set point characterization.")
    P("Sự đặc tính hóa này diễn ra bên ngoài vòng phản hồi của bộ định vị và tránh thay đổi khuếch "
      "đại vòng định vị. Phương pháp này cũng có giới hạn động. Ví dụ, có thể có những vùng trong "
      "dải van mà thay đổi tín hiệu quá trình 1,0% bị thu hẹp qua quá trình đặc tính hóa thành chỉ "
      "0,1% tín hiệu tới van (tức là ở vùng phẳng của đường đặc tính hóa). Nhiều van điều khiển "
      "không thể đáp ứng với thay đổi tín hiệu nhỏ đến vậy.",
      "This characterization occurs outside the positioner feedback loop, and avoids changing "
      "the positioner loop gain. This method also has its dynamic limitations. For example, there "
      "can be places in a valve range where a 1.0% process signal change might be narrowed through "
      "this characterization process to only a 0.1% signal change to the valve (that is, in the "
      "flat regions of the characterizing curve). Many control valves are unable to respond to "
      "signal changes this small.")
    P("Hiệu năng quá trình tốt nhất đạt được khi đặc tính dòng yêu cầu thu được bằng thay đổi trim "
      "van thay vì dùng đặc tính hóa phi tuyến. Chọn đúng van điều khiển được thiết kế để tạo đặc "
      "tính dòng lắp đặt tương đối tuyến tính trên dải vận hành của hệ thống là bước then chốt "
      "đảm bảo hiệu năng quá trình tối ưu.",
      "The best process performance occurs when the required flow characteristic is obtained "
      "through changes in the valve trim rather than through use of non-linear characterization. "
      "Proper selection of a control valve designed to produce a reasonably linear installed flow "
      "characteristic over the operating range of the system is a critical step in ensuring "
      "optimum process performance.")

    # ------------------------------------------------------------ 2.1.5
    H("2.1.5 Tính cỡ van", "2.1.5 Valve Sizing")
    P("Việc chọn van quá lớn đôi khi xảy ra khi cố tối ưu hiệu năng quá trình thông qua giảm biến "
      "thiên quá trình. Điều này phát sinh từ việc dùng van cỡ đường ống, đặc biệt với van quay "
      "công suất cao, cũng như việc cộng thêm một cách thận trọng nhiều hệ số an toàn ở các giai "
      "đoạn khác nhau trong thiết kế quá trình.",
      "Oversizing of valves sometimes occurs when trying to optimize process performance through "
      "a reduction of process variability. This results from using line-size valves, especially "
      "with high-capacity rotary valves, as well as the conservative addition of multiple safety "
      "factors at different stages in the process design.")
    P("Van quá lớn gây hại cho biến thiên quá trình theo hai cách. Thứ nhất, van quá lớn đặt quá "
      "nhiều khuếch đại vào van, để lại ít linh hoạt hơn trong chỉnh bộ điều khiển. Hiệu năng tốt "
      "nhất đạt được khi phần lớn khuếch đại vòng đến từ bộ điều khiển.",
      "Oversizing the valve hurts process variability in two ways. First, the oversized valve puts "
      "too much gain in the valve, leaving less flexibility in adjusting the controller. Best "
      "performance results when most loop gain comes from the controller.")
    P("Lưu ý ở đường cong khuếch đại Hình 2.5, khuếch đại quá trình khá cao ở vùng dưới khoảng 25% "
      "hành trình van. Nếu van quá lớn, làm khả năng vận hành trong hoặc gần vùng này cao hơn, "
      "khuếch đại cao này có thể nghĩa là cần giảm khuếch đại bộ điều khiển để tránh mất ổn định "
      "vòng. Điều đó tất nhiên có nghĩa là bị phạt bằng tăng biến thiên quá trình.",
      "Notice in the gain curve of Figure 2.5, the process gain gets quite high in the region "
      "below about 25% valve travel. If the valve is oversized, making it more likely to operate "
      "in or near this region, this high gain can likely mean that the controller gain will need "
      "to be reduced to avoid instability problems with the loop. This, of course, will mean a "
      "penalty of increased process variability.")
    P("Cách thứ hai van quá lớn gây hại cho biến thiên quá trình là van quá lớn có khả năng vận "
      "hành thường xuyên hơn ở độ mở thấp, nơi ma sát gioăng có thể lớn hơn, đặc biệt ở van quay. "
      "Vì van quá lớn tạo thay đổi dòng tỷ lệ lớn hơn cho một gia số hành trình nhất định, hiện "
      "tượng này có thể phóng đại mạnh biến thiên quá trình liên quan đến vùng chết do ma sát.",
      "The second way oversized valves hurt process variability is that an oversized valve is "
      "likely to operate more frequently at lower valve openings where seal friction can be "
      "greater, particularly in rotary valves. Because an oversized valve produces a "
      "disproportionately large flow change for a given increment of valve travel, this "
      "phenomenon can greatly exaggerate the process variability associated with deadband due to "
      "friction.")
    P("Bất kể đặc tính vốn có thực tế của nó, van quá lớn nghiêm trọng có xu hướng hoạt động giống "
      "van mở nhanh hơn, dẫn đến khuếch đại quá trình lắp đặt cao ở vùng nâng thấp (Hình 2.5). "
      "Ngoài ra, khi van quá lớn, van có xu hướng đạt công suất hệ thống ở hành trình tương đối "
      "thấp, làm đường cong dòng phẳng ra ở hành trình cao hơn (Hình 2.5). Với hành trình van "
      "trên khoảng 50 độ, van này trở nên hoàn toàn vô hiệu cho mục đích điều khiển vì khuếch đại "
      "quá trình tiệm về không và van phải trải qua thay đổi hành trình lớn với thay đổi dòng rất "
      "nhỏ. Hệ quả là gần như không thể đạt biến thiên quá trình chấp nhận được trong vùng này.",
      "Regardless of its actual inherent valve characteristic, a severely oversized valve tends "
      "to act more like a quick-opening valve, which results in high installed process gain in "
      "the lower lift regions (Figure 2.5). In addition, when the valve is oversized, the valve "
      "tends to reach system capacity at relatively low travel, making the flow curve flatten out "
      "at higher valve travels (Figure 2.5). For valve travels above about 50 degrees, this valve "
      "has become totally ineffective for control purposes because the process gain is approaching "
      "zero and the valve must undergo wide changes in travel with very little resulting changes "
      "in flow. Consequently, there is little hope of achieving acceptable process variability in "
      "this region.")
    P("Van trong Hình 2.5 được dùng hoàn toàn sai trong ứng dụng này vì dải điều khiển quá hẹp "
      "(khoảng 25 độ đến 45 độ). Tình huống này xảy ra do chọn van bướm cỡ đường ống, chủ yếu vì "
      "chi phí thấp, và không cân nhắc lợi nhuận bị mất do hy sinh biến thiên quá trình từ hiệu "
      "năng động kém của van điều khiển.",
      "The valve shown in Figure 2.5 is totally misapplied in this application because it has such "
      "a narrow control range (approximately 25 degrees to 45 degrees). This situation came about "
      "because a line-sized butterfly valve was chosen, primarily due to its low cost, and no "
      "consideration was given to the lost profit that results from sacrificing process "
      "variability through poor dynamic performance of the control valve.")
    P("Đáng tiếc là tình huống này thường lặp lại. Nghiên cứu điều khiển quá trình cho thấy, với "
      "một số ngành, phần lớn van hiện nay trong vòng điều khiển quá trình đều quá lớn cho ứng "
      "dụng. Dù có vẻ phản trực giác, thường thì hợp lý về kinh tế khi chọn van điều khiển cho "
      "điều kiện hiện tại rồi thay van khi điều kiện thay đổi.",
      "Unfortunately, this situation is often repeated. Process control studies show that, for "
      "some industries, the majority of valves currently in process control loops are oversized "
      "for the application. While it might seem counterintuitive, it often makes economic sense "
      "to select a control valve for present conditions and then replace the valve when conditions "
      "change.")
    P("Khi chọn van, điều quan trọng là cân nhắc kiểu van, đặc tính vốn có và kích cỡ van để mang "
      "lại dải điều khiển rộng nhất có thể cho ứng dụng. Xem Chương 5 để biết thêm thông tin về "
      "tính cỡ.",
      "When selecting a valve, it is important to consider the valve style, inherent "
      "characteristic, and valve size that will provide the broadest possible control range for "
      "the application. Refer to Chapter 5 for more sizing information.")

    # ------------------------------------------------------------ 2.2
    H("2.2 Kết quả kinh tế", "2.2 Economic Results")
    P("Cân nhắc các yếu tố đã thảo luận trong chương này có thể có tác động lớn đến kết quả kinh "
      "tế của một nhà máy đang vận hành. Ngày càng nhiều người dùng van điều khiển tập trung vào "
      "các thông số hiệu năng động như vùng chết, thời gian đáp ứng và khuếch đại lắp đặt (trong "
      "điều kiện tải quá trình thực tế) như cách cải thiện hiệu năng vòng quá trình. Dù có thể đo "
      "nhiều thông số hiệu năng động này trong điều kiện vòng hở, tác động của chúng trở nên rõ "
      "ràng khi đo hiệu năng vòng kín. Kết quả thử vòng kín trong Hình 2.7 cho thấy khả năng của "
      "ba van khác nhau trong giảm biến thiên quá trình ở các điều kiện chỉnh khác nhau.",
      "Consideration of the factors discussed in this chapter can have a dramatic impact on the "
      "economic results of an operating plant. More and more control valve users focus on dynamic "
      "performance parameters such as deadband, response times, and installed gain (under actual "
      "process load conditions) as a means to improve process loop performance. Although it is "
      "possible to measure many of these dynamic performance parameters in an open loop "
      "situation, the impact these parameters have becomes clear when closed-loop performance is "
      "measured. The closed-loop test results shown in Figure 2.7 demonstrate the ability of three "
      "different valves to reduce process variability over different tuning conditions.")
    FIG(7, F.fig_f27())
    P("Sơ đồ này vẽ biến thiên quá trình dưới dạng phần trăm của biến điểm đặt theo hằng số thời "
      "gian vòng kín, thước đo mức độ chỉnh vòng. Đường nằm ngang nhãn Manual cho thấy mức biến "
      "thiên vốn có trong vòng khi không có nỗ lực điều khiển nó (vòng hở). Đường dốc xuống bên "
      "trái nhãn Minimum Variability biểu diễn hiệu năng động tính toán của cụm van lý tưởng "
      "(không có phi tuyến). Mọi cụm van thực thường nằm ở đâu đó giữa hai điều kiện này.",
      "This diagram plots process variability as a percent of the set point variable versus the "
      "closed-loop time constant, which is a measure of loop tuning. The horizontal line labeled "
      "Manual shows how much variability is inherent in the loop when no attempt is made to "
      "control it (open loop). The line sloping downward to the left marked Minimum Variability "
      "represents the calculated dynamic performance of an ideal valve assembly (one with no "
      "non-linearities). All real valve assemblies should normally fall somewhere between these "
      "two conditions.")
    P("Không phải van nào cũng cho hiệu năng động như nhau dù tất cả về mặt lý thuyết đều đáp ứng "
      "thông số mua hàng về hiệu năng tĩnh và được coi là van tương đương (Hình 2.7). Van A trong "
      "Hình 2.7 bám tốt đường biến thiên tối thiểu trên dải rộng các chỉnh bộ điều khiển. Van này "
      "cho hiệu năng động xuất sắc với biến thiên tối thiểu. Ngược lại, thiết kế van B và C không "
      "tốt bằng và làm biến thiên tăng khi hệ thống được chỉnh mạnh hơn để giảm hằng số thời gian "
      "vòng kín.",
      "Not all valves provide the same dynamic performance even though they all theoretically "
      "meet static performance purchase specifications and are considered to be equivalent valves "
      "(Figure 2.7). Valve A in Figure 2.7 does a good job of following the trend of the minimum "
      "variability line over a wide range of controller tunings. This valve shows excellent "
      "dynamic performance with minimum variability. In contrast, Valves B and C designs don't "
      "fare as well and increase in variability as the system is tuned more aggressively for "
      "decreasing closed-loop time constants.")
    P("Cả ba thiết kế van đều có khả năng điều khiển quá trình và giảm biến thiên, nhưng hai thiết "
      "kế làm kém hơn. Hãy xem xét điều gì sẽ xảy ra nếu van B kém hơn được thay bằng van A tốt "
      "nhất, và hệ thống được chỉnh ở hằng số thời gian vòng kín 2,0 giây. Số liệu thử nghiệm cho "
      "thấy điều này mang lại cải thiện 1,4% về biến thiên quá trình.",
      "All three valve designs are capable of controlling the process and reducing the "
      "variability, but two designs don't do it as well. Consider what would happen if the poorer "
      "performing Valve B was replaced with the best performing Valve A, and the system was tuned "
      "to a 2.0 second closed-loop time constant. The test data shows this would result in a 1.4% "
      "improvement in process variability.")
    P("Điều này có vẻ không nhiều, nhưng kết quả theo thời gian có thể rất ấn tượng. Một van có "
      "thể mang lại mức cải thiện đó mỗi phút mỗi ngày có thể tiết kiệm đáng kể tiền bạc trong "
      "một năm. Hiệu năng của van tốt hơn trong ví dụ này là bằng chứng mạnh mẽ rằng cụm van "
      "điều khiển vượt trội có thể có tác động kinh tế sâu sắc.",
      "This might not seem like much, but the results over a time can be impressive. A valve that "
      "can provide this much improvement every minute of every day can save significant dollars "
      "over a single year. The performance of the better valve in this example provides strong "
      "evidence that a superior control valve assembly can have a profound economic impact.")
    P("Ví dụ này chỉ là một cách van điều khiển tăng lợi nhuận nhờ điều khiển chặt chẽ hơn. Giảm "
      "chi phí năng lượng, tăng năng suất, giảm chi phí xử lý lại sản phẩm ngoài quy cách... đều "
      "là cách van điều khiển tốt tăng kết quả kinh tế nhờ điều khiển chặt chẽ hơn. Dù chi phí ban "
      "đầu của van tốt nhất có thể cao hơn, vài đô la thêm chi cho van được thiết kế tốt có thể "
      "tăng mạnh lợi tức đầu tư. Thường chi phí ban đầu thêm của van có thể được bù đắp trong vài "
      "ngày.",
      "This example is only one way a control valve can increase profits through tighter control. "
      "Decreased energy costs, increased throughput, less reprocessing cost for out-of-"
      "specification product, and so on, are all ways a good control valve can increase economic "
      "results through tighter control. While the initial cost might be higher for the best "
      "control valve, the few extra dollars spent on a well-engineered control valve can "
      "dramatically increase the return on investment. Often the extra initial cost of the valve "
      "can be paid for in a matter of days.")
    P("Kết quả là ngành quá trình ngày càng nhận thức rằng cụm van điều khiển đóng vai trò quan "
      "trọng trong hiệu năng vòng/đơn vị/nhà máy. Họ cũng nhận ra rằng phương pháp chỉ định cụm van "
      "truyền thống không còn đủ để đảm bảo lợi ích của tối ưu hóa quá trình. Dù quan trọng, các "
      "chỉ số hiệu năng tĩnh như khả năng dòng, độ rò, tương thích vật liệu và số liệu hiệu năng "
      "băng không đủ để xử lý đặc tính động của vòng điều khiển quá trình.",
      "As a result, the process industries have become increasingly aware that control valve "
      "assemblies play an important role in loop/unit/plant performance. They have also realized "
      "that traditional methods of specifying a valve assembly are no longer adequate to ensure "
      "the benefits of process optimization. While important, such static performance indicators "
      "as flow capacity, leakage, materials compatibility, and bench performance data are not "
      "sufficiently adequate to deal with the dynamic characteristics of process control loops.")

    # ------------------------------------------------------------ 2.3
    H("2.3 Thử nghiệm hiệu năng Signature Series",
      "2.3 Signature Series Performance Testing")
    P("Thử nghiệm hiệu năng Signature Series của phần mềm ValveLink do nhà máy thực hiện có sẵn "
      "cho bất kỳ cụm van điều khiển Fisher nào có bộ điều khiển van kỹ thuật số FIELDVUE, và có "
      "thể dùng làm điểm khởi đầu trong chương trình bảo trì van điều khiển.",
      "ValveLink Software Signature Series factory-executed performance testing is available for "
      "any Fisher control valve assembly that includes a FIELDVUE digital valve controller and "
      "can be used as the starting point in a control valve maintenance program.")
    P("Thử nghiệm hiệu năng Signature Series tạo ra một chuẩn so sánh về hiệu năng của van lắp "
      "ráp trước khi xuất xưởng. Chuẩn này cung cấp điểm khởi đầu cho việc so sánh dữ liệu trong "
      "tương lai, cho phép người dùng theo dõi tình trạng vận hành của van điều khiển và tối đa "
      "hóa hiệu năng van.",
      "Signature Series performance testing creates a benchmark of an assembled valve's "
      "performance prior to shipment. This benchmark provides a starting point for future data "
      "comparison, enabling the user to track the operating condition of the control valve and "
      "maximize valve performance.")
    P("Khi được đặt hàng cùng van điều khiển có FIELDVUE, nhà máy dùng khả năng chẩn đoán của "
      "phần mềm ValveLink để thử kỹ từng cụm van như một phần của công đoạn lắp ráp cuối.",
      "When ordered with a FIELDVUE equipped control valve, the factory uses the diagnostic "
      "capability of ValveLink software to thoroughly test each valve assembly as part of its "
      "final assembly.")

    H("2.3.1 Signature Series 1", "2.3.1 Signature Series 1", h3)
    P("Trong cấp thử nghiệm Signature Series 1, người dùng nhận được:",
      "Within the Signature Series 1 test level, the user receives:")
    B(["Màn hình cấu hình thiết bị.",
       "Giám sát trạng thái (hành trình 50%).",
       "Bảng thông số kỹ thuật van.",
       "Đường chữ ký van, ghi từ -5% đến 105% đầu vào (thời gian quét cho phép thử này phụ thuộc "
       "kích cỡ cơ cấu chấp hành).",
       "Đường cong dải sai số động, ghi từ -5% đến 105% đầu vào (thời gian quét phụ thuộc kích "
       "cỡ cơ cấu chấp hành).",
       "Tín hiệu lái, ghi từ -5% đến 105% đầu vào (thời gian quét phụ thuộc kích cỡ cơ cấu chấp "
       "hành).",
       "Kết quả thử Signature Series dưới dạng điện tử từ văn phòng bán hàng Emerson."],
      ["Instrument Configuration Display.",
       "Status Monitor (50% travel).",
       "Valve Spec Sheet.",
       "Valve Signature, as recorded from -5 to 105% input (scan time for this test depends on "
       "actuator size).",
       "Dynamic Error Band Curve, as recorded from -5 to 105% input (scan time for this test "
       "depends on actuator size).",
       "Drive Signal, as recorded from -5 to 105% input (scan time for this test depends on "
       "actuator size).",
       "Signature Series test results electronically from the Emerson Sales office."])

    H("2.3.2 Signature Series 2", "2.3.2 Signature Series 2", h3)
    P("Ngoài thông tin Signature Series 1, người dùng nhận thêm:",
      "In addition to Signature Series 1 information, the user receives:")
    B(["Thử bước hiệu năng.",
       "Giám sát trạng thái (0, 25, 50, 75, 100%).",
       "Kết quả thử Signature Series dưới dạng điện tử từ văn phòng bán hàng Emerson."],
      ["Performance Step Test.",
       "Status Monitor (0, 25, 50, 75, 100%).",
       "Signature Series test results electronically from the Emerson Sales office."])

    H("2.3.3 Signature Series 3", "2.3.3 Signature Series 3", h3)
    P("Thử nghiệm Signature Series 3 cung cấp các phép thử Series 1 và 2 do người dùng chỉ định "
      "và cho phép mọi thay đổi về điểm cuối hoặc thời gian quét. Khả năng này cho phép người dùng "
      "điều chỉnh thử nghiệm theo yêu cầu hoặc nhu cầu quá trình cụ thể.",
      "Signature Series 3 testing provides user specified Series 1 and 2 tests and allows any "
      "change in end points or scan times. This capability allows the user to adjust the testing "
      "to specific requirements or process needs.")
    FIG(8, F.fig_f28())
    P("So sánh dữ liệu: Nếu van điều khiển được trang bị thiết bị FIELDVUE có khả năng chẩn đoán, "
      "sau khi van đã đưa vào vận hành, có thể dùng phần mềm ValveLink để chạy lại các phép thử "
      "như đã chạy tại nhà máy. Sau đó, bằng nhập dữ liệu Signature Series vào ValveLink, người "
      "dùng có thể so sánh hiệu năng lúc xuất xưởng với tình trạng vận hành hiện tại của van. Có "
      "thể đối chiếu dữ liệu hiện tại với dữ liệu chuẩn để nhanh chóng xác định vấn đề, như Hình "
      "2.9.",
      "Data Comparison: If a control valve is equipped with a FIELDVUE instrument that includes "
      "diagnostic capability, after the valve has been in-service, ValveLink Software can be used "
      "to run the same tests that were run at the factory. Then, by importing the Signature "
      "Series data into ValveLink Software, the user can compare the as-shipped performance with "
      "the valve's current operating condition. The current data can be compared to the baseline "
      "data to quickly pinpoint issues, as shown in Figure 2.9.")
    FIG(9, F.fig_f29())
    P("Tính sẵn có của Signature Series: Thử nghiệm Signature Series có sẵn cho mọi van điều "
      "khiển Fisher. Để đặt thử Signature Series, ghi rõ yêu cầu thử trên đơn đặt hàng van Fisher.",
      "Signature Series Availability: Signature Series testing is available for all Fisher "
      "control valves. To order Signature Series testing, specify Signature Series testing "
      "requirements on the Fisher control valve order.")
    P("Tận dụng Signature Series: Thực hiện thử chẩn đoán bằng phần mềm ValveLink cung cấp phân "
      "tích các thông số vận hành van điều khiển, như Hình 2.10. Người dùng có thể tận dụng "
      "Signature Series bằng liên hệ văn phòng bán hàng Emerson. Ghi rõ yêu cầu thử Signature "
      "Series khi đặt hàng. Emerson có thể cung cấp dữ liệu chẩn đoán cần thiết để giữ van vận "
      "hành ở hiệu năng cao nhất.",
      "Take Advantage of the Signature Series: Performing a Diagnostic Test with ValveLink "
      "Software provides an analysis of control valve operating parameters, as shown in Figure "
      "2.10. Users can take advantage of the Signature Series by contacting an Emerson Sales "
      "office. Specify the Signature Series testing requirements when placing an order. Emerson "
      "can provide the diagnostic data needed to keep valves operating at top performance.")
    FIG(10, F.fig_f2_10())

    # ------------------------------------------------------------ 2.4
    H("2.4 Tóm tắt", "2.4 Summary")
    P("Cụm van điều khiển đóng vai trò cực kỳ quan trọng trong việc tạo ra hiệu năng tốt nhất có "
      "thể từ vòng điều khiển. Tối ưu hóa quá trình nghĩa là tối ưu hóa toàn bộ quá trình, không "
      "chỉ các thuật toán điều khiển dùng trong thiết bị phòng điều khiển. Van được gọi là phần "
      "tử điều khiển cuối cùng vì chính tại cụm van điều khiển mà điều khiển quá trình được thực "
      "hiện.",
      "The control valve assembly plays an extremely important role in producing the best "
      "possible performance from the control loop. Process optimization means optimizing the "
      "entire process, not just the control algorithms used in the control room equipment. The "
      "valve is called the final control element because the control valve assembly is where "
      "process control is implemented.")
    P("Không có ý nghĩa gì khi lắp đặt chiến lược điều khiển quá trình và hệ thống thiết bị phần "
      "cứng tinh vi có khả năng đạt điều khiển quá trình 0,5% hoặc tốt hơn, rồi lại thực hiện "
      "chiến lược đó bằng van điều khiển 5% hoặc tệ hơn. Các cuộc kiểm toán trên hàng nghìn vòng "
      "điều khiển quá trình đã chứng minh rõ ràng rằng phần tử điều khiển cuối cùng đóng vai trò "
      "đáng kể trong đạt được tối ưu hóa quá trình thực sự. Khả năng sinh lời tăng lên khi van "
      "điều khiển được thiết kế đúng cho ứng dụng của nó.",
      "It makes no sense to install an elaborate process control strategy and hardware "
      "instrumentation system capable of achieving 0.5% or better process control and then to "
      "implement that control strategy with a 5% or worse control valve. Audits performed on "
      "thousands of process control loops have provided strong proof that the final control "
      "element plays a significant role in achieving true process optimization. Profitability "
      "increases when a control valve has been properly engineered for its application.")
    P("Van điều khiển là sản phẩm tinh vi, công nghệ cao và không nên coi như hàng hóa thông "
      "thường. Dù thông số kỹ thuật van truyền thống đóng vai trò quan trọng, thông số kỹ thuật van "
      "cũng phải đề cập đến đặc tính hiệu năng động thực nếu muốn đạt tối ưu hóa quá trình thực "
      "sự. Các thông số này nhất thiết phải gồm vùng chết, thời gian chết, thời gian đáp ứng, v.v.",
      "Control valves are sophisticated, high-tech products and should not be treated as a "
      "commodity. Although traditional valve specifications play an important role, valve "
      "specifications must also address real dynamic performance characteristics if true process "
      "optimization is to be achieved. It is imperative that these specifications include such "
      "parameters as deadband, dead time, response time, etc.")
    P("Cuối cùng, tối ưu hóa quá trình bắt đầu và kết thúc bằng tối ưu hóa toàn bộ vòng. Không "
      "thể xử lý riêng lẻ các bộ phận của vòng để đạt hiệu năng phối hợp. Tương tự, không thể đánh "
      "giá hiệu năng của bất kỳ bộ phận nào của vòng một cách cô lập. Các phép thử cô lập trong "
      "điều kiện băng, không có tải, sẽ không cho thông tin hiệu năng như khi thử phần cứng trong "
      "điều kiện quá trình thực tế.",
      "Finally, process optimization begins and ends with optimization of the entire loop. Parts "
      "of the loop cannot be treated individually to achieve coordinated loop performance. "
      "Likewise, performance of any part of the loop cannot be evaluated in isolation. Isolated "
      "tests under non-loaded, bench-type conditions will not provide performance information "
      "that is obtained from testing the hardware under actual process conditions.")

    # ------------------------------------------------------------ source quirks
    H("Ghi chú về nguồn", "Source notes", h3)
    N("Nguyên bản có một số điểm đáng lưu ý: nhãn Hình 2.9 viết là <i>Data Comparision</i> (lỗi "
      "chính tả) — bản tiếng Anh giữ nguyên, bản tiếng Việt dùng \"so sánh dữ liệu\"; Hình 2.6 và "
      "2.8 cùng mang nhãn <i>Effect of Valve Style on Control Range</i> dù nằm ở các mục khác "
      "nhau; bảng Hình 2.4 dùng ký hiệu NR = No Response; danh sách năm yếu tố thiết kế và các "
      "mục trong Signature Series được đánh dấu bằng ô vuông đặc trong nguyên bản và được trình "
      "bày thành danh sách gạch đầu dòng ở bản dịch. Các đường cong trong Hình 2.1, 2.3 đến 2.10 "
      "được vẽ lại dạng vector minh họa, còn số liệu bảng Hình 2.4 giữ nguyên giá trị của nguồn.",
      "The source has several quirks: the caption of Figure 2.9 reads <i>Data Comparision</i> (a "
      "misspelling), which is preserved in the English text while the Vietnamese uses "
      "\"so sanh du lieu\" (data comparison); Figures 2.6 and 2.8 share the caption <i>Effect of "
      "Valve Style on Control Range</i> although they appear in different sections; the Figure "
      "2.4 table uses NR = No Response; and the five design considerations and the Signature "
      "Series lists are marked with a solid-square glyph in the source and are presented as "
      "bullet lists here. Curves in Figures 2.1 and 2.3 through 2.10 are redrawn as illustrative "
      "vectors, while the Figure 2.4 table keeps the source values.")

    P("Chương 2 chiếm tr. 34–53 của bản in (20 trang) trong Emerson, Control Valve Handbook, ấn "
      "bản 6 (2020). Nội dung gồm bốn mục: biến thiên quá trình và các yếu tố thiết kế van, kết "
      "quả kinh tế, thử nghiệm Signature Series và tóm tắt. Mười hình đánh số 2.1–2.10 được vẽ "
      "lại dạng vector trong cvh6fig.py và đặt đúng vị trí xuất hiện của chú thích gốc.",
      "Chapter 2 occupies printed pp. 34-53 (20 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains four sections: process variability and valve design factors, "
      "economic results, Signature Series performance testing, and a summary. The ten numbered "
      "figures, 2.1-2.10, are redrawn as vectors in cvh6fig.py and placed where the source "
      "captions occur.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 "
      "Emerson Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 "
      "Emerson Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
