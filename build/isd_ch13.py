# -*- coding: utf-8 -*-
"""Book 5, Chapter 13 — Case-Based Reasoning for Safety Evaluation
(EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 95–102.  The chapter presents
case-based reasoning (CBR): the five functional steps, suitability equations
7–10, prior work (Koiranen & Hurme 1997; Chung & Jefferson 1997), the
MS-Excel prototype application (input/output parameters, retrieval), and the
acetic-acid case study — process-level CBR (Tables 28–29, carbonylation vs
oxidation), reactor-system CBR (Figures 8–9 redrawn) and the resulting I_ST
score.
"""

from isd_common import eq, fig, h2, h3, note, ol, p, table
import isdfig as F

PAGES_SRC = 8            # source pages 95–102
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Case-Based Reasoning for Safety Evaluation"
TITLE_VI = "Suy luận dựa trên tình huống trong đánh giá an toàn"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 13.</b> suy luận dựa trên tình huống "
                "(CBR — case-based reasoning) · kho tình huống (case-base) · "
                "truy hồi (retrieval) · độ phù hợp (suitability Y<sub>ij</sub>) · "
                "hệ số trọng số W<sub>i</sub> · độ phù hợp tổng S<sub>R</sub> · "
                "tham số truy hồi vs tham số đầu ra · IChemE Accident Database · "
                "tình huống oxy hóa vs cacbonyl hóa · phản hồi nhiệt (thermal "
                "feedback loop).")
    return ("<b>Key terms.</b> case-based reasoning (CBR) · case-base · "
            "retrieval · suitability (Y<sub>ij</sub>) · weight factor "
            "W<sub>i</sub> · overall suitability S<sub>R</sub> · retrieval "
            "parameters vs output parameters · IChemE Accident Database · "
            "oxidation vs carbonylation cases · thermal feedback loop.")


_D = '<span style="color:#bbb">—</span>'

# Source Table 28 (p. 99): input data of the process-level search.
_T28 = [
    ("Nguyên liệu · Raw material", "TRUE", "9", "methanol"),
    ("Sản phẩm · Product", "TRUE", "9", "acetic acid"),
    ("Loại phản ứng · Reaction type", "FALSE", _D, _D),
    ("Loại nhiệt của phản ứng · Thermic type of reaction", "FALSE", _D, _D),
    ("Pha phản ứng · Phase of reaction", "FALSE", _D, _D),
    ("Chất xúc tác · Catalyst", "FALSE", _D, _D),
    ("ISBL / OSBL", "TRUE", "6", "isbl"),
    ("Hệ thống · System", "FALSE", _D, _D),
    ("Hệ con · Subsystem", "FALSE", _D, _D),
    ("Thiết bị · Equipment", "FALSE", _D, _D),
    ("Chi tiết · Detail", "FALSE", _D, _D),
]

# Source Table 29 (p. 100): output data — the three retrieved cases.
_T29 = [
    "QUÁ TRÌNH · PROCESS",
    ("Nguyên liệu · Raw material", "methanol", "butane", "butane"),
    ("Sản phẩm · Product", "acetic acid", "acetic acid", "acetic acid"),
    ("Loại phản ứng · Reaction type", "carbonylation", "oxidation", "oxidation"),
    ("Loại nhiệt phản ứng · Thermic type", "exo", _D, "exo"),
    ("Pha phản ứng · Phase of reaction", "liquid", "liquid", "liquid"),
    ("Chất xúc tác · Catalyst", _D, "Rh complex", _D),
    ("ISBL / OSBL", "isbl", "isbl", "isbl"),
    "HỆ THỐNG · SYSTEM",
    ("Hệ thống · System", _D, "reaction", "reaction"),
    ("Hệ con · Subsystem", _D, "intermediate storage", "purging feed"),
    ("Thiết bị · Equipment", _D, "tank", "reactor / boiler"),
    ("Chi tiết · Detail", _D, _D, "inlet pipe"),
    "TAI NẠN · INCIDENT",
    ("Sự cố · Incident", "explosion", "fire", "explosion"),
    ("Nguyên nhân 1 · Cause 1", "static electricity",
     "self-ignition of acetaldehyde", "oxygen leak"),
    ("Nguyên nhân 2 · Cause 2", _D, "filling through vapor phase",
     "methane ignited"),
    ("Khuyến nghị · Recommendations", _D, _D, "fill through bottom"),
    ("Chất · Material", "acetic acid", "acetaldehyde", "butane/air"),
    ("Bản chất chất · Nature of material", "organic acid", "aldehyde", "LPG"),
    ("Chỉ số an toàn (0–5) · Safety Index (0–5)", _D, "4", "5"),
    ("Phụ lục · Appendix", "Phụ lục 1 · App. 1", _D, "Phụ lục 1 · App. 1"),
]


