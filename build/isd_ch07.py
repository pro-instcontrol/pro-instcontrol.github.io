# -*- coding: utf-8 -*-
"""Book 5, Chapter 7 — Factors Selected to Represent the Inherent Safety in
Preliminary Process Design (EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 39–55.  The chapter introduces the
parameters that represent inherent safety at the conceptual-design stage:
Table 4 (project-stage matrix, after Kletz 1991), Figure 5 (formation of the
index — redrawn as `isdfig.fig_c07_index`), Table 5 (parameter selection by
Edwards & Lawrence 1993 vs Heikkilä et al. 1996), Table 6 (principles ↔ PIIS ↔
ISI mapping) and Sections 7.1–7.9 (heat of reaction, hazardous substances,
corrosiveness, chemical interaction, inventory, temperature, pressure,
equipment safety, safe process structure).
"""

from isd_common import eq, fig, h2, h3, note, p, table
import isdfig as F

PAGES_SRC = 17          # source pages 39–55
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Factors Representing Inherent Safety in Preliminary Design"
TITLE_VI = "Các yếu tố đại diện an toàn nội tại trong thiết kế sơ bộ"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 7.</b> nhiệt phản ứng (ΔH<sub>r</sub>) — "
                "năng lượng tỏa ra từ phản ứng · điểm chớp cháy (flash point) · "
                "giới hạn nổ dưới LEL / trên UEL · TLV — ngưỡng giới hạn phơi "
                "nhiễm · LD<sub>50</sub> / LC<sub>50</sub> — liều/nồng độ gây tử "
                "vong 50% nhóm thử · tốc độ ăn mòn (mm/a) và phần dự trữ ăn mòn · "
                "ma trận tương thích hóa học (EPA, Chempat) · tồn kho (inventory) · "
                "sự giòn hóa ở nhiệt độ thấp (embrittlement) · an toàn thiết bị · cấu trúc quá "
                "trình an toàn · suy luận dựa trên tình huống (case-based "
                "reasoning).")
    return ("<b>Key terms.</b> heat of reaction (ΔH<sub>r</sub>) — energy "
            "released by the reaction · flash point · lower/upper explosion "
            "limits (LEL/UEL) · TLV — Threshold Limit Value · LD<sub>50</sub> / "
            "LC<sub>50</sub> — dose/concentration lethal to 50% of the test "
            "group · corrosion rate (mm/a) and corrosion allowance · chemical "
            "compatibility matrix (EPA, Chempat) · inventory · low-temperature "
            "embrittlement · equipment safety · safe process structure · "
            "case-based reasoning.")


# ---------------------------------------------------------------------------
# Source Table 4 (p. 40): project stages at which each feature of friendly
# design should be discussed (Kletz, 1991).  The single-X rows are placed
# following the source print and the original Kletz (1991) table.
_X = '<b style="color:#1f5f8b">✕</b>'
_D = '<span style="color:#bbb">—</span>'

_T4 = [
    ("Cường tập hóa · Intensification", _X, _X, _D),
    ("Thay thế · Substitution", _X, _X, _D),
    ("Suy yếu · Attenuation", _X, _X, _D),
    "Giới hạn hệ quả · Limitation of effects",
    ("&nbsp;&nbsp;• bằng thiết kế thiết bị · by equipment design", _X, _X, _D),
    ("&nbsp;&nbsp;• bằng thay đổi điều kiện phản ứng · by changing reaction conditions",
     _X, _D, _D),
    ("Đơn giản hóa · Simplification", _X, _X, _D),
    "Tránh hiệu ứng dây chuyền · Avoiding knock-on effects",
    ("&nbsp;&nbsp;• bằng bố trí · by layout", _X, _X, _D),
    ("&nbsp;&nbsp;• bằng cách khác · in other ways", _X, _X, _D),
    ("Không thể lắp sai · Making incorrect assembly impossible", _D, _D, _X),
    ("Làm rõ trạng thái · Making status clear", _D, _D, _X),
    ("Chịu lỗi · Tolerance", _D, _D, _X),
    ("Dễ điều khiển · Ease of control", _X, _X, _D),
    ("Phần mềm · Software", _D, _D, _X),
]

# Source Table 5 (p. 42): inherent safety parameters and their selection.
_T5 = [
    ("Tồn kho · Inventory", "x", "x", "tỷ lệ với công suất · relative to capacity"),
    ("Pha · Phase", _D, _D, "tính chất xả · release property"),
    ("Nhiệt độ · Temperature", "x", "x", _D),
    ("Áp suất · Pressure", "x", "x", _D),
    ("Nhiệt phản ứng chính · Heat of main reaction", _D, "x",
     "sinh nhiệt cao/thấp · high/low heat generation"),
    ("Tạo pha mới · New phase generation", _D, _D, "tạo rắn/khí · solid/gas formation"),
    ("Chất xúc tác · Catalysts", _D, _D, _D),
    ("Phản ứng phụ · Side reactions", _D, "x", "sinh nhiệt · heat generation"),
    ("Sản phẩm thải · Waste products", _D, _D,
     "xét qua các chất · considered by substances"),
    ("Hiệu suất phản ứng · Reaction yield", _D, _D,
     "xét qua tồn kho · considered by inventory"),
    ("Tốc độ phản ứng · Reaction rate", _D, _D,
     "xét qua ΔH<sub>R</sub> · considered by ΔH<sub>R</sub>"),
    ("Độ nhớt · Viscosity", _D, _D, "điểm nóng cục bộ · hot spots"),
    ("Khả cháy · Flammability", "x", "x", "dễ cháy (chất lỏng) · ease of burning (liquid)"),
    ("Tính nổ · Explosiveness", "x", "x", "hỗn hợp khí nổ · explosive gas mixture"),
    ("Ăn mòn · Corrosiveness", _D, "x", "vật liệu kết cấu · construction material"),
    ("Độc tính · Toxicity", "x", "x",
     "tác hại cho cơ thể người · adverse effect on the human body"),
    ("Tương tác hóa học *) · Chemical interaction *)", _D, "x",
     "tính phản ứng · reactivity"),
    ("Loại thiết bị *) · Type of equipment *)", _D, "x",
     "chọn thiết bị · choice of equipment"),
    ("Cấu trúc quá trình an toàn *) · Safety of process structure *)", _D, "x",
     "chọn cấu hình · choice of configuration"),
]

# Source Table 6 (p. 44): characteristics of inherent safety in conceptual
# process design — principles vs PIIS vs ISI.  Assembled row-by-row in
# `_t6_rows()` (VI) / `_t6_rows_en()` (EN) below.


def _t6_rows():
    """Assemble Table 6 rows: group headers + 2-col body rows."""
    rows = []
    g = [
        ("Cường tập hóa<br><i>Intensification</i> — tồn kho, thể tích phản ứng "
         "(inventory, reaction volume)",
         ("tồn kho · inventory",
          "tồn kho, hiệu suất phản ứng · inventory, reaction yield")),
        ("Thay thế<br><i>Substitution</i> — vật liệu an toàn hơn (safer materials)",
         ("khả cháy, tính nổ, độc tính · flammability, explosiveness, toxicity",
          "khả cháy, tính nổ, độc tính, tương tác hóa học · flammability, "
          "explosiveness, toxicity, chemical interaction")),
        ("Suy yếu<br><i>Attenuation</i> — nhiệt độ, áp suất thấp hơn "
         "(lower temperature, pressure)",
         ("nhiệt độ, áp suất · temperature, pressure",
          "nhiệt độ, áp suất · temperature, pressure")),
        ("Giới hạn hệ quả<br><i>Limitation of Effects</i> — phương án kỹ thuật và "
         "điều kiện phản ứng an toàn hơn (safer technical alternatives, safer "
         "reaction conditions)",
         ("nhiệt độ, áp suất · temperature, pressure",
          "an toàn thiết bị, cấu trúc quá trình an toàn, áp suất, nhiệt độ, "
          "tương tác hóa học · equipment safety, safe process structure, "
          "pressure, temperature, chemical interaction")),
        ("Đơn giản hóa<br><i>Simplification</i> — đơn giản hóa cơ sở quá trình "
         "(simplify process facilities)",
         (_D, "cấu trúc quá trình an toàn · safe process structure")),
        ("Không thể lắp sai<br><i>Making Incorrect Assembly Impossible</i> — chọn "
         "đúng thiết bị, đường ống và phụ tùng (choice of equipment, piping and "
         "fittings correctly)",
         (_D, "an toàn thiết bị, cấu trúc quá trình an toàn · equipment safety, "
          "safe process structure")),
        ("Chịu lỗi<br><i>Tolerance</i> — chịu được vận hành sai "
         "(resistant to maloperation)",
         (_D, "ăn mòn, an toàn thiết bị, cấu trúc quá trình an toàn · "
          "corrosiveness, equipment safety, safe process structure")),
        ("Dễ điều khiển<br><i>Ease of Control</i>",
         (_D, "cấu trúc quá trình an toàn, nhiệt phản ứng · safe process "
          "structure, heat of reaction")),
    ]
    for head, (piis, isi) in g:
        rows.append(head)
        rows.append((piis, isi))
    return rows


