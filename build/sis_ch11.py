# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 11, Installing a System
(Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (fig, h2, h3, h4, lead, note, ol, p, quote, refs,
                          table, ul)

import sis11fig as F

PAGES_SRC = 13
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>FAT (factory acceptance test)</em> — thử chấp nhận tại xưởng chế tạo, trước khi hệ rời "
            "xưởng. · "
            "<em>SAT (site acceptance test)</em> — thử chấp nhận tại công trường, tức phần lớn nội dung "
            "của việc thẩm định. · "
            "<em>Thẩm định (validation)</em> — chứng minh hệ đã lắp đặt đáp ứng đầy đủ đặc tả yêu cầu an "
            "toàn; làm một lần, cho cả hệ. · "
            "<em>Kiểm chứng (verification)</em> — chứng minh từng pha của vòng đời đã hoàn thành đúng yêu "
            "cầu của chính pha ấy; làm ở mọi pha. · "
            "<em>FSA (functional safety assessment)</em> — điều tra dựa trên bằng chứng để phán xét mức an "
            "toàn chức năng đã đạt được. · "
            "<em>PSSR</em> — ở một số nước, tên gọi của lần FSA cuối cùng trước khởi động. · "
            "<em>Free issue</em> — vật tư do chủ đầu tư cấp cho nhà thầu, không nằm trong gói thầu. · "
            "<em>Force</em> — gán cưỡng bức giá trị vào/ra trong hệ khả trình, một dạng bypass không để lại "
            "dấu vết.")
    return note(
        "<b>Key terms.</b> <em>FAT (factory acceptance test)</em> — acceptance testing at the vendor's "
        "works, before the system ships. · <em>SAT (site acceptance test)</em> — acceptance testing on "
        "site, which is most of what validation consists of. · <em>Validation</em> — demonstrating that "
        "the installed system meets the safety requirements specification in all respects; once, for the "
        "whole system. · <em>Verification</em> — demonstrating that each phase of the lifecycle met the "
        "objectives set for that phase; at every phase. · <em>FSA (functional safety assessment)</em> — "
        "an evidence-based investigation judging the functional safety actually achieved. · <em>PSSR</em> "
        "— in some countries, the name given to the final assessment before startup. · <em>Free issue</em> "
        "— material supplied by the client rather than bought by the contractor. · <em>Force</em> — "
        "overwriting an I/O value in a programmable system, a bypass that leaves no visible trace.")


