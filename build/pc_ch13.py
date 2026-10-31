# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 13, Basic Principles of Fuzzy Logic and
Neural Networks (Wolfgang Altmann, IDC Technologies)."""
import pc13fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 17
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Tập hợp chuẩn (crisp set)</em> — một phần tử hoặc thuộc hoặc không thuộc, không có "
            "vùng giữa. · "
            "<em>Tập hợp mờ (fuzzy set)</em> — một phần tử thuộc ở một mức độ nào đó, có thể thuộc "
            "nhiều tập cùng lúc. · "
            "<em>Độ phụ thuộc μ</em> — con số từ 0 đến 1 nói phần tử thuộc tập ở mức nào. · "
            "<em>Mảng mờ (fuzzy patch)</em> — vùng trong mặt phẳng vào–ra mà một luật bao phủ. · "
            "<em>Giải mờ (defuzzification)</em> — biến đường cong đầu ra mờ thành một con số duy nhất. · "
            "<em>Nơ-ron</em> — phần tử tính một tổng có trọng số rồi bẻ cong kết quả. · "
            "<em>Lan truyền ngược (back-propagation)</em> — sửa trọng số theo hướng làm giảm sai số.")
    return note(
        "<b>Key terms.</b> <em>Crisp set</em> — an element either belongs or does not; there is no middle "
        "ground. · <em>Fuzzy set</em> — an element belongs to some degree, and may belong to several sets "
        "at once. · <em>Membership μ</em> — the number from 0 to 1 saying how far an element belongs. · "
        "<em>Fuzzy patch</em> — the region of the input–output plane a rule covers. · "
        "<em>Defuzzification</em> — turning the fuzzy output curve into one number. · <em>Neuron</em> — "
        "the element that forms a weighted sum and bends the result. · <em>Back-propagation</em> — "
        "adjusting the weights in the direction that reduces the error.")


# ---------------------------------------------------------------- Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Cho tới đây, mọi chương của cuốn sách đều đứng trên một giả định ngầm: người thiết kế viết được "
        "phương trình của quá trình. Một hàm truyền, một thời hằng, một thời gian chết — rồi từ đó suy "
        "ra bộ điều khiển. Chương 12 còn đi xa hơn một bước: dựng hẳn một mô hình song song bên cạnh quá "
        "trình thật để bù thời gian chết."))
    b.append(p(
        "Nhưng có những quá trình không cho ta phương trình ấy — không phải vì ta lười, mà vì nó không "
        "tồn tại. Một lò nung clinker, một tháp chưng cất mười hai mâm, một dây chuyền mà nguyên liệu "
        "đổi theo từng mẻ: không ai viết được hàm truyền cho chúng, và nếu có viết thì các hệ số cũng "
        "trôi đi sau vài tuần vận hành."))
    b.append(p(
        "Chương này giới thiệu hai lối thoát, và chúng khác nhau về bản chất. Lô-gic mờ thay phương trình "
        "bằng lời: người vận hành giỏi luôn biết phải làm gì, chỉ là họ không viết được điều đó thành "
        "công thức — lô-gic mờ là cách phát biểu lại những câu “nếu … thì …” ấy cho máy hiểu được. Mạng "
        "nơ-ron thì không cần cả lời: nó tự rút ra quy luật từ dữ liệu, và cái nó học được nằm rải trong "
        "một tập trọng số mà không ai đọc được thành câu."))
    b.append(p(
        "Cả hai đều là công cụ thật, đã chạy trong công nghiệp hàng chục năm. Cả hai cũng đều bị thổi "
        "phồng nhiều hơn mức cần thiết. Đọc chương này nên giữ cả hai thái cực ấy trong đầu."))

    b.append(h2("13.1 Mục tiêu", "Objectives"))
    b.append(p(
        "Chương này nhằm ôn lại các nguyên lý và mô tả cơ bản của mạng nơ-ron và lô-gic mờ."))
    b.append(p("Sau khi học chương này, học viên phải có khả năng:"))
    b.append(ul([
        "Mô tả được các nguyên lý cơ bản của lô-gic mờ;",
        "Mô tả được các từ viết tắt và thuật ngữ cơ bản dùng trong ứng dụng mạng nơ-ron và lô-gic mờ."]))

    b.append(h2("13.2 Giới thiệu về lô-gic mờ", "Introduction to Fuzzy Logic"))
    b.append(p(
        "Trong thế giới thực có rất nhiều tình trạng mơ hồ và không chính xác, chúng chống lại một câu "
        "phát biểu đơn giản kiểu “Đúng” hay “Sai” khi ta muốn mô tả trạng thái của chúng. Máy tính và "
        "lô-gic nhị phân của nó không có khả năng biểu diễn thoả đáng những trạng thái mơ hồ ấy — những "
        "trạng thái mà con người vẫn hiểu được. Lô-gic mờ là một nhánh của trí tuệ máy, giúp máy tính "
        "hiểu được những biến thiên xảy ra trong một thế giới bất định và rất mơ hồ mà ta đang sống."))
    b.append(p(
        "Lô-gic mờ “thao tác” trên những khái niệm mơ hồ như “ấm” hay “đang chạy nhanh”, theo cách giúp "
        "ta thiết kế được những thứ như máy điều hoà nhiệt độ hay hệ điều khiển tốc độ biết chuyển từ bộ "
        "tiêu chí điều khiển này sang bộ tiêu chí khác — kể cả khi lý do chuyển là “trời hơi nóng quá, "
        "hoặc chưa đủ nóng để chạy nhanh hơn, hay chậm lại một chút”. Tất cả những “mệnh lệnh” ấy đều "
        "hiển nhiên với ta, nhưng chúng rất xa thế giới số chỉ có 1 và 0."))
    b.append(p(
        "Những phát biểu ĐÚNG và SAI tuyệt đối về ý nghĩa của chúng đều xuất phát từ một điểm khởi đầu "
        "xác định và được thiết kế để kết thúc ở một đích đã biết."))
    b.append(p(
        "Không có mô hình toán học nào mô tả được hành động của một con tàu đi từ một điểm không xác định "
        "nào đó ngoài khơi vào vùng cầu cảng và cuối cùng dừng lại đúng một vị trí trên bến. Con người và "
        "lô-gic mờ làm được việc đó rất chính xác: nếu gió thổi mạnh hơn một chút, hay một con tàu khác "
        "cản trở một thao tác cập bến cụ thể, hệ thống cảm nhận được và đưa ra một hành động không liên "
        "quan trực tiếp nhưng hiệu quả. Hành động ấy khác nhau mỗi lần, vì nhiễu cũng khác nhau mỗi lần "
        "(những sự kiện tương tự nhưng không giống nhau xảy ra mỗi khi một con tàu thực hiện thủ tục "
        "này)."))
    b.append(p(
        "Khi các nhà toán học không có sẵn thuật toán cụ thể quy định hệ phải đáp ứng đầu vào ra sao, "
        "lô-gic mờ có thể được dùng để điều khiển hoặc mô tả hệ bằng những luật thông thường dựa trên các "
        "đại lượng không xác định."))
    b.append(p(
        "Ứng dụng của lô-gic mờ vượt xa khỏi hệ điều khiển; về nguyên tắc chúng mở rộng tới bất kỳ hệ "
        "liên tục nào, dù trong vật lý hay sinh học. Rất có thể các mô hình mờ còn hữu ích và chính xác "
        "hơn các mô hình toán học chuẩn."))

    b.append(h2("13.3 Lô-gic mờ là gì?", "What is Fuzzy Logic?"))
    b.append(p(
        "Trong lý thuyết tập hợp chuẩn, một đối tượng hoặc thuộc hoặc không thuộc một tập. “Không có vùng "
        "giữa.” Đây là một luật cổ của Hy Lạp do Aristotle đề ra — luật bài trung."))
    b.append(p(
        "Số NĂM thuộc trọn vẹn vào tập các số lẻ và hoàn toàn không thuộc tập các số chẵn. Trong những "
        "tập nhị nguyên như vậy, một đối tượng không thể vừa thuộc một tập vừa thuộc phần bù của nó, "
        "cũng không thể không thuộc cả hai. Nguyên lý này bảo toàn cấu trúc của lô-gic và ngăn một đối "
        "tượng vừa “là” vừa “không là” cùng một lúc."))
    b.append(p(
        "Những tập “mờ” hay đa trị phá vỡ luật “không có vùng giữa” ấy ở một mức độ nào đó. Các phần tử "
        "chỉ thuộc một phần vào một tập mờ, và chúng còn có thể thuộc nhiều hơn một tập. Biên của tập "
        "chuẩn là chính xác, còn biên của tập mờ thì cong hoặc thoải dần — chính điều này tạo ra những "
        "mâu thuẫn bộ phận. Nhiệt độ không khí có thể vừa là 20 % mát vừa là 80 % không mát cùng một "
        "lúc."))
    b.append(fig(1, F.fig_13_1()))

    b.append(h2("13.4 Lô-gic mờ làm được gì?", "What does Fuzzy Logic do?"))
    b.append(p(
        "Độ mờ KHÔNG giống với phần trăm xác suất. Xác suất đo việc một điều gì đó sẽ xảy ra hay không. "
        "Độ mờ đo mức độ mà một điều gì đó đang xảy ra, hay một điều kiện đang tồn tại."))
    b.append(p(
        "Đây là phân biệt quan trọng nhất trong cả chương, và cũng là chỗ hay bị hiểu nhầm nhất. Khi nói "
        "“70 % khả năng trời mưa”, ta nói về một sự kiện chưa xảy ra. Khi nói “không khí 70 % ấm”, ta "
        "không nói gì về tương lai — trạng thái ấy đã đang là như vậy, chỉ là ta mô tả nó bằng một mức độ "
        "thay vì bằng một ngưỡng."))

    b.append(h2("13.5 Các luật của lô-gic mờ", "The Rules of Fuzzy Logic"))
    b.append(p(
        "Ràng buộc thực sự duy nhất khi dùng lô-gic mờ là: với đối tượng đang xét, độ phụ thuộc của nó "
        "vào một nhóm và vào nhóm bù của nhóm ấy phải cộng lại bằng một."))
    b.append(eq("μ<sub>A</sub>(x) + μ<sub>Ā</sub>(x) = 1", "13.1"))
    b.append(p(
        "Nếu một thứ là 30 % mát thì nó phải là 70 % KHÔNG mát. Điều này cho phép lô-gic mờ tránh mâu "
        "thuẫn nhị nguyên kiểu một thứ vừa 100 % mát vừa 100 % không mát — mâu thuẫn đó sẽ phá huỷ lô-gic "
        "hình thức."))
    b.append(p(
        "Cần phân biệt rõ: ràng buộc này áp cho một tập và phần bù của chính nó, không áp cho hai tập "
        "lân cận. “Mát” và “vừa phải” là hai tập khác nhau, không phải hai nửa của một cặp bù nhau, nên "
        "tổng độ phụ thuộc vào chúng không buộc phải bằng một."))

    b.append(h3("13.5.1 Một nghịch lý", "Fuzzy Logic — a Conundrum"))
    b.append(p(
        "(Xin cảm ơn Bertrand Russell.) Mục này có lẽ giúp minh hoạ thế giới của lô-gic mờ; hãy đọc nó "
        "với toàn bộ sự chú ý, vì nó cho thấy khác biệt giữa “nửa vơi” và “nửa đầy”. Đây là một nghịch lý "
        "Hy Lạp nằm ở trung tâm của lý thuyết tập hợp và lô-gic hiện đại."))
    b.append(ul([
        "Một người Crete khẳng định rằng mọi người Crete đều nói dối.",
        "Vậy anh ta có đang nói dối không?",
        "Nếu anh ta nói dối, thì điều anh ta nói là đúng, tức là anh ta không nói dối.",
        "Nếu anh ta không nói dối, thì anh ta nói thật, và như vậy là anh ta nói dối."]))
    b.append(p(
        "Cả hai trường hợp đều dẫn tới mâu thuẫn, vì phát biểu vừa đúng vừa sai. Nghịch lý tương tự tồn "
        "tại trong lý thuyết tập hợp: tập hợp của mọi tập hợp là một tập hợp, nên nó là phần tử của chính "
        "nó; nhưng tập hợp mọi quả táo không phải là phần tử của chính nó, vì các phần tử của nó là táo "
        "chứ không phải tập hợp. Mâu thuẫn nằm ở chỗ: tập hợp của mọi tập hợp không là phần tử của chính "
        "nó — nó có là phần tử của chính nó không? Nếu có thì không; nếu không thì có."))
    b.append(p(
        "Lô-gic cổ điển đầu hàng ở đây. Lô-gic mờ thì nói câu trả lời là nửa đúng và nửa sai — chia "
        "50–50, năm mươi phần trăm phát biểu của người Crete là đúng và năm mươi phần trăm là sai; anh "
        "ta nói dối nửa thời gian và nói thật nửa còn lại. Khi độ phụ thuộc nhỏ hơn trọn vẹn, lô-gic nhị "
        "nguyên có thể đơn giản hoá bằng cách làm tròn xuống 0 hoặc lên 100 %. NHƯNG 50 phần trăm thì "
        "không làm tròn lên cũng không làm tròn xuống được."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Mục 13.5.1 trong bản PDF gốc có tiêu đề “Fuzzy Logic "
        "! a Conundrum”; dấu “!” ở đây là lỗi quét của một dấu gạch ngang. Bản gốc cũng gọi nghịch lý này "
        "là “một nghịch lý Hy Lạp”, nhưng nghịch lý người Crete nói dối là của Epimenides còn cách xử lý "
        "theo lý thuyết tập hợp là của Russell — bản dịch giữ nguyên cả hai tên như bản gốc đã dẫn."))

    b.append(h3("13.5.2 Một ví dụ minh hoạ luật mờ", "An Example to Illustrate Fuzzy Rules"))
    b.append(p(
        "Lô-gic mờ dựa trên các luật có dạng “Nếu … Thì …”, chuyển đầu vào thành đầu ra — chuyển một tập "
        "mờ thành một tập mờ khác. Ví dụ, bộ điều khiển của máy điều hoà trên một chiếc ô tô có thể gồm "
        "những luật như:"))
    b.append(ul([
        "Nếu nhiệt độ là mát, thì đặt động cơ ở mức chậm.",
        "Nếu nhiệt độ là vừa phải, thì đặt tốc độ ở mức trung bình."]))
    b.append(p(
        "Các nhiệt độ (mát và vừa phải) và các tốc độ động cơ (chậm và trung bình) đặt tên cho những tập "
        "mờ chứ không phải cho những giá trị cụ thể. Đây là điểm mấu chốt: “mát” không phải là 21 °C, nó "
        "là một tập hợp mà 21 °C thuộc vào ở một mức độ nào đó."))

    b.append(h3("13.5.3 Vẽ và tạo một mảng mờ", "Plotting and Creating a Fuzzy Patch"))
    b.append(p(
        "Nếu bây giờ ta vẽ các đầu vào (nhiệt độ) trên một trục của đồ thị và các đầu ra (tốc độ động cơ) "
        "trên trục thứ hai, thì tích của hai tập mờ này tạo thành một mảng mờ — một vùng biểu diễn tập hợp "
        "mọi liên hệ mà luật ấy thiết lập giữa đầu vào và đầu ra. Kích thước của mảng cho biết độ lớn của "
        "sự mơ hồ hay bất định của luật."))
    b.append(p(
        "Tuy nhiên, nếu “mát” đúng bằng 21,5 °C thì tập mờ ấy sụp lại thành một “cái gai”. Nếu cả tập "
        "“chậm” lẫn tập “mát” đều là gai thì mảng của luật chỉ còn là một điểm. Điều này xảy ra khi 21,5 "
        "°C đòi hỏi tốc độ động cơ đúng 650 vòng/phút — một kết quả hoàn toàn hợp lý cho bài toán ấy."))
    b.append(p(
        "Nói cách khác, tập mờ càng hẹp thì mảng càng nhỏ và luật càng dứt khoát; khi tập co lại thành "
        "một điểm, lô-gic mờ quay trở về đúng lô-gic chuẩn. Đây là lý do lô-gic mờ được xem là một mở "
        "rộng của lô-gic chuẩn chứ không phải một thứ đối lập với nó."))

    b.append(h3("13.5.4 Việc dùng các mảng mờ", "The Use of Fuzzy Patches"))
    b.append(p(
        "Một hệ mờ phải có một bộ mảng chồng lên nhau, phủ toàn bộ dải đầu vào tới đầu ra. Có thể thấy "
        "rằng đủ nhiều mảng mờ nhỏ sẽ phủ được đồ thị của bất kỳ hàm nào, tức bất kỳ quan hệ vào–ra nào. "
        "Cũng có thể chọn trước sai số tối đa của phép xấp xỉ và tin chắc rằng tồn tại một số hữu hạn "
        "luật mờ đạt được sai số ấy."))
    b.append(p(
        "Một hệ mờ “suy luận” dựa trên các mảng luật của nó. Hai luật trở lên biến một con số đầu vào "
        "thành một kết quả nào đó, vì các mảng chồng lên nhau. Khi dữ liệu kích hoạt các luật, những mảng "
        "chồng nhau phản ứng song song — nhưng mỗi mảng chỉ ở một mức độ nhất định."))

    b.append(h2("13.6 Ví dụ dùng 5 luật và 5 mảng", "Example using 5 Rules and Patches"))
    b.append(p(
        "Như một ví dụ về lô-gic mờ, ta xét một máy điều hoà dựa trên năm luật và do đó năm mảng để liên "
        "hệ nhiệt độ với tốc độ động cơ. Hình 13-2 minh hoạ ứng dụng này."))

    b.append(h3("13.6.1 Định nghĩa các luật", "Defining the Rules"))
    b.append(p(
        "Các tập nhiệt độ là LẠNH, MÁT, VỪA PHẢI, ẤM và NÓNG; chúng phủ mọi đầu vào mờ có thể có. Các "
        "tập tốc độ động cơ là RẤT CHẬM, CHẬM, TRUNG BÌNH, NHANH và TỐI ĐA; chúng mô tả mọi đầu ra mờ."))
    b.append(fig(2, F.fig_13_2()))
    b.append(p(
        "Một nhiệt độ, giả sử 68 °F, có thể được biểu diễn bằng các tập mờ và các luật sau:"))
    b.append(ul([
        "20 % mát, và do đó 80 % KHÔNG mát, và",
        "70 % vừa phải, và 30 % KHÔNG vừa phải;",
        "đồng thời không khí là 0 % lạnh, 0 % ấm và 0 % nóng."]))
    b.append(p(
        "Các luật “nếu mát” và “nếu vừa phải” sẽ kích hoạt và gọi cả hai tốc độ CHẬM và TRUNG BÌNH."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Ba gạch đầu dòng trên cộng lại chỉ được 90 % (20 % "
        "mát + 70 % vừa phải), trong khi mục 13.5 khẳng định độ phụ thuộc vào một nhóm và nhóm bù của nó "
        "phải cộng lại bằng một. Con số 10 % còn lại không được bản gốc giải thích. Bản dịch giữ nguyên "
        "các giá trị 20 % và 70 % như bản gốc vì toàn bộ ví dụ về sau dựa trên chúng."))

    b.append(h3("13.6.2 Tác động lên các luật", "Acting on the Rules"))
    b.append(p(
        "Hai luật đóng góp theo tỉ lệ vào tốc độ động cơ cuối cùng. Vì nhiệt độ là 20 % mát, đường cong "
        "mô tả động cơ chậm phải co xuống còn 20 % chiều cao của nó. Đường cong trung bình cũng vì lý do "
        "ấy phải co xuống còn 70 %. Cộng hai đường cong này lại cho ta đường cong cuối cùng của tập mờ."))
    b.append(fig(3, F.fig_13_3()))
    b.append(p(
        "Tuy nhiên, ở dạng mờ của nó, đường cong ấy không thể được một hệ nhị phân hiểu được; vì vậy "
        "bước cuối cùng của quá trình là giải mờ."))

    b.append(h3("13.6.3 Giải mờ", "Defuzzification"))
    b.append(p(
        "Đây là bước biến đường cong đầu ra mờ thu được thành một giá trị số duy nhất. Cách thông thường "
        "để làm việc này là tính khối tâm, hay trọng tâm, của diện tích dưới đường cong. Trong ví dụ của "
        "ta, việc này tương ứng với tốc độ 47 vòng/phút."))
    b.append(fig(4, F.fig_13_4()))
    b.append(p(
        "Như vậy, bắt đầu từ một đầu vào nhiệt độ định lượng, bộ điều khiển điện tử có thể suy luận từ "
        "các tập nhiệt độ và tốc độ mờ để đi tới một đầu ra tốc độ vừa thích hợp vừa chính xác."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Con số 47 vòng/phút ở mục 13.6.3 không tái tạo được "
        "từ chính các dữ kiện mà bản gốc đưa ra. Với hai tập tam giác có cùng nửa độ rộng và hai lát cắt "
        "ở mức 0,20 và 0,70, trọng tâm tính ra khoảng 45 % thang tốc độ, và giá trị này gần như không đổi "
        "khi thay đổi độ rộng của các tập (thử từ 15 đến 25 đơn vị đều cho 44,7 đến 45,1). Ngoài ra đơn "
        "vị “vòng/phút” cũng không khớp với ví dụ trước đó ở mục 13.5.3, nơi 21,5 °C ứng với 650 "
        "vòng/phút. Hình 13-4 vẽ đúng trọng tâm tính được và đánh dấu vị trí 47 của bản gốc để tiện đối "
        "chiếu."))

    b.append(h2("13.7 Gót chân Achilles của lô-gic mờ", "The Achilles Heel of Fuzzy Logic"))
    b.append(p(
        "Điểm yếu của lô-gic mờ nằm ở chính các luật của nó. Trong phần lớn ứng dụng mờ, các luật ấy do "
        "những kỹ sư am hiểu ứng dụng liên quan đặt ra. Điều này dẫn tới một quá trình “chỉnh định” các "
        "luật và các tập mờ rất dài. Để tự động hoá quá trình ấy, nhiều công ty đang chuyển sang xây dựng "
        "và dùng các hệ mờ thích nghi, dùng mạng nơ-ron hoặc các công cụ thống kê khác để tinh chỉnh, thậm "
        "chí để hình thành nên những luật ban đầu đó."))
    b.append(quote(
        "Một hệ mờ không tự biết mình đúng hay sai. Nó chỉ làm đúng những gì người ta viết vào — kể cả "
        "khi điều người ta viết vào là sai.",
        "Hệ quả của mục 13.7"))
    b.append(p(
        "Đây là lý do tự nhiên để chuyển sang nửa sau của chương. Nếu vấn đề của lô-gic mờ là các luật "
        "phải do người viết ra, thì một hệ có thể tự viết luật cho mình từ dữ liệu sẽ giải quyết được "
        "đúng điểm yếu ấy. Đó là ý tưởng của mạng nơ-ron."))

    b.append(h2("13.8 Mạng nơ-ron", "Neural Networks"))
    b.append(p(
        "Mạng nơ-ron là tập hợp các “nơ-ron” và các “khớp nối”, chúng thay đổi giá trị để đáp lại đầu vào "
        "từ các nơ-ron và khớp nối xung quanh. Mạng nơ-ron hoạt động như một máy tính vì nó ánh xạ đầu "
        "vào thành đầu ra. Các nơ-ron và khớp nối có thể là linh kiện silic hoặc là những phương trình "
        "phần mềm mô phỏng hành vi của chúng. Một nơ-ron cộng mọi tín hiệu đến từ các nơ-ron khác rồi "
        "phát ra phản ứng của mình dưới dạng một con số. Tín hiệu đi qua các khớp nối, và mỗi khớp nối "
        "mang một giá trị số đóng vai trò trọng số cho dòng giá trị nơ-ron."))
    b.append(p(
        "Khi dữ liệu đầu vào mới “kích hoạt” một mạng nơ-ron, các giá trị khớp nối có thể thay đổi đôi "
        "chút. Một mạng nơ-ron “học” khi nó thay đổi giá trị các khớp nối của mình."))

    b.append(h3("13.8.1 Quá trình học", "The Learning Process"))
    b.append(p(
        "Hình 13-5 minh hoạ một mạng nơ-ron điển hình và các kết nối khớp nối của nó. Mỗi nơ-ron, như "
        "hình vẽ, nhận một số đầu vào X<sub>i</sub> được gán trọng số bởi khớp nối W<sub>i</sub> nối vào "
        "nó. Từ tổng đầu vào có trọng số, phần tử xử lý tính ra một giá trị đầu ra duy nhất Y."))
    b.append(fig(5, F.fig_13_5()))
    b.append(p(
        "Hình 13-6 cho thấy điều gì xảy ra bên trong mỗi nơ-ron khi nó được kích hoạt hay xử lý."))
    b.append(fig(6, F.fig_13_6()))
    b.append(h4("Đầu vào của nơ-ron"))
    b.append(p(
        "Nhiều tín hiệu khác nhau (các đầu vào X<sub>i</sub> của nơ-ron) được nhận từ các nơ-ron khác qua "
        "các khớp nối."))
    b.append(h4("Tính toán đầu vào của nơ-ron"))
    b.append(p("Một tổng có trọng số của các giá trị đầu vào này được tính."))
    b.append(h4("Biến đổi bằng hàm bên trong nơ-ron"))
    b.append(p(
        "Tổng của phép tính đầu vào được biến đổi bởi một hàm bên trong, hàm này thường — nhưng không "
        "phải luôn luôn — cố định cho một nơ-ron tại thời điểm mạng được xây dựng."))
    b.append(h4("Đầu ra của nơ-ron"))
    b.append(p(
        "Kết quả đã biến đổi (các đầu ra) được gửi riêng lẻ tới các nơ-ron khác qua khớp nối liên kết."))

    b.append(h3("13.8.2 Hành động của nơ-ron trong “học”", "Neuron Actions in Learning"))
    b.append(p(
        "Học có nghĩa là nơ-ron thay đổi hành vi từ đầu vào tới đầu ra để đáp lại môi trường mà nó tồn "
        "tại. Tuy nhiên, hàm biến đổi của nơ-ron thường là cố định, nên cách duy nhất để thay đổi phép "
        "biến đổi đầu vào–đầu ra là thay đổi trọng số ngưỡng áp lên các ĐẦU VÀO."))
    b.append(p(
        "Vậy nên “học” đạt được bằng cách thay đổi các trọng số trên đầu vào, và mô hình bên trong của "
        "mạng được thể hiện trong toàn bộ tập hợp các trọng số ấy."))
    b.append(p("Vậy làm thế nào để thay đổi các “trọng số” này?"))
    b.append(p(
        "Một trong những dạng phổ biến và được dùng rộng rãi nhất được gọi là “lan truyền ngược”, thường "
        "được dùng trong kỹ thuật hoá học."))

    b.append(h2("13.9 Mạng lan truyền ngược", "Neural Back-Propagation Networking"))
    b.append(p(
        "Những mạng này luôn gồm ba lớp nơ-ron: lớp vào, lớp giữa và lớp ra. Cách xây dựng là mỗi nơ-ron "
        "trong một lớp được nối tới mọi nơ-ron của lớp kế tiếp (Hình 13-5). Số nơ-ron của lớp giữa thì "
        "thay đổi, nhưng phải chọn cẩn thận: quá nhiều sẽ cho ra những mẫu hình không quản lý nổi, còn "
        "quá ít sẽ đòi hỏi một số vòng lặp quá lớn trước khi có được đầu ra chấp nhận được."))

    b.append(h3("13.9.1 Dòng đầu ra thuận (khởi tạo nơ-ron)", "Forward Output Flow"))
    b.append(p(
        "Mẫu ban đầu của các trọng số nơ-ron được chọn ngẫu nhiên và đưa vào lớp vào, lớp này chuyển tiếp "
        "nó tới lớp giữa. Mỗi nơ-ron tính tín hiệu đầu ra của mình như sau. Tổng đầu ra I<sub>j</sub> "
        "được xác định bằng cách nhân từng tín hiệu đầu vào với giá trị trọng số ngẫu nhiên trên khớp nối "
        "liên kết:"))
    b.append(eq("I<sub>j</sub> = Σ<sub>i</sub> W<sub>ji</sub> · X<sub>i</sub> + B<sub>j</sub>", "13.2"))
    b.append(p(
        "Tổng có trọng số này được biến đổi bởi một hàm f(X) gọi là hàm kích hoạt của nơ-ron; hàm này "
        "quyết định mức hoạt động được tạo ra trong nơ-ron do kết quả của một tín hiệu đầu vào có độ lớn "
        "nhất định."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Công thức (13.2) bị quét hỏng hoàn toàn trong bản PDF "
        "gốc: dòng gốc in ra “i j j i i j Ij = W X +B − − ∑ . 1 . 1”, không đọc được. Bản dịch phục dựng "
        "lại dạng chuẩn của tổng có trọng số cộng ngưỡng lệch, đúng như phần chữ ngay trên đó mô tả "
        "(nhân từng đầu vào với trọng số trên khớp nối rồi cộng lại). Ký hiệu W<sub>ji</sub> theo đúng "
        "quy ước của bản gốc: chỉ số thứ nhất là nơ-ron nhận, chỉ số thứ hai là nơ-ron gửi."))

    b.append(h3("13.9.2 Hàm sigmoid của nơ-ron", "Neural Sigmoidal Functions"))
    b.append(p(
        "Với mạng lan truyền ngược, và với hầu hết ứng dụng trong kỹ thuật hoá học, hàm được mô tả ở mục "
        "13.9 là một hàm sigmoid. Hàm này, như thấy ở Hình 13-7, có các tính chất:"))
    b.append(ul([
        "Liên tục;",
        "Có dạng chữ S;",
        "Tăng đơn điệu;",
        "Tiệm cận những giá trị cố định khi đầu vào tiến tới ±∞."]))
    b.append(fig(7, F.fig_13_7()))
    b.append(p(
        "Nói chung, giới hạn trên của một hàm sigmoid được đặt bằng +1 và giới hạn dưới bằng 0 hoặc −1. "
        "Độ dốc của đường cong, và thậm chí cả công thức chính xác dùng để tính nó, thường ít quan trọng "
        "hơn hình dạng chữ “S” nói chung."))
    b.append(p(
        "Đường cong sigmoid sau đây, biểu diễn như một hàm của I<sub>j</sub> — tổng đầu vào có trọng số "
        "của nơ-ron — được dùng rất rộng rãi:"))
    b.append(eq("f(I<sub>j</sub>) = 1 / (1 + e<sup>−(I<sub>j</sub> − T)</sup>)", "13.3"))
    b.append(p(
        "trong đó T là một ngưỡng đơn giản và X là đầu vào. Tín hiệu đã biến đổi này trở thành toàn bộ "
        "mức hoạt động của các nơ-ron lớp giữa, được dùng làm đầu ra của chúng; các đầu ra ấy lại trở "
        "thành đầu vào của lớp nơ-ron đầu ra, nơi một hành động tương tự diễn ra trong nơ-ron đầu ra, "
        "dùng hàm sigmoid để tạo ra một giá trị đầu ra cuối cùng từ nơ-ron."))
    b.append(note(
        "<b>Ghi chú của người dịch về bản gốc.</b> Công thức (13.3) cũng bị quét hỏng: bản gốc in ra "
        "“() Ij T j j e X f I − + + =”, chỉ còn nhận ra được các ký hiệu rời. Dạng chuẩn của hàm sigmoid "
        "một ngưỡng đúng là dạng được phục dựng ở trên, và nó khớp với cả bốn tính chất mà bản gốc liệt "
        "kê ngay trước đó."))

    b.append(h3("13.9.3 Lan truyền sai số ngược (quy tắc delta)",
                "Backward Error Propagation — the Delta Rule"))
    b.append(p(
        "Kết quả ở đầu ra được đem so với đầu ra mong muốn. Hiệu số (hay sai số) trở thành một giá trị "
        "ngưỡng mà nhờ đó ta sửa các trọng số trên các kết nối nơ-ron. Thường phải mất vài vòng lặp mới "
        "khớp được đầu ra mục tiêu yêu cầu."))
    b.append(p(
        "Phương pháp delta là một trong những phương pháp phổ biến nhất dùng trong lan truyền ngược. Quy "
        "tắc delta lặp đi lặp lại việc cực tiểu hoá sai số bình phương trung bình giữa đầu ra của từng "
        "nơ-ron và giá trị mục tiêu. Gradient sai số sau đó được xác định cho các lớp ẩn (lớp giữa) bằng "
        "cách tính sai số có trọng số của lớp ấy. Cụ thể:"))
    b.append(ul([
        "Các sai số được lan truyền ngược lại một lớp;",
        "Thủ tục tương tự được áp dụng đệ quy cho tới khi chạm lớp vào;",
        "Đó là dòng sai số ngược."]))
    b.append(p(
        "Các gradient sai số tính được sau đó dùng để cập nhật trọng số của mạng. Một số hạng quán tính "
        "có thể được đưa vào thủ tục này để xác định ảnh hưởng của những thay đổi trọng số trước đó lên "
        "thay đổi trọng số hiện tại, trong không gian trọng số. Việc này thường giúp cải thiện sự hội "
        "tụ."))
    b.append(eq("Δw<sub>ji</sub>(k) = α · Δw<sub>ji</sub>(k−1) − η · ∂E/∂w<sub>ji</sub>", "13.4"))
    b.append(p(
        "trong đó α là hệ số quán tính và η là tốc độ học. Như vậy lan truyền ngược là một thuật toán hạ "
        "theo gradient, nó cố cực tiểu hoá sai số bình phương trung bình của mạng bằng cách đi xuống "
        "theo gradient của đường cong sai số. Trong một hệ đơn giản, đường cong sai số có dạng cái bát "
        "(paraboloid) và cuối cùng mạng sẽ tới được đáy bát."))
    b.append(fig(8, F.fig_13_8()))

    b.append(h2("13.10 Huấn luyện một mạng nơ-ron", "Training a Neuron Network"))
    b.append(p(
        "Về nguyên tắc có bảy kỹ thuật chuẩn được dùng để “huấn luyện” một mạng đạt sai số bằng không "
        "(tức nằm yên ở đáy của đường cong sai số dạng bát)."))

    b.append(h3("13.10.1 Khởi tạo lại các trọng số", "Re-initialize the Weights"))
    b.append(p(
        "Nếu gặp khó khăn trong việc tìm cực tiểu toàn cục, có thể áp một bộ trọng số ngẫu nhiên mới lên "
        "đầu vào của quá trình và lặp lại quá trình học."))

    b.append(h3("13.10.2 Thêm bước nhảy vào các trọng số hiện có", "Add Step Changes to the Weights"))
    b.append(p(
        "Mạng có thể “dao động” quanh một giá trị sai số do bất kỳ thay đổi trọng số nào tính được cũng "
        "không làm giảm số hạng sai số. Điều thường cần chỉ là một “cú huých nhẹ” vào các hệ số trọng số. "
        "Có thể đạt được điều này bằng cách dịch ngẫu nhiên các giá trị trọng số tới vị trí mới, nhưng "
        "không quá xa điểm xuất phát."))

    b.append(h3("13.10.3 Tránh quá nhiều tham số", "Avoiding Overparameterization"))
    b.append(p(
        "Nếu lớp giữa (lớp ẩn) có quá nhiều nơ-ron thì xảy ra hiện tượng quá nhiều tham số, và điều đó "
        "dẫn tới dự báo kém. Giảm số nơ-ron ở lớp này là cách chữa. Ở đây không có quy tắc ngón tay cái "
        "nào; số nơ-ron cần thiết tốt nhất là xác định bằng thực nghiệm."))

    b.append(h3("13.10.4 Thay đổi số hạng quán tính", "Changing the Momentum Term"))
    b.append(p(
        "Đây là việc dễ làm nhất nếu hệ là một mạng phần mềm. Số hạng quán tính α được thực hiện bằng "
        "cách cộng một phần của số hạng trọng số trước vào số hạng mới; thay đổi giá trị này — cũng tốt "
        "nhất là làm bằng thực nghiệm — có thể giúp chữa được lỗi."))

    b.append(h3("13.10.5 Nhiễu và dữ liệu lặp lại", "Noise and Repeated Data"))
    b.append(p(
        "Tránh dữ liệu lặp lại hoặc ít nhiễu. Đầu vào lặp lại hoặc không có nhiễu làm mạng ghi nhớ mẫu "
        "hình thay vì khái quát hoá các đặc điểm của nó. Nếu mạng không bao giờ gặp cùng một giá trị đầu "
        "vào hai lần thì điều đó ngăn nó ghi nhớ mẫu hình. Đưa nhiễu vào có thể giúp ngăn chặn việc này."))

    b.append(h3("13.10.6 Thay đổi dung sai học", "Changing the Learning Tolerance"))
    b.append(p(
        "Việc huấn luyện một mạng dừng lại khi giá trị sai số của mọi trường hợp đều bằng hoặc nhỏ hơn "
        "dung sai học. Nếu dung sai này quá nhỏ thì quá trình học không bao giờ dừng. Hãy thử nghiệm mức "
        "dung sai cho tới khi đạt một điểm thoả đáng, ở đó các trọng số thôi thay đổi giá trị một cách "
        "đáng kể."))

    b.append(h3("13.10.7 Tăng số nơ-ron lớp giữa (lớp ẩn)", "Increasing the Hidden Layer Value"))
    b.append(p(
        "Đây là bài toán ngược với vấn đề mô tả ở mục 13.10.3, “Tránh quá nhiều tham số”, và được dùng "
        "khi mọi cách khác đều đã thất bại. Nói cách khác, ta có quá ít nơ-ron ở lớp giữa, trong khi ở "
        "mục 13.10.3 ta có quá nhiều. Nói chung, tăng quá 10 % cho thấy có cải thiện."))
    b.append(table(
        ["Kỹ thuật", "Khi nào dùng", "Điều cần lưu ý"],
        [["Khởi tạo lại trọng số",
          "Kẹt ở một cực tiểu địa phương, sai số không giảm nữa",
          "Mỗi lần chạy cho một kết quả khác; phải lưu lại bộ trọng số tốt nhất"],
         ["Thêm bước nhảy nhỏ",
          "Sai số dao động quanh một giá trị mà không giảm",
          "Bước nhảy phải nhỏ, nếu không mạng mất toàn bộ phần đã học"],
         ["Giảm số nơ-ron lớp ẩn",
          "Dự báo kém dù sai số huấn luyện thấp",
          "Không có quy tắc cố định; phải thử"],
         ["Đổi hệ số quán tính α",
          "Hội tụ quá chậm hoặc dao động",
          "Dễ làm nhất với mạng phần mềm; đổi từng bước nhỏ"],
         ["Thêm nhiễu, tránh dữ liệu lặp",
          "Mạng học thuộc mẫu hình thay vì khái quát hoá",
          "Nhiễu phải nhỏ hơn biến thiên thật của quá trình"],
         ["Nới dung sai học",
          "Quá trình học không bao giờ dừng",
          "Dung sai quá lớn thì mạng dừng khi còn sai số đáng kể"],
         ["Tăng số nơ-ron lớp ẩn",
          "Đã thử mọi cách trên mà vẫn không đạt",
          "Tăng quá 10 %; quay lại rủi ro quá nhiều tham số"]],
        "Bảng 13-1. Bảy kỹ thuật huấn luyện của mục 13.10, tóm tắt theo triệu chứng."))

    b.append(h2("13.11 Kết luận, và bước tiếp theo", "Conclusions, and then the Next Step"))
    b.append(p(
        "Lô-gic mờ đã được dùng từ đầu những năm 1980 và đã rất thành công trong nhiều ứng dụng, ví dụ "
        "việc Hitachi dùng nó để điều khiển tàu điện ngầm — chính xác và tin cậy tới mức hiệu năng của nó "
        "vượt cả những gì một người lái được huấn luyện có thể làm. Khi các nguyên lý ấy được dùng cùng "
        "với mạng nơ-ron hay mạng tự học, ta có trong tay một bộ công cụ rất mạnh. Khi áp dụng vào hệ "
        "điều khiển quá trình, nó mở ra một tương lai nhìn thấy được của những hệ điều khiển không còn "
        "sai số, có thể xử lý mọi biến thiên — kể cả người vận hành — tới mức cuối cùng ta có thể có một "
        "hệ “hoàn hảo”."))
    b.append(p(
        "Trong lúc chờ đợi, còn hai vấn đề nữa cần xem xét, và có thể coi chúng là bước trung gian từ "
        "công nghệ quá khứ và hiện tại tới hệ điều khiển tự học, hoàn toàn chính xác của tương lai. Hai "
        "vấn đề ấy, được bàn và mô tả ở chương 14, khép lại cuốn sách này về điều khiển quá trình thực "
        "tế. Đó là điều khiển quá trình bằng thống kê (SPC) và bộ điều khiển tự chỉnh định."))
    b.append(p(
        "SPC được dùng để thấy quá trình đang sai ở đâu — một bài toán mà mạng nơ-ron giải được; còn bộ "
        "điều khiển tự chỉnh định là bài toán mà lô-gic mờ có thể giải."))
    b.append(p(
        "Cần nói thêm một điều mà bản gốc chỉ ngụ ý. Trong điều khiển quá trình công nghiệp, lô-gic mờ "
        "và mạng nơ-ron hiếm khi thay thế một bộ PID; chúng thường ngồi bên cạnh nó — đặt điểm đặt, chỉnh "
        "hệ số, hoặc phát hiện những chế độ vận hành mà bộ PID không xử lý nổi. Một vòng điều khiển lưu "
        "lượng vẫn là một bộ PID, và nên là như vậy. Giá trị của hai công cụ này nằm ở những bài toán mà "
        "phương trình không viết được, chứ không nằm ở những bài toán mà phương trình viết được rất dễ."))
    return "".join(b)


# ---------------------------------------------------------------- English

def body_en():
    b = []
    b.append(p(
        "Every chapter so far has stood on an unspoken assumption: that the designer can write down the "
        "process equation. A transfer function, a time constant, a dead time — and the controller follows "
        "from them. Chapter 12 went a step further and built a parallel model to cancel a dead time."))
    b.append(p(
        "Some processes will not give you that equation, and not because you are lazy — because it does "
        "not exist. A clinker kiln, a twelve-tray column, a line whose feedstock changes with every batch: "
        "nobody can write their transfer function, and if they could the coefficients would drift within "
        "weeks of operation."))
    b.append(p(
        "This chapter presents two ways out, and they are different in kind. Fuzzy logic replaces the "
        "equation with words: a good operator always knows what to do, they simply cannot write it as a "
        "formula — fuzzy logic is the notation that turns those “if … then …” sentences into something a "
        "machine can execute. A neural network does not even need the words: it extracts the rule from "
        "the data, and what it learns lives scattered across a set of weights that nobody can read back "
        "as a sentence."))

    b.append(h2("Fuzziness is not probability", "§ 13.4"))
    b.append(p(
        "The single most useful distinction in the chapter is stated in one line and deserves more space "
        "than it gets. Probability measures whether something <em>will</em> occur. Fuzziness measures the "
        "degree to which something <em>does</em> occur."))
    b.append(p(
        "“There is a 70 per cent chance of rain” is a statement about a future event that has not "
        "happened. “The air is 70 per cent warm” is a statement about the present, which is already the "
        "case — it is merely described by a degree rather than a threshold. Confusing the two produces "
        "the classic mistake of building a fuzzy system whose memberships are really likelihoods, and "
        "then wondering why the output drifts."))
    b.append(fig(1, F.fig_13_1(), "en"))
    b.append(p(
        "Figure 13-1 is the whole of section 13.3 in one picture. The crisp set is a step: an element is "
        "in or out, and the boundary is a vertical line. The fuzzy set tapers, so the same element can "
        "belong partly and not belong partly at the same time. Everything else in fuzzy control follows "
        "from allowing that taper."))

    b.append(h2("The one hard constraint: complements sum to one", "§ 13.5"))
    b.append(p(
        "Fuzzy logic gives up very little. It abandons the law of the excluded middle, but keeps one rule "
        "that stops the whole structure collapsing into contradiction: an element's membership in a set "
        "and in that set's complement must sum to one. If something is 30 per cent cool it is, by "
        "definition, 70 per cent not cool. Without that, you could have a thing that is fully cool and "
        "fully not cool, and formal logic would be gone."))
    b.append(eq("μ<sub>A</sub>(x) + μ<sub>Ā</sub>(x) = 1", "13.1"))
    b.append(p(
        "Note carefully what the constraint does <em>not</em> say. It applies to a set and its own "
        "complement, not to two neighbouring sets. “Cool” and “just right” are different sets, not two "
        "halves of a complementary pair, so their memberships need not sum to one. This is worth stating "
        "because the chapter's own worked example later appears to assume otherwise — see the translator's "
        "note on the 20 / 70 split."))

    b.append(h2("Russell's paradox, and why 50 per cent is the hard case", "§ 13.5.1"))
    b.append(p(
        "The Cretan who says all Cretans lie is not a curiosity; it is the reason fuzzy logic needs "
        "degrees at all. Classical logic surrenders in front of the paradox because the statement is both "
        "true and false. Fuzzy logic answers “half true, half false” — and then makes a sharper point "
        "than it first appears to."))
    b.append(p(
        "A bivalent system can always rescue itself from a partial membership by rounding: 0.2 becomes 0, "
        "0.9 becomes 1. The rounding is a lie, but a small one, and the system keeps working. At exactly "
        "0.5 the trick fails, because 0.5 rounds neither up nor down. Half-truth is the one value a "
        "two-valued system cannot approximate, which is precisely why the paradox has no classical "
        "resolution and why fuzzy logic does."))

    b.append(h2("Patches: the rule as a region, not a point", "§ 13.5.3–13.5.4"))
    b.append(p(
        "The chapter's best idea is visual. Plot the input on one axis and the output on the other, and a "
        "rule stops being a sentence and becomes an area — a fuzzy patch. The patch is the product of the "
        "input set and the output set, and its size is a direct measure of how vague the rule is."))
    b.append(p(
        "That framing does two useful things. First, it makes the collapse to classical logic visible: "
        "shrink the input set to a single value (21.5 °C) and the patch becomes a spike; shrink both and "
        "it becomes a point, which is just a lookup table. Fuzzy logic is a generalisation of the lookup "
        "table, not a replacement for it. Second, it makes coverage an engineering question rather than a "
        "matter of taste: enough small patches cover any input–output relationship to any accuracy you "
        "care to name, and you can pick the maximum error in advance and be sure a finite number of rules "
        "achieves it."))

    b.append(h2("Five rules, one air conditioner", "§ 13.6"))
    b.append(fig(2, F.fig_13_2(), "en"))
    b.append(p(
        "Figure 13-2 is the chapter's worked example. Five temperature sets, five speed sets, five rules, "
        "five patches stepping up the diagonal. Because the patches overlap, any temperature in range "
        "fires at least two rules — and each fires only to a degree."))
    b.append(p(
        "The example's numbers are 20 per cent cool and 70 per cent just right at 68 °F. Two things are "
        "worth noticing. The two memberships sum to 90 per cent, not 100, which contradicts the "
        "complement rule only if you assume cool and just-right are complements — they are not, they are "
        "neighbours, so the sum is free to be anything. And the remaining 10 per cent is simply "
        "unassigned, which in a real controller would be a gap in coverage and a sign that the sets need "
        "widening."))
    b.append(fig(3, F.fig_13_3(), "en"))
    b.append(p(
        "Figure 13-3 is the step the chapter describes but does not draw. Acting on the rules means "
        "clipping: the SLOW curve is cut down to 20 per cent of its height, the MEDIUM curve to 70 per "
        "cent, because those are the degrees to which their rules fired. The two clipped slices are then "
        "unioned point by point, and the outer envelope is the fuzzy output set."))
    b.append(fig(4, F.fig_13_4(), "en"))
    b.append(p(
        "Defuzzification then collapses that envelope to one number: the abscissa of its centroid. This "
        "is where the chapter's arithmetic does not close. With the two triangular sets and the 0.20 / "
        "0.70 cuts it describes, the centroid lands at about 45 per cent of the speed scale — and stays "
        "between 44.7 and 45.1 for every set width from 15 to 25 units. The book states 47 rpm. The "
        "figure draws the computed centroid and marks the book's 47 alongside it so the discrepancy is "
        "visible rather than hidden."))

    b.append(h2("The Achilles heel is the rules, and it is a real one", "§ 13.7"))
    b.append(p(
        "The weakness the chapter names is not a technical limitation but an organisational one. The "
        "rules are written by engineers who know the application, and tuning them — together with the "
        "sets — is a long, manual, undocumented process. A fuzzy controller is only as good as the "
        "operator whose knowledge it encodes, and it will reproduce that operator's mistakes with perfect "
        "consistency and no judgement."))
    b.append(quote(
        "A fuzzy system does not know whether it is right. It does exactly what was written into it — "
        "including when what was written into it is wrong.",
        "The consequence of section 13.7"))
    b.append(p(
        "That is the honest reason the chapter turns to neural networks next. If the weakness is that "
        "humans must write the rules, a system that derives its own rules from data addresses exactly "
        "that weakness. Whether it addresses it well is a separate question, taken up below."))

    b.append(h2("A neuron is a weighted sum and a bend", "§ 13.8"))
    b.append(fig(5, F.fig_13_5(), "en"))
    b.append(p(
        "Figure 13-5 shows the topology: three layers, every neuron connected to every neuron of the next. "
        "The input layer does nothing but hold the numbers. The hidden layer does the work. The output "
        "layer produces the answer. Nothing in the diagram is more complicated than that, and it is worth "
        "saying plainly because the vocabulary around neural networks suggests otherwise."))
    b.append(fig(6, F.fig_13_6(), "en"))
    b.append(p(
        "Figure 13-6 opens one neuron. Inputs arrive, each multiplied by a weight, summed, offset by a "
        "bias, and passed through a fixed non-linear function. The function is fixed. The bias is fixed "
        "once chosen. The <em>only</em> thing that can change is the weights — and that single fact is "
        "what makes training possible at all: the learning problem reduces to finding a set of numbers."))
    b.append(eq("I<sub>j</sub> = Σ<sub>i</sub> W<sub>ji</sub> · X<sub>i</sub> + B<sub>j</sub>", "13.2"))
    b.append(p(
        "The source's formula is destroyed in the scan — it appears as a scatter of subscripts — so the "
        "equation above is reconstructed from the prose that describes it. The convention is the usual "
        "one: the first subscript is the receiving neuron, the second the sending one."))

    b.append(h2("The sigmoid, and why its exact shape does not matter", "§ 13.9.2"))
    b.append(fig(7, F.fig_13_7(), "en"))
    b.append(p(
        "Figure 13-7 plots f(I) = 1/(1 + e<sup>−(I−T)</sup>) at two thresholds. The chapter's list of "
        "properties — continuous, S-shaped, monotonically increasing, asymptotic — is a list of things "
        "that are true of almost any sigmoid, and that is the point it is making: the steepness and even "
        "the exact formula matter far less than the S shape. What the S shape buys you is differentiability "
        "everywhere, which is what makes the gradient in the next section exist."))
    b.append(eq("f(I<sub>j</sub>) = 1 / (1 + e<sup>−(I<sub>j</sub> − T)</sup>)", "13.3"))

    b.append(h2("Back-propagation is gradient descent, and the bowl explains the tuning", "§ 13.9.3"))
    b.append(p(
        "The delta rule is the whole of training: compute the error at the output, propagate it backwards "
        "one layer at a time, and nudge every weight in the direction that reduces it. The chapter "
        "describes it as descending the gradient of a bowl-shaped error surface, and that image is worth "
        "taking literally, because it explains every one of the seven training techniques in section "
        "13.10."))
    b.append(eq("Δw<sub>ji</sub>(k) = α · Δw<sub>ji</sub>(k−1) − η · ∂E/∂w<sub>ji</sub>", "13.4"))
    b.append(fig(8, F.fig_13_8(), "en"))
    b.append(p(
        "Figure 13-8 draws the bowl from above. Real error surfaces are elongated, not circular: the "
        "curvature is steep in some directions and shallow in others. Plain gradient descent therefore "
        "does two things at once — it damps the wobble across the steep axis within a couple of steps, "
        "and then crawls along the shallow axis for hundreds more. The momentum term α is precisely a "
        "device for speeding up the crawl: it accumulates velocity along the direction that keeps "
        "pointing the same way."))
    b.append(p(
        "Read the seven techniques in section 13.10 against that picture and they stop being a list of "
        "tricks. Re-initialising the weights escapes a local minimum. A small random push escapes a flat "
        "spot where the gradient has vanished. Reducing hidden neurons removes redundant directions that "
        "make the bowl unnecessarily elongated. Changing α trades crawl speed against wobble. Adding "
        "noise stops the network memorising the training set. Loosening the tolerance stops it chasing "
        "noise forever. Increasing hidden neurons, the last resort, adds the capacity the bowl was "
        "missing. Every one of them is a statement about the shape of the error surface."))

    b.append(h2("What the chapter is too optimistic about", "§ 13.11"))
    b.append(p(
        "The conclusion promises control systems that are error-free and cope with all variances, "
        "including the operator, until we finally have a “perfect” system. That is the one paragraph in "
        "the chapter that has not aged well, and it is worth saying so plainly."))
    b.append(p(
        "Neither technique replaced the PID controller, and in regulatory control neither was ever going "
        "to. What actually happened in the two decades after this text is more modest and more useful: "
        "fuzzy logic found a durable niche in multivariable supervisory layers and in appliances where "
        "the rule base is small and stable; neural networks, after a long winter, returned as the "
        "soft sensor and the inferential model — predicting a quality variable from the variables you can "
        "measure, feeding it to a controller that is still a PID."))
    b.append(p(
        "The judgement worth carrying away is this. Use fuzzy logic when an experienced operator can "
        "articulate the rule but nobody can write the equation. Use a neural network when you have "
        "history, a target you can measure, and no theory. Do not use either where a PID would do — and "
        "in process control, a PID does more often than the literature suggests."))
    return "".join(b)
