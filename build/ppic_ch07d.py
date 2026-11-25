# -*- coding: utf-8 -*-
"""Book 9, Chapter 7 (part D) - Tables 7.4 and 7.5 (EN/VI).

Source: work/ppic_raw.txt, absolute lines 4047-4085 (PDF pp. 152-153,
printed pp. 136-137). Both tables are raster images in the PDF; every
cell below is transcribed from the page renders p152.png and p153.png.
Table 7.5 is a 21-column matrix printed as two stacked sub-matrices
('ASSESSMENT OF IMPACT MAGNITUDE' and 'ASSESSMENT OF IMPACT SIGNIFICANCE');
it is emitted as one table with full-width group rows separating the parts.
"""
from ppic_ch07_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

# ------------------------------------------------------------- Table 7.4
_T74_HEAD_VI = ["Lĩnh vực của Chiến lược", "Hoạt động ưu tiên"]
_T74_HEAD_EN = ["Sector of the Strategy", "Priority activities"]

_T74_ROWS_VI = [
    "HỆ THỐNG ĐIỆN LỰC",
    ["", "Tái thiết và loại bỏ các nhà máy nhiệt điện theo Chỉ thị về các "
         "nhà máy đốt lớn"],
    ["", "Nhà máy nhiệt điện than có công suất 700MW vào năm 2025 "
         "(350MW vào năm 2020)"],
    ["", "Nhà máy thủy điện đảo chiều “Bistrica” và/hoặc nhà máy thủy điện "
         "đảo chiều “Djerdap 3”"],
    ["", "Xây dựng các nhà máy kết hợp nhiệt và điện công suất khoảng "
         "450 MW vào năm 2020"],
    "NGUỒN NĂNG LƯỢNG TÁI TẠO",
    ["", "Phát triển các trang trại gió"],
    ["", "Phát triển các nhà máy thủy điện và các nhà máy thủy điện nhỏ"],
    ["", "Phát triển các nhà máy điện sinh khối"],
    ["", "Phát triển các nhà máy điện mặt trời"],
    ["", "Phát triển các nhà máy điện địa nhiệt"],
]

_T74_ROWS_EN = [
    "Electric power system",
    ["", "Reconstruction and withdrawal of thermal power plants pursuant "
         "to Large Combustion Plants Directive"],
    ["", "Coal-fired power plants of capacity of 700MW by 2025 "
         "(350MW by 2020)"],
    ["", "“Bistrica” reversible HPP and/or “Djerdap 3” reversible HPP"],
    ["", "Construction of combined heat and PP's of capacity of approx. "
         "450 MW by 2020"],
    "Renewable energy sources",
    ["", "Development of wind farms"],
    ["", "Development of hydroelectric power plants and small hydro "
         "power plants"],
    ["", "Development of biomass power plants"],
    ["", "Development of solar power plants"],
    ["", "Development of geothermal power plants"],
]

# ------------------------------------------------------------- Table 7.5
_T75_HEAD_VI = ["Ưu tiên chiến lược"] + [str(i) for i in range(1, 22)]
_T75_HEAD_EN = ["Strategic priorities"] + [str(i) for i in range(1, 22)]

# Row labels of the magnitude sub-matrix (as printed on p152).
_MAG_LABELS_EN = [
    "Reconstruction and withdrawal of thermal power plants pursuant to the "
    "Large Combustion Plants Directive",
    "Coal-fired thermal of capacity of 700MW by 2025",
    "“Bistrica” reversible HPP and/or “Djerdap 3” reversible HPP",
    "Development of combined heat and power plants using gas engines of "
    "capacity of approx. 450 MW by 2020",
    "Development of wind farms",
    "Development of HPPs and SHPPs",
    "Development of biomass power plants",
    "Development of solar power plants",
]
_MAG_LABELS_VI = [
    "Tái thiết và loại bỏ các nhà máy nhiệt điện theo Chỉ thị về các nhà "
    "máy đốt lớn",
    "Nhà máy nhiệt điện than có công suất 700MW vào năm 2025",
    "Nhà máy thủy điện đảo chiều “Bistrica” và/hoặc nhà máy thủy điện đảo "
    "chiều “Djerdap 3”",
    "Phát triển các nhà máy kết hợp nhiệt và điện sử dụng động cơ khí có "
    "công suất khoảng 450 MW vào năm 2020",
    "Phát triển các trang trại gió",
    "Phát triển các nhà máy thủy điện và các nhà máy thủy điện nhỏ",
    "Phát triển các nhà máy điện sinh khối",
    "Phát triển các nhà máy điện mặt trời",
]

