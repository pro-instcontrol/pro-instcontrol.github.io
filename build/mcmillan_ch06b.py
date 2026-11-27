# -*- coding: utf-8 -*-
"""Chapter 6, module B - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas* (1998),
printed pp. 154-156 (PDF pp. 175-177): the conclusion of 6.1.1, sections
6.1.2-6.1.4, 6.2, 6.2.1 and the opening of 6.2.2 with Table 6.3.
Continues directly after module A. The full Zone 20/21/22 layer rules,
6.2.3 and the figures belong to later modules. Unofficial study
translation; the integration module owns the page shell, references and
end matter.
"""
from mcmillan_common import h3, h4, p, note, table
import mcmillan_tbl61 as T61


def body_vi():
    b = []
    b.append(p("Năng lượng bắt lửa của một đám mây bụi có thể được xác định bằng "
               "cách phân tán bụi lơ lửng trong không khí bên trong một ống thử, "
               "sau đó đưa một nguồn bắt lửa vào. Một số giá trị cho việc này được "
               "cho trong Bảng 6.2. Dù việc đo đã được thực hiện với nhiều loại "
               "bụi khác nhau và các giá trị đã tồn tại, thông tin này chỉ có giá "
               "trị đối với các thiết bị điện tạo ra hồ quang hoặc tia lửa mà đám "
               "mây bụi có thể tiếp cận được. Tình huống đó là không bình thường, "
               "bởi cách tiếp cận thông thường là loại trừ bụi ra khỏi bên trong "
               "thiết bị, nơi có thể xuất hiện các hồ quang hoặc tia lửa ấy. Về "
               "mặt lịch sử đã không có một phương pháp thử nghiệm nào được công "
               "nhận quốc tế, và các thông tin sẵn có thu được từ một chuỗi các "
               "phép thử vẫn do chính những người có chuyên môn trong lĩnh vực "
               "này thực hiện."))
    b.append(p("Vào thời điểm các nhiệt độ bắt lửa đám mây bụi được liệt kê trong "
               "Bảng 6.2 được lập ra, đã không có phương pháp quốc tế nào được "
               "chính thức công nhận để xác định nhiệt độ bắt lửa của lớp bụi lắng. "
               "Tuy nhiên, một trong những phương pháp lịch sử thường dùng để xác "
               "định nhiệt độ bắt lửa của đám mây bụi là xác định nhiệt độ tối "
               "thiểu mà tại đó một đám mây bụi trong không khí sẽ bắt lửa trong "
               "một chuỗi phép thử, dùng lò Godbert–Greenwald hoặc thiết bị tương "
               "tự. Cần một chuỗi phép thử vì khó đạt được trường hợp xấu nhất và "
               "một đám mây đồng đều. Nếu xem xét các giá trị cho trong Bảng 6.2, "
               "sẽ thấy rằng, ngoại trừ lưu huỳnh, đối với tất cả các vật liệu "
               "được đưa vào thì nhiệt độ đều vào khoảng 400 °C hoặc cao hơn."))
    b.append(p("Hiện đã có một Tiêu chuẩn Quốc tế (IEC 1241 – 2⁴), do Ủy ban Điện "
               "kỹ Quốc tế (IEC) xây dựng, cho các phương pháp thử chuẩn của những "
               "phép bắt lửa này."))
    b.append(note(
        "<b>Đặc điểm in ấn — ký hiệu tiêu chuẩn và ngoại lệ lưu huỳnh.</b> Ở đây "
        "bản in viết tiêu chuẩn thành 'IEC 1241 – 2⁴', với một dấu gạch ngang dài "
        "có khoảng trắng trước chữ 2 và một dấu chỉ ghi chú ⁴ ở dạng chỉ số trên; "
        "trong danh mục tài liệu tham khảo, cùng một tài liệu lại được ghi là "
        "'IEC 1241–2' không có khoảng trắng. Cả hai cách viết được giữ nguyên như "
        "trong bản in. Nhận định rằng mọi vật liệu ngoại trừ lưu huỳnh đều bắt lửa "
        "ở khoảng 400 °C hoặc cao hơn phù hợp với Bảng 6.2, nơi lưu huỳnh là giá "
        "trị nhiệt độ bắt lửa đám mây duy nhất dưới 400 °C (280 °C)."))
    b.append(h4("6.1.2 Sự bắt lửa của lớp bụi lắng",
                "6.1.2 The ignition of dust layers"))
    b.append(p("Sự bắt lửa của lớp bụi lắng là một hiện tượng phức tạp, phụ thuộc "
               "vào kích thước hạt của lớp bụi và vào môi trường mà sự bắt lửa "
               "được thực hiện — tức là liệu lớp bụi đã được gia nhiệt sơ bộ hay "
               "không. Một lần nữa, đã không có phép thử chuẩn nào cho việc này "
               "khi các giá trị trong Bảng 6.2 được lập ra và, nói chung, nhiệt độ "
               "bắt lửa được xác định bằng cách đốt nóng một lớp bụi dày 5 mm trên "
               "một bếp nóng và xác định nhiệt độ tại đó sự bắt lửa xảy ra."))
    b.append(p("Điều này gặp khó khăn vì bụi có xu hướng âm ỉ cháy khi bị bắt lửa. "
               "Trong khi một số loại tiếp tục cháy và lan dần dọc theo lớp bụi "
               "ra xa nguồn bắt lửa, thì một số khác lại không như vậy và sẽ tắt "
               "ngay khi nguồn bắt lửa được đưa ra. Bất chấp sự khác biệt đó, "
               "nhiệt độ bắt lửa được xem là nhiệt độ mà tại đó sự âm ỉ cháy bắt "
               "đầu, ngay cả khi bụi tắt đi sau khi đưa nguồn nhiệt ra. Cần lưu ý "
               "rằng nhiệt độ bắt lửa của lớp bụi trong hầu hết các trường hợp "
               "thấp hơn nhiệt độ bắt lửa của đám mây bụi."))
    b.append(p("Hiện đã có một Tiêu chuẩn Quốc tế cho phương pháp đo thông số này "
               "– IEC 1241–2⁴."))
    b.append(note(
        "<b>Đặc điểm in ấn — ký hiệu tiêu chuẩn lần hai.</b> Trích dẫn chú giải ⁴ "
        "thứ hai này được in là 'IEC 1241–2⁴', không có khoảng trắng như dạng "
        "'IEC 1241 – 2⁴' ở đoạn trước. Cả hai dạng trong văn bản chính đều được "
        "giữ nguyên, không dạng nào bị đổi lặng lẽ sang dạng của danh mục tài "
        "liệu tham khảo là 'IEC 1241–2'. Định nghĩa nhiệt độ bắt lửa như là điểm "
        "bắt đầu của sự âm ỉ cháy cũng được giữ nguyên, ngay cả khi bụi tắt đi "
        "sau khi đưa nguồn nhiệt ra."))
    b.append(h4("6.1.3 Sự sinh ra khí và hơi dễ cháy từ bụi",
                "6.1.3 Production of flammable gases and vapours by dusts"))
    b.append(p("Một số loại bụi, đặc biệt khi bị đốt nóng, sinh ra khí và hơi. "
               "Hoạt động này là do bụi bắt đầu phân hủy, và khí cùng hơi thoát ra "
               "có thể là dễ cháy. Để xác định tình huống ban đầu, bụi đang xét "
               "được đốt nóng trong một ống thử với một ngọn lửa đặt phía trên "
               "bụi. Nếu bất kỳ khí hoặc hơi dễ cháy nào thoát ra trong quá trình "
               "phân hủy bụi thì sẽ xảy ra sự bắt lửa. Nếu thu được sự bắt lửa thì "
               "cần xác định các khí và hơi đã thoát ra và, nếu bụi có thể đạt tới "
               "nhiệt độ cần thiết để giải phóng chúng trong tình huống xử lý và "
               "chế biến thực tế, thì phải thực hiện các biện pháp phòng ngừa "
               "chống lại sự bắt lửa của chúng."))
    b.append(h4("6.1.4 Các tính chất quan trọng khác của bụi",
                "6.1.4 Other important dust properties"))
    b.append(p("Mặc dù mục tiêu khi chế tạo thiết bị điện dùng trong môi trường "
               "có bụi là loại trừ bụi ra khỏi bên trong thiết bị, trong phạm vi "
               "cần thiết để ngăn ngừa sự bắt lửa, nhưng điều đó không nhất thiết "
               "có nghĩa là phải loại trừ hoàn toàn. Tuy nhiên, bụi có thể dẫn "
               "điện và, trong những trường hợp như vậy, phải được loại trừ hoàn "
               "toàn khỏi thiết bị để ngăn ngừa sự cố hoạt động."))
    b.append(h3("6.2 Phân loại khu vực cho sự phát thải bụi",
                "6.2 Area classification for dust releases"))
    b.append(p("Phương pháp phân loại một khu vực nguy hiểm khi có mặt bụi không "
               "khác mấy so với phương pháp phân loại trong trường hợp khí hoặc "
               "hơi. Trước hết cần xác định khả năng có mặt của một đám mây bụi "
               "hoặc một lớp bụi lắng, dựa trên thông tin về quá trình sản xuất "
               "hoặc các khả năng phát thải có thể xảy ra. Sau đó các đối tượng "
               "này được xếp cấp như các nguồn phát thải theo cách tương tự như "
               "đối với khí và hơi, rồi xác định loại và phạm vi của các khu vực "
               "nguy hiểm."))
    b.append(h4("6.2.1 Nguồn phát thải bụi",
                "6.2.1 Sources of dust release"))
    b.append(p("Các nguồn phát thải bụi được xếp cấp hoàn toàn như trong trường "
               "hợp phát thải khí hoặc hơi và được phân loại như sau:"))
    b.append(p("<b>Nguồn phát thải cấp liên tục.</b> Nguồn phát thải cấp liên tục "
               "là nguồn phát thải một đám mây bụi trong một phần lớn thời gian "
               "và, is in definition, synonymous với nguồn tương đương của nó "
               "trong trường hợp khí hoặc hơi. Điển hình của các khu vực như vậy "
               "là bên trong các thiết bị công nghiệp như phễu chứa và bồn chứa, "
               "v.v."))
    b.append(p("<b>Nguồn phát thải cấp chính.</b> Nguồn phát thải cấp chính trong "
               "trường hợp bụi là những khu vực mà các lớp bụi hoặc đám mây bụi "
               "không được kiểm soát thường không hiện diện, nhưng có thể xuất "
               "hiện trong quá trình vận hành bình thường của nhà máy. Một lần "
               "nữa, chúng tương đồng về nguồn gốc với các nguồn tương ứng của "
               "khí và hơi, và dự kiến không hiện diện quá 10 per cent của thời "
               "gian. Điển hình của các phát thải như vậy là bên trong một số "
               "bình công nghiệp và các điểm nạp liệu, cũng như các cửa ra vào "
               "của các bình chế biến bụi hoặc của các hệ thống vận chuyển."))
    b.append(p("<b>Nguồn phát thải cấp phụ.</b> Nguồn phát thải cấp phụ là những "
               "nguồn thường không được kỳ vọng là sẽ phát thải, trừ khi vận "
               "hình ở trạng thái bất thường, chẳng hạn như hỏng bộ lọc hút và "
               "các tình huống tương tự."))
    b.append(note(
        "<b>Đặc điểm in ấn — cụm 'and, is in definition, synonymous'.</b> Định "
        "nghĩa cấp liên tục được in nguyên văn như ở đoạn trên. Cách diễn đạt này "
        "bị lỗi ngữ pháp và nhiều khả năng định ý là 'by definition' (theo định "
        "nghĩa), nhưng cụm từ in được giữ lại đây thay vì được sửa lặng lẽ. Con "
        "số 10 per cent cho nguồn cấp chính cũng được giữ nguyên như in."))
    b.append(h4("6.2.2 Định nghĩa các Vùng",
                "6.2.2 Definition of Zones"))
    b.append(p("Các vùng nguy hiểm liên quan đến cấp phát thải theo cách rất giống "
               "với trường hợp khí hoặc hơi, ngoại trừ việc sự hiện diện của các "
               "lớp bụi lắng có thể dẫn đến một mức phân loại nghiêm trọng hơn so "
               "với trường hợp khác (xem Bảng 6.3), bởi thay vì phân tán, bụi lắng "
               "xuống mặt đất. Theo nhiều cách, một tình huống trong nhà với "
               "chuyển động không khí nhỏ có thể có lợi về mặt kéo dài thời gian "
               "tồn lưu của các đám mây bụi. Dù điều này dường như là một lợi "
               "thế, nó lại bị giảm đi bởi thực tế là lớp bụi đã hình thành có "
               "thể bị xáo trộn và tạo thành một đám mây, và bản thân lớp bụi đó "
               "cũng có khả năng bắt lửa."))
    b.append(table(T61.HEAD63_VI, T61.ROWS63,
                   T61.CAPTION63_VI + "<br>" + T61.NOTE63_VI))
    b.append(note(
        "<b>Đặc điểm in ấn — ghi chú nguồn của Bảng 6.3.</b> Ghi chú nguồn in là "
        "'(Theo BS/94/213454 DC⁴)', với dấu gạch chéo và dấu chỉ ghi chú ⁴ ở dạng "
        "chỉ số trên; tài liệu tham khảo 3 trong danh mục lại ghi '(BS 94/213454 "
        "DC)' với một khoảng trắng thay cho dấu gạch chéo. Cả hai dạng được giữ "
        "nguyên như in tại vị trí tương ứng của chúng."))
    b.append(p("<b>Vùng 20.</b> Nguồn phát thải cấp liên tục sẽ tạo ra Vùng 20 từ "
               "đám mây bụi mà nó tạo thành, dù ở trong nhà hay ngoài trời, và "
               "chỉ phạm vi là thay đổi tùy theo sự phân tán và sự lắng xuống của "
               "bụi để tạo thành một lớp."))
    return "".join(b)


