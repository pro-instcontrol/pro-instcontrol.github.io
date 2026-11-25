# -*- coding: utf-8 -*-
"""Book 9, Chapter 5 (part B) — block-type HTRs, fuel geometry, the four
spatial separation levels and the two-step calculation scheme (EN/VI).

Source: decoded lines 2578-2700 of ``work/ppic_raw.txt`` (PDF pp. 98-102,
printed pp. 82-86). Contains Figures 1-4 and Table 5.1; the source prints
all eight values and all column heads of that table. No numbered equation
occurs in this range. The final paragraph of the source ends mid-sentence
("295-"); it is completed from the following printed line so the text is
not left broken. Figures 1-4 are supplied by ``ppicfig5_a``.
"""
import ppicfig5 as F
from ppic_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401

# The figure supplier may not be integrated yet. Neutral bilingual
# placeholders keep section() callable in a partial build; any figure
# already registered by the real supplier is left untouched.
if not all(hasattr(F, "fig_f%02d" % n) for n in range(1, 5)):
    from ppicfig5_common import _mk

    _PLACEHOLDERS = [
        (1, "Lò HTR chạy nhiên liệu thori và khối nhiên liệu",
         "Thorium-fueled HTR and fuel block",
         "Sơ đồ lõi lò dạng vành khăn và khối nhiên liệu.",
         "Annular reactor core and fuel block schematic."),
        (2, "Bốn mức tách không gian",
         "Four levels of spatial separation",
         "Sơ đồ bốn mức tách thori và urani trong lò HTR kiểu khối.",
         "Four levels of thorium/uranium separation in a block-type HTR."),
        (3, "Mô hình tính toán lõi lò cho 1/6 lõi",
         "Reactor core calculation model for 1/6 core",
         "Mô hình lõi lò một phần sáu dùng trong tính toán.",
         "One-sixth core calculation model."),
        (4, "Sơ đồ tính toán hai bước",
         "Schematic diagram of the two-step calculation scheme",
         "Sơ đồ các bước tính toán khối và lõi đầy đủ.",
         "Block and full-core calculation steps."),
    ]
    for _n, _cvi, _cen, _avi, _aen in _PLACEHOLDERS:
        _name = "fig_f%02d" % _n
        if not hasattr(F, _name):
            setattr(F, _name,
                    lambda _t=_mk(_n, [], _cvi, _cvi, _cen,
                                  _avi, _aen): _t)

