# -*- coding: utf-8 -*-
"""Book 7, Chapter 22 (part a) — chapter opening, Equation 22-1 and Graphs A/B/C.

EN/VI bilingual prose for printed pp. 137-139 (PDF pp. 136-138). The OCR text
layer garbles Equation 22-1; the form used here was transcribed from the
render of printed p. 137 (work/cvp22_pages/p136.png)::

    L_{a,liq.} = A + B + C - rw plus modifiers, in dBA at 1 m distance    (22-1)

Figures 22-1 to 22-4 are embedded with fig(n, F.fig_f22N()); a non-overwriting
stub is installed only if the figure supplier module has not yet defined the
corresponding callable.
"""
from cvp_common import fig, h3, lead, note, p, eq
try:
    import cvpfig22 as F
except ImportError:  # supplier module not landed yet
    import types
    F = types.ModuleType("cvpfig22")


PAGES_SRC = 7
TITLE_EN = "Graphical Estimation of Noise Produced by Turbulence and Cavitation of Liquids"
TITLE_VI = "Ước tính đồ thị tiếng ồn do nhiễu loạn và xâm thực chất lỏng"
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"


def _stub(n, vi_label, en_label):
    """A minimal valid 5-tuple used only while the figure supplier is running."""
    def _f():
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 360" '
            'role="img" aria-label="Figure 22-%d">'
            '<rect x="46" y="16" width="588" height="272" fill="#fdfcf9" '
            'stroke="#888888"/>'
            '<text x="340" y="160" text-anchor="middle" font-size="18" '
            'fill="#555555">Figure 22-%d - %s</text></svg>' % (n, n, en_label)
        )
        return (svg,
                "Hình 22-%d · %s" % (n, vi_label),
                "Figure 22-%d · %s" % (n, en_label),
                "Hình 22-%d" % n,
                "Figure 22-%d" % n)
    return _f


for _n, _vi, _en in (
    (1, "Đồ thị A", "Graph A"),
    (2, "Đồ thị B", "Graph B"),
    (3, "Đồ thị C", "Graph C"),
    (4, "Số liệu thử nghiệm van cắm quay", "Rotary plug test data"),
):
    if not hasattr(F, "fig_f22%d" % _n):
        setattr(F, "fig_f22%d" % _n, _stub(_n, _vi, _en))


