# -*- coding: utf-8 -*-
"""Book 4, Chapter 3 — Terminology (EN/VI bilingual, no figures).

Adapted from ANSI/ASME Performance Test Code PTC-25.3-1988, Appendix I.
Sections A–B are prose; C–E and the CEN block are term/definition lists.
"""

from prv_common import p, h2, h3, h4, ul, note

PAGES_SRC = 4
BYLINE = "Crosby Valve Inc. · Technical Document TP-V300"
TITLE_EN = "Terminology"
TITLE_VI = "Thuật ngữ"


# -------------------------------------------------------------------------
# Term/definition source rows: (en_term, en_def, vi_term, vi_def)
# Rendered as a <ul> list in either language by _render_terms().
# -------------------------------------------------------------------------
_PARTS = [
    ("approach channel",
     "the passage through which the fluid must pass to reach the operating parts of a pressure relief device",
     "kênh tiếp cận",
     "lối đi mà chất lưu phải đi qua để tới các chi tiết vận hành của thiết bị xả áp lực"),
    ("breaking pin",
     "the load-carrying element of a breaking pin device",
     "chốt phá",
     "chi tiết chịu tải của thiết bị chốt phá"),
    ("breaking pin housing",
     "the structure which encloses the breaking pin mechanism",
     "vỏ bọc chốt phá",
     "kết cấu bao bọc cơ cấu chốt phá"),
    ("discharge channel",
     "the passage through which the fluid must pass between the operating parts of a pressure relief device and its outlet",
     "kênh xả",
     "lối đi mà chất lưu phải đi qua giữa các chi tiết vận hành của thiết bị xả áp lực và đầu ra của nó"),
    ("disc",
     "the pressure containing movable element of a pressure relief valve which effects closure",
     "đĩa (đĩa van)",
     "chi tiết chuyển động chứa áp của van xả áp lực, thực hiện việc đóng kín"),
    ("huddling chamber",
     "the annular pressure chamber located beyond the valve seat for the purpose of generating a popping characteristic",
     "buồng điều khiển (huddling chamber)",
     "buồng áp suất dạng vành khuyên nằm phía sau đệm kín van, dùng để tạo đặc tính bật (popping)"),
    ("lifting device",
     "a device for manually opening a pressure relief valve by the application of external force to lessen the spring loading which holds the valve closed",
     "cơ cấu nâng",
     "thiết bị dùng lực ngoài để mở van xả áp lực bằng tay, làm giảm tải lò xo giữ van đóng"),
    ("lifting lever",
     "see lifting device",
     "đòn bẩy nâng",
     "xem cơ cấu nâng"),
    ("nozzle",
     "a pressure containing element which constitutes the inlet flow passage and includes the fixed portion of the seat closure",
     "miệng phun (nozzle)",
     "chi tiết chứa áp tạo thành lối vào dòng chảy, bao gồm phần cố định của đệm kín"),
    ("pilot valve",
     "an auxiliary valve which actuates a major relieving device (Crosby sometimes calls pilot actuator)",
     "van pilot",
     "van phụ điều khiển thiết bị xả chính (Crosby đôi khi gọi là cơ cấu truyền động pilot)"),
    ("pressure containing member (of a pressure relief device)",
     "a part which is in actual contact with the pressure media in the protected vessel",
     "chi tiết chứa áp",
     "chi tiết tiếp xúc trực tiếp với môi chất áp suất trong bình được bảo vệ"),
    ("pressure retaining member (of a pressure relief device)",
     "a part which is stressed due to its function in holding one or more pressure containing members in position",
     "chi tiết giữ áp",
     "chi tiết chịu ứng suất do chức năng giữ một hoặc nhiều chi tiết chứa áp ở vị trí quy định"),
    ("rupture disc",
     "the pressure containing and pressure sensitive element of a rupture disc device",
     "đĩa vỡ",
     "chi tiết chứa áp và nhạy áp suất của thiết bị đĩa vỡ"),
    ("rupture disc holder",
     "the structure which encloses and clamps the rupture disc in position",
     "giá giữ đĩa vỡ",
     "kết cấu bao bọc và kẹp đĩa vỡ vào vị trí"),
    ("seat",
     "the pressure containing contact between the fixed and moving portions of the pressure containing elements of a valve",
     "đệm kín (seat)",
     "tiếp xúc chứa áp giữa phần cố định và phần chuyển động của các chi tiết chứa áp của van"),
    ("vacuum support",
     "an auxiliary element of a rupture disc device designed to prevent rupture or deformation of the disc due to vacuum or back pressure",
     "giá đỡ chân không",
     "chi tiết phụ của thiết bị đĩa vỡ, ngăn đĩa bị vỡ hoặc biến dạng do chân không hoặc áp suất ngược"),
]

