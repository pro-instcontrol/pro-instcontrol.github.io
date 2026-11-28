# -*- coding: utf-8 -*-
"""Chapter 11, module D - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 290-292 (PDF pp. 311-313).

Covers Section 11.5.2 Ducting from its heading through the paragraph that
introduces Table 11.2. The spark/particle-arrester material (Table 11.2,
the spark-arresting-devices paragraph and Fig. 11.7) and Section 11.5.3
belong to module E. Figures 11.4-11.6 are inserted at their printed
positions, including the mid-paragraph placements caused by the page
breaks between printed pp. 290, 291 and 292.

Printed quirks are kept in the English text (the 'Which makes matters
very difficult...' fragment and the long, loosely joined condition for a
spark/particle device) with bilingual notes. The pressure unit is kept as
'50 N/m²' in the notes. The chapter shell owns the chapter h2, the
references and the end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, fig
import mcmillanfig11 as F


def body_vi():
    b = []

    # Printed p.290. Section 11.5.2 opens here; the tail of 11.5.1 that
    # precedes it on this page belongs to module C.
    b.append(h4("11.5.2 Ống dẫn", "11.5.2 Ducting"))
    b.append(p("Vì ống dẫn là một phần của vỏ bọc, nó cần đáp ứng các yêu cầu "
               "như đối với vỏ bọc. Với việc dùng khí nén, điều này không "
               "thành vấn đề vì các ống dẫn sẽ ngắn, chỉ nằm trong khu vực "
               "của vỏ bọc (xem Hình 11.4) – việc cấp khí tới điểm đó thường "
               "là qua đường ống khí nén, còn ống dẫn đầu ra thì ngắn vì nó "
               "xả vào vùng nguy hiểm. (Không được phép để ống dẫn đầu ra xả "
               "vào vùng không nguy hiểm, vì làm như vậy sẽ biến nơi đó thành "
               "vùng nguy hiểm). Vì vậy, trong những trường hợp này, mọi "
               "đường ống và ống dẫn đều ở áp suất cao hơn áp suất khí quyển "
               "và các ống dẫn có thể tạo thành một phần của thiết bị."))
    b.append(p("Khi khí bảo vệ là không khí và được cấp bằng quạt (điều này "
               "thường không thể áp dụng với khí trơ), có hai khả năng. Thứ "
               "nhất, quạt và đoạn ống dẫn ngay sau đó có thể là một phần "
               "của vỏ bọc và nằm dưới sự kiểm soát của nhà sản xuất. Tuy "
               "nhiên, không khí phải lấy từ một vùng không nguy hiểm, dẫn "
               "đến chiều dài ống dẫn đáng kể. Như vậy, đây trở thành vấn đề "
               "của người lắp đặt. Điều này làm cho vấn đề rất khó khăn vì "
               "áp suất"))

    # Fig. 11.4 is printed between the two halves of this paragraph.
    b.append(fig(4, F.fig_f1104()))
    b.append(p("trong ống dẫn cấp sẽ thấp hơn áp suất khí quyển (xem Hình "
               "11.5) và, do các ống dẫn phải đi qua một vùng nguy hiểm, bất "
               "kỳ sự rò rỉ nào cũng có thể để khí quyển nổ xâm nhập vào vỏ "
               "bọc. Vì lý do đó, cách tiếp cận thứ nhất không được khuyến "
               "nghị; giải pháp thay thế là dùng quạt đặt xa kết hợp với ống "
               "dẫn được tạo áp thì được ưu tiên hơn (xem Hình 11.6)."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Bản in bắt "
                  "đầu câu thứ hai của đoạn bằng cụm 'Which makes matters "
                  "very difficult...' ngay sau một dấu chấm, tạo thành một "
                  "câu không đầy đủ. Cách diễn đạt này được giữ nguyên trong "
                  "bản tiếng Anh; bản tiếng Việt nối ý theo nghĩa tác giả "
                  "muốn nói: chiều dài ống dẫn đáng kể khiến vấn đề trở nên "
                  "khó khăn vì áp suất trong ống dẫn cấp thấp hơn áp suất "
                  "khí quyển."))

    # Printed p.291: the paragraph continues after the first sentence block,
    # then Figs 11.5 and 11.6 are printed before its continuation on p.292.
    b.append(p("Khi ống dẫn xả ngắn và xả vào một vùng nguy hiểm, bất kỳ tia "
               "lửa nóng đỏ nào bên trong vỏ bọc cũng có thể, trong một số "
               "trường hợp, gây phóng ra các hạt nóng đỏ vào vùng nguy hiểm. "
               "Một thiết bị ngăn ngừa sự phóng ra đó thường là cần thiết khi "
               "thiết bị tạo ra tia lửa có khả năng đánh lửa sinh ra các hạt "
               "này, hoặc chứa một cơ chế khác (ví dụ, máy sắc ký ion hóa "
               "ngọn lửa), hoạt động trong vận hành bình thường, và ống xả "
               "thải vào bất kỳ vùng nguy hiểm nào; cũng như khi dù bản thân "
               "thiết bị không tự sinh ra các hạt đó trong vận hành bình "
               "thường nhưng ống dẫn xả lại thải vào Vùng 1. Trường hợp sau "
               "nhằm đề phòng"))
    b.append(fig(5, F.fig_f1105()))
    b.append(fig(6, F.fig_f1106()))
    b.append(p("tình huống sự cố điện bên trong có thể sinh ra các hạt nóng "
               "đỏ. Bảng 11.2 trình bày điều này dưới dạng bảng."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Nguyên bản "
                  "nối các điều kiện cần thiết bị chắn bằng một câu rất dài "
                  "và lỏng lẻo ('...which can in normal operation, and the "
                  "exhaust duct discharges into any hazardous area and when "
                  "even though...'). Bản tiếng Anh giữ nguyên cách diễn đạt "
                  "in; bản tiếng Việt tách thành hai điều kiện theo ý định: "
                  "thiết bị phát tia lửa có khả năng đánh lửa hoặc có cơ chế "
                  "khác tạo hạt và xả vào bất kỳ vùng nguy hiểm nào, hoặc "
                  "thiết bị không tự tạo hạt nhưng xả vào Vùng 1."))
    b.append(note("<b>Ghi chú về đơn vị áp suất.</b> Nhãn trên các hình in "
                  "ghi '50 N/m²'; lớp văn bản OCR đọc nhầm thành 'N/mz' và "
                  "'Nlm2'. Các hình vẽ lại dùng đúng dạng in, có dấu cách và "
                  "số 2 viết ở dạng mũ, không đổi đơn vị."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.290. Section 11.5.2 opens here; the tail of 11.5.1 that
    # precedes it on this page belongs to module C.
    b.append(h4("11.5.2 Ducting", "11.5.2 Ducting"))
    b.append(p("As the ducting forms part of the enclosure it needs to "
               "satisfy the same requirements as those for enclosures. With "
               "the use of compressed gas, this is no problem as the ducts "
               "will be short, being only in the area of the enclosure (see "
               "Fig. 11.4) – the supply of gas to that point normally being "
               "compressed gas piping, and the outlet ducting being short as "
               "it discharges into the hazardous area. (It is not possible "
               "to permit the exit ducting to exhaust into a non-hazardous "
               "area, as to do so would make it a hazardous area). Therefore, "
               "in these cases, all piping and ducting will be at a pressure "
               "above atmospheric pressure and the ducts can form a part of "
               "the apparatus."))
    b.append(p("Where the protective gas is air, and fan supplied (not "
               "normally possible for inert gas), then there are two "
               "possibilities. First, the fan and immediate ducting may form "
               "part of the enclosure and be under the control of the "
               "manufacturer. The air must, however, be obtained from a "
               "non-hazardous area resulting in a considerable length of "
               "ducting. This, then, becomes an installer problem. Which "
               "makes matters very difficult because the pressure"))

    # Fig. 11.4 is printed between the two halves of this paragraph.
    b.append(fig(4, F.fig_f1104()))
    b.append(p("in the supplying duct will be below atmospheric pressure "
               "(see Fig. 11.5) and, as the ducts must pass through a "
               "hazardous area, any leak will permit the possible entry of "
               "an explosive atmosphere into the enclosure. This first "
               "approach is not, therefore, recommended and the alternative "
               "of the remote fan with pressurized ducting is preferred (see "
               "Fig. 11.6)."))
    b.append(note("<b>Note on printed wording.</b> The print starts the "
                  "second sentence of this paragraph with 'Which makes "
                  "matters very difficult...' after a full stop, leaving a "
                  "fragment. The printed wording is retained in English; the "
                  "Vietnamese follows the intended sense: the considerable "
                  "duct length makes the matter difficult because the "
                  "pressure in the supplying duct will be below atmospheric."))

    # Printed p.291: the paragraph continues after the first sentence block,
    # then Figs 11.5 and 11.6 are printed before its continuation on p.292.
    b.append(p("Where the exhaust ducting is short and discharges into a "
               "hazardous area any incandescent sparking inside the "
               "enclosure can, in certain circumstances, cause the ejection "
               "of incandescent particles into the hazardous area. A device "
               "to prevent such ejection is normally necessary when the "
               "apparatus produces ignition-capable sparking which can give "
               "rise to such particles or contains some other mechanism (for "
               "example, a flame ionization chromatograph), which can in "
               "normal operation, and the exhaust duct discharges into any "
               "hazardous area and when even though the apparatus does not "
               "itself produce such particles in normal operation but the "
               "exhaust ducting exhausts into a Zone 1. This latter is to "
               "cover the"))
    b.append(fig(5, F.fig_f1105()))
    b.append(fig(6, F.fig_f1106()))
    b.append(p("situation where internal electrical fault can cause the "
               "incandescent particles. Table 11.2 produces this in tabular "
               "form."))
    b.append(note("<b>Note on printed wording.</b> The source expresses the "
                  "conditions for needing a barrier in one long, loosely "
                  "joined sentence ('...which can in normal operation, and "
                  "the exhaust duct discharges into any hazardous area and "
                  "when even though the apparatus does not itself produce "
                  "such particles in normal operation but the exhaust "
                  "ducting exhausts into a Zone 1'). The printed wording is "
                  "kept in English; the Vietnamese follows the intended two "
                  "conditions."))
    b.append(note("<b>Note on pressure units.</b> The labels in the figures "
                  "print '50 N/m²'; the OCR text layer reads 'N/mz' and "
                  "'Nlm2'. The redraws use the printed form with the space "
                  "and superscript 2; no unit conversion is made."))
    return "".join(b)
