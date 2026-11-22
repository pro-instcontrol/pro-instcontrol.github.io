# -*- coding: utf-8 -*-
"""Book 7c, Chapter 1 — Introduction to Control Valves (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 16-33.
The chapter is essentially a terminology handbook: it defines, in five
sections, the terms used for sliding-stem valves, rotary valves, valve
functions and characteristics, and general process control. All nineteen
numbered source figures (1.1-1.19) are redrawn as vector schematics in
`cvh6fig.py` and placed at the points where the source captions occur.
"""

from cvh6_common import (fig, h2, h3, lead, note, p, ul)
import cvh6fig as F

PAGES_SRC = 18          # source printed pp. 16-33 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Introduction to Control Valves"
TITLE_VI = "Giới thiệu về van điều khiển"


def _defs(pairs, lang):
    """Render a bilingual glossary block as a definition list.

    Each item is ((vi_term, vi_def), (en_term, en_def)); the Vietnamese member
    is primary and the English member mirrors it.
    """
    out = []
    for vi, en in pairs:
        term, dfn = vi if lang == "vi" else en
        out.append("<b>%s</b> — %s" % (term, dfn))
    return ul(out)


# ===========================================================================
# 1.2 Sliding-stem control valve terminology (source pp. 17-23)
# ===========================================================================
_D12_A = [
    (("Lò xo cơ cấu chấp hành", "Một lò xo hoặc nhóm lò xo đặt trong ách, vỏ cơ cấu chấp hành "
      "hoặc xi lanh piston, có tác dụng đẩy thân cơ cấu chấp hành theo hướng ngược với hướng "
      "do áp suất nạp tạo ra."),
     ("Actuator Spring", "A spring, or group of springs, enclosed in the yoke or actuator "
      "casing or piston cylinder that moves the actuator stem in a direction opposite to that "
      "created by loading pressure.")),
    (("Thân cơ cấu chấp hành", "Chi tiết nối cơ cấu chấp hành với thân van và truyền chuyển động "
      "(lực) từ cơ cấu chấp hành tới van."),
     ("Actuator Stem", "The part that connects the actuator to the valve stem and transmits "
      "motion (force) from the actuator to the valve.")),
    (("Đoạn nối dài thân cơ cấu chấp hành", "Đoạn nối dài của thân cơ cấu chấp hành kiểu piston, "
      "dùng để truyền chuyển động piston tới bộ định vị van."),
     ("Actuator Stem Extension", "An extension of the piston actuator stem to provide a means "
      "of transmitting piston motion to the valve positioner.")),
    (("Lực thân cơ cấu chấp hành", "Lực ròng từ cơ cấu chấp hành sẵn có để định vị thực tế nút "
      "van, còn gọi là hành trình van."),
     ("Actuator Stem Force", "The net force from an actuator that is available for actual "
      "positioning of the valve plug, referred to as valve travel.")),
]

_D12_B = [
    (("Đáy van (Bottom Flange)", "Chi tiết đóng một lỗ mở của thân van ở phía đối diện với lỗ mở "
      "của nắp van. Có thể chứa bạc dẫn hướng hoặc cho phép đảo chiều tác động của van."),
     ("Bottom Flange", "A part that closes a valve body opening opposite the bonnet opening. "
      "It can include a guide bushing and/or serve to allow reversal of the valve action.")),
    (("Bạc lót (Bushing)", "Thiết bị đỡ và/hoặc dẫn hướng các chi tiết chuyển động như thân van "
      "và nút van."),
     ("Bushing", "A device that supports and/or guides moving parts such as valve stems and plugs.")),
    (("Lồng (Cage)", "Một phần của bộ trim bao quanh phần đóng, có thể tạo đặc tính dòng và/hoặc "
      "bề mặt chỗ ngồi. Nó cũng tạo độ ổn định, dẫn hướng, cân bằng và căn chỉnh, đồng thời "
      "giúp lắp ráp các chi tiết khác của trim. Thành lồng có các lỗ thường quyết định đặc tính "
      "dòng của van."),
     ("Cage", "A part of the valve trim that surrounds the closure member and can provide flow "
      "characterization and/or a seating surface. It also provides stability, guiding, balance, "
      "and alignment, and facilitates assembly of other parts of the valve trim. The walls of "
      "the cage contain openings that usually determine the flow characteristic of the control "
      "valve.")),
    (("Phần đóng (Closure Member)", "Bộ phận di động của van được định vị trong đường dòng để "
      "điều chỉnh lưu lượng qua van."),
     ("Closure Member", "The movable part of the valve that is positioned in the flow path to "
      "modulate the rate of flow through the valve.")),
    (("Dẫn hướng phần đóng", "Phần của phần đóng căn chỉnh chuyển động của nó trong lồng, vòng "
      "chỗ ngồi (dẫn theo cổng), nắp van, đáy van, thân van hoặc bất kỳ hai trong số đó."),
     ("Closure Member Guide", "That portion of a closure member that aligns its movement in "
      "either a cage, seat ring (port guiding), bonnet, bottom flange, stem or any two of these.")),
    (("Xi lanh (Cylinder)", "Buồng của cơ cấu chấp hành piston, nơi piston chuyển động."),
     ("Cylinder", "The chamber of a piston actuator in which the piston moves.")),
    (("Chỗ kín đầu xi lanh", "Chi tiết làm kín tại điểm nối xi lanh cơ cấu chấp hành piston với ách."),
     ("Cylinder Closure Seal", "The sealing element at the connection of the piston actuator "
      "cylinder to the yoke.")),
    (("Màng (Diaphragm)", "Chi tiết mềm, nhạy áp, truyền lực tới đĩa màng và thân cơ cấu chấp hành."),
     ("Diaphragm", "A flexible, pressure responsive element that transmits force to the "
      "diaphragm plate and actuator stem.")),
    (("Cơ cấu chấp hành màng", "Thiết bị chạy bằng chất lỏng, thường là khí nén, tác động lên "
      "màng mềm để tạo lực di chuyển phần đóng."),
     ("Diaphragm Actuator", "A fluid-powered device in which the fluid, usually compressed air, "
      "acts upon a flexible component, the diaphragm to produce a force to move the closure "
      "member.")),
    (("Vỏ màng (Diaphragm Case)", "Vỏ gồm phần trên và phần dưới, dùng để đỡ màng và tạo một "
      "hoặc hai buồng áp suất."),
     ("Diaphragm Case", "A housing, consisting of top and bottom section, used for supporting "
      "a diaphragm and establishing one or two pressure chambers.")),
    (("Đĩa màng (Diaphragm Plate)", "Đĩa cứng, đồng tâm với màng, dùng để truyền lực tới thân "
      "cơ cấu chấp hành."),
     ("Diaphragm Plate", "A rigid plate concentric with the diaphragm for transmitting force "
      "to the actuator stem.")),
    (("Cơ cấu chấp hành tác động trực tiếp", "Cơ cấu chấp hành mà thân dịch ra khi áp suất nạp "
      "tăng."),
     ("Direct-Acting Actuator", "An actuator in which the actuator stem extends with increasing "
      "loading pressure.")),
    (("Nắp kéo dài (Extension Bonnet)", "Nắp có kích thước lớn hơn giữa hộp đệm và bích nắp, "
      "dùng cho dịch vụ nóng hoặc lạnh."),
     ("Extension Bonnet", "A bonnet with greater dimension between the packing box and bonnet "
      "flange for hot or cold service.")),
    (("Van cầu (Globe Valve)", "Van có phần đóng chuyển động tuyến tính, một hoặc nhiều cổng, "
      "và thân được phân biệt bằng buồng hình cầu quanh vùng cổng. Van cầu được phân loại "
      "thành: hai chiều một cổng, hai chiều hai cổng, kiểu góc hoặc ba chiều."),
     ("Globe Valve", "A valve with a linear motion closure member, one or more ports, and a body "
      "distinguished by a globular shaped cavity around the port region. Globe valves can be "
      "further classified as: two-way single-ported, two-way double-ported, angle-style, or "
      "three-way.")),
    (("Áp suất nạp (Loading Pressure)", "Chất lỏng, thường là khí nén, được cấp vào màng hoặc "
      "piston của cơ cấu chấp hành khí nén."),
     ("Loading Pressure", "Fluid, usually compressed air, applied to the diaphragm or piston "
      "in a pneumatic actuator.")),
    (("Van lệch trục (Offset Valve)", "Cấu trúc van có các kết nối đường ống vào và ra nằm trên "
      "các mặt phẳng khác nhau nhưng quay ngược nhau 180 độ."),
     ("Offset Valve", "A valve construction having inlet and outlet line connections on "
      "different planes, but 180 degrees opposite each other.")),
]