_DIM = [
    ("actual discharge area",
     "the measured minimum net area which determines the flow through a valve",
     "diện tích xả thực",
     "tiết diện thuần nhỏ nhất đo được quyết định dòng chảy qua van"),
    ("bore area",
     "the minimum cross-sectional flow area of a nozzle",
     "diện tích lỗ miệng phun",
     "tiết diện dòng chảy nhỏ nhất của miệng phun"),
    ("bore diameter",
     "the minimum diameter of a nozzle",
     "đường kính lỗ miệng phun",
     "đường kính nhỏ nhất của miệng phun"),
    ("curtain area",
     "the area of the cylindrical or conical discharge opening between the seating surfaces created by the lift of the disc above the seat",
     "diện tích màn (curtain area)",
     "diện tích lỗ xả hình trụ hoặc côn giữa các bề mặt đệm kín, được tạo ra khi đĩa nhấc khỏi đệm"),
    ("developed lift",
     "the actual travel of the disc from closed position to the position reached when the valve is at flow-rating pressure",
     "hành trình phát triển",
     "hành trình thực của đĩa từ vị trí đóng đến vị trí đạt được khi van ở áp suất định mức dòng chảy"),
    ("discharge area",
     "see actual discharge area",
     "diện tích xả",
     "xem diện tích xả thực"),
    ("effective discharge area",
     "a nominal or computed area of flow through a pressure relief valve, differing from the actual discharge area, for use in recognized flow formulas to determine the capacity of a pressure relief valve",
     "diện tích xả hiệu dụng",
     "tiết diện dòng chảy danh định hoặc tính toán qua van xả áp, khác với diện tích xả thực, dùng trong các công thức dòng chảy chuẩn để xác định lưu lượng van"),
    ("inlet size",
     "the nominal pipe size of the inlet of a pressure relief valve, unless otherwise designated",
     "cỡ đầu vào",
     "cỡ ống danh định của đầu vào van xả áp lực, trừ khi có quy định khác"),
    ("lift",
     "the actual travel of the disc away from closed position when a valve is relieving",
     "hành trình nâng",
     "hành trình thực của đĩa rời khỏi vị trí đóng khi van đang xả"),
    ("nozzle area, nozzle throat area",
     "see bore area",
     "diện tích miệng phun, tiết diện cổ miệng phun",
     "xem diện tích lỗ miệng phun"),
    ("nozzle diameter",
     "see bore diameter",
     "đường kính miệng phun",
     "xem đường kính lỗ miệng phun"),
    ("orifice area",
     "see effective discharge area",
     "diện tích lỗ (orifice area)",
     "xem diện tích xả hiệu dụng"),
    ("outlet size",
     "the nominal pipe size of the outlet of a pressure relief valve, unless otherwise designated",
     "cỡ đầu ra",
     "cỡ ống danh định của đầu ra van xả áp lực, trừ khi có quy định khác"),
    ("rated lift",
     "the design lift at which a valve attains its rated relieving capacity",
     "hành trình nâng định mức",
     "hành trình nâng theo thiết kế tại đó van đạt lưu lượng xả định mức"),
    ("seat angle",
     "the angle between the axis of a valve and the seating surface. A flat-seated valve has a seat angle of 90 degrees",
     "góc đệm kín",
     "góc giữa trục van và bề mặt đệm kín. Van đệm phẳng có góc đệm kín 90 độ"),
    ("seat area",
     "the area determined by the seat diameter",
     "diện tích đệm kín",
     "diện tích được xác định bởi đường kính đệm kín"),
    ("seat diameter",
     "the smallest diameter of contact between the fixed and moving portions of the pressure containing elements of a valve",
     "đường kính đệm kín",
     "đường kính tiếp xúc nhỏ nhất giữa phần cố định và phần chuyển động của các chi tiết chứa áp van"),
    ("seat flow area",
     "see curtain area",
     "diện tích dòng chảy qua đệm",
     "xem diện tích màn"),
    ("throat area",
     "see bore area",
     "diện tích cổ",
     "xem diện tích lỗ miệng phun"),
    ("throat diameter",
     "see bore diameter",
     "đường kính cổ",
     "xem đường kính lỗ miệng phun"),
]

