# -*- coding: utf-8 -*-
"""Book 4, Chapter 2 — Design Fundamentals (EN/VI bilingual)."""

import prvfig as F
from prv_common import p, h2, h3, ul, fig, note

PAGES_SRC = 6
BYLINE = "Crosby Valve Inc. · Technical Document TP-V300"
TITLE_EN = "Fundamentals of Pressure Relief Valve Design"
TITLE_VI = "Nguyên lý cơ bản thiết kế van xả áp lực"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 2.</b> "
                "MAWP — áp suất làm việc cực đại cho phép · blowdown — tỷ lệ đóng lại · "
                "huddling chamber — buồng điều khiển · JLT — trim lưu chất · soft seat — đệm mềm.")
    return ("<b>Key terms.</b> MAWP — maximum allowable working pressure · blowdown — the "
            "reclose ratio · huddling chamber — the control chamber · JLT — liquid trim · "
            "soft seat — elastomer seating.")


def body_vi():
    b = []
    b.append(p("Một van xả áp lực là thiết bị an toàn dùng để bảo vệ bình chịu áp lực hoặc hệ "
               "thống trong sự cố quá áp. Sự cố quá áp là bất kỳ điều kiện nào làm áp suất vượt "
               "quá áp suất thiết kế hoặc áp suất làm việc cực đại cho phép (MAWP). Vì là thiết "
               "bị an toàn, van chịu sự chi phối của nhiều tiêu chuẩn và quy code."))
    b.append(h2("Buồng điều khiển và vòng miệng phun", "Control / huddling chamber"))
    b.append(p("Thiết kế buồng điều khiển (huddling chamber) là một chuỗi đánh đổi: tối đa hóa "
               "lực nâng thì blowdown dài, còn tối thiểu hóa blowdown thì lực nâng yếu. Nhiều "
               "van vì vậy được trang bị vòng miệng phun (nozzle ring) điều chỉnh được để thay "
               "đổi hình học buồng điều khiển nhằm đáp ứng yêu cầu vận hành cụ thể."))
    b.append(fig(1, F.fig_f22_closed()))
    b.append(fig(2, F.fig_f22_open()))
    b.append(p("Hình F2-2 minh họa đĩa được lò xo giữ ở vị trí đóng. Khi áp suất hệ thống đạt "
               "áp lực thiết lập, lực do áp suất tác dụng lên diện tích A1 bằng lực lò xo và đĩa "
               "nhấc lên cho chất lưu thoát ra. Khi áp suất trở về mức an toàn, van đóng lại. Vì "
               "lực lò xo tăng khi đĩa nhấc, áp suất hệ thống phải tăng thêm (cho phép quá áp) "
               "để đạt hành trình toàn mở."))
    b.append(fig(3, F.fig_f23()))
    b.append(h2("Thiết kế trim lưu chất", "Liquid trim designs"))
    b.append(p("Với ứng dụng chất lỏng, Crosby cung cấp thiết kế trim lưu chất có bản quyền "
               "kiểu JLT-JOS hoặc JLT-JBS (Hình F2-4), có đệm kim loại hoặc mềm, cho hiệu năng "
               "không rung (non-chattering) và lưu lượng lớn tại quá áp 10%."))
    b.append(fig(4, F.fig_f24()))
    b.append(h2("Vật liệu chế tạo", "Materials of construction"))
    b.append(p("Tương thích với chất lưu đạt được bằng chọn vật liệu đủ bền chịu áp suất, nhiệt "
               "độ và chống ăn mòn; bề mặt tiếp xúc (đĩa, miệng phun) phải đạt độ phẳng quang "
               "học để kín khít. Tỷ lệ giãn nở nhiệt của các chi tiết ăn khớp cũng là một yếu tố "
               "thiết kế."))
    b.append(h2("Xét đến áp suất ngược", "Back pressure considerations"))
    b.append(p("Van trên hệ thống sạch, không độc, không ăn mòn có thể xả thẳng ra khí quyển; "
               "van trên hệ thống kín hoặc ống xả dài có thể phát sinh áp suất ngược lớn, cần "
               "đánh giá ảnh hưởng đến hiệu năng và lưu lượng xả."))
    b.append(h2("Rò rỉ tại đệm kín", "Seat leakage"))
    b.append(p("Van phải giữ kín trong thời gian dài dưới điều kiện áp suất và nhiệt độ thay đổi. "
               "Giới hạn rò rỉ cho van xả áp nghiêm ngặt hơn nhiều so với van thông thường; đạt "
               "được nhờ kiểm soát khe lệch, bề mặt phẳng quang học và vật liệu phù hợp. Với "
               "các hệ yêu cầu kín hơn, có thể dùng đệm mềm (Hình F2-6)."))
    b.append(fig(5, F.fig_f26()))
    b.append(h2("Van vận hành bằng pilot", "Pilot operated pressure relief valves"))
    b.append(p("Van vận hành bằng pilot gồm van chính có đĩa vận hành bằng piston (hoặc màng) "
               "và một pilot. Trong điều kiện bình thường, pilot cho áp suất hệ thống vào buồng "
               "piston; vì diện tích piston lớn hơn diện tích đệm đĩa nên đĩa được giữ đóng. Khi "
               "đạt áp lực thiết lập, pilot tác động ngắt áp suất vào buồng piston đồng thời xả "
               "buồng này, làm đĩa mở. Pilot giúp áp suất vận hành có thể tiệm cận 95% áp lực "
               "thiết lập mà không tăng rò rỉ, và cho phép đóng lại với blowdown rất ngắn."))
    b.append(fig(6, F.fig_f29()))
    b.append(h2("Lưu lượng xả cần thiết", "Required relieving capacity"))
    b.append(p("Van phải xả đủ chất lưu để áp suất không vượt quá quá áp quy định. Cần đánh giá "
               "mọi nguyên nhân quá áp (van chặn không đóng, lỗi điều khiển, hỏa hoạn, hỏng "
               "bơm, phản ứng mất kiểm soát, cách ly bình…) và lấy tổ hợp xấu nhất làm cơ sở. "
               "Tổng lưu lượng định mức của (các) van chọn phải lớn hơn lưu lượng cần thiết."))
    b.append(note("Tóm tắt: chương giới thiệu các nguyên lý thiết kế van xả áp và các tiêu chuẩn "
                  "chi phối, nhấn mạnh đây là thiết bị an toàn bảo vệ bình/chệ̂ thồng khỏi sự cố "
                  "phá hủy thảm khốc."))
    return "".join(b)


