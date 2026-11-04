# -*- coding: utf-8 -*-
"""§32.9 Manometric Thermometers — Franco Pavese, p130-137."""
import math as _m
import hb32kit as K
R = K.R                      # lazy proxy to reader_hb_ch32 helpers

TITLE_EN = "Manometric Thermometers"
TITLE_VI = "Nhiệt kế áp suất kế"

# Flat (English, Vietnamese, depth) tuples — depth 0 -> h3, 1 -> h4.
# The English strings are exactly those passed to the headings; sec_index()
# builds the TOC links from #s32-9-<slug(english)>, so spelling must match.
SUBS = [
    ("Vapor Pressure", "Áp suất hơi", 0),
    ("Gas Thermometry", "Đo nhiệt bằng khí", 0),
]


# ---------------------------------------------------------------- references
def refs(lang):
    vi = (lang == "vi")
    items = [
        "1. R. E. Bedford, G. Bonnier, H. Maas, and F. Pavese, Techniques for approximating "
        "the ITS-90, Monograph 90/1 of the Bureau International des Poids et Mesures, Sèvres: "
        "BIPM, 1990.",
        "2. F. Pavese and G. F. Molinar, Modern gas-based temperature and pressure "
        "measurements, International Monograph Series on Cryogenic Engineering, New York: "
        "Plenum Publishing, 1992, and references therein.",
        "3. J. F. Schooley, Thermometry, Boca Raton, FL: CRC Press, 1986.",
        "4. T. J. Quinn, Temperature, London: Academic Press, 1983.",
        "5. R. E. Bedford, G. Bonnier, H. Maas, and F. Pavese, Recommended values of "
        "temperature on the ITS-90 for a selected set of secondary reference points, "
        "<i>Metrologia</i>, 33, 133-154, 1996.",
        "6. F. Pavese, Recalculation on ITS-90 of accurate vapour-pressure equations for "
        "e-H<sub>2</sub>, Ne, N<sub>2</sub>, O<sub>2</sub>, Ar, CH<sub>4</sub> and CO<sub>2</sub>, "
        "<i>J. Chem. Thermodynam.</i>, 25, 1351-1361, 1993.",
    ]
    head_ = ('<h3 id="t32-tltk-9">Tài liệu tham khảo</h3>' if vi else
             '<h3 id="t32-tltk-9">References</h3>')
    return head_ + R.wl(items)


# where-clauses for numbered equations (none are rendered as display equations
# in this section — the vapour-pressure relations appear inside Table 32.23).
_W = {}


# num -> (cap_vi, cap_en, aria_vi, aria_en, title_vi)
_CAP = {
75: ("Hình 32.75 · Vùng đo của phép đo nhiệt bằng áp suất hơi cho các khí khác nhau. Các thanh "
     "nằm ngang biểu diễn khoảng nhiệt độ của từng khí trên trục logarit. Phần tô bóng chỉ những "
     "vùng ít phổ biến hoặc kém chính xác. c: điểm tới hạn; C: điểm ba; λ: điểm lambda.",
     "Figure 32.75 · Range for vapor-pressure thermometry of various gases. The horizontal bars "
     "show each gas temperature span on a logarithmic axis. The shaded parts indicate regions "
     "where it is less common or less accurate. c, critical point; C, triple point; λ, "
     "lambda-point.",
     "Các thanh nằm ngang biểu diễn vùng nhiệt độ của từng khí",
     "Horizontal bars showing each gas temperature range",
     "Vùng đo áp suất hơi theo nhiệt độ"),
76: ("Hình 32.76 · Độ nhạy dp/dT của phép đo nhiệt bằng áp suất hơi cho một số khí được chọn. "
     "Phần tô bóng chỉ vùng ít phổ biến hoặc kém chính xác.",
     "Figure 32.76 · Sensitivity dp/dT of vapor-pressure thermometry for selected gases. The "
     "shaded parts indicate regions where it is less common or less accurate.",
     "Các đường cong độ nhạy theo nhiệt độ",
     "Sensitivity curves versus temperature",
     "Độ nhạy dp/dT theo nhiệt độ"),
77: ("Hình 32.77 · Sơ đồ bố trí chung của một nhiệt kế áp suất kế. Được trình bày cùng đầu dò áp "
     "suất màng chấn lạnh; khi đầu dò đặt ở nhiệt độ phòng thì van bypass cũng đặt ở nhiệt độ "
     "phòng.",
     "Figure 32.77 · The general layout of a manometric thermometer. Shown with a cryogenic "
     "diaphragm pressure transducer; when the transducer is placed at room temperature, the "
     "bypass valve is also at room temperature.",
     "Sơ đồ nhiệt kế áp suất kế với bóng đo, ống mao dẫn, màng ngăn và áp kế",
     "Schematic of a manometric thermometer with bulb, capillary, diaphragm and manometer",
     "Bố trí chung của nhiệt kế áp suất kế"),
}


def _emit_diagram(lang, num, W, H, parts):
    cv, ce, av, ae, tv = _CAP[num]
    return K.diagram(num, W, H, parts, cv, ce, av, ae, lang, tv)


