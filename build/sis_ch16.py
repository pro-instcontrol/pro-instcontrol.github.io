# -*- coding: utf-8 -*-
"""Safety Instrumented Systems — Chapter 16, Case Study (Gruhn & Cheddie, ISA 2006)."""
from pcsis_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, refs,
                          table, ul)

import sis16fig as F

PAGES_SRC = 20
BYLINE = "Paul Gruhn & Harry Cheddie · ISA (2006)"

TICK = "X"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Case study</em> — nghiên cứu tình huống: một bài tập chạy suốt vòng đời trên một lò nung "
            "có thật. · "
            "<em>Fired heater</em> — lò nung: thiết bị gia nhiệt bằng lửa trực tiếp; ở đây là lò của phân "
            "xưởng chưng cất dầu thô. · "
            "<em>Pass</em> — nhánh ống: lò có nhiều nhánh ống song song, mỗi nhánh có lưu lượng riêng. · "
            "<em>Pilot</em> — khí mồi: dòng khí nhỏ cháy thường trực để giữ lửa. · "
            "<em>K.O. drum</em> — bình tách lỏng (knock-out drum): tách giọt lỏng khỏi dòng khí trước khi "
            "vào đầu đốt. · "
            "<em>Cause and effect diagram</em> — sơ đồ nguyên nhân – kết quả: bảng chéo nói nguyên nhân "
            "nào đóng van nào. · "
            "<em>Nuisance trip</em> — cắt nhầm. · "
            "<em>PSAT</em> — kiểm tra nghiệm thu trước khởi động. · "
            "<em>Bypass</em> — nhánh rẽ, mở ra để thử hệ mà không cắt dây chuyền.")
    return note(
        "<b>Key terms.</b> <em>Case study</em> — a worked example that runs the whole lifecycle on one "
        "real furnace. · <em>Fired heater</em> — a furnace heated by direct flame; here, the crude unit "
        "charge heater. · <em>Pass</em> — one of several parallel tube runs through the furnace, each "
        "with its own flow. · <em>Pilot</em> — a small, continuously burning gas stream that keeps the "
        "main flame lit. · <em>K.O. drum</em> — knockout drum: removes liquid droplets from a gas stream "
        "before it reaches the burners. · <em>Cause and effect diagram</em> — a cross-reference sheet "
        "saying which cause closes which valve. · <em>Nuisance trip</em> — a spurious shutdown. · "
        "<em>PSAT</em> — pre-startup acceptance test. · <em>Bypass</em> — a valve opened to test the "
        "system without shutting the unit down.")


