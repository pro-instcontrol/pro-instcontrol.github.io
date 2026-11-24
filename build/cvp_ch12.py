# -*- coding: utf-8 -*-
"""Book 7, Chapter 12 - How to Install a Control Valve (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
91-93 (PDF pp. 95-97). No figures, no tables and no references; one five-item
list of installation considerations, one twelve-item list of things that can
go wrong, a safety/service-life paragraph and three additional-reading items.
"""
from cvp_common import h2, h3, note, p, ul

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "How to Install a Control Valve"
TITLE_VI = "Lắp đặt van điều khiển thế nào"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 12.</b> lắp đặt van điều khiển (control valve "
                "installation) · bố trí đường ống (piping layout) · khả năng tiếp cận "
                "(accessibility) · van không mặt bích (flangeless valve) · thanh liên "
                "kết / ty ren (tie rods) · đoạn thu nhỏ (pipe reducer) · chỉ thị hành "
                "trình (travel indicator) · tay quay (hand wheel) · đường bypass · van "
                "chặn và van xả (block and drain valves) · xâm thực (cavitation) · hóa "
                "hơi (flashing) · bẫy hơi (steam trap) · tổng hơi (steam header) · cút "
                "và tee · đường kính ống (pipe diameter) · cút cong dài (long sweeping "
                "elbow) · tiếng ồn đường ống · van vệ sinh (sanitary valve) · chất lưu "
                "nguy hiểm · gioăng mặt bích (flange gasket) · packing thân van (valve "
                "stem packing) · nhiệt độ môi trường (ambient temperature) · gia nhiệt "
                "bằng băng (heat tracing) · chống cháy (fire-safe) · chống nổ "
                "(explosion-proof) · bản vẽ kích thước được xác nhận (certified "
                "dimensional drawing) · biển tên (nameplate) · siết trước (pretorque) · "
                "mũi tên chiều dòng chảy (flow arrow) · khe hở nút van (close-clearance "
                "plug) · mô-men / hệ số lưu lượng Cv · van bướm lót elastomer · mặt bích "
                "kiểu trượt (slip-on flange) · mặt bích nâng cao (raised-face flange) · "
                "lót PTFE · chảy nguội (cold flow) · van xả / van thoát nước (bleed or "
                "drain valve) · cổ kéo dài (extension bonnet) · van cryogenic · hộp "
                "packing bị đóng băng · vỏ che bảo vệ (protective metal shroud) · thân "
                "van dạng wafer · phớt bellows · màng làm kín thân van (stem sealing "
                "diaphragm) · thử áp lực thủy tĩnh (hydrostatic testing) · khí thiết bị "
                "đã tách ẩm (dehydrated instrument air) · quy chuẩn an toàn · đế van / "
                "bệ van / mặt tựa của van (seat).")
    return ("<b>Key terms.</b> control valve installation · piping layout · "
            "accessibility · flangeless valve · tie rods · pipe reducer · travel "
            "indicator · hand wheel · bypass · block and drain valves · cavitation · "
            "flashing · steam trap · steam header · elbow and tee · pipe diameter · "
            "long sweeping elbow · pipe noise · sanitary valve · dangerous fluid · "
            "flange gasket · valve stem packing · ambient temperature · heat tracing · "
            "fire-safe · explosion-proof · certified dimensional drawing · nameplate · "
            "pretorque · flow arrow · close-clearance plug · Cv · elastomer-lined "
            "butterfly valve · slip-on flange · raised-face flange · PTFE liner · cold "
            "flow · bleed or drain valve · extension bonnet · cryogenic valve · frozen "
            "packing box · protective metal shroud · wafer-style body · bellows seal · "
            "stem sealing diaphragm · hydrostatic testing · dehydrated instrument air · "
            "safety code · seat.")


