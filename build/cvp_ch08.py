# -*- coding: utf-8 -*-
"""Book 7, Chapter 8 - What About Fail-Safe? (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
55-56 (PDF pp. 61-62). No figures, no tables, and no references; one numbered
footnote and one four-item ordered list of consequences in increasing severity.
"""
from cvp_common import h2, h3, note, ol, p

PAGES_SRC = 2
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "What About Fail-Safe?"
TITLE_VI = "Về an toàn khi mất điện (fail-safe)?"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 8.</b> an toàn khi hỏng / an toàn khi mất điện "
                "(fail-safe) · bộ truyền động màng–lò xo (spring-diaphragm actuator) · "
                "lò xo được nén sẵn (precompressed spring) · mất khí nén (air failure) · "
                "đứt dây tín hiệu · bộ điều khiển trục trặc · bộ truyền động xi lanh "
                "(cylinder actuator) · áp suất khí tích trữ · van khóa tác động bằng áp "
                "suất (pressure-actuated lockup valve) · đế van / bệ van / mặt tựa của "
                "van (seat) · van cầu một đế (single-seated globe valve) · nút van (valve "
                "plug) · trục van (valve stem) · nguồn điện dự phòng (standby power) · "
                "bộ ắc quy (battery pack) · fail-close (đóng an toàn) / fail-open (mở an "
                "toàn) · chất lưu dễ cháy · đầu đốt (burner) · bộ trao đổi nhiệt · phản "
                "ứng tỏa nhiệt (exothermic reaction) · gia nhiệt bằng hơi (steam tracing) "
                "· đường ống dầu thô · độ nhớt (viscosity) · ổ bi động cơ (motor bearing) "
                "· máy nén khí · sét đánh (lightning strike) · van giảm áp "
                "(pressure-reducing valve) · van an toàn (relief / safety valve) · chất "
                "lưu bị giam giữ · giãn nở nhiệt (thermal expansion) · fail-in-place (giữ "
                "nguyên vị trí khi hỏng) · bộ truyền động điện kiểu bánh răng · van điện "
                "từ hai chiều (two-way solenoid valve) · dòng chảy hướng mở / hướng đóng "
                "(flow-to-open / flow-to-close) · bộ định vị van (valve positioner) · "
                "xâm thực (cavitation) · hóa hơi (flashing).")
    return ("<b>Key terms.</b> fail-safe · spring-diaphragm actuator · precompressed "
            "spring · air failure · signal-wire breakage · controller malfunction · "
            "cylinder actuator · stored air pressure · pressure-actuated lockup valve · "
            "seat · single-seated globe valve · valve plug · valve stem · standby power · "
            "battery pack · fail-close / fail-open · flammable fluid · burner · heat "
            "exchanger · exothermic reaction · steam tracing · crude oil pipe · viscosity "
            "· motor bearing · air compressor · lightning strike · pressure-reducing "
            "valve · relief / safety valve · trapped liquid · thermal expansion · "
            "fail-in-place · electric gear-type actuator · two-way solenoid valve · "
            "flow-to-open / flow-to-close · valve positioner · cavitation · flashing.")


