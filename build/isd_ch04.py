# -*- coding: utf-8 -*-
"""Book 5, Chapter 4 — Some Safety Analysis Methods for Process Plant Design
(EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 19–24.  Four subsections (4.1 Dow
Fire and Explosion Hazard Index, 4.2 Mond Index, 4.3 Hazop, 4.4 PIIS) plus
Table 1 on p. 24.  The chapter has NO figures in the source; the two vector
graphics in `isdfig.py` (`fig_c04_stages`, `fig_c04_indices`) are explicitly
labelled editorial schematics drawn from the prose.
"""

from isd_common import (fig, h2, h3, note, p, table, ul)
import isdfig as F

PAGES_SRC = 6           # source pages 19–24
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Some Safety Analysis Methods for Process Plant Design"
TITLE_VI = "Một số phương pháp phân tích an toàn trong thiết kế nhà máy quá trình"


# ---- Source-derived tables -------------------------------------------------
def _t_prelim(lang):
    """The five other preliminary methods named on pp. 19–20 (Wells et al., 1993)."""
    if lang == "vi":
        hdr = ["Ký hiệu", "Tên phương pháp", "Mục đích và thời điểm"]
        rows = [
            ("CSR", "Rà soát an toàn khái niệm (Concept Safety Review)",
             "Đánh giá sớm các mối nguy về an toàn, sức khỏe và môi trường; góp phần vào "
             "quyết định như <b>địa điểm đặt nhà máy và lộ trình ưu tiên</b>."),
            ("CHA", "Phân tích mối nguy khái niệm (Concept Hazard Analysis)",
             "Nhận diện <b>đặc tính nguy hiểm</b> của dự án đã được ghi nhận trong các sự "
             "cố trước đó — gồm cả mối nguy và các điều kiện nguy hiểm."),
            ("CE", "Khảo sát tới hạn an toàn hệ thống (Critical Examination)",
             "Nghiên cứu sớm <b>ý đồ thiết kế</b> của một phân đoạn chế biến; dùng để loại "
             "bỏ hoặc giảm hệ quả có thể có của một sự kiện nguy hiểm."),
            ("PCA", "Phân tích hệ quả sơ bộ (Preliminary Consequence Analysis)",
             "Nhận diện các tai nạn lớn có thể xảy ra và khảo sát tác động của sự cố lên "
             "một nhà máy cụ thể; tiến hành <b>ngay khi có mô tả sơ đồ dòng quá trình</b>."),
            ("PHA", "Phân tích mối nguy sơ bộ (Preliminary Hazard Analysis)",
             "Nhận diện các mối nguy áp dụng được và hệ quả có thể có của chúng nhằm giảm "
             "rủi ro; cần làm <b>ở giai đoạn thiết kế còn có thể thay đổi</b>."),
        ]
        cap = ("Năm phương pháp phân tích sơ bộ khác (Wells et al., 1993), nguyên bản "
               "tr. 19–20; dùng từ lúc rà soát an toàn khái niệm cho đến khi có sơ đồ dòng "
               "tương đối chắc chắn hoặc P&amp;ID sớm.")
    else:
        hdr = ["Abbrev.", "Method", "Purpose and timing"]
        rows = [
            ("CSR", "Concept Safety Review",
             "Early assessment of safety, health and environmental hazards; contributes "
             "to decisions such as <b>siting and preferred route</b>."),
            ("CHA", "Concept Hazard Analysis",
             "Identifies the <b>hazardous characteristics</b> of the project recognized in "
             "previous incidents — both hazards and hazardous conditions."),
            ("CE", "Critical Examination of System Safety",
             "Early study of the <b>design intent</b> of a particular processing section; "
             "can eliminate or reduce the possible consequences of a hazardous event."),
            ("PCA", "Preliminary Consequence Analysis",
             "Identifies likely major accidents and examines the impact of a possible "
             "accident on a particular plant; carried out <b>as soon as a description of "
             "the process flow diagram is available</b>."),
            ("PHA", "Preliminary Hazard Analysis",
             "Identification of applicable hazards and their possible consequences with "
             "the aim of risk reduction; should be done <b>while design change is still "
             "possible</b>."),
        ]
        cap = ("Five other preliminary safety analysis methods (Wells et al., 1993), "
               "source pp. 19–20; meant for the period from concept safety review until "
               "reasonably firm process flow diagrams or early P&amp;IDs exist.")
    return table(hdr, rows, caption=cap, cls="tbl wide")


