# -*- coding: utf-8 -*-
"""Control Systems (W. Bolton, Newnes 2002) — Chapter 3, System response.

Vietnamese and English prose with the 3 redrawn vector figures and the
Laplace-transform reference table.
"""
import boltonfig3 as F
from bolton_common import (eq, fig, h2, h3, h4, lead, note, ol, p, quote, table, ul, keyterms)

PAGES_SRC = 12
BYLINE = "W. Bolton · Newnes, 2002"


def note_terms(lang):
    if lang == "vi":
        return note(
            "<b>Thuật ngữ chính của chương.</b> "
            "<em>Đầu vào chuẩn (standard inputs)</em> — bậc (step), xung (impulse), dốc (ramp). · "
            "<em>Hàm truyền G(s)</em> — Y(s)/X(s), với điều kiện ban đầu không. · "
            "<em>Phân số từng phần (partial fractions)</em> — kỹ thuật tách F(s) thành các hạng đơn giản để tra bảng. · "
            "<em>Bảng biến đổi Laplace</em> — ánh xạ giữa miền s và miền thời gian. · "
            "<em>Giảm chấn (damping)</em> — ζ > 1 quá giảm, ζ = 1 tới hạn, ζ &lt; 1 dưới giảm.")
    return note(
        "<b>Key terms.</b> <em>Standard inputs</em> — step, impulse, ramp. · <em>Transfer function G(s)</em> — "
        "Y(s)/X(s) with zero initial conditions. · <em>Partial fractions</em> — splitting F(s) into simple terms "
        "to read from a table. · <em>Laplace table</em> — maps s-domain to time-domain functions. · "
        "<em>Damping</em> — ζ > 1 overdamped, ζ = 1 critical, ζ &lt; 1 underdamped.")


