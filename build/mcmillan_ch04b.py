# -*- coding: utf-8 -*-
"""Chapter 4, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 102-106 (PDF pp. 123-127).

Continuation of Section 4.1: the jet geometry of Fig. 4.2, the
direction-of-jet rule, the composite solution for an obstruction with
Eqs. 4.8-4.12, and the ground-proximity and density corrections. Section
4.1.1 then works Examples 1 and 2, including the printed inconsistencies
which are flagged in notes rather than silently corrected.

Module A opens the Section 4.1 heading and owns Eqs. 4.1-4.7 and Fig. 4.1.
This module therefore does not repeat that heading. The integration module
owns the page shell, source-page count, references, glossary terms, closing
note and legal line.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h4, p, note, eq, fig

import mcmillanfig04_a as F


def body_vi():
    b = []
    b.append(p("Phạm vi tính toán nằm theo hướng của tia phun, do đó nếu hướng tia "
               "được xác định chắc chắn thì khu vực nguy hiểm có thể được xác định "
               "như Hình 4.2. Điều này chỉ đúng khi gió không đóng vai trò nào "
               "(áp suất trên áp suất tới hạn và không có vật cản) và khi hướng "
               "tia có thể xác định với độ tin cậy cao."))
    b.append(fig(2, F.fig_f402()))
    b.append(p("Tuy nhiên, do những yếu tố bất định có thể xuất hiện, người ta cho "
               "rằng trừ khi có mức độ tin cậy cao, khu vực nguy hiểm luôn phải là "
               "một hình cầu có bán kính bằng khoảng cách tới giới hạn nổ dưới "
               "(LEL), lấy điểm rò làm tâm."))
    b.append(p("Một vấn đề khác phát sinh khi phát thải ở áp suất trên áp suất tới "
               "hạn và có một vật cản ở khoảng cách nhỏ hơn khoảng cách tới LEL "
               "xác định theo Phương trình 4.6. Khi đó cần một lời giải tổng hợp. "
               "Vì quan hệ giữa khoảng cách từ điểm phát thải và nồng độ là tuyến "
               "tính (xem Phương trình 4.6), có thể dùng Phương trình 4.8 để xác "
               "định phần trăm khí hoặc hơi dễ cháy trong hỗn hợp tại điểm vật cản. "
               "(Điều này tất nhiên chỉ cần thiết ở áp suất trên áp suất tới hạn.)"))
    b.append(eq("B = 100 − L[(100 − LEL)/X] %", "4.8"))
    b.append(p("trong đó B = phần trăm khí hoặc hơi trong không khí; L = khoảng "
               "cách tới vật cản, m; X = khoảng cách tới LEL, m."))
    b.append(p("Vì đã biết tỷ lệ thể tích, có thể tính một khối lượng phân tử hiệu "
               "dụng mới cho hỗn hợp như sau:"))
    b.append(eq("M(Mixture) = [M(Gas) × %(Gas)/100] + "
                "[M(Air) × %(Air)/100]", "4.9"))
    b.append(p("Đối với phép tính này, khối lượng phân tử của không khí có thể "
               "lấy bằng 29."))
    b.append(p("Giờ có thể tính giá trị G của hỗn hợp bằng cách dùng lượng khí "
               "phát thải ban đầu cộng với lượng không khí có trong hỗn hợp tại "
               "điểm vật cản."))
    b.append(eq("V(Gas) = 0.082 G T/M(Gas) m³/s"))
    b.append(eq("V(Mixture) = V(Gas) × "
                "[100/% Gas in Mixture] m<sup>3</sup>", "4.10"))
    b.append(eq("G(Mixture) = V(Mixture) × "
                "12.19 M(Mixture)/T kg", "4.11"))
    b.append(p("Cần tính một giới hạn nổ dưới (LEL) mới cho hỗn hợp, thực hiện "
               "đơn giản bằng phép tính sau:"))
    b.append(eq("LEL(Mixture) = LEL(Gas) × "
                "[100/% Gas in Mixture] %", "4.12"))
    b.append(p("Các giá trị mới này sau đó được thay vào Phương trình 4.7 để tính "
               "khoảng cách tới mép khu vực nguy hiểm. Khoảng cách này, cộng với "
               "khoảng cách giữa điểm phát thải và vật cản, sẽ xác định phạm vi "
               "khu vực nguy hiểm theo hướng của vật cản."))
    b.append(p("Một vấn đề khác xảy ra khi điểm phát thải gần mặt đất, vì sự phân "
               "tán bị ảnh hưởng. Không có quy trình toán học để xác định chính "
               "xác ảnh hưởng này, nhưng các cách xử lý điển hình sau đây được "
               "áp dụng."))
    b.append(p("Thứ nhất, bất kể áp suất phát thải (trên hay dưới áp suất tới hạn), "
               "nếu giới hạn dưới của bầu khí quyển nổ cách mặt đất chưa tới 3 m "
               "thì trong mọi trường hợp phải dùng Phương trình 4.7 để tính phạm "
               "vi khu vực nguy hiểm và chiếu các giới hạn ngang xuống mặt đất "
               "(Chương 3 trình bày chi tiết hơn)."))
    b.append(p("Thứ hai, khi điểm thấp nhất của bầu khí quyển nổ nằm trong vòng "
               "1.5 m tính từ mặt đất, phải dùng phương trình phát thải trôi theo "
               "gió (Phương trình 4.7) và lại chiếu các mép của bầu khí quyển nổ "
               "xuống mặt đất, nhưng trong trường hợp này diện tích tiếp xúc với "
               "mặt đất phải nhân với 1.5 (Chương 3 trình bày chi tiết hơn)."))
    b.append(p("Thứ ba, khi điểm thấp nhất của bầu khí quyển nổ chạm mặt đất, phạm "
               "vi khu vực nguy hiểm lấy bằng kết quả của phương trình trôi "
               "(Phương trình 4.7) nhân với 1.5 để tính đến ảnh hưởng làm méo dạng "
               "của mặt đất đối với sự phân tán khí theo mọi hướng (Chương 3 "
               "trình bày chi tiết hơn)."))
    b.append(p("Cách tiếp cận tính toán trên về cơ bản xử lý được mọi tình huống "
               "bình thường về phát thải khí hoặc hơi, miễn là khí hoặc hơi đó có "
               "tỷ trọng không khác biệt lớn so với không khí. Đối với phát thải "
               "âm thanh không bị cản, do đó dùng Phương trình 4.1 và 4.6, ảnh "
               "hưởng của tỷ trọng không đáng kể trong hầu hết trường hợp bình "
               "thường (kể cả hydrogen), vì năng lượng của dòng khí do vận tốc "
               "của nó sẽ khắc phục mọi ảnh hưởng đáng kể của sự khác biệt tỷ "
               "trọng. Nhưng khi phát thải trở nên dưới âm thanh (thường là các "
               "trường hợp dùng Phương trình 4.3 và 4.7), sự khác biệt tỷ trọng "
               "ngày càng trở nên quan trọng."))
    b.append(p("Khó xác định chính xác ảnh hưởng này, nhưng theo quy tắc kinh "
               "nghiệm, phạm vi thẳng đứng của bầu khí quyển nổ phải được nhân đôi "
               "bất cứ khi nào tỷ trọng lớn hơn 1.5 lần tỷ trọng không khí hoặc "
               "nhỏ hơn 0.7 lần tỷ trọng không khí. Điều này có nghĩa, chẳng hạn, "
               "nhân đôi phạm vi phía trên đối với các khí như hydrogen và nhân "
               "đôi phạm vi phía dưới đối với các khí như pentane — điều này áp "
               "dụng cho hầu hết các khí hydrocarbon."))

    b.append(h4("4.1.1 Các ví dụ về phát thải khí và hơi",
                "4.1.1 Examples of gas and vapour release"))
    b.append(p("<b>Ví dụ 1.</b> Gioăng mặt bích của một đường ống bị hỏng, tạo lỗ "
               "tiết 4 × 10⁻⁵ m². Khí chứa trong ống là ethylene (M = 28) và áp "
               "suất bên trong ống là 4 × 10⁵ N/m². Nhiệt độ môi trường là 22 °C; "
               "khí trong ống ở nhiệt độ môi trường. Giả sử không thể xác định "
               "chắc chắn hướng của tia phun, khu vực nguy hiểm bao quanh mối nối "
               "đường ống sẽ như thế nào? Giới hạn nổ dưới của ethylene trong "
               "không khí ở 22 °C và áp suất khí quyển là 2.7 %."))
    b.append(p("Vì áp suất phát thải vượt quá áp suất tới hạn, áp dụng Phương "
               "trình 4.1:"))
    b.append(eq("G = 0.006 × 4 × 10<sup>−5</sup> × 3 × 10<sup>5</sup> "
                "(28/295)<sup>0.5</sup> kg/s = 0.03 kg/s"))
    b.append(p("Sự phân tán do chính năng lượng của tia, nên khoảng cách tới LEL "
               "là (Phương trình 4.6):"))
    b.append(eq("X = 2.1 × 10<sup>3</sup> (0.03/2.7<sup>2</sup> × "
                "28<sup>1.5</sup> × 295<sup>0.5</sup>)<sup>0.5</sup> m = 2.7 m"))
    b.append(p("Khu vực nguy hiểm sẽ là một hình cầu lan rộng 2.7 m từ nguồn phát "
               "thải theo mọi hướng."))
    b.append(note("<b>Sự không nhất quán trong Ví dụ 1 (giá trị nguồn).</b> Ví dụ "
                  "nêu áp suất trong ống là 4 × 10⁵ N/m² nhưng khi thay số lại "
                  "dùng 3 × 10⁵ N/m²; chỉ giá trị 4 × 10⁵ mới cho kết quả "
                  "0.03 kg/s như đã in. Cả hai giá trị đều được giữ nguyên như "
                  "trong bản gốc."))
    b.append(p("<b>Ví dụ 2.</b> Có một vật cản ở khoảng cách ngang 1 m từ vị trí "
               "rò rỉ trong Ví dụ 1. Phạm vi khu vực nguy hiểm sẽ là bao nhiêu? "
               "Lượng phát thải theo khối lượng vẫn là 0.03 kg/s như ví dụ thứ "
               "nhất, và cần tính lượng khí trong hỗn hợp tại vật cản như sau:"))
    b.append(p("Dùng Phương trình 4.8:"))
    b.append(eq("B = 100 − (100 − 2.7) × 1/2.7 = 64 %"))
    b.append(p("Tốc độ phát thải thể tích của khí tại điểm rò là (Phương trình "
               "4.4):"))
    b.append(eq("V = 0.082 × 0.03 × 295/28 = 0.026 m³/s"))
    b.append(p("Thể tích của hỗn hợp khí/không khí tại điểm vật cản là (Phương "
               "trình 4.10):"))
    b.append(eq("V<sub>m</sub> = 0.026 × 100/57.7 = 0.04 m³/s"))
    b.append(p("Khối lượng phân tử của hỗn hợp tại điểm vật cản cần được tính như "
               "sau (Phương trình 4.9):"))
    b.append(eq("M<sub>m</sub> = [28 × (64/100)] + [27 × (36/100)] = 27.6"))
    b.append(p("Sắp xếp lại Phương trình 4.4 thành Phương trình 4.10, khối lượng "
               "hỗn hợp tại điểm vật cản là:"))
    b.append(eq("G<sub>m</sub> = 0.04 × 12.19 × 27.6/295 = 0.04 kg/s"))
    b.append(p("Ngoài ra, LEL mới cần được tính như sau (Phương trình 4.12):"))
    b.append(eq("LEL<sub>m</sub> = 2.7 × (100/57.7) = 4.68 %"))
    b.append(p("Có thể thay các giá trị trên vào Phương trình 4.7 để tính phạm vi "
               "khu vực nguy hiểm phía sau vật cản:"))
    b.append(eq("X<sub>m</sub> = 10.8 (0.046 × 295/27.6 × 4.21)<sup>0.55</sup> "
                "m = 3.3 m"))
    b.append(p("Do đó, theo hướng của vật cản, khu vực nguy hiểm sẽ lan rộng tới "
               "4.3 m từ nguồn rò rỉ (= 1 + 3,3), và 3.3 m lên phía trên và phía "
               "dưới vật cản nếu giá trị này lớn hơn phạm vi thẳng đứng suy từ "
               "phát thải cơ bản không xét đến vật cản (xem Phương trình 4.7). "
               "Không cần điều chỉnh theo tỷ trọng tương đối, nhưng phải tính đến "
               "mọi ảnh hưởng do gần mặt đất."))
    b.append(note("<b>Sự không nhất quán trong Ví dụ 2 (giá trị in).</b> Phương "
                  "trình 4.8 cho B = 64 %, nhưng các bước tính V<sub>m</sub> và "
                  "LEL<sub>m</sub> lại dùng 57.7 % (100/57.7); Phương trình 4.11 "
                  "cho G<sub>m</sub> = 0.04 kg/s nhưng phép thay vào Phương trình "
                  "4.7 dùng 0.046 kg/s. Kết quả in cũng trộn 3.3 m (phạm vi sau "
                  "vật cản và phạm vi thẳng đứng) với tổng 4.3 m (= 1 + 3,3) theo "
                  "hướng vật cản."))
    return "".join(b)


def body_en():
    b = []
    b.append(p("The calculated extent is in the direction of the jet, so if the "
               "jet direction is known the hazardous area can be defined as in "
               "Fig. 4.2. This is only true where the wind does not play a part "
               "(above the critical pressure with no obstructions) and where the "
               "jet direction can be defined with confidence."))
    b.append(fig(2, F.fig_f402()))
    b.append(p("Because of the unknown factors likely to come into play, it is, "
               "however, felt that unless a high degree of confidence exists, "
               "the hazardous area should always be a sphere of radius equal to "
               "the distance to the lower explosive limit, centred on the leak."))
    b.append(p("A further problem occurs where the release is at a pressure above "
               "the critical pressure and an obstruction is present at a distance "
               "less than the distance to the lower explosive limit determined "
               "from Equation 4.6. A composite solution is then necessary. Since "
               "the relationship between distance from the release and "
               "concentration is linear (see Equation 4.6), Equation 4.8 can be "
               "used to determine the percentage of flammable gas or vapour in "
               "the mixture at the point of obstruction. (This is, of course, "
               "only necessary at pressures above the critical pressure.)"))
    b.append(eq("B = 100 − L[(100 − LEL)/X] %", "4.8"))
    b.append(p("where B = percentage of gas or vapour in air; L = distance to "
               "obstruction, m; X = distance to the lower explosive limit, m."))
    b.append(p("As the volume ratio is now known, a new effective molecular "
               "weight can be calculated for the mixture as follows:"))
    b.append(eq("M(Mixture) = [M(Gas) × %(Gas)/100] + "
                "[M(Air) × %(Air)/100]", "4.9"))
    b.append(p("For this calculation the molecular weight of air can be taken "
               "as 29."))
    b.append(p("A figure for G of the mixture can now be calculated using the "
               "original released mass of gas plus the mass of air included in "
               "the mixture at the point of obstruction."))
    b.append(eq("V(Gas) = 0.082 G T/M(Gas) m³/s"))
    b.append(eq("V(Mixture) = V(Gas) × "
                "[100/% Gas in Mixture] m<sup>3</sup>", "4.10"))
    b.append(eq("G(Mixture) = V(Mixture) × "
                "12.19 M(Mixture)/T kg", "4.11"))
    b.append(p("It is now necessary to calculate a new lower explosive limit for "
               "the mixture, which can be done simply by the following "
               "calculation:"))
    b.append(eq("LEL(Mixture) = LEL(Gas) × "
                "[100/% Gas in Mixture] %", "4.12"))
    b.append(p("These new figures can then be inserted in Equation 4.7 and a "
               "distance to the edge of the hazardous area calculated. This "
               "distance, added to the distance between the point of release and "
               "the obstruction, will define the extent of the hazardous area in "
               "the direction of the obstruction."))
    b.append(p("A further problem occurs when the release is close to the ground, "
               "as the dispersion is affected. There are no mathematical "
               "procedures for determining the effects of this, but the following "
               "are typical of the procedures adopted."))
    b.append(p("First, whatever the release pressure (above or below that defined "
               "by the critical pressure ratio), provided that the lower limit of "
               "explosive atmosphere is less than 3 m from the ground then "
               "Equation 4.7 should be used in all cases for the extent of the "
               "hazardous area and the horizontal limits should be projected to "
               "the ground (Chapter 3 deals with the results of this in more "
               "detail)."))
    b.append(p("Second, where the lower extremity of the explosive atmosphere is "
               "within 1.5 m of the ground the drift release equation (Equation "
               "4.7) should be used and, again, the extremities of the explosive "
               "atmosphere projected to ground level, but in this case the ground "
               "footprint should be multiplied by 1.5 (Chapter 3 deals with the "
               "results of this in more detail)."))
    b.append(p("Third, where the lower extremity of the explosive atmosphere "
               "touches the ground the extent of the hazardous area should be "
               "that produced when the result of the drift equation (Equation "
               "4.7) is multiplied by 1.5 to take account of the distorting effect "
               "of the ground upon dispersion of gas in all directions (Chapter 3 "
               "deals with the results of this in more detail)."))
    b.append(p("The above gives a calculative approach which will effectively "
               "deal with all normal circumstances where gas or vapour is "
               "released, provided that the gas or vapour does not have a density "
               "dramatically different from air. In the case of sonic releases "
               "which are unimpeded, and therefore utilize Equations 4.1 and 4.6, "
               "density will not have a significant effect in any normal "
               "circumstance (including hydrogen), as the energy in the released "
               "gas by virtue of its velocity will overcome any significant "
               "effect of density differences. Where releases become subsonic "
               "(typically where Equations 4.3 and 4.7 are relevant), differences "
               "of density will become increasingly relevant."))
    b.append(p("It is difficult to determine the exact effect of these, but as a "
               "rule of thumb the vertical extents of explosive atmosphere should "
               "be doubled wherever the density is more than 1.5 times the "
               "density of air, or less than 0.7 times the density of air. This "
               "will mean, for instance, doubling the upward extent for such "
               "gases as hydrogen and doubling the downward direction for such "
               "gases as pentane — indeed this latter will apply for most of the "
               "hydrocarbon gases."))

    b.append(h4("4.1.1 Examples of gas and vapour release",
                "4.1.1 Examples of gas and vapour release"))
    b.append(p("<b>Example 1.</b> A pipe flange gasket fails, producing an orifice "
               "of 4 × 10⁻⁵ m². The contained gas is ethylene (M = 28) and the "
               "pressure inside the pipe is 4 × 10⁵ N/m². Ambient temperature is "
               "22 °C, and the contained gas is at ambient temperature. Assuming "
               "the jet direction cannot be defined with confidence, what will be "
               "the hazardous area surrounding the pipe joint? The lower "
               "explosive limit of ethylene in air at 22 °C and atmospheric "
               "pressure is 2.7 per cent."))
    b.append(p("The release pressure is in excess of critical pressure, so "
               "Equation 4.1 applies:"))
    b.append(eq("G = 0.006 × 4 × 10<sup>−5</sup> × 3 × 10<sup>5</sup> "
                "(28/295)<sup>0.5</sup> kg/s = 0.03 kg/s"))
    b.append(p("Dispersal is by jet energy, so the distance to the lower "
               "explosive limit is (Equation 4.6):"))
    b.append(eq("X = 2.1 × 10<sup>3</sup> (0.03/2.7<sup>2</sup> × "
                "28<sup>1.5</sup> × 295<sup>0.5</sup>)<sup>0.5</sup> m = 2.7 m"))
    b.append(p("The hazardous area will be a sphere extending 2.7 m from the "
               "source of release in all directions."))
    b.append(note("<b>Inconsistency in Example 1 (source value).</b> The example "
                  "states a pipe pressure of 4 × 10⁵ N/m² but substitutes "
                  "3 × 10⁵ N/m²; only 4 × 10⁵ reproduces the printed 0.03 kg/s. "
                  "Both values are retained exactly as printed."))
    b.append(p("<b>Example 2.</b> An obstruction is present at a horizontal "
               "distance of 1 m from the leak location described in Example 1. "
               "What will the extent of the hazardous area be? The mass release "
               "remains at 0.03 kg/s as in the first example, and it is necessary "
               "to calculate the amount of gas in the mixture at the obstruction "
               "as follows:"))
    b.append(p("Using Equation 4.8:"))
    b.append(eq("B = 100 − (100 − 2.7) × 1/2.7 = 64 %"))
    b.append(p("The volume release rate of gas at the point of leakage is "
               "(Equation 4.4):"))
    b.append(eq("V = 0.082 × 0.03 × 295/28 = 0.026 m³/s"))
    b.append(p("The volume of the gas/air mixture at the point of obstruction is "
               "(Equation 4.10):"))
    b.append(eq("V<sub>m</sub> = 0.026 × 100/57.7 = 0.04 m³/s"))
    b.append(p("The molecular weight of the mixture at the point of obstruction "
               "needs now to be calculated as follows (Equation 4.9):"))
    b.append(eq("M<sub>m</sub> = [28 × (64/100)] + [27 × (36/100)] = 27.6"))
    b.append(p("Rearranging Equation 4.4 as Equation 4.10, the mass of mixture at "
               "the point of obstruction is as follows:"))
    b.append(eq("G<sub>m</sub> = 0.04 × 12.19 × 27.6/295 = 0.04 kg/s"))
    b.append(p("In addition, the new lower explosive limit needs to be calculated "
               "as follows (Equation 4.12):"))
    b.append(eq("LEL<sub>m</sub> = 2.7 × (100/57.7) = 4.68 %"))
    b.append(p("The foregoing figures can now be inserted into Equation 4.7 to "
               "give the extent of the hazardous area beyond the obstruction:"))
    b.append(eq("X<sub>m</sub> = 10.8 (0.046 × 295/27.6 × 4.21)<sup>0.55</sup> "
                "m = 3.3 m"))
    b.append(p("The hazardous area in the direction of the obstruction will, "
               "therefore, extend to 4.3 m from the source of leakage (= 1 + 3.3), "
               "and vertically upwards and downwards from the obstruction for "
               "3.3 m if this is larger than the vertical extent derived from the "
               "basic release ignoring the effect of the obstruction (see "
               "Equation 4.7). No adjustment for relative density is necessary, "
               "but any effects due to ground proximity need to be taken into "
               "account."))
    b.append(note("<b>Inconsistency in Example 2 (printed values).</b> Equation "
                  "4.8 gives B = 64 %, but the steps for V<sub>m</sub> and "
                  "LEL<sub>m</sub> use 57.7 % (100/57.7); Equation 4.11 gives "
                  "G<sub>m</sub> = 0.04 kg/s but the substitution into Equation "
                  "4.7 uses 0.046 kg/s. The printed answer also mixes 3.3 m (the "
                  "extent beyond the obstruction and the vertical extent) with "
                  "the total of 4.3 m (= 1 + 3.3) toward the obstruction."))
    return "".join(b)
