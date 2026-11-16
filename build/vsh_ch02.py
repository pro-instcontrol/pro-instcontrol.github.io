# -*- coding: utf-8 -*-
"""Book 6, Unit 2 — Fundamentals I: Fluid Tightness of Valves and the Sealing
Mechanism (EN/VI bilingual).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 7–12 (PDF pp. 21–26): valve seals, leakage criterion (four classes, Lok
steam/atom criteria, JPL zero-leakage definition, Figure 2-1), proving fluid
tightness, sealability against liquids (Figure 2-2, Equation 2-1), against
gases, and the mechanism for closing leakage passages.
"""

from vsh_common import (eq, fig, h2, h3, note, p, table, ul)
import vshfig as F

PAGES_SRC = 6           # source book pp. 7-12
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Fundamentals I — Fluid Tightness and the Sealing Mechanism"
TITLE_VI = "Cơ sở I — Độ kín chất lỏng và cơ chế làm kín"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 2.</b> fluid tightness — độ kín chất lỏng · "
                "leakage criterion — tiêu chuẩn rò rỉ cho phép · leakage capillary "
                "— mao dẫn rò rỉ (kênh rò vi mô giữa hai bề mặt) · leakage rate — "
                "tốc độ rò rỉ · steam class / atom class — cấp hơi / cấp nguyên tử "
                "(phân cấp độ kín của Lok) · zero leakage — rò rỉ bằng không · "
                "sccs — standard cubic centimeters per second · contact angle — "
                "góc tiếp xúc · surface tension — sức căng bề mặt · waviness / "
                "roughness — độ gợn / độ nhám bề mặt · yield strain — biến dạng "
                "dẻo giới hạn · sealant — chất làm kín bôi trơn.")
    return ("<b>Key terms.</b> fluid tightness · leakage criterion · leakage "
            "capillary · leakage rate · steam class / atom class (Lok) · zero "
            "leakage · sccs · contact angle · surface tension · waviness / "
            "roughness · yield strain · sealant · search gas.")


def _t_classes(lang):
    hdr = (["Cấp độ kín", "Áp dụng cho", "Tiêu chuẩn rò rỉ"] if lang == "vi"
           else ["Tightness class", "Applies to", "Leakage criterion"])
    rows = [
        ("Nominal leakage (rò rỉ danh nghĩa)",
         "Chỗ kín seat của van không cần đóng kín — thông dụng khi khống chế "
         "lưu lượng" if lang == "vi" else
         "Valve seats not required to shut off tightly — typical for flow-rate "
         "control",
         "—"),
        ("Low leakage (rò rỉ thấp)",
         "Như trên, mức kín cao hơn" if lang == "vi" else "As above, tighter",
         "—"),
        ("Steam class (cấp hơi)",
         "Chỗ kín seat, trục van và mối ghép thân của van dùng cho hơi và đa "
         "số ứng dụng công nghiệp" if lang == "vi" else
         "Seat, stem and body-joint seals of valves for steam and most other "
         "industrial applications",
         "Khí: 10–100 µg/s mỗi mét chiều dài chỗ kín; chất lỏng: 0.1–1.0 µg/s "
         "mỗi mét" if lang == "vi" else
         "Gas: 10–100 µg/s per m seal length; liquid: 0.1–1.0 µg/s per m"),
        ("Atom class (cấp nguyên tử)",
         "Độ kín cực cao — tàu vũ trụ, nhà máy điện hạt nhân" if lang == "vi"
         else "Extremely high tightness — spacecraft, atomic power plant "
              "installations",
         "Khí: 10<sup>-3</sup>–10<sup>-5</sup> µg/s mỗi mét; tại Hoa Kỳ thường "
         "gọi là <i>zero leakage</i>" if lang == "vi" else
         "Gas: 10<sup>-3</sup>–10<sup>-5</sup> µg/s per m; in the U.S. "
         "commonly called <i>zero leakage</i>"),
    ]
    cap = ("Bốn cấp độ kín chất lỏng của van; tiêu chuẩn cấp hơi/nguyên tử theo "
           "đề xuất của Lok (tr. 8)." if lang == "vi" else
           "The four classes of valve fluid tightness; steam/atom-class criteria "
           "after Lok's proposal (p. 8).")
    return table(hdr, rows, caption=cap, cls="tbl wide")


