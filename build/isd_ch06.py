# -*- coding: utf-8 -*-
"""Book 5, Chapter 6 — Inherent Safety (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 31–38.  Three sections: an essay
introduction, §6.1 The Principles of Inherent Safety (Kletz's twelve
principles), §6.2 Inherent Safety in Preliminary Process Design and §6.3
Evaluation of Inherent Safety.  The source contains one figure — Figure 4
(p. 36, after Kletz 1991) — redrawn here as `fig_c06_kletz`; the tiered
`fig_c06_principles` is an explicitly labelled editorial schematic of §6.1.
"""

from isd_common import fig, h2, h3, note, p
import isdfig as F

PAGES_SRC = 8           # source pages 31–38
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Inherent Safety"
TITLE_VI = "An toàn nội tại"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 6.</b> an toàn nội tại — an toàn nhờ "
                "đặc tính bản chất của quá trình, không nhờ thiết bị bảo vệ "
                "bổ sung · Kletz — người phát biểu nguyên tắc an toàn nội tại "
                "từ cuối thập niên 1970 · Flixborough (1974) — vụ nổ thúc đẩy "
                "ra đời tư tưởng thiết kế an toàn nội tại · cường tập hóa "
                "(intensification) — giảm tồn kho chất nguy hiểm · thay thế "
                "(substitution) — dùng vật liệu an toàn hơn · suy yếu "
                "(attenuation) — điều kiện phản ứng dịu hơn · Inherent SHE — "
                "an toàn, môi trường và sức khỏe tích hợp · SEVESO II · OSHA "
                "PSM · EMAS · ISO 14000 · Responsible Care · PIIS — Chỉ số "
                "Nguyên mẫu An toàn Nội tại (Edwards &amp; Lawrence, 1993) · "
                "INSIDE / InSPIRE — dự án và bộ công cụ đánh giá an toàn "
                "nội tại.")
    return ("<b>Key terms.</b> inherent safety — safety by the essential "
            "nature of the process rather than by added-on protective "
            "equipment · Kletz — first formulated the principles in the late "
            "1970s · Flixborough (1974) — the explosion that spurred inherently "
            "safer design · intensification — smaller inventories of "
            "hazardous materials · substitution — using safer materials · "
            "attenuation — less hazardous conditions · Inherent SHE — safety, "
            "environment and health integrated · SEVESO II · OSHA PSM · EMAS · "
            "ISO 14000 · Responsible Care · PIIS — Prototype Index of "
            "Inherent Safety (Edwards &amp; Lawrence, 1993) · INSIDE / "
            "InSPIRE — project and toolkit for inherently safer design.")