# ---------------------------------------------------------------------------
def body_vi():
    b = []

    b.append(p("Như đã đề cập, <b>sự thiếu thông tin làm công tác xem xét an toàn "
               "trong thiết kế sơ bộ nhà máy quá trình trở nên khó khăn</b>. Vì "
               "vậy cần tận dụng mọi chi tiết sẵn có có thể ảnh hưởng đến an toàn "
               "nội tại của nhà máy. Để làm được điều đó, các đặc tính an toàn nội "
               "tại nên được đánh giá một cách có hệ thống trong suốt quá trình "
               "thiết kế. Cho mục đích này, cần một phương pháp luận chuyên dụng "
               "để ước lượng an toàn nội tại dựa trên lượng thông tin khan hiếm "
               "hiện có."))
    b.append(p("Phần lớn các nguyên tắc an toàn nội tại đều hữu ích ngay ở giai "
               "đoạn thiết kế sơ bộ, dù chi tiết quá trình vẫn còn thiếu nhiều. "
               "Điều này thể hiện ở Bảng 4 — cho biết ở giai đoạn dự án nào mỗi "
               "đặc tính của thiết kế thân thiện nên được xem xét. Thực tế, cơ hội "
               "áp dụng các đặc tính an toàn nội tại giảm dần khi thiết kế tiến "
               "triển (Kletz, 1991). Từ Bảng 4 có thể thấy phần lớn các đặc tính "
               "có thể xem xét ở giai đoạn khái niệm và sơ đồ dòng."))
    hdr4 = ("Đặc tính thiết kế thân thiện (Kletz, 1991)",
            "Giai đoạn<br>khái niệm", "Giai đoạn<br>sơ đồ dòng",
            "Giai đoạn<br>sơ đồ P&amp;ID")
    b.append(table(hdr4, _T4,
                   caption="Bảng 4 · Các giai đoạn dự án mà mỗi đặc tính của thiết kế thân "
                           "thiện nên được thảo luận (Kletz, 1991). Với các hàng chỉ có một dấu "
                           "✕, vị trí cột theo bản in nguồn / bản gốc của Kletz — các quyết định "
                           "chi tiết thiết bị (lắp ráp, trạng thái, chịu lỗi, phần mềm) thuộc giai "
                           "đoạn sơ đồ P&amp;ID."))
    b.append(p("Trong luận văn này, <b>phương pháp dựa trên chỉ số được chọn</b> vì "
               "an toàn nội tại gồm nhiều yếu tố thành phần liên hệ với nhau. Vì "
               "vậy cách biểu diễn trực tiếp nhất là các chỉ số thành phần "
               "(subindex) được gán trọng số theo điểm trung bình, sẽ bàn ở "
               "Chương 9."))
    b.append(fig(1, F.fig_c07_index()))
    b.append(p("Sự hình thành các chỉ số an toàn nội tại dựa trên nguyên tắc sau "
               "(Hình 5): các nguyên tắc cơ bản của an toàn nội tại (mục 6.1) "
               "được mô tả trước thành các tham số (Bảng 5); các tham số quan "
               "trọng nhất được chọn để triển khai thành các chỉ số thành phần "
               "an toàn nội tại."))
    b.append(p("Edwards và Lawrence (1993) đã đưa ra danh sách <b>mười sáu tính "
               "chất hóa lý và tham số quá trình</b> có sẵn ở giai đoạn chọn lộ "
               "trình quá trình (Bảng 5). Bảy trong mười sáu tham số này được họ "
               "đưa vào phương pháp chỉ số (PIIS). Các tham số được chọn tập "
               "trung nhiều vào lộ trình hóa học và bản chất hóa học của quá "
               "trình. Họ cũng đã kiểm chứng lựa chọn bằng đánh giá chuyên gia, "
               "mang lại sự ủng hộ cho công trình (Edwards et al., 1996)."))
    b.append(p("Tuy nhiên an toàn nội tại chịu tác động của <b>cả thiết bị quá "
               "trình lẫn tính chất của các chất hóa học</b> có mặt trong quá "
               "trình, nên chỉ số cũng phải phản ánh điều này. Vì vậy danh sách "
               "tham số (Bảng 5) được bổ sung các tham số đại diện cho khía cạnh "
               "quá trình: loại thiết bị và an toàn cấu trúc quá trình — mô tả "
               "cấu hình quá trình dưới góc nhìn hệ thống. Còn một tham số thứ ba "
               "mô tả tương tác (tính phản ứng) giữa các hóa chất, vì đây là "
               "nguồn rủi ro rõ ràng."))
    hdr5 = ("Tham số an toàn nội tại",
            "E&amp;L<br>(1993)", "Heikkilä et al.<br>(1996)", "Ghi chú")
    b.append(table(hdr5, _T5,
                   caption="Bảng 5 · Các tham số an toàn nội tại. *) Không có trong tài liệu "
                           "tham chiếu Edwards và Lawrence (1993)."))
    b.append(p("Ví dụ <b>tồn kho</b> được cả hai nhóm chọn: nó tỷ lệ với công suất "
               "quá trình và thời gian lưu trong thiết bị, có ảnh hưởng lớn đến "
               "mức độ mối nguy và nên giữ nhỏ bằng cường tập hóa. <b>Pha</b> là "
               "tính chất xả có thể biểu diễn qua tồn kho nên bị loại. <b>Hiệu "
               "suất phản ứng</b> cũng biểu diễn tồn kho, vì hiệu suất cao hơn "
               "giảm tái tuần hoàn và làm nhỏ kích thước lò phản ứng."))
    b.append(p("Cả hai nhóm đều chọn <b>nhiệt độ và áp suất</b>: nhiệt độ là thước "
               "đo trực tiếp năng lượng nhiệt sẵn có lúc xả; áp suất vừa là thước "
               "đo năng lượng lúc xả vừa là năng lượng gây ra việc xả. <b>Nhiệt "
               "phản ứng</b> (Heikkilä et al., 1996) đo năng lượng sẵn có từ "
               "phản ứng — nhiệt phản ứng cao có thể tạo nhiệt độ cao hơn và "
               "phản ứng chạy trốn nguy hiểm. Tham số khác cần cân nhắc về khả "
               "năng điều khiển là tốc độ phản ứng, nhưng nó không biểu diễn "
               "trực tiếp mức nguy hiểm (ví dụ khi nhiệt phản ứng thấp) nên bị "
               "loại khỏi danh sách."))
    b.append(p("<b>Tương tác hóa học</b> cùng nhiệt phản ứng phụ biểu diễn tiềm "
               "năng phản ứng của quá trình. Phản ứng phụ không mong muốn có thể "
               "là trùng hợp nhanh, sinh nhiệt, tạo khí cháy hoặc khí độc. Phản "
               "ứng phụ và rủi ro phản ứng trong hệ lưu trữ được tính qua nhiệt "
               "phản ứng và tương tác hóa học. Cả hai nhóm chọn <b>khả cháy, tính "
               "nổ và độc tính</b> làm tính chất mối nguy của chất; nhóm Heikkilä "
               "thêm <b>ăn mòn</b> vì trong môi trường ăn mòn, chọn đúng vật liệu "
               "kết cấu là yếu tố sống còn của an toàn nội tại."))
    b.append(p("<b>Độ nhớt</b> không được thấy là có ý nghĩa: hiệu ứng điểm nóng "
               "trong lò phản ứng nhớt trộn kém có thể gộp vào tham số nhiệt phản "
               "ứng. <b>Tạo pha mới và chất xúc tác</b> không được chọn vì cả hai "
               "được xét qua tính chất mối nguy của các chất (tương tác hóa học, "
               "tính nổ…); điều này cũng đúng cho tham số sản phẩm thải."))
    b.append(p("Các tham số có ý nghĩa được chọn là: <b>nhiệt phản ứng, khả cháy, "
               "tính nổ, độc tính, ăn mòn, tương tác hóa học, tồn kho, nhiệt độ "
               "và áp suất quá trình, an toàn thiết bị và cấu trúc quá trình an "
               "toàn</b> (Bảng 5). Điều đó không có nghĩa các yếu tố khác là vô "
               "nghĩa — ngược lại, chúng cần được xem xét chi tiết hơn ở các "
               "giai đoạn thiết kế sau."))
    hdr6 = ("Nguyên tắc an toàn nội tại (Kletz, 1991)",
            "PIIS<br>(Edwards &amp; Lawrence, 1993)",
            "ISI<br>(Heikkilä et al., 1996)")
    b.append(table(hdr6, _t6_rows(),
                   caption="Bảng 6 · Các đặc tính của an toàn nội tại trong thiết kế khái niệm "
                           "quá trình."))
    b.append(p("Từ Bảng 6 thấy các tham số được chọn có liên hệ với các nguyên "
               "tắc cơ bản của an toàn nội tại. Ví dụ các chỉ số an toàn thiết bị "
               "và cấu trúc quá trình an toàn chứa nhiều đặc tính cùng lúc như "
               "giới hạn hệ quả hay chịu được vận hành sai. Việc gộp nhiều đặc "
               "tính vào ít tham số là hợp lý vì các nguyên tắc an toàn nội tại "
               "rất rộng và chồng lấn nhau; triết lý đằng sau không thể mô tả chỉ "
               "bởi một tham số quá trình duy nhất. Các tham số được chọn được "
               "bàn chi tiết ở các mục sau."))

    # ---- 7.1 -----------------------------------------------------------------
    b.append(h2("7.1 Nhiệt phản ứng", "7.1 Heat of Reaction"))
    b.append(p("Một phản ứng là tỏa nhiệt nếu sinh nhiệt. Các phản ứng giải phóng "
               "lượng nhiệt hoặc khí lớn là mối nguy tiềm tàng, đặc biệt trong "
               "phân hủy nhanh hay oxy hóa hoàn toàn."))
    b.append(p("Manh mối chính về mức độ dữ dội của phản ứng nằm ở <b>nhiệt giải "
               "phóng, nhiệt độ có thể đạt được và thể tích cùng bản chất của khí "
               "và hơi hình thành</b>. Các đặc tính hóa học làm tăng tiềm năng "
               "nổ: enthalpy phân hủy hoặc phản ứng cao, tốcộc sinh năng lượng "
               "cao. Nói rộng ra, mọi phản ứng có thể làm nhiệt độ tăng 300°C "
               "hoặc sinh ra lượng khí/hơi đáng kể đều là mối nguy lớn (King, "
               "1990; IChemE, 1987)."))
    b.append(p("Chất có enthalpy tạo thành dương sẽ tỏa năng lượng khi phân hủy. "
               "Chất có năng lượng cao nói chung nhận diện được qua các nhóm cấu "
               "trúc phân tử nguy hiểm: nhóm peroxide, nitro, azo, các liên kết "
               "kép và ba. Sự hiện diện của các nhóm này không nhất thiết nghĩa "
               "chất đó nguy hiểm (IChemE, 1987); ngược lại, ban đầu không có "
               "nhóm bất ổn định cũng không bảo đảm ổn định lâu dài. King (1990) "
               "chỉ ra tốc độ phản ứng thường ít hoặc không liên quan đến nhiệt "
               "hay năng lượng sinh ra: một số phản ứng rất nhanh (phản ứng ion "
               "trong dung dịch nước) sinh ít hoặc không sinh nhiệt, trong khi "
               "các phản ứng sinh nhiều nhiệt lại diễn ra rất chậm nếu không có "
               "chất xúc tác. Vì vậy, thay cho tốc độ phản ứng hay sự hiện diện "
               "của nhóm bất ổn định, <b>nhiệt phản ứng được chọn làm tiêu chí</b>."))
    b.append(p("Biến thiên năng lượng (ΔU<sub>r</sub>) trong phản ứng bằng hiệu "
               "giữa năng lượng tạo thành của sản phẩm và chất phản ứng:"))
    b.append(eq("ΔU<sub>r</sub> = Σ(U<sub>f</sub>)<sub>sản phẩm</sub> − "
                "Σ(U<sub>f</sub>)<sub>chất phản ứng</sub>", "(1)"))
    b.append(p("Nếu phản ứng diễn ra trong điều kiện đẳng áp (áp suất không đổi), "
               "năng lượng được thay bằng enthalpy (ΔH<sub>r</sub>) và phương "
               "trình trên viết cho điều kiện thể tích không đổi như sau:"))
    b.append(eq("ΔH<sub>r</sub> = Σ(H<sub>f</sub>)<sub>sản phẩm</sub> − "
                "Σ(H<sub>f</sub>)<sub>chất phản ứng</sub>", "(2)"))

    # ---- 7.2 -----------------------------------------------------------------
    b.append(h2("7.2 Chất nguy hiểm", "7.2 Hazardous Substances"))
    b.append(p("Các chất nguy hiểm trong quá trình được nhận diện dựa trên khả "
               "cháy, tính nổ và độc tính. Khả cháy của khí và hơi của chất lỏng "
               "cháy là mối quan tâm lớn trong công nghiệp quá trình: kết quả "
               "của một mồi lửa có thể là cháy, là nổ, hoặc cả hai. Cháy và nổ "
               "tai thường của hỗn hợp cháy với không khí thường theo sau việc "
               "rò rỉ chất cháy hoặc không khí lọt vào thiết bị."))
    b.append(h3("7.2.1 Khả cháy", "7.2.1 Flammability"))
    b.append(p("Khả cháy nghĩa là mức độ dễ cháy trong không khí của vật liệu "
               "(King, 1990); áp dụng cho khí, lỏng và rắn. Khả cháy rất quan "
               "trọng chẳng hạn trong các trường hợp rò rỉ. Chất lỏng có điểm "
               "chớp cháy thấp hơn nhiệt độ gia công hoặc lưu trữ có thể tạo "
               "hỗn hợp cháy được và nói chung bị coi là nguy hiểm."))
    b.append(p("Khả cháy của chất lỏng phụ thuộc vào giới hạn cháy dưới của vật "
               "liệu và áp suất hơi của nó ở nhiệt độ hiện hành. <b>Điểm chớp "
               "cháy</b> là nhiệt độ thấp nhất mà chất lỏng tỏa đủ hơi cháy gần "
               "bề mặt, sao cho hỗn hợp kín với không khí bén lửa khi có tia lửa "
               "hay ngọn lửa (tức áp suất hơi đủ cao để nồng độ khí đạt giới hạn "
               "cháy dưới). Vì vậy điểm chớp cháy là tham số chính trong phân "
               "loại mối nguy của chất lỏng và các quy định nhà nước dựa trên "
               "nó (Lees, 1996). <b>Điểm sôi</b> có thể lấy làm chỉ dấu của độ "
               "bay hơi; với chất lỏng cháy, điểm sôi là thước đo trực tiếp mối "
               "nguy khi sử dụng (Sax, 1979)."))
    b.append(p("Pháp luật Phần Lan (Pyötsiä, 1994) phân loại khả cháy của hóa "
               "chất dựa trên điểm chớp cháy và điểm sôi — tương tự các chỉ thị "
               "của Liên minh châu Âu về chất nguy hiểm. Cách tiếp cận tương tự "
               "cũng được dùng trong Chỉ số cháy và nổ Dow (1987) và bởi Edwards "
               "và Lawrence (1993)."))
    b.append(h3("7.2.2 Tính nổ", "7.2.2 Explosiveness"))
    b.append(p("Tính nổ ở đây nghĩa là khuynh hướng của hóa chất tạo hỗn hợp nổ "
               "trong không khí. Khi nổ xảy ra trong khí quyển, năng lượng giải "
               "phóng rất nhanh trong thể tích nhỏ, tạo sóng áp suất nghe được. "
               "Nổ là sự giải phóng năng lượng đột ngột và dữ dội; năng lượng đó "
               "bắt nguồn từ năng lượng vật lý hoặc hóa học."))
    b.append(p("Mối nguy từ năng lượng vật lý (áp suất) được xét bởi chỉ số áp "
               "suất, nên ở đây chỉ bàn năng lượng hóa học. Hóa chất nổ có thể "
               "là chất nổ mạnh hoặc khí cháy: chất nổ mạnh chứa sẵn oxy và "
               "không cần oxy ngoài để nổ — được xét qua tham số nhiệt phản ứng; "
               "còn khí cháy (thường hữu cơ) nổ trong không khí dư tạo lượng lớn "
               "CO<sub>2</sub> và H<sub>2</sub>O — được bàn qua tham số tính nổ."))
    b.append(p("Tính nổ của hóa chất được mô tả bằng <b>giới hạn nổ trên và "
               "dưới</b>. Tính nổ của đám mây hơi phụ thuộc đặc biệt vào giới "
               "hạn nổ dưới (LEL) — nồng độ hơi mà đám mây có thể bị kích nổ. "
               "Dải giữa hai giới hạn càng rộng thì xác suất đám mây nằm trong "
               "vùng cháy càng cao, tức xu hướng nổ càng lớn; Edwards và "
               "Lawrence (1993) dùng giới hạn nổ để xác định tính nổ của hóa "
               "chất. Dùng hóa chất có tiềm năng nổ thấp hơn làm quá trình an "
               "toàn nội tại hơn. Các vụ nổ nguy hiểm nhất đến từ những đám mây "
               "lớn chất cháy tìm được mồi lửa — Flixborough (Lees, 1996) là "
               "ví dụ về mức tàn phá của loại sự cố này."))
    b.append(h3("7.2.3 Phơi nhiễm độc tính", "7.2.3 Toxic Exposure"))
    b.append(p("Marshall (1987) và Wells (1980) mô tả độc tính là tính chất phá "
               "hủy sự sống hoặc gây thương tích khi được đưa vào hoặc hấp thụ "
               "bởi sinh vật. Mối nguy độc là thước đo khả năng thiệt hại xảy "
               "ra; nó được xác định bởi tần suất, thời gian phơi nhiễm và nồng "
               "độ hóa chất trong phơi nhiễm."))
    b.append(p("Ước lượng độc tính dựa trên thí nghiệm động vật. Độc tính phụ "
               "thuộc đặc tính vật lý và sinh học của chất, đường xâm nhập "
               "(nuốt, qua da, hít vào) và liều lượng. Phơi nhiễm kéo dài ở mức "
               "thấp với nhiều hóa chất công nghiệp cũng có thể gây bệnh mạn "
               "tính dẫn tới tàn phế nặng hoặc chết sớm (King, 1990). Các mối "
               "nguy sức khỏe cực đoan của vật liệu quá trình là gây ung thư, "
               "gây quái thai và gây đột biến; cần biện pháp đặc biệt khi xử lý "
               "các chất có tính chất này (Fawsett, 1982)."))
    b.append(p("Theo Wells (1980), thuật ngữ độc tính dùng phổ biến nhất là "
               "<b>TLV — Threshold Limit Value</b>: nồng độ trong không khí có "
               "thể hít vào không hại sức khỏe trong năm ngày làm việc liên "
               "tiếp, mỗi ngày 8 giờ. TLV dựa trên các hiệu ứng khác nhau, từ "
               "kích ứng đến tổn thương sinh lý; trong công nghiệp TLV là giá "
               "trị hữu dụng nhất vì mục tiêu bảo vệ người lao động. Ngưỡng mùi "
               "quan trọng khi TLV thấp hơn nồng độ cần để mùi xuất hiện "
               "(Siegell, 1996) — yếu tố then chốt trong kế hoạch ứng cứu khẩn "
               "cấp. Vì pháp luật thường bảo vệ mọi người nói chung, ví dụ pháp "
               "luật Phần Lan (Pyötsiä, 1994) dùng LD<sub>50</sub> và "
               "LC<sub>50</sub> cho độc tính, còn kích ứng và các hiệu ứng khác "
               "xét riêng: <b>LD<sub>50</sub></b> là liều uống hoặc hấp thụ qua "
               "da gây chết 50% nhóm thử trong 14 ngày quan sát; "
               "<b>LC<sub>50</sub></b> là nồng độ trong không khí mà phơi nhiễm "
               "24 giờ hoặc ít hơn gây chết 50% nhóm thử."))

    # ---- 7.3 -----------------------------------------------------------------
    b.append(h2("7.3 Ăn mòn", "7.3 Corrosiveness"))
    b.append(p("Mọi kim loại đều ăn mòn trong những điều kiện nhất định. Ăn mòn "
               "trong gây ra bởi ăn mòn điện ly, rỗ pỉt, ăn mòn mỏi, nứt ứng "
               "suất ăn mòn, dòng điện lạc v.v. Ăn mòn làm giảm độ tin cậy và "
               "toàn vẹn của nhà máy: giảm bền vật liệu, gây rò rỉ; sản phẩm ăn "
               "mòn ảnh hưởng tới vật liệu quá trình, bộ phận chuyển động, hiệu "
               "suất quá trình và gây bám bẩn. Ăn mòn diễn tiến chậm và thường "
               "là mối quan tâm của kỹ sư hơn của chuyên gia an toàn, nhưng nó "
               "đã gây các sự cố thảm khốc với thiệt hại nhân mạng nặng nề "
               "(King, 1990)."))
    b.append(p("Các vấn đề an toàn từ tính chất ăn mòn của dòng quá trình có "
               "thể phòng tránh bằng <b>chọn đúng vật liệu kết cấu</b>. Thiết "
               "kế cơ khí dựa trên giá trị thiết kế quá trình (nhiệt độ, áp "
               "suất) mà vượt quá là không cho phép vì gây hậu quả nguy hiểm. "
               "Bền cơ học của thiết bị giảm dần trong suốt đời quá trình do ăn "
               "mòn; tốc độ ăn mòn đo bằng mm/a. Trong thiết kế thiết bị, ăn "
               "mòn được tính bằng việc chọn vật liệu và <b>phần dự trữ ăn "
               "mòn</b> tương ứng — vật liệu được chọn sao cho phần dự trữ "
               "không bị vượt quá trong thời gian sống của thiết bị. Tốc độ ăn "
               "mòn không phải lúc nào cũng biết được ở giai đoạn thiết kế sơ "
               "bộ, nhưng loại vật liệu thô thường được dự đoán trước. Vì nhu "
               "cầu vật liệu tốt hơn hầu như luôn chỉ ra điều kiện ăn mòn mạnh "
               "hơn, phân loại dựa trên loại vật liệu kết cấu là hợp lý."))
    b.append(p("Chỉ số cháy và nổ Dow (1987) cũng xét rủi ro ăn mòn nhưng trừ "
               "điểm qua các tốc độ ăn mòn không chấp nhận được. Các tiêu chuẩn "
               "thiết kế cũng có khuyến nghị về tốc độ ăn mòn chấp nhận được "
               "(Uhlig và Reviev, 1985)."))

    # ---- 7.4 -----------------------------------------------------------------
    b.append(h2("7.4 Tương tác hóa học", "7.4 Chemical Interaction"))
    b.append(p("Các hóa chất khác nhau trong nhà máy có thể trong điều kiện thuận "
               "lợi phản ứng với nhau hoặc với không khí, nước, gây ra vấn đề "
               "an toàn hoặc kỹ thuật. Tương tác hóa học dựa trên tính phản ứng "
               "của mỗi chất với các chất khác hiện diện trong nhà máy. Là mối "
               "nguy quá trình tiềm tàng, tính phản ứng của bất kỳ chất nào cần "
               "xét trong các ngữ cảnh sau:"))
    b.append(bullet_vi())
    b.append(p("Trong một quá trình, tương tác hóa học hoặc là chủ đích hoặc là "
               "ngoài ý muốn. Phản ứng mong muốn được kiểm soát, ví dụ trong lò "
               "phản ứng. Tương tác hóa học ngoài ý muốn có thể dẫn tới những "
               "bất ngờ khó chịu: sinh nhiệt, cháy, tạo khí vô hại không cháy, "
               "tạo khí độc, tạo khí cháy, nổ, trùng hợp nhanh, hoặc hóa chất "
               "độc hòa tan."))
    b.append(p("Cơ quan Bảo vệ Môi trường Hoa Kỳ, EPA (Hatayama et al., 1980) đã "
               "cung cấp <b>ma trận xác định tính tương thích của chất thải "
               "nguy hiểm</b>: mức tương tác giữa các chất được trình bày cùng "
               "hậu quả phản ứng như sinh nhiệt, cháy, trùng hợp nhanh, tạo khí "
               "cháy v.v. Các ma trận tương tự khác cũng tồn tại, ví dụ Chempat "
               "(Leggett, 1997)."))

    # ---- 7.5 -----------------------------------------------------------------
    b.append(h2("7.5 Tồn kho", "7.5 Inventory"))
    b.append(note("\"Bất kỳ vật liệu nào… khi hiện diện với số lượng lớn đều có "
                  "thể được xếp vào loại nguy hiểm.\" — Wells (1980)"))
    b.append(p("Tổng lượng vật liệu cần lưu trữ ban đầu do kỹ thuật quá trình, "
               "các cân nhắc thương mại và chính trị quyết định, dù các cân nhắc "
               "mối nguy về sau có thể giảm lượng hoặc dẫn tới bố trí cải tiến "
               "hay phân tán kho bãi. Nói chung <b>tồn kho lớn tập trung một chỗ "
               "bất lợi khi cháy hoặc vỡ bồn</b>. Mức độ nghiêm trọng tiềm tàng "
               "có thể giảm bằng giữ tồn kho thấp, làm nhỏ lò phản ứng và tránh "
               "lưu trữ vật liệu tiềm tàng nguy hiểm trong chuỗi tổng hợp (CCPS, "
               "1995a). Ví dụ, lượng lớn khí rất độc và chất lỏng dễ bay hơi là "
               "một trong những sai lầm chính trong vụ Bhopal (King, 1990). Sau "
               "Bhopal và một số vụ khác, chính quyền đã thắt chặt giới hạn tồn "
               "kho khí và chất lỏng cháy."))
    b.append(p("Lượng chất hiện diện trong nhà máy (tồn kho) có ảnh hưởng lớn "
               "đến mức độ mối nguy. Khuyến nghị dùng tồn kho chất nguy hiểm tối "
               "thiểu và xây khu quá trình, lưu trữ xa khu dân cư hoặc khu vực "
               "có thể trở thành dân cư."))

    # ---- 7.6 -----------------------------------------------------------------
    b.append(h2("7.6 Nhiệt độ", "7.6 Temperature"))
    b.append(p("Vận hành trong điều kiện cực đoan có những vấn đề và mối nguy "
               "riêng — cực đoan thường nghĩa là nhiệt độ hoặc áp suất rất thấp "
               "hoặc rất cao. <b>Nhiệt độ là thước đo trực tiếp năng lượng nhiệt "
               "sẵn có lúc xả</b> (Edwards và Lawrence, 1993). Nhiệt độ là yếu "
               "tố quan trọng nhất ảnh hưởng tốc độ phản ứng theo phương trình "
               "Arrhenius: trên thực tế, tăng 10°C làm tăng tốc độ phản ứng riêng "
               "hai đến bốn lần tùy năng lượng hoạt hóa (CCPS, 1995a)."))
    b.append(p("Dùng nhiệt độ cao kết hợp áp suất cao làm tăng mạnh lượng năng "
               "lượng tích trữ trong nhà máy. Nhà máy nhiệt độ cao có những vấn "
               "đề nghiêm trọng về vật liệu kết cấu; nhiệt độ cao nghĩa là nhà "
               "máy chịu ứng suất nhiệt, đặc biệt trong khởi động và dừng. Nhà "
               "máy nhiệt độ thấp cũng chịu ứng suất nhiệt vì cùng lý do — các "
               "ứng suất này cần được tính đến và càng xa càng tốt tránh được."))
    b.append(p("Nhà máy nhiệt độ thấp chứa lượng lớn chất lỏng chỉ giữ trạng "
               "thái lỏng nhờ áp suất và nhiệt độ; nếu vì lý do gì không giữ "
               "được lạnh, các chất lỏng bắt đầu bay hơi. Mối nguy khác của nhà "
               "máy nhiệt độ thấp là các tạp chất trong dòng, dễ kết tủa thành "
               "rắn: rắn lắng đọng có thể gây tắc, và trong một số trường hợp, "
               "gây nổ. Vấn đề vật liệu kết cấu của nhà máy nhiệt độ thấp là "
               "<b>sự giòn hóa ở nhiệt độ thấp (embrittlement)</b>. Yêu cầu vật liệu tuy đã "
               "được hiểu rõ, nhưng sự cố phát sinh từ lắp sai vật liệu hoặc "
               "dòng nhiệt độ thấp chảy vào khu vực xây bằng thép thường — cả "
               "hai đều là vấn đề an toàn nội tại."))

    # ---- 7.7 -----------------------------------------------------------------
    b.append(h2("7.7 Áp suất", "7.7 Pressure"))
    b.append(p("Dùng áp suất cao làm tăng mạnh lượng năng lượng sẵn có trong nhà "
               "máy: nhà máy áp suất khí quyển tích trữ chủ yếu năng lượng hóa "
               "học, còn nhà máy áp suất cao còn có thêm năng lượng của khí nén "
               "thường trực và của chất lỏng chỉ giữ trạng thái lỏng nhờ áp "
               "suất. Tuy áp suất cao tự nó không gây vấn đề nghiêm trọng cho "
               "vật liệu kết cấu, sự kết hợp với nhiệt độ cao, nhiệt độ thấp "
               "hoặc vật liệu ăn mòn thì có. Vấn đề là đạt được độ bền vật liệu "
               "yêu cầu cho vận hành áp suất cao bất chấp các yếu tố đó."))
    b.append(p("Với vận hành áp suất cao, vấn đề rò rỉ trở nên nghiêm trọng hơn "
               "nhiều: lượng chất lỏng rò qua một lỗ cho trước lớn hơn nhờ chênh "
               "áp, và chất lỏng có thể bùng hơi khi áp suất giảm. <b>Áp suất "
               "thấp (dưới khí quyển)</b> nói chung không nguy hiểm bằng các "
               "điều kiện cực đoan khác; nhưng nhà máy áp suất thấp xử lý chất "
               "cháy có mối nguy không khí lọt vào tạo hỗn hợp cháy, và có thể "
               "xảy ra nổ hơi (steam explosion) nếu chất dễ bay hơi (ví dụ nước) "
               "được nạp vào hệ áp suất thấp gây bay hơi tức thời."))
    b.append(p("Người ta cho rằng thiết kế <b>chứ kín toàn phần</b> an toàn hơn "
               "(Englund, 1990): thiết bị được thiết kế chịu được áp suất cực "
               "đại có thể phát sinh từ phản ứng chạy trốn hay sự cố nguy hiểm "
               "khác. Điều này đòi hỏi tri thức chi tiết về quá trình và áp suất "
               "quá áp có thể xảy ra — tốt nhất lấy từ dữ liệu thực nghiệm kết "
               "hợp phân tích lý thuyết. Đáng tiếc là thông tin này thường "
               "không có sẵn khi so sánh các phương án quá trình. Trong thực tế, "
               "xây dựng chịu được áp suất khẩn cấp — vốn có thể cao hơn nhiều "
               "áp suất vận hành bình thường — thường không khả thi, vì vậy hệ "
               "thống xả áp gần như luôn luôn cần thiết cùng các thiết bị bảo vệ "
               "bổ sung như lửa đuốc hay tháp hấp thụ khí."))

    # ---- 7.8 -----------------------------------------------------------------
    b.append(h2("7.8 An toàn thiết bị", "7.8 Equipment Safety"))
    b.append(p("An toàn thiết bị cố gắng đo khả năng một thiết bị cụ thể là "
               "không an toàn (Heikkilä và Hurme, 1998a). Ở đây thiết bị gồm mọi "
               "thiết bị chính như bơm, bồn chứa v.v., nhưng không gồm đường "
               "ống, van hay thiết bị đo như những thực thể riêng lẻ. An toàn "
               "thiết bị xét độ an toàn của thiết bị tự nó, không xét tương tác "
               "qua quá trình với thiết bị khác — khía cạnh sau thuộc cấu trúc "
               "quá trình an toàn (mục 7.9). Tuy nhiên tương tác qua bố trí, "
               "chẳng hạn lò nung có thể là mồi lửa cho rò rỉ từ thiết bị khác, "
               "được xét trong an toàn thiết bị."))
    b.append(p("So sánh độ an toàn của thiết bị không đơn giản; nó phụ thuộc "
               "nhiều đặc tính của cả quá trình lẫn thiết bị. Có thể đánh giá "
               "từ dữ liệu tai nạn và hỏng hóc định lượng, và từ thực hành cùng "
               "khuyến nghị kỹ thuật. Kinh nghiệm đã dùng cho khuyến nghị bố "
               "trí và cho phát triển các phương pháp phân tích an toàn như "
               "Chỉ số Dow E&amp;F (Dow, 1987). Thống kê chứa chi tiết, nguyên "
               "nhân và tỷ lệ hỏng hóc của thiết bị, cùng dữ liệu về thiết bị "
               "dính líu đến các tổn thất lớn."))
    b.append(p("Dữ liệu về thiết bị trong các tổn thất lớn được thu thập ví dụ "
               "bởi Mahoney (1997) và Instone (1989). Mahoney phân tích <b>170 "
               "tổn thất lớn nhất</b> trong các nhà máy lọc dầu, petro hóa và "
               "xử lý khí từ 1966 đến 1996 — hầu như mọi tổn thất đều liên quan "
               "cháy hoặc nổ. Instone phân tích khoảng <b>2.000 hồ sơ tổn thất "
               "lớn</b> của công nghiệp hydrocarbon tại Cigna Insurance. Khác "
               "biệt giữa hai bộ dữ liệu: Mahoney phân tích thiết bị nào là "
               "<b>nguyên nhân chính</b> của tổn thất, còn Instone liệt kê "
               "thiết bị <b>dính líu</b> đến tổn thất."))
    b.append(p("Trong thiết kế nhà máy, an toàn thiết bị cũng được ghi nhận qua "
               "bố trí: mục tiêu của bố trí là giảm thiểu rủi ro cho nhân lực, "
               "giảm thiểu leo thang (trong nhà máy và sang nhà máy lân cận), "
               "bảo đảm tiếp cận khẩn cấp đầy đủ, và bảo đảm tiếp cận bảo dưỡng "
               "vận hành. Bố trí là yếu tố quyết định an toàn vì phân tách các "
               "rủi ro khác nhau, kiểm soát tai nạn và giới hạn phơi nhiễm. Bố "
               "trí an toàn được thiết kế trên tiêu chuẩn thiết kế và quy định "
               "địa phương; khoảng cách hợp lý giữa các thao tác công nghệ cũng "
               "được coi là giải pháp an toàn nội tại hơn (Bollinger et al., "
               "1996)."))
    b.append(p("Khuyến nghị khoảng cách bố trí đã được công bố dưới dạng ma trận "
               "và danh sách khoảng cách tối thiểu điển hình giữa các hạng mục "
               "(Industrial Risk Insurers, 1991; Bausbacher và Hunt, 1993; "
               "Prugh, 1982). Khoảng cách phù hợp tới hạng mục khác phụ thuộc "
               "chủ yếu vào tính chất an toàn của hạng mục; khoảng cách bảo "
               "dưỡng và tiếp cận thường ngắn hơn khoảng cách an toàn. Vì vậy "
               "có thể giả định <b>trung bình các khoảng cách khuyến nghị phản "
               "ánh mức độ không an toàn chung của hạng mục quá trình cụ "
               "thể</b>."))
    b.append(p("Chỉ số cháy và nổ Dow (1987) trừ điểm cho thiết bị đốt và một "
               "số thiết bị quay xác định — một phần của thành phần mối nguy "
               "quá trình đặc biệt. Còn dữ liệu thống kê về hỏng hóc của các "
               "bộ phận hệ thống quá trình: Arulanantham và Lees (1981) nghiên "
               "cứu hỏng hóc bồn áp suất và lò nung trong các nhà máy như nhà "
               "máy olefin, định nghĩa hỏng hóc là tình trạng nứt, rò hoặc lỗi "
               "khác phát triển đến mức phải sửa chữa hoặc thay thế — gồm một "
               "phần hỏng hóc tiềm tàng nguy hiểm và toàn bộ hỏng hóc thảm khốc. "
               "Tỷ lệ hỏng hóc liên hệ ở mức độ nào đó với độ an toàn của hạng "
               "mục: thiết bị có lịch sử hỏng hóc dài có thể gây vấn đề an toàn "
               "trong tương lai, nên cân nhắc thiết bị khác. Cần nhớ rằng không "
               "phải mọi thông tin độ tin cậy đều biểu diễn an toàn trực tiếp, "
               "vì không phải hỏng hóc nào cũng nguy hiểm và không phải tai nạn "
               "nào cũng do hỏng thiết bị."))

    # ---- 7.9 -----------------------------------------------------------------
    b.append(h2("7.9 Cấu trúc quá trình an toàn", "7.9 Safe Process Structure"))
    b.append(p("Cấu trúc quá trình an toàn mô tả an toàn nội tại của các cấu "
               "hình quá trình: những thao tác nào có mặt trong quá trình và "
               "chúng được nối với nhau ra sao. Vì vậy nó mô tả độ an toàn của "
               "quá trình dưới góc nhìn kỹ thuật hệ thống: các thao tác công "
               "nghệ hay hạng mục làm việc cùng nhau tốt thế nào, nên được nối "
               "và điều khiển cùng nhau ra sao, và các hệ trợ giúp như làm "
               "mát, gia nhiệt hay hệ xả áp nên được cấu hình và nối với quá "
               "trình chính thế nào (Heikkilä et al., 1998). Tầm quan trọng của "
               "chỉ số này đang tăng lên khi các quá trình ngày càng tích hợp "
               "qua mạng truyền nhiệt và truyền chất."))
    b.append(p("Phần lớn các yếu tố ảnh hưởng an toàn nội tại khá đơn giản để "
               "ước lượng, vì dựa trên tính chất vật lý và hóa học của các hợp "
               "chất hiện diện. <b>Cấu trúc quá trình an toàn nội tại không thể "
               "định nghĩa bằng quy tắc tường minh</b>, mà phải dựa vào tiêu "
               "chuẩn, khuyến nghị và báo cáo tai nạn — tri thức hình thành từ "
               "kinh nghiệm vận hành của các quá trình khác nhau (Lees, 1996). "
               "Báo cáo tai nạn đưa ra thông tin quý giá về điểm yếu của các "
               "giải pháp quá trình; các cơ sở dữ liệu rộng đã được thu thập từ "
               "báo cáo tai nạn (Anon, 1996) và từ đó xây dựng được cơ sở dữ "
               "liệu các thiết kế tốt và xấu."))
    b.append(p("Vì không thể mô tả bằng quy tắc tường minh, suy luận phải dựa "
               "trên <b>phép loại suy</b>: thiết kế hiện tại được so sánh xem có "
               "giống các trường hợp thiết kế an toàn hay không an toàn đã biết "
               "trong cơ sở dữ liệu. Cách suy luận này các kỹ sư thực hành còn "
               "dùng trong đầu để tạo thiết kế mới; khi được máy hóa nó gọi là "
               "<b>suy luận dựa trên tình huống</b> (case-based reasoning) "
               "(Gonzalez và Dankel, 1993)."))
    return "".join(b)