# ====================================================================== VI
def body_vi():
    b = []
    b.append(lead(
        "Mười lăm chương trước là mười lăm mảnh của một quy trình. Chương này ghép chúng lại: một lò nung "
        "của phân xưởng chưng cất dầu thô, đi từ phân tích mối nguy tới quy trình thử nghiệm ba tháng một "
        "lần, qua đủ tám bước của vòng đời. Trọng tâm không phải lời giải mà là cách làm."))
    b.append(ul([
        "Vòng đời an toàn và tầm quan trọng của nó",
        "Mô tả tình huống: hệ cắt an toàn cho lò nung",
        "Phạm vi phân tích",
        "Xác định SIL mục tiêu",
        "Lập đặc tả yêu cầu an toàn",
        "Thiết kế khái niệm SIS",
        "Phân tích chi phí vòng đời",
        "Kiểm chứng thiết kế khái niệm có đạt SIL",
        "Thiết kế chi tiết",
        "Lắp đặt, chạy thử và kiểm tra trước khởi động",
        "Quy trình vận hành và bảo trì",
    ]))

    # ------------------------------------------------------------------ 16.1
    b.append(h2("16.1 Giới thiệu", "Introduction"))
    b.append(p("Tình huống trong chương này nhằm cho thấy cách dùng những chất liệu và kỹ thuật đã trình bày "
               "ở Chương 1 đến Chương 15 để đặc tả, thiết kế, lắp đặt, chạy thử và bảo trì một hệ an toàn "
               "điển hình. Ý định là đi hết các bước của vòng đời đã nêu ở Chương 2. Qua việc xem lại cách "
               "giải quyết từng vấn đề cụ thể trong tình huống này, người đọc sẽ làm rõ thêm các kỹ thuật, "
               "hiểu và đánh giá đúng hơn nhu cầu về tài liệu tốt, và gỡ được những chỗ hiểu nhầm."))
    b.append(p("Trọng tâm của chương là cách tiếp cận, không phải bài toán hay lời giải cuối cùng. Tình "
               "huống và bộ tài liệu đã được giản lược để giữ sự tập trung vào câu hỏi «làm thế nào» chứ "
               "không phải «bao nhiêu»."))

    # ------------------------------------------------------------------ 16.2
    b.append(h2("16.2 Vòng đời an toàn và tầm quan trọng của nó",
                "The safety lifecycle and its importance"))
    b.append(p("Như đã nhấn mạnh ở Chương 2, tiêu chuẩn ANSI/ISA 84.00.01-2004 Phần 1-3 (sửa đổi từ IEC "
               "61511) liệt kê các bước phải theo để bảo đảm hệ an toàn được đặc tả, thiết kế, lắp đặt và "
               "bảo trì đúng. Hình 16-1 là bản giản lược của vòng đời ấy. Các bước chia thành ba pha "
               "chính: (1) phân tích rủi ro, (2) thiết kế và thực hiện, (3) vận hành và bảo trì."))
    b.append(note(
        "<b>Một lời cảnh báo.</b> Các thiết bị điều khiển và bảo vệ trong chương này là những ví dụ đơn "
        "giản hoá, chỉ để học. Chúng không phản ánh — dưới bất kỳ hình thức nào — những gì một công trình "
        "thực tế đòi hỏi. Các lời giải và hệ thống được đề xuất ở đây cũng không nhất thiết tuân thủ một "
        "số tiêu chuẩn được công nhận trên thế giới (ví dụ của Hiệp hội Phòng cháy Quốc gia Hoa Kỳ NFPA, "
        "hay Viện Dầu khí Hoa Kỳ API)."))
    b.append(fig(1, F.fig_16_1(), "vi"))
    b.append(p("Pha phân tích rủi ro bao gồm phân tích mối nguy quá trình, đánh giá rủi ro, nhận diện các "
               "chức năng an toàn (SIF), xác định mức toàn vẹn an toàn (SIL) và lập đặc tả yêu cầu an toàn "
               "(SRS). Pha thiết kế và thực hiện bao gồm việc thiết kế và triển khai SIS — trong đó có các "
               "phép tính kiểm chứng SIL để xác nhận hệ sắp lắp đặt thoả yêu cầu SIL — cùng việc lắp đặt và "
               "chạy thử. Pha vận hành và bảo trì lo việc vận hành và bảo trì hệ trong suốt đời sống của nó, "
               "nhằm giữ vững SIL của từng chức năng."))
    b.append(p("Tiêu chuẩn cũng nhấn mạnh rằng việc quản lý an toàn chức năng, đánh giá an toàn chức năng, "
               "cấu trúc và lập kế hoạch vòng đời an toàn, cùng các hoạt động kiểm chứng, phải diễn ra "
               "xuyên suốt vòng đời. Đó là khối dọc bên trái của Hình 16-1."))
    b.append(p("Tất cả những hoạt động trên đều phải được xử lý, vì ba lý do:"))
    b.append(ul([
        "Chương 2 đã dẫn lại kết luận của Cơ quan An toàn và Sức khoẻ Vương quốc Anh (U.K. HSE): tai nạn "
        "do hệ điều khiển và hệ an toàn hỏng đều truy nguyên được về những sai sót lẽ ra đã bị bắt nếu "
        "tuân thủ vòng đời này.",
        "Tuân thủ vòng đời giúp giảm hỏng hệ thống. Loại hỏng này sinh ra từ đặc tả thiếu, thiết kế sai, "
        "phát triển phần mềm ẩu, thử nghiệm sơ sài, đào tạo thiếu và quy trình không đầy đủ.",
        "SIL phải được nhìn nhận như một vấn đề của cả vòng đời. Muốn giữ được SIL đã xác định cho từng "
        "chức năng an toàn, mọi bước của vòng đời đều phải hoàn thành và được kiểm chứng.",
    ]))

    # ------------------------------------------------------------------ 16.3
    b.append(h2("16.3 Mô tả tình huống: hệ cắt an toàn cho lò nung",
                "Case description: furnace/fired heater safety shutdown system"))
    b.append(p("Hệ an toàn cho cụm điều khiển nhiên liệu của một lò nung thuộc phân xưởng chưng cất dầu thô "
               "cần được nâng cấp. Ban lãnh đạo nhà máy lo rằng hệ hiện hữu không đủ, không hiệu quả và "
               "không đáng tin. Lò đốt bằng khí tự nhiên, thông gió tự nhiên, có khí mồi cháy thường trực. "
               "Hình 16-2 là sơ đồ lò và các vòng điều khiển điều chỉnh cơ bản đi kèm."))
    b.append(h3("Mô tả các vòng điều khiển điều chỉnh cơ bản",
                "Description of basic process controls"))
    b.append(p("Lưu lượng liệu vào lò do hai vòng điều chỉnh FC-9 và FC-10 giữ. Một bộ điều chỉnh áp suất tự "
               "hành tại chỗ (PCV-6) giữ áp suất khí mồi. Lưu lượng khí đốt và nhiệt độ đầu ra cuộn ống là "
               "một phần của hệ điều khiển cascade: bộ điều chỉnh lưu lượng khí (FC-3) mắc cascade với bộ "
               "điều chỉnh nhiệt độ (TC-8). FC-3 tác động lên van FV-3 để giữ lưu lượng khí theo giá trị đặt "
               "do TC-8 đưa ra. Toàn bộ các vòng điều chỉnh nằm trong hệ điều khiển quá trình cơ bản (BPCS) "
               "đặt tại phòng điều khiển cách lò chừng 60 m (200 ft)."))
    b.append(fig(2, F.fig_16_2(), "vi"))
    b.append(p("Trong buổi rà soát mối nguy quá trình, người ta nhận diện được các sự kiện nguy hiểm sau:"))
    b.append(table(
        ["Mối nguy", "Nguyên nhân khả dĩ", "Hậu quả", "Khả năng"],
        [["Nổ lò", "Mất khí mồi", "Nhiều người thiệt mạng", "Trung bình"],
         ["Cháy lò", "Mất khí mồi, hoặc mất lưu lượng trong ống lò", "Tổn thất 1.000.000 $", "Trung bình"],
         ["Vỡ ống", "Mất lưu lượng trong ống lò", "Tổn thất 1.000.000 $", "Trung bình"]],
        caption="Bảng 16-1. Các mối nguy của lò nung"))
    b.append(p("Hội đồng đánh giá rằng không thể bổ sung thêm lớp bảo vệ nào không dùng thiết bị đo để ngăn "
               "hoặc giảm nhẹ các sự kiện trên. Các thiết bị an toàn và bảo vệ sau được khuyến nghị:"))
    b.append(ol([
        "Cắt khí đốt khi lưu lượng thấp ở bất kỳ nhánh nào (trễ 20 giây).",
        "Cắt cả khí đốt lẫn khí mồi khi áp suất khí mồi thấp.",
        "Bố trí một công tắc đi dây cứng chuyên dụng tại phòng điều khiển chính để dừng tay cả khí đốt lẫn "
        "khí mồi.",
    ]))
    b.append(p("Mỗi chức năng an toàn được dự kiến có yêu cầu ít hơn một lần mỗi năm. Ngoài ra, có thể chấp "
               "nhận một lần cắt nhầm lò mỗi năm do hệ an toàn hỏng. Thiệt hại của một lần cắt nhầm khoảng "
               "20.000 $."))

    # ------------------------------------------------------------------ 16.4
    b.append(h2("16.4 Phạm vi phân tích", "Scope of analysis"))
    b.append(p("Phạm vi phân tích gồm các bước sau của vòng đời an toàn:"))
    b.append(ol([
        "xác định SIL mục tiêu cho từng SIF;",
        "lập đặc tả yêu cầu an toàn (SRS);",
        "thiết kế khái niệm SIS;",
        "phân tích chi phí vòng đời;",
        "kiểm chứng thiết kế khái niệm có đạt SIL;",
        "thiết kế chi tiết;",
        "lắp đặt, chạy thử và kiểm tra trước khởi động;",
        "xây dựng quy trình vận hành và bảo trì.",
    ]))
    b.append(p("Nằm ngoài phạm vi trên là những hoạt động vòng đời quan trọng khác cũng phải hoàn thành "
               "trước hoặc song song với các bước trên:"))
    b.append(ul([
        "<b>Lập kế hoạch vòng đời an toàn.</b> Cần xây dựng và ban hành một kế hoạch vòng đời an toàn cho "
        "dự án. Các tiêu chuẩn không bắt buộc công ty vận hành phải theo đúng vòng đời như tiêu chuẩn vẽ "
        "ra.",
        "<b>Hoạt động quản lý an toàn chức năng.</b> Một số việc gồm: lập kế hoạch quản lý an toàn chức "
        "năng; xác định vai trò và trách nhiệm của từng vị trí; bảo đảm năng lực nhân sự; tài liệu và "
        "kiểm soát tài liệu; lập kế hoạch kiểm chứng an toàn chức năng; lập kế hoạch đánh giá an toàn "
        "chức năng; đánh giá an toàn định kỳ.",
        "<b>Hoạt động kiểm chứng</b> gắn với từng bước của vòng đời.",
        "<b>Đánh giá an toàn chức năng.</b> Ít nhất phải thực hiện một lần trước khi khởi động nhà máy.",
    ]))

    # ------------------------------------------------------------------ 16.5
    b.append(h2("16.5 Xác định SIL mục tiêu", "Define target SILs"))
    b.append(p("Mỗi chức năng an toàn phải được xác định một mức toàn vẹn an toàn. Chương 6 đã trình bày "
               "mấy phương pháp xác định SIL:"))
    b.append(ul([
        "<b>Định tính:</b> dùng ma trận rủi ro ba chiều.",
        "<b>Định tính:</b> dùng đồ thị rủi ro (risk graph).",
        "<b>Định lượng:</b> phân tích lớp bảo vệ (LOPA).",
    ]))
    b.append(p("Tình huống này dùng ma trận rủi ro ba chiều. Hậu quả và khả năng của các sự kiện nguy hiểm "
               "đã được ghi ở Bảng 16-1. Ma trận xác định rủi ro/SIL dưới đây là bản giản lược của ma trận "
               "ở Hình 6-2; nó cho biết SIL cần thiết theo từng tổ hợp hậu quả và khả năng, với giả định "
               "không có thêm lớp an toàn nào — đúng như kết luận của nghiên cứu an toàn."))
    b.append(note(
        "<b>Một lời cảnh báo.</b> Hạng mục hậu quả dùng khi xác định SIL là hậu quả tồi tệ nhất có thể tin "
        "được, với giả định không có bất kỳ biện pháp bảo vệ nào. Hạng mục khả năng thì giả định mọi biện "
        "pháp bảo vệ đều có, trừ chính chức năng an toàn đang xét. Rất nhiều trường hợp, hạng mục khả năng "
        "trong nghiên cứu và báo cáo an toàn lại đã bao gồm cả SIF. Nếu vậy, nhóm xác định SIL phải làm "
        "lại hạng mục khả năng với giả định SIF không tồn tại."))
    b.append(table(
        ["Hậu quả ＼ Khả năng", "Thấp", "Trung bình", "Cao"],
        [["Cao", "2", "3", "3"],
         ["Trung bình", "2", "2", "3"],
         ["Thấp", "1", "2", "2"]],
        caption="Ma trận rủi ro ba chiều dùng trong tình huống này — ô là SIL cần thiết"))
    b.append(p("SIL cần cho hai SIF theo ma trận trên được ghi ở Bảng 16-2."))
    b.append(table(
        ["Hạng mục", "Chức năng an toàn", "Hậu quả", "Khả năng", "SIL"],
        [["1", "Mất hoặc lưu lượng thấp ở các nhánh",
          "Vỡ ống, tổn thất 1.000.000 $<br>Cháy lò, tổn thất 1.000.000 $", "TB", "TB", "2"],
         ["2", "Áp suất khí mồi thấp", "Nổ, nhiều người thiệt mạng", "Cao", "TB", "3"]],
        caption="Bảng 16-2. Yêu cầu mức toàn vẹn an toàn cho ví dụ lò nung"))
    b.append(p("Lưu ý rằng không có SIL nào được chọn cho chức năng dừng tay. Theo định nghĩa, chức năng an "
               "toàn là hệ tự động đưa thiết bị hoặc quá trình về trạng thái an toàn khi một số điều kiện "
               "bị vi phạm. Báo động và dừng tay thường không được coi là chức năng an toàn vì chúng không "
               "tự hành động. Vì vậy nhiều công ty không yêu cầu chọn SIL cho báo động và dừng tay."))

    # ------------------------------------------------------------------ 16.6
    b.append(h2("16.6 Lập đặc tả yêu cầu an toàn", "Develop the safety requirement specification"))
    b.append(p("Chương 5 đã trình bày đặc tả yêu cầu an toàn (SRS), gồm hai phần: đặc tả chức năng (hệ làm "
               "gì) và đặc tả toàn vẹn (hệ làm tốt tới đâu). Trên thực tế SRS có thể là một bộ tài liệu. "
               "Bảng 16-3 tóm tắt những thông tin then chốt phải có trong SRS. Liệt kê mọi yêu cầu vào một "
               "bảng duy nhất cho phép đối chiếu đơn giản xem còn thiếu gì. Cột «Chi tiết» cho biết thông "
               "tin về từng hạng mục có cần cho ứng dụng này hay không; nếu cần, có thể ghi chú thêm ngay "
               "trong cột đó."))
    b.append(table(
        ["Hạng mục", "Chi tiết yêu cầu"],
        ["Tài liệu đầu vào và các yêu cầu chung",
         ["P&ID", "Bắt buộc. Hình 16-2 là bản giản lược của P&ID thực tế."],
         ["Sơ đồ nguyên nhân – kết quả", "Kèm theo. (Xem Bảng 16-4.)"],
         ["Sơ đồ logic", "Bản vẽ nguyên nhân – kết quả đã đủ để xác định yêu cầu logic."],
         ["Phiếu dữ liệu quá trình",
          "Cần cung cấp cho mọi thiết bị hiện trường, tức FT-22, FT-23, PT-7, PT-24 và bốn van cắt."],
         ["Thông tin quá trình của từng sự kiện nguy hiểm cần SIF (động học nguyên nhân sự cố, phần tử "
          "cuối, v.v.)",
          "Cần mô tả chi tiết: nổ, cháy hoặc vỡ ống có thể xảy ra thế nào và thiết bị bảo vệ sẽ giảm nhẹ "
          "ra sao; tốc độ đáp ứng và độ chính xác của hệ bảo vệ phải được xác định; các yêu cầu đặc biệt "
          "cho van cắt (chống cháy, cấp độ kín)."],
         ["Cân nhắc hỏng do nguyên nhân chung của quá trình, như ăn mòn, tắc nghẽn, bám cặn",
          "Đo lưu lượng dầu thô là ứng dụng khó vì độ nhớt cao và hiện tượng đóng băng. Ưu tiên thiết bị "
          "đo kiểu đặt trong đường ống. Với ứng dụng này, nhà máy đã có kinh nghiệm tốt với lưu lượng kế "
          "kiểu Coriolis. Cần xử lý ăn mòn do hydrogen sulfide trong không khí."],
         ["Yêu cầu pháp lý tác động tới SIS",
          "Phải thoả mãn ANSI/ISA-84.00.01-2004 Phần 1-3. API 556 có thể dùng làm tài liệu tham chiếu. "
          "Không bắt buộc tuân thủ đầy đủ tiêu chuẩn."],
         ["Khác", "Không."],
         "Yêu cầu chi tiết cho từng SIF",
         ["Số hiệu SIF", "Xem Bảng 16-4."],
         ["SIL yêu cầu của SIF", "Xem Bảng 16-4."],
         ["Tần suất yêu cầu dự kiến", "Một lần mỗi năm. Vận hành ở chế độ nhu cầu thấp."],
         ["Khoảng thời gian kiểm tra", "3 tháng."],
         ["Định nghĩa trạng thái an toàn của quá trình cho từng sự kiện đã nhận diện",
          "Trạng thái an toàn là cắt khí đốt, cắt khí mồi và cắt dòng liệu vào lò."],
         ["Đầu vào quá trình của SIS và điểm cắt", "Xem Bảng 16-4."],
         ["Dải vận hành bình thường của các biến quá trình và giới hạn vận hành", "Xem Bảng 16-4."],
         ["Đầu ra quá trình của SIS và tác động tương ứng", "Xem Bảng 16-4."],
         ["Quan hệ chức năng giữa đầu vào và đầu ra, kể cả logic, hàm toán và mọi điều kiện cho phép",
          "Xem Bảng 16-4."],
         ["Chọn kiểu cắt khi mất điện hay cấp điện để cắt",
          "Toàn bộ hệ an toàn phải ở trạng thái cắt khi mất điện."],
         ["Cân nhắc dừng tay",
          "Một công tắc dừng đi dây cứng đặt tại phòng điều khiển chính (HS-21). Chức năng dừng tay phải "
          "độc lập với hệ khả trình."],
         ["Yêu cầu về quy trình khởi động và khởi động lại SIS", "Có. Sẽ xây dựng."],
         ["Danh mục yêu cầu an toàn đặc biệt cho phần mềm ứng dụng", "Không có."],
         ["Yêu cầu về khoá tạm và nhánh rẽ, kể cả cách xoá", "Có. Sẽ xây dựng."],
         ["Hành động khi mất nguồn năng lượng cấp cho SIS", "Mọi van cắt phải đóng."],
         ["Yêu cầu thời gian đáp ứng để đưa quá trình về trạng thái an toàn",
          "5 giây là chấp nhận được."],
         ["Phản ứng với chẩn đoán và với lỗi phát hiện được",
          "Đáp ứng tức thời. Việc bảo trì phải được ưu tiên cao nhất. Bộ phận vận hành phải theo dõi sát "
          "các thông số then chốt cho tới khi khắc phục xong."],
         ["Yêu cầu về giao diện người – máy",
          "Cần báo động đi dây cứng tại phòng điều khiển chính cho mọi lỗi hoặc trạng thái cắt của hệ an "
          "toàn. Cần nút dừng tay."],
         ["Chức năng đặt lại", "Van cắt phải được trang bị solenoid đặt lại bằng tay."],
         ["Yêu cầu chẩn đoán để đạt SIL",
          "Dùng cảm biến hiện trường thông minh để tận dụng khả năng chẩn đoán của chúng. Van cắt phải có "
          "công tắc hành trình để xác nhận đã đóng khi bộ logic yêu cầu."],
         ["Yêu cầu bảo trì và kiểm tra để đạt SIL", "Xem quy trình kiểm tra bằng tay."],
         ["Yêu cầu độ tin cậy nếu cắt nhầm có thể nguy hiểm",
          "Phải tính tần suất cắt nhầm để thoả yêu cầu của nghiên cứu an toàn."],
         ["Chế độ hỏng của từng van điều khiển", "Đóng khi hỏng (fail closed)."],
         ["Chế độ hỏng của mọi cảm biến và biến đổi", "Thấp khi hỏng (fail low)."],
         ["Khác", "Không."]],
        caption="Bảng 16-3. Bảng tóm tắt đặc tả yêu cầu an toàn", cls="tbl srs"))

    b.append(h3("Sơ đồ nguyên nhân – kết quả", "Cause and effect diagram"))
    b.append(p("Bảng 16-4 là sơ đồ nguyên nhân – kết quả của hệ. Bốn cột cuối là bốn van cắt: XV-30A và "
               "XV-30B trên dòng khí mồi, XV-31A và XV-31B trên dòng khí đốt. Dấu × nghĩa là nguyên nhân ở "
               "cột đầu sẽ đóng van ở cột đó."))
    b.append(table(
        ["Tag", "Mô tả", "SIL", "Dải", "Ngưỡng cắt", "ĐV", "XV-30A", "XV-30B", "XV-31A", "XV-31B", "Ghi chú"],
        [["FT-22", "Lưu lượng nhánh A vào lò", "2", "0–500", "100,0", "B/H", TICK, TICK, "", "", "1"],
         ["FT-23", "Lưu lượng nhánh B vào lò", "2", "0–500", "100,0", "B/H", TICK, TICK, "", "", "1"],
         ["PT-7/24", "Áp suất khí mồi", "3", "0–30", "5", "PSIG", TICK, TICK, TICK, TICK, "2"],
         ["—", "Mất nguồn điều khiển", "NA", "", "", "", TICK, TICK, TICK, TICK, ""],
         ["—", "Mất khí dụng cụ", "NA", "", "", "", TICK, TICK, TICK, TICK, ""],
         ["HS-21", "Dừng tay", "NA", "", "", "", TICK, TICK, TICK, TICK, ""]],
        caption="Bảng 16-4. Sơ đồ nguyên nhân – kết quả. Ghi chú 1: phải trễ 20 giây trước khi đóng van. "
                "Ghi chú 2: cả bốn van cắt đều phải có solenoid đặt lại bằng tay.",
        cls="tbl matrix ce"))

    # ------------------------------------------------------------------ 16.7
    b.append(h2("16.7 Thiết kế khái niệm SIS", "SIS conceptual design"))
    b.append(p("Thiết kế khái niệm phải tuân thủ mọi tiêu chuẩn nội bộ có liên quan. Dưới đây là bản tóm "
               "tắt các hướng dẫn của công ty về SIL và về chọn thiết bị:"))
    b.append(table(
        ["SIL", "Cảm biến", "Bộ xử lý logic", "Phần tử cuối"],
        [["3", "Cần cảm biến dư thừa, hoặc 1oo2 hoặc 2oo3 tuỳ yêu cầu về cắt nhầm.",
          "Cần PLC an toàn dư thừa.", "Yêu cầu bỏ phiếu 1oo2."],
         ["2", "Có thể cần hoặc không cần dư thừa. Phương án ban đầu là không dư thừa. Chọn dư thừa nếu "
               "phép tính PFDavg cho thấy cần.",
          "Cần PLC an toàn.",
          "Có thể cần hoặc không cần dư thừa. Phương án ban đầu là không dư thừa. Chọn dư thừa nếu phép "
          "tính PFDavg cho thấy cần."],
         ["1", "Một cảm biến.", "PLC không dư thừa hoặc logic relay.", "Một thiết bị."]],
        caption="Bảng 16-5. Hướng dẫn thiết kế SIS theo SIL"))
    b.append(p("Dựa trên các tiêu chí ở Bảng 16-5, hệ được đề xuất như Hình 16-3."))
    b.append(fig(3, F.fig_16_3(), "vi"))
    b.append(h3("Yêu cầu của thiết kế khái niệm", "Conceptual design requirements"))
    b.append(p("Thiết kế khái niệm (xem Chương 10) được xây trên và bổ sung cho đặc tả yêu cầu an toàn ở mục "
               "16.6, đồng thời tiếp nhận các hướng dẫn thiết kế của công ty. Những thông tin then chốt mà "
               "nhà thầu kỹ thuật cần để hoàn thành gói thiết kế chi tiết phải được cung cấp đầy đủ. Thiết "
               "kế phải theo đúng tiêu chuẩn và quy trình của công ty. Không được có mâu thuẫn giữa SRS và "
               "các yêu cầu của thiết kế khái niệm."))
    b.append(table(
        ["Hạng mục", "Yêu cầu"],
        [["Kiến trúc hệ thống",
         "Bộ xử lý logic phải là PLC an toàn dư thừa, đã được chứng nhận. Tủ đặt trong toà nhà điều khiển "
         "chính. Cần bỏ phiếu 1oo2 cho các biến đổi áp suất khí mồi, cũng như cho van cắt khí đốt và khí "
         "mồi. Phải kiểm chứng rằng thiết kế này đạt yêu cầu SIL. Hình 16-4 là bản phác cấu hình tổng thể."],
        ["Giảm thiểu nguyên nhân chung",
         "Dây từ các van và biến đổi 1oo2 về SIS phải đi riêng, tách khỏi dây của BPCS. Dùng bộ cấp nguồn "
         "liên tục (UPS) riêng cho SIS. Mọi biến đổi phải có điểm lấy áp riêng."],
        ["Điều kiện môi trường",
         "Phân loại khu vực là Class 1, Group D, Div 2. Có hydrogen sulfide trong không khí quanh lò. Nhiệt "
         "độ môi trường có thể xuống tới −35 °C vào mùa đông."],
        ["Nguồn điện",
         "Có nguồn 110 V, 60 Hz từ hai hệ UPS độc lập đặt tại phòng điều khiển chính."],
        ["Nối đất",
         "Phải theo tiêu chuẩn nối đất của công ty cho hệ thiết bị đo và hệ nguồn."],
        ["Nhánh rẽ",
         "Phải lắp van nhánh rẽ quanh cặp van cắt khí mồi và cặp van cắt khí đốt để thử trực tuyến. Cần "
         "một báo động trên BPCS cho biết van nhánh rẽ đã mở. Không cần nhánh rẽ nào khác."],
        ["Phần mềm ứng dụng", "Dùng logic thang cho toàn bộ việc lập trình trong SIS."],
        ["An ninh",
         "Phải theo các yêu cầu an ninh hiện hành của công ty về truy cập và sửa đổi logic SIS."],
        ["Giao diện vận hành",
         "Báo động cắt và báo động chẩn đoán phải đi dây về bảng thông báo cứng hiện hữu. Báo động nhánh "
         "rẽ nối về BPCS."]],
        caption="Bảng 16-6. Tóm tắt các yêu cầu của thiết kế khái niệm", cls="tbl srs"))
    b.append(fig(4, F.fig_16_4(), "vi"))

    # ------------------------------------------------------------------ 16.8
    b.append(h2("16.8 Phân tích chi phí vòng đời", "Lifecycle cost analysis"))
    b.append(table(
        ["Hạng mục", "Vật tư ($)", "Nhân công ($)", "Tổng ($)"],
        ["Chi phí cố định ban đầu",
         ["Phân loại an toàn", "", "", "1.000"],
         ["SRS và đặc tả thiết kế", "", "", "3.000"],
         ["Thiết kế chi tiết và kỹ thuật", "", "", "20.000"],
         ["Cảm biến", "", "", "24.000"],
         ["Phần tử cuối", "", "", "6.000"],
         ["Hệ logic", "", "", "30.000"],
         ["Linh tinh — nguồn, dây, hộp nối", "", "", "4.000"],
         ["Đào tạo ban đầu", "", "", "5.000"],
         ["FAT / lắp đặt / PSAT", "4.000", "16.000", "20.000"],
         ["Khởi động và hiệu chỉnh", "1.000", "2.000", "3.000"],
         ["<b>Cộng chi phí cố định</b>", "", "", "<b>116.000</b>"],
          "Chi phí hằng năm",
         ["Đào tạo thường xuyên", "", "", "1.000"],
         ["Thay đổi kỹ thuật", "1.000", "1.000", "2.000"],
         ["Hợp đồng dịch vụ", "", "", "1.000"],
         ["Chi phí vận hành và bảo trì cố định", "", "", "1.000"],
         ["Phụ tùng", "", "", "4.000"],
         ["Thử trực tuyến", "", "", "8.000"],
         ["Chi phí sửa chữa", "1.000", "500", "1.500"],
         ["Chi phí do cắt nhầm", "", "", "8.000"],
         ["<b>Cộng chi phí hằng năm</b>", "", "", "<b>26.500</b>"],
         ["Hiện giá của chi phí hằng năm (20 năm, lãi suất 5 %)", "", "", "330.249"],
         ["<b>Tổng chi phí vòng đời</b>", "", "", "<b>446.249</b>"]],
        caption="Bảng 16-7. Tóm tắt chi phí vòng đời", cls="tbl cost"))

    # ------------------------------------------------------------------ 16.9
    b.append(h2("16.9 Kiểm chứng thiết kế khái niệm có đạt SIL",
                "Verify that the conceptual design meets the SIL"))
    b.append(p("Phải kiểm chứng rằng từng chức năng an toàn đạt yêu cầu về mức toàn vẹn an toàn. Ở đây có "
               "ba chức năng: lưu lượng thấp nhánh A, lưu lượng thấp nhánh B, và áp suất khí mồi thấp. Chức "
               "năng áp suất khí mồi thấp cần SIL 3, hai chức năng lưu lượng nhánh cần SIL 2. Ở đây chỉ "
               "phân tích chức năng SIL 3."))
    b.append(p("Các công thức ở Chương 8 được dùng cho phép tính. Hình 16-5 là sơ đồ khối của chức năng "
               "cắt áp suất thấp khí mồi ở mức khái niệm."))
    b.append(fig(5, F.fig_16_5(), "vi"))
    b.append(p("Giả thiết:"))
    b.append(ul([
        "Thời gian sửa chữa trung bình (MTTR): 8 giờ.",
        "Tần suất yêu cầu trung bình: một lần mỗi năm.",
        "Khoảng thời gian kiểm tra bằng tay: 3 tháng.",
        "Hệ số nguyên nhân chung β: 5 %.",
        "Chẩn đoán biến đổi bằng cách so sánh: 90 %.",
    ]))
    b.append(table(
        ["Hạng mục", "Tốc độ hỏng nguy hiểm λ<sub>d</sub>", "Tốc độ hỏng an toàn λ<sub>s</sub>"],
        [["Biến đổi PT-7/24", "0,01 (1/100 năm)", "0,02 (1/50 năm)"],
         ["Van và solenoid XV-30A/B, XV-31A/B", "0,02 (1/50 năm)", "0,1 (1/10 năm)"],
         ["PLC an toàn", "Xem ghi chú 1", "Xem ghi chú 1"]],
        caption="Bảng 16-8. Dữ liệu tốc độ hỏng (số lần hỏng mỗi năm). Ghi chú 1: giá trị PFDavg và MTTFsp "
                "của PLC an toàn dư thừa do nhà cung cấp đưa."))
    b.append(h3("Tính PFDavg", "PFDavg calculations"))
    b.append(eq("PFD<sub>avg</sub> (cảm biến) = 0,01 × 0,1 × 0,05 × 0,25/2 = 0,00000625", "16.1"))
    b.append(p("Tức là: tốc độ hỏng × 10 % số hỏng không phát hiện được × 5 % nguyên nhân chung × khoảng "
               "thời gian kiểm tra chia hai."))
    b.append(eq("PFD<sub>avg</sub> (van và solenoid) = 2 × 0,02 × 0,05 × 0,25/2 = 0,00025", "16.2"))
    b.append(p("Tức là: số lượng × tốc độ hỏng × 5 % nguyên nhân chung × khoảng thời gian kiểm tra chia "
               "hai."))
    b.append(eq("PFD<sub>avg</sub> (PLC an toàn dư thừa) = 0,00005"))
    b.append(eq("PFD<sub>avg</sub> (tổng) = 0,000306"))
    b.append(p("Giá trị lớn nhất cho phép đối với SIL 3 là 0,001, nên thiết kế khái niệm thoả yêu cầu an "
               "toàn. Hệ số giảm rủi ro của hệ (RRF = 1/PFD) là 3.300, nằm trong dải 1.000 đến 10.000 của "
               "SIL 3."))
    b.append(h3("Tính MTTF<sub>spurious</sub>", "MTTFspurious calculations"))
    b.append(p("Mọi thiết bị hiện trường đều được đưa vào phép tính cắt nhầm."))
    b.append(eq("MTTF<sub>spurious</sub> (cảm biến) = 1/(4 × 0,02) = 12,5 năm"))
    b.append(eq("MTTF<sub>spurious</sub> (van và solenoid) = 1/(4 × 0,1) = 2,5 năm"))
    b.append(eq("MTBF<sub>sp</sub> (PLC an toàn) = 1/0,01 = 100 năm"))
    b.append(eq("MTBF<sub>sp</sub> (tổng) = 2,0 năm"))
    b.append(p("Như vậy trung bình khoảng hai năm sẽ có một lần cắt nhầm — vẫn thoả yêu cầu ban đầu là "
               "chấp nhận một lần cắt nhầm mỗi năm."))

    # ------------------------------------------------------------------ 16.10
    b.append(h2("16.10 Thiết kế chi tiết", "Detailed design"))
    b.append(p("Thiết kế chi tiết phải tuân thủ đặc tả yêu cầu an toàn và thiết kế khái niệm. Gói tài liệu "
               "thiết kế chi tiết phải gồm:"))
    b.append(ol([
        "kết quả và khuyến nghị của các nghiên cứu an toàn và mối nguy;",
        "toàn bộ phép tính PFDavg và MTTFspurious;",
        "sơ đồ ống và thiết bị đo (P&ID);",
        "bảng liệt kê thiết bị đo;",
        "phiếu đặc tả của PLC an toàn, biến đổi và van;",
        "sơ đồ vòng;",
        "ma trận nguyên nhân – kết quả;",
        "bản vẽ vị trí của mọi thiết bị và cụm điều khiển chính;",
        "cấu hình hệ PLC, bảng liệt kê vào/ra và bản in chương trình thang;",
        "sơ đồ đấu nối hộp nối và tủ;",
        "bảng lịch tủ điện;",
        "sơ đồ đường ống khí nén;",
        "danh mục phụ tùng;",
        "tài liệu tiêu chuẩn của nhà cung cấp, gồm đặc tả, yêu cầu lắp đặt và sổ tay vận hành – bảo trì;",
        "phiếu và quy trình kiểm tra;",
        "quy trình kiểm tra bằng tay.",
    ]))

    # ------------------------------------------------------------------ 16.11
    b.append(h2("16.11 Lắp đặt, chạy thử và kiểm tra trước khởi động",
                "Installation, commissioning and pre-startup tests"))
    b.append(p("Phải hoàn thành các hoạt động sau:"))
    b.append(ul([
        "<b>Kiểm tra nghiệm thu tại xưởng (FAT)</b> của hệ logic. Trách nhiệm và nội dung kiểm tra phải nằm "
        "trong phạm vi thiết kế chi tiết. Nhân sự hỗ trợ phải chứng kiến buổi kiểm tra.",
        "<b>Lắp đặt hiện trường toàn hệ.</b> Việc lắp đặt phải đúng các bản vẽ lắp đặt trong gói thiết kế.",
        "<b>Kiểm tra sau lắp đặt.</b> Phiếu kiểm tra từng thiết bị phải được điền đầy đủ và nộp kèm phạm vi "
        "công việc lắp đặt.",
        "<b>Thẩm định hoặc kiểm tra nghiệm thu tại công trường.</b> Kiểm tra chức năng theo đúng phiếu và "
        "quy trình kiểm tra chức năng.",
        "<b>Kiểm tra nghiệm thu trước khởi động (PSAT).</b> Do bộ phận vận hành thực hiện trước khi khởi "
        "động cụm. Sơ đồ nguyên nhân – kết quả là đủ cho PSAT.",
    ]))

    # ------------------------------------------------------------------ 16.12
    b.append(h2("16.12 Quy trình vận hành và bảo trì", "Operation and maintenance procedures"))
    b.append(p("Phải xây dựng quy trình vận hành và bảo trì an toàn cho cụm. Phải xây dựng quy trình kiểm "
               "tra cho từng chức năng an toàn. Quy trình dưới đây áp dụng cho chức năng cắt áp suất thấp "
               "khí mồi."))
    b.append(fig(6, F.fig_16_6(), "vi"))

    b.append(h3("Quy trình kiểm tra cắt — Quy trình số XX-1", "Shutdown test procedure #XX-1"))
    b.append(h4("1.0 Mục đích"))
    b.append(p("Kiểm tra chức năng cắt áp suất thấp khí mồi của lò F-001 và của hai biến đổi PT-7 và "
               "PT-24."))
    b.append(h4("2.0 Trách nhiệm thực hiện"))
    b.append(p("Người vận hành lò chịu trách nhiệm hoàn thành buổi kiểm tra. Kỹ thuật viên thiết bị đo "
               "thường trực phải đi cùng người vận hành trong suốt buổi kiểm tra."))
    b.append(h4("3.0 Dụng cụ và vật tư cần thiết"))
    b.append(p("Một bộ đàm cầm tay. Không cần dụng cụ đặc biệt nào để hoàn thành buổi kiểm tra này."))
    b.append(h4("4.0 Tần suất kiểm tra cắt"))
    b.append(p("Phải hoàn thành buổi kiểm tra này ba tháng một lần."))
    b.append(h4("5.0 Mối nguy"))
    b.append(ul([
        "Không mở van nhánh rẽ của khí mồi hoặc của khí đốt sẽ làm lò cắt, và có thể gây cháy hoặc nổ lò.",
        "Không đóng hết van nhánh rẽ sau khi kiểm tra xong có thể vô hiệu hoá chức năng cắt của lò.",
    ]))
    b.append(h4("6.0 Tài liệu tham chiếu"))
    b.append(p("Các tài liệu sau phải có sẵn để hỗ trợ khắc phục sự cố: bản vẽ vòng, phiếu đặc tả thiết bị "
               "đo, và bản mô tả hệ cắt."))
    b.append(h4("7.0 Quy trình kiểm tra từng bước"))
    b.append(p("Tham chiếu bản phác kèm theo (Hình 16-6) cùng bản mô tả hệ cắt."))
    b.append(table(
        ["Bước", "Hành động", "OK"],
        [["1", "Thông báo cho toàn bộ nhân sự vận hành cụm biết buổi kiểm tra sắp bắt đầu.", ""],
         ["2", "Mở hết van nhánh rẽ khí mồi HV-25. Xác nhận báo động nhánh rẽ ZA-25 trên BPCS. Xác nhận "
               "đã nhận báo động.", ""],
         ["3", "Mở hết van nhánh rẽ khí đốt HV-26. Xác nhận báo động nhánh rẽ ZA-26 trên BPCS. Xác nhận "
               "đã nhận báo động.", ""],
         ["4", "Xác nhận lại rằng lò vẫn đang vận hành ổn định.", ""],
         ["5", "Đóng van cách ly quá trình của PT-7. Xả áp từ từ về phía biến đổi. Hai van cắt khí mồi và "
               "hai van cắt khí đốt phải cắt tại 5 psig. Ghi lại áp suất cắt. Xác nhận cả bốn van đã đóng "
               "hết. Xác nhận thời gian đóng nhỏ hơn 3 giây.", ""],
         ["6", "Xác nhận báo động PAL-7 đã hiện trên bảng thông báo phòng điều khiển chính và trên BPCS. "
               "Xác nhận đã nhận báo động.", ""],
         ["7", "Cấp áp lại cho PT-7.", ""],
         ["8", "Báo động PAL-7 phải tan. Xác nhận.", ""],
         ["9", "Đặt lại solenoid của bốn van cắt. Các van phải mở lại ngay. Xác nhận.", ""],
         ["10", "Lặp lại các bước 5 đến 9 cho PT-24.", ""],
         ["11", "Đóng hết van nhánh rẽ khí mồi HV-25. Xác nhận báo động ZA-25 trên BPCS đã tan.", ""],
         ["12", "Đóng hết van nhánh rẽ khí đốt HV-26. Xác nhận báo động ZA-26 trên BPCS đã tan.", ""],
         ["13", "Thông báo cho toàn bộ nhân sự vận hành rằng buổi kiểm tra cắt cho PT-7 và PT-24 đã xong.",
          ""],
         ["14", "Điền đầy đủ, ký và chuyển tài liệu đã hoàn thành cho kỹ sư nhà máy để rà soát và lưu hồ "
                "sơ.", ""]],
        caption="Các bước của quy trình kiểm tra cắt", cls="tbl chk"))
    b.append(p("<b>Kết quả / Ghi chú / Thiếu sót:</b>"))
    b.append(p("Người hoàn thành kiểm tra cắt: ____________________  Ngày: __________"))
    b.append(p("<b>Vận hành:</b> nếu áp suất ở PT-7 hoặc PT-24 xuống dưới 5 PSIG thì các van XV-30A, "
               "XV-30B, XV-31A và XV-31B sẽ đóng trong vòng 3 giây."))

    # ------------------------------------------------------------------ summary
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p("Tình huống lò nung trong chương này cho thấy cách dùng những chất liệu và kỹ thuật đã trình "
               "bày ở Chương 1 đến Chương 15 để đặc tả, thiết kế, lắp đặt, chạy thử và bảo trì một hệ an "
               "toàn điển hình. Các mục sau của mô hình vòng đời đã được xử lý cho ứng dụng này:"))
    b.append(ul([
        "xác định SIL mục tiêu cho từng SIF;",
        "lập đặc tả yêu cầu an toàn (SRS);",
        "thiết kế khái niệm SIS;",
        "phân tích chi phí vòng đời;",
        "kiểm chứng thiết kế khái niệm có đạt SIL;",
        "thiết kế chi tiết;",
        "lắp đặt, chạy thử và kiểm tra trước khởi động;",
        "quy trình vận hành và bảo trì.",
    ]))

    b.append(h2("Ghi chú của người dịch", "Translator's note"))
    b.append(note(
        "<b>Bốn điểm cần lưu ý khi đọc chương này.</b><br><br>"
        "(1) <b>Bảng 16-4</b> trong bản gốc được in ở đầu mục 16.7, nhưng chính mục 16.6 đã nói «Kèm theo. "
        "(Xem Bảng 16-4)» khi bàn tới sơ đồ nguyên nhân – kết quả. Ở đây bảng được đặt lại vào cuối mục "
        "16.6, đúng chỗ nó được viện dẫn lần đầu; số hiệu bảng giữ nguyên.<br><br>"
        "(2) <b>Bước 12</b> của quy trình kiểm tra trong bản gốc ghi «Xác nhận báo động ZA-25 trên BPCS đã "
        "tan» — nhưng bước 12 nói về van nhánh rẽ khí đốt HV-26, nên báo động phải là <b>ZA-26</b>. Đây là "
        "lỗi in của sách; bản dịch đã sửa và giữ nguyên cách hiểu đúng.<br><br>"
        "(3) <b>Bảng 16-7</b> trong bản gốc có bốn cột (vật tư, nhân công, tổng, tạm tính) nhưng chỉ hai "
        "dòng được tách vật tư và nhân công; các dòng còn lại chỉ in một con số. Bản dịch giữ nguyên như "
        "in, không tự suy ra phần tách còn thiếu. Các phép cộng đã được kiểm lại: chi phí cố định 116.000 "
        "$ và chi phí hằng năm 26.500 $ đều khớp; 26.500 × [1 − 1,05<sup>−20</sup>]/0,05 = 330.249 $; tổng "
        "446.249 $.<br><br>"
        "(4) <b>Mục 16.9</b> chỉ phân tích chức năng SIL 3; hai chức năng SIL 2 (lưu lượng thấp nhánh A và "
        "nhánh B) không được tính trong sách. Con số MTTF<sub>sp</sub> tổng 2,0 năm là kết quả của "
        "1/(1/12,5 + 1/2,5 + 1/100) = 1/0,49 ≈ 2,04 năm — sách làm tròn xuống 2,0."))
    return "".join(b)