# ---------------------------------------------------------------------------
def body_vi():
    b = []

    b.append(p("Cách tốt nhất để đối phó với một mối nguy là <b>loại bỏ hoàn toàn "
               "mối nguy đó</b>. Việc trang bị các phương tiện để kiểm soát mối "
               "nguy chỉ là giải pháp thứ hai. Như Lees (1996) đã nói, mục tiêu "
               "phải là thiết kế quá trình và nhà máy sao cho chúng an toàn nội "
               "tại hơn."))
    b.append(p("Từ <i>\"nội tại\"</i> (inherent) được định nghĩa trong từ điển "
               "American College Dictionary là \"hiện hữu trong một sự vật như "
               "một yếu tố, phẩm chất hay thuộc tính thường trực và không thể "
               "tách rời\". Vì vậy, một quá trình hóa học an toàn nội tại hơn là "
               "an toàn nhờ những đặc tính bản chất của nó — những đặc tính "
               "thuộc về quá trình một cách tự nhiên. Thiết kế an toàn nội tại "
               "là thiết kế <b>tránh mối nguy thay vì kiểm soát mối nguy</b>, "
               "đặc biệt bằng cách loại bỏ hoặc giảm lượng vật liệu nguy hiểm "
               "trong nhà máy và số lượng các thao tác nguy hiểm."))
    b.append(p("An toàn nội tại lần đầu được phát biểu rộng rãi vào cuối thập "
               "niên 1970 bởi Trevor Kletz. Các nguyên tắc cơ bản đều là lẽ "
               "thường: tránh dùng vật liệu nguy hiểm, tối thiểu hóa tồn kho "
               "chất nguy hiểm, hướng tới các quá trình đơn giản hơn với các "
               "phương án ôn hòa hơn (Kletz, 1984)."))
    b.append(p("Dù nguyên tắc cơ bản của thiết kế an toàn nội tại nhìn chung "
               "được chấp nhận, việc áp dụng không phải lúc nào cũng dễ dàng. "
               "Thiết kế an toàn nội tại đã được cổ vũ từ vụ nổ Flixborough "
               "năm 1974. Tiến bộ là có thật, nhưng khái niệm này chưa được "
               "chấp nhận nhanh như đánh giá rủi ro định lượng — vốn được đưa "
               "vào ngành hóa học chỉ vài năm trước đó (Kletz, 1996)."))
    b.append(p("Có ý kiến cho rằng các phương pháp phát triển cho đến nay chủ "
               "yếu dùng để <b>đánh giá</b> an toàn của một thiết kế đã đề xuất. "
               "Trong tương lai, các chuyên gia an toàn kỳ vọng thấy nhiều hơn "
               "việc dùng tri thức để <b>tổng hợp</b> thiết kế an toàn ngay từ "
               "đầu. Theo họ, giá trị của an toàn nội tại đã được thừa nhận, "
               "nhưng vẫn còn dư địa để nâng cao nhận thức và thực hành. Lo "
               "ngại của các chuyên gia là thực tiễn tốt nhất chưa được các "
               "người sử dụng tiềm năng áp dụng đủ nhanh (Preston, 1998)."))
    b.append(p("Mansfield (1994) chỉ ra rằng trong công nghiệp ngày càng cần "
               "xem xét — và đôi khi cân bằng — các khía cạnh sức khỏe, an toàn "
               "và môi trường trên toàn bộ vòng đời. Điều đó cho thấy trong "
               "thực tế nên nói về <b>Inherent SHE</b> (An toàn – Môi trường – "
               "Sức khỏe nội tại) thay vì chỉ an toàn nội tại thuần túy. Đặc "
               "biệt trong quản lý an toàn, sức khỏe và bảo vệ môi trường cần "
               "tích hợp pháp luật (ví dụ SEVESO II, OSHA Process Safety "
               "Management) và các hệ thống như EMAS, ISO 14000, Responsible "
               "Care (Turney, 1998). Nếu không, có thể tạo ra các tình huống "
               "xung đột: chẳng hạn tiết kiệm năng lượng quan trọng về môi "
               "trường và kinh tế lại có thể dẫn đến giải pháp quá trình kém "
               "an toàn nội tại hơn (xem Hình 9 ở chương sau)."))

    # ---- 6.1 -----------------------------------------------------------------
    b.append(h2("6.1 Nguyên tắc của an toàn nội tại",
                "6.1 The Principles of Inherent Safety"))
    b.append(p("An toàn nội tại là sự theo đuổi việc <b>thiết kế để loại bỏ "
               "mối nguy khỏi quá trình</b>, thay vì dùng các biện pháp kỹ "
               "thuật hay quy trình để giảm thiểu rủi ro. Vì thế an toàn nội "
               "tại cố gắng tránh và loại bỏ mối nguy thay vì kiểm soát chúng "
               "bằng các hệ thống bổ sung thêm. An toàn nội tại được xem xét "
               "tốt nhất ở giai đoạn đầu của thiết kế — khi lựa chọn lộ trình "
               "quá trình và khái niệm thiết kế."))
    b.append(p("Kletz (1984, 1991) đã đưa ra các nguyên tắc cơ bản của an toàn "
               "nội tại như sau:"))

    b.append(h3("Cường tập hóa — Intensification"))
    b.append(p("\"Cái bạn không có thì không thể rò rỉ.\" Tồn kho vật liệu "
               "nguy hiểm nhỏ làm giảm hậu quả của rò rỉ. Tồn kho thường có "
               "thể giảm được ở hầu hết mọi thao tác công nghệ cũng như lưu "
               "trữ. Điều này còn giảm chi phí: vật liệu ít hơn cần bồn nhỏ "
               "hơn, kết cấu và móng nhỏ hơn."))
    b.append(h3("Thay thế — Substitution"))
    b.append(p("Nếu không thể cường tập hóa, một phương án là thay thế. Có thể "
               "thay môi chất lạnh và trung gian truyền nhiệt cháy được bằng "
               "loại không cháy, thay sản phẩm nguy hiểm bằng sản phẩm an toàn "
               "hơn, và thay các quá trình dùng nguyên liệu hay trung gian "
               "nguy hiểm bằng các quá trình không dùng. Dùng vật liệu an toàn "
               "hơn làm giảm nhu cầu thiết bị bảo vệ bổ sung, do đó giảm chi "
               "phí và độ phức tạp của nhà máy."))
    b.append(h3("Suy yếu — Attenuation"))
    b.append(p("Nếu cường tập hóa và thay thế không thể thực hiện được, một "
               "phương án là suy yếu: thực hiện phản ứng nguy hiểm trong điều "
               "kiện ít nguy hiểm hơn, hoặc lưu trữ, vận chuyển vật liệu nguy "
               "hiểm ở dạng ít nguy hiểm hơn. Đôi khi suy yếu ngược với cường "
               "tập hóa, vì điều kiện phản ứng ít khắc nghiệt hơn có thể kéo "
               "dài thời gian lưu."))
    b.append(h3("Giới hạn hệ quả — Limitation of Effects"))
    b.append(p("Nếu không thể làm nhà máy an toàn hơn bằng cường tập hóa, thay "
               "thế hay suy yếu thì phải giới hạn hệ quả của sự cố. Ví dụ thiết "
               "bị được thiết kế sao cho nếu rò rỉ cũng chỉ ở tốc độ thấp, dễ "
               "dừng hoặc dễ kiểm soát; gioăng được chọn để giảm tối đa tốc độ "
               "rò rỉ. Giới hạn hệ quả nên thực hiện bằng thiết kế thiết bị "
               "hay thay đổi điều kiện phản ứng, thay vì thêm thiết bị bảo vệ."))
    b.append(h3("Đơn giản hóa — Simplification"))
    b.append(p("Nhà máy đơn giản an toàn nội tại hơn nhà máy phức tạp, vì ít "
               "cơ hội mắc lỗi hơn và ít thiết bị có thể hỏng hơn. Nhà máy đơn "
               "giản thường rẻ hơn và thân thiện với người vận hành hơn."))
    b.append(h3("Thay đổi sớm — Change Early"))
    b.append(p("Thay đổi sớm nghĩa là nhận diện mối nguy càng sớm càng tốt "
               "trong thiết kế quá trình. Kết quả của việc nhận diện mối nguy "
               "sớm có thể quyết định thành bại của ngân sách đầu tư cho một "
               "quá trình mới. Điều này đạt được bằng các phương pháp đánh giá "
               "an toàn chuyên dụng, được thiết kế cho mục đích thiết kế sơ "
               "bộ."))
    b.append(h3("Tránh hiệu ứng dây chuyền — Avoiding Knock-On Effects"))
    b.append(p("Nhà máy an toàn hơn được thiết kế để các sự cố xảy ra không "
               "gây hiệu ứng dây chuyền hay domino. Ví dụ bố trí vách ngăn "
               "cháy giữa các khu vực để hạn chế cháy lan; với vật liệu cháy, "
               "nhà máy xây ngoài trời để rò rỉ được khuếch tán bằng thông "
               "gió tự nhiên."))
    b.append(h3("Làm rõ trạng thái — Making Status Clear"))
    b.append(p("Thiết bị nên được chọn sao cho dễ nhìn thấy nó đã lắp đúng "
               "chưa, đang ở trạng thái mở hay đóng. Đây là công thái học của "
               "nhà máy. Cũng cần giải thích rõ hóa học của quá trình để nhân "
               "lực vận hành nhận diện được các mối nguy tiềm ẩn."))
    b.append(h3("Không thể lắp sai — Making Incorrect Assembly Impossible"))
    b.append(p("Nhà máy an toàn được thiết kế để việc lắp ráp sai khó hoặc "
               "không thể xảy ra. Các chi tiết lắp ghép phải đáp ứng yêu cầu "
               "thiết kế. Rò rỉ có thể xảy ra chỉ vì dùng sai loại gioăng."))
    b.append(h3("Chịu lỗi — Tolerance"))
    b.append(p("Thiết bị nên chịu được vận hành sai, lắp đặt hay bảo dưỡng "
               "kém mà không hỏng. Ví dụ vòng giãn nở trên đường ống chịu lắp "
               "đặt kém tốt hơn ống lượn (bellows). Vật liệu kết cấu phải "
               "chống được ăn mòn và điều kiện vật lý; với đa số ứng dụng kim "
               "loại an toàn hơn thủy tinh hay nhựa."))
    b.append(h3("Dễ điều khiển — Ease of Control"))
    b.append(p("Quá trình nên được điều khiển bằng các nguyên lý vật lý thay "
               "vì thiết bị điều khiển bổ sung — tức là động lực học của quá "
               "trình phải thuận lợi. Nếu quá trình khó điều khiển, hãy tìm "
               "cách thay đổi quá trình hoặc nguyên lý điều khiển trước khi "
               "đầu tư vào hệ thống điều khiển phức tạp."))
    b.append(h3("Kiểm soát hành chính / quy trình — Administrative Controls"))
    b.append(p("Lỗi con người là nguyên nhân thường gặp nhất của mất khả năng "
               "chứ (loss of containment). Đào tạo và cấp chứng chỉ cho nhân "
               "lực về các quy trình quan trọng là việc làm thường xuyên. Các "
               "nguyên tắc khác như dễ điều khiển, làm rõ trạng thái, chịu "
               "lỗi và không thể lắp sai cũng phát huy tác dụng ở đây."))
    b.append(fig(1, F.fig_c06_principles()))
    b.append(p("Thiết kế an toàn nội tại cần chứa đựng các nguyên tắc nêu trên "
               "và chúng phải phủ suốt tiến trình thiết kế. Ở giai đoạn đầu "
               "của thiết kế quá trình, các nguyên tắc này giúp chọn vật liệu, "
               "điều kiện quá trình và thậm chí công nghệ quá trình an toàn "
               "nhất. Khó khăn hiện nay là <b>thiếu các quy trình vận hành "
               "để đưa các nguyên tắc an toàn nội tại vào thực tế</b>."))

    # ---- 6.2 -----------------------------------------------------------------
    b.append(h2("6.2 An toàn nội tại trong thiết kế sơ bộ quá trình",
                "6.2 Inherent Safety in Preliminary Process Design"))
    b.append(p("Khả năng tác động đến an toàn nội tại của một quá trình <b>giảm "
               "dần khi thiết kế tiến triển</b> và ngày càng nhiều quyết định "
               "kỹ thuật, tài chính đã được đưa ra (Hình 4). Thay đổi cấu hình "
               "quá trình và an toàn nội tại ở giai đoạn thiết kế khái niệm "
               "dễ hơn nhiều so với các giai đoạn sau. Ví dụ việc chọn lộ "
               "trình quá trình được thực hiện ở thiết kế khái niệm và thường "
               "rất khó, rất đắt nếu muốn đổi lộ trình sau đó. Thời gian và "
               "tiền bạc cũng được tiết kiệm khi cần ít sửa đổi an toàn tốn "
               "kém và ít thiết bị an toàn bổ sung trong giải pháp cuối cùng."))
    b.append(fig(2, F.fig_c06_kletz()))
    b.append(p("Ở các giai đoạn đầu của thiết kế, thông tin sẵn có chỉ giới "
               "hạn ở sản phẩm, sản phẩm phụ và nguyên liệu, công suất, thiết "
               "bị chính và một dải thô của điều kiện quá trình (nhiệt độ, áp "
               "suất). Từ các bước của Suokas và Kakko (1993) ở Hình 2, chỉ "
               "<b>nhận diện mối nguy</b> có thể thực hiện một phần trong thiết "
               "kế sơ bộ. Tuy nhiên chính ở giai đoạn sớm nhất, các thay đổi "
               "vì an toàn có lợi nhất: chưa có gì được xây dựng hay đặt "
               "hàng, nên không cần sửa đổi tốn kém."))

    # ---- 6.3 -----------------------------------------------------------------
    b.append(h2("6.3 Đánh giá an toàn nội tại",
                "6.3 Evaluation of Inherent Safety"))
    b.append(p("Như Hendershot (1995) chỉ ra, <b>hầu hết các phương án quá "
               "trình sẽ an toàn nội tại hơn theo một loại mối nguy, nhưng có "
               "thể kém an toàn theo góc nhìn khác</b>. Trong một số trường "
               "hợp tổng thể cân bằng là hiển nhiên và dễ thống nhất phương án "
               "nào cân bằng an toàn tốt nhất. Trong các trường hợp khác, sự "
               "cân bằng ít rõ ràng hơn và cần các công cụ tinh vi hơn: bảng "
               "xếp hạng định tính, phân tích rủi ro định lượng và công cụ ra "
               "quyết định chính thức."))
    b.append(p("Nhiều tác giả đề xuất các phương pháp cho thiết kế an toàn nội "
               "tại. Công cụ trải từ các phương pháp mở, có hệ thống như phân "
               "tích What-If (CCPS, 1992) và \"critical examination\" (Wells et "
               "al., 1993), đến các checklist chi tiết (CCPS, 1992; "
               "Hendershot, 1991; Englund, 1994; Lutz, 1994). Hendershot "
               "(1994) đề nghị dùng các kỹ thuật phân tích quyết định để xử "
               "lý các yếu tố kinh tế, kỹ thuật và SHE khi tối ưu việc chọn "
               "lộ trình và thiết kế nhà máy; các công ty dẫn đầu khác cũng "
               "đang cân nhắc hoặc áp dụng cách tiếp cận tương tự."))
    b.append(p("Các chỉ số như Chỉ số cháy và nổ Dow và Chỉ số Mond cũng được "
               "đề nghị để đo mức độ SHE nội tại của một quá trình. Rushton et "
               "al. (1994) chỉ ra các chỉ số này phù hợp để đánh giá nhà máy "
               "hiện hữu hoặc ở giai đoạn thiết kế chi tiết: chúng đòi hỏi "
               "thông số chi tiết như sơ đồ bố trí mặt bằng, kích thước thiết "
               "bị, tồn kho vật liệu và dòng chảy. Checklist, ma trận tương "
               "tác, Hazop và các công cụ nhận diện mối nguy khác cũng dùng "
               "được cho đánh giá, vì mọi mối nguy phải được nhận diện và hậu "
               "quả tiềm tàng phải được hiểu rõ. Chẳng hạn Hazop dùng được ở "
               "các giai đoạn khác nhau của thiết kế nhưng ở chế độ giới hạn: "
               "một nghiên cứu Hazop hoàn chỉnh đòi hỏi bản vẽ quá trình cuối "
               "cùng cùng sơ đồ dòng và P&amp;ID."))
    b.append(p("P.I.I.S. do Edwards và Lawrence (1993) phát triển nhằm ước "
               "lượng an toàn nội tại của <b>mối nguy phản ứng ở giai đoạn "
               "thiết kế khái niệm</b> — phân tích lựa chọn lộ trình quá trình, "
               "tức nguyên liệu và trình tự các bước phản ứng (xem Chương 4)."))
    b.append(p("Dự án INSIDE (INSIDE, 1997) đã phát triển bộ công cụ tên "
               "InSPIRE — một hyperbook cung cấp cho các nhà hóa học và kỹ sư "
               "công cụ, phương pháp để nhận diện, đánh giá, tối ưu và chọn "
               "các quá trình, thiết kế hóa học SHE nội tại một cách có hệ "
               "thống. Các mối nguy an toàn, sức khỏe, môi trường được xử lý "
               "tích hợp để xung đột và hiệp đồng giữa các khía cạnh được nhận "
               "diện và quản lý hiệu quả. Bộ công cụ đặc biệt tập trung vào "
               "các giai đoạn đầu của dự án — nơi hầu hết các quyết định chính "
               "quyết định hiệu năng SHE của nhà máy được đưa ra. Hiện hyperbook "
               "InSPIRE không còn sẵn có; cuối dự án nhiều công cụ trong bộ "
               "còn cần phát triển hoặc kiểm chứng thêm."))
    b.append(note("Kết luận của chương: có rất nhiều phương pháp đánh giá an "
                  "toàn nội tại, nhưng <b>chúng không trực tiếp phù hợp làm "
                  "công cụ phân tích an toàn cho các hệ thống thiết kế mới "
                  "trong thiết kế sơ bộ quá trình</b>. Đa số phương pháp hiện "
                  "có cần thông tin quá trình chi tiết và không áp dụng trực "
                  "tiếp được ở giai đoạn thiết kế sớm; mặt khác, không phải "
                  "phương pháp nào cũng thích hợp để dùng máy hóa cùng các "
                  "công cụ tối ưu hóa và mô phỏng. Chính khoảng trống này "
                  "dẫn tới Chỉ số An toàn Nội tại được trình bày từ Chương 8."))
    return "".join(b)