def bullet_vi():
    return ("<ul>"
            "<li>tính phản ứng với các nguyên tố và hợp chất mà nó được yêu cầu "
            "phản ứng trong quá trình</li>"
            "<li>tính phản ứng với oxy khí quyển</li>"
            "<li>tính phản ứng với nước</li>"
            "<li>tính phản ứng với chính nó — khuynh hướng trùng hợp, ngưng tụ, "
            "phân hủy và nổ</li>"
            "<li>tính phản ứng với các vật liệu khác mà nó có thể tiếp xúc ngoài "
            "ý muốn trong quá trình, lưu trữ hoặc vận chuyển</li>"
            "<li>tính phản ứng với vật liệu kết cấu — tức tính ăn mòn của nó "
            "(xem mục 7.3)</li>"
            "</ul>")


# ---------------------------------------------------------------------------
def body_en():
    b = []

    b.append(p("As mentioned earlier, <b>the lack of information complicates the "
               "safety considerations in preliminary process plant design</b>. "
               "It is therefore important to utilize all the available details "
               "that may affect the inherent safety of the plant. To make this "
               "possible, the inherent safety characteristics should be "
               "evaluated systematically during process design. For this "
               "purpose, a dedicated methodology for estimating inherent safety "
               "using the scarce information available is required."))
    b.append(p("Most of the principles of inherent safety are useful already in "
               "the preliminary design phase, even though most process details "
               "are still missing. This is represented in Table 4, which shows "
               "at which project stage each feature of friendly design should "
               "be considered. In fact, the opportunities for installing "
               "inherent safety features decrease as the design progresses "
               "(Kletz, 1991). Table 4 shows that most features can be "
               "considered at the conceptual and flowsheet stages."))
    hdr4 = ("Feature of friendly design (Kletz, 1991)",
            "Conceptual<br>stage", "Flowsheet<br>stage", "P&amp;ID<br>stage")
    b.append(table(hdr4, _T4_EN,
                   caption="Table 4 · Project stages at which each feature of friendly design "
                           "should be discussed (Kletz, 1991). For the single-✕ rows the column "
                           "position follows the source print / the original Kletz table — "
                           "equipment-detail decisions (incorrect assembly, status, tolerance, "
                           "software) belong to the P&amp;ID stage."))
    b.append(p("In this thesis an <b>index-based method was selected</b>, since "
               "inherent safety is formed of many interrelated subfactors. It is "
               "therefore more straightforward to represent these factors as "
               "subindices weighted by score means, as discussed later in "
               "Chapter 9."))
    b.append(fig(1, F.fig_c07_index()))
    b.append(p("The formation of the inherent safety indices is based on the "
               "following principle (Figure 5): the basic principles of "
               "inherent safety (Section 6.1) are first described as parameters "
               "(Table 5), and the most important of these parameters are "
               "selected to be implemented as inherent safety subindices."))
    b.append(p("Edwards and Lawrence (1993) presented a list of <b>sixteen "
               "chemical and physical properties and process parameters</b> "
               "available at the process-route selection stage (Table 5). Seven "
               "of these sixteen parameters were included in their index method "
               "(PIIS). Their selected parameters concentrate very much on the "
               "chemical process route and the chemistry. They also tested "
               "their selection by expert judgement, which gave support to "
               "their work (Edwards et al., 1996)."))
    b.append(p("Intrinsic safety, however, is affected by <b>both the process "
               "equipment and the properties of the chemical substances</b> "
               "present. Therefore the index should reflect this fact. "
               "Parameters representing the process aspects of inherent safety "
               "were added to the list (Table 5): the type of equipment involved "
               "and the safety of the process structure, which describe the "
               "process configuration from a system point of view. A third "
               "parameter describing the interaction (reactivity) of the "
               "chemicals present was included as well, since this is an "
               "obvious source of risk."))
    hdr5 = ("Inherent safety parameter",
            "E&amp;L<br>(1993)", "Heikkilä et al.<br>(1996)", "Comments")
    b.append(table(hdr5, _T5_EN,
                   caption="Table 5 · Inherent safety parameters. *) Not included in the "
                           "reference Edwards and Lawrence (1993)."))
    b.append(p("<b>Inventory</b>, for example, was chosen by both groups: it is "
               "relative to the capacity of a process and to residence times "
               "(hold-ups) in vessels; it has a large effect on the degree of "
               "hazard and should be kept small by intensification. <b>Phase</b> "
               "is a release property which can be expressed by inventory and "
               "was therefore excluded. <b>Reaction yield</b> also expresses "
               "inventory, since higher yields decrease recycling and thus "
               "decrease reactor size."))
    b.append(p("Both groups chose <b>temperature and pressure</b>: temperature "
               "is a direct measure of the heat energy available at release; "
               "pressure is both a measure of the energy available at release "
               "and the energy available to cause a release. The <b>heat of "
               "reaction</b> (Heikkilä et al., 1996) measures the energy "
               "available from the reaction — a high heat of reaction may "
               "generate higher temperatures and dangerous runaway reactions. "
               "Another parameter to consider is reaction rate, but it does not "
               "directly express the hazardousness of a reaction (e.g. when the "
               "heat of reaction is low) and was therefore excluded."))
    b.append(p("<b>Chemical interaction</b> together with the heat of the side "
               "reaction expresses the potential reactiveness present in the "
               "process. Unwanted side reactions may be, for example, rapid "
               "polymerization, heat formation, and formation of flammable or "
               "toxic gas. Side reactions and possible reaction risks in "
               "storage systems are taken into account by the heat of reaction "
               "and chemical interaction. Both groups chose <b>flammability, "
               "explosiveness and toxicity</b> as the hazardous properties of "
               "substances; Heikkilä et al. (1996) also included "
               "<b>corrosiveness</b>, because in corrosive environments the "
               "right choice of construction materials is essential to inherent "
               "safety."))
    b.append(p("<b>Viscosity</b> has not been found meaningful: the hot-spot "
               "effect in poorly mixed viscous reactors can be included in the "
               "heat-of-reaction parameter. <b>New phase generation and "
               "catalysts</b> were not chosen either, because both parameters "
               "are considered through the hazardous properties of the "
               "substances (chemical interaction, explosiveness etc.); the same "
               "applies to the waste-products parameter."))
    b.append(p("The chosen meaningful parameters are: <b>heat of reaction, "
               "flammability, explosiveness, toxicity, corrosiveness, chemical "
               "interaction, inventory, process temperature and pressure, "
               "equipment safety and safe process structure</b> (Table 5). This "
               "does not mean that other factors affecting inherent safety are "
               "meaningless — on the contrary, they should be considered in more "
               "detail in further design stages."))
    hdr6 = ("Principle of inherent safety (Kletz, 1991)",
            "PIIS<br>(Edwards &amp; Lawrence, 1993)",
            "ISI<br>(Heikkilä et al., 1996)")
    b.append(table(hdr6, _t6_rows_en(),
                   caption="Table 6 · The characteristics of inherent safety in conceptual "
                           "process design."))
    b.append(p("From Table 6 it can be seen how the selected parameters connect "
               "to the basic principles of inherent safety. For instance, the "
               "equipment-safety and safe-process-structure subindices contain "
               "several inherent safety characteristics at once, such as "
               "limitation of effects or tolerance to maloperation. It is "
               "practical to include several characteristics in few parameters, "
               "since the inherent safety principles are both very broad and "
               "overlapping; the philosophy behind them cannot be described by "
               "just one process parameter. The selected parameters are "
               "discussed in more detail in the following sections."))

    # ---- 7.1 -----------------------------------------------------------------
    b.append(h2("7.1 Heat of Reaction", "7.1 Nhiệt phản ứng"))
    b.append(p("A reaction is exothermic if heat is generated. Reactions in "
               "which large quantities of heat or gas are released are "
               "potentially hazardous, particularly during fast decomposition "
               "or complete oxidation."))
    b.append(p("The main clue to the possible violence of any reaction lies in "
               "the <b>heat liberated, the temperature that may be reached, and "
               "the volume and nature of any gases and vapours formed</b>. "
               "Chemical characteristics that increase the potential of an "
               "explosion are high decomposition or reaction enthalpies and "
               "high rates of energy generation. Broadly speaking, any reaction "
               "that can lead to a temperature rise of 300°C or to the "
               "production of a significant amount of gas or vapour may pose a "
               "significant hazard (King, 1990; IChemE, 1987)."))
    b.append(p("Substances with a positive enthalpy of formation release energy "
               "during decomposition. Energetic substances can in general be "
               "identified by hazardous molecular structures such as peroxide, "
               "nitro and azo groups and double and triple bonds. The presence "
               "of these groups does not necessarily imply that the substance "
               "is hazardous (IChemE, 1987); on the other hand, the initial "
               "absence of unstable groups is no guarantee of long-term "
               "stability. King (1990) has pointed out that the rates of "
               "chemical reactions often bear little or no relation to the heat "
               "they generate: some very fast reactions (e.g. ionic reactions "
               "in aqueous solution) produce little or no heat, while others "
               "that develop a great deal of heat proceed very slowly in the "
               "absence of a catalyst. Thus, instead of reaction rate or the "
               "presence of unstable structures, <b>the reaction heat has been "
               "chosen as the criterion</b>."))
    b.append(p("The energy change (ΔU<sub>r</sub>) during the reaction equals "
               "the difference between the energies of formation of the "
               "products and the reactants:"))
    b.append(eq("ΔU<sub>r</sub> = Σ(U<sub>f</sub>)<sub>products</sub> − "
                "Σ(U<sub>f</sub>)<sub>reactants</sub>", "(1)"))
    b.append(p("If the reaction occurs under isobaric conditions (constant "
               "pressure), energy can be replaced by enthalpy (ΔH<sub>r</sub>) "
               "and the equation can be written for constant-volume conditions "
               "as follows:"))
    b.append(eq("ΔH<sub>r</sub> = Σ(H<sub>f</sub>)<sub>products</sub> − "
                "Σ(H<sub>f</sub>)<sub>reactants</sub>", "(2)"))

    # ---- 7.2 -----------------------------------------------------------------
    b.append(h2("7.2 Hazardous Substances", "7.2 Chất nguy hiểm"))
    b.append(p("Hazardous substances present in the process are identified on "
               "the basis of flammability, explosiveness and toxicity. The "
               "flammability of gases and of vapours of flammable liquids is a "
               "great concern in the process industries: the result of an "
               "ignition can be a fire, an explosion, or both. Accidental fires "
               "and explosions of flammable mixtures with air often follow the "
               "escape of combustible materials or the inlet of air into "
               "process equipment."))
    b.append(h3("7.2.1 Flammability", "7.2.1 Khả cháy"))
    b.append(p("Flammability means the ease with which a material burns in air "
               "(King, 1990); it applies to gases, liquids and solids. It is "
               "very important to know, for instance, in cases of leaks. A "
               "liquid whose flash point is below the processing or storage "
               "temperature can give rise to a flammable mixture and is "
               "generally considered hazardous."))
    b.append(p("The flammability of liquids depends on the lower flammability "
               "limit of the material and its vapour pressure at the prevailing "
               "temperature. The <b>flash point</b> is the lowest temperature "
               "at which a liquid gives off enough flammable vapour at or near "
               "its surface to ignite in an intimate mixture with air given a "
               "spark or a flame (i.e. the vapour pressure is high enough for "
               "the gas concentration to correspond to the lower flammability "
               "limit). The flash point is therefore the main parameter in the "
               "hazard classification of liquids, and government regulations "
               "are based on it (Lees, 1996). The <b>boiling point</b> may be "
               "taken as an indication of volatility; for a flammable liquid it "
               "can be a direct measure of the hazard involved in its use "
               "(Sax, 1979)."))
    b.append(p("The Finnish legislation (Pyötsiä, 1994) classifies the "
               "flammability of chemical substances on the basis of their flash "
               "and boiling points — similar to the European Union directives "
               "on hazardous substances. Similar approaches are used by the Dow "
               "Fire and Explosion Index (1987) and by Edwards and Lawrence "
               "(1993)."))
    b.append(h3("7.2.2 Explosiveness", "7.2.2 Tính nổ"))
    b.append(p("Explosiveness here means the tendency of chemicals to form an "
               "explosive mixture in air. When an explosion occurs in the "
               "atmosphere, energy is released in a short time and in a small "
               "volume, generating an audible pressure wave. An explosion is a "
               "sudden and violent release of energy, deriving either from "
               "physical or from chemical energy."))
    b.append(p("Dangers from physical energy (pressure) are considered by the "
               "pressure subindex, so only chemical energy is discussed here. "
               "The explosive chemicals may be either high explosives or "
               "flammable gases: high explosives contain their own oxygen and "
               "need no external oxygen to explode — they are considered by the "
               "heat-of-reaction parameter; flammable (usually organic) gases "
               "explode in excess air to yield a large volume of "
               "CO<sub>2</sub> and H<sub>2</sub>O and are discussed by the "
               "explosiveness parameter."))
    b.append(p("The explosive nature of chemical substances is described with "
               "the <b>upper and lower explosion limits</b>. The explosiveness "
               "of a vapour cloud depends especially on the lower explosion "
               "limit (LEL) — the concentration of vapour at which the cloud "
               "can be ignited. The wider the range between the explosion "
               "limits, the more probable it is that the cloud lies in the "
               "flammable region, i.e. the higher the tendency for explosion; "
               "Edwards and Lawrence (1993) used explosion limits to determine "
               "the explosiveness of substances. Using industrial chemicals "
               "with less explosive potential makes the process more "
               "intrinsically safe. The most dangerous explosions come from "
               "large clouds of flammable material finding an ignition source — "
               "Flixborough (Lees, 1996) is an example of the destruction "
               "caused by such an incident."))
    b.append(h3("7.2.3 Toxic Exposure", "7.2.3 Phơi nhiễm độc tính"))
    b.append(p("Marshall (1987) and Wells (1980) have described toxicity as a "
               "property of a substance which destroys life or injures health "
               "when introduced into or absorbed by a living organism. The "
               "toxic hazard is a measure of the likelihood of such damage "
               "occurring, determined by the frequency and duration of exposure "
               "and the concentration of the chemical."))
    b.append(p("The estimation of toxicity is based on animal experimentation. "
               "Toxicity depends on the physical and biological characteristics "
               "of the substance, the way of entry (swallowing, through the "
               "skin, breathing) and the size of the dose. Persistent exposure "
               "of workers to relatively low levels of many industrial "
               "chemicals can produce chronic disease leading to serious "
               "disability or premature death (King, 1990). The extreme health "
               "hazards of process materials are carcinogenicity, teratology "
               "and mutagenity; special precautions are needed when handling "
               "substances possessing these properties (Fawsett, 1982)."))
    b.append(p("According to Wells (1980), probably the most commonly used "
               "toxicity term is the <b>Threshold Limit Value (TLV)</b>: the "
               "concentration in air which can be breathed without harmful "
               "effect for five consecutive 8-hour working days. TLVs are based "
               "on effects ranging from irritation to physiological damage; in "
               "the industrial context they are the most usable toxicity "
               "values, since their aim is to protect employees at work. The "
               "threshold of odour is important when the TLV is lower than the "
               "concentration needed for an odour to appear (Siegell, 1996) — "
               "a crucial factor in emergency planning. Because legislation is "
               "usually made to protect people in general, e.g. the Finnish "
               "legislation (Pyötsiä, 1994) uses LD<sub>50</sub> and "
               "LC<sub>50</sub> for toxicity, while irritation and other "
               "effects are dealt with separately. <b>LD<sub>50</sub></b> is "
               "the dose administered orally or by skin absorption causing the "
               "death of 50% of the test group within a 14-day observation "
               "period; <b>LC<sub>50</sub></b> is the concentration in air to "
               "which exposure for 24 hours or less would cause the death of "
               "50% of a test group."))

    # ---- 7.3 -----------------------------------------------------------------
    b.append(h2("7.3 Corrosiveness", "7.3 Ăn mòn"))
    b.append(p("All metals corrode under certain conditions. Internal corrosion "
               "is caused by galvanic corrosion, pitting, corrosion fatigue, "
               "stress corrosion cracking, stray currents, etc. Corrosion "
               "reduces the reliability and integrity of the plant: it reduces "
               "the strength of materials and causes leaks; corrosion products "
               "affect process materials, moving parts and process efficiency "
               "and cause fouling. Corrosion proceeds slowly and is usually "
               "more the concern of engineers than of safety professionals — "
               "yet it has caused catastrophic failures with heavy loss of life "
               "(King, 1990)."))
    b.append(p("The safety problems caused by the corrosive properties of the "
               "process streams can be prevented by a proper choice of "
               "<b>construction materials</b>. The mechanical design is based "
               "on process design values (temperature and pressure) beyond "
               "which operation is not allowed since it can cause hazardous "
               "effects. The mechanical strength of equipment is reduced "
               "during the life of the process by corrosion; corrosion is "
               "usually measured as corrosion rates (mm/a). In equipment "
               "design, corrosion is taken into account by the selection of "
               "material and the corresponding <b>corrosion allowance</b> — "
               "the material is selected so that the allowance is not exceeded "
               "during the lifetime of the equipment. Corrosion rates are not "
               "always known during predesign, but a rough type of "
               "construction material is often anticipated. Since the need for "
               "a better material most often indicates more corrosive "
               "conditions, a classification based on the type of construction "
               "material can be justified."))
    b.append(p("The Dow Fire and Explosion Index (1987) also considers "
               "corrosion risks, but the penalties are given through "
               "unacceptable corrosion rates. Design standards also include "
               "advice on acceptable corrosion rates (Uhlig and Reviev, 1985)."))

    # ---- 7.4 -----------------------------------------------------------------
    b.append(h2("7.4 Chemical Interaction", "7.4 Tương tác hóa học"))
    b.append(p("The various chemical substances present in a process plant may, "
               "under favourable conditions, react with each other or with air "
               "or water, causing safety or technical problems. This chemical "
               "interaction is based on the chemical reactivity of each "
               "substance with the other substances present in the plant. As a "
               "potential process hazard, the chemical reactivity of any "
               "substance should be considered in the following contexts:"))
    b.append(bullet_en())
    b.append(p("In a process, chemical interaction is either intended or "
               "unintended. The wanted reactions are under control, e.g. in "
               "the reactor. Unwanted chemical interaction can lead to "
               "unpleasant surprises: heat formation, fire, formation of "
               "harmless non-flammable gas, formation of toxic gas, formation "
               "of flammable gas, explosion, rapid polymerization, or soluble "
               "toxic chemicals."))
    b.append(p("The United States Environmental Protection Agency (Hatayama et "
               "al., 1980) has provided a <b>matrix for determining the "
               "compatibility of hazardous wastes</b>: the interactivity of "
               "substances is presented with the consequences of the reaction, "
               "such as heat formation, fire, rapid polymerization and "
               "formation of flammable gases. Similar matrices also exist, "
               "e.g. Chempat (Leggett, 1997)."))

    # ---- 7.5 -----------------------------------------------------------------
    b.append(h2("7.5 Inventory", "7.5 Tồn kho"))
    b.append(note("\"Any material when … present in large quantity may be "
                  "classified as hazardous.\" — Wells (1980)"))
    b.append(p("The total quantity of material to be stored is set initially by "
               "process engineering, commercial and political considerations, "
               "although subsequent hazard considerations may reduce the "
               "quantity or lead to improved layout or deconcentration of "
               "storage facilities. In general, <b>large inventories in one "
               "place are unfavourable in the cases of fire or rupture of a "
               "vessel</b>. Potential severity can be reduced by keeping "
               "inventories low, by minimizing the reactor size and by avoiding "
               "storage of potentially hazardous materials in the synthesis "
               "train (CCPS, 1995a). For instance, large quantities of very "
               "toxic gases and volatile liquids were one of the major mistakes "
               "in the Bhopal accident (King, 1990). After Bhopal and several "
               "other accidents the authorities have tightened the limits for "
               "the inventories of flammable gases and liquids."))
    b.append(p("The amount of a substance present in the plant has a large "
               "effect on the degree of hazard. It is advised to use a minimum "
               "storage inventory of hazardous materials and to construct "
               "process and storage areas away from residential — or "
               "potentially residential — areas."))

    # ---- 7.6 -----------------------------------------------------------------
    b.append(h2("7.6 Temperature", "7.6 Nhiệt độ"))
    b.append(p("Operation in extreme conditions has its own problems and "
               "hazards; extreme conditions usually mean very low or high "
               "temperatures or pressures. <b>Temperature is a direct measure "
               "of the heat energy available at release</b> (Edwards and "
               "Lawrence, 1993). Temperature is the most important factor "
               "influencing reaction rate, as shown by the Arrhenius equation: "
               "in practice, an increase of 10°C increases a specific reaction "
               "rate by two to four times, depending on the energy of "
               "activation (CCPS, 1995a)."))
    b.append(p("High temperatures combined with high pressures greatly increase "
               "the amount of energy stored in the plant. High-temperature "
               "plants have severe problems with materials of construction: "
               "high temperature implies thermal stresses, particularly during "
               "start-up and shut-down. Low-temperature plants are subject to "
               "thermal stresses for the same reason; these stresses need to "
               "be allowed for and, as far as possible, avoided."))
    b.append(p("Low-temperature plants contain large amounts of fluids kept in "
               "the liquid state only by pressure and temperature; if for any "
               "reason the plant cannot be kept cold, the liquids begin to "
               "vapourize. Another hazard in low-temperature plants is possible "
               "impurities in the fluids, liable to come out of solution as "
               "solids: deposited solids may cause not only blockage but, in "
               "some cases, an explosion. A materials problem in "
               "low-temperature plants is <b>low-temperature embrittlement</b>. "
               "The material requirements are well understood; the problems "
               "arise from the installation of incorrect materials or from the "
               "flow of low-temperature fluids to sections constructed in mild "
               "steel — both refer to inherent safety problems."))

    # ---- 7.7 -----------------------------------------------------------------
    b.append(h2("7.7 Pressure", "7.7 Áp suất"))
    b.append(p("High pressure greatly increases the amount of energy available "
               "in the plant: in an atmospheric plant the stored energy is "
               "mainly chemical, while in a high-pressure plant there is in "
               "addition the energy of compressed permanent gases and of fluids "
               "kept liquid only by pressure. Although high pressures in "
               "themselves do not pose serious materials problems, the "
               "combination with high temperatures, low temperatures or "
               "aggressive materials does. The problem is to obtain the "
               "material strength required by high-pressure operation despite "
               "these factors."))
    b.append(p("With high-pressure operation the problem of leaks becomes much "
               "more serious: the amount of fluid which can leak through a "
               "given hole is greater on account of the pressure difference, "
               "and the fluid may be a liquid which flashes off as the "
               "pressure is reduced. <b>Low (subatmospheric) pressures</b> are "
               "not in general as hazardous as the other extreme conditions; "
               "but in low-pressure plants handling flammables, the ingress of "
               "air with consequent formation of a flammable mixture is a real "
               "hazard, and steam explosions may take place if a volatile "
               "material (e.g. water) is fed to a low-pressure system, causing "
               "consequent vapourization."))
    b.append(p("It is claimed that it is safer to design for <b>total "
               "containment</b> (Englund, 1990): the processing equipment is "
               "designed to withstand the maximum pressure expected from a "
               "runaway or another hazardous incident. This requires detailed "
               "knowledge of the process and of the possible overpressure — "
               "best obtained from experimental data combined with theoretical "
               "analysis. Unfortunately, in many cases this information is not "
               "at hand when comparing process alternatives. In real life it "
               "is not often practical to construct for an emergency pressure "
               "which can be very much higher than the normal operating "
               "pressure; therefore a relief system is nearly always required, "
               "together with added-on protective equipment such as a flare or "
               "a gas scrubber."))

    # ---- 7.8 -----------------------------------------------------------------
    b.append(h2("7.8 Equipment Safety", "7.8 An toàn thiết bị"))
    b.append(p("Equipment safety tries to measure the possibility that a piece "
               "of equipment is unsafe (Heikkilä and Hurme, 1998a). Here "
               "equipment includes all major pieces such as pumps and vessels, "
               "but not piping, valves or instruments as separate entities. "
               "Equipment safety considers the safety of the equipment as such, "
               "without interactions through the process with other equipment — "
               "that latter aspect is described by the safe process structure "
               "(Section 7.9). However, interactions through layout, such as a "
               "furnace being a source of ignition for a leak from another "
               "piece of equipment, are considered by equipment safety."))
    b.append(p("The comparison of the safety of equipment is not "
               "straightforward: it depends on several features of both the "
               "process and the equipment themselves. It can be evaluated from "
               "quantitative accident and failure data and from engineering "
               "practice and recommendations. Experience has been used for "
               "layout recommendations and for the development of safety "
               "analysis methods such as the Dow E&amp;F Index (Dow, 1987). "
               "Statistics contain details, causes and rates of failures of "
               "equipment, and data on equipment involved in large losses."))
    b.append(p("Data on equipment involved in large losses has been collected, "
               "for instance, by Mahoney (1997) and Instone (1989). Mahoney "
               "analysed the <b>170 largest losses</b> in refineries, "
               "petrochemical and gas processing plants from 1966 to 1996 — "
               "nearly all involved fires or explosions. Instone analysed some "
               "<b>2,000 large loss claims</b> of the hydrocarbon industry at "
               "Cigna Insurance. The difference is that Mahoney analysed which "
               "equipment items were the <b>primary causes</b> of losses, "
               "whereas Instone listed the equipment <b>involved</b> in the "
               "losses."))
    b.append(p("During plant design the safety of process equipment is also "
               "recognized by layout: the objectives are to minimize risk to "
               "personnel, to minimize escalation (within the plant and to "
               "adjacent plants) and to ensure adequate emergency access, as "
               "well as adequate access for maintenance and operations. Plant "
               "layout is a crucial safety factor because of segregation of "
               "risks, containment of accidents and limitation of exposure. "
               "Safe layout is designed on the basis of design standards and "
               "local regulations; appropriate spacing of unit operations "
               "within a process is also considered an inherently safer "
               "solution (Bollinger et al., 1996)."))
    b.append(p("Spacing recommendations have been presented in the literature "
               "as matrices and lists of typical minimum distances between "
               "process items (Industrial Risk Insurers, 1991; Bausbacher and "
               "Hunt, 1993; Prugh, 1982). The distance to another item depends "
               "mostly on the safety properties of the items; maintenance and "
               "access clearances are usually shorter than safety clearances. "
               "Therefore it can be assumed that <b>the average of the "
               "recommended spacings mostly reflects the general unsafety of a "
               "specific process item</b>."))
    b.append(p("The frequently used Dow Fire &amp; Explosion Hazard Index "
               "(1987) gives penalties for fired equipment and certain "
               "specified rotating equipment — part of the Special Process "
               "Hazards term. There is also a certain amount of statistical "
               "information on the failures of process system components: "
               "Arulanantham and Lees (1981) studied pressure vessel and fired "
               "heater failures in plants such as olefins plants, defining "
               "failure as a condition in which a crack, leak or other defect "
               "has developed to the extent that repair or replacement is "
               "required — including some potentially dangerous as well as all "
               "catastrophic failures. Failure rates are related to some extent "
               "to the safety of process items: equipment with a long history "
               "of failures may cause safety problems in the future, so another "
               "piece of equipment should be considered. It should be "
               "remembered that not all reliability information expresses "
               "safety directly, since not all failures are dangerous and not "
               "all accidents are due to equipment failures."))

    # ---- 7.9 -----------------------------------------------------------------
    b.append(h2("7.9 Safe Process Structure", "7.9 Cấu trúc quá trình an toàn"))
    b.append(p("Safe process structure describes the inherent safety of the "
               "process configurations: which operations are involved in the "
               "process and how they are connected together. It describes the "
               "safety of the process from a system-engineering point of view: "
               "how well certain unit operations or other items work together, "
               "how they should be connected and controlled, and how auxiliary "
               "systems such as cooling, heating or relief systems should be "
               "configured and connected to the main process (Heikkilä et al., "
               "1998). The importance of this subindex is increasing as "
               "processes become more integrated through heat and mass-transfer "
               "networks."))
    b.append(p("Most factors affecting inherent safety are quite "
               "straightforward to estimate, being based on the physical and "
               "chemical properties of the compounds present. <b>An inherently "
               "safe process structure cannot be defined by explicit rules</b>; "
               "one has to rely on standards, recommendations and accident "
               "reports — information based on the experience gained in the "
               "operation practice of different processes (Lees, 1996). "
               "Accident reports give valuable information about possible "
               "weaknesses in different process solutions, and extensive "
               "databases have been collected from them (Anon, 1996); from "
               "this data a database of good and bad designs can be built."))
    b.append(p("Since an inherently safe process structure cannot be described "
               "by explicit rules, the reasoning has to be based on "
               "<b>analogies</b>: the current design is compared against known "
               "safe or unsafe design cases in the database. This is the same "
               "approach practising engineers use mentally to generate new "
               "process designs; when computerized it is called <b>case-based "
               "reasoning</b> (Gonzalez and Dankel, 1993)."))
    return "".join(b)


