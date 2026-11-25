# -*- coding: utf-8 -*-
"""Book 9, Chapter 5 (part C) — reactor core model, the two-step calculation
scheme and the nuclear fuel cycle cost method (EN/VI bilingual).

Source: decoded lines 2701-2786 of ``work/ppic_raw.txt`` (PDF pp. 103-105,
printed pp. 87-89). Part B already completes the sentence that breaks across
lines 2700-2703 ("295-group cross-section library ... transport equation"),
so this module resumes at line 2704. Contains Figure 5 and Tables 5.2 and
5.3 (printed as Tables 2 and 3); every printed value is transcribed from the
page renders. No numbered equation occurs in this range. Figure 5 is
supplied by ``ppicfig5_a``; a bilingual placeholder keeps section() callable
in a partial build.
"""
import ppicfig5 as F
from ppic_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

# The figure supplier may not be integrated yet. A neutral placeholder keeps
# section() callable; any callable already registered by the real supplier
# is left untouched.
if not hasattr(F, "fig_f05"):
    from ppicfig5_common import _mk

    _CAP_VI = ("Dòng tiền chi phí chu trình nhiên liệu hạt nhân với phương "
               "án xử lý trực tiếp")
    _CAP_EN = "Time flow of nuclear fuel cycle cost with direct disposal option"
    _AVI = "Sơ đồ dòng thời gian các thành phần chi phí chu trình nhiên liệu."
    _AEN = "Time flow of the nuclear fuel cycle cost components."
    _FIG5 = _mk(5, [], "Nuclear fuel cycle cost time flow",
                _CAP_VI, _CAP_EN, _AVI, _AEN)
    setattr(F, "fig_f05", lambda _t=_FIG5: _t)

# ------------------------------------------------------------- Table 5.2
# Printed Table 2: reactor operation data for the HTR.
_T52_HEAD_VI = ["Mục", "Giá trị"]
_T52_HEAD_EN = ["Items", "Values"]
_T52_ROWS_VI = [
    ["Công suất nhiệt", "600 MWth"],
    ["Công suất điện", "240 MWe"],
    ["Tuổi thọ nhà máy", "60 năm"],
    ["Chiều dài chu kỳ nạp nhiên liệu", "2 năm"],
    ["Hệ số tải", "90%"],
    ["Các phương án cuối chu trình", "Xử lý trực tiếp"],
    ["Tỷ lệ chiết khấu", "8%"],
]
_T52_ROWS_EN = [
    ["Thermal output", "600 MWth"],
    ["Electric output", "240 MWe"],
    ["Plant lifetime", "60 years"],
    ["Refueling cycle length", "2 years"],
    ["Load factor", "90%"],
    ["Back-end options", "Direct disposal"],
    ["Discount rate", "8%"],
]