_D12_C = [
    (("Hộp đệm (Packing Box)", "Bộ phận của cụm nắp dùng để làm kín chống rò rỉ quanh thân phần "
      "đóng. Bộ gồm nhiều tổ hợp của các chi tiết như gioăng đệm, đĩa ép gioăng, đai ốc gioăng, "
      "vòng lantern, lò xo gioăng, bích gioăng, vòng gioăng, vòng lau, lò xo Belleville, vòng "
      "chống đẩy ra."),
     ("Packing Box (Assembly)", "The part of the bonnet assembly used to seal against leakage "
      "around the closure member stem. Included in the complete packing box assembly are "
      "various combinations of some or all of the following component parts: packing, packing "
      "follower, packing nut, lantern ring, packing spring, packing flange, packing flange studs "
      "or bolts, packing flange nuts, packing ring, packing wiper ring, felt wiper ring, "
      "Belleville springs, anti-extrusion ring.")),
    (("Piston", "Chi tiết di động cứng, nhạy áp, truyền lực tới thân cơ cấu chấp hành piston."),
     ("Piston", "A rigid movable pressure responsive element that transmits force to the "
      "piston actuator stem.")),
    (("Cơ cấu chấp hành kiểu piston", "Thiết bị chạy bằng chất lỏng, thường là khí nén, tác dụng "
      "lên piston di động để tạo chuyển động cho thân và lực đóng khi đóng van. Được phân loại "
      "thành tác động kép (có thể phát lực toàn phần ở cả hai chiều) hoặc kiểu lò xo an toàn "
      "(spring-fail)."),
     ("Piston-Type Actuator", "A fluid powered device in which the fluid, usually compressed "
      "air, acts upon a movable piston to provide motion of the actuator stem and provide "
      "seating force upon closure. Piston-type actuators are classified as either double-acting, "
      "so that full power can be developed in either direction, or as spring-fail so that upon "
      "loss of supply power, the actuator moves the valve in the required direction of travel.")),
    (("Cổng (Port)", "Lỗ tiết lưu điều khiển dòng của van điều khiển."),
     ("Port", "The flow control orifice of a control valve.")),
    (("Vòng giữ (Retaining Ring)", "Vòng hở dùng để giữ một bích rời trên thân van."),
     ("Retaining Ring", "A split ring that is used to retain a separable flange on a valve body.")),
    (("Cơ cấu chấp hành tác động ngược", "Cơ cấu chấp hành mà thân thu vào khi áp suất nạp tăng. "
      "Có vòng đệm seal bushing lắp ở đầu trên của ách để chống rò áp nạp dọc thân."),
     ("Reverse-Acting Actuator", "An actuator in which the actuator stem retracts with increasing "
      "loading pressure. Reverse actuators have a seal bushing installed in the upper end of the "
      "yoke to prevent leakage of the loading pressure along the actuator stem.")),
    (("Ống cao su (Rubber Boot)", "Thiết bị bảo vệ ngăn vật liệu lạ gây hại xâm nhập vào vòng đệm "
      "seal bushing của cơ cấu chấp hành piston."),
     ("Rubber Boot", "A protective device to prevent entrance of damaging foreign material into "
      "the piston actuator seal bushing.")),
    (("Vòng đệm Seal Bushing", "Các bạc trên và dưới tạo phương thức làm kín xi lanh cơ cấu chấp "
      "hành piston chống rò rỉ. Vòng O-ring cao su tổng hợp được dùng trong các bạc này để làm "
      "kín xi lanh, thân và đoạn nối dài thân cơ cấu chấp hành."),
     ("Seal Bushing", "Top and bottom bushings that provide a means of sealing the piston "
      "actuator cylinder against leakage. Synthetic rubber O-rings are used in the bushings to "
      "seal the cylinder, the actuator stem, and the actuator stem extension.")),
    (("Chỗ ngồi (Seat)", "Vùng tiếp xúc giữa phần đóng và bề mặt ăn khớp, tạo nên độ đóng kín của van."),
     ("Seat", "The area of contact between the closure member and its mating surface that "
      "establishes valve shutoff.")),
    (("Tải chỗ ngồi (Seat Load)", "Lực tiếp xúc ròng giữa phần đóng và chỗ ngồi trong các điều "
      "kiện tĩnh đã nêu. Thực tế, việc chọn cơ cấu chấp hành cho một van dựa trên lực cần để "
      "thắng mất cân bằng tĩnh, ma sát thân và mất cân bằng động, có tính đến tải chỗ ngồi đầy đủ."),
     ("Seat Load", "The net contact force between the closure member and seat with stated static "
      "conditions. In practice, the selection of an actuator for a given control valve will be "
      "based on how much force is required to overcome static, stem, and dynamic unbalance with "
      "an allowance made for adequate seat load.")),
    (("Vòng chỗ ngồi (Seat Ring)", "Bộ phận của cụm thân van tạo bề mặt chỗ ngồi cho phần đóng "
      "và có thể tạo một phần lỗ tiết lưu."),
     ("Seat Ring", "A part of the valve body assembly that provides a seating surface for the "
      "closure member and can provide part of the flow control orifice.")),
    (("Bích rời (Separable Flange)", "Bích lắp vừa vào kết nối dòng của thân van, thường được giữ "
      "bằng vòng giữ."),
     ("Separable Flange", "A flange that fits over a valve body flow connection. It is generally "
      "held in place by means of a retaining ring.")),
    (("Vít chỉnh lò xo", "Chi tiết, thường có ren trên thân cơ cấu chấp hành hoặc ren vào ách, "
      "dùng để chỉnh độ nén lò xo."),
     ("Spring Adjuster", "A fitting, usually threaded on the actuator stem or into the yoke, to "
      "adjust the spring compression.")),
    (("Đế lò xo (Spring Seat)", "Tấm giữ lò xo đúng vị trí và tạo bề mặt phẳng cho vít chỉnh lò xo tiếp xúc."),
     ("Spring Seat", "A plate to hold the spring in position and to provide a flat surface for "
      "the spring adjuster to contact.")),
    (("Mất cân bằng tĩnh", "Lực ròng tác dụng lên thân van do áp suất chất lỏng quá trình tác động "
      "lên phần đóng và thân khi chất lỏng ở trạng thái nghỉ và trong các điều kiện áp suất đã nêu."),
     ("Static Unbalance", "The net force produced on the valve stem by the process fluid pressure "
      "acting on the closure member and stem with the fluid at rest and with stated pressure "
      "conditions.")),
    (("Đầu nối thân (Stem Connector)", "Thiết bị nối thân cơ cấu chấp hành với thân van."),
     ("Stem Connector", "The device that connects the actuator stem to the valve stem.")),
    (("Bộ trim", "Các chi tiết bên trong của van điều chỉnh dòng chất lỏng được điều khiển. Trong "
      "thân van cầu, trim thường gồm phần đóng, vòng chỗ ngồi, lồng, thân và chốt thân."),
     ("Trim", "The internal components of a valve that modulate the flow of the controlled "
      "fluid. In a globe valve body, trim would typically include closure member, seat ring, "
      "cage, stem, and stem pin.")),
    (("Trim chỗ kín mềm", "Trim van dùng vật liệu đàn hồi, nhựa hoặc vật liệu dễ biến dạng khác "
      "ở phần đóng hoặc vòng chỗ ngồi để đóng kín với lực cơ cấu chấp hành nhỏ."),
     ("Trim, Soft-Seated", "Valve trim with an elastomeric, plastic, or other readily deformable "
      "material used either in the closure component or seat ring to provide tight shutoff with "
      "minimal actuator forces.")),
    (("Thân van (Valve Body)", "Ranh giới áp suất chính của van, đồng thời tạo các đầu nối ống, "
      "đường dòng chảy và đỡ bề mặt chỗ ngồi cùng phần đóng. Các cấu trúc thường gặp gồm: thân "
      "một cổng với một nút; thân hai cổng với một nút; thân hai chiều với một vào một ra; thân "
      "ba chiều với ba kết nối (hai vào một ra để gộp dòng, hoặc một vào hai ra để tách dòng)."),
     ("Valve Body", "The main pressure boundary of the valve that also provides the pipe "
      "connecting ends, the fluid flow passageway, and supports the seating surfaces and the "
      "valve closure member. Among the most common valve body constructions are: single-ported "
      "valve bodies having one port and one valve plug; double-ported valve bodies having two "
      "ports and one valve plug; two-way valve bodies having two flow connections, one inlet "
      "and one outlet; three-way valve bodies having three flow connections, two of which can "
      "be inlets with one outlet (for converging or mixing flows), or one inlet and two outlets "
      "(for diverging or diverting flows).")),
    (("Cụm thân van (Valve Body Assembly)", "Cụm gồm thân van, cụm nắp, đáy van (nếu dùng) và các "
      "chi tiết trim. Trim gồm phần đóng mở, đóng hoặc làm tắc một phần một hay nhiều cổng."),
     ("Valve Body Assembly", "An assembly of a valve body, bonnet assembly, bottom flange (if "
      "used), and trim elements. The trim includes the closure member, which opens, closes, or "
      "partially obstructs one or more ports.")),
    (("Nút van (Valve Plug)", "Thuật ngữ thường dùng để chỉ phần đóng trong van thân trục trượt."),
     ("Valve Plug (Plug)", "A term frequently used to reference the valve closure member in a "
      "sliding-stem valve.")),
    (("Thân van điều khiển (Valve Stem)", "Trong van chuyển động tuyến tính, chi tiết nối thân cơ "
      "cấu chấp hành với phần đóng."),
     ("Valve Stem", "In a linear motion valve, the part that connects the actuator stem with "
      "the closure member.")),
    (("Ách (Yoke)", "Cấu trúc nối cứng bộ phận động lực của cơ cấu chấp hành với van."),
     ("Yoke", "The structure that rigidly connects the actuator power unit to the valve.")),
]

# ===========================================================================
# 1.3 Rotary control valve terminology (source pp. 23-25)
# ===========================================================================
_D13_A = [
    (("Cần cơ cấu chấp hành", "Cánh tay gắn vào trục van quay để đổi chuyển động tuyến tính của "
      "thân cơ cấu chấp hành thành mô-men xoắn nhằm định vị đĩa hoặc bi. Thường được nối chặt "
      "với trục qua then then chốt hoặc cơ cấu tương tự để giảm hở và mất chuyển động."),
     ("Actuator Lever", "Arm attached to rotary valve shaft to convert linear actuator stem "
      "motion to rotary force (torque) to position a disk or ball of a rotary valve. The lever "
      "normally is positively connected to the rotary by close tolerance splines or other means "
      "to minimize play and lost motion.")),
    (("Bi đầy (Ball, Full)", "Phần đóng của van quay dùng một hình cầu hoàn chỉnh có lỗ dòng "
      "chảy hình trụ xuyên qua; lỗ này bằng hoặc khớp với đường kính ống."),
     ("Ball, Full", "The flow closure member of rotary control valves using a complete sphere "
      "with a cylindrical flow passage through it. The flow passage equals or matches the pipe "
      "diameter.")),
    (("Bi phân đoạn (Ball, Segmented)", "Phần đóng của van quay dùng một hình cầu một phần có "
      "lỗ dòng chảy xuyên qua."),
     ("Ball, Segmented", "The flow closure member of rotary control valves using a partial "
      "sphere with a flow passage through it.")),
    (("Bi rãnh V (Ball, V-Notch)", "Kiểu van bi phân đoạn phổ biến nhất. Bi rãnh V có bề mặt "
      "hình cầu một phần được đánh bóng hoặc mạ, quay ăn khớp với vòng chỗ kín trong suốt dải "
      "hành trình. Rãnh chữ V cho dải điều chỉnh rộng và tạo đặc tính dòng phần trăm bằng nhau."),
     ("Ball, V-Notch", "The most common type of segmented ball control valve. The V-notch ball "
      "includes a polished or plated partial sphere surface that rotates against the seal ring "
      "throughout the travel range. The V-shaped notch in the ball permits wide rangeability "
      "and produces an equal-percentage flow characteristic.")),
    (("Đĩa thường (Disk, Conventional)", "Phần đóng đối xứng dùng trong các dạng van bướm quay "
      "phổ biến nhất. Mô-men xoắn động cao thường giới hạn đĩa thường ở góc quay tối đa 60 độ "
      "trong dịch vụ tiết lưu."),
     ("Disk, Conventional", "The symmetrical flow closure member used in the most common "
      "varieties of butterfly rotary valves. Highly-dynamic torques normally limit conventional "
      "disks to 60 degrees maximum rotation in throttling service.")),
    (("Đĩa thiết kế động", "Đĩa van bướm được tạo hình để giảm mô-men xoắn động ở những góc quay "
      "lớn, nhờ đó phù hợp cho dịch vụ tiết lưu với góc quay đĩa tới 90 độ."),
     ("Disk, Dynamically-Designed", "A butterfly valve disk contoured to reduce dynamic torque "
      "at large increments of rotation, thereby making it suitable for throttling service with "
      "up to 90 degrees of disk rotation.")),
    (("Đĩa lệch tâm (Disk, Eccentric)", "Tên thường gọi của kiểu van mà vị trí lệch tâm của điểm "
      "nối trục/đĩa làm đĩa đi theo đường hơi lệch (cam) khi mở. Điều này cho phép đĩa thoát khỏi "
      "chỗ kín ngay khi mở, giảm ma sát và mòn."),
     ("Disk, Eccentric", "Common name for valve design in which the off-centered positioning of "
      "the valve shaft/disk connections causes the disk to take a slightly eccentric (cammed) "
      "path on opening. This allows the disk to be swung out of contact with the seal as soon "
      "as it is opened, reducing friction and wear.")),
    (("Van không bích (Flangeless Valve)", "Kiểu van thường gặp ở van điều khiển quay. Van không "
      "bích được kẹp giữa hai bích chuẩn ANSI/ASME bằng bulông xuyên dài (đôi khi gọi là thân "
      "van kiểu wafer)."),
     ("Flangeless Valve", "Valve style common to rotary control valves. Flangeless valves are "
      "held between ANSI/ASME-class flanges by long through-bolts (sometimes also called "
      "wafer-style valve bodies).")),
    (("Nút lệch tâm (Plug, Eccentric)", "Kiểu van điều khiển quay có nút quay lệch tâm, vào và ra "
      "khỏi chỗ ngồi theo đường cam, giúp giảm ma sát và mòn. Rất phù hợp cho ứng dụng xói mòn."),
     ("Plug, Eccentric", "Style of rotary control valve with an eccentrically-rotating plug which "
      "cams into and out of the seat, which reduces friction and wear. This style of valve is "
      "well suited for erosive applications.")),
    (("Dòng ngược (Reverse Flow)", "Dòng chảy từ phía trục/đầu trục đi qua mặt sau của đĩa, bi "
      "hoặc nút. Một số van quay xử lý tốt dòng hai chiều; kiểu khác có thể cần chỉnh lại liên "
      "kết cơ cấu chấp hành."),
     ("Reverse Flow", "Flow from the shaft/hub side over the back of the disk, ball, or plug. "
      "Some rotary control valves are capable of handling flow equally well in either "
      "direction. Other rotary designs might require modification of actuator linkage to handle "
      "reverse flow.")),
    (("Ổ bi đầu cần (Rod End Bearing)", "Liên kết thường dùng giữa thân cơ cấu chấp hành và cần "
      "chấp hành để đổi lực đẩy tuyến tính thành mô-men xoắn với mất chuyển động tối thiểu. Dùng "
      "cơ cấu chấp hành reciprocating tiêu chuẩn trên thân van quay thường cần liên kết với "
      "hai ổ bi đầu cần; chọn cơ cấu chấp hành thiết kế riêng cho van quay chỉ cần một ổ, giảm "
      "mất chuyển động."),
     ("Rod End Bearing", "The connection often used between actuator stem and actuator lever to "
      "facilitate conversion of linear actuator thrust to rotary force (torque) with minimum of "
      "lost motion. Use of a standard reciprocating actuator on a rotary valve body commonly "
      "requires linkage with two rod end bearings. However, selection of an actuator specially "
      "designed for rotary valve service requires only one such bearing and thereby reduces "
      "lost motion.")),
    (("Van điều khiển quay", "Kiểu van trong đó phần đóng (bi đầy, bi một phần, đĩa hoặc nút) được "
      "quay trong dòng để điều chỉnh năng lực của van."),
     ("Rotary Control Valve", "A valve style in which the flow closure member (full ball, partial "
      "ball, disk or plug) is rotated in the flow stream to control the capacity of the valve.")),
    (("Vòng chỗ kín (Seal Ring)", "Bộ phận của cụm van quay tương ứng với vòng chỗ ngồi của van "
      "cầu. Vị trí của đĩa hoặc bi so với vòng chỗ kín quyết định diện tích dòng và năng lực "
      "của van tại mỗi bước hành trình quay."),
     ("Seal Ring", "The portion of a rotary control valve assembly corresponding to the seat "
      "ring of a globe valve. Positioning of the disk or ball relative to the seal ring "
      "determines the flow area and capacity of the unit at that particular increment of "
      "rotational travel.")),
    (("Trục (Shaft)", "Bộ phận của cụm van quay tương ứng với thân van của van cầu. Quay trục định "
      "vị đĩa hoặc bi trong dòng và điều khiển dòng qua van."),
     ("Shaft", "The portion of a rotary control valve assembly corresponding to the valve stem "
      "of a globe valve. Rotation of the shaft positions the disk or ball in the flow stream and "
      "controls flow through the valve.")),
    (("Chỗ kín trượt (Sliding Seal)", "Chỗ kín xi lanh dưới trong cơ cấu chấp hành piston khí nén "
      "thiết kế cho van quay. Chỗ kín này cho phép thân cơ cấu chấp hành chuyển động cả theo "
      "phương dọc lẫn ngang mà không rò áp nạp xi lanh dưới, nhờ đó chỉ cần một ổ bi đầu cần."),
     ("Sliding Seal", "The lower cylinder seal in a pneumatic piston-style actuator designed for "
      "rotary valve service. This seal permits the actuator stem to move both vertically and "
      "laterally without leakage of lower cylinder loading pressure, allowing for a single rod "
      "end bearing.")),
    (("Dòng chuẩn (Standard Flow)", "Với van quay có vòng chỗ kín hoặc vòng dòng riêng, là chiều "
      "dòng mà chất lỏng vào thân van qua đường ống kề vòng chỗ kín và ra từ phía đối diện vòng "
      "chỗ kín. Đôi khi gọi là dòng xuôi hoặc dòng vào mặt phần đóng."),
     ("Standard Flow", "For those rotary control valves having a separate seal ring or flow "
      "ring, the flow direction in which fluid enters the valve body through the pipeline "
      "adjacent to the seal ring and exits from the side opposite the seal ring. Sometimes "
      "called forward flow or flow into the face of the closure member.")),
    (("Lắp chặn (Trunnion Mounting)", "Kiểu lắp đĩa hoặc bi trên trục van hoặc trục chốt với hai "
      "ổ bi đối nhau đường kính."),
     ("Trunnion Mounting", "A style of mounting the disk or ball on the valve shaft or stub shaft "
      "with two diametrically opposed bearings.")),
]