def body_vi():
    b = []
    b.append(lead(
        "Chương này mang tên “lắp đặt một hệ thống” nhưng thực ra nói về khoảng thời gian nguy hiểm nhất "
        "trong đời một hệ an toàn: từ lúc bản vẽ đóng lại đến lúc nhà máy chạy thật. Đó là lúc mọi sai sót "
        "tích tụ của những tháng trước có cơ hội bộc lộ cùng một lúc, và cũng là lúc sửa chúng đắt nhất."))

    # ------------------------------------------------------------------ 11.1
    b.append(h2("11.1 Giới thiệu", "Introduction"))
    b.append(p("Tuy tên chương là “lắp đặt một hệ thống”, ý định của chương là bao quát những hoạt động "
               "then chốt, từ lúc hoàn tất thiết kế cho tới khi hệ thống vận hành trôi chảy. Những hoạt "
               "động ấy gồm:"))
    b.append(ul([
        "thử nghiệm chấp nhận tại xưởng (FAT)",
        "lắp đặt và các kiểm tra lắp đặt",
        "thẩm định / thử nghiệm chấp nhận tại công trường (SAT)",
        "đánh giá an toàn chức năng / rà soát an toàn trước khởi động (PSSR)",
        "đào tạo",
        "bàn giao cho vận hành",
        "khởi động",
        "các hoạt động sau khởi động",
    ]))
    b.append(p("Mục tiêu tổng thể là bảo đảm hệ an toàn được lắp đặt đúng theo yêu cầu thiết kế, hoạt "
               "động đúng theo đặc tả yêu cầu an toàn, và nhân sự được đào tạo đầy đủ để vận hành và hỗ "
               "trợ hệ thống. Muốn đạt được điều đó một cách hiệu quả thì phải làm đủ những hoạt động kể "
               "trên."))
    b.append(p("Cơ quan An toàn và Sức khoẻ Anh [Tài liệu 1] đã xem xét hơn 30 vụ tai nạn và thấy rằng "
               "6 % số vụ là do các vấn đề “lắp đặt và chạy thử”. Con số tương đối thấp ấy có thể gây hiểu "
               "nhầm, bởi khả năng xảy ra vấn đề lớn là rất cao nếu hệ an toàn không được lắp đúng thiết "
               "kế và không được chạy thử theo đặc tả yêu cầu an toàn. Một số vấn đề tiềm ẩn:"))
    b.append(ul([
        "Lỗi lắp đặt, chẳng hạn đấu dây sai hoặc đấu không đúng, hay lắp nhầm thiết bị cho một dịch vụ "
        "cụ thể.",
        "Thử nghiệm không đủ để phát hiện lỗi lắp đặt và/hoặc lỗi thiết kế. Điều này thường xảy ra khi "
        "việc thử không được hoạch định tốt, người thử không được đào tạo thoả đáng, hoặc quy trình và "
        "tài liệu thử quá kém.",
        "Nhà thầu lắp đặt dùng vật tư “free issue” không đạt chất lượng. Các thiết bị chính thường được "
        "đặc tả tốt. Những hạng mục nhỏ như cầu đấu hay đầu nối cũng cần đạt chất lượng chấp nhận được "
        "để tránh rắc rối về sau.",
        "Thay đổi không được phê duyệt hoặc không có căn cứ, thực hiện trong quá trình xây lắp, thử "
        "nghiệm hoặc khởi động. Việc tạo ra những thay đổi “tạm thời” để hệ chạy được là điều hấp dẫn và "
        "thường dễ làm. Mọi thay đổi đều phải theo quy trình quản lý thay đổi (xem Chương 13).",
        "Tài liệu không được cập nhật theo tình trạng hoàn công. Điều này thường gây rắc rối khi cần bảo "
        "trì hệ thống.",
        "Đào tạo vận hành và hỗ trợ không đầy đủ. Ban lãnh đạo phải cam kết bảo đảm mọi nhân sự liên quan "
        "đến hệ an toàn đều được đào tạo thoả đáng.",
        "Bypass hoặc force tạm thời không được tháo ra sau khi thử nghiệm hay khởi động. Rất dễ bypass "
        "hoặc force đầu vào/đầu ra (I/O) của hệ khả trình. Những cầu nối trên cầu đấu có thể nằm đó rất "
        "lâu mà không ai để ý. Việc này phải được quản lý bằng kiểm soát ra vào và bằng quy trình.",
    ]))
    b.append(fig(1, F.fig_11_1(), "vi"))

    # ------------------------------------------------------------------ 11.2
    b.append(h2("11.2 Thuật ngữ", "Terminology"))
    b.append(p("Các tiêu chuẩn gần đây đưa vào một số thuật ngữ mà không phải ai cũng quen. Mấy thuật ngữ "
               "đáng làm rõ là:"))
    b.append(ul(["thẩm định (validation)", "kiểm chứng (verification)",
                 "đánh giá an toàn chức năng", "rà soát an toàn trước khởi động (PSSR)"]))

    b.append(p("<b>Thẩm định.</b> ANSI/ISA-84.00.01-2004, Phần 1–3 (IEC 61511-1 đến 3, bản sửa đổi) mô tả "
               "hoạt động này là việc"))
    b.append(quote("chứng minh rằng (các) chức năng an toàn và (các) hệ thống an toàn được xét, sau khi "
                   "đã lắp đặt, đáp ứng về mọi phương diện bản đặc tả yêu cầu an toàn.",
                   "ANSI/ISA-84.00.01-2004, Phần 1–3"))
    b.append(p("Bước này thường được thực hiện sau khi hệ đã lắp đặt xong. Đôi khi nó được gọi là thử "
               "nghiệm chấp nhận tại công trường (SAT)."))
    b.append(p("<b>Kiểm chứng.</b> Thuật ngữ này <em>không</em> đồng nghĩa với thẩm định. Kiểm chứng được "
               "định nghĩa là “những hoạt động chứng minh, cho từng pha của vòng đời an toàn liên quan, "
               "bằng phân tích và/hoặc bằng thử nghiệm, rằng với những đầu vào xác định thì đầu ra đáp "
               "ứng về mọi phương diện các mục tiêu và yêu cầu đặt ra cho pha ấy”. Vì thế kiểm chứng bảo "
               "đảm rằng mỗi pha của vòng đời an toàn đã được hoàn thành một cách thoả đáng. Thẩm định do "
               "đó có thể là một phần trong toàn bộ hoạt động kiểm chứng."))
    b.append(p("<b>Đánh giá an toàn chức năng.</b> Được định nghĩa là “việc điều tra, dựa trên bằng "
               "chứng, để phán xét mức an toàn chức năng đạt được bởi một hay nhiều lớp bảo vệ”. Việc này "
               "có thể làm ở nhiều thời điểm khác nhau trong vòng đời, nhưng phải có ít nhất một lần đánh "
               "giá sau khi lắp đặt, chạy thử và thẩm định."))
    b.append(p("<b>Rà soát an toàn trước khởi động (PSSR).</b> Ở một số nước, lần đánh giá an toàn chức "
               "năng cuối cùng (tức sau khi lắp đặt, chạy thử và thẩm định) được gọi là rà soát an toàn "
               "trước khởi động (PSSR)."))
    b.append(fig(2, F.fig_11_2(), "vi"))

    # ------------------------------------------------------------------ 11.3
    b.append(h2("11.3 Thử nghiệm chấp nhận tại xưởng (FAT)", "Factory Acceptance Testing (FAT)"))
    b.append(p("Tiểu mục 13.1.1 của ANSI/ISA-84.00.01-2004, Phần 1–3 (IEC 61511-1 đến 3, bản sửa đổi) "
               "định nghĩa mục tiêu của thử nghiệm chấp nhận tại xưởng là “thử bộ giải logic cùng phần mềm "
               "đi kèm với nhau để bảo đảm chúng đáp ứng các yêu cầu đã đặt ra trong đặc tả yêu cầu an "
               "toàn. Bằng việc thử bộ giải logic và phần mềm đi kèm trước khi lắp vào nhà máy, các lỗi có "
               "thể được phát hiện và sửa chữa dễ dàng”. Tiêu chuẩn cũng đưa ra các khuyến nghị cho FAT."))
    b.append(p("Thử nghiệm chấp nhận tại xưởng thường liên quan đến hệ logic và (các) giao diện vận hành, "
               "bất kể công nghệ logic được dùng là gì. Dù hệ logic chỉ gồm 20 rơ-le hay là một hệ điện tử "
               "khả trình phức tạp với hàng trăm điểm I/O, phần cứng và phần mềm của hệ vẫn phải được thử "
               "kỹ trước khi giao cho người dùng."))
    b.append(p("Phần dưới đây phác ra lợi ích, thành phần tham gia, những gì cần đưa vào FAT, và cách thực "
               "hiện việc thử. Chi tiết bổ sung về FAT có thể tìm trong các tài liệu tham khảo ở cuối "
               "chương."))
    b.append(h3("Lợi ích", "Benefits"))
    b.append(ul([
        "Phần cứng và phần mềm của hệ có thể được xem xét và thử trong một môi trường được kiểm soát, ít "
        "áp lực, cách xa công trường.",
        "Mọi vấn đề gặp phải đều dễ giải quyết và sửa chữa hơn nhờ nguồn lực sẵn có tại cơ sở của nhà "
        "cung cấp.",
        "FAT là một khoá đào tạo rất tốt cho nhân sự hỗ trợ.",
        "Hiểu biết của nhân sự tăng lên, và họ có cơ hội làm rõ cũng như sửa lại những chỗ hiểu nhầm.",
        "Tinh thần làm việc nhóm giữa nhà cung cấp, nhóm thiết kế và nhóm hỗ trợ được củng cố.",
    ]))
    b.append(h3("Thành phần tham gia", "Participants"))
    b.append(p("Số người tham gia phụ thuộc vào độ phức tạp và quy mô của hệ. Trách nhiệm của từng người "
               "phải được định nghĩa và hiểu rõ. Tối thiểu phải có:"))
    b.append(ul([
        "đại diện của nhà cung cấp;",
        "đại diện thiết kế của người dùng — thường là người chịu trách nhiệm tổng thể về thiết kế SIS. "
        "Người này nên giữ vai trò chủ trì FAT, chịu trách nhiệm điều phối FAT cũng như soạn các quy "
        "trình thử;",
        "nhân sự hỗ trợ của người dùng cuối.",
    ]))
    b.append(h3("Những gì được thử", "What Is Tested"))
    b.append(ul([
        "toàn bộ phần cứng của hệ logic, gồm các mô-đun I/O, cầu đấu, cáp nội bộ, bộ xử lý, mô-đun truyền "
        "thông và (các) giao diện vận hành;",
        "chuyển mạch tự động và dự phòng (nếu có);",
        "phần mềm (cả phần vận hành lẫn phần ứng dụng).",
    ]))
    b.append(h3("Cách thử", "How the System Is Tested"))
    b.append(p("Việc thử phải dựa trên những quy trình được ghi chép đầy đủ và được cả nhà cung cấp lẫn "
               "người dùng phê duyệt. Việc thử bao gồm, nhưng không giới hạn ở:"))
    b.append(ul([
        "kiểm tra bằng mắt;",
        "bơm tín hiệu vào (ví dụ tín hiệu số, xung, 4–20 mA, cặp nhiệt) và quan sát phản ứng của hệ;",
        "kích hoạt đầu ra (số và/hoặc tương tự);",
        "tạo ra nhiều tình huống hỏng khác nhau để thử các hệ dự phòng;",
        "thử phần logic không tương tác (tức phần logic không cần hồi tiếp từ thiết bị trường để hoạt "
        "động).",
    ]))
    b.append(p("Toàn bộ hệ logic, kể cả các mô-đun I/O, có thể được đấu tới công tắc, chiết áp 4–20 mA và "
               "đèn báo, mỗi thứ được dán nhãn như một thiết bị trường. Tổ thử mô phỏng hoạt động của đầu "
               "vào trường bằng cách bấm các công tắc số và quay các chiết áp tương tự. Bằng việc ghi nhận "
               "trạng thái của các đèn báo đầu ra, họ quan sát được trạng thái của từng đầu ra và so với "
               "các sơ đồ logic (ví dụ sơ đồ nhân quả) để kiểm chứng hoạt động của hệ. Cách thử như vậy "
               "cũng sẽ bộc lộ mọi vấn đề phần cứng. Nhiều dạng thử tương tự có thể được tự động hoá bằng "
               "một PC nối hoặc với riêng bộ điều khiển SIS, hoặc gồm cả cầu đấu trường và mô-đun I/O. PC "
               "có thể chạy hết các thủ tục thử nhanh hơn cách làm thủ công và còn tự động ghi lại kết quả."))
    b.append(fig(3, F.fig_11_3(), "vi"))
    b.append(p("Một số người dùng cho biết họ đã chuyển được trách nhiệm FAT sang cho nhà cung cấp/nhà "
               "tích hợp, và tiết kiệm được chi phí nhờ vậy."))

    # ------------------------------------------------------------------ 11.4
    b.append(h2("11.4 Lắp đặt", "Installation"))
    b.append(p("Các vấn đề lắp đặt bao gồm cảm biến, cơ cấu chấp hành cuối, cáp trường, hộp nối, tủ, hệ "
               "logic, (các) giao diện vận hành, chuông báo và toàn bộ phần cứng khác gắn với SIS."))
    b.append(p("<b>Yêu cầu lắp đặt chung:</b>"))
    b.append(ul([
        "Việc lắp đặt SIS thường là một phần của công việc lắp đặt thiết bị đo và điện nói chung, và có "
        "thể do cùng một nhà thầu và cùng một lực lượng lao động thực hiện. Nên xem xét tách riêng phạm "
        "vi công việc SIS khỏi phần việc thiết bị đo và điện còn lại. Việc này giảm thiểu khả năng gặp "
        "vấn đề nguyên nhân chung do lắp đặt, đồng thời nhấn mạnh tính trọng yếu và những yêu cầu đặc "
        "biệt của SIS (ví dụ thử nghiệm, đào tạo, v.v.).",
        "Bảo đảm hồ sơ thiết kế giao cho nhà thầu là đầy đủ và chính xác. Việc đào tạo và kinh nghiệm của "
        "nhà thầu là quan trọng.",
        "Mọi thiết bị phải được lắp theo khuyến nghị của nhà sản xuất.",
        "Mọi thiết bị và công trình lắp đặt phải tuân thủ tất cả quy chuẩn và yêu cầu pháp định đang có "
        "hiệu lực tại địa điểm. Nhà thầu phải hiểu những yêu cầu này và bảo đảm tuân thủ.",
        "Mọi vật tư “free issue” do nhà thầu cung cấp phải có chất lượng phù hợp với dịch vụ dự kiến. "
        "Những hạng mục này không phải lúc nào cũng có đặc tả chi tiết.",
        "Mọi thiết bị phải được lắp theo cách cho phép tiếp cận dễ dàng để bảo trì và thử nghiệm.",
        "Nhà thầu lắp đặt không được thay đổi việc hiệu chuẩn hay cài đặt của thiết bị trường.",
        "Phải cẩn thận bảo vệ mọi thiết bị trường khỏi hư hại cơ học và/hoặc môi trường trước khi lắp.",
        "Nhà thầu không được thay đổi hay lệch khỏi bản vẽ thiết kế nếu không có phê duyệt bằng văn bản. "
        "Phải theo đúng quy trình quản lý thay đổi (xem Chương 13). Các thay đổi phải được ghi lại trên "
        "một bộ bản vẽ hoàn công.",
    ]))

    b.append(h3("11.4.1 Kiểm tra lắp đặt", "Installation Checks"))
    b.append(p("Kiểm tra lắp đặt bảo đảm SIS được lắp đúng theo thiết kế chi tiết và sẵn sàng cho việc "
               "thẩm định. Những hoạt động này xác nhận rằng thiết bị và hệ thống dây đã được lắp đúng và "
               "các thiết bị trường hoạt động được. Cách tốt nhất để hoàn thành kiểm tra lắp đặt là tách "
               "công việc thành hai giai đoạn riêng biệt."))
    b.append(ol([
        "<b>Kiểm tra thiết bị trường và hệ thống dây.</b> Đây là việc kiểm tra cách thiết bị trường được "
        "lắp đặt về mặt vật lý, hệ thống dây, tính liên tục của dây, cầu đấu, ghi nhãn, hộp nối, v.v. Nhà "
        "thầu lắp đặt thường hoàn thành giai đoạn này khi hệ chưa được cấp điện.",
        "<b>Kiểm tra chức năng thiết bị.</b> Việc kiểm tra chức năng của thiết bị trường và hệ logic sau "
        "khi SIS đã được cấp điện. Nhà thầu lắp đặt hoặc một tổ độc lập có thể hoàn thành giai đoạn này.",
    ]))
    b.append(p("Những kiểm tra này nhằm xác nhận rằng:"))
    b.append(ul([
        "các nguồn năng lượng hoạt động được;",
        "mọi thiết bị đo đã được hiệu chuẩn đúng;",
        "các thiết bị trường hoạt động được;",
        "bộ giải logic hoạt động được.",
    ]))
    b.append(p("Một số ấn phẩm của IEC [Tài liệu 4 và 5] có sẵn các quy trình và biểu mẫu để thực hiện "
               "những kiểm tra trên. Những quy trình và biểu mẫu này giúp bảo đảm thiết bị được lắp đúng, "
               "mọi thiết bị đều được kiểm tra đúng, và hồ sơ được lưu giữ đầy đủ."))

    # ------------------------------------------------------------------ 11.5
    b.append(h2("11.5 Thẩm định / thử nghiệm chấp nhận tại công trường (SAT)",
                "Validation / Site Acceptance Tests (SAT)"))
    b.append(p("Thẩm định thường được gọi là thử nghiệm chấp nhận tại công trường (SAT). Những kiểm tra "
               "này chỉ nên được làm sau khi đã hoàn thành các kiểm tra lắp đặt. Mục tiêu chính của thẩm "
               "định là xác nhận hệ đáp ứng những yêu cầu ban đầu đã đặt ra, kể cả tính đúng đắn của phần "
               "logic của hệ. Cũng cần bảo đảm rằng:"))
    b.append(ul([
        "mọi thiết bị đã được đưa vào sử dụng theo sổ tay an toàn của nhà cung cấp;",
        "kế hoạch thử đã đầy đủ, kèm quy trình thử và quy trình ghi lại kết quả;",
        "mọi tài liệu của vòng đời an toàn đã đầy đủ.",
    ]))
    b.append(p("Việc thẩm định phải được hoàn thành một cách thoả đáng <em>trước khi</em> đưa những mối "
               "nguy mà SIS được thiết kế để ngăn ngừa hay giảm nhẹ vào hiện trường. Việc thẩm định phải "
               "bao gồm, nhưng không giới hạn ở những điểm sau:"))
    b.append(ul([
        "Hệ hoạt động được trong cả chế độ vận hành bình thường lẫn bất thường (ví dụ khởi động, dừng, "
        "bảo trì, v.v.).",
        "SIS trao đổi được (khi có yêu cầu) với hệ điều khiển quá trình cơ bản hoặc với bất kỳ hệ thống "
        "hay mạng nào khác.",
        "Cảm biến, phần logic, các phép tính và cơ cấu chấp hành cuối hoạt động đúng theo đặc tả yêu cầu "
        "an toàn.",
        "Cảm biến tác động tại đúng các giá trị đặt đã định trong đặc tả yêu cầu an toàn.",
        "Xác nhận rằng các chức năng hoạt động đúng như đặc tả khi biến quá trình không hợp lệ (ví dụ "
        "ngoài dải đo).",
        "Các trình tự dừng đúng được kích hoạt.",
        "SIS đưa ra đúng các thông báo và màn hình vận hành.",
        "Các phép tính là chính xác.",
        "Chức năng reset toàn phần và reset từng phần hoạt động đúng như thiết kế.",
        "Chức năng bypass và reset bypass hoạt động đúng như thiết kế.",
        "Chức năng dừng bằng tay hoạt động đúng như thiết kế.",
        "Chức năng báo động chẩn đoán hoạt động đúng như yêu cầu.",
        "Chu kỳ thử được ghi trong quy trình bảo trì, phù hợp với các yêu cầu về SIL.",
        "Tài liệu của SIS khớp với tình trạng lắp đặt thực tế và với quy trình vận hành.",
    ]))

    b.append(h3("11.5.1 Tài liệu cần thiết", "Necessary Documentation"))
    b.append(p("Tài liệu cần để hỗ trợ việc thẩm định phụ thuộc vào độ phức tạp của hệ và vào những gì "
               "nhóm thiết kế đã chuẩn bị ban đầu. Vì ở đây thử cả hệ, nên không một bản vẽ đơn lẻ nào là "
               "đủ. Điều thiết yếu là phải soạn và tuân thủ những quy trình chi tiết. Thường cần những tài "
               "liệu sau để hỗ trợ việc thẩm định:"))
    b.append(ul([
        "các quy trình kiểm tra phục vụ thẩm định;",
        "một bản đặc tả yêu cầu an toàn;",
        "bản liệt kê / bản in chương trình của PES;",
        "sơ đồ khối của toàn hệ;",
        "danh sách đầu vào và đầu ra kèm địa chỉ vật lý;",
        "các sơ đồ đường ống và thiết bị đo (P&amp;ID);",
        "danh mục thiết bị đo;",
        "phiếu đặc tả cho mọi thiết bị chính, gồm nhà sản xuất, kiểu máy và các tuỳ chọn;",
        "sơ đồ vòng đo;",
        "sơ đồ điện;",
        "cấu hình BPCS cho mọi đầu vào/đầu ra thuộc SIS;",
        "sơ đồ logic (ví dụ sơ đồ nhân quả hoặc sơ đồ Boolean);",
        "bản vẽ chỉ vị trí của mọi thiết bị chính;",
        "sơ đồ đấu nối hộp nối và tủ;",
        "bản vẽ chỉ sự đấu nối và điểm kết thúc của mọi dây;",
        "sơ đồ đường ống của hệ khí nén;",
        "tài liệu của nhà cung cấp thiết bị, bao gồm (nhưng không giới hạn ở) đặc tả, yêu cầu lắp đặt và "
        "sổ tay vận hành.",
    ]))

    # ------------------------------------------------------------------ 11.6
    b.append(h2("11.6 Đánh giá an toàn chức năng / rà soát an toàn trước khởi động (PSSR)",
                "Functional Safety Assessment / Pre-startup Safety Review (PSSR)"))
    b.append(p("Tiểu mục 5.2.6.1.1 của ANSI/ISA-84.00.01-2004, Phần 1–3 (IEC 61511-1 đến 3, bản sửa đổi) "
               "quy định:"))
    b.append(quote("Phải định nghĩa và thực hiện một quy trình đánh giá an toàn chức năng theo cách cho "
                   "phép đưa ra phán xét về mức an toàn chức năng và mức toàn vẹn an toàn mà hệ thống an "
                   "toàn đã đạt được. Quy trình phải yêu cầu chỉ định một nhóm đánh giá, bao gồm chuyên môn "
                   "kỹ thuật, chuyên môn ứng dụng và chuyên môn vận hành cần thiết cho công trình lắp đặt "
                   "cụ thể đó.",
                   "ANSI/ISA-84.00.01-2004, Phần 1–3, tiểu mục 5.2.6.1.1"))
    b.append(p("Tối thiểu phải hoàn thành ít nhất một lần đánh giá trước khi có mối nguy hiện diện. Thành "
               "phần nhóm đánh giá phải bao gồm ít nhất một người có năng lực cao cấp <em>không</em> tham "
               "gia nhóm thiết kế dự án. Một số yêu cầu then chốt mà tiêu chuẩn nêu ra là:"))
    b.append(ul([
        "việc đánh giá mối nguy và rủi ro đã được thực hiện;",
        "những khuyến nghị từ việc đánh giá mối nguy và rủi ro có liên quan đến hệ thống an toàn đã được "
        "thực hiện hoặc đã được giải quyết;",
        "các quy trình thay đổi thiết kế dự án đã có và đã được thực hiện đúng;",
        "những khuyến nghị từ lần đánh giá an toàn chức năng trước đó đã được giải quyết;",
        "hệ thống an toàn đã được thiết kế, chế tạo và lắp đặt theo đặc tả yêu cầu an toàn, và mọi sai "
        "khác đã được nhận diện và giải quyết;",
        "các quy trình an toàn, vận hành, bảo trì và ứng cứu liên quan đến hệ thống an toàn đã có;",
        "kế hoạch thẩm định hệ thống an toàn là phù hợp và các hoạt động thẩm định đã hoàn thành;",
        "việc đào tạo nhân viên đã hoàn thành và những thông tin cần thiết về hệ thống an toàn đã được "
        "cung cấp cho nhân sự bảo trì và vận hành;",
        "các kế hoạch hay chiến lược để thực hiện những lần đánh giá an toàn chức năng tiếp theo đã có.",
    ]))

    # ------------------------------------------------------------------ 11.7
    b.append(h2("11.7 Đào tạo", "Training"))
    b.append(p("Tính trọng yếu của hệ an toàn phải được nhận thức đầy đủ. Nhân sự cần được đào tạo thì hệ "
               "mới vận hành đúng được. Việc đào tạo cho hệ an toàn nên bắt đầu từ lúc soạn đặc tả yêu cầu "
               "an toàn và kéo dài suốt đời sống nhà máy. Những người then chốt cần được đào tạo gồm nhân "
               "sự vận hành và nhân sự hỗ trợ. Nội dung đào tạo nên gồm:"))
    b.append(ul([
        "hiểu đặc tả yêu cầu an toàn;",
        "cấu hình và lập trình PES cùng các thiết bị điện tử khác;",
        "vị trí thiết bị SIS trong phòng điều khiển và ngoài hiện trường;",
        "tài liệu SIS và nơi lưu giữ;",
        "những quy trình bảo trì đặc biệt phải tuân theo;",
        "quy trình thử trực tuyến;",
        "cách xử lý khi tình trạng vận hành bị rối loạn;",
        "cách xử lý khi có tình huống dừng khẩn cấp;",
        "thẩm quyền cần có trước khi bypass một SIS;",
        "hiểu SIS hoạt động thế nào (ví dụ các giá trị đặt, những van sẽ đóng, v.v.);",
        "hiểu phải làm gì khi một báo động chẩn đoán nổi lên;",
        "đào tạo cho nhân sự bảo trì, trong đó có việc xác định ai đủ năng lực làm việc trên hệ thống.",
    ]))
    b.append(p("Những cơ hội và cách thức để đào tạo hiệu quả là:"))
    b.append(ul([
        "quá trình soạn đặc tả yêu cầu an toàn;",
        "thử nghiệm chấp nhận tại xưởng;",
        "chạy mô phỏng / giả lập logic;",
        "đào tạo trên lớp;",
        "sổ tay và hệ thống đào tạo tại chỗ;",
        "thẩm định;",
        "khởi động;",
        "đào tạo ôn tập định kỳ.",
    ]))
    b.append(p("Nhân sự của nhà cung cấp sẽ được gọi đến để hỗ trợ cuối cùng. Hãy tìm hiểu họ là ai, liên "
               "hệ thế nào, và liệu họ có hiểu hệ thống của bạn và có đủ năng lực cung cấp mức hỗ trợ cần "
               "thiết hay không."))
    b.append(p("OSHA 29 CFR 1910.119 (Quản lý an toàn quá trình đối với hoá chất có mức nguy hiểm cao) "
               "cũng định nghĩa các yêu cầu về đào tạo liên quan đến hệ an toàn. Nên xem lại những yêu cầu "
               "của quy định đó."))

    # ------------------------------------------------------------------ 11.8
    b.append(h2("11.8 Bàn giao cho vận hành", "Handover to Operations"))
    b.append(p("Hoàn thành thoả đáng việc thẩm định phải là căn cứ để bàn giao hệ thống cho vận hành. "
               "Từng chức năng an toàn phải được ký nghiệm thu để xác nhận rằng mọi thử nghiệm đã hoàn "
               "thành tốt đẹp. Bộ phận vận hành phải thấy thoả mãn rằng họ đã được đào tạo về cách vận "
               "hành hệ thống. Nếu còn bất kỳ vấn đề tồn đọng nào, chúng phải được phản ánh trong tài liệu, "
               "kèm chỉ rõ:"))
    b.append(ul([
        "khiếm khuyết đó sẽ ảnh hưởng thế nào đến việc vận hành SIS;",
        "khi nào nó sẽ được giải quyết;",
        "ai chịu trách nhiệm giải quyết.",
    ]))
    b.append(p("Nếu nhóm đánh giá cho rằng bất kỳ khiếm khuyết tồn đọng nào có khả năng tạo ra một sự kiện "
               "nguy hiểm, thì việc khởi động phải được hoãn lại hoặc thu hẹp phạm vi cho tới khi các vấn "
               "đề ấy được giải quyết."))

    # ------------------------------------------------------------------ 11.9
    b.append(h2("11.9 Khởi động", "Startup"))
    b.append(p("Hệ an toàn có khả năng tác động nhiều hơn trong lần khởi động đầu tiên của nhà máy so với "
               "bất kỳ thời điểm nào khác. Với một số nhà máy, khởi động lần đầu là một trong những giai "
               "đoạn vận hành nguy hiểm nhất, vì những lý do sau:"))
    b.append(ul([
        "Dù nhà máy mới có giống hệt một nhà máy đang chạy hay không, vẫn luôn có những khía cạnh riêng. "
        "Chỉ sau một thời gian vận hành và tích luỹ kinh nghiệm thì hoạt động thực tế mới được hiểu đầy "
        "đủ.",
        "Trong giai đoạn này, bộ phận vận hành thường yêu cầu bypass hoặc sửa các giá trị đặt cắt. Điều "
        "đó là dễ hiểu, nhưng thiết yếu là các quy trình thay đổi phải được ban hành và thực thi nghiêm "
        "ngặt. Sự cần thiết và tác động của thay đổi phải được phân tích kỹ (xem Chương 13). Đã có những "
        "trường hợp bypass còn nằm đó nhiều tháng sau khởi động. Một cách bypass phổ biến là force đầu ra "
        "từ PES. Nên dùng một dạng báo động nào đó để theo dõi mọi chức năng đang bị force.",
        "Bộ phận vận hành có thể chưa đủ kinh nghiệm xử lý các tình huống rối loạn, và tình trạng có thể "
        "leo thang thành một lần dừng máy.",
        "Một số hỏng hóc mang tính hệ thống (trong thiết kế và lắp đặt) có thể đang bắt đầu bộc lộ, dẫn "
        "đến dừng máy.",
        "Các thành phần của hệ có thể đang nằm trong giai đoạn tử vong sơ sinh. Suất hỏng cao nhất là "
        "trong giai đoạn này.",
        "Trong giai đoạn này có rất nhiều hoạt động, nên khả năng xảy ra sai sót của con người cũng cao "
        "hơn.",
    ]))

    # ------------------------------------------------------------------ 11.10
    b.append(h2("11.10 Các hoạt động sau khởi động", "Post Startup Activities"))
    b.append(p("Những hoạt động chính còn lại sau khởi động là tài liệu, đào tạo lần cuối và giải quyết "
               "các khiếm khuyết. Nên lập một lịch trình ghi rõ ai chịu trách nhiệm từng hoạt động cùng "
               "một dòng thời gian. Danh sách đầy đủ hơn về những việc còn lại sau khởi động gồm:"))
    b.append(ul([
        "soạn bản vẽ hoàn công;",
        "tài liệu và/hoặc quy trình bảo trì đặc biệt;",
        "danh sách khiếm khuyết;",
        "đào tạo nốt những nhân sự vận hành và hỗ trợ còn lại;",
        "thiết lập các chương trình thử trực tuyến cần thiết;",
        "thiết lập các chương trình bảo trì phòng ngừa cần thiết;",
        "xem xét định kỳ các dữ liệu chẩn đoán của hệ.",
    ]))

    # ------------------------------------------------------------------ Summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Chương này đã xem xét các hoạt động từ lúc hoàn tất thiết kế hệ thống cho tới khi vận hành "
               "trôi chảy. Những hoạt động then chốt gồm thử nghiệm chấp nhận tại xưởng (FAT), lắp đặt, "
               "thử nghiệm chấp nhận tại công trường (SAT), đánh giá an toàn chức năng / rà soát an toàn "
               "trước khởi động (PSSR), và khởi động. Mục tiêu tổng thể của những hoạt động này là bảo "
               "đảm hệ được lắp đặt và hoạt động đúng theo đặc tả yêu cầu an toàn, đồng thời bảo đảm nhân "
               "sự được đào tạo đầy đủ để vận hành và hỗ trợ hệ thống."))

    b.append(note(
        "<b>Ba điểm cần lưu ý khi đọc chương này.</b><br>"
        "<b>(1) Một chỉ dẫn tài liệu bị sai.</b> Mục 11.4.1 viết “Various IEC publications [Ref. 3 and 4]” "
        "cho các biểu mẫu kiểm tra vòng đo, nhưng Tài liệu 3 là <em>Guidelines for Safe Automation of "
        "Chemical Processes</em> của AIChE/CCPS — không phải ấn phẩm IEC. Hai văn bản IEC đúng ở đây là "
        "Tài liệu 4 (IEC/PAS 62381, về FAT/SAT/SIT) và Tài liệu 5 (IEC/PAS 62382, về kiểm tra vòng đo). "
        "Bản dịch dẫn [Tài liệu 4 và 5] theo đúng nghĩa.<br>"
        "<b>(2) “Free issue” bị dùng ngược ở hai chỗ.</b> Mục 11.1 nói tới “vật tư free issue do nhà thầu "
        "lắp đặt cung cấp”, còn mục 11.4 lại nói “vật tư free issue do nhà thầu cung cấp”. Nguyên nghĩa "
        "của thuật ngữ này trong hợp đồng xây lắp là vật tư do <em>chủ đầu tư</em> cấp cho nhà thầu, không "
        "nằm trong giá thầu. Bản dịch giữ nguyên cụm “free issue” kèm chú thích, thay vì tự chọn một "
        "nghĩa.<br>"
        "<b>(3) Số 6 % ở mục 11.1 không mâu thuẫn với số 44 % ở Chương 2 và Chương 10.</b> Hai con số trả "
        "lời hai câu hỏi khác nhau: 6 % là tỉ lệ <em>vụ tai nạn</em> do lắp đặt và chạy thử, còn 44 % là "
        "tỉ lệ <em>vấn đề của hệ thống</em> bắt nguồn từ đặc tả sai. Cùng một nguồn (HSE), khác mẫu và "
        "khác đơn vị đếm."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "<em>Out of Control: Why Control Systems Go Wrong and How to Prevent Failure</em>. U.K. Health &amp; "
        "Safety Executive, 1995.",
        "ANSI/ISA-84.00.01-2004, Phần 1–3 (IEC 61511-1 đến 3, bản sửa đổi). <em>Functional Safety: Safety "
        "Instrumented Systems for the Process Industry Sector</em>.",
        "<em>Guidelines for Safe Automation of Chemical Processes</em>. American Institute of Chemical "
        "Engineers – Center for Chemical Process Safety, 1993.",
        "IEC/PAS 62381 ed. 1.0 en:2004. <em>Activities during the factory acceptance test (FAT), site "
        "acceptance test (SAT), and site integration test (SIT) for automation systems in the process "
        "industry</em>.",
        "IEC/PAS 62382 ed. 1.0 en:2004. <em>Electrical and instrumentation loop check</em>.",
    ]))
    return "".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "The chapter is called installing a system, but what it really covers is the most dangerous "
        "fortnight in a safety system's life: the gap between the drawings closing and the plant running. "
        "Everything that went wrong quietly during design gets its chance to appear at once, at the moment "
        "when fixing it costs the most."))

    b.append(h2("Six per cent is not the number to take comfort from"))
    b.append(p("The Health and Safety Executive examined more than thirty accidents and attributed six per "
               "cent of them to installation and commissioning. It reads like a small number, and section "
               "11.1 immediately explains why it is not: the figure counts accidents that happened, not "
               "hazards that were created. A safety function that was wired to the wrong terminal and "
               "tested against the wrong cause-and-effect row is a protection layer that does not exist, "
               "and it will sit there looking healthy for years."))
    b.append(p("The list of failure modes in 11.1 is worth reading as a list of things that are all "
               "invisible at the moment they happen. A wrong termination is invisible. A substandard "
               "terminal strip is invisible until it corrodes. A jumper left on a terminal block is "
               "invisible until somebody needs the trip. An as-built drawing that was never updated is "
               "invisible until the first maintenance outage. None of these announce themselves; the "
               "system is quiet either way."))

    b.append(h2("Four gates, four different kinds of evidence"))
    b.append(p("Figure 11-1 is the spine of the chapter, and its argument is that the four gates are not "
               "interchangeable. FAT proves that the logic solver and its software left the works matching "
               "the specification — it says nothing about field wiring, because at that point there is no "
               "field. Installation checks prove that the wiring, tagging and calibration match the "
               "drawings, and they are deliberately done before power is applied, so they cannot prove the "
               "logic runs. SAT proves the installed system meets the safety requirements specification, "
               "and it is the first test that uses the real sensors and the real valves. FSA/PSSR is not a "
               "test at all; it is an independent judgement about evidence somebody else gathered."))
    b.append(p("The order matters as much as the content. Each gate is cheap to pass and expensive to "
               "fail, and each one narrows what is left to discover. If you skip FAT because the schedule "
               "is tight, you do not save the FAT; you move it to the site, where the same defect costs "
               "more, takes longer, and is found by people who did not write the code."))

    b.append(h2("Verification is not validation, and the standard is right to insist"))
    b.append(p("Section 11.2 spends a page on four words that are routinely used as synonyms and are not. "
               "Verification is per phase: did this phase meet the objectives set for this phase. "
               "Validation is per system, once, after installation: does the whole thing meet the safety "
               "requirements specification. Figure 11-2 draws the relationship — validation is a subset of "
               "verification, not a peer of it. The confusion has a cost: teams that treat SAT as "
               "\"validation done\" skip the phase-by-phase checks, and then discover during SAT that the "
               "cause-and-effect diagram they are testing against was never verified against the hazard "
               "study."))
    b.append(p("The FSA is a third thing again, and the standard's requirement that at least one assessor "
               "come from outside the design team is the whole point. An assessment conducted by the people "
               "who made the decisions is a review, and reviews of one's own work reliably find nothing. "
               "The PSSR, where that name is used, is simply the last of these assessments, moved to the "
               "moment just before the hazard is introduced."))

    b.append(h2("The FAT bench is a model of the plant, and models lie in specific ways"))
    b.append(p("Figure 11-3 shows the classic bench: switches for discrete inputs, potentiometers for 4–20 "
               "mA, thermocouple simulators, lamps for outputs, each labelled as the field device it stands "
               "in for. It is genuinely good value — it finds logic errors, addressing errors, scaling "
               "errors and configuration errors before anyone books a flight."))
    b.append(p("What it cannot find is everything that lives between the terminal and the process. Cable "
               "capacitance and induced noise. A shield grounded at both ends. A 24 V supply that sags when "
               "forty solenoids pick up together. A valve that takes eleven seconds to stroke when the "
               "cause-and-effect diagram assumes three. An instrument that reads correctly in a workshop at "
               "21 °C and drifts at 60 °C. The bench tests the logic solver; only the site tests the loop."))
    b.append(p("The automated version, with a PC running the script and writing the record, is better than "
               "the manual version for a reason that has nothing to do with speed: it produces evidence. A "
               "manual FAT produces a technician's memory of a long day. If the FAT is going to be used as "
               "proof in an assessment, the proof has to exist on paper."))

    b.append(h2("Free issue is where quality goes to die"))
    b.append(p("Section 11.1 and 11.4 both worry about free issue material, and the worry is well placed. "
               "The logic solver, the transmitters and the valves are specified to three decimal places and "
               "audited by everyone. The terminal strips, the ferrules, the cable glands and the jumpers "
               "are bought by whoever is buying, to whatever standard is cheapest, because nobody wrote a "
               "specification for them."))
    b.append(p("These are exactly the components that decide whether the system works in year eight. A "
               "terminal that corrodes open is a dangerous undetected failure in a de-energised circuit. A "
               "ferrule that is crimped with the wrong tool is a resistance that drifts. The cost of "
               "specifying them properly is trivial against the cost of the outage that finds them."))

    b.append(h2("Bypasses outlive the startups that created them"))
    b.append(p("Both section 11.1 and section 11.9 raise the same problem from two directions: temporary "
               "bypasses and forces that were needed to get the plant running and were never removed. "
               "Section 11.9 adds the detail that makes it dangerous — forcing an output from the PES is "
               "the common method, because it needs no jumper wire, leaves no physical evidence, and in "
               "many systems survives a download."))
    b.append(p("The mitigations the chapter asks for are modest and mostly procedural: an alarm on any "
               "forced point, a register, a time limit, shift-by-shift renewal, and access control on who "
               "can force at all. None of them is technically difficult. All of them fail when the plant "
               "is struggling at three in the morning and the person who could remove the force has gone "
               "home."))

    b.append(h2("Startup is the only test that uses the real process"))
    b.append(p("Section 11.9 lists six reasons why first startup is the most hazardous phase, and they "
               "compound. The plant is not quite the plant on the drawings. Operations are learning. "
               "Systematic design and installation failures choose this moment to surface, because it is "
               "the first moment the system is asked to do everything at once. And the components are "
               "sitting in their infant mortality period, where the failure rate is highest and falling."))
    b.append(p("The bathtub curve from chapter 8 is not an abstraction here; it is a schedule. The first "
               "weeks of operation are when the hardware is most likely to fail and when the people are "
               "least able to cope, which is precisely why the chapter insists that validation be complete "
               "before the hazard is introduced, and why the assessment team is given the authority to "
               "defer the startup."))

    b.append(h2("The handover signature is a liability document"))
    b.append(p("Section 11.8 is short and easy to skim, but the requirement that each safety function be "
               "signed off individually is doing real work. A single signature for the whole system means "
               "one deficiency anywhere blocks everything, so in practice it gets signed anyway. A "
               "signature per function means the deficiencies are enumerated, owned and dated, and the "
               "system can go into service with a written, bounded list of what is not yet right."))
    b.append(p("That is the whole discipline of this chapter in one sentence: a safety system does not "
               "have to be perfect to start up, but it does have to be honest about what it is."))
    return "".join(b)
