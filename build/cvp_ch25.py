# -*- coding: utf-8 -*-
"""Book 7, Chapter 25 - Seat Leakage and Seat Materials / Độ rò rỉ đế van và
vật liệu đế van (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
153-155 (PDF pp. 151-153; printed = PDF + 2). Three printed pages, two tables
(Table 25-1 ANSI/FCI leakage classifications, Table 25-2 Class VI leakage
rates), no figures, no equations and no references. Covers soft versus metal
seating, seat-material temperature limits, the "How Does a Valve Close?"
calibration section, and positioner settings for sliding seals.
"""
from cvp_common import h2, lead, note, p, table

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Seat Leakage and Seat Materials"
TITLE_VI = "Độ rò rỉ đế van và vật liệu đế van"

# Table 25-2 numeric rows are language-neutral; only headers/captions localize.
_T25_2_ROWS = [
    ["1 (25 mm)", "0.15", "1"],
    ["1.5 (40 mm)", "0.30", "2"],
    ["2 (50 mm)", "0.45", "3"],
    ["2.5 (65 mm)", "0.60", "4"],
    ["3 (80 mm)", "0.90", "6"],
    ["4 (100 mm)", "1.70", "11"],
    ["6 (150 mm)", "4.00", "27"],
    ["8 (200 mm)", "6.75", "45"],
    ["10 (250 mm)", "11.1", "–"],
    ["12 (300 mm)", "16", "–"],
    ["14 (350 mm)", "21.6", "–"],
    ["16 (400 mm)", "28.4", "–"],
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 25.</b> rò rỉ đế van (seat leakage) · van ngắt / van "
                "chặn (shutoff valve) · kín nhỏ giọt (drip tight) · ANSI/FCI Class VI · "
                "ANSI B16.104 (FCI 70-2) · giao diện mềm (soft interface) · vòng đế "
                "(seat ring) · nút van (plug) · elastomer · vật liệu nhựa · xói mòn bề mặt "
                "làm kín · khả năng điều chỉnh lưu lượng nhỏ (rangeability) · tốc độ dòng "
                "nhỏ nhất · van lưu lượng nhỏ · van bướm dạng đung đưa (swing-through "
                "butterfly) · Buna N · Teflon · ma sát tĩnh / ma sát khởi động (static or "
                "break-away friction) · ma sát động · mất ổn định tạm thời · thép không gỉ "
                "Type 316 · thép Type 440 C · hợp kim coban Stellit · kỹ thuật mài láp "
                "(lapping) · điều kiện chảy tầng (laminar flow) · cơ chế làm kín ép xuống "
                "(push-down seal) · cơ chế làm kín trượt (sliding seal) · van bướm · van "
                "bi cầu lệch tâm · hiệu chỉnh bộ định vị (positioner calibration) · chế độ "
                "fail close / fail open · tín hiệu 3–15 psi · 4–20 mA · tín hiệu định vị "
                "vượt điểm chảy · góc quay dư · áp suất thử tại xưởng")
    return ("<b>Key terms.</b> seat leakage · shutoff valve · drip tight · ANSI/FCI Class VI "
            "· ANSI B16.104 (FCI 70-2) · soft interface · seat ring · plug · elastomer · "
            "plastic material · erosion of seating surfaces · rangeability · minimum "
            "controlled flow rate · small flow valve · swing-through butterfly valve · "
            "Buna N · Teflon · static or break-away friction · dynamic friction · temporary "
            "valve instability · Type 316 stainless steel · Type 440 C · cobalt alloy "
            "Stellit · lapping · laminar flow · push-down seal · sliding seal · butterfly "
            "valve · eccentric rotary ball valve · positioner calibration · fail close / "
            "fail open · 3–15 psi · 4–20 mA · signal beyond flow stoppage · extra rotary "
            "degrees · shop test pressure")


