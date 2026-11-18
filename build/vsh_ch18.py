# -*- coding: utf-8 -*-
"""Book 6, Unit 18 — Actuators (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 293–308 (PDF pp. 307–322): actuator reasons and categories, valve
operating forces, pneumatic, electric and hydraulic actuators, control-
valve actuator sizing, specification sheets, spares and maintenance
(Figures 8-1…8-5).
"""

from vsh_common import fig, h2, h3, ol, p, table, ul
import vshfig15 as F15

PAGES_SRC = 16         # source book pp. 293-308
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Actuators"
TITLE_VI = "Cơ cấu chấp hành"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 18.</b> actuator — cơ cấu chấp hành · "
                "linear — chuyển động thẳng · part-turn — quay một phần vòng · "
                "multi-turn — quay nhiều vòng · fail-safe — an toàn khi mất "
                "nguồn · breakout torque — mô-men khởi động · thrust — lực "
                "đẩy · scotch yoke — yoke Scotch · rack and pinion — thanh "
                "răng và bánh răng · cam — cam · vane — cánh vane · "
                "positioner — bộ định vị · spring return — về vị trí bằng lò "
                "xo · solenoid — van điện từ · accumulator — bình tích áp · "
                "handwheel — tay quay · limit switch — công tắc hành trình · "
                "spares — phụ tùng dự phòng.")
    return ("<b>Key terms.</b> actuator · linear · part-turn · multi-turn · "
            "fail-safe · breakout torque · thrust · scotch yoke · rack and "
            "pinion · cam · vane · positioner · spring return · solenoid · "
            "accumulator · handwheel · limit switch · spares.")


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
    H("Vì sao dùng cơ cấu chấp hành", "Why use an actuator")
    P("Van vận hành bằng tay do nhân viên nhà máy cung cấp năng lượng để mở, "
      "đóng hoặc định vị phần đóng. Trong nhiều trường hợp vận hành tay không "
      "phải là lựa chọn được, người ta lắp thêm thiết bị gọi là cơ cấu chấp "
      "hành. Với năng lượng cung cấp, thiết bị này có thể vận hành van bằng "
      "một nút bấm hoặc tự động theo hệ thống công nghệ.",
      "A manually operated valve relies on plant personnel to supply the "
      "energy to open, close or position the closing element. Where manual "
      "operation is not an option, an additional device called an actuator "
      "is fitted. With supplied energy it can operate the valve by pushbutton "
      "or automatically through process systems.")
    FIG(1, F15.fig_vsh_8_1())
    U([("Điều khiển hệ thống công nghệ.", "Control of the process system."),
       ("Vị trí khó tiếp cận hoặc ở xa.", "Inaccessibility or remote location."),
       ("Yêu cầu dừng khẩn cấp hoặc an toàn khi mất nguồn.",
        "Emergency shutdown or fail-safe requirements."),
       ("Mô-men vận hành van quá lớn.", "Excessive valve operating torque."),
       ("An toàn.", "Safety.")])
    P("Phương pháp chấp hành chia thành ba nhóm: tuyến tính, quay một phần "
      "vòng và quay nhiều vòng. Mỗi nhóm có thể dùng nguồn thủy lực, điện "
      "hoặc khí nén. Khi chọn loại, kỹ sư phải bảo đảm cơ cấu tạo đủ mô-men "
      "và lực để di chuyển và ép kín van với nguồn thấp nhất sẵn có, đồng "
      "thời giữ vị trí open, đóng hoặc trung gian trong điều kiện dòng chảy "
      "xấu nhất. Cơ cấu cũng phải hoàn thành hành trình 90°, 180° hoặc nhiều "
      "vòng với tốc độ yêu cầu và có thiết bị ngăn lực quá mức khi nguồn "
      "không ổn định.",
      "Actuation methods fall into linear, part-turn and multi-turn groups. "
      "Each can be powered hydraulically, electrically or pneumatically. The "
      "engineer must ensure enough torque and thrust to move and seat the "
      "valve at the minimum available supply, and to hold open, closed or "
      "intermediate position under the worst flow conditions. The actuator "
      "must also complete 90°, 180° or multi-turn travel at the required "
      "speed and include a device that prevents excessive force under "
      "adverse supply conditions.")

    # ======================================================== operating forces
    H("Lực và mô-men vận hành van", "Valve operating forces")
    H("Van chuyển động thẳng", "Linear valves", h3)
    P("Van tuyến tính mở và đóng theo chuyển động qua lại lên xuống. Có thể "
      "dùng cơ cấu điện quay vít có ren hoặc truyền trực tiếp vào ty qua "
      "xi lanh khí nén hoặc thủy lực. Cơ cấu phải tạo lực đẩy thắng ma sát "
      "giữa gland và ty hoặc thanh đi vào thân van.",
      "Linear valves open and close in reciprocating motion. An electric "
      "actuator may rotate a screwed stem, or a pneumatic or hydraulic "
      "cylinder may drive a rod directly. The actuator must provide thrust "
      "to overcome friction between the gland and the stem or rod entering "
      "the body.")
    U([("Van cửa dạng nêm rắn hoặc nêm mềm: khi đóng có hiệu ứng tiết lưu "
        "làm tăng chênh áp, ép cửa vào ghế dưới và cần lực đẩy bổ sung.",
        "Solid and flexible wedge gates: closing throttles the flow, raising "
        "differential pressure and forcing the gate onto the downstream seat; "
        "extra thrust is required."),
       ("Van trượt song song: xét đến ma sát tương tự nhưng không cần cấp "
        "lực ép kín bổ sung vì áp suất tự ép cửa vào ghế.",
        "Parallel slide valves: similar friction, but no extra seating "
        "allowance because pressure itself forces the slide onto the seat."),
       ("Van cầu kiểu vặn xuống thường lắp dòng chảy dưới đĩa nên chống đóng; "
        "cần lực đẩy lớn để ép kín kim loại–kim loại.",
        "Screw-down globe valves are usually installed with flow under the "
        "disc, resisting closure; high additional thrust is needed for "
        "metal-to-metal sealing."),
       ("Van điều khiển: cần xét hình dáng nút đóng, lưu lượng và chênh áp.",
        "Control valves: plug shape, flow rate and differential pressure "
        "need separate thought."),
       ("Van màng và van kẹp: độ cứng của lớp lót ảnh hưởng đến lực kẹp; "
        "không được chọn cơ cấu quá lớn làm rách màng.",
        "Diaphragm and pinch valves: lining stiffness affects closing force; "
        "an oversized actuator must not rupture the internal membrane.")])
    P("Với van màng và van kẹp, lực kẹp phụ thuộc nhiều vào độ cứng của vật "
      "liệu lót. Điều quan trọng là vừa đủ lực để đóng kín, vừa tránh quá tải "
      "làm rách màng bên trong.",
      "For diaphragm and pinch valves, closing force depends strongly on "
      "lining stiffness. The actuator must close tightly without overloading "
      "and rupturing the internal membrane.")
    H("Van quay 90 độ", "Part-turn valves — 90 degrees", h3)
    P("Hầu hết van quay một phần vòng chỉ cần 90° để mở hoặc đóng. Quãng "
      "đường ngắn giúp giảm đáng kể công suất cần thiết so với van quay "
      "nhiều vòng.",
      "Most part-turn valves need only 90° to open or close. The short travel "
      "gives a clear power advantage over multi-turn valves.")
    U([("Van bi: xét hệ số ma sát giữa bi kim loại với ghế mềm hoặc ghế kim "
        "loại, cùng nhiệt độ, áp suất, vận tốc dòng và độ nhớt. Nhà chế tạo "
        "cung cấp đường cong mô-men, trong đó mô-men khởi động là giá trị "
        "quan trọng cho PTFE, PEEK hoặc ghế kim loại.",
        "Ball valves: consider the friction coefficient between metal ball "
        "and soft or metal seat, plus temperature, pressure, velocity and "
        "viscosity. Makers supply torque curves; breakout torque is critical "
        "for PTFE, PEEK and metal seats."),
       ("Van bướm: vận tốc dòng ảnh hưởng lớn đến mô-men vì cánh đóng có "
        "tiết diện dạng khí động. Nhiều cơ cấu được trang bị tự khóa vì "
        "phản lực dòng có thể làm cánh dịch chuyển.",
        "Butterfly valves: flow velocity strongly affects torque because the "
        "closure plate is aerofoil-shaped. Self-locking devices are common "
        "because flow reaction can move the plate."),
       ("Van cắm: loại có bôi trơn và không bôi trơn có yêu cầu mô-men khác "
        "nhau; do không ép kín bằng áp suất, mô-men mở và đóng gần nhau. Cắm "
        "song song cần mô-men nhỏ hơn cắm côn.",
        "Plug valves: lubricated and non-lubricated types differ; without "
        "pressure-assisted sealing, opening and closing torques are close. "
        "A parallel plug needs less torque than a tapered plug.")])
    P("Nhà chế tạo uy tín thường cho mô-men lớn nhất trong điều kiện dịch vụ "
      "bình thường. Cần cộng thêm mô-men cho khí khô, bùn, vận tốc cao, "
      "nhiệt độ cao hoặc thấp và ít dùng. Nhà chế tạo cũng có thể cho biết "
      "lượng khí hoặc dầu tiêu thụ cho một hành trình hai chiều.",
      "Reputable manufacturers give maximum torque under normal service. "
      "Extra torque is needed for dry gas, slurry, high velocity, high or low "
      "temperature and infrequent use. The maker can also state media "
      "consumption for a full stroke in both directions.")

    # ============================================================ pneumatic
    H("Cơ cấu khí nén", "Pneumatic actuators")
    P("Cơ cấu khí nén có lẽ là loại phổ biến nhất vì nguồn khí nén rẻ và sẵn. "
      "Chúng thường ít tốn kém hơn phương án điện hoặc thủy lực, thiết kế "
      "đơn giản hơn và dễ bảo trì. Loại này đặc biệt phù hợp van quay một "
      "phần vòng nhưng cũng dùng được cho van tuyến tính; khí nén dễ tích "
      "trữ và dùng được khi nguồn điện hạn chế hoặc không có.",
      "Pneumatic actuators are probably the most common because compressed "
      "air is cheap and available. They are generally less expensive than "
      "electric or hydraulic alternatives, simpler in design and easier to "
      "maintain. They suit part-turn valves but also linear valves; air is "
      "easy to store and useful where power capacity is limited or absent.")
    P("Nguồn cấp thường là khí nén khô, nhưng cũng có thiết kế dùng khí tự "
      "nhiên. Khi lập mạng nhiều cơ cấu, phải tính máy nén và bình tích áp. "
      "Thời gian vận hành van ảnh hưởng lớn đến công suất nguồn và kích "
      "thước ống dẫn.",
      "Supply is usually dry compressed air, though natural-gas designs "
      "exist. For a network of actuators, compressor and accumulator design "
      "matters. Valve operating time strongly affects supply capacity and "
      "tubing size.")
    H("Kiểu màng", "Diaphragm types", h3)
    P("Cơ cấu màng thường tạo chuyển động thẳng, dù cũng có dạng quay. Màng "
      "linh hoạt được kẹp giữa hai vỏ bắt bulông tạo hai buồng kín. Khí vào "
      "một buồng làm màng cong, đẩy hoặc kéo ty van; kiểu tác động trực tiếp "
      "đẩy ty xuống, kiểu ngược đẩy ty lên. Lò xo ở buồng kia tạo cơ chế an "
      "toàn khi mất nguồn, đưa van về mở hoặc đóng.",
      "Diaphragm actuators are usually linear, although rotary designs exist. "
      "A flexible plate is clamped between bolted casings forming two "
      "airtight chambers. Air into one chamber flexes the diaphragm and "
      "extends or retracts the stem; direct acting pushes down, reverse "
      "acting pushes up. A spring in the opposite chamber gives fail-safe "
      "return to open or closed on air failure.")
    P("Cơ cấu màng rẻ, cấu tạo cơ bản và dễ bảo trì, rất phù hợp lực đẩy thấp "
      "ở hạng áp đường ống thấp. Nhược điểm là chiều cao có thể gây khó khăn "
      "trên van nhỏ ở vị trí chật, và vỏ cơ cấu trở nên quá nặng trên van lớn.",
      "Diaphragm actuators are cheap, basic and easy to maintain, and suit "
      "low thrust in lower pressure classes. Their height can be awkward on "
      "small valves in restricted locations, and casings become heavy on "
      "large valves.")
    H("Kiểu piston và cơ chế quay 90 độ", "Piston types and 90-degree mechanisms", h3)
    P("Cơ cấu piston gồm xi lanh và piston trượt làm kín bằng O-ring đàn hồi. "
      "Xi lanh nối với van qua giá đỡ đúc, chừa chỗ cho bộ định vị và phụ "
      "kiện. Thường dùng kiểu tác động kép có cấp khí hai buồng, bộ định vị "
      "nhận tín hiệu và cấp hoặc xả khí cho buồng tương ứng. Lực tuyến tính "
      "truyền thẳng cho ty hoặc chuyển thành lực quay cho van quay một phần "
      "vòng.",
      "A piston actuator has a cylinder and sliding piston sealed by "
      "elastomer O-rings. A cast yoke leaves room for positioners and "
      "accessories. It is usually double acting with air to both chambers "
      "and a positioner that supplies or bleeds air as required. Linear force "
      "goes directly to the stem or is converted to rotary force for "
      "part-turn valves.")
    O([("Yoke Scotch gồm piston, trục nối và chốt quay (Hình 8-2).",
        "A scotch yoke has a piston, connecting shaft and rotary pin "
        "(Figure 8-2)."),
       ("Thanh răng và bánh răng gồm một hoặc hai piston ghép với thanh răng "
        "dẫn bánh răng (Hình 8-3).",
        "Rack and pinion uses one or two pistons coupled to a rack driving "
        "the pinion (Figure 8-3)."),
       ("Trunnion/cần đòn là xi lanh gắn bản lề, piston tác động trực tiếp "
        "vào cần gắn trục van.",
        "A trunnion/lever actuator is a mounted cylinder whose piston acts "
        "directly on a lever attached to the valve shaft."),
       ("Cam gồm hai piston nối bằng thanh, với cam và trục ở giữa "
        "(Hình 8-4).",
        "A cam actuator has double pistons linked by bars with a cam and "
        "shaft between them (Figure 8-4).")])
    FIG(2, F15.fig_vsh_8_2())
    FIG(3, F15.fig_vsh_8_3())
    FIG(4, F15.fig_vsh_8_4())
    P("Cơ cấu cánh vane thường dùng cho van quay 90°. Một cánh dạng tấm nằm "
      "trong buồng kín, gắn liền trục quay. Khí nén vào một buồng và thoát "
      "buồng kia làm cánh và trục quay (Hình 8-5). Ưu điểm là chi phí thấp, "
      "ít chi tiết chuyển động và bảo trì dễ; nhược điểm là mô-men rất nhỏ "
      "nên chỉ dùng cho áp suất thấp.",
      "Vane actuators are common for 90° quarter-turn duty. A plate vane in "
      "an airtight chamber is integral with the rotary shaft. Air enters one "
      "chamber and exhausts the other, rotating vane and shaft (Figure 8-5). "
      "Advantages are low cost, few moving parts and low maintenance; the "
      "drawback is very low torque, limiting use to low-pressure service.")
    FIG(5, F15.fig_vsh_8_5())
    H("Ưu và nhược điểm", "Advantages and disadvantages", h3)
    U([("Khí nén tiện lợi, tương đối rẻ và xả an toàn ra khí quyển.",
        "Compressed air is convenient, relatively cheap and safely vented."),
       ("Piston không tự khóa và có thể làm việc cùng lò xo cho thao tác khẩn "
        "cấp một lần.",
        "A piston is not self-locking and can work against a spring for "
        "single-shot emergency operation."),
       ("Khí nén không có động năng ban đầu nên không tạo được cú đập mở "
        "nêm, và dễ bị trôi vị trí do nén được.",
        "Air has no kinetic hammerblow to unseat a wedge and can drift "
        "because it is compressible."),
       ("Cần cách nhiệt nếu cơ cấu phải làm việc khi có hỏa hoạn; khí không "
        "được sấy khô dễ gây kẹt hoặc ăn mòn trong.",
        "Thermal insulation is needed if the actuator must operate during "
        "fire; insufficiently dried air can cause seizure or internal "
        "corrosion."),
       ("Tiêu hao khí lớn với van lớn cần mô-men cao.",
        "Air consumption can be high for large, high-torque valves.")])
    P("Tóm lại, cơ cấu khí nén có thể là loại dùng phổ biến nhất nhờ ưu điểm "
      "chi phí, phụ tùng sẵn và nhiều vật liệu chế tạo. Lớp phủ bảo vệ cũng "
      "dễ áp dụng.",
      "Overall, the pneumatic actuator is perhaps the most widely used "
      "because of cost, available spares and the range of construction "
      "materials. Protective coatings are also easy to apply.")

    # ================================================================ electric
    H("Cơ cấu điện", "Electric actuators")
    P("Cơ cấu điện hiện đại cho phép vận hành tại chỗ, từ xa và bằng tay, "
      "cho nhiều kiểu và cỡ van. Bộ gồm mô tơ có thể đảo chiều, hộp điều "
      "khiển, hộp số và công tắc hành trình. Ưu điểm chính là vận hành êm, "
      "ổn định, mô-men rất cao và lực duy trì tốt vì không gặp vấn đề của "
      "chất lưu động nén được. Ví dụ điển hình là cơ cấu điện ba pha có tay "
      "quay ở Hình 8-1.",
      "Modern electric actuators allow local, remote and hand operation for "
      "many valve types and sizes. They comprise a reversible motor, control "
      "box, gearbox and limit switches. Main advantages are smooth operation, "
      "stability, very high torque and maintained thrust without compressible "
      "fluid problems. A three-phase unit with handwheel is shown in "
      "Figure 8-1.")
    P("Mô tơ cho van đa vòng hoặc quay một phần có thể dùng nguồn một pha "
      "hoặc một chiều, nhưng mô tơ ba pha phổ biến nhất vì bền và dễ điều "
      "khiển. Mô tơ lắp ngoài trời phải được chế tạo để không tích tụ ẩm "
      "hoặc ngưng tụ bên trong. Tốc độ cao của mô tơ cần tỉ số giảm tốc lớn; "
      "van quay một phần cần giảm tốc hơn nữa.",
      "Motors for multi-turn and part-turn valves may use single-phase or DC "
      "supply, but three-phase is most common for robustness and control. "
      "Outdoor motors must prevent internal moisture or condensation. High "
      "motor speed needs large gear reduction, with further reduction for "
      "part-turn valves.")
    P("Khi mô tơ hỏng, có thể bố trí tay quay bằng tay, thường nối qua ly "
      "hợp cần gạt và tự động trở về chế độ mô tơ khi có điện lại. Cơ cấu "
      "điện cho hành trình cứng, không dao động và thiết kế nhỏ gọn, nhưng "
      "đắt hơn, phức tạp hơn, lưu điện khó và cần bảo vệ cáp ở nhiệt độ cao. "
      "Thiết bị ở khu vực nguy hiểm phải an toàn bản chất.",
      "On motor failure, a handwheel can be engaged by a lever clutch that "
      "returns automatically to motor drive when power returns. Electric "
      "actuators give a stiff, non-fluctuating stroke in a compact design, "
      "but cost more, are more complex, cannot easily store power and need "
      "cable protection at high temperature. Equipment in hazardous areas "
      "must be intrinsically safe.")
    P("Điện là lựa chọn tốt khi cần điều khiển chính xác hệ thống công "
      "nghệ. Cần tránh đánh giá quá cao nguồn sẵn có rồi chọn cơ cấu nhỏ hơn "
      "và rẻ hơn. Mô tơ có ít chi tiết chuyển động hơn, bảo trì thấp và "
      "thường hiệu quả năng lượng.",
      "Electric drive is excellent where accurate process control matters. "
      "Care is needed not to overestimate supply and choose a smaller, "
      "cheaper unit. Motors have fewer moving parts, lower maintenance and "
      "are generally energy efficient.")

    # =============================================================== hydraulic
    H("Cơ cấu thủy lực", "Hydraulic actuators")
    P("Cơ cấu thủy lực tạo mô-men rất lớn và tốc độ hành trình nhanh cho van "
      "lớn. Chất lỏng được coi là không nén được nên hành trình rất cứng. "
      "Chúng được dùng khi cơ cấu khí nén hoặc điện không phù hợp hoặc "
      "không có sẵn.",
      "Hydraulic actuators deliver very high torque and fast stroking speed "
      "for large valves. The liquid is treated as incompressible, giving a "
      "stiff stroke. They are used where pneumatic or electric drives are "
      "unsuitable or unavailable.")
    U([("Bốn dạng cơ bản: thanh răng–bánh răng, mô tơ thủy lực với bánh vít "
        "và bánh răng, piston quay, và piston–xi lanh.",
        "Four basic designs: rack and pinion, hydraulic motor with worm and "
        "gear, rotary piston, and piston and cylinder."),
       ("Có thể tác động kép hoặc về bằng lò xo; áp do bơm cấp tại chỗ hoặc "
        "từ xa qua ống nhỏ.",
        "Double-acting or spring-return types are available; pressure comes "
        "from a local power pack or remotely through small-bore tubing."),
       ("Áp chất lỏng thay đổi được để tạo các mô-men khác nhau, linh hoạt "
        "hơn nguồn điện hoặc khí nén. Công suất tác động kép không đổi, còn "
        "kiểu về lò xo mất năng lượng khi nén lò xo.",
        "Hydraulic pressure can be varied for different torque outputs, "
        "giving more flexibility than electric or pneumatic power. Double-"
        "acting output is constant; spring-return types lose energy while "
        "compressing the spring.")])
    U([("Ưu điểm: lực lớn, tích trữ được áp, vận hành ổn định và thân cơ cấu "
        "nhỏ gọn, dễ phủ và cách nhiệt.",
        "Advantages: high operating forces, stored pressure, stable "
        "operation, and a compact body that is economical to coat and "
        "insulate."),
       ("Nhược điểm: không có cú đập mở nêm, mạng ống đắt, đường ống dài gây "
        "tụt áp, gia công chính xác cao và nguy cơ hỏng khi cháy. Giãn nở "
        "nhiệt cao có thể cần thiết bị giảm áp.",
        "Disadvantages: no hammerblow, costly tubing networks, long runs and "
        "pressure drop, close machining tolerances and poor fire survival. "
        "High thermal expansion may require a relief device.")])
    P("Tóm lại, cơ cấu thủy lực và điện–thủy lực bền, tin cậy và có hành "
      "trình cứng. Loại chế tạo tốt kín nước, dùng được ở môi trường cực ẩm "
      "như giàn khoan hoặc đầu giếng dưới biển, nhưng đắt, có thể cồng kềnh "
      "và cần chú ý đặc biệt khi vận hành.",
      "Hydraulic and electrohydraulic actuators are robust, reliable and "
      "stiff. Well-built units are watertight and suit extremely wet "
      "environments such as offshore and subsea wellheads, but they are "
      "expensive, may be bulky and need special operating attention.")

    # ============================================================ control sizing
    H("Định cỡ cơ cấu cho van điều khiển", "Sizing actuators for control valves")
    P("Khi định cỡ cơ cấu cho van điều khiển, phải xét trường hợp xấu nhất "
      "khi van mở, đóng hoặc đang tiết lưu. Van điều khiển định cỡ sai sẽ "
      "chạy không ổn định, gây rung và mòn phần đóng cùng các chi tiết bên "
      "trong. Khi cơ cấu chạy hết hành trình, nó phải thắng mô-men khởi động "
      " và ma sát của ty qua các thành phần làm kín.",
      "When sizing a control-valve actuator, the worst case must be "
      "considered with the valve open, closed or throttling. Incorrectly "
      "sized control valves operate erratically, leading to vibration and "
      "wear of the closure device and trim. At full stroke the actuator must "
      "overcome breakout torque and stem friction through the sealing "
      "components.")
    P("Lực cơ cấu sẵn có luôn phải lớn hơn lực cần để mở, đóng và tiết lưu "
      "hiệu quả trong dịch vụ thực tế.",
      "Available actuator force must always exceed the force needed to open, "
      "close and throttle the process service efficiently.")

    # ============================================================== spec sheet
    H("Bảng đặc tính kỹ thuật", "Actuator specification sheet")
    P("Để bảo đảm cơ cấu đáp ứng mọi yêu cầu công nghệ và tránh nhầm lẫn, "
      "cần lập bảng đặc tính kỹ thuật cho mỗi van dùng cơ cấu. Bảng phải "
      "chứa thông tin về cơ cấu lẫn thân van sẽ lắp. Cách này giúp nhóm "
      "thiết kế thống nhất và cho phép bộ phận mua hàng gửi yêu cầu rõ ràng "
      "cho nhà cung cấp.",
      "To ensure the actuator meets all process requirements and avoid "
      "confusion, an engineering specification sheet should be created for "
      "each actuated valve. It must contain technical information about both "
      "the actuator and the valve body. This aligns the design group and lets "
      "procurement place confident requisitions with suppliers.")

    # =========================================================== spares/service
    H("Phụ tùng và bảo trì", "Spare parts and maintaining actuated valves")
    P("Cơ cấu thường được chọn cho tuổi thọ nhà máy 20 đến 25 năm. Không "
      "nên mong thiết bị phức tạp tồn tại bấy lâu mà không bảo trì định kỳ "
      "và thay một số chi tiết. Vì vậy cần cân nhắc đặt phụ tùng ngay khi "
      "mua cơ cấu.",
      "Actuators are usually selected for a plant life of 20 to 25 years. A "
      "complex device cannot be expected to last that long without periodic "
      "maintenance and part replacement. Spare parts should therefore be "
      "considered when the actuator is purchased.")
    U([("Phụ tùng chạy thử: trong giai đoạn chạy thử, đường ống có thể còn "
        "bụi bẩn dù đã xả rửa; cần bộ gioăng mềm và O-ring dự phòng.",
        "Commissioning spares: dirt can remain after flushing; keep soft "
        "seals and O-rings available."),
       ("Phụ tùng hai năm: ngân sách thường lập khi nhà máy còn bảo hành; "
        "gồm gioăng mềm, O-ring, gland, đĩa/nút đóng và bộ lò xo.",
        "Two-year spares: budgeted while still under warranty; include soft "
        "seals, O-rings, glands, closure discs or plugs, and spring sets."),
       ("Phụ tùng dài hạn: mở rộng danh sách hai năm và cân nhắc thay toàn "
        "bộ thiết bị có thời gian chế tạo dài, vì hỏng hóc gây tốn kém.",
        "Long-term spares: extend the two-year list and consider total "
        "replacement of long-lead items because failure is costly.")])
    P("Nhà chế tạo có trách nhiệm cung cấp sổ tay vận hành an toàn và hướng "
      "dẫn bảo trì, nêu chu kỳ và các chi tiết cần bôi trơn, mỡ hoặc chỉnh "
      "chỉnh. Hỏng lớn trong thời gian bảo hành phải do nhà chế tạo xử lý "
      "ngoài chế độ bảo trì thông thường. Dù hỏng sau bảo hành, nhà chế tạo "
      "ban đầu vẫn là lựa chọn nên xem xét đầu tiên.",
      "The maker should supply a manual covering safe operation and "
      "maintenance, stating intervals and parts needing lubrication, "
      "greasing or adjustment. Major failure within warranty requires work "
      "outside the normal maintenance regime by the manufacturer. Even after "
      "warranty, the original maker should be the first option considered.")
    P("Với hỏng lớn, nhiều trường hợp mua thiết bị mới rẻ hơn vì chi phí "
      "phụ tùng và nhân công gần bằng giá mua mới. Sau khi sửa, các chi tiết "
      "khác cũng có thể tiếp tục hỏng trong thời gian ngắn.",
      "For major failure, buying new equipment is often cheaper because "
      "parts and labor approach the purchase price. After repair, other "
      "parts are likely to fail soon afterwards.")

    # ================================================================== table
    H("Bảng tóm tắt cơ cấu chấp hành", "Actuator summary")
    b.append(table(
        ["Hình / chủ đề", "Loại", "Điểm chính"]
        if vi else ["Figure / topic", "Type", "Key point"],
        [
            ["8-1", "Điện ba pha" if vi else "Three-phase electric",
             "Tay quay, mô tơ, hộp số, trục ra" if vi else
             "Handwheel, motor, gearing, output drive"],
            ["van thẳng" if vi else "Linear valves",
             "Đẩy / ma sát" if vi else "Thrust and friction",
             "Nêm, cửa song song, cầu, màng" if vi else
             "Wedge, parallel slide, globe, diaphragm"],
            ["van 90°" if vi else "90-degree valves",
             "Mô-men" if vi else "Torque",
             "Bi, bướm, cắm; mô-men khởi động" if vi else
             "Ball, butterfly, plug; breakout torque"],
            ["8-2", "Yoke Scotch" if vi else "Scotch yoke",
             "Piston, rãnh yoke, chốt quay" if vi else
             "Piston, yoke slot, rotary pin"],
            ["8-3", "Thanh răng" if vi else "Rack and pinion",
             "Đơn, song song, đối lập kép" if vi else
             "Single, tandem, dual-opposed"],
            ["8-4", "Cam" if vi else "Cam",
             "Hai piston nối, cam và trục" if vi else
             "Linked pistons, cam and shaft"],
            ["8-5", "Cánh vane" if vi else "Vane",
             "Mô-men thấp, van 90°" if vi else "Low torque, quarter-turn"],
            ["khí nén" if vi else "Pneumatic",
             "Màng, piston, cánh" if vi else "Diaphragm, piston, vane",
             "Rẻ, đơn giản; dễ trôi vị trí" if vi else
             "Cheap, simple; possible drift"],
            ["điện" if vi else "Electric",
             "Mô tơ đảo chiều" if vi else "Reversible motor",
             "Ổn định, mô-men cao; đắt hơn" if vi else
             "Stable, high torque; higher cost"],
            ["thủy lực" if vi else "Hydraulic",
             "Áp chất lỏng" if vi else "Liquid pressure",
             "Lực lớn, hành trình cứng" if vi else
             "High force, stiff stroke"],
            ["định cỡ" if vi else "Sizing",
             "Trường hợp xấu nhất" if vi else "Worst case",
             "Thắng mô-men khởi động và ma sát" if vi else
             "Overcome breakout torque and friction"],
            ["phụ tùng" if vi else "Spares",
             "20–25 năm" if vi else "20–25 years",
             "Chạy thử, hai năm, dài hạn" if vi else
             "Commissioning, two-year, long-term"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 293–308, "
                 "Hình 8-1…8-5." if vi else
                 "Summary from source text, book pp. 293–308, "
                 "Figures 8-1…8-5."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
