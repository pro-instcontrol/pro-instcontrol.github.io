# -*- coding: utf-8 -*-
"""Book 7, Chapter 26 - Valves for Sanitary or Aseptic Service / Van dùng cho
dịch vụ vệ sinh hoặc vô trùng (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
157-163 (PDF pp. 154-160; printed = PDF + 3). Seven printed pages, four
figures (angle valve, modern flow-to-open sanitary valve, diaphragm valve,
improved modulating diaphragm valve), one surface-finish table (Table 26-1)
and three references. No equations.
"""
from cvp_common import fig, h2, h3, note, ol, p, refs, table

import cvpfig26 as F

PAGES_SRC = 7
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Valves for Sanitary or Aseptic Service"
TITLE_VI = "Van dùng cho dịch vụ vệ sinh hoặc vô trùng"

_REFS = [
    "H. D. Baumann, “Construction and Application of Modulating Control Valves for "
    "Bioprocessing Systems,” Bioprocessing Engineering Symposium, ASME BED-Vol. 21 "
    "(1991): 93–96.",
    "ASME Standard BPE-1997, Bioprocessing Equipment (New York: The American Society "
    "of Mechanical Engineers).",
    "J. D. Ciancarelli, “Sanitary Control Valves for the Biotech Industry,” InTech "
    "(May 1991): 18–21.",
]

# Table 26-1 rows differ by language only in the range connector ("to" / "đến").
_T26_1_ROWS_VI = [
    ["150", "30 đến 35", "0,8 đến 0,9", "45", "N6"],
    ["240", "15 đến 20", "0,4 đến 0,5", "17", "N5"],
    ["320", "8 đến 12", "0,2 đến 0,3", "9", "N4"],
]
_T26_1_ROWS_EN = [
    ["150", "30 to 35", "0.8 to 0.9", "45", "N6"],
    ["240", "15 to 20", "0.4 to 0.5", "17", "N5"],
    ["320", "8 to 12", "0.2 to 0.3", "9", "N4"],
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 26.</b> van vệ sinh (sanitary valve) · van vô trùng / "
                "aseptic (germ-free) · chế biến sữa · cụm thân van đánh bóng cao · tháo rời "
                "nhanh · rửa sau mỗi lần dùng · CIP (làm sạch tại chỗ) · SIP (tiệt trùng tại "
                "chỗ) · hàn quỹ đạo (orbital welding) · hệ thống sinh học · van đóng‑mở tự "
                "động · van điều tiết kiểu modulát · giảm áp hơi tiệt trùng · nước tinh khiết "
                "· 3-A Council · van góc tự thoát nước · độ nhám trung bình Ra · Grip Finish "
                "· đế kim loại · vòng O-ring thân van · hướng chảy đóng (flow-to-close) · hướng "
                "chảy mở (flow-to-open) · phục hồi áp suất · hệ số FL · xâm thực · ASME "
                "BPE · van màng (diaphragm valve) · đặc tính lưu lượng kém · cơ cấu chấp hành "
                "piston áp suất khí cao · bộ định vị van · lò xo đối kháng · màng EPDM phủ "
                "PTFE liên kết hóa học · lối chảy hình khuyên · khe tiết lưu · vát 45° · "
                "cơ cấu bật toggle · phớt phụ (secondary seal) và kết nối báo động (telltale) · "
                "băng chết (deadband) · bố trí cơ cấu chấp hành nằm ngang")
    return ("<b>Key terms.</b> sanitary valve · aseptic (germ-free) valve · dairy processing "
            "· highly polished body subassembly · rapid disassembly · wash after each use · "
            "CIP (cleaned-in-place) · SIP (sterilized-in-place) · orbital welding · "
            "bioprocessing · automated on-off valve · modulating control valve · sterile "
            "steam pressure reduction · high-purity water · 3-A Council · self-draining "
            "angle valve · roughness average Ra · grit finish · metal plug · stem O-ring · "
            "flow-to-close · flow-to-open · pressure recovery · FL · cavitation · ASME BPE · "
            "diaphragm valve · poor flow characteristic · high-air-pressure piston actuator "
            "· valve positioner · spring-opposed diaphragm actuator · PTFE-faced EPDM "
            "diaphragm · circular orifice · throttling gap · 45° retracted slope · toggle "
            "mechanism · secondary seal and telltale connection · deadband · horizontal "
            "actuator mounting")