def body_vi():
    b = []
    b.append(h2("Những điều cần cân nhắc khi lắp đặt",
                "Key installation considerations"))
    b.append(p("Việc chọn đúng van điều khiển không tự động đảm bảo van sẽ làm đúng "
               "công việc của nó. Lắp đặt đúng cách cũng quan trọng không kém. Tiếc là "
               "điều này lại phụ thuộc rất nhiều vào kinh nghiệm của người đã thiết kế "
               "bố trí đường ống. Có thể nên đặt người đó vài câu hỏi về kế hoạch lắp "
               "đặt van điều khiển. Dù sao thì, cách đó cũng cho thấy bạn quan tâm. Mặt "
               "khác, bạn có thể ngăn ngừa một sai lầm lớn mà về sau chính bạn sẽ bị "
               "đổ lỗi."))
    b.append(p("Dưới đây là một số — nhưng chắc chắn chưa phải tất cả — điều cần cân "
               "nhắc quan trọng khi lắp đặt van điều khiển."))
    b.append(ul([
        "<b>Khả năng tiếp cận (Accessibility) –</b> Có đủ không gian để tháo bộ truyền "
        "động khi cần sửa chữa không? Có tháo được bu lông mặt bích hoặc các thanh liên "
        "kết (tie rods) không? (Đây có thể là vấn đề, đặc biệt với van không mặt bích, "
        "khi thân van được kẹp giữa hai đoạn thu nhỏ đường ống.) Có nhìn thấy đồng hồ "
        "của bộ định vị hoặc chỉ thị hành trình van không? Có thể điều chỉnh bộ định vị "
        "không? Nếu có tay quay, nó có nằm ở vị trí cho phép quay không? Có thể xả áp "
        "hoặc thoát nước đoạn ống dẫn tới van không?",
        "<b>Cân nhắc vận hành bằng tay (Considerations for manual operation) –</b> Ở "
        "nhiều ứng dụng quan trọng, bạn nên cân nhắc một van tiết lưu vận hành bằng tay "
        "trên đường bypass quanh van; đường bypass cần có van chặn và van xả phù hợp ở "
        "hai bên van điều khiển, cho phép sửa chữa hoặc thay thế van mà không phải dừng "
        "quá trình (hãy xác định xem có thể vận hành nhà máy bằng tay hay không).",
        "<b>Vị trí lắp đặt (Location) –</b> Vị trí lắp van có cho phép sửa chữa không? "
        "Vị trí có được tối ưu để giúp ngăn ngừa xâm thực (cavitation), hay có để "
        "xâm thực xảy ra trong môi trường phía sau thường xuyên hóa hơi (flashing) vì "
        "đường ống ra quá dài? Nếu van nằm ở đáy tổng hơi, hãy đặt bẫy hơi gần đầu vào "
        "của van. Không đặt cút hoặc tee cách van bướm hoặc van bi chưa tới sáu đường "
        "kính ống ở phía sau, để tránh ảnh hưởng đến khả năng lưu lượng của van."
        "<p>Trong các ứng dụng giảm áp khí hoặc hơi có áp suất cao, hãy cố gắng chỉ dùng "
        "đoạn ống thẳng phía sau van, hoặc dùng cút cong dài, để tránh phát sinh thêm "
        "tiếng ồn đường ống. Hãy chừa khả năng thoát nước qua van. Điều này đặc biệt "
        "quan trọng với van vệ sinh và van xử lý chất lưu nguy hiểm.</p>"
        "<p>Hãy cân nhắc khả năng ăn mòn do gioăng mặt bích rò rỉ hoặc packing thân van "
        "gây ra cho thiết bị nằm bên dưới van. Van có ở gần nguồn nhiệt cực cao, hoặc "
        "ở nơi phụ kiện có thể bị đóng băng vào mùa đông không? Có thể bạn phải cân "
        "nhắc xếp hạng nhiệt độ môi trường của bộ truyền động hoặc bộ định vị, hoặc "
        "gia nhiệt bằng băng (heat trace) cho van hoặc đường ống khí. Van có cần đạt "
        "chuẩn chống cháy (fire-safe) không, hoặc phụ kiện điện có cần chống nổ "
        "(explosion-proof) vì nằm trong khu vực được coi là nguy hiểm không?</p>",
        "<b>Bản vẽ và phụ tùng (Drawings and parts) –</b> Tối thiểu, bạn nên có bản vẽ "
        "kích thước được xác nhận từ nhà cung cấp để đảm bảo van vừa khít với đường "
        "ống. Khi mua van “không mặt bích” (flangeless), hãy đảm bảo nhà cung cấp cấp "
        "kèm các thanh liên kết và đai ốc dùng để kết nối.",
        "<b>Hồ sơ (Records) –</b> Cuối cùng, hãy lưu giữ hồ sơ đầy đủ về những gì bạn "
        "đã mua, để sau này có thể thay thế hoặc sửa chữa van. Biển tên gốc có thể bị "
        "rách hoặc bị sơn phủ sau vài năm.",
    ]))

    b.append(h2("Những điều khác có thể đi sai",
                "Other things that can go wrong"))
    b.append(ul([
        "Người lắp đặt quên siết trước (pretorque) các thanh liên kết giữ van điều "
        "khiển không mặt bích, đặc biệt khi van điều khiển chất lưu lạnh.",
        "Người lắp đặt không để ý đến mũi tên chiều dòng chảy trên thân van.",
        "Không lắp bộ lọc phía trước van có nút van khe hở nhỏ (Cv < 0,1).",
        "Thân van bướm hoặc van bi bị lệch so với mặt bích đường ống. Điều này có "
        "thể làm giảm Cv tối đa của van tới 20%.",
        "Không có van chặn trên đường cấp khí nén tới bộ định vị. Cũng không có bộ "
        "điều áp hoặc bộ lọc khí.",
        "Van bướm lót elastomer được lắp giữa các mặt bích đường ống kiểu trượt "
        "(slip-on), khiến lớp lót bị hỏng vì không được giữ chặt do bề mặt gioăng "
        "của lớp lót quá hẹp.",
        "Van chống ăn mòn lót polytetrafluoroethylene (PTFE) được lắp giữa các mặt "
        "bích nâng cao (raised-face) có lớp lót nhựa, khiến bề mặt PTFE bị “chảy "
        "nguội” (cold flow) và gây rò rỉ giữa thân van và mặt bích đường ống.",
        "Không lắp van xả hoặc van thoát nước trên đường ống để giải áp cho đường "
        "ống khi van điều khiển ngừng hoạt động.",
        "Người lắp đặt lại cách nhiệt phần cổ kéo dài (extension bonnet) của van "
        "cryogenic, khiến hộp packing bị đóng băng.",
        "Không có vỏ che bằng kim loại bảo vệ quanh các thanh liên kết và thân van "
        "dạng wafer ở khu vực có nguy cơ cháy.",
        "Phớt bellows (hoặc màng làm kín thân van) không được tháo ra khỏi van trong "
        "lúc thử áp lực thủy tĩnh cho van và hệ thống đường ống, làm bellows (hoặc "
        "màng) bị vỡ.",
        "Bộ định vị của van đặt ngoài trời, chịu nhiệt độ đóng băng, lại được nối "
        "vào đường khí nén thông thường của xưởng thay vì nguồn khí thiết bị đã được "
        "tách ẩm (dehydrated instrument air).",
    ]))

    b.append(h2("An toàn trước, tiết kiệm sau",
                "Safety first, savings second"))
    b.append(p("Dĩ nhiên, mối quan tâm hàng đầu của bạn luôn phải là an toàn. Việc lắp "
               "đặt phải đáp ứng mọi yêu cầu của quy chuẩn an toàn và được rà soát để "
               "loại bỏ mọi nguy hiểm, kể cả khả năng gây ô nhiễm. Sau đó, hãy cân nhắc "
               "tiết kiệm cho công ty một khoản kha khá bằng cách đảm bảo van sẽ tồn "
               "tại ít nhất 20 năm mà không trở thành nguyên nhân gây dừng nhà máy "
               "hoặc dừng quá trình tốn kém."))

    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "API RP550, Sổ tay lắp đặt thiết bị và hệ thống điều khiển trong nhà máy lọc "
        "dầu (Manual on Installation of Refinery Instruments and Control Systems), ấn "
        "bản 2 (New York: American Petroleum Institute).",
        "Guy Borden Jr., biên tập, Control Valves (Research Triangle Park, NC: ISA "
        "[Instrument Society of America]), 1998: 543.",
        "T. C. Dickenson, Sổ tay về van, đường ống và pipelines (Handbook of Valves, "
        "Piping and Pipelines), ấn bản 2 (Amsterdam, Netherlands: Elsevier Science, "
        "1986).",
    ]))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR có một số dấu gạch nối "
                  "khi xuống dòng («planned con-trol valve»); bản dịch ghép lại thành "
                  "từ hoàn chỉnh. (2) Nguồn in «The original nameplate maybe torn off "
                  "or painted over» (dùng «maybe» thay vì «may be») và «when the "
                  "control was shut down» (thiếu «valve»); bản dịch hiểu theo ý định "
                  "là «may be» và «when the control valve was shut down». (3) Các cụm "
                  "có gạch nối trong bản in («corrosion-resistant», «elastomer-lined», "
                  "«explosion-proof», «fire-safe», «raised-face», «slip-on», "
                  "«wafer-style») được giữ nguyên. (4) Chương này không có hình, không "
                  "có bảng và không có tài liệu tham khảo trong thân bài; ba mục Đọc "
                  "thêm được giữ nguyên."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 12 chiếm các trang in 91–93 của ấn bản in (PDF tr. 95–97). "
               "Nguyên bản gồm một đoạn mở đầu, năm mục cần cân nhắc khi lắp đặt, "
               "danh sách mười hai sự cố thường gặp, một đoạn kết về an toàn và ba mục "
               "đọc thêm — tất cả đều được giữ lại. Các tiêu đề phụ trong bản dịch "
               "được biên tập thêm vì nguyên bản chỉ dùng các mục gạch đầu dòng."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Những điều cần cân nhắc khi lắp đặt",
                "Key installation considerations"))
    b.append(p("Having properly selected a given control valve does not automatically "
               "ensure that it will do the right job. Proper installation is almost as "
               "important. Unfortunately, this might depend greatly on the experience "
               "of the person who designed the piping layout. It might be a good idea "
               "to ask that person a few questions regarding the planned control valve "
               "installation. If nothing else, it shows him or her that you care. On "
               "the other hand, you might prevent a major mistake that you could be "
               "blamed for later."))
    b.append(p("Here are some, but by no means all, of the important considerations "
               "regarding control valve installations."))
    b.append(ul([
        "<b>Accessibility –</b> Is there sufficient space to remove the actuator when "
        "repair is necessary? Can the flange bolt or the tie rods be removed? (This "
        "can be a problem, especially with flangeless valves, if the body is installed "
        "between pipe reducers.) Can the positioner gauges or the valve travel "
        "indicator be seen? Can the positioner be adjusted? If a hand wheel is "
        "provided, is it in a position so that it can be rotated? Can the pipe leading "
        "to the valve be depressurized or drained?",
        "<b>Considerations for manual operation –</b> In many critical applications, "
        "you may want to consider a manually operated throttling valve in a bypass "
        "around the valve; the bypass would have appropriate block and drain valves on "
        "either side of the control valve that allow for the repair or replacement of "
        "the control valve without shutting down the process (ascertain if it is "
        "possible to run the plant manually).",
        "<b>Location –</b> Does the location of the valve permit repair? Is the "
        "location optimized to help prevent cavitation, or does the location permit "
        "cavitation to happen in a normally flashing downstream environment because "
        "the outlet pipe is too long? If the valve is on the bottom of a steam header, "
        "place a steam trap close to the valve inlet. Do not place an elbow or pipe tee "
        "less than six pipe diameters downstream of a butterfly or ball valve to avoid "
        "interference with the valve's flow capacity."
        "<p>In high-pressure gas or steam pressure-reducing applications, try to have "
        "only straight pipes downstream of the valve or use long sweeping elbows to "
        "avoid additional pipe noise. Allow for drainage through the valve. This is "
        "especially important for sanitary valves and for valves handling dangerous "
        "fluids.</p>"
        "<p>Consider the possibility of corrosion caused by leaky flange gaskets or "
        "valve stem packings on equipment located below the valve. Is the valve located "
        "near a source of extreme heat or where the accessories might freeze up in "
        "winter? You may have to consider the ambient temperature rating of the "
        "actuator or positioner, or heat trace the valve or air lines. Does the valve "
        "have to be fire-safe, or must the electrical accessories be explosion-proof "
        "because they are located in an area that is considered to be hazardous?</p>",
        "<b>Drawings and parts –</b> At a minimum, you should have certified "
        "dimensional drawings from your vendor to ensure the valve fits into the "
        "piping. When you purchase a “flangeless” valve, make sure the vendor supplies "
        "the connecting tie rods and nuts.",
        "<b>Records –</b> Finally, keep good records of what you purchased so you are "
        "able to replace or repair the valve. The original nameplate maybe torn off or "
        "painted over after a few years.",
    ]))

    b.append(h2("Những điều khác có thể đi sai",
                "Other things that can go wrong"))
    b.append(ul([
        "The installer forgot to pretorque the tie rods that hold a flangeless control "
        "valve, especially when it will control a cold fluid.",
        "The installer paid no attention to the flow arrow on the valve body.",
        "No filter was placed ahead of a valve that has a close clearance valve plug "
        "(Cv< 0.1).",
        "The valve body of a butterfly or ball valve was misaligned with the piping "
        "flanges. This can reduce the maximum valve Cv by up to 20%.",
        "No shutoff valve was provided in the pneumatic supply line to the positioner. "
        "Neither was a pressure regulator or air filter.",
        "An elastomer-lined butterfly valve was installed between slip-on type line "
        "flanges, causing the liner to fail because it is not properly retained due to "
        "the narrow width of the gasket surface in the liner.",
        "A polytetrafluorethylene (PTFE)-lined, corrosion-resistant valve was installed "
        "between plastic-lined, raised-face line flanges, causing the PTFE valve "
        "surface to “cold flow” and cause leakage between the body and pipe flanges.",
        "A bleed or drain valve was not installed in the pipe to relieve the pressure "
        "in the line when the control was shut down.",
        "The valve installer insulated the extension bonnet on a cryogenic valve, "
        "causing the packing box to freeze up.",
        "No protective metal shroud was placed around the tie rods and wafer-style "
        "valve body in an area where there is a potential fire hazard.",
        "The bellows seal (or stem sealing diaphragm) was not removed from a valve "
        "during hydrostatic testing of the valve and piping system causing the "
        "bellows (or diaphragm) to rupture.",
        "The positioner of a valve located outside and subject to freezing temperatures "
        "was connected to an ordinary shop airline instead of a dehydrated instrument "
        "air supply.",
    ]))

    b.append(h2("An toàn trước, tiết kiệm sau",
                "Safety first, savings second"))
    b.append(p("Of course, your primary concern should always be safety. The "
               "installation should meet all safety code requirements and be "
               "investigated to eliminate all hazards, including the possibility of "
               "causing pollution. Then, consider saving your company a bundle of money "
               "by ensuring that the valve will last for at least 20 years without "
               "being the cause of an expensive shutdown of the plant or process."))

    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "API RP550, Manual on Installation of Refinery Instruments and Control Systems, "
        "2nd ed. (New York: American Petroleum Institute).",
        "Guy Borden Jr., ed., Control Valves (Research Triangle Park, NC: ISA "
        "[Instrument Society of America]), 1998: 543.",
        "T. C. Dickenson, Handbook of Valves, Piping and Pipelines, 2nd ed. (Amsterdam, "
        "Netherlands: Elsevier Science, 1986).",
    ]))

    b.append(note("<b>Source notes.</b> (1) The OCR text layer contains a line-break "
                  "hyphenation («planned con-trol valve»); the translation rejoins it "
                  "into a whole word. (2) The source prints «The original nameplate "
                  "maybe torn off or painted over» (where «may be» is intended) and "
                  "«when the control was shut down» (where «control valve» is "
                  "intended); the translation follows the intended meaning. (3) "
                  "Compounds printed with hyphens («corrosion-resistant», "
                  "«elastomer-lined», «explosion-proof», «fire-safe», «raised-face», "
                  "«slip-on», «wafer-style») are retained. (4) The chapter has no "
                  "figures, no tables and no in-text references; the three Additional "
                  "Reading items are retained."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 12 occupies printed pp. 91-93 of the book (PDF pp. 95-97). "
               "The source consists of an opening passage, five installation "
               "considerations, a twelve-item list of things that can go wrong, a "
               "closing safety passage and three additional-reading items, all of "
               "which are retained. The editorial subheadings in the translation were "
               "added because the source uses only bulleted items."))
    return "".join(b)
