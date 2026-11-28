# -*- coding: utf-8 -*-
from mcmillan_common import h3, h4, p, note, fig, ul, ol
import mcmillanfig16 as F


def body_vi():
    b = []

    # A0-A3 (printed p.474) and B1 (printed p.475): chapter opening.
    b.append(h3("Mở đầu chương", "Chapter opening"))
    b.append(p("Để hiểu đầy đủ cách tiếp cận trong tương lai đối với thiết bị "
               "dùng trong bầu khí quyển nổ, cần xem xét các vấn đề của hệ "
               "thống hiện hành vốn dựa trên Chỉ thị 76/117/EEC¹ và các Chỉ "
               "thị bổ sung. Các Chỉ thị này xác định các tiêu chuẩn cấu tạo "
               "chi tiết mà thiết bị phải tuân thủ để đủ điều kiện được chứng "
               "nhận hợp quy chính thức bởi một ‘cơ quan được thông báo’, như "
               "đã mô tả trong các chương trước. Phương thức xác định này đã "
               "hạn chế hiệu quả các loại thiết bị có thể được sử dụng trong "
               "Vùng 0 và 1, bởi dù Chỉ thị chỉ đề cập đến chứng nhận hợp quy "
               "như một phương thức thâm nhập thị trường châu Âu, nó lại trên "
               "thực tế xác định những gì có thể được dùng trong các Vùng đó, "
               "vì ngành công nghiệp người sử dụng phần lớn không sẵn sàng "
               "dùng bất kỳ loại thiết bị nào khác. Điều này không áp dụng cho "
               "Vùng 2, do cách tiếp cận ở đây thoải mái hơn nhiều vì mức rủi "
               "ro được hình dung thấp hơn rất nhiều."))
    b.append(p("Tuy nhiên, trong trường hợp Vùng 0 và 1, cách tiếp cận đó dẫn "
               "đến những hạn chế đáng kể và không thể đáp ứng được sự tiến bộ "
               "công nghệ cũng như các hoàn cảnh đặc biệt. Theo đó, trong phạm "
               "vi quốc gia, Vương quốc Anh đã áp dụng khái niệm bảo vệ được "
               "gọi là bảo vệ đặc biệt ‘s’. Mục tiêu của khái niệm này là cung "
               "cấp một cơ chế cho phép phê duyệt chính thức thiết bị mà, dù "
               "không tuân thủ (hoặc không tuân thủ hoàn toàn) bất kỳ khái niệm "
               "bảo vệ chuẩn hóa nào (‘d’, ‘e’, ‘i’, ‘m’, ‘o’, ‘p’, ‘q’), vẫn "
               "đạt được mức an toàn tối thiểu yêu cầu về khả năng gây cháy "
               "nổ. Mục đích của việc này không phải là chứng nhận những "
               "‘trường hợp suýt sót’ mà là tạo điều kiện cho những tiến bộ "
               "trong công nghệ. Giá trị của cách tiếp cận này thể hiện rõ khi "
               "người ta nhận ra rằng nó đã được dùng cho các khái niệm bảo vệ "
               "như bọc kín ‘m’ và các thiết bị không có đường dẫn ngọn lửa đo "
               "được, chẳng hạn như các tấm thiêu kết (sinter), trước khi "
               "những cái đó được đưa vào Tiêu chuẩn khái niệm bảo vệ tương ứng "
               "và được Chỉ thị công nhận cụ thể. Gần đây hơn, cách tiếp cận "
               "này đã được dùng để cho phép các ống hai chân (bi-pin) hoạt "
               "động ở chế độ catốt lạnh trong các đèn chiếu sáng, trên cơ sở "
               "có nhiều (ít nhất là bốn) kết nối cho phép dự phòng — một cách "
               "tiếp cận không được công nhận trong an toàn tăng cường ‘e’ — "
               "và để công nhận các máy dò khí đo oxy cùng các thiết bị tương "
               "tự, trong đó nồng độ oxy của bầu khí quyển nổ được tăng lên và "
               "không thuộc phạm vi các khái niệm bảo vệ tiêu chuẩn, trên cơ sở "
               "thử nghiệm đặc biệt (thường trong bầu khí quyển giàu oxy)."))
    b.append(note("<b>Ghi chú về cụm ‘Zone 0 and 1’ và chữ ‘q’.</b> Bản in viết "
                  "‘Zone 0 and 1’ ở hai chỗ (không lặp lại ‘Zone 1’), và danh "
                  "sách khái niệm bảo vệ kết thúc bằng ‘q’, không phải ‘4’ như "
                  "bản OCR đọc nhầm; bản tiếng Anh giữ nguyên cả hai."))
    # A3+B1 are one continuous paragraph across the printed 474/475 break.
    b.append(p("Tại Vương quốc Anh, chứng nhận quốc gia theo một bộ yêu cầu "
               "thỏa thuận đã từ lâu sẵn có trên cùng một cơ sở như đối với "
               "các cách tiếp cận cấu tạo cổ điển hơn. Chỉ thị 76/117/EEC¹ đã "
               "cố gắng giải quyết vấn đề này bằng cách đưa vào Giấy chứng "
               "nhận kiểm tra, cho phép chứng nhận các phương pháp bảo vệ đặc "
               "biệt. Tuy nhiên, giấy chứng nhận này khác biệt rõ rệt với Giấy "
               "chứng nhận hợp quy và trước khi cấp cần có sự đồng ý của tất "
               "cả các cơ quan được thông báo của châu Âu, những cơ quan này "
               "có quyền tự tiến hành thử nghiệm của mình với chi phí do nhà "
               "sản xuất chịu trước khi cấp phê duyệt như vậy. Kết quả của hai "
               "tình huống này làm cho cách tiếp cận Giấy chứng nhận kiểm tra "
               "trở nên rất kém hấp dẫn và dẫn đến rất ít giấy chứng nhận được "
               "cấp và, hệ quả là, sự tiến bộ công nghệ diễn ra chậm chạp "
               "trong bối cảnh châu Âu. Ngoài ra, 76/117/EEC chỉ đề cập đến "
               "tình huống khí, hơi và sương mù, để lại bụi nằm ngoài pháp "
               "luật châu Âu."))
    b.append(note("<b>Ghi chú về ‘resultantly, slow advance’.</b> Bản in viết "
                  "‘resultantly, slow advance in technology in the European "
                  "scenario’; bản tiếng Anh giữ nguyên cách diễn đạt này."))
    b.append(p("Trong quá trình soạn thảo Chỉ thị mới 94/9/EC², người ta đã cố "
               "gắng khắc phục cả hai vấn đề trên. Chỉ thị mới không viện dẫn "
               "các Tiêu chuẩn châu Âu để xác định yêu cầu cấu tạo mà đưa các "
               "yêu cầu đó vào chính văn bản của mình như những ‘yêu cầu thiết "
               "yếu’. Điều này cho phép một phương thức đơn giản hơn nhiều "
               "trong việc đề cập đến các Tiêu chuẩn châu Âu, chỉ bằng cách "
               "viện dẫn chúng trên Tạp chí EU³ như những Tiêu chuẩn xác định "
               "các yêu cầu cấu tạo đáp ứng các yêu cầu thiết yếu, đồng thời "
               "bỏ cách tiếp cận Giấy chứng nhận kiểm tra cồng kềnh trước đây "
               "bằng cách dùng Giấy chứng nhận hợp quy trong mọi trường hợp "
               "và cung cấp một lộ trình chấp nhận nhanh hơn cho sự tiến bộ "
               "công nghệ. Ngoài ra, thiết bị dành cho nguy cơ bụi hiện được "
               "đưa vào cùng với các hệ thống bảo vệ, chẳng hạn như những hệ "
               "thống dùng với thiết bị áp suất ‘p’, vốn trước đây chưa được "
               "đề cập đầy đủ."))
    b.append(p("Tuy nhiên, một khía cạnh tiêu cực của Chỉ thị mới là yêu cầu "
               "về sự tuân thủ. Theo 76/117/EEC¹, việc sử dụng thiết bị phù hợp "
               "là tùy chọn, Chỉ thị chỉ nêu rằng các quốc gia thành viên "
               "không được cản trở việc nhập khẩu thiết bị đó. Chỉ thị "
               "94/9/EC² thì hoàn toàn khác, vì nó cấm đưa ra thị trường và "
               "đưa vào sử dụng thiết bị không phù hợp với Chỉ thị, từ đó làm "
               "giảm tính linh hoạt quốc gia được dùng rộng rãi. Dù Chỉ thị "
               "cho phép tiếp cận theo 76/117/EEC cho đến cuối tháng 6 năm "
               "2003, và do đó cho phép sử dụng thiết bị có Giấy chứng nhận "
               "hợp quy hoặc Giấy chứng nhận kiểm tra cho đến thời điểm đó, "
               "việc đưa ra thị trường tại các quốc gia thành viên của thiết "
               "bị không phù hợp với 76/117/EEC hoặc 94/9/EC đã có hiệu lực, "
               "kể từ khi Chỉ thị mới được thực thi."))

    # Heading 16.1 and B5+C1 (printed pp.475/476) as one paragraph.
    b.append(h3("16.1 Chấp nhận các yêu cầu kỹ thuật",
                "16.1 Acceptance of technical requirements"))
    b.append(p("Như đã nêu, các yêu cầu thiết yếu đối với cấu tạo của thiết bị "
               "nhằm tuân thủ 94/9/EC được chứa ngay trong bản thân Chỉ thị. "
               "Tuy nhiên, những yêu cầu này được coi là chưa đủ chi tiết để "
               "cho phép chế tạo thiết bị, và CENELEC⁴ có nhiệm vụ xây dựng "
               "các Tiêu chuẩn đáp ứng ‘các yêu cầu thiết yếu’ và chứa đựng "
               "mức độ chi tiết cần thiết. Dự kiến hoạt động này sẽ hoàn "
               "thành đối với ‘d’, ‘e’, ‘i’, ‘m’, ‘o’, ‘p’ và ‘q’ vào giữa "
               "năm 1997 và muộn hơn một chút đối với một số loại. Tình hình "
               "đối với ‘n’ không khó khăn bằng, vì Chỉ thị duy trì mức độ "
               "trang trọng thấp hơn của chứng nhận vốn trước đây được dùng "
               "cho thiết bị Vùng 2. Khi được ban hành, các Tiêu chuẩn châu "
               "Âu này sẽ được xác định trên Tạp chí EU là đáp ứng ‘các yêu "
               "cầu thiết yếu’, và mọi bổ sung trong tương lai cũng sẽ đi theo "
               "lộ trình này. Như vậy, tiến bộ công nghệ được đặt rõ ràng vào "
               "tay cơ quan xây dựng tiêu chuẩn kỹ thuật, và một lộ trình "
               "công nhận nhanh hơn nhiều được mở ra. Cách thức vận hành cuối "
               "cùng của hệ thống này vẫn chưa rõ, nhưng nếu cách tiếp cận "
               "mang tính tích cực thì một tình huống linh hoạt hơn nhiều sẽ "
               "xuất hiện."))
    b.append(note("<b>Ghi chú về ‘technical-standards-making body’ và ‘94/9/EC’.</b> "
                  "Bản in viết ‘technical-standards-making body’ với hai dấu "
                  "gạch ngang, và trong mục 16.1 viết ‘94/9/EC’ không có chỉ "
                  "số trên ²; bản tiếng Anh giữ nguyên cả hai."))

    # Heading 16.2, C3 and C4 (printed p.476).
    b.append(h3("16.2 Các yêu cầu thiết yếu", "16.2 Essential requirements"))
    b.append(p("‘Các yêu cầu thiết yếu’, mặc dù có tác động kỹ thuật, thực chất "
               "được viết bởi các nhân viên của Ủy ban Châu Âu, với những lời "
               "khuyên mà họ thấy cần thiết. Những yêu cầu này có xu hướng "
               "nêu mục tiêu cần đạt được một cách chung chung và để các quy "
               "tắc kỹ thuật cần thiết để đạt được những mục tiêu đó cho "
               "người khác. Dù cách tiếp cận này nhìn chung hợp lý, nó vẫn "
               "nảy sinh một số điểm bất thường kỳ lạ như sẽ thấy trong chương "
               "này."))
    b.append(note("<b>Ghi chú về ‘not withstanding’.</b> Bản in viết ‘not "
                  "withstanding’ thành hai từ; bản tiếng Anh giữ nguyên dù "
                  "nghĩa là ‘mặc dù’."))
    b.append(p("Các yêu cầu này áp dụng, khác với yêu cầu của 76/117/EEC,¹ cho "
               "cả rủi ro điện và rủi ro cơ khí, dù việc thực thi đối với "
               "trường hợp rủi ro cơ khí bị trì hoãn vì hiện chưa có Tiêu "
               "chuẩn nào có thể dùng để xác định yêu cầu chi tiết. Chúng được "
               "chia thành ba phần:"))
    b.append(note("<b>Ghi chú về ‘76/117/EEC,¹’.</b> Bản in đặt chỉ số tham "
                  "chiếu ¹ sau dấu phẩy; bản tiếng Anh giữ nguyên."))

    # Heading 16.2.1, lead-in C6 and the five unnumbered requirements.
    b.append(h4("16.2.1 Yêu cầu chung", "16.2.1 General requirements"))
    b.append(p("Những yêu cầu này xác định năm yêu cầu cơ bản mà thiết bị phải "
               "đáp ứng:"))

    b.append(h4("Các nguyên tắc", "Principles"))
    b.append(p("Thiết bị được yêu cầu ngăn ngừa, nếu có thể, việc hình thành "
               "bất kỳ bầu khí quyển nổ nào từ bất kỳ khí, hơi, sương mù hoặc "
               "bụi nào mà chính nó có thể giải phóng, và ngăn ngừa, trong "
               "chừng mực có thể, bất kỳ sự cháy nổ nào của bầu khí quyển nổ "
               "được hình thành từ sự giải phóng của chính nó hoặc từ nguồn "
               "khác. Khi không thể làm được điều đó, thiết bị được yêu cầu "
               "hạn chế vụ nổ trong chừng mực có thể để ngăn ngừa hư hỏng hoặc "
               "thương tích."))
    b.append(note("<b>Ghi chú về ‘formed by is own release’.</b> Bản in viết "
                  "‘is’, không phải ‘its’, trong cụm ‘formed by is own release "
                  "or otherwise’; bản tiếng Anh giữ nguyên, còn bản tiếng Việt "
                  "dịch theo ý định là ‘sự giải phóng của chính nó’."))

    b.append(h4("Yêu cầu về môi trường", "Environmental requirements"))
    b.append(p("Thiết bị hoặc hệ thống bảo vệ (các hệ thống bảo vệ, chẳng hạn "
               "như hệ thống dừng hoạt động, được bao gồm) được yêu cầu phải "
               "có khả năng hoạt động mà không bị hư hỏng hoặc suy giảm trong "
               "các điều kiện môi trường mà nó được dự định sử dụng. Đây không "
               "phải là yêu cầu riêng của bầu khí quyển nổ nhưng rất quan "
               "trọng trong bối cảnh bầu khí quyển nổ; nếu thiết bị suy giảm "
               "quá mức thì các bộ phận bảo vệ chống nổ của nó cũng có thể "
               "suy giảm theo. Vì vậy, bất kỳ vấn đề nào đã được xác định liên "
               "quan đến môi trường của thiết bị không được ảnh hưởng bất lợi "
               "đến khả năng bảo vệ chống nổ của nó."))

    b.append(h4("Cấu tạo và sử dụng cơ bản", "Basic construction and use"))
    b.append(p("Thiết bị hoặc hệ thống bảo vệ phải được thiết kế và chế tạo "
               "sao cho, trong phạm vi dung sai quy định, trong vận hành bình "
               "thường và sau khi đã xảy ra bất kỳ lỗi nào dự kiến, và có tính "
               "đến bất kỳ việc kiểm tra và bảo trì nào mà nhà thiết kế dự "
               "liệu, nó không tạo ra điều kiện nguy hiểm. Điều kiện nguy hiểm "
               "trong ngữ cảnh này có nghĩa là nguy cơ cháy nổ không thể chấp "
               "nhận được."))
    b.append(note("<b>Ghi chú về ‘Dangerous condition in this context means’.</b> "
                  "Bản in lặp lại cụm ‘Dangerous condition’ trong cùng một câu; "
                  "bản tiếng Anh giữ nguyên sự lặp này."))

    b.append(h4("Thông tin", "Information"))
    b.append(p("Phải cung cấp đủ thông tin cùng với thiết bị để cho phép sử "
               "dụng an toàn. Nhà sản xuất có thể được yêu cầu cung cấp đủ "
               "thông tin cho phép sửa chữa; một mức độ thông tin mà một số "
               "nhà sản xuất không muốn cung cấp vì khả năng sao chép bản "
               "thiết kế."))

    b.append(h4("Ghi nhãn", "Marking"))
    b.append(p("Mọi thiết bị tuân thủ Chỉ thị đều được yêu cầu mang Dấu cộng "
               "đồng (Hình 16.1), Dấu bảo vệ chống nổ (Hình 16.2) và một dấu "
               "hiệu để thể hiện mối nguy mà nó được dự định giải quyết (là "
               "‘G’ đối với bầu khí quyển nổ dạng khí, hơi hoặc sương mù, và "
               "‘D’ nếu nó được dự định sử dụng cho nguy cơ bụi). Điều này, "
               "một cách quan trọng, thể hiện sự mở rộng việc sử dụng dấu "
               "‘Ex’ (Hình 16.2) sang cả hệ thống bảo vệ bên cạnh thiết bị "
               "được bảo vệ. Việc sử dụng ‘G’ và ‘D’ cũng là mới và có thể "
               "gây nhầm lẫn nếu không được xác định rõ cùng với dấu ‘Ex’."))
    b.append(fig(1, F.fig_f1601()))
    b.append(note("<b>Ghi chú về câu dùng ‘G’ và ‘D’ và về chú thích hình.</b> "
                  "Bản in dùng ‘are’ với cấu trúc số ít ‘The use of the G and "
                  "D’, và chú thích Hình 16.1 viết thường chữ ‘community’; bản "
                  "tiếng Anh giữ nguyên cả hai."))

    return "".join(b)