# Row labels of the significance sub-matrix (as printed on p152; a few
# labels differ slightly from the magnitude sub-matrix - retained verbatim).
_SIG_LABELS_EN = [
    "Reconstruction and withdrawal of thermal power plants pursuant to the "
    "Large Combustion Plants Directive",
    "Coal-fired thermal power plants of capacity of 700MW by 2025",
    "“Bistrica” reversible hydropower plant and/or “Djerdap 3” reversible "
    "HPP",
    "Development of combined heat and power plant using gas engines of "
    "capacity of approx. 450 MW by 2020",
    "Development of wind farms",
    "Development of HPPs and SHPPs",
    "Development of biomass power plants",
    "Development of solar power plants",
]
_SIG_LABELS_VI = [
    "Tái thiết và loại bỏ các nhà máy nhiệt điện theo Chỉ thị về các nhà "
    "máy đốt lớn",
    "Các nhà máy nhiệt điện than có công suất 700MW vào năm 2025",
    "Nhà máy thủy điện đảo chiều “Bistrica” và/hoặc nhà máy thủy điện đảo "
    "chiều “Djerdap 3”",
    "Phát triển nhà máy kết hợp nhiệt và điện sử dụng động cơ khí có công "
    "suất khoảng 450 MW vào năm 2020",
    "Phát triển các trang trại gió",
    "Phát triển các nhà máy thủy điện và các nhà máy thủy điện nhỏ",
    "Phát triển các nhà máy điện sinh khối",
    "Phát triển các nhà máy điện mặt trời",
]

# Assessment of impact magnitude: signed values for objectives 1-21.
_MAG_VALS = [
    ["+3", "+3", "0", "+2", "0", "0", "0", "+1", "0", "+1", "+1", "+1",
     "+1", "0", "+1", "0", "0", "+1", "-1", "+1", "+3"],
    ["0", "0", "0", "-1", "0", "-2", "0", "-1", "0", "+1", "0", "+1",
     "-1", "0", "+2", "+2", "+2", "0", "-1", "0", "+2"],
    ["0", "0", "-3", "-2", "-1", "-2", "-1", "-2", "0", "0", "0", "+1",
     "-1", "0", "+2", "+2", "+3", "-2", "+3", "0", "+3"],
    ["+1", "0", "0", "0", "0", "-1", "0", "0", "0", "0", "0", "+1",
     "0", "0", "+2", "+1", "0", "0", "+2", "0", "+1"],
    ["+3", "0", "-2", "-1", "0", "-1", "-1", "-2", "0", "+2", "+1", "+1",
     "0", "0", "+1", "+1", "+1", "-1", "+3", "0", "+2"],
    ["+3", "0", "-2", "-1", "0", "-1", "-1", "-2", "0", "+2", "+1", "+1",
     "0", "0", "+1", "+1", "+1", "-1", "+3", "0", "+2"],
    ["-1", "0", "0", "0", "0", "0", "0", "0", "0", "+1", "+1", "+1",
     "0", "0", "+1", "+1", "+1", "0", "+3", "0", "+1"],
    ["+3", "0", "0", "-1", "-1", "-1", "0", "0", "0", "0", "+1", "+1",
     "0", "0", "+1", "+1", "+1", "0", "+3", "0", "+3"],
]

