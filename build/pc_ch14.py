# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 14, Self-Tuning Intelligent Control and
Statistical Process Control (Wolfgang Altmann, IDC Technologies)."""
import pc14fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 18
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"

_D2 = [("2", "1,128", "0,853"), ("3", "1,693", "0,888"), ("4", "2,059", "0,880"),
       ("5", "2,326", "0,864"), ("6", "2,534", "0,848"), ("7", "2,704", "0,833"),
       ("8", "2,847", "0,820"), ("9", "2,970", "0,808"), ("10", "3,078", "0,797")]

_A2 = [("2", "1,880", "0,000", "3,268"), ("3", "1,023", "0,000", "2,574"),
       ("4", "0,729", "0,000", "2,282"), ("5", "0,577", "0,000", "2,114"),
       ("6", "0,483", "0,000", "2,004"), ("7", "0,419", "0,076", "1,924"),
       ("8", "0,373", "0,136", "1,864"), ("9", "0,337", "0,184", "1,816"),
       ("10", "0,308", "0,223", "1,777")]


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Tự chỉnh định (self-tuning)</em> — bộ điều khiển tự tính lại tham số của chính nó. · "
            "<em>Nhận dạng hệ (system identifier)</em> — khối ước lượng tham số của quá trình. · "
            "<em>Tổng hợp bộ điều khiển</em> — khối tính ra bộ tham số mới từ các tham số vừa nhận "
            "dạng. · "
            "<em>Điều khiển theo lịch trình độ lợi</em> — đổi độ lợi theo một biến phụ đo được. · "
            "<em>Nhóm con (subgroup)</em> — một mẫu n giá trị lấy cùng một thời điểm. · "
            "<em>Biến thiên có kiểm soát</em> — chỉ do nguyên nhân ngẫu nhiên. · "
            "<em>Nguyên nhân gán được</em> — nguyên nhân cụ thể gây ra một điểm nằm ngoài giới hạn. · "
            "<em>SPC</em> — điều khiển quá trình bằng thống kê.")
    return note(
        "<b>Key terms.</b> <em>Self-tuning</em> — a controller that recomputes its own parameters. · "
        "<em>System identifier</em> — the block that estimates the process parameters. · "
        "<em>Controller synthesiser</em> — the block that computes a new parameter set from the "
        "identified ones. · <em>Gain scheduling</em> — changing the gain against a measured auxiliary "
        "variable. · <em>Subgroup</em> — a sample of n values taken at one instant. · <em>Controlled "
        "variation</em> — caused by chance alone. · <em>Assignable cause</em> — a specific cause that "
        "puts a point outside the limits. · <em>SPC</em> — statistical process control.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Mười ba chương vừa qua đã dạy cách chọn và chỉnh một bộ điều khiển. Chương cuối này đặt câu "
        "hỏi khác đi: nếu bộ điều khiển tự chỉnh lấy thì sao, và làm sao biết cả vòng điều khiển đang "
        "làm tốt hay không?"))
    b.append(p(
        "Hai câu hỏi ấy nghe không liên quan, nhưng chúng là hai nửa của cùng một vấn đề. Tự chỉnh định "
        "là chuyện của bộ điều khiển: nó tự đo đáp ứng của quá trình rồi sửa tham số của mình. SPC là "
        "chuyện của người quản lý quá trình: nhìn chuỗi sản phẩm và nói xem quá trình còn ổn định hay "
        "đã trôi. Cái thứ nhất hỏi “chỉnh bao nhiêu”, cái thứ hai hỏi “có cần chỉnh hay không”. Và câu "
        "trả lời của SPC thường là: không, vấn đề không nằm ở bộ điều khiển."))
    b.append(p(
        "Đây cũng là chương khép lại cuốn sách, nên nó dừng lại ở những điều có thể dùng được ngay "
        "trong một nhà máy thật: một bảng hệ số, một tờ giấy kẻ ô, và một cách nhìn để không sửa nhầm "
        "chỗ."))

    b.append(h2("14.1 Mục tiêu", "Objectives"))
    b.append(p("Sau khi học chương này, học viên phải có khả năng:"))
    b.append(ul([
        "Mô tả được lý thuyết và cách vận hành của một bộ điều khiển tự chỉnh định;",
        "Mô tả được khái niệm điều khiển quá trình bằng thống kê (SPC) và việc dùng nó để phân tích "
        "và chỉ ra mức hiệu năng của hệ điều khiển."]))
    b.append(p(
        "Chương này giới thiệu các khái niệm cơ bản của bộ điều khiển tự chỉnh định hay thích nghi, "
        "của bộ điều khiển thông minh, và đưa ra một cái nhìn tổng quan về điều khiển quá trình bằng "
        "thống kê (SPC)."))

    b.append(h2("14.2 Bộ điều khiển tự chỉnh định", "Self-Tuning Controllers"))
    b.append(p(
        "Bộ điều khiển tự chỉnh định có khả năng tự tính lại các tham số chỉnh định của bộ điều khiển "
        "quá trình. Chúng xuất hiện trên thị trường vào đầu những năm 1970, và đã tiến hoá từ những "
        "loại dùng kiểu điều chỉnh tối ưu và kiểu điều khiển, tới những loại hiện nay — nhờ sự ra đời "
        "của bộ xử lý tốc độ cao — dựa trên các thuật toán điều khiển thích nghi."))
    b.append(p("Các thành phần chính của một hệ tự chỉnh định được minh hoạ ở Hình 14-1, gồm:"))
    b.append(ul([
        "<b>Bộ nhận dạng hệ</b> — mô hình này ước lượng các tham số của quá trình.",
        "<b>Bộ tổng hợp bộ điều khiển</b> — mô hình này phải tổng hợp, hay tính ra, các tham số bộ "
        "điều khiển do các hàm mục tiêu điều khiển chỉ định.",
        "<b>Khối thực thi bộ điều khiển</b> — đây là bộ điều khiển mà các tham số của nó (độ lợi Kc, "
        "thời gian tích phân Ti, thời gian vi phân Td, v.v.) được bộ tổng hợp thay đổi và sửa lại theo "
        "chu kỳ."]))
    b.append(fig(1, F.fig_14_1()))

    b.append(h3("14.2.1 Bộ nhận dạng hệ", "The System Identifier"))
    b.append(p(
        "Bộ nhận dạng hệ, bằng cách so sánh tác động của PV do một thay đổi MV gây ra, và dùng các "
        "thuật toán dựa trên ước lượng đệ quy, xác định đáp ứng của hệ. Việc này thường được thực hiện "
        "bằng lô-gic mờ: rút ra những đặc trưng động học then chốt từ một dao động quá độ trong động "
        "học của hệ. Những dao động ấy có thể do bộ điều khiển cố ý tạo ra, nhưng thường là lúc khởi "
        "động và những dao động do nhiễu quá trình — tức những dao động bình thường."))
    b.append(p(
        "Điểm cần nhớ: bộ nhận dạng không đo quá trình, nó chỉ nghe trộm quá trình. Mọi thứ nó biết đều "
        "đến từ những lần quá trình tình cờ bị kích thích — và nếu quá trình chạy êm quá lâu, nó không "
        "có gì để học."))

    b.append(h3("14.2.2 Bộ tổng hợp bộ điều khiển", "The Controller Synthesizer"))
    b.append(p(
        "Các giá trị mong muốn cho các thuật toán P, I và D mà bộ điều khiển dùng được khối này xác "
        "định. Các phép tính có thể từ đơn giản đến rất phức tạp, tuỳ theo các luật được dùng."))

    b.append(h3("14.2.3 Vận hành tự chỉnh định", "Self Tuning Operation"))
    b.append(p(
        "Kỹ thuật này cần một điểm xuất phát rút ra từ hiểu biết về những nhà máy đã biết và đang vận "
        "hành có tính chất tương tự. Phương pháp này chịu ảnh hưởng của quan hệ giữa tham số nhà máy và "
        "tham số bộ điều khiển. Vì các tham số của nhà máy chưa biết, chúng được lấy bằng các thuật toán "
        "nhận dạng tham số đệ quy. Các tham số điều khiển sau đó được lấy từ ước lượng các tham số nhà "
        "máy."))
    b.append(p(
        "Xét Hình 14-1: bộ điều khiển được gọi là “tự chỉnh định” vì nó có khả năng tự chỉnh các tham số "
        "của mình. Nó gồm hai vòng: một vòng trong là vòng điều khiển thông thường nhưng có tham số "
        "thay đổi, và một vòng ngoài gồm bộ nhận dạng và bộ tổng hợp điều khiển, chúng chỉnh các tham "
        "số của bộ điều khiển quá trình."))
    b.append(p(
        "Hai vòng này phải chạy ở hai tốc độ khác hẳn nhau. Vòng trong chạy theo từng giây; vòng ngoài "
        "phải quan sát ít nhất vài chu kỳ dao động rồi mới kết luận, nên nó chạy theo từng phút hoặc "
        "từng giờ. Nếu vòng ngoài chạy nhanh như vòng trong, nó sẽ đuổi theo chính những dao động do "
        "nó vừa gây ra."))

    b.append(h2("14.3 Bộ điều khiển theo lịch trình độ lợi", "Gain Scheduling Controller"))
    b.append(p(
        "Điều khiển theo lịch trình độ lợi dựa trên một thực tế: có thể tìm được những biến phụ hoặc "
        "biến thay thế của quá trình, chúng tương quan tốt với biến quá trình chính. Nhờ những biến phụ "
        "này, có thể bù các biến thiên của quá trình bằng cách thay đổi các tham số đặt của bộ điều "
        "khiển khi có những thay đổi trong các biến phụ. Hình 14-2 minh hoạ khái niệm này."))
    b.append(fig(2, F.fig_14_2()))

    b.append(h3("14.3.1 Ưu điểm của lịch trình độ lợi", "Gain Scheduling Advantages"))
    b.append(p(
        "Ưu điểm chính là các tham số có thể được thay đổi khá nhanh để đáp lại những thay đổi trong "
        "động học của nhà máy. Phương pháp này thuận tiện nếu động học của nhà máy đơn giản và đã biết "
        "rõ."))

    b.append(h3("14.3.2 Nhược điểm của lịch trình độ lợi", "Gain Scheduling Disadvantages"))
    b.append(p(
        "Nhược điểm là lịch trình độ lợi là một dạng thích nghi HỞ, không có khả năng học hay trí tuệ "
        "thực sự. Phạm vi và các tiêu chí thiết kế cũng có thể rất lớn. Việc chọn điểm đo phụ phải được "
        "làm với rất nhiều hiểu biết và suy nghĩ về vận hành quá trình."))
    b.append(p(
        "Nói cách khác: lịch trình độ lợi không biết nó có đúng hay không. Nó tra bảng theo một biến "
        "đo được và tin rằng bảng ấy còn đúng. Nếu nhà máy thay đổi — bộ trao đổi nhiệt bị bẩn, xúc tác "
        "già đi — thì bảng vẫn tra như cũ và sai một cách im lặng."))

    b.append(h2("14.4 Yêu cầu triển khai cho bộ tự chỉnh định",
                "Implementation Requirements for Self Tuning Controllers"))
    b.append(p(
        "Những bộ tự chỉnh định cố ý đưa nhiễu đã biết vào hệ để đo tác động từ một nguyên nhân đã biết "
        "thì không được ưa chuộng. Người ta thích những bộ tự chỉnh định ngồi ở phía sau, đo và đánh "
        "giá xem bộ điều khiển đang làm gì. Sau đó so sánh điều đó với tác động nó đang gây ra trên quá "
        "trình, rồi ra quyết định trên cơ sở các tham số đo được ấy, và cập nhật các biến vận hành của "
        "bộ điều khiển."))
    b.append(p(
        "Để làm được điều này, các thuật toán cập nhật thường được giữ ngủ yên cho tới khi số hạng sai "
        "số do bộ điều khiển của hệ sinh ra trở nên cao không chấp nhận được (lớn hơn 1 %); đến lúc đó "
        "các thuật toán hiệu chỉnh mới được thả ra cho hệ điều khiển, và hành động hiệu chỉnh mới bắt "
        "đầu."))
    b.append(p(
        "Sau khi sai số đã hình thành, thuật toán tự chỉnh định có thể kiểm tra đáp ứng của bộ điều "
        "khiển qua ba đại lượng: chu kỳ dao động, mức tắt dần và độ vọt lố. Hình 14-3 minh hoạ các "
        "tham số này."))
    b.append(fig(3, F.fig_14_3()))
    b.append(p(
        "Ngưỡng 1 % ở trên đáng để dừng lại một chút. Nó không phải một con số kỹ thuật mà là một quyết "
        "định thiết kế: dưới 1 %, việc chỉnh lại tham số có thể làm quá trình tệ đi nhiều hơn là tốt "
        "lên, vì bản thân phép đo đã có sai số cỡ đó. Chỉ khi sai số vượt ngưỡng ấy thì mới chắc chắn "
        "rằng có cái gì thật sự đáng sửa."))

    b.append(h2("14.5 Điều khiển quá trình bằng thống kê (SPC)",
                "Statistical Process Control"))
    b.append(p(
        "Mục tiêu cuối cùng của một hệ điều khiển quá trình là giữ cho sản phẩm — kết quả cuối cùng do "
        "quá trình tạo ra — luôn nằm trong mọi giới hạn đã định trước do mô tả sản phẩm đặt ra."))
    b.append(p(
        "Trong thế giới kỹ thuật thực tế có gần như vô số phương pháp và cách tiếp cận hệ thống để giúp "
        "đạt được điều đó. Tuy nhiên, dù mọi công cụ ấy đều tồn tại, vẫn cần có những thủ tục phân tích "
        "hiệu năng của quá trình, so sánh nó với chất lượng sản phẩm và cho ra những kết quả vừa "
        "“hiểu được” đối với mọi người tham gia quản lý quá trình, vừa chính xác và có ý nghĩa. Có một "
        "vài thuật ngữ và khái niệm cần hiểu để quản lý được một khái niệm cơ bản và dùng được về chất "
        "lượng điều khiển; và một khi đã hiểu chúng, thế giới của điều khiển quá trình bằng thống kê — "
        "SPC — trở nên rõ ràng, có ý nghĩa và dùng được như một công cụ mạnh để giữ một hệ điều khiển "
        "quá trình trong trạng thái kiểm soát được về mặt kinh tế và vận hành."))

    b.append(h3("14.5.1 Sản phẩm đồng nhất", "Uniform Product"))
    b.append(p(
        "Chỉ bằng cách hiểu quá trình với mọi biến thiên và tính khí của nó, với nhiễu sản phẩm, những "
        "trục trặc và cả “cá tính” riêng của nó, ta mới có thể hy vọng đạt được trạng thái sản phẩm gần "
        "như đồng nhất. Không có hai nhà máy hay hệ thống “giống hệt nhau” nào lại cho ra sản phẩm giống "
        "hệt nhau — tương tự thì có, nhưng không bao giờ giống hệt. Đây chính là chỗ SPC giúp nhận ra "
        "những khác biệt “giống hệt” ấy."))
    b.append(p(
        "Tiến sĩ Shewhart, làm việc tại Phòng thí nghiệm Bell vào đầu những năm 1920, sau khi so sánh "
        "những biến thiên trong tự nhiên với những sản phẩm được tạo ra trong các hệ quá trình, đã phát "
        "hiện những điểm không nhất quán và đưa ra phát biểu sau:"))
    b.append(quote(
        "Mọi quá trình đều có biến thiên; một số quá trình có biến thiên được kiểm soát, số khác có "
        "biến thiên không được kiểm soát.",
        "W. A. Shewhart, Phòng thí nghiệm Bell, đầu những năm 1920"))

    b.append(h4("Biến thiên được kiểm soát"))
    b.append(p(
        "Đặc trưng của nó là một mẫu hình biến thiên ổn định và nhất quán theo thời gian, quy được về "
        "những nguyên nhân “ngẫu nhiên”. Xét một sản phẩm có một kích thước hay đặc tính đo được (cơ "
        "học hoặc hoá học). Người ta lấy mẫu trong quá trình sản xuất. Kết quả kiểm tra những sản phẩm "
        "này cho thấy các phương sai do máy móc, vật liệu, người vận hành và phương pháp cùng tác động "
        "lẫn nhau tạo ra. Những biến thiên ấy nhất quán theo thời gian vì chúng do nhiều nhân tố góp "
        "phần gây ra. Những nguyên nhân ngẫu nhiên này tạo ra “biến thiên được kiểm soát”."))

    b.append(h4("Biến thiên không được kiểm soát"))
    b.append(p(
        "Loại này do những nguyên nhân gán được gây ra, tạo thành một mẫu hình biến thiên theo thời "
        "gian. Ngoài những thay đổi do nguyên nhân ngẫu nhiên, còn tồn tại những nhân tố đặc biệt có "
        "thể gây tác động lớn lên phép đo sản phẩm; chúng có thể do máy móc chỉnh sai, vật liệu khác "
        "đi, phương pháp thay đổi và cả môi trường thay đổi. Những nhân tố gán được này có thể đủ lớn để "
        "tạo ra những thay đổi rõ rệt trong những mẫu hình biến thiên đã biết và đã hiểu."))

    b.append(h2("14.6 Hai cách cải tiến một quá trình sản xuất",
                "Two Ways to Improve a Production Process"))
    b.append(p(
        "Hai phương pháp được mô tả ở đây để cải tiến một quá trình là khác nhau về bản chất: một cách "
        "tìm sự thay đổi cho một quá trình đang nhất quán, cách kia tìm những sửa đổi chính quá trình."))

    b.append(h3("14.6.1 Bài toán biến thiên được kiểm soát", "Controlled Variations Problem"))
    b.append(p(
        "Khi một quá trình có biến thiên được kiểm soát, nó nên được coi là ổn định và nhất quán. Các "
        "biến thiên là do những nhân tố nằm sẵn trong chính quá trình. Muốn giảm những biến thiên này "
        "thì phải THAY ĐỔI QUÁ TRÌNH."))

    b.append(h3("14.6.2 Bài toán biến thiên không được kiểm soát", "Uncontrolled Variations Problem"))
    b.append(p(
        "Điều này có nghĩa quá trình đang thay đổi theo thời gian. Nó vừa không nhất quán vừa không ổn "
        "định. Giải pháp là nhận ra và loại bỏ (các) nguyên nhân của (các) vấn đề."))
    b.append(p(
        "Đây là phân biệt quan trọng nhất của cả chương, và nó là chỗ người ta hay hành động sai nhất. "
        "Khi một quá trình đang chạy tốt mà sản phẩm vẫn lệch, người ta thường đi chỉnh bộ điều khiển — "
        "nhưng bộ điều khiển không phải nguyên nhân, và chỉnh nó chỉ làm quá trình dao động thêm. Ngược "
        "lại, khi có một nguyên nhân gán được, người ta lại đi đổi quy trình sản xuất — trong khi chỉ "
        "cần siết lại một con ốc."))

    b.append(h2("14.7 Lấy thông tin cần thiết cho SPC", "Obtaining the Information required for SPC"))
    b.append(p(
        "Về cơ bản chỉ có một cách ghi lại hiệu năng thực của quá trình: dùng một BĂNG GHI biểu diễn tín "
        "hiệu biến quá trình, và nếu có thể thì cả tín hiệu đầu ra bộ điều khiển. Nghĩa là, những mệnh "
        "lệnh gửi vào quá trình, và câu trả lời của quá trình cho những mệnh lệnh ấy, cả về độ lớn lẫn "
        "thời gian."))

    b.append(h3("14.7.1 Suy luận thống kê", "Statistical Inference"))
    b.append(p(
        "Trung bình của 2, 4, 6 và 8 là 5 — đây là điểm cân bằng của mẫu dữ liệu này. Khoảng biến thiên "
        "của mẫu này là 6, tức là 2 và 8 cách nhau bao xa (giá trị cực tiểu và cực đại). Tuy nhiên, suy "
        "luận thống kê dựa trên một thực tế: tồn tại một tổng thể khái niệm, và cần có nó để hợp lý hoá "
        "mọi nỗ lực dự báo, và rằng mọi mẫu đã lấy đều đến từ tổng thể này — cần có điều đó để tin vào "
        "các ước lượng dựa trên thống kê mẫu."))
    b.append(p(
        "Để đơn giản và rõ ràng, ta sẽ coi rằng mọi mẫu đều khách quan và đại diện cho một tổng thể khái "
        "niệm. Nếu điều này không đúng thì kết quả có thể rất không nhất quán và các thống kê sẽ thất "
        "thường. Thực tế, nếu điều đó xảy ra, có thể coi quá trình là “tâm thần phân liệt”, tức là quá "
        "trình đang có biến thiên không được kiểm soát. Các thống kê thu được đơn giản là không thể "
        "khái quát hoá được."))

    b.append(h3("14.7.2 Dùng nhóm con để theo dõi quá trình", "Using Subgroups to Monitor the Process"))
    b.append(p(
        "Mỗi mẫu thu được tại một thời điểm là một nhóm con, và mỗi nhóm được xử lý như một mẫu riêng. "
        "Hình 14-4 cho thấy bốn nhóm con chọn từ một quá trình ổn định, mỗi giờ một nhóm. Những đường "
        "cong hình chuông biểu diễn toàn bộ đầu ra của quá trình trong mỗi giờ, các chấm biểu diễn những "
        "giá trị đo được trong mỗi nhóm."))
    b.append(fig(4, F.fig_14_4()))

    b.append(h3("14.7.3 Ghi trung bình và khoảng biến thiên của một quá trình ổn định",
                "Recording Averages and Ranges for a Stable Process"))
    b.append(p(
        "Bước tiếp theo là ghi trung bình và khoảng biến thiên lên một băng ghi theo trục thời gian, như "
        "thấy ở Hình 14-5. Chừng nào các điểm này còn di chuyển trong các giới hạn trên và dưới đã định "
        "và cũng được hiển thị trên biểu đồ, ta có thể coi rằng mọi nhóm con đều xuất phát từ cùng một "
        "tổng thể khái niệm."))
    b.append(fig(5, F.fig_14_5()))

    b.append(h3("14.7.4 Ghi trung bình và khoảng biến thiên của một quá trình không ổn định",
                "Recording Averages and Ranges for an Unstable Process"))
    b.append(p(
        "Nếu bây giờ ta xét cùng ví dụ ấy nhưng bản thân quá trình đang thay đổi theo từng giờ, ta để "
        "các đường cong hình chuông ở Hình 14-6 biểu diễn đầu ra của quá trình trong mỗi giờ."))
    b.append(fig(6, F.fig_14_6()))
    b.append(p(
        "Lúc 09:00, trung bình của quá trình tăng, đẩy trung bình nhóm lên trên giới hạn trên. Lúc "
        "10:00, trung bình của quá trình giảm mạnh, và nhóm con rơi xuống dưới giới hạn dưới. Trong ba "
        "giờ đầu, từ 08:00 đến 11:00, độ tán xạ của quá trình KHÔNG thay đổi và khoảng biến thiên của "
        "mọi nhóm con đều nằm trong giới hạn kiểm soát… NHƯNG đến 11:00, độ tán xạ của quá trình tăng "
        "và trung bình của quá trình quay về giá trị ban đầu. Nhóm con thu được trong giờ này có KHOẢNG "
        "BIẾN THIÊN nằm trên giới hạn kiểm soát trên, và TRUNG BÌNH nằm trong giới hạn kiểm soát."))
    b.append(fig(7, F.fig_14_7()))
    b.append(p(
        "Có thể thấy rằng nhờ dùng các nhóm con theo chu kỳ, hai biến bổ sung đã được đưa vào: trung "
        "bình nhóm và khoảng biến thiên nhóm. Đây là hai biến được dùng để theo dõi quá trình."))
    b.append(p(
        "Ví dụ sau minh hoạ hành vi của hai biến này và cách chúng liên hệ với các giá trị đo khi quá "
        "trình ổn định. Xem bảng 14-1 và hình 14-7."))

    b.append(h3("14.7.5 Ví dụ về một quá trình ổn định", "Example of a Stable Process"))
    b.append(p(
        "Số liệu trong ví dụ này lấy từ một quá trình ổn định. Các giá trị đo biểu diễn độ dày của một "
        "sản phẩm. Các con số cho biết chi tiết vượt quá 0,300 inch bao nhiêu, tính theo đơn vị 0,001."))
    b.append(table(
        ["Nhóm", "M1", "M2", "M3", "M4", "Trung bình", "R"],
        [[str(i + 1)] + [str(v) for v in r] + ["%.2f" % F.AVGS[i], str(F.RNGS[i])]
         for i, r in enumerate(F.DATA)],
        "Bảng 14-1. Số liệu cho hình 14-7 và 14-8 (bảng 14.1 của bản gốc)."))
    b.append(p(
        "Các biểu đồ tần suất ở Hình 14-8 đều cùng tỉ lệ trên cả hai trục. Tuy nhiên cả ba biểu diễn "
        "những hình dạng và độ tán xạ hoàn toàn khác nhau. Vì vậy việc phân biệt ba đại lượng này là "
        "thiết yếu."))
    b.append(fig(8, F.fig_14_8()))

    b.append(h3("14.7.6 Phân bố của giá trị đo, trung bình và khoảng biến thiên",
                "Distributions of Measurements, Averages and Ranges"))
    b.append(p(
        "Tuy các giá trị đo, trung bình và khoảng biến thiên có những phân bố khác nhau, chúng liên hệ "
        "với nhau theo những cách nhất định khi đều xuất phát từ một quá trình ổn định. Hình 14-9 cho "
        "thấy những quan hệ này rõ hơn."))
    b.append(fig(9, F.fig_14_9()))
    b.append(p("Các ký hiệu liên quan tới Hình 14-9:"))
    b.append(ul([
        "Gọi AVER(X) là trung bình của phân bố các giá trị X.",
        "Gọi SD(X) là độ lệch chuẩn của phân bố X.",
        "Tương tự, AVER(x̄) và SD(x̄) là trung bình và độ lệch chuẩn của phân bố các trung bình nhóm; "
        "còn AVER(R) và SD(R) là của các khoảng biến thiên."]))
    b.append(p("Với các ký hiệu này, quan hệ giữa các trung bình và độ lệch chuẩn có thể viết là:"))
    b.append(eq("AVER(x̄) = AVER(X)", "14.1"))
    b.append(eq("SD(x̄) = SD(X) / √n", "14.2"))
    b.append(eq("AVER(R) = d<sub>2</sub> · SD(X)", "14.3"))
    b.append(eq("SD(R) = d<sub>3</sub> · SD(X)", "14.4"))
    b.append(p(
        "Các hằng số d<sub>2</sub> và d<sub>3</sub> là những hệ số tỉ lệ phụ thuộc vào cỡ nhóm con n. "
        "Các hệ số này được cho ở bảng 14-2 dưới đây và dựa trên giả thiết X có phân bố chuẩn."))
    b.append(table(["Cỡ nhóm n", "d<sub>2</sub>", "d<sub>3</sub>"],
                   [[a, b_, c] for a, b_, c in _D2],
                   "Bảng 14-2. Hệ số cho trung bình và độ lệch chuẩn của phân bố khoảng biến thiên."))

    b.append(h2("14.8 Tính các giới hạn kiểm soát", "Calculating Control Limits"))
    b.append(p(
        "Từ bốn quan hệ vừa nêu ở trên, có thể thu được các giới hạn kiểm soát cho trung bình nhóm và "
        "khoảng biến thiên nhóm."))
    b.append(p(
        "Có hai phương pháp chính để tính giới hạn kiểm soát: một là cách tiếp cận cấu trúc, hai là "
        "dùng công thức. Cả hai phương pháp được minh hoạ dưới đây."))
    b.append(p(
        "Khi lần đầu lập giới hạn kiểm soát, thông lệ là thu từ hai mươi đến ba mươi nhóm con trước khi "
        "tính giới hạn. Dùng nhiều nhóm con giúp giảm nhỏ tác động của một giá trị cực đoan."))
    b.append(p(
        "Dùng ví dụ ở mục 14.7.5 về trung bình nhóm và khoảng biến thiên của một quá trình đang được "
        "kiểm soát, hai mục tiếp theo minh hoạ cách tiếp cận cấu trúc và cách tiếp cận công thức trong "
        "việc tính các giới hạn kiểm soát quá trình."))
    b.append(table(["Cỡ nhóm n", "A<sub>2</sub>", "D<sub>3</sub>", "D<sub>4</sub>"],
                   [[a, b_, c, d] for a, b_, c, d in _A2],
                   "Bảng 14-3. Các hệ số dùng để tính giới hạn kiểm soát cho ví dụ 14.7.5."))
    b.append(p(
        "Dùng số liệu ở bảng 14-3, các giới hạn kiểm soát như trên hình 14-10 sẽ được tìm ra bằng cả "
        "hai cách tiếp cận cấu trúc và công thức."))

    b.append(h3("14.8.1 Cách tiếp cận cấu trúc", "The Structural Approach"))
    b.append(p("<b>1.</b> Trước hết ta ước lượng phân bố của các giá trị X:"))
    b.append(ul([
        "Trung bình lớn X̄ = 4,763 ước lượng AVER(X);",
        "Khoảng biến thiên trung bình R̄ = 4,05;",
        "nên ước lượng của SD(X) là R̄ / d<sub>2</sub> = 4,05 / 2,059 = 1,967."]))
    b.append(p("<b>2.</b> Ước lượng phân bố của các giá trị X̄:"))
    b.append(ul([
        "Trung bình lớn X̄ = 4,763 ước lượng AVER(X);",
        "ước lượng của SD(X̄) là R̄ / (d<sub>2</sub>√n) = 1,967 / 2 = 0,984."]))
    b.append(p("<b>3.</b> Giới hạn kiểm soát cho trung bình nhóm là:"))
    b.append(eq("4,763 ± 3(0,984) = 1,811 ÷ 7,715", ""))
    b.append(p("<b>4.</b> Ước lượng phân bố của các giá trị R:"))
    b.append(ul([
        "Khoảng biến thiên trung bình R̄ = 4,05 ước lượng AVER(R);",
        "ước lượng của SD(R) là (d<sub>3</sub> × R̄) / d<sub>2</sub> = (0,88 × 4,05) / 2,059 = 1,731."]))
    b.append(p("<b>5.</b> Giới hạn kiểm soát cho khoảng biến thiên nhóm là:"))
    b.append(eq("4,05 ± 3(1,731) = −1,143 ÷ 9,243", ""))
    b.append(p(
        "Vì khoảng biến thiên nhóm không thể âm, giới hạn dưới âm là vô nghĩa. Trong trường hợp này "
        "giới hạn kiểm soát dưới bằng 0."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Bản PDF gốc in giới hạn trên của khoảng biến thiên "
        "là “9.423”. Con số đúng là 9,243: cộng 4,05 với 3 × 1,731 được 9,243, và công thức D<sub>4</sub>"
        "·R̄ = 2,282 × 4,05 cũng cho 9,242. Bản gốc đã đảo hai chữ số. Ngoài ra bản gốc đánh số mục ví "
        "dụ là “14.8.5” dù nó nằm giữa 14.7.4 và 14.7.6, và sau đó dẫn chiếu lại đúng bằng số ấy; bản "
        "dịch đánh số lại thành 14.7.5 cho liền mạch và đã sửa các chỗ dẫn chiếu tương ứng. Cuối cùng, "
        "bản gốc gọi hình minh hoạ lô-gic biểu đồ kiểm soát là “figure 14.10” trong phần chữ nhưng lại "
        "đặt chú thích “Figure 14.11”; bản dịch theo đúng chú thích hình."))

    b.append(h3("14.8.2 Cách tiếp cận công thức", "The Formulated Approach"))
    b.append(p(
        "Trung bình lớn là 4,763. Khoảng biến thiên trung bình là 4,05. Cỡ nhóm con là 4. Tra bảng "
        "14-3 với n = 4 ta được A<sub>2</sub> = 0,729, D<sub>3</sub> = 0 và D<sub>4</sub> = 2,282. Do "
        "đó:"))
    b.append(eq("X̄ ± A<sub>2</sub>·R̄ = 4,763 ± 0,729 × 4,05 = 1,811 ÷ 7,715", "14.5"))
    b.append(eq("D<sub>3</sub>·R̄ = 0   và   D<sub>4</sub>·R̄ = 2,282 × 4,05 = 9,242", "14.6"))
    b.append(p(
        "Hai cách cho cùng một kết quả, và đó là điều đáng chú ý: cách cấu trúc đi vòng qua độ lệch "
        "chuẩn ước lượng, cách công thức đi thẳng. Chúng gặp nhau vì các hằng số A<sub>2</sub>, "
        "D<sub>3</sub>, D<sub>4</sub> được lập ra chính từ d<sub>2</sub> và d<sub>3</sub>."))
    b.append(fig(10, F.fig_14_10()))

    b.append(h2("14.9 Lô-gic đằng sau các biểu đồ kiểm soát", "The Logic Behind Control Charts"))
    b.append(p(
        "Để kết luận, cho cả chương này và cho cả buổi thực hành, hình 14-11 minh hoạ lô-gic đằng sau "
        "các biểu đồ kiểm soát."))
    b.append(fig(11, F.fig_14_11()))
    b.append(p(
        "Cần nhấn mạnh điều mà sơ đồ ấy nói bằng hình: hai nhánh của nó dẫn tới hai hành động khác nhau "
        "về bản chất, và không thể thay thế nhau. Một điểm nằm trong giới hạn không có nghĩa là quá "
        "trình tốt — nó chỉ có nghĩa là quá trình đang làm đúng những gì nó vẫn làm. Nếu sản phẩm vẫn "
        "không đạt, vấn đề nằm ở thiết kế quá trình chứ không nằm ở người vận hành."))
    b.append(p(
        "Ngược lại, một điểm nằm ngoài giới hạn là một lời mời đi tìm nguyên nhân cụ thể. Và nguyên nhân "
        "ấy, trong đa số trường hợp thực tế, không phải bộ điều khiển."))

    b.append(h2("Khép lại cuốn sách", "Closing the Book"))
    b.append(p(
        "Mười bốn chương vừa đi qua một vòng tròn. Chương 2 nói về cảm biến — làm sao biết được quá "
        "trình đang ở đâu. Chương 3 nói về van — làm sao tác động được lên nó. Rồi từ chương 4 tới "
        "chương 12 là toàn bộ phần lý thuyết điều khiển: ổn định, các mode, PID, chỉnh định, vòng ghép, "
        "điều khiển theo hướng và thời gian chết. Chương 13 và 14 đưa ra những công cụ cho những bài "
        "toán mà lý thuyết ấy không với tới."))
    b.append(p(
        "Điều đáng giữ lại sau tất cả không phải là bộ công thức — chúng nằm sẵn trong mọi bộ điều "
        "khiển bán trên thị trường. Mà là một thói quen: trước khi chỉnh bất cứ thứ gì, hãy xác định "
        "quá trình đang có vấn đề ở đâu. Van kẹt, cảm biến trôi, thời gian chết dài, hay đơn giản là "
        "quá trình vốn đã dao động như thế và không có gì hỏng cả. Một kỹ sư giỏi khác một người biết "
        "vặn núm ở chỗ ấy."))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Thirteen chapters have taught how to choose and tune a controller. This last one asks a "
        "different question: what if the controller tuned itself, and how would you know whether the "
        "whole loop is doing well?"))
    b.append(p(
        "The two questions sound unrelated but they are two halves of one problem. Self-tuning belongs "
        "to the controller: it measures the process response and corrects its own parameters. SPC "
        "belongs to whoever owns the process: it looks at the run of product and says whether the "
        "process is still stable or has drifted. The first asks “how much should I adjust”; the second "
        "asks “is adjusting even the right response”. And SPC's answer is often: no, the problem is not "
        "in the controller."))

    b.append(h2("Self-tuning is a slow outer loop, and that is the whole trick", "§ 14.2"))
    b.append(fig(1, F.fig_14_1(), "en"))
    b.append(p(
        "Figure 14-1 shows the structure and it is worth reading as two loops running at two speeds. The "
        "inner loop is the ordinary control loop. The outer loop watches the MV and the PV, identifies "
        "the process, and writes new parameters back into the controller."))
    b.append(p(
        "The speeds must differ by orders of magnitude, and the chapter does not say so explicitly. The "
        "inner loop runs in seconds. The outer loop has to observe several oscillations before it can "
        "conclude anything about period or damping, so it runs in minutes or hours. If the outer loop "
        "ran at anything like the inner loop's rate, it would be chasing the oscillations it had just "
        "created — a feedback loop around a feedback loop, with the same stability question one level "
        "up."))
    b.append(p(
        "Section 14.4's threshold is the practical expression of the same idea. The updating algorithms "
        "stay dormant until the error exceeds about 1 per cent. That is not a technical constant; it is "
        "a judgement that below 1 per cent the measurement noise is the same size as the correction, so "
        "adjusting makes the process worse more often than better."))

    b.append(h2("Gain scheduling: open-loop adaptation, and honest about it", "§ 14.3"))
    b.append(fig(2, F.fig_14_2(), "en"))
    b.append(p(
        "Figure 14-2 draws gain scheduling as what it actually is: a table of gains indexed by a "
        "measured auxiliary variable, approximating a continuous requirement with a staircase. The "
        "approximation error between breakpoints is the price; the absence of any model or learning is "
        "the benefit."))
    b.append(p(
        "The chapter is unusually candid about the weakness — it calls it “an OPEN LOOP adaptation with "
        "no real learning or intelligence”. That is exactly right, and it is worth spelling out what it "
        "means in practice: the schedule does not know whether it is still correct. It looks up a table "
        "and trusts the table. When the plant changes underneath it — a fouled exchanger, a deactivated "
        "catalyst — the table is consulted as before and is silently wrong."))
    b.append(p(
        "That is not an argument against gain scheduling. It is the most robust of the adaptive methods "
        "precisely because it has no feedback to go unstable. It is an argument for scheduling against "
        "a variable that tracks the actual change in dynamics, and for reviewing the table when the "
        "plant is modified."))

    b.append(h2("The three numbers a self-tuner reads off the response", "§ 14.4"))
    b.append(fig(3, F.fig_14_3(), "en"))
    b.append(p(
        "Figure 14-3 names them: overshoot, period of oscillation, and damping — the ratio of successive "
        "peaks. Three numbers, three unknowns. Overshoot and damping together fix the closed-loop "
        "damping ratio; period fixes the natural frequency; from those two the gain and the integral "
        "time follow. It is the Ziegler–Nichols idea generalised: instead of driving the loop to "
        "sustained oscillation and measuring the ultimate gain, the self-tuner reads the same "
        "information off an ordinary transient."))

    b.append(h2("Shewhart's distinction is the most useful idea in the chapter", "§ 14.5–14.6"))
    b.append(p(
        "Every process varies; some vary in a controlled way and some do not. That sentence, from "
        "Shewhart at Bell Labs in the early 1920s, is the foundation of everything that follows, and it "
        "is a distinction about <em>causes</em>, not about sizes."))
    b.append(p(
        "Controlled variation comes from many small causes acting together — machine, material, "
        "operator, method — each too small to identify. It is stable because it is the sum of many "
        "independent contributions, and its shape is therefore predictable even though no individual "
        "value is. Uncontrolled variation comes from an assignable cause: a specific, findable thing "
        "that has changed."))
    b.append(p(
        "The two demand opposite responses, and getting them the wrong way round is the most common "
        "error in process plants. Faced with controlled variation and a product that is off target, "
        "people adjust the controller — which is not the cause, and adjusting it only adds variation. "
        "Faced with an assignable cause, people redesign the procedure — when tightening one bolt would "
        "have done."))
    b.append(quote(
        "Every process displays variation; some processes display controlled variation, others display "
        "uncontrolled variation.",
        "W. A. Shewhart, Bell Laboratories, early 1920s"))

    b.append(h2("Two variables, because mean and spread move independently", "§ 14.7"))
    b.append(fig(4, F.fig_14_4(), "en"))
    b.append(fig(6, F.fig_14_6(), "en"))
    b.append(p(
        "Figures 14-4 and 14-6 are the same four hours seen twice: once for a stable process, where the "
        "four bells sit on top of each other, and once for a moving one, where they shift right, then "
        "left, then widen. The widening is the important case, because it is invisible in the average."))
    b.append(fig(5, F.fig_14_5(), "en"))
    b.append(fig(7, F.fig_14_7(), "en"))
    b.append(p(
        "Figures 14-5 and 14-7 are the corresponding charts. Figure 14-7 is the one that earns the "
        "method: at 09:00 the average breaks the upper limit, at 10:00 it breaks the lower, and at "
        "11:00 the average returns to normal while the range breaks its own upper limit. For the first "
        "three hours the spread never moved. An operator watching only the range — or only the product, "
        "which averages the two — would have missed two excursions entirely."))
    b.append(p(
        "That is the argument for plotting both variables rather than one, and it is worth stating "
        "plainly because it is the reason the chapter introduces subgroups at all. A subgroup of n gives "
        "you two numbers per sample instead of one, and they answer different questions: where is the "
        "process, and how consistent is it."))

    b.append(h2("Why the average chart is more sensitive than the product", "§ 14.7.6"))
    b.append(fig(9, F.fig_14_9(), "en"))
    b.append(p(
        "Figure 14-9 contains the statistical reason the method works, and it is one line of algebra: "
        "SD(x̄) = SD(X)/√n. The average of four measurements varies half as much as a single "
        "measurement; the average of nine, a third as much. Plotting averages therefore compresses the "
        "random noise by √n while leaving a genuine shift in the mean untouched — which is why a shift "
        "that is invisible in the individual readings stands out on the chart."))
    b.append(eq("SD(x̄) = SD(X) / √n", "14.2"))
    b.append(p(
        "The range distribution behaves differently: it is skewed, not normal, which is why it is "
        "converted through d<sub>2</sub> and d<sub>3</sub> rather than used directly. Figure 14-8 shows "
        "all three histograms from the chapter's own data table, drawn to the same scale — the "
        "measurements wide and flat, the averages narrow and tall, the ranges skewed hard right."))
    b.append(fig(8, F.fig_14_8(), "en"))

    b.append(h2("Two routes to the same limits, and why they agree", "§ 14.8"))
    b.append(p(
        "The chapter computes the limits twice — once structurally, through the estimated standard "
        "deviation, and once by formula, through A<sub>2</sub>, D<sub>3</sub> and D<sub>4</sub>. Both "
        "give 1.811 to 7.715 for the averages and 0 to about 9.24 for the ranges. They must agree, "
        "because the tabulated constants were derived from d<sub>2</sub> and d<sub>3</sub> in the first "
        "place: A<sub>2</sub> = 3/(d<sub>2</sub>√n), D<sub>4</sub> = 1 + 3d<sub>3</sub>/d<sub>2</sub>."))
    b.append(eq("X̄ ± A<sub>2</sub>·R̄ = 4.763 ± 0.729 × 4.05 = 1.811 to 7.715", "14.5"))
    b.append(fig(10, F.fig_14_10(), "en"))
    b.append(p(
        "Figure 14-10 is that calculation applied to the chapter's own twenty subgroups. All twenty "
        "averages fall between the limits and all twenty ranges fall below the upper one, so the process "
        "is judged stable. Note the lower range limit is 0, not the −1.143 the arithmetic produces: a "
        "range cannot be negative, and a limit that cannot be reached is not a limit."))
    b.append(note(
        "<b>A note on the source.</b> The original prints the upper range limit as 9.423. The correct "
        "value is 9.243 — 4.05 + 3(1.731) — and D<sub>4</sub>·R̄ gives 9.242; two digits have been "
        "transposed. The original also numbers the worked example 14.8.5 while placing it between 14.7.4 "
        "and 14.7.6, then cross-refers to it by that number; this translation renumbers it 14.7.5 and "
        "updates the cross-references."))

    b.append(h2("What the chart is really telling you", "§ 14.9"))
    b.append(fig(11, F.fig_14_11(), "en"))
    b.append(p(
        "Figure 14-11 is the decision the chart supports, and the two branches are different in kind. "
        "Inside the limits means the process is doing what it always does — which is not the same as "
        "doing well. If the product is still off target, the problem is in the design of the process, "
        "and no amount of operator attention will fix it."))
    b.append(p(
        "Outside the limits means something specific has changed, and it can be found. That is a much "
        "more hopeful diagnosis, and a much cheaper one. The discipline SPC imposes is simply to ask "
        "which of the two situations you are in before touching anything."))

    b.append(h2("Closing the book"))
    b.append(p(
        "Fourteen chapters have gone round a full circle. Chapter 2 was sensors — how to know where the "
        "process is. Chapter 3 was valves — how to act on it. Chapters 4 to 12 were the theory: "
        "stability, control modes, PID, tuning, cascade, feedforward, dead time. Chapters 13 and 14 "
        "supplied tools for the problems that theory does not reach."))
    b.append(p(
        "What is worth keeping is not the formulas — every controller on the market already contains "
        "them. It is a habit: before adjusting anything, establish where the process is actually wrong. "
        "A sticking valve, a drifting transmitter, a long dead time, or simply a process that was always "
        "this variable and is not broken at all. That is the difference between an engineer and someone "
        "who knows which knob to turn."))
    return "".join(b)
