# -*- coding: utf-8 -*-
"""Book 6, Unit 1 — Introduction (EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (Gulf Professional
Publishing / Elsevier, 2004), pp. 1–5 of the book (PDF pp. 15–19).  One
editorial vector schematic (valve families grouped by duty) is drawn in
`vshfig.py`.
"""

from vsh_common import (fig, h2, h3, note, p, table, ul)
import vshfig as F

PAGES_SRC = 5           # source book pp. 1-5
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Introduction"
TITLE_VI = "Giới thiệu"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 1.</b> closure member — phần đóng (cấu kiện "
                "đóng mở) · stop/start flow — dừng/khởi động dòng chảy · throttle — "
                "khống chế lưu lượng · divert — phân luồng · backflow — dòng ngược · "
                "check valve — van một chiều · pressure relief valve — van an toàn "
                "áp suất · rupture disc — đĩa nứt vỡ · reclosing — tái đóng (đóng "
                "lại sau xả) · simmer — rò rỉ nhẹ ngay dưới áp suất cài đặt · "
                "chatter — dao động đóng/mở nhanh · deflagration — cháy lan · "
                "vent panel — tấm xả áp.")
    return ("<b>Key terms.</b> closure member · stop/start flow · throttle · "
            "divert · backflow · check valve · pressure relief valve · rupture "
            "disc · reclosing · simmer · chatter · deflagration · vent panel · "
            "piping specifying engineer.")


def _t_duties(lang):
    hdr = (["Nhiệm vụ", "Nhóm thiết bị", "Ví dụ kiểu loại"] if lang == "vi"
           else ["Duty", "Device group", "Typical examples"])
    rows = [
        ("Dừng / khởi động dòng chảy", "Van tay", "globe, gate, plug, ball, butterfly, diaphragm"),
        ("Khống chế lưu lượng (throttle)", "Van tay", "globe, butterfly, pinch, diaphragm"),
        ("Phân luồng dòng chảy", "Van tay nhiều đường", "3-way globe, multiport plug / ball"),
        ("Ngăn dòng ngược", "Van một chiều", "lift, swing, tilting-disc, diaphragm"),
        ("Giải áp (tái đóng được)", "Van an toàn áp suất", "direct-loaded, pilot-operated"),
        ("Giải áp (một lần, không tái đóng)", "Đĩa nứt vỡ", "forward-domed, reverse-buckling"),
    ]
    if lang == "en":
        rows = [
            ("Stopping and starting flow", "Manual valves",
             "globe, gate, plug, ball, butterfly, diaphragm"),
            ("Controlling flow rate (throttling)", "Manual valves",
             "globe, butterfly, pinch, diaphragm"),
            ("Diverting flow", "Multiport manual valves",
             "3-way globe, multiport plug / ball"),
            ("Preventing backflow", "Check valves",
             "lift, swing, tilting-disc, diaphragm"),
            ("Relieving pressure (reclosing)", "Pressure relief valves",
             "direct-loaded, pilot-operated"),
            ("Relieving pressure (non-reclosing)", "Rupture discs",
             "forward-domed, reverse-buckling"),
        ]
    cap = ("Nhiệm vụ của van trong hệ thống dòng chảy/áp suất — tóm lược từ chương 1 "
           "(tr. 1–2)." if lang == "vi" else
           "Valve duties in a fluid flow or pressure system — condensed from "
           "chapter 1 (pp. 1–2).")
    return table(hdr, rows, caption=cap, cls="tbl wide")


def _t_groups(lang):
    hdr = (["Nhóm van tay", "Chuyển động phần đóng", "Kiểu tiêu biểu"]
           if lang == "vi" else
           ["Manual valve group", "Closure member movement", "Typical types"])
    rows = [
        ("Stopper (chặn nút)", "Chuy động thẳng, ép lên chỗ kín",
         "globe, needle"),
        ("Vertical slide (trượt dọc)", "Trượt dọc qua lỗ dòng",
         "gate (parallel, wedge)"),
        ("Rotary (quay)", "Quay 90° hoặc ít hơn",
         "ball, plug, butterfly"),
        ("Flexible body (thân biến dạng)", "Ép biến dạng thân van/màng",
         "diaphragm, pinch"),
    ] if lang == "vi" else [
        ("Stopper type", "Linear motion onto the seat", "globe, needle"),
        ("Vertical slide", "Vertical slide across the flow port", "gate"),
        ("Rotary type", "Quarter-turn or less", "ball, plug, butterfly"),
        ("Flexible body", "Body / membrane flexure", "diaphragm, pinch"),
    ]
    cap = ("Bốn nhóm van tay phân theo chuyển động của phần đóng lên chỗ kín "
           "(tr. 2)." if lang == "vi" else
           "The four manual valve groups by the way the closure member moves "
           "onto the seat (p. 2).")
    return table(hdr, rows, caption=cap, cls="tbl")