# Assessment of impact significance: letters (R/L/I/N) or blank cells.
_SIG_VALS = [
    ["R", "R", "", "L", "", "", "", "L", "", "L", "R", "L",
     "L", "", "L", "", "", "I", "L", "R", "R"],
    ["", "", "", "L", "", "L", "", "L", "", "L", "", "R",
     "L", "", "N", "L", "N", "", "N", "", "R"],
    ["", "", "I", "I", "I", "I", "I", "N", "", "", "", "I",
     "L", "", "N", "L", "N", "I", "N", "", "N"],
    ["L", "", "", "", "", "L", "", "", "", "", "", "L",
     "", "", "L", "L", "", "", "L", "", "L"],
    ["N", "", "I", "L", "", "L", "L", "I", "", "L", "L", "N",
     "", "", "N", "N", "N", "I", "N", "", "N"],
    ["N", "", "I", "L", "", "L", "L", "I", "", "L", "L", "N",
     "", "", "N", "N", "N", "I", "N", "", "N"],
    ["L", "", "", "", "", "", "", "", "", "L", "L", "L",
     "", "", "L", "L", "L", "", "L", "", "L"],
    ["L", "", "", "L", "L", "L", "", "", "", "", "L", "L",
     "", "", "L", "L", "L", "", "L", "", "L"],
]


def _t75_rows(mag_labels, sig_labels, mag_grp, sig_grp, sea_obj):
    """Assemble the two stacked sub-matrices as one table body."""
    rows = [mag_grp, sea_obj]
    rows.extend([label] + vals
                for label, vals in zip(mag_labels, _MAG_VALS))
    rows.append(sig_grp)
    rows.append(sea_obj)
    rows.extend([label] + vals
                for label, vals in zip(sig_labels, _SIG_VALS))
    return rows


_T75_ROWS_VI = _t75_rows(
    _MAG_LABELS_VI, _SIG_LABELS_VI,
    "ĐÁNH GIÁ MỨC ĐỘ TÁC ĐỘNG", "ĐÁNH GIÁ TẦM QUAN TRỌNG CỦA TÁC ĐỘNG",
    "Các mục tiêu SEA")