# ---------------------------------------------------------------------------
def body_en():
    b = []

    b.append(p("The best way of dealing with a hazard is to <b>remove it "
               "completely</b>. The provision of means to control the hazard is "
               "very much the second solution. As Lees (1996) has said, the aim "
               "should be to design the process and plant so that they are "
               "inherently safer."))
    b.append(p("\"Inherent\" is defined by the American College Dictionary as "
               "\"existing in something as a permanent and inseparable element, "
               "quality or attribute\". Thus an inherently safer chemical "
               "process is safer because of its essential characteristics — "
               "those which belong to the process by its very nature. An "
               "inherently safer design is one that <b>avoids hazards instead "
               "of controlling them</b>, particularly by removing or reducing "
               "the amount of hazardous material in the plant or the number of "
               "hazardous operations."))
    b.append(p("Inherent safety was first widely expressed in the late 1970s by "
               "Trevor Kletz. The basic principles are common sense: avoid the "
               "use of hazardous materials, minimise the inventories of "
               "hazardous materials and aim for simpler processes with more "
               "benign and moderate process alternatives (Kletz, 1984)."))
    b.append(p("While the basic principle of inherently safer design is "
               "generally accepted, it is not always easy to put into "
               "practice. Inherently safer design has been advocated since the "
               "explosion at Flixborough in 1974. Progress has been real, but "
               "nevertheless the concept has not been adopted nearly as "
               "rapidly as quantitative risk assessment, which was introduced "
               "into the chemical industry only a few years earlier (Kletz, "
               "1996)."))
    b.append(p("It has been commented that methods developed to date have "
               "largely been for <b>evaluating</b> the safety of some proposed "
               "design. In the future, safety experts expect to see a greater "
               "emphasis on the use of knowledge to <b>synthesize</b> a safe "
               "plant design in the first place. In their opinion the value of "
               "inherent safety has been recognised, but there is still room "
               "for better awareness and practice. The concern expressed by "
               "inherent safety experts is that best practice is not being "
               "adopted quickly enough by the potential practitioners "
               "(Preston, 1998)."))
    b.append(p("Mansfield (1994) has pointed out that in industry there is an "
               "increasing need to address — and sometimes balance — the "
               "overall lifecycle health, safety and environmental aspects of "
               "performance. This shows that in real life we should talk about "
               "<b>Inherent SHE</b> (Safety, Environment and Health) instead of "
               "plain inherent safety. Especially in the management of safety, "
               "health and environmental protection, integration of legislation "
               "(e.g. SEVESO II, OSHA Process Safety Management) and systems "
               "such as EMAS, ISO 14000 and Responsible Care is needed (Turney, "
               "1998). Otherwise it is possible to create conflict situations: "
               "for example, environmentally and economically important energy "
               "savings may lead to inherently less safe process solutions "
               "(see Figure 9 in the following chapter)."))

    # ---- 6.1 -----------------------------------------------------------------
    b.append(h2("6.1 The Principles of Inherent Safety",
                "6.1 Nguyên tắc của an toàn nội tại"))
    b.append(p("Inherent safety is the pursuit of <b>designing hazards out of "
               "a process</b>, as opposed to using engineering or procedural "
               "controls to mitigate risk. Inherent safety therefore strives "
               "to avoid and remove hazards rather than to control them by "
               "added-on systems. It is best considered in the initial stages "
               "of design, when the choice of process route and concept is "
               "made."))
    b.append(p("Kletz (1984, 1991) has given the Basic Principles of Inherent "
               "Safety as follows:"))

    b.append(h3("Intensification", "Cường tập hóa"))
    b.append(p("\"What you don't have, can't leak.\" Small inventories of "
               "hazardous materials reduce the consequences of leaks. "
               "Inventories can often be reduced in almost all unit operations "
               "as well as storage. This also brings reductions in cost, since "
               "less material needs smaller vessels, structures and "
               "foundations."))
    b.append(h3("Substitution", "Thay thế"))
    b.append(p("If intensification is not possible, an alternative is "
               "substitution. It may be possible to replace flammable "
               "refrigerants and heat transfer media with non-flammable ones, "
               "hazardous products with safer ones, and processes that use "
               "hazardous raw materials or intermediates with processes that "
               "do not. Using a safer material in place of a hazardous one "
               "decreases the need for added-on protective equipment and thus "
               "decreases plant cost and complexity."))
    b.append(h3("Attenuation", "Suy yếu"))
    b.append(p("If intensification and substitution are not possible or "
               "practicable, an alternative is attenuation: carrying out a "
               "hazardous reaction under less hazardous conditions, or storing "
               "or transporting a hazardous material in a less hazardous form. "
               "Attenuation is sometimes the reverse of intensification, "
               "because less extreme reaction conditions may lead to a longer "
               "residence time."))
    b.append(h3("Limitation of Effects", "Giới hạn hệ quả"))
    b.append(p("If it is not possible to make plants safer by intensification, "
               "substitution or attenuation, the effects of a failure should "
               "be limited. For instance, equipment is designed so that it can "
               "leak only at a low rate that is easy to stop or control, and "
               "gaskets are chosen to minimise leak rates. Limitation of "
               "effects should be achieved by equipment design or a change in "
               "reaction conditions rather than by adding on protective "
               "equipment."))
    b.append(h3("Simplification", "Đơn giản hóa"))
    b.append(p("Simpler plants are inherently safer than complex plants, "
               "because they provide fewer opportunities for error and contain "
               "less equipment that can go wrong. Simpler plants are usually "
               "also cheaper and more user friendly."))
    b.append(h3("Change Early", "Thay đổi sớm"))
    b.append(p("Change Early means identification of hazards as early as "
               "possible in the process design. The payback for early hazard "
               "identification can make or break the capital budget of a new "
               "process. This can be achieved by dedicated safety evaluation "
               "methodologies designed for preliminary process design "
               "purposes."))
    b.append(h3("Avoiding Knock-On Effects", "Tránh hiệu ứng dây chuyền"))
    b.append(p("Safer plants are designed so that incidents which do occur do "
               "not produce knock-on or domino effects. For example, safer "
               "plants are provided with fire breaks between sections to "
               "restrict the spread of fire, or — where flammable materials "
               "are handled — the plant is built out-of-doors so that leaks "
               "can be dispersed by natural ventilation."))
    b.append(h3("Making Status Clear", "Làm rõ trạng thái"))
    b.append(p("Equipment should be chosen so that it can easily be seen "
               "whether it has been installed correctly or whether it is in "
               "the open or shut position. This refers to the ergonomics of "
               "the plant. A clear explanation of the chemistry involved in "
               "the process also helps operating personnel identify possible "
               "hazards."))
    b.append(h3("Making Incorrect Assembly Impossible", "Không thể lắp sai"))
    b.append(p("Safe plants are designed so that incorrect assembly is "
               "difficult or impossible. Assembled components must meet their "
               "design requirements: a loss of containment may result from "
               "using, for example, the wrong type of gaskets."))
    b.append(h3("Tolerance", "Chịu lỗi"))
    b.append(p("Equipment should tolerate maloperation, poor installation or "
               "maintenance without failure. Expansion loops in pipework, for "
               "example, are more tolerant of poor installation than "
               "bellows. Construction materials should be resistant to "
               "corrosion and to the physical conditions; for most "
               "applications metal is safer than glass or plastic."))
    b.append(h3("Ease of Control", "Dễ điều khiển"))
    b.append(p("A process should be controlled by the use of physical "
               "principles rather than added-on control equipment — that is, "
               "the dynamics of the process should be favourable. If a process "
               "is difficult to control, one should look for ways of changing "
               "the process or the principles of control before investing in a "
               "complex control system."))
    b.append(h3("Administrative Controls / Procedures",
                "Kiểm soát hành chính / quy trình"))
    b.append(p("Human error is the most frequent cause of loss of containment. "
               "Training and certification of personnel on critical procedures "
               "are permanent considerations. Other inherent safety principles "
               "— ease of control, making status clear, tolerance and making "
               "incorrect assembly impossible — also come into play here."))
    b.append(fig(1, F.fig_c06_principles()))
    b.append(p("An inherently safe design should contain the principles "
               "mentioned above, and they should cover the whole design "
               "process. In the early stages of process design these "
               "principles help to choose the safest materials, process "
               "conditions and even process technology. The present difficulty "
               "is the <b>lack of routines to implement these inherent safety "
               "principles into reality</b>."))

    # ---- 6.2 -----------------------------------------------------------------
    b.append(h2("6.2 Inherent Safety in Preliminary Process Design",
                "6.2 An toàn nội tại trong thiết kế sơ bộ quá trình"))
    b.append(p("The possibility of affecting the inherent safety of a process "
               "<b>decreases as the design proceeds</b> and more and more "
               "engineering and financial decisions have been made (Figure 4). "
               "It is much easier to affect the process configuration and "
               "inherent safety in the conceptual design phase than in the "
               "later phases. For instance, the process route selection is "
               "made in conceptual design, and it is many times difficult and "
               "expensive to change the route later. Time and money are also "
               "saved when fewer expensive safety modifications are needed and "
               "fewer added-on safety devices are included in the final "
               "solution."))
    b.append(fig(2, F.fig_c06_kletz()))
    b.append(p("In the early design phases the available information is "
               "limited to products, by-products and raw materials, capacity, "
               "main process equipment and a rough range of process conditions "
               "such as temperature and pressure. Of the steps of Suokas and "
               "Kakko (1993) in Figure 2, only <b>hazard identification</b> "
               "can partly be done in preliminary process design. In the early "
               "phases of a plant design, however, changes for safety are the "
               "most profitable: nothing has been built or ordered yet, so no "
               "expensive modifications are needed."))

    # ---- 6.3 -----------------------------------------------------------------
    b.append(h2("6.3 Evaluation of Inherent Safety",
                "6.3 Đánh giá an toàn nội tại"))
    b.append(p("As Hendershot (1995) has pointed out, <b>most process options "
               "will be inherently safer with respect to one type of hazard, "
               "but may be less safe from a different viewpoint</b>. In some "
               "cases the overall balance is readily apparent and it is easy "
               "to reach general agreement on which option offers the safest "
               "overall balance. In other cases the balance is less apparent, "
               "and more sophisticated tools are needed — qualitative ranking "
               "schemes, quantitative risk analysis and formal decision-making "
               "tools."))
    b.append(p("Several authors have put forward ideas for methods to be used "
               "in inherently safer design. Tools range from systematic open "
               "methods such as What-If analysis (CCPS, 1992) and critical "
               "examination (Wells et al., 1993), through to detailed "
               "checklists (CCPS, 1992; Hendershot, 1991; Englund, 1994; Lutz, "
               "1994). Hendershot (1994) has proposed decision analysis "
               "techniques to help address the economic, engineering and SHE "
               "factors that arise when optimising route selection and plant "
               "design; similar approaches are being considered or used by "
               "other leading companies."))
    b.append(p("Indices such as the Dow Fire and Explosion Hazard Index and "
               "the Mond Index have been suggested to measure the degree of "
               "inherent SHE of a process. Rushton et al. (1994) pointed out "
               "that these indices can be used for the assessment of existing "
               "plants or at the detailed design stages: they require detailed "
               "plant specifications such as the plot plan, equipment sizes, "
               "material inventories and flows. Checklists, interaction "
               "matrices, Hazop and other hazard identification tools are also "
               "usable for the evaluation, because all hazards must be "
               "identified and their potential consequences understood. Hazop, "
               "for example, can be used at different stages of process design "
               "but in a restricted mode: a complete Hazop study requires "
               "final process plans with flow sheets and P&amp;IDs."))
    b.append(p("The P.I.I.S. developed by Edwards and Lawrence (1993) is "
               "intended for estimating the inherent safety of <b>reaction "
               "hazards at the conceptual design stage</b> — analysing the "
               "choice of process route, i.e. the raw materials and the "
               "sequence of the reaction steps (see Chapter 4)."))
    b.append(p("The INSIDE project (INSIDE, 1997) developed a toolkit called "
               "InSPIRE — a hyperbook providing chemists and engineers with "
               "the tools and methods to systematically identify, evaluate, "
               "optimise and select inherently SHE chemical processes and "
               "designs. Safety, health and environmental hazards are treated "
               "in an integrated way so that conflicts and synergies between "
               "these aspects are recognised and effectively managed. The "
               "toolkit especially addresses the key early stages of a "
               "project, where almost all of the main decisions that determine "
               "the SHE performance of the plant are taken. The InSPIRE "
               "hyperbook is no longer readily available, and at the end of "
               "the project many of the tools merited further development or "
               "validation."))
    b.append(note("The chapter's conclusion: there seem to be plenty of "
                  "evaluation methods for inherent safety, but <b>they are not "
                  "directly suitable safety analysis tools for use with novel "
                  "design systems in preliminary process design</b>. Most "
                  "existing methods need detailed process information and are "
                  "not directly applicable in the early design stages; on the "
                  "other hand, not all methods suit computerised use with "
                  "optimisation and simulation tools. This gap leads to the "
                  "Inherent Safety Index presented from Chapter 8 onwards."))
    return "".join(b)
