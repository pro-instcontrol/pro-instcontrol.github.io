# -*- coding: utf-8 -*-
"""Book 7c, Chapter 3 - Valve and Actuator Types (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 54-81.
This is a terminology and catalogue chapter. It surveys valve body styles,
rotary valves, end connections and bonnets, packing and environmental
compliance, trim characterization and actuators. All fifty-two numbered
source figures (3.1-3.52) are redrawn as vector schematics in `cvh6fig.py`
and placed at the points where the source captions occur.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import fig, h2, h3, h4, lead, note, p, table, ul
import cvh6fig as F

PAGES_SRC = 28          # source printed pp. 54-81 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Valve and Actuator Types"
TITLE_VI = "Các loại van và cơ cấu chấp hành"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> control valve style — kiểu van điều khiển · "
            "closure member — phần tử đóng · globe valve — van cầu · angle valve — van góc · "
            "single-ported — một cổng · double-ported — hai cổng · cage-style trim — trim dạng lồng · "
            "balanced plug — nút cân bằng · three-way valve — van ba chiều · sanitary valve — van vệ sinh · "
            "butterfly valve — van bướm · segmented ball valve — van bi đoạn · eccentric plug — nút lệch tâm · "
            "full-port ball valve — van bi cổng đầy · multi-port flow selector — van chọn dòng đa cổng · "
            "end connection — đầu nối · bolted flange — bích bắt bulông · welded end — đầu hàn · "
            "bonnet — nắp van · extension bonnet — nắp kéo dài · bellows seal — kín bằng ống mềm · "
            "packing — vật liệu đệm / gioăng đệm · fugitive emission — khí thải bay hơi · "
            "LDAR — chương trình phát hiện và sửa rò rỉ · packing follower — bích ép đệm · "
            "flow characteristic — đặc tính dòng · inherent characteristic — đặc tính vốn có · "
            "quick-opening — mở nhanh · equal-percentage — phần trăm bằng · linear — tuyến tính · "
            "plug guiding — dẫn hướng nút van · actuator — cơ cấu chấp hành · diaphragm actuator — cơ cấu màng · "
            "piston actuator — cơ cấu piston · rack-and-pinion — răng cưa - bánh răng · "
            "electric actuator — cơ cấu chấp hành điện · fail-open / fail-closed — an toàn khi mất khí: mở / đóng")
    return (
        "<b>Key terms in this chapter.</b> control valve style · closure member · globe valve · "
        "angle valve · single-ported · double-ported · cage-style trim · balanced plug · "
        "three-way valve · sanitary valve · butterfly valve · segmented ball valve · eccentric plug · "
        "full-port ball valve · multi-port flow selector · end connection · bolted flange · "
        "welded end · bonnet · extension bonnet · bellows seal · packing · fugitive emission · "
        "LDAR · packing follower · flow characteristic · inherent characteristic · quick-opening · "
        "equal-percentage · linear · plug guiding · actuator · diaphragm actuator · piston actuator · "
        "rack-and-pinion · electric actuator · fail-open / fail-closed")


def note(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> Nguyên bản có một số điểm đặc thù: mục 3.1.1.2 lặp lại một đoạn "
            "về dẫn hướng bằng nắp/lồng(chỗ đã nói ở 3.6), bản dịch giữ nguyên nhưng gộp để tránh "
            "lặp từ; Hình 3.24 trong nguyên bản được dùng cho cả ống mềm tạo hình cơ khí lẫn bố trí "
            "vật liệu đệm, bản dịch gộp hai hình ống mềm thành Hình 3.23 và dành Hình 3.24 cho bố trí "
            "đệm; một số chú thích bị cắt bỏ chữ cuối trong bản in (ví dụ <i>Various Plug Contour for "
            "Different Flow Characterization</i>) được viết đầy đủ ở đây. Các con số trong bảng ISO "
            "15848-1 và FCI 91-1 được giữ nguyên theo nguồn. Các ký hiệu ô vuông đặc trong nguyên bản "
            "được trình bày thành danh sách gạch đầu dòng. Đường cong và mặt cắt được vẽ lại dạng "
            "vector minh họa, không phải bản vẽ kỹ thuật có tỷ lệ.")
    return (
        "<b>Source notes.</b> The source has several quirks: section 3.1.1.2 repeats a passage on "
            "bonnet/cage guiding already covered in 3.6 - the translation keeps it but merges the "
            "duplicated lines; Figure 3.24 in the source is used both for mechanically-formed bellows "
            "and for packing arrangements, so here the two bellows views are grouped as Figure 3.23 "
            "and Figure 3.24 is reserved for packing arrangements; a few captions are truncated in "
            "print (for example <i>Various Plug Contour for Different Flow Characterization</i>) and "
            "are completed here. All ISO 15848-1 and FCI 91-1 table values are kept as printed. "
            "Solid-square bullets in the source are rendered as ordinary bullet lists. Curves and "
            "cross-sections are redrawn as illustrative vectors, not scale engineering drawings.")


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
        "Chương này khảo sát các kiểu thân van điều khiển, van quay, đầu nối và nắp van, vật liệu "
        "đệm và tuân thủ môi trường, định hình dòng chảy và cơ cấu chấp hành — toàn bộ dải lựa chọn "
        "cơ khí tạo nên một cụm van điều khiển hoàn chỉnh."
        if vi else
        "This chapter surveys control valve body styles, rotary valves, end connections and bonnets, "
        "packing and environmental compliance, flow characterization and actuators - the full range "
        "of mechanical choices that make up a complete control valve assembly."))
    N(note_terms("vi"), note_terms("en"))

    # ------------------------------------------------------------ 3.1
    H("3.1 Các kiểu van điều khiển", "3.1 Control Valve Styles")
    P("Van điều khiển điều chỉnh tốc độ dòng chảy của chất lỏng khi vị trí của phần tử đóng thay đổi "
      "dưới tác dụng của lực từ cơ cấu chấp hành. Để làm được điều đó, van phải:",
      "The control valve regulates the rate of fluid flow as the position of the valve closure member "
      "is changed by force from the actuator. To do this, the valve must:")
    B(["Chứa được chất lỏng mà không rò rỉ ra bên ngoài;",
       "Có đủ năng lực cho dịch vụ dự kiến;",
       "Có khả năng chịu được các tác động xói mòn, ăn mòn và nhiệt độ của quá trình; và",
       "Có đầu nối phù hợp để ghép với đường ống kề cận và phương tiện lắp cơ cấu chấp hành cho phép "
       "truyền lực đẩy của cơ cấu tới thân hoặc trục van."],
      ["Contain the fluid without external leakage;",
       "Have adequate capacity for the intended service;",
       "Be capable of withstanding the erosive, corrosive, and temperature influences of the process; and",
       "Incorporate appropriate end connections to mate with adjacent pipelines and actuator "
       "attachment means to permit transmission of actuator thrust to the valve stem or shaft."])
    P("Nhiều kiểu thân van điều khiển đã được phát triển qua nhiều năm. Một số được ứng dụng rộng rãi, "
      "trong khi số khác đáp ứng các điều kiện dịch vụ đặc thù và được dùng ít hơn. Tóm tắt sau mô tả "
      "một số kiểu thân van điều khiển phổ biến đang dùng hiện nay.",
      "Many styles of control valve bodies have been developed through the years. Some have found "
      "wide application, while others meet specific service conditions and are used less frequently. "
      "The following summary describes some popular control valve body styles in use today.")

    # ------------------------------------------------------------ 3.1.1
    H("3.1.1 Van cầu", "3.1.1 Globe Valves", h3)
    H("3.1.1.1 Thân van một cổng", "3.1.1.1 Single-Port Valve Bodies", h4)
    B(["Một cổng là kiểu thân van phổ biến nhất và có kết cấu đơn giản.",
       "Van một cổng có nhiều dạng, như kiểu cầu, kiểu góc, thân phôi than, thân rèn và kết cấu tách.",
       "Nhiều thân van một chỗ ngồi dùng kết cấu lồng hoặc vòng giữ để giữ vòng chỗ ngồi, dẫn hướng "
       "nút van và tạo phương tiện thiết lập các đặc tính dòng đặc thù của van.",
       "Thân van một chỗ ngồi kiểu lồng hoặc vòng giữ cũng có thể dễ dàng thay đổi bằng cách đổi "
       "chi tiết trim để thay đổi đặc tính dòng hoặc tạo lưu lượng giảm, giảm tiếng ồn, hoặc giảm hay "
       "loại bỏ xói mòn do sủi bọt (cavitation).",
       "Van góc (Hình 3.1) thường dùng cho nước cấp lò hơi và thoát nước gia nhiệt, và trong các sơ "
       "đồ đường ống mà không gian bị hạn chế và van cũng có thể đóng vai trò như một khúc khuỷu. "
       "Van được minh họa có kết cấu kiểu lồng. Các kiểu khác có thể có đầu ra mở rộng, trim bị tiết "
       "lưu hoặc lót đầu ra để giảm xói mòn, bay hơi (flashing) hoặc hư hỏng do sủi bọt."],
      ["Single port is the most common valve body style and is simple in construction.",
       "Single-port valves are available in various forms, such as globe, angle, bar stock, forged, "
       "and split constructions.",
       "Many single-seated valve bodies use cage or retainer-style construction to retain the seat "
       "ring, provide valve plug guiding, and provide a means for establishing particular valve flow "
       "characteristics.",
       "Cage or retainer-style single-seated valve bodies can also be easily modified by change of "
       "trim parts to change the flow characteristic or provide reduced-capacity flow, noise "
       "attenuation, or reduction or elimination of cavitation.",
       "Angle valves (Figure 3.1) are commonly used in boiler feedwater and heater drain service and "
       "in piping schemes where space is at a premium and the valve can also serve as an elbow. The "
       "valve shown has cage-style construction. Others might have expanded outlet connections, "
       "restricted trim, or outlet liners for reduction of erosion, flashing, or cavitation damage."])
    FIG(1, F.fig_f31())
    P("Thân van bằng hợp kim thường được chỉ định cho ứng dụng ăn mòn (xem Hình 3.2). Chúng có thể "
      "chế tạo từ thanh phôi, vật đúc hoặc vật rèn. Khi cần hợp kim đặc biệt để chống ăn mòn, đôi khi "
      "thân van bằng thanh phôi rẻ hơn thân van đúc. Cũng có thể dùng van có lớp lót polyme.",
      "Alloy valve bodies are often specified for corrosive applications (see Figure 3.2). They can "
      "be made from bar stock, castings, or forgings. When exotic metal alloys are required for "
      "corrosion resistance, sometimes a bar stock valve body is less expensive than a cast valve "
      "body. A valve with a polymer liner may also be used.")
    FIG(2, F.fig_f32())
    P("Van áp suất cao thường dùng trong công nghiệp hydrocarbon và điện lực, có sẵn tới CL4500 hoặc "
      "API 10.000. Chúng có thể là kiểu cầu hoặc kiểu góc và thường có trim chuyên dụng tùy chọn cho "
      "dịch vụ khắc nghiệt. Van cầu dẫn hướng bằng thân áp suất cao thường dùng trong sản xuất khí "
      "và dầu. Các biến thể sẵn có gồm nắp ren và góc tự thoát nước. Phiên bản có bích có cấp tới "
      "Class 2500.",
      "High-pressure valves are often used in the hydrocarbon and power industries and are available "
      "to CL4500 or API 10,000. These can be globe or angle designs and typically have optional "
      "specialized trim for severe service applications. High-pressure stem-guided globe valves are "
      "often used in production of gas and oil. Variations available include a threaded bonnet and "
      "self-draining angle. Flanged versions are available with ratings to Class 2500.")

    H("3.1.1.2 Thân van dẫn hướng bằng chốt và bằng cổng",
      "3.1.1.2 Post- and Port-Guided Valve Bodies", h4)
    P("Phương pháp dẫn hướng bằng chốt và bằng cổng trong van GX thay đổi theo kích cỡ van. Bảng sau "
      "quy định các phương pháp dẫn hướng khác nhau theo từng cỡ.",
      "Post- and port-guiding methods in GX valve vary according to valve size. The table below "
      "specifies the different guiding methods across sizes.")
    b.append(table(
        ["Dẫn hướng bằng thân / Stem guiding", "Dẫn hướng bằng cổng / Port guiding",
         "Dẫn hướng bằng nắp / Bonnet guiding"],
        [("Cỡ 1/2 đến 1 inch / Size 1/2 to 1 in",
          "Cỡ 1 1/2 đến 4 inch / Size 1 1/2 to 4 in",
          "Cỡ 3 đến 6 inch / Size 3 to 6 in"),
         ("Nút được dẫn bằng thân / Plug guided by stem",
          "Nút được dẫn bằng cổng / Plug guided by port",
          "Nút được dẫn bằng nắp / Plug guided by bonnet"),
         ("Nút mất cân bằng / Unbalanced plug",
          "Nút mất cân bằng / Unbalanced plug",
          "Nút mất cân bằng và cân bằng / Unbalanced and balanced plug")],
        caption="Phương pháp dẫn hướng theo kích cỡ / Guiding method by size"))
    B(["Thường được chỉ định cho ứng dụng có yêu cầu đóng chặt nghiêm ngặt. Chúng dùng bề mặt chỗ "
       "ngồi kim loại-kim loại hoặc đệm mềm bằng PTFE hay vật liệu composition khác tạo lớp làm kín. "
       "Chúng đáp ứng được hầu hết yêu cầu dịch vụ.",
       "Vì chất lỏng áp suất cao thường nạp vào toàn bộ diện tích của cổng, lực mất cân bằng tạo ra "
       "phải được tính đến khi chọn cơ cấu chấp hành cho thân van điều khiển dẫn hướng bằng chốt và "
       "bằng cổng.",
       "Dù phổ biến nhất ở cỡ nhỏ, van dẫn hướng bằng chốt và cổng thường có thể dùng ở cỡ NPS 4-8 "
       "(DN 100-200) với cơ cấu chấp hành lực đẩy lớn.",
       "Chúng có thể nhạy với rung do giảm áp suất cao, nên cần lưu ý trong thiết kế để tránh hiện "
       "tượng này."],
      ["Generally specified for applications with stringent shutoff requirements. They use "
       "metal-to-metal seating surfaces or soft seating with PTFE or other composition materials "
       "forming the seal. They can handle most service requirements.",
       "Because high-pressure fluid is normally loading the entire area of the port, the unbalanced "
       "force created must be considered in selecting actuators for post- and port-guided control "
       "valve bodies.",
       "Although most popular in the smaller sizes, post- and port-guided valves can often be used "
       "in NPS 4-8 (DN 100-200) sizes with high-thrust actuators.",
       "They can be susceptible to high-pressure drop vibration, so care is needed with the design "
       "to avoid this."])
    P("Hình 3.3 cho thấy một trong những kiểu thân van điều khiển dạng cầu dẫn hướng bằng chốt phổ "
      "biến nhất. Chúng được dùng rộng rãi trong điều khiển quá trình, đặc biệt ở cỡ NPS 1-4 "
      "(DN 20-100). Chiều dòng chảy thông thường nhất là đi lên qua vòng chỗ ngồi.",
      "Figure 3.3 shows one of the more popular styles of post-guided globe-type control valve "
      "bodies. They are widely used in process control applications, particularly in NPS 1-4 "
      "(DN 20-100). Normal flow direction is most often up through the seat ring.")
    FIG(3, F.fig_f33())

    H("3.1.1.3 Thân van kiểu lồng", "3.1.1.3 Cage-Style Valve Bodies", h4)
    P("Trim kiểu lồng (Hình 3.4) cung cấp dẫn hướng cho nút van, giữ vòng chỗ ngồi và định hình dòng "
      "chảy. Ngoài ra, có nhiều vật liệu và kiểu làm kín khác nhau để làm kín giữa phần trên của đường "
      "kính ngoài nút van và lỗ lồng, nhằm hạn chế chất lỏng áp suất cao phía thượng lưu rò sang hệ "
      "thống hạ lưu áp suất thấp hơn. Ở thiết kế cân bằng, áp suất hạ lưu tác động lên cả mặt trên và "
      "mặt dưới của nút van, triệt tiêu phần lớn lực mất cân bằng tĩnh. Lực mất cân bằng giảm cho phép "
      "vận hành van với cơ cấu chấp hành nhỏ hơn so với trim mất cân bằng.",
      "Cage-style trim (Figure 3.4) provides valve plug guiding, seat ring retention, and flow "
      "characterization. In addition, a variety of seal materials and styles are available to seal "
      "between the upper portion of the valve plug's outer diameter and the cage bore to limit "
      "leakage of the upstream, high-pressure fluid into the lower pressure downstream system. In "
      "balanced designs, downstream pressure acts on both the top and bottom sides of the valve plug, "
      "which nullifies most of the static unbalanced force. Reduced unbalanced force permits "
      "operation of the valve with smaller actuators than those necessary for unbalanced valve trim.")
    P("Khả năng thay thế lẫn nhau của trim cho phép lựa chọn một số đặc tính dòng, giảm tiếng ồn, "
      "chống sủi bọt hoặc các khả năng dịch vụ khắc nghiệt khác. Với hầu hết thiết kế trim sẵn có, "
      "chiều dòng chuẩn là đi vào qua các lỗ lồng và đi xuống qua vòng chỗ ngồi. Tuy nhiên, trim giảm "
      "tiếng ồn thường cho dòng đi lên. Các trim này có sẵn trong nhiều tổ hợp vật liệu, kích cỡ tới "
      "NPS 36 (DN 900) và cấp áp suất tới Class 4500 hoặc API 10.000.",
      "Interchangeability of trim permits choice of several flow characteristics, noise attenuation, "
      "anti-cavitation, or other severe service capability. For most available trim designs, the "
      "standard direction of flow is in through the cage openings and down through the seat ring. "
      "However, noise attenuation trim is typically flow up. These are available in various material "
      "combinations, sizes through NPS 36 (DN 900), and pressure ratings up to Class 4500 or "
      "API 10,000.")
    FIG(4, F.fig_f34())

    H("3.1.1.4 Thân van hai cổng", "3.1.1.4 Double-Ported Valve Bodies", h4)
    B(["Ngành công nghiệp phần lớn đã chuyển sang không dùng thiết kế van hai cổng.",
       "Lực động trên nút có xu hướng tự cân bằng vì dòng chảy có xu hướng mở một cổng và đóng cổng kia.",
       "Lực động giảm tác động lên nút có thể cho phép chọn cơ cấu chấp hành nhỏ hơn so với thân van "
       "một cổng mất cân bằng có năng lực tương đương.",
       "Thân van thường chỉ được cung cấp ở cỡ NPS 4 (DN 100) trở lên.",
       "Thân van thường có năng lực cao hơn van một cổng cùng cỡ đường ống.",
       "Nhiều thân van hai cổng có thể đảo chiều, nên nút van có thể lắp theo kiểu đẩy xuống để mở "
       "hoặc đẩy xuống để đóng (Hình 3.5).",
       "Chỗ ngồi kim loại-kim loại thường cho khả năng đóng cấp II, dù cũng có thể đạt cấp III.",
       "Nút van dẫn hướng bằng cổng thường dùng cho dịch vụ đóng mở hoặc tiết lưu áp suất thấp. Nút "
       "dẫn hướng trên và dưới cho vận hành ổn định trong điều kiện dịch vụ khắc nghiệt."],
      ["The industry has predominantly moved away from using double-ported valve designs.",
       "Dynamic force on the plug tends to be balanced as flow tends to open one port and close the other.",
       "Reduced dynamic forces acting on the plug might permit choosing a smaller actuator than would "
       "be necessary for a single-ported unbalanced valve body with similar capacity.",
       "Bodies are usually furnished only in NPS 4 (DN 100) or larger.",
       "Bodies normally have higher capacity than single-ported valves of the same line size.",
       "Many double-ported bodies reverse, so the valve plug can be installed as either push-down-to-open "
       "or push-down-to-close (Figure 3.5).",
       "Metal-to-metal seating usually provides Class II shutoff capability, although Class III "
       "capability is also possible.",
       "Port-guided valve plugs are often used for on/off or low-pressure throttling service. "
       "Top- and bottom-guided valve plugs furnish stable operation for severe service conditions."])
    P("Thân van điều khiển trong Hình 3.5 được lắp để nút van hoạt động theo kiểu đẩy xuống để mở. "
      "Thiết kế hai cổng từng được dùng trong nhà máy lọc dầu với chất lỏng có độ nhớt cao hoặc nơi "
      "lo ngại về chất gây ô nhiễm hay cặn quá trình bám trên trim.",
      "The control valve body shown in Figure 3.5 is assembled for push-down-to-open valve plug "
      "action. Double-ported designs were historically used in refineries on highly viscous fluids "
      "or where there was a concern about contaminants or process deposits on the trim.")
    FIG(5, F.fig_f35())

    H("3.1.1.5 Thân van ba chiều", "3.1.1.5 Three-Way Valve Bodies", h4)
    B(["Ba đầu nối đường ống cung cấp dịch vụ gộp dòng (trộn) hoặc tách dòng (chia) nói chung.",
       "Các biến thể gồm thiết kế dẫn hướng bằng lồng, bằng cổng và bằng thân, được chọn cho dịch vụ "
       "nhiệt độ cao, và có thể chỉ định đầu nối chuẩn (bích, ren, hàn đối đầu, v.v.) để ghép với hầu "
       "hết mọi sơ đồ đường ống.",
       "Việc chọn cơ cấu chấp hành đòi hỏi cân nhắc cẩn thận, đặc biệt với kết cấu có nút van mất cân bằng."],
      ["Three pipeline connections provide general converging (flow-mixing) or diverging "
       "(flow-splitting) service.",
       "Variations include cage-, port-, and stem-guided designs, selected for high-temperature "
       "service, and standard end connections (flanged, screwed, butt weld, etc.) can be specified "
       "to mate with most any piping scheme.",
       "Actuator selection demands careful consideration, particularly for constructions with an "
       "unbalanced valve plug."])
    P("Trong Hình 3.6, thân van ba chiều có nút cân bằng được thể hiện với nút trụ ở vị trí giữa "
      "hành trình. Vị trí này mở cổng chung dưới sang cả cổng bên phải và cổng bên trái. Kết cấu có "
      "thể dùng để điều tiết tại vị trí giữa cho chất lỏng gộp hoặc tách.",
      "In Figure 3.6, a three-way valve body with a balanced valve plug is shown with the cylindrical "
      "valve plug in the mid-travel position. This position opens the bottom common port to both the "
      "right-hand port and left-hand port. The construction can be used for throttling mid-travel "
      "position control of either converging or diverging fluids.")
    FIG(6, F.fig_f36())

    # ------------------------------------------------------------ 3.1.2
    H("3.1.2 Van vệ sinh", "3.1.2 Sanitary Valves", h3)
    P("Những kiểu thân van này được thiết kế để đáp ứng các yêu cầu nghiêm ngặt của ngành dược phẩm "
      "và công nghệ sinh học. Tiêu chuẩn của các ngành này khác với tiêu chuẩn áp dụng cho thiết kế "
      "van điều khiển thông thường vì trong nhiều ứng dụng, chất lỏng quá trình cuối cùng sẽ dùng cho "
      "tiêu dùng của con người. Vì lý do đó, việc ngăn ngừa sự phát triển của vi khuẩn và sự xâm nhập "
      "của tạp chất vào chất lỏng quá trình là tối quan trọng.",
      "These valve body styles are designed to satisfy the stringent demands of the pharmaceutical "
      "and biotechnology industries. The standards of these industries differ from those that apply "
      "to conventional control valve designs because in many applications, the process fluid will "
      "ultimately be for human consumption. For this reason, it is of utmost importance to prevent "
      "the development of bacterial growth and the addition of foreign matter into the process fluid.")
    B(["Các gioăng trượt và không trượt theo ASME-BPE đã được tích hợp để đáp ứng nhiều ứng dụng "
       "vô trùng. Có sẵn chứng nhận.",
       "Vật liệu kim loại dùng trong các van này đáp ứng Tiêu chuẩn Vệ sinh 3A. Có sẵn chứng nhận.",
       "Các elastomer dùng trong thiết kế van được chứng nhận theo FDA và USP CL VI.",
       "Van có sẵn bề mặt bên trong đánh bóng điện hóa <35 Ra microinch (0,89 micron) theo tiêu "
       "chuẩn. Các giá trị độ nhám bề mặt thấp hơn có sẵn như tùy chọn.",
       "Thiết kế tự thoát nước làm cho các van này rất phù hợp cho ứng dụng Làm sạch tại chỗ (CIP) "
       "và Hấp tiệt trùng tại chỗ (SIP).",
       "Van được gia công từ thép không gỉ 316L với đầu nối tri-clamp hoặc tùy chọn đầu hàn đối đầu. "
       "Có sẵn vật liệu khác như tùy chọn.",
       "Có thể đáp ứng các ứng dụng hấp tiệt trùng liên tục với nhiệt độ tới 177 độ C (350 độ F)."],
      ["ASME-BPE sliding and non-sliding seals have been incorporated to satisfy a broad range of "
       "aseptic applications. Certifications are available.",
       "Metallic materials used in these valves satisfy 3A Sanitary Standards. Certifications are available.",
       "Elastomers used in these valve designs are certified per FDA and USP CL VI.",
       "Valves are available with <35 Ra microinch (0.89 Micron) electro-polished internal surfaces "
       "as standard. Other lesser values for surface roughness are available as options.",
       "Self-draining designs make these valves well suited for Clean-in-Place (CIP) and "
       "Steam-in-Place (SIP) applications.",
       "Valves are machined 316L stainless steel with tri-clamp or optional butt weld-ends. Other "
       "materials are available as options.",
       "Continuous sterile steam applications with temperatures up to 177 deg C (350 deg F) can be "
       "accommodated."])

    # ------------------------------------------------------------ 3.1.3
    H("3.1.3 Van quay", "3.1.3 Rotary Valves", h3)

    H("3.1.3.1 Thân van bướm", "3.1.3.1 Butterfly Valve Bodies", h4)
    B(["Thân van cần ít không gian lắp đặt nhất (Hình 3.9).",
       "Chúng cho tổn thất áp suất thấp qua van.",
       "Thân van bướm mang lại tính kinh tế, đặc biệt ở cỡ lớn và lưu lượng trên mỗi đồng vốn đầu tư.",
       "Thân van ghép được với bích ASME và DN dạng mặt nổi tiêu chuẩn.",
       "Van bướm có thể cần cơ cấu chấp hành công suất lớn hoặc cỡ lớn nếu van to hoặc giảm áp lớn, "
       "vì mô-men vận hành có thể rất lớn.",
       "Có sẵn thiết bị cho dịch vụ trong nhà máy điện hạt nhân với yêu cầu rò rỉ rất nghiêm ngặt.",
       "Van bướm tiêu chuẩn có sẵn cỡ tới NPS 72 (DN 1800) cho các ứng dụng điều khiển đa dạng. Cỡ nhỏ "
       "có thể dùng các phiên bản cơ cấu khí nén màng hoặc piston truyền thống, kể cả kiểu cơ cấu quay "
       "hiện đại. Cỡ lớn có thể cần cơ cấu điện công suất lớn, xi lanh khí nén hành trình dài hoặc cơ "
       "cấu điện-thủy lực. Van bướm thường có đặc tính dòng gần phần trăm bằng. Chúng dùng được cho "
       "điều tiết hoặc điều khiển đóng mở.",
       "Có sẵn cả thân van bướm loại lệch một và lệch hai.",
       "Đĩa rời khỏi gioăng sau 15 độ hành trình. Điều này giúp kéo dài tuổi thọ gioăng và cho phép "
       "mô-men nhỏ hơn hoặc đóng chặt hơn so với kiểu truyền thống."],
      ["Bodies require minimum space for installation (Figure 3.9).",
       "They provide low pressure loss through the valves.",
       "Butterfly valve bodies offer economy, particularly in larger sizes and flow capacity per "
       "investment dollar.",
       "Bodies mate with standard raised-face ASME and DN flanges.",
       "Butterfly valve bodies might require high-output or large actuators if the valve is big or "
       "the pressure drop is high because operating torques might be quite large.",
       "Units are available for service in nuclear power plant applications with very stringent "
       "leakage requirements.",
       "Standard butterfly valves are available in sizes through NPS 72 (DN 1800) for miscellaneous "
       "control valve applications. Smaller sizes can use versions of traditional diaphragm or "
       "piston pneumatic actuators, including the modern rotary actuator styles. Larger sizes might "
       "require high-output electric, long-stroke pneumatic cylinder, or electro-hydraulic actuators. "
       "Butterfly valves typically exhibit an approximately equal-percentage flow characteristic. "
       "They can be used for throttling service or for on/off control.",
       "Both single and double offset body type available in butterfly valve bodies.",
       "The disk rotates away from seal after 15 degree of travel. It helps extend the seal life and "
       "allows for lower torques / tighter shutoff than traditional models."])
    b.append(table(
        ["Kiểu van / Valve type", "Kích cỡ / Size", "Độ lệch / Offset"],
        [("Van bướm / Butterfly valve", "Đến 12 inch / Up to 12 in",
          "Có cả lệch đơn và lệch đôi / Single and double available"),
         ("Van bướm / Butterfly valve", "> 12 đến 36 inch / > 12 up to 36",
          "Lệch đơn / Single offset")],
        caption="Phân biệt độ lệch theo kích cỡ / Offset differentiation by size"))
    FIG(7, F.fig_f37())
    FIG(8, F.fig_f38())
    FIG(9, F.fig_f39())

    H("3.1.3.2 Thân van bi đoạn", "3.1.3.2 Segmented Ball Valve Bodies", h4)
    P("Kết cấu này tương tự van bi thông thường, nhưng có đoạn cầu với rãnh V định hình được cấp "
      "bằng sáng chế (Hình 3.9). Rãnh V tạo đặc tính dòng phần trăm bằng.",
      "This construction is similar to a conventional ball valve, but with a patented, contoured "
      "V-notch segment in the ball (Figure 3.9). The V-notch produces an equal-percentage flow "
      "characteristic.")
    P("Các van điều khiển này có khả năng điều chỉnh dải (rangeability), điều khiển và đóng chặt tốt. "
      "Ngành giấy, nhà máy hóa chất, nhà máy xử lý nước thải, ngành điện và nhà máy lọc dầu dùng kiểu "
      "thiết kế van này. Emerson cung cấp thêm tùy chọn cho van bi để bảo vệ ở mức tiếng ồn và sủi bọt "
      "trung bình. Xem Hình 3.10 cho các tùy chọn van bi chống sủi bọt và giảm tiếng ồn.",
      "These control valves have good rangeability, control, and shutoff capability. The paper "
      "industry, chemical plants, sewage treatment plants, the power industry, and petroleum "
      "refineries use these type of valve designs. Emerson offers additional options in ball valves "
      "for moderate noise and cavitation protection. Refer to Figure 3.10 for ball valve options for "
      "cavitation and noise attenuation.")
    B(["Thiết kế dòng chảy thẳng có thể chịu được giảm áp nhỏ.",
       "Thân van bi đoạn rãnh V phù hợp điều khiển chất lỏng xói mòn hoặc nhớt, bột giấy hoặc các "
       "hỗn dịch chứa hạt rắn hoặc sợi.",
       "Chúng dùng cơ cấu quay tiêu chuẩn màng-lò xo, piston, điện hoặc điện-thủy lực.",
       "Quả cầu luôn tiếp xúc với gioăng trong lúc quay, tạo hiệu ứng cắt khi van đóng và hạn chế tắc nghẽn.",
       "Thân van có sẵn gioăng cầu bằng hợp kim chịu lực nặng hoặc hợp chất nhồi PTFE để cho dải "
       "điều chỉnh vượt trội trên 300:1.",
       "Van bi đoạn có sẵn đầu nối không bích hoặc thân có bích.",
       "Cả van có bích và không bích đều ghép được với bích ASME Class 150, 300 hoặc 600. Cũng có "
       "thiết kế cho bích DN, PN10, 16, 25 hoặc 40. Có cả thiết kế bích JIS 10K và 20K."],
      ["Straight-through flow design can accommodate small pressure drop.",
       "V-notch ball control valve bodies are suited to control erosive or viscous fluids, paper "
       "stock, or other slurries containing entrained solids or fibers.",
       "They use standard spring-and-diaphragm, piston, electric, or electro-hydraulic rotary actuators.",
       "The ball remains in contact with the seal during rotation, which produces a shearing effect "
       "as the ball closes and minimizes clogging.",
       "Bodies are available with either heavy-duty or PTFE-filled composition ball seal ring to "
       "provide excellent rangeability in excess of 300:1.",
       "Segmented ball control valves are available in flangeless or flanged-body end connections.",
       "Both flanged and flangeless valves mate with ASME Class 150, 300, or 600 flanges. Designs are "
       "also available for DN flanges, PN10, 16, 25, or 40. JIS 10K and 20K flanged designs are also "
       "available."])
    FIG(10, F.fig_f3_10())

    H("3.1.3.3 Thân van bướm hiệu năng cao",
      "3.1.3.3 High-Performance Butterfly Valve Bodies", h4)
    B(["Các thân van này cho điều tiết hiệu quả.",
       "Thân van bướm điều khiển hiệu năng cao cho đặc tính dòng tuyến tính qua 90 độ quay đĩa (Hình 3.11).",
       "Lắp lệch đôi của đĩa kéo đĩa ra khỏi gioăng sau khi bắt đầu mở, giảm mòn gioăng.",
       "Thân van bướm điều khiển hiệu năng cao có sẵn cỡ tới NPS 48 (DN 1200), tương thích bích ASME tiêu chuẩn.",
       "Chúng dùng cơ cấu quay tiêu chuẩn màng-lò xo, piston, điện hoặc điện-thủy lực.",
       "Chiều dòng chuẩn phụ thuộc thiết kế gioăng; dòng ngược làm giảm năng lực."],
      ["These bodies offer effective throttling control.",
       "High-performance butterfly control valve bodies provide linear flow characteristic through "
       "90 degrees of disk rotation (Figure 3.11).",
       "Double offset mounting of disk pulls it away from the seal after it begins to open, "
       "minimizing seal wear.",
       "High-performance butterfly control valve bodies are available in sizes through NPS 48 "
       "(DN 1200) compatible with standard ASME flanges.",
       "They use standard spring-and-diaphragm, piston, electric, or electro-hydraulic rotary actuators.",
       "Standard flow direction is dependent on seal design; reverse flow results in reduced capacity."])
    P("Van bướm điều khiển hiệu năng cao dùng cho ứng dụng dịch vụ nói chung không cần điều tiết chính "
      "xác. Chúng thường được dùng trong ứng dụng cần cỡ lớn và nhiệt độ cao nhờ chi phí thấp hơn so "
      "với kiểu van điều khiển khác. Dải điều khiển của kiểu van này xấp xỉ một phần ba so với van bi "
      "hoặc van kiểu cầu. Do đó cần thêm thận trọng khi tính cỡ và áp dụng kiểu van này để tránh các "
      "vấn đề điều khiển liên quan đến thay đổi tải quá trình. Chúng làm việc rất tốt cho ứng dụng tải "
      "quá trình không đổi. Thiết kế dùng đường bao định hình có thể mở rộng dải điều khiển tới mức "
      "của van bi đoạn.",
      "High-performance butterfly control valves are intended for general service applications not "
      "requiring precision throttling control. They are frequently used in applications requiring "
      "large sizes and high temperatures due to their lower cost relative to other styles of control "
      "valves. The control range for this style of valve is approximately one third as large as ball "
      "or globe-style valves. Consequently, additional care is required in sizing and applying this "
      "style of valve to eliminate control problems associated with process load changes. They work "
      "quite well for constant process load applications. Designs using characterized contour are "
      "able to expand the control range to that of a segmented ball valve.")
    FIG(11, F.fig_f3_11())

    H("3.1.3.4 Thân van nút lệch tâm", "3.1.3.4 Eccentric Plug Valve Bodies", h4)
    B(["Cụm van chống xói mòn. Thiết kế thân và trim chắc chắn chịu nhiệt tới 427 độ C (800 độ F) và "
       "chênh áp đóng tới 1500 psi (103 bar).",
       "Đường đi của đĩa lệch tâm giảm tiếp xúc với vòng chỗ ngồi khi mở, giảm mòn và ma sát, kéo dài "
       "tuổi thọ chỗ ngồi và cải thiện hiệu năng điều tiết (Hình 3.13).",
       "Vòng chỗ ngồi tự định tâm và đĩa chắc chắn cho phép dòng xuôi hoặc ngược với độ kín chặt ở "
       "cả hai hướng. Đĩa, vòng chỗ ngồi và vòng giữ có sẵn vật liệu cứng, kể cả gốm, để lựa chọn "
       "khả năng chống xói mòn.",
       "Nút, vòng chỗ ngồi và vòng giữ có sẵn vật liệu cứng, kể cả gốm và cacbua, để cải thiện lựa "
       "chọn chống xói mòn.",
       "Có sẵn tùy chọn vòng làm kín hỗ trợ bằng áp suất hai chiều cho độ đóng kín đặc biệt.",
       "Có sẵn thiết kế dùng quả cầu rãnh V thay cho nút van cho yêu cầu năng lực cao hơn."],
      ["Valve assembly combats erosion. The rugged body and trim design handle temperatures to "
       "427 deg C (800 deg F) and shutoff pressure drops to 1500 psi (103 bar).",
       "The path of the eccentric disk minimizes contact with the seat ring when opening, reducing "
       "seat wear and friction, prolonging seat life, and improving throttling performance "
       "(Figure 3.13).",
       "Self-centering seat ring and rugged disk allow forward or reverse flow with tight shutoff in "
       "either direction. Disk, seat ring, and retainer are available in hardened materials, "
       "including ceramics, for selection of erosion resistance.",
       "Plug, seat ring, and retainer are available in hardened materials, including ceramics and "
       "carbides, for improved selection of erosion resistance.",
       "Bi-directional pressure assisted seal ring options available that provide exceptional tight shut off.",
       "Designs offering a segmented V-notch ball in place of the plug for higher capacity "
       "requirements are available."])
    FIG(12, F.fig_f3_12())
    P("Kiểu van quay điều khiển này phù hợp chất lỏng xói mòn, đóng cốc (coking) và các chất khó xử "
      "lý khác, cho vận hành điều tiết hoặc đóng mở. Van có bích hoặc không bích có đường dẫn suôn "
      "sẻ và chi tiết trim kim loại chắc chắn cho dịch vụ đáng tin cậy trong ứng dụng hỗn dịch. Các "
      "van này được dùng trong khai khoáng, lọc dầu, điện và công nghiệp giấy và bột giấy.",
      "This style of rotary control valve suits erosive, coking, and other hard-to-handle fluids, "
      "providing either throttling or on/off operation. The flanged or flangeless valves feature "
      "streamlined flow passages and rugged, metal trim components for dependable service in slurry "
      "applications. These valves are used in mining, petroleum refining, power, and pulp and paper "
      "industries.")
    FIG(13, F.fig_f3_13())

    H("3.1.3.5 Thân van bi cổng đầy", "3.1.3.5 Full-Port Ball Valve Bodies", h4)
    P("Van bi điều khiển cổng đầy được thiết kế để tối ưu áp suất, điều tiết, dòng chảy và điều khiển "
      "quá trình. Emerson có van bi cổng đầy ba mảnh gắn trục chốt thiết kế đặc biệt cho điều khiển "
      "tự động trong dịch vụ bypass, mẻ, giám sát và đóng khẩn cấp, và gần như không gây hạn chế "
      "dòng. Các van này đã được thử lửa và chứng nhận theo API 6 và 6FA.",
      "The full-port ball control valve is designed for optimized pressure, throttling, flow, and "
      "process control. Emerson has special design three piece trunnion mounted full-bore control "
      "valves designed for automated control in bypass, batch, monitor, and emergency shutoff service "
      "applications, and it presents little or no restriction flow. These valves are fire tested and "
      "certified for API 6 and 6FA.")
    P("Thường thì có tùy chọn giảm chấn để kiểm soát tiếng ồn và rung trong van cổng đầy. Van bi dùng "
      "như thiết bị điều tiết lý tưởng là sản phẩm tiết diện giảm, hoặc cơ cấu cổng đầy có bộ giảm "
      "chấn hấp thụ một phần giảm áp nhỏ ở vị trí mở rộng. Van bi cổng đầy ở vị trí mở rộng phải quay "
      "15 đến 20 độ trước khi hấp thụ năng lượng đáng kể từ hệ thống, liên quan đến độ trễ điều khiển "
      "quá trình bổ sung. Thiết bị tiết diện giảm hoặc giảm chấn hấp thụ một lượng áp suất nhỏ khi mở "
      "rộng; khi quả cầu quay, giảm áp tăng dần ngay ở các đoạn đầu của hành trình. Van bi cổng đầy "
      "gần như không hạn chế dòng và cho phép thông tẩy (khi không lắp giảm chấn). Xem Hình 3.14.",
      "Typically, there is an option for attenuation to control noise and vibration in full-bore "
      "valves. A ball valve as a throttling control device ideally is a reduced bore product, or "
      "full-bore mechanism with an attenuator that absorbs some small pressure drop in the wide-open "
      "position. A full-port ball valve, in the wide-open position, must rotate 15 to 20 degrees "
      "before absorbing any significant energy from the system, this relates to additional process "
      "control lag. A reduced bore or attenuated device absorbs a small amount of pressure wide open; "
      "as the ball rotates, increasing pressure drop occurs in the first increments of travel. Full "
      "port ball valves present little or no restriction to flow and allow for pigging (when not "
      "attenuated). See Figure 3.14.")
    FIG(14, F.fig_f3_14())
    FIG(15, F.fig_f3_15())

    H("3.1.3.6 Bộ chọn dòng đa cổng", "3.1.3.6 Multi-Port Flow Selector", h4)
    P("Van chọn dòng đa cổng nối với tám đường vào, cho phép cô lập, chuyển hướng và thử chất lỏng từ "
      "một đường riêng qua nút quay, trong khi bảy đường còn lại tiếp tục chảy tới cổng ra chung của "
      "nhóm. Van này cung cấp lựa chọn và chuyển hướng gọn nhẹ chất lỏng từ một đường riêng để thử "
      "mà không làm gián đoạn sản xuất từ tất cả các đường khác.",
      "A multi-port flow selector valve connects to eight input lines, allowing for the isolation, "
      "diversion, and testing of fluid from any individual line through a rotating plug, while the "
      "remaining seven lines continue to flow to a common group outlet. This valve provides compact "
      "selection and diversion of fluids from an individual line for testing without disrupting the "
      "production from all other lines.")
    P("Bộ chọn dòng đa cổng gồm bốn thành phần chính: thân, nắp, nút rô-to và cơ cấu chấp hành. Thân "
      "gồm các cổng vào và ra để nối cả tám đầu vào, một cổng ra thử hoặc chuyển hướng và cổng ra chung "
      "của nhóm. Nắp giữ nút theo phương thẳng đứng, được cân bằng để quay trong thân, và làm kín chặt "
      "với thân van. Nút dùng để chọn môi chất nào được đưa qua cổng ra thử.",
      "The multi-port flow selector consists of four main components: the body, bonnet, rotor plug, "
      "and actuator. The body consists of inlet and outlet ports to connect all eight inlets, one "
      "test or diversion outlet, and common group outlet. The bonnet will hold the plug vertically, "
      "balanced to rotate within the body, and provides tight sealing to the valve body. The plug is "
      "used to select which media port is sent through the test outlet port.")
    FIG(16, F.fig_f3_16())

    # ------------------------------------------------------------ 3.2
    H("3.2 Đầu nối van điều khiển", "3.2 Control Valve End Connections")
    P("Ba phương pháp phổ biến nhất để lắp van điều khiển vào đường ống là dùng ren ống, bích có "
      "gioăng bắt bulông và đầu nối hàn.",
      "The three most common methods of installing control valves into pipelines are by means of "
      "screwed pipe threads, bolted gasketed flanges, and welded end connections.")

    H("3.2.1 Ren ống", "3.2.1 Screwed Pipe Threads", h3)
    P("Đầu nối ren phổ biến ở van điều khiển cỡ nhỏ, kinh tế hơn đầu có bích. Ren thường chỉ định là "
      "ren NPT (National Pipe Thread) cái dạng côn trên thân van. Chúng tạo lớp làm kín kim loại-kim "
      "loại bằng cách nêm vào ren đực tương ứng ở đầu đường ống.",
      "Screwed end connections, popular in small control valves, offer more economy than flanged "
      "ends. The threads usually specified are tapered female NPT (National Pipe Thread) on the valve "
      "body. They form a metal-to-metal seal by wedging over the mating male threads on the pipeline ends.")
    P("Kiểu nối này thường chỉ giới hạn ở van NPS 2 (DN 50) trở xuống, không được khuyến nghị cho "
      "dịch vụ nhiệt độ cao. Bảo trì van có thể phức tạp hơn với đầu nối ren nếu cần tháo thân van khỏi "
      "đường ống, vì không thể tháo van mà không phá một mối nối bích hoặc khớp nối để vặn thân van ra "
      "khỏi đường ống.",
      "This connection style, usually limited to valves NPS 2 (DN 50) or smaller, is not recommended "
      "for elevated temperature service. Valve maintenance might be complicated by screwed end "
      "connections if it is necessary to take the body out of the pipeline because the valve cannot "
      "be removed without breaking a flanged joint or union connection to permit unscrewing the valve "
      "body from the pipeline.")

    H("3.2.2 Bích có gioăng bắt bulông", "3.2.2 Bolted Gasketed Flanges", h3)
    P("Van đầu bích dễ tháo khỏi đường ống và phù hợp cho toàn dải áp suất làm việc mà hầu hết van "
      "điều khiển được chế tạo (Hình 3.17). Đầu nối bích dùng được trong dải nhiệt độ từ gần không "
      "tuyệt đối đến khoảng 815 độ C (1500 độ F). Chúng dùng cho mọi cỡ van. Các loại đầu nối bích "
      "phổ biến gồm mặt phẳng, mặt nổi và mối nối kiểu vòng.",
      "Flanged end valves are easily removed from the piping and are suitable for use through the "
      "range of working pressures for which most control valves are manufactured (Figure 3.17). "
      "Flanged end connections can be used in a temperature range from near absolute zero to "
      "approximately 815 deg C (1500 deg F). They are used on all valve sizes. The most common "
      "flanged end connections include flat-face, raised-face, and ring-type joint.")
    P("Loại mặt phẳng cho phép các bích ghép tiếp xúc toàn bộ bề mặt với gioăng kẹp giữa chúng. Kết "
      "cấu này thường dùng cho van gang và đồng áp suất thấp, giúp giảm ứng suất bích do lực siết "
      "bulông ban đầu. Bích mặt nổi có vùng nổi hình tròn với đường kính trong bằng lỗ van và đường "
      "kính ngoài nhỏ hơn đường tròn bulông. Mặt nổi được gia công rãnh tròn đồng tâm để làm kín tốt "
      "và chống gioăng bị thổi ra. Loại bích này dùng với nhiều vật liệu gioăng và vật liệu bích cho "
      "áp suất tới 6000 psig (414 bar) và nhiệt độ tới 815 độ C (1500 độ F). Kiểu bích này thường là "
      "tiêu chuẩn trên thân gang Class 250 và tất cả thân thép và thép hợp kim.",
      "The flat-face variety allows the matching flanges to be in full-face contact with the gasket "
      "clamped between them. This construction is commonly used in low pressure, cast iron, and "
      "brass valves and minimizes flange stresses caused by initial bolting-up force. The raised-face "
      "flange features a circular raised face with inside diameter the same as the valve opening and "
      "with the outside diameter something less than the bolt circle diameter. The raised face is "
      "finished with concentric circular grooves for good sealing and resistance to gasket blowout. "
      "This kind of flange is used with a variety of gasket materials and flange materials for "
      "pressures through the 6000 psig (414 bar) pressure range and for temperatures through "
      "815 deg C (1500 deg F). This style of flanging is normally standard on Class 250 cast iron "
      "bodies and all steel and alloy steel bodies.")
    FIG(17, F.fig_f3_17())
    P("Bích kiểu vòng có bề ngoài giống bích mặt nổi, nhưng có rãnh chữ U cắt trên mặt nổi, đồng tâm "
      "với đường tâm ống. Gioăng là một vòng kim loại có tiết diện elip hoặc bát giác. Khi siết "
      "bulông, gioăng được nêm vào rãnh của hai bích ghép và tạo lớp làm kín chặt. Gioăng thường bằng "
      "sắt mềm nhưng có sẵn gần như mọi kim loại. Điều này tạo mối nối xuất sắc ở áp suất cao và dùng "
      "tới 15.000 psig (1034 bar), nhưng nói chung không dùng ở nhiệt độ cao. Chỉ cung cấp trên thân "
      "van thép và hợp kim khi được yêu cầu.",
      "The ring-type joint flange looks like the raised-face flange except that a U-shaped groove is "
      "cut in the raised face concentric with the pipe centerline. The gasket consists of a metal "
      "ring with either an elliptical or octagonal cross section. When the flange bolts are tightened, "
      "the gasket is wedged into the groove of the mating flanges and a tight seal is made. The gasket "
      "is generally soft iron but is available in almost any metal. This makes an excellent joint at "
      "high pressure and is used up to 15,000 psig (1034 bar), but is generally not used at high "
      "temperatures. It is furnished only on steel and alloy valve bodies when specified.")

    H("3.2.3 Đầu nối hàn", "3.2.3 Welded End Connections", h3)
    P("Đầu hàn trên van điều khiển kín ở mọi áp suất và nhiệt độ và có chi phí ban đầu thấp (Hình 3.18). "
      "Van đầu hàn khó tháo khỏi đường ống hơn và rõ ràng chỉ giới hạn ở vật liệu hàn được. Đầu hàn có "
      "hai kiểu: hàn lổ và hàn đối đầu.",
      "Welded ends on control valves are leak-tight at all pressures and temperatures and are "
      "economical in first cost (Figure 3.18). Weld-end valves are more difficult to take from the "
      "line and are obviously limited to weldable materials. Welded ends come in two styles: socket "
      "weld and butt weld.")
    FIG(18, F.fig_f3_18())
    P("Đầu hàn lổ được chuẩn bị bằng cách khoan ở mỗi đầu van một lỗ có đường kính trong lớn hơn một "
      "chút đường kính ngoài của ống. ống trượt vào lỗ, tựa vào vai rồi nối với van bằng mối hàn góc. "
      "Vì mối hàn góc không thấm hoàn toàn mối nối giữa van và ống, một số phương pháp thử không phá "
      "hủy không được dùng cho các van này. Đầu hàn lổ ở một cỡ nhất định có kích thước như nhau bất "
      "kể độ dày thành ống. Chúng thường được cung cấp ở cỡ tới NPS 2 (DN 50).",
      "The socket weld-ends are prepared by boring in each end of the valve a socket with an inside "
      "diameter slightly larger than the pipe outside diameter. The pipe slips into the socket where "
      "it butts against a shoulder and then joins to the valve with a fillet weld. Since a fillet weld "
      "does not fully penetrate the valve-pipe connection, some non-destructive methods are not used "
      "for these valves. Socket weld ends in any given size are dimensionally the same regardless of "
      "pipe schedule. They are usually furnished in sizes through NPS 2 (DN 50).")
    P("Đầu hàn đối đầu được chuẩn bị bằng cách vát mép mỗi đầu van để khớp với vát tương tự trên ống. "
      "Đầu van sau đó được nối vào đường ống bằng mối hàn thấm hoàn toàn. Loại mối nối này dùng được "
      "cho mọi kiểu van. Cách chuẩn bị đầu khác nhau cho mỗi độ dày ống. Chúng thường được cung cấp "
      "cho van điều khiển ở cỡ NPS 2-1/2 (DN 65) trở lên. Phải cẩn thận khi hàn thân van vào đường ống "
      "để tránh truyền quá nhiều nhiệt tới chi tiết trim. Trim có vật liệu hợp chất nhiệt độ thấp phải "
      "được tháo ra trước khi hàn.",
      "The butt weld-ends are prepared by beveling each end of the valve to match a similar bevel on "
      "the pipe. The valve ends are then joined to the pipeline and joined with a full-penetration "
      "weld. This type of joint can be used on all valve styles. The end preparation is different for "
      "each schedule of pipe. These are generally furnished for control valves in sizes NPS 2-1/2 "
      "(DN 65) and larger. Care must be exercised when welding valve bodies in the pipeline to "
      "prevent excessive heat transmitted to valve trim parts. Trims with low-temperature composition "
      "materials must be removed before welding.")

    H("3.2.4 Đầu nối khác", "3.2.4 Other Valve End Connections", h3)
    P("Có các loại đầu nối khác dùng với van điều khiển. Những kiểu này thường phục vụ mục đích riêng "
      "hoặc phản ánh thiết kế độc quyền. Một số ví dụ gồm đầu nối vệ sinh (hygienic) hoặc đầu nối "
      "dạng moay-ơ (hub).",
      "There are other types of end connections used with control valves. These types of end "
      "connections often serve specific purposes or reflect proprietary designs. Some examples "
      "include hygienic end connections or hub end connections.")

    # ------------------------------------------------------------ 3.3
    H("3.3 Nắp thân van điều khiển", "3.3 Valve Body Bonnets")
    P("Nắp của van điều khiển là phần của cụm thân mà thân nút van hoặc trục quay đi xuyên qua. Trên "
      "thân kiểu cầu hoặc góc, nó là chi tiết chịu áp cho một đầu của thân van. Nắp thường cung cấp "
      "phương tiện để lắp cơ cấu chấp hành vào thân và chứa hộp đệm.",
      "The bonnet of a control valve is that part of the body assembly through which the valve plug "
      "stem or rotary shaft moves. On globe or angle bodies, it is the pressure-retaining component "
      "for one end of the valve body. The bonnet normally provides a means of mounting the actuator "
      "to the body and houses the packing box.")
    P("Nói chung, van quay không có nắp. (Trên một số van quay, bộ đệm được đặt trong phần kéo dài của "
      "chính thân van, hoặc hộp đệm là chi tiết riêng được bắt bulông giữa thân van và nắp.) Trên thân "
      "van điều khiển kiểu cầu điển hình, nắp được làm từ cùng vật liệu với thân van hoặc vật liệu rèn "
      "tương đương vì nó là chi tiết chịu áp chịu cùng nhiệt độ và tác động ăn mòn như thân.",
      "Generally, rotary valves do not have bonnets. (On some rotary valves, the packing is housed "
      "within an extension of the valve body itself, or the packing box is a separate component "
      "bolted between the valve body and bonnet.) On a typical globe-style control valve body, the "
      "bonnet is made of the same material as the valve body or is an equivalent forged material "
      "because it is a pressure-containing member subject to the same temperature and corrosion "
      "effects as the body.")
    P("Một số kiểu nối thân van với nắp được minh họa. Kiểu bích bắt bulông phổ biến nhất được thể "
      "hiện trong Hình 3.19 với nắp có bích liền. Trong van điều khiển quay, bộ đệm thường được đặt "
      "bên trong thân van và không dùng nắp.",
      "Several styles of valve body-to-bonnet connections are illustrated. The most common bolted "
      "flange type is shown in Figure 3.19 of a bonnet with an integral flange. In rotary control "
      "valves, the packing is typically housed within the valve body and a bonnet is not used.")
    FIG(19, F.fig_f3_19())
    P("Các biến thể nắp van được minh họa trong Hình 3.20: nắp thường, nắp kéo dài cho dịch vụ nhiệt "
      "độ cao hoặc thấp và nắp kín bằng ống mềm khi không cho phép rò rỉ. Lựa chọn nắp phù hợp phụ "
      "thuộc vào nhiệt độ, áp suất và yêu cầu làm kín của ứng dụng.",
      "Bonnet variations are illustrated in Figure 3.20: standard, extension for high or low "
      "temperature service, and bellows seal where no leakage can be tolerated. The right bonnet "
      "choice depends on the temperature, pressure and sealing duty of the application.")
    FIG(20, F.fig_f3_20())
    P("Trên thân van điều khiển có trim kiểu lồng hoặc vòng giữ, nắp truyền lực nén để ngăn rò giữa "
      "bích nắp và thân van và giữa vòng chỗ ngồi với thân van. Việc siết bulông thân-nắp nén một tấm "
      "gioăng phẳng để làm kín mối nối thân-nắp, nén gioăng xoắn ốc trên đỉnh lồng và nén một tấm "
      "gioăng phẳng khác dưới vòng chỗ ngồi để làm kín vòng chỗ ngồi với thân. Nắp cũng căn chỉnh cho "
      "lồng, nhờ đó dẫn hướng nút van, đảm bảo căn chỉnh đúng van, nút và thân với bộ đệm và chỗ ngồi.",
      "On control valve bodies with cage- or retainer-style trim, the bonnet furnishes loading force "
      "to prevent leakage between the bonnet flange and the valve body and also between the seat ring "
      "and the valve body. The tightening of the body-bonnet bolting compresses a flat sheet gasket to "
      "seal the body-bonnet joint, compresses a spiral-wound gasket on top of the cage, and compresses "
      "another flat sheet gasket below the seat ring to provide the seat ring-body seal. The bonnet "
      "also provides alignment for the cage, which, in turn, guides the valve plug, to ensure proper "
      "valve, plug, and stem alignment with the packing and seating.")
    P("Như đã đề cập, nắp thông thường trên van điều khiển kiểu cầu chứa bộ đệm. Bộ đệm thường được giữ "
      "bởi bích ép đệm, được cố định tại chỗ bằng bích ở vùng vai ách của nắp (Hình 3.19). Cách giữ bộ "
      "đệm khác là bích ép đệm được giữ bằng đai ốc ren (screwed gland). Cách này gọn nên thường dùng cho van "
      "điều khiển nhỏ; tuy nhiên người dùng không phải lúc nào cũng chắc chắn về mức ăn khớp ren. Do "
      "đó cần thận trọng khi điều chỉnh độ nén đệm khi van đang vận hành.",
      "As mentioned, the conventional bonnet on a globe-type control valve houses the packing. The "
      "packing is most often retained by a packing-follower, held in place by a flange on the yoke "
      "boss area of the bonnet (Figure 3.19). An alternate means of packing retention is where the "
      "packing-follower is held in place by a screwed gland. This alternate is compact, so it is often "
      "used on small control valves; however, the user cannot always be sure of thread engagement. "
      "Therefore, caution should be used in adjusting packing compression when the control valve is "
      "in service.")
    P("Hầu hết nắp kiểu bích bắt bulông có một vùng ở bên hộp đệm có thể khoan và cắt ren. Lỗ này "
      "được bịt bằng nút ống tiêu chuẩn trừ khi có một trong các điều kiện sau:",
      "Most bolted-flange bonnets have an area on the side of the packing box which can be drilled "
      "and tapped. This opening is closed with a standard pipe plug unless one of the following "
      "conditions exists:")
    B(["Cần xả sạch thân van và nắp khỏi chất lỏng quá trình, khi đó lỗ có thể dùng làm đầu nối xả;",
       "Lỗ trên nắp được dùng để phát hiện rò từ bộ đệm thứ nhất hoặc từ ống mềm bị hỏng."],
      ["It is necessary to purge the valve body and bonnet of process fluid, in which case the "
       "opening can be used as a purge connection.",
       "The bonnet opening is being used to detect leakage from the first set of packing or from a "
       "failed bellows seal."])

    H("3.3.1 Nắp kéo dài", "3.3.1 Extension Bonnets", h3)
    P("Nắp kéo dài dùng cho dịch vụ nhiệt độ cao hoặc thấp để bảo vệ bộ đệm thân van khỏi nhiệt độ "
      "quá trình cực đoan. Bộ đệm thân van PTFE tiêu chuẩn dùng được cho hầu hết ứng dụng tới 232 độ C "
      "(450 độ F). Nắp kéo dài đưa hộp đệm ra xa nhiệt độ cực đoan của quá trình đủ để nhiệt độ bộ đệm "
      "duy trì trong dải khuyến nghị.",
      "Extension bonnets are used for either high or low temperature service to protect valve stem "
      "packing from extreme process temperatures. Standard PTFE valve stem packing is useful for most "
      "applications up to 232 deg C (450 deg F). Extension bonnets move the packing box of the bonnet "
      "far enough away from the extreme temperature of the process that the packing temperature "
      "remains within the recommended range.")
    P("Nắp kéo dài có dạng đúc hoặc chế tạo (Hình 3.21). Nắp đúc cho dịch vụ nhiệt độ cao tốt hơn nhờ "
      "độ phát xạ nhiệt lớn hơn, tạo hiệu ứng làm mát tốt hơn. Ngược lại, bề mặt nhẵn — như bề mặt chế "
      "tạo từ ống thép không gỉ — được ưu tiên cho dịch vụ lạnh vì nhiệt xâm nhập thường là mối quan "
      "tâm chính.",
      "Extension bonnets are either cast or fabricated (Figure 3.21). Cast extensions offer better "
      "high-temperature service because of greater heat emissivity, which provides better cooling "
      "effect. Conversely, smooth surfaces–such as those fabricated from stainless steel tubing–are "
      "preferred for cold service because heat influx is typically the major concern.")
    P("Trong cả hai trường hợp, nên giảm độ dày thành nắp kéo dài để cản truyền nhiệt. Thép không gỉ "
      "thường được ưu tiên hơn thép cacbon vì hệ số dẫn nhiệt thấp hơn. Trong ứng dụng dịch vụ lạnh, "
      "có thể thêm vật liệu cách nhiệt quanh phần kéo dài để bảo vệ thêm khỏi nhiệt xâm nhập.",
      "In either case, extension wall thickness should be minimized to cut down heat transfer. "
      "Stainless steel is usually preferable to carbon steel because of its lower coefficient of "
      "thermal conductivity. In cold service applications, insulation can be added around the "
      "extension to protect further against heat influx.")
    FIG(21, F.fig_f3_21())

    H("3.3.2 Nắp kín bằng ống mềm", "3.3.2 Bellows Seal Bonnets", h3)
    P("Nắp kín bằng ống mềm (Hình 3.22) được dùng khi không cho phép rò rỉ dọc thân (dưới 1x10-6 "
      "cc/giây helium). Chúng thường được dùng khi chất lỏng quá trình độc hại, dễ bay hơi, phóng xạ "
      "hoặc rất đắt giá. Kết cấu nắp đặc biệt này bảo vệ cả thân và bộ đệm van khỏi tiếp xúc với chất "
      "lỏng quá trình. Kết cấu hộp đệm tiêu chuẩn hoặc hộp đệm môi trường bên trên cụm ống mềm sẽ ngăn "
      "hỏng sự cố trong trường hợp ống mềm bị vỡ hoặc hỏng.",
      "Bellows seal bonnets (Figure 3.22) are used when no leakage (less than 1x10-6 cc/sec of "
      "helium) along the stem can be tolerated. They are often used when the process fluid is toxic, "
      "volatile, radioactive, or very expensive. This special bonnet construction protects both the "
      "stem and the valve packing from contact with the process fluid. Standard or environmental "
      "packing box constructions above the bellows seal unit will prevent catastrophic failure in "
      "case of rupture or failure of the bellows.")
    P("Cũng như các giới hạn áp suất và nhiệt độ khác của van điều khiển, các cấp áp suất này giảm khi "
      "nhiệt độ tăng. Việc lựa chọn thiết kế ống mềm cần được cân nhắc cẩn thận, đặc biệt chú ý đến "
      "kiểm tra và bảo trì thích hợp sau khi lắp đặt. Vật liệu ống mềm cần được xem xét cẩn thận để đảm "
      "bảo tuổi thọ chu trình tối đa.",
      "As with other control valve pressure and temperature limitations, these pressure ratings "
      "decrease with increasing temperature. Selection of a bellows seal design should be carefully "
      "considered with particular attention to proper inspection and maintenance after installation. "
      "The bellows material should be carefully considered to ensure the maximum cycle life.")
    FIG(22, F.fig_f3_22())
    P("Có hai loại thiết kế ống mềm dùng cho van điều khiển: ống mềm lá hàn và ống mềm tạo hình cơ "
      "khí. Thiết kế lá hàn (Hình 3.23) cho chiều cao tổng ngắn hơn. Do cách chế tạo và thiết kế vốn "
      "có, tuổi thọ dịch vụ có thể bị hạn chế.",
      "Two types of bellows seal designs can be used for control valves. These are welded-leaf and "
      "mechanically-formed bellows. The welded-leaf design (Figure 3.23) offers a shorter total "
      "package height. Due to its method of manufacture and inherent design, service life may be limited.")
    FIG(23, F.fig_f3_23())
    P("Thiết kế tạo hình cơ khí (Hình 3.24) cao hơn theo so sánh và được sản xuất bằng quy trình chế "
      "tạo lặp lại được, do đó độ tin cậy cao hơn.",
      "The mechanically-formed design (Figure 3.24) is taller by comparison and is produced with a "
      "more repeatable manufacturing process and, therefore, higher reliability.")
    FIG(24, F.fig_f3_24())

    # ------------------------------------------------------------ 3.4
    H("3.4 Bộ đệm van điều khiển", "3.4 Control Valve Packing")
    P("Hầu hết van điều khiển dùng hộp đệm với bộ đệm được giữ và điều chỉnh bằng bích và bulông chốt "
      "(thể hiện trong Hình 3.26). Có thể dùng một số vật liệu đệm tùy theo điều kiện dịch vụ dự kiến "
      "và việc ứng dụng có yêu cầu tuân thủ quy định môi trường hay không. Mô tả ngắn gọn và hướng dẫn "
      "điều kiện dịch vụ cho một số vật liệu phổ biến và bố trí vật liệu đệm điển hình được thể hiện "
      "trong Hình 3.24.",
      "Most control valves use packing boxes with the packing retained and adjusted by a flange and "
      "stud bolts (shown in Figure 3.26). Several packing materials can be used, depending on the "
      "service conditions expected and whether the application requires compliance to environmental "
      "regulations. Brief descriptions and service condition guidelines for several popular "
      "materials and typical packing material arrangements are shown in Figure 3.24.")

    H("3.4.1 Vòng V PTFE", "3.4.1 PTFE V-Ring", h3)
    B(["Vật liệu nhựa có khả năng tự giảm ma sát.",
       "Được ép thành các vòng hình V, được nạp lò xo và tự điều chỉnh trong hộp đệm. Không cần bôi "
       "trơn bộ đệm.",
       "Chống lại hầu hết hóa chất đã biết, trừ kim loại kiềm nóng chảy.",
       "Cần bề mặt thân rất nhẵn (2 đến 4 micro-inch RMS) để làm kín đúng. Sẽ rò nếu thân hoặc bề mặt "
       "đệm bị hư hỏng.",
       "Giới hạn nhiệt độ khuyến nghị: -40 đến 232 độ C (-40 đến 450 độ F).",
       "Không phù hợp dịch vụ hạt nhân vì PTFE dễ bị phá hủy bởi bức xạ."],
      ["Plastic material with inherent ability to minimize friction.",
       "Molded in V-shaped rings that are spring-loaded and self-adjusting in the packing box. "
       "Packing lubrication is not required.",
       "Resistant to most known chemicals, except molten alkali metals.",
       "Requires extremely smooth (2 to 4 micro-inches RMS) stem finish to seal properly. Will leak "
       "if stem or packing surface is damaged.",
       "Recommended temperature limits: -40 to 232 deg C (-40 to 450 deg F).",
       "Not suitable for nuclear service because PTFE is easily destroyed by radiation."])

    H("3.4.2 Than chì dạng lá và dạng sợi", "3.4.2 Laminated and Filament Graphite", h3)
    B(["Phù hợp cho mọi dịch vụ nhiệt độ cao và dịch vụ hạt nhân hoặc nơi mong muốn hàm lượng "
       "clorua thấp (Cấp GTN).",
       "Cho vận hành không rò, dẫn nhiệt cao và tuổi thọ dài, nhưng tạo ma sát thân lớn và độ trễ "
       "hysteresis tương ứng.",
       "Không thấm với hầu hết chất lỏng khó xử lý và bức xạ cao.",
       "Dải nhiệt độ phù hợp: nhiệt độ đông lạnh xu tới -198 độ C (-325 độ F).",
       "Không cần bôi trơn, nhưng nên dùng nắp kéo dài hoặc ách thép khi nhiệt độ hộp đệm vượt "
       "427 độ C (800 độ F)."],
      ["Suitable for all high-temperature service and nuclear service or where low chloride content "
       "is desirable (Grade GTN).",
       "Provides leak-free operation, high-thermal conductivity, and long service life, but produces "
       "high stem friction and resultant hysteresis.",
       "Impervious to most hard-to-handle fluids and high radiation.",
       "Suitable temperature range: cryogenic temperatures down to -198 deg C (-325 deg F).",
       "Lubrication is not required, but an extension bonnet or steel yoke should be used when packing "
       "box temperature exceeds 427 deg C (800 deg F)."])

    H("3.4.3 Yêu cầu quy định của Hoa Kỳ về khí thải bay hơi",
      "3.4.3 U.S. Regulatory Requirements for Fugitive Emissions", h3)
    P("Khí thải bay hơi (fugitive emissions) là phát thải hữu cơ dễ bay hơi từ nguồn không điểm phát "
      "sinh do rò rỉ thiết bị quá trình. Người ta ước tính rò rỉ thiết bị tại Hoa Kỳ vượt quá 400 "
      "triệu pound mỗi năm. Các quy định nghiêm ngặt của chính phủ do Hoa Kỳ xây dựng quy định các "
      "chương trình phát hiện và sửa rò rỉ (LDAR). Van và bơm đã được xác định là nguồn chính của khí "
      "thải bay hơi. Đối với van, đó là rò ra khí quyển do hỏng gioăng đệm hoặc gioăng.",
      "Fugitive emissions are non-point source volatile organic emissions which result from process "
      "equipment leaks. Equipment leaks in the United States have been estimated at over 400 million "
      "pounds per year. Strict government regulations, developed by the US, dictate leak detection "
      "and repair programs (LDAR). Valves and pumps have been identified as key sources of fugitive "
      "emissions. For valves, this is the leakage to atmosphere due to packing seal or gasket failures.")
    P("Các chương trình LDAR yêu cầu ngành công nghiệp giám sát tất cả van (điều khiển và không điều "
      "khiển) theo khoảng thời gian xác định bởi tỷ lệ phần trăm van được phát hiện rò vượt ngưỡng "
      "500 ppmv (một số thành phố dùng tiêu chí 100 ppmv). Mức rò này rất nhỏ đến mức không nhìn thấy "
      "hay nghe thấy. Cần dùng thiết bị giám sát di động tinh vi để phát hiện. Việc phát hiện được "
      "thực hiện bằng cách ngửi vùng đệm van để tìm rò theo quy trình của Cơ quan Bảo vệ Môi trường "
      "(EPA). Đây là quá trình tốn kém và nặng nề cho ngành công nghiệp.",
      "The LDAR programs require industry to monitor all valves (control and non-control) at an "
      "interval that is determined by the percentage of valves found to be leaking above a threshold "
      "level of 500 ppmv (some cities use a 100 ppmv criteria). This leakage level is so slight you "
      "cannot see or hear it. The use of sophisticated portable monitoring equipment is required for "
      "detection. Detection occurs by sniffing the valve packing area for leakage using an "
      "Environmental Protection Agency (EPA) protocol. This is a costly and burdensome process for "
      "industry.")
    P("Các quy định cho phép kéo dài chu kỳ giám sát tới một năm nếu cơ sở chứng minh được tỷ lệ van rò "
      "liên tục rất thấp (dưới 0,5% tổng số van). Cơ hội kéo dài tần suất đo được thể hiện trong Hình 3.25.",
      "The regulations do allow for the extension of the monitoring period for up to one year if the "
      "facility can demonstrate a very low ongoing percentage of leaking valves (less than 0.5% of "
      "the total valve population). The opportunity to extend the measurement frequency is shown in "
      "Figure 3.25.")
    FIG(25, F.fig_f3_25())
    P("Các hệ thống đệm được thiết kế cho yêu cầu rò cực thấp cũng kéo dài tuổi thọ và hiệu năng làm "
      "kín để hỗ trợ mục tiêu giám sát hàng năm. Hệ thống đệm ENVIRO-SEAL là một ví dụ. Các gioăng "
      "nâng cao của hệ thống này gồm bốn nguyên tắc thiết kế chính: chứa vật liệu làm kín dẻo qua chi "
      "tiết chống ép ra, căn chỉnh đúng thân hoặc trục trong lỗ nắp, áp dụng ứng suất đệm không đổi "
      "qua lò xo Belleville và giảm số vòng làm kín để hạn chế nén chặt, ma sát và giãn nở nhiệt.",
      "Packing systems designed for extremely low leakage requirements also extend packing-seal life "
      "and performance to support an annual monitoring objective. The ENVIRO-SEAL packing system is "
      "one example. Its enhanced seals incorporate four key design principles: the containment of "
      "the pliable seal material through an anti-extrusion component, proper alignment of the valve "
      "stem or shaft within the bonnet bore, applying a constant packing stress through Belleville "
      "springs, and minimizing the number of seal rings to reduce consolidation, friction, and "
      "thermal expansion.")
    P("Quy trình chọn van truyền thống nghĩa là chọn thiết kế van dựa trên khả năng áp suất và nhiệt "
      "độ, đặc tính dòng và khả năng tương thích vật liệu. Loại đệm thân van dùng trong van được xác "
      "định chủ yếu bằng nhiệt độ tại vùng hộp đệm. Các lựa chọn vật liệu sẵn có gồm PTFE cho nhiệt độ "
      "dưới 93 độ C (200 độ F) và than chì cho ứng dụng nhiệt độ cao hơn. Ngày nay, việc chọn hệ "
      "thống đệm van trở nên phức tạp hơn nhiều do nhiều cân nhắc.",
      "The traditional valve selection process meant choosing a valve design based on its pressure "
      "and temperature capabilities, flow characteristics, and material compatibility. Which valve "
      "stem packing to use in the valve was determined primarily by the operating temperature in the "
      "packing box area. The available material choices included PTFE for temperatures below "
      "93 deg C (200 deg F) and graphite for higher-temperature applications. Today, choosing a valve "
      "packing system has become much more involved due to a number of considerations.")

    H("3.4.4 Tiêu chuẩn toàn cầu về khí thải bay hơi",
      "3.4.4 Global Standards for Fugitive Emissions", h3)
    P("ISO 15848 là tiêu chuẩn của Tổ chức Tiêu chuẩn hóa Quốc tế (ISO) về đo lường, thử nghiệm và "
      "quy trình đánh giá khí thải bay hơi của van công nghiệp. ISO 15848-1 là hệ thống phân loại và "
      "đánh giá thử nghiệm kiểu cho van, được tạo ra để cho phép phân loại hiệu năng của các thiết kế "
      "khí thải bay hơi khác nhau và xác định thử nghiệm kiểu dùng để đánh giá và đánh giá van khi "
      "có quy định tiêu chuẩn khí thải bay hơi.",
      "ISO 15848 is the International Organization for Standardization's (ISO) standard for "
      "measurement, test, and qualification procedures for fugitive emissions of industrial valves. "
      "ISO 15848-1 is a classification system and qualification for type testing of valves that was "
      "created to enable classification of performance of different fugitive emission designs and to "
      "define the type test for evaluation and qualification of valves where fugitive emissions "
      "standards are specified.")
    P("Thử nghiệm kiểu nghĩa là thử nghiệm đánh giá được thực hiện trên một thiết kế van và hệ thống "
      "đệm, và mọi đánh giá đều được chuyển sang tất cả van sản xuất theo thiết kế đệm đó. Thử nghiệm "
      "kiểu khác với thử nghiệm sản xuất ISO 15848-2, là thử nghiệm đánh giá thực hiện tại thời điểm "
      "lắp ráp và có thể được yêu cầu cho nhiều cụm van.",
      "Type testing means that the qualification test is performed on one valve and packing system "
      "design and any qualification is passed on to all valves produced to that packing design. Type "
      "testing differs from ISO 15848-2 production testing, which is a qualification test done at the "
      "time of assembly and can be dictated for more than one valve assembly.")
    P("ISO 15848-1 bao gồm cả van điều khiển và van cô lập (đóng mở). Yêu cầu chu trình cơ khí của hai "
      "loại van khác nhau, như thể hiện trong Hình 3.26. Chu trình cơ khí được thực hiện ở 10% hành "
      "trình đầy đủ ở cả hai phía của vị trí 50% đối với van điều khiển và full stroke đối với van cô "
      "lập. Giống như các tiêu chuẩn khí thải bay hơi khác, ISO 15848-1 quy định thử nghiệm đánh giá "
      "gồm nhiều tổ hợp cấp rò, chu trình nhiệt và chu trình cơ khí. Có một số khác biệt đáng chú ý "
      "giữa ISO 15848-1 và yêu cầu, tiêu chuẩn có nguồn gốc từ chính phủ Hoa Kỳ như LDAR và tiêu "
      "chuẩn ANSI/FCI 91-1 về đánh giá gioăng thân van điều khiển.",
      "ISO 15848-1 covers both control valves and isolation (on/off) valves. The mechanical cycle "
      "requirements for the two types of valves differ, as shown in Figure 3.26. Mechanical cycles "
      "are performed at 10% of full travel on both sides of the 50% travel position for control "
      "valves and full stroke for isolation valves. Like other fugitive emission standards, ISO "
      "15848-1 lays out a qualification test that includes several combinations of leakage classes, "
      "thermal cycles, and mechanical cycles. There are several notable differences between ISO "
      "15848-1 and government requirements and standards of US origin such as LDAR and ANSI/FCI "
      "91-1 standard for qualification of control valve stem seals.")
    FIG(26, F.fig_f3_26())
    P("ANSI/FCI 91-1 yêu cầu <i>phương pháp ngửi</i> theo EPA Method 21 để đọc nồng độ <i>ppm</i> và "
      "viện dẫn 100ppm và 500ppm với các cấp chu trình khác nhau, như thể hiện trong Hình 3.29. ISO "
      "15848-1 quy định phương pháp đo <i>tổng rò</i> bằng chân không hoặc dây chuyền (flushing) được "
      "mô tả trong Phụ lục A của tiêu chuẩn. Rò được ghi thành tỷ lệ rò theo kích thước thân đo được. "
      "Không phương pháp nào trong hai phương pháp này tương quan được với EPA Method 21 (phương pháp "
      "ngửi) và ISO 15848-1 nêu rõ không có ý định tương quan giữa các cấp độ kín khi chất lỏng thử là "
      "helium và khi chất lỏng thử là methane. Xem Hình 3.27 và 3.28.",
      "ANSI/FCI 91-1 requires the <i>sniffing method</i> per EPA Method 21 for a <i>ppm</i> "
      "concentration reading and cites 100ppm and 500ppm with various cycle classes, as shown in "
      "Figure 3.29. ISO 15848-1 specifies either the vacuum or flushing <i>total leakage</i> "
      "measurement methods described in Annex A of the standard. Leakage is recorded as a leakage "
      "rate per measured stem size. Neither of these methods can be correlated with EPA Method 21 "
      "(sniffing method) and ISO 15848-1 states there is no correlation intended between the "
      "tightness classes when the test fluid is helium and when the test fluid is methane. See "
      "Figures 3.27 and 3.28.")
    FIG(27, F.fig_f3_27())
    FIG(28, F.fig_f3_28())
    FIG(29, F.fig_f3_29())
    P("Ngày nay, việc chọn hệ thống đệm van trở nên phức tạp hơn nhiều do nhiều cân nhắc. Ví dụ, yêu "
      "cầu kiểm soát phát thải — như những yêu cầu do Clean Air Act tại Hoa Kỳ và ISO 15848 trên phạm "
      "vi toàn cầu — đặt ra giới hạn chặt chẽ hơn về hiệu năng làm kín. Những đòi hỏi liên tục cải "
      "thiện sản lượng quá trình có nghĩa là hệ thống đệm van không được cản trở hiệu năng van. Và "
      "xu hướng hiện nay hướng tới chu kỳ bảo trì kéo dài đòi hỏi hệ thống đệm van phải cung cấp độ "
      "kín cần thiết trong thời gian dài hơn.",
      "Today, choosing a valve packing system has become much more involved due to a number of "
      "considerations. For example, emissions control requirements–such as those specified by the "
      "Clean Air Act within the US and ISO 15848 on a global basis–place tighter restrictions on "
      "sealing performance. Constant demands for improved process output mean that the valve packing "
      "system must not hinder valve performance. And today's trend toward extended maintenance "
      "schedules dictates that valve packing systems provide the required sealing over longer periods.")
    P("Với nhiều ứng dụng và điều kiện dịch vụ đa dạng trong công nghiệp, các biến số này (khả năng làm "
      "kín, mức ma sát vận hành, tuổi thọ vận hành) khó định lượng và so sánh. Hình 3.31 và 3.32 dùng "
      "cách tiếp cận kỹ thuật để đánh giá tương đối tính phù hợp và hiệu năng của bộ đệm. Nhưng trước "
      "hết, việc hiểu đúng các bảng đòi hỏi làm rõ tên thương mại.",
      "Given the wide variety of valve applications and service conditions within industry, these "
      "variables (sealing ability, operating friction levels, operating life) are difficult to "
      "quantify and compare. Figures 3.31 and 3.32 use an engineered approach in providing a "
      "relative evaluation of packing applicability and performance. But first, proper understanding "
      "of the tables requires a clarification of trade names.")

    H("3.4.5 Đệm V-Ring PTFE đơn", "3.4.5 Single PTFE V-Ring Packing", h3)
    P("Bố trí V-ring PTFE đơn dùng lò xo giữa bộ đệm và vòng hộp đệm. Nó đáp ứng tiêu chí 100 ppmv cho "
      "van thân trượt, giả thiết áp suất không vượt quá 300 psi (20,7 bar) và nhiệt độ giữa -18 độ C "
      "và 93 độ C (0 độ F và 200 độ F). Đệm V-ring PTFE đơn không có tiêu chí phát thải thấp cho van "
      "quay. Nó cho hiệu năng làm kín rất tốt với ma sát vận hành thấp nhất. Xem Hình 3.30.",
      "The single PTFE V-ring arrangement uses a coil spring between the packing and packing box "
      "ring. It meets the 100 ppmv criteria for sliding-stem valves, assuming that the pressure does "
      "not exceed 300 psi (20.7 bar) and the temperature is between -18 deg C and 93 deg C (0 deg F "
      "and 200 deg F). Single PTFE V-ring packing does not come with low emissions criteria for "
      "rotary valves. It offers very good sealing performance with the lowest operating friction. "
      "See Figure 3.30.")
    FIG(30, F.fig_f3_30())

    H("3.4.6 Đệm PTFE ENVIRO-SEAL", "3.4.6 ENVIRO-SEAL PTFE Packing", h3)
    P("Hệ thống đệm PTFE ENVIRO-SEAL là phương pháp đệm tiên tiến dùng thiết kế lò xo tải trực tiếp "
      "gọn, phù hợp cho ứng dụng môi trường tới 750 psi và 232 độ C (51,7 bar và 450 độ F). Dù thường "
      "được coi là hệ thống đệm giảm phát thải, đệm PTFE ENVIRO-SEAL cũng phù hợp cho ứng dụng không "
      "thuộc môi trường với nhiệt độ và áp suất cao, mang lợi ích tuổi thọ dịch vụ dài hơn liên tục ở "
      "cả van thân trượt lẫn van quay. Xem Hình 3.31.",
      "The ENVIRO-SEAL PTFE packing system is an advanced packing method that utilizes a compact, "
      "live-load spring design suited to environmental applications up to 750 psi and 232 deg C "
      "(51.7 bar and 450 deg F). While it is typically thought of as an emission-reducing packing "
      "system, ENVIRO-SEAL PTFE packing is also suited to non-environmental applications involving "
      "high temperatures and pressures, yielding the benefit of longer, ongoing service life in both "
      "sliding-stem and rotary valves. See Figure 3.31.")
    FIG(31, F.fig_f3_31())

    H("3.4.7 Đệm kép ENVIRO-SEAL", "3.4.7 ENVIRO-SEAL Duplex Packing", h3)
    P("Hệ thống đệm đặc biệt này cung cấp khả năng của cả thành phần PTFE và than chì, cho giải pháp "
      "ma sát thấp, phát thải thấp, đã thử lửa (API Standard 589) cho ứng dụng có nhiệt độ quá trình "
      "tới 232 độ C (450 độ F) ở van thân trượt. Van quay không có sẵn đệm kép ENVIRO-SEAL. Xem Hình 3.32.",
      "This special packing system provides the capabilities of both PTFE and graphite components to "
      "yield a low friction, low emission, fire-tested solution (API Standard 589) for applications "
      "with process temperatures up to 232 deg C (450 deg F) in sliding-stem valves. Rotary valves "
      "are not available with ENVIRO-SEAL Duplex packing. See Figure 3.32.")
    FIG(32, F.fig_f3_32())

    H("3.4.8 Đệm PTFE ISO-Seal", "3.4.8 ISO-Seal PTFE Packing", h3)
    P("Hệ thống đệm này được thiết kế cho áp suất vượt quá khả năng của đệm PTFE ENVIRO-SEAL trong "
      "dịch vụ môi trường. Nó có sẵn để dùng ở cả van thân trượt lẫn van quay.",
      "This packing system is designed for pressures exceeding the capabilities of ENVIRO-SEAL PTFE "
      "packing for environmental service. It is available for use in both sliding-stem and rotary valves.")

    H("3.4.9 Than chì ULF ENVIRO-SEAL", "3.4.9 ENVIRO-SEAL Graphite ULF", h3)
    P("Hệ thống đệm này được thiết kế chủ yếu cho ứng dụng môi trường ở nhiệt độ trên 232 độ C "
      "(450 độ F). Hệ thống đệm ULF được cấp bằng sáng chế gồm các lớp PTFE rất mỏng bên trong vòng "
      "đệm, cũng như các vòng đệm PTFE mỏng ở mỗi bên của vòng đệm. Cách bố trí chiến lược này của "
      "PTFE giúp giảm vấn đề điều khiển, giảm ma sát, hỗ trợ làm kín và kéo dài tuổi thọ chu trình của "
      "bộ đệm. Xem Hình 3.33.",
      "This packing system is designed primarily for environmental applications at temperatures in "
      "excess of 232 deg C (450 deg F). The patented ULF packing system incorporates very thin PTFE "
      "layers inside the packing rings as well as thin PTFE washers on each side of the packing rings. "
      "This strategic placement of PTFE minimizes control problems, reduces friction, promotes "
      "sealing and extends the cycle life of the packing set. See Figure 3.33.")
    FIG(33, F.fig_f3_33())

    H("3.4.10 Than chì ULF HIGH-SEAL", "3.4.10 HIGH-SEAL Graphite ULF", h3)
    P("Giống hệt hệ thống đệm than chì ULF ENVIRO-SEAL bên dưới bích ép đệm, hệ thống HIGH-SEAL dùng "
      "lò xo Belleville cỡ lớn, đường kính lớn chịu lực nặng. Các lò xo này cung cấp thêm hành trình "
      "cho bích ép và có thể hiệu chỉnh bằng thang tải để có chỉ thị trực quan về tải và độ mòn của bộ đệm.",
      "Identical to the ENVIRO-SEAL graphite ULF packing system below the packing-follower, the "
      "HIGH-SEAL system utilizes heavy-duty, large diameter Belleville springs. These springs provide "
      "additional follower travel and can be calibrated with a load scale for a visual indication of "
      "packing load and wear.")

    H("3.4.11 Đệm than chì ISO-Seal", "3.4.11 ISO-Seal Graphite Packing", h3)
    P("Hệ thống đệm này được thiết kế cho nhiệt độ vượt quá khả năng của đệm than chì ULF ENVIRO-SEAL. "
      "Nó có thể dùng từ -46 đến 400 độ C (-50 đến 752 độ F) cho dịch vụ môi trường. Có sẵn cho cả "
      "van thân trượt lẫn van quay.",
      "This packing system is designed for temperatures exceeding the capabilities of ENVIRO-SEAL "
      "Graphite ULF packing. It can be used from -46 to 400 deg C (-50 to 752 deg F) for environmental "
      "service. It is available for use in both sliding-stem and rotary valves.")

    H("3.4.12 Than chì ENVIRO-SEAL cho van quay",
      "3.4.12 ENVIRO-SEAL Graphite for Rotary Valves", h3)
    P("Đệm than chì ENVIRO-SEAL được thiết kế cho ứng dụng môi trường từ -6 đến 316 độ C (20 đến "
      "600 độ F) hoặc cho những ứng dụng cần an toàn cháy. Nó có thể dùng với áp suất tới 1500 psi "
      "(103 bar) mà vẫn đạt tiêu chí rò 100 ppmv của EPA. Bộ đệm có thể dùng tới 371 độ C (700 độ F) "
      "nếu dùng trong ứng dụng không thuộc môi trường. Xem Hình 3.34.",
      "ENVIRO-SEAL graphite packing is designed for environmental applications from -6 to 316 deg C "
      "(20 to 600 deg F) or for those applications where fire safety is a concern. It can be used "
      "with pressures up to 1500 psi (103 bar) and still satisfy the 100 ppmv EPA leakage criteria. "
      "The packing can be used up to 371 deg C (700 deg F) if used in non-environmental applications. "
      "See Figure 3.34.")
    FIG(34, F.fig_f3_34())

    H("3.4.13 Băng than chì cho van quay", "3.4.13 Graphite Ribbon for Rotary Valves", h3)
    P("Đệm băng than chì được thiết kế cho ứng dụng không thuộc môi trường với dải nhiệt độ rộng, từ "
      "-198 đến 538 độ C (-325 đến 1000 độ F).",
      "Graphite ribbon packing is designed for non-environmental applications that span a wide "
      "temperature range, from -198 to 538 deg C (-325 to 1000 deg F).")

    H("3.4.14 Lựa chọn đệm môi trường cho thân trượt",
      "3.4.14 Sliding-Stem Environmental Packing Selection", h3)
    P("Hình 3.35 cung cấp so sánh các lựa chọn đệm thân trượt khác nhau và xếp hạng tương đối về hiệu "
      "năng làm kín, tuổi thọ dịch vụ và ma sát đệm cho ứng dụng môi trường. Sợi than chì bện và PTFE "
      "kép không phải giải pháp làm kín môi trường chấp nhận được.",
      "Figure 3.35 provides a comparison of various sliding-stem packing selections and a relative "
      "ranking of seal performance, service life, and packing friction for environmental applications. "
      "Braided graphite filament and double PTFE are not acceptable environmental sealing solutions.")
    FIG(35, F.fig_f3_35())

    H("3.4.15 Lựa chọn đệm môi trường cho van quay",
      "3.4.15 Rotary Environmental Packing Selection", h3)
    P("Hình 3.36 áp dụng cho van quay. Trong trường hợp van quay, bố trí đệm PTFE đơn và băng than chì "
      "không hoạt động tốt như giải pháp làm kín khí thải bay hơi.",
      "Figure 3.36 applies to rotary valves. In the case of rotary valves, single PTFE and graphite "
      "ribbon packing arrangements do not perform well as fugitive emission sealing solutions.")
    P("Kiểm soát khí thải bay hơi của van và giảm chi phí tuân thủ quy định của ngành có thể đạt được "
      "thông qua các công nghệ làm kín thân này. Dù hệ thống đệm ENVIRO-SEAL được thiết kế riêng cho "
      "ứng dụng khí thải bay hơi, các công nghệ này cũng nên được cân nhắc cho bất kỳ ứng dụng nào mà "
      "hiệu năng và tuổi thọ làm kín là mối bận tâm liên tục hoặc vấn đề chi phí bảo trì.",
      "The control of valve fugitive emissions and a reduction in industry's cost of regulatory "
      "compliance can be achieved through these stem sealing technologies. While ENVIRO-SEAL packing "
      "systems have been designed specifically for fugitive emission applications, these technologies "
      "also should be considered for any application where seal performance and seal life have been "
      "an ongoing concern or maintenance cost issue.")
    FIG(36, F.fig_f3_36())

    # ------------------------------------------------------------ 3.5
    H("3.5 Định hình dòng cho thân van dẫn hướng bằng lồng",
      "3.5 Characterization of Cage-Guided Valve Bodies")
    P("Trong thân van có trim dẫn hướng bằng lồng, hình dạng của các lỗ dòng hay cửa sổ trên thành của "
      "lồng hình trụ quyết định định hình dòng. Khi nút van dịch chuyển ra khỏi vòng chỗ ngồi, cửa sổ "
      "lồng được mở ra cho phép dòng chảy qua van. Các lồng tiêu chuẩn được thiết kế để tạo các đặc "
      "tính dòng vốn có tuyến tính, phần trăm bằng và mở nhanh. Định hình tùy biến cũng có thể có sẵn. "
      "Lưu ý sự khác biệt về hình dạng cửa sổ lồng trong Hình 3.37. Quan hệ lưu lượng/hành trình do van "
      "dùng các lồng này tạo ra là một trong các đường cong tuyến tính, mở nhanh hoặc phần trăm bằng "
      "thể hiện cho nút van định hình (Hình 3.38).",
      "In valve bodies with cage-guided trim, the shape of the flow openings or windows in the wall "
      "of the cylindrical cage determines flow characterization. As the valve plug is moved away from "
      "the seat ring, the cage windows are opened to permit flow through the valve. Standard cages "
      "have been designed to produce linear, equal-percentage, and quick-opening inherent flow "
      "characteristics. Custom characterization may also be available. Note the differences in the "
      "shapes of the cage windows shown in Figure 3.37. The flow rate/travel relationship provided "
      "by valves using these cages is either the linear, quick-opening, or equal-percentage curves "
      "shown for contoured valve plugs (Figure 3.38).")
    P("Trim dẫn hướng bằng lồng cho phép dễ dàng thay đổi đặc tính dòng vốn có của van bằng cách lắp "
      "một lồng khác. Việc đổi lồng để tạo đặc tính dòng vốn có khác không yêu cầu thay nút van hay "
      "vòng chỗ ngồi. Các lồng tiêu chuẩn thể hiện có thể dùng cho cả trim cân bằng và mất cân bằng. "
      "Đệm mềm, khi cần, có sẵn dạng chi tiết chèn giữ trong vòng chỗ ngồi và độc lập với lựa chọn "
      "lồng hay nút van.",
      "Cage-guided trim allows for the inherent flow characteristic of the valve to be easily changed "
      "by installing a different cage. Interchange of cages to provide a different inherent flow "
      "characteristic does not require changing the valve plug or seat ring. The standard cages shown "
      "can be used with either balanced or unbalanced trim constructions. Soft seating, when "
      "required, is available as a retained insert in the seat ring and is independent of cage or "
      "valve plug selection.")
    P("Khả năng thay thế lồng có thể mở rộng sang thiết kế lồng chuyên dụng giảm tiếng ồn hoặc chống "
      "sủi bọt. Các lồng này thường cho đặc tính dòng vốn có tuyến tính nhưng yêu cầu dòng chảy theo "
      "một hướng cụ thể qua các lỗ lồng. Do đó có thể cần đảo thân van trong đường ống để có hướng "
      "dòng đúng.",
      "Cage interchangeability can be extended to specialized cage designs that provide noise "
      "attenuation or combat cavitation. These cages typically furnish a linear inherent flow "
      "characteristic, but require flow to be in a specific direction through the cage openings. "
      "Therefore, it could be necessary to reverse the valve body in the pipeline to obtain proper "
      "flow direction.")
    FIG(37, F.fig_f3_37())
    FIG(38, F.fig_f3_38())

    H("3.5.1 Nút van định hình", "3.5.1 Characterized Valve Plugs", h3)
    P("Nút van, phần chuyển động của cụm van điều khiển kiểu cầu, tạo ra sự hạn chế thay đổi đối với "
      "dòng chảy của chất lỏng. Mỗi kiểu nút van được thiết kế để tạo một đặc tính dòng cụ thể, cho "
      "phép một cách dẫn hướng hoặc căn chỉnh xác định với vòng chỗ ngồi, hoặc có khả năng đóng chặt "
      "hoặc chống hư hỏng đặc thù.",
      "The valve plug, the movable part of a globe-style control valve assembly, provides a variable "
      "restriction to fluid flow. Valve plug styles are each designed to provide a specific flow "
      "characteristic, permit a specified manner of guiding or alignment with the seat ring, or have "
      "a particular shutoff or damage-resistance capability.")
    P("Đường bao của bề mặt nút van cạnh vòng chỗ ngồi đóng vai trò quyết định đặc tính dòng vốn có của "
      "van điều khiển định hình bằng nút. Khi cơ cấu chấp hành di chuyển nút van trong suốt hành trình "
      "của nó, diện tích dòng không bị cản thay đổi về kích thước và hình dạng tùy theo đường bao của "
      "nút van.",
      "The contour of the valve plug surface next to the seat ring is instrumental in determining "
      "the inherent flow characteristic of a plug-characterized control valve. As the actuator moves "
      "the valve plug through its travel range, the unobstructed flow area changes in size and shape "
      "depending on the contour of the valve plug.")
    FIG(39, F.fig_f3_39())
    P("Khi duy trì chênh áp không đổi qua van, có thể mô tả quan hệ thay đổi giữa phần trăm năng lực "
      "dòng tối đa và phần trăm tổng phạm vi hành trình (Hình 3.38), và được gọi là đặc tính dòng vốn "
      "có của van. Các đặc tính dòng vốn có thường được chỉ định gồm tuyến tính, phần trăm bằng và mở "
      "nhanh. Chúng được mô tả thêm trong Chương 5.",
      "When a constant pressure differential is maintained across the valve, the changing "
      "relationship between percentage of maximum flow capacity and percentage of total travel range "
      "can be portrayed (Figure 3.38), and is designated as the inherent flow characteristic of the "
      "valve. Commonly specified inherent flow characteristics include linear, equal-percentage, and "
      "quick-opening. These are described further in Chapter 5.")
    FIG(40, F.fig_f3_40())

    # ------------------------------------------------------------ 3.6
    H("3.6 Dẫn hướng nút van", "3.6 Valve Plug Guiding")
    P("Dẫn hướng chính xác nút van là cần thiết để căn chỉnh đúng với vòng chỗ ngồi và điều khiển hiệu "
      "quả chất lỏng quá trình. Các phương pháp thường dùng và tên gọi của chúng nhìn chung tự giải "
      "thích.",
      "Accurate guiding of the valve plug is necessary for proper alignment with the seat ring and "
      "efficient control of the process fluid. The common methods used and their names are generally "
      "self-descriptive.")
    B(["Dẫn hướng bằng lồng: Đường kính ngoài của nút van sát với bề mặt thành trong của lồng hình trụ "
       "suốt phạm vi hành trình. Vì nắp, lồng và vòng chỗ ngồi tự căn chỉnh trong cụm, nên đảm bảo "
       "nút van và vòng chỗ ngồi căn chỉnh đúng khi van đóng.",
       "Dẫn hướng trên và dưới: Nút van được căn chỉnh bằng bạc dẫn trong nắp và bích dưới (xem Hình "
       "3.5). Kiểu này thường thấy trong kết cấu hai cổng.",
       "Dẫn hướng bằng cổng: Nút van được căn chỉnh bằng cổng của thân van."],
      ["Cage-Guiding: The outside diameter of the valve plug is close to the inside wall surface of "
       "the cylindrical cage throughout the travel range. Since the bonnet, cage, and seat ring are "
       "self-aligning on the assembly, correct valve plug and seat ring alignment is assured when the "
       "valve closes.",
       "Top- and Bottom-Guiding: The valve plug is aligned by guide bushings in the bonnet and bottom "
       "flange (see Figure 3.5). This is typically found in double-ported constructions.",
       "Port-Guiding: The valve plug is aligned by the valve body port."])
    FIG(41, F.fig_f3_41())

    # ------------------------------------------------------------ 3.7
    H("3.7 Trim van điều khiển năng lực hạn chế",
      "3.7 Restricted-Capacity Control Valve Trim")
    P("Hầu hết nhà sản xuất van điều khiển có thể cung cấp van có chi tiết trim giảm hoặc hạn chế năng "
      "lực. Lưu lượng giảm có thể mong muốn vì một trong các lý do sau:",
      "Most control valve manufacturers can provide valves with reduced- or restricted-capacity trim "
      "parts. The reduced flow rate might be desirable for any of the following reasons:")
    B(["Trim năng lực hạn chế có thể cho phép chọn thân van đủ lớn cho nhu cầu lưu lượng tăng trong "
       "tương lai, nhưng với năng lực trim phù hợp; nắp, lồng và vòng chỗ ngồi tự căn chỉnh trong cụm, "
       "nút van và vòng chỗ ngồi căn chỉnh đúng khi van đóng.",
       "Dẫn hướng trên: nút van được căn chỉnh bằng một bạc dẫn duy nhất trong nắp hoặc thân van, hoặc "
       "bằng cách bố trí bộ đệm.",
       "Dẫn hướng bằng thân: nút van được căn chỉnh với vòng chỗ ngồi bằng bạc dẫn trong nắp tác dụng "
       "lên thân nút van.",
       "Thân van lớn với trim năng lực hạn chế có thể dùng để giảm vận tốc chất lỏng đầu vào và đầu ra.",
       "Có thể tránh mua các đoạn thu nhỏ đường ống đắt tiền.",
       "Lỗi chọn quá cỡ có thể được sửa bằng cách dùng chi tiết trim năng lực hạn chế."],
      ["Restricted capacity trim may make it possible to select a valve body large enough for "
       "increased future flow requirements, but with trim capacity; the bonnet, cage, and seat ring "
       "are self-aligning on the assembly, correct valve plug and seat ring alignment is assured when "
       "the valve closes.",
       "Top-Guiding: the valve plug is aligned by a single guide bushing in the bonnet or valve body, "
       "or by the packing arrangement.",
       "Stem-Guiding: the valve plug is aligned with the seat ring by a guide bushing in the bonnet "
       "that acts on the valve plug stem.",
       "Large bodies with restricted-capacity trim can be used to reduce inlet and outlet fluid velocities",
       "Purchase of expensive pipeline reducers can be avoided.",
       "Over-sizing errors can be corrected by use of restricted-capacity trim parts."])
    P("Thân van kiểu cầu thông thường có thể lắp vòng chỗ ngồi với cỡ cổng nhỏ hơn bình thường và nút "
      "van được định cỡ để khớp với các cổng nhỏ hơn đó. Van có trim dẫn hướng bằng lồng thường đạt "
      "hiệu ứng năng lực giảm bằng cách dùng nút, lồng và vòng chỗ ngồi từ cỡ van nhỏ hơn có kết cấu "
      "tương tự, cùng các đoạn chuyển tiếp phía trên lồng và dưới vòng chỗ ngồi để ghép các chi tiết "
      "nhỏ hơn với thân van (Hình 3.42). Vì dịch vụ năng lực giảm không phải là hiếm, hầu hết nhà sản "
      "xuất cung cấp sẵn các tổ hợp chi tiết trim để thực hiện chức năng yêu cầu.",
      "Conventional globe-style valve bodies can be fitted with seat rings with smaller port sizes "
      "than normal and valve plugs sized to fit those smaller ports. Valves with cage-guided trim "
      "often achieve the reduced-capacity effect by using valve plug, cage, and seat ring parts from "
      "a smaller valve size of similar construction and adapter pieces above the cage and below the "
      "seat ring to mate those smaller parts with the valve body (Figure 3.42). Because reduced "
      "capacity service is not unusual, most manufacturers provide readily available trim part "
      "combinations to perform the required function.")
    FIG(42, F.fig_f3_42())

    # ------------------------------------------------------------ 3.8
    H("3.8 Cơ cấu chấp hành", "3.8 Actuators")
    P("Cơ cấu chấp hành van điều khiển chạy bằng khí nén là loại phổ biến nhất đang dùng, nhưng cơ cấu "
      "điện, thủy lực và bằng tay cũng được dùng rộng rãi. Cơ cấu khí nén màng-lò xo được chỉ định "
      "nhiều nhất nhờ độ tin cậy và thiết kế đơn giản. Cơ cấu piston chạy khí nén cho lực đẩy thân lớn "
      "cho điều kiện dịch vụ khắt khe. Có sẵn biến thể của cả cơ cấu màng-lò xo và piston khí nén để "
      "lắp trực tiếp lên van điều khiển quay.",
      "Pneumatically-operated control valve actuators are the most popular type in use, but electric, "
      "hydraulic, and manual actuators are also widely used. The spring-and-diaphragm pneumatic "
      "actuator is most commonly specified due to its dependability and simplicity of design. "
      "Pneumatically-operated piston actuators provide high stem force output for demanding service "
      "conditions. Adaptations of both spring-and-diaphragm and pneumatic piston actuators are "
      "available for direct installation on rotary control valves.")

    H("3.8.1 Cơ cấu màng", "3.8.1 Diaphragm Actuators", h3)
    B(["Cơ cấu màng chạy khí nén dùng khí cấp từ bộ điều khiển, bộ định vị hoặc nguồn khác.",
       "Các kiểu gồm: tác động trực tiếp, trong đó áp suất khí tăng đẩy màng xuống và dãn thân cơ cấu "
       "(Hình 3.43).",
       "Tác động ngược, trong đó áp suất khí tăng đẩy màng lên và co thân cơ cấu (Hình 3.43).",
       "Có thể đảo chiều, trong đó cơ cấu có thể lắp để tác động trực tiếp hoặc ngược (Hình 3.44).",
       "Cơ cấu tác động trực tiếp cho van quay, trong đó áp suất tăng đẩy xuống màng, tùy theo hướng "
       "cần gắn trên trục van mà mở hoặc đóng van (xem Hình 3.45).",
       "Lực đẩy đầu ra ròng là hiệu giữa lực màng và lực lò xo ngược chiều.",
       "Màng ép (molded) cho hiệu năng tuyến tính và hành trình lớn hơn.",
       "Lực đẩy đầu ra yêu cầu và áp suất khí cấp sẵn có quyết định kích cỡ.",
       "Cơ cấu màng đơn giản, đáng tin cậy và kinh tế."],
      ["Pneumatically-operated diaphragm actuators use air supply from controllers, positioners, or "
       "other sources.",
       "Various styles include: direct-acting, in which the increasing air pressure pushes the "
       "diaphragm down and extends the actuator stem (Figure 3.43).",
       "Reverse-acting, in which the increasing air pressure pushes the diaphragm up and retracts the "
       "actuator stem (Figure 3.43).",
       "Reversible, in which actuators can be assembled for either direct or reverse action "
       "(Figure 3.44).",
       "Direct-acting unit for rotary valves, in which the increasing air pressure pushes down on "
       "the diaphragm, which, depending on orientation of the actuator lever on the valve shaft, may "
       "either open or close the valve (see Figure 3.45).",
       "Net output thrust is the difference between diaphragm force and opposing spring force.",
       "Molded diaphragms provide linear performance and increased travels.",
       "Output thrust required and supply air pressure available dictate size.",
       "Diaphragm actuators are simple, dependable, and economical."])
    FIG(43, F.fig_f3_43())
    FIG(44, F.fig_f3_44())
    FIG(45, F.fig_f3_45())

    H("3.8.2 Cơ cấu piston", "3.8.2 Piston Actuators", h3)
    B(["Cơ cấu piston chạy khí nén dùng khí nhà máy áp suất cao tới 150 psig (10,3 bar), thường loại "
       "bỏ nhu cầu bộ điều chỉnh áp suất cấp.",
       "Cơ cấu piston cho lực đẩy đầu ra cực đại và tốc độ hành trình nhanh.",
       "Cơ cấu piston tác động kép để cho lực lớn nhất ở cả hai hướng, hoặc hồi lò xo để vận hành an "
       "toàn khi mất khí: mở (fail-open) hoặc đóng (fail-closed) (Hình 3.46).",
       "Có thể tích hợp nhiều phụ kiện để định vị piston tác động kép khi mất áp suất cấp, gồm van "
       "trip khí nén và hệ thống khóa.",
       "Các phiên bản khác cho dịch vụ trên van điều khiển quay gồm gioăng trượt ở đầu dưới xi lanh. "
       "Điều này cho phép thân cơ cấu dịch chuyển ngang cũng như lên xuống mà không rò áp suất xi "
       "lanh. Tính năng này cho phép nối trực tiếp thân cơ cấu với cần gắn trên trục van quay, loại bỏ "
       "một mối nối hay nguồn chuyển động bị mất."],
      ["Piston actuators are pneumatically-operated using high-pressure plant air up to 150 psig "
       "(10.3 bar), often eliminating the need for a supply pressure regulator.",
       "Piston actuators furnish maximum thrust output and fast stroking speeds.",
       "Piston actuators are double-acting to give maximum force in both directions, or spring-return "
       "to provide fail-open or fail-closed operation (Figure 3.46).",
       "Various accessories can be incorporated to position a double-acting piston in the event of "
       "supply pressure failure, including pneumatic trip valves and lock-up systems.",
       "Other versions for service on rotary control valves include a sliding seal in the lower end "
       "of the cylinder. This permits the actuator stem to move laterally, as well as up and down "
       "without leakage of cylinder pressure. This feature permits direct connection of the actuator "
       "stem to the actuator lever mounted on the rotary valve shaft, thus eliminating one joint or "
       "source of lost motion."])
    FIG(46, F.fig_f3_46())
    FIG(47, F.fig_f3_47())

    H("3.8.3 Cơ cấu tay", "3.8.3 Manual Actuators", h3)
    B(["Cơ cấu tay hữu ích nơi không cần điều khiển tự động nhưng vẫn cần thao tác dễ dàng và điều "
       "khiển tay tốt (Hình 3.48 và 3.49). Chúng thường dùng để tác động van bypass trong vòng bypass "
       "ba van quanh van điều khiển, để điều khiển quá trình bằng tay trong lúc bảo trì hoặc tắt hệ "
       "thống tự động.",
       "Cơ cấu tay có sẵn nhiều cỡ cho cả van kiểu cầu lẫn van quay.",
       "Thiết bị chỉ thị dạng mặt số có sẵn cho một số kiểu để định vị lại chính xác nút van hoặc đĩa.",
       "Cơ cấu tay rẻ hơn nhiều so với cơ cấu tự động."],
      ["Manual actuators are useful where automatic control is not required, but where ease of "
       "operation and good manual control is still necessary (Figures 3.48 and 3.49). They are often "
       "used to actuate the bypass valve in a three-valve bypass loop around control valves for manual "
       "control of the process during maintenance or shut down of the automatic system.",
       "Manual actuators are available in various sizes for both globe-style and rotary valves.",
       "Dial-indicating devices are available for some models to permit accurate repositioning of the "
       "valve plug or disk.",
       "Manual actuators are much less expensive than automatic actuators."])
    FIG(48, F.fig_f3_48())
    FIG(49, F.fig_f3_49())

    H("3.8.4 Cơ cấu răng cưa - bánh răng", "3.8.4 Rack-and-Pinion Actuators", h3)
    P("Thiết kế răng cưa - bánh răng cho giải pháp gọn và kinh tế cho van quay (Hình 3.44). Do có độ "
      "hở răng, chúng thường dùng cho ứng dụng đóng mở hoặc nơi biến thiên quá trình không đáng lo ngại.",
      "Rack-and-pinion designs provide a compact and economical solution for rotary valves "
      "(Figure 3.44). Because of backlash, they are typically used for on/off applications or where "
      "process variability is not a concern.")
    FIG(50, F.fig_f3_50())

    H("3.8.5 Cơ cấu điện", "3.8.5 Electric Actuators", h3)
    P("Thiết kế cơ cấu điện dùng động cơ điện và một dạng giảm tốc để di chuyển nút van (Hình 3.51 "
      "và 3.52). Dù cơ cấu điện theo truyền thống chỉ giới hạn ở vận hành đóng mở, hiện một số có khả "
      "năng điều khiển liên tục. Việc dùng động cơ không chổi than trong cơ cấu điện có thể giảm hoặc "
      "loại bỏ cháy động cơ liên quan đến việc bật tắt động cơ nhanh. Giá mua ban đầu vẫn có xu hướng "
      "cao hơn cơ cấu khí nén. Công dụng chính của cơ cấu điện là ở những khu vực không có sẵn khí "
      "dụng cụ hoặc nơi số lượng van quá ít để biện minh cho chi phí hệ thống máy nén.",
      "Electric actuator designs use an electric motor and some form of gear reduction to move the "
      "valve plug (Figures 3.51 and 3.52). While electric actuators have traditionally been limited "
      "to on/off operation, some are now capable of continuous control. The use of brushless motors "
      "in electric actuators can reduce or eliminate motor burnout associated with turning the motor "
      "on and off rapidly. The initial purchase price still tends to remain above that of pneumatic "
      "actuation. The primary usage of electric actuation is in areas where instrument air is not "
      "readily available or where an insufficient quantity of valves exist to justify the cost of a "
      "compressor system.")
    FIG(51, F.fig_f3_51())
    FIG(52, F.fig_f3_52())

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(note("vi"), note("en"))
    P("Chương 3 chiếm tr. 54–81 của bản in (28 trang) trong Emerson, Control Valve Handbook, ấn bản "
      "6 (2020). Nội dung gồm tám mục: kiểu van điều khiển, đầu nối, nắp van, bộ đệm, định hình dòng, "
      "dẫn hướng nút, trim năng lực hạn chế và cơ cấu chấp hành. Năm mươi hai hình đánh số 3.1–3.52 "
      "được vẽ lại dạng vector trong cvh6fig.py và đặt đúng vị trí xuất hiện của chú thích gốc.",
      "Chapter 3 occupies printed pp. 54-81 (28 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains eight sections: control valve styles, end connections, bonnets, "
      "packing, flow characterization, plug guiding, restricted-capacity trim and actuators. The "
      "fifty-two numbered figures, 3.1-3.52, are redrawn as vectors in cvh6fig.py and placed where "
      "the source captions occur.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 "
      "Emerson Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 "
      "Emerson Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