def bullet_en():
    return ("<ul>"
            "<li>reactivity with the elements and compounds with which it is "
            "required to react in the process</li>"
            "<li>reactivity with atmospheric oxygen</li>"
            "<li>reactivity with water</li>"
            "<li>reactivity with itself — its propensity to polymerise, "
            "condense, decompose and explode</li>"
            "<li>reactivity with other materials with which it may come into "
            "contact unintentionally in process, storage or transport</li>"
            "<li>reactivity with materials of construction — its corrosivity "
            "(see Section 7.3)</li>"
            "</ul>")


# English variants of Tables 4 and 5 (single-language cells).
_T4_EN = [
    ("Intensification", _X, _X, _D),
    ("Substitution", _X, _X, _D),
    ("Attenuation", _X, _X, _D),
    "Limitation of effects",
    ("&nbsp;&nbsp;• by equipment design", _X, _X, _D),
    ("&nbsp;&nbsp;• by changing reaction conditions", _X, _D, _D),
    ("Simplification", _X, _X, _D),
    "Avoiding knock-on effects",
    ("&nbsp;&nbsp;• by layout", _X, _X, _D),
    ("&nbsp;&nbsp;• in other ways", _X, _X, _D),
    ("Making incorrect assembly impossible", _D, _D, _X),
    ("Making status clear", _D, _D, _X),
    ("Tolerance", _D, _D, _X),
    ("Ease of control", _X, _X, _D),
    ("Software", _D, _D, _X),
]

