# -*- coding: utf-8 -*-
"""Book 7, Chapter 11, Section B - The Valve Is Unstable (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), the final prose
sections "The Valve Is Unstable", the stiffness-equation summary, References,
Additional Reading, source notes and the about-the-source block, printed
pp. 85-90 (PDF pp. 89-94), source lines 2611-2775 of work/cvp_raw.txt. Figures
11-2 and 11-3 are redrawn in cvpfig11.py. The integration module supplies the
title, byline, glossary and page shell.
"""
from cvp_common import eq, fig, h2, h3, note, p, refs, ul
import cvpfig11 as F


def body_vi():
    b = []
    b.append(h2("Van không ổn định", "The Valve Is Unstable"))
    b.append(p("Sự mất ổn định do các lực chất lỏng động (dynamic fluid forces) "
               "tác dụng lên nút van, đĩa van hoặc bi van không nên nhầm lẫn với "
               "sự mất ổn định của bộ định vị hoặc của vòng điều khiển (đôi khi "
               "rất khó phân biệt). Như ví dụ trước đã cho thấy, các lực tác dụng "
               "lên nút van hoặc qua van bướm (và nói chung là qua nút van quay) "
               "có thể thay đổi dữ dội theo điều kiện dòng chảy. Đã có nhiều bài "
               "viết về chủ đề này [4], hầu hết bắt bạn phải trở thành chuyên gia "
               "toán học! Vì vậy, tôi sẽ cố giữ cho vấn đề được đơn giản."))
    b.append(p("Để bộ lót van (valve trim) ổn định, độ thay đổi của lực thân van "
               "trên mỗi inch chuyển động của thân van phải nhỏ hơn độ thay đổi "
               "của lực thân van trên mỗi inch hành trình do bộ truyền động tạo "
               "ra. Cái sau được gọi là hệ số độ cứng Kn của bộ truyền động, được "
               "biểu thị bằng in-lb/in. Đối với bộ truyền động màng lò xo "
               "(spring-diaphragm), đây đơn giản là tốc độ của lò xo bộ truyền "
               "động (hoặc tổng hợp của tất cả các lò xo nếu là loại nhiều lò "
               "xo), bỏ qua giảm chấn khí nén (pneumatic damping)."))
    b.append(p("Với bộ truyền động piston, mọi thứ phức tạp hơn một chút. Ở đây, "
               "lực sinh ra khi nén áp suất khí bên trong bộ truyền động do "
               "piston dịch chuyển qua một quãng nhất định chính là thứ quyết "
               "định độ cứng. Rõ ràng, lực này thay đổi theo vị trí thân van, "
               "thể tích xi lăng ban đầu (L) và áp suất khí tuyệt đối. Theo quy "
               "tắc chung, bộ truyền động piston cứng hơn nhiều [5] so với bộ "
               "truyền động màng lò xo và, vì thế, có thể vận hành van cầu một "
               "đế theo chiều dòng chảy làm đóng (flow-to-close) — điều mà bộ "
               "truyền động màng lò xo thông thường không làm được."))
    b.append(p("Thói quen chung là lắp van cầu một đế theo chiều dòng chảy làm "
               "mở (flow-to-open), nơi vấn đề mất ổn định động hiếm khi phát "
               "sinh. Tuy nhiên, vấn đề có thể xuất hiện ở van lồng cân bằng lực "
               "(force-balanced cage valves) và van góc (angle valves) xử lý "
               "chất lỏng xâm thực (cavitating) hoặc hóa hơi (flashing), khi "
               "dòng chảy thoát ra phía sau nút van (dòng có xu hướng làm đóng). "
               "Điều xảy ra là không chỉ diện tích hiệu dụng của nút van tăng "
               "lên khi tiến gần vị trí tựa, mà áp suất phía sau còn giảm nhanh, "
               "xấp xỉ theo bình phương của mức giảm lưu lượng. Tất cả chúng ta "
               "đều đã trải nghiệm hiện tượng này trong bồn tắm: khi nước còn "
               "trong bồn, ta từ từ buông dây xích, nút cao su tiến về phía lỗ "
               "thoát, nhưng ở khoảng 3/16 in cách đế van thì nút đột ngột lao "
               "xuống và đập mạnh vào mặt tựa. Chuyện tương tự xảy ra trong van. "
               "Bí quyết là phải có bộ truyền động đủ cứng để giữ nút van đúng "
               "vị trí."))
    b.append(p("Theo quy tắc kinh nghiệm, hãy coi diện tích nút van mất cân bằng "
               "(off-balance plug area) tăng từ không đến cực đại trong một "
               "quãng bằng giá trị nhỏ hơn của 1/3 hành trình van hoặc 1/4 "
               "đường kính lỗ tiết lưu. Hơn nữa, hãy giả định chênh áp tăng từ "
               "P1 − P2 ở lưu lượng bình thường lên P1 cực đại trong cùng quãng "
               "đó."))
    b.append(p("Dưới đây là một ví dụ: van góc 3 in với lỗ tiết lưu đường kính "
               "2,5 in có thân van đường kính 1/2 in. P1 bình thường = 165 psig; "
               "P2 bình thường = 125 psig; P1 cực đại = 175 psig; hành trình "
               "bộ truyền động theo chiều dòng chảy làm đóng = 1,5 in. Vì diện "
               "tích của thân van tương đối nhỏ, ta có thể bỏ qua và lấy diện "
               "tích nút van mất cân bằng của lỗ tiết lưu 2,5 in, tức 4,9 in²."))
    b.append(p("Trước hết, xét quãng thay đổi diện tích: 1/3 của 1,5 in hành "
               "trình = 0,5 in; 1/4 của 2,5 in đường kính lỗ tiết lưu = 0,625 "
               "in; do đó ta chọn 0,50 in vì nó nhỏ hơn. Tốc độ thay đổi lực "
               "thân van khi đó là"))
    b.append(eq("1/3 × 1,5 in = 0,5 in;   1/4 × 2,5 in = 0,625 in;   chọn 0,50 in", ""))
    b.append(eq("Diện tích mất cân bằng × ΔP thay đổi / Quãng đường", "11-1"))
    b.append(p("trong đó"))
    b.append(eq("ΔP thay đổi = P1 cực đại − ΔP = 175 − (165 − 125) = 135 psi", ""))
    b.append(p("Vì vậy, theo Phương trình 11-1, 4,9 in² × 135 psi / 0,50 in = "
               "1323 lb/in."))
    b.append(eq("4,9 in² × 135 psi / 0,50 in = 1323 lb/in", ""))
    b.append(p("Giả sử bộ truyền động là màng lò xo có diện tích 100 in² và dải "
               "bench 3 đến 15 psi, tốc độ lò xo sẽ là (15 − 3 psi) × 100 in² / "
               "1,5 in hành trình = 800 lb/in."))
    b.append(eq("(15 − 3 psi) × 100 in² / 1,5 in = 800 lb/in", ""))
    b.append(p("Con số này hoàn toàn không đủ, và ta phải hoặc đề xuất bộ truyền "
               "động 175 in², hoặc đổi dải bench của lò xo (hoặc các lò xo) sang "
               "6 đến 30 psi."))
    b.append(eq("(30 − 6 psi) × 100 in² / 1,5 in = 1600 lb/in", ""))
    b.append(p("Điều này nâng độ cứng của bộ truyền động lên 1600 lb/in, đủ biên "
               "an toàn. Việc nén khí bên trong bộ truyền động sẽ làm tăng độ "
               "cứng và vì thế tạo thêm một hệ số an toàn, dù độ cứng đó nhỏ hơn "
               "nhiều so với bộ truyền động xi lăng vì thể tích khí lớn hơn."))
    b.append(p("Các van điều khiển quay (rotary) cũng gặp vấn đề độ cứng tương "
               "tự. Chúng phức tạp hơn vì ta phải xử lý mô-men xoắn thay vì lực. "
               "Hãy xét đặc tính mô-men xoắn tổng hợp của van bướm (cho trong "
               "Hình 11-2, lấy từ Hình 4 trong Tài liệu tham khảo 6). Ở đây, sự "
               "thay đổi mô-men xoắn lớn nhất cho mỗi độ xảy ra tại 60°, khi "
               "mô-men xoắn tổng hợp thay đổi với tốc độ (0,011 in-lb / d³ psi) "
               "× P1 cho hành trình ±5°, tức từ 0,064 ở 55° đến 0,075 ở 65°. "
               "Giả sử ta có van 10 in với chênh áp cực đại (khi van đóng) là "
               "87 psig. Ta có sự thay đổi mô-men xoắn tại độ mở 60° (và giả "
               "sử van phải mở trên 60° để cho qua lưu lượng cực đại) là "
               "0,011 in-lb × 10 in³ × 87 psi = 960 in-lb cho mỗi 10°."))
    b.append(eq("(0,011 in-lb/d³ psi) × 10 in³ × 87 psi = 960 in-lb cho mỗi 10°", ""))
    b.append(fig(2, F.fig_f112()))

    b.append(p("Giả sử ta có bộ truyền động xi lăng với diện tích 75 in² chuyển "
               "động 4 in để đưa cánh (vane) từ độ mở 0° sang 90°. Bỏ qua ảnh "
               "hưởng cosin góc, ta có thể giả định ở độ mở 65°, hành trình "
               "piston là (4 in / 90°) × 65° = 2,88 in, và ở cánh 55°, hành "
               "trình = (4 in / 90°) × 55° = 2,44 in."))
    b.append(eq("(4 in / 90°) × 65° = 2,88 in;   (4 in / 90°) × 55° = 2,44 in", ""))
    b.append(p("Điều cần biết là sự thay đổi thể tích nếu bộ truyền động đi từ "
               "2,44 đến 2,88 in hành trình piston và giả sử có 0,3 in hành "
               "trình vượt (overtravel) trong xi lăng. Hãy tính tỷ số thể tích "
               "không khí giữa hai vị trí hành trình:"))
    b.append(eq("Tỷ số thể tích = A(hi + ho + Δh)/A(hi + ho)", ""))
    b.append(p("Do đó,"))
    b.append(eq("75 in²(2,88 in + 0,3 in) / 75 in²(2,44 in + 0,3 in) = "
                "239 in³ / 206 in³ = 1,16", ""))
    b.append(p("Giả sử thêm rằng áp suất đầu ra của bộ định vị trong xi lăng ở "
               "hành trình 65° là 65 psia, giờ ta có thể tính sự thay đổi lực do "
               "nén khí khi bộ truyền động đột ngột đi từ 65° xuống 55° vì ảnh "
               "hưởng của mô-men động (nhớ rằng ở hầu hết van quay, mô-men có "
               "xu hướng làm van đóng)."))
    b.append(eq("Thay đổi lực bộ truyền động = (Tỷ số thể tích − 1) × Diện tích "
                "× Áp suất khí (10 − 2) = (1,16 − 1) × 75 in² × 65 psia = 780 lb", ""))
    b.append(p("Việc còn lại là đổi lực này sang mô-men xoắn. Vì hành trình là "
               "4 in khi quay 90°, ta có thể coi chiều dài hiệu dụng của cánh "
               "tay làm quay trục bằng hành trình bộ truyền động / 2 × tan 45° "
               "= 4/(2 × 1) = 2,00 in."))
    b.append(eq("hành trình bộ truyền động / 2 × tan 45° = 4/(2 × 1) = 2,00 in", ""))
    b.append(p("Như vậy, sự thay đổi lực 780 lb cho sự thay đổi mô-men xoắn là "
               "780 lb × 2 in = 1560 in-lb cho mỗi 10° hành trình. Giá trị này "
               "cao hơn sự thay đổi mô-men cánh động 960 in-lb / 10°, nên ta có "
               "thể kỳ vọng vận hành ổn định, vì ma sát phớt piston tạo thêm "
               "lực cản với sự thay đổi đột ngột."))
    b.append(eq("780 lb × 2 in = 1560 in-lb cho mỗi 10° hành trình", ""))
    b.append(fig(3, F.fig_f113()))

    b.append(p("Nếu đây là bộ truyền động màng lò xo với cùng hành trình 4 in, "
               "yêu cầu mô-men xoắn 960 in-lb cho mỗi 10° hành trình cánh sẽ đòi "
               "hỏi 960 in-lb / 2 in cánh tay hiệu dụng = 480 lb thay đổi lực "
               "cho mỗi 0,44 in hành trình bộ truyền động và, vì vậy, cần tốc độ "
               "lò xo 480 lb / 0,44 in = 1091 lb/in."))
    b.append(eq("960 in-lb / 2 in = 480 lb cho 0,44 in;   480 lb / 0,44 in = "
                "1091 lb/in", ""))
    b.append(p("Bỏ qua độ cứng tăng thêm do nén khí, điều này tương đương với bộ "
               "truyền động 180 in² với dải bench 6 đến 30 psi — một sự tăng "
               "kích thước bộ truyền động rất lớn."))
    b.append(p("Ví dụ trên giả định cánh thông thường (conventional vane); các "
               "cánh mô-men thấp (low-torque vanes) sẽ giảm yêu cầu độ cứng và "
               "vì thế cho phép dùng bộ truyền động màng lò xo dù hệ số độ cứng "
               "của chúng thấp hơn. Lưu ý: độ mở 60° với cánh mô-men thấp có góc "
               "đệm tựa 15° xảy ra ở hành trình cánh 45° (xem Hình 11-2)."))
    b.append(note("<b>Lưu ý.</b> Nguồn in «15-inch angle-seating»; bản dịch trình "
                  "bày là 15° theo đúng ý định."))
    b.append(p("Sau đây là tóm tắt các phương trình độ cứng [8]."))
    b.append(ul([
        "Bộ truyền động màng lò xo (bỏ qua độ cứng nhỏ hơn do nén khí<sup>5</sup>):"
        + eq("Kn = (Diện tích màng × Dải tín hiệu)/Hành trình lb/in", ""),
        "Bộ truyền động xi lăng (tác động đơn):"
        + eq("Kn = {[A<sub>C</sub>(h<sub>i</sub> + h<sub>o</sub> + Δh)/"
             "A<sub>C</sub>(h<sub>i</sub> + h<sub>o</sub>)] − 1} × S × "
             "A<sub>C</sub>/Δh lb/in", "")
        + "<p>trong đó A<sub>C</sub> = diện tích hiệu dụng của xi lăng, in²; "
          "h<sub>i</sub> = vị trí hành trình ban đầu, in; h<sub>o</sub> = hành "
          "trình vượt của piston (hành trình không dùng), in; S = áp suất tín "
          "hiệu tại vị trí hành trình đã cho, psia; Δh = thay đổi hành trình do "
          "nhiễu loạn, in.</p>",
        "Bộ truyền động xi lăng (tác động kép). Kết quả bằng bộ truyền động xi "
        "lăng tác động đơn nhân đôi.",
    ]))
    b.append(note("<b>Chú thích 5.</b> Giả định là đẳng nhiệt (isothermal)."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "H. D. Baumann, “How Do Control Valves Close?” Valve World magazine "
        "(April 2020): 78–79.",
        "N. Jeschke, et al., “Untersuchungen der Stopfbuchse Reibung an "
        "Stellventile Mit Pneumatischer Membranantrieb,” RTP, Volume 3. West "
        "Germany (1968).",
        "H. D. Baumann, “The Need for Pneumatic Power Signals for Control "
        "Valves,” InTech (January 1988): 34–41.",
        "G. A. Keith, “Analytical Prediction of Valve Stability,” ISA Paper "
        "838-70 (Research Triangle Park, NC: ISA, 1970).",
        "P. J. Schafbuch, “Fluid Inertia Effects on Unbalanced Valve Stability,” "
        "ISA Paper 85-0207 (Research Triangle Park, NC: ISA, 1983).",
        "H. D. Baumann, “Preventing Dynamic Instability of Rotary Valves,” Valve "
        "World magazine (October 2020).",
        "Paul J. Schafbuch, “Fluid Inertia Effects on Unbalanced Valve Stability,” "
        "Proceedings of the ISA Final Control Elements Symposium, April 1985, "
        "New Orleans, LA. Paper no. 85-207, 32–48.",
        "ISA-TR75.24.01-2017 draft, Liner and Pneumatic Actuator Sizing and "
        "Selection (Research Triangle Park, NC: ISA [International Society of "
        "Automation]).",
    ]))

    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "H. D. Baumann, “A Case for Butterfly Valves in Throttling Applications,” "
        "Instruments and Control Systems (May 1979): 35–38.",
    ]))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR có nhiều dấu gạch "
                  "nối khi xuống dòng; các từ đó được ghép lại thành từ hoàn "
                  "chỉnh. Ký hiệu «P 1» bị tách khoảng được chuẩn hóa thành P1, "
                  "và các mảnh OCR như «2 2 π/4» và «2.0632 π/4» được trình bày "
                  "là (2²π/4) và (2.063²π/4). (2) Ở công thức Tỷ số thể tích, "
                  "nguồn thiếu dấu ngoặc ở mẫu số; bản dịch trình bày nhất quán "
                  "là A(hi+ho+Δh)/A(hi+ho). (3) Biểu thức cánh tay đòn trong "
                  "nguồn là «4/(2 × l)»; bản dịch xử lý là 4/(2 × 1). (4) Chú "
                  "thích hình in «toque» (lỗi chính tả) và «15-inch "
                  "angle-seating»; bản dịch dùng mô-men xoắn và 15° và đã ghi "
                  "chú lỗi này. (5) Các hình 11-1 đến 11-3 được vẽ lại dạng "
                  "vector đã đơn giản hóa; Hình 11-1 là bản rút gọn của mẫu ISA, "
                  "không phải bản sao facsimile. (6) Toàn chương chiếm các trang "
                  "in 81–90 (PDF tr. 85–94); tiêu đề tài liệu tham khảo 8 được "
                  "giữ nguyên theo bản in."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Phần văn bản kết thúc này của Chương 11 chiếm các trang in 85–90 "
               "của ấn bản in (PDF tr. 89–94); toàn chương trải dài từ tr. 81–90 "
               "(PDF tr. 85–94). Các hình 11-2 và 11-3 được vẽ lại dạng vector "
               "đã đơn giản hóa, còn Hình 11-1 là bản rút gọn của phiếu dữ liệu "
               "ISA."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Van không ổn định", "The Valve Is Unstable"))
    b.append(p("The instability caused by dynamic fluid forces on a plug, disk, "
               "or ball should not be confused with positioner or control loop "
               "instability (sometimes hard to distinguish). As shown in the "
               "prior example, forces acting on a valve plug or across a "
               "butterfly valve (or rotating plug, for that matter) can vary "
               "drastically with flow conditions. Many papers have been written "
               "on the subject [4], most requiring you to become a math major! "
               "Therefore, I will try to keep the matter simple."))
    b.append(p("For a valve trim to be stable, the change in stem force per inch "
               "of stem motion has to be less than the change in stem force per "
               "inch of travel exerted by the actuator. The latter is called the "
               "actuator stiffness factor, Kn, and is expressed in-lb/in. For a "
               "spring-diaphragm actuator, this is simply the spring rate of the "
               "actuator spring (or all the springs combined if multispring), "
               "ignoring the pneumatic damping."))
    b.append(p("With piston actuators, things get a bit more complex. Here, the "
               "force generated by compressing the internal actuator air "
               "pressure when the piston is moved over a given distance "
               "determines the stiffness. Obviously, this force varies with "
               "stem position, initial cylinder volume (L), and absolute air "
               "pressure. As a rule, piston actuators are much stiffer [5] than "
               "spring-diaphragm actuators and, therefore, can operate "
               "single-seated globe valves in the flow-to-close direction, a "
               "feat normal spring-diaphragm actuators cannot handle."))
    b.append(p("The general practice is to install single-seated globe valves in "
               "the flow-to-open direction, where the problem of dynamic "
               "instability seldom arises. However, it can be a problem in "
               "force-balanced cage valves and angle valves handling cavitating "
               "or flashing fluids where discharging occurs downstream of the "
               "valve plug (flow tending-to-close). What happens is that not "
               "only does the effective area of the plug increase as you approach "
               "the seating point but, in addition, the downstream pressure "
               "decreases rapidly, roughly to the square of the flow rate "
               "decrease. We all have experienced this phenomenon in the "
               "bathtub: with water in the tub, as we slowly let go of the chain, "
               "the rubber plug approaches the drain, but, at about 3/16 in from "
               "the seat, the plug suddenly surges down and slams onto the seat. "
               "The same thing happens in a valve. The trick is to have the "
               "actuator stiff enough to hold the valve plug in place."))
    b.append(p("As a rule of thumb, consider that the off-balance plug area goes "
               "from zero to maximum within a distance that is the lesser of "
               "either 1/3 of valve travel or 1/4 of the orifice diameter. "
               "Further, assume that the differential pressure will increase "
               "from P1 − P2 at normal flow to P1 maximum within this same "
               "distance."))
    b.append(p("Here is an example: A 3-inch angle valve with a 2.5-inch orifice "
               "diameter has a 1/2-inch valve stem diameter. Normal P1 = 165 "
               "psig; normal P2 = 125 psig; maximum P1 = 175 psig; flow-to-close "
               "actuator travel = 1.5 in. Because the area of the stem is "
               "relatively small, we can ignore this and assume the off-balance "
               "plug area of the 2.5-inch orifice, which is 4.9 in²."))
    b.append(p("First, consider the distance of area change: 1/3 of 1.5 in "
               "travel = 0.5 in; 1/4 of 2.5 in orifice diameter = 0.625 in; "
               "therefore, we chose 0.50 in as it is smaller. The rate of change "
               "in stem forces is now"))
    b.append(eq("1/3 × 1.5 in = 0.5 in;   1/4 × 2.5 in = 0.625 in;   choose 0.50 in", ""))
    b.append(eq("Off-Balance Area × ΔP change / Distance", "11-1"))
    b.append(p("where"))
    b.append(eq("ΔP change = maximum P1 − ΔP = 175 − (165 − 125) = 135 psi", ""))
    b.append(p("Therefore, from Equation 11-1, 4.9 in² × 135 psi / 0.50 in = "
               "1323 lb/in."))
    b.append(eq("4.9 in² × 135 psi / 0.50 in = 1323 lb/in", ""))
    b.append(p("Assuming the actuator is a spring-diaphragm with an area of "
               "100 in² and a 3 to 15 psi bench range, this makes the spring "
               "rate (15 − 3 psi) × 100 in² / 1.5 in travel = 800 lb/in."))
    b.append(eq("(15 − 3 psi) × 100 in² / 1.5 in = 800 lb/in", ""))
    b.append(p("This is quite insufficient, and we either have to recommend a "
               "175 in² actuator or change the bench range of the spring (or "
               "springs) to 6 to 30 psi."))
    b.append(eq("(30 − 6 psi) × 100 in² / 1.5 in = 1600 lb/in", ""))
    b.append(p("This would increase the actuator stiffness to 1600 lb/in, which "
               "will provide a sufficient safety margin. Air compression within "
               "the actuator will increase the stiffness and, therefore, provide "
               "a safety factor, although such stiffness is much less than in "
               "cylinder actuators due to larger air volume."))
    b.append(p("Rotary control valves have similar stiffness problems. They are "
               "more complex because we have to deal with torque instead of "
               "force. Consider the combined torque characteristic of a "
               "butterfly valve (shown in Figure 11-2, taken from Figure 4 in "
               "Reference 6). Here, the greatest change in torque per degree "
               "occurs at 60°, where the combined torque changes at a rate of "
               "(0.011 in-lb / d³ psi) × P1 for ±5° travel, that is, from 0.064 "
               "at 55° to 0.075 at 65°. Assume we have a 10-inch valve with a "
               "maximum differential pressure (when the valve is closed) of "
               "87 psig. We have a torque change at 60° opening (and assuming "
               "the valve has to open above 60° to pass the maximum flow) of "
               "0.011 in-lb × 10 in³ × 87 psi = 960 in-lb per 10°."))
    b.append(eq("(0.011 in-lb/d³ psi) × 10 in³ × 87 psi = 960 in-lb per 10°", ""))
    b.append(fig(2, F.fig_f112()))

    b.append(p("Assume we have a cylinder actuator with a 75 in² area that "
               "travels 4 in to move the vane from a 0° to 90° opening. "
               "Neglecting angular cosine effects, we can assume that at a 65° "
               "opening, the piston travel will be at (4 in / 90°) × 65° = "
               "2.88 in, and at 55° vane, travel = (4 in / 90°) × 55° = 2.44 in."))
    b.append(eq("(4 in / 90°) × 65° = 2.88 in;   (4 in / 90°) × 55° = 2.44 in", ""))
    b.append(p("What we need to know is the volume change if the actuator is "
               "going from 2.44 to 2.88 in piston travel and assuming 0.3 in of "
               "overtravel in the cylinder. Let us calculate the ratio of air "
               "volume between both travel positions:"))
    b.append(eq("Volume Ratio = A(hi + ho + Δh)/A(hi + ho)", ""))
    b.append(p("Therefore,"))
    b.append(eq("75 in²(2.88 in + 0.3 in) / 75 in²(2.44 in + 0.3 in) = "
                "239 in³ / 206 in³ = 1.16", ""))
    b.append(p("Assuming further that the positioner output pressure in the "
               "cylinder at 65° travel is 65 psia, we can now calculate the "
               "force change due to air compression caused by the actuator "
               "suddenly moving from 65° to 55° because of dynamic torque "
               "effects (remember that in most rotary valves, torque tends "
               "cause the valve to close)."))
    b.append(eq("Actuator force change = (Volume ratio − 1) × Area × Air pressure "
                "(10 − 2) = (1.16 − 1) × 75 in² × 65 psia = 780 lb", ""))
    b.append(p("All we have to do now is to convert this force change to torque. "
               "Because we know the travel is 4 in at 90° rotation, we can "
               "assume that the effective length of the lever turning the shaft "
               "is equal to actuator travel/2 × tan 45° = 4/(2 × 1) = 2.00 in."))
    b.append(eq("actuator travel/2 × tan 45° = 4/(2 × 1) = 2.00 in", ""))
    b.append(p("Thus, the force change of 780 lb translates into a torque change "
               "of 780 lb × 2 in = 1560 in-lb per 10° travel. This is above the "
               "dynamic vane torque change of 960 in-lb / 10°, and we could "
               "expect stability of operation because the friction of the "
               "piston seal will provide extra resistance to sudden change."))
    b.append(eq("780 lb × 2 in = 1560 in-lb per 10° travel", ""))
    b.append(fig(3, F.fig_f113()))

    b.append(p("If this had been a spring-diaphragm actuator with the same "
               "4-inch travel, a torque requirement of 960 in-lb per 10° vane "
               "travel would demand a 960 in-lb / 2 in effective lever = 480 lb "
               "force change per 0.44 in actuator travel and, therefore, would "
               "require a 480 lb / 0.44 in = 1091 lb/in spring rate."))
    b.append(eq("960 in-lb / 2 in = 480 lb per 0.44 in;   480 lb / 0.44 in = "
                "1091 lb/in", ""))
    b.append(p("Neglecting added stiffness due to air compression, this is "
               "equivalent to a 180 in² actuator with a 6 to 30 psi bench "
               "range—a drastic increase in actuator size."))
    b.append(p("While the above example assumed a conventional vane, so-called "
               "low-torque vanes would reduce the stiffness requirement and "
               "would, therefore, be effective when allowing for the use of "
               "spring-diaphragm actuators despite their lower stiffness factor. "
               "Note: A 60° opening with the 15° angle-seating, low-torque vane "
               "occurs at 45° vane travel (see Figure 11-2)."))
    b.append(note("<b>Note.</b> The source prints «15-inch angle-seating»; it is "
                  "presented here as 15°, as intended."))
    b.append(p("The following is a summary of stiffness equations [8]."))
    b.append(ul([
        "Spring-diaphragm actuator (ignoring lesser stiffness due to air "
        "compression<sup>5</sup>):"
        + eq("Kn = (Diaphragm area × Signal span)/Travel lb/in", ""),
        "Cylinder actuator (single-acting):"
        + eq("Kn = {[A<sub>C</sub>(h<sub>i</sub> + h<sub>o</sub> + Δh)/"
             "A<sub>C</sub>(h<sub>i</sub> + h<sub>o</sub>)] − 1} × S × "
             "A<sub>C</sub>/Δh lb/in", "")
        + "<p>where A<sub>C</sub> = effective area of the cylinder, in²; "
          "h<sub>i</sub> = initial travel position, in; h<sub>o</sub> = "
          "overtravel of the piston (travel not used), in; S = signal pressure "
          "at given travel position, psia; Δh = change in travel due to "
          "disturbance, in.</p>",
        "Cylinder actuator (double-acting). Results from single-acting cylinder "
        "actuator times two.",
    ]))
    b.append(note("<b>Footnote 5.</b> Assumed to be isothermal."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "H. D. Baumann, “How Do Control Valves Close?” Valve World magazine "
        "(April 2020): 78–79.",
        "N. Jeschke, et al., “Untersuchungen der Stopfbuchse Reibung an "
        "Stellventile Mit Pneumatischer Membranantrieb,” RTP, Volume 3. West "
        "Germany (1968).",
        "H. D. Baumann, “The Need for Pneumatic Power Signals for Control "
        "Valves,” InTech (January 1988): 34–41.",
        "G. A. Keith, “Analytical Prediction of Valve Stability,” ISA Paper "
        "838-70 (Research Triangle Park, NC: ISA, 1970).",
        "P. J. Schafbuch, “Fluid Inertia Effects on Unbalanced Valve Stability,” "
        "ISA Paper 85-0207 (Research Triangle Park, NC: ISA, 1983).",
        "H. D. Baumann, “Preventing Dynamic Instability of Rotary Valves,” Valve "
        "World magazine (October 2020).",
        "Paul J. Schafbuch, “Fluid Inertia Effects on Unbalanced Valve Stability,” "
        "Proceedings of the ISA Final Control Elements Symposium, April 1985, "
        "New Orleans, LA. Paper no. 85-207, 32–48.",
        "ISA-TR75.24.01-2017 draft, Liner and Pneumatic Actuator Sizing and "
        "Selection (Research Triangle Park, NC: ISA [International Society of "
        "Automation]).",
    ]))

    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "H. D. Baumann, “A Case for Butterfly Valves in Throttling Applications,” "
        "Instruments and Control Systems (May 1979): 35–38.",
    ]))

    b.append(note("<b>Source notes.</b> (1) The OCR text layer contains many "
                  "line-break hyphenations, which were rejoined into whole "
                  "words. The spaced «P 1» was normalized to P1, and OCR "
                  "fragments such as «2 2 π/4» and «2.0632 π/4» are presented as "
                  "(2²π/4) and (2.063²π/4). (2) The source denominator in the "
                  "Volume Ratio lacked parentheses; it is presented consistently "
                  "as A(hi+ho+Δh)/A(hi+ho). (3) The source lever expression "
                  "«4/(2 × l)» is treated as 4/(2 × 1). (4) The figure captions "
                  "print «toque» (a typo) and «15-inch angle-seating»; these are "
                  "given as torque and 15° with the typo noted. (5) Figures 11-1 "
                  "to 11-3 are simplified vector redrawings; Figure 11-1 is an "
                  "abridged ISA form, not a facsimile. (6) The chapter occupies "
                  "printed pp. 81–90 (PDF pp. 85–94); the title of reference 8 is "
                  "retained as printed."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("This final prose section of Chapter 11 occupies printed pp. "
               "85–90 of the book (PDF pp. 89–94); the full chapter spans "
               "printed pp. 81–90 (PDF pp. 85–94). Figures 11-2 and 11-3 are "
               "redrawn as simplified vectors, and Figure 11-1 is an abridged "
               "redrawing of the ISA form."))
    return "".join(b)
