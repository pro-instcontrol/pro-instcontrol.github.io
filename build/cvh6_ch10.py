# -*- coding: utf-8 -*-
"""Book 7c, Chapter 10 - Isolation Valves (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 210-239.
The chapter is extracted from IPT's *Pipe Trades Handbook* by Robert A. Lee,
with permission. It surveys the basic isolation valve types (gate, globe,
check, preheater-protection, reheater-isolation, turbine-extraction, bypass,
diaphragm, pinch, ball, butterfly and plug valves) and closes with a long run
of face-to-face and end-to-end dimension tables for cast iron and steel
valves. Fifty-three numbered figures are redrawn as legible vectors in
`cvh6fig10.py` and placed in numerical order at their logical prose points.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import fig, h2, h3, h4, lead, note, p, ul
import cvh6fig10 as F10

PAGES_SRC = 30         # source printed pp. 210-239 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Isolation Valves"
TITLE_VI = "Van cô lập"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> isolation valve — van cô lập · "
            "gate valve — van "
            "cổng · globe valve — van cầu · check valve — van kiểm (van một chiều) "
            "· diaphragm "
            "valve — van màng · pinch valve — van kẹp · ball valve — van bi · "
            "butterfly valve — "
            "van bướm · plug valve — van cắm · relief valve — van an toàn · wedge "
            "— nêm · solid "
            "wedge — nêm đặc · flexible wedge — nêm linh hoạt · split wedge — nêm "
            "tách · "
            "flexible split wedge — nêm tách linh hoạt · double disk — đĩa kép · "
            "parallel slide — "
            "trượt song song · eyelet — vòng dẫn hướng (eyelet) · bonnet — nắp van "
            "· bolted "
            "bonnet — nắp bắt bulông · pressure seal — gioăng áp lực · seat — ghế "
            "van (bề mặt "
            "đảm) · stem — thân van · packing — bao bì chân van · gland — hộp đệm "
            "· valvehead — "
            "đầu van · disk — đĩa van · body guided — dẫn hướng bằng thân van · "
            "stem bonnet "
            "guided — dẫn hướng bằng trục trong nắp van · non-return valve (NRV) — "
            "van một chiều · "
            "stop-check — van dừng-kiểm · throttling — tiết lưu · wire drawing — "
            "xói mòn do dòng "
            "chảy · disk chatter — rung đĩa · shock closure — đóng va đập · "
            "face-to-face — kích "
            "thước mặt đối mặt · center-to-face — kích thước tâm đến mặt · "
            "end-to-end — kích "
            "thước đầu đến đầu · NPS (nominal pipe size) — kích thước ống danh "
            "nghĩa · ANSI class "
            "— cấp áp lực ANSI · raised face — mặt bích nhô · flat face — mặt bích "
            "phẳng · "
            "beveled end — đầu vát · short pattern — kiểu ngắn · long pattern — "
            "kiểu dài · bypass "
            "— đường vòng · feedwater heater — máy gia nhiệt nước cấp · reheater — "
            "bộ quá nhiệt "
            "lại · turbine extraction — chiết hơi tuabin · hydro-test — thử áp lực "
            "nước · blind — "
            "tấm bịt · actuator — bộ truyền động")
    return (
        "<b>Key terms in this chapter.</b> isolation valve · gate valve · "
        "globe valve · check "
        "valve · diaphragm valve · pinch valve · ball valve · butterfly valve "
        "· plug valve · "
        "relief valve · wedge · solid wedge · flexible wedge · split wedge · "
        "flexible split wedge "
        "· double disk · parallel slide · eyelet · bonnet · bolted bonnet · "
        "pressure seal · seat · "
        "stem · packing · gland · valvehead · disk · body guided · stem bonnet "
        "guided · "
        "non-return valve (NRV) · stop-check · throttling · wire drawing · "
        "disk chatter · shock "
        "closure · face-to-face · center-to-face · end-to-end · NPS (nominal "
        "pipe size) · ANSI "
        "class · raised face · flat face · beveled end · short pattern · long "
        "pattern · bypass · "
        "feedwater heater · reheater · turbine extraction · hydro-test · blind "
        "· actuator")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Trong bản dump, chú thích «Figure 10.2 "
            "Gate Valve "
            "Bolted Bonnet» xuất hiện trước chú thích «Figure 10.1 Gate Valve "
            "Pressure Seal», dù "
            "theo số thì Hình 10.1 đứng trước; ở đây hai hình được đặt lại đúng "
            "thứ tự số. "
            "(2) Tương tự, chú thích Hình 10.30 «Bypass and Auxiliary Connections» "
            "nằm trước "
            "chú thích Hình 10.29 «Bypass Valve» trong bản dump; hai hình được sắp "
            "lại thành "
            "10.29 rồi 10.30. (3) Chú thích Hình 10.46 in thành «Figure 10.46. "
            "Steel Gate Valve "
            "(Class 2500)» có dấu chấm sau số; dấu chấm đó được giữ trong bản Anh "
            "và bỏ trong bản "
            "Việt. (4) Đoạn mô tả van cầu dạng T, dạng Y và dạng góc lặp gần như "
            "nguyên văn câu "
            "«This valve is considered as sealing by torque... acting against the "
            "pressure»; "
            "phần lặp được giữ trong bản Anh và gộp tự nhiên trong bản Việt. (5) "
            "Các ô «---» trong "
            "bảng không phải là lỗi OCR mà là ký hiệu của nguồn: theo ghi chú in, "
            "kích thước đó "
            "không có trong tiêu chuẩn ASME/ANSI nhưng có thể có trên thị trường; "
            "ký hiệu được "
            "giữ nguyên. (6) Một số lỗi chính tả và ngữ pháp được giữ nguyên ở bản "
            "Anh và hiệu "
            "đính trong bản Việt: «opearation», «effeciency», «confirguration», "
            "«is is achieved», "
            "«It's function is», «along with is major components», «saunders "
            "valves» và "
            "«Venture-port» (viết lại là Venturi-port). (7) Chú thích Hình 10.25 "
            "in «Feedheater "
            "System» trong khi văn bản gọi thiết bị là «preheater» hoặc «feedwater "
            "heater»; cách "
            "gọi của nguồn được giữ. (8) Một số ô số liệu trong bảng có vẻ lệch "
            "một chữ số so với "
            "quy luật các cột (ví dụ 812.2, 557.9), nhưng ở đây vẫn chuyển nguyên "
            "như bản in vì "
            "đây là bản dịch, không phải bản hiệu đính tiêu chuẩn. (9) Các dòng "
            "ghi chú «Notes» "
            "được đặt ngay trước chú thích Hình 10.40, 10.41, 10.46 và 10.53; ở "
            "đây chúng được "
            "trình bày thành các danh sách gạch đầu dòng song ngữ. (10) Nguồn "
            "không có bảng hay "
            "phương trình nào nằm ngoài các hình: toàn bộ bảng kích thước là nội "
            "dung của Hình "
            "10.40 đến Hình 10.53, nên ở đây không tạo bảng hay phương trình mới. "
            "(11) Hình trong "
            "bản in là bản vẽ và bảng dữ liệu; ở đây được vẽ lại dạng vector dễ "
            "đọc, không phải "
            "hình gốc.")
    return (
        "<b>Source notes.</b> (1) In the dump, the caption «Figure 10.2 Gate "
        "Valve Bolted "
        "Bonnet» appears before «Figure 10.1 Gate Valve Pressure Seal», "
        "although numerically "
        "Figure 10.1 comes first; the two figures are restored here to "
        "numerical order. (2) "
        "Likewise the caption for Figure 10.30, «Bypass and Auxiliary "
        "Connections», is printed "
        "ahead of the caption for Figure 10.29, «Bypass Valve»; they are "
        "reordered here as 10.29 "
        "then 10.30. (3) The caption of Figure 10.46 is printed as «Figure "
        "10.46. Steel Gate "
        "Valve (Class 2500)» with a leading period after the number; the "
        "period is retained in "
        "English and dropped in Vietnamese. (4) The descriptions of the "
        "T-pattern, Y-pattern "
        "and angle-pattern globe valves repeat almost verbatim the sentence "
        "«This valve is "
        "considered as sealing by torque ... acting against the pressure»; the "
        "repetition is "
        "kept in English and smoothed over in Vietnamese. (5) The «---» cells "
        "in the tables are "
        "not OCR losses but the source's own notation: per the printed note, "
        "the size is not "
        "shown in ASME/ANSI standards but may be commercially available; the "
        "notation is kept. "
        "(6) Several spelling and grammar quirks are retained in English and "
        "corrected in "
        "Vietnamese: «opearation», «effeciency», «confirguration», «is is "
        "achieved», «It's "
        "function is», «along with is major components», «saunders valves» and "
        "«Venture-port» "
        "(rendered as Venturi-port in Vietnamese). (7) The caption of Figure "
        "10.25 reads "
        "«Feedheater System», while the text calls the device a «preheater» or "
        "«feedwater "
        "heater»; the source wordings are retained. (8) A few table cells look "
        "off by one digit "
        "relative to the pattern of their columns (for example 812.2 and "
        "557.9); they are "
        "transcribed as printed, since this is a translation rather than a "
        "standards erratum. "
        "(9) The «Notes» blocks sit immediately before the captions of Figures "
        "10.40, 10.41, "
        "10.46 and 10.53; they are presented here as bilingual bulleted lists. "
        "(10) The source "
        "has no table or equation outside the figures: every dimension table "
        "is the content of "
        "Figures 10.40 through 10.53, so no new table or equation is "
        "introduced. (11) Figures "
        "are line drawings and data tables in print; they are redrawn here as "
        "legible vectors, "
        "not the original images.")


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
        "Chương này trình bày các dạng van cô lập cơ bản dùng trong công "
        "nghiệp — van cổng, van "
        "cầu, van kiểm, van bảo vệ máy gia nhiệt sơ bộ, van cô lập bộ quá "
        "nhiệt lại, van chiết "
        "hơi tuabin, van đường vòng, van màng, van kẹp, van bi, van bướm và "
        "van cắm — cùng với "
        "các bảng kích thước mặt đối mặt và đầu đến đầu của van gang và van "
        "thép theo tiêu chuẩn "
        "ASME/ANSI B16.10."
        if vi else
        "This chapter presents the basic isolation valve types used in "
        "industry - gate, globe, "
        "check, preheater-protection, reheater-isolation, turbine-extraction, "
        "bypass, diaphragm, "
        "pinch, ball, butterfly and plug valves - together with face-to-face "
        "and end-to-end "
        "dimension tables for cast iron and steel valves to ASME/ANSI "
        "B16.10."))
    P("Chương này được trích từ cuốn Pipe Trades Handbook của IPT của tác "
    "giả Robert A. Lee, "
      "được phép của tác giả.",
      "This chapter has been extracted from IPT's Pipe Trades Handbook by "
      "Robert A. Lee, with "
      "permission.")
    N(note_terms("vi"), note_terms("en"))

    # ------------------------------------------------------------ 10.1
    H("10.1 Các dạng van cơ bản", "10.1 Basic Valve Types")
    P("Có rất nhiều loại, kiểu, kích cỡ và hình dạng van được sử dụng trong "
    "công nghiệp. Dù có "
      "hàng chục loại van để lựa chọn, mục đích chính của van vẫn không đổi: "
      "ngăn hoặc cho dòng "
      "chảy, hoặc điều tiết dòng chảy.",
      "There are numerous valve types, styles, sizes, and shapes available "
      "for use in industry. "
      "Even though there are dozens of valve varieties to choose from, the "
      "primary purpose of "
      "valves remains the same; that is to stop or start flow, or to "
      "regulate flow.")
    P("Điều tiết dòng chảy bao gồm: tiết lưu, ngăn ngừa dòng chảy ngược, và "
    "giảm áp hoặc điều "
      "hòa áp lực trong một hệ thống. Việc lựa chọn van cho một hệ thống dựa "
      "trên mục đích sử "
      "dụng và chức năng thiết kế của van. Có tám dạng thiết kế van cơ "
      "bản:",
      "Regulation of flow includes: throttling, prevention of flow reversal, "
      "and relieving or "
      "regulating pressure within a system. Selection of valves for a system "
      "is based on the "
      "valve's intended service and design function. There are eight basic "
      "valve designs "
      "available:")
    B(["Van cổng", "Van cầu", "Van kiểm", "Van màng", "Van bi", "Van bướm", "Van cắm",
       "Van an toàn"],
      ["Gate", "Globe", "Check", "Diaphragm", "Ball", "Butterfly", "Plug", "Relief"])

    # ------------------------------------------------------------ 10.1.1
    H("10.1.1 Van cổng", "10.1.1 Gate Valves")
    P("Van cổng được dùng cho chế độ đóng/mở và được thiết kế để vận hành ở "
    "trạng thái mở hoàn "
      "toàn hoặc đóng hoàn toàn. Vì rung động và mài mòn quá mức phát sinh ở "
      "van cổng đóng một "
      "phần, loại van này không dùng để tiết lưu hoặc điều tiết lưu lượng. "
      "Van cổng có các kiểu "
      "nêm đặc, nêm linh hoạt, nêm tách, nêm tách linh hoạt, đĩa kép, trượt "
      "song song và trượt "
      "song song có vòng dẫn hướng (eyelet). Một van cổng điển hình và các "
      "bộ phận chính của nó "
      "được trình bày trong Hình 10.2. Xem các Bảng 10.1 và 10.3 đến 10.7 "
      "của chương này để biết "
      "kích cỡ và kích thước.",
      "Gate valves are used for on/off service and are designed to operate "
      "fully open or fully "
      "closed. Because of excessive vibration and wear created in "
      "partially-closed gates, the "
      "valves are not intended for throttling or flow regulation. Gate "
      "valves are available in "
      "solid wedge, flexible wedge, split wedge, flexible split wedge, "
      "double-disk, parallel "
      "slide and parallel slide with eyelet styles. A typical gate valve and "
      "its major parts are "
      "shown in Figure 10.2. See Tables 10.1 and 10.3 through 10.7 of this "
      "chapter for sizes and "
      "dimensions.")
    FIG(1, F10.fig_f10_01())
    FIG(2, F10.fig_f10_02())
    P("Van cổng kiểu nêm có một nêm thuôn dần sẽ chèn giữa hai ghế van cũng "
    "thuôn dần khi van "
      "đóng. Thiết kế nêm đặc (Hình 10.2) được dùng rộng rãi và phù hợp cho "
      "môi trường không khí, "
      "khí, dầu, hơi nước và nước. Van cổng nêm linh hoạt được dùng trong "
      "những dịch vụ có xu "
      "hướng làm kẹt thiết kế nêm đặc do biến động nhiệt độ quá lớn.",
      "Wedge-type gate valves have a tapered wedge that wedges between two "
      "tapered seats when "
      "the valve is closed. The solid-wedge design (Figure 10.2) is widely "
      "used and is suitable "
      "for air, gas, oil, steam, and water service. Flexible wedge gate "
      "valves are used in "
      "services that have a tendency to bind the solid-wedge design due to "
      "excessive variations "
      "in temperatures.")
    FIG(3, F10.fig_f10_03())
    FIG(4, F10.fig_f10_04())
    P("Thiết kế nêm linh hoạt (trình bày trong Hình 10.4) cho khả năng đảm "
    "kín tốt (khi mở và khi "
      "đóng) trong dải nhiệt độ rộng, đồng thời vẫn bảo đảm đóng kín chắc "
      "chắn.",
      "The design of the flexible wedge (shown in Figure 10.4) provides good "
      "seating "
      "characteristics (opening and closing) for a wide range of "
      "temperatures while providing "
      "positive shutoff.")
    FIG(5, F10.fig_f10_05())
    P("Van cổng nêm tách và van cổng đĩa kép có đĩa hoặc nêm gồm hai mảnh. Ở "
    "kiểu nêm tách (Hình "
      "10.5), vòng quay cuối cùng của tay vặn ép hai đĩa vào các ghế thuôn "
      "dần. Van cổng đĩa kép "
      "có các đĩa và ghế song song. Việc đóng đĩa kép được thực hiện bằng "
      "một bộ phận nong hoặc "
      "nêm ép các đĩa song song vào ghế. Van cổng đĩa kép được trình bày "
      "trong Hình 10.6.",
      "Split-wedge and double-disk gate valves have disks or wedges that are "
      "made of two pieces. "
      "In the split-wedge design (Figure 10.5), the last turn of the "
      "handwheel forces the two "
      "disks against the tapered seats. The double-disk gate valve has "
      "parallel disks and seats. "
      "Closure of the double disk is accomplished by a spreader or wedge "
      "which forces the "
      "parallel disks against the seats. The double-disk gate valve is shown "
      "in Figure 10.6.")
    FIG(6, F10.fig_f10_06())
    P("Ma sát gây mài mòn ghế và đĩa được giữ ở mức tối thiểu ở cả van cổng "
    "nêm tách lẫn van cổng "
      "đĩa kép, vì ghế và đĩa chỉ tiếp xúc khi đóng van.",
      "Friction, which causes wear on seats and disks, is kept to a minimum "
      "in both the "
      "split-wedge and double-disk gate valves because the seat and disk are "
      "in contact only on "
      "closing the valve.")
    P("Khi lắp đặt van cổng nêm tách hoặc van cổng đĩa kép, thân van phải ở "
    "vị trí thẳng đứng "
      "(van đứng), để bảo đảm các đĩa không bị kẹt tách ra trước khi đóng.",
      "When installing either the split-wedge or double-disk gate valve, the "
      "stem of the valve "
      "must be vertical (valve upright) which ensures the disks do not jam "
      "apart before closing.")
    P("Thiết kế nêm tách linh hoạt kết hợp ưu điểm của kiểu trượt song song "
    "và kiểu nêm linh "
      "hoạt. Cấu trúc bên trong đặc biệt, linh hoạt, được chế tạo thành hai "
      "mảnh trượt song song, "
      "cho phép đóng van theo vị trí. Kết quả là mô-men yêu cầu bị hạn chế, "
      "cũng như việc chọn "
      "kích cỡ bộ truyền động. Áp lực môi trường càng cao thì độ kín của van "
      "càng lớn mà không bị "
      "kẹt. Hình dạng nêm giúp rút ngắn thời gian tiếp xúc giữa ghế và cụm "
      "nêm, vì vậy mài mòn "
      "thấp và độ kín bền lâu được kỳ vọng. Khi đóng theo vị trí, độ kín "
      "cũng được bảo đảm ở áp "
      "suất thấp, không rò rỉ ở 6 bar khí.",
      "The design of flexible split wedges mixes the advantages of parallel "
      "slide and flexible "
      "wedge executions. The special flexible internal construction, which "
      "is made in two "
      "pieces as parallel slides, allows valves to be closed by position. As "
      "a result, the "
      "requested torque is limited, as actuator sizing. The higher the "
      "medium pressure, the "
      "higher the valve tightness will be without jamming. The wedge shape "
      "minimizes the mating "
      "time between seats and wedge assembly, so low wear and lasting "
      "tightness are expected. "
      "When closing by position, tightness is ensured also at low pressure, "
      "zero leakage at 6 "
      "bar air.")
    FIG(7, F10.fig_f10_07())
    P("Thiết kế trượt song song có vòng dẫn hướng (eyelet) vận hành hoàn "
    "toàn giống như trượt "
      "song song tiêu chuẩn, nhưng ở vị trí mở có một bộ dẫn hướng eyelet "
      "tích hợp làm khép khe "
      "hở giữa các ghế.",
      "The design of parallel slides with eyelet operates in exactly the "
      "same way as standard "
      "parallel slides, but when in the open position it has an inbuilt "
      "eyelet follower that "
      "closes the gap between the seats.")
    P("Vòng eyelet mang lại các lợi ích sau:",
      "The eyelet provides the following:")
    B(["Bảo vệ các ghế van khỏi dòng chảy.",
       "Bảo vệ đĩa van khỏi dòng chảy.",
       "Giảm nhiễu loạn trong không gian tích hợp, từ đó giảm tổn thất áp lực "
       "và tiếng ồn."],
      ["Protects the seats from the flow.",
       "Protects the disk from the flow.",
       "Reduces turbulence in the integrated space, thereby providing a lower "
       "pressure loss and "
       "less noise."])
    P("Van được xem là «tự đảm kín theo vị trí». Kiểu ứng dụng này phù hợp "
    "hơn cho áp lực cao, "
      "kích cỡ lớn và các ứng dụng có vận tốc dòng chảy cao.",
      "The valve is considered to seal by position. This type of application "
      "is more suitable "
      "for higher pressure, larger sizes, and high velocity applications.")
    P("Liên kết giữa thân và nắp của tất cả van cô lập có thể là:",
      "Body to bonnet junction of all isolation valves can be:")
    B(["Nắp bắt bulông, dùng bulông và đai ốc cho mọi cấp áp lực từ 150 đến "
    "1500.",
       "Gioăng áp lực (pressure seal), chỉ dùng cho các cấp áp lực cao từ 900 "
       "đến 4500."],
      ["Bolted bonnet with bolts and nuts applied to all classes from 150 to "
      "1500.",
       "Pressure seal applied only to high pressure classes from 900 to "
       "4500."])
    P("Hoạt động của gioăng áp lực có thể mô tả như sau:",
      "Pressure seal operation could be described as:")
    B([
        "Một lực trục tăng lên khi áp lực bên trong tăng được tác dụng lên "
        "gioăng.",
        "Lực này nén gioăng, làm gioăng biến dạng theo hướng xuyên tâm và "
        "trục.",
        "Theo hướng xuyên tâm, gioăng bị ép vào thành thân van và nắp van, từ "
        "đó đạt được áp "
        "suất bề mặt và lực đảm kín tương ứng.",
        "Vòng nằm phía trên gioăng hấp thụ lực trục và truyền lực đó tới các "
        "vòng đoạn.",
        "Các vòng đoạn được lắp trong một rãnh trên thân van, nhờ đó truyền "
        "lực trục sang thân "
        "van.",
        "Nắp được căng trước bằng các chốt tán (stud) để gioăng đã biến dạng "
        "và đạt được hiệu "
        "ứng đảm kín ngay cả khi áp lực bên trong thấp."],
      [
        "An axial force that increases as the internal pressure increases are "
        "applied to the "
        "gasket.",
        "This force compresses the gasket, which deforms radially and "
        "axially.",
        "In the radial direction it is pressed against the wall of the body "
        "and the cover, thus "
        "achieving the required surface pressure and associated sealing "
        "force.",
        "The ring above the gasket absorbs the axial force and transfers it to "
        "the segment "
        "rings.",
        "The segment rings are fitted in a groove in the body, thus "
        "transferring the axial "
        "force to the body.",
        "The cover is pre-stressed by studs so that the gasket is deformed and "
        "the sealing "
        "effect achieved even when the internal pressure is low."])
    P("Nhìn chung, nắp bắt bulông là giải pháp thông dụng ở các cấp áp lực "
      "từ 150 đến 1500, "
      "trong khi gioăng áp lực chỉ được dùng ở các cấp cao từ 900 đến 4500, "
      "nơi lực trục do "
      "áp lực bên trong tạo ra trở thành bộ phận chính của cơ cấu đảm kín. "
      "Hình 10.8 minh "
      "họa cấu tạo của cơ cấu gioăng áp lực này.",
      "In summary, the bolted bonnet is the common solution for classes from "
      "150 to 1500, "
      "whereas the pressure seal is used only in high-pressure classes from "
      "900 to 4500, "
      "where the axial force generated by internal pressure becomes the main "
      "part of the "
      "sealing mechanism. Figure 10.8 illustrates the construction of this "
      "pressure seal.")
    FIG(8, F10.fig_f10_08())

    # ------------------------------------------------------------ 10.1.2
    H("10.1.2 Van cầu", "10.1.2 Globe Valves")
    P("Khác với van cổng, van cầu được dùng trong các ứng dụng cần vận hành "
    "thường xuyên hoặc "
      "tiết lưu dòng chảy. Thiết kế van cầu (trình bày trong Hình 10.9) giảm "
      "thiểu sự xói mòn "
      "ghế van, đồng thời dễ bảo trì. Khi dòng chảy bắt đầu trong van cầu, "
      "đĩa van rời hoàn toàn "
      "khỏi ghế, nhờ đó hạn chế xói mòn và hiện tượng xói dây (wire "
      "drawing). Xem cuối chương để "
      "biết kích cỡ và kích thước.",
      "Globe valves, unlike gate valves, are used in applications requiring "
      "frequent operation "
      "and/or throttling of flow. The design of the globe valve (shown in "
      "Figure 10.9) keeps seat "
      "erosion to a minimum, while making it an easy valve to service. When "
      "flow begins in the "
      "globe valve design, the disk moves completely away from the seat, "
      "thus minimizing erosion "
      "and wire drawing. See end of this chapter for sizes and dimensions.")
    FIG(9, F10.fig_f10_09())
    P("Van cầu có ba kiểu thân: thân góc, thân kiểu Y và thân kiểu T, hoặc "
    "thân thẳng (phổ biến "
      "nhất). Thường có sẵn chức năng không quay lại, gọi là van dừng-kiểm "
      "(stop-check) hoặc van "
      "một chiều. Trong trường hợp này, đầu van không được cố định vào thân "
      "van, nên khi van ở "
      "vị trí mở và xảy ra dòng chảy ngược, đầu van sẽ đóng và thực hiện "
      "chức năng của van kiểm.",
      "Globe valves are available in three body styles: angle body, "
      "Y-pattern and T-pattern "
      "body, or straightway body (most common). Often available with a "
      "non-return function, "
      "referred to as a stop-check or non-return valve. In this instance, "
      "the valvehead is not "
      "fixed to the stem, so when in open position in the event of a flow "
      "reversal the valvehead "
      "will close and perform a check valve function.")
    P("Cả ba kiểu thân đều phù hợp để tiết lưu, nhưng mỗi kiểu có đặc tính "
    "dòng chảy và phạm vi "
      "ứng dụng riêng.",
      "All three body styles are suited for throttling, but each has its own "
      "flow characteristic "
      "and service applicability.")
    P("Việc lựa chọn kiểu thân vì thế phụ thuộc vào hướng đi của đường ống, "
      "mức độ hạn chế dòng "
      "chảy cho phép và tính chất môi chất. Kiểu thẳng là cấu hình mặc định "
      "khi không có yêu cầu "
      "đặc biệt; kiểu góc thay thế được một đoạn cong và tiết kiệm không "
      "gian; kiểu Y được ưu "
      "tiên khi cần đường dẫn chảy êm và tổn thất áp lực thấp.",
      "The choice of body style therefore depends on the direction of the "
      "piping, the "
      "allowable flow restriction and the nature of the medium. The "
      "straightway body is the "
      "default where no special requirement exists; the angle body replaces "
      "a bend and saves "
      "space; and the Y-pattern is preferred where a smooth flow path and "
      "low pressure loss "
      "are required.")
    P("Van thân góc cho phép đổi hướng dòng chảy 90 độ (xem Hình 10.10), "
    "giúp tiết kiệm không "
      "gian, vật liệu và thời gian lắp đặt ở một số công trình. Thiết kế bên "
      "trong của van thân "
      "góc có độ hạn chế dòng chảy nhỏ hơn kiểu T thông thường nhưng lớn hơn "
      "van cầu kiểu Y.",
      "Angle body valves provide for a 90 degree change of direction (see "
      "Figure 10.10), which "
      "in some installations saves space, material, and installation time. "
      "The inner design of "
      "the angle body valve offers less flow restriction than the "
      "conventional T-pattern, but "
      "more than the Y-pattern globe valve.")
    FIG(10, F10.fig_f10_10())
    FIG(11, F10.fig_f10_11())
    P("Do thân van nghiêng 45 độ so với đường ống, van cầu kiểu Y có rất ít "
    "hạn chế dòng chảy. "
      "Hình 10.11 trình bày một van cầu kiểu Y điển hình. Van cầu kiểu Y rất "
      "phù hợp cho các ứng "
      "dụng cần dòng chảy gần như đầy đủ qua van nhưng vẫn mang đặc tính của "
      "van cầu. Ứng dụng "
      "của van cầu kiểu Y gồm xả đáy nồi hơi (boiler blow-offs) và các dịch "
      "vụ có thể có bùn, cát "
      "hoặc chất lỏng nhớt.",
      "Because of the 45-degree stem inclination from the run, Y-pattern "
      "globe valves give very "
      "little flow restriction. Figure 10.11 shows a typical Y-pattern globe "
      "valve. The "
      "Y-pattern globe valve is ideally suited for applications requiring "
      "almost full flow in a "
      "valve, but with the characteristics of a globe valve. Applications "
      "for the Y-pattern "
      "globe valve include boiler blow-offs and services where mud, grit, "
      "and/or viscous fluids "
      "may be encountered.")
    P("Các loại van cầu chính theo cách bố trí ghế van là:",
      "The main types of globe valves according to their seat arrangements "
      "are:")
    B(["Đĩa thông thường", "Đĩa cắm"],
      ["Conventional disk", "Plug disk"])
    P("Van cầu đĩa thông thường dùng một đĩa ngắn, thuôn dần lắp vào ghế "
    "thuôn tương ứng để đóng "
      "và tiết lưu (trình bày trong Hình 10.12). Khi điều kiện dòng chảy có "
      "xu hướng lắng đọng "
      "hoặc đóng cặn trên ghế van, người ta thường chọn thiết kế đĩa thông "
      "thường. Đĩa hẹp dùng "
      "trong van đĩa thông thường thường xuyên cắt qua lớp cặn và cho đảm "
      "kín chắc chắn, thay vì "
      "ép cặn vào ghế.",
      "Conventional disk globe valves use a short, tapered disk that fits "
      "into a matched tapered "
      "seat for closure and throttling (shown in Figure 10.12). When flow "
      "conditions have a "
      "tendency to deposit or coke on valve seats, the conventional disk "
      "valve design is often "
      "preferred. The narrow disk used in the conventional disk valve will "
      "usually break through "
      "deposits, giving positive seating, rather than packing the "
      "deposits.")
    FIG(12, F10.fig_f10_12())
    P("Đĩa cắm khác với đĩa thông thường ở chỗ cụm đĩa cắm và ghế dài hơn và "
    "thuôn dần hơn. Diện "
      "tích tiếp xúc dài hơn của cắm và ghế cho van cắm khả năng chống xói "
      "mòn do dòng chảy cao "
      "nhất. Một ví dụ về van cầu đĩa cắm được trình bày trong Hình 10.13.",
      "The plug disk differs from the conventional disk in that the plug "
      "disk and seat "
      "arrangement are longer and more tapered. The longer area of the plug "
      "and seat give the "
      "plug valve maximum resistance to flow-induced erosion. An example of "
      "a plug disk globe "
      "valve is shown in Figure 10.13.")
    FIG(13, F10.fig_f10_13())
    FIG(14, F10.fig_f10_14())
    P("Van cầu kiểu «T» hay «Tee» là một trong những cấu hình phổ biến nhất. "
    "Tên gọi bắt nguồn "
      "từ hình chữ T ngược của van. Loại này phù hợp cho cả áp lực thấp, áp "
      "lực cao, đường kính "
      "nhỏ và đường kính lớn. Van này được xem là «đảm kín bằng mô-men». "
      "Nhìn chung, áp lực tác "
      "dụng từ phía dưới đầu van và mô-men tác dụng lên van chống lại áp lực "
      "đó. Một ví dụ về van "
      "cầu kiểu T được trình bày trong Hình 10.14.",
      "A T or Tee pattern globe is one of the most common configurations. "
      "Its name derives from "
      "the inverted T shape of the valve. They are suitable for low "
      "pressure, high pressure, "
      "small bore, and large bore applications. This valve is considered as "
      "sealing by torque. "
      "Generally, the pressure will be from below the valvehead, and the "
      "torque applied to the "
      "valve acts against the pressure. An example of a t-type globe valve "
      "is shown in Figure "
      "10.14.")
    FIG(15, F10.fig_f10_15())
    P("Van cầu kiểu «Y» hay «Wye» là cấu hình phổ biến. Tên gọi bắt nguồn từ "
    "hình chữ Y nghiêng "
      "của van. Loại này thường được dùng nhất cho các ứng dụng áp lực cao "
      "nhờ đường dòng chảy "
      "êm hơn so với kiểu T, giúp tổn thất áp lực thấp hơn. Van này cũng "
      "được xem là «đảm kín "
      "bằng mô-men». Nhìn chung, áp lực tác dụng từ phía dưới đầu van và "
      "mô-men tác dụng lên van "
      "chống lại áp lực đó. Một ví dụ về van cầu kiểu Y được trình bày trong "
      "Hình 10.15. Câu mô "
      "tả về đảm kín bằng mô-men ở đây lặp lại với đoạn trên, phản ánh đúng "
      "văn bản nguồn.",
      "A Y or Wye pattern globe is a common confirguration. Its name comes "
      "from the inclined Y "
      "shape of the valve. They are most commonly used on high pressure "
      "applications due to the "
      "smoother flow path compared to a T pattern that provides a lower "
      "pressure loss. This "
      "valve is considered as sealing by torque. Generally, the pressure "
      "will be from below the "
      "valvehead with the torque applied to the valve acting against the "
      "pressure. An example of "
      "a y-type globe valve is shown in Figure 10.15.")
    P("Van cầu kiểu góc là cấu hình ít phổ biến hơn trong nhiệm vụ cô lập, "
    "thường gắn với chức "
      "năng điều khiển. Loại này cũng được xem là «đảm kín bằng mô-men». "
      "Nhìn chung, áp lực tác "
      "dụng từ phía dưới đầu van và mô-men tác dụng lên van chống lại áp lực "
      "đó. Một ví dụ về van "
      "cầu kiểu góc được trình bày trong Hình 10.16.",
      "An angle pattern globe valve is a less common configuration of globe "
      "valves on isolation "
      "duty, more often associated with control functionality. They are "
      "considered as sealing by "
      "torque. Generally, the pressure will be from below the valvehead with "
      "torque applied to "
      "the valve acting against the pressure. An example of a angle type "
      "globe valve is shown in "
      "Figure 10.16.")
    FIG(16, F10.fig_f10_16())
    P("Các đặc điểm chính của chức năng dừng của van như sau:",
      "Main characteristics of valve stop functions are as follows:")
    P("<b>Chức năng dừng (Stop Function):</b> đầu van và thân van được nối "
    "với nhau; van chỉ có "
      "thể đóng bằng cách vận hành tay vặn hoặc bộ truyền động.",
      "<b>Stop Function:</b> valvehead and stem connected; valve can only be "
      "closed by operation "
      "of handwheel / actuator.")
    FIG(17, F10.fig_f10_17())
    P("<b>Chức năng dừng-kiểm (Stop-Check Function):</b> đầu van và thân van "
    "không nối với nhau; "
      "van có thể đóng bằng cách vận hành tay vặn hoặc bộ truyền động; hoặc "
      "khi dòng chảy đảo "
      "chiều.",
      "<b>Stop-Check Function:</b> valvehead and stem not connected; valve "
      "can be closed by "
      "operation of handwheel / actuator; flow reversal.")
    FIG(18, F10.fig_f10_18())

    # ------------------------------------------------------------ valve guiding
    H("10.1.2.1 Dẫn hướng van", "10.1.2.1 Valve Guiding Types", h3)
    P("Chìa khóa cho hiệu năng tin cậy là bảo đảm các phần tử đóng luôn được "
    "căn chỉnh đúng "
      "hướng. Có hai cách tiếp cận cơ bản: dẫn hướng bằng thân van (body "
      "guided) và dẫn hướng "
      "bằng trục trong nắp van (stem bonnet guided).",
      "The key to reliable performance is ensuring that the closure elements "
      "remain aligned in "
      "the correct orientation. There are two main fundamental approaches to "
      "this - body guided "
      "and stem bonnet guided.")
    P("Dẫn hướng bằng thân van thường dùng cho van cầu và van một chiều cỡ "
    "lớn. Thường đạt được "
      "bằng cách dẫn hướng đầu van ngay trên thân van.",
      "Body guiding is commonly used on larger globe and non-return valves. "
      "This is normally "
      "achieved by using guiding of the valvehead on the body.")
    P("<b>Ưu điểm:</b> diện tích tiếp xúc lớn giúp ổn định đầu van.",
      "<b>Advantages:</b> large contact area to provide stability of the "
      "valvehead.")
    P("<b>Nhược điểm:</b> có thể cần phủ cứng (hard-facing) cho các ứng dụng "
    "mài mòn cao; có thể "
      "bị bám bẩn và kẹt nếu điều kiện hệ thống không được duy trì, ví dụ "
      "đóng cặn; thường cần "
      "đầu van lớn hơn. Trong ứng dụng van một chiều, nếu đầu van bị kẹt "
      "chặt vào thân van thì "
      "chức năng van cầu cũng bị mất.",
      "<b>Disadvantages:</b> it may require hard-facing for high wear "
      "applications; it can be "
      "subject to fouling and binding if system conditions are not "
      "maintained, i.e. scale; a "
      "larger valvehead is often required. On NRV applications, if the "
      "valvehead seizes to the "
      "body, then the globe valve functionality can be lost also.")
    FIG(19, F10.fig_f10_19())
    H("10.1.2.2 Dẫn hướng bằng trục trong nắp van",
      "10.1.2.2 Stem Bonnet Guiding", h3)
    P("Dẫn hướng bằng trục trong nắp van thường dùng cho van đường kính nhỏ "
    "và được thực hiện "
      "bằng cách dẫn hướng trục van bên trong nắp van. Hướng của các phần tử "
      "đóng được bảo đảm "
      "bởi một thiết bị chống quay bên ngoài.",
      "Stem bonnet guiding is common on smaller diameter valves and is "
      "achieved by guiding the "
      "stem within the bonnet. The orientation of the closure elements is by "
      "an external "
      "anti-rotation device.")
    P("<b>Ưu điểm:</b> đưa bộ phận dẫn hướng ra khỏi tác động trực tiếp của "
    "môi chất hệ thống; có "
      "thể giảm kích thước và trọng lượng của đầu van; nhìn chung không cần "
      "phủ cứng cho các "
      "chi tiết; ở thiết kế van một chiều, cho phép dùng van như van cầu khi "
      "bị kẹt.",
      "<b>Advantages:</b> it removes the guiding from the direct effects of "
      "the system media; "
      "can reduce the size / weight of valvehead; generally no need for "
      "hard-facing on "
      "components; on NRV designs, allows the valve to be used as a globe "
      "valve in the event of "
      "seizure.")
    P("<b>Nhược điểm:</b> có thể cần đường kính trục lớn hơn đối với van cỡ "
    "lớn.",
      "<b>Disadvantages:</b> it may require a larger stem diameter for big "
      "size valves.")
    FIG(20, F10.fig_f10_20())

    # ------------------------------------------------------------ 10.1.3
    H("10.1.3 Van kiểm", "10.1.3 Check Valves")
    P("Van kiểm được dùng để ngăn dòng chảy ngược trong hệ thống đường ống "
    "và thiết bị được nối "
      "với nó. Ba thiết kế van kiểm phổ biến nhất là:",
      "Check valves are used to prevent flow reversal in piping systems and "
      "connected "
      "equipment. The three most common designs of check valves are:")
    B(["Van kiểm dạng xoay (swing check)", "Đĩa nghiêng (tilting disk)",
       "Van kiểm dạng nâng (lift check)"],
      ["Swing check", "Tilting disk", "Lift check"])
    P("Ba thiết kế này khác nhau chủ yếu ở cách đĩa van trở về ghế: dạng "
      "xoay dùng bản lề và "
      "trọng lực, dạng đĩa nghiêng dùng vị trí bản lệ lệch để đóng nhanh, "
      "còn dạng nâng dùng "
      "chuyển động thẳng đứng theo kiểu van cầu. Lựa chọn giữa chúng phụ "
      "thuộc vào mức tổn thất "
      "áp lực cho phép, hướng lắp đặt và nguy cơ đóng va đập trong hệ thống.",
      "These three designs differ mainly in how the disk returns to its seat: "
      "the swing check "
      "uses a hinge and gravity, the tilting disk uses an offset hinge "
      "location for quick "
      "closure, and the lift check uses vertical motion in the manner of a "
      "globe valve. The "
      "choice among them depends on the allowable pressure loss, the "
      "installation orientation "
      "and the risk of shock closure in the system.")
    P("Thiết kế van kiểm dạng xoay (trình bày trong Hình 10.21) gồm một đĩa "
    "được bản lề, sẽ xoay "
      "mở khi dòng chảy bắt đầu theo hướng mong muốn và xoay đóng khi dòng "
      "chảy đảo chiều. Vì "
      "chuyển động xoay của đĩa, điều quan trọng là lắp đặt mọi van kiểm "
      "dạng xoay sao cho đĩa "
      "đóng chắc chắn nhờ trọng lực. Khi mở hoàn toàn, van kiểm dạng xoay có "
      "lực cản dòng chảy "
      "nhỏ hơn thiết kế van kiểm dạng nâng.",
      "The swing check valve design (shown in Figure 10.21) consists of a "
      "hinged disk that "
      "swings open when flow starts in the desired direction and swings "
      "closed in flow reversal "
      "situations. Because of this swinging action of the disk, it is "
      "important to install all "
      "swing check valves so that the disk closes positively by gravity. "
      "When fully open, the "
      "swing check offers less flow resistance than the lift check valve "
      "design.")
    FIG(21, F10.fig_f10_21())
    P("Trong những tình huống dòng chảy gây đóng va đập hoặc rung đĩa, có "
    "thể dùng các biến thể "
      "khác của van kiểm dạng xoay để giúp giảm thiểu vấn đề. Xem các bảng ở "
      "cuối chương để biết "
      "kích cỡ và kích thước.",
      "In flow situations where shock closure and/or disk chatter are "
      "encountered, other "
      "varieties of swing check valves can be used to help minimize the "
      "problems. See Tables at "
      "the end of this chapter for sizes and dimensions.")
    FIG(22, F10.fig_f10_22())
    P("Van kiểm dạng xoay có cần và đối trọng bên ngoài (trình bày trong "
    "Hình 10.22) hoặc đĩa "
      "có lò xo có thể giúp đóng ngay khi dòng chảy đảo chiều. Việc đóng "
      "ngay này hạn chế tổn "
      "hại do va đập và rung đĩa trong hệ thống. Van kiểm dạng xoay đĩa "
      "nghiêng là một loại khác "
      "của van kiểm dạng xoay, được dùng để giúp tránh hiện tượng đóng mạnh "
      "(slamming), xem Hình "
      "10.23.",
      "Swing check valves with outside lever and weight arrangements (shown "
      "in Figure 10.22) or "
      "spring-loaded disks can facilitate immediate closure in flow reverse. "
      "This immediate "
      "closure minimizes the possible damages of shock and disk chatter in "
      "systems. The "
      "tilting-disk swing check valve is another type of swing check valve "
      "that is used to help "
      "prevent slamming (see Figure 10.23).")
    FIG(23, F10.fig_f10_23())
    P("Van có thể được dùng như thiết kế thay thế cho nhiều ứng dụng giống "
    "như nơi người ta dùng "
      "van kiểm dạng xoay. Van được mở bằng chiều dòng chảy, với dòng chảy "
      "đi bên dưới lẫn phía "
      "trên đĩa, và được đóng bằng sự kết hợp giữa trọng lực và dòng chảy "
      "đảo chiều. Dòng chảy "
      "phía trên đĩa giúp đĩa ổn định hơn khi vận hành. Nhìn chung, ưu điểm "
      "của thiết kế này mang "
      "lợi ích thuận tiện nhất ở kích cỡ trên 6 in., cũng như trong các ứng "
      "dụng áp lực cao và "
      "lưu lượng thấp, nơi có nguy cơ mất ổn định đĩa.",
      "It can be used as an alternate design to many of the same "
      "applications where swing check "
      "valves are considered. The valve is opened by the flow direction, "
      "with the flow passing "
      "below as well as over the disk, and is closed by the combination of "
      "gravity and flow "
      "reversal. The flow over the disk provides greater stability of the "
      "disk in service. "
      "Generally, the advantages of this design provide the most convenient "
      "benefits above 6 in. "
      "and also on higher pressure and low flow rate applications, where "
      "there is a risk of disk "
      "stability.")
    P("Thiết kế van kiểm dạng nâng (trình bày trong Hình 10.24) được dùng "
    "trong những trường hợp "
      "không coi tổn thất áp lực là yếu tố quyết định. Kiểu dòng chảy qua "
      "van tương ứng với của "
      "van cầu. Van kiểm dạng nâng có cả thiết kế nằm ngang và thiết kế "
      "thẳng đứng.",
      "The lift check valve design (shown in Figure 10.24) is used in "
      "situations where pressure "
      "drop is not considered critical. The flow pattern through the valve "
      "corresponds to that "
      "of the globe valve. Lift check valves are available in horizontal and "
      "vertical designs.")
    FIG(24, F10.fig_f10_24())

    # ------------------------------------------------------------ 10.1.4
    H("10.1.4 Van bảo vệ máy gia nhiệt sơ bộ",
      "10.1.4 Preheater Protection Valves")
    P("Hệ thống gia nhiệt sơ bộ được thiết kế để gia nhiệt nước cấp trước "
    "khi vào nồi hơi, nhằm "
      "nâng cao hiệu suất. Điều này đạt được bằng cách lấy hơi từ hệ thống "
      "và dùng nó để gia "
      "nhiệt nước cấp đầu vào. Quá trình này diễn ra trong một bộ trao đổi "
      "nhiệt, thường được gọi "
      "là «máy gia nhiệt sơ bộ» hoặc «máy gia nhiệt nước cấp» (feedwater "
      "heater), gồm nhiều ống "
      "chứa nước áp lực cao được bao quanh bởi hơi áp lực tương đối thấp. "
      "Khi một ống bị vỡ, nước "
      "áp lực cao sẽ lấn át hơi áp lực thấp và có nguy cơ nước bị ép ngược "
      "trở lại hệ thống hơi. "
      "Để tránh điều đó, một hệ thống chỉ báo mức nước được lắp trong máy "
      "gia nhiệt sơ bộ và khi "
      "hệ thống này kích hoạt, cần có một cơ chế cô lập hiệu quả nước áp lực "
      "cao khỏi máy gia "
      "nhiệt sơ bộ. Có nhiều cách thực hiện, nhưng một cách là dùng van vào "
      "và van ra ba chiều. "
      "Các van này có thể vận hành bằng điện cơ hoặc bằng chính môi chất, "
      "tức là dùng áp lực "
      "nước cấp để vận hành van.",
      "The preheater system is designed to preheat the feedwater prior to it "
      "entering the boiler, "
      "to improve effeciency. This is achieved by taking steam from the "
      "system and using it to "
      "heat the incoming feedwater. This process is carried out in a heat "
      "exchanger, often "
      "referred to as preheater or feedwater heater, which consists of a "
      "number of tubes that "
      "contain high pressure water that are surrounded by relatively low "
      "pressure steam. In the "
      "event of a tube fracture, the high pressure water will overcome the "
      "low pressure steam "
      "and there is risk that water will force itself back down into the "
      "steam system. To avoid "
      "this, a water level indicator system is installed in the preheater "
      "and when this is "
      "triggered there needs to be a system to effectively isolate the high "
      "pressure water from "
      "the preheater. There are a number of ways to do this, but one system "
      "is using 3-way inlet "
      "and outlet valves. These can be either motor operated or medium "
      "operated, i.e. using the "
      "feedwater pressure to operate the valves.")
    H("Ứng dụng cơ bản của van", "Basic Valve Application", h3)
    P("<b>Vận hành bình thường:</b> nước đi vào van vào, sau đó ra tới máy "
    "gia nhiệt. Nước đã "
      "gia nhiệt đi vào van ra từ máy gia nhiệt, rồi đi qua van ra và cuối "
      "cùng tới nồi hơi.",
      "<b>Normal Operation:</b> water enters the inlet valve, then exits to "
      "the heater. The "
      "heated water enters the outlet valve from the heater, then enters the "
      "outlet valve and, "
      "finally, on to the boiler.")
    P("<b>Vận hành đường vòng:</b> các van được đóng. Nước lúc này đi qua "
    "phía trên bề mặt đảm "
      "của van vào và thoát ra qua đường ống ra của đường vòng vào van ra, "
      "nhờ đó cô lập máy gia "
      "nhiệt khỏi áp lực.",
      "<b>Bypass Operation:</b> valves are closed. The water now passes over "
      "the top of the inlet "
      "valve seating and exits via the bypass outlet piping into the outlet "
      "valve, thereby "
      "isolating the heater from the pressure.")
    FIG(25, F10.fig_f10_25())
    FIG(26, F10.fig_f10_26())

    # ------------------------------------------------------------ 10.1.5
    H("10.1.5 Van cô lập bộ quá nhiệt lại", "10.1.5 Reheater Isolation Valves")
    P("Thiết kế của cả hệ thống đốt than và hệ thống đốt khí đều nhằm truyền "
    "nhiệt từ quá trình "
      "cháy vào hơi nước cho quá trình phát điện. Ở một thời điểm nào đó "
      "trong vòng đời của nồi "
      "hơi, có thể cần tiến hành thử áp lực nước (hydro-test) để xác nhận "
      "tính toàn vẹn của nồi "
      "hơi. Điều này có thể do yêu cầu chứng nhận, hoặc để kiểm tra công "
      "việc bảo trì như thay "
      "ống nồi hơi.",
      "The design of both coal-fired and gas-fired systems is used to "
      "transfer heat from the "
      "combustion process into steam for the power generation process. At "
      "some point in the life "
      "of the boiler, it may be necessary to carry out a hydro-test to "
      "confirm the integrity of "
      "the boiler. This may be due to certification, or to check maintenance "
      "work, such as boiler "
      "tube replacement.")
    P("Nhìn chung có hai khu vực của nồi hơi dùng để sinh hơi và vì vậy phải "
    "chịu thử áp lực "
      "nước. Thông thường, các phép thử được thực hiện trên:",
      "There are generally two sections of the boiler that are used to "
      "generate steam and are "
      "therefore subject to hydro-test. Normally, tests are performed on:")
    B(["Khu vực hơi chính", "Khu vực quá nhiệt lại"],
      ["Main steam section", "Reheater section"])
    P("Khu vực hơi chính thường tương đối dễ cô lập, vì nó thường có van "
    "trên các đoạn đường ống "
      "hơi chính và nước cấp, có thể dùng để cô lập khu vực này khi cần thử "
      "áp lực. Tuy nhiên, "
      "khu vực quá nhiệt lại có thể khó cô lập hơn do vị trí và sự gần kề "
      "với tuabin. Đường ống "
      "quá nhiệt lại được dùng để thu hồi thêm năng lượng nhằm nâng cao hiệu "
      "suất, nên thường "
      "được dùng ở áp lực thấp hơn và đường ống lớn hơn để giảm tổn thất áp "
      "lực qua ống. Đây là "
      "một trong những lý do khiến người ta thường ngại lắp van trên các "
      "đường ống này, trừ khi "
      "có yêu cầu cụ thể, vì tổn thất áp lực có thể làm giảm hiệu suất.",
      "The main steam section is usually relatively easy to isolate, as it "
      "often has valves in "
      "the main steam and feedwater piping sections, which can be used to "
      "isolate in the main "
      "steam section in the event of a hydro-test requirement. However, the "
      "reheat section can "
      "be more difficult to isolate, due to the location and proximity to "
      "the turbine. The "
      "reheat lines are used to recover additional energy to increase "
      "efficiency and therefore, "
      "normally are used at lower pressures and on larger piping to minimize "
      "pressure losses "
      "through the piping. This is one of the reasons why there is often a "
      "reluctance to install "
      "valves in these lines, unless specifically required, because pressure "
      "loss could reduce "
      "efficiency.")
    P("Khi cần tiến hành thử áp lực nước, thường có rất ít điểm cô lập cho "
    "phép gói gọn phép thử "
      "trong khu vực quá nhiệt lại của nồi hơi. Điều này thường không phải "
      "là mối quan tâm của "
      "nhà sản xuất thiết bị gốc (OEM), mà của người sử dụng cuối, người sẽ "
      "cần hoàn thành công "
      "việc trong những năm tới.",
      "When a hydro-test needs to be carried out, there are often few "
      "isolation points that "
      "would allow the hydro-test to be contained within the reheat section "
      "of the boiler. This "
      "is generally not a concern of the OEM, but of the end-user who will "
      "need to complete the "
      "work in years to come.")
    P("Một giải pháp phổ biến là cắt ống và lắp mặt bích cùng các tấm bịt "
    "(blind) cho phép cô lập "
      "khu vực quá nhiệt lại. Đây có thể là giải pháp tốn kém.",
      "A common solution would be to cut the pipe and install flanges and "
      "blinds that will allow "
      "isolation of the reheat section. This can be a costly solution.")
    H("Giải pháp điển hình", "Typical Solution", h3)
    P("Một giải pháp cô lập quá nhiệt lại gồm một thân van rỗng được chọn "
    "kích thước với đường "
      "kính đầy đủ để giảm thiểu tổn thất áp lực. Van được lắp một nắp tiếp "
      "cận lớn kiểu gioăng "
      "áp lực để cho phép lắp một tấm bịt khi cần. Thường nắp này được lắp "
      "gioăng O-ring, nhưng "
      "cũng có thể lắp gioăng graphit cho các ứng dụng thử hơi nếu yêu "
      "cầu.",
      "A reheat isolation solution consists of an empty valve body sized "
      "with a full bore to "
      "minimize pressure loss. The valve is fitted with a large pressure "
      "seal access cover to "
      "allow the installation of a blind when required. This is normally "
      "fitted with an O-ring "
      "seal, but can also be fitted with a graphite gasket for steam test "
      "applications, if "
      "required.")
    FIG(27, F10.fig_f10_27())
    P("Sau khi lắp đặt, cơ cấu đóng được ép trước vào gioăng. Sau đó cơ cấu "
    "đóng gioăng áp lực "
      "được lắp lại và van có thể được cấp áp đến áp lực thử yêu cầu. Áp lực "
      "này tác dụng lên "
      "tấm bịt và khi áp lực tăng thì tải trọng đảm kín trên tấm bịt cũng "
      "tăng theo. Sau phép "
      "thử, có thể tháo tấm và đưa van trở lại thành một đường ống rỗng, "
      "đường kính đầy đủ để "
      "vận hành bình thường.",
      "Once installed, the closure is preloaded to the seal. The pressure "
      "seal closure is then "
      "reinstated and the valve can then be pressurized to the required test "
      "pressure. This "
      "pressure acts on the blind and as the pressure increases, so does the "
      "sealing load on the "
      "blind. Following the test, the plate can be removed and the valve "
      "reinstated to an empty "
      "full bore line for normal operation.")

    # ------------------------------------------------------------ 10.1.6
    H("10.1.6 Van chiết hơi tuabin", "10.1.6 Turbine Extraction Valves")
    P("Van chiết hơi tuabin là van kiểm dạng xoay hoặc van đĩa nghiêng, với "
    "bộ truyền động khí "
      "nén tác động đơn lắp bên hông hoặc phía trên. Ứng dụng: chiết hơi và "
      "xả hơi áp cao trong "
      "các nhà máy điện có tuabin hơi trung áp / hạ áp khởi động. Chức năng "
      "của van là ngăn hơi "
      "quá nhiệt lại quay trở lại tuabin khi sự cố ngắt (trip).",
      "Turbine extraction valves are a swing check valve / tilting disk "
      "valve with a side / top "
      "mounted single-acting pneumatic actuator. Application: Extraction "
      "service and HP exhaust "
      "service in power plants with IP / LP steam turbine start-up. It's "
      "function is to prevent "
      "the reheat steam from returning to turbine on trip.")
    H("Đặc điểm chính", "Main Features", h3)
    B(["«Bảo vệ kép», gồm đóng chắc chắn và đóng có hỗ trợ năng lượng.",
       "Đóng nhanh.",
       "Đảm kín chắc chắn."],
      ["Double protection, including positive closure and power-assisted "
      "closure.",
       "Fast closure.",
       "Positive tight seating."])
    FIG(28, F10.fig_f10_28())

    # ------------------------------------------------------------ 10.1.7
    H("10.1.7 Van đường vòng", "10.1.7 Bypass Valves")
    P("Trong các trường hợp van lớn phải chịu áp lực cao hoặc nhiệt độ cao, "
    "người ta thường lắp "
      "một van đường vòng nhỏ hơn để cân bằng áp lực hoặc để làm nóng đoạn "
      "ống phía dưới trước "
      "khi mở van lớn. Hình 10.29 trình bày một cách bố trí đường vòng điển "
      "hình. Hình 10.30 cho "
      "biết vị trí và kích cỡ tiêu chuẩn của các kết nối đường vòng và kết "
      "nối phụ trợ.",
      "In larger valve situations where high pressures and/or high "
      "temperatures are encountered, "
      "a smaller bypass valve is often installed to equalize pressure and/or "
      "to allow the pipe "
      "downstream to warm up before the larger valve is opened. Figure 10.29 "
      "shows a typical "
      "bypass arrangement. Figure 10.30 gives standard bypass and auxiliary "
      "connection "
      "locations and sizes.")
    FIG(29, F10.fig_f10_29())
    FIG(30, F10.fig_f10_30())

    # ------------------------------------------------------------ 10.1.8
    H("10.1.8 Van màng", "10.1.8 Diaphragm Valves")
    P("Van màng (đôi khi gọi là van Saunders) được thiết kế để điều tiết "
    "dòng chảy trong các "
      "dịch vụ ăn mòn, nơi thành phần của chất lưu trong đường ống có thể "
      "ảnh hưởng bất lợi tới "
      "các chi tiết của van. Ứng dụng khác của van màng là các dịch vụ không "
      "cho phép nhiễm bẩn "
      "từ nguồn bên ngoài, ví dụ công nghiệp dược phẩm và thực phẩm.",
      "Diaphragm valves (sometimes referred to as saunders valves) are "
      "designed to control flow "
      "in corrosive services where line content could adversely affect valve "
      "components. Other "
      "applications for diaphragm valves are in services where contamination "
      "from outside "
      "sources cannot be tolerated; for example, the pharmaceutical and food "
      "industries.")
    P("Van màng khác với các loại van khác ở chỗ thân van và chất lưu trong "
    "đường ống được cách "
      "ly với mọi bộ phận chuyển động của van bằng một màng mềm. Lớp màng "
      "mềm này ngăn rò rỉ "
      "bao bì chân van của chất lưu và ngăn nhiễm bẩn dòng chảy bởi chất bôi "
      "trơn của bao bì.",
      "Diaphragm valves differ from other valves in that the body of the "
      "valve and line content "
      "is sealed off from all moving parts of the valve by a flexible "
      "diaphragm. This flexible "
      "diaphragm seal prevents stem packing leakage of line content and flow "
      "contamination by "
      "packing lubricants.")
    P("Dù có nhiều biến thể của thiết kế van màng, hầu hết được xếp vào hai "
    "loại: dạng đập (weir-"
      "type) hoặc dạng thẳng (straightway-type).",
      "Even though there are many variations of diaphragm valve designs, "
      "most can be classified "
      "as either weir-type or straightway-type.")
    FIG(31, F10.fig_f10_31())
    P("Van màng dạng đập là loại van màng được dùng phổ biến nhất. Hình "
    "10.31 trình bày một van "
      "dạng đập điển hình cùng các thành phần chính của nó. Van màng dạng "
      "đập có một đoạn nhô "
      "lên (đập - weir) ở giữa thân van, đóng vai trò là điểm đảm kín cho "
      "màng mềm. Nhờ cách tạo "
      "hình đập trong thân van, hành trình của màng được rút ngắn, nhờ đó "
      "kéo dài tuổi thọ màng "
      "và giảm bảo trì tổng thể.",
      "Weir-type diaphragm valves are the most common type of diaphragm "
      "valve used. Figure 10.31 "
      "shows a typical weir-type valve along with is major components. The "
      "weir-type diaphragm "
      "valve incorporates a raised section (weir) halfway through the valve, "
      "which acts as a "
      "closure point for the flexible diaphragm. Because of the way the weir "
      "is formed in the "
      "body, diaphragm movement is shortened, which in turn prolongs "
      "diaphragm life and reduces "
      "overall maintenance.")
    FIG(32, F10.fig_f10_32())
    P("Van màng dạng thẳng không có đập trong thiết kế. Hình 10.32 trình bày "
    "một van dạng thẳng "
      "điển hình. Thiết kế này cho van một đường đi thông suốt, phù hợp với "
      "dòng chảy nhớt hoặc "
      "chứa chất rắn.",
      "Straightway-type diaphragm valves have no weir incorporated in the "
      "valve design. Figure "
      "10.32 shows a typical straightway valve. This design gives the valve "
      "an uninterrupted "
      "passageway suited for flows which are viscous or contain solids.")
    P("Có nhiều loại vật liệu màng tùy theo điều kiện dịch vụ và nhiệt độ. "
    "Vì van dạng thẳng cần "
      "hành trình màng dài hơn so với van dạng đập, lựa chọn vật liệu cho "
      "van dạng thẳng bị hạn "
      "chế hơn.",
      "There are many types of diaphragm materials available, depending on "
      "service and "
      "temperature conditions. Because longer diaphragm movement is needed "
      "in the straightway-"
      "type valve compared to the weir-type, material selection is limited "
      "for the straightway-"
      "type valve.")

    # ------------------------------------------------------------ 10.1.9
    H("10.1.9 Van kẹp", "10.1.9 Pinch Valves")
    P("Van kẹp, cũng như van màng, dùng một màng mềm trong việc đóng và mở "
    "van. Van kẹp dùng một "
      "ống mềm rỗng được bóp lại để ngăn dòng chảy bằng phương pháp thủ công "
      "hoặc có năng lượng. "
      "Một van kẹp đơn giản vận hành bằng khí nén được trình bày trong Hình "
      "10.33.",
      "The pinch valve, like the diaphragm valve, uses a flexible diaphragm "
      "in the closing and "
      "opening of the valve. Pinch valves use a flexible hollow sleeve which "
      "is pinched closed "
      "to stop flow by manual or power methods. A simple, air-operated pinch "
      "valve is shown in "
      "Figure 10.33.")
    FIG(33, F10.fig_f10_33())
    P("Van kẹp rất phù hợp cho các dịch vụ vận chuyển chất rắn lơ lửng, bùn "
    "và dòng bột rắn.",
      "Pinch valves are ideally suited in services which carry suspended "
      "matter, slurries, and "
      "solid powder flows.")

    # ------------------------------------------------------------ 10.1.10
    H("10.1.10 Van bi", "10.1.10 Ball Valves")
    P("Van bi, như tên gọi, chứa một nút hình cầu trong thân van để điều "
    "tiết dòng chảy. Quả bóng "
      "có một lỗ tròn hoặc đường dẫn chảy xuyên qua tâm và khi xoay một phần "
      "tư vòng thì dòng "
      "chảy bị ngăn. Van bi có ba kiểu phổ biến:",
      "The ball valve, as the name indicates, contains a ball-shaped plug "
      "within a valve body "
      "which regulates flow. The ball has a circular hole or flow-way "
      "through its center and "
      "when turned one-quarter of the way, the flow stops. Ball valves come "
      "in three general "
      "patterns:")
    B(["Cổng Venturi", "Cổng đầy đủ", "Cổng thu nhỏ (đôi khi gọi là cổng thường)"],
      ["Venture-port", "Full-port", "Reduced-port (sometimes referred to as regular-port)"])
    P("Các kiểu cổng cho biết đường kính bên trong của đường dẫn chảy qua "
    "quả bóng. Van bi cũng "
      "có thể được phân loại theo kiểu thân. Kiểu thân gồm thân một mảnh và "
      "thân nhiều mảnh. Một "
      "van bi cổng thu nhỏ (hoặc cổng thường) điển hình với thân nhiều mảnh "
      "được trình bày trong "
      "Hình 10.34.",
      "The port patterns indicate the inside diameter of the ball flow-way. "
      "Ball valves may also "
      "be classified by their body style. Body styles comes in one-piece and "
      "multi-piece bodies. "
      "A typical reduced-port (or regular-port) ball valve with a "
      "multi-piece body is shown in "
      "Figure 10.34.")
    FIG(34, F10.fig_f10_34())

    # ------------------------------------------------------------ 10.1.11
    H("10.1.11 Van bướm", "10.1.11 Butterfly Valves")
    P("Van bướm có thiết kế đơn giản, nhẹ, gọn và rẻ, đặc biệt ở kích cỡ van "
    "lớn. Van gồm một "
      "đĩa phẳng, tròn được bản lề ở tâm, đóng hoặc mở hoàn toàn bằng một "
      "phần tư vòng. Bề mặt "
      "đảm cho đĩa do ghế kim loại hoặc vật liệu mềm như elastomer và nhựa "
      "cung cấp. Nhờ những "
      "tiến bộ trong vật liệu làm ghế, van bướm đã được chấp nhận rộng rãi "
      "trong các lĩnh vực "
      "dầu, khí, hóa chất, nước và công nghiệp chế biến. Van thường được "
      "dùng thay van cổng, "
      "nhưng có thêm ưu điểm là điều tiết dòng chảy.",
      "The butterfly valve offers a simple design that is lightweight, "
      "compact, and inexpensive, "
      "particularly in larger valve sizes. It consists of a flat, circular "
      "disk hinged in its "
      "center, which closes or fully opens with a quarter turn. Seating for "
      "the disk is supplied "
      "by metal seats or resilient types of material like elastomers and "
      "plastics. Because of "
      "the advances in seating material, butterfly valves have found general "
      "acceptance in the "
      "oil, gas, chemical, water, and process fields. The valve is often "
      "used in place of a gate "
      "valve, but has the added advantage of flow regulation.")
    P("Van bướm có hai kiểu thân cơ bản:",
      "Butterfly valves are available in two basic body types:")
    B(["Dạng wafer (kẹp giữa hai mặt bích)", "Dạng hai mặt bích"],
      ["Wafer-type", "Double flanged-type"])
    P("Kiểu wafer (trình bày trong Hình 10.35) được lắp giữa hai mặt bích và "
    "được giữ tại chỗ "
      "bằng bulông mặt bích.",
      "The wafer-type (shown in Figure 10.35) is mounted between two flanges "
      "and is held in place "
      "by flange bolts.")
    FIG(35, F10.fig_f10_35())
    P("Trong trường hợp việc tháo rời thiết bị hoặc đường ống có thể yêu cầu "
    "tháo một trong các "
      "mặt bích giữ, có thể dùng van bướm wafer dạng tai (lug-wafer). Van "
      "bướm lug-wafer (trình "
      "bày trong Hình 10.36) có các tai ren, qua đó bulông mặt bích được vặn "
      "vào và giữ van tại "
      "chỗ ngay cả khi một mặt bích đã được tháo. Ở hầu hết van bướm wafer, "
      "lớp kín elastomer "
      "cũng đóng vai trò là gioăng mặt bích của chính nó.",
      "In situations where dismantling of equipment or lines may require "
      "disconnecting of one of "
      "the holding flanges, a lug-wafer butterfly valve can be used. The "
      "lug-wafer butterfly "
      "valve (shown in Figure 10.36) has tapped lugs through which the "
      "flange bolts are screwed "
      "and hold the valve in place, even when one flange is removed. In most "
      "wafer butterfly "
      "valves, the elastomer seal also acts as its own flange gasket.")
    FIG(36, F10.fig_f10_36())
    P("Van bướm hai mặt bích (trình bày trong Hình 10.37) có hai đầu mặt "
    "bích được bắt bulông "
      "riêng lẻ vào mặt bích của đường ống hoặc thiết bị. Gioăng được dùng "
      "giữa các đầu van và "
      "mặt bích nối.",
      "The double-flanged butterfly (shown in Figure 10.37) incorporates two "
      "flange ends which "
      "are bolted individually into the pipework or equipment flanges. "
      "Gaskets are used between "
      "the valve ends and connecting flanges.")
    FIG(37, F10.fig_f10_37())

    # ------------------------------------------------------------ 10.1.12
    H("10.1.12 Van cắm", "10.1.12 Plug Valves")
    P("Van cắm (còn gọi là van nút) gồm một nút cắm thuôn dần hoặc song song "
    "có thể xoay một phần "
      "tư vòng trong thân van. Phần tư vòng cho phép đóng hoàn toàn hoặc mở "
      "hoàn toàn van. Có hai "
      "loại van cắm cơ bản:",
      "Plug valves (also known as cock valves) consist of a tapered or "
      "parallel side plug which "
      "can be rotated a quarter turn within a valve body. The quarter turn "
      "gives full closure or "
      "fully open operation of the valve. There are two basic types of plug "
      "valves available:")
    B(["Van cắm bôi trơn", "Van cắm không bôi trơn"],
      ["Lubricated plug", "Non-lubricated plug"])
    P("Một biến thể của van cắm bôi trơn được trình bày trong Hình 10.38. "
    "Van cắm bôi trơn khác "
      "van cắm không bôi trơn ở chỗ nó có phương tiện bôi trơn các bề mặt "
      "đảm của van. Lớp bôi "
      "trơn này giúp tránh hiện tượng kẹt van mà vẫn cho đảm kín chắc chắn. "
      "Không nên dùng van "
      "cắm bôi trơn nếu nhiễm bẩn dòng chảy có thể thành vấn đề.",
      "One variation of the lubricated plug is shown in Figure 10.38. The "
      "lubricated plug differs "
      "from the non-lubricated plug in that it provides a means to lubricate "
      "the seating surfaces "
      "of the valve. This lubrication helps to eliminate valve seizing while "
      "still providing a "
      "positive seal. Lubricated plugs should not be used if flow "
      "contamination may be a problem.")
    FIG(38, F10.fig_f10_38())
    P("Thiết kế van cắm cũng phù hợp với các cách bố trí van nhiều cổng như "
    "trình bày trong Hình "
      "10.39.",
      "The plug valve design also lends itself to multi-port valve "
      "arrangements as shown in "
      "Figure 10.39.")
    FIG(39, F10.fig_f10_39())

    # ------------------------------------------------------------ dimension tables
    H("Bảng kích thước van", "Valve Dimension Tables")
    P("Phần còn lại của chương gồm các bảng kích thước mặt đối mặt "
    "(face-to-face) và đầu đến đầu "
      "(end-to-end) của van gang và van thép, lấy theo tiêu chuẩn ASME/ANSI "
      "B16.10. Kích thước "
      "được cho cả bằng inch và milimet; các con số milimet được làm tròn "
      "đến một chữ số thập "
      "phân. Các dấu «---» trong bảng có nghĩa là kích thước đó không được "
      "nêu trong tiêu chuẩn "
      "ASME/ANSI nhưng có thể có sẵn trên thị trường. Ở đây các bảng được "
      "trình bày dưới dạng "
      "hình vẽ lại, theo đúng thứ tự Hình 10.40 đến Hình 10.53.",
      "The remainder of the chapter consists of face-to-face and end-to-end "
      "dimension tables for "
      "cast iron and steel valves, taken from ASME/ANSI B16.10. Dimensions "
      "are given in both "
      "inches and millimeters, with millimeter values rounded off to the "
      "first decimal point. A "
      "«---» entry means the valve size is not shown in ASME/ANSI standards "
      "but may be "
      "commercially available. The tables are presented here as redrawn "
      "figures, in the order of "
      "Figures 10.40 through 10.53.")

    # ------------------------------------------------------------ fig 10.40
    H("Van cổng gang", "Cast Iron Gate Valves", h3)
    P("Bảng Hình 10.40 cho kích thước van cổng gang theo các cấp ANSI 125, "
    "250 và 800, với mặt "
      "bích phẳng (Flat Face / Class 125) và mặt bích nhô (Raised Face / "
      "Class 250 và Class 800). "
      "Kích thước được lấy từ khoảng cách mặt đối mặt của van và được liệt "
      "kê cho cả kiểu nêm "
      "đặc lẫn kiểu đĩa kép, tính theo đường kính ống danh nghĩa từ 1/4 in. "
      "đến 36 in.",
      "Figure 10.40 gives the dimensions of cast iron gate valves in ANSI "
      "Classes 125, 250 and "
      "800, with flat face (Class 125) and raised face (Class 250 and Class "
      "800). Dimensions are "
      "taken from the face-to-face of the valve and are listed for both "
      "solid-wedge and "
      "double-disk designs, for nominal pipe sizes from 1/4 in. to 36 in.")
    B(["Dấu «---» cho biết kích thước van không được nêu trong tiêu chuẩn "
    "ASME/ANSI nhưng có thể "
       "có sẵn trên thị trường.",
       "Kích thước milimet được làm tròn đến chữ số thập phân đầu tiên.",
       "Kích thước dựa trên tiêu chuẩn ASME/ANSI B16.10."],
      ["(---) Indicates valve size is not shown in ASME/ANSI standards but "
      "may be commercially "
       "available.",
       "Millimeter dimensions are rounded off to first decimal point.",
       "Dimensions based on ASME/ANSI B16.10 Standard."])
    FIG(40, F10.fig_f10_40())

    # ------------------------------------------------------------ fig 10.41
    H("Van cầu gang", "Cast Iron Globe Valves", h3)
    P("Bảng Hình 10.41 cho kích thước van cầu gang các cấp ANSI 125 và 250. "
    "Với van thẳng "
      "(straightway), kích thước lấy theo mặt đối mặt; với van góc (angle), "
      "kích thước lấy theo "
      "tâm đến mặt (center-to-face). Bảng gồm các cột cho van thẳng, van góc "
      "và van điều khiển, "
      "ứng với mặt bích phẳng (Class 125) và mặt bích nhô (Class 250).",
      "Figure 10.41 gives the dimensions of cast iron globe valves in ANSI "
      "Classes 125 and 250. "
      "For straightway valves the dimensions are taken face-to-face, and for "
      "angle valves "
      "center-to-face. The table includes columns for straightway, angle and "
      "globe control "
      "styles, with flat face (Class 125) and raised face (Class 250).")
    B(["Dấu «---» cho biết kích thước van không được nêu trong tiêu chuẩn "
    "ASME/ANSI nhưng có thể "
       "có sẵn trên thị trường.",
       "Kích thước milimet được làm tròn đến chữ số thập phân đầu tiên.",
       "Kích thước dựa trên tiêu chuẩn ASME/ANSI B16.10.",
       "Kích thước của van kiểm dạng nâng thẳng và van kiểm dạng xoay thẳng "
       "tiêu chuẩn có thể "
       "dùng thay cho kích thước van cầu thẳng (trừ van kiểm xoay thẳng đứng "
       "16 in. / 400 mm).",
       "Kích thước của van kiểm dạng nâng góc tiêu chuẩn có thể dùng thay cho "
       "kích thước van cầu "
       "góc."],
      ["(---) Indicates valve size is not shown in ASME/ANSI standards but "
      "may be commercially "
       "available.",
       "Millimeter dimensions are rounded off to first decimal point.",
       "Dimensions based on ASME/ANSI B16.10 Standard.",
       "Dimensions for standard straightway lift and swing check valves are "
       "interchangeable with "
       "straightway globe valve dimensions (excluding 16 in. (400 mm) "
       "vertical swing checks).",
       "Dimensions for standard angle lift check valves are interchangeable "
       "with angle globe "
       "valve dimensions."])
    FIG(41, F10.fig_f10_41())

    # ------------------------------------------------------------ fig 10.42
    H("Van cổng thép — Cấp 150", "Steel Gate Valve — Class 150", h3)
    P("Bảng Hình 10.42 cho kích thước van cổng thép cấp ANSI 150, lấy theo "
    "mặt đối mặt và đầu đến "
      "đầu của van. Bảng gồm bốn nhóm cột: mặt bích nhô / cấp 150 và đầu vát "
      "/ cấp 150, mỗi nhóm "
      " lại chia cho nêm đặc và đĩa kép, từ NPS 1/4 đến NPS 36. Nguồn không "
      "in ghi chú riêng cho "
      "bảng này, nhưng các ghi chú chung về ký hiệu «---», làm tròn milimet "
      "và tiêu chuẩn B16.10 "
      "vẫn áp dụng.",
      "Figure 10.42 gives the dimensions of steel gate valves in ANSI Class "
      "150, taken from "
      "face-to-face and end-to-end of the valves. The table has four column "
      "groups: raised face "
      "/ Class 150 and beveled end / Class 150, each split between solid "
      "wedge and double disk, "
      "from NPS 1/4 to NPS 36. The source prints no separate notes for this "
      "table, but the "
      "general notes on the «---» notation, millimeter rounding and B16.10 "
      "still apply.")
    P("Trong nhóm bảng van cổng thép, cụm «Raised Face» chỉ đầu nối mặt bích "
      "nhô, còn "
      "«Beveled End» chỉ đầu nối vát để hàn trực tiếp vào đường ống. Khi cả "
      "hai dạng đầu nối "
      "được nêu trong cùng một nhóm tiêu đề, các cột tương ứng cho biết "
      "kích thước mặt đối mặt "
      "hoặc đầu đến đầu của cùng một cỡ van. Cột «Short Pattern» chỉ phiên "
      "bản ngắn hơn, thường "
      "áp dụng cho van nắp gioăng áp lực hoặc van không mặt bích.",
      "Within the steel gate valve tables, «Raised Face» denotes a raised-face "
      "flanged end and "
      "«Beveled End» a beveled end for direct welding into the piping. Where "
      "both end types "
      "appear under one group heading, the corresponding columns give the "
      "face-to-face or "
      "end-to-end dimension of the same valve size. The «Short Pattern» "
      "column denotes the "
      "shorter version, generally applied to pressure seal or flangeless "
      "bonnet valves.")
    FIG(42, F10.fig_f10_42())

    # ------------------------------------------------------------ fig 10.43
    H("Van cổng thép — Cấp 300", "Steel Gate Valve — Class 300", h3)
    P("Bảng Hình 10.43 tiếp tục với van cổng thép cấp ANSI 300, cũng lấy "
    "kích thước theo mặt đối "
      "mặt và đầu đến đầu. Cấu trúc cột giống hệt bảng trước: mặt bích nhô / "
      "cấp 300 và đầu vát / "
      "cấp 300, mỗi nhóm gồm nêm đặc và đĩa kép. Dải kích thước NPS từ 1/4 "
      "đến 36. Các kích thước "
      "nhỏ hơn NPS 1-1/2 chỉ có số liệu cho kiểu nêm đặc; các ô còn lại để "
      "trống bằng «---».",
      "Figure 10.43 continues with steel gate valves in ANSI Class 300, "
      "again taken "
      "face-to-face and end-to-end. The column structure matches the "
      "previous table: raised face "
      "/ Class 300 and beveled end / Class 300, each with solid wedge and "
      "double disk. The size "
      "range is NPS 1/4 through 36. Sizes below NPS 1-1/2 carry figures for "
      "the solid-wedge "
      "design only; the remaining cells are shown as «---».")
    FIG(43, F10.fig_f10_43())

    # ------------------------------------------------------------ fig 10.44
    H("Van cổng thép — Cấp 400 và 600",
      "Steel Gate Valve — Class 400 and 600", h3)
    P("Bảng Hình 10.44 gồm van cổng thép cấp 400 và 600. Các nhóm cột gồm: "
    "mặt bích nhô và đầu "
      "vát / cấp 400; mặt bích nhô / cấp 600; đầu vát / cấp 600 — mỗi nhóm "
      "chia cho nêm đặc và "
      "đĩa kép — cùng một cột kiểu ngắn (Short Pattern) duy nhất ở cuối "
      "bảng. Kích thước lấy theo "
      "mặt đối mặt và đầu đến đầu, đơn vị inch và milimet.",
      "Figure 10.44 covers steel gate valves in Classes 400 and 600. The "
      "column groups are: "
      "raised face and beveled end / Class 400; raised face / Class 600; "
      "beveled end / Class 600, "
      "each split between solid wedge and double disk, plus a single Short "
      "Pattern column at the "
      "end. Dimensions are taken face-to-face and end-to-end, in inches and "
      "millimeters.")
    FIG(44, F10.fig_f10_44())

    # ------------------------------------------------------------ fig 10.45
    H("Van cổng thép — Cấp 900 và 1500",
      "Steel Gate Valve — Class 900 and 1500", h3)
    P("Bảng Hình 10.45 gồm van cổng thép cấp 900 và 1500, với các nhóm: mặt "
    "bích nhô và đầu vát / "
      "cấp 900; đầu vát / cấp 900; mặt bích nhô và đầu vát / cấp 1500. Mỗi "
      "nhóm gồm nêm đặc, đĩa "
      "kép và kiểu ngắn (Short Pattern). Ở các kích thước NPS 22 và một số ô "
      "khác, nguồn ghi "
      "«---» để biểu thị không có số liệu theo tiêu chuẩn.",
      "Figure 10.45 covers steel gate valves in Classes 900 and 1500, with "
      "groups for raised face "
      "and beveled end / Class 900; beveled end / Class 900; and raised face "
      "and beveled end / "
      "Class 1500. Each group includes solid wedge, double disk and Short "
      "Pattern. At NPS 22 and "
      "in several other cells the source records «---» where no standard "
      "figure exists.")
    FIG(45, F10.fig_f10_45())

    # ------------------------------------------------------------ fig 10.46
    H("Van cổng thép — Cấp 2500", "Steel Gate Valve — Class 2500", h3)
    P("Bảng Hình 10.46 (chú thích trong nguồn có một dấu chấm sau số hình) "
    "cho kích thước van cổng "
      "thép ANSI cấp 2500. Các nhóm cột gồm mặt bích nhô / cấp 2500 và đầu "
      "vát / cấp 2500, mỗi "
      "nhóm có nêm đặc và đĩa kép, cộng thêm cột kiểu ngắn. Bảng chỉ liệt kê "
      "đến NPS 18.",
      "Figure 10.46 (whose source caption carries a leading period after the "
      "figure number) gives "
      "the dimensions of steel gate valves in ANSI Class 2500. The column "
      "groups are raised face "
      "/ Class 2500 and beveled end / Class 2500, each with solid wedge and "
      "double disk, plus a "
      "Short Pattern column. The table lists sizes only up to NPS 18.")
    B(["Dấu «---» cho biết kích thước van không được nêu trong tiêu chuẩn "
    "ASME/ANSI nhưng có thể "
       "có sẵn trên thị trường.",
       "Kích thước milimet được làm tròn đến chữ số thập phân đầu tiên.",
       "Kích thước dựa trên tiêu chuẩn ASME/ANSI B16.10.",
       "Kích thước kiểu ngắn áp dụng cho van nắp gioăng áp lực hoặc van không "
       "mặt bích; đây là "
       "tùy chọn trên van nắp bắt bulông."],
      ["(---) Indicates valve size is not shown in ASME/ANSI standards but "
      "may be commercially "
       "available.",
       "Millimeter dimensions are rounded off to first decimal point.",
       "Dimensions based on ASME/ANSI B16.10 Standard.",
       "Short pattern dimensions apply to pressure seal or flange less bonnet "
       "valves (option on "
       "bolted bonnets)."])
    FIG(46, F10.fig_f10_46())

    # ------------------------------------------------------------ steel globe/check intro
    H("Van cầu và van kiểm thép", "Steel Globe and Check Valves", h3)
    P("Bảy bảng cuối (Hình 10.47 đến Hình 10.53) cho kích thước van cầu và "
      "van kiểm thép. "
      "Với van thẳng, "
      "kích thước lấy theo mặt đối mặt và đầu đến đầu; với van góc, kích "
      "thước lấy theo tâm đến "
      "mặt và tâm đến đầu. Các cột thường gặp gồm van cầu thẳng, van cầu "
      "góc, van cầu kiểu Y, van "
      "cầu điều khiển và van kiểm dạng xoay. Ghi chú liên tục được lặp lại "
      "trong nguồn: kích "
      "thước van điều khiển chỉ áp dụng cho van có mặt bích nhô.",
      "The last seven tables (Figures 10.47 through 10.53) give the "
      "dimensions of steel globe "
      "and check valves. For "
      "straightway valves the dimensions are taken face-to-face and "
      "end-to-end; for angle valves "
      "center-to-face and center-to-end. Common columns include straightway "
      "globe, angle globe, "
      "Y-pattern globe, control valve globe and swing check. A note is "
      "repeated throughout the "
      "source: control valve dimensions pertain to raised-face flange valves "
      "only.")
    P("Các bảng phân biệt rõ «Long Pattern» và «Short Pattern». Kiểu dài dùng "
      "đầu nối mặt bích "
      "nhô hoặc đầu vát theo cấp áp lực tương ứng; kiểu ngắn dùng đầu vát và "
      "được liệt kê riêng "
      "ở các cấp 600, 900, 1500 và 2500. Ở dòng tiêu đề, ký hiệu (*) sau "
      "«Control Valve Globe» "
      "được nguồn dùng để phân biệt cột van điều khiển với các cột van cầu "
      "thông thường.",
      "The tables distinguish clearly between Long Pattern and Short "
      "Pattern. The long "
      "pattern uses raised-face or beveled ends at the corresponding pressure "
      "class, while the "
      "short pattern uses beveled ends and is listed separately in Classes "
      "600, 900, 1500 and "
      "2500. In the headings the source marks «Control Valve Globe (*)» to "
      "distinguish the "
      "control-valve column from the ordinary globe valve columns.")

    # ------------------------------------------------------------ fig 10.47
    P("Hình 10.47 cho kích thước van cầu và van kiểm thép cấp ANSI 150, với "
    "các cột van cầu "
      "thẳng, van cầu góc, van cầu kiểu Y, van cầu điều khiển và van kiểm "
      "dạng xoay, từ NPS 1/4 "
      "đến NPS 36.",
      "Figure 10.47 gives the dimensions of steel globe and check valves in "
      "ANSI Class 150, with "
      "columns for straightway globe, angle globe, Y-pattern globe, control "
      "valve globe and swing "
      "check, from NPS 1/4 to NPS 36.")
    B(["Lưu ý: kích thước van điều khiển chỉ áp dụng cho van có mặt bích "
    "nhô."],
      ["Note: Control valve dimensions pertain to raised-face flange valves "
      "only."])
    FIG(47, F10.fig_f10_47())

    # ------------------------------------------------------------ fig 10.48
    P("Hình 10.48 cho kích thước van cầu và van kiểm thép cấp ANSI 300. Cấu "
    "trúc cột gồm van cầu "
      "thẳng, van cầu góc, van cầu điều khiển và van kiểm dạng xoay. Ở bảng "
      "này, nguồn viết ghi "
      "chú thiếu chữ «Note:» ở đầu dòng.",
      "Figure 10.48 gives the dimensions of steel globe and check valves in "
      "ANSI Class 300. The "
      "columns cover straightway globe, angle globe, control valve globe and "
      "swing check. In this "
      "table the source omits the leading word «Note:» from the note.")
    B(["Kích thước van điều khiển chỉ áp dụng cho van có mặt bích nhô."],
      ["Control valve dimensions pertain to raised face flange valves "
      "only."])
    FIG(48, F10.fig_f10_48())

    # ------------------------------------------------------------ fig 10.49
    P("Hình 10.49 gồm van cầu và van kiểm thép cấp 400 và 600, kiểu dài "
    "(Long Pattern). Mỗi cấp "
      "có bốn nhóm cột: van cầu thẳng, van cầu góc, van kiểm dạng xoay và — "
      "ở cột cuối — van kiểm "
      "xoay lại. Với cấp 600, các cột được nhân đôi cho cả hai dạng mặt bích "
      "nhô và đầu vát.",
      "Figure 10.49 covers steel globe and check valves in Classes 400 and "
      "600, Long Pattern. "
      "Each class has four column groups: straightway globe, angle globe and "
      "swing check, with a "
      "final swing-check column. For Class 600 the columns are duplicated "
      "for both raised face "
      "and beveled end.")
    FIG(49, F10.fig_f10_49())

    # ------------------------------------------------------------ fig 10.50
    P("Hình 10.50 là bảng kiểu ngắn (Short Pattern) cho van cầu và van kiểm "
    "thép cấp 600, đầu "
      "vát (Beveled End). Các cột gồm van cầu thẳng, van cầu góc, van kiểm "
      "dạng xoay và van cầu "
      "điều khiển. Đây là bảng duy nhất trong nhóm cấp 600 dùng riêng cho "
      "kiểu ngắn.",
      "Figure 10.50 is the Short Pattern table for steel globe and check "
      "valves in Class 600, "
      "Beveled End. The columns cover straightway globe, angle globe, swing "
      "check and control "
      "valve globe. This is the only Class 600 table in the group devoted "
      "entirely to the short "
      "pattern.")
    FIG(50, F10.fig_f10_50())

    # ------------------------------------------------------------ fig 10.51
    P("Hình 10.51 cho van cầu và van kiểm thép ANSI cấp 900, chia thành kiểu "
    "dài (Long Pattern, "
      "mặt bích nhô và đầu vát / cấp 900) và kiểu ngắn (Short Pattern, đầu "
      "vát / cấp 900). Mỗi "
      "kiểu gồm van cầu thẳng, van cầu góc và van kiểm dạng xoay.",
      "Figure 10.51 gives steel globe and check valves in ANSI Class 900, "
      "split into Long Pattern "
      "(raised face and beveled end / Class 900) and Short Pattern (beveled "
      "end / Class 900). "
      "Each pattern includes straightway globe, angle globe and swing "
      "check.")
    FIG(51, F10.fig_f10_51())

    # ------------------------------------------------------------ fig 10.52
    P("Hình 10.52 cho van cầu và van kiểm thép ANSI cấp 1500, cũng gồm kiểu "
    "dài và kiểu ngắn. "
      "Ở kiểu ngắn, bảng chỉ liệt kê van cầu thẳng và van kiểm dạng xoay, "
      "không có cột van cầu "
      "góc. Dải kích thước từ NPS 1/2 đến NPS 24.",
      "Figure 10.52 gives steel globe and check valves in ANSI Class 1500, "
      "again split into Long "
      "and Short Patterns. In the Short Pattern the table lists only "
      "straightway globe and swing "
      "check, with no angle-globe column. The size range runs from NPS 1/2 "
      "to NPS 24.")
    FIG(52, F10.fig_f10_52())

    # ------------------------------------------------------------ fig 10.53
    P("Hình 10.53 là bảng cuối của chương, cho van cầu và van kiểm thép ANSI "
    "cấp 2500 gồm kiểu "
      "dài và kiểu ngắn. Đây là bảng duy nhất trong nhóm van cầu và van kiểm "
      "có đầy đủ sáu ghi "
      "chú, bao gồm cả các ghi chú về khả năng thay thế kích thước giữa van "
      "kiểm dạng nâng và van "
      "cầu, và về kích thước kiểu ngắn áp dụng cho van nắp gioăng áp lực "
      "hoặc van không mặt bích.",
      "Figure 10.53 is the final table of the chapter, covering steel globe "
      "and check valves in "
      "ANSI Class 2500 in both Long and Short Patterns. It is the only table "
      "in the globe and "
      "check group to carry all six notes, including those on "
      "interchangeability of lift-check "
      "and globe valve dimensions and on short pattern dimensions applying "
      "to pressure seal or "
      "flangeless bonnet valves.")
    B(["Dấu «---» cho biết kích thước van không được nêu trong tiêu chuẩn "
    "ASME/ANSI nhưng có thể "
       "có sẵn trên thị trường.",
       "Kích thước milimet được làm tròn đến chữ số thập phân đầu tiên.",
       "Kích thước dựa trên tiêu chuẩn ASME/ANSI B16.10.",
       "Kích thước của van kiểm dạng nâng thẳng tiêu chuẩn có thể dùng thay "
       "cho kích thước van "
       "cầu thẳng nêu ở bảng trên.",
       "Kích thước của van kiểm dạng nâng góc có thể dùng thay cho kích thước "
       "van cầu góc nêu "
       "trong các bảng.",
       "Kích thước kiểu ngắn áp dụng cho van nắp gioăng áp lực hoặc van không "
       "mặt bích; đây là "
       "tùy chọn trên van nắp bắt bulông."],
      ["(---) Indicates valve size is not shown in ASME/ANSI standards but "
      "may be commercially "
       "available.",
       "Millimeter dimensions are rounded off to first decimal point.",
       "Dimensions based on ASME/ANSI B16.10 Standard.",
       "Standard straightway lift check valve dimensions are interchangeable "
       "with straightway "
       "globe valve dimensions given above.",
       "Angle lift check valve dimensions are interchangeable with angle "
       "globe valve dimensions "
       "given in tables.",
       "Short pattern dimensions apply to pressure seal or flangeless bonnet "
       "valves (option on "
       "bolted bonnets)."])
    FIG(53, F10.fig_f10_53())

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 10 chiếm tr. 210–239 của bản in (30 trang) trong Emerson, "
    "Control Valve Handbook, "
      "ấn bản 6 (2020). Nội dung gồm mục 10.1 với mười hai mục con từ 10.1.1 "
      "đến 10.1.12, tiếp "
      "theo là các bảng kích thước van gang và van thép. Năm mươi ba hình "
      "được vẽ lại dạng vector "
      "và đặt theo thứ tự số tại vị trí văn bản hợp lý.",
      "Chapter 10 occupies printed pp. 210-239 (30 pages) of Emerson, "
      "Control Valve Handbook, 6th "
      "edition (2020). It contains section 10.1 with twelve subsections, "
      "10.1.1 through 10.1.12, "
      "followed by the cast iron and steel valve dimension tables. The 53 "
      "numbered figures are "
      "redrawn as vectors and placed in numbered order at their logical "
      "prose points.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội "
    "dung gốc © 2020 Emerson "
      "Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original "
      "content © 2020 Emerson "
      "Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