# ---------------------------------------------------------------------------
def body_vi():
    b = []
    b.append(p("Mục đích của cuốn sách là trợ giúp <b>kỹ sư quy cách đường ống</b> "
               "(piping specifying engineer) lựa chọn van cho một ứng dụng cụ thể "
               "thỏa mãn các thông số thiết kế của dịch vụ quá trình. Lựa chọn van "
               "dựa trên: chức năng, độ phù hợp vật liệu, giới hạn áp suất/nhiệt độ "
               "thiết kế, tuổi thọ nhà máy, kiểu kết nối đầu, phương thức vận hành, "
               "khối lượng, khả năng cung ứng, bảo trì, và chi phí. Tác giả cố ý "
               "đặt <b>chi phí ở cuối</b> danh sách vì một lý do: nếu van không đạt "
               "các tiêu chí thiết kế thì dù được cho miễn phí nó vẫn <i>đắt</i> — "
               "kể cả chi phí thay thế khi nó hỏng. Cũng như cuộc sống, lựa chọn van "
               "là một chuỗi các đánh đổi."))
    b.append(fig(1, F.fig_vsh_intro()))

    b.append(h2("Van là gì và làm việc gì",
                "What valves are and what they do"))
    b.append(p("Van là cấu kiện trong hệ thống dòng chảy hoặc áp suất dùng để "
               "<b>khống chế dòng chảy hoặc áp suất</b> của chất lỏng. Nhiệm vụ này "
               "có thể gồm: dừng và khởi động dòng chảy, khống chế lưu lượng, phân "
               "luồng dòng, ngăn dòng ngược, khống chế áp suất, hoặc giải áp. Các "
               "nhiệm vụ được thực hiện bằng cách điều chỉnh vị trí của <b>phần "
               "đóng</b> (closure member) trong van — bằng tay hoặc bằng tự động. "
               "Vận hành tay còn bao gồm cả điều khiển qua một cơ cấu truyền động "
               "được điều khiển bằng tay."))
    b.append(_t_duties("vi"))
    b.append(p("Trong cuốn sách này: các van được vận hành bằng tay để dừng/khởi "
               "động dòng, khống chế lưu lượng và phân luồng gọi là <b>van tay</b>; "
               "các van ngăn dòng ngược và giải áp gọi tương ứng là <b>van một "
               "chiều</b> và <b>van an toàn áp suất</b>. Đĩa nứt vỡ là thiết bị giải "
               "áp <b>không tái đóng</b>, đảm nhiệm vai trò tương tự van an toàn "
               "áp suất."))

    b.append(h2("Cơ sở kỹ thuật (chương 2)", "Fundamentals (chapter 2)"))
    b.append(p("Hiệu năng làm kín và đặc tính dòng chảy là hai khía cạnh quan trọng "
               "trong lựa chọn van; hiểu về chúng rất hữu ích và thường là bắt buộc "
               "để chọn đúng van. Chương 2 bàn về <b>cơ sở của chỗ kín van</b> và "
               "<b>dòng chảy qua van</b>. Phần chỗ kín bắt đầu bằng định nghĩa độ "
               "kín chất lỏng, rồi mô tả cơ chế làm kín và thiết kế chỗ kín seat, "
               "chỗ kín gioăng đệm, và chỗ kín trục van. Phần dòng chảy bao gồm tổn "
               "thất áp suất, xâm thực (cavitation), waterhammer, và giảm tiếng ồn "
               "của van."))

    b.append(h2("Van tay", "Manual valves"))
    b.append(p("Van tay được chia thành <b>bốn nhóm</b> theo cách phần đóng chuyển "
               "động lên chỗ kín; mỗi nhóm gồm một số kiểu van riêng biệt, và mỗi "
               "kiểu lại được chế tạo với nhiều biến thể. Cách phần đóng chuyển "
               "động lên chỗ kín tạo ra cho nhóm hoặc kiểu van một <b>đặc tính "
               "khống chế dòng</b> tiêu biểu; đặc tính này được dùng để lập bảng "
               "chọn van sơ bộ. Lựa chọn cuối cùng được thực hiện từ mô tả của các "
               "kiểu van và biến thể của chúng ngay sau bảng đó."))
    b.append(_t_groups("vi"))

    b.append(h2("Van một chiều", "Check valves"))
    b.append(p("Nhiều kiểu van một chiều cũng được chia thành bốn nhóm theo cách "
               "phần đóng chuyển động lên chỗ kín: <i>lift</i>, <i>swing</i> (một "
               "và hai tấm), <i>tilting disc</i>, và <i>diaphragm</i>. Nhiệm vụ cơ "
               "bản là ngăn dòng ngược. Nhưng van còn phải <b>đóng đủ nhanh</b> để "
               "tránh hình thành vận tốc dòng ngược đáng kể — vì khi đóng đột ngột, "
               "dòng ngược ấy có thể tạo áp suất surge cao khó chấp nhận và/hoặc "
               "làm phần đóng đập mạnh vào chỗ kín. Ngoài ra, phần đóng phải "
               "<b>ổn định</b> ở vị trí mở. Chương 4 mô tả thiết kế và đặc tính "
               "vận hành của các van này, cùng các tiêu chí lựa chọn."))

    b.append(h2("Van an toàn áp suất", "Pressure relief valves"))
    b.append(p("Van an toàn áp suất chia thành hai nhóm lớn: <b>tác động trực "
               "tiếp</b> (direct-acting) — được kích hoạt trực tiếp bởi áp suất "
               "chất lỏng của hệ thống — và <b>điều khiển bằng pilot</b> "
               "(pilot-operated) — pilot điều khiển đóng/mở van chính theo áp suất "
               "hệ thống."))
    b.append(ul([
        "Van tác động trực tiếp có thể được trang bị <b>cơ cấu chấp hành phụ</b> "
        "hỗ trợ lift khi mở và/hoặc bổ sung lực đóng khi tái ngồi. Hỗ trợ lift "
        "nhằm chống <i>chatter</i> (dao động đóng/mở nhanh); lực đóng bổ sung "
        "nhằm giảm <i>simmer</i> (rò rỉ nhẹ ngay dưới áp suất cài đặt). Cơ cấu "
        "phụ dùng nguồn năng lượng ngoài; nếu nguồn ngoài mất, van vận hành như "
        "van tác động trực tiếp.",
        "Van điều khiển bằng pilot có thể dùng pilot <b>tác động trực tiếp</b> — "
        "điều khiển van chính bằng cơ cấu nội bộ — hoặc pilot <b>tác động gián "
        "tiếp</b> — điều khiển van chính bằng chất lỏng xả ra từ pilot.",
        "Kiểu thứ ba là van an toàn <b>được cấp nguồn</b> (powered), pilot vận "
        "hành bằng nguồn năng lượng ngoài; kiểu này chỉ áp dụng cho các dịch vụ "
        "mà quy phạm bắt buộc.",
    ]))

    b.append(h2("Đĩa nứt vỡ", "Rupture discs"))
    b.append(p("Đĩa nứt vỡ là thiết bị giải áp <b>không tái đóng</b>, dùng một mình "
               "hoặc kết hợp với van an toàn áp suất. Các kiểu chính: kiểu <b>vòm "
               "xuôi</b> (forward domed) — vỡ do kéo — và kiểu <b>đảo buckling</b> "
               "(reverse buckling) — vỡ do nén. Kiểu đảo buckling có thể chế tạo "
               "với dung sai vỡ chặt hơn; mặt hạn chế, không phải đĩa đảo buckling "
               "nào cũng phù hợp để giải áp chất lỏng không nén được."))
    b.append(p("Trong khi việc áp dụng van an toàn bị giới hạn ở các biến động áp "
               "suất <b>không bạo lực</b> (nonviolent excursions), đĩa nứt vỡ còn "
               "dùng được cho các biến động áp suất bạo lực do <b>cháy lan</b> "
               "(deflagration) của khí dễ cháy và bụi. Đĩa nứt vỡ dùng xả áp cháy "
               "lan cho bể chứa áp suất khí quyển hoặc nhà xưởng được gọi là "
               "<b>tấm xả áp</b> (vent panels)."))

    b.append(h2("Đơn vị đo và quy ước định danh",
                "Units of measurement and size/class identification"))
    b.append(p("Số liệu được cho theo cả hệ <b>SI</b> và <b>imperial</b>. Các "
               "phương trình giải theo đơn vị thông thường không liên hợp "
               "(incoherent) được trình bày riêng cho hệ SI và hệ imperial như "
               "thói quen của các nhà sản xuất Mỹ; các phương trình ở đơn vị liên "
               "hợp (coherent) dùng được cho cả hai hệ."))
    b.append(p("Định danh kích cỡ và cấp áp van theo khuyến nghị của "
               "<b>MSS Standard Practice SP-86</b>: kích cỡ danh nghĩa và cấp áp "
               "được viết <i>không kèm đơn vị</i> — ví dụ NPS 2, DN 50, Class 150, "
               "PN 20. NPS 2 là nominal pipe size 2 in.; DN 50 là diameter nominal "
               "50 mm; Class 150 là class 150 lb; PN 20 là pressure nominal "
               "20 bar."))

    b.append(h2("Tiêu chuẩn và các chương bổ sung",
                "Standards and additional chapters"))
    b.append(p("Phụ lục C liệt kê các tiêu chuẩn Mỹ, Anh và ISO quan trọng về van, "
               "nhóm theo kiểu/nhóm van. Ấn bản thứ năm có thêm ba chương chưa từng "
               "xuất hiện trong các ấn bản trước: <b>chương 8 — Cơ cấu chấp hành "
               "(actuator)</b>, <b>chương 9 — Van bi chặn kép và xả</b> (double "
               "block and bleed), <b>chương 10 — Thiết bị khóa cơ khí cho van</b>; "
               "cộng với bộ thuật ngữ toàn diện ở Phụ lục E."))

    b.append(h3("Sách không bàn về van điều khiển", "Not a control valve book"))
    b.append(p("Cuốn sách <b>không</b> đề cập van điều khiển (control valve). Với "
               "lĩnh vực này, nguyên bản dẫn hai xuất bản ISA: (1) H. D. Baumann, "
               "<i>Control Valve Primer, A User's Guide</i> (ấn bản 3, 1998) — có "
               "vật liệu mới về định cỡ van, positioner smart (số), kiến trúc "
               "field-based, công nghệ hệ thống mạng, và đánh giá hiệu năng vòng "
               "điều khiển; (2) Guy Borden (biên tập), <i>Control Valves, Practical "
               "Guides for Measuring and Control</i> (1998) — thuộc loạt Practical "
               "Guide của ISA, chương cuối bàn cả regulator và so sánh hiệu năng "
               "với van điều khiển."))
    b.append(note("Ý chính: lựa chọn van bắt đầu từ <b>nhiệm vụ</b> (dừng/khởi động, "
                  "khống chế, phân luồng, chặn dòng ngược, giải áp) và từ <b>cách "
                  "phần đóng chuyển động lên chỗ kín</b> — chính chuyển động ấy tạo "
                  "ra đặc tính dòng chảy và cơ chế làm kín của từng họ van. Chi phí "
                  "xét sau cùng: van không đạt tiêu chí thiết kế thì miễn phí vẫn "
                  "đắt. Cấu trúc sách đi đúng trật tự đó: cơ sở làm kín và dòng "
                  "chảy → từng họ van tay → van một chiều → van an toàn → đĩa nứt "
                  "vỡ → định cỡ → actuator → khóa cơ khí."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội "
               "dung gốc © 2004 Elsevier Inc. (Gulf Professional Publishing).</i>"))
    return "".join(b)