_OPS = [
    ("back pressure",
     "the static pressure existing at the outlet of a pressure relief device due to pressure in the discharge system",
     "áp suất ngược",
     "áp suất tĩnh tại đầu ra của thiết bị xả áp do áp suất trong hệ thống xả gây ra"),
    ("blowdown",
     "the difference between actual popping pressure of a pressure relief valve and actual reseating pressure expressed as a percentage of set pressure or in pressure units",
     "độ đóng lại (blowdown)",
     "hiệu giữa áp suất bật thực và áp suất tái ngồi thực của van xả áp, biểu thị bằng % áp suất thiết lập hoặc bằng đơn vị áp suất"),
    ("blowdown pressure",
     "the value of decreasing inlet static pressure at which no further discharge is detected at the outlet of a pressure relief valve after the valve has been subjected to a pressure equal to or above the popping pressure",
     "áp suất đóng lại",
     "giá trị áp suất tĩnh đầu vào giảm tại đó không còn phát hiện xả tại đầu ra van sau khi van chịu áp suất bằng hoặc trên áp suất bật"),
    ("breaking pressure",
     "the value of inlet static pressure at which a breaking pin or shear pin device functions",
     "áp suất phá",
     "giá trị áp suất tĩnh đầu vào tại đó thiết bị chốt phá hoặc chốt cắt hoạt động"),
    ("built-up back pressure",
     "pressure existing at the outlet of a pressure relief device caused by the flow through that particular device into a discharge system",
     "áp suất ngược sinh ra",
     "áp suất tại đầu ra thiết bị xả áp do dòng chảy qua chính thiết bị đó vào hệ thống xả gây ra"),
    ("burst pressure",
     "the value of inlet static pressure at which a rupture disc device functions",
     "áp suất vỡ",
     "giá trị áp suất tĩnh đầu vào tại đó thiết bị đĩa vỡ hoạt động"),
    ("chatter",
     "abnormal rapid reciprocating motion of the movable parts of a pressure relief valve in which the disc contacts the seat",
     "rung va (chatter)",
     "chuyển động tịnh tiến nhanh bất thường của các chi tiết chuyển động van xả áp, trong đó đĩa chạm vào đệm kín"),
    ("closing pressure",
     "the value of decreasing inlet static pressure at which the valve disc reestablishes contact with the seat or at which lift becomes zero",
     "áp suất đóng",
     "giá trị áp suất tĩnh đầu vào giảm tại đó đĩa van tái tiếp xúc với đệm kín hoặc hành trình nâng về không"),
    ("coefficient of discharge",
     "the ratio of the measured relieving capacity to the theoretical relieving capacity",
     "hệ số lưu lượng xả",
     "tỷ số giữa lưu lượng xả đo được và lưu lượng xả lý thuyết"),
    ("cold differential test pressure",
     "the inlet static pressure at which a pressure relief valve is adjusted to open on the test stand. This test pressure includes corrections for service conditions of superimposed back pressure and/or temperature",
     "áp suất thử vi sai nguội",
     "áp suất tĩnh đầu vào mà tại đó van xả áp được chỉnh mở trên băng thử. Áp suất thử này bao gồm hiệu chỉnh cho điều kiện vận hành của áp suất ngược chồng chất và/hoặc nhiệt độ"),
    ("constant back pressure",
     "a superimposed back pressure which is constant with time",
     "áp suất ngược không đổi",
     "áp suất ngược chồng chất không đổi theo thời gian"),
    ("cracking pressure",
     "see opening pressure",
     "áp suất nứt (cracking)",
     "xem áp suất mở"),
    ("flow capacity",
     "see measured relieving capacity",
     "lưu lượng xả",
     "xem lưu lượng xả đo được"),
    ("flow-rating pressure",
     "the inlet static pressure at which the relieving capacity of a pressure relief device is measured",
     "áp suất định mức dòng chảy",
     "áp suất tĩnh đầu vào tại đó lưu lượng xả của thiết bị xả áp được đo"),
    ("flutter",
     "abnormal, rapid reciprocating motion of the movable parts of a pressure relief valve in which the disc does not contact the seat",
     "rung lắc (flutter)",
     "chuyển động tịnh tiến nhanh bất thường của các chi tiết chuyển động van xả áp, trong đó đĩa không chạm đệm kín"),
    ("leak pressure",
     "see start-to-leak pressure",
     "áp suất rò",
     "xem áp suất bắt đầu rò"),
    ("leak test pressure",
     "the specified inlet static pressure at which a quantitative seat leakage test is performed in accordance with a standard procedure",
     "áp suất thử rò",
     "áp suất tĩnh đầu vào quy định mà tại đó thử nghiệm rò đệm kín định lượng được thực hiện theo quy trình chuẩn"),
    ("marked breaking pressure",
     "the value of pressure marked on a breaking pin device or its nameplate",
     "áp suất phá ghi trên nhãn",
     "giá trị áp suất ghi trên thiết bị chốt phá hoặc bảng tên của nó"),
    ("marked burst pressure",
     "the value of pressure marked on the rupture disc device or its nameplate or on the tag of the rupture disc and indicates the burst pressure at the coincident disc temperature",
     "áp suất vỡ ghi trên nhãn",
     "giá trị áp suất ghi trên thiết bị đĩa vỡ, bảng tên hoặc thẻ đĩa, chỉ áp suất vỡ tại nhiệt độ đĩa tương ứng"),
    ("marked pressure",
     "the value or values of pressure marked on a pressure relief device",
     "áp suất ghi trên nhãn",
     "giá trị hoặc các giá trị áp suất ghi trên thiết bị xả áp"),
    ("marked relieving capacity",
     "see rated relieving capacity",
     "lưu lượng xả định mức ghi trên nhãn",
     "xem lưu lượng xả định mức"),
    ("measured relieving capacity",
     "the relieving capacity of a pressure relief device measured at the flow-rating pressure, expressed in gravimetric or volumetric units",
     "lưu lượng xả đo được",
     "lưu lượng xả của thiết bị xả áp đo tại áp suất định mức dòng chảy, biểu thị bằng đơn vị khối lượng hoặc thể tích"),
    ("opening pressure",
     "the value of increasing inlet static pressure of a pressure relief valve at which there is a measurable lift, or at which the discharge becomes continuous as determined by seeing, feeling, or hearing",
     "áp suất mở",
     "giá trị áp suất tĩnh đầu vào tăng của van xả áp tại đó có hành trình nâng đo được, hoặc xả trở nên liên tục theo quan sát, cảm giác hoặc âm thanh"),
    ("start-to-discharge pressure",
     "see opening pressure",
     "áp suất bắt đầu xả",
     "xem áp suất mở"),
    ("start-to-leak pressure",
     "the value of increasing inlet static pressure at which the first bubble occurs when a pressure relief valve is tested by means of air under a specified water seal on the outlet",
     "áp suất bắt đầu rò",
     "giá trị áp suất tĩnh đầu vào tăng tại đó xuất hiện bọt đầu tiên khi van xả áp được thử bằng khí qua lớp nước bịt kín quy định tại đầu ra"),
    ("superimposed back pressure",
     "the static pressure existing at the outlet of a pressure relief device at the time the device is required to operate. It is the result of pressure in the discharge system from other sources",
     "áp suất ngược chồng chất",
     "áp suất tĩnh tại đầu ra thiết bị xả áp tại thời điểm thiết bị cần hoạt động, do áp suất trong hệ thống xả từ các nguồn khác gây ra"),
    ("test pressure",
     "see relieving pressure",
     "áp suất thử",
     "xem áp suất xả"),
    ("theoretical relieving capacity",
     "the computed capacity expressed in gravimetric or volumetric units of a theoretically perfect nozzle having a minimum cross-sectional flow area equal to the actual discharge area of a pressure relief valve or relief area of a non-reclosing pressure relief device",
     "lưu lượng xả lý thuyết",
     "lưu lượng tính toán (theo đơn vị khối lượng hoặc thể tích) của một miệng phun lý tưởng có tiết diện dòng chảy nhỏ nhất bằng diện tích xả thực của van xả áp hoặc diện tích xả của thiết bị không tự đóng lại"),
    ("vapor-tight pressure",
     "see resealing pressure",
     "áp suất kín hơi",
     "xem áp suất tái kín"),
    ("variable back pressure",
     "a superimposed back pressure that will vary with time",
     "áp suất ngược biến thiên",
     "áp suất ngược chồng chất thay đổi theo thời gian"),
    ("warn",
     "see simmer",
     "tiếng rít báo hiệu (warn)",
     "xem simmer"),
]

