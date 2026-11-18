# -*- coding: utf-8 -*-
"""Book 6, Unit 17 — Sizing Pressure Relief Devices (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 269–292 (PDF pp. 283–306): gas, vapor, steam and liquid sizing;
back-pressure, overpressure and viscosity corrections; inlet and
discharge piping; rupture-disc sizing for nonviolent and violent duty
(Figures 7-1…7-9).
"""

from vsh_common import eq, fig, h2, h3, ol, p, table, ul
import vshfig14 as F14

PAGES_SRC = 24         # source book pp. 269-292
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Sizing Pressure Relief Devices"
TITLE_VI = "Định cỡ thiết bị giải áp"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 17.</b> sizing — định cỡ · choked / sonic "
                "flow — dòng tới hạn / dòng âm · subsonic flow — dòng dưới âm · "
                "isentropic coefficient k — hệ số đẳng entropy k · "
                "compressibility factor Z — hệ số nén Z · nozzle — miệng phóng · "
                "set pressure — áp cài đặt · overpressure — quá áp · back "
                "pressure — áp ngược · built-up back pressure — áp ngược tích "
                "lũy · superimposed back pressure — áp ngược chồng lên · "
                "coefficient of discharge K — hệ số xả K · Reynolds number — "
                "số Reynolds · resistance coefficient ζ — hệ số trở lực ζ · "
                "minimum net flow area — diện tích lưu thông ròng nhỏ nhất · "
                "vent panel — tấm thông nổ · KST / KG — hạng nổ bụi / khí.")
    return ("<b>Key terms.</b> sizing · choked / sonic flow · subsonic flow · "
            "isentropic coefficient k · compressibility factor Z · nozzle · "
            "set pressure · overpressure · back pressure · built-up back "
            "pressure · superimposed back pressure · coefficient of discharge "
            "K · Reynolds number · resistance coefficient ζ · minimum net "
            "flow area · vent panel · KST / KG explosion classes.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(items):
        b.append(ul([(i[0] if vi else i[1]) for i in items]))

    def O(items):
        b.append(ol([(i[0] if vi else i[1]) for i in items]))

    def E(body, num):
        b.append(eq(body, num))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # =========================================================== introduction
    H("Vì sao phải định cỡ đúng", "Why correct sizing matters")
    P("Định cỡ tối ưu thiết bị giải áp là điều kiện cần để bảo vệ an toàn "
      "hệ thống đường ống khỏi quá áp. Thiết bị quá nhỏ không xả được lưu "
      "lượng cần thiết; thiết bị quá lớn gây tốn vật tư và nhân công không "
      "đáng có. Mỗi dòng chảy có công thức hoặc quy trình riêng để xác định "
      "diện tích miệng phóng hoặc lưu lượng yêu cầu.",
      "Optimum sizing of pressure relief devices is essential to protect a "
      "piping system from overpressurization safely. An undersized device "
      "cannot relieve effectively; an oversized one adds unnecessary material "
      "and labor cost. Each flow regime has its own formula or procedure for "
      "finding the required nozzle area or flow rate.")
    U([("Khí hoặc hơi: dòng dưới âm (không tới hạn) và dòng âm (tới hạn).",
        "Gas or vapor: subsonic / non-choked and sonic / choked flow."),
       ("Chất lỏng.", "Liquid flow."),
       ("Dòng hai pha: khí chứa giọt lỏng, lỏng chứa bọt khí, và lỏng "
        "bay hơi qua van.",
        "Mixed-phase flow: gas with liquid droplets, liquid with gas bubbles, "
        "and liquid flashing to vapor through the valve.")])
    P("Ở thời điểm xuất bản, các cơ quan luật định và tổ chức tiêu chuẩn chưa "
      "có khuyến nghị chắc chắn cho phương trình định cỡ dòng hai pha. Các "
      "phương trình trong chương này được trình bày ở hệ đơn vị SI và hệ "
      "thường dụng Anh/Mỹ; ký hiệu xem Bảng 7-1 và Hình 7-1.",
      "At the time of publication, statutory bodies and standards "
      "organizations had not issued firm recommendations for mixed-phase "
      "sizing equations. The equations are presented in SI and customary "
      "imperial units; nomenclature is in Table 7-1 and Figure 7-1.")
    FIG(1, F14.fig_vsh_7_1())
    P("Các chỉ số tại vị trí đánh dấu được dùng thống nhất trong phương "
      "trình lưu lượng: bình nguồn (1), cổng bình (E), vào van (N), đầu ra "
      "van (2), đầu ống xả (3) và nhiệt độ dòng (T). Đây là nền tảng để "
      "phân biệt áp tuyệt đối tại miệng phóng, áp trong buồng giữa miệng "
      "phóng và đầu ra, cùng áp tại đầu ống xả.",
      "The subscripts at the marked points are used consistently in the flow "
      "equations: source vessel (1), vessel nozzle (E), valve inlet (N), "
      "valve outlet (2), discharge pipe outlet (3) and stream temperature "
      "(T). This distinguishes absolute pressure at the nozzle face, in the "
      "chamber between nozzle and outlet, and at the discharge pipe end.")

    # =========================================================== gas and vapor
    H("Khí và hơi", "Gas and vapor")
    P("Phương trình định cỡ cho khí hoặc hơi dựa trên định luật khí lý "
      "tưởng, giả thiết dòng qua miệng phóng là đẳng entropy. Độ lệch so với "
      "khí lý tưởng được hiệu chỉnh bằng hệ số nén Z, lấy tại điều kiện đầu "
      "vào. Nếu không xác định được Z, thường dùng Z = 1,0; cách này vẫn "
      "thiên về an toàn khi áp và nhiệt độ không quá cao.",
      "Gas and vapor sizing equations rest on the ideal-gas laws with "
      "isentropic flow through the nozzle. Departure from ideal behavior is "
      "corrected by the compressibility factor Z, evaluated at inlet "
      "conditions. If Z cannot be determined, Z = 1.0 is commonly used and is "
      "conservative where pressure and temperature are not too high.")
    P("Tỉ lệ giữa áp tuyệt đối phía dưới và phía trên miệng phóng quyết định "
      "chế độ dòng. Khi tỉ lệ cao hơn khoảng 0,5, dòng là dưới âm; khi tỉ lệ "
      "bằng hoặc thấp hơn khoảng 0,5, dòng đạt tới hạn. Giá trị chính xác "
      "phụ thuộc hệ số k đẳng entropy:",
      "The ratio of absolute downstream to upstream pressure across the "
      "nozzle sets the regime. Above about 0.5 flow is subsonic; at about 0.5 "
      "and below it becomes sonic. The exact transition depends on the "
      "isentropic coefficient k:")
    E("P<sub>CF</sub> / P<sub>1</sub> = [2 / (k + 1)]<sup>k/(k−1)</sup>",
      "7-1")
    P("Pcf là áp miệng phóng tới hạn; Bảng 7-2 cho tỉ lệ áp tới hạn và hệ số "
      "C cho k từ 1,01 đến 2,00. Với dòng tới hạn, diện tích được tính từ "
      "lưu lượng khối hoặc lưu lượng thể tích theo các phương trình 7-2 đến "
      "7-6; ví dụ dạng lưu lượng khối hệ SI:",
      "Pcf is the critical nozzle-flow pressure. Table 7-2 lists critical "
      "pressure ratios and coefficient C for k from 1.01 to 2.00. For sonic "
      "flow, area follows from mass or volumetric flow in equations 7-2 to "
      "7-6; in SI mass-flow form:")
    E("A = 131.6 W C K P<sub>1</sub> K<sub>b</sub> √(T Z / M)",
      "7-4")
    P("Với dòng dưới âm, dùng các phương trình 7-7 đến 7-11, trong đó hệ số "
      "F được đọc từ Hình 7-2 theo tỉ lệ áp và k. Khi xác định F, áp ngược "
      "phải lấy P'2 trong buồng giữa miệng phóng và đầu ra van, không phải "
      "áp tại mặt bích nếu nhà chế tạo không cung cấp cách chuyển đổi. Nếu "
      "không xác định được P'2, phải dùng hệ số xả xác định theo API "
      "Standard 2000.",
      "For subsonic flow, equations 7-7 to 7-11 apply, with factor F read "
      "from Figure 7-2 against pressure ratio and k. For F, the back pressure "
      "must be P'2 in the chamber between nozzle and valve outlet, not simply "
      "the flange pressure unless the maker supplies a conversion. If P'2 "
      "cannot be found, use a discharge coefficient determined under API "
      "Standard 2000.")
    FIG(2, F14.fig_vsh_7_2())
    P("Hệ số Kb trên Hình 7-3 hiệu chỉnh ảnh hưởng của áp ngược tích lũy và "
      "áp ngược chồng lên đến hành trình của van cân bằng bellows dùng cho "
      "khí hoặc hơi. Kb giữ ở 1,0 khi áp ngược thấp, sau đó giảm; mức giảm "
      "phụ thuộc quá áp 10% hay 20%.",
      "Figure 7-3 gives Kb for the effect of built-up and superimposed back "
      "pressure on the lift of bellows-balanced gas or vapor valves. Kb stays "
      "at 1.0 for low back pressure and then falls, with the decline depending "
      "on 10% or 20% overpressure.")
    FIG(3, F14.fig_vsh_7_3())

    # ============================================================ steam
    H("Hơi bão hòa và hơi quá nhiệt", "Dry saturated and superheated steam")
    P("Tại Hoa Kỳ, van an toàn xả hơi bão hòa từng được định cỡ theo phương "
      "trình dòng hơi Napier, được lập thực nghiệm cho điều kiện tới hạn. "
      "Đến khoảng 105 bara (1515 psia), Napier cho kết quả tương tự phương "
      "trình khí tổng quát với k = 1,3. Ở áp cao hơn, Napier có thể dự báo "
      "diện tích quá lớn; vì vậy Thompson và Buxton đưa vào hệ số KN.",
      "In the United States, dry saturated steam relief valves were "
      "historically sized by Napier's empirically formulated choked-flow "
      "equation. Up to about 105 bara (1515 psia), Napier agrees with general "
      "gas equations using k = 1.3. At higher pressures it can grossly "
      "oversize, which led Thompson and Buxton to introduce KN.")
    E("A = W / (51.5 K P<sub>1</sub> K<sub>N</sub> K<sub>SH</sub>)",
      "7-12")
    P("Với P1 dưới 1515 psia, KN = 1. Trên miền đó đến 3215 psia, KN được "
      "tính theo biểu thức thực nghiệm hoặc đọc từ Hình 7-4. Hệ số KSH cho "
      "độ quá nhiệt lấy từ Bảng 7-3. Hệ SI dùng dạng phương trình 7-13 với "
      "giới hạn tương ứng 105 bara và 221,7 bara.",
      "For P1 below 1515 psia, KN = 1. Above that range up to 3215 psia, KN "
      "comes from the empirical expression or Figure 7-4. The superheat "
      "factor KSH is taken from Table 7-3. SI form equation 7-13 uses the "
      "corresponding limits of 105 bara and 221.7 bara.")
    FIG(4, F14.fig_vsh_7_4())

    # ============================================================ liquid
    H("Dòng chất lỏng", "Liquid flow")
    P("Với chất lỏng, diện tích miệng phóng phụ thuộc lưu lượng, hệ số xả K, "
      "các hệ số hiệu chỉnh quá áp, áp ngược và độ nhớt, cùng độ chênh áp "
      "qua van. Dạng lưu lượng khối hệ SI được cho ở phương trình 7-15:",
      "For liquid service, nozzle area depends on flow, discharge coefficient "
      "K, overpressure, back-pressure and viscosity corrections, and the "
      "pressure differential across the valve. The SI mass-flow form is "
      "equation 7-15:")
    E("A = 0.621 W / [K K<sub>P</sub> K<sub>V</sub> K<sub>W</sub> "
      "√((P<sub>1</sub> − P<sub>2</sub>) ρ)]", "7-15")
    P("Kp trên Hình 7-5 áp dụng cho van cần 25% quá áp để mở hoàn toàn. Ở quá "
      "áp thấp hơn 25%, phải dùng Kp; dưới 10% nguy cơ rung van tăng rõ rệt. "
      "Với van mở hoàn toàn trong vòng 10% quá áp, giá trị K đã chứng nhận "
      "phải lấy từ nhà chế tạo. Trên 25%, lưu lượng chỉ thay đổi theo chính "
      "độ quá áp.",
      "Kp in Figure 7-5 applies to valves needing 25% overpressure for full "
      "lift. At lower overpressure Kp must be used; below 10% the tendency to "
      "chatter is heightened. For valves fully open within 10% overpressure, "
      "the certified K must come from the manufacturer. Above 25%, capacity "
      "changes only with overpressure itself.")
    FIG(5, F14.fig_vsh_7_5())
    P("Kw trên Hình 7-6 là hệ số áp ngược cho van chất lỏng cân bằng "
      "bellows; giá trị sản phẩm cụ thể phải hỏi nhà chế tạo. Van thường "
      "chịu ảnh hưởng của áp ngược tích lũy, nhưng thường không được phép "
      "hiệu chỉnh lưu lượng theo áp ngược này.",
      "Kw in Figure 7-6 is the back-pressure factor for bellows-balanced "
      "liquid valves; product-specific values must come from the maker. "
      "Conventional valves are affected by built-up back pressure, but "
      "capacity correction for it is not commonly allowed.")
    FIG(6, F14.fig_vsh_7_6())
    P("Khi dịch vụ có độ nhớt, phải lặp: trước tiên tính theo dòng không "
      "nhớt và chọn cỡ miệng tiêu chuẩn kế tiếp; sau đó tính số Reynolds từ "
      "phương trình 7-16, 7-17 hoặc 7-18; đọc Kv từ Hình 7-7 và áp vào diện "
      "tích ban đầu. Nếu diện tích đã hiệu chỉnh vượt cỡ đã chọn, lặp lại "
      "với cỡ lớn hơn. Phương trình theo Saybolt không nên dùng dưới 100 SU.",
      "For viscous service, iterate: first solve non-viscous flow and choose "
      "the next standard orifice; then compute Reynolds number from equation "
      "7-16, 7-17 or 7-18; read Kv from Figure 7-7 and apply it to the initial "
      "area. If the corrected area exceeds the chosen orifice, repeat with the "
      "next larger size. The Saybolt expression is not recommended below "
      "100 SU.")
    FIG(7, F14.fig_vsh_7_7())

    # ====================================================== inlet pressure loss
    H("Tổn thất áp đầu vào và đường ống vào", "Inlet pressure loss and inlet piping")
    P("Lưu lượng xả phản ứng với áp tại đầu vào van, bằng áp cài đặt trừ tổn "
      "thất áp đường vào. Với dòng khí tới hạn, lưu lượng khối giảm tỉ lệ "
      "thuận với tổn thất áp đầu vào; với dòng khí dưới âm và chất lỏng, mức "
      "thay đổi phụ thuộc độ chênh áp qua miệng phóng. Thông lệ bỏ qua tổn "
      "thất 3% khi định cỡ van tác động trực tiếp, nhưng mọi tổn thất vượt 3% "
      "đều phải tính đến, nhất là với pilot dạng chảy kiểu bật.",
      "Discharge capacity responds to pressure at the valve inlet, equal to "
      "set pressure minus inlet pressure loss. For sonic gas flow, mass flow "
      "falls in direct proportion to inlet loss; for subsonic gas and liquid, "
      "the change depends on the differential across the nozzle. A 3% inlet "
      "loss is commonly neglected for direct-acting valves, but any loss "
      "above 3% must be accounted for, especially with snap-acting flowing "
      "pilots.")
    P("Quy tắc lắp đặt yêu cầu tổng tổn thất không hồi phục trong đường vào, "
      "kể cả tổn thất lối vào tại cổng bình, không vượt quá 3% áp cài đặt ở "
      "lưu lượng định mức. Quy trình Hình 7-8 gồm: ước tính hệ số trở lực "
      "đường hiện có, tính 0,9Ae/(AnK), đọc hệ số cho tổn thất 3%, rồi so "
      "sánh. Hình lập cho khí và hơi có k = 1,3; đường gạch đứt áp dụng cho "
      "chất lỏng không phụ thuộc tỉ lệ P2/P1.",
      "Installation codes require cumulative non-recoverable inlet loss, "
      "including vessel-nozzle entry loss, not to exceed 3% of set pressure "
      "at rated mass flow. The Figure 7-8 procedure estimates the proposed "
      "resistance coefficient, computes 0.9Ae/(AnK), reads the coefficient "
      "for 3% loss and compares the two. The chart assumes k = 1.3 for gas "
      "and vapor; the dashed line applies to liquids regardless of P2/P1.")
    FIG(8, F14.fig_vsh_7_8())

    # ======================================================= discharge piping
    H("Đường ống xả", "Discharge piping")
    P("Trước khi định cỡ ống xả, phải lấy từ nhà chế tạo áp ngược cho phép "
      "P2 tại đầu ra van. Với van cân bằng bellows, áp ngược cho phép là "
      "tổng áp ngược tích lũy và áp ngược chồng lên. Sau khi tính hệ số trở "
      "lực của ống đề xuất, so sánh với hệ số tương ứng với áp ngược cho "
      "phép; nếu ống đề xuất có trở lực cao hơn, phải thiết kế lại.",
      "Before sizing the discharge pipe, obtain the permissible outlet back "
      "pressure P2 from the valve manufacturer. For bellows-balanced valves "
      "it is the sum of built-up and superimposed back pressure. Compute the "
      "resistance coefficient of the proposed pipe and compare it with the "
      "coefficient for permissible built-up back pressure; redesign if the "
      "proposed line is more resistive.")
    P("Với chất lỏng, phương trình 7-19 biểu thị áp ngược tích lũy theo "
      "chênh áp qua van; nếu giới hạn 10% áp cài đặt, phương trình 7-20 cho "
      "ζ của ống xả. Với khí hoặc hơi, tính tỉ lệ áp tới hạn theo phương "
      "trình 7-21, xác định PT, rồi dùng P2/PT với Hình 7-9 để đọc hệ số trở "
      "lực cho áp ngược tích lũy cho phép.",
      "For liquids, equation 7-19 expresses built-up back pressure relative "
      "to the differential across the valve; if the limit is 10% of set "
      "pressure, equation 7-20 gives the discharge-line ζ. For gas or vapor, "
      "calculate the critical pressure relation in equation 7-21, determine "
      "PT, then use P2/PT with Figure 7-9 to read the resistance coefficient "
      "for permissible built-up back pressure.")
    FIG(9, F14.fig_vsh_7_9())

    # ====================================================== rupture disc sizing
    H("Định cỡ đĩa vỡ", "Rupture disc sizing")
    H("Dao động áp không dữ dội", "Nonviolent pressure excursions", h3)
    P("Đĩa vỡ được dùng cả ở hệ thống có dao động áp không dữ dội như hệ "
      "thống dùng van an toàn, lẫn hệ thống chịu tăng áp dữ dội do cháy chậm "
      "khí hoặc bụi trong bình thành mỏng. Hai chế độ này cần cách định cỡ "
      "khác nhau.",
      "Rupture discs serve systems with nonviolent excursions like those "
      "handled by relief valves, and systems subject to violent excursions "
      "from deflagration of gases or dusts in low-strength containers. The two "
      "regimes require different sizing approaches.")
    P("ASME Code (1992) và API RP 520 Part I (1993) cho phép phương trình "
      "đơn giản với K = 0,62 khi bỏ qua tổn thất đường vào và đường xả, "
      "với điều kiện: đĩa xả trực tiếp ra khí quyển, đặt trong vòng tám đường "
      "kính ống từ cổng bình, chiều dài ống xả không quá năm đường kính, "
      "đường kính danh nghĩa vào và ra không nhỏ hơn NPS ghi trên thiết bị, và "
      "diện tích A là diện tích lưu thông ròng nhỏ nhất do nhà chế tạo "
      "xác định. Trong giới hạn đó, dùng các phương trình 7-22 đến 7-31 "
      "tương tự phương trình van an toàn.",
      "The ASME Code (1992) and API RP 520 Part I (1993) allow a simplified "
      "K = 0.62 method that neglects inlet and discharge pressure drops, "
      "provided the disc discharges directly to atmosphere, lies within eight "
      "pipe diameters of the vessel nozzle, has no more than five pipe "
      "diameters of discharge pipe, inlet and discharge nominal diameters at "
      "least the stamped NPS, and uses the manufacturer's minimum net flow "
      "area as A. Within those limits, equations 7-22 to 7-31 mirror the "
      "relief-valve equations.")
    P("ISO 6718 cũng cho phép phương pháp trở lực dòng, đòi hỏi phân tích "
      "toàn hệ thống và hệ số trở lực chứng nhận KR của đĩa vỡ. Phương pháp "
      "này đang được đưa vào sửa đổi ASME, API và tiêu chuẩn châu Âu; nó "
      "thường cần phần mềm để tính nhanh và chính xác.",
      "ISO 6718 also permits a flow-resistance method requiring analysis of "
      "the whole system and a certified disc resistance factor KR. This "
      "approach is entering pending ASME and API revisions and the emerging "
      "European standard; it often needs software for speed and accuracy.")
    H("Dao động áp dữ dội", "Violent pressure excursions", h3)
    P("Với tấm thông nổ trong bình thành mỏng, số liệu định cỡ dựa trên mô "
      "hình đơn giản và thử nghiệm nổ hơi hoặc bụi. Quy trình được khuyến "
      "nghị trong NFPA Guide for Venting of Deflagrations và VDI-Richtlinien "
      "3673 (1995). Các yếu tố ảnh hưởng gồm thể tích và hình dạng bình, "
      "đồng nhất hay không đồng nhất của hỗn hợp, áp tối đa cho phép khi xả, "
      "áp vỡ tĩnh của tấm thông, mức độ nổ theo KST cho bụi hoặc KG cho khí, "
      "và việc áp dụng nomogram.",
      "For vent panels on low-strength containers, sizing data come from "
      "simple models and vapor or dust explosion tests. Recommended "
      "procedures appear in the NFPA Guide for Venting of Deflagrations and "
      "VDI-Richtlinien 3673 (1995). Influencing factors include enclosure "
      "volume and shape, mixture homogeneity, maximum permitted venting "
      "pressure, static burst pressure of the panel, explosion severity as "
      "KST for dust or KG for gas, and use of nomograms.")

    # ================================================================== table
    H("Bảng tóm tắt định cỡ", "Sizing summary")
    b.append(table(
        ["Hình / chủ đề", "Áp dụng", "Điểm chính"]
        if vi else ["Figure / topic", "Application", "Key point"],
        [
            ["7-1", "Lắp đặt điển hình" if vi else "Typical installation",
             "Chỉ số P1, P'2, P2, P3" if vi else "Subscripts P1, P'2, P2, P3"],
            ["dòng khí" if vi else "Gas flow",
             "Tới hạn / dưới âm" if vi else "Sonic / subsonic",
             "Tỉ lệ tới hạn theo k" if vi else "Critical ratio depends on k"],
            ["7-2", "Hệ số F" if vi else "Factor F",
             "Đọc theo tỉ lệ áp và k" if vi else "Read from pressure ratio and k"],
            ["7-3", "Van bellows" if vi else "Bellows valve",
             "Kb theo áp ngược" if vi else "Kb versus back pressure"],
            ["7-4", "Hơi áp cao" if vi else "High-pressure steam",
             "KN trên 105 bara" if vi else "KN above 105 bara"],
            ["7-5", "Chất lỏng 25%" if vi else "Liquid 25% lift",
             "Kp; dưới 10% rung van" if vi else "Kp; below 10% chatter"],
            ["7-6", "Bellows chất lỏng" if vi else "Liquid bellows",
             "Kw theo áp ngược" if vi else "Kw versus back pressure"],
            ["7-7", "Độ nhớt" if vi else "Viscosity",
             "Lặp Kv theo Reynolds" if vi else "Iterate Kv via Reynolds"],
            ["7-8", "Ống vào" if vi else "Inlet piping",
             "Tổng tổn thất ≤3%" if vi else "Total loss ≤3%"],
            ["7-9", "Ống xả" if vi else "Discharge piping",
             "P2/PT → ζ" if vi else "P2/PT → ζ"],
            ["đĩa vỡ" if vi else "Rupture disc",
             "Dao động không dữ dội" if vi else "Nonviolent duty",
             "K = 0,62 trong giới hạn" if vi else "K = 0.62 within limits"],
            ["tấm thông nổ" if vi else "Vent panel",
             "Dao động dữ dội" if vi else "Violent duty",
             "NFPA 68 / VDI 3673" if vi else "NFPA 68 / VDI 3673"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 269–292, "
                 "Hình 7-1…7-9." if vi else
                 "Summary from source text, book pp. 269–292, "
                 "Figures 7-1…7-9."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