def body_vi():
    b = []

    b.append(h2("13. Suy luận dựa trên tình huống trong đánh giá an toàn",
                "13. Case-Based Reasoning for Safety Evaluation"))

    b.append(p("Khi việc giải bài toán dựa trên kinh nghiệm khó định nghĩa "
               "thành luật tường minh, có thể áp dụng <b>suy luận dựa trên "
               "tình huống (CBR — case-based reasoning)</b>. CBR <b>dùng trực "
               "tiếp các giải pháp của bài toán cũ để giải bài toán mới</b>. "
               "Các bước chức năng của CBR là (Gonzalez và Dankel, 1993):"))
    b.append(ol([
        "Trình bày bài toán mới.",
        "Truy hồi các tình huống giống nhất từ kho tình huống (case-base).",
        "Thích nghi các giải pháp giống nhất để tạo giải pháp cho bài toán hiện tại.",
        "Kiểm chứng giải pháp hiện tại.",
        "Học từ các tình huống bài toán bằng cách thêm giải pháp đã kiểm chứng vào kho tình huống.",
    ]))

    b.append(p("Bảng dữ liệu của kho tình huống có thể chia thành phần <b>đầu "
               "vào</b> và <b>đầu ra</b>: tham số đầu vào là tham số truy hồi, "
               "tham số đầu ra là tham số đặc tả thiết kế. Bài toán được đặc "
               "trưng hóa thành dữ liệu đầu vào của hệ; trong pha truy hồi, "
               "tập giá trị tham số truy hồi của mọi tình huống trong kho được "
               "so sánh với dữ liệu đầu vào; các tình huống giống nhất được "
               "chọn và xếp hạng theo kết quả so sánh."))
    b.append(p("Với dữ liệu kiểu chuỗi, độ phù hợp đơn giản là:"))
    b.append(eq("X<sub>i</sub> = C<sub>i,j</sub> ⇒ Y<sub>i,j</sub> = 1", "(7)"))
    b.append(eq("X<sub>i</sub> ≠ C<sub>i,j</sub> ⇒ Y<sub>i,j</sub> = 0", "(8)"))
    b.append(p("trong đó X<sub>i</sub> là giá trị đầu vào của tham số i, "
               "C<sub>i,j</sub> là giá trị của tham số i của tình huống j, và "
               "Y<sub>i,j</sub> là độ phù hợp của tham số i cho tình huống j. "
               "Chất lượng suy luận tăng lên nếu tầm quan trọng của các tham số "
               "chọn có thể thay đổi được: người dùng xác định tầm quan trọng "
               "của các tham số chọn cho chủ đề đang xét. Độ phù hợp có trọng "
               "số R<sub>ij</sub> được biểu diễn:"))
    b.append(eq("R<sub>ij</sub> = W<sub>i</sub> Y<sub>i,j</sub>", "(9)"))
    b.append(p("với W<sub>i</sub> là hệ số trọng số của tham số chọn i do người "
               "dùng đánh giá. Độ phù hợp tổng được tính cho tình huống j dựa "
               "trên số tham số N và các độ phù hợp tham số R<sub>ij</sub>:"))
    b.append(eq("S<sub>R</sub> = Σ<sub>i=1</sub><sup>N</sup> R<sub>i,j</sub> / N",
                "(10)"))

    b.append(p("CBR đã được dùng trước đây chẳng hạn cho thiết kế thiết bị. "
               "Koiranen và Hurme (1997) dùng CBR cho thiết kế máy trộn chất "
               "lỏng và lựa chọn bộ trao đổi nhiệt ống-vỏ; họ còn đưa ước tính "
               "chất lượng thiết kế vào truy hồi tình huống bên cạnh các yếu "
               "tố kỹ thuật. Chung và Jefferson (1997) đã kết hợp <b>IChemE "
               "Accident Database</b> (Smith và cộng sự, 1997) với CBR để tạo "
               "truy hồi dữ liệu tự động cho nhà thiết kế và vận hành viên; "
               "họ hướng tới hệ thông minh tự động tìm các thuật ngữ liên quan "
               "(ví dụ \"hỏng hóc thiết bị điện\") và truy hồi thông tin liên "
               "quan, tích hợp với công cụ của nhà thiết kế, vận hành và bảo "
               "trì. Mục tiêu của hệ của Chung và Jefferson là tìm mọi nguyên "
               "nhân liên quan của tai nạn quá khứ để cải tiến quá trình, "
               "trong khi hệ CBR của chúng tôi hướng tới suy luận về <b>cấu "
               "trúc quá trình</b> và các đặc tính thuận/lợi bất lợi cho mục "
               "đích thiết kế sơ bộ; cơ sở dữ liệu của họ là cơ sở dữ liệu tai "
               "nạn, còn cơ sở của chúng tôi chứa cả <b>khuyến nghị thiết "
               "kế</b>; hệ của họ dành cho phạm vi rộng hơn — từ nhà thiết kế, "
               "vận hành đến đội bảo trì — còn hệ của chúng tôi dành riêng cho "
               "nhà thiết kế quá trình."))

    # ---- 13.1 ----------------------------------------------------------------
    b.append(h3("13.1 Mô tả ứng dụng nguyên mẫu",
                "13.1 Description of Prototype Application"))

    b.append(p("Ứng dụng CBR nguyên mẫu được xây dựng trên bảng tính "
               "<b>MS-Excel</b>, tổ chức trên nhiều sheet. Một cơ sở dữ liệu "
               "tình huống được tạo, gồm các tình huống tai nạn thu thập từ "
               "tài liệu (ví dụ Lees (1996) và Loss Prevention Bulletin) và "
               "các khuyến nghị thiết kế; chương trình gồm các hàm truy hồi "
               "dùng để lấy các tình huống phù hợp nhất từ cơ sở dữ liệu."))

    b.append(h3("13.1.1 Tham số đầu vào và đầu ra",
                "13.1.1 Input and Output Parameters"))

    b.append(p("Phạm vi tìm kiếm được định nghĩa bằng các mức <b>quá trình, "
               "quá trình con, hệ thống, hệ con, thiết bị và chi tiết</b> làm "
               "tham số đầu vào. Cấu trúc phân cấp này dùng để làm rõ cấu trúc "
               "quá trình và giúp sử dụng phép tương tự quá trình khả thi hơn "
               "trong suy luận — ví dụ một thiết bị ngưng tụ có các đặc tính "
               "an toàn nhất định không phụ thuộc quá trình chứa nó. Bên cạnh "
               "cấu trúc quá trình, tham số đầu vào gồm nguyên liệu, sản phẩm "
               "và một số chi tiết phản ứng; tầm quan trọng của các tham số "
               "được đánh giá bằng hệ số trọng số."))
    b.append(p("Tham số đầu ra chứa tham số đầu vào cùng thông tin về đặc tính "
               "an toàn của quá trình và thông tin về tai nạn cùng nguyên nhân "
               "của chúng; các khuyến nghị thiết kế cụ thể nằm trong đầu ra. "
               "Về tai nạn, đầu ra mô tả:"))
    b.append(("<ul>"
              "<li>loại sự cố nào đã xảy ra;</li>"
              "<li>nguyên nhân thực sự của sự cố là gì;</li>"
              "<li>các yếu tố hoặc hoàn cảnh góp phần vào sự cố;</li>"
              "<li>cách cải thiện ứng dụng để an toàn hơn.</li>"
              "</ul>"))
    b.append(p("Mọi tình huống lưu trữ đều được kiểm chứng trên cơ sở chỉ số "
               "cấu trúc quá trình an toàn; các kiểm chứng cho mọi tình huống "
               "và được đưa vào đầu ra. Thông tin thêm cho ở các phụ lục mô tả "
               "tình huống chi tiết hơn."))

    b.append(h3("13.1.2 Truy hồi tình huống", "13.1.2 Retrieval of Cases"))

    b.append(p("Trong công trình này, các tình huống được lưu trên các worksheet "
               "MS-Excel riêng và được sao chép lên sheet tính toán truy hồi "
               "trong pha truy hồi. Mọi tham số truy hồi đều là <b>tham số "
               "chuỗi</b> nên so sánh giữa kho và bài toán đầu vào rất đơn "
               "giản: giá trị đầu vào bằng giá trị tình huống → khoảng cách "
               "là 1, ngược lại là 0. Độ phù hợp có trọng số tính theo "
               "Phương trình 9 với hệ số trọng số do người dùng nhập; độ phù "
               "hợp tổng tính theo Phương trình 10; các tình huống được xếp "
               "hạng theo độ phù hợp tổng và <b>năm tình huống gần nhất</b> "
               "được hiển thị cho người dùng trên worksheet đầu ra."))
    b.append(p("Truy hồi có thể thực hiện nhiều bước: bước một là đánh giá quá "
               "trình với các tình huống đã lưu — qua đó thấy được quá trình "
               "an toàn hơn hay kém an toàn hơn các quá trình thay thế; bước "
               "hai là đánh giá an toàn của các hệ thống, hệ con hoặc thiết bị "
               "cụ thể; cơ sở dữ liệu chứa khuyến nghị cải tiến để tránh tai "
               "nạn lặp lại. Đánh giá có thể mở rộng tới mức chi tiết — kể cả "
               "chi tiết thiết bị hay van an toàn v.v."))

    # ---- 13.2 ----------------------------------------------------------------
    b.append(h3("13.2 Nghiên cứu tình huống", "13.2 Case Study"))

    b.append(p("Để đánh giá cấu trúc quá trình an toàn của quá trình axit "
               "axetic (Chương 12, Hình 7), các tìm kiếm CBR được thực hiện "
               "trên hai mức (Heikkilä và cộng sự, 1998): mức một là quá trình "
               "axit axetic như một tổng thể; mức hai là hệ lò phản ứng được "
               "nghiên cứu chi tiết hơn."))

    b.append(h3("13.2.1 CBR ở mức quá trình", "13.2.1 CBR on Process Level"))

    b.append(p("Trước tiên, quá trình axit axetic được nghiên cứu như một tổng "
               "thể để tìm xem các quá trình thay thế có khác nhau về an toàn "
               "ở mức khái niệm (mức quá trình) hay không. Tìm kiếm (Bảng 28) "
               "tìm thấy các tình huống cho quá trình cacbonyl hóa và oxy hóa "
               "(Bảng 29). Có thể thấy <b>cả hai loại nhà máy đều đã có nổ và "
               "cháy</b>. Vụ nổ ở nhà máy cacbonyl hóa do <b>điện tĩnh khi "
               "đổ đầy bồn chứa</b> — loại nổ này không đặc hữu cho nhà máy "
               "cacbonyl hóa mà có thể xảy ra trong nhiều quá trình khác. Các "
               "vụ cháy và nổ ở nhà máy oxy hóa <b>liên quan đến hóa chất</b> "
               "trong quá trình đó — có nhiều khả năng xảy ra hơn ở loại nhà "
               "máy này. Vì vậy, dựa trên thông tin từ tìm kiếm này, quá trình "
               "cacbonyl hóa có thể được coi <b>an toàn hơn quá trình oxy "
               "hóa</b>."))
    b.append(table(("Tham số truy hồi", "Kích hoạt", "Tầm quan trọng", "Giá trị"),
              _T28, "Bảng 28 · Dữ liệu đầu vào của tìm kiếm cho quá trình axit axetic."))
    b.append(table(("Thuộc tính", "Tình huống 1", "Tình huống 2", "Tình huống 3"),
              _T29,
              "Bảng 29 · Dữ liệu đầu ra của tìm kiếm cho quá trình axit axetic. "
              "Phụ lục 1: vụ nổ xảy ra do oxy nguyên chất lọt vào lò hơi khí "
              "và trộn với butan và hơi nước dùng để tạo axit axetic; vụ nổ "
              "thứ nhất gần lò hơi khí, vụ thứ hai tại lò phản ứng gần đó "
              "(3 người chết, 37 người bị thương)."))

    b.append(h3("13.2.2 CBR ở hệ lò phản ứng", "13.2.2 CBR on the Reactor System"))

    b.append(p("Trong pha hai, các tìm kiếm được thực hiện ở mức hệ thống và hệ "
               "con — cần cho so sánh các phương án quá trình và cho thiết kế "
               "lò phản ứng tỏa nhiệt cùng hệ truyền nhiệt. Cacbonyl hóa "
               "methanol là phản ứng tỏa nhiệt nên chỉ tìm các lò phản ứng "
               "tỏa nhiệt. Tìm kiếm CBR tìm thấy hai tình huống — các khuyến "
               "nghị chung về thiết kế lò phản ứng tỏa nhiệt với hệ truyền "
               "nhiệt, trình bày ở Hình 8 và 9."))
    b.append(p("Tình huống ở Hình 8 là lò phản ứng với hai hệ làm mát khác "
               "nhau. Trong trường hợp <b>không khuyến nghị</b> (bên phải), hệ "
               "làm mát tạo một <b>vòng phản hồi</b> giữa mức tăng nhiệt của "
               "lò phản ứng và mức tăng nhiệt độ coolant — điều cần tránh. Bên "
               "trái là hệ khuyến nghị, nơi nhiệt độ coolant <b>không phụ "
               "thuộc</b> nhiệt độ lò phản ứng."))
    b.append(fig(1, F.fig_c13_cooling()))
    b.append(p("Tình huống ở Hình 9 là hệ thu hồi nhiệt của lò phản ứng. "
               "Trường hợp <b>không khuyến nghị</b> (bên trái): cấp feed cho lò "
               "phản ứng tỏa nhiệt được sấy nóng <b>bằng sản phẩm</b> — mức "
               "tăng nhiệt độ trong lò có thể dẫn tới mức tăng nhiệt độ feed. "
               "Trường hợp khuyến nghị (bên phải) an toàn hơn vì <b>liên kết "
               "nhiệt bị đứt</b>: truyền nhiệt được thực hiện bằng cách sinh và "
               "dùng hơi áp trung."))
    b.append(fig(2, F.fig_c13_preheat()))

    b.append(h3("13.2.3 Điểm của chỉ số cấu trúc quá trình an toàn",
                "13.2.3 Score of the Safe Process Structure Subindex"))

    b.append(p("Từ suy luận ở mức quá trình, quá trình cacbonyl hóa nhận "
               "<b>điểm 2</b> (không có dữ liệu hoặc trung tính), vì tình huống "
               "tìm thấy không đặc hữu cho quá trình này. Với quá trình oxy "
               "hóa, điểm là <b>5</b>, vì đã xảy ra tai nạn lớn. Với hệ lò phản "
               "ứng khuyến nghị, điểm có thể là <b>0</b> (được khuyến nghị/"
               "tiêu chuẩn) hoặc <b>1</b> (thực hành kỹ thuật tốt) tùy cách "
               "định giá các khuyến nghị này."))
    b.append(p("Điểm cuối của chỉ số cấu trúc quá trình an toàn cho quá trình "
               "cacbonyl hóa sẽ là <b>2</b> dựa trên suy luận giới hạn này, vì "
               "điểm cuối của I<sub>ST</sub> được chọn theo trường hợp xấu "
               "nhất. Dĩ nhiên, trong thực tế nên thực hiện suy luận trên tất "
               "cả các hệ thống và hệ con của quá trình; nghiên cứu tình huống "
               "này chỉ nhằm minh họa nguyên lý CBR khi suy luận giá trị của "
               "chỉ số cấu trúc quá trình an toàn."))

    b.append(note("Kết quả: cacbonyl hóa I<sub>ST</sub> = 2 (trung tính) vs "
                  "oxy hóa I<sub>ST</sub> = 5 (tai nạn lớn); hệ lò phản ứng "
                  "theo khuyến nghị cho điểm 0–1. Điểm cuối theo trường hợp "
                  "xấu nhất = 2 cho quá trình axit axetic trong phạm vi suy "
                  "luận này."))

    return "".join(b)