# ------------------------------------------------------------- Table 5.3
# Printed Table 3: fuel cycle cost data for the HTR. Numeric values are kept
# exactly as printed; only the component names and time units are localized.
_T53_HEAD_VI = ["Thành phần", "Giá", "Thời gian dẫn trước hoặc độ trễ"]
_T53_HEAD_EN = ["Components", "Prices", "Lead or lag times"]
_T53_ROWS_VI = [
    ["Mua urani tự nhiên", "120.9 $/kg U", "24 tháng"],
    ["Mua thori", "120.9 $/kg Th", "24 tháng"],
    ["Chuyển đổi", "8.75 $/kg U", "18 tháng"],
    ["Làm giàu", "126.5 $/SWU", "12 tháng"],
    ["Chế tạo", "777 $/kg HM", "6 tháng"],
    ["Lưu trữ", "230 $/kg HM", "5 năm"],
    ["Xử lý", "610 $/kg HM", "40 năm"],
]
_T53_ROWS_EN = [
    ["Natural uranium purchase", "120.9 $/kg U", "24 months"],
    ["Thorium purchase", "120.9 $/kg Th", "24 months"],
    ["Conversion", "8.75 $/kg U", "18 months"],
    ["Enrichment", "126.5 $/SWU", "12 months"],
    ["Fabrication", "777 $/kg HM", "6 months"],
    ["Storage", "230 $/kg HM", "5 years"],
    ["Disposal", "610 $/kg HM", "40 years"],
]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 5."""
    b = []

    # --------------------------- continuation of the neutronic model text
    P(b, lang,
      "Sau đó, các nhóm năng lượng của tiết diện được thu gọn còn 26 nhóm "
      "trong quá trình đồng nhất hóa khối nhiên liệu. Ở bước (b), một lõi "
      "dạng vành khăn 1D được mô hình hóa, gồm một vùng nhiên liệu đã đồng "
      "nhất hóa và hai vùng phản xạ. Các tiết diện đã đồng nhất hóa của khối "
      "nhiên liệu tạo ra ở bước (a) được dùng cho vùng nhiên liệu ở bước này, "
      "còn các tiết diện của grafite tạo ra ở bước (a) được dùng cho các bộ "
      "phản xạ của mô hình lò 1D. Các phép tính vận chuyển 1D được thực hiện "
      "bằng phương pháp ordinate rời rạc (S_N). Chỉ các bộ phản xạ được đồng "
      "nhất hóa để tạo tiết diện của bộ phản xạ cho các phép tính toàn lõi "
      "tiếp theo. Ở bước (c), các phép tính toàn lõi 2D được thực hiện bằng "
      "phương pháp dòng giao diện (IC). Tiết diện của các khối nhiên liệu ở "
      "bước này lấy từ bước (a), trong khi tiết diện của các bộ phản xạ lấy "
      "từ bước (b).",
      "Then, the energy groups of the cross-sections are condensed to 26 "
      "groups during the homogenization of the fuel block. In step (b), a "
      "1D annular core is modeled, comprising a homogenized fuel zone and "
      "two reflector zones. The homogenized cross-sections of the fuel block "
      "generated in step (a) are used for the fuel zone in this step, and "
      "the cross-sections of the graphite generated in step (a) are used for "
      "the reflectors of the 1D reactor model. The 1D transport calculations "
      "are executed by the discrete ordinate (S_N) method. Only the "
      "reflectors are homogenized to generate the cross-sections of the "
      "reflector for the following full-core calculations. In step (c), the "
      "2D full-core calculations are executed by the interface current (IC) "
      "method. The cross-sections of fuel blocks in this step come from the "
      "step (a), while the cross-sections of reflectors come from step (b).")

    # --------------------------------------------- fuel cost analysis model
    H(b, lang, "Mô hình phân tích chi phí nhiên liệu",
      "Fuel Cost Analysis Model", level=4)

    P(b, lang,
      "Cần có một tiêu chí đánh giá khi so sánh các mức tách không gian khác "
      "nhau. Thường thì chi phí chu trình nhiên liệu là một trong các tiêu "
      "chí đó. Để so sánh công bằng, việc áp dụng một phương pháp luận chuẩn "
      "hóa cho tính toán chi phí chu trình nhiên liệu là điều kiện tiên "
      "quyết. Vì vậy, phương pháp chi phí vòng đời san đều được dùng trong "
      "nghiên cứu này. Phương pháp chi phí vòng đời san đều do Tổ chức Hợp "
      "tác và Phát triển Kinh tế (OECD) phát triển [16], dùng một phương pháp "
      "đánh giá đầu tư được chấp nhận quốc tế để phân tích chi phí chu trình "
      "nhiên liệu.",
      "An evaluation criterion must be in the comparison of different spatial "
      "separation levels. Usually, the fuel cycle cost is one of the "
      "criteria. To make a fair comparison, the adoption of a standardized "
      "methodology for fuel cycle cost calculations is prerequisite. "
      "Therefore, the levelized lifetime cost methodology is used in this "
      "study. The levelized lifetime cost methodology was developed by the "
      "Organization for Economic Cooperation and Development (OECD) [16], "
      "which uses an internationally accepted investment appraisal "
      "methodology to analyze the fuel cycle cost.")

    P(b, lang,
      "Dòng tiền cho vật liệu và dịch vụ chu trình nhiên liệu bắt đầu trước "
      "khi lò bắt đầu phát điện và tiếp tục sau khi lò ngừng vận hành. Thời "
      "điểm chính xác của các khoản thanh toán cho mua urani tự nhiên, "
      "chuyển đổi, làm giàu, chế tạo, lưu trữ nhiên liệu đã qua sử dụng và "
      "xử lý phụ thuộc vào thời gian dẫn trước và độ trễ tương ứng của các "
      "thành phần chu trình nhiên liệu. Để tính tổng chi phí chu trình "
      "nhiên liệu, cần xác định quy mô của từng thành phần chi phí và thời "
      "điểm thích hợp khi nó phát sinh. Số lượng nhiên liệu được lấy từ các "
      "phép tính neutron học của lò như mô tả trong Phần 2.2.1. Các số lượng "
      "vật liệu và dịch vụ này được điều chỉnh để tính đến tổn thất công "
      "nghệ ở các giai đoạn thành phần khác nhau của chu trình hạt nhân, rồi "
      "nhân với đơn giá để thu được chi phí từng thành phần. Cuối cùng, tổng "
      "chi phí chu trình nhiên liệu thu được bằng cách chiết khấu các "
      "thành phần chi phí này về giá trị hiện tại trong một năm cơ sở quy "
      "định (thường là ngày đưa lò vào vận hành), như thể hiện trong Hình 5. "
      "Phương pháp chi phí vòng đời san đều cho chi phí trên mỗi đơn vị điện "
      "năng tạo ra, là tỷ lệ giữa các chi phí trong toàn vòng đời và tổng "
      "sản lượng dự kiến, biểu diễn theo giá trị tương đương hiện tại. "
      "Phương pháp này rút ra ưu điểm kinh tế bằng cách so sánh chi phí vòng "
      "đời san đều trung bình tương ứng của chúng.",
      "The cash flow for fuel cycle material and services commences before "
      "the reactor starts to generate electricity and continues well after "
      "the reactor ceases operation. The exact timing of payments for "
      "natural uranium purchase, conversion, enrichment, fabrication, spent "
      "fuel storage, and disposal depends on the associated lead and lag "
      "times for the fuel cycle components. To calculate the overall fuel "
      "cycle cost, the magnitude of each component cost and the appropriate "
      "time that it occurs must be identified. Fuel quantities are obtained "
      "from reactor neutronic calculations as described in Section 2.2.1. "
      "These quantities of materials and services are adjusted to allow for "
      "process losses in the various component stages of the nuclear fuel "
      "cycle and then multiplied by the unit costs to obtain the component "
      "costs. Finally, the total fuel cycle cost is gotten by discounting "
      "these component costs to their present values in a specified base "
      "year (usually the commission date of reactor), as shown in Figure 5. "
      "The levelized lifetime cost methodology provides costs per unit of "
      "electricity generated which are the ratios of lifetime expenses to "
      "total expected output, expressed in terms of the present value "
      "equivalent. This method derives economic merits by comparing their "
      "respective average levelized lifetime costs.")

    FIG(b, 5, F.fig_f05(), lang)

    P(b, lang,
      "Dữ liệu về lò và dữ liệu chi phí chu trình nhiên liệu cho lò HTR lần "
      "lượt được thể hiện trong Bảng 2 và Bảng 3. Bảng 2 đưa thông tin về lò, "
      "gồm công suất, tuổi thọ, chiều dài chu kỳ và các phương án cuối chu "
      "trình. Bảng 3 đưa đơn giá và thời gian dẫn trước hoặc độ trễ cho mua "
      "urani tự nhiên, mua thori, chuyển đổi và làm giàu. Giá của urani tự "
      "nhiên, chuyển đổi và làm giàu lần lượt là giá trung bình trên thị "
      "trường giao ngay từ 2010 đến 2015 (http://www.uxc.com/): 120.9 $/kg U, "
      "8.75 $/kg U và 126.5 $/SWU. Chi phí chế tạo 777 $/kg HM cho các khối "
      "nhiên liệu HTR lấy từ báo cáo của Phòng Thí nghiệm Quốc gia Oak Ridge "
      "(ORNL) [17]. Các giá trị còn lại giống như trong báo cáo của OECD "
      "[16]. Dù các mức tách nhiên liệu khác nhau có thể ảnh hưởng đến đơn "
      "giá liên quan đến chế tạo và, đặc biệt, lưu trữ và xử lý, tỷ phần "
      "của chúng trong tổng chi phí chu trình nhiên liệu là nhỏ, như đã đề "
      "cập trong Phần 3.4. Hơn nữa, phân tích độ nhạy cho thấy sự thay đổi "
      "±50% giá của chế tạo, lưu trữ hoặc xử lý sẽ dẫn đến sự thay đổi không "
      "vượt quá ±5% chi phí chu trình nhiên liệu [18]. Vì vậy, ngay cả khi "
      "các mức tách nhiên liệu khác nhau có giá chế tạo, lưu trữ và xử lý "
      "khác nhau, phân tích trong chương này vẫn còn giá trị.",
      "The reactor data and fuel cycle cost data for the HTR are shown in "
      "Tables 2 and 3, respectively. Table 2 gives the information about "
      "the reactor including the power, lifetime, cycle length, and "
      "back-end options. Table 3 gives the unit price and lead or lag time "
      "for natural uranium purchase, thorium purchase, conversion, and "
      "enrichment. The price of natural uranium, conversion, and enrichment "
      "is the average price of spot market from 2010 to 2015 "
      "(http://www.uxc.com/), respectively: 120.9 $/kg U, 8.75 $/kg U, and "
      "126.5 $/SWU. The fabrication cost of 777 $/kg HM for HTR fuel blocks "
      "comes from the Oak Ridge National Laboratory (ORNL)'s report [17]. "
      "Others are the same as the OECD's report [16]. Although different "
      "fuel separation levels would likely affect unit price related to "
      "fabrication and, in particular, storage, and disposal, their fraction "
      "in total fuel cycle cost is small, as mentioned in Section 3.4. "
      "Moreover, the sensitivity analysis shows that a ±50% variation of "
      "the price of fabrication, storage, or disposal will lead to a "
      "no-more-than ±5% variation of fuel cycle cost [18]. Thus, even if "
      "different fuel separation levels have a different price of "
      "fabrication, storage, and disposal, the analysis in this chapter is "
      "still valid.")

    TBL(b, lang, _T52_HEAD_VI, _T52_HEAD_EN,
        _T52_ROWS_VI if lang == "vi" else _T52_ROWS_EN,
        caption_vi="Bảng 5.2 — Dữ liệu vận hành của lò HTR",
        caption_en="Table 5.2 — Reactor operation data for the HTR")

    TBL(b, lang, _T53_HEAD_VI, _T53_HEAD_EN,
        _T53_ROWS_VI if lang == "vi" else _T53_ROWS_EN,
        caption_vi="Bảng 5.3 — Dữ liệu chi phí chu trình nhiên liệu cho lò HTR",
        caption_en="Table 5.3 — Fuel cycle cost data for the HTR")

    return b
