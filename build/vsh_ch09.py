# -*- coding: utf-8 -*-
"""Book 6, Unit 9 — Manual Valves V: Ball Valves (EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 108–119 (PDF pp. 122–133): ball valve sealing concept, seat materials,
four seating designs, pressure equalizing, antistatic and fire exposure,
cryogenic service, body construction and face-to-face dimensions
(Figures 3-60…3-68).
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig6 as F6

PAGES_SRC = 12          # source book pp. 108-119
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Manual Valves V — Ball Valves"
TITLE_VI = "Van tay V — Van bi"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 9.</b> ball valve — van bi · floating "
                "ball — bi nổi · trunnion-supported ball — bi đỡ bằng chốt · "
                "torsion seat — chỗ kín xoắn (môi công đòn) · cantilevered "
                "lip — môi công đòn · pressure-equalizing slot — rãnh cân "
                "bằng áp · diaphragm-supported seat — chỗ kín do màng đỡ · "
                "wedge seat — chỗ kín dạng nêm · squeeze ring — vòng ép kín · "
                "cold flow — chảy nguội · installed prestress — ứng suất ép "
                "lắp đặt · sealant injection — bơm chất làm kín · "
                "antistatic plunger — pít-tông chống tĩnh điện · fire-safe — "
                "chịu lửa · extended bonnet — nắp dài · reduced bore / "
                "full bore — đường kính trong thu nhỏ / đầy · face-to-face — "
                "mặt–mặt.")
    return ("<b>Key terms.</b> ball valve · floating ball · trunnion-supported "
            "ball · torsion seat · cantilevered lip · pressure-equalizing "
            "slot · diaphragm-supported seat · wedge seat · squeeze ring · "
            "cold flow · installed prestress · sealant injection · "
            "antistatic plunger · fire-safe · extended bonnet · reduced "
            "bore / full bore · face-to-face.")


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
    H("Van bi", "Ball valves")
    P("Van bi là một dạng van phích có phần đóng hình cầu. Chỗ kín ăn khớp "
      "với bi có dạng tròn nên ứng suất kín phân bố đều theo chu vi. Hầu hết "
      "van bi còn có chỗ kín mềm dễ theo sát mặt bi. Vì vậy về mặt làm kín, "
      "khái niệm van bi rất tốt; các van Hình 3-60 đến Hình 3-68 là đại diện "
      "cho các loại van bi hiện có.",
      "Ball valves are a species of plug valves with a ball-shaped closure "
      "member. The seat matching the ball is circular, so the seating stress "
      "is circumferentially uniform. Most ball valves also have soft seats "
      "that conform readily to the ball surface. From the sealing point of "
      "view the concept is excellent; the valves in Figures 3-60 to 3-68 are "
      "typical of those available.")
    P("Đặc tính khống chế dòng do cổng tròn đi ngang qua chỗ kín tròn và "
      "độ giảm áp kép qua hai chỗ kín tạo ra rất tốt. Tuy nhiên nếu van để "
      "hở một phần lâu dưới chênh áp lớn qua bi, chỗ kín mềm có thể chảy "
      "quanh mép lỗ bi và khóa bi tại vị trí đó. Vì vậy van bi thao tác tay "
      "phù hợp nhất cho dừng/khởi động dòng và khống chế vừa phải. Khi khống "
      "chế tự động, bi luôn chuyển động nên hư hỏng này thường không xảy ra.",
      "The flow-control characteristic from a round port moving across a "
      "circular seat and the double pressure drop across two seats is very "
      "good. If the valve is left partially open for long under a high "
      "pressure drop, however, the soft seat tends to flow around the edge "
      "of the ball orifice and may lock the ball in position. Manually "
      "operated ball valves are therefore best suited to stopping and "
      "starting flow and moderate throttling; with automatic control the "
      "ball is continuously moving and this failure does not normally occur.")
    P("Vì bi tẩy qua chỗ kín, van bi xử lý được chất lỏng mang rắn lơ lửng; "
      "nhưng chất rắn mài mòn làm hỏng chỗ kín và mặt bi, còn vật liệu sợi "
      "dài dai có thể quấn quanh bi. Để tiết kiệm, hầu hết van bi có đường "
      "kính trong thu nhỏ với đường dòng dạng venturi khoảng ba phần tư cỡ "
      "danh định. Tổn thất áp của kiểu thu nhỏ nhỏ đến mức van toàn lưu "
      "thường không đáng chi phí, trừ khi đường ống cần chạy dụng cụ làm "
      "sạch.",
      "Because the ball moves across the seats with a wiping motion, ball "
      "valves handle fluids with solids in suspension; abrasive solids "
      "damage the seats and ball surface, and long tough fibrous material "
      "may wrap around the ball. To economise, most ball valves have a "
      "reduced bore with a venturi-shaped passage about three-quarters of "
      "nominal size. The pressure drop is so small that full-bore valves "
      "are normally not justified, except when the pipeline must be scraped.")

    # ------------------------------------------------------ seat materials
    H("Vật liệu chỗ kín", "Seat materials")
    P("Vật liệu quan trọng nhất là PTFE: trơ với hầu hết hóa chất, hệ số "
      "ma sát thấp, phạm vi nhiệt độ rộng và làm kín tốt. Tuy nhiên PTFE có "
      "hệ số giãn nở lớn, dễ chảy nguội và dẫn nhiệt kém, nên thiết kế chỗ "
      "kín phải tính đến các tính chất đó. Vật liệu nhựa khác gồm PTFE độn, "
      "nylon và nhiều loại; chỗ kín càng cứng thì độ tin cậy làm kín càng "
      "giảm, nhất là ở chênh áp thấp. Ê-lô-me như buna-N cũng dùng được "
      "nhưng hạn chế về tương thích chất lỏng và nhiệt độ, lại dễ bám vào "
      "bi nếu chất lỏng không đủ bôi trơn. Với dịch vụ không dùng được chỗ "
      "kín mềm, có chỗ kín kim loại và gốm.",
      "The most important seat material is PTFE: inert to almost all "
      "chemicals, low friction, wide temperature range and excellent "
      "sealing. It also has a high expansion coefficient, susceptibility to "
      "cold flow and poor heat transfer, so the seat must be designed around "
      "these properties. Other plastics include filled PTFE, nylon and many "
      "more; as the material becomes harder, sealing reliability tends to "
      "suffer, particularly at low pressure differentials. Elastomers such "
      "as buna-N are also used but restrict fluid compatibility and "
      "temperature range and tend to grip the ball unless the fluid has "
      "sufficient lubricity. For services unsuitable for soft seatings, "
      "metal and ceramic seatings are used.")

    # ------------------------------------------------------- seating designs
    H("Thiết kế chỗ kín", "Seating designs")
    P("Tiếp xúc khít giữa các mặt kín đạt được bằng nhiều cách; bốn cách "
      "thường dùng là:",
      "Intimate contact between the seatings may be achieved in a number of "
      "ways; four frequently used ones are:")
    U([("Áp suất chất lỏng ép bi nổi vào chỗ kín — Hình 3-60 đến Hình 3-63.",
        "Fluid pressure forces a floating ball against the seat — Figures "
        "3-60 to 3-63."),
       ("Áp suất chất lỏng ép vòng chỗ kín phao vào bi đỡ bằng chốt — Hình "
        "3-64.",
        "Fluid pressure forces a floating seat ring against a "
        "trunnion-supported ball — Figure 3-64."),
       ("Chủ yếu dựa vào ứng suất ép lắp đặt giữa chỗ kín và bi đỡ chốt — "
        "Hình 3-65.",
        "Mainly installed prestress between the seats and a trunnion-"
        "supported ball — Figure 3-65."),
       ("Dùng lực cơ khí đưa vào bi và chỗ kín lúc đóng — Hình 3-66.",
        "A mechanical force applied to ball and seat on closing — "
        "Figure 3-66.")])
    P("Ngoài ra có van bi dùng vòng ép kín như O-ring. Cách thứ nhất, tải kín "
      "do áp suất chất lỏng tác động lên bi, phổ biến nhất; áp suất làm việc "
      "cho phép bị giới hạn bởi khả năng chịu tải của vòng chỗ kín hạ lưu "
      "ở nhiệt độ làm việc mà không biến dạng vĩnh cửu đáng kể.",
      "Ball valves are also available in which the seal is achieved by a "
      "squeeze ring such as an O-ring. The first method, with seating load "
      "regulated by fluid pressure on the ball, is the most common; the "
      "permissible pressure is limited by the downstream seat ring's ability "
      "to withstand fluid loading at working temperature without permanent "
      "gross deformation.")
    H("Chỗ kín xoắn và các biến thể bi nổi", "Torsion seats and floating-ball variants")
    P("Vòng chỗ kín Hình 3-60 và 3-61 có môi công đòn: lúc đầu bi chỉ tiếp "
      "xúc đầu môi. Vì hai chỗ kín được ép sẵn vào bi khi lắp, môi bị uốn và "
      "đưa vòng vào trạng thái xoắn. Lúc đóng chắn áp đường ống, môi chỗ kín "
      "hạ lưu uốn thêm cho đến khi toàn bộ mặt chỗ kín khớp với bi. Nhờ đó "
      "chỗ kín có tác dụng lò xo, làm kín tốt cả ở áp suất thấp, và cấu trúc "
      "đàn hồi tránh bị nghiền nát khi tải chất lỏng lớn.",
      "The seat rings of Figures 3-60 and 3-61 have a cantilevered lip: the "
      "ball initially contacts only the tip. As the upstream and downstream "
      "seats are pre-stressed against the ball on assembly, the lips deflect "
      "and put the rings into torsion. When closing against line pressure "
      "the downstream lip deflects further until the whole seat surface "
      "matches the ball. The seats thereby have spring action promoting "
      "good sealing even at low pressure, and their resilient construction "
      "keeps them from being crushed at high fluid loads.")
    FIG(60, F6.fig_vsh_3_60())
    P("Vòng chỗ kín Hình 3-60 còn có các rãnh cân bằng áp ở chu vi. Áp "
      "thượng lưu lọt qua rãnh vào khoang thân làm vòng chỗ kín thượng lưu "
      "được cân bằng áp, giảm ảnh hưởng của áp thượng lưu lên momen toàn "
      "van. Hình 3-61 dùng thân vào theo hướng trục.",
      "The seat rings of Figure 3-60 also have peripheral pressure-equalizing "
      "slots: upstream pressure filters past the upstream seat into the body "
      "cavity, balancing that seat and reducing its contribution to total "
      "valve torque. Figure 3-61 uses an axial-entry body.")
    FIG(61, F6.fig_vsh_3_61())
    P("Hình 3-62 và 3-63 cũng bảo đảm tải ép sẵn giữa các mặt kín. Ở Hình "
      "3-62, vòng chỗ kín được đỡ trên màng kim loại đóng vai trò lò xo "
      "phía sau, thân ghép kẹp. Ở Hình 3-63, lò xo từ trên ép cụm bi và vòng "
      "chỗ kín vào mặt nêm sau của chỗ kín trong thân một mảnh vào từ trên.",
      "Figures 3-62 and 3-63 also ensure preload between the seatings. In "
      "Figure 3-62 the seat rings are supported on metal diaphragms acting "
      "as springs behind them, in a sandwich-split body. In Figure 3-63 a "
      "spring forces the ball and seat-ring assembly from the top into "
      "wedge-shaped seat back faces in a one-piece top-entry body.")
    FIG(62, F6.fig_vsh_3_62())
    FIG(63, F6.fig_vsh_3_63())
    H("Bi đỡ bằng chốt", "Trunnion-supported balls")
    P("Hình 3-64 dùng cách thứ hai: áp suất chất lỏng ép vòng chỗ kín phao "
      "vào bi đỡ chốt, vòng được kín chu vi bằng O-ring. Vì diện tích "
      "không được cân bằng áp của vòng nhỏ, tải kín ở một cấp áp cho trước "
      "có thể điều chỉnh theo khả năng chịu của chỗ kín; van dùng được cho "
      "áp suất chất lỏng cao ngoài tầm kiểu bi nổi. Van còn có cơ cấu quay "
      "nhẹ vòng chỗ kín mỗi lần thao tác để phân bố đều mòn; nếu chỗ kín "
      "hỏng có thể bơm chất làm kín tạm thời.",
      "Figure 3-64 uses the second method: fluid pressure forces a floating "
      "seat ring against a trunnion-supported ball, the ring being sealed "
      "peripherally by an O-ring. Because the pressure-uncompensated area is "
      "small, seating load for a given rating can be regulated to the "
      "bearing capacity of the seat; the valve serves high pressures beyond "
      "the floating-ball range. A device rotates the seat rings slightly on "
      "each operation to distribute wear evenly, and a temporary seal can "
      "be made by injecting sealant if the seat fails.")
    FIG(64, F6.fig_vsh_3_64())
    P("Hình 3-65 dùng cách thứ ba: độ kín chủ yếu nhờ ứng suất ép lắp đặt "
      "giữa chỗ kín và bi đỡ chốt, nhằm hạn chế momen ở áp suất cao. Môi "
      "chỗ kín quanh cổng bi được bo tròn để giảm ghen khi bi ở vị trí mở; "
      "khi bi quay đến vị trí đóng, độ ghen tăng. Nếu yêu cầu chặn kép xả "
      "trung gian, mặt sau vòng chỗ kín phải có O-ring ê-lô-me.",
      "Figure 3-65 uses the third method: the seal depends mainly on "
      "installed prestress between seats and trunnion ball, limiting torque "
      "at high pressures. Lips around the ball ports are radiused to reduce "
      "seating interference when open; interference increases as the ball "
      "moves closed. For double block and bleed the back of the seat rings "
      "must carry an elastomeric O-ring.")
    FIG(65, F6.fig_vsh_3_65())
    P("Cách thứ tư dùng lực cơ khí lúc đóng để tránh phần lớn trượt giữa "
      "các mặt kín. Hình 3-66 dùng cơ cấu cam nâng bi ra khỏi chỗ kín trước "
      "khi mở và ép bi trở lại sau khi đóng.",
      "The fourth method applies mechanical force on closing to avoid most "
      "sliding between seatings. Figure 3-66 uses a cam mechanism that lifts "
      "the ball out of the seat before opening and forces it back after "
      "closing.")
    FIG(66, F6.fig_vsh_3_66())

    # ------------------------------------------------ pressure equalizing
    H("Nối cân bằng áp", "Pressure-equalizing connection")
    P("Van bi hai chỗ kín có thể có khoang thân kín ở cả vị trí mở lẫn đóng. "
      "Khi đóng, khoang kín nằm giữa hai chỗ kín; khi mở, có thể có thêm "
      "khoang kín giữa bi và thân. Nếu các khoang này chứa chất lỏng giãn "
      "nhiệt lớn, áp suất tăng do nhiệt có thể quá tải một số chi tiết nếu "
      "không xả được áp dư. Khoang giữa bi và thân thường được xả vào "
      "đường dòng qua lỗ ở cạnh trên hoặc dưới của bi.",
      "Double-seated ball valves may have a sealed body cavity in both open "
      "and closed positions: between the seats when closed, and possibly "
      "between ball and body when open. Liquid of high thermal expansion in "
      "these cavities may overstress components unless excess pressure is "
      "relieved. The cavity between ball and body is normally relieved to "
      "the flow passage through a hole in the top or bottom flank of the "
      "ball.")
    P("Khi van đóng, áp dư giữa hai chỗ kín được xả khác nhau. Ở van chỗ kín "
      "phao như Hình 3-64, áp dư trong thân mở chỗ kín thượng lưu tại chỗ "
      "có chênh áp nhỏ nhất. Ở van hai chỗ kín khác, áp chất lỏng phải "
      "thắng ứng suất ép sẵn giữa bi và chỗ kín thượng lưu. Nếu vòng chỗ "
      "kín có tác dụng lò xo như Hình 3-60 đến 3-62, áp có thể mở chỗ kín "
      "thượng lưu trước khi quá cao; nếu vòng cứng hơn, sự giãn nhiệt có "
      "thể sinh áp rất cao và cạnh thượng lưu của bi thường có lỗ cân "
      "bằng áp — khi đó dòng chỉ đi một chiều. Nếu catalog không nói rõ, "
      "nên hỏi nhà chế tạo. Nối cân bằng áp thường không phải tiêu chuẩn, "
      "trừ dịch vụ nhiệt độ rất thấp, vì nhựa trở nên cứng và chống mở "
      "chỗ kín thượng lưu.",
      "When closed, excess pressure between the seats is relieved in various "
      "ways. With floating seats as in Figure 3-64, excess body pressure "
      "opens the upstream seat seal where the pressure differential is "
      "least. In other double-seated valves the fluid pressure must overcome "
      "prestress between ball and upstream seat. Springing seat rings as in "
      "Figures 3-60 to 3-62 may let the upstream seal open without excessive "
      "pressure; more rigid rings may allow thermal expansion to create "
      "excessive pressure, and the upstream flank of the ball is then "
      "usually provided with a pressure-equalizing hole, permitting flow in "
      "one direction only. If the catalogue is silent, consult the maker. "
      "Such a connection is not normally standard except for cryogenic "
      "service, where plastics become rigid and resist opening.")

    # ---------------------------------------------------- safety & special
    H("Thiết bị chống tĩnh điện", "Antistatic device")
    P("Chỗ kín và gioăng polyme có thể cách điện bi và trục khỏi thân, nên "
      "van bi có thể cần thiết bị chống tĩnh điện như đã nêu cho van phích "
      "trang 98. Hình 3-67 cho thấy thiết bị điển hình gồm pít-tông nén lò "
      "xo: một đặt giữa lưỡi trục và bi, một giữa trục và thân.",
      "Polymeric seats and packings can insulate the ball and stem from the "
      "body, so ball valves may need an antistatic device for the reasons "
      "given for plug valves on page 98. Figure 3-67 shows a typical device "
      "of spring-loaded plungers: one between the stem tongue and the ball, "
      "a second between the stem and the body.")
    FIG(67, F6.fig_vsh_3_67())
    H("Van bi chịu lửa", "Ball valves for fire exposure")
    P("Chỗ kín mềm sẽ phá hủy nếu van chịu lửa đủ lâu. Với chất dễ cháy, van "
      "phải được thiết kế để mất chỗ kín mềm do cháy bên ngoài không gây rò "
      "rỉ lớn bên trong hay bên ngoài. Thiết kế như vậy có chỗ kín và gioăng "
      "khẩn cấp hoạt động sau khi chỗ kín chính hỏng: chỗ kín kim loại phụ "
      "sắc mép hoặc vát cạnh đặt gần bi để bi nổi vào sau khi vòng mềm bị "
      "phá hủy; hộp đón dùng gioăng amiang hoặc graphit nguyên chất bổ sung.",
      "Soft seat and stem seals disintegrate under sufficiently long fire "
      "exposure. Valves for flammable fluids must be designed so that loss "
      "of the soft seals in an external fire does not cause gross internal "
      "or external leakage. Such designs provide emergency seat and stem "
      "seals that operate after the primary seals fail: a sharp-edged or "
      "chamfered secondary metal seat close to the ball, against which the "
      "ball floats after the soft rings disintegrate; the stuffing box may "
      "have auxiliary asbestos-based or pure graphite packing, or be made "
      "entirely of such material.")
    P("Nhiều tiêu chuẩn quy định thử nghiệm và đánh giá van bi chỗ kín mềm "
      "khi chịu lửa; ba tiêu chuẩn cơ bản là BS 5146, API 607 và API RP 6F. "
      "BS 5146 bắt nguồn từ OCMA FA VI, vốn lấy từ quy định thử của Esso "
      "Petroleum ở Anh; thử nghiệm đó khác các thử trước ở chỗ yêu cầu van "
      "mở trong lúc thử và dùng chất lỏng dễ cháy, vì trong cháy thực tế "
      "nhiều van đang mở và sau đó phải đóng được. Nhiều tổ chức đang tiến "
      "tới tiêu chuẩn thử lửa quốc tế.",
      "Numerous standards cover fire testing of soft-seated ball valves; the "
      "three basic ones are BS 5146, API 607 and API RP 6F. BS 5146 derives "
      "from OCMA FA VI, itself taken from an Esso Petroleum UK test "
      "specification. That test differed from earlier ones by requiring the "
      "valve to be open during the test with a flammable liquid in it, "
      "recognising that in a real plant fire many valves are open and must "
      "subsequently be closed. Several standards bodies are moving toward "
      "an international fire-test specification.")
    P("Cần quan tâm không chỉ thử lửa van bi mà cả ảnh hưởng của lửa lên "
      "toàn hệ thống xử lý chất lỏng, gồm van khác, bộ truyền, bơm, bộ lọc, "
      "bình áp lực và nhất là bích, bulông và gioăng đường ống. Van đã qua "
      "thử lửa được gọi là fire-safe, nhưng thuật ngữ này bị nhà chế tạo "
      "từ chối về mặt trách nhiệm sản phẩm.",
      "Attention must also be paid to the effect of fire on the whole fluid "
      "system — other valves, operators, pumps, filters, pressure vessels "
      "and especially pipe flanges, bolting and gaskets. Fire-tested valves "
      "are referred to as fire-safe, a term unacceptable to manufacturers "
      "from a product-liability standpoint.")
    H("Cấu hình đa cổng", "Multiport configuration", h3)
    P("Van bi thích nghi với cấu hình đa cổng tương tự van phích đã xét "
      "trang 98.",
      "Ball valves adapt to multiport configurations in a manner similar to "
      "plug valves discussed on page 98.")
    H("Van bi cho dịch vụ nhiệt độ rất thấp", "Ball valves for cryogenic service", h3)
    P("Van bi dùng rộng rãi ở nhiệt độ rất thấp nhưng phải thiết kế riêng. "
      "Yếu tố chính là hệ số co nhiệt của vật liệu vòng chỗ kín thường cao "
      "hơn thép không gỉ của bi và thân; ở nhiệt độ thấp vòng co lại vào "
      "bi, momen tăng, nặng có thể vỡ vòng. Có thể giảm ứng suất ép lắp đặt "
      "để đạt ứng suất đúng ở nhiệt độ cryogenic, nhưng độ kín ở áp thấp "
      "có thể không tốt nếu van cũng làm việc ở nhiệt độ thường. Biện pháp "
      "khác: đỡ chỗ kín trên màng kim loại dẻo, chọn vật liệu co ít hơn "
      "PTFE nguyên chất như PTFE độn graphit hoặc carbon, hoặc chế tạo vòng "
      "thép không gỉ có đệm PTFE với hàm lượng PTFE tối thiểu.",
      "Ball valves are used extensively in cryogenic services but their "
      "design must be adapted. A main consideration is the thermal "
      "contraction coefficient of the seat ring, normally higher than that "
      "of the stainless ball and body: the ring shrinks onto the ball, "
      "operating torque increases and in severe cases the ring may split. "
      "Installed prestress may be reduced to give the correct value at "
      "cryogenic temperature, though tightness at low pressure may then "
      "suffer at ambient temperature. Other means include flexible metal "
      "diaphragms, seat materials with much lower contraction such as "
      "graphite- or carbon-filled PTFE, or stainless rings with minimum "
      "PTFE inserts.")
    P("Vì nhựa trở nên cứng ở nhiệt độ cryogenic, chất lượng bề mặt và độ "
      "cầu của bi phải cao để đạt độ kín. Như các van cryogenic khác, nắp "
      "dài không được đặt quá 45° so với phương thẳng đứng để gioăng trục "
      "làm việc hiệu quả.",
      "Because plastic seat materials become rigid at cryogenic temperature, "
      "surface finish and ball sphericity must be of a high standard for "
      "tight sealing. As with other cryogenic valves, the extended bonnet "
      "should be no more than 45° from upright for an effective stem seal.")

    # -------------------------------------------------- body & dimensions
    H("Các kiểu thân van", "Variations of body construction")
    P("Có nhiều cách tiếp cận bên trong van bi, dẫn tới các kiểu thân khác "
      "nhau như Hình 3-68. Thân một mảnh có ít mối nối chịu ứng suất đường "
      "ống nhất nên thường chọn cho chất lỏng nguy hiểm; dạng thân kín hay "
      "dùng khi chôn. Thân một mảnh vào từ trên và các kiểu ghép cho phép "
      "dễ tiếp cận bên trong; với van hàn trong đường ống, kiểu vào từ trên "
      "có thể sửa tại chỗ. Lựa chọn thường là sở thích cá nhân.",
      "Access to ball valve internals can be provided in various ways, "
      "leading to the body constructions of Figure 3-68. A one-piece body "
      "has the fewest joints subject to pipeline stress and is often chosen "
      "for hazardous fluids; the sealed variant is frequent for buried "
      "service. One-piece top-entry and split bodies give easy internal "
      "access; welded-in-line valves with top entry can be serviced in situ. "
      "Selection is often a matter of personal preference.")
    FIG(68, F6.fig_vsh_3_68())
    H("Kích thước mặt–mặt", "Face-to-face dimensions")
    P("Ban đầu nhà chế tạo Mỹ lấy kích thước mặt–mặt của van bi bích theo "
      "tiêu chuẩn van gần nhất để tiết kiệm vật liệu — đó là tiêu chuẩn van "
      "cửa; nhưng class 150 và class 300 cỡ DN 200 (NPS 8) đến DN 300 (NPS "
      "12) chỉ cho phép cấu trúc đường kính thu nhỏ. Năm 1961, khi nhà sản "
      "xuất Anh cũng đưa van bi bích vào, nhu cầu van toàn lưu tăng lên; "
      "không vừa trong kích thước van cửa, họ dùng kích thước van phích "
      "kiểu thường. Vì vậy có hai dãy mặt–mặt cho class 150 và cho cỡ DN "
      "200–300 class 150: một dãy đường kính thu nhỏ, một dãy toàn lưu. Ở "
      "cấp áp cao hơn, kích thước van cửa chứa được cả hai kiểu.",
      "U.S. manufacturers originally made flanged ball valve face-to-face "
      "dimensions to the nearest valve standard for minimum material — the "
      "gate valve standard — but class 150 and class 300 sizes DN 200 (NPS "
      "8) to DN 300 (NPS 12) permitted only reduced-bore construction. In "
      "1961 UK makers introduced flanged ball valves with a demand for "
      "full-bore types; when these would not fit gate-valve dimensions, "
      "regular-pattern plug-valve dimensions were adopted. Thus short and "
      "long series exist for class 150 and for DN 200–300 class 300 — one "
      "for reduced-bore, one for full-bore valves. At higher ratings gate-"
      "valve dimensions accommodate both.")
    P("Tiêu chuẩn chủ đạo cho mặt–mặt là ISO 5752, gồm mọi kích thước được "
      "công nhận trên thế giới; tuy nhiên ISO 5752 không định nghĩa đường "
      "kính thu nhỏ hay toàn lưu, trừ cỡ DN 200–300 class 300. Phụ lục C "
      "liệt kê tiêu chuẩn Mỹ và Anh về van bi.",
      "The master standard for face-to-face dimensions is ISO 5752, covering "
      "all recognised dimensions worldwide; it does not define reduced or "
      "full bore except for class 300 sizes DN 200–300. Appendix C lists "
      "U.S. and British standards pertaining to ball valves.")

    H("Ứng dụng", "Applications")
    P("Nhiệm vụ: dừng và khởi động dòng; khống chế vừa phải; phân luồng dòng.",
      "Duty: stopping and starting flow; moderate throttling; flow diversion.")
    P("Dịch vụ: khí; chất lỏng; hỗn dịch không mài mòn; chân không; nhiệt độ "
      "rất thấp.",
      "Service: gases; liquids; non-abrasive slurries; vacuum; cryogenic.")

    H("Bảng tóm tắt các thiết kế trong đơn vị", "Ball valve designs in this unit")
    b.append(table(
        ["Hình", "Thiết kế", "Cách tạo độ kín", "Đặc điểm chính"]
        if vi else
        ["Figure", "Design", "Sealing method", "Key feature"],
        [
            ["3-60", "Bi nổi, chỗ kín xoắn / Floating, torsion",
             "Áp chất lỏng ép bi / Fluid pressure on ball",
             "Rãnh cân bằng áp / Pressure-equalizing slots"],
            ["3-61", "Bi nổi, thân vào trục / Axial entry",
             "Chỗ kín xoắn / Torsion seats",
             "Thân vào theo trục / Axial-entry body"],
            ["3-62", "Bi nổi, màng đỡ / Diaphragm seats",
             "Màng kim loại làm lò xo / Metal diaphragm springs",
             "Thân ghép kẹp / Sandwich-split body"],
            ["3-63", "Bi nổi, chỗ kín nêm / Wedge seats",
             "Lò xo từ trên / Top spring",
             "Thân một mảnh vào trên / One-piece top entry"],
            ["3-64", "Bi đỡ chốt, chỗ kín phao / Trunnion, floating seats",
             "Áp ép vòng vào bi / Pressure on seat ring",
             "Tự quay vòng chỗ kín / Seat rotation, sealant"],
            ["3-65", "Bi đỡ chốt, chỗ kín nêm / Trunnion, wedge",
             "Ứng suất ép lắp đặt / Installed prestress",
             "Môi bo tròn giảm momen / Radiused lips, low torque"],
            ["3-66", "Cơ cấu cam / Cam mechanism",
             "Lực cơ khí lúc đóng / Mechanical closing force",
             "Nâng bi trước khi mở / Lift ball before opening"],
            ["3-67", "Chống tĩnh điện / Antistatic",
             "Pít-tông nối trục–bi–thân / Plungers",
             "Tránh tia lửa / Prevents incendiary spark"],
            ["3-68", "Kiểu thân / Body construction",
             "—", "Một mảnh, ghép, vào trên, kín / One-piece, split, "
             "top entry, sealed"],
        ],
        caption=("Tóm tắt theo Hình 3-60…3-68 (văn bản nguồn, book pp. 108–119)."
                 if vi else
                 "Summary from Figures 3-60…3-68 (source text, book pp. 108–119)."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