def body_en():
    b = []

    b.append(h2("13. Case-Based Reasoning for Safety Evaluation",
                "13. Suy luận dựa trên tình huống trong đánh giá an toàn"))

    b.append(p("When problem solving is based on experience which is difficult "
               "to define as explicit rules, it is possible to apply "
               "<b>case-based reasoning (CBR)</b>. CBR <b>uses directly the "
               "solutions of old problems to solve new problems</b>. The "
               "functional steps in CBR are (Gonzalez and Dankel, 1993):"))
    b.append(ol([
        "New problem presentation.",
        "Retrieval of the most similar cases from the case-base.",
        "Adaptation of the most similar solutions for generating a solution "
        "for the current problem.",
        "Validation of the current solution.",
        "Learning from the problem cases by adding the verified solution into "
        "the case-base.",
    ]))

    b.append(p("A data table of a case-base can be divided into <b>input</b> "
               "and <b>output</b> sections: the input parameters are retrieval "
               "parameters and the output parameters are design specification "
               "parameters. The problem is characterized as input data to the "
               "system; in the retrieval phase the set of retrieval-parameter "
               "values of all cases in the case-base is compared to the input "
               "data; the most similar cases are then selected and ranked "
               "based on the comparison."))
    b.append(p("In the case of string data types the suitability is simply:"))
    b.append(eq("X<sub>i</sub> = C<sub>i,j</sub> ⇒ Y<sub>i,j</sub> = 1", "(7)"))
    b.append(eq("X<sub>i</sub> ≠ C<sub>i,j</sub> ⇒ Y<sub>i,j</sub> = 0", "(8)"))
    b.append(p("where X<sub>i</sub> is the input value of parameter i, "
               "C<sub>i,j</sub> the value of parameter i of case j, and "
               "Y<sub>i,j</sub> the suitability of parameter i for case j. The "
               "quality of reasoning increases if the importance of the "
               "selection parameters can be altered: the user should determine "
               "the importances of the selection parameters for the topic "
               "under study. The weighted suitability R<sub>ij</sub> can be "
               "expressed:"))
    b.append(eq("R<sub>ij</sub> = W<sub>i</sub> Y<sub>i,j</sub>", "(9)"))
    b.append(p("where W<sub>i</sub> is the weight factor of selection "
               "parameter i evaluated by the user. The overall suitability can "
               "be calculated for case j based on the number of parameters N "
               "and the parametric suitabilities R<sub>ij</sub>:"))
    b.append(eq("S<sub>R</sub> = Σ<sub>i=1</sub><sup>N</sup> R<sub>i,j</sub> / N",
                "(10)"))

    b.append(p("Case-based reasoning has earlier been used, for instance, for "
               "equipment design. Koiranen and Hurme (1997) used CBR for "
               "fluid-mixer design and for the selection of shell-and-tube "
               "heat exchangers, including an estimation of design quality for "
               "case retrieval beside technical factors. Chung and Jefferson "
               "(1997) combined the <b>IChemE Accident Database</b> (Smith et "
               "al., 1997) with CBR to create an automatic data retrieval for "
               "designers' and operators' use; they intend to develop an "
               "intelligent system which takes, for example, the term "
               "\"electrical equipment failure\", works out all the related "
               "terms and retrieves the relevant information automatically, "
               "integrated with the computer tools of designers, operators and "
               "maintenance engineers. The aim of their system is to find all "
               "relevant causes of past accidents to improve processes, "
               "whereas our CBR system is intended for reasoning on the "
               "<b>structure of a process</b> and its favourable and "
               "unfavourable characteristics for preliminary process design; "
               "their database is an accident database, whereas ours contains "
               "also <b>design recommendations</b>; their system is developed "
               "for wider use — from plant designers and operators to "
               "maintenance teams — while ours is intended specifically for "
               "process designers."))

    # ---- 13.1 ----------------------------------------------------------------
    b.append(h3("13.1 Description of Prototype Application",
                "13.1 Mô tả ứng dụng nguyên mẫu"))

    b.append(p("The prototype CBR application has been implemented on an "
               "<b>MS-Excel</b> spreadsheet, organized on several sheets. A "
               "database of cases was created, consisting of accident cases "
               "collected from the literature (e.g. Lees (1996) and the Loss "
               "Prevention Bulletin) and of design recommendations; the "
               "application includes retrieval functions used to retrieve the "
               "most suitable cases from the database."))

    b.append(h3("13.1.1 Input and Output Parameters",
                "13.1.1 Tham số đầu vào và đầu ra"))

    b.append(p("The scope of a database search is defined by using the "
               "categories <b>process, subprocess, system, subsystem, "
               "equipment and detail</b> as input parameters. This hierarchy "
               "is used to clarify the process structure and to make the use "
               "of process analogies more feasible in reasoning — e.g. a "
               "condenser has certain safety characteristics independent of "
               "the process it is located in. Beside the process structures, "
               "the input parameters include the raw materials and products "
               "and some reaction details; the importance of the parameters "
               "may be evaluated using weighting factors."))
    b.append(p("The output parameters contain the input parameters plus "
               "information on the safety characteristics of the process and "
               "information on accidents and their causes; specific design "
               "recommendations are included in the output. On accidents, the "
               "output describes:"))
    b.append(("<ul>"
              "<li>what kind of incidents have happened;</li>"
              "<li>what is the actual cause of the incident;</li>"
              "<li>what are the contributing factors or circumstances;</li>"
              "<li>how to improve the application for better safety.</li>"
              "</ul>"))
    b.append(p("All stored cases are validated on the basis of the Safe "
               "Process Structure Subindex; the validations are given for "
               "every case and included in the output. Further information is "
               "given as appendices, which describe the case in more detail."))

    b.append(h3("13.1.2 Retrieval of Cases", "13.1.2 Truy hồi tình huống"))

    b.append(p("In this work the cases are stored on their own MS-Excel "
               "worksheets and copied onto a retrieval calculation sheet "
               "during the retrieval phase. All retrieval parameters are "
               "<b>textual string parameters</b>, so the comparison between "
               "the case-base and the input problem is simple: when the input "
               "value equals the case value the distance is 1, otherwise 0. "
               "The weighted suitability is calculated by Equation 9 with the "
               "weighting factors introduced by the user; the overall "
               "suitability by Equation 10. The cases are ranked according to "
               "their overall suitability and <b>the five nearest cases</b> "
               "are shown to the user on an output worksheet."))
    b.append(p("The retrieval of cases can be done in several steps: the first "
               "step is the evaluation of the process with the stored cases — "
               "this shows whether the process is safer or unsafer than the "
               "alternative processes; the second step is the safety "
               "evaluation of specific process systems, subsystems or pieces "
               "of equipment; the database contains improvement "
               "recommendations to avoid the same accidents happening again. "
               "The evaluation can be extended to the detailed level — even "
               "equipment details or safety valves can be checked at this "
               "level."))

    # ---- 13.2 ----------------------------------------------------------------
    b.append(h3("13.2 Case Study", "13.2 Nghiên cứu tình huống"))

    b.append(p("For the evaluation of the safe process structure of the acetic "
               "acid process (Ch. 12, Fig. 7), CBR database searches were done "
               "on two levels (Heikkilä et al., 1998): the first level was the "
               "acetic acid process as a whole; on the second level the "
               "reactor system was studied in more detail."))

    b.append(h3("13.2.1 CBR on Process Level", "13.2.1 CBR ở mức quá trình"))

    b.append(p("First the acetic acid process was studied as a whole, to find "
               "out whether the alternative processes differ in safety at the "
               "conceptual (i.e. process) level. The search (Table 28) found "
               "cases for carbonylation and oxidation processes (Table 29). It "
               "can be seen that <b>there have been explosions and fires on "
               "both types of plants</b>. The explosion in the carbonylation "
               "plant was due to <b>static electricity in the loading of a "
               "storage vessel</b> — this type of explosion is not specific to "
               "carbonylation plants but is possible in many other processes. "
               "The fires and explosions in the oxidation plants were "
               "<b>related to the chemicals present</b> in that process — they "
               "are more likely to happen in such a plant than somewhere else. "
               "Thus, based on the information from this search, the "
               "carbonylation process can be considered <b>safer than the "
               "oxidation process</b>."))
    b.append(table(("Retrieval parameters", "Active", "Importance", "Value"),
              _T28, "Table 28 · Input data of the search for the acetic acid "
              "process."))
    b.append(table(("Attribute", "1st case", "2nd case", "3rd case"),
              _T29,
              "Table 29 · Output data of the search for the acetic acid "
              "process. Appendix 1: the explosion occurred because pure "
              "oxygen entered a gas-fired boiler and mixed with the butane and "
              "steam used to form acetic acid; the first blast occurred near "
              "the gas-fired boiler and the second at a nearby reactor "
              "(3 killed, 37 injured)."))

    b.append(h3("13.2.2 CBR on the Reactor System",
                "13.2.2 CBR ở hệ lò phản ứng"))

    b.append(p("In the second phase, searches were made on the system and "
               "subsystem level — needed for the comparison of process "
               "alternatives and for the design of the exothermic reactor and "
               "its heat-transfer systems. Carbonylation of methanol is an "
               "exothermic reaction, so only exothermal reactors were "
               "searched. The CBR search found two cases — general "
               "recommendations on the design of exothermic reactors with "
               "heat-transfer systems, shown in Figures 8 and 9."))
    b.append(p("The case in Figure 8 represents a reactor with two different "
               "cooling systems. In the <b>not recommended</b> case (right), "
               "the cooling system presents a <b>feedback loop</b> between a "
               "reactor heat rise and the rise in the coolant temperature, "
               "which should be avoided. On the left is the recommended "
               "system, where the coolant temperature <b>does not depend</b> "
               "on the reactor temperature."))
    b.append(fig(1, F.fig_c13_cooling()))
    b.append(p("The case in Figure 9 shows a heat-recovery system of a "
               "reactor. In the <b>not recommended</b> case (left), the feed "
               "to an exothermic reactor is heated <b>by the product</b>: a "
               "temperature rise in the reactor may lead to a temperature rise "
               "in the feed. The recommended case (right) is safer since the "
               "connection is broken — the heat transfer is done by generating "
               "and using medium-pressure steam."))
    b.append(fig(2, F.fig_c13_preheat()))

    b.append(h3("13.2.3 Score of the Safe Process Structure Subindex",
                "13.2.3 Điểm của chỉ số cấu trúc quá trình an toàn"))

    b.append(p("From the reasoning on the process level we get <b>score 2</b> "
               "(no data or neutral) for the carbonylation process, since the "
               "found case was not specific to this process. For the oxidation "
               "process we get <b>score 5</b>, since a major accident has "
               "taken place. For the recommended reactor system we can get "
               "<b>scores 0</b> (recommended/standard) <b>or 1</b> (sound "
               "engineering practice), depending on how we value these "
               "recommendations."))
    b.append(p("The final score of the Safe Process Structure Subindex for the "
               "carbonylation process would be <b>2</b> based on this limited "
               "reasoning, since the final score of I<sub>ST</sub> is chosen "
               "on the basis of the worst case. Of course, in practice one "
               "should reason on all the systems and subsystems of the "
               "process; this case study was given only to represent the "
               "principle of CBR in reasoning the value of the Safe Process "
               "Structure Subindex."))

    b.append(note("Result: carbonylation I<sub>ST</sub> = 2 (neutral) vs "
                  "oxidation I<sub>ST</sub> = 5 (major accident); the "
                  "recommended reactor system scores 0–1. The final score on "
                  "the worst-case basis = 2 for the acetic acid process within "
                  "this limited reasoning."))

    return "".join(b)
