# -*- coding: utf-8 -*-
"""Book 7, Chapter 22, part C - anticavitation trims and fluid/schedule
adjustments (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
141-143 (PDF pp. 140-142). Covers the Table 22-1 verification note, sound
reduction from anticavitation trims, multistep trim with increasing flow
areas (required inputs, initial calculations, final equations and the
3-inch globe worked example), single-stage resistance trims with Figure
22-5, the adaptation for liquids other than water and the pipe-schedule
modifiers.

Every equation in this range is garbled in the OCR text layer; all formulas
and numeric results below were transcribed from the page renders. Printed
arithmetic slips (log(156), 10.31) are retained in the English text; the
Vietnamese uses the intended values.
"""
from cvp_common import p, h2, h3, eq, ul, note, fig

try:
    import cvpfig22 as F
except ImportError:
    import sys as _sys
    import types as _types
    F = _sys.modules.setdefault("cvpfig22", _types.ModuleType("cvpfig22"))

if not hasattr(F, "fig_f225"):
    # Temporary non-overwriting stand-in used only until the figure supplier
    # lands; a real supplier callable is never replaced.
    def _fig_f225_stub():
        return (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 360" '
            'role="img" aria-label="3 inch globe valve multi-stage trim test data">'
            '<rect x="70" y="30" width="560" height="250" fill="#ffffff" '
            'stroke="#333333"/>'
            '<line x1="70" y1="280" x2="630" y2="280" stroke="#333333"/>'
            '<line x1="70" y1="30" x2="70" y2="280" stroke="#333333"/>'
            '<polyline points="70,280 630,30" fill="none" stroke="#999999" '
            'stroke-dasharray="2,4"/>'
            '<text x="350" y="308" font-size="12">Pressure Ratio X 10</text>'
            '<text x="14" y="160" font-size="12">Sound Level dB(A)</text>'
            '</svg>',
            "Hình 22-5 · Số liệu thử nghiệm của van cầu 3 in với bộ lót giảm ồn đa cấp.",
            "Figure 22-5 · Test data for a 3 in globe valve with multistep "
            "noise-reducing trim.",
            "",
            "",
        )

    F.fig_f225 = _fig_f225_stub


