# -*- coding: utf-8 -*-
"""Book 7, Chapter 27 - Sixteen Commandments: What You Shall Not Do! /
Mười sáu điều răn: Những điều bạn không được làm (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
165-166 (PDF pp. 161-162; printed = PDF + 4). Two printed pages, sixteen
numbered "thou shalt not" rules, no figures, tables, equations or references.
"""
from cvp_common import h2, note, ol, p

PAGES_SRC = 2
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Sixteen Commandments: What You Shall Not Do!"
TITLE_VI = "Mười sáu điều răn: Những điều bạn không được làm"

_VI_ITEMS = [
    "Lắp van hơi ở đáy của đường ống dẫn hơi đi xuống (down-header).",
    "Lắp van hơi ở đáy của đường ống dẫn hơi đi xuống mà không bố trí bẫy hơi gần "
    "phía đầu vào của van.",
    "Đặt van hồi lưu ngưng tụ cách bình hóa hơi (flash tank) hoặc thiết bị ngưng "
    "tụ hơn 3 ft.",
    "Mua van có bộ lồng định hình (cage-trim) cho dịch vụ nhiệt độ cao mà không có "
    "đỡ đàn hồi giữa lồng và nắp van.",
    "Mua bộ chuyển đổi I/P có tín hiệu đầu ra 3 đến 15 psi khi lò xo cơ cấu chấp "
    "hành của van cũng là 3 đến 15 psi và không có bộ định vị.",
    "Mua van điều khiển không mặt bích kiểu wafer mà không có vỏ che bảo vệ ở nơi "
    "có nguy cơ cháy.",
    "Khởi động van điều khiển khi chưa kiểm tra độ kín của đệm thân van.",
    "Thử áp lực thủy tĩnh van có phớt màng (bellows seal) khi chưa kiểm tra ý kiến "
    "của nhà sản xuất.",
    "Lắp van cầu một đế với cơ cấu chấp hành màng lò xo, chảy theo hướng đóng "
    "(flow-to-close), trừ khi van có bộ lưu lượng nhỏ hoặc chỉ dùng cho dịch vụ "
    "đóng‑mở.",
    "Dùng vật liệu thân van bằng thép cacbon cho dịch vụ nước bão hòa (ngưng tụ).",
    "Lắp van vào đường ống có đường kính lớn hơn hai lần đường kính của van.",
    "Để bộ điều khiển mất ổn định quá lâu; hậu quả có thể là đệm thân van bị rò.",
    "Để vận tốc đầu ra của van vượt quá 250 ft/s khi dùng bộ lồng giảm tiếng ồn "
    "(low-noise trim).",
    "Lắp cơ cấu chấp hành nặng đặt nằm ngang mà không có giá đỡ thích hợp.",
    "Cách nhiệt nắp van (bonnet) của van cryogenic.",
    "Bịt lỗ thông hơi trên cơ cấu chấp hành khí nén.",
]

_EN_ITEMS = [
    "Install a steam valve at the bottom of a down-header.",
    "Install a steam valve at the bottom of a down-header without providing a "
    "steam trap near the inlet side of a valve.",
    "Locate a condensate return valve more than 3 ft away from a flash tank or "
    "condenser.",
    "Buy a cage-trim valve for elevated temperature service without elastic "
    "support between the cage and bonnet.",
    "Buy an I/P transducer with a 3 to 15 psi output signal when the actuator "
    "spring of the valve is also 3 to 15 psi and there is no positioner.",
    "Buy a flangeless, wafer-style control valve without a protective shroud "
    "where there is a fire hazard.",
    "Start up a control valve without first checking the packing tightness.",
    "Hydrostatically test a valve with bellows seal without first checking with "
    "the manufacturer.",
    "Install a single-seated globe valve with a spring-diaphragm actuator, "
    "flow-to-close, unless it has a small flow trim or it is used only for on-off "
    "service.",
    "Use carbon steel valve body material for saturated water (condensate) service.",
    "Install a valve in a pipe more than twice the diameter of the valve.",
    "Let a controller go unstable for too long; the result may be a leaky stem "
    "packing.",
    "Allow the valve outlet velocity to exceed 250 ft/s when you use a low-noise "
    "trim.",
    "Install a horizontally placed heavy actuator without proper support.",
    "Insulate a valve bonnet on a cryogenic valve.",
    "Plug the vent hole on a pneumatic actuator.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 27.</b> đường ống dẫn hơi đi xuống (down-header) · "
                "bẫy hơi (steam trap) · van hồi lưu ngưng tụ · bình hóa hơi (flash tank) · "
                "thiết bị ngưng tụ · bộ lồng định hình (cage-trim) · đỡ đàn hồi · lồng van "
                "· nắp van (bonnet) · bộ chuyển đổi I/P · lò xo cơ cấu chấp hành · bộ định "
                "vị · van không mặt bích kiểu wafer · vỏ che bảo vệ · nguy cơ cháy · đệm "
                "thân van · thử áp lực thủy tĩnh · phớt màng (bellows seal) · van cầu một "
                "đế · cơ cấu chấp hành màng lò xo · hướng chảy đóng / chảy mở · bộ lưu "
                "lượng nhỏ · dịch vụ đóng‑mở · thép cacbon · nước bão hòa / ngưng tụ · "
                "đường kính ống · mất ổn định vòng điều khiển · vận tốc đầu ra · bộ lồng "
                "giảm tiếng ồn · cơ cấu chấp hành nặng · van cryogenic · lỗ thông hơi · "
                "cơ cấu chấp hành khí nén")
    return ("<b>Key terms.</b> down-header · steam trap · condensate return valve · flash "
            "tank · condenser · cage-trim valve · elastic support · cage · bonnet · I/P "
            "transducer · actuator spring · positioner · flangeless wafer-style valve · "
            "protective shroud · fire hazard · stem packing · hydrostatic test · bellows "
            "seal · single-seated globe valve · spring-diaphragm actuator · flow-to-close "
            "/ flow-to-open · small flow trim · on-off service · carbon steel · saturated "
            "water / condensate · pipe diameter · loop instability · outlet velocity · "
            "low-noise trim · heavy actuator · cryogenic valve · vent hole · pneumatic "
            "actuator")


def body_vi():
    b = []
    b.append(h2("Mười sáu điều răn: Những điều bạn không được làm!",
                "Sixteen Commandments: What You Shall Not Do!"))
    b.append(p("Bạn không được:"))
    b.append(ol(_VI_ITEMS))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương chỉ gồm mười sáu điều liệt kê ngắn "
                  "dưới tiêu đề “You shall not”, không có giải thích kèm theo, không có hình, "
                  "bảng, phương trình hay tài liệu tham khảo. Các con số và đơn vị gốc "
                  "(3 ft, 3–15 psi, 250 ft/s) được giữ nguyên; văn bản tiếng Việt thêm bản "
                  "dịch thuật ngữ trong ngoặc để người đọc dễ đối chiếu."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © 2011 Hans D. Baumann, do ISA / John Wiley &amp; Sons xuất bản.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Sixteen Commandments: What You Shall Not Do!",
                "Sixteen Commandments: What You Shall Not Do!"))
    b.append(p("You shall not:"))
    b.append(ol(_EN_ITEMS))
    b.append(note("<b>Source quirks.</b> The chapter consists only of sixteen short numbered "
                  "rules under the heading “You shall not,” with no accompanying explanation, "
                  "figures, tables, equations or references. Original numbers and units "
                  "(3 ft, 3–15 psi, 250 ft/s) are retained verbatim."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 2011 Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>"))
    return "".join(b)
