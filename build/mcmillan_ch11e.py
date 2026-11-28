# -*- coding: utf-8 -*-
"""Chapter 11, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 292-295 (PDF pp. 313-316).

Covers Table 11.2, the spark/particle-arrester material and Fig. 11.7,
Section 11.5.3 Internal electrical components, etc with Fig. 11.8, and
Section 11.6 Safety provisions and devices through the paragraph ending
'(EN 954)'. The chapter shell owns the chapter h2, the ten printed
references, the glossary and the end matter.

Printed quirks are kept in the English text - the 'made,?' punctuation,
'gasflow' as one word, the superscript footnote marker after '(EN 954)'
and the italic 'etc' in the 11.5.3 heading - with bilingual notes. The
Vietnamese follows the intended sense. OCR misreadings in the figure
labels and the table source line are flagged in the notes but are not
reproduced. This is an unofficial study translation; the source PDF is
not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig
import mcmillanfig11 as F
import mcmillan_tbl11_1_2 as T


def body_vi():
    b = []

    # Printed p.292: Table 11.2 follows the sentence that introduces it in
    # module D. The supplier carries the two-level heading, the printed
    # rows and the localized caption and source note.
    b.append(table(T.HEAD112_VI, T.ROWS112_VI, T.CAPTION112_VI))
    if T.NOTE112_VI:
        b.append(note(T.NOTE112_VI))
    b.append(note("<b>Ghi chú về dòng nguồn của bảng.</b> Nguyên bản in "
                  "'(from BS/EN 50016)'; lớp văn bản OCR đọc nhầm thành "
                  "'worn BSEN 50026)'. Hình vẽ lại và bảng dựng lại theo "
                  "bản in, giữ nguyên dạng gạch chéo 'BS/EN'."))

    # Spark-arresting devices and the exhaust-duct warning, still on p.292.
    b.append(p("Thiết bị ngăn tia lửa thường là thiết bị dạng mê cung hoặc, "
               "ví dụ, len thép (xem Hình 11.7)."))
    b.append(p("Cuối cùng, cần lưu ý rằng các ống dẫn xả tạo thành một đường "
               "dẫn để khí quyển dễ nổ xâm nhập trong những giai đoạn không "
               "có áp suất dư. Vì vậy, cần có một phương pháp nào đó để ngăn "
               "hoặc làm chậm sự xâm nhập của các khí quyển như vậy, như một "
               "phần của quy trình hạn chế tốc độ xâm nhập của khí quyển dễ "
               "nổ khi áp suất bị mất hoặc khi ngắt điện."))

    # Fig. 11.7 is printed directly after the exhaust-duct paragraph.
    b.append(fig(7, F.fig_f1107()))
    b.append(note("<b>Ghi chú về kiểu chữ in.</b> Tiêu đề Mục 11.5.3 bên "
                  "dưới in 'etc' ở dạng nghiêng, còn các nhãn trong Hình "
                  "11.7 viết hoa chữ cái đầu ở 'Labyrinth' và 'Labyrinthine' "
                  "(OCR đọc nhầm thành '-abyrinthine'). Cả hai được giữ "
                  "trong tiêu đề và hình vẽ lại."))

    # Printed p.292. Section 11.5.3 opens here; Fig. 11.8 is printed at the
    # top of p.293, after this first paragraph.
    b.append(h4("11.5.3 Các thành phần điện bên trong, v.v.",
                "11.5.3 Internal electrical components, <i>etc</i>"))
    b.append(p("Vì các bộ phận bên trong của vỏ bọc được bảo vệ bằng cách "
               "tạo áp, yêu cầu đối với chúng nói chung chỉ là những yêu "
               "cầu cần thiết cho sử dụng công nghiệp thông thường. Tuy "
               "nhiên, có một số điều kiện đặc biệt."))
    b.append(fig(8, F.fig_f1108()))
    b.append(note("<b>Ghi chú về nhãn trong hình.</b> Lớp văn bản OCR đọc "
                  "nhầm thành 'matenal' và chuỗi 'F l a m m a b l e b v -* "
                  "material'; bản in ghi 'Flammable material'. Hình vẽ lại "
                  "dùng đúng từ ngữ in."))

    # Printed p.293. The two paragraphs on inner enclosures and internal
    # release of flammable material.
    b.append(p("Khi vỏ bọc được tạo áp chứa các vỏ bọc khác, chẳng hạn như "
               "những vỏ thường lắp trên thiết bị được bao bọc (ví dụ, hộp "
               "rơ le, vỏ màn hình truyền hình, v.v.), có khả năng các vỏ "
               "này bị đầy khí quyển dễ nổ và không được dồn khí hiệu quả. "
               "Vì lý do đó, các vỏ bọc bên trong nên được tháo bỏ hoặc cắt "
               "các lỗ lớn để đảm bảo việc dồn khí có hiệu quả. Cách dễ hơn "
               "thường là tháo bỏ vỏ bọc bên trong. Điều này là không cần "
               "thiết khi vỏ bọc bên trong được bịt kín hiệu quả bằng một "
               "phương pháp nào đó. Các gioăng cao su đàn hồi, bổ sung cho "
               "các mối hàn kín, được coi là đủ cho mục đích này."))
    b.append(p("Có một vấn đề tiềm ẩn khác là khi xảy ra sự phóng thích bên "
               "trong vật liệu dễ cháy, một khí quyển dễ nổ có thể xuất hiện "
               "trong vùng của sự phóng thích trước khi quá trình dồn loãng "
               "hoàn tất nhờ dòng khí bảo vệ liên tục (nếu khí đó là không "
               "khí hoặc nếu chính vật liệu phóng thích chứa oxy). Trong "
               "những trường hợp này, tất cả các linh kiện điện, ngoại trừ "
               "những linh kiện đã được làm thành không có khả năng đánh "
               "lửa theo một khái niệm bảo vệ khác, phải được giữ xa khu "
               "vực dồn loãng (xem Hình 11.8). Điều này thường đạt được bằng "
               "cách đảm bảo không có linh kiện điện nào không được bảo vệ "
               "nằm gần đường nhìn thẳng từ điểm phóng thích đến lỗ thoát "
               "của vỏ bọc. Có thể đảm bảo điều này bằng cách đặt nguồn rò "
               "rỉ tiềm ẩn giữa các linh kiện điện và lỗ thoát. Tất nhiên, "
               "điều này không áp dụng cho các nguồn đánh lửa cố ý như ngọn "
               "lửa trong máy sắc ký ion hóa ngọn lửa và các thiết bị đánh "
               "lửa của chúng."))

    # Printed p.293, continuing on p.294. Section 11.6 opens here.
    b.append(h4("11.6 Các biện pháp và thiết bị an toàn",
                "11.6 Safety provisions and devices"))
    b.append(p("Rõ ràng là an toàn của khái niệm bảo vệ này phụ thuộc rất "
               "nhiều vào các thiết bị giám sát và điều khiển đảm bảo việc "
               "dồn khí có hiệu quả và áp suất được duy trì. Như trong mọi "
               "trường hợp, ngoại trừ những trường hợp liên quan đến duy "
               "trì áp suất trong tạo áp tĩnh, những thiết bị này không "
               "phải lúc nào cũng do nhà sản xuất cung cấp. Lúc đầu có vẻ "
               "hơi mâu thuẫn khi một Tiêu chuẩn chính thức lại được viết "
               "cho một khái niệm bảo vệ ít được nhà sản xuất kiểm soát hơn "
               "các khái niệm khác. Tuy nhiên, điều này không đúng, vì xem "
               "xét kỹ bất kỳ công trình lắp đặt nào sử dụng bất kỳ khái "
               "niệm bảo vệ nào sẽ cho thấy phần lớn sự an toàn của nó được "
               "quyết định bởi các vấn đề lắp đặt (ví dụ, quy định bảo vệ "
               "điện nào được áp dụng? loại cáp nào được sử dụng?, v.v.). "
               "Do đó, tình huống trong đó các cảm biến dồn khí và áp suất "
               "cùng các thiết bị điều khiển liên quan chỉ được kiểm soát "
               "bởi thông số kỹ thuật là có thể chấp nhận được."))
    b.append(note("<b>Ghi chú về dấu câu trong bản in.</b> Nguyên bản viết "
                  "'what electrical protection provisions are made,? what "
                  "cables are used?, etc.' với dấu phẩy ngay trước dấu hỏi "
                  "sau 'made'. Dấu câu nguyên bản được giữ trong bản tiếng "
                  "Anh; bản tiếng Việt dùng dấu hỏi thông thường theo ý "
                  "định."))

    b.append(p("Các thiết bị phát hiện áp suất và tốc độ dồn khí nên, trong "
               "khả năng cho phép, được đặt tại hoặc gần lối thoát của vỏ "
               "bọc để tránh nhận định sai về tình trạng dồn khí/áp suất "
               "(ví dụ, rò rỉ khí ở đầu vào của khí dồn khiến người ta cho "
               "rằng việc dồn khí đã đúng trong khi thực tế khí đang rò rỉ "
               "trước khi vào vỏ bọc, hoặc nhận định sai là áp suất dư đúng "
               "trong khi lối vào vỏ bọc bị tắc). Ngoài ra, nên tránh tối "
               "đa việc dùng các kết nối có đường kính nhỏ tới các thiết bị "
               "này để phòng tắc nghẽn."))

    b.append(p("Trình tự dồn khí nên như sau đối với cả ba cách áp dụng kỹ "
               "thuật này:"))
    b.append(p("1. Các đầu dò phải xác định là đã đạt áp suất và lưu lượng "
               "tối thiểu trước khi bắt đầu tính thời gian dồn khí."))
    b.append(p("2. Nếu áp suất hoặc lưu lượng dồn khí giảm dưới mức tối "
               "thiểu quy định trong khi dồn khí, việc dồn khí phải dừng lại "
               "và các mạch điều khiển phải bắt đầu lại việc dồn khí khi "
               "các điều kiện tối thiểu đã được khôi phục."))
    b.append(p("3. Sau khi dồn khí, trong trường hợp tạo áp có bù rò rỉ hoặc "
               "có dồn loãng liên tục, hệ thống điều khiển phải đóng các van "
               "thoát dồn khí và tiếp tục theo dõi áp suất và, trong trường "
               "hợp dồn loãng liên tục, lưu lượng khí."))
    b.append(p("4. Khi áp suất bị mất, hoặc trong trường hợp dòng chảy liên "
               "tục, khi lưu lượng khí bị mất, phải có biện pháp để báo động "
               "hoặc ngắt hoàn toàn điện, sự lựa chọn do người sử dụng quyết "
               "định."))
    b.append(p("5. Nếu vỏ bọc được mở ra, ngay cả khi hành động báo động hoặc "
               "ngắt điện bị các mạch điều khiển bảo trì ghi đè, thiết bị "
               "phải trải qua toàn bộ chu trình dồn khí khi đóng lại ngay "
               "sau khi các điều kiện dồn khí đã được thiết lập."))
    b.append(note("<b>Ghi chú về 'gasflow'.</b> Bước 4 in 'gasflow' như một "
                  "từ ghép. Bản tiếng Anh giữ nguyên từ ghép như bản in; "
                  "bản tiếng Việt tách thành hai từ."))

    b.append(p("Có thể tạo áp cho nhiều vỏ bọc từ cùng một nguồn nhưng phải "
               "cẩn thận khi làm như vậy. Nếu chúng được tạo áp nối tiếp, "
               "khả năng cao là mất áp suất ở một vỏ bọc sẽ gây mất áp suất "
               "ở tất cả các vỏ bọc phía sau. Trong trường hợp này, hành động "
               "khắc phục đối với bất kỳ sự cố đơn lẻ nào cũng phải áp dụng "
               "cho tất cả các vỏ bọc bị ảnh hưởng. Ngay cả khi không phải "
               "vậy, bất kỳ sự cố đơn lẻ nào cũng sẽ khởi động việc dồn khí "
               "lại cho tất cả các vỏ bọc. Khi nguồn tạo áp chung cấp áp cho "
               "các vỏ bọc song song, tình huống này không xảy ra và, miễn "
               "là có thể nhận dạng riêng biệt sự cố của từng vỏ bọc, chỉ "
               "cần dồn khí lại vỏ bọc đó sau khi khắc phục."))

    # Printed p.295. The last paragraph before the references (owned by the
    # chapter shell) carries the superscript footnote marker ¹⁰.
    b.append(p("Độ tin cậy của các thiết bị điều khiển dồn khí và tạo áp là "
               "yếu tố cơ bản đối với an toàn của khái niệm bảo vệ. Một Tiêu "
               "chuẩn Châu Âu (EN 954)¹⁰ đang được soạn thảo và sẽ đề cập "
               "đến độ tin cậy của các mạch và thiết bị liên quan đến an "
               "toàn, nhưng cho đến khi có tiêu chuẩn này thì không có Tiêu "
               "chuẩn Châu Âu nào có thể áp dụng hiệu quả. Các cách tiếp cận "
               "an toàn chung (ví dụ, fail to safety - an toàn khi hỏng) nên "
               "chi phối thiết kế của các hệ thống và nếu có bất kỳ sự nghi "
               "ngờ nào trong một trường hợp cụ thể, nên xem xét việc nhân "
               "bản các linh kiện hoặc mạch."))
    b.append(note("<b>Ghi chú về ký hiệu chú thích.</b> Nguyên bản đặt số mũ "
                  "¹⁰ sau '(EN 954)'; lớp văn bản OCR đọc nhầm thành '1°'. "
                  "Số mũ được giữ nguyên; mục tham khảo nằm trong danh mục "
                  "tài liệu tham khảo của chương."))
    return "".join(b)


def body_en():
    b = []

    # Printed p.292: Table 11.2 follows the sentence that introduces it in
    # module D. The supplier carries the two-level heading, the printed
    # rows and the localized caption and source note.
    b.append(table(T.HEAD112_EN, T.ROWS112, T.CAPTION112_EN))
    if T.NOTE112_EN:
        b.append(note(T.NOTE112_EN))
    b.append(note("<b>Note on the table source line.</b> The print reads "
                  "'(from BS/EN 50016)'; the OCR text layer rendered it as "
                  "'worn BSEN 50026)'. The table follows the print, and the "
                  "'BS/EN' slash form is kept throughout."))

    # Spark-arresting devices and the exhaust-duct warning, still on p.292.
    b.append(p("Spark-arresting devices are usually labyrinthine devices or, "
               "for example, steel wool (see Fig. 11.7)."))
    b.append(p("Finally, it must be noted that the exhaust ducts provide a "
               "route for explosive atmosphere entry in periods when no "
               "pressurization is present. Therefore, some method of "
               "preventing or slowing down entry of such atmospheres is "
               "necessary as part of the procedure for restricting the rate "
               "of entry of explosive atmosphere on pressurization failure "
               "or electrical isolation."))

    # Fig. 11.7 is printed directly after the exhaust-duct paragraph.
    b.append(fig(7, F.fig_f1107()))
    b.append(note("<b>Note on printed typography.</b> The heading of Section "
                  "11.5.3 below italicises 'etc', and the labels in Fig. "
                  "11.7 print 'Labyrinth' and 'Labyrinthine' with initial "
                  "capitals (the OCR layer read '-abyrinthine'). Both are "
                  "kept in the heading and in the redraw."))

    # Printed p.292. Section 11.5.3 opens here; Fig. 11.8 is printed at the
    # top of p.293, after this first paragraph.
    b.append(h4("11.5.3 Internal electrical components, <i>etc</i>",
                "11.5.3 Internal electrical components, <i>etc</i>"))
    b.append(p("As the internal parts of the enclosure are protected by "
               "pressurization, the requirements for them are normally only "
               "those which would be required for normal industrial use. "
               "There are some special conditions however."))
    b.append(fig(8, F.fig_f1108()))
    b.append(note("<b>Note on the figure labels.</b> The OCR text layer "
                  "reads 'matenal' and the garbled 'F l a m m a b l e b v -* "
                  "material'; the print has 'Flammable material'. The "
                  "redraw uses the printed wording."))

    # Printed p.293. The two paragraphs on inner enclosures and internal
    # release of flammable material.
    b.append(p("Where the pressurized enclosure contains other enclosures "
               "such as those normally fitted to the enclosed equipment "
               "(e.g., relay cases, television monitor cases, etc.) it is "
               "possible that these could fill with an explosive atmosphere "
               "and not be effectively purged. For this reason the inner "
               "enclosures should either be removed or have large holes cut "
               "in to ensure that the purge is effective. The easier way is "
               "normally to remove the internal enclosure. This is not "
               "necessary when the inner enclosure is effectively sealed by "
               "some means. Elastomeric seals in addition to fusion seals "
               "are considered adequate for this purpose."))
    b.append(p("There is a further possible problem in that where an "
               "internal release of flammable material occurs an explosive "
               "atmosphere may occur in the region of the release before "
               "complete dilution of the release has taken place by the "
               "continuous flow of protective gas (if that gas is air or if "
               "oxygen is contained in the release itself). In these "
               "circumstances all electrical components, other than those "
               "which are rendered non-ignition capable by another "
               "protection concept, should be kept well away from the "
               "dilution area (see Fig. 11.8). This is normally achieved by "
               "ensuring that no unprotected electrical components are near "
               "the line of sight from the release to the enclosure exit "
               "aperture. This can be assured by siting the possible source "
               "of leakage between the electrical components and the exit "
               "aperture. This does not apply, of course, to deliberate "
               "ignition sources such as flames in flame ionization "
               "chromatographs and their ignitors."))

    # Printed p.293, continuing on p.294. Section 11.6 opens here.
    b.append(h4("11.6 Safety provisions and devices",
                "11.6 Safety provisions and devices"))
    b.append(p("It is clear that the security of this protection concept "
               "relies to a very large extent upon the monitoring and "
               "control devices which ensure that purging is effective and "
               "pressurization is maintained. As in all cases, except those "
               "associated with pressure maintenance in static "
               "pressurization, these are not always provided by the "
               "manufacturer. It appears at first sight to be somewhat "
               "incongruous that a formal Standard is written for a "
               "protection concept which is less controlled by the "
               "manufacturer than others. This is not, however, true as a "
               "close look at any installation using any protection concept "
               "will show that much of its safety is determined by "
               "installation matters (e.g., what electrical protection "
               "provisions are made,? what cables are used?, etc.). "
               "Therefore, the situation where the purge and pressurization "
               "sensing devices and their associated control devices are "
               "only controlled by specification is acceptable."))
    b.append(note("<b>Note on printed punctuation.</b> The print reads 'what "
                  "electrical protection provisions are made,? what cables "
                  "are used?, etc.' with a comma followed by a question mark "
                  "after 'made'. The printed punctuation is retained in "
                  "English; the Vietnamese follows the intended sense with "
                  "a plain question mark."))

    b.append(p("Pressure and purge rate detection devices should, as far as "
               "possible, be sited at or near the enclosure outlet to avoid "
               "incorrect identification of the purge/pressure situation "
               "occurring (e.g., a gas leak at the input of the purge gas "
               "causing identification of correct purge when, in fact, gas "
               "is leaking before it enters the enclosure, or identifying "
               "correct over pressure when inlet to enclosure is blocked). "
               "In addition, small bore connections to such devices should "
               "be avoided as far as possible to prevent blockage."))

    b.append(p("The sequences for purging should be as follows for all three "
               "applications of the technique:"))
    b.append(p("1. Detectors should identify that minimum pressure and "
               "flowrate is achieved before timing of purge is commenced."))
    b.append(p("2. If pressure or purge flowrate falls below the specified "
               "minimum specification during the purge, the purge should "
               "cease and the control circuits should recommence purge when "
               "the minimum conditions have been restored."))
    b.append(p("3. After purging, in the case of pressurization with leakage "
               "compensation or with continuous dilution, the control system "
               "should close purging exit valves and continue to monitor "
               "pressure and, in the case of continuous dilution, gas flow."))
    b.append(p("4. On failure of either pressure, or in the case of "
               "continuous flow, gasflow provision must be made for an "
               "alarm to be sounded or complete electrical isolation the "
               "choice being made by the user."))
    b.append(p("5. If the enclosure is opened, even if alarm or isolation "
               "action is overridden by maintenance control circuits, the "
               "apparatus must go through its entire purge cycle on "
               "reclosure as soon as the purge conditions have been "
               "established."))
    b.append(note("<b>Note on 'gasflow'.</b> Step 4 prints 'gasflow' as one "
                  "word. The compound is kept as printed in English; the "
                  "Vietnamese uses two words."))

    b.append(p("It is possible to pressurize several enclosures from the "
               "same source but care must be taken in so doing. If they are "
               "pressurized in series, it is likely that failure of pressure "
               "in any one enclosure will cause failure in all downstream "
               "enclosures. In this case the corrective action on any single "
               "failure must apply to all affected enclosures. Even if this "
               "is not the case any single failure will initiate the "
               "repurging of all enclosures. Where the common pressurization "
               "source is pressurizing the enclosures in parallel, this "
               "situation does not occur and, provided the failure of any "
               "one enclosure can be uniquely identified, it is only "
               "necessary to repurge that one enclosure after correction."))

    # Printed p.295. The last paragraph before the references (owned by the
    # chapter shell) carries the superscript footnote marker ¹⁰.
    b.append(p("The reliability of the purge and pressurization control "
               "devices is fundamental to the security of the protection "
               "concept. A European Standard (EN 954)¹⁰ is in preparation "
               "and will concern itself with the reliability of safety "
               "related circuits and devices, but until this is available "
               "there is no European Standard which can be effectively "
               "applied. General safety approaches (e.g., fail to safety) "
               "should govern the design of systems and if there is any "
               "doubt in a particular case, duplication of components or "
               "circuits should be considered."))
    b.append(note("<b>Note on the footnote marker.</b> The print carries the "
                  "superscript ¹⁰ after '(EN 954)', which the OCR text layer "
                  "read as '1°'. The superscript is retained; the reference "
                  "itself is given in the chapter reference list."))
    return "".join(b)