# ---------------------------------------------------------------------------
def body_vi():
    b = []
    b.append(p("Cơ sở của một kiểu van nằm ở <b>đặc tính làm kín</b> của nó: kín "
               "chỗ seat trong đường ống khi đóng, và — khi áp dụng — kín trục van "
               "để không cho rò rỉ ra khí quyển. Với hệ thống quá trình chứa chất "
               "lỏng nguy hại (độc hại cho cả khí quyển lẫn con người), <b>chỗ kín "
               "trục van</b> được coi là quan trọng hơn."))

    b.append(h2("Chỗ kín của van", "Valve seals"))
    b.append(p("Một trong các nhiệm vụ của đa số van là tạo <b>chỗ kín chất lỏng</b> "
               "giữa seat và phần đóng. Nếu phần đóng được dẫn động bằng trục xuyên "
               "từ ngoài vào hệ thống chịu áp, cần thêm một chỗ kín quanh trục. "
               "Chỗ kín cũng phải có giữa các cấu kiện thân van chịu áp. Nếu rò rỉ "
               "ra khí quyển không thể chấp nhận, các chỗ kín thân/trục này có thể "
               "quan trọng hơn cả chỗ kín seat — vì vậy kết cấu chỗ kín ảnh hưởng "
               "lớn tới lựa chọn van."))

    b.append(h2("Tiêu chuẩn rò rỉ", "Leakage criterion"))
    b.append(p("Một chỗ kín được coi là <b>kín</b> nếu rò rỉ không bị nhận ra, hoặc "
               "lượng rò rỉ nhận ra là cho phép. Lượng rò rỉ tối đa cho phép của "
               "ứng dụng gọi là <b>tiêu chuẩn rò rỉ</b> (leakage criterion). Độ kín "
               "có thể diễn đạt bằng thời gian để một khối lượng/thể tích chất lỏng "
               "đi qua các mao dẫn rò rỉ, hoặc thời gian để áp suất hệ thống biến "
               "thiên một lượng cho trước; thực tế thường dùng nghịch đảo của chúng "
               "— <b>tốc độ rò rỉ</b> hoặc tốc độ biến đổi áp suất."))
    b.append(_t_classes("vi"))
    b.append(p("Ở cấp nguyên tử, báo cáo kỹ thuật của <b>Jet Propulsion "
               "Laboratory</b> (Viện Công nghệ California) định nghĩa rò rỉ bằng "
               "không cho tàu vũ trụ như sau: rò rỉ bằng không tồn tại khi <b>sức "
               "căng bề mặt ngăn chất lỏng đi vào các mao dẫn rò rỉ</b>. Còn rò rỉ "
               "khí bằng không thì không tồn tại. Hình 2-1 là một đường cong tùy "
               "nghi được dựng làm tiêu chuẩn rò rỉ khí bằng không."))
    b.append(fig(2, F.fig_vsh_2_1()))

    b.append(h2("Chứng minh độ kín", "Proving fluid tightness"))
    b.append(p("Đa số van làm việc ở mức <b>cấp hơi</b> là đủ. Thử chứng minh thường "
               "dùng nước, khí nén hoặc khí trơ, áp cho thân van, seat, và tùy kết "
               "cấu, cả mặt làm kín ngược (back seat) của hộp gioăng — nhưng thường "
               "<i>không</i> gồm chính chỗ kín hộp gioăng. Thử bằng nước: đo thể "
               "ích/thời gian hoặc số giọt/thời gian. Thử khí: dẫn khí rò qua nước "
               "hoặc chất tạo bọt chuyên dụng rồi đếm bong bóng theo thời gian — "
               "cách này đo được tới <b>1×10<sup>-2</sup> hoặc 1×10<sup>-4</sup> "
               "sccs</b> tùy tay nghề người thao tác. Rò rỉ cấp nguyên tử thấp hơn "
               "phải dùng <b>khí dò (search gas)</b> kết hợp đầu dò khí dò. Quy cách "
               "chứng minh độ kín có trong các tiêu chuẩn van (Phụ lục C); phương "
               "pháp thử cấp nguyên tử mô tả trong BS 3636."))

    b.append(h2("Cơ chế làm kín", "Sealing mechanism"))
    b.append(h3("Kín với chất lỏng", "Sealability against liquids"))
    b.append(p("Khả năng kín với chất lỏng do <b>sức căng bề mặt</b> và <b>độ nhớt</b> "
               "của chất lỏng quyết định. Khi mao dẫn rò rỉ đang chứa khí, sức căng "
               "bề mặt có thể hút chất lỏng vào mao dẫn hoặc đẩy chất lỏng ra, tùy "
               "<b>góc tiếp xúc</b> giữa chất lỏng và thành mao dẫn — thước đo mức "
               "ướt của bề mặt rắn, tức tỷ lệ tương đối giữa lực hút của thành mao "
               "dẫn lên phân tử chất lỏng và lực hút giữa các phân tử chất lỏng với "
               "nhau. Hai lực đối trọng cân bằng khi:"))
    b.append(eq("πr²·ΔP = 2πrT·cosθ   ⟺   ΔP = 2T·cosθ/r", "2-1"))
    b.append(p("với r là bán kính mao dẫn, ΔP là áp suất mao dẫn, T là sức căng "
               "bề mặt, θ là góc tiếp xúc giữa rắn và chất lỏng. Nếu góc tiếp xúc "
               "<b>lớn hơn 90°</b>, sức căng bề mặt có thể chặn dòng rò rỉ; nếu "
               "<b>nhỏ hơn 90°</b>, chất lỏng bị hút vào mao dẫn và dòng rò bắt đầu "
               "ở áp suất thấp."))
    b.append(fig(3, F.fig_vsh_2_2()))
    b.append(p("Xu hướng bề mặt kim loại tạo góc tiếp xúc lớn hơn 90° phụ thuộc vào "
               "lớp <b>màng dầu/mỡ/sáp</b> thường bao bọc bề mặt kim loại. Khi lớp "
               "này bị dung môi rửa trôi, tính chất bề mặt thay đổi: chất lỏng vốn "
               "bị đẩy ra bỗng làm ướt bề mặt. Ví dụ kinh điển: <b>kerosene</b> "
               "hoá tan màng mỡ — van vốn kín nước có thể rò rỉ nặng sau khi chỗ "
               "kín bị rửa bằng kerosene; lau lại bề mặt bằng khăn thường đã đủ "
               "phục hồi màng mỡ, tức độ kín nước ban đầu."))
    b.append(p("Khi các mao dẫn rò rỉ đã bị <b>ngập đầy</b> chất lỏng, áp suất mao "
               "dẫn triệt tiêu — trừ khi bọt khí theo dòng phá cột chất lỏng. Nếu "
               "mao dẫn lớn và số Reynolds vượt giá trị tới hạn, dòng rò là <b>rối</b>; "
               "khi mao dẫn nhỏ dần và Reynolds xuống dưới giá trị tới hạn, dòng rò "
               "thành <b>tầng</b> — theo phương trình Poiseuille, dòng rò tỉ lệ "
               "nghịch với độ nhớt và chiều dài mao dẫn, tỉ lệ thuận với lực đẩy và "
               "đường kính mao dẫn. Với độ nhớt cao và mao dẫn nhỏ, dòng rò nhỏ "
               "đến mức không đo được."))
    b.append(h3("Kín với khí", "Sealability against gases"))
    b.append(p("Khả năng kín với khí do <b>độ nhớt của khí và kích thước phân tử "
               "khí</b> quyết định. Dòng rò cũng chuyển từ rối sang tầng khi mao "
               "dẫn nhỏ dần (Poiseuille). Khi đường kính mao dẫn xuống cùng cỡ với "
               "<b>đường đi tự do trung bình của phân tử khí</b>, dòng chảy mất bản "
               "chất khối và thành <b>khuyếch tán</b> — các phân tử khí đi qua mao "
               "dẫn bằng chuyển động nhiệt ngẫu nhiên. Mao dẫn có thể nhỏ dưới cả "
               "kích thước phân tử, nhưng dòng chảy cũng không dừng hẳn — khí được "
               "biết là khuyếch tán xuyên được cả thành kim loại rắn."))
    b.append(h3("Cơ chế đóng các kênh rò rỉ", "Mechanism for closing leakage "
                "passages"))
    b.append(p("Bề mặt gia công có hai thành phần kết cấu: <b>độ gợn</b> (waviness) "
               "— khoảng cách giữa các đỉnh tương đối rộng — và <b>độ nhám</b> "
               "(roughness) — các gờ nhỏ chồng lên nền gợn. Dù hoàn thiện đến mức "
               "độ nhám nào, các gờ này vẫn lớn hơn nhiều so với kích thước phân tử. "
               "Nếu vật liệu một trong hai bề mặt có <b>biến dạng dẻo giới hạn</b> "
               "đủ cao, các kênh rò do gờ bề mặt tạo ra có thể được đóng bằng biến "
               "dạng đàn hồi thuần túy — <b>cao su</b>, với biến dạng giới hạn lớn "
               "hơn thép các-bon thấp khoảng 1 000 lần, làm kín mà không vượt giới "
               "hạn đàn hồi. Đa số vật liệu khác có biến dạng đàn hồi thấp hơn "
               "nhiều, nên phải <b>vượt giới hạn đàn hồi</b> mới đóng được kênh rò."))
    b.append(p("Nếu cả hai bề mặt đều kim loại, thoạt đầu chỉ các <b>đỉnh</b> gờ "
               "chạm nhau và tải nhỏ đã đủ để biến dạng dẻo các đỉnh. Khi diện tích "
               "tiếp xúc thực tăng, biến dạng chuyển sang dẻo–đàn hồi. Khi các khe "
               "hở do độ gợn đã đóng, chỉ còn <b>độ nhám trong đáy thung lũng</b>; "
               "để đóng các kênh còn lại cần tải rất lớn, có thể làm biến dạng dẻo "
               "nặng vật liệu bên dưới. Tuy nhiên, tiếp xúc mật độ giữa hai bề mặt "
               "chỉ cần kéo dài dọc <b>một đường hoặc dải liên tục</b> để tạo chỗ "
               "kín; các gờ <b>hướng xuyên tâm</b> thì khó hoặc không thể làm kín."))

    b.append(note("Ý chính: độ kín không phải trạng thái có/không mà là một "
                  "<b>tiêu chuẩn rò rỉ</b> chọn theo ứng dụng — van khống chế lưu "
                  "lượng chấp nhận rò rỉ danh nghĩa, còn tàu vũ trụ đòi hỏi cấp "
                  "nguyên tử. Với chất lỏng, cửa ngõ của dòng rò là <b>góc tiếp "
                  "xúc</b> và sức căng bề mặt (Phương trình 2-1): một màng mỡ mỏng "
                  "quyết định van có kín nước hay không, và kerosene có thể phá "
                  "nó. Với khí, khi mao dẫn nhỏ cỡ phân tử, dòng rò thành khuyếch "
                  "tán và chỉ có thể chặn bằng tiếp xúc kim loại–kim loại biến "
                  "dạng dẻo dọc một dải liên tục."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. "
               "Nội dung gốc © 2004 Elsevier Inc. (Gulf Professional "
               "Publishing).</i>"))
    return "".join(b)