# ---------------------------------------------------------------------------
def body_en():
    b = []
    b.append(p("The purpose of this book is to assist the <b>piping specifying "
               "engineer</b> in the selection of valves for a specific application "
               "that meet the design parameters of the process service. Valve "
               "selection is based on function, material suitability, design "
               "pressure/temperature extremities, plant life, end connections, "
               "operation, weight, availability, maintenance, and cost. The author "
               "deliberately placed <b>cost at the end</b> for a reason: if the "
               "valve does not meet the design criteria, then even if it is free, "
               "it is still too expensive — because of the costs to replace it "
               "when it fails. Just like life, valve selection is a series of "
               "compromises."))
    b.append(fig(1, F.fig_vsh_intro()))

    b.append(h2("What valves are and what they do",
                "Van là gì và làm việc gì"))
    b.append(p("Valves are the components in a fluid flow or pressure system that "
               "regulate either the <b>flow or the pressure</b> of the fluid. This "
               "duty may involve stopping and starting flow, controlling flow "
               "rate, diverting flow, preventing backflow, controlling pressure, "
               "or relieving pressure. These duties are performed by adjusting the "
               "position of the <b>closure member</b> in the valve — either "
               "manually or automatically. Manual operation also includes the "
               "operation of the valve by means of a manually controlled power "
               "operator."))
    b.append(_t_duties("en"))
    b.append(p("In this book, valves that are manually operated for stopping and "
               "starting flow, controlling flow rate and diverting flow are "
               "referred to as <b>manual valves</b>, while valves for the "
               "prevention of backflow and the relief of pressure are referred to "
               "as <b>check valves</b> and <b>pressure relief valves</b>, "
               "respectively. Rupture discs are non-reclosing pressure-relieving "
               "devices which fulfil a duty similar to pressure relief valves."))

    b.append(h2("Fundamentals (chapter 2)", "Cơ sở kỹ thuật (chương 2)"))
    b.append(p("Sealing performance and flow characteristics are important aspects "
               "in valve selection; an understanding of these aspects is helpful "
               "and often essential in the selection of the correct valve. Chapter "
               "2 deals with the <b>fundamentals of valve seals</b> and <b>flow "
               "through valves</b>. The discussion on valve seals begins with the "
               "definition of fluid tightness, followed by the sealing mechanism "
               "and the design of seat seals, gasketed seals and stem seals. The "
               "subject of flow through valves covers pressure loss, cavitation, "
               "waterhammer and the attenuation of valve noise."))

    b.append(h2("Manual valves", "Van tay"))
    b.append(p("Manual valves are divided into <b>four groups</b> according to the "
               "way the closure member moves onto the seat. Each group consists of "
               "a number of distinct types of valves that, in turn, are made in "
               "numerous variations. The way the closure member moves onto the "
               "seat gives a particular group or type of valve a typical "
               "<b>flow-control characteristic</b>. This characteristic has been "
               "used to establish a preliminary chart for the selection of valves; "
               "the final selection may be made from the description of the "
               "various types of valves and their variations that follow that "
               "chart."))
    b.append(_t_groups("en"))

    b.append(h2("Check valves", "Van một chiều"))
    b.append(p("The many types of check valves are likewise divided into four "
               "groups according to the way the closure member moves onto the "
               "seat: <i>lift</i>, <i>swing</i> (single and double plate), "
               "<i>tilting disc</i>, and <i>diaphragm</i>. Their basic duty is to "
               "prevent backflow. However, the valves should also <b>close fast "
               "enough</b> to prevent the formation of a significant reverse-flow "
               "velocity, which on sudden shut-off may introduce an undesirably "
               "high surge pressure and/or cause heavy slamming of the closure "
               "member against the seat. In addition, the closure member should "
               "remain <b>stable</b> in the open valve position. Chapter 4 "
               "describes the design and operating characteristics of these valves "
               "and discusses the criteria upon which check valves should be "
               "selected."))

    b.append(h2("Pressure relief valves", "Van an toàn áp suất"))
    b.append(p("Pressure relief valves are divided into two major groups: "
               "<b>direct-acting</b> pressure relief valves that are actuated "
               "directly by the pressure of the system fluid, and <b>pilot-"
               "operated</b> pressure relief valves in which a pilot controls the "
               "opening and closing of the main valve in response to the system "
               "pressure."))
    b.append(ul([
        "Direct-acting valves may be provided with an <b>auxiliary actuator</b> "
        "that assists valve lift on opening and/or introduces a supplementary "
        "closing force on reseating. Lift assistance is intended to prevent valve "
        "<i>chatter</i>, while supplementary loading is intended to reduce valve "
        "<i>simmer</i>. The auxiliary actuator is actuated by a foreign power "
        "source; should it fail, the valve operates as a direct-acting pressure "
        "relief valve.",
        "Pilot-operated valves may use a <b>direct-acting pilot</b> that controls "
        "the main valve by means of an internal mechanism, or an <b>indirect-"
        "acting pilot</b> that controls the main valve by means of the fluid "
        "discharged from the pilot.",
        "A third type is the <b>powered</b> pressure relief valve, in which the "
        "pilot is operated by a foreign power source; this type is restricted to "
        "applications required by code.",
    ]))

    b.append(h2("Rupture discs", "Đĩa nứt vỡ"))
    b.append(p("Rupture discs are non-reclosing pressure relief devices that may "
               "be used alone or in conjunction with pressure relief valves. The "
               "principal types are <b>forward-domed</b> discs, which fail in "
               "tension, and <b>reverse-buckling</b> discs, which fail in "
               "compression. Reverse-buckling discs can be manufactured to close "
               "burst tolerances; on the debit side, not all of them are suitable "
               "for relieving incompressible fluids."))
    b.append(p("While the application of pressure relief valves is restricted to "
               "relieving <b>nonviolent</b> pressure excursions, rupture discs may "
               "also be used for relieving violent pressure excursions resulting "
               "from the <b>deflagration</b> of flammable gases and dust. Rupture "
               "discs for deflagration venting of atmospheric-pressure containers "
               "or buildings are referred to as <b>vent panels</b>."))

    b.append(h2("Units of measurement and size/class identification",
                "Đơn vị đo và quy ước định danh"))
    b.append(p("Measurements are given in <b>SI and imperial units</b>. Equations "
               "for solving in customary but incoherent units are presented "
               "separately for solution in SI and imperial units, as presented "
               "customarily by U.S. manufacturers; equations presented in "
               "coherent units are valid for solving in either system."))
    b.append(p("The identification of valve sizes and pressure classes follows the "
               "recommendations of <b>MSS Standard Practice SP-86</b>: nominal "
               "sizes and pressure classes are expressed <i>without units</i> — "
               "e.g. NPS 2, DN 50, Class 150, PN 20. NPS 2 stands for nominal pipe "
               "size 2 in., DN 50 for diameter nominal 50 mm, Class 150 for class "
               "150 lb, and PN 20 for pressure nominal 20 bar."))

    b.append(h2("Standards and additional chapters",
                "Tiêu chuẩn và các chương bổ sung"))
    b.append(p("Appendix C contains the more important U.S., British and ISO "
               "standards pertaining to valves, grouped by valve type or group. "
               "The fifth edition adds three chapters not previously included: "
               "<b>chapter 8 — Actuators</b>, <b>chapter 9 — Double Block and "
               "Bleed Ball Valves</b>, and <b>chapter 10 — Mechanical Locking "
               "Devices for Valves</b>, plus a comprehensive glossary in Appendix "
               "E."))

    b.append(h3("Not a control valve book", "Sách không bàn về van điều khiển"))
    b.append(p("This book does <b>not</b> deal with control valves. For that "
               "field, the source directs readers to two ISA publications: "
               "(1) H. D. Baumann, <i>Control Valve Primer, A User's Guide</i> "
               "(3rd edition, 1998) — with new material on valve sizing, smart "
               "(digital) valve positioners, field-based architecture, network "
               "system technology, and control loop performance evaluation; "
               "(2) Guy Borden (ed.), <i>Control Valves, Practical Guides for "
               "Measuring and Control</i> (1998) — part of the ISA Practical Guide "
               "Series, whose last chapter also covers regulators and compares "
               "their performance against control valves."))
    b.append(note("Central idea: valve selection starts from the <b>duty</b> "
                  "(stop/start, throttle, divert, prevent backflow, relieve "
                  "pressure) and from <b>the way the closure member moves onto "
                  "the seat</b> — that motion is what creates each family's flow "
                  "characteristic and sealing mechanism. Cost comes last: a valve "
                  "that fails the design criteria is too expensive even when "
                  "free. The book follows exactly that order: sealing and flow "
                  "fundamentals → each manual valve family → check valves → "
                  "pressure relief valves → rupture discs → sizing → actuators → "
                  "mechanical locking."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © 2004 Elsevier Inc. (Gulf Professional Publishing).</i>"))
    return "".join(b)