def body_vi():
    b = []
    b.append(lead("Các đồ thị trong Hình 22-1, 22-2 và 22-3 cho phép ước tính "
                  "nhanh mức âm mà không cần dùng chương trình máy tính. Độ "
                  "chính xác điển hình có thể đạt ±3 dB."))

    b.append(eq("L<sub>a,liq.</sub> = A + B + C − r<sub>w</sub> cộng thêm các "
                "hệ số hiệu chỉnh, tính bằng dBA tại khoảng cách 1 m", "22-1"))

    b.append(p("Tiếng ồn do dòng rối tương đối dễ ước tính, nhưng tiếng ồn do "
               "xâm thực nước lại cực kỳ phức tạp, và các phương trình trong "
               "tiêu chuẩn IEC 60534-8-4 dựa trên sự pha trộn giữa các định "
               "luật khoa học và các hệ số thực nghiệm. Không thể kỳ vọng kết "
               "quả chính xác do có quá nhiều biến số, chẳng hạn số hạt lơ "
               "lửng trong nước, độ nhám bề mặt thành thân van, v.v. Thay vì "
               "sao chép nhiều phương trình phức tạp mà độ chính xác lại hạn "
               "chế, tôi nghĩ tốt nhất là cung cấp cho người đọc một phương "
               "pháp đồ thị đơn giản."))

    b.append(p("Trong Phương trình 22-1, A là mức nền dựa trên Cᵥ trên D² tìm "
               "được từ đồ thị Hình 22-1; B là hệ số hiệu chỉnh áp suất, với "
               "B = 35 log(P₁) − 35 và P₁ là áp suất đầu vào tính bằng psia; "
               "còn C là hệ số giảm áp suất được hiệu chỉnh bởi hệ số bắt đầu "
               "xâm thực (X_Fz)."))
    b.append(eq("B = 35 log(P₁) − 35, với P₁ tính bằng psia"))

    b.append(h3("Đồ thị A — mức nền", "Graph A — Base Level"))
    b.append(p("Hình 22-1 biểu diễn mức âm dB(A) theo đường kính ống phía sau "
               "van, từ 0 đến 14 in (thang phụ tính bằng mm, 25 đến 350). Bảy "
               "đường cong tương ứng với Cᵥ = 1×D², 2×D², 3×D², 5×D², 7×D², "
               "10×D² và 15×D². Các đường cong tăng dốc rồi dần phẳng; đọc "
               "giá trị A tại giao điểm giữa đường kính ống và đường cong "
               "Cᵥ/D² tương ứng."))
    b.append(fig(1, F.fig_f221()))

    b.append(h3("Đồ thị B — hiệu chỉnh áp suất", "Graph B — Pressure Adjustment"))
    b.append(p("Hình 22-2 biểu diễn LP theo áp suất tuyệt đối đầu vào của van, "
               "từ 0 đến 350 psia (thang phụ 0 đến 22,5 bar(a)), với LP trên "
               "trục tung từ 0 đến 55 dB(A). Chỉ có một đường cong, "
               "35 log(P₁ [psia]) − 35, mang một điểm đánh dấu tại khoảng "
               "145 psia và 40,5 dBA."))
    b.append(fig(2, F.fig_f222()))

    b.append(h3("Đồ thị C — thành phần xâm thực", "Graph C — Cavitation Component"))
    b.append(p("Hình 22-3 cộng gộp thành phần tiếng ồn rối (màu xám) và thành "
               "phần tiếng ồn do xâm thực (màu đen) của nước để xác định mức "
               "âm. Trục tung là Lx tính bằng dBA, từ 0 đến 55; trục hoành là "
               "10X, từ 0 đến 10. Đường đứt nét màu xám tăng từ khoảng (1, 0) "
               "lên mức ổn định chừng 20 dBA. Bốn đường liền nét màu đen ứng "
               "với X_Fz = 0,2; 0,3; 0,4 và 0,5 (với F_L = 0,7) đều tăng đến "
               "đỉnh rồi giảm về khoảng 20 dBA khi 10X tiến về 9–10."))
    b.append(fig(3, F.fig_f223()))

    b.append(h3("Biểu đồ số liệu thử nghiệm van cắm quay",
                "Rotary-Plug Test-Data Chart"))
    b.append(p("Hình 22-4 có tiêu đề «Mức âm của van cắm quay 0,100 m: Cᵥ = 18, "
               "F_L = 0,9, F_d = 0,25, P₁ = 1000 kPa». Trục hoành là X × 10 từ "
               "1 đến 10, trục tung là mức âm tính bằng dB(A) từ 0 đến 120. "
               "Biểu đồ gồm ba chuỗi số liệu: số liệu thử nghiệm, số liệu tính "
               "toán và xu hướng rối. Số liệu thử nghiệm và tính toán tăng đến "
               "đỉnh gần X × 10 ≈ 6–7 rồi giảm về khoảng 80 dB(A), trong khi "
               "xu hướng rối tăng chậm dần."))
    b.append(fig(4, F.fig_f224()))

    b.append(note("<b>Ghi chú về nguồn.</b> Phương trình 22-1 được chuyển chép "
                  "từ bản in trang 137: vế trái in là L<sub>a,liq.</sub>; lớp "
                  "văn bản OCR làm sai lệch công thức này. Các nhãn và số liệu "
                  "trong bốn hình được giữ theo bản in."))
    return "".join(b)


