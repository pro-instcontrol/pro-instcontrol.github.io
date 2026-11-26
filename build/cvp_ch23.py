# -*- coding: utf-8 -*-
"""Book 7, Chapter 23 - Flashing / Hóa hơi (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
145-146 (PDF pp. 143-144; printed = PDF + 2). Two printed pages, one figure
(a photograph in the source, redrawn here as a vector schematic), one sizing
relation with its liquid-pressure-recovery modifier, a worked example and
the recommendation to discharge into a flash tank or open air.

The OCR text layer garbles the exponent placement in the sizing formula;
the printed forms and the example were transcribed from pypdfium2 renders
of both pages. The printed example states Cv = 117 although substituting
its own numbers gives about 41.6; the English text keeps the printed
result, while the Vietnamese text and a note flag the discrepancy.
"""
from cvp_common import eq, fig, h2, h3, lead, note, p, ul

import cvpfig23 as F

PAGES_SRC = 2
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Flashing"
TITLE_VI = "Hóa hơi (flashing)"


def note_terms(lang):
    """One-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 23.</b> hóa hơi (flashing) · áp suất hơi P<sub>v</sub> "
                "· áp suất đầu ra · áp suất chân không · hơi hòa tan · hơi chưa hòa tan "
                "· xâm thực (cavitation) · dòng nghẽn (choked flow) · tốc độ hỗn hợp "
                "nước/hơi · cột áp tốc độ · bể hóa hơi (flash tank) · xả trực tiếp ra "
                "không khí · hệ số lưu lượng C<sub>v</sub> · lưu lượng Q (gpm) · "
                "áp suất đầu vào tuyệt đối P<sub>1</sub> (psia) · hệ số áp suất hơi "
                "F<sub>f</sub> · áp suất tới hạn P<sub>c</sub> = 3206 psia · hệ số "
                "phục hồi áp suất F<sub>L</sub> · van bi lệch tâm 3 inch")
    return ("<b>Key terms.</b> flashing · vapor pressure P<sub>v</sub> · outlet pressure · "
            "vacuum · dissolved vapor · undissolved vapor · cavitation · choked flow · "
            "water/vapor mixture velocity · velocity head · flash tank · discharge to "
            "open air · flow coefficient C<sub>v</sub> · flow rate Q (gpm) · absolute "
            "inlet pressure P<sub>1</sub> (psia) · vapor-pressure factor F<sub>f</sub> · "
            "critical pressure P<sub>c</sub> = 3206 psia · pressure recovery factor "
            "F<sub>L</sub> · 3-inch eccentric ball valve")


def body_vi():
    b = []
    b.append(lead("Hóa hơi là điều kiện dòng chất lỏng mà áp suất ở cửa ra giảm xuống "
                  "bằng hoặc thấp hơn áp suất hơi của chất lỏng. Hình hơi sinh ra "
                  "trong giai đoạn vận tốc cao vẫn hòa tan trong dòng, vì không có "
                  "đủ chênh áp để gây xâm thực."))

    b.append(h2("Định nghĩa và cơ chế", "Definition and mechanism"))
    b.append(p("Hình 23-1 cho thấy tia nước thoát ra từ cửa ra của van. Ảnh gốc cho "
               "thấy rõ hơi chưa hòa tan trộn với nước; khi ra tới không khí tự do, "
               "hơi này sẽ hòa tan trở lại vào nước mà không gây hại. Mức ồn của "
               "hỗn hợp này là ồn rối, có thể ước tính bằng tỷ số giảm áp bằng 1. "
               "Hóa hơi xảy ra bất cứ khi nào áp suất phía dưới là chân không hoặc "
               "bằng áp suất hơi của chất lưu cụ thể."))
    b.append(fig(1, F.fig_f231()))
    b.append(p("Bản thân hóa hơi không gây hư hỏng, trừ khi áp suất ngược sinh ra "
               "do vận tốc cao của hỗn hợp nước/hơi lại gây xâm thực. Giả sử áp "
               "suất phía dưới là 7,75 psia (0,5 bara). Trong điều kiện đó lượng "
               "hơi nước cuốn theo chiếm 5% tổng khối lượng, tức tỷ lệ nước trên "
               "hơi là 290:1. Tổng khối lượng chảy vì thế gấp khoảng 14 lần khối "
               "lượng chất lỏng riêng. Nếu vận tốc chất lỏng bình thường trong "
               "ống là 10 ft/s (3 m/s), vận tốc hỗn hợp nước/hơi tăng lên 140 ft/s "
               "(42 m/s), tạo cột áp tốc độ khoảng 8 psi (0,6 bara). Cộng với "
               "chân không 7,75 psia, điều này có thể gây xâm thực trong ống hạ "
               "lưu hoặc ngay tại cửa ra van."))
    b.append(p("Quá trình này thường bị hiểu nhầm và hóa hơi bị đổ lỗi cho hư hỏng "
               "do xâm thực. Để tránh điều đó, luôn lắp cửa ra van trực tiếp vào "
               "bể hóa hơi hoặc xả ra không khí tự do, và tránh mọi đoạn ống hạ "
               "lưu. Ở đó hơi vẫn ở trạng thái hòa tan; do áp suất khí quyển hoặc "
               "chân không không có đủ chênh áp để hơi implode."))

    b.append(h2("Định cỡ trong điều kiện hóa hơi", "Sizing for flashing conditions"))
    b.append(eq("C<sub>v</sub> = Q / [(P<sub>1</sub> − P<sub>v</sub> × F<sub>f</sub>)<sup>0,5</sup> / F<sub>L</sub>]"))
    b.append(p("Trong đó Q là lưu lượng tính bằng gpm, P<sub>1</sub> là áp suất đầu "
               "vào tuyệt đối tính bằng psia, và P<sub>c</sub> = 3206 psia. Hệ số "
               "áp suất hơi được tính theo:"))
    b.append(eq("F<sub>f</sub> = 0,96 − 0,28 (P<sub>v</sub> / P<sub>c</sub>)<sup>0,5</sup> P<sub>v</sub>"))
    b.append(h3("Ví dụ", "Example"))
    b.append(p("Cho Q = 500 gpm, P<sub>1</sub> = 60 psia, P<sub>v</sub> = 10 psia, "
               "P<sub>c</sub> = 3206 psia và F<sub>L</sub> = 0,6. Thay vào công thức:"))
    b.append(eq("C<sub>v</sub> = 500 / {(60 − 10 × (0,96 − 0,28 (10 / 3206)<sup>0,5</sup> "
                "× 10))<sup>0,5</sup> / 0,6}"))
    b.append(p("Nguyên bản nêu C<sub>v</sub> = 117 và kết luận có thể dùng van bi "
               "lệch tâm 3 inch. Tuy nhiên, thay trực tiếp các số liệu in trong "
               "công thức trên cho kết quả khoảng 41,6; con số 117 của nguyên bản "
               "được giữ nguyên trong bản Anh, còn bản Việt nêu rõ sự sai lệch này."))
    b.append(note("<b>Lưu ý về nguyên bản.</b> Lớp văn bản OCR làm sai vị trí số mũ "
                  "trong công thức định cỡ; công thức và ví dụ ở đây được đọc lại "
                  "từ ảnh trang in 145–146. Ảnh hóa hơi trong sách được vẽ lại "
                  "thành sơ đồ vector với cửa ra, tia nước và hòa tan hơi trong "
                  "không khí. Phép tính ví dụ in ra C<sub>v</sub> = 117, nhưng "
                  "thay số theo công thức in cho khoảng 41,6; bản Anh giữ nguyên "
                  "kết quả in, bản Việt dùng giá trị suy ra từ công thức."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. "
               "Nội dung gốc © 2011 Hans D. Baumann, xuất bản bởi ISA / "
               "John Wiley &amp; Sons.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(lead("Flashing is defined as a liquid flow condition where the outlet "
                  "pressure drops at, or below, the vapor pressure of the liquid. "
                  "The vapor created during the high-velocity phase remains "
                  "dissolved, lacking the necessary pressure differential to "
                  "cause cavitation."))
    b.append(h2("Definition and mechanism", "Definition and mechanism"))
    b.append(p("Figure 23-1 shows a water jet exiting a valve outlet. The photograph "
               "clearly shows the undissolved vapor mixed with the water. This "
               "vapor will later harmlessly dissolve back into water in the open "
               "air. The sound level of such a mixture is turbulent and can be "
               "estimated using the pressure drop ratio of 1. Flashing will occur "
               "whenever the downstream pressure is in a vacuum or at the vapor "
               "pressure of a specific fluid."))
    b.append(fig(1, F.fig_f231()))
    b.append(p("Flashing poses no problem except when the resultant backpressure "
               "due to the high velocity of the water/vapor pressure causes "
               "cavitation. Assume that the downstream pressure is 7.75 psia "
               "(0.5 bara). Under these conditions, the amount of entrained water "
               "vapor is 5% of the total mass. The result is that the ratio "
               "between the water and vapor is 290:1. Ts means that the total "
               "flowing mass is 14 times that of the liquid alone. Assuming that "
               "the normal liquid pipe velocity is 10 ft/s (3 m/s), the combined "
               "water/vapor velocity increases to 140 ft/s (42 m/s). The resultant "
               "velocity head of this mixture now is 8 psi (0.6 bara). This, "
               "together with the 7.75 psia vacuum, can cause cavitation either in "
               "the downstream pipe or at the valve outlet."))
    b.append(p("Unfortunately, this process has often been misunderstood and "
               "flashing has been blamed for the resultant damage. To prevent "
               "this from happening, always mount the valve outlet directly on a "
               "flash tank or in the open and avoid all downstream piping. Here, "
               "water vapor stays in the solution. Because of the atmospheric "
               "pressure or vacuum, there is not enough pressure differential to "
               "cause the vapor to implode."))
    b.append(h2("How to size for flashing conditions", "How to size for flashing conditions"))
    b.append(eq("C<sub>v</sub> = Q / [(P<sub>1</sub> − P<sub>v</sub> × F<sub>f</sub>)<sup>0.5</sup> / F<sub>L</sub>]"))
    b.append(ul(["Q = gpm", "P<sub>1</sub> = psia",
                 "F<sub>f</sub> = 0.96 − 0.28 (P<sub>v</sub> / P<sub>c</sub>)<sup>0.5</sup> P<sub>v</sub>",
                 "P<sub>c</sub> = 3206 psia"]))
    b.append(h3("Example", "Example"))
    b.append(p("Q = 500 gpm, P<sub>1</sub> = 60 psia, P<sub>v</sub> = 10 psia, "
               "P<sub>c</sub> = 3206 psia, F<sub>L</sub> = 0.6."))
    b.append(eq("C<sub>v</sub> = 500 / {(60 − 10 × (0.96 − 0.28 (10 / 3206)<sup>0.5</sup> "
                "× 10))<sup>0.5</sup> / 0.6}"))
    b.append(eq("C<sub>v</sub> = 117"))
    b.append(p("A 3-inch eccentric ball valve could be used."))
    b.append(note("<b>Source quirks.</b> The OCR text layer garbles the exponent "
                  "placement in the sizing relation; the formula and example here "
                  "were re-read from the rendered printed pages 145-146. The "
                  "printed photograph of flashing was redrawn as a vector "
                  "schematic with the outlet, the two-phase jet and the vapor "
                  "redissolving in open air. The printed example states C<sub>v</sub> "
                  "= 117, but substituting its own figures into the printed "
                  "relation gives about 41.6; the printed result is retained."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © 2011 Hans D. Baumann, published by ISA / John Wiley "
               "&amp; Sons.</i>"))
    return "".join(b)