def body_en():
    b = []
    b.append(p("A pressure relief valve is a safety device designed to protect a pressurized "
               "vessel or system during an overpressure event. An overpressure event is any "
               "condition that drives pressure beyond the specified design pressure or maximum "
               "allowable working pressure (MAWP). Being safety devices, relief valves are "
               "governed by many Codes and Standards."))
    b.append(h2("Control / huddling chamber", "Buồng điều khiển và vòng miệng phun"))
    b.append(p("The design of the control (huddling) chamber involves trade-offs: maximizing "
               "lift effort gives a long blowdown, while minimizing blowdown diminishes lift "
               "effort. Many valves are therefore fitted with an adjustable nozzle ring that "
               "varies the control-chamber geometry to meet a particular operating requirement."))
    b.append(fig(1, F.fig_f22_closed()))
    b.append(fig(2, F.fig_f22_open()))
    b.append(p("Figure F2-2 is a simple sketch of the disc held closed by the spring. When "
               "system pressure reaches set pressure, the force of pressure over area A1 equals "
               "the spring force and the disc lifts to let fluid escape. As the disc lifts, the "
               "spring force increases, so system pressure must rise further (the allowable "
               "overpressure) to reach full lift."))
    b.append(fig(3, F.fig_f23()))
    b.append(h2("Liquid trim designs", "Thiết kế trim lưu chất"))
    b.append(p("For liquid service Crosby offers a patented liquid trim designated Style JLT-JOS "
               "or JLT-JBS (Figure F2-4), available in metal or soft-seated versions, giving "
               "stable non-chattering performance and high capacity at 10% overpressure."))
    b.append(fig(4, F.fig_f24()))
    b.append(h2("Materials of construction", "Vật liệu chế tạo"))
    b.append(p("Compatibility with the process fluid is achieved by careful material selection "
               "for strength, temperature and chemical resistance; seating surfaces must be "
               "finely finished (optically flat) for tight shut-off. Thermal expansion of mating "
               "parts is another design factor."))
    b.append(h2("Back pressure considerations", "Xét đến áp suất ngược"))
    b.append(p("Valves on clean, non-toxic, non-corrosive systems may vent to atmosphere; those "
               "on corrosive, toxic or valuable recoverable fluids vent into closed systems. "
               "Closed systems or long vent pipes can develop high back pressure that must be "
               "evaluated for its effect on performance and relieving capacity."))
    b.append(h2("Seat leakage", "Rò rỉ tại đệm kín"))
    b.append(p("Relief valves must hold tight over long periods. Allowable seat leakage limits "
               "are far more stringent than for other valves, achieved through part alignment, "
               "optically flat seating and suitable materials. Where system conditions permit, "
               "soft or elastomer seats (Figure F2-6) give additional tightness."))
    b.append(fig(5, F.fig_f26()))
    b.append(h2("Pilot operated pressure relief valves", "Van vận hành bằng pilot"))
    b.append(p("A pilot-operated PRV consists of a main valve with a piston- or diaphragm-"
               "operated disc and a pilot. Under normal conditions the pilot admits system "
               "pressure into the piston chamber; because the piston area exceeds the disc seat "
               "area, the disc is held closed. At set pressure the pilot shuts off supply to the "
               "piston chamber and vents it, opening the disc. Pilots allow operating pressure "
               "to reach within 5% of set pressure without increased seat leakage, and can be "
               "set to close with very short blowdown."))
    b.append(fig(6, F.fig_f29()))
    b.append(h2("Required relieving capacity", "Lưu lượng xả cần thiết"))
    b.append(p("The valve must relieve enough fluid that pressure never exceeds the specified "
               "overpressure. All credible overpressure sources (failed shut-off valve, control "
               "failure, fire, pump failure, runaway reaction, isolation, etc.) are evaluated "
               "and the worst-case combination sets the required capacity. Total rated "
               "relieving capacity of the selected valve(s) must exceed that requirement."))
    b.append(note("Summary: this chapter introduces the design considerations and governing "
                  "Codes and Standards, emphasizing that a relief valve is a safety device that "
                  "protects vessels and systems from catastrophic failure."))
    return "".join(b)