# ===========================================================================
# 1.4 Control valve functions and characteristics terminology (pp. 25-27)
# ===========================================================================
_D14 = [
    (("Cài đặt băng (Bench Set)", "Quy trình hiệu chuẩn lò xo cơ cấu chấp hành để nó dùng một "
      "dải áp suất nhằm đi hết hành trình định mức của van."),
     ("Bench Set", "The calibration procedure of an actuator spring so that it can use a pressure "
      "range to fully stroke a valve to its rated travel.")),
    (("Năng lực (Capacity)", "Lượng dòng qua van (Cv hoặc Kv) trong các điều kiện đã nêu."),
     ("Capacity", "Amount of flow through a valve (Cv or Kv), under stated conditions.")),
    (("Dòng khe hở (Clearance Flow)", "Dòng xảy ra dưới mức dòng nhỏ nhất có thể điều khiển khi "
      "phần đóng chưa ngồi kín hoàn toàn."),
     ("Clearance Flow", "Flow that occurs below the minimum controllable flow with the closure "
      "member not fully seated.")),
    (("Dải áp suất màng", "Hiệu giữa giá trị cao và thấp của dải áp suất nạp màng."),
     ("Diaphragm Pressure Span", "Difference between the high and low values of the diaphragm "
      "loading pressure range.")),
    (("Cơ cấu chấp hành tác động kép", "Cơ cấu chấp hành được cấp khí nén, thủy lực hoặc điện "
      "ở cả hai chiều."),
     ("Double-Acting Actuator", "An actuator in which pneumatic, hydraulic, or electric power "
      "is supplied in either direction.")),
    (("Mất cân bằng động", "Lực ròng tác dụng lên nút van ở một vị trí mở đã nêu do áp suất chất "
      "lỏng quá trình tác động lên nó."),
     ("Dynamic Unbalance", "The net force produced on the valve plug in any stated open position "
      "by the fluid process pressure acting upon it.")),
    (("Diện tích hiệu dụng", "Trong cơ cấu chấp hành, phần diện tích của màng hoặc piston tạo ra "
      "lực thân. Diện tích hiệu dụng của màng có thể thay đổi khi đi hành trình, thường lớn nhất "
      "lúc bắt đầu và nhỏ nhất lúc kết thúc; màng ép khuôn thay đổi ít hơn màng phẳng nên được "
      "khuyên dùng."),
     ("Effective Area", "In an actuator, the part of the diaphragm or piston area that produces "
      "a stem force. The effective area of a diaphragm might change as it is stroked, usually "
      "being a maximum at the start and a minimum at the end of the travel range. Molded "
      "diaphragms have less change in effective area than flat sheet diaphragms; thus, molded "
      "diaphragms are recommended.")),
    (("Đóng an toàn (Fail-Closed)", "Trạng thái phần đóng của van chuyển về vị trí đóng khi nguồn "
      "năng lượng chấp hành bị mất."),
     ("Fail-Closed", "A condition wherein the valve closure member moves to a closed position "
      "when the actuating energy source fails.")),
    (("Mở an toàn (Fail-Open)", "Trạng thái phần đóng của van chuyển về vị trí mở khi nguồn năng "
      "lượng chấp hành bị mất."),
     ("Fail-Open", "A condition wherein the valve closure member moves to an open position when "
      "the actuating energy source fails.")),
    (("An toàn khi mất nguồn (Fail-Safe)", "Đặc tính của van và cơ cấu chấp hành: khi mất nguồn "
      "năng lượng chấp hành, phần đóng sẽ đóng hoàn toàn, mở hoàn toàn hoặc giữ nguyên vị trí "
      "cuối — tùy vị trí nào được xác định là cần thiết để bảo vệ quá trình và thiết bị; có thể "
      "dùng cả điều khiển phụ nối với cơ cấu chấp hành."),
     ("Fail-Safe", "A characteristic of a valve and its actuator, which upon loss of actuating "
      "energy supply, will cause a valve closure member to be fully closed, fully open, or "
      "remain in the last position, whichever position is defined as necessary to protect the "
      "process and equipment. Action can involve the use of auxiliary controls connected to "
      "the actuator.")),
    (("Đặc tính dòng", "Quan hệ giữa dòng qua van và phần trăm hành trình định mức khi hành trình "
      "thay đổi từ 0 đến 100%. Thuật ngữ này luôn phải được ghi rõ là đặc tính dòng vốn có hoặc "
      "đặc tính dòng lắp đặt."),
     ("Flow Characteristic", "Relationship between flow through the valve and percent rated "
      "travel as the latter is varied from 0 to 100%. This term should always be designated as "
      "either inherent flow characteristic or installed flow characteristic.")),
    (("Hệ số dòng (Cv)", "Hằng số liên quan đến hình học của van, tại một hành trình đã nêu, dùng "
      "để xác định năng lực dòng. Đó là số gallon Mỹ mỗi phút nước ở 16 °C (60 °F) chảy qua van "
      "với độ giảm áp một pound trên inch vuông."),
     ("Flow Coefficient (Cv)", "A constant related to the geometry of a valve, for a given "
      "travel, that can be used to establish flow capacity. It is the number of U.S. gallons "
      "per minute of 16 °C (60 °F) water that will flow through a valve with a one pound per "
      "square inch pressure drop.")),
    (("Van phục hồi cao", "Thiết kế van tiêu hao tương đối ít năng lượng dòng nhờ đường dòng "
      "được tạo hình suôn và nhiễu loạn tối thiểu; vì thế áp suất phía sau chỗ thắt (vena "
      "contracta) phục hồi tới tỉ lệ cao so với giá trị đầu vào. Van dòng thẳng như van bi quay "
      "thường là van phục hồi cao."),
     ("High-Recovery Valve", "A valve design that dissipates relatively little flow stream "
      "energy due to streamlined internal contours and minimal flow turbulence. Therefore, "
      "pressure downstream of the valve vena contracta recovers to a high percentage of its "
      "inlet value. Straight-through flow valves, such as rotary ball valves, are typically "
      "high-recovery valves.")),
    (("Dải áp suất màng vốn có", "Giá trị áp suất cao và thấp áp lên màng để tạo hành trình nút "
      "van định mức khi áp suất trong thân van bằng áp suất khí quyển. Dải này thường gọi là dải "
      "cài đặt băng vì đó là dải van đi hết hành trình khi đặt trên bàn làm việc."),
     ("Inherent Diaphragm Pressure Range", "The high and low values of pressure applied to the "
      "diaphragm to produce rated valve plug travel with atmospheric pressure in the valve body. "
      "This range is often referred to as a bench set range because it will be the range over "
      "which the valve will stroke when it is set on the work bench.")),
    (("Đặc tính dòng vốn có", "Quan hệ giữa lưu lượng và hành trình phần đóng khi nó đi từ vị trí "
      "đóng đến hành trình định mức với độ giảm áp không đổi qua van."),
     ("Inherent Flow Characteristic", "The relationship between the flow rate and the closure "
      "member travel as it is moved from the closed position to rated travel with constant "
      "pressure drop across the valve.")),
    (("Dải áp suất màng lắp đặt", "Giá trị áp suất cao và thấp áp lên màng để tạo hành trình định "
      "mức trong các điều kiện đã nêu trong thân van. Do các lực tác động lên phần đóng, dải áp "
      "suất màng vốn có có thể khác dải áp suất màng lắp đặt."),
     ("Installed Diaphragm Pressure Range", "The high and low values of pressure applied to the "
      "diaphragm to produce rated travel with stated conditions in the valve body. It is because "
      "of the forces acting on the closure member that the inherent diaphragm pressure range "
      "can differ from the installed diaphragm pressure range.")),
    (("Đặc tính dòng lắp đặt", "Quan hệ giữa lưu lượng và hành trình phần đóng khi nó đi từ vị trí "
      "đóng đến hành trình định mức, với độ giảm áp qua van chịu ảnh hưởng của các điều kiện quá "
      "trình thay đổi."),
     ("Installed Flow Characteristic", "The relationship between the flow rate and the closure "
      "member travel as it is moved from the closed position to rated travel as the pressure "
      "drop across the valve is influenced by the varying process conditions.")),
    (("Van phục hồi thấp", "Thiết kế van tiêu hao đáng kể năng lượng dòng do nhiễu loạn tạo bởi "
      "đường dòng; áp suất sau chỗ thắt phục hồi tới tỉ lệ thấp hơn so với van có đường dòng suôn "
      "hơn. Dù thiết kế riêng lệch nhau, van cầu thông thường có khả năng phục hồi áp suất thấp."),
     ("Low-Recovery Valve", "A valve design that dissipates a considerable amount of flow stream "
      "energy due to turbulence created by the contours of the flow path. Consequently, pressure "
      "downstream of the valve vena contracta recovers to a lesser percentage of its inlet value "
      "than is the case with a valve having a more streamlined flow path. Although individual "
      "designs vary, conventional globe-style valves generally have low pressure recovery "
      "capability.")),
    (("Đặc tính dòng parabolic biến tính", "Đặc tính dòng vốn có cho đặc tính phần trăm bằng nhau "
      "ở hành trình phần đóng nhỏ và xấp xỉ đặc tính tuyến tính ở các đoạn hành trình trên."),
     ("Modified Parabolic Flow Characteristic", "An inherent flow characteristic that provides "
      "equal-percentage characteristic at low closure member travel and approximately a linear "
      "characteristic for upper portions of closure member travel.")),
    (("Van thường đóng / thường mở", "Xem Đóng an toàn / Mở an toàn."),
     ("Normally-Closed Valve / Normally-Open Valve", "See Fail-Closed / Fail-Open.")),
    (("Kết cấu ấn để đóng (PDTC)", "Kết cấu van kiểu cầu trong đó phần đóng nằm giữa cơ cấu chấp "
      "hành và vòng chỗ ngồi, sao cho thân cơ cấu chấp hành dịch ra đẩy phần đóng về phía vòng "
      "chỗ ngồi và cuối cùng đóng van. Cũng áp dụng cho van quay khi dịch ra đẩy bi hoặc đĩa về "
      "phía đóng. Còn gọi là tác động trực tiếp."),
     ("Push-Down-to-Close (PDTC) Construction", "A globe-style valve construction in which the "
      "closure member is located between the actuator and the seat ring, such that extension of "
      "the actuator stem moves the closure member toward the seat ring, finally closing the "
      "valve. The term can also be applied to rotary valve constructions where linear extension "
      "of the actuator stem moves the ball or disk toward the closed position. Also called "
      "direct-acting.")),
    (("Kết cấu ấn để mở (PDTO)", "Kết cấu van kiểu cầu trong đó vòng chỗ ngồi nằm giữa cơ cấu "
      "chấp hành và phần đóng, sao cho thân cơ cấu chấp hành dịch ra đẩy phần đóng rời vòng chỗ "
      "ngồi, mở van. Cũng áp dụng cho van quay. Còn gọi là tác động ngược."),
     ("Push-Down-to-Open (PDTO) Construction", "A globe-style valve construction in which the "
      "seat ring is located between the actuator and the closure member, so that extension of "
      "the actuator stem moves the closure member from the seat ring, opening the valve. The "
      "term can also be applied to rotary valve constructions where linear extension of the "
      "actuator stem moves the ball or disk toward the open position. Also called reverse-acting.")),
    (("Dải điều chỉnh (Rangeability)", "Tỉ lệ giữa hệ số dòng lớn nhất (Cv hoặc Kv) và nhỏ nhất "
      "mà trong đó độ lệch so với đặc tính dòng quy định không vượt quá giới hạn đã nêu. Van vẫn "
      "điều khiển tốt khi dòng tăng gấp 100 lần dòng nhỏ nhất có thể điều khiển thì có dải điều "
      "chỉnh 100:1. Cũng được biểu thị bằng tỉ lệ dòng lớn nhất/nhỏ nhất có thể điều khiển."),
     ("Rangeability", "The ratio of the largest flow coefficient (Cv or Kv) to the smallest flow "
      "coefficient (Cv or Kv) within which the deviation from the specified flow characteristic "
      "does not exceed the stated limits. A control valve that still does a good job of "
      "controlling when flow increases to 100 times the minimum controllable flow has a "
      "rangeability of 100 to 1. Rangeability can also be expressed as the ratio of the maximum "
      "to minimum controllable flow rates.")),
    (("Hệ số dòng định mức (Cv)", "Hệ số dòng (Cv) của van tại hành trình định mức."),
     ("Rated Flow Coefficient (Cv)", "The flow coefficient (Cv) of the valve at rated travel.")),
    (("Hành trình định mức", "Khoảng cách dịch chuyển của phần đóng từ vị trí đóng đến vị trí mở "
      "hoàn toàn định mức — là độ mở lớn nhất do nhà sản xuất khuyến nghị."),
     ("Rated Travel", "The distance of movement of the closure member from the closed position "
      "to the rated full-open position. The rated full-open position is the maximum opening "
      "recommended by the manufacturers.")),
    (("Hệ số dòng tương đối (Cv)", "Tỉ lệ giữa hệ số dòng (Cv) tại một hành trình đã nêu và hệ số "
      "dòng (Cv) tại hành trình định mức."),
     ("Relative Flow Coefficient (Cv)", "The ratio of the flow coefficient (Cv) at a stated "
      "travel to the flow coefficient (Cv) at rated travel.")),
    (("Rò rỉ chỗ ngồi (Seat Leakage)", "Lượng chất lỏng đi qua van khi van ở vị trí đóng hoàn "
      "toàn và chịu tải chỗ ngồi lớn nhất sẵn có, với chênh áp và nhiệt độ đã quy định."),
     ("Seat Leakage", "The quantity of fluid passing through a valve when the valve is in the "
      "fully closed position and maximum available seat load is applied with pressure "
      "differential and temperature as specified.")),
    (("Độ cứng lò xo (Ks)", "Lực thay đổi trên mỗi đơn vị thay đổi chiều dài của lò xo. Trong cơ "
      "cấu chấp hành màng, thường nêu bằng pound-force trên inch nén."),
     ("Spring Rate (Ks)", "The force change per unit changes in length of a spring. In diaphragm "
      "actuators, the spring rate is usually stated in pounds force per inch compression.")),
    (("Chỗ thắt (Vena Contracta)", "Đoạn của dòng mà tại đó vận tốc chất lỏng lớn nhất, áp suất "
      "tĩnh và diện tích mặt cắt nhỏ nhất. Trong van điều khiển, chỗ thắt thường xảy ra ngay phía "
      "sau điểm tiết lưu vật lý thực tế."),
     ("Vena Contracta", "The portion of a flow stream where fluid velocity is at its maximum and "
      "fluid static pressure and the cross-sectional area are at their minimum. In a control "
      "valve, the vena contracta normally occurs just downstream of the actual physical "
      "restriction.")),
]