def _emit_chart(lang, num, W, H, xr, yr, xt, yt, curves, xlab, ylab,
                extra="", pad=(56, 20, 18, 42)):
    cv, ce, av, ae, tv = _CAP[num]
    return K.chart(num, W, H, xr, yr, xt, yt, curves, xlab, ylab,
                   cv, ce, av, ae, lang, tv, extra=extra, pad=pad)


# ------------------------------------------------------------------- figures
def F75(lang):
    W, H = 560, 300
    L, R_ = 70, 540
    TOP, BOT = 44, 250

    def X(T):
        return L + (_m.log10(T) - 0.0) / (_m.log10(400.0) - 0.0) * (R_ - L)

    p = [K._line(L, TOP, L, BOT, K.E, 1.4),
         K._line(L, BOT, R_, BOT, K.E, 1.4)]
    for T, lab in ((1, "1"), (10, "10"), (100, "100"), (300, "300")):
        x = X(T)
        p.append(K._line(x, BOT - 4, x, BOT + 4, K.E, 1.0))
        p.append(K._lbl(x, BOT + 18, lab, "ts", "middle", K._fs(8)))
    p.append(K._lbl((L + R_) / 2.0, BOT + 36,
                    "nhiệt độ T (K, thang log) / temperature", "ts", "middle", K._fs(8)))
    gases = [("⁴He", 1.25, 5.2), ("H₂", 13.8, 20.3), ("Ne", 24.6, 40.0),
             ("N₂", 56.0, 125.0), ("O₂", 54.0, 154.0), ("Ar", 83.8, 150.0),
             ("CH₄", 90.7, 190.0), ("CO₂", 216.6, 304.0)]
    y0, dy = TOP + 4, 24
    for i, (name, t0, t1) in enumerate(gases):
        yy = y0 + i * dy
        x0, x1 = X(t0), X(t1)
        p.append(K._rect(x0, yy - 5, max(2.0, x1 - x0), 10, K.FILL, K.E, 1.2))
        p.append(K._lbl(L - 6, yy + 3, name, "ts", "end", K._fs(9)))
    p.append(K._lbl(L, BOT + 52,
                    "c = điểm tới hạn · C = điểm ba · λ = điểm lambda",
                    "ts", "start", K._fs(7)))
    return _emit_diagram(lang, 75, W, H, p)


def F76(lang):
    W, H = 560, 300
    xr, yr = (1, 320), (0, 1.0)
    xt = [(1, "1"), (10, "10"), (100, "100"), (300, "300")]
    yt = [(0, "0"), (0.5, "0.5"), (1.0, "1.0")]
    gases = [("⁴He", 0.95, "c1"), ("H₂", 0.80, "c2"), ("Ne", 0.70, "c3"),
             ("N₂", 0.60, "d1"), ("O₂", 0.55, "c1"), ("Ar", 0.50, "c2"),
             ("CH₄", 0.45, "c3"), ("CO₂", 0.40, "d1")]
    curves = []
    for name, a, cls in gases:
        pts = []
        for i in range(40):
            T = 1.0 + 319.0 * i / 39.0
            yv = a * (1.0 / T) ** 1.2
            if yv < 1e-3:
                yv = 1e-3
            pts.append((T, yv))
        curves.append((pts, cls))
    return _emit_chart(lang, 76, W, H, xr, yr, xt, yt, curves,
                       "nhiệt độ T (K) / temperature",
                       "độ nhạy dp/dT (chuẩn hóa) / sensitivity")


def F77(lang):
    W, H = 560, 320
    p = []
    # bulb
    p.append(K._circ(70, 172, 36, "none", K.E, 1.6))
    p.append(K._lbl(70, 226, "Bóng đo / bulb (V_b)", "ts", "middle", K._fs(9)))
    # capillary tube
    p.append(K._rect(106, 167, 300, 10, K.FILL, K.E, 1.2))
    p.append(K._lbl(186, 154, "Ống mao dẫn / capillary tube", "ts", "middle", K._fs(8)))
    # bypass valve branch
    p.append(K._line(257, 110, 257, 167, K.E, 1.2))
    p.append(K._rect(250, 110, 14, 57, K.DARK, K.E, 1.2))
    p.append(K._lbl(257, 100, "Van bypass / bypass valve", "ts", "middle", K._fs(8)))
    # diaphragm and manometer
    p.append(K._rect(406, 150, 70, 44, K.FILL, K.E, 1.5))
    p.append(K._lbl(441, 172, "Màng ngăn / diaphragm", "ts", "middle", K._fs(8)))
    p.append(K._rect(486, 152, 58, 40, K.FILL, K.E, 1.5))
    p.append(K._lbl(515, 174, "Áp kế / manometer", "ts", "middle", K._fs(8)))
    # flow arrow
    p.append(K._arr(112, 172, 400, 172, K.E, sw=1.4))
    # notes
    p.append(K._lbl(20, 256,
                    "Nhiệt kế áp suất hơi: đường kính ống tăng từng bước khi áp suất < 10 Pa để "
                    "giảm tổn thất áp suất nhiệt phân tử.", "ts", "start", K._fs(7)))
    p.append(K._lbl(20, 274,
                    "Nhiệt kế khí (thể tích không đổi): đường ống nối bóng với đầu dò áp suất "
                    "phải nhỏ để giảm 'thể tích chết'.", "ts", "start", K._fs(7)))
    p.append(K._lbl(20, 292,
                    "Vapor pressure: tube widens in steps below ~10 Pa. Gas (CV): connecting "
                    "pipes must be small to reduce 'dead-volume'.", "ts", "start", K._fs(7)))
    return _emit_diagram(lang, 77, W, H, p)