_T5_EN = [
    ("Inventory", "x", "x", "relative to capacity"),
    ("Phase", _D, _D, "release property"),
    ("Temperature", "x", "x", _D),
    ("Pressure", "x", "x", _D),
    ("Heat of main reaction", _D, "x", "high/low heat generation"),
    ("New phase generation", _D, _D, "solid/gas formation"),
    ("Catalysts", _D, _D, _D),
    ("Side reactions", _D, "x", "heat generation"),
    ("Waste products", _D, _D, "considered by substances"),
    ("Reaction yield", _D, _D, "considered by inventory"),
    ("Reaction rate", _D, _D, "considered by ΔH<sub>R</sub>"),
    ("Viscosity", _D, _D, "hot spots"),
    ("Flammability", "x", "x", "ease of burning (liquid)"),
    ("Explosiveness", "x", "x", "explosive gas mixture"),
    ("Corrosiveness", _D, "x", "construction material"),
    ("Toxicity", "x", "x", "an adverse effect on the human body"),
    ("Chemical interaction *)", _D, "x", "reactivity"),
    ("Type of equipment *)", _D, "x", "choice of equipment"),
    ("Safety of process structure *)", _D, "x", "choice of configuration"),
]


def _t6_rows_en():
    rows = []
    g = [
        ("Intensification <i>(inventory, reaction volume)</i>",
         ("inventory", "inventory, reaction yield")),
        ("Substitution <i>(safer materials)</i>",
         ("flammability, explosiveness, toxicity",
          "flammability, explosiveness, toxicity, chemical interaction")),
        ("Attenuation <i>(lower temperature, pressure)</i>",
         ("temperature, pressure", "temperature, pressure")),
        ("Limitation of Effects <i>(safer technical alternatives, safer "
         "reaction conditions)</i>",
         ("temperature, pressure",
          "equipment safety, safe process structure, pressure, temperature, "
          "chemical interaction")),
        ("Simplification <i>(simplify process facilities)</i>",
         (_D, "safe process structure")),
        ("Making Incorrect Assembly Impossible "
         "<i>(choice of equipment, piping and fittings correctly)</i>",
         (_D, "equipment safety, safe process structure")),
        ("Tolerance <i>(resistant to maloperation)</i>",
         (_D, "corrosiveness, equipment safety, safe process structure")),
        ("Ease of Control",
         (_D, "safe process structure, heat of reaction")),
    ]
    for head, (piis, isi) in g:
        rows.append(head)
        rows.append((piis, isi))
    return rows
