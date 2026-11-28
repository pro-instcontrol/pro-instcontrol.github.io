# -*- coding: utf-8 -*-
"""Chapter 11, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 282-285 (PDF pp. 303-306).

Covers the assigned source span LF 12554-12715: the tail of Section 11.2.2
(printed p. 282), Section 11.2.3 Pressurization with continuous dilution
(p. 283), Section 11.3 Purge and dilution gases and Section 11.4 Flammable
materials imported into enclosures and their containment (pp. 284-285).
The module ends mid-sentence at the printed p. 285/286 break; module C
continues that sentence. There are no figures and no tables in this span.

Printed quirks are kept in the English text (the missing verb in the
helium/carbon dioxide sentence, the scrambled oxygen-enrichment sentence,
the comma splice on brittle seals, superscript footnote 6, the space in
'50 N/m²', the true minus in '−20 and +40 °C' and the closed-up
'gas/vapour-phase mixture') with bilingual notes, and the Vietnamese
follows the intended meaning. The chapter shell owns the chapter h2, the
references and the end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note


def body_vi():
    b = []

    # Printed p.282 tail. This continues a sentence from printed p.281
    # (module A) and belongs to Section 11.2.2.
    b.append(p("và thời gian làm sạch phải được kéo dài cho mục đích này. "
               "(Tiếc là thể tích của các ống dẫn hoặc đường ống đó chỉ được "
               "xác định khi lắp đặt và người sử dụng thiết bị phải quyết "
               "định tổng thời gian làm sạch cần thiết. Các thiết bị đảm bảo "
               "làm sạch đúng cách và kiểm soát việc làm sạch (tức là bộ định "
               "thời, đầu dò lưu lượng v.v.) cũng có thể do bên lắp đặt lắp "
               "đặt theo thông số kỹ thuật của nhà sản xuất và thường tạo "
               "thành một phần của gói điều khiển được chế tạo riêng, gói này "
               "cung cấp tất cả các điều khiển cần thiết sau khi được kích "
               "hoạt bởi các công tắc giới hạn áp suất và lưu lượng gắn trên "
               "vỏ bọc (xem Mục 11.5 của chương này)."))

    # Printed p.282: unnumbered subheading under Section 11.2.2.
    b.append(h4("Sự rò rỉ vật liệu dễ cháy bên trong",
                "Internal release of flammable material"))
    b.append(p("Khác với phương pháp tạo áp tĩnh, vật liệu dễ cháy có thể "
               "được đưa vào các vỏ bọc khi tạo áp bằng bù rò rỉ, miễn là "
               "việc tạo áp được thực hiện bằng khí trơ. Lý do không cho phép "
               "dùng không khí là nếu vỏ bọc không phải là kín quá kém thì "
               "lưu lượng khí tạo áp đi vào nó sẽ nhỏ; thực ra đó chính là "
               "mục tiêu. Trong những trường hợp như vậy, nếu dùng không "
               "khí, bên trong vỏ bọc sẽ nhanh chóng bị lấp đầy bởi một khí "
               "quyển nổ nếu xảy ra rò rỉ, vì không khí bên trong vỏ bọc gần "
               "như đứng yên, và lượng khí dễ cháy trong hỗn hợp bên trong "
               "vỏ bọc sẽ tăng theo tốc độ rò rỉ và nhanh chóng vượt quá "
               "giới hạn nổ dưới."))
    b.append(p("Sự xâm nhập của vật liệu dễ cháy từ hệ thống chứa vào vỏ bọc "
               "gây ra các vấn đề bổ sung ngay cả khi dùng khí trơ, vì có thể "
               "có oxy trong vật liệu dễ cháy được giải phóng. Để tính đến "
               "điều này, thời gian làm sạch xác định cho vỏ bọc khi không "
               "xét đến rò rỉ cần được tăng lên, và mức 1,5 lần giá trị đó "
               "được coi là phù hợp khi xét đến sự rò rỉ bên trong. Ngoài ra, "
               "không được có nhiều hơn 2 phần trăm oxy trong hỗn hợp khí "
               "dễ cháy được chứa cho phép đi vào vỏ bọc nếu muốn dùng kiểu "
               "tạo áp này."))
    b.append(p("Phương pháp tạo áp bằng bù rò rỉ không được coi là chấp nhận "
               "được khi việc giải phóng là một phần bình thường của vận "
               "hành trong hệ thống chứa bên trong vỏ bọc, vì trong những "
               "trường hợp đó vỏ bọc luôn chứa vật liệu dễ cháy và sẽ yêu "
               "cầu phải làm sạch hệ thống chứa và làm sạch vỏ bọc trước khi "
               "có thể mở nó. Điều này được coi là quá phiền phức để có thể "
               "chấp nhận như một quy trình kiểm soát (xem Bảng 11.1)."))
    b.append(p("Cũng phải nhận ra rằng sự giải phóng từ vỏ bọc, dù là do rò "
               "rỉ hay do làm sạch, sẽ chứa khí hoặc hơi dễ cháy trong những "
               "lúc có rò rỉ bên trong và một khí quyển nổ có thể bao quanh "
               "vỏ bọc vì lý do này. Mặc dù điều này thường không thành vấn "
               "đề vì vỏ bọc thường nằm trong một khu vực đã trở nên nguy "
               "hiểm do chính các vật liệu đang rò rỉ, trong một số trường "
               "hợp đặc biệt thiết bị có thể chứa các thuốc thử và vật liệu "
               "tương tự nguy hiểm hơn các vật liệu trong khu vực xung "
               "quanh. Do đó, khu vực xung quanh có thể chuyển sang một nhóm "
               "con nghiêm ngặt hơn, ảnh hưởng đến các thiết bị khác trong "
               "khu vực."))

    # Printed p.283.
    b.append(h4("11.2.3 Tạo áp bằng pha loãng liên tục",
                "11.2.3 Pressurization with continuous dilution"))
    b.append(p("Tạo áp bằng pha loãng liên tục (hoặc dòng khí sau khi làm "
               "sạch) là hình thức tạo áp đắt nhất và chỉ cần thiết khi độ "
               "rò rỉ lớn đến mức cần dòng khí liên tục để giữ áp suất vỏ "
               "bọc cao hơn mức chênh lệch 50 N/m² yêu cầu, hoặc khi có sự "
               "pha loãng các sự rò rỉ bên trong. Kỹ thuật này yêu cầu làm "
               "sạch vỏ bọc trước khi vận hành để đảm bảo bên trong không có "
               "khí quyển nổ trước khi cấp điện, nhưng khác ở chỗ một dòng "
               "khí đáng kể liên tục vẫn tiếp tục sau khi cấp điện. Như với "
               "các phương pháp tạo áp trước đó, phải tính đến tình huống "
               "khí quyển nổ có thể xâm nhập vào vỏ bọc khi mất tạo áp và "
               "các quy trình tương tự được áp dụng."))
    b.append(note("<b>Ghi chú về đơn vị áp suất.</b> Bản in ghi '50 N/m²' có "
                  "dấu cách và số 2 viết ở dạng mũ; lớp văn bản OCR đọc nhầm "
                  "thành '50N/m2'. Giữ nguyên dạng in, không đổi đơn vị."))

    # Unnumbered subheading, as printed.
    b.append(h4("Không có sự rò rỉ vật liệu dễ cháy bên trong",
                "No internal release of flammable material"))
    b.append(p("Chỉ có hai lý do để dùng kỹ thuật này khi không có sự rò rỉ "
               "vật liệu dễ cháy: thứ nhất, khi độ rò rỉ lớn, trong trường "
               "hợp đó đây chỉ là một trường hợp giới hạn của phương pháp "
               "tạo áp bằng bù rò rỉ và vì thế không cần đề cập ở đây; và "
               "thứ hai, khi có nhân viên đi vào, nhưng vì các tình huống "
               "duy nhất có khả năng xảy ra điều này là các nhà và phòng "
               "phân tích (đều bị loại khỏi BS/EN 50016⁶), nên cách tiếp "
               "cận này không cần thiết khi không có sự rò rỉ bên trong "
               "thiết bị."))
    b.append(note("<b>Ghi chú về chỉ số ghi chú.</b> Bản in ghi 'BS/EN "
                  "50016⁶', trong đó chữ số 6 là chỉ số ghi chú dạng mũ, "
                  "không phải một phần của số tiêu chuẩn. Lớp văn bản OCR "
                  "đọc nhầm thành '500166'. Không gộp chữ số vào tên tiêu "
                  "chuẩn."))

    # Unnumbered subheading, as printed.
    b.append(h4("Sự rò rỉ vật liệu dễ cháy bên trong",
                "Internal release of flammable material"))
    b.append(p("Khi có sự rò rỉ hạn chế vật liệu dễ cháy trong điều kiện sự "
               "cố, dòng liên tục của khí tạo áp đi qua vỏ bọc có thể là "
               "không khí hoặc khí trơ. Cách làm sạch trong những trường hợp "
               "này khác ở chỗ tính đến sự giải phóng từ hệ thống chứa cả "
               "trong lần làm sạch lẫn trong lần pha loãng liên tục sau đó. "
               "Khi khí làm sạch là khí trơ, không khí ở tốc độ rò rỉ khí "
               "bên trong lớn nhất có thể từ quá trình được phun vào vỏ bọc "
               "trong suốt thử nghiệm làm sạch, ngoài việc ban đầu lấp đầy "
               "vỏ bọc bằng không khí. Thời gian làm sạch lại là thời gian "
               "để khí ở đầu ra đạt đến điểm chứa ít hơn 2 phần trăm oxy. "
               "Khi không khí là khí làm sạch, việc phun là một hoặc cả hai "
               "khí thử (tức là heli hoặc argon/carbon dioxide) và thời gian "
               "làm sạch là thời gian cần để đạt đến giới hạn ít hơn 1 phần "
               "trăm heli hoặc 0,25 phần trăm argon/carbon dioxide. Lưu lượng "
               "heli/carbon dioxide đi vào vỏ bọc phải bằng mức lớn nhất mà "
               "khí có thể rò rỉ vào vỏ bọc khi vận hành."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Bản in viết "
                  "'The helium/carbon dioxide flow into the enclosure equal "
                  "to the maximum...' mà thiếu động từ 'is'. Cách diễn đạt "
                  "này được giữ nguyên trong bản tiếng Anh; bản tiếng Việt "
                  "dùng 'phải bằng' theo ý định tác giả."))
    b.append(p("Tốc độ dòng pha loãng cũng được xác định theo cách tương tự, "
               "với tốc độ rò rỉ lớn nhất của vật liệu dễ cháy. Mục tiêu là "
               "duy trì mức oxy tối đa ở đầu ra khi làm sạch bằng khí trơ ở "
               "mức dưới 2 phần trăm và nồng độ tối đa của khí hoặc hơi dễ "
               "cháy ở đầu ra dưới 25 phần trăm giới hạn nổ dưới nếu khí pha "
               "loãng là không khí."))

    # Printed p.284.
    b.append(p("Khi có sự giải phóng bình thường có chủ đích vật liệu dễ cháy "
               "vào vỏ bọc, nó phải định lượng được và được xử lý như sự giải "
               "phóng hạn chế trong điều kiện sự cố, ngoại trừ việc khí pha "
               "loãng và tạo áp phải là không khí để đảm bảo phần lớn hỗn hợp "
               "bên trong vỏ bọc luôn không nổ, ngay cả khi vỏ bọc được mở. "
               "Tương tự, khi giới hạn nổ trên của khí hoặc hơi được giải "
               "phóng lớn hơn 80 phần trăm, chỉ có thể pha loãng bằng không "
               "khí vì, ngay cả với nồng độ không khí thấp 2 phần trăm cần "
               "thiết để pha loãng bằng khí trơ, tình huống đó vẫn không "
               "được coi là đủ an toàn."))
    b.append(p("Trong trường hợp giải phóng không hạn chế (do giải phóng "
               "chất lỏng sau đó bay hơi), không khí không được coi là phù "
               "hợp làm khí làm sạch và pha loãng vì khó đạt được mức 25 phần "
               "trăm giới hạn nổ dưới với độ tin cậy đủ. Do đó, phải dùng khí "
               "trơ và tiêu chí ít hơn 2 phần trăm oxy phải được đáp ứng "
               "trong trường hợp xấu nhất. Điều này giả định rằng tốc độ giải "
               "phóng oxy tối đa từ hệ thống chứa phải định lượng được ngay "
               "cả khi sự giải phóng chứa nhiều hơn 2 phần trăm oxy."))

    b.append(h4("11.3 Khí dùng cho làm sạch và pha loãng",
                "11.3 Purge and dilution gases"))
    b.append(p("Nguồn khí dùng để làm sạch, tạo áp, bù rò rỉ và pha loãng có "
               "thể được cấp từ quạt, đường ống khí nén hoặc bình chứa. Trong "
               "mọi trường hợp, phải đảm bảo khí sạch và không chứa lượng "
               "đáng kể hơi ẩm, bằng cách lọc nếu cần. Theo tình hình chung, "
               "khí phải có nhiệt độ giữa −20 và +40 °C, nhưng trong phạm vi "
               "đó thì được phép dùng nó làm môi chất gia nhiệt hoặc làm "
               "mát. Khi dùng khí trơ, phải làm rõ cho những người liên quan "
               "đến việc áp dụng thiết bị rằng có thể tồn tại nguy cơ ngạt "
               "thở đáng kể gần thiết bị, đặc biệt khi dùng pha loãng liên "
               "tục. Trong trường hợp nào cũng không được có các thành phần "
               "dễ cháy đáng kể trong khí."))
    b.append(note("<b>Ghi chú về nhiệt độ.</b> Bản in ghi '−20 and +40 °C' "
                  "với dấu trừ thật và ký hiệu độ; lớp văn bản OCR đọc nhầm "
                  "dấu độ thành dấu ngoặc kép. Giữ nguyên dạng in."))

    b.append(h4("11.4 Vật liệu dễ cháy đưa vào vỏ bọc và sự chứa đựng của "
                "chúng",
                "11.4 Flammable materials imported into enclosures and "
                "their containment"))
    b.append(h4("11.4.1 Vật liệu dễ cháy đưa vào vỏ bọc",
                "11.4.1 Flammable materials imported into enclosures"))
    b.append(p("Các vật liệu dễ cháy đi vào vỏ bọc tạo áp có thể là khí, hơi, "
               "sương mù hoặc chất lỏng ở nhiệt độ cao hơn điểm cháy của "
               "chúng và do đó có thể tạo thành một khí quyển nổ trong không "
               "khí. Cần biết tốc độ bay hơi tối đa của các vũng chất lỏng "
               "hình thành bên trong vỏ bọc vì chúng ảnh hưởng đến lưu lượng "
               "không khí yêu cầu. Nếu các chất lỏng đi vào vỏ bọc không có "
               "tốc độ bay hơi có thể dễ dàng chứng minh là ngăn được sự tích "
               "tụ chất lỏng trong vỏ bọc, cần chú ý đến phương pháp thoát "
               "các chất lỏng đó để đảm bảo vỏ bọc không bị đầy chất lỏng dễ "
               "cháy. Việc thoát chất lỏng phải dẫn đến sự chứa đựng an toàn, "
               "chẳng hạn như"))
    b.append(note("<b>Ghi chú về chính tả.</b> Nguyên bản dùng cách viết Mỹ "
                  "'analyzers' và 'vaporizes'; bản tiếng Việt không sửa "
                  "thành cách viết Anh."))

    # Printed p.285.
    b.append(p("một bình thu nhận được thiết kế cho mục đích đó, bình này "
               "sẽ chứa chất lỏng và không ảnh hưởng xấu đến đặc tính của "
               "vùng nguy hiểm nơi nó đặt. Có thể áp dụng cách tiếp cận tương "
               "tự như cách dùng tại các điểm lấy mẫu."))
    b.append(p("Có những giới hạn mà đặc tính của bất kỳ vật liệu dễ cháy nào "
               "phải nằm trong nếu muốn được chấp nhận. Đối với phương pháp "
               "tạo áp bằng bù rò rỉ, hỗn hợp khí/hơi của nó không được có "
               "nhiều hơn 2 phần trăm oxy trong mọi điều kiện, và đối với "
               "phương pháp tạo áp bằng pha loãng liên tục thì không nhiều "
               "hơn 21 phần trăm. Con số sau nhằm ngăn ngừa sự làm giàu oxy "
               "trong quá trình pha loãng liên tục và là cần thiết vì trong "
               "không khí chỉ có 21 phần trăm oxy. Đối với mọi loại bảo vệ, "
               "tình chung là chúng không được thiết kế cho khí quyển nổ "
               "chứa nhiều hơn 21 phần trăm oxy."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Câu in 'This "
                  "latter figure is intended to prevent with continuous "
                  "dilution of oxygen enrichment' có trật tự từ bị xáo trộn "
                  "trong nguyên bản. Bản tiếng Anh giữ nguyên; bản tiếng Việt "
                  "diễn theo nghĩa tác giả muốn nói: con số 21 phần trăm "
                  "nhằm ngăn sự làm giàu oxy khi pha loãng liên tục."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Bản in viết "
                  "'gas/vapour-phase mixture' không có dấu cách sau dấu gạch "
                  "chéo; lớp văn bản OCR thêm một dấu cách. Giữ nguyên dạng "
                  "in."))

    b.append(h4("11.4.2 Sự chứa đựng vật liệu dễ cháy bên trong vỏ bọc",
                "11.4.2 Containment of flammable materials within "
                "enclosures"))
    b.append(p("Khi có vật liệu dễ cháy được đưa vào vỏ bọc, khác với môi "
               "chất tạo áp, nó sẽ nằm trong một cơ chế vận chuyển chứa đựng "
               "nào đó. Điển hình của các hệ thống như vậy là đường ống và "
               "các cell có cửa sổ quang học (như loại dùng trong máy phân "
               "tích quang học), hoặc đường ống và hệ thống giải phóng có "
               "kiểm soát (như loại dùng trong máy sắc ký). Thực tế có ba "
               "loại trong số này cho mục đích của nguyên lý bảo vệ này."))
    b.append(p("Khi sự chứa đựng có thể rò rỉ, cần xem xét tình huống mà dù "
               "các mạch điện bên trong vỏ bọc đã bị ngắt do mất tạo áp, vẫn "
               "có các bộ phận bên trong vỏ bọc còn khả năng đánh lửa do "
               "điện tích còn lưu lại hoặc nhiệt độ cao. Trong những trường "
               "hợp đó, các thiết bị xác định sự mất tạo áp cũng phải cắt "
               "dòng vật liệu dễ cháy đến hệ thống chứa."))

    # Unnumbered subheading, as printed.
    b.append(h4("Sự chứa đựng tuyệt đối đáng tin cậy",
                "Infallible containment"))
    b.append(p("Nếu vật liệu dễ cháy có thể được chứa đựng hiệu quả bên trong "
               "vỏ bọc tạo áp sao cho có mức độ tin cậy rất cao là trong mọi "
               "sử dụng bình thường nó không thể được giải phóng, thì sự "
               "chứa đựng đó có thể được mô tả là tuyệt đối đáng tin cậy. Sự "
               "chứa đựng như vậy không được dựa vào những thứ như gioăng ép "
               "bằng kim loại hoặc elastomer, vì chúng có thể hỏng, mà phải "
               "đạt được bằng các phương pháp như hàn, hàn gió đá hoặc các "
               "gioăng kim loại–thủy tinh tạo bằng nóng chảy hay các quy trình "
               "tương tự để đạt được độ tin cậy yêu cầu. Ngay cả các phương "
               "pháp hàn ở nhiệt độ thấp, như hàn thiếc, cũng không được coi "
               "là đủ chắc chắn cho mục đích chứa đựng tuyệt đối đáng tin cậy. "
               "Ngoài ra, thực tế là một số kỹ thuật này tạo ra các gioăng "
               "giòn (ví dụ, gioăng nóng chảy kim loại–thủy tinh) cần được "
               "xem xét cẩn thận về mặt cơ khí. Các gioăng phải chắc chắn "
               "chịu được sự rơi rụng và va đập thường yêu cầu đối với BS/EN "
               "50016⁶ nhưng, ngoài ra, cần xem xét các ứng suất lắp ráp và "
               "sự thay đổi nhiệt độ trong sử dụng để đảm bảo chúng không "
               "gây ứng suất đủ lớn lên các mối nối tạo ra, dẫn đến nứt gãy. "
               "Không có thử nghiệm cụ thể nào cho những"))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Nguyên bản "
                  "nối '...fusion seals) mechanical considerations need to "
                  "be carefully considered.' bằng một dấu phẩy thay vì một "
                  "liên từ. Cách diễn đạt này được giữ nguyên trong bản tiếng "
                  "Anh; bản tiếng Việt tách thành hai ý theo nghĩa tác giả."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.282 tail. This continues a sentence from printed p.281
    # (module A) and belongs to Section 11.2.2.
    b.append(p("and the purging time must be extended for this purpose. "
               "(Unfortunately, the volume of such ducts or pipes is only "
               "determined at installation and the user of the apparatus "
               "must decide on the total purge time necessary. The devices "
               "to ensure proper purging and purge control (i.e., timers, "
               "flow detectors etc.) may also be fitted by the installer to "
               "the manufacturer's specification and often form part of a "
               "specially produced control package which provides all of "
               "the controls necessary once activated by the pressure and "
               "flow limit switches attached to the enclosure (see Section "
               "11.5 of this chapter)."))

    # Printed p.282: unnumbered subheading under Section 11.2.2.
    b.append(h4("Internal release of flammable material",
                "Internal release of flammable material"))
    b.append(p("Unlike static pressurization, flammable materials may be "
               "brought into the enclosures with pressurization by leakage "
               "compensation, provided the pressurization is with inert gas. "
               "The reason air is not permitted is that if the enclosure is "
               "other than very badly sealed the pressurizing gas flow into "
               "it will be small; indeed that is the objective. In such "
               "circumstances, if air were to be used the interior of the "
               "enclosure would rapidly become filled with an explosive "
               "atmosphere if a leak occurred because the air inside the "
               "enclosure would be almost static, and the amount of "
               "flammable gas in the mixture inside the enclosure would "
               "increase at the rate of its leakage and would rapidly exceed "
               "the lower explosive limit."))
    b.append(p("The incursion of the flammable material from the containment "
               "system into the enclosure produces additional problems even "
               "if an inert gas is used, as there may be oxygen in the "
               "released flammable material. To allow for this, the purge "
               "time determined for the enclosure when no leakage is "
               "considered needs to be increased, and a figure of 1.5 times "
               "that figure is considered as appropriate when the internal "
               "release is taken into account. In addition, there must be no "
               "more than 2 per cent oxygen in the contained flammable gas "
               "mixture permitted to enter the enclosure if this type of "
               "pressurization is to be used."))
    b.append(p("Pressurization with leakage compensation is not considered as "
               "acceptable when release is a normal part of operation in the "
               "containment system within the enclosure as, in such "
               "circumstances, the enclosure would always contain flammable "
               "material and would require that the containment be cleared "
               "and the enclosure purged before it could be opened. This is "
               "considered as too cumbersome a control procedure to be "
               "acceptable (see Table 11.1)."))
    b.append(p("It must also be recognized that the release from the "
               "enclosure, either by leakage or by purging, will contain a "
               "flammable gas or vapour in times of internal leakage and an "
               "explosive atmosphere may surround the enclosure due to this. "
               "While this is normally not a problem because the enclosure "
               "is usually in an area made hazardous by the same materials "
               "as those leaking, in some exceptional cases the apparatus "
               "may contain reagents and similar materials which are more "
               "hazardous than those in the surrounding area. Therefore, the "
               "surrounding area may change to a more onerous sub-group, "
               "affecting other apparatus in the area."))

    # Printed p.283.
    b.append(h4("11.2.3 Pressurization with continuous dilution",
                "11.2.3 Pressurization with continuous dilution"))
    b.append(p("Pressurization with continuous dilution (or gas flow after "
               "purging) is the most expensive form of pressurization and is "
               "only necessary where leakage is such that continuous flow of "
               "gas is necessary to keep the enclosure pressure above the "
               "50 N/m² differential required, or where dilution of internal "
               "releases are present. The technique requires purging of the "
               "enclosure before operation to ensure that the interior is "
               "free from explosive atmospheres before electrical "
               "energization but is different in that a continuous "
               "significant flow of gas continues after energization. As "
               "with previous methods of pressurization, the situation of "
               "possible entry of explosive atmosphere into the enclosure "
               "on pressurization failure has to be taken into account and "
               "the same procedures are appropriate."))
    b.append(note("<b>Note on pressure units.</b> The print reads '50 N/m²' "
                  "with a space and a superscript 2; the OCR text layer reads "
                  "'50N/m2'. The printed form is kept and no unit conversion "
                  "is made."))

    # Unnumbered subheading, as printed.
    b.append(h4("No internal release of flammable material",
                "No internal release of flammable material"))
    b.append(p("The only two reasons for using this technique where there is "
               "no release of flammable material are: first, where leakage "
               "is great, in which case it is merely a limiting case of "
               "pressurization with leakage compensation and as such need "
               "not be addressed here; and, second, where personnel enter, "
               "but as the only situations where this is likely are analyzer "
               "houses and rooms (both excluded from BS/EN 50016⁶) this "
               "approach is not necessary where no release occurs inside the "
               "apparatus."))
    b.append(note("<b>Note on footnote marker.</b> The print reads 'BS/EN "
                  "50016⁶', where the 6 is a superscript footnote marker and "
                  "not part of the standard designation. The OCR text layer "
                  "misreads it as '500166'. The digit is not folded into the "
                  "designation."))

    # Unnumbered subheading, as printed.
    b.append(h4("Internal release of flammable material",
                "Internal release of flammable material"))
    b.append(p("Where there is a limited release of flammable material under "
               "fault conditions, the continuous flow of pressurizing gas "
               "through the enclosure may be either air or inert gas. The "
               "purging approach in these cases is different, in that account "
               "is taken of the release from the containment in both the "
               "purge and the later continuous dilution. Where the purge gas "
               "is inert, air at the maximum rate of internal gas leakage "
               "rate possible from process is injected into the enclosure "
               "throughout the purge test in addition to initially filling "
               "the enclosure with air. The purge time again becomes the "
               "time taken for the outlet gas to reach a point where it "
               "contains less than 2 per cent oxygen. Where air is the purge "
               "gas the injection is one or both of the test gases (i.e., "
               "helium or argon/carbon dioxide) and the purge time is the "
               "time required to reach the limit of less than 1 per cent "
               "helium or 0.25 per cent argon/carbon dioxide. The "
               "helium/carbon dioxide flow into the enclosure equal to the "
               "maximum at which gas can leak into the enclosure in "
               "service."))
    b.append(note("<b>Note on printed wording.</b> The print reads 'The "
                  "helium/carbon dioxide flow into the enclosure equal to "
                  "the maximum...' without the verb 'is'. The printed wording "
                  "is retained in English; the Vietnamese rendering supplies "
                  "the verb according to the intended meaning."))
    b.append(p("Dilution flow rates are also determined in the same way, with "
               "the maximum leak rate of flammable material. The object is "
               "to maintain the maximum outlet oxygen level for inert gas "
               "purging at less than 2 per cent and the maximum outlet "
               "concentration of flammable gas or vapour at less than 25 per "
               "cent of lower explosive limit if the dilution gas is air."))

    # Printed p.284.
    b.append(p("Where there is a deliberate normal release of flammable "
               "material into the enclosure it must be quantifiable, and is "
               "treated as for the limited fault release except that the "
               "dilution and pressurization gas must be air to ensure that "
               "the majority of the mixture inside the enclosure is always "
               "non-explosive, even when the enclosure is opened. Likewise, "
               "where the upper explosive limit of the released gas or "
               "vapour is more than 80 per cent, only dilution with air is "
               "possible as, even with the low air concentration of 2 per "
               "cent required for inert gas dilution, the situation is not "
               "considered as sufficiently safe."))
    b.append(p("In the case of unlimited releases (caused by release of "
               "liquid which then vaporizes) air is not considered as "
               "suitable for a purge and dilution gas as it is difficult to "
               "achieve the 25 per cent lower explosive limit figure with "
               "sufficient confidence. Therefore, inert gas must be used and "
               "the criterion of less than 2 per cent oxygen must be met in "
               "the worst case. This presupposes that the maximum release "
               "rate of oxygen from the containment must be quantifiable "
               "even where the release contains more than 2 per cent oxygen."))

    b.append(h4("11.3 Purge and dilution gases",
                "11.3 Purge and dilution gases"))
    b.append(p("Supplies of gas used for purging pressurization, leakage "
               "compensation and dilution may be supplied from fans, "
               "compressed gas mains or cylinders. In all cases it should be "
               "ensured that the gas is clean and free from significant "
               "quantities of moisture, by filtering if necessary. In line "
               "with the general situation it should be at a temperature of "
               "between −20 and +40 °C, but within that range it is "
               "acceptable for it to be used as a heating or cooling medium. "
               "Where inert gas is used it must be made clear to those "
               "involved in application of the apparatus that a significant "
               "asphyxiation risk may exist in the proximity of the "
               "apparatus, particularly where continuous dilution is used. "
               "Under no circumstances may significant flammable "
               "constituents be included in the gas."))
    b.append(note("<b>Note on temperature.</b> The print reads '−20 and "
                  "+40 °C' with a true minus sign and a degree symbol; the "
                  "OCR text layer misreads the degree sign as a double quote. "
                  "The printed form is kept."))

    b.append(h4("11.4 Flammable materials imported into enclosures and "
                "their containment",
                "11.4 Flammable materials imported into enclosures and "
                "their containment"))
    b.append(h4("11.4.1 Flammable materials imported into enclosures",
                "11.4.1 Flammable materials imported into enclosures"))
    b.append(p("The flammable materials entering pressurized enclosures may "
               "be gases, vapours, mists or liquids which are above their "
               "flashpoints and can, therefore, form an explosive atmosphere "
               "in air. It is necessary to know the maximum vaporization "
               "rate of liquid pools forming inside the enclosure as these "
               "have an effect on the airflow required. If the liquids which "
               "enter the enclosure do not have a vaporization rate which "
               "can be easily shown to prevent build up of liquid in the "
               "enclosure, attention is necessary to the method of draining "
               "such liquids to ensure that the enclosure does not fill with "
               "flammable liquid. Draining should be to safe containment, "
               "such as"))
    b.append(note("<b>Note on spelling.</b> The source uses the US spellings "
                  "'analyzers' and 'vaporizes'; these are kept as printed."))

    # Printed p.285.
    b.append(p("a receiver designed for the purpose which will contain the "
               "liquid and not adversely affect the specification of the "
               "hazardous area in which it is located. An approach similar "
               "to that used on sampling points may be appropriate."))
    b.append(p("There are limits within which the specification of any "
               "flammable material must fall if it is to be acceptable. For "
               "pressurization with leakage compensation it must not have "
               "more than 2 per cent oxygen in its gas/vapour-phase mixture "
               "under any conditions, and for pressurization not more than "
               "21 per cent. This latter figure is intended to prevent with "
               "continuous dilution of oxygen enrichment and is necessary "
               "as there is only 21 per cent oxygen in air. It is common to "
               "all types of protection that they are not intended for "
               "explosive atmospheres containing more than 21 per cent "
               "oxygen."))
    b.append(note("<b>Note on printed wording.</b> The sentence 'This latter "
                  "figure is intended to prevent with continuous dilution "
                  "of oxygen enrichment' has scrambled word order in the "
                  "source. The printed wording is retained in English; the "
                  "Vietnamese follows the intended sense."))
    b.append(note("<b>Note on printed wording.</b> The print reads "
                  "'gas/vapour-phase mixture' with no space after the slash; "
                  "the OCR text layer inserts a space. The printed form is "
                  "kept."))

    b.append(h4("11.4.2 Containment of flammable materials within enclosures",
                "11.4.2 Containment of flammable materials within "
                "enclosures"))
    b.append(p("Where there is a flammable material transported into the "
               "enclosure, other than the pressurization medium, it will be "
               "in some type of containing transport mechanism. Typical of "
               "such systems are piping, and cells with optical viewports "
               "(such as those used in optical analyzers), or piping and "
               "controlled release systems (such as those used in "
               "chromatographs). There are effectively three types of these "
               "for the purposes of this protection concept."))
    b.append(p("Where the containment can leak it is necessary to consider "
               "the situation where, although the electrical circuits within "
               "the enclosure are isolated by pressurization failure, there "
               "are items within the enclosure which remain ignition capable "
               "due to retained charge or high temperature. In these "
               "circumstances the devices which identify the loss of "
               "pressurization must also cut off the flow of flammable "
               "material to the containment."))

    # Unnumbered subheading, as printed.
    b.append(h4("Infallible containment", "Infallible containment"))
    b.append(p("If the flammable material can be effectively contained within "
               "the pressurized enclosure so that there is a very high level "
               "of confidence that in all normal usage it cannot be released, "
               "then the containment may be described as infallible. Such "
               "containment may not rely on such things as metal or "
               "elastomeric compression seals, which may fail, but must be "
               "achieved by methods such as welding, brazing or glass-to-metal "
               "seals formed by fusion or similar processes to achieve the "
               "required confidence. Even low temperature sealing methods, "
               "such as soldering, are not considered to be sufficiently "
               "secure for the purpose of infallible containment. In addition, "
               "the fact that some of these techniques produce brittle seals "
               "(e.g., glass-to-metal fusion seals) mechanical considerations "
               "need to be carefully considered. The seals must be secure "
               "against the drop and impact normally required by BS/EN "
               "50016⁶ but, in addition, assembly stresses and temperature "
               "changes in use need to be considered to ensure they do not "
               "cause sufficient stress on the joints produced which may "
               "cause fractures. There are no specific tests for these"))
    b.append(note("<b>Note on printed wording.</b> The source joins '...fusion "
                  "seals) mechanical considerations need to be carefully "
                  "considered.' with a comma splice rather than a "
                  "conjunction. The printed wording is retained in English; "
                  "the Vietnamese separates the two ideas."))
    return "".join(b)