# ------------------------------------------------------------------- tables
def _t3223(lang):
    vi = (lang == "vi")
    hd = (["Trạng thái cân bằng", "Khoảng T<sub>90</sub> (K)", "−dT (mK)",
           "Độ tinh khiết (vol%)", "Hệ số phương trình"]
          if vi else
          ["Equilibrium state", "T<sub>90</sub> range (K)", "−dT (mK)",
           "Purity (vol%)", "Equation coefficients"])
    rows = [
        ["Liquid-vapor phases of helium-4" if not vi else "Pha lỏng–hơi của heli-4",
         "1.25–2.1768", "0.1", "99.9999",
         "A₀=1.392408, A₁=0.527153, A₂=0.166756, A₃=0.050988, A₄=0.026514, "
         "A₅=0.001975, A₆=−0.017976, A₇=0.005409, A₈=0.013259; B=5.6; C=2.9"],
        ["Liquid-vapor phases of helium-4" if not vi else "Pha lỏng–hơi của heli-4",
         "2.1768–5.0", "0.1", "99.9999",
         "A₀=3.146631, A₁=1.357655, A₂=0.413923, A₃=0.091159, A₄=0.016349, "
         "A₅=0.001826, A₆=−0.004325, A₇=−0.004973; B=10.3; C=1.9"],
        ["Liquid-vapor phases of equilibrium hydrogen" if not vi else "Pha lỏng–hơi của hiđro cân bằng",
         "13.8–20.3", "1", "99.99",
         "A=4.037592968, B=−101.2775246, C=0.0478333313; b₀=1902.885683, b₁=−331.2282212, "
         "b₂=32.25341774, b₃=−2.106674684, b₄=0.060293573, b₅=−0.000645154"],
        ["Liquid-vapor phases of natural neon" if not vi else "Pha lỏng–hơi của neon tự nhiên",
         "24.6–40", "2", "99.99",
         "A=4.61948943, B=−106.478268, C=−0.0369937132, D=0.00004256101"],
        ["Solid-vapor phases of nitrogen" if not vi else "Pha rắn–hơi của nitơ",
         "56.0–63.1", "2", "99.999",
         "A=12.07856655, B=−858.0046109, C=−0.009224098"],
        ["Liquid-vapor phases of nitrogen" if not vi else "Pha lỏng–hơi của nitơ",
         "63.2–125", "5", "99.999",
         "A=−6.10273365, B=1.153844492, C=−1.087106903, D=−1.759094154; "
         "T_c=126.2124 K, p_c=3.39997 MPa"],
        ["Liquid-vapor phases of oxygen" if not vi else "Pha lỏng–hơi của oxy",
         "54–154", "2", "99.999",
         "t=1−T₉₀/T_c; A=−6.044437278, B=1.176127337, C=−0.994073392, "
         "D=−3.449554987, E=3.343141113; T_c=154.5947 K, p_c=5.0430 MPa"],
        ["Liquid-vapor phases of argon" if not vi else "Pha lỏng–hơi của agon",
         "83.8–150", "5", "99.999",
         "A=−5.906852299, B=1.132416723, C=−0.7720072001, D=−1.671235815; "
         "T_c=150.7037 K, p_c=4.8653 MPa"],
        ["Liquid-vapor phases of methane" if not vi else "Pha lỏng–hơi của metan",
         "90.7–190", "5", "99.99",
         "A=−6.047641425, B=1.346053934, C=−0.660194779, D=−1.304583684; "
         "T_c=190.568 K, p_c=4.595 MPa"],
        ["Liquid-vapor phases of carbon dioxide" if not vi else "Pha lỏng–hơi của cacbon điôxít",
         "216.6–304", "15", "99.99",
         "A₀=11.37453929, A₁=−6.886475614, A₂=−9.589976746, A₃=13.6748941, "
         "A₄=−8.601763027; T_c=304.2022 K, p_c=7.3825 MPa"],
    ]
    cap = ("Bảng 32.23 · Các phương trình áp suất hơi đã được chứng nhận, liên kết áp suất p đo "
           "được với nhiệt độ T chưa biết (thang ITS-90). p₀ = 101325 Pa trừ khi có ghi chú khác. "
           "Xem [6] để biết thêm các khí và tài liệu tham khảo." if vi else
           "Table 32.23 · Certified vapor pressure equations, linking the measured pressure p to "
           "the unknown temperature T (on the ITS-90 scale). p₀ = 101325 Pa unless otherwise "
           "stated. See [6] for more gases and references.")
    return R.table(hd, rows, cap, small=True,
                   widths=["28%", "16%", "10%", "14%", "32%"])


