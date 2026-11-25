# -*- coding: utf-8 -*-
"""Book 7, Chapter 19 - The Graphical ABC Method for Gases (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
121-123 (PDF pp. 123-125). Three printed pages, three vector redraws of Graphs
A, B and C, one pipe-schedule modifier table and one worked example. The source
contains no numbered equations; the printed forms are carried as unnumbered
equation markup. The OCR text layer garbles the mathematical symbols, so the
expressions and the table were checked against page renders of all three pages.
"""
from cvp_common import eq, fig, h2, h3, note, p, table
import cvpfig19 as F

PAGES_SRC = 3
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "The Graphical ABC Method for Gases"
TITLE_VI = "Phương pháp ABC dạng đồ thị cho chất khí"


def note_terms(lang):
    """A one-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 19.</b> phương pháp ABC dạng đồ thị "
                "(graphical ABC method) · đồ thị A/B/C (hình 19-1/19-2/19-3) · "
                "hệ số lưu lượng Cv · <b>D</b> = kích thước lớn hơn giữa cỡ van và "
                "cỡ ống hạ lưu, tính bằng inch · tỷ số Cv/D² · đường kính ống ra · "
                "áp suất đầu vào tuyệt đối P₁, psia · tỷ số áp suất "
                "X = (P₁ − P₂)/P₁ · 10X · hệ số đường kính tia khí Fd · hệ số FL · "
                "mức áp suất âm thanh dBA tại 1 m · cấp ống (pipe schedule) "
                "20 / 40 / 80 / 160 · hệ số thành ống · van cầu (globe valve) · "
                "bộ mở rộng (expander)")
    return ("<b>Key terms.</b> graphical ABC method · Graphs A, B and C "
            "(Figures 19-1 to 19-3) · flow coefficient Cv · <b>D</b>, the larger "
            "of valve size or downstream pipe size in inches · Cv/D² ratio · "
            "outlet pipe diameter · absolute inlet pressure P₁ in psia · "
            "pressure ratio X = (P₁ − P₂)/P₁ · 10X · gas jet diameter factor Fd · "
            "FL · sound pressure level in dBA at 1 m · pipe schedule "
            "(20, 40, 80, 160) · pipe wall modifier · globe valve · expander")


def body_vi():
    b = []
    b.append(h2("Các đồ thị ABC cho chất khí", "The Graphical ABC for Gases"))

    b.append(p("Ở đây ta có các đồ thị A, B và C (Hình 19-1, 19-2 và 19-3), mô tả "
               "chính xác tất cả các phương trình của Chương 18 dưới dạng đồ thị."))
    b.append(p("<b>D</b> là kích thước lớn hơn giữa cỡ van và cỡ ống hạ lưu, tính "
               "bằng inch."))
    b.append(p("Sau đây là cách sử dụng các đồ thị."))

    b.append(h3("Đồ thị A — Hình 19-1", "Graph A — Figure 19-1"))
    b.append(p("Trước hết, chia Cv thực tế (phù hợp với điều kiện dòng chảy của "
               "bạn) cho đường kính ống ra tính bằng inch. Xác định đường kính "
               "ống ở dưới cùng của Đồ thị A, từ đó nhận diện đường cong khớp với "
               "Cv/D². Sau đó đọc giá trị dBA tương ứng ở bên trái."))
    b.append(eq("A = 25 log(D) − 10 + 20 log(Cv/D²)"))
    b.append(fig(1, F.fig_f191()))

    b.append(h3("Đồ thị B — Hình 19-2", "Graph B — Figure 19-2"))
    b.append(p("Tiếp theo, xác định áp suất đầu vào thực tế tính bằng psia ở dưới "
               "cùng của Đồ thị B. Đi lên đến đường cong rồi đọc giá trị dBA tương "
               "ứng ở bên trái."))
    b.append(eq("B = 35 log(P₁ psia) − 35"))
    b.append(fig(2, F.fig_f192()))

    b.append(h3("Đồ thị C — Hình 19-3", "Graph C — Figure 19-3"))
    b.append(p("Giờ đến Đồ thị C. Trước tiên tính tỷ số áp suất thực tế "
               "X = (P₁ − P₂)/P₁. Nhân X với 10. Từ giá trị 10X tương ứng, hãy "
               "tìm đường cong khớp với giá trị Fd của van đã chọn (nếu cần, xem "
               "Bảng 5-4)."))
    b.append(eq("X = (P₁ − P₂)/P₁   ·   10X"))
    b.append(eq("C = 27 + 30 log(10X) + 20 log(Fd)"))
    b.append(fig(3, F.fig_f193()))

    b.append(h2("Cộng các thành phần và các hệ số hiệu chỉnh",
                "Adding the Parts and Modifiers"))
    b.append(p("Việc còn lại rất dễ: cộng tất cả các giá trị A, B và C rồi hiệu "
               "chỉnh theo 30 log(F_L/0,7), trong đó F_L là hệ số F_L của van đã "
               "được thử nghiệm. Kết quả là mức ồn ước tính, tính bằng dBA, tại "
               "khoảng cách 1 m từ thành ống."))
    b.append(eq("A + B + C + 30 log(F_L/0,7)"))
    b.append(p("Lưu ý: luôn dùng đường kính của ống tại cửa ra của van, hoặc sau "
               "cửa ra của bộ mở rộng nếu có."))

    b.append(h3("Ví dụ: hệ số thành ống", "Example: Pipe wall modifier"))
    b.append(p("Đối với van cầu, trừ 3 dB. Nếu cần điều chỉnh theo độ dày của "
               "ống, dùng các hệ số sau: schedule 40 = 0; schedule 80: trừ 4; "
               "schedule 160: trừ 6. Bảng in trong nguyên bản cho biết Pipe "
               "Schedule: 20 | 40 | 80 | 160 và C, dBA = +4 | 0 | −4 | −8."))
    b.append(table(
        ["Cấp ống (Pipe Schedule)", "20", "40", "80", "160"],
        [["C, dBA", "+4", "0", "−4", "−8"]],
        "Bảng 19-1. Hệ số hiệu chỉnh thành ống (cộng vào kết quả A + B + C)."))
    b.append(p("Nếu kết quả với ống schedule 40 là 85 dB(A), thì khi thay bằng "
               "ống schedule 80 mức ồn sẽ là 85 − 4 = 81 dB."))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Nguyên bản không đánh số phương "
                  "trình nào; bản dịch trình bày các biểu thức dưới dạng phương "
                  "trình không số, gồm X = (P₁ − P₂)/P₁ và 30 log(F_L/0,7). "
                  "(2) Phần văn bản ghi schedule 160 trừ 6, nhưng bảng in cho "
                  "giá trị −8 (schedule 20 = +4, 40 = 0, 80 = −4, 160 = −8). "
                  "Bản Anh giữ cả hai cách ghi và nêu rõ sự khác biệt giữa 6 và "
                  "8 trong ghi chú này; bản Việt cũng trình bày cả hai. (3) Ba "
                  "đồ thị là ảnh trong PDF; bản dịch vẽ lại dạng vector theo các "
                  "phương trình đã in. (4) Lớp văn bản OCR xáo trộn các ký hiệu "
                  "toán học; các dạng in được đọc lại từ ảnh trang."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Chương 19 chiếm các trang in 121–123 của ấn bản in (PDF tr. "
               "123–125). Nguyên bản gồm phần mở đầu với ba đồ thị A, B, C, "
               "hướng dẫn cách dùng từng đồ thị, phần cộng và hiệu chỉnh theo "
               "F_L, ví dụ về hệ số thành ống kèm bảng bốn cột, và ba hình "
               "19-1 đến 19-3 — tất cả đều được giữ lại."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("The Graphical ABC for Gases", "The Graphical ABC for Gases"))

    b.append(p("Here we have graphs A, B, and C (Figures 19-1, 19-2, and 19-3), "
               "depicting exactly all equations from Chapter 18 in graphical form."))
    b.append(p("<b>D</b> is the larger of valve size or downstream pipe size in "
               "inches."))
    b.append(p("Here is how to use the graphs."))

    b.append(h3("Graph A — Figure 19-1", "Graph A — Figure 19-1"))
    b.append(p("First, divide the actual Cv (which matches your flow condition) "
               "by the outlet pipe diameter in inches. Locate the pipe diameter "
               "at the bottom of Graph A, and from there identify the curve "
               "matching your Cv/D². Then look up the corresponding dBA value on "
               "the left."))
    b.append(eq("A = 25 log(D) − 10 + 20 log(Cv/D²)"))
    b.append(fig(1, F.fig_f191()))

    b.append(h3("Graph B — Figure 19-2", "Graph B — Figure 19-2"))
    b.append(p("Next, locate the actual inlet pressure in psia at the bottom of "
               "Graph B. Go up to the curve and find the matching dBA on the "
               "left."))
    b.append(eq("B = 35 log(P₁ psia) − 35"))
    b.append(fig(2, F.fig_f192()))

    b.append(h3("Graph C — Figure 19-3", "Graph C — Figure 19-3"))
    b.append(p("Now to Graph C. First, calculate the actual pressure ratio "
               "X = (P₁ − P₂)/P₁. Multiply X by 10. Then, from the corresponding "
               "10X, look up to identify a curve matching the Fd value of your "
               "selected valve (consult Table 5-4 if needed)."))
    b.append(eq("X = (P₁ − P₂)/P₁   ·   10X"))
    b.append(eq("C = 27 + 30 log(10X) + 20 log(Fd)"))
    b.append(fig(3, F.fig_f193()))

    b.append(h2("Adding the Parts and Modifiers", "Adding the Parts and Modifiers"))
    b.append(p("Now is the easy part: simply add all A, B, and C variables and "
               "correct for 30 log(FL/0.7), where FL is the FL of the tested "
               "valve. You now have the estimated sound level in dBA at 1 m from "
               "the pipe wall."))
    b.append(eq("A + B + C + 30 log(FL/0.7)"))
    b.append(p("Note: Always use the diameter of the pipe at the valve’s outlet "
               "or after an expander outlet, should one be used."))

    b.append(h3("Example: Pipe wall modifier (add to ABC results)",
                "Example: Pipe wall modifier (add to ABC results)"))
    b.append(p("For globe valves, subtract 3 dB. If adjustments are needed for "
               "the pipe, use these modifiers: schedule 40 = 0; for schedule 80, "
               "subtract 4; for schedule 160, subtract 6. The printed table says "
               "Pipe Schedule: 20 40 80 160, with C, dBA = +4 0 −4 −8."))
    b.append(table(
        ["Pipe Schedule", "20", "40", "80", "160"],
        [["C, dBA", "+4", "0", "−4", "−8"]],
        "Table 19-1. Pipe wall modifier (add to ABC results)."))
    b.append(p("If the result using a schedule 40 pipe is 85 dB(A), then "
               "substituting a schedule 80 pipe would result in a sound level of "
               "85 − 4 = 81 dB."))

    b.append(note("<b>Source note.</b> (1) The source numbers no equations; the "
                  "translation shows the expressions as unnumbered equation "
                  "markup, including X = (P₁ − P₂)/P₁ and 30 log(FL/0.7). "
                  "(2) The prose says to subtract 6 for schedule 160, while the "
                  "printed table gives −8 dBA (Pipe Schedule 20 / 40 / 80 / "
                  "160; C, dBA = +4 / 0 / −4 / −8). Both readings are kept here, "
                  "and the 6-versus-8 discrepancy is recorded in this note; the "
                  "Vietnamese also shows both. (3) The three graphs are images "
                  "in the PDF; they are redrawn as vectors from the printed "
                  "equations. (4) The OCR text layer garbles the mathematical "
                  "symbols; the printed forms were read back from the page "
                  "renders."))
    b.append(h3("About the source", "About the source"))
    b.append(p("Chapter 19 occupies printed pp. 121–123 (PDF pp. 123–125). The "
               "source consists of the introduction to graphs A, B and C, the "
               "instructions for using each graph, the addition and the FL "
               "correction, the pipe wall modifier example with its four-column "
               "table, and Figures 19-1 to 19-3, all of which are retained."))
    return "".join(b)