def body_vi():
    b = []
    b.append(lead(
        "Chương này dùng hàm truyền để tìm đáp ứng theo thời gian của hệ trước các đầu vào chuẩn (bậc, xung, "
        "dốc). Phương pháp: nhân G(s) với đầu vào dưới dạng s, rồi tra bảng biến đổi Laplace (hoặc dùng phân "
        "số từng phần) để có hàm thời gian. Cuối chương áp dụng cho hệ bậc nhất và bậc hai."))

    # 3.1
    b.append(h2("3.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Làm thế nào đầu ra của một hệ thay đổi khi có đầu vào? Chương 2 đã giới thiệu hàm truyền — tỉ lệ giữa "
        "đầu ra và đầu vào dưới dạng hàm của s. Chương này dùng hàm truyền để xác định cách đầu ra biến thiên "
        "theo thời gian ứng với từng đầu vào cụ thể."))
    # 3.2
    b.append(h2("3.2 Các dạng đầu vào", "Inputs"))
    b.append(p("Các đầu vào thường gặp có ba dạng chuẩn (Hình 3.1):"))
    b.append(fig(1, F.fig_3_1()))
    b.append(ul([
        "<b>Đầu vào bậc (step):</b> nhảy đến một giá trị không đổi tại một thời điểm.",
        "<b>Đầu vào xung (impulse):</b> tồn tại rất ngắn rồi về lại không.",
        "<b>Đầu vào dốc (ramp):</b> bắt đầu tại một thời điểm và tăng đều theo thời gian.",
    ]))
    b.append(p("Dưới dạng hàm của s:"))
    b.append(eq("Bậc đơn vị:  X(s) = 1/s", "3.1"))
    b.append(eq("Xung đơn vị:  X(s) = 1", "3.2"))
    b.append(eq("Dốc đơn vị:  X(s) = 1/s²", "3.3"))
    b.append(p(
        "Nếu đầu vào nhân với hằng số thì biến đổi Laplace cũng nhân với hằng số đó (bậc 5 V → 5/s; dốc 3 V/s "
        "→ 3/s²)."))

    # 3.3
    b.append(h2("3.3 Xác định đầu ra", "Determining outputs"))
    b.append(p("Quy trình:"))
    b.append(ol([
        "Xác định đầu ra dưới dạng hàm s: <b>Output(s) = G(s) × Input(s)</b>.",
        "Tìm hàm thời gian tương ứng bằng bảng biến đổi Laplace (Bảng 3.1); đôi khi cần đưa về dạng trong bảng.",
    ]))
    b.append(p(
        "Các tính chất hữu ích: nhân Laplace với hằng số thì hàm thời gian cũng nhân hằng số đó; tổng các số hạng "
        "s riêng biệt cho tổng các hàm thời gian tương ứng."))
    b.append(table(
        ["#", "Laplace F(s)", "Hàm thời gian f(t)"],
        [["1", "1", "xung đơn vị"],
         ["2", "1/s", "bậc đơn vị"],
         ["3", "1/s²", "dốc đơn vị t"],
         ["4", "1/(s+a)", "e^(−at)"],
         ["5", "a/[s(s+a)]", "1 − e^(−at)"],
         ["6", "1/(s+a)²", "t·e^(−at)"],
         ["7", "a²/[s²(s+a)]", "t − (1−e^(−at))/a"],
         ["8", "b/[(s+a)(s+b)]", "(e^(−at) − e^(−bt))/(b−a)"],
         ["9", "1/(s²+ω²)", "(1/ω)·sin ωt"],
         ["10", "s/(s²+ω²)", "cos ωt"],
         ["11", "ω/[(s+a)²+ω²]", "e^(−at)·sin ωt"],
         ["12", "(s+a)/[(s+a)²+ω²]", "e^(−at)·cos ωt"],
         ["13", "ωn²/[s²+2ζωn s+ωn²]", "1 − e^(−ζωn t)·sin(ωd t+φ)"]],
        caption="Bảng 3.1 — Một số cặp hàm Laplace và hàm thời gian thường dùng (ωd = ωn√(1−ζ²))."))
    b.append(p(
        "Ví dụ: đầu ra 1/(s+5) → dạng 4 với a=5 → e^(−5t) (tắt dần theo thời gian). Đầu ra 10/[s(s+5)] → dạng 5 "
        "với a=5, hệ số 2 → 2(1−e^(−5t)). Với hàm truyền 1/(s+2) và đầu vào bậc đơn vị: Y(s)=1/[s(s+2)] → dạng 5 "
        "→ ½(1−e^(−2t)). Với đầu vào dốc 2 V/s và G=4/(s+2): Y(s)=8/[s²(s+2)] → dạng 7 → 4t − 2(1−e^(−2t))."))
    b.append(h3("3.3.1 Phân số từng phần (Partial fractions)", "Partial fractions"))
    b.append(p(
        "Kỹ thuật tách một phân thức phức thành nhiều phân thức đơn giản để tra bảng. Có ba dạng:"))
    b.append(ul([
        "Mẫu chỉ chứa thừa số (s+a), (s+b), (s+c): mỗi thừa số một số hạng A/(s+a) + B/(s+b) + …",
        "Mẫu có thừa số lặp (s+a)^n: một số hạng cho mỗi lũy thừa A/(s+a) + B/(s+a)² + … + N/(s+a)^n.",
        "Mẫu có thừa số bậc hai không phân tích được (as²+bs+c): số hạng (As+B)/(as²+bs+c) + C/(s+d).",
    ]))
    b.append(p(
        "Tìm hằng số bằng cách thế s để một số hạng triệt tiêu, hoặc bằng cách so sánh hệ số từng bậc của s. Ví dụ "
        "(s+4)/[(s+1)(s+2)] = 3/(s+1) − 2/(s+2); (3s+1)/(s+2)³ = 3/(s+2)² − 5/(s+2)³; (2s+1)/[(s²+s+1)(s+2)] = "
        "(s+1)/(s²+s+1) − 1/(s+2)."))

    # 3.4
    b.append(h2("3.4 Hệ bậc nhất", "First order systems"))
    b.append(p("Hệ bậc nhất có phương trình τ·dy/dt + y = kx, hàm truyền G(s) = k/(τs+1)."))
    b.append(p(
        "<b>Đầu vào xung đơn vị</b> (X(s)=1): Y(s) = k/(τs+1) = (k/τ)/(s+1/τ) → dạng 4. Đầu ra y = (k/τ)e^(−t/τ) "
        "— một hàm suy giảm mũ, cực đại tại t=0, sau 1τ còn 0,37; 2τ còn 0,14; 3τ còn 0,05 (Hình 3.2)."))
    b.append(fig(2, F.fig_3_2()))
    b.append(p(
        "<b>Đầu vào bậc đơn vị</b> (X(s)=1/s): Y(s) = k/[s(τs+1)] → dạng 5. Đầu ra y = k(1−e^(−t/τ)) — tại 1τ đạt "
        "0,63k; 2τ đạt 0,86k; 3τ đạt 0,95k; 4τ đạt giá trị xác lập k (Hình 3.3)."))
    b.append(fig(3, F.fig_3_3()))
    b.append(p(
        "Ví dụ: mạch RC có G(s)=1/(RCs+1); với xung 3 V → Vc = (3/RC)e^(−t/RC). Cặp nhiệt điện G(s)=30×10⁻⁶/(10s+1) "
        "nhúng đột ngột vào nước 100°C (bậc 100/s) → V = 30×10⁻⁴(1−e^(−0,1t))."))

    # 3.5
    b.append(h2("3.5 Hệ bậc hai", "Second order systems"))
    b.append(p(
        "Phương trình d²y/dt² + 2ζωn·dy/dt + ωn²y = kωn²x, hàm truyền G(s) = kωn²/(s²+2ζωn s+ωn²). Với đầu vào "
        "bậc đơn vị, tùy ζ mà có ba dạng đáp ứng:"))
    b.append(ul([
        "<b>ζ > 1 (quá giảm chấn):</b> hai nghiệm thực phân biệt, đầu ra tắt dần không dao động, tiến tới k.",
        "<b>ζ = 1 (giảm chấn tới hạn):</b> hai nghiệm thực trùng, đầu ra y = k[1 − e^(−ωn t)(1+ωn t)], không dao động.",
        "<b>ζ &lt; 1 (dưới giảm chấn):</b> nghiệm phức, đầu ra dao động tắt dần với tần số góc ωd = ωn√(1−ζ²), tiến tới k.",
    ]))
    b.append(p(
        "Ví dụ: G(s)=1/(s²+8s+16)=1/[(s+4)²] → nghiệm trùng −4 → giảm chấn tới hạn. Hệ dy/dt+5dy/dt+6y=x → G(s)="
        "1/[(s+3)(s+2)] → hai nghiệm thực → quá giảm chấn; dùng phân số từng phần: y = 1/6 + (1/3)e^(−3t) − (1/2)e^(−2t)."))
    b.append(h3("Bài tập cuối chương (Problems)", "End-of-chapter problems"))
    b.append(p(
        "Chương có 19 bài tập: tìm đầu vào dưới dạng s (bậc, xung, dốc); tìm hàm thời gian từ đầu ra s; đáp ứng hệ "
        "bậc nhất/bậc hai với các đầu vào khác nhau; rút gọn phân số từng phần; xác định trạng thái giảm chấn của "
        "các hàm truyền; và đáp ứng hệ kín âm G=2/(s+2), H=4 trước đầu vào bậc đơn vị."))
    return "".join(b)