# ====================================================================== EN
def body_en():
    b = []
    b.append(p("Chapters 1 to 15 each handed over one piece of a procedure. This chapter is where the "
               "pieces get assembled: a crude unit charge heater, followed from process hazard analysis "
               "to a quarterly test procedure, through all eight lifecycle steps. The emphasis is on the "
               "method, not on the answer."))
    b.append(fig(1, F.fig_16_1(), "en"))
    b.append(p("The chapter is worth reading as a whole because of something no single chapter could "
               "show — how much of the engineering is bookkeeping. Six tables, one P&ID, four block "
               "diagrams and a fourteen-step checklist. The safety argument is not won by a clever "
               "calculation; it is won by the fact that the calculation, the cause-and-effect sheet and "
               "the test procedure all refer to the same four valves by the same names."))
    b.append(p("The plant itself is an ordinary crude unit charge heater: two feed passes, a fuel gas "
               "train through a knock-out drum, and pilot gas on its own pressure control. Every loop on "
               "it belongs to the BPCS, which sits two hundred feet away in the control room."))
    b.append(fig(2, F.fig_16_2(), "en"))
    b.append(p("What the SIS adds is deliberately small, and seeing how small is the best preparation for "
               "the arithmetic that follows: three transmitters, one logic block, four trip valves and a "
               "hard-wired manual switch. Everything else on the drawing already existed."))
    b.append(fig(3, F.fig_16_3(), "en"))

    b.append(h2("The numbers that decide the design"))
    b.append(p("Two of them do most of the work, and both are small. The pilot gas function needs SIL 3 "
               "because a pilot flame failure can explode the furnace and kill people; the two pass-flow "
               "functions need SIL 2 because the worst credible outcome is a million-dollar tube failure "
               "or a million-dollar fire. That single split in Table 16-2 is what produces the asymmetry "
               "in the whole design: only the pilot gas group gets 1oo2 transmitters, only it gets a "
               "1oo2 valve pair on both the pilot and the fuel gas."))
    b.append(fig(4, F.fig_16_4(), "en"))
    b.append(p("The second number is the demand rate. Once a year, stated in section 16.3 almost in "
               "passing, is what makes every PFD in section 16.9 a simple multiplication. At one demand "
               "per year, with a three-month proof test, the average probability of failure on demand is "
               "the failure rate times the undetected fraction times the common-cause factor times half "
               "the test interval. No Markov model, no numerical integration, no software. The chapter's "
               "arithmetic fits on one page because the demand rate made it possible to fit on one page."))

    b.append(h2("What the PFD calculation actually reveals"))
    b.append(p("Follow the three terms. The transmitters contribute 6.25 × 10⁻⁶. The safety PLC "
               "contributes 5 × 10⁻⁵. The valves contribute 2.5 × 10⁻⁴. The valves are forty times the "
               "PLC and forty times the transmitters put together."))
    b.append(p("The design response is visible in Figure 16-5 and it is worth naming: the PFD covers "
               "four valves, not two, because losing the pilots requires shutting both the pilot gas and "
               "the fuel gas. That is a correct and easily missed detail — the function is not 'close "
               "XV-30A/B', it is 'close everything that can feed this fire box'. Counting only the pilot "
               "valves would have understated the PFD by half and, more importantly, would have described "
               "the wrong function on the cause-and-effect sheet."))
    b.append(fig(5, F.fig_16_5(), "en"))
    b.append(p("And the result is 3.06 × 10⁻⁴ against a SIL 3 limit of 1 × 10⁻³. That is a margin of "
               "about three, which sounds comfortable until you notice where it comes from: the margin "
               "exists because the valves are 1oo2 and tested quarterly. Change the test interval to "
               "annual and the valve term becomes 1 × 10⁻³ on its own — the function fails SIL 3 with "
               "nothing else altered. The test interval is not a maintenance detail. It is a design "
               "parameter, and it is the one that actually holds the SIL up."))

    b.append(h2("The spurious trip budget is the tighter constraint"))
    b.append(p("Section 16.3 sets two requirements, and they pull in opposite directions: no more than "
               "one nuisance trip per year, and SIL 3. Everyone remembers the SIL 3. Almost nobody "
               "remembers the nuisance trip limit, and it is the harder of the two."))
    b.append(p("The calculation gives 2.0 years between spurious trips, against a requirement of one per "
               "year. That is a factor of two in hand — but look at the terms. The transmitters are "
               "12.5 years, the PLC is 100 years, and the valves are 2.5 years. The valves are again the "
               "binding term, and this time the arithmetic is unforgiving: four valves at λs = 0.1 per "
               "year give 1/(4 × 0.1) = 2.5 years, and no amount of transmitter redundancy improves it. "
               "The only lever is the safe failure rate of the valves themselves."))
    b.append(p("This is the same lesson Chapter 14 taught with its two cost cases, arriving here from a "
               "different direction: the final element dominates both the safety case and the "
               "availability case, and it is the component most often left until last. A project that "
               "spends its redundancy budget on 2oo3 transmitters and a fault-tolerant PLC, and then buys "
               "the cheapest available shutdown valves, has optimised the wrong end of the loop."))

    b.append(h2("Why the SRS table is the most important artefact"))
    b.append(p("Table 16-3 is thirty-odd rows of mostly one-line answers, and it looks like paperwork. It "
               "is not. Read down the 'Details' column and notice how many rows say 'Refer to Table "
               "16-4'. The SRS is deliberately refusing to restate the cause-and-effect sheet, and that "
               "refusal is the point: there is exactly one place where the trip points live, and every "
               "other document points at it."))
    b.append(p("The rows that are not pointers are the ones that decide whether the system can be tested. "
               "De-energise to trip. Manual reset solenoids. Limit switches to confirm closure. Smart "
               "transmitters for diagnostics. Bypass valves for on-line testing, with alarms in the BPCS. "
               "Five seconds response. Every one of those is a decision about how the plant will be "
               "operated for the next twenty years, taken at the specification stage, and each one is "
               "much cheaper to take now than to retrofit."))
    b.append(p("The bypass row deserves particular attention because it is the row that makes the rest of "
               "the chapter possible. Without HV-25 and HV-26, the only way to prove the trip works is to "
               "trip the furnace — which means it gets proved rarely, or not at all. With them, the proof "
               "test is a fourteen-step procedure an operator can run in an afternoon. The bypass is not "
               "a concession to convenience; it is what buys the three-month test interval that the PFD "
               "calculation depends on."))
    b.append(fig(6, F.fig_16_6(), "en"))

    b.append(h2("The test procedure as a safety document"))
    b.append(p("Look at what the fourteen steps actually do. Steps 2 and 3 open the bypasses and confirm "
               "the bypass alarms. Step 4 confirms the furnace is still stable. Only then does step 5 vent "
               "PT-7. Step 6 checks the annunciator. Steps 7 to 9 restore, reset and confirm. Step 10 "
               "repeats the whole thing for PT-24. Steps 11 and 12 close the bypasses and confirm the "
               "alarms cleared."))
    b.append(p("The order is the safety argument. The bypass alarm is verified before the bypass is relied "
               "on, and the bypass closure is verified after the test — because a bypass left open is a "
               "disabled shutdown function, and section 5.0 of the procedure says so in as many words: "
               "'Failure to close the bypass valves fully upon completing the test can disable the "
               "furnace shutdown functions.' That sentence is the whole reason the procedure exists in "
               "written form."))
    b.append(p("There is also a defect worth noticing, because noticing it is a habit worth building. "
               "Step 12 closes the fuel gas bypass HV-26 and then asks the operator to confirm that alarm "
               "ZA-25 has cleared. ZA-25 is the pilot gas bypass alarm; the fuel gas one is ZA-26. The "
               "book has a typo, and an operator following it literally would confirm the wrong alarm and "
               "sign the sheet. This translation corrects it to ZA-26 and says so in the translator's "
               "note. Procedures are code; typos in code get executed."))

    b.append(h2("What the case study leaves out, and why it matters"))
    b.append(p("Section 16.4 is unusually honest about scope. It lists eight lifecycle steps as in scope "
               "and then names four that are not: lifecycle planning, functional safety management, "
               "verification activities, and functional safety assessment. The chapter does the "
               "engineering and skips the management system that is supposed to surround it."))
    b.append(p("That omission is deliberate for a textbook and unacceptable in a project. The eight steps "
               "produce a design; the four omitted activities produce the evidence that the design was "
               "done competently, by people with defined roles and demonstrated competence, with "
               "documentation under control, and with an independent assessment before startup. A plant "
               "that installs this exact SIS without the four missing activities has the same hardware "
               "and none of the assurance."))
    b.append(p("Which is the right way to read the whole chapter: as a worked example of the technical "
               "steps, not as a template for a project. The tables tell you what to produce. They do not "
               "tell you who signs, who checks, or who is allowed to change the cause-and-effect sheet "
               "after commissioning — and those three questions are where real safety instrumented "
               "systems fail."))
    return "".join(b)
