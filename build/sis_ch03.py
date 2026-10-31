# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 3, Process Control vs. Safety Control
(Gruhn & Cheddie, ISA 2006)."""
import sisfig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 15
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>BPCS</em> — hệ điều khiển quá trình cơ bản, làm chức năng điều chỉnh thường ngày. · "
            "<em>SIS</em> — hệ thống đo lường an toàn, đưa quá trình về trạng thái an toàn. · "
            "<em>SIF</em> — một chức năng an toàn đo lường cụ thể trong SIS. · "
            "<em>Lỗi tự bộc lộ (revealed failure)</em> — lỗi làm hệ ngừng làm việc nên thấy được ngay. · "
            "<em>Lỗi ẩn (unrevealed failure)</em> — lỗi không gây biểu hiện gì cho tới khi cần dùng hệ. · "
            "<em>Nguyên nhân chung (common cause)</em> — một tác nhân duy nhất làm hỏng nhiều bộ phận. · "
            "<em>Hệ số beta</em> — tỉ lệ lỗi có thể ảnh hưởng đồng thời các nhánh dự phòng. · "
            "<em>Lỗi hệ thống (systematic failure)</em> — lỗi do thiết kế hay quy trình, lặp lại được.")
    return note(
        "<b>Key terms.</b> <em>BPCS</em> — the basic process control system, doing the everyday regulating. · "
        "<em>SIS</em> — the safety instrumented system, taking the process to a safe state. · "
        "<em>SIF</em> — one safety instrumented function inside a SIS. · "
        "<em>Revealed failure</em> — a failure that stops the system working, so it is seen at once. · "
        "<em>Unrevealed failure</em> — a failure with no symptom until the system is needed. · "
        "<em>Common cause</em> — one stressor taking out several items at once. · "
        "<em>Beta factor</em> — the share of failures that can hit redundant legs together. · "
        "<em>Systematic failure</em> — a design or process error that repeats under the same conditions.")


# ===================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Chương này là chương ngắn nhưng là chương đặt nền cho cả cuốn sách: nó trả lời câu hỏi vì sao hệ "
        "điều khiển và hệ an toàn phải là hai hệ khác nhau, chứ không phải hai phần mềm chạy trong cùng một "
        "bộ xử lý. Câu trả lời không nằm ở độ tin cậy của máy tính — mà ở chỗ hai hệ có hai kiểu lỗi khác "
        "nhau, hai kiểu người dùng khác nhau và hai kiểu thay đổi khác nhau."))

    # ---------------------------------------------------------------- 3.1
    b.append(h2("3.1 Định nghĩa điều khiển và an toàn", "Control and Safety Defined"))
    b.append(p("Các hệ tới hạn đòi hỏi phải được thử nghiệm và ghi chép đầy đủ. Còn hệ điều khiển quá trình "
               "thông thường có cần mức độ chặt chẽ ấy hay không thì vẫn còn tranh cãi. Năm 1992, khi chính "
               "phủ Hoa Kỳ ban hành quy định về quản lý an toàn quá trình (PSM, 29 CFR 1910.119), nhiều "
               "người đặt câu hỏi liệu các yêu cầu bắt buộc về ghi chép và thử nghiệm có áp dụng cho cả hệ "
               "điều khiển lẫn hệ an toàn hay không. Ví dụ, hầu hết các tổ chức đều có quy trình thử nghiệm "
               "được ghi chép cho hệ thống đo lường an toàn của mình, nhưng không thể nói như vậy với toàn "
               "bộ các vòng điều khiển. Người dùng trong ngành chế biến đã hỏi đại diện OSHA rằng các yêu "
               "cầu trong quy định PSM áp dụng cho cả 6.000 vòng trong DCS của họ, hay chỉ cho 300 vòng "
               "trong hệ đo lường an toàn. OSHA trả lời: tất cả."))
    b.append(p("Người dùng coi đó là nhát búa cuối cùng đóng nắp quan tài của ngành. Chính bất bình này đã "
               "thúc đẩy sự ra đời của tiêu chuẩn ANSI/ISA-91.01-1995, “Nhận dạng các hệ dừng khẩn cấp và "
               "các điều khiển tới hạn đối với việc duy trì an toàn trong ngành chế biến”. Tiêu chuẩn "
               "ANSI/ISA-91.00.01-2001 được khẳng định lại năm 2001. Văn bản ngắn này — chỉ hai trang — "
               "đưa ra định nghĩa cho ba khái niệm: điều khiển quá trình, điều khiển an toàn, và điều khiển "
               "tới hạn về an toàn."))
    b.append(table(
        ["Thuật ngữ", "Định nghĩa của ANSI/ISA-91.00.01-2001", "Tỉ lệ điển hình"],
        [["Hệ điều khiển quá trình cơ bản (BPCS)",
          "“Thiết bị điều khiển được lắp đặt để thực hiện các chức năng điều chỉnh thông thường của quá "
          "trình (ví dụ điều khiển PID và điều khiển trình tự).”",
          "tới 95 % thiết bị đo của một nhà máy trên bờ"],
         ["Hệ dừng khẩn cấp (ESD)",
          "“Thiết bị đo và điều khiển được lắp đặt nhằm đưa quá trình, hoặc một thiết bị cụ thể trong quá "
          "trình, về trạng thái an toàn. Không bao gồm thiết bị đo và điều khiển dùng cho việc dừng không "
          "khẩn cấp hoặc vận hành thường lệ.”",
          "dưới 10 % thiết bị đo"],
         ["Điều khiển tới hạn về an toàn",
          "“Một điều khiển mà việc không làm việc đúng sẽ trực tiếp dẫn tới việc phát tán thảm khốc chất "
          "độc, chất phản ứng, chất cháy hoặc chất nổ.”",
          "rất nhỏ, và phải là rất nhỏ"]],
        "Bảng 3-1 · Ba hạng mục của ANSI/ISA-91.00.01-2001. Chính ba định nghĩa này là cơ sở để người dùng "
        "lập luận rằng 6.000 vòng DCS của họ không liên quan tới an toàn, còn 300 vòng đo lường an toàn "
        "thì có."))
    b.append(p("Tiêu chuẩn định nghĩa BPCS — để phân biệt với một hệ điều khiển quá trình “cao cấp” — là "
               "“thiết bị điều khiển được lắp đặt để thực hiện các chức năng điều chỉnh thông thường của "
               "quá trình”. Có người cho rằng hạng mục này chiếm tới 95 % thiết bị đo của phần lớn nhà máy "
               "trên bờ, và phần lớn thực hiện điều đó bằng DCS, PLC hoặc hệ lai."))
    b.append(p("“Hệ dừng khẩn cấp” được định nghĩa là “thiết bị đo và điều khiển được lắp đặt nhằm đưa quá "
               "trình, hoặc một thiết bị cụ thể trong quá trình, về trạng thái an toàn”. Hạng mục này "
               "chiếm dưới 10 % thiết bị đo."))
    b.append(p("Tiêu chuẩn còn định nghĩa hạng mục thứ ba, “điều khiển tới hạn về an toàn”: “một điều khiển "
               "mà việc không làm việc đúng sẽ trực tiếp dẫn tới việc phát tán thảm khốc chất độc, chất "
               "phản ứng, chất cháy hoặc chất nổ”. Nói cách khác, đó là bất kỳ lớp điều khiển hay lớp an "
               "toàn nào mà nếu không có thêm lớp nào khác thì một lỗi sẽ ngay lập tức thành sự kiện nguy "
               "hiểm. May mắn là tỉ lệ các vòng như vậy rất nhỏ."))
    b.append(p("Dựa trên các định nghĩa này, người dùng trình bày với OSHA rằng 6.000 vòng DCS của họ không "
               "liên quan tới an toàn và do đó không cần mức độ chặt chẽ về ghi chép và thử nghiệm như 300 "
               "vòng đo lường an toàn."))
    b.append(note(
        "Điều này <b>không</b> có nghĩa là thiết kế hệ điều khiển phân tán không cần phân tích, ghi chép và "
        "kiểm soát quản lý đầy đủ. Rõ ràng là có — chỉ là không tới mức như hệ an toàn. Sự khác biệt không "
        "phải giữa “có” và “không”, mà giữa hai mức độ."))

    # ---------------------------------------------------------------- 3.2
    b.append(h2("3.2 Điều khiển quá trình — chủ động và động",
                "Process Control — Active/Dynamic"))
    b.append(p("Cần hiểu rõ khác biệt cơ bản giữa điều khiển quá trình và điều khiển an toàn. Hệ điều khiển "
               "quá trình là hệ <em>chủ động</em>, hay <em>động</em>. Chúng có đầu vào tương tự, đầu ra "
               "tương tự, thực hiện tính toán, và có vòng phản hồi. Vì vậy, phần lớn lỗi trong hệ điều "
               "khiển <b>tự bộc lộ</b>."))
    b.append(p("Lấy ví dụ một robot trên dây chuyền tự động. Bình thường robot gắp chi tiết A đặt vào vị trí "
               "B. Nếu hệ hỏng, ai cũng thấy ngay: nó không còn đặt chi tiết A vào vị trí B nữa. Không có "
               "thứ gọi là lỗi “ẩn” trong trường hợp này. Hệ hoặc làm việc, hoặc không. Chỉ có một kiểu "
               "lỗi — đã bộc lộ — và không cần chẩn đoán rộng mới phát hiện được."))
    b.append(p("Nếu một van điều khiển điều biến hỏng ở vị trí mở hoàn toàn hoặc đóng hoàn toàn, nó gần như "
               "chắc chắn ảnh hưởng tới sản xuất và vấn đề sẽ lộ ra rất nhanh. Nếu van kẹt ở trạng thái cuối "
               "cùng, các vấn đề kéo theo cũng sẽ tự lộ ra tương đối nhanh. Một lần nữa, thử nghiệm và chẩn "
               "đoán rộng thường không cần thiết để phát hiện những lỗi ấy."))

    b.append(h3("3.2.1 Nhu cầu — và sự dễ dàng — của việc thay đổi thường xuyên",
                "The Need For (and Ease of) Making Frequent Changes"))
    b.append(p("Hệ điều khiển quá trình phải đủ linh hoạt để cho phép thay đổi thường xuyên. Các tham số quá "
               "trình (điểm đặt, thông số PID, chế độ tay/tự động…) cần được thay đổi trong lúc vận hành "
               "bình thường. Từng phần của hệ cũng có thể bị đặt bypass và quá trình có thể được điều khiển "
               "bằng tay. Tất cả những điều đó là bình thường với hệ điều khiển. Truy cập đơn giản, dễ và "
               "nhanh là một yêu cầu, chứ không phải một tiện ích."))

    # ---------------------------------------------------------------- 3.3
    b.append(h2("3.3 Điều khiển an toàn — thụ động và ngủ",
                "Safety Control — Passive/Dormant"))
    b.append(p("Hệ an toàn thì ngược lại. Chúng <em>ngủ</em>, hay <em>thụ động</em>. Chúng làm việc trong "
               "những khoảng thời gian dài mà hầu như không làm gì, và hy vọng sẽ không bao giờ được gọi "
               "tới. Ví dụ là một van an toàn: bình thường van đóng, chỉ mở khi áp suất tới một giới hạn "
               "nào đó. Nếu áp suất không bao giờ vượt giá trị ấy, van không bao giờ hoạt động."))
    b.append(p("Nhiều lỗi trong các hệ này <b>không</b> tự bộc lộ. Nếu van an toàn bị tắc, không có dấu hiệu "
               "nào ngay lập tức. Một PLC có thể bị treo trong một vòng lặp vô hạn; nếu không có bộ định "
               "thời canh chừng (watchdog timer) thì hệ không nhận ra được vấn đề — và nếu hệ đang ngủ thì "
               "bạn cũng không. Một mô-đun đầu ra có thể dùng triac và hỏng ở trạng thái luôn có điện. Nhiều "
               "hệ không nhận ra được tình trạng đó: nếu đầu ra vốn đã có điện trong vận hành bình thường "
               "thì làm sao bạn nhận ra?"))
    b.append(p("Bạn tin tới mức nào rằng một van bảy năm không được dịch chuyển sẽ thực sự đóng khi cần? Bạn "
               "tin tới mức nào rằng một máy phát dự phòng hai năm không được khởi động sẽ thực sự chạy khi "
               "cần? Và cũng câu hỏi đó: bạn tin tới mức nào rằng chiếc máy cắt cỏ sẽ nổ máy nếu nó nằm cả "
               "mùa đông trong ga-ra với xăng trong bình và trong bộ chế hòa khí? Có thể đặt được bao nhiêu "
               "tin cậy vào một thứ mà trong điều kiện bình thường vốn không hoạt động?"))
    b.append(p("Cách duy nhất để biết một hệ đang ngủ có làm việc khi cần hay không là <b>thử</b> nó. Hoặc "
               "bạn phải thử hệ, hoặc hệ phải tự thử được. Vì thế, hệ an toàn thụ động, ngủ, đòi hỏi chẩn "
               "đoán rộng. Phương án thay thế là dùng các hệ vốn đã an toàn theo thiết kế (fail-safe), nơi "
               "những lỗi nguy hiểm như vậy khó xảy ra về mặt thiết kế — nhưng điều này nói chung không "
               "làm được cho mọi thành phần."))
    b.append(p("Điều đó có nghĩa là một hệ được thiết kế cho điều khiển có thể hoàn toàn không phù hợp cho "
               "an toàn. Hai vấn đề chính là <b>bảo mật</b> (tức kiểm soát truy cập) và <b>chẩn đoán</b>."))
    b.append(p("Hệ an toàn đòi hỏi mức kiểm soát truy cập cao để thực thi các tính năng bảo mật và áp đặt "
               "quy trình quản lý thay đổi. Không ai được phép tùy tiện can thiệp vào chức năng an toàn. "
               "Làm sao cho người vận hành truy cập dễ dàng vào một số chức năng nhưng bị khóa khỏi những "
               "chức năng khác? Làm sao biết rằng thay đổi ở một khu vực của hệ sẽ không ảnh hưởng tới một "
               "chức năng tới hạn ở chỗ khác? Nhiều hệ điều khiển không thực hiện được các biện pháp kiểm "
               "soát truy cập hiệu quả."))
    b.append(p("Chẩn đoán rộng là bắt buộc trong hệ an toàn đơn giản vì không phải mọi lỗi đều tự bộc lộ. "
               "Nhiều người cho rằng mọi hệ điện tử hiện đại đều có chẩn đoán rộng. Đáng tiếc là không "
               "phải. Có những lý do kinh tế rất đơn giản khiến điều đó không đúng; sẽ bàn kỹ ở chương 7."))

    b.append(h3("3.3.1 Nhu cầu hạn chế thay đổi", "The Need for Restricting Changes"))
    b.append(p("Hệ thống đo lường an toàn phải được thiết kế để cho phép rất ít tương tác của con người. "
               "Người vận hành tương tác và điều khiển quá trình <em>qua hệ điều khiển</em>. Nếu hệ điều "
               "khiển không còn giữ được điều khiển, các cảnh báo độc lập thường chỉ ra vấn đề; khi đó "
               "người vận hành có thể giám sát vận hành bằng tay. Nếu cả hệ điều khiển tự động lẫn sự can "
               "thiệp của con người đều không tạo được hiệu chỉnh cần thiết, thì tuyến phòng thủ cuối cùng "
               "phải hoạt động <b>tự động và độc lập</b>."))
    b.append(p("Tương tác duy nhất nên được phép giữa người vận hành và hệ an toàn là các lệnh ghi đè "
               "(override) để khởi động và để bảo dưỡng từng phần của hệ. Khi đó phải tuân thủ quy trình "
               "nghiêm ngặt. Mọi người phải biết rằng có một tuyến phòng thủ cuối cùng — một thứ có thể "
               "tin được. Các hệ này phải được kiểm soát truy cập chặt. Điều không ai muốn nhất là một hệ "
               "không hoạt động chỉ vì một người vận hành đơn lẻ đã vô hiệu hóa nó mà không ai biết. "
               "Chuyện đó đã xảy ra rồi."))

    b.append(h3("3.3.2 Chế độ theo yêu cầu và chế độ liên tục",
                "Demand Mode vs. Continuous Mode"))
    b.append(p("Hướng dẫn của AIChE CCPS năm 1993 và bản ANSI/ISA-84.01 năm 1996 đều coi hệ an toàn là hệ "
               "<em>chế độ yêu cầu thấp</em>, dù thời đó chưa dùng thuật ngữ này. Quan điểm là: một hệ an "
               "toàn được thiết kế đúng sẽ ít khi bị đặt yêu cầu — ví dụ khoảng một lần mỗi năm. Tiêu "
               "chuẩn IEC 61508 ra đời sau đó, viết cho mọi ngành, đưa ra khái niệm hệ <em>chế độ yêu cầu "
               "cao</em>, hay <em>chế độ liên tục</em>: đơn giản là những hệ bị đặt yêu cầu thường xuyên. "
               "Ví dụ kinh điển là phanh ô tô. Khái niệm chế độ liên tục sau đó được đưa vào IEC 61511 cho "
               "ngành chế biến và vào ủy ban ISA SP84."))
    b.append(p("Như thường lệ với mọi thay đổi, vấn đề nảy sinh. Các yêu cầu về hiệu năng an toàn vốn được "
               "ghi cho từng mức toàn vẹn an toàn (SIL) chỉ áp dụng cho hệ chế độ yêu cầu thấp. Khái niệm "
               "“xác suất hỏng khi có yêu cầu” không có nghĩa với một hệ có thể bị đặt yêu cầu 10 lần, hay "
               "10.000 lần một năm. Dù vẫn có người không đồng ý với cách giải quyết được chọn, ủy ban đã "
               "thông qua việc gán <em>tốc độ hỏng nguy hiểm</em> thay cho <em>xác suất</em> cho từng mức "
               "SIL. Chênh lệch giữa tốc độ và xác suất là hệ số 10.000, dựa trên đơn giản hóa rằng một "
               "năm có khoảng 10.000 giờ."))
    b.append(note(
        "<b>Đọc kỹ chỗ này.</b> Việc đổi từ xác suất sang tốc độ hỏng không phải là đổi đơn vị cho tiện. "
        "Nó thay đổi câu hỏi: với chế độ yêu cầu thấp, câu hỏi là “xác suất hệ không làm việc khi được gọi "
        "là bao nhiêu”; với chế độ liên tục, câu hỏi là “mỗi giờ hệ hỏng nguy hiểm bao nhiêu lần”. Hai câu "
        "hỏi này cho hai con số khác nhau, và một hệ có thể trả lời tốt câu thứ nhất mà trả lời kém câu "
        "thứ hai."))
    b.append(p("Hệ chế độ liên tục về bản chất giống với cái mà ANSI/ISA-91.01 gọi là “điều khiển tới hạn "
               "về an toàn”. Ngay cả thành viên ủy ban ISA SP84 cũng khó nêu ví dụ về hệ chế độ liên tục "
               "trong ngành chế biến. Một số ví dụ — như chức năng cắt mức cao trong một lò phản ứng theo "
               "mẻ được nạp mỗi ngày một lần — bị nhiều người coi chỉ là ví dụ về điều khiển quá trình tồi, "
               "chứ không phải về an toàn."))

    # ---------------------------------------------------------------- 3.4
    b.append(h2("3.4 Tách rời hệ điều khiển và hệ an toàn",
                "Separation of Control and Safety Systems"))
    b.append(p("Một chủ đề tranh cãi kéo dài trong ngành là có nên gộp hệ điều khiển và hệ an toàn vào một "
               "hệ hay không — nói cách khác, có nên đưa toàn bộ chức năng an toàn vào hệ điều khiển quá "
               "trình? Phía ủng hộ lập luận rằng cả hai hệ ngày nay đều khả trình, hệ điều khiển quá trình "
               "thì đáng tin cậy và có thể dự phòng, vậy tại sao không? Phản bác thì khá đơn giản và "
               "<b>không</b> dựa vào độ tin cậy. Như sẽ thấy, mọi tiêu chuẩn, thực hành khuyến nghị và "
               "hướng dẫn trong ngành đều khuyến nghị cung cấp hai hệ riêng cho điều khiển quá trình và "
               "điều khiển an toàn."))
    b.append(p("Phía ủng hộ việc gộp còn nêu rằng vì hệ điều khiển là chủ động và động, lỗi tự bộc lộ, nên "
               "chúng rất phù hợp cho an toàn vì sẽ không có lỗi ẩn. Ví dụ, một van điều khiển tương tự "
               "liên tục được dịch chuyển, và việc đó sẽ phát hiện vấn đề. Đúng — nhưng không phải mọi vấn "
               "đề. Việc có thêm một solenoid riêng trên van điều khiển (được cấp nguồn từ một hệ an toàn "
               "riêng) vẫn có thể không đáp ứng yêu cầu an toàn tổng thể. Dịch chuyển van không bảo đảm "
               "rằng van sẽ đóng kín hoàn toàn, và dịch chuyển van cũng không kiểm tra được rằng solenoid "
               "sẽ làm việc khi cần. Nếu van hỏng ở trạng thái kẹt — mọi thứ đều hỏng, chỉ là vấn đề thời "
               "điểm — thì sẽ không còn khả năng thực hiện tác động an toàn nào nữa. Cần phân tích cẩn thận "
               "để xem yêu cầu an toàn có được thỏa mãn hay không khi gộp, vì còn nhiều vấn đề khác phải "
               "xét."))
    b.append(quote(
        "Hệ an toàn như các chức năng cắt khẩn cấp nên hoàn toàn độc lập với hệ điều khiển và, khi làm "
        "được, nên đấu dây cứng. Nếu chúng dựa trên máy tính thì máy tính đó phải độc lập với máy tính "
        "điều khiển.",
        "Trevor Kletz"))

    b.append(h3("3.4.1 HSE", "HSE"))
    b.append(p("Người Anh không thể nói rõ hơn về sự cần thiết phải tách rời. Tài liệu của họ gồm hai phần: "
               "Phần I dành cho các nhà quản lý, chỉ 17 trang, trong đó <b>Hình 3-1</b> chiếm trọn một "
               "trang. Phần kỹ thuật — dành cho kỹ sư — dày khoảng 170 trang. Cảm biến riêng, hộp logic "
               "riêng, van riêng."))
    b.append(fig(1, F.fig_3_1(), "vi"))

    b.append(h3("3.4.2 AIChE — CCPS", "AIChE — CCPS"))
    b.append(p("Tài liệu của Viện Kỹ sư Hóa học Hoa Kỳ (AIChE) là một bộ “hướng dẫn”. Khoảng 50 trang dành "
               "cho cái được gọi là hệ liên động, kèm thêm tư liệu nền tốt. Vì là hướng dẫn, văn bản không "
               "dùng những từ ngụ ý bắt buộc như “shall”. Thay vào đó là những câu như “thông thường…” — "
               "luôn mở ra nhiều cách hiểu. Tuy vậy, một số câu rất dứt khoát:"))
    b.append(quote(
        "Thông thường, (các) bộ giải logic được tách khỏi các thành phần tương tự trong hệ điều khiển quá "
        "trình cơ bản (BPCS). Hơn nữa, cảm biến đầu vào và phần tử chấp hành cuối của SIS nói chung cũng "
        "tách khỏi các thành phần tương tự trong BPCS.",
        "AIChE CCPS, Guidelines for Safe Automated Process Control"))
    b.append(p("Căn cứ nào để không làm theo cái mà một cuốn sách do các chuyên gia trong ngành — toàn là "
               "người dùng cuối — coi là “thông thường” và “nói chung” phù hợp?"))
    b.append(quote(
        "Hãy bảo đảm tách rời về mặt vật lý và chức năng, và có nhận dạng phân biệt, giữa cảm biến, cơ cấu "
        "chấp hành, bộ giải logic, mô-đun I/O và khung của BPCS với của SIS…",
        "AIChE CCPS"))
    b.append(p("Nói cách khác: tách các thành phần về mặt vật lý để lỗi của bộ này không ảnh hưởng bộ kia. "
               "Thực hiện <em>logic khác nhau</em>, vì nếu cùng một logic được làm ở cả hai hệ và có sai "
               "sót trong đặc tả chức năng thì cả hai hệ sẽ cùng một lỗi. Và nhận dạng hai hệ khác nhau "
               "trên bản vẽ cũng như ngoài hiện trường, để mọi người nhận ra: “À, đây là thiết bị an toàn, "
               "mình phải cẩn thận và theo quy trình bổ sung.”"))

    b.append(h3("3.4.3 IEC 61508", "IEC 61508"))
    b.append(p("Tiêu chuẩn quốc tế này dành cho mọi ngành và bao quát việc dùng hệ an toàn kiểu rơ-le, bán "
               "dẫn và khả trình (hay E/E/PES: hệ điện, điện tử và điện tử khả trình)."))
    b.append(quote(
        "Hệ điều khiển của EUC (thiết bị được điều khiển) phải tách rời và độc lập với các hệ liên quan an "
        "toàn E/E/PE, với các hệ liên quan an toàn dùng công nghệ khác, và với các phương tiện giảm rủi ro "
        "bên ngoài.",
        "IEC 61508"))
    b.append(p("Nếu không thỏa mãn được yêu cầu này thì toàn bộ hệ điều khiển phải được thiết kế như một hệ "
               "liên quan an toàn và tuân theo các yêu cầu của tiêu chuẩn. Một ví dụ là điều khiển máy bay: "
               "khó hình dung một hệ an toàn riêng biệt được thiết kế để làm cho một chiếc máy bay ở độ cao "
               "35.000 feet rơi về trạng thái an toàn. Trong một số trường hợp, điều khiển và an toàn đan "
               "vào nhau tới mức toàn bộ hệ phải được thiết kế như hệ liên quan an toàn."))

    b.append(h3("3.4.4 ANSI/ISA-84.00.01-2004", "ANSI/ISA-84.00.01-2004"))
    b.append(p("Bản gốc năm 1996 của tiêu chuẩn này có hai câu về tách rời, rất rõ ràng và dễ hiểu:"))
    b.append(quote("Cảm biến cho SIS phải tách khỏi cảm biến của BPCS.", "ANSI/ISA-84.01-1996"))
    b.append(p("Có hai ngoại lệ: nếu dự phòng đủ lớn, hoặc nếu phân tích mối nguy xác định rằng đã có đủ "
               "các lớp an toàn khác bảo vệ thỏa đáng."))
    b.append(quote("Bộ giải logic phải tách khỏi BPCS…", "ANSI/ISA-84.01-1996"))
    b.append(p("Có ngoại lệ cho trường hợp không thể tách chức năng điều khiển khỏi chức năng an toàn, ví "
               "dụ thiết bị quay tốc độ cao như tuabin khí."))
    b.append(p("Tiêu chuẩn ISA nói chung được soát xét năm năm một lần. Thay vì viết lại hoàn toàn tiêu "
               "chuẩn của ISA SP84, ủy ban đồng ý lấy tiêu chuẩn IEC 61511 làm chuẩn. Cách diễn đạt của "
               "IEC về tách rời không dứt khoát như bản 1996 của ISA SP84. Thực tế, một khiếu nại đúng về "
               "điểm này đã làm chậm việc phát hành tiêu chuẩn mới cả một năm. Người dùng đơn giản là không "
               "muốn bị áp đặt tách rời."))
    b.append(p("Nhiều người cho rằng với hệ rất nhỏ, hoặc hệ có yêu cầu hiệu năng thấp, gộp điều khiển và "
               "an toàn có thể chấp nhận được, miễn là mọi thứ vẫn được làm đúng. Tiêu chuẩn mới nói:"))
    b.append(ul([
        "<b>Điều 9.5.1:</b> “Thiết kế… phải được đánh giá để bảo đảm xác suất lỗi do nguyên nhân chung… và "
        "lỗi phụ thuộc giữa… các lớp bảo vệ và BPCS là đủ thấp so với yêu cầu toàn vẹn an toàn tổng thể "
        "của các lớp bảo vệ.” Định nghĩa “đủ thấp” dĩ nhiên mở ra nhiều cách hiểu, cũng như việc thế nào "
        "là một đánh giá phù hợp.",
        "<b>Điều 9.4.3:</b> “Nếu một mức giảm rủi ro lớn hơn 10 được tuyên bố cho BPCS thì BPCS phải được "
        "thiết kế theo tiêu chuẩn.” Nghĩa là: nếu bạn định gộp điều khiển và an toàn vào một hộp và tuyên "
        "bố một mức hiệu năng, kể cả chỉ ở mức SIL 1 thấp nhất, thì hệ sẽ phải được thiết kế theo tiêu "
        "chuẩn. Điều đó khả thi với hệ nhỏ nhưng hoàn toàn không thực tế với hệ lớn.",
        "<b>Điều 11.2.4:</b> “Nếu không có ý định đánh giá BPCS theo tiêu chuẩn này, thì BPCS phải được "
        "thiết kế tách rời và độc lập tới mức mà tính toàn vẹn chức năng của SIS không bị suy giảm.” Lại "
        "là những câu như “tới mức mà…” — luôn mở.",
        "<b>Điều 11.2.10:</b> “Một thiết bị dùng để thực hiện một phần chức năng an toàn đo lường không "
        "được dùng cho mục đích điều khiển quá trình cơ bản, khi lỗi của thiết bị đó dẫn tới lỗi của chức "
        "năng điều khiển quá trình cơ bản gây ra yêu cầu đặt lên chức năng an toàn đo lường, trừ khi đã "
        "thực hiện phân tích để xác nhận rủi ro tổng thể là chấp nhận được.” Nói cách khác, cả thiết bị "
        "trường cũng phải tách. Tuy vậy vẫn còn một “cửa ra” nếu “một phân tích” biện minh được cho việc "
        "gộp hệ.",
    ]))
    b.append(p("Loại biện minh nào? Nói đơn giản: loại biện minh mà bạn sẵn sàng đem ra tòa."))

    b.append(h3("3.4.5 API RP 14C", "API RP 14C"))
    b.append(p("Viện Dầu khí Hoa Kỳ, Thực hành Khuyến nghị 14C, “Phân tích, thiết kế, lắp đặt và thử nghiệm "
               "các hệ an toàn bề mặt cơ bản cho giàn khai thác ngoài khơi”, áp dụng cho thiết kế hệ dừng "
               "của giàn ngoài khơi. Nó quy định cách xác định đầu vào và đầu ra cho hệ dừng của từng cụm "
               "công nghệ. Tuy nhiên nó không nói gì về thiết kế hộp logic (vì giả định phần lớn hệ logic "
               "là khí nén)."))
    b.append(quote(
        "Hệ an toàn nên cung cấp hai mức bảo vệ… Hai mức bảo vệ này phải độc lập với, và bổ sung thêm cho, "
        "các thiết bị điều khiển dùng trong vận hành bình thường.",
        "API RP 14C"))
    b.append(p("Đáng ngạc nhiên là một số tài liệu lại mở tới mức ấy. Ví dụ, một van an toàn và một hệ phát "
               "hiện khí có được coi là “hai mức bảo vệ độc lập và bổ sung cho các thiết bị điều khiển” "
               "không? 14C cho bạn biết cách xác định I/O và logic chức năng cho hệ; nó không nói phải "
               "dùng loại hộp logic nào. Người ta đã lắp hệ khí nén, rơ-le, PLC và TMR (dự phòng ba mô-đun) "
               "trên các giàn ngoài khơi và tất cả đều tuyên bố đã đáp ứng RP 14C — và thực sự có thể là "
               "tất cả đều đúng."))

    b.append(h3("3.4.6 API RP 554", "API RP 554"))
    b.append(p("Thực hành Khuyến nghị 554 của API, “Thiết bị đo và điều khiển quá trình”, áp dụng cho nhà "
               "máy lọc dầu. Các câu về tách rời khá thẳng: “Chức năng dừng và chức năng điều khiển nên "
               "nằm trong phần cứng riêng và độc lập…”, và “Thiết bị dừng nên dành riêng và tách khỏi cảnh "
               "báo trước khi dừng và khỏi hệ điều khiển quá trình.” Nói cách khác, hệ logic liên quan an "
               "toàn và thiết bị trường nên dành riêng và tách khỏi hệ điều khiển và hệ cảnh báo. Lưu ý "
               "rằng tài liệu này, cũng như 14C, là thực hành khuyến nghị chứ không phải tiêu chuẩn bắt "
               "buộc: nó dùng “should” chứ không dùng “shall”."))

    b.append(h3("3.4.7 NFPA 85", "NFPA 85"))
    b.append(p("Hiệp hội Phòng cháy Quốc gia Hoa Kỳ có các tiêu chuẩn áp dụng cho hệ quản lý lò hơi và đầu "
               "đốt, như “Quy phạm an toàn cho hệ lò hơi và hệ đốt”. Có thể coi đây là ví dụ của tiêu chuẩn "
               "“quy định cụ thể” (prescriptive): những câu đen trắng, dễ hiểu, và vì thế làm yên lòng một "
               "số người. Tiêu chuẩn này yêu cầu tách rời rất rõ:"))
    b.append(quote(
        "Yêu cầu về tính độc lập: Hệ logic thực hiện các chức năng an toàn cho quản lý đầu đốt không được "
        "gộp với bất kỳ hệ logic nào khác.",
        "NFPA 85"))
    b.append(p("Một DCS có thể được dùng cho 6.000 điểm I/O của một lò hơi công nghiệp khổng lồ, nhưng hệ "
               "quản lý đầu đốt phải là một hệ riêng. Còn một câu nữa: “Hệ logic chỉ được giới hạn cho một "
               "lò hơi.” Nghĩa là dùng một hệ logic dự phòng có khả năng chạy nhiều chương trình để phục vụ "
               "nhiều hệ quản lý đầu đốt là không chấp nhận được. Tuy vậy, các cơ sở tự bảo hiểm có thể "
               "không theo NFPA."))

    b.append(h3("3.4.8 IEEE 603", "IEEE 603"))
    b.append(p("Viện Kỹ sư Điện và Điện tử có các tiêu chuẩn áp dụng cho thiết kế nhà máy điện hạt nhân, như "
               "“Tiêu chí tiêu chuẩn cho hệ an toàn của nhà máy điện hạt nhân”. Ngành chế biến dĩ nhiên "
               "không bị ràng buộc chặt như ngành hạt nhân, nhưng khái niệm các lớp an toàn tách rời ở đây "
               "rất rõ:"))
    b.append(quote(
        "Thiết kế hệ an toàn phải bảo đảm rằng những lỗi có thể tin được và những tác động kéo theo của "
        "các hệ khác không ngăn được hệ an toàn thỏa mãn các yêu cầu.",
        "IEEE 603"))
    b.append(p("Một số cơ sở hạt nhân dùng cấu hình máy tính dự phòng bốn (quad), kiểu hai hệ nối tiếp ghép "
               "song song với hai hệ khác. Và như thế vẫn chưa đủ với một số nơi: họ dùng hai hệ dự phòng "
               "bốn như vậy ghép với nhau. Hoa Kỳ thường dùng hệ bốn lớp, có hệ “tương tự truyền thống” "
               "làm dự phòng."))
    b.append(p("Một bài báo trên tạp chí Anh vài năm trước mô tả việc thử phần mềm cho hệ an toàn khả trình "
               "của một nhà máy điện hạt nhân Anh: 50 kỹ sư làm trong 6 tháng mới thử xong! Khó tin rằng "
               "nhiều công ty trong ngành hóa dầu có thể chi 25 người-năm để thử từng hệ an toàn của mình. "
               "Một người ở Ủy ban Điều tiết Hạt nhân (NRC) nói với một trong hai tác giả rằng con số không "
               "phải 25 người-năm mà là vài trăm người-năm."))

    # ---------------------------------------------------------------- 3.5
    b.append(h2("3.5 Lỗi do nguyên nhân chung và lỗi hệ thống/chức năng",
                "Common Cause and Systematic/Functional Failures"))
    b.append(p("Có nhiều tên gọi và định nghĩa khác nhau cho nguyên nhân chung. Về bản chất, lỗi do nguyên "
               "nhân chung là <em>một</em> tác nhân căng thẳng hay một lỗi duy nhất tác động lên nhiều hạng "
               "mục hoặc nhiều phần của hệ."))
    b.append(p("Một cách gọi vấn đề này là “hệ số beta”: phần trăm của toàn bộ lỗi đã nhận dạng trong một "
               "“nhánh” của hệ dự phòng mà có thể ảnh hưởng tới các thành phần giống nhau và làm hỏng cả "
               "hệ. Ví dụ, giả sử một bộ xử lý trung tâm (CPU) có tốc độ hỏng 10⁻⁶ lỗi/giờ. Nếu CPU được "
               "nhân ba và cả ba đặt cạnh nhau trong cùng một khung, một số lỗi có thể ảnh hưởng đồng thời "
               "hai hoặc ba CPU (lỗi thiết kế, lỗi chế tạo, lỗi phần mềm). Với hệ số beta 10 %, hệ sẽ hành "
               "xử như không dự phòng với tốc độ hỏng 10⁻⁶ lỗi/giờ."))
    b.append(note(
        "<b>Hệ số beta là mô hình, không phải hiện thực.</b> Nó thuần túy thực nghiệm — một cách ước lượng "
        "hiện thực, không phải bản thân hiện thực. Có nhiều kỹ thuật đã được ghi chép để ước lượng giá trị "
        "beta."))
    b.append(p("Lỗi hệ thống, còn gọi là lỗi chức năng, tác động lên toàn bộ hệ và vì thế đôi khi được xếp "
               "vào nhóm lỗi do nguyên nhân chung. Ví dụ về lỗi hệ thống thường là lỗi con người trong "
               "thiết kế, vận hành và bảo dưỡng; tuy vậy nhiệt, rung và các yếu tố bên ngoài khác cũng có "
               "thể được tính trong định nghĩa. Những lỗi này có thể tác động lên hệ dự phòng hoặc không "
               "dự phòng."))
    b.append(p("Một lỗi hệ thống khi đặc tả van solenoid có thể khiến van không làm việc đúng ở nhiệt độ "
               "thấp. Nếu dùng van dự phòng thì lỗi hệ thống đó cũng trở thành lỗi do nguyên nhân chung. "
               "Trong khi một số lỗi hệ thống tương đối dễ nhận ra (ví dụ lỗi thiết kế), con số hay tỉ lệ "
               "chính xác của chúng thường khó định lượng hơn. Ví dụ, dự đoán được chính xác tới đâu tần "
               "suất một lỗi thiết kế kỹ thuật xảy ra, hay việc một kỹ thuật viên bảo dưỡng hiệu chuẩn sai "
               "cả ba bộ truyền?"))
    b.append(p("Một nghiên cứu trong ngành hạt nhân phát hiện 25 % số lỗi ở nhà máy điện hạt nhân liên quan "
               "tới nguyên nhân chung. Các điều tra trong hệ điều khiển dự phòng cho thấy tỉ lệ nguyên nhân "
               "chung từ 10 % đến 30 %. Đáng ngạc nhiên là một số hệ rất dư thừa vẫn còn điểm hỏng đơn. Có "
               "một hệ máy tính nối mạng với đường truyền dự phòng bảy lớp; đáng tiếc là cả bảy đều đi qua "
               "cùng một sợi cáp quang, và khi cáp bị cắt thì toàn hệ mất. Rõ ràng không ai cố ý thiết kế "
               "như vậy. Vấn đề là: mọi thứ cuối cùng lớn tới mức một cá nhân không thể “thấy” hết, và một "
               "số hạng mục chắc chắn lọt qua kẽ."))
    b.append(p("Nếu chức năng điều khiển và chức năng an toàn được thực hiện trong cùng một hệ thì luôn có "
               "khả năng xảy ra lỗi do nguyên nhân chung. Hai hệ càng tách rời về mặt vật lý thì càng khó "
               "có lỗi đơn tác động lên cả hai. Một câu đơn giản tóm được ý này: “Đừng bỏ tất cả trứng vào "
               "một giỏ.” Dù cái giỏ có chắc và đáng tin tới đâu, luôn có những hoàn cảnh không lường trước "
               "khiến nó rơi. Mọi thứ đều hỏng, chỉ là vấn đề thời điểm."))

    b.append(h3("3.5.1 Vấn đề con người", "Human Issues"))
    b.append(p("Các tiêu chuẩn khác nhau đều nói hệ điều khiển và hệ an toàn phải tách rời, nhưng họ không "
               "thực sự nói <em>vì sao</em>. Vấn đề thực ra khá rõ ràng, và phần lớn quy về con người."))
    b.append(p("Hệ an toàn đòi hỏi quản lý thay đổi nghiêm ngặt. Nếu gộp điều khiển và an toàn vào cùng một "
               "hệ, làm sao cấp cho người vận hành quyền truy cập vào những chức năng họ cần thay đổi "
               "thường xuyên, đồng thời khóa họ khỏi những chức năng họ không được đụng tới? Làm sao chắc "
               "rằng thay đổi ở một khu vực (ví dụ logic phần mềm) không ảnh hưởng tới một chức năng an "
               "toàn ở chỗ khác? Làm sao chắc rằng việc đặt một vòng điều khiển vào bypass — chuyện rất "
               "bình thường — không ảnh hưởng tới hoạt động của một cảnh báo hay một tác động an toàn? Cách "
               "duy nhất để có được sự bảo đảm thực sự là có hai hệ riêng."))
    b.append(p("Một ví dụ thực tế giúp thấy rõ điều này. Câu chuyện được kể cho một trong hai tác giả trong "
               "một bữa trưa ở kỳ họp ủy ban ISA SP84. Một công ty người dùng mua lại một nhà máy có sẵn "
               "của một tổ chức khác. Một kỹ sư của công ty mẹ được cử đi kiểm toán hệ điều khiển và hệ an "
               "toàn của nhà máy vừa mua. Kỹ sư này phát hiện toàn bộ chức năng điều khiển và an toàn đều "
               "được thực hiện trong DCS. Kiểm tra thêm, ông thấy <b>một phần ba</b> chức năng an toàn đã "
               "đơn giản là biến mất (bị xóa), <b>một phần ba</b> khác đang ở trạng thái bypass, và "
               "<b>phần ba</b> còn lại được thử và phát hiện là không hoạt động."))
    b.append(p("Có thể lập luận rằng nếu thiết lập và tuân thủ quy trình đúng thì tình huống đó đã không xảy "
               "ra. Suy cho cùng, phải có quy trình cho việc bypass, bảo dưỡng, thử nghiệm và quản lý thay "
               "đổi hệ an toàn. Đáng tiếc là quy trình thường bị vi phạm, dù cố ý hay vô tình. Suy cho "
               "cùng, nếu tất cả chúng ta đều là người lái xe đúng luật và tuân thủ quy trình thì đã không "
               "cần dây an toàn hay túi khí."))

    # ---------------------------------------------------------------- summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Hệ điều khiển quá trình là chủ động và động, nên phần lớn lỗi tự bộc lộ. Hệ an toàn là thụ "
               "động hay ngủ, nên nhiều lỗi không tự bộc lộ. Hệ an toàn cần hoặc thử nghiệm bằng tay, hoặc "
               "tự chẩn đoán hiệu quả — điều mà nhiều hệ điều khiển đa dụng không làm được tốt."))
    b.append(p("Hệ điều khiển được thiết kế để cho phép truy cập tương đối dễ, để người vận hành thực hiện "
               "những thay đổi cần thiết. Hệ an toàn thì đòi hỏi quy trình bảo mật và kiểm soát truy cập "
               "nghiêm ngặt để ngăn thay đổi vô ý. Bản thân hệ điều khiển, và mọi thay đổi trên nó, không "
               "được ngăn hệ an toàn làm việc đúng."))
    b.append(p("Cách đây không lâu, điều khiển quá trình và an toàn được thực hiện trên hai hệ công nghệ "
               "khác nhau và tách rời: hệ điều khiển khí nén được thay bằng DCS dựa trên phần mềm, hệ an "
               "toàn dùng rơ-le được thay bằng PLC dựa trên phần mềm. Gộp cả hai vào một hệ mang lại những "
               "lợi ích tiềm năng: một nguồn cung duy nhất, đơn giản hóa kho phụ tùng, bảo dưỡng và đào "
               "tạo, và có thể giảm chi phí. Nhưng tiêu chuẩn, hướng dẫn và thực hành khuyến nghị của rất "
               "nhiều ngành đều phản đối mạnh mẽ cách làm đó. Vấn đề hầu như không liên quan tới độ tin cậy "
               "của hệ điều khiển hiện đại."))
    b.append(p("Thiết kế hệ an toàn đòi hỏi tuân theo các yêu cầu thiết kế nghiêm ngặt và bảo thủ. Phân "
               "tích, ghi chép, thiết kế, vận hành, bảo dưỡng và quản lý thay đổi đều cần thêm công sức cho "
               "hệ an toàn. Gộp cả điều khiển và an toàn vào một hệ nghĩa là công sức thêm đó phải áp lên "
               "toàn bộ hệ điều khiển — điều này đơn giản là không khả thi về kinh tế với bất kỳ hệ có quy "
               "mô hợp lý nào."))
    b.append(p("Bỏ tất cả trứng vào một giỏ hiếm khi là ý hay. Mọi thứ đều hỏng, chỉ là vấn đề thời điểm."))
    return "\n".join(b)


# ===================================================================== EN
def body_en():
    b = []
    b.append(lead(
        "This is a short chapter, but it lays the foundation for the whole book: it answers why the control "
        "system and the safety system must be two different systems rather than two programs in one "
        "processor. The answer has nothing to do with computer reliability — it lies in the fact that the "
        "two systems have different failure modes, different users, and different rules about change."))

    b.append(h2("Two systems, two jobs, two sets of habits"))
    b.append(p("A control system is judged by how well it holds the plant at the set point. A safety system "
               "is judged by whether it still works on the day it is needed — which may be a day five years "
               "from now, after five years in which it did nothing at all. Those two judgements cannot be "
               "satisfied by the same design philosophy, because they reward opposite things."))
    b.append(p("Control rewards accessibility. The operator must be able to change a set point at three in "
               "the morning without waking anybody, put a loop in manual, force an output, tune a "
               "controller. Every one of those actions is a normal, desirable, safety-improving act in a "
               "control system, and every one of them is a potentially catastrophic act if applied to a "
               "safety function. A single system cannot be simultaneously easy to change in one place and "
               "impossible to change in another, when both places are the same engineering database."))
    b.append(p("Safety rewards inertia. Nothing should change, nobody should touch it, and every change "
               "should require a signature, a review and a record. The two philosophies are not in tension "
               "because one is careless; they are in tension because they are both right, about different "
               "things."))

    b.append(h2("Revealed and unrevealed: the asymmetry that decides everything"))
    b.append(p("The deepest difference is not philosophical but statistical. A control loop announces its "
               "own failure. If a flow controller dies, the flow stops following the set point, the "
               "operator sees it within minutes, and the failure is repaired. The failure is revealed, and "
               "the time to repair it is short, and the probability that the loop is dead at some random "
               "moment is small."))
    b.append(p("A safety function announces nothing. It sits at logic one, output energised, valve open, "
               "year after year. If its sensor has drifted out of range, or its output card has failed "
               "energised, or its logic has been bypassed and never restored, the plant looks exactly the "
               "same as it does when everything is healthy. The failure is unrevealed, and the only thing "
               "that converts it into a revealed failure is a proof test — or a demand, which is the same "
               "test conducted at the worst possible moment."))
    b.append(p("This asymmetry explains the otherwise puzzling fact that safety systems need far more "
               "diagnostics than control systems, even though they are simpler. A control system's "
               "diagnostics exist to help maintenance; a safety system's diagnostics exist because without "
               "them there is no information at all about whether the system is alive. It also explains "
               "why the standards' insistence on separation is not about redundancy. Two systems in one box "
               "can be perfectly redundant electrically and still share the failure that matters most: the "
               "one nobody can see."))

    b.append(h2("The standards say separate; the reason is human"))
    b.append(p("Every document quoted in this chapter — the HSE two-part volume, the CCPS guidelines, IEC "
               "61508, ISA-84, API 14C and 554, NFPA 85, IEEE 603 — arrives at the same requirement from a "
               "different direction, and the wording ranges from the absolute (“shall not be combined”) to "
               "the negotiable (“to the extent that…”). It is tempting to read that range as a difference "
               "in conviction. It is more accurately a difference in how much each document trusts the "
               "management system that will operate the plant."))
    b.append(p("The HSE document makes the point with a single picture that fills a whole page, and it is "
               "worth more than the sentence it illustrates: sensors separate, logic separate, final "
               "elements separate. Not because two processors in one cabinet would be unreliable, but "
               "because the boundary has to be visible to the person who is about to do something unwise."))
    b.append(fig(1, F.fig_3_1(), "en"))
    b.append(p("The prescriptive standards — NFPA 85 in particular — come from industries where the "
               "consequence of a mistake is immediate and public, and where the regulator can afford to be "
               "blunt. The performance-based ones come from industries where the same plant may be run by "
               "a large competent operator or by a small one with three engineers, and where a rule written "
               "for the worst case would be unaffordable for the best. Neither approach is wrong; they "
               "simply put the burden of judgement in different places."))
    b.append(p("What every one of them assumes, however, is that human beings will eventually do something "
               "they should not. The bypass that is never removed, the alarm that is silenced because it "
               "is a nuisance, the interlock deleted during a commissioning push and never restored — the "
               "audit story in section 3.5.1 is not an unusual case, it is the normal end state of a "
               "system that makes the wrong action easy. Separation is not a technical fix for that; it is "
               "the recognition that the fix has to be organisational, and that the organisation needs a "
               "physical boundary to defend."))

    b.append(h2("Beta factor: a number that admits it is a guess"))
    b.append(p("The beta factor is one of the few places in functional safety where the arithmetic openly "
               "confesses. It says: of all the failures that could take out one leg of a redundant system, "
               "this fraction will take out the others too. A beta of ten percent turns a triplicated "
               "processor into a single processor with a tenth of the failure rate, which is exactly what "
               "it deserves to be called — a model, not a measurement."))
    b.append(p("The value of the model is that it forces the question. Once you have written down that ten "
               "percent of failures are common cause, you have to ask which ten percent, and the answer is "
               "almost never in the hardware. It is in the things the legs share: the same power supply, "
               "the same cabinet, the same firmware revision, the same technician with the same calibration "
               "procedure, the same impulse line, the same fibre route. Redundancy that shares any of "
               "those is redundancy on paper only, and the beta factor is the instrument that makes the "
               "paper honest."))
    return "\n".join(b)
