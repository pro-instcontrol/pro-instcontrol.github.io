# -*- coding: utf-8 -*-
"""Book 5, Chapter 11 — Subindices for the Process Inherent Safety Index
(EN/VI bilingual).

Source: Heikkilä, *Inherent Safety in Process Plant Design — An Index-Based
Approach*, VTT Publications 384 (1999), pp. 68–90.  The chapter defines the
process subindices: inventory (Table 15, ISBL/OSBL scales after the Mond
Index scaled by expert recommendations), process temperature (Table 16),
process pressure (Table 17, Dow F&EI limits), equipment safety (Tables 18–24:
layout-spacing comparisons, large-loss statistics, ignition sources, ISBL and
OSBL score tables) and safe process structure (Figure 6 — CBR database
levels, redrawn — and Table 25).
"""

from isd_common import fig, h2, h3, note, p, table
import isdfig as F

PAGES_SRC = 23           # source pages 68–90
BYLINE = "Anna-Mari Heikkilä · VTT Publications 384 (1999)"
TITLE_EN = "Subindices for the Process Inherent Safety Index"
TITLE_VI = "Chỉ số thành phần của an toàn nội tại quá trình"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 11.</b> tồn kho (inventory) — khối lượng "
                "chất trong thiết bị · thời gian lưu (residence time) · ISBL / "
                "OSBL — trong/ngoài giới hạn thiết bị · thermal stress — ứng "
                "suất nhiệt · Mond Index (ICI, 1985) · Dow F&E Index (Dow, "
                "1987) · tốc độ hỏng hóc (failures/year) — Arulanantham và Lees "
                "(1981) · nghiên cứu Canvey (HSE, 1978) · suy luận dựa trên "
                "tình huống (CBR) — cơ sở dữ liệu quá trình/trợ giúp/chi tiết "
                "(Hình 6) · khoảng cách bố trí tối thiểu · nguồn kích giữ "
                "(ignition source).")
    return ("<b>Key terms.</b> inventory — the mass of chemicals held in "
            "equipment · residence time · ISBL / OSBL — inside/outside battery "
            "limits · thermal stress · Mond Index (ICI, 1985) · Dow F&E Index "
            "(Dow, 1987) · failure rates (failures/year) — Arulanantham and "
            "Lees (1981) · the Canvey study (HSE, 1978) · case-based reasoning "
            "(CBR) — process/system/detail database levels (Figure 6) · "
            "minimum layout spacing · ignition source.")


_D = '<span style="color:#bbb">—</span>'

# Source Table 15 (p. 69): inventory subindex II — ISBL vs OSBL scales.
_T15 = [
    ("0–1 t", "0–10 t", "0"),
    ("1–10 t", "10–100 t", "1"),
    ("10–50 t", "100–500 t", "2"),
    ("50–200 t", "500–2000 t", "3"),
    ("200–500 t", "2000–5000 t", "4"),
    ("500–1000 t", "5000–10000 t", "5"),
]

# Source Table 16 (p. 70): process temperature subindex IT.
_T16 = [
    ("&lt; 0 °C", "1"),
    ("0–70 °C", "0"),
    ("70–150 °C", "1"),
    ("150–300 °C", "2"),
    ("300–600 °C", "3"),
    ("&gt; 600 °C", "4"),
]

# Source Table 17 (p. 71): process pressure subindex Ip.
_T17 = [
    ("0.5–5 bar", "0"),
    ("0–0.5 hoặc 5–25 bar", "1"),
    ("25–50 bar", "2"),
    ("50–200 bar", "3"),
    ("200–1000 bar", "4"),
]

_T17_EN = [
    ("0.5–5 bar", "0"),
    ("0–0.5 or 5–25 bar", "1"),
    ("25–50 bar", "2"),
    ("50–200 bar", "3"),
    ("200–1000 bar", "4"),
]

# Source Table 18 (p. 74): average spacing recommendations, ISBL items
# (Prugh 1982 / Bausbacher & Hunt 1993 / Industrial Risk Insurers 1991 /
# Institut Français du Pétrole).  Cells transcribed from the print; a dash
# marks values not printed in the source.
_T18 = [
    ("Lò nung · Furnaces", "15.3", "11", "15.7", "13.2"),
    ("Máy nén · Compressors", "9.6", "4.6", "14.2", "9.1"),
    ("Lò phản ứng nguy hiểm cao · Reactors (high hazard)*", "8.9", _D, "11", _D),
    ("Giàn làm mát bằng không khí · Air coolers", "8.1", "4.4", "10", "5.4"),
    ("Lò phản ứng · Reactors", "8", "4.2", "9.2", "5.4"),
    ("Bơm nguy hiểm cao · Pumps (high hazard)*", "8.8", "4.1", "8.2", "5.3"),
    ("Tháp, bình phân tách · Towers, drums", "7.7 / 7.2", "3.2", "10", "4.0 / 2.8"),
    ("Bộ trao đổi nhiệt · Heat exchangers", "7.5–6.6", "2.3", "7.8", "4.9–3.6"),
    ("Bơm (đầu nhẹ/thông thường) · Pumps (light ends/normal)",
     "7.7 / 6.3", _D, "7", "4.6 / 4.3"),
    ("Thiết bị chứa chất không cháy · Equipment handling non-flammables",
     "1.7 min (= 1 m)", "1.6", _D, _D),
]

# Source Table 19 (p. 76): average spacing recommendations, OSBL items
# (Bausbacher & Hunt 1993 / Prugh 1982 / Mecklenburgh 1985).
_T19 = [
    ("Đốt trên mặt đất, hở · Flare on ground, open", "60–120", "120", "150"),
    ("Đốt trên mặt đất, che chắn · Flare on ground, shielded", _D, "95", "&gt;60"),
    ("Tháp làm mát · Cooling towers", "78", "49", "31"),
    ("Lò hơi / nhà lò hơi · Boilers / boiler houses", "75", "41", _D),
    ("Máy nén · Compressors", "59", "48", _D),
    ("Hệ xả khẩn cấp · Blowdown facilities", "75", "43", _D),
    ("Bình chứa có áp · Pressure storage tanks", "74", "49", "35"),
    ("Bình chứa khí áp thấp (&lt; 1 barg) · Low pressure gas storage tanks",
     "74", "34", _D),
    ("Bình chứa khí quyển chất lỏng cháy (FP&lt;38°C) · Atmospheric flammable "
     "liquid storage tanks (FP&lt;38°C)", "72", "43", "34"),
    ("Bình chứa khí quyển (FP&gt;38°C) · Atmospheric storage tanks (FP&gt;38°C)",
     "72", "40", _D),
    ("Bơm trên điểm tự bốc cháy · Pumps above autoignition", _D, "34", _D),
    ("Bơm (đầu nhẹ và chất cháy khác) · Pumps (light ends and other flammables)",
     _D, "30", _D),
    ("Bơm chất không cháy · Pumps handling non-flammables", _D, "24", _D),
]

# Source Table 20 (p. 77): ISBL equipment involved in large losses
# (Mahoney 1992: % losses, avg $M; Instone 1989: % of losses).
_T20 = [
    ("Lò phản ứng · Reactors", "13", "67.9", "3"),
    ("Bình phân tách quá trình · Process drums", "7", "26.1", "3"),
    ("Bơm – máy nén · Pumps – compressors", "6", "29.1", "5+5"),
    ("Bộ trao đổi nhiệt · Heat exchangers", "4", "23.8", "4"),
    ("Tháp quá trình · Process towers", "4", "58.5", "3"),
    ("Lò gia nhiệt – lò hơi · Heaters – boilers", "2", "18.6", "10+5"),
]

# Source Table 21 (p. 78): OSBL equipment involved in large losses.
_T21 = [
    ("Bình chứa · Tanks", "15", "62", "14"),
    ("Bơm – máy nén* · Pumps – compressors*", "8", "8", "5 + 5"),
    ("Lò gia nhiệt – lò hơi* · Heaters – boilers*", "2", "16", "10 + 5"),
    ("Nhà kho · Warehouse", _D, _D, "3"),
    ("Ống đốt · Flare", _D, _D, "&lt;1"),
    ("Tháp làm mát · Cooling tower", _D, _D, "&lt;1"),
    ("Bể tách API · API separator", _D, _D, "&lt;1"),
]

# Source Table 22 (p. 79): sources of ignition.
_T22 = [
    ("Bề mặt nóng · Hot surfaces", "18", "16", "18"),
    ("Lò nung · Furnace", "18", "4", _D),
    ("Lò hơi · Boiler", "&lt;3", "2", "18"),
    ("Ống đốt · Flare", "&lt;3", "6.5", _D),
]

# Source Table 23 (p. 83): I_EQ scores for ISBL.
_T23 = [
    ("Thiết bị chứa chất không cháy, không độc · Equipment handling "
     "nonflammable, nontoxic materials", "0"),
    ("Bộ trao đổi nhiệt, bơm, tháp, bình phân tách · Heat exchangers, pumps, "
     "towers, drums", "1"),
    ("Giàn làm mát, lò phản ứng, bơm nguy hiểm cao · Air coolers, reactors, "
     "high hazard pumps", "2"),
    ("Máy nén, lò phản ứng nguy hiểm cao · Compressors, high hazard reactors", "3"),
    ("Lò nung, lò gia nhiệt · Furnaces, fired heaters", "4"),
]

# Source Table 24 (p. 85): I_EQ scores for OSBL.
_T24 = [
    ("Thiết bị chứa chất không cháy, không độc · Equipment handling "
     "nonflammable, nontoxic materials", "0"),
    ("Bình chứa khí quyển, bơm · Atmospheric storage tanks, pumps", "1"),
    ("Tháp làm mát, máy nén, hệ xả, bình chứa có áp hoặc lạnh · Cooling towers, "
     "compressors, blowdown systems, pressurised or refrigerated storage tanks", "2"),
    ("Ống đốt, lò hơi, lò nung · Flares, boilers, furnaces", "3"),
]

# Source Table 25 (p. 90): I_ST values.
_T25 = [
    ("Được khuyến nghị (tiêu chuẩn an toàn v.v.) · Recommended (safety etc. "
     "standard)", "0"),
    ("Thực hành kỹ thuật tốt · Sound engineering practice", "1"),
    ("Không có dữ liệu hoặc trung tính · No data or neutral", "2"),
    ("Có khả năng không an toàn · Probably unsafe", "3"),
    ("Đã có tai nạn nhỏ · Minor accidents", "4"),
    ("Đã có tai nạn lớn · Major accidents", "5"),
]

_T25_EN = [
    ("Recommended (safety etc. standard)", "0"),
    ("Sound engineering practice", "1"),
    ("No data or neutral", "2"),
    ("Probably unsafe", "3"),
    ("Minor accidents", "4"),
    ("Major accidents", "5"),
]


