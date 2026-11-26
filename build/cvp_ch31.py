# -*- coding: utf-8 -*-
"""Book 7, Chapter 31 - Thinking “Green” and Saving Metal /
Tư duy “xanh” và tiết kiệm kim loại (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
183-184 (PDF pp. 176-177; printed = PDF + 7). Two printed pages, one vector
figure (Figure 31-1), one long endnote and a three-item additional-reading
list. No tables or equations.
"""
from cvp_common import fig, h2, h3, note, p, ul

import cvpfig31 as F

PAGES_SRC = 2
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Thinking “Green” and Saving Metal"
TITLE_VI = "Tư duy “xanh” và tiết kiệm kim loại"

_ENDNOTE_EN = (
    "<b>1</b> This article on the Electroheat Induction website provides calculations "
    "for determining the kilowatt hours required to melt various types of steel: "
    "“How to Calculate Electricity Cost for Melting Metal in Induction Melting Furnace: "
    "Power Consumption for the Electroheat Furnace for Cast Iron Melting Requires "
    "550-575 kWh/ton,” November 7, 2013, "
    "https://electroheatinduction.com/"
    "how-to-calculate-electricity-cost-for-melting-metal-in-induction-melting-furnace/."
)
_ENDNOTE_VI = (
    "<b>1</b> Bài viết này trên trang web Electroheat Induction cung cấp các phép tính "
    "để xác định số kilowatt-giờ cần thiết để nấu chảy các loại thép khác nhau: "
    "“How to Calculate Electricity Cost for Melting Metal in Induction Melting Furnace: "
    "Power Consumption for the Electroheat Furnace for Cast Iron Melting Requires "
    "550-575 kWh/ton,” ngày 7 tháng 11 năm 2013, "
    "https://electroheatinduction.com/"
    "how-to-calculate-electricity-cost-for-melting-metal-in-induction-melting-furnace/."
)

_READING_EN = [
    "C. E. Cating, “Control Valve Industry Update—1990,” Control (March 1990): 34–38.",
    "H. D. Baumann, “Important Trends in Control Valves and Actuators,” Instrument "
    "&amp; Control Systems (November 1975): 21–25.",
    "L. Driskell, “Save Money by Combining Regulators, Distributed Control,” Power "
    "(April 1985).",
]
_READING_VI = [
    "C. E. Cating, “Control Valve Industry Update—1990,” Control (tháng 3 năm 1990): 34–38.",
    "H. D. Baumann, “Important Trends in Control Valves and Actuators,” Instrument "
    "&amp; Control Systems (tháng 11 năm 1975): 21–25.",
    "L. Driskell, “Save Money by Combining Regulators, Distributed Control,” Power "
    "(tháng 4 năm 1985).",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 31.</b> tư duy “xanh” (green thinking) · độ giảm áp "
                "qua van (pressure drop across valves) · kiểu van (valve type) · van lồng "
                "(cage valve) · mặt bích nắp van (bonnet flange) · giữ lồng trong thân van "
                "(cage retention) · cụm thân van kiểu lồng (cage-type valve body "
                "subassembly) · tiết lưu hai cấp (double-stage throttling) · khả năng "
                "chống xâm thực (cavitation resistance) · độ phạm vi lưu lượng "
                "(rangeability) · vòng làm kín trượt (sliding seal) · phớt trên mềm "
                "(flexible top seal) · phớt trên nén (compressible top seal) · lồng vặn "
                "vào thân (cage screwed into housing) · nút nối đóng ghim (staked stem "
                "connection) · van cầu (globe valve) · van quay (rotary valve) · van "
                "đóng–mở (on-off valve) · lưu lượng C<sub>v</sub> · năng lượng bơm và máy "
                "nén · chi phí vận chuyển (freight) · lợi nhuận (profit margin) · nấu chảy "
                "bằng cảm ứng (induction melting) · kWh trên tấn (kWh/ton)")
    return ("<b>Key terms.</b> green thinking · pressure drop across valves · valve type "
            "selection · cage valve · bonnet flange · cage retention within the valve "
            "housing · cage-type valve body subassembly · double-stage throttling · "
            "cavitation resistance · rangeability · sliding seal · flexible top seal · "
            "compressible top seal · cage screwed into housing · staked stem connection · "
            "globe valve · rotary valve · on-off valve · flow capacity C<sub>v</sub> · "
            "energy used to run pumps and compressors · freight expenses · profit margin · "
            "induction melting · kilowatt hours per ton (kWh/ton)")


