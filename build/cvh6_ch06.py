# -*- coding: utf-8 -*-
"""Book 7c, Chapter 6 - Special and Severe Service Control Valves (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 150-161.
This is a reference chapter: high-capacity and very-low-Cv valves, high-temperature
and cryogenic designs, cavitation and particulate trims, customized characteristics,
noise abatement, nuclear service qualification, and resistance to sulfide stress
cracking. Nine numbered figures are redrawn as vector schematics in `cvh6fig6.py`
and placed at their logical prose points.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul
import cvh6fig6 as F6

PAGES_SRC = 12          # source printed pp. 150-161 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Special and Severe Service Control Valves"
TITLE_VI = "Van điều khiển cho dịch vụ đặc biệt và khắc nghiệt"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> high-capacity valve — van công suất lớn · "
            "high-performance butterfly valve — van bướm hiệu năng cao · static pressure load — "
            "tải áp suất tĩnh · unbalance force — lực mất cân bằng · splined shaft — trục then · "
            "very-low Cv — hệ số Cv rất nhỏ · deadband — vùng chết · hysteresis — độ trễ · "
            "extension bonnet — nắp kéo dài · packing box — hộp đệm · cryogenic — đông lạnh · "
            "flashing — hóa hơi · cavitation — xâm thực · particulate — hạt rắn · "
            "anti-cavitation trim — trim chống xâm thực · DST (disk stack trim) — trim đĩa xếp "
            "chồng · inherent characteristic — đặc tính vốn có · noise abatement — giảm ồn · "
            "ASME Section III — Mục III của Bộ luật ASME · 10CFR50 Appendix B — Phụ lục B của "
            "10CFR50 · N stamp — tem dấu N · hydrostatic testing — thử áp lực thủy tĩnh · "
            "seismic qualification — thẩm định địa chấn · sulfide stress cracking (SSC) — nứt "
            "do ứng suất trong môi trường H2S · sour service — dịch vụ chua chứa H2S · "
            "hardness limit — giới hạn độ cứng · HRC — độ cứng Rockwell C · heat-affected zone "
            "(HAZ) — vùng ảnh hưởng nhiệt · post-weld heat treatment (PWHT) — xử lý nhiệt sau hàn · "
            "carbon equivalent (CE) — giá trị tương đương carbon")
    return (
        "<b>Key terms in this chapter.</b> high-capacity valve · high-performance butterfly valve · "
        "static pressure load · unbalance force · splined shaft · very-low Cv · deadband · "
        "hysteresis · extension bonnet · packing box · cryogenic · flashing · cavitation · "
        "particulate · anti-cavitation trim · DST (disk stack trim) · inherent characteristic · "
        "noise abatement · ASME Section III · 10CFR50 Appendix B · N stamp · hydrostatic testing · "
        "seismic qualification · sulfide stress cracking (SSC) · sour service · hardness limit · "
        "HRC · heat-affected zone (HAZ) · post-weld heat treatment (PWHT) · carbon equivalent (CE)")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Trong bản dump văn bản, chú thích Hình 6.4 xuất hiện "
            "trước chú thích Hình 6.3 trên cùng trang in 152; ở đây các hình được đặt theo thứ tự "
            "số, tức 6.3 trước 6.4, đúng vị trí văn bản hợp lý. Chú thích gốc của Hình 6.4 ghi "
            "«Very Low Flow Rates» trong khi tiêu đề mục là «Low-Flow Cv»; giữ nguyên chú thích gốc. "
            "(2) Các lỗi OCR «compontents» (thay cho components, mục 6.7), «in1975» (thiếu dấu cách), "
            "«MRO103/ISO 17945» (chữ O thay số 0) và «MR0103ISO 17945» (thiếu dấu gạch chéo) được "
            "giữ nguyên ở bản Anh và giải thích tại đây; bản Việt hiệu đính theo ý đúng. "
            "(3) Mục 6.4 in «below -101°C (150°F)» — giá trị °F thiếu dấu trừ có ở giá trị °C; "
            "giữ nguyên theo bản in. (4) Mục 6.3 giữ nguyên các con số in là 0,04 đến 0,08% và "
            "WC9 dùng tới 593°C (1100°F). (5) Đoạn Canada ở cuối mục 6.7 lặp lại cụm «Section III "
            "does apply…» và nêu chu kỳ sửa đổi là các phụ lục nửa năm, khác với cụm «ấn bản mới "
            "mỗi ba năm» ở đoạn Hoa Kỳ; cả hai được giữ nguyên. Dù thảo luận về bảo đảm chất lượng "
            "hạt nhân, lớp văn bản chương này không nêu rõ tên tiêu chuẩn NQA-1. "
            "(6) Bảng về các lớp van Mục III và về giới hạn độ cứng được gom từ các phát biểu rời "
            "rạc trong văn bản, không phải bảng có trong bản in. (7) Các hình trong bản in là ảnh "
            "chụp hoặc bản vẽ; ở đây vẽ lại dạng sơ đồ vector minh họa, không phải hình gốc.")
    return (
        "<b>Source notes.</b> (1) In the text dump the caption for Figure 6.4 appears before that "
        "of Figure 6.3 on printed p. 152; the figures are placed here in numbered order, 6.3 before "
        "6.4, at their logical prose points. The original caption for Figure 6.4 reads "
        "<i>Very Low Flow Rates</i> while the section heading is <i>Low-Flow Cv</i>; the original "
        "caption is preserved. (2) The OCR typos <i>compontents</i> (for components, 6.7), "
        "<i>in1975</i> (missing space), <i>MRO103/ISO 17945</i> (letter O for zero) and "
        "<i>MR0103ISO 17945</i> (missing slash) are retained in English and explained here; the "
        "Vietnamese text corrects them. (3) Section 6.4 prints <i>below -101°C (150°F)</i> - the °F "
        "value lacks the minus sign shown on the °C value; kept as printed. (4) Section 6.3 keeps "
        "the printed figures of 0.04 to 0.08% carbon and WC9 used up to 593°C (1100°F). "
        "(5) The Canadian passage at the end of 6.7 repeats the phrase <i>Section III does apply…</i> "
        "and gives a semi-annual addenda revision cycle, differing from the three-year new-edition "
        "cycle in the U.S. passage; both are retained. Although nuclear quality assurance is "
        "discussed, the chapter's text layer never names the NQA-1 standard. "
        "(6) The tables of Section III valve classes and of hardness limits are consolidated from "
        "statements scattered in the prose, not tables in the printed source. "
        "(7) Figures are photographs or line drawings in print; they are redrawn here as "
        "illustrative vector schematics, not the original images.")


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
        "Chương này là tài liệu tham khảo về van điều khiển cho dịch vụ đặc biệt và khắc nghiệt: "
        "van công suất lớn và van có hệ số Cv rất nhỏ, thiết kế cho nhiệt độ cao và đông lạnh, trim "
        "chống xâm thực và xử lý hạt rắn, đặc tính tùy biến, giảm ồn, bảo đảm chất lượng cho dịch vụ "
        "hạt nhân và khả năng chống nứt do ứng suất sunfat."
        if vi else
        "This chapter is a reference on control valves for special and severe service: high-capacity "
        "and very-low-Cv valves, designs for high temperature and cryogenic duty, trims for "
        "cavitation and particulate, customized characteristics, noise abatement, nuclear service "
        "qualification, and resistance to sulfide stress cracking."))
    N(note_terms("vi"), note_terms("en"))

    P("Như đã thảo luận ở các chương trước, van điều khiển tiêu chuẩn đáp ứng được nhiều ứng dụng "
      "điều khiển. Phạm vi ứng dụng tiêu chuẩn có thể được xem là nằm trong: áp suất khí quyển đến "
      "414 bar (6000 psig), từ -101°C (-150°F) đến 232°C (450°F), hệ số lưu lượng Cv từ 1,0 đến "
      "25000, và các giới hạn do những tiêu chuẩn công nghiệp thông thường đặt ra. Tất nhiên, "
      "tính ăn mòn và độ nhớt của chất lỏng, tỷ lệ rò rỉ và nhiều yếu tố khác vẫn cần được xem xét "
      "ngay cả với ứng dụng tiêu chuẩn. Có lẽ nhu cầu cân nhắc kỹ lưỡng khi lựa chọn van trở nên "
      "quan trọng hơn đối với các ứng dụng nằm ngoài những giới hạn tiêu chuẩn nêu trên.",
      "As discussed in previous chapters, standard control valves can handle a wide range of "
      "control applications. The range of standard applications can be defined as being encompassed "
      "by: atmospheric pressure and 414 bar (6000 psig), -101°C (-150°F) and 232°C (450°F), flow "
      "coefficient Cv values of 1.0 and 25000, and the limits imposed by common industrial "
      "standards. Certainly, corrosiveness and viscosity of the fluid, leakage rates, and many "
      "other factors demand consideration even for standard applications. Perhaps the need for "
      "careful consideration of valve selection becomes more critical for applications outside "
      "the standard limits mentioned above.")
    P("Chương này thảo luận một số ứng dụng đặc biệt và các biến đổi van điều khiển hữu ích để "
      "điều khiển chúng, thiết kế và vật liệu cho dịch vụ khắc nghiệt, cùng các yêu cầu thử nghiệm "
      "hữu ích cho van dùng trong nhà máy điện hạt nhân.",
      "This chapter discusses some special applications and control valve modifications useful in "
      "controlling them, designs and materials for severe service, and test requirements useful "
      "for control valves used in nuclear power plant service.")

    # ------------------------------------------------------------ 6.1
    H("6.1 Van điều khiển công suất lớn", "6.1 High-Capacity Control Valves")
    P("Nhìn chung, van dạng cầu lớn hơn NPS 12, van bi lớn hơn NPS 24 và van bướm hiệu năng cao "
      "lớn hơn NPS 48 thuộc nhóm van đặc biệt. Khi kích thước van tăng theo cấp số cộng, tải áp "
      "suất tĩnh khi đóng tăng theo cấp số nhân. Do đó độ bền trục, tải ổ đỡ, lực mất cân bằng và "
      "lực đẩy có sẵn của cơ cấu chấp hành đều trở nên quan trọng hơn khi van lớn dần. Thường thì "
      "chênh áp tối đa cho phép được giảm trên van lớn để giữ yêu cầu thiết kế và cơ cấu chấp hành "
      "trong giới hạn hợp lý. Ngay cả với cấp áp lực làm việc đã hạ thấp, năng lực lưu lượng của "
      "một số van lưu lượng lớn vẫn rất lớn.",
      "Generally, globe-style valves larger than NPS 12, ball valves over NPS 24, and "
      "high-performance butterfly valves larger than NPS 48 fall in the special valve category. "
      "As valve sizes increase arithmetically, static pressure loads at shutoff increase "
      "geometrically. Consequently, shaft strength, bearing loads, unbalance forces, and available "
      "actuator thrust all become more significant with increasing valve size. Normally maximum "
      "allowable pressure drop is reduced on large valves to keep design and actuator requirements "
      "within reasonable limits. Even with lowered working pressure ratings, the flow capacity of "
      "some large-flow valves remains tremendous.")
    FIG(1, F6.fig_f6_01())
    P("Van bướm hiệu năng cao cho hiệu năng xuất sắc trong điều kiện áp suất và nhiệt độ cực đoan. "
      "Van duy trì đóng kín và có thể được chỉ định cho nhiều điều kiện áp suất và nhiệt độ. Trục "
      "dẫn then ghép với nhiều loại cơ cấu chấp hành màng-lò xo hoặc piston khí nén, tạo nên van "
      "bướm hiệu năng cao đáng tin cậy cho nhiều ứng dụng điều tiết và đóng/mở trong các ngành "
      "quá trình khác nhau. Trong số nhiều gioăng động có thể dùng cho nhiều ứng dụng khó khăn, "
      "với lựa chọn gioăng và vật liệu chế tạo phù hợp, gioăng hỗ trợ áp suất cho khả năng đóng kín "
      "xuất chúng.",
      "High-performance butterfly valves provide outstanding performance under extreme pressure "
      "and temperature conditions. The valve maintains tight shutoff and can be specified for a "
      "wide range of pressure and temperature conditions. A splined drive shaft combines with a "
      "variety of spring-and-diaphragm or pneumatic piston actuators to make the valve a reliable, "
      "high-performance butterfly valve for a variety of throttling and on-off applications in "
      "the various process industries. One of several dynamic seals that can be used in a variety "
      "of demanding applications, with the appropriate seal selection and materials of "
      "construction, the pressure-assisted seal provides excellent shutoff.")
    P("Các cấu kiện làm phức tạp việc lắp đặt và bảo trì. Việc đưa cụm thân van vào đường ống và "
      "tháo, thay thế các bộ phận trim chính cần đến palăng tải trọng lớn.",
      "Components complicate installations and maintenance procedures. Installation of the valve "
      "body assembly into the pipeline and removal and replacement of major trim parts require "
      "heavy-duty hoists.")
    P("Mức ồn phải được cân nhắc cẩn thận trong mọi lắp đặt lưu lượng lớn, vì mức áp suất âm tăng "
      "tỷ lệ thuận với độ lớn của dòng chảy. Để giữ tiếng ồn do van phát sinh trong giới hạn cho "
      "phép, đã phát triển các thiết kế thân van đúc hoặc chế tạo lớn (Hình 6.2). Những thân này, "
      "thường dạng cage, dùng hành trình nút van đặc biệt dài, rất nhiều lỗ dòng chảy nhỏ xuyên "
      "thành cage và đầu nối đường ống ra được mở rộng nhằm giảm mức ồn đầu ra và hạ vận tốc chất "
      "lưu lượng.",
      "Noise levels must be carefully considered in all large-flow installations because sound "
      "pressure levels increase in direct proportion to flow magnitude. To keep valve-originated "
      "noise within tolerable limits, large cast or fabricated valve body designs (Figure 6.2) "
      "have been developed. These bodies, normally cage-style construction, use unusually long "
      "valve plug travel, a great number of small flow openings through the wall of the cage, and "
      "an expanded outlet line connection to minimize noise output and reduce fluid velocity.")
    FIG(2, F6.fig_f6_02())
    P("Tự nhiên là yêu cầu cơ cấu chấp hành rất khắc nghiệt, và người ta thường chỉ định piston "
      "khí nén tác động kép, hành trình dài cho các ứng dụng lưu lượng lớn. Kích thước và trọng "
      "lượng vật lý của van cùng các bộ phận cơ cấu chấp hành làm phức tạp việc lắp đặt và bảo trì. "
      "Việc đưa cụm thân van vào đường ống và tháo, thay thế các bộ phận trim chính cần palăng tải "
      "trọng lớn. Nhân viên bảo trì phải tuân thủ chặt chẽ sổ tay hướng dẫn của nhà sản xuất để "
      "giảm thiểu nguy cơ chấn thương.",
      "Naturally, actuator requirements are severe, and long-stroke, double-acting pneumatic "
      "pistons are typically specified for large-flow applications. The physical size and weight "
      "of the valve and actuator components complicate installation and maintenance procedures. "
      "Installation of the valve body assembly into the pipeline and removal and replacement of "
      "major trim parts require heavy-duty hoists. Maintenance personnel must follow the "
      "manufacturers' instruction manuals closely to minimize risk of injury.")
    P("Một số cấp áp suất trung gian và năng lực công suất lớn có thể đáp ứng bằng thân rèn khối. "
      "Có thể thiết kế cả dạng cầu lẫn dạng góc. Chúng được thiết kế theo ASME B16.34 với bích tích "
      "hợp.",
      "Some of the intermediate ratings and high capacity can be met with block forged bodies. "
      "Both globe and angle design can be designed. They are designed in accordance to ASME B16.34 "
      "with integral flanges.")
    FIG(3, F6.fig_f6_03())

    # ------------------------------------------------------------ 6.2
    H("6.2 Van điều khiển Cv thấp", "6.2 Low-Flow Cv Control Valves")
    FIG(4, F6.fig_f6_04())
    P("Ngoài các ngành chế biến nói chung, có nhiều ứng dụng trong phòng thí nghiệm và nhà máy thí "
      "điểm cần điều khiển lưu lượng cực nhỏ. Các ứng dụng này thường được xử lý theo một trong hai "
      "cách.",
      "Many applications exist in laboratories and pilot plants in addition to the general "
      "processing industries where control of extremely low flow rates is required. These "
      "applications are commonly handled in one of two ways.")
    P("Thứ nhất, thường có sẵn trim đặc biệt lắp trong thân van điều khiển tiêu chuẩn. Trim đặc biệt "
      "thường gồm vòng đế van và nút van được thiết kế và gia công với dung sai rất chặt để điều "
      "khiển chính xác dòng rất nhỏ. Những cấu trúc này thường xử lý được hệ số lưu lượng thấp tới "
      "0,03. Dùng các trim đặc biệt này trong van tiêu chuẩn mang lại tính kinh tế bằng cách giảm "
      "nhu cầu tồn kho phụ tùng cho van và cơ cấu chấp hành đặc biệt. Cách tiếp cận này cũng giúp "
      "dễ dàng mở rộng lưu lượng trong tương lai chỉ bằng cách thay thế các bộ phận trim trong thân "
      "van tiêu chuẩn.",
      "First, special trims are often available in standard control valve bodies. The special trim "
      "is typically made up of a seat ring and valve plug that have been designed and machined to "
      "very close tolerances to allow accurate control of very small flows. These types of "
      "constructions can often handle flow coefficients as low as 0.03. Using these special trims "
      "in standard control valves provides economy by reducing the need for spare parts inventory "
      "for special valves and actuators. Using this approach also makes future flow expansions easy "
      "by simply replacing the trim components in the standard control valve body.")
    P("Các thiết kế lưu lượng thấp có vùng chết và độ trễ thấp, năng lực dòng lớn, đặc tính điều "
      "khiển xuất sắc, đóng kín và hệ thống đệm tiên tiến để đáp ứng điều kiện dịch vụ khó khăn.",
      "The low flow designs feature low deadband and hysteresis, high flow capacity, superb control "
      "characteristics, tight shutoff and advanced packing systems to meet demanding service "
      "conditions.")
    P("Những van này thường xử lý hệ số lưu lượng thấp tới 0,000001. Ngoài dòng cực nhỏ, các van "
      "điều khiển chuyên dụng này nhỏ gọn và nhẹ vì thường dùng trong môi trường phòng thí nghiệm "
      "với đường ống hoặc ống dẫn thành rất mỏng. Chúng được thiết kế đặc biệt để điều khiển chính "
      "xác các ứng dụng chất lỏng hoặc khí có lưu lượng rất nhỏ.",
      "These valves often handle flow coefficients as low as 0.000001. In addition to the very low "
      "flows, these specialty control valves are compact and lightweight because they are often "
      "used in laboratory environments where very light schedule piping/tubing is used. These "
      "types of control valves are specially designed for the accurate control of very low flowing "
      "liquid or gaseous fluid applications.")

    # ------------------------------------------------------------ 6.3
    H("6.3 Van điều khiển nhiệt độ cao", "6.3 High-Temperature Control Valves")
    P("Van điều khiển dùng ở nhiệt độ trên 232°C (450°F) phải được thiết kế và chỉ định với điều "
      "kiện nhiệt độ được tính đến. Ở nhiệt độ cao, chẳng hạn có thể gặp trong hệ thống nước cấp "
      "lò hơi và hệ thống bypass bộ quá nhiệt, vật liệu chế tạo van tiêu chuẩn có thể không đủ. "
      "Ví dụ, nhựa, elastomer và gioăng tiêu chuẩn thường không phù hợp và phải thay bằng vật liệu "
      "bền hơn. Luôn dùng vật liệu đế kim loại-kim loại. Thường dùng đệm than chì mềm dạng bán kim "
      "loại hoặc Many lớp, và cần gioăng bằng thép không gỉ quấn xoắn ốc với than chì mềm.",
      "Control valves for service at temperatures above 232°C (450°F) must be designed and "
      "specified with the temperature conditions in mind. At elevated temperatures, such as those "
      "that may be encountered in boiler feedwater systems and superheater bypass systems, the "
      "standard materials of control valve construction might be inadequate. For instance, "
      "plastics, elastomers, and standard gaskets generally prove unsuitable and must be replaced "
      "by more durable materials. Metal-to-metal seating materials are always used. Semi-metallic "
      "or laminated flexible graphite packing materials are commonly used, and spiral-wound "
      "stainless steel and flexible graphite gaskets are necessary.")
    P("Thép Cr-Mo thường được dùng cho thân đúc ở nhiệt độ trên 538°C (1000°F). ASTM A217 Grade WC9 "
      "được dùng tới 593°C (1100°F). Với nhiệt độ tới 816°C (1500°F), vật liệu thường chọn là ASTM "
      "A351 Grade CF8M, thép không gỉ Type 316. Trong khoảng từ 538°C (1000°F) đến 816°C (1500°F), "
      "hàm lượng carbon phải được kiểm soát ở mức cao của dải, 0,04 đến 0,08%. Vật liệu 9%Cr−1%Mo−V "
      "như ASTM A217 grade C12a dạng đúc và ASTM A182 grade F91 dạng rèn được dùng ở nhiệt độ tới "
      "650°C (1200°F).",
      "Cr-Mo steels are often used for the valve body castings for temperatures above 538°C "
      "(1000°F). ASTM A217 Grade WC9 is used up to 593°C (1100°F). For temperatures up to 816°C "
      "(1500°F) the material usually selected is ASTM A351 Grade CF8M, Type 316 stainless steel. "
      "For temperatures between 538°C (1000°F) and 816°C (1500°F), the carbon content must be "
      "controlled to the upper end of the range, 0.04 to 0.08%. The 9%Cr−1%Mo−V materials, such as "
      "ASTM A217 grade C12a castings and ASTM A182 grade F91 forgings are used at temperatures up "
      "to 650°C (1200°F).")
    P("Nắp kéo dài giúp bảo vệ các bộ phận hộp đệm khỏi nhiệt độ cực cao. Vật liệu trim điển hình "
      "gồm hợp kim gốc coban 6, thép 316 phủ cứng alloy 6 và thép không gỉ 422 tôi nitơ.",
      "Extension bonnets help protect packing box parts from extremely high temperatures. Typical "
      "trim materials include cobalt-based alloy 6, 316 with alloy 6 hardfacing, and nitrided 422 "
      "SST.")

    # ------------------------------------------------------------ 6.4
    H("6.4 Van cho dịch vụ đông lạnh", "6.4 Cryogenic Service Valves")
    P("Đông lạnh là khoa học nghiên cứu vật liệu và quá trình ở nhiệt độ dưới -101°C (150°F). Đối "
      "với ứng dụng van điều khiển trong dịch vụ đông lạnh, nhiều vấn đề cần được xem xét giống như "
      "với van nhiệt độ cao. Các cấu kiện nhựa và elastomer thường ngừng hoạt động đúng cách ở nhiệt "
      "độ dưới -18°C (0°F). Trong dải nhiệt độ này, các cấu kiện như đệm kín và gioăng nút cần được "
      "xem xét đặc biệt. Với gioăng nút, gioăng mềm tiêu chuẩn trở nên rất cứng và kém dẻo, do đó "
      "không đạt được độ kín như đế mềm. Đã dùng các elastomer đặc biệt ở nhiệt độ này nhưng cần tải "
      "trọng đặc biệt để đạt được độ kín chặt.",
      "Cryogenics is the science dealing with materials and processes at temperatures below "
      "-101°C (150°F). For control valve applications in cryogenic services, many of the same "
      "issues need consideration as with high-temperature control valves. Plastic and elastomeric "
      "components often cease to function appropriately at temperatures below -18°C (0°F). In "
      "these temperature ranges, components such as packing and plug seals require special "
      "consideration. For plug seals, a standard soft seal will become very hard and less pliable "
      "thus not providing the shutoff required from a soft seat. Special elastomers have been "
      "applied in these temperatures but require special loading to achieve a tight seal.")
    P("Đệm kín là mối lo ngại trong ứng dụng đông lạnh vì sương giá có thể hình thành trên van. Hơi "
      "ẩm từ khí quyển ngưng tụ trên bề mặt lạnh hơn và khi nhiệt độ bề mặt dưới điểm đóng băng, hơi "
      "ẩm sẽ đóng thành lớp sương giá. Khi sương và băng hình thành trên vùng nắp và thân van và khi "
      "thân van được cơ cấu chấp hành di chuyển, lớp sương trên thân bị kéo qua đệm kín gây rách và "
      "do đó mất độ kín. Giải pháp là dùng nắp kéo dài (Hình 6.5) để vùng hộp đệm của van được làm ấm "
      "bởi nhiệt độ môi trường, ngăn sương giá hình thành trên thân và vùng hộp đệm. Chiều dài của "
      "nắp kéo dài phụ thuộc vào nhiệt độ ứng dụng và yêu cầu cách nhiệt. Ứng dụng càng lạnh thì nắp "
      "kéo dài càng dài.",
      "Packing is a concern in cryogenic applications because of the frost that may form on valves "
      "in cryogenic applications. Moisture from the atmosphere condensates on colder surfaces and "
      "where the temperature of the surface is below freezing, the moisture will freeze into a "
      "layer of frost. As this frost and ice forms on the bonnet and stem areas of control valves "
      "and as the stem is stroked by the actuator, the layer of frost on the stem is drawn through "
      "the packing causing tears and thus loss of seal. The solution is to use extension bonnets "
      "(Figure 6.5) that allow the packing box area of the control valve to be warmed by ambient "
      "temperatures, thus preventing frost from forming on the stem and packing box areas. The "
      "length of the extension bonnet depends on the application temperature and insulation "
      "requirements. The colder the application, the longer the extension bonnet required.")
    FIG(5, F6.fig_f6_05())
    P("Vật liệu chế tạo cho ứng dụng đông lạnh nói chung là thân và nắp CF8M với trim thép không gỉ "
      "dãy 300. Trong ứng dụng có hóa hơi, có thể cần phủ cứng để chống xói mòn.",
      "Materials of construction for cryogenic applications are generally CF8M body and bonnet "
      "material with 300 series stainless steel trim material. In flashing applications, hard "
      "facing might be required to combat erosion.")

    # ------------------------------------------------------------ 6.5
    H("6.5 Van chịu xâm thực và chất lưu có hạt rắn",
      "6.5 Valves Subjected to Cavitation and Fluids with Particulate")
    P("Áp suất và nhiệt độ trong các cơ sở chế biến và khai thác dầu hiện nay tiếp tục tăng. Khi "
      "đó, khả năng xảy ra xâm thực cũng tăng theo. Có thể phát sinh thêm hạt rắn trong chất lưu. "
      "Khi chất lưu bẩn hơn, nguy cơ tắc các lỗ nhỏ dùng để giảm xâm thực cũng tăng lên.",
      "Pressure and temperatures in today's process and oil recovery facilities continue to climb. "
      "As those pressures and resultant pressure drops increase, the propensity for cavitation to "
      "occur also increases. With that can come additional particulate in the fluid. As the fluid "
      "becomes dirtier, the potential for clogging the small holes used for cavitation abatement "
      "increases.")
    P("Có sẵn trim đặc biệt chịu được chênh áp trên 6000 psig mà vẫn cho qua hạt rắn kích thước tới "
      "1,27 cm (1/2 inch). Trim điều khiển chống xâm thực nhiều tầng dùng trong dịch vụ mà chất lưu "
      "có thể chứa hạt rắn gây tắc đường dẫn hoặc làm xói mòn trim chống xâm thực thông thường. DST "
      "thường được dùng trong ứng dụng chênh áp cao tới 4200 psid trong các ngành hóa chất, lọc dầu, "
      "sản xuất dầu khí và điện lực.",
      "Special trims are available that can handle pressure drops in excess of 6000 psig while "
      "still allowing particulate to pass that is up to 1.27 cm (½-inch) in size. Multi-stage, "
      "anti-cavitation control valve trim for use in services where the fluid may have entrained "
      "particulate that could plug the passages, or cause erosion damage to conventional "
      "anti-cavitation trims. DST is frequently used in high pressure drop applications up to 4200 "
      "psid in the chemical, refining, oil and gas production, and power industries.")
    FIG(6, F6.fig_f6_06())
    P("Van điều khiển quay nút lệch tâm điều khiển chất lưu xói mòn, đóng cặn và khó xử lý khác, vận "
      "hành điều tiết hoặc đóng/mở. Van có bích này có đường dòng suôi, bộ phận trim kim loại chắc "
      "chắn và vòng đế van tự căn giữa.",
      "Eccentric plug rotary control valve controls erosive, coking, and other hard-to-handle "
      "fluids, providing either throttling or on/off operation. The flanged valve features "
      "streamline flow passages, rugged metal trim components, and a self-centering seat ring.")
    FIG(7, F6.fig_f6_07())

    # ------------------------------------------------------------ 6.6
    H("6.6 Đặc tính tùy biến, giảm ồn và giảm xâm thực",
      "6.6 Customized Characteristics, Noise Abatement, and Cavitation Mitigation Trims")
    P("Dù đặc tính van dùng trong van tiêu chuẩn (Hình 6.8) đáp ứng yêu cầu của hầu hết ứng dụng, "
      "vẫn thường cần đặc tính tùy chỉnh cho một ứng dụng cụ thể. Trong những trường hợp đó, có thể "
      "chế tạo thiết kế trim đặc biệt đáp ứng yêu cầu. Với nút định hình, có thể sửa đổi thiết kế "
      "đầu nút sao cho khi nút di chuyển trong toàn bộ hành trình, diện tích dòng không bị cản thay "
      "đổi kích thước để tạo ra đặc tính dòng cụ thể. Tương tự, có thể thiết kế lại cage để đáp ứng "
      "đặc tính riêng. Điều này đặc biệt phổ biến ở trim giảm ồn và chống xâm thực, nơi cần mức bảo "
      "vệ cao ở lưu lượng thấp nhưng mức bảo vệ thấp hơn nhiều ở lưu lượng cao.",
      "Although control valve characteristics used in standard control valves (Figure 6.8) meet "
      "the requirements of most applications, often custom characteristics are needed for a given "
      "application. In these instances, special trim designs can be manufactured that meet these "
      "requirements. For contoured plugs, the design of the plug tip can be modified so that as "
      "the plug is moved through its travel range, the unobstructed flow area changes in size to "
      "allow for the generation of the specific flow characteristic. Likewise, cages can be "
      "redesigned to meet specific characteristics as well. This is especially common in noise "
      "abatement and anti-cavitation type trims where a high level of protection may be required "
      "at low flow rates but much lower protection levels are required for the higher flow rate "
      "conditions.")
    FIG(8, F6.fig_f6_08())
    P("Các nhà máy được vận hành tuần hoàn nhiều lần mỗi ngày với hạt rắn trong dòng đang gây xói "
      "mòn đế van. Hư hỏng có thể xảy ra khi có hạt rắn cuốn theo từ sự ăn mòn trong hệ thống nước "
      "cấp lò hơi. Các hạt này, được các tia phun ra từ lỗ cage đẩy đi, có thể gây hư hỏng nghiêm "
      "trọng khi đầu nút nằm trước các lỗ trong thời gian dài. Hư hỏng cũng xảy ra khi điều khiển "
      "dưới Cv tối thiểu khuyến nghị và dòng khe hở xói mòn đầu nút. Thiết kế đế được bảo vệ bên "
      "trong có thể kéo dài tuổi thọ của đế van và đầu nút.",
      "The plants that are being cycled multiple times daily with particles in the flow are causing "
      "seat erosion. The damage can occur when there is entrained particulate that comes from "
      "corrosion occurring in the boiler feedwater system. This particulate, driven by the jets "
      "exiting the cage holes, can cause serious damage when the position of the plug tip is "
      "located in front of the holes for extended period of times. The damage can occur when "
      "controlling below recommended minimum Cv and the clearance flow erodes the plug tip. The "
      "protected inside seat design can extend the service life of the seat and the plug tip.")

    # ------------------------------------------------------------ 6.7
    H("6.7 Van điều khiển cho dịch vụ hạt nhân ở Bắc Mỹ",
      "6.7 Control Valves for Nuclear Service in North America")
    P("Từ năm 1970, các nhà sản xuất và nhà cung cấp linh kiện cho nhà máy điện hạt nhân tại Hoa Kỳ "
      "phải tuân thủ yêu cầu của Phụ lục B, Title 10, Part 50 của Bộ luật Quy định Liên bang, có tựa "
      "đề Quality Assurance Criteria for Nuclear Power Plants and Fuel Reprocessing Plants. Ủy ban "
      "Điều tiết Hạt nhân Hoa Kỳ thực thi quy định này. Trách nhiệm cuối cùng trong việc chứng minh "
      "sự tuân thủ Phụ lục B thuộc về chủ sở hữu nhà máy, người lại phải dựa vào các nhà sản xuất "
      "linh kiện để cung cấp bằng chứng có ghi chép rằng linh kiện được chế tạo, kiểm tra và thử "
      "nghiệm bằng kỹ thuật đã được chứng minh, do nhân viên có trình độ thực hiện theo quy trình "
      "được ghi chép.",
      "Since 1970, U.S. manufacturers and suppliers of components for nuclear power plants have "
      "been subject to the requirements of Appendix B, Title 10, Part 50 of the Code of Federal "
      "Regulations entitled Quality Assurance Criteria for Nuclear Power Plants and Fuel "
      "Reprocessing Plants. The U.S. Nuclear Regulatory Commission enforces this regulation. "
      "Ultimate responsibility of proof of compliance to Appendix B rests with the owner of the "
      "plant, who must in turn rely on the manufacturers of various plant components to provide "
      "documented evidence that the components were manufactured, inspected, and tested by proven "
      "techniques performed by qualified personnel according to documented procedures.")
    P("Phù hợp với Bộ luật Quy định Liên bang, hầu hết linh kiện nhà máy điện hạt nhân được chỉ định "
      "theo Mục III của Bộ luật ASME về Nồi hơi và Bình áp lực, có tựa đề Rules for Construction of "
      "Nuclear Facility Components. Mọi khía cạnh của quá trình chế tạo phải được ghi trong sổ tay "
      "kiểm soát chất lượng và được ASME kiểm toán, chứng nhận trước khi chế tạo thực tế. Mọi vật "
      "liệu và thao tác chế tạo sau đó đều được kiểm tra bởi thanh tra viên được ủy quyền. Tất cả "
      "van chế tạo theo yêu cầu Mục III đều nhận tem tên ASME và ký hiệu dấu N biểu thị sự chấp nhận "
      "dùng trong ứng dụng nhà máy điện hạt nhân. ASME Mục III được sửa đổi bằng ấn bản mới ba năm "
      "một lần, có thể dùng sau ngày phát hành và trở thành bắt buộc sáu tháng sau ngày phát hành.",
      "In keeping with the requirements of the Code of Federal Regulations, most nuclear power "
      "plant components are specified in accordance with Section III of the ASME Boiler and "
      "Pressure Vessel Code entitled Rules for Construction of Nuclear Facility Components. All "
      "aspects of the manufacturing process must be documented in a quality control manual and "
      "audited and certified by ASME before actual manufacture of the components. All subsequent "
      "manufacturing materials and operations are to be checked by an authorized inspector. All "
      "valves manufactured in accordance with Section III requirements receive an ASME code "
      "nameplate and an N stamp symbolizing acceptability for service in nuclear power plant "
      "applications. ASME Section III is revised by means of new editions every three years, which "
      "may be used after date of issue, and which become mandatory six months after date of issue.")
    P("ASME Mục III định nghĩa ba lớp mã cho van — Class 1, 2 và 3. Van Class 1 là một phần của ranh "
      "giới áp suất hệ thống sơ cấp, nằm giữa bình áp suất lò phản ứng và các van cô lập chứa ngoài "
      "cùng. Van Class 2 là một phần của hệ thống làm mát lõi khẩn cấp và là bộ phận không thể "
      "tách rời của hệ thống bảo vệ sức khỏe cộng đồng và an toàn. Van Class 3 được lắp trong các "
      "hệ thống hạt nhân thực hiện chức năng làm mát thiết bị khẩn cấp và các hệ thống có thể chứa "
      "chất lỏng hoặc vật liệu phóng xạ.",
      "ASME Section III defines three code classes for valves — Class 1, 2, and 3. Class 1 valves "
      "are part of the primary system pressure boundary, located between the reactor pressure "
      "vessel and the outermost containment isolation valves. Class 2 valves are part of the "
      "emergency core cooling system and present an integral part of the protection of the public "
      "health and safety system. Class 3 valves are installed in nuclear systems that perform "
      "emergency equipment cooling functions and systems that may contain radioactive fluids or "
      "materials.")
    TBL(["Lớp / Class", "Phạm vi áp dụng / Scope"],
        [("Class 1",
          "Ranh giới áp suất hệ thống sơ cấp, giữa bình áp suất lò phản ứng và van cô lập chứa ngoài "
          "cùng / Primary system pressure boundary, between the reactor pressure vessel and the "
          "outermost containment isolation valves"),
         ("Class 2",
          "Hệ thống làm mát lõi khẩn cấp, một phần của hệ thống bảo vệ sức khỏe cộng đồng và an toàn "
          "/ Emergency core cooling system, integral to protection of public health and safety"),
         ("Class 3",
          "Hệ thống làm mát thiết bị khẩn cấp và hệ thống có thể chứa chất lỏng hoặc vật liệu phóng "
          "xạ / Emergency equipment cooling systems and systems that may contain radioactive fluids "
          "or materials")],
        "Ba lớp mã van theo ASME Mục III / Three valve code classes under ASME Section III.")
    P("Mục III áp dụng cho vật liệu dùng ở bộ phận chịu áp, tiêu chí thiết kế, quy trình chế tạo, "
      "quy trình thử không phá hủy cho bộ phận chịu áp, thử áp lực thủy tĩnh và quy trình đánh dấu "
      "đóng tem. Bộ phận chịu áp tiếp xúc hoặc chịu tải bởi áp suất quá trình trong đường ống. Ở van "
      "điều khiển, đó thường là thân van, nắp, bulong và đai ốc nắp-thân, và nút hoặc đĩa.",
      "Section III applies to materials used for pressure retaining parts, design criteria, "
      "fabrication procedures, non-destructive test procedures for pressure retaining parts, "
      "hydrostatic testing, and marking and stamping procedures. Pressure retaining parts are "
      "exposed to or loaded by the process pressure within a pipeline. In control valves, these "
      "are typically the valve body, bonnet, body-bonnet studs and nuts, and the plug or disc.")
    P("Mục III không áp dụng cho bộ phận không liên quan đến chức năng chịu áp; cho cơ cấu chấp hành "
      "và phụ kiện trừ khi chúng là bộ phận chịu áp; cho sự suy giảm của cấu kiện van do bức xạ, ăn "
      "mòn, xói mòn, thẩm định địa chấn hoặc môi trường; cũng không áp dụng cho yêu cầu làm sạch, sơn "
      "hoặc đóng gói. Các yêu cầu này thường do tiêu chuẩn của khách hàng bao phủ. Dù không thuộc "
      "phạm vi Mục III, các bộ phận này vẫn có thể được xác định là linh kiện liên quan an toàn và "
      "chịu Phụ lục B của 10CFR50 cùng yêu cầu báo cáo của 10CFR Part 21. Linh kiện liên quan an toàn "
      "là thiết bị ngăn ngừa hoặc giảm thiểu phơi nhiễm ra ngoài công trình và/hoặc cho phép nhà máy "
      "đạt và duy trì trạng thái dừng an toàn. Ở van điều khiển, các bộ phận liên quan an toàn có thể "
      "khác nhau tùy chức năng và ứng dụng an toàn cụ thể của cụm, nhưng thường gồm giá đỡ cơ cấu "
      "chấp hành, thân van, cụm liên kết thân và lò xo cơ cấu chấp hành, cũng như các bộ phận ranh "
      "giới áp suất. Đệm kín và gioăng nói chung không được coi là cấu kiện liên quan an toàn.",
      "Section III does not apply to parts not associated with the pressure-retaining function; "
      "to actuators and accessories unless they are pressure retaining parts; to deterioration of "
      "valve components due to radiation, corrosion, erosion, seismic or environmental "
      "qualifications; or to cleaning, painting, or packaging requirements. Customer "
      "specifications normally cover these areas. While these parts are not applicable to ASME "
      "Section III, they may be defined as safety related components and subject to 10CFR50 "
      "Appendix B and reporting requirements of 10CFR Part 21. Safety related components are "
      "items that prevent or mitigate offsite exposure; and/or enable a plant to go to and remain "
      "in a safe shutdown condition. In control valves, safety related parts can differ depending "
      "on the specific safety function and application of an assembly, but typically include the "
      "actuator yokes, valve stems, stem connector assemblies, and actuator springs as well as the "
      "pressure boundary valve components. Packing and gaskets would not generally be considered "
      "safety related compontents.")
    P("Tại Hoa Kỳ, hai thiết kế lò phản ứng chính là Lò nước áp lực (PWR) và Lò nước sôi (BWR). Trong "
      "PWR, nước làm mát sơ cấp được bơm dưới áp suất cao tới lõi lò, nơi nước được đốt nóng và chảy "
      "vào bộ tạo hơi, ở đó hệ thống nước thứ cấp tạo hơi để dẫn động tua-bin hơi. Trong BWR, nước "
      "làm mát sơ cấp được lõi lò đốt nóng đến điểm sôi và chuyển thành hơi dùng trực tiếp dẫn động "
      "tua-bin chính. Một ứng dụng van điều khiển quan trọng trong thiết kế PWR là Van phun bình áp "
      "lực. Van này cấp nước làm mát sơ cấp vào bình áp lực, nơi điều khiển áp suất nước làm mát "
      "trong lò phản ứng. Các ứng dụng van điều khiển quan trọng khác trong cả hai thiết kế gồm Van "
      "điều khiển nước cấp chính và khởi động, Van điều khiển bypass hơi chính và Van xả hơi chính.",
      "In the U.S., the two main reactor designs are Pressurized Water Reactors (PWR) and Boiling "
      "Water Reactors (BWR). In a PWR, primary coolant water is pumped under high pressure to the "
      "reactor core where it is heated and flows into a steam generator, where a secondary water "
      "system generates steam that drives the steam turbines. In a BWR, primary cooling water is "
      "heated to a boiling point by the reactor core and converted to steam that is directly used "
      "to drive the main turbines. A critical control valve application within a PWR design is a "
      "Pressurizer Spray Valve. This valve provides primary coolant to the pressurizer that "
      "controls the coolant pressure within the reactor. Other critical control valve applications "
      "within both designs include Main and Startup Feedwater Control Valves, Main Steam Bypass "
      "Control Valves, and Main Steam Dump Valves.")
    FIG(9, F6.fig_f6_09())
    P("Tại Canada, thiết kế lò phản ứng chính được gọi là CANDU (Canada Deuterium Uranium). CANDU "
      "là Lò nước nặng áp lực (PHWR) dùng urani làm nhiên liệu. Nhiều ứng dụng van điều khiển quan "
      "trọng trong thiết kế này ban đầu yêu cầu dùng nắp có ống đệm kín (bellow sealed bonnet) để "
      "giảm phát thải có hại qua đệm thân. Hệ thống đệm như Enviro-Seal đang được áp dụng khi các "
      "nhà máy CANDU được cải tạo, nhằm giảm chiều cao tổng thể của cụm van và cải thiện hiệu năng "
      "địa chấn. Tuy nhiên, các yêu cầu này thường do tiêu chuẩn khách hàng bao phủ. Mục III vẫn áp "
      "dụng cho vật liệu dùng ở bộ phận chịu áp, tiêu chí thiết kế, quy trình chế tạo, quy trình "
      "thử không phá hủy cho bộ phận chịu áp, thử áp lực thủy tĩnh và quy trình đánh dấu đóng tem. "
      "ASME Mục III được sửa đổi bằng các phụ lục nửa năm, có thể dùng sau ngày phát hành và trở "
      "thành bắt buộc sáu tháng sau ngày phát hành.",
      "In Canada, the main reactor design is referred to as CANDU (Canada Deuterium Uranium). "
      "CANDU is a Pressurized Heavy Water Reactor (PHWR) that uses uranium as its fuel source. Many "
      "critical control valve applications within this plant design originally required the use of "
      "bellow sealed bonnets to mitigate harmful emissions through the stem packing. Packing "
      "systems such as Enviro-Seal are being implemented as utilities refurbish the CANDU plants to "
      "reduce the overall height of the valve assembly and improve seismic performance. However, "
      "customer specifications normally cover these areas. Section III does apply to materials used "
      "for pressure retaining parts, to design criteria, to fabrication procedures, to "
      "non-destructive test procedures for pressure retaining parts, to hydrostatic testing, and "
      "to marking and stamping procedures. ASME Section III is revised by means of semi-annual "
      "addenda, which may be used after date of issue, and which become mandatory six months after "
      "date of issue.")

    # ------------------------------------------------------------ 6.8
    H("6.8 Van chịu nứt do ứng suất sunfat",
      "6.8 Valves Subjected to Sulfide Stress Cracking")
    P("NACE International là một hiệp hội kỹ thuật quan tâm đến ăn mòn và các vấn đề liên quan ăn "
      "mòn. NACE chịu trách nhiệm về nhiều tiêu chuẩn, nhưng tiêu chuẩn có ảnh hưởng và nổi tiếng "
      "nhất là MR0175, trước đây có tựa đề Sulfide Stress Cracking-Resistant Metallic Materials for "
      "Oilfield Equipment. MR0175 do NACE ban hành năm 1975 để đưa ra hướng dẫn lựa chọn vật liệu "
      "chống hỏng trong môi trường sản xuất dầu khí chứa hydro sunfat. MR0175 được trích dẫn rộng "
      "rãi đến mức trong toàn ngành quá trình, thuật ngữ «NACE» gần như đồng nghĩa với «MR0175». "
      "Tuy nhiên, tình hình đã thay đổi năm 2003.",
      "NACE International is a technical society concerned with corrosion and corrosion-related "
      "issues. NACE is responsible for a large number of standards, but by far the most influential "
      "and well known is MR0175, formerly entitled Sulfide Stress Cracking- Resistant Metallic "
      "Materials for Oilfield Equipment. MR0175 was issued by NACE in1975 to provide guidelines "
      "for the selection of materials that are resistant to failure in hydrogen sulfide-containing "
      "oil and gas production environments. MR0175 has been so widely referenced that, throughout "
      "the process industry, the term \"NACE\" has become nearly synonymous with \"MR0175.\" "
      "However, the situation changed in 2003.")
    P("MR0175 được sửa đổi đáng kể trong bản sửa năm 2003 để bao hàm cả nứt do ứng suất ăn mòn "
      "clorua, ngoài nứt do ứng suất sunfat. Sau đó, cuối năm 2003, tài liệu được sửa và phát hành "
      "thành tài liệu chung NACE/ISO có tên NACE MR0175/ISO 15156, Petroleum and Natural Gas "
      "Industries—Materials for Use in H2S-Containing Environments in Oil and Gas Production.",
      "MR0175 was modified significantly in a 2003 revision to cover chloride stress corrosion "
      "cracking, in addition to sulfide stress cracking. Then, in late 2003, the document was "
      "revised and released as a joint NACE/ISO document called NACE MR0175/ISO 15156, Petroleum "
      "and Natural Gas Industries—Materials for Use in H2S-Containing Environments in Oil and Gas "
      "Production.")
    P("Tháng 4 năm 2003, NACE cũng phát hành tiêu chuẩn mới MR0103, có tựa đề Materials Resistant to "
      "Sulfide Stress Cracking in Corrosive Petroleum Refining Environments. Tiêu chuẩn này về cơ "
      "bản là «NACE MR0175» của ngành lọc dầu. MR0103 chỉ đề cập đến nứt do ứng suất sunfat và vì "
      "vậy giống nhiều mặt với các bản MR0175 trước năm 2003. Việc dùng MR0103 trong ngành lọc dầu "
      "đang tăng nhanh.",
      "In April 2003, NACE also released a new standard, MR0103, which is entitled, Materials "
      "Resistant to Sulfide Stress Cracking in Corrosive Petroleum Refining Environments. This "
      "standard is essentially the refining industry's \"NACE MR0175.\" MR0103 only addresses "
      "sulfide stress cracking, and as such is similar in many respects to the pre-2003 revisions "
      "of MR0175. Use of the MR0103 standard in the refining industry is accelerating.")
    P("Năm 2013, tài liệu được sửa đổi, định dạng lại và phát hành thành tài liệu ISO có tên ISO "
      "17945, có tựa đề Petroleum, Petrochemical, and Natural Gas Industries – Metallic Materials "
      "Resistant to Sulfide Stress Cracking in Corrosive Petroleum Refining Environments. Năm 2015, "
      "tài liệu này được NACE chấp nhận là MRO103/ISO 17945.",
      "In 2013, the document was revised, reformatted, and released as an ISO document called ISO "
      "17945, titled Petroleum, Petrochemical, and Natural Gas Industries – Metallic Materials "
      "Resistant to Sulfide Stress Cracking in Corrosive Petroleum Refining Environments. In 2015, "
      "this was adopted by NACE as MRO103/ISO 17945.")
    P("Cần lưu ý rằng việc tuân thủ một số bản MR0175 hoặc MR0175/ISO 15156 được pháp luật bắt buộc "
      "ở một số tiểu bang và vùng tại Hoa Kỳ. Hiện tại, MR0103ISO 17945 không được cơ quan quản lý "
      "nào bắt buộc.",
      "Note that compliance with certain revisions of NACE MR0175 or NACE MR0175/ISO 15156 is "
      "mandated by statute in some states and regions in the U.S.A. At this time, NACE MR0103ISO "
      "17945 is not mandated by any governing bodies.")

    H("6.8.1 Các bản MR0175 trước năm 2003", "6.8.1 Pre-2003 Revisions of NACE MR0175", h3)
    P("Các phát biểu dưới đây, dù dựa trên thông tin và yêu cầu trong các bản MR0175 trước năm 2003, "
      "không thể trình bày chi tiết như trong tiêu chuẩn thực tế và không bảo đảm tính phù hợp của "
      "bất kỳ vật liệu cụ thể nào trong môi trường chua chứa hydro sunfat. Độc giả được khuyến khích "
      "tham khảo tiêu chuẩn thực tế trước khi chọn van điều khiển cho dịch vụ chua.",
      "The following statements, although based on information and requirements in the pre-2003 "
      "revisions of MR0175, cannot be presented in the detail furnished in the actual standard and "
      "do not guarantee suitability for any given material in hydrogen sulfide-containing sour "
      "environments. The reader is urged to refer to the actual standard before selecting control "
      "valves for sour service.")
    B(["Hầu hết kim loại đen có thể trở nên nhạy với nứt do ứng suất sunfat (SSC) do làm cứng bằng "
       "xử lý nhiệt và/hoặc gia công nguội. Ngược lại, nhiều kim loại đen có thể được xử lý nhiệt để "
       "cải thiện khả năng chống SSC.",
       "Thép carbon và thép hợp kim thấp phải được xử lý nhiệt đúng cách để chống SSC. Giới hạn độ "
       "cứng tối đa HRC 22 áp dụng cho thép carbon và thép hợp kim thấp.",
       "Thép không gỉ austenit chống SSC tốt nhất ở trạng thái ủ; một số cấp và trạng thái cụ thể "
       "của thép không gỉ được chấp nhận tới 35 HRC.",
       "Hợp kim gốc đồng vốn chống SSC nhưng nói chung không dùng ở bộ phận quan trọng của van "
       "khi chưa có sự chấp thuận của người mua, do lo ngại ăn mòn nói chung.",
       "Hợp kim niken nói chung cho khả năng chống SSC tốt nhất. Một số hợp kim niken có thể làm "
       "cứng bằng kết tủa được chấp nhận cho ứng dụng cần độ bền và/hoặc độ cứng tới 40 HRC.",
       "Mạ crom, niken và các loại mạ khác không bảo vệ khỏi SSC. Việc dùng chúng được phép trong "
       "ứng dụng chua để chống mòn, nhưng không được dùng nhằm bảo vệ vật liệu nền không chống được "
       "SSC.",
       "Sửa chữa bằng hàn và mối hàn chế tạo trên thép carbon và thép hợp kim thấp phải được xử lý "
       "đúng cách để bảo đảm đáp ứng yêu cầu độ cứng tối đa 22 HRC ở kim loại nền, vùng ảnh hưởng "
       "nhiệt (HAZ) và kim loại lấp đầy mối hàn. Thép hợp kim cần xử lý nhiệt sau hàn và xử lý nhiệt "
       "sau hàn nói chung cũng dùng cho thép carbon.",
       "Đóng dấu nhận dạng thông thường được phép ở vùng ứng suất thấp, chẳng hạn đường kính ngoài "
       "của bích đường ống. Phải dùng dấu nhận dạng ứng suất thấp ở các vùng khác.",
       "Tiêu chuẩn cấm dùng bulong ASTM A193 Grade B7 cho ứng dụng được coi là «phơi nhiễm». Dùng "
       "vật liệu bulong chống SSC (như ASTM A193 Grade B7M) đôi khi bắt phải giảm cấp van thiết kế "
       "ban đầu dùng bulong B7. Ví dụ, ở van cầu Class 600, thường dùng bulong 17-4PH H1150 DBL để "
       "tránh giảm cấp."],
      ["Most ferrous metals can become susceptible to sulfide stress cracking (SSC) due to "
       "hardening by heat treatment and/or cold work. Conversely, many ferrous metals can be heat "
       "treated to improve resistance to SSC.",
       "Carbon and low-alloy steels must be properly heat treated to provide resistance to SSC. A "
       "maximum hardness limit of HRC 22 applies to carbon and low-alloy steels.",
       "Austenitic stainless steels are most resistant to SSC in the annealed condition; some "
       "specific grades and conditions of stainless steels are acceptable up to 35 HRC.",
       "Copper-based alloys are inherently resistant to SSC, but are generally not used in critical "
       "parts of a valve without the approval of the purchaser due to concerns about general "
       "corrosion.",
       "Nickel alloys generally provide the best resistance to SSC. Some precipitation-hardenable "
       "nickel alloys are acceptable for use in applications requiring high strength and/or "
       "hardness up to 40 HRC.",
       "Chromium, nickel, and other types of plating offer no protection against SSC. Their use is "
       "allowed in sour applications for wear resistance, but they cannot be used in an attempt to "
       "protect a non-resistant base material from SSC.",
       "Weld repairs and fabrication welds on carbon and low-alloy steels must be properly "
       "processed to ensure that they meet the 22 HRC maximum hardness requirement in the base "
       "metal, heat-affected zone (HAZ), and weld deposit. Alloy steels require post-weld heat "
       "treatment, and post−weld heat treatment is generally used for carbon steels as well.",
       "Conventional identification stamping is permissible in low stress areas, such as on the "
       "outside diameter of line flanges. Low-stress identification stamping must be used in other "
       "areas.",
       "The standard precludes using ASTM A193 Grade B7 bolting for applications that are "
       "considered \"exposed.\" Use of SSC-resistant bolting materials (such as ASTM A193 Grade "
       "B7M) sometimes necessitates derating of valves designed originally to use B7 bolting. For "
       "example, in a Class 600 globe valve, 17-4PH H1150 DBL bolting was often used to avoid "
       "derating."])
    TBL(["Vật liệu / Material", "Giới hạn hoặc yêu cầu / Limit or requirement"],
        [("Thép carbon và hợp kim thấp / Carbon and low-alloy steels",
          "Xử lý nhiệt đúng cách; độ cứng tối đa HRC 22 / Properly heat treated; maximum HRC 22"),
         ("Thép không gỉ austenit / Austenitic stainless steels",
          "Bền nhất ở trạng thái ủ; một số cấp/trạng thái tới 35 HRC / Most resistant when annealed; "
          "some grades/conditions up to 35 HRC"),
         ("Hợp kim niken kết tủa cứng / Precipitation-hardenable nickel alloys",
          "Chống SSC tốt nhất; một số loại tới 40 HRC / Best SSC resistance; some up to 40 HRC"),
         ("Hợp kim gốc đồng / Copper-based alloys",
          "Vốn chống SSC nhưng không dùng cho bộ phận quan trọng khi chưa có phê duyệt / Inherently "
          "resistant but not for critical parts without purchaser approval"),
         ("Lớp mạ crom, niken / Chromium, nickel plating",
          "Không chống SSC; chỉ dùng để chống mòn / No SSC protection; wear resistance only"),
         ("Mối hàn và vùng HAZ / Welds and HAZ",
          "Tối đa 22 HRC ở nền, HAZ và mối hàn; PWHT / Max 22 HRC in base metal, HAZ and weld "
          "deposit; PWHT")],
        "Giới hạn độ cứng và yêu cầu vật liệu theo các bản MR0175 trước 2003 / Hardness limits and "
        "material requirements under pre-2003 MR0175 revisions.")

    H("6.8.2 NACE MR0175/ISO 15156", "6.8.2 NACE MR0175/ISO 15156", h3)
    P("NACE MR0175/ISO 15156 đưa những thay đổi đáng kể vào tiêu chuẩn. Tuy nhiên, nhiều người dùng "
      "cuối vẫn tiếp tục chỉ định NACE MR0175-2002, cho rằng nó đáp ứng đủ nhu cầu mang lại tuổi "
      "thọ sử dụng tốt. Những thay đổi quan trọng nhất gồm:",
      "NACE MR0175/ISO 15156 introduced significant changes to the standard. However, many end "
      "users continue to specify NACE MR0175-2002, feeling that it adequately meets their needs in "
      "providing good service life. The most significant changes in NACE MR0175/ISO 15156 include:")
    B(["Bulong 17-4PH H1150 DBL từng dùng cho bulong phơi nhiễm đầy tải trong van cầu Class 600 "
       "không còn được phép.",
       "Bản sửa đề cập cả nứt do ứng suất sunfat lẫn nứt do ứng suất ăn mòn clorua. Các bản trước "
       "chỉ liệt kê vật liệu là được hoặc không được chấp nhận. Vì phạm vi mở rộng sang nứt do "
       "clorua, tiêu chuẩn mới liệt kê mọi hợp kim chống ăn mòn là được chấp nhận trong giới hạn, "
       "gọi là «giới hạn môi trường hoặc hạn chế môi trường». Các giới hạn này thường biểu thị bằng "
       "áp suất riêng phần H2S, nhiệt độ tối đa, ppm clorua và sự có mặt của lưu huỳnh tự do.",
       "Việc dùng 316 vẫn được phép nhưng chỉ trong điều kiện môi trường rất hạn chế. Nếu tuân thủ "
       "nghiêm ngặt, vật liệu này sẽ ít được dùng.",
       "Tiêu chuẩn chỉ áp dụng cho thiết bị sản xuất, khoan, thu gom và đường dẫn dầu khí cùng cơ "
       "sở xử lý hiện trường dùng trong dịch vụ hydrocarbon chứa H2S. Nó không áp dụng cho nhà máy "
       "lọc dầu.",
       "Trách nhiệm rõ ràng được đặt lên người mua hoặc người dùng trong việc chỉ định đúng vật "
       "liệu. Nhà sản xuất chỉ chịu trách nhiệm đáp ứng yêu cầu luyện kim của MR0175/ISO 15156, "
       "không chịu trách nhiệm chỉ định đúng vật liệu."],
      ["The 17-4PH H1150 DBL bolting that was previously used for full-rated exposed bolting in a "
       "Class 600 globe valve is no longer allowed.",
       "The revision addresses both sulfide stress cracking and chloride stress corrosion "
       "cracking. Prior versions simply listed most materials as acceptable or unacceptable. "
       "Because its scope was expanded to cover chloride stress corrosion cracking, the new "
       "standard lists all corrosion-resistant alloys as acceptable within limits, referred to as "
       "\"environmental limits or environmental restrictions.\" These are typically expressed in "
       "terms of H2S partial pressure, maximum temperature, ppm chlorides, and the presence of free "
       "sulfur.",
       "316 usage is still allowed but under very limited environmental conditions. The impact, if "
       "strictly followed, is that this material will find very little use.",
       "The standard applies only to petroleum production, drilling, gathering and flow line "
       "equipment, and field processing facilities to be used in H2S bearing hydrocarbon service. "
       "It does not apply to refineries.",
       "There is clear responsibility placed on the buyer or user to specify the correct "
       "materials. The manufacturer is only responsible for meeting the metallurgical requirements "
       "of MR0175/ISO 15156, but not to specify the correct materials."])

    H("6.8.3 NACE MR0103", "6.8.3 NACE MR0103", h3)
    P("Như đã nêu, NACE MR0103 giống nhiều mặt với các bản MR0175 trước năm 2003. Sau đây là một số "
      "khác biệt chính:",
      "As mentioned, NACE MR0103 is similar in many respects to the pre-2003 revisions of NACE "
      "MR0175. The following are some major differences:")
    B(["MR0103 dùng định nghĩa về môi trường chua dựa trên ngành lọc dầu. Người dùng chịu trách "
       "nhiệm áp đặt yêu cầu của MR0103 khi có liên quan.",
       "Các bản MR0175 năm 2002 và cũ hơn có chứa hạn chế môi trường với một số ít vật liệu được "
       "giữ lại ở các bản sau. MR0103 chỉ đề cập nứt do ứng suất sunfat, không áp đặt giới hạn môi "
       "trường cho vật liệu nào. Vật liệu hoặc được chấp nhận, hoặc không.",
       "Vật liệu nền thép carbon được phân loại là thép P-No. 1 nhóm 1 hoặc 2 theo Bộ luật ASME về "
       "Nồi hơi và Bình áp lực được chấp nhận theo MR0103 mà không cần yêu cầu độ cứng kim loại "
       "nền. P-No. 1 nhóm 1 và 2 gồm thép đúc WCC và LCC, thép rèn A105, thép tấm A516 Grade 70 "
       "và các vật liệu bình áp lực thép carbon thông thường khác.",
       "MR0103 áp đặt kiểm soát hàn trên thép carbon nghiêm ngặt hơn MR0175-2002. MR0103 yêu cầu "
       "thép carbon P-No. 1 được hàn theo tài liệu NACE khác là RP0472, Methods and Controls to "
       "Prevent In-Service Environmental Cracking of Carbon Steel Weldments in Corrosive Petroleum "
       "Refining Environments. RP0472 áp đặt kiểm soát bảo đảm cả kim loại lấp đầy mối hàn lẫn vùng "
       "ảnh hưởng nhiệt (HAZ) đủ mềm để chống SSC. RP0472 yêu cầu thử độ cứng thực tế kim loại lấp "
       "đầy mối hàn trong sản xuất, dù được miễn thử khi dùng một số tổ hợp quy trình hàn/vật liệu "
       "phụ cụ thể. Độ cứng HAZ có thể kiểm soát bằng xử lý nhiệt sau hàn (PWHT) hoặc bằng hạn chế "
       "thành phần hóa học kim loại nền, chẳng hạn áp đặt giá trị tương đương carbon (CE) tối đa.",
       "Giống các bản MR0175 từ 2003 trở đi, MR0103 không cho phép dùng vật liệu S17400 H1150 DBL "
       "làm bulong. Điều đó có nghĩa bulong 17-4PH H1150 DBL từng dùng cho bulong phơi nhiễm đầy tải "
       "trong van Class 600 không còn được phép."],
      ["MR0103 utilizes different, refinery-based definitions for what constitutes a sour "
       "environment. The user is responsible for imposing the requirements of MR0103 when they are "
       "applicable.",
       "The 2002 and older revisions of MR0175 included environmental restrictions on a few "
       "materials that were continued in the latter editions. MR0103 only deals with sulfide "
       "stress cracking. It does not impose environmental limits on any materials. Materials are "
       "either acceptable or not.",
       "Carbon steel base materials that are classified as P-No. 1, group 1 or 2 steels in the ASME "
       "Boiler and Pressure Vessel Code are acceptable per MR0103 without base metal hardness "
       "requirements. P-No. 1 groups 1 and 2 include WCC and LCC castings, A105 forgings, A516 "
       "Grade 70 plate, and the other common carbon steel pressure vessel materials.",
       "MR0103 imposes welding controls on carbon steels that are more rigorous than those imposed "
       "by MR0175-2002. MR0103 requires that P-No. 1 carbon steels be welded per another NACE "
       "document called RP0472 \"Methods and Controls to Prevent In-Service Environmental Cracking "
       "of Carbon Steel Weldments in Corrosive Petroleum Refining Environments.\" RP0472 imposes "
       "controls that ensure both the weld deposit and heat affected zone (HAZ) in a weldment will "
       "be soft enough to resist sulfide stress cracking. RP0472 invokes actual hardness testing of "
       "weld deposits in production, although hardness testing is waived if certain welding "
       "process/filler material combinations are employed. HAZ hardness may be controlled by either "
       "post-weld heat treatment (PWHT) or by base material chemistry restrictions such as imposing "
       "a maximum carbon equivalent (CE).",
       "Like the 2003 and later revisions of MR0175, MR0103 does not allow the use of S17400 double "
       "H1150 material for bolting. This means that the 17-4PH H1150 DBL bolting that was "
       "previously used for full-rated exposed bolting in a Class 600 valve is no longer allowed."])
    P("Thế nào là NACE phổ dụng? NACE phổ dụng là một bản đúc WCC tuân thủ cả bốn tiêu chuẩn: "
      "MR0175-2002, MR0175-2003, MR0175/ISO 15156 và MR0103.",
      "What is Universal NACE? Universal NACE is a WCC NACE casting that complies with all four "
      "standards (MR0175-2002, MR0175-2003, MR0175/ISO 15156, and MR0103).")

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 6 chiếm tr. 150–161 của bản in (12 trang) trong Emerson, Control Valve Handbook, ấn bản "
      "6 (2020). Nội dung gồm tám mục 6.1–6.8: van công suất lớn, van Cv thấp, van nhiệt độ cao, van "
      "đông lạnh, van chịu xâm thực và hạt rắn, đặc tính tùy biến và giảm ồn, van cho dịch vụ hạt "
      "nhân ở Bắc Mỹ, và van chịu nứt do ứng suất sunfat. Chín hình được vẽ lại dạng vector trong "
      "cvh6fig6.py và đặt theo thứ tự số tại vị trí văn bản hợp lý.",
      "Chapter 6 occupies printed pp. 150-161 (12 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains eight sections, 6.1-6.8: high-capacity valves, low-Cv valves, "
      "high-temperature valves, cryogenic valves, valves for cavitation and particulate, customized "
      "characteristics and noise abatement, nuclear service valves in North America, and valves "
      "subjected to sulfide stress cracking. The nine numbered figures are redrawn as vectors in "
      "cvh6fig6.py and placed in numbered order at their logical prose points.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 Emerson Flow "
      "Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 Emerson Flow "
      "Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
