# -*- coding: utf-8 -*-
"""Book 7, Chapter 15 - Cavitation (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
103-108 (PDF pp. 106-111). Five vector figures, one material-lifetime table,
several equations, an application pointer, two references and two
additional-reading items.
"""
from cvp_common import eq, fig, h2, h3, note, ol, p, refs, table, ul
import cvpfig15 as F

PAGES_SRC = 6
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Cavitation"
TITLE_VI = "Xâm thực"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 15.</b> xâm thực (cavitation) · implode / sụp đổ bong bóng "
                "hơi · áp suất va đập · mức ồn tương đối (dB) · mức ồn A-weighted (dBA) · "
                "thành phần bộ lót chịu mòn · tuổi thọ tương đối · hạ áp chất lỏng · tep hơi "
                "(flash tank) · hóa hơi (flashing) · hệ số bắt đầu xâm thực X_Fz · tỷ số áp "
                "suất X = (P1 − P2)/(P1 − Pv) · áp suất hơi hóa Pv · dòng bị nghẽn (choked "
                "flow) · vận tốc tia Uvc · tốc độ âm trong chất lỏng ci · hệ số FL · độ dốc "
                "60 log(X/X_Fz) · Xy (xâm thực cực đại) · tiếng ồn rối (turbulent sound) · "
                "hiệu suất âm thanh · phun khí vào dòng (air injection) · trục van rỗng · "
                "van một chiều (check valve) · van bướm chống xâm thực răng cưa (sharktooth) "
                "· Cv · giảm áp đa cấp (multistage let-down) · van cầu thông thường · bình "
                "hở / xả ra khí quyển · hố rỗ do xâm thực · bộ lót tôi cứng (ceramic, "
                "Stellite) · đế van / bệ van / mặt tựa của van (seat).")
    return ("<b>Key terms.</b> cavitation · bubble implosion · impact pressure · relative sound "
            "level (dB) · A-weighted sound level (dBA) · wear-resistant trim · relative "
            "lifetime · liquid pressure reduction · flash tank · flashing · incipient "
            "cavitation coefficient X_Fz · pressure ratio X = (P1 − P2)/(P1 − Pv) · vapor "
            "pressure Pv · choked flow · jet velocity Uvc · liquid sound speed ci · FL · "
            "60 log(X/X_Fz) slope · Xy (maximum cavitation) · turbulent sound · acoustical "
            "efficiency · air injection · hollow valve stem · check valve · sharktooth "
            "anticavitation butterfly valve · Cv · multistage pressure let-down · conventional "
            "globe valve · open tank / atmospheric discharge · cavitation pitting · hardened "
            "trim (ceramic, Stellite) · seat.")