# ===========================================================================
# 1.5 Process control terminology (source pp. 27-33)
# ===========================================================================
_D15_A = [
    (("Phụ tùng (Accessory)", "Thiết bị lắp thêm vào cụm van điều khiển để bổ sung các chức năng "
      "hoặc tạo ra tác động mong muốn, đặc biệt là tác động chấp hành (bộ định vị, bộ điều chỉnh "
      "áp suất cấp, van điện từ, công tắc hành trình…)."),
     ("Accessory", "A device mounted to a control valve assembly to complement various functions "
      "or produce desired actions, particularly actuation (positioners, supply pressure "
      "regulators, solenoids, limit switches, etc.).")),
    (("Cơ cấu chấp hành", "Thiết bị chạy bằng khí nén, thủy lực hoặc điện cung cấp lực và chuyển "
      "động để mở hoặc đóng van."),
     ("Actuator", "A pneumatic, hydraulic, or electrically powered device that supplies force "
      "and motion to open or close a valve.")),
    (("Cụm cơ cấu chấp hành", "Cơ cấu chấp hành bao gồm mọi phụ tùng liên quan để thành một cụm "
      "vận hành hoàn chỉnh."),
     ("Actuator Assembly", "An actuator, including all the pertinent accessories that make it a "
      "complete operating unit.")),
    (("ANSI", "Viết tắt của American National Standards Institute (Viện Tiêu chuẩn Quốc gia Hoa Kỳ)."),
     ("ANSI", "Abbreviation for American National Standards Institute.")),
    (("API", "Viết tắt của American Petroleum Institute (Viện Dầu khí Hoa Kỳ)."),
     ("API", "Abbreviation for American Petroleum Institute.")),
    (("ASME", "Viết tắt của American Society of Mechanical Engineers (Hội Kỹ sư Cơ khí Hoa Kỳ)."),
     ("ASME", "Abbreviation for American Society of Mechanical Engineers.")),
    (("ASTM", "Trước đây viết tắt của American Society for Testing and Materials; khi phạm vi "
      "trở nên quốc tế, đổi tên thành ASTM International. ASTM không còn là từ viết tắt."),
     ("ASTM", "Used to stand for American Society for Testing and Materials. As the scope of "
      "the organization became international, the name was changed to ASTM International. ASTM "
      "is no longer an abbreviation.")),
    (("Hệ điều khiển tự động", "Hệ điều khiển vận hành không cần sự can thiệp của con người."),
     ("Automatic Control System", "A control system that operates without human intervention.")),
    (("Hở (Backlash)", "Một dạng vùng chết do sự gián đoạn tạm thời giữa đầu vào và đầu ra của "
      "thiết bị khi đầu vào đổi chiều (độ lỏng của liên kết cơ khí)."),
     ("Backlash", "A form of deadband that results from a temporary discontinuity between the "
      "input and output of a device when the input of the device changes direction.")),
    (("Sơ đồ Bode", "Đồ thị logarit biên độ và góc pha theo tần số logarit của một hàm truyền; "
      "là cách biểu diễn phổ biến nhất của dữ liệu đáp ứng tần số."),
     ("Bode Diagram", "A plot of log amplitude ratio and phase angle values on a log frequency "
      "base for a transfer function. It is the most common form of graphically presenting "
      "frequency response data.")),
    (("Đường cong hiệu chuẩn", "Biểu diễn đồ thị của báo cáo hiệu chuẩn: đầu ra ổn định của thiết "
      "bị theo đầu vào ổn định, thường là phần trăm dải đầu ra so với phần trăm dải đầu vào."),
     ("Calibration Curve", "A graphical representation of the calibration report. Steady state "
      "output of a device plotted as a function of its steady state input. The curve is usually "
      "shown as percent output span versus percent input span.")),
    (("Chu trình hiệu chuẩn", "Áp dụng các giá trị đã biết của biến đo và ghi các giá trị đầu ra "
      "tương ứng trên toàn dải của thiết bị, theo chiều tăng và giảm; dùng để đo độ trễ (hysteresis)."),
     ("Calibration Cycle", "The application of known values of the measured variable and the "
      "recording of corresponding values of output readings, over the range of the instrument, "
      "in ascending and descending directions. It provides a measurement of hysteresis.")),
    (("Năng lực (van)", "Lượng dòng qua van (Cv) trong các điều kiện đã nêu."),
     ("Capacity (Valve)", "The amount of flow through a valve (Cv) under stated conditions.")),
    (("Vòng kín (Closed Loop)", "Sự liên kết các thành phần điều khiển quá trình sao cho thông tin "
      "về biến quá trình được liên tục phản hồi về điểm đặt của bộ điều khiển, tạo ra các hiệu "
      "chỉnh liên tục, tự động cho biến quá trình."),
     ("Closed Loop", "The interconnection of process control components such that information "
      "regarding the process variable is continuously fed back to a controller set point to "
      "provide continuous, automatic corrections to the process variable.")),
    (("Phần đóng", "Chi tiết trim của van (còn gọi là nút, đĩa, bi phân đoạn hoặc bi lỗ toàn "
      "phần) dùng để điều chỉnh lưu lượng trong van điều khiển."),
     ("Closure Member", "A valve trim element (also known as a plug, disk, segmented ball, or "
      "full-port ball) used to modulate the flow rate within a control valve.")),
    (("Bộ điều khiển", "Thiết bị hoạt động tự động theo một thuật toán xác lập để điều chỉnh biến "
      "được điều khiển. Đầu vào nhận thông tin về trạng thái của biến quá trình, sau đó đưa tín "
      "hiệu ra thích hợp tới phần tử điều khiển cuối cùng."),
     ("Controller", "A device that operates automatically, by use of some established algorithm, "
      "to regulate a controlled variable. The controller input receives information about the "
      "status of the process variable and then provides an appropriate output signal to the "
      "final control element.")),
    (("Vòng điều khiển", "Xem Vòng kín hoặc Vòng hở."),
     ("Control Loop", "See Closed Loop or Open Loop.")),
    (("Dải điều khiển", "Dải hành trình van mà trong đó van duy trì độ khuếch đại van lắp đặt "
      "giữa các giá trị chuẩn hóa 0,5 và 2,0."),
     ("Control Range", "The range of valve travel over which a control valve can maintain the "
      "installed valve gain between the normalized values of 0.5 and 2.0.")),
    (("Cụm van điều khiển", "Thiết bị điều chỉnh dòng chất lỏng bằng cách thay đổi kích thước "
      "đường dòng theo tín hiệu từ bộ điều khiển."),
     ("Control Valve Assembly", "A device used to modulate fluid flow by varying the size of the "
      "flow passage as directed by a signal from a controller.")),
]

