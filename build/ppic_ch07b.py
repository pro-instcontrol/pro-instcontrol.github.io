# -*- coding: utf-8 -*-
"""Book 9, Chapter 7 (part B) - Figure 7.1 and Tables 7.1-7.3 (EN/VI).

Source: work/ppic_raw.txt, absolute lines 3897-3906 (PDF pp. 145-148,
printed pp. 129-132). The figure and all three tables are raster images in
the PDF; every cell, sign, percentage and unit below is transcribed from the
page renders p145.png-p148.png. Table 7.1 spans two printed pages.

Figure 7.1 is supplied by ``ppicfig7``. A neutral bilingual placeholder keeps
section() callable before the supplier module is integrated; any callable
already registered by the real supplier is left untouched.
"""
try:
    import ppicfig7 as F
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

from ppic_ch07_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

if not hasattr(F, "fig_f71"):
    _STUB_SVG = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 90" '
        'role="img"><rect x="1" y="1" width="678" height="88" rx="6" '
        'fill="#f4f6fa" stroke="#9aa7bd"/>'
        '<text x="340" y="38" text-anchor="middle" '
        'style="font:15px Helvetica,sans-serif;fill:#24364f">'
        'Procedure and methodological framework for the SEA</text>'
        '<text x="340" y="63" text-anchor="middle" '
        'style="font:12px Helvetica,sans-serif;fill:#5a6b82">'
        'Hình 7.1 / Figure 7.1</text></svg>'
    )
    _STUB_F71 = (
        _STUB_SVG,
        "Hình 7.1 · Quy trình và khung phương pháp luận cho SEA",
        "Figure 7.1 · Procedure and methodological framework for the SEA",
        "Sơ đồ quy trình và khung phương pháp luận của đánh giá môi trường "
        "chiến lược.",
        "Flowchart of the procedure and methodological framework for the "
        "strategic environmental assessment.")
    setattr(F, "fig_f71", lambda _t=_STUB_F71: _t)

# ------------------------------------------------------------- Table 7.1
# Printed Table 1: SEA objectives and indicators for the Strategy [34].
# Group labels are strings -> rendered as full-width group rows by C.table().
_T71_HEAD_VI = ["Mục tiêu SEA cụ thể", "Chỉ số"]
_T71_HEAD_EN = ["Specific SEA objectives", "Indicators"]