_T75_ROWS_EN = _t75_rows(
    _MAG_LABELS_EN, _SIG_LABELS_EN,
    "ASSESSMENT OF IMPACT MAGNITUDE", "ASSESSMENT OF IMPACT SIGNIFICANCE",
    "SEA objectives")


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 7."""
    b = []

    TBL(b, lang, _T74_HEAD_VI, _T74_HEAD_EN,
        _T74_ROWS_VI if lang == "vi" else _T74_ROWS_EN,
        caption_vi="Bảng 7.4 · Các ưu tiên chiến lược trong Chiến lược đưa "
                   "vào SEA liên quan đến các dự án nhà máy điện [34]",
        caption_en="Table 7.4 · Strategic priorities in the strategy "
                   "included in the SEA relating to the projects of power "
                   "plants [34]")

    P(b, lang,
      "Bảng 7.4 thể hiện các ưu tiên chiến lược trong Chiến lược có liên quan "
      "trực tiếp đến các dự án nhà máy điện và cũng được đưa vào đánh giá đa "
      "tiêu chí trình bày ở phần sau. Ngoài các ưu tiên này, Chiến lược còn "
      "xác định các ưu tiên liên quan trực tiếp đến nhà máy điện vì thực chất "
      "chúng nằm trong chức năng của các nhà máy này. Điều này bao gồm, ví dụ, "
      "mở rộng các khu khai thác than lộ thiên hiện có và mở các mỏ than lộ "
      "thiên mới cung cấp than cho các nhà máy nhiệt điện. Các ưu tiên chiến "
      "lược này cũng được phân tích trong SEA cho Chiến lược, nhưng không "
      "được trình bày ở đây.",
      "Table 7.4 shows the strategic priorities in the Strategy, which "
      "directly relate to the projects of power plants and which were also "
      "included in the multi-criteria evaluation presented further herein. "
      "In addition to these priorities, the Strategy also formulates "
      "priorities that directly relate to power plants because they are "
      "actually in their function. This includes, for example, the extension "
      "of coal open-pit-mining areas and opening of new coal open-pit mines "
      "which supply thermal power plants with coal. These strategic "
      "priorities were also elaborated in the SEA for the Strategy, but are "
      "not presented herein.")

    P(b, lang,
      "Từng ưu tiên chiến lược riêng lẻ trong Chiến lược liên quan đến các dự "
      "án nhà máy điện (Bảng 7.4) đã được đưa vào quá trình đánh giá đa tiêu "
      "chí bằng cách lập các ma trận (Bảng 7.5), trong đó các ưu tiên nói trên "
      "liên quan đến nhà máy điện ‘giao thoa’ với các mục tiêu và chỉ số SEA "
      "(Bảng 7.1). Chúng được đánh giá theo các nhóm tiêu chí đã được chấp "
      "nhận (Bảng 7.2).",
      "Each individual strategic priority in the Strategy relating to the "
      "projects of power plants (Table 7.4) was included in the "
      "multi-criteria evaluation process by forming matrices (Table 7.5) in "
      "which the mentioned priorities relating to power plants 'intersect' "
      "with the SEA objectives and indicators (Table 7.1). They were "
      "evaluated according to the adopted groups of criteria (Table 7.2).")

    TBL(b, lang, _T75_HEAD_VI, _T75_HEAD_EN,
        _T75_ROWS_VI if lang == "vi" else _T75_ROWS_EN,
        caption_vi="Bảng 7.5 · Ma trận tác động không gian của nhà máy điện "
                   "đến môi trường và phát triển bền vững [34]",
        caption_en="Table 7.5 · Matrices of spatial impacts of power plants "
                   "on the environment and sustainable development [34]")

    NOTE(b, lang,
         "* Tiêu chí theo Bảng 2.",
         "*Criteria according to Table 2.")

    P(b, lang,
      "Các ma trận được lập cho hai nhóm tiêu chí đầu tiên (mức độ và tầm "
      "quan trọng của tác động) vì có thể nhận diện các tác động có ý nghĩa "
      "chiến lược ngay trên cơ sở hai nhóm tiêu chí này, cụ thể là các tác "
      "động mà kết quả đánh giá nằm trong các giá trị đã được chấp nhận và "
      "trình bày tại Bảng 7.3.",
      "The matrices were formed for the first two groups of criteria "
      "(impact magnitude and impact significance) because it is possible to "
      "identify the impacts of strategic importance already based on these "
      "two groups of criteria, namely the impacts where evaluation is within "
      "the values adopted and presented in Table 7.3.")

    P(b, lang,
      "Việc đánh giá các ưu tiên chiến lược mang tính bán định lượng, định "
      "tính và phù hợp với mức độ chi tiết/khái quát hóa đặc trưng của các "
      "văn bản chiến lược như Chiến lược. Đánh giá dựa trên cách tiếp cận quy "
      "hoạch, theo đó các tác động không gian (lãnh thổ) được xem xét, cũng "
      "như các xung đột không gian có thể phát sinh trong tương tác giữa các "
      "hoạt động hiện có và các hoạt động được quy hoạch tại một không gian "
      "cụ thể, không đi sâu vào các khía cạnh kỹ thuật và công nghệ của các "
      "tác động tiềm ẩn mà không thể nhận diện được ở cấp độ quy hoạch này.",
      "The evaluation of strategic priorities was semi-quantitative, "
      "qualitative and aligned with the level of detail/generality that "
      "characterizes the strategic documents such as the Strategy. It was "
      "based on the planning approach through which the spatial "
      "(territorial) impacts were considered, as well as on possible "
      "conflicts in space that can occur in the interaction between the "
      "existing and the planned activities in a specific space without "
      "going into the technical and technological aspects of potential "
      "impacts that are not possible to be identified at this level of "
      "planning.")

    P(b, lang,
      "Sau đó, từng ưu tiên chiến lược riêng lẻ cũng được trình bày dưới dạng "
      "biểu đồ (Hình 7.2) và theo cách dễ hiểu đối với công chúng và những "
      "người ra quyết định, phù hợp với các nguyên tắc của Công ước Aarhus.",
      "Each individual strategic priority was then also presented in the "
      "form of graph (Figure 7.2) and in a way comprehensible to the general "
      "public and decision-makers, this being in accordance with the Arhus "
      "Convention principles.")

    return b
