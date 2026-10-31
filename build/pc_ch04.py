# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 4, Fundamentals of Control Systems
(Wolfgang Altmann, IDC Technologies)."""
import pc4fig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 17
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Điều khiển đóng – ngắt (on-off / two-position)</em> — đầu ra chỉ có hai mức. · "
            "<em>Điều khiển điều biến (modulating)</em> — đầu ra biến thiên liên tục trong một dải xác định. · "
            "<em>Vòng hở (open loop)</em> — tác động điều khiển không phụ thuộc PV. · "
            "<em>Điều khiển theo mô hình (feedforward)</em> — dựa trên nhiễu đo được thay vì sai lệch. · "
            "<em>Vòng kín (closed loop / feedback)</em> — tác động điều khiển dựa trên sai lệch Err = SP − PV. · "
            "<em>Tác động thuận / nghịch</em> — PV tăng thì OP tăng / giảm. · "
            "<em>Thời gian chết L (dead time)</em> — khoảng trễ trước khi PV bắt đầu đáp ứng. · "
            "<em>Hằng số thời gian T (lag)</em> — quán tính của hệ, đo bằng thời điểm đạt 63,2 %. · "
            "<em>Vùng chết (dead zone / differential gap)</em> — dải quanh điểm đặt mà tại đó không có tác động.")
    return note(
        "<b>Key terms.</b> <em>On-off (two-position)</em> — a two-state output. · "
        "<em>Modulating</em> — a continuously variable output inside a defined range. · "
        "<em>Open loop</em> — the control action does not depend on the PV. · "
        "<em>Feedforward</em> — action taken on a measured disturbance instead of on the error. · "
        "<em>Closed loop</em> — action taken on the error Err = SP − PV. · "
        "<em>Direct / reverse acting</em> — PV up gives OP up / OP down. · "
        "<em>Dead time L</em> — the delay before the PV begins to respond. · "
        "<em>Lag T</em> — the inertia, measured as the 63.2 % point. · "
        "<em>Dead zone</em> — the band around the set point inside which no action is taken.")


def body_vi():
    b = []
    b.append(lead(
        "Chương trước nói về phần tử chấp hành cuối; chương này nói về cách ra quyết định trước khi tín hiệu "
        "tới phần tử đó. Có bốn chiến lược cơ bản — đóng – ngắt, điều biến, vòng hở và vòng kín — và mỗi "
        "chiến lược chỉ đúng trong một vùng điều kiện nhất định. Phần cuối chương dành cho hai đại lượng "
        "quyết định số phận của mọi vòng điều khiển: thời gian chết và vùng chết."))

    # ---------------------------------------------------------------- 4.1
    b.append(h2("4.1 Mục tiêu", "Objectives"))
    b.append(p("Chương này ôn lại các nguyên lý cơ bản của điều khiển quá trình. Sau khi học xong chương và "
               "làm các bài thực hành liên quan, sinh viên có thể:"))
    b.append(ul([
        "Giải thích rõ các khái niệm: điều khiển đóng – ngắt, điều khiển điều biến, điều khiển vòng hở và "
        "điều khiển tỉ lệ;",
        "Liệt kê mười từ viết tắt và thuật ngữ thông dụng nhất của điều khiển quá trình (ví dụ PV, MV, OP);",
        "Mô tả sự khác nhau giữa bộ điều khiển tác động nghịch và tác động thuận;",
        "Chỉ ra thời gian chết là gì và nó ảnh hưởng tới quá trình ra sao.",
    ]))
    b.append(table(
        ["Viết tắt", "Tiếng Anh", "Nghĩa"],
        [["PV", "Process Variable", "Biến quá trình — đại lượng được đo và điều khiển"],
         ["SP", "Set Point", "Điểm đặt — giá trị mong muốn của PV"],
         ["MV", "Manipulated Variable", "Biến điều khiển — đại lượng bị tác động"],
         ["OP", "Controller Output", "Tín hiệu ra của bộ điều khiển, tính theo %"],
         ["Err", "Error", "Sai lệch — hiệu giữa SP và PV"],
         ["K", "Gain", "Hệ số khuếch đại"],
         ["L", "Dead Time", "Thời gian chết"],
         ["T", "Time Constant", "Hằng số thời gian (độ trễ)"],
         ["PID", "Proportional-Integral-Derivative", "Ba chế độ điều khiển cơ bản"],
         ["DC", "Distortion Coefficient", "Hệ số méo dạng do lắp đặt"]],
        "Bảng 4-1 · Mười thuật ngữ và viết tắt cơ bản. Các ký hiệu này được dùng thống nhất trong toàn bộ "
        "bộ sách."))

    # ---------------------------------------------------------------- 4.2
    b.append(h2("4.2 Điều khiển đóng – ngắt", "ON-OFF Control"))
    b.append(p("Chiến lược điều khiển lâu đời nhất là dùng một công tắc, tạo ra điều khiển đóng – ngắt đơn "
               "giản như <b>Hình 4-1</b>. Đây là dạng tác động điều khiển không liên tục, còn gọi là điều "
               "khiển hai vị trí. Kỹ thuật này thô sơ, nhưng có thể là phương thức điều khiển rẻ và hiệu quả "
               "nếu chấp nhận được dao động khá lớn của biến quá trình."))
    b.append(fig(1, F.fig_4_1(), "vi"))
    b.append(p("Một bộ điều khiển đóng – ngắt lý tưởng ở trạng thái “bật” khi giá trị đo dưới điểm đặt, và "
               "khi đó biến điều khiển ở giá trị cực đại. Trên điểm đặt, bộ điều khiển “tắt” và MV ở mức cực "
               "tiểu."))
    b.append(p("Điều khiển đóng – ngắt được dùng rộng rãi trong cả công nghiệp lẫn sinh hoạt. Hầu hết mọi "
               "người đều quen với kỹ thuật này qua hệ thống sưởi gia đình và bình nước nóng. Lấy ví dụ một "
               "nồi hơi đốt gas gia dụng: khi nhiệt độ dưới điểm đặt, nhiên liệu “bật”; khi nhiệt độ vượt "
               "điểm đặt, nhiên liệu “tắt”, như <b>Hình 4-2</b>."))
    b.append(fig(2, F.fig_4_2(), "vi"))
    b.append(p("Thông thường có một vùng chết do các trễ cơ khí trong quá trình. Vùng này thường được đưa "
               "vào một cách có chủ ý để giảm tần số đóng cắt và giảm mài mòn chi tiết. Kết quả cuối cùng của "
               "chế độ điều khiển này là nhiệt độ sẽ dao động quanh giá trị yêu cầu."))
    b.append(note(
        "<b>Vì sao đóng – ngắt vẫn tồn tại.</b> Nó không bao giờ đưa PV đứng yên tại điểm đặt, nhưng nó "
        "không cần mô hình quá trình, không cần chỉnh tham số và không bao giờ mất ổn định. Với một nồi hơi "
        "gia nhiệt, một tủ lạnh hay một bể bơm nước, dao động ±1 °C hoàn toàn chấp nhận được — và cái giá "
        "của một bộ PID cùng van điều tiết là không cần thiết."))

    # ---------------------------------------------------------------- 4.3
    b.append(h2("4.3 Điều khiển điều biến", "Modulating Control"))
    b.append(p("Nếu đầu ra của bộ điều khiển có thể nhận một dải giá trị, đó là điều khiển điều biến."))
    b.append(p("Điều khiển điều biến chỉ diễn ra trong một dải làm việc xác định — nghĩa là nó phải có giới "
               "hạn trên và giới hạn dưới. Điều khiển điều biến mượt hơn điều khiển bước, và có thể dùng "
               "trong cả hệ vòng hở lẫn vòng kín."))

    # ---------------------------------------------------------------- 4.4
    b.append(h2("4.4 Điều khiển vòng hở", "Open Loop Control"))
    b.append(p("Trong điều khiển vòng hở, tác động điều khiển (tín hiệu ra OP) <b>không</b> phải là hàm của "
               "biến quá trình PV. Điều khiển vòng hở không tự sửa khi PV trôi, và điều đó có thể dẫn tới "
               "những sai lệch lớn so với giá trị tối ưu của PV."))

    b.append(h3("4.4.1 Sử dụng điều khiển vòng hở", "Use of Open Loop Control"))
    b.append(p("Kiểu điều khiển này thường dựa trên các nhiễu đo được ở đầu vào của hệ. Loại vòng hở thông "
               "dụng nhất là điều khiển theo mô hình (feedforward). Trong kỹ thuật này, tác động điều khiển "
               "dựa trên trạng thái của một nhiễu đầu vào mà không tham chiếu tới tình trạng thực của hệ — "
               "nghĩa là đầu ra của hệ không ảnh hưởng tới tác động điều khiển, và các biến vào được tác "
               "động để bù cho ảnh hưởng của nhiễu quá trình."))
    b.append(fig(3, F.fig_4_3(), "vi"))

    b.append(h3("4.4.2 Chức năng của điều khiển vòng hở", "Function of Open Loop Control"))
    b.append(p("Điều khiển theo mô hình cho kết quả sửa sai nhanh hơn nhiều so với điều khiển phản hồi, "
               "nhưng đòi hỏi lượng thông tin lớn hơn hẳn về ảnh hưởng của nhiễu lên hệ, và đòi hỏi tay nghề "
               "vận hành cao hơn."))

    b.append(h3("4.4.3 Ví dụ về điều khiển vòng hở", "Examples of Open Loop Control"))
    b.append(p("Một ứng dụng gia dụng quen thuộc minh hoạ điều khiển vòng hở là máy giặt. Hệ được đặt trước "
               "và chạy theo thời gian, lần lượt qua các chu trình giặt, xả và vắt như đã lập trình. Ở đây, "
               "tác động điều khiển chính là việc người dùng đánh giá khối lượng và độ bẩn của đồ rồi đặt "
               "máy tương ứng. Máy không đo tín hiệu ra — tức độ sạch của quần áo — nên độ chính xác của quá "
               "trình, hay thành công của lần giặt, phụ thuộc vào việc hiệu chuẩn của hệ."))
    b.append(p("Một hệ điều khiển vòng hở được trang bị kém để xử lý nhiễu, và nhiễu sẽ làm giảm hoặc phá "
               "hỏng khả năng hoàn thành nhiệm vụ mong muốn. Bất kỳ hệ điều khiển nào chạy theo thời gian "
               "đều là vòng hở; một ví dụ khác là đèn giao thông."))
    b.append(p("Rất khó thực hiện điều khiển vòng hở ở dạng thuần trong phần lớn ứng dụng điều khiển quá "
               "trình, vì khó đo chính xác các nhiễu và khó lường trước mọi nhiễu mà quá trình có thể gặp. "
               "Do mô hình dùng và phép đo đầu vào không hoàn toàn chính xác, điều khiển vòng hở thuần sẽ "
               "tích luỹ sai số và cuối cùng trở nên không đủ."))

    b.append(h3("4.4.4 Giới thiệu điều khiển tỉ lệ", "Introduction to Ratio Control"))
    b.append(p("Điều khiển tỉ lệ, đúng như tên gọi, là một dạng điều khiển theo mô hình nhằm giữ tỉ số của "
               "hai biến ở một giá trị xác định. Ví dụ, nếu cần điều khiển tỉ số của hai biến quá trình "
               "X<sub>PV</sub> và Y<sub>PV</sub>, thì đại lượng được điều khiển là PVR chứ không phải từng PV "
               "riêng lẻ:"))
    b.append(eq("PVR = X<sub>PV</sub> / Y<sub>PV</sub>", "4.1"))
    b.append(p("Một ví dụ điển hình là giữ tỉ lệ nhiên liệu/không khí cấp vào lò hơi không đổi, bất kể việc "
               "giữ nguyên hay thay đổi nhiệt độ lò. Cách làm này đôi khi được gọi là điều khiển giới hạn "
               "chéo (cross limiting control)."))
    b.append(fig(4, F.fig_4_4(), "vi"))

    # ---------------------------------------------------------------- 4.5
    b.append(h2("4.5 Vòng điều khiển kín", "Closed Control Loop"))
    b.append(p("Trong điều khiển vòng kín, mục tiêu của điều khiển — tức PV — được dùng để xác định tác động "
               "điều khiển. Cách gọi khác là điều khiển phản hồi, và nó được dùng phổ biến hơn điều khiển "
               "theo mô hình. Vòng kín được thiết kế để đạt và duy trì trạng thái mong muốn của quá trình "
               "bằng cách so sánh trạng thái thực với trạng thái mong muốn — điểm đặt SP — để có sai lệch "
               "Err."))
    b.append(fig(7, F.fig_4_7(), "vi"))

    b.append(h3("4.5.1 Bộ điều khiển tác động nghịch và tác động thuận",
                "Reverse or Direct Acting Controllers"))
    b.append(p("Vì tác động sửa sai của bộ điều khiển dựa trên độ lớn và dấu của sai lệch — được tính từ "
               "SP − PV hoặc PV − SP — nên các hàm P, I, D của bộ điều khiển không quan tâm dùng thuật toán "
               "nào, bởi thuật toán chỉ đổi dấu của số hạng sai lệch."))
    b.append(p("Tuy vậy, hãy xét <b>Hình 4-5</b>, minh hoạ cùng một bộ điều khiển làm cùng một việc nhưng "
               "theo hai cách khác nhau:"))
    b.append(ul([
        "<b>Trường hợp một:</b> tác động lên lưu lượng <em>ra</em> qua van V2 để điều khiển mức bể. Đây là "
        "tác động <b>thuận</b>. Khi PV tăng (bể đang đầy), OP tăng (mở van ra rộng hơn) để xả bể nhanh hơn. "
        "Tác động thuận: PV ⇑ → OP ⇑, khi đó Err = PV − SP.",
        "<b>Trường hợp hai:</b> điều khiển lưu lượng <em>vào</em> qua van V1 để điều khiển mức bể. Đây là "
        "tác động <b>nghịch</b>. Khi PV tăng (bể đang đầy), OP giảm (đóng bớt van vào) để giảm tốc độ cấp. "
        "Tác động nghịch: PV ⇑ → OP ⇓, khi đó Err = SP − PV.",
    ]))
    b.append(fig(5, F.fig_4_5(), "vi"))
    b.append(p("Đầu ra của bộ điều khiển thay đổi cùng độ lớn và cùng dấu với giá trị sai lệch thu được."))
    b.append(fig(6, F.fig_4_6(), "vi"))
    b.append(note(
        "<b>Cách nhớ nhanh.</b> Đừng hỏi “van này thuận hay nghịch”, hãy hỏi “khi PV tăng thì tôi phải làm "
        "gì để nó giảm”. Nếu câu trả lời là <em>mở thêm</em> thì đó là tác động thuận; nếu là <em>đóng "
        "bớt</em> thì là tác động nghịch. Việc đặt sai chiều tác động biến một bộ điều khiển tốt thành một "
        "bộ khuếch đại dương tính — và vòng kín sẽ bão hoà hoặc dao động ngay khi đóng điện."))

    b.append(h3("4.5.2 Các chế độ điều khiển trong vòng kín", "Control Modes in Closed Loop Control"))
    b.append(p("Phần lớn bộ điều khiển vòng kín có thể làm việc với ba chế độ, dùng riêng hoặc kết hợp: tỉ lệ "
               "(P), tích phân (I) và vi phân (D). Ba chế độ này được bàn kỹ ở chương sau."))

    b.append(h3("4.5.3 Minh hoạ khái niệm vòng hở và vòng kín",
                "Illustration of Open and Closed Loop Control"))
    b.append(p("Các sơ đồ ở <b>Hình 4-4</b> và <b>Hình 4-7</b> minh hoạ khái niệm vòng hở và vòng kín trên "
               "một hệ gia nhiệt nước:"))
    b.append(ul([
        "Ở ví dụ vòng hở (theo mô hình), lưu lượng hơi được thay đổi theo nhiệt độ của nước lạnh đi vào hệ. "
        "Người vận hành phải đủ kỹ năng để xác định thay đổi vị trí van bao nhiêu là đủ đưa nước lạnh vào hệ "
        "tới nhiệt độ mong muốn khi ra khỏi hệ.",
        "Ở ví dụ vòng kín (phản hồi), lưu lượng hơi được thay đổi theo nhiệt độ của nước nóng đi ra khỏi "
        "hệ. Người vận hành phải xác định độ lệch giữa giá trị đo đó với nhiệt độ mong muốn rồi thay đổi vị "
        "trí van cho tới khi hết sai lệch.",
        "Ví dụ trên là điều khiển bằng tay, nhưng khái niệm hoàn toàn giống với điều khiển tự động — vốn "
        "cho độ chính xác cao hơn.",
    ]))

    b.append(h3("4.5.4 Kết hợp điều khiển phản hồi và điều khiển theo mô hình",
                "Combination of Feedback and Feedforward"))
    b.append(p("Ưu điểm của điều khiển phản hồi là tương đối đơn giản và có thể vẫn làm việc được khi xuất "
               "hiện nhiễu chưa biết. Điều khiển theo mô hình có ưu điểm đáp ứng nhanh hơn với nhiễu ở đầu "
               "vào, điều này có thể tiết kiệm đáng kể chi phí trong một vận hành quy mô lớn."))
    b.append(fig(8, F.fig_4_8(), "vi"))
    b.append(p("Nói chung, điều khiển quá trình công nghiệp tốt nhất đạt được khi kết hợp cả vòng hở lẫn "
               "vòng kín. Nếu một mô hình feedforward không hoàn hảo sửa được 90 % nhiễu ngay khi nó xảy ra, "
               "và 10 % còn lại do vòng phản hồi tạo ra độ lệch bù tiếp, thì phần feedforward không bị đẩy "
               "quá khả năng của nó, tải cho vòng phản hồi giảm đi, và đạt được điều khiển chặt hơn nhiều."))
    b.append(quote(
        "Thời gian chết là kẻ thù tồi tệ nhất của điều khiển tốt, và mọi nỗ lực nên dồn vào việc giảm "
        "thiểu nó.",
        "Altmann, Ch.4 — Dead Time Processes"))

    # ---------------------------------------------------------------- 4.6
    b.append(h2("4.6 Quá trình có thời gian chết", "Dead Time Processes"))
    b.append(p("Ở những quá trình có chuyển động khối lượng, thời gian chết là yếu tố đáng kể trong động học "
               "của quá trình. Đó là độ trễ trong đáp ứng của quá trình sau khi một biến bị thay đổi, và "
               "trong suốt khoảng trễ đó không có thông tin nào về trạng thái mới của quá trình. Nó còn được "
               "gọi là độ trễ vận chuyển (transportation lag) hay độ trễ thời gian."))
    b.append(p("Mọi đường đáp ứng của quá trình đều bị dịch sang phải khi quá trình có thời gian chết. Khi "
               "thời gian chết đã qua, quá trình bắt đầu đáp ứng với tốc độ đặc trưng của nó, gọi là độ nhạy "
               "của quá trình."))
    b.append(fig(9, F.fig_4_9(), "vi"))

    b.append(h3("4.6.1 Giảm thời gian chết", "Reduction of Dead Time"))
    b.append(p("Mục tiêu của điều khiển tốt là giảm thiểu thời gian chết, và giảm thiểu tỉ số giữa thời gian "
               "chết và hằng số thời gian. Tỉ số này càng lớn thì khả năng hệ điều khiển làm việc đúng càng "
               "thấp."))
    b.append(p("Có thể giảm thời gian chết bằng cách giảm các độ trễ vận chuyển: tăng tốc độ bơm hoặc khuấy "
               "trộn, giảm khoảng cách giữa thiết bị đo và quá trình, v.v."))

    b.append(h3("4.6.2 Ảnh hưởng của thời gian chết lên các chế độ P, I, D và thuật toán lấy mẫu – giữ",
                "Dead Time Effects on P, I and D Modes and Sample-and-Hold Algorithms"))
    b.append(p("Nếu bản chất của quá trình là thời gian chết của vòng lớn hơn hằng số thời gian của nó, thì "
               "điều khiển PID truyền thống khó có thể làm việc, và người ta dùng điều khiển lấy mẫu – giữ. "
               "Dạng điều khiển này dựa trên việc bật bộ điều khiển để nó thực hiện những chỉnh định định "
               "kỳ, rồi chuyển đầu ra sang trạng thái giữ và chờ hết thời gian chết của quá trình trước khi "
               "bật lại đầu ra bộ điều khiển. Các thuật toán dùng vẫn giống hệt thuật toán điều khiển quá "
               "trình thông thường, chỉ khác là chúng chỉ được bật trong những khoảng thời gian ngắn."))
    b.append(fig(10, F.fig_4_10(), "vi"))
    b.append(p("Vấn đề duy nhất là bộ điều khiển có ít thời gian chỉnh định hơn nhiều, nên nó phải làm "
               "nhanh hơn. Điều đó có nghĩa là thông số tích phân phải được tăng lên tỉ lệ với mức giảm thời "
               "gian mà vòng ở chế độ tự động."))

    # ---------------------------------------------------------------- 4.7
    b.append(h2("4.7 Đáp ứng của quá trình", "Process Responses"))
    b.append(p("Đáp ứng động học của một quá trình thường được đặc trưng bằng ba tham số: hệ số khuếch đại "
               "của quá trình, thời gian chết và độ trễ (hằng số thời gian) của quá trình."))
    b.append(fig(11, F.fig_4_11(), "vi"))

    b.append(h3("4.7.1 Hệ số khuếch đại của quá trình", "Response Process Gain"))
    b.append(p("Hệ số khuếch đại của quá trình là tỉ số giữa thay đổi ở đầu ra (sau khi đã ổn định ở trạng "
               "thái mới) và thay đổi ở đầu vào — tức tỉ số giữa thay đổi của biến quá trình và thay đổi của "
               "biến điều khiển. Nó còn được gọi là độ nhạy của quá trình, vì nó mô tả mức độ mà quá trình "
               "đáp ứng với một đầu vào."))
    b.append(eq("K<sub>P</sub> = ΔPV / ΔMV = K<sub>S</sub> × K<sub>C</sub> × K<sub>V</sub>", "4.2"))
    b.append(p("Một quá trình chậm là quá trình có hệ số khuếch đại thấp, nơi phải mất rất lâu mới tạo ra "
               "một thay đổi nhỏ ở MV. Ví dụ là hệ sưởi trong nhà: phải mất một thời gian dài để nhiệt tích "
               "tụ đủ làm nhiệt độ phòng tăng chút ít. Với quá trình như vậy nên dùng bộ điều khiển có hệ số "
               "khuếch đại cao."))
    b.append(p("Một quá trình nhanh có hệ số khuếch đại cao, nghĩa là MV tăng nhanh. Điều này xảy ra ở các hệ "
               "như quá trình lưu lượng, hay quá trình pH gần điểm trung tính — nơi chỉ một giọt thuốc thử "
               "cũng gây thay đổi lớn về pH. Với quá trình như vậy cần bộ điều khiển có hệ số khuếch đại "
               "thấp."))
    b.append(p("Xét từ góc độ bộ điều khiển, hệ số khuếch đại của quá trình gồm ba thành phần nhân với nhau: "
               "hệ số khuếch đại của cảm biến đo (K<sub>S</sub>), của bản thân quá trình (K<sub>C</sub>) và "
               "của phần tử mà PV hoặc đầu ra bộ điều khiển tác động vào (K<sub>V</sub>)."))

    b.append(h3("4.7.2 Thời gian chết của đáp ứng", "Response Dead Time"))
    b.append(p("Thời gian chết (L) là khoảng trễ giữa lúc biến điều khiển thay đổi và lúc biến quá trình "
               "thay đổi thấy được. Thời gian chết có ở hầu hết quá trình vì rất ít, nếu không muốn nói là "
               "không có, sự kiện thực tế nào là tức thời. Một ví dụ đơn giản là hệ nước nóng: khi mở vòi "
               "nóng, sẽ có một khoảng trễ nhất định để nước nóng từ bình chạy dọc đường ống tới vòi. Đó "
               "chính là thời gian chết."))

    b.append(h3("4.7.3 Độ trễ của đáp ứng", "Response Process Lag"))
    b.append(p("Độ trễ của quá trình (T) gây ra bởi quán tính của hệ và ảnh hưởng tới tốc độ mà biến quá "
               "trình đáp ứng với một thay đổi của biến điều khiển. Nó tương đương với hằng số thời gian: "
               "sau một khoảng T kể từ khi bắt đầu đáp ứng, PV đã đi được 63,2 % quãng đường tới giá trị "
               "cuối cùng."))

    # ---------------------------------------------------------------- 4.8
    b.append(h2("4.8 Vùng chết", "Dead Zone"))
    b.append(p("Trong phần lớn ứng dụng thực tế, có một dải hẹp — do ma sát cơ khí hoặc do hồ quang ở tiếp "
               "điểm điện — mà sai lệch phải vượt qua trước khi có chuyển mạch. Dải này có thể được gọi là "
               "vùng chết, khe vi sai (differential gap) hay vùng trung tính."))
    b.append(p("Kích thước vùng chết thường là 0,5 % đến 2 % toàn dải dao động của PV, và nó nằm đối xứng "
               "qua điểm đặt. Khi PV nằm trong vùng chết thì không có tác động điều khiển nào, vì vậy sự có "
               "mặt của nó thường là điều mong muốn để giảm dao động chu kỳ của quá trình. Một vấn đề của "
               "điều khiển đóng – ngắt là mài mòn phần tử điều khiển; mài mòn giảm khi dải dao động của quá "
               "trình tăng lên và do đó tần số đóng cắt giảm đi."))
    b.append(table(
        ["Đại lượng", "Ký hiệu", "Đơn vị", "Ảnh hưởng tới điều khiển"],
        [["Hệ số khuếch đại", "K<sub>P</sub>", "—", "K cao: đáp ứng mạnh, dễ mất ổn định; K thấp: chậm, sai lệch lớn"],
         ["Thời gian chết", "L", "giây", "Càng lớn so với T thì càng khó điều khiển; PID có thể thất bại"],
         ["Hằng số thời gian", "T", "giây", "Quán tính của quá trình; T nhỏ thì đáp ứng nhanh"],
         ["Tỉ số L/T", "L/T", "—", "Chỉ số quyết định: L/T &lt; 1 mới nên dùng PID thường"],
         ["Vùng chết", "—", "% dải", "Giảm đóng cắt nhưng tạo sai lệch tĩnh không thể khử"]],
        "Bảng 4-2 · Bốn đại lượng quyết định độ khó của một vòng điều khiển. Trong thực tế, người ta thường "
        "chỉ nhìn vào tỉ số L/T để quyết định có dùng PID hay không."))

    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản gốc kết thúc chương bằng Bài thực hành 1 (một vòng điều khiển "
        "lưu lượng đơn giản trên phần mềm mô phỏng). Bài thực hành không được dịch vì gắn với phần mềm cụ "
        "thể của nhà xuất bản; sinh viên có thể thay bằng bất kỳ bộ mô phỏng vòng kín nào, miễn là quan sát "
        "đủ bốn hiện tượng: đáp ứng bậc thang, ảnh hưởng của K, ảnh hưởng của L và ảnh hưởng của vùng chết."))
    return "\n".join(b)


def body_en():
    b = []
    b.append(lead(
        "Chapter 3 dealt with the final control element; this chapter deals with the decision taken before "
        "the signal reaches it. Four strategies cover almost everything in practice — on-off, modulating, "
        "open loop and closed loop — and each is right only inside a particular range of conditions. The "
        "chapter closes with the two quantities that decide the fate of every loop: dead time and dead "
        "zone."))

    b.append(h2("On-off control: crude, cheap, and hard to beat"))
    b.append(p("A switch is the oldest controller there is. It never holds the process variable at the set "
               "point; it makes the variable oscillate about it, inside a band set by the hysteresis of the "
               "switch and by the thermal inertia of the plant. That sounds like a defect until you compare "
               "the cost: an on-off controller needs no model, no tuning, no valve and no transmitter "
               "calibration, and it cannot go unstable. For a domestic boiler, a refrigerator or a sump "
               "pump, a swing of one degree is entirely acceptable and a PID loop would be an expensive way "
               "of achieving nothing more."))
    b.append(p("The design decision is therefore not “which is better” but “how tight does the band have to "
               "be”. Once the answer is tighter than the switching differential can deliver, on-off is out "
               "and modulating control begins."))

    b.append(h2("Open loop: fast, and blind"))
    b.append(p("Feedforward control measures the disturbance and acts before the process variable has moved "
               "at all. That is its whole advantage: the correction arrives at the same time as the upset, "
               "not one dead time later. Its whole weakness is that nothing checks the result. A perfect "
               "model gives perfect correction; a model that is 10 % wrong leaves a 10 % error that nothing "
               "will ever remove."))
    b.append(p("This is why pure feedforward is rare and hybrid control is normal. The industrial rule of "
               "thumb is that feedforward should carry the bulk of the correction — 80 to 90 % — and the "
               "feedback loop should be left with only the residue. Sized that way, neither loop is asked to "
               "do more than it is good at: the feedforward branch is not pushed beyond the accuracy of its "
               "model, and the feedback branch is not asked to fight a disturbance it would only see a dead "
               "time too late."))

    b.append(h2("Direct or reverse: one question, asked once"))
    b.append(p("Every loop has a sign, and getting it wrong is the most common commissioning error in the "
               "trade. The question is not “what kind of valve is this” but “when the measurement rises, "
               "what must the output do to bring it back”. If the answer is open more, the controller is "
               "direct acting; if it is close more, the controller is reverse acting. A tank whose level is "
               "held by the outlet valve is direct acting — more level, more drain. The same tank held by "
               "the inlet valve is reverse acting — more level, less fill."))
    b.append(p("The P, I and D terms do not care which convention is used, because changing PV − SP into "
               "SP − PV only changes the sign of the error, and the sign can be absorbed anywhere in the "
               "chain. What cannot be absorbed is getting it wrong: a loop with the wrong sign is a "
               "positive-feedback amplifier, and it will either saturate or oscillate the moment it is put "
               "in automatic."))

    b.append(h2("Dead time is the enemy"))
    b.append(p("Dead time is not lag. Lag is inertia: the process starts responding at once and approaches "
               "the new value exponentially. Dead time is silence: the process does not respond at all, and "
               "the controller has no information about whether its last move was right, too small or far "
               "too large. A loop can tolerate a large lag; it cannot tolerate a large dead time, because "
               "every correction is applied blind and the controller ends up reacting to a state of the "
               "plant that no longer exists."))
    b.append(p("The number that matters is the ratio L/T, not either quantity alone. Below about 0.5 a "
               "conventional PID will do everything asked of it. Around 1 the loop becomes sluggish and "
               "detuned, and the achievable performance collapses quickly beyond that. When L exceeds T, "
               "the standard remedy is sample-and-hold: enable the controller for short windows, freeze the "
               "output in between, and let the process finish responding before looking again. The "
               "algorithms are the same; only the integral setting has to be raised, because the controller "
               "is in automatic for a fraction of the time."))

    b.append(h2("What the three parameters actually describe"))
    b.append(p("A process response curve carries three numbers, and every tuning method in the rest of the "
               "book is built on them. The gain K tells you how far the variable will travel for a given "
               "move of the valve — and, just as importantly, whether the plant is fast and twitchy (high "
               "K, flow and pH loops) or slow and stubborn (low K, furnaces and heated rooms). The dead time "
               "L tells you how long you must wait before you are allowed to learn anything. The lag T tells "
               "you how fast the variable moves once it starts."))
    b.append(p("The dead zone is the fourth, and the one most often forgotten. It is deliberately built into "
               "on-off controllers to stop them chattering, and it is accidentally built into every "
               "mechanical linkage as friction and backlash. Either way it produces a standing error that no "
               "amount of integral action can remove, because inside the band the controller is not being "
               "told that anything is wrong."))
    return "\n".join(b)