def body_vi():
    b = []
    b.append(h2("Cơ chế xâm thực", "The cavitation mechanism"))
    b.append(p("Tôi từng nói, nửa đùa nửa thật, rằng xâm thực là người bạn tốt nhất của nhà "
               "sản xuất, vì nó tạo ra nhu cầu ổn định cho các bộ phận bộ lót thay thế. Không "
               "có gì lạ, bởi cơ chế xâm thực — sự sụp đổ dữ dội của các bong bóng hơi trong "
               "chất lỏng sau khi dòng chất lỏng giảm tốc và áp suất sau đó phục hồi — có thể "
               "tạo áp suất va đập tới 1,5 × 10³ N/mm² trên bề mặt nút van, thành trong của "
               "thân van hoặc thành ống đối với nước (218.000 psi!). Không có vật liệu nào "
               "được biết đến có thể chịu được hư hỏng do xâm thực. Tuy nhiên, vật liệu cứng "
               "hơn (giới hạn ứng suất đàn hồi cao hơn) sẽ bền hơn vật liệu mềm hơn. Ví dụ, "
               "sau đây là tuổi thọ tương đối của một số vật liệu (cùng mức tổn hao vật liệu "
               "trong cùng điều kiện xâm thực) [1]:"))
    b.append(table(
        ["Vật liệu", "Tuổi thọ tương đối"],
        [["Hợp kim nhôm mềm", "1"],
         ["Thép carbon loại 1020", "2,4"],
         ["Thép không gỉ loại 304", "6,5"],
         ["Thép tôi cứng 42% Cr, 4% Mo", "13"]],
        caption="Bảng 15.1 · Tuổi thọ tương đối của vật liệu trong cùng điều kiện xâm thực"))
    b.append(p("Xâm thực — sự implode dữ dội của các bong bóng hơi li ti trong dòng chất lưu — "
               "có lẽ là nguyên nhân chính gây bảo trì các van điều khiển xử lý giảm áp chất "
               "lỏng. Vì vậy, điều quan trọng là hiểu hiện tượng này và có thể tính toán tiếng "
               "ồn sinh ra như một chỉ thị cho mức độ phá hủy mà nó có thể gây ra. Sau đây là "
               "giải thích về quá trình vật lý liên quan."))
    b.append(note("<b>Lưu ý.</b> Không phải chỉ có nước mới bị xâm thực. Điều đó là sai. Xâm thực "
                  "cũng xảy ra ở van điều khiển dầu thô trong đường ống."))

    b.append(p("Khi áp suất phía dưới van giảm đến và vượt quá một tỷ số áp suất tương ứng gọi "
               "là X_Fz, áp suất tĩnh trong lỗ tiết lưu của van đạt tới áp suất hơi hóa của "
               "chất lỏng. Điều này gây bay hơi một phần chất lỏng, đồng thời hình thành các "
               "bong bóng hơi nhỏ. Tại thời điểm đó, chất lỏng đạt vận tốc cao nhất. Sau khi "
               "đi qua lỗ tiết lưu, vận tốc chất lỏng bắt đầu giảm trong khi áp suất tĩnh "
               "tăng. Khi áp suất tĩnh của chất lỏng vượt áp suất hơi hóa, các bong bóng bắt "
               "đầu implode, tạo ra sóng xung kích âm thanh. Điều này sinh ra sóng âm tuân theo "
               "định luật âm thanh khí và có thể đạt mức ồn tới 125 dB."))
    b.append(eq("X = (P1 − P2) / (P1 − Pv)"))
    b.append(p("Việc giảm thêm áp suất đầu ra làm tăng đường kính của tia chất lỏng và làm "
               "vận tốc của nó giảm tỷ lệ với áp suất tĩnh tăng lên, theo định luật Bernoulli "
               "(giả sử áp suất đầu vào không đổi). Hãy lưu ý rằng có dòng bị nghẽn (tức là "
               "vận tốc trong lỗ tiết lưu giữ không đổi trong lúc xâm thực). Độ tăng áp suất "
               "âm thanh do xâm thực tương ứng với 60 log(X/X_Fz) theo định luật âm thanh khí; "
               "ở đây X là tỷ số áp suất nêu trên và X_Fz là hệ số bắt đầu xâm thực. Hình 15-1 "
               "cho thấy quan hệ giữa X_Fz và mức ồn sinh ra."))
    b.append(fig(1, F.fig_f151()))

    b.append(h2("Tránh xâm thực", "Cavitation avoidance"))
    b.append(p("Trong hầu hết trường hợp có thể tránh quá trình này bằng cách chọn bộ lót loại "
               "F_L cao, dời van đến vị trí có áp suất tĩnh cao hơn, đặt thêm một phần tử "
               "tiết lưu ở phía dưới, hoặc phun không khí/khí vào van gần nút van hoặc cánh "
               "van (xem Hình 15-2). Việc chọn bộ lót tôi cứng chỉ kéo dài tuổi thọ và, đương "
               "nhiên, sẽ tăng doanh thu của nhà cung cấp nhờ bán phụ tùng (xem thêm Chương "
               "14). Một số trường hợp xâm thực, đặc biệt với nước nóng (nước ngưng tụ), là "
               "do đặt van quá xa bình flash tank."))
    b.append(fig(2, F.fig_f152()))
    b.append(p("Tôi đã đóng góp kiến thức mới về hiểu biết và ước tính tiếng ồn của xâm thực "
               "trong Hình 15-1."))
    b.append(ol([
        "Xâm thực là một quá trình khí động học độc lập với độ rối nền. Điều này thấy rõ qua "
        "độ dốc 60 log(X) của đường giữa X_Fz và Xy (tỷ số giảm áp X mà tại đó xâm thực cực "
        "đại)." + eq("60 log(X)"),
        "Mức ồn xâm thực cực đại đạt được khi cột áp động của tia bên trong và cột áp tĩnh "
        "bằng nhau tại Xy. Ở đây " + eq("Xy = (1 + X_Fz) / 2"),
        "Đường mức ồn rối bên ngoài bằng 30 log(X) cho đến X = F_L²."
        + eq("30 log(X)   (X ≤ F_L²)"),
        "Hệ số hiệu suất âm thanh đối với chất lỏng là (Uvc/ci) × 10⁻⁴. Ở đây Uvc = vận tốc "
        "tia và ci = tốc độ âm thanh của chất lỏng."
        + eq("(Uvc / ci) × 10⁻⁴"),
    ]))

    b.append(h3("Lời khuyên ứng dụng", "Application pointer"))
    b.append(p("Có thể phát sinh vấn đề khi đối diện với các ứng dụng giảm áp cao, chẳng hạn "
               "xả 1000 psi nước ra khí quyển. Cách thông thường là quy định van chống xâm "
               "thực đa cấp với giả định sáu cấp giống hệt nhau, mỗi cấp có tỷ số áp suất "
               "(X) bằng 0,25. Phần giảm áp cuối cùng ở cấp cuối là từ 180 psia xuống 14,5 "
               "psia."))
    b.append(p("Thay vì giải pháp đắt tiền đó, tôi khuyên dùng một van cầu thông thường và "
               "giảm áp trong một bước (one sloop). Khi đó van có tỷ số áp suất X = 0,99."))
    b.append(p("Đồ thị Hình 15-1 cho thấy không còn xâm thực ở tỷ số áp suất 0,99, do đó không "
               "có hư hỏng hay tiếng ồn do xâm thực (vẫn còn tiếng ồn rối nhưng ở mức thấp "
               "hơn nhiều)."))
    b.append(p("Điều gì xảy ra với năng lượng động học 1000 psi? Nó vẫn được tiêu hao bằng "
               "cách tạo ra hàng triệu bong bóng hơi li ti. Tuy nhiên, vì áp suất phía dưới "
               "là 14,5 psia, không có đủ chênh áp để làm chúng implode; vì vậy chúng lặng lẽ "
               "trở lại thành chất lỏng. Ở đây ta có một quá trình “hóa hơi” (flashing)."))
    b.append(note("<b>Lưu ý.</b> Cách này chỉ làm việc nếu van xả trực tiếp vào một bình hở "
                  "hoặc ra không khí, để tránh áp suất ngược."))
    b.append(p("Dữ liệu thử nghiệm cho một van bướm chống xâm thực (Hình 15-3) được trình bày "
               "trong Hình 15-4. Hãy chú ý hệ số X_Fz cao bất thường là 0,64, cho biên độ xâm "
               "thực chỉ 6,4 dB ở tỷ số áp suất 0,82. Một van bướm thông thường với X_Fz = 0,3 "
               "(Xy = 0,65) sẽ chịu mức ồn xâm thực cực đại 110 dB trong cùng điều kiện dòng."))
    b.append(fig(3, F.fig_f153()))
    b.append(fig(4, F.fig_f154()))

    b.append(h2("Hư hỏng do xâm thực", "Damage caused by cavitation"))
    b.append(p("Hình 15-5 cho thấy loại hư hỏng do xâm thực gây ra. Trong trường hợp này, xâm "
               "thực kéo dài đã ăn mòn một nửa nút van dạng parabol ban đầu. Sự phá hủy tương "
               "tự cũng xảy ra tại lỗ tiết lưu tương ứng của van."))
    b.append(fig(5, F.fig_f155()))
    b.append(p("Sự phá hủy tương tự như trong Hình 15-5 xảy ra khi mức ồn bên ngoài vượt 80 "
               "dBA. Jon Monsen [2] đề xuất một thang theo cỡ van: 85 dBA cho van 4 in đến "
               "6 in, 90 dBA cho cỡ 8 in đến 14 in và 95 dBA cho các cỡ lớn hơn."))
    b.append(p("Dù bộ lót tôi cứng như gốm hoặc Stellite có thể kéo dài tuổi thọ, không có vật "
               "liệu vành van nào được biết đến chịu được hư hỏng do xâm thực vì các sóng áp "
               "suất cực cao (vượt 100.000 psi) của các bong bóng hơi implode."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "W. L. Kennecott, “Use of Hard Carbide Components,” in Petrochemical Processing, "
        "ASME Paper 61-SA-51 (1962).",
        "Jon Monsen, “Predicting Cavitation Damage in Control Valves,” Flow Control magazine "
        "(May 2018): 4–17.",
    ]))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "T. Dobben, “Kavitation in Stellglieder” (Frankfurt, Germany: SAMSON AG).",
        "H. D. Baumann, “A Practical Guide for the Cavitation Prevention of Throttling "
        "Butterfly Valves,” ISA paper C.l.84-R777 (Research Triangle Park, NC: ISA "
        "[Instrument Society of America], October 1984).",
    ]))
    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR có nhiều dấu gạch nối khi xuống "
                  "dòng («mech-», «lon-», «relo-», «turbu-»); bản dịch ghép lại thành từ hoàn "
                  "chỉnh. Ký hiệu «X Fz» được chuẩn hóa thành X_Fz và «P 1», «P 2» thành P1, "
                  "P2. (2) Văn bản in «one sloop» (thay vì «one step»); bản dịch giữ nguyên "
                  "ý định là giảm áp trong một bước và ghi chú lỗi này. (3) Hình 15-2 ghi nguồn "
                  "«Courtesy of H. D. Baumann», Hình 15-5 ghi «Photo courtesy of Jon Monsen»; "
                  "bản dịch giữ các ghi nhận đó trong chú thích hình, đồng thời ghi rõ các "
                  "hình là bản vẽ lại vector đã đơn giản hóa, không phải ảnh gốc. (4) Bảng "
                  "tuổi thọ vật liệu được dựng lại từ bốn dòng in rời rạc trên trang 103; giá "
                  "trị giữ nguyên. (5) Các ký hiệu toán học trong bản gốc được trình bày lại "
                  "dạng ký hiệu Unicode trong bản dịch."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 15 chiếm các trang in 103–108 của ấn bản in (PDF tr. 106–111). Nguyên "
               "bản gồm phần mở đầu, giải thích cơ chế, mục tránh xâm thực, bốn đóng góp của "
               "tác giả, một lời khuyên ứng dụng, mục hư hỏng, bảng tuổi thọ vật liệu, năm "
               "hình, hai tài liệu tham khảo và hai mục đọc thêm — tất cả đều được giữ lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Cơ chế xâm thực", "The cavitation mechanism"))
    b.append(p("I used to say, only half in jest, that cavitation is the manufacturer's best "
               "friend because it supplies a steady demand for replacement trim parts. No "
               "wonder, because the mechanism of cavitation (violent collapse of vapor bubbles "
               "in a liquid following deceleration of the liquid flow and subsequent pressure "
               "recovery) can cause impact pressures on the surface of the valve plug, the "
               "inner body wall, or the pipe wall up to 1.5 × 10³ N/mm² for water (218,000 "
               "psi!). There is no material known to man that will withstand cavitation "
               "damage. However, a harder material (higher elastic stress limit) will last "
               "longer than a softer material. For example, here are the relative lifetimes of "
               "some materials (same material loss under the same cavitation conditions) [1]:"))
    b.append(table(
        ["Material", "Relative lifetime"],
        [["Soft aluminum alloy", "1"],
         ["Type 1020 carbon steel", "2.4"],
         ["Type 304 stainless steel", "6.5"],
         ["Hardened 42% chromium (Cr), 4% molybdenum (Mo) steel", "13"]],
        caption="Table 15.1 · Relative material lifetimes under the same cavitation conditions"))
    b.append(p("Cavitation, the violent implosion of tiny vapor bubbles in a fluid stream, "
               "probably is the primary cause for maintenance on control valves that handle "
               "the pressure reduction of liquids. It is therefore important to understand "
               "this phenomenon and to be able to calculate the resultant noise as an "
               "indicator of the degree of destruction that it may cause. The following is an "
               "explanation of the physical process involved in cavitation."))
    b.append(note("<b>Note.</b> One might believe that only water cavitates. This is wrong. "
                  "Cavitation also happens with valves controlling crude oil in pipelines."))

    b.append(p("When the downstream pressure in a valve decreases at and beyond a corresponding "
               "pressure ratio called X_Fz, the static pressure in the valve's orifice reaches "
               "the vapor pressure of the liquid. This causes evaporation of some of the liquid "
               "with the simultaneous formation of small vapor bubbles. At this point, the "
               "liquid reaches its highest velocity. After passing the orifice, the liquid "
               "velocity starts to decrease while the static pressure increases. When the "
               "liquid static pressure exceeds vapor pressure, the bubbles start to implode, "
               "creating sonic shock waves. This causes acoustic sound waves that follow the "
               "laws of gas acoustics and reach sound levels up to 125 dB."))
    b.append(eq("X = (P1 − P2) / (P1 − Pv)"))
    b.append(p("Further reduction in outlet pressure causes more of the diameter of the jet to "
               "enlarge and its velocity to decrease in proportion to the increased static "
               "pressure following the laws of Bernoulli (assuming constant inlet pressure). "
               "Note that there is choked flow (that is, the orifice velocity stays constant "
               "during cavitation). The resultant sound pressure from the cavitation increase "
               "corresponds to 60 log(X/X_Fz) following the acoustic gas laws; here X is a "
               "pressure ratio as given above, and X_Fz is a coefficient of incipient "
               "cavitation. Figure 15-1 shows the relationship between X_Fz and the resultant "
               "sound level."))
    b.append(fig(1, F.fig_f151()))

    b.append(h2("Cavitation avoidance", "Cavitation avoidance"))
    b.append(p("This process can be avoided in most cases by selecting a high F_L type trim and "
               "by relocating the valve to a point of higher static pressure, by placing an "
               "additional restrictor downstream, or by injecting air or gas into the valve "
               "near the plug or vane (see Figure 15-2). Selecting a hardened trim will only "
               "prolong the service and, of course, will increase the revenue of your vendor "
               "from the sale of spare parts (see also Chapter 14). Some cavitation, especially "
               "with hot water (condensate), is due to placing the valve too far away from the "
               "flash tank."))
    b.append(fig(2, F.fig_f152()))
    b.append(p("I contributed new knowledge about the understanding and sound estimation of "
               "cavitation in Figure 15-1."))
    b.append(ol([
        "Cavitation is an aerodynamic process independent of the underlying turbulence. This "
        "can be seen by the 60 log(X) slope of the curve between X_Fz and Xy (the pressure "
        "drop X where max cavitation occurs)." + eq("60 log(X)"),
        "A maximum of cavitation sound is achieved when the internal jet velocity head and the "
        "static head are equal at Xy. Here " + eq("Xy = (1 + X_Fz) / 2"),
        "The external turbulent sound profile is equal to 30 log(X) up to X = F_L²."
        + eq("30 log(X)   (X ≤ F_L²)"),
        "The acoustical efficiency factor for liquids is: (Uvc/ci) × 10⁻⁴. Here Uvc = jet "
        "velocity and ci = speed of sound of liquid." + eq("(Uvc / ci) × 10⁻⁴"),
    ]))

    b.append(h3("Application pointer", "Application pointer"))
    b.append(p("Problems can arise when faced with high-pressure let-down applications, such as "
               "releasing 1000 psi water to the atmosphere. The normal wisdom is to specify a "
               "multistage anticavitation valve with assumed six identical stages, each with a "
               "pressure ratio (X) of 0.25. This leaves a final pressure drop at the last stage "
               "of 180 psia to 14.5 psia."))
    b.append(p("Rather than such an expensive solution, I recommend using a conventional globe "
               "valve and reducing the pressure in one sloop. This valve then has a pressure "
               "ratio of X = 0.99."))
    b.append(p("The graph in Figure 15-1 indicates that there is no more cavitation at a "
               "pressure ratio of 0.99 and therefore no damage or cavitation noise (there still "
               "is turbulent noise but at a much lower level)."))
    b.append(p("What happens with the 1000 psi kinetic energy? It still is gone by producing "
               "millions of tiny vapor bubbles. However, because the downstream pressure is "
               "14.5 psia, there is insufficient pressure difference to make them implode; "
               "therefore, they quietly turn back into liquid. Here, we have a process of "
               "“flashing.”"))
    b.append(note("<b>Note.</b> This scheme only works if the valve discharges directly into an "
                  "open tank or into air to avoid back pressure."))
    b.append(p("Test data for an anticavitation butterfly valve (Figure 15-3) are shown in "
               "Figure 15-4. Note the exceptionally high X_Fz factor of 0.64, resulting in a "
               "cavitation amplitude of only 6.4 dB at a pressure ratio of 0.82. A conventional "
               "butterfly valve with an X_Fz of 0.3 (Xy = 0.65) would see a maximum cavitation "
               "sound level of 110 dB under the same flow conditions."))
    b.append(fig(3, F.fig_f153()))
    b.append(fig(4, F.fig_f154()))

    b.append(h2("Damage caused by cavitation", "Damage caused by cavitation"))
    b.append(p("Figure 15-5 shows the type of damage caused by cavitation. In this case, "
               "prolonged cavitation ate away one-half of the original parabolic valve plug. "
               "Similar destruction happened at the corresponding valve orifice."))
    b.append(fig(5, F.fig_f155()))
    b.append(p("Destruction similar to that shown in Figure 15-5 happens when the external "
               "sound level exceeds 80 dBA. Jon Monsen [2] suggests a sliding scale such as 85 "
               "dBA for valve sizes 4 in to 6 in, 90 dBA for sizes 8 in to 14 in, and 95 dBA "
               "for larger sizes."))
    b.append(p("Even though hardened trim such as ceramics or Stellite can prolong service "
               "life, there is no known valve rim material that can withstand cavitation damage "
               "due to the extremely high-pressure waves (exceeding 100,000 psi) of the "
               "imploding vapor bubbles."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "W. L. Kennecott, “Use of Hard Carbide Components,” in Petrochemical Processing, "
        "ASME Paper 61-SA-51 (1962).",
        "Jon Monsen, “Predicting Cavitation Damage in Control Valves,” Flow Control magazine "
        "(May 2018): 4–17.",
    ]))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "T. Dobben, “Kavitation in Stellglieder” (Frankfurt, Germany: SAMSON AG).",
        "H. D. Baumann, “A Practical Guide for the Cavitation Prevention of Throttling "
        "Butterfly Valves,” ISA paper C.l.84-R777 (Research Triangle Park, NC: ISA "
        "[Instrument Society of America], October 1984).",
    ]))
    b.append(note("<b>Source notes.</b> (1) The OCR text layer contains many line-break "
                  "hyphenations («mech-», «lon-», «relo-», «turbu-»); the translation rejoins "
                  "them into whole words. The spaced «X Fz» is normalized to X_Fz and «P 1», "
                  "«P 2» to P1, P2. (2) The source prints «one sloop» (for «one step»); the "
                  "translation follows the intended meaning of single-step pressure reduction "
                  "and notes the typo. (3) Figure 15-2 carries «Courtesy of H. D. Baumann» and "
                  "Figure 15-5 «Photo courtesy of Jon Monsen»; the credits are kept in the "
                  "figure captions, which also state that the figures are simplified vector "
                  "redrawings rather than the original photographs. (4) The material-lifetime "
                  "table is reconstructed from four loose printed lines on page 103; the "
                  "values are unchanged. (5) Mathematical symbols in the source are presented "
                  "with Unicode notation in the translation."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chapter 15 occupies printed pp. 103-108 of the book (PDF pp. 106-111). The "
               "source consists of an opening passage, an explanation of the mechanism, a "
               "cavitation-avoidance section, four contributions by the author, an application "
               "pointer, a damage section, a material-lifetime table, five figures, two "
               "references and two additional-reading items, all of which are retained."))
    return "".join(b)