# ---------------------------------------------------------------------------
def body_en():
    b = []
    b.append(p("The fundamentals of a particular type of valve relate to its "
               "<b>sealing characteristics</b>: in-line seat sealing when closed "
               "and, where applicable, stem sealing which should prevent potential "
               "leaks into the atmosphere. For process systems handling hazardous "
               "fluids — harmful to both the atmosphere and personnel — stem "
               "sealing is considered to be of more importance."))

    b.append(h2("Valve seals", "Chỗ kín của van"))
    b.append(p("One of the duties of most valves is to provide a fluid seal "
               "between the seat and the closure member. If the closure member is "
               "moved by a stem that penetrates into the pressure system from the "
               "outside, another fluid seal must be provided around the stem. "
               "Seals must also be provided between the pressure-retaining valve "
               "components. If the escape of fluid into the atmosphere cannot be "
               "tolerated, the latter seals can assume a higher importance than "
               "the seat seal — so the construction of the valve seals can greatly "
               "influence the selection of valves."))

    b.append(h2("Leakage criterion", "Tiêu chuẩn rò rỉ"))
    b.append(p("A seal is <b>fluid-tight</b> if the leakage is not noticed, or if "
               "the amount of noticed leakage is permissible. The maximum "
               "permissible leakage for the application is known as the "
               "<b>leakage criterion</b>. Fluid tightness may be expressed either "
               "as the time taken for a given mass or volume of fluid to pass "
               "through the leakage capillaries, or as the time taken for a given "
               "pressure change in the fluid system; in practice its reciprocals "
               "are used — the <b>leakage rate</b> or the rate of pressure change."))
    b.append(_t_classes("en"))
    b.append(p("For the atom class, a technical report of the <b>Jet Propulsion "
               "Laboratory</b>, California Institute of Technology, defines zero "
               "leakage for spacecraft requirements: zero leakage exists if "
               "<b>surface tension prevents the entry of liquid into the leakage "
               "capillaries</b>. Zero <i>gas</i> leakage as such does not exist. "
               "Figure 2-1 shows an arbitrary curve constructed for use as a "
               "specification standard for zero gas leakage."))
    b.append(fig(2, F.fig_vsh_2_1()))

    b.append(h2("Proving fluid tightness", "Chứng minh độ kín"))
    b.append(p("Most valves are intended for duties for which <b>steam-class</b> "
               "fluid tightness is satisfactory. The proving tests are normally "
               "carried out with water, air, or inert gas, and are applied to the "
               "valve body and the seat and — depending on the construction — also "
               "to the stuffing-box back seat, but they frequently <i>exclude</i> "
               "the stuffing-box seal itself. With water, the leakage rate is "
               "metered as volume-per-time or liquid droplets-per-time. Gas "
               "leakage may be metered by conducting the leaking gas through water "
               "or a bubble-forming leak-detector agent and counting bubbles per "
               "time unit — permitting metering down to <b>1×10<sup>-2</sup> or "
               "1×10<sup>-4</sup> sccs</b> (standard cubic centimeters per second), "
               "depending on the skill of the operator. Lower, atom-class leakage "
               "rates are detected using a <b>search gas</b> with a search-gas "
               "detector. Specifications for proving leakage tightness may be "
               "found in the valve standards of Appendix C; atom-class testing "
               "methods are described in BS 3636."))

    b.append(h2("Sealing mechanism", "Cơ chế làm kín"))
    b.append(h3("Sealability against liquids", "Kín với chất lỏng"))
    b.append(p("Sealability against liquids is determined by the <b>surface "
               "tension</b> and the <b>viscosity</b> of the liquid. When the "
               "leakage capillary is filled with gas, surface tension can either "
               "draw the liquid into the capillary or repel it, depending on the "
               "<b>contact angle</b> formed by the liquid with the capillary wall "
               "— a measure of the degree of wetting of the solid, i.e. the "
               "relative strength of the attractive forces exerted by the capillary "
               "wall on the liquid molecules compared with the attraction between "
               "the liquid molecules themselves. The opposing forces are in "
               "equilibrium when:"))
    b.append(eq("πr²·ΔP = 2πrT·cosθ   ⟺   ΔP = 2T·cosθ/r", "2-1"))
    b.append(p("where r is the capillary radius, ΔP the capillary pressure, T the "
               "surface tension and θ the contact angle between solid and liquid. "
               "If the contact angle is <b>greater than 90°</b>, surface tension "
               "can prevent leakage flow; if it is <b>less than 90°</b>, the liquid "
               "is drawn into the capillaries and leakage flow starts at low "
               "pressures."))
    b.append(fig(3, F.fig_vsh_2_2()))
    b.append(p("The tendency of metal surfaces to form a contact angle greater "
               "than 90° depends on the presence of a layer of <b>oily, greasy or "
               "waxy substances</b> that normally cover metal surfaces. When this "
               "layer is removed by a solvent, the surface properties alter, and a "
               "liquid that previously was repelled may now wet the surface. The "
               "classic example: <b>kerosene</b> dissolves the greasy surface film "
               "— a valve that was fluid-tight against water may leak badly after "
               "the seatings have been washed with kerosene. Wiping the seating "
               "surfaces with an ordinary cloth may be sufficient to restore the "
               "greasy film, and with it the original seat tightness against "
               "water."))
    b.append(p("Once the leakage capillaries are <b>flooded</b>, the capillary "
               "pressure becomes zero — unless gas bubbles carried by the fluid "
               "break the liquid column. If the capillary diameter is large and "
               "the Reynolds number of the leakage flow exceeds its critical "
               "value, the flow is <b>turbulent</b>. As the diameter decreases and "
               "the Reynolds number falls below its critical value, the flow "
               "becomes <b>laminar</b> — and from Poiseuille's equation the "
               "leakage flow varies inversely with the viscosity of the liquid and "
               "the length of the capillary, and proportionally to the driving "
               "force and the capillary diameter. For high viscosity and small "
               "capillary size, the leakage flow can become so small that it "
               "reaches undetectable amounts."))
    b.append(h3("Sealability against gases", "Kín với khí"))
    b.append(p("Sealability against gases is determined by the <b>viscosity of "
               "the gas and the size of the gas molecules</b>. As the capillary "
               "diameter decreases and the Reynolds number drops below its "
               "critical value, the leakage flow again becomes laminar "
               "(Poiseuille). When the capillary diameter approaches the <b>free "
               "mean path of the gas molecules</b>, the flow loses its mass "
               "character and becomes <b>diffusive</b> — the gas molecules pass "
               "through the capillaries by random thermal motion. The capillary "
               "may decrease finally below the molecular size of the gas, but even "
               "then flow will not strictly cease: gases are known to be capable "
               "of diffusing through solid metal walls."))
    b.append(h3("Mechanism for closing leakage passages",
                "Cơ chế đóng các kênh rò rỉ"))
    b.append(p("Machined surfaces have two texture components: a <b>waviness</b> "
               "with comparatively wide peak spacing, and a <b>roughness</b> of "
               "very small irregularities superimposed on the wavy pattern. Even "
               "for the finest surface finish, these irregularities are large "
               "compared with the size of a molecule. If the material of one of "
               "the mating bodies has a high enough <b>yield strain</b>, the "
               "leakage passages formed by the surface irregularities can be "
               "closed by elastic deformation alone — <b>rubber</b>, with a yield "
               "strain approximately 1,000 times that of mild steel, provides a "
               "fluid-tight seal without being stressed above its elastic limit. "
               "Most materials, however, have a considerably lower elastic strain, "
               "so the material must be stressed <b>above its elastic limit</b> to "
               "close the leakage passages."))
    b.append(p("If both surfaces are metallic, only the <b>summits</b> of the "
               "surface irregularities meet initially, and small loads suffice to "
               "deform the summits plastically. As the area of real contact grows, "
               "the deformation becomes plastic-elastic. When the gaps formed by "
               "the surface waviness are closed, only the surface roughness in the "
               "valleys remains; closing those remaining channels requires very "
               "high loads that may cause severe plastic deformation of the "
               "underlying material. The intimate contact between the two faces "
               "needs, however, to extend only along <b>a continuous line or "
               "ribbon</b> to produce a fluid-tight seal; <b>radially directed "
               "asperities</b> are difficult or impossible to seal."))

    b.append(note("Central idea: tightness is not a yes/no state but a "
                  "<b>leakage criterion</b> chosen for the duty — flow-control "
                  "valves accept nominal leakage while spacecraft demand the atom "
                  "class. For liquids the gateway to leakage is the <b>contact "
                  "angle</b> and surface tension (Equation 2-1): a thin greasy "
                  "film decides whether a valve is water-tight, and kerosene can "
                  "destroy it. For gases, once the capillary shrinks to molecular "
                  "size the flow becomes diffusive and can only be stopped by "
                  "plastically deformed metal-to-metal contact along a continuous "
                  "ribbon."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © 2004 Elsevier Inc. (Gulf Professional Publishing).</i>"))
    return "".join(b)
