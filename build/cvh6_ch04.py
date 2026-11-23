# -*- coding: utf-8 -*-
"""Book 7c, Chapter 4 - Control Valve Accessories (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 82-97.
This chapter surveys the instruments directly connected to a control valve
assembly: positioners, I/P transducers, volume boosters, safety instrumented
systems, optimized digital valves, controllers, position transmitters, limit
switches, solenoid valves, trip systems, switching valves and handwheels. The
twenty-seven numbered figures are redrawn as vector schematics in `cvh6fig.py`
and placed at the points where the source captions occur.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import fig, h2, h3, lead, note, p, ul
import cvh6fig as F

PAGES_SRC = 16          # source printed pp. 82-97 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Control Valve Accessories"
TITLE_VI = "Phụ kiện van điều khiển"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> control valve accessory — phụ kiện van điều khiển · "
            "positioner — bộ định vị · pneumatic positioner — bộ định vị khí nén · "
            "analog I/P positioner — bộ định vị I/P tương tự · digital valve controller (DVC) — "
            "bộ điều khiển van số · diagnostics — chẩn đoán · two-way communication — truyền thông "
            "hai chiều · I/P transducer — bộ chuyển đổi I/P · volume booster — bộ tăng thể tích · "
            "deflector/nozzle — thanh chắn / vòi phun · safety instrumented system (SIS) — hệ thống "
            "an toàn bằng dụng cụ · partial stroke test (PST) — thử hành trình một phần · "
            "FMEDA — phân tích chế độ hỏng, ảnh hưởng và chẩn đoán · optimized digital valve (ODV) — "
            "van số tối ưu · proportional band — dải tỷ lệ · reset — tích phân · rate — vi phân · "
            "anti-reset windup — chống bão hòa tích phân · differential pressure controller — bộ "
            "điều khiển áp suất chênh · gauge pressure controller — bộ điều khiển áp suất đo · "
            "temperature indicating controller — bộ điều khiển chỉ thị nhiệt độ · "
            "position transmitter — bộ phát vị trí · limit switch — công tắc hành trình · "
            "solenoid valve (SOV) — van điện từ · 1oo1 / 1oo2 / 2oo2 — một trong một / một trong hai / "
            "hai trong hai · trip system — hệ thống ngắt · switching valve — van chuyển mạch · "
            "handwheel — tay quay")
    return (
        "<b>Key terms in this chapter.</b> control valve accessory · positioner · pneumatic "
        "positioner · analog I/P positioner · digital valve controller (DVC) · diagnostics · "
        "two-way communication · I/P transducer · volume booster · deflector/nozzle · safety "
        "instrumented system (SIS) · partial stroke test (PST) · FMEDA · optimized digital "
        "valve (ODV) · proportional band · reset · rate · anti-reset windup · differential "
        "pressure controller · gauge pressure indicating controller · temperature indicating "
        "controller · position transmitter · limit switch · solenoid valve (SOV) · "
        "1oo1 / 1oo2 / 2oo2 · trip system · switching valve · handwheel")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> Nguyên bản có một số điểm đặc thù: (1) mục 4.10 đánh số nhầm "
            "các hình van điện từ thành 14.14–14.23 dù chúng thuộc chương này; ở đây đổi thành "
            "4.14–4.23 theo thứ tự, và toàn bộ viết dẫn trong thân bilingual giữ số gốc kèm số đã "
            "sửa trong ngoặc; (2) Hình 4.11 và 4.12 cùng mang chú thích <i>Pneumatic Controller "
            "Schematic</i> trong bản in — ở đây vẫn giữ nguyên cụm từ đó nhưng thêm định danh "
            "chỉ tỷ lệ và tỷ lệ cộng tích phân cộng vi phân; (3) thân hình 4.11 gộp chữ "
            "<i>QuadrantBeam</i> do lỗi tách cột; (4) lỗi OCR <i>postioning</i> (mục 4.3) và "
            "<i>diaghragm</i> (mục 4.2.1) được giữ nguyên ở bản Anh và giải thích tại đây, bản "
            "Việt dịch đúng; (5) chỗ mục 4.4 dẫn «Figure 4.6» cho bộ tăng thể tích (thực ra là "
            "Hình 4.7) được giữ nguyên kèm số đã sửa; (6) mục 4.10 dẫn 14.17 cho cấu trúc 1oo2 "
            "và 14.19 cho 2oo2 dù chú thích gán các vai trò đó cho 14.19 và 14.20 — giữ nguyên "
            "theo nguồn. Các sơ đồ được vẽ lại dạng vector minh họa, không phải bản vẽ kỹ thuật "
            "có tỷ lệ.")
    return (
        "<b>Source notes.</b> The source has several quirks: (1) section 4.10 mis-numbers its "
        "solenoid-valve figures as 14.14-14.23 even though they belong to this chapter; here they "
        "are renumbered 4.14-4.23 and every body reference keeps the original number with the "
        "corrected number in parentheses; (2) Figures 4.11 and 4.12 both carry the caption "
        "<i>Pneumatic Controller Schematic</i> in print - the wording is preserved here but "
        "qualified as proportional-only and proportional-plus-reset-plus-rate; (3) a Figure 4.1 "
        "callout is run together as <i>QuadrantBeam</i> by the column break; (4) the OCR typos "
        "<i>postioning</i> (4.3) and <i>diaghragm</i> (4.2.1) are retained in English and "
        "explained here, while the Vietnamese text corrects them; (5) section 4.4 cites "
        "<i>Figure 4.6</i> for the volume booster (the booster is in fact Figure 4.7), kept with "
        "a corrected number added; (6) section 4.10 cites 14.17 for a 1oo2 architecture and "
        "14.19 for 2oo2 although the captions assign those roles to 14.19 and 14.20 - kept as "
        "printed. All diagrams are redrawn as illustrative vectors, not scale engineering "
        "drawings.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def B(v, e):
        b.append(ul(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn, lang))

    def N(v, e):
        b.append(note(v if vi else e))

    # ------------------------------------------------------------ lead
    b.append(lead(
        "Chương này trình bày các phụ kiện van điều khiển — từ bộ định vị, bộ chuyển đổi I/P, bộ "
        "tăng thể tích đến bộ điều khiển an toàn, hệ thống an toàn bằng dụng cụ, van điện từ, hệ "
        "thống ngắt, van chuyển mạch và tay quay — cùng các cân nhắc về môi trường và ứng dụng khi "
        "lựa chọn chúng."
        if vi else
        "This chapter presents control valve accessories - from positioners, I/P transducers and "
        "volume boosters to controllers, safety instrumented systems, solenoid valves, trip "
        "systems, switching valves and handwheels - together with the environmental and "
        "application considerations that govern their selection."))
    N(note_terms("vi"), note_terms("en"))

    P("Ngày nay, các hệ thống điều khiển hiện đại dùng tín hiệu điện tử để lệnh cho van điều khiển "
      "mở, đóng hoặc tiết lưu. Ngoài ra, các hệ thống này dùng tín hiệu phản hồi vị trí và thông tin "
      "chẩn đoán để xác nhận hoạt động của van điều khiển. Hơn nữa, kỳ vọng về hiệu năng của van "
      "điều khiển — về tốc độ đáp ứng, độ chính xác, độ ổn định, độ tin cậy và an toàn — thay đổi "
      "theo nhu cầu điều khiển quá trình. Vì van điều khiển được lắp trong nhiều ứng dụng khác nhau "
      "và đặc thù, phụ kiện van điều khiển là cần thiết. Phụ kiện là nhóm rộng các thiết bị được "
      "nối trực tiếp với cụm van điều khiển.",
      "Today, modern control systems use electronic signaling to command the control valve to "
      "open, close, or throttle. Additionally, these systems use position feedback signals and "
      "diagnostic information to validate the operation of the control valve. Furthermore, the "
      "performance expectations of control valves in terms of speed of response, accuracy, "
      "stability, reliability, and safety vary based on the process control needs. Because "
      "control valves are installed in many different and unique applications, control valve "
      "accessories are necessary. Accessories are the broad category of instruments that are "
      "directly connected to a control valve assembly.")
    P("Có năm lý do cơ bản để thêm thiết bị và phụ kiện vào van điều khiển:",
      "There are five basic reasons that instrumentation and accessories are added to a control "
      "valve:")
    B(["Cải thiện điều khiển quá trình;",
       "Cải thiện an toàn cho quá trình hoặc con người;",
       "Cải thiện hiệu năng van hoặc tốc độ đáp ứng;",
       "Giám sát hoặc kiểm chứng khả năng đáp ứng của van; và",
       "Chẩn đoán các sự cố tiềm ẩn của van."],
      ["Improve process control;",
       "Improve safety for the process or personnel;",
       "Improve valve performance or speed of response;",
       "Monitor or verify the valve responsiveness; and",
       "Diagnose potential valve issues."])

    # ------------------------------------------------------------ 4.1
    H("4.1 Các cân nhắc về môi trường và ứng dụng",
      "4.1 Environmental &amp; Application Considerations")
    P("Nhà máy công nghiệp, xưởng, mỏ và xưởng cán gặp điều kiện môi trường khắc nghiệt do vị trí "
      "địa lý và các quá trình sản xuất. Vì vậy, van và thiết bị trong các cơ sở này phải bền chắc "
      "và tin cậy.",
      "Industrial plants, factories, mines, and mills experience tough environmental conditions "
      "due to their geographical location and the processes involved in manufacturing their "
      "products. As a result, valves and instruments in these facilities must be rugged and "
      "reliable.")
    P("Nhiệt độ môi trường của thiết bị có thể từ -60 đến 125°C (-76 đến 257°F). Khí quyển ăn mòn, "
      "chẳng hạn nước biển và tiếp xúc hóa chất, có thể đòi hỏi vật liệu chế tạo bằng thép không "
      "gỉ hoặc nhựa kỹ thuật. Rung động mạnh có thể đòi hỏi lắp đặt thiết bị chắc chắn, cơ chế bên "
      "trong bền bỉ hoặc khả năng lắp đặt từ xa. Độ ẩm cao dẫn đến ăn mòn, nên có thể cần bảo vệ "
      "linh kiện điện tử. Địa điểm nguy hiểm chứa khí hoặc bụi có thể đòi hỏi thiết bị thiết kế "
      "theo các khái niệm bảo vệ như chống cháy, chống nổ, an toàn nội tại hoặc không gây cháy. "
      "Các điều kiện môi trường và ứng dụng này cần được cân nhắc khi chọn phụ kiện van điều khiển "
      "phù hợp.",
      "Ambient temperatures for instrumentation can range from -60 to 125°C (-76 to 257°F). "
      "Corrosive atmospheres, such as salt water and chemical exposure, may require stainless "
      "steel or engineered resin materials of construction. Intense vibration may require sturdy "
      "instrument mounting, rugged internal mechanisms, or remote mounting capability. High "
      "levels of humidity can lead to corrosion, so protection of electronic components may be "
      "necessary. Hazardous locations containing gaseous or dusty atmospheres may require "
      "instrumentation that is designed using protection concepts, such as flameproof, explosion "
      "proof, intrinsic safety, or non-incendive. These environmental and application conditions "
      "should be considered when selecting the proper control valve accessories.")

    # ------------------------------------------------------------ 4.2
    H("4.2 Bộ định vị", "4.2 Positioners")
    P("Một phụ kiện van điều khiển thường gặp là bộ điều khiển vị trí van, còn gọi là bộ định vị "
      "(positioner). Chức năng cơ bản của bộ định vị là cung cấp khí có áp suất cho cơ cấu chấp "
      "hành sao cho vị trí của thân hoặc trục van tương ứng với điểm đặt từ hệ thống điều khiển. "
      "Bộ định vị thường được dùng khi van cần tác động tiết lưu. Bộ định vị cần phản hồi vị trí "
      "từ thân hoặc trục van và cung cấp áp suất khí nén cho cơ cấu chấp hành để mở và đóng van. "
      "Bộ định vị phải được lắp trên hoặc gần cụm van điều khiển. Có ba loại chính tùy theo loại "
      "tín hiệu điều khiển, khả năng chẩn đoán và giao thức truyền thông.",
      "A common control valve accessory is the valve position controller, also called a "
      "positioner. The fundamental function of a positioner is to deliver pressurized air to the "
      "valve actuator, such that the position of the valve stem or shaft corresponds to the set "
      "point from the control system. Positioners are typically used when a valve requires "
      "throttling action. A positioner requires position feedback from the valve stem or shaft "
      "and delivers pneumatic pressure to the actuator to open and close the valve. The "
      "positioner must be mounted on or near the control valve assembly. There are three main "
      "categories of positioners, depending on the type of control signal, the diagnostic "
      "capability, and the communication protocol.")

    # ------------------------------------------------------------ 4.2.1
    H("4.2.1 Bộ định vị khí nén", "4.2.1 Pneumatic Positioners", h3)
    P("Loại thứ nhất là bộ định vị khí nén. Các đơn vị công nghệ cũ có thể dùng tín hiệu áp suất "
      "khí nén làm điểm đặt cho van điều khiển. Áp suất thường được điều biến giữa 20,7 và 103 kPa "
      "(3 đến 15 psig) để chuyển van từ vị trí 0 đến 100%.",
      "The first category of positioners are pneumatic positioners. Legacy processing units may "
      "use pneumatic pressure signaling as the control set point to the control valves. Pressure "
      "is typically modulated between 20.7 to 103 kPa (3 to 15 psig) to move the valve from 0 to "
      "100% position.")
    P("Trong thiết kế bộ định vị khí nén thông thường (Hình 4.1), vị trí của thân hoặc trục van "
      "được so sánh với vị trí của ống mềm (bellows) nhận tín hiệu điều khiển khí nén. Khi tín hiệu "
      "đầu vào tăng, ống mềm giãn ra và dịch chuyển một thanh đòn (beam). Thanh đòn quay quanh trục "
      "đầu vào, đưa cánh chắn (flapper) lại gần vòi phun hơn. Áp suất vòi phun tăng, làm tăng áp "
      "suất đầu ra tới cơ cấu chấp hành qua rơ-le khuếch đại khí nén. Áp suất đầu ra tăng làm thân "
      "van dịch chuyển. Chuyển động thân van được phản hồi về thanh đòn qua cam. Khi cam quay, "
      "thanh đòn quay quanh trục phản hồi để đưa cánh chắn hơi rời vòi phun. Áp suất vòi phun giảm "
      "và áp suất đầu ra tới cơ cấu chấp hành giảm. Thân van tiếp tục dịch chuyển, đưa cánh chắn ra "
      "xa vòi phun cho đến khi đạt cân bằng.",
      "In a common pneumatic positioner design (Figure 4.1), the position of the valve stem or "
      "shaft is compared with the position of a bellows that receives the pneumatic control "
      "signal. When the input signal increases, the bellows expands and moves a beam. The beam "
      "pivots about an input axis, which moves a flapper closer to the nozzle. The nozzle pressure "
      "increases, which increases the output pressure to the actuator through a pneumatic "
      "amplifier relay. The increased output pressure to the actuator causes the valve stem to "
      "move. Stem movement is fed back to the beam by means of a cam. As the cam rotates, the "
      "beam pivots about the feedback axis to move the flapper slightly away from the nozzle. The "
      "nozzle pressure decreases and reduces the output pressure to the actuator. Stem movement "
      "continues, backing the flapper away from the nozzle until equilibrium is reached.")
    FIG(1, F.fig_f4_01())
    P("Khi tín hiệu đầu vào giảm, ống mềm co lại (nhờ lò xo dải bên trong) và thanh đòn quay quanh "
      "trục đầu vào để đưa cánh chắn ra xa vòi phun. Áp suất vòi phun giảm và rơ-le cho phép xả áp "
      "suất vỏ màng ra khí quyển, cho phép thân cơ cấu chấp hành dịch chuyển lên. Qua cam, chuyển "
      "động thân van được phản hồi để định vị lại cánh chắn gần vòi phun hơn. Khi đạt cân bằng, "
      "thân van dừng và cánh chắn được định vị để ngăn áp suất cơ cấu chấp hành giảm thêm.",
      "When the input signal decreases, the bellows contracts (aided by an internal range spring) "
      "and the beam pivots about the input axis to move the flapper away from the nozzle. Nozzle "
      "pressure decreases and the relay permits the release of diaphragm casing pressure to the "
      "atmosphere, which allows the actuator stem to move upward. Through the cam, stem movement "
      "is fed back to the beam to reposition the flapper closer to the nozzle. When equilibrium "
      "conditions are obtained, stem movement stops and the flapper is positioned to prevent any "
      "further decrease in actuator pressure.")
    P("Bộ định vị thiết kế cho ứng dụng hạt nhân, được đánh giá là thiết bị thương mại chuyên dụng "
      "theo chương trình bảo đảm chất lượng 10CFR50, Phụ lục B, dùng vật liệu có hiệu năng vượt "
      "trội ở nhiệt độ và mức bức xạ cao. Vòng chữ O bằng EPDM (ethylene propylene) và màng bằng "
      "EPDM/meta-aramid. EPDM có khả năng nhiệt và tuổi thọ lưu kho vượt trội so với nitrile. Loại "
      "vải màng meta-aramid (nguyên bản viết là <i>diaghragm</i>) giữ độ bền tốt hơn ở nhiệt độ và "
      "điều kiện bức xạ cao.",
      "Positioners designed for nuclear applications, which are qualified commercial-grade "
      "dedicated under 10CFR50, Appendix B, quality assurance program, include materials that "
      "provide superior performance at elevated temperatures and radiation levels. The o-rings "
      "are made of EPDM (ethylene propylene) and the diaphragms are EPDM/meta-aramid. EPDM "
      "demonstrates superior temperature capability and shelf life over nitrile. The meta-aramid "
      "diaghragm fabric demonstrates improved strength retention at elevated temperature and "
      "radiation conditions.")

    # ------------------------------------------------------------ 4.2.2
    H("4.2.2 Bộ định vị I/P tương tự", "4.2.2 Analog I/P Positioners", h3)
    P("Loại thứ hai là bộ định vị I/P tương tự. Hầu hết đơn vị công nghệ hiện đại dùng tín hiệu 4 "
      "đến 20 mA DC để điều biến van điều khiển. Điều này đưa điện tử vào thiết kế bộ định vị và "
      "yêu cầu bộ định vị chuyển tín hiệu dòng điện thành tín hiệu áp suất khí nén (dòng sang khí "
      "nén, hay I/P). Bộ chuyển đổi khí nén kết hợp với bộ chuyển đổi điện-khí nén trở thành bộ "
      "định vị tương tự. Bộ chuyển đổi điện-khí nén tích hợp này có thể lắp tại nhà máy hoặc lắp "
      "tại hiện trường cho bộ định vị hiện hữu. Việc nâng cấp bộ định vị khí nén hiện hữu bằng cách "
      "lắp tại hiện trường bộ chuyển đổi điện-khí nén được thực hiện qua thay đổi cách lắp và dải "
      "tín hiệu đầu vào của bộ định vị.",
      "The second type of positioner is an analog I/P positioner. Most modern processing units "
      "use a 4 to 20 mA DC signal to modulate the control valves. This introduces electronics "
      "into the positioner design and requires that the positioner convert the electronic current "
      "signal into a pneumatic pressure signal (current-to-pneumatic or I/P). The pneumatic "
      "converter in combination with electro-pneumatic converter becomes the analog positioner. "
      "This integral electro-pneumatic converter can be factory installed or installed in the "
      "field on existing positioners. Upgrading an existing pneumatic positioner by field "
      "installation of electro-pneumatic converter by changing the existing positioner mounting "
      "and the input signal range.")
    P("Trong bộ định vị I/P tương tự điển hình (xem Hình 4.2 và 4.3), bộ chuyển đổi nhận tín hiệu "
      "DC đầu vào và tạo tín hiệu đầu ra khí nén tỷ lệ qua cấu trúc vòi phun/cánh chắn. Tín hiệu "
      "đầu ra khí nén cung cấp tín hiệu đầu vào cho bộ định vị khí nén. Ngoài ra, thiết kế giống hệt "
      "bộ định vị khí nén.",
      "In a typical analog I/P positioner (see Figure 4.2 and 4.3), the converter receives a DC "
      "input signal and provides a proportional pneumatic output signal through a nozzle/flapper "
      "arrangement. The pneumatic output signal provides the input signal to the pneumatic "
      "positioner. Otherwise, the design is the same as the pneumatic positioner.")
    FIG(2, F.fig_f4_02())
    FIG(3, F.fig_f4_03())

    # ------------------------------------------------------------ 4.2.3
    H("4.2.3 Bộ điều khiển van số", "4.2.3 Digital Valve Controllers", h3)
    P("Trong khi bộ định vị khí nén và bộ định vị I/P tương tự cung cấp điều khiển vị trí van cơ "
      "bản, bộ điều khiển van số (digital valve controller) thêm một chiều kích mới cho khả năng "
      "của bộ định vị. Loại bộ định vị này là thiết bị dựa trên vi xử lý. Vi xử lý cho phép chẩn "
      "đoán và truyền thông hai chiều, đơn giản hóa thiết lập và khắc phục sự cố.",
      "While pneumatic positioners and analog I/P positioners provide basic valve position "
      "control, digital valve controllers add another dimension to positioner capabilities. This "
      "type of positioner is a microprocessor-based instrument. The microprocessor enables "
      "diagnostics and two-way communication to simplify setup and troubleshooting.")
    P("Trong bộ điều khiển van số điển hình, tín hiệu điều khiển được vi xử lý đọc, xử lý bằng thuật "
      "toán số và chuyển thành tín hiệu dòng dẫn tới bộ chuyển đổi I/P. Vi xử lý thực hiện thuật "
      "toán điều khiển vị trí thay vì cụm thanh đòn, cam và cánh chắn cơ khí. Khi tín hiệu điều "
      "khiển tăng, tín hiệu dẫn tới bộ chuyển đổi I/P tăng, làm tăng áp suất đầu ra từ bộ chuyển "
      "đổi. Áp suất này được dẫn tới rơ-le khuếch đại khí nén và tạo hai áp suất đầu ra cho cơ cấu "
      "chấp hành. Khi tín hiệu điều khiển tăng, một áp suất đầu ra luôn tăng và áp suất còn lại "
      "giảm.",
      "In a typical digital valve controller, the control signal is read by the microprocessor, "
      "processed by a digital algorithm, and converted into a drive current signal to the I/P "
      "converter. The microprocessor performs the position control algorithm rather than a "
      "mechanical beam, cam, and flapper assembly. As the control signal increases, the drive "
      "signal to the I/P converter increases, increasing the output pressure from the I/P "
      "converter. This pressure is routed to a pneumatic amplifier relay and provides two output "
      "pressures to the actuator. With increasing control signal, one output pressure always "
      "increases and the other output pressure decreases.")
    P("Cơ cấu chấp hành tác động kép dùng cả hai đầu ra, trong khi cơ cấu tác động đơn chỉ dùng một "
      "đầu ra. Áp suất đầu ra thay đổi làm thân hoặc trục cơ cấu chấp hành dịch chuyển. Vị trí van "
      "được phản hồi về vi xử lý. Thân van tiếp tục dịch chuyển cho đến khi đạt vị trí đúng; tại đó "
      "vi xử lý ổn định tín hiệu dẫn tới bộ chuyển đổi I/P cho đến khi cân bằng. Hệ thống phản hồi "
      "hiệu năng cao, không liên kết cơ khí, loại bỏ tiếp xúc vật lý giữa thân van và bộ điều khiển "
      "van số. Nhờ đó không có chi tiết chịu mài mòn và tuổi thọ chu kỳ được tối đa. Thiết kế bộ "
      "định vị đáp ứng nhanh với bước thay đổi lớn và điều khiển chính xác cho thay đổi điểm đặt "
      "nhỏ.",
      "Double-acting actuators use both outputs, whereas single-acting actuators use only one "
      "output. The changing output pressure causes the actuator stem or shaft to move. Valve "
      "position is fed back to the microprocessor. The stem continues to move until the correct "
      "position is attained. At this point, the microprocessor stabilizes the drive signal to the "
      "I/P converter until equilibrium is obtained. The high performance, linkage-less feedback "
      "system eliminates physical contact between the valve stem and the digital valve "
      "controller. Hence, there are no wearing parts, so cycle life is maximized. The positioner "
      "design provides quick response to large step changes and precise control for small set "
      "point changes.")
    FIG(4, F.fig_f4_04())

    H("4.2.3.1 Chẩn đoán", "4.2.3.1 Diagnostics", h3)
    P("Vi xử lý bên trong bộ điều khiển van số cho phép bộ định vị chạy, phân tích và lưu trữ các "
      "phép thử chẩn đoán. Thông tin chẩn đoán hữu ích để xác định tình trạng của toàn bộ cụm van "
      "điều khiển. Thông qua cảm biến áp suất, cảm biến nhiệt độ, cảm biến hành trình và các chỉ số "
      "nội bộ, biểu đồ thể hiện hiệu năng và tình trạng của van được tạo ra và các hành động được "
      "đề xuất được trình bày. Thông tin này được dùng để xác định những thành phần của cụm van có "
      "thể cần bảo trì. Các chẩn đoán này cho phép giám sát tình trạng và hiệu năng của toàn bộ cụm "
      "van ngay khi van đang điều khiển quá trình. Bộ điều khiển van số dùng thuật toán thống kê để "
      "xác định các vấn đề liên quan đến tình trạng và hiệu năng dựa trên chỉ số trực tiếp từ cảm "
      "biến. Nó cũng cho phép truy cập thử nghiệm động toàn hành trình của cụm van, gồm đường chữ "
      "ký van, dải lỗi động, đáp ứng bước và thời gian hành trình.",
      "The microprocessor inside the digital valve controller allows the positioner to run, "
      "analyze, and store diagnostic tests. Diagnostic information is useful in determining the "
      "health of the entire control valve assembly. Through the use of pressure sensors, "
      "temperature sensors, travel sensors, and internal readings, graphical representations of "
      "control valve performance and health are created and recommended actions are presented. "
      "This information is then used to identify elements of the control valve assembly that may "
      "require maintenance. These diagnostics enable condition and performance monitoring of the "
      "entire valve assembly while the valve is actively controlling the process. The digital "
      "valve controller uses statistical algorithms to determine the conditions and performance "
      "related issues based on live readings from the sensors. It also provides access to "
      "full-stroke dynamic testing of the valve assembly, including valve signature, dynamic "
      "error band, step response, and stroke time.")

    H("4.2.3.2 Truyền thông số hai chiều", "4.2.3.2 Two-Way Digital Communication", h3)
    P("Vi xử lý bên trong bộ điều khiển van số cũng cho phép bộ định vị truyền thông với hệ thống "
      "điều khiển qua tín hiệu số. Điều này cho phép bộ điều khiển van số cung cấp phản hồi bổ sung, "
      "như hành trình van thực tế và cảnh báo chẩn đoán, về hệ thống điều khiển.",
      "The microprocessor inside the digital valve controller also allows the positioner to "
      "communicate with the control system via a digital signal. This enables the digital valve "
      "controller to provide additional feedback, such as actual valve travel and diagnostic "
      "alerts back to the control system.")
    P("Một giao thức được dùng rộng rãi là truyền thông HART®. Truyền thông HART dùng tín hiệu số "
      "chồng lên tín hiệu điều khiển 4 đến 20 mA DC truyền thống. Giao thức này cho phép hệ thống "
      "chủ được dùng để cấu hình, hiệu chuẩn và giám sát tình trạng của bộ định vị. Truyền thông "
      "HART mang lại lợi ích của truyền thông số với sự quen thuộc của hệ thống điều khiển 4 đến "
      "20 mA. HART cho phép người dùng đưa nhanh vòng điều khiển vào vận hành bằng nhiều công cụ, "
      "tại cụm van hoặc từ xa.",
      "One widely used protocol is HART® communication. HART communication uses a digital signal "
      "superimposed over the traditional 4 to 20 mA DC control signal. This communication "
      "protocol allows the host system to be used to configure, calibrate, and monitor the health "
      "of the positioner. HART communication offers the benefits of digital communication with "
      "the familiarity of a 4 to 20 mA control system. HART communication allows the user to "
      "quickly commission loops with a variety of tools, either locally at the valve assembly or "
      "remotely.")
    P("FOUNDATION™ fieldbus là một giao thức chuẩn ngành khác. Giao thức này hoàn toàn số, nghĩa là "
      "tín hiệu điều khiển (điểm đặt) là số thay vì dòng 4 đến 20 mA DC. Tương tự truyền thông "
      "HART, hệ thống chủ cũng có thể dùng để cấu hình, hiệu chuẩn và giám sát bộ định vị. "
      "PROFIBUS cũng là giao thức công nghiệp phổ biến cung cấp truyền thông hoàn toàn số. Lớp vật "
      "lý của PROFIBUS và FOUNDATION fieldbus giống nhau; tuy nhiên giao thức truyền thông khác "
      "nhau và có ưu điểm riêng. Công nghệ không dây cung cấp cách bổ sung để truyền thông tin giữa "
      "hệ thống điều khiển và bộ điều khiển van số. Với bộ định vị được trang bị khả năng không "
      "dây, thông tin số có thể được truyền độc lập với dây dẫn của hệ thống điều khiển.",
      "FOUNDATION™ fieldbus is another industry standard protocol. This protocol is all digital, "
      "which means that the control signal (set point) is digital, rather than a 4 to 20 mA DC "
      "current. Similar to HART communication, the host system can also be used to configure, "
      "calibrate, and monitor the positioner. PROFIBUS is also a common industry protocol that "
      "provides all digital communication. The physical layer for PROFIBUS and FOUNDATION fieldbus "
      "is the same; however, the communication protocols differ and offer their own advantages. "
      "Wireless technology offers an additional method to communicate information between the "
      "control system and the digital valve controller. For positioners outfitted with wireless "
      "capability, digital information can be transmitted independent of the control system "
      "wiring.")

    # ------------------------------------------------------------ 4.3
    H("4.3 Bộ chuyển đổi I/P", "4.3 I/P Transducers")
    P("Trong một số ứng dụng, độ chính xác định vị cao mà bộ định vị cung cấp là không cần thiết. "
      "Trong các ứng dụng đó, có thể dùng bộ chuyển đổi điện-khí nén (I/P) (Hình 4.6). Bộ chuyển "
      "đổi I/P dùng mô-đun chuyển đổi đầu vào dòng 4 đến 20 mA thành đầu ra áp suất tỷ lệ. Rơ-le "
      "khuếch đại khí nén bên trong cung cấp năng lực cần thiết để đưa áp suất đầu ra tới cơ cấu "
      "chấp hành van điều khiển. Không có phản hồi vị trí van và đáp ứng rất nhanh.",
      "In some applications, the high level of postioning accuracy that a positioner provides is "
      "not required. In these applications, an electro-pneumatic (I/P) transducer can be used. An "
      "I/P transducer (Figure 4.6) uses a converter module that converts a 4 to 20 mA current "
      "input to a proportional pressure output. An internal pneumatic amplifier relay provides "
      "the capacity necessary to deliver output pressure to the control valve actuator. There is "
      "no valve position feedback and responsiveness is very quick.")
    P("Bộ chuyển đổi có thiết kế thanh chắn/vòi phun (deflector/nozzle) (Hình 4.5) gồm hai vòi phun "
      "được bố trí sao cho dòng khí không đổi thoát ra từ vòi phun cấp được hướng vào miệng vòi phun "
      "nhận. Tín hiệu dòng đầu vào định vị một thanh chắn trong dòng chảy giữa hai vòi. Khi tín hiệu "
      "thay đổi, thanh chắn dịch chuyển để làm đổi dòng chảy tới vòi phun nhận, thiết lập áp suất "
      "thử (pilot pressure) tại vòi phun nhận. Áp suất thử này lần lượt điều khiển cấp khuếch đại và "
      "đầu ra của bộ chuyển đổi.",
      "The transducer includes a deflector / nozzle design (Figure 4.5) that consists of two "
      "nozzles positioned so that the constant air flow exiting the supply nozzle is directed at "
      "the entrance of the receiver nozzle. The input current signal positions a deflector bar "
      "within the nozzles flow stream. As the input signal changes, the deflector bar moves to "
      "alter the flow stream to the receiver nozzle, establishing a pilot pressure at the "
      "receiver nozzle. The pilot pressure, in turn, controls the booster stage and output of the "
      "transducer.")
    FIG(5, F.fig_f4_05())
    FIG(6, F.fig_f4_06())
    P("Mạng điều khiển phản hồi điện tử liên tục so sánh giá trị tín hiệu đầu ra khí nén với tín "
      "hiệu dòng đầu vào. Cảm biến áp suất thể rắn là một phần của gói điện tử giám sát đầu ra khí "
      "nén. Mạch so sánh trong mạng điều khiển phát hiện sai lệch đầu vào-đầu ra và điều chỉnh đầu "
      "ra bằng cách đưa thanh chắn trong cấp thử đến vị trí đã hiệu chỉnh. Nhờ mạng phản hồi này, "
      "bộ chuyển đổi có thể hiệu chỉnh các ảnh hưởng gây sai số như biến đổi áp suất cấp và rò rỉ "
      "phía sau.",
      "An electronic feedback control network constantly compares the value of the pneumatic "
      "output signal with the input current signal. A solid-state pressure sensor is part of the "
      "electronics package monitoring the pneumatic output. A comparator circuit in the control "
      "network detects input-output deviations and adjusts the output by moving the deflector in "
      "the pilot stage to a corrected position. Because of this feedback network, the transducer "
      "can correct for error-producing effects such as variations in supply pressure and "
      "downstream leakage.")
    P("Bộ chuyển đổi dùng cho dịch vụ hạt nhân, được đánh giá là thiết bị thương mại chuyên dụng "
      "theo chương trình bảo đảm chất lượng 10CFR50, Phụ lục B, dùng vòng chữ O EPDM và màng "
      "EPDM/Nomex có hiệu năng vượt trội và giữ độ bền tốt ở nhiệt độ và bức xạ cao. EPDM bị thoái "
      "hóa khi tiếp xúc dầu bôi trơn gốc dầu mỏ. Vì vậy, nên dùng nguồn khí sạch, khô và không dầu "
      "với thiết bị chứa linh kiện EPDM.",
      "Transducers for nuclear service which are qualified commercial grade dedicated under "
      "10CFR50, Appendix B, quality assurance program employs EPDM o-rings and EPDM/Nomex "
      "diaphragms that provide superior performance and demonstrates improved strength retention "
      "at elevated temperatures and radiation conditions. EPDM is subjected to degradation when "
      "exposed to petroleum-based lubricants. So, it is recommended to use clean, dry, and oil "
      "free air supply with instruments containing EPDM components.")

    # ------------------------------------------------------------ 4.4
    H("4.4 Bộ tăng thể tích", "4.4 Volume Boosters")
    P("Bộ định vị và bộ chuyển đổi I/P được thiết kế để cung cấp năng lực đầu ra khí nén đủ cho van "
      "điều khiển tiết lưu điển hình. Tuy nhiên, một số ứng dụng yêu cầu tốc độ hành trình nhanh "
      "hơn. Khi thể tích cơ cấu chấp hành lớn, tốc độ đáp ứng của việc định vị trở nên đáng lo "
      "ngại hơn.",
      "Positioners and I/P transducers are designed to provide enough pneumatic output capacity "
      "to drive a typical throttling control valve. However, some applications require faster "
      "stroking speeds. When the actuator volume is large, the positioning speed of response can "
      "become more of a concern.")
    P("Bộ tăng thể tích (volume booster) giải quyết vấn đề bằng cách khuếch đại đầu ra từ bộ định "
      "vị van để tăng tốc độ hành trình của cơ cấu chấp hành. Bộ tăng thể tích cung cấp năng lực "
      "đầu ra khí nén bổ sung cho cụm van (Hình 4.7). Một thay đổi lớn, đột "
      "ngột của tín hiệu đầu vào (áp suất đầu ra từ bộ định vị) tạo chênh áp giữa tín hiệu đầu vào "
      "và đầu ra của bộ tăng. Khi đó, các màng dịch chuyển để mở cổng cấp hoặc cổng xả, tùy tác "
      "động cần thiết để giảm chênh áp. Cổng giữ mở cho đến khi chênh áp giữa đầu vào và đầu ra của "
      "bộ tăng nằm trong giới hạn vùng chết (deadband) của bộ tăng.",
      "Volume boosters solve the issue by amplifying the output from valve positioners to "
      "increase the stroking speed of actuators. Volume boosters are used to provide additional "
      "pneumatic output capacity to a valve assembly (Figure 4.6, here Figure 4.7). A large, "
      "sudden change in input signal (output pressure from the positioner) causes a pressure "
      "differential to exist between the input signal and the output of the booster. When this "
      "occurs, the diaphragms move to open the supply port or the exhaust port, whichever action "
      "is required to reduce the differential. The port remains open until the difference between "
      "the booster input and output pressure is within the deadband limit of the booster.")
    FIG(7, F.fig_f4_07())
    P("Các bộ tăng có vùng chết cố định, kết cấu chỗ ngồi mềm và phụ tùng bypass tích hợp. Với "
      "tiết lưu bypass được chỉnh để vận hành ổn định, các tín hiệu có biên độ và tốc độ thay đổi "
      "nhỏ đi qua tiết lưu bypass vào cơ cấu chấp hành mà không kích hoạt bộ tăng. Cả cổng cấp và "
      "cổng xả đều giữ đóng, ngăn tiêu thụ khí không cần thiết và khả năng bão hòa rơ-le bộ định "
      "vị. Van xả và van cấp có chỗ ngồi mềm tạo độ kín bọt khí, giảm tiêu thụ khí không cần thiết "
      "và bảo đảm chế độ an toàn khi mất khí nhà máy. Bộ trim xả giảm tiếng ồn tiêu chuẩn cho phép "
      "xả khí nhanh và êm từ cơ cấu chấp hành.",
      "The boosters incorporate fixed deadband, soft seat construction, and integral bypass "
      "fitting. With the bypass restriction adjusted for stable operation, signals having small "
      "magnitude and rate changes pass through the bypass restriction and into the actuator "
      "without initiating booster operation. Both the supply and exhaust ports remain closed, "
      "preventing unnecessary air consumption and possible saturation of positioner relays. Soft "
      "seated exhaust and supply valves provide for bubble tight shutoff to reduce unnecessary "
      "air consumption and ensure fail mode upon loss of plant air. The standard noise "
      "attenuating exhaust trim allows air to be exhausted quickly and quietly from the "
      "actuator.")
    P("Cơ cấu chấp hành tác động đơn thường dùng một bộ tăng thể tích. Cơ cấu tác động kép cần ít "
      "nhất hai bộ tăng, một cho mỗi phía của piston (Hình 4.8). Một số ứng dụng, như chống đua "
      "máy nén hoặc đường vòng tua-bin, có thể cần thêm bộ tăng để cung cấp thể tích khí cần thiết "
      "cho đáp ứng nhanh của van. Nhiều phụ kiện có thể nối trực tiếp vào bộ tăng, loại bỏ đoạn "
      "ống dài và đơn giản hóa sơ đồ đấu dây tổng thể để bảo trì tại hiện trường dễ dàng.",
      "Single-acting actuators typically use one volume booster. Double-acting actuators require "
      "at least two volume boosters, one to feed each side of the actuator piston. (Figure 4.8) "
      "Some applications, such as compressor anti-surge or turbine bypass, may require additional "
      "volume boosters to provide the needed pneumatic volume for fast valve response. Multiple "
      "accessories can be connected directly to the booster, eliminating long lengths of tubing, "
      "and simplifying the overall hookup schematic for easy field maintenance.")
    FIG(8, F.fig_f4_08())

    # ------------------------------------------------------------ 4.5
    H("4.5 Hệ thống an toàn bằng dụng cụ (SIS)",
      "4.5 Safety Instrumented Systems (SIS)")
    P("Mục đích chính của van điều khiển là điều biến dòng chất lỏng hoặc khí trong đường ống trong "
      "vòng điều khiển quá trình. Trong cùng các vòng này cũng có van thông hơi, van chặn hoặc van "
      "cô lập khẩn cấp. Các van này thường là van đóng/mở dùng để đưa vòng quá trình về trạng thái "
      "an toàn khi có sự cố điều khiển (Hình 4.9). Một hệ thống an toàn riêng biệt, thường do bộ "
      "giải logic điều khiển, điều khiển các van này.",
      "The primary purpose of a control valve is to modulate the flow of liquid or gas in a pipe "
      "within a process control loop. Within these same process loops, there are also emergency "
      "vent, block, or isolation valves. These valves are typically on/off valves that are used "
      "to take the process loop to a safe state in the event of a process control emergency "
      "(Figure 4.9). A separate safety system, often controlled by a logic solver, controls these "
      "valves.")
    FIG(9, F.fig_f4_09())

    H("4.5.1 Thử hành trình một phần", "4.5.1 Partial Stroke Testing", h3)
    P("Vì van an toàn tĩnh và không điều biến trong điều kiện bình thường, chúng dễ bị kẹt. Khi có "
      "yêu cầu khẩn cấp, tồn tại rủi ro là van không dịch chuyển khi được lệnh. Để giảm rủi ro này, "
      "có thể dùng bộ điều khiển van số như thiết bị thử hành trình một phần. Chức năng quan trọng "
      "của thiết bị là định kỳ vận hành van. Điều này được thực hiện bằng phép thử hành trình một "
      "phần (partial stroke test - PST). PST dịch chuyển van chậm một phần của tổng hành trình rồi "
      "trở về trạng thái bình thường. Phép thử này vận hành các thành phần cơ khí của van an toàn "
      "với sự gián đoạn tối thiểu cho vòng quá trình. Hơn nữa, bộ điều khiển van số có khả năng "
      "chẩn đoán sự cố tiềm ẩn và truyền bất kỳ cảnh báo nào nếu phép thử thất bại.",
      "Because safety valves are static and do not modulate under normal conditions, they are "
      "prone to sticking. When an emergency demand occurs, there is a risk that the valves will "
      "not move when commanded. To mitigate this risk, the digital valve controller can be used "
      "as a partial stroke testing device. An important function of the instrument is "
      "periodically exercising the valve. This is performed with a valve partial stroke test "
      "(PST). The PST slowly moves the valve a portion of the total valve travel and then returns "
      "to the normal state. This exercises the mechanical components of the safety valve with "
      "minimal disruption to the process loop. Furthermore, the digital valve controller has the "
      "ability to diagnose potential issues and communicate any alerts if the test fails.")

    H("4.5.2 Chức năng an toàn và chứng nhận sản phẩm",
      "4.5.2 Safety Function and Product Certification", h3)
    P("Cơ cấu chấp hành tác động đơn có lò xo hồi vị cung cấp chế độ an toàn cố hữu cho cụm van. "
      "Trong yêu cầu khẩn cấp, cách thông thường để đưa van về trạng thái an toàn là xả áp suất khí "
      "khỏi cơ cấu chấp hành và để lò xo định vị van. Có thể dùng van điện từ và/hoặc bộ điều khiển "
      "van số để thực hiện chức năng này. Có thể có thêm thiết bị trên van an toàn, như bộ tăng, bộ "
      "phát vị trí và hệ thống ngắt. Tất cả các yếu tố này phải được đánh giá về ảnh hưởng của "
      "chúng đối với hệ thống an toàn. Các yếu tố này có thể hỏng bằng cách gây ngắt ngoài kế hoạch "
      "hoặc bằng cách không đưa van an toàn về trạng thái an toàn. Phân tích Chế độ hỏng, Ảnh hưởng "
      "và Chẩn đoán (FMEDA) cung cấp chỉ số cho từng thành phần. Điều này cho phép kỹ sư an toàn "
      "thiết kế hệ thống an toàn bằng dụng cụ ở mức giảm rủi ro mong muốn. Xem Chương 12 để biết "
      "thêm thông tin về hệ thống an toàn bằng dụng cụ.",
      "A spring-return, single-acting actuator provides an inherent fail mode for the valve "
      "assembly. During an emergency demand, the typical method to move the valve to the safe "
      "state is to remove the air pressure to the actuator and allow the spring to position the "
      "valve. A solenoid valve and/or digital valve controller can be used to perform this "
      "function. There may be additional instrumentation on the safety valve, such as boosters, "
      "position transmitters, and trip systems. All of these elements must be evaluated for their "
      "effect on the safety system. These elements can fail by causing an unplanned trip or by not "
      "getting the safety valve to the safe state. The Failure Modes, Effects, and Diagnostics "
      "Analysis (FMEDA) provides metrics for each component. This allows a safety engineer to "
      "design the safety instrumented system to the desired level of risk reduction. See Chapter "
      "12 for more information about safety instrumented systems.")

    # ------------------------------------------------------------ 4.6
    H("4.6 Van số tối ưu", "4.6 Optimized Digital Valves")
    P("Gói Van số tối ưu (Optimized Digital Valve - ODV) được dùng để đáp ứng hiệu năng động "
      "nghiêm ngặt và yêu cầu về thời gian hành trình. Van nhanh và chính xác hơn nói chung cho "
      "phép hiệu suất cao hơn, mang lại tiết kiệm chi phí lớn hơn cho người dùng cuối. Được thử "
      "nghiệm kỹ và thiết kế để giảm rung bằng phanh khí và xi lanh đệm, ODV cải thiện hiệu năng "
      "động nhờ bộ lọc đầu vào lead-lag, tăng lead-lag và điều khiển áp suất đầu cuối.",
      "Optimized Digital Valve (ODV) packages are used to meet stringent dynamic performances as "
      "well as stroking time requirements. Faster and more accurate valves generally allow for "
      "higher efficiencies resulting in greater cost savings to the end-user. Thoroughly tested "
      "and designed to reduce vibration by using air brake and cushioned cylinder, ODV improves "
      "the dynamic performances by using lead-lag input filter, lead-lag boost, and end-point "
      "pressure control.")

    # ------------------------------------------------------------ 4.7
    H("4.7 Bộ điều khiển", "4.7 Controllers")
    P("Trong một số ứng dụng, quá trình được điều khiển tại chỗ mà không cần hệ thống điều khiển "
      "phân tán (DCS) hoặc bộ điều khiển logic lập trình (PLC) quy mô lớn. Bộ điều khiển tại chỗ "
      "được dùng để đo điều kiện quá trình như áp suất, nhiệt độ hoặc mức và trực tiếp dẫn áp suất "
      "khí nén đầu ra tới van điều khiển (Hình 4.10). Đầu vào của bộ điều khiển tại chỗ thường là "
      "áp suất, áp suất chênh, nhiệt độ hoặc dịch chuyển mức. Phép đo quá trình được chuyển thành "
      "chuyển động của cụm thanh-cánh chắn nối với phần tử đầu vào. Phần tử đầu vào có thể là ống "
      "Bourdon, cụm ống mềm, cụm cần dịch chuyển chất lỏng hoặc bầu nhiệt.",
      "In some applications, control of the process is performed locally without the need for a "
      "large scale distributed control system (DCS) or programmable logic controller (PLC). Local "
      "controllers are used to measure process conditions, such as pressure, temperature, or level "
      "and directly drive the pneumatic output pressure to a control valve (Figure 4.10). The "
      "input to the local controller is typically pressure, differential pressure, temperature, or "
      "level displacement. The process measurement is translated into a beam-flapper assembly "
      "movement, which is connected to an input element. The input element can be a Bourdon tube, "
      "bellows assembly, liquid displacement lever assembly, or temperature bulb.")
    FIG(10, F.fig_f4_10())
    P("Phần tử đầu vào được nối với kim quá trình (điều chỉnh điểm đặt) và với cánh chắn qua các "
      "liên kết. Khi đầu vào quá trình tăng (trong bộ điều khiển tác động trực tiếp), cánh chắn "
      "tiến về phía vòi phun, hạn chế dòng qua vòi phun và tăng áp suất vòi phun. Rơ-le khi đó "
      "tăng áp suất đầu ra tới cơ cấu chấp hành, làm van điều khiển điều biến. Áp suất đầu ra được "
      "phản hồi về ống mềm tỷ lệ. Tác động của ống mềm tỷ lệ đối kháng với chuyển động cánh chắn do "
      "thay đổi đầu vào quá trình, rồi đưa cánh chắn ra xa vòi phun cho đến khi bộ điều khiển đạt "
      "cân bằng. Việc chỉnh điểm đặt làm thay đổi độ gần của vòi phun và cánh chắn, cũng như thay "
      "đổi đầu vào quá trình; tuy nhiên khi điểm đặt thay đổi thì vòi phun dịch chuyển so với cánh "
      "chắn.",
      "The input element is connected to the process pointer (set point adjustment) and to the "
      "flapper by connecting links. As the process input increases (in a direct-acting "
      "controller), the flapper moves toward the nozzle, which restricts flow through the nozzle "
      "and increases nozzle pressure. When this occurs, relay action increases the output pressure "
      "to the actuator, which modulates the control valve. Output pressure is fed back to the "
      "proportional bellows. The action of the proportional bellows counters the flapper movement "
      "that resulted from the process input change. It then moves the flapper away from the nozzle "
      "until the controller reaches a point of equilibrium. The set point adjustment changes the "
      "proximity of the nozzle and flapper, as does a change in process input. However, when the "
      "set point is changed, the nozzle moves with respect to the flapper.")
    P("Núm chỉnh dải tỷ lệ định vị vòi phun trên cánh chắn. Tăng hoặc mở rộng dải tỷ lệ dịch vòi "
      "phun đến vị trí trên cánh chắn nơi có ít chuyển động hơn, làm giảm hệ số khuếch đại của bộ "
      "điều khiển. Giảm hoặc thu hẹp dải tỷ lệ dịch vòi phun về vị trí có nhiều chuyển động hơn, làm "
      "tăng hệ số khuếch đại. Tác động của bộ điều khiển đổi từ trực tiếp sang ngược bằng cách xoay "
      "núm chỉnh dải tỷ lệ để định vị vòi phun tại điểm trên cánh chắn mà tại đó chiều chuyển động "
      "cánh chắn so với chuyển động đầu vào bị đảo ngược. Ở chế độ tác động ngược, tăng đầu vào "
      "quá trình làm giảm áp suất đầu ra tới cơ cấu chấp hành. Áp suất cấp rỉ qua một lỗ cố định "
      "trong rơ-le và thoát qua vòi phun. Áp suất vòi phun tác động lên màng rơ-le lớn và điều biến "
      "áp suất tải trên màng rơ-le nhỏ, từ đó điều biến áp suất đầu ra của bộ điều khiển tới cơ cấu "
      "chấp hành (Hình 4.11).",
      "The proportional band adjustment knob positions the nozzle on the flapper. Increasing or "
      "widening the proportional band moves the nozzle to a position on the flapper where less "
      "flapper motion occurs, decreasing the gain of the controller. Decreasing or narrowing the "
      "proportional band moves the nozzle toward a position where more flapper motion occurs, "
      "increasing the gain. Controller action is changed from direct to reverse by turning the "
      "proportional band adjustment knob to position the nozzle to a point on the flapper where "
      "the direction of the flapper motion versus the input motion is reversed. With the "
      "controller in the reverse-acting mode, an increase in process input causes a decrease in "
      "output pressure to the actuator. Supply pressure bleeds through a fixed orifice in the "
      "relay and exits through the nozzle. The nozzle pressure registers on the large relay "
      "diaphragm and modulates loading pressure on the small relay diaphragm. This also modulates "
      "the controller output pressure to the actuator (Figure 4.11).")
    FIG(11, F.fig_f4_11())
    P("Bộ điều khiển có tác động tỷ lệ cộng tích phân (proportional-plus-reset) tương tự bộ điều "
      "khiển chỉ tỷ lệ, khác ở chỗ áp suất đầu ra được phản hồi về cả ống mềm tích phân và ống mềm "
      "tỷ lệ. Khi vận hành, bộ điều khiển tỷ lệ cộng tích phân giảm thiểu độ lệch giữa biến quá "
      "trình và điểm đặt. Bộ điều khiển có tác động tỷ lệ cộng tích phân cộng vi phân "
      "(proportional-plus-reset-plus-rate) có van tốc độ (rate valve), một tiết lưu có thể chỉnh "
      "duy trì ngắn hệ số khuếch đại để tăng tốc tác động hiệu chỉnh cho hệ thống chậm (Hình 4.12). "
      "Tác động vi phân trì hoãn việc giảm hệ số khuếch đại vừa đủ để hệ thống đáp ứng với thay "
      "đổi, nhưng không đủ dài để hệ thống mất ổn định. Sau đó, hệ số khuếch đại thấp do tác động "
      "tỷ lệ giữ hệ thống ổn định. Cuối cùng, tác động tích phân tăng dần hệ số khuếch đại và đưa "
      "quá trình trở về điểm đặt.",
      "Controllers with proportional-plus-reset operation are similar to that of "
      "proportional-only controllers, except that output pressure is fed back to the reset and "
      "proportional bellows. In operation, proportional-plus-reset controllers minimize the "
      "offset between the process variable and the set point. Controllers with "
      "proportional-plus-reset-plus-rate have a rate valve, an adjustable restriction that "
      "briefly maintains the controller gain to accelerate the corrective action for slow systems "
      "(Figure 4.12). The rate action delays the gain reduction just long enough to allow the "
      "system to respond to the change, but not long enough for the system to become unstable. "
      "Then, the low gain provided by the proportional action keeps the system stable. Finally, "
      "the reset action slowly increases the gain and returns the process toward the set point.")
    FIG(12, F.fig_f4_12())
    P("Chống bão hòa tích phân (anti-reset windup) giảm vượt quá của đầu vào quá trình có thể do "
      "sai lệch lớn hoặc kéo dài so với điểm đặt. Tùy chọn này có thể được chỉnh để tác động khi áp "
      "suất đầu ra tăng hoặc giảm. Van xả chênh áp hoạt động khi chênh áp giữa áp suất ống mềm tỷ "
      "lệ và áp suất ống mềm tích phân đạt một giá trị định trước.",
      "Anti-reset windup reduces overshoot of the process input that can result from large or "
      "prolonged deviation from the set point. This option can be adjusted to operate on either "
      "increasing or decreasing output pressure. The differential relief valve operates when the "
      "difference between proportional bellows pressure and reset bellows pressure reaches a "
      "predetermined value.")

    H("4.7.1 Bộ điều khiển áp suất chênh", "4.7.1 Differential Pressure Controllers", h3)
    P("Bộ điều khiển chỉ thị áp suất chênh hiển thị áp suất chênh của quá trình và điểm đặt trên "
      "thang đo dễ đọc. Các bộ điều khiển này cảm nhận hai áp suất khác nhau và so sánh hiệu giữa "
      "chúng với điểm đặt do người vận hành chỉnh. Sau đó, tín hiệu khí nén được gửi tới phần tử "
      "điều khiển để đưa áp suất chênh của quá trình về phía điểm đặt.",
      "The differential pressure indicating controllers show process differential pressure and "
      "set point on an easy-to-read process scale. The controllers sense two different pressures "
      "and compare the difference between these pressures with an operator-adjusted set point. A "
      "pneumatic signal is then delivered to a control element to change the process differential "
      "pressure toward the set point.")

    H("4.7.2 Bộ điều khiển chỉ thị áp suất đo",
      "4.7.2 Gauge Pressure Indicating Controllers", h3)
    P("Bộ điều khiển chỉ thị áp suất đo hiển thị áp suất quá trình và điểm đặt trên thang đo dễ "
      "đọc. Các bộ điều khiển này so sánh áp suất quá trình với điểm đặt do người vận hành chỉnh "
      "và gửi tín hiệu khí nén tới phần tử điều khiển để áp suất quá trình thay đổi về phía điểm "
      "đặt.",
      "Gauge pressure indicating controllers show process pressure and set point on an "
      "easy-to-read process scale. The controllers compare process pressure with an "
      "operator-adjusted set point and delivers a pneumatic signal to a control element so that "
      "process pressure changes toward the set point.")

    H("4.7.3 Bộ điều khiển chỉ thị nhiệt độ",
      "4.7.3 Temperature Indicating Controllers", h3)
    P("Bộ điều khiển chỉ thị nhiệt độ hiển thị nhiệt độ quá trình và điểm đặt trên thang đo dễ đọc. "
      "Chúng được dùng trong các ngành yêu cầu giám sát và điều khiển nhiệt độ chính xác. Bầu nhiệt "
      "đo nhiệt độ quá trình. Bộ điều khiển nhiệt độ sau đó so sánh nhiệt độ quá trình với điểm "
      "đặt do người vận hành chỉnh và gửi tín hiệu khí nén tới phần tử điều khiển. Phần tử điều "
      "khiển thay đổi nhiệt độ quá trình về phía điểm đặt.",
      "Temperature indicating controllers show process temperature and set point on an "
      "easy-to-read process scale. The controllers are used in industries requiring accurate "
      "process monitoring and temperature control. A temperature bulb measures process "
      "temperature. The temperature controller then compares process temperature with an "
      "operator-adjusted set point. The controller delivers a pneumatic signal to a control "
      "element. The control element changes the process temperature toward the set point.")

    # ------------------------------------------------------------ 4.8
    H("4.8 Bộ phát vị trí", "4.8 Position Transmitters")
    P("Mục đích của bộ phát vị trí là cung cấp phản hồi vị trí van độc lập cho hệ thống điều khiển. "
      "Phản hồi vị trí thường được dùng để giám sát quá trình, khắc phục sự cố hoặc kiểm tra "
      "khởi động/dừng. Bộ phát vị trí được lắp trực tiếp vào van và đo vị trí của thân hoặc trục "
      "van. Trong lắp đặt có dây, bộ phát vị trí cung cấp tín hiệu 4 đến 20 mA tương ứng với dải "
      "tiết lưu của van điều khiển. Trong lắp đặt không dây, bộ phát vị trí cung cấp tín hiệu số 0 "
      "đến 100% (Hình 4.13).",
      "The purpose of a position transmitter is to provide independent valve position feedback to "
      "the control system. Position feedback is often used for process monitoring, "
      "troubleshooting, or startup/shutdown verification. The position transmitter is mounted "
      "directly to the valve and measures the position of the valve stem or shaft. In a wired "
      "installation, the position transmitter provides a 4 to 20 mA signal that corresponds with "
      "the throttling range of the control valve. In a wireless installation, the position "
      "transmitter provides a 0 to 100% digital signal (Figure 4.13).")
    FIG(13, F.fig_f4_13())

    # ------------------------------------------------------------ 4.9
    H("4.9 Công tắc hành trình", "4.9 Limit Switches")
    P("Mục đích của công tắc hành trình là cung cấp tín hiệu đóng hoặc mở rời rạc cho hệ thống "
      "điều khiển khi van đạt một vị trí xác định trong dải hành trình. Công tắc hành trình cũng "
      "được dùng để giám sát quá trình, khắc phục sự cố hoặc kiểm tra khởi động/dừng. Công tắc "
      "nhận phản hồi vị trí từ thân hoặc trục van và gửi tín hiệu có dây hoặc không dây tới hệ "
      "thống điều khiển. Có nhiều công nghệ công tắc khác nhau, như cảm ứng gần (proximity), thể "
      "rắn, từ tính và đóng tiếp điểm.",
      "The purpose of a limit switch is to provide a discrete open or close signal to the control "
      "system when the valve reaches a specific position within its range of travel. Limit "
      "switches are also used for process monitoring, troubleshooting, or startup/shutdown "
      "verification. The limit switch receives position feedback from the valve stem or shaft and "
      "will send either a wired or a wireless signal to the control system. There are many "
      "different switch technologies available, such as proximity, solid state, magnetic, and "
      "contact closure.")

    # ------------------------------------------------------------ 4.10
    H("4.10 Van điện từ", "4.10 Solenoid Valves")
    P("Van điện từ được lắp trên đường ống khí nén dẫn tới cơ cấu chấp hành. Trong một số ứng dụng, "
      "van điện từ xả khí khỏi cơ cấu chấp hành để van chuyển về trạng thái mất khí an toàn. Trong "
      "ứng dụng khác, van điện từ giữ khí trong cơ cấu chấp hành để khóa van ở vị trí hiện tại. "
      "Van điện từ ba chiều thường được dùng cho cơ cấu chấp hành hồi vị bằng lò xo; van điện từ "
      "bốn chiều thường dùng cho cơ cấu tác động kép. Van điện từ được kích hoạt bằng cách đóng "
      "hoặc cắt một tín hiệu điện rời rạc từ hệ thống điều khiển.",
      "A solenoid valve is installed in the pneumatic tubing path to the actuator. In some "
      "applications, the solenoid valve will vent the air from the actuator to allow the valve to "
      "move to its no air, fail state. In other applications, the solenoid valve will trap air in "
      "the actuator to lock the valve in its current position. Three-way solenoids are generally "
      "used to operate spring-return actuators and four-way solenoids are generally used for "
      "double-acting actuators. The solenoid valve is activated by making or breaking a discrete "
      "electrical signal from the control system.")
    P("Van điều khiển bằng điện từ (solenoid-operated valve - SOV) là van đóng/mở điện từ được "
      "điều khiển bằng tín hiệu điện rời rạc từ hệ thống điều khiển. Trong ứng dụng điều khiển quá "
      "trình, SOV thường được dùng để cấp áp hoặc xả áp cho cơ cấu chấp hành đóng/mở. SOV ba chiều "
      "dùng cho cơ cấu hồi vị bằng lò xo và SOV bốn chiều dùng cho cơ cấu tác động kép (xem Hình "
      "4.14 và 4.15).",
      "A solenoid-operated valve (SOV) is an on/off electro-magnetic valve that is controlled by "
      "a discrete electrical signal from a control system. In process control applications, SOVs "
      "are generally used to pressurize or de-pressurize on/off actuators. A three-way SOV is used "
      "for spring return actuator applications and a four-way SOV is used for double-acting "
      "actuator applications (see Figures 14.14 and 14.15 (here Figures 4.14 and 4.15)).")
    FIG(14, F.fig_f4_14())
    FIG(15, F.fig_f4_15())
    P("Ứng dụng van điều khiển thường dùng van điện từ giữa bộ điều khiển van số và van điều khiển "
      "(Hình 4.16). SOV giữ trạng thái được cấp điện trong khi van điều khiển "
      "đang được bộ điều khiển van số điều khiển. Tín hiệu khí nén của bộ điều khiển van số đi qua "
      "SOV trong vận hành bình thường. SOV được bố trí để cho phép đóng nhanh van điều khiển độc "
      "lập với bộ điều khiển van số. Van điều khiển có thể đưa về trạng thái đóng hoặc an toàn bởi "
      "van điện từ hoặc bởi bộ điều khiển van số. Cách bố trí này gọi là cấu hình một trong hai "
      "(1-out-of-2, 1oo2). Thuật ngữ này có nghĩa là bất kỳ 1 trong 2 thiết bị đều có thể đưa van "
      "điều khiển về trạng thái an toàn. Hai thiết bị đó là bộ điều khiển van số và SOV.",
      "Control valve applications will typically use a solenoid valve between the digital valve "
      "controller and the control valve (Figure 14.16, here Figure 4.16). The SOV will remain "
      "energized while the control valve is being controlled by the digital valve controller. The "
      "digital valve controller pneumatic signal will pass through the SOV during normal "
      "operation. The SOV is in place to allow quick shutdown of the control valve that is "
      "independent of the digital valve controller. The control valve can be put in the closed or "
      "safe state by either the solenoid valve or the digital valve controller. This type of "
      "arrangement is called a 1-out-of-2 (1oo2) arrangement. This nomenclature means that any 1 "
      "device of the 2 devices can put the control valve in its safe state. The devices are the "
      "digital valve controller and SOV.")
    FIG(16, F.fig_f4_16())
    P("Khi chọn SOV cho ứng dụng van điều khiển, phải bảo đảm SOV vận hành được trên toàn dải áp "
      "suất của cơ cấu chấp hành và bộ điều khiển van số. Áp suất cho các ứng dụng này có thể từ 0 "
      "đến 150 psi tùy loại cơ cấu chấp hành. Để làm việc hiệu quả trên dải áp suất đó, phải dùng "
      "SOV tác động trực tiếp (Hình 4.17) hoặc SOV dẫn khí ngoài "
      "(externally-piloted) (Hình 4.18). SOV tác động trực tiếp chỉ vận hành "
      "bằng lực điện từ của cuộn dây. SOV dẫn khí ngoài dùng áp suất khí bên ngoài để đổi trạng "
      "thái; áp suất này được bật/tắt bởi mẫu điện từ tác động trực tiếp là một phần của SOV. Áp "
      "suất khí ngoài cho phép loại SOV này đổi trạng thái mà không cần áp suất trong thân chính "
      "của SOV.",
      "When choosing an SOV for use in a control valve application, one must make sure that the "
      "SOV can operate over the entire pressure range of the control valve actuator and digital "
      "valve controller. The pressures for these applications may range from 0-150 psi depending "
      "upon the actuator type. In order to work effectively over this pressure range, a "
      "direct-acting SOV (Figure 14.17, here Figure 4.17) or externally-piloted SOV (Figure 14.18, "
      "here Figure 4.18) must be used. A direct-acting SOV is operated solely by the "
      "electro-magnetic force of the solenoid. An externally piloted SOV uses external air "
      "pressure to change the state of the SOV. The external air pressure is turned on and off by "
      "the direct-acting electro-magnetic solenoid pilot that is part of the SOV. The external air "
      "pressure allows this type of SOV to change state without any air pressure in the main part "
      "of the SOV.")
    FIG(17, F.fig_f4_17())
    FIG(18, F.fig_f4_18())
    P("Có nhiều kiến trúc SOV khác nhau tùy ưu tiên và nhu cầu của người dùng cuối. Xem Hình 4.17 "
      "để biết kiến trúc 1oo2 điển hình dùng trong hệ thống mà yêu cầu bất kỳ "
      "1 SOV nào cũng đưa phần tử điều khiển cuối về trạng thái an toàn. Xem Hình 4.19 "
      "để biết kiến trúc SOV 2oo2 yêu cầu cả hai SOV cùng đưa phần tử điều khiển cuối về "
      "trạng thái an toàn. Kiến trúc SOV có cấu hình phức tạp hơn. Điểm quan trọng cần nhớ là ký "
      "hiệu XooY có nghĩa cụ thể: bất kỳ X SOV trong tổng số Y SOV phải đổi trạng thái khi có yêu "
      "cầu nhằm đưa phần tử điều khiển cuối về trạng thái an toàn. Một van điện từ dùng riêng được "
      "coi là 1oo1.",
      "There are multiple SOV architectures that can be used based upon the preference and need "
      "of the end user. See Figure 14.17 (here Figure 4.17) for a typical 1oo2 architecture that "
      "is used in systems where the need is for any 1 SOV to put the final control element in its "
      "safe state. See Figure 14.19 (here Figure 4.19) for a 2oo2 SOV architecture that requires "
      "both SOVs to put the final control element in its safe state. SOV architectures are "
      "available in more complex configurations. The important aspect to remember about SOV "
      "architecture is the nomenclature specified as XooY has a specific meaning. Any X SOV(s) of "
      "the total Y SOV(s) must change state when demanded, in order to put the final control "
      "element in its safe state. A single solenoid used by itself is considered 1oo1.")
    FIG(19, F.fig_f4_19())
    FIG(20, F.fig_f4_20())
    P("SOV có nhiều thiết kế, từ van ba chiều tác động trực tiếp đơn giản đến van đặt lại bằng tay "
      "phức tạp hơn và hệ thống van điện từ dự phòng. SOV đặt lại bằng tay (xem Hình 4.22) "
      "được dùng khi cần người vận hành xác nhận trước đưa SOV vào vận hành. Thường "
      "thì SOV được cấp điện nhưng sẽ không tác động cho đến khi người vận hành nâng cần cơ khí vào "
      "vị trí. Hệ thống SOV dự phòng (xem Hình 4.21) được dùng cho ứng dụng "
      "trọng yếu để tránh ngắt giả và/hoặc giúp bảo đảm việc đóng sẽ xảy ra khi có yêu cầu tại "
      "phần tử điều khiển cuối.",
      "SOVs come in many different designs, from simple three-way direct-acting valves to more "
      "complicated manual reset valves and redundant solenoid systems. Manual reset SOVs (see "
      "Figure 14.22, here Figure 4.22) are used when verification from an operator is needed prior "
      "to putting the SOV in service. Typically, the SOV is energized electrically but will not "
      "operate until an operator physically lifts a lever into place. Redundant SOV (see Figure "
      "14.21, here Figure 4.21) systems are used in critical applications to avoid spurious trips "
      "and/or to help ensure that a shutdown will occur when demanded in a final control element.")
    FIG(21, F.fig_f4_21())
    FIG(22, F.fig_f4_22())
    FIG(23, F.fig_f4_23())

    # ------------------------------------------------------------ 4.11
    H("4.11 Hệ thống ngắt", "4.11 Trip Systems")
    P("Hệ thống ngắt (trip system) được dùng trong ứng dụng điều khiển mà cần một tác động xác định "
      "của cơ cấu chấp hành khi mất áp suất cấp (Hình 4.24). Chúng được dùng với cơ cấu chấp hành "
      "tác động kép không có trạng thái mất khí an toàn cố hữu, hoặc với cơ cấu tác động đơn/kép để "
      "khóa khí nén (pneumatic lock-up). Khi áp suất cấp xuống dưới điểm ngắt, van ngắt làm cơ cấu "
      "chấp hành chuyển lên, khóa ở vị trí cuối cùng hoặc chuyển xuống. Với ứng dụng tác động kép, "
      "bình chứa cung cấp thể tích khí dự phòng để vận hành van cho đến khi áp suất cấp được khôi "
      "phục. Khi áp suất cấp tăng lại trên điểm ngắt, van ngắt tự đặt lại, cho phép hệ thống trở "
      "về vận hành bình thường.",
      "Trip systems are used in control applications where a specific actuator action is required "
      "in the event that supply pressure is lost (Figure 4.24). These are used with double-acting "
      "actuators that do not have an inherent no air, fail state or with single- or double-acting "
      "actuators to provide pneumatic lock-up. When supply pressure falls below the trip point, "
      "the trip valve causes the actuator to fail up, lock in the last position, or fail down. For "
      "double-acting applications, a volume tank provides the reserve pneumatic air capacity to "
      "operate the valve until the supply pressure is restored. When the supply pressure rises "
      "above the trip point, the trip valve automatically resets, allowing the system to return to "
      "normal operation.")
    FIG(24, F.fig_f4_24())

    # ------------------------------------------------------------ 4.12
    H("4.12 Van chuyển mạch", "4.12 Switching Valves")
    P("Van chuyển mạch thường được dùng để cung cấp áp suất giảm không đổi của chất lỏng khí cho bộ "
      "điều khiển dẫn khí và thiết bị khí nén khác. Với lựa chọn lò xo để độ phân giải tối ưu, điểm "
      "chuyển mạch được đặt theo yêu cầu cụ thể bằng vít chỉnh ở đầu vỏ lò xo. Chủ yếu được dùng "
      "trong cơ cấu chấp hành kiểu màng và lò xo để đạt tác động an toàn «Khóa ở vị trí cuối cùng» "
      "(Hình 4.25).",
      "The switching valves are typically used to deliver constant reduced pressure of gaseous "
      "fluids to pilot-operated controllers and other pneumatic instrumentation. With a choice of "
      "springs for optimum resolution, the switching point is set to a specific requirement by an "
      "adjusting screw at top the spring case. Predominantly used in spring and diaphragm "
      "actuators to achieve Lock in Last position as fail action. (Figure 4.25)")
    FIG(25, F.fig_f4_25())

    # ------------------------------------------------------------ 4.13
    H("4.13 Tay quay", "4.13 Handwheels")
    P("Tay quay cho cơ cấu chấp hành màng thường được dùng làm điểm dừng hành trình có thể chỉnh. "
      "Chúng cũng cung cấp cách sẵn có để định vị van điều khiển trong trường hợp khẩn cấp. Tay "
      "quay lắp bên hông có thể dùng để đi van theo một trong hai hướng tại bất kỳ điểm nào trong "
      "hành trình thân cơ cấu chấp hành (Hình 4.26). Tay quay lắp bên hông có thể được định vị để "
      "giới hạn hành trình theo một hướng, nhưng không phải cả hai hướng cùng lúc. Ở vị trí trung "
      "tính, vận hành tự động được phép trong toàn bộ hành trình van. Ở bất kỳ vị trí nào khác, "
      "hành trình van bị giới hạn. Tay quay lắp trên đỉnh được dùng cho dịch vụ không thường xuyên "
      "để đi van bằng tay (Hình 4.27).",
      "Handwheels for diaphragm actuators are often used as adjustable travel stops. They also "
      "provide a ready means of positioning the control valve in an emergency. Side-mounted "
      "handwheels can be used to stroke the valve in either direction at any point in the actuator "
      "stem travel (Figure 4.26). The side-mounted handwheel can be positioned to limit travel in "
      "either direction, but not both at the same time. With the handwheel in the neutral "
      "position, automatic operation is possible throughout full valve travel. In any other "
      "position, valve travel will be restricted. Top-mounted handwheels are used for infrequent "
      "service to manually stroke the valve (Figure 4.27).")
    FIG(26, F.fig_f4_26())
    FIG(27, F.fig_f4_27())

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 4 chiếm tr. 82–97 của bản in (16 trang) trong Emerson, Control Valve Handbook, ấn bản "
      "6 (2020). Nội dung gồm mười ba mục: cân nhắc môi trường và ứng dụng, bộ định vị, bộ chuyển "
      "đổi I/P, bộ tăng thể tích, hệ thống an toàn bằng dụng cụ, van số tối ưu, bộ điều khiển, bộ "
      "phát vị trí, công tắc hành trình, van điện từ, hệ thống ngắt, van chuyển mạch và tay quay. "
      "Hai mươi bảy hình đánh số 4.1–4.27 (gồm mười hình 14.14–14.23 được đổi số trong mục 4.10) "
      "được vẽ lại dạng vector trong cvh6fig.py và đặt đúng vị trí xuất hiện của chú thích gốc.",
      "Chapter 4 occupies printed pp. 82-97 (16 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains thirteen sections: environmental and application "
      "considerations, positioners, I/P transducers, volume boosters, safety instrumented systems, "
      "optimized digital valves, controllers, position transmitters, limit switches, solenoid "
      "valves, trip systems, switching valves and handwheels. The twenty-seven numbered figures, "
      "4.1-4.27 (including ten renumbered from 14.14-14.23 in section 4.10), are redrawn as "
      "vectors in cvh6fig.py and placed where the source captions occur.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 "
      "Emerson Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 "
      "Emerson Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