def _t_table1(lang):
    """Table 1 (p. 24) — 'The elements included into some safety analysis methods'."""
    if lang == "vi":
        hdr = ["Phương pháp phân tích an toàn", "Các yếu tố của phương pháp"]
        rows = [
            ("Chỉ số cháy và nổ Dow<br><i>Dow Fire and Explosion Index</i>",
             "<b>Hệ số vật liệu (MF):</b> tính dễ cháy và khả năng phản ứng.<br>"
             "<b>Mối nguy quá trình chung:</b> phản ứng hóa học tỏa nhiệt, quá trình thu "
             "nhiệt, bốc dỡ và vận chuyển vật liệu, cụm thiết bị kín hoặc trong nhà, lối "
             "tiếp cận khu vực, tiêu thoát và kiểm soát tràn đổ.<br>"
             "<b>Mối nguy quá trình đặc biệt:</b> vật liệu độc, áp suất dưới khí quyển, "
             "vận hành trong hoặc gần vùng dễ cháy, nổ bụi, áp suất xả, nhiệt độ thấp, "
             "lượng vật liệu dễ cháy và không bền, ăn mòn và xói mòn, rò rỉ tại mối nối "
             "và đệm kín, lò đốt, hệ thống dầu nóng, thiết bị quay."),
            ("Chỉ số Mond<br><i>Mond Index</i>",
             "Hệ số vật liệu · mối nguy vật liệu đặc biệt · mối nguy quá trình chung · "
             "mối nguy quá trình đặc biệt · hệ số lượng · mối nguy mặt bằng · mối nguy độc tính."),
            ("Phân tích mối nguy và khả năng vận hành<br><i>HAZOP</i>",
             "Nhận diện các nhiễu loạn quá trình bằng <b>từ dẫn</b>: Không / không có; "
             "nhiều hơn, ít hơn; cũng như; một phần của; ngược lại; khác với; sớm hơn, "
             "muộn hơn; nơi khác."),
            ("Chỉ số nguyên mẫu an toàn nội tại<br><i>PIIS</i>",
             "<b>Điểm hóa học:</b> tồn lượng, tính dễ cháy, tính nổ, độc tính.<br>"
             "<b>Điểm quá trình:</b> nhiệt độ, áp suất, hiệu suất.<br>"
             "<b>Tổng điểm:</b> tổng của điểm hóa học và điểm quá trình."),
        ]
        cap = ("Bảng 1 (nguyên bản tr. 24) — các yếu tố được đưa vào một số phương pháp "
               "phân tích an toàn. Giữ nguyên cấu trúc hai cột của nguyên bản.")
    else:
        hdr = ["Safety analysis method", "Elements of the method"]
        rows = [
            ("Dow Fire and Explosion<br>Index",
             "<b>Material factor:</b> flammability and reactivity.<br>"
             "<b>General process hazards:</b> exothermic chemical reactions, endothermic "
             "processes, material handling and transfer, enclosed or indoor process units, "
             "access to the area, drainage and spill control.<br>"
             "<b>Special process hazards:</b> e.g. toxic materials, sub-atmospheric "
             "pressure, operation in or near flammable range, dust explosion, relief "
             "pressure, low temperature, quantity of flammable and unstable materials, "
             "corrosion and erosion, leakage in the cases of joints and packing, use of "
             "fired heaters, hot oil exchange systems, rotating equipment."),
            ("Mond Index",
             "Material factor · Special material hazards · General process hazards · "
             "Special process hazards · Quantity factor · Layout hazards · Toxicity hazards."),
            ("Hazard and Operability<br>Analysis (HAZOP)",
             "Identification of process disturbances with the <b>guide words</b>: No, not; "
             "more, less; as well as; part of; reverse; other than; sooner, later; other place."),
            ("Prototype Index of Inherent<br>Safety (PIIS)",
             "<b>Chemical score:</b> inventory, flammability, explosiveness and toxicity.<br>"
             "<b>Process score:</b> temperature, pressure and yield.<br>"
             "<b>Total score:</b> sum of the chemical and process scores."),
        ]
        cap = ("Table 1 (source p. 24) — the elements included into some safety analysis "
               "methods. The two-column structure of the original is kept.")
    return table(hdr, rows, caption=cap, cls="tbl wide")


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 4.</b> Dow F&amp;EI — Chỉ số cháy và nổ Dow · "
                "MF — hệ số vật liệu · UHF — hệ số mối nguy đơn vị · GPH / SPH — mối nguy "
                "quá trình chung / đặc biệt · Mond Index — Chỉ số Mond · Hazop — phân tích "
                "mối nguy và khả năng vận hành · guide words — từ dẫn · PIIS — Chỉ số "
                "nguyên mẫu an toàn nội tại · CSR / CHA / CE / PCA / PHA — các phương pháp "
                "sơ bộ · P&amp;ID — sơ đồ đường ống và thiết bị đo.")
    return ("<b>Key terms.</b> Dow F&amp;EI · MF — material factor · UHF — unit hazard "
            "factor · GPH / SPH — general / special process hazards · Mond Index · Hazop "
            "— Hazard and Operability Analysis · guide words · PIIS — Prototype Index of "
            "Inherent Safety · CSR / CHA / CE / PCA / PHA · P&amp;ID · flowsheet Hazop.")


