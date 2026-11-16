# -*- coding: utf-8 -*-
"""Book 6, Unit 6 — Manual Valves II: Piston & Parallel Gate Valves
(EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 74–84 (PDF pp. 88–98): parallel gate valves — conventional types
(Figures 3-25…3-28) and conduit gate valves (Figures 3-29…3-32), valve
bypass, pressure-equalizing connection with the locked-chamber pressure
chart (Figure 3-33), standards and applications.
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig3 as F3

PAGES_SRC = 11          # source book pp. 74-84
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Manual Valves II — Parallel Gate and Conduit Gate Valves"
TITLE_VI = "Van tay II — Van cửa song song và van cửa ống dẫn"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 6.</b> parallel gate valve — van cửa "
                "song song · slide gate valve — van cửa trượt · follower "
                "eyepiece — ống áp dẫn dòng · belt eye — vòng đai giữ đĩa · "
                "wedging mechanism — cơ cấu nêm · self-releasing — tự nhả · "
                "floating seat — chỗ kín phao · O-ring — vòng đệm tròn · "
                "double block and bleed — chặn kép xả trung gian · knife gate "
                "valve — van cửa dao · slurry — hỗn dịch · conduit gate "
                "valve — van cửa ống dẫn · porthole — cổng mở trên đĩa · "
                "skirt — váy chặn chất rắn · disc spring — lò xo đĩa · "
                "sealant — chất làm kín · valve bypass — đường tắt van · "
                "pressure-equalizing connection — nối cân bằng áp · "
                "revaporation — bay hơi lại.")
    return ("<b>Key terms.</b> parallel gate valve · slide gate valve · "
            "follower eyepiece · belt eye · wedging mechanism · "
            "self-releasing wedge · floating seat · O-ring · double block "
            "and bleed · knife gate valve · slurry · conduit gate valve · "
            "porthole · skirt · disc spring · sealant · valve bypass · "
            "pressure-equalizing connection · revaporation.")


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

    # -------------------------------------------------- parallel gate valves
    H("Van cửa song song", "Parallel gate valves")
    P("Van cửa song song có phần đóng là hai đĩa song song, giữa đó là cơ cấu "
      "nêm. Lực ép đĩa vào chỗ kín do áp suất chất lỏng tác động lên đĩa phao "
      "hoặc chỗ kín phao tạo ra; ở van hai đĩa, lực này có thể được bổ sung "
      "bằng lực cơ khí của cơ cấu nêm giữa hai đĩa.",
      "The closure member of a parallel gate valve consists of two parallel "
      "discs with a spreading mechanism in between. The force that presses "
      "the disc against the seat is controlled by the fluid pressure acting "
      "on either a floating disc or a floating seat. In twin-disc parallel "
      "gate valves this force may be supplemented with a mechanical force "
      "from a spreading mechanism between the discs.")
    P("Ưu điểm của van cửa song song là trở lực dòng thấp — ở van đường kính "
      "đầy, trở lực tiệm cận của một đoạn ống thẳng ngắn. Vì đĩa trượt ngang "
      "trên mặt chỗ kín, van cũng xử lý được chất lỏng mang chất rắn lơ lửng.",
      "One advantage of parallel gate valves is their low resistance to "
      "flow, which in the case of full-bore valves approaches that of a "
      "short length of straight pipe. Because the disc slides across the "
      "seat face, parallel gate valves are also capable of handling fluids "
      "which carry solids in suspension.")
    P("Cách làm việc đó cũng đặt ra một số hạn chế:",
      "This mode of operation also imposes some limitations on the use of "
      "parallel gate valves:")
    U([("Nếu áp suất chất lỏng thấp, lực ép kín có thể không đủ để tạo độ kín "
        "giữa hai mặt chỗ kín kim loại.",
        "If fluid pressure is low, the seating force may be insufficient to "
        "produce a satisfactory seal between metal-to-metal seatings."),
       ("Thao tác thường xuyên làm mòn mặt chỗ kín, tùy vào áp suất chất "
        "lỏng, chiều rộng mặt kín, tính bôi trơn của chất lỏng và khả năng "
        "chống mài mòn của vật liệu. Vì vậy van cửa song song thường chỉ "
        "dùng cho thao tác không thường xuyên.",
        "Frequent valve operation may lead to excessive wear of the seating "
        "faces, depending on the magnitude of fluid pressure, width of the "
        "seating faces, lubricity of the fluid to be sealed and the wear "
        "resistance of the seating material. For this reason, parallel gate "
        "valves are normally used for infrequent valve operation only."),
       ("Đĩa dẫn hướng lỏng và các chi tiết rời sẽ rung mạnh khi cắt dòng "
        "có mật độ và vận tốc cao.",
        "Loosely guided discs and loose disc components will tend to rattle "
        "violently when shearing high-density, high-velocity flow."),
       ("Đặc tính khống chế dòng của đĩa tròn đi ngang qua đường dòng tròn "
        "chỉ tốt từ vị trí đóng 50% đến đóng hoàn toàn. Do đó van cửa song "
        "song thường dùng cho nhiệm vụ on-off, dù một số kiểu đã được cải "
        "tiến để khống chế dòng, ví dụ bằng cách tạo rãnh chữ V ở chỗ kín.",
        "Flow control from a circular disc travelling across a circular "
        "flow passage becomes satisfactory only between the 50% closed and "
        "the fully closed positions. Parallel gate valves are therefore "
        "normally used for on-off duty only, though some types have been "
        "adapted for flow control, for example by V-porting the seat.")])
    P("Các van ở Hình 3-25 đến Hình 3-28 là van cửa song song thông thường; "
      "các van ở Hình 3-29 đến Hình 3-32 là van cửa ống dẫn (conduit gate). "
      "Loại sau là van đường kính đầy, khác ở chỗ đĩa bịt kín khoang thân "
      "van chống chất rắn lọt vào cả khi mở lẫn khi đóng. Vì vậy có thể dùng "
      "chúng trên đường ống cần làm sạch bằng dụng cụ chạy ống (pig).",
      "The valves shown in Figures 3-25 to 3-28 are conventional parallel "
      "gate valves; those in Figures 3-29 to 3-32 are conduit gate valves. "
      "The latter are full-bore valves which differ from the former in that "
      "the disc seals the valve body cavity against the ingress of solids "
      "in both the open and closed positions. Such valves may therefore be "
      "used in pipelines that have to be scraped.")

    # ------------------------------------------------- conventional types
    H("Van cửa song song thông thường", "Conventional parallel gate valves")
    P("Hình 3-25 cho thấy một trong những kiểu nổi tiếng nhất, thường gọi là "
      "van cửa trượt song song (parallel slide gate valve). Phần đóng gồm hai "
      "đĩa có lò xo ở giữa; lò xo giữ hai chỗ kín thượng lưu và hạ lưu tiếp "
      "xúc trượt và tăng tải kín khi áp suất chất lỏng thấp. Hai đĩa được "
      "mang trong vòng đai (belt eye) để không tách ra quá mức khi van mở "
      "hoàn toàn. Đường dòng của kiểu này có dạng venturi; khe giữa hai chỗ "
      "kín khi van mở hoàn toàn được ống áp (eyelet) bắc qua để dòng chảy "
      "được êm.",
      "Among the best-known conventional types is the parallel slide gate "
      "valve of Figure 3-25. Its closure member consists of two discs with "
      "springs in between; the springs keep the upstream and downstream "
      "seatings in sliding contact and improve the seating load at low "
      "fluid pressures. The discs are carried in a belt eye which prevents "
      "their unrestrained spreading as they move into the fully open "
      "position. The flow passage is venturi shaped, and the gap between "
      "the seats of the fully open valve is bridged by an eyelet to ensure "
      "smooth flow.")
    FIG(25, F3.fig_vsh_3_25())
    P("Cấu tạo này vừa kinh tế vừa giảm công thao tác và chi phí bảo trì; "
      "nhược điểm duy nhất là tăng nhẹ tổn thất áp suất qua van. Ứng suất "
      "kín đạt cực đại khi van gần đóng, lúc đó áp suất chênh lệch cũng gần "
      "cực đại nhưng diện tích tiếp xúc chỉ là một phần mặt kín. Khi đĩa đi "
      "từ vị trí đóng ba phần tư đến gần đóng, chất lỏng có xu hướng nghiêng "
      "đĩa vào lỗ chỗ kín gây mòn ở lỗ và mép ngoài đĩa; vì vậy mặt kín phải "
      "đủ rộng. Dù yêu cầu chiều rộng mặt kín vừa nhỏ để đạt ứng suất kín "
      "cao vừa lớn để hạn chế mòn, độ kín đạt được vẫn thỏa tiêu chí kín "
      "cấp hơi nước nếu áp suất chất lỏng không quá thấp.",
      "This construction offers economy, reduced operating effort and lower "
      "maintenance cost; the only disadvantage is a slight increase in "
      "pressure loss across the valve. The seating stress reaches its "
      "maximum when the valve is nearly closed, when the pressure drop is "
      "near maximum but only part of the seating area is in contact. As the "
      "disc travels from three-quarter closed to nearly closed, the flowing "
      "fluid tends to tilt the disc into the seat bore, so heavy wear may "
      "occur in the bore and on the outer edge of the disc. The seating "
      "width must therefore be appropriately wide — paradoxically small "
      "enough for high seating stress yet wide enough to limit wear. The "
      "fluid tightness achieved still satisfies the steam-class leakage "
      "criterion provided the fluid pressure is not too low.")
    P("Van cửa trượt song song có thêm nhiều ưu điểm: chỗ kín gần như tự "
      "chỉnh và không bị ảnh hưởng bởi chuyển động nhiệt của thân van. Khi "
      "van đã đóng ở trạng thái nguội, sự dãn nhiệt của trục không làm quá "
      "tải chỗ kín. Lúc đóng van cũng không cần định vị đĩa quá chính xác, "
      "nên cơ cấu điện có thể hạn hành trình — loại cơ cấu vừa kinh tế vừa "
      "tin cậy. Vì thế các nhà máy điện lớn thường chọn kiểu này làm van "
      "chặn. Van dùng được cho nhiều dịch vụ khác như nước, đặc biệt nước "
      "cấp lò hơi, và dầu.",
      "Parallel slide gate valves have further advantages: the seatings are "
      "virtually self-aligning and the seat seal is not impaired by thermal "
      "movements of the body. When the valve has been closed cold, thermal "
      "extension of the stem cannot overload the seatings. Nor is high "
      "accuracy in disc positioning necessary when closing, so an electric "
      "drive can be travel limited — an economical and reliable arrangement. "
      "For this reason larger power stations often prefer these valves as "
      "block valves. They are also used for many other services such as "
      "water, in particular boiler feed water, and oil.")
    P("Một biến thể dùng chủ yếu ở Hoa Kỳ (Hình 3-26) có phần đóng là hai đĩa "
      "và cơ cấu nêm ở giữa: khi chạm đáy thân van, cơ cấu nêm ép hai đĩa tách "
      "ra; khi mở lại, cơ cấu nhả đĩa. Góc nêm phải đủ lớn để tự nhả, nên tải "
      "bổ sung từ tác dụng nêm bị hạn chế. Để đĩa không tách sớm, van phải "
      "lắp trục thẳng đứng hướng lên; nếu bắt buộc lắp trục hướng xuống thì "
      "phải dùng lò xo đỡ nêm. Hiệu năng tương tự van cửa trượt song song, "
      "nhưng chất rắn và chất dính trong dòng có thể cản trở cơ cấu nêm, còn "
      "dãn nhiệt của trục có thể quá tải chỗ kín. Kiểu này chủ yếu dùng cho "
      "khí, nước và dầu.",
      "A variation used mainly in the United States (Figure 3-26) has two "
      "discs with a wedging mechanism between them: on contact with the "
      "bottom of the valve body the wedge spreads the discs, and on opening "
      "it releases them. The wedge angle must be wide enough for the wedge "
      "to be self-releasing, so the supplementary seating load is limited. "
      "To prevent premature spreading the valve must be mounted with the "
      "stem upright; if it must be mounted stem-down, the wedge needs spring "
      "support. Its performance largely matches that of the parallel slide "
      "gate valve, but solids and sticky substances in the fluid may "
      "interfere with the wedging mechanism and thermal extension of the "
      "stem can overload the seatings. It is used mainly in gas, water and "
      "oil services.")
    FIG(26, F3.fig_vsh_3_26())
    P("Van cửa song song thông thường cũng có thể lắp chỗ kín mềm như Hình "
      "3-27. Phần đóng là một đĩa mang hai vòng chỗ kín phao chịu nén bằng lò "
      "xo; mỗi vòng có một vòng đệm O-ring dán trên mặt và một vòng "
      "thứ hai ở chu vi. Khi đĩa về vị trí đóng, O-ring trên mặt vòng chạm "
      "chỗ kín thân van tạo lớp kín ban đầu; áp suất chất lỏng tác động lên "
      "mặt sau vòng sau đó ép chỗ kín khít thêm. Diện tích không cân bằng ở "
      "mặt sau vòng phao nhỏ hơn diện tích lỗ chỗ kín, nên tải kín ở một áp "
      "suất và cỡ van cho trước nhỏ hơn so với các kiểu kể trên. Tuy vậy O-ring "
      "cho độ kín cao ngay cả ở áp suất thấp, và nguyên lý này cho phép chặn "
      "kép xả trung gian.",
      "Conventional parallel gate valves may also be fitted with soft "
      "seatings, as in Figure 3-27. The closure member is a disc carrying "
      "two spring-loaded floating seating rings, each with a bonded O-ring "
      "on the face and a second O-ring on the periphery. On closing, the "
      "face O-ring contacts the body seat and produces the initial fluid "
      "seal; fluid pressure on the back of the ring then forces the seatings "
      "into still closer contact. Because the unbalanced area on the back "
      "of the floating rings is smaller than the area of the seat bore, the "
      "seating load for a given pressure and valve size is smaller than in "
      "the previously described valves. The O-ring nevertheless gives a "
      "high degree of tightness even at low fluid pressures, and this "
      "sealing principle also permits double block and bleed.")
    FIG(27, F3.fig_vsh_3_27())
    P("Hình 3-28 là van cửa dao (knife gate valve), thiết kế cho hỗn dịch "
      "kể cả vật liệu dạng sợi. Đĩa có mép dao cắt được sợi, còn thân van "
      "hầu như không có khoang chứa. Đĩa đi trong dẫn hướng ngang và được "
      "các móc ở đáy ép vào chỗ kín; nếu cần độ kín cao có thể thêm O-ring.",
      "The knife gate valve of Figure 3-28 is designed to handle slurries, "
      "including fibrous material. It owes this ability to the knife-edged "
      "disc, which cuts through fibres, and to the virtual absence of a "
      "valve body cavity. The disc travels in lateral guides and is forced "
      "against the seat by lugs at the bottom; an O-ring seat seal may be "
      "added when a high degree of fluid tightness is required.")
    FIG(28, F3.fig_vsh_3_28())

    # ----------------------------------------------------- conduit gates
    H("Van cửa ống dẫn", "Conduit gate valves")
    P("Bốn kiểu trong Hình 3-29 đến Hình 3-32 đại diện cho van cửa ống dẫn. "
      "Cả bốn đều có chỗ kín phao do áp suất chất lỏng ép vào đĩa.",
      "The four types in Figures 3-29 to 3-32 are representative of conduit "
      "gate valves. All four are provided with floating seats that are "
      "forced against the disc by the fluid pressure.")
    P("Chỗ kín của van Hình 3-29 được bọc PTFE và làm kín chu vi bằng O-ring. "
      "Đĩa được kéo dài ở đáy để nhận một cổng mở (porthole); khi van mở hoàn "
      "toàn, cổng này khớp với cổng thân van và đĩa bịt kín khoang thân, "
      "ngăn chất rắn lọt vào. Tác dụng kín của chỗ kín phao cũng cho phép "
      "chặn kép xả trung gian; nếu chỗ kín hỏng trong vận hành có thể bơm "
      "chất làm kín vào mặt chỗ kín để tạo lớp kín tạm thời.",
      "The seats of the valve in Figure 3-29 are faced with PTFE and sealed "
      "peripherally by O-rings. The disc is extended at the bottom to receive "
      "a porthole; when the valve is fully open, the porthole engages the "
      "valve ports so that the disc seals the body cavity against the "
      "ingress of solids. The floating-seat action also permits double "
      "block and bleed, and a temporary seat seal can be produced by "
      "injecting a sealant into the seat face if the seat seal fails in "
      "service.")
    FIG(29, F3.fig_vsh_3_29())
    P("Van Hình 3-30 khác ở chỗ đĩa gồm hai nửa có mặt tiếp xúc dạng nêm. "
      "Hai nửa liên kết với nhau và tách ra khi đi đến vị trí mở hoàn toàn "
      "hoặc đóng hoàn toàn, nhưng buông lỏng ở vị trí trung gian để đĩa di "
      "chuyển. Tùy mục đích sử dụng, mặt chỗ kín phao bằng kim loại hoặc có "
      "đệm PTFE. Để ngăn chất rắn lọt vào khoang thân trong suốt hành trình "
      "của đĩa, chỗ kín phao có váy (skirt) và đĩa trượt giữa hai váy. Van "
      "cũng cho phép chặn kép xả trung gian và có thể bơm chất làm kín tạm "
      "thời khi cần.",
      "The valve in Figure 3-30 differs in that the disc consists of two "
      "halves with a wedge-shaped interface. The halves are interlinked so "
      "that they wedge apart at the fully open or closed positions but "
      "relax in the intermediate position to permit travel. Depending on the "
      "use, the floating-seat faces may be metallic or provided with a PTFE "
      "insert. To prevent ingress of solids into the body cavity during all "
      "stages of disc travel, the floating seats have skirts between which "
      "the disc travels. This valve likewise permits double block and bleed, "
      "and a temporary seat seal can be provided by sealant injection.")
    FIG(30, F3.fig_vsh_3_30())
    P("Ở van Hình 3-31, tác dụng kín phụ thuộc vào chất làm kín được đưa tới "
      "mặt chỗ kín hạ lưu mỗi lần thao tác van. Chỗ kín phao mang các bể chứa "
      "đầy chất làm kín, trên có piston phao. Toàn bộ khoang van chứa mỡ "
      "truyền áp suất chất lỏng tới đỉnh piston của bể hạ lưu. Phần đóng gồm "
      "hai đĩa được lò xo tách ra. Cả chất làm kín và mỡ thân van đều được "
      "bổ sung từ bên ngoài trong khi van còn vận hành; một lần đầy bể đủ cho "
      "hơn 100 lần thao tác. Cách làm kín này đạt độ kín cao ở áp suất chất "
      "lỏng lớn.",
      "The sealing action of the valve in Figure 3-31 depends on a sealant "
      "fed to the downstream seat face each time the valve is operated. The "
      "floating seats carry reservoirs filled with sealant and topped by a "
      "floating piston. The entire valve chamber is filled with a grease "
      "which transmits fluid pressure to the top of the downstream piston. "
      "The closure member consists of two discs spread apart by springs. "
      "Both sealant and body grease can be replenished from outside while "
      "the valve is in service; each reservoir filling lasts for more than "
      "100 valve operations. This mode of sealing achieves a high degree of "
      "fluid tightness at high fluid pressures.")
    FIG(31, F3.fig_vsh_3_31())
    P("Van Hình 3-32 được thiết kế riêng cho vận chuyển than và quặng bằng "
      "thủy lực, và cho khí nhiễu nhiều bụi. Cửa là một tấm dày chịu mòn, có "
      "cổng mở ở đáy, trượt giữa hai chỗ kín phao được nén mạnh vào đĩa bằng "
      "lò xo đĩa. Chỗ kín có váy suốt hành trình của đĩa để ngăn chất rắn lọt "
      "vào khoang thân. Mặt đĩa và mặt chỗ kín bằng kim loại và được đánh "
      "bóng cao; khoang van chứa chất bôi trơn để bôi trơn mặt kín.",
      "The valve in Figure 3-32 is designed especially for the hydraulic "
      "transport of coal and ore and for heavily dust-laden gases. The gate "
      "is a heavy wear-resistant plate with a porthole at the bottom, "
      "sliding between two floating seats highly pre-stressed against the "
      "disc by disc springs. The seats have skirts for the full disc travel "
      "to prevent entry of solids into the body cavity. The disc and seat "
      "faces are metallic and highly polished, and the valve chamber is "
      "filled with a lubricant that ensures lubrication of the seating "
      "faces.")
    FIG(32, F3.fig_vsh_3_32())

    # ------------------------------------------------------------ bypass
    H("Đường tắt van", "Valve bypass")
    P("Ở van cửa song song lớn (trừ loại có chỗ kín phao), tải kín có thể "
      "rất cao khi áp suất chất lỏng lớn đến mức ma sát giữa các mặt kín làm "
      "khó nâng đĩa ra khỏi vị trí đóng. Vì vậy người ta thường lắp một đường "
      "tắt có van để giảm tải kín trước khi mở van. Không có quy tắc cứng "
      "nhanh về thời điểm dùng đường tắt; nên tham khảo khuyến nghị của nhà "
      "chế tạo, và một số tiêu chuẩn van cửa có quy định kích thước tối "
      "thiểu của đường tắt.",
      "The seating load of larger parallel gate valves (except those with "
      "floating seats) can become so high at high fluid pressures that "
      "friction between the seatings makes it difficult to raise the disc "
      "from the closed position. Such valves are therefore frequently "
      "provided with a valved bypass line used to relieve the seating load "
      "before opening. There are no fast rules about when to employ a "
      "bypass; the manufacturer's recommendation may be sought, and some "
      "gate-valve standards contain recommendations on the minimum bypass "
      "size.")
    P("Với khí và hơi ngưng tụ trong hệ thống hạ lưu nguội, việc tạo áp cho "
      "phía hạ lưu bị chậm đáng kể; trong trường hợp này đường tắt phải lớn "
      "hơn kích thước tối thiểu khuyến nghị.",
      "In the case of gases and vapours, such as steam, that condense in "
      "the cold downstream system, pressurization of the downstream system "
      "can be considerably retarded; the bypass line should then be larger "
      "than the minimum recommended size.")

    # ------------------------------------------------- pressure equalizing
    H("Nối cân bằng áp", "Pressure-equalizing connection")
    P("Ở van cửa song song hai đĩa thông thường như Hình 3-25 và Hình 3-26, "
      "sự giãn nhiệt của chất lỏng bị giam trong khoang van đẩy hai đĩa ép "
      "chặt hơn vào chỗ kín và làm áp suất khoang tăng. Ứng suất kín tăng "
      "lại càng khó nâng đĩa, và áp suất có thể nhanh chóng tới mức làm rò "
      "mối nối bích nắp hoặc biến dạng thân van. Vì vậy nếu dùng các van này "
      "cho chất lỏng có độ giãn nhiệt cao, phải có nối cân bằng áp nối "
      "khoang van với đường ống thượng lưu.",
      "In the conventional double-seated parallel gate valves of Figures "
      "3-25 and 3-26, thermal expansion of a liquid trapped in the closed "
      "valve chamber forces the upstream and downstream discs into more "
      "intimate contact with their seats and raises the chamber pressure. "
      "The higher seating stress in turn makes the discs harder to raise, "
      "and the pressure may quickly become high enough to leak at the bonnet "
      "flange joint or deform the valve body. Valves used with liquids of "
      "high thermal expansion must therefore have a pressure-equalizing "
      "connection linking the chamber to the upstream piping.")
    P("Áp suất khoang cũng tăng do bay hơi lại của nước ngưng bị giam, ví dụ "
      "khi van đóng chắn hơi nước. Ban đầu khoang van và đường ống thượng lưu "
      "đều có áp và đầy hơi; sau đó hơi nguội, ngưng tụ và một phần được "
      "thay bằng không khí. Khi khởi động lại, hơi đi vào đường ống thượng "
      "lưu và, vì chỗ kín thượng lưu thường không kín với áp thượng lưu, "
      "cũng vào khoang van. Một phần hơi mới tiếp tục ngưng cho đến khi "
      "thân van và ống đã đạt nhiệt độ bão hòa. Khi đó hơi bắt đầu sôi bay "
      "nước ngưng; nếu không có nối cân bằng áp, hơi giãn nở ép hai đĩa vào "
      "chỗ kín và đẩy áp suất khoang tăng. Độ lớn áp suất phụ thuộc vào "
      "nhiệt độ nước và mức độ đầy nước của khoang, có thể đọc từ Hình 3-33.",
      "Pressure rise may also be caused by revaporation of trapped "
      "condensate, as when these valves are closed against steam. Both the "
      "chamber and the upstream piping are initially pressurised and filled "
      "with steam; eventually the steam cools, condenses and is replaced to "
      "some extent by air. On restart, steam enters the upstream piping "
      "and, since the upstream seat is not normally fluid-tight against "
      "upstream pressure, enters the valve chamber. Some of the new steam "
      "condenses initially until the body and piping reach the saturation "
      "temperature. The steam then begins to boil off the condensate. "
      "Without a pressure-equalizing connection the expanding steam forces "
      "the discs into closer contact and raises the chamber pressure. Its "
      "magnitude depends on the water temperature and the degree of filling "
      "of the chamber with water, and may be obtained from Figure 3-33.")
    FIG(33, F3.fig_vsh_3_33())
    P("Nối cân bằng áp có thể là một lỗ trên đĩa thượng lưu hoặc bằng biện "
      "pháp bên trong hay bên ngoài khác. Với van dùng cho hơi nước, một số "
      "nhà chế tạo kiểu Hình 3-25 và Hình 3-26 kết hợp đường tắt với đường "
      "cân bằng áp.",
      "The pressure-equalizing connection may be a hole in the upstream "
      "disc or other internal or external means. Some makers of the valve "
      "types in Figures 3-25 and 3-26 combine the bypass line with a "
      "pressure-equalizing line when the valve is intended for steam.")
    P("Phụ lục C liệt kê các tiêu chuẩn Hoa Kỳ và Anh liên quan đến van cửa "
      "song song.",
      "Appendix C provides a list of U.S. and British standards pertaining "
      "to parallel gate valves.")

    # -------------------------------------------------------- applications
    H("Ứng dụng", "Applications")
    P("Nhiệm vụ: dừng và khởi động dòng; thao tác không thường xuyên.",
      "Duty: stopping and starting flow; infrequent operation.")
    P("Dịch vụ: khí; chất lỏng; chất lỏng mang chất rắn lơ lửng. Van cửa dao "
      "dùng cho hỗn dịch gồm bã, sợi, bột và hạt; cũng dùng cho chân không "
      "và dịch vụ nhiệt độ rất thấp (cryogenic).",
      "Service: gases; liquids; fluids with solids in suspension; knife "
      "gate valve for slurries, fibres, powders and granules; vacuum; "
      "cryogenic.")

    # ------------------------------------------------------------- summary
    H("Bảng tóm tắt các kiểu van trong đơn vị", "Valve types in this unit")
    b.append(table(
        ["Hình", "Kiểu van", "Chỗ kín", "Đặc điểm chính"]
        if vi else
        ["Figure", "Valve type", "Seating", "Key feature"],
        [
            ["3-25", "Van cửa trượt song song / Parallel slide gate",
             "Kim loại, lò xo giữa hai đĩa / Metal, springs between discs",
             "Đường dòng venturi, ống áp / Venturi passage, eyelet"],
            ["3-26", "Van hai đĩa có nêm / Twin disc with wedge",
             "Kim loại, cơ cấu nêm tự nhả / Metal, self-releasing wedge",
             "Lắp trục thẳng đứng / Stem upright mounting"],
            ["3-27", "Van cửa song song chỗ kín mềm / Soft-seated",
             "Vòng phao có O-ring / Floating rings with O-rings",
             "Kín ở áp thấp, chặn kép xả / Tight at low pressure, DB&B"],
            ["3-28", "Van cửa dao / Knife gate",
             "Chỗ kín O-ring tùy chọn / Optional O-ring seat",
             "Cắt sợi, gần như không có khoang thân / Cuts fibres, no cavity"],
            ["3-29", "Cửa ống dẫn, chỗ kín phao / Conduit gate, floating seats",
             "PTFE + O-ring chu vi / PTFE + peripheral O-rings",
             "Cổng mở đáy đĩa / Disc porthole"],
            ["3-30", "Cửa ống dẫn, đĩa giãn / Conduit gate, expandable disc",
             "Kim loại hoặc PTFE, có váy / Metal or PTFE, with skirts",
             "Hai nửa đĩa nêm ra / Two disc halves wedge apart"],
            ["3-31", "Cửa ống dẫn, bơm chất làm kín / Conduit gate, sealant",
             "Chỗ kín phao + chất làm kín / Floating seats + sealant",
             "Bơm tự động hạ lưu / Automatic downstream injection"],
            ["3-32", "Cửa ống dẫn, chỗ kín kim loại / Conduit gate, metal seats",
             "Kim loại đánh bóng, lò xo đĩa / Polished metal, disc springs",
             "Khoang đầy dầu / Oil-filled chamber"],
        ],
        caption=("Tóm tắt theo Hình 3-25…3-32 (văn bản nguồn, book pp. 74–84)."
                 if vi else
                 "Summary from Figures 3-25…3-32 (source text, book pp. 74–84)."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
