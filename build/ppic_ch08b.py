# -*- coding: utf-8 -*-
"""Book 9, Chapter 8 (part B) -- OPTIMIZATION METHOD AND DESIGN OF
EXPERIMENTAL MODEL (EN/VI bilingual).

Source: Ling-Yun Peng, Ying-Jie Kang, Zong-Rui Lai and Yu-Ke Deng, in
L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and Control*
(Bibliotex, 2019), PDF pp. 172-176, printed pp. 156-160 (absolute lines
4675-4769 of work/ppic_raw.txt).

Covers the parameter optimization of the coal bucket damper (CBD) structure
(Figure 1), the displacement response transfer function and the modal
decomposition of the shear model. Every printed equation number is retained:
(1)-(10), (12) and (13); equation (11) is not numbered in the printed source.
Coefficients, subscripts, overbars, overdots and transposes were transcribed
from the page renders p173.png ... p176.png because the PDF text layer scatters
the mathematical symbols.
"""
try:
    import ppicfig8 as F  # noqa: F401  (shared supplier import style)
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()


def _stub_tuple(n):
    """A minimal valid 5-tuple used only while the supplier is unavailable."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 60" '
        'role="img"><rect x="1" y="1" width="678" height="58" '
        'fill="#f4f6fa" stroke="#9aa7bd"/>'
        '<text x="340" y="35" text-anchor="middle" '
        'style="font:14px Helvetica,sans-serif;fill:#24364f">'
        'Figure 8.%d</text></svg>' % n
    )
    return (svg,
            "Hình 8.%d · Sơ đồ nhà máy điện than có CBD." % n,
            "Figure 8.%d · Simplified coal-fired power plant with CBDs." % n,
            "Hình 8.%d" % n,
            "Figure 8.%d" % n)


# Never replace a real supplier callable: these stubs only fill missing names.
if not hasattr(F, "fig_f01"):
    F.fig_f01 = lambda: _stub_tuple(1)

from ppic_ch08_lib import H, P, L, E, FIG, TBL, NOTE, REFS  # noqa: F401


def section(lang):
    """Return the bilingual HTML fragments for this part of Chapter 8."""
    b = []

    # ------------------------------------------- OPTIMIZATION METHOD AND DESIGN
    H(b, lang,
      "PHƯƠNG PHÁP TỐI ƯU VÀ THIẾT KẾ MÔ HÌNH THỰC NGHIỆM",
      "OPTIMIZATION METHOD AND DESIGN OF EXPERIMENTAL MODEL", level=2)

    H(b, lang,
      "Tối ưu hóa thông số của kết cấu CBD",
      "Parameter Optimization of CBD Structure", level=3)

    P(b, lang,
      "Hình 1 mô tả vị trí các phễu than được cố định vào khung của một nhà "
      "máy điện truyền thống. Công nghệ CBD được đề xuất loại bỏ liên kết cố "
      "định này bằng cách treo hoặc đỡ các phễu than. Theo đó, các phần tử đàn "
      "hồi và giảm chấn nối kết cấu với các phễu than được sử dụng để điều "
      "chỉnh tần số dao động và độ giảm chấn bổ sung của các phễu, tương ứng. "
      "Để tối ưu hóa hiệu ứng giảm chấn của các CBD, cần phải tối ưu hóa thiết "
      "kế các đặc tính động của các CBD.",
      "Figure 1 depicts the locations of coal buckets fixed to the frame of a "
      "traditional power plant. The proposed CBD technology removes this fixed "
      "connection by suspending or supporting the coal buckets. Accordingly, "
      "elastic and damping elements connecting the structure to the coal "
      "buckets are used to adjust the oscillation frequency and additional "
      "damping of the buckets, respectively. To optimize the damping effect of "
      "the CBDs, it is necessary to optimize the design of the dynamic "
      "characteristics of the CBDs.")

    FIG(b, 1, F.fig_f01(), lang)

    H(b, lang,
      "Hàm truyền đáp ứng chuyển vị",
      "Displacement Response Transfer Function", level=3)

    P(b, lang,
      "Kết cấu nhà máy điện được đơn giản hóa thành một mô hình cắt (shear "
      "model) có N bậc tự do. Các CBD được đề xuất gồm m đơn vị CBD được bố trí "
      "tại tầng thứ j. Phương trình động của mô hình có các CBD dưới kích "
      "thích gia tốc nền ẍ_g(t) như sau:",
      "The power plant structure is simplified to a shear model with N degrees "
      "of freedom. The proposed CBDs consisting of m CBD units are arranged on "
      "the jth story. The dynamic equations of the model with CBDs under the "
      "base acceleration excitation ẍ_g(t) are as follows:")

    E(b, lang,
      "Mẍ(t) + Cẋ(t) + Kx(t) = F_CBDs − M I_N ẍ_g(t),",
      "Mẍ(t) + Cẋ(t) + Kx(t) = F_CBDs − M I_N ẍ_g(t),", num="1")

    E(b, lang,
      "M̄ x̄̈(t) + M̄ I_m ẍ_j(t) + C̄ x̄̇(t) + K̄ x̄(t) = −M̄ I_m ẍ_g(t),",
      "M̄ x̄̈(t) + M̄ I_m ẍ_j(t) + C̄ x̄̇(t) + K̄ x̄(t) = −M̄ I_m ẍ_g(t),", num="2")

    E(b, lang,
      "F_CBDs = I_mᵀ (C̄ x̄̇(t) + K̄ x̄(t)) D_j.",
      "F_CBDs = I_mᵀ (C̄ x̄̇(t) + K̄ x̄(t)) D_j.", num="3")

    P(b, lang,
      "Trong (1), M, C và K lần lượt là ma trận khối lượng, ma trận giảm chấn "
      "và ma trận độ cứng của kết cấu chính, và các ma trận này có kích thước "
      "N × N. Các hàm x(t), ẋ(t) và ẍ(t) lần lượt là các vectơ chuyển vị, vận "
      "tốc và gia tốc của kết cấu chính so với mặt đất và đều có N chiều. Biến "
      "I_N biểu thị một vectơ đơn vị N chiều. Trong (2), M̄, C̄ và K̄ lần lượt là "
      "ma trận khối lượng, ma trận giảm chấn và ma trận độ cứng của các CBD, và "
      "các ma trận này có kích thước m × m. Các hàm x̄(t), x̄̇(t) và x̄̈(t) lần "
      "lượt là các vectơ chuyển vị, vận tốc và gia tốc của các CBD so với kết "
      "cấu chính và đều có m chiều. Biến I_m là một vectơ đơn vị m chiều. Hàm "
      "ẍ_j(t) là gia tốc của tầng thứ j của kết cấu, F_CBDs là lực tác dụng lên "
      "kết cấu chính từ các CBD, và D_j là vectơ vị trí của các CBD trong đó "
      "phần tử thứ j bằng 1 và tất cả các phần tử khác bằng 0.",
      "In (1), M, C, and K are the mass matrix, damping matrix, and stiffness "
      "matrix of the main structure, respectively, and these matrices are of "
      "dimensions N × N. The functions x(t), ẋ(t), and ẍ(t) are the displacement, "
      "velocity, and acceleration vectors of the main structure, respectively, "
      "with respect to the ground and are all of N dimensions. The variable I_N "
      "represents an N-dimensional unit vector. In (2), M̄, C̄, and K̄ are the mass "
      "matrix, damping matrix, and stiffness matrix, respectively, of the CBDs, "
      "and these matrices are of dimensions m × m. The functions x̄(t), x̄̇(t), "
      "and x̄̈(t) are the displacement, velocity, and acceleration vectors, "
      "respectively, of the CBDs with respect to the main structure, and they "
      "are all of m dimensions. The variable I_m is an m-dimensional unit "
      "vector. The function ẍ_j(t) is the acceleration of the jth story of the "
      "structure, F_CBDs is the force acting on the main structure from the "
      "CBDs, and D_j is the position vector of the CBDs in which the jth element "
      "is 1, and all other elements are 0.")

    P(b, lang,
      "Phương trình (3) cũng có thể được viết là",
      "Equation (3) can also be written as")

    E(b, lang,
      "F_CBDs = D_j Σ_(p=1)^(m) (c_p x̄̇_p + k_p x̄_p),",
      "F_CBDs = D_j Σ_(p=1)^(m) (c_p x̄̇_p + k_p x̄_p),", num="4")

    P(b, lang,
      "trong đó k_p và c_p lần lượt là hệ số độ cứng và hệ số giảm chấn của CBD "
      "thứ p. Các biến x̄_p và x̄̇_p lần lượt là chuyển vị và vận tốc của CBD thứ p.",
      "where k_p and c_p are the stiffness and damping coefficient, respectively, "
      "of the pth CBD. The variables x̄_p and x̄̇_p are the displacement and "
      "velocity, respectively, of the pth CBD.")

    P(b, lang,
      "Sau đó, dao động của hệ kết cấu được phân rã và thu được ma trận dao động "
      "Φ, trong đó q(t) là vectơ chuyển vị pháp tuyến N × 1. Thay x(t) = Φq(t) "
      "vào (1) và nhân trước hai vế của phần kết cấu với Φᵀ sẽ cho:",
      "The vibration mode of the structural system is then decomposed and the "
      "vibration matrix Φ is obtained, where q(t) is the N × 1 modal displacement "
      "vector. Substituting x(t) = Φq(t) into (1) and premultiplying the two "
      "sides of the building part by Φᵀ yield")

    E(b, lang,
      "M* q̈(t) + C* q̇(t) + K* q(t) = Φᵀ F_CBDs − Φᵀ M I_N ẍ_g(t),",
      "M* q̈(t) + C* q̇(t) + K* q(t) = Φᵀ F_CBDs − Φᵀ M I_N ẍ_g(t),", num="5")

    P(b, lang,
      "trong đó M*, C* và K* lần lượt là ma trận khối lượng pháp tuyến, ma trận "
      "giảm chấn pháp tuyến và ma trận độ cứng pháp tuyến của kết cấu. Cân bằng "
      "động của dao động cấp n là:",
      "where M*, C*, and K* are the structural modal mass, structural modal "
      "damping, and structural mode stiffness matrix, respectively. The dynamic "
      "equilibrium of the nth order mode is")

    E(b, lang,
      "M_n q̈_n(t) + C_n q̇_n(t) + K_n q_n(t)\n"
      "= φ_nj Σ_(p=1)^(m) (c_p x̄̇_p + k_p x̄_p) − Φ_nᵀ M I_N ẍ_g(t),",
      "M_n q̈_n(t) + C_n q̇_n(t) + K_n q_n(t)\n"
      "= φ_nj Σ_(p=1)^(m) (c_p x̄̇_p + k_p x̄_p) − Φ_nᵀ M I_N ẍ_g(t),", num="6")

    P(b, lang,
      "trong đó M_n, C_n và K_n lần lượt là khối lượng pháp tuyến, giảm chấn "
      "pháp tuyến và độ cứng pháp tuyến của dao động cấp n của kết cấu. Biến "
      "q_n(t) biểu thị tọa độ tổng quát của dao động cấp n, Φ_n là vectơ dao "
      "động thứ n, và φ_nj là phần tử thứ j của Φ_n.",
      "where M_n, C_n, and K_n are the nth order structural modal mass, "
      "structural modal damping, and structural mode stiffness, respectively. "
      "The variable q_n(t) represents the generalized coordinates of the nth "
      "order vibration mode, Φ_n is the nth mode vector, and φ_nj is the jth "
      "element of Φ_n.")

    P(b, lang,
      "Nếu dao động thứ n là dao động chính trong kiểm soát dao động, thay "
      "ẍ_j(t) = φ_nj q̈_n(t) vào (2) sẽ thu được phương trình sau:",
      "If the nth mode is the main mode of vibration control, substituting "
      "ẍ_j(t) = φ_nj q̈_n(t) into (2) yields the following equation:")

    E(b, lang,
      "M̄ x̄̈(t) + M̄ I_m φ_nj q̈_n(t) + C̄ x̄̇(t) + K̄ x̄(t) = −M̄ I_m ẍ_g(t).",
      "M̄ x̄̈(t) + M̄ I_m φ_nj q̈_n(t) + C̄ x̄̇(t) + K̄ x̄(t) = −M̄ I_m ẍ_g(t).", num="7")

    P(b, lang,
      "Hệ phương trình động mới mô tả các dao động chính và hệ MTMD được tạo "
      "thành từ (6) và (7). Sau khi đặt U(t) = [q_n(t); x̄(t)], hai phương trình "
      "này trở thành:",
      "The new system of dynamic equations describing the main vibration modes "
      "and the MTMD is composed of (6) and (7). After setting U(t) = [q_n(t); "
      "x̄(t)], these two equations become")

    E(b, lang,
      "M̃ Ü(t) + C̃ U̇(t) + K̃ U(t) = {−Φ_nᵀ M I_N; −M̄ I_m} ẍ_g(t),",
      "M̃ Ü(t) + C̃ U̇(t) + K̃ U(t) = {−Φ_nᵀ M I_N; −M̄ I_m} ẍ_g(t),", num="8")

    P(b, lang, "trong đó", "in which")

    E(b, lang,
      "M̃ = [M_n, 0; M̄ I_m φ_nj, M̄],\n"
      "C̃ = [C_n, −φ_nj c_1 − φ_nj c_2 − … − φ_nj c_m; 0, C̄],\n"
      "K̃ = [K_n, −φ_nj k_1 − φ_nj k_2 − … − φ_nj k_m; 0, K̄].",
      "M̃ = [M_n, 0; M̄ I_m φ_nj, M̄],\n"
      "C̃ = [C_n, −φ_nj c_1 − φ_nj c_2 − … − φ_nj c_m; 0, C̄],\n"
      "K̃ = [K_n, −φ_nj k_1 − φ_nj k_2 − … − φ_nj k_m; 0, K̄].", num="9")

    P(b, lang,
      "Theo tính chất bảo toàn tần số của hệ tuyến tính, đặt ẍ_g(t) = e^(iωt) "
      "và thay U(t) = y(ω)e^(iωt) vào (8), trong đó y(ω) là hàm truyền của hệ, "
      "phương trình trở thành:",
      "According to the frequency-preserving property of a linear system, "
      "setting ẍ_g(t) = e^(iωt) and substituting U(t) = y(ω)e^(iωt) into (8), in "
      "which y(ω) is the transfer function of the system, the equation becomes")

    E(b, lang,
      "−ω² M̃ y(ω) e^(iωt) + iω C̃ y(ω) e^(iωt)\n"
      "+ K̃ y(ω) e^(iωt) = {−Φ_nᵀ M I_N; −M̄ I_m} e^(iωt).",
      "−ω² M̃ y(ω) e^(iωt) + iω C̃ y(ω) e^(iωt)\n"
      "+ K̃ y(ω) e^(iωt) = {−Φ_nᵀ M I_N; −M̄ I_m} e^(iωt).", num="10")

    P(b, lang,
      "Bằng cách đặt Γ = {−Φ_nᵀ M I_N; −M̄ I_m}, có thể thu được y(ω) từ (10) "
      "như sau:",
      "By setting Γ = {−Φ_nᵀ M I_N; −M̄ I_m}, y(ω) can be obtained by using (10) "
      "as follows:")

    P(b, lang,
      "Hàm truyền tọa độ tổng quát của dao động cấp n của kết cấu chính là phần "
      "tử đầu tiên của y(ω), có thể thu được bằng phép tính sau [21]:",
      "The generalized coordinate transfer function of the nth order vibration "
      "mode of the main structure is the first element of y(ω), which can be "
      "obtained by calculation as follows [21]:")

    E(b, lang,
      "y_1(ω) = (−η_n − φ_nj Z(ω)) / "
      "(−ω² + 2 i ξ_n ω ω_n + ω_n² − ω² φ_nj² Z(ω));\n"
      "Z(ω) = Σ_(p=1)^(m) (m_p/M_n) · "
      "(2 i ξ_p ω ω_p + ω_p²) / (−ω² + 2 i ξ_p ω ω_p + ω_p²).",
      "y_1(ω) = (−η_n − φ_nj Z(ω)) / "
      "(−ω² + 2 i ξ_n ω ω_n + ω_n² − ω² φ_nj² Z(ω));\n"
      "Z(ω) = Σ_(p=1)^(m) (m_p/M_n) · "
      "(2 i ξ_p ω ω_p + ω_p²) / (−ω² + 2 i ξ_p ω ω_p + ω_p²).", num="12")

    P(b, lang, "trong đó", "in which")

    E(b, lang,
      "η_n = Φ_nᵀ M I_N / M_n,   ω_n = √(K_n/M_n),\n"
      "ξ_n = C_n / (2 ω_n M_n),   ω_p = √(k_p/m_p),   "
      "ξ_p = c_p / (2 ω_p m_p).",
      "η_n = Φ_nᵀ M I_N / M_n,   ω_n = √(K_n/M_n),\n"
      "ξ_n = C_n / (2 ω_n M_n),   ω_p = √(k_p/m_p),   "
      "ξ_p = c_p / (2 ω_p m_p).", num="13")

    P(b, lang,
      "trong đó η_n, ω_n và ξ_n lần lượt là hệ số tham gia dao động thứ n, tần "
      "số pháp tuyến của kết cấu và tỷ lệ giảm chấn pháp tuyến của kết cấu, còn "
      "m_p, ω_p và ξ_p lần lượt là khối lượng, tần số và tỷ lệ giảm chấn của CBD "
      "thứ p.",
      "where η_n, ω_n, and ξ_n are the nth mode participation factor, structural "
      "modal frequency, and structural mode damping ratio, respectively, and "
      "m_p, ω_p, and ξ_p are the pth CBD mass, frequency, and damping ratio, "
      "respectively")

    return b
