# -*- coding: utf-8 -*-
"""Book 6, Unit 5 — Manual Valves I: Functions, Selection and Globe Valves
(EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 47–73 (PDF pp. 61–87): functions of manual valves, grouping by method of
flow regulation (Figure 3-1), selection by duty incl. end connections and
ratings (Table 3-1), globe valves (body patterns Figures 3-2…3-14, seatings
Figures 3-15/3-16, disc-to-stem connection, stem screws, bonnet joints,
stuffing boxes Figures 3-17…3-19, direction of flow) and piston valves
(Figures 3-20…3-24).
"""

from vsh_common import (fig, h2, h3, note, p, table, ul)
import vshfig3 as F3

PAGES_SRC = 27          # source book pp. 47-73
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Manual Valves I — Functions, Selection and Globe Valves"
TITLE_VI = "Van tay I — Chức năng, lựa chọn và van cầu"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 5.</b> closing-down valve — van đóng "
                "hướng trục · slide valve — van trượt · rotary valve — van "
                "quay · flex-body valve — van thân mềm · diverting — phân "
                "luồng dòng · solids in suspension — chất rắn lơ lửng · "
                "threaded / flanged / welding end — đầu nối ren / bích / "
                "hàn · seal welding — hàn kín mối nối · creep relaxation — "
                "chảy dẻo (creep) làm lỏng mối nối · WOG / WSP — định mức nước-"
                "dầu-khí / hơi nước · stuffing box — hộp đón · back seat — "
                "chỗ kín ngược · lantern ring — vòng lantern · pressure-seal "
                "bonnet — nắp kín áp · galling — kẹt dính mặt trượt · "
                "soft seating — chỗ kín mềm · ram-seal — nguyên tắc ram-seal.")
    return ("<b>Key terms.</b> closing-down valve · slide valve · rotary "
            "valve · flex-body valve · diverting · solids in suspension · "
            "threaded / flanged / welding end · seal welding · creep "
            "relaxation · WOG / WSP rating · stuffing box · back seat · "
            "lantern ring · pressure-seal bonnet · galling · soft seating · "
            "ram-seal principle.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(items):
        b.append(ul([(i[0] if vi else i[1]) for i in items]))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ------------------------------------------------------------ functions
    H("Chức năng của van tay",
      "Functions of manual valves")
    P("Van tay là van do nhân viên vận hành trực tiếp thao tác bằng bánh tay "
      "hoặc cần quay, hoặc bằng cơ cấu on/off đối với van chặn khẩn cấp. Một "
      "số van tự động có cơ cấu chấp hành vẫn được trang bị thêm bánh tay để "
      "cho phép thao tác tay khi mất điện.",
      "A manual valve is a valve operated by plant personnel directly, by "
      "the use of either a handwheel/wrench or an on/off actuator in the "
      "case of shutdown valves. Certain automated valves with actuators are "
      "also supplied with handwheels to allow manual operation in the event "
      "of power failure.")
    P("Trong hệ thống xử lý chất lỏng, van tay phục vụ ba chức năng chính: "
      "dừng và khởi động dòng chảy, khống chế lưu lượng, và phân luồng dòng. "
      "Van dùng để dừng/khởi động dòng thường được dùng luôn để khống chế "
      "lưu lượng và ngược lại, còn van phân luồng được thiết kế riêng cho "
      "nhiệm vụ đó.",
      "Manual valves serve three major functions in fluid-handling systems: "
      "stopping and starting flow, controlling flow rate, and diverting "
      "flow. Valves for stopping and starting flow are frequently employed "
      "also for controlling flow rate, and vice versa, while valves for "
      "diverting flow are designed for that single purpose.")

    # ------------------------------------------------------------- grouping
    H("Phân nhóm van theo phương pháp khống chế dòng",
      "Grouping of valves by method of flow regulation")
    P("Van tay có thể phân nhóm theo cách phần đóng di chuyển tới chỗ kín. "
      "Theo đó phân biệt được bốn nhóm van:",
      "Manual valves may be grouped according to the way the closure member "
      "moves onto the seat. Four groups of valves are thereby distinguishable:")
    U([("<b>Van đóng hướng trục</b> — phần đóng dạng chặn di chuyển tới và "
        "khỏi chỗ kín theo phương trục chỗ kín.",
        "<b>Closing-down valves</b> — a stopper-like closure member is moved "
        "to and from the seat in the direction of the seat axis."),
       ("<b>Van trượt</b> — phần đóng dạng cửa trượt ngang qua đường dòng.",
        "<b>Slide valves</b> — a gate-like closure member is moved across "
        "the flow passage."),
       ("<b>Van quay</b> — phần đóng dạng phích hoặc đĩa quay trong đường "
        "dòng quanh trục vuông góc với dòng chảy.",
        "<b>Rotary valves</b> — a plug or disc-like closure member is "
        "rotated within the flow passage, around an axis normal to the flow "
        "stream."),
       ("<b>Van thân mềm</b> — phần đóng làm mềm (biến dạng) thân van.",
        "<b>Flex-body valves</b> — the closure member flexes the valve "
        "body.")])
    P("Mỗi nhóm gồm nhiều kiểu van dùng cùng một phương pháp khống chế dòng "
      "nhưng khác nhau về hình dạng phần đóng: chẳng hạn van phích và van "
      "bướm đều là van quay nhưng khác kiểu. Hình 3-1 vẽ lại các phương pháp "
      "khống chế dòng chính và tên các kiểu van thuộc từng nhóm.",
      "Each valve group represents a number of distinct types of valves "
      "that use the same method of flow regulation, but differ in the shape "
      "of the closure member. For example, plug valves and butterfly valves "
      "are both rotary valves, but of a different type. Figure 3-1 "
      "illustrates the principal methods of flow regulation and names the "
      "types of valves which belong to a particular valve group.")
    FIG(1, F3.fig_vsh_3_1())

    # ------------------------------------------------------------ selection
    H("Lựa chọn van",
      "Selection of valves")
    P("Cách phần đóng khống chế dòng và cấu hình đường dòng qua van tạo ra "
      "một đặc tính dòng nhất định, được cân nhắc khi chọn van cho một "
      "nhiệm vụ khống chế dòng cụ thể.",
      "The method by which the closure member regulates the flow and the "
      "configuration of the flow path through the valve impart a certain "
      "flow characteristic to the valve, which is taken into account when "
      "selecting a valve for a given flow-regulating duty.")
    H("Van để dừng và khởi động dòng", "Valves for stopping and starting flow",
      h3)
    P("Thường chọn van có trở lực thấp và đường dòng thẳng: đó là các van "
      "trượt, van quay và van thân mềm. Van đóng hướng trục có đường dòng "
      "khúc khuỷu nên trở lực cao hơn, ít được dùng cho nhiệm vụ này; tuy "
      "nhiên nếu trở lực cao hơn chấp nhận được — như thường gặp — thì vẫn "
      "dùng được.",
      "These valves are normally selected for low flow resistance and a "
      "straight-through flow passage. Such valves are slide valves, rotary "
      "valves, and flex-body valves. Closing-down valves offer by their "
      "tortuous flow passage a higher flow resistance than other valves and "
      "are therefore less frequently used for this purpose. However, if the "
      "higher flow resistance can be accepted — as is frequently the case — "
      "closing-down valves may likewise be used for this duty.")
    H("Van để khống chế lưu lượng", "Valves for controlling flow rate", h3)
    P("Chọn van có thể chỉnh lưu lượng dễ dàng. Van đóng hướng trục phù hợp "
      "vì kích thước chỗ kín tỉ lệ trực tiếp với hành trình phần đóng. Van "
      "quay và van thân mềm cũng cho khống chế tốt nhưng thường chỉ trong "
      "phạm vi mở hạn chế. Van cửa, trong đó đĩa tròn chạy ngang qua chỗ kín "
      "tròn, chỉ đạt khống chế tốt gần vị trí đóng nên không thường dùng cho "
      "nhiệm vụ này.",
      "These are selected for easy adjustment of the flow rate. Closing-down "
      "valves lend themselves for this duty because of the directly "
      "proportional relationship between the size of the seat opening and "
      "the travel of the closure member. Rotary valves and flex-body valves "
      "also offer good throttling control, but normally only over a "
      "restricted valve-opening range. Gate valves, in which a circular disc "
      "travels across a circular seat opening, achieve good flow control "
      "only near the closed valve position and are therefore not normally "
      "used for this duty.")
    H("Van để phân luồng dòng", "Valves for diverting flow", h3)
    P("Van phân luồng có ba cổng trở lên, tùy nhiệm vụ phân luồng. Van phích "
      "và van bi dễ thích nghi cho nhiệm vụ này, vì vậy hầu hết van phân "
      "luồng là một trong hai kiểu đó. Các kiểu van khác cũng được cải biến "
      "để phân luồng, trong một số trường hợp bằng cách ghép hai van trở lên "
      "liên kết với nhau.",
      "These valves have three or more ports, depending on the flow "
      "diversion duty. Valves that adapt readily to this duty are plug "
      "valves and ball valves. For this reason, most valves for the "
      "diversion of flow are one of these types. However, other types of "
      "valves have also been adapted for the diversion of flow, in some "
      "cases by combining two or more valves that are suitably "
      "interlinked.")
    H("Van cho chất lỏng có rắn lơ lửng",
      "Valves for fluids with solids in suspension", h3)
    P("Van phù hợp nhất là van có phần đóng trượt ngang qua chỗ kín với "
      "chuyển động quét. Van mà phần đóng đóng mở vuông góc trên chỗ kín có "
      "thể giữ rắn lại và vì vậy chỉ phù hợp cho chất lỏng tương đối sạch, "
      "trừ khi vật liệu chỗ kín có thể nhấn chìm rắn bị giữ.",
      "If the fluid carries solids in suspension, the valves best suited "
      "for this duty have a closure member that slides across the seat with "
      "a wiping motion. Valves in which the closure member moves squarely "
      "on and off the seat may trap solids and are therefore suitable only "
      "for essentially clean fluids unless the seating material can embed "
      "trapped solids.")

    H("Đầu nối van", "Valve end connections", h3)
    P("Van có thể trang bị bất kỳ kiểu đầu nối ống nào; quan trọng nhất cho "
      "van là đầu nối ren, đầu nối bích và đầu nối hàn.",
      "Valves may be provided with any type of end connection used to "
      "connect piping. The most important of these for valves are threaded, "
      "flanged, and welding end connections.")
    U([("<b>Đầu nối ren.</b> Thường làm bằng ren nữ thon hoặc song song vặn "
        "lên ren nam thon của ống. Mối nối chứa khe rò rỉ lớn nên phải dùng "
        "chất làm kín hoặc vật liệu độn; nếu vật liệu thân van hàn được, "
        "mối ren có thể hàn kín (seal welding) — cần thiết khi hai chi tiết "
        "chênh nhau nhiều về hệ số giãn nở và nhiệt độ vận hành dao động "
        "rộng. Van đầu ren chủ yếu dùng tới DN 50 (NPS 2); khó lắp và làm "
        "kín nhanh khi kích thước tăng, nhưng vẫn có tới DN 150 (NPS 6). "
        "Để lắp và tháo dễ, hệ ống dùng khớp nối tại các vị trí phù hợp: "
        "khớp nối tới DN 50 (NPS 1) là khớp nối union với đai ốc ren "
        "song song; khớp lớn hơn dùng bích. Tiêu chuẩn có thể hạn chế dùng "
        "van đầu ren tùy ứng dụng.",
        "<b>Threaded end connections.</b> Made as a rule with taper or "
        "parallel female threads screwed over tapered male pipe threads. "
        "Because such a joint contains large leakage passages, a sealant or "
        "filler closes the leakage passages; if the body material is "
        "weldable, screwed joints may be seal welded — necessary when "
        "mating parts have widely differing coefficients of expansion and "
        "the operating temperature cycles widely. Threaded-end valves are "
        "primarily used up to DN 50 (NPS 2); installing and sealing the "
        "joint becomes rapidly more difficult with size, though valves are "
        "available up to DN 150 (NPS 6). Couplings at appropriate points "
        "ease erection and removal: up to DN 50 (NPS 1) unions with a "
        "parallel-thread nut, larger couplings flanged. Codes may restrict "
        "the use of threaded-end valves depending on application."),
       ("<b>Đầu nối bích.</b> Cho phép lắp và tháo van khỏi đường ống dễ "
        "dàng, nhưng van cồng kềnh hơn và đắt hơn van đầu ren. Vì mối bích "
        "được siết bằng nhiều bu lông, mỗi bu lông cần mô men nhỏ hơn mối "
        "ren tương ứng, nên thích nghi cho mọi kích thước và áp suất. "
        "Tuy nhiên trên 350 °C (660 °F), hiện tượng chảy dẻo (creep) của "
        "bu lông, gioăng và bích làm giảm tải bu lông theo thời gian; mối "
        "bích chịu ứng suất cao có thể rò rỉ ở nhiệt độ này. Tiêu chuẩn "
        "bích đưa ra nhiều kiểu mặt bích và chỉ định độ nhám phù hợp: mặt "
        "bích khía răng cho gioăng mềm cho kết quả tốt; gioăng kim loại "
        "cần mặt bích mịn hơn. Thiết kế gioăng bàn ở đơn vị 2.",
        "<b>Flanged end connections.</b> Permit valves to be easily "
        "installed and removed from the pipeline, but flanged valves are "
        "bulkier and dearer than threaded-end valves. Because flanged "
        "joints are tightened by a number of bolts, each requiring less "
        "torque than a corresponding screwed joint, they can be adapted for "
        "all sizes and pressures. Above 350 °C (660 °F), however, creep "
        "relaxation of bolts, gasket and flanges can in time noticeably "
        "lower the bolt load; highly stressed joints may leak at these "
        "temperatures. Flange standards offer a variety of flange-face "
        "designs and recommend the face finish: a serrated finish gives "
        "good results with soft gaskets, metallic gaskets need a finer "
        "finish. Gasket design is discussed in unit 2."),
       ("<b>Đầu nối hàn.</b> Phù hợp mọi áp suất và nhiệt độ, đáng tin hơn "
        "nhiều so với đầu bích ở nhiệt độ cao và các ứng dụng khắc nghiệt; "
        "nhưng tháo và lắp lại khó hơn nên thường chỉ dùng cho ứng dụng "
        "yêu cầu vận hành tin cậy lâu dài hoặc ứng dụng tới hạn, nhiệt độ "
        "cao. Van hàn tới DN 50 (NPS 2) thường có ổ hàn (welding socket) "
        "nhận ống đầu trơn; mối hàn ổ tạo khe hở có nguy cơ ăn mòn khe với "
        "một số chất lỏng, và rung động ống có thể làm mỏi mối nối — tiêu "
        "chuẩn có thể hạn chế dùng ổ hàn.",
        "<b>Welding end connections.</b> Suitable for all pressures and "
        "temperatures and considerably more reliable than flanged "
        "connections at elevated temperatures and other severe "
        "applications; removal and re-erection is more difficult, so their "
        "use is normally restricted to applications in which the valve must "
        "operate reliably for long periods, or which are critical or involve "
        "high temperatures. Welding-end valves up to DN 50 (NPS 2) are "
        "usually provided with welding sockets receiving plain-end pipes; "
        "socket-weld joints form a crevice with possible crevice corrosion "
        "for some fluids, and pipe vibrations can fatigue the joint — codes "
        "may restrict the use of welding sockets.")])
    P("Phụ lục C liệt kê các tiêu chuẩn Mỹ và Anh quan trọng nhất về đầu "
      "nối van.", "Appendix C lists the most important U.S. and British "
      "standards pertaining to valve ends.")

    H("Định mức van", "Valve ratings", h3)
    P("Định mức van xác định quan hệ áp suất–nhiệt độ mà van có thể vận "
      "hành. Trách nhiệm xác định định mức trong nhiều năm chủ yếu thuộc về "
      "nhà sản xuất. Thói quen Mỹ nêu định mức van đa dụng bằng WOG (nước, "
      "dầu, khí) và WSP (áp suất hơi ướt) là kế thừa từ thời nước, dầu, khí "
      "và hơi ướt là các môi trường phổ biến: WOG là định mức nhiệt độ phòng, "
      "WSP thường là định mức nhiệt độ cao. Khi nêu cả hai, mặc nhiên hiểu "
      "là quan hệ áp suất–nhiệt độ tuyến tính nối hai điểm đó.",
      "The rating of valves defines the pressure-temperature relationship "
      "within which the valve may be operated; the responsibility for "
      "determining ratings has been left largely to the manufacturer. The "
      "U.S. practice of stating the rating of general-purpose valves as WOG "
      "(water, oil, gas) and WSP (wet steam pressure) is a carryover from "
      "the days when these were the substances generally carried: WOG refers "
      "to the room-temperature rating, WSP is usually the high-temperature "
      "rating. When both are given, a straight-line pressure-temperature "
      "relationship is generally understood to exist between the two points.")
    P("Một số tiêu chuẩn Mỹ và Anh cho van bích đặt định mức bằng định mức "
      "bích tiêu chuẩn; cả hai nhóm tiêu chuẩn cũng chỉ định vật liệu cho "
      "các chi tiết chịu áp. Định mức van đầu hàn thường bằng van bích, "
      "nhưng tiêu chuẩn có thể cho phép thiết kế theo định mức riêng đáp "
      "ứng điều kiện vận hành thực tế. Nếu van chứa bộ phận bằng polymer, "
      "quan hệ áp suất–nhiệt độ bị giới hạn bởi tính chất polymer; một số "
      "tiêu chuẩn (ví dụ van bi) nêu giới hạn P-T cho van. Nếu không có tiêu "
      "chuẩn như vậy, nhà sản xuất phải nêu giới hạn áp suất và nhiệt độ của "
      "van.",
      "Some U.S. and British standards for flanged valves set ratings equal "
      "to the standard flange rating and specify the permissible materials "
      "for the pressure-containing parts. The rating of welding-end valves "
      "frequently corresponds to that of flanged valves, but standards may "
      "permit special ratings meeting the actual operating conditions. If "
      "the valve contains polymeric components, the pressure-temperature "
      "relationship is limited by the properties of the polymer; some "
      "standards (e.g. ball valves) specify P-T limits for the valve, and "
      "where they do not, it is the manufacturer's responsibility to state "
      "the pressure and temperature limitations.")

    H("Bảng chọn van", "Valve selection chart", h3)
    P("Bảng 3-1 dựa trên các nguyên tắc trên và dùng để chọn van cho một "
      "nhiệm vụ khống chế dòng cho trước. Vật liệu thân van do áp suất và "
      "nhiệt độ vận hành cùng tiêu chuẩn áp dụng, và tính chất chất lỏng "
      "(ăn mòn, xói mòn) quyết định. Vật liệu chỗ kín bàn ở đơn vị 2. Cách "
      "tốt nhất là tra catalogue nhà sản xuất, vốn nêu vật liệu tiêu chuẩn "
      "cho điều kiện vận hành cho trước; nhưng người mua phải đảm bảo vật "
      "liệu thân van tương thích với chất lỏng. Nếu chi phí van chọn ban "
      "đầu quá cao, phải xét tính phù hợp của các kiểu van khác; đôi khi "
      "phải thỏa hiệp. Quy trình chọn đòi hỏi kiến thức về các kiểu van và "
      "biến thể hiện có, và có thể cả các tiêu chuẩn van — thông tin này "
      "trình bày ở các mục tiếp theo.",
      "The valve selection chart in Table 3-1 is based on the foregoing "
      "guidelines and may be used to select the valve for a given "
      "flow-regulating duty. The construction material follows from the "
      "operating pressure and temperature in conjunction with the applicable "
      "standard, and from the properties of the fluid (corrosive, erosive). "
      "Seating-material selection is discussed in unit 2. The best approach "
      "is to consult the manufacturer's catalogue, which usually states the "
      "standard construction material for given operating conditions; "
      "however, it is the purchaser's responsibility to ensure the material "
      "is compatible with the fluid. If the cost of the initially selected "
      "valve is too high for the purpose, the suitability of other types "
      "must be investigated; sometimes a compromise has to be made. The "
      "procedure requires knowledge of the available valve types and their "
      "variations, and possibly of the valve standards — this information "
      "is given in the sections that follow.")
    _sel_chart(b, vi)

    # -------------------------------------------------------- globe valves
    H("Van cầu", "Globe valves")
    P("Van cầu là van đóng hướng trục trong đó phần đóng di chuyển vuông "
      "góc đóng mở trên chỗ kín; theo thói quen phần đóng được gọi là đĩa "
      "bất kể hình dạng của nó. Với kiểu di chuyển này, chỗ kín thay đổi tỉ "
      "lệ trực tiếp với hành trình đĩa — quan hệ lý tưởng cho khống chế lưu "
      "lượng. Ngoài ra tải chỗ kín của van cầu có thể khống chế chắc chắn "
      "bằng trục vít, và đĩa áp lên chỗ kín với ma sát nhỏ hoặc không, tùy "
      "thiết kế chỗ kín và đĩa — do đó khả năng làm kín tiềm năng cao. Mặt "
      "hạn chế: chỗ kín có thể giữ rắn từ chất lỏng chảy qua.",
      "Globe valves are closing-down valves in which the closure member is "
      "moved squarely on and off the seat; it is customary to refer to the "
      "closure member as a disc irrespective of its shape. By this mode of "
      "disc travel, the seat opening varies in direct proportion to the "
      "travel of the disc — ideally suited for regulating flow rate. In "
      "addition, the seating load can be positively controlled by a screwed "
      "stem, and the disc moves with little or no friction onto the seat, "
      "depending on the seat and disc design — the sealing capacity is "
      "therefore potentially high. On the debit side, the seatings may trap "
      "solids travelling in the flowing fluid.")
    P("Van cầu cũng dùng được cho nhiệm vụ on/off nếu trở lực của đường dòng "
      "khúc khuỷu chấp nhận được; một số van cầu được thiết kế trở lực thấp "
      "riêng cho mục đích này. Nếu van phải mở đóng thường xuyên, van cầu "
      "cực kỳ phù hợp nhờ hành trình đĩa ngắn giữa vị trí mở và đóng và chỗ "
      "kín bền bỉ với các chuyển động đó. Nhờ dải nhiệm vụ rộng này, van "
      "cầu phát triển nhiều biến thể nhằm đáp ứng một nhiệm vụ cụ thể với "
      "chi phí thấp nhất: các Hình 3-2 đến 3-11 là các biến thể phổ biến "
      "trong đường ống để khống chế dòng; Hình 3-12 đến 3-14 là các van "
      "chuyên dụng cho nhiệm vụ đặc biệt như ghi chú trong chú thích hình.",
      "Globe valves may of course be used for on-off duty provided the flow "
      "resistance from the tortuous flow passage can be accepted; some are "
      "designed for low flow resistance specifically for on-off duty. If "
      "the valve has to be opened and closed frequently, globe valves are "
      "ideally suited because of the short disc travel and the inherent "
      "robustness of the seatings to these movements. This wide range of "
      "duties has led to numerous variations designed to meet a particular "
      "duty at the lowest cost: Figures 3-2 through 3-11 show valves "
      "commonly used in pipelines for flow control; Figures 3-12 through "
      "3-14 are specialty valves for special duties, as described in their "
      "captions.")
    H("Kiểu thân van", "Valve body patterns", h3)
    P("Ba kiểu thân van cầu cơ bản: kiểu chuẩn (Hình 3-2, 3-3, 3-5, 3-6, "
      "3-9, 3-11), kiểu góc (Hình 3-4, 3-8) và kiểu nghiêng (Hình 3-7, 3-10, "
      "3-12, 3-13). Kiểu chuẩn phổ biến nhất nhưng do đường dòng khúc khuỷu "
      "mà có trở lực dòng cao nhất. Nếu van lắp gần khúc cua ống, thân kiểu "
      "góc có hai lợi thế: trở lực giảm mạnh so với kiểu chuẩn, và giảm số "
      "mối nối ống, tiết kiệm một khúc cua. Thân kiểu nghiêng được thiết kế "
      "để giảm trở lực tới mức tối thiểu — đạt tốt nhất ở van Hình 3-10, "
      "kết hợp trở lực thấp cho on/off với sự bền bỉ của chỗ kín van cầu.",
      "The basic globe-body patterns are the standard pattern (Figures 3-2, "
      "3-3, 3-5, 3-6, 3-9, 3-11), the angle pattern (Figures 3-4, 3-8) and "
      "the oblique pattern (Figures 3-7, 3-10, 3-12, 3-13). The standard "
      "pattern is the most common but offers, by its tortuous flow passage, "
      "the highest resistance to flow. If the valve is mounted near a pipe "
      "bend, the angle-pattern body offers two advantages: greatly reduced "
      "flow resistance, and fewer pipe joints — it saves a pipe elbow. The "
      "oblique pattern is designed to reduce the flow resistance to a "
      "minimum, particularly well achieved in Figure 3-10, which combines "
      "low flow resistance for on-off duty with the robustness of "
      "globe-valve seatings.")
    FIG(2, F3.fig_vsh_3_2())
    FIG(3, F3.fig_vsh_3_3())
    FIG(4, F3.fig_vsh_3_4())
    FIG(5, F3.fig_vsh_3_5())
    FIG(6, F3.fig_vsh_3_6())
    FIG(7, F3.fig_vsh_3_7())
    FIG(8, F3.fig_vsh_3_8())
    FIG(9, F3.fig_vsh_3_9())
    FIG(10, F3.fig_vsh_3_10())
    FIG(11, F3.fig_vsh_3_11())
    P("Các van chuyên dụng: Hình 3-12 là van cầu kiểu nghiêng, thân tách "
      "lùa, có cơ chế quét chỗ kín cho dịch vụ slurry (hỗn hợp quánh); Hình 3-13 "
      "là van cầu cải biến để xả bình chứa, chỗ kín sát đáy bình; "
      "Hình 3-14 là van cầu ba lộ dùng làm van chuyển mạch trong thiết bị "
      "van an toàn áp suất: một van an toàn bị cô lập trong khi van kia "
      "đang phục vụ.",
      "The specialty valves: Figure 3-12 shows an oblique-pattern globe "
      "with split body and seat-wiping mechanism for slurry service; "
      "Figure 3-13 a globe adapted for draining vessels with the seat flush "
      "with the bottom of the vessel; Figure 3-14 a three-way globe used as "
      "change-over valve in pressure-relief-valve installations — one PRV "
      "isolated while the second is in service.")
    FIG(12, F3.fig_vsh_3_12())
    FIG(13, F3.fig_vsh_3_13())
    FIG(14, F3.fig_vsh_3_14())

    H("Chỗ kín van", "Valve seatings", h3)
    P("Van cầu dùng chỗ kín kim loại hoặc chỗ kín mềm. Với chỗ kín kim loại, "
      "ứng suất chỗ kín phải không chỉ cao mà còn đều theo chu vi để đạt "
      "độ kín mong muốn. Các yêu cầu này dẫn tới nhiều thiết kế chỗ kín; "
      "Hình 3-15 là các biến thể phổ biến.",
      "Globe valves may be provided with metal or soft seatings. With metal "
      "seatings, the seating stress must not only be high but also "
      "circumferentially uniform to achieve the desired fluid tightness. "
      "These requirements have led to a number of seating designs; those "
      "shown in Figure 3-15 are common variations.")
    FIG(15, F3.fig_vsh_3_15())
    P("<b>Chỗ kín phẳng</b> (Hình 3-15a) có ưu điểm tự căn chỉnh với nhau "
      "mà không cần dẫn hướng đĩa chặt chẽ; nếu đĩa áp xuống không kèm xoay "
      "thì hai mặt khớp nhau không ma sát, nên độ chống kẹt dính (galling) "
      "của vật liệu không quan trọng. Biến dạng tròn của chỗ kín do ứng suất "
      "đường ống không cản trở độ kín chừng nào mặt chỗ kín còn phẳng. Nếu "
      "dòng chảy từ phía trên đĩa, mặt chỗ kín được che khỏi va đập trực "
      "tiếp của rắn hoặc giọt lỏng.",
      "<b>Flat seatings</b> (Figure 3-15a) align readily to each other "
      "without close disc guiding; if the disc is moved onto the seat "
      "without being rotated, the seatings mate without friction, so "
      "galling resistance of the material is unimportant. Distortion of "
      "seat roundness by pipeline stresses does not interfere with "
      "sealability as long as the seat face remains flat. If flow is "
      "directed from above the seat, the seating faces are protected from "
      "the direct impact of solids or liquid droplets.")
    P("<b>Chỗ kín côn</b> (Hình 3-15b, c, d) tăng mạnh ứng suất chỗ kín cho "
      "cùng một tải, nhưng chỉ hiệu quả nếu hai mặt khớp hoàn hảo — đĩa "
      "không được đặt lệch, phải dẫn hướng đúng, và mặt chỗ kín phải tròn "
      "tuyệt đối — điều khó duy trì ở van lớn khi ứng suất đường ống có thể "
      "làm méo chỗ kín. Ngoài ra khi siết chặt, đĩa trượt sâu vào chỗ kín "
      "dưới ma sát, nên vật liệu phải chống kẹt dính.",
      "<b>Tapered seatings</b> (Figure 3-15b, c, d) greatly increase the "
      "seating stress for a given load, but only if the seatings mate "
      "perfectly — the disc must not land cocked, must be properly guided, "
      "and the faces must be perfectly round, which is difficult to "
      "maintain in larger valves where pipeline stresses may distort the "
      "seat. Furthermore, as the seatings tighten, the disc slips deeper "
      "under friction, so the materials must be galling-resistant.")
    P("Chỗ kín côn mặt hẹp (b) có ứng suất đặc biệt cao nhưng mặt hẹp không "
      "dẫn được đĩa thẳng trục; nếu dẫn hướng tốt thì đạt độ kín cực cao — "
      "nhưng dễ hư hỏng bởi rắn và giọt lỏng nên chủ yếu cho khí không có "
      "rắn và giọt. Để tăng độ bền mà không mất ứng suất, chỗ kín (c) có "
      "mặt rộng dẫn đĩa vào chỗ kín, với mặt tiếp xúc ban đầu hẹp khoảng "
      "3 mm (⅛ in), phần còn lại của lòng chỗ kín côn dốc hơn; khi tải "
      "tăng, đĩa trượt sâu làm rộng mặt kín — ít bị xói mòn hơn (b), và "
      "côn dài của đĩa cải thiện đặc tính khống chế. Hiệu năng có thể cải "
      "thiện thêm bằng cách khoét rỗng đĩa (như van Hình 3-11) để đĩa có độ "
      " đàn hồi thích nghi với sai lệch độ tròn.",
      "Narrow-faced tapered seatings (b) have particularly high stress but "
      "cannot guide the disc squarely; properly guided, they achieve an "
      "extremely high degree of fluid tightness — yet they are readily "
      "damaged by solids or droplets, so they serve mainly for gases free "
      "of solids and droplets. To improve robustness without sacrificing "
      "stress, the seatings in (c) are tapered with wide faces that guide "
      "the disc, the initial contact face being about 3 mm (1/8 in.) wide "
      "with the remainder of the seat bore tapered slightly steeper; as the "
      "load increases the disc slips deeper, widening the seating width — "
      "less readily eroded than (b), and the long disc taper improves the "
      "throttling characteristic. Performance may be further improved by "
      "hollowing out the disc (Figure 3-11) to give the disc shell "
      "elasticity to adapt to roundness deviations.")
    P("Chỗ kín bi (d): đĩa hình bi trên chỗ kín côn, đĩa có thể lăn nhẹ trên "
      "chỗ kín đến khi căn thẳng; tiếp xúc gần trục tuyến nên ứng suất rất "
      "cao, nhưng tiếp xúc tuyến dễ hư hỏng vì xói mòn — chỉ dùng cho khí "
      "khô, không rắn; cấu trúc này chủ yếu của các nhà sản xuất Mỹ.",
      "Ball-shaped seatings (d): a ball disc on a tapered seat; the disc "
      "can roll to some extent on the seat until aligned. Because contact "
      "approaches line contact, the stress is very high — but line contact "
      "is prone to erosion damage, so this construction serves only for dry "
      "gases free of solids, and is used mainly by U.S. manufacturers.")
    FIG(16, F3.fig_vsh_3_16())
    P("Nếu van dùng cho khống chế mịn, đĩa thường có phần kéo dài hình kim "
      "(như van Hình 3-4) hoặc vây V-Port (như van Hình 3-8 và chỗ kín "
      "Hình 3-16). Trong thiết kế V-Port, mặt chỗ kín tách nhau trước khi "
      "các cổng V mở, nhờ đó mặt chỗ kín phần lớn được che khỏi xói mòn. "
      "Ví dụ chỗ kín mềm là van Hình 3-2: lắp ghép chỗ kín mềm được mang "
      "trên đĩa và có thể thay dễ dàng.",
      "For fine throttling duty, the disc is frequently provided with a "
      "needle-shaped extension (Figure 3-4) or a V-port skirt (Figure 3-8 "
      "and the seatings in Figure 3-16). In the V-port design the seating "
      "faces separate before the V-ports open, largely protecting the faces "
      "against erosion. An example of soft-seating design is the valve in "
      "Figure 3-2: the soft insert is carried by the disc and may be "
      "renewed readily.")

    H("Nối đĩa với trục", "Connection of disc to stem", h3)
    P("Trục van cầu có thể quay khi nâng hạ đĩa, hoặc bị chặn không quay "
      "khi thực hiện nhiệm vụ đó — hai kiểu vận hành chi phối thiết kế nối "
      "đĩa với trục. Phần lớn van cầu dùng trục quay vì thiết kế đơn giản. "
      "Nếu đĩa liền trục quay — thường gặp ở van kim nhỏ như Hình 3-4 — "
      "chỗ kín khớp nhau trong lúc quay và có thể mài mòn nặng; ứng dụng "
      "chính của loại này là khống chế dòng với tần suất đóng ít. Với mọi "
      "nhiệm vụ khác dùng trục quay, đĩa được thiết kế quay tự do (swivel) trên "
      "trục; nhưng đĩa lươn chỉ nên có hành trình dọc rất nhỏ để tránh dao "
      "động qua lại nhanh của đĩa trên trục ở gần vị trí đóng, và nếu đĩa "
      "được dẫn bởi trục, lateral play giữa trục và đĩa phải nhỏ để đĩa "
      "không đặt lệch lên chỗ kín.",
      "The stem may rotate while raising or lowering the disc, or be "
      "prevented from rotating — bearing on the disc-to-stem connection. "
      "Most globe valves incorporate a rotating stem for simplicity. If the "
      "disc is integral with the rotating stem — frequent in small needle "
      "valves (Figure 3-4) — the seatings mate while the disc rotates, "
      "possibly causing severe wear; such valves serve mainly regulating "
      "duty with infrequent shut-off. For all other duties with rotating "
      "stems the disc swivels freely on the stem; swivel discs should have "
      "minimum free axial play to prevent rapid reciprocating disc "
      "movements near the closed position, and if the disc is guided by the "
      "stem there should be little lateral play so the disc cannot land "
      "cocked on the seat.")
    P("Với trục không quay — các van Hình 3-6, 3-7, 3-10, 3-11 — đĩa hoặc "
      "liền trục (Hình 3-11) hoặc là chi tiết rời (Hình 3-6, 3-7, 3-10). "
      "Trục không quay bắt buộc ở van có gioăng trục dạng màng hoặc bellows "
      "(Hình 3-6, 3-7), và dùng ở van áp cao (Hình 3-10, 3-11) để dễ gắn "
      "cơ cấu chấp hành động lực.",
      "With nonrotating stems — Figures 3-6, 3-7, 3-10, 3-11 — the disc may "
      "be integral with the stem (Figure 3-11) or a separate component "
      "(Figures 3-6, 3-7, 3-10). Nonrotating stems are required in valves "
      "with diaphragm or bellows stem seals (Figures 3-6, 3-7), and are "
      "used in high-pressure valves (Figures 3-10, 3-11) to facilitate "
      "power operators.")

    H("Trục vít trong và ngoài", "Inside and outside stem screw", h3)
    P("Trục vít nâng hạ trục có thể đặt trong thân van (Hình 3-2 đến 3-4) "
      "hoặc ngoài thân van (Hình 3-5 đến 3-14). Trục vít trong cho kết cấu "
      "nắp kinh tế nhưng không bảo trì được từ bên ngoài, phù hợp nhất cho "
      "chất lỏng có độ bôi trơn tốt; với đại đa số nhiệm vụ nhỏ, trục vít "
      "trong vẫn cho dịch vụ tốt. Trục vít ngoài có thể bảo trì từ bên "
      "ngoài nên được ưu tiên cho nhiệm vụ khắc nghiệt.",
      "The screw may be located inside the valve body (Figures 3-2 through "
      "3-4) or outside (Figures 3-5 through 3-14). The inside screw permits "
      "an economical bonnet construction but cannot be serviced from "
      "outside — best suited for fluids of good lubricity; for the majority "
      "of minor duties it gives good service. The outside screw can be "
      "serviced from outside and is preferred for severe duties.")

    H("Mối nối nắp (bonnet)", "Bonnet joints", h3)
    P("Nắp có thể nối với thân bằng vặn, bích, hàn, hoặc cơ chế kín áp; "
      "hoặc nắp liền thân.",
      "Bonnets may be joined to the body by screwing, flanging, welding or "
      "a pressure-seal mechanism; or the bonnet may be integral with the "
      "body.")
    U([("<b>Nắp vặn</b> (Hình 3-4): đơn giản, rẻ nhất; nhưng gioăng nắp "
        "phải thích nghi với mặt quay, tháo lắp nhiều lần có thể hư hại mặt "
        "mối nối, và mô men siết rất lớn ở van cỡ lớn — nên hạn chế cho van "
        "tối đa DN 80 (NPS 3).",
        "<b>Screwed-in bonnet</b> (Figure 3-4): simplest and least "
        "expensive; but the gasket must accommodate rotating faces, "
        "frequent unscrewing may damage the joint faces, and the torque "
        "becomes very large for larger valves — restricted to sizes not "
        "greater than DN 80 (NPS 3)."),
       ("<b>Nắp hàn kín hoặc hàn hoàn toàn</b> (Hình 3-6, 3-7): nếu vật liệu "
        "hàn được, nắp vặn có thể hàn kín, hoặc mối nối hoàn toàn bằng hàn. "
        "Kinh tế và đáng tin nhất bất kể kích thước, áp suất, nhiệt độ; mặt "
        "trái: tiếp cận cơ cấu bên trong chỉ bằng phá mối hàn — dùng khi "
        "van cần không bảo trì lâu dài, van bỏ đi (throw-away), hoặc độ "
        "kín của mối nối quan trọng hơn khả năng tiếp cận.",
        "<b>Seal-welded or welded bonnet</b> (Figures 3-6, 3-7): if the "
        "material is weldable, the screwed-in bonnet may be seal welded, or "
        "the connection made entirely by welding — economical and most "
        "reliable irrespective of size, pressure and temperature; on the "
        "debit side, access to the internals only by removing the weld, so "
        "these are used where the valve can stay maintenance-free for long "
        "periods, is a throw-away valve, or where sealing reliability "
        "outweighs access."),
       ("<b>Nắp với vòng khớp nối rời</b> (Hình 3-2, 3-3): ngăn mọi chuyển "
        "động giữa các mặt mối nối khi siết, nên tháo nắp nhiều lần không "
        "dễ hại mặt nối; giới hạn kích thước như nắp vặn (DN 80).",
        "<b>Bonnet with screwed union ring</b> (Figures 3-2, 3-3): prevents "
        "any motion between the joint faces while tightening, so repeated "
        "unscrewing cannot readily harm the faces; size restriction as for "
        "screwed-in bonnets (DN 80)."),
       ("<b>Nắp bích</b> (Hình 3-8, 3-9): nỗ lực siết dàn trải qua nhiều "
        "bu lông, thiết kế được cho mọi kích thước và áp suất; nhưng khi "
        "kích thước và áp tăng, mối nối nặng và cồng kềnh; trên 350 °C "
        "chảy dẻo có thể giảm tải bu lông — ứng dụng tới hạn có thể hàn "
        "kín.",
        "<b>Flanged bonnet</b> (Figures 3-8, 3-9): tightening effort spread "
        "over a number of bolts, designable for any valve size and "
        "pressure; but increasingly heavy and bulky with size and "
        "pressure, and above 350 °C (660 °F) creep relaxation can lower the "
        "bolt load — critical applications may be seal welded."),
       ("<b>Nắp kín áp</b> (Hình 3-10): buộc áp suất chất lỏng siết mối "
        "nối — gioăng nắp càng kín hơn khi áp tăng; thường ưa chuộng cho "
        "van lớn ở áp suất và nhiệt độ cao.",
        "<b>Pressure-seal bonnet</b> (Figure 3-10): the fluid pressure "
        "tightens the joint — the seal becomes tighter as pressure "
        "increases; frequently preferred for large valves at high pressures "
        "and temperatures."),
       ("<b>Nắp liền thân</b> (Hình 3-5, 3-11): van nhỏ tránh hẳn mối nối "
        "nắp; tiếp cận cơ cấu qua miệng bộ ép gioăng (gland opening) đủ rộng cho "
        "các bộ phận van đi qua.",
        "<b>Integral bonnet</b> (Figures 3-5, 3-11): small valves avoid the "
        "bonnet joint altogether; access to the internals through the gland "
        "opening, which is large enough to pass the valve components.")])

    H("Hộp đón và chỗ kín ngược", "Stuffing boxes and back seating", h3)
    P("Hình 3-17 đến 3-19 cho thấy ba kiểu hộp đón điển hình của van trục "
      "nâng. Hộp đón cơ bản (Hình 3-17): khoang vòng chứa gioăng giữa gân "
      "ép phía trên và vai đỡ phía dưới; mặt dưới hộp đón mang chỗ kín "
      "ngược (back seat) — kết hợp với chỗ kín tương ứng quanh trục — dùng "
      "để cách ly gioăng khỏi chất lỏng hệ thống khi van mở hết cỡ.",
      "Figures 3-17 through 3-19 show three types of stuffing boxes typical "
      "for valves with a rising stem. The basic box (Figure 3-17) is an "
      "annular chamber containing the packing between the gland at the top "
      "and a shoulder at the bottom; the underside of the box carries a "
      "back seat which, with a corresponding seat around the stem, isolates "
      "the packing from the system fluid when the valve is fully open.")
    FIG(17, F3.fig_vsh_3_17())
    P("Hộp đón Hình 3-18 có thêm ngăn ngưng tụ phía dưới — nguyên thủy là "
      "ngăn làm mát cho khí có thể ngưng như hơi nước; trong trường hợp này "
      "ngăn ngưng có nắp thử (test plug) tháo ra để thử độ kín của chỗ kín "
      "ngược. Biến thể thứ ba (Hình 3-19) có vòng lantern đặt giữa hai đoạn "
      "gioăng, chủ yếu dùng với gioăng nén, có thể phục vụ bốn mục đích:",
      "The box in Figure 3-18 is supplemented with a condensing chamber at "
      "the bottom — originally a cooling chamber for condensable gases such "
      "as steam; here it carries a test plug which may be removed to test "
      "the back seat for leak tightness. A third variation (Figure 3-19) "
      "has a lantern ring mounted between two packing sections, mainly with "
      "compression packings, serving four different purposes:")
    FIG(18, F3.fig_vsh_3_18())
    U([("Buồng phun chất làm kín hoặc chất bôi trơn bị ép chui ra hoặc bị rửa "
        "trôi.", "Injection chamber for a sealant or for extruded or "
        "leached-out lubricant."),
       ("Buồng áp suất trong đó chất lỏng ngoài được ép tới áp bằng hoặc "
        "hơn nhẹ áp hệ thống để ngăn rò rỉ chất lỏng hệ thống ra ngoài — "
        "chất lỏng ngoài phải tương thích với chất lỏng hệ thống và vô hại "
        "với môi trường xung quanh van.",
        "Pressure chamber in which an external fluid is pressurized to "
        "equal or slightly above system pressure to prevent leakage of the "
        "system fluid — the external fluid must be compatible and harmless "
        "to the valve surroundings."),
       ("Buồng chất làm kín trong dịch vụ chân không, được cấp chất lỏng "
        "ngoài làm chất làm kín.",
        "Sealant chamber in vacuum service, fed with an external fluid "
        "acting as sealant."),
       ("Buồng thu gom rò rỉ, từ đó dẫn rò rỉ đến vị trí an toàn.",
        "Leakage collection chamber from which leakage is piped to a safe "
        "location.")])
    FIG(19, F3.fig_vsh_3_19())
    P("Tuy nhiên vòng lantern làm sâu thêm cột gioăng; ma sát thành làm giảm "
      "tải ép truyền tới gioăng khi chiều sâu tăng, làm suy giảm độ kín. "
      "Trong kín trục bơm quay, thay vòng lantern bằng lò xo được dùng để "
      "cải thiện độ kín.",
      "The lantern ring, however, increases the packing depth; sidewall "
      "friction reduces the gland input load as the depth increases, "
      "impairing seal integrity. Replacing the lantern ring with a spring "
      "is used in rotating pump-shaft seals to improve integrity.")

    H("Hướng dòng chảy qua van cầu",
      "Direction of flow through globe valves", h3)
    P("Câu hỏi hướng dòng có hai lời giải. Nếu có khả năng dòng từ phía "
      "trên đĩa có thể tuột đĩa khỏi trục hoặc tuột bộ phận khỏi đĩa thì "
      "dòng từ dưới đĩa là bắt buộc. Với dòng từ dưới, van cầu tay với trục "
      "quay và chỗ kín kim loại chỉ đóng kín không tốn quá nhiều công nếu "
      "tải chất lỏng dưới đĩa không vượt quá khoảng 40–60 kN (9 000–13 000 "
      "lb); với trục không quay và đai ốc trục đỡ trên vòng bi lăn, như các van "
      "Hình 3-10 và 3-11, có thể đóng kín với tải khoảng 70–100 kN "
      "(16 000–22 000 lb), tùy tiêu chuẩn độ kín và kết cấu van. Ưu điểm "
      "riêng của dòng từ dưới: hộp đón của van đóng được giải tróng khỏi áp "
      "trước van. Mặt trái: nếu van đóng với chất lỏng nóng như hơi, co "
      "nhiệt của trục sau khi đóng có thể vừa đủ gây rò chỗ kín.",
      "The question of flow direction has two answers. If flow from above "
      "the disc could remove the disc from the stem or a component from the "
      "disc, flow directed from below the disc is mandatory. Hand-operated "
      "globe valves with rotating stem and metal seatings can then be "
      "closed fluid-tight without undue effort only if the fluid load on "
      "the underside of the disc does not exceed about 40–60 kN "
      "(9,000–13,000 lb); with a nonrotating stem and roller-bearing "
      "supported stem nut (Figures 3-10, 3-11), tight closure is possible "
      "against about 70–100 kN (16,000–22,000 lb), depending on the leakage "
      "criterion and valve construction. One advantage of flow from below: "
      "the stuffing box of the closed valve is relieved from the upstream "
      "pressure. On the debit side, closing against a hot fluid such as "
      "steam, thermal contraction of the stem afterwards can be just enough "
      "to induce seat leakage.")
    P("Nếu dòng từ trên đĩa, lực đóng từ áp chất lỏng đè lên đĩa hỗ trợ lực "
      "đóng từ trục — độ kín của van tăng rất nhiều. Với trục quay, van mở "
      "bằng tay chỉ không quá tốn công nếu tải trên đĩa không vượt khoảng "
      "40–60 kN; với trục không quay và đai ốc trên vòng bi lăn, có thể mở bằng "
      "tay với tải tới khoảng 70–100 kN. Nếu tải trên đĩa cao hơn, có thể "
      "phải trang bị van bypass cho phép gia áp hệ thống phía hạ lưu trước "
      "khi mở van cầu.",
      "If flow is directed from above the disc, the closing force from the "
      "fluid on top of the disc supplements the stem force — greatly "
      "increasing sealing reliability. With a rotating stem the valve may "
      "be opened without excessive effort only if the fluid load does not "
      "exceed about 40–60 kN; with a nonrotating stem and roller-bearing "
      "stem nut, hand opening is possible against about 70–100 kN. If the "
      "load is higher, a bypass valve may have to be provided to pressurize "
      "the downstream system before the globe valve is opened.")
    P("Phụ lục C liệt kê các tiêu chuẩn Mỹ và Anh về van cầu.",
      "Appendix C lists the U.S. and British standards pertaining to globe "
      "valves.")
    P("<b>Nhiệm vụ:</b> khống chế dòng · dừng và khởi động dòng · thao tác "
      "van thường xuyên. <b>Dịch vụ:</b> khí về cơ bản không có rắn · chất "
      "lỏng về cơ bản không có rắn · chân không · lạnh sâu (cryogenic).",
      "<b>Duty:</b> controlling flow · stopping and starting flow · "
      "frequent valve operation. <b>Service:</b> gases essentially free of "
      "solids · liquids essentially free of solids · vacuum · cryogenic.")

    # -------------------------------------------------------- piston valves
    H("Van piston", "Piston valves")
    P("Van piston là van đóng hướng trục trong đó bộ phận đóng hình piston "
      "chui vào hoặc rút khỏi lòng chỗ kín (Hình 3-20 đến 3-24). Chỗ kín "
      "đạt được giữa mặt bên của piston và lòng chỗ kín. Khi mở, dòng không "
      "bắt đầu cho tới khi piston rút hoàn toàn khỏi lòng chỗ kín — mọi "
      "hư hỏng xói mòn do đó xảy ra xa các mặt chỗ kín. Khi đóng, piston có "
      "xu hướng quét sạch rắn có thể đọng trên chỗ kín; van piston vì vậy "
      "xử lý được chất lỏng có rắn lơ lửng. Nếu chỗ kín hư hỏng, piston và "
      "chỗ kín thay tại chỗ, van như mới mà không cần gia công.",
      "Piston valves are closing-down valves in which a piston-shaped "
      "closure member intrudes into or withdraws from the seat bore "
      "(Figures 3-20 through 3-24). The seat seal is achieved between the "
      "lateral faces of the piston and the seat bore. When the valve opens, "
      "flow cannot start until the piston has been completely withdrawn — "
      "erosive damage occurs away from the seating surfaces. When closing, "
      "the piston tends to wipe away solids deposited on the seat, so "
      "piston valves may handle fluids carrying solids in suspension. If "
      "the seatings are damaged, piston and seat can be replaced in situ — "
      "the valve is like new without any machining.")
    FIG(20, F3.fig_vsh_3_20())
    FIG(21, F3.fig_vsh_3_21())
    FIG(22, F3.fig_vsh_3_22())
    FIG(23, F3.fig_vsh_3_23())
    FIG(24, F3.fig_vsh_3_24())
    P("Giống van cầu, van piston cho khống chế dòng tốt; nếu cần chỉnh dòng "
      "nhạy, piston có thể trang bị phần kéo dài hình kim. Van piston cũng "
      "dùng để dừng/khởi động dòng khi trở lực của đường dòng khúc khuỷu "
      "được chấp nhận.",
      "Like globe valves, piston valves permit good flow control; for "
      "sensitive adjustment the piston may be fitted with a needle-shaped "
      "extension. They are also used for stopping and starting flow when "
      "the flow resistance of the tortuous passage is accepted.")
    H("Kết cấu", "Construction", h3)
    P("Chỗ kín van piston tạo bởi mặt bên của lòng van và piston. Tiếp xúc "
      "kín chất lỏng giữa hai mặt đạt bằng một gioăng thuộc về lòng van "
      "(Hình 3-20 đến 3-22) hoặc thuộc về piston (Hình 3-23, 3-24). Gioăng "
      "thường dùng là gioăng nén trên amiang nén hoặc PTFE và gioăng O-ring.",
      "The seatings are formed by the lateral faces of the valve bore and "
      "the piston. Fluid-tight contact is achieved by a packing forming "
      "part of the valve bore (Figures 3-20 through 3-22) or part of the "
      "piston (Figures 3-23, 3-24). Packings commonly used are compression "
      "packings based on compressed asbestos or PTFE, and O-ring packings.")
    P("Ở van Hình 3-20, piston chạy trong hai gioăng cách nhau bằng vòng "
      "lantern: gioăng dưới là gioăng chỗ kín, gioăng trên kín piston với "
      "khí quyển; nắp van đồng thời là bộ ép gioăng cho phép siết cả hai gioăng "
      "qua bu lông nắp. Lò xo đĩa dưới đai ốc bu lông giảm biến thiên ứng "
      "suất gioăng do giãn nở nhiệt. Khi một gioăng rò, khôi phục độ kín "
      "bằng siết lại bu lông — phải thực hiện khi van đóng để gioăng chỗ "
      "kín không giãn nở tự do vào lòng van. Van Hình 3-21 chỉ khác ở piston "
      "được cân bằng áp.",
      "In the Figure 3-20 valve the piston moves in two packings separated "
      "by a lantern ring: the lower packing is the seat packing, the upper "
      "seals the piston to the atmosphere; the bonnet serves as the gland, "
      "letting both packings be tightened through the cover bolts. Disc "
      "springs under the bolt nuts minimize packing-stress variations from "
      "thermal expansion. If a packing leaks, the seal is restored by "
      "retightening — while the valve is closed, to prevent unrestrained "
      "expansion of the seat packing into the bore. The Figure 3-21 valve "
      "differs only in the pressure-balanced piston.")
    P("Bộ gioăng của van Hình 3-22 cũng được ứng suất qua nắp với lò xo dưới "
      "đai ốc bu lông hoặc lò xo giữa nắp và gioăng; khi piston vào vị trí "
      "đóng cuối, vai trên piston chạm vòng nén trên đỉnh gioăng nên hành "
      "trình tiếp theo siết gioăng chặt hơn nữa. Van Hình 3-23 mang gioăng "
      "chỗ kín trên đầu piston, đỡ bên dưới bằng vòng nén rời; khi piston "
      "đến vị trí đóng cuối, vòng nén tựa lên vai trong lòng chỗ kín — hành "
      "trình tiếp theo làm vòng nén siết gioăng. Vì gioăng chỉ tạo áp âu "
      "trong các giai đoạn đóng cuối, nỗ lực vận hành thấp hơn trên một "
      "phần hành trình so với các van trên — nguyên tắc Ram-Seal. Van "
      "Hình 3-24 cũng mang gioăng trên piston nhưng thay vòng nén rời bằng "
      "vòng ma sát hoạt động như phần tử lò xo, ứng suất trước gioăng; khi "
      "piston vào chỗ kín, vòng ma sát tựa trong lòng chỗ kín và hành trình "
      "tiếp theo tăng ứng suất gioăng.",
      "The packing train of Figure 3-22 is likewise stressed through the "
      "bonnet with springs under the bolt nuts or between bonnet and "
      "packing; as the piston reaches the final closing position a shoulder "
      "on the piston contacts a compression ring on top of the packing, so "
      "further travel tightens the packing further. The Figure 3-23 valve "
      "carries the seat packing on the end of the piston, supported from "
      "below by a loose compression ring; in the final closing position the "
      "ring comes to rest on a shoulder in the seat bore, and further "
      "progression tightens the packing. Because the packing establishes "
      "interference only in the last closing stages, the operating effort "
      "is lower over part of the travel — the Ram-Seal principle. The "
      "Figure 3-24 valve also carries the packing on the piston, but the "
      "loose ring is replaced by a friction ring acting as a spring "
      "element pre-stressing the packing; as the piston enters the seat the "
      "ring comes to rest in the bore and further travel increases the "
      "packing stress.")
    P("Tiêu chuẩn quốc gia riêng cho van piston hiện không tồn tại.",
      "National standards applying specifically to piston valves do not "
      "exist.")
    P("<b>Nhiệm vụ:</b> khống chế dòng · dừng và khởi động dòng. "
      "<b>Dịch vụ:</b> khí · chất lỏng · chất lỏng có rắn lơ lửng · chân "
      "không.",
      "<b>Duty:</b> controlling flow · stopping and starting flow. "
      "<b>Service:</b> gases · liquids · fluids with solids in suspension · "
      "vacuum.")

    return "".join(b)


def _sel_chart(b, vi):
    """Source Table 3-1 — Valve Selection Chart (transcribed; a dash marks
    a cell the source leaves blank)."""
    def cell(v):
        if v == "Y":
            return "Yes" if not vi else "Có"
        if v == "M":
            return "moderate" if not vi else "trung bình"
        if v == "S":
            return "special" if not vi else "đặc biệt"
        return "—" if not vi else "—"
    hdr = ["Nhóm", "Kiểu van", "On-off", "Khống chế", "Phân luồng",
           "Rắn không mài mòn", "Rắn mài mòn", "Dính", "Vệ sinh"] if vi else \
          ["Group", "Valve type", "On-off", "Throttling", "Diverting",
           "Solids non-abrasive", "abrasive", "Sticky", "Sanitary"]
    rows = [
        ["Closing down", "Globe — straight pattern", "YY Y", "", "", "", "", "", ""],
    ]
    data = [
        ("g1", "Globe — straight pattern", ["Y", "Y", "Y", "", "", "", ""]),
        ("g1", "Globe — angle pattern", ["Y", "Y", "", "Y", "S", "S", ""]),
        ("g1", "Globe — oblique pattern", ["Y", "Y", "", "Y", "", "S", ""]),
        ("g1", "Globe — multiport pattern", ["Y", "Y", "Y", "", "", "", ""]),
        ("g1", "Piston", ["Y", "Y", "", "Y", "", "S", ""]),
        ("g2", "Parallel gate — conventional", ["Y", "Y", "", "Y", "", "", ""]),
        ("g2", "Parallel gate — conduit gate", ["Y", "Y", "Y", "Y", "", "", ""]),
        ("g2", "Parallel gate — knife gate", ["Y", "S", "", "Y", "Y", "Y", ""]),
        ("g2", "Wedge gate — with bottom cavity", ["Y", "", "", "Y", "", "", ""]),
        ("g2", "Wedge gate — rubber seated, no cavity",
         ["Y", "M", "", "Y", "Y", "", ""]),
        ("g3", "Plug — non-lubricated", ["Y", "M", "Y", "Y", "", "Y", ""]),
        ("g3", "Plug — lubricated", ["Y", "Y", "Y", "Y", "Y", "", ""]),
        ("g3", "Plug — eccentric", ["Y", "M", "", "Y", "", "Y", ""]),
        ("g3", "Plug — lift plug", ["Y", "Y", "Y", "Y", "", "", ""]),
        ("g3", "Ball", ["Y", "M", "Y", "Y", "", "", ""]),
        ("g3", "Butterfly", ["Y", "Y", "S", "Y", "Y", "Y", ""]),
        ("g4", "Pinch", ["Y", "Y", "S", "Y", "Y", "Y", "Y"]),
        ("g4", "Diaphragm — weir type", ["Y", "Y", "", "Y", "Y", "Y", "Y"]),
        ("g4", "Diaphragm — straight-through",
         ["Y", "M", "", "Y", "Y", "Y", "Y"]),
    ]
    gname = {"g1": "Đóng hướng trục" if vi else "Closing down",
             "g2": "Trượt" if vi else "Sliding",
             "g3": "Quay" if vi else "Rotating",
             "g4": "Thân mềm" if vi else "Flexing"}
    rows = []
    last = None
    for g, typ, cells in data:
        if g != last:
            rows.append(gname[g])
            last = g
        rows.append([typ] + [cell(c) for c in cells])
    cap = ("Ô nét gạch là ô bảng gốc để trống — bảng nguồn không chỉ dẫn "
           "cho ô đó." if vi else
           "A dash marks a cell the source table leaves blank.")
    b.append(table(hdr, rows, caption=cap, cls="tbl wide"))


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