# ---------------------------------------------------------------------------
def body_vi():
    b = []

    b.append(h2("Tổng quan: phương pháp nào cho giai đoạn nào",
                "Overview: which method for which stage"))
    b.append(p("Đã có nhiều phương pháp phân tích an toàn được phát triển. Một số được "
               "biết đến và kiểm chứng quốc tế, một số được dùng và phát triển ít nhiều "
               "bên trong các công ty. <b>Yêu cầu thông tin của các phương pháp khác "
               "nhau, kết quả tạo ra cũng khác nhau</b>; vì thế mỗi phương pháp phù hợp "
               "với một giai đoạn khác nhau của phát triển quá trình, thiết kế và vận "
               "hành (xem Hình 3 ở chương 3)."))
    b.append(p("Ngành công nghiệp quá trình đã dùng <b>Chỉ số cháy và nổ Dow</b> (DOW, "
               "1987) và <b>Chỉ số Mond</b> (ICI, 1985) trong nhiều năm. Hai chỉ số này "
               "đánh giá mức độ nguy hiểm cháy nổ của nhà máy, là phương pháp đánh giá "
               "nhanh dùng trong quá trình phát triển quá trình và nhà máy, cũng như "
               "trong thiết kế mặt bằng. Chúng <b>phù hợp nhất ở các giai đoạn thiết kế "
               "muộn</b>, khi đã biết thiết bị, hóa chất và điều kiện quá trình."))
    b.append(p("<b>Hazop</b> (Kletz, 1992) là phương pháp phổ biến khác, nhưng Hazop "
               "thông thường được xây dựng để nhận diện nhiễu loạn quá trình khi đã có "
               "<b>sơ đồ quá trình và sơ đồ thiết bị đo hoàn chỉnh</b>, nên không mấy "
               "dùng được cho thiết kế sơ bộ. Kletz cũng nhắc đến <i>Hazop sơ đồ dòng</i> "
               "dùng được trong thiết kế sơ bộ, nhưng nó không được dùng rộng rãi. Phương "
               "pháp hữu dụng hơn ở giai đoạn sơ bộ là <b>PIIS</b> (Edwards và Lawrence, "
               "1993), vốn được phát triển để <b>chọn lộ trình quá trình an toàn</b>."))
    b.append(fig(1, F.fig_c04_stages()))

    b.append(h2("Năm phương pháp phân tích sơ bộ khác",
                "Five other preliminary methods"))
    b.append(p("Các phương pháp phân tích an toàn sơ bộ khác gồm rà soát an toàn khái "
               "niệm (CSR), khảo sát tới hạn an toàn hệ thống (CE), phân tích mối nguy "
               "khái niệm (CHA), phân tích hệ quả sơ bộ (PCA) và phân tích mối nguy sơ bộ "
               "(PHA) (Wells et al., 1993). Các phương pháp này được thiết kế để thực "
               "hiện <b>từ lúc rà soát an toàn khái niệm cho đến khi có sơ đồ dòng quá "
               "trình tương đối chắc chắn hoặc P&amp;ID sớm</b>."))
    b.append(_t_prelim("vi"))
    b.append(p("Bốn phương pháp được khảo sát kỹ hơn dưới đây là Chỉ số cháy và nổ Dow, "
               "Chỉ số Mond, Hazop và PIIS; các yếu tố của chúng cũng được trình bày ở "
               "Bảng 1 (cuối chương)."))

    b.append(h2("4.1 Chỉ số cháy và nổ Dow", "4.1 Dow Fire and Explosion Hazard Index"))
    b.append(p("Mục đích của Chỉ số cháy và nổ Dow (Dow, 1987) là: <b>1)</b> định lượng "
               "mức hư hỏng kỳ vọng của các sự cố cháy nổ tiềm ẩn bằng những thuật ngữ "
               "thực tế; <b>2)</b> nhận diện thiết bị có khả năng góp phần tạo ra hoặc "
               "leo thang sự cố; và <b>3)</b> truyền đạt tiềm năng rủi ro cháy nổ cho "
               "ban quản lý. <b>Chỉ số Dow là tích của Hệ số mối nguy đơn vị (UHF) và "
               "Hệ số vật liệu (MF)</b> (Bảng 1)."))
    b.append(p("<b>Hệ số vật liệu MF</b> của đơn vị quá trình được lấy theo chất nguy "
               "hiểm nhất hiện diện, dẫn tới phân tích <b>trường hợp xấu nhất có thể "
               "thực sự xảy ra</b>. MF biểu thị cường độ giải phóng năng lượng từ vật "
               "liệu hoặc hỗn hợp vật liệu nguy hiểm nhất có mặt với lượng đáng kể trong "
               "quá trình; nó suy từ tính dễ cháy và khả năng phản ứng của các chất. "
               "Quá trình được chia thành các đơn vị và MF được tính riêng cho từng "
               "đơn vị. Dow (1987) đã lập danh mục nhiều hợp chất và vật liệu kèm giá "
               "trị MF."))
    b.append(p("<b>Hệ số mối nguy đơn vị</b> là tích của mối nguy quá trình chung và "
               "mối nguy quá trình đặc biệt. Các hệ số phạt của <b>mối nguy quá trình "
               "chung</b> liên quan đến phản ứng hóa học tỏa nhiệt, quá trình thu nhiệt, "
               "bốc dỡ và vận chuyển vật liệu, cụm thiết bị kín hoặc đặt trong nhà, lối "
               "tiếp cận khu vực, tiêu thoát và kiểm soát tràn đổ. <b>Mối nguy quá trình "
               "đặc biệt</b> gồm các hệ số cho vật liệu độc, áp suất dưới khí quyển, vận "
               "hành trong hoặc gần vùng dễ cháy, nổ bụi, áp suất xả, nhiệt độ thấp, "
               "lượng vật liệu dễ cháy và không bền, ăn mòn và xói mòn, rò rỉ tại mối "
               "nối và đệm kín, lò đốt, hệ thống dầu nóng và thiết bị quay."))
    b.append(p("Giá trị các hệ số được xác định theo <i>Dow's Fire &amp; Explosion "
               "Hazard Index Classification Guide</i> (Dow, 1987). Cuốn hướng dẫn gồm "
               "các quy tắc và bảng phủ khá đầy đủ hầu hết chất hóa học và thao tác "
               "đơn vị."))

    b.append(h2("4.2 Chỉ số Mond", "4.2 Mond Index"))
    b.append(p("Chỉ số Mond (ICI, 1985) được phát triển từ phiên bản năm 1973 của Chỉ số "
               "Dow F&amp;E. Theo Lees (1996), các sửa đổi chính gồm: <b>1)</b> khảo sát "
               "được phạm vi rộng hơn của quá trình và công trình lưu trữ; <b>2)</b> bao "
               "phủ chế biến hóa chất có tính nổ; <b>3)</b> cải thiện xem xét mối nguy "
               "đối với hydro; <b>4)</b> bổ sung mối nguy quá trình đặc biệt; và "
               "<b>5)</b> đưa <b>độc tính</b> vào đánh giá."))
    b.append(p("Trong Chỉ số Mond, nhà máy được chia thành các đơn vị riêng lẻ dựa trên "
               "<b>khả năng tạo ra các rào ngăn cách</b> — vì thế một trong các yếu tố "
               "được xét là <b>mặt bằng nhà máy</b>. Mối nguy tiềm ẩn được biểu diễn "
               "bằng giá trị ban đầu của một bộ chỉ số về cháy, nổ và độc tính. Sau đó "
               "tiến hành <b>rà soát hệ số mối nguy</b> để xem các thay đổi thiết kế có "
               "giảm mối nguy không, và xác định các giá trị trung gian của chỉ số. Cuối "
               "cùng áp dụng <b>các hệ số bù trừ</b> cho đặc điểm phòng ngừa và bảo vệ, "
               "rồi tính giá trị cuối cùng của các chỉ số, gọi là <b>chỉ số đã bù trừ</b> "
               "(offset indices). Các yếu tố của phương pháp Mond được liệt kê ở Bảng 1."))

    b.append(h2("4.3 Phân tích mối nguy và khả năng vận hành (Hazop)",
                "4.3 Hazard and Operability Analysis (Hazop)"))
    b.append(p("Hazop (Kletz, 1992) là một trong những phương pháp phân tích an toàn "
               "được dùng nhiều nhất trong công nghiệp quá trình, và là một trong những "
               "cách <b>đơn giản nhất</b> để nhận diện mối nguy. Hazop rà soát nhà máy "
               "<b>từng bình chứa đến từng bình chứa, từng đường ống đến từng đường "
               "ống</b>; với mỗi bình và mỗi ống, nhận diện các nhiễu loạn có thể và hệ "
               "quả tiềm ẩn của chúng."))
    b.append(p("Hazop dựa trên các <b>từ dẫn</b> (guide words) như <i>không, nhiều hơn, "
               "ít hơn, ngược lại, khác với</i>, được hỏi cho mọi đường ống và bình chứa "
               "(Bảng 1). Mục đích của từ dẫn là <b>kích thích trí tưởng tượng</b>, và "
               "phương pháp này <b>phụ thuộc rất nhiều vào chuyên môn của người thực "
               "hiện</b>. Ý tưởng đằng sau các câu hỏi là mọi nhiễu loạn trong nhà máy "
               "hóa chất đều có thể mô tả bằng các biến trạng thái vật lý. Hazop có thể "
               "dùng ở nhiều giai đoạn thiết kế nhưng <b>ở chế độ hạn chế</b>; một nghiên "
               "cứu Hazop đầy đủ đòi hỏi bản thiết kế quá trình cuối cùng với sơ đồ dòng "
               "và P&amp;ID."))
    b.append(p("Kletz (1991) nêu một khác biệt quan trọng giữa <b>Hazop thông thường "
               "trên sơ đồ đường ống (P&amp;ID)</b> và <b>Hazop trên sơ đồ dòng</b> (tức "
               "khái niệm quá trình): ở Hazop thông thường, sai lệch so với điều kiện "
               "thiết kế được coi là không mong muốn và người ta tìm cách ngăn chúng; "
               "còn ở Hazop sơ đồ dòng, sai lệch cũng được tạo ra nhưng thực chất là để "
               "<b>tìm ra các phương án quá trình mới</b>. Dù đã có nhiều mô tả chi tiết "
               "về Hazop thông thường, gần như không có công bố nào về kết quả chi tiết "
               "của Hazop sơ đồ dòng (so với Hình 3 ở chương 3, nơi Hazop bị coi là ít "
               "dùng trong thiết kế khái niệm). Dẫu vậy, mối quan tâm với Hazop sơ đồ "
               "dòng đang tăng lên nhờ khả năng <b>liên kết Hazop trên máy tính với hệ "
               "thống thiết kế hỗ trợ bằng máy tính</b>, cho phép làm Hazop sơ bộ ngay "
               "trong khi thiết kế."))
    b.append(p("Dù Hazop thông thường là kỹ thuật mạnh để nhận diện mối nguy và vấn đề "
               "vận hành, nó <b>đến quá muộn để có thể thực hiện các thay đổi lớn</b>. "
               "Tiêu chuẩn Hazop sắp ra đời (IEC 61882, 1999) khuyến nghị tiến hành "
               "nghiên cứu Hazop <b>xuyên suốt vòng đời</b> của hệ thống, nhưng với giai "
               "đoạn khái niệm và định nghĩa thì lại đề xuất các phương pháp cơ bản khác "
               "(xem Hình 3)."))

    b.append(h2("4.4 Chỉ số nguyên mẫu an toàn nội tại (PIIS)",
                "4.4 Prototype Index of Inherent Safety (PIIS)"))
    b.append(p("Edwards và Lawrence (1993) phát triển <b>Chỉ số nguyên mẫu an toàn nội "
               "tại (PIIS)</b> cho thiết kế quá trình. Chỉ số này nhằm phân tích "
               "<b>việc lựa chọn lộ trình quá trình</b> — tức nguyên liệu sử dụng và "
               "trình tự các bước phản ứng. Phương pháp <b>thiên rất nhiều về phản ứng</b> "
               "và không xét đúng mức các phần còn lại của quá trình, dù chúng thường "
               "chiếm đa số thiết bị."))
    b.append(p("PIIS được tính là một <b>tổng điểm</b> bằng tổng của <b>điểm hóa học</b> "
               "và <b>điểm quá trình</b> (Bảng 1). Điểm hóa học gồm tồn lượng, tính dễ "
               "cháy, tính nổ và độc tính; điểm quá trình gồm nhiệt độ, áp suất và hiệu "
               "suất. Một số điểm dựa trên các bảng tương tự trong Chỉ số Dow và Mond; "
               "các điểm khác được xây bằng cách <b>chia miền giá trị của một thông số "
               "thành các khoảng và gán điểm cho mỗi khoảng</b> — và dự kiến sẽ được "
               "sửa đổi trong tương lai."))
    b.append(p("Có ý kiến cho rằng một chỉ số an toàn nội tại tổng hợp như PIIS hàm chứa "
               "<b>một dạng phán đoán sẵn</b> về tầm quan trọng tương đối của các loại "
               "mối nguy. Người dùng hoặc phải <b>chấp nhận phán đoán của người phát "
               "triển chỉ số</b>, hoặc phải sửa đổi chỉ số để đưa phán đoán của mình vào "
               "— nhưng khi đó <b>kết quả không còn so sánh được</b> với người dùng khác "
               "(Hendershot, 1997). PIIS cũng có thể dùng nguyên dạng, hoặc các yếu tố "
               "được <b>trọng số hóa</b> bởi người dùng. Hendershot (1997) ưa một hệ "
               "trong đó các yếu tố đóng góp được đánh giá bằng các chỉ số đã biết như "
               "Chỉ số Dow F&amp;E, còn các phương án được so sánh chẳng hạn bằng phương "
               "pháp Kepner-Tregoe (Kepner và Tregoe, 1981). Tuy nhiên cần nhớ rằng "
               "<b>ngay cả Chỉ số Dow F&amp;E cũng chứa phán đoán sẵn</b> về tầm quan "
               "trọng của các số hạng."))
    b.append(p("PIIS có một số <b>ưu điểm rõ rệt</b> so với các chỉ số số học khác ở giai "
               "đoạn thiết kế sớm, vì nó dùng được khi <b>phần lớn thông tin chi tiết về "
               "quá trình vẫn còn thiếu</b>."))
    b.append(fig(2, F.fig_c04_indices()))

    b.append(h2("Bảng 1 — các yếu tố của bốn phương pháp",
                "Table 1 — elements of the four methods"))
    b.append(p("Bảng 1 của nguyên bản (tr. 24) liệt kê các yếu tố được đưa vào bốn "
               "phương pháp vừa khảo sát. Bảng dưới đây giữ nguyên cấu trúc hai cột và "
               "toàn bộ nội dung của nguyên bản."))
    b.append(_t_table1("vi"))
    b.append(note("Chi tiết cần lưu ý (nhận xét biên tập): đoạn văn §4.3 nêu năm từ dẫn "
                  "(<i>không, nhiều hơn, ít hơn, ngược lại, khác với</i>), trong khi Bảng "
                  "1 liệt kê tám nhóm (<i>Không/không có; nhiều hơn, ít hơn; cũng như; "
                  "một phần của; ngược lại; khác với; sớm hơn, muộn hơn; nơi khác</i>). "
                  "Bản dịch giữ nguyên cả hai danh sách đúng vị trí của chúng thay vì "
                  "gộp lại."))

    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 4 chiếm tr. 19–24 của VTT Publications 384 (1999): phần tổng quan "
               "và các phương pháp sơ bộ ở tr. 19–20, §4.1 Dow ở tr. 20–21, §4.2 Mond ở "
               "tr. 21, §4.3 Hazop ở tr. 22, §4.4 PIIS ở tr. 23, và Bảng 1 ở tr. 24. "
               "<b>Nguyên bản không có hình vẽ nào trong chương này</b>; hai sơ đồ B và C "
               "là sơ đồ biên tập dựng lại từ văn bản, đã được ghi rõ trong chú thích "
               "của từng hình."))
    b.append(p("Tài liệu được trích dẫn: DOW (1987), ICI (1985), Kletz (1992, 1991), "
               "Edwards và Lawrence (1993), Wells et al. (1993), Lees (1996), Hendershot "
               "(1997), Kepner và Tregoe (1981), IEC 61882 (1999); danh mục đầy đủ ở phần "
               "Tài liệu tham khảo (tr. 121–129)."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội "
               "dung gốc © 1999 Anna-Mari Heikkilä / VTT (VTT Publications 384).</i>"))
    return "".join(b)