_T71_ROWS_VI = [
    "KHÔNG KHÍ",
    ["- Giảm phát thải các chất ô nhiễm không khí đến mức phát thải quy định",
     "- Phát thải hạt, và phát thải SO₂ và NOₓ<br>"
     "- Tần suất vượt giá trị giới hạn hàng ngày đối với bồ hóng, SO₂ và NO₂<br>"
     "- Thay đổi phát thải khí nhà kính, chủ yếu là CO₂ (%)<br>"
     "- Tăng tỷ trọng RES trong cân bằng năng lượng (%)"],
    "NƯỚC",
    ["- Giảm ô nhiễm nước mặt và nước ngầm đến mức không làm ảnh hưởng đến "
     "chất lượng của chúng<br>"
     "- Giảm thiểu tác động tiêu cực của các cơ sở năng lượng đến chế độ thủy văn",
     "- BOD và COD ở các dòng nước chịu ảnh hưởng của các cơ sở và hoạt động "
     "năng lượng<br>"
     "- Thay đổi nhiệt độ ở các dòng nước<br>"
     "- Thay đổi chế độ nước<br>"
     "- Thay đổi cấp chất lượng nước (%)<br>"
     "- Nước được tái sử dụng và tái chế do hoạt động của ngành năng lượng (m³)"],
    "ĐẤT",
    ["- Bảo vệ đất nông nghiệp và đất lâm nghiệp<br>"
     "- Giảm suy thoái đất và xói mòn",
     "- Thay đổi độ che phủ rừng (%)<br>"
     "- Thay đổi diện tích đất nông nghiệp (%)<br>"
     "- Tỷ lệ diện tích suy thoái do các hoạt động trong lĩnh vực năng lượng (%)<br>"
     "- Diện tích đất bị đe dọa bởi các quá trình xói mòn đất (ha)"],
    "GIÁ TRỊ TỰ NHIÊN",
    ["Mục tiêu SEA cụ thể", "Chỉ số"],
    ["- Bảo vệ cảnh quan<br>"
     "- Bảo vệ các giá trị và khu vực tự nhiên<br>"
     "- Bảo tồn đa dạng sinh học – tránh những tổn thất không thể đảo ngược",
     "- Tỷ lệ diện tích được phục hồi trong tổng diện tích các vùng suy thoái (%)<br>"
     "- Số cơ sở năng lượng có thể gây thay đổi cảnh quan<br>"
     "- Diện tích của tất cả các khu vực tự nhiên được bảo vệ có thể bị ảnh hưởng<br>"
     "- Số loài thực vật và động vật quý hiếm có thể bị ảnh hưởng"],
    "DI SẢN VĂN HÓA VÀ LỊCH SỬ",
    ["- Bảo vệ các tài sản văn hóa",
     "- Số lượng và tầm quan trọng của các tài sản văn hóa bất động được bảo "
     "vệ có thể bị ảnh hưởng"],
    "CHẤT THẢI",
    ["- Cải thiện việc tận dụng, xử lý và tiêu hủy chất thải",
     "- Tổng lượng chất thải phát sinh hàng năm trong ngành năng lượng (t)<br>"
     "- % tổng lượng chất thải được tái sử dụng, tái chế và xử lý"],
    "SỨC KHỎE DÂN CƯ",
    ["- Giảm tác động tiêu cực của ngành công nghiệp năng lượng đến sức khỏe "
     "con người",
     "- Tần suất mắc các bệnh hô hấp (%) gần các cơ sở năng lượng<br>"
     "- Tần suất các bệnh có thể liên quan đến hoạt động năng lượng<br>"
     "- Số người bị ảnh hưởng bởi tiếng ồn do các cơ sở năng lượng phát sinh"],
    "PHÁT TRIỂN XÃ HỘI",
    ["- Chất lượng cuộc sống tốt hơn<br>"
     "- Duy trì mật độ dân số ở các khu vực nông thôn",
     "- Cải thiện hiệu quả năng lượng trong các tòa nhà dân cư (%)<br>"
     "- Số hộ gia đình bị di dời do hoạt động năng lượng"],
    "PHÁT TRIỂN THỂ CHẾ",
    ["- Cải thiện dịch vụ bảo vệ, quản lý và kiểm soát môi trường",
     "- Số điểm đo trong hệ thống giám sát"],
    "PHÁT TRIỂN KINH TẾ",
    ["- Khuyến khích phát triển kinh tế<br>"
     "- Thúc đẩy việc làm tại địa phương<br>"
     "- Giảm phụ thuộc vào nguồn năng lượng nhập khẩu<br>"
     "- Giảm các tác động môi trường tiêu cực xuyên biên giới",
     "- % số người làm việc trong ngành năng lượng có mức lương cao hơn lương "
     "trung bình<br>"
     "- Giảm số người thất nghiệp nhờ tăng trưởng việc làm trong ngành năng "
     "lượng (%)<br>"
     "- Số chương trình bảo vệ môi trường cho phát triển ngành năng lượng<br>"
     "- Số cơ sở năng lượng IPPC có tác động xuyên biên giới"],
    "TÀI NGUYÊN TỰ NHIÊN",
    ["- Sử dụng hợp lý các nguồn năng lượng không tái tạo và tăng sử dụng "
     "năng lượng tái tạo<br>"
     "- Nâng cao hiệu quả năng lượng<br>"
     "- Áp dụng công nghệ sạch hơn",
     "- Tiêu thụ năng lượng cuối cùng trên đầu người<br>"
     "- Tỷ trọng nguồn năng lượng tái tạo trong tổng sử dụng năng lượng<br>"
     "- Cải thiện hiệu quả năng lượng (% giảm tiêu thụ năng lượng)"],
]