_D15_B = [
    (("Vùng chết (Deadband)", "Hiện tượng chung cho thấy dải tín hiệu đầu vào có thể thay đổi khi "
      "đổi chiều mà không gây ra thay đổi observable ở đầu ra. Với van điều khiển, đầu ra bộ "
      "điều khiển (CO) là đầu vào và biến quá trình (PV) là đầu ra. Khi bàn về vùng chết, phải "
      "xác định rõ cả đầu vào và đầu ra và các phép thử phải tiến hành trong điều kiện đầy tải. "
      "Vùng chết thường thể hiện bằng phần trăm dải đầu vào."),
     ("Deadband", "A general phenomenon, that can apply to any device, where the range through "
      "which an input signal can be varied, upon reversal of direction, without initiating an "
      "observable change in output signal. For control valves, the controller output (CO) is the "
      "input to the valve assembly and the process variable (PV) is the output. Whenever "
      "discussing deadband, it is essential that both the input and output variables are "
      "identified, and that any quantifiable tests be conducted under fully-loaded conditions. "
      "Deadband is typically expressed as a percent of the input span.")),
    (("Thời gian chết (Dead Time)", "Khoảng thời gian (Td) không phát hiện thấy đáp ứng của hệ "
      "thống sau một bước đầu vào nhỏ (thường 0,25% - 5%), tính từ lúc bắt đầu bước đến đáp ứng "
      "đầu tiên có thể phát hiện. Áp dụng cho cụm van hoặc toàn quá trình."),
     ("Dead Time", "The time interval (Td) in which no response of the system is detected "
      "following a small (usually 0.25% - 5%) step input. This time is derived from the moment "
      "the step input is initiated to the first detectable response of the system. Dead time "
      "can apply to a valve assembly or to the entire process.")),
    (("Enthalpy (H)", "Đại lượng nhiệt động bằng tổng nội năng của vật và tích của thể tích với "
      "áp suất: H = U + pV. Còn gọi là nhiệt lượng chứa."),
     ("Enthalpy", "A thermodynamic quantity that is the sum of the internal energy of a body and "
      "the product of its volume multiplied by the pressure: H = U + pV. Also called the heat "
      "content.")),
    (("Entropy", "Thước đo lý thuyết về năng lượng không thể chuyển thành công cơ học trong một "
      "hệ nhiệt động."),
     ("Entropy", "The theoretical measure of energy that cannot be transformed into mechanical "
      "work in a thermodynamic system.")),
    (("Đặc tính phần trăm bằng nhau", "Đặc tính dòng vốn có mà với mỗi bước hành trình định mức "
      "bằng nhau sẽ cho các thay đổi phần trăm bằng nhau của hệ số dòng (Cv) tính từ Cv hiện có."),
     ("Equal-Percentage Characteristic", "An inherent flow characteristic that, for equal "
      "increments of rated travel, will ideally give equal-percentage changes of the flow "
      "coefficient (Cv) from the existing Cv.")),
    (("Tín hiệu phản hồi", "Tín hiệu trở về do phép đo biến được điều khiển trực tiếp tạo ra. Với "
      "van có bộ định vị, đó thường là chỉ thị cơ học vị trí thân phần đóng được phản hồi vào "
      "bộ định vị."),
     ("Feedback Signal", "The return signal that results from a measurement of the directly "
      "controlled variable. For a control valve with a positioner, the return signal is usually "
      "a mechanical indication of closure member stem position that is fed back into the "
      "positioner.")),
    (("FCI", "Viết tắt của Fluid Controls Institute — tổ chức cung cấp tiêu chuẩn và tài liệu "
      "giáo dục giúp người mua và người dùng hiểu và sử dụng thiết bị điều khiển và điều hòa "
      "chất lỏng."),
     ("FCI", "Abbreviation for Fluid Controls Institute. Provides standards and educational "
      "materials to assist purchasers and users in understanding and using fluid control and "
      "conditioning equipment.")),
    (("Phần tử điều khiển cuối cùng", "Thiết bị thực hiện chiến lược điều khiển do đầu ra của bộ "
      "điều khiển quyết định. Dù có thể có nhiều dạng (cửa gió, thiết bị đóng cắt…), dạng phổ "
      "biến nhất hiện nay là cụm van điều khiển, điều chỉnh dòng khí, hơi, nước, hợp chất hóa "
      "học… để bù nhiễu tải và giữ biến quá trình gần điểm đặt nhất có thể."),
     ("Final Control Element", "A device that implements the control strategy determined by the "
      "output of a controller. While this final control element can take many forms (dampers, "
      "on/off switching devices, etc.) the most common final control element in industry today "
      "is the control valve assembly. Control valves modulate flowing fluid (i.e. gas, steam, "
      "water, chemical compounds, etc.) to compensate for load disturbances and keep the "
      "regulated process variable as close to the desired set point as possible.")),
    (("Bậc nhất (First-Order)", "Thuật ngữ mô tả quan hệ động giữa đầu vào và đầu ra của thiết bị. "
      "Hệ hoặc thiết bị bậc nhất chỉ có một phần tử lưu trữ năng lượng và quan hệ quá độ giữa "
      "đầu vào và đầu ra có tính chất hàm mũ."),
     ("First-Order", "A term referring to the dynamic relationship between the input and output "
      "of a device. First-order systems, or devices, have only one energy storage device and the "
      "dynamic transient relationship between the input and output is characterized by an "
      "exponential behavior.")),
    (("Đặc tính đáp ứng tần số", "Quan hệ phụ thuộc tần số, cả về biên độ lẫn pha, giữa đầu vào "
      "hình sin ổn định và đầu ra hình sin cơ bản kết quả. Biên độ và độ lệch pha được quan sát "
      "như hàm của tần số thử để mô tả hành vi động của thiết bị điều khiển."),
     ("Frequency Response Characteristic", "The frequency-dependent relation, in both amplitude "
      "and phase, between steady-state sinusoidal inputs and the resulting fundamental "
      "sinusoidal outputs. Output amplitude and phase shift are observed as functions of the "
      "input test frequency and used to describe the dynamic behavior of the control device.")),
    (("Ma sát (Friction)", "Lực chống lại chuyển động tương đối giữa hai bề mặt tiếp xúc, phụ "
      "thuộc vào lực pháp tuyến và bản chất bề mặt. Gồm ma sát tĩnh (stick/slip, stiction) — lực "
      "phải thắng trước khi có chuyển động, một nguyên nhân chính gây vùng chết — và ma sát động "
      "(ma sát trượt) cần để duy trì chuyển động."),
     ("Friction", "A force that tends to oppose the relative motion between two surfaces that "
      "are in contact with each other. The associated force is a function of the normal force "
      "holding these two surfaces together and the characteristic nature of the two surfaces. "
      "Friction has two components: static friction and dynamic friction. Static friction (also "
      "known as stick/slip, or stiction) is the force that must be overcome before there is any "
      "relative motion between the two surfaces. Static friction is also one of the major "
      "causes of deadband in a valve assembly. Once relative movement has begun, dynamic friction "
      "(also known as running friction, or sliding friction) is the force that must be overcome "
      "to maintain the relative motion.")),
    (("Độ khuếch đại (Gain)", "Tỉ lệ giữa độ lớn của sự thay đổi đầu ra và độ lớn của sự thay đổi "
      "đầu vào gây ra nó. Gồm độ khuếch đại tĩnh (độ nhạy, ở trạng thái ổn định) và độ khuếch "
      "đại động (khi hệ đang chuyển động, phụ thuộc tần số hoặc tốc độ thay đổi đầu vào)."),
     ("Gain", "Term used to describe the ratio of the magnitude of an output change of a given "
      "system or device to the magnitude of an input change that caused the output change. Gain "
      "has two components: static gain and dynamic gain. Static gain (also known as sensitivity) "
      "is the gain relationship between the input and output in a steady-state condition. "
      "Dynamic gain is the gain relationship when the system is in a state of movement or flux "
      "and is a function of frequency or rate of change of the input.")),
    (("Độ cứng (Hardness)", "Khả năng chống biến dạng dẻo của kim loại, thường bằng cách ấn lõm; "
      "với nhựa và cao su là khả năng chống xuyên của đầu ấn vào bề mặt."),
     ("Hardness", "Resistance of metal to plastic deformation, usually by indentation. "
      "Resistance of plastics and rubber to penetration of an indentor point into its surface.")),
    (("Dao động (Hunting)", "Dao động không mong muốn, biên độ đáng kể, kéo dài sau khi kích "
      "thích bên ngoài biến mất; còn gọi là chu trình hoặc chu trình giới hạn, là dấu hiệu vận "
      "hành ở hoặc gần giới hạn ổn định. Ở van điều khiển, biểu hiện là dao động áp suất nạp "
      "tới cơ cấu chấp hành do mất ổn định ở chính van hoặc bộ định vị."),
     ("Hunting", "An undesirable oscillation of appreciable magnitude, prolonged after external "
      "stimuli disappear. Sometimes called cycling or limit cycle, hunting is evidence of "
      "operation at or near the stability limit. In control valve applications, hunting would "
      "appear as an oscillation in the loading pressure to the actuator caused by instability "
      "in the valve or the valve positioner.")),
    (("Độ trễ (Hysteresis)", "Hiệu lớn nhất của giá trị đầu ra với một giá trị đầu vào bất kỳ "
      "trong một chu trình hiệu chuẩn, không kể sai số do vùng chết; là sự chậm trễ của hiệu ứng "
      "khi lực tác động lên vật thay đổi (như do độ nhớt hoặc ma sát trong)."),
     ("Hysteresis", "The maximum difference in output value for any single input value during a "
      "calibration cycle, excluding errors due to deadband. A retardation of an effect when the "
      "forces acting upon a body are changed (as if from viscosity or internal friction).")),
]

