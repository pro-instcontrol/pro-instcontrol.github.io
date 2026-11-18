# -*- coding: utf-8 -*-
"""Book 6, Unit 11 — Manual Valves VII: Diaphragm and Stainless Steel Valves
(EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 144–151 (PDF pp. 158–165): weir and straight-through diaphragm valves,
construction materials, pressure/temperature and flow characteristics,
operational limits and applications; then stainless-steel corrosion-resistant
alloys, crevice corrosion, galling and light-weight construction
(Figures 3-93…3-99).
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig8 as F8

PAGES_SRC = 8          # source book pp. 144-151
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Manual Valves VII — Diaphragm and Stainless Steel Valves"
TITLE_VI = "Van tay VII — Van màng và van thép không gỉ"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 11.</b> diaphragm valve — van màng · "
                "flex-body valve — van thân mềm · diaphragm — màng · "
                "compressor — bản ép · weir — đập · straight-through — "
                "đường thẳng · rising stem — cần van nâng · lift indicator — "
                "ống chỉ báo nâng · double bonnet — nắp kép · T-branch — "
                "nhánh chữ T · ballooning — phồng màng · positive "
                "displacement — dịch chuyển thể tích · crevice corrosion — "
                "ăn mòn khe hở · galling — bó kẹt do ma sát · stellite — "
                "hợp kim cô-ban chống mài mòn · solution anneal — ủ dung dịch "
                "· self-aligning wedge — nêm tự chỉnh · light-weight valve — "
                "van nhẹ 150 lb.")
    return ("<b>Key terms.</b> diaphragm valve · flex-body valve · diaphragm · "
            "compressor · weir · straight-through · rising stem · lift "
            "indicator · double bonnet · T-branch · ballooning · positive "
            "displacement · crevice corrosion · galling · stellite · solution "
            "anneal · self-aligning wedge · light-weight valve.")


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

    # ======================================================= diaphragm valves
    H("Van màng", "Diaphragm valves")
    P("Van màng là van thân mềm trong đó thân van gồm một phần cứng và một "
      "phần mềm. Phần mềm là màng; màng cùng bản ép tạo thành cơ cấu đóng. "
      "Chỗ kín nằm ở phần thân cứng và có thể là một đập ngang qua đường "
      "dòng như Hình 3-93, hoặc là thành của đường dòng thẳng như Hình 3-94.",
      "Diaphragm valves are flex-body valves in which the valve body consists "
      "of a rigid and a flexible section. The flexible section is a diaphragm "
      "which, together with a compressor, forms the closure member. The seat "
      "is provided by the rigid body section: either a weir across the flow "
      "passage, as in Figure 3-93, or the wall of a straight-through passage, "
      "as in Figure 3-94.")
    P("Van màng có cùng lợi thế với van kẹp: đường dòng không bị cản bởi "
      "chi tiết chuyển động và không có khe hở. Vì vậy chúng dùng được cho "
      "những công việc tương tự, kể cả xử lý vệ sinh thực phẩm và dược phẩm.",
      "Diaphragm valves share the pinch valve's advantage: a flow passage not "
      "obstructed by moving parts and free of crevices. They may therefore be "
      "put to similar uses, including the sanitary handling of foodstuffs "
      "and pharmaceuticals.")
    FIG(93, F8.fig_vsh_3_93())
    FIG(94, F8.fig_vsh_3_94())

    H("Van màng kiểu đập", "Weir-type diaphragm valves")
    P("Đập được thiết kế để giảm uốn màng ở mức tối thiểu mà vẫn giữ đường "
      "dòng êm và suôn. Ứng suất uốn vì thế rất nhỏ, cho tuổi thọ màng tương "
      "ứng dài. Hành trình ngắn cũng cho phép dùng màng PTFE, vốn quá cứng "
      "đối với hành trình dài; mặt sau của các màng này được lót ê-lô-me để "
      "tạo ứng suất ép kín đồng đều khi đóng van.",
      "The weir is designed to reduce diaphragm flexing to a minimum while "
      "keeping a smooth, streamlined passage. Flexing stress is therefore "
      "minimal and diaphragm life correspondingly long. The short stroke "
      "also permits plastics such as PTFE, which would be too inflexible for "
      "longer strokes; the back of such diaphragms is lined with an "
      "elastomer to promote uniform seating stress on closing.")
    P("Van kiểu đập dùng được cho dịch vụ chân không nói chung và chân không "
      "cao, dù một số nhà chế tạo yêu cầu màng gia cố riêng ở chân không cao. "
      "Diện tích màng lớn so với tiết diện đường dòng nên áp suất chất lỏng "
      "tạo lực lớn trên màng nhấc lên; momen đóng sinh ra giới hạn kích "
      "cỡ chế tạo. Van kiểu Hình 3-93 thường tới DN 350 (NPS 14); cỡ lớn hơn "
      "tới DN 500 (NPS 20) dùng cụm nắp kép như Hình 3-95.",
      "Weir-type valves may be used in general and high vacuum service, "
      "although some makers require a specially reinforced diaphragm for "
      "high vacuum. Because the diaphragm area is large compared with the "
      "passage, fluid pressure imposes a high force on the raised diaphragm; "
      "the resulting closing torque limits valve size. Weir types like "
      "Figure 3-93 are typically made to DN 350 (NPS 14); larger valves up "
      "to DN 500 (NPS 20) use the double-bonnet assembly of Figure 3-95.")
    FIG(95, F8.fig_vsh_3_95())
    P("Có thể có thân dạng chữ T như Hình 3-96: một nhánh nối vào đường dòng "
      "chính mà không cản dòng. Chức năng chính là lấy mẫu, bảo đảm lấy được "
      "mẫu thật từ chất lỏng đang chảy.",
      "A T-configuration body is also available, as in Figure 3-96, in which "
      "a branch joins the main passage without impeding pipeline flow. Its "
      "main function is sampling duty, where a true sample of the flowing "
      "fluid must be assured.")
    FIG(96, F8.fig_vsh_3_96())
    P("Cần van kiểu Hình 3-93 là cần nâng. Tay quay mang bọc che ren cần "
      "khỏi bụi và ăn mòn từ bên ngoài, trượt trên ống chỉ báo màu vàng; ống "
      "này lại mang buồng mỡ đóng sẵn để bôi trơn ren cho tuổi thọ dài. Nếu "
      "cần, cần van có thêm O-ring làm kín với nắp van để chất lỏng không "
      "thoát ra môi trường khi màng bị hỏng trong lúc vận hành.",
      "The stem of the Figure 3-93 valve is of the rising type. A handwheel "
      "shroud protects the external stem thread from dust and outside "
      "corrosion, sliding over a yellow lift-indicator sleeve which carries "
      "a prepacked lubrication chamber for long thread life. If required, "
      "an O-ring seal between stem and bonnet prevents fluid escaping to "
      "the surroundings should the diaphragm fail in service.")
    P("Van kiểu đập thông thường cũng dùng được trên đường ống nằm ngang "
      "cần tự thoát nước. Tự thoát đạt được khi lắp van với cần nghiêng khoảng "
      "15° đến 25° lên từ phương ngang, miễn là chính đường ống có độ dốc.",
      "Conventional weir-type valves may also be used on horizontal lines "
      "that must be self-draining. This is achieved by mounting the valve "
      "with the stem about 15° to 25° up from the horizontal, provided the "
      "line itself has some fall.")

    H("Van màng kiểu đường thẳng", "Straight-through diaphragm valves")
    P("Đường dòng thẳng đòi hỏi màng dẻo hơn kiểu đập, nên vật liệu màng bị "
      "giới hạn ở ê-lô-me. Vì màng rất dẻo và có diện tích lớn, chân không "
      "cao có xu hướng phồng màng vào đường dòng. Mức phồng khác nhau theo "
      "hãng chế tạo: hoặc chỉ giảm nhẹ tiết diện và chấp nhận được, hoặc màng "
      "bị sụp. Trường hợp sau phải hút chân không buồng nắp để cân bằng áp "
      "suất hai phía màng; cần hỏi nhà chế tạo khi dùng cho chân không cao.",
      "A straight-through passage requires a more flexible diaphragm than a "
      "weir type, so diaphragm material is restricted to elastomers. Their "
      "high flexibility and large area mean that high vacuum tends to "
      "balloon the diaphragm into the passage. The degree of ballooning "
      "varies by make, causing either a small acceptable loss of flow area "
      "or collapse of the diaphragm; in the latter case the bonnet must be "
      "evacuated to balance pressures. Consult the manufacturer for high "
      "vacuum service.")
    P("Van kiểu đường thẳng có cả dạng đường kính đầy và đường kính thu nhỏ. "
      "Với van thu nhỏ, dùng cụm nắp của cỡ nhỏ hơn kế tiếp: ví dụ van DN 50 "
      "(NPS 2) thu nhỏ lắp nắp DN 40 (NPS 1½); cấu trúc nắp khác nếu không "
      "giống kiểu đập. Dải cỡ thường tới DN 350 (NPS 14).",
      "Straight-through valves come with full-bore and reduced-bore passages. "
      "A reduced-bore valve uses the bonnet assembly of the next smaller "
      "size: for example a DN 50 (NPS 2) reduced-bore valve is fitted with a "
      "DN 40 (NPS 1½) bonnet. The bonnet is otherwise similar to that of "
      "weir-type valves. The size range typically reaches DN 350 (NPS 14).")

    H("Vật liệu chế tạo", "Construction materials")
    P("Thân van màng có nhiều vật liệu, kể cả nhựa, để đáp ứng yêu cầu dịch "
      "vụ. Dạng thân đơn giản cũng dễ lót bằng nhiều vật liệu chống ăn mòn, "
      "thường cho giải pháp chi phí thấp cho một van vốn đắt đỏ. Vì màng "
      "ngăn cách buồng nắp với chất lỏng, nắp thường bằng gang đúc phủ ê-pô-xi "
      "cả trong lẫn ngoài; có thể yêu cầu vật liệu khác.",
      "Diaphragm valve bodies are available in a great variety of materials, "
      "including plastics, to meet service requirements. The simple body "
      "shape also lends itself readily to lining with many corrosion-"
      "resistant materials, often giving a low-cost solution for an "
      "otherwise expensive valve. Because the diaphragm separates the bonnet "
      "from the flowing fluid, the bonnet is normally cast iron epoxy-coated "
      "inside and out; other materials are available on request.")
    P("Màng có nhiều ê-lô-me và nhựa. Catalog của nhà chế tạo hướng dẫn chọn "
      "vật liệu màng cho từng ứng dụng.",
      "Diaphragms are available in a great variety of elastomers and "
      "plastics. Makers' catalogs advise on diaphragm material selection "
      "for a given application.")

    H("Quan hệ áp suất và nhiệt độ", "Valve pressure/temperature relationships")
    P("Hình 3-97 và Hình 3-98 cho thấy quan hệ áp suất/nhiệt độ điển hình "
      "của van màng kiểu đập và kiểu đường thẳng. Ở đây chỉ trình bày sơ đồ "
      "biên tập, không có thang số: không phải vật liệu nào cũng cho phép "
      "toàn bộ dải đó. Người dùng phải xem catalog nhà chế tạo để biết áp "
      "suất làm việc cho phép ở nhiệt độ đã định.",
      "Figures 3-97 and 3-98 show typical pressure/temperature relationships "
      "of weir-type and straight-through diaphragm valves. They are shown "
      "here as editorial schematics without a numeric scale: not all "
      "construction materials permit the full range. The user must consult "
      "the manufacturer's catalog for the permissible operating pressure at "
      "a given temperature.")
    FIG(97, F8.fig_vsh_3_97())
    FIG(98, F8.fig_vsh_3_98())

    H("Đặc tính dòng", "Valve flow characteristics")
    P("Hình 3-99 cho thấy đặc tính dòng vốn có và sau lắp đặt điển hình của "
      "van màng kiểu đập, dạng đường có thể thay đổi đôi chút theo cỡ van. "
      "Khi điều khiển tự động, có thể biến đổi đặc tính bằng bộ định vị cam "
      "thay đổi được.",
      "Figure 3-99 shows typical inherent and installed flow characteristics "
      "of weir-type diaphragm valves, although curve shapes vary somewhat "
      "between valve sizes. In automatic control these characteristics may "
      "be modified with a variable cam positioner.")
    FIG(99, F8.fig_vsh_3_99())

    H("Giới hạn vận hành và tiêu chuẩn", "Operational limitations and standards")
    P("Như van kẹp, van màng dịch chuyển một lượng chất lỏng nhất định khi "
      "thao tác — chúng là van thể tích dương. Vì vậy không được lắp van màng "
      "làm van chặn trên đường ống chứa chất lỏng không nén được mà không có "
      "chỗ cho chất lỏng dịch chuyển.",
      "Like pinch valves, diaphragm valves displace a certain amount of "
      "fluid when operated; they are positive-displacement valves. They "
      "must therefore not be installed as shut-off valves in lines carrying "
      "an incompressible fluid where the fluid has no room to move.")
    P("Phụ lục C liệt kê các tiêu chuẩn Hoa Kỳ, Anh và ISO áp dụng cho van màng.",
      "Appendix C lists U.S., British and ISO standards pertaining to "
      "diaphragm valves.")

    H("Ứng dụng", "Applications")
    P("Nhiệm vụ của cả hai kiểu đập và đường thẳng: dừng và khởi động dòng; "
      "khống chế lưu lượng.",
      "Duty for both weir and straight-through types: stopping and starting "
      "flow; controlling flow.")
    U([("Kiểu đập: khí và chất lỏng có thể lẫn rắn, chất lỏng nhớt, xử lý "
        "kín không rò chất nguy hiểm, xử lý vệ sinh dược phẩm và thực phẩm, "
        "chân không.",
        "Weir type: gases and liquids that may carry solids, viscous fluids, "
        "leak-proof handling of hazardous fluids, sanitary handling of "
        "pharmaceuticals and foodstuffs, vacuum."),
       ("Kiểu đường thẳng: khí và chất lỏng có thể lẫn rắn, chất lỏng nhớt, "
        "bùn, hỗn dịch có thể chứa chất mài mòn, môi trường khô, chân không "
        "(hỏi nhà chế tạo).",
        "Straight-through: gases and liquids that may carry solids, viscous "
        "fluids, sludges, slurries that may carry abrasives, dry media, "
        "vacuum (consult manufacturer).")])

    # ==================================================== stainless steel
    H("Van thép không gỉ", "Stainless steel valves")
    H("Hợp kim chống ăn mòn", "Corrosion-resistant alloys", h3)
    P("Hợp kim chống ăn mòn thấp nhất thường được coi là thép AISI 304 "
      "(18 Cr, 10 Ni). Thép AISI 316 (18 Cr, 12 Ni, 2,5 Mo) có dải chống ăn "
      "mòn rộng hơn, và nhà chế tạo thường chuẩn hóa ở 316 như hợp kim thấp "
      "nhất được chấp nhận. Nếu van được hàn vào đường ống, loại các-bon "
      "thấp (dưới 0,3% C) tốt hơn loại ổn định. Van bích chỉ cần hàn khi sửa "
      "khuyết điểm vật đúc; vì việc sửa thực hiện trước khi ủ dung dịch nước "
      "ở 1100 °C (2000 °F), loại các-bon tiêu chuẩn vẫn hoàn toàn phù hợp "
      "cho van bích.",
      "The least corrosion-resistant alloy is normally steel AISI type 304 "
      "(18 Cr, 10 Ni). AISI type 316 (18 Cr, 12 Ni, 2.5 Mo) resists a wider "
      "range, and makers often standardize on 316 as the least resistant "
      "alloy. Where a valve is welded into the pipeline, low-carbon grades "
      "(under 0.3% carbon) are better than stabilized grades. Flanged valves "
      "need welding only to repair a casting defect; because the repair is "
      "made before the 1100 °C (2000 °F) water-quench solution anneal, "
      "standard carbon grades are satisfactory for flanged valves.")
    H("Ăn mòn khe hở", "Crevice corrosion", h3)
    P("Hầu hết hợp kim chống ăn mòn đều nhạy với ăn mòn khe hở. Thiết kế tốt "
      "vì thế tránh ren ở bất kỳ chi tiết nào tiếp xúc với chất lỏng ăn mòn; "
      "chỗ kín thường làm một khối với thân van. Ngoại lệ là thiết kế kẹp "
      "chỗ kín giữa hai nửa thân như Hình 3-12, nhưng gioăng giữa chỗ kín và "
      "thân phải cắt gọn để không tạo khe hở.",
      "Practically all corrosion-resistant alloys are susceptible to "
      "crevice corrosion. Good designs therefore avoid threading any "
      "component that touches the corrosive fluid; seats are normally an "
      "integral part of the body. An exception is a seat clamped between two "
      "body halves as in Figure 3-12, but the gaskets must be cleanly cut "
      "to avoid crevices.")
    P("Nếu van được vặn vào đường ống, hàn kín mối ren sẽ cải thiện hiệu "
      "năng; có thể dùng chất trám ren hóa cứng sau khi bôi để chống ăn mòn "
      "khe hở. Nên tránh mặt bích có khe hở như kiểu lưỡi và rãnh. Điểm xốp "
      "trong thân tiếp xúc chất ăn mòn cũng gây ăn mòn khe hở: thân có thể "
      "thủng tại điểm đó và rò rỉ lớn trong khi phần còn lại vẫn tốt.",
      "For screwed-in valves, seal welding improves the joint; thread "
      "sealants that harden after application also help. Flanged facings "
      "with crevices, such as tongue and groove, should be avoided. Porosity "
      "exposed to the corrosive fluid can likewise cause crevice corrosion: "
      "the body may corrode through at that point and leak grossly while "
      "the rest remains sound.")
    H("Bó kẹt do ma sát", "Galling of valve parts", h3)
    P("Thép không gỉ khi tiếp xúc trượt — nhất là loại ô-sten-it có thành "
      "phần giống nhau — dễ bị bó kẹt. Xu hướng này giảm nhiều nếu chất lỏng "
      "có độ bôi trơn tốt và bề mặt tiếp xúc giữ được chất bôi trơn lẫn tạp "
      "chất bảo vệ. Bề mặt đánh bóng giữ rất ít nên dễ bó kẹt hơn; vì vậy mặt "
      "chỗ kín của van thép không gỉ thường được gia công cực mịn thay vì "
      "đánh bóng.",
      "Stainless steel in sliding contact, particularly austenitic grades "
      "of like composition, is susceptible to galling. The tendency falls "
      "considerably when the fluid has good lubricity and the seating "
      "surfaces retain lubricants and protective contaminants. Polished "
      "surfaces retain little and therefore gall more readily, so seating "
      "faces of stainless steel valves are usually very finely machined "
      "rather than polished.")
    P("Khi dự kiến bó kẹt mạnh, chẳng hạn với khí khô, có thể phủ một mặt "
      "chỗ kín bằng stellite, hợp kim chống ăn mòn và mài mòn tốt. Tránh kẹt "
      "cần van trong bạc yoke bằng cách chọn vật liệu khác nhau: bạc bằng "
      "gang dẻo Ni-Resist D2 có than chì nên hoàn toàn không bó kẹt; nếu bạc "
      "cũng bằng thép không gỉ, loại dễ gia công 303 kết hợp với cần 304 "
      "hoặc 316 cho khả năng chống bó kẹt rất tốt.",
      "When high galling is expected, as with dry gases, one seating face "
      "may be faced with stellite, which resists many corrosives well. "
      "Seizing of the stem in the yoke bush is commonly avoided by choosing "
      "dissimilar materials: Ni-Resist ductile iron D2 bushings give freedom "
      "from galling thanks to their graphite; if the bush is stainless, "
      "free-machining type 303 with a type 304 or 316 stem gives remarkable "
      "freedom from galling.")
    H("Kết cấu nhẹ", "Light-weight valve constructions", h3)
    P("Nỗ lực giảm chi phí van thép không gỉ tại Hoa Kỳ dẫn đến tiêu chuẩn "
      "van thép không gỉ nhẹ 150 lb. Mức áp suất trong tiêu chuẩn đó chỉ áp "
      "dụng cho van làm bằng vật liệu ô-sten-it. Bích mỏng hơn bích thép "
      "các-bon cùng cấp và có mặt phẳng trơn; nhiều người dùng không thích "
      "bích mỏng nên yêu cầu bích đầy cấp có mặt nổi. Thân nhẹ cũng mềm hơn, "
      "đặc biệt quan trọng với van cổng vì chuyển động thân có thể làm đĩa "
      "rời chỗ kín: nêm đặc chỉ dùng tới DN 100 (NPS 4), cỡ lớn hơn phải dùng "
      "nêm tự chỉnh.",
      "U.S. efforts to cut stainless valve cost led to standards for 150 lb "
      "light-weight stainless steel valves. Their pressure ratings apply "
      "only to valves made from austenitic materials. The flanges are "
      "thinner than full-rating carbon steel flanges and have plain flat "
      "faces; many users object and request full-rating flanges with a "
      "raised face. Light bodies are more flexible, especially important "
      "for gate valves where body movement can unseat the disc: plain solid "
      "wedges are used only to DN 100 (NPS 4), and larger valves need "
      "self-aligning wedges.")
    P("Phụ lục C liệt kê tiêu chuẩn áp dụng cho van thép không gỉ.",
      "Appendix C lists the standards pertaining to stainless steel valves.")

    # -------------------------------------------------------------- table
    H("Bảng tóm tắt các thiết kế trong đơn vị", "Designs in this unit")
    b.append(table(
        ["Hình / chủ đề", "Thiết kế", "Đặc điểm chính"]
        if vi else ["Figure / topic", "Design", "Key feature"],
        [
            ["3-93", "Van màng kiểu đập / Weir-type diaphragm valve",
             "Đập giảm uốn màng, tuổi thọ cao / Weir minimizes flexing"],
            ["3-94", "Van màng đường thẳng / Straight-through diaphragm",
             "Màng dẻo hơn, chỉ ê-lô-me / More flexing, elastomers only"],
            ["3-95", "Nắp kép / Double-bonnet assembly",
             "Cho cỡ tới DN 500 / Allows sizes up to DN 500"],
            ["3-96", "Thân chữ T / T-branch body",
             "Lấy mẫu thật, không cản dòng / True sampling, no obstruction"],
            ["3-97", "Áp suất/nhiệt độ kiểu đập / Weir P–T envelope",
             "Tùy vật liệu màng / Depends on diaphragm material"],
            ["3-98", "Áp suất/nhiệt độ đường thẳng / Straight-through P–T",
             "Dải hẹp hơn / Narrower envelope"],
            ["3-99", "Đặc tính dòng / Inherent vs installed flow",
             "Cam biến đổi được / Variable cam positioner"],
            ["Vật liệu / Materials", "Thân, nắp, màng / Body, bonnet, diaphragm",
             "Nhiều nhựa và ê-lô-me / Plastics and elastomers"],
            ["Giới hạn / Limit", "Van dịch chuyển thể tích / Positive displacement",
             "Không chặn chất lỏng không nén kín / No locked-in liquid"],
            ["304 / 316", "AISI 304 (18Cr, 10Ni), AISI 316 (18Cr, 12Ni, 2.5Mo)",
             "316 phổ biến hơn / 316 usually the minimum"],
            ["Khe hở / Crevice", "Ren, gioăng, điểm xốp / Threads, gaskets, porosity",
             "Tránh khe hở / Avoid crevices"],
            ["Bó kẹt / Galling", "Mặt kín, bạc cần / Seats, yoke bush",
             "Gia công mịn, stellite, Ni-Resist D2 / Fine machine, stellite"],
            ["Van nhẹ / Light-weight", "150 lb, bích phẳng / 150 lb, flat flanges",
             "Nêm tự chỉnh bên trên DN 100 / Self-aligning above DN 100"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 144–151, "
                 "Hình 3-93…3-99." if vi else
                 "Summary from source text, book pp. 144–151, "
                 "Figures 3-93…3-99."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
