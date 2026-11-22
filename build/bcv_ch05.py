# -*- coding: utf-8 -*-
"""Book 7b, Chapter 5 — Control Valve Actuators (EN/VI bilingual).

Source: Borden / Friedmann (eds.), *Control Valves*, ISA Practical Guides
for Measurement and Control (1998), Chapter 5, printed pp. 93-103.  The local
source is a 12-page image-only scan (p01 is the book cover; p02-p12 are the
printed chapter).  There is no text layer, so the prose below was transcribed
from the scanned pages.  The four numbered source figures (5-1 ... 5-4) are
redrawn as vector schematics in `bcvfig.py`.
"""

from bcv_common import (fig, h2, h3, note, p, refs)
import bcvfig as F

PAGES_SRC = 11            # printed pp. 93-103 inclusive (the scan has 12 pages)
BYLINE = "Guy Borden, Jr., Editor · Paul G. Friedmann, Style Editor · ISA, 1998"
TITLE_EN = "Control Valve Actuators"
TITLE_VI = "Cơ cấu chấp hành van điều khiển"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 5.</b> control valve actuator — cơ cấu chấp hành "
                "van điều khiển · isolation valve — van cô lập · signal — tín hiệu · "
                "power source — nguồn năng lượng · psig — pound trên inch vuông (áp "
                "suất kế) · mA — miliampe · direct-acting / air-to-extend — tác động "
                "trực tiếp / khí đẩy thân van ra · reverse-acting / air-to-retract — "
                "tác động ngược / khí kéo thân van vào · fail-open / fail-closed — "
                "mở / đóng khi mất nguồn · spring-opposed diaphragm — màng đối lò "
                "xo · rolling diaphragm — màng lăn · bench range — dải băng (phạm vi "
                "bàn thử) · dead band — vùng chết · positioner — bộ định vị · spring "
                "rate — độ cứng lò xo · effective area — diện tích hiệu dụng · yoke — "
                "giá đỡ · piston — piston · O-ring seal — phớt chữ O · electric "
                "motor/gear — mô-tơ điện/bộ giảm tốc · electrohydraulic — điện-thủy "
                "lực · modulating solenoid — van điện từ điều tiết · LVDT — biến áp "
                "sai biệt tuyến tính · vane actuator — cơ cấu chấp hành cánh quạt · "
                "lever / rack and pinion / scotch yoke / ball screw — đòn bẩy / bánh "
                "răng thanh răng / cơ cấu scotch yoke / vít bi · lockup valve — van "
                "khóa · handwheel override — tay quay dự phòng · volume booster — bộ "
                "tăng lưu lượng khí.")
    return ("<b>Key terms.</b> control valve actuator · isolation valve · signal vs. "
            "power source · psig · mA · direct-acting / air-to-extend · reverse-acting "
            "/ air-to-retract · fail-open / fail-closed · spring-opposed diaphragm · "
            "rolling diaphragm · bench range · dead band · positioner · spring rate · "
            "effective area · yoke · piston · O-ring seal · electric motor/gear · "
            "electrohydraulic · modulating solenoid · LVDT · vane actuator · lever · "
            "rack and pinion · scotch yoke · ball screw · lockup valve · handwheel "
            "override · volume booster.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e, e if vi else v))

    def N(v, e):
        b.append(note(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ---- opening (printed p. 93) ------------------------------------------
    P("Cơ cấu chấp hành van điều khiển là thiết bị chạy bằng chất lưu hoặc điện, "
      "cung cấp lực cần thiết để định vị trục hoặc thân van.",
      "A control valve actuator is a fluid or electrically powered device that "
      "supplies the required force to position a valve shaft or stem.")

    P("Khác với cơ cấu chấp hành của van cô lập, cơ cấu chấp hành van điều khiển "
      "tạo ra chuyển động tới một vị trí nhất định <b>tỷ lệ với tín hiệu</b> do bộ "
      "điều khiển hệ thống gửi tới. Cơ cấu chấp hành van cô lập thường chỉ có hai "
      "vị trí: mở hoàn toàn hoặc đóng hoàn toàn. Ngược lại, cơ cấu chấp hành van "
      "điều khiển hiếm khi mở hoặc đóng hẳn mà luôn ở <b>vị trí trung gian</b> do "
      "bộ điều khiển yêu cầu để thỏa mãn điều kiện của hệ thống quá trình. Một cơ "
      "cấu chấp hành van điều khiển không chủ yếu dùng để đóng kín thường tạo ra "
      "<b>lực đầu ra nhỏ hơn</b> cơ cấu chấp hành van cô lập; tuy nhiên, nó bảo đảm "
      "điều khiển vị trí chính xác.",
      "Distinct from an isolation valve actuator, a control valve actuator provides "
      "motion to a certain position <b>in proportion to a signal</b> sent from a "
      "system controller to the actuator. An isolation valve actuator usually "
      "provides one of two positions: full open or full closed. In contrast, a "
      "control valve actuator is seldom fully open or closed but in an "
      "<b>intermediate position</b> required by the controller to satisfy the "
      "process system conditions. A control valve actuator that is not primarily "
      "used for tight shutoff usually produces <b>less output force</b> than an "
      "isolation valve actuator. However, it provides accurate position control.")

    P("Quá trình lựa chọn cơ cấu chấp hành van điều khiển xem xét nhiều thuộc tính. "
      "Cơ cấu chấp hành có đủ hành trình không? Có tạo đủ lực hoặc mô-men để đáp ứng "
      "nhu cầu của van trong ứng dụng cụ thể không? Ngoài những xem xét cơ bản đó "
      "còn nhiều yếu tố khác giúp xác định kiểu cơ cấu chấp hành nào phù hợp nhất. "
      "<b>Không có kiểu cơ cấu chấp hành nào là xấu hay tốt</b>; mỗi kiểu đều tốt "
      "cho những ứng dụng riêng. Chương này thảo luận nhiều kiểu và mô tả đặc tính "
      "của chúng để hỗ trợ quá trình lựa chọn.",
      "The selection process for a control valve actuator considers many "
      "attributes. Does the actuator have sufficient travel? Does the actuator "
      "generate sufficient force or torque to satisfy the valve's need for the "
      "specific application? Beyond these basic considerations are many more that "
      "will identify which actuator is best suited for the application. "
      "<b>There are no bad or good actuator styles</b>; they all are good for "
      "specific applications. This chapter discusses many styles and describes "
      "their characteristics to aid in the selection process.")

    P("Gần đây, cơ cấu chấp hành van điều khiển đã phát triển theo kịp sự phát triển "
      "của chính các van điều khiển. Những thay đổi gồm có thêm nhiều kiểu chuyển "
      "động quay, cơ cấu chấp hành chính xác hơn dùng thủy lực, và bộ truyền "
      "mô-tơ/bánh răng.",
      "Control valve actuators have evolved recently to keep pace with the "
      "evolution of control valves. The changes include more styles of rotary "
      "motion, higher precision actuators using hydraulics, and motor/gear drives.")

    # ---- Signals and Power Sources ----------------------------------------
    H("Nguồn tín hiệu và nguồn năng lượng", "Signals and Power Sources")
    P("Mọi van điều khiển đều nhận tín hiệu từ một bộ điều khiển. Đó là đặc điểm "
      "phân biệt van điều khiển với tất cả các van khác.",
      "All control valves receive a signal from a controller. This is the "
      "characteristic that distinguishes control valves from all other valves.")

    P("Cơ cấu chấp hành van điều khiển cần hai tác động từ bên ngoài: một <b>tín "
      "hiệu</b> và một <b>nguồn năng lượng</b>. Tín hiệu thường là tín hiệu khí nén "
      "tương tự 3 đến 15 psig hoặc dòng điện 4 đến 20 miliampe (mA). Ngoài ra, tín "
      "hiệu số bắt đầu xuất hiện và sẽ sớm tạo ra ảnh hưởng đáng kể đối với công "
      "nghệ điều khiển.",
      "Control valve actuators require two outside influences, a <b>signal</b> and "
      "a <b>power source</b>. The signal is typically an analog pneumatic 3 to 15 "
      "psig or a 4 to 20 milliamperes (mA) electric current. In addition, digital "
      "signals are beginning to emerge and will soon make a significant impact on "
      "control technology.")

    P("Nguồn năng lượng phổ biến nhất cho cơ cấu chấp hành là khí nén trong khoảng "
      "60 đến 100 psig. Điện xoay chiều (AC) và một chiều (DC) cũng được dùng, cũng "
      "như năng lượng thủy lực. Năng lượng thủy lực có thể lấy từ một nguồn tập "
      "trung hoặc được tạo ra ngay tại cơ cấu chấp hành từ điện năng. Khí nén là "
      "nguồn năng lượng có chi phí thấp nhất và được dùng trong hầu hết các ứng "
      "dụng. Tuy nhiên, điện và thủy lực có những ưu điểm mà khí nén không có. Với "
      "nhiều ứng dụng, tín hiệu khí nén đồng thời cũng là nguồn năng lượng của cơ "
      "cấu chấp hành.",
      "The most common power for actuators is compressed air in the 60 to 100 psig "
      "range. AC and DC electric power are also used, as is fluid hydraulic power. "
      "The hydraulic power can come from a central source or can be generated at "
      "the actuator from electric power. Compressed air is the lowest-cost power "
      "source and is used in the vast majority of applications. However, "
      "electricity and hydraulics have certain virtues that are not available in "
      "pneumatics. For many applications the pneumatic signal also serves as the "
      "actuator's power.")

    # ---- Basic Styles ------------------------------------------------------
    H("Các kiểu cơ bản", "Basic Styles")
    P("Cơ cấu chấp hành có nhiều kiểu khác nhau, mỗi kiểu có ưu điểm và đặc tính "
      "riêng. Mỗi loại đều có một giá trị riêng; nếu không có thì nó đã không tồn "
      "tại trên thị trường.",
      "Actuators are available in many different styles, each with its own "
      "advantage and characteristic. Each type of actuator has its own virtue. If "
      "it did not, it would not exist in the market.")

    H("Màng / Lò xo", "Spring/Diaphragm", h3)
    P("Kiểu được dùng phổ biến và rộng rãi nhất là <b>màng đối lò xo</b> "
      "(spring-opposed diaphragm), như minh họa trong Hình 5-1 và 5-2. Màng làm "
      "bằng vật liệu cao su đàn hồi phủ vải (elastomeric/fabric) chuyển động ép vào "
      "đĩa màng, đĩa này bị kháng lại bởi một hoặc nhiều <b>lò xo nén xoắn ốc</b>. "
      "Nguồn năng lượng thường là khí nén, nhưng cũng có thể dùng khí nén hóa hoặc "
      "chất lỏng. Khí nén (hoặc chất lỏng) sẽ dịch chuyển hoặc ép màng về phía lò "
      "xo. Khi áp suất khí tăng lên, lò xo bị nén thêm và đẩy thân van đến vị trí "
      "yêu cầu. Khi áp suất khí giảm, lò xo kéo màng trở lại. Vì vậy, có thể đạt "
      "được vị trí mong muốn bằng cách thay đổi áp suất khí.",
      "The most common and widely used actuator is the <b>spring-opposed "
      "diaphragm</b>, which is illustrated in Figures 5-1 and 5-2. An "
      "elastomeric/fabric diaphragm moves against a diaphragm plate that is "
      "opposed by one or more helical coil compression springs. The power usually "
      "comes from compressed air, but compressed gas or a liquid can also be used. "
      "The compressed air will move or extend the diaphragm or a liquid against "
      "the spring. As more air pressure is applied, the spring is further "
      "compressed, moving the valve stem to the required position. When the air "
      "pressure is reduced the spring will retract the diaphragm. Therefore, "
      "position may be achieved by varying the air pressure.")

    FIG(1, F.fig_f51())

    P("Hướng của lực màng/lò xo có thể đảo ngược, tạo ra kiểu <b>khí đẩy thân van "
      "ra</b> (tác động trực tiếp, air-to-extend) hoặc <b>khí kéo thân van vào</b> "
      "(tác động ngược, air-to-retract). Việc lựa chọn tùy thuộc vào việc van phải "
      "ở trạng thái mở hay đóng khi mất nguồn. Hình 5-1 cho thấy cơ cấu tác động "
      "trực tiếp; Hình 5-2 minh họa tác động ngược.",
      "The orientation of the spring/diaphragm force direction can be reversed, "
      "providing either air to extend (direct-acting) or air to retract "
      "(reverse-acting). These options are chosen based on whether the valve is "
      "to fail in an open or closed position. Figure 5-1 shows a direct-acting "
      "actuator; Figure 5-2 illustrates reverse action.")

    FIG(2, F.fig_f52())

    P("Màng có thể là một tấm phẳng hoặc một màng lăn (rolling diaphragm) được tạo "
      "hình có nếp gấp. Tấm phẳng có chi phí thấp nhất nhưng diện tích hiệu dụng "
      "của nó thay đổi theo hành trình. Màng lăn đắt hơn nhưng nhìn chung có diện "
      "tích hiệu dụng không đổi trong suốt hành trình, cho độ chính xác cao hơn. "
      "Nó cũng có tuổi thọ chu kỳ dài hơn vì lăn thay vì uốn gập.",
      "The diaphragm can vary from a flat sheet to a molded convoluted rolling "
      "diaphragm. The flat sheet has the lowest cost but also has a changing "
      "effective area with travel. The rolling diaphragm is more expensive but "
      "has generally a constant effective area throughout the travel, providing "
      "greater precision. It also has a longer cycle life because it rolls rather "
      "than flexes.")

    P("Lò xo của cơ cấu chấp hành kháng lại lực do khí tác động lên màng. Lò xo có "
      "thể là một hoặc nhiều, xếp đồng tâm hoặc bố trí thành một vòng tròn. Ở kiểu "
      "tác động trực tiếp (air-to-extend), khí ở phía trên màng đẩy màng và thân "
      "cơ cấu chấp hành đi xuống; lò xo sẽ đẩy chúng lên khi giảm áp suất khí. Ở "
      "kiểu tác động ngược (air-to-retract), khí ở bên dưới màng đẩy màng và thân "
      "cơ cấu chấp hành đi lên; lò xo sẽ đẩy chúng xuống khi giảm áp suất khí.",
      "The actuator's springs oppose the force from the air on the diaphragm. The "
      "springs may be singular or multiple, nested concentrically or placed in a "
      "circular row. A direct-acting actuator, also called air-to-extend, has air "
      "on top of the diaphragm moving the diaphragm and actuator stem in a "
      "downward motion. The spring will move them up when the air pressure is "
      "reduced. A reverse-acting actuator, also called air-to-retract, has air "
      "underneath the diaphragm moving the diaphragm and actuator stem in an "
      "upward motion. The spring will move them down when the air pressure is "
      "reduced.")

    N("Kiểu tác động trực tiếp được chọn khi van phải <b>mở khi mất áp suất khí</b> "
      "(fail-open). Kiểu tác động ngược được chọn khi van phải <b>đóng khi mất khí</b> "
      "(fail-closed).",
      "<b>Direct-acting is chosen when the valve should fail open when air pressure "
      "is lost. Reverse-acting is chosen when the valve should fail closed with "
      "air failure.</b>")

    P("Lò xo ở chế độ air-to-extend thường có lực nhỏ và độ cứng thấp, chỉ đủ đưa "
      "cơ cấu chấp hành trở về vị trí ban đầu khi áp suất khí giảm. Chế độ ngược "
      "(air-to-retract) thường dùng lò xo có lực lớn hơn và độ cứng cao hơn để tạo "
      "lực đóng kín và độ ổn định cần thiết.",
      "The springs in the air-to-extend mode are usually low force with a low "
      "spring rate that simply provides enough force to return the actuator to "
      "its initial position as air pressure is reduced. The reverse or "
      "air-to-retract mode often uses springs with higher forces and a higher "
      "spring rate to provide the required shutoff force and operating stability.")

    P("Lò xo thường được chọn cho tín hiệu 3 đến 15 psig hoặc 6 đến 30 psig. Tuy "
      "nhiên, các dải khác như 25 đến 50 psig cũng được dùng cho ứng dụng "
      "air-to-retract, khi chính lò xo tạo ra lực đóng kín. Các cơ cấu chấp hành "
      "màng/lò xo thời kỳ đầu chỉ dùng trực tiếp tín hiệu 3-to-15 hoặc 6-to-30-psig "
      "tác động lên màng. Lực đẩy ròng lên thân van khi đó rất nhỏ vì gần như toàn "
      "bộ áp suất tín hiệu được dùng để nén lò xo. Về sau, việc dùng bộ định vị đã làm tăng "
      "đáng kể dải lực đẩy của cơ cấu chấp hành, đặc biệt ở chế độ tác động trực "
      "tiếp. Áp suất cấp được nạp lên màng khi van đã ngồi kín và tín hiệu của bộ "
      "định vị đạt giới hạn trên, 15 hoặc 30 psig. Thay vì chỉ có lực ròng 2 hoặc 3 "
      "psi ép van, có thể đạt lực ròng 45 psi với áp suất cấp 60 psig.",
      "The springs often match a 3 to 15 psig or 6 to 30 psig signal. However, "
      "other ranges, such as 25 to 50 psig, are used for air-to-retract "
      "applications, in which the springs provide the shutoff force. Early "
      "spring/diaphragm actuators were used solely with a 3-to-15 or "
      "6-to-30-psig signal directly on the diaphragm. The net thrust to the valve "
      "stem was quite small as virtually all of the signal pressure was used to "
      "compress the spring. In later years, the use of valve positioners greatly "
      "increased the actuator's thrust range, especially in direct action. The "
      "supply pressure is loaded onto the diaphragm when the valve is seated and "
      "the positioner's signal reaches the upper limit, 15 or 30 psig. Instead of "
      "a net 2 or 3 psi seating the valve, 45 psi net pressure is possible with a "
      "60-psig supply pressure.")

    P("Một cơ cấu chấp hành thường được mô tả bằng <b>dải băng</b> (bench range). "
      "Dải băng nằm giữa áp suất mà cơ cấu chấp hành bắt đầu chuyển động và áp "
      "suất mà nó đạt hết hành trình. Cơ cấu chấp hành với lò xo 3-to-15 psi sẽ "
      "có “dải băng” 3-to-15. Tiếc là “dải băng” có thể bị sai lệch khi van đang "
      "vận hành.",
      "An actuator is often characterized by its <b>bench range</b>. The bench "
      "range lies between the pressure at which the actuator begins to move and "
      "the pressure at which the actuator reaches full travel. An actuator with "
      "a 3-to-15 psi spring will have a 3-to-15 “bench range.” Unfortunately, "
      "the “bench range” may distort when the valve is in service.")

    N("Xét một cơ cấu chấp hành có màng hiệu dụng 100 inch vuông trên một van chịu "
      "lực đẩy lên 200 pound do áp suất. Trong chế độ này, dải băng bị lệch 2 psi: "
      "cơ cấu chấp hành bắt đầu chuyển động ở 5 psi (3 psi cộng 2 psi lệch) và tới "
      "chỗ ngồi ở 17 psi. Theo quy tắc thường dùng, van ở giữa hành trình tại 9 "
      "psig, nhưng trong trường hợp này là 11 psig. Có bốn cách xử lý: dùng van có "
      "cân bằng áp suất tốt hơn, dùng cơ cấu chấp hành lớn hơn, dịch chuyển tín "
      "hiệu bộ điều khiển thành 5 đến 17 psi, hoặc dùng bộ định vị.",
      "Consider an actuator with a 100-square-inch effective diaphragm on a valve "
      "that has an upward thrust from pressure of 200 pounds. In this service, "
      "the bench range is biased by 2 psi, the actuator begins to move at 5 psi (3 "
      "psi plus the 2-psi bias) and will reach the seat at 17 psi. The usual rule "
      "is the valve is at mid-travel at 9 psig, but in this case it is 11 psig. "
      "There are four solutions to this situation: use a valve that has a better "
      "pressure balance, use a larger actuator, bias the controller's signal to 5 "
      "to 17 psi, or use a positioner.")

    N("Vùng chết 10% là chuyện thường gặp. Thêm vùng chết vào cơ cấu chấp hành có "
      "dải băng 3-to-15: tương đương lực cản ma sát 1,5 psi và sai số vị trí 10%. "
      "Áp suất tại điểm giữa hành trình khi đóng sẽ là 9 cộng 1,5, tức 10,5 psi, "
      "và khi mở là 9 trừ 1,5, tức 7,5 psi. Vì vậy, dải áp suất tại điểm giữa "
      "hành trình là từ 10,5 đến 7,5 psi.",
      "A dead band of 10% is not unusual. Let us add dead band to a 3-to-15 bench "
      "range actuator. This equates to a friction drag of 1.5 psi and a position "
      "error of 10%. The pressure at mid-travel while closing will be 9 plus 1.5, "
      "or 10.5 psi, and the pressure while opening will be 9 minus 1.5, or 7.5 "
      "psi. Therefore, the pressure range at mid-travel is 10.5 to 7.5 psi.")

    P("Ảnh hưởng của vùng chết có thể giảm bằng cách dùng tổ hợp van–cơ cấu chấp "
      "hành có ma sát rất thấp. Cách dễ hơn là loại bỏ gần như hoàn toàn vùng chết "
      "bằng cách lắp bộ định vị.",
      "The effect of dead band can be reduced with a valve-actuator combination "
      "that has very low friction. An easier solution is to virtually eliminate "
      "dead band by adding a positioner.")

    P("Diện tích hiệu dụng của cơ cấu chấp hành màng/lò xo có thể từ 30 đến 450 inch "
      "vuông, trong đó 60 đến 200 là dải thường gặp hơn. Hành trình có thể dài tới "
      "6 inch với những diện tích hiệu dụng lớn, nhưng thường là 3 inch hoặc ngắn "
      "hơn.",
      "The effective areas of spring/diaphragm actuators may range from 30 to 450 "
      "square inches, with 60 to 200 as the more common range. Travels may be as "
      "long as 6 inches for the larger effective areas but usually are 3 inches "
      "or less.")

    P("Lực tác dụng lên thân van từ phần trang trí bên trong van (trim) thường thay "
      "đổi trong suốt hành trình do diện tích hiệu dụng và độ giảm áp qua trim "
      "thay đổi. Để bảo đảm vận hành ổn định, tốc độ thay đổi lực của cơ cấu chấp "
      "hành phải cao hơn tốc độ thay đổi lực trong van do áp suất chất lưu quá "
      "trình và các lực động từ dòng chảy gây ra.",
      "The force on a valve stem from the valve's trim usually changes through "
      "its travel due to the changing effective areas and changing pressure drops "
      "of the valve trim. To ensure stable operation, the rate of force change in "
      "the actuator must be higher than the force change rate in the valve "
      "resulting from the effects of the process fluid pressure and the dynamic "
      "forces from flow.")

    P("Yếu tố đóng góp chính cho độ ổn định vận hành là <b>độ cứng lò xo</b> "
      "(spring rate). Góp phần vào đó còn có tỷ lệ nén của chất lưu ép màng. Khí "
      "ở áp suất thấp có tỷ lệ nén rất nhỏ, và tỷ lệ này tăng khi áp suất khí tăng. "
      "Chất lỏng ép có tỷ lệ nén cực cao và đóng góp đáng kể vào độ ổn định.",
      "The main contributor for operating stability is the actuator's <b>spring "
      "rate</b>. Also contributing is compression rate on the fluid that drives "
      "the diaphragm. Low-pressure air has a very low compression rate, with the "
      "compression rate increasing as the air pressure increases. A "
      "liquid-actuating fluid has an extremely high compression rate and will "
      "make a significant contribution to stable operation.")

    N("Một van không ổn định sẽ bị dao động thân van không kiểm soát được. Khi đó "
      "van đang điều khiển cơ cấu chấp hành nhiều hơn là cơ cấu chấp hành điều "
      "khiển van.",
      "<b>An unstable valve will have uncontrolled cycling stem motion. The valve "
      "will be driving the actuator more than the actuator will be driving the "
      "valve.</b>")

    P("Ách (yoke) của cơ cấu chấp hành màng/lò xo thường làm bằng gang, nhưng gang "
      "dẻo hoặc thép được dùng khi cần biên an toàn cao hơn trong những ứng dụng "
      "như điện hạt nhân, nơi độ tin cậy của van trong sự kiện địa chấn là mối quan "
      "tâm hàng đầu. Rung động hoặc chuyển động đột ngột của đường ống có thể gây "
      "ứng suất đủ lớn làm hỏng gang xám. Vỏ màng thường được dập từ thép, với "
      "hình dạng cong và nón để tăng độ bền. Màng là vải phủ cao su đàn hồi; độ "
      "bền của màng bắt nguồn từ chính lớp vải, thường làm bằng nylon, polyester "
      "hoặc nomex. Màng có thể được phủ thêm lớp cao su nitrite hoặc neoprene. "
      "Cao su silicone được dùng cho môi trường nhiệt độ cao hoặc bức xạ cao. "
      "Vật liệu làm van và màng được thảo luận ở Chương 11.",
      "The spring/diaphragm actuator's yoke is usually made of cast iron, but "
      "ductile iron or steel is used when additional safety margins are desired "
      "in applications such as nuclear power, where valve reliability during a "
      "seismic event is a prime consideration. Pipeline vibrations or sudden "
      "motions can cause sufficient stresses to fail gray iron. The diaphragm "
      "cases are usually made of pressed steel using curved and conical shapes "
      "to enhance strength. The diaphragm is an elastomeric-coated fabric. The "
      "strength of the diaphragm is derived from the fabric, which is usually "
      "made of nylon, polyester, or nomex. The diaphragm may be sealed with a "
      "coating of nitrite or neoprene rubber. Silicone rubber may be used for "
      "high-temperature or high-radiation situations. Valve and diaphragm "
      "materials are discussed in Chapter 11.")

    P("Cơ cấu chấp hành màng/lò xo có chi phí thấp nhất trong tất cả các cơ cấu "
      "chấp hành van điều khiển. Dải diện tích hiệu dụng và hành trình của nó bao "
      "phủ hầu hết các ứng dụng van. Một nhược điểm là độ cứng thấp hơn, có thể "
      "không ổn định trong một số ứng dụng. Đôi khi nó cũng thiếu hành trình hoặc "
      "diện tích hiệu dụng cần thiết.",
      "The spring/diaphragm actuator has the lowest cost of all control valve "
      "actuators. Its range of effective areas and travels covers most valve "
      "applications. A disadvantage is its lower stiffness, which may not be "
      "stable in some applications. It sometimes lacks sufficient travel and "
      "sufficient effective area.")

    # ---- Piston ------------------------------------------------------------
    H("Piston", "Piston", h3)
    P("Cơ cấu chấp hành piston có nhiều đặc điểm và ưu điểm chung với kiểu "
      "màng/lò xo. Điểm khác biệt chủ yếu là <b>phớt trượt hình trụ</b> thay cho "
      "màng uốn hoặc màng lăn. Ưu điểm chính của cơ cấu piston là khả năng hành "
      "trình dài hơn và diện tích hiệu dụng lớn hơn. Nó cũng nói chung chịu được "
      "áp suất chấp hành cao hơn. Như kiểu màng, cơ cấu piston có thể đối lò xo, "
      "air-to-extend hoặc air-to-retract. Cơ cấu piston cũng được dùng ở chế độ "
      "tác động kép (double-acting), với áp suất chấp hành tác động lên một bên "
      "hoặc cả hai bên piston tùy theo hướng và độ lớn của lực thân van cần có. "
      "Chế độ tác động kép cũng có thể dùng cùng chế độ đối lò xo. Một bộ định vị "
      "bốn chiều thường được dùng với chế độ tác động kép, trong khi bộ định vị "
      "một chiều có thể phục vụ chế độ đối lò xo.",
      "Piston actuators share many features and advantages of the spring/diaphragm "
      "style. The principal difference is the cylindrical sliding seal instead "
      "of a flexing or rolling diaphragm. The main advantages of a piston "
      "actuator are its capacity for longer travel and larger possible effective "
      "area. It also generally tolerates higher actuating pressures. As with the "
      "diaphragm style, the piston actuators can be spring-opposed, air-to-extend "
      "or air-to-retract. Piston actuators are also used in double-acting mode "
      "with actuating pressure on either side or both sides of the piston "
      "depending on the required direction and magnitude of stem force. The "
      "double-acting mode can also be used with the spring-opposed mode. A "
      "four-way positioner is often used with the double-acting mode, while a "
      "single-acting positioner may serve the spring-opposed mode.")

    P("Khả năng chịu áp suất cao hơn của cơ cấu piston rất phù hợp với nguồn thủy "
      "lực. Năng lượng có thể lấy từ nguồn ở xa hoặc được tạo ra ngay tại cơ cấu "
      "chấp hành bằng bơm điện. Những ưu điểm gồm độ ổn định cao, lực đầu ra lớn "
      "hơn ở áp suất cao, và có thể tốc độ di chuyển nhanh hơn, tùy thuộc vào "
      "nguồn cung cấp chất lỏng thủy lực.",
      "The higher pressure capacity of a piston actuator is well suited for "
      "hydraulic power. The power may come from a remote source or may be "
      "generated at the actuator by an electric pump. The advantages include "
      "high stability, higher force output with higher pressures, and possibly "
      "faster travel speeds, depending on the supply of hydraulic fluid.")

    P("Thiết kế phớt của piston rất quan trọng. Hai đặc tính mong muốn là tuổi thọ "
      "dài và ma sát thấp. Phớt piston hiệu quả là một vòng chữ O (O-ring). Độ nén "
      "của phớt phải thấp để tránh bị xoắn khi piston di chuyển. Vòng chữ O có ưu "
      "điểm là làm việc được hai chiều. Một cơ cấu piston thường dùng trong dịch "
      "vụ thủy lực có phớt nặng, ma sát cao, và có thể không phù hợp làm cơ cấu "
      "chấp hành van điều khiển.",
      "The design of the piston's seal is important. Two characteristics are "
      "desirable: long life and low friction. An effective piston seal is an "
      "O-ring. The seal compression must be low to prevent twisting of the "
      "O-ring as the piston travels. The O-ring has the advantage of being "
      "bidirectional. A piston actuator commonly used in hydraulic power service "
      "usually has a heavy seal that has high friction and may not be suitable "
      "as a control valve actuator.")

    P("Ách của cơ cấu piston được làm từ cùng vật liệu với kiểu màng/lò xo vì "
      "những lý do tương tự. Xi lanh piston có thể bằng đồng thau hoặc thép mạ. "
      "Sợi thủy tinh phủ lớp ma sát thấp ở đường kính trong cũng được dùng; nó "
      "nhẹ và ít ma sát nhưng không chịu lửa. Phớt piston có thể là vòng chữ O "
      "bằng cao su đàn hồi hoặc phớt Teflon được ép bởi áp suất hoặc lò xo kim "
      "loại. Một lựa chọn khác là vòng chữ O đàn hồi bọc Teflon, vừa có độ đàn hồi "
      "vừa có ma sát thấp.",
      "The piston actuator's yoke is made of the same materials as the "
      "spring/diaphragm for the same reasons. The piston cylinder may be brass or "
      "plated steel. Fiberglass with low friction coating on the inside diameter "
      "is also used, and while it has low weight and friction it lacks fire "
      "resistance. The piston seal may be an elastomeric O-ring or a Teflon seal "
      "energized either by pressure or a metallic spring. Another option is an "
      "elastomeric O-ring encapsulating with Teflon, which gives both resilience "
      "and low friction.")

    P("Cơ cấu chấp hành piston thường đắt hơn kiểu màng/lò xo nhưng có lợi thế về "
      "chi phí khi dùng với áp suất chấp hành cao hơn, diện tích hiệu dụng lớn, "
      "hoặc hành trình dài. Hình 5-3 cho thấy các van dùng cơ cấu chấp hành piston.",
      "Piston actuators usually cost more than a spring/diaphragm but offer a "
      "cost advantage when used with higher actuating pressures, with a large "
      "effective area, or with long travel. Figure 5-3 shows valves with piston "
      "actuators.")

    FIG(3, F.fig_f53())

    # ---- Electric Motor/Gear -----------------------------------------------
    H("Mô-tơ điện / Bộ giảm tốc", "Electric Motor/Gear", h3)
    P("Cơ cấu chấp hành mô-tơ điện với bộ giảm tốc tạo ra mô-men hoặc lực với "
      "chuyển động quay. Với van chuyển động quay, kết nối có thể là trực tiếp, "
      "nhưng van chuyển động tuyến tính cần chuyển đổi sang chuyển động tuyến "
      "tính. Một dạng chuyển đổi thường gặp là mô-tơ làm quay một đai ốc ren trên "
      "một thân không quay. Một hệ hiệu quả hơn dùng đai ốc bi tuần hoàn thay cho "
      "đai ốc ren.",
      "An electric motor actuator with gear reduction will produce torque or "
      "force with rotary motion. For rotary-motion valves, the connection may be "
      "direct, but conversion to linear motion is required for linear-motion "
      "valves. A common form of conversion involves the actuator turning a "
      "threaded nut on a nonrotating stem. A more efficient system uses a "
      "recirculating ball nut in place of the threaded nut.")

    P("Cơ cấu chấp hành mô-tơ điện có một số ưu điểm so với cơ cấu khí nén. Chúng "
      "rất phù hợp cho những vị trí xa vì truyền tải điện năng thực tế hơn trên "
      "quãng đường dài so với truyền khí nén.",
      "An electric motor actuator has several advantages over pneumatic "
      "actuators. They are well suited for remote locations because the "
      "transmission of electric power is more practical over long distances than "
      "is the transmission of compressed air.")

    P("Hầu hết cơ cấu mô-tơ điện/bộ giảm tốc sẽ giữ nguyên vị trí khi mất điện, trừ "
      "khi bộ bánh răng có hiệu suất rất cao và cho phép quay ngược (backdrive). "
      "Những ứng dụng van có lực thân van thay đổi nhanh – vốn có thể không ổn "
      "định với cơ cấu khí nén – sẽ vốn đã ổn định với cơ cấu điện có bánh răng. "
      "Hành trình tuyến tính dài dễ dàng đạt được. Với một công suất mô-tơ nhất "
      "định, việc đổi tỷ số bánh răng cho phép dễ dàng đánh đổi giữa mô-men và "
      "tốc độ di chuyển, hy sinh cái này để lấy cái kia. Cơ cấu điện có thể rẻ "
      "hơn hệ khí nén nếu tính cả chi phí bảo trì hệ thống khí nén.",
      "Most electric motor/gear actuators will fail in place on power "
      "interruption unless the gear train has very high efficiency and "
      "backdrives. Valve applications with rapidly changing stem forces that may "
      "be unstable with pneumatic actuators will be inherently stable with "
      "geared electric actuators. Long linear travels are easily achievable. "
      "With a motor of given horsepower, changing the gearing can easily trade "
      "between torque and travel speed, sacrificing one to gain the other. An "
      "electric actuator may cost less than a pneumatic system if the cost of "
      "maintaining the pneumatic system is included.")

    N("Cơ cấu điện trong những lắp đặt chỉ có ít van và không có nguồn khí nén có "
      "thể rẻ hơn việc lắp một máy nén khí cho vài van đó.",
      "<b>Electric actuators in installations with few valves and without a "
      "compressed air source may cost less than installing an air compressor for "
      "the few valves.</b>")

    P("Một số cơ cấu điện có công tắc giới hạn mô-men lò xo, ngắt mô-tơ khi đạt tới "
      "một mô-men nhất định. Các công tắc này có thể chỉnh được, cho phép thay đổi "
      "lực đầu ra cho phù hợp với ứng dụng. Công tắc giới hạn vị trí cũng được "
      "dùng trong cùng hệ thống để phát tín hiệu về vị trí hoặc ngắt mô-tơ ở các "
      "vị trí cực đoan.",
      "Some electric actuators have a spring-loaded torque limit switch that "
      "disengages the electric motor as a certain torque is reached. The torque "
      "switches are adjustable, allowing the delivered output to be varied to "
      "suit the application. Position-limit switches are also used in the same "
      "system to give a signal relative to position or to disengage the motor at "
      "extreme positions.")

    P("Đôi khi mô-tơ khí hoặc chất lỏng được dùng thay cho mô-tơ điện. Chất lưu có "
      "thể là khí nén, chất lỏng, hoặc chính chất lưu của quá trình.",
      "Fluid power motors are sometimes available in place of the electric motor. "
      "The fluids can be compressed air, liquids, or the process fluid itself.")

    P("Phụ tùng thường gặp gồm tay quay ghi đè (handwheel override), chỉ thị vị trí "
      "tại chỗ, công tắc giới hạn vị trí, đèn báo và nút mở/đóng/dừng.",
      "Common accessories include handwheel overrides, local position indicators, "
      "position-limit switches, indicating lights, and open/close/stop pushbuttons.")

    # ---- Electrohydraulic ---------------------------------------------------
    H("Điện-thủy lực", "Electrohydraulic", h3)
    P("Cơ cấu chấp hành điện-thủy lực kết hợp đặc tính của piston với một bơm "
      "thủy lực chạy bằng điện. Sự kết hợp này cho lực đầu ra lớn so với thể tích "
      "của cơ cấu chấp hành và thường có độ chính xác vị trí cao. Lò xo có thể "
      "được dùng để fail-open hoặc fail-closed, nhưng cũng dễ dàng đạt fail-as-is "
      "bằng cách khóa chất lỏng thủy lực ở vị trí cuối cùng.",
      "Electrohydraulic actuators combine the attributes of the piston with an "
      "electric-driven hydraulic pump. This combination delivers a high output "
      "force relative to the volume of the actuator and usually has high position "
      "accuracy. Springs can be used for either fail-open or fail-closed but also "
      "can easily be fail-as-is by locking the hydraulic fluids in the last position.")

    # ---- Electric Solenoid --------------------------------------------------
    H("Van điện từ điện", "Electric Solenoid", h3)
    P("Một phát triển gần đây là van điện từ điều tiết bằng điện (electric "
      "modulating solenoid). Bên trong nắp van hoặc phần nối dài của nắp có một "
      "lõi cố định và một lõi di động gắn với thân van. Cuộn dây điện từ được lắp "
      "bên ngoài ống nắp. Khi cấp điện cho cuộn, lực hút từ tính phát sinh giữa hai "
      "lõi. Lõi di động bị kháng bởi một lò xo bên trong ống nắp. Khi lực hút vượt "
      "qua lực lò xo, lõi di động tiến về phía lõi cố định, nén lò xo và dịch "
      "chuyển thân van. Lực từ tác động lên lõi di động tỷ lệ với dòng điện cấp "
      "cho cuộn. Chuyển động của lõi phụ thuộc vào giá trị dòng điện theo quan hệ "
      "với tốc độ của lò xo. Vì vậy, thay đổi dòng điện sẽ tạo ra chuyển động tỷ "
      "lệ của lõi hoặc thân van. Chuyển động của thân được đo bằng biến áp sai "
      "biệt tuyến tính (LVDT). Tín hiệu LVDT được đưa tới bộ định vị điện tử và "
      "tới bất kỳ chỉ thị vị trí nào tại chỗ hoặc từ xa.",
      "A recent actuator development is the electric modulating solenoid. Within "
      "the valve bonnet or bonnet extension is a fixed core and a movable core "
      "attached to the valve stem. A solenoid coil actuator is mounted external "
      "to the bonnet tube. Energizing the solenoid coil creates a magnetic "
      "attractive force between the fixed and movable cores. The movable core is "
      "opposed by a spring inside the bonnet tube. When the attractive force "
      "overcomes the spring force, the movable core moves towards the fixed core, "
      "compressing the spring and moving the valve stem. The magnetic force "
      "acting on the movable core is proportional to the current supplied to the "
      "solenoid. The movement of the core is dependent upon the value of the "
      "solenoid current in relationship to the rate of the spring. Therefore, "
      "varying the solenoid current results in proportional motion of the core "
      "or valve stem. The stem motion is measured by a linear variable "
      "differential transformer (LVDT). The LVDT signal is supplied to the "
      "electronic positioner and to any local or remote position indicators.")

    N("Lực truyền tới thân van từ van điện từ tương đối nhỏ so với các kiểu cơ cấu "
      "chấp hành khác. Thường cần trim cân bằng với lực nhỏ vì lực chấp hành tương "
      "đối nhỏ.",
      "<b>The force transmitted to the valve stem from the solenoid is relatively "
      "small compared to other style actuators. Balanced trims with low forces "
      "are usually required because of the relatively small actuating forces.</b>")

    P("Ưu điểm chính của van điện từ điều tiết là có thể bịt kín hoàn toàn van, "
      "với mọi bộ phận chuyển động nằm bên trong vỏ chịu áp của van.",
      "The electric modulating solenoid's primary advantage is that the valve "
      "can be hermetically sealed with all moving parts located within the "
      "valve's pressure enclosure.")

    # ---- Vane ---------------------------------------------------------------
    H("Cánh quạt", "Vane", h3)
    P("Cơ cấu chấp hành cánh quạt chỉ có đầu ra quay. Có thể coi nó như một piston "
      "quay. Bên trong một buồng áp suất chia đoạn là một cánh hoặc lá kín có đầu "
      "gắn với trục quay. Áp suất chất lưu ở một bên cánh tạo ra chuyển động quay "
      "cho trục. Ưu điểm chính của cơ cấu cánh quạt là đơn giản và chi phí thấp. "
      "Nhược điểm là <b>không có lò xo hồi vị bên trong, ma sát cao từ phớt của "
      "cánh, và khó lắp các phụ tùng thông thường</b>.",
      "Vane actuators have only rotary outputs. They can be thought of as a "
      "rotary piston. Located within a segmented pressure chamber is a sealed "
      "blade or vane whose end is attached to the rotary shaft. Fluid pressure on "
      "one side of the vane induces rotary motion in the shaft. The main virtue "
      "of a vane actuator is its simplicity and low cost. Its disadvantages are "
      "the lack of an internal spring-return, high friction from the vane's seal, "
      "and the difficulty of mounting the usual accessories.")

    # ---- Motion Conversion --------------------------------------------------
    H("Chuyển đổi chuyển động", "Motion Conversion")
    P("Cơ cấu màng/lò xo và piston vốn có chuyển động tuyến tính, trong khi cơ cấu "
      "mô-tơ điện/bánh răng vốn có chuyển động quay. Mỗi loại có thể được chuyển "
      "sang kiểu chuyển động kia bằng một thiết bị chuyển đổi.",
      "Spring/diaphragm and piston actuators have inherent linear motion while "
      "electric motor/gear actuators have inherent rotary motion. Each of these "
      "can be converted to the other motion using a conversion device.")

    H("Đòn bẩy (Tuyến tính sang quay)", "Lever (Linear to Rotary)", h3)
    P("Phương pháp phổ biến nhất là một đòn bẩy gắn ở một đầu vào trục van quay và "
      "đầu kia vào thân cơ cấu chấp hành tuyến tính. Thân cơ cấu chấp hành có thể "
      "nối trực tiếp vào đòn bẩy, nhưng phải có cách để màng/piston quay theo "
      "đường đi của điểm tựa đòn bẩy, hoặc phải thêm một liên kết giữa thân cơ cấu "
      "và điểm tựa đó.",
      "The most common method is a lever attached to a rotary valve shaft on one "
      "end and the linear actuator stem on the other. The actuator stem can be "
      "directly connected to the lever, but provisions must be made to enable "
      "the diaphragm/piston to rotate in the path of the lever pivot or a link "
      "must be added between the actuator stem and the lever pivot.")

    H("Bánh răng thanh răng (Tuyến tính sang quay)",
      "Rack and Pinion (Linear to Rotary)", h3)
    P("Phương pháp thứ hai là bánh răng thanh răng, thường dùng với cơ cấu piston. "
      "Trục piston được nối với một thanh răng, hoặc piston được chế tạo thành "
      "một khối với thanh răng. Thanh răng làm quay một bánh răng nhỏ lắp trên trục "
      "van quay.",
      "A second method is a rack and pinion that is usually used with a piston "
      "actuator. The piston shaft is connected to a rack, or the piston is "
      "integral with a rack. The rack turns a pinion gear that is mounted on the "
      "rotary valve shaft.")

    H("Cơ cấu chạng vạc (Tuyến tính sang quay)",
      "Scotch Yoke (Linear to Rotary)", h3)
    P("Cơ cấu chạng vạc (scotch yoke) là một biến thể của phép chuyển đổi bằng đòn "
      "bẩy, với thân cơ cấu chấp hành nối vào một rãnh trên đòn bẩy. Với cách bố "
      "trí này, không cần liên kết phụ cũng không cần điểm tựa quay.",
      "The scotch yoke is a variation of the lever conversion with the actuator "
      "stem connecting to a slot in the lever. Within this arrangement, neither "
      "an additional link nor pivoting is required.")

    H("Vít ren hoặc vít bi (Quay sang tuyến tính)",
      "Threaded Screw or Ball Screw (Rotary to Linear)", h3)
    P("Bộ phận quay ở giữa của cơ cấu mô-tơ điện/bánh răng có thể được cắt ren để "
      "nhận một thân ren hoặc một cơ chế vít bi tuần hoàn. Thân van được dẫn hướng "
      "để không quay, và ren quay hoặc vít bi sẽ chuyển chuyển động quay thành "
      "chuyển động tuyến tính.",
      "The center rotating member on an electric motor/gear actuator can be "
      "threaded to accept either a threaded stem or a recirculating ball screw "
      "mechanism. The stem will be guided so it does not rotate, and the rotating "
      "thread or ball screw will convert the rotary motion to linear.")

    # ---- Linear-Rotary Torque/Travel Relationships --------------------------
    H("Quan hệ mô-men – hành trình giữa tuyến tính và quay",
      "Linear-Rotary Torque/Travel Relationships")
    P("Quan hệ giữa mô-men đầu ra và hành trình của thân cơ cấu chấp hành với một "
      "lực thân không đổi khác nhau giữa ba phương pháp chuyển đổi tuyến tính "
      "sang quay. Mô-men đầu ra khi dùng đòn bẩy lớn nhất tại điểm giữa hành "
      "trình, khi đòn bẩy vuông góc với thân cơ cấu chấp hành. Mô-men đầu ra không "
      "đổi ở mọi vị trí với bánh răng thanh răng. Cơ cấu chạng vạc có mô-men lớn "
      "nhất ở hai đầu cực của hành trình – một lợi thế cho van quay cần mô-men "
      "đóng kín cao. Những khác biệt về đặc tính mô-men này có thể là yếu tố tích "
      "cực trong việc lựa chọn cơ cấu chấp hành, tùy vào nhu cầu của ứng dụng van.",
      "The relationship between output torque and the actuator stem travel with "
      "a constant stem force differs for the three different linear-to-rotary "
      "conversion methods. The output torque using the lever is greatest at "
      "mid-travel when the lever is perpendicular to the actuator stem. The "
      "output torque is constant at all travel with the rack and pinion. The "
      "scotch yoke has the greatest torque at the two extreme ends of the travel, "
      "an advantage for rotary valves that require high seating torques. These "
      "differences in torque characteristic can be a positive factor in selecting "
      "actuators, depending on the need for which the valve is selected.")

    # ---- Motion/Force Amplifiers --------------------------------------------
    H("Bộ khuếch đại chuyển động / lực", "Motion/Force Amplifiers")
    P("Có thể dùng các thiết bị cơ khí để thay đổi quan hệ giữa hành trình và "
      "lực. Định luật bảo toàn năng lượng cho phép đánh đổi giữa hành trình và "
      "lực: nếu một đại lượng giảm hoặc tăng thì đại lượng kia thay đổi ngược lại. "
      "Có một số thiết bị cơ khí dùng cho phép chuyển đổi này: đòn bẩy, kéo cắt "
      "(scissors) hoặc cơ cấu bật (toggles), bánh răng và đòn bẩy quay.",
      "Mechanical devices can be used to modify the relationship between travel "
      "and force. The laws of energy conservation allow the trading of travel "
      "force. If one is reduced or increased the other will change inversely. "
      "There are several mechanical devices used for conversion: levers, scissors "
      "or toggles, gears, and a rotary lever.")

    # ---- Power Failure Modes -------------------------------------------------
    H("Chế độ khi mất nguồn", "Power Failure Modes")
    P("Mỗi loại cơ cấu chấp hành có một chế độ vị trí tự nhiên khi mất nguồn chấp "
      "hành. Màng hồi lò xo hoặc piston hồi lò xo sẽ trở về vị trí ban đầu khi "
      "không có nguồn chấp hành. Piston tác động kép sẽ chuyển theo hướng lực thân "
      "van do van tác động. Có thể ngăn cả hai trường hợp này nếu muốn, bằng một "
      "van khóa (lockup valve) bịt kín khí chấp hành trong cơ cấu khi mất nguồn. "
      "Một bình có thể được dùng làm bể chứa áp lực khi nguồn chất lỏng chấp hành "
      "bị gián đoạn. Cơ cấu mô-tơ điện/bánh răng nói chung giữ nguyên vị trí khi "
      "mất điện, trừ trường hợp hiệu suất cơ khí rất cao – khi đó nó sẽ quay "
      "ngược (back-drive) theo hướng lực tác động.",
      "Each actuator type has its natural mode of failure position when the "
      "actuation power is removed. A spring-return diaphragm or spring-return "
      "piston will return to its initial position with no actuating power. A "
      "double-acting piston will fail in the direction of applied stem force "
      "from the valve. Both of these cases can be prevented, if desired, with a "
      "lockup valve that seals the actuating air in the actuator upon power "
      "failure. A tank may be used as a pressure reservoir when the supply of "
      "actuating fluid is disrupted. The electric motor/gear actuator generally "
      "fails in place when power is interrupted except in cases of high "
      "mechanical efficiency, when it will back drive in the direction of applied "
      "force.")

    # ---- Actuator/Valve Sizing Factors --------------------------------------
    H("Yếu tố chọn kích cỡ cơ cấu chấp hành / van",
      "Actuator/Valve Sizing Factors")
    P("Việc chọn đúng kiểu và dạng cơ cấu chấp hành dựa trên nguồn năng lượng, "
      "mức độ phù hợp với mục đích sử dụng của van và chi phí.",
      "The selection of the appropriate actuator type and style is based on "
      "power, applicability to the valve's use, and cost.")

    P("Chế độ tác động – trực tiếp, ngược hoặc tác động kép – nên được chọn dựa "
      "trên yêu cầu của hệ thống quá trình.",
      "The mode of action, direct, reverse-, or double-acting, should be chosen "
      "based on process system requirements.")

    P("Lĩnh vực thứ ba trong việc tính chọn cơ cấu chấp hành là kích cỡ của nó. "
      "Nhà sản xuất thường chế tạo một dải kích cỡ; lực đầu ra tăng từ kích cỡ này "
      "sang kích cỡ kế tiếp theo tỷ lệ khoảng 1,6:1. Cần chọn kích cỡ phù hợp với "
      "ứng dụng. Hai yếu tố cần biết là lực hoặc mô-men đầu ra yêu cầu và hành "
      "trình yêu cầu. Lực hoặc mô-men cần có là tổng của lực ngồi kín, lực áp "
      "suất tác động lên trim hoặc các diện tích mất cân bằng, và diện tích thân "
      "van, cộng thêm ma sát của phớt và vật liệu đệm kín. Cũng phải xét đến các "
      "lực động do chất lưu đang chảy gây ra.",
      "The third area of actuator sizing and selection is the actuator's size. "
      "Actuator manufacturers will make a series of sizes. Actuator sizes are "
      "often made with the outputs increasing from one size to another in a ratio "
      "of about 1.6:1. The appropriate size should be selected to suit the "
      "application. Two factors need to be known: the required force or torque "
      "output and the required travel. The required force or torque is the "
      "summation of seating forces, pressure forces acting on the trim or "
      "unbalanced areas, and the stem area, plus seals and packing friction. "
      "Dynamic forces from the flowing fluids must also be considered.")

    P("Như đã nêu ở trên, tốc độ thay đổi lực của van theo hành trình phải được "
      "biết hoặc ước lượng chính xác để bảo đảm độ cứng của cơ cấu chấp hành lớn "
      "hơn tốc độ thay đổi lực đó trong suốt hành trình. Nếu quan hệ bị đảo ngược, "
      "chuyển động của thân van sẽ bị dao động chu kỳ không ổn định. Thảo luận chi "
      "tiết về tính chọn cơ cấu chấp hành có trong Tài liệu tham khảo 1.",
      "As stated earlier, the valve's force rate of change relative to travel "
      "must be known or accurately estimated to ensure the actuator's stiffness "
      "exceeds the valve's stem rate of change throughout the travel. If the "
      "relationship reverses, the valve's stem motion will have unstable cyclic "
      "motion. Detailed discussions of actuator sizing can be found in Reference 1.")

    N("Tốc độ thay đổi lực của van theo hành trình phải được biết hoặc ước lượng "
      "chính xác để bảo đảm <b>độ cứng của cơ cấu chấp hành lớn hơn tốc độ thay "
      "đổi lực của van trong suốt hành trình</b>.",
      "<b>The valve's force rate of change relative to travel must be known or "
      "accurately estimated to ensure that the actuator's stiffness exceeds the "
      "valve's force rate of change throughout the travel.</b>")

    P("Việc xác định lực hoặc mô-men cần thiết của van là trách nhiệm của nhà sản "
      "xuất van, trong khi nhà sản xuất cơ cấu chấp hành chịu trách nhiệm xác định "
      "đầu ra và đặc tính lực của cơ cấu. Trong hầu hết trường hợp, van và cơ cấu "
      "chấp hành do cùng một nhà sản xuất chế tạo.",
      "Determining the valve's required force or torque is the responsibility of "
      "the valve manufacturer, while the actuator manufacturer is responsible for "
      "determining the actuator output and force characteristic. In most cases, "
      "both the valve and actuator will be made by the same manufacturer.")

    # ---- Actuator Accessories -----------------------------------------------
    H("Phụ tùng của cơ cấu chấp hành", "Actuator Accessories")
    P("Cơ cấu chấp hành van điều khiển có thể có các phụ tùng bổ sung cho hiệu "
      "năng của nó. Phụ tùng van được thảo luận ở Chương 15. Các phụ tùng thường "
      "gặp của cơ cấu chấp hành được mô tả trong các mục sau.",
      "A control valve actuator may have accessories to complement its "
      "performance. Valve accessories are discussed in Chapter 15. The usual "
      "actuator accessories are described in the following sections.")

    H("Tay quay dự phòng / Điều khiển tay", "Manual Override or Handwheel", h3)
    P("Tay quay dự phòng có thể lắp trên đỉnh cơ cấu màng/lò xo, ép hoặc kéo theo "
      "hướng áp suất khí tác động. Nó thường kháng lại lò xo của cơ cấu chấp hành. "
      "Với cơ cấu piston và một số cơ cấu màng/lò xo, tay quay có thể lắp bên hông. "
      "Hình 5-4 cho thấy các kiểu lắp trên đỉnh và bên hông. Với piston tác động "
      "kép không có lò xo để kháng lại, nên tay quay có cơ chế khóa thân van, cho "
      "phép tác động lực theo cả hai hướng. Tay quay của cơ cấu mô-tơ điện/bánh "
      "răng thường là một thiết bị có thể nhả ly hợp, làm quay một trong các trục "
      "bánh răng chính. Tay quay được dùng để định vị van khi mất điện, đưa van "
      "đến một vị trí đặt trước để hiệu chỉnh phụ tùng, và đôi khi dùng làm điểm "
      "dừng hành trình trên cơ cấu màng/lò xo.",
      "A manual override may be top-mounted on a spring/diaphragm actuator either "
      "pushing or pulling in the direction of the applied air pressure. It "
      "usually opposes the actuator spring. For piston actuators and some "
      "spring/diaphragm actuators it may be side-mounted. Figure 5-4 shows "
      "top- and side-mounted overrides. For a double-acting piston there is no "
      "spring to oppose, so the override will have a stem locking feature that "
      "allows force to be applied in either direction. Overrides for electric "
      "motor/gear actuators are usually a disengageable device that turns one of "
      "the primary gear shafts. The override is used to position the valve "
      "during a power failure and move the valve to a set position for accessory "
      "calibration, and it is sometimes used on spring/diaphragm actuators as a "
      "travel stop.")

    FIG(4, F.fig_f54())

    H("Bộ định vị", "Positioners", h3)
    P("Bộ định vị là một bộ điều khiển van so sánh tín hiệu của bộ điều khiển với "
      "phản hồi vị trí thân van. Bộ định vị sẽ thay đổi năng lượng cấp cho cơ cấu "
      "chấp hành để hành trình của van khớp với tín hiệu. Ưu điểm của bộ định vị "
      "là độ chính xác định vị cao hơn và thường tốc độ di chuyển nhanh hơn. Bộ "
      "định vị có thể là khí nén, điện-khí nén hoặc điện.",
      "A positioner is a valve controller that compares the controller's signal "
      "with the stem position feedback. The positioner will change the power to "
      "the actuator so the valve travel matches the signal. The advantages of a "
      "positioner is higher positioning accuracy and usually faster travel "
      "speeds. Positioners can be pneumatic, electropneumatic, or electrical.")

    H("Công tắc hành trình", "Limit Switches", h3)
    P("Công tắc hành trình được lắp trên hoặc trong cơ cấu chấp hành để phát tín "
      "hiệu điện khi đạt đến một giới hạn hành trình đặt trước. Thường chúng được "
      "đặt ở hai đầu của hành trình, nhưng đôi khi cũng đặt ở một vị trí trung "
      "gian. Chúng thường được coi là thiết bị cho biết thân van đang ở đâu, nhưng "
      "thực tế chúng cho biết thân van <b>không ở đâu</b>.",
      "Limit switches are mounted on or in the actuator to give an electrical "
      "signal when a preset travel limit is reached. Usually, they are set at "
      "either end of the travel, but they are also sometimes set at an "
      "intermediate position. They are usually considered devices for telling "
      "where to stem is, but actually they tell where the stem isn't.")

    H("Bộ phát tín hiệu vị trí", "Position Transmitter", h3)
    P("Bộ phát tín hiệu vị trí có thể được coi là một bộ định vị ngược. Nó phát ra "
      "một tín hiệu liên tục, thường là 3 đến 15 psig hoặc 4 đến 20 mA, tỷ lệ với "
      "vị trí hành trình của van. Khác với công tắc hành trình, bộ phát tín hiệu "
      "vị trí luôn cho biết vị trí hành trình của van. Đôi khi bộ phát tín hiệu "
      "vị trí được tích hợp trong bộ định vị; điều này có thể mang lại lợi thế về "
      "chi phí. Tuy nhiên, nếu liên kết phản hồi hành trình trên bộ định vị hỏng, "
      "bộ phát tín hiệu vị trí sẽ cho tín hiệu sai. Cách an toàn nhất là lắp riêng "
      "biệt hai thiết bị này.",
      "A position transmitter can be considered a reverse positioner. It will "
      "provide a continuous signal, usually 3 to 15 psig or 4 to 20 mA, "
      "proportional to the valve's travel position. Unlike limit switches, a "
      "position transmitter always tells the valve's travel position. Sometimes "
      "a position transmitter is incorporated in the positioner; this may offer "
      "a cost advantage. However, if the travel feedback linkage on the "
      "positioner fails, the position transmitter will give a false signal. The "
      "safest approach is to have separate mountings for both devices.")

    H("Van điện từ", "Solenoid Valves", h3)
    P("Van điện từ có thể được dùng để ghi đè nguồn khí nén hoặc tín hiệu. Nó có "
      "thể được dùng để xả hoặc cấp áp suất đầy đủ cho cơ cấu chấp hành bất kể "
      "tín hiệu.",
      "A solenoid valve may be used as a pneumatic power or signal override. It "
      "may be used to vent or fully pressurize the actuator regardless of the "
      "signal.")

    H("Bộ điều áp", "Air Regulators", h3)
    P("Bộ điều áp hoặc bộ điều chỉnh khí được dùng để hạn chế áp suất khí tới cơ "
      "cấu chấp hành hoặc các phụ tùng của nó, nhằm tránh hư hỏng do quá tải cho "
      "các phụ tùng, cơ cấu chấp hành hoặc chính van.",
      "Air regulators or air sets are used to limit the air pressure to the "
      "actuator or its accessories in order to avoid overload damage to the "
      "accessories, the actuator, or the valve.")

    H("Bộ tăng lưu lượng khí", "Volume Boosters", h3)
    P("Bộ tăng lưu lượng khí được dùng để tăng lưu lượng khí tới cơ cấu chấp hành. "
      "Bộ định vị hoặc bộ điều khiển có thể không cho qua đủ thể tích khí để đạt "
      "thời gian di chuyển yêu cầu. Có thể lắp một bộ tăng lưu lượng trên đường ra "
      "của bộ định vị hoặc bộ điều khiển, với một kết nối để cấp áp suất khí. Bộ "
      "tăng là một thiết bị dẫn (pilot) sẽ chỉnh áp suất đầu ra theo áp suất đầu "
      "vào ở lưu lượng cao hơn.",
      "Volume boosters are used to increase air flow volume to the actuator. "
      "Positioners or controllers may not pass a sufficient amount of air volume "
      "to achieve the required travel time. A volume booster may be installed in "
      "the positioner's or controller's output line with a connection for "
      "supplying air pressure. The booster is a pilot device that will match its "
      "output pressure with its input pressure at higher flow rates.")

    # ---- References ---------------------------------------------------------
    H("Tài liệu tham khảo", "References")
    b.append(refs([
        "ISA-dRP75.24.01, “Control Valve Actuator Sizing Method” (Research "
        "Triangle Park, N.C.: ISA, 1997).",
    ]))

    # ---- About the source ---------------------------------------------------
    H("Về nguồn tài liệu", "About the source", h3)
    P("Chương này được chép từ <b>bản quét 12 trang, chỉ có hình ảnh</b> của một "
      "chương duy nhất: Chương 5 “Control Valve Actuators” của Borden / Friedmann "
      "(biên tập), *Control Valves*, ISA Practical Guides for Measurement and "
      "Control (1998). Trang p01 là bìa sách; các trang p02–p12 tương ứng với "
      "<b>11 trang in, từ tr. 93 đến tr. 103</b> (PAGES_SRC = 11). Tệp PDF nguồn "
      "không có lớp văn bản (text layer), nên toàn bộ prose ở đây được đọc và "
      "chép thủ công từ các trang quét. Bốn hình được đánh số trong nguyên bản "
      "(Hình 5-1 đến 5-4) đã được vẽ lại dạng vector trong <i>bcvfig.py</i>; những "
      "hình này là sơ đồ đơn giản hóa, không phải bản sao cơ khí chính xác.",
      "This chapter was transcribed from a <b>12-page, image-only scan of a "
      "single chapter</b>: Chapter 5, “Control Valve Actuators,” of Borden / "
      "Friedmann (eds.), *Control Valves*, ISA Practical Guides for Measurement "
      "and Control (1998). Page p01 is the book cover; pages p02-p12 correspond "
      "to the <b>11 printed pages 93-103</b> (PAGES_SRC = 11). The source PDF has "
      "no text layer, so all prose here was read and transcribed by hand from the "
      "scanned pages. The four numbered source figures (Figures 5-1 to 5-4) were "
      "redrawn as vectors in <i>bcvfig.py</i>; they are simplified schematics, "
      "not exact mechanical copies.")

    P("<b>Những điểm cần lưu ý về nguyên bản.</b> (1) Hình 5-1 và 5-2 được chú "
      "là “Courtesy of Norriseal,” Hình 5-3 là “Courtesy of Valtek,” Hình 5-4 là "
      "“Courtesy of Norriseal”; nhãn Series 127 (direct acting) và Series 137 "
      "(reverse acting) được giữ lại trong sơ đồ. (2) Ví dụ về vùng chết ở tr. 97 "
      "viết dải áp suất theo thứ tự cao xuống thấp, “10.5 to 7.5 psi” — giữ "
      "nguyên dù thứ tự này hơi bất thường. (3) Ở tr. 103, nguyên bản viết “The "
      "advantages of a positioner <i>is</i> higher ...” và “telling where <i>to</i> "
      "stem is” (lỗi chính tả rõ rệt của “the stem is”); bản Anh giữ nguyên, bản "
      "Việt dịch theo ý nghĩa. (4) Mục Vane ở tr. 100 thiếu dấu phẩy/liên từ giữa "
      "“lack of an internal spring-return” và “high friction from the vane's seal”; "
      "bản dịch tách rõ ba nhược điểm. (5) Mã tài liệu tham khảo được chép đúng "
      "theo trang quét là “ISA-dRP75.24.01” (thường thấy dạng ISA-dPR75.24.01 ở "
      "nơi khác). (6) Các hộp ô bên lề (sidebar) và hai hộp ví dụ được trình bày "
      "dưới dạng ô ghi chú trong bản dịch này.",
      "<b>Source discrepancies worth noting.</b> (1) Figures 5-1 and 5-2 are "
      "credited “Courtesy of Norriseal,” Figure 5-3 “Courtesy of Valtek,” and "
      "Figure 5-4 “Courtesy of Norriseal”; the Series 127 (direct acting) and "
      "Series 137 (reverse acting) labels are retained in the redraws. (2) The "
      "dead-band example on p. 97 states the mid-travel pressure range in "
      "descending order, “10.5 to 7.5 psi” — kept as printed although the order "
      "is unusual. (3) On p. 103 the source reads “The advantages of a "
      "positioner <i>is</i> higher ...” and “telling where <i>to</i> stem is” "
      "(an evident typo for “the stem is”); the English body keeps both, while "
      "the Vietnamese follows the intended meaning. (4) The Vane paragraph on "
      "p. 100 omits a comma/conjunction between “lack of an internal "
      "spring-return” and “high friction from the vane's seal”; the translation "
      "lists the three disadvantages separately. (5) The reference code is "
      "transcribed exactly as scanned, “ISA-dRP75.24.01” (elsewhere often seen "
      "as ISA-dPR75.24.01). (6) The printed sidebars and the two worked-example "
      "boxes are rendered as note boxes in this translation.")

    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
      "gốc © 1998 ISA — Instrumentation, Systems, and Automation Society.</i>",
      "<i>This is an unofficial translation for study purposes. Original content "
      "© 1998 ISA — Instrumentation, Systems, and Automation Society.</i>")

    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