_T71_ROWS_EN = [
    "AIR",
    ["- Reducing air pollutant emissions to prescribed emission levels",
     "- Particle emissions, and SO₂ and NOₓ emissions<br>"
     "- Frequency of exceeding the daily limit values for soot, SO₂ and NO₂<br>"
     "- Changes in greenhouse gas emissions, primarily in CO₂ (%)<br>"
     "- Increase of RES share in energy balance (%)"],
    "WATER",
    ["- Reducing surface and groundwater pollution to the level that will "
     "not affect their quality<br>"
     "- Mitigating negative effects of energy facilities on hydrological regimes",
     "- BOD and COD in watercourses affected by energy facilities and "
     "activities<br>"
     "- Temperature changes in watercourses<br>"
     "- Changes in water regimes<br>"
     "- Changes in water quality class (%)<br>"
     "- Reused and recycled water as a result of energy sector activities (m³)"],
    "SOIL",
    ["- Protection of agricultural and forestry land<br>"
     "- Reducing soil degradation and erosion",
     "- Changes in forest cover (%)<br>"
     "- Changes in agricultural land area (%)<br>"
     "- Share of degraded areas as a result of activities in the field of "
     "energy (%)<br>"
     "- Land area threatened by soil erosion processes (ha)"],
    "NATURAL VALUES",
    ["Specific SEA objectives", "Indicators"],
    ["- Landscape protection<br>"
     "- Protection of natural values and areas<br>"
     "- Biodiversity conservation – avoid irreversible losses",
     "- Share of re-cultivated areas in the overall area of degraded regions (%)<br>"
     "- The number of energy facilities that may cause landscape changes<br>"
     "- The area of all protected natural areas that may be affected<br>"
     "- Number of endangered flora and fauna that may be affected"],
    "CULTURAL AND HISTORIC HERITAGE",
    ["- Cultural properties protection",
     "- Number and importance of protected immoveable cultural properties "
     "that may be affected"],
    "WASTE",
    ["- Improving waste utilization, treatment and disposal",
     "- Total annual amount of waste generated in energy sector (t)<br>"
     "- % of total amount of waste subject to re-use, recycling and treatment"],
    "POPULATION HEALTH",
    ["- Reducing negative effects of energy industry on human health",
     "- Frequency of respiratory diseases (%) close to energy facilities<br>"
     "- Frequency of diseases which can be associated with energy activities<br>"
     "- Number of people affected by noise generated by energy facilities"],
    "SOCIAL DEVELOPMENT",
    ["- Better quality of life<br>"
     "- Preservation of population density in rural areas",
     "- Improvement of energy efficiency in residential buildings (%)<br>"
     "- Number of households displaced as a result of energy activities"],
    "INSTITUTIONAL DEVELOPMENT",
    ["- Improve environmental protection and management and control services",
     "- Number of measuring points in monitoring system"],
    "ECONOMIC DEVELOPMENT",
    ["- Encouraging economic development<br>"
     "- Promote local employment<br>"
     "- Reducing dependency on sources of imported energy<br>"
     "- Reducing transboundary negative environmental impacts",
     "- % of employed in the energy sector with salary above the average "
     "salary<br>"
     "- Reduction in number of unemployed as a result of growth in the "
     "energy sector employment (%)<br>"
     "- Number of environmental protection programs for energy sector "
     "development<br>"
     "- Number of IPPC energy facilities with transboundary impacts"],
    "NATURAL RESOURCES",
    ["- Rational use of non RES and increasing the use of RES<br>"
     "- Improving energy efficiency<br>"
     "- Introducing cleaner technologies",
     "- Final energy consumption per capita<br>"
     "- Share of renewable energy sources in total energy use<br>"
     "- Improvements in energy efficiency (% of reduction in energy use)"],
]

# ------------------------------------------------------------- Table 7.2
# Printed Table 2: SEA evaluation criteria for the Strategy [34].
_T72_HEAD_VI = ["Cường độ tác động", "Ký hiệu", "Mô tả"]
_T72_HEAD_EN = ["Impact magnitude", "Designation", "Description"]

_T72_ROWS_VI = [
    ["Nghiêm trọng", "-3", "Quá tải môi trường đáng kể"],
    ["Lớn", "-2", "Xáo trộn môi trường ở mức lớn"],
    ["Nhỏ", "-1", "Xáo trộn môi trường ở mức nhỏ"],
    ["Không có tác động", "0", "Không có tác động môi trường trực tiếp "
     "và/hoặc không rõ ràng"],
    ["Tích cực", "+1", "Những thay đổi tích cực nhỏ về môi trường"],
    ["Thuận lợi", "+2", "Những thay đổi môi trường thuận lợi"],
    ["Rất thuận lợi", "+3", "Những thay đổi cải thiện đáng kể chất lượng "
     "cuộc sống"],
    ["Ý nghĩa tác động", "Ký hiệu", "Mô tả"],
    ["Quốc tế", "I", "Tác động xuyên biên giới có thể xảy ra"],
    ["Quốc gia", "N", "Tác động có thể xảy ra ở cấp quốc gia"],
    ["Khu vực", "R", "Tác động có thể xảy ra ở cấp khu vực"],
    ["Địa phương", "L", "Tác động có thể xảy ra ở cấp địa phương"],
    ["Xác suất", "Ký hiệu", "Mô tả"],
    ["100%", "S", "Tác động chắc chắn xảy ra"],
    ["Hơn 50%", "L", "Tác động có khả năng xảy ra"],
    ["Ít hơn 50%", "P", "Tác động có thể xảy ra"],
]

