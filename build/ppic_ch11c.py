# -*- coding: utf-8 -*-
"""Book 9, Chapter 11, section c: saturated adaptive output-feedback
power-level control design (Theorem 1, controller and adaptation laws,
stability inequalities, Remarks 2-3). Equations (17)-(33).
"""
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS
from ppic_ch11_eqb import EQ as EB


def section(lang):
    b = []
    H(b, lang,
      "THIẾT KẾ BỘ ĐIỀU KHIỂN CÔNG SUẤT THÍCH ỨNG BÃO HÒA PHẢN HỒI ĐẦU RA",
      "SATURATED ADAPTIVE OUTPUT-FEEDBACK POWER-LEVEL CONTROL DESIGN", level=2)

    P(b, lang,
      "Kết quả thiết kế của luật điều khiển công suất thích ứng bão hòa phản hồi đầu ra "
      "cho các MHTGR được tóm tắt trong Định lý 1 sau đây. Đây là kết quả chính của bài "
      "báo và giải quyết Bài toán 1 được nêu ở cuối Mục 2.",
      "The design result of the saturated adaptive output-feedback power-level control "
      "law for the MHTGRs is summarized as the following Theorem 1 which is the main "
      "result of this paper and solves Problem 1 raised in the end of Section 2.")

    P(b, lang,
      "<b>Định lý 1.</b> Xét hệ phi tuyến (9) với bộ điều khiển phản hồi đầu ra thích ứng "
      "bão hòa:",
      "<b>Theorem 1.</b> Consider nonlinear system (9) with saturated adaptive output "
      "feedback control:")

    E(b, lang, EB[17], EB[17], num="17")

    P(b, lang, "trong đó:", "where:")

    E(b, lang, EB[18], EB[18], num="18")
    E(b, lang, EB[19], EB[19], num="19")
    E(b, lang, EB[20], EB[20], num="20")
    E(b, lang, EB[21], EB[21], num="21")
    E(b, lang, EB[22], EB[22], num="22")
    E(b, lang, EB[23], EB[23], num="23")
    E(b, lang, EB[24], EB[24], num="24")
    E(b, lang, EB[25], EB[25], num="25")

    P(b, lang,
      "k<sub>NP</sub>, k<sub>NI</sub>, q<sub>R</sub>, k<sub>ξ</sub>, κ<sub>gi</sub> "
      "(i = 1, 2), κ<sub>fi</sub> (i = 1, 2, 3) và γ đều là các hằng số dương cho "
      "trước, 0 &lt; γ &lt; 1; còn θ̂<sub>i</sub> (i = 1, 2) là các tham số được thích "
      "ứng trực tuyến, với luật thích ứng cho bởi:",
      "k<sub>NP</sub>, k<sub>NI</sub>, q<sub>R</sub>, k<sub>ξ</sub>, κ<sub>gi</sub> "
      "(i = 1, 2), κ<sub>fi</sub> (i = 1, 2, 3); γ are all given positive constants, "
      "0 &lt; γ &lt; 1; and θ̂<sub>i</sub> (i = 1, 2) are online adapted parameters "
      "with adaptation law given by:")

    E(b, lang, EB[26], EB[26], num="26")
    E(b, lang, EB[27], EB[27], num="27")

    P(b, lang,
      "trong đó π<sub>i</sub> (i = 1, 2) là các hằng số dương cho trước. Khi đó, hệ vòng "
      "kín được tạo thành bởi (9) và (17) là ổn định nhờ đầu vào nếu:",
      "where π<sub>i</sub> (i = 1, 2) are given positive constants. Then, the "
      "closed-loop system constituted by (9) and (17) is input-to-state stable if:")

    E(b, lang, EB[28], EB[28], num="28")
    E(b, lang, EB[29], EB[29], num="29")
    E(b, lang, EB[30], EB[30], num="30")
    E(b, lang, EB[31], EB[31], num="31")
    E(b, lang, EB[32], EB[32], num="32")

    P(b, lang, "và:", "and:")

    E(b, lang, EB[33], EB[33], num="33")

    P(b, lang,
      "trong đó η, q<sub>Ei</sub> (i = 1, 2), ε<sub>NP</sub> và γ<sub>w</sub> đều là các "
      "hằng số dương cho trước, với 0 &lt; η &lt; 1.",
      "where η, q<sub>Ei</sub> (i = 1, 2), ε<sub>NP</sub> and γ<sub>w</sub> are all given "
      "positive constants, and 0 &lt; η &lt; 1.")

    P(b, lang,
      "Trước khi trình bày chứng minh của định lý này, trước tiên đưa ra hai nhận xét hữu "
      "ích sau, từ đó có thể suy ra sơ bộ một số tính chất của luật điều khiển công suất "
      "MHTGR mới được xây dựng (17).",
      "Before giving the proof of this theorem, the following two useful remarks are "
      "firstly given, from which we can preliminarily deduce some properties of "
      "newly-built MHTGR power-level control (17).")

    P(b, lang,
      "<b>Nhận xét 2.</b> Số hạng u<sub>cp</sub> trong Phương trình (17) được thiết kế "
      "đặc biệt để bù cho bão hòa đầu vào điều khiển. Nhờ tính bị chặn của hàm tiếp tuyến "
      "hyperbol th(·) cho bởi Phương trình (24), bất đẳng thức (30) có thể dễ dàng được "
      "thỏa mãn bằng cách lựa chọn phù hợp các vô hướng dương k<sub>g</sub>, q<sub>Ei</sub> "
      "(i = 1, 2), κ<sub>gi</sub> (i = 1, 2), κ<sub>fi</sub> (i = 1, 3).",
      "<b>Remark 2.</b> The term u<sub>cp</sub> in Equation (17) is just designed for "
      "compensating the control input saturation. Because of the boundness of hyperbolic "
      "tangent function th(·) given by Equation (24), inequality (30) can be easily "
      "satisfied by proper choosing positive scalars k<sub>g</sub>, q<sub>Ei</sub> "
      "(i = 1, 2), κ<sub>gi</sub> (i = 1, 2), κ<sub>fi</sub> (i = 1, 3).")

    P(b, lang,
      "<b>Nhận xét 3.</b> Nhờ tính bị chặn của hàm th(·), rõ ràng đầu vào điều khiển cho "
      "bởi Phương trình (17) thỏa mãn bất đẳng thức (16), nghĩa là bộ điều khiển này tự "
      "nhiên bị bão hòa.",
      "<b>Remark 3.</b> Due to the boundness of function th(·), it is clear that control "
      "input given by Equation (17) satisfies inequality (16), which means that this "
      "control is naturally saturated.")

    return b