def body_vi():
    b = []

    b.append(h2("11. Các chỉ số thành phần của chỉ số an toàn nội tại quá trình",
                "11. Subindices for Process Inherent Safety Index"))

    b.append(p("Chỉ số an toàn nội tại quá trình thể hiện an toàn nội tại của "
               "<b>bản thân quá trình</b>, gồm cả thiết bị và các tham số vận "
               "hành. Chỉ số được chia thành các chỉ số thành phần về tồn kho, "
               "nhiệt độ, áp suất, an toàn thiết bị và cấu trúc quá trình an "
               "toàn."))

    # ---- 11.1 inventory ------------------------------------------------------
    b.append(h3("11.1 Chỉ số tồn kho", "11.1 Inventory Subindex"))

    b.append(p("Tính chính xác tồn kho trong giai đoạn thiết kế khái niệm là "
               "khó, vì kích thước thiết bị thường chưa biết. Tuy nhiên <b>dòng "
               "khối lượng</b> trong quá trình đã biết từ công suất thiết kế. "
               "Vì vậy việc ước tính tồn kho dựa trên dòng khối lượng và thời "
               "gian lưu ước tính là thực tế hơn: tồn kho được đưa vào ISI dưới "
               "dạng dòng khối lượng trong thiết bị ISBL (gồm cả tuần hoàn) với "
               "<b>thời gian lưu danh nghĩa một giờ</b> cho mỗi bình quá trình "
               "(lò phản ứng, cột chưng cất v.v.). Với bồn chứa lớn, kích thước "
               "cần được ước tính. Tổng tồn kho là tổng tồn kho của mọi bình "
               "quá trình."))

    b.append(p("Ở khu vực OSBL, kích thước bồn thường không biết trong thiết kế "
               "khái niệm, nên tồn kho OSBL không tính trực tiếp được — nó phụ "
               "thuộc cả điều kiện địa phương, logistics v.v. Đối với tồn kho "
               "OSBL, các giá trị của Mond Index (ICI, 1985) đã được dùng. "
               "Edwards và cộng sự (1993) cũng dùng chúng cho ISBL, nhưng các "
               "chuyên gia phê bình vì thang tồn kho liên quan trong ISBL nhỏ "
               "hơn nhiều; thêm nữa, do bố trí dày đặc hơn, cùng một lượng tồn "
               "kho trong ISBL nguy hiểm hơn trong OSBL. Vì vậy một thang mới "
               "được xây dựng bằng cách hiệu chỉnh giá trị Mond theo khuyến "
               "nghị của chuyên gia trong công trình của Lawrence (1996) — "
               "xem Bảng 15."))
    b.append(table(("Tồn kho ISBL", "Tồn kho OSBL", "Điểm I<sub>I</sub>"), _T15,
              "Bảng 15 · Xác định chỉ số tồn kho I<sub>I</sub>."))

    # ---- 11.2 temperature ----------------------------------------------------
    b.append(h3("11.2 Chỉ số nhiệt độ quá trình",
                "11.2 Process Temperature Subindex"))

    b.append(p("Nhiệt độ là chỉ báo của năng lượng nhiệt trong hệ. Mối nguy "
               "tăng ở nhiệt độ cao vì bản thân năng lượng chứa trong hệ và vì "
               "<b>độ bền vật liệu suy giảm ở nhiệt độ cao hoặc rất thấp</b>. "
               "Biến thiên nhiệt độ lớn giữa trạng thái dừng (nhiệt độ môi "
               "trường) và nhiệt độ vận hành cũng gây ứng suất nhiệt, làm tăng "
               "nguy cơ mất containment."))
    b.append(p("Nhiệt độ quá trình trong ISI xác định trên cơ sở <b>nhiệt độ "
               "tối đa</b> trong vùng quá trình đang xét — khả thi vì ở giai "
               "đầu thiết kế đã có ước tính sơ bộ nhiệt độ và áp suất. Vì các "
               "mối nguy ở nhiệt độ thấp tăng lên do vấn đề cơ học và đóng băng "
               "khi có nước, các nhiệt độ dưới 0 °C cũng được đưa vào chỉ số. "
               "Khi có nhiều mức nhiệt độ trong vùng đang xét, <b>giá trị chỉ "
               "số nhiệt độ cao nhất</b> được áp dụng. Các khoảng nhiệt độ "
               "được chọn dựa trên nguy hiểm cho con người và độ bền vật liệu "
               "theo nhiệt độ: 0–70 °C vô hại với con người nói chung; "
               "70–150 °C là vùng nhiệt độ điển hình của quá trình nhiệt độ "
               "nhẹ; giới hạn tiếp theo là 300 °C — trên ngưỡng này độ bền thép "
               "carbon giảm đáng kể so với nhiệt độ phòng; nhiệt độ cao hơn cần "
               "vật liệu chịu nhiệt tốt hơn. Nhiệt độ dưới 0 cũng gây vấn đề "
               "như đã trình bày ở mục 7.6."))
    b.append(table(("Nhiệt độ quá trình", "Điểm I<sub>T</sub>"), _T16,
              "Bảng 16 · Xác định chỉ số nhiệt độ quá trình I<sub>T</sub>."))

    # ---- 11.3 pressure -------------------------------------------------------
    b.append(h3("11.3 Chỉ số áp suất quá trình", "11.3 Process Pressure Subindex"))

    b.append(p("Áp suất là chỉ báo của <b>thế năng</b> ảnh hưởng đến tốc độ rò "
               "rỉ khi mất containment. Áp suất cao hơn cũng đòi hỏi yêu cầu "
               "khắt khe hơn về độ bền bình chứa. Rò rỉ ở thiết bị chân không "
               "có thể gây hút không khí vào và theo đó là nổ. Trong ISI, áp "
               "suất quá trình xác định trên cơ sở <b>áp suất tối đa trong vùng "
               "quá trình ở điều kiện vận hành bình thường</b>; các giới hạn "
               "trong Bảng 17 dựa trên Dow F&amp;E Index (Dow, 1987)."))
    b.append(table(("Áp suất quá trình", "Điểm I<sub>p</sub>"), _T17,
              "Bảng 17 · Xác định chỉ số áp suất quá trình I<sub>p</sub>."))

    # ---- 11.4 equipment ------------------------------------------------------
    b.append(h3("11.4 Chỉ số an toàn thiết bị", "11.4 Equipment Safety Subindex"))

    b.append(p("Chỉ số an toàn thiết bị được đưa vào ISI để có cái nhìn tốt "
               "hơn về an toàn nội tại tổng thể, bằng cách xét cả <b>lựa chọn "
               "và loại thiết bị</b> sử dụng (Heikkilä và Hurme, 1998a, 1998b). "
               "An toàn thiết bị cố đo khả năng một thiết bị là không an toàn. "
               "Ở đây thiết bị gồm các thiết bị chính như bơm, bình chứa v.v., "
               "nhưng không gồm đường ống, van hay thiết bị đo — vì chúng chưa "
               "được thiết kế ở giai đoạn thiết kế đầu. Chỉ số an toàn thiết bị "
               "xét an toàn của thiết bị như một thực thể riêng, không xét "
               "tương tác qua quá trình với thiết bị khác — khía cạnh sau được "
               "mô tả bởi chỉ số cấu trúc quá trình an toàn. Tuy nhiên, tương "
               "tác qua bố trí — ví dụ lò nung có thể là nguồn kích giữ cho rò "
               "rỉ từ thiết bị khác — được chỉ số an toàn thiết bị xét đến."))
    b.append(p("Hỏng hóc chính của thiết bị là <b>mất containment quá trình</b>. "
               "Hệ quả phụ thuộc tính chất và lượng chất rò rỉ cùng điều kiện "
               "trong và ngoài thiết bị. Bơm và máy nén (Marshall, 1987) có lẽ "
               "là vị trí dễ tổn thương nhất của hệ có áp, vì chúng chứa bộ "
               "phận chuyển động và chịu xói mòn, xoáy cavitation; chúng còn "
               "tạo rung động có thể dẫn đến hỏng mỏi. Cả ghim bịt và ổ trục "
               "của bơm, máy nén đều dễ hỏng. Hệ khuấy cũng gặp khó khăn do ứng "
               "suất cơ học dù tốc độ thấp hơn nhiều so với bơm."))

    b.append(h3("11.4.1 Đánh giá an toàn thiết bị",
                "11.4.1 Evaluation of Equipment Safety"))

    b.append(p("So sánh an toàn của thiết bị không đơn giản: nó phụ thuộc bản "
               "thân thiết bị và điều kiện quá trình. An toàn thiết bị có thể "
               "đánh giá từ <b>dữ liệu tai nạn và hỏng hóc định lượng</b> và từ "
               "<b>thực hành và khuyến nghị kỹ thuật</b>. Thông tin dựa trên "
               "kinh nghiệm tìm thấy trong khuyến nghị bố trí và các phương "
               "pháp phân tích an toàn như Dow F&amp;E Index (1987); dữ liệu "
               "định lượng từ thống kê tai nạn và vận hành. Cần nhớ rằng "
               "<b>không phải mọi thông tin tin cậy hay hỏng hóc đều thể hiện "
               "an toàn trực tiếp</b>: không phải mọi hỏng hóc đều nguy hiểm và "
               "không phải mọi tai nạn đều do hỏng hóc thiết bị."))
    b.append(p("Với chỉ số an toàn thiết bị, khu vực nhà máy được chia thành "
               "hai vùng có tính chất an toàn khác nhau. Vùng <b>ISBL</b> là "
               "nơi nguyên liệu được biến thành sản phẩm — đặc trưng bởi số "
               "lượng lớn thiết bị và đường ống tập trung trong diện tích nhỏ. "
               "Phần còn lại là vùng <b>OSBL</b> — đặc trưng bởi tồn kho lớn "
               "chất lỏng thường cháy và/hoặc độc; số thiết bị ít hơn nhưng cỡ "
               "lớn hơn, bố trí thưa hơn nhiều để tăng an toàn."))

    b.append(h3("11.4.2 Bố trí thiết bị", "11.4.2 Equipment Layout"))

    b.append(p("Trong thiết kế nhà máy, an toàn thiết bị cũng được bảo đảm qua "
               "<b>bố trí</b>: mục tiêu là tối thiểu hóa rủi ro cho con người, "
               "tối thiểu hóa lan truyền (trong nhà máy và sang nhà máy kề "
               "bên), bảo đảm tiếp cận khẩn cấp đủ dụng, cũng như tiếp cận cho "
               "bảo trì và vận hành. Bố trí an toàn được thiết kế trên cơ sở "
               "tiêu chuẩn thiết kế và quy định địa phương — thường diễn đạt "
               "dạng khoảng cách tối thiểu giữa các thiết bị. Về nguyên tắc, "
               "khoảng cách an toàn có thể tính bằng cách ước tính cỡ rò rỉ có "
               "thể, xác suất kích giữ và nổ cùng hệ quả; nhưng cách này đầy "
               "khó khăn nên <b>khoảng cách tối thiểu dựa trên kinh nghiệm</b> "
               "được dùng thay thế (Wells, 1980). Dù sơ đồ bố trí chưa có ở "
               "khâu thiết kế sơ bộ, các khuyến nghị khoảng cách cho ý niệm "
               "về mức rủi ro của từng thiết bị đối với môi trường xung quanh."))
    b.append(p("Khoảng cách bố trí còn chịu ảnh hưởng của các yếu tố khác ngoài "
               "an toàn: không gian cho bảo trì, sửa chữa và vận hành tốt; đủ "
               "chỗ cho đường ống, giá đỡ và móng. Các khuyến nghị khoảng cách "
               "được trình bày trong tài liệu dạng ma trận và danh sách khoảng "
               "cách tối thiểu. Trong công trình này, các ma trận khoảng cách "
               "của Industrial Risk Insurers (1991), Bausbacher và Hunt (1993), "
               "Prugh (1982), Mecklenburgh (1985) và Institut Français du "
               "Petrole đã được so sánh. Khoảng cách phù hợp tới một thiết bị "
               "khác phụ thuộc phần lớn vào tính chất an toàn của thiết bị; "
               "khoảng cách cho bảo trì và tiếp cận thường ngắn hơn khoảng cách "
               "an toàn. Vì vậy đã giả định rằng <b>trung bình các khoảng cách "
               "khuyến nghị</b> phản ánh chủ yếu mức không an toàn chung của "
               "một thiết bị, chứ không phải khía cạnh bảo trì."))
    b.append(p("Việc đánh giá dữ liệu bố trí được thực hiện bằng cách tính "
               "<b>trung bình các khoảng cách khuyến nghị</b>; ở một số ma "
               "trận không có khoảng cách vận hành/bảo trì thì dùng tối thiểu "
               "một mét. Thứ tự các thiết bị theo yêu cầu khoảng cách trung "
               "bình <b>gần như giống hệt nhau trong mọi ma trận</b>: cho bố "
               "trí ISBL (Bảng 18), lò nung, máy nén và lò phản ứng nguy hiểm "
               "cao đứng đầu danh sách, còn thiết bị chứa chất không cháy, "
               "không độc nằm ở cuối. Nhóm đầu cần khoảng cách an toàn thêm; "
               "nhóm sau chỉ cần đủ chỗ để vận hành, sửa chữa và bảo trì. "
               "Ngoại lệ là thứ hạng cao hơn của các tháp trong ma trận của "
               "Industrial Risk Insurers (1991) — có lẽ do tồn kho lớn của "
               "chất gây tổn thất kinh tế lớn khi vỡ."))
    b.append(table(("Thiết bị", "Prugh (1982)", "Bausbacher và Hunt (1993)",
                    "Industrial Risk Insurers (1991)", "Institut Français du Petrole"),
              _T18,
              "Bảng 18 · So sánh khuyến nghị khoảng cách trung bình cho một số "
              "thiết bị ISBL (mét). * nguy hiểm cao = chứa chất trên điểm tự "
              "bốc cháy; ô gạch nối = không in trong tài liệu gốc."))
    b.append(p("Các khuyến nghị khoảng cách trung bình cho thiết bị OSBL cho "
               "thấy thứ tự thiết bị <b>cũng khá giống nhau trong mọi ma trận</b> "
               "(Bảng 19). Ống đốt (flare) nhận khuyến nghị khoảng cách lớn "
               "nhất rõ rệt — nhằm ngăn kích giữ hay thiệt hại do bức xạ nhiệt "
               "và khả năng rơi chất lỏng đang cháy; mọi hơi cháy thoát ra từ "
               "các phần khác của nhà máy phải khuếch tán xuống dưới giới hạn "
               "cháy dưới trước khi tới ống đốt."))
    b.append(table(("Thiết bị", "Bausbacher và Hunt (1993)", "Prugh (1982)",
                    "Mecklenburgh (1985)"), _T19,
              "Bảng 19 · So sánh khuyến nghị khoảng cách trung bình cho một số "
              "thiết bị OSBL (mét). Ô gạch nối = không in trong tài liệu gốc."))
    b.append(p("Tháp làm mát có khoảng cách lớn xung quanh: nếu chất cháy có "
               "thể vào nước làm mát rồi thoát ra khí quyển thì <b>không được "
               "có nguồn kích giữ gần tháp</b>; tháp làm mát tạo khối lượng lớn "
               "không khí ẩm gây sương mù, mưa, đóng băng và ăn mòn về phía "
               "xuống gió, và cần bể nước cùng móng lớn. Các hệ trợ giúp khác "
               "cũng có khuyến nghị rộng: lò hơi có ngọn lửa và bề mặt nóng — "
               "nguồn kích giữ; máy nén cần khoảng cách lớn để tách rò rỉ khỏi "
               "nguồn kích giữ, gây rung động có thể làm rò rỉ đường ống và "
               "cần không gian xung quanh để vận hành, bảo trì."))
    b.append(p("Bình chứa thường nằm ở bồn khu. Khoảng cách xung quanh và tới "
               "thiết bị khác phụ thuộc <b>chất chứa, mức nguy hiểm tiềm năng "
               "và khả năng thay đổi bất ngờ điều kiện chứa</b>. Bồn chứa nên "
               "ở vị trí an toàn, xa vùng quá trình và khu công cộng; cần ngăn "
               "cháy lan giữa các bồn bằng cách giữ bức xạ nhiệt ở mức chấp "
               "nhận được (Mecklenburgh, 1985). Các loại bồn khác nhau — khí "
               "quyển hoặc có áp, mái cố định hoặc mái nổi, nhiệt độ thấp hoặc "
               "cao — có khuyến nghị khoảng cách riêng theo pha chất lỏng, áp "
               "suất chứa và điểm chớp cháy (Bảng 19). Bơm cũng có thể làm "
               "việc với chất lỏng dưới hoặc trên điểm chớp cháy/điểm tự bốc "
               "cháy — điều được các khuyến nghị bố trí chung ghi nhận."))

    b.append(h3("11.4.3 Thiết bị trong các tổn thất lớn",
                "11.4.3 Equipment Involved in Large Losses"))

    b.append(p("Mahoney (1997) đã phân tích <b>170 tổn thất lớn nhất</b> trong "
               "nhà máy lọc dầu, hóa dầu và xử lý khí từ 1966 đến 1996: gần "
               "như mọi tổn thất đều liên quan cháy hoặc nổ, và <b>nguyên nhân "
               "chính phổ biến nhất là đường ống</b>. Instone (1989) phân tích "
               "khoảng 2000 hồ sơ bồi thường tổn thất lớn của công nghiệp "
               "hydrocarbon tại Cigna Insurance. Bảng 20 liệt kê thiết bị ISBL "
               "và Bảng 21 trình bày dữ liệu thiết bị OSBL theo Mahoney (1992, "
               "1997) và Instone (1989)."))
    b.append(table(("Loại thiết bị", "% tổn thất (Mahoney, 1992)",
                    "Tổn thất bình quân (triệu $, Mahoney, 1992)",
                    "% tổn thất (Instone, 1989)"), _T20,
              "Bảng 20 · Một số thiết bị ISBL liên quan tổn thất lớn."))
    b.append(p("Trong Bảng 20, <b>lò phản ứng</b> tham gia 13% sự cố (Mahoney, "
               "1992) và tạo tổn thất bình quân cao nhất, vì lò phản ứng hư "
               "hỏng do nổ lan tàn phá ra vùng rộng. <b>Tháp quá trình</b> chỉ "
               "tham gia 4% sự cố nhưng tổn thất bình quân cao thứ hai: ít tai "
               "nạn nhưng tổn thất kinh tế lớn do tồn kho lớn trong tháp. Lò "
               "gia nhiệt và lò hơi chỉ gây 2% sự cố với tổn thất bình quân "
               "thấp nhất; tuy nhiên trong nhiều trường hợp chúng có thể là "
               "<b>nguyên nhân thứ cấp</b> dưới dạng nguồn kích giữ — điều "
               "không được thể hiện trong dữ liệu của Mahoney."))
    b.append(p("Theo Instone (1989), thiết bị thường gặp nhất trong tổn thất "
               "lớn là <b>lò nung hoặc lò hơi (15%)</b>, còn lò phản ứng và "
               "bình phân tách khá hiếm (mỗi loại 3%) — khác biệt chính so với "
               "dữ liệu Mahoney. Lý do có thể: Instone phân tích các đơn vị "
               "quá trình <b>tham gia</b> vào tổn thất lớn, còn Mahoney phân "
               "tích <b>nguyên nhân chính</b>."))
    b.append(table(("Loại thiết bị", "% tổn thất (Mahoney, 1997)",
                    "Tổn thất bình quân (triệu $, Mahoney, 1997)",
                    "% tổn thất (Instone, 1989)"), _T21,
              "Bảng 21 · Một số thiết bị OSBL liên quan tổn thất lớn. "
              "* gồm cả OSBL và ISBL."))
    b.append(p("Trong dữ liệu OSBL của Mahoney (1997), <b>bình chứa</b> nói "
               "chung tham gia 15% tai nạn; tồn kho lớn và chi phí thay thế "
               "cao của bồn cùng phụ kiện dẫn đến hậu quả đắt giá. <b>Bơm và "
               "máy nén</b> tham gia 8% sự cố nhưng tổn thất bình quân cao "
               "nhất — do chi phí thay thế máy nén và hệ điện của chúng cao; "
               "bơm thường đặt cạnh nhau nên một tai nạn phá hủy nhiều bơm "
               "cùng lúc. Lò gia nhiệt và lò hơi chỉ 2% với tổn thất bình quân "
               "thấp nhất. Trong dữ liệu của Instone (1989), thiết bị OSBL "
               "thường gặp nhất là <b>bình chứa (14%)</b>; lò gia nhiệt và lò "
               "hơi được nhắc trong 15% sự cố; bơm, máy nén và lò hơi ngang "
               "nhau (5% mỗi loại); ống đốt, tháp làm mát và bể tách API khá "
               "hiếm (mỗi loại &lt;1%). Khác biệt về lò gia nhiệt/lò hơi giữa "
               "hai nguồn dữ liệu lại do góc nhìn nguyên nhân chính vs tham "
               "gia — lò hơi là nguồn kích giữ phổ biến nhất (Bảng 22) nên "
               "Mahoney có lẽ xếp chúng là nguyên nhân thứ cấp."))
    b.append(table(("Nguồn kích giữ", "% kích giữ (Instone, 1989)",
                    "% kích giữ đã biết (Planas-Cuchi và cộng sự, 1997)",
                    "% kích giữ đã biết (Fire Protection Association, 1974)"),
              _T22,
              "Bảng 22 · Một số nguồn kích giữ."))

    b.append(h3("11.4.4 Thiết bị trong các chỉ số khác",
                "11.4.4 Equipment in Other Indices"))

    b.append(p("Một chỉ số an toàn dùng phổ biến trong công nghiệp quá trình là "
               "Dow Fire &amp; Explosion Hazard Index (1987). Dow F&amp;E Index "
               "cho <b>hình phạt</b> đối với thiết bị gia nhiệt và một số thiết "
               "bị quay xác định — thuộc nhóm Special Process Hazards, trong đó "
               "các hình phạt của đơn vị quá trình được cộng lại. Thiết bị gia "
               "nhiệt bị phạt nếu chất trong đơn vị gần cửa hút khí của lò có "
               "thể thoát trên điểm sôi, là bụi cháy được, hoặc có thể thoát "
               "trên điểm sôi; hình phạt phụ thuộc khoảng cách từ nguồn rò rỉ "
               "có thể, dao động 0.1–1.0 — ví dụ 15 m cho hình phạt 0.27 (trên "
               "điểm chớp cháy) và 0.60 (trên điểm sôi). Tình huống với chất "
               "xử lý dưới điểm chớp cháy không bị phạt."))
    b.append(p("Thiết bị quay lớn — 1) máy nén trên 450 kW, 2) bơm trên 56 kW, "
               "3) khuấy và bơm tuần hoàn mà hỏng hóc có thể tạo phản ứng tỏa "
               "nhiệt, 4) thiết bị quay lớn tốc độ cao khác có lịch sử tổn "
               "thất đáng kể, ví dụ máy li tâm — đều nhận hình phạt không đổi "
               "0.5. Thang hình phạt này <b>hẹp hơn nhiều</b> so với thang "
               "khoảng cách bố trí hoặc chi phí tổn thất lớn, vì Dow F&amp;E "
               "Index chỉ xét thiết bị quay lớn — được biết có nhiều khả năng "
               "góp phần vào tai nạn hơn thiết bị nhỏ; thiết bị nhỏ an toàn "
               "hơn nên không bị phạt."))

    b.append(h3("11.4.5 Hỏng hóc thiết bị và đánh giá",
                "11.4.5 Equipment Failures and Their Evaluation"))

    b.append(p("Có một lượng thông tin thống kê nhất định về hỏng hóc của các "
               "thành phần hệ quá trình. Arulanantham và Lees (1981) nghiên "
               "cứu hỏng hóc bình áp lực trong các nhà máy như nhà máy olefin: "
               "hỏng hóc được định nghĩa là tình trạng mà vết nứt, rò rỉ hay "
               "khuyết tật đã phát triển đến mức phải sửa chữa hoặc thay thế — "
               "gồm cả các hỏng hóc tiềm năng nguy hiểm lẫn mọi hỏng hóc thảm "
               "khốc. Trong nhà máy olefin, <b>lò gia nhiệt có tốc độ hỏng "
               "khoảng 0.4 hỏng hóc/năm</b>, bình áp lực quá trình 0.0025/năm "
               "và bộ trao đổi nhiệt 0.0015/năm — lò gia nhiệt kém an toàn hơn "
               "nhiều so với bình áp lực."))
    b.append(p("Trong nghiên cứu Canvey (King, 1990; Health and Safety "
               "Executive, 1978) về mối nguy tiềm năng cho công chúng từ hoạt "
               "động công nghiệp tại đảo Canvey/Thurrock, Essex, bình áp lực "
               "có tần suất hỏng thảm khốc giả định <b>lớn gấp mười lần</b> "
               "bơm LPG. Crawley và Grant (1997) phát triển công cụ đánh giá "
               "rủi ro cho nhà máy ngoài khơi mới: họ khảo sát tần suất rò rỉ "
               "điển hình của các thiết bị và xác suất kích giữ trong bốn dải "
               "áp suất; từ đó xác định cỡ rò rỉ, tần suất và tần suất rò rỉ "
               "bị kích giữ cho mọi thiết bị. Trong nhà máy ngoài khơi, bình "
               "tách khí có tần suất sự kiện bị kích giữ <b>cao gấp mười lần</b> "
               "bơm dầu."))

    b.append(h3("11.4.6 Chỉ số an toàn thiết bị cho ISBL",
                "11.4.6 Equipment Safety Subindex for ISBL"))

    b.append(p("Từ dữ liệu đã trình bày, thứ tự thiết bị trong các khuyến nghị "
               "khoảng cách bố trí gần như giống hệt nhau: lò nung và lò gia "
               "nhiệt đứng đầu; tiếp theo là máy nén và lò phản ứng nguy hiểm "
               "cao; rồi giàn làm mát, lò phản ứng thường và bơm nguy hiểm "
               "cao; sau đó tháp, bình phân tách, bộ trao đổi nhiệt và bơm; "
               "nhóm an toàn nhất là thiết bị chứa chất không cháy, không độc. "
               "Khác biệt duy nhất là thứ hạng cao hơn của tháp/bình trong dữ "
               "liệu Industrial Risk Insurers (1991) — có lẽ do tồn kho chất "
               "cháy lớn; vì tồn kho đã được xét riêng bằng chỉ số tồn kho, "
               "các bình nên được xếp cùng nhóm với bộ trao đổi nhiệt và bơm."))
    b.append(p("Thống kê tai nạn về thiết bị trong tổn thất lớn cho thông tin "
               "hơi mâu thuẫn (Bảng 20): theo Mahoney (1992), nguyên nhân chính "
               "phổ biến nhất là <b>lò phản ứng</b>, tiếp theo là bình phân "
               "tách, còn lò gia nhiệt thuộc nhóm an toàn nhất; ngược lại với "
               "dữ liệu Instone (1989), nơi lò nung/lò hơi thường gặp nhất. Vì "
               "lò nung là nguồn kích giữ cho rò rỉ cháy từ thiết bị khác, "
               "chúng không nhất thiết được liệt kê là nguyên nhân chính dù có "
               "lẽ tham gia như nguyên nhân thứ cấp trong nhiều tổn thất. Do "
               "đó, việc đưa cả lò phản ứng lẫn lò nung vào nhóm thiết bị kém "
               "an toàn nhất là hợp lý."))
    b.append(p("Chúng tôi xếp <b>lò nung kém an toàn hơn (điểm 4) so với lò "
               "phản ứng (điểm 3 hoặc 2)</b>, vì lò gia nhiệt là nguồn kích giữ "
               "phổ biến nhất (Instone, 1989) cho mọi rò rỉ; Instone cũng liệt "
               "kê lò nung là thiết bị thường tham gia tổn thất nhất; Dow "
               "F&amp;E Index (1987) có thể cho hình phạt cao hơn cho lò nung "
               "so với lò phản ứng hoặc máy nén lớn; và Arulanantham cùng Lees "
               "(1981) cho tốc độ hỏng cơ học rất cao cho lò gia nhiệt nhà máy "
               "olefin. <b>Máy nén</b> được xếp rất kém an toàn vì chúng là "
               "thiết bị dễ tổn thương (Marshall, 1987): chứa bộ phận chuyển "
               "động, chịu rung động, có thể xả khí cháy khi hỏng, và đứng rất "
               "cao trong danh sách bố trí. Với <b>bình phân tách, tháp, bộ "
               "trao đổi nhiệt và bơm</b> (dưới điểm tự bốc cháy), Mahoney "
               "(1997) và Instone (1989) cho thống kê tổn thất thấp tương tự, "
               "Arulanantham và Lees (1981) cho tốc độ hỏng cơ học gần nhau — "
               "từ đó cùng dữ liệu bố trí, chúng được gộp thành một mức điểm "
               "thấp (điểm 1)."))
    b.append(p("Tóm lại, các thiết bị được xếp thành năm nhóm: nhóm an toàn "
               "nhất — thiết bị chứa chất không độc, không cháy; nhóm hai — "
               "thiết bị quá trình thông thường (bình phân tách, bơm, bộ trao "
               "đổi nhiệt); nhóm ba — thiết bị nguy hiểm như lò phản ứng và "
               "bơm trên điểm tự bốc cháy; nhóm bốn — nguy hiểm hơn như lò "
               "phản ứng nguy hiểm cao; nhóm kém an toàn nhất — thiết bị chứa "
               "nguồn kích giữ như lò gia nhiệt. Xếp hạng đầy đủ cho ISBL cho "
               "ở Bảng 23."))
    b.append(table(("Thiết bị", "Điểm I<sub>EQ</sub>"), _T23,
              "Bảng 23 · Điểm của chỉ số an toàn thiết bị I<sub>EQ</sub> cho "
              "ISBL."))

    b.append(h3("11.4.7 Chỉ số an toàn thiết bị cho OSBL",
                "11.4.7 Equipment Safety Subindex for OSBL"))

    b.append(p("Với thiết bị ngoài nhà máy, điểm <b>0–3</b> được dùng thay cho "
               "0–4 của ISBL (Heikkilä và Hurme, 1998b), vì offsite chỉ chiếm "
               "khoảng một phần ba tổng tổn thất (Instone, 1989) nên không "
               "thiết yếu bằng ISBL. Ngoài ra phần lớn rủi ro OSBL là do tồn "
               "kho lớn chất cháy hoặc độc — đã được các chỉ số tồn kho, khả "
               "cháy và độc tính xét đến — và thiết bị có lẽ an toàn hơn trong "
               "OSBL nhờ khoảng cách bố trí lớn hơn."))
    b.append(p("Thứ tự thiết bị trong khuyến nghị khoảng cách (Bảng 19) khá "
               "giống nhau: ống đốt đứng đầu; kế tiếp là tháp làm mát, lò hơi "
               "và máy nén; rồi bình chứa có áp; sau đó bình áp thấp/khí quyển "
               "và bơm chất lỏng cháy; cuối cùng là thiết bị chứa chất không "
               "cháy, không độc. Thống kê tổn thất (Bảng 21) hơi mâu thuẫn: "
               "theo Mahoney (1997), nguyên nhân chính phổ biến nhất trong hệ "
               "offsite là <b>bình chứa</b>; lò gia nhiệt và lò hơi chỉ 2% dù "
               "trong bố trí được khuyến nghị khoảng cách tương đương bồn. "
               "Vì lò hơi là nguồn kích giữ rất phổ biến (Bảng 22), việc đưa "
               "chúng vào nhóm kém an toàn nhất là hợp lý. Ống đốt không cao "
               "trong danh sách Mahoney và Instone, nhưng Planas-Cuchi và cộng "
               "sự (1997) xếp chúng quan trọng ngang lò nung và lò hơi cộng "
               "lại (Bảng 22); do đó <b>ống đốt được xếp cùng nhóm nguy hiểm "
               "với lò hơi và lò nung</b> — mọi thiết bị hoạt động như nguồn "
               "kích giữ bằng ngọn lửa (ống đốt, lò hơi, lò nung) được coi là "
               "nguy hiểm nhất và cho điểm 3, do thống kê tổn thất cao và vai "
               "trò nguồn kích giữ."))
    b.append(p("Nhóm điểm 2 gồm bồn chứa áp cao và áp thấp (p &lt; 1 barg), "
               "bồn chứa lạnh, máy nén và tháp làm mát — đều là <b>nguồn khí "
               "cháy</b> tiềm năng, đứng cao trong danh sách khoảng cách và tổn "
               "thất. Bồn chứa khí quyển chất lỏng cháy và bơm chất lỏng cháy "
               "hoặc độc ở nhóm 1 — nguồn chất lỏng cháy không tạo đám mây "
               "hơi trực tiếp. Thiết bị chứa chất không cháy, không độc thuộc "
               "nhóm an toàn nhất (điểm 0). Xem Bảng 24."))
    b.append(table(("Thiết bị", "Điểm I<sub>EQ</sub>"), _T24,
              "Bảng 24 · Điểm của chỉ số an toàn thiết bị I<sub>EQ</sub> cho "
              "OSBL."))

    # ---- 11.5 structure ------------------------------------------------------
    b.append(h3("11.5 Chỉ số cấu trúc quá trình an toàn",
                "11.5 Safe Process Structure Subindex"))

    b.append(p("<b>Cấu trúc quá trình</b> xác định những thao tác nào tham gia "
               "vào quá trình và chúng được nối với nhau ra sao. Vì vậy chỉ số "
               "cấu trúc quá trình an toàn mô tả an toàn của quá trình dưới góc "
               "nhìn kỹ thuật hệ thống: các thao tác đơn vị phối hợp với nhau "
               "tốt ra sao, nên nối và điều khiển với nhau thế nào; các hệ trợ "
               "giúp như làm mát, gia nhiệt hoặc xả áp nên cấu hình và nối vào "
               "quá trình chính ra sao. Tầm quan trọng của chỉ số này ngày "
               "càng tăng khi các quá trình ngày càng tích hợp qua mạng truyền "
               "nhiệt và truyền chất (Heikkilä và cộng sự, 1998). Chỉ số cấu "
               "trúc quá trình <b>không</b> mô tả an toàn của từng thiết bị "
               "hay tương tác qua bố trí — những khía cạnh đó thuộc chỉ số an "
               "toàn thiết bị (mục 11.4)."))

    b.append(h3("11.5.1 Đánh giá cấu trúc quá trình an toàn",
                "11.5.1 Evaluation of Safe Process Structure"))

    b.append(p("Ở giai đoạn thiết kế khái niệm, nhiều cấu hình quá trình thay "
               "thế có thể được tạo ra; khi chọn phương án khả thi nhất, an "
               "toàn nên là một tiêu chí đánh giá chính. Vì vậy cần thông tin "
               "về đặc tính an toàn của các cấu trúc quá trình thay thế ngay "
               "từ thiết kế sơ bộ. Phần lớn các chỉ số thành phần khác của ISI "
               "khá trực tiếp để ước tính vì dựa trên tính chất vật lý, hóa "
               "học; riêng chỉ số cấu trúc quá trình xét quá trình dưới góc "
               "nhìn kỹ thuật hệ thống nên <b>khó ước tính hơn nhiều</b> — "
               "thực tế không có cách ước tính tường minh mà phải dựa vào dữ "
               "liệu kinh nghiệm được lưu trong tiêu chuẩn, khuyến nghị thiết "
               "kế và báo cáo tai nạn."))

    b.append(h3("11.5.2 Nguồn thông tin an toàn dựa trên kinh nghiệm",
                "11.5.2 Sources of Experience Based Safety Information"))

    b.append(p("Các giải pháp quá trình đã bộc lộ điểm mạnh, điểm yếu, điểm "
               "an toàn và không an toàn của chúng trong thực tiễn vận hành. "
               "Kiến thức về các giải pháp này gồm chi tiết thu thập trong vận "
               "hành và bảo trì: giải pháp thực tiễn cho biết thao tác đơn vị "
               "nào thích hợp cho mục đích nào và các đơn vị có thể nối an toàn "
               "với nhau ra sao. Một phần thông tin nằm trong <b>tiêu chuẩn "
               "thiết kế</b> được xây dựng từ kinh nghiệm vận hành nhà máy hiện "
               "có (Lees, 1996)."))
    b.append(p("Nguồn thiết kế khác là <b>báo cáo tai nạn</b> — chúng cho biết "
               "những điểm yếu có thể xảy ra trong thao tác đơn vị khi dùng "
               "cho mục đích nhất định. Trong quá khứ, nhiều thao tác đơn vị "
               "đã bộc lộ đặc tính bất lợi của mình; thông tin này chủ yếu được "
               "thu thập vào báo cáo tai nạn và đưa vào tiêu chuẩn an toàn. "
               "Báo cáo tai nạn cho biết ví dụ: cấu hình thiết bị nào có tính "
               "chất bất lợi; loại hóa chất nào không hợp với thao tác đơn vị "
               "nhất định; thao tác/cấu hình nào rủi ro; khi nào việc nối các "
               "đơn vị quá trình nên tránh. Khó khăn khi sử dụng báo cáo tai "
               "nạn là <b>thiếu tiêu chuẩn báo cáo</b> — các báo cáo ghi lại "
               "chi tiết tai nạn, con đường tới sự kiện cuối, nguyên nhân và "
               "hậu quả rất khác nhau. Dù vậy, báo cáo chứa nhiều thông tin "
               "kinh nghiệm có thể — và nên — được tận dụng khi thiết kế nhà "
               "máy mới; mục tiêu lớn của việc cải thiện thiết kế an toàn nên "
               "là <b>tăng tái sử dụng kinh nghiệm thiết kế</b>, vì cùng một "
               "sai lầm được lặp đi lặp lại (Kletz, 1991)."))
    b.append(p("Dạng tinh chế hơn của báo cáo tai nạn là <b>cơ sở dữ liệu tai "
               "nạn</b>, nơi mọi báo cáo được trình bày ở định dạng chuẩn hóa; "
               "các kho dữ liệu lớn đã được thu thập (Anon, 1996). Định dạng "
               "chuẩn hóa cho phép truy hồi thông tin tai nạn dễ hơn, kể cả bằng "
               "phương tiện máy tính."))

    b.append(h3("11.5.3 Cấu trúc cơ sở dữ liệu", "11.5.3 Structure of the Database"))

    b.append(p("Nền tảng của ước tính cấu trúc quá trình an toàn là tích hợp "
               "hai nguồn thông tin: 1) <b>khuyến nghị và tiêu chuẩn</b> về "
               "cách quá trình nên được thiết kế, và 2) <b>cơ sở dữ liệu tai "
               "nạn</b> mô tả các trường hợp tiêu cực để học hỏi. Vì vậy cần "
               "một kho tình huống (casebase) các thiết kế tốt và xấu; cả hai "
               "nguồn đều nên sẵn sàng cho kỹ sư thiết kế qua cơ sở dữ liệu — "
               "một bài toán thiết kế có thể so sánh với các tình huống trong "
               "kho hợp nhất này, ví dụ bằng <b>suy luận dựa trên tình huống "
               "(CBR)</b>."))
    b.append(p("Trong cách tiếp cận này, tình huống tai nạn và khuyến nghị "
               "thiết kế được phân tích <b>từng mức một</b>. Trong cơ sở dữ "
               "liệu, kiến thức về các quá trình đã biết được chia thành các "
               "mức: <b>quá trình</b> (process) — đơn vị chế biến độc lập, ví "
               "dụ phân xưởng hiđro hóa; <b>quá trình con</b> (subprocess) — "
               "phần độc lập của quá trình như phần phản ứng hoặc phần tách; "
               "<b>hệ thống</b> (system) — phần độc lập của quá trình con, ví "
               "dụ cột chưng cất cùng mọi hệ trợ giúp; <b>hệ con</b> "
               "(subsystem) — phần chức năng của hệ thống, ví dụ hệ thu hồi "
               "nhiệt lò phản ứng hay hệ đỉnh cột gồm cả hệ điều khiển; "
               "<b>thiết bị</b> (equipment) — một thao tác đơn vị hoặc đơn vị "
               "quá trình như bộ trao đổi nhiệt, lò phản ứng, cột chưng cất; "
               "<b>chi tiết</b> (detail) — một phần tử trong đường ống hoặc "
               "thiết bị (khay trong cột, van điều khiển trong ống). Xem "
               "Hình 6."))
    b.append(fig(1, F.fig_c11_levels()))
    b.append(p("Việc tìm tình huống trong kho dữ liệu có thể thực hiện trên các "
               "mức này tùy bản chất bài toán thiết kế: nếu một quá trình được "
               "thiết kế từ đầu, tìm kiếm đầu tiên cho cả quá trình; sau đó "
               "tìm các quá trình con, hệ thống, hệ con và thiết bị liên quan. "
               "Trên cơ sở thông tin hồi về, nhà thiết kế có thể đánh giá giá "
               "trị chỉ số đúng cho cấu trúc quá trình của phần đang xét. Dữ "
               "liệu vào cho tìm kiếm chứa thông tin về mức quá trình, nguyên "
               "liệu và sản phẩm, loại phản ứng và chi tiết của nó (chất xúc "
               "tác, pha phản ứng). Đầu ra là thông tin về các cấu hình quá "
               "trình bất lợi, cấu hình được khuyến nghị và các tình huống tai "
               "nạn."))
    b.append(p("Nhà máy được chia thành vùng ISBL và OSBL; cấu hình hai vùng "
               "khác nhau đáng kể — cỡ thiết bị, lượng hóa chất và khoảng cách "
               "đều lớn hơn trong OSBL — và khía cạnh này cũng được đưa vào cơ "
               "sở dữ liệu. Cơ sở dữ liệu không phải lúc nào cũng chứa thông "
               "tin trực tiếp liên quan đến quá trình đang xét, vì vậy khả năng "
               "dùng <b>phép tương tự</b> là quan trọng: phần lớn thiết kế quá "
               "trình mới dựa vào tương tự — ví dụ các quá trình hiđro hóa có "
               "đặc điểm giống nhau, các bồn chứa khí hóa lỏng có nét tương "
               "đồng. Vì vậy cơ sở dữ liệu còn chứa thông tin về loại chất "
               "trong sự cố (ví dụ khí hóa lỏng), loại phản ứng (ví dụ oxy "
               "hóa), bản chất nhiệt của lò phản ứng (ví dụ tỏa nhiệt), pha "
               "phản ứng và loại chất xúc tác."))
    b.append(p("Để học từ các tình huống tai nạn, điều thiết yếu là chỉ ra "
               "<b>loại sự cố</b> đã xảy ra (ví dụ nổ), <b>nguyên nhân trực "
               "tiếp</b> (ví dụ điện tĩnh), <b>lý do</b> điều này có thể xảy ra "
               "(ví dụ đổ đầy qua pha khí) và cuối cùng — quan trọng nhất — "
               "<b>bài học</b> tránh được điều này (ví dụ đổ đầy bồn qua đáy)."))

    b.append(h3("11.5.4 Chỉ số an toàn nội tại của cấu trúc quá trình an toàn",
                "11.5.4 Inherent Safety Index of Safe Process Structure"))

    b.append(p("Cấu trúc quá trình được chia thành <b>sáu nhóm điểm từ 0 đến "
               "5</b> theo hiểu biết về hành vi an toàn của chúng trong vận "
               "hành. Nhóm một, an toàn nhất (điểm 0), gồm các giải pháp quá "
               "trình và thiết bị được khuyến nghị và chuẩn hóa. Nhóm hai dựa "
               "trên thực hành kỹ thuật tốt — dùng các phương án quá trình đã "
               "biết và tin cậy. Nhóm ba gồm các quá trình trung tính hoặc "
               "chưa có dữ liệu an toàn. Nhóm bốn gồm các cấu hình có lẽ đáng "
               "nghi ngờ về an toàn dù tai nạn chưa xảy ra. Nhóm năm và sáu "
               "gồm các trường hợp quá trình đã có <b>tai nạn nhỏ hoặc tai "
               "nạn lớn được ghi nhận</b>. Điểm cuối của chỉ số được chọn theo "
               "<b>trường hợp xấu nhất</b> giữa các mức của suy luận; kết quả "
               "được dùng cùng các chỉ số thành phần khác để ước tính an toàn "
               "nội tại tổng thể của các phương án quá trình, phục vụ lựa chọn "
               "khái niệm quá trình hoặc chi tiết cấu hình. Chi tiết về chỉ số "
               "cấu trúc quá trình an toàn cho ở Heikkilä và cộng sự (1998)."))
    b.append(table(("Mức an toàn của cấu trúc quá trình",
                    "Điểm I<sub>ST</sub>"), _T25,
              "Bảng 25 · Giá trị của chỉ số cấu trúc quá trình an toàn "
              "I<sub>ST</sub>."))

    b.append(note("Tổng điểm tối đa của các chỉ số quá trình theo Bảng 15–25 "
                  "tạo thành I<sub>PI</sub> theo Phương trình 5 (Chương 8): "
                  "I<sub>I</sub> (5) + I<sub>T</sub> (4) + I<sub>p</sub> (4) "
                  "+ I<sub>EQ</sub> (4) + I<sub>ST</sub> (5), tối đa 22 điểm; "
                  "với OSBL, I<sub>EQ</sub> tối đa 3."))

    return "".join(b)