def _t3224(lang):
    vi = (lang == "vi")
    hd = (["Hạng mục", "Tiêu chí thiết kế", "Ví dụ"]
          if vi else
          ["Item", "Design criterion", "Example"])
    rows = [
        ["1. Lựa chọn chất làm việc" if not vi else "1. Choice of working substance",
         ("Mỗi chất chỉ bao phủ một khoảng nhiệt độ hẹp: T<sub>max</sub>/T<sub>min</sub> < 2–3 "
          "(kể cả vùng rắn–hơi), trừ heli. Giới hạn: T<sub>max</sub> do áp suất lớn nhất của áp "
          "kế, T<sub>min</sub> do độ nhạy của áp kế." if vi else
          "Each substance spans only a narrow temperature interval: T<sub>max</sub>/T<sub>min</sub> "
          "< 2–3 (including the solid–vapor range), except helium. Limits: T<sub>max</sub> set by "
          "the manometer full-scale pressure, T<sub>min</sub> by manometer sensitivity."),
         ("T<sub>max</sub>/T<sub>min</sub>: ³He ≈ 10, ⁴He ≈ 9, H₂ ≈ 3, Ne ≈ 3, N₂ ≈ 2.5, "
          "O₂ ≈ 2.5, Ar ≈ 2.5, CO₂ ≈ 2 (rắn ≈ 1.5)" if vi else
          "T<sub>max</sub>/T<sub>min</sub>: ³He ≈ 10, ⁴He ≈ 9, H₂ ≈ 3, Ne ≈ 3, N₂ ≈ 2.5, "
          "O₂ ≈ 2.5, Ar ≈ 2.5, CO₂ ≈ 2 (solid ≈ 1.5)")],
        ["2. Lựa chọn hệ đo áp suất" if not vi else "2. Choice of pressure measuring system",
         ("Độ nhạy và độ chính xác phải phù hợp với dải dp/dT và p, tức là T, cần đo." if vi else
          "Sensitivity and accuracy must be matched to the range of dp/dT and of p, i.e. of T, to "
          "be measured."),
         ("Áp kế mặt số: độ chính xác > 1%; màng kim loại/bellows (điện tử): 0,1–0,03%; ống "
          "Bourdon thạch anh: ≈ 0,01% (He rò qua thạch anh); đầu dò chấn lạnh: > 0,1%; màng "
          "tụ điện: độ lặp zero < 0,1 Pa." if vi else
          "Dial manometers: accuracy > 1%; metal diaphragm or bellows (electronic): 0.1–0.03%; "
          "quartz Bourdon: ≈ 0.01% (He leaks through quartz); cryogenic transducers: > 0.1%; "
          "capacitive diaphragms: zero reproducibility < 0.1 Pa.")],
        ["3. Lựa chọn nhiệt kế kín hay “mở”" if not vi else "3. Choice of sealed vs. “open” thermometer",
         ("Nhiệt kế kín chỉ đạt độ chính xác thấp (mặt số); nhiệt kế “mở” ngưng mẫu khí từng "
          "lần đo nên cần hệ thống xử lý khí thường trực." if vi else
          "Sealed thermometers achieve low accuracy only (e.g. dial); “open” thermometers "
          "condense fresh samples for each measurement and require a permanent gas-handling "
          "system."),
         ("Kín: chỉ độ chính xác thấp; “mở”: mẫu được ngưng tụ trong bóng only trong khi đo." if vi else
          "Sealed: low accuracy only; “open”: substance condensed in the bulb only during "
          "measurement.")],
        ["4. Độ tinh khiết, thành phần đồng vị và cân bằng spin" if not vi else
         "4. Gas purity, isotopic composition and spin equilibrium",
         ("Phải biết và kiểm tra độ tinh khiết; một số khí có độ không lặp lại do thành phần "
          "đồng vị; một số khí cần xúc tác để đạt cân bằng spin." if vi else
          "Purity must be known and checked; some gases show irreproducibility from sample-to-"
          "sample isotopic changes; some need a catalyst for spin equilibrium."),
         ("Chỉ gặp vấn đề ở độ chính xác cao: Kr, Xe; H₂, D₂ (cân bằng spin)." if vi else
          "Problems only for high accuracy: Kr, Xe; H₂, D₂ (spin equilibrium).")],
        ["5. Nạp chất vào nhiệt kế" if not vi else "5. Thermometer filling",
         ("Tính lượng chất n cần ngưng tụ; bỏ qua các số hạng in đậm ở xấp xỉ bậc nhất." if vi else
          "Calculate the amount of substance n to condense; to first order the bold terms can be "
          "omitted."),
         ("Ví dụ ⁴He: T<sub>min</sub>=2,2 K, p<sub>min</sub>=5,263 kPa, "
          "T<sub>max</sub>=5,2 K, p<sub>max</sub>=227,5 kPa, V_b ≈ 2 cm³, n ≈ 0,034 mol." if vi else
          "⁴He example: T<sub>min</sub>=2.2 K, p<sub>min</sub>=5.263 kPa, T<sub>max</sub>=5.2 K, "
          "p<sub>max</sub>=227.5 kPa, V_b ≈ 2 cm³, n ≈ 0.034 mol.")],
    ]
    cap = ("Bảng 32.24 · Tóm tắt các tiêu chí thiết kế cho nhiệt kế áp suất hơi (trích theo [2])."
           if vi else
           "Table 32.24 · Summary of design criteria for vapor-pressure thermometers (after [2]).")
    return R.table(hd, rows, cap, small=True,
                   widths=["22%", "44%", "34%"])