def body_en():
    b = []

    b.append(h2("Overview: which method for which stage",
                "Tổng quan: phương pháp nào cho giai đoạn nào"))
    b.append(p("Several safety analysis methods have been developed already. Some of them "
               "are internationally known and proved, some have been used and developed "
               "more or less inside companies. <b>Information requirements of the methods "
               "are different, also the results produced vary</b>. Thus different safety "
               "methods are suitable for different stages of process development, design "
               "and operation (see Figure 3 in Chapter 3)."))
    b.append(p("Process industry has used the <b>Dow Fire and Explosion Hazard Index</b> "
               "(DOW, 1987) and the <b>Mond Index</b> (ICI, 1985) for many years. These "
               "indices deal with fire and explosion hazard rating of process plants; they "
               "are rapid hazard-assessment methods for use on chemical plant, during "
               "process and plant development, and in the design of plant layout. They are "
               "<b>best suited to later design stages</b> when process equipment, chemical "
               "substances and process conditions are known."))
    b.append(p("Another widely used method is <b>Hazop</b> (Kletz, 1992), but conventional "
               "Hazop was developed to identify probable process disturbances when "
               "<b>complete process and instrumentation diagrams</b> are available, so it "
               "is not very applicable to conceptual process design. Kletz has also "
               "mentioned a <i>Hazop of a flowsheet</i> usable in preliminary process "
               "design, but it is not widely used. A more usable method in preliminary "
               "process design is <b>PIIS</b> (Edwards and Lawrence, 1993), developed to "
               "<b>select safe process routes</b>."))
    b.append(fig(1, F.fig_c04_stages()))

    b.append(h2("Five other preliminary methods",
                "Năm phương pháp phân tích sơ bộ khác"))
    b.append(p("Other possible preliminary safety analysis methods are concept safety "
               "review (CSR), critical examination of system safety (CE), concept hazard "
               "analysis (CHA), preliminary consequence analysis (PCA) and preliminary "
               "hazard analysis (PHA) (Wells et al., 1993). These methods are meant to be "
               "carried out <b>from the time of the concept safety review until such time "
               "as reasonably firm process flow diagrams or early P&amp;IDs are "
               "available</b>."))
    b.append(_t_prelim("en"))
    b.append(p("The four methods discussed here in more detail are the Dow Fire and "
               "Explosion Hazard Index, the Mond Index, Hazop and PIIS; their elements are "
               "also presented in Table 1 at the end of this chapter."))

    b.append(h2("4.1 Dow Fire and Explosion Hazard Index", "4.1 Chỉ số cháy và nổ Dow"))
    b.append(p("The purpose of the Dow Fire and Explosion Hazard Index (Dow, 1987) is to: "
               "<b>1)</b> quantify the expected damage of potential fire and explosion "
               "incidents in realistic terms, <b>2)</b> identify equipment that would be "
               "likely to contribute to the creation or escalation of an incident and "
               "<b>3)</b> communicate the fire and explosion risk potential to management. "
               "<b>The Dow Index is the product of the Unit Hazard Factor and the Material "
               "Factor</b> (Table 1)."))
    b.append(p("The <b>material factor MF</b> for the process unit is taken of the most "
               "hazardous substance present, which leads to the analysis of <b>the worst "
               "case that could actually occur</b>. MF denotes the intensity of energy "
               "release from the most hazardous material or mixture of materials present "
               "in significant quantity in the process; it is obtained from the "
               "flammability and reactivity of the substances. The process is divided "
               "into units and the material factor is calculated for each unit separately. "
               "Dow (1987) has listed a number of chemical compounds and materials with "
               "their MFs."))
    b.append(p("The <b>Unit Hazard Factor</b> for a process unit is the product of general "
               "and special process hazards. Penalties of <b>general process hazards</b> "
               "deal with different exothermic chemical reactions, endothermic processes, "
               "material handling and transfer, enclosed or indoor process units, access "
               "to the area, and drainage and spill control. <b>Special process hazards</b> "
               "contain the factors for toxic materials, sub-atmospheric pressure, "
               "operation in or near flammable range, dust explosion, relief pressure, low "
               "temperature, quantity of flammable and unstable materials, corrosion and "
               "erosion, leakage in the cases of joints and packing, use of fired heaters, "
               "hot oil systems and rotating equipment."))
    b.append(p("The values of the factors are determined on the basis of <i>Dow's "
               "Fire &amp; Explosion Hazard Index Classification Guide</i> (Dow, 1987). "
               "The Guide includes rules and tables which cover well the most chemical "
               "substances and unit operations."))

    b.append(h2("4.2 Mond Index", "4.2 Chỉ số Mond"))
    b.append(p("The Mond Index (ICI, 1985) has been developed from the 1973 version of "
               "the Dow F&amp;E Index. The principal modifications to the Dow method "
               "include (Lees, 1996): <b>1)</b> a wider range of processes and storage "
               "installations can be studied, <b>2)</b> it covers processing of chemicals "
               "having explosive properties, <b>3)</b> improved hazard consideration for "
               "hydrogen, <b>4)</b> additional special process hazards, and <b>5)</b> "
               "<b>toxicity is included into the assessment</b>."))
    b.append(p("In the Mond Index the plant is divided into individual units on the basis "
               "of the <b>feasibility of creating separating barriers</b>; one of the "
               "factors taken into account is therefore <b>plant layout</b>. The potential "
               "hazard is expressed in terms of the initial value of a set of indices for "
               "fire, explosion and toxicity. A <b>hazard factor review</b> is then "
               "carried out to see if design changes reduce the hazard, and intermediate "
               "values of the indices are determined. <b>Offsetting factors</b> for "
               "preventative and protective features are applied and the final values of "
               "the indices, or <b>offset indices</b>, are calculated. The elements of the "
               "Mond method are listed in Table 1."))

    b.append(h2("4.3 Hazard and Operability Analysis (Hazop)",
                "4.3 Phân tích mối nguy và khả năng vận hành (Hazop)"))
    b.append(p("Hazard and Operability Analysis (Hazop) (Kletz, 1992) is one of the most "
               "used safety analysis methods in the process industry and one of the "
               "<b>simplest approaches</b> to hazard identification. Hazop involves a "
               "<b>vessel to vessel and a pipe to pipe review</b> of a plant: for each "
               "vessel and pipe the possible disturbances and their potential consequences "
               "are identified."))
    b.append(p("Hazop is based on <b>guide words</b> such as <i>no, more, less, reverse, "
               "other than</i>, which should be asked for every pipe and vessel (Table 1). "
               "The intention of the guide words is to <b>stimulate the imagination</b>, and "
               "the method relies very much on the <b>expertise of the persons performing "
               "the analysis</b>. The idea behind the questions is that any disturbance in "
               "a chemical plant can be described in terms of physical state variables. "
               "Hazop can be used in different stages of process design but <b>in "
               "restricted mode</b>; a complete Hazop study requires final process "
               "plannings with flow sheets and P&amp;IDs."))
    b.append(p("Kletz (1991) pointed out an important difference between a <b>conventional "
               "Hazop of a line diagram (P&amp;ID)</b> and a <b>Hazop of a flowsheet</b> "
               "(the process concept): in a conventional Hazop deviations from design "
               "conditions are assumed to be undesirable and ways of preventing them are "
               "looked for, whereas in a flowsheet Hazop deviations are generated but are "
               "actually looked for <b>to find new process alternatives</b>. Although many "
               "detailed accounts of conventional Hazops have been published, little or "
               "nothing has appeared concerning the detailed results of a flowsheet Hazop "
               "(compare Figure 3 in Chapter 3, which considers Hazop as rarely used in "
               "conceptual design). Still there is a growing interest in flowsheet Hazop "
               "thanks to the ability to <b>link a computerized Hazop to computer aided "
               "design systems</b>, which allows a preliminary Hazop to be done during "
               "design."))
    b.append(p("Even if the conventional Hazop is a powerful technique for identifying "
               "hazards and operating problems, it <b>comes too late for major changes to "
               "be made</b>. In the forthcoming Hazop standard (IEC 61882, 1999) Hazop "
               "studies are recommended to be carried out <b>throughout the life cycle</b> "
               "of a system — but for the concept and definition phase other basic methods "
               "are suggested (see Figure 3)."))

    b.append(h2("4.4 Prototype Index of Inherent Safety (PIIS)",
                "4.4 Chỉ số nguyên mẫu an toàn nội tại (PIIS)"))
    b.append(p("Edwards and Lawrence (1993) developed a <b>Prototype Index of Inherent "
               "Safety (PIIS)</b> for process design. The inherent safety index is "
               "intended for analysing the <b>choice of process route</b> — the raw "
               "materials used and the sequence of the reaction steps. This method is "
               "<b>very reaction oriented</b> and does not consider properly the other "
               "parts of the process even though they usually represent the majority of "
               "equipment."))
    b.append(p("The PIIS is calculated as a <b>total score</b>, the sum of a <b>chemical "
               "score</b> and a <b>process score</b> (Table 1). The chemical score consists "
               "of inventory, flammability, explosiveness and toxicity; the process score "
               "includes temperature, pressure and yield. Some of the scores are based on "
               "similar tables in the Dow and Mond Indices; others have been constructed "
               "by <b>dividing the domain of values of a parameter into ranges and "
               "assigning a score to each range</b>. They are supposed to be modified in "
               "the future."))
    b.append(p("It has been argued that an overall inherent safety index such as the PIIS "
               "incorporates <b>some kind of built-in judgement</b> of the relative "
               "importance of the various types of hazards. The user has to <b>defer to the "
               "judgement of the developer</b> of the index or modify it to incorporate his "
               "own judgement — in the latter case <b>the results are no longer comparable "
               "with other users</b> (Hendershot, 1997). The PIIS may also be used as such "
               "or the factors may be <b>weighted by the user</b>. Hendershot (1997) "
               "prefers a system where contributory factors are evaluated by known indices "
               "such as the Dow F&amp;E Index and the alternatives are compared e.g. by the "
               "Kepner-Tregoe method (Kepner and Tregoe, 1981). We should keep in mind, "
               "however, that <b>even the Dow F&amp;E Index includes built-in judgement</b> "
               "on the importance of terms."))
    b.append(p("The PIIS has some <b>clear advantages</b> over some other numerical "
               "indices in early design stages, because it can be used when <b>most of the "
               "detailed process information is still lacking</b>."))
    b.append(fig(2, F.fig_c04_indices()))

    b.append(h2("Table 1 — elements of the four methods",
                "Bảng 1 — các yếu tố của bốn phương pháp"))
    b.append(p("Table 1 of the source (p. 24) lists the elements included into the four "
               "methods just reviewed. The table below keeps the original two-column "
               "structure and all of its content."))
    b.append(_t_table1("en"))
    b.append(note("Detail worth noticing (editorial observation): the prose of §4.3 names "
                  "five guide words (<i>no, more, less, reverse, other than</i>), whereas "
                  "Table 1 lists eight groups (<i>No, not; more, less; as well as; part of; "
                  "reverse; other than; sooner, later; other place</i>). The translation "
                  "keeps both lists in their original places rather than merging them."))

    b.append(h3("About the source", "Về nguồn tài liệu"))
    b.append(p("Chapter 4 occupies pp. 19–24 of VTT Publications 384 (1999): the overview "
               "and preliminary methods on pp. 19–20, §4.1 Dow on pp. 20–21, §4.2 Mond on "
               "p. 21, §4.3 Hazop on p. 22, §4.4 PIIS on p. 23, and Table 1 on p. 24. "
               "<b>The source contains no figures in this chapter</b>; Figures B and C are "
               "editorial schematics reconstructed from the prose and are labelled as such "
               "in their captions."))
    b.append(p("Works cited: DOW (1987), ICI (1985), Kletz (1992, 1991), Edwards and "
               "Lawrence (1993), Wells et al. (1993), Lees (1996), Hendershot (1997), "
               "Kepner and Tregoe (1981), IEC 61882 (1999); the full bibliography is in "
               "the References unit (pp. 121–129)."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © 1999 Anna-Mari Heikkilä / VTT (VTT Publications 384).</i>"))
    return "".join(b)