_T72_ROWS_EN = [
    ["Critical", "-3", "Significant environmental overload"],
    ["Greater", "-2", "Environmental disturbance of great extent"],
    ["Smaller", "-1", "Environmental disturbance of smaller extent"],
    ["No impact", "0", "No direct and/or unclear environmental impact"],
    ["Positive", "+1", "Smaller positive environmental changes"],
    ["Favourable", "+2", "Favourable environmental changes"],
    ["Very favourable", "+3", "Changes that significantly improve the "
     "quality of life"],
    ["Impact significance", "Designation", "Description"],
    ["International", "I", "Possible transboundary impact"],
    ["National", "N", "Possible impact at the national level"],
    ["Regional", "R", "Possible impact at the regional level"],
    ["Local", "L", "Possible impact of local character"],
    ["Probability", "Designation", "Description"],
    ["100%", "S", "Impact will definitely occur"],
    ["More than 50%", "L", "Likely impact"],
    ["Less than 50%", "P", "Possible impact"],
]

# ------------------------------------------------------------- Table 7.3
# Printed Table 3: SEA criteria for evaluating strategically significant
# impacts of the Strategy [34]. The first printed column holds a level label
# merged across four rows, rendered here as a group row per level.
_T73_HEAD_VI = ["Cấp độ", "Cường độ tác động", "Ký hiệu tác động có ý nghĩa"]
_T73_HEAD_EN = ["Level", "Impact magnitude", "Designation of significant impacts"]

_T73_ROWS_VI = [
    "Mức quốc tế: I",
    ["Tác động tích cực mạnh", "+3", "I+3"],
    ["Tác động tích cực lớn", "+2", "I+2"],
    ["Tác động tiêu cực mạnh", "-3", "I-3"],
    ["Tác động tiêu cực lớn", "-2", "I-2"],
    "Mức quốc gia: N",
    ["Tác động tích cực mạnh", "+3", "N+3"],
    ["Tác động tích cực lớn", "+2", "N+2"],
    ["Tác động tiêu cực mạnh", "-3", "N-3"],
    ["Tác động tiêu cực lớn", "-2", "N-2"],
    "Mức khu vực: R",
    ["Tác động tích cực mạnh", "+3", "R+3"],
    ["Tác động tích cực lớn", "+2", "R+2"],
    ["Tác động tiêu cực mạnh", "-3", "R-3"],
    ["Tác động tiêu cực lớn", "-2", "R-2"],
]

_T73_ROWS_EN = [
    "International level: I",
    ["Strong positive impact", "+3", "I+3"],
    ["Greater positive impact", "+2", "I+2"],
    ["Strong negative impact", "-3", "I-3"],
    ["Greater negative impact", "-2", "I-2"],
    "National level: N",
    ["Strong positive impact", "+3", "N+3"],
    ["Greater positive impact", "+2", "N+2"],
    ["Strong negative impact", "-3", "N-3"],
    ["Greater negative impact", "-2", "N-2"],
    "Regional level: R",
    ["Strong positive impact", "+3", "R+3"],
    ["Greater positive impact", "+2", "R+2"],
    ["Strong negative impact", "-3", "R-3"],
    ["Greater negative impact", "-2", "R-2"],
]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 7."""
    b = []

    FIG(b, 1, F.fig_f71(), lang)

    TBL(b, lang, _T71_HEAD_VI, _T71_HEAD_EN,
        _T71_ROWS_VI if lang == "vi" else _T71_ROWS_EN,
        caption_vi="Bảng 7.1 · Mục tiêu và chỉ số SEA cho Chiến lược [34]",
        caption_en="Table 7.1 · SEA objectives and indicators for the "
                   "Strategy [34]")

    TBL(b, lang, _T72_HEAD_VI, _T72_HEAD_EN,
        _T72_ROWS_VI if lang == "vi" else _T72_ROWS_EN,
        caption_vi="Bảng 7.2 · Tiêu chí đánh giá SEA cho Chiến lược [34]",
        caption_en="Table 7.2 · SEA evaluation criteria for the Strategy [34]")

    TBL(b, lang, _T73_HEAD_VI, _T73_HEAD_EN,
        _T73_ROWS_VI if lang == "vi" else _T73_ROWS_EN,
        caption_vi="Bảng 7.3 · Tiêu chí SEA đánh giá các tác động có ý nghĩa "
                   "chiến lược của Chiến lược [34]",
        caption_en="Table 7.3 · SEA criteria for evaluating strategically "
                   "significant impacts of the Strategy [34]")

    return b