_CEN = [
    ("accumulation",
     "a pressure increase over the set pressure of a pressure relief valve, usually expressed as a percentage of the set pressure",
     "sự tích lũy áp (accumulation)",
     "sự tăng áp so với áp suất thiết lập của van xả áp, thường biểu thị bằng % áp suất thiết lập"),
    ("pilot-operated safety valve",
     "safety valve, the operation of which is initiated and controlled by the fluid discharged from a pilot valve which is itself a direct-loaded safety valve",
     "van an toàn vận hành bằng pilot",
     "van an toàn mà sự vận hành được khởi động và điều khiển bởi chất lưu xả từ một van pilot, chính van pilot là van an toàn tải trực tiếp"),
    ("supplementary loaded safety valve",
     "safety valve which has, until the pressure at the inlet to the safety valve reaches the set pressure, an additional force which increases the sealing force. This additional force (supplementary load), which may be provided by means of an extraneous power source, is reliably released when the pressure at the inlet of the safety valve reaches the set pressure",
     "van an toàn có tải bổ sung",
     "van an toàn có lực bổ sung làm tăng lực kín cho đến khi áp suất đầu vào đạt áp suất thiết lập; lực bổ sung này (tải phụ) có thể từ nguồn năng lượng ngoài và được giải phóng tin cậy khi áp suất đầu vào đạt áp suất thiết lập"),
    ("overpressure",
     "a pressure increase over the set pressure of a pressure relief valve, usually expressed as a percentage of set pressure",
     "quá áp",
     "sự tăng áp so với áp suất thiết lập của van xả áp, thường biểu thị bằng % áp suất thiết lập"),
    ("popping pressure",
     "the value of increasing inlet static pressure at which the disc moves in the opening direction at a faster rate as compared with corresponding movement at higher or lower pressures. It applies only to safety or safety relief valves on compressible-fluid service",
     "áp suất bật (popping)",
     "giá trị áp suất tĩnh đầu vào tăng tại đó đĩa chuyển theo hướng mở nhanh hơn so với chuyển động tương ứng ở áp suất cao hơn hoặc thấp hơn; chỉ áp dụng cho van an toàn hoặc van an toàn xả trên chất lưu nén được"),
    ("primary pressure",
     "the pressure at the inlet in a safety, safety relief, or relief valve",
     "áp suất sơ cấp",
     "áp suất tại đầu vào của van an toàn, van an toàn xả hoặc van xả"),
    ("rated relieving capacity",
     "that portion of the measured relieving capacity permitted by the applicable code or regulation to be used as a basis for the application of a pressure relief device",
     "lưu lượng xả định mức",
     "phần lưu lượng xả đo được được quy code hoặc quy định áp dụng cho phép dùng làm cơ sở lựa chọn thiết bị xả áp"),
    ("reference conditions",
     "those conditions of a test medium which are specified by either an applicable standard or an agreement between the parties to the test, which may be used for uniform reporting of measured flow test results",
     "điều kiện tham chiếu",
     "các điều kiện của môi chất thử được quy định bởi tiêu chuẩn áp dụng hoặc thỏa thuận giữa các bên, dùng để báo cáo thống nhất kết quả thử dòng chảy đo được"),
    ("relieving pressure",
     "set pressure plus overpressure",
     "áp suất xả",
     "áp suất thiết lập cộng quá áp"),
    ("resealing pressure",
     "the value of decreasing inlet static pressure at which no further leakage is detected after closing. The method of detection may be a specified water seal on the outlet or other means appropriate for this application",
     "áp suất tái kín",
     "giá trị áp suất tĩnh đầu vào giảm tại đó không còn phát hiện rò rỉ sau khi đóng; phương pháp phát hiện có thể là lớp nước bịt kín quy định tại đầu ra hoặc cách khác phù hợp"),
    ("reseating pressure",
     "see closing pressure",
     "áp suất tái ngồi (đóng lại)",
     "xem áp suất đóng"),
    ("seal-off pressure",
     "see resealing pressure",
     "áp suất chặn kín",
     "xem áp suất tái kín"),
    ("secondary pressure",
     "the pressure existing in the passage between the actual discharge area and the valve outlet in a safety, safety relief, or relief valve",
     "áp suất thứ cấp",
     "áp suất trong lối đi giữa diện tích xả thực và đầu ra van của van an toàn, van an toàn xả hoặc van xả"),
    ("set pressure",
     "the value of increasing inlet static pressure at which a pressure relief valve displays one of the operational characteristics as defined under opening pressure, popping pressure, or start-to-leak pressure",
     "áp suất thiết lập",
     "giá trị áp suất tĩnh đầu vào tăng tại đó van xả áp thể hiện một trong các đặc tính vận hành như định nghĩa tại áp suất mở, áp suất bật hoặc áp suất bắt đầu rò"),
    ("simmer",
     "the audible or visible escape of fluid between the seat and disc at an inlet static pressure below the popping pressure and at no measurable capacity. It applies to safety or safety relief valves on compressible-fluid service",
     "simmer (tiếng sôi)",
     "sự thoát chất lưu có thể nghe hoặc nhìn thấy giữa đệm kín và đĩa ở áp suất tĩnh đầu vào dưới áp suất bật và không có lưu lượng đo được; áp dụng cho van an toàn hoặc van an toàn xả trên chất lưu nén được"),
    ("specified burst pressure (of a rupture disc device)",
     "the value of increasing inlet static pressure, at a specified temperature, at which a rupture disc is designed to function",
     "áp suất vỡ quy định (của thiết bị đĩa vỡ)",
     "giá trị áp suất tĩnh đầu vào tăng, tại nhiệt độ quy định, mà tại đó đĩa vỡ được thiết kế để hoạt động"),
]


