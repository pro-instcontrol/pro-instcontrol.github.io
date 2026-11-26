# -*- coding: utf-8 -*-
"""Book 7, Chapter 30 - The Bus System to the Rescue, or What the Future May
Bring / Hệ thống bus tới giải cứu, hay tương lai sẽ mang lại gì (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
175-181 (PDF pp. 169-175; printed = PDF + 6). Seven printed pages: solid-state
valves, fieldbus and distributed control, the smart-valve concept with a
vortex meter, an air-loaded regulator alternative, wireless Ethernet, four
vector figures, one footnote and one reference. No tables or equations.
"""
from cvp_common import fig, h2, h3, note, p, refs

import cvpfig30_a as FA
import cvpfig30_b as FB

PAGES_SRC = 7
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "The Bus System to the Rescue, or What the Future May Bring"
TITLE_VI = "Hệ thống bus tới giải cứu, hay tương lai sẽ mang lại gì"

_REFS = [
    "H. D. Baumann, “Important Trends in Control Valves and Actuators,” Instrument "
    "&amp; Control Systems (November 1975): 21–25.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 30.</b> van điều khiển tiết lưu · chuyển động vĩnh cửu · "
                "entropy · dòng chảy rối / dòng chảy tầng · van thể rắn (solid-state valve) · "
                "cơ cấu chấp hành vi điện tử · khối lượng treo · màng composite "
                "bimetallic-silicon · điện cực ngoài / điện cực trong · fieldbus · tín hiệu "
                "tương tự 4 đến 20 mA · bộ định vị van · chip PID · cặp dây xoắn · an toàn "
                "nội tại (intrinsically safe) · ghép kênh / chia sẻ thời gian · thiết bị khóa "
                "khí nén · hệ thống điều khiển phân tán (DCS) · van thông minh · đồng hồ "
                "lưu lượng kiểu xoáy (vortex meter) · độ phạm vi lưu lượng · điểm đặt lưu "
                "lượng · điều khiển tầng (cascade control) · bộ điều chỉnh nạp khí "
                "(air-loaded regulator) · lỗ tiết lưu FO · bộ chuyển đổi I/P · TE / TIC · "
                "Wireless HART · ISA-100 · Ethernet không dây · vòng lặp kín “mềm” · độ "
                "trễ đo nhiệt độ")
    return ("<b>Key terms.</b> throttling control valve · perpetual motion · entropy · "
            "turbulent / laminar flow · solid-state valve · microelectronic actuator · "
            "suspended mass · bimetallic-silicon diaphragm · outer / inner electrode · "
            "fieldbus · analog 4 to 20 mA signal · valve positioner · PID chip · twisted "
            "pair · intrinsically safe · multiplex / time-share · pneumatic lockup device "
            "· distributed control system (DCS) · smart valve · vortex flow meter · "
            "rangeability · flow set point · cascade control · air-loaded regulator · "
            "fixed or variable orifice FO · I/P transducer · TE / TIC · Wireless HART · "
            "ISA-100 · wireless Ethernet · “soft” closed-loop control · temperature "
            "measurement lag")


