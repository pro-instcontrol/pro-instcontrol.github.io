# -*- coding: utf-8 -*-
"""Book 7c, Chapter 8 - Installation and Maintenance (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 176-191.
This is a reference chapter: storage and protection before installation,
installation techniques (manual, pipeline cleanliness, inspection, piping
practices, criss-cross bolt tightening, flushing/hydro/start-up trim),
predictive maintenance and non-intrusive diagnostics, service and repair
parts with OEM parts and spare-parts kits, actuator maintenance (spring and
diaphragm, piston, packing, seat rings, bench set, travel), and the STO
planning process. Eleven numbered figures are redrawn as vector schematics
in `cvh6fig8.py` and placed in numbered order at their logical prose points.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul
import cvh6fig8 as F

PAGES_SRC = 16          # source printed pp. 176-191 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Installation and Maintenance"
TITLE_VI = "Lắp đặt và bảo trì"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> final control element — phần tử điều khiển cuối · "
            "predictive maintenance — bảo trì dự báo · reactive maintenance — bảo trì phản ứng · "
            "preventive maintenance — bảo trì phòng ngừa · non-intrusive diagnostics — chẩn đoán "
            "không xâm lấn · digital valve controller — bộ điều khiển van số · in-service — khi "
            "đang vận hành · deadband — vùng chết · travel deviation — độ lệch hành trình · "
            "instrument air — khí nén thiết bị · air mass flow — lưu lượng khối khí · droop — "
            "sụt áp · crossover pressure — áp suất chuyển tiếp · "
            "OEM — nhà sản xuất thiết bị gốc · RSPL — danh sách phụ tùng dự phòng đề xuất · "
            "parts kit — bộ phụ tùng · packing — đệm kín thân van · seat ring — vòng đế · "
            "lapping — mài ép bề mặt đế · bench set — giá trị nén lò xo ban đầu · seating force — "
            "lực ép đế · spring-and-diaphragm actuator — cơ cấu chấp hành lò xo - màng · "
            "piston actuator — cơ cấu chấp hành piston · single-acting — tác động đơn · "
            "double-acting — tác động kép · molded diaphragm — màng ép khuôn · "
            "flushing trim — trim xả rửa · sacrificial trim — trim hy sinh tạm thời · "
            "hydrostatic test — thử áp lực thủy · blow down trim — trim xả thổi · "
            "STO — dừng máy, đại tu hoặc mất máy · scope creep — phạm vi công việc dần mở rộng · "
            "punch list — danh sách công việc tồn đọng · CMMS — phần mềm quản lý bảo trì · "
            "ValveLink — phần mềm chẩn đoán van · FlowScanner — công cụ quét chẩn đoán · "
            "turnaround — dừng máy định kỳ · key performance indicator (KPI) — chỉ số hiệu suất "
            "chính")
    return (
        "<b>Key terms in this chapter.</b> final control element · predictive maintenance · "
        "reactive maintenance · preventive maintenance · non-intrusive diagnostics · digital "
        "valve controller · in-service diagnostics · deadband · travel deviation · instrument "
        "air · air mass flow · droop · crossover pressure · OEM (original equipment "
        "manufacturer) · RSPL (Recommended Spare Parts List) · parts kit · packing · seat ring "
        "· lapping · bench set · seating force · spring-and-diaphragm actuator · piston "
        "actuator · single-acting · double-acting · molded diaphragm · flushing trim · "
        "sacrificial trim · hydrostatic test · blow down trim · STO (shutdown, turnaround, "
        "outage) · scope creep · punch list · CMMS · ValveLink · FlowScanner · turnaround · "
        "key performance indicator (KPI)")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Trong bản dump văn bản, chú thích Hình 8.7 xuất hiện "
            "trước Hình 8.6 trên cùng trang in 184, và chú thích Hình 8.9 xuất hiện trước Hình "
            "8.8 trên trang in 185. Ở đây các hình được sắp theo thứ tự số, 8.6 trước 8.7 và 8.8 "
            "trước 8.9, tại các vị trí văn bản hợp lý. (2) Chú thích Hình 8.4 nằm giữa đoạn của "
            "mục 8.3.5 trên trang in 182 dù hình minh họa cơ cấu lò xo - màng được bàn trong mục "
            "8.5.1; hình được giữ tại vị trí nguồn để duy trì thứ tự số, còn chú thích Hình 8.5 "
            "đứng cuối mục 8.4.2. (3) Chú thích Hình 8.1 trong bản dump viết đầy đủ là «Arrow "
            "Depicting the Flow Direction on a Metal-Seated Ball Valve»; ở đây giữ nguyên cách "
            "viết đó. (4) Các nhãn của Hình 8.11 bị OCR xáo trộn («EXECUTION» đứng trước «2 1 6», "
            "«PRE-STO PLANNING5WORK SCOPE DEFINITION» bị dính nhau); ở đây được trình bày lại theo "
            "thứ tự bảy bước từ 1 đến 7. (5) Một số lỗi chính tả và ngữ pháp được giữ nguyên ở bản "
            "Anh và hiệu đính trong bản Việt: «Reducded maintenance costs», «referred to a "
            "single-acting actuators», «substaintially reduce», «customer liasion», «I.E., TV144», "
            "cách dùng «flowed» và «oversee» (theo nghĩa giám sát). Ký hiệu «» là ký tự bullet "
            "của PDF bị OCR thành ký tự «» — ở đây được thay bằng danh sách gạch đầu dòng bình thường. "
            "(6) Nguồn không có bảng dữ liệu hay phương trình trình bày dưới dạng toán học; quan hệ "
            "lực ép đế trong mục 8.5.5 và Hình 8.10 chỉ được viết bằng lời («áp suất áp dụng trừ "
            "bench set trừ độ nén lò xo do hành trình»), nên ở đây không tạo phương trình hay bảng "
            "mới. (7) Hình trong bản in là ảnh chụp hoặc bản vẽ; ở đây vẽ lại dạng sơ đồ vector "
            "minh họa, không phải hình gốc.")
    return (
        "<b>Source notes.</b> (1) In the text dump the caption for Figure 8.7 precedes that of "
        "Figure 8.6 on printed p. 184, and the caption for Figure 8.9 precedes that of Figure 8.8 "
        "on printed p. 185. The figures are ordered numerically here, 8.6 before 8.7 and 8.8 "
        "before 8.9, at their logical prose points. (2) The caption for Figure 8.4 floats in the "
        "middle of section 8.3.5 on printed p. 182 although the figure illustrates the "
        "spring-and-diaphragm actuator discussed in 8.5.1; it is kept at its source position to "
        "preserve numeric order, while the caption for Figure 8.5 closes section 8.4.2. "
        "(3) The dump caption for Figure 8.1 reads in full <i>Arrow Depicting the Flow Direction "
        "on a Metal-Seated Ball Valve</i>; that fuller wording is retained here. (4) The labels "
        "of Figure 8.11 are jumbled by the OCR (<i>EXECUTION</i> appears before <i>2 1 6</i>, and "
        "<i>PRE-STO PLANNING5WORK SCOPE DEFINITION</i> run together); they are presented here in "
        "the seven-step order 1 through 7. (5) Several spelling and grammar quirks are retained "
        "in English and corrected in Vietnamese: <i>Reducded maintenance costs</i>, <i>referred to "
        "a single-acting actuators</i>, <i>substaintially reduce</i>, <i>customer liasion</i>, "
        "<i>I.E., TV144</i>, and the uses of <i>flowed</i> and <i>oversee</i> (in the sense of "
        "monitor). The PDF bullet glyph misread as «» is rendered here as a normal bulleted "
        "list. (6) The source contains no data tables and no equation set in mathematical "
        "notation; the seating-force relationship in 8.5.5 and Figure 8.10 is given in words "
        "(<i>applied pressure minus bench set minus spring compression due to travel</i>), so no "
        "equation or table is invented here. (7) Figures are photographs or line drawings in "
        "print; they are redrawn here as illustrative vector schematics, not the original images.")


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
        "Chương này là tài liệu tham khảo về lắp đặt và bảo trì van điều khiển: lưu trữ và bảo vệ "
        "trước khi lắp, các kỹ thuật lắp đặt đúng (đọc sổ hướng dẫn, vệ sinh đường ống, kiểm tra "
        "van, bố trí đường ống, siết bulông chéo và dùng trim hy sinh cho thử áp lực và xả rửa), "
        "bảo trì dự báo với chẩn đoán không xâm lấn, phụ tùng và bộ kit dịch vụ, bảo trì cơ cấu "
        "chấp hành, và quy trình lập kế hoạch dừng máy STO bảy bước."
        if vi else
        "This chapter is a reference on installing and maintaining control valves: storage and "
        "protection before installation, proper installation techniques (reading the manual, "
        "cleaning the pipeline, inspecting the valve, piping practices, criss-cross bolt "
        "tightening, and sacrificial trim for hydrotesting and flushing), predictive maintenance "
        "with non-intrusive diagnostics, service parts and kits, actuator maintenance, and the "
        "seven-step STO planning process."))
    N(note_terms("vi"), note_terms("en"))

    # ------------------------------------------------------------ introduction
    P("Hiệu quả của van điều khiển ảnh hưởng trực tiếp đến lợi nhuận của nhà máy quá trình. Vai trò "
      "của van điều khiển trong việc tối ưu hóa quá trình thường bị bỏ qua. Nhiều quản đốc nhà máy "
      "tập trung phần lớn nguồn lực vào hệ thống điều khiển phân tán và tiềm năng cải thiện hiệu "
      "suất sản xuất của nó. Tuy nhiên, chính phần tử điều khiển cuối cùng — thường là van điều "
      "khiển — mới thực sự tạo ra sự thay đổi của biến số quá trình. Nếu van không hoạt động đúng, "
      "dù có điện tử tinh vi đến đâu ở phía trước cũng không khắc phục được sự cố tại van. Như "
      "nhiều nghiên cứu đã chỉ ra, van điều khiển thường bị lãng quên đến mức trở thành mắt xích "
      "yếu trong sơ đồ điều khiển quá trình.",
      "Control valve efficiency directly affects process plant profitability. The role a control "
      "valve plays in optimizing processes is often overlooked. Many process plant managers focus "
      "most resources on distributed control systems and their potential for improving production "
      "efficiency. However, it is the final control element (typically a control valve) that "
      "actually creates the change in the process variable. If the valve is not working properly, "
      "no amount of sophisticated electronics at the front end will correct problems at the valve. "
      "As many studies have shown, control valves are often neglected to the point that they "
      "become the weak link in the process control scheme.")
    P("Van điều khiển phải vận hành đúng, bất kể hệ thống tự động hóa tinh vi đến đâu hay thiết bị "
      "đo chính xác đến đâu. Khi van vận hành đúng, bạn đạt được năng suất cao, sản phẩm chất "
      "lượng, lợi nhuận tối đa và tiết kiệm năng lượng.",
      "Control valves must operate properly, no matter how sophisticated the automation system or "
      "how accurate the instrumentation. With proper valve operation, you can achieve high yields, "
      "quality products, maximum profits, and energy conservation.")
    P("Tối ưu hóa hiệu quả của van điều khiển phụ thuộc vào:",
      "Optimizing control valve efficiency depends on:")
    B(["Lựa chọn đúng van điều khiển cho ứng dụng",
       "Lưu trữ và bảo vệ đúng cách",
       "Kỹ thuật lắp đặt đúng",
       "Một chương trình bảo trì dự báo hiệu quả"],
      ["Correct control valve selection for the application",
       "Proper storage and protection",
       "Proper installation techniques",
       "An effective predictive maintenance program"])
    P("Lựa chọn van điều khiển được trình bày ở Chương 5. Lưu trữ và bảo vệ đúng cách, kỹ thuật "
      "lắp đặt và bảo trì dự báo được trình bày trong chương này.",
      "Control valve selection is covered in Chapter 5. Proper storage and protection, "
      "installation techniques, and predictive maintenance are included in this chapter.")

    # ------------------------------------------------------------ 8.1
    H("8.1 Lưu trữ và bảo vệ đúng cách", "8.1 Proper Storage and Protection")
    P("Cần cân nhắc việc lưu trữ và bảo vệ đúng cách ngay từ giai đoạn lựa chọn, trước khi van "
      "được vận chuyển. Thông thường, nhà sản xuất có tiêu chuẩn đóng gói phụ thuộc vào nơi đến "
      "và thời gian lưu trữ dự kiến trước khi lắp đặt. Vì hầu hết van đến công trường trước khi "
      "lắp đặt một thời gian, nhiều sự cố có thể được tránh bằng cách nắm rõ tiến độ lắp đặt và "
      "trao đổi với nhà sản xuất tại thời điểm chọn van. Ngoài ra, cần thực hiện biện pháp phòng "
      "ngừa đặc biệt khi nhận van tại điểm đến cuối cùng. Ví dụ, van phải được lưu trữ ở nơi sạch "
      "sẽ, khô ráo, tránh xa các luồng phương tiện hoặc hoạt động có thể làm hỏng van.",
      "Proper storage and protection should be considered early in the selection process, before "
      "the valve is shipped. Typically, manufacturers have packaging standards that are dependent "
      "upon the destination and intended length of storage before installation. Because most "
      "valves arrive on site some time before installation, many problems can be averted by making "
      "sure the details of the installation schedule are known and discussed with the manufacturer "
      "at the time of valve selection. In addition, special precautions should be taken upon "
      "receipt of the valve at the final destination. For example, the valve must be stored in a "
      "clean, dry place away from any traffic or other activity that could damage the valve.")

    # ------------------------------------------------------------ 8.2
    H("8.2 Kỹ thuật lắp đặt đúng", "8.2 Proper Installation Techniques")
    P("Luôn tuân theo hướng dẫn lắp đặt và các lưu ý của nhà sản xuất van điều khiển. Các hướng "
      "dẫn điển hình được tóm tắt sau đây.",
      "Always follow the control valve manufacturer's installation instructions and cautions. "
      "Typical instructions are summarized next.")

    H("8.2.1 Đọc sổ hướng dẫn", "8.2.1 Read the Instruction Manual", h3)
    P("Trước khi lắp van, hãy đọc sổ hướng dẫn. Sổ hướng dẫn mô tả sản phẩm và xem xét các vấn đề "
      "an toàn cùng các biện pháp phòng ngừa cần thực hiện trước và trong khi lắp đặt. Tuân theo "
      "hướng dẫn trong sổ giúp quá trình lắp đặt dễ dàng và thành công.",
      "Before installing the valve, read the instruction manual. Instruction manuals describe the "
      "product and review safety issues and precautions to be taken before and during "
      "installation. Following the guidelines in the manual helps ensure an easy and successful "
      "installation.")

    H("8.2.2 Đảm bảo đường ống sạch", "8.2.2 Be Sure the Pipeline Is Clean", h3)
    P("Vật lạ trong đường ống có thể làm hỏng bề mặt ép đế của van hoặc thậm chí cản trở chuyển "
      "động của nút, bi hoặc đĩa van khiến van không đóng kín. Để giảm khả năng xảy ra tình huống "
      "nguy hiểm, hãy vệ sinh tất cả đường ống trước khi lắp đặt. Đảm bảo loại bỏ vảy ống, mạt kim "
      "loại, xỉ hàn và các vật lạ khác. Ngoài ra, kiểm tra mặt bích đường ống để đảm bảo bề mặt "
      "gioăng nhẵn.",
      "Foreign material in the pipeline could damage the seating surface of the valve or even "
      "obstruct the movement of the valve plug, ball, or disk so that the valve does not shut off "
      "properly. To help reduce the possibility of a dangerous situation from occurring, clean all "
      "pipelines before installing. Make sure pipe scale, metal chips, welding slag, and other "
      "foreign materials are removed. In addition, inspect pipe flanges to ensure a smooth gasket "
      "surface.")
    P("Nếu van có đầu nối ren, hãy bôi hợp chất làm kín ren chất lượng tốt vào ren ngoài của đường "
      "ống. Không bôi chất làm kín vào ren trong, vì hợp chất dư ở ren trong có thể bị đẩy vào thân "
      "van. Lượng hợp chất dư có thể gây kẹt nút van hoặc tích tụ bụi bẩn, làm van không đóng kín "
      "tốt.",
      "If the valve has screwed end connections, apply a good grade of pipe sealant compound to "
      "the male pipeline threads. Do not use sealant on the female threads because excess compound "
      "on the female threads could be forced into the valve body. Excess compound could cause "
      "sticking in the valve plug or accumulation of dirt, which could prevent good valve "
      "shutoff.")

    H("8.2.3 Kiểm tra van điều khiển", "8.2.3 Inspect the Control Valve", h3)
    P("Dù nhà sản xuất có biện pháp ngăn hư hại trong vận chuyển, hư hại vẫn có thể xảy ra và cần "
      "được phát hiện, báo cáo trước khi lắp đặt. Không lắp van điều khiển mà đã biết bị hư hại "
      "trong vận chuyển hoặc lưu trữ. Trước khi lắp, kiểm tra và tháo bỏ mọi chặn vận chuyển, nút "
      "bịt bảo vệ hoặc nắp che bề mặt gioăng. Kiểm tra bên trong thân van để chắc chắn không có vật "
      "lạ.",
      "Although valve manufacturers take steps to prevent shipment damage, such damage is possible "
      "and should be discovered and reported before the valve is installed. Do not install a "
      "control valve known to have been damaged in shipment or while in storage. Before "
      "installing, check for and remove all shipping stops and protective plugs or gasket surface "
      "covers. Check inside the valve body to make sure no foreign objects are present.")

    H("8.2.4 Dùng phương pháp bố trí đường ống đúng", "8.2.4 Use Good Piping Practices", h3)
    P("Hầu hết van điều khiển có thể lắp ở bất kỳ vị trí nào. Tuy nhiên, cách phổ biến nhất là đặt "
      "cơ cấu chấp hành thẳng đứng và phía trên thân van. Nếu bắt buộc lắp cơ cấu chấp hành nằm "
      "ngang, hãy cân nhắc bổ sung giá đỡ thẳng đứng cho cơ cấu. Đảm bảo thân van được lắp sao cho "
      "chất lưu chảy theo chiều mũi tên chỉ dòng chảy (Hình 8.1) hoặc theo sổ hướng dẫn.",
      "Most control valves can be installed in any position. However, the most common method is "
      "with the actuator vertical and above the valve body. If horizontal actuator mounting is "
      "necessary, consider additional vertical support for the actuator. Be sure the body is "
      "installed so that fluid flow will be in the direction indicated by the flow arrow (Figure "
      "8.1) or instruction manual.")
    FIG(1, F.fig_f8_01())
    P("Hãy chừa khoảng trống hợp lý phía trên và phía dưới van để có thể tháo cơ cấu chấp hành hoặc "
      "nút van dễ dàng khi kiểm tra và bảo trì. Khoảng cách thông thường có thể xem trong bản vẽ "
      "kích thước được chứng nhận của nhà sản xuất. Với thân van nối bích, đảm bảo các bích được "
      "căn chỉnh đúng để bề mặt gioăng tiếp xúc đều. Siết nhẹ các bulông sau khi căn chỉnh bích "
      "xong, rồi siết tiếp theo kiểu chéo (Hình 8.2). Siết đúng cách giúp tránh ép gioăng không "
      "đều, ngăn rò rỉ và tránh khả năng làm hỏng thậm chí gãy bích. Lưu ý này đặc biệt quan "
      "trọng khi nối vào bích có vật liệu khác với bích của van.",
      "Be sure to allow ample space above and below the valve to permit easy removal of the "
      "actuator or valve plug for inspection and maintenance. Clearance distances are normally "
      "available from the valve manufacturer as certified dimension drawings. For flanged valve "
      "bodies, be sure the flanges are properly aligned to provide uniform contact of the gasket "
      "surfaces. Snug up the bolts gently after establishing proper flange alignment. Finish "
      "tightening them in a criss-cross pattern (Figure 8.2). Proper tightening will avoid uneven "
      "gasket loading and will help prevent leaks. It will also help avoid the possibility of "
      "damaging, or even breaking, the flange. This precaution is particularly important when "
      "connecting to flanges that are not the same material as the valve flanges.")
    FIG(2, F.fig_f8_02())
    P("Các điểm lấy áp đặt phía trên và phía dưới van điều khiển hữu ích để kiểm tra lưu lượng hoặc "
      "chênh áp. Đặt các điểm này ở đoạn ống thẳng, tránh xa cút, bộ giảm hoặc bộ mở rộng. Vị trí "
      "như vậy giảm thiểu sai số do nhiễu loạn chất lưu.",
      "Pressure taps installed upstream and downstream of the control valve are useful for "
      "checking flow capacity or pressure drop. Locate such taps in straight runs of pipe away "
      "from elbows, reducers, or expanders. This location minimizes inaccuracies resulting from "
      "fluid turbulence.")
    P("Dùng ống hoặc ống dẫn đường kính 1/4 inch hoặc 3/8 inch (6–10 milimet) từ đầu nối áp suất "
      "trên cơ cấu chấp hành đến thiết bị đo. Giữ đoạn này tương đối ngắn và hạn chế số mối nối "
      "và cút để giảm độ trễ thời gian của hệ thống. Nếu khoảng cách bắt buộc phải dài, hãy dùng "
      "bộ định vị van hoặc bộ tăng thể tích để giảm độ trễ.",
      "Use 1/4-inch or 3/8-inch (6-10 millimeters) tubing or pipe from the pressure connection on "
      "the actuator to the instrumentation. Keep this distance relatively short and minimize the "
      "number of fittings and elbows to reduce system time lag. If the distance must be long, use "
      "a valve positioner or a volume booster to reduce any lag time.")

    H("8.2.5 Trim xả rửa, thử áp lực và khởi động", "8.2.5 Flushing/Hydro/Start-Up Trim", h3)
    P("Khi hàn van đầu hàn ổ cắm hoặc đầu hàn đối đầu vào đường ống, cần tháo trim của van điều "
      "khiển để tránh hư hại các chi tiết trim. Trong quá trình thử áp lực thủy của hệ thống và xả "
      "rửa, cũng cần thay trim bằng một bộ trim hy sinh tạm thời.",
      "When welding socket weld-end or butt weld-end valves in-line, the control valve trim needs "
      "to be removed in order to prevent damage to trim parts. The trim also needs to be replaced "
      "with a temporary sacrificial trim set while conducting the system hydrostatic test and "
      "flushing the system.")
    P("<i>Lưu ý: Rất nên lắp trim ứng dụng cuối cùng chỉ sau khi van đã được hàn vào đường ống, "
      "đường ống đã được xả rửa và thử áp lực thủy xong.</i>",
      "<i>Note: It is strongly recommended that the final application trim not be installed until "
      "after the valve has been welded in the line, the line flushed, and hydrostatically tested</i>")
    P("Sau khi một hoặc nhiều van được hàn vào đường ống, thường có yêu cầu thử áp lực và xả rửa hệ "
      "thống. Thử áp lực hệ thống thường theo quy định thực hiện ở mức 1-1/2 lần áp suất làm việc "
      "nguội hoặc áp suất thiết kế của hệ thống. Thường thì, giả sử van ở vị trí mở trong lúc thử, "
      "chi tiết duy nhất có thể bị ảnh hưởng bất lợi ở áp lực đó là đệm kín thân van (packing). "
      "Đệm PTFE có thể bị ép tràn nhẹ do thử áp lực cao, vì vậy khuyến nghị ít nhất nên thay đệm "
      "PTFE sau khi thử áp lực.",
      "After a valve or valves are welded in a line, there normally are requirements to hydro and "
      "flush the system. It is not uncommon for the system hydro to be consistent with codes that "
      "state that the hydro is to be conducted at 1-1/2 times the system cold working pressure or "
      "design pressure. Normally, the only valve components that may be adversely affected by this "
      "level of a hydro pressure (assuming that the valve is in the open position during hydro) "
      "would be the valve stem packing. PTFE packing may exhibit some extrusion resulting from a "
      "high-pressure hydro, and therefore it is recommended that at a minimum the PTFE packing "
      "should be replaced after a hydro test.")
    P("Đệm graphit không cần thay nếu van được đưa vào vận hành trong thời gian ngắn. Để đệm graphit "
      "ướt trong van không hoạt động quá lâu có thể gây ăn mòn điện hóa thân van. Tuy nhiên, vì hệ "
      "thống thường được xả rửa cùng lúc, nên cần lắp một bộ trim hy sinh để đáp ứng cả thử áp lực "
      "lẫn xả rửa.",
      "Graphite packing should not need to be replaced if the valve is to be put into service "
      "within a short time period. Leaving wet graphite packing in an inactive valve long term may "
      "result in galvanic corrosion of the valve stem. However, since the system is normally "
      "flushed at the same time, a sacrificial set of trim should be installed to handle both "
      "hydro testing and flushing.")
    P("Với một số van điều khiển và van điều hòa hơi, thao tác xả rửa không đi qua van từ đầu vào đến "
      "đầu ra. Do thiết kế hoặc ứng dụng của van, quá trình xả rửa có thể đi vào đầu vào hoặc đầu "
      "ra (tùy cấu hình) rồi ra qua lỗ nắp (bonnet). Kiểu trim xả rửa này thường được gọi là trim "
      "«xả thổi» (blow down) hoặc «đẩy ra» (blow out).",
      "With some control valves and steam conditioning valves, the flushing operation does not go "
      "through the valve from valve inlet to outlet. Because of the valve design or application, "
      "the flushing operation may either go in the valve inlet, or outlet (depending on "
      "configuration) and out the bonnet opening. This type of flushing trim is more commonly "
      "known as “blow down” or “blow out” trim.")
    P("Việc xả rửa hệ thống có thể tạo ra điều kiện làm hỏng trim van điều khiển, chẳng hạn xỉ hàn, "
      "gỉ, ăn mòn chảy qua van. Các vật liệu này làm hỏng bề mặt ép đế và thường bịt tắc các lỗ "
      "khoan hoặc trim dạng đĩa xếp chồng. Vì vậy luôn khuyến nghị tháo trim van và lắp một dạng trim "
      "xả rửa tiêu hao thay thế. Sau khi hàn van vào đường ống, thường còn xỉ hàn bên trong đường "
      "ống, ngoài vảy bong ra từ thành ống do nhiệt độ của quá trình hàn. Nếu vật liệu này chảy "
      "qua van, rất có thể làm tắc trim và làm hỏng tính kín của đế van.",
      "Flushing the system presents some conditions that can damage the control valve trim. These "
      "conditions can include weld slag, rust, corrosion, etc. being flowed through the valve. "
      "These materials can damage the valve seating surface and will often plug drilled hole or "
      "stacked disk trims. Therefore, it is always recommended that the valve trim be removed and "
      "some form of expendable flushing trim installed. After welding valves in a line, there is "
      "usually weld slag inside the line, in addition to scale that has been dislodged from the "
      "inside of the valve piping due to temperatures associated with the welding process. If this "
      "material was flowed through the valve, it would likely plug the valve trim and possibly "
      "damage the seating integrity of the valve.")

    # ------------------------------------------------------------ 8.3
    H("8.3 Bảo trì van điều khiển", "8.3 Control Valve Maintenance")
    P("Luôn tuân theo hướng dẫn bảo trì của nhà sản xuất van điều khiển. Các nội dung bảo trì điển "
      "hình được tóm tắt ở đây.",
      "Always follow the control valve manufacturer's maintenance instructions. Typical "
      "maintenance topics are summarized here.")
    P("Tối ưu hóa tài sản van điều khiển phụ thuộc vào triết lý và chương trình bảo trì hiệu quả. "
      "Ba cách tiếp cận cơ bản nhất là:",
      "Optimization of control valve assets depends on an effective maintenance philosophy and "
      "program. Three of the most basic approaches are:")
    B(["Phản ứng — Hành động được thực hiện sau khi sự kiện đã xảy ra. Chờ van có sự cố rồi sửa hoặc "
       "thay thế.",
       "Phòng ngừa — Hành động được thực hiện theo lịch dựa trên lịch sử; tức là cố ngăn không cho "
       "điều xấu xảy ra.",
       "Dự báo — Hành động được thực hiện dựa trên dữ liệu hiện trường dùng thiết bị chẩn đoán, thử "
       "nghiệm và đánh giá không xâm lấn tiên tiến hoặc dùng thiết bị thông minh."],
      ["Reactive – Action is taken after an event has occurred. Wait for something to happen to a "
       "valve and then repair or replace it.",
       "Preventive – Action is taken on a timetable based on history; that is, try to prevent "
       "something bad from happening.",
       "Predictive – Action is taken based on field input using state-of-the-art, non-intrusive "
       "diagnostic test and evaluation devices or using smart instrumentation."])
    P("Dù cả chương trình phản ứng lẫn phòng ngừa đều có tác dụng, chúng không tối ưu được tiềm năng "
      "của van. Sau đây là một số nhược điểm của từng cách tiếp cận.",
      "Although both reactive and preventive programs work, they do not optimize valve potential. "
      "Following are some of the disadvantages of each approach.")

    H("8.3.1 Bảo trì phản ứng", "8.3.1 Reactive Maintenance", h3)
    P("Bảo trì phản ứng để các khiếm khuyết nhỏ không được chú ý và xử lý, đơn giản vì không có dấu "
      "hiệu rõ ràng của sự cố. Ngay cả van quan trọng cũng có thể bị bỏ quên cho đến khi rò rỉ quá "
      "mức hoặc không hành trình đúng. Trong một số trường hợp, phản hồi từ bộ phận sản xuất giúp "
      "bảo trì phản ứng trước khi vấn đề nghiêm trọng phát triển, nhưng van cũng có thể bị tháo "
      "không cần thiết chỉ vì nghi ngờ hỏng. Van lớn hoặc van hàn trực tiếp vào đường ống có thể "
      "cần một ngày hoặc lâu hơn để tháo, tháo rời, kiểm tra và lắp lại. Thời gian và nguồn lực có "
      "thể bị lãng phí mà không giải quyết được vấn đề nếu triệu chứng thực chất do bộ phận khác "
      "của hệ thống gây ra.",
      "Reactive maintenance allows subtle deficiencies to go unnoticed and untreated, simply "
      "because there is no clear indication of a problem. Even critical valves might be neglected "
      "until they leak excessively or fail to stroke properly. In some cases, feedback from "
      "production helps maintenance react before serious problems develop, but valves might be "
      "removed unnecessarily on the suspicion of malfunction. Large valves or those welded in-line "
      "can require a day or longer for removal, disassembly, inspection, and re-installation. Time "
      "and resources could be wasted without solving the problem if the symptoms are actually "
      "caused by some other part of the system.")

    H("8.3.2 Bảo trì phòng ngừa", "8.3.2 Preventive Maintenance", h3)
    P("Bảo trì phòng ngừa nhìn chung là cải tiến đáng kể. Tuy nhiên, vì lịch bảo trì thu được rất "
      "ít thông tin về các van đang vận hành, nhiều nhà máy chỉ đơn giản đại tu tất cả van điều "
      "khiển theo lịch luân phiên. Các chương trình như vậy dẫn đến việc bảo dưỡng một số van "
      "không cần sửa hay chỉnh, trong khi để lại những van khác trong hệ thống rất lâu sau khi "
      "chúng ngừng vận hành hiệu quả.",
      "Preventive maintenance generally represents a significant improvement. However, because "
      "maintenance schedules have been able to obtain little information on valves that are "
      "operating, many plants simply overhaul all control valves on a rotating schedule. Such "
      "programs result in servicing some valves that need no repair or adjustment and leaving "
      "others in the system long after they have stopped operating efficiently.")

    H("8.3.3 Bảo trì dự báo", "8.3.3 Predictive Maintenance", h3)
    P("Ngày nay, người vận hành nhà máy thường kéo dài thời gian giữa các lần dừng máy định kỳ lên "
      "ba hoặc bốn năm, thậm chí lâu hơn, để tối đa thời gian vận hành. Những chu kỳ chạy kéo dài "
      "này làm giảm cơ hội chẩn đoán van truyền thống khi van phải ngừng hoạt động.",
      "Today, plant operators often extend the time between turnarounds to three or four years, "
      "and even longer, in order to maximize plant uptime. These extended run times offer less "
      "opportunity for traditional, out-of-service valve diagnostics.")
    P("Quá trình bảo trì truyền thống gồm bốn chế độ riêng biệt:",
      "The traditional maintenance process consists of four distinct modes:")
    B(["Phát hiện lỗi — Phần lớn công sức bảo trì van dành cho việc giám sát van khi đang vận hành "
       "để phát hiện sự cố. Khi xác định được lỗi, quá trình chuyển sang phân biệt lỗi.",
       "Phân biệt lỗi — Ở chế độ này, tài sản van được đánh giá để xác định nguyên nhân lỗi và thiết "
       "lập hướng hành động khắc phục.",
       "Khôi phục quá trình — Hành động khắc phục được thực hiện để sửa nguồn gốc của khiếm khuyết.",
       "Xác nhận — Ở chế độ cuối cùng, tài sản van được đánh giá so với trạng thái như mới hoặc so "
       "với đường cơ sở gần đây nhất. Sau khi xác nhận, quá trình bảo trì trở lại trạng thái phát "
       "hiện lỗi."],
      ["Fault Detection – A majority of valve maintenance effort is spent in monitoring valves "
       "while in service to detect the occurrence of a fault. When a fault is identified, the "
       "maintenance process transitions to fault discrimination.",
       "Fault Discrimination – During this mode, valve assets are evaluated to determine the "
       "cause of the fault and to establish a course of corrective action.",
       "Process Recovery – Corrective action is taken to fix the source of the defect.",
       "Validation – In this final mode, valve assets are evaluated relative to either as-new "
       "condition or the last established baseline condition. Once validated, the maintenance "
       "process returns to fault detection status."])

    H("8.3.4 Sử dụng chẩn đoán van điều khiển", "8.3.4 Using Control Valve Diagnostics", h3)
    P("Sự xuất hiện của thiết bị van vi xử lý có khả năng chẩn đoán khi đang vận hành đã cho phép "
      "các công ty thiết kế lại thực hành công việc bảo trì van điều khiển của mình. Các thiết bị "
      "số này cải thiện đáng kể khía cạnh phát hiện và phân biệt lỗi của chương trình bảo trì "
      "truyền thống.",
      "The advent of micro-processor-based valve instruments with their in-service diagnostics "
      "capabilities has allowed companies to redesign their control valve maintenance work "
      "practices. These digital devices significantly improve the fault detection and "
      "discrimination aspects of traditional maintenance programs.")
    P("Ví dụ, chẩn đoán khi đang vận hành (Hình 8.3) có thể phát hiện sự cố về chất lượng khí nén "
      "thiết bị, rò rỉ và hạn chế áp suất cấp, đồng thời nhận diện các vấn đề của van như ma sát "
      "quá mức, vùng chết và sai lệch hiệu chuẩn. Khi phát hiện sự cố, mức độ nghiêm trọng được "
      "báo cáo, các nguyên nhân có thể được liệt kê và hướng xử lý được đưa ra.",
      "For example, in-service diagnostics (Figure 8.3) can detect problems with instrument air "
      "quality, leakage and supply pressure restriction, and can identify valve problems, such as "
      "excessive friction, deadband, and falling out of calibration. When a problem is identified, "
      "its severity is reported, possible causes are listed, and a course of action is given.")
    FIG(3, F.fig_f8_03())
    P("Các chẩn đoán này thường dẫn đến một trong ba tình trạng:",
      "These diagnostics typically result in one of three conditions:")
    B(["Không phát hiện lỗi (tình trạng xanh). Van nên tiếp tục vận hành và việc giám sát nên "
       "tiếp tục.",
       "Cảnh báo đã phát hiện lỗi nhưng điều khiển không bị ảnh hưởng (tình trạng vàng). Đây là dấu "
       "hiệu dự báo rằng vấn đề phát hiện có khả năng ảnh hưởng đến điều khiển và cần lên kế hoạch "
       "bảo trì trong tương lai.",
       "Báo cáo lỗi cho thấy đã phát hiện lỗi ảnh hưởng đến điều khiển (tình trạng đỏ). Những lỗi "
       "này nhìn chung cần được xử lý ngay."],
      ["No fault detected (green condition). The valve should remain in service, and monitoring "
       "should continue.",
       "A warning that a fault has been detected, but control remains unaffected (yellow "
       "condition). This is a predictive indication that the detected problem has the potential "
       "to affect control and that future maintenance should be planned.",
       "An error report that a fault affecting control has been detected (red condition). These "
       "faults generally require immediate attention."])
    P("Cụ thể hơn, chẩn đoán khi đang vận hành giám sát rò rỉ khí nén thiết bị, áp suất cấp, độ lệch "
      "hành trình và chỉnh relay, chất lượng khí nén thiết bị, ma sát, v.v.",
      "More specifically, in-service diagnostics oversee instrument air leakage, supply pressure, "
      "travel deviation and relay adjustment, instrument air quality, friction, etc.")

    H("8.3.4.1 Rò rỉ khí nén thiết bị", "8.3.4.1 Instrument Air Leakage", h4)
    P("Chẩn đoán lưu lượng khối không đo lưu lượng khí nén thiết bị đi qua cụm cơ cấu chấp hành. Nhờ "
      "nhiều cảm biến, chẩn đoán này phát hiện được cả dòng khí dương (cấp) lẫn âm (xả) từ bộ điều "
      "khiển van số. Chẩn đoán này không chỉ phát hiện rò rỉ trong cơ cấu chấp hành hoặc ống liên "
      "quan, mà còn phát hiện được các vấn đề khó hơn. Ví dụ, ở cơ cấu chấp hành piston, chẩn đoán "
      "lưu lượng khối có thể phát hiện phớt piston bị rò hoặc o-ring hư.",
      "Air mass flow diagnostics measure instrument air flow through the actuator assembly. "
      "Because of multiple sensors, this diagnostic can detect both positive (supply) and negative "
      "(exhaust) air mass flow from the digital valve controller. This diagnostic not only detects "
      "leaks in the actuator or related tubing, but also much more difficult problems. For "
      "example, in piston actuators, the air mass flow diagnostic can detect leaking piston seals "
      "or damaged o-rings.")

    H("8.3.4.2 Áp suất cấp", "8.3.4.2 Supply Pressure", h4)
    P("Chẩn đoán áp suất cấp phát hiện các vấn đề của van điều khiển liên quan đến áp suất cấp. "
      "Chẩn đoán khi đang vận hành này phát hiện cả chỉ số áp suất cấp thấp lẫn cao. Ngoài việc "
      "kiểm tra áp suất cấp đầy đủ, chẩn đoán này có thể dùng để phát hiện và định lượng độ sụt áp "
      "của nguồn khí trong các chuyển động hành trình lớn. Điều này đặc biệt hữu ích để xác định "
      "đường cấp bị hạn chế.",
      "The supply pressure diagnostic detects control valve problems related to supply pressure. "
      "This in-service diagnostic will detect both low and high supply pressure readings. In "
      "addition to checking for adequate supply pressure, this diagnostic can be used to detect "
      "and quantify droop in the air supply during large travel excursions. This is particularly "
      "helpful in identifying supply line restrictions.")

    H("8.3.4.3 Độ lệch hành trình và chỉnh relay",
      "8.3.4.3 Travel Deviation and Relay Adjustment", h4)
    P("Chẩn đoán độ lệch hành trình dùng để giám sát áp suất cơ cấu chấp hành và độ lệch hành trình "
      "so với điểm đặt. Chẩn đoán này hữu ích để nhận diện van bị kẹt, liên kết được kích hoạt "
      "(interlocks), áp suất cấp thấp hoặc sự thay đổi trong hiệu chuẩn hành trình.",
      "The travel deviation diagnostic is used to monitor actuator pressure and travel deviation "
      "from setpoint. This diagnostic is useful in identifying a stuck control valve, active "
      "interlocks, low supply pressure, or shifts in travel calibration.")
    P("Chẩn đoán chỉnh relay dùng để giám sát áp suất chuyển tiếp trên các cơ cấu chấp hành tác động "
      "kép. Nếu áp suất chuyển tiếp quá thấp, cơ cấu chấp hành mất độ cứng, làm vị trí nút van dễ "
      "bị lực quá trình lấn át. Nếu áp suất chuyển tiếp đặt quá cao, cả hai buồng đều gần bằng áp "
      "suất cấp, lực khí nén xấp xỉ bằng nhau, lực lò xo chiếm ưu thế và cơ cấu chấp hành chuyển "
      "đến vị trí an toàn do lò xo (spring-fail).",
      "The relay adjustment diagnostic is used to monitor crossover pressure on double-acting "
      "actuators. If the crossover pressure is too low, the actuator loses stiffness, making the "
      "valve plug position susceptible to being overcome by process forces. If the crossover "
      "pressure is set too high, both chambers will be near supply, the pneumatic forces will be "
      "roughly equal, the spring force will be dominant and the actuator will move to its "
      "spring-fail position.")

    H("8.3.4.4 Chất lượng khí nén thiết bị", "8.3.4.4 Instrument Air Quality", h4)
    P("Chẩn đoán giám sát I/P và relay có thể nhận diện các sự cố như tắc ở chi tiết chính của I/P "
      "hoặc ở vòi I/P, hỏng màng thiết bị, hỏng o-ring của I/P và sai lệch hiệu chuẩn I/P. Chẩn "
      "đoán này đặc biệt hữu ích để xác định sự cố do chất bẩn trong nguồn khí và do nhiệt độ cực "
      "đoan.",
      "The I/P and relay monitoring diagnostic can identify problems such as plugging in the I/P "
      "primary or in the I/P nozzle, instrument diaphragm failures, I/P instrument o-ring "
      "failures, and I/P calibration shifts. This diagnostic is particularly useful in identifying "
      "problems from contaminants in the air supply and from temperature extremes.")

    H("8.3.4.5 Ma sát khi vận hành và xu hướng ma sát",
      "8.3.4.5 In-Service Friction and Friction Trending", h4)
    P("Chẩn đoán ma sát và vùng chết khi đang vận hành xác định ma sát trong cụm van khi cụm này do "
      "hệ thống điều khiển điều khiển. Dữ liệu chẩn đoán ma sát được thu thập và lập xu hướng để "
      "phát hiện những thay đổi của van ảnh hưởng đến điều khiển quá trình.",
      "The in-service friction and deadband diagnostic determines friction in the valve assembly "
      "as it is controlled by the control system. Friction diagnostics data is collected and "
      "trended to detect valve changes that affect process control.")

    H("8.3.4.6 Các ví dụ khác", "8.3.4.6 Other Examples", h4)
    P("Có thể cấu hình chẩn đoán tùy biến khi đang vận hành để thu thập và vẽ đồ thị bất kỳ biến "
      "đo nào của van thông minh. Chẩn đoán tùy biến có thể định vị và phân biệt lỗi mà các cách "
      "khác không phát hiện được. Thông thường các lỗi này phức tạp và cần chuyên môn bên ngoài. "
      "Trong những trường hợp đó, dữ liệu do nhân viên bảo trì tại chỗ thu thập rồi gửi cho chuyên "
      "gia giám sát tình trạng van để phân tích sâu hơn, từ đó tránh được chi phí và độ trễ của "
      "một chuyến đi đến hiện trường.",
      "In-service custom diagnostics can be configured to collect and graph any measured variable "
      "of a smart valve. Custom diagnostics can locate and discriminate faults not detectable by "
      "other means. Often, these faults are complicated and require outside expertise. In such "
      "cases, data is collected by local maintenance personnel and is then sent to a valve "
      "condition monitoring specialist for further analysis. Therefore, avoiding the costs and "
      "delays associated with an on-site visit.")

    H("8.3.5 Tiếp tục phát triển chẩn đoán",
      "8.3.5 Continued Diagnostics Development", h3)
    P("Nhìn chung, các ngành công nghiệp quá trình sẽ tiếp tục đòi hỏi hiệu quả ngày càng cao về "
      "chất lượng, năng suất và độ tin cậy. Riêng từng nhà sản xuất sẽ tiếp tục kéo dài thời gian "
      "giữa các lần dừng máy. Những yêu cầu này dẫn đến ít cơ hội bảo trì hơn cho công tác sửa chữa "
      "thiết bị đo. Câu trả lời tất yếu cho thiếu hụt này là các phát triển chẩn đoán trong tương "
      "lai tập trung vào khả năng thử nghiệm và đánh giá không xâm lấn khi đang vận hành, chẳng hạn "
      "như giám sát tình trạng van.",
      "Overall, the process industries will continue to demand more and more efficiency in terms "
      "of quality, yield, and reliability. Individually, producers will continue to lengthen time "
      "between turnarounds. These demands will lead to fewer maintenance opportunities being "
      "available for instrumentation repair. The inevitable answer to this shortfall will be "
      "future diagnostic developments that focus on in-service, non-intrusive test and evaluation "
      "capabilities, such as valve condition monitoring.")
    P("Khả năng đánh giá hiệu năng van qua chẩn đoán khi đang vận hành cải thiện việc lập kế hoạch "
      "dừng máy, vì thông tin thu thập được dùng để xác định chính xác van cần bảo trì lẫn van còn "
      "tốt. Hình 8.4 minh họa cụm van điển hình với cơ cấu chấp hành lò xo - màng — đối tượng được "
      "đánh giá tình trạng.",
      "The ability to evaluate valve performance via in-service diagnostics improves turnaround "
      "planning as the information gathered can be used to pinpoint valve maintenance that is "
      "necessary, as well as valves that are healthy. Figure 8.4 shows the typical valve assembly "
      "with a spring-and-diaphragm actuator whose health is assessed.")
    FIG(4, F.fig_f8_04())
    P("Một giải pháp là dùng thiết bị đo van thông minh vi xử lý đánh giá tình trạng vận hành của "
      "cụm van điều khiển trong khi van vẫn đang vận hành. Dữ liệu được thu thập mà không can thiệp "
      "vào vận hành quá trình bình thường. Thiết bị phân tích thông tin theo thời gian thực và đưa "
      "ra khuyến nghị bảo trì cho từng vấn đề vận hành mà nó nhận diện được.",
      "An answer is to utilize smart, micro-processor-based valve instrumentation that evaluates "
      "the operating health of the control valve assembly while the valve is in service. Data is "
      "collected without intruding on normal process operations. The instrumentation analyzes the "
      "information in real-time and provides maintenance recommendations for each valve operating "
      "problem that it identifies.")

    # ------------------------------------------------------------ 8.4
    H("8.4 Phụ tùng dịch vụ và sửa chữa", "8.4 Service and Repair Parts")

    H("8.4.1 Dùng phụ tùng của nhà sản xuất gốc (OEM)",
      "8.4.1 Using Original Equipment Manufacturers (OEM) Parts", h3)
    P("Để duy trì an toàn và tính toàn vẹn của nhà máy, cũng như đảm bảo hiệu năng mong đợi của van, "
      "điều bắt buộc là phụ tùng dịch vụ sử dụng phải có nguồn gốc từ OEM. Chính OEM hoặc đại lý "
      "được ủy quyền là nguồn duy nhất có các thông số kỹ thuật cần thiết cho những phụ tùng đó.",
      "To maintain plant safety and integrity, as well as ensure the expected performance from a "
      "valve, it is imperative that the service parts utilized be from the OEM. The OEM, or their "
      "authorized agent, are the only source who has the required specifications for the service "
      "parts.")
    P("Lợi ích của việc dùng phụ tùng Fisher chính hãng gồm:",
      "Benefits of using OEM Fisher Parts include:")
    B(["Tăng an toàn cho nhà máy và nhân viên",
       "Tăng độ tin cậy của van điều khiển",
       "Giảm rủi ro pháp lý và môi trường",
       "Giảm chi phí để đẩy nhanh có được phụ tùng",
       "Reducded maintenance costs",
       "Tăng thời gian vận hành của nhà máy",
       "Hiệu năng van tối đa"],
      ["Increased plant and employee safety",
       "Increased control valve reliability",
       "Reduced legal and environmental risk",
       "Reduced expenditures expediting spare parts",
       "Reducded maintenance costs",
       "Increased plant uptime",
       "Maximum valve performance"])
    P("Phụ tùng sao chép cho van điều khiển có sẵn từ nhiều nguồn. Dù các chi tiết này trông có vẻ "
      "giống hệt, chúng không được chế tạo theo thông số của thiết kế gốc và không được thử nghiệm "
      "đầy đủ để xác nhận hiệu năng. Không khuyến nghị dùng các chi tiết "
      "này. Phụ tùng nhái có thể rẻ hơn khi mua nhưng cũng có thể dẫn đến chi phí tổng cao hơn cho "
      "tổ chức do thời gian dừng máy ngoài kế hoạch, ảnh hưởng đến an toàn và lợi nhuận.",
      "Replicated parts for control valves are available from a variety of sources. Although these "
      "parts may look identical, they are not manufactured to the specifications of the original "
      "design or thoroughly tested to validate their performance. The use of these parts is not "
      "recommended. Imitation parts may cost less to purchase but may also result in overall higher "
      "costs to the organization due to unplanned downtime, impacting safety and profitability.")
    P("Các OEM trong ngành van tham gia xây dựng và duy trì liên tục các tiêu chuẩn ngành vì họ có "
      "kiến thức chuyên sâu về ứng dụng và vật liệu có thể dùng để cải thiện tiêu chuẩn và mang lại "
      "lợi ích cho người dùng cuối. Bên sao chép thường thiếu chuyên môn cần thiết để tham gia "
      "giám sát tiêu chuẩn và thử nghiệm phát triển. Sự thiếu chuyên môn này có thể ảnh hưởng đến "
      "độ tin cậy lâu dài của van, đe dọa an toàn người lao động, làm hỏng thiết bị và gây dừng "
      "nhà máy.",
      "Valve industry OEMs participate in the development and ongoing upkeep of industry standards "
      "because they have specialized application and materials knowledge that can be used to "
      "enhance the standards and benefit end-users. Replicators typically lack the level of "
      "expertise required to participate in standards oversight and development testing. This lack "
      "of expertise can potentially impact long-term valve reliability, threaten workers' safety, "
      "damage equipment, and cause plant shutdowns.")
    P("Ngoài ra, việc dùng phụ tùng thay thế không được ủy quyền thường làm mất hiệu lực bảo hành "
      "sản phẩm của OEM.",
      "Additionally, the use of unauthorized replacement parts typically voids any OEM product "
      "warranty.")

    H("8.4.2 Phụ tùng dự phòng đề xuất", "8.4.2 Recommended Spare Parts", h3)
    P("Nhiều công ty xác định một số chi tiết là phụ tùng dự phòng đề xuất và cung cấp danh sách "
      "các chi tiết đó cho một van hoặc cơ cấu chấp hành cụ thể. Danh sách này gọi là «Danh sách phụ "
      "tùng dự phòng đề xuất» (RSPL). Danh sách dựa trên ý tưởng một số cấu phần sẽ hao mòn theo "
      "thời gian. Đó là những chi tiết làm việc. Trong van, đó có thể là phần tử điều khiển (tức là "
      "nút/ty, cage, đĩa, bi, trục, ổ bi, v.v.) hoặc các chi tiết làm kín (tức là đế, vòng đệm, "
      "phớt cân bằng, packing, v.v.). Trong cơ cấu chấp hành, đó có thể là màng, o-ring, bạc, v.v.",
      "Many companies will identify parts as a recommended spare and provide a list of these parts "
      "for a given valve or actuator. This list is referred to as a “Recommended Spare Parts List” "
      "(RSPL). The list is based on the idea that certain components will wear over time. These "
      "components are the parts that do the work. In a valve, it could be the controlling element "
      "(i.e. plug/stem, cage, disk, ball, shaft, bearings, etc.) or the sealing components (i.e. "
      "seat, seal ring, balance seal, packing, etc.). In an actuator it could be the diaphragm, "
      "o-rings, bushings, etc.")
    FIG(5, F.fig_f8_05())
    P("Người dùng nên cân nhắc dự trữ các chi tiết đề xuất để có sẵn khi cần bảo dưỡng van. Duy trì "
      "tồn kho tại chỗ cho công tác bảo trì nội bộ có thể là khoản đầu tư lớn và dẫn đến lượng "
      "phụ tùng tồn đáng kể.",
      "Users should consider stocking recommended parts for quick availability to service the "
      "valve when required. Keeping an on-hand inventory of parts for in-house maintenance, could "
      "be a large investment and can lead to a considerable amount of parts stocked.")
    P("Cần cân nhắc một số yếu tố khi quyết định dự trữ cái gì. Trước hết là mức độ quan trọng của "
      "van hoặc tài sản. Dự trữ đúng phụ tùng tại chỗ tăng sự tự tin của người dùng vào khả năng "
      "thực hiện, chất lượng và an toàn của lần sửa chữa. Thứ hai, cân nhắc rủi ro khi thiết bị "
      "không vận hành như ý trong bất kỳ khoảng thời gian ngừng hoạt động nào. Có phụ tùng sẵn giúp "
      "rút ngắn thời gian sửa chữa nhờ giải pháp ngay lập tức khi van điều khiển ngừng chạy. Điều "
      "này giảm các vấn đề tiềm ẩn về môi trường, an toàn và lắp đặt. Thứ ba, cân nhắc sự sẵn có "
      "của phụ tùng cần thiết — chúng có được cung cấp nhanh từ nhà sản xuất hoặc đại lý được ủy "
      "quyền không?",
      "Several factors should be considered when deciding what to stock. The first thing to "
      "consider is the criticality of the valve or asset. Stocking the right spare parts in-house "
      "increases user confidence in the ability to perform, performance quality of, and safety of "
      "a repair. Second, consider the risk of not having the unit function as intended for any "
      "given amount of time the asset is down. Having parts stocked minimizes the time of repair "
      "by providing an immediate solution when a control valve is down. This reduces potential "
      "environmental, safety, and installation issues. Then third, consider what is the "
      "availability of the parts needed, are they available quickly from the manufacturer or "
      "manufacturer's authorized agent?")
    P("Dù việc dự trữ phụ tùng bảo trì giúp giảm chi phí đẩy nhanh khi có dừng máy ngoài kế hoạch, "
      "trong trường hợp chi tiết không có sẵn tại chỗ, mạng lưới kho của OEM vẫn có thể hỗ trợ giao "
      "trong ngày hoặc qua đêm. OEM thường cố đáp ứng nhu cầu phụ tùng của khách hàng bằng sự kết "
      "hợp của mạng lưới văn phòng bán hàng toàn cầu có hàng, các nhà máy sản xuất khu vực, kho phụ "
      "tùng và cơ sở dịch vụ có khả năng chế tạo phụ tùng trong tình huống khẩn cấp.",
      "Although, inventorying parts for maintenance lowers cost spent on expediting when "
      "unexpected downtime occurs, in situations when a part is not stocked in-house, an OEM "
      "warehouse network can potentially support same-day or overnight delivery of expediting "
      "parts. OEM's typically try to support customer parts needs with a combination of a global "
      "network of sales offices with stock, regional manufacturing plants, spare parts warehouses, "
      "and service facilities capable of manufacturing parts in emergency situations.")
    P("Nhà sản xuất có thể cung cấp danh sách phụ tùng hợp nhất, trong đó xác định các chi tiết dùng "
      "được cho nhiều van trong cùng cơ sở của bạn.",
      "The manufacturer may be able to provide a consolidated spares list where they have "
      "identified parts that could be used in multiple valves across your facility.")

    H("8.4.3 Tiện lợi của bộ phụ tùng", "8.4.3 The Convenience of Parts Kits", h3)
    P("Bộ phụ tùng thường được thiết kế để cung cấp các phụ tùng cần thiết nhằm sửa cụm van dựa trên "
      "một vấn đề cụ thể hoặc một loại công việc sửa chữa. Ví dụ là sửa rò rỉ đế van hoặc rò rỉ "
      "packing, thậm chí hỗ trợ mở và kiểm tra cơ bản một van. Các chi tiết trong bộ có thể là sự "
      "kết hợp của cả chi tiết cứng và chi tiết mềm. Người dùng thường có lựa chọn thay thế một số "
      "chi tiết hoặc thay toàn bộ chi tiết nhận được trong bộ để đưa cụm đã mòn về trạng thái tối "
      "ưu.",
      "Parts Kits are typically designed to provide the spare parts needed to repair a valve "
      "assembly based on a specific issue or a type of repair. An example of this would be to "
      "repair a valve seat leak or packing leak, or even support a basic opening and inspection of "
      "a valve. Parts included in these kits may be a combination of both hard parts and soft "
      "parts. The user typically has the option to replace selected parts or replace all the parts "
      "received in the kit to repair a worn assembly back to optimal condition.")
    FIG(6, F.fig_f8_06())
    FIG(7, F.fig_f8_07())
    P("Việc có sẵn bộ kit cải thiện kiểm soát tồn kho khi dự trữ tại chỗ. Có tồn kho dạng kit giúp "
      "giảm diện tích chiếm dụng và số mã phụ tùng phải quản lý.",
      "Kitting availability improves inventory control when stocking kits in-house. Having kit "
      "inventory reduces occupied space and the amount of part numbers to manage.")
    P("Điều này cho phép người dùng lấy một bộ mà không cần đặt từng chi tiết và đảm bảo rằng mọi "
      "chi tiết cần thiết cho lần sửa chữa đều đến cùng lúc.",
      "This allows the user to retrieve a kit without needing to order individual parts and "
      "assures the user all parts needed for the repair will securely arrive.")

    H("8.4.4 Cân nhắc nâng cấp trim van", "8.4.4 Consider Upgrades for the Valve Trim", h3)
    P("Trong chu kỳ bảo trì, luôn quan trọng là kiểm tra chi tiết và cân nhắc nhu cầu nâng cấp. Các "
      "cân nhắc có thể là ồn khi van vận hành, hư hại trim quá mức, hoặc thông số vận hành của hệ "
      "thống đã thay đổi so với thiết kế ban đầu. Nhiều khi chỉ cần thay đổi trim van là giải quyết "
      "được những vấn đề này.",
      "During the maintenance cycle, it is always important to examine parts and consider the need "
      "to upgrade. Considerations could be valve noise when operating, excessive trim damage, or "
      "if system operating parameters have changed from the original design. Many times changes "
      "to the valve trim can address these issues.")

    # ------------------------------------------------------------ 8.5
    H("8.5 Bảo trì cơ cấu chấp hành", "8.5 Actuator Maintenance")

    H("8.5.1 Cơ cấu chấp hành lò xo - màng",
      "8.5.1 Spring-and-Diaphragm Actuators", h3)
    P("Hầu hết cơ cấu chấp hành lò xo - màng khí nén dùng màng ép khuôn. Màng ép khuôn giúp lắp đặt "
      "dễ dàng, cho diện tích hiệu dụng tương đối đồng đều trong suốt hành trình van và cho phép "
      "hành trình lớn hơn so với màng dạng tấm phẳng. Khí cấp vào màng tạo lực cho cơ cấu chấp hành "
      "theo một chiều, còn lò xo tạo lực theo chiều ngược lại. Vì khí chỉ tạo lực một chiều, các "
      "cơ cấu này thường được gọi là cơ cấu chấp hành tác động đơn.",
      "Most pneumatic spring-and-diaphragm actuators use a molded diaphragm. The molded diaphragm "
      "facilitates installation, provides a relatively uniform effective area throughout valve "
      "travel, and permits greater travel than could be possible with a flat-sheet diaphragm. Air "
      "to the diaphragm provides the actuator force in one direction and a spring will provide the "
      "force in the other direction. Since the air provides the force in only one direction, these "
      "actuators are often times referred to a single-acting actuators.")

    H("8.5.2 Cơ cấu chấp hành piston", "8.5.2 Piston Actuators", h3)
    P("Cơ cấu chấp hành piston dùng piston với phớt o-ring hoặc quad ring trong xi lanh. Khí có thể "
      "được cấp vào cả hai phía piston để tạo lực theo một trong hai chiều; các cơ cấu này được gọi "
      "là cơ cấu tác động kép. Cơ cấu chấp hành piston cũng có thể dùng lò xo để thay khí ở một "
      "phía piston hoặc để tạo lực bổ sung cùng khí.",
      "Piston actuators utilize a piston with an o-ring or quad ring seal within a cylinder. Air "
      "can be supplied to both sides of the piston to provide the actuator force in either "
      "direction, these are said to be double-acting actuators. A piston actuator may also utilize "
      "a spring to replace the air on one side of the piston or to provide additional force with "
      "the air.")

    H("8.5.3 Đệm kín thân van", "8.5.3 Stem Packing", h3)
    P("Packing (Hình 8.9) tạo lớp kín áp suất quanh thân của thân van kiểu cầu, kiểu góc và quanh "
      "trục của van quay. Cần thay packing nếu rò rỉ phát triển quanh thân hoặc nếu van được tháo "
      "rời hoàn toàn để bảo trì hoặc kiểm tra. Trước khi nới đai ốc packing, hãy đảm bảo không còn "
      "áp suất trong thân van.",
      "Packing (Figure 8.9), which provides the pressure seal around the stem of a globe-style, "
      "angle-style valve body, and the shaft of a rotary valve should be replaced if leakage "
      "develops around the stem, or if the valve is completely disassembled for other maintenance "
      "or inspection. Before loosening packing nuts, make sure there is no pressure in the valve "
      "body.")
    P("Tháo packing mà không tháo cơ cấu chấp hành thì khó và không được khuyến nghị. Cũng không nên "
      "cố thổi các vòng packing cũ ra bằng cách cấp áp suất vào lỗ bôi trơn trên nắp van. Cách này "
      "có thể nguy hiểm và hiệu quả kém, vì nhiều cấu hình packing có khoảng một nửa số vòng nằm "
      "dưới lỗ bôi trơn.",
      "Removing the packing without removing the actuator is difficult and is not recommended. "
      "Also, do not try to blow out the old packing rings by applying pressure to the lubricator "
      "hole in the bonnet. This can be dangerous and it does not work very well, as many packing "
      "arrangements have about half of the rings below the lubricator hole.")
    FIG(8, F.fig_f8_08())
    FIG(9, F.fig_f8_09())
    P("Cách tốt hơn là tháo cơ cấu chấp hành và nắp van rồi kéo thân ra. Đẩy hoặc gõ các vòng packing "
      "cũ ra từ phía trên nắp. Không dùng thân nút van vì ren có thể bị hỏng.",
      "A better method is to remove the actuator and valve bonnet and pull out the stem. Push or "
      "drive the old packing out the top of the bonnet. Do not use the valve plug stem because the "
      "threads could sustain damage.")
    P("Vệ sinh hộp packing. Kiểm tra thân xem có vết xước hoặc khiếm khuyết nào có thể làm hỏng "
      "packing mới không. Kiểm tra trim và các chi tiết khác khi cần. Sau khi lắp lại, siết bulông "
      "thân và nắp theo trình tự tương tự như đã mô tả cho bích trong Hình 8.2.",
      "Clean the packing box. Inspect the stem for scratches or imperfections that could damage "
      "new packing. Check the trim and other parts as appropriate. After re-assembling, tighten "
      "body and bonnet bolting in a sequence similar to that described for flanges in Figure 8.2.")
    P("Luồn các chi tiết packing mới qua thân theo đúng thứ tự, cẩn thận để ren thân không làm hỏng "
      "vòng packing. Chỉnh packing theo hướng dẫn của nhà sản xuất.",
      "Slide new packing parts over the stem in proper sequence, being careful that the stem "
      "threads do not damage the packing rings. Adjust packing by following the manufacturer's "
      "instructions.")

    H("8.5.4 Vòng đế", "8.5.4 Seat Rings", h3)
    P("Điều kiện vận hành khắc nghiệt có thể làm hỏng bề mặt ép đế của vòng đế khiến van không đóng "
      "kín đầy đủ. Mài ép (lapping) đúng cách bề mặt ép đế sẽ cải thiện độ kín nếu hư hại không "
      "nghiêm trọng. Với hư hại nặng, hãy thay vòng đế.",
      "Severe service conditions can damage the seating surface of the seat ring(s) so that the "
      "valve does not shut off adequately. Properly lapping the seating surfaces will improve "
      "shutoff if damage is not severe. For severe damage, replace the seat ring.")

    H("8.5.4.1 Thay vòng đế", "8.5.4.1 Replacing Seat Rings", h4)
    P("Tuân theo hướng dẫn của nhà sản xuất. Vòng đế có thể được ren vào thân, kẹp (giữ bằng cage "
      "hoặc chi tiết khác), bắt bulông hoặc treo (nối với cage). Với vòng đế ren, dùng dụng cụ kéo "
      "vòng đế. Trước khi cố tháo vòng đế, kiểm tra xem vòng đã được hàn điểm vào thân van chưa. Nếu "
      "có, cắt bỏ mối hàn.",
      "Follow the manufacturer's instructions. Seat rings could be threaded into the body, "
      "clamped (held in by a cage or other part), bolted in or hung (connected to the cage). For "
      "threaded seat rings, use a seat ring puller. Before trying to remove the seat ring(s), check "
      "to see if the ring has been tack-welded to the valve body. If so, cut away the weld.")
    P("Trên thân van hai cổng, một vòng đế nhỏ hơn vòng kia. Với van tác động trực tiếp (đẩy xuống để "
      "đóng), lắp vòng nhỏ hơn vào cổng thân xa nắp van hơn trước khi lắp vòng lớn hơn. Với van tác "
      "động ngược (đẩy xuống để mở), lắp vòng nhỏ hơn vào cổng thân gần nắp van hơn trước khi lắp "
      "vòng lớn hơn.",
      "On double-port bodies, one of the seat rings is smaller than the other. On direct-acting "
      "valves (push-down-to-close action), install the smaller ring in the body port farther from "
      "the bonnet before installing the larger ring. On reverse-acting valves (push-down-to-open "
      "action), install the smaller ring in the body port closer to the bonnet before installing "
      "larger ring.")
    P("Loại bỏ hoàn toàn hợp chất làm kín ren sau khi siết vòng đế ren. Hàn điểm vòng đế ren tại chỗ "
      "để đảm bảo nó không bị lỏng khi cần thiết.",
      "Remove all excess pipe compound after tightening the threaded seat ring. Spot weld a "
      "threaded seat ring in place to ensure that it does not loosen when required.")

    H("8.5.4.2 Liên kết: nút-ty, bi-trục và đĩa-trục",
      "8.5.4.2 Connections: Plug-to-Stem, Ball-to-Shaft, and Disk-to-Shaft", h4)
    P("Liên kết giữa phần tử điều khiển (nút, bi hoặc đĩa) với ty hoặc trục rất quan trọng cho vận "
      "hành an toàn và đúng ý đồ của van. Liên kết này có thể yêu cầu yêu cầu đặc biệt về lắp vừa "
      "hoặc quy trình lắp ráp. Rất quan trọng là tuân theo mọi hướng dẫn lắp ráp của OEM được cung "
      "cấp. Luôn cân nhắc mua nút và ty dưới dạng cụm nút/ty để đảm bảo hiệu năng an toàn và đúng "
      "đắn. Kết nối không đúng có thể dẫn đến điều khiển không ổn định và rò rỉ packing quá mức.",
      "The connection between the controlling element (plug, ball, or disk) and the stem or shaft "
      "is critical for the safe and intended operation of the valve. This may require special "
      "requirements in the fit or assembly procedure. It is very important to follow all the OEM "
      "assembly instructions provided. Always consider purchasing plugs and stems, as a plug/stem "
      "assembly to ensure safe and proper performance. An improper connection can result in "
      "unstable control and excessive packing leakage.")

    H("8.5.5 Giá trị bench set", "8.5.5 Bench Set", h3)
    P("Bench set là giá trị nén ban đầu đặt trên lò xo cơ cấu chấp hành bằng vít chỉnh lò xo. Với van "
      "khí mở (air-to-open), bench set thấp hơn xác định lực có sẵn và áp suất cần để bắt đầu "
      "chuyển động mở van. Với van khí đóng (air-to-close), bench set thấp hơn xác định áp suất cần "
      "để bắt đầu chuyển động đóng van. Lực ép đế được xác định bằng áp suất áp dụng trừ bench set "
      "trừ độ nén lò xo do hành trình (Hình 8.10). Do dung sai lò xo, góc của lò xo có thể có một "
      "chút thay đổi. Bench set khi van đã ép đế đòi hỏi độ chính xác cao nhất. Tham khảo hướng dẫn "
      "của nhà sản xuất để chỉnh lò xo.",
      "Bench set is initial compression placed on the actuator spring with a spring adjuster. For "
      "air-to-open valves, the lower bench set determines the amount of force available and the "
      "pressure required to begin valve-opening travel. For air-to-close valves, the lower bench "
      "set determines the pressure required to begin valve-closing travel. Seating force is "
      "determined by pressure applied minus bench set minus spring compression due to travel "
      "(Figure 8.10). Because of spring tolerances, there might be some variation in the spring "
      "angle. The bench set, when the valve is seated, requires the greatest accuracy. Refer to "
      "manufacturer's instructions for adjusting the spring.")
    FIG(10, F.fig_f8_10())

    H("8.5.6 Hành trình van", "8.5.6 Valve Travel", h3)
    P("Hành trình đúng của van rất cần thiết để đạt được hiệu năng điều khiển đúng. Hành trình "
      "không đủ có thể làm van không đạt được lưu lượng thiết kế. Hành trình vượt mức có thể làm "
      "giảm tải ép đế từ cơ cấu chấp hành, ảnh hưởng đến độ kín và làm hỏng trim. Một vấn đề khác "
      "do hành trình vượt mức gây ra là nút có thể chạm đáy nắp van làm ty bị tuột khỏi nút. Hành "
      "trình của van thân trượt quan trọng hơn hành trình của van quay. Vì vậy, cần chú ý tỉ mỉ "
      "hơn khi đặt hành trình cho van thân trượt. Tham khảo sổ hướng dẫn của nhà sản xuất để biết "
      "quy trình đặt hành trình đúng.",
      "Proper valve travel is essential to achieving proper control valve performance. Insufficient "
      "travel can cause the valve not to achieve the designed flow rate. Over travel can reduce "
      "the seat load from the actuator affecting shutoff and cause damage to the trim. Another "
      "problem attributed to over travel is that the plug can contact the bottom of the bonnet "
      "causing the stem to be pulled out of the plug. Sliding-stem valve travel is more critical "
      "than rotary valve travel. Therefore, greater attention to detail is crucial when setting "
      "sliding-stem valve travel. Refer to the manufacturers' instruction manual for the procedure "
      "to properly set valve travel.")

    # ------------------------------------------------------------ 8.6
    H("8.6 Quy trình lập kế hoạch dừng máy, đại tu hoặc mất máy (STO)",
      "8.6 Shutdown, Turnaround, Outage Planning Process")
    P("Hầu hết các đơn vị quá trình công nghiệp đều thực hiện bảo trì dừng máy, đại tu hoặc mất máy "
      "(STO). Các đợt này có thể được lên kế hoạch hoặc không. Nếu được lên kế hoạch, tùy theo loại "
      "ngành và đơn vị quá trình, hoạt động bảo trì định kỳ trung bình có thể diễn ra ba đến năm "
      "năm một lần để bảo trì và nâng cấp tài sản, thiết bị của nhà máy. Cách lập dòng thời gian, "
      "xác định và thực hiện phạm vi công việc thay đổi theo ngành, vì vậy việc giảm thiểu thời "
      "gian và chuyên môn cần thiết luôn then chốt để STO đạt ngân sách và tiến độ. Mỗi ngày đơn "
      "vị quá trình ngừng vì STO là nhà máy không sản xuất sản phẩm, tức là không tạo ra lợi nhuận.",
      "Most industry process units perform a maintenance shutdown, turnaround, or an outage (STO). "
      "They can either be planned or unplanned. If they are planned, dependent on type of industry "
      "and process units, they can have scheduled maintenance activities every three to five years "
      "on average to maintain and upgrade plant assets and equipment. How the timeline is planned "
      "out and the scope is defined and executed varies depending on the industry, so minimizing "
      "the amount of time and expertise needed is always critical to the success of the STO to meet "
      "budgets and deadlines. Every day a process unit is down for an STO, the specific plant "
      "itself is not making product, which in turn means it is not making profits.")
    P("Bạn có thể gặp khó khăn trong việc thực hiện STO thành công do giới hạn ngân sách, thiếu kỹ "
      "năng và nguồn lực cần thiết, cũng như thiếu dữ liệu và diễn giải về tình trạng tài sản. Bạn "
      "cần một đối tác có thể giúp xác định phạm vi công việc cần thiết, đồng thời lập và thực hiện "
      "chương trình đáp ứng yêu cầu ngân sách và đưa hệ thống sản xuất trở lại vận hành trong thời "
      "gian ngắn nhất.",
      "You may struggle to execute successful STOs due to budget constraints, a lack of necessary "
      "skills and resources, and insufficient asset health data and interpretation. You need a "
      "partner who can help define the necessary scope of work, while planning and executing a "
      "program that meets your budget requirements and gets production systems back up and running "
      "in the shortest possible time.")
    P("Các ngành cần làm việc với nhà cung cấp từ rất sớm trước STO; tùy ngành, có thể nhìn trước từ "
      "12 đến 60 tháng để lập kế hoạch, xác định phạm vi rồi thực hiện đúng cách. Hãy nhớ năm chữ "
      "P: Lập kế hoạch đúng đắn ngăn ngừa hiệu quả kém (Proper Planning Prevents Poor Performance).",
      "Industries need to work with vendors well in advance of the STO, depending on industry you "
      "can look out from 12 to 60 months in advance of execution to properly plan, scope, and then "
      "execute. Remember the Five P's: Proper Planning Prevents Poor Performance.")

    H("8.6.1 Mời nhà cung cấp van điều khiển tham gia",
      "8.6.1 Bring in the Control Valve Vendor", h3)
    P("Hầu hết nhà cung cấp và đơn vị dịch vụ lớn về van điều khiển đều có kinh nghiệm với các đợt "
      "STO cho nhiều người dùng và ngành khác nhau. Việc tham gia của các đội ngũ giàu kinh nghiệm này "
      "giúp làm rõ phạm vi van điều khiển và tiến độ sửa chữa, khám phá cơ hội giảm chi phí, và đưa "
      "van điều khiển về trạng thái OEM nhờ dùng phụ tùng được chứng nhận lắp đặt theo quy trình "
      "nhà máy do kỹ thuật viên được đào tạo thực hiện.",
      "Most major control valve vendors and service providers have experience with STO engagements "
      "across different end-users and industries. Engaging these experienced teams can help to "
      "increase the clarity on the control valve scope and timeline for repairs, discover "
      "opportunities to reduce cost, and bring control valves back to an OEM state by using "
      "certified parts installed with factory procedures performed by trained factory technicians.")
    P("Các cuộc thảo luận có thể bắt đầu sớm nhất là 24 đến 60 tháng trước STO dự kiến để xác định "
      "phạm vi và đơn vị được lên lịch bảo trì. Khi hợp tác với Emerson, họ dùng quy trình STO bảy "
      "bước đã được chứng minh mang lại kết quả nhất quán.",
      "Discussions can start as early as 24 to 60 months before a planned STO to define the scope "
      "and unit scheduled for maintenance. When you partner with Emerson, they use a 7-step proven "
      "STO process that leads to consistent outcomes.")

    H("8.6.2 Bước lập kế hoạch vận hành", "8.6.2 Operational Planning", h3)
    P("Bước lập kế hoạch vận hành diễn ra khoảng 24 đến 60 tháng trước khi thực hiện. Các dự án "
      "tương lai được lên kế hoạch ở mức tổng quát cùng các bên liên quan chính cho một STO thành "
      "công, đúng hạn và an toàn. Kênh bán hàng và trưởng dịch vụ bắt đầu làm việc với khách hàng "
      "và đội ngũ của họ từ 24 đến 60 tháng trước khi thực hiện. Phát triển phạm vi sơ bộ và xếp "
      "hạng mức quan trọng, tối ưu sản xuất/lập lịch, kế hoạch tích hợp CAPEX và các chỉ số hiệu "
      "suất chính được xác định.",
      "The operational planning step is about 24 to 60 months prior to execution. Future projects "
      "are planned at a high level with key stakeholders for a future successful STO, which is on "
      "time and safe. The sales channel and service leader start engaging with customers and their "
      "teams 24 to 60 months prior to execution. Preliminary scope development and criticality "
      "ranking, production / scheduling optimization, CAPEX integration plan and key performance "
      "indicators are identified.")
    P("Các bên liên quan chính gồm Quản lý tài khoản Kênh bán hàng Emerson, Quản lý dự án STO, Trưởng "
      "dịch vụ, cùng Quản lý nhà máy của Khách hàng, Quản lý vận hành, Quản lý bảo trì, Quản lý đại "
      "tu, và các đội Kỹ thuật, Độ tin cậy và HSE.",
      "The key stakeholders should be Emerson Sales Channel Account Manager(s), STO Project "
      "Manager, Service Lead, along with the Customer Plant Manager, Operations Manager, "
      "Maintenance Manager, Turnaround Manager, Engineering, Reliability, and HSE teams.")

    H("8.6.3 Bước thống nhất", "8.6.3 Alignment Step", h3)
    P("Bước thống nhất diễn ra khoảng 12 đến 24 tháng trước STO. Nội dung gồm thống nhất các sáng "
      "kiến chính và mục tiêu dự án, lập danh sách công việc theo thứ tự ưu tiên, chiến lược kéo "
      "sản phẩm và xác định ngày chốt phạm vi cùng các bên liên quan. Định nghĩa phạm vi ban đầu "
      "được thiết lập, mốc tiến độ và ngân sách sơ bộ được xác định. Mục tiêu dự án cũng được xác "
      "định, danh sách công việc được sắp ưu tiên và ngày chốt phạm vi được ấn định. Kết quả là đội "
      "ngũ có phạm vi ban đầu dựa trên các tài sản được nhắm sửa chữa, thay thế hoặc nâng cấp. Nếu "
      "có hợp đồng Giám sát tình trạng van, đây là thời điểm lý tưởng để xem xét phân tích xu hướng "
      "nhằm xác định van nào cần hoặc không cần xử lý. Cuối cùng, trong kế hoạch nên có thảo luận "
      "về việc đưa kỹ sư của nhà cung cấp vào quy trình khởi động lại nhà máy.",
      "The Alignment Step happens about 12 to 24 months prior to the STO. Alignment on key "
      "initiatives, project goals, develop prioritized worklist, product pull-through strategy, "
      "and determine scope freeze date stakeholders. The initial scope definition is generated, "
      "preliminary schedule milestones and budgets are defined. The project goals and objectives "
      "are also defined, work lists are prioritized, and a scope freeze date determined. As an "
      "outcome, the team should have an initial scope defined based on assets targeted for repair, "
      "replacement, or upgrade. If a Valve Condition Monitoring contract is in place, this is the "
      "perfect time to review trending analysis to define valves that do or do not need attention. "
      "Lastly, as part of the plan, a discussion should be in place to discuss a vendor engineer(s) "
      "as part of the plant restart process.")
    P("Các bên liên quan chính gồm Quản lý tài khoản Kênh bán hàng Emerson, Quản lý dự án STO, "
      "Trưởng dịch vụ, cùng Quản lý đại tu của Khách hàng, Quản lý kỹ thuật, Giám sát đơn vị và "
      "Quản lý độ tin cậy.",
      "The key stakeholders should be Emerson Sales Channel Account Manager(s), STO Project "
      "Manager, Service Lead, along with the Customer Turnaround Manager, Engineering Manager, "
      "Unit Supervisor, and Reliability Manager.")

    H("8.6.4 Bước xác định phạm vi công việc", "8.6.4 Work Scope Definition Step", h3)
    P("Bước xác định phạm vi công việc diễn ra khoảng 12 đến 18 tháng trước STO. Cuộc họp khởi động "
      "với khách hàng được tổ chức cùng nhân viên bán hàng và dịch vụ để xác định rõ hơn danh sách "
      "tài sản đưa vào phạm vi. Công cụ số và chẩn đoán được dùng để xác nhận đề xuất phạm vi STO "
      "cuối cùng. Một cuộc đi khảo sát số xác định tài sản, thu thập mọi dữ liệu liên quan và kiểm "
      "tra tình trạng thực tế, sau đó báo cáo tóm tắt được gửi cho khách hàng. Các công cụ chẩn "
      "đoán (AMS, ValveLink, FlowScanner) được dùng để xác nhận tài sản có thể sửa tại chỗ bằng "
      "hiệu chuẩn hoặc chỉnh trước STO, hay cần kiểm tra thêm và phải đưa vào phạm vi chung. Báo "
      "cáo đánh giá chẩn đoán này cần ở định dạng số để dữ liệu thu thập được tải lên phần mềm "
      "CMMS của khách hàng. Có thể cần xem xét ứng dụng công nghiệp nếu một van cụ thể cần sửa hoặc "
      "thay trong mỗi lần bảo trì.",
      "The Work Scope Definition Step happens about 12 to 18 months prior to the STO. A customer "
      "kick-off meeting is held with sales and service personnel to further define a list of "
      "assets to be identified for the scope. Digital and diagnostic tools are used to validate "
      "the final STO scope proposal. A digital walkdown identifies assets to capture all relevant "
      "data and physical health checks and then given to the customer in a walkdown summary. "
      "Diagnostic tools (AMS, ValveLink, FlowScanner) are utilized to validate if the asset can be "
      "repaired in-line with a calibration or adjustment prior to the STO, or if the asset needs "
      "further inspection and it does need to be included in the overall scope. This diagnostic "
      "evaluation report needs to be done in a digital format so the data collected can be "
      "uploaded to the customer CMMS software. An industry application may need to be reviewed if "
      "a certain valve needs to be repaired or replaced during each maintenance event.")
    P("Do đó, phạm vi STO chỉ được xác định sau khi mọi hạng mục đã được đi khảo sát, chẩn đoán đã "
      "thực hiện trên tất cả hoặc các van quan trọng được nhắm, và kế hoạch đã được thỏa thuận đầy "
      "đủ với khách hàng trước ngày chốt phạm vi. Chỉ khi đó đề xuất mới được lập ra để đảm bảo "
      "mọi van cần sửa, phụ tùng cần thay hoặc hạng mục nâng cấp đều có sẵn trước khi thực hiện.",
      "So, the scope of the STO is determined after all items have been walked down, diagnostics "
      "have taken place on all or targeted critical valves, and a plan is fully agreed upon with "
      "the customer ahead of the scope or freeze date. Only then can a proposal be generated to "
      "make sure all valves to be repaired, parts to be replaced, or upgraded items can be on-hand "
      "prior to the execution.")
    P("Các bên liên quan chính gồm Quản lý tài khoản Kênh bán hàng Emerson, Quản lý dự án STO, "
      "Trưởng dịch vụ, cùng Quản lý đại tu của Khách hàng, Quản lý kỹ thuật, Chủ ngân sách/Bộ phận "
      "mua hàng, Giám sát đơn vị và Quản lý độ tin cậy.",
      "The key stakeholders should be Emerson Sales Channel Account Manager(s), STO Project "
      "Manager, Service Lead, along with the Customer Turnaround Manager, Engineering Manager, "
      "Budget Owner / Procurement, Unit Supervisor, and Reliability Manager.")

    H("8.6.5 Bước lập kế hoạch chi tiết", "8.6.5 Detailed Planning Step", h3)
    P("Bước lập kế hoạch chi tiết diễn ra khoảng 4 đến 6 tháng trước STO. Khách hàng đã đồng ý đề "
      "xuất và phạm vi đã được xác định. Thời gian đã được lên kế hoạch và hoạch định năng lực bắt "
      "đầu. Quản lý dự án STO của Emerson cùng đội bán hàng và dịch vụ lập kế hoạch mua phụ tùng dự "
      "phòng đề xuất, đồng thời xem xét các đơn vị được nhắm sửa chữa, nâng cấp hoặc thay thế.",
      "The Detailed Planning Step occurs about 4 to 6 months prior to the STO. The customer has "
      "agreed to the proposal and the scope has been determined. Timing has now been planned and "
      "the capacity planning has begun. The Emerson STO Project Manager, along the sales and "
      "service team, make plans to acquire recommended spare parts and also look at what units "
      "have been targeted for repairs, upgrades, or replacements.")
    P("Phụ tùng van quan trọng có thời gian chờ dài cần được đặt hàng cùng với các khoảng dự trữ sẵn. "
      "Nhu cầu nhân lực cũng cần được lên kế hoạch và phân lịch, cũng như quyết định STO được thực "
      "hiện tại công trường khách hàng hay tại cơ sở sửa chữa (depot). Nếu làm tại công trường, "
      "cần đặt trước Trung tâm dịch vụ di động và hoàn tất các phê duyệt cuối cùng từ khách hàng. "
      "Nếu làm tại công trường, Quản lý ES&amp;H cần đảm bảo có kế hoạch đào tạo an toàn và thu thập "
      "bảng dữ liệu an toàn vật liệu (MSDS) phù hợp với quá trình. Cần giải quyết danh mục kiểm tra "
      "gồm an toàn, phụ tùng, nhân lực và việc cấp thẻ nhận diện cho người làm việc hiện trường. "
      "Cuối cùng, cần lập gói công việc gồm thẻ seri, tài liệu MSDS và phạm vi công việc theo từng "
      "Tag Number của van.",
      "Critical valve spares with long lead times need to be put on order along with stocked "
      "items. The need for labor should be planned and scheduled as well as if the execution of "
      "the STO will be done at the customer site or in a repair facility (depot). If the work is "
      "to be done at the customer site, Mobile Service Center(s) need to be booked and other final "
      "approvals from the customer should be done. If work is to be done at the customer site, the "
      "ES&amp;H Manager should make sure there is safety training planned and MSDS sheets acquired "
      "based on the process. A checklist of items should be addressed such as safety, parts, "
      "labor, and making sure badges are acquired for the names of the field workers. Finally, "
      "work packages that include serial cards, MSDS documents, and scope of what is to be done to "
      "the valve by Tag Number should be generated.")
    P("Các bên liên quan chính gồm Quản lý tài khoản Kênh bán hàng Emerson, Quản lý dự án STO, "
      "Trưởng dịch vụ, cùng Quản lý đại tu và Người lập kế hoạch của Khách hàng, Kỹ sư thiết bị đo, "
      "Giám sát đơn vị và Quản lý độ tin cậy.",
      "The key stakeholders should be Emerson Sales Channel Account Manager(s), STO Project "
      "Manager, Service Lead, along with the Customer Turnaround Manager and Planner, "
      "Instrumentation Engineers, Unit Supervisor, and Reliability Manager.")

    H("8.6.6 Bước lập kế hoạch trước STO", "8.6.6 Pre-STO Planning Step", h3)
    P("Bước lập kế hoạch trước STO diễn ra khoảng 2 đến 6 tháng trước STO. Đến lúc này, mọi nguồn "
      "lực phải được thống nhất cho công tác thực hiện. Bước này chuẩn bị cho việc thực hiện và "
      "giảm rủi ro, gồm mọi kế hoạch truyền thông, kiểm tra an toàn và đào tạo, quy trình cùng các "
      "bước ký duyệt để bắt đầu STO. Việc thường xuyên đồng bộ với khách hàng qua Quản lý dự án, "
      "thậm chí qua cả Kênh bán hàng, là rất có giá trị. Có nhiều trường hợp phạm vi dần mở rộng "
      "ngay cả trước khi sự kiện bắt đầu — họ có thể thêm van hoặc tài sản vào phạm vi. Đôi khi, "
      "tùy tiến độ và ngân sách, họ cũng có thể giảm nội dung. Hãy sẵn sàng tăng hoặc giảm năng "
      "lực tùy theo cuộc họp trước STO cuối cùng với tất cả các bên. Nhà cung cấp tốt sẽ đảm bảo "
      "mọi phụ tùng, nâng cấp và sản phẩm được đóng túi, đóng hộp hoặc gắn nhãn theo số ID của van, "
      "ví dụ TV144, 4” Fisher ET/667/DVC6200, S/N 987654321.",
      "The Pre-STO Planning Step occurs about 2 to 6 months prior to the STO. By now, all resources "
      "should be aligned for the execution. This step prepares for execution and risk reduction "
      "and all communication plans, safety checks and training, procedures, and signoffs to "
      "commence the STO. It's of value to constantly be in sync with the customer through the "
      "Project Manager and even the Sales Channel. There are many times when scope creep comes "
      "into play even before the event begins. They may be adding valves or assets to the scope. "
      "Sometimes, depending on schedule and budget, they may reduce the content as well. Be "
      "prepared to add capacity or reduce capacity depending on the final pre-STO meeting with all "
      "parties. A good vendor will make sure all parts, upgrades, and products are bagged, boxed or "
      "tagged by the valve ID number. I.E., TV144, 4” Fisher ET/667/DVC6200, S/N 987654321.")
    P("Các bên liên quan chính gồm Quản lý tài khoản Kênh bán hàng Emerson, Quản lý dự án STO, "
      "Trưởng dịch vụ, cùng Quản lý đại tu và Người lập kế hoạch của Khách hàng, Chủ ngân "
      "sách/Bộ phận mua hàng, nhiều kỹ sư thuộc các chuyên ngành khác nhau, Quản lý bảo trì và "
      "Quản lý HSE.",
      "The key stakeholders should be Emerson Sales Channel Account Manager(s), STO Project "
      "Manager, Service Lead, along with the Customer Turnaround Manager and Planner, Budget Owner "
      "/ Procurement, various Engineers from many disciplines, Maintenance Manager, and HSE "
      "Manager.")

    H("8.6.7 Bước thực hiện STO", "8.6.7 STO Execution Step", h3)
    P("Sau khi đơn vị được dừng an toàn, vệ sinh và đảm bảo an toàn để tiếp cận, công việc có thể "
      "bắt đầu tại chỗ, hoặc đây là thời điểm van bắt đầu được tháo khỏi vận hành và chuẩn bị đưa "
      "đi sửa chữa. An toàn cũng là yếu tố then chốt trong giai đoạn này vì nhà máy đã mất điện "
      "có thể rất nguy hiểm. Các cuộc họp giao tiếp hàng ngày được tổ chức trực tiếp hoặc qua Teams, "
      "WebEx, v.v., vì truyền thông tổng thể là chìa khóa thành công. Báo cáo cập nhật được cung "
      "cấp về tiến độ, những việc làm tốt và các vấn đề phát sinh.",
      "Once the unit is brought down safely, cleaned, and safe to approach, the work can begin "
      "either on-site or this is the point when valves start to be removed from service and ready "
      "to be picked up for repair. Safety is also key during this stage because a de-energized "
      "plant can be dangerous. Daily communication meetings are held in-person or via Teams, "
      "WebEx, etc. as overall communications are key to success. Updates are provided on progress "
      "report status, what's going well, and what issues are being seen.")
    P("Cập nhật cũng được cung cấp cho các hạng mục không nằm trong phạm vi nhưng được nhìn nhận "
      "và đưa vào danh sách tồn đọng (punch list) để báo cho khách hàng biết những việc có thể cần "
      "xử lý ngay hoặc có thể chờ đến lần bảo trì sau.",
      "Updates are also provided on items that were not part of the scope but are viewed and added "
      "to a punch list to update the customer on non-scope items that may need attention now or "
      "can wait until the next maintenance event.")
    P("Nhà cung cấp tốt như Emerson sẽ ghi chép tài sản đã làm việc thông qua Báo cáo sửa chữa số. "
      "Tài liệu có thể được tải lên phần mềm CMMS để cập nhật mới nhất cho Tag Number nằm trong hệ "
      "thống quản lý bảo trì của khách hàng. Một lần nữa, có thể có phạm vi dần mở rộng nếu các tài "
      "sản bổ sung được cho là có thể gây dừng máy bất ngờ nếu không xử lý ngay. Lệnh thay đổi được "
      "lập với chi phí bổ sung và trình khách hàng phê duyệt. Có thể có một nhân viên liên lạc của "
      "khách hàng ký xác nhận sản phẩm đã sửa hoặc mới, tạo hồ sơ về an toàn, chất lượng và chi phí. "
      "Các hạng mục đã sửa được trả lại và lắp về đường ống sau khi hoàn tất sửa chữa, được kiểm "
      "kê và ghi nhận là đã về công trường. Đào tạo công nghệ mới cho nhân viên hiện trường được "
      "ghi nhận tại đây như việc bắt buộc phải làm khi nhà máy đã vận hành ổn định. Cuối cùng, đội "
      "chạy thử của nhà cung cấp nên ở trạng thái sẵn sàng cho việc khởi động lại hoặc chạy lại nhà "
      "máy.",
      "A good vendor, like Emerson, will document the asset worked on through a digital Repair "
      "Report. The document can be uploaded to the CMMS software so the latest update on the Tag "
      "Number is in the customer maintenance management system. Again, there may be some scope "
      "creep if additional assets are deemed to potentially cause an unexpected shutdown if not "
      "properly addressed now. Change orders are put together with extra costs and vetted through "
      "the customer. There may be a customer liasion who signs off on repaired or new products, so "
      "they have a paper trail on safety, quality, and cost. Items that are repaired and returned "
      "to be put back in line after the repairs are complete, checked in, and documented that they "
      "are back at the plant site. Training on new technology for site personnel would be "
      "documented here as a must-do when the plant is up and running. Lastly, a vendor "
      "commissioning team should be put on standby for plant restart / recommissioning.")
    P("Các bên liên quan chính gồm Quản lý tài khoản Kênh bán hàng Emerson, Quản lý dự án STO, "
      "Trưởng dịch vụ, cùng Người lập kế hoạch đại tu của Khách hàng, Kỹ sư, Quản lý bảo trì, Kiểm "
      "soát chất lượng, Quản lý HSE và đội nhà máy cho công tác chạy thử.",
      "The key stakeholders should be Emerson Sales Channel Account Manager(s), STO Project "
      "Manager, Service Lead, along with the Customer Turnaround Planner, Engineers, Maintenance "
      "Managers, Quality Control, HSE Manager, and Plant teams for commissioning.")

    H("8.6.8 Bước đánh giá sau STO", "8.6.8 Post STO Evaluation Step", h3)
    P("Bước đánh giá sau STO diễn ra 2 đến 4 tháng sau khi nhà máy khởi động lại, khi các đơn vị "
      "quá trình đã trở lại vận hành và nhà máy đã sản xuất sản phẩm. Việc nắm bắt hiệu quả thực "
      "hiện đợt dừng máy, đo lường mức độ hiệu quả của chiến lược, đối chiếu (benchmark) cho so "
      "sánh bảo trì và độ tin cậy, cũng như cập nhật tài liệu là then chốt cho sự thành công của "
      "các sự kiện sau và vận hành nhà máy giữa các lần. Nếu có vượt tiến độ hay chi phí, cần xác "
      "định và hiểu rõ nguồn gốc của những lần vượt đó. Thông tin này được đưa vào tài liệu bài học "
      "kinh nghiệm. Cuối cùng, một báo cáo cho toàn bộ đợt dừng máy, từ lập lịch đến khâu kết thúc, "
      "được lập ra. Báo cáo nên chứa mọi khía cạnh của đợt dừng và được dùng làm đầu vào để bắt đầu "
      "lập kế hoạch cho sự kiện tiếp theo.",
      "The Post STO Evaluation Step occurs 2 to 4 months post plant restart after the process "
      "units are back on-line and the plant is producing product. Capturing the performance of the "
      "outage execution, measuring the effectiveness of the strategy, benchmarking for "
      "maintenance and reliability comparisons, and updating documentation are crucial to the "
      "success of future events and plant operations between them. If overruns occurred, the "
      "source of those overruns will need to be determined and understood. This will be fed into "
      "the lessons learned documentation. Finally, a report for the entire outage from scheduling "
      "to the close-out portion of the outage will be prepared. The report should contain every "
      "aspect of the outage and is used as an input to start planning the next event.")
    P("Các cuộc xem xét này nên là xem xét hai chiều: một từ nhà thầu tới hiện trường và một từ hiện "
      "trường tới nhà thầu. Về phía nhà thầu, họ phải họp nội bộ trước và một quy trình KPI chính "
      "thức nên đã được thống nhất giữa khách hàng và nhà thầu ở giai đoạn lập kế hoạch để biết mỗi "
      "bên đạt được gì.",
      "These reviews should be a two-way review. One from the contractors to the site and one from "
      "the site to contractors. From the contractor point of view, they must meet internally first "
      "and a formal KPI process should have been decided at the planning stage between customer "
      "and contractor to know how each fared.")
    P("Báo cáo và tài liệu về công việc đã thực hiện mang lại lợi ích cho khách hàng. Đây cũng là "
      "lúc đưa ra khuyến nghị cho vận hành nhà máy đang diễn ra cũng như khuyến nghị hành động và "
      "kế hoạch cho đợt dừng máy tiếp theo. Mục tiêu là ghi nhận thành công và duy trì vận hành "
      "theo mục tiêu của khách hàng. Tài liệu xem xét sau dừng máy nên là đánh giá toàn diện, ban "
      "đầu từ nhà thầu tới khách hàng. Một số kết quả xem xét sau dừng máy mà nhà thầu gửi khách "
      "hàng nên bao gồm, nhưng không giới hạn ở:",
      "The report and documentation of the work performed is a benefit to the customer. It is also "
      "the time when recommendations for ongoing plant operations are made as well as "
      "recommendations for actions and plans for the next outage. The goal is to document success "
      "and maintain operations per customer objectives. The post outage review documentation "
      "should be an all-encompassing review from the contractor to the customer initially. Some of "
      "the post outage review deliverables from a contractor to the customer should include, but "
      "limited to:")
    B(["Chất lượng sản phẩm và dịch vụ",
       "Các hạng mục thương mại",
       "Truyền thông trước, trong và sau sự kiện",
       "Xem xét an toàn — mọi mối nguy hoặc vấn đề tại công trường khách hàng",
       "Punch list STO — các hạng mục đã thấy hoặc không nằm trong phạm vi ban đầu cần xử lý "
       "trong sự kiện tiếp theo",
       "Báo cáo đi khảo sát các tài sản trong phạm vi",
       "Báo cáo chẩn đoán (trước và sau) của van để cho thấy vấn đề ban đầu và tình trạng vận hành "
       "hiện nay sau sửa chữa hoặc nâng cấp (kiểm tra chất lượng)",
       "Báo cáo sửa chữa các tài sản đã sửa hoặc nâng cấp",
       "Xem xét KPI về chất lượng, đúng tiến độ và đúng ngân sách",
       "Chi phí vượt so với lịch và phạm vi báo giá ban đầu; có xác nhận của khách hàng về việc "
       "cho phép tiến hành để mọi bên cùng kiểm soát",
       "Danh sách sản phẩm mới và kế hoạch đào tạo nhân viên nhà máy (ví dụ học qua bữa trưa)",
       "Danh sách phụ tùng dự phòng cập nhật cho tài sản quan trọng",
       "Danh sách số seri đã cập nhật phản ánh sửa chữa hoặc nâng cấp",
       "Bài học kinh nghiệm: đã thấy phạm vi gì; có thể cải thiện gì về lập kế hoạch, nhân sự, vấn "
       "đề phạm vi dần mở rộng; cần gì và cải thiện thế nào cho lần dừng máy tiếp theo"],
      ["Product and service quality",
       "Commercial items",
       "Communications before, during, and after the event",
       "Safety review - any hazards or issues at the customer site",
       "STO punch list - items that seen, or not part of the initial scope should be attended to "
       "during the next event",
       "Walkdown reports on the assets that were in scope",
       "Diagnostic reports (before and after) of valves to show initial issues and how they are "
       "operating now after a repair or upgrade (a quality check)",
       "Repair reports on assets that were repaired or upgraded.",
       "KPI review on quality, on-schedule, and on budget.",
       "Cost overruns from initial schedule scope and quote. Backup with customer authorization "
       "to proceed keeps everyone in check.",
       "List of new products and plan to train plant personnel (lunch and learn as an example).",
       "List of updated recommended spares for critical assets.",
       "List of serial numbers that have been updated to reflect repair or upgrades.",
       "Lessons learned: what scope was seen; what can be improved regarding planning, personnel, "
       "scope creep issues; and what's needed and how to improve on the next outage."])
    P("Đây phải là cuộc thảo luận hai chiều giữa nhà thầu và khách hàng.",
      "This should be a two-way discussion between contractor and customer")
    P("Các bên liên quan chính gồm Quản lý tài khoản Kênh bán hàng Emerson, Quản lý dự án STO, "
      "Trưởng dịch vụ, cùng Quản lý đại tu và Người lập kế hoạch của Khách hàng, Chủ ngân "
      "sách/Bộ phận mua hàng, Quản lý bảo trì, Kỹ sư độ tin cậy và Quản lý HSE.",
      "The key stakeholders should be Emerson Sales Channel Account Manager(s), STO Project "
      "Manager, Service Lead, along with Customer Turnaround Manager and Planner, Budget Owner / "
      "Procurement, Maintenance Manager, Reliability Engineers, and HSE Manager.")

    H("8.6.9 Kết luận", "8.6.9 Conclusion", h3)
    P("STO là sự kiện rất tốn kém nhưng có thể kiểm soát tốt nếu được lập kế hoạch theo đúng năm "
      "chữ P: Lập kế hoạch đúng đắn ngăn ngừa hiệu quả kém. Để giúp khách hàng hiểu van và tài sản "
      "nào cần sửa chữa, hãy dùng bộ định vị thông minh, hợp đồng Giám sát tình trạng van và chẩn "
      "đoán. Việc xác định một van điều khiển có thực sự cần tháo ra trong STO hay không có thể "
      "giảm đáng kể thời gian và chi phí STO. Nhận diện các van điều khiển còn tốt giúp giảm số "
      "van cần bảo dưỡng. Nhà cung cấp van điều khiển như Emerson có thể hỗ trợ những nhu cầu này "
      "và các nhu cầu STO khác, gồm xác định phạm vi van điều khiển, xem xét và thử nghiệm van điều "
      "khiển, và sửa van tại chỗ. Những công nghệ và dịch vụ này không chỉ rút ngắn thời gian và "
      "giảm chi phí STO mà còn giảm rất nhiều khả năng phát sinh sự cố ngoài kế hoạch.",
      "STOs are very costly events that can be properly controlled if planned in accordance with "
      "the Five ‘Ps’: Proper Planning Prevents Poor Performance. To help customers understand which "
      "valves and assets need to be repaired, use smart positioners, Valve Condition Monitoring "
      "contracts, and diagnostics. Determining if a control valve really needs to be pulled during "
      "an STO can substaintially reduce STO time and costs. Identifying healthy control valves can "
      "reduce the number of valves that need servicing. A control valve vendor, like Emerson, can "
      "assist with these and other STO needs, including defining the control valve scope, reviewing "
      "and testing control valves, and onsite valve repair. These technologies and services not "
      "only cut STO time and cost, but also greatly reduce the possibility of unplanned problems "
      "and issues.")
    FIG(11, F.fig_f8_11())

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 8 chiếm tr. 176–191 của bản in (16 trang) trong Emerson, Control Valve Handbook, ấn "
      "bản 6 (2020). Nội dung gồm sáu mục 8.1–8.6: lưu trữ và bảo vệ, kỹ thuật lắp đặt, bảo trì "
      "van điều khiển, phụ tùng dịch vụ và sửa chữa, bảo trì cơ cấu chấp hành, và quy trình lập "
      "kế hoạch STO. Mười một hình được vẽ lại dạng vector và đặt theo thứ tự số tại vị trí văn "
      "bản hợp lý.",
      "Chapter 8 occupies printed pp. 176-191 (16 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains six sections, 8.1-8.6: storage and protection, installation "
      "techniques, control valve maintenance, service and repair parts, actuator maintenance, and "
      "the STO planning process. The eleven numbered figures are redrawn as vectors and placed in "
      "numbered order at their logical prose points.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 Emerson "
      "Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 Emerson "
      "Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