def body_vi():
    b = []
    b.append(h2("Van màng–lò xo và khả năng an toàn khi hỏng",
                "Spring-diaphragm valves and fail-safe action"))
    b.append(p("Một trong những lợi ích quan trọng của van điều khiển kiểu màng–lò xo là "
               "khả năng an toàn khi hỏng (fail-safe) nhờ tác dụng của lò xo bộ truyền "
               "động được nén sẵn — tức là van sẽ đóng hoặc mở khi mất khí nén, hoặc, "
               "thường gặp hơn, khi dây tín hiệu bị đứt hoặc bộ điều khiển trục trặc."))

    b.append(h2("Bộ truyền động xi lanh và bộ truyền động điện",
                "Cylinder and electric actuators"))
    b.append(p("Van điều khiển dùng bộ truyền động xi lanh không tự an toàn khi hỏng nếu "
               "không bổ sung lò xo hoặc áp suất khí được tích trữ trong một xi lanh "
               "riêng, được giữ lại đó bởi một van khóa (lockup valve) tác động bằng áp "
               "suất. Đôi khi, chiều dòng chảy của van cầu một đế (single-seated globe "
               "valve) được đảo ngược để chính lực của chất lưu giúp đóng nút van (nếu "
               "mong muốn fail-close)."))
    b.append(p("Thông thường, bộ truyền động điện không có tác dụng an toàn khi hỏng trừ "
               "khi có một nguồn điện dự phòng, chẳng hạn như bộ ắc quy được kích hoạt "
               "bằng công tắc rơ le. Ở đây, đương nhiên, việc bảo trì định kỳ và sạc lại "
               "ắc quy là điều bắt buộc."))

    b.append(h2("Hướng an toàn: đóng hay mở khi hỏng?",
                "Fail-safe direction: close or open?"))
    b.append(p("Hướng an toàn khi hỏng (mở hay đóng) thường do các yêu cầu an toàn quyết "
               "định. Thông thường,<sup>1</sup> người ta quy định fail-close nếu chất lưu "
               "cần xử lý dễ cháy (ví dụ khí tự nhiên đi tới đầu đốt) hoặc là môi chất gia "
               "nhiệt đi tới bộ trao đổi nhiệt, nơi việc cấp quá nhiều nhiệt cho một bình "
               "chứa có thể gây sôi hoặc gây phản ứng tỏa nhiệt của một hóa chất. Hầu hết "
               "các van xử lý hóa chất đều được quy định là van fail-close."))
    b.append(note("<b>Chú thích 1.</b> Trong 75% đến 80% số ứng dụng."))
    b.append(p("Tuy nhiên, trong một số ứng dụng gia nhiệt, tác dụng fail-open lại có lợi "
               "hơn. Hãy xét ví dụ gia nhiệt bằng hơi (steam tracing) cho một đường ống "
               "dầu thô. Ở đây, độ nhớt quá thấp (do quá nhiều nhiệt) có lẽ vẫn tốt hơn là "
               "để chất lưu gần như đứng yên, đặc biệt là vào giữa mùa đông. Một ứng dụng "
               "fail-open khác là điều khiển chất lưu làm mát tới ổ bi của động cơ, nơi "
               "tác hại xấu nhất có thể chỉ là giảm hiệu suất."))

    b.append(h2("Tự kiểm tra: nếu van đột ngột mở hoặc đóng?",
                "Self-check: if the valve suddenly opens or closes?"))
    b.append(p("Hãy tự hỏi: điều gì sẽ xảy ra nếu van này đột ngột mở (hoặc đóng) khi máy "
               "nén khí hỏng hoặc khi mất tín hiệu (máy tính sự cố, dây bị đứt, sét đánh)? "
               "Khi còn nghi ngờ, hãy hỏi ý kiến của những người phụ trách công nghệ. Một "
               "câu hỏi khác cần ghi nhớ là van an toàn hạ lưu có đủ khả năng lưu lượng để "
               "xử lý dòng chảy từ một van giảm áp khi van này hỏng ở trạng thái mở hoàn "
               "toàn hay không. Cùng chung suy nghĩ đó, hãy xem xét ảnh hưởng của giãn nở "
               "nhiệt đối với một chất lưu bị giam giữ khi van cấp môi chất gia nhiệt hỏng "
               "ở vị trí đóng."))

    b.append(h2("Fail-in-place: giữ nguyên vị trí khi mất điện ngắn hạn",
                "Fail-in-place: holding position during a short power failure"))
    b.append(p("Trong một số trường hợp, bạn có thể muốn van giữ nguyên ở vị trí hành "
               "trình cuối cùng, đặc biệt khi hệ thống điều khiển bị mất điện trong thời "
               "gian ngắn. Ở đây, bộ truyền động điện kiểu bánh răng tiêu chuẩn là lựa "
               "chọn lý tưởng. Các bộ truyền động màng–lò xo và các bộ truyền động khí nén "
               "khác phải dùng van khóa để giữ áp suất khí bên trong bộ truyền động nếu "
               "mong muốn chế độ fail-in-place (giữ nguyên vị trí khi hỏng)."))
    b.append(p("Để phòng khi mất khí nén, hãy cho tín hiệu khí nén tới bộ truyền động đi "
               "qua một van được giữ mở bởi áp suất trong một đường cấp khí riêng biệt. "
               "Ngay khi áp suất cấp này giảm, van khóa sẽ đóng lại và giữ áp suất trong "
               "bộ truyền động. Để phòng khi mất tín hiệu, một van điện từ hai chiều "
               "(two-way solenoid valve) có thể thay thế van khóa khí nén và giữ khí lại "
               "khi mất điện."))

    b.append(h2("Chiều dòng chảy và hỏng trục van",
                "Flow direction and valve stem failure"))
    b.append(p("Để tăng mức độ an toàn, bạn có thể cân nhắc chiều dòng chảy qua van nhằm "
               "đề phòng hậu quả của việc hỏng trục van. Ví dụ, ở đây bạn muốn quy định "
               "chiều chảy của chất lưu là “flow-to-open” (chảy theo hướng mở) trong "
               "trường hợp van cần fail-open, hoặc “flow-to-close” (chảy theo hướng đóng) "
               "nếu mong muốn van đóng. Tuy nhiên, việc quy định nút van kiểu "
               "“flow-to-close” có thể tế nhị, vì nó có thể dẫn đến mất ổn định (nút van "
               "có thể đóng sập); xem Chương 10, “Bộ định vị van”."))

    b.append(h2("Các hậu quả theo mức độ nghiêm trọng tăng dần",
                "Consequences in order of increasing severity"))
    b.append(p("Khi xem xét các khía cạnh an toàn của một ứng dụng van điều khiển, hãy "
               "đánh giá các hậu quả có thể xảy ra sau đây theo thứ tự mức độ nghiêm "
               "trọng tăng dần:"))
    b.append(ol([
        "Giảm sản lượng sản phẩm",
        "Dừng quá trình sản xuất",
        "Hư hỏng thiết bị công nghệ",
        "Gây thương tích cho người hoặc thiệt mạng",
    ]))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR của các trang in có nhiều "
                  "dấu gạch nối khi xuống dòng («con-troller», «peri-odic», "
                  "«particu-larly», «fail-ure», «par-ticularly», «fail-in-place», "
                  "«follow-ing»); bản dịch ghép lại thành từ hoàn chỉnh. (2) Chỉ số chú "
                  "thích «1» trong nguyên bản đứng ngay sau «Typically» trong câu quy "
                  "định fail-close («fail close is specified if the fluid ...»), nhưng "
                  "nội dung chú thích lại được in ở chân trang 61, xen giữa câu về gia "
                  "nhiệt bằng hơi cho đường ống dầu thô. Bản dịch giữ nguyên sự gắn kết "
                  "của chú thích với câu fail-close."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 8 chiếm các trang in 55–56 của ấn bản in (PDF tr. 61–62). Nguyên "
               "bản không có hình, không có bảng và không có tài liệu tham khảo; chương "
               "chỉ có một chú thích đánh số và một danh sách gồm bốn mục theo mức độ "
               "nghiêm trọng tăng dần, tất cả đều được giữ lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Van màng–lò xo và khả năng an toàn khi hỏng",
                "Spring-diaphragm valves and fail-safe action"))
    b.append(p("One of the important benefits of spring-diaphragm-actuated control valves "
               "is their ability to fail-safe by the action of the precompressed actuator "
               "spring, that is, to close or open the valve on air failure or, more "
               "typically, breakage of the signal wire or controller malfunction."))

    b.append(h2("Bộ truyền động xi lanh và bộ truyền động điện",
                "Cylinder and electric actuators"))
    b.append(p("Cylinder-actuated valves do not fail-safe without the addition of springs "
               "or stored air pressure in a separated cylinder kept there by a "
               "pressure-actuated lockup valve. Sometimes, the flow direction of a "
               "single-seated globe valve is reversed so that the fluid forces help to "
               "close the valve plug (if fail close is desired)."))
    b.append(p("Typically, electric actuators do not provide fail-safe action unless a "
               "standby power source, such as a relay switch-actuated battery pack, is "
               "provided. Here, of course, periodic maintenance and recharging of the "
               "battery is a must."))

    b.append(h2("Hướng an toàn: đóng hay mở khi hỏng?",
                "Fail-safe direction: close or open?"))
    b.append(p("The fail-safe direction (open or closed) is usually dictated by safety "
               "concerns. Typically,<sup>1</sup> fail close is specified if the fluid to "
               "be handled is flammable (e.g., natural gas going to a burner) or is a "
               "heating medium going to a heat exchanger where adding too much heat to a "
               "kettle can cause boiling or can cause an exothermic reaction of a "
               "chemical. Most valves handling chemicals are specified as fail close "
               "valves."))
    b.append(note("<b>Footnote 1.</b> In 75% to 80% of all applications."))
    b.append(p("However, in some heating applications, fail open action is more "
               "advantageous. As an example, consider the steam tracing of a crude oil "
               "pipe. Here, too little viscosity (too much heat) is probably better than "
               "having the fluid come to a near standstill, particularly in the middle of "
               "winter. Another fail open application is controlling cooling fluid to a "
               "motor bearing where the worst effect may be a decrease in efficiency."))

    b.append(h2("Tự kiểm tra: nếu van đột ngột mở hoặc đóng?",
                "Self-check: if the valve suddenly opens or closes?"))
    b.append(p("Ask yourself, what would happen if this valve suddenly opens (or closes) "
               "on the failure of the air compressor or on signal failure (computer "
               "breakdown, wire breakage, lightning strike)? When in doubt, check with "
               "your process people. Another question to keep in mind is whether the "
               "downstream safety valve has sufficient flow capacity to handle the flow "
               "from a pressure-reducing valve when it fails wide-open. In the same vein, "
               "consider the effects on a trapped liquid experiencing thermal expansion "
               "when a valve that is supplying a heating medium fails in the closed "
               "position."))

    b.append(h2("Fail-in-place: giữ nguyên vị trí khi mất điện ngắn hạn",
                "Fail-in-place: holding position during a short power failure"))
    b.append(p("In some cases, you may wish the valve would remain in the last travel "
               "position, particularly if you are dealing with a short power failure to "
               "the control system. Here, the standard electric gear-type actuator is "
               "ideal. Spring-diaphragm and other pneumatic actuators have to use lockup "
               "valves to trap air pressure in the actuator if the fail-in-place mode is "
               "desired."))
    b.append(p("To guard against compressed air failure, have the pneumatic signal to the "
               "actuator pass through a valve that is kept open by the pressure in a "
               "separate air supply line. As soon as this supply pressure diminishes, it "
               "will close the lockup valve and trap the actuator pressure. To guard "
               "against signal failure, a two-way solenoid valve can take the place of "
               "the pneumatic lockup valve and trap the air on electrical power failure."))

    b.append(h2("Chiều dòng chảy và hỏng trục van",
                "Flow direction and valve stem failure"))
    b.append(p("For added safety, you may want to consider the flow direction through the "
               "valve to guard against the consequences of valve stem failure. Here, for "
               "example, you want to specify the direction of fluid flow as "
               "“flow-to-open” in case the valve should fail open, or “flow-to-close” if "
               "closure is desired. However, specifying a “flow-to-close” plug can be "
               "tricky because it can lead to instability (the plug may slam closed); see "
               "Chapter 10, “Valve Positioners.”"))

    b.append(h2("Các hậu quả theo mức độ nghiêm trọng tăng dần",
                "Consequences in order of increasing severity"))
    b.append(p("When considering the safety aspects of a control valve application, "
               "evaluate the following possible consequences in order of increasing "
               "severity:"))
    b.append(ol([
        "Decrease in product yield",
        "Shutdown of process",
        "Damage to process equipment",
        "Injury to personnel or loss of life",
    ]))

    b.append(note("<b>Source notes.</b> (1) The OCR text layer of the printed pages "
                  "contains line-break hyphenations («con-troller», «peri-odic», "
                  "«particu-larly», «fail-ure», «par-ticularly», «fail-in-place», "
                  "«follow-ing»); the translation joins them into whole words. (2) In the "
                  "source, the footnote marker «1» sits directly after «Typically» in the "
                  "fail-close sentence («fail close is specified if the fluid ...»), while "
                  "the footnote text is printed at the foot of page 61 in the middle of "
                  "the steam-tracing sentence. The translation keeps the footnote "
                  "attached to the fail-close sentence."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 8 occupies printed pp. 55-56 of the book (PDF pp. 61-62). The "
               "source has no figures, no tables, and no references; it contains one "
               "numbered footnote and a four-item ordered list of consequences in "
               "increasing severity, all of which are retained."))
    return "".join(b)
