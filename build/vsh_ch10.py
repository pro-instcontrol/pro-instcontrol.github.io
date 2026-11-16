# -*- coding: utf-8 -*-
"""Book 6, Unit 10 — Manual Valves VI: Butterfly and Pinch Valves (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 120–143 (PDF pp. 134–157): butterfly leakage classes and seating
designs, installation precautions, pressure-energized and high-performance
seats, fire exposure, body configurations, torque characteristics, then
pinch-valve construction, flow control, body materials and limitations
(Figures 3-69…3-92).
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig7 as F7

PAGES_SRC = 24          # source book pp. 120-143
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Manual Valves VI — Butterfly and Pinch Valves"
TITLE_VI = "Van tay VI — Van bướm và van kẹp"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 10.</b> butterfly valve — van bướm · "
                "disc — đĩa · wafer body — thân wafer kẹp giữa hai bích · "
                "resilient liner — lớp lót đàn hồi · interference seating — "
                "chỗ kín ép ghen · nominal / low leakage — rò rỉ danh nghĩa / "
                "rò rỉ thấp · tight shut-off — đóng kín chặt · double offset "
                "hinge — bản lề lệch kép · pressure-energized seal — chỗ kín "
                "cấp áp · high-performance butterfly valve — van bướm hiệu "
                "năng cao · fire-tested — đã thử lửa · tear drops — gờ hình "
                "giọt lệch · pinch valve — van kẹp · flex-body — thân mềm · "
                "prepinched — ép sẵn · crevice-free passage — đường dòng "
                "không khe hở · iris-like closing — đóng kiểu mống mắt · "
                "equal-percentage — phần trăm bằng nhau · hydrodynamic / "
                "bearing / seating torque — momen thủy động / ma sát gối đỡ "
                "/ ép kín.")
    return ("<b>Key terms.</b> butterfly valve · disc · wafer body · "
            "resilient liner · interference seating · nominal / low leakage "
            "· tight shut-off · double offset hinge · pressure-energized "
            "seal · high-performance butterfly valve · fire-tested · "
            "tear drops · pinch valve · flex-body · prepinched · "
            "crevice-free passage · iris-like closing · equal-percentage · "
            "hydrodynamic / bearing / seating torque.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(items):
        b.append(ul([(i[0] if vi else i[1]) for i in items]))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ========================================================= butterflies
    H("Van bướm", "Butterfly valves")
    P("Van bướm là van quay có cơ cấu đóng dạng đĩa, quay khoảng 90° để mở "
      "hoặc đóng đường dòng. Các van từ Hình 3-69 đến Hình 3-83 chỉ là một "
      "mẫu trong số rất nhiều biến thể. Van bướm nguyên thủy chỉ là cánh "
      "tắt gió đường ống, không định dùng để đóng kín chặt, nhưng đến nay vẫn là "
      "một thành viên quan trọng của họ van bướm.",
      "Butterfly valves are rotary valves in which a disc-shaped closure "
      "member is rotated through approximately 90° to open or close the flow "
      "passage. The valves in Figures 3-69 to 3-83 represent a cross section "
      "of the many variations available. The original butterfly valve was "
      "the simple pipeline damper, not intended for tight shut-off; it "
      "remains an important member of the butterfly family.")
    P("Sự xuất hiện của ê-lô-me thúc đẩy nhanh các van bướm đóng kín chặt, "
      "dùng ê-lô-me làm phần tử làm kín giữa mép đĩa và thân van; ban đầu "
      "chúng dùng cho nước. Khi có nhiều ê-lô-me chịu hóa chất hơn, van bướm "
      "lan rộng vào công nghiệp quá trình. Vật liệu làm kín không chỉ phải "
      "chống ăn mòn mà còn chống mài mòn, ổn định kích thước và giữ được độ "
      "đàn hồi — không được hóa cứng. Nếu thiếu một tính chất, ê-lô-me có thể "
      "không phù hợp; nhà chế tạo nên được hỏi cho từng ứng dụng.",
      "The advent of elastomers initiated rapid development of tight "
      "shut-off butterfly valves in which the elastomer seals between the "
      "disc rim and the body; their original use was for water. As more "
      "chemical-resistant elastomers appeared, butterfly valves spread "
      "through the process industries. Such elastomers must resist corrosion "
      "and abrasion, remain dimensionally stable and retain resiliency — "
      "they must not harden. A missing property may make the elastomer "
      "unsuitable, and manufacturers should advise on selection and limits.")
    P("Nỗ lực khắc phục giới hạn của ê-lô-me dẫn đến van bướm chỗ kín PTFE "
      "và van bướm chỗ kín kim loại đóng kín chặt. Nhờ đó van bướm có mặt "
      "trong dải áp suất và nhiệt độ rộng theo nhiều nguyên lý làm kín. Van "
      "ít cản dòng khi mở hoàn toàn và khống chế lưu lượng nhạy khi mở khoảng "
      "15°–70°. Throttling chất lỏng quá mức có thể gây xâm thực tùy áp suất "
      "hơi và áp hạ lưu; có thể chọn van nhỏ hơn đường ống để throttling xảy "
      "ra gần vị trí mở một nửa và/hoặc chia tổn thất áp thành nhiều cấp như "
      "đã bàn ở Chương 2. Đóng van quá nhanh trong dịch vụ chất lỏng cũng "
      "gây nước dội quá mức; đóng chậm sẽ tránh được.",
      "Efforts to overcome elastomer limitations led to PTFE-seated and "
      "metal-seated tight shut-off butterfly valves, giving the family a "
      "wide pressure and temperature range through several sealing "
      "principles. Butterfly valves offer little resistance when fully open "
      "and sensitive flow control between about 15° and 70°. Severe liquid "
      "throttling may cause cavitation depending on vapour pressure and "
      "downstream pressure; this can be combated by sizing the valve smaller "
      "than the line so throttling occurs near half-open, and/or by taking "
      "the pressure drop in steps as discussed in Chapter 2. Closing too "
      "quickly in liquid service may cause excessive waterhammer, avoided "
      "by closing slowly.")
    P("Vì đĩa tiến vào chỗ kín bằng chuyển động tẩy, hầu hết van bướm xử lý "
      "được chất lỏng có rắn lơ lửng và, tùy độ chắc của chỗ kín, cả bột và "
      "hạt. Trên đường ống nằm ngang nên lắp van với trục nằm ngang; khi mở, "
      "đáy đĩa phải nhấc ra khỏi vật liệu có thể lắng đọng ở phía thượng lưu.",
      "Because the disc moves into the seat with a wiping motion, most "
      "butterfly valves handle fluids with solids in suspension and, "
      "depending on seat robustness, powders and granules. In horizontal "
      "pipelines the stem should be horizontal, and on opening the bottom of "
      "the disc should lift away from solids accumulated upstream.")

    H("Cấp rò rỉ và thiết kế chỗ kín", "Leakage classes and seating designs")
    P("Theo độ kín có thể chia van bướm thành loại rò rỉ danh nghĩa, rò rỉ "
      "thấp và đóng kín chặt. Hai loại đầu chủ yếu dùng để throttling hoặc "
      "khống chế lưu lượng; loại đóng kín chặt dùng được cho đóng kín, "
      "throttling hoặc khống chế. Hình 3-69 là ví dụ van rò rỉ danh nghĩa và "
      "rò rỉ thấp với cả chỗ kín lẫn đĩa đều kim loại; khi cần rò rỉ thấp hơn "
      "có loại lắp xít piston trên mép đĩa.",
      "By seat tightness butterfly valves fall into nominal-leakage, "
      "low-leakage and tight shut-off classes. The first two are used mainly "
      "for throttling or flow control; tight shut-off valves may be used for "
      "tight shut-off, throttling or flow control. Figure 3-69 shows nominal- "
      "and low-leakage valves with metallic seats and discs; where lower "
      "leakage is required, a piston ring on the disc rim is available.")
    FIG(69, F7.fig_vsh_3_69())
    P("Độ tiếp xúc khít giữa các mặt kín của van đóng kín chặt đạt được bằng "
      "nhiều cách:",
      "Intimate contact between the seatings of tight shut-off butterfly "
      "valves is achieved in several ways:")
    U([("Ép ghen: đĩa phải bị nén vào chỗ kín.",
        "Interference seating: the disc is jammed into the seat."),
       ("Đẩy đĩa vào chỗ kín nhờ bản lề lệch kép, tương tự van một chiều đĩa "
        "nghiêng (trang 154).",
        "Force the disc against the seat about a double offset hinge, "
        "comparable to a tilting-disc check valve (page 154)."),
       ("Làm kín cấp áp bằng O-ring, môi kín, màng hoặc ống hơi bơm căng.",
        "Pressure-energized sealing with O-rings, lip seals, diaphragms or "
        "inflatable hoses.")])
    P("Đa số van bướm là kiểu ép ghen với lớp lót cao su như Hình 3-70 đến "
      "Hình 3-72. Khi cao su không tương thích, lớp lót PTFE được đỡ bằng đệm "
      "ê-lô-me để tạo độ đàn hồi cho chỗ kín. Các cấu trúc lót thường gặp: "
      "vòng chữ U lồng qua thân không dán, dễ thay (Hình 3-70); cao su dán "
      "trực tiếp vào thân, hạn chế hiện tượng lót bị dồn khi đĩa quay nhưng "
      "không thay được; và vòng chữ U dán vào băng kim loại để đưa vào thân "
      "chia đôi (Hình 3-72). Với vật liệu cứng như PTFE, thân được chia theo "
      "đường tâm để lắp lớp lót không phải bẻ cong.",
      "Most butterfly valves are interference-seated with a rubber liner, "
      "as in Figures 3-70 to 3-72. Where rubber is incompatible, a PTFE liner "
      "is backed by an elastomer cushion for resiliency. Common liner "
      "constructions are an unbonded U-ring slipped over the body and readily "
      "replaceable (Figure 3-70); rubber bonded to the body, limiting bunching "
      "as the disc rotates but not replaceable; and a U-liner bonded to a "
      "metal band for insertion into a split body (Figure 3-72). With a rigid "
      "material such as PTFE the body is split on the centreline so the liner "
      "can be inserted without manipulation.")
    FIG(70, F7.fig_vsh_3_70())
    FIG(71, F7.fig_vsh_3_71())
    FIG(72, F7.fig_vsh_3_72())
    P("Để phát huy hết khả năng làm kín, van lót cao su phải lắp đúng cách. "
      "Lớp lót cần được bích ống đỡ toàn bộ, nên dùng bích cổ hàn thay vì "
      "bích lồng: với bích lồng, đoạn lót giữa lỗ van và đường kính ngoài của "
      "ống không được đỡ, dễ biến dạng khi thao tác, dẫn đến mòn sớm và rò "
      "chỗ kín. Lúc lắp, đặt đĩa gần đóng để bảo vệ mép đĩa; trước khi siết "
      "bulông bích, quay đĩa mở hoàn toàn để lớp lót về vị trí tự nhiên. "
      "Mép lót cao su đã tự làm kín với bích ống, nên không lắp thêm gioăng "
      "cao su — gioăng thêm làm giảm độ đỡ và khả năng làm kín.",
      "To achieve full sealing capacity, rubber-lined valves must be "
      "installed correctly. The liner must be fully supported by weld-neck "
      "rather than slip-on flanges: with slip-on flanges the liner is "
      "unsupported between the valve bore and pipe outside diameter, tending "
      "to distort in operation and causing early wear and seat leakage. Put "
      "the disc near-closed while handling to protect its rim, then rotate it "
      "fully open before tightening flange bolts so the liner finds its "
      "undisturbed position. The liner flange already seals against the "
      "pipeline flange; extra rubber gaskets reduce liner support and "
      "sealing capacity.")
    FIG(73, F7.fig_vsh_3_73())
    P("Hình 3-74 cho thấy phần tử đàn hồi đặt trên mép đĩa của van ép ghen: "
      "O-ring tiết diện lớn có đuôi kẹp vào đĩa. Chỉnh lực kẹp sẽ chỉnh độ "
      "ghen trong giới hạn nhất định. Vì phần tử biến dạng trên mặt rộng thay "
      "vì quanh mép đĩa hẹp, momen ép kín và nhả kín thấp hơn; kiểu này chỉ "
      "chế tạo cỡ lớn và dùng cho áp chất lỏng tương đối cao.",
      "Figure 3-74 shows the resilient element carried on the disc rim of an "
      "interference-seated valve: a heavy-section O-ring with a tail clamped "
      "to the disc. Adjusting the clamping force adjusts interference within "
      "limits. Because the element deforms against a wide face rather than "
      "the narrow disc edge, seating and unseating torques are lower; this "
      "make is produced only in larger sizes for relatively high fluid "
      "pressures.")
    FIG(74, F7.fig_vsh_3_74())
    P("Hình 3-75 và 3-76 dùng phần tử cao su cấp áp. Ở Hình 3-75, ống hơi "
      "đặt trên mép đĩa được gia cố bằng ống kim loại bên trong và nối qua "
      "trục với hệ thống thượng lưu hoặc nguồn áp ngoài. Đĩa vào chỗ kín côn "
      "khi ống xì để momen ép kín nhỏ nhất, sau đó bơm căng ống để kín chặt; "
      "có thể dùng bơm tay nếu cần ép thêm. Khi mở van, xì ống trước để momen "
      "nhả kín nhỏ nhất. Van chế tạo đến cỡ lớn nhất đang dùng. Hình 3-76 đặt "
      "màng ống tiết diện chữ T trong rãnh thân, cấp áp lúc đóng và xì áp lúc "
      "mở theo cách tương tự.",
      "Figures 3-75 and 3-76 rely on pressure-energized rubber. In Figure "
      "3-75 an inflatable hose on the disc rim is internally reinforced by a "
      "metallic conduit and connected through the shaft to upstream or "
      "external pressure. The disc enters the tapered seat with the hose "
      "deflated for minimum seating torque, then the hose is pressurised for "
      "a fluid-tight seal, optionally topped up by hand pump; before opening "
      "it is deflated again for minimum unseating torque. The valve is made "
      "to the largest sizes in use. Figure 3-76 mounts a tubular diaphragm of "
      "T-cross-section in a body slot, pressurised on closing and "
      "depressurised on opening in the same manner.")
    FIG(75, F7.fig_vsh_3_75())
    FIG(76, F7.fig_vsh_3_76())

    H("Van bướm hiệu năng cao", "High-performance butterfly valves")
    P("Để mở rộng dải nhiệt độ và áp suất, một họ van bướm có thể lắp chỗ kín "
      "kim loại–polyme hoặc kim loại–kim loại, kể cả phiên bản đã thử lửa, và "
      "thường dùng được cho dòng hai chiều. Gọi là hiệu năng cao vì bao viền "
      "áp suất–nhiệt độ rộng hơn van lót ê-lô-me thông thường. Hình 3-77 đến "
      "Hình 3-83 là các ví dụ; hình minh họa không thể hiện mọi biến thể chỗ "
      "kín của từng van.",
      "Extending temperature and pressure range produced a family of "
      "butterfly valves with metal-to-polymer or metal-to-metal seatings, "
      "including fire-tested versions, generally suitable for flow in both "
      "directions. The name denotes a wider pressure-temperature envelope "
      "than ordinary elastomer-lined valves. Figures 3-77 to 3-83 are "
      "examples; the drawings do not show every seal variation available.")
    P("Hình 3-77 dùng bản lề lệch kép để đẩy đĩa vào chỗ kín, tương tự van một "
      "chiều đĩa nghiêng. Đĩa là một lát cắt của phích côn ở góc xiên so với "
      "trục, tạo mặt kín côn trên chu vi ê-líp. Trục đĩa nằm dưới tâm van và "
      "phía sau mặt chỗ kín nên đĩa lọt vào và nhấc ra với rất ít cọ xát. Tải "
      "kín gồm momen đóng từ bộ thao tác và momen thủy tĩnh do áp chất lỏng "
      "tác động lên diện tích không cân bằng của đĩa. Có thể dùng chỗ kín "
      "kim loại–kim loại hoặc phần tử mềm ép vào chỗ kín kim loại của thân; "
      "với cấu trúc này van làm việc đến 35 bar và −200…650 °C.",
      "Figure 3-77 forces the disc against the seat about a double offset "
      "hinge, comparable to a tilting-disc check valve. The disc is a slice "
      "from a tapered plug cut obliquely to the plug axis, giving tapered "
      "faces on an elliptical circumference. Its axis lies below the valve "
      "centreline and behind the seat face, so the disc drops into and lifts "
      "out of the seat with little rubbing. Seating load comes from applied "
      "closing torque plus hydrostatic torque on the unbalanced disc area. "
      "Metal-to-metal seatings or soft elements sealing against a metal body "
      "seat are available; the construction serves up to 35 bar and "
      "−200…650 °C.")
    FIG(77, F7.fig_vsh_3_77())
    P("Hình 3-78 gần với van bi dạng wafer: vòng kín nhựa chữ U đặt trong rãnh "
      "chữ T của thân và được O-ring ê-lô-me đỡ. O-ring tạo ứng suất ép ban "
      "đầu; khi đĩa vào chỗ kín với độ ghen nhỏ, áp chất lỏng tác động lên "
      "O-ring ép vòng sát hơn vào mép đĩa. Có nhiều cấu trúc vòng kín, kể cả "
      "kim loại, cho các điều kiện làm việc khác nhau.",
      "Figure 3-78 resembles a ball valve using a wafer section: a U-shaped "
      "plastic seal ring sits in a body T-slot and is backed by an "
      "elastomeric O-ring. The O-ring gives initial compression; as the disc "
      "enters with slight interference, fluid pressure on the O-ring forces "
      "the ring closer to the disc rim. Several seat-ring constructions, "
      "including metal, suit different conditions.")
    FIG(78, F7.fig_vsh_3_78())
    P("Hình 3-79 cũng mượn ý tưởng từ van bi nhưng trục đĩa lệch không chỉ "
      "khỏi mặt chỗ kín mà còn một ít khỏi tâm van. Nhờ đó đĩa vào chỗ kín "
      "theo tác dụng cam, tiếp xúc dần dần, và thoát chỗ kín nhanh lúc mở để "
      "giảm cọ xát. Chỗ kín là môi PTFE có đuôi kẹp giữa thân và vòng giữ; "
      "sau khi đĩa vào với độ ghen nhỏ, áp chất lỏng ép môi sát mép đĩa dù "
      "chỗ kín nằm thượng lưu hay hạ lưu. Đặc tính kín hai chiều còn nhờ một "
      "chuyển động trục nhỏ nhưng được khống chế của đĩa. Có phiên bản chỗ "
      "kín kim loại và đã thử lửa.",
      "Figure 3-79 also borrows from the ball valve, but the disc axis is "
      "offset not only from the seat plane but also slightly from the valve "
      "centreline. The disc cams progressively into contact and disengages "
      "quickly on opening, minimising rubbing. The seat is a PTFE lip with a "
      "tail clamped between body and retainer; once the disc enters with "
      "slight interference, fluid pressure forces the lip onto the disc rim "
      "whether the seat is upstream or downstream. Bidirectional sealing is "
      "aided by a small controlled axial movement of the disc. Metal and "
      "fire-tested seat constructions are available.")
    FIG(79, F7.fig_vsh_3_79())
    P("Nguyên lý lệch kép kết hợp làm kín cấp áp hai chiều áp dụng cho cả các "
      "van Hình 3-80 đến 3-82. Hình 3-80 dùng môi PTFE biến tính được vòng "
      "titan đỡ; Hình 3-81 dùng O-ring ê-lô-me bọc PTFE neo trong thân — "
      "O-ring cung cấp độ đàn hồi, vỏ PTFE bảo vệ nó khỏi chất lỏng. Cả hai "
      "đều có phiên bản đã thử lửa.",
      "The double offset axis with bidirectional pressure-energized sealing "
      "also applies to Figures 3-80 to 3-82. Figure 3-80 uses a modified PTFE "
      "lip supported by a titanium ring; Figure 3-81 uses a PTFE-encapsulated "
      "elastomeric O-ring anchored in the body — the O-ring supplies "
      "elasticity while the PTFE envelope protects it from the fluid. Both "
      "have fire-tested versions.")
    FIG(80, F7.fig_vsh_3_80())
    FIG(81, F7.fig_vsh_3_81())
    P("Hình 3-82 gồm chỗ kín kết hợp màng dẻo đưa chỗ kín về vị trí ban đầu "
      "sau mỗi lần thao tác. Một phiên bản dùng cụm PTFE chữ T nhúng màng dẻo; "
      "phiên bản đã thử lửa dùng cụm kim loại chữ U có đệm PTFE đặt trên màng "
      "kim loại. PTFE làm kín trong điều kiện thường; nếu cháy làm mất đệm "
      "PTFE thì chỗ kín kim loại tiếp nhận chức năng làm kín.",
      "Figure 3-82 combines the seat with a flexible membrane that returns "
      "it to its original position after each operation. One version embeds "
      "a pliant membrane in a T-shaped PTFE member; a fire-tested version "
      "uses a U-shaped metal member with a PTFE insert carried on a metal "
      "membrane. The PTFE insert seals under normal conditions; if fire "
      "destroys it, the metal seat takes over.")
    FIG(82, F7.fig_vsh_3_82())
    P("Khác với các van trên, Hình 3-83 dựa vào ép ghen với đĩa lệch kép. Chỗ "
      "kín có thể bằng nhựa, ê-lô-me, kim loại hoặc nhựa/kim loại đã thử lửa "
      "cho chất lỏng dễ cháy. Chỗ kín nhựa và kim loại dùng vòng dây đỡ: khi "
      "đóng, vòng tạo độ cứng tuyệt đối để đạt độ ghen kín ở cả áp cao, áp "
      "thấp và chân không; khi mở, không đặt tải lên chỗ kín để phần tử làm "
      "kín được uốn cong tự do theo hướng kính.",
      "Unlike the preceding valves, Figure 3-83 relies on interference "
      "seating with a double offset disc. The seat may be plastic, "
      "elastomer, metal or a fire-tested plastic/metal composition for "
      "flammable liquids. Plastic and metal seats use a back-up wire winding "
      "that gives absolute rigidity when closed — achieving interference for "
      "tight shut-off at high and low pressures including vacuum — while "
      "leaving the seat unloaded and free to flex radially when open.")
    FIG(83, F7.fig_vsh_3_83())

    H("Van bướm chịu lửa", "Butterfly valves for fire exposure", h3)
    P("Van bướm xử lý chất lỏng dễ cháy có thể gặp cháy nhà máy phải vẫn kín "
      "chặt bên trong và bên ngoài, thao tác được trong và sau đám cháy. Các "
      "phiên bản đã thử lửa của van bướm hiệu năng cao đáp ứng yêu cầu này. "
      "Yêu cầu thử và đánh giá tương tự như đã nêu cho van bi ở trang 108.",
      "Butterfly valves handling flammable fluids that may be exposed to a "
      "plant fire must remain essentially fluid-tight internally and "
      "externally and be operable during and after the fire. Fire-tested "
      "versions of high-performance butterfly valves meet these conditions; "
      "test and evaluation requirements are similar to those for ball valves "
      "on page 108.")

    H("Cấu hình thân", "Body configurations", h3)
    P("Kiểu thân wafer kẹp giữa hai bích đường ống được ưu tiên. Bulông kéo "
      "hai bích lại chịu toàn bộ ứng suất kéo do biến dạng đường ống và đặt "
      "thân wafer trong nén; ứng suất nén này được giảm bởi ứng suất kéo do "
      "áp chất lỏng bên trong. Thân có bích thì tự chịu mọi ứng suất kéo từ "
      "đường ống, và ứng suất kéo do áp chất lỏng cộng dồn. Vì hầu hết kim "
      "loại chịu nén tốt gấp khoảng hai lần giới hạn kéo, thân wafer được "
      "khuyến nghị mạnh. Tuy nhiên nếu phía hạ lưu cũng là điểm tháo rời mà "
      "phía thượng lưu vẫn có áp, thân wafer bắt bulông ngang không dùng "
      "được trừ khi có bích giả; khi đó dùng thân có bích hoặc wafer có tai "
      "ren để nhận bulông từ bích kề.",
      "The preferred butterfly body is the wafer clamped between two pipe "
      "flanges: the bolts pulling the flanges together carry line-strain "
      "tension and place the wafer in compression, eased by tensile stress "
      "from internal pressure. A flanged body must carry all line-strain "
      "tension, with pressure tension cumulative. Since most metals accept "
      "compressive loads up to about twice their tensile limit, the wafer "
      "body is strongly favoured. If the downstream side is also a "
      "disconnection point while upstream remains pressurised, a "
      "cross-bolted wafer is unsuitable unless fitted with a false flange; "
      "a flanged body or lugged wafer with threaded lugs receiving screws "
      "from adjacent flanges is then used.")

    H("Đặc tính momen", "Torque characteristics")
    P("Momen thao tác van bướm gồm ba thành phần: Th là momen thủy động do "
      "dòng chảy tác động lên đĩa; Tb là momen khắc phục ma sát gối đỡ; và Ts "
      "là momen ép kín hoặc nhả kín đĩa. Momen thủy động thay đổi theo độ mở "
      "và tổn thất áp. Với đĩa đối xứng, momen này như nhau cho hai chiều "
      "dòng và luôn chống lại chiều mở. Với đĩa lệch như Hình 3-84, momen "
      "thủy động khác nhau theo chiều dòng; nhỏ nhất khi dòng chảy về phía "
      "đĩa. Dòng về phía trục luôn chống mở, còn dòng về phía đĩa chỉ chống "
      "lúc đầu rồi đổi chiều khi van mở thêm. Momen gối đỡ, ép kín và nhả kín "
      "luôn chống chuyển động; độ lớn của momen gối đỡ tương ứng với lực "
      "thủy động tổng hợp trên đĩa, còn momen ép/nhả kín không phụ thuộc dòng.",
      "Operating torque has three components: Th, hydrodynamic torque from "
      "flow acting on the disc; Tb, bearing-friction torque; and Ts, torque "
      "to seat or unseat the disc. Hydrodynamic torque varies with opening "
      "and pressure drop. For a symmetrical disc it is the same for either "
      "flow direction and always opposes opening. For an offset disc as in "
      "Figure 3-84 it differs by direction and is lowest with flow toward "
      "the disc: flow toward the shaft opposes opening throughout, whereas "
      "flow toward the disc opposes it initially then reverses as opening "
      "increases. Bearing, seating and unseating torques always oppose "
      "motion; bearing torque follows the resultant hydrodynamic force, "
      "while seating and unseating torque is independent of flow.")
    FIG(84, F7.fig_vsh_3_84())
    P("Với van ép ghen đến DN 400 (NPS 16) và vận tốc dòng không quá cao, "
      "momen ép/nhả kín thường áp đảo và đủ để chọn bộ truyền theo các momen "
      "này. Độ lớn phụ thuộc chất lỏng và tần suất thao tác: chất lỏng bôi "
      "trơn tốt và van thao tác thường xuyên cho momen thấp hơn chất ít bôi "
      "trơn, chứa rắn hoặc van ít thao tác; nhà chế tạo cung cấp bảng theo "
      "điều kiện. Với van lớn hơn DN 400 hoặc vận tốc cao, momen thủy động "
      "và gối đỡ có thể vượt xa momen ép/nhả kín, nên phải chọn bộ thao tác "
      "cùng nhà chế tạo.",
      "For interference-seated valves up to DN 400 (NPS 16) at moderate "
      "velocity, seating and unseating torques normally dominate and suffice "
      "for sizing the gear. Their magnitude depends on fluid and operating "
      "frequency: good lubricity and frequent operation give lower torque "
      "than poor lubricity, solids or infrequent operation; manufacturers "
      "supply tables. Above DN 400 or at high velocity, hydrodynamic and "
      "bearing torques can greatly exceed seating torque, so the operator "
      "should be selected with the manufacturer.")
    P("Hình 3-85 tổng hợp momen mở ở tổn thất áp không đổi cho đĩa đối xứng "
      "và đĩa lệch. Trong hầu hết lắp đặt thực tế, tổn thất áp giảm dần khi "
      "van mở như Hình 3-86, làm momen tương ứng giảm theo; momen lớn nhất "
      "vì thế dịch từ vùng gần mở hoàn toàn sang vùng mở một phần như Hình "
      "3-87. Momen thấp nhất khi đĩa lệch và dòng về phía đĩa, nhưng đổi lại "
      "tổn thất áp cao hơn một chút. Với van lớn và vận tốc cao, đặc tính "
      "này giúp giảm chi phí bộ thao tác.",
      "Figure 3-85 summarises opening torque at constant pressure drop for "
      "symmetrical and offset discs. In most real installations pressure drop "
      "falls as the valve opens (Figure 3-86), reducing the corresponding "
      "torque; the maximum therefore shifts from near fully open to partly "
      "open (Figure 3-87). Torque is lowest for an offset disc with flow "
      "toward the disc, at the penalty of a somewhat higher pressure drop. "
      "For large valves at high velocity this characteristic can reduce "
      "operator cost.")
    FIG(85, F7.fig_vsh_3_85())
    FIG(86, F7.fig_vsh_3_86())
    FIG(87, F7.fig_vsh_3_87())
    H("Tiêu chuẩn", "Standards", h3)
    P("Phụ lục C liệt kê các tiêu chuẩn Mỹ và Anh liên quan đến van bướm.",
      "Appendix C lists U.S. and British standards pertaining to butterfly "
      "valves.")
    H("Ứng dụng của van bướm", "Butterfly valve applications", h3)
    P("Nhiệm vụ: dừng và khởi động dòng; khống chế lưu lượng.",
      "Duty: stopping and starting flow; controlling flow.")
    P("Dịch vụ: khí; chất lỏng; hỗn dịch; bột; hạt; xử lý vệ sinh dược phẩm "
      "và thực phẩm; chân không.",
      "Service: gases; liquids; slurries; powder; granules; sanitary handling "
      "of pharmaceuticals and foodstuffs; vacuum.")

    # ============================================================== pinch
    H("Van kẹp", "Pinch valves")
    P("Van kẹp là van thân mềm gồm một ống mềm bị ép bằng cơ khí như Hình "
      "3-88 đến 3-90, hoặc bằng áp suất chất lỏng tác động lên bên ngoài thân "
      "như Hình 3-91 và 3-92. Ưu điểm chính là đường dòng thẳng, không khe hở "
      "và không chi tiết chuyển động; thân mềm còn có thể kín quanh rắn bị kẹt. "
      "Vì vậy van kẹp hợp cho hỗn dịch và chất rắn dễ làm tắc đường dòng có "
      "vật cản, cũng như xử lý vệ sinh thực phẩm và dược phẩm. Tùy vật liệu, "
      "van kẹp còn xử lý chất mài mòn dữ dội và hầu hết chất ăn mòn.",
      "Pinch valves are flex-body valves consisting of a flexible tube "
      "pinched mechanically (Figures 3-88 to 3-90) or by fluid pressure "
      "applied outside the body (Figures 3-91 and 3-92). A principal "
      "advantage is a straight, crevice-free passage with no moving parts; "
      "the soft body can also seal around trapped solids. Pinch valves thus "
      "suit slurries and solids that would clog obstructed passages, and "
      "sanitary food and pharmaceutical handling. Depending on body material "
      "they also handle severely abrasive fluids and most corrosive fluids.")
    H("Van kẹp hở và van kẹp kín", "Open and enclosed pinch valves", h3)
    P("Van ép cơ khí có thể kiểu hở để quan sát và kiểm tra trực tiếp thân "
      "trong lúc làm việc. Vỏ bị phồng hoặc chỗ mềm là dấu hiệu cần thay thân "
      "như Hình 3-88. Nếu không được phép để chất lỏng thoát ra khi thân vỡ "
      "ngoài ý muốn, thân phải được bọc kín. Vỏ thường chia dọc theo trục "
      "đường dòng để dễ tiếp cận, nhưng cũng có dạng nguyên khối. Hình 3-89 "
      "thêm ống ép sẵn 50% và nút xả tháo được để nối chân không; Hình 3-90 "
      "dùng thân PTFE có gờ hình giọt lệch.",
      "Mechanically pinched valves may be open so the body can be inspected "
      "visually and physically in service; bulges and soft spots signal "
      "replacement, as in Figure 3-88. If escape from an accidentally "
      "ruptured body cannot be tolerated, the body must be encased, normally "
      "split along the flow axis for access although unit casings also "
      "exist. Figure 3-89 adds a 50% prepinched sleeve and removable drain "
      "plug for vacuum connection; Figure 3-90 uses a PTFE body with tear "
      "drops.")
    FIG(88, F7.fig_vsh_3_88())
    FIG(89, F7.fig_vsh_3_89())
    FIG(90, F7.fig_vsh_3_90())
    H("Khống chế lưu lượng", "Flow control", h3)
    P("Van kẹp gần như không khống chế được lưu lượng từ mở hoàn toàn đến ép "
      "50% vì tổn thất áp ở các vị trí này rất nhỏ; đóng thêm sau đó cho khống "
      "chế tốt. Vì vậy van ép cơ khí dùng để khống chế thường được ép sẵn 50%. "
      "Với chất lỏng xói mòn mạnh, tránh khống chế gần vị trí đóng để không "
      "tạo rãnh trên thân; van cũng phải đóng kín chặt để dòng rò không khoét "
      "rãnh thân.",
      "Pinch valves give little flow control between fully open and 50% "
      "pinched because pressure drop there is negligible; further closing "
      "gives good control. Mechanically pinched control valves are therefore "
      "often 50% prepinched. With severely erosive fluid, avoid control near "
      "the closed position to prevent grooving of the body, and always close "
      "fluid-tight so leakage flow cannot groove it.")
    P("Van kẹp thao tác bằng áp chất lỏng thường không hợp cho khống chế tay "
      "vì chỉ cần áp hạ lưu thay đổi là vị trí van tự thiết lập lại. Nếu không "
      "xét đến điểm đó, đặc tính khống chế của Hình 3-91 tương tự van ép cơ "
      "khí.",
      "Fluid-pressure operated pinch valves are not normally suitable for "
      "manual flow control because any change in downstream pressure resets "
      "the valve position. Otherwise the characteristic of Figure 3-91 is "
      "similar to that of mechanically pinched valves.")
    FIG(91, F7.fig_vsh_3_91())
    P("Ngoại lệ là Hình 3-92: cơ cấu đóng kiểu mống mắt, ép tròn 360° quanh "
      "ống nên lỗ luôn tròn và luôn tâm, cho đặc tính equal-percentage trong "
      "toàn dải. Mống mắt cho qua hạt lớn hơn mọi kiểu van ở mọi vị trí, giảm "
      "xu hướng hỗn dịch tạo cầu ở van mở một phần, và lỗ tiết lưu tròn cũng "
      "giảm rãnh thân khi throttling chất mài mòn. Nhược điểm là van không "
      "đóng kín hoàn toàn được.",
      "The exception in Figure 3-92 closes iris-like: the rubber muscle "
      "exerts literally a 360° squeeze, giving an always round, always "
      "centred hole and equal-percentage control throughout. The iris lets "
      "larger particles pass in any position than any other valve, reducing "
      "slurry bridging when partly closed; the circular throttling orifice "
      "also reduces body grooving under severe abrasive throttling. The "
      "drawback is that it cannot close fully.")
    FIG(92, F7.fig_vsh_3_92())
    H("Vật liệu thân và giới hạn", "Body material and limitations", h3)
    P("Thân van làm bằng ê-lô-me, PTFE hoặc vật liệu tương tự, có thể pha trộn "
      "hoặc gia cố vải để tăng độ bền cơ học. Cao su tự nhiên chống nứt do "
      "uốn cong tốt nhất, đồng thời chống mài mòn và ăn mòn hóa học rất tốt. "
      "Tuy nhiên với chất hoạt tính hóa học, bề mặt cao su chịu ứng suất lớn "
      "bị tấn công nhanh hơn; sản phẩm ăn mòn có thể tạo màng mỏng kém dẻo hơn "
      "cao su gốc, màng này nứt khi uốn mạnh và để chất lỏng tấn công tiếp, "
      "cuối cùng thông suốt. Một số cao su tổng hợp chịu dạng tấn công này "
      "tốt hơn, mở rộng phạm vi dịch vụ ăn mòn; nhà chế tạo tìm vật liệu vừa "
      "chống ăn mòn, vừa bền kéo cao mà vẫn mềm để chống mài mòn và dễ đóng. "
      "Để giảm mức uốn, bên trong thân có thể làm rãnh ở hai phía đối nhau "
      "hoặc gờ hình giọt lệch như Hình 3-90; thiết kế này cho phép thân làm "
      "hoàn toàn bằng PTFE.",
      "The body is made of elastomer, PTFE or similar materials, optionally "
      "fabric-reinforced. Natural rubber best resists flex cracking and also "
      "resists abrasive wear and corrosion by many fluids. With chemically "
      "active fluids, highly stressed rubber is attacked more readily; "
      "corrosion products may form a thin film far less flexible than the "
      "parent rubber, cracking on severe flexing and exposing fresh rubber "
      "until cracking goes through. Some synthetic rubbers resist this "
      "attack better and extend corrosive service; compounders seek "
      "corrosion resistance together with high tensile strength, softness "
      "for abrasion resistance and easy closure. To reduce flexing, the body "
      "inside may have opposing groove-like recesses or tear drops as in "
      "Figure 3-90 — a design that permits an all-PTFE sleeve.")
    P("Thân mềm đặt ra một số giới hạn, có thể khắc phục bằng thiết kế thân "
      "đặc biệt hoặc cách thao tác:",
      "The flexible body imposes limitations, sometimes overcome by special "
      "body designs or methods of operation:")
    U([("Van kẹp cấp áp có xu hướng xẹp khi hút chân không; nếu dùng van ép "
        "cơ khí cho dịch vụ này, thân phải gắn chắc vào cơ cấu thao tác.",
        "Fluid-pressure operated pinch valves tend to collapse on suction "
        "duty; for mechanical pinch valves the body must be positively "
        "attached to the operating mechanism."),
       ("Van kẹp sau bơm phải mở trước khi khởi động bơm. Nếu van còn đóng, "
        "không khí giữa bơm và van nén lại rồi thoát nhanh khi van hé; cột "
        "chất lỏng theo sau đập mạnh vào thân, có thể làm vỡ thân.",
        "Pinch valves downstream of a pump should be opened before starting "
        "the pump. If closed, trapped air compresses and escapes rapidly when "
        "the valve cracks open; the following liquid column then strikes the "
        "body heavily, perhaps bursting it."),
       ("Dòng chảy nhấp nhô làm thân van phập phồng và hỏng vì mỏi.",
        "Pulsating flow makes the body pant and eventually fail by fatigue."),
       ("Khi van kẹp là van chặn chính trong hệ thống chất lỏng bị khóa không "
        "chỗ giãn nở, đóng van cần dịch chuyển một lượng chất lỏng nên không "
        "thể thao tác; cố ép có thể làm vỡ thân.",
        "As the main shut-off in a system where liquid is locked with no "
        "room to move, the valve cannot close because it must displace "
        "liquid; forcing it may burst the body.")])
    P("Hiện không có tiêu chuẩn quốc gia nào riêng cho van kẹp.",
      "No national standards apply specifically to pinch valves.")
    H("Ứng dụng của van kẹp", "Pinch valve applications", h3)
    P("Nhiệm vụ: dừng và khởi động dòng; khống chế lưu lượng.",
      "Duty: stopping and starting flow; controlling flow.")
    P("Dịch vụ: chất lỏng; hỗn dịch mài mòn; bột; hạt; xử lý vệ sinh dược "
      "phẩm và thực phẩm.",
      "Service: liquids; abrasive slurries; powders; granules; sanitary "
      "handling of pharmaceuticals and foodstuffs.")

    # -------------------------------------------------------------- table
    H("Bảng tóm tắt các thiết kế trong đơn vị", "Designs in this unit")
    b.append(table(
        ["Hình", "Thiết kế", "Nguyên lý làm kín / ép", "Đặc điểm chính"]
        if vi else
        ["Figure", "Design", "Sealing / pinching principle", "Key feature"],
        [
            ["3-69", "Đĩa và chỗ kín kim loại / Metal disc and seat",
             "Kim loại / Metal", "Rò rỉ danh nghĩa–thấp / Nominal–low leakage"],
            ["3-70", "Lót chữ U lồng / Unbonded U-liner",
             "Ép ghen / Interference", "Dễ thay lót / Liner replaceable"],
            ["3-71", "Đĩa kép / Double disc",
             "Ép ghen / Interference", "Chặn kép xả / Double block and bleed"],
            ["3-72", "Lót dán băng thép / Steel-band liner",
             "Ép ghen / Interference", "Thân chia đôi / Split body"],
            ["3-73", "Lắp bích / Flange installation",
             "Bích cổ hàn, không gioăng thêm / Weld-neck, no extra gasket",
             "Đỡ lót, đĩa mở trước khi siết / Support, open before bolts"],
            ["3-74", "O-ring mép đĩa / Disc-rim O-ring",
             "Đuôi kẹp chỉnh ghen / Clamped tail", "Momen thấp / Low torque"],
            ["3-75", "Ống hơi mép đĩa / Inflatable disc-rim hose",
             "Cấp áp / Pressure-energized", "Xì khi mở / Deflate to open"],
            ["3-76", "Màng chữ T trong thân / T-diaphragm in body",
             "Cấp áp / Pressure-energized", "Rãnh thân / Body slot"],
            ["3-77", "Lệch kép, mặt côn / Double offset, tapered",
             "Momen đóng + thủy tĩnh / Closing + hydrostatic",
             "35 bar, −200…650 °C"],
            ["3-78", "Vòng nhựa đỡ O-ring / O-ring-backed plastic",
             "Cấp áp qua O-ring / O-ring energized",
             "Rãnh chữ T / T-slot"],
            ["3-79", "Môi PTFE đuôi kẹp / PTFE lip with tail",
             "Tác dụng cam / Camming", "Kín hai chiều / Bidirectional"],
            ["3-80", "Môi PTFE đỡ titan / Titanium-supported lip",
             "Cấp áp / Pressure-energized", "Vòng titan / Titanium ring"],
            ["3-81", "O-ring bọc PTFE / PTFE-encapsulated O-ring",
             "Đàn hồi + vỏ bảo vệ / Elastic + envelope",
             "Có bản chịu lửa / Fire-tested version"],
            ["3-82", "Màng dẻo tự hồi / Pliant membrane return",
             "PTFE → kim loại khi cháy / PTFE to metal in fire",
             "Chỗ kín về vị trí cũ / Seat reset"],
            ["3-83", "Ép ghen lệch kép / Interference double offset",
             "Vòng dây đỡ / Back-up wire winding",
             "Bốn vật liệu chỗ kín / Four seat materials"],
            ["3-84", "Đĩa lệch / Offset disc",
             "Momen thủy động đổi chiều / Direction-dependent torque",
             "Dòng về đĩa momen thấp / Flow toward disc"],
            ["3-85…3-87", "Đặc tính momen / Torque maps",
             "Δp không đổi và bơm thực tế / Constant Δp, actual pumping",
             "Momen lớn nhất dịch khi mở một phần / Peak shifts partly open"],
            ["3-88", "Van kẹp hở / Open pinch valve",
             "Ép cơ khí / Mechanical", "Nhìn thấy ống / Sleeve visible"],
            ["3-89", "Van kẹp kín, ép sẵn 50% / Enclosed, 50% prepinch",
             "Ép cơ khí / Mechanical", "Khống chế nhạy / Sensitive control"],
            ["3-90", "Thân PTFE có gờ giọt / PTFE with tear drops",
             "Ép cơ khí / Mechanical", "Giảm uốn, thân PTFE / Less flexing"],
            ["3-91", "Van kẹp cấp áp / Fluid-pressure pinch",
             "Áp chất lỏng / Fluid pressure", "Không cho khống chế tay / Not manual"],
            ["3-92", "Đóng kiểu mống mắt / Iris-like closing",
             "Ép tròn 360° / 360° squeeze",
             "Equal-percentage; không đóng kín / Cannot close fully"],
        ],
        caption=("Tóm tắt theo Hình 3-69…3-92 (văn bản nguồn, book pp. 120–143)."
                 if vi else
                 "Summary from Figures 3-69…3-92 (source text, book pp. 120–143)."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