def body_en():
    b = []
    b.append(p("The ignition energy of a dust cloud can be determined by dispersing "
               "dust suspended in a cloud, in air inside a tube, and then introducing "
               "an ignition source. Some figures for this are given in Table 6.2. "
               "Although this has been done for a variety of dusts and figures "
               "exist, the information is only of value in respect of electrical "
               "equipment which creates arcs or sparks to which the dust cloud has "
               "access. That situation is unusual, since the normal approach is to "
               "exclude the dust from the interior of the equipment where such arcs "
               "or sparks could occur. Historically there has been no internationally "
               "recognized test method, and the available information comes from a "
               "series of tests which were, nonetheless, carried out by those expert "
               "in the field."))
    b.append(p("At the time when the dust-cloud ignition temperatures listed in "
               "Table 6.2 were produced there was no officially recognized "
               "international method for the determination of dust-layer ignition "
               "temperature. One of the common historic methods for determining a "
               "dust-cloud ignition temperature was, however, to determine the "
               "minimum temperature at which a cloud of the dust in air will ignite "
               "in a series of tests in a Godbert–Greenwald furnace or similar "
               "apparatus. A series of tests is required because of the difficulty "
               "of achieving the worst case and a uniform cloud. If one addresses "
               "the figures given in Table 6.2 it will be noted that, with the "
               "exception of sulphur, for all of the materials included the "
               "temperature is around 400 °C or above."))
    b.append(p("An International Standard (IEC 1241 – 2⁴) now exists, produced by "
               "the International Electrotechnical Commission (IEC) for the "
               "standard test methods for these ignitions."))
    b.append(note(
        "<b>Printed quirks — standard number and the sulphur exception.</b> The "
        "prose prints the standard as 'IEC 1241 – 2⁴', with a spaced en dash before "
        "the 2 and a superscript 4 footnote marker; the reference list prints the "
        "same document as 'IEC 1241–2' without spaces. Both forms are retained as "
        "printed here. The statement that all materials except sulphur ignite at "
        "around 400 °C or above is consistent with Table 6.2, where sulphur is the "
        "only cloud ignition temperature below 400 °C (280 °C)."))
    b.append(h4("6.1.2 The ignition of dust layers",
                "6.1.2 The ignition of dust layers"))
    b.append(p("The ignition of dust layers is a complex phenomenon, depending upon "
               "the particle size of the layer and the environment in which "
               "ignition is to be achieved (for example, whether it has been "
               "pre-heated). Again, there was no standard test for this when the "
               "figures given in Table 6.2 were produced and, in general, the "
               "ignition temperature was obtained by heating a 5 mm layer of dust "
               "on a hotplate and determining the temperature at which ignition "
               "occurs."))
    b.append(p("This is difficult, as dusts tend to smoulder when ignited. While "
               "some will continue to burn and progress along the layer away from "
               "the source of ignition, others will not and will extinguish as soon "
               "as the source of ignition is removed. Notwithstanding this "
               "difference, the ignition temperature is considered to be the "
               "temperature at which smouldering begins, even if the dust "
               "extinguishes on removal of the heat source. It should be noted that "
               "the layer ignition temperature is, in most cases, lower than the "
               "cloud ignition temperature."))
    b.append(p("An International Standard now exists for the method of measuring "
               "this parameter – IEC 1241–2⁴."))
    b.append(note(
        "<b>Printed quirk — the standard number again.</b> This second footnote-4 "
        "citation is printed as 'IEC 1241–2⁴' without the spaces used in the "
        "earlier 'IEC 1241 – 2⁴'; both prose forms are kept verbatim, and neither "
        "is silently converted to the reference-list form 'IEC 1241–2'. The "
        "definition of ignition as the onset of smouldering is also retained even "
        "where the dust goes out when the heat source is taken away."))
    b.append(h4("6.1.3 Production of flammable gases and vapours by dusts",
                "6.1.3 Production of flammable gases and vapours by dusts"))
    b.append(p("Some dusts, particularly when heated, give off gases and vapours. "
               "This action is caused by the dust beginning to decompose, and it "
               "is possible that the gases and vapours given off may be flammable. "
               "Initially, to determine the situation, the dust in question is "
               "heated in a tube with a flame applied above it. If any flammable "
               "gases or vapours are emitted during the decomposition of the dust "
               "then an ignition will occur. If an ignition is obtained then the "
               "released gases and vapours need to be identified and, if the dust "
               "can reach the temperature necessary to release them in the "
               "practical handling and process situation, then precautions to "
               "prevent their ignition have to be taken."))
    b.append(h4("6.1.4 Other important dust properties",
                "6.1.4 Other important dust properties"))
    b.append(p("While the objective in constructing electrical equipment for use in "
               "dust situations is to exclude the dust from the interior, insofar "
               "as is necessary to prevent an ignition, this may not mean total "
               "exclusion. The dust may, however, be conducting and, in such cases, "
               "must be totally excluded from the apparatus to prevent malfunction."))
    b.append(h3("6.2 Area classification for dust releases",
                "6.2 Area classification for dust releases"))
    b.append(p("The method of classifying a hazardous area where dust presence is "
               "the problem is little different from that of classification in the "
               "case of gases or vapours. It is first necessary to identify the "
               "possibility of the presence of a dust cloud or layer from process "
               "information or likely release possibilities. These are then graded "
               "as sources of release in the same way as for gases and vapours, "
               "after which the type and extents of hazardous areas may be "
               "identified."))
    b.append(h4("6.2.1 Sources of dust release",
                "6.2.1 Sources of dust release"))
    b.append(p("Sources of release of dusts are graded exactly as in the case of "
               "gas or vapour release and are classified as follows:"))
    b.append(p("<b>Continuous grade source of release.</b> A continuous Grade "
               "Source of Release is one which releases a dust cloud for a large "
               "part of the time and, is in definition, synonymous with its gas or "
               "vapour counterpart. Typical of such areas are those inside process "
               "equipment such as hoppers, silos, etc."))
    b.append(p("<b>Primary grade source of release.</b> Primary Grade Sources of "
               "Release in the case of dusts are those areas where uncontrolled "
               "layers or clouds of dust are not normally present but may occur "
               "during the normal operation of the plant. Again, these are "
               "synonymous in derivation with their gas and vapour counterparts "
               "and are not expected to be present for more than 10 per cent of "
               "the time. Typical of such releases are the interior of some "
               "process vessels and loading points, and access doors to dust "
               "processing vessels or transport systems."))
    b.append(p("<b>Secondary grade sources of release.</b> Secondary Grade Sources "
               "of Release are those which are not normally expected to release "
               "except in abnormal operation, such as the failure of extract "
               "filters and similar situations."))
    b.append(note(
        "<b>Printed quirk — 'and, is in definition, synonymous'.</b> The "
        "continuous-grade definition is printed exactly as above; the wording is "
        "anomalous and is likely to mean 'by definition', but the printed phrase "
        "is preserved here rather than silently corrected. The 10 per cent figure "
        "for primary grade sources is likewise printed as '10 per cent' and is "
        "retained."))
    b.append(h4("6.2.2 Definition of Zones",
                "6.2.2 Definition of Zones"))
    b.append(p("Hazardous zones are related to the grade of release in much the "
               "same way as in the gas or vapour situation, except that the "
               "presence of dust layers can give rise to a more severe "
               "classification than would otherwise be the case (see Table 6.3), "
               "as, instead of dispersing, the dust settles on the ground. In many "
               "ways an indoor situation, where air movement is small, can be "
               "advantageous insofar as longevity of dust clouds is concerned. "
               "While this appears to be an advantage it is mitigated by the fact "
               "that the layer of dust so formed can be disturbed and create a "
               "cloud and is, itself, ignition capable."))
    b.append(table(T61.HEAD63_EN, T61.ROWS63,
                   T61.CAPTION63_EN + "<br>" + T61.NOTE63_EN))
    b.append(note(
        "<b>Printed quirk — Table 6.3 source note.</b> The printed source note "
        "reads '(From BS/94/213454 DC⁴)' with a slash and a superscript 4; "
        "reference 3 in the reference list gives '(BS 94/213454 DC)' with a space "
        "instead of the slash. Both forms are preserved as printed in their "
        "respective places."))
    b.append(p("<b>Zone 20.</b> A continuous grade source of release will give a "
               "Zone 20 from the cloud it creates, be it indoors or outdoors, and "
               "only the extent will vary dependent upon its dispersion and "
               "settling of the dust to form a layer."))
    return "".join(b)
