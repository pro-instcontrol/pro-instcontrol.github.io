# -*- coding: utf-8 -*-
"""Chapter 8, span C: objective function of optimum design.

Source: work/ppic_raw.txt lines 4770-4818, PDF pp. 177-178, printed pp. 161-162.
Table 1 and equations (14)-(17) were re-read from the page renders.
"""
import ppicfig8 as F
from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS

_EQ14 = ("σ<sub>qₙ</sub>² = ∫<sub>−∞</sub><sup>∞</sup> S<sub>qₙ</sub>(ω) dω "
         "= ∫<sub>−∞</sub><sup>∞</sup> |y₁(ω)|² S₀ dω.")
_EQ15 = "ω<sub>d</sub> = (1 − Δ)ω<sub>n</sub>."
_EQ16 = ("ω<sub>p</sub> = [(1 − Δ) + (p − (m + 1)/2)β/(m − 1)]ω<sub>n</sub>.")
_EQ17 = "min σ<sub>qₙ</sub>²(Δ, β, ξ<sub>d</sub>)."

_SCALE = [
    "S<sub>L</sub> = 1/30",
    "S<sub>E</sub> = 1/2",
    "S<sub>ρe</sub> = 4.24",
    "S<sub>T</sub> = 0.097",
    "S<sub>ω</sub> = 10.3",
    "S<sub>a</sub> = 3.5",
]
_DIM = ["[L]", "[FL<sup>−2</sup>]", "[FL<sup>−4</sup>T<sup>2</sup>]",
        "[T]", "[T<sup>−1</sup>]", "[LT<sup>−2</sup>]"]
_VI_ROWS = [
    ["Kích thước", _DIM[0], _SCALE[0]],
    ["Mô đun Young", _DIM[1], _SCALE[1]],
    ["Mật độ khối lượng hiệu dụng", _DIM[2], _SCALE[2]],
    ["Thời gian", _DIM[3], _SCALE[3]],
    ["Tần số", _DIM[4], _SCALE[4]],
    ["Gia tốc", _DIM[5], _SCALE[5]],
]
_EN_ROWS = [
    ["Size", _DIM[0], _SCALE[0]],
    ["Young's modulus", _DIM[1], _SCALE[1]],
    ["Effective mass density", _DIM[2], _SCALE[2]],
    ["Time", _DIM[3], _SCALE[3]],
    ["Frequency", _DIM[4], _SCALE[4]],
    ["Acceleration", _DIM[5], _SCALE[5]],
]


def section(lang):
    b = []
    H(b, lang, "Hàm mục tiêu của thiết kế tối ưu",
      "Objective Function of Optimum Design", level=3)
    P(b, lang,
      "Vì chuyển động nền gồm các dao động ngẫu nhiên, phương sai của phản ứng dịch chuyển kết "
      "cấu được giải trong mô hình ngẫu nhiên của chuyển động nền động đất, và phương sai nhỏ "
      "nhất được dùng làm hàm mục tiêu cho thông số tối ưu.",
      "Considering that ground motion consists of random vibrations, the variance of the "
      "structural displacement response is solved under the stochastic model of the earthquake "
      "ground motion, and the minimum variance is used as the objective function of the optimal "
      "parameter.")
    TBL(b, lang,
        ["Đại lượng vật lý", "Thứ nguyên", "Hệ số tỷ lệ"],
        ["Physical quantity", "Dimension", "Scaling coefficient"],
        _VI_ROWS if lang == "vi" else _EN_ROWS,
        caption_vi="Bảng 8.1 · Hệ số tương tự chi tiết",
        caption_en="Table 8.1 · Detailed similarity coefficients")
    P(b, lang,
      "Giả sử tác động địa chấn là một quá trình ngẫu nhiên dừng kết hợp nhiễu trắng và S₀ là "
      "mật độ phổ công suất của sóng địa chấn, phương sai phản ứng của tọa độ tổng quát trong "
      "phương thức chính của kết cấu có thể được biểu diễn như sau [33]:",
      "Assuming that the seismic excitation is a stationary random white-noise process and that "
      "S₀ is the power spectrum density of seismic waves, the generalized coordinate response "
      "variance of the main structure mode can be expressed as follows [33]:")
    E(b, lang, _EQ14, _EQ14, num="14")
    P(b, lang,
      "Trong xây dựng nhà máy nhiệt điện, khối lượng của tất cả các phễu than là như nhau và tỷ "
      "số cản của tất cả CBD được thiết kế bằng nhau, tức là m<sub>p</sub> = m<sub>d</sub> và "
      "ξ<sub>p</sub> = ξ<sub>d</sub>, với p = 1, 2, ..., m. Biến βω<sub>n</sub> là độ hội tụ của "
      "tỷ số tần số, và khoảng tỷ số tần số được cho bởi βω<sub>n</sub>/(m − 1).",
      "In thermal power plant construction, the mass of all coal scuttles is the same, and the "
      "damping ratios of all CBDs are designed to be equal, that is, m<sub>p</sub> = m<sub>d</sub> "
      "and ξ<sub>p</sub> = ξ<sub>d</sub>, where p = 1, 2, ..., m. The variable βω<sub>n</sub> is "
      "the frequency ratio convergence, and the frequency ratio interval is given by "
      "βω<sub>n</sub>/(m − 1).")
    P(b, lang,
      "Biến ω<sub>d</sub> biểu diễn tần số trung bình của các CBD, còn Δ là độ lệch giữa tần số "
      "trung bình của các CBD và tần số của phương thức chính của kết cấu, liên hệ như sau [17]:",
      "The variable ω<sub>d</sub> represents the average frequency of the CBDs, and Δ is the "
      "deviation between the average frequency of the CBDs and the frequency of the main "
      "structure mode, related as follows [17]:")
    E(b, lang, _EQ15, _EQ15, num="15")
    P(b, lang,
      "Do đó, tần số của CBD thứ p có thể được tính bằng",
      "Thus, the pth CBD frequency can be calculated by")
    E(b, lang, _EQ16, _EQ16, num="16")
    P(b, lang,
      "Trong kết cấu nhà máy nhiệt điện, khối lượng của phễu than có thể được xác định trước. Do "
      "đó, hàm mục tiêu có thể được biểu diễn là:",
      "In a thermal power plant structure, the mass of the coal scuttle can be determined first. "
      "Therefore, the objective function can be expressed as")
    E(b, lang, _EQ17, _EQ17, num="17")
    P(b, lang,
      "Trong bài báo này, quá trình tối ưu được thực hiện bằng các kỹ thuật tìm kiếm số sử dụng "
      "gói phần mềm MATLAB.",
      "In this paper, the optimization process is performed by numerical searching techniques "
      "using the MATLAB software package.")
    return b