def _render_terms(rows, lang):
    out = []
    for en_term, en_def, vi_term, vi_def in rows:
        if lang == "vi":
            out.append("<b>%s</b> — %s" % (vi_term, vi_def))
        else:
            out.append("<b>%s</b> — %s" % (en_term, en_def))
    return ul(out)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> "
                "pressure relief valve — van xả áp lực · safety valve — van an toàn · "
                "huddling chamber — buồng điều khiển · back pressure — áp suất ngược · "
                "set pressure — áp suất thiết lập · blowdown — độ đóng lại · "
                "relieving capacity — lưu lượng xả.")
    return ("<b>Key terms in this chapter.</b> "
            "pressure relief valve · safety valve · huddling chamber · back pressure · "
            "set pressure · blowdown · relieving capacity.")


def body_vi():
    b = []
    b.append(p("Chương này chứa các thuật ngữ phổ biến và được chuẩn hóa liên quan đến "
               "thiết bị xả áp lực, được soạn theo và chuyển ngữ từ ANSI/ASME Performance "
               "Test Code PTC-25.3-1988, Phụ lục I cùng các tập quán được chấp nhận khác."))
    b.append(h2("A. Tổng quan", "A. General"))
    b.append(h3("Thiết bị xả áp lực", "Pressure Relief Devices"))
    b.append(p("Thiết bị xả áp lực là thiết bị được thiết kế để ngăn áp suất chất lưu bên "
               "trong tăng vượt quá áp suất cực đại định trước trong bình chịu áp lực khi gặp "
               "điều kiện khẩn cấp hoặc bất thường."))
    b.append(h3("Thử nghiệm lưu lượng", "Flow Capacity Testing"))
    b.append(p("Thử nghiệm thiết bị xả áp lực để xác định các đặc tính vận hành, bao gồm cả "
               "lưu lượng xả đo được."))
    b.append(h3("Thử nghiệm tại chỗ", "In-Service Testing"))
    b.append(p("Thử nghiệm thiết bị xả áp lực trong khi đang bảo vệ hệ thống mà nó lắp trên "
               "đó, nhằm xác định một phần hoặc toàn bộ đặc tính vận hành bằng áp suất hệ "
               "thống đơn thuần hoặc phối hợp với cơ cấu nâng phụ hoặc nguồn áp suất khác."))
    b.append(h3("Thử nghiệm trên băng", "Bench Testing"))
    b.append(p("Thử nghiệm thiết bị xả áp lực trên hệ thống có áp suất để xác định áp suất "
               "mở và độ kín đệm."))
    b.append(h2("B. Các loại thiết bị", "B. Types of Devices"))
    b.append(h3("Thiết bị xả áp lực có thể tự đóng lại", "Reclosing Pressure Relief Devices"))
    b.append(h4("Van xả áp lực", "Pressure Relief Valve"))
    b.append(p("(a) Van xả áp lực là thiết bị xả áp bằng lò xo, được thiết kế để mở xả áp "
               "dư và tự đóng lại, ngăn dòng chảy tiếp theo sau khi điều kiện bình thường "
               "được khôi phục. Nó có đặc tính mở kiểu bật (pop) nhanh hoặc mở tỷ lệ thuận "
               "với sự tăng áp suất trên áp suất mở. Tùy thiết kế, chỉnh định hoặc ứng dụng mà "
               "nó dùng cho chất lưu nén hoặc không nén."))
    b.append(h4("Van an toàn", "Safety Valve"))
    b.append(p("(b) Van an toàn là van xả áp lực vận hành bằng áp suất tĩnh đầu vào, có đặc "
               "tính mở bật nhanh. (Thường dùng cho hơi và khí.)"))
    b.append(p("<b>Van an toàn nâng thấp</b> — van an toàn có đĩa tự nhấc sao cho diện tích "
               "xả thực được xác định bởi vị trí đĩa."))
    b.append(p("<b>Van an toàn nâng toàn phần</b> — van an toàn có đĩa tự nhấc sao cho diện "
               "tích xả thực không phụ thuộc vào vị trí đĩa."))
    b.append(h4("Van xả", "Relief Valve"))
    b.append(p("(c) Van xả là thiết bị xả áp vận hành bằng áp suất tĩnh đầu vào, có hành "
               "trình nâng dần tỷ lệ thuận với sự tăng áp suất trên áp suất mở. Nó có thể "
               "được trang bị vỏ lò xo kín phù hợp cho hệ thống xả kín, chủ yếu dùng cho "
               "chất lỏng."))
    b.append(h4("Van an toàn xả", "Safety Relief Valve"))
    b.append(p("(d) Van an toàn xả là van xả áp lực có đặc tính mở bật nhanh hoặc mở tỷ lệ "
               "thuận với sự tăng áp suất trên áp suất mở, tùy ứng dụng, và có thể dùng cho "
               "chất lỏng hoặc chất lưu nén."))
    b.append(p("<b>Van an toàn xả kiểu thông thường</b> — van an toàn xả có vỏ lò xo thông "
               "ra phía xả của van; đặc tính vận hành (áp suất mở, áp suất đóng, lưu lượng "
               "xả) bị ảnh hưởng trực tiếp bởi sự thay đổi áp suất ngược trên van."))
    b.append(p("<b>Van an toàn xả cân bằng</b> — van an toàn xả có cơ cấu giảm thiểu ảnh "
               "hưởng của áp suất ngược lên đặc tính vận hành (áp suất mở, áp suất đóng, "
               "lưu lượng xả)."))
    b.append(h4("Van xả áp lực vận hành bằng pilot", "Pilot-Operated Pressure Relief Valve"))
    b.append(p("(e) Van xả áp lực vận hành bằng pilot là van xả áp lực mà trong đó thiết bị "
               "xả chính được kết hợp và điều khiển bởi một van xả áp phụ tự vận hành."))
    b.append(h4("Van xả áp lực vận hành bằng nguồn ngoài", "Power-Actuated Pressure Relief Valve"))
    b.append(p("(f) Van xả áp lực vận hành bằng nguồn ngoài là van xả áp lực mà thiết bị xả "
               "chính được kết hợp và điều khiển bởi một cơ cấu cần nguồn năng lượng bên "
               "ngoài."))
    b.append(h4("Van xả áp lực vận hành bằng nhiệt độ", "Temperature-Actuated Pressure Relief Valve"))
    b.append(p("(g) Van xả áp lực vận hành bằng nhiệt độ là van xả áp lực có thể vận hành "
               "bằng nhiệt độ ngoài hoặc trong, hoặc bằng áp suất phía đầu vào."))
    b.append(h4("Van xả chân không", "Vacuum Relief Valve"))
    b.append(p("(h) Van xả chân không là thiết bị xả áp được thiết kế để nạp chất lưu nhằm "
               "ngăn chân không bên trong quá mức; nó tự đóng lại và ngăn dòng chảy tiếp "
               "theo sau khi điều kiện bình thường được khôi phục."))
    b.append(h3("Thiết bị xả áp lực không tự đóng lại", "Non-Reclosing Pressure Relief Devices"))
    b.append(p("Thiết bị xả áp lực không tự đóng lại là thiết bị xả áp được thiết kế để luôn "
               "mở sau khi hoạt động. Có thể bố trí cơ cấu đặt lại bằng tay."))
    b.append(p("<b>Thiết bị đĩa vỡ</b> — thiết bị xả áp không tự đóng lại vận hành bằng áp "
               "suất tĩnh đầu vào, hoạt động nhờ sự vỡ của một đĩa chịu áp."))
    b.append(p("<b>Thiết bị chốt phá</b> — thiết bị xả áp không tự đóng lại vận hành bằng áp "
               "suất tĩnh đầu vào, hoạt động nhờ gãy một đoạn chịu tải của chốt đang đỡ một "
               "chi tiết chứa áp."))
    b.append(h2("C. Các chi tiết của thiết bị xả áp lực", "C. Parts of Pressure Relief Devices"))
    b.append(_render_terms(_PARTS, "vi"))
    b.append(h2("D. Đặc tính kích thước van xả áp lực", "D. Pressure Relief Valve Dimensional Characteristics"))
    b.append(_render_terms(_DIM, "vi"))
    b.append(h2("E. Đặc tính vận hành thiết bị xả áp lực", "E. Operational Characteristics of Pressure Relief Devices"))
    b.append(_render_terms(_OPS, "vi"))
    b.append(h2("Định nghĩa CEN", "CEN Definitions"))
    b.append(_render_terms(_CEN, "vi"))
    b.append(note("Tóm tắt: chương liệt kê thuật ngữ chuẩn hóa (ANSI/ASME PTC-25.3 và CEN) "
                  "cho thiết bị xả áp — phân loại thiết bị, chi tiết, kích thước và đặc tính "
                  "vận hành — làm nền tảng từ vựng cho các chương định cỡ tiếp theo."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
               "© 1997 Crosby Valve Inc.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(p("This chapter contains common and standardized terminology related to "
               "pressure relief devices and is in accordance with, and adapted from, "
               "ANSI/ASME Performance Test Code PTC-25.3-1988, Appendix I and other "
               "accepted practices."))
    b.append(h2("A. General", "A. Tổng quan"))
    b.append(h3("Pressure Relief Devices", "Thiết bị xả áp lực"))
    b.append(p("A pressure relief device is a device designed to prevent internal fluid "
               "pressure from rising above a predetermined maximum pressure in a pressure "
               "vessel exposed to emergency or abnormal conditions."))
    b.append(h3("Flow Capacity Testing", "Thử nghiệm lưu lượng"))
    b.append(p("Testing of a pressure relief device to determine its operating "
               "characteristics including measured relieving capacity."))
    b.append(h3("In-Service Testing", "Thử nghiệm tại chỗ"))
    b.append(p("Testing of a pressure relief device while protecting the system on which it "
               "is installed to determine some or all of its operating characteristics using "
               "system pressure solely or in conjunction with an auxiliary lift device or "
               "other pressure source."))
    b.append(h3("Bench Testing", "Thử nghiệm trên băng"))
    b.append(p("Testing of a pressure relief device on a pressurized system to determine set "
               "pressure and seat tightness."))
    b.append(h2("B. Types of Devices", "B. Các loại thiết bị"))
    b.append(h3("Reclosing Pressure Relief Devices", "Thiết bị xả áp lực có thể tự đóng lại"))
    b.append(h4("Pressure Relief Valve", "Van xả áp lực"))
    b.append(p("(a) A pressure relief valve is a spring loaded pressure relief device which "
               "is designed to open to relieve excess pressure and to reclose and prevent the "
               "further flow of fluid after normal conditions have been restored. It is "
               "characterized by rapid opening pop action or by opening generally proportional "
               "to the increase in pressure over the opening pressure. It may be used for "
               "either compressible or incompressible fluids, depending on design, adjustment, "
               "or application."))
    b.append(h4("Safety Valve", "Van an toàn"))
    b.append(p("(b) A safety valve is a pressure relief valve actuated by inlet static "
               "pressure and characterized by rapid opening or pop action. (It is normally "
               "used for steam and air services.)"))
    b.append(p("<b>Low-Lift Safety Valve.</b> A low-lift safety valve is a safety valve in "
               "which the disc lifts automatically such that the actual discharge area is "
               "determined by the position of the disc."))
    b.append(p("<b>Full-Lift Safety Valve.</b> A full-lift safety valve is a safety valve in "
               "which the disc lifts automatically such that the actual discharge area is not "
               "determined by the position of the disc."))
    b.append(h4("Relief Valve", "Van xả"))
    b.append(p("(c) A relief valve is a pressure relief device actuated by inlet static "
               "pressure having a gradual lift generally proportional to the increase in "
               "pressure over opening pressure. It may be provided with an enclosed spring "
               "housing suitable for closed discharge system application and is primarily "
               "used for liquid service."))
    b.append(h4("Safety Relief Valve", "Van an toàn xả"))
    b.append(p("(d) A safety relief valve is a pressure relief valve characterized by rapid "
               "opening or pop action, or by opening in proportion to the increase in pressure "
               "over the opening pressure, depending on the application and may be used either "
               "for liquid or compressible fluid."))
    b.append(p("<b>Conventional Safety Relief Valve.</b> A conventional safety relief valve "
               "is a pressure relief valve which has its spring housing vented to the "
               "discharge side of the valve. The operational characteristics (opening "
               "pressure, closing pressure, and relieving capacity) are directly affected by "
               "changes of the back pressure on the valve."))
    b.append(p("<b>Balanced Safety Relief Valve.</b> A balanced safety relief valve is a "
               "pressure relief valve which incorporates means of minimizing the effect of "
               "back pressure on the operational characteristics (opening pressure, closing "
               "pressure, and relieving capacity)."))
    b.append(h4("Pilot-Operated Pressure Relief Valve", "Van xả áp lực vận hành bằng pilot"))
    b.append(p("(e) A pilot-operated pressure relief valve is a pressure relief valve in "
               "which the major relieving device is combined with and is controlled by a "
               "self-actuated auxiliary pressure relief valve."))
    b.append(h4("Power-Actuated Pressure Relief Valve", "Van xả áp lực vận hành bằng nguồn ngoài"))
    b.append(p("(f) A power-actuated pressure relief valve is a pressure relief valve in "
               "which the major relieving device is combined with and controlled by a device "
               "requiring an external source of energy."))
    b.append(h4("Temperature-Actuated Pressure Relief Valve", "Van xả áp lực vận hành bằng nhiệt độ"))
    b.append(p("(g) A temperature-actuated pressure relief valve is a pressure relief valve "
               "which may be actuated by external or internal temperature or by pressure on "
               "the inlet side."))
    b.append(h4("Vacuum Relief Valve", "Van xả chân không"))
    b.append(p("(h) A vacuum relief valve is a pressure relief device designed to admit fluid "
               "to prevent an excessive internal vacuum; it is designed to reclose and prevent "
               "further flow of fluid after normal conditions have been restored."))
    b.append(h3("Non-Reclosing Pressure Relief Devices", "Thiết bị xả áp lực không tự đóng lại"))
    b.append(p("A non-reclosing pressure relief device is a pressure relief device designed to "
               "remain open after operation. A manual resetting means may be provided."))
    b.append(p("<b>Rupture Disc Device.</b> A rupture disc device is a non-reclosing pressure "
               "relief device actuated by inlet static pressure and designed to function by "
               "the bursting of a pressure containing disc."))
    b.append(p("<b>Breaking Pin Device.</b> A breaking pin device is a non-reclosing pressure "
               "relief device actuated by inlet static pressure and designed to function by "
               "the breakage of a load-carrying section of a pin which supports a pressure "
               "containing member."))
    b.append(h2("C. Parts of Pressure Relief Devices", "C. Các chi tiết của thiết bị xả áp lực"))
    b.append(_render_terms(_PARTS, "en"))
    b.append(h2("D. Pressure Relief Valve Dimensional Characteristics", "D. Đặc tính kích thước van xả áp lực"))
    b.append(_render_terms(_DIM, "en"))
    b.append(h2("E. Operational Characteristics of Pressure Relief Devices", "E. Đặc tính vận hành thiết bị xả áp lực"))
    b.append(_render_terms(_OPS, "en"))
    b.append(h2("CEN Definitions", "Định nghĩa CEN"))
    b.append(_render_terms(_CEN, "en"))
    b.append(note("Summary: this chapter lists the standardized terminology (ANSI/ASME "
                  "PTC-25.3 and CEN) for pressure relief — device classification, parts, "
                  "dimensions and operational characteristics — establishing the vocabulary "
                  "for the sizing chapters that follow."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content © "
               "1997 Crosby Valve Inc.</i>"))
    return "".join(b)
