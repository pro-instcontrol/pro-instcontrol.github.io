# -*- coding: utf-8 -*-
"""Book 6, Unit 8 — Manual Valves IV: Plug Valves (EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 97–108 (PDF pp. 111–122): cylindrical and taper plug valves, sealing
methods, antistatic devices, fire exposure, multiport configurations,
face-to-face dimensions and valve patterns (Figures 3-49…3-59).
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig5 as F5

PAGES_SRC = 12          # source book pp. 97-108
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Manual Valves IV — Plug Valves"
TITLE_VI = "Van tay IV — Van phích (plug)"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 8.</b> plug valve — van phích · "
                "cylindrical / taper plug — phích trụ / phích côn · "
                "sealant (sealing compound) — chất làm kín (hợp chất bôi kín) "
                "· packing sleeve — ống bọc đệm · follower nut — đai ốc ép · "
                "split plug — phích tách đôi · eccentric semi-plug — bán "
                "phích lệch tâm · lift plug — phích nâng · balance hole — lỗ "
                "cân bằng áp · PTFE body sleeve — ống lót thân PTFE · "
                "antistatic device — thiết bị chống tĩnh điện · incendiary "
                "spark — tia lửa gây cháy · fire exposure — chịu lửa · "
                "multiport — đa cổng · transflow / non-transflow — dòng "
                "chuyển tiếp / không chuyển tiếp · face-to-face dimension — "
                "kích thước mặt bích đến mặt bích · short / regular / "
                "venturi / full-area pattern — kiểu ngắn / thường / venturi "
                "/ cổng tròn đầy diện tích.")
    return ("<b>Key terms.</b> plug valve · cylindrical / taper plug · "
            "sealant · packing sleeve · follower nut · split plug · "
            "eccentric semi-plug · lift plug · balance hole · PTFE body "
            "sleeve · antistatic device · incendiary spark · fire exposure "
            "· multiport · transflow / non-transflow · face-to-face "
            "dimension · short / regular / venturi / full-area pattern.")


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

    # ------------------------------------------------------------ overview
    H("Van phích", "Plug valves")
    P("Van phích là van quay trong đó phần đóng dạng phích được quay từng "
      "bước 90° để cho cổng hoặc các lỗ trên phích khớp hay rời khỏi cổng "
      "trên thân van. Phích có dạng trụ như Hình 3-49 đến Hình 3-53, hoặc "
      "dạng côn như Hình 3-54 đến Hình 3-58. Van quay có phích hình cầu cũng "
      "thuộc họ van phích nhưng theo thông lệ gọi là van bi và được xét "
      "riêng ở trang 108.",
      "Plug valves are rotary valves in which a plug-shaped closure member "
      "is rotated through increments of 90° to engage or disengage a "
      "porthole or holes in the plug with the ports in the valve body. The "
      "plug may be cylindrical, as in Figures 3-49 to 3-53, or tapered, as "
      "in Figures 3-54 to 3-58. Rotary valves with ball-shaped plugs are "
      "likewise members of the plug valve family but are conventionally "
      "referred to as ball valves and are discussed separately on page 108.")
    P("Cổng thường có dạng chữ nhật ở phích trụ và dạng tam giác cụt ở phích "
      "côn. Các hình dạng này cho phép thân van mỏng và nhẹ hơn, đổi lại có "
      "chút tổn thất áp suất. Cổng tròn toàn diện tích thường chỉ dùng khi "
      "đường ống phải làm sạch bằng dụng cụ chạy ống hoặc tính chất chất "
      "lỏng đòi hỏi; một số van phích chỉ chế tạo cổng tròn do cách làm kín "
      "áp dụng.",
      "The port is commonly rectangular in parallel plugs and truncated "
      "triangular in taper plugs. These shapes permit a slimmer, lighter "
      "valve at the expense of some pressure drop. Full-area round-bore "
      "ports are normally used only if the pipeline has to be scraped or "
      "the nature of the fluid demands them; some plug valves are made only "
      "with round bores because of the method of sealing employed.")
    P("Van phích phù hợp nhất cho dừng và khởi động dòng cùng phân luồng, "
      "dù đôi khi cũng dùng khống chế vừa phải tùy dịch vụ và khả năng "
      "chống xói mòn của chỗ kín. Vì mặt kín chuyển động tẩy qua nhau và ở "
      "vị trí mở hoàn toàn được bảo vệ khỏi tiếp xúc với dòng chảy, van "
      "phích nói chung xử lý được chất lỏng có rắn lơ lửng.",
      "Plug valves are best suited to stopping and starting flow and flow "
      "diversion, though occasionally used for moderate throttling depending "
      "on the service and the erosion resistance of the seatings. Because "
      "the seatings move against each other with a wiping motion and are "
      "fully protected from the flowing fluid when open, plug valves are "
      "generally capable of handling fluids with solids in suspension.")

    # -------------------------------------------------- cylindrical plugs
    H("Van phích trụ", "Cylindrical plug valves")
    P("Khả năng sử dụng van phích phụ thuộc một phần vào cách tạo độ kín "
      "giữa phích và thân. Với van phích trụ có bốn cách thường dùng: dùng "
      "hợp chất làm kín, nở phích, dùng O-ring, và nêm phích lệch tâm vào "
      "chỗ kín.",
      "The use of plug valves depends in part on how the seal between plug "
      "and body is produced. For cylindrical plug valves four methods are "
      "frequently employed: a sealing compound, expanding the plug, O-rings, "
      "and wedging an eccentrically shaped plug into the seat.")
    P("Van Hình 3-49 là van phích trụ bôi trơn, độ kín phụ thuộc vào hợp chất "
      "làm kín giữa phích và thân. Hợp chất được đưa tới chỗ kín qua cán "
      "phích bằng vít hoặc súng bơm. Nhờ đó có thể khôi phục chỗ kín hỏng "
      "bằng cách bơm thêm hợp chất ngay khi van đang vận hành. Vì mặt kín "
      "được bảo vệ ở vị trí mở hoàn toàn và chỗ kín hỏng dễ phục hồi, van "
      "bôi trơn đặc biệt phù hợp chất lỏng mài mòn. Tuy không thiết kế để "
      "khống chế, đôi khi vẫn dùng cho mục đích đó; khống chế làm mất hợp "
      "chất trên mặt kín hở nên phải phục hồi mỗi lần đóng van.",
      "The valve of Figure 3-49 is lubricated: the seat seal depends on a "
      "sealing compound between plug and body, introduced through the plug "
      "shank by a screw or injection gun. A defective seat seal can "
      "therefore be restored by injecting more compound while the valve is "
      "in service. With seating surfaces protected when fully open and "
      "damage easily repaired, lubricated plug valves are particularly "
      "suited to abrasive fluids. They are not intended for throttling, "
      "though sometimes used for it: throttling removes the compound from "
      "exposed surfaces, so the seal must be restored each time the valve "
      "closes.")
    FIG(49, F5.fig_vsh_3_49())
    P("Bảo trì thủ công hợp chất thường là vấn đề con người; bơm tự động "
      "khắc phục nhưng tăng chi phí lắp đặt. Khi phích không quay được do "
      "thiếu bảo trì, chọn sai hợp chất hoặc kết tinh giữa hai mặt kín, van "
      "phải được vệ sinh hoặc sửa chữa.",
      "Manual maintenance of the sealing compound is often a human problem; "
      "automatic injection overcomes it but adds installation cost. When the "
      "plug becomes immovable through lack of maintenance, wrong compound "
      "selection or crystallisation between the seatings, the valve must be "
      "cleaned or repaired.")
    P("Ở van Hình 3-50 và 3-51, độ kín phụ thuộc vào khả năng nở phích ép vào "
      "chỗ kín. Phích Hình 3-50 có ống bọc đệm được đai ốc ép siết vào chỗ "
      "kín; đệm thường là amiang nén hoặc PTFE đặc. Nếu cần siết lại để phục "
      "hồi độ kín, phải làm khi van đang đóng để đệm không nở vào đường "
      "dòng. Van chỉ chế tạo cỡ nhỏ nhưng dùng được áp suất và nhiệt độ khá "
      "cao, thường để cô lập đồng hồ áp suất và đồng hồ mức.",
      "In the valves of Figures 3-50 and 3-51 the seat seal depends on the "
      "plug expanding against the seat. The plug in Figure 3-50 has a "
      "packing sleeve tightened against the seat by a follower nut; the "
      "packing is usually compressed asbestos or solid PTFE. If retightened "
      "to restore tightness, this must be done with the valve closed so the "
      "packing does not expand into the flow passage. Made only in small "
      "sizes, the valve serves fairly high pressures and temperatures, "
      "typically isolating pressure gauges and level gauges.")
    FIG(50, F5.fig_vsh_3_50())
    P("Phích Hình 3-51 gồm hai nửa được nêm tách ra, nêm chỉnh được từ bên "
      "ngoài. Độ kín do các vòng PTFE hẹp đặt trong mặt hai nửa phích; cách "
      "nạp và ép này cũng cho phép chặn kép xả trung gian. Van được thiết kế "
      "riêng cho nhiệm vụ cần thép không gỉ và hợp kim đắt, xử lý được hỗn "
      "dịch nhưng không chịu chất rắn mài mòn; chất quá dính cũng làm cơ cấu "
      "nêm không hoạt động. Trong giới hạn đó, van tỏ ra rất tin cậy khi "
      "thao tác thường xuyên.",
      "The plug of Figure 3-51 is split into two halves spread apart by a "
      "wedge adjustable from outside. Narrow PTFE rings inserted in the "
      "plug faces provide the seal; this method of sealing and seat loading "
      "also permits double block and bleed. The valve is intended for duties "
      "requiring stainless steel and other expensive alloys, and handles "
      "slurries but not abrasive solids; very tacky substances also render "
      "the wedging mechanism inoperable. Within these limits it has proved "
      "very reliable under frequent operation.")
    FIG(51, F5.fig_vsh_3_51())
    P("Hình 3-52 là van phích trụ song song có O-ring làm kín đặt trên các "
      "mỏm nhô ra của cổng thượng lưu và hạ lưu, tạo thành chỗ kín cho "
      "phích. Khi đóng, áp suất chất lỏng lọt qua O-ring thượng lưu vào "
      "khoang giữa phích và thân, ép O-ring hạ lưu tiếp xúc chặt với phích "
      "và mỏm cổng. Ứng dụng chính là hệ thủy lực áp suất cao.",
      "Figure 3-52 shows a parallel plug valve whose O-rings are mounted on "
      "spigot-like projections of the upstream and downstream ports, forming "
      "the seats for the plug. On closing, fluid pressure passes the "
      "upstream O-ring into the cavity between plug and body and forces the "
      "downstream O-ring into intimate contact with the plug and port "
      "projections. Its main application is high-pressure hydraulic systems.")
    FIG(52, F5.fig_vsh_3_52())
    P("Để giảm phần lớn ma sát giữa các mặt kín và điều khiển khả năng làm "
      "kín bằng momen tác dụng, phát triển van phích lệch tâm Hình 3-53: "
      "phích lệch tâm ăn khớp với mặt nổi trong thân. Cách tiếp xúc này dễ "
      "thao tác và xử lý được chất dính khó với các kiểu khác. Mặt kín có "
      "thể tiếp xúc kim loại hoặc bọc ê-lô-me/nhựa cùng với lớp lót thân.",
      "Efforts to eliminate most seating friction and to control sealing "
      "capacity by applied torque led to the eccentric plug valve of Figure "
      "3-53, in which an eccentric plug matches a raised face in the body. "
      "This method of seating is easy to operate and handles sticky "
      "substances difficult for other valve types. The seating faces may be "
      "in metallic contact or lined with an elastomer or plastic together "
      "with the body lining.")
    FIG(53, F5.fig_vsh_3_53())

    # ------------------------------------------------------- taper plugs
    H("Van phích côn", "Taper plug valves")
    P("Van phích côn cho phép chỉnh khe hở giữa các mặt kín bằng cách ép "
      "phích sâu hơn vào chỗ kín. Tùy thiết kế, phích có thể quay khi vẫn "
      "tiếp xúc chặt với thân, hoặc được nhấc ra khỏi thân trước khi quay "
      "rồi ép lại sau khi quay 90°.",
      "Taper plug valves permit the leakage gap between seatings to be "
      "adjusted by forcing the plug deeper into the seat. Depending on "
      "design, the plug may rotate while in intimate contact with the body, "
      "or be lifted out before rotation and reseated after rotating through "
      "90°.")
    P("Hình 3-54 là van phích côn chỗ kín kim loại không bôi trơn. Vì ma sát "
      "giữa các mặt kín cao, tải kín cho phép bị hạn chế để phích luôn quay "
      "được; khe hở vì thế khá rộng và van chỉ kín tốt với chất lỏng có sức "
      "căng bề mặt hoặc độ nhớt cao. Nếu phích được bôi mỡ trước khi lắp, "
      "van còn dùng được cho khí ướt như khí nén ẩm và có dầu.",
      "Figure 3-54 shows a taper plug valve with unlubricated metal seatings. "
      "Because friction is high, the permissible seating load is limited to "
      "keep the plug freely movable; the leakage gap is therefore relatively "
      "wide and the valve seals satisfactorily only with liquids of high "
      "surface tension or viscosity. If the plug is grease-coated before "
      "installation, the valve may also be used for wet gases such as wet "
      "and oily compressed air.")
    FIG(54, F5.fig_vsh_3_54())
    P("Van phích côn bôi trơn Hình 3-55 tương tự van phích trụ bôi trơn về "
      "nhiệm vụ, chỉ khác hình dạng phích, nhưng có một ưu điểm vận hành: "
      "nếu phích không quay được sau thời gian dài đứng yên hoặc do quên bôi "
      "trơn, bơm thêm hợp chất có thể nhấc phích khỏi chỗ kín vừa đủ để quay "
      "lại. Lúc đó không được nới lỏng ty ren như người dùng đôi khi vẫn "
      "làm, mà nên siết vừa phải. Ngược lại, siết quá tay có thể làm phích "
      "bị kẹt cứng.",
      "The lubricated taper plug valve of Figure 3-55 resembles the "
      "lubricated cylindrical type in duty, differing only in plug shape, "
      "but has one operational advantage: if the plug becomes immovable "
      "after a long static period or neglected lubrication, injecting more "
      "sealing compound can lift it just enough to move again. The gland "
      "should then not be slackened as users sometimes do, but rather "
      "judiciously tightened. Conversely, manual overtightening can seize "
      "the plug.")
    FIG(55, F5.fig_vsh_3_55())
    P("Van Hình 3-56 là van phích côn bôi trơn có phích lật ngược và tách "
      "khỏi trục. Vị trí phích được chỉnh bằng vít trong nắp van, còn chất "
      "làm kín bơm vào thân ở đầu trục. Để áp suất chất lỏng không đẩy phích "
      "vào chỗ kín, hai đầu phích có lỗ cân bằng áp cho chất lỏng vào khoang "
      "hai đầu. Nhờ đó van dùng được cho áp suất rất cao mà không bị kẹt do "
      "áp suất ép phích.",
      "In the valve of Figure 3-56 the lubricated taper plug is mounted "
      "inverted and divorced from the stem. Its position is adjusted by a "
      "screw in the valve cover while sealant is injected into the body at "
      "the stem end. To prevent fluid pressure driving the plug into the "
      "seat, the plug ends have balance holes admitting pressure to both "
      "end cavities. The valve may therefore be used at very high pressures "
      "without becoming inoperable.")
    FIG(56, F5.fig_vsh_3_56())
    P("Để giải quyết vấn đề bảo trì của van bôi trơn, Hình 3-57 dùng phích "
      "côn chạy trong ống lót PTFE. Ống lót giữ phích không bị dính, nhưng "
      "momen vẫn có thể khá cao do diện tích và ứng suất kín lớn. Ngược lại, "
      "diện tích kín lớn bảo vệ tốt khi mặt kín bị hư cục bộ; van chắc chắn, "
      "chịu được cách sử dụng thô, và ống lót cho phép chế tạo bằng vật liệu "
      "đặc biệt vốn dễ bị kẹt khi tiếp xúc trực tiếp. Van sửa được tại hiện "
      "trường, không cần xát phích.",
      "Efforts to overcome lubricated-valve maintenance led to the taper "
      "plug valve of Figure 3-57, whose plug moves in a PTFE body sleeve. "
      "The sleeve keeps the plug from sticking, though torque can still be "
      "relatively high because of the large seating area and stress. "
      "Conversely, the large area gives good protection against leakage "
      "after local damage; the valve is rugged, tolerates abusive treatment, "
      "and the sleeve permits exotic materials that would otherwise bind. "
      "It is easily repaired in the field and requires no lapping.")
    FIG(57, F5.fig_vsh_3_57())
    P("Van Hình 3-58 được thiết kế để loại bỏ phần lớn trượt giữa các mặt "
      "kín: cơ cấu bản lề nâng phích khỏi chỗ kín trước khi quay rồi ép lại "
      "sau khi quay tới vị trí mong muốn. Phích có thể bọc cao su và tự khóa "
      "nhờ độ côn. Đây là van đa cổng đồng hành với van phích lệch tâm Hình "
      "3-53.",
      "The valve of Figure 3-58 eliminates most sliding between seatings by "
      "a hinged lever arrangement that lifts the plug out of the body seat "
      "before rotation and reseats it afterwards. The plug may be rubber "
      "faced and is normally self-locking by its taper. It is a multiport "
      "companion valve to the eccentric plug valve of Figure 3-53.")
    FIG(58, F5.fig_vsh_3_58())

    # -------------------------------------------------- safety / fire / ports
    H("Thiết bị chống tĩnh điện", "Antistatic device")
    P("Ở van phích, chỗ kín và gioăng làm bằng vật liệu polyme như PTFE có "
      "thể cách điện phích và trục khỏi thân. Khi đó ma sát của dòng chảy "
      "có thể sinh điện tích trên phích và trục đủ lớn để tạo tia lửa gây "
      "cháy, đặc biệt với dòng hai pha. Nếu chất lỏng dễ cháy, van phải có "
      "thiết bị chống tĩnh điện bảo đảm thông mạch giữa phích, trục và thân.",
      "In plug valves, polymeric seats and packings such as PTFE can "
      "electrically insulate the plug and stem from the body. Friction from "
      "the flowing fluid may then generate an electrostatic charge high "
      "enough to produce an incendiary spark, more so with two-phase flow. "
      "For flammable fluids the valve must have an antistatic device giving "
      "electrical continuity between plug, stem and body.")
    H("Van phích chịu lửa", "Plug valves for fire exposure")
    P("Van phích có thể gặp cháy nhà máy khi xử lý chất dễ cháy phải vẫn kín "
      "bên trong và bên ngoài, và thao tác được trong và sau đám cháy. Mức "
      "chống cháy này đặc biệt khó đạt khi van vốn dùng polyme cho chỗ kín "
      "và gioăng trục. Thông lệ là bố trí chỗ kín kim loại phụ gần phích để "
      "phích nổi vào đó sau khi chỗ kín mềm bị phá hủy; gioăng trục mềm được "
      "thay bằng gioăng chịu lửa. Yêu cầu thử nghiệm và đánh giá tương tự "
      "van bi ở trang 108–109.",
      "Plug valves exposed to a plant fire while handling flammable fluid "
      "must remain essentially tight internally and externally and be "
      "operable during and after the fire. This is especially difficult "
      "when the valve relies on polymers for seat and stem seals. Common "
      "practice is an auxiliary metal seat close to the plug, against which "
      "the plug can float after the soft seat disintegrates; soft stem "
      "packing is replaced by fire-resistant packing. Test and evaluation "
      "requirements are similar to those for ball valves on pages 108–109.")
    H("Cấu hình đa cổng", "Multiport configuration")
    P("Van phích dễ bố trí đa cổng như Hình 3-59. Van có thể thiết kế dòng "
      "chuyển tiếp (transflow), cổng dòng thứ hai mở trước khi cổng thứ nhất "
      "đóng; hoặc không chuyển tiếp (non-transflow), cổng thứ nhất đóng "
      "trước khi cổng thứ hai mở. Dòng chuyển tiếp dùng khi không được ngắt "
      "dòng dù chỉ thoáng qua, ví dụ đầu ra của bơm thể tích dương không có "
      "van an toàn. Dòng không chuyển tiếp cần khi không cho phép chất lỏng "
      "chảy thoáng qua từ cổng này sang cổng kia, ví dụ đầu ra của bình "
      "đo; nhưng phích thường không thiết kế kín chất lỏng ở vị trí trung "
      "gian. Trong hầu hết ứng dụng thực tế, khi thao tác nhanh thì hai "
      "thứ tự này gần như không khác nhau.",
      "Plug valves adapt readily to multiport configurations such as Figure "
      "3-59. They may be designed for transflow, where the second passage "
      "opens before the first closes, or non-transflow, where the first "
      "closes before the second opens. Transflow suits duties in which flow "
      "cannot be momentarily interrupted, for example the outlet of a "
      "positive-displacement pump without a relief valve. Non-transflow may "
      "be required when momentary flow from one port to the other is not "
      "permissible, for example at the outlet of a measuring vessel; the "
      "plug is not normally intended to shut off fluid-tight in the "
      "intermediate position. In most practical applications with fairly "
      "quick operation there is little difference between the two.")
    FIG(59, F5.fig_vsh_3_59())
    P("Chiều dòng qua van phích đa cổng bôi trơn phải để áp suất chất lỏng "
      "ép phích vào cổng cần đóng. Nếu áp suất tác động ngược chiều, van "
      "phích bôi trơn sẽ không giữ được áp định mức.",
      "The direction of flow through lubricated multiport valves should be "
      "such that fluid pressure forces the plug against the port to be shut "
      "off. If pressure acts from the opposite direction, lubricated plug "
      "valves will not hold their rated pressure.")

    # -------------------------------------------------- dimensions/patterns
    H("Kích thước mặt–mặt và kiểu thân", "Face-to-face dimensions and patterns")
    P("Người soạn tiêu chuẩn Mỹ và Anh cho van phích gang và thép carbon đã "
      "cố làm cho kích thước mặt–mặt giống van cửa. Để vừa trong kích thước "
      "đó, ở cấp áp thấp phải nhượng bộ về diện tích dòng qua phích. Dù vậy "
      "van phích class 150 chỉ thay thế được van cửa đến DN 300 (NPS 12). "
      "Hạn chế này dẫn đến thêm dãy van dài cho class 150. Các kiểu sau đưa "
      "ra:",
      "Designers of U.S. and British standards for cast-iron and carbon-steel "
      "plug valves tried to make face-to-face dimensions identical to those "
      "of gate valves. To fit plug valves within those dimensions, "
      "concessions had to be made on flow area at the lower pressure ratings. "
      "Even so, class 150 plug valves are interchangeable with gate valves "
      "only up to DN 300 (NPS 12), which led to an additional long-series "
      "class 150 valve. The following patterns emerged:")
    U([("<b>Kiểu ngắn</b> — cổng phích diện tích giảm, mặt–mặt thay thế được "
        "van cửa; chỉ áp dụng đến DN 300 (NPS 12), class 150.",
        "<b>Short pattern</b> — reduced-area plug ports and face-to-face "
        "dimensions interchangeable with gate valves; sizes up to DN 300 "
        "(NPS 12) in class 150 only."),
       ("<b>Kiểu thường</b> — cổng lớn hơn kiểu ngắn và venturi; mặt–mặt "
        "thay thế được van cửa từ class 300 trở lên; bản class 150 dùng dãy "
        "dài, không thay thế được van cửa.",
        "<b>Regular pattern</b> — ports larger than short or venturi "
        "patterns; face-to-face interchangeable with gate valves for class "
        "300 and higher; class 150 uses a long series not interchangeable "
        "with gate valves."),
       ("<b>Kiểu venturi</b> — cổng diện tích giảm, cổ họng thân gần dạng "
        "venturi; thay thế được van cửa từ class 300 trở lên; class 150 dùng "
        "dãy dài.",
        "<b>Venturi pattern</b> — reduced-area ports and approximately "
        "venturi body throats; interchangeable with gate valves for class "
        "300 and higher; class 150 uses a long series."),
       ("<b>Kiểu cổng tròn đầy diện tích</b> — cổng tròn toàn diện tích xuyên "
        "van; mặt–mặt dài hơn các kiểu trên và không thay thế được van cửa.",
        "<b>Round-port full-area pattern</b> — full-area round ports; "
        "face-to-face longer than short, regular or venturi patterns and "
        "not interchangeable with gate valves.")])
    P("Phụ lục C liệt kê các tiêu chuẩn Hoa Kỳ và Anh liên quan đến van phích.",
      "Appendix C provides a list of U.S. and British standards pertaining "
      "to plug valves.")

    H("Ứng dụng", "Applications")
    P("Nhiệm vụ: dừng và khởi động dòng; khống chế vừa phải; phân luồng dòng.",
      "Duty: stopping and starting flow; moderate throttling; flow diversion.")
    P("Chất lỏng: khí; chất lỏng; hỗn dịch không mài mòn; hỗn dịch mài mòn "
      "với van phích bôi trơn; chất dính với van phích lệch tâm và phích "
      "nâng; xử lý hợp vệ sinh dược phẩm và thực phẩm; chân không.",
      "Fluids: gases; liquids; non-abrasive slurries; abrasive slurries for "
      "lubricated plug valves; sticky fluids for eccentric and lift plug "
      "valves; sanitary handling of pharmaceuticals and foodstuffs; vacuum.")

    H("Bảng tóm tắt các kiểu trong đơn vị", "Valve types in this unit")
    b.append(table(
        ["Hình", "Kiểu van", "Cách làm kín", "Đặc điểm chính"]
        if vi else
        ["Figure", "Valve type", "Sealing method", "Key feature"],
        [
            ["3-49", "Phích trụ bôi trơn / Lubricated cylindrical",
             "Hợp chất bôi kín / Sealing compound",
             "Bơm lại trong vận hành / In-service reseal"],
            ["3-50", "Phích trụ ống bọc đệm / Packing-sleeve cylindrical",
             "Đệm nén + đai ốc ép / Packing + follower nut",
             "Cỡ nhỏ, áp nhiệt cao / Small, high p/T"],
            ["3-51", "Phích tách đôi / Split plug",
             "Vòng PTFE + nêm / PTFE rings + wedge",
             "Chặn kép xả / Double block and bleed"],
            ["3-52", "Phích trụ O-ring / O-ring cylindrical",
             "O-ring trên mỏm cổng / O-rings on port spigots",
             "Thủy lực áp cao / High-pressure hydraulics"],
            ["3-53", "Bán phích lệch tâm / Eccentric semi-plug",
             "Mặt nổi thân / Raised body face",
             "Chất dính, momen điều khiển / Sticky fluids, torque control"],
            ["3-54", "Phích côn kim loại / Unlubricated taper",
             "Kim loại không bôi trơn / Dry metal",
             "Chất nhớt hoặc căng bề mặt cao / Viscous liquids"],
            ["3-55", "Phích côn bôi trơn / Lubricated taper",
             "Hợp chất làm kín / Sealant",
             "Bơm thêm nhấc phích / Sealant frees stuck plug"],
            ["3-56", "Phích lật ngược cân bằng áp / Inverted balanced",
             "Sealant + lỗ cân bằng / Sealant + balance holes",
             "Áp suất rất cao / Very high pressure"],
            ["3-57", "Phích côn ống lót PTFE / PTFE sleeve",
             "Ống lót thân PTFE / PTFE body sleeve",
             "Sửa tại chỗ, không xát / Field repair, no lapping"],
            ["3-58", "Phích nâng đa cổng / Multiport lift plug",
             "Mặt cao su tự khóa / Rubber face, self-locking",
             "Nâng trước khi quay / Lift before rotation"],
            ["3-59", "Cấu hình đa cổng / Multiport configurations",
             "—", "Dòng chuyển tiếp / không chuyển tiếp / Transflow / "
             "non-transflow"],
        ],
        caption=("Tóm tắt theo Hình 3-49…3-59 (văn bản nguồn, book pp. 97–108)."
                 if vi else
                 "Summary from Figures 3-49…3-59 (source text, book pp. 97–108)."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