def _t3225(lang):
    vi = (lang == "vi")
    hd = (["Hạng mục", "Tiêu chí thiết kế", "Ví dụ"]
          if vi else
          ["Item", "Design criterion", "Example"])
    rows = [
        ["1. Lựa chọn khoảng và độ trải T<sub>min</sub> ≪ T<sub>max</sub>" if not vi else
         "1. Choice of temperature range and span T<sub>min</sub> ≪ T<sub>max</sub>",
         ("Việc này tiên quyết cho hầu hết các tham số thiết kế. Dưới 273,16 K, đo nhiệt bằng ⁴He "
          "giới hạn tới 2,5 K; với ³He, hiệu chỉnh virial chính xác tới 1,5 K." if vi else
          "This choice is preliminary to most design parameters. Below 273.16 K, ⁴He "
          "thermometry is limited down to 2.5 K; with ³He, accurate virial corrections are "
          "available down to 1.5 K."),
         ("Vì p ∝ T, dải 2,5–273,16 K ứng với p<sub>max</sub>/p<sub>min</sub> > 100; mật độ mol "
          "thường phải đổi theo dải để tối ưu độ chính xác." if vi else
          "Since p ∝ T, the 2.5–273.16 K span corresponds to p<sub>max</sub>/p<sub>min</sub> > "
          "100; molar density is usually changed across the range to optimise accuracy.")],
        ["2. Lựa chọn nhiệt độ tham chiếu T₀" if not vi else "2. Choice of reference temperature T₀",
         ("Nhiệt kế tuyệt đối thật sự: chỉ một lựa chọn — 273,16 K. Nhiệt độ tham chiếu thấp T*₀ "
          "(≈ 25–90 K) được gán bởi một thí nghiệm độc lập." if vi else
          "Truly absolute thermometer: only one choice — 273.16 K. A low-temperature reference "
          "T*₀ (≈ 25–90 K) is assigned by an independent experiment."),
         ("CVGT một bóng thường dùng với T*₀; CVGT hai bóng tránh việc đưa bóng lên T₀." if vi else
          "Single-bulb CVGT commonly uses T*₀; two-bulb CVGT avoids bringing the bulb up to T₀.")],
        ["3. Lựa chọn khí đo và mật độ nạp" if not vi else "3. Choice of thermometric gas and filling density",
         ("Khí đo: nitơ (thấp–trung bình); e-hiđro (T > 20 K); ⁴He (> 2,5 K); ³He (> 1,5 K). "
          "p ∝ n/V và dp/dT ∝ n/V." if vi else
          "Thermometric gas: nitrogen (low–medium); e-hydrogen (T > 20 K); ⁴He (> 2.5 K); ³He "
          "(> 1.5 K). p ∝ n/V and dp/dT ∝ n/V."),
         ("Quy tắc: n/V < 250 mol m⁻³ trên ≈ 2,5 K; < 160 dưới 1,2 K; < 30 tại 0,8 K." if vi else
          "Rule: n/V < 250 mol m⁻³ above ≈ 2.5 K; < 160 down to 1.2 K; < 30 at 0.8 K.")],
        ["4. Lựa chọn hệ đo áp suất" if not vi else "4. Choice of the pressure measuring system",
         "Xem Bảng 32.24." if vi else "See Table 32.24.",
         "—", "—"],
        ["5. Thiết kế tham số CVGT" if not vi else "5. CVGT parameter design",
         ("A. Đầu dò áp suất ở nhiệt độ phòng. B. Đầu dò áp suất chấn lạnh. Bóng: độ chính xác "
          "cao ~1 L, thấp ~50 cm³." if vi else
          "A. Room-temperature pressure transducer. B. Cryogenic pressure transducer. Bulb: ~1 L "
          "for top accuracy, as low as 50 cm³ for low accuracy."),
         ("Thể tích chết: độ chính xác cao < 10 cm³; độ chính xác thấp tới 10% thể tích bóng." if vi else
          "Dead-volume: < 10 cm³ for top accuracy; up to 10% of bulb volume for low accuracy.")],
        ["6. Thiết kế bóng" if not vi else "6. Bulb design",
         ("Thể tích có thể không không đổi do môđun nén (vách dày) hoặc bóng đặt trong buồng bảo "
          "vệ; ứng suất được giải tỏa bằng ủ sau gia công." if vi else
          "Volume may not be constant because of the compression modulus (thick walls or a guard "
          "chamber at bulb pressure); stress is relieved by annealing after machining."),
         "³He, ⁴He, N₂, O₂, Ar, CH₄, CO₂ — xem Bảng 32.24 về áp kế." if vi else
         "³He, ⁴He, N₂, O₂, Ar, CH₄, CO₂ — see Table 32.24 for the manometer."],
    ]
    cap = ("Bảng 32.25 · Tóm tắt các tiêu chí thiết kế cho nhiệt kế khí thể tích không đổi tuyệt "
           "đối (CVGT) trong vùng nhiệt độ thấp (T < 273,16 K)." if vi else
           "Table 32.25 · Summary of design criteria for an absolute constant-volume gas "
           "thermometer (CVGT) in the low-temperature range (T < 273.16 K).")
    return R.table(hd, rows, cap, small=True,
                   widths=["22%", "44%", "34%"])