def body_vi():
    b = []
    b.append(h2("Van dùng cho dịch vụ vệ sinh hoặc vô trùng",
                "Valves for Sanitary or Aseptic Service"))
    b.append(p("Van điều khiển vệ sinh đã tồn tại từ khi các sản phẩm sữa được chế biến tự "
               "động. Đó là các cụm thân van được đánh bóng cao, có thể tháo rời nhanh và "
               "được rửa sau mỗi lần sử dụng."))
    b.append(p("Van điều khiển dùng trong công nghiệp sinh học lại là chuyện khác. Trong khi "
               "van vệ sinh phải “sạch”, van sinh học phải không chứa vi khuẩn (vô trùng, "
               "aseptic). Hơn nữa, khác với van chế biến thực phẩm vệ sinh (xem Hình 26-1), "
               "van sinh học không bị tháo rời mà được làm sạch tại chỗ (CIP) và tiệt trùng "
               "tại chỗ (SIP) [1]. Thường thì các van này được hàn vào đường ống bằng kỹ "
               "thuật hàn quỹ đạo (orbital welding)."))
    b.append(p("Van điều khiển kiểu modulát, trái với van đóng‑mở tự động, đang được dùng "
               "ngày càng nhiều, đặc biệt trong các hệ thống sinh học được nâng cấp từ quy "
               "mô mẻ nhỏ lên sản xuất lớn. Ứng dụng trải từ giảm áp hơi tiệt trùng đến tiêm "
               "và điều khiển lưu lượng nước tinh khiết với lưu lượng từ 0,001 đến 500 L/phút. "
               "Thiết kế của các van này phải đáp ứng yêu cầu CIP và SIP [2]; có thể cho "
               "đặc tính lưu lượng tốt, khả năng điều chỉnh rộng (rangeability cao), đóng kín "
               "chặt và ma sát vận hành thấp; đồng thời chống xâm thực và tự thoát nước để "
               "đáp ứng yêu cầu của vòng điều khiển ổn định với thời gian chết tối thiểu do "
               "phần tử điều khiển tạo ra."))
    b.append(p("Các kiểu van sớm dùng trong thiết bị sinh học ban đầu được thiết kế cho "
               "ngành thực phẩm theo hướng dẫn của Hội đồng 3-A nhằm đáp ứng yêu cầu "
               "“vệ sinh” [3]."))
    b.append(fig(1, F.fig_f261()))
    b.append(p("Van góc trên Hình 26-1 là ví dụ điển hình của van vệ sinh. Van đáp ứng mọi "
               "yêu cầu của thiết kế vệ sinh: tự thoát nước, có thể đánh bóng đến độ hoàn "
               "thiện bề mặt yêu cầu — thường là độ nhám trung bình (Ra) 0,15 đến 0,20 µM — "
               "và có thể có độ kín thỏa đáng tại giao diện giữa mặt bích thân trên và nắp "
               "dẫn hướng thân van. Tuy nhiên, vòng O-ring ở thân van là vùng khó tiệt trùng "
               "và làm sạch cho dịch vụ vô trùng. Việc liên tục cho van chu trình trong quá "
               "trình tiệt trùng có lẽ là cách duy nhất để thực hiện việc này, đòi hỏi một "
               "hệ thống điều khiển định thời phụ trợ."))
    b.append(p("Nút van cho đặc tính lưu lượng chấp nhận được. Tuy nhiên, hướng chảy "
               "flow-to-close lại khuyến khích phục hồi áp suất (FL thấp), tức là vận tốc "
               "tiết lưu cao hơn cho cùng một chênh áp và xu hướng xâm thực với chất lỏng. "
               "Ngoài ra, nút kim loại không cho đóng kín chặt. Kiểu hiện đại hơn được trình "
               "bày trên Hình 26-2, trong đó hướng flow-to-close dễ mất ổn định đã được thay "
               "bằng hướng flow-to-open ổn định. Ở đây vòng O-ring được bố trí ở vị trí có "
               "thể làm sạch và đáp ứng yêu cầu của tiêu chuẩn sinh học ASME (American "
               "Society for Mechanical Engineers) [2]. Van này dùng được cho cả ứng dụng "
               "vệ sinh lẫn vô trùng."))
    b.append(fig(2, F.fig_f262()))
    b.append(p("Một thiết kế đã được kiểm chứng thời gian là van màng trình bày trên Hình "
               "26-3, cũng có thể dùng trong ứng dụng không vệ sinh. Van có khả năng đóng kín "
               "tốt và cấu trúc đáp ứng yêu cầu vô trùng của hệ thống. Nhược điểm lớn là đặc "
               "tính lưu lượng kém. Có thể cải thiện phần nào bằng cách dùng cơ cấu chấp hành "
               "hai bước để khắc phục nhược điểm này. Vì áp suất chất lưu tác động lên diện "
               "tích màng tương đối lớn, lực chấp hành cao, đòi hỏi cơ cấu chấp hành piston "
               "dùng khí áp suất cao (và bộ định vị van đắt tiền) hoặc cơ cấu màng đối kháng "
               "lò xo lớn (so với kích thước van)."))
    b.append(fig(3, F.fig_f263()))
    b.append(p("Một thiết kế phổ biến khác dùng màng vừa làm nắp bịt thân vừa làm cơ cấu làm "
               "kín van, như trên Hình 26-4 [1]. Ở đây đặc tính lưu lượng về cơ bản là tuyến "
               "tính nhờ dùng lỗ tròn thay vì weir và hành trình màng tương đối ngắn. Thân "
               "van đáp ứng mọi yêu cầu về vật liệu và độ hoàn thiện bề mặt vô trùng (xem "
               "Bảng 26-1) và tự thoát nước. Yêu cầu lực chấp hành cao của van màng được "
               "khắc phục bằng cơ cấu bật toggle bằng thép không gỉ đặt bên trong nắp van, "
               "nắp này còn được trang bị phớt phụ và kết nối báo động (telltale) để phòng "
               "màng bị vỡ. Điều đáng chú ý nữa là hình dạng dòng chảy đặc biệt của màng. "
               "Hãy nhìn chỗ lõm rỗng phía trên lỗ: nó tạo đường vào cong cho chất lưu chảy "
               "vào vùng tiết lưu hẹp dọc theo mép lỗ. Sau khi đi qua “khe tiết lưu” này, "
               "chất lưu đột ngột tách khỏi màng nhờ độ dốc lùi khoảng 45° của màng. Kiểu "
               "chảy đột ngột này tránh dính chất lưu và giảm phục hồi áp suất của tia "
               "(FL ≥ 0,85), đảm bảo xu hướng xâm thực thấp."))
    b.append(fig(4, F.fig_f264()))
    b.append(p("Van này thường được trang bị màng ethylene propylene diene monomer (EPDM) "
               "được phủ polytetrafluorethylene (PTFE) bằng liên kết hóa học. Chuyển động lăn "
               "của màng ngăn không cho màng bị kéo dãn — điều sẽ làm tách lớp phủ PTFE "
               "(Teflon). Kinh nghiệm cho thấy sự kết hợp vật liệu này chịu được điều kiện "
               "khắc nghiệt của hơi nước lên đến 160°C (330°F), ngay cả khi van dùng liên tục "
               "cho dịch vụ giảm áp hơi. Cơ cấu bật khuếch đại cơ học cũng giảm ma sát của "
               "các bộ phận bên trong chuyển động. Kết quả là băng chết điển hình của van "
               "nhỏ hơn 2% dải tín hiệu, nên van dùng được mà không cần bộ định vị riêng và "
               "mức tiêu thụ khí cao liên quan."))
    b.append(p("Một mặt tiêu cực của cấu trúc này là cần lắp cơ cấu chấp hành trong mặt "
               "phẳng nằm ngang để thoát nước, đòi hỏi giá đỡ cho cơ cấu chấp hành ở cỡ lớn."))
    b.append(table(
        ["Grit", "Hoàn thiện Ra", "μinch", "μmeter RMS", "Số ISO"],
        _T26_1_ROWS_VI,
        caption="Bảng 26-1. So sánh độ hoàn thiện bề mặt [3]. (Bản in ghi “0,4 t đến 0,5”; "
                "ở đây hiệu chỉnh thành “0,4 đến 0,5”.)"))
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Bảng 26-1 nằm cuối chương, sau phần "
                  "thảo luận về vật liệu và độ hoàn thiện bề mặt; ở đây bảng được đặt sau "
                  "đoạn mô tả Hình 26-4 để giữ mạch đọc. Giá trị “0,4 t đến 0,5” trong bản in "
                  "là lỗi gõ, được hiệu chỉnh thành “0,4 đến 0,5”. Chú thích của Hình 26-4 "
                  "ghi “septic service” (dịch vụ nhiễm khuẩn) — có thể là lỗi in của “aseptic "
                  "service” — được giữ nguyên trong bản tiếng Anh. Không có phương trình "
                  "nào trong chương này."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © 2011 Hans D. Baumann, do ISA / John Wiley &amp; Sons xuất bản.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Valves for Sanitary or Aseptic Service",
                "Valves for Sanitary or Aseptic Service"))
    b.append(p("Sanitary control valves have been around as long as dairy products have "
               "been processed automatically. These are highly polished body subassemblies "
               "that can be taken apart rapidly and are washed after each use."))
    b.append(p("Control valves used in the bioprocessing industry are another matter. "
               "Whereas sanitary control valves must be “clean,” the bioprocessing valve "
               "must be germ-free (aseptic). Also, in contrast to sanitary food-processing "
               "valves (see Figure 26-1), bioprocessing valves are not disassembled but "
               "cleaned-in-place (CIP) and sterilized-in-place (SIP) [1]. Frequently, such "
               "valves are welded by orbital welding techniques to the pipe."))
    b.append(p("Modulating-type control valves, in contrast to automated on-off valves, "
               "are seeing increased use, especially in bioprocess systems that are "
               "upgraded from small batch systems to larger production systems. Applications "
               "range from pressure reduction of sterile steam to injection and flow "
               "control of high-purity water in quantities from 0.001 to 500 L/min. Designs "
               "for such valves must meet CIP and SIP requirements [2]; be able to provide "
               "good flow characteristic, high rangeability, tight shutoff, and low operating "
               "friction; and be cavitation resistant and self-draining to meet the "
               "requirements for a stable control loop calling for minimum dead time by the "
               "controlling element."))
    b.append(p("Early valve types used in bioprocess equipment were originally designed "
               "for the food industry under the guidelines of the 3-A Council to meet "
               "“sanitary” requirements [3]."))
    b.append(fig(1, F.fig_f261()))
    b.append(p("The angle valve shown in Figure 26-1 is a typical example of a sanitary "
               "valve. It meets all requirements of a sanitary design. It is self-draining, "
               "can be polished to the required surface finish, usually has a roughness "
               "average (Ra) of 0.15 to 0.20 µM, and can have sufficient seal integrity at "
               "the interface between the upper housing flange and the bonnet guiding the "
               "stem. However, the stem O-ring seal is a difficult area to sterilize and "
               "clean for aseptic service. Continuous cycling of the valve during the "
               "sterilization process is perhaps the only way to accomplish this task, "
               "calling for an auxiliary timing control system."))
    b.append(p("The valve plug provides an acceptable flow characteristic. However, the "
               "flow-to-close fluid flow direction will encourage pressure recovery (low "
               "FL), that is, higher throttling velocities for a given pressure drop and "
               "the tendency to cavitate with liquids. Also, metal plugs will not provide "
               "a tight shutoff. A more modern type is shown in Figure 26-2, where the "
               "instability-prone flow-to-close has been replaced by a stable flow-to-open "
               "design. Here the O-ring seal is located to be cleanable and to meet the "
               "requirements of the American Society for Mechanical Engineers (ASME) "
               "bioprocessing standard [2]. This valve can be used for both sanitary and "
               "aseptic applications."))
    b.append(fig(2, F.fig_f262()))
    b.append(p("Another time-proven design is the diaphragm valve shown in Figure 26-3, "
               "which can also be used in nonsanitary applications. It has good shutoff "
               "capability and a construction that can meet the aseptic requirements of the "
               "system. A major drawback is the poor flow characteristic. Some improvements "
               "can be made using a two-step actuating device to overcome this handicap. "
               "Because the fluid pressure is acting on a relatively large diaphragm area, "
               "actuator forces are high, thus requiring high-air pressure piston actuators "
               "(and expensive valve positioners) or large (in comparison to the valve "
               "size) spring-opposed diaphragm actuators."))
    b.append(fig(3, F.fig_f263()))
    b.append(p("Another common design employs a diaphragm serving as a combination housing "
               "closure and valve sealing member as shown in Figure 26-4 [1]. Here the flow "
               "characteristic is essentially linear due to the employment of a circular "
               "orifice, instead of a weir, and a relatively short diaphragm travel. The "
               "valve housing meets all aseptic material and surface finish (see Table 26-1) "
               "requirements and is self-draining. The high actuator force requirement of "
               "diaphragm valves is overcome by the employment of a unique stainless steel "
               "toggle mechanism inside the valve bonnet, which, incidentally, is equipped "
               "with a secondary seal and telltale connection to guard against diaphragm "
               "rupture. Of additional interest is the special flow profile of the "
               "diaphragm. Notice the hollow indentation above the orifice. This leads to a "
               "curved inlet path for the fluid to flow into the narrow throttling area "
               "along the rim of the orifice. After passing this “throttling gap,” the fluid "
               "is suddenly separated from the diaphragm due to the diaphragm's approximate "
               "45° retracted slope. This abrupt flow pattern avoids fluid attachment and "
               "reduces pressure recovery of the fluid jet (FL ≥0.85), assuring a low "
               "tendency to cavitate."))
    b.append(fig(4, F.fig_f264()))
    b.append(p("This valve is typically equipped with an ethylene propylene diene monomer "
               "(EPDM) diaphragm that is polytetrafluorethylene (PTFE)-faced by chemical "
               "bonding. The rolling action of the diaphragm prevents stretching, which "
               "would separate the PTFE (Teflon) coating. Experience has shown that this "
               "material combination survives the rigors of up to 160°C (330°F) steam "
               "service even when the valve is used in continuous steam pressure-reducing "
               "service. The mechanical amplifying toggle mechanism also reduces friction "
               "from the moving internal valve parts. As a result, the typical deadband of "
               "the valve is less than 2% of the signal span, so the valve can be used "
               "without a separate valve positioner and the associated higher air "
               "consumption."))
    b.append(p("One negative aspect of this construction is the need to mount the actuator "
               "in the horizontal plane to achieve drainage, which calls for actuator "
               "support in larger sizes."))
    b.append(table(
        ["Grit Finish", "Roughness Average Ra", "μinch", "μmeter RMS", "ISO No."],
        _T26_1_ROWS_EN,
        caption="Table 26-1. Surface finish comparison [3]. (The printed “0.4 t to 0.5” "
                "is corrected here to “0.4 to 0.5”.)"))
    b.append(h3("References", "References"))
    b.append(refs(_REFS))
    b.append(note("<b>Source quirks.</b> Table 26-1 appears at the very end of the printed "
                  "chapter, after the material and surface-finish discussion; it is placed "
                  "after the Figure 26-4 paragraph here to preserve the reading flow. The "
                  "printed “0.4 t to 0.5” is a typo, corrected to “0.4 to 0.5”. The Figure "
                  "26-4 caption says “septic service” — likely a misprint for “aseptic "
                  "service” — retained in the English text. There are no equations in this "
                  "chapter."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 2011 Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)