def body_en():
    b = []

    # A0-A3 (printed p.474) and B1 (printed p.475): chapter opening.
    b.append(h3("Chapter opening", "Chapter opening"))
    b.append(p("To fully understand the future approach to apparatus for use "
               "in explosive atmospheres it is necessary to consider the "
               "problems with the present system which is based upon Directive "
               "76/117/EEC¹ and its supplementary Directives. These define the "
               "detailed constructional standards with which apparatus must "
               "comply to be suitable for formal conformity certification by "
               "a ‘notified body’, as described in earlier chapters. This "
               "method of definition effectively restricted the types of "
               "equipment which could be used in Zone 0 and 1 as, although the "
               "Directive only addressed conformity certification as a method "
               "of European market admission, it effectively defined what "
               "could be used in those Zones because user industry was "
               "unwilling, in the main, to utilize any other type of "
               "equipment. This did not apply to Zone 2 as the approach was "
               "much more relaxed due to the much lesser risk envisaged."))
    b.append(p("In the case of Zone 0 and 1, however, the approach led to "
               "considerable restriction and inability to deal with "
               "technological advance and special circumstances. Accordingly, "
               "within a national arena, the UK exploited the protection "
               "concept known as special protection ‘s’. The objective of this "
               "concept was to provide a vehicle which would allow formal "
               "approval of apparatus which, while not complying (or not "
               "complying fully) with any of the standardized protection "
               "concepts (‘d’, ‘e’, ‘i’, ‘m’, ‘o’, ‘p’, ‘q’) achieved the "
               "minimum required level of security in respect of ignition "
               "capability. The objective of this was not to certify ‘near "
               "misses’ but to allow for advances in technology. The proof of "
               "the value of this approach is clear when it is recognized that "
               "it has been used for such protection concepts as encapsulation "
               "‘m’ and devices without measurable flamepaths, such as "
               "sinters, before these were included in the relevant protection "
               "concept Standard and specifically recognized by the Directive. "
               "More recently, the approach has been used to permit bi-pin "
               "tubes used in the cold cathode mode in luminaires on the basis "
               "of multiple (at least four) connections allowing redundancy, "
               "an approach not recognized in increased safety ‘e’, and to "
               "recognize gas detectors measuring oxygen, and similar "
               "apparatus where the oxygen concentration of the explosive "
               "atmosphere was enhanced and not covered by the standard "
               "protection concepts, on the basis of special testing (usually "
               "in oxygen enriched atmospheres)."))
    b.append(note("<b>Source quirks: ‘Zone 0 and 1’ and ‘q’.</b> The print reads "
                  "‘Zone 0 and 1’ twice (without repeating ‘Zone 1’), and the "
                  "list of protection concepts ends in ‘q’, not the ‘4’ "
                  "misread by the OCR; both are retained as printed."))
    # A3+B1 are one continuous paragraph across the printed 474/475 break.
    b.append(p("Within the UK, national certification to an agreed set of "
               "requirements has been historically available on the same basis "
               "as it has been for the more classic approaches to construction. "
               "Directive 76/117/EEC¹ attempted to address this problem by "
               "introducing the Inspection Certificate which allowed "
               "certification of special protection methods. This certificate, "
               "however, was noticeably different to the Certificate of "
               "Conformity and required, before issue, the agreement of all of "
               "the European notified bodies who had the right to perform "
               "their own tests at the expense of the manufacturer before "
               "granting such approval. The result of these two situations "
               "made the Inspection Certificate approach very unattractive and "
               "resulted in very few certificates being issued and, "
               "resultantly, slow advance in technology in the European "
               "scenario. In addition, 76/117/EEC addressed only the gas, "
               "vapour and mist scenario, leaving dusts outside European "
               "legislation."))
    b.append(note("<b>Source quirk: ‘resultantly, slow advance’.</b> The print "
                  "reads ‘resultantly, slow advance in technology in the "
                  "European scenario’; this wording is retained."))
    b.append(p("In the production of the new Directive 94/9/EC² an attempt has "
               "been made to overcome both of these problems. The new Directive "
               "does not refer to European Standards for definition of "
               "construction requirements but includes them as ‘essential "
               "requirements’ within its own text. This allows a much simpler "
               "method of addressing European Standards by merely referring to "
               "them in the EU Journal³ as Standards defining constructional "
               "requirements which satisfy essential requirements and removes "
               "the previous cumbersome Inspection Certificate approach by "
               "using Certificates of Conformity in all cases and providing a "
               "more rapid acceptance route for technological advance. In "
               "addition, apparatus for dust risks is now included together "
               "with protective systems, such as those used with pressurized "
               "apparatus ‘p’ which were hitherto not adequately addressed."))
    b.append(p("The one negative aspect of the new Directive, however, is its "
               "requirement for compliance. Under 76/117/EEC¹ use of conforming "
               "apparatus was optional, the Directive merely stating that "
               "member states could not prevent its import. Directive 94/9/EC² "
               "is quite different in that it prohibits marketing and putting "
               "into use of apparatus not complying with it thereby reducing "
               "widely used national flexibility. While it permits the "
               "76/117/EEC approach until the end of June 2003, and hence the "
               "use of apparatus subject to a Certificate of Conformity or an "
               "Inspection Certificate until that date, the marketing in "
               "member states of apparatus which does not conform to 76/117/EEC "
               "or 94/9/EC is already in force, having been introduced with the "
               "implementation of the new Directive."))

    # Heading 16.1 and B5+C1 (printed pp.475/476) as one paragraph.
    b.append(h3("16.1 Acceptance of technical requirements",
                "16.1 Acceptance of technical requirements"))
    b.append(p("As already stated, the essential requirements for construction "
               "of apparatus in order to comply with 94/9/EC are contained "
               "within the Directive itself. These are, however, considered as "
               "insufficiently detailed to allow construction of apparatus and "
               "CENELEC⁴ has the mandate to produce Standards which satisfy the "
               "‘essential requirements’ and contain the required level of "
               "detail. This activity is expected to be complete for ‘d’, ‘e’, "
               "‘i’, ‘m’, ‘o’, ‘p’ and ‘q’ in mid-1997 and for some time later. "
               "The situation in regard to ‘n’ is not quite so difficult as "
               "the Directive maintained the lower level of certification "
               "formality previously used in Zone 2 equipment. When produced, "
               "these European Standards will be identified in the EU Journal "
               "as satisfying ‘essential requirements’ and any future additions "
               "will also follow this route. Thus technological progress is "
               "placed clearly in the hands of the technical-standards-making "
               "body and a much more rapid route to recognition is made "
               "available. How this will ultimately operate is not yet clear "
               "but if the approach is positive then a much more flexible "
               "situation should emerge."))
    b.append(note("<b>Source quirks: ‘technical-standards-making body’ and "
                  "‘94/9/EC’.</b> The print has ‘technical-standards-making "
                  "body’ with two hyphens, and in section 16.1 writes ‘94/9/EC’ "
                  "without the superscript ²; both are retained."))

    # Heading 16.2, C3 and C4 (printed p.476).
    b.append(h3("16.2 Essential requirements", "16.2 Essential requirements"))
    b.append(p("The ‘essential requirements’, not withstanding their technical "
               "impact were, in fact, written by employees of the European "
               "Commission taking such advice as they felt necessary. They "
               "tend to specify the objectives to be achieved in a general way "
               "and leave the technical rules necessary for the achievement of "
               "these objectives to others. While this approach is generally "
               "reasonable it does throw up some curious anomalies as will be "
               "seen later in this chapter."))
    b.append(note("<b>Source quirk: ‘not withstanding’.</b> The print writes "
                  "‘not withstanding’ as two words; this is retained even "
                  "though the meaning is ‘despite’."))
    b.append(p("The requirements apply, unlike those of 76/117/EEC,¹ to both "
               "electrical risks and mechanical risks, although implementation "
               "in the case of mechanical risks is delayed as there are "
               "currently no Standards which can be used to identify detailed "
               "requirements. They are divided into three parts:"))
    b.append(note("<b>Source quirk: ‘76/117/EEC,¹’.</b> The print places the "
                  "reference marker ¹ after the comma; this is retained."))

    # Heading 16.2.1, lead-in C6 and the five unnumbered requirements.
    b.append(h4("16.2.1 General requirements", "16.2.1 General requirements"))
    b.append(p("These identify five basic requirements which apparatus must "
               "meet:"))

    b.append(h4("Principles", "Principles"))
    b.append(p("The equipment is required to prevent, if possible, any "
               "explosive atmosphere being formed by any gas, vapour, mist or "
               "dust which it may itself release and prevent, as far as "
               "possible, any ignition of an explosive atmosphere formed by is "
               "own release or otherwise. Where it cannot do this it is "
               "required to contain the explosion as far as possible to "
               "prevent damage or injury."))
    b.append(note("<b>Source quirk: ‘formed by is own release’.</b> The print "
                  "reads ‘is’, not ‘its’, in ‘formed by is own release or "
                  "otherwise’; this is retained verbatim."))

    b.append(h4("Environmental requirements", "Environmental requirements"))
    b.append(p("The apparatus or protective system (protective systems, such "
               "as shut-down systems, are included) is required to be capable "
               "of operation without damage or deterioration in the "
               "environmental conditions in which it is intended to be used. "
               "This is not uniquely an explosive atmosphere requirement but "
               "is very important in the explosive atmosphere context; if the "
               "apparatus deteriorates excessively then so may its explosion "
               "protection elements. Thus any identified problems with its "
               "environment must not adversely affect its explosion "
               "protection."))

    b.append(h4("Basic construction and use", "Basic construction and use"))
    b.append(p("The apparatus or protective system must be designed and "
               "manufactured so that within its specified tolerances, in normal "
               "operation and with any expected faults having occurred, and "
               "taking account of any required checking and maintenance "
               "envisaged by the designer, it does not create a dangerous "
               "condition. Dangerous condition in this context means an "
               "unacceptable risk of ignition."))
    b.append(note("<b>Source quirk: ‘Dangerous condition in this context "
                  "means’.</b> The print repeats ‘Dangerous condition’ within "
                  "the same sentence; this repetition is retained."))

    b.append(h4("Information", "Information"))
    b.append(p("Sufficient information must be supplied with the equipment to "
               "allow its safe use. Manufacturers may well be required to "
               "release sufficient information to permit repair; a level of "
               "information which some manufacturers are reluctant to release "
               "because of the possibility of copying of designs."))

    b.append(h4("Marking", "Marking"))
    b.append(p("All apparatus complying with the Directive is required to carry "
               "the Community Mark (Fig. 16.1), the Explosion Protection Mark "
               "(Fig. 16.2) and a mark to indicate the hazard which it is "
               "intended to address (which is ‘G’ in respect of explosive "
               "atmospheres of gas, vapour or mist, and ‘D’ if it is intended "
               "for use in respect of dust risks). This, importantly, "
               "represents an extension of the use of the ‘Ex’ mark (Fig. "
               "16.2) to protective systems as well as protected apparatus. "
               "The use of the ‘G’ and ‘D’ are also new and may cause some "
               "confusion unless clearly identified with the ‘Ex’ mark."))
    b.append(fig(1, F.fig_f1601()))
    b.append(note("<b>Source quirks: the ‘G’ and ‘D’ sentence and the caption.</b> "
                  "The print reads ‘The use of the ‘G’ and ‘D’ are also new’, "
                  "with the plural ‘are’ after a singular construction, and "
                  "the Fig. 16.1 caption prints ‘community’ with a lowercase "
                  "c; both are retained."))

    return "".join(b)