def body_en():
    b = []
    b.append(lead(
        "This chapter uses the transfer function to find a system's time response to standard inputs (step, "
        "impulse, ramp). The method: multiply G(s) by the input in s-form, then read the time function from the "
        "Laplace table (or use partial fractions). It ends by applying this to first- and second-order systems."))

    # 3.1
    b.append(h2("3.1 Introduction", "Introduction"))
    b.append(p(
        "How does a system's output change when there is an input? Chapter 2 introduced the transfer function — "
        "the ratio of output to input as a function of s. This chapter uses it to determine how the output varies "
        "with time for particular inputs."))
    # 3.2
    b.append(h2("3.2 Inputs", "Inputs"))
    b.append(p("Inputs commonly take a number of standard forms (Figure 3.1):"))
    b.append(fig(1, F.fig_3_1()))
    b.append(ul([
        "<b>Step input:</b> switches suddenly to a constant value at a particular time.",
        "<b>Impulse input:</b> exists for a very brief time before dropping back to zero.",
        "<b>Ramp input:</b> starts at a time and then increases at a constant rate.",
    ]))
    b.append(p("As s-functions:"))
    b.append(eq("Unit step:  X(s) = 1/s", "3.1"))
    b.append(eq("Unit impulse:  X(s) = 1", "3.2"))
    b.append(eq("Unit ramp:  X(s) = 1/s²", "3.3"))
    b.append(p(
        "If an input is multiplied by a constant, its Laplace transform is multiplied by the same constant (a 5 V "
        "step → 5/s; a 3 V/s ramp → 3/s²)."))

    # 3.3
    b.append(h2("3.3 Determining outputs", "Determining outputs"))
    b.append(p("The procedure:"))
    b.append(ol([
        "Determine the output as an s-function: <b>Output(s) = G(s) × Input(s)</b>.",
        "Find the corresponding time function from a table of Laplace transforms (Table 3.1); sometimes the expression must first be rearranged into a tabulated form.",
    ]))
    b.append(p(
        "Useful properties: multiplying a Laplace transform by a constant multiplies the time function by the same "
        "constant; the sum of separate s-terms gives the sum of the corresponding time functions."))
    b.append(table(
        ["#", "Laplace F(s)", "Time function f(t)"],
        [["1", "1", "unit impulse"],
         ["2", "1/s", "unit step"],
         ["3", "1/s²", "unit ramp t"],
         ["4", "1/(s+a)", "e^(−at)"],
         ["5", "a/[s(s+a)]", "1 − e^(−at)"],
         ["6", "1/(s+a)²", "t·e^(−at)"],
         ["7", "a²/[s²(s+a)]", "t − (1−e^(−at))/a"],
         ["8", "b/[(s+a)(s+b)]", "(e^(−at) − e^(−bt))/(b−a)"],
         ["9", "1/(s²+ω²)", "(1/ω)·sin ωt"],
         ["10", "s/(s²+ω²)", "cos ωt"],
         ["11", "ω/[(s+a)²+ω²]", "e^(−at)·sin ωt"],
         ["12", "(s+a)/[(s+a)²+ω²]", "e^(−at)·cos ωt"],
         ["13", "ωn²/[s²+2ζωn s+ωn²]", "1 − e^(−ζωn t)·sin(ωd t+φ)"]],
        caption="Table 3.1 — Some commonly used Laplace and time-function pairs (ωd = ωn√(1−ζ²))."))
    b.append(p(
        "Example: an output 1/(s+5) → form 4 with a=5 → e^(−5t) (exponential decay). An output 10/[s(s+5)] → form "
        "5 with a=5, coefficient 2 → 2(1−e^(−5t)). With transfer function 1/(s+2) and a unit step: Y(s)=1/[s(s+2)] "
        "→ form 5 → ½(1−e^(−2t)). With a 2 V/s ramp input and G=4/(s+2): Y(s)=8/[s²(s+2)] → form 7 → 4t − 2(1−e^(−2t))."))
    b.append(h3("3.3.1 Partial fractions", "Partial fractions"))
    b.append(p(
        "Partial fractions convert a complex fraction into simpler fractions so it matches a tabulated form. Three "
        "basic types:"))
    b.append(ul([
        "Denominator factors only of the form (s+a), (s+b), (s+c): one term per factor, A/(s+a) + B/(s+b) + …",
        "Denominator has repeated (s+a)^n: one term for each power, A/(s+a) + B/(s+a)² + … + N/(s+a)^n.",
        "Denominator has a non-factorising quadratic (as²+bs+c): (As+B)/(as²+bs+c) + C/(s+d).",
    ]))
    b.append(p(
        "Find the constants by choosing s-values that zero some terms, or by equating coefficients of powers of s. "
        "E.g. (s+4)/[(s+1)(s+2)] = 3/(s+1) − 2/(s+2); (3s+1)/(s+2)³ = 3/(s+2)² − 5/(s+2)³; (2s+1)/[(s²+s+1)(s+2)] "
        "= (s+1)/(s²+s+1) − 1/(s+2)."))

    # 3.4
    b.append(h2("3.4 First order systems", "First order systems"))
    b.append(p("A first-order system obeys τ·dy/dt + y = kx, with transfer function G(s) = k/(τs+1)."))
    b.append(p(
        "<b>Unit impulse input</b> (X(s)=1): Y(s) = k/(τs+1) = (k/τ)/(s+1/τ) → form 4. Output y = (k/τ)e^(−t/τ) — an "
        "exponential decay, maximum at t=0, then 0.37 after 1τ, 0.14 after 2τ, 0.05 after 3τ (Figure 3.2)."))
    b.append(fig(2, F.fig_3_2()))
    b.append(p(
        "<b>Unit step input</b> (X(s)=1/s): Y(s) = k/[s(τs+1)] → form 5. Output y = k(1−e^(−t/τ)) — 0.63k after 1τ, "
        "0.86k after 2τ, 0.95k after 3τ, steady value k after 4τ (Figure 3.3)."))
    b.append(fig(3, F.fig_3_3()))
    b.append(p(
        "Example: an RC circuit has G(s)=1/(RCs+1); a 3 V impulse → Vc = (3/RC)e^(−t/RC). A thermocouple with "
        "G(s)=30×10⁻⁶/(10s+1) suddenly immersed in 100°C water (step 100/s) → V = 30×10⁻⁴(1−e^(−0.1t))."))

    # 3.5
    b.append(h2("3.5 Second order systems", "Second order systems"))
    b.append(p(
        "The equation is d²y/dt² + 2ζωn·dy/dt + ωn²y = kωn²x, transfer function G(s) = kωn²/(s²+2ζωn s+ωn²). For a "
        "unit step input, the damping ratio ζ gives three response forms:"))
    b.append(ul([
        "<b>ζ > 1 (overdamped):</b> two distinct real roots, output decays without oscillation, approaching k.",
        "<b>ζ = 1 (critically damped):</b> two equal real roots, output y = k[1 − e^(−ωn t)(1+ωn t)], no oscillation.",
        "<b>ζ &lt; 1 (underdamped):</b> complex roots, output oscillates with damped angular frequency ωd = ωn√(1−ζ²), approaching k.",
    ]))
    b.append(p(
        "Example: G(s)=1/(s²+8s+16)=1/[(s+4)²] → repeated root −4 → critically damped. The system dy/dt+5dy/dt+6y=x "
        "→ G(s)=1/[(s+3)(s+2)] → two real roots → overdamped; by partial fractions y = 1/6 + (1/3)e^(−3t) − (1/2)e^(−2t)."))
    b.append(h3("End-of-chapter problems", "End-of-chapter problems"))
    b.append(p(
        "The chapter has 19 problems: finding inputs as s-functions (step, impulse, ramp); finding time functions "
        "from s-outputs; responses of first/second-order systems to various inputs; partial-fraction reduction; "
        "determining damping state of transfer functions; and the response of the closed-loop system G=2/(s+2), "
        "H=4 to a unit step input."))
    return "".join(b)