def body_vi():
    b = []
    b.append(lead("Vì muốn tiết kiệm tiền và không gian đường ống, hầu hết người dùng tìm "
                  "một van điều khiển có thể kiêm luôn van chặn. Than ôi, điều đó không dễ "
                  "đạt được."))
    b.append(h2("Độ rò rỉ đế van và vật liệu đế van", "Seat Leakage and Seat Materials"))
    b.append(p("Thứ nhất, để đạt mức “không nhỏ giọt” (drip tight) — ANSI/FCI Class VI, "
               "xem Bảng 25-1 — phải có một giao diện mềm giữa vòng đế và nút van, chẳng "
               "hạn như elastomer hoặc vật liệu nhựa. Điều này lại loại trừ các ứng dụng "
               "nhiệt độ cao."))
    b.append(p("Thứ hai, van điều khiển luôn luôn tiết lưu. Điều đó có nghĩa là bề mặt làm "
               "kín có thể chịu vận tốc chất lưu rất cao gây xói mòn. Thường thì chất lưu "
               "được điều khiển còn chứa các hạt rắn làm tăng tốc độ mòn. Vì vậy, mức rò "
               "rỉ mà nhà sản xuất chứng nhận lúc van xuất xưởng có thể không còn đúng "
               "khi van đưa vào vận hành."))
    b.append(p("Tuy nhiên, vẫn có những ứng dụng cho phép dùng van điều khiển làm thiết bị "
               "chặn, dù chỉ trong trường hợp khẩn cấp. Có thể kể đến van bypass hơi trong "
               "nhà máy điện nguyên tử. Ngoài ra còn có các vòng điều khiển không trọng "
               "yếu, nơi có thể chấp nhận một lượng rò nhỏ: lượng chất lưu rò ra không "
               "ảnh hưởng đáng kể đến quá trình và không gây nguy hiểm."))
    b.append(p("Một tiêu chí khác là khả năng điều chỉnh lưu lượng nhỏ (rangeability). Lưu "
               "lượng tối thiểu mà bạn muốn điều khiển không được nhỏ hơn tốc độ rò rỉ "
               "(xem Bảng 25-2). Điều này cần cân nhắc với van lưu lượng nhỏ hoặc van bướm "
               "dạng đung đưa. Loại vật liệu đế thường quyết định mức rò rỉ mong đợi. Như "
               "đã nêu ở chương trước, vật liệu đế mềm cho mức rò rỉ thấp nhất, thường là "
               "Class VI theo ANSI B16.104-1976 (FCI 70-2)."))
    b.append(table(
        ["Lớp", "Rò rỉ cho phép", "Môi trường thử", "Chênh áp thử"],
        [
            ["I", "Không yêu cầu thử", "", ""],
            ["II", "0,5% công suất định mức", "Không khí hoặc nước ở nhiệt độ phòng",
             "45 đến 60 psi ra khí quyển*"],
            ["III", "0,1% công suất định mức", "Không khí hoặc nước ở nhiệt độ phòng",
             "45 đến 60 psig ra khí quyển"],
            ["IV", "0,01% công suất định mức", "Không khí hoặc nước ở nhiệt độ phòng",
             "45 đến 60 psig ra khí quyển"],
            ["V", "0,0005 ml/phút nước cho mỗi inch đường kính đế (D) ở chênh áp "
                  "vận hành cực đại",
             "4,7 ml/phút không khí hoặc nitơ cho mỗi inch đường kính đế (c)",
             "50 psig ra khí quyển (c)**"],
            ["VI", "Xem bảng liệt kê", "Không khí hoặc nitơ ở 50–125°F",
             "50 psig hoặc áp suất vận hành (b)"],
        ],
        caption="Bảng 25-1. Phân loại rò rỉ đế van điều khiển theo ANSI B16.104 (FCI 70-2). "
                "* Nếu thấp hơn 50 psi. ** Thử thay bằng không khí hoặc N₂. "
                "Đã sửa theo IEC 60534-4-4 (2008)."))
    b.append(p("Các elastomer như Buna N được dùng ở nhiệt độ trung bình (đến 180°F), trong "
               "khi Teflon được dùng rộng rãi khi có chất lưu ăn mòn. Giới hạn nhiệt độ "
               "của Teflon là 450°F. Cần lưu ý khi dùng Teflon làm vật liệu đế trong một "
               "số van quay như van bướm hoặc van bi: ma sát tĩnh hay ma sát “khởi động” "
               "(break-away) có thể lớn gấp hai hoặc hơn ma sát vận hành (ma sát động). "
               "Có thể cần lực cơ cấu chấp hành đáng kể để thắng ma sát tĩnh, dẫn đến "
               "mất ổn định tạm thời của van."))
    b.append(table(
        ["(D) Đường kính đế (inch)", "Tốc độ rò (ml/phút, cc/phút)", "Bọt khí/phút"],
        _T25_2_ROWS,
        caption="Bảng 25-2. Tốc độ rò rỉ Class VI theo đường kính đế (bản in)."))
    b.append(h2("Có thể nói điều tương tự cho một số van đế kim loại như van bướm hiệu "
                "năng cao, dù mức độ nghiêm trọng thấp hơn. Van có đế kim loại‑kim loại "
                "được dùng trong hầu hết van điều khiển dạng cầu (globe). Ở chênh áp thấp "
                "(đến 500 psi), thép không gỉ Type 316 là lựa chọn ưu tiên; khi đó tốc độ "
                "rò thường gặp của van một đế là Class IV và của van hai đế là Class II. "
                "Type 440 C là thép không gỉ tôi cứng, thường dùng cho hơi nước đến 800°F. "
                "Hợp kim coban như Stellit là vật liệu đế ưu tiên cho nhiệt độ cao hơn "
                "(đến 1500°F) và áp suất cao. Một lần nữa, rò rỉ đế điển hình (một đế) "
                "đạt Class IV, dù — cũng như với đế thép không gỉ — có thể đạt Class V "
                "bằng kỹ thuật mài láp đặc biệt.",
                "Metal-seated valves and seat-material selection"))
    b.append(p("Đặc tả rò rỉ Class V dùng khí làm môi trường thử là tiêu chuẩn tương đối "
               "mới. Số lượng cho phép được suy từ thể tích thử bằng nước với giả thiết "
               "dòng chảy tầng. Ví dụ, với đế đường kính 4 inch, rò rỉ cho phép là "
               "4,7 × 4 = 18,8 cc/phút."))
    b.append(h2("Van đóng như thế nào?", "How Does a Valve Close?"))
    b.append(p("Có hai cơ chế làm kín khác nhau trong van điều khiển: cơ chế ép xuống "
               "(push-down seal, như trong van cầu) và cơ chế trượt (sliding seal, thấy "
               "trong van bướm và van bi quay lệch tâm). Cơ chế ép xuống cần thêm lực để "
               "ngăn rò, trong khi cơ chế trượt cần thêm góc quay vượt qua điểm chất lưu "
               "ngừng chảy. Phải nhận thức được điều này khi hiệu chỉnh bộ định vị van. "
               "Bộ định vị cho van cầu ở chế độ fail close nên được hiệu chỉnh ở 4 psi "
               "(5 mA) khi nút van đã nằm trên đế (để ngăn dòng chảy), để khi tín hiệu "
               "giảm xuống 3 psia (4 mA) vẫn có đủ lực từ cơ cấu chấp hành ngăn rò rỉ. "
               "Ở chế độ fail open, chọn tín hiệu lần lượt là 14 và 15 psi (18 và 20 mA)."))
    b.append(p("Van quay cần khoảng năm độ quay thêm sau điểm ngăn dòng để cơ chế làm "
               "kín trượt ăn khít và ngăn rò. Một lần nữa, hãy cho phép ít nhất một psi "
               "tín hiệu vượt qua điểm ngăn dòng."))
    b.append(p("Nếu làm đúng các điều trên, tại hiện trường sẽ không có rò rỉ. Cũng cần "
               "nhớ rằng áp suất chất lưu thực tế khi vận hành cao hơn nhiều so với áp "
               "suất thử 50 psi tại xưởng."))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Bảng 25-1 và Bảng 25-2 được trình bày "
                  "liền nhau trên trang in; ở đây Bảng 25-1 được đặt trước vì được trích "
                  "dẫn trước trong văn bản. Các chú thích gốc (*, **, (b), (c)) và ghi chú "
                  "sửa đổi theo IEC 60534-4-4 (2008) được giữ lại. Chương này không có "
                  "hình, phương trình hay tài liệu tham khảo."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © 2011 Hans D. Baumann, do ISA / John Wiley &amp; Sons xuất bản.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(lead("To save money and piping space, most users look for a control valve "
                  "that can double as a shutoff valve. Alas, this is hard to accomplish."))
    b.append(h2("Seat Leakage and Seat Materials", "Seat Leakage and Seat Materials"))
    b.append(p("First, to be “drip tight” (ANSI/FCI Class VI, see Table 25-1), there has "
               "to be a soft interface between the seat ring and plug, such as an "
               "elastomer or a plastic material. This then excludes high-temperature "
               "applications."))
    b.append(p("Second, control valves throttle all the time. This means that seating "
               "surfaces can be subjected to very high fluid velocities that can cause "
               "erosion. Often there are entrained particles within the controlled fluid "
               "that hasten the wear. This implies that whatever the manufacturer "
               "certified as measured leakage when the valve left the plant may not be "
               "applicable when the valve is put in service."))
    b.append(p("Nevertheless, there are applications where a control valve can be used "
               "as a shutoff device, even if only in an emergency. A steam bypass valve "
               "in an atomic power plant comes to mind. There are other noncritical loop "
               "applications where a small leakage can be tolerated, where the amount of "
               "leaked fluid has no material impact on the process, and there is no "
               "safety hazard."))
    b.append(p("Another criterion is rangeability. The minimum flow rate that you want "
               "to control should not be less than the leakage rate (see Table 25-2). "
               "This can be a consideration with small flow valves or swing-through "
               "butterfly valves. The type of seat material often determines the "
               "expected seat leakage rate. As mentioned previously, a soft seating "
               "material will provide the lowest leakage rate, typically Class VI of "
               "ANSI B16.104-1976 (FCI 70-2)."))
    b.append(table(
        ["Class", "Allowable Leakage", "Test Medium", "Test Pressure Drop"],
        [
            ["I", "No test required", "", ""],
            ["II", "0.5% of rated capacity", "Air or water at room temperature",
             "45 to 60 psi to atmosphere*"],
            ["III", "0.1% of rated capacity", "Air or water at room temperature",
             "45 to 60 psig to atmosphere"],
            ["IV", "0.01% of rated capacity", "Air or water at room temperature",
             "45 to 60 psig to atmosphere"],
            ["V", "0.0005 ml per minute of water per inch of seat diameter (D) at "
                  "maximum service pressure drop",
             "4.7 ml per minute of air or nitrogen per inch of seat diameter (c)",
             "50 psig to atmosphere (c)**"],
            ["VI", "See tabulation", "Air or nitrogen at 50–125°F",
             "50 psig or operating pressure(b)"],
        ],
        caption="Table 25-1. Control valve seat leakage classifications per ANSI B16.104 "
                "(FCI 70-2). * If lower than 50 psi. ** Alternate air or N2 test. "
                "Revised per IEC 60534-4-4 (2008)."))
    b.append(p("Elastomers such as Buna N are used for moderate temperature (to 180°F), "
               "while Teflon is widely used when corrosive fluids are involved. The "
               "temperature limit for Teflon is 450°F. Attention should be given if "
               "Teflon is used as seating material in certain rotary valves such as "
               "butterfly or ball valves. Static or “break-away” friction can sometimes "
               "be two or more times the operating friction (dynamic friction). It may "
               "take considerable actuator force to overcome this static friction "
               "leading to temporary valve instability."))
    b.append(table(
        ["(D) Seat Diameter in Inches", "Leakage Rate in ml per Minute (cc/min)",
         "Bubbles per Minute"],
        _T25_2_ROWS,
        caption="Table 25-2. Class VI leakage rates by seat diameter (as printed)."))
    b.append(h2("Metal-to-metal seats and seat-material selection",
                "Metal-to-metal seats and seat-material selection"))
    b.append(p("The same may be said about some metal-seated valves such as "
               "high-performance butterfly valves, although the problem is less severe. "
               "Metal-to-metal seat valves are used in nearly all globe control valves. "
               "For low pressure drops (up to 500 psi), Type 316 stainless steel is the "
               "preferred choice where the usual leakage rate for single-seated valves "
               "is Class IV and for double-seated valves Class II. Type 440 C is a "
               "hardened stainless steel often used for steam applications up to 800°F. "
               "A cobalt alloy such as Stellit is the preferred seat material for higher "
               "temperatures (up to 1500°F) and high pressures. Again, the typical seat "
               "leakage (single seat) conforms to Class IV, although, as with the "
               "stainless steel seating, Class V can be met with special lapping "
               "techniques."))
    b.append(p("The Class V leakage specification using gas as a test medium is a "
               "relatively new standard. The allowable quantities are derived from the "
               "water test volumes assuming laminar flow conditions. For example, with "
               "a 4-inch seat diameter, the allowable leakage is 4.7 × 4 = 18.8 cc/min."))
    b.append(h2("How Does a Valve Close?", "How Does a Valve Close?"))
    b.append(p("There are two distinct sealing mechanisms in control valves: push-down "
               "seals (such as in globe valves) and the sliding seals (found in "
               "butterfly and eccentric rotary ball valves). Push-down seals require "
               "extra force to stop leaking, whereas sliding seals require extra "
               "rotation beyond the point where fluid flow is stopped. This fact must "
               "be realized when calibrating valve positioners. Positioners for globe "
               "valves in the fail close position should be calibrated at 4 psi (5 mA) "
               "when the plug sits on the seat (to stop flow), so when the signal drops "
               "to 3 psia (4 mA), there is sufficient force from the actuator to stop "
               "the leakage. For fail open mode, signal selection should be 14 and 15 "
               "psi (18 and 20 mA), respectively."))
    b.append(p("Rotary valves need about five extra degrees beyond fluid stopping to "
               "engage a sliding seal sufficiently to stop leakage. Again, allow at "
               "least one extra signal psi beyond the point of fluid stoppage."))
    b.append(p("If you do all this correctly, there will be no leakage in the field. "
               "Realize too, actual fluid pressures in service are much higher than the "
               "50 psi test pressure in the shop."))
    b.append(note("<b>Source quirks.</b> Tables 25-1 and 25-2 appear adjacent on the "
                  "printed page; Table 25-1 is placed first here because it is cited "
                  "first in the text. The original footnotes (*, **, (b), (c)) and the "
                  "revision note per IEC 60534-4-4 (2008) are retained. The chapter has "
                  "no figures, equations or references."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 2011 Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)