_D15_C = [
    (("Đặc tính vốn có", "Quan hệ giữa hệ số dòng và hành trình phần đóng khi đi từ vị trí đóng "
      "đến hành trình định mức với độ giảm áp không đổi. Thường vẽ trên đồ thị với trục hoành "
      "là phần trăm hành trình và trục tung là phần trăm dòng (hoặc Cv). Các dạng điển hình: "
      "tuyến tính, phần trăm bằng nhau và mở nhanh."),
     ("Inherent Characteristic", "The relationship between the flow coefficient and the closure "
      "member travel as it is moved from the closed position to rated travel with constant "
      "pressure drop across the valve. Typically, these characteristics are plotted on a curve "
      "where the horizontal axis is labeled in percent travel and the vertical axis is labeled "
      "as percent flow (or Cv). Typical valve characteristics conducted in this manner are named "
      "linear, equal-percentage, and quick opening.")),
    (("Độ khuếch đại van vốn có", "Tỉ lệ độ lớn của thay đổi dòng qua van với thay đổi hành trình "
      "trong điều kiện giảm áp không đổi; là hàm vốn có của thiết kế van, bằng độ dốc của đường "
      "đặc tính vốn có tại mỗi điểm hành trình."),
     ("Inherent Valve Gain", "The magnitude ratio of the change in flow through the valve to the "
      "change in valve travel under conditions of constant pressure drop. Inherent valve gain "
      "is an inherent function of the valve design. It is equal to the slope of the inherent "
      "characteristic curve at any travel point and is a function of valve travel.")),
    (("Đặc tính lắp đặt", "Quan hệ giữa lưu lượng và hành trình phần đóng khi đi từ đóng đến "
      "hành trình định mức, với độ giảm áp qua van chịu ảnh hưởng của điều kiện quá trình thay đổi."),
     ("Installed Characteristic", "The relationship between the flow rate and the closure "
      "member travel as it is moved from the closed position to rated travel as the pressure "
      "drop across the valve is influenced by the varying process conditions.")),
    (("Độ khuếch đại van lắp đặt", "Tỉ lệ độ lớn của thay đổi dòng với thay đổi hành trình trong "
      "điều kiện quá trình thực tế, khi độ giảm áp thay đổi tự nhiên theo toàn hệ thống. Bằng độ "
      "dốc của đường đặc tính lắp đặt và là hàm của hành trình."),
     ("Installed Valve Gain", "The magnitude ratio of the change in flow through the valve to the "
      "change in valve travel under actual process conditions. Installed valve gain is equal to "
      "the slope of the installed characteristic curve, and is a function of valve travel.")),
    (("Áp suất thiết bị", "Áp suất đầu ra từ bộ điều khiển tự động dùng để vận hành van điều khiển."),
     ("Instrument Pressure", "The output pressure from an automatic controller that is used to "
      "operate a control valve.")),
    (("I/P", "Viết tắt của current-to-pressure (chuyển dòng sang áp), thường áp cho mô-đun bộ "
      "chuyển đổi tín hiệu."),
     ("I/P", "Shorthand for current-to-pressure (I-to-P). Typically applied to input transducer "
      "modules.")),
    (("ISA", "Viết tắt của International Society for Automation (Hội Tự động hóa Quốc tế)."),
     ("ISA", "Abbreviation for the International Society for Automation.")),
    (("Tính tuyến tính", "Mức độ mà đường cong giữa hai biến gần với đường thẳng; cũng có nghĩa "
      "là cùng một đường thẳng áp dụng cho cả chiều tăng và giảm. Vì vậy vùng chết được coi là "
      "một dạng phi tuyến."),
     ("Linearity", "The closeness to which a curve relating to two variables approximates a "
      "straight line. Linearity also means that the same straight line will apply for both "
      "upscale and downscale directions. Thus, deadband would typically be considered a "
      "non-linearity.")),
    (("Đặc tính tuyến tính", "Đặc tính dòng vốn có biểu diễn bằng đường thẳng trên đồ thị hệ số "
      "dòng (Cv) theo hành trình định mức; các bước hành trình bằng nhau cho các bước Cv bằng nhau."),
     ("Linear Characteristic", "An inherent flow characteristic that can be represented by a "
      "straight line on a rectangular plot of flow coefficient (Cv) versus rated travel. "
      "Therefore equal increments of travel provide equal increments of flow coefficient, Cv.")),
    (("Áp suất nạp", "Áp suất dùng để định vị cơ cấu chấp hành khí nén — là áp suất thực tác "
      "dụng lên màng hoặc piston và có thể là áp suất thiết bị khi không dùng bộ định vị."),
     ("Loading Pressure", "The pressure employed to position a pneumatic actuator. This is the "
      "pressure that actually works on the actuator diaphragm or piston and it can be the "
      "instrument pressure if a valve positioner is not used.")),
    (("Vòng (Loop)", "Xem Vòng kín hoặc Vòng hở."),
     ("Loop", "See Closed Loop or Open Loop.")),
    (("Độ khuếch đại vòng", "Độ khuếch đại tổng hợp của mọi thành phần trong vòng khi xét nối "
      "tiếp vòng tròn; đôi khi gọi là độ khuếch đại vòng hở. Phải nêu rõ là tĩnh hay động tại "
      "một tần số nhất định."),
     ("Loop Gain", "The combined gain of all the components in the loop when viewed in series "
      "around the loop. Sometimes referred to as open loop gain. It must be clearly specified "
      "whether referring to the static loop gain or the dynamic loop gain at some frequency.")),
    (("Điều khiển tay", "Xem Vòng hở."),
     ("Manual Control", "See Open Loop.")),
    (("NACE", "Trước đây viết tắt của National Association of Corrosion Engineers; đổi thành "
      "NACE International khi mang tính quốc tế. NACE không còn là từ viết tắt."),
     ("NACE", "Used to stand for National Association of Corrosion Engineers. As the scope of "
      "the organization became international, the name was changed to NACE International. NACE "
      "is no longer an abbreviation.")),
    (("Vòng hở (Open Loop)", "Tình trạng liên kết các thành phần điều khiển bị ngắt, thông tin "
      "về biến quá trình không còn được phản hồi về điểm đặt và không còn hiệu chỉnh biến. "
      "Thường thực hiện bằng cách đưa bộ điều khiển về chế độ tay."),
     ("Open Loop", "The condition where the interconnection of process control components is "
      "interrupted such that information from the process variable is no longer fed back to the "
      "controller set point so that corrections to the process variable are no longer provided. "
      "This is typically accomplished by placing the controller in the manual operating position.")),
    (("Môi trường vận hành", "Chất lỏng, thường là không khí hoặc khí, dùng để cấp năng lượng "
      "cho bộ định vị hoặc bộ điều khiển tự động."),
     ("Operating Medium", "This is the fluid, generally air or gas, used to supply the power for "
      "operation of valve positioner or automatic controller.")),
    (("Giới hạn làm việc", "Dải điều kiện vận hành mà thiết bị có thể chịu đựng mà không suy "
      "giảm vĩnh viễn các đặc tính vận hành."),
     ("Operative Limits", "The range of operating conditions to which a device can be subjected "
      "without permanent impairment of operating characteristics.")),
    (("OSHA", "Viết tắt của Occupational Safety and Health Administration (Cơ quan Quản lý An "
      "toàn và Sức khỏe Nghề nghiệp, Hoa Kỳ)."),
     ("OSHA", "Abbreviation for Occupational Safety and Health Administration (U.S.).")),
    (("Gioăng đệm (Packing)", "Bộ phận của cụm van dùng để làm kín chống rò rỉ quanh trục hoặc "
      "thân van."),
     ("Packing", "A part of the valve assembly used to seal against leakage around the valve "
      "shaft or stem.")),
    (("Bộ định vị (Positioner)", "Bộ điều khiển vị trí (cơ cấu servo) nối cơ học với bộ phận "
      "chuyển động của phần tử điều khiển cuối cùng hoặc cơ cấu chấp hành, tự động chỉnh đầu "
      "ra tới cơ cấu chấp hành để giữ vị trí mong muốn tỉ lệ với tín hiệu đầu vào."),
     ("Positioner", "A position controller (servomechanism) that is mechanically connected to a "
      "moving part of a final control element or its actuator and that automatically adjusts "
      "its output to the actuator to maintain a desired position in proportion to the input "
      "signal.")),
    (("Quá trình (Process)", "Tất cả các thành phần kết hợp trong vòng điều khiển, trừ bộ điều "
      "khiển. Đôi khi chỉ chất lỏng chảy qua vòng."),
     ("Process", "All the combined elements in the control loop, except the controller. Sometimes "
      "refers to the fluid that passes through the loop.")),
    (("Độ khuếch đại quá trình", "Tỉ lệ giữa sự thay đổi của biến quá trình được điều khiển với "
      "sự thay đổi tương ứng của đầu ra bộ điều khiển."),
     ("Process Gain", "The ratio of the change in the controlled process variable to a "
      "corresponding change in the output of the controller.")),
    (("Độ biến thiên quá trình", "Thước đo thống kê chính xác mức độ quá trình được điều khiển "
      "chặt quanh điểm đặt, thường tính bằng phần trăm (2s/m), với m là điểm đặt hoặc giá trị "
      "trung bình và s là độ lệch chuẩn."),
     ("Process Variability", "A precise statistical measure of how tightly the process is being "
      "controlled about the set point. Process variability is defined in percent as typically "
      "(2s/m), where m is the set point or mean value of the measured process variable and s is "
      "the standard deviation of the process variable.")),
    (("Đặc tính mở nhanh", "Đặc tính dòng vốn có trong đó hệ số dòng cực đại đạt được với hành "
      "trình phần đóng rất nhỏ."),
     ("Quick-Opening (QO) Characteristic", "An inherent flow characteristic in which a maximum "
      "flow coefficient is achieved with minimal closure member travel.")),
    (("Dải (Range)", "Vùng giữa các giới hạn mà trong đó một đại lượng được đo, nhận hoặc truyền, "
      "biểu thị bằng giá trị dưới và trên. Ví dụ: 3 đến 15 psi; -40 đến 100 °C (-40 đến 212 °F)."),
     ("Range", "The region between the limits within which a quantity is measured, received, or "
      "transmitted, expressed by stating the lower and upper range values. For example: 3 to "
      "15 psi; -40 to 100 °C (-40 to 212 °F).")),
    (("Bộ khuếch đại (Relay)", "Thiết bị hoạt động như bộ khuếch đại công suất: nhận tín hiệu "
      "điện, khí nén hoặc cơ khí và tạo đầu ra có lưu lượng lớn khí hoặc chất lỏng thủy lực tới "
      "cơ cấu chấp hành. Có thể là bộ phận trong bộ định vị hoặc phụ tùng riêng."),
     ("Relay", "A device that acts as a power amplifier. It takes an electrical, pneumatic, or "
      "mechanical input signal and produces an output of a large volume flow of air or hydraulic "
      "fluid to the actuator. The relay can be an internal component of the positioner or a "
      "separate valve accessory.")),
    (("Độ lặp lại (Repeatability)", "Mức độ đồng nhất giữa nhiều phép đo liên tiếp đầu ra với "
      "cùng một giá trị đầu vào, trong cùng điều kiện, tiếp cận từ cùng một hướng và quét toàn "
      "dải; thường nêu dưới dạng độ không lặp lại, tính bằng phần trăm dải, không gồm độ trễ."),
     ("Repeatability", "The closeness of agreement among a number of consecutive measurements "
      "of the output for the same value of the input under the same operating conditions, "
      "approaching from the same direction, for full-range traverses. It is usually measured "
      "as a non-repeatability and expressed as repeatability in percent of span. It does not "
      "include hysteresis.")),
    (("Độ phân giải (Resolution)", "Thay đổi nhỏ nhất có thể của đầu vào để tạo ra thay đổi "
      "có thể phát hiện ở đầu ra khi đầu vào không đổi chiều; thường bằng phần trăm dải đầu vào."),
     ("Resolution", "The minimum possible change in input required to produce a detectable "
      "change in the output when no reversal of the input takes place. Resolution is typically "
      "expressed as a percent of the input span.")),
    (("Thời gian đáp ứng", "Thường đo bằng thông số gồm cả thời gian chết và hằng số thời gian. "
      "Khi áp cho van, gồm toàn bộ cụm van."),
     ("Response Time", "Usually measured by a parameter that includes both dead time and time "
      "constant. When applied to the valve, it includes the entire valve assembly.")),
    (("Bậc hai (Second-Order)", "Thuật ngữ mô tả quan hệ động giữa đầu vào và đầu ra của thiết bị "
      "có hai phần tử lưu trữ năng lượng, có thể trao đổi động năng và thế năng qua lại, tạo "
      "khả năng dao động và vượt quá (overshoot)."),
     ("Second-Order", "A term that refers to the dynamic relationship between the input and "
      "output of a device. A second-order system or device is one that has two energy storage "
      "devices that can transfer kinetic and potential energy back and forth between themselves, "
      "thus introducing the possibility of oscillatory behavior and overshoot.")),
    (("Độ nhạy (Sensitivity)", "Tỉ lệ giữa thay đổi độ lớn đầu ra và thay đổi đầu vào gây ra nó "
      "sau khi đã đạt trạng thái ổn định."),
     ("Sensitivity", "The ratio of the change in output magnitude to the change of the input "
      "that causes it after the steady-state has been reached.")),
    (("Cảm biến (Sensor)", "Thiết bị cảm nhận giá trị của biến quá trình và đưa tín hiệu đầu ra "
      "tương ứng tới bộ phát. Có thể là bộ phận của bộ phát hoặc chi tiết riêng."),
     ("Sensor", "A device that senses the value of the process variable and provides a "
      "corresponding output signal to a transmitter. The sensor can be an integral part of the "
      "transmitter, or it may be a separate component.")),
    (("Điểm đặt (Set Point)", "Giá trị tham chiếu biểu thị giá trị mong muốn của biến quá trình "
      "được điều khiển."),
     ("Set Point", "A reference value representing the desired value of the process variable "
      "being controlled.")),
    (("Xoắn trục (Shaft Wind-Up)", "Hiện tượng một đầu trục van quay trong khi đầu kia không "
      "quay. Thường xảy ra ở van quay có cơ cấu chấp hành nối với phần đóng qua trục tương đối "
      "dài: ma sát chỗ kín giữ một đầu, đầu kia xoay làm trục bị vặn cho đến khi đủ lực thắng ma sát."),
     ("Shaft Wind-Up", "A phenomenon where one end of a valve shaft turns and the other does not. "
      "This typically occurs in rotary-style valves where the actuator is connected to the valve "
      "closure member by a relatively long shaft. While seal friction in the valve holds one end "
      "of the shaft in place, rotation of the shaft at the actuator end is absorbed by twisting "
      "of the shaft until the actuator input transmits enough force to overcome the friction.")),
    (("Tín hiệu (Signal)", "Đại lượng vật lý, trong đó một hoặc nhiều thông số mang thông tin về "
      "một đại lượng khác mà tín hiệu đại diện."),
     ("Signal", "A physical variable, one or more parameters of which carry information about "
      "another variable the signal represents.")),
    (("T tuần tự biên độ tín hiệu", "Hành động tạo ra hai hay nhiều tín hiệu, hoặc kích hoạt hai "
      "hay nhiều phần tử điều khiển cuối cùng, bằng một tín hiệu đầu vào, mỗi phần tử đáp ứng "
      "liên tiếp (có hoặc không chồng lấn) theo độ lớn của tín hiệu đó."),
     ("Signal Amplitude Sequencing (Split Ranging)", "Action in which two or more signals are "
      "generated or two or more final controlling elements are actuated by an input signal, "
      "each one responding consecutively, with or without overlap, to the magnitude of that "
      "input signal.")),
    (("Định cỡ van (Sizing)", "Quy trình có hệ thống nhằm đảm bảo năng lực van đúng cho từng "
      "điều kiện trong tập điều kiện quá trình đã quy định."),
     ("Sizing (Valve)", "A systematic procedure designed to ensure the correct valve capacity "
      "for each condition of a set of specified process conditions.")),
    (("Dải giá trị (Span)", "Hiệu đại số giữa giá trị giới hạn trên và dưới. Ví dụ: nếu dải là "
      "0 đến 66 °C (150 °F) thì span = 66 °C; nếu dải là 3 đến 15 psig thì span = 12 psig."),
     ("Span", "The algebraic difference between the upper and lower range values. For example: "
      "If range = 0 to 66 °C (150 °F), then span = 66 °C (150 °F); if range = 3 to 15 psig, "
      "then span = 12 psig.")),
    (("Stiction (Ma sát tĩnh)", "Lực cần để đưa một vật đang tiếp xúc với vật khác bắt đầu "
      "chuyển động. Xem thêm Ma sát."),
     ("Stiction (Static Friction)", "The force required to cause one body in contact with another "
      "to begin to move. Also see Friction.")),
    (("Áp suất cấp (Supply Pressure)", "Áp suất tại cổng cấp của thiết bị. Giá trị thường gặp "
      "của van điều khiển là 20 psig cho dải 3 đến 15 psig và 35 psig cho dải 6 đến 30 psig."),
     ("Supply Pressure", "The pressure at the supply port of a device. Common values of control "
      "valve supply pressure are 20 psig for a 3 to 15 psig range and 35 psig for a 6 to 30 psig "
      "range.")),
    (("T63", "Thước đo đáp ứng của thiết bị, bằng cách áp bước đầu vào nhỏ (thường 1-5%); tính "
      "từ lúc bắt đầu bước đến lúc đầu ra đạt 63% giá trị ổn định cuối. Bằng tổng thời gian chết "
      "(Td) và hằng số thời gian (t)."),
     ("T63", "A measure of device response. It is measured by applying a small (usually 1-5%) "
      "step input to the system. T63 is measured from the time the step input is initiated to the "
      "time when the system output reaches 63% of the final steady-state value. It is the "
      "combined total of the system dead time (Td) and the system time constant (t).")),
    (("Hằng số thời gian (Time Constant)", "Thông số thời gian thường áp cho phần tử bậc nhất; "
      "khoảng thời gian từ đáp ứng đầu tiên có thể phát hiện sau bước nhỏ (0,25%-5%) đến lúc đầu "
      "ra đạt 63% giá trị cuối. Với quá trình vòng hở ký hiệu là T (Tau), với hệ vòng kín là λ (Lambda)."),
     ("Time Constant", "A time parameter that normally applies to a first-order element. It is "
      "the time interval measured from the first detectable response of the system to a small "
      "(usually 0.25% - 5%) step input until the system output reaches 63% of its final "
      "steady-state value. When applied to an open-loop process, the time constant is usually "
      "designated as T (Tau). When applied to a closed-loop system, the time constant is usually "
      "designated as λ (Lambda).")),
    (("Bộ phát (Transmitter)", "Thiết bị cảm nhận giá trị biến quá trình và truyền tín hiệu đầu ra "
      "tương ứng tới bộ điều khiển để so với điểm đặt."),
     ("Transmitter", "A device that senses the value of the process variable and transmits a "
      "corresponding output signal to the controller for comparison with the set point.")),
    (("Hành trình (Travel)", "Chuyển động của phần đóng từ vị trí đóng đến vị trí trung gian hoặc "
      "mở hoàn toàn định mức."),
     ("Travel", "The movement of the closure member from the closed position to an intermediate "
      "or rated full-open position.")),
    (("Chỉ thị hành trình", "Kim và thang dùng để hiển thị bên ngoài vị trí của phần đóng, thường "
      "tính bằng phần trăm hành trình hoặc độ quay."),
     ("Travel Indicator", "A pointer and scale used to externally show the position of the "
      "closure member typically with units of opening percent of travel or degrees of rotation.")),
    (("Trim", "Các thành phần bên trong của van điều chỉnh dòng chất lỏng được điều khiển."),
     ("Trim", "The internal components of a valve that modulate the flow of the controlled "
      "fluid.")),
    (("Van (Valve)", "Xem Cụm van điều khiển."),
     ("Valve", "See Control Valve Assembly.")),
    (("Bộ tăng lượng (Volume Booster)", "Relay độc lập thường được gọi là bộ tăng lượng hoặc "
      "bộ boost vì nó tăng (khuếch đại) thể tích không khí cấp tới cơ cấu chấp hành. Xem Bộ khuếch đại."),
     ("Volume Booster", "A stand-alone relay is often referred to as a volume booster or simply "
      "booster because it boosts, or amplifies, the volume of air supplied to the actuator. See Relay.")),
    (("Sai số zero (Zero Error)", "Sai số của thiết bị vận hành trong điều kiện sử dụng đã quy "
      "định khi đầu vào ở giá trị giới hạn dưới của dải; thường thể hiện bằng phần trăm dải lý tưởng."),
     ("Zero Error", "Error of a device operating under specified conditions of use when the input "
      "is at the lower range value. It is usually expressed as percent of ideal span.")),
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 1.</b> sliding-stem — thân trục trượt · rotary — quay · "
                "closure member — phần đóng · trim — bộ phận bên trong (nút, vòng chỗ ngồi, "
                "lồng, thân) · cage — lồng · seat ring — vòng chỗ ngồi · bonnet — nắp van · "
                "packing — gioăng đệm · actuator — cơ cấu chấp hành · diaphragm — màng · "
                "loading pressure — áp suất nạp · bench set — cài đặt băng · inherent / installed "
                "characteristic — đặc tính vốn có / lắp đặt · Cv — hệ số dòng · rangeability — "
                "dải điều chỉnh · vena contracta — chỗ thắt · deadband — vùng chết · "
                "stiction — ma sát tĩnh · hysteresis — độ trễ · fail-safe — an toàn khi mất nguồn · "
                "positioner — bộ định vị · set point — điểm đặt.")
    return ("<b>Key terms.</b> sliding-stem · rotary · closure member · trim · cage · seat ring · "
            "bonnet · packing · actuator · diaphragm · loading pressure · bench set · inherent / "
            "installed characteristic · Cv · rangeability · vena contracta · deadband · stiction "
            "· hysteresis · fail-safe · positioner · set point.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def D(pairs):
        b.append(_defs(pairs, lang))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ------------------------------------------------------------ lead
    b.append(lead(
        "Chương này đưa ra định nghĩa và thuật ngữ dùng cho van điều khiển và hệ thống điều "
        "khiển quá trình, theo tiêu chuẩn ANSI/ISA-75.05.01 và ISA S75.05."
        if vi else
        "This chapter presents the definitions and terminology used for control valves and "
        "process control systems, following ANSI/ISA-75.05.01 and ISA S75.05."))

    # ------------------------------------------------------------ 1.1
    H("1.1 Van điều khiển là gì?",
      "1.1 What is a Control Valve?")
    P("Các nhà máy chế biến hiện đại sử dụng mạng lưới vòng điều khiển rộng lớn để tạo ra "
      "sản phẩm cuối cùng đưa ra thị trường. Các vòng này được thiết kế nhằm giữ một biến quá "
      "trình (PV) — chẳng hạn áp suất, lưu lượng, mức, nhiệt độ… — trong một dải vận hành yêu "
      "cầu để đảm bảo chất lượng sản phẩm. Mỗi vòng vừa nhận vừa tự sinh ra các nhiễu loạn "
      "ảnh hưởng bất lợi đến biến quá trình; tương tác từ các vòng khác trong mạng lưới cũng "
      "tạo nhiễu loạn. Xem Hình 1.1.",
      "Modern processing plants utilize a vast network of control loops to produce an end "
      "product for market. These control loops are designed to keep a process variable "
      "(i.e. pressure, flow, level, temperature, etc.) within a required operating range to "
      "ensure a quality end product is produced. Each of these loops receives and internally "
      "creates disturbances that detrimentally affect the process variable (PV). Interaction "
      "from other loops in the network also provide disturbances that influence the process "
      "variable. See Figure 1.1.")
    FIG(1, F.fig_f01())
    P("Để giảm ảnh hưởng của các nhiễu loạn tải, cảm biến và bộ phát thu thông tin về biến quá "
      "trình (PV) và mối quan hệ của nó với điểm đặt mong muốn. Bộ điều khiển xử lý thông tin "
      "này và quyết định phải làm gì để đưa PV về đúng giá trị sau khi có nhiễu loạn. Sau khi "
      "mọi phép đo, so sánh và tính toán hoàn tất, một phần tử điều khiển cuối cùng phải thực "
      "hiện chiến lược do bộ điều khiển chọn. Phần tử điều khiển cuối cùng phổ biến nhất trong "
      "công nghiệp điều khiển quá trình là van điều khiển: nó điều chỉnh một chất lỏng đang chảy "
      "— khí, hơi, nước hoặc hợp chất hóa học — để bù nhiễu loạn tải và giữ biến được điều "
      "chỉnh càng gần điểm đặt càng tốt.",
      "To reduce the effect of these load disturbances, sensors and transmitters collect "
      "information about the process variable (PV) and its relationship to some desired set "
      "point. A controller processes this information and decides what must be done to get the "
      "process variable back to where it should be after a load disturbance occurs. When all "
      "the measuring, comparing, and calculating are done, some type of final control element "
      "must implement the strategy selected by the controller. The most common final control "
      "element in the process control industries is the control valve. The control valve "
      "manipulates a flowing fluid, such as gas, steam, water, or chemical compounds to "
      "compensate for the load disturbance and keep the regulated process variable as close as "
      "possible to the desired set point.")
    P("Van điều khiển là bộ phận then chốt của vòng điều khiển. Nhiều người nói đến van điều "
      "khiển thực chất đang nói đến cụm van điều khiển. Cụm này thường gồm thân van, các chi "
      "tiết trim bên trong, cơ cấu chấp hành cung cấp động lực vận hành van và nhiều phụ tùng "
      "bổ sung như bộ chuyển đổi, bộ điều chỉnh áp suất cấp, bộ thao tác tay, bộ giảm chấn "
      "(snubber) hoặc công tắc hành trình.",
      "The control valve is a critical part of the control loop. Many people who talk about "
      "control valves are really referring to a control valve assembly. The control valve "
      "assembly typically consists of the valve body, the internal trim parts, an actuator to "
      "provide the motive power to operate the valve, and a variety of additional valve "
      "accessories, which can include transducers, supply pressure regulators, manual "
      "operators, snubbers, or limit switches.")
    P("Có hai kiểu thiết kế van điều khiển chính, tùy theo chuyển động của phần đóng: thân trục "
      "trượt (sliding-stem) và quay (rotary). Van thân trục trượt (Hình 1.2 và 1.3) dùng chuyển "
      "động tuyến tính để đưa phần đóng vào và ra khỏi bề mặt chỗ ngồi. Van quay (Hình 1.13 và "
      "1.17) dùng chuyển động quay để xoay phần đóng vào và ra khỏi bề mặt chỗ ngồi.",
      "There are two main types of control valve designs, depending on the action of the "
      "closure member: sliding-stem or rotary. Sliding-stem valves, as seen in Figure 1.2 and "
      "1.3, use linear motion to move a closure member into and out of a seating surface. "
      "Rotary valves, as seen in Figure 1.13 and 1.17, use rotational motion to turn a closure "
      "member into and out of a seating surface.")

    # ------------------------------------------------------------ 1.2
    H("1.2 Thuật ngữ van điều khiển thân trục trượt",
      "1.2 Sliding-Stem Control Valve Terminology")
    P("Các thuật ngữ sau áp dụng cho đặc tính vật lý và vận hành của van điều khiển thân trục "
      "trượt tiêu chuẩn với cơ cấu chấp hành màng hoặc piston. Một số thuật ngữ, đặc biệt là "
      "những thuật ngữ liên quan đến cơ cấu chấp hành, cũng phù hợp cho van quay. Nhiều định "
      "nghĩa được đưa ra theo ANSI/ISA-75.05.01, Control Valve Terminology, nhưng cũng có thêm "
      "các thuật ngữ phổ biến khác; lời giải thích bổ sung được đưa vào với một số thuật ngữ "
      "phức tạp hơn.",
      "The following terminology applies to the physical and operating characteristics of "
      "standard sliding-stem control valves with diaphragm or piston actuators. Some of the "
      "terms, particularly those pertaining to actuators, are also appropriate for rotary "
      "control valves. Many of the definitions presented are in accordance with ANSI/ISA-75.05.01, "
      "Control Valve Terminology, although other popular terms are also included. Additional "
      "explanation is provided for some of the more complex terms.")
    FIG(2, F.fig_f02())
    FIG(3, F.fig_f03())
    D(_D12_A)
    FIG(4, F.fig_f04())
    P("Van góc (Hình 1.4) là kiểu van có cổng vào và cổng ra vuông góc với nhau; van nắp kín "
      "bằng ống mềm (Hình 1.5) và cụm nắp van (Hình 1.6) cho thấy các phương thức làm kín quanh "
      "thân phần đóng.",
      "The angle valve (Figure 1.4) has inlet and outlet ports perpendicular to each other; the "
      "bellows seal bonnet (Figure 1.5) and the bonnet assembly (Figure 1.6) show the means of "
      "sealing around the closure member stem.")
    FIG(5, F.fig_f05())
    FIG(6, F.fig_f06())
    D(_D12_B)
    FIG(7, F.fig_f07())
    FIG(8, F.fig_f08())
    FIG(9, F.fig_f09())
    FIG(10, F.fig_f10())
    FIG(11, F.fig_f11())
    FIG(12, F.fig_f12())
    D(_D12_C)

    # ------------------------------------------------------------ 1.3
    H("1.3 Thuật ngữ van điều khiển quay",
      "1.3 Rotary Control Valve Terminology")
    P("Các thuật ngữ sau áp dụng cho đặc tính vật lý và vận hành của van điều khiển quay với cơ "
      "cấu chấp hành màng hoặc piston. Phần đóng trong thiết kế quay (bi, đĩa, nút lệch tâm…) "
      "thực hiện chức năng tương đương nút van trong van thân trục trượt: khi quay, chúng thay "
      "đổi kích thước và hình dạng của dòng bằng cách mở nhiều hay ít diện tích làm kín cho "
      "chất lỏng chảy qua. Nhiều định nghĩa theo ISA S75.05; các thuật ngữ liên quan đến cơ cấu "
      "chấp hành cũng phù hợp cho van quay.",
      "The following terminology applies to the physical and operating characteristics of rotary "
      "control valves with diaphragm or piston actuators. The closure members (i.e. balls, disks, "
      "eccentric plugs, etc.) in rotary designs perform a function comparable to the valve plug "
      "in a sliding-stem control valve. That is, as they rotate they vary the size and shape of "
      "the flow stream by opening more or less of the seal area to the flowing fluid. Many of the "
      "definitions presented are in accordance with ISA S75.05, Control Valve Terminology, "
      "although other popular terms are also included. Terms pertaining to actuators are also "
      "appropriate for rotary control valves.")
    FIG(13, F.fig_f13())
    D(_D13_A)
    FIG(14, F.fig_f14())
    FIG(15, F.fig_f15())
    FIG(16, F.fig_f16())
    FIG(17, F.fig_f17())

    # ------------------------------------------------------------ 1.4
    H("1.4 Thuật ngữ chức năng và đặc tính van điều khiển",
      "1.4 Control Valve Functions and Characteristics Terminology")
    D(_D14)

    # ------------------------------------------------------------ 1.5
    H("1.5 Thuật ngữ điều khiển quá trình",
      "1.5 Process Control Terminology")
    P("Các thuật ngữ và định nghĩa sau, chưa được định nghĩa ở các mục trên, thường được người "
      "làm việc với van điều khiển, thiết bị đo và phụ tùng gặp phải. Một số thuật ngữ, đánh dấu "
      "bằng dấu hoa thị (*), lấy từ tiêu chuẩn ISA 51.1, Process Instrumentation Terminology; "
      "các thuật ngữ phổ biến khác trong ngành van điều khiển cũng được đưa vào.",
      "The following terms and definitions not previously defined are frequently encountered by "
      "people associated with control valves, instrumentation, and accessories. Some of the "
      "terms, indicated with an asterisk (*), are derived from the ISA standard, Process "
      "Instrumentation Terminology, ISA 51.1. Other popular terminology used throughout the "
      "control valve industry is also included.")
    D(_D15_A)
    FIG(18, F.fig_f18())
    D(_D15_B)
    FIG(19, F.fig_f19())
    D(_D15_C)

    # ------------------------------------------------------------ about
    H3 = "Về nguồn tài liệu" if vi else "About the source"
    b.append(h3(H3, "About the source" if vi else "Về nguồn tài liệu"))
    P("Chương 1 chiếm tr. 16–33 của bản in (18 trang) trong Emerson, Control Valve Handbook, "
      "ấn bản 6 (2020). Đây là chương thuật ngữ: năm mục lần lượt định nghĩa các thuật ngữ về "
      "van thân trục trượt, van quay, chức năng và đặc tính van, và điều khiển quá trình. "
      "Nguyên bản có mười chín hình vẽ đánh số 1.1–1.19; tất cả được vẽ lại dạng vector trong "
      "cvh6fig.py, giữ nguyên cấu trúc và nhãn cùng các số gọi chi tiết.",
      "Chapter 1 occupies printed pp. 16-33 (18 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It is a terminology chapter: five sections define terms for sliding-stem "
      "valves, rotary valves, valve functions and characteristics, and process control. The "
      "source contains nineteen numbered figures, 1.1-1.19; all are redrawn as vectors in "
      "cvh6fig.py, keeping their topology, labels and numbered callouts.")
    P("Đặc điểm đáng chú ý của nguyên bản: Hình 1.2 và 1.3 là ảnh chụp van kèm số gọi chi tiết "
      "(được cần thay bằng mặt cắt vector); Hình 1.7 là ba ảnh nhỏ về cửa sổ lồng; Hình 1.18 và "
      "1.19 là các đồ thị đường nét; cuối mỗi mục có một ký hiệu ô vuông đặc biệt để báo kết "
      "thúc mục. Bản dịch gộp các định nghĩa thành danh sách cho dễ đọc nhưng giữ nguyên nội "
      "dung và thứ tự.",
      "Notable source quirks: Figures 1.2 and 1.3 are photographs with numbered callouts "
      "(here rendered as vector cross-sections); Figure 1.7 shows three small photos of cage "
      "windows; Figures 1.18 and 1.19 are line charts; and each section ends with a special "
      "solid-square glyph. The translation groups the definitions into lists for readability "
      "while keeping their content and order.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 "
      "Emerson Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 "
      "Emerson Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
