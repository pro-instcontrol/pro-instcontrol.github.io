# -*- coding: utf-8 -*-
"""Book 6, Unit 14 — Pilot-Operated Pressure Relief Valves (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 213–226 (PDF pp. 227–240): direct-acting and indirect-acting pilot
valves, pilot types, main-valve construction, accessories, stable
operation, and the installation of pilot-operated relief valves
(Figures 5-35…5-44).
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig11 as F11

PAGES_SRC = 14         # source book pp. 213-226
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Pilot-Operated Pressure Relief Valves"
TITLE_VI = "Van an toàn xả điều khiển bằng pilot"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 14.</b> pilot-operated pressure relief "
                "valve — van an toàn xả điều khiển bằng pilot · main valve — "
                "van chính · pilot — bộ điều khiển pilot · direct-acting "
                "pilot — pilot tác động trực tiếp · indirect-acting pilot — "
                "pilot tác động gián tiếp · dome — buồng áp · pressure sense "
                "line — đường cảm áp · vent — đường thông hơi · flowing "
                "pilot — pilot chảy · non-flowing pilot — pilot không chảy · "
                "snap action — tác động bật · modulating action — tác động "
                "điều tiết · balanced / unbalanced pilot — pilot cân bằng / "
                "không cân bằng · full-bore valve — van đường kính đầy đủ · "
                "backflow preventer — van chống chảy ngược · unloader — van "
                "dỡ tải · blowdown — độ giảm áp đóng lại.")
    return ("<b>Key terms.</b> pilot-operated pressure relief valve · main "
            "valve · pilot · direct-acting pilot · indirect-acting pilot · "
            "dome · pressure sense line · vent · flowing pilot · non-flowing "
            "pilot · snap action · modulating action · balanced / unbalanced "
            "pilot · full-bore valve · backflow preventer · unloader · "
            "blowdown.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(items):
        b.append(ul([(i[0] if vi else i[1]) for i in items]))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ================================================================ review
    H("Tổng quan", "Review")
    P("Van an toàn xả điều khiển bằng pilot khác van tải lò xo ở chỗ chính "
      "lưu chất của hệ thống vừa là môi trường mở vừa là môi trường đóng. "
      "Van gồm van chính — bộ phận xả áp thực sự — và một pilot tự tác động "
      "điều khiển van chính theo áp suất vượt tăng hoặc giảm. ASME gọi loại "
      "có pilot tự tác động là pilot-operated pressure relief valve; van dùng "
      "nguồn năng lượng ngoài để mở là loại điều khiển bằng nguồn riêng.",
      "Pilot-operated pressure relief valves differ from direct mechanically "
      "loaded valves in that the system fluid is the medium for both opening "
      "and closing. They consist of a main valve — the actual pressure "
      "relief valve — and a self-actuated pilot that controls it as "
      "overpressure develops and recedes. The ASME calls the self-actuated "
      "form a pilot-operated pressure relief valve; a valve opened by an "
      "external power source is a power-operated relief valve.")
    P("Theo thời gian hình thành hai họ van. Họ có nguồn gốc Hoa Kỳ dùng "
      "pilot điều khiển trực tiếp ba đường: đường cảm áp, buồng áp của van "
      "chính và đường thông hơi; đây là pilot tác động trực tiếp. Họ gốc "
      "châu Âu dùng pilot là một van an toàn lò xo, điều khiển van chính "
      "bằng chính lưu chất xả ra; đây là pilot tác động gián tiếp (EN 1268-1).",
      "Two families evolved. The U.S. type uses a pilot that directly "
      "controls three passages: the pressure sense line, the main-valve dome "
      "and the vent; this is the direct-acting pilot. The European type uses "
      "a spring-loaded safety valve as pilot, controlling the main valve by "
      "the discharged fluid; this is the indirect-acting pilot "
      "(EN 1268-1).")

    # ======================================================= direct-acting pilot
    H("Pilot tác động trực tiếp", "Direct-acting pilot")
    P("Hình 5-35 cho thấy bố trí cơ bản. Piston là cơ cấu đóng của van chính "
      "và được pilot điều khiển. Khi áp hệ thống thấp hơn áp cài đặt, áp này "
      "tác động lên mặt trên của piston trong khi đường thông hơi vẫn đóng. "
      "Vì diện tích piston phía buồng áp lớn hơn diện tích béc, lực đóng "
      "tăng dần theo áp hệ thống. Đến áp cài đặt, pilot xì đủ áp buồng để "
      "áp dưới piston đẩy van mở; khi áp vượt giảm về áp đóng đã định, pilot "
      "đóng đường xì và đưa áp hệ thống trở lại để đóng van.",
      "Figure 5-35 shows the basic layout. The piston is the closing member "
      "of the main valve and is controlled by the pilot. Below set pressure, "
      "system pressure acts on top of the piston while the vent is closed. "
      "Because the piston area facing the dome exceeds the nozzle area, the "
      "closing force grows with system pressure. At set pressure the pilot "
      "vents enough dome pressure for the pressure under the piston to open "
      "the valve; as overpressure recedes to the predetermined closing "
      "pressure, the pilot closes the vent and reapplies system pressure in "
      "the closing direction.")
    FIG(35, F11.fig_vsh_5_35())

    H("Các loại pilot và kiểu tác động", "Pilot types and actions")
    U([("Pilot chảy cho lưu chất đi tiếp ra thông hơi trong suốt chu kỳ xả; "
        "pilot không chảy ngừng cấp lưu chất vào buồng áp khi cần xả, nên "
        "hạn chế tạp chất lọt vào cơ cấu pilot và thường được ưu tiên.",
        "Flowing pilots let system fluid continue bleeding to vent throughout "
        "the discharge cycle; non-flowing pilots stop the bleed into the dome "
        "when venting is required, reducing the chance of impurities entering "
        "the pilot. The non-flowing pilot is generally preferred."),
       ("Pilot bật-tắt đưa toàn áp hệ thống vào buồng áp cho đến áp cài đặt, "
        "rồi xì buồng để van mở bật hoàn toàn. Khi áp giảm về blowdown, pilot "
        "đưa áp trở lại và van đóng dứt khoát.",
        "On/off pilots admit full system pressure to the dome until set "
        "pressure, then vent it so the main valve pops fully open. When "
        "pressure falls to blowdown, the pilot reintroduces pressure and the "
        "valve drops closed."),
       ("Pilot điều tiết mở và đóng theo từng bước theo nhu cầu. Áp buồng "
        "bắt đầu giảm ở khoảng 95% áp cài đặt; van bắt đầu mở ở áp cài đặt "
        "và có thể mở hoàn toàn ở áp vượt khoảng 105%, rồi đóng ngược lại "
        "khi áp giảm.",
        "Modulating pilots open and close in increments with demand. Dome "
        "pressure begins to decay at about 95% of set pressure; the valve "
        "starts to open at set pressure and may be fully open at about 105% "
        "of set pressure, reversing as pressure recedes."),
       ("Pilot cân bằng có thể xì thẳng ra đầu ra của van chính nếu áp ngược "
        "không vượt áp vào. Pilot không cân bằng phải xì ra khí quyển tại "
        "pilot hoặc nơi an toàn khác; khi áp ngược có thể vượt áp vào, cần "
        "van chống chảy ngược.",
        "Balanced pilots may vent directly to the main-valve outlet as long "
        "as back pressure does not exceed inlet pressure. Unbalanced pilots "
        "must vent to atmosphere at the pilot or to a preferred location; "
        "where outlet pressure can exceed inlet pressure, a backflow "
        "preventer is required.")])

    # ============================================================ main valves
    H("Van chính: kiểu màng, kiểu piston và hướng dòng",
      "Main valves: diaphragm, piston and flow direction")
    P("Van chính thường được phân loại theo cơ cấu chuyển động: kiểu màng, "
      "kiểu ống màng hoặc kiểu piston. Van kiểu màng chỉ dùng cho dịch vụ áp "
      "thấp (Hình 5-37, 5-38); nếu bình xả có thể phát sinh chân không ngoài "
      "dự kiến, màng sẽ nhấc khỏi chỗ kín và bảo vệ bình khỏi bị ép sụp. "
      "Hình 5-39 là ví dụ van chính piston với pilot cân bằng, dùng cho khí, "
      "chất lỏng và lưu chất hai pha.",
      "Main valves are classified by moving member as diaphragm, bellows or "
      "piston types. Diaphragm-type main valves are used only on low-pressure "
      "service (Figures 5-37, 5-38); if unwanted vacuum develops in the "
      "discharge vessel, the diaphragm lifts and protects the vessel from "
      "collapse. Figure 5-39 shows a piston-type main valve with a balanced "
      "pilot for gas, liquid and two-phase fluids.")
    FIG(37, F11.fig_vsh_5_37())
    FIG(38, F11.fig_vsh_5_38())
    FIG(39, F11.fig_vsh_5_39())
    P("Thường lưu chất tác động lên mặt dưới cơ cấu đóng như Hình 5-35. "
      "Hình 5-41 đảo chiều dòng qua van chính, đưa piston và ống dẫn nằm trong "
      "vùng áp của van. Khi đó piston và ống dẫn ở nhiệt độ lưu chất nên không "
      "chịu sốc nhiệt lúc van mở, và hạt rắn theo dòng không va trực tiếp "
      "vào bề mặt làm kín. Giảm chấn tích hợp khống chế gia tốc và giảm tốc "
      "của piston để hạn chế sốc cơ học cho van và đường ống.",
      "Normally flow acts on the underside of the closure member as in "
      "Figure 5-35. Figure 5-41 reverses the flow through the main valve so "
      "the piston and guide lie in the pressure zone. They then remain at "
      "fluid temperature and avoid thermal shock on opening, while solids in "
      "the discharge do not strike the seating surface directly. Built-in "
      "dampers control piston acceleration and deceleration to limit "
      "mechanical shock to the valve and piping.")
    FIG(41, F11.fig_vsh_5_41())

    H("Van thép mặt bích tiêu chuẩn và van đường kính đầy đủ",
      "Standard and full-bore flanged steel main valves")
    P("API 526, vốn quy định đầu nối, cỡ béc và giới hạn áp/nhiệt cho van "
      "an toàn lò xo thép mặt bích, đã được mở rộng sang cả van điều khiển "
      "bằng pilot. Tuy nhiên nhiều nhà sản xuất Hoa Kỳ vẫn cung cấp van "
      "ngoài tiêu chuẩn gọi là full-bore: cỡ béc tiệm cận đường kính lòng "
      "ống vào (Hình 5-36). Một số thân van chứa được nhiều cỡ béc nhờ "
      "bulông chỉnh hành trình piston; các cỡ béc theo API 526 từ D đến T. "
      "Piston có vòng cản áp để dập dao động nhanh do cộng hưởng giữa cụm "
      "van và đường ống vào.",
      "API 526, covering end connections, nozzle sizes and pressure/temperature "
      "limits for flanged steel spring-loaded relief valves, has been "
      "extended to pilot-operated valves. Many U.S. makers nevertheless offer "
      "non-standard full-bore valves whose nozzle approaches the inlet pipe "
      "bore (Figure 5-36). Some bodies accept several orifice sizes by "
      "adjusting piston stroke with an adjustable length bolt; API 526 sizes "
      "D through T are covered. The piston carries a pressure-actuated drag "
      "ring to suppress rapid oscillation from resonant reinforcement of the "
      "assembly and inlet piping.")
    FIG(36, F11.fig_vsh_5_36())
    P("Hình 5-40 và 5-41 minh họa các van pilot không chảy tác động bật dùng "
      "chủ yếu cho khí, đặc biệt hơi, kể cả dịch vụ nặng có bụi bẩn, hydrat "
      "và độ ẩm cao. Hình 5-40 nêu dải áp cài đặt từ 25 đến trên 6000 psig "
      "(1,7 đến trên 400 barg) và nhiệt độ làm việc liên tục từ −253 °C đến "
      "260 °C. Hình 5-41 nêu áp cài đặt tối đa 1200 psig (82,8 barg), nhiệt "
      "độ tối đa 538 °C, blowdown chỉnh được, điều khiển từ xa và tùy chọn "
      "hai pilot có bộ chọn tích hợp.",
      "Figures 5-40 and 5-41 illustrate non-flowing snap-action pilots used "
      "mainly for gas, especially steam, including severe service with dirt, "
      "hydrates and high moisture. Figure 5-40 quotes set pressures from 25 "
      "to over 6000 psig (1.7 to over 400 barg) and continuous service "
      "temperatures from −253 °C to 260 °C. Figure 5-41 gives a maximum set "
      "pressure of 1200 psig (82.8 barg), maximum temperature 538 °C, "
      "adjustable blowdown, remote actuation and a dual-pilot option with an "
      "integral selector.")
    FIG(40, F11.fig_vsh_5_40())

    # =============================================================== accessories
    H("Phụ kiện", "Accessories")
    U([("Đầu nối thử tại hiện trường để kiểm tra áp cài đặt khi đang chạy.",
        "Field test connection for in-service verification of set pressure."),
       ("Chỉ thị thử tại hiện trường, chỉ dùng được với pilot kiểu điều tiết.",
        "Field test indicator for in-service verification of set pressure on "
        "modulating pilots only."),
       ("Van chống chảy ngược về phía vào nếu áp đầu ra vượt áp đầu vào.",
        "Backflow preventer to stop accidental reverse flow if outlet "
        "pressure exceeds inlet pressure."),
       ("Bộ lọc cấp cho pilot, đặc biệt cần với pilot điều tiết kiểu chảy ở "
        "dịch vụ lỏng.",
        "Pilot supply filter, especially appropriate with flowing modulating "
        "pilots in liquid service."),
       ("Bộ giảm xung áp để làm dịu xung áp sau máy nén piston.",
        "Pressure spike snubber to attenuate pressure spikes downstream of "
        "reciprocating compressors."),
       ("Van dỡ tải tay hoặc từ xa để mở van chính và giảm áp hệ thống.",
        "Manual or remote unloader to open the main valve and depressurize "
        "the system."),
       ("Cần nâng pilot để thử tác động bằng tay; cần này không dùng để kiểm "
        "tra áp cài đặt.",
        "Pilot lift lever for manual testing of valve operation; it does not "
        "permit checking set pressure."),
       ("Tùy vật liệu NACE MR0175 cho dịch vụ khí chua, áp dụng cho cả pilot "
        "lẫn van chính.",
        "NACE material option for sour gas service to MR0175, for both pilot "
        "and main valve.")])

    # ======================================================== stable operation
    H("Vận hành ổn định với pilot bật-tắt",
      "Stable operation with on/off pilots")
    P("Tổn thất áp trên đoạn ống vào giữa điểm lấy áp tích hợp và nguồn "
      "phải nhỏ hơn blowdown của pilot. Nếu không, van sẽ đóng rồi mở lại "
      "liên tục cho đến khi tự phá hủy hoặc áp hệ thống tăng đủ để dừng "
      "chu kỳ. Nên để blowdown lớn hơn ít nhất 2% so với tổn thất áp trên "
      "đoạn ống trước điểm cảm áp. Pilot điều tiết tránh được chu kỳ này.",
      "The pressure loss in the inlet pipe between the integral sense "
      "pick-up and the source must be less than pilot blowdown. Otherwise the "
      "valve recloses and reopens rapidly until it destroys itself or system "
      "pressure rises enough to stop cycling. Blowdown should be at least 2% "
      "greater than the inlet-pipe loss upstream of the sense point. "
      "Modulating pilots overcome this potential for cycling.")
    P("Đường cảm áp từ xa dài theo khoảng cách giữa van và điểm cảm áp, phải "
      "bố trí không để hơi ngưng tụ làm tắc đường dẫn. Với pilot không chảy đã "
      "ghi nhận đường dài 200 ft (60 m), dùng ống DN 25 theo code đường ống "
      "áp dụng. Với hơi và dịch vụ dễ ngưng tụ, nên đặt van gần nguồn áp "
      "nhất. Nếu piston không được giảm chấn, chỉ một cút ống hoặc trở lực "
      "tương đương cũng gây rung chatter. Với van full-bore, giữ L/D đường "
      "vào không quá 5 và đầu vào bo tròn tốt; khi cần ống dài, tăng một cỡ "
      "ống và dùng giảm tâm trước van.",
      "Remote sense-line length follows the distance from valve to sensing "
      "point, but the line must be routed so condensate cannot block the "
      "passage. Non-flowing pilots have been reported with 200 ft (60 m) "
      "lines using DN 25 piping to the applicable code. For steam and other "
      "condensing services the valve should be as close to the pressure "
      "source as possible. An undamped main piston can chatter from a single "
      "elbow or equivalent restriction. Full-bore valves may be stabilized "
      "with an inlet L/D of 5 and a well-rounded entry; for longer runs, use "
      "one larger pipe size with a concentric reducer below the valve.")
    P("Trong trường hợp lắp đặt không lý tưởng, ma sát chuyển động của piston "
      "có thể dập hoàn toàn dao động cộng hưởng; Hình 5-36 dùng thiết bị cản "
      "áp giữa piston và xi lanh để đạt hiệu quả này.",
      "In less than ideal installations, frictional resistance to piston "
      "movement can completely suppress resonant chatter; Figure 5-36 uses "
      "a pressure-activated drag device between piston and cylinder.")

    H("Vận hành ổn định với pilot điều tiết và giới hạn dịch vụ",
      "Stable operation with modulating pilots and service limits")
    U([("Pilot điều tiết chịu điều kiện lắp đặt xấu hơn pilot bật-tắt vì van "
        "mở tỉ lệ theo nhu cầu.",
        "Modulating pilots tolerate unfavorable installation better than "
        "on/off pilots because the valve opens in proportion to demand."),
       ("Pilot kiểu chảy không ưu tiên trừ khi môi trường tương đối sạch; "
        "được ưa dùng cho hơi vì làm pilot ấm dần bên trong, tránh ngưng tụ "
        "hơi đột ngột gây mất ổn định.",
        "Flowing pilots are not preferred unless the medium is relatively "
        "clean, but suit steam because internal warm-up prevents sudden "
        "condensation and erratic action."),
       ("Pilot không chảy nói chung được ưu tiên.",
        "The non-flowing pilot is generally preferred."),
       ("Tác động bật được ưu tiên khi tốc độ tăng áp cao hoặc lưu chất có "
        "thể tạo chất rắn sau khi giãn nở làm tắc header xả, ví dụ CO₂ tạo "
        "đá khô.",
        "Pop action is preferred for high rates of pressure rise or when "
        "expansion can form solids that plug the discharge header, such as "
        "CO₂ dry ice."),
       ("Điều tiết được ưu tiên khi lưu lượng xả thay đổi lớn, ở dịch vụ "
        "lỏng, khi van quá lớn hoặc hơi nhỏ do đánh giá thấp tổn thất áp "
        "vào, hoặc khi trạng thái pha có thể thay đổi.",
        "Modulating action is preferred when required capacity varies "
        "greatly, in liquid service, for oversized or modestly undersized "
        "valves, or when process phase can vary."),
       ("Tham vấn nhà chế tạo nếu lưu chất có hạt rắn lơ lửng hoặc có thể "
        "đông đặc/ngưng tụ ở nhiệt độ môi trường.",
        "Consult the manufacturer if the fluid carries suspended solids or "
        "can freeze or condense at ambient temperature."),
       ("Không dùng van điều khiển bằng pilot cho dịch vụ mài mòn hoặc nhớt "
        "trên 5000 SSU, cũng như dịch vụ có thể kết cốc, trùng hợp hoặc ăn "
        "mòn bộ phận ướt, trừ khi van được thiết kế riêng với lưu chất sạch "
        "bảo vệ cơ cấu bên trong.",
        "Do not use pilot-operated valves in abrasive or viscous services "
        "above 5000 SSU, or where coking, polymerization or corrosion of "
        "wetted parts can occur, unless specially designed with a clean "
        "external medium protecting the critical internals.")])

    # ====================================================== indirect-acting pilot
    H("Pilot tác động gián tiếp", "Indirect-acting pilots")
    P("Có hai dạng chính: van chính mở khi mất điện (deenergize-to-open) và "
      "van chính mở khi có điện (energize-to-open). Hình 5-42 gồm van chính "
      "và pilot lò xo thiết kế cho hơi. Khi pilot mở do áp vượt tăng, lưu "
      "chất xả tác động lên van một chiều, van này mở đường thông buồng áp "
      "của van chính. Áp hệ thống trên diện tích không cân bằng của piston "
      "làm van chính mở. Trong thời gian van mở vẫn có một dòng xì nhỏ liên "
      "tục vào buồng áp. Khi áp giảm, pilot đóng, van một chiều trở về và "
      "đóng đường thông; dòng xì nay đóng van. Hình 5-42 cũng có côn đục lỗ "
      "ở đầu ra làm bộ giảm thanh khuếch tán.",
      "Two principal forms exist: main valves that open when deenergized and "
      "those that open when energized. Figure 5-42 shows a main valve and a "
      "spring-loaded pilot designed for steam. As the pilot opens on rising "
      "overpressure, its discharge acts on a check valve that vents the main "
      "valve dome. System pressure on the unbalanced piston area opens the "
      "main valve, while a small continuous bleed enters the dome. When "
      "overpressure recedes the pilot closes, the check valve recloses the "
      "dome vent, and the bleed closes the main valve. A perforated cone in "
      "the outlet acts as a diffuser-type silencer.")
    FIG(42, F11.fig_vsh_5_42())
    P("Hình 5-43 là sơ đồ lắp đặt điển hình với ba đường điều khiển: hai "
      "pilot tác động gián tiếp như Hình 5-42 và một van solenoid. Van cô lập "
      "ở hai đầu mỗi pilot và van solenoid được liên khóa để chỉ cô lập được "
      "một đường tại một thời điểm, phục vụ kiểm tra và bảo trì. Số đường "
      "điều khiển do người dùng hoặc code thực hành quy định.",
      "Figure 5-43 shows a typical installation with three control lines: two "
      "indirect-acting pilots as in Figure 5-42 and one solenoid control "
      "valve. Isolation valves on each side of the pilots and solenoid are "
      "interlocked so that one line at a time can be isolated for inspection "
      "and maintenance. The number of control lines is chosen by the user or "
      "required by the code of practice.")
    FIG(43, F11.fig_vsh_5_43())
    P("Van chính ở Hình 5-44 mở khi có điện. Cơ cấu đóng là thân dạng trụ "
      "di chuyển trên piston trung tâm; pilot là van an toàn lò xo kín bằng "
      "ống màng, có thể có tải bổ sung và hỗ trợ nâng bằng solenoid. Khi áp "
      "đạt cài đặt, pilot mở và đưa áp hệ thống qua ống trung tâm lên mặt "
      "trên piston, áp tích tụ làm van mở, với một phần áp xì qua lỗ nhỏ ra "
      "đầu ra. Khi áp giảm về blowdown, pilot đóng, áp trên piston xì ra đầu "
      "ra và lò xo phía trên trợ giúp đóng nhanh. Ở cả hai dạng pilot gián "
      "tiếp, cơ cấu đóng nằm trong vùng áp hệ thống nên không chịu sốc nhiệt "
      "và hạt rắn không va trực tiếp vào bề mặt làm kín; hai dạng này được "
      "dùng rộng rãi trong nhà máy nhiệt điện và nhà máy điện hạt nhân.",
      "The main valve in Figure 5-44 opens when energized. Its closure member "
      "is a cylinder-shaped vessel moving on a central piston; the pilot is "
      "a bellows-sealed direct spring-loaded relief valve that may have "
      "supplementary loading and solenoid-assisted lift. At set pressure the "
      "pilot opens and admits system pressure through a central tube to the "
      "top of the piston; pressure build-up opens the valve while a small "
      "hole bleeds to the outlet. At blowdown the pilot closes, pressure "
      "above the piston bleeds to outlet, and a spring assists sudden "
      "closure. In both indirect forms the closure member lies in the system "
      "pressure zone, avoiding thermal shock and direct solids impact on "
      "seating faces; both are widely used in conventional and nuclear power "
      "stations.")
    FIG(44, F11.fig_vsh_5_44())

    # ================================================================== table
    H("Bảng tóm tắt các thiết kế trong đơn vị", "Designs in this unit")
    b.append(table(
        ["Hình / chủ đề", "Thiết kế", "Đặc điểm chính"]
        if vi else ["Figure / topic", "Design", "Key feature"],
        [
            ["5-35", "Pilot tác động trực tiếp" if vi else "Direct-acting pilot",
             "Điều khiển cảm áp, buồng áp, thông hơi"
             if vi else "Senses, controls dome and vent"],
            ["5-36", "Van full-bore" if vi else "Full-bore main valve",
             "Bulông chỉnh hành trình, vòng cản áp"
             if vi else "Stroke bolt, pressure-actuated drag ring"],
            ["5-37", "Màng, pilot chảy" if vi else "Diaphragm, flowing pilot",
             "Bật hoặc điều tiết, áp hoặc chân không"
             if vi else "Snap or modulating, pressure or vacuum"],
            ["5-38", "Màng, pilot không chảy cân bằng"
             if vi else "Diaphragm, balanced non-flowing pilot",
             "Điều tiết, khí áp thấp" if vi else "Modulating, low-pressure gas"],
            ["5-39", "Piston, pilot cân bằng" if vi else "Piston, balanced pilot",
             "Khí, lỏng, hai pha" if vi else "Gas, liquid, two-phase"],
            ["5-40", "Pilot bật chịu hơi bẩn" if vi else "Snap pilot for dirty steam",
             "1,7 đến trên 400 barg, −253…260 °C"
             if vi else "1.7 to over 400 barg, −253…260 °C"],
            ["5-41", "Dòng đảo, piston trong vùng áp"
             if vi else "Reversed flow, piston in pressure zone",
             "Giảm chấn, điều khiển từ xa, hai pilot"
             if vi else "Damper, remote and dual-pilot options"],
            ["5-42", "Mở khi mất điện" if vi else "Deenergize-to-open",
             "Van một chiều, pilot xả, giảm thanh"
             if vi else "Check valve, discharging pilot, silencer"],
            ["5-43", "Ba đường điều khiển" if vi else "Three control lines",
             "Hai pilot gián tiếp, một solenoid, liên khóa"
             if vi else "Two indirect pilots, one solenoid, interlocked"],
            ["5-44", "Mở khi có điện" if vi else "Energize-to-open",
             "Pilot ống màng, piston trung tâm, xì ra đầu ra"
             if vi else "Bellows pilot, central piston, outlet bleed"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 213–226, "
                 "Hình 5-35…5-44." if vi else
                 "Summary from source text, book pp. 213–226, "
                 "Figures 5-35…5-44."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
