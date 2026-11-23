# -*- coding: utf-8 -*-
"""Book 7c, Chapter 5 - Control Valve Sizing (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 98-149.
This is a reference chapter: control valve dimensions, seat leakage classes,
flow characteristics, the ISA/IEC sizing equations and sample problems,
actuator sizing, cavitation and flashing, noise prediction and control,
packing and body-material selection, pressure-temperature ratings and
non-destructive examination. Eighteen numbered figures are redrawn as vector
schematics in `cvh6fig5.py` and placed at the source caption points.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import eq, fig, h2, h3, h4, lead, note, ol, p, table, ul
import cvh6fig5 as F5

PAGES_SRC = 52          # source printed pp. 98-149 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Control Valve Sizing"
TITLE_VI = "Định cỡ van điều khiển"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> control valve sizing — định cỡ van điều khiển · "
            "service conditions — điều kiện làm việc · face-to-face dimension — kích thước mặt đến "
            "mặt · seat leakage class — cấp độ rò rỉ chỗ ngồi · flow characteristic — đặc tính "
            "dòng chảy · inherent / installed characteristic — đặc tính vốn có / khi lắp đặt · "
            "quick-opening — mở nhanh · linear — tuyến tính · equal-percentage — phần trăm bằng · "
            "Cv (flow coefficient) — hệ số lưu lượng · FL (liquid pressure recovery factor) — hệ số "
            "phục hồi áp suất chất lỏng · Fp (piping geometry factor) — hệ số hình học đường ống · "
            "xT (pressure drop ratio factor at choked flow) — hệ số tỷ lệ sụt áp ở chảy nghẽn · "
            "Y (expansion factor) — hệ số giãn nở · choked flow — dòng chảy nghẽn · "
            "cavitation — xâm thực · flashing — bay hơi · vena contracta — tiết diện co hẹp nhất · "
            "ΔPsizing — sụt áp dùng để định cỡ · ΔPchoked — sụt áp gây nghẽn dòng · "
            "acoustic efficiency — hiệu suất âm thanh · insertion loss — suy hao chèn · "
            "packing — đệm kín thân van · non-destructive examination — kiểm tra không phá hủy")
    return (
        "<b>Key terms in this chapter.</b> control valve sizing · service conditions · "
        "face-to-face dimension · seat leakage class · flow characteristic · inherent / installed "
        "characteristic · quick-opening · linear · equal-percentage · Cv (flow coefficient) · "
        "FL (liquid pressure recovery factor) · Fp (piping geometry factor) · xT (pressure drop "
        "ratio factor at choked flow) · Y (expansion factor) · choked flow · cavitation · "
        "flashing · vena contracta · ΔPsizing · ΔPchoked · acoustic efficiency · insertion "
        "loss · packing · non-destructive examination")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Bản PDF in các phương trình định cỡ dưới dạng hình ảnh, nên "
            "lớp văn bản chỉ để lại các cụm từ như «And», «Now, calculate Fp:», «Then, determine…» rồi "
            "để trống; ở đây các phương trình được biểu diễn tương đương bằng ký hiệu (q, N1, Cv, FL, "
            "Fp, xT, Y, ΔP, P1, P2, Pv, Pc, ρ1…), không phải công thức được số hóa lại từ bản in. "
            "(2) Giữ nguyên lỗi OCR «step-step» (thay cho step-by-step, mục 5.8) và «postioning»; "
            "bản Việt dịch đúng ý. (3) Nhiều bảng kích thước bị gãy cột: tiêu đề nêu năm cấp áp lực "
            "nhưng mỗi dòng chỉ ba cặp mm/in; các giá trị được giữ nguyên như trong lớp văn bản và "
            "được ghi chú rõ trong chú thích bảng. (4) Một số ô bị lệch rõ rệt (ví dụ 475 tại DN 350, "
            "bảng 5.1.1 phần 2; 321.8 bar tại 250°C, bảng 5.20.2; WCC 800°F = 80/410/825/1.235/2.055) "
            "được giữ nguyên theo nguồn. (5) Chú thích Hình 5.1 ghi «Feedback Control Loop» dù nội dung "
            "vẽ là đường cong đặc tính dòng chảy; giữ nguyên chú thích gốc. (6) Ví dụ chất lỏng propane "
            "kết thúc ở Cv = 121,7 và van NPS 4 mở khoảng 75% hành trình (con số 66% thuộc ví dụ hơi "
            "nước ở mục 5.9.5); giữ nguyên theo bản in. (7) Hình 5.8 và 5.9 là ảnh chụp trong bản in; "
            "ở đây vẽ lại dạng sơ đồ vector minh họa, không phải ảnh gốc.")
    return (
        "<b>Source notes.</b> (1) The printed sizing equations are images, so the text layer keeps only "
        "phrases such as <i>And</i>, <i>Now, calculate Fp:</i> and <i>Then, determine…</i> followed by "
        "a blank. The equations here are symbolic equivalents using the symbols the source names "
        "(q, N1, Cv, FL, Fp, xT, Y, ΔP, P1, P2, Pv, Pc, ρ1…), not re-typeset copies of the printed "
        "formulae. (2) The OCR typos <i>step-step</i> (for step-by-step, 5.8) and <i>postioning</i> are "
        "retained in English and explained here; the Vietnamese text corrects them. (3) Several "
        "dimension tables are column-broken: a heading names five pressure classes while each row "
        "exposes only three mm/in pairs; the stated values are kept verbatim and the limitation is "
        "recorded in the table captions. (4) Obvious outliers (e.g. 475 at DN 350 in table 5.1.1 part "
        "2; 321.8 bar at 250°C in table 5.20.2; WCC 800°F = 80/410/825/1,235/2,055) are kept as "
        "printed. (5) The Figure 5.1 caption reads <i>Feedback Control Loop</i> although the graphic "
        "is a flow-characteristic chart; the original caption is preserved. (6) The liquid propane "
        "sample ends at Cv = 121.7 with an NPS 4 valve about 75% open (the 66% figure belongs to the "
        "steam example in 5.9.5); kept as printed. (7) Figures 5.8 and 5.9 are photographs in print; "
        "they are redrawn here as illustrative vector damage schematics, not the original images.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def B(v, e):
        b.append(ul(v if vi else e))

    def O(v, e, start=1):
        b.append(ol(v if vi else e, start))

    def FIG(n, fn):
        b.append(fig(n, fn, lang))

    def N(v, e):
        b.append(note(v if vi else e))

    def EQ(body, num="", v="", e=""):
        b.append(eq(body, num))
        if v or e:
            P(v, e)

    def TBL(header, rows, cap=""):
        b.append(table(header, rows, caption=cap))

    # ------------------------------------------------------------ lead
    b.append(lead(
        "Chương này là tài liệu tham khảo về định cỡ van điều khiển: kích thước thân van, phân loại rò "
        "rỉ chỗ ngồi, đặc tính dòng chảy, phương trình định cỡ ISA/IEC và các bài toán mẫu, định cỡ "
        "cơ cấu chấp hành, xâm thực và bay hơi, dự báo và kiểm soát tiếng ồn, lựa chọn đệm kín, vật "
        "liệu thân van, xếp hạng áp suất-nhiệt độ và kiểm tra không phá hủy."
        if vi else
        "This chapter is a reference on control valve sizing: valve body dimensions, seat leakage "
        "classifications, flow characteristics, the ISA/IEC sizing equations and sample problems, "
        "actuator sizing, cavitation and flashing, noise prediction and control, packing selection, "
        "body materials, pressure-temperature ratings and non-destructive examination."))
    N(note_terms("vi"), note_terms("en"))

    P("Van điều khiển xử lý mọi loại chất lỏng ở nhiệt độ từ vùng đông lạnh đến trên 538°C (1000°F). "
      "Việc lựa chọn cụm thân van đòi hỏi cân nhắc đặc biệt để có sự kết hợp tốt nhất giữa kiểu thân, "
      "vật liệu và cấu trúc trim cho dịch vụ đã định. Yêu cầu năng lực và dải áp suất vận hành của hệ "
      "thống cũng phải được tính đến để bảo đảm vận hành thỏa mãn mà không tốn kém không cần thiết.",
      "Control valves handle all kinds of fluids at temperatures from the cryogenic range to well "
      "over 538°C (1000°F). Selection of a control valve body assembly requires particular "
      "consideration to provide the best available combination of valve body style, material, and "
      "trim construction design for the intended service. Capacity requirements and system "
      "operating pressure ranges also must be considered in selecting a control valve to ensure "
      "satisfactory operation without undue initial expense.")
    P("Nhà sản xuất và đại diện uy tín sẵn sàng giúp chọn van phù hợp nhất với điều kiện hiện có. Vì "
      "thường có nhiều lựa chọn đúng cho một ứng dụng, điều quan trọng là phải cung cấp đầy đủ thông "
      "tin sau cho mỗi bộ điều kiện được coi là quan trọng:",
      "Reputable control valve manufacturers and their representatives are dedicated to helping "
      "select the control valve most appropriate for the existing service conditions. Because there "
      "are frequently several possible correct choices for an application, it is important that all "
      "the following information be provided for any set of conditions deemed important:")
    B(["Loại chất lỏng cần điều khiển;",
       "Nhiệt độ của chất lỏng;",
       "Độ nhớt của chất lỏng;",
       "Nồng độ của mọi thành phần, kể cả tạp chất dấu vết;",
       "Điều kiện quá trình khi khởi động, vận hành bình thường và dừng máy;",
       "Vệ sinh hóa học định kỳ;",
       "Trọng lực riêng hoặc tỷ trọng của chất lỏng;",
       "Lưu lượng chất lỏng;",
       "Áp suất đầu vào tại van;",
       "Áp suất đầu ra hoặc sụt áp;",
       "Sụt áp khi đóng;",
       "Mức tiếng ồn tối đa cho phép, nếu có liên quan, và điểm đo tham chiếu;",
       "Mức quá nhiệt hoặc sự hiện diện của bay hơi, nếu biết;",
       "Kích thước và cấp ống đầu vào/đầu ra;",
       "Thông tin gắn nhãn đặc biệt yêu cầu;",
       "Vật liệu thân đúc (ASTM A216 WCC, ASTM A217 WC9, ASTM A351 CF8M…);",
       "Đầu nối và cấp áp suất của van (ren, bích Class 600 RF, bích Class 1500 RTJ…);",
       "Tác động mong muốn khi mất khí (van mở, đóng hoặc giữ vị trí điều khiển cuối);",
       "Nguồn khí dụng cụ sẵn có;",
       "Tín hiệu dụng cụ (3 đến 15 psig, 4 đến 20 mA, HART…)."],
      ["Type of fluid to be controlled;",
       "Temperature of fluid;",
       "Viscosity of fluid;",
       "Concentrations of all constituents including trace impurities;",
       "Process conditions during startup, normal operations, and shutdowns;",
       "Chemical cleaning that may occur periodically;",
       "Specific gravity or density of fluid;",
       "Fluid flow rate;",
       "Inlet pressure at valve;",
       "Outlet pressure or pressure drop;",
       "Pressure drop at shutoff;",
       "Maximum permissible noise level, if pertinent, and the measurement reference point;",
       "Degrees of superheat or existence of flashing, if known;",
       "Inlet and outlet pipeline size and schedule;",
       "Special tagging information required;",
       "Cast body material (ASTM A216 grade WCC, ASTM A217 grade WC9, ASTM A351 CF8M, etc.);",
       "End connections and valve rating (screwed, Class 600 RF flanged, Class 1500 RTJ flanges, etc.);",
       "Action desired on air failure (valve to open, close, or retain last controlled position);",
       "Instrument air supply available;",
       "Instrument signal (3 to 15 psig, 4 to 20 mA, HART, etc.)."])
    P("Ngoài ra, thông tin sau đây cần sự thỏa thuận giữa người sử dụng và nhà sản xuất tùy theo tập "
      "quán mua sắm và kỹ thuật được áp dụng: số loại van, cỡ van, cấu trúc thân van, cách dẫn hướng "
      "nút van, tác động nút van, cỡ cổng, vật liệu trim, chiều dòng chảy, cỡ cơ cấu chấp hành, kiểu "
      "nắp, vật liệu đệm kín và phụ kiện cần thiết.",
      "In addition, the following information will require the agreement of the user and the "
      "manufacturer depending on the purchasing and engineering practices being followed: valve type "
      "number, valve size, valve body construction, valve plug guiding, valve plug action, port size, "
      "valve trim materials required, flow action, actuator size required, bonnet style, packing "
      "material, and accessories required.")
    P("Một số lựa chọn này đã được thảo luận ở các chương trước; những lựa chọn khác sẽ được khảo sát "
      "trong chương này và các chương sau.",
      "Some of these options have been discussed in previous chapters of this book, and others will "
      "be explored in this and following chapters.")

    H("Quy trình lựa chọn van / Valve selection process", "")
    O(["Xác định điều kiện làm việc: P1, ΔP, Q, T1, tính chất chất lỏng, tiếng ồn cho phép… Chọn cấp "
       "áp suất ANSI phù hợp cho thân và trim.",
       "Tính sơ bộ Cv cần thiết. Kiểm tra mức tiếng ồn và xâm thực.",
       "Chọn kiểu trim: trim tiêu chuẩn nếu không có dấu hiệu ồn hoặc xâm thực; trim giảm ồn nếu ồn "
       "khí động học cao; trim giảm xâm thực nếu ồn chất lỏng cao hoặc có xâm thực.",
       "Chọn thân van và cỡ trim có Cv yêu cầu; ghi chú hành trình, nhóm trim và tùy chọn đóng.",
       "Chọn vật liệu trim cho ứng dụng và bảo đảm trim có sẵn trong nhóm trim của cỡ van đã chọn.",
       "Xem xét các tùy chọn về độ kín đóng, đệm kín thân van và các tùy chọn khác."],
      ["Determine service conditions: P1, ΔP, Q, T1, fluid properties, allowable noise, etc. Select "
       "the appropriate ANSI pressure class for valve body and trim.",
       "Calculate preliminary Cv required. Check noise and cavitation levels.",
       "Select trim type: standard trim if no noise or cavitation indication; noise reduction trim if "
       "aerodynamic noise is high; cavitation reduction trim if liquid noise is high and/or cavitation "
       "is indicated.",
       "Select valve body and trim size with required Cv. Note travel, trim group, and shutoff options.",
       "Select trim materials for the application; make sure the selected trim is available in the "
       "trim group for the valve size selected.",
       "Consider options on shutoff, stem packing, etc."])

    # ------------------------------------------------------------ 5.1
    H("5.1 Kích thước van điều khiển", "5.1 Control Valve Dimensions")
    P("Các bảng dưới đây cho số liệu kích thước mặt đến mặt và mặt đến tâm theo tiêu chuẩn ANSI/ISA "
      "và MSS cho thân van dạng cầu, góc, quay và bướm.",
      "The tables below give face-to-face and face-to-centerline dimensions to ANSI/ISA and MSS "
      "standards for globe, angle, rotary and butterfly valve bodies.")

    H("5.1.1 Kích thước mặt đến mặt của van điều khiển dạng cầu có bích",
      "5.1.1 Face-to-Face Dimensions for Flanged, Globe-Style Control Valves", h3)
    P("Cấp 125, 150, 250, 300 và 600 (kích thước theo ANSI/ISA-75.08.01).",
      "Classes 125, 150, 250, 300, and 600 (dimensions in accordance with ANSI/ISA-75.08.01).")
    TBL(["DN", "NPS", "mm", "in", "mm", "in", "mm", "in"],
        [("15", "1/2", "184", "7.25", "197", "7.75", "190", "7.50"),
         ("20", "3/4", "184", "7.25", "197", "7.75", "194", "7.62"),
         ("25", "1", "184", "7.25", "197", "7.75", "197", "7.75"),
         ("40", "1-1/2", "222", "8.75", "235", "9.25", "235", "9.25"),
         ("50", "2", "254", "10.00", "267", "10.50", "267", "10.50"),
         ("65", "2-1/2", "276", "10.88", "289", "11.38", "292", "11.50"),
         ("80", "3", "298", "11.75", "311", "12.25", "318", "12.50"),
         ("100", "4", "352", "13.88", "365", "14.38", "368", "14.50"),
         ("150", "6", "451", "17.75", "464", "18.25", "473", "18.62"),
         ("200", "8", "543", "21.38", "556", "21.88", "568", "22.38"),
         ("250", "10", "673", "26.50", "686", "27.00", "708", "27.88"),
         ("300", "12", "737", "29.00", "749", "29.50", "775", "30.50"),
         ("350", "14", "889", "35.00", "902", "35.50", "927", "36.50"),
         ("400", "16", "1016", "40.00", "1029", "40.50", "1057", "41.62")],
        "Class 125 FF (CI) / Class 150 RF (STL) / Class 150 RTJ (STL) / Class 250 RF (CI) / Class 300 RF (STL) — "
        "bản in nêu năm cấp nhưng lớp văn bản chỉ cho ba cặp mm/in / print names five classes but the text "
        "layer exposes only three mm/in pairs per row.")
    P("Viết tắt: FF — mặt phẳng (Flat Face); RF — mặt nổi (Raised Face); RTJ — mối nối kiểu vòng "
      "(Ring-Type Joint); CI — gang đúc (Cast Iron).",
      "Abbreviations used above: FF — Flat Face; RF — Raised Face; RTJ — Ring-Type Joint; CI — Cast Iron.")
    P("Tiếp theo: Class 300 RTJ (STL), Class 600 RF (STL) và Class 600 RTJ (STL).",
      "Continued: Class 300 RTJ (STL), Class 600 RF (STL) and Class 600 RTJ (STL).")
    TBL(["DN", "NPS", "mm", "in", "mm", "in", "mm", "in"],
        [("15", "1/2", "202", "7.94", "203", "8.00", "203", "8.00"),
         ("20", "3/4", "206", "8.12", "206", "8.12", "206", "8.12"),
         ("25", "1", "210", "8.25", "210", "8.25", "210", "8.25"),
         ("40", "1-1/2", "248", "9.75", "251", "9.88", "251", "9.88"),
         ("50", "2", "282", "11.12", "286", "11.25", "284", "11.37"),
         ("65", "2-1/2", "308", "12.12", "311", "12.25", "314", "12.37"),
         ("80", "3", "333", "13.12", "337", "13.25", "340", "13.37"),
         ("100", "4", "384", "15.12", "394", "15.50", "397", "15.62"),
         ("150", "6", "489", "19.24", "508", "20.00", "511", "20.12"),
         ("200", "8", "584", "23.00", "610", "24.00", "613", "24.12"),
         ("250", "10", "724", "28.50", "752", "29.62", "755", "29.74"),
         ("300", "12", "790", "31.12", "819", "32.25", "822", "32.37"),
         ("350", "14", "943", "37.12", "972", "38.25", "475", "38.37"),
         ("400", "16", "1073", "42.24", "1108", "43.62", "1111", "43.74")],
        "Ba cặp số theo thứ tự Class 300 RTJ / Class 600 RF / Class 600 RTJ; giá trị 475 (DN 350) được "
        "giữ nguyên theo bản in / three pairs in the order Class 300 RTJ / Class 600 RF / Class 600 RTJ; "
        "the 475 value (DN 350) is kept as printed.")
    P("Viết tắt: STL — thép (Steel). Cấp 900, 1500 và 2500 theo ANSI/ISA-75.08.06.",
      "Abbreviations: STL — Steel. Classes 900, 1500, and 2500 are in accordance with ANSI/ISA-75.08.06.")
    TBL(["DN", "NPS", "Cl 900 mm ngắn", "Cl 900 mm dài", "Cl 900 in ngắn", "Cl 900 in dài",
         "Cl 1500 mm ngắn", "Cl 1500 mm dài"],
        [("15", "1/2", "273", "292", "10.75", "11.50", "273", "292"),
         ("20", "3/4", "273", "292", "10.75", "11.50", "273", "292"),
         ("25", "1", "273", "292", "10.75", "11.50", "273", "292"),
         ("40", "1-1/2", "311", "333", "12.25", "13.12", "311", "333"),
         ("50", "2", "340", "375", "13.38", "14.75", "340", "375"),
         ("65", "2-1/2", "-", "410", "-", "16.12", "-", "410"),
         ("80", "3", "387", "441", "15.25", "17.38", "406", "460"),
         ("100", "4", "464", "511", "18.25", "20.12", "483", "530"),
         ("150", "6", "600", "714", "21.87", "28.12", "692", "768"),
         ("200", "8", "781", "914", "30.75", "36.00", "838", "972"),
         ("250", "10", "864", "991", "34.00", "39.00", "991", "1067"),
         ("300", "12", "1016", "1130", "40.00", "44.50", "1130", "1219"),
         ("350", "14", "-", "1257", "-", "49.50", "-", "1257"),
         ("400", "16", "-", "1422", "-", "56.00", "-", "1422"),
         ("450", "18", "-", "1727", "-", "68.00", "-", "1727")],
        "Cấp 900 và 1500 — lớp văn bản không chứa cặp inch của Class 1500 / Classes 900 and 1500 — "
        "the Class 1500 inch pair is absent from the text layer.")
    TBL(["DN", "NPS", "Cl 1500 in ngắn", "Cl 1500 in dài", "Cl 2500 mm ngắn", "Cl 2500 mm dài",
         "Cl 2500 in ngắn", "Cl 2500 in dài"],
        [("15", "1/2", "10.75", "11.50", "308", "318", "12.12", "12.50"),
         ("20", "3/4", "10.75", "11.50", "308", "318", "12.12", "12.50"),
         ("25", "1", "10.75", "11.50", "308", "318", "12.12", "12.50"),
         ("40", "1-1/2", "12.25", "13.12", "359", "381", "14.12", "15.00"),
         ("50", "2", "13.38", "14.75", "-", "400", "-", "16.25"),
         ("65", "2-1/2", "-", "16.12", "-", "441", "-", "17.38"),
         ("80", "3", "16.00", "18.12", "498", "660", "19.62", "26.00"),
         ("100", "4", "19.00", "20.87", "575", "737", "22.62", "29.00"),
         ("150", "6", "24.00", "30.25", "819", "864", "32.25", "34.00"),
         ("200", "8", "33.00", "38.25", "-", "1022", "-", "40.25"),
         ("250", "10", "39.00", "42.00", "1270", "1372", "50.00", "54.00"),
         ("300", "12", "44.50", "48.00", "1321", "1575", "52.00", "62.00"),
         ("350", "14", "-", "49.50", "-", "-", "-", "-"),
         ("400", "16", "-", "56.00", "-", "-", "-", "-"),
         ("450", "18", "-", "68.00", "-", "-", "-", "-")],
        "Tiếp theo: Class 1500 (inch) và Class 2500 / Continued: Class 1500 (in) and Class 2500.")

    H("5.1.2 Kích thước mặt đến mặt của van dạng cầu đầu hàn giáp môi",
      "5.1.2 Face-to-Face Dimensions for Butt Weld-End, Globe-Style Valves", h3)
    P("Cấp 150, 300, 600, 900, 1500 và 2500 (theo ANSI/ISA-75.08.05).",
      "Classes 150, 300, 600, 900, 1500, and 2500 (in accordance with ANSI/ISA-75.08.05).")
    TBL(["DN", "NPS", "150/300/600 mm ngắn", "mm dài", "in ngắn", "in dài",
         "900/1500 mm ngắn", "mm dài"],
        [("15", "1/2", "187", "203", "7.38", "8.00", "194", "279"),
         ("20", "3/4", "187", "206", "7.38", "8.25", "194", "279"),
         ("25", "1", "187", "210", "7.38", "8.25", "197", "279"),
         ("40", "1-1/2", "222", "251", "8.75", "9.88", "235", "330"),
         ("50", "2", "254", "286", "10.00", "11.25", "292", "375"),
         ("65", "2-1/2", "292", "311", "11.50", "12.25", "292", "375"),
         ("80", "3", "318", "337", "12.50", "13.25", "318", "460"),
         ("100", "4", "368", "394", "14.50", "15.50", "368", "530"),
         ("150", "6", "451", "508", "17.75", "20.00", "508", "768"),
         ("200", "8", "543", "610", "21.38", "24.00", "610", "832"),
         ("250", "10", "673", "752", "26.50", "29.62", "762", "991"),
         ("300", "12", "737", "819", "29.00", "32.35", "914", "1130"),
         ("350", "14", "851", "1029", "33.50", "40.50", "-", "1257"),
         ("400", "16", "1016", "1108", "40.00", "43.62", "-", "1422"),
         ("450", "18", "1143", "-", "45.00", "-", "-", "1727")],
        "Class 150/300/600 và 900/1500 / Classes 150/300/600 and 900/1500.")
    TBL(["DN", "NPS", "900/1500 in ngắn", "in dài", "2500 mm ngắn", "mm dài",
         "2500 in ngắn", "in dài"],
        [("15", "1/2", "7.62", "11.00", "216", "318", "8.50", "12.50"),
         ("20", "3/4", "7.62", "11.00", "216", "318", "8.50", "12.50"),
         ("25", "1", "7.75", "11.00", "216", "318", "8.50", "12.50"),
         ("40", "1-1/2", "9.25", "13.00", "260", "359", "10.25", "14.12"),
         ("50", "2", "11.50", "14.75", "318", "400", "12.50", "15.75"),
         ("65", "2-1/2", "11.50", "14.75", "318", "400", "12.50", "15.75"),
         ("80", "3", "12.50", "18.12", "381", "498", "15.00", "19.62"),
         ("100", "4", "14.50", "20.88", "406", "575", "16.00", "22.62"),
         ("150", "6", "24.00", "30.25", "610", "819", "24.00", "32.25"),
         ("200", "8", "24.00", "32.75", "762", "1029", "30.00", "40.25"),
         ("250", "10", "30.00", "39.00", "1016", "1270", "40.00", "50.00"),
         ("300", "12", "36.00", "44.50", "1118", "1422", "44.00", "56.00"),
         ("350", "14", "-", "49.50", "1803", "-", "71.00", "-"),
         ("400", "16", "-", "56.00", "-", "-", "-", "-"),
         ("450", "18", "-", "68.00", "-", "-", "-", "-")],
        "Class 900/1500 (inch) và Class 2500 / Classes 900/1500 (in) and 2500.")

    H("5.1.3 Kích thước mặt đến mặt của van dạng cầu đầu hàn ổ cắm",
      "5.1.3 Face-to-Face Dimensions for Socket Weld-End, Globe-Style Valves", h3)
    P("Cấp 150, 300, 600, 900, 1500 và 2500 (theo ANSI/ISA-75.08.03).",
      "Classes 150, 300, 600, 900, 1500, and 2500 (in accordance with ANSI/ISA-75.08.03).")
    TBL(["DN", "NPS", "150/300/600 mm ngắn", "mm dài", "in ngắn", "in dài",
         "900/1500 mm ngắn", "mm dài"],
        [("15", "1/2", "170", "206", "6.69", "8.12", "178", "279"),
         ("20", "3/4", "170", "210", "6.69", "8.25", "178", "279"),
         ("25", "1", "197", "210", "7.75", "8.25", "178", "279"),
         ("40", "1-1/2", "235", "251", "9.25", "9.88", "235", "330"),
         ("50", "2", "267", "286", "10.50", "11.25", "292", "375"),
         ("65", "2-1/2", "292", "311", "11.50", "12.25", "292", "-"),
         ("80", "3", "318", "337", "12.50", "13.25", "318", "533"),
         ("100", "4", "368", "394", "14.50", "15.50", "368", "530")],
        "Class 150/300/600 và 900/1500 / Classes 150/300/600 and 900/1500.")
    TBL(["DN", "NPS", "900/1500 in ngắn", "in dài", "2500 mm ngắn", "mm dài",
         "2500 in ngắn", "in dài"],
        [("15", "1/2", "7.00", "11.00", "216", "318", "8.50", "12.50"),
         ("20", "3/4", "7.00", "11.00", "216", "318", "8.50", "12.50"),
         ("25", "1", "7.00", "11.00", "216", "318", "8.50", "12.50"),
         ("40", "1-1/2", "9.25", "13.00", "260", "381", "10.25", "15.00"),
         ("50", "2", "11.50", "14.75", "324", "400", "12.75", "15.75"),
         ("65", "2-1/2", "11.50", "-", "324", "-", "12.75", "-"),
         ("80", "3", "12.50", "21.00", "381", "660", "15.00", "26.00"),
         ("100", "4", "14.50", "20.88", "406", "737", "16.00", "29.00")],
        "Class 900/1500 (inch) và Class 2500 / Classes 900/1500 (in) and 2500.")

    H("5.1.4 Kích thước mặt đến mặt của van dạng cầu đầu ren",
      "5.1.4 Face-to-Face Dimensions for Screwed-End, Globe-Style Valves", h3)
    P("Cấp 150, 300 và 600 (theo ANSI/ISA-75.08.03).",
      "Classes 150, 300, and 600 (in accordance with ANSI/ISA-75.08.03).")
    TBL(["DN", "NPS", "mm ngắn", "mm dài", "in ngắn", "in dài"],
        [("15", "1/2", "165", "206", "6.50", "8.12"),
         ("20", "3/4", "165", "210", "6.50", "8.25"),
         ("25", "1", "197", "210", "7.75", "8.25"),
         ("40", "1-1/2", "235", "251", "9.25", "9.88"),
         ("50", "2", "267", "286", "10.50", "11.25"),
         ("65", "2-1/2", "292", "311", "11.50", "12.26")],
        "Class 150, 300 và 600 / Classes 150, 300 and 600.")

    H("5.1.5 Kích thước mặt đến tâm của van góc dạng cầu mặt nổi",
      "5.1.5 Face-to-Centerline Dimensions for Raised-Face, Globe-Style Angle Valves", h3)
    P("Cấp 150, 300 và 600 (theo ANSI/ISA-75.08.08).",
      "Classes 150, 300, and 600 (in accordance with ANSI/ISA-75.08.08).")
    TBL(["DN", "NPS", "Cl150 mm", "Cl150 in", "Cl300 mm", "Cl300 in", "Cl600 mm", "Cl600 in"],
        [("25", "1", "92", "3.62", "99", "3.88", "105", "4.12"),
         ("40", "1-1/2", "111", "4.37", "117", "4.62", "125", "4.94"),
         ("50", "2", "127", "5.00", "133", "5.25", "143", "5.62"),
         ("80", "3", "149", "5.88", "159", "6.25", "168", "6.62"),
         ("100", "4", "176", "6.94", "184", "7.25", "197", "7.75"),
         ("150", "6", "226", "8.88", "236", "9.31", "254", "10.00"),
         ("200", "8", "272", "10.69", "284", "11.19", "305", "12.00")],
        "Kích thước mặt đến tâm / Face-to-centerline dimensions.")

    H("5.1.6 Kích thước mặt đến mặt của van dạng cầu bích rời",
      "5.1.6 Face-to-Face Dimensions for Separable Flange, Globe-Style Valves", h3)
    P("Cấp 150, 300 và 600 (theo ANSI/ISA-75.08.07).",
      "Classes 150, 300, and 600 (in accordance with ANSI/ISA-75.08.07).")
    TBL(["DN", "NPS", "mm", "in"],
        [("25", "1", "216", "8.50"),
         ("40", "1-1/2", "241", "9.50"),
         ("50", "2", "292", "11.50"),
         ("80", "3", "356", "14.00"),
         ("100", "4", "432", "17.00")],
        "Van bích rời / Separable-flange valves.")

    H("5.1.7 Kích thước mặt đến mặt của van quay có bích và không bích (trừ van bướm)",
      "5.1.7 Face-to-Face Dimensions for Flanged and Flangeless Rotary Valves (Except Butterfly)", h3)
    P("Cấp 150, 300 và 600 (theo ANSI/ISA-75.08.02).",
      "Classes 150, 300, and 600 (in accordance with ANSI/ISA-75.08.02).")
    TBL(["DN", "NPS", "mm", "in"],
        [("20", "3/4", "76", "3.00"), ("25", "1", "102", "4.00"),
         ("40", "1-1/2", "114", "4.50"), ("50", "2", "124", "4.88"),
         ("80", "3", "165", "6.50"), ("100", "4", "194", "7.62"),
         ("150", "6", "229", "9.00"), ("200", "8", "243", "9.56"),
         ("250", "10", "297", "11.69"), ("300", "12", "338", "13.31"),
         ("350", "14", "400", "15.75"), ("400", "16", "400", "15.75"),
         ("450", "18", "457", "18.00"), ("500", "20", "508", "20.00"),
         ("600", "24", "610", "24.00")],
        "Van quay, trừ van bướm / Rotary valves except butterfly.")

    H("5.1.8 Kích thước mặt đến mặt của van bướm một bích (kiểu lug) và không bích (kiểu wafer)",
      "5.1.8 Face-to-Face Dimensions for Single Flange (Lug-Type) and Flangeless (Wafer-Type) "
      "Butterfly Valves", h3)
    P("Theo MSS-SP-67. Kích thước thân hẹp sau khi lắp vào đường ống; không gồm chiều dày gioăng rời, "
      "nhưng gồm gioăng hoặc phớt là bộ phận cố hữu của van ở trạng thái đã nén.",
      "In accordance with MSS-SP-67. Narrow-body dimensions after installation in the pipeline; "
      "they exclude separate gasket thickness but include gaskets or seals that are an integral part "
      "of the valve, with those seals compressed.")
    TBL(["DN", "NPS", "in", "mm"],
        [("40", "1-1/2", "1.31", "33.3"), ("50", "2", "1.69", "42.9"),
         ("65", "2-1/2", "1.81", "46.0"), ("80", "3", "1.81", "46.0"),
         ("100", "4", "2.06", "52.3"), ("150", "6", "2.19", "55.6"),
         ("200", "8", "2.38", "60.5"), ("250", "10", "2.69", "68.3"),
         ("300", "12", "3.06", "77.7"), ("350", "14", "3.06", "77.7"),
         ("400", "16", "3.12", "79.2"), ("450", "18", "4.00", "101.6"),
         ("500", "20", "4.38", "111.2")],
        "Thân van tương thích bích gang Class 125 hoặc bích thép Class 150 / Bodies compatible with "
        "Class 125 cast iron or Class 150 steel flanges.")

    H("5.1.9 Kích thước mặt đến mặt của van bướm áp suất cao kiểu lệch",
      "5.1.9 Face-to-Face Dimensions for High-Pressure Butterfly Valves with Offset Design", h3)
    P("Cấp 150, 300 và 600 (theo MSS SP-68).",
      "Classes 150, 300, and 600 (in accordance with MSS SP-68).")
    TBL(["DN", "NPS", "Cl150 in", "Cl150 mm", "Cl300 in", "Cl300 mm", "Cl600 in", "Cl600 mm"],
        [("80", "3", "1.88", "48", "1.88", "48", "2.12", "54"),
         ("100", "4", "2.12", "54", "2.12", "54", "2.50", "64"),
         ("150", "6", "2.25", "57", "2.31", "59", "3.06", "78"),
         ("200", "8", "2.50", "63", "2.88", "73", "4.00", "102"),
         ("250", "10", "2.81", "71", "3.25", "83", "4.62", "117"),
         ("300", "12", "3.19", "81", "3.62", "92", "5.50", "140"),
         ("350", "14", "3.62", "92", "4.62", "117", "6.12", "155"),
         ("400", "16", "4.00", "101", "5.25", "133", "7.00", "178"),
         ("450", "18", "4.50", "114", "5.88", "149", "7.88", "200"),
         ("500", "20", "5.00", "127", "6.25", "159", "8.50", "216"),
         ("600", "24", "6.06", "154", "7.12", "181", "9.13", "232")],
        "Van bướm lệch áp suất cao / High-pressure offset butterfly valves.")

    # ------------------------------------------------------------ 5.2
    H("5.2 Phân loại rò rỉ chỗ ngồi của van điều khiển",
      "5.2 Control Valve Seat Leakage Classifications")
    P("Phân loại theo ANSI/FCI 70-2 và IEC 60534-4. Mức rò rỉ tối đa, môi trường và áp suất thử, "
      "cùng thủ tục cần thiết để xác lập cấp được nêu trong bảng dưới đây.",
      "In accordance with ANSI/FCI 70-2 and IEC 60534-4. The maximum leakage allowable, test medium "
      "and pressures, and the procedures required to establish each rating are given below.")
    TBL(["Cấp / Class", "Rò rỉ tối đa / Maximum leakage allowable",
         "Môi trường / Medium", "Áp suất thử / Test pressure", "Thủ tục / Procedure"],
        [("I", "—", "—", "—", "Không cần thử nếu người dùng và nhà cung cấp đồng ý / No test required if so agreed"),
         ("II", "0.5% công suất định mức / of rated capacity",
          "Không khí hoặc nước 10-52°C / Air or water at 10-52°C",
          "3-4 bar (45-60 psig) hoặc sụt áp vận hành tối đa, tùy giá trị nhỏ hơn",
          "Áp suất vào đầu van, đầu ra thông khí quyển; cơ cấu chấp hành tạo toàn lực đóng bình thường"),
         ("III", "0.1% công suất định mức", "Như trên / As above", "Như trên / As above", "Như trên / As above"),
         ("IV", "0.01% công suất định mức", "Như trên / As above", "Như trên / As above", "Như trên / As above"),
         ("V", "0.0005 ml/phút nước trên mỗi inch đường kính lỗ và mỗi psi chênh áp "
          "(5 × 10−12 m3/s trên mỗi mm và mỗi bar)",
          "Nước 10-52°C / Water at 10-52°C",
          "Sụt áp dịch vụ lớn nhất qua nút van, không vượt cấp áp suất thân van",
          "Đổ đầy khoang thân và ống nối, đóng van, dùng đúng lực đóng tối đa quy định, chờ dòng rò ổn định"),
         ("VI", "Không vượt giá trị trong bảng 5.3 theo đường kính cổng",
          "Không khí hoặc nitơ 10-52°C / Air or nitrogen at 10-52°C",
          "3.5 bar (50 psig) hoặc chênh áp định mức tối đa, tùy giá trị nhỏ hơn",
          "Áp suất vào đầu van, chỉnh cơ cấu chấp hành đến điều kiện vận hành với toàn lực đóng; "
          "chờ ổn định và dùng thiết bị đo phù hợp")],
        "Cấp I–VI / Classes I-VI.")

    H("5.3 Rò rỉ chỗ ngồi tối đa cho phép cấp VI",
      "5.3 Class VI Maximum Seat Leakage Allowable")
    P("Theo ANSI/FCI 70-2. Số bọt mỗi phút là phương án thay thế được đề xuất dựa trên ống có đường "
      "kính ngoài 1/4 inch (6.3 mm), thành 0.032 inch (0.8 mm), nhúng sâu 1/8 đến 1/4 inch (3 đến 6 "
      "mm) trong nước; đầu ống phải cắt vuông, nhẵn, không vát mép hoặc gờ, trục ống vuông góc với "
      "mặt nước.",
      "In accordance with ANSI/FCI 70-2. Bubbles per minute are a suggested alternative based on a "
      "1/4 inch (6.3 mm) O.D. × 0.032 inch (0.8 mm) wall tube submerged 1/8 to 1/4 inch (3 to 6 mm) in "
      "water; the tube end must be cut square and smooth with no chamfers or burrs, and the tube axis "
      "perpendicular to the water surface.")
    TBL(["Đường kính cổng danh nghĩa in", "mm", "ml/phút", "Bọt/phút"],
        [("1", "25", "0.15", "1"), ("1-1/2", "38", "0.30", "2"),
         ("2", "51", "0.45", "3"), ("2-1/2", "64", "0.60", "4"),
         ("3", "76", "0.90", "6"), ("4", "102", "1.70", "11"),
         ("6", "152", "4.00", "27"), ("8", "203", "6.75", "45")],
        "Bảng 5.3 / Table 5.3.")

    # ------------------------------------------------------------ 5.4
    H("5.4 Đặc tính dòng chảy của van điều khiển",
      "5.4 Control Valve Flow Characteristics")
    P("Đặc tính dòng chảy là quan hệ giữa lưu lượng qua van và hành trình van khi hành trình thay đổi "
      "từ 0 đến 100%. Đặc tính vốn có là đặc tính quan sát được với sụt áp không đổi qua van. Đặc tính "
      "khi lắp đặt là đặc tính thu được trong vận hành, khi sụt áp thay đổi theo lưu lượng và các thay "
      "đổi khác của hệ thống.",
      "The flow characteristic of a control valve is the relationship between the flow rate through "
      "the valve and the valve travel as the travel is varied from 0 to 100%. Inherent flow "
      "characteristic refers to the characteristic observed with a constant pressure drop across the "
      "valve. Installed flow characteristic means the one obtained in service where the pressure "
      "drop varies with flow and other changes in the system.")
    P("Việc định hình đặc tính cho van điều khiển giúp vòng điều khiển ổn định tương đối đồng đều trong "
      "toàn dải điều kiện vận hành dự kiến. Để xác định đặc tính cần thiết cho một hệ thống cho trước "
      "cần phân tích động lực học của vòng điều khiển. Tuy nhiên, các phân tích đã được thực hiện cho "
      "những quá trình thường gặp, nên có thể đưa ra một số hướng dẫn hữu ích trong lựa chọn.",
      "Characterizing control valves provides for a relatively uniform control loop stability over "
      "the expected range of system operating conditions. To establish the flow characteristic needed "
      "to match a given system requires a dynamic analysis of the control loop. Analyses of the more "
      "common processes have been performed, however, so some useful guidelines for the selection of "
      "the proper flow characteristic can be established.")

    H("5.4.1 Đặc tính dòng chảy", "5.4.1 Flow Characteristics", h3)
    P("Đặc tính mở nhanh cho sự thay đổi lớn nhất của lưu lượng ở hành trình nhỏ với quan hệ gần "
      "tuyến tính. Khi tăng hành trình thêm, mức thay đổi lưu lượng giảm mạnh và khi nút van gần vị "
      "trí mở hoàn toàn, sự thay đổi lưu lượng tiến về không. Trong van điều khiển, đặc tính mở nhanh "
      "chủ yếu dùng cho dịch vụ đóng/mở nhưng cũng phù hợp với nhiều ứng dụng thường quy định nút "
      "tuyến tính.",
      "The quick-opening flow characteristic provides for maximum change in flow rate at low valve "
      "travels with a nearly linear relationship. Additional increases in valve travel give sharply "
      "reduced changes in flow rate, and when the valve plug nears the wide open position, the change "
      "in flow rate approaches zero. In a control valve, the quick-opening characteristic is used "
      "primarily for on/off service; but it is also suitable for many applications where a linear "
      "valve plug would normally be specified.")
    FIG(1, F5.fig_f5_01())
    P("Đường đặc tính tuyến tính cho thấy lưu lượng tỷ lệ thuận với hành trình van. Quan hệ tỷ lệ này "
      "tạo ra đường có hệ số góc không đổi, nên với sụt áp không đổi, độ khuếch đại của van như nhau ở "
      "mọi lưu lượng. Độ khuếch đại của van là tỷ số giữa sự thay đổi nhỏ của lưu lượng và sự thay đổi "
      "nhỏ của vị trí nút van; nó phụ thuộc vào cỡ và cấu trúc van, điều kiện vận hành hệ thống và "
      "đặc tính nút van. Nút tuyến tính thường được chọn cho điều khiển mức chất lỏng và một số ứng "
      "dụng điều khiển lưu lượng yêu cầu độ khuếch đại không đổi.",
      "The linear flow characteristic curve shows that the flow rate is directly proportional to the "
      "valve travel. This proportional relationship produces a characteristic with a constant slope "
      "so that with constant pressure drop, the valve gain will be the same at all flows. Valve gain "
      "is the ratio of an incremental change in flow to an incremental change in valve plug position; "
      "it is a function of valve size and configuration, system operating conditions and valve plug "
      "characteristic. The linear valve plug is commonly specified for liquid level control and for "
      "certain flow control applications requiring constant gain.")
    P("Với đặc tính phần trăm bằng, các bước tăng bằng nhau của hành trình tạo ra những thay đổi có "
      "cùng phần trăm so với lưu lượng hiện có. Mức thay đổi lưu lượng luôn tỷ lệ với lưu lượng ngay "
      "trước khi thay đổi vị trí nút, đĩa hoặc bi. Van có đặc tính phần trăm bằng thường dùng cho "
      "điều khiển áp suất và các ứng dụng mà phần lớn sụt áp do chính hệ thống hấp thụ, chỉ một phần "
      "tương đối nhỏ còn lại tại van. Cũng nên cân nhắc van phần trăm bằng khi dự kiến điều kiện sụt "
      "áp thay đổi mạnh.",
      "In the equal-percentage flow characteristic, equal increments of valve travel produce "
      "equal-percentage changes in the existing flow. The change in flow rate is always proportional "
      "to the flow rate just before the change in valve plug, disk, or ball position is made. Valves "
      "with an equal-percentage flow characteristic are generally used on pressure control "
      "applications and on other applications where a large percentage of the pressure drop is "
      "normally absorbed by the system itself, with only a relatively small percentage available at "
      "the control valve. Valves with an equal-percentage characteristic should also be considered "
      "where highly varying pressure drop conditions can be expected.")

    H("5.4.2 Lựa chọn đặc tính dòng chảy", "5.4.2 Selection of Flow Characteristics", h3)
    P("Đặc tính lý tưởng là đặc tính cho đường đặc tính khi lắp đặt tuyến tính và độ khuếch đại khi "
      "lắp đặt đồng đều. Để đạt hiệu năng tối ưu có thể thực hiện phân tích động lực học đầy đủ, vì "
      "nhiều yếu tố khác ngoài đặc tính dòng chảy ảnh hưởng đến hiệu năng. Phân tích như vậy đặc biệt phù "
      " hợp với ứng dụng yêu cầu điều khiển chính xác. Với các ứng dụng khác, đặc tính không lý tưởng "
      "vẫn có thể được hiệu chỉnh ở một mức độ nhất định trong thiết bị điều khiển. Xem Chương 2 để "
      "biết thêm về hiệu năng van điều khiển.",
      "The ideal flow characteristic should be one that would result in a linear installed "
      "characteristic and a uniform installed gain. For optimal performance, a complete dynamic "
      "analysis could be performed, since there are many other factors besides flow characteristic "
      "that affect performance. Such an analysis would be most appropriate for applications where "
      "accurate control is critical. For other applications, a less-than-ideal flow characteristic "
      "may be adjusted to some degree in the control equipment. See Chapter 2 for more information "
      "on control valve performance.")

    # ------------------------------------------------------------ 5.5
    H("5.5 Định cỡ van", "5.5 Valve Sizing")
    P("Các hoạt động chuẩn hóa trong định cỡ van điều khiển bắt đầu từ đầu thập niên 1960, khi Fluids "
      "Control Institute công bố phương trình định cỡ cho cả chất lưu nén được và không nén được. Dải "
      "điều kiện được mô tả chính xác khi đó khá hẹp nên tiêu chuẩn không được chấp nhận rộng rãi. Năm "
      "1967, ISA thành lập ủy ban xây dựng và công bố các phương trình chuẩn; kết quả là quy trình "
      "định cỡ van được công nhận là Tiêu chuẩn Quốc gia Hoa Kỳ. Sau đó, một ủy ban của Ủy ban Kỹ thuật "
      "Điện Quốc tế (IEC) dùng công trình của ISA làm nền tảng để xây dựng tiêu chuẩn quốc tế. "
      "ANSI/ISA-75.01.01 và IEC 60534-2-1 đã được hài hòa, nên có thể dùng tiêu chuẩn nào cũng được.",
      "Standardization activities for control valve sizing can be traced back to the early 1960s when "
      "a trade association, the Fluids Control Institute, published sizing equations for use with "
      "both compressible and incompressible fluids. The range of service conditions that could be "
      "accommodated accurately by these equations was quite narrow, and the standard did not achieve "
      "a high degree of acceptance. In 1967, the ISA established a committee to develop and publish "
      "standard equations. The efforts of this committee culminated in a valve sizing procedure that "
      "has achieved the status of American National Standard. Later, a committee of the "
      "International Electrotechnical Commission (IEC) used the ISA works as a basis to formulate "
      "international standards for sizing control valves. The ANSI/ISA-75.01.01 and IEC 60534-2-1 "
      "valve sizing standards have been harmonized, so either standard may be used.")
    P("Dù phương trình định cỡ chuẩn làm việc tốt cho đa số trường hợp, các tiêu chuẩn đều nêu rõ giới "
      "hạn sử dụng; dùng ngoài ranh giới đó phải hết sức thận trọng. Yêu cầu về độ chính xác hợp lý "
      "của tiêu chuẩn là:",
      "Although the standard valve sizing methods work well for the majority of control valve sizing "
      "situations, it is important to note that the standards call out limits for their use. Use "
      "outside of their intended boundaries must be done with care. The standards' requirements for "
      "reasonable accuracy are:")
    B(["Chất lưu một thành phần, một pha; chất Newton; khí và hơi lý tưởng;",
       "Tỷ lệ nhiệt dung riêng lý tưởng 1.08 < γ < 1.65 đối với khí và hơi;",
       "Van có xT ≤ 0.84 và van có Cv/d² < 30."],
      ["Single component, single phase fluids; Newtonian fluids; ideal gases and vapors;",
       "Ideal ratio of specific heats in the range 1.08 < γ < 1.65 for gases and vapors;",
       "Valves with xT ≤ 0.84 and valves with Cv/d² < 30."])
    P("Trong các mục dưới đây, ký hiệu và quy trình được giải thích cùng các bài toán mẫu. Mọi dòng "
      "chảy được giả thiết là chảy rối hoàn toàn; với chất có độ nhớt cao hoặc lưu lượng rất nhỏ cần "
      "xem xét bổ sung.",
      "In the following sections, the nomenclature and procedures are explained, and sample problems "
      "are solved to illustrate their use. For the discussion below, all flows are assumed to be fully "
      "turbulent. For situations with high viscosity fluids or very low flow rates, additional "
      "considerations are required.")

    # ------------------------------------------------------------ 5.6
    H("5.6 Viết tắt và thuật ngữ", "5.6 Abbreviations and Terminology")
    P("Bảng ký hiệu dùng trong các phương trình định cỡ và định nghĩa của chúng.",
      "The symbols used in the sizing equations and their definitions.")
    TBL(["Ký hiệu / Symbol", "Định nghĩa / Definition"],
        [("Cv", "Hệ số định cỡ van / Valve sizing coefficient"),
         ("d", "Cỡ van danh nghĩa / Nominal valve size"),
         ("D1, D2", "Đường kính trong của ống thượng lưu và hạ lưu / Internal diameter of upstream and downstream piping"),
         ("Fd", "Hệ số kiểu van, không thứ nguyên / Valve style modifier, dimensionless"),
         ("FF", "Hệ số áp suất tới hạn của chất lỏng, không thứ nguyên / Liquid critical pressure ratio factor"),
         ("Fγ", "Hệ số tỷ lệ nhiệt dung riêng, không thứ nguyên / Ratio of specific heats factor"),
         ("FL", "Hệ số phục hồi áp suất chất lỏng, không thứ nguyên / Liquid pressure recovery factor"),
         ("FLP", "Hệ số phục hồi áp suất chất lỏng kết hợp hệ số hình học đường ống khi có phụ tùng kèm theo / Combined liquid pressure recovery and piping geometry factor"),
         ("Fp", "Hệ số hình học đường ống, không thứ nguyên / Piping geometry factor"),
         ("K", "Hệ số tổn thất cột áp của một thiết bị, không thứ nguyên (ζ trong tiêu chuẩn) / Head loss coefficient"),
         ("M", "Khối lượng phân tử / Molecular weight"),
         ("N", "Hằng số số học theo hệ đơn vị / Numerical constant for units"),
         ("P1, P2", "Áp suất tĩnh tuyệt đối thượng lưu, hạ lưu / Upstream and downstream absolute static pressures"),
         ("Pc", "Áp suất tới hạn nhiệt động tuyệt đối / Absolute thermodynamic critical pressure"),
         ("Pv", "Áp suất hơi bão hòa tuyệt đối của chất lỏng ở nhiệt độ đầu vào / Vapor pressure absolute of liquid at inlet temperature"),
         ("q", "Lưu lượng thể tích tiêu chuẩn / Standard volumetric flow rate (15.5°C, 101.3 kPa)"),
         ("T1", "Nhiệt độ tuyệt đối thượng lưu / Absolute upstream temperature"),
         ("w", "Lưu lượng khối lượng / Mass flow rate"),
         ("x", "Tỷ số sụt áp qua van trên áp suất tuyệt đối thượng lưu (ΔP/P1) / Ratio of pressure drop to upstream absolute pressure"),
         ("xchoked", "Tỷ lệ sụt áp gây nghẽn dòng với chất nén được / Choked pressure drop ratio"),
         ("xsizing", "Tỷ lệ sụt áp dùng định cỡ chất nén được / Pressure drop ratio used for compressible sizing"),
         ("xT", "Hệ số tỷ lệ sụt áp tại dòng nghẽn, không thứ nguyên / Pressure drop ratio factor at choked flow"),
         ("xTP", "Hệ số xT khi có phụ tùng kèm theo / Pressure drop ratio factor with attached fittings"),
         ("Y", "Hệ số giãn nở, không thứ nguyên / Expansion factor"),
         ("Z1", "Hệ số nén ở điều kiện đầu vào / Compressibility factor at inlet conditions"),
         ("γ", "Tỷ lệ nhiệt dung riêng lý tưởng / Ideal ratio of specific heats"),
         ("ν", "Độ nhớt động học / Kinematic viscosity"),
         ("ρ1", "Tỷ trọng ở điều kiện đầu vào / Density at inlet conditions"),
         ("ρ1/ρo", "Trọng lực riêng của chất lỏng ở đầu vào / Liquid specific gravity at inlet"),
         ("ΔP", "Sụt áp qua van (P1−P2) / Pressure drop across the valve"),
         ("ΔPchoked", "Sụt áp chất lỏng gây nghẽn dòng / Liquid pressure drop that limits flow by choking"),
         ("ΔPsizing", "Sụt áp dùng cho tính toán định cỡ chất lỏng / Pressure drop used for liquid sizing")],
        "Điều kiện tiêu chuẩn: 15.5°C (60°F) và 14.7 psia (101.3 kPa) / Standard conditions: 15.5°C "
        "(60°F) and 14.7 psia (101.3 kPa).")

    # ------------------------------------------------------------ 5.7
    H("5.7 Hằng số phương trình", "5.7 Equation Constants")
    P("Nhiều phương trình định cỡ chứa hằng số N với chỉ số dưới; các hằng số này cho phép dùng nhiều "
      "hệ đơn vị khác nhau. Ví dụ N1 = 1.00 khi lưu lượng là gpm và áp suất là psia; N1 = 0.0865 khi "
      "lưu lượng là m³/h và áp suất là kPa. Mọi áp suất đều là áp suất tuyệt đối.",
      "Many sizing equations contain a numerical constant N with a subscript; these constants allow "
      "different units to be used. For example N1 = 1.00 when flow is in U.S. gpm and pressures are "
      "psia; N1 = 0.0865 when flow is m³/h and pressures are kPa. All pressures are absolute.")
    TBL(["Hằng số / Constant", "Giá trị / Value", "Đơn vị / Units", "Ghi chú / Note"],
        [("N1", "0.0865", "m³/h, kPa", "Lưu lượng thể tích chất lỏng"),
         ("N1", "0.865", "m³/h, bar", ""),
         ("N1", "1.00", "gpm, psia", ""),
         ("N2", "0.00214 / 890", "mm / inch", "d, D"),
         ("N5", "0.00241 / 1000", "mm / inch", "d, D"),
         ("N6", "2.73 / 27.3 / 63.3", "kg/h kPa / kg/h bar / lb/h psia", "ρ = kg/m³, lbm/ft³"),
         ("N8", "0.948 / 94.8 / 19.3", "kg/h kPa / kg/h bar / lb/h psia", "T = K, deg R"),
         ("N9", "21.2", "m³/h, kPa, K", "Điều kiện danh định TN = 0°C"),
         ("N9", "2120", "m³/h, bar, K", "Điều kiện danh định TN = 0°C"),
         ("N9", "22.5", "m³/h, kPa, K", "Điều kiện chuẩn Ts = 15°C"),
         ("N9", "2250", "m³/h, bar, K", "Điều kiện chuẩn Ts = 15°C"),
         ("N9", "7320", "scfh, psia, deg R", "Điều kiện chuẩn TS = 60°F")],
        "Áp suất cơ sở 101.3 kPa (1.013 bar, 14.7 psia) / Pressure base 101.3 kPa (1.013 bar, 14.7 psia).")

    # ------------------------------------------------------------ 5.8
    H("5.8 Định cỡ van cho chất lỏng", "5.8 Sizing Valves for Liquids")
    P("Dưới đây là quy trình từng bước (nguyên bản viết là «step-step») định cỡ van cho dòng chất "
      "lỏng theo ISA và IEC. Nghiêm ngặt mà nói phương pháp này chỉ đúng cho chất một thành phần, "
      "nhưng có thể dùng cẩn trọng cho hỗn hợp đa thành phần. Mỗi bước đều quan trọng. Cần lưu ý rằng "
      "giá trị Cv và FL là cặp tương ứng: nếu dùng Cv khác thì phải lấy FL tương ứng từ tài liệu sản "
      "phẩm cho cỡ van và hành trình đó.",
      "Following is a step-step procedure for the sizing of control valves for liquid flow using the "
      "ISA and IEC procedure. Strictly speaking, this sizing method is valid only for single "
      "component fluids, however multi-component mixtures can be used with care. Each of these steps "
      "is important and must be considered during any valve sizing procedure. It is important to note "
      "that Cv values and FL values are matched sets. If a different Cv is used, the corresponding FL "
      "for that valve and valve travel must be obtained from the product literature.")
    O(["Xác định các biến: thiết kế mong muốn, chất lưu quá trình và điều kiện làm việc; q hoặc w, "
       "P1, P2 hoặc ΔP, T1, ρ1/ρo, Pv, Pc và ν.",
       "Xác định hằng số phương trình N1 và N2.",
       "Xác định Fp (hệ số hình học đường ống) và FLP (hệ số phục hồi áp suất chất lỏng đã điều chỉnh "
       "theo phụ tùng kèm theo), dùng Cv ước tính và FL tương ứng.",
       "Xác định sụt áp dùng để định cỡ ΔPsizing.",
       "Tính Cv; nếu giá trị này không gần giá trị ước tính ở bước 3, lặp lại với Cv mới và FL tương ứng."],
      ["Specify the variables: desired design, process fluid, and appropriate service conditions — q "
       "or w, P1, P2 or ΔP, T1, ρ1/ρo, Pv, Pc, and ν.",
       "Determine the equation constants N1 and N2.",
       "Determine Fp and FLP using an estimated Cv and the corresponding FL.",
       "Determine the pressure drop to use for sizing, ΔPsizing.",
       "Calculate Cv. If this Cv value is not close to the estimate used in step 3, iterate using this "
       "new Cv value and the corresponding FL from the product information."])

    H("5.8.1 Xác định Fp và FLP khi có phụ tùng kèm theo",
      "5.8.1 Determining the Piping Geometry Factor (FP) and the Liquid Pressure-Recovery Factor (FLP) "
      "Adjusted for Fittings", h3)
    P("Xác định Fp nếu có phụ tùng như giảm tiết, cùi chỏ hoặc chữ T nối trực tiếp vào đầu vào và đầu "
      "ra của van. Khi có thể, nên xác định Fp và FLP bằng thử nghiệm với đúng van đã quy định. Với "
      "bộ giảm tiết đồng tâm gắn trực tiếp, có thể dùng các công thức dưới dạng tổng hệ số tổn thất "
      "cột áp của tất cả phụ tùng.",
      "Determine an FP factor if fittings such as reducers, elbows, or tees will be directly attached "
      "to the inlet and outlet connections of the valve. When possible, it is recommended that FP "
      "and FLP be determined experimentally using the specified valve in actual tests. For attached "
      "concentric reducers, reasonable approximations can be made with the equations below.")
    EQ(r"\Sigma K = K_1 + K_2 + K_{B1} + K_{B2}", "1",
       "K1 và K2 là hệ số trở lực của phụ tùng thượng lưu và hạ lưu; KB1 và KB2 là hệ số Bernoulli "
       "đầu vào và đầu ra. Nếu hai đoạn ống cùng cỡ thì KB1 = KB2 và hai hệ số này được bỏ khỏi ΣK.",
       "K1 and K2 are the resistance coefficients of upstream and downstream fittings; KB1 and KB2 "
       "are the inlet and outlet Bernoulli coefficients. If upstream and downstream piping are of "
       "equal size, KB1 = KB2 and they are dropped from the ΣK equation.")
    EQ(r"F_P = \Phi(\Sigma K,\; C_v,\; d,\; D_1,\; D_2),\qquad "
       r"F_{LP} = \Psi(F_L,\;\Sigma K,\; C_v,\; d)", "2",
       "Phụ tùng thường gặp nhất là bộ giảm tiết đồng tâm ngắn; xét các trường hợp giảm ở đầu vào, "
       "giảm ở đầu ra và van lắp giữa hai bộ giảm giống hệt nhau. Fp = 1 và FLP = FL khi không có phụ "
       "tùng kèm theo.",
       "The most commonly used fitting is the short-length concentric reducer; cases cover an inlet "
       "reducer, an outlet reducer, and a valve installed between identical reducers. FP = 1 and "
       "FLP = FL when no fittings are attached.")

    H("5.8.2 Xác định sụt áp dùng để định cỡ (ΔPsizing)",
      "5.8.2 Determining the Pressure Drop to Use for Sizing (ΔPsizing)", h3)
    P("Khi chênh áp giữa thượng lưu và hạ lưu đủ lớn, chất lỏng bắt đầu hóa hơi gây chảy nghẽn. Nếu "
      "sụt áp thực tế ΔP lớn hơn sụt áp gây nghẽn thì phải dùng ΔPchoked thay cho ΔP.",
      "When the difference between upstream and downstream pressure is high enough, the liquid may "
      "start to vaporize, causing choked flow. If the actual pressure drop across the valve, ΔP, is "
      "higher than the pressure drop that causes choked flow, the choked flow pressure drop, "
      "ΔPchoked, must be used in place of the actual pressure drop.")
    EQ(r"F_F = \Phi(P_v,\;P_c),\qquad \Delta P_{\rm choked} = F_L^{2}\,(P_1 - F_F\,P_v),\qquad "
       r"\Delta P_{\rm sizing} = \min(\Delta P,\;\Delta P_{\rm choked})", "3",
       "Nếu ΔPchoked < ΔP thì dòng đang xâm thực hoặc bay hơi. Nếu áp suất đầu ra lớn hơn áp suất hơi "
       "thì xâm thực gây nghẽn dòng; nếu áp suất đầu ra nhỏ hơn áp suất hơi thì dòng bay hơi.",
       "If ΔPchoked < ΔP, the flow is either cavitating or flashing. If the outlet pressure is greater "
       "than the vapor pressure of the fluid, cavitation is causing the choked flow; if the outlet "
       "pressure is less than the vapor pressure, the flow is flashing.")

    H("5.8.3 Tính hệ số lưu lượng cần thiết (Cv)",
      "5.8.3 Calculating the Required Flow Coefficient (Cv)", h3)
    P("Hệ số lưu lượng của van cần thiết để cho qua lưu lượng đã cho được tính như sau.",
      "The valve flow coefficient required to pass the given amount of flow is calculated as follows.")
    EQ(r"q = N_1\,F_P\,C_v\sqrt{\dfrac{\Delta P_{\rm sizing}}{\rho_1/\rho_o}}\qquad\Longleftrightarrow\qquad "
       r"C_v = \dfrac{q}{N_1\,F_P}\sqrt{\dfrac{\rho_1/\rho_o}{\Delta P_{\rm sizing}}}", "4",
       "Cv ở đây phải là cặp với FL đã dùng khi tính FLP; nếu không, phải lặp lại.",
       "The Cv used here must be the one paired with the FL used to obtain FLP; otherwise iterate.")

    H("5.8.4 Bài toán mẫu định cỡ chất lỏng", "5.8.4 Liquid Sizing Sample Problem", h3)
    P("Giả thiết một lắp đặt khi khởi động nhà máy chưa chạy ở công suất thiết kế tối đa. Đường ống "
      "được tính cho công suất cuối cùng, nhưng nay muốn lắp van chỉ định cỡ theo yêu cầu hiện tại. "
      "Cỡ ống 8 inch, đã quy định van cầu Class 300 với lồng phần trăm bằng. Dùng bộ giảm tiết đồng "
      "tâm tiêu chuẩn để lắp van vào đường ống. Xác định cỡ van phù hợp.",
      "Assume an installation that, at initial plant start-up, will not be operating at maximum design "
      "capability. The lines are sized for the ultimate system capacity, but there is a desire to "
      "install a control valve now which is sized only for currently anticipated requirements. The "
      "line size is 8 inches, and a Class 300 globe valve with an equal-percentage cage has been "
      "specified. Standard concentric reducers will be used to install the valve into the line. "
      "Determine the appropriate valve size.")
    B(["Thiết kế mong muốn: van cầu Class 300, lồng phần trăm bằng, giả thiết cỡ 3 inch; van này có "
       "Cv = 121 ở 100% mở và FL = 0.89.",
       "Chất lưu: propane lỏng.",
       "Điều kiện làm việc: q = 800 gpm; P1 = 300 psig = 314.7 psia; P2 = 275 psig = 289.7 psia; "
       "ΔP = 25 psi; T1 = 21°C (70°F); ρ1/ρo = 0.50; Pv = 124.3 psia; Pc = 616.3 psia.",
       "Hằng số: N1 = 1.0 và N2 = 890.",
       "Tìm hệ số trở lực cần thiết khi ống thượng lưu và hạ lưu cùng cỡ, rồi tính Fp và FLP.",
       "Tìm hệ số áp suất tới hạn của chất lỏng, sau đó ΔPchoked. Vì sụt áp thực tế thấp hơn sụt áp "
       "nghẽn, dùng ΔP thực tế.",
       "Tính Cv cần thiết."],
      ["Desired valve design: Class 300 globe valve with an equal-percentage cage and assumed valve "
       "size of 3 inches, this valve has a 100% open Cv of 121 with FL of 0.89.",
       "Process fluid: liquid propane.",
       "Service conditions: q = 800 gpm; P1 = 300 psig = 314.7 psia; P2 = 275 psig = 289.7 psia; "
       "ΔP = 25 psi; T1 = 21°C (70°F); ρ1/ρo = 0.50; Pv = 124.3 psia; Pc = 616.3 psia.",
       "Constants: N1 = 1.0 and N2 = 890.",
       "Find the necessary resistance coefficients for equal upstream and downstream pipe sizes, "
       "then calculate Fp and FLP.",
       "Find the liquid critical pressure ratio factor, then ΔPchoked. Because the actual pressure "
       "drop is lower than the choked pressure drop, use the actual ΔP.",
       "Calculate the required Cv value."])
    P("Cv cần thiết là 125.7, vượt năng lực của van đã giả thiết có Cv = 121. Dù ở ví dụ này có thể "
      "thấy rõ cỡ lớn hơn tiếp theo (NPS 4 (DN 100)) là đúng, điều đó không phải lúc nào cũng đúng và "
      "cần lặp lại quy trình trên.",
      "The required Cv of 125.7 exceeds the capacity of the assumed valve, which has a Cv of 121. "
      "Although for this example it may be obvious that the next larger size (NPS 4 (DN 100)) would "
      "be the correct valve size, this may not always be true, and a repeat of the above procedure "
      "should be carried out.")
    P("Giờ giả thiết van NPS 4 (DN 100), Cv = 203 và FL = 0.91, lấy từ bảng hệ số lưu lượng cho van "
      "cầu Fisher ES Class 300, NPS 4 (DN 100), lồng phần trăm bằng. Tính lại Cv cần thiết với Cv "
      "giả thiết 203 trong phép tính Fp.",
      "Now, assume a NPS 4 (DN 100) valve, Cv = 203 and FL = 0.91. These values were determined from "
      "the flow coefficient table for a Class 300, NPS 4 (DN 100) Fisher ES globe valve with an "
      "equal-percentage cage. Recalculate the required Cv using an assumed Cv value of 203 in the Fp "
      "calculation.")
    P("Lời giải này chỉ cho thấy van NPS 4 (DN 100) đủ lớn để đáp ứng điều kiện làm việc. Có thể cần "
      "dự đoán chính xác hơn Cv; khi đó phải xác định lại Cv với Fp mới dựa trên Cv vừa nhận được. "
      "Trong ví dụ này Cv là 121.7, cho kết quả tiếp theo.",
      "This solution indicates only that the NPS 4 (DN 100) valve is large enough to satisfy the "
      "service conditions given. There may be cases, however, where a more accurate prediction of the "
      "Cv is required. In such cases, the required Cv should be redetermined using a new Fp value "
      "based on the Cv value obtained above. In this example, Cv is 121.7, which leads to the "
      "following result.")
    P("Vì Cv mới xác định rất gần với Cv đã dùng khi tính lại (116.6 so với 121.7), quy trình định cỡ "
      "hoàn tất: van NPS 4 (DN 100) mở khoảng 75% tổng hành trình là đủ cho yêu cầu. Ở trường hợp này "
      "không cần cập nhật FL và FLP; nếu FL thay đổi giữa các lần lặp thì phải cập nhật và tính lại Cv.",
      "Because this newly determined Cv is very close to the Cv used initially for this recalculation "
      "(116.6 versus 121.7), the valve sizing procedure is complete, and the conclusion is that a NPS "
      "4 (DN 100) valve opened to about 75% of total travel should be adequate for the required "
      "specifications. Note that for this case, it was not needed to update the FL and FLP values. If "
      "the FL value were to change between iterations, these values would need to be updated, and the "
      "Cv recalculated.")

    # ------------------------------------------------------------ 5.9
    H("5.9 Định cỡ van cho chất lưu nén được", "5.9 Sizing Valves for Compressible Fluids")
    P("Quy trình sáu bước sau đây định cỡ van cho dòng nén được theo ISA. Mỗi bước đều quan trọng.",
      "Following is a six-step procedure for the sizing of control valves for compressible flow using "
      "the ISA standardized procedure. Each of these steps is important and must be considered during "
      "any valve sizing procedure.")
    B(["Xác định các biến: thiết kế mong muốn (ví dụ van cầu cân bằng với lồng tuyến tính), chất lưu "
       "(không khí, khí tự nhiên, hơi nước…) và điều kiện làm việc: q hoặc w, P1, P2 hoặc ΔP, T1, M, "
       "γ và Z1 hoặc ρ1.",
       "Xác định hằng số N2, N5 và N6, N8 hoặc N9 tùy dữ liệu và đơn vị. Dùng N6 khi có lưu lượng "
       "khối lượng và biết tỷ trọng ρ1; nếu biết hệ số nén thì dùng N8 cho lưu lượng khối lượng và N9 "
       "cho lưu lượng thể tích tiêu chuẩn.",
       "Xác định Fp và xTP (hệ số tỷ lệ sụt áp đã điều chỉnh theo phụ tùng kèm theo), dùng Cv ước "
       "tính và xTP tương ứng. Khi không có phụ tùng, Fp = 1 và xTP = xT.",
       "Xác định tỷ lệ sụt áp dùng định cỡ xsizing và hệ số giãn nở Y. Nếu x lớn hơn tỷ lệ gây nghẽn "
       "xchoked thì dùng xchoked; khi chảy nghẽn Y = 2/3.",
       "Tính Cv; nếu chưa gần giá trị ước tính ở bước 3 thì lặp với Cv mới và xT tương ứng."],
      ["Specify the variables: desired valve design (e.g. balanced globe with linear cage), process "
       "fluid (air, natural gas, steam, etc.) and service conditions — q or w, P1, P2 or ΔP, T1, M, γ, "
       "and Z1 or ρ1.",
       "Determine N2, N5 and N6, N8 or N9 depending on data and units. N6 is used for mass flow with "
       "known density ρ1; if compressibility is known instead, N8 is used for mass flow and N9 for "
       "standard volumetric flow.",
       "Determine Fp and xTP using an estimated Cv and corresponding xTP. With no attached fittings, "
       "FP = 1 and xTP = xT.",
       "Determine xsizing and Y. If x exceeds the choked pressure drop ratio xchoked, use xchoked; "
       "when flow is choked, Y = 2/3.",
       "Calculate Cv; if it is not close to the step-3 estimate, iterate with the new Cv and the "
       "corresponding xT."])

    H("5.9.1 Xác định Fp và xTP tại dòng nghẽn khi có phụ tùng kèm theo",
      "5.9.1 Determining the Piping Geometry Factor (FP) and the Pressure Drop Ratio Factor (xTP) at "
      "Choked Flow with Attached Fittings", h3)
    P("Giá trị Fp đối với chất nén được tìm như khi định cỡ chất lỏng; xem mục 5.8.1 cho phương trình "
      "Fp và các hệ số trở lực. xTP được tìm từ giá trị xT tương ứng với Cv của van đã chọn.",
      "The value of FP for compressible flow sizing is obtained in the same manner as with liquid "
      "sizing. See section 5.8.1 for FP and the associated resistance coefficients. xTP is found using "
      "the xT value corresponding to the selected valve's Cv.")
    EQ(r"x_{TP} = \Xi(x_T,\;F_P,\;\Sigma K,\;C_v,\;d)", "5",
       "Các ký hiệu như trong mục 5.8; khi không có phụ tùng kèm theo thì xTP = xT.",
       "Symbols as in section 5.8; with no attached fittings, xTP = xT.")

    H("5.9.2 Xác định xsizing và hệ số giãn nở Y",
      "5.9.2 Determining the Pressure Drop Ratio to Use for Sizing (xsizing) and the Expansion Factor (Y)", h3)
    EQ(r"F_{\gamma} = \dfrac{\gamma}{1.4},\qquad x_{\rm choked} = F_{\gamma}\,x_{TP},\qquad "
       r"x_{\rm sizing} = \min(x,\;x_{\rm choked}),\qquad "
       r"Y = 1 - \dfrac{x_{\rm sizing}}{3\,F_{\gamma}\,x_{TP}}", "6",
       "Trước tiên tìm hệ số tỷ lệ nhiệt dung riêng Fγ, rồi tỷ lệ sụt áp gây nghẽn; hệ số giãn nở "
       "được tính từ cả xsizing và xchoked.",
       "First find the specific heat ratio factor Fγ, then the choked flow pressure drop ratio; the "
       "expansion factor is calculated using both xsizing and xchoked.")

    H("5.9.3 Tính hệ số lưu lượng (Cv)", "5.9.3 Calculating Flow Coefficient (Cv)", h3)
    P("Một trong ba phương trình sau được dùng tùy dạng dữ liệu quá trình: lưu lượng khối lượng và tỷ "
      "trọng; lưu lượng khối lượng và hệ số nén; hoặc lưu lượng thể tích tiêu chuẩn và hệ số nén.",
      "One of the following three equations is used depending on the form of the process data: mass "
      "flow rate and density; mass flow rate and compressibility; or standard volumetric flow rate and "
      "compressibility.")
    EQ(r"w = N_6\,F_P\,C_v\,Y\sqrt{x_{\rm sizing}\,P_1\,\rho_1}", "7a",
       "Lưu lượng khối lượng và tỷ trọng / Mass flow rate and density.")
    EQ(r"w = N_8\,F_P\,C_v\,Y\,P_1\sqrt{\dfrac{x_{\rm sizing}\,M}{T_1\,Z_1}}", "7b",
       "Lưu lượng khối lượng và hệ số nén / Mass flow rate and compressibility.")
    EQ(r"q = N_9\,F_P\,C_v\,Y\,P_1\sqrt{\dfrac{x_{\rm sizing}}{M\,T_1\,Z_1}}", "7c",
       "Lưu lượng thể tích tiêu chuẩn và hệ số nén / Standard volumetric flow rate and compressibility.")

    H("5.9.4 Bài toán mẫu 1 định cỡ chất nén được",
      "5.9.4 Compressible Fluid Sizing Sample Problem No. 1", h3)
    P("Xác định cỡ và phần trăm mở của van bi Fisher V250 với các điều kiện làm việc sau; giả thiết "
      "cỡ van và cỡ ống bằng nhau.",
      "Determine the size and percent opening for a Fisher V250 ball valve operating with the "
      "following service conditions. Assume that the valve and line size are equal.")
    B(["Thiết kế: van Fisher V250; chất lưu: khí tự nhiên.",
       "Điều kiện: P1 = 200 psig = 214.7 psia; P2 = 50 psig = 64.7 psia; ΔP = 150 psi; "
       "x = ΔP/P1 = 150/214.7 = 0.70; T1 = 60°F = 520°R; M = 17.38; Z1 = 1; γ = 1.31; "
       "q = 6.0 × 10^6 scfh.",
       "Hằng số: N2 = 890, N5 = 1000 và N9 = 7320 cho lưu lượng thể tích tiêu chuẩn scfh.",
       "Vì van cùng cỡ ống và không có phụ tùng kèm theo, Fp = 1 và xTP = xT. Với van V250 NPS 8 "
       "(DN 200) ở 100% hành trình, xT = 0.14.",
       "Tính Fγ, xchoked, xsizing và Y; tỷ lệ sụt áp nghẽn nhỏ hơn tỷ lệ thực tế.",
       "Tính Cv: kết quả cho thấy van đủ lớn (Cv định mức = 2190). Cv yêu cầu xảy ra tại khoảng 83 độ; "
       "ở góc này xT = 0.219, khác nhiều với giá trị định mức 0.137 dùng ban đầu."],
      ["Design: Fisher V250 valve; process fluid: natural gas.",
       "Conditions: P1 = 200 psig = 214.7 psia; P2 = 50 psig = 64.7 psia; ΔP = 150 psi; "
       "x = ΔP/P1 = 150/214.7 = 0.70; T1 = 60°F = 520°R; M = 17.38; Z1 = 1; γ = 1.31; "
       "q = 6.0 × 10^6 scfh.",
       "Constants: N2 = 890, N5 = 1000 and N9 = 7320 for standard volumetric flow in scfh.",
       "Since the valve is line-sized with no attached fittings, FP = 1 and xTP = xT. For an NPS 8 "
       "(DN 200) V250 valve at 100% travel, xT = 0.14.",
       "Calculate Fγ, xchoked, xsizing and Y; the choked pressure drop ratio is less than the actual "
       "pressure drop ratio.",
       "Calculate Cv: the result indicates the valve is adequately sized (rated Cv = 2190). The "
       "required Cv occurs at approximately 83 degrees; at that opening xT = 0.219, substantially "
       "different from the rated value of 0.137 used initially."])
    P("Tính lại xchoked: dòng vẫn nghẽn nên Cv cần thiết giảm mạnh, chỉ do sự khác biệt của xT giữa "
      "hành trình định mức và 83 độ. Tiếp tục quá trình cho đến khi có Cv cuối cùng: Cv = 923 và "
      "xT = 0.372 tại khoảng 74 độ.",
      "Recalculate xchoked: the flow is still choked, so the required Cv drops dramatically, solely "
      "because of the difference in xT values at rated and 83 degrees travel. Continuing the process "
      "results in Cv = 923 and xT = 0.372 at about 74 degrees travel.")

    H("5.9.5 Bài toán mẫu 2 định cỡ chất nén được",
      "5.9.5 Compressible Fluid Sizing Sample Problem No. 2", h3)
    P("Giả thiết cần cấp hơi cho một quá trình thiết kế vận hành ở 250 psig (17.2 bar). Nguồn cấp là "
      "ống tập trung duy trì 500 psig (34.5 bar) và 260°C (500°F). Dự kiến đường ống NPS 6 (DN 150) "
      "tiêu chuẩn dẫn hơi từ ống chính đến quá trình. Nếu cỡ van cần thiết nhỏ hơn NPS 6 (DN 150) thì "
      "lắp với bộ giảm tiết đồng tâm. Xác định van Fisher ED phù hợp với lồng tuyến tính.",
      "Assume steam is to be supplied to a process designed to operate at 250 psig (17.2 bar). The "
      "supply source is a header maintained at 500 psig (34.5 bar) and 260°C (500°F). A NPS 6 (DN 150) "
      "standard schedule line from the steam main to the process is being planned. Also assume that if "
      "the required valve size is less than NPS 6 (DN 150), it will be installed using concentric "
      "reducers. Determine the appropriate Fisher ED valve with a linear cage.")
    B(["Thiết kế: van Fisher ED Class 300 với lồng tuyến tính; giả thiết cỡ NPS 4 (DN 100). Chất lưu: "
       "hơi quá nhiệt.",
       "Ống 6 inch tiêu chuẩn có D = 6.1 inch.",
       "Điều kiện: w = 125,000 lb/h; P1 = 500 psig = 514.7 psia; P2 = 250 psig = 264.7 psia; "
       "ΔP = 250 psi; x = ΔP/P1 = 250/514.7 = 0.49; T1 = 260°C (500°F); ρ1 = 1.042 lbm/ft³; γ = 1.33.",
       "Thử van NPS 4 (DN 100) ED với trim tuyến tính ở 100% hành trình: Cv = 236, xT = 0.690.",
       "Hằng số: N2 = 890, N5 = 1000 và N6 = 63.3 cho lưu lượng lb/h và tỷ trọng lbm/ft³.",
       "Vì ống thượng lưu và hạ lưu cùng cỡ, tính hệ số trở lực, rồi Fp và xTP.",
       "Tỷ lệ sụt áp nghẽn lớn hơn tỷ lệ thực tế, nên dùng tỷ lệ thực tế; tính Y rồi Cv."],
      ["Design: Class 300 Fisher ED valve with a linear cage; assume valve size NPS 4 (DN 100). "
       "Process fluid: superheated steam.",
       "6-inch standard schedule pipe has D = 6.1 inches.",
       "Conditions: w = 125,000 lb/h; P1 = 500 psig = 514.7 psia; P2 = 250 psig = 264.7 psia (printed "
       "as P1); ΔP = 250 psi; x = ΔP/P1 = 250/514.7 = 0.49; T1 = 260°C (500°F); ρ1 = 1.042 lbm/ft³; "
       "γ = 1.33.",
       "Try a NPS 4 (DN 100) ED valve with linear trim at 100% travel: Cv = 236, xT = 0.690.",
       "Constants: N2 = 890, N5 = 1000 and N6 = 63.3 for lb/h and lbm/ft³.",
       "Since upstream and downstream pipes are the same size, calculate the resistance coefficients, "
       "then FP and xTP.",
       "The choked flow pressure drop ratio is greater than the actual pressure drop ratio, so use "
       "the actual ratio; calculate Y then Cv."])
    P("Lặp với các giá trị xT từ danh mục sản phẩm cho Cv = 169 và xT = 0.754. Điều này xảy ra tại "
      "khoảng 66% mở, nên van NPS 4 (DN 100) ED với trim tuyến tính là giải pháp chấp nhận được về "
      "năng lực. Cỡ nhỏ hơn tiếp theo có Cv định mức chỉ 148 nên không phù hợp.",
      "Iterating using xT values from the product catalog results in a required Cv = 169 and xT = "
      "0.754. This occurs at about 66% open, so the NPS 4 (DN 100) ED valve with linear trim would be "
      "an acceptable solution with respect to capacity. The next smaller size of ED valve with linear "
      "trim has a rated Cv of only 148, so it would not be an appropriate valve for this situation.")

    # ------------------------------------------------------------ 5.10
    H("5.10 Hệ số định cỡ đại diện", "5.10 Representative Sizing Coefficients")
    P("Các bảng sau cho giá trị Cv, FL, xT và Fd đại diện cho một số kiểu van; phải dùng dữ liệu của "
      "nhà sản xuất cho sản phẩm cụ thể.",
      "The following tables give representative Cv, FL, xT and Fd values for several valve styles; "
      "manufacturer data must be used for a specific product.")

    H("5.10.1 Van dạng cầu một cổng", "5.10.1 Single-Ported, Globe-Style Valve Bodies", h3)
    TBL(["NPS", "Kiểu nút / Plug", "Đặc tính / Characteristic", "Đường kính cổng in",
         "Hành trình in", "Cv", "FL", "xT", "Fd"],
        [("1/2", "Post-Guided", "Equal-Percentage", "0.38", "0.50", "2.41", "0.90", "0.54", "0.61"),
         ("3/4", "Post-Guided", "Equal-Percentage", "0.56", "0.50", "5.92", "0.84", "0.61", "0.61"),
         ("1", "Micro-Form", "Equal-Percentage", "3/8", "3/4", "3.07", "0.89", "0.66", "0.72"),
         ("1", "Micro-Form", "Equal-Percentage", "1/2", "3/4", "4.91", "0.93", "0.80", "0.67"),
         ("1", "Micro-Form", "Equal-Percentage", "3/4", "3/4", "8.84", "0.97", "0.92", "0.62"),
         ("1", "Cage-Guided", "Linear", "1-5/16", "3/4", "20.6", "0.84", "0.64", "0.34"),
         ("1", "Cage-Guided", "Equal-Percentage", "1-5/16", "3/4", "17.2", "0.88", "0.67", "0.38"),
         ("1-1/2", "Micro-Form", "Equal-Percentage", "3/8", "3/4", "3.20", "0.84", "0.65", "0.72"),
         ("1-1/2", "Micro-Form", "Equal-Percentage", "1/2", "3/4", "5.18", "0.91", "0.71", "0.67"),
         ("1-1/2", "Micro-Form", "Equal-Percentage", "3/4", "3/4", "10.2", "0.92", "0.80", "0.62"),
         ("1-1/2", "Cage-Guided", "Linear", "1-7/8", "3/4", "39.2", "0.82", "0.66", "0.34"),
         ("1-1/2", "Cage-Guided", "Equal-Percentage", "1-7/8", "3/4", "35.8", "0.84", "0.68", "0.38"),
         ("2", "Cage-Guided", "Linear", "2-5/16", "1-1/8", "72.9", "0.77", "0.64", "0.33"),
         ("2", "Cage-Guided", "Equal-Percentage", "2-5/16", "1-1/8", "59.7", "0.85", "0.69", "0.31"),
         ("3", "Cage-Guided", "Linear", "3-7/16", "1-1/2", "148", "0.82", "0.62", "0.30"),
         ("3", "Cage-Guided", "Equal-Percentage", "3-7/16", "1-1/2", "136", "0.82", "0.68", "0.32"),
         ("4", "Cage-Guided", "Linear", "4-3/8", "2", "236", "0.82", "0.69", "0.28"),
         ("4", "Cage-Guided", "Equal-Percentage", "4-3/8", "2", "224", "0.82", "0.72", "0.28"),
         ("6", "Cage-Guided", "Linear", "7", "2", "433", "0.84", "0.74", "0.28"),
         ("6", "Cage-Guided", "Equal-Percentage", "7", "2", "394", "0.85", "0.78", "0.26"),
         ("8", "Cage-Guided", "Linear", "8", "3", "846", "0.87", "0.81", "0.31"),
         ("8", "Cage-Guided", "Equal-Percentage", "8", "3", "818", "0.86", "0.81", "0.26")],
        "Hệ số định cỡ đại diện, thân cầu một cổng / Representative sizing coefficients, single-ported globe bodies.")

    H("5.10.2 Van quay", "5.10.2 Representative Sizing Coefficients for Rotary Valves", h3)
    TBL(["NPS", "Kiểu van / Style", "Góc mở", "Cv", "FL", "xT", "Fd"],
        [("1", "V-Notch Ball", "60", "15.6", "0.86", "0.53", "-"),
         ("1", "V-Notch Ball", "90", "34.0", "0.86", "0.42", "-"),
         ("1-1/2", "V-Notch Ball", "60", "28.5", "0.85", "0.50", "-"),
         ("1-1/2", "V-Notch Ball", "90", "77.3", "0.74", "0.27", "-"),
         ("2", "V-Notch Ball", "60", "59.2", "0.81", "0.53", "-"),
         ("2", "V-Notch Ball", "90", "132", "0.77", "0.41", "-"),
         ("2", "High-Performance Butterfly", "60", "58.9", "0.76", "0.50", "0.49"),
         ("2", "High-Performance Butterfly", "90", "80.2", "0.71", "0.44", "0.70"),
         ("3", "V-Notch Ball", "60", "120", "0.80", "0.50", "0.92"),
         ("3", "V-Notch Ball", "90", "321", "0.74", "0.30", "0.99"),
         ("3", "High-Performance Butterfly", "60", "115", "0.81", "0.46", "0.49"),
         ("3", "High-Performance Butterfly", "90", "237", "0.64", "0.28", "0.70"),
         ("4", "V-Notch Ball", "60", "195", "0.80", "0.52", "0.92"),
         ("4", "V-Notch Ball", "90", "596", "0.62", "0.22", "0.99"),
         ("4", "High-Performance Butterfly", "60", "270", "0.69", "0.32", "0.49"),
         ("4", "High-Performance Butterfly", "90", "499", "0.53", "0.19", "0.70"),
         ("6", "V-Notch Ball", "60", "340", "0.80", "0.52", "0.91"),
         ("6", "V-Notch Ball", "90", "1100", "0.58", "0.20", "0.99"),
         ("6", "High-Performance Butterfly", "60", "664", "0.66", "0.33", "0.49"),
         ("6", "High-Performance Butterfly", "90", "1260", "0.55", "0.20", "0.70"),
         ("8", "V-Notch Ball", "60", "518", "0.82", "0.54", "0.91"),
         ("8", "V-Notch Ball", "90", "1820", "0.54", "0.18", "0.99"),
         ("8", "High-Performance Butterfly", "60", "1160", "0.66", "0.31", "0.49"),
         ("8", "High-Performance Butterfly", "90", "2180", "0.48", "0.19", "0.70"),
         ("10", "V-Notch Ball", "60", "1000", "0.80", "0.47", "0.91"),
         ("10", "V-Notch Ball", "90", "3000", "0.56", "0.19", "0.99"),
         ("10", "High-Performance Butterfly", "60", "1670", "0.66", "0.38", "0.49"),
         ("10", "High-Performance Butterfly", "90", "3600", "0.48", "0.17", "0.70"),
         ("12", "V-Notch Ball", "60", "1530", "0.78", "0.49", "0.92"),
         ("12", "V-Notch Ball", "90", "3980", "0.63", "0.25", "0.99"),
         ("12", "High-Performance Butterfly", "60", "2500", "-", "-", "0.49"),
         ("12", "High-Performance Butterfly", "90", "5400", "-", "-", "0.70"),
         ("16", "V-Notch Ball", "60", "2380", "0.80", "0.45", "0.92"),
         ("16", "V-Notch Ball", "90", "8270", "0.37", "0.13", "1.00"),
         ("16", "High-Performance Butterfly", "60", "3870", "0.69", "0.40", "-"),
         ("16", "High-Performance Butterfly", "90", "8600", "0.52", "0.23", "-")],
        "Hệ số định cỡ đại diện, van quay / Representative sizing coefficients, rotary valves.")

    # ------------------------------------------------------------ 5.11
    H("5.11 Định cỡ cơ cấu chấp hành", "5.11 Actuator Sizing")
    P("Cơ cấu chấp hành được chọn bằng cách đối chiếu lực cần thiết để đi van với lực mà cơ cấu có "
      "thể cung cấp. Với van quay, quy trình tương tự đối chiếu mô-men cần thiết với mô-men đầu ra. "
      "Cùng một nguyên tắc được dùng cho cơ cấu khí nén, điện và điện-thủy lực.",
      "Actuators are selected by matching the force required to stroke the valve with an actuator that "
      "can supply that force. For rotary valves a similar process matches the torque required to "
      "stroke the valve with an actuator that will supply that torque. The same fundamental process "
      "is used for pneumatic, electric, and electro-hydraulic actuators.")

    H("5.11.1 Van cầu", "5.11.1 Globe Valves", h3)
    P("Lực cần để vận hành van cầu gồm: lực khắc phục mất cân bằng tĩnh của nút van; lực tạo tải chỗ "
      "ngồi; lực khắc phục ma sát đệm kín; và các lực bổ sung cho một số ứng dụng hoặc cấu trúc đặc "
      "biệt. Tổng lực = A + B + C + D.",
      "The force required to operate a globe valve includes: force to overcome static unbalance of the "
      "valve plug; force to provide a seat load; force to overcome packing friction; and additional "
      "forces required for certain applications or constructions. Total force required = A + B + C + D.")

    H("5.11.1.1 Lực mất cân bằng (A)", "5.11.1.1 Unbalance Force (A)", h4)
    P("Lực mất cân bằng là lực do áp suất chất lỏng khi đóng; nói chung: lực mất cân bằng = chênh áp "
      "ròng × diện tích mất cân bằng ròng. Thường lấy áp suất đo lớn nhất thượng lưu làm chênh áp ròng "
      "trừ khi thiết kế quá trình luôn bảo đảm áp suất ngược ở áp suất đầu vào lớn nhất. Diện tích mất "
      "cân bằng ròng là diện tích cổng của van một chỗ ngồi dòng đi lên; tùy cấu trúc có thể phải tính "
      "cả diện tích thân. Van cân bằng vẫn có một diện tích nhỏ mất cân bằng; số liệu này do nhà sản "
      "xuất cung cấp.",
      "The unbalance force is that resulting from fluid pressure at shutoff and in the most general "
      "sense can be expressed as: unbalance force = net pressure differential × net unbalance area. "
      "Frequent practice is to take the maximum upstream gauge pressure as the net pressure "
      "differential unless the process design always ensures a back pressure at the maximum inlet "
      "pressure. Net unbalance area is the port area on a single-seated, flow-up design. Unbalance "
      "area may have to take into account the stem area depending on configuration. For balanced "
      "valves there is still a small unbalance area; this data can be obtained from the manufacturer.")
    FIG(2, F5.fig_f5_02())
    TBL(["Đường kính cổng in", "Diện tích mất cân bằng — van một chỗ, mất cân bằng",
         "Diện tích mất cân bằng — van cân bằng"],
        [("1/4", "0.028", "-"), ("3/8", "0.110", "-"), ("1/2", "0.196", "-"),
         ("3/4", "0.441", "-"), ("1", "0.785", "-"), ("1-5/16", "1.35", "0.04"),
         ("1-7/8", "2.76", "0.062"), ("2-5/16", "4.20", "0.27"),
         ("3-7/16", "9.28", "0.118"), ("4-3/8", "15.03", "0.154"),
         ("7", "38.48", "0.81"), ("8", "50.24", "0.86")],
        "Diện tích cổng điển hình / Typical port areas (in²).")

    H("5.11.1.2 Lực tạo tải chỗ ngồi (B)",
      "5.11.1.2 Force to Provide Seat Load (B)", h4)
    FIG(3, F5.fig_f5_03())
    TBL(["Cấp rò / Leak class", "Tải chỗ ngồi khuyến nghị / Recommended seat load"],
        [("Class I", "Theo yêu cầu của người sử dụng, không cần thử rò tại nhà máy / As required by user specification, no factory leak test required"),
         ("Class II", "20 pound trên mỗi inch đường tròn cổng / 20 pounds per lineal inch of port circumference"),
         ("Class III", "40 pound trên mỗi inch đường tròn cổng / 40 pounds per lineal inch"),
         ("Class IV", "Chỗ ngồi tiêu chuẩn (dưới): 40 pound/inch (cổng đến 4-3/8 inch); "
          "80 pound/inch (cổng lớn hơn 4-3/8 inch) / Standard (lower) seat only: 40 lb/in up through "
          "4-3/8 in port; 80 lb/in for larger ports"),
         ("Class V", "Kim loại: xác định pound/inch từ Hình 5.2 / Metal seat: determine pounds per lineal inch from Figure 5.2"),
         ("Class VI", "Kim loại: 300 pound trên mỗi inch đường tròn cổng / Metal seat: 300 pounds per lineal inch")],
        "Tải chỗ ngồi / Recommended seat load (bản in ghi «Figure 5.2» cho Class V, giữ nguyên / the "
        "source cites Figure 5.2 for Class V, kept as printed).")
    FIG(4, F5.fig_f5_04())
    P("Tải chỗ ngồi, thường tính bằng pound trên mỗi inch đường tròn cổng, được xác định bởi yêu cầu "
      "đóng. Dùng hướng dẫn trên để đạt phép thử chấp nhận tại nhà máy theo ANSI/FCI 70-2 và IEC "
      "60534-4 cho các cấp II đến VI. Do khác biệt về mức độ khắc nghiệt của điều kiện làm việc, "
      "không nên coi các cấp rò và tỷ lệ rò tương ứng là chỉ số hiệu năng hiện trường. Để kéo dài "
      "tuổi thọ chỗ ngồi và khả năng đóng, dùng tải cao hơn khuyến nghị; nếu đóng kín không phải ưu "
      "tiên chính thì dùng cấp rò thấp hơn.",
      "Seat load, usually expressed in pounds per lineal inch of port circumference, is determined by "
      "shutoff requirements. Use the following guidelines to determine the seat load required to meet "
      "the factory acceptance tests for ANSI/FCI 70-2 and IEC 60534-4 leak classes II through VI. See "
      "Figures 5.3 and 5.4 for recommended seat load. Because of differences in the severity of "
      "service conditions, do not construe these leak classifications and corresponding leakage rates "
      "as indicators of field performance. To prolong seat life and shutoff capabilities, use a higher "
      "than recommended seat load. If tight shutoff is not a prime consideration, use a lower leak class.")

    H("5.11.1.3 Ma sát đệm kín (C)", "5.11.1.3 Packing Friction (C)", h4)
    P("Ma sát đệm kín phụ thuộc vào cỡ thân, kiểu đệm và tải nén do quá trình hoặc bu lông đặt lên đệm. "
      "Đặc tính ma sát không lặp lại hoàn toàn 100%. Thiết kế đệm nạp tải trực tiếp có thể có lực ma "
      "sát đáng kể, đặc biệt khi dùng đệm than chì.",
      "Packing friction is determined by stem size, packing type, and the amount of compressive load "
      "placed on the packing by the process or the bolting. Packing friction is not 100% repeatable in "
      "its friction characteristics. Live-loaded packing designs can have significant friction forces "
      "especially if graphite packing is used.")
    FIG(5, F5.fig_f5_05())
    TBL(["Cỡ thân in", "Cấp áp", "PTFE đơn", "PTFE đôi", "Graphite ribbon / filament"],
        [("5/16", "All", "20", "30", "-"),
         ("3/8", "125", "38", "56", "-"), ("3/8", "150/250", "38", "56", "125/-"),
         ("3/8", "300", "38", "56", "190"), ("3/8", "600", "38", "56", "250"),
         ("3/8", "900", "38", "56", "320"), ("3/8", "1500", "38", "56", "380"),
         ("1/2", "125", "50", "75", "-"), ("1/2", "150/250", "50", "75", "180/-"),
         ("1/2", "300", "50", "75", "230"), ("1/2", "600", "50", "75", "320"),
         ("1/2", "900", "50", "75", "410"), ("1/2", "1500", "50", "75", "500"),
         ("1/2", "2500", "50", "75", "590"),
         ("5/8", "125", "63", "95", "-"), ("5/8", "150/250", "63", "95", "218/-"),
         ("5/8", "300", "63", "95", "290"), ("5/8", "600", "63", "95", "400"),
         ("3/4", "125", "75", "112.5", "-"), ("3/4", "150/250", "75", "112.5", "350/-"),
         ("3/4", "300", "75", "112.5", "440"), ("3/4", "600", "75", "112.5", "660"),
         ("3/4", "900", "75", "112.5", "880"), ("3/4", "1500", "75", "112.5", "1100"),
         ("3/4", "2500", "75", "112.5", "1320"),
         ("1", "300", "100", "150", "610"), ("1", "600", "100", "150", "850"),
         ("1", "900", "100", "150", "1060"), ("1", "1500", "100", "150", "1300"),
         ("1", "2500", "100", "150", "1540"),
         ("1-1/4", "300", "120", "180", "800"), ("1-1/4", "600", "120", "180", "1100"),
         ("1-1/4", "900", "120", "180", "1400"), ("1-1/4", "1500", "120", "180", "1700"),
         ("1-1/4", "2500", "120", "180", "2040"),
         ("2", "300", "200", "300", "1225"), ("2", "600", "200", "300", "1725"),
         ("2", "900", "200", "300", "2250"), ("2", "1500", "200", "300", "2750"),
         ("2", "2500", "200", "300", "3245")],
        "Giá trị ma sát điển hình với quy trình siết bu lông đệm tiêu chuẩn / Typical friction forces "
        "with standard packing flange bolt torquing procedures (một số ô ghép từ cột bị gãy / some cells "
        "reconstructed from column-broken rows).")

    H("5.11.1.4 Các lực bổ sung (D)", "5.11.1.4 Additional Forces (D)", h4)
    P("Có thể cần lực bổ sung để đi van như độ cứng của ống mềm, lực ma sát bất thường do phớt hoặc "
      "lực ngồi đặc biệt cho phớt kim loại mềm. Nhà sản xuất nên cung cấp thông tin này hoặc tính đến "
      "nó khi định cỡ cơ cấu chấp hành.",
      "Additional forces may be required to stroke the valve such as: bellow stiffness; unusual "
      "frictional forces resulting from seals; or special seating forces for soft metal seals as an "
      "example. The manufacturer should either supply this information or take it into account when "
      "sizing an actuator.")

    H("5.11.2 Tính lực cơ cấu chấp hành", "5.11.2 Actuator Force Calculations", h3)
    P("Cơ cấu chấp hành màng khí nén tạo lực ròng với áp suất khí bổ sung sau khi nén lò xo (air-to-close) "
      "hoặc với sự tiền nén ròng của lò xo (air-to-open). Ví dụ: cần 275 lbf để đóng van; một cơ cấu "
      "air-to-open với diện tích màng 100 inch vuông và bench set 6 đến 15 psig là một lựa chọn. Dải "
      "vận hành dự kiến 3 đến 15 psig; tiền nén là hiệu giữa đầu dưới bench set (6 psig) và đầu dải "
      "vận hành (3 psig).",
      "Pneumatic diaphragm actuators provide a net force with the additional air pressure after "
      "compressing the spring in air to close, or with the net precompression of the spring in air to "
      "open. For example: suppose 275 lbf is required to close the valve. An air-to-open actuator with "
      "100 square inches of diaphragm area and a bench set of 6 to 15 psig is one available option. "
      "The expected operating range is 3 to 15 psig; the precompression is the difference between the "
      "lower end of the bench set (6 psig) and the beginning of the operating range (3 psig).")
    EQ(r"F_{\rm net}=3\;{\rm psig}\times 100\;{\rm in^2}=300\;{\rm lbf}", "8",
       "Lực này vượt lực yêu cầu nên lựa chọn đủ. Cơ cấu piston có lò xo được tính tương tự; cơ cấu "
       "không lò xo: (diện tích piston)(áp suất cấp tối thiểu) = lực đẩy sẵn có.",
       "This exceeds the force required and is an adequate selection. Spring-loaded piston actuators "
       "are sized the same way; without springs: (piston area)(minimum supply pressure) = available "
       "thrust.")
    P("Trong một số trường hợp cơ cấu chấp hành có thể cung cấp quá nhiều lực, làm thân van bị uốn cong "
      "gây rò hoặc hư hỏng chi tiết bên trong. Nhà sản xuất thường chịu trách nhiệm định cỡ cơ cấu và "
      "nên có phương pháp kiểm tra tải trọng tối đa trên thân, đồng thời công bố lực đẩy, diện tích "
      "màng hiệu dụng và số liệu lò xo.",
      "In some circumstances an actuator could supply too much force and cause the stem to buckle, to "
      "bend sufficiently to cause a leak, or to damage valve internals. The manufacturer normally "
      "takes responsibility for actuator sizing and should have methods documented to check for "
      "maximum stem loads. Manufacturers also publish data on actuator thrusts, effective diaphragm "
      "areas, and spring data.")

    # ------------------------------------------------------------ 5.12
    H("5.12 Định cỡ cơ cấu chấp hành cho van quay",
      "5.12 Actuator Sizing for Rotary Valves")
    P("Khi chọn cơ cấu chấp hành kinh tế nhất cho van quay, các yếu tố quyết định là mô-men cần để mở "
      "và đóng van và mô-men đầu ra của cơ cấu. Phương pháp này giả thiết van đã được định cỡ đúng và "
      "ứng dụng không vượt giới hạn áp suất của van.",
      "In selecting the most economical actuator for a rotary valve, the determining factors are the "
      "torque required to open and close the valve and the torque output of the actuator. This method "
      "assumes the valve has been properly sized for the application and the application does not "
      "exceed pressure limitations for the valve.")
    H("5.12.1 Phương trình mô-men", "5.12.1 Torque Equations", h3)
    P("Mô-men của van quay bằng tổng của nhiều thành phần. Để tránh nhầm lẫn, một số thành phần đã "
      "được gộp và một số phép tính đã thực hiện sẵn, nên mô-men của mỗi kiểu van được biểu diễn bằng "
      "hai phương trình đơn giản.",
      "Rotary valve torque equals the sum of a number of torque components. To avoid confusion, a "
      "number of these have been combined and a number of calculations have been performed in "
      "advance, so the torques required for each valve type can be represented with two simple and "
      "practical equations.")
    H("5.12.2 Mô-men khởi động", "5.12.2 Breakout Torque", h3)
    EQ(r"T_B = A\,(\Delta P_{\rm shutoff}) + B", "9",
       "A và B là hệ số theo kiểu van và cỡ van / A and B are valve-style and size factors.")
    H("5.12.3 Mô-men động", "5.12.3 Dynamic Torque", h3)
    EQ(r"T_D = C\,(\Delta P_{\rm eff})", "10",
       "C là hệ số theo kiểu van và cỡ van / C is the valve-style and size factor.")

    # ------------------------------------------------------------ 5.13
    H("5.13 Hệ số mô-men van quay điển hình", "5.13 Typical Rotary Valve Torque Factors")
    H("5.13.1 Van bi rãnh V với phớt composite",
      "5.13.1 Torque Factors for V-Notch Ball Valve with Composition Seal", h3)
    TBL(["NPS", "Đường kính trục in", "A", "B", "C 60°", "C 70°", "Tối đa TD, lbf·in"],
        [("2-1/2", "0.15", "80", "0.11", "0.60", "515", "-"),
         ("3", "3/4", "0.10", "280", "0.15", "3.80", "2120"),
         ("4", "3/4", "0.10", "380", "1.10", "18.0", "2120"),
         ("6", "1", "1.80", "500", "1.10", "36.0", "4140"),
         ("8", "1-1/4", "1.80", "750", "3.80", "60.0", "9820"),
         ("10", "1-1/4", "1.80", "1250", "3.80", "125", "9820"),
         ("12", "1-1/2", "4.00", "3000", "11.0", "143", "12,000"),
         ("14", "1-3/4", "42", "2400", "75", "413", "23,525"),
         ("16", "2", "60", "2800", "105", "578", "23,525"),
         ("18", "2-1/8", "60", "2800", "105", "578", "55,762"),
         ("20", "2-1/2", "97", "5200", "190", "1044", "55,762")],
        "Cột A bị gãy ở dòng NPS 2-1/2 trong lớp văn bản; giữ nguyên / the A column is column-broken at "
        "NPS 2-1/2 in the text layer; kept as printed.")

    H("5.13.2 Van bướm hiệu năng cao với phớt composite",
      "5.13.2 Torque Factors for High-Performance Butterfly Valve with Composition Seal", h3)
    TBL(["NPS", "Trục in", "A", "B", "C 60°", "C 75°", "C 90°",
         "TB breakout", "TD dynamic"],
        [("3", "1/2", "0.50", "136", "0.8", "1.8", "8", "280", "515"),
         ("4", "5/8", "0.91", "217", "3.1", "4.7", "25", "476", "1225"),
         ("6", "3/4", "1.97", "403", "30", "24", "70", "965", "2120"),
         ("8", "1", "4.2", "665", "65", "47", "165", "1860", "4140"),
         ("10", "1-1/4", "7.3", "1012", "125", "90", "310", "3095", "9820"),
         ("12", "1-1/2", "11.4", "1422", "216", "140", "580", "4670", "12,000")],
        "Mô-men tính bằng inch-pound / Torques in inch-pounds.")

    H("5.13.2.1 Góc quay tối đa", "5.13.2.1 Maximum Rotation", h4)
    P("Góc quay tối đa là góc của đĩa hoặc bi ở vị trí mở hoàn toàn, thường là 90 độ. Một số cơ cấu "
      "piston hồi vị bằng lò xo và cơ cấu màng-lò xo khí nén bị giới hạn ở 60 hoặc 75 độ. Với cơ cấu "
      "màng-lò xo, giới hạn góc quay cho phép tiền nén lò xo lớn hơn nên mô-men khởi động cao hơn. "
      "Chiều dài hiệu dụng của cần đòn cũng thay đổi theo góc quay; mô-men công bố, đặc biệt của cơ "
      "cấu piston khí nén, phản ánh sự thay đổi này.",
      "Maximum rotation is defined as the angle of valve disk or ball in the fully open position, "
      "normally 90 degrees. Some pneumatic spring-return piston and pneumatic spring-and-diaphragm "
      "actuators are limited to 60 or 75 degrees rotation. For spring-and-diaphragm actuators, "
      "limiting maximum rotation allows for higher initial spring compression, resulting in more "
      "actuator breakout torque. The effective length of each actuator lever also changes with valve "
      "rotation; published torques, particularly for pneumatic piston actuators, reflect this "
      "changing lever length.")

    # ------------------------------------------------------------ 5.14
    H("5.14 Xâm thực và bay hơi", "5.14 Cavitation and Flashing")
    H("5.14.1 Dòng nghẽn gây bay hơi và xâm thực",
      "5.14.1 Choked Flow Causes Flashing and Cavitation", h3)
    P("Tiêu chuẩn định cỡ chất lỏng IEC tính sụt áp nghẽn ΔPchoked. Nếu sụt áp thực tế qua van lớn hơn "
      "ΔPchoked thì có thể xảy ra bay hơi hoặc xâm thực, và có thể gây hư hỏng cấu trúc cho van và "
      "đường ống lân cận. Hiểu rõ điều gì đang xảy ra bên trong van cho phép chọn van loại bỏ hoặc "
      "giảm ảnh hưởng của xâm thực và bay hơi.",
      "The IEC liquid sizing standard calculates a choked pressure drop, ΔPchoked. If the actual "
      "pressure drop across the valve is greater than ΔPchoked then either flashing or cavitation may "
      "occur. Structural damage to the valve and adjacent piping may also result. Knowledge of what "
      "is actually happening within the valve will permit selection of a valve that can eliminate or "
      "reduce the effects of cavitation and flashing.")
    FIG(6, F5.fig_f5_06())
    P("Thuật ngữ «hiện tượng vật lý» được dùng để mô tả bay hơi và xâm thực vì các điều kiện này là "
      "những thay đổi thực sự của pha chất lưu, từ lỏng sang hơi, do vận tốc tăng tại hoặc ngay sau "
      "chỗ tiết lưu lớn nhất, thường là cổng van. Khi dòng lỏng đi qua chỗ tiết lưu, dòng bị thắt lại; "
      "tiết diện nhỏ nhất nằm ngay sau chỗ tiết lưu vật lý, gọi là vena contracta.",
      "The physical phenomena label is used to describe flashing and cavitation because these "
      "conditions represent actual changes in the phase of the fluid media. The change is from the "
      "liquid state to the vapor state and results from the increase in fluid velocity at or just "
      "downstream of the greatest flow restriction, normally the valve port. As liquid flow passes "
      "through the restriction, there is a necking down, or contraction, of the flow stream. The "
      "minimum cross-sectional area of the flow stream occurs just downstream of the actual physical "
      "restriction at a point called the vena contracta.")
    P("Để duy trì dòng chảy ổn định, vận tốc phải lớn nhất tại vena contracta, nơi tiết diện nhỏ nhất. "
      "Tăng vận tốc (năng lượng động) đi kèm giảm đáng kể áp suất (năng lượng thế) tại đây. Phía hạ "
      "lưu hơn, khi dòng giãn ra, vận tốc giảm và áp suất tăng, nhưng áp suất không bao giờ phục hồi "
      "hoàn toàn về giá trị thượng lưu. Sụt áp ΔP qua van là thước đo năng lượng đã tiêu tán trong van.",
      "To maintain a steady flow of liquid through the valve, the velocity must be greatest at the "
      "vena contracta, where cross-sectional area is the least. The increase in velocity (or kinetic "
      "energy) is accompanied by a substantial decrease in pressure (or potential energy) at the vena "
      "contracta. Further downstream, as the fluid stream expands into a larger area, velocity "
      "decreases and pressure increases. However, downstream pressure never recovers completely to "
      "equal the pressure that existed upstream of the valve. The pressure differential (ΔP) across "
      "the valve is a measure of the amount of energy that was dissipated in the valve.")
    FIG(7, F5.fig_f5_07())
    P("Không kể đặc tính phục hồi của van, chênh áp đáng chú ý đối với bay hơi và xâm thực là chênh "
      "giữa đầu vào van và vena contracta. Nếu áp suất tại vena contracta giảm dưới áp suất hơi của "
      "chất lỏng thì bọt khí hình thành trong dòng. Nếu áp suất đầu ra vẫn dưới áp suất hơi, bọt tồn "
      "tại trong hệ thống hạ lưu và quá trình gọi là bay hơi. Bay hơi gây xói mòn nghiêm trọng cho trim, "
      "đặc trưng bởi bề mặt nhẵn bóng, thường mạnh nhất tại hoặc gần đường tiếp xúc giữa nút và vòng "
      "chỗ ngồi.",
      "Regardless of the recovery characteristics of the valve, the pressure differential of interest "
      "pertaining to flashing and cavitation is the differential between the valve inlet and the vena "
      "contracta. If pressure at the vena contracta should drop below the vapor pressure of the fluid, "
      "bubbles will form in the flow stream. If pressure at the valve outlet remains below the vapor "
      "pressure of the liquid, the bubbles will remain in the downstream system and the process is "
      "said to be flashing. Flashing can produce serious erosion damage to the valve trim parts and is "
      "characterized by a smooth, polished appearance of the eroded surface. Flashing is normally "
      "greatest at the point of highest velocity, which is usually at or near the seat line of the "
      "valve plug and seat ring.")
    FIG(8, F5.fig_f5_08())
    P("Mặt khác, nếu áp suất hạ lưu cao hơn áp suất hơi, bọt sẽ sụp hoặc nổ bên trong gây xâm thực. Sự "
      "sụp bọt giải phóng năng lượng và tạo tiếng ồn như sỏi chảy qua van. Nếu bọt sụp gần bề mặt rắn, "
      "năng lượng có thể xé toạc vật liệu để lại bề mặt thô ráp như xỉ. Xâm thực có thể lan sang đường "
      "ống hạ lưu nơi áp suất phục hồi. Van phục hồi cao dễ bị xâm thực hơn vì áp suất vena contracta "
      "thấp hơn và dễ chạm áp suất hơi hơn.",
      "On the other hand, if the downstream pressure is above the vapor pressure of the liquid, the "
      "bubbles will collapse, or implode, producing cavitation. Collapsing of the vapor bubbles "
      "releases energy and produces a noise similar to what one would expect if gravel were flowing "
      "through the valve. If the bubbles collapse in close proximity to solid surfaces in the valve, "
      "the energy released may tear away the material leaving a rough, cinderlike surface. Cavitation "
      "damage may extend to the adjacent downstream pipeline, if that is where pressure recovery "
      "occurs and the bubbles collapse. High-recovery valves tend to be more subject to cavitation, "
      "since the vena contracta pressure is lower and more likely to reach down to the liquid's vapor "
      "pressure.")

    H("5.14.2 Lựa chọn van cho dịch vụ bay hơi", "5.14.2 Valve Selection for Flashing Service", h3)
    P("Bay hơi xảy ra vì P2 nhỏ hơn Pv; P2 là áp suất hạ lưu, phụ thuộc vào quá trình và đường ống "
      "hạ lưu, còn Pv phụ thuộc vào chất lưu và nhiệt độ vận hành. Vì các biến xác định bay hơi không "
      "do van kiểm soát trực tiếp, không van nào ngăn được bay hơi. Giải pháp tốt nhất là chọn van có "
      "hình học và vật liệu phù hợp để tránh hoặc giảm thiểu hư hỏng.",
      "Flashing occurs because P2 is less than Pv. P2 is the pressure downstream of the valve and is "
      "a function of the downstream process and piping. Pv is a function of the fluid and operating "
      "temperature. Therefore, the variables that define flashing are not directly controlled by the "
      "valve. This further means there is no way for any control valve to prevent flashing. Since "
      "flashing cannot be prevented by the valve the best solution is to select a valve with proper "
      "geometry and materials to avoid or minimize damage.")
    B(["Ngăn hoặc giảm va chạm của hạt (giọt lỏng) với bề mặt van;",
       "Làm cứng bề mặt nhiều nhất có thể;",
       "Giảm vận tốc của dòng xói mòn."],
      ["Preventing or reducing the particle (liquid droplets in this case) impact with the valve surfaces;",
       "Making those surfaces as hard as possible;",
       "Lowering the velocity of the erosive flow."])
    P("Chọn van có ít thay đổi hướng dòng nhất để giảm số lần va chạm. Van góc thân trượt là giải pháp "
      "truyền thống; một số van quay như van nút lệch tâm và van bi đoạn cũng cho đường chảy thẳng. "
      "Van có vùng dòng giãn rộng sau chỗ tiết lưu làm giảm vận tốc xói mòn. Ở nơi chất lưu bắt buộc "
      "phải va vào bề mặt van, chẳng hạn bề mặt chỗ ngồi, chọn vật liệu cứng nhất có thể. Chất lưu vừa "
      "bay hơi vừa ăn mòn đặc biệt khó xử lý: nước bay hơi trong van thép gây ăn mòn thép rồi xói mòn "
      "lớp oxit mềm tạo thành, tổng hợp gây hư hỏng nặng hơn từng cơ chế riêng. Giải pháp là ngăn ăn "
      "mòn bằng cách chọn ít nhất thép hợp kim thấp.",
      "Selecting a valve with as few fluid directional changes as possible provides the least number "
      "of particle impacts. Sliding-stem angle valves are traditional solutions which provide such a "
      "flow path. Some rotary valves, such as eccentric rotary plug, and segmented ball valves, also "
      "offer straight-through flow paths. Valves with expanded flow areas downstream of the "
      "throttling point are beneficial because the erosive velocity is reduced. For those areas where "
      "the fluid must impact the valve surfaces, at the seating surfaces for example, choose materials "
      "that are as hard as possible. Generally the harder the material the longer it will resist "
      "erosion. Fluids that are both flashing and corrosive can be especially troublesome. Flashing "
      "water in a steel valve is an example of the synergistic result of both corrosion and erosion. "
      "The solution is to prevent the corrosion by selecting, as a minimum, a low-alloy steel.")

    H("5.14.3 Lựa chọn van cho dịch vụ xâm thực", "5.14.3 Valve Selection for Cavitation Service", h3)
    P("Xâm thực để lại bề mặt thô như xỉ, khác hẳn bề mặt nhẵn bóng do bay hơi. Xâm thực xảy ra khi áp "
      "suất vena contracta nhỏ hơn Pv và P2 lớn hơn Pv. Có thể xử lý bằng nhiều cách.",
      "Cavitation damage is characterized by a rough, cinder-like appearance of the eroded surface. It "
      "is distinctly different from the smooth, polished appearance caused by the erosion of flashing. "
      "Cavitation occurs when the vena contracta pressure is less than Pv, and P2 is greater than Pv. "
      "Cavitation can be treated by several means.")
    FIG(9, F5.fig_f5_09())
    P("Cách thứ nhất là loại bỏ xâm thực bằng quản lý sụt áp: nếu áp suất cục bộ không bao giờ giảm "
      "dưới áp suất hơi thì không có bọt để sụp. Muốn vậy, chia tổng sụt áp qua van thành các phần nhỏ "
      "hơn bằng trim nhiều cấp; mỗi phần giữ áp suất vena contracta trên áp suất hơi.",
      "The first is to eliminate the cavitation and thus the damage by managing the pressure drop. If "
      "the pressure drop across the valve can be controlled such that the local pressure never drops "
      "below the vapor pressure, then no vapor bubbles will form. To eliminate cavitation the total "
      "pressure drop across the valve is split, using multiple-stage trims, into smaller portions. "
      "Each of these small drops keeps its vena contracta pressure above the vapor pressure so no "
      "vapor bubbles are formed.")
    P("Cách thứ hai không loại bỏ xâm thực mà giảm thiểu hoặc cô lập hư hỏng, tương tự giải pháp bay "
      "hơi: cô lập xâm thực khỏi bề mặt van và làm cứng những bề mặt bị va chạm. Cách thứ ba là thay "
      "đổi hệ thống để ngăn nguyên nhân: nâng P2 đủ cao để áp suất vena contracta không giảm dưới áp "
      "suất hơi, tức van không còn bị nghẽn. Có thể nâng P2 bằng cách dời van đến vị trí có cột áp tĩnh "
      "lớn hơn ở phía hạ lưu, hoặc dùng tấm tiết lưu hay thiết bị áp suất ngược tương tự; nhược điểm "
      "là xâm thực có thể chuyển từ van sang tấm tiết lưu.",
      "The second method does not eliminate the cavitation but rather minimizes or isolates the damage "
      "much the same as with flashing solutions. This method aims to isolate the cavitation from valve "
      "surfaces and to harden those surfaces that the cavitation does impact. A third method is to "
      "change the system in a manner to prevent the causes of cavitation. If P2 can be raised enough "
      "so that the vena contracta pressure does not fall below the vapor pressure, that is the valve "
      "is no longer choked, then cavitation will be avoided. P2 can be raised by moving the valve to a "
      "location that has more static head on the downstream side. Applying an orifice plate or similar "
      "backpressure device can also raise P2 at the valve; the downside is the potential for the "
      "cavitation to transfer from the valve to the orifice plate.")

    # ------------------------------------------------------------ 5.15
    H("5.15 Dự báo tiếng ồn", "5.15 Noise Prediction")
    H("5.15.1 Tiếng ồn khí động học", "5.15.1 Aerodynamic", h3)
    P("Các nhà lãnh đạo ngành dùng tiêu chuẩn IEC 60534-8-3: Industrial-process control valves — Part "
      "8: Noise Considerations — Section 3: Control valve aerodynamic noise prediction method. "
      "Phương pháp này kết hợp lý thuyết nhiệt động, khí động học và dữ liệu thực nghiệm. Nó cho phép "
      "dự báo tiếng ồn dựa trên hình học đo được của van và điều kiện làm việc, đồng thời cho phép "
      "nhà cung cấp dùng dữ liệu đo trong phòng thí nghiệm để dự báo chính xác hơn. Nhờ cấu trúc phân "
      "tích này, phương pháp IEC cho phép đánh giá khách quan các phương án.",
      "Industry leaders use the International Electrotechnical Commission standard IEC 60534-8-3: "
      "Industrial-process control valves — Part 8: Noise Considerations — Section 3: Control valve "
      "aerodynamic noise prediction method. This method consists of a mix of thermodynamic and "
      "aerodynamic theory and empirical information. The design of the method allows a noise "
      "prediction for a valve based on the measurable geometry of the valve and the service conditions "
      "applied to the valve. The standard also allows valve vendors to use laboratory measured "
      "empirical data within the framework to provide more accurate predictions. Because of this "
      "analytical framework the IEC method allows an objective evaluation of alternatives.")
    P("Phương pháp mô tả hai nguồn ồn góp phần tạo nên tổng tiếng ồn của van: ồn trim và ồn ở đầu ra van. "
      "Ồn trim phụ thuộc vào kiểu trim và đặc điểm hình học; ồn đầu ra phụ thuộc vào diện tích đầu ra, "
      "số Mach tại đầu ra và bộ giãn nở phía hạ lưu. Có năm bước cơ bản; khi thích hợp phải thực hiện "
      "cho cả hai nguồn rồi cộng thành mức ồn tổng.",
      "The method describes two different noise sources that can contribute to the overall noise "
      "generated by the valve: trim noise and valve outlet noise. Trim noise is dependent on the type "
      "of trim and its geometric features. Valve outlet noise is dependent on the valve outlet area, "
      "valve outlet Mach number and any expander downstream of the valve. The method defines five "
      "basic steps; where applicable these need to be completed for both sources and combined into a "
      "total valve noise level.")
    O(["Tính tổng công suất dòng tại vena contracta. Công suất tiêu tán khi tiết lưu được tính từ dạng "
       "của phương trình động năng 1/2 mv², thay khối lượng bằng lưu lượng khối lượng; vận tốc là vận "
       "tốc vena contracta từ định luật 1 của nhiệt động học.",
       "Xác định phần công suất là công suất âm. Có năm chế độ xác định theo quan hệ giữa áp suất vena "
       "contracta và áp suất hạ lưu; mỗi chế độ có hiệu suất âm riêng. Hiệu suất âm thấp là một mục "
       "tiêu khi thiết kế van êm.",
       "Chuyển công suất âm thành phổ áp suất âm. Mục tiêu cuối là mức áp suất âm tại điểm tham chiếu "
       "bên ngoài van. Phổ tần số cho biết mức ồn ở từng tần số trong dải nghe được; dạng phổ được xác "
       "định từ hình học van, điều kiện dòng và phổ đặc trưng lý tưởng trong tiêu chuẩn.",
       "Tính suy hao truyền qua thành ống và biểu diễn lại phổ tại mặt ngoài của ống. Thành ống rung "
       "do tương tác với ồn trong chất lưu, rồi truyền ra ngoài và phát sóng âm; ba bước truyền này "
       "phụ thuộc tần số.",
       "Tính đến khoảng cách và tính mức áp suất âm tại vị trí người quan sát. Công suất âm không đổi "
       "nhưng mức áp suất âm giảm khi diện tích phân bố tăng theo khoảng cách."],
      ["Calculate the total stream power in the process at the vena contracta. The kinetic energy "
       "equation 1/2 mv² is used with mass flow rate substituted for mass; the velocity is the vena "
       "contracta velocity from the First Law of Thermodynamics.",
       "Determine the fraction of total power that is acoustic power. There are five defined regimes "
       "dependent on the relationship between vena contracta pressure and downstream pressure; each "
       "has an acoustic efficiency. Lower acoustic efficiency is one of the goals in designing a quiet "
       "valve.",
       "Convert acoustic power to sound pressure spectrum. The final goal is the sound pressure level "
       "at a reference point outside the valve. A sound pressure spectrum defines how much noise "
       "exists at each frequency in the audible range; its shape is determined from valve geometry, "
       "flow conditions and an ideal characteristic spectrum.",
       "Account for transmission loss of the pipe wall and restate the spectrum at the outside surface "
       "of the pipe. The pipe wall vibrates and transmits the noise to the atmosphere; these three "
       "transmission steps depend on frequency.",
       "Account for distance and calculate the sound pressure level at the observer's location. Sound "
       "power is constant but the associated sound pressure level decreases as the area over which "
       "power is spread increases."])
    EQ(r"W = \tfrac12\,\dot m\,v_{vc}^{2},\qquad L_p = \mathcal{F}(W,\;\eta,\;S(f),\;TL(f),\;r)", "11",
       "Công suất dòng W, lưu lượng khối lượng ṁ, vận tốc vena contracta v_vc, hiệu suất âm η, phổ S(f), "
       "suy hao truyền qua thành ống TL(f) và khoảng cách r.",
       "Stream power W, mass flow rate ṁ, vena contracta velocity v_vc, acoustic efficiency η, "
       "spectrum S(f), pipe transmission loss TL(f) and distance r.")

    H("5.15.2 Tiếng ồn thủy động", "5.15.2 Hydrodynamic", h3)
    P("Tiếng ồn thủy động đáng chú ý thường đi kèm xâm thực; cách mô tả truyền thống là «đá chảy trong "
      "ống». Các phương pháp dự báo hiện nay phân biệt một đặc tính ồn cho chất lỏng không nghẽn và "
      "một đặc tính cho dòng nghẽn có xâm thực. Có nhiều trường hợp chất lưu là hỗn hợp hai pha: hỗn "
      "hợp lỏng-khí tại đầu vào van, chất bay hơi hoặc chất có hiện tượng thoát khí khi tiết lưu. "
      "Phương pháp dự báo cho các trường hợp này chưa được thiết lập tốt; kết quả thử và khảo sát "
      "hiện trường cho thấy các mức ồn này không đóng góp đáng kể vào tiếng ồn chung của nhà máy cũng "
      "như không vượt mức phơi nhiễm của người lao động.",
      "Noticeable hydrodynamic noise is usually associated with cavitation. The traditional description "
      "of the sound is as rocks flowing inside the pipe. The various prediction methods account for "
      "one noise characteristic for liquids in non-choked flow situations and another in choked, "
      "cavitating flow situations. There are a variety of situations where the fluid is a two-phase "
      "mixture: liquid-gas two-phase fluids at the inlet of the valve, flashing fluids, and fluids "
      "that demonstrate outgassing due to throttling. Noise prediction methods for these cases are "
      "not yet well established. Test results and field surveys of installed multi-phase systems "
      "indicate these noise levels do not contribute to overall plant noise levels or exceed worker "
      "exposure levels.")
    FIG(10, F5.fig_f5_10())

    # ------------------------------------------------------------ 5.16
    H("5.16 Kiểm soát tiếng ồn", "5.16 Noise Control")
    P("Trong hệ thống kín (không xả ra khí quyển), mọi tiếng ồn phát sinh trong quá trình chỉ trở thành "
      "tiếng ồn trong không khí qua truyền dẫn qua van và đường ống bao quanh dòng chảy. Trường âm "
      "trong dòng bắt các ranh giới rắn rung; độ rung gây nhiễu loạn môi trường và lan truyền thành sóng "
      "âm. Kiểm soát tiếng ồn dùng xử lý tại nguồn, xử lý đường truyền hoặc cả hai.",
      "In closed systems (not vented to atmosphere), any noise produced in the process becomes airborne "
      "only by transmission through the valves and adjacent piping that contain the flowstream. The "
      "sound field in the flowstream forces these solid boundaries to vibrate. The vibrations cause "
      "disturbances in the ambient atmosphere that are propagated as sound waves. Noise control "
      "employs either source treatment, path treatment, or both.")
    P("Xử lý tại nguồn — ngăn hoặc làm suy giảm ồn ngay tại nguồn — là cách đáng mong muốn nhất nếu khả "
      "thi về kinh tế và kỹ thuật. Cách tiếp cận bằng lồng trim được khuyến nghị: lồng nhiều rãnh song "
      "song hẹp giảm nhiễu loạn và cho phân bố vận tốc thuận lợi trong vùng giãn nở, cho suy giảm 15 "
      "đến 20 dBA với ít hoặc không giảm năng lực. Trim hai cấp cho suy giảm tới 30 dBA khi tỷ lệ sụt "
      "áp ΔP/P1 cao.",
      "Source treatment, preventing or attenuating noise at its source, is the most desirable approach, "
      "if economically and physically feasible. Recommended cage-style source treatment approaches "
      "are depicted in Figure 5.10. The upper view shows a cage with many narrow parallel slots "
      "designed to minimize turbulence and provide a favorable velocity distribution in the expansion "
      "area. This economical approach can provide 15 to 20 dBA noise reduction with little or no "
      "decrease in flow capacity. The lower view shows a two-stage cage-style trim designed for "
      "optimum attenuation where pressure drop ratios (ΔP/P1) are high; this design can reduce valve "
      "noise by as much as 30 dBA.")
    P("Để đạt kết quả, các chỗ tiết lưu trên thành lồng chính phải được định cỡ và bố trí sao cho ồn "
      "do tương tác tia không lớn hơn tổng ồn của các tia riêng lẻ. Thiết kế cuối cùng kết hợp nhiều "
      "chiến lược giảm ồn, tới 40 dBA: hình dạng đường dẫn đặc biệt giảm chuyển công suất dòng thành "
      "công suất âm; giảm áp đa cấp chia công suất giữa các cấp; dịch phổ tần số để giảm năng lượng âm "
      "trong dải nghe được nhờ suy hao của đường ống; giữ các tia thoát độc lập tránh tái tạo ồn do hợp "
      "tia; quản lý vận tốc bằng diện tích giãn dần; và thiết kế thân bổ trợ tránh va chạm dòng vào "
      "thành thân.",
      "To obtain the desired results, restrictions must be sized and spaced in the primary cage wall "
      "so that the noise generated by jet interaction is not greater than the summation of the noise "
      "generated by the individual jets. The final design uses a combination of several noise "
      "reduction strategies to reduce valve noise up to 40 dBA: unique passage shape reduces the "
      "conversion of total stream power into noise power; multistage pressure reduction divides the "
      "stream power between stages and further reduces the acoustic conversion efficiency; frequency "
      "spectrum shifting reduces acoustic energy in the audible range by capitalizing on pipe "
      "transmission loss; exit jet independence is maintained to avoid noise regeneration due to jet "
      "coalescence; velocity management is accomplished with expanding areas; and complementary body "
      "designs prevent flow impingement on the body wall and secondary noise sources.")
    P("Ở tỷ lệ áp suất cao (ΔP/P1 > 0.8), cách mắc nối tiếp chia sụt áp giữa van điều khiển và một chỗ "
      "tiết lưu cố định (bộ khuếch tán) phía hạ lưu có thể hiệu quả. Để tối ưu, bộ khuếch tán phải "
      "được thiết kế riêng cho từng lắp đặt sao cho mức ồn do van và bộ khuếch tán bằng nhau (Hình 5.11). "
      "Hệ thống xả ra khí quyển thường rất ồn do tỷ lệ áp suất và vận tốc thoát cao. Chia sụt áp giữa "
      "cổng xả và van thượng lưu bằng bộ khuếch tán xả làm êm cả hai; tổ hợp đúng kích thước có thể "
      "giảm tiếng ồn hệ thống tới 40 dBA (Hình 5.12).",
      "For control valve applications operating at high pressure ratios (ΔP/P1 > 0.8) the series "
      "restriction approach, splitting the total pressure drop between the control valve and a fixed "
      "restriction (diffuser) downstream of the valve can be effective. To optimize the effectiveness "
      "of a diffuser, it must be designed for each given installation so that the noise levels "
      "generated by the valve and diffuser are equal (Figure 5.11). Control systems venting to "
      "atmosphere are generally very noisy because of high pressure ratios and high exit velocities. "
      "Dividing the total pressure drop between the actual vent and an upstream control valve by means "
      "of a vent diffuser quiets both the valve and the vent; a properly sized combination can reduce "
      "overall system noise as much as 40 dBA (Figure 5.12).")
    FIG(11, F5.fig_f5_11())
    FIG(12, F5.fig_f5_12())
    P("Xử lý tại nguồn cho van chất lỏng chủ yếu nhằm loại bỏ hoặc giảm thiểu xâm thực. Vì điều kiện "
      "gây xâm thực dự báo chính xác, ồn do xâm thực có thể triệt tiêu bằng cách áp giới hạn phù hợp "
      "cho điều kiện làm việc qua tấm tiết lưu phá áp, van mắc nối tiếp… Cách khác là dùng trim đặc "
      "biết theo nguyên lý tiết lưu nối tiếp để loại bỏ xâm thực (Hình 5.13).",
      "Source treatment for noise problems associated with control valves handling liquid is directed "
      "primarily at eliminating or minimizing cavitation. Because flow conditions that will produce "
      "cavitation can be accurately predicted, valve noise resulting from cavitation can be eliminated "
      "by application of appropriate limits to the service conditions at the valve by use of "
      "break-down orifices, valves in series, etc. Another approach is using special valve trim that "
      "uses the series restriction concept to eliminate cavitation as shown in Figure 5.13.")
    FIG(13, F5.fig_f5_13())
    P("Cách thứ hai là xử lý đường truyền: chất lưu là đường truyền ồn rất tốt, nên tăng trở kháng của "
      "đường truyền để giảm năng lượng âm tới người nhận. Tiêu tán năng lượng âm bằng vật liệu hấp thụ "
      "là một trong những phương pháp hiệu quả nhất; vật liệu nên đặt trong dòng tại hoặc ngay sau "
      "nguồn ồn. Trong hệ thống khí, bộ giảm thanh nối inline tiêu tán ồn trong dòng và làm giảm mức "
      "ồn truyền tới ranh giới rắn. Khi có lưu lượng khối lớn hoặc tỷ lệ áp suất cao, bộ giảm thanh "
      "inline là cách thực tế và kinh tế nhất; suy hao chèn thường giới hạn khoảng 25 dBA vì lý do "
      "chi phí.",
      "A second approach is path treatment. The fluid stream is an excellent noise transmission path. "
      "Path treatment consists of increasing the impedance of the transmission path to reduce the "
      "acoustic energy communicated to the receiver. Dissipation of acoustic energy by use of "
      "acoustical absorbent materials is one of the most effective methods; the material should be in "
      "the flow stream at or immediately downstream of the noise source. In gas systems, inline "
      "silencers effectively dissipate noise within the fluid stream and attenuate the noise level "
      "transmitted to the solid boundaries. Where high-mass flow rates and/or high pressure ratios "
      "exist, inline silencers are often the most realistic and economical approach. Absorption-type "
      "inline silencers can provide almost any degree of attenuation desired, but economic "
      "considerations generally limit insertion loss to approximately 25 dBA.")
    FIG(14, F5.fig_f5_14())
    P("Ồn không thể loại bỏ trong dòng phải xử lý bên ngoài: dùng ống thành dày, cách âm các ranh giới "
      "rắn lộ ra, hộp cách âm hoặc nhà bao kín để cô lập nguồn. Ống thành dày hoặc cách âm bên ngoài là "
      "kỹ thuật kinh tế và hiệu quả cho giảm ồn tại chỗ; tuy nhiên ồn lan truyền xa qua dòng chất lưu "
      "và hiệu quả của biện pháp kết thúc tại nơi biện pháp kết thúc.",
      "Noise that cannot be eliminated within the boundaries of the flow stream must be eliminated by "
      "external treatment: heavy walled piping, acoustical insulation of the exposed solid boundaries, "
      "insulated boxes or buildings to isolate the noise source. Path treatment such as heavy wall "
      "pipe or external acoustical insulation can be economical and effective for localized noise "
      "abatement. However, noise is propagated for long distances via the fluid stream and the "
      "effectiveness of the treatment ends where the treatment ends.")

    # ------------------------------------------------------------ 5.17
    H("5.17 Tóm tắt về tiếng ồn", "5.17 Noise Summary")
    P("Mức tiếng ồn do một lắp đặt van đề xuất có thể dự báo nhanh và hợp lý bằng các phương pháp "
      "tiêu chuẩn ngành, sẵn có trong phần mềm máy tính. Các công cụ định cỡ và dự báo ồn này giúp "
      "lựa chọn đúng thiết bị giảm ồn như Hình 5.15 và 5.16. Yêu cầu của cơ sở công nghiệp về tác động "
      "môi trường thấp sẽ tiếp tục thúc đẩy nhu cầu van điều khiển êm hơn; công nghệ dự báo và thiết "
      "kế van luôn được cải tiến. Liên hệ đại diện nhà sản xuất để biết thiết bị hoặc công nghệ mới nhất.",
      "The amount of noise that will be generated by a proposed control valve installation can be "
      "quickly and reasonably predicted by use of industry standard methods available in computer "
      "software. Such sizing and noise prediction tools help in the proper selection of noise reduction "
      "equipment such as shown in Figures 5.15 and 5.16. Process facility requirements for low "
      "environmental impact will continue to drive the need for quieter control valves. The prediction "
      "technologies and valve designs that deliver this are always being improved. For the latest in "
      "either equipment or prediction technology, contact the valve manufacturer's representative.")
    FIG(15, F5.fig_f5_15())
    FIG(16, F5.fig_f5_16())

    # ------------------------------------------------------------ 5.18
    H("5.18 Lựa chọn đệm kín", "5.18 Packing Selection")
    P("Các bảng và Hình 5.17, 5.18 đưa ra hướng dẫn lựa chọn đệm kín cho van thân trượt và van quay.",
      "The following tables and Figures 5.17 and 5.18 offer packing selection guidelines for "
      "sliding-stem and rotary valves.")
    FIG(17, F5.fig_f5_17())
    FIG(18, F5.fig_f5_18())

    H("5.18.1 Hướng dẫn lựa chọn đệm cho van thân trượt",
      "5.18.1 Packing Selection Guidelines for Sliding-Stem Valves", h3)
    TBL(["Hệ đệm / Packing system", "100 PPM: áp suất, nhiệt độ",
         "Không môi trường: áp suất, nhiệt độ"],
        [("PTFE V-Ring đơn", "20.7 bar, -18 đến 93°C / 300 psi, 0 đến 200°F",
          "Xem Hình 5.15, -46 đến 232°C / -50 đến 450°F"),
         ("PTFE V-Ring đôi", "—", "Xem Hình 5.15, -46 đến 232°C / -50 đến 450°F"),
         ("ENVIRO-SEAL PTFE", "Xem Hình 5.14, -46 đến 232°C / -50 đến 450°F",
          "Xem Hình 5.15, -46 đến 232°C / -50 đến 450°F"),
         ("ENVIRO-SEAL Duplex", "51.7 bar, -46 đến 232°C / 750 psi, -50 đến 450°F",
          "Xem Hình 5.15, -46 đến 232°C / -50 đến 450°F"),
         ("ENVIRO-SEAL H2 Duplex", "138 bar, -46 đến 149°C / 2000 psi, -50 đến 300°F",
          "330 bar, -46 đến 149°C / 4800 psi, -50 đến 300°F"),
         ("KALREZ với Vespel CR-6100 (K-VSP 500)",
          "24.1 bar, 4 đến 260°C / 350 psig, 40 đến 500°F",
          "Xem Hình 5.15, -40 đến 260°C / -40 đến 500°F"),
         ("ENVIRO-SEAL Graphite ULF", "103 bar, -7 đến 315°C / 1500 psi, 20 đến 600°F",
          "207 bar, -198 đến 371°C / 3000 psi, -325 đến 700°F"),
         ("HIGH-SEAL Graphite ULF", "103 bar, -7 đến 315°C / 1500 psi, 20 đến 600°F",
          "290 bar(4), -198 đến 538°C / 4200 psi(4), -325 đến 1000°F"),
         ("Graphite Composite / HIGH-SEAL Graphite", "—",
          "290 bar(4), -198 đến 649°C / 4200 psi(4), -325 đến 1200°F"),
         ("Braided Graphite Filament", "—", "290 bar, -198 đến 538°C(5) / 4200 psi, -325 đến 1000°F(5)"),
         ("Graphite ULF", "—", "290 bar, -198 đến 538°C / 4200 psi, -325 đến 1000°F")],
        "Giá trị chỉ là hướng dẫn; nhiệt độ áp dụng cho chính đệm, không phải nhiệt độ quá trình. "
        "(4) trừ thân 9.5 mm (3/8 inch): 110 bar (1600 psi). (5) trừ dịch vụ oxy hóa: -198 đến 371°C. "
        "Values are guidelines only; (4) except 3/8 in stem: 110 bar; (5) except oxidizing service.")
    TBL(["Hệ đệm / Packing system", "Chỉ số làm kín", "Tuổi thọ", "Ma sát"],
        [("PTFE V-Ring đơn", "Better", "Long", "Very low"),
         ("PTFE V-Ring đôi", "Better", "Long", "Low"),
         ("ENVIRO-SEAL PTFE", "Best", "Very long", "Low"),
         ("ENVIRO-SEAL Duplex", "Best", "Very long", "Low"),
         ("ENVIRO-SEAL H2 Duplex", "Best", "Very long", "Medium"),
         ("KALREZ với Vespel CR 6100", "Best", "Long", "Low"),
         ("ENVIRO-SEAL Graphite ULF", "Best", "Very long", "Medium"),
         ("HIGH-SEAL Graphite ULF", "Best", "Very long", "Medium"),
         ("Graphite Composite / HIGH-SEAL Graphite", "Better", "Very long", "Very high"),
         ("Braided Graphite Filament", "Good", "Moderate", "High"),
         ("Graphite ULF", "Better", "Very long", "Medium")],
        "Chỉ số hiệu năng đệm thân trượt / Sliding-stem packing performance index.")

    H("5.18.2 Hướng dẫn lựa chọn đệm cho van quay",
      "5.18.2 Packing Selection Guidelines for Rotary Valves", h3)
    TBL(["Hệ đệm / Packing system", "100 PPM", "Không môi trường"],
        [("PTFE V-Ring đơn", "—", "103 bar, -46 đến 232°C / 1500 psig, -50 đến 450°F"),
         ("ENVIRO-SEAL PTFE", "103 bar, -46 đến 232°C / 1500 psig, -50 đến 450°F",
          "207 bar, -46 đến 232°C / 3000 psig, -50 đến 450°F"),
         ("PTFE nạp tải cho van V250", "69 bar, -29 đến 93°C / 1000 psig, -20 đến 200°F",
          "155 bar, -46 đến 232°C / 2250 psig, -50 đến 450°F"),
         ("KALREZ với Vespel CR 6100 (KVSP 500)", "24.1 bar, 4 đến 260°C / 350 psig, 40 đến 500°F",
          "51 bar, -40 đến 260°C / 750 psig, -40 đến 500°F"),
         ("ENVIRO-SEAL Graphite", "103 bar, -7 đến 315°C / 1500 psig, 20 đến 600°F",
          "207 bar, -198 đến 371°C / 3000 psig, -325 đến 700°F"),
         ("Graphite Ribbon", "—", "103 bar, -198 đến 538°C(2) / 1500 psig, -325 đến 1000°F(2)")],
        "(2) trừ dịch vụ oxy hóa: -198 đến 371°C / except oxidizing service: -198 to 371°C.")
    TBL(["Hệ đệm / Packing system", "Chỉ số làm kín", "Tuổi thọ", "Ma sát"],
        [("PTFE V-Ring đơn", "Better", "Long", "Very low"),
         ("ENVIRO-SEAL PTFE", "Excellent", "Very long", "Low"),
         ("PTFE nạp tải cho van V250", "Excellent", "Very long", "Low"),
         ("KALREZ với Vespel CR-6100", "Excellent", "Long", "Very low"),
         ("ENVIRO-SEAL Graphite", "Excellent", "Very long", "Moderate"),
         ("Graphite Ribbon", "Acceptable", "Acceptable", "High")],
        "Chỉ số hiệu năng đệm van quay / Rotary packing performance index.")

    # ------------------------------------------------------------ 5.19
    H("5.19 Vật liệu thân van", "5.19 Valve Body Materials")
    P("Lựa chọn vật liệu thân thường dựa trên áp suất, nhiệt độ và tính ăn mòn, xói mòn của dòng chảy. "
      "Đôi khi phải thỏa hiệp: vật liệu chống xói mòn tốt có thể không đạt vì chống ăn mòn kém với một "
      "chất lưu cụ thể. Một số điều kiện đòi hợp kim và kim loại đặc biệt đắt hơn nhiều so với kim loại "
      "thông thường, nên kinh tế cũng là yếu tố. May mắn là đa số ứng dụng xử lý chất tương đối không "
      "ăn mòn ở áp suất và nhiệt độ hợp lý, nên thép cacbon đúc là vật liệu thân phổ biến nhất với chi "
      "phí thấp hơn nhiều.",
      "Body material selection is usually based on the pressure, temperature, corrosive properties, and "
      "erosive properties of the flow media. Sometimes a compromise must be reached. Some service "
      "conditions require exotic alloys and metals which are much more expensive than common metals, "
      "so economy may also be a factor. Fortunately, the majority of control valve applications "
      "handle relatively non-corrosive fluids at reasonable pressures and temperatures. Therefore, "
      "cast carbon steel is the most commonly used valve body material and can provide satisfactory "
      "service at much lower cost than the exotic alloy materials.")
    P("Các quy định đã được xây dựng để đặt hàng vật đúc hợp kim cao chống ăn mòn mạnh, giải quyết các "
      "vấn đề như khả năng chống ăn mòn kém hơn vật gia công, khó hàn và thời gian giao hàng dài. Các "
      "quy định này gồm đánh giá xưởng đúc, thiết bị khuôn riêng, đánh giá hợp kim khuôn, đánh giá nhiệt "
      "và kiểm soát chi tiết nguyên liệu, kiểm tra trực quan, sửa chữa bằng hàn, xử lý nhiệt và kiểm tra "
      "không phá hủy.",
      "Specifications have been developed for ordering highly corrosion-resistant, high-alloy castings. "
      "These problems included unacceptable corrosion resistance compared to wrought materials, "
      "weldability issues, and unacceptable lead times. These alloys are also difficult to cast. The "
      "specifications include a foundry qualification process, dedicated pattern equipment, pattern "
      "alloy qualification, heat qualification, and detailed controls on raw material, visual "
      "inspection, weld repairs, heat treatment, and non-destructive testing.")
    P("Thép cacbon đúc ASTM A216 WCC là vật liệu phổ biến cho dịch vụ vừa phải như không khí, hơi bão "
      "hòa hoặc quá nhiệt, chất lỏng và khí không ăn mòn; không dùng trên 425°C (800°F) vì pha giàu "
      "cacbon có thể chuyển thành graphit. Thép Cr-Mo ASTM A217 WC9 là cấp đúc chuẩn, thay C5 nhờ đặc "
      "tính đúc và hàn tốt hơn, dùng tới 595°C (1100°F) cho hơi và nước cấp lò hơi. Thép không gỉ ASTM "
      "A351 CF3 (304L) thường dùng cho axit nitric; không xếp hạng cho bộ phận chịu áp trên 425°C. CF8M "
      "(316) là vật liệu chuẩn trong ngành, chống ăn mòn, rỗ, biến dạng chậm và chất oxy hóa tốt hơn 304, dải "
      "nhiệt -254°C (-425°F) đến 816°C (1500°F). CG8M (317) có thêm 1% niken và molypden, chống rỗ tốt "
      "hơn, chứa 15 đến 35% ferrit nên từ tính một phần đến mạnh, giới hạn 538°C cho bộ phận chịu áp.",
      "Cast carbon steel ASTM A216 WCC is the most popular cast steel for moderate services such as air, "
      "saturated or superheated steam, non-corrosive liquids and gases; it is not used above 425°C "
      "(800°F) as the carbon rich phase might be converted to graphite. Cast Cr-Mo steel ASTM A217 WC9 "
      "is the standard cast grade, having replaced C5 because of superior casting and welding "
      "properties; the chromium and molybdenum provide erosion-corrosion and creep resistance, making "
      "it useful to 595°C (1100°F). Cast Type 304L stainless steel ASTM A351 CF3 is common for nitric "
      "acid and certain chemical service; CF3 is not rated above 425°C. Cast Type 316 ASTM A351 CF8M is "
      "the industry standard, with greater resistance to corrosion, pitting, creep and oxidizing fluids "
      "than 304, and the widest temperature range: -254°C (-425°F) to 816°C (1500°F). Cast Type 317 "
      "CG8M has nickel and molybdenum increased 1% each, gives greater pitting resistance, contains 15 "
      "to 35% ferrite and is partly to strongly magnetic; maximum temperature for pressure-retaining "
      "parts is 538°C.")
    P("Dùng đúng ký hiệu ASTM được coi là thói quen tốt và được khuyến khích, đặc biệt cho bộ phận chịu "
      "áp. Thêm dữ liệu kỹ thuật về các vật liệu này ở Chương 13.",
      "Use of proper ASTM designations is considered good practice and is encouraged in specifying "
      "materials, particularly for pressure-containing parts. Additional engineering data on these "
      "materials is included in Chapter 13.")

    H("5.19.1 Ký hiệu vật liệu thân van thường gặp",
      "5.19.1 Designations for Common Valve Body Materials", h3)
    TBL(["Ký hiệu đúc / Casting", "Tên chung / Generic", "UNS tương đương wrought"],
        [("CD3MN", "Duplex tiêu chuẩn / Standard duplex", "S31803, S32205"),
         ("CD3MWCuN", "Super duplex", "S32760"),
         ("CF3", "304L", "S30403"), ("CF8", "304", "S30400"),
         ("CF3M", "316L", "S31603"), ("CF8M", "316", "S31600"),
         ("CG3M", "317L", "S31703"), ("CG8M", "317", "S31700"),
         ("CK3MCuN", "Alloy 254 SMO", "S31254"),
         ("CN7M", "Alloy 20Cb3", "N08020"),
         ("CU5MCuC", "Alloy 825", "N08825"),
         ("CW12MW", "Alloy C (lỗi thời / obsolete)", "N10002"),
         ("CW2M", "Alloy C", "N10276, N06455"),
         ("CX2MW", "Alloy C22", "N06022"),
         ("CW6MC", "Alloy 625", "N06625"),
         ("CX2M", "Alloy 59", "N06059"),
         ("CY40", "Alloy 600", "N06600"),
         ("CZ100", "Nickel Alloy 200", "N02200"),
         ("LCB", "LCB", "J03003"), ("LCC", "LCC", "J02505"),
         ("M35-1", "Alloy 400", "N04400"),
         ("N12MV", "Alloy B", "N10001"),
         ("N7M", "Alloy B2", "N10665"),
         ("WCB", "WCB", "J03002"), ("WCC", "WCC", "J02503"),
         ("Titanium C3", "C3", "R50550"),
         ("Zirconium 702C", "702C", "R60702"),
         ("Zirconium 705C", "705C", "R60705")],
        "Ký hiệu đúc, tên chung và số UNS / Casting designations, generic designations and UNS numbers.")

    # ------------------------------------------------------------ 5.20
    H("5.20 Xếp hạng áp suất-nhiệt độ", "5.20 Pressure-Temperature Ratings")
    P("Các bảng sau theo ASME B16.34-2013. Giá trị bar và psig được giữ nguyên theo bản in.",
      "The following tables are in accordance with ASME B16.34-2013. Bar and psig values are kept as "
      "printed.")

    H("5.20.1 Van đúc ASTM A216 WCC, Class tiêu chuẩn",
      "5.20.1 Pressure-Temperature Ratings for Standard Class ASTM A216 Grade WCC Cast Valves", h3)
    TBL(["°C", "Cl150 bar", "Cl300", "Cl600", "Cl900", "Cl1500"],
        [("-29 đến 38", "19.8", "51.7", "103.4", "155.1", "258.6"),
         ("50", "19.5", "51.7", "103.4", "155.1", "258.6"),
         ("100", "17.7", "51.5", "103.0", "154.6", "257.6"),
         ("150", "15.8", "50.2", "100.3", "150.5", "250.8"),
         ("200", "13.8", "48.6", "97.2", "145.8", "243.2"),
         ("250", "12.1", "46.3", "92.7", "139.0", "231.8"),
         ("325", "9.3", "41.4", "82.6", "124.0", "206.6"),
         ("350", "8.4", "40.0", "80.0", "120.1", "200.1"),
         ("375", "7.4", "37.8", "75.7", "113.5", "189.2"),
         ("400", "6.5", "34.7", "69.4", "104.2", "173.6"),
         ("425", "5.5", "28.8", "57.5", "86.3", "143.8")],
        "WCC — bar theo °C / bar by °C.")
    TBL(["°F", "Cl150 psig", "Cl300", "Cl600", "Cl900", "Cl1500"],
        [("-20 đến 100", "290", "750", "1,500", "2,250", "3,750"),
         ("200", "260", "750", "1,500", "2,250", "3,750"),
         ("300", "230", "730", "1,455", "2,185", "3,640"),
         ("400", "200", "705", "1,405", "2,110", "3,520"),
         ("500", "170", "665", "1,330", "1,995", "3,325"),
         ("600", "140", "605", "1,210", "1,815", "3,025"),
         ("650", "125", "590", "1,175", "1,765", "2,940"),
         ("700", "110", "555", "1,110", "1,665", "2,775"),
         ("750", "95", "505", "1,015", "1,520", "2,535"),
         ("800", "80", "410", "825", "1,235", "2,055")],
        "WCC — psig theo °F / psig by °F.")

    H("5.20.2 Van đúc ASTM A217 WC9, Class tiêu chuẩn",
      "5.20.2 Pressure-Temperature Ratings for Standard Class ASTM A217 Grade WC9 Cast Valves", h3)
    TBL(["°C", "Cl150 bar", "Cl300", "Cl600", "Cl900", "Cl1500"],
        [("-29 đến 38", "19.8", "51.7", "103.4", "155.1", "258.6"),
         ("50", "19.5", "51.7", "103.4", "155.1", "258.6"),
         ("100", "17.7", "51.5", "103.0", "154.6", "257.6"),
         ("150", "15.8", "50.3", "100.3", "150.6", "250.8"),
         ("200", "13.8", "48.6", "97.2", "145.8", "243.4"),
         ("250", "12.1", "46.3", "92.7", "139.0", "321.8"),
         ("300", "10.2", "42.9", "85.7", "128.6", "214.4"),
         ("325", "9.3", "41.4", "82.6", "124.0", "206.6"),
         ("350", "8.4", "40.3", "80.4", "120.7", "201.1"),
         ("375", "7.4", "38.9", "77.6", "116.5", "194.1"),
         ("400", "6.5", "36.5", "73.3", "109.8", "183.1"),
         ("425", "5.5", "35.2", "70.0", "105.1", "175.1"),
         ("450", "4.6", "33.7", "67.7", "101.4", "169.0"),
         ("475", "3.7", "31.7", "63.4", "95.1", "158.2"),
         ("500", "2.8", "28.2", "56.5", "84.7", "140.9"),
         ("538", "1.4", "18.4", "36.9", "55.3", "92.2")],
        "WC9 — bar; giá trị 321.8 tại 250°C được giữ nguyên theo bản in / the 321.8 value at 250°C is kept.")
    TBL(["°F", "Cl150 psig", "Cl300", "Cl600", "Cl900", "Cl1500"],
        [("-20 đến 100", "290", "750", "1,500", "2,250", "3,750"),
         ("200", "260", "750", "1,500", "2,250", "3,750"),
         ("300", "230", "730", "1,455", "2,185", "3,640"),
         ("400", "200", "705", "1,410", "2,115", "3,530"),
         ("500", "170", "665", "1,330", "1,995", "3,325"),
         ("600", "140", "605", "1,210", "1,815", "3,025"),
         ("650", "125", "590", "1,175", "1,765", "2,940"),
         ("700", "110", "570", "1,135", "1,705", "2,840"),
         ("750", "95", "530", "1,065", "1,595", "2,660"),
         ("800", "80", "510", "1,015", "1,525", "2,540"),
         ("850", "65", "485", "975", "1,460", "2,435"),
         ("900", "50", "450", "900", "1,350", "2,245"),
         ("950", "35", "385", "755", "1,160", "1,930"),
         ("1000", "20", "265", "535", "800", "1,335"),
         ("1050", "20 (1)", "175", "350", "525", "875"),
         ("1100", "20 (1)", "110", "220", "330", "550")],
        "WC9 — psig; (1) xếp hạng đầu bích kết thúc tại 538°C (1000°F) / flanged end ratings terminate at 538°C.")

    H("5.20.3 Van đúc ASTM A351 CF3, Class tiêu chuẩn",
      "5.20.3 Pressure-Temperature Ratings for Standard Class ASTM A351 Grade CF3 Cast Valves", h3)
    TBL(["°C", "Cl150 bar", "Cl300", "Cl600", "Cl900", "Cl1500"],
        [("-29 đến 38", "19.0", "49.6", "99.3", "148.9", "248.2"),
         ("50", "18.3", "47.8", "95.6", "143.5", "239.1"),
         ("100", "15.7", "40.9", "81.7", "122.6", "204.3"),
         ("150", "14.2", "37.0", "74.0", "111.0", "185.0"),
         ("200", "13.2", "34.5", "69.0", "103.4", "172.4"),
         ("250", "12.1", "32.5", "65.0", "97.5", "162.4"),
         ("325", "9.3", "30.2", "60.4", "90.7", "151.1"),
         ("350", "8.4", "29.6", "59.3", "88.9", "148.1"),
         ("375", "7.4", "29.0", "58.1", "87.1", "145.2"),
         ("400", "6.5", "28.4", "56.9", "85.3", "142.2"),
         ("425", "5.5", "28.0", "56.0", "84.0", "140.0")],
        "CF3 — bar theo °C / bar by °C.")
    TBL(["°F", "Cl150 psig", "Cl300", "Cl600", "Cl900", "Cl1500"],
        [("-20 đến 100", "275", "720", "1,440", "2,160", "3,600"),
         ("200", "230", "600", "1,200", "1,800", "3,000"),
         ("300", "205", "540", "1,075", "1,615", "2,690"),
         ("400", "190", "495", "995", "1,490", "2,485"),
         ("500", "170", "465", "930", "1,395", "2,330"),
         ("600", "140", "440", "885", "1,325", "2,210"),
         ("650", "125", "430", "865", "1,295", "2,160"),
         ("700", "110", "420", "845", "1,265", "2,110"),
         ("750", "95", "415", "825", "1,240", "2,065"),
         ("800", "80", "405", "810", "1,215", "2,030")],
        "CF3 — psig theo °F / psig by °F.")

    H("5.20.4 Van đúc ASTM A351 CF8M và CG8M, Class tiêu chuẩn",
      "5.20.4 Pressure-Temperature Ratings for Standard Class ASTM A351 Grades CF8M and CG8M Cast Valves", h3)
    TBL(["°C", "Cl150 bar", "Cl300", "Cl600", "Cl900", "Cl1500"],
        [("-29 đến 38", "19.0", "49.6", "99.3", "148.9", "248.2"),
         ("50", "18.4", "48.1", "96.2", "144.3", "240.6"),
         ("100", "16.2", "42.2", "84.4", "126.6", "211.0"),
         ("150", "14.8", "38.5", "77.0", "115.5", "192.5"),
         ("200", "13.7", "35.7", "71.3", "107.0", "178.3"),
         ("250", "12.1", "33.4", "66.8", "100.1", "166.9"),
         ("300", "10.2", "31.6", "63.2", "94.9", "158.1"),
         ("325", "9.3", "30.9", "61.8", "92.7", "154.4"),
         ("350", "8.4", "30.3", "60.7", "91.0", "151.6"),
         ("375", "7.4", "29.9", "59.8", "89.6", "149.4"),
         ("400", "6.5", "29.4", "58.9", "88.3", "147.2"),
         ("425", "5.5", "29.1", "58.3", "87.4", "145.7"),
         ("450", "4.6", "28.8", "57.7", "86.5", "144.2"),
         ("475", "3.7", "28.7", "57.3", "86.0", "143.4"),
         ("500", "2.8", "28.2", "56.5", "84.7", "140.9"),
         ("538", "1.4", "25.2", "50.0", "75.2", "125.5"),
         ("550", "1.4(2)", "25.0", "49.8", "74.8", "124.9"),
         ("575", "1.4(2)", "24.0", "47.9", "71.8", "119.7"),
         ("600", "1.4(2)", "19.9", "39.8", "59.7", "99.5"),
         ("625", "1.4(2)", "15.8", "31.6", "47.4", "79.1"),
         ("650", "1.4(2)", "12.7", "25.3", "38.0", "63.3"),
         ("675", "1.4(2)", "10.3", "20.6", "31.0", "51.6"),
         ("700", "1.4(2)", "8.4", "16.8", "25.1", "41.9"),
         ("725", "1.4(2)", "7.0", "14.0", "21.0", "34.9"),
         ("750", "1.4(2)", "5.9", "11.7", "17.6", "29.3"),
         ("775", "1.4(2)", "4.6", "9.0", "13.7", "22.8"),
         ("800", "1.2(2)", "3.5", "7.0", "10.5", "17.4"),
         ("816", "1.0(2)", "2.8", "5.9", "8.6", "14.1")],
        "CF8M/CG8M — bar; CG8M giới hạn 538°C; (2) xếp hạng đầu bích CF8M kết thúc tại 538°C / "
        "CG8M limited to 538°C; CF8M flanged end ratings terminate at 538°C.")
    TBL(["°F", "Cl150 psig", "Cl300", "Cl600", "Cl900", "Cl1500"],
        [("-20 đến 100", "275", "720", "1,440", "2,160", "3,600"),
         ("200", "235", "620", "1,240", "1,860", "3,095"),
         ("300", "215", "560", "1,120", "1,680", "2,795"),
         ("400", "195", "515", "1,025", "1,540", "2,570"),
         ("500", "170", "480", "955", "1,435", "2,390"),
         ("600", "140", "450", "900", "1,355", "2,255"),
         ("650", "125", "440", "885", "1,325", "2,210"),
         ("700", "110", "435", "870", "1,305", "2,170"),
         ("750", "95", "425", "855", "1,280", "2,135"),
         ("800", "80", "420", "845", "1,265", "2,110"),
         ("850", "65", "420", "835", "1,255", "2,090"),
         ("900", "50", "415", "830", "1,245", "2,075"),
         ("950", "35", "385", "775", "1,160", "1,930"),
         ("1000", "20", "365", "725", "1,090", "1,820"),
         ("1050", "20", "360", "720", "1,080", "1,800"),
         ("1100", "20(2)", "305", "610", "915", "1,525"),
         ("1150", "20(2)", "235", "475", "710", "1,185"),
         ("1200", "20(2)", "185", "370", "555", "925"),
         ("1250", "20(2)", "145", "295", "440", "735"),
         ("1300", "20(2)", "115", "235", "350", "585"),
         ("1350", "20(2)", "95", "190", "290", "480"),
         ("1400", "20(2)", "75", "150", "225", "380"),
         ("1450", "20(2)", "60", "115", "175", "290"),
         ("1500", "15(2)", "40", "85", "125", "205")],
        "CF8M/CG8M — psig theo °F / psig by °F.")

    # ------------------------------------------------------------ 5.21
    H("5.21 Viết tắt vật liệu phi kim", "5.21 Non-Metallic Material Abbreviations")
    TBL(["Ký hiệu ASTM và tên thương mại", "Mô tả chung / Generic description"],
        [("CR", "Chloroprene"),
         ("EPDM", "Ethylene propylene terpolymer"),
         ("FFKM, Kalrez(1), Chemraz(2)", "Perfluoroelastomer"),
         ("FKM, Viton(1)", "Fluoroelastomer"),
         ("FVMQ", "Fluorosilicone"),
         ("NBR", "Nitrile"),
         ("NR", "Natural rubber"),
         ("PUR", "Polyurethane"),
         ("VMQ", "Silicone"),
         ("PEEK", "Polyetheretherketone"),
         ("PTFE", "Polytetrafluoroethylene"),
         ("PTFE, Carbon Filled", "Polytetrafluoroethylene, carbon filled"),
         ("PTFE, Glass Filled", "Polytetrafluoroethylene, glass filled"),
         ("TCM Plus(3)", "Mineral and MoS2 filled PTFE"),
         ("TCM Ultra(3)", "PEEK and MoS2 filled PTFE"),
         ("Composition Gasket", "Composite Gasket"),
         ("Flexible Graphite, Grafoil(4)", "Flexible Graphite")],
        "(1) nhãn hiệu của DuPont Performance Elastomers; (2) Greene, Tweed &amp; Co.; (3) Fisher Controls "
        "International LLC; (4) GrafTech Intl. / registered trademarks as noted in the source.")

    # ------------------------------------------------------------ 5.22
    H("5.22 Quy trình kiểm tra không phá hủy", "5.22 Non-Destructive Test Procedures")
    P("Kiểm tra không phá hủy thành công là yêu cầu đối với van dùng trong dịch vụ hạt nhân và có thể "
      "do quy phạm hoặc khách hàng yêu cầu trong ứng dụng phi hạt nhân, đặc biệt trong ngành điện. Việc "
      "đạt kiểm tra cũng có thể cho phép nâng cấp van đầu hàn giáp môi Class tiêu chuẩn lên xếp hạng "
      "Special Class, cho phép dùng ở áp suất cao hơn; thủ tục nâng cấp được quy định trong ASME B16.34. "
      "Dưới đây là nguyên tắc và thủ tục của bốn loại kiểm tra chính theo ANSI, ASME và ASTM.",
      "Successful completion of specific non-destructive examinations is required for valves intended "
      "for nuclear service and may be required by codes or customers in non-nuclear applications, "
      "particularly in the power industry. Successful completion may also permit uprating of ASME "
      "Standard Class butt welded-end valves to a Special Class rating, allowing higher pressures; the "
      "procedures are detailed in ASME Standard B16.34. The principles and procedures of four major "
      "types of non-destructive examinations defined in ANSI, ASME, and ASTM standards are summarized "
      "below.")
    H("5.22.1 Kiểm tra hạt từ tính (bề mặt)", "5.22.1 Magnetic Particle (Surface) Examination", h3)
    P("Chỉ dùng được cho vật liệu có thể từ hóa. Cho dòng điện chạy qua chi tiết để tạo từ trường; khuyết "
      "tật bề mặt hoặc cạn làm méo từ trường và tạo từ trường thứ cấp quanh khuyết. Rắc bột từ khô hoặc "
      "lơ lửng trong chất lỏng lên bề mặt sẽ thấy vùng méo. Sau khi khử từ bằng cách đảo chiều dòng điện, "
      "có thể hàn sửa hoặc phải thay thế chi tiết; sau sửa chữa hoặc thay thế phải kiểm tra lại.",
      "Magnetic particle examination can be used only on materials which can be magnetized. A direct "
      "current is applied to induce a magnetic field. Surface or shallow subsurface defects distort "
      "the field so that a secondary field develops around the defect. Magnetic powder, dry or "
      "suspended in liquid, reveals the distorted areas. After de-magnetizing by reversing the current, "
      "the indication may be weld repaired or the piece replaced; after repair or replacement the "
      "examination must be repeated.")
    H("5.22.2 Kiểm tra thấm ngấm (bề mặt)", "5.22.2 Liquid Penetrant (Surface) Examination", h3)
    P("Phương pháp này phát hiện chỉ báo bề mặt không thấy bằng mắt thường. Bề mặt được làm sạch và phơi "
      "khô; thuốc thấm (rửa được bằng nước hoặc tẩy được bằng dung môi) được nhúng, quét hoặc phun rồi "
      "để thấm. Phần thừa được rửa hoặc lau, bề mặt phơi khô lại và chất hiện hình (lỏng hoặc bột) được "
      "phủ lên. Kiểm tra dưới nguồn sáng thích hợp; một số chất hiện hình cần tia cực tím hoặc đèn đen. "
      "Nếu phát hiện khuyết tật và hàn sửa, phải kiểm tra lại sau sửa chữa.",
      "This examination method permits detection of surface indications not visible to the naked eye. "
      "The surface is cleaned thoroughly and dried. Liquid penetrant dye, water washable or solvent "
      "removable, is applied by dipping, brushing, or spraying and allowed time to penetrate. Excess "
      "penetrant is washed or wiped off, the surface is dried again and a developer (liquid or powder) "
      "is applied. Inspection is performed under the applicable light source; some developers require "
      "ultraviolet or black light to expose defective areas. If defects are discovered and repaired by "
      "welding, the piece must be re-examined after repair.")
    H("5.22.3 Kiểm tra chiếu X (thể tích)", "5.22.3 Radiographic (Volumetric) Examination", h3)
    P("Tia X và tia gamma đi qua vật kim loại không cho ánh sáng nhìn thấy xuyên qua và phơi sáng phim hoặc cảm "
      "biến kỹ thuật số. Số lượng và cường độ tia phụ thuộc mật độ vật liệu; khuyết tật dưới bề mặt làm "
      "thay đổi mật độ nên phát hiện được. Vật cần kiểm tra đặt giữa nguồn tia và phim. Độ chi tiết và "
      "độ nhạy tương phản được xác định bằng cách chiếu đồng thời một hoặc nhiều tấm phẳng mỏng gọi là "
      "penetrameter có khoan lỗ đường kính quy định. Chụp X-quang phát hiện khuyết như bọt khí, lỗ do "
      "khí, tạp chất cát, co ngót bên trong, vết nứt, vết rách nóng và xỉ. Với vật đúc hạt nhân, một số "
      "khuyết như nứt và rách nóng bị cấm và không được sửa. Thẩm quyền và kinh nghiệm của người chụp "
      "rất quan trọng vì phải so sánh với tiêu chuẩn chấp nhận (ASTM reference radiographs). Khi cần "
      "hàn sửa, phải chụp lại sau sửa chữa.",
      "Radiography works on the principle that X-rays and gamma rays pass through metal objects "
      "impervious to visible light and expose photographic film or digital X-ray sensors. The number "
      "and intensity of rays depend on material density; sub-surface defects change density and can "
      "therefore be detected. The piece is placed between the source and the film. Detail and contrast "
      "sensitivity are determined by radiographing small flat plates of specified thickness with "
      "holes of specified diameters, called a penetrameter, at the same time. Radiography can detect "
      "gas and blowholes, sand inclusions, internal shrinkage, cracks, hot tears, and slag inclusions. "
      "In castings for nuclear service, some defects such as cracks and hot tears are expressly "
      "forbidden and cannot be repaired. The judgment and experience of the radiographers is "
      "important because they must compare the radiograph with the acceptance criteria (ASTM reference "
      "radiographs). When weld repairs are required, the casting must be radiographed again.")
    H("5.22.4 Kiểm tra siêu âm (thể tích)", "5.22.4 Ultrasonic (Volumetric) Examination", h3)
    P("Phương pháp này theo dõi sự phản xạ sóng âm từ chi tiết để xác định độ sâu và kích thước của chỉ "
      "báo. Siêu âm phát hiện vật lạ và sự không liên tục trong kim loại hạt mịn, phù hợp kiểm tra thể "
      "tích của tấm, thanh và vật rèn. Thử thường thực hiện với dầu tiếp xúc (couplant) hoặc dưới nước "
      "để truyền sóng hiệu quả. Sóng do đầu dò tinh thể tạo ra và phản xạ tại mỗi giao diện, kể cả mặt "
      "ngoài của chi tiết và mặt của phần hư hỏng hoặc biến dạng bên trong. Các phản xạ được đầu dò thu "
      "và hiển thị trên màn hình để xác định vị trí và mức độ của chỉ báo.",
      "This method monitors sound wave reflections from the piece being inspected to determine the "
      "depth and size of any indications. Ultrasonic examination can detect foreign materials and "
      "discontinuities in fine-grained metal and thus lends itself to volumetric examination of "
      "structures such as plate, bar, and forgings. The test is normally conducted with a special oil "
      "called a couplant or underwater to ensure efficient transmission of sound waves. The sound waves "
      "are generated by a crystal probe and are reflected at each interface in the piece being tested, "
      "that is, at each outer face of the piece itself and at each face of the damaged or malformed "
      "internal portion. These reflections are received by the crystal probe and displayed on a screen "
      "to reveal the location and severity of the indication.")

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 5 chiếm tr. 98–149 của bản in (52 trang) trong Emerson, Control Valve Handbook, ấn bản "
      "6 (2020). Nội dung gồm hai mươi hai mục 5.1–5.22: kích thước van, phân loại rò rỉ chỗ ngồi, "
      "đặc tính dòng chảy, định cỡ chất lỏng và chất nén, hệ số định cỡ đại diện, định cỡ cơ cấu chấp "
      "hành, mô-men van quay, xâm thực và bay hơi, dự báo và kiểm soát tiếng ồn, đệm kín, vật liệu thân "
      "van, xếp hạng áp suất-nhiệt độ, viết tắt vật liệu phi kim và kiểm tra không phá hủy. Mười tám "
      "hình illustration được vẽ lại dạng vector trong cvh6fig5.py và đặt đúng vị trí xuất hiện của chú "
      "thích gốc.",
      "Chapter 5 occupies printed pp. 98-149 (52 pages) of Emerson, Control Valve Handbook, 6th edition "
      "(2020). It contains twenty-two sections, 5.1-5.22: valve dimensions, seat leakage classifications, "
      "flow characteristics, liquid and compressible sizing, representative sizing coefficients, "
      "actuator sizing, rotary valve torques, cavitation and flashing, noise prediction and control, "
      "packing, body materials, pressure-temperature ratings, non-metallic abbreviations and "
      "non-destructive examination. The eighteen numbered figures are redrawn as vectors in cvh6fig5.py "
      "and placed where the source captions occur.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 Emerson Flow "
      "Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 Emerson Flow "
      "Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
