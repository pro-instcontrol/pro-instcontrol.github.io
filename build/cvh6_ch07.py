# -*- coding: utf-8 -*-
"""Book 7c, Chapter 7 - Steam Conditioning (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 162-175.
This is a reference chapter: understanding desuperheating and its technical
aspects, typical desuperheater designs (fixed-geometry, variable-geometry,
self-contained, steam-atomized and geometry-assisted wafer), steam conditioning
valves and their attemperator / sparger variants, and turbine bypass systems
with their valves, water control valves and actuation packages. Fourteen
numbered figures are redrawn as vector schematics in `cvh6fig7.py` and placed
in numbered order at their logical prose points.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul
import cvh6fig7 as F

PAGES_SRC = 14          # source printed pp. 162-175 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Steam Conditioning"
TITLE_VI = "Điều hòa hơi"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> desuperheating — giảm nhiệt độ hơi quá nhiệt · "
            "desuperheater — thiết bị giảm nhiệt · superheated steam — hơi quá nhiệt · "
            "spraywater — nước phun · temperature control loop — vòng điều khiển nhiệt độ · "
            "atomization — phun sương · atomizing steam — hơi phun sương · "
            "fixed-geometry nozzle — vòi phun hình học cố định · variable-geometry nozzle — "
            "vòi phun hình học thay đổi · backpressure-activated — kích hoạt bằng áp suất ngược · "
            "self-contained design — thiết kế tích hợp · wafer design — thiết kế dạng wafer · "
            "venturi — ống venturi · liner — ống lót · steam conditioning valve — van điều hòa "
            "hơi · attemperator — thiết bị làm mát hơi · steam sparger — ống phân phối hơi · "
            "flashing — bay hơi đột ngột · turndown — tỷ lệ điều chỉnh · rangeability — khả năng "
            "điều chỉnh · thermal stratification — phân tầng nhiệt · Class V shutoff — độ kín "
            "cấp V · turbine bypass system — hệ thống chuyển tải tuabin · actuation package — "
            "gói cơ cấu chấp hành · digital valve controller — bộ điều khiển van số · "
            "stroking speed — tốc độ hành trình · positioning accuracy — độ chính xác vị trí · "
            "enthalpy — entanpy · specific gravity — trọng lực riêng")
    return (
        "<b>Key terms in this chapter.</b> desuperheating · desuperheater · superheated steam · "
        "spraywater · temperature control loop · atomization · atomizing steam · fixed-geometry "
        "nozzle · variable-geometry nozzle · backpressure-activated · self-contained design · "
        "wafer design · venturi · liner · steam conditioning valve · attemperator · steam sparger "
        "· flashing · turndown · rangeability · thermal stratification · Class V shutoff · "
        "turbine bypass system · actuation package · digital valve controller · stroking speed · "
        "positioning accuracy · enthalpy · specific gravity")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Trong bản dump văn bản, chú thích Hình 7.8 xuất hiện "
            "trước Hình 7.7 trên cùng trang in 168, còn chú thích Hình 7.9 có một dấu cách thừa ở "
            "đầu và nằm rời rạc giữa các nhãn của Hình 7.8. Ở đây các hình được đặt theo thứ tự "
            "số, 7.7 trước 7.8 rồi 7.9, tại các vị trí văn bản hợp lý. (2) Các lỗi OCR «geo "
            "metric» (thiếu dấu cách), «heat−transfer» (dấu trừ Unicode), «Failure to ignore "
            "these mesh sizes» (mâu thuẫn với ý định), «up until a few year ago» và câu lộn xộn "
            "«Typically, of 2-4 seconds are required to move the valve position stroking speeds "
            "from open to close» được giữ nguyên ở bản Anh và giải thích tại đây; bản Việt hiệu "
            "đính theo ý đúng. (3) Một chữ «n» rời rạc xuất hiện ở cuối nhiều mục (sau danh sách "
            "thông số của 7.1, sau 7.2.5, 7.3, 7.4.2, 7.5 và 7.6.3); đây là tàn tích ký hiệu chú "
            "thích của bản PDF, được giữ nguyên ở bản Anh và bỏ qua ở bản Việt. (4) Các phương "
            "trình cân bằng nhiệt và định cỡ trong bản in được trình bày dạng phân số xếp chồng "
            "và căn số; bản dump làm phẳng chúng thành «( )H1-H2 H2-Hw», «0.1247 pw» và «SG "
            "∆Pdsh√». Ở đây chúng được viết lại dạng Qw = Q1 × (H1−H2)/(H2−Hw), Qw = Q2 × "
            "(H1−H2)/(Hw−H1) (đúng như dấu in), Qw(volumetric) = Qw(mass) × 0.1247/ρw và Cv = "
            "Qw(volumetric) × √(SG/ΔPdsh); «pw» là ρw, mật độ nước phun. (5) Hình trong bản in "
            "là ảnh chụp hoặc bản vẽ; ở đây vẽ lại dạng sơ đồ vector minh họa, không phải hình gốc.")
    return (
        "<b>Source notes.</b> (1) In the text dump the caption for Figure 7.8 appears before that "
        "of Figure 7.7 on printed p. 168, while the caption for Figure 7.9 has a leading space "
        "and sits adrift among the labels of Figure 7.8. The figures are placed here in numbered "
        "order, 7.7 before 7.8 and then 7.9, at their logical prose points. (2) The OCR quirks "
        "<i>geo metric</i> (missing space), <i>heat−transfer</i> (Unicode minus), <i>Failure to "
        "ignore these mesh sizes</i> (contradictory wording), <i>up until a few year ago</i> and "
        "the garbled sentence <i>Typically, of 2-4 seconds are required to move the valve position "
        "stroking speeds from open to close</i> are retained in English and explained here; the "
        "Vietnamese text corrects them. (3) A stray letter <i>n</i> appears at the end of several "
        "sections (after the parameter list in 7.1, and after 7.2.5, 7.3, 7.4.2, 7.5 and 7.6.3); "
        "it is a leftover footnote marker from the PDF, kept in English and dropped in Vietnamese. "
        "(4) The heat-balance and sizing equations are printed as stacked fractions and a radical; "
        "the dump flattens them into <i>( )H1-H2 H2-Hw</i>, <i>0.1247 pw</i> and <i>SG ∆Pdsh√</i>. "
        "They are rendered here as Qw = Q1 × (H1−H2)/(H2−Hw), Qw = Q2 × (H1−H2)/(Hw−H1) (as "
        "printed, sign convention retained), Qw(volumetric) = Qw(mass) × 0.1247/ρw and Cv = "
        "Qw(volumetric) × √(SG/ΔPdsh); <i>pw</i> stands for ρw, the spraywater density. "
        "(5) Figures are photographs or line drawings in print; they are redrawn here as "
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
        "Chương này là tài liệu tham khảo về điều hòa hơi: giảm nhiệt độ hơi quá nhiệt bằng cách "
        "phun nước (desuperheating), các kiểu thiết bị giảm nhiệt và vòi phun, van điều hòa hơi "
        "kết hợp giảm áp và giảm nhiệt trong một cụm, và hệ thống chuyển tải tuabin (turbine "
        "bypass) cùng các cấu phần của nó."
        if vi else
        "This chapter is a reference on steam conditioning: reducing superheated steam temperature "
        "by water injection (desuperheating), the various desuperheater and spray-nozzle designs, "
        "steam conditioning valves that combine pressure reduction with desuperheating in one unit, "
        "and turbine bypass systems with their components."))
    N(note_terms("vi"), note_terms("en"))

    # ------------------------------------------------------------ 7.1
    H("7.1 Tìm hiểu về giảm nhiệt độ hơi", "7.1 Understanding Desuperheating")
    P("Hơi quá nhiệt là nguồn năng lượng tuyệt vời để phát điện cơ khí. Tuy nhiên, trong nhiều "
      "trường hợp, hơi ở nhiệt độ giảm đáng kể, gần bão hòa, lại là chất mong muốn hơn. Đó là "
      "trường hợp của hầu hết các ứng dụng trao đổi nhiệt. Cần kiểm soát nhiệt độ chính xác để "
      "nâng cao hiệu suất gia nhiệt, loại bỏ nhiệt độ quá nhiệt không mong muốn trong các quá "
      "trình tiết lưu, hoặc bảo vệ sản phẩm và/hoặc thiết bị phía sau khỏi hư hại do nhiệt. Một "
      "phương pháp giảm nhiệt độ là lắp đặt thiết bị giảm nhiệt (desuperheater).",
      "Superheated steam provides an excellent source of energy for mechanical power generation. "
      "However, in many instances, steam at greatly reduced temperatures, near saturation, proves "
      "a more desirable commodity. This is the case for most heat−transfer applications. Precise "
      "temperature control is needed to improve heating efficiency, eliminate unintentional "
      "superheat in throttling processes, or to protect downstream product and/or equipment from "
      "heat related damage. One method to reduce temperature is the installation of a "
      "desuperheater.")
    P("Thiết bị giảm nhiệt phun một lượng nước được kiểm soát, xác định trước vào dòng hơi để hạ "
      "nhiệt độ hơi. Để đạt được điều này một cách hiệu quả, thiết bị phải được thiết kế và lựa "
      "chọn đúng cho ứng dụng. Dù có vẻ đơn giản về mặt thiết kế, thiết bị giảm nhiệt phải phối "
      "hợp được với nhiều biến số phức tạp về nhiệt và động lực học dòng chảy thì mới có hiệu "
      "quả. Việc điều khiển lượng nước — và do đó nhiệt độ hơi — dùng một vòng điều khiển nhiệt "
      "độ. Vòng này gồm cảm biến nhiệt độ phía sau, bộ điều khiển so sánh nhiệt độ đo được với "
      "điểm đặt mong muốn, và truyền tín hiệu điều khiển đến cụm van/cơ cấu chấp hành điều khiển "
      "nước để định lượng nước cần thiết.",
      "A desuperheater injects a controlled, predetermined amount of water into a steam flow to "
      "lower the temperature of the steam. To achieve this efficiently, the desuperheater must be "
      "designed and selected correctly for the application. Although it can appear simplistic in "
      "design, the desuperheater must integrate with a wide variety of complex thermal and flow "
      "dynamic variables to be effective. The control of the water quantity, and thus the steam "
      "temperature, uses a temperature control loop. This loop includes a downstream temperature "
      "sensing device, a controller to interpret the measured temperature relative to the desired "
      "set point, and the transmission of the control signal to a water controlling valve/actuator "
      "assembly to meter the required quantity of water.")
    P("Thành công hay thất bại của một lần lắp đặt thiết bị giảm nhiệt phụ thuộc vào nhiều yếu tố "
      "vật lý, nhiệt và hình học. Một số rõ ràng, một số khó nhận thấy, nhưng tất cả đều có tác "
      "động khác nhau đến hiệu năng của thiết bị và của hệ thống lắp đặt nó. Yếu tố đầu tiên — và "
      "có lẽ quan trọng nhất — để thiết bị giảm nhiệt vận hành hiệu quả là chọn đúng kiểu thiết "
      "kế cho từng ứng dụng. Thiết bị giảm nhiệt có đủ mọi hình dạng và kích cỡ, dùng nhiều kỹ "
      "thuật truyền năng lượng và cơ khí khác nhau để đạt hiệu năng mong muốn trong giới hạn của "
      "môi trường hệ thống. Mục 7.2 trình bày chi tiết sự khác nhau giữa các kiểu thiết bị giảm "
      "nhiệt sẵn có và hiệu năng dự kiến.",
      "The success or failure of a particular desuperheater installation rests on a number of "
      "physical, thermal, and geo metric factors. Some of these are obvious and some obscure, but "
      "all of them have a varying impact on the performance of the equipment and the system in "
      "which it is installed. The first–and probably most important–factor for efficient "
      "desuperheater operation is to select the correct design for the respective application. "
      "Desuperheaters come in all shapes and sizes and use various energy transfer and mechanical "
      "techniques to achieve the desired performance within the limits of the system environment. "
      "Section 7.2 details the differences in the types of desuperheaters available and expected "
      "performance.")
    FIG(1, F.fig_f7_01())

    # ------------------------------------------------------------ 7.1.1
    H("7.1.1 Khía cạnh kỹ thuật của giảm nhiệt", "7.1.1 Technical Aspects of Desuperheating", h3)
    P("Một số thông số vật lý ảnh hưởng đến hiệu năng của hệ thống giảm nhiệt gồm:",
      "Some of the physical parameters that affect the performance of a desuperheating system "
      "include:")
    B(["Hướng lắp đặt / Installation orientation",
       "Chiều dài đoạn ống thẳng phía sau / Downstream straight pipe length",
       "Nhiệt độ và áp suất nước phun / Spraywater temperature and pressure",
       "Lượng nước phun / Spraywater quantity",
       "Kích thước đường ống hoặc ống lót / Pipeline or liner size",
       "Mật độ hơi / Steam density",
       "Phương pháp phun sương / Method of atomization",
       "Vận tốc hơi / Steam velocity",
       "Tỷ lệ điều chỉnh của thiết bị so với hệ thống / Equipment versus system turndown"],
      ["Installation orientation",
       "Downstream straight pipe length",
       "Spraywater temperature and pressure",
       "Spraywater quantity",
       "Pipeline or liner size",
       "Steam density",
       "Method of atomization",
       "Steam velocity",
       "Equipment versus system turndown"])
    P("Hướng lắp đặt là yếu tố thường bị bỏ qua nhưng rất quan trọng đối với hiệu năng của hệ "
      "thống. Vị trí lắp đặt thiết bị giảm nhiệt có thể ảnh hưởng đến vận hành hệ thống lớn hơn "
      "cả kiểu thiết bị. Với hầu hết thiết bị, hướng tối ưu là đường ống thẳng đứng với chiều "
      "dòng chảy hướng lên — điều này trái với hầu hết các lần lắp đặt thấy trong công nghiệp "
      "hiện nay. Các yếu tố hướng lắp đặt khác gồm phụ kiện đường ống, cút và mọi loại chướng "
      "ngại khác phía sau điểm phun nước. Hình 7.2 minh họa các biến thể trong lắp đặt thiết bị "
      "giảm nhiệt. Cần lưu ý rằng hầu như mọi hướng lắp đặt đều có thể hoạt động nếu tất cả "
      "thông số được đưa đúng vào thiết kế hệ thống.",
      "Installation orientation is an often overlooked–but critical–factor in the performance of "
      "the system. Correct placement of the desuperheater can have a greater impact on system "
      "operation than the style of the unit itself. For most units, the optimum orientation is in "
      "a vertical pipeline with the flow direction up. This is contrary to most installations seen "
      "in industry today. Other orientation factors include pipe fittings, elbows, and any other "
      "type of pipeline obstruction that exists downstream of the water injection point. Figure "
      "7.2 illustrates variations in the installation of a desuperheater. It is important to note "
      "that almost any orientation can be made to work if all parameters are correctly "
      "incorporated into the design of the system.")
    FIG(2, F.fig_f7_02())
    P("Nhiệt độ nước phun có thể ảnh hưởng đáng kể đến hiệu năng của thiết bị giảm nhiệt. Dù đi "
      "ngược với suy nghĩ thông thường, nước ở nhiệt độ cao lại tốt hơn cho việc làm mát. Khi "
      "nhiệt độ nước phun tăng, đặc tính dòng chảy và nhiệt được cải thiện, tác động đến:",
      "Spraywater temperature can have a significant impact on desuperheater performance. Although "
      "it goes against logical convention, high-temperature water is better for cooling. As the "
      "spraywater temperature increases, flow and thermal characteristics improve and impact the "
      "following:")
    B(["Sức căng bề mặt / Surface tension",
       "Phân bố kích thước giọt / Droplet size distribution",
       "Nhiệt ẩn hóa hơi / Latent heat of vaporization",
       "Tốc độ bay hơi / Vaporization rate"],
      ["Surface tension",
       "Droplet size distribution",
       "Latent heat of vaporization",
       "Vaporization rate"])
    P("Cải thiện tất cả các khía cạnh nhờ tăng nhiệt độ nước phun sẽ nâng cao hiệu năng tổng thể "
      "của hệ thống.",
      "Improvements in all these areas, as a result of increased spraywater temperature, improves "
      "the overall performance of the system.")
    P("Không kém phần quan trọng là áp suất giảm có sẵn qua hệ thống nước phun (van nước phun và "
      "vòi phun). Tăng áp suất giảm có sẵn qua hệ thống này có thể rút ngắn đáng kể chiều dài "
      "ống thẳng cần thiết phía sau thiết bị giảm nhiệt.",
      "Equally as important is the pressure drop available across the spraywater system "
      "(spraywater valve and nozzle). Increasing the pressure drop available across this system "
      "can result in significantly shorter straight pipe length requirements downstream of the "
      "desuperheating device.")
    P("Lượng nước cần phun có ảnh hưởng tỷ lệ thuận đến thời gian bay hơi. Quá trình truyền nhiệt "
      "phụ thuộc vào thời gian, vì vậy lượng nước phun ảnh hưởng đến thời gian bay hơi hoàn toàn "
      "và độ ổn định nhiệt. Để xác định lượng nước phun cần thiết (Qw) như hàm của lưu lượng hơi "
      "đầu vào (Q1), thực hiện cân bằng nhiệt đơn giản theo phương trình sau:",
      "The quantity of water to be injected will have a directly proportional effect on the time "
      "for vaporization. The heat transfer process is time-dependent and thus the quantity of "
      "spraywater will affect the time for complete vaporization and thermal stability. To "
      "determine the spraywater required (Qw) as a function of inlet steam flow (Q1), perform a "
      "simple heat balance using the following equation:")
    EQ("Q<sub>w</sub>(mass) = Q<sub>1</sub> × (H<sub>1</sub> − H<sub>2</sub>) "
       "/ (H<sub>2</sub> − H<sub>w</sub>)", "1")
    P("Trong đó Q là lưu lượng khối lượng tính bằng PPH và H là giá trị entanpy riêng tại đầu "
      "vào, đầu ra và nước phun.",
      "Where Q is the mass flow in PPH and H is the individual enthalpy values at the inlet, "
      "outlet, and spraywater.")
    P("Khi phép tính được thực hiện như hàm của lưu lượng hơi đầu ra (Q2), tức là tổ hợp của lưu "
      "lượng hơi đầu vào và nước phun giảm nhiệt, dùng phương trình sau:",
      "When the calculation is performed as a function of outlet steam flow (Q2), that is, the "
      "combination of inlet steam flow and desuperheating spraywater, use the following equation:")
    EQ("Q<sub>w</sub>(mass) = Q<sub>2</sub> × (H<sub>1</sub> − H<sub>2</sub>) "
       "/ (H<sub>w</sub> − H<sub>1</sub>)", "2")
    P("Để thực hiện tính toán Cv cơ bản nhằm định cỡ ban đầu cho thiết bị giảm nhiệt, cần chuyển "
      "Qw(mass) thu được sang Qw(volumetric). Khi dùng hệ đơn vị Anh, phép chuyển đổi như sau:",
      "To perform a basic Cv calculation for initial desuperheater sizing, it is required that "
      "the resultant Qw(mass) is converted to Qw(volumetric). When using English units, the "
      "conversion is done as follows:")
    EQ("Q<sub>w</sub>(volumetric) = Q<sub>w</sub>(mass) × 0.1247 / ρ<sub>w</sub>", "3")
    P("Qw(volumetric) tính bằng GPM và ρw là mật độ của nước phun tính bằng lbm/Ft3. Dựa trên phép "
      "chuyển đổi này, có thể hoàn tất việc định cỡ bằng phép tính Cv sau cho mỗi bộ điều kiện:",
      "Qw(volumetric) is in GPM and pw is the density of the spraywater in lbm/ Ft3. Based on this "
      "conversion, the sizing can be completed with the following Cv calculation for each set of "
      "conditions:")
    EQ("C<sub>v</sub> = Q<sub>w</sub>(volumetric) × √(SG / ΔP<sub>dsh</sub>)", "4")
    P("Trong đó SG là trọng lực riêng của nước phun và ΔPdsh là chênh áp qua thiết bị giảm nhiệt "
      "đề xuất.",
      "Where SG is the specific gravity of the spraywater and ∆Pdsh is the pressure differential "
      "across the proposed desuperheater.")
    P("Khi thiết kế một lần lắp đặt thiết bị giảm nhiệt mới, một mối quan tâm khác cho hiệu năng "
      "đúng đắn của hệ thống là kích thước đường ống. Khi kích thước ống tăng, cần chú ý nhiều "
      "hơn đến vận tốc xuyên thấu của tia phun và độ phủ trong dòng hơi (Hình 7.3).",
      "When designing a new desuperheater installation, another concern for proper system "
      "performance is the pipeline size. As the line size gets larger, more attention must be paid "
      "to the penetration velocity of the spray and the coverage in the flow steam (Figure 7.3).")
    FIG(3, F.fig_f7_03())
    P("Một số thiết bị giảm nhiệt dạng phun điểm đơn có năng lượng vòi phun không đủ để phân tán "
      "khắp toàn bộ diện tích mặt cắt ngang của đường ống. Kết quả là mạng phun bị sụp và xảy ra "
      "phân tầng nhiệt. Một lõi trung tâm bị làm lạnh quá mức hình thành, được bao bọc bởi hơi quá "
      "nhiệt. Tình trạng này thường được loại bỏ sau khi dòng chảy đi qua một vài lần đổi hướng "
      "đường ống, nhưng không phải lúc nào cũng làm được trong giới hạn của hệ thống điều khiển "
      "hoặc của quá trình. Việc bố trí đúng các thiết bị nhiều vòi phun năng lượng cao trong "
      "đường ống lớn thường ngăn được sự hình thành phân tầng nhiệt.",
      "Some single-point, injection-type desuperheaters have insufficient nozzle energy to "
      "disperse throughout the entire cross sectional flow area of the pipeline. As a result, the "
      "spray pattern collapses and thermal stratification occurs. A subcooled center core is "
      "formed that is shrouded with superheated steam. This condition is normally eliminated after "
      "the flow stream has undergone several piping directional changes, but this is not always "
      "possible within the limits of the control system or process. Proper placement of "
      "high-energy, multi-nozzle units in the larger pipelines normally prevents the formation of "
      "thermal stratification.")
    P("Vận tốc tối đa và tối thiểu của hơi có quan hệ trực tiếp với sự trộn lẫn thành công của "
      "nước. Vận tốc ảnh hưởng trực tiếp đến thời gian lưu để nước trộn với hơi. Khi vận tốc tối "
      "đa quá cao, có thể không đủ thời gian để nước trộn đều trước khi gặp chướng ngại như cút "
      "hoặc tê. Vận tốc tối đa lý tưởng cho đường ống thường nằm trong khoảng 150–250 feet/giây "
      "(46–76 mét/giây). Lưu ý rằng vận tốc cục bộ cao hơn tại điểm phun có thể có lợi. Khi vận "
      "tốc tối thiểu quá thấp, độ nhiễu loạn giảm và các giọt nước có xu hướng rơi ra khỏi trạng "
      "thái lơ lửng trong hơi. Theo kinh nghiệm, vận tốc hơi tối thiểu để nước còn lơ lửng là khoảng "
      "15–30 feet/giây (4,5–9 mét/giây) đối với vòi phun lò xo. Với ứng dụng có vận tốc thấp hơn, "
      "trộn lẫn tốt có thể đạt được nhờ thiết bị giảm nhiệt có venturi hoặc hơi phun sương "
      "(atomizing steam).",
      "The maximum and minimum velocity of the steam has a direct relationship on the successful "
      "mixing of the water. The velocity directly affects the residence time available for the "
      "water to mix with the steam. When the maximum velocity is too high, there potentially is "
      "not enough time for the water to mix before it encounters a piping obstruction such as an "
      "elbow or tee. Ideal maximum velocity for pipelines usually ranges from 150-250 feet per "
      "second (46-76 meters per second). Note that higher localized velocities at point of "
      "injection can be beneficial. When the minimum velocity is too low, turbulence is reduced "
      "and the water droplets tend to fall out of suspension in the steam. As a rule, the minimum "
      "steam velocity in which water can remain suspended is approximately 15-30 feet per second "
      "(4.5-9 meters per second) for spring loaded nozzles. For applications with lower "
      "velocities, proper mixing may be achieved with desuperheaters that offer a venturi or "
      "atomizing steam.")
    P("Một trong những khái niệm bị lạm dụng và hiểu sai nhất trong lĩnh vực giảm nhiệt là "
      "turndown. Khi áp dụng cho phần tử điều khiển cuối cùng như van, turndown là tỷ số đơn giản "
      "giữa lưu lượng lớn nhất và lưu lượng nhỏ nhất có thể điều khiển. Turndown đôi khi được dùng "
      "thay thế cho rangeability (khả năng điều chỉnh). Tuy nhiên, ý nghĩa chính xác khác nhau "
      "đáng kể khi so sánh hiệu năng thực tế. Thiết bị giảm nhiệt không phải phần tử điều khiển "
      "cuối cùng, vì vậy hiệu năng của nó liên kết trực tiếp với môi trường hệ thống. Mỗi thành "
      "phần của hệ thống giảm nhiệt có khả năng điều chỉnh riêng (van giảm áp hơi PRV, van điều "
      "khiển nước TCV, vận tốc hơi trong ống, Δp vòi phun). Turndown thực tế của hệ thống thiên "
      "về hàm của thông số hệ thống hơn là dựa trên sự thay đổi lưu lượng thực nghiệm của thiết "
      "bị. Khi hiểu được điều này, rõ ràng là một thiết bị giảm nhiệt tốt không thể khắc phục "
      "khiếm khuyết của một hệ thống kém. Cần đánh giá chúng trên giá trị riêng và có trọng số "
      "phù hợp.",
      "One of the most over-used and misunderstood concepts in the area of desuperheating is "
      "turndown. When applied to a final control element, such as a valve, turndown is a simple "
      "ratio of the maximum to the minimum controllable flow rate. Turndown is sometimes used "
      "interchangeably with rangeability. However, the exact meaning differs considerably when it "
      "comes to actual performance comparisons. A desuperheater is not a final control element, and "
      "as such, its performance is directly linked to its system environment. Each component of "
      "the desuperheater system has a rangeability all its own (steam PRV, water TCV, pipe steam "
      "velocity, nozzle dP). The actual system turndown is more a function of the system parameters "
      "rather than based on the equipment’s empirical flow variations. Once this is understood, it "
      "is obvious that a good desuperheater cannot overcome the failings of a poor system. They "
      "must be evaluated on their own merits and weighted accordingly.")
    P("Dù công nghệ thiết kế vòi phun đã được cải tiến, ống lót (liner) vẫn thường được chỉ định, "
      "đặc biệt ở những khu vực của Hệ thống sinh hơi thu hồi nhiệt (HRSG) cần attemperator liên "
      "cấp hoặc cấp cuối. Ống lót rất hiếm khi dùng trong ứng dụng chuyển tải tuabin. Do các hạt "
      "rắn thường có trong hệ thống và đường ống nước phun, cần luôn lắp bộ lọc nối tiếp (inline "
      "strainer). Kích thước lưới lọc phụ thuộc vào kích thước vòi phun cụ thể được chọn cho ứng "
      "dụng và sẽ được quy định như một phần của thiết kế. Không tuân thủ các kích thước lưới lọc "
      "này có thể dẫn đến giảm nhiệt không đúng cách hoặc hư hại đường ống.",
      "Even with improved nozzle design technology, pipe liners are often specified, especially "
      "in areas of the Heat Recovery Steam Generator where interstage or final stage attemperators "
      "are required. Liners are rarely used in turbine bypass applications. Due to the particulate "
      "often present in spray water systems and piping, inline strainers are always required. Mesh "
      "size is dependent on the particular nozzle size selected for the application and will be "
      "specified as part of the design. Failure to ignore these mesh sizes may result in improper "
      "desuperheating or pipe damage.")
    P("Các phép tính và khuyến nghị trên cung cấp thông tin cần thiết để chọn đúng kiểu và kích "
      "cỡ thiết bị giảm nhiệt. Việc lựa chọn này nên dựa trên nhiều cân nhắc của ứng dụng, như:",
      "The previous calculations and recommendations provide the necessary information to select "
      "the proper desuperheater design and size. This selection should be based on a variety of "
      "application considerations such as:")
    B(["Khả năng điều chỉnh từ tải trọng tối thiểu đến tối đa / Minimum to maximum load "
       "requirement rangeability",
       "Vận tốc hơi tối thiểu và tối đa / Minimum and maximum steam velocity",
       "Chiều dài ống thẳng và khoảng cách cảm biến nhiệt độ phía sau thiết bị giảm nhiệt / "
       "Straight pipe length and temperature sensor distance downstream of the desuperheater",
       "Kích thước và cấp độ dày (schedule) của đường ống hơi / Steam pipe line size and schedule",
       "Chênh áp giữa nước và hơi / Pressure differential between water and steam"],
      ["Minimum to maximum load requirement rangeability",
       "Minimum and maximum steam velocity",
       "Straight pipe length and temperature sensor distance downstream of the desuperheater",
       "Steam pipe line size and schedule",
       "Pressure differential between water and steam n"])

    # ------------------------------------------------------------ 7.2
    H("7.2 Các kiểu thiết bị giảm nhiệt điển hình", "7.2 Typical Desuperheater Designs")
    H("7.2.1 Thiết kế vòi phun hình học cố định",
      "7.2.1 Fixed-Geometry Nozzle Design", h3)
    P("Thiết kế vòi phun hình học cố định (Hình 7.4) là thiết bị giảm nhiệt phun sương cơ khí "
      "đơn giản, với một hoặc nhiều vòi phun có hình học cố định. Thiết bị này dành cho ứng dụng "
      "có thay đổi tải gần như không đổi (khả năng điều chỉnh đến 5:1) và có thể phun sương tốt "
      "ở vận tốc dòng hơi thấp tới 25–30 feet/giây trong điều kiện tối ưu. Lắp đặt tiêu chuẩn "
      "của kiểu này là qua một cút nhánh nối bích trên đường ống hơi NPS 6 (DN 150) trở lên. "
      "Thiết kế này thường không có sẵn cho yêu cầu Cv lớn. Thiết bị cần van điều khiển nước bên "
      "ngoài để định lượng nước dựa trên tín hiệu từ cảm biến nhiệt độ trong đường ống hơi phía "
      "sau.",
      "The fixed-geometry nozzle design (Figure 7.4) is a simple mechanically atomized "
      "desuperheater with single or multiple fixed-geometry spray nozzles. It is intended for "
      "applications with nearly constant load changes (rangeability up to 5:1) and is capable of "
      "proper atomization in steam flow velocities as low as 25-30 feet per second under optimum "
      "conditions. Standard installation of this type of unit is through a flanged branch "
      "connection tee on a NPS 6 (DN 150) or larger steam pipe line. This design is usually not "
      "available for large Cv requirements. This unit requires an external water control valve to "
      "meter water flow based on a signal from a temperature sensor in the downstream steam line.")
    FIG(4, F.fig_f7_04())

    H("7.2.2 Thiết kế vòi phun hình học thay đổi",
      "7.2.2 Variable-Geometry Nozzle Design", h3)
    P("Thiết kế vòi phun hình học thay đổi (Hình 7.5) cũng là thiết bị giảm nhiệt phun sương cơ "
      "khí đơn giản, nhưng dùng một hoặc nhiều vòi phun có hình học thay đổi, kích hoạt bằng áp "
      "suất ngược. Nhờ hình học thay đổi, thiết bị này đáp ứng được ứng dụng cần điều khiển theo "
      "những thay đổi tải vừa phải (khả năng điều chỉnh đến 20:1) và có thể phun sương tốt ở vận "
      "tốc dòng hơi thấp tới 25–30 feet/giây trong điều kiện tối ưu. Lắp đặt tiêu chuẩn của kiểu "
      "này là qua cút nhánh nối bích trên đường ống hơi NPS 8 (DN 200) trở lên. Các thiết bị này "
      "có sẵn cho yêu cầu Cv vừa phải. Thiết kế cần van điều khiển nước bên ngoài để định lượng "
      "nước dựa trên tín hiệu từ cảm biến nhiệt độ trong đường ống hơi phía sau.",
      "The variable-geometry nozzle design (Figure 7.5) is also a simple mechanically atomized "
      "desuperheater, but it employs one or more variable-geometry, back pressure activated spray "
      "nozzles. Due to the variable-geometry, this unit can handle applications requiring control "
      "over moderate load changes (rangeability up to 20:1) and is capable of proper atomization "
      "in steam flow velocities as low as 25-30 feet per second under optimum conditions. Standard "
      "installation of this type of unit is through a flanged branch connection tee on a NPS 8 "
      "(DN 200) or larger steam pipe line. These units are available for moderate Cv requirements. "
      "This design requires an external water control valve to meter water flow based on a signal "
      "from a temperature sensor in the downstream steam line.")
    FIG(5, F.fig_f7_05())

    H("7.2.3 Thiết kế tích hợp", "7.2.3 Self-Contained Design", h3)
    P("Thiết kế tích hợp (Hình 7.6) cũng phun sương cơ khí với một hoặc nhiều vòi phun hình học "
      "thay đổi, kích hoạt bằng áp suất ngược. Như một đặc điểm riêng, thiết bị này gộp cả phần tử "
      "điều khiển lưu lượng nước vào cùng một cụm với thiết bị giảm nhiệt. Sự kết hợp này hoạt động "
      "y hệt van nước phun và thiết bị giảm nhiệt riêng biệt, nhưng được đóng gói chung để giảm "
      "hạn chế về không gian và công việc sửa đổi đường ống cần thiết cho các lần lắp đặt hiện có. "
      "Nhờ sự phối hợp chặt chẽ giữa phần tử điều khiển vốn có và vòi phun hình học thay đổi, "
      "thiết bị này đáp ứng được ứng dụng cần điều khiển theo thay đổi tải từ vừa đến cao (khả "
      "năng điều chỉnh đến 25:1). Nó phun sương tốt ở vận tốc dòng hơi thấp tới 25–30 feet/giây "
      "trong điều kiện tối ưu. Lắp đặt tiêu chuẩn của kiểu này là qua cút nhánh nối bích trên "
      "đường ống hơi NPS 8 (DN 200) trở lên. Các thiết bị này có sẵn cho yêu cầu Cv vừa phải.",
      "The self-contained design (Figure 7.6) is also mechanically atomized with one or more "
      "variable-geometry, backpressure-activated spray nozzles. As a special feature, this unit "
      "incorporates a water flow control element packaged to a desuperheating device. This "
      "combination works just like a separate spray water valve and desuperheater but is packaged "
      "together to minimize space constraints and piping modification necessary on existing "
      "installations. Because of the close coordination of the intrinsic control element and the "
      "variable-geometry nozzle(s), this unit can handle applications requiring control over "
      "moderate to high load changes (rangeability up to 25:1). It offers proper atomization in "
      "steam flow velocities as low as 25-30 feet per second under optimum conditions. Standard "
      "installation of this type of unit is through a flanged branch connection tee on a NPS 8 "
      "(DN 200) or larger steam pipe line. These are available for moderate Cv requirements.")
    FIG(6, F.fig_f7_06())

    H("7.2.4 Thiết kế phun sương bằng hơi", "7.2.4 Steam-Atomized Design", h3)
    P("Thiết kế phun sương bằng hơi (Hình 7.7) dùng hơi áp suất cao để phun sương nước phun nhanh "
      "và hoàn toàn. Điều này đặc biệt hữu ích ở đường ống hơi có vận tốc thấp. Hơi phun sương, "
      "thường có áp suất gấp đôi áp suất đường ống hơi chính trở lên, gặp nước trong buồng vòi "
      "phun, nơi năng lượng của hơi giãn nở được dùng để biến nước thành những giọt rất nhỏ. Những "
      "giọt nhỏ hơn chuyển thành hơi nhanh hơn và giúp nước tiếp tục lơ lửng trong dòng có vận "
      "tốc thấp, từ đó bay hơi hoàn toàn. Vì vậy, thiết kế phun sương bằng hơi có thể trộn nước "
      "vào dòng hơi có vận tốc thấp tới khoảng 10 feet/giây trong điều kiện tối ưu. Thiết kế này "
      "xử lý ứng dụng cần thay đổi tải rất lớn (khả năng điều chỉnh đến 50:1). Lắp đặt tiêu chuẩn "
      "qua cút nhánh nối bích trên đường ống hơi NPS 8 (DN 200) trở lên. Thiết kế này có sẵn cho "
      "yêu cầu Cv vừa phải. Nó cần van điều khiển nước bên ngoài để định lượng nước dựa trên tín "
      "hiệu từ cảm biến nhiệt độ trong đường ống hơi phía sau. Hệ thống cũng cần một van đóng/ngắt "
      "riêng cho nguồn hơi phun sương.",
      "The steam-atomized design (Figure 7.7) incorporates the use of high-pressure steam for rapid "
      "and complete atomization of the spraywater. This is especially useful in steam pipe lines "
      "that have low steam velocity. The atomizing steam, usually twice the main steam line "
      "pressure or higher, encounters the water in the spray nozzle chamber where the energy of "
      "the expanding atomizing steam is used to atomize the water into very small droplets. These "
      "smaller droplets allow for faster conversion to steam and permit the water to remain "
      "suspended in a low steam velocity flow, thereby allowing complete vaporization to occur. "
      "The steam-atomized design, therefore, can properly mix water into steam flow velocities as "
      "low as approximately 10 feet per second under optimum conditions. This design handles "
      "applications requiring very high load changes (rangeability up to 50:1). Standard "
      "installation of this type of unit is through a flanged branch connection tee on a NPS 8 "
      "(DN 200) or larger steam pipe line. This design is available for moderate Cv requirements. "
      "It requires an external water control valve to meter water flow based on a signal from a "
      "temperature sensor in the downstream steam line. This system also requires a separate "
      "on/off valve for the atomizing steam supply.")
    FIG(7, F.fig_f7_07())
    FIG(8, F.fig_f7_08())

    H("7.2.5 Thiết kế wafer hỗ trợ bằng hình học",
      "7.2.5 Geometry-Assisted Wafer Design", h3)
    P("Thiết kế wafer hỗ trợ bằng hình học (Hình 7.9) ban đầu được phát triển cho đường ống hơi "
      "nhỏ hơn NPS 6 (DN 150), không thể chứa thiết bị giảm nhiệt dạng chèn. Thiết bị được chế tạo "
      "dạng wafer lắp giữa hai bích trong đường ống hơi. Một cổ hẹp venturi đường kính giảm cho "
      "nước phun bao quanh wafer và cho phép nhiều điểm phun qua các lỗ khoan hoặc vòi phun nhỏ. "
      "Ngoài ra, venturi tăng vận tốc hơi tại điểm phun, tăng cường phun sương và trộn lẫn ở vận "
      "tốc dòng hơi thấp tới khoảng 15 feet/giây trong điều kiện tối ưu. Thiết bị xử lý ứng dụng "
      "cần điều khiển theo thay đổi tải vừa phải (khả năng điều chỉnh đến 20:1). Có thể lắp cho "
      "đường ống kích thước NPS 1 đến NPS 24 (DN 25 đến DN 600) và có sẵn cho yêu cầu Cv vừa phải. "
      "Thiết kế này cần van điều khiển nước bên ngoài để định lượng nước dựa trên tín hiệu từ cảm "
      "biến nhiệt độ trong đường ống hơi phía sau.",
      "The geometry-assisted wafer design (Figure 7.9) was originally developed for small steam "
      "pipe line sizes of less than NPS 6 (DN 150) that were unable to accommodate an "
      "insertion-style desuperheater. The unit is designed as a wafer that is installed between "
      "two flanges in the steam pipe line. A reduced diameter throat venturi allows water to spray "
      "completely around the wafer and permits multiple points of spraying either through drilled "
      "holes or small nozzles. In addition, the venturi increases the steam velocity at the point "
      "of injection, which enhances atomization and mixing in steam flow velocities as low as "
      "approximately 15 feet per second under optimum conditions. It handles applications "
      "requiring control over moderate load change (rangeability up to 20:1). It can be installed "
      "in steam pipe line sizes of NPS 1 through NPS 24 (DN 25 through DN 600), and is available "
      "for moderate Cv requirements. This design requires an external water control valve to meter "
      "water flow based on a signal from a temperature sensor in the downstream steam line.")
    FIG(9, F.fig_f7_09())

    # ------------------------------------------------------------ 7.3
    H("7.3 Tìm hiểu về van điều hòa hơi", "7.3 Understanding Steam Conditioning Valves")
    P("Van điều hòa hơi được dùng để giảm đồng thời áp suất và nhiệt độ hơi xuống mức cần thiết "
      "cho một ứng dụng nhất định. Thường thì các ứng dụng này liên quan đến áp suất và nhiệt độ "
      "đầu vào cao, đòi hỏi giảm đáng kể cả hai. Vì vậy, tốt nhất nên chế tạo thân van rèn và chế "
      "tạo, có thể chịu tốt hơn tải hơi ở áp suất và nhiệt độ cao. Vật liệu rèn cho phép ứng suất "
      "thiết kế cao hơn, cấu trúc hạt được cải thiện và tính toàn vẹn vật liệu vốn có so với thân "
      "van đúc. Kết cấu rèn cũng cho phép nhà sản xuất cung cấp đến Class 4500, cùng các cấp áp "
      "lực trung gian. Van đúc vẫn có thể là lựa chọn khi cần thân kiểu cầu hoặc khi áp suất và "
      "nhiệt độ thấp hơn.",
      "A steam conditioning valve is used for the simultaneous reduction of steam pressure and "
      "temperature to the level required for a given application. Frequently, these applications "
      "deal with high inlet pressures and temperatures and require significant reductions of both "
      "properties. They are, therefore, best manufactured in a forged and fabricated body that "
      "can better withstand steam loads at elevated pressures and temperatures. Forged materials "
      "permit higher design stresses, improved grain structure, and an inherent material integrity "
      "over cast valve bodies. The forged construction also allows the manufacturer to provide up "
      "to Class 4500, as well as intermediate class ratings. Castings may still be an option when "
      "globe-style bodies are required or lower pressures and temperatures are present.")
    P("Do tính chất hơi thay đổi cực đoan thường xuyên khi giảm nhiệt độ và áp suất, thiết kế thân "
      "rèn và chế tạo cho phép bổ sung đầu ra mở rộng để kiểm soát vận tốc hơi đầu ra ở áp suất "
      "thấp hơn. Tương tự, với áp suất đầu ra giảm, thiết kế rèn-chế tạo cho phép nhà sản xuất "
      "cung cấp cấp áp lực khác nhau cho đầu nối vào và ra để khớp hơn với đường ống lân cận.",
      "Due to frequent extreme changes in steam properties as a result of the temperature and "
      "pressure reduction, the forged and fabricated valve body design allows for the addition of "
      "an expanded outlet to control outlet steam velocity at the lower pressure. Similarly, with "
      "reduced outlet pressure, the forged and fabricated design allows the manufacturer to "
      "provide different pressure class ratings for the inlet and outlet connections to more "
      "closely match the adjacent piping.")
    P("Những ưu điểm khác của việc gộp chức năng giảm áp và giảm nhiệt trong cùng một van, so với "
      "hai thiết bị riêng biệt, gồm:",
      "Other advantages of combining the pressure reduction and desuperheater function in the same "
      "valve versus two separate devices include:")
    B(["Trộn nước phun tốt hơn nhờ dùng tối ưu vùng giãn nở nhiễu loạn phía sau phần tử giảm áp / "
       "Improved spraywater mixing due to the optimum utilization of the turbulent expansion zone "
       "downstream of the pressure reduction elements",
       "Khả năng điều chỉnh được cải thiện / Improved rangeability",
       "Dễ lắp đặt và bảo dưỡng chỉ một thiết bị / Ease of installing and servicing only one "
       "device"],
      ["Improved spraywater mixing due to the optimum utilization of the turbulent expansion zone "
       "downstream of the pressure reduction elements",
       "Improved rangeability",
       "Ease of installing and servicing only one device"])
    P("Có nhiều thiết kế van điều hòa hơi sẵn có đáp ứng các ứng dụng khác nhau. Sau đây là những "
      "ví dụ điển hình.",
      "Several available steam conditioning valve designs meet various applications. Typical "
      "examples of these follow. n")

    # ------------------------------------------------------------ 7.4
    H("7.4 Van điều hòa hơi", "7.4 Steam Conditioning Valves")
    P("Van điều hòa hơi đại diện cho điều khiển hiện đại nhất về áp suất và nhiệt độ hơi bằng cách "
      "kết hợp cả hai chức năng trong một cụm điều khiển tích hợp. Các van này đáp ứng nhu cầu "
      "kiểm soát tốt hơn các điều kiện hơi do chi phí năng lượng tăng và vận hành nhà máy khắt "
      "khe hơn. Van điều hòa hơi cũng cho điều khiển nhiệt độ tốt hơn, giảm ồn tốt hơn và ít hạn "
      "chế về đường ống và lắp đặt hơn so với trạm giảm nhiệt và giảm áp tương đương.",
      "Steam conditioning valves represent state-of-the-art control of steam pressure and "
      "temperature by combining both functions within one integral control unit. These valves "
      "address the need for better control of steam conditions brought on by increased energy costs "
      "and more rigorous plant operation. Steam conditioning valves also provide better "
      "temperature control, improved noise abatement, and require fewer piping and installation "
      "restrictions than the equivalent desuperheater and pressure reduction station.")
    P("Van điều hòa hơi trong Hình 7.10 kết hợp điều khiển áp suất và nhiệt độ trong một van. Phân "
      "tích phần tử hữu hạn (FEA) và công cụ động lực học chất lưu tính toán (CFD) đã được dùng "
      "trong quá trình phát triển để xác minh tính toàn vẹn kết cấu cũng như tối ưu hiệu năng "
      "vận hành và độ tin cậy tổng thể. Thiết kế chắc chắn của van này có khả năng xử lý các lần "
      "giảm áp hơi chính toàn áp suất, trong khi cấu hình dòng chảy hướng lên kết hợp công nghệ "
      "giảm ồn của van điều khiển ngăn không cho phát sinh ồn và rung động quá mức.",
      "The steam conditioning valve shown in Figure 7.10 combines pressure and temperature control "
      "in a single valve. Finite element analysis (FEA) and computational fluid dynamic (CFD) tools "
      "were used in its development to qualify its structural integrity as well as optimize the "
      "valve’s operating performance and overall reliability. The rugged design of this steam "
      "conditioning valve proves capable of handling full-pressure main steam drops, while its "
      "flow-up configuration in conjunction with control valve noise abatement technology prevents "
      "the generation of excessive noise and vibration.")
    FIG(10, F.fig_f7_10())
    P("Cấu hình trim đơn giản dùng trong van điều hòa hơi chịu được những thay đổi nhiệt độ nhanh, "
      "như khi tuabin bị cắt. Cage được tôi cứng bề mặt để tuổi thọ tối đa và được phép giãn nở "
      "trong các đợt dao động do nhiệt. Nút van được dẫn hướng liên tục và dùng lớp phủ gốc "
      "coban cả làm dải dẫn hướng và để tạo độ kín kim loại-kim loại chặt với đế.",
      "The simplified trim configuration used in the steam conditioning valve accommodates rapid "
      "changes in temperature, as experienced during a turbine trip. The cage is case hardened for "
      "maximum life and is allowed to expand during thermally induced excursions. The valve plug "
      "is continuously guided and utilizes cobalt-based overlays both as guide bands and to "
      "provide tight, metal-to-metal shutoff against the seat.")
    P("Van điều hòa hơi có manifold nước phun phía sau cấp giảm áp. Manifold có các vòi phun hình "
      "học thay đổi, kích hoạt bằng áp suất ngược, tối đa hóa sự trộn lẫn và bay hơi nhanh nước "
      "phun.",
      "The steam conditioning valve incorporates a spraywater manifold downstream of its pressure "
      "reduction stage. The manifold features variable-geometry, backpressure activated spray "
      "nozzles that maximize mixing and quick vaporization of the spraywater.")
    P("Vòi phun ban đầu được phát triển cho hệ thống xả vào tụng điện, nơi áp suất hơi phía sau "
      "có thể xuống dưới mức bão hòa. Kiểu vòi này cải thiện turndown của thiết bị bằng cách giảm "
      "lưu lượng tối thiểu. Điều này đạt được nhờ áp suất ngược của vòi ở Δp thấp. Cũng có lợi là "
      "Δp vòi tăng ở độ mở thấp giúp nước bay hơi đột ngột qua lối ra của vòi thay vì qua trim của "
      "van nước phun. Việc tải lò xo cho nút vòi phun ngăn không cho những thay đổi đó xảy ra bằng "
      "cách bắt nút đóng lại khi hiện tượng bay hơi đột ngột xuất hiện. Khi bay hơi đột ngột, độ "
      "nén của chất lỏng thay đổi và lò xo vòi sẽ ép đóng lại, tái áp lực cho cột chất lỏng. Sau "
      "đó chất lỏng lấy lại tính chất lỏng và thiết lập lại dòng chảy vào tụng điện.",
      "The spray nozzle was developed originally for condenser dump systems in which the "
      "downstream steam pressure can fall below the saturation level. These style nozzles allow "
      "for improved equipment turndown by reducing the minimum flow. This is accomplished through "
      "nozzle backpressure at lower dP. Also beneficial is that an increased nozzle dP at lower "
      "openings allows the water to flash across the nozzle exit instead of across the spray water "
      "valve trim. Spring loading of the nozzle plug within the spray nozzle prevents any such "
      "changes by forcing the plug to close when flashing occurs. With flashing, the "
      "compressibility of the fluid changes, and the nozzle spring will force closure and "
      "re-pressurization of the fluid leg. Once this is done, the fluid will regain its liquid "
      "properties and reestablish flow to the condenser.")
    FIG(11, F.fig_f7_11())
    P("Van điều hòa hơi phun nước về giữa đường ống và xa thành ống. Số điểm phun thay đổi theo "
      "ứng dụng. Với chênh áp hơi lớn, kích thước đầu ra của van tăng mạnh để chứa thể tích riêng "
      "lớn hơn. Tương ứng, số vòi phun tăng lên được bố trí quanh chu vi đầu ra, tạo sự phân bố "
      "nước phun đều và đầy đủ hơn.",
      "The steam conditioning valve injects the spray water towards the center of the pipeline and "
      "away from the pipe wall. The number of injection points varies by application. With high "
      "differentials in steam pressure, the outlet size of the valve increases drastically to "
      "accommodate the larger specific volumes. Correspondingly, an increased number of nozzles are "
      "arranged around the circumference of the outlet, making for a more even and complete "
      "distribution of the spray water.")
    P("Bố trí trim đơn giản trong van điều hòa hơi cho phép mở rộng dùng đến cấp áp lực cao hơn "
      "(qua ANSI Class 2500 hoặc cao hơn) và nhiệt độ vận hành cao hơn. Cấu hình nút cân bằng cho "
      "độ kín Class V và đặc tính dòng chảy tuyến tính.",
      "The simplified trim arrangement in the steam conditioning valve permits extending its use "
      "to higher pressure classes (through ANSI Class 2500 or higher) and operating temperatures. "
      "Its balanced plug configuration provides Class V shutoff and a linear flow characteristic.")
    P("Van điều hòa hơi thường dùng cơ cấu chấp hành piston khí nén hiệu năng cao kết hợp bộ điều "
      "khiển van số để đạt hành trình đầy đủ trong chưa tới hai giây mà vẫn duy trì đáp ứng bước "
      "rất chính xác.",
      "The steam conditioning valve typically uses high-performance, pneumatic piston actuators in "
      "combination with a digital valve controller to achieve a full stroke in less than two "
      "seconds while maintaining highly accurate step response.")
    P("Khi đường ống bắt buộc, van điều hòa hơi có thể được cung cấp dưới dạng các cấu phần riêng, "
      "cho phép điều khiển áp suất trong thân van và giảm nhiệt độ trong bộ làm mát hơi phía sau. "
      "Thân van kiểu cầu đúc cũng có thể được cung cấp và dùng kết hợp với thiết bị giảm nhiệt "
      "dạng chèn để tiết kiệm hơn.",
      "When piping dictates, the steam conditioning valve can be provided as separate components, "
      "allowing pressure control in the valve body and temperature reduction in a downstream "
      "steam cooler. Also cast globe bodies can be provided and used in combination with "
      "insertion-style desuperheaters for more economical purposes.")

    H("7.4.1 Bộ làm mát hơi", "7.4.1 Steam Attemperator", h3)
    P("Bộ làm mát hơi (Hình 7.12) thường được dùng khi ứng dụng yêu cầu tách riêng chức năng giảm "
      "áp và giảm nhiệt. Bộ làm mát hoặc attemperator được trang bị manifold cấp nước. Manifold "
      "(có thể có nhiều manifold) dẫn nước làm mát đến một số vòi phun riêng lẻ lắp trên thành ống "
      "của đoạn đầu ra. Kết quả là tia phun mịn được bắn theo phương hướng tâm vào vùng nhiễu "
      "loạn cao của dòng hơi dọc trục. Sự kết hợp giữa diện tích tiếp xúc lớn của nước và độ "
      "nhiễu loạn cao của hơi tạo nên sự trộn lẫn rất hiệu quả và bay hơi nhanh.",
      "The steam attemperator (Figure 7.12) is normally used when an application requires a "
      "separation of the pressure reduction and desuperheating functions. The steam cooler or "
      "attemperator is equipped with a water supply manifold. The manifold (multiple manifolds are "
      "possible) provides cooling water flow to a number of individual spray nozzles installed in "
      "the pipe wall of the outlet section. The result is a fine spray injected radially into the "
      "high turbulence of the axial steam flow. The combination of large contact surface area of "
      "the water and high turbulence in the steam make for very efficient mixing and rapid "
      "vaporization.")
    FIG(12, F.fig_f7_12())

    H("7.4.2 Ống phân phối hơi", "7.4.2 Steam Sparger", h3)
    P("Ống phân phối hơi (Hình 7.13) là thiết bị giảm áp dùng để xả hơi an toàn vào tụng điện "
      "hoặc ống xả của tuabin. Ngoài ra, ống phân phối hơi tạo áp suất ngược cho van chuyển tải "
      "tuabin, hạn chế vận tốc hơi và cho phép giảm kích thước ống giữa van chuyển tải và ống phân "
      "phối. Thiết kế và lắp đặt ống phân phối đều là yếu tố then chốt khi xét đến tổng độ ồn của "
      "hệ thống. Thiết kế của ống phân phối rất quan trọng đối với sự vận hành đúng đắn của hệ "
      "thống chuyển tải tuabin. Để giải quyết ồn do dòng chảy, ống phân phối hơi có thể dùng "
      "nhiều công nghệ giảm ồn khác nhau.",
      "Steam spargers (Figure 7.13) are pressure-reducing devices used to safely discharge steam "
      "into a condenser or turbine exhaust duct. In addition, the steam sparger provides "
      "backpressure to the turbine bypass valve, limits steam velocity and allows reduced pipe size "
      "between the bypass valve and sparger. Sparger design and installation are both key elements "
      "when considering total system noise. The design of the sparger is critical to a properly "
      "functioning turbine bypass system. To address flow-induced noise, steam spargers can employ "
      "various noise abatement technologies.")
    FIG(13, F.fig_f7_13())

    # ------------------------------------------------------------ 7.5
    H("7.5 Tìm hiểu về hệ thống chuyển tải tuabin",
      "7.5 Understanding Turbine Bypass Systems")
    P("Hệ thống chuyển tải tuabin đã phát triển trong vài thập kỷ qua khi phương thức vận hành "
      "nhà máy điện thay đổi. Hệ thống được dùng thường xuyên ở nhà máy điện tiện ích, nơi vận "
      "hành đòi hỏi đáp ứng nhanh với biến động lớn về nhu cầu năng lượng. Một ngày vận hành điển "
      "hình có thể bắt đầu ở tải tối thiểu, tăng đến công suất đầy đủ trong hầu hết thời gian, "
      "giảm nhanh về công suất tối thiểu, rồi lại tăng lên tải đầy đủ — tất cả trong vòng 24 giờ. "
      "Lò hơi, tuabin, tụng điện và thiết bị liên quan không thể đáp ứng đúng những thay đổi nhanh "
      "như vậy nếu không có một dạng hệ thống chuyển tải tuabin.",
      "The turbine bypass system has evolved over the last few decades as the mode of power plant "
      "operations has changed. It is employed routinely in utility power plants where operations "
      "require quick response to wide swings in energy demands. A typical day of power plant "
      "operation might start at minimum load, increase to full capacity for most of the day, "
      "rapidly reduce back to minimum output, then up again to full load—all within a 24-hour "
      "period. Boilers, turbines, condensers and other associated equipment cannot respond "
      "properly to such rapid changes without some form of turbine bypass system.")
    P("Hệ thống chuyển tải tuabin cho phép vận hành lò hơi độc lập với tuabin. Ở chế độ khởi động, "
      "hoặc khi giảm nhanh yêu cầu phát điện, chuyển tải tuabin không chỉ cung cấp đường dẫn dòng "
      "chảy thay thế cho hơi mà còn điều hòa hơi tới cùng áp suất và nhiệt độ như thường được tạo "
      "ra bởi quá trình giãn nở trong tuabin. Bằng cách cung cấp đường dẫn thay thế, hệ thống bảo "
      "vệ tuabin, lò hơi và tụng điện khỏi hư hại do dao động nhiệt và áp suất. Vì lý do này, "
      "nhiều hệ thống yêu cầu thời gian đáp ứng đóng/mở cực nhanh để bảo vệ thiết bị tối đa. Điều "
      "này được thực hiện nhờ hệ thống cơ cấu chấp hành cung cấp cả lực và điều khiển cho thao "
      "tác đó.",
      "The turbine bypass system allows operation of the boiler independent of the turbine. In the "
      "start-up mode, or rapid reduction of generation requirement, the turbine bypass not only "
      "supplies an alternate flow path for steam, but conditions the steam to the same pressure and "
      "temperature normally produced by the turbine expansion process. By providing an alternate "
      "flow path for the steam, the turbine bypass system protects the turbine, boiler, and "
      "condenser from damage that may occur from thermal and pressure excursions. For this reason, "
      "many turbine bypass systems require extremely rapid open/close response times for maximum "
      "equipment protection. This is accomplished with an actuation system that provides both the "
      "forces and controls for such operation.")
    P("Ngoài ra, khi chạy thử nhà máy mới, hệ thống chuyển tải tuabin cho phép khởi động và kiểm "
      "tra lò hơi riêng biệt với tuabin. Điều này giúp khởi động nhanh hơn, mang lại lợi ích kinh "
      "tế hấp dẫn. Nó cũng có nghĩa là hệ thống vòng kín này có thể ngăn mất nước cấp đã xử lý ra "
      "khí quyển và giảm phát thải ồn môi trường.",
      "Additionally, when commissioning a new plant, the turbine bypass system allows start up and "
      "check out of the boiler separately from the turbine. This allows for quicker plant "
      "start-ups, which results in attractive economic gains. It also means that this closed-loop "
      "system can prevent atmospheric loss of treated feedwater and reduction of ambient noise "
      "emissions.")

    # ------------------------------------------------------------ 7.6
    H("7.6 Các cấu phần của hệ thống chuyển tải tuabin",
      "7.6 Turbine Bypass System Components")
    P("Thành phần chính của hệ thống chuyển tải tuabin là van chuyển tải tuabin, van điều khiển "
      "nước chuyển tải tuabin và hệ thống cơ cấu chấp hành.",
      "The major elements of a turbine bypass system are turbine bypass valves, turbine bypass "
      "water control valves, and the actuation system.")

    H("7.6.1 Van chuyển tải tuabin", "7.6.1 Turbine Bypass Valves", h3)
    P("Dù cho ứng dụng áp suất thấp, trung bình hay cao, van chuyển tải tuabin thường yêu cầu đóng "
      "kín (Class V). Do yêu cầu lắp đặt đặc thù, các van kiểu manifold đôi khi được tách thành "
      "hai phần: phần giảm áp của van và phần làm mát đầu ra/manifold đặt gần tụng điện hơn. Việc "
      "chọn van điều khiển chuyển tải tuabin cho quá trình phức tạp này trước hết nên thực hiện "
      "bằng cách hiểu các mục tiêu hiệu năng cần đạt, hình học đường ống thực tế hiện có hoặc dự "
      "kiến, và xác định điều khiển quá trình cần thiết. Khi đã hiểu rõ, các yếu tố khác như kiểu "
      "và kích thước van điều khiển, nhu cầu điều khiển áp suất và lưu lượng, yêu cầu quy định về "
      "ồn, yêu cầu vật liệu và thói quen vận hành của quá trình mới được đưa vào. Có nhiều biến "
      "thể, từ thân cầu riêng với thiết bị giảm nhiệt phía sau đến thiết bị tích hợp điều khiển áp "
      "suất và nhiệt độ trong một cụm.",
      "Whether for low-pressure, intermediate pressure, or high-pressure applications, turbine "
      "bypass valves usually require tight shutoff (Class V). Because of particular installation "
      "requirements these manifold design valves will occasionally be separated into two parts: the "
      "pressure-reducing portion of the valve and then the outlet/manifold cooler section located "
      "closer to the condenser. Selecting a turbine bypass control valve for this complex process "
      "should first be done by understanding the performance goals that need to be accomplished, "
      "what real piping geometry exists or is planned, and determining what process controls are "
      "needed. Once this is understood, other factors such as control valve style and size, "
      "pressure and flow control needs, noise specification requirements, material requirements, "
      "and operational practices of the process can be incorporated. Many variations are possible "
      "and range from separate globe bodies with downstream desuperheaters to devices that "
      "incorporate pressure and temperature control in one unit.")
    P("Thiết kế van chuyển tải tuabin có thể khác nhau đáng kể, cũng như các ứng dụng chúng phải "
      "phục vụ. Mỗi loại có đặc tính hoặc tùy chọn riêng mang lại vận hành hiệu quả trong dải điều "
      "kiện rộng và theo yêu cầu riêng của khách hàng. Van chuyển tải tuabin thường được tùy chỉnh "
      "cho từng lần lắp đặt cụ thể. Rất hiếm khi hai lần lắp đặt van chuyển tải tuabin giống hệt "
      "nhau.",
      "Turbine bypass valve designs can vary considerably, as do the applications they are "
      "required to handle. Each has particular characteristics or options that yield efficient "
      "operation over a wide range of conditions and customer specified requirements. Turbine "
      "bypass valves are often customized to specific installations. Rarely are any two turbine "
      "bypass valves installations identical.")
    P("Có thể chọn thân van cầu hoặc van góc riêng với thiết bị giảm nhiệt phía sau, phù hợp tiện "
      "lợi với bố trí đường ống hiện có. Van điều khiển thân trượt được thiết kế để điều khiển "
      "lưu lượng chính xác. Chúng cũng có thể dùng trim giảm ồn thường cần cho các lần giảm áp lớn "
      "trong ứng dụng xả hơi và chuyển tải tuabin. Cách tiếp cận này phù hợp với dải ứng dụng từ "
      "nhẹ đến khắc nghiệt.",
      "Separate globe or angle valve bodies with downstream desuperheating devices can be selected "
      "that conveniently fit into the piping layouts already in place. Sliding-stem control valves "
      "are designed to provide precise flow control. They also can incorporate noise abatement "
      "trims that are often needed for the large pressure drops seen in steam letdown and turbine "
      "bypass applications. This approach can accommodate mild to severe application ranges.")

    H("7.6.2 Van điều khiển nước chuyển tải tuabin",
      "7.6.2 Turbine Bypass Water Control Valves", h3)
    P("Những van này cần thiết để điều khiển dòng nước đến van chuyển tải tuabin. Do yêu cầu bảo "
      "vệ thiết bị, các van này nhất thiết phải đóng kín (Class V). Yêu cầu trim của van có thể "
      "từ trim tiêu chuẩn đến kiểu giảm xâm thực.",
      "These valves are required to control the flow of the water to the turbine bypass valves. Due "
      "to equipment protection requirements, it is imperative that these valves provide tight "
      "shutoff (Class V). Valve trim requirements can range from standard trim to "
      "cavitation-reduction styles.")

    H("7.6.3 Cơ cấu chấp hành", "7.6.3 Actuation", h3)
    P("Trong hệ thống chuyển tải điển hình, thông lệ phổ biến là cho van chuyển tải nhảy đến một "
      "độ mở đặt trước tương ứng với nhu cầu lưu lượng xác định trong sự kiện nhà máy. Tuy nhiên, "
      "van phải được để ở chế độ tay trong một khoảng thời gian nhất định đến khi hệ thống ổn "
      "định thì mới chuyển sang vận hành tự động. Điều này đòi hỏi thuật toán và logic điều khiển "
      "chuyên biệt làm tăng độ phức tạp vận hành — cho đến vài năm trước đây điều đó là không "
      "tránh khỏi.",
      "In typical bypass systems, it has been common practice to trip the bypass valves to a preset "
      "opening corresponding to a predetermined flow rate demand during a plant event. However, "
      "the valves have to be left in manual for a specific amount of time until the systems "
      "stabilized before they could switch over to automatic operation. This requires specialized "
      "algorithms and control logic that increases operation complexity which, up until a few year "
      "ago, was unavoidable.")
    P("Tuy nhiên, trong thị trường điện lực ngày nay, giới hạn của hệ thống chuyển tải tuabin đang "
      "bị đẩy xa hơn. Thay vì phải lo chuyển van chuyển tải sang chế độ tay trong sự kiện nhà "
      "máy, các lắp đặt đang dùng cơ cấu chấp hành hiệu năng cao để đáp ứng vừa nhanh vừa chính "
      "xác nhằm đáp ứng các nhu cầu khác nhau của nhà máy. Van chuyển tải tuabin phải đáp ứng nhanh "
      "để bảo vệ tuabin quan trọng và đắt tiền khỏi hư hại trong các quá trình chuyển tiếp. Chúng "
      "cũng phải chính xác để cho phép vận hành ở hiệu suất đỉnh.",
      "However, in today’s power market, the limits of turbine bypass systems are being pushed. "
      "Instead of having to worry about putting the bypass valves in manual during a plant event, "
      "installations are using high performance actuation to respond with both fast and precise "
      "control to meet various plant demands. Turbine bypass valves must be responsive in order to "
      "protect critical and costly turbines from damage during transients. They also must be "
      "accurate to allow operation at peak efficiency.")
    P("Việc hiểu rõ yêu cầu về tốc độ hành trình và điều khiển có thể cần đến các gói cơ cấu chấp "
      "hành phức tạp thiết kế riêng đáp ứng yêu cầu của quá trình. Thường cần 2–4 giây để di chuyển "
      "van từ vị trí mở đến đóng. Công nghệ chấp hành chính xác không chỉ cần để nhả van nhanh mà "
      "còn phải đạt độ chính xác vị trí tốt hơn 1%, ngay cả với van điều khiển rất lớn.",
      "An understanding of the stroking speed and control requirements may necessitate complex "
      "actuation packages designed to meet the requirements of the process. Typically, of 2-4 "
      "seconds are required to move the valve position stroking speeds from open to close. "
      "Precision actuation technology is required to not only trip this valve quickly but do so "
      "with better than 1% positioning accuracy for even very large control valves.")
    P("Việc thiết lập và chỉnh định nên hoàn tất trong vài phút, và khả năng thực hiện từ xa là rất "
      "mong muốn. Về phần mềm, điều này được thực hiện qua các gói phần mềm cung cấp thông số "
      "chỉnh định được đặt riêng cho kiểu van này. Thông số nên được đặt để cải thiện đáp ứng với "
      "các bước nhỏ bằng cách đẩy quá điểm đặt, điều chỉnh bất đối xứng để đặt riêng thời gian mở "
      "và đóng, và tích hợp đồ họa thời gian thực cho phép chỉnh sửa từ xa.",
      "Setup and tuning should be accomplished within minutes with the capability of doing so "
      "remotely being highly desirable. On the software side, this is done through software "
      "packages that provide for tuning parameters set specifically for these types of valves. "
      "Parameters should be set to improve the response to small amplitude steps by overdriving "
      "the set point, asymmetrically adjust the response to set independently in the opening and "
      "closing times, and integrate real time graphics to allow for adjustments to be done "
      "remotely.")
    P("Về phần cứng, có sẵn giải pháp khí nén hoặc thủy lực để thực hiện nhiệm vụ khó khăn này. Cả "
      "hai đều là giải pháp được thị trường chấp nhận rộng rãi và có thể đạt cùng mục tiêu với bảo "
      "trì tối thiểu.",
      "On the hardware side, pneumatic or hydraulic solutions are available to accomplish this "
      "difficult task. Both are well accepted solutions in the market and can be made to "
      "accomplish the same goal with minimal maintenance required. n")
    FIG(14, F.fig_f7_14())

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 7 chiếm tr. 162–175 của bản in (14 trang) trong Emerson, Control Valve Handbook, ấn "
      "bản 6 (2020). Nội dung gồm sáu mục 7.1–7.6: tìm hiểu về giảm nhiệt độ hơi và các khía cạnh "
      "kỹ thuật, các kiểu thiết bị giảm nhiệt điển hình, tìm hiểu về van điều hòa hơi, van điều "
      "hòa hơi cùng bộ làm mát và ống phân phối, tìm hiểu về hệ thống chuyển tải tuabin, và các "
      "cấu phần của hệ thống chuyển tải tuabin. Mười bốn hình được vẽ lại dạng vector và đặt theo "
      "thứ tự số tại vị trí văn bản hợp lý.",
      "Chapter 7 occupies printed pp. 162-175 (14 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains six sections, 7.1-7.6: understanding desuperheating and its "
      "technical aspects, typical desuperheater designs, understanding steam conditioning valves, "
      "steam conditioning valves with their attemperator and sparger variants, understanding "
      "turbine bypass systems, and the components of a turbine bypass system. The fourteen "
      "numbered figures are redrawn as vectors and placed in numbered order at their logical "
      "prose points.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 Emerson "
      "Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 Emerson "
      "Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