def body_vi():
    b = []
    b.append(p("Bảng 22-1 đưa ra các ví dụ so sánh số liệu thử nghiệm thực tế của "
               "nhiều loại van với các ước tính theo phương pháp ABC. <b>Lưu ý:</b> "
               "Những phép tính này đã được một thành viên của ủy ban tiêu chuẩn "
               "ISA75 (tiêu chuẩn 75.07) về tiếng ồn của van điều khiển kiểm chứng."))

    b.append(h2("Giảm tiếng ồn nhờ bộ lót van chống xâm thực",
                "Sound Reduction from Using Anticavitation Valve Trim"))

    b.append(h3("Bộ lót nhiều cấp với diện tích dòng chảy tăng dần",
                "Multistep Trim with Increasing Flow Areas"))
    b.append(p("Loại bộ lót này làm giảm tiếng ồn do chất lỏng nhiễu loạn và do "
               "xâm thực phát ra."))

    b.append(h3("Dữ liệu đầu vào bắt buộc", "Required Input"))
    b.append(ul([
        "C<sub>v</sub> ở điều kiện dòng chảy dưới ngưỡng (underflow)",
        "P₁ = áp suất đầu vào, tính bằng psia",
        "AR = tỷ số diện tích giữa diện tích của cấp (các cấp) đầu vào và cấp "
        "(các cấp) đầu ra",
        "F<sub>L</sub> của cấp (các cấp) đầu ra",
        "D = đường kính ống đầu ra, tính bằng inch",
    ]))
    b.append(note("Đối với bộ lót có diện tích không đổi, dùng AR = 1/n₀, trong "
                  "đó n₀ là số cấp."))

    b.append(h3("Tính toán ban đầu", "Initial Calculations"))
    b.append(eq("AR = A₁ / A₂"))
    b.append(eq("P₁s = P₁ × AR;    ΔX = 30 log(1 / AR)<sup>0.5</sup>"))

    b.append(h3("Phương trình cuối", "Final Equations"))
    b.append(eq("A = 8 log(D) + 12 log(C<sub>v</sub> / D²) + 4  dB"))
    b.append(eq("B<sub>ls</sub> = 35 log(P₁s) − 35  dB"))
    b.append(eq("L<sub>pAe,1m</sub> = A + B<sub>ls</sub> + 30 log(10X) − ΔX  dBA"))

    b.append(h3("Ví dụ", "Example"))
    b.append(ul([
        "D = 3 in",
        "P₁ = 480 psia",
        "AR = 4/1",
        "F<sub>L</sub> của cấp cuối = 0.8",
        "C<sub>v</sub> = 13",
        "X = 0.5",
    ]))
    b.append(eq("AR = 0.25, P₁s = 480 × 0.25 = 120 psia, C<sub>v</sub> / D² = 1.56, "
                "ΔX = 30 log(1 / 0.25)<sup>0.5</sup> = 9 dB"))
    b.append(eq("A = 8 log(3) + 12 log(1.56) + 4 = 3.82 + 2.32 + 4 = 10.13 dB"))
    b.append(eq("B<sub>ls</sub> = 35 log(P₁s) − 35 = 37.8 dB"))
    b.append(eq("L<sub>Ae,1m</sub> = 60.14 dBA (số liệu thử nghiệm trong Hình 22-5 "
                "cho kết quả 60 dBA tại X = 0.5)"))
    b.append(note("Nguyên bản in log(156) rồi dùng 10.31 thay cho 10.13 ở dòng "
                  "cộng; bản Anh giữ nguyên cách in, bản Việt dùng log(1.56) và "
                  "10.13 theo ý đồ tính toán."))

    b.append(h2("Bộ lót điện trở một cấp", "Single-Stage Resistance Trims"))
    b.append(p("Loại bộ lót này gồm các lồng hoặc tấm có nhiều lỗ. Dù mang lại một "
               "số lợi ích, chúng không làm giảm mức ồn của dòng chảy nhiễu loạn. "
               "Tuy nhiên, nếu thiết kế tốt, chúng có thể tăng hệ số bắt đầu xâm "
               "thực X<sub>Fz</sub>, từ đó giảm tiếng ồn do xâm thực."))
    b.append(p("Các đường dẫn chất lỏng với đầu vào thuôn dần đặc biệt hiệu quả "
               "trong việc này: trước hết chúng làm giảm sự co thắt của tia, cho "
               "phép các đường dẫn nhỏ hơn và nhiều diện tích dòng chảy hơn trên "
               "bề mặt ngoài với cùng một lượng chất lỏng. Thứ hai, cách này có "
               "xu hướng tăng hệ số phục hồi áp suất (F<sub>L</sub>), làm tăng hệ "
               "số X<sub>Fz</sub>. Tăng hệ số X<sub>Fz</sub> từ 0.2 lên 0.4 sẽ "
               "giúp tiết kiệm 14 dB mức ồn."))
    b.append(note("Nếu không tính đến lực cản của chất lỏng trong thân van, hệ số "
                  "X<sub>Fz</sub> của một đường dẫn tương đương với F<sub>L</sub>² "
                  "của đường dẫn đó."))
    b.append(fig(5, F.fig_f225()))

    b.append(h2("Điều chỉnh tiêu chuẩn cho chất lỏng khác nước (chất lỏng)",
                "Adapting the Standard for Fluids Other Than Water (Liquid)"))
    b.append(p("Các điều chỉnh này cho chất lỏng khác nước áp dụng cho mọi phương "
               "pháp ước tính tiếng ồn và xâm thực của chất lỏng."))
    b.append(eq("L<sub>pAe,1m(liquid)</sub> = L<sub>Ae,1m(water)</sub> + "
                "25 log(327 / cᵢ(liquid)) + 20 log(62.5 / ρ(liquid))"))

    b.append(h3("Ví dụ", "Example"))
    b.append(p("L<sub>pAe,1m(water)</sub> = 85 dBA; một chất lỏng khác có tốc độ "
               "âm (cᵢ) là 219 ft/s và khối lượng riêng ρ là 53 lb/ft³."))
    b.append(eq("L<sub>pAe,1m(different liquid)</sub> = 85 + 25 log(327 / 219) + "
                "20 log(62.5 / 53) = 90.7 dBA"))

    b.append(h2("Các hệ số hiệu chỉnh", "Modifiers"))
    b.append(p("Ống schedule 40: trừ (0) dB; ống schedule 80: trừ 3 dB; và ống "
               "schedule 160: trừ 7 dB."))
    return "".join(b)