def body_vi():
    b = []
    b.append(h2("Hệ thống bus tới giải cứu, hay tương lai sẽ mang lại gì",
                "The Bus System to the Rescue, or What the Future May Bring"))
    b.append(p("Van điều khiển thông thường (kiểu tiết lưu) có sẽ biến mất không? Không chắc. "
               "Hãy nhớ rằng ô tô đã không thay thế hoàn toàn xe đạp. Chúng ta khó lòng "
               "chấp nhận việc “lãng phí” năng lượng trong một van tiết lưu. Tuy nhiên, dù "
               "đã có những nỗ lực suốt nhiều thế kỷ nhằm chế tạo “chuyển động vĩnh cửu”, "
               "tức thiết bị hoạt động mà không “dùng” năng lượng (không chuyển năng lượng "
               "lên mức entropy cao hơn), chúng ta vẫn chưa tìm được thiết bị như vậy. "
               "Điều đó cũng đúng với việc điều khiển chất lưu trong đường ống. Các định "
               "luật cơ bản của vật lý vẫn tiếp tục áp dụng."))
    b.append(p("Người ta đã thử tìm cách điều khiển thanh lịch hơn. Ví dụ, bằng cách đặt dòng "
               "điện vào chất lưu [1], bạn có thể giảm lưu lượng thông qua thay đổi kiểu "
               "chảy rối hoặc chảy tầng (xem Hình 30-1). Cách này hoạt động như một đồng hồ "
               "lưu lượng từ tính chạy ngược, nhưng không phải là giải pháp thực tế. Đã có "
               "van vi điện tử để điều khiển lưu lượng nhỏ. Một thiết kế như vậy<sup>1</sup> "
               "dựa trên tương tác giữa một khối lượng treo và thân van để mở và đóng. Ở vị "
               "trí đóng, khối lượng treo nằm trực tiếp lên cổng ra trong thân van. Dời "
               "khối này đi sẽ mở van."))
    b.append(p("<small><sup>1</sup> Thiết kế này do IC Sensors chế tạo.</small>"))
    b.append(fig(1, FA.fig_f301()))
    b.append(p("Chuyển động của khối được thực hiện bằng cách thay đổi điện áp cấp cho màng "
               "làm bằng vật liệu composite bimetallic-silicon. Màng bao quanh khối treo để "
               "giữ nó. Màng gồm các điện trở khuếch tán vào một lớp silicon mỏng và được "
               "phủ một lớp nhôm. Khi điện áp được cấp vào các vật liệu kim loại, nhiệt độ "
               "của màng thay đổi và khối treo dịch chuyển tương ứng."))
    b.append(p("Khe hở giữa đế van và bề mặt ăn khớp có thể điều chỉnh tỷ lệ theo tín hiệu "
               "điện vào, cho phép điều khiển lưu lượng theo tỷ lệ cùng các chức năng thông "
               "thường của van là mở hoàn toàn hoặc đóng hoàn toàn. Van có thể điều khiển "
               "lưu lượng trong khoảng 0 đến 150 cc/min ở áp suất đầu vào từ 1 đến 50 psig."))
    b.append(p("Bơm điều chỉnh tốc độ đã được thử với thành công hạn chế. Vậy triển vọng "
               "tương lai thế nào?"))
    b.append(p("Điện tử vẫn sẽ mang lại những thay đổi quan trọng về cả phần mềm và phần "
               "cứng cơ cấu chấp hành. Tác động lớn nhất là việc dùng các chuẩn fieldbus, "
               "hiện đang dần thay thế tín hiệu tương tự 4 đến 20 mA bằng tín hiệu truyền "
               "thông số giữa bộ điều khiển hoặc máy tính với bộ định vị van. Lợi ích là "
               "tăng chức năng (xem Chương 9)."))
    b.append(fig(2, FA.fig_f302()))
    b.append(p("Một số bộ định vị đã có chip chức năng tỷ lệ – tích phân – vi phân (PID) và "
               "tự thực hiện toàn bộ việc điều khiển dựa trên tín hiệu cảm biến qua fieldbus. "
               "Điều này giảm chi phí dây dẫn (một cặp dây xoắn nối mọi thứ; xem Hình 30-2) "
               "và đơn giản hóa truyền dữ liệu với ít nhiễu hơn, độ chính xác cao hơn. Đồng "
               "thời, fieldbus có thể gửi dữ liệu quan trọng trở lại máy tính, ví dụ vị trí "
               "van. Có thể nhúng thêm cảm biến vào bộ định vị để báo cáo rò rỉ đế van, ma "
               "sát đệm thân van, ma sát cơ cấu chấp hành, rò khí trong cơ cấu chấp hành, v.v. "
               "Tuy nhiên, tôi xin thương người vận hành phải bị choáng ngợp khi theo dõi "
               "khoảng 10 kênh dữ liệu liên tục cho mỗi van trong một nhà máy thông thường "
               "có 500 vòng điều khiển! Vì vậy, việc dùng có chọn lọc tùy chọn này là đương "
               "nhiên. Chẳng hạn, biết băng chết của van cao hơn bình thường có thể giải "
               "thích sự mất ổn định đột ngột của vòng điều khiển và kích hoạt bảo trì phòng "
               "ngừa. Biết được rò rỉ ở cụm đệm thân van có thể tránh được sự cố tràn nguy hiểm."))
    b.append(p("Vấn đề nghiêm trọng hơn là lượng dòng điện mà fieldbus có thể mang mà không "
               "mất nhãn “an toàn nội tại”. Dĩ nhiên, dòng thấp hơn nghĩa là ít bộ định vị "
               "hơn trên đường dây. Giải pháp là ghép kênh (chia sẻ thời gian), để chỉ một "
               "bộ định vị trong vòng nhận thay đổi tín hiệu tại một thời điểm. Điều này "
               "cần một thiết bị nhớ hoặc thiết bị khóa khí nén giữ bộ định vị ở vị trí hiện "
               "tại cho đến lần “bật” tiếp theo, và lần lượt có thể làm tốc độ di chuyển của "
               "van chậm lại đến mức không còn phù hợp cho điều khiển lưu lượng hoặc áp "
               "suất. Đây chỉ là một trong số nhiều vấn đề cần giải quyết trước khi hệ "
               "thống fieldbus được chấp nhận rộng rãi."))
    b.append(p("Giải pháp khả dĩ nhất là dùng cáp riêng để cấp điện cho các thiết bị chấp "
               "hành tại chỗ. Điều này đương nhiên làm mất đi một phần lợi ích của fieldbus, "
               "cụ thể là tiết kiệm cáp tới từng thiết bị. Tuy nhiên, vẫn có một mục tiêu "
               "cơ bản có thể đạt được: kết nối tất cả thành phần vòng điều khiển tại chỗ "
               "như cảm biến, bộ điều khiển và van thành một hệ thống làm việc độc lập "
               "(hệ thống điều khiển phân tán) chỉ được nối tới mạng máy tính trung tâm để "
               "giám sát và ghi dữ liệu. Kết quả là tiết kiệm lớn về cáp và về lượng dữ "
               "liệu được truyền."))
    b.append(h3("Van thông minh", "Smart valves"))
    b.append(p("Mặt khác, van thông minh sẽ có tương lai. Rắc rối là thế nào là van thông "
               "minh? Định nghĩa tôi ưa dùng là “đỉnh cao của điều khiển phân tán”. Trước "
               "hết, phải nhận ra rằng mọi van điều khiển đều điều khiển tốc độ dòng chảy "
               "đi qua nó. Không gì khác. Sự khác biệt giữa van điều khiển mức và van điều "
               "khiển áp suất nằm ở chỗ cái đầu dùng cảm biến mức thay vì cảm biến áp suất. "
               "Nếu cũng chính van đó, với cùng dòng chảy, nằm trong vòng mà phản hồi đến "
               "từ cảm biến nhiệt độ, thì ta có van điều khiển nhiệt độ."))
    b.append(p("Khi đã nhận ra mỗi van chỉ điều khiển tốc độ dòng chảy, ta có thể đi thêm "
               "một bước và tạo hệ thống điều khiển lưu lượng vòng kín lấy van làm trung "
               "tâm. Nhìn Hình 30-3, một đồng hồ lưu lượng — tốt nhất là đồng hồ kiểu xoáy "
               "(vì độ phạm vi và dải ứng dụng rộng, kể cả hơi) — được gắn ở đầu vào van "
               "(điểm có ít nhiễu loạn nhất). Bộ điều khiển lưu lượng hoặc gắn vào đồng hồ, "
               "hoặc trở thành một phần của bộ định vị I/P, trong khi điểm đặt lưu lượng do "
               "bộ điều khiển quy trình chính hoặc máy tính đưa ra (thể hiện như một phần "
               "của hệ thống điều khiển nhiệt độ). Máy tính đặt lưu lượng để đạt nhiệt độ "
               "được điều khiển cuối cùng. Chừng nào hệ thống không có nhiễu loạn, mọi thứ "
               "đều ổn. Nhưng giả sử môi trường gia nhiệt đi qua van là hơi và, vì nhu cầu "
               "ở nơi khác, áp suất đầu vào giảm 10%. Với dòng tới hạn, điều này có thể "
               "làm lưu lượng hơi giảm đột ngột 10%. Trong hệ thống nhiệt độ thông thường, "
               "có thể mất vài phút<sup>2</sup> để nhiệt độ được điều khiển bắt đầu giảm và "
               "để máy tính phản ứng mở van thêm. Điều đó gây xáo trộn nhiệt độ."))
    b.append(p("<small><sup>2</sup> Ví dụ, độ trễ đo nhiệt độ của bầu cảm biến 1/2 inch trong "
               "giếng nhiệt khi đo chất lỏng nặng ở vận tốc thấp có thể từ 60 đến 180 giây.</small>"))
    b.append(p("Để biết các dạng điều khiển lưu lượng tiên tiến hơn, xem Chương 6, “High-Recovery "
               "Valves.”"))
    b.append(fig(3, FB.fig_f303()))
    b.append(p("Với van thông minh, mặt khác, đồng hồ lưu lượng sẽ cảm nhận ngay sự thay đổi "
               "lưu lượng, làm van tăng hành trình và khôi phục lưu lượng trước khi các hiệu "
               "ứng nhiệt động chậm chạp kịp biểu hiện ở phía hạ lưu. Nhờ vậy nhiệt độ giữ "
               "ở điểm đặt và máy tính có lẽ không bao giờ phát hiện sự xáo trộn áp suất "
               "hơi. Đây đương nhiên là một dạng điều khiển tầng (cascade), chỉ khác là các "
               "phần lớn của vòng nay nằm gọn trong một cụm thiết bị. Dù có thêm chi phí (và "
               "có thể thêm dây), vẫn có lý do chính đáng để dùng van thông minh như vậy "
               "trong các vòng quan trọng, nơi van có thể hấp thụ nhiễu loạn quy trình "
               "trước khi nó ảnh hưởng đến biến được điều khiển cuối cùng."))
    b.append(p("Một ý ưa thích khác của tôi và một số người là hồi sinh bộ điều chỉnh áp suất "
               "tốt ngày xưa với đáp ứng tần số xuất sắc và dải lưu lượng rộng. Dùng hệ "
               "thống điều khiển nhiệt độ tương tự như đã mô tả, bộ điều chỉnh trong Hình "
               "30-4 có thể có áp suất đặt do tín hiệu khí từ bộ chuyển đổi I/P nhận tín "
               "hiệu từ bộ điều khiển nhiệt độ (xem sơ đồ vòng). Bộ điều chỉnh này điều "
               "khiển áp suất của chất lưu trao đổi nhiệt, chẳng hạn dầu hoặc hơi, trước "
               "lỗ tiết lưu cố định (FO) hoặc bộ tiết lưu điều chỉnh được. Với kích thước "
               "đúng, sự kết hợp giữa diện tích lỗ và áp suất trước lỗ sẽ điều khiển hiệu "
               "quả tốc độ dòng chảy (và do đó là Btu) tới bộ trao đổi nhiệt. Mọi nhu cầu "
               "tăng nhiệt độ được đáp ứng bằng cách bộ điều khiển tăng tín hiệu tới I/P, "
               "lại tăng tải khí bên dưới màng cơ cấu chấp hành và làm van mở. Điều này "
               "tăng độ giảm áp qua lỗ và lưu lượng chất gia nhiệt. Mọi nhiễu loạn tại chỗ, "
               "chẳng hạn giảm đột ngột áp suất cấp, nay được màng van cảm nhận, dẫn đến "
               "hiệu chỉnh gần như tức thì mà cảm biến nhiệt độ (TE) tại bộ trao đổi nhiệt "
               "không hề nhận ra. Ta có một van thông minh với đặc tính hiệu năng gần như "
               "giống Hình 30-3, nhưng chỉ với một phần nhỏ chi phí."))
    b.append(fig(4, FB.fig_f304()))
    b.append(h3("Ethernet không dây", "Wireless Ethernet"))
    b.append(p("Chuẩn không dây ISA-100 hiện đang được xây dựng và chuẩn Wireless HART đã "
               "công bố sẽ giúp người dùng dễ dàng chuyển mạng nối tiếp sang truyền thông "
               "Ethernet. Điều này mang lại chu kỳ thăm dò nhanh hơn và, đương nhiên, loại "
               "bỏ được nhiều dây dẫn."))
    b.append(p("Các vấn đề cần giải là an ninh, nhiễu có thể xảy ra và tiếng ồn. Thiết bị "
               "truyền thông không dây cũng cần nguồn điện — ví dụ pin. Khoảng cách cũng là "
               "vấn đề (tối đa 20 dặm giữa bộ phát và bộ thu). Chính vì những lý do này và "
               "một số lý do khác, việc dùng hệ thống không dây ban đầu sẽ bị giới hạn ở "
               "truyền dữ liệu và điều khiển vòng hở hoặc vòng kín “mềm”."))
    b.append(refs(_REFS))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm bảy trang in (175–181; trang in "
                  "= trang PDF + 6), có bốn hình, một chú thích cuối trang và một tài liệu "
                  "tham khảo; không có bảng hay phương trình. Bốn hình được vẽ lại dưới dạng "
                  "vector từ các trang in, đơn giản hóa nhưng giữ nguyên cấu trúc và nhãn. "
                  "Các giá trị gốc (4 đến 20 mA, 0 đến 150 cc/min, 1 đến 50 psig, 10 kênh "
                  "dữ liệu, 500 vòng, giảm 10%, 1/2 inch, 60 đến 180 giây, 20 dặm) được "
                  "giữ nguyên."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © 2011 Hans D. Baumann, do ISA / John Wiley &amp; Sons xuất bản.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("The Bus System to the Rescue, or What the Future May Bring",
                "The Bus System to the Rescue, or What the Future May Bring"))
    b.append(p("Will the conventional (throttling-type) control valve cease to exist? Not "
               "likely. Remember, the automobile did not completely replace the bicycle. "
               "It goes against our grain to “waste” energy in a throttling valve. However, "
               "despite attempts over the centuries to invent “perpetual motion,” that is, "
               "a device that works without “using” energy (converting energy to a higher "
               "entropy level), we have found none. The same is true for the control of "
               "fluids in a pipe. The basic laws of physics still apply."))
    b.append(p("Attempts have been made to obtain control more elegantly. For example, by "
               "applying electric current to a fluid [1], you can reduce the flowing "
               "quantity by changing the turbulent or laminar flow pattern (see Figure "
               "30-1). This works like a magnetic flow meter in reverse; however, it is not "
               "a practical approach. Microelectronic valves are available to control "
               "small flows. One such design<sup>1</sup> relies on the interaction of a "
               "suspended mass with a valve body to open and close. In the closed position, "
               "the suspended mass is seated directly over an outlet port in the valve "
               "body. Displacement of this mass opens the valve."))
    b.append(p("<small><sup>1</sup> This design is manufactured by IC Sensors.</small>"))
    b.append(fig(1, FA.fig_f301()))
    b.append(p("The displacement is achieved by changing the electric voltage supplied to "
               "a diaphragm made of a bimetallic-silicon composite. The diaphragm surrounds "
               "the suspended mass to provide suspension. It is made up of resistors "
               "diffused into a thin layer of silicon and covered by a layer of aluminum. "
               "When an electric voltage is supplied to the metallic materials, it affects "
               "a change in the temperature of the diaphragm and a corresponding "
               "displacement of the suspended mass."))
    b.append(p("The gap between the valve seat and its mating surface can be adjusted in "
               "proportion to the electrical input, which enables proportional control of "
               "flow and the usual fully open or fully closed functions of a valve. The "
               "valve can control flow rates in the range of 0 to 150 cc/min at input "
               "pressures between 1 and 50 psig."))
    b.append(p("Speed-controlled pumps have been tried with limited success. So, what is "
               "the outlook for the future?"))
    b.append(p("Electronics will still bring us important changes as far as actuating "
               "software and hardware are concerned. The biggest impact has been the use "
               "of fieldbus standards that now tend to replace the current analog 4 to 20 "
               "mA signal with a digital communication signal between the controller or "
               "computer and the valve positioner. The benefit is increased functionality "
               "(see Chapter 9)."))
    b.append(fig(2, FA.fig_f302()))
    b.append(p("Some positioners already have a proportional, integral, and derivative "
               "(PID) function chip and do all the control based on the sensor input via "
               "the fieldbus. This reduces hardwiring costs (a single pair of twisted wire "
               "connects everything; see Figure 30-2) and offers simplified data transfer "
               "with less noise and increased accuracy. At the same time, the fieldbus can "
               "transmit important data back to the computer regarding the valve position, "
               "for example. Other sensors could be embedded in a positioner to inform "
               "about seat leakage, stem packing friction, actuator friction, air leakage "
               "in the actuator, and so on. However, I pity the poor operator who must be "
               "absolutely overwhelmed by monitoring perhaps 10 continuous data input "
               "channels per valve in a typical process plant having 500 individual loops! "
               "So, selective use of this option is certainly in order. Being informed of "
               "a higher-than-usual valve deadband could explain sudden loop instability "
               "and may trigger preventive maintenance, for example. Being aware of the "
               "stem package leakage could avoid dangerous spills."))
    b.append(p("More serious problems exist with the amount of electric current a fieldbus "
               "can handle without losing its “intrinsically safe” label. Of course, a low "
               "current means fewer valve positioners on the line. The solution is to "
               "multiplex (time-share) so that only one positioner in the loop receives a "
               "signal change at any given time. This will require a memory device or "
               "pneumatic lockup device to freeze the valve positioner until the next "
               "“switch on,” which in turn might slow down the valve travel speed to a "
               "level that may be unsuitable for flow or pressure control. This is one "
               "example of several problems that must be addressed prior to the wide "
               "acceptance of the fieldbus system."))
    b.append(p("The likely solution would be to have separate cables to supply electric "
               "power to local actuating devices. This, of course, negates some of the "
               "advantages of having a fieldbus system, namely, savings in cable lines to "
               "individual components. Nevertheless, there is a basic goal that can be "
               "reached, that is, tie in all local loop components such as sensors, "
               "controllers, and valves into an independent local working system "
               "(distributed control system) to be connected only for purposes of "
               "supervisory control and data logging to a central computer network. This "
               "will result in major cost savings in cabling as well as in the amount of "
               "data being transmitted."))
    b.append(h3("Smart valves", "Smart valves"))
    b.append(p("Smart valves, on the other hand, will have a future. The trouble is, what is "
               "a smart valve? My preferred definition is the “ultimate in distributed "
               "control.” First, you have to realize that every control valve controls the "
               "rate of flow passing through it. Nothing else. The difference between a "
               "level control valve and a pressure control valve is determined by the fact "
               "that the first one employs a level transmitter instead of a pressure "
               "transmitter. If the identical valve handling the same flow is in a loop "
               "where the feedback comes from a temperature transmitter, then we have a "
               "temperature control valve."))
    b.append(p("Once we realize that each valve controls only the rate of flow, we can go a "
               "step further and create a closed-loop flow control system with the valve "
               "as its centerpiece. Referring to Figure 30-3, a flow meter, preferably a "
               "vortex meter (for rangeability and a wide range of applications, including "
               "steam), is attached to the valve inlet (point of lowest turbulence). A flow "
               "controller is either attached to the flow meter or is made part of the I/P "
               "positioner, while the set point for the flow controller is given by the "
               "main process controller or computer (shown as part of a temperature control "
               "system). The computer sets the flow rate to achieve the ultimate controlled "
               "temperature. As long as there is no disturbance in the system, everything "
               "will be fine. However, assume the heating medium passing the valve is "
               "steam, and, because of demand elsewhere, the inlet pressure drops by 10%. "
               "This can cause a sudden reduction in the steam flow rate by 10%, assuming "
               "choked flow. In a conventional temperature system, it may take several "
               "minutes<sup>2</sup> for the controlled temperature to begin to drop and for "
               "the computer to react and open the valve farther. This leads to an upset in "
               "the controlled temperature."))
    b.append(p("<small><sup>2</sup> For example, the temperature measurement lag of a 1/2-inch "
               "bulb thermal well sensing a heavy liquid at low velocities can vary between "
               "60 and 180 s.</small>"))
    b.append(p("For more advanced types of flow control, see Chapter 6, “High-Recovery "
               "Valves.”"))
    b.append(fig(3, FB.fig_f303()))
    b.append(p("With the smart valve, on the other hand, the flow meter will sense the "
               "change in flow immediately, will make the valve increase the travel, and "
               "will restore the flow before the usually slow thermodynamic effects make "
               "themselves felt downstream. Thus, the temperature stays at the set point, "
               "and the computer probably never even detects the upset in steam pressure. "
               "This is, of course, a form of cascade control, except good portions of the "
               "loop are now in a tidy, compact package. Despite the added cost (and "
               "perhaps added wiring), a case can be made to use such a smart valve in "
               "critical loops where the valve can absorb process disturbances before they "
               "can affect the ultimate controlled variable."))
    b.append(p("Another favorite of mine, and a few others, is to resurrect the good old "
               "pressure regulator with its excellent frequency response and high flow "
               "range. Using a temperature control system similar to that described above, "
               "the regulator shown in Figure 30-4 can have a set pressure determined by "
               "the air signal from an I/P transducer signal coming from a temperature "
               "controller (see loop diagram). This regulator controls the pressure of a "
               "heat exchange fluid, such as oil or steam, ahead of an orifice (FO) or an "
               "adjustable restrictor. Sized correctly, the combination orifice area and "
               "pressure ahead of the orifice will effectively control the rate of flow "
               "(and, therefore, Btu) to the heat exchanger. Any demand for an increase in "
               "temperature is met by the controller increasing the signal to the I/P "
               "transducer, which, in turn, increases the air load below the actuator "
               "diaphragm and causes the valve to open. This increases the pressure drop "
               "across the orifice and the flow of heating fluid. Any local disturbance, "
               "such as a sudden decrease in supply pressure, is now sensed by the valve "
               "diaphragm, which leads to a nearly instantaneous correction without the "
               "disturbance being noticed by the temperature transmitter (TE) at the heat "
               "exchanger. We have a smart valve with nearly the same performance "
               "characteristics as those in Figure 30-3, but at a fraction of the cost."))
    b.append(fig(4, FB.fig_f304()))
    b.append(h3("Wireless Ethernet", "Wireless Ethernet"))
    b.append(p("The ISA-100 wireless standard currently being developed and the already "
               "published wireless HART standard will make it easier for the user to "
               "convert serial networks to Ethernet communication. This will offer faster "
               "polling cycles and, of course, eliminate a lot of wiring."))
    b.append(p("Problems to be solved are security, possible interference, and noise. "
               "Wireless communication devices also need power—batteries, for example. "
               "Distance is also a problem (20 miles maximum between sender and receiver). "
               "It is for these and other reasons that the initial use of wireless systems "
               "will be restricted to data transmission and open-loop or “soft” closed-loop "
               "control systems."))
    b.append(refs(_REFS))
    b.append(note("<b>Source quirks.</b> The chapter spans seven printed pages (175–181; "
                  "printed = PDF + 6), with four figures, one endnote and one reference; no "
                  "tables or equations. The four figures were redrawn as vectors from the "
                  "printed pages, simplified but keeping their topology and callouts. "
                  "Original values are retained: 4 to 20 mA, 0 to 150 cc/min, 1 to 50 "
                  "psig, 10 data channels, 500 loops, a 10% pressure drop, 1/2 inch, 60 and "
                  "180 s, and 20 miles."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 2011 Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)
