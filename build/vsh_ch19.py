# -*- coding: utf-8 -*-
"""Book 6, Unit 19 — Double Block and Bleed Ball Valves (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 309–313 (PDF pp. 323–328): DBB isolation philosophy, instrument DBB
valves, in-line DBB valves (Figures 9-1, 9-2).
"""

from vsh_common import fig, h2, h3, ol, p, table, ul
import vshfig16 as F16

PAGES_SRC = 5          # source book pp. 309-313
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Double Block and Bleed Ball Valves"
TITLE_VI = "Van bi chặn kép và xả (double block & bleed)"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 19.</b> double block and bleed (DBB) — "
                "chặn kép và xả · bleed valve — van xả · isolation — cách ly · "
                "trapped fluid — lưu chất bị kẹt giữa hai van · instrument "
                "DBB — DBB dùng cho thiết bị đo · in-line DBB — DBB đặt trong "
                "đường ống · quill — ống dẫn thẳng vào dòng chảy · chemical "
                "injection — phun hóa chất · sampling — lấy mẫu · poppet "
                "check valve — van một chiều poppet · trunnion mounted — bi "
                "gắn trục quay · pressure class — cấp áp suất.")
    return ("<b>Key terms.</b> double block and bleed (DBB) · bleed valve · "
            "isolation · trapped fluid · instrument DBB · in-line DBB · "
            "quill · chemical injection · sampling · poppet check valve · "
            "trunnion mounted · pressure class.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(items):
        b.append(ul([(i[0] if vi else i[1]) for i in items]))

    def O(items):
        b.append(ol([(i[0] if vi else i[1]) for i in items]))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ============================================================= introduction
    H("Giới thiệu van bi chặn kép và xả",
      "An introduction to double block and bleed ball valves")
    P("Hoạt động ngày càng mạnh ở khu vực ngoài khơi của ngành năng lượng đã "
      "khiến các yếu tố mới phải được tính tới khi thiết kế hệ thống đường "
      "ống. Không gian ở các vị trí ngoài khơi luôn khan hiếm nên hệ thống "
      "đường ống và các bộ phận đi kèm phải gọn hơn. Còn có những ràng buộc "
      "kết cấu rất quan trọng, ví dụ giữ kết cấu càng nhẹ càng tốt, và việc "
      "làm nhỏ gọn, nhẹ hơn các bộ phận rõ ràng mang lại lợi ích. Nhân công "
      "lắp dựng ngoài khơi cũng rất đắt, nên bất kỳ sự giảm bớt nhân lực lắp "
      "đặt nào cũng có lợi.",
      "The increased activity in the offshore sector of the energy industry "
      "has led to additional factors that have to be taken into "
      "consideration when designing piping systems. Space in these offshore "
      "locations is always at a premium and the design of piping systems and "
      "their associated components must therefore be more compact. There are "
      "structural constraints that are also very important, such as to keep "
      "the structure as light as possible, and there are obvious benefits "
      "from making components smaller and lighter. Construction labor in "
      "offshore locations is also very expensive and any reduction in "
      "installation manpower is also beneficial.")
    P("Tình hình trên đã dẫn tới việc cải tiến hình dạng các chi tiết van "
      "nhằm tiết kiệm không gian, trọng lượng và chi phí nhân công ở mức có "
      "thể, trong khi vẫn giữ nguyên chức năng ban đầu của van. Ban đầu các "
      "cải tiến này làm tăng giá thành, nhưng khi chi phí lắp đặt giảm xuống "
      "thì chi phí cuối cùng comparable với phương án dùng nhiều van rời như "
      "trước kia.",
      "The above situation has led to the modification of the patterns of "
      "valve components to incorporate savings in space, weight, and labor "
      "costs where possible, while still retaining the original function of "
      "the valve. Initially these modifications have meant that there is a "
      "cost impact, however when installation costs are reduced, the final "
      "costs are then comparable with the multi-component option used in the "
      "past.")

    # ============================================================= philosophy
    H("Triết lý cách ly chặn kép và xả",
      "Double block and bleed isolation philosophy")
    P("Triết lý cách ly quá trình ngày càng phức tạp khi các vấn đề an toàn "
      "phải được giải quyết và yêu cầu cách ly kiểu chặn kép và xả ngày càng "
      "phổ biến, đặc biệt ở ngoài khơi. Cách ly DBB cần hai van cách ly đặt "
      "trong đường ống và một van xả, dùng để xả hoặc thông hơi lưu chất bị "
      "kẹt giữa hai phần tử đóng. Van DBB là những bộ phận đặc biệt, tuy "
      "nhiên hiện nay đã có nhiều nhà sản xuất loại van này. Các van bi DBB "
      "đã được dùng rất thành công ở khu vực ngoài khơi của ngành năng lượng "
      "và nhiều lợi ích của chúng đã được hiện thực hóa, không chỉ cho các "
      "nhà máy xây mới mà còn cho các nhà máy đang hoạt động có lắp bổ sung.",
      "Process isolation philosophy has become more complex as safety issues "
      "have to be addressed and the requirement for double block and bleed "
      "isolation has become more commonly used, especially in offshore "
      "locations. Double block and bleed isolation requires two in-line "
      "isolation valves and a bleed valve, used to drain or vent trapped "
      "fluid between the two closure elements. Double block and bleed valves "
      "are special components, however there are now several manufacturers "
      "of this type of valve. These double block and bleed ball valves have "
      "been used very successfully in the offshore sector of the energy "
      "industry and their numerous benefits have been realized there not "
      "only for new builds, but also for existing plants where they have "
      "been retrofitted.")
    P("Khi quá trình đòi hỏi triết lý cách ly DBB, các van này được dùng cho "
      "hai chức năng:",
      "When a process calls for a double block and bleed isolation "
      "philosophy, these valves are used for two functions:")
    O([
        ("DBB dùng cho thiết bị đo (2 in trở xuống) — cho các kết nối áp "
         "suất, phun hóa chất, lấy mẫu, xả và thông hơi, v.v.",
         "Instrument double block and bleed (2 in and below) — for pressure "
         "connections, chemical injection, sampling, vents and drains, etc."),
        ("DBB đặt trong đường ống (2 in trở lên) — để cách ly quá trình.",
         "In-line double block and bleed (2 in and above) — for process "
         "isolation."),
    ])

    # ============================================================= instrument
    H("Van bi DBB dùng cho thiết bị đo",
      "Instrument double block and bleed ball valves")
    P("Những van DBB cỡ nhỏ gọn này (Hình 9-1a và 9-1b) thường được dùng để "
      "cách ly thiết bị đo như đồng hồ chỉ áp (PI) và ống đo mức (LG), và "
      "chúng có nhiều tổ hợp khác nhau. Kết nối đầu có thể là mặt bích hai "
      "đầu, hoặc một đầu mặt bích và đầu còn lại ren để gắn đồng hồ đo của "
      "thiết bị. Các kiểu kết nối khác như kiểu kẹp (clamp) cũng có nếu "
      "người mua yêu cầu.",
      "These small bore compact double block and bleed valves (Figures 9-1a "
      "and 9-1b) are generally used to isolate instrumentation such as "
      "pressure indicators (PIs) and level gauges (LGs) and they come in a "
      "variety of combinations. The end connections can be flanged both "
      "ends, or flanged one end and threaded the other end to receive the "
      "instrument gauge. Other end connections such as clamp type are "
      "available if specified by the purchaser.")
    P("Hai van cách ly thường thuộc loại bi quay một phần vòng, với đế "
      "mềm hoặc kim loại – kim loại tùy điều kiện thiết kế của lưu chất quá "
      "trình. Van xả nhỏ hơn, thường ¾ in hoặc ½ in, có thể kiểu cầu (globe), "
      "kim (needle), hoặc trong một số trường hợp kiểu bi. Thân có thể một "
      "mảnh hoặc chia đôi, và bi có thể loại nổi hoặc gắn trục quay "
      "(trunnion) ở các cấp áp cao.",
      "The two isolating valves are usually of a quarter-turn ball type, "
      "with either soft or metal-to-metal seats depending on the design "
      "conditions of the process fluid. The smaller, usually ¾ in or ½ in, "
      "bleed valve can be a globe, needle, or in some cases a ball type "
      "design. The body can be of a one piece or a split type and the ball "
      "can be either a floating type or a trunnion type design in the "
      "high-pressure classes.")
    FIG(1, F16.fig_vsh_9_1())
    P("Các van gọn này còn có thể dùng để phun hóa chất hoặc lấy mẫu lưu "
      "chất quá trình bằng cách gắn thêm ống thẳng (quill) vào lỗ của mặt "
      "bích. Khi lắp vào mặt bích ghép, ống quill đi vào dòng chảy quá "
      "trình; hóa chất được đưa qua van rồi qua ống, vốn nằm trong dòng "
      "chảy. Một van một chiều poppet đặt trong đường ống được bố trí thêm "
      "trong van gọn để ngăn dòng chảy ngược và ngăn lưu chất quá trình làm "
      "bẩn nguồn hóa chất. Khi lấy mẫu thì làm ngược lại: mẫu có thể được "
      "lấy từ lưu chất quá trình, qua ống quill, qua các van mở trong đường "
      "ống rồi thu vào chai lấy mẫu, sau đó mang đi phân tích.",
      "These compact valves can also be used for injecting chemicals or "
      "sampling process fluid by adding straight tubing onto the bore of "
      "the flange face. When assembled onto a mating flange this quill "
      "enters into the process flow and chemicals can be introduced through "
      "the valve and then the tube, which is in the process flow. An "
      "additional in-line poppet type check valve is incorporated in the "
      "compact valve to prevent reverse flow and process fluid contaminating "
      "the chemical source. For sampling the reverse is applied and samples "
      "can be removed from the process fluid, via the quill, through the "
      "open in-line valves and then collected in a sample bottle, which can "
      "be taken away for analysis.")
    FIG(3, F16.fig_vsh_9_3())

    # ============================================================= in-line
    H("Van bi DBB đặt trong đường ống",
      "In-line double block and bleed ball valves")
    P("Loại này (Hình 9-2a và 9-2b) cỡ lớn hơn, thường 2 in trở lên, và được "
      "đặt trong dòng quá trình chính. Các van gọn này có thể được cung cấp "
      "với nhiều kiểu kết nối đầu giống các phiên bản DBB dùng cho thiết bị "
      "đo nhỏ. Do kích thước, kết nối ren hầu như không bao giờ dùng, tuy "
      "nhiên kết nối đầu hàn đối tiếp (butt-weld) là một lựa chọn, cùng với kết "
      "nối kiểu kẹp.",
      "These (see Figures 9-2a and 9-2b) are larger in size, usually 2 in "
      "and above, and they are located in the primary process stream. These "
      "compact valves can be supplied in a similar number of end connections "
      "as the smaller instrument double block and bleed versions. Because of "
      "their size, a threaded connection will rarely if ever be used, "
      "however butt-weld end connections are an option that is available, "
      "along with clamp type end connections.")
    P("Van bi DBB trong đường ống có tới cỡ 8 in và cấp áp tới và bao gồm "
      "ASME 2500 lb. Khả năng cung cấp tùy vào các nhà sản xuất và năng lực "
      "của họ. Trong những trường hợp rất đặc biệt, một số công ty có thể "
      "làm khuôn riêng và chế tạo các van này ở cỡ lớn hơn.",
      "In-line double block and bleed ball valves are available up to "
      "around 8 in and pressure ratings up to and including ASME 2500 lb. "
      "Availability will depend on the manufacturers and their capabilities. "
      "In very special cases some companies are in a position to create "
      "special patterns and construct these valves in larger sizes.")
    FIG(2, F16.fig_vsh_9_2())
    P("Van bi DBB trong đường ống đắt; tuy nhiên, nếu tính cả chi phí các "
      "van rời, đường ống nối và gia công, thì hai mức chi phí này tương "
      "đương ở các cỡ tới 8 in. Van DBB là một bộ phận rất nặng và ở cỡ lớn "
      "nó sẽ cần tính toán nâng hộ nếu phải tháo ra để bảo trì.",
      "In-line double block and bleed ball valves are expensive; however, "
      "when you consider the cost of the individual valves, the "
      "interconnecting pipework, and the fabrication, the two costs are "
      "comparable in sizes up to 8 in. The double block and bleed valve is a "
      "very heavy component and in the larger sizes it will require lifting "
      "studies if the valve is to be removed for maintenance.")

    # ============================================================= summary
    H("Tóm tắt đơn vị 19", "Unit 19 summary")
    b.append(table(
        ["Hạng mục", "DBB thiết bị đo", "DBB trong đường ống"]
        if vi else ["Aspect", "Instrument DBB", "In-line DBB"],
        [
            ["Cỡ van" if vi else "Valve size",
             "2 in trở xuống" if vi else "2 in and below",
             "2 in trở lên, tới cỡ 8 in" if vi else
             "2 in and above, up to about 8 in"],
            ["Công dụng" if vi else "Purpose",
             "áp suất, phun hóa chất, lấy mẫu, xả/thông hơi" if vi else
             "pressure connections, injection, sampling, vents and drains",
             "cách ly quá trình chính" if vi else "primary process isolation"],
            ["Van cách ly" if vi else "Isolation valves",
             "bi quay 1/4 vòng, đế mềm hoặc kim loại" if vi else
             "quarter-turn balls, soft or metal seats",
             "bi trunnion, cấp áp cao" if vi else
             "trunnion balls, high-pressure classes"],
            ["Van xả" if vi else "Bleed valve",
             "¾ in hoặc ½ in; globe, kim hoặc bi" if vi else
             "¾ in or ½ in; globe, needle or ball",
             "theo thiết kế của nhà sản xuất" if vi else
             "per manufacturer design"],
            ["Kết nối đầu" if vi else "End connections",
             "mặt bích, ren, kiểu kẹp" if vi else
             "flanged, threaded, clamp",
             "mặt bích, hàn đối tiếp, kiểu kẹp" if vi else
             "flanged, butt-weld, clamp"],
            ["Cấp áp" if vi else "Pressure rating",
             "tùy điều kiện quá trình" if vi else "per process conditions",
             "tới ASME 2500 lb" if vi else "up to ASME 2500 lb"],
            ["Chi phí" if vi else "Cost",
             "gọn, nhẹ, ít nhân công lắp" if vi else
             "compact, light, less installation labor",
             "tương đương cụm van rời tới 8 in" if vi else
             "comparable to valve train up to 8 in"],
            ["Lưu ý" if vi else "Note",
             "có van một chiều poppet chống chảy ngược" if vi else
             "in-line poppet check prevents reverse flow",
             "cỡ lớn cần tính toán nâng khi bảo trì" if vi else
             "large sizes need lifting studies"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 309–313, "
                 "Hình 9-1, 9-2." if vi else
                 "Summary from source text, book pp. 309–313, "
                 "Figures 9-1, 9-2."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