def body_en():
    b = []
    b.append(p("Table 22-1 provides examples of comparing real test data for "
               "various valve types with ABC method estimations. <b>Note:</b> "
               "These calculations were verified by a member of the ISA75 "
               "standards committee (standard 75.07) on control valve noise."))

    b.append(h2("Sound Reduction from Using Anticavitation Valve Trim"))

    b.append(h3("Multistep Trim with Increasing Flow Areas"))
    b.append(p("This type of trim reduces the sound produced by turbulent fluid "
               "and cavitation."))

    b.append(h3("Required Input"))
    b.append(ul([
        "C<sub>v</sub> underflow condition",
        "P₁ = inlet pressure in psia",
        "AR = area ratio between the area of inlet stage (s) and outlet stage(s)",
        "F<sub>L</sub> of outlet stage(s)",
        "D = outlet pipe diameter in inches",
    ]))
    b.append(note("For constant area trims, use AR = 1/n₀, where n₀ is the number "
                  "of stages."))

    b.append(h3("Initial Calculations"))
    b.append(eq("AR = A₁ / A₂"))
    b.append(eq("P₁s = P₁ × AR;    ΔX = 30 log(1 / AR)<sup>0.5</sup>"))

    b.append(h3("Final Equations"))
    b.append(eq("A = 8 log(D) + 12 log(C<sub>v</sub> / D²) + 4  in dB"))
    b.append(eq("B<sub>ls</sub> = 35 log(P₁s) − 35  in dB"))
    b.append(eq("LP<sub>Ae,1m</sub> = A + B<sub>ls</sub> + 30 log(10X) − ΔX  in dBA"))

    b.append(h3("Example"))
    b.append(ul([
        "D = 3 in",
        "P₁ = 480 psia",
        "AR = 4/1",
        "F<sub>L</sub> last stage = 0.8",
        "C<sub>v</sub> = 13",
        "X = 0.5",
    ]))
    b.append(eq("AR = 0.25, P₁s = 480 × 0.25 = 120 psia, C<sub>v</sub> / D² = 1.56, "
                "ΔX = 30 log(1 / 0.25)<sup>0.5</sup> = 9 dB"))
    b.append(eq("A = 8 log(3) + 12 log(156) + 4 = 3.82 + 2.32 + 4 = 10.13 dB"))
    b.append(eq("B<sub>ls</sub> = 35 log(P₁s) − 35 = 37.8 dB"))
    b.append(eq("L<sub>Ae,1m</sub> = 10.31 + 37.8 + 21 − 9"))
    b.append(eq("L<sub>Ae,1m</sub> = 60.14 dBA (test data from Figure 22-5 shows "
                "60 dBA results at X = 0.5)"))
    b.append(note("The printed calculation writes log(156) and then uses 10.31 in "
                  "place of 10.13 on the summation line; both are retained above "
                  "as printed. The Vietnamese text uses log(1.56) and 10.13."))

    b.append(h2("Single-Stage Resistance Trims"))
    b.append(p("This type of trim consists of multiported cages or plates. While "
               "providing some benefits, they do not reduce sound levels from "
               "turbulent flow. However, if well-designed, they can increase the "
               "coefficient of cavitation X<sub>Fz</sub> and thus reduce cavitation "
               "noise."))
    b.append(p("Flow passages with tapered inlets are especially effective in this "
               "regard by first reducing jet constriction, thereby allowing for "
               "smaller passages and more flow areas at the external surface for "
               "the same amount of fluid. Second, this tends to increase the "
               "pressure recovery factor (F<sub>L</sub>), which increases the "
               "X<sub>Fz</sub> factor. An increase from an X<sub>Fz</sub> factor "
               "of 0.2 to 0.4 will result in a sound level savings of 14 dB."))
    b.append(note("Not counting fluid resistance in the valve housing, the "
                  "X<sub>Fz</sub> factor of a passage is equivalent to the "
                  "F<sub>L</sub>² of a passage."))
    b.append(fig(5, F.fig_f225()))

    b.append(h2("Adapting the Standard for Fluids Other Than Water (Liquid)"))
    b.append(p("These modifications for liquids other than water apply to all "
               "liquid sound and cavitation estimating methods."))
    b.append(eq("L<sub>pAe,1m(liquid)</sub> = L<sub>Ae,1m(water)</sub> + "
                "25 log(327 / cᵢ(liquid)) + 20 log(62.5 / ρ(liquid))"))

    b.append(h3("Example"))
    b.append(p("L<sub>pAe,1m(water)</sub> = 85 dBA; a different liquid has a speed "
               "of sound (cᵢ) of 219 ft/s and a density ρ of 53 lb/ft³."))
    b.append(eq("L<sub>pAe,1m(different liquid)</sub> = 85 + 25 log(327 / 219) + "
                "20 log(62.5 / 53) = 90.7 dBA"))

    b.append(h2("Modifiers"))
    b.append(p("For schedule 40 pipe, subtract (0) dB; for schedule 80 pipe, "
               "subtract 3 dB; and for schedule 160 pipe, subtract 7 dB."))
    return "".join(b)
