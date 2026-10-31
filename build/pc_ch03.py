# -*- coding: utf-8 -*-
"""Practical Process Control — Chapter 3, Basic Principles of Control Valves
and Actuators (Wolfgang Altmann, IDC Technologies)."""
import pcfig as F
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul)

PAGES_SRC = 40
BYLINE = "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Van điều khiển (control valve)</em> — phần tử chấp hành cuối, nhận tín hiệu từ bộ điều khiển và "
            "định lượng dòng chảy. · <em>Đặc tuyến bản chất (inherent characteristic)</em> — quan hệ giữa phần "
            "trăm hành trình và phần trăm lưu lượng khi độ chênh áp trên van không đổi. · "
            "<em>Dải điều chỉnh (rangeability)</em> — tỉ số giữa lưu lượng cực đại và lưu lượng nhỏ nhất còn "
            "điều khiển được. · <em>Hệ số méo dạng DC (distortion coefficient)</em> — tỉ lệ tổn thất áp suất "
            "trên van so với tổng tổn thất của hệ khi lưu lượng cực đại. · "
            "<em>Bộ định vị (positioner)</em> — bộ điều khiển tỉ lệ hệ số khuếch đại cao, khép vòng tại chỗ "
            "quanh vị trí trục van. · <em>C<sub>V</sub></em> — hệ số lưu lượng của van theo định nghĩa của "
            "hãng sản xuất. Tiêu đề mỗi mục giữ nguyên bản tiếng Anh trong ngoặc để tiện đối chiếu với bản gốc.")
    return note(
        "<b>Key terms.</b> <em>Control valve</em> — the final control element that converts the controller "
        "output into a throttled flow. · <em>Inherent characteristic</em> — flow versus travel at constant "
        "valve pressure drop. · <em>Rangeability</em> — maximum to minimum controllable flow. · "
        "<em>Distortion coefficient DC</em> — the share of the total system pressure drop that appears across "
        "the valve at maximum flow. · <em>Positioner</em> — a local high-gain proportional loop closed around "
        "stem position.")