def body_en():
    b = []
    b.append(lead("The graphs in Figures 22-1, 22-2, and 22-3 provide a quick "
                  "sound level estimate without using computer programs. "
                  "Accuracies of typical ±3 dB can be expected."))

    b.append(eq("L<sub>a,liq.</sub> = A + B + C − r<sub>w</sub> plus modifiers, "
                "in dBA at 1 m distance", "22-1"))

    b.append(p("While turbulent noise is relatively simple to estimate, the "
               "noise produced by cavitation of water is extremely complex, "
               "and the equations provided by IEC standard 60534-8-4 are based "
               "on a mixture of scientific laws and factors based on empirical "
               "data. No exact results can be expected due to the great number "
               "of variables, such as the number of entrained particles in the "
               "water, the surface roughness of the body wall, and so on. "
               "Rather than reproducing many complicated equations with "
               "limited accuracy, I thought it best to provide readers with a "
               "simple graphical method."))

    b.append(p("In Equation 22-1, A is a base level based on Cv per D² found in "
               "the graph in Figure 22-1; B is a pressure adjustment factor, "
               "where B = 35 log(P₁) − 35 and P₁ = inlet pressure in psia; and "
               "C is a pressure drop factor modified by the coefficient of "
               "incipient cavitation (X_Fz)."))
    b.append(eq("B = 35 log(P₁) − 35, with P₁ in psia"))

    b.append(h3("Graph A — Base Level", "Graph A — Base Level"))
    b.append(p("Figure 22-1 plots sound level in dB(A) against the downstream "
               "pipe diameter from 0 to 14 in, with a secondary scale in mm "
               "(25 to 350). Seven curves are labelled Cv = 1×D², 2×D², 3×D², "
               "5×D², 7×D², 10×D² and 15×D². The curves rise steeply and then "
               "flatten; read A at the intersection of the pipe diameter and "
               "the corresponding Cv/D² curve."))
    b.append(fig(1, F.fig_f221()))

    b.append(h3("Graph B — Pressure Adjustment", "Graph B — Pressure Adjustment"))
    b.append(p("Figure 22-2 plots LP against the absolute inlet pressure to the "
               "valve from 0 to 350 psia (secondary scale 0 to 22.5 bar(a)), "
               "with LP on the vertical axis from 0 to 55 dB(A). A single "
               "curve, 35 log(P₁ psia) − 35, carries a marker at about 145 "
               "psia and 40.5 dBA."))
    b.append(fig(2, F.fig_f222()))

    b.append(h3("Graph C — Cavitation Component", "Graph C — Cavitation Component"))
    b.append(p("Figure 22-3 combines the turbulence (gray) and cavitation "
               "(black) sound level components of water to help determine "
               "sound levels. The vertical axis is Lx in dBA from 0 to 55 and "
               "the horizontal axis is 10X from 0 to 10. The dashed gray "
               "turbulence curve rises from about (1, 0) to a plateau near 20 "
               "dBA. Four solid black cavitation curves for X_Fz = 0.2, 0.3, "
               "0.4 and 0.5 (for FL = 0.7) each rise to a peak and then fall "
               "back to roughly 20 dBA as 10X approaches 9 to 10."))
    b.append(fig(3, F.fig_f223()))

    b.append(h3("Rotary-Plug Test-Data Chart", "Rotary-Plug Test-Data Chart"))
    b.append(p("Figure 22-4 is titled 'Sound Levels of 0.100 m Rotary Plug "
               "Valve: Cv = 18, FL = 0.9, Fd = 0.25, P1 = 1000 kPa'. The "
               "horizontal axis is X × 10 from 1 to 10 and the vertical axis "
               "is Sound Level in dB(A) from 0 to 120. It shows three series: "
               "Test Data, Calculated Data and Turbulent Trend. The test and "
               "calculated data rise to a peak near X × 10 ≈ 6–7 and then fall "
               "toward 80 dB(A), while the turbulent trend rises slowly."))
    b.append(fig(4, F.fig_f224()))

    b.append(note("<b>Source note.</b> Equation 22-1 was transcribed from the "
                  "printed page 137: its left-hand side prints as "
                  "L<sub>a,liq.</sub>; the OCR text layer garbles the formula. "
                  "The labels and figures in the four graphs follow the "
                  "printed charts."))
    return "".join(b)