def body_vi():
    b = []
    b.append(h2("Tư duy “xanh” và tiết kiệm kim loại",
                "Thinking “Green” and Saving Metal"))
    b.append(p("Một nỗ lực toàn cầu nhằm tiết kiệm năng lượng đang được tiến hành. Nỗ lực "
               "này có thể được hỗ trợ bởi cả người sử dụng lẫn nhà sản xuất van điều "
               "khiển. Bên cạnh việc phân bổ độ giảm áp thấp hơn qua van như đã nêu ở "
               "Chương 29, “Saving Energy,” có thể nhấn mạnh vào thiết kế và lựa chọn "
               "kiểu van (ví dụ, xem Chương 6). Hầu hết các thiết kế hiện nay khá nặng, và "
               "có thể tiết kiệm được nhiều kim loại<sup>1</sup>, chẳng hạn ở van lồng. "
               "Ở đây, trọng lượng của mặt bích nắp van nặng có thể được cắt làm đôi nếu "
               "lồng được giữ chắc trong thân van (xem Hình 31-1). Nhiều van cầu cũng có "
               "thể được thay bằng các kiểu van quay (không phải loại đóng–mở) làm được "
               "cùng công việc với trọng lượng chưa bằng một nửa. Thêm vào đó, van điều "
               "khiển quay có lưu lượng (C<sub>v</sub>) lớn hơn khoảng 20% so với van cầu, "
               "nhờ vậy giảm được độ giảm áp và tiết kiệm năng lượng dùng để chạy bơm và "
               "máy nén."))
    b.append(p("Tư duy “xanh” như vậy không chỉ giảm mạnh việc sử dụng các kim loại tiêu "
               "thụ nhiều năng lượng mà còn giảm chi phí vận chuyển (cước vận chuyển). "
               "Cuối cùng, những khoản tiết kiệm này cũng cải thiện đáng kể lợi nhuận của "
               "cả nhà sản xuất lẫn người sử dụng."))
    b.append(note(_ENDNOTE_VI))
    b.append(fig(1, F.fig_f311()))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul(_READING_VI))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm hai trang in (183–184; trang "
                  "in = trang PDF + 7), có một hình, một chú thích cuối trang và danh sách "
                  "đọc thêm gồm ba mục; không có bảng hay phương trình. Hình 31-1 được vẽ "
                  "lại dưới dạng vector từ trang in, đơn giản hóa nhưng giữ nguyên cấu trúc "
                  "và các nhãn A–E. Các giá trị gốc được giữ lại: cắt làm đôi trọng lượng "
                  "mặt bích nắp van, chưa bằng một nửa trọng lượng, khoảng 20% C<sub>v</sub> "
                  "và 550-575 kWh/ton."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © 2011 Hans D. Baumann, do ISA / John Wiley &amp; Sons xuất bản.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Thinking “Green” and Saving Metal",
                "Thinking “Green” and Saving Metal"))
    b.append(p("A worldwide effort to save energy is currently underway. This effort can "
               "be supported by users and manufacturers of control valves alike. Besides "
               "assigning lower pressure drops across valves as outlined in Chapter 29, "
               "“Saving Energy,” emphasis could be placed on the design and selection of "
               "valve types (for an example, see Chapter 6). Most current designs are "
               "quite heavy, and much metal<sup>1</sup> could be saved in cage valves, for "
               "example. Here the weight of the heavy bonnet flange could be cut in half "
               "with proper cage retention within the valve housing (see Figure 31-1). "
               "Many globe valves, too, can be replaced by rotary valve styles (not on-off "
               "types) that can perform the same job at less than half the weight. In "
               "addition, rotary control valves offer about 20% more flow capacity "
               "(C<sub>v</sub>) over globe valves, thus enabling lower pressure drops and "
               "savings in the energy used to run pumps and compressors."))
    b.append(p("Such green thinking would not only drastically reduce the use of "
               "energy-consuming metals but would also reduce transportation (freight) "
               "expenses. Finally, such savings will also greatly improve the profit "
               "margins of both the manufacturer and the user."))
    b.append(note(_ENDNOTE_EN))
    b.append(fig(1, F.fig_f311()))
    b.append(h3("Additional Reading", "Additional Reading"))
    b.append(ul(_READING_EN))
    b.append(note("<b>Source quirks.</b> The chapter spans two printed pages (183–184; "
                  "printed = PDF + 7), with one figure, one endnote and a three-item "
                  "additional-reading list; no tables or equations. Figure 31-1 was "
                  "redrawn as a vector from the printed page, simplified but keeping its "
                  "topology and A–E callouts. Original values are retained: the bonnet "
                  "flange weight cut in half, less than half the weight, about 20% more "
                  "C<sub>v</sub>, and 550-575 kWh/ton."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 2011 Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)