# ------------------------------------------------------------------- section
def _section(lang):
    vi = (lang == "vi")

    def H3(en, vn):
        return R.h3(vn, en) if vi else R.h3(en)

    def H4(en, vn):
        return R.h4(vn, en) if vi else R.h4(en)

    def P(en, vn):
        return R.p(vn if vi else en)

    def FR(n, d):
        return R._frac(n, d)

    def EQ(body, num):
        wen, wvi = _W[num]
        return R.eq(body, num) + R.wl(wvi if vi else wen)

    b = [R.h2("32.9 Nhiệt kế áp suất kế" if vi else "32.9 Manometric Thermometers",
              "Manometric Thermometers" if vi else "Nhiệt kế áp suất kế")]
    b.append(R.authors("Franco Pavese", ""))

    # ============================================================ introduction
    b.append(P(
        "Manometric thermometers are defined in this Handbook as those thermometers that make "
        "use of the pressure of a gaseous medium as the physical quantity to obtain temperature. "
        "Very seldom are they available from commercial sources; for example, the temperature "
        "control of a home freezer is often of this kind. Consequently, instead of simply buying "
        "one, every user must build his own if this kind of thermometer is needed. They can be a "
        "quite useful choice since, in the era of electronic devices and sensors, it is still "
        "possible to make a totally non-electronic thermometer, which in addition keeps its "
        "calibration indefinitely, as long as the quantity of substance sealed in it remains "
        "unchanged. The range of temperatures that can be covered by this kind of thermometer "
        "depends on the principle and on the substance used.",
        "Trong cuốn sách này, nhiệt kế áp suất kế được định nghĩa là những nhiệt kế sử dụng áp "
        "suất của một môi trường khí làm đại lượng vật lý để xác định nhiệt độ. Rất hiếm khi "
        "chúng có sẵn trên thị trường; thí dụ, việc điều khiển nhiệt độ của một tủ đông gia đình "
        "thường thuộc loại này. Do đó, thay vì đơn giản mua một cái, mỗi người dùng phải tự chế "
        "tạo nếu cần loại nhiệt kế này. Chúng có thể là một lựa chọn khá hữu dụng vì, trong thời "
        "đại của các linh kiện và cảm biến điện tử, vẫn có thể làm một nhiệt kế hoàn toàn không "
        "dùng điện, lại giữ được hiệu chuẩn vĩnh viễn miễn là lượng chất bị hàn kín bên trong "
        "không đổi. Dải nhiệt độ mà loại nhiệt kế này có thể phủ phụ thuộc vào nguyên lý và vào "
        "chất được dùng."))
    b.append(P(
        "When the thermodynamic equilibrium between the condensed phase of a substance (either "
        "liquid or solid) and its vapor is used, one has a “vapor-pressure thermometer” and the "
        "temperature range spanned by each substance is generally narrow. In addition, only "
        "substances that are gaseous at room temperature (i.e., condensed at temperatures lower "
        "than 0°C) are normally used, confining the working range to below room temperature; "
        "however, some substances that are liquid at room temperature and have a high vapor "
        "pressure (i.e., which easily evaporate) have been used, but do not result in a sizable "
        "extension of the working range much above room temperature. A special case of vapor "
        "pressure being used at high temperature is the device called a “heat pipe,” which is not "
        "used as a thermometer, but instead as an accurate thermostat [1]; using sodium, the "
        "working range is pushed up to ~1100°C. When a pure substance is used only in its gaseous "
        "state, one has a “gas thermometer,” whose temperature range can be very wide, especially "
        "for moderate accuracy, depending mainly on the manometer; on the other hand, its "
        "fabrication is somewhat more complex and its use less straightforward.",
        "Khi sử dụng cân bằng nhiệt động giữa pha ngưng tụ của một chất (lỏng hoặc rắn) và hơi "
        "của nó, ta có một “nhiệt kế áp suất hơi” và dải nhiệt độ mà mỗi chất phủ thường khá "
        "hẹp. Thêm vào đó, chỉ những chất ở dạng khí ở nhiệt độ phòng (tức ngưng tụ ở nhiệt độ "
        "dưới 0°C) mới thường được dùng, nên vùng làm việc bị giới hạn dưới nhiệt độ phòng; tuy "
        "nhiên, một số chất ở dạng lỏng ở nhiệt độ phòng và có áp suất hơi cao (tức dễ bay hơi) "
        "đã được dùng, nhưng cũng không mở rộng đáng kể vùng làm việc lên cao hơn nhiều so với "
        "nhiệt độ phòng. Một trường hợp đặc biệt dùng áp suất hơi ở nhiệt độ cao là thiết bị gọi "
        "là “ống nhiệt” (heat pipe), không dùng làm nhiệt kế mà làm một bộ điều nhiệt chính xác "
        "[1]; dùng natri, vùng làm việc được đẩy lên tới ~1100°C. Khi một chất tinh khiết chỉ "
        "được dùng ở trạng thái khí, ta có một “nhiệt kế khí”, có dải nhiệt độ rất rộng, nhất là "
        "với độ chính xác trung bình, tùy thuộc chủ yếu vào áp kế; mặt khác, việc chế tạo phức "
        "tạp hơn một chút và sử dụng kém trực tiếp hơn."))
    b.append(P(
        "Both thermometers can be built to satisfy the state-of-the-art accuracy of national "
        "standards (uncertainty better than ±0.001 K) or for lower accuracies, down to an "
        "uncertainty of ±1% or higher. Both thermometers require the measurement of pressure, in "
        "the range from less than 1 Pa up to 100 bar. Directions about the choice of the "
        "manometer can be found in Chapter 5.1 of this Handbook. A complete and specialized "
        "treatment on both vapor-pressure and gas thermometers up to room temperature and on "
        "pressure measurement instruments and techniques for gaseous media can be found in [2]. "
        "Gas thermometry above room temperature is treated in [3, 4].",
        "Cả hai loại nhiệt kế đều có thể được chế tạo để đạt độ chính xác tiên tiến nhất của các "
        "chuẩn quốc gia (độ không đảm bảo tốt hơn ±0,001 K) hoặc độ chính xác thấp hơn, xuống tới "
        "độ không đảm bảo ±1% hoặc lớn hơn. Cả hai đều đòi hỏi đo áp suất, trong dải từ dưới 1 Pa "
        "tới 100 bar. Chỉ dẫn về việc chọn áp kế có thể tìm thấy ở Mục 5.1 của cuốn sách này. "
        "Một trình bày đầy đủ và chuyên sâu về cả nhiệt kế áp suất hơi lẫn nhiệt kế khí tới nhiệt "
        "độ phòng, cùng các dụng cụ và kỹ thuật đo áp suất cho môi trường khí, có trong [2]. Đo "
        "nhiệt bằng khí trên nhiệt độ phòng được trình bày trong [3, 4]."))
    b.append(P(
        "In consideration of the fact that these kinds of thermometers typically must be built by "
        "the users, the following will concentrate on the basic guidelines for their design and "
        "fabrication.",
        "Xét rằng những loại nhiệt kế này thường phải do chính người dùng tự chế tạo, phần sau "
        "sẽ tập trung vào các hướng dẫn cơ bản để thiết kế và chế tạo chúng."))

    # ============================================================ vapor pressure
    b.append(H3("Vapor Pressure", "Áp suất hơi"))
    b.append(P(
        "Figures 32.75 and 32.76 show the pressure values and the sensitivities in the "
        "temperature range allowed for each of the most common gaseous substances, considering "
        "also, in addition to the liquid phase, the use of the solid phase (where vapor pressure "
        "is lower) below the triple point. The lower end of the range is determined by the "
        "manometer uncertainty (for a given accuracy), the upper end by the full-scale pressure "
        "of the manometer (or by the full evaporation of the condensed phase).",
        "Hình 32.75 và 32.76 thể hiện các giá trị áp suất và độ nhạy trong dải nhiệt độ cho phép "
        "của từng chất khí phổ biến nhất, xét cả pha rắn (nơi áp suất hơi thấp hơn) bên dưới điểm "
        "ba ngoài pha lỏng. Đầu dưới của dải được xác định bởi độ không đảm bảo của áp kế (với một "
        "độ chính xác cho trước), đầu trên bởi áp suất toàn thang của áp kế (hoặc bởi sự bốc hơi "
        "hoàn toàn của pha ngưng tụ)."))
    b.append(F75(lang))
    b.append(F76(lang))
    b.append(P(
        "Table 32.23 reports “certified” vapor pressure equations, linking the measured pressure "
        "p to the unknown temperature T. The reader might prefer them to the plethora of "
        "equations found in the literature, since they have been checked by official bodies and T "
        "is expressed in the ITS-90, the International Temperature Scale [5, text in 2]. More "
        "checked equations can be found in [6].",
        "Bảng 32.23 đưa ra các phương trình áp suất hơi “đã được chứng nhận”, liên kết áp suất p "
        "đo được với nhiệt độ T chưa biết. Độc giả có thể thích chúng hơn vô số phương trình tìm "
        "thấy trong tài liệu, vì chúng đã được các cơ quan chính thức kiểm tra và T được biểu diễn "
        "trên thang ITS-90, thang nhiệt độ quốc tế [5, trích dẫn trong 2]. Thêm các phương trình "
        "đã kiểm tra có trong [6]."))
    b.append(_t3223(lang))
    b.append(P(
        "Figure 32.77 shows the general layout of a vapor-pressure thermometer. The fabrication "
        "of a vapor-pressure thermometer is not exceedingly difficult if a few guidelines are "
        "followed. Table 32.24 summarizes the most critical ones — design criteria and filling "
        "information — in a compact form [2]. Much more constructional details can be found in "
        "[1, 3]. In most cases, the manometer is located at room temperature, and the bulb is "
        "connected to it via a small-bore tube (the “capillary tube”) without critical drawbacks. "
        "The accuracy of these thermometers ranges from ±0.0001 K using very pure substances in "
        "calorimeters and precision mercury manometers, to ≈ ±1% using dial manometers.",
        "Hình 32.77 trình bày bố cục chung của một nhiệt kế áp suất hơi. Việc chế tạo nhiệt kế "
        "áp suất hơi không quá khó nếu tuân theo một vài hướng dẫn. Bảng 32.24 tóm tắt những điểm "
        "quan trọng nhất — tiêu chí thiết kế và thông tin nạp — dưới dạng cô đọng [2]. Nhiều chi "
        "tiết chế tạo hơn có trong [1, 3]. Trong hầu hết các trường hợp, áp kế đặt ở nhiệt độ "
        "phòng và bóng đo nối với nó qua một ống nhỏ (”ống mao dẫn”) mà không gây trở ngại đáng "
        "kể. Độ chính xác của các nhiệt kế này dao động từ ±0,0001 K khi dùng chất rất tinh khiết "
        "trong các nhiệt lượng kế và áp kế thủy ngân chính xác, tới ≈ ±1% khi dùng áp kế mặt số."))
    b.append(F77(lang))
    b.append(_t3224(lang))

    # ============================================================ gas thermometry
    b.append(H3("Gas Thermometry", "Đo nhiệt bằng khí"))
    b.append(P(
        "The layout of Figure 32.77 also applies to the design of a constant-volume gas "
        "thermometer (more common than the constant-pressure type), with the differences "
        "indicated in the relevant caption. The lower temperature end of the working range of a "
        "gas thermometer is stated, well before condensation of the substance takes place, by the "
        "increase of the uncertainty due to the increase in the nonideality of the gas — i.e., "
        "deviation from linearity of the relationship p(T) — which takes place when approaching "
        "the condensed state or for increasing gas densities, or due to excessive absorption of "
        "gas on the bulb surface, thereby changing the quantity of the thermometric substance. All "
        "these conditions act at the lower end of the range. The upper end is stated by "
        "technological reasons or by the manometer full-scale capability.",
        "Bố cục của Hình 32.77 cũng áp dụng cho việc thiết kế một nhiệt kế khí thể tích không "
        "đổi (phổ biến hơn loại áp suất không đổi), với những khác biệt được chỉ ra trong chú "
        "thích tương ứng. Đầu dưới của dải làm việc của nhiệt kế khí được xác định, từ lâu trước "
        "khi chất ngưng tụ, bởi sự tăng độ không đảm bảo do tính không lý tưởng của khí tăng lên "
        "— tức sự lệch khỏi tính tuyến tính của quan hệ p(T) — xảy ra khi tiệm cận trạng thái "
        "ngưng tụ hoặc khi mật độ khí tăng, hoặc do sự hấp thụ quá mức khí trên bề mặt bóng, làm "
        "thay đổi lượng chất đo. Tất cả các điều kiện này tác động ở đầu dưới của dải. Đầu trên "
        "được xác định bởi các lý do công nghệ hoặc bởi khả năng toàn thang của áp kế."))
    b.append(P(
        "The best substances are, as listed, helium (either isotopes), hydrogen, and nitrogen. "
        "From a design point of view, Table 32.25 summarizes the most critical issues. The major "
        "problem, apart from gas purity and ideality, is meeting the constant-volume requirement. "
        "Being that the manometer is generally at room temperature, the fraction of gas filling "
        "the connecting “capillary” tube is subtracted from the total amount of thermometric "
        "substance filling the system, and since this fraction is not constant, but depends on "
        "temperature and on technical conditions, it tends to increase the measurement "
        "uncertainty, which is contrary to the case of the vapor-pressure thermometer; this error "
        "is called the dead-volume error. Also, the bulb volume itself changes with temperature, "
        "due to thermal expansion and, to a much smaller extent, to the change in internal "
        "pressure. Design and fabrication criteria and measuring procedures are given in great "
        "detail in [2]. The case where the gas thermometer is calibrated at a number of fixed "
        "points is also described, with a discussion of the simplification in the use of the gas "
        "thermometer introduced with this instrument (called the interpolating gas thermometer, "
        "defined in the ITS-90 for use between 3 K and 26 K).",
        "Các chất tốt nhất, như đã liệt kê, là heli (một trong hai đồng vị), hiđro và nitơ. Về "
        "mặt thiết kế, Bảng 32.25 tóm tắt những vấn đề quan trọng nhất. Vấn đề chính, ngoài độ "
        "tinh khiết và tính lý tưởng của khí, là thỏa mãn yêu cầu thể tích không đổi. Vì áp kế "
        "thường ở nhiệt độ phòng, phần khí lấp đầy “ống mao dẫn” nối sẽ bị trừ đi từ tổng lượng "
        "chất đo trong hệ thống, và vì phần này không không đổi mà phụ thuộc vào nhiệt độ và các "
        "điều kiện kỹ thuật, nó có xu hướng làm tăng độ không đảm bảo đo — trái ngược với trường "
        "hợp nhiệt kế áp suất hơi; sai số này gọi là lỗi thể tích chết (dead-volume). Thể tích "
        "bóng cũng tự thay đổi theo nhiệt độ do giãn nở nhiệt và, ở mức nhỏ hơn nhiều, do thay "
        "đổi áp suất bên trong. Các tiêu chí thiết kế, chế tạo và quy trình đo được trình bày rất "
        "chi tiết trong [2]. Trường hợp nhiệt kế khí được hiệu chuẩn tại một số điểm cố định cũng "
        "được mô tả, kèm thảo luận về sự đơn giản hóa khi sử dụng nhiệt kế khí nhờ dụng cụ này "
        "(gọi là nhiệt kế khí nội suy, được định nghĩa trong ITS-90 để dùng trong khoảng 3 K đến "
        "26 K)."))
    b.append(_t3225(lang))

    b.append(refs(lang))
    return "".join(b)


def sec_vi():
    return _section("vi")


def sec_en():
    return _section("en")