def body_en():
    b = []

    b.append(h2("11. Subindices for Process Inherent Safety Index",
                "11. Các chỉ số thành phần của chỉ số an toàn nội tại quá trình"))

    b.append(p("The Process Inherent Safety Index expresses the inherent safety "
               "of <b>the process itself</b>, including the equipment and the "
               "operating parameters. The Index has been divided into "
               "subindices for inventory, temperature, pressure, equipment "
               "safety and safe process structure."))

    # ---- 11.1 inventory ------------------------------------------------------
    b.append(h3("11.1 Inventory Subindex", "11.1 Chỉ số tồn kho"))

    b.append(p("An exact calculation of inventory is difficult in the "
               "conceptual-design phase, since the size of equipment is not "
               "usually known. The <b>mass flows</b> in the process are, "
               "however, known from the design capacity. Therefore it is "
               "practical to base the estimation of inventory on mass flows "
               "and an estimated residence time: inventory is included in the "
               "ISI as a mass flow in the ISBL equipment (including recycles) "
               "with a <b>one-hour nominal residence time for each process "
               "vessel</b> (reactor, distillation column, etc.). For large "
               "storage tanks the size should be estimated. The total inventory "
               "is the sum of the inventories of all process vessels."))

    b.append(p("In the OSBL area the tank sizes are normally not known in "
               "conceptual design, which means that the OSBL inventory cannot "
               "readily be calculated — it depends not only on the ISBL "
               "process type but also on local conditions, logistics, etc. For "
               "the OSBL inventory, values based on the Mond Index (ICI, 1985) "
               "were used. These were also used for ISBL by Edwards et al. "
               "(1993), but the experts criticized this, since the relevant "
               "inventory scale in ISBL is much smaller; also, due to a "
               "tighter layout, the same inventory in ISBL is more dangerous "
               "than in OSBL. Therefore a new scale was developed by scaling "
               "the Mond values using the expert recommendations in Lawrence's "
               "work (1996) — see Table 15."))
    b.append(table(("ISBL inventory", "OSBL inventory", "Score of I<sub>I</sub>"),
              _T15, "Table 15 · Determination of the inventory subindex I<sub>I</sub>."))

    # ---- 11.2 temperature ----------------------------------------------------
    b.append(h3("11.2 Process Temperature Subindex",
                "11.2 Chỉ số nhiệt độ quá trình"))

    b.append(p("Temperature is an indicator of the heat energy in the system. "
               "The hazard increases at higher temperatures because of the "
               "energy content itself and also because <b>the strength of "
               "materials becomes weaker at high or very low temperatures</b>. "
               "Great temperature changes between ambient (shutdown) and "
               "operating temperatures also cause thermal stress, which may "
               "increase the hazard of a loss of containment."))
    b.append(p("Process temperature in the ISI is determined on the basis of "
               "the <b>maximum temperature</b> in the process area under "
               "investigation — feasible, since preliminary estimates of "
               "temperatures and pressures are available in the early stage of "
               "process design. Because the hazards in the low-temperature "
               "range increase due to mechanical problems and freezing if water "
               "is present, temperatures below 0 °C are also included in the "
               "index. When there are many temperature levels in the area "
               "under study, <b>the highest temperature subindex value</b> is "
               "applied. The temperature ranges have been chosen on the basis "
               "of the danger to humans and of material strength as a function "
               "of temperature: 0–70 °C is harmless to people in general; "
               "70–150 °C is the typical range of mild-temperature processes; "
               "the next limit is 300 °C, beyond which the strength of carbon "
               "steel is decreased considerably compared to room temperature; "
               "higher temperatures require materials with better heat "
               "resistance. Subzero temperatures cause problems as explained "
               "in Section 7.6."))
    b.append(table(("Process temperature", "Score of I<sub>T</sub>"), _T16,
              "Table 16 · Determination of the process temperature subindex "
              "I<sub>T</sub>."))

    # ---- 11.3 pressure -------------------------------------------------------
    b.append(h3("11.3 Process Pressure Subindex",
                "11.3 Chỉ số áp suất quá trình"))

    b.append(p("Pressure is an indicator of <b>potential energy</b> which "
               "affects the leak rates in the case of loss of containment. "
               "Higher pressures also pose stricter requirements on vessel "
               "strength. Leaks in vacuum equipment may cause inlet of air and "
               "a consequent explosion. In the ISI the process pressure is "
               "determined on the basis of the <b>maximum pressure in the "
               "process area under normal operation</b>; the pressure limits "
               "in Table 17 are based on the Dow F&amp;E Index (Dow, 1987)."))
    b.append(table(("Process pressure", "Score of I<sub>p</sub>"), _T17_EN,
              "Table 17 · Determination of the process pressure subindex "
              "I<sub>p</sub>."))

    # ---- 11.4 equipment ------------------------------------------------------
    b.append(h3("11.4 Equipment Safety Subindex", "11.4 Chỉ số an toàn thiết bị"))

    b.append(p("The Equipment Safety Subindex has been included in the ISI to "
               "get a better view of total inherent safety by discussing also "
               "the <b>selection and type of equipment</b> used (Heikkilä and "
               "Hurme, 1998a and 1998b). Equipment safety tries to measure the "
               "possibility that a piece of equipment is unsafe. Here equipment "
               "includes all major pieces such as pumps and vessels, but not "
               "piping, valves or instruments — these have not been designed "
               "yet in the early design stages. The equipment safety index "
               "considers the safety of the equipment as such, without "
               "interactions through the process with other equipment — this "
               "latter aspect is described by the safe process structure "
               "subindex. However, interactions through layout, such as a "
               "furnace being a source of ignition for a leak from another "
               "piece of equipment, are considered by the equipment safety "
               "index."))
    b.append(p("The main failure of equipment is a <b>loss of process "
               "containment</b>. The consequences depend on the properties and "
               "the amount of the leaking material and the conditions inside "
               "and outside the equipment. Pumps and compressors (Marshall, "
               "1987) are perhaps the most vulnerable items of pressurised "
               "systems: they contain moving parts and are subject to erosion "
               "and cavitation; they also produce vibration which may lead to "
               "fatigue failure. Both seals and bearings are liable to fail. "
               "Agitator systems present difficulties due to mechanical "
               "stresses, though they operate at much lower speeds than "
               "pumps."))

    b.append(h3("11.4.1 Evaluation of Equipment Safety",
                "11.4.1 Đánh giá an toàn thiết bị"))

    b.append(p("The comparison of the safety of equipment is not "
               "straightforward: it depends on the equipment themselves and on "
               "the process conditions. Equipment safety can be evaluated from "
               "<b>quantitative accident and failure data</b> and from "
               "<b>engineering practice and recommendations</b>. "
               "Experience-based information is found in layout recommendations "
               "and safety analysis methods such as the Dow F&amp;E Index "
               "(1987); quantitative data in accident and operational "
               "statistics. It should be remembered that <b>not all reliability "
               "or failure information expresses safety directly</b>: not all "
               "failures are dangerous and not all accidents are due to "
               "equipment failures."))
    b.append(p("For the Equipment Safety Subindex the process plant area is "
               "divided into two areas with different safety properties. The "
               "<b>ISBL</b> area is where the raw materials are converted into "
               "products — characterised by a large number of equipment and "
               "piping located in a concentrated way in a small area. The rest "
               "of the plant is the <b>OSBL</b> area — characterised by large "
               "inventories of fluids, which are often flammable and/or toxic; "
               "the number of equipment items is smaller but their size larger, "
               "and the layout is much more scattered, to enhance safety."))

    b.append(h3("11.4.2 Equipment Layout", "11.4.2 Bố trí thiết bị"))

    b.append(p("During plant design the safety of process equipment is also "
               "recognised by <b>layout</b>: the objectives are to minimise "
               "risk to personnel, to minimise escalation (both within the "
               "plant and to adjacent plants), and to ensure adequate "
               "emergency access, as well as access for maintenance and "
               "operations. Safe plant layout is designed on the basis of "
               "design standards and local regulations, often expressed as "
               "minimum clearances between equipment. Safety distances can in "
               "principle be calculated by estimating the size of possible "
               "leaks, the probability of ignition and explosion and their "
               "effects; since this approach is full of difficulties, "
               "<b>experience-based minimum distances</b> are used instead "
               "(Wells, 1980). Even though process layouts are not available "
               "in preliminary design, the spacing recommendations give an "
               "idea of the risk of certain pieces of equipment to their "
               "environment."))
    b.append(p("Layout spacings are also affected by other factors than "
               "safety: the space requirements of maintenance, repair works "
               "and proper performing of process operations; enough room for "
               "pipes, supports and foundations. The spacing recommendations "
               "have been presented in the literature as matrices and lists of "
               "typical minimum distances. In this work the equipment spacing "
               "matrices of Industrial Risk Insurers (1991), Bausbacher and "
               "Hunt (1993), Prugh (1982), Mecklenburgh (1985) and the Institut "
               "Français du Petrole have been compared. A suitable distance to "
               "another process item depends mostly on the safety properties "
               "of the process items; clearances required for maintenance and "
               "access are usually shorter than safety clearances. Therefore it "
               "was assumed that <b>the average of the recommended equipment "
               "spacings</b> is mostly related to the general unsafety of a "
               "specific process item, not to maintenance aspects."))
    b.append(p("The evaluation of the layout spacing data was done by "
               "calculating <b>the averages of the recommended spacings</b>; "
               "where operational and maintenance-access spacings were not "
               "included in some matrices, a minimum distance of one metre was "
               "used. It was noticed that the order of the process items "
               "according to their average spacing requirements is <b>almost "
               "identical in all referred matrices</b>: for ISBL layout "
               "(Table 18), furnaces, compressors and high-hazard reactors "
               "were at the top of the lists, while equipment handling "
               "nonflammable and nontoxic materials was at the other end. The "
               "former needed extra spacing for safety; the latter required "
               "only enough room for operation, repair and maintenance. The "
               "exception is the higher ranking of towers in the matrix of "
               "Industrial Risk Insurers (1991) — probably because of the "
               "large inventory of material, which leads to large economical "
               "losses in a case of rupture."))
    b.append(table(("Equipment items", "Prugh (1982)",
                    "Bausbacher and Hunt (1993)",
                    "Industrial Risk Insurers (1991)",
                    "Institut Français du Petrole"), _T18,
              "Table 18 · Comparison of the average spacing recommendations for "
              "some ISBL process items (metres). * high hazard = handling "
              "materials above their autoignition point; a dash marks values "
              "not printed in the source."))
    b.append(p("The calculated average spacing recommendations for OSBL "
               "equipment (Table 19) show that the order of the process items "
               "is <b>quite similar in all matrices</b>. Flares are given "
               "clearly the largest spacing recommendations — the aim of the "
               "long distances is to prevent ignition or other damage caused "
               "by heat radiation and the possible dropout of burning liquid; "
               "any releases of flammable vapour from other parts of the site "
               "should disperse to below their lower flammable limit before "
               "reaching the flare."))
    b.append(table(("Equipment items", "Bausbacher and Hunt (1993)",
                    "Prugh (1982)", "Mecklenburgh (1985)"), _T19,
              "Table 19 · Comparison of the average spacing recommendations for "
              "some OSBL items (metres). A dash marks values not printed in "
              "the source."))
    b.append(p("Cooling towers have large spacings around them: if the release "
               "of flammable materials into the cooling water and then into "
               "the atmosphere is possible, <b>there must not be any ignition "
               "sources near the tower</b>; cooling towers produce large "
               "volumes of wet air, which can cause fog, precipitation, "
               "freezing and corrosion downwind, and they require water basins "
               "and substantial foundations. Other utility systems have wide "
               "recommendations too: boilers have flame and hot surfaces which "
               "can act as ignition sources; large distances are often "
               "recommended for compressors to separate possible leaks from "
               "ignition sources — compressors also cause considerable "
               "vibration, which may cause leaks in piping, and need clear "
               "space around them to be maintained and operated properly."))
    b.append(p("Storage vessels are usually located on tank farms. The space "
               "around a tank and the distances to other equipment depend on "
               "the <b>materials stored, their potential hazardousness and the "
               "possibility of unexpected changes in storage conditions</b>. "
               "Fluid storages should be in a safe location away from process "
               "and public areas; it is also important to prevent fire "
               "spreading between tanks by keeping the heat radiation at an "
               "acceptable level (Mecklenburgh, 1985). Storage vessels may be "
               "atmospheric or pressurised, fixed- or floating-roof tanks, or "
               "low/high-temperature tanks; the spacing recommendations are "
               "given for each vessel type separately, according to the phase "
               "of the fluid, storage pressure and flash points (Table 19). "
               "Pumps may also handle fluids below or above their flash or "
               "autoignition points — recognised by general layout "
               "recommendations too."))

    b.append(h3("11.4.3 Equipment Involved in Large Losses",
                "11.4.3 Thiết bị trong các tổn thất lớn"))

    b.append(p("Mahoney (1997) has analysed the <b>170 largest losses</b> in "
               "refineries, petrochemical plants and gas processing plants "
               "from 1966 to 1996: nearly all the losses involved fires or "
               "explosions, and the most common primary cause of losses was "
               "<b>piping</b>. Instone (1989) analysed some 2000 large-loss "
               "claims of the hydrocarbon industry at Cigna Insurance. Table "
               "20 lists the ISBL equipment and Table 21 the OSBL data by "
               "Mahoney (1992, 1997) and Instone (1989)."))
    b.append(table(("Types of equipment", "Percent of losses (Mahoney, 1992)",
                    "Average dollar loss (millions $, Mahoney, 1992)",
                    "Proportion of losses (Instone, 1989)"), _T20,
              "Table 20 · Some ISBL equipment involved in large losses."))
    b.append(p("In Table 20, <b>reactors</b> were involved in 13% of incidents "
               "(Mahoney, 1992) and produced the highest average loss, because "
               "an explosion-damaged reactor spreads devastation over a large "
               "area. <b>Process towers</b> were involved in only 4% of "
               "incidents, but produced the second highest average loss: few "
               "accidents, but great economical losses due to the large "
               "inventories involved. Heaters and boilers caused only 2% of "
               "incidents with the lowest average loss; however, in many cases "
               "they have probably been <b>secondary causes of failure</b> as "
               "ignition sources — which is not taken into account in "
               "Mahoney's data."))
    b.append(p("By Instone (1989), the process unit types most often involved "
               "in large losses seem to be <b>furnaces or boilers (15%)</b>, "
               "whereas reactors and process drums seem quite rarely involved "
               "(3% each) — the major difference from Mahoney's data. A "
               "possible reason is that Instone analysed the process units "
               "<b>involved</b> in large losses and Mahoney the <b>primary "
               "causes</b> of large losses."))
    b.append(table(("Types of equipment", "Percent of losses (Mahoney, 1997)",
                    "Average dollar loss (millions $, Mahoney, 1997)",
                    "Proportion of losses (Instone, 1989)"), _T21,
              "Table 21 · Some OSBL equipment involved in large losses. "
              "* include both OSBL and ISBL."))
    b.append(p("In Mahoney's data (1997) for OSBL, <b>tanks</b> in general "
               "have been involved in 15% of accidents; the large inventories "
               "and high replacement costs of tanks with their accessories "
               "lead to expensive consequences. <b>Pumps and compressors</b> "
               "were involved in 8% of incidents but produced the highest "
               "average loss — due to the high replacement costs of compressors "
               "and their electrical installations; pumps are often located "
               "nearby each other, so an accident destroys several pumps with "
               "their electrifications at the same time. Heaters and boilers "
               "were involved in only 2% of incidents with the lowest average "
               "loss. In Instone's data (1989) the OSBL equipment most often "
               "involved seems to be <b>storage tanks (14%)</b>; heaters and "
               "furnaces are mentioned in 15% of incidents; pumps, compressors "
               "and boilers are involved equally (5% each); flares, cooling "
               "towers and API separators are quite rarely involved (&lt;1% "
               "each). The differences concerning fired heaters and boilers "
               "again stem from the primary-cause vs involvement perspectives "
               "— heaters and boilers are the most common ignition sources "
               "(Table 22) and are therefore probably considered secondary "
               "causes by Mahoney."))
    b.append(table(("Ignition sources", "% of ignitions (Instone, 1989)",
                    "% of known ignitions (Planas-Cuchi et al., 1997)",
                    "% of known ignitions (Fire Protection Association, 1974)"),
              _T22, "Table 22 · Some sources of ignition."))

    b.append(h3("11.4.4 Equipment in Other Indices",
                "11.4.4 Thiết bị trong các chỉ số khác"))

    b.append(p("A frequently used safety index in the process industry is the "
               "Dow Fire &amp; Explosion Hazard Index (1987). The Dow F&amp;E "
               "Index gives <b>penalties</b> for fired equipment and certain "
               "specified rotating equipment — part of the Special Process "
               "Hazards, within which the penalties of a process unit are "
               "summed. Fired equipment receives penalties if the material in "
               "the process unit near the air intake of the fired heater could "
               "be released above its boiling point, is a combustible dust, or "
               "could be released above its boiling point; the penalty depends "
               "on the distance from the possible leak source and varies "
               "between 0.1 and 1.0 — e.g. a distance of 15 m gives penalties "
               "of 0.27 (above the flash point) and 0.60 (above the boiling "
               "point). Any situation involving a material processed below its "
               "flash point receives no penalty."))
    b.append(p("Large rotating equipment — 1) compressors in excess of 450 kW, "
               "2) pumps in excess of 56 kW, 3) agitators and circulating "
               "pumps in which failure could produce a process exotherm, and "
               "4) other large, high-speed rotating equipment with a "
               "significant loss history, e.g. centrifuges — all have a "
               "constant penalty of 0.5. The scale of penalties is <b>much "
               "narrower</b> than the scale of recommended layout spacings or "
               "the cost of large losses, because the Dow F&amp;E Index takes "
               "into account only large rotating equipment — known to be more "
               "likely to contribute to accidents than smaller equipment, "
               "which is safer and receives no penalties."))

    b.append(h3("11.4.5 Equipment Failures and Their Evaluation",
                "11.4.5 Hỏng hóc thiết bị và đánh giá"))

    b.append(p("There is a certain amount of statistical information available "
               "on the failures of process system components. Arulanantham and "
               "Lees (1981) studied pressure-vessel failures in process plants "
               "such as olefins plants: failure is defined as a condition in "
               "which a crack, leak or other defect has developed to the "
               "extent that repair or replacement is required — a definition "
               "which includes some potentially dangerous as well as all "
               "catastrophic failures. In olefins plants, <b>fired heaters "
               "have failure rates of about 0.4 failures/year</b>, process "
               "pressure vessels 0.0025 failures/year and heat exchangers "
               "0.0015 failures/year — fired heaters are much unsafer than "
               "process pressure vessels."))
    b.append(p("In the Canvey study (King, 1990; Health and Safety Executive, "
               "1978) of the potential hazards to the public from the "
               "industrial activities in the Canvey Island/Thurrock area of "
               "Essex, pressure vessels had a <b>ten times bigger</b> assumed "
               "frequency of catastrophic failures than LPG pumps. Crawley and "
               "Grant (1997) developed a risk assessment tool for new offshore "
               "installations: they examined typical leak frequencies of "
               "equipment items and the ignition probability of these leaks in "
               "four pressure bands, making it possible to define leak size "
               "and frequency for any piece of equipment and the ignited leak "
               "frequency. In offshore installations, gas separation vessels "
               "were found to have a <b>ten times higher</b> ignited event "
               "frequency than oil pumps."))

    b.append(h3("11.4.6 Equipment Safety Subindex for ISBL",
                "11.4.6 Chỉ số an toàn thiết bị cho ISBL"))

    b.append(p("From the data discussed above: the order of process items in "
               "the layout spacing recommendations is almost identical — "
               "furnaces and fired heaters at the top (Table 18); the next "
               "group is formed by compressors and high-hazard reactors; air "
               "coolers, ordinary reactors and high-hazard pumps appear next; "
               "after that come towers, process drums, heat exchangers and "
               "pumps; the last and safest group is formed of equipment "
               "handling nonflammable and nontoxic materials. The only "
               "discrepancy is the higher ranking of towers and drums in the "
               "Industrial Risk Insurers (1991) data — probably because of the "
               "large inventory of flammables; since inventory is considered "
               "separately by the inventory subindex, the vessels may best be "
               "included in the same group as heat exchangers and pumps."))
    b.append(p("Accident statistics on the equipment involved in large losses "
               "give somewhat contradictory information (Table 20): according "
               "to Mahoney (1992), the most common primary accident cause is "
               "the <b>reactor</b>, next are process drums, whereas heaters "
               "are among the safest; this contrasts with Instone's (1989) "
               "data, where heaters and boilers were the most common process "
               "items in accidents. Since furnaces are sources of ignition for "
               "flammable leaks from other equipment, they are not necessarily "
               "listed as primary causes even though they are probably "
               "involved as secondary causes in many losses. Therefore the "
               "inclusion of both reactors and furnaces in the list of the "
               "most unsafe equipment is well justified."))
    b.append(p("We have ranked <b>furnaces unsafer (score 4) than reactors "
               "(score 3 or 2)</b>, since fired heaters are the most common "
               "ignition sources (Instone, 1989) for any leaks; Instone also "
               "lists furnaces as the most commonly involved process items in "
               "losses; the Dow F&amp;E Index (1987) can give higher penalties "
               "for furnaces than for reactors (cooling systems and agitators) "
               "or large compressors; and Arulanantham and Lees (1981) give "
               "very high mechanical failure rates to olefin-plant fired "
               "heaters. <b>Compressors</b> are ranked very unsafe because "
               "they are referred to as very vulnerable process items "
               "(Marshall, 1987): they contain moving parts, are subject to "
               "vibration and can release flammable gas in a case of failure; "
               "they are also very high in the layout list. For <b>process "
               "drums, towers, heat exchangers and pumps</b> (below "
               "autoignition), Mahoney (1997) and Instone (1989) give similar "
               "low loss statistics and Arulanantham and Lees (1981) roughly "
               "the same mechanical failure rates — from this and the layout "
               "data, they can be grouped together as one single low score "
               "level (score 1)."))
    b.append(p("To summarize: the process items were arranged into five groups "
               "— the safest group is the equipment handling nontoxic and "
               "nonflammable material; the second group contains common "
               "process items such as process drums, pumps and heat "
               "exchangers; the third group hazardous equipment such as "
               "reactors and pumps above autoignition; the fourth group more "
               "hazardous items such as high-hazard reactors; the most unsafe "
               "group is the equipment containing ignition sources such as "
               "fired heaters. The full compilation of the equipment ranking "
               "for ISBL is given in Table 23."))
    b.append(table(("Equipment items", "Score of I<sub>EQ</sub>"), _T23,
              "Table 23 · The scores of the Equipment Safety Subindex "
              "I<sub>EQ</sub> for ISBL."))

    b.append(h3("11.4.7 Equipment Safety Subindex for OSBL",
                "11.4.7 Chỉ số an toàn thiết bị cho OSBL"))

    b.append(p("For offsite equipment the scores <b>0–3</b> have been used "
               "instead of the 0–4 of ISBL (Heikkilä and Hurme, 1998b), since "
               "the offsites represent only one third of all losses (Instone, "
               "1989) and are therefore not as essential as ISBL. Also, much "
               "of the OSBL risk is due to the large inventory of flammable "
               "or toxic chemicals — discussed by the inventory, flammability "
               "and toxicity subindices — and equipment is probably safer in "
               "OSBL than in ISBL because of the larger layout spacings."))
    b.append(p("The order of process items in the layout spacing "
               "recommendations (Table 19) is quite similar: flares are at the "
               "top of the list; the next unsafe are cooling towers, boilers "
               "and compressors; pressure storage tanks appear next; after "
               "that come low-pressure and atmospheric storage tanks and pumps "
               "of flammable liquids; the last and safest group is formed of "
               "equipment handling nonflammable and nontoxic materials. "
               "Accident statistics (Table 21) give somewhat contradictory "
               "information: according to Mahoney (1997), the most common "
               "primary accident cause within offsite systems is the "
               "<b>tank</b>; fired heaters and boilers represent only 2% of "
               "losses, while in layout they are recommended about the same "
               "spacings as tanks. Since heaters and boilers are very common "
               "sources of ignition (Table 22), their inclusion in the list of "
               "the most unsafe equipment is well justified. Flares are not "
               "high in the lists of Mahoney (1997) and Instone (1989); "
               "however, Planas-Cuchi et al. (1997) list them as equally "
               "important as furnaces and boilers together as ignition sources "
               "(Table 22). From this it has been concluded that <b>flares "
               "should be included in the same equipment hazard group with "
               "boilers and furnaces</b> — all equipment which acts as a "
               "source of ignition through flame (furnaces, boilers, flares) "
               "is considered the most dangerous and given score 3, due to the "
               "high loss statistics (Instone, 1989, Table 21) and their "
               "function as ignition sources (Table 22)."))
    b.append(p("The next index group (score 2) contains high- and low-pressure "
               "(p &lt; 1 barg) tanks, refrigerated storage tanks, compressors "
               "and cooling towers — all of which represent a <b>source of "
               "flammable gas</b> and are located high in the layout-spacing "
               "and large-loss lists. Atmospheric storage tanks of flammable "
               "liquids and pumps of flammable or toxic liquids belong to "
               "group 1 — sources of flammable liquid which do not produce a "
               "vapour cloud directly. Equipment handling nonflammable and "
               "nontoxic material belongs to the safest group (score 0). See "
               "Table 24."))
    b.append(table(("Equipment items", "Score of I<sub>EQ</sub>"), _T24,
              "Table 24 · The scores of the Equipment Safety Index "
              "I<sub>EQ</sub> for OSBL."))

    # ---- 11.5 structure ------------------------------------------------------
    b.append(h3("11.5 Safe Process Structure Subindex",
                "11.5 Chỉ số cấu trúc quá trình an toàn"))

    b.append(p("A <b>process structure</b> defines which operations are "
               "involved in the process and how they are connected together. "
               "Therefore the Safe Process Structure Subindex describes the "
               "safety of the process from a systems-engineering point of "
               "view: how well certain unit operations or other process items "
               "work together, how they should be connected and controlled "
               "together; also how auxiliary systems such as cooling, heating "
               "or relief systems should be configured and connected to the "
               "main process. The importance of this subindex is increasing as "
               "the processes become more integrated through heat and "
               "mass-transfer networks (Heikkilä et al., 1998). The Process "
               "Structure Subindex does <b>not</b> describe the safety of the "
               "process items as such or their interaction through the "
               "non-process route (i.e. through layout) — this is described by "
               "the Equipment Safety Subindex (Section 11.4)."))

    b.append(h3("11.5.1 Evaluation of Safe Process Structure",
                "11.5.1 Đánh giá cấu trúc quá trình an toàn"))

    b.append(p("Many different alternative process configurations can be "
               "created for a process in the conceptual design phase; in "
               "choosing the most feasible alternative, safety should be one "
               "of the major evaluation criteria. Therefore information on the "
               "safety features of alternative process structures is needed in "
               "preliminary process design. Most of the other subindices of "
               "the ISI are quite straightforward to estimate, since they are "
               "based e.g. on the physical and chemical properties of the "
               "compounds present. The process structure subindex looks at the "
               "process from a systems-engineering point of view and is "
               "<b>much more difficult to estimate</b>: in fact there is no "
               "explicit way of estimating the safety of the process structure, "
               "and one has to rely on experience-based data documented as "
               "standards, design recommendations and accident reports."))

    b.append(h3("11.5.2 Sources of Experience Based Safety Information",
                "11.5.2 Nguồn thông tin an toàn dựa trên kinh nghiệm"))

    b.append(p("Process solutions have shown their strong and weak, safe and "
               "unsafe points in operation practice. The knowledge of "
               "practised solutions consists of the details collected during "
               "operation and maintenance: practised solutions reveal, for "
               "instance, which unit operations are preferable for certain "
               "purposes and how the units can be connected safely together. "
               "Some of the information can also be found in <b>design "
               "standards</b> created on the basis of the operating experience "
               "of existing process plants (Lees, 1996)."))
    b.append(p("Another source of design information is the <b>accident "
               "reports</b> made after an accident. They give valuable "
               "information on the possible weaknesses that can occur in unit "
               "operations when used for certain purposes. In the past many "
               "unit operations have shown their adverse characteristics; this "
               "information is mainly collected into accident reports and "
               "included in safety standards. Accident reports tell us, for "
               "example: which process equipment configurations have "
               "unfavourable properties; which types of chemicals do not suit "
               "certain unit operations; which unit operations/configurations "
               "are risky; when the connection of process units should be "
               "avoided. The difficulty in utilizing accident reports lies in "
               "the <b>lack of accident-report standards</b> — the reports "
               "vary a lot in how they document the details of the accident, "
               "the path to the final event, the causes and the consequences. "
               "Still, the reports can tell much experience-based information "
               "which can — and should — be utilized in designing new plants. "
               "In fact, a major goal in improving the design of safe process "
               "plants should be to <b>enhance the reuse of design "
               "experience</b>: the same mistakes are done again and again "
               "(Kletz, 1991)."))
    b.append(p("A more refined form of the accident report is an <b>accident "
               "database</b>, where all the reports are presented in a "
               "standardized format; extensive databanks have already been "
               "collected from accident reports (Anon, 1996). Such a "
               "standardized format allows easier retrieval of accident "
               "information, also by computerized means."))

    b.append(h3("11.5.3 Structure of the Database",
                "11.5.3 Cấu trúc cơ sở dữ liệu"))

    b.append(p("The basis for the estimation of safe process structure lies in "
               "the integration of two types of information sources: "
               "1) <b>recommendations and standards</b> on how the process "
               "should be designed, and 2) an <b>accident database</b> "
               "describing the negative cases from which one can learn. "
               "Therefore a casebase of good and bad design cases is needed; "
               "both sources should be readily available to the design "
               "engineer through the database. A design problem can be "
               "compared with the cases in this combined databank, for "
               "instance by <b>case-based reasoning (CBR)</b>."))
    b.append(p("In this approach, accident cases and design recommendations "
               "can be analysed <b>level by level</b>. In the database the "
               "knowledge of known processes is divided into categories: "
               "<b>process</b> — an independent processing unit (e.g. a "
               "hydrogenation unit); <b>subprocess</b> — an independent part "
               "of a process, such as a reactor or separation section; "
               "<b>system</b> — an independent part of a subprocess, such as a "
               "distillation column with all its auxiliary systems; "
               "<b>subsystem</b> — a functional part of a system, such as a "
               "reactor heat-recovery system or a column overhead system "
               "including its control systems; <b>equipment</b> — a unit "
               "operation or unit process such as a heat exchanger, a reactor "
               "or a distillation column; <b>detail</b> — an item in a pipe or "
               "a piece of equipment (a tray in a column, a control valve in a "
               "pipe). See Figure 6."))
    b.append(fig(1, F.fig_c11_levels()))
    b.append(p("A search for cases in the databank can be made on these levels "
               "according to the nature of the design problem: if a process is "
               "being designed from the beginning, the first search is made "
               "for a whole process; the search is then made for those "
               "subprocesses, systems, subsystems and equipment which are "
               "relevant for the design. On the basis of the retrieved "
               "information the designer can evaluate the right index value "
               "for the process structure of the section under review. The "
               "input data for a database search contains information on the "
               "process level and on the raw materials and products, reaction "
               "types and their details such as catalysts and the phase of the "
               "reaction. As output there is information about unfavourable "
               "process configurations, recommended configurations and "
               "accident cases."))
    b.append(p("A plant is divided into inside and offsite battery-limit "
               "areas; the configurations of ISBL and OSBL areas differ "
               "considerably — generally the size of equipment, the amount of "
               "chemicals and the spacings are larger in the OSBL area — and "
               "this aspect is included in the database as well. The database "
               "does not always contain information directly related to the "
               "process under review; therefore it is important to be able to "
               "use <b>analogies</b>: in general, much of the design of new "
               "processes relies on analogies — most hydrogenation processes "
               "have similar features, most tanks of liquefied gases have "
               "similarities, etc. For that reason the database also includes "
               "information on the type of material in the incident (e.g. "
               "liquefied gas), the type of reaction (e.g. oxidation), the "
               "thermal nature of the reactor (e.g. exothermic), the phase of "
               "the reaction and the type of catalyst."))
    b.append(p("To learn from the accident cases it is essential to indicate "
               "the <b>type of incident</b> which happened (e.g. explosion), "
               "the <b>direct cause</b> of the incident (e.g. static "
               "electricity), the <b>reason</b> why this could take place "
               "(e.g. filling through the gas phase) and finally — most "
               "important — the <b>lesson</b> of how this can be avoided (e.g. "
               "fill the tank through the bottom)."))

    b.append(h3("11.5.4 Inherent Safety Index of Safe Process Structure",
                "11.5.4 Chỉ số an toàn nội tại của cấu trúc quá trình an toàn"))

    b.append(p("Process structures are divided into <b>six groups of scores "
               "from 0 to 5</b> according to the knowledge of their safety "
               "behaviour in operation. The first group is the safest (score "
               "0): recommended and standardized process and equipment "
               "solutions. The second group is based on sound engineering "
               "practice — the use of well-known and reliable process "
               "alternatives. The third group contains processes which look "
               "neutral, or on which no safety data is available. The fourth "
               "group includes configurations which are probably questionable "
               "on the basis of safety, even though accidents have not yet "
               "occurred. The fifth and sixth groups contain process cases on "
               "which documented <b>minor or major accident cases</b> exist, "
               "respectively. The final score of the subindex is chosen on the "
               "basis of the <b>worst case</b> of the different levels of the "
               "reasoning. The results can be used with the other subindices "
               "for estimating the total inherent safety of process "
               "alternatives, for the selection of the process concept or the "
               "details of the process configuration. Details of the Safe "
               "Process Structure Subindex are given by Heikkilä et al. "
               "(1998)."))
    b.append(table(("Safety level of process structure", "Score of I<sub>ST</sub>"),
              _T25_EN, "Table 25 · Values of the Safe Process Structure "
              "Subindex I<sub>ST</sub>."))

    b.append(note("The process subindex scores of Tables 15–25 assemble into "
                  "I<sub>PI</sub> per Equation 5 (Chapter 8): I<sub>I</sub> (5) "
                  "+ I<sub>T</sub> (4) + I<sub>p</sub> (4) + I<sub>EQ</sub> (4) "
                  "+ I<sub>ST</sub> (5), with a maximum of 22 points; for "
                  "OSBL, I<sub>EQ</sub> max 3."))

    return "".join(b)
