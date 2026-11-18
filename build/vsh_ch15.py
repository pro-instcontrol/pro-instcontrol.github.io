# -*- coding: utf-8 -*-
"""Book 6, Unit 15 — Rupture Discs: Construction (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 227–260 (PDF pp. 241–274): terminology, applications and liquid-system
limits, materials, temperature effects, heat shields, application
parameters, metal tension-loaded and compression-loaded discs, graphite
discs, holders, quick-change housings, accessories and double-disc
assemblies (Figures 6-1…6-33).
"""

from vsh_common import fig, h2, p, table, ul
import vshfig12 as F12

PAGES_SRC = 34         # source book pp. 227-260
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Rupture Discs: Construction"
TITLE_VI = "Đĩa vỡ: Cấu tạo"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 15.</b> rupture disc — đĩa vỡ · "
                "non-reclosing — không đóng lại · burst pressure — áp vỡ · "
                "rated / marked burst pressure — áp vỡ định mức / ghi nhãn · "
                "burst tolerance — sai số áp vỡ · manufacturing range — "
                "phạm vi chế tạo · performance tolerance — sai số hiệu năng · "
                "operating ratio — tỉ lệ vận hành · forward-acting — tác động "
                "thuận · reverse-buckling — vòm ngược · tension-loaded — tải "
                "kéo · compression-loaded — tải nén · vacuum support — giá "
                "chống chân không · back-pressure support — giá chống áp "
                "ngược · operating ratio — tỉ lệ vận hành · reversal ratio — "
                "tỉ lệ đảo chiều · heat shield — tấm chắn nhiệt · holder — "
                "giá đỡ · clean-sweep — quét sạch · quick-change housing — "
                "vỏ thay nhanh · excess flow valve — van dòng vượt.")
    return ("<b>Key terms.</b> rupture disc · non-reclosing · burst pressure · "
            "rated / marked burst pressure · burst tolerance · manufacturing "
            "range · performance tolerance · operating ratio · "
            "forward-acting · reverse-buckling · tension-loaded · "
            "compression-loaded · vacuum support · back-pressure support · "
            "reversal ratio · heat shield · holder · clean-sweep · "
            "quick-change housing · excess flow valve.")


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
    H("Tổng quan và ứng dụng", "Review and application")
    P("Đĩa vỡ là thiết bị giảm áp không đóng lại; sau khi vỡ phải thay thế. "
      "Dù điều đó có hậu quả kinh tế, nhiều trường hợp đĩa vỡ làm việc tốt "
      "hơn van an toàn xả: phản ứng quá nhanh để van kịp mở do quán tính, "
      "không được phép rò dù chỉ rất nhỏ ra khí quyển, lưu chất cực nhớt, "
      "lưu chất lắng đọng chất rắn làm kẹt đĩa van, hoặc nhiệt độ thấp làm "
      "van bị kẹt.",
      "A rupture disc is a non-reclosing relief device and must be replaced "
      "after bursting. Despite the economic consequence, discs can outperform "
      "relief valves where reaction or overpressurization is too rapid for "
      "valve inertia, where even minute leakage to atmosphere cannot be "
      "tolerated, where the fluid is extremely viscous, where solids would "
      "deposit under a valve disc and disable it, or where low temperature "
      "would cause a valve to seize.")
    P("Đĩa vỡ có thể lắp hai cái nối tiếp hoặc song song, hoặc phối hợp với "
      "van an toàn xả. Hai đĩa nối tiếp ngăn lưu chất ăn mòn thoát ra khi đĩa "
      "thứ nhất rò, nhưng nếu đĩa thứ nhất vỡ sớm thì đĩa thứ hai cũng dễ vỡ "
      "theo; chúng cũng làm cơ cấu mở nhanh khi xì áp giữa hai đĩa. Đĩa song "
      "song với van là thiết bị giảm áp dự phòng. Đĩa lắp trước van ngăn "
      "lưu chất ăn mòn vào van, ngăn rò ra khí quyển, ngăn cặn bám quanh "
      "chỗ kín và giảm chi phí bảo trì. Đĩa lắp sau van ngăn lưu chất ăn mòn "
      "từ hệ thống xả ngược vào van; có thể dùng cả trước lẫn sau.",
      "Discs may be installed in series or parallel, or combined with relief "
      "valves. Two in series prevent corrosive leakage if the first disc "
      "leaks, although premature failure of the first is likely to burst the "
      "second; they also form a quick-opening device when the interspace is "
      "depressurized. A parallel disc acts as secondary relief. An upstream "
      "disc keeps corrosive fluid out of the valve, prevents atmospheric "
      "leakage, prevents deposits at the seat and reduces valve maintenance. "
      "A downstream disc keeps corrosive vent-system fluid out of the valve; "
      "both positions may be used together.")

    H("Giới hạn trong hệ thống lỏng", "Limitations in liquid systems")
    P("Khi đĩa dẻo vỡ trong khí, khí giãn nở mở đĩa trong mili-giây. Trong "
      "chất lỏng, cách vỡ nhanh như vậy chỉ xảy ra nếu có đủ túi khí giữa "
      "chất lỏng và đĩa; để mở nhanh hoàn toàn, thể tích khí phía trước đĩa "
      "thường được khuyến nghị tương đương ít nhất 10 lần đường kính ống nối. "
      "Nếu hệ thống đầy lỏng và áp tăng do giãn nở nhiệt, áp ban đầu chỉ làm "
      "đĩa biến dạng; thể tích tăng thêm có thể tạm ngăn áp tăng tiếp, nhưng "
      "cuối cùng đĩa tác động thuận vỡ ở áp định mức. Chỉ một số ít đĩa vòm "
      "ngược vỡ được ở áp định mức trong hệ thống đầy lỏng, cần hỏi nhà chế "
      "tạo. Đĩa graphite giòn mở ngay lập tức trong mọi dịch vụ. Dù loại nào, "
      "túi khí cũng giảm tốc độ tăng áp do thay đổi thể tích và giảm tải xung "
      "đỉnh khi dao động.",
      "When a ductile disc bursts in gas, expanding gas opens it in "
      "milliseconds. In liquid service this requires a sufficiently large "
      "gas pocket; for rapid full opening, the recommended upstream gas "
      "volume is at least ten pipe diameters of the connected pipe. In a "
      "totally liquid-full system heated at constant volume, pressure first "
      "only deforms the disc; the added volume may temporarily stop further "
      "rise, but a forward-acting disc finally fails at rated pressure. Only "
      "limited reverse-buckling types burst at rated pressure in liquid-full "
      "service and the maker should be consulted. Brittle graphite discs open "
      "instantly in any service. Regardless of type, a gas pocket reduces "
      "pressure rise from liquid volume change and damps peak impulse loads "
      "in pulsating service.")

    H("Vật liệu chế tạo", "Construction materials")
    P("Vật liệu dẻo thường dùng gồm thép không gỉ, Inconel, Monel, nickel "
      "và có thể nhôm, tantalum, platinum, gold, silver hoặc Hastelloy B và "
      "C. Titanium và Hastelloy chỉ nên chọn khi không có vật liệu thay thế, "
      "vì cả hai dễ vỡ sớm do giòn. Đĩa dẻo có thể phủ hoặc lót FEP, TFE, PFA, "
      "epoxy, vinyl, lead hoặc polyethylene. Nhiệt độ tối đa khuyến nghị: "
      "nhôm và bạc 125 °C, nickel và Monel 425 °C, Inconel 535 °C, thép "
      "không gỉ 480 °C; lead 120 °C, PVC 80 °C, FEP 215 °C, TFE hoặc PFA "
      "260 °C.",
      "Common ductile materials are stainless steel, Inconel, Monel and "
      "nickel, with aluminum, tantalum, platinum, gold, silver and Hastelloy "
      "B and C also used. Titanium and Hastelloy should be selected only "
      "where no substitute exists because both tend to fail prematurely "
      "through brittleness. Ductile discs may carry FEP, TFE, PFA, epoxy, "
      "vinyl, lead or polyethylene coatings and linings. Recommended maximum "
      "temperatures are: aluminum and silver 125 °C, nickel and Monel "
      "425 °C, Inconel 535 °C, stainless steel 480 °C; lead 120 °C, PVC "
      "80 °C, FEP 215 °C, TFE or PFA 260 °C.")
    P("Vật liệu giòn hầu như là graphite, dù từng thử gang và sứ. Graphite "
      "thường dùng được chế từ coke dầu mỏ tro thấp nung nhiệt độ cao, trộn "
      "nhựa pitch, ép khối rồi xử lý nhiệt. Vật liệu xốp giòn này được bão "
      "hòa chân không bằng nhựa phenolic hoặc furan. Graphite nguyên chất là "
      "graphite tách lớp dạng bột, ép thành tấm không thấm và dẻo; có thể "
      "hấp thụ một ít lỏng nên đôi khi cần phủ riêng mặt tiếp xúc sản phẩm, "
      "khi đó nhiệt độ giới hạn bởi lớp phủ.",
      "Brittle discs are almost entirely graphite, although cast iron and "
      "porcelain have been tried. Common graphite is made from low-ash "
      "petroleum coke calcined at high temperature, mixed with pitch, formed "
      "into blocks and heat treated. The porous brittle result is vacuum "
      "impregnated with phenolic or furan resin. Pure graphite is exfoliated "
      "powder compressed into an impermeable flexible sheet; it may absorb "
      "some liquid, so a process-side coating is sometimes needed, with "
      "temperature then limited by the coating.")

    H("Nhiệt độ, áp vỡ và tấm chắn nhiệt", "Temperature, burst pressure and heat shields")
    P("Nhiệt độ làm thay đổi độ bền vật liệu nên có quan hệ giữa nhiệt độ "
      "và áp vỡ; quan hệ này khác nhau ngay cả giữa các đĩa cùng vật liệu "
      "nhưng khác cấu tạo. Hình 6-1 chỉ là đường xuân cho đĩa vòm thuận kim "
      "loại rắn của một nhà sản xuất; mỗi lô vật liệu có đường riêng do nhà "
      "chế tạo xác định. Đĩa vòm ngược chịu ảnh hưởng nhiệt độ nhỏ hơn nhiều.",
      "Temperature changes material strength and therefore burst pressure. "
      "The relationship differs even between discs of the same material but "
      "different construction. Figure 6-1 is only qualitative for solid-metal "
      "forward-domed discs from one maker; each material lot has its own "
      "relationship established by the manufacturer. Reverse-buckling discs "
      "are considerably less affected by temperature.")
    FIG(1, F12.fig_vsh_6_1())
    P("Tấm chắn nhiệt che mặt tiếp xúc sản phẩm khỏi bức xạ, hoặc bức xạ "
      "cộng đối lưu, nhưng không được cản trở đĩa vỡ. Có thể dùng các tấm "
      "thép không gỉ chồng nhau để áp tạo cả hai mặt; dòng vỡ sẽ gập mở các "
      "tấm này. Có thể thêm đoạn ống làm bể hút nhiệt và tấm chắn thứ hai ở "
      "đầu kia. Hình 6-2 là giá chứa len sợi silica vô định hình rời để chắn "
      "nhiệt cho đĩa graphite. Khi đĩa vỡ, tấm chắn này phân mảnh và bị thổi "
      "ra, nên không dùng được với giá chống chân không hoặc áp ngược có thể "
      "bị mảnh vỡ làm tắc. Loại này chỉ hợp khí khô vì hút ẩm làm đổi mật độ "
      "len và có thể sụp khối len.",
      "Heat shields protect the process side from radiation, or radiation and "
      "convection, without interfering with rupture. Overlapping stainless "
      "flats allow pressure on both sides and fold open with the discharge. "
      "A spool may act as a heat sink with a second shield at its far end. "
      "Figure 6-2 is a holder packed with loose amorphous-silica wool for "
      "graphite discs. The shield fragments and is discharged on rupture, so "
      "it cannot be combined with a vacuum or back-pressure support that "
      "fragments could block. It suits dry gases only because moisture "
      "absorption changes wool density and may collapse the filling.")
    FIG(2, F12.fig_vsh_6_2())

    H("Thông số ứng dụng", "Application parameters")
    U([("Áp vỡ định mức hay ghi nhãn là áp vỡ trung bình xác định bằng cách "
        "vỡ ít nhất hai đĩa thử; không được vượt áp vỡ tối đa cho phép của "
        "bình theo code.",
        "Rated or marked burst pressure is the average from bursting at least "
        "two test discs and must not exceed the vessel's maximum allowable "
        "burst pressure under the code."),
       ("Sai số áp vỡ: đến 2,76 barg (40 psig) không vượt ±0,14 barg "
        "(±2 psig); trên mức đó không vượt ±5%. Một số loại có thể ±2%.",
        "Burst tolerance: up to 2.76 barg (40 psig), no more than ±0.14 barg "
        "(±2 psig); above that, no more than ±5%; some types offer ±2%."),
       ("Phạm vi chế tạo là dải áp quanh áp đã định, thỏa thuận giữa người "
        "dùng và nhà chế tạo, cho phép chọn lá kim loại phù hợp mà không tốn "
        "quá nhiều thử nghiệm. Có thể biểu thị âm hoặc âm/dương theo phần "
        "trăm hoặc đơn vị áp.",
        "Manufacturing range is the agreed band around the specified burst "
        "pressure that permits economic selection of foil without excessive "
        "finding tests, expressed as minus or plus/minus percentage or in "
        "pressure units."),
       ("Sai số hiệu năng gồm phạm vi chế tạo cộng sai số áp vỡ. "
        "Tỉ lệ vận hành là áp vận hành tối đa chia cho áp vỡ nhỏ nhất, "
        "thường từ 70% hoặc thấp hơn đến 90% tùy loại và nhiệt độ.",
        "Performance tolerance combines manufacturing range and burst "
        "tolerance. Operating ratio is maximum operating pressure divided by "
        "minimum burst pressure, typically 70% or less up to 90% by type and "
        "temperature."),
       ("Tỉ lệ hư hỏng là áp vỡ của đĩa bị hư chia cho áp vỡ của đĩa nguyên "
        "vẹn. Tỉ lệ đảo chiều là áp vỡ khi lắp ngược chia cho áp vỡ khi lắp "
        "đúng. Lô là nhóm đĩa cùng loại, cỡ, giới hạn áp và nhiệt độ, làm "
        "từ cùng vật liệu.",
        "Damage ratio is damaged-disc burst pressure divided by undamaged "
        "burst pressure. Reversal ratio is reversed-installation burst "
        "pressure divided by correct-installation burst pressure. A lot is a "
        "single group of same type, size, pressure and temperature limits "
        "from material of the same identity and properties."),
       ("Cháy chậm là cháy với tốc độ ngọn lửa dưới tốc độ âm trong môi "
        "trường; nổ là cháy với tốc độ vượt tốc độ âm; explosion là vỡ bao "
        "bọc do áp sinh ra từ cháy chậm.",
        "Deflagration burns below the speed of sound in the medium; "
        "detonation propagates a combustion zone above that speed; explosion "
        "is rupture of an enclosure from internally developed deflagration "
        "pressure.")])

    # ==================================================== tension-loaded metal
    H("Đĩa kim loại: kiểu tác động thuận chịu kéo",
      "Metal discs: tension-loaded forward-acting types")
    P("Có hai họ đĩa kim loại dẻo: tác động thuận chịu kéo và tác động ngược "
      "chịu nén. Đĩa vòm thuận và đĩa phẳng thuộc loại chịu kéo. Đĩa vòm thuận "
      "rắn được tạo hình từ đĩa phẳng bằng áp chất lỏng từ mặt dưới, thường "
      "trên 70% áp vỡ, tạo dạng bán cầu (Hình 6-3). Khi áp làm việc vượt áp "
      "tiền tạo vòm, vòm lớn dần; khi tiệm 95% áp vỡ, tâm vòm mỏng đi cục bộ "
      "và đĩa vỡ kèm một số mảnh vỡ. Áp làm việc thường giới hạn 70% áp định "
      "mức hoặc thấp hơn.",
      "Ductile metal discs fall into forward-acting tension-loaded and "
      "reverse-acting compression-loaded families. Forward-domed and flat "
      "discs are tension-loaded. A solid forward-domed disc is formed from "
      "flat stock by fluid pressure on its underside, generally above 70% of "
      "burst pressure, giving a hemispherical shape (Figure 6-3). Above the "
      "predoming pressure the dome grows; near 95% of burst pressure the "
      "centre thins locally and the disc bursts with some fragmentation. "
      "Normal pressure is commonly limited to 70% of rated burst pressure "
      "or less.")
    FIG(3, F12.fig_vsh_6_3())
    P("Lá mỏng dễ bị chân không hoặc áp ngược làm sụp một phần hoặc toàn "
      "phần. Khi có các điều kiện đó cần giá chống chân không khít sát mặt lõm "
      "(Hình 6-4), hoặc trường hợp áp ngược cộng thêm cần giá cố định bổ sung "
      "(Hình 6-5). Nếu giá không khít, đĩa uốn ngược rồi kéo căng luân phiên, "
      "tạo vết nhăn lưng rùa (Hình 6-6) và tuổi thọ kém. Trong dịch vụ đầy "
      "lỏng, đĩa có thể vỡ ban đầu theo dạng khe rồi mở thêm khi áp tăng "
      "(Hình 6-7). Ở áp thấp, đĩa cực mỏng có vòng bảo vệ hai mặt, giá chống "
      "chân không tích hợp và nắp chống va chạm khi cầm (Hình 6-8).",
      "Thin foils may partially or fully collapse under vacuum or "
      "superimposed back pressure. Vacuum supports must closely fit the "
      "concave face (Figure 6-4); supplementary permanent supports may be "
      "needed for back pressure (Figure 6-5). Inadequate support allows "
      "alternate reverse flexing and stretching, producing the turtle-backing "
      "wrinkle pattern (Figure 6-6) and poor life. In liquid-full service the "
      "disc may first open as a slit and then open further as pressure rises "
      "(Figure 6-7). Low-pressure discs use protective rings, an integral "
      "vacuum support and a handling cap (Figure 6-8).")
    FIG(4, F12.fig_vsh_6_4())
    FIG(5, F12.fig_vsh_6_5())
    FIG(6, F12.fig_vsh_6_6())
    FIG(7, F12.fig_vsh_6_7())
    FIG(8, F12.fig_vsh_6_8())
    P("Đĩa vòm thuận có khe và lớp lót gồm ba lớp: lớp vòm trên đục lỗ ở hai "
      "đầu, lớp làm kín thường bằng fluoro-carbon hoặc kim loại đặc biệt và "
      "lớp giá chống chân không khi cần (Hình 6-9). Đĩa vạch cắt chéo dùng "
      "vật liệu dày hơn cho cùng áp vỡ, nâng tỉ lệ vận hành tới 80% hoặc 85%; "
      "mở theo đường cắt dự đoán được và không phân mảnh khi có lớp "
      "fluoro-carbon (Hình 6-10). Trong dịch vụ trùng hợp, giá đỡ được thiết "
      "kế tránh khe hở nơi polymer bắt đầu mọc; không lắp giá chống chân "
      "không trong trường hợp này (Hình 6-11).",
      "A slotted and lined forward-domed disc has three layers: a dome with "
      "pierced holes at each end, a fluorocarbon or exotic-metal seal, and a "
      "vacuum support where required (Figure 6-9). Cross-scored discs use "
      "thicker material, raising operating ratio to 80% or 85%, with a "
      "predictable non-fragmenting opening when combined with a fluorocarbon "
      "seal (Figure 6-10). For polymerization service the holder avoids the "
      "crevice where growth starts, and a vacuum support cannot be fitted "
      "(Figure 6-11).")
    FIG(9, F12.fig_vsh_6_9())
    FIG(10, F12.fig_vsh_6_10())
    FIG(11, F12.fig_vsh_6_11())
    P("Hai dạng đĩa phẳng có khe và lớp lót dùng cho dòng một chiều hoặc hai "
      "chiều. Hình 6-12 là seal môi trường chi phí thấp cho bồn chứa và xe "
      "vận chuyển hoặc phía sau van an toàn xả; kẹp trực tiếp giữa hai mặt "
      "bích class 150, không cần giá riêng, tỉ lệ vận hành tối đa 50%. Hình "
      "6-13 bảo vệ quá áp hệ thống áp thấp, chịu chân không đầy đủ, dùng cho "
      "khí hoặc lỏng đầy, tỉ lệ vận hành tới 80%.",
      "Two slotted and lined flat discs serve one-way or two-way flow. Figure "
      "6-12 is a low-cost environmental seal for transport and storage tanks "
      "or downstream of relief valves; it clamps directly between class 150 "
      "flanges without a separate holder and has a maximum operating ratio "
      "of 50%. Figure 6-13 protects low-pressure systems, withstands full "
      "vacuum, suits gas and liquid-full service and reaches an 80% operating "
      "ratio.")
    FIG(12, F12.fig_vsh_6_12())
    FIG(13, F12.fig_vsh_6_13())

    # ================================================= compression-loaded metal
    H("Đĩa kim loại: kiểu vòm ngược chịu nén",
      "Metal discs: compression-loaded reverse-buckling types")
    P("Ở đĩa vòm ngược, lưu chất tác động lên mặt lõm nhưng gây nén vòm; áp "
      "vỡ do mô-đun Young quyết định, ổn định và ít phụ thuộc nhiệt độ hơn "
      "độ bền kéo. Vỡ xảy ra ở ứng suất thấp hơn nhiều nên đĩa dày hơn, dễ "
      "chế tạo sai số nhỏ trên dải nhiệt rộng. Khi nhiệt độ tăng, độ bền vật "
      "liệu giảm nhưng vòm giãn ra và cứng hơn, phần nào bù trừ. Đĩa không tự "
      "xé toạc khi vòm ngược; cần dao cắt, vạch cắt hoặc đẩy đĩa ra khỏi giá. "
      "Ưu điểm là áp vỡ thấp, tỉ lệ vận hành tới 90% hoặc cao hơn, có thể "
      "zero manufacturing range và sai số ±2%, chịu chu kỳ và xung tốt, tuổi "
      "thọ dài hơn do ít mỏi.",
      "In reverse-buckling discs, fluid loads the convex side in compression. "
      "Buckling pressure is governed by Young's modulus, which is more "
      "reproducible and less temperature-sensitive than tensile strength. "
      "Buckling occurs at much lower stress, so discs are thicker and easier "
      "to make to close tolerances over a wide temperature range. Rising "
      "temperature lowers material strength but expands and stiffens the "
      "dome, partly compensating. Reversal alone does not burst the disc; "
      "cutting devices, scoring or expulsion complete opening. Advantages "
      "include low burst pressures, operating ratios up to 90% and above, "
      "optional zero manufacturing range and ±2% tolerance, excellent cyclic "
      "and pulsating performance and longer fatigue life.")
    P("Đĩa có dao cắt (Hình 6-14) chỉ dùng cho khí hoặc lỏng có túi khí lớn; "
      "trong hệ thống đầy lỏng vòm ngược quá chậm nên đĩa tựa lên dao rồi "
      "bị cắt sau khi áp tăng cao, từng gây vỡ bình. Dao phải sắc và kiểm tra "
      "định kỳ. Đĩa có vòng răng (Hình 6-15) cắt đĩa khi vòm ngược và thiết "
      "kế cho áp vỡ thấp hơn đáng kể. Đĩa vạch cắt chéo mặt lõm (Hình 6-16) "
      "mở thành các cánh hình nêm mà không cần dao.",
      "Knife-blade discs (Figure 6-14) suit gas or liquid with a large gas "
      "pocket; in totally liquid-full systems reversal is too slow, so the "
      "disc rests on the blades and is cut only after a substantial pressure "
      "rise, a known cause of vessel ruptures. Blades must be kept sharp and "
      "checked regularly. A teeth ring (Figure 6-15) pierces the disc at "
      "buckling for considerably lower burst pressure. A disc cross-scored "
      "on the concave side (Figure 6-16) opens in pie-shaped sections without "
      "knife assistance.")
    FIG(14, F12.fig_vsh_6_14())
    FIG(15, F12.fig_vsh_6_15())
    FIG(16, F12.fig_vsh_6_16())
    P("Đĩa có vạch cắt ngoại vi một phần xé dọc vạch rồi gập quanh bản lề "
      "(Hình 6-17, 6-18). Ở Hình 6-19 vạch được đục lỗ để đạt áp vỡ cực "
      "thấp, các lỗ được O-ring làm kín và ép chặt ngay khi có áp; các đĩa "
      "này dùng được cả trong hệ thống đầy lỏng.",
      "Discs with a partial circumferential score shear along the line and "
      "fold around a pivot (Figures 6-17, 6-18). In Figure 6-19 the score is "
      "perforated for extremely low burst pressure; the perforations are "
      "sealed by an O-ring energized as soon as pressure is applied, and the "
      "discs may also be used in liquid-full systems.")
    FIG(17, F12.fig_vsh_6_17())
    FIG(18, F12.fig_vsh_6_18())
    FIG(19, F12.fig_vsh_6_19())
    P("Đĩa trượt ra (Hình 6-20) không xé mà bị đẩy khỏi giá khi vòm ngược; "
      "đế phẳng hẹp ép bằng O-ring hoặc gasket, không cần mô-men siết đặc "
      "biệt. Có thể thêm bộ chặn để đĩa không đi theo ống xả, cho phép lắp "
      "trước van an toàn xả. Tỉ lệ vận hành tới 95%, cỡ DN 25 đến DN 1200, "
      "nhưng không hợp lỏng đầy trừ cỡ lớn và có thể cần giá chống chân "
      "không. Đĩa có khe và thanh uốn (Hình 6-21) dùng phần tử cảm áp có khe "
      "hình răng và các tab uốn; khi đạt áp vòm, thanh uốn gãy, đĩa mở bản "
      "lề và vòng răng cắt lớp làm kín. Đĩa có zero manufacturing range, sai "
      "số đến ±2%, tỉ lệ vận hành 95%, DN 25 đến DN 600, áp đến 120 barg ở "
      "22 °C và nhiệt độ tối đa 550 °C.",
      "The slip-away disc (Figure 6-20) is expelled from the holder on "
      "buckling rather than torn. Its narrow flat seating is sealed by an "
      "O-ring or gasket with no special torque; an arresting device prevents "
      "travel along the vent line, allowing upstream installation. Operating "
      "ratio can reach 95%, sizes run DN 25 to DN 1200, but liquid-full "
      "service is unsuitable except in larger sizes and vacuum support may "
      "be needed. The slotted, lined disc with buckling bars (Figure 6-21) "
      "has a teeth-shaped slot and tabs that buckle and break so the disc "
      "hinges open while the teeth ring cuts the seal. It offers zero "
      "manufacturing range, tolerance down to ±2%, 95% operating ratio, DN 25 "
      "to DN 600, up to 120 barg at 22 °C and a 550 °C maximum.")
    FIG(20, F12.fig_vsh_6_20())
    FIG(21, F12.fig_vsh_6_21())
    P("Đĩa hai chiều dạng vòm tác động thuận ở một chiều và ngược ở chiều kia. "
      "Hình 6-22 gồm đĩa thuận đục lỗ có vạch cắt một phần chống quá áp, "
      "lớp kín PTFE hỏng ở cả quá áp lẫn áp dưới môi trường, và đĩa thanh "
      "uốn ngược hỏng khi chân không. Hình 6-23 dùng đĩa thuận đục lỗ kín "
      "bằng đĩa Teflon tác động ngược, vành đỡ và dao cắt; khi chân không, "
      "đĩa Teflon bị ép vào dao và bị cắt, còn khi quá áp cả hai lớp chịu kéo "
      "và vỡ.",
      "Domed two-way discs act forward in one direction and reverse in the "
      "other. Figure 6-22 combines a perforated forward-domed disc with a "
      "partial score for overpressure, a PTFE seal that fails under "
      "overpressure and subnormal pressure, and a reverse buckling-bar disc "
      "for subnormal pressure. Figure 6-23 uses a perforated forward disc "
      "sealed by a reverse-acting Teflon disc, with a supporting girdle and "
      "knife blades; subnormal pressure presses the Teflon onto the blades, "
      "while overpressure puts both layers in tension and ruptures them.")
    FIG(22, F12.fig_vsh_6_22())
    FIG(23, F12.fig_vsh_6_23())

    # ============================================================ graphite discs
    H("Đĩa graphite", "Graphite rupture discs")
    P("Graphite thấm nhựa giòn, gần như không biến dạng khi vỡ, đồng nhất và "
      "yếu hơn kim loại nên đĩa dày hơn nhưng sai số áp vỡ rất nhỏ. Graphite "
      "nguyên chất dẻo dùng cho đĩa vòm ngược, chịu nhiệt cao hơn vì không "
      "có nhựa thấm. Cả hai dùng được cho khí và lỏng đầy.",
      "Resin-impregnated graphite is brittle, ruptures with almost no "
      "deformation, homogeneous and weaker than metal; discs are thicker but "
      "can hold very small burst tolerances. Pure graphite is flexible and "
      "used for reverse-buckling discs, tolerating higher temperatures "
      "because it has no resin impregnation. Both suit gas and liquid-full "
      "services.")
    P("Đĩa monoblock (Hình 6-24, 6-25) là cụm một mảnh gồm màng vỡ phẳng và "
      "mặt bích lắp. Loại không gia cố DN 25 đến DN 600 có tỉ lệ vận hành "
      "90%, nhiệt độ −70 đến 180 °C, nâng tới 500 °C khi dùng tấm chắn nhiệt, "
      "nhưng cần siết bulông có kiểm soát. Loại gia cố có vòng thép dán quanh "
      "chu vi để ngắn ứng suất đường ống truyền tới màng. Loại hai chiều "
      "(Hình 6-26) có áp vỡ tối đa 10 bar mỗi chiều và chênh lệch tối thiểu "
      "0,7 barg giữa hai mức.",
      "Monoblock discs (Figures 6-24, 6-25) are one-piece devices combining "
      "a flat bursting membrane with the mounting flange. The non-armored "
      "DN 25 to DN 600 type has a 90% operating ratio, −70 to 180 °C service "
      "and up to 500 °C with a heat shield, but needs controlled flange-bolt "
      "torque. The armored type has a bonded circumferential steel ring that "
      "keeps unequal piping stress from reaching the membrane. The two-way "
      "version (Figure 6-26) bursts at up to 10 bar in either direction with "
      "a minimum 0.7 barg difference between ratings.")
    FIG(24, F12.fig_vsh_6_24())
    FIG(25, F12.fig_vsh_6_25())
    FIG(26, F12.fig_vsh_6_26())
    P("Hình 6-27 là cụm có màng graphite thay thế được, lắp trong hốc sâu "
      "định sâu nên không nhạy mô-men siết; các giá chống áp ngược làm diện "
      "tích xả chỉ còn khoảng 50% tiết diện đầy. Hình 6-28 là đĩa vòm ngược "
      "graphite nguyên chất, dày dễ cầm, dùng cho hoá chất và nhiệt độ điển "
      "hình 550 °C; đĩa trên 1,2 barg chịu chân không đầy đủ, sai số áp vỡ "
      "±5% trên 1,0 barg.",
      "Figure 6-27 has a replaceable graphite membrane in a controlled-depth "
      "recess, making installation insensitive to torque, but reverse "
      "supports reduce free vent area to about 50% of full bore. Figure 6-28 "
      "is a pure-graphite reverse-buckling disc, thicker and easier to "
      "handle, suited to chemicals and typically 550 °C. Above 1.2 barg it "
      "supports full vacuum, with ±5% burst tolerance above 1.0 barg.")
    FIG(27, F12.fig_vsh_6_27())
    FIG(28, F12.fig_vsh_6_28())

    # ================================================ holders and assemblies
    H("Giá đỡ, cụm quét sạch và vỏ thay nhanh",
      "Holders, clean-sweep assemblies and quick-change housings")
    P("Giá đỡ hai mặt bích phẳng ban đầu làm đĩa dễ bị cắt ở cạnh sắc của "
      "mặt bích trên và trượt giữa hai mặt phẳng. Bo tròn góc trong khắc phục "
      "cắt; đế côn 30° kẹp đĩa giữa hai mặt khắc phục trượt (Hình 6-29). "
      "Siết quá lực làm mỏng lá hoặc biến dạng môi côn, nên phải tuân mô-men "
      "nhà chế tạo; vòng gia cố bảo vệ mép đĩa mỏng. Cấu hình phẳng có rãnh "
      "vẫn thông dụng ở châu Âu và Viễn Đông cho áp thấp. Đĩa vòm ngược chịu "
      "nén nên không trượt; mặt đế có thể phẳng, nhưng cạnh đỡ không được làm "
      "biến dạng vòm hay mép vòm.",
      "Early flat-faced holders cut discs on the sharp upper edge and allowed "
      "slippage and leakage. Radiusing the inside corner solved cutting; a "
      "30-degree conical seat wedges the disc and solved slippage "
      "(Figure 6-29). Overtightening can thin foils or deform the conical "
      "lip, so maker torque must be observed and stiffening rings protect "
      "fragile edges. Flat seats with tongue and groove remain common in "
      "Europe and the Far East for low pressure. Reverse-buckling discs do "
      "not slip under compression and may use flat faces, but supporting "
      "edges must not deform the dome or its edge.")
    FIG(29, F12.fig_vsh_6_29())
    P("Cụm quét sạch hay T nhớt (Hình 6-30) dùng khi chất nhớt dễ tích tụ làm "
      "tắc đường chảy; dòng quét ngang qua nhánh đĩa làm giảm vấn đề này. "
      "Vỏ thay nhanh (Hình 6-31, 6-32) cho phép thay đĩa đã vỡ nhanh chóng, "
      "bằng tay hoặc bằng cơ cấu khí nén dạng cổng trượt. O-ring trong vỏ "
      "làm kín đĩa đã định vị; khi khôi phục áp hệ thống, O-ring tạo liên "
      "khóa mạnh giữa vỏ và giá đỡ.",
      "The clean-sweep or viscous Tee assembly (Figure 6-30) serves services "
      "where viscous product could build up and plug the passage; the "
      "sweeping main flow reduces this problem. Quick-change housings "
      "(Figures 6-31, 6-32) allow rapid replacement by hand or by a "
      "pneumatic sliding gate. O-rings seal the positioned disc, and once "
      "system pressure is restored they form a powerful interlock between "
      "housing and disc holders.")
    FIG(30, F12.fig_vsh_6_30())
    FIG(31, F12.fig_vsh_6_31())
    FIG(32, F12.fig_vsh_6_32())
    P("Phụ kiện thường gặp gồm jackscrew để tách mặt bích mang giá đỡ khỏi "
      "đường xả được đỡ riêng, eyebolt để nâng giá nặng, tản lưu hướng dòng "
      "xả bảo vệ nhân sự và hấp thụ lực phản hồi, cùng bộ báo vỡ phát tín "
      "hiệu nhìn hoặc nghe tại chỗ hoặc từ xa, có thể an toàn nội tại trong "
      "môi trường nổ.",
      "Common accessories include jackscrews to separate the holder flange "
      "from a separately supported discharge pipe, eyebolts for lifting "
      "heavy holders, baffle plates that deflect discharge to protect "
      "personnel and absorb reaction force, and burst indicators giving "
      "local or remote visible or audible signals, optionally intrinsically "
      "safe in explosive atmospheres.")
    P("Cụm hai đĩa (Hình 6-33) được dùng trong dịch vụ ăn mòn để báo rò do "
      "đĩa phía sản phẩm bị thủng, hoặc làm cơ cấu mở nhanh. Khoảng giữa hai "
      "đĩa cần thiết bị báo gồm van dòng vượt và đồng hồ áp: nếu đĩa thứ nhất "
      "rò sớm, áp trong khoảng tăng và thiết bị báo hoạt động. Nếu không chấp "
      "nhận được khả năng đĩa thứ hai cũng vỡ, áp vỡ của nó phải được nâng "
      "và cần thảo luận với nhà chế tạo.",
      "Double-disc assemblies (Figure 6-33) warn of product leakage from "
      "corrosion of the process-side disc or act as quick-opening devices. "
      "The interspace needs a telltale device, commonly an excess-flow valve "
      "and pressure gauge: a pinhole in the first disc raises interspace "
      "pressure and actuates the warning. If premature failure of the second "
      "disc cannot be accepted, its burst pressure must be raised after "
      "discussion with the manufacturer.")
    FIG(33, F12.fig_vsh_6_33())

    # ================================================================== table
    H("Bảng tóm tắt các cấu tạo trong đơn vị", "Constructions in this unit")
    b.append(table(
        ["Hình", "Cấu tạo", "Đặc điểm chính"]
        if vi else ["Figure", "Construction", "Key feature"],
        [
            ["6-1", "Quan hệ nhiệt độ/áp vỡ" if vi else "Temperature/burst chart",
             "Đường xuân theo vật liệu" if vi else "Qualitative by material"],
            ["6-2", "Tấm chắn nhiệt len silica" if vi else "Silica-wool heat shield",
             "Chỉ khí khô, phân mảnh khi vỡ"
             if vi else "Dry gas only, fragments on burst"],
            ["6-3", "Đĩa vòm thuận rắn" if vi else "Solid forward-domed disc",
             "Mỏng tâm, vỡ phân mảnh"
             if vi else "Centre thinning, fragmented burst"],
            ["6-4…6-6", "Giá chống chân không và vết lưng rùa"
             if vi else "Vacuum supports and turtle backing",
             "Giá khít; vết nhăn khi giá kém"
             if vi else "Close fit; wrinkles if unsupported"],
            ["6-7…6-8", "Vỡ trong lỏng và đĩa áp thấp"
             if vi else "Liquid burst and low-pressure disc",
             "Nắp bảo vệ và giá tích hợp"
             if vi else "Protective cap and integral support"],
            ["6-9", "Vòm thuận có khe và lót" if vi else "Slotted lined forward dome",
             "Ba lớp: vòm, kín, giá" if vi else "Dome, seal and support layers"],
            ["6-10…6-11", "Vạch cắt chéo" if vi else "Cross-scored discs",
             "Tỉ lệ vận hành 80–85%, chống trùng hợp"
             if vi else "80–85% ratio, polymerization service"],
            ["6-12…6-13", "Đĩa phẳng có khe và lót"
             if vi else "Slotted lined flat discs",
             "Seal môi trường hoặc áp thấp"
             if vi else "Environmental seal or low pressure"],
            ["6-14…6-15", "Dao cắt và vòng răng" if vi else "Knife blades and teeth ring",
             "Cắt đĩa khi vòm ngược"
             if vi else "Cut the disc on reversal"],
            ["6-16…6-19", "Vạch cắt chéo và ngoại vi"
             if vi else "Cross and partial scores",
             "Mở theo vạch, đục lỗ áp thấp"
             if vi else "Predictable opening, low-pressure perforations"],
            ["6-20", "Đĩa trượt ra" if vi else "Slip-away disc",
             "Đẩy khỏi giá, tới 95%"
             if vi else "Expelled from holder, up to 95%"],
            ["6-21", "Thanh uốn kết hợp khe và lót"
             if vi else "Slotted lined disc with buckling bars",
             "Zero manufacturing range, ±2%"
             if vi else "Zero range, ±2% tolerance"],
            ["6-22…6-23", "Đĩa hai chiều" if vi else "Two-way discs",
             "Thuận một chiều, ngược chiều kia"
             if vi else "Forward one way, reverse the other"],
            ["6-24…6-25", "Graphite monoblock" if vi else "Monoblock graphite",
             "Không gia cố hoặc vòng thép"
             if vi else "Unarmored or steel-armored"],
            ["6-26", "Graphite hai chiều" if vi else "Two-way graphite",
             "Tối đa 10 bar mỗi chiều" if vi else "10 bar maximum each way"],
            ["6-27", "Màng graphite thay được" if vi else "Replaceable graphite membrane",
             "Hốc định sâu, không nhạy mô-men"
             if vi else "Controlled recess, torque-insensitive"],
            ["6-28", "Vòm ngược graphite nguyên chất"
             if vi else "Pure-graphite reverse dome",
             "Lên tới ~550 °C" if vi else "Up to about 550 °C"],
            ["6-29", "Giá đỡ 30°" if vi else "Conical holder seat",
             "Kẹp đĩa, tránh trượt"
             if vi else "Wedges disc, prevents slip"],
            ["6-30", "Cụm quét sạch" if vi else "Clean-sweep Tee",
             "Dòng ngang hạn chế tắc nhớt"
             if vi else "Sweeping flow limits build-up"],
            ["6-31…6-32", "Vỏ thay nhanh" if vi else "Quick-change housings",
             "Bằng tay hoặc khí nén"
             if vi else "Manual or pneumatic actuation"],
            ["6-33", "Cụm hai đĩa" if vi else "Double-disc assembly",
             "Báo rò bằng đồng hồ và van dòng vượt"
             if vi else "Gauge and excess-flow warning"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 227–260, "
                 "Hình 6-1…6-33." if vi else
                 "Summary from source text, book pp. 227–260, "
                 "Figures 6-1…6-33."),
        cls="tbl wide"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