# ------------------------------------------------------------- Table 5.1
# Printed columns: parameter, width across flat, block height, fuel
# channels, coolant channels, kernel diameter, TRISO thickness and density.
_T51_HEAD_VI = [
    "Thông số",
    "Chiều rộng qua mặt phẳng [cm]",
    "Chiều cao của khối [cm]",
    "Đường kính/số kênh nhiên liệu [cm/−]",
    "Đường kính/số kênh làm mát [cm/−]",
    "Đường kính hạt nhân [μm]",
    "Chiều dày các lớp TRISO [μm]",
    "Tỷ trọng các lớp TRISO [g/cm³]",
]
_T51_HEAD_EN = [
    "Parameters",
    "Width across flat [cm]",
    "Height of block [cm]",
    "Diameter/number of fuel channels [cm/−]",
    "Diameter/number of coolant channels [cm/−]",
    "Diameter of kernels [μm]",
    "Thickness of TRISO layers [μm]",
    "Density of TRISO layers [g/cm³]",
]
_T51_ROWS = [
    ["Values", "36", "79.3", "1.27/210", "1.588/102, 1.27/6",
     "500", "100/35/35/40", "1.05/1.9/3.2/1.9"],
]


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 5."""
    b = []

    # ------------------------------------------------------- main section
    H(b, lang,
      "LÒ HTR KIỂU KHỐI VÀ PHƯƠNG PHÁP TÍNH TOÁN",
      "BLOCK-TYPE HTRS AND CALCULATION METHODOLOGIES", level=2)
    H(b, lang,
      "Lò HTR kiểu khối và các mức tách không gian",
      "Block-Type HTRs and Spatial Separation Levels", level=3)
    H(b, lang, "Lò HTR kiểu khối", "Block-Type HTRs", level=4)

    P(b, lang,
      "Các lò HTR kiểu khối dạng mô-đun [12] là một loại lò phản ứng an toàn "
      "bản chất, thải nhiệt phân rã một cách thụ động bằng đối lưu tự nhiên, "
      "dẫn nhiệt và bức xạ từ lõi lò, đồng thời giữ nhiên liệu không bị hư "
      "hỏng. Như đã đề cập trong Phần 1, lò HTR kiểu khối là lựa chọn tốt hơn "
      "cho nhiên liệu gốc thori vì đạt cháy sâu cao hơn và phổ neutron cứng "
      "hơn. Hơn nữa, một ưu điểm của lò HTR kiểu khối so với lò HTR giường sỏi "
      "là loại trước cung cấp sự phân bố không gian cố định ở nhiều cấp của "
      "nhiên liệu thori/urani trong lõi lò.",
      "Modular block-type HTRs [12] are one kind of inherently safe reactors, "
      "which passively remove decay heat by natural convection, conduction, "
      "and radiation from the reactor core and keep the fuel intact. As "
      "mentioned in Section 1, block-type HTRs are a better choice for "
      "thorium-based fuel for higher burnup and harder neutron spectrum. "
      "Moreover, an advantage of block-type HTRs over pebble-bed HTRs is that "
      "the former provides multi-level and fixed spatial distribution of "
      "thorium/uranium fuels in the reactor cores.")

    P(b, lang,
      "Lõi lò của các HTR kiểu khối được nghiên cứu, như thể hiện trong Hình "
      "1(a), gồm một vùng nhiên liệu dạng vành khăn, các bộ phản xạ trong và "
      "các bộ phản xạ ngoài. Vùng nhiên liệu dạng vành khăn gồm 1980 khối "
      "nhiên liệu, như thể hiện trong Hình 1(b). Các khối nhiên liệu được xếp "
      "chặt lên nhau thành các cột tạo thành một vành khăn giữa bộ phản xạ "
      "trong và bộ phản xạ ngoài; cả hai đều gồm các vòng khối grafite không "
      "chứa nhiên liệu. Cấu hình lõi dạng vành khăn đảm bảo công suất nhiệt "
      "cao hơn và tính an toàn bản chất trong hầu hết các điều kiện sự cố và "
      "quá độ. Mỗi khối nhiên liệu gồm 210 kênh nhiên liệu, 108 kênh làm mát "
      "và 6 kênh chứa chất độc cháy được cố định; các kênh này được lấp đầy "
      "bằng grafite trong các tính toán tiếp theo. Các viên nén nhiên liệu "
      "hình trụ được xếp chồng bên trong các kênh khoan trên các khối grafite "
      "hình lục giác. Các thông số hình học khác của khối nhiên liệu được "
      "liệt kê trong Bảng 1.",
      "The reactor core of the block-type HTRs investigated, as shown in "
      "Figure 1(a), is comprised of an annular fuel zone, inner reflectors, "
      "and outer reflectors. The annular fuel zone is comprised of 1980 fuel "
      "blocks, as shown in Figure 1(b). The fuel blocks are stacked firmly "
      "against each other in columns that form an annulus between an inner "
      "and an outer reflector, both of which consist of rings of unfueled "
      "graphite blocks. The annular core configuration ensures higher "
      "thermal power and inherent safety under most accidents and transient "
      "conditions. Each fuel block includes 210 fuel channels, 108 coolant "
      "channels, and 6 fixed burnable poison channels which are filled with "
      "graphite in the flowing calculations. The cylindrical fuel compacts "
      "are stacked inside channels drilled into hexagonal graphite blocks. "
      "Other geometrical parameters of the fuel blocks are listed in "
      "Table 1.")

    FIG(b, 1, F.fig_f01(), lang)

    TBL(b, lang, _T51_HEAD_VI, _T51_HEAD_EN, _T51_ROWS,
        caption_vi="Bảng 5.1 — Thông số hình học cơ bản của khối nhiên liệu "
                   "trong lò HTR",
        caption_en="Table 5.1 — Basic geometrical parameters of fuel blocks "
                   "in the HTR")

    P(b, lang,
      "Đặc điểm nổi bật nhất của lò HTR kiểu khối là việc sử dụng các hạt đẳng "
      "hướng ba cấu trúc (TRISO), gồm năm lớp từ trong ra ngoài: hạt nhân "
      "nhiên liệu, lớp đệm cacbon xốp, cacbon pirolit trong (IPyC), cacbua "
      "silic (SiC) và cacbon pirolit ngoài (OPyC). Lớp đệm cacbon xốp được "
      "bố trí để bảo vệ PyC đặc khỏi hư hại do giật lù phân hạch và tạo thể "
      "tích trống nhằm hạn chế áp suất khí phân hạch. PyC đặc có độ ổn định "
      "dưới chiếu xạ tốt và khả năng giữ nguyên vẹn để giữ lại sản phẩm phân "
      "hạch trong các điều kiện phơi nhiễm nghiêm trọng. Nằm giữa hai lớp PyC, "
      "lớp SiC đảm nhiệm việc giữ các sản phẩm phân hạch kim loại và cung cấp "
      "độ bền cơ học. Các hạt nhiên liệu TRISO được trộn và kết dính với ma "
      "trận grafite để tạo thành các viên nén nhiên liệu. Hình 2 minh họa "
      "cách các hạt TRISO được đóng gói vào lõi dạng vành khăn.",
      "The most prominent feature of block-type HTRs is use of "
      "tristructural-isotropic (TRISO) particles, which contain five layers "
      "from inside to outside: fuel kernel, porous carbon buffer, inner "
      "pyrolytic carbon (IPyC), silicon carbide (SiC), and outer pyrolytic "
      "carbon (OPyC). The porous carbon buffer layer is provided to protect "
      "the dense PyC from fission recoil damage and to provide void volume "
      "to limit the fission gas pressure. The dense PyC has good irradiation "
      "stability and capability to remain intact to perform fission "
      "production retention under severe exposure conditions. Sandwiched "
      "between the two PyC layers, the SiC layer provides metallic fission "
      "production retention and mechanical strength. TRISO fuel particles "
      "are blended and bonded together with a graphite matrix to form fuel "
      "compacts. Figure 2 illustrates how the TRISO particles are packaged "
      "into the annular core.")

    FIG(b, 2, F.fig_f02(), lang)

    # ------------------------------------- definition of multiscale levels
    H(b, lang,
      "Định nghĩa sự tách không gian đa cấp",
      "Definition of Multiscale Spatial Separation", level=3)
    P(b, lang,
      "Khi sử dụng thori trong lò HTR, có hai yếu tố quan trọng ảnh hưởng đến "
      "hiệu năng hạt nhân. Một là hàm lượng thori (tỷ lệ khối lượng của Th-232 "
      "so với tất cả các đồng vị kim loại nặng), tức tỷ lệ pha trộn giữa thori "
      "và urani. Yếu tố kia là mức tách không gian của thori và urani, tức cách "
      "thức thori và urani được pha trộn. Theo mức tách không gian, trong lò "
      "HTR kiểu khối có bốn mức:",
      "When using thorium in HTRs, two important factors influence nuclear "
      "performance. One is the thorium content (the mass ratio of Th-232 to "
      "all heavy metal isotopes), meaning the mixed proportion of thorium "
      "and uranium. The other is the spatial separation level of thorium and "
      "uranium, meaning how thorium and uranium are to be mixed. According "
      "to the level of spatial separation, four levels are in a block-type "
      "HTR:")
    L(b, lang,
      ["Không tách (mức Th/U MOX): với nhiên liệu Th/U MOX, thori và urani "
       "được trộn trong từng hạt nhân nhiên liệu dưới dạng (Th,U)O₂, như thể "
       "hiện trong Hình 2(a). Thori và urani không tách ở cấp vĩ mô.",
       "Tách ở cấp TRISO (mức SBT): UO₂ và ThO₂ được chế tạo thành các hạt "
       "nhiên liệu TRISO riêng biệt (TRISO UO₂ và TRISO ThO₂), nhưng hai loại "
       "hạt nhiên liệu TRISO này lại được trộn vào cùng một viên nén nhiên "
       "liệu, như thể hiện trong Hình 2(b).",
       "Tách ở cấp kênh (mức SBU): mỗi kênh nhiên liệu chỉ chứa một loại viên "
       "nén nhiên liệu (viên nén UO₂ hoặc viên nén ThO₂), nhưng một khối "
       "nhiên liệu lại có cả kênh nhiên liệu UO₂ và kênh nhiên liệu ThO₂, như "
       "thể hiện trong Hình 2(c).",
       "Tách ở cấp khối (mức WASB): mỗi khối nhiên liệu chỉ chứa một loại "
       "nhiên liệu (UO₂ hoặc ThO₂), nhưng lõi lò lại có cả khối nhiên liệu "
       "UO₂ và khối nhiên liệu ThO₂, như thể hiện trong Hình 2(d)."],
      ["No separation (Th/U MOX level): with Th/U MOX fuel, the thorium and "
       "uranium are mixed in each fuel kernel as a form of (Th,U)O₂, as "
       "shown in Figure 2(a). Thorium and uranium do not separate in the "
       "macrolevel.",
       "TRISO-level separation (SBT level): UO₂ and ThO₂ are made into "
       "different TRISO fuel particles (UO₂ TRISO and ThO₂ TRISO) "
       "separately, but the two kinds of TRISO fuel particles are mixed into "
       "the same fuel compact, as shown in Figure 2(b).",
       "Channel-level separation (SBU level): each fuel channel has only one "
       "kind of fuel compacts (UO₂ fuel compacts or ThO₂ fuel compacts), but "
       "a fuel block has both UO₂ fuel channels and ThO₂ fuel channels, as "
       "shown in Figure 2(c).",
       "Block-level separation (WASB level): each fuel block only has a kind "
       "of fuel (UO₂ or ThO₂), but the core has both UO₂ fuel blocks and "
       "ThO₂ fuel blocks, as shown in Figure 2(d)."],
      ordered=True)

    # ------------------------------------- calculation and evaluation
    H(b, lang,
      "Phương pháp tính toán và đánh giá",
      "Calculation and Evaluation Methods", level=3)
    H(b, lang,
      "Phương pháp tính toán neutron học",
      "Neutronic Calculation Method", level=4)
    P(b, lang,
      "Để chỉ phân tích riêng ảnh hưởng của sự tách không gian, các thông số "
      "khác được giữ nguyên, gồm hình học khối nhiên liệu như liệt kê trong "
      "Bảng 1 và sơ đồ đảo nhiên liệu như thể hiện trong Hình 3. Một phép tính "
      "vận chuyển 3D toàn lõi chi tiết trong một bước sẽ đòi hỏi bộ nhớ và "
      "thời gian đơn vị xử lý trung tâm (CPU) đáng kể, ngay cả đối với các cơ "
      "sở sản xuất hay phòng thí nghiệm phục vụ thiết kế. Do đó, sơ đồ tính "
      "toán hai bước là điển hình: (1) một phép tính chi tiết ở cấp cụm với "
      "điều kiện biên phản xạ, cho các tiết diện đã đồng nhất hóa của cụm, "
      "được thu gọn đến một số nhóm nhất định (bước tính toán mạng), và (2) "
      "phép tính thứ hai ở cấp lõi với các thuộc tính đã đồng nhất hóa trong "
      "mỗi cụm và thường là số nhóm nhỏ (bước tính toán toàn lõi).",
      "To only analyze the influence of spatial separation, the other "
      "parameters are kept the same including the fuel block geometry, as "
      "listed in Table 1, and the fuel shuffling scheme, as shown in "
      "Figure 3. A detailed full-core 3D transport calculation in one step "
      "will require significant memory and a central processing unit (CPU) "
      "time as utilities in producing calculations or even in laboratories "
      "for design purposes. Therefore, a two-step calculation scheme is "
      "typical: (1) a detailed calculation at the assembly level with "
      "reflective boundary conditions, which gives homogenized "
      "cross-sections for the assemblies, condensed to a certain number of "
      "groups (lattice calculation step) and (2) a second calculation at the "
      "core level with homogenized properties in each assembly and usually "
      "small number of groups (full-core calculation step).")

    FIG(b, 3, F.fig_f03(), lang)

    P(b, lang,
      "Trong chương này, sơ đồ tính toán hai bước truyền thống được xây dựng "
      "dựa trên hệ mã DRAGON V4 [13], như thể hiện trong Hình 4. Một đặc điểm "
      "hấp dẫn của mã DRAGON là khả năng xử lý nhiên liệu dạng hạt trong ma "
      "trận grafite trong một phép tính toàn cụm. Mã này cho phép xác định hỗn "
      "hợp ngẫu nhiên các cấu trúc vi mô dạng cầu có thể được phân bố bên "
      "trong các hỗn hợp phức hợp của hình học vĩ mô hiện tại, dùng mô hình "
      "bất đồng nhất kép Hebert [14] hoặc mô hình bất đồng nhất kép "
      "Sanchez-Pogroming [15].",
      "In this chapter, the traditional two-step calculation scheme is "
      "constructed based on the DRAGON V4 code system [13], as shown in "
      "Figure 4. An attractive feature of the DRAGON code is its ability to "
      "treat particle fuel in a graphite matrix in a full-assembly "
      "calculation. It provides the possibility to define a stochastic "
      "mixture of spherical micro-structures that can be distributed inside "
      "composite mixtures of the current macro-geometry using the Hebert "
      "double-heterogeneity model [14] or Sanchez-Pogroming "
      "double-heterogeneity model [15].")

    FIG(b, 4, F.fig_f04(), lang)

    P(b, lang,
      "Ở bước (a) trong Hình 4, một khối nhiên liệu 2D được mô hình hóa bao "
      "gồm cả cấu trúc của hạt TRISO. Phương pháp đặc trưng (MOC) và thư viện "
      "tiết diện 295 nhóm (http://www.polymtl.ca/merlin/libraries.htm) được "
      "dùng để giải phương trình vận chuyển.",
      "In step (a) in Figure 4, a 2D fuel block is modeled including the "
      "structure of the TRISO particle. The method of characteristics (MOC) "
      "and the 295-group cross-section library "
      "(http://www.polymtl.ca/merlin/libraries.htm) are used to solve the "
      "transport equation.")

    return b