def body_vi():
    b = []
    b.append(lead(
        "Trong hầu hết hệ điều khiển quá trình, phần tử chấp hành cuối — thứ nhận tín hiệu ra của bộ điều "
        "khiển — là một loại van nào đó. Van là nơi duy nhất trong vòng mà năng lượng cơ học thực sự được "
        "điều tiết, và cũng là nơi tập trung nhiều phi tuyến nhất: đặc tuyến, ma sát, trễ, méo dạng do lắp "
        "đặt. Chương này đi qua tám họ van thông dụng, ba khái niệm phải hiểu để chọn được van (đặc tuyến, "
        "dải điều chỉnh, chọn cỡ) và bốn họ cơ cấu chấp hành."))

    b.append(h2("3.1 Mục tiêu", "Objectives"))
    b.append(p("Chương này nhằm ôn lại các kiểu và nguyên lý hoạt động cơ bản của van điều khiển quá trình, "
               "cùng hệ cơ cấu chấp hành và bộ định vị đi kèm. Sau khi học xong chương, sinh viên có thể:"))
    b.append(ul([
        "Liệt kê các kiểu van điều khiển quá trình thông dụng, mô tả vắn tắt thiết kế và kết cấu cơ bản của chúng;",
        "Giải thích ý nghĩa của <i>đặc tuyến</i>, <i>dải điều chỉnh</i> và <i>chọn cỡ van</i>;",
        "Mô tả các kiểu cơ cấu chấp hành thường gặp trong hệ điều khiển quá trình và liệt kê ứng dụng của chúng."]))

    # ------------------------------------------------------------- 3.2
    b.append(h2("3.2 Tổng quan tám loại van điều khiển cơ bản nhất", "An Overview of Eight Basic Valve Types"))
    b.append(p("Chương này giới thiệu tám kiểu van điều khiển thông dụng nhất, các thiết bị tiết lưu dòng và "
               "dải cơ cấu chấp hành cơ bản dùng để điều khiển chúng. Các mục 3.2.1 đến 3.2.8 mô tả từng kiểu "
               "van: tổng quan và mô tả chung, các biến thể trong dải sản phẩm của nhà sản xuất, kích cỡ, áp "
               "suất thiết kế, dải nhiệt độ và dải điều chỉnh. Những thuộc tính hay công dụng đặc biệt của "
               "van cũng được nêu. Mục 3.2.9 giới thiệu một số kiểu van ít gặp hơn cùng thiết kế và công dụng "
               "của chúng."))

    # 3.2.1
    b.append(h3("3.2.1 Van bi", "Ball Valves"))
    b.append(p("Van bi quay, từng được coi chỉ là van đóng–mở, nay được dùng khá rộng rãi như một thiết bị "
               "điều chỉnh lưu lượng. Ưu điểm gồm giá và khối lượng thấp hơn, khả năng lưu lượng lớn, đóng "
               "kín chắc và các thiết kế chịu được cháy. Van bi có một nút hình cầu điều khiển dòng chảy qua "
               "thân van. Van bi và van kiểu lồng gần như tuyến tính nếu xét theo phần trăm lưu lượng hay C<sub>V</sub> "
               "theo phần trăm hành trình trục hoặc góc quay của bi. Ba kiểu van bi cơ bản:"))
    b.append(ul([
        "<b>Quy ước</b> — kiểu bi khoan lỗ, quay 1/4 vòng.",
        "<b>Có hình dạng</b> — bi cắt rãnh chữ V, chữ U, hoặc bi parabol.",
        "<b>Kiểu lồng</b> — định vị bi bằng một lồng so với đệm kín và cửa xả; dùng cho mục đích điều khiển."]))
    b.append(fig(1, F.fig_3_1()))
    b.append(h4("Kích cỡ và áp suất thiết kế"))
    b.append(ul([
        "1/2 in đến 42 in (12,5 mm đến 1,06 m) ở cấp ANSI 150; đến 12 in (300 mm) ở cấp ANSI 2500.",
        "Bi phân đoạn — 1 in đến 24 in (50 mm đến 600 mm) ở cấp ANSI 150, đến 16 in (400 mm) ở cấp ANSI 300.",
        "Áp suất đến 2500 psig (17 MPa)."]))
    b.append(h4("Nhiệt độ thiết kế"))
    b.append(ul(["Thay đổi theo thiết kế và vật liệu, điển hình −160 °C đến +310 °C.",
                 "Các thiết kế đặc biệt mở rộng dải này từ −180 °C đến trên +1000 °C."]))
    b.append(h4("Dải điều chỉnh"))
    b.append(p("Nói chung được công bố khoảng 50:1. Xem mục 3.3.3."))
    b.append(fig(2, F.fig_3_2()))
    b.append(p("Van bi có hình dạng với cửa parabol gần đặc tuyến phần trăm đều, còn đặc tuyến của van bi "
               "khoan thẳng và kiểu lồng gần tuyến tính hơn khi dùng cho nước. Với khí ở vận tốc tới hạn, "
               "đường đặc tuyến của van bi có hình dạng dịch về phía tuyến tính."))

    # 3.2.2
    b.append(h3("3.2.2 Van bướm", "Butterfly Valves"))
    b.append(p("Đây là một trong những kiểu van lâu đời nhất còn dùng, có từ thập niên 1920. Van hoạt động "
               "như một tấm chắn hoặc một van tiết lưu trong đường ống, gồm một đĩa quay quanh một trục "
               "đường kính. Như van bi, hành trình quay từ đóng hoàn toàn đến mở hoàn toàn là 90°. Vì đĩa có "
               "thể hoạt động như một cánh dạng khí động trong dòng chính mà nó đang điều khiển, phải cẩn "
               "thận bảo đảm rằng mọi mô-men tăng thêm đều được cơ cấu chấp hành hấp thụ."))
    b.append(h4("Các kiểu van bướm"))
    b.append(ul([
        "<b>Đa dụng, trục thẳng</b> — cánh, đĩa, lá hoặc nắp quay nhờ trục mà nó gắn vào.",
        "<b>Van bướm hiệu năng cao (HPBV), trục lệch tâm</b> — thiết kế này kết hợp đóng kín chắc, mô-men "
        "vận hành giảm và khả năng tiết lưu tốt nhờ hình dạng đĩa đặc biệt xoay qua."]))
    b.append(h4("Kích cỡ và áp suất thiết kế"))
    b.append(ul(["Điển hình đến 48 in (51 mm đến 1,22 m).",
                 "Đã có thiết bị từ 0,75 in đến 200 in (19 mm đến 5 m)."]))
    b.append(h4("Nhiệt độ thiết kế"))
    b.append(ul(["Điển hình −260 °C đến +540 °C.",
                 "Thiết kế đặc biệt mở rộng dải này đến trên +1200 °C."]))
    b.append(fig(3, F.fig_3_3()))
    b.append(h4("Dải điều chỉnh"))
    b.append(p("Nói chung được công bố khoảng 50:1. Xem mục 3.3.4."))
    b.append(fig(4, F.fig_3_4()))
    b.append(p("Đặc tuyến lưu lượng của van bướm phụ thuộc vị trí trục (thẳng hay lệch tâm) và tỉ lệ kích "
               "thước trục so với cỡ van. Với mục đích tiết lưu, van thường chỉ được quay trong khoảng 0–60°."))

    # 3.2.3
    b.append(h3("3.2.3 Van số", "Digital Valves"))
    b.append(p("Van số gồm một nhóm phần tử van (cửa) lắp trong một ống góp chung. Mỗi phần tử có quan hệ "
               "nhị phân với phần tử kề: bắt đầu từ cửa nhỏ nhất, cửa tiếp theo có tiết diện gấp đôi cửa "
               "trước. Ưu điểm chính của kiểu van này là tốc độ cao, độ chính xác cao và dải điều chỉnh gần "
               "như không giới hạn. Nhược điểm lớn nhất là giá thành cao."))
    b.append(p("Kích cỡ: 3/4 in đến 10 in (19 mm đến 250 mm), cả kiểu thẳng dòng lẫn kiểu góc. Nhiệt độ thiết "
               "kế: từ cryogenic đến +670 °C. Giới hạn áp suất thiết kế: đến 10.000 psig (690 bar)."))
    b.append(fig(5, F.fig_3_5()))
    b.append(table(
        ["Số bit", "8", "10", "12", "14", "16"],
        [["Độ phân giải", "255:1", "1023:1", "4095:1", "16.383:1", "65.535:1"]],
        "Bảng 3-3a · Dải điều chỉnh của van số theo số bit điều khiển. Dải điều chỉnh bằng 2ⁿ − 1."))
    b.append(p("<b>Ứng dụng:</b> những nơi cần tốc độ cao (25 đến 100 ms), độ chính xác, dải điều chỉnh lớn "
               "và đóng kín chắc."))

    # 3.2.4
    b.append(h3("3.2.4 Van cầu", "Globe Valves"))
    b.append(p("Khoảng hai mươi năm trước, phần lớn van điều khiển tiết lưu là kiểu van cầu, đặc trưng bởi "
               "chuyển động thẳng của nút van và được dẫn động bằng cơ cấu màng – lò xo. Ưu điểm chính của "
               "van cầu gồm: kết cấu cơ cấu chấp hành màng – lò xo đơn giản, dải đặc tuyến rộng, ít xâm "
               "thực và ít ồn, nhiều thiết kế cho môi trường ăn mòn, mài mòn, nhiệt độ cao và áp suất cao, "
               "quan hệ tuyến tính giữa tín hiệu điều khiển và hành trình trục van, và vùng chết cũng như "
               "độ trễ tương đối nhỏ."))
    b.append(h4("Các kiểu van cầu"))
    b.append(ul(["Một cửa, nút van có hình dạng",
                 "Một cửa, dẫn hướng bằng lồng",
                 "Một cửa, thân chẻ",
                 "Hai cửa, nút van dẫn hướng đỉnh–đáy hoặc kiểu váy",
                 "Đĩa lệch tâm, van cầu quay",
                 "Kiểu góc",
                 "Ba cửa hoặc kiểu chữ Y"]))
    b.append(fig(6, F.fig_3_6()))
    b.append(h4("Đặc tuyến lưu lượng"))
    b.append(p("Đặc tuyến được quyết định bởi biên dạng nút van: (A) phần trăm đều, (B) tuyến tính, "
               "(C) mở nhanh."))
    b.append(h4("Kích cỡ và áp suất thiết kế"))
    b.append(ul(["Nói chung 1/2 in đến 14 in (20 mm đến 356 mm).",
                 "Cỡ lớn nhất của kiểu C là 6 in (152 mm).",
                 "Cỡ lớn nhất của kiểu E là 12 in (305 mm).",
                 "Cỡ lớn nhất của kiểu D là 16 in (406 mm).",
                 "Kiểu F (kiểu góc) đã được chế tạo tới 42 in (1,05 m)."]))
    b.append(p("Nói chung mọi cấp áp suất đều có đến ANSI 1500, riêng kiểu B và D đến ANSI 2500; kiểu C và E "
               "giới hạn ở ANSI 600."))
    b.append(h4("Nhiệt độ thiết kế"))
    b.append(ul(["Nói chung −200 °C đến +540 °C.",
                 "Kiểu B giới hạn ở nhiệt độ tối đa +400 °C.",
                 "Kiểu C làm việc được xuống tới −260 °C."]))
    b.append(h4("Dải điều chỉnh"))
    b.append(p("Nếu định nghĩa là vùng mà trong đó hệ số khuếch đại của van còn nằm trong 25% giá trị lý "
               "thuyết thì dải này hiếm khi vượt 20:1. Các nhà sản xuất dùng định nghĩa khác công bố 35:1. "
               "Xem mục 3.3.3."))
    b.append(fig(7, F.fig_3_7()))
    b.append(p("Đặc tuyến lý thuyết của van dịch chuyển theo cách lắp đặt. Các đường nét đứt phản ánh sự "
               "dịch chuyển đó trong một quá trình chủ yếu là ma sát, nơi 100% lưu lượng và 20% tổng tổn thất "
               "áp suất được gán cho van điều khiển."))

    # 3.2.5
    b.append(h3("3.2.5 Van kẹp", "Pinch Valves"))
    b.append(p("Kiểu van này được gọi là van kẹp hoặc van kẹp chặt tuỳ theo cấu hình ống mềm và cách ép ống. "
               "Chúng được chế tạo từ nhiều loại vật liệu như Teflon, PVC, Neoprene và polyurethane; mỗi "
               "loại elastomer hay nhựa có công dụng riêng."))
    b.append(p("Nếu được chọn cẩn thận, kiểu van này có nhiều ưu điểm: chịu mài mòn và ăn mòn cao, kết cấu "
               "không có đệm kín (packless), dải điều chỉnh lưu lượng hợp lý, dòng chảy êm, chi phí thay thế "
               "thấp và tuổi thọ dài hơn van kim loại ở những nơi có mài mòn và ăn mòn."))
    b.append(p("Tuy vậy, van cũng có giới hạn: ràng buộc về áp suất và nhiệt độ do bản chất vật liệu làm "
               "ống lót, và số lần vận hành (số lần gấp) mà một loại ống lót chịu được — dù nên coi tuổi thọ "
               "tối thiểu là trên 50.000 chu kỳ đóng–mở."))
    b.append(p("Kích cỡ: 1 đến 24 in (25 mm đến 610 mm); các thiết bị đặc biệt từ 0,1 in đến 72 in "
               "(2,5 mm đến 1,8 m). Áp suất thiết kế: nói chung đến ANSI 150, thiết bị đặc biệt đến ANSI 300. "
               "Nhiệt độ thiết kế: thay đổi theo thiết kế và vật liệu, điển hình −30 °C đến +200 °C. "
               "Dải điều chỉnh: nói chung được công bố từ 5:1 đến 10:1. Xem mục 3.3.3."))
    b.append(fig(8, F.fig_3_8()))
    b.append(fig(9, F.fig_3_9()))
    b.append(p("Bằng cách giảm tiết diện cửa hoặc làm ống lót có dạng hình nón, đặc tuyến trở nên tuyến tính "
               "hơn. Việc thêm một tiết lưu biến thiên trong ống lót tạo ra khả năng tiết lưu ở nửa trên của "
               "hành trình."))

    # 3.2.6
    b.append(h3("3.2.6 Van nút", "Plug Valves"))
    b.append(p("Van nút có lẽ là kiểu van lâu đời nhất còn tồn tại, từng được dùng trong hệ thống phân phối "
               "nước của La Mã cổ đại và có thể ra đời trước cả van bướm."))
    b.append(p("Van gồm một xy-lanh đứng hình côn có cửa hoặc rãnh dẫn dòng nằm ngang, lắp vào khoang của "
               "thân van; nhờ độ côn và hệ thống bôi trơn, van gần như không rò rỉ với cả khí lẫn chất lỏng. "
               "Một ứng dụng rất phổ biến của kiểu van này là chiết bia từ thùng. Van cho khả năng đóng mở "
               "nhanh với độ kín chắc chắn ở áp suất làm việc từ chân không đến 10.000 psig (70 MPa). Van "
               "dùng được cho chất lỏng, khí và bùn không mài mòn; kiểu lệch tâm có thể có nút nâng dùng cho "
               "chất lỏng dính. Như van bướm và van bi, van nút vận hành qua một cơ cấu chấp hành có chuyển "
               "động góc 90°."))
    b.append(p("Kích cỡ: 1/2 in đến 36 in (12,5 mm đến 960 mm)."))
    b.append(h4("Các kiểu"))
    b.append(ul(["<b>Cửa chữ V</b> — dùng cho cả đóng–mở lẫn tiết lưu, với nút hình V và thân có rãnh chữ V. "
                 "Lý tưởng cho vật liệu dạng sợi hoặc nhớt.",
                 "Các thiết kế ba, bốn và năm cửa hoặc nhiều cửa.",
                 "Kiểu làm kín chịu cháy."]))
    b.append(fig(10, F.fig_3_10()))
    b.append(p("Áp suất thiết kế: điển hình từ cấp ANSI 125 đến ANSI 300 và đến 720 psig (5 MPa); có thiết "
               "bị đặc biệt cho ANSI 2500. Nhiệt độ thiết kế: điển hình −70 °C đến +200 °C, thiết bị đặc "
               "biệt −160 °C đến +315 °C. Dải điều chỉnh: nói chung được công bố khoảng 20:1. Xem mục 3.3.3."))
    b.append(fig(11, F.fig_3_11()))

    # 3.2.7
    b.append(h3("3.2.7 Van màng Saunders", "Saunders Diaphragm Valves"))
    b.append(p("Van Saunders hay van màng đôi khi còn gọi là van tràn. Van hoạt động bằng cách đưa một màng "
               "mềm lại gần hoặc ra xa một gờ tràn. Có thể coi đây là van kẹp “một nửa”, vì chỉ dùng một "
               "màng ngăn chuyển động so với gờ tràn cố định; do đó đặc tuyến lưu lượng của chúng tương tự "
               "nhau. Van Saunders thông thường có thân, xét theo mặt cắt bên, dạng chữ U ngược, với màng "
               "ngăn đóng cửa ở phía trên. Cũng có kiểu toàn dòng (full-bore): khi mở hoàn toàn, lòng van "
               "tròn đầy — một đặc điểm quan trọng cho việc cọ rửa bằng bàn chải cầu như yêu cầu trong công "
               "nghiệp thực phẩm. Cần lưu ý rằng có thể xảy ra hư hỏng cơ khí khi mở kiểu van này dưới chân "
               "không của quá trình."))
    b.append(p("Kích cỡ: 1/2 in đến 12 in (12,5 mm đến 300 mm); thiết bị đặc biệt chế tạo đến 20 in "
               "(500 mm). Các kiểu: tràn, toàn dòng, thẳng dòng, hai dải."))
    b.append(fig(12, F.fig_3_12()))
    b.append(p("Áp suất thiết kế theo cỡ: ≤ 4 in (100 mm) là 150 psig (10,3 bar); 6 in (150 mm) là 125 psig "
               "(8,6 bar); 8 in (200 mm) là 100 psig (6,9 bar); 10–12 in (250–300 mm) là 65 psig (4,5 bar). "
               "Nhiệt độ thiết kế: với hầu hết màng elastomer là −12 °C đến +65 °C; với màng PTFE là −34 °C "
               "đến +175 °C. Dải điều chỉnh: nói chung được công bố 10:1. Xem mục 3.3.3."))
    b.append(fig(13, F.fig_3_13()))

    # 3.2.8
    b.append(h3("3.2.8 Van cổng trượt", "Sliding Gate Valves"))
    b.append(p("Trong kiểu van này, lưu lượng được điều khiển bằng cách trượt một tấm có lỗ qua một tấm cố "
               "định — thường đặt vuông góc 90° với đường dòng — cũng có lỗ tương ứng. Các lỗ có thể tròn, "
               "hoặc được tạo hình để định hình đặc tuyến lưu lượng của van. Van đôi khi được dùng trong "
               "điều khiển tự động nhưng thực ra không được coi là van điều khiển. Tuy vậy, kiểu van này làm "
               "việc được với áp suất đến 10.000 psig (70 MPa). Độ chính xác của van, đặc biệt trong điều "
               "khiển tỉ lệ, chỉ phụ thuộc vào độ chính xác của cơ cấu chấp hành được chọn."))
    b.append(h4("Các kiểu và kích cỡ"))
    b.append(table(
        ["Kiểu", "Mô tả", "Kích cỡ"],
        [["A — Cổng dao cắt", "Đóng–mở", "2 in đến 120 in (50 mm đến 3,0 m)"],
         ["B — Chèn chữ V", "Tiết lưu", "1/2 đến 24 in (12 mm đến 600 mm)"],
         ["C — Tấm và đĩa (nhiều lỗ)", "Tiết lưu", "1/2 in đến 6 in (12 mm đến 150 mm)"],
         ["D — Đĩa định vị", "Tiết lưu", "1 in và 2 in (25 mm và 50 mm)"]],
        "Bảng 3-3b · Các kiểu van cổng trượt, công dụng và dải kích cỡ."))
    b.append(fig(14, F.fig_3_14()))
    b.append(p("Áp suất thiết kế: kiểu A và B đến ANSI 150; kiểu C đến ANSI 300; kiểu D đến 10.000 psig "
               "(70 MPa). Nhiệt độ thiết kế: kiểu A và B từ cryogenic đến 260 °C; kiểu C và D từ −30 °C đến "
               "+600 °C. Dải điều chỉnh: kiểu A là 10:1, kiểu B là 20:1, kiểu C được công bố tới 50:1. Xem "
               "mục 3.3.3."))
    b.append(fig(15, F.fig_3_15()))

    # 3.2.9
    b.append(h3("3.2.9 Các thiết kế van đặc biệt", "Special Valve Designs"))
    b.append(p("Mục này đưa ra một số kiểu van ít gặp đang được dùng, vì với những tiến bộ kỹ thuật và yêu "
               "cầu khắt khe về độ chính xác hiện nay, các van này đang trở nên phổ biến hơn. Chúng không "
               "hoạt động theo kiểu tịnh tiến hay quay, mà dùng các phương thức khác như dòng học (fluidics) "
               "hay áp suất tĩnh của dòng quá trình để tiết lưu."))
    b.append(h4("Van nút cân bằng động"))
    b.append(p("Họ van này dùng ở nơi không có nguồn năng lượng ngoài để vận hành van, do đó áp suất tĩnh của "
               "dòng quá trình được dùng để tiết lưu. Áp suất thượng nguồn (áp suất ngược) đẩy nút van thắng "
               "lực lò xo hồi vị. Sự thay đổi áp suất cấp ảnh hưởng tới vị trí nút van so với sức căng lò "
               "xo. Việc điều khiển được thực hiện bằng một cụm van thí điểm kiểu poppet."))
    b.append(fig(16, F.fig_3_16()))
    b.append(h4("Van thẳng dòng kiểu xy-lanh điều khiển bằng màng"))
    b.append(p("Van này dùng cho khí áp suất cao nhờ mức rung, rối và ồn thấp. Nó gồm một màng ít nếp gấp "
               "để làm kín tích cực. Với cỡ 2 in (50 mm), có thể đạt áp suất vào 1400 MPa và áp suất ra "
               "600 MPa."))
    b.append(fig(17, F.fig_3_17()))
    b.append(h4("Van thẳng dòng có phần tử giãn nở"))
    b.append(p("Dòng khí chảy êm xuất hiện trong một van mà ở đó một xy-lanh cao su đặc được giãn ra hoặc "
               "co lại để thay đổi tiết diện của một khe vành khuyên. Việc điều khiển do một cơ cấu chấp "
               "hành hoặc piston thuỷ lực đảm nhiệm, dùng để thay đổi độ giãn của xy-lanh cao su. Van này "
               "điều khiển được áp suất đến 1200 psid."))
    b.append(p("Một phần tử giãn nở hay màng ngăn được căng trên một vòm có lỗ; nó chặn dòng của van khi áp "
               "suất phía trên màng lớn hơn áp suất đường ống. Bằng cách thay đổi áp suất bên ngoài phần tử "
               "từ bên ngoài, có thể điều khiển được dòng chính."))
    b.append(fig(18, F.fig_3_18()))
    b.append(h4("Van tương tác dòng"))
    b.append(p("Hiệu ứng Coanda — cơ sở của dòng học — được dùng trong kiểu van chuyển hướng này, có cỡ từ "
               "1/2 in đến 4 in (12,5 mm đến 100 mm). Van có tác động kiểu lật trạng thái, dùng để bẻ dòng "
               "xả từ cửa này sang cửa khác trong một cấu hình chữ Y, nhờ các cửa điều khiển bên đặt ở đáy "
               "chỗ giao chữ V của chữ Y. Kiểu van này có nhiều ứng dụng, đặc biệt trong công nghiệp hoá "
               "chất; khả năng bẻ dòng nhanh — thường dưới 100 ms — khiến nó là một thành viên quan trọng "
               "của họ van điều khiển."))
    b.append(fig(19, F.fig_3_19()))

    # ------------------------------------------------------------- 3.3
    b.append(h2("3.3 Hệ số khuếch đại, đặc tuyến, méo dạng và dải điều chỉnh",
                "Valve Gain, Characteristics, Distortion and Rangeability"))
    b.append(p("Đặc tuyến, dải điều chỉnh và hệ số khuếch đại của van điều khiển liên quan chặt chẽ với "
               "nhau; hiểu rõ chúng là điều kiện để nắm được “chân dung tính cách” của một van điều khiển "
               "quá trình."))

    b.append(h3("3.3.1 Hệ số khuếch đại của van và của vòng", "Valve and Loop Gain"))
    b.append(p("Hệ số khuếch đại được định nghĩa là tỉ số giữa thay đổi ở đầu ra và thay đổi ở đầu vào. Với "
               "một van <b>tuyến tính</b> (hệ số khuếch đại không đổi), hệ số khuếch đại của van (K<sub>V</sub>) "
               "được định nghĩa là phần trăm lưu lượng cực đại chia cho hành trình van tính theo phần trăm."))
    b.append(p("Hệ số khuếch đại vòng của một hệ điều khiển quá trình (K<sub>LOOP</sub>) về lý tưởng nên "
               "bằng 0,5 để có được tắt dần biên độ một phần tư — một trạng thái lý tưởng và rất ổn định. "
               "Hầu hết vòng điều khiển quá trình gồm tối thiểu bốn khâu tác động, mỗi khâu có ký hiệu riêng "
               "trong ngoặc vuông:"))
    b.append(ul([
        "Bộ điều khiển quá trình, chế độ P hay tỉ lệ [K<sub>C</sub>].",
        "Đầu ra bộ điều khiển dẫn động van điều khiển [K<sub>V</sub>].",
        "Van tác động lên quá trình [K<sub>P</sub>].",
        "Cảm biến/bộ chuyển đổi đo quá trình và đưa tín hiệu về bộ điều khiển [K<sub>S</sub>]."]))
    b.append(p("Để hệ ổn định, cả bốn thành phần phải có hệ số khuếch đại tuyến tính và tích các hệ số "
               "khuếch đại phải bằng 0,5 (ứng với tắt dần một phần tư):"))
    b.append(eq("K<sub>LOOP</sub> = K<sub>C</sub> × K<sub>V</sub> × K<sub>P</sub> × K<sub>S</sub> = 0,5", "3.1"))
    b.append(p("Khi dùng bộ điều khiển và cảm biến tuyến tính, và hệ số khuếch đại của quá trình cũng tuyến "
               "tính, thì cần một van tuyến tính (K<sub>V</sub> không đổi) để giữ hệ số khuếch đại tổng của "
               "vòng không đổi ở giá trị 0,5."))
    b.append(p("Tuy nhiên, nếu quá trình phi tuyến (K<sub>P</sub> thay đổi theo tải) trong khi K<sub>C</sub>, "
               "K<sub>V</sub> và K<sub>S</sub> không đổi, thì K<sub>LOOP</sub> cũng sẽ thay đổi quanh giá trị "
               "tối ưu 0,5, dẫn tới quá trình vận hành hoặc ì ạch hoặc mất ổn định. Cách duy nhất để giữ ổn "
               "định là để một thành phần khác trong vòng thay đổi hệ số khuếch đại của nó theo hướng và độ "
               "lớn ngược lại với thay đổi hệ số khuếch đại của quá trình. Thành phần đó có thể là hệ số "
               "khuếch đại của bộ điều khiển (K<sub>C</sub>) hoặc của van (K<sub>V</sub>); ở đây ta xét thay "
               "đổi của K<sub>V</sub>."))
    b.append(p("Khi hệ số khuếch đại của van thay đổi theo tải (lưu lượng), van được gọi tên theo đặc tuyến "
               "của nó:"))
    b.append(ul([
        "<b>PHẦN TRĂM ĐỀU</b> — K<sub>V</sub> tăng với tốc độ không đổi theo lưu lượng.",
        "<b>TỐC ĐỘ BIẾN THIÊN</b> — K<sub>V</sub> tăng theo một biên dạng: parabol, hyperbol, v.v.",
        "<b>MỞ NHANH</b> — K<sub>V</sub> giảm khi lưu lượng qua van tăng."]))
    b.append(p("Hệ số khuếch đại lý thuyết của van luôn thay đổi trong sử dụng thực tế nếu độ chênh áp trên "
               "van thay đổi theo tải. Đó là trường hợp của hầu hết hệ bơm, nơi chênh áp trên van giảm khi "
               "lưu lượng tăng, do đó làm giảm K<sub>V</sub>. Điều này có xu hướng dịch hệ số khuếch đại của "
               "van phần trăm đều về phía kiểu tuyến tính. Trong trường hợp đó, lắp một van phần trăm đều "
               "vào hệ thường giúp giữ hệ số khuếch đại của van được tuyến tính."))
    b.append(p("Đặc tuyến <i>bản chất</i> của van điều khiển mô tả quan hệ giữa đầu ra của bộ điều khiển (như "
               "cơ cấu chấp hành nhận được) và lưu lượng qua van, với giả thiết:"))
    b.append(ul(["Cơ cấu chấp hành tuyến tính (hành trình van tỉ lệ với đầu ra bộ điều khiển).",
                 "Độ chênh áp ΔP trên van không đổi.",
                 "Dòng quá trình không chớp hơi (flashing), không bị xâm thực và không ở vận tốc âm."]))
    b.append(fig(20, F.fig_3_20()))
    b.append(p("Chọn đặc tuyến van có thể là một thủ tục dài dòng và phức tạp. Driskell đã rút ra một quy "
               "tắc ngón tay cái để chọn đặc tuyến cho những vòng thông dụng nhất:"))
    b.append(table(
        ["Dịch vụ yêu cầu", "ΔP van &lt; 2:1", "ΔP van &gt; 2:1 và &lt; 5:1"],
        [["Lưu lượng kiểu lỗ", "Mở nhanh", "Tuyến tính"],
         ["Lưu lượng tuyến tính", "Tuyến tính", "Phần trăm đều"],
         ["Mức", "Tuyến tính", "Phần trăm đều"],
         ["Áp suất khí", "Tuyến tính", "Phần trăm đều"],
         ["Áp suất chất lỏng", "Phần trăm đều", "Phần trăm đều"]],
        "Bảng 3-1 · Danh mục đặc tuyến van thông dụng theo ứng dụng (quy tắc Driskell)."))
    b.append(p("Trong nhiều trường hợp, việc chọn đặc tuyến van ít ảnh hưởng tới các tham số của vòng, và "
               "gần như kiểu nào cũng chấp nhận được với:"))
    b.append(ul([
        "Quá trình có hằng số thời gian ngắn, như điều khiển lưu lượng, phần lớn vòng điều khiển áp suất và "
        "điều khiển nhiệt độ khi trộn dòng nóng với dòng lạnh;",
        "Vòng điều khiển do bộ điều khiển có dải tỉ lệ hẹp (hệ số khuếch đại cao) vận hành, như phần lớn bộ "
        "điều áp;",
        "Quá trình có biến thiên tải dưới 2:1."]))

    b.append(h3("3.3.2 Méo dạng của van", "Valve Distortion"))
    b.append(p("Dòng chảy qua van chịu tổn thất ma sát; hậu quả được trình bày trên Hình 3-21. Từ các đường "
               "cong này có thể thấy tiêu chí lắp đặt có thể ảnh hưởng đáng kể tới đặc tuyến lưu lượng và "
               "dải điều chỉnh của van."))
    b.append(fig(21, F.fig_3_21()))
    b.append(p("Van tuyến tính có hệ số khuếch đại không đổi ở mọi lưu lượng, còn van phần trăm đều có hệ số "
               "khuếch đại tỉ lệ trực tiếp với lưu lượng."))
    b.append(p("Do đó, nếu một vòng có xu hướng dao động ở lưu lượng thấp (nghĩa là hệ số khuếch đại vòng "
               "≥ 1) và ì ạch ở lưu lượng cao (hệ số khuếch đại &lt; 0,25), nên chuyển từ van tuyến tính sang "
               "van phần trăm đều. Ngược lại, nếu dao động xuất hiện ở lưu lượng cao và hiệu năng ì ạch ở "
               "lưu lượng thấp, hãy chuyển từ van phần trăm đều sang van tuyến tính."))

    b.append(h3("3.3.3 Dải điều chỉnh của van", "Valve Rangeability"))
    b.append(p("Theo truyền thống, dải điều chỉnh được định nghĩa là tỉ số giữa lưu lượng “điều khiển được” "
               "nhỏ nhất và lớn nhất qua van. Thuật ngữ “lưu lượng nhỏ nhất” (F<sub>MIN</sub>) được định "
               "nghĩa là lưu lượng mà dưới đó van có xu hướng đóng hoàn toàn. Với định nghĩa này, các nhà "
               "sản xuất thường công bố:"))
    b.append(ul(["50:1 với van phần trăm đều.",
                 "33:1 với van tuyến tính.",
                 "20:1 với van mở nhanh."]))
    b.append(p("Điều đó cho thấy lưu lượng qua các van này có thể được điều khiển xuống tới 2%, 3% và 5% "
               "C<sub>V</sub> định mức tương ứng. Tuy nhiên, trên Hình 3-21 có thể thấy lưu lượng điều khiển "
               "được nhỏ nhất tăng lên khi hệ số méo dạng (DC) giảm."))
    b.append(p("Vì ở độ mở nhỏ nhất, tổn thất áp suất qua van ΔP là cực đại, van sẽ cho qua lưu lượng nhiều "
               "hơn một cách tương ứng. Dải điều chỉnh nên được tính bằng tỉ số giữa C<sub>V</sub> cần thiết "
               "ở lưu lượng cực đại (tổn thất áp suất cực tiểu) và C<sub>V</sub> cần thiết ở lưu lượng cực "
               "tiểu (tổn thất áp suất cực đại)."))
    b.append(note(
        "<b>Vì sao hai định nghĩa cho hai con số khác nhau.</b> Định nghĩa truyền thống đo dải điều chỉnh "
        "trên một van đặt riêng lẻ, với chênh áp không đổi — tức là trên <i>đặc tuyến bản chất</i>. Định "
        "nghĩa thứ hai đo trên van đã lắp trong hệ, nơi chênh áp giảm khi lưu lượng tăng — tức là trên "
        "<i>đặc tuyến lắp đặt</i>. Chính vì thế một van được công bố 50:1 có thể chỉ còn 10:1 khi lắp vào "
        "một hệ có DC nhỏ. Khi đọc catalogue, luôn phải hỏi con số ấy ứng với DC nào."))

    # ------------------------------------------------------------- 3.4
    b.append(h2("3.4 Cơ cấu chấp hành của van điều khiển", "Control Valve Actuators"))
    b.append(p("Cơ cấu chấp hành là phần của cụm van đáp ứng tín hiệu ra của bộ điều khiển quá trình, gây ra "
               "một chuyển động cơ học, và chuyển động ấy làm thay đổi dòng chảy qua van."))
    b.append(p("Cơ cấu chấp hành phải thực hiện được hai chức năng cơ bản:"))
    b.append(ul([
        "Đáp ứng một tín hiệu bên ngoài và làm van chuyển động tương ứng; nếu chọn đúng, có thể tích hợp "
        "thêm các chức năng khác vào cụm này, ví dụ tác động an toàn mong muốn khi mất nguồn.",
        "Cung cấp giá đỡ (nếu cần) cho các phụ kiện như bộ định vị, công tắc hành trình, van điện từ và bộ "
        "điều khiển tại chỗ."]))
    b.append(p("Có năm dạng cơ cấu chấp hành cơ bản: số, điện, thuỷ lực, nam châm điện và khí nén. Bốn loại "
               "đầu có cách hoạt động và ứng dụng hoàn toàn khác loại cuối — cơ cấu khí nén."))

    b.append(h3("3.4.1 Cơ cấu số, điện, thuỷ lực và nam châm điện",
                "Digital, Electric, Hydraulic and Solenoid Actuators"))
    b.append(ol([
        "Kiểu số.",
        "Kiểu điện cơ: (2a) động cơ bước cho van cỡ nhỏ; (2b) động cơ đảo chiều kèm hộp giảm tốc cho van cỡ lớn.",
        "Kiểu điện–thuỷ lực (bơm được dẫn động bằng động cơ bước hoặc động cơ servo).",
        "Kiểu nam châm điện."]))
    b.append(h4("Nguồn năng lượng"))
    b.append(p("Điện hoặc điện–thuỷ lực."))
    b.append(h4("Kỹ thuật giảm tốc"))
    b.append(p("Bánh vít, bánh răng trụ, hoặc không dùng bánh răng."))
    b.append(h4("Dải mô-men"))
    b.append(ul(["0,5 đến 30 ft·lb (0,6 đến 40 N·m) với kiểu 2a.",
                 "1 đến 75.000 ft·lb (1,3 đến 100.000 N·m) với kiểu 2b."]))
    b.append(h4("Tốc độ quay"))
    b.append(p("Từ 5 đến 300 giây cho một chu kỳ mở hoặc đóng hoàn toàn."))
    b.append(h4("Dải lực đẩy tuyến tính"))
    b.append(ul(["Tối đa 500 lbf (225 kgf) từ cơ cấu kiểu 2a.",
                 "100 đến 10.000 lbf (45 đến 4.500 kgf) từ cơ cấu kiểu 2a cỡ lớn.",
                 "100.000 lbf (45.000 kgf) từ cơ cấu kiểu 3."]))
    b.append(h4("Tốc độ hành trình toàn phần"))
    b.append(ul(["Nam châm điện nhỏ có thể đóng trong 8 đến 12 ms.",
                 "Nam châm điện tiết lưu hành trình trong khoảng 1 giây.",
                 "Van dẫn động bằng động cơ điện cơ hành trình trong 5 đến 300 giây.",
                 "Cơ cấu điện–thuỷ lực thường dịch chuyển 0,25 in/s (6 mm/s)."]))
    b.append(p("Về bản chất, cơ cấu chấp hành phải tạo được mô-men lớn hơn để thắng lực cản khi mở một số "
               "kiểu van — thường gọi là lực bứt phá (breakaway force). Vận hành theo chiều ngược lại, tức "
               "đóng van, đôi khi cũng cần mô-men phụ để bảo đảm đệm kín ăn khớp chắc; tuy vậy vẫn cần một "
               "kiểu khớp ly hợp giữ bằng lò xo phòng trường hợp có vật lạ kẹt trong thân van."))
    b.append(p("Nhiều loại công tắc hành trình — từ công tắc lưỡi, hồng ngoại đến vi công tắc — có thể được "
               "gắn trong cụm cơ khí của cơ cấu chấp hành để báo hiệu và nhờ đó ngăn ngừa hiện tượng vượt "
               "hành trình và chuyển động quá mức."))

    b.append(h3("3.4.2 Cơ cấu chấp hành khí nén", "Pneumatic Actuators"))
    b.append(p("Cơ cấu chấp hành khí nén đáp ứng tín hiệu khí bằng cách đưa phần trong của van tới vị trí "
               "tiết lưu tương ứng. Có hai kiểu cơ bản: tuyến tính và quay."))
    b.append(h4("Các kiểu và ứng dụng"))
    b.append(table(
        ["Nhóm", "Ký hiệu", "Kiểu"],
        [["Tuyến tính", "a1", "Màng – lò xo"],
         ["Tuyến tính", "a2", "Piston"],
         ["Quay", "b1", "Xy-lanh có đòn bẩy scotch yoke"],
         ["Quay", "b2", "Xy-lanh có thanh răng – bánh răng"],
         ["Quay", "b3", "Xy-lanh đôi"],
         ["Quay", "b4", "Then hoa hoặc xoắn ốc"],
         ["Quay", "b5", "Cánh quay"],
         ["Quay", "b6", "Khí – thuỷ lực"],
         ["Quay", "b7", "Động cơ khí"],
         ["Quay", "b8", "Điện – khí nén"]],
        "Bảng 3-3c · Phân loại cơ cấu chấp hành khí nén."))
    b.append(p("Các cơ cấu trên áp dụng cho các cỡ van sau: kiểu a1 cho 0,5–8 in (12,5–200 mm); kiểu a2 cho "
               "0,5–16 in (12,5–400 mm); kiểu B cho 2–30 in (50–750 mm). Áp suất định mức cực đại: kiểu a1 "
               "là 60 psi (414 kPa), một số cao hơn; kiểu a2 là 150 psi (1035 kPa); kiểu B là 250 psi "
               "(1725 kPa). Diện tích màng/piston: kiểu a1 từ 25 đến 500 in² (0,016 đến 0,323 m²); kiểu a2 "
               "và B từ 10 đến 600 in² (0,006 đến 0,38 m²), đường kính trong 2 đến 44 in (50 mm đến 1,1 m), "
               "hành trình đến 24 in (0,61 m)."))
    b.append(p("Lực đẩy tuyến tính (lực trục): kiểu a1 từ 200 đến 45.000 lbf (100 đến 20.400 kgf); kiểu a2 "
               "từ 200 đến 32.000 lbf (100 đến 14.500 kgf); loại đặc biệt đến 186.000 lbf (84.000 kgf). Tốc "
               "độ hành trình toàn phần: kiểu a1 là 1 đến 5 giây; kiểu a2 là 0,33 đến 6,0 in/s "
               "(8 đến 150 mm/s)."))

    b.append(h3("3.4.3 Phương trình trạng thái ổn định", "The Steady State Equation"))
    b.append(p("Trong cơ cấu chấp hành khí nén kiểu màng – lò xo, vị trí trục van đạt được nhờ cân bằng lực "
               "trên trục. Xét Hình 3-22 (các lực trên van màng – lò xo), có thể rút ra phương trình sau từ "
               "tổng các lực, với chiều dương hướng xuống (chiều đóng) và dòng chảy từ trái sang phải:"))
    b.append(eq("P·A − K·X − P<sub>V</sub>·A<sub>V</sub> = 0", "3.2"))
    b.append(p("Với dòng chảy ngược, từ phải sang trái:"))
    b.append(eq("P·A − K·X + P<sub>V</sub>·A<sub>V</sub> = 0", "3.3"))
    b.append(p("Trường hợp ngược lại, khi trục chuyển động theo chiều âm hướng lên (chiều mở) và dòng chảy "
               "từ trái sang phải:"))
    b.append(eq("−P·A + K·X − P<sub>V</sub>·A<sub>V</sub> = 0", "3.4"))
    b.append(p("Với dòng chảy ngược, từ phải sang trái:"))
    b.append(eq("−P·A + K·X + P<sub>V</sub>·A<sub>V</sub> = 0", "3.5"))
    b.append(p("trong đó A là diện tích hiệu dụng của màng; A<sub>V</sub> là diện tích hiệu dụng của cửa van; "
               "K là độ cứng lò xo; P là áp suất màng; P<sub>V</sub> là độ chênh áp trên van ΔP; X là hành "
               "trình trục."))
    b.append(p("Các phương trình này là dạng đơn giản hoá vì chưa xét ma sát trong đệm kín trục van, trong "
               "dẫn hướng cơ cấu chấp hành và trong (các) dẫn hướng nút van, cũng chưa xét quán tính."))
    b.append(fig(22, F.fig_3_22()))
    b.append(fig(23, F.fig_3_23()))
    b.append(p("Hình 3-23 minh hoạ quan hệ giữa áp suất trên màng và lượng hành trình của trục van, cho thấy "
               "thêm một nguồn phi tuyến và méo dạng nữa."))
    b.append(table(
        ["Kiểu cơ cấu", "Ưu điểm", "Nhược điểm", "Ứng dụng"],
        [["Tuyến tính màng – lò xo", "Giá thấp; an toàn cơ khí; lực vừa; gọn; thiết kế đơn giản; điều khiển "
                                      "tốt (kèm hoặc không kèm thiết bị điều khiển)",
          "Tốc độ chậm; độ cứng thấp; không ổn định", "Van tuyến tính, thân 0,5–8 in"],
         ["Tuyến tính piston", "Giá thấp; lực vừa; gọn; thiết kế đơn giản; điều khiển tốt khi có thiết bị "
                               "điều khiển; hành trình dài",
          "Không an toàn cơ khí; tốc độ chậm; độ cứng thấp; không ổn định", "Van tuyến tính, thân 0,5–16 in"],
         ["Quay màng – lò xo", "Giá thấp; an toàn cơ khí; gọn; thiết kế đơn giản; dễ đảo chiều; điều khiển "
                               "tốt khi có thiết bị điều khiển",
          "Lực thấp trong chu kỳ lò xo; tốc độ chậm; không ổn định", "Van quay, thân 1–6 in"],
         ["Quay piston", "Giá thấp; lực vừa; cỡ từ nhỏ đến lớn; an toàn cơ khí; điều khiển tốt khi có thiết "
                         "bị điều khiển",
          "Tốc độ chậm; hành trình lò xo lớn", "Van quay, thân 1–24 in"]],
        "Bảng 3-3 · Đặc điểm của cơ cấu chấp hành khí nén: ưu nhược điểm và ứng dụng của bốn kiểu thông "
        "dụng nhất."))

    # ------------------------------------------------------------- 3.5
    b.append(h2("3.5 Bộ định vị van", "Control Valve Positioners"))
    b.append(p("Có lẽ phụ kiện quan trọng nhất cho việc điều khiển van là <i>bộ định vị</i>, đôi khi được gọi "
               "là “điện tử van thông minh”, nhiều loại trong đó do vi xử lý điều khiển."))
    b.append(p("Bộ định vị là một bộ điều khiển tỉ lệ có hệ số khuếch đại cao: nó đo vị trí trục van tới "
               "±0,1 mm, so sánh vị trí ấy với tín hiệu đặt — nên coi là đầu ra của bộ điều khiển quá trình "
               "chính — và hiệu chỉnh trên mọi tín hiệu sai lệch phát sinh. Hệ số khuếch đại vòng hở của "
               "các bộ định vị này nằm trong khoảng 10 đến 200, ứng với dải tỉ lệ từ 10% đến 0,5%, và chu kỳ "
               "dao động của chúng từ 0,3 đến 10 giây, tức đáp ứng tần số 3 đến 0,1 Hz. Nói cách khác, đó là "
               "một bộ điều khiển chỉ tỉ lệ, được chỉnh rất nhạy."))
    b.append(fig(24, F.fig_3_24()))
    b.append(p("Hệ STARPACK do Valtek chế tạo là ví dụ về một bộ định vị “đủ bộ”: nó không chỉ điều khiển và "
               "đo lưu lượng qua van mà còn đo áp suất thượng nguồn và hạ nguồn (do đó suy ra được chênh "
               "áp), vị trí trục và nhiệt độ. Ưu thế của nó là lưu được các “hồ sơ” của van để phần mềm hiệu "
               "chỉnh hoặc sửa đổi đặc tuyến lưu lượng."))

    b.append(h3("3.5.1 Khi nào KHÔNG nên dùng bộ định vị", "When NOT to use Positioners"))
    b.append(p("Cần nhớ rằng bộ định vị trở thành một phần hữu cơ của toàn bộ vòng điều khiển, rất giống bộ "
               "điều khiển thứ cấp trong một hệ nối tầng; do đó phải cẩn thận khi dùng chúng. Quy tắc ngón "
               "tay là hằng số thời gian của khâu tòng phải ngắn hơn 10 lần (hệ số khuếch đại vòng hở cao "
               "hơn 10 lần), và chu kỳ dao động của khâu tòng phải ngắn hơn 3 lần (đáp ứng tần số cao hơn "
               "3 lần) so với bộ điều khiển sơ cấp hay chủ."))

    # ------------------------------------------------------------- 3.6
    b.append(h2("3.6 Chọn cỡ van", "Valve Sizing"))
    b.append(p("Có nhiều phương pháp tính cỡ van, rất khác nhau và đôi khi rất phức tạp, vượt ra ngoài phạm "
               "vi tài liệu này. Tuy vậy, theo nguyên tắc, phải xác định và tính đến các yêu cầu C<sub>V</sub> "
               "cực tiểu và cực đại của van. Những yêu cầu như “khởi động quá trình”, “mọi chức năng bất "
               "thường của quá trình được yêu cầu”, và rất quan trọng là “các phản ứng cần thiết với mọi "
               "tình huống khẩn cấp” phải được tính đến trước, và van phải được chọn sao cho làm việc thoả "
               "đáng trong khoảng từ 0,8·C<sub>V,min</sub> đến 1,2·C<sub>V,max</sub>."))
    b.append(p("Nếu điều đó dẫn tới một dải điều chỉnh vượt quá khả năng của một van, thì phải dùng hai van "
               "trở lên. <b>Không</b> được dùng van điều khiển ngoài dải điều chỉnh đã công bố."))
    b.append(p("Cũng phải cẩn thận: khi cộng dồn mọi tổn thất áp suất có thể xảy ra trong một ứng dụng bơm có "
               "tốc độ không đổi, đừng lấy kết quả ấy áp thẳng cho van để hiệu chỉnh — làm vậy luôn dẫn tới "
               "việc chọn van <b>quá lớn</b>, và van sẽ làm việc gần như ở vị trí đóng trong phần lớn thời "
               "gian."))
    b.append(note(
        "<b>Quá lớn tệ hơn quá nhỏ.</b> Một van quá lớn không chỉ đắt hơn: nó còn buộc phải làm việc ở 5–10% "
        "hành trình, nơi đặc tuyến bị méo mạnh nhất, ma sát tĩnh chiếm tỉ trọng lớn nhất và hiện tượng xâm "
        "thực/ồn dễ xuất hiện nhất. Một van quá nhỏ chỉ đơn giản là không đủ lưu lượng ở đỉnh tải — hậu quả "
        "rõ ràng và dễ phát hiện hơn nhiều."))
    b.append(quote(
        "Van không phải một cái khoá có thể vặn đến bất kỳ đâu. Nó là một phần tử có hệ số khuếch đại riêng, "
        "và hệ số ấy thay đổi theo lưu lượng, theo chênh áp và theo cách bạn lắp nó.",
        "Wolfgang Altmann"))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "This chapter is a catalogue with an argument inside it. The catalogue is the eight valve families — "
        "ball, butterfly, digital, globe, pinch, plug, Saunders diaphragm, sliding gate — each with its sizes, "
        "pressure classes, temperature limits and rangeability. The argument is that none of those numbers "
        "means anything until you know the valve's gain, and the gain is the one property that the installation "
        "changes for you."))
    b.append(p(
        "Read it in that order. Sections 3.2.1–3.2.9 are reference material you will come back to; sections "
        "3.3 onwards are the part that decides whether a loop is stable."))

    b.append(h2("The eight families at a glance"))
    b.append(table(
        ["Family", "How it throttles", "Typical rangeability", "Where it wins"],
        [["Ball", "Rotating sphere with a port; V-notch or parabolic for characterising",
          "≈ 50:1", "Cheap, light, tight shut-off, fire-safe"],
         ["Butterfly", "Disc on a diametral or offset shaft", "≈ 50:1",
          "Large pipes, low cost, low torque when offset"],
         ["Digital", "Binary-weighted ports in a manifold", "2ⁿ − 1 (255:1 at 8 bit)",
          "25–100 ms stroking, huge range, tight shut-off"],
         ["Globe", "Plug moving linearly into a seat", "20:1 (35:1 claimed)",
          "Wide choice of trim, low cavitation and noise"],
         ["Pinch", "Rubber sleeve squeezed shut", "5:1 to 10:1",
          "Abrasive and corrosive slurries, packless"],
         ["Plug", "Tapered plug with a port, 90° turn", "≈ 20:1",
          "Ancient, leak-tight, good for viscous and fibrous"],
         ["Saunders", "Diaphragm against a weir", "10:1",
          "Slurries, food industry, full-bore cleaning"],
         ["Sliding gate", "Plate with a hole sliding past a fixed plate", "10:1 to 50:1",
          "High pressure up to 10,000 psig, simple"]],
        "Table 3.A · The eight families compared on the three numbers that decide a selection: how the flow "
        "is throttled, the rangeability the maker claims, and the application where the type is the right "
        "answer."))
    b.append(p(
        "Two entries deserve a warning. The digital valve's rangeability of 255:1 at eight bits is real, but "
        "it is bought with cost — roughly three times a single-port globe of the same size. And the "
        "rangeabilities in the third column are all <em>inherent</em> figures, measured on a bench with "
        "constant pressure drop; section 3.3.3 explains why the installed figure is usually much smaller."))

    b.append(h3("Ball"))
    b.append(p(
        "A sphere with a bore through it, turned a quarter turn. The plain port is a gate rather than a "
        "throttle: its characteristic is quick opening, and it is at its worst halfway through the stroke, "
        "where the opening is a pair of crescents and the flow area changes fastest. Cut a V-notch or a "
        "parabolic slot into the leading edge and the same body becomes a usable control valve — at the cost "
        "of the bubble-tight shut-off the plain port gave you."))
    b.append(fig(1, F.fig_3_1(), "en"))
    b.append(p(
        "The notch does more than soften the characteristic. On water the characterised trim tracks equal "
        "percentage closely; on gas at critical velocity the same trim drifts towards linear, because the "
        "flow is choked and the port area stops being the limiting quantity. That is the first reminder in "
        "this chapter that a characteristic belongs to the fluid as much as to the metal."))
    b.append(fig(2, F.fig_3_2(), "en"))

    b.append(h3("Butterfly"))
    b.append(p(
        "A disc on a shaft, and the only family that scales painlessly to a metre and a half of bore. At 0° "
        "the disc stands across the flow and seals; at 90° it lies parallel to the flow and the valve is wide "
        "open. Nothing about that geometry is linear, and the torque curve is worse than the flow curve."))
    b.append(fig(3, F.fig_3_3(), "en"))
    b.append(p(
        "Throttling is therefore confined to the first 60° or so of opening, where the disc still has "
        "authority and the actuator still has margin. Whether the shaft passes through the disc (aligned) or "
        "sits behind it (eccentric) changes both the characteristic and the torque, and so does the shaft "
        "diameter relative to the bore — which is why two butterfly valves of the same size from two makers "
        "can behave quite differently in the same line."))
    b.append(fig(4, F.fig_3_4(), "en"))

    b.append(h3("Digital"))
    b.append(p(
        "Not one orifice but a manifold of them, each element twice the area of its neighbour — 1, 2, 4, 8 "
        "and so on. Open the ports in binary order and eight on/off solenoids give 255 discrete positions. "
        "The characteristic is linear in port count by construction, rangeability is set by the smallest "
        "port, and because every element is either shut or open there is no stem to stick and no packing to "
        "leak. The cost is the solenoid count and the finite step at the bottom of the range."))
    b.append(fig(5, F.fig_3_5(), "en"))

    b.append(h3("Globe"))
    b.append(p(
        "The reference design against which the others are judged. A plug travels linearly into a seat, so "
        "the flow path turns twice and the body absorbs energy that would otherwise leave as noise or "
        "cavitation. Trim is interchangeable — contoured for equal percentage, drilled cage for low noise, "
        "multistage for a large pressure drop — which is why the family still covers applications that no "
        "other type can reach. The penalties are weight and permanent pressure loss."))
    b.append(fig(6, F.fig_3_6(), "en"))

    b.append(h3("Pinch"))
    b.append(p(
        "A rubber sleeve squeezed shut by air or by a bar. Nothing in the wetted path but the sleeve, so "
        "abrasive slurry and corrosive liquor see no metal and there is no packing to leak past. "
        "Rangeability is poor and the sleeve is a consumable, but on a slurry line the alternative is a valve "
        "that erodes itself out of calibration within months."))
    b.append(fig(8, F.fig_3_8(), "en"))
    b.append(p(
        "Reducing the port or coning the sleeve linearises what is otherwise a quick-opening characteristic, "
        "and a variable orifice inside the sleeve recovers throttling in the upper half of the stroke, where "
        "a plain sleeve has already passed full flow."))
    b.append(fig(9, F.fig_3_9(), "en"))

    b.append(h3("Plug"))
    b.append(p(
        "The oldest throttling geometry still in service: a tapered plug with a rectangular or round port, "
        "turned 90° in a matching body. The plug is held against its seat by the process pressure itself, so "
        "shut-off is tight and the valve is self-cleaning in viscous and fibrous service — the reason it "
        "survives in paper stock and heavy oil despite everything the ball valve does better."))
    b.append(fig(10, F.fig_3_10(), "en"))
    b.append(p(
        "The characteristic is whatever the port shape makes it: a round hole gives quick opening, a V gives "
        "something closer to linear. There is no trim to change, so the port shape is chosen at order time "
        "and cannot be revised later."))
    b.append(fig(11, F.fig_3_11(), "en"))

    b.append(h3("Saunders"))
    b.append(p(
        "A diaphragm clamped over a weir and pushed down by a compressor. The diaphragm isolates the whole "
        "mechanism from the fluid, the body is full-bore when open and drains completely, and the assembly "
        "comes apart for cleaning — which is why food and pharmaceutical plants adopted it wholesale."))
    b.append(fig(12, F.fig_3_12(), "en"))
    b.append(p(
        "The conventional design is close to quick opening. The dual-range version brings in a second, "
        "smaller diaphragm area over the upper half of the stroke and comes out close to linear, which is the "
        "difference between a valve that can be tuned and one that can only be switched."))
    b.append(fig(13, F.fig_3_13(), "en"))

    b.append(h3("Sliding gate"))
    b.append(p(
        "Two plates with holes in them, one sliding across the other. Because the motion is shear rather than "
        "compression, the actuator sees almost no unbalanced force, so the valve stays small and cheap even "
        "at 10,000 psig — the highest pressure in the table and the one place where this family has no "
        "competitor."))
    b.append(fig(14, F.fig_3_14(), "en"))
    b.append(p(
        "The characteristic is set entirely by the insert: a V gives something near equal percentage, a round "
        "hole gives quick opening, and a stepped insert gives a characteristic with a deliberate plateau in "
        "the middle."))
    b.append(fig(15, F.fig_3_15(), "en"))

    b.append(h3("Four more that do not fit the table"))
    b.append(p(
        "The catalogue has variants that are not separate families but answers to specific failures. The "
        "dynamically balanced plug admits process pressure to the back of the plug so that the two faces "
        "cancel, and a small pilot poppet does the metering: the actuator no longer has to hold the line "
        "pressure, only the pilot."))
    b.append(fig(16, F.fig_3_16(), "en"))
    b.append(p(
        "The diaphragm-operated cylinder valve puts the same idea in-line for high-pressure drops. The "
        "expandable-element valve replaces the plug with a solid rubber cylinder that is expanded or "
        "contracted to change an annular area — a pinch valve turned inside out, with the same absence of "
        "packing and the same temperature limit."))
    b.append(fig(17, F.fig_3_17(), "en"))
    b.append(fig(18, F.fig_3_18(), "en"))
    b.append(p(
        "The fluid-interaction valve has no moving part in the flow at all. Two lateral control ports sit at "
        "the base of a Y; a small control flow deflects the main jet from one port to the other in a "
        "flip-flop, and the valve is switched rather than throttled. It is a diverter, and it belongs in this "
        "chapter only because it is the limiting case of the argument: the less the valve obstructs the "
        "flow, the less it can modulate it."))
    b.append(fig(19, F.fig_3_19(), "en"))

    b.append(h2("Gain is the only number that matters"))
    b.append(p(
        "Equation 3.1 is the whole chapter in one line: K_LOOP = K_C × K_V × K_P × K_S = 0.5. The 0.5 is "
        "quarter-amplitude damping. If the process gain K_P rises when load rises — which is what most "
        "processes do — something else in the product has to fall by the same factor, or the loop goes from "
        "sluggish to oscillating as load changes."))
    b.append(p(
        "The controller can do that (that is what gain scheduling is), or the valve can. Choosing an equal "
        "percentage valve is choosing to let the valve do it: its gain is proportional to flow, so when the "
        "process gain rises with flow the valve gain falls to compensate. A linear valve has constant gain and "
        "compensates for nothing."))
    b.append(fig(20, F.fig_3_20(), "en"))
    b.append(p(
        "That is why the Driskell table in the text is worth more than it looks. It is not a list of "
        "preferences; it is a list of which loops have a process gain that varies enough to need compensating. "
        "Level loops and gas-pressure loops get equal percentage when the valve takes more than 2:1 of the "
        "pressure drop; flow loops stay linear because a flow loop's process gain is already close to constant."))

    b.append(h2("Distortion: why the bench curve is a lie"))
    b.append(p(
        "Boger's relation is the useful piece of mathematics here. If DC is the fraction of the total system "
        "pressure drop that appears across the valve at maximum flow, then the installed flow is "
        "q = f(x) / √(DC + (1−DC)·f(x)²). At DC = 1 — a valve with the whole system drop across it — the "
        "installed curve is the inherent curve. As DC falls, the curve saturates earlier and the usable travel "
        "shrinks."))
    b.append(fig(7, F.fig_3_7(), "en"))
    b.append(p(
        "Figure 3.21 plots that family. At DC = 0.05, a linear valve is fully open by 40 % travel: the last "
        "60 % of the stroke does nothing. The valve is not faulty; the installation has removed its range. "
        "This is the single most common reason a valve that tested perfectly on the bench controls badly in "
        "the plant."))
    b.append(fig(21, F.fig_3_21(), "en"))
    b.append(p(
        "The practical consequence is in section 3.3.3: rangeability should be computed from the C_V needed at "
        "maximum flow (minimum drop) and the C_V needed at minimum flow (maximum drop), not taken from the "
        "catalogue. The catalogue figure assumes a constant drop that no real installation has."))

    b.append(h2("Actuators: force balance, not magic"))
    b.append(p(
        "Equations 3.2 to 3.5 are one equation written four times, once for each combination of direction and "
        "flow. P·A is the diaphragm force, K·X the spring, P_V·A_V the force the process exerts on the plug. "
        "Set the sum to zero and you have the steady-state stem position. The sign of the P_V·A_V term is what "
        "makes a valve 'flow-to-open' or 'flow-to-close', and it is why a valve can be stable in one piping "
        "arrangement and unstable in the reverse."))
    b.append(fig(22, F.fig_3_22(), "en"))
    b.append(p(
        "The simplifications matter too. Friction in the packing, in the actuator guide and in the plug guide "
        "is left out, and so is inertia. Those omissions are exactly the hysteresis loop drawn in Figure 3.23: "
        "the real valve does not retrace its path, and the width of that loop is the dead band the controller "
        "has to overcome before anything moves."))
    b.append(fig(23, F.fig_3_23(), "en"))
    b.append(p(
        "The positioner is the answer to friction, and it is also a trap. A positioner is a high-gain "
        "proportional controller (K = 10 to 200, proportional band 10 % to 0.5 %) closed around stem position. "
        "It makes the valve follow its set point regardless of packing friction — and in doing so it inserts a "
        "second, fast loop inside the first. The rule in section 3.5.1 is the cascade rule: the slave must be "
        "at least ten times faster than the master, or the two loops fight."))
    b.append(fig(24, F.fig_3_24(), "en"))

    b.append(h2("Sizing: the mistake that is hard to see"))
    b.append(p(
        "Section 3.6 is short and is the most expensive page in the chapter. The instruction is to size "
        "between 0.8·C_V,min and 1.2·C_V,max and not to use a valve outside its rangeability. The trap it "
        "warns about is summing every pressure drop in a constant-speed pumping system and handing the total "
        "to the valve: the valve is then sized for a drop it will never see, ends up oversized, and spends its "
        "life at 5–10 % travel where the characteristic is most distorted and cavitation is most likely."))
    b.append(p(
        "An oversized valve is worse than an undersized one because the failure is quiet. An undersized valve "
        "simply cannot pass the peak flow — obvious, and easy to justify replacing. An oversized valve passes "
        "everything, controls nothing well, and nobody notices until the loop is retuned for the third time."))
    b.append(quote(
        "A valve is not a tap you can turn anywhere. It is an element with its own gain, and that gain changes "
        "with flow, with pressure drop, and with the way you installed it.",
        "Wolfgang Altmann"))
    return "".join(b)
