# -*- coding: utf-8 -*-
"""Book 6, Unit 7 — Manual Valves III: Wedge Gate Valves (EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 85–96 (PDF pp. 99–110): wedge gate valves — plain, self-aligning and
rubber-seated designs (Figures 3-34…3-45), wedge-to-stem connection,
wedge guide design, a failure case study (Figures 3-46…3-48), standards
and applications.
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig4 as F4

PAGES_SRC = 12          # source book pp. 85-96
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Manual Valves III — Wedge Gate Valves"
TITLE_VI = "Van tay III — Van cửa nêm"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 7.</b> wedge gate valve — van cửa nêm · "
                "plain wedge — nêm đặc/rỗng dạng cơ bản · hollow wedge — nêm "
                "rỗng · flexible wedge — nêm linh hoạt · two-piece wedge — "
                "nêm hai mảnh · spacer ring — vòng đệm chỉnh · hard-faced — "
                "phủ vật liệu cứng chịu mòn · guide rib / guide slot — gờ / "
                "rãnh dẫn · self-aligning — tự chỉnh · rubber-lined — bọc cao "
                "su · diaphragm — màng ngăn · T-slot — rãnh chữ T · "
                "torque-limited drive — cơ cấu hạn momen · travel-limited — "
                "hạn hành trình · block-and-bleed — chặn và xả · bottom "
                "cavity — khoang đáy thân van.")
    return ("<b>Key terms.</b> wedge gate valve · plain wedge · hollow wedge "
            "· flexible wedge · two-piece wedge · spacer ring · hard-faced "
            "guide · guide rib / slot · self-aligning wedge · rubber-lined "
            "wedge · diaphragm · T-slot · torque-limited drive · "
            "travel-limited drive · block-and-bleed · bottom cavity.")


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
    H("Van cửa nêm", "Wedge gate valves")
    P("Van cửa nêm khác van cửa song song ở chỗ phần đóng có dạng nêm thay vì "
      "song song, như Hình 3-34 đến Hình 3-45. Dạng nêm tạo ra tải kín bổ "
      "sung lớn, giúp van cửa nêm chỗ kín kim loại kín được cả ở áp suất chất "
      "lỏng cao lẫn thấp. Độ kín đạt được vì thế cao hơn về mặt lý thuyết so "
      "với van cửa song song thông thường chỗ kín kim loại. Tuy nhiên tải kín "
      "phía thượng lưu thường không đủ lớn để cho phép chặn và xả (block-and-"
      "bleed) ở van cửa nêm chỗ kín kim loại.",
      "Wedge gate valves differ from parallel gate valves in that the closure "
      "member is wedge-shaped instead of parallel, as shown in Figures 3-34 "
      "to 3-45. The purpose of the wedge shape is to introduce a high "
      "supplementary seating load that enables metal-seated wedge gate "
      "valves to seal not only against high but also low fluid pressures. "
      "The degree of tightness achievable is therefore potentially higher "
      "than with conventional metal-seated parallel gate valves. The "
      "upstream seating load is not normally high enough, however, to permit "
      "block-and-bleed operation of metal-to-metal seated wedge gate valves.")
    P("Thân van có gờ dẫn hoặc rãnh dẫn để đĩa nêm trượt. Mục đích chính của "
      "dẫn hướng là giữ nêm rời khỏi chỗ kín hạ lưu, trừ một đoạn ngắn gần vị "
      "trí đóng, nhằm giảm mòn giữa các mặt kín. Mục đích thứ hai là ngăn đĩa "
      "xoay quá mức khi đi giữa hai vị trí mở và đóng. Nếu có xoay, đĩa trước "
      "hết bị kẹt một bên giữa hai mặt kín thân van, rồi tự xoay về đúng vị "
      "trí trước khi đi tiếp đến vị trí kín cuối cùng. Một số kiểu, như Hình "
      "3-45, không cần dẫn hướng vì nêm do màng nâng đỡ.",
      "The bodies of these valves carry guide ribs or slots in which the disc "
      "travels. The main purpose is to carry the wedge away from the "
      "downstream seat except near the closed position, so as to minimise "
      "wear between the seatings. A second purpose is to prevent excessive "
      "rotation of the disc between the open and closed positions. If some "
      "rotation occurs, the disc initially jams on one side between the body "
      "seatings and then rotates into the correct position before travelling "
      "into the final seating position. Some types, such as Figure 3-45, can "
      "dispense with a wedge guide because the wedge is carried by a "
      "diaphragm.")
    P("So với van cửa song song, van cửa nêm có thêm một số nhược điểm:",
      "Compared with parallel gate valves, wedge gate valves have some "
      "negative features:")
    U([("Không bố trí được ống dẫn dòng theo (follower conduit) thuận tiện "
        "như van cửa song song.",
        "Wedge gate valves cannot accommodate a follower conduit as "
        "conveniently as parallel gate valves can."),
       ("Khi đĩa tiến lại gần chỗ kín, chất rắn trong dòng có thể bị kẹt giữa "
        "hai mặt kín. Tuy nhiên van cửa nêm chỗ kín cao su (Hình 3-44, 3-45) "
        "vẫn kín được quanh hạt rắn nhỏ bị kẹt.",
        "As the disc approaches the seat, the seatings may trap solids "
        "carried by the fluid. Rubber-seated wedge gate valves (Figures 3-44 "
        "and 3-45), however, are capable of sealing around small trapped "
        "solids."),
       ("Cơ cấu điện phức tạp hơn vì phải hạn momen thay vì hạn hành trình. "
        "Momen phải đủ lớn để nêm vào chỗ kín khi đóng chắn toàn bộ chênh áp "
        "đường ống; nếu đóng ở chênh áp bằng không thì lực nêm càng lớn. Để "
        "mở lại được chắn chênh áp đầy đủ, và để dự phòng tăng lực thao tác "
        "do dãn nhiệt, bộ truyền động phải được chọn dư lớn.",
        "An electrical drive must be torque-limited rather than travel-"
        "limited. Its torque must be high enough to wedge the wedge into the "
        "seats when closing against full differential line pressure; closing "
        "against zero differential pressure makes the wedging still higher. "
        "To permit reopening against full differential pressure and to allow "
        "for increased effort from thermal movements, the operator must be "
        "generously sized.")])
    P("Các hạn chế khác của van cửa nêm tương tự van cửa song song.",
      "The limitations of wedge gate valves are otherwise similar to those "
      "of parallel gate valves.")

    # ------------------------------------------------------ wedge variations
    H("Các biến thể của nêm", "Variations of wedge design")
    P("Nêm cơ bản là nêm đặc hoặc nêm rỗng như các van Hình 3-34 đến Hình "
      "3-39. Kiểu này đơn giản và chắc chắn, nhưng biến dạng thân van do "
      "ứng suất nhiệt và ứng suất đường ống có thể làm nêm chỗ kín kim loại "
      "bị nhấc khỏi chỗ kín hoặc bị kẹt; hư hỏng dạng này thường gặp ở van "
      "chế tạo nhẹ.",
      "The basic type is the plain wedge of solid or hollow construction, as "
      "in Figures 3-34 to 3-39. It is simple and robust, but distortion of "
      "the valve body due to thermal and pipeline stresses may unseat or jam "
      "the metal-seated wedge — a failure more often experienced in valves "
      "of light-weight construction.")
    FIG(34, F4.fig_vsh_3_34())
    FIG(35, F4.fig_vsh_3_35())
    FIG(36, F4.fig_vsh_3_36())
    FIG(37, F4.fig_vsh_3_37())
    FIG(38, F4.fig_vsh_3_38())
    FIG(39, F4.fig_vsh_3_39())
    P("Độ tin cậy làm kín của van nêm cơ bản được cải thiện nhờ phần tử làm "
      "kín bằng ê-lô-me hoặc nhựa đặt ở chỗ kín hoặc trên nêm. Hình 3-40 cho "
      "thấy chỗ kín có đệm PTFE nhô cao hơn mặt kim loại một chút vừa đủ để "
      "tiếp xúc kín với nêm.",
      "Sealing reliability of plain-wedge valves can be improved by "
      "elastomeric or plastic sealing elements in either the seat or the "
      "wedge. Figure 3-40 shows a seat with a PTFE insert standing proud of "
      "the metal face just enough to ensure a seal against the wedge.")
    FIG(40, F4.fig_vsh_3_40())
    H("Nêm tự chỉnh", "Self-aligning wedges")
    P("Để khắc phục vấn đề chỉnh hướng của nêm cơ bản, người ta phát triển "
      "nêm tự chỉnh như Hình 3-41 đến Hình 3-43. Đơn giản nhất là nêm linh "
      "hoạt ở Hình 3-41 và 3-42, gồm hai nửa đĩa có gờ liền khối ở giữa; đủ "
      "mềm để tự tìm hướng. Vì cấu tạo đơn giản, không có chi tiết rời có "
      "thể lỏng ra khi vận hành, kiểu này trở thành thiết kế được ưa dùng.",
      "Efforts to overcome the alignment problem of plain wedges led to "
      "self-aligning wedges such as Figures 3-41 to 3-43. The simplest is the "
      "flexible wedge of Figures 3-41 and 3-42, composed of two discs with an "
      "integral boss in between; it is sufficiently flexible to find its own "
      "orientation. Being simple and containing no separate components that "
      "could rattle loose in service, this construction has become a favoured "
      "design.")
    FIG(41, F4.fig_vsh_3_41())
    FIG(42, F4.fig_vsh_3_42())
    P("Nêm tự chỉnh của van Hình 3-43 gồm hai tấm hình nêm giống hệt nhau "
      "đung đưa quanh một vòng đệm rời. Vòng này cũng dùng để chỉnh lại bộ "
      "nêm khi mòn. Để giữ hai tấm cùng nhau, thân van có rãnh dẫn bộ nêm "
      "trượt trong đó; khi rãnh dẫn mòn, có thể khôi phục dung sai ban đầu "
      "bằng cách chỉnh chiều dày vòng đệm.",
      "The self-aligning wedge of Figure 3-43 consists of two identical "
      "tapered plates rocking around a separate spacer ring. The ring may "
      "also be used to adjust the wedge assembly for wear. To keep the plates "
      "together the body has grooves in which the assembly travels; when "
      "wear takes place in the guides, the original guide tolerance can be "
      "restored by adjusting the spacer ring thickness.")
    FIG(43, F4.fig_vsh_3_43())
    H("Nêm bọc cao su", "Rubber-lined wedges")
    P("Bọc cao su cho nêm như Hình 3-44 và 3-45 dẫn đến khái niệm làm kín "
      "mới: một phần độ kín đạt được giữa mép nêm và thân van. Nhờ đó có thể "
      "bỏ hẳn khoang ở đáy thân van; các van này xử lý được chất lỏng mang "
      "chất rắn lơ lửng, vốn sẽ tích tụ trong khoang hở.",
      "Rubber lining of the wedge, as in Figures 3-44 and 3-45, led to new "
      "seating concepts in which the seat seal is achieved partly between "
      "the rim of the wedge and the valve body. In this way the creation of a "
      "pocket at the bottom of the body could be avoided altogether, so the "
      "valves handle fluids carrying solids in suspension which would "
      "otherwise collect in an open cavity.")
    P("Ở van Hình 3-44, nêm có hai vòng cao su hình yên cương bọc mép dưới "
      "hai bên và mặt hông phía trên. Lúc đóng, vòng cao su kín vào đáy và "
      "thành hông thân van, đồng thời nhờ tác dụng nêm mà kín vào mặt chỗ kín "
      "phía trên. Nêm của van Hình 3-45 được bọc cao su hoàn toàn và là một "
      "phần của màng ngăn cách cơ cấu thao tác với dòng chảy; khi đóng, đáy "
      "nêm kín vào đáy thân và chỗ kín thân. Van cũng có thể lót vật liệu "
      "chống ăn mòn nên được dùng rộng rãi trong công nghiệp hóa chất.",
      "In the valve of Figure 3-44 the wedge carries two stirrup-shaped "
      "rubber rings facing the wedge rim at the bottom sides and the upper "
      "lateral faces. When closing, the rings seal against the bottom and "
      "sidewalls of the body and, by a wedging action, against the seat faces "
      "at the top. The wedge of Figure 3-45 is completely rubber lined and "
      "forms part of a diaphragm separating the operating mechanism from the "
      "fluid; when closing, the wedge bottom seals against the body bottom "
      "and body seats. The valve may also be lined with corrosion-resistant "
      "materials and is therefore widely used in the chemical industry.")
    FIG(44, F4.fig_vsh_3_44())
    FIG(45, F4.fig_vsh_3_45())

    # --------------------------------------------------------- stem & guide
    H("Nối nêm với trục", "Connection of wedge to stem")
    P("Thường nối nêm với trục bằng rãnh chữ T ở đỉnh nêm nhận một cổ trên "
      "trục. Theo tiêu chuẩn API 600, mối nối này phải bền hơn tiết diện yếu "
      "nhất của trục để nêm không bị tuột khỏi trục trong khi thao tác.",
      "The wedge-to-stem connection usually consists of a T-slot in the top "
      "of the wedge receiving a collar on the stem. According to API 600, "
      "this connection must be stronger than the weakest stem section so "
      "that the wedge cannot become detached from the stem during operation.")
    P("Rãnh chữ T có thể đặt theo hướng dòng, như Hình 3-38, 3-39 và 3-41, "
      "hoặc ngang dòng, như Hình 3-36 và 3-42. Cách thứ hai cho phép thân van "
      "gọn hơn nên phổ biến vì lý do kinh tế, đồng thời hạ thấp điểm trục tác "
      "dộng lên nêm. Tuy nhiên rãnh phải đủ rộng để chứa độ chơi của nêm trong "
      "dẫn hướng, kể cả khi dẫn hướng đã mòn. Có ngoại lệ như Hình 3-34 và "
      "3-37, trục phải chịu toàn bộ lực đẩy của nêm nên chỉ phù hợp áp suất "
      "thấp. Ở Hình 3-43, gần như không có độ chơi dẫn hướng nên trục được "
      "giữ chặt trong nêm.",
      "The T-slot may lie in line with the flow passage, as in Figures 3-38, "
      "3-39 and 3-41, or across it, as in Figures 3-36 and 3-42. The latter "
      "allows a more compact body and has therefore become popular for "
      "economic reasons; it also lowers the point at which the stem acts on "
      "the wedge. The T-slot must nevertheless be wide enough to accommodate "
      "guide play, including guide wear. Exceptions such as Figures 3-34 and "
      "3-37 put the entire wedge thrust on the stem and so suit low-pressure "
      "applications only. In Figure 3-43 guide play is virtually absent, "
      "allowing the stem to be captured in the wedge.")
    H("Thiết kế dẫn hướng nêm", "Wedge guide design", h3)
    P("Dẫn hướng thân van thường là gờ lồng vào rãnh của nêm hoặc ngược lại, "
      "như minh họa ở Hình 3-42 và 3-43. Vì lý do kinh tế, gờ thân thường "
      "không được gia công; bề mặt thô của loại này không phù hợp để chịu nêm "
      "chạy dưới tải lớn. Do đó lúc mở van, nêm ban đầu vẫn nằm trên chỗ kín "
      "cho đến khi tải chất lỏng giảm đủ để gờ thân chịu lấy. Cách dẫn hướng "
      "này có thể cần độ chơi đáng kể, phải khớp với độ chơi của rãnh chữ T "
      "treo nêm trên trục.",
      "Body guides commonly consist of ribs fitting into slots of the wedge, "
      "or slots receiving ribs of the wedge, as illustrated in Figures 3-42 "
      "and 3-43. Body ribs are normally unmachined for reasons of cost; their "
      "rough finish is unsuited to carrying a travelling wedge under high "
      "load. On opening, the wedge is therefore initially carried on the seat "
      "until the fluid load is small enough for the ribs to carry it. This "
      "may require considerable guide play, matched by the play in the T-slot "
      "suspending the wedge on the stem.")
    P("Khi gờ thân bắt đầu chịu nêm, nêm phải được đỡ toàn chiều dài. Nếu "
      "chiều dài đỡ không đủ, lực chất lỏng tác động vào đoạn nêm không được "
      "đỡ có thể nghiêng nêm vào lỗ chỗ kín hạ lưu — yêu cầu đôi khi không "
      "được đáp ứng, dù có nhà chế tạo cố đảm bảo đỡ suốt hành trình. Không "
      "có gì đảm bảo nêm trượt trên cổ trục lúc mở: ma sát lớn tại mặt tiếp "
      "xúc giữa rãnh chữ T và cổ trục có thể làm nêm nghiêng trên trục; nếu "
      "lại lắp chặt và tải chất lỏng cao, các vuông tạo rãnh chữ T có thể bị "
      "nứt.",
      "Once the body ribs begin to carry the wedge, the wedge must be fully "
      "supported. If the length of support is insufficient, the fluid force "
      "on the unsupported section may tilt the wedge into the downstream "
      "seat bore — a requirement sometimes not complied with, although some "
      "makers go to great lengths to ensure full support. There is no "
      "assurance that the wedge slides on the stem collar when opening: "
      "considerable friction in the T-slot/collar contact may tilt the wedge "
      "on the stem, and a tight fit with high fluid load may crack the claws "
      "forming the T-slot.")
    P("Với ứng dụng quan trọng, dẫn hướng được gia công dung sai chặt và "
      "thiết kế đỡ nêm gần như suốt hành trình như Hình 3-42 và 3-43. Ở Hình "
      "3-42, rãnh nêm được phủ vật liệu cứng và dẫn chính xác trên gờ gia "
      "công hàn vào thân; nêm chỉ được chỗ kín đỡ trong 5% tổng hành trình. "
      "Ở Hình 3-43, hai tấm nêm mang lưỡi phủ cứng dẫn trong rãnh gia công "
      "của thân, và độ chơi được phục hồi bằng vòng đệm chỉnh.",
      "For critical applications, guides are machined to close tolerances "
      "and designed to carry the wedge over nearly the whole travel, as in "
      "Figures 3-42 and 3-43. In Figure 3-42 the wedge grooves are hard-faced "
      "and precision-guided on machined ribs welded to the body; the wedge is "
      "carried by the seat for only 5% of total travel. In Figure 3-43 the two "
      "wedge plates carry hard-faced tongues guided in machined body grooves, "
      "and guide tolerance is restored with the spacer ring.")

    # --------------------------------------------------- bypass / equalizing
    H("Đường tắt và nối cân bằng áp", "Bypass and pressure equalizing")
    P("Van cửa nêm có thể cần đường tắt với lý do đã nêu cho van cửa song song "
      "trang 77. Với nêm đôi tự chỉnh hai chỗ kín, sự giãn nhiệt của chất lỏng "
      "bị giam trong thân ép hai mặt kín lại gần nhau và làm áp suất khoang "
      "tăng. Tình huống tương tự xảy ra ở van chỗ kín mềm có nêm tạo được độ "
      "kín thượng lưu. Vì vậy nếu xử lý chất lỏng giãn nhiệt lớn, hoặc có thể "
      "bay hơi lại nước ngưng bị giam, các van này có thể cần nối cân bằng áp "
      "như đã mô tả cho van cửa song song.",
      "Wedge gate valves may need bypass connections for the reasons "
      "described for parallel gate valves on page 77. With a self-aligning "
      "double-seated wedge, thermal expansion of fluid locked in the body "
      "forces the upstream and downstream seatings into closer contact and "
      "raises cavity pressure. A similar situation may arise with soft-seated "
      "valves whose wedge can produce an upstream seat seal. Valves handling "
      "liquids of high thermal expansion, or where revaporation of trapped "
      "condensate can occur, may therefore need a pressure-equalizing "
      "connection as described for parallel gate valves.")

    # ------------------------------------------------------------ case study
    H("Nghiên cứu tình huống hư hỏng van cửa nêm",
      "Case study of wedge gate valve failure")
    P("Hình 3-46 đến 3-48 mô tả các bộ phận của van cửa nêm DN 300 (NPS 12) "
      "class 150 theo API 600 bị hỏng ngay lần sử dụng đầu tiên. Van lắp trên "
      "đường ống nằm ngang, nghiêng 45° so với phương thẳng đứng để thuận "
      "tiện thao tác bộ truyền bánh răng. Vị trí đó bắt nêm phải trượt trên "
      "gờ thân; rãnh dẫn trên nêm lại có cạnh sắc. Khi nêm trượt, cạnh sắc "
      "cọ vào bề mặt gờ thô, làm nêm xoay cho đến khi chạm gờ thân bên kia và "
      "bị kẹt. Lực đóng tiếp theo của nhân viên vận hành gây hư hỏng các bộ "
      "phận bên trong.",
      "Figures 3-46 to 3-48 show components of a DN 300 (NPS 12) class 150 "
      "wedge gate valve to API 600 that failed on first application. The "
      "valve was mounted in a horizontal line at 45° from the vertical for "
      "easy hand-operation of a gear drive. This position required the wedge "
      "to ride on a body rib, and the guide slot in the wedge had sharp "
      "edges. As the wedge travelled, those edges caught on the rough rib "
      "surface, causing the wedge to rotate until it contacted the opposite "
      "body rib and jammed. Further closing effort damaged the internals.")
    FIG(46, F4.fig_vsh_3_46())
    FIG(47, F4.fig_vsh_3_47())
    FIG(48, F4.fig_vsh_3_48())
    P("Kiểm tra còn thấy độ chơi ở dẫn hướng nêm lớn hơn hành trình trượt của "
      "nêm trên trục, nên trục phải nâng nêm ở một phần hành trình trong tư "
      "thế nghiêng; chiều dài gờ thân và rãnh dẫn lại quá ngắn để đỡ nêm suốt "
      "các giai đoạn chuyển động. Sự cố không phải cá biệt mà điển hình cho "
      "tỷ lệ cao van cửa nêm đã lắp đặt; cuối cùng toàn bộ van nghi ngờ đều "
      "phải thay thế trước khi đưa nhà máy vào vận hành.",
      "Further inspection showed that play in the wedge guides was larger "
      "than the possible travel of the wedge on the stem, so the stem had to "
      "carry the wedge tilted for part of its travel; the lengths of body rib "
      "and wedge guide were also far too short to support the wedge "
      "throughout its travel. This failure was not isolated but typical of a "
      "high percentage of installed wedge gate valves; all suspect valves "
      "had to be replaced before plant start-up.")
    P("Phụ lục C liệt kê các tiêu chuẩn Hoa Kỳ và Anh liên quan đến van cửa "
      "nêm.",
      "Appendix C provides a list of U.S. and British standards pertaining "
      "to wedge gate valves.")

    H("Ứng dụng", "Applications")
    P("Nhiệm vụ: dừng và khởi động dòng; thao tác không thường xuyên.",
      "Duty: stopping and starting flow; infrequent operation.")
    P("Dịch vụ: khí; chất lỏng; van cửa nêm chỗ kín cao su không khoang đáy "
      "dùng cho chất lỏng mang chất rắn lơ lửng; chân không; nhiệt độ rất "
      "thấp (cryogenic).",
      "Service: gases; liquids; rubber-seated wedge gate valves without "
      "bottom cavity for fluids carrying solids in suspension; vacuum; "
      "cryogenic.")

    H("Bảng tóm tắt các thiết kế nêm", "Wedge designs in this unit")
    b.append(table(
        ["Hình", "Thiết kế nêm", "Nắp / trục", "Đặc điểm chính"]
        if vi else
        ["Figure", "Wedge design", "Bonnet / stem", "Key feature"],
        [
            ["3-34", "Nêm rỗng / Hollow wedge", "Ren / vít trong · Screwed / internal",
             "Trục chịu lực đẩy, áp thấp / Direct thrust, low pressure"],
            ["3-35", "Nêm rỗng / Hollow wedge", "Bulông / vít trong · Bolted / internal",
             "Gờ dẫn thân / Body guide ribs"],
            ["3-36", "Nêm đặc / Solid wedge", "Khớp nối / vít trong · Union / internal",
             "Rãnh chữ T ngang dòng / T-slot across flow"],
            ["3-37", "Nêm đặc / Solid wedge", "Kẹp / vít trong · Clamped / internal",
             "Chỉ áp thấp / Low pressure only"],
            ["3-38", "Nêm đặc / Solid wedge", "Bulông / vít ngoài · Bolted / external",
             "Rãnh chữ T theo dòng / T-slot in line with flow"],
            ["3-39", "Nêm đặc / Solid wedge", "Hàn / ống sóng · Welded / bellows",
             "Hộp đón phụ / Auxiliary stuffing box"],
            ["3-40", "Đệm PTFE / PTFE insert", "—", "Nhô khỏi mặt kim loại / Proud of metal face"],
            ["3-41", "Nêm linh hoạt / Flexible wedge", "Kín áp / vít ngoài · Pressure-seal / external",
             "Tự chỉnh / Self-aligning"],
            ["3-42", "Nêm rèn linh hoạt / Forged flexible", "Kín áp / vít ngoài · Pressure-seal / external",
             "Rãnh phủ cứng trên gờ gia công / Hard-faced grooves, machined ribs"],
            ["3-43", "Nêm hai mảnh / Two-piece wedge", "Kín áp / vít ngoài · Pressure-seal / external",
             "Vòng đệm chỉnh mòn / Adjustable spacer ring"],
            ["3-44", "Nêm bọc cao su / Rubber-lined", "Bulông / vít ngoài · Bolted / external",
             "Vòng yên cương, không khoang đáy / Stirrup rings, no bottom cavity"],
            ["3-45", "Nêm bọc cao su + màng / Rubber wedge + diaphragm",
             "Màng / Diaphragm", "Công nghiệp hóa chất / Chemical industry"],
            ["3-46…3-48", "Hư hỏng do nêm xoay kẹt / Wedge rotated and jammed",
             "DN 300 class 150", "Rãnh dẫn, gờ thân, trục cong / Slots, ribs, bent stem"],
        ],
        caption=("Tóm tắt theo Hình 3-34…3-48 (văn bản nguồn, book pp. 85–96)."
                 if vi else
                 "Summary from Figures 3-34…3-48 (source text, book pp. 85–96)."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
