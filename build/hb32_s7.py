# -*- coding: utf-8 -*-
"""§32.7 Pyroelectric Thermometers — Jacob Fraden, p110-117."""
import math as _m
import hb32kit as K
R = K.R                      # lazy proxy to reader_hb_ch32 helpers

TITLE_EN = "Pyroelectric Thermometers"
TITLE_VI = "Nhiệt kế áp điện"

# Flat (English, Vietnamese, depth) tuples — depth 0 -> h3, 1 -> h4.
# The English strings are exactly those passed to the headings; sec_index()
# builds the TOC links from #s32-7-<slug(english)>, so spelling must match.
SUBS = [
    ("Pyroelectric Effect", "Hiệu ứng áp điện", 0),
    ("Pyroelectric Materials", "Vật liệu áp điện", 0),
    ("Manufacturing Process", "Quy trình chế tạo", 0),
    ("Pyroelectric Sensors", "Cảm biến áp điện", 0),
    ("Applications", "Ứng dụng", 0),
]


# ---------------------------------------------------------------- references
def refs(lang):
    vi = (lang == "vi")
    items = [
        "1. J. Fraden, <i>Handbook of Modern Sensors</i>, 2nd ed., Woodbury, NY: AIP Press, 1997.",
        "2. H. Meixner, G. Mader, and P. Kleinschmidt, Infrared sensors based on the "
        "pyroelectric polymer polyvinylidene fluoride (PVDF), <i>Siemens Forsch. Entwickl. "
        "Ber.</i>, 15(3), 105-114, 1986.",
        "3. P. Kleinschmidt, Piezo- und pyroelektrische Effekte. Heywang, W., ed., in "
        "<i>Sensorik</i>, Kap. 6: New York: Springer, 1984.",
        "4. <i>Semiconductor Sensors, Data Handbook</i>, Philips Export B.V, 1988.",
        "5. C. Ye, T. Tamagawa, and D.L. Polla, Pyroelectric PbTiO3 thin films for "
        "microsensor applications, <i>Transducers'91. Int. Conf. Solid-State Sensors and "
        "Actuators</i>, 904-907, 1991.",
        "6. H. Kawai, The piezoelectricity of poly(vinylidene fluoride), <i>Jap. J. Appl. "
        "Phys.</i>, 8, 975-976, 1969.",
        "7. A. Okada, Some electrical and optical properties of ferroelectric "
        "lead-zirconite-lead-titanate thin films, <i>J. Appl. Phys.</i>, N. 48, 2905, 1977.",
        "8. P.F. Radice, Corona Discharge poling process, U.S. Patent No. 4,365,283; 1982.",
        "9. P.D. Southgate, <i>Appl. Phys. Lett.</i>, 28, 250, 1976.",
    ]
    head_ = ('<h3 id="t32-tltk-7">Tài liệu tham khảo</h3>' if vi else
             '<h3 id="t32-tltk-7">References</h3>')
    return head_ + R.wl(items)


# ------------------------------------------------------------- where clauses
# (English items, Vietnamese items) keyed by equation number 32.119-32.130.
_W = {
"32.119": (["where &nbsp; <i>m</i> = dipole moment per unit volume",
            "&nbsp; <i>A</i> = sensor's area",
            "&nbsp; <i>h</i> = thickness"],
           ["trong đó &nbsp; <i>m</i> = moment lưỡng cực trên một đơn vị thể tích",
            "&nbsp; <i>A</i> = diện tích cảm biến",
            "&nbsp; <i>h</i> = chiều dày"]),
"32.120": (["where &nbsp; <i>Q</i><sub>a</sub> = charge picked up by the electrodes",
            "&nbsp; <i>M</i> = dipole moment of the material"],
           ["trong đó &nbsp; <i>Q</i><sub>a</sub> = điện tích thu được ở các điện cực",
            "&nbsp; <i>M</i> = moment lưỡng cực của vật liệu"]),
"32.121": (["where &nbsp; <i>M</i><sub>0</sub> = remanent (frozen-in) dipole moment"],
           ["trong đó &nbsp; <i>M</i><sub>0</sub> = moment lưỡng cực tàn dư (đóng băng)"]),
"32.122": (["where &nbsp; <i>m</i> depends on the temperature <i>T</i><sub>a</sub> and the "
            "incremental thermal energy Δ<i>W</i> absorbed"],
           ["trong đó &nbsp; <i>m</i> phụ thuộc nhiệt độ <i>T</i><sub>a</sub> và năng lượng "
            "nhiệt gia tăng Δ<i>W</i> được hấp thụ"]),
"32.123": (["where &nbsp; <i>P</i><sub>s</sub> = spontaneous polarization (electric charge)",
            "&nbsp; <i>E</i> = electric field strength",
            "&nbsp; <i>T</i> = temperature in K"],
           ["trong đó &nbsp; <i>P</i><sub>s</sub> = phân cực tự phát (điện tích điện)",
            "&nbsp; <i>E</i> = cường độ điện trường",
            "&nbsp; <i>T</i> = nhiệt độ (K)"]),
"32.124": (["where &nbsp; <i>ε</i><sub>r</sub> = relative permittivity, "
            "<i>ε</i><sub>0</sub> = dielectric constant"],
           ["trong đó &nbsp; <i>ε</i><sub>r</sub> = hằng số điện môi tương đối, "
            "<i>ε</i><sub>0</sub> = hằng số điện môi"]),
"32.125": (["where &nbsp; <i>p</i><sub>Q</sub> = pyroelectric charge coefficient, "
            "<i>A</i> = area, Δ<i>T</i> = temperature rise"],
           ["trong đó &nbsp; <i>p</i><sub>Q</sub> = hệ số điện tích áp điện, "
            "<i>A</i> = diện tích, Δ<i>T</i> = độ tăng nhiệt độ"]),
"32.126": (["where &nbsp; <i>p</i><sub>V</sub> = pyroelectric voltage coefficient, "
            "<i>h</i> = thickness"],
           ["trong đó &nbsp; <i>p</i><sub>V</sub> = hệ số điện áp áp điện, "
            "<i>h</i> = chiều dày"]),
"32.127": (["where &nbsp; <i>C</i> = sensor capacitance, <i>A</i> = area, <i>h</i> = thickness"],
           ["trong đó &nbsp; <i>C</i> = điện dung cảm biến, <i>A</i> = diện tích, "
            "<i>h</i> = chiều dày"]),
"32.128": (["where &nbsp; <i>p</i><sub>Q</sub> = pyroelectric charge coefficient, "
            "<i>C</i> = capacitance"],
           ["trong đó &nbsp; <i>p</i><sub>Q</sub> = hệ số điện tích áp điện, "
            "<i>C</i> = điện dung"]),
"32.129": (["where &nbsp; <i>i</i><sub>0</sub> = peak current, "
            "<i>τ</i><sub>T</sub> = thermal time constant"],
           ["trong đó &nbsp; <i>i</i><sub>0</sub> = dòng đỉnh, "
            "<i>τ</i><sub>T</sub> = hằng số thời gian nhiệt"]),
"32.130": (["where &nbsp; <i>c</i> = specific heat of the sensing element, "
            "<i>r</i> = thermal resistance"],
           ["trong đó &nbsp; <i>c</i> = nhiệt dung riêng của phần tử cảm biến, "
            "<i>r</i> = điện trở nhiệt"]),
}


# ---------------------------------------------------------- figure captions
# num -> (cap_vi, cap_en, aria_vi, aria_en, title_vi)
_CAP = {
65: ("Hình 32.65 · Phân cực tinh thể áp điện trong điện trường mạnh. Cảm biến phải được bảo "
     "quản và vận hành dưới nhiệt độ Curie.",
     "Figure 32.65 · Poling of a pyroelectric crystal in a strong electric field. The sensor "
     "must be stored and operated below the Curie temperature.",
     "Ba trạng thái phân cực A, B, C của tinh thể áp điện",
     "Three poling states A, B, C of a pyroelectric crystal",
     "Phân cực tinh thể áp điện"),
66: ("Hình 32.66 · Cảm biến áp điện và mạch tương đương của nó.",
     "Figure 32.66 · Pyroelectric sensor and its equivalent circuit.",
     "Khối tinh thể có hai điện cực, nguồn dòng i, tụ C và điện trở rò Rb",
     "Crystalline block with two electrodes, current source i, capacitor C and leakage Rb",
     "Cảm biến áp điện và mạch tương đương"),
67: ("Hình 32.67 · Cảm biến áp điện có hai điện cực ở hai mặt đối diện của vật liệu tinh thể. "
     "Bức xạ nhiệt được chiếu dọc theo trục 3.",
     "Figure 32.67 · Pyroelectric sensor has two electrodes at the opposite sides of the "
     "crystalline material. Thermal radiation is applied along axis 3.",
     "Khối tinh thể với hai điện cực và mũi tên bức xạ nhiệt dọc trục 3",
     "Crystalline block with two electrodes and a thermal-radiation arrow along axis 3",
     "Cảm biến áp điện hai điện cực"),
68: ("Hình 32.68 · Đáp ứng của cảm biến áp điện với hàm bước nhiệt. Độ lớn của điện tích Q0 và "
     "điện áp v0 được phóng đại để minh họa.",
     "Figure 32.68 · Response of a pyroelectric sensor to a thermal step function. The "
     "magnitudes of charge Q0 and voltage v0 are exaggerated for clarity.",
     "Giản đồ thời gian của điện tích Q và điện áp V theo thời gian",
     "Timing diagrams of charge Q and voltage V versus time",
     "Đáp ứng bước nhiệt của cảm biến áp điện"),
69: ("Hình 32.69 · Mạch giao tiếp cho cảm biến áp điện hoạt động ở chế độ điện áp (A) và "
     "dòng (B).",
     "Figure 32.69 · Interface circuits for pyroelectric sensors operating in voltage (A) and "
     "current (B) modes.",
     "Hai sơ đồ mạch: bộ theo điện áp (A) và bộ nối đất ảo (B)",
     "Two circuit diagrams: voltage follower (A) and virtual-ground (B)",
     "Mạch giao tiếp cảm biến áp điện"),
}


def _emit_diagram(lang, num, W, H, parts):
    cv, ce, av, ae, tv = _CAP[num]
    return K.diagram(num, W, H, parts, cv, ce, av, ae, lang, tv)


# ------------------------------------------------------------------ figures
def F65(lang):
    W, H = 560, 300
    p = [K._lbl(24, 26, "(A) Dipoles randomly oriented / các dipole định hướng ngẫu nhiên",
                 "ts", "start", K._fs(9)),
         K._lbl(220, 26, "(B) Aligned in field E / định hướng theo trường E",
                "ts", "start", K._fs(9)),
         K._lbl(400, 26, "(C) Frozen + neutralized / đông cứng và trung hòa",
                "ts", "start", K._fs(9))]
    for x0 in (24, 220, 400):
        p.append(K._rect(x0, 50, 130, 200, K.FILL, K.E, 1.4))
    A = [((40, 82), (66, 100)), ((92, 72), (118, 90)), ((50, 120), (78, 138)),
         ((100, 128), (126, 110)), ((44, 170), (70, 156)), ((96, 182), (122, 200)),
         ((58, 210), (86, 196)), ((104, 214), (130, 228))]
    for (x1, y1), (x2, y2) in A:
        p.append(K._arr(x1, y1, x2, y2, K.E, sw=1.2))
    p.append(K._lbl(89, 264, "(A)", "ts", "middle", K._fs(9)))
    Bx = [240, 265, 290, 315, 340]
    for x in Bx:
        p.append(K._arr(x, 232, x, 72, K.E, sw=1.2))
    p.append(K._arr(372, 250, 372, 60, K.G, sw=1.4))
    p.append(K._lbl(372, 52, "E", "ts", "middle", K._fs(11)))
    p.append(K._lbl(285, 264, "(B)", "ts", "middle", K._fs(9)))
    for x in Bx:
        p.append(K._arr(x, 232, x, 72, K.E, sw=1.2))
    p.append(K._lbl(404, 56, "+ + + + +", "ts", "start", K._fs(9)))
    p.append(K._lbl(404, 244, "− − − − −", "ts", "start", K._fs(9)))
    p.append(K._lbl(456, 150, "e⁻", "ts", "middle", K._fs(9)))
    p.append(K._lbl(456, 172, "e⁺", "ts", "middle", K._fs(9)))
    p.append(K._lbl(285, 280, "(C)", "ts", "middle", K._fs(9)))
    return _emit_diagram(lang, 65, W, H, p)


def F66(lang):
    W, H = 560, 320
    p = []
    p.append(K._rect(40, 90, 90, 150, K.FILL, K.E, 1.5))     # material
    p.append(K._rect(40, 76, 90, 14, K.DARK, K.E, 1.2))     # top electrode
    p.append(K._rect(40, 240, 90, 14, K.DARK, K.E, 1.2))    # bottom electrode
    p.append(K._lbl(85, 70, "+", "ts", "middle", K._fs(12)))
    p.append(K._lbl(85, 262, "−", "ts", "middle", K._fs(12)))
    p.append(K._lbl(85, 292, "pyroelectric material / vật liệu áp điện",
                   "ts", "middle", K._fs(8)))
    p.append(K._line(85, 76, 85, 55, K.E, 1.3))
    p.append(K._line(85, 55, 200, 55, K.E, 1.3))
    p.append(K._line(200, 55, 200, 70, K.E, 1.3))
    p.append(K._line(85, 254, 85, 295, K.E, 1.3))
    p.append(K._line(85, 295, 200, 295, K.E, 1.3))
    p.append(K._line(200, 295, 200, 200, K.E, 1.3))
    p.append(K._line(200, 70, 400, 70, K.E, 1.3))           # top node
    p.append(K._line(200, 200, 400, 200, K.E, 1.3))        # bottom node
    p.append(K._source(250, 135, r=18))                     # current source
    p.append(K._lbl(250, 135, "i", "ts", "middle", K._fs(9)))
    p.append(K._line(250, 70, 250, 117, K.E, 1.3))
    p.append(K._line(250, 153, 250, 200, K.E, 1.3))
    p.append(K._line(315, 95, 355, 95, K.E, 2.0))          # capacitor top plate
    p.append(K._line(315, 125, 355, 125, K.E, 2.0))        # capacitor bottom plate
    p.append(K._line(335, 70, 335, 95, K.E, 1.3))
    p.append(K._line(335, 125, 335, 200, K.E, 1.3))
    p.append(K._lbl(360, 110, "C", "ts", "start", K._fs(9)))
    p.append(K._res_v(380, 135, w=9, h=34))                 # leakage Rb
    p.append(K._lbl(392, 135, "Rb", "ts", "start", K._fs(9)))
    p.append(K._line(380, 70, 380, 118, K.E, 1.3))
    p.append(K._line(380, 152, 380, 200, K.E, 1.3))
    p.append(K._lbl(24, 312, "(A) pyroelectric detector · (B) equivalent circuit / mạch tương đương",
                   "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 66, W, H, p)


def F67(lang):
    W, H = 560, 300
    p = []
    p.append(K._rect(180, 70, 200, 160, K.FILL, K.E, 1.6))   # crystal
    p.append(K._rect(180, 52, 200, 16, K.DARK, K.E, 1.2))    # top electrode
    p.append(K._rect(180, 230, 200, 16, K.DARK, K.E, 1.2))   # bottom electrode
    p.append(K._lbl(280, 40, "+", "ts", "middle", K._fs(12)))
    p.append(K._lbl(280, 262, "−", "ts", "middle", K._fs(12)))
    p.append(K._arr(280, 210, 280, 100, K.G, sw=1.4))        # heat flow
    p.append(K._lbl(296, 150, "heat flow / dòng nhiệt", "ts", "start", K._fs(8)))
    p.append(K._darr(280, 292, 280, 250, K.E, sw=1.4))       # incoming radiation
    p.append(K._lbl(296, 278, "thermal radiation / bức xạ nhiệt", "ts", "start", K._fs(8)))
    p.append(K._lbl(280, 286, "axis 3 / trục 3", "ts", "middle", K._fs(8)))
    p.append(K._lbl(180, 22, "crystalline material / vật liệu tinh thể", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 67, W, H, p)


def F68(lang):
    W, H = 560, 300
    p = []
    p.append(K._line(60, 40, 60, 240, K.E, 1.3))            # y axis
    p.append(K._line(60, 240, 500, 240, K.E, 1.3))          # x axis
    p.append(K._lbl(40, 200, "signal", "ts", "end", K._fs(9)))
    p.append(K._lbl(500, 255, "t", "ts", "end", K._fs(9)))
    p.append(K._pl([(60, 228), (180, 228), (180, 215), (500, 215)], K.S, 1.4))   # step Φ
    p.append(K._lbl(190, 210, "Φ (step)", "ts", "start", K._fs(8)))
    p.append(K._pl([(60, 222), (180, 222), (180, 70), (220, 110), (280, 150),
                    (360, 190), (500, 215)], K.E, 1.8))     # Q(t)
    p.append(K._lbl(188, 66, "Q0", "ts", "start", K._fs(9)))
    p.append(K._pl([(60, 222), (180, 222), (230, 205), (300, 180), (380, 150),
                    (460, 120), (500, 112)], K.G, 1.8))     # V(t)
    p.append(K._lbl(470, 108, "v0", "ts", "start", K._fs(9)))
    p.append(K._lbl(24, 284, "Q: đỉnh tức thời, suy giảm với τT · V: trễ rồi suy giảm với τT",
                   "ts", "start", K._fs(8)))
    p.append(K._lbl(300, 30, "Charge Q and voltage V vs time / điện tích và điện áp theo thời gian",
                   "ts", "middle", K._fs(8)))
    return _emit_diagram(lang, 68, W, H, p)


def F69(lang):
    W, H = 560, 330
    p = [K._lbl(24, 26, "(A) Voltage mode / chế độ điện áp", "ts", "start", K._fs(9)),
         K._lbl(300, 26, "(B) Current mode / chế độ dòng", "ts", "start", K._fs(9))]
    # (A) voltage follower
    p.append(K._blk(40, 100, 70, 46, ["pyro", "sensor"], fs=8))
    p.append(K._res_v(75, 200, w=9, h=30))
    p.append(K._lbl(86, 200, "Rb", "ts", "start", K._fs(8)))
    p.append(K._line(75, 146, 75, 185, K.E, 1.2))
    p.append(K._gnd(75, 215, "GND", K.E))
    p.append(K._line(110, 123, 150, 123, K.E, 1.3))
    p.append(K._poly([(150, 80), (150, 166), (210, 123)], "none", K.E, 1.4))
    p.append(K._lbl(158, 96, "+", "ts", "start", K._fs(10)))
    p.append(K._line(210, 123, 300, 123, K.E, 1.3))
    p.append(K._lbl(305, 118, "Vout (A)", "ts", "start", K._fs(8)))
    p.append(K._line(300, 123, 300, 90, K.E, 1.2))
    p.append(K._line(300, 90, 210, 90, K.E, 1.2))
    p.append(K._line(210, 90, 210, 111, K.E, 1.2))
    # (B) virtual-ground
    p.append(K._blk(320, 100, 70, 46, ["pyro", "sensor"], fs=8))
    p.append(K._res_v(355, 200, w=9, h=30))
    p.append(K._lbl(366, 200, "Rb", "ts", "start", K._fs(8)))
    p.append(K._line(355, 146, 355, 185, K.E, 1.2))
    p.append(K._gnd(355, 215, "GND", K.E))
    p.append(K._line(390, 123, 430, 123, K.E, 1.3))
    p.append(K._poly([(430, 80), (430, 166), (490, 123)], "none", K.E, 1.4))
    p.append(K._lbl(438, 96, "−", "ts", "start", K._fs(10)))
    p.append(K._line(490, 123, 540, 123, K.E, 1.3))
    p.append(K._lbl(545, 118, "Vout (B)", "ts", "start", K._fs(8)))
    p.append(K._res_v(460, 100, w=9, h=30))                  # Rf feedback
    p.append(K._line(490, 123, 490, 90, K.E, 1.2))
    p.append(K._line(490, 90, 460, 90, K.E, 1.2))
    p.append(K._line(460, 90, 460, 100, K.E, 1.2))
    p.append(K._line(460, 115, 460, 123, K.E, 1.2))
    p.append(K._line(460, 123, 430, 123, K.E, 1.2))
    p.append(K._lbl(300, 300, "(A) bộ theo điện áp · (B) bộ nối đất ảo (virtual ground)",
                   "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 69, W, H, p)


# ------------------------------------------------------------------- table
def _t3219(lang):
    vi = (lang == "vi")
    hd = (["Vật liệu", "Nhiệt độ Curie (°C)", "Dẫn nhiệt (W mK⁻¹)",
           "Hằng số điện môi tương đối εr", "Hệ số điện tích áp điện (C m⁻² K⁻¹)",
           "Hệ số điện áp áp điện (V m K⁻¹)", "Ghép kp² (%)"] if vi else
          ["Material", "Curie temp. (°C)", "Thermal conduct. (W mK⁻¹)",
           "Rel. permittivity εr", "Pyroelectric charge coeff. (C m⁻² K⁻¹)",
           "Pyroelectric voltage coeff. (V m K⁻¹)", "Coupling kp² (%)"])
    g1 = "Tinh thể đơn" if vi else "Single crystals"
    g2 = "Gốm" if vi else "Ceramics"
    g3 = "Polyme" if vi else "Polymers"
    rows = [
        g1,
        ["TGS", "49", "0.4", "30", "3.5·10<sup>−4</sup>", "1.3·10<sup>6</sup>", "7.5"],
        ["LiTaO3", "618", "4.2", "45", "2.0·10<sup>−4</sup>", "0.5·10<sup>6</sup>", "1.0"],
        g2,
        ["BaTiO3", "120", "3.0", "1000", "4.0·10<sup>−4</sup>", "0.05·10<sup>6</sup>", "0.2"],
        ["PZT", "340", "1.2", "1600", "4.2·10<sup>−4</sup>", "0.03·10<sup>6</sup>", "0.14"],
        g3,
        ["PVDF polycrystalline layers", "205", "0.13", "12", "0.4·10<sup>−4</sup>",
         "0.40·10<sup>6</sup>", "0.2"],
        ["PbTiO3", "470", "2 (monocrystal)", "200", "2.3·10<sup>−4</sup>", "0.13·10<sup>6</sup>",
         "0.39"],
    ]
    cap = ("Bảng 32.19 · Các tính chất vật lý của vật liệu áp điện. Các trị số có thể thay đổi tùy "
           "công nghệ chế tạo. Từ Tài liệu [2]." if vi else
           "Table 32.19 · Physical Properties of Pyroelectric Materials. The above figures may "
           "vary depending on manufacturing technologies. From Reference [2].")
    return R.table(hd, rows, cap, small=True,
                   widths=["20%", "12%", "14%", "14%", "16%", "16%", "8%"])


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

    b = [R.h2("32.7 Nhiệt kế áp điện" if vi else "32.7 Pyroelectric Thermometers",
              "Pyroelectric Thermometers" if vi else "Nhiệt kế áp điện")]
    b.append(R.authors("Jacob Fraden", ""))

    # ===================================================== Pyroelectric Effect
    b.append(H3("Pyroelectric Effect", "Hiệu ứng áp điện"))
    b.append(P(
        "The pyroelectric materials are crystalline substances capable of generating an electric "
        "charge in response to heat flow [1]. The pyroelectric effect is very closely related to "
        "the piezoelectric effect. The materials belong to a class of ferroelectrics. The name was "
        "given in association with ferromagnetics and is rather misleading because most such "
        "materials have nothing to do with iron.",
        "Vật liệu áp điện là những chất tinh thể có khả năng sinh ra điện tích khi có dòng nhiệt "
        "chảy qua [1]. Hiệu ứng áp điện có liên hệ rất chặt chẽ với hiệu ứng áp điện (piezoelectric). "
        "Các vật liệu này thuộc nhóm sắt điện. Tên gọi trên bắt nguồn từ sự liên tưởng với sắt từ "
        "và khá gây hiểu lầm, vì hầu hết vật liệu như vậy chẳng liên quan gì đến sắt."))
    b.append(P(
        "A crystal is considered to be pyroelectric if it exhibits a spontaneous "
        "temperature-dependent polarization. Of the 32 crystal classes, 21 are noncentrosymmetric "
        "and 10 of these exhibit pyroelectric properties. Besides pyroelectric properties, all "
        "these materials exhibit some degree of piezoelectric properties as well — they generate "
        "an electric charge in response to mechanical stress.",
        "Một tinh thể được coi là áp điện nếu nó thể hiện sự phân cực tự phát phụ thuộc nhiệt độ. "
        "Trong 32 lớp tinh thể, có 21 lớp không đối tâm và 10 trong số đó có tính áp điện. Ngoài "
        "tính áp điện, tất cả các vật liệu này còn có một mức độ nào đó tính áp điện (piezo) — "
        "chúng sinh ra điện tích khi chịu ứng suất cơ học."))
    b.append(P(
        "Pyroelectricity was observed for the first time in tourmaline crystals in the 18th "
        "century (some claim that the Greeks noticed it 23 centuries ago). Later, in the 19th "
        "century, Rochelle salt was used to make pyroelectric sensors. A large variety of "
        "materials became available after 1915: KDP (KH2PO4), ADP (NH4H2PO4), BaTiO3, and a "
        "composite of PbTiO3 and PbZrO3 known as PZT. Presently, more than 1000 materials with "
        "reversible polarization are known. They are called ferroelectric crystals. Most important "
        "among them are triglycine sulfate (TGS) and lithium tantalate (LiTaO3).",
        "Hiệu ứng áp điện được quan sát lần đầu tiên trong tinh thể tourmaline vào thế kỷ 18 (một "
        "số ý kiến cho rằng người Hy Lạp đã nhận ra nó từ 23 thế kỷ trước). Sau đó, vào thế kỷ 19, "
        "muối Rochelle được dùng để chế tạo cảm biến áp điện. Nhiều vật liệu đa dạng trở nên sẵn "
        "có sau năm 1915: KDP (KH2PO4), ADP (NH4H2PO4), BaTiO3, và hợp chất của PbTiO3 và PbZrO3 "
        "gọi là PZT. Hiện nay, hơn 1000 vật liệu có phân cực đảo nghịch đã được biết đến, gọi là "
        "các tinh thể sắt điện. Quan trọng nhất trong số đó là sulfat triglycin (TGS) và titanat "
        "liti (LiTaO3)."))
    b.append(P(
        "A pyroelectric material can be considered a composition of a large number of minute "
        "crystallites, where each behaves as a small electric dipole. All these dipoles are "
        "randomly oriented, however, along a preferred direction. Above a certain temperature, "
        "known as the Curie point, the crystallites have no dipole moment. When the temperature of "
        "a pyroelectric material changes, the material becomes polarized. In other words, an "
        "electric charge appears on its surface. It should be clearly understood that the "
        "polarization occurs not as a function of temperature, but only as a function of a change "
        "in temperature of the material. There are several mechanisms by which changes in "
        "temperature will result in pyroelectricity. Temperature changes can cause shortening or "
        "elongation of individual dipoles. It can also affect the randomness of the dipole "
        "orientations due to thermal agitation. These phenomena are called primary pyroelectricity. "
        "There is also secondary pyroelectricity, which, in a simplified way, can be described as a "
        "result of the piezoelectric effect; that is, a development of strain in the material due "
        "to thermal expansion.",
        "Vật liệu áp điện có thể được xem là tập hợp của một số lượng lớn các hạt tinh thể nhỏ "
        "li ti, mỗi hạt đóng vai trò như một lưỡng cực điện nhỏ. Tất cả các lưỡng cực này tuy "
        "được định hướng ngẫu nhiên nhưng lại thiên về một hướng ưu tiên. Ở trên một nhiệt độ nhất "
        "định gọi là điểm Curie, các hạt tinh thể không có moment lưỡng cực. Khi nhiệt độ của vật "
        "liệu áp điện thay đổi, vật liệu bị phân cực. Nói cách khác, một điện tích xuất hiện trên "
        "bề mặt của nó. Cần hiểu rõ rằng sự phân cực không phải là hàm của nhiệt độ, mà chỉ là hàm "
        "của sự thay đổi nhiệt độ của vật liệu. Có một số cơ chế mà theo đó sự thay đổi nhiệt độ dẫn "
        "đến áp điện. Sự thay đổi nhiệt độ có thể làm ngắn lại hoặc kéo dài các lưỡng cực riêng "
        "lẻ. Nó cũng có thể ảnh hưởng đến tính ngẫu nhiên của định hướng lưỡng cực do kích động "
        "nhiệt. Các hiện tượng này gọi là áp điện sơ cấp. Ngoài ra còn có áp điện thứ cấp, có thể "
        "mô tả một cách đơn giản là kết quả của hiệu ứng áp điện (piezo); nghĩa là sự phát triển "
        "biến dạng trong vật liệu do giãn nở nhiệt."))
    b.append(EQ("<i>M</i> = <i>m</i> <i>A</i> <i>h</i>", "32.119"))
    b.append(P(
        "The charge, <i>Q</i><sub>a</sub>, which can be picked up by the electrodes, develops the "
        "dipole moment across the material:",
        "Điện tích <i>Q</i><sub>a</sub> thu được ở các điện cực làm phát triển moment lưỡng cực "
        "xuyên suốt vật liệu:"))
    b.append(EQ(FR("<i>M</i>", "<i>h</i>"), "32.120"))
    b.append(P(
        "When the temperature varies, the dipole moment also changes, resulting in an induced "
        "charge. The dipole moment, <i>M</i>, must be equal to the remanent moment <i>M</i><sub>0</sub>, "
        "so that:",
        "Khi nhiệt độ thay đổi, moment lưỡng cực cũng thay đổi, dẫn đến một điện tích cảm ứng. "
        "Moment lưỡng cực <i>M</i> phải bằng moment tàn dư <i>M</i><sub>0</sub>, do đó:"))
    b.append(EQ(FR("<i>M</i><sub>0</sub>", "<i>h</i>"), "32.121"))
    b.append(P(
        "Thermal absorption can be related to a dipole change, so that <i>m</i> must be considered "
        "a function of both temperature, <i>T</i><sub>a</sub>, and an incremental thermal energy, "
        "Δ<i>W</i>, absorbed by the material:",
        "Sự hấp thụ nhiệt có thể liên hệ với sự thay đổi lưỡng cực, vì vậy <i>m</i> phải được xem "
        "là hàm của cả nhiệt độ <i>T</i><sub>a</sub> và năng lượng nhiệt gia tăng Δ<i>W</i> được "
        "vật liệu hấp thụ:"))
    b.append(EQ("<i>m</i> = <i>m</i>(<i>T</i><sub>a</sub>, Δ<i>W</i>)", "32.122"))
    b.append(P(
        "The above equation shows the magnitude of electric charge resulting from absorption of "
        "thermal energy. To pick up the charge, the pyroelectric materials are fabricated in the "
        "shapes of a flat capacitor with two electrodes on opposite sides and the pyroelectric "
        "material serving as a dielectric.",
        "Phương trình trên cho thấy độ lớn điện tích sinh ra do hấp thụ năng lượng nhiệt. Để thu "
        "được điện tích, vật liệu áp điện được chế tạo thành dạng tụ phẳng với hai điện cực ở hai "
        "mặt đối diện và vật liệu áp điện đóng vai trò như một chất điện môi."))

    # =================================================== Pyroelectric Materials
    b.append(H3("Pyroelectric Materials", "Vật liệu áp điện"))
    b.append(P(
        "To select the most appropriate pyroelectric material, energy conversion efficiency should "
        "be considered. It is, indeed, the function of the pyroelectric sensor to convert thermal "
        "energy into electrical. 'How effective is the sensor?' is a key question in the design "
        "practice. A measure of efficiency is <i>k</i><sub>p</sub>² which is called the pyroelectric "
        "coupling coefficient [2, 3]. It shows the factor by which the pyroelectric efficiency is "
        "lower than the Carnot limiting value Δ<i>T</i>/<i>T</i><sub>a</sub>. Numerical values for "
        "<i>k</i><sub>p</sub>² are shown in Table 32.19.",
        "Để chọn vật liệu áp điện thích hợp nhất, cần xét đến hiệu suất chuyển đổi năng lượng. "
        "Đúng vậy, chức năng của cảm biến áp điện là chuyển đổi năng lượng nhiệt thành năng lượng "
        "điện. 'Cảm biến hiệu quả đến mức nào?' là câu hỏi then chốt trong thực hành thiết kế. Một "
        "thước đo hiệu suất là <i>k</i><sub>p</sub>² gọi là hệ số ghép áp điện [2, 3]. Nó chỉ ra "
        "hệ số mà theo đó hiệu suất áp điện thấp hơn giá trị giới hạn Carnot Δ<i>T</i>/"
        "<i>T</i><sub>a</sub>. Các giá trị số của <i>k</i><sub>p</sub>² được trình bày trong Bảng "
        "32.19."))
    b.append(P(
        "Table 32.19 shows that triglycine sulfate (TGS) crystals are the most efficient "
        "pyroelectric converters. However, for a long time they were quite impractical for use in "
        "sensors because of a low Curie temperature. If the sensor's temperature is elevated above "
        "that level, it permanently loses its polarization. In fact, TGS sensors proved to be "
        "unstable even below the Curie temperature, with the signal being lost quite spontaneously "
        "[4]. It was discovered that doping of TGS crystals with L-alanine (LATGS process patented "
        "by Philips) during its growth stabilizes the material below the Curie temperature. The "
        "Curie temperature was raised to 60 °C, which allows its use at the upper operating "
        "temperature of 55 °C, which is sufficient for many applications.",
        "Bảng 32.19 cho thấy các tinh thể sulfat triglycin (TGS) là bộ chuyển đổi áp điện hiệu quả "
        "nhất. Tuy nhiên, trong một thời gian dài chúng khá không thực tế để dùng trong cảm biến "
        "do nhiệt độ Curie thấp. Nếu nhiệt độ cảm biến vượt quá mức đó, nó mất vĩnh viễn sự phân "
        "cực. Thực tế, cảm biến TGS tỏ ra không ổn định ngay cả dưới nhiệt độ Curie, với tín hiệu "
        "bị mất khá tự phát [4]. Người ta phát hiện rằng việc pha tạp tinh thể TGS bằng L-alanine "
        "(quy trình LATGS được Philips cấp bằng sáng chế) trong quá trình nuôi tinh thể sẽ ổn định "
        "vật liệu dưới nhiệt độ Curie. Nhiệt độ Curie được nâng lên 60 °C, cho phép dùng nó ở nhiệt "
        "độ làm việc cực đại 55 °C, đủ cho nhiều ứng dụng."))
    b.append(P(
        "Other materials, such as lithium tantalate and pyroelectric ceramics, are also used to "
        "produce pyroelectric sensors. Polymer films (KYNAR from AMP Inc.) have become increasingly "
        "popular for a variety of applications. During recent years, deposition of pyroelectric "
        "thin films has been intensively researched. Especially promising is the use of lead "
        "titanate (PbTiO3), which is a ferroelectric ceramic having both a high pyroelectric "
        "coefficient and a high Curie temperature of about 490 °C. This material can be easily "
        "deposited on silicon substrates by the so-called sol-gel spin casting deposition method "
        "[5].",
        "Các vật liệu khác như titanat liti và gốm áp điện cũng được dùng để chế tạo cảm biến áp "
        "điện. Các màng polymer (KYNAR của AMP Inc.) ngày càng phổ biến trong nhiều ứng dụng. "
        "Trong những năm gần đây, việc lắng đọng các màng mỏng áp điện được nghiên cứu rất mạnh. "
        "Đầy hứa hẹn nhất là việc dùng titanat chì (PbTiO3), một gốm sắt điện có cả hệ số áp điện "
        "cao lẫn nhiệt độ Curie cao khoảng 490 °C. Vật liệu này có thể dễ dàng lắng đọng trên đế "
        "silicon bằng phương pháp lắng đọng sol-gel quay ly tâm [5]."))
    b.append(P(
        "In 1969, Kawai discovered strong piezoelectricity in the plastic materials, polyvinyl "
        "fluoride (PVF) and polyvinylidene fluoride (PVDF) [6]. These materials also possess "
        "substantial pyroelectric properties. PVDF is a semicrystalline polymer with an approximate "
        "degree of crystallinity of 50% [7]. Like other semicrystalline polymers, PVDF consists of "
        "a lamellar structure mixed with amorphous regions. The chemical structure contains the "
        "repeat unit of doubly fluorinated ethene CF2-CH2. The molecular weight of PVDF is about "
        "10⁵, which corresponds to about 2000 repeat units. The film is quite transparent in the "
        "visible and near-IR regions, and is absorptive in the far-infrared portion of the "
        "electromagnetic spectrum. The polymer melts at about 170 °C. Its density is about 1780 kg "
        "m⁻³. PVDF is mechanically durable and flexible.",
        "Năm 1969, Kawai phát hiện tính áp điện mạnh trong các vật liệu nhựa, polyvinyl fluoride "
        "(PVF) và polyvinylidene fluoride (PVDF) [6]. Các vật liệu này cũng có tính áp điện đáng "
        "kể. PVDF là một polymer bán kết tinh với độ kết tinh xấp xỉ 50% [7]. Giống như các polymer "
        "bán kết tinh khác, PVDF gồm cấu trúc lớp lamen xen kẽ với các vùng vô định hình. Cấu trúc "
        "hóa học chứa đơn vị lặp lại của ethen hai lần fluor CF2-CH2. Khối lượng phân tử của PVDF "
        "khoảng 10⁵, tương ứng khoảng 2000 đơn vị lặp. Màng khá trong suốt trong vùng khả kiến và "
        "hồng ngoại gần, và hấp thụ trong phần hồng ngoại xa của phổ điện từ. Polymer nóng chảy "
        "khoảng 170 °C. Khối lượng riêng của nó khoảng 1780 kg m⁻³. PVDF bền cơ học và dẻo."))
    b.append(P(
        "Since silicon does not possess pyroelectric properties, such properties can be added on "
        "by depositing crystalline layers of pyroelectric materials. The three most popular "
        "materials are zinc oxide (ZnO), aluminum nitride (AlN), and the so-called solid solution "
        "system of lead-zirconite-titanium oxides Pb(Zr,Ti)O3 known as PZT ceramic, which is "
        "basically the same material used for fabrication of discrete piezoelectric and pyroelectric "
        "sensors. One of the advantages of using zinc oxide is the ease of chemical etching. The "
        "zinc oxide thin films are usually deposited on silicon by employing sputtering technology. "
        "Note, however, that silicon has a large coefficient of thermal conductivity. That is, its "
        "thermal time constant is very small (see below), so the pyroelectric sensors made with "
        "silicon substrates possess low sensitivity yet are capable of fast response.",
        "Vì silicon không có tính áp điện, người ta có thể bổ sung tính chất này bằng cách lắng đọng "
        "các lớp tinh thể của vật liệu áp điện. Ba vật liệu phổ biến nhất là oxit kẽm (ZnO), nitrua "
        "nhôm (AlN), và hệ dung dịch rắn các oxit chì-zircon-titan Pb(Zr,Ti)O3 gọi là gốm PZT, về "
        "cơ bản là cùng vật liệu dùng để chế tạo các cảm biến áp điện và áp điện rời rạc. Một ưu "
        "điểm của oxit kẽm là dễ ăn mòn hóa học. Các màng mỏng oxit kẽm thường được lắng đọng trên "
        "silicon bằng công nghệ phún xạ. Tuy nhiên, cần lưu ý silicon có hệ số dẫn nhiệt lớn. Nghĩa "
        "là hằng số thời gian nhiệt của nó rất nhỏ (xem bên dưới), do đó các cảm biến áp điện chế "
        "tạo trên đế silicon có độ nhạy thấp nhưng đáp ứng nhanh."))
    b.append(_t3219(lang))

    # ==================================================== Manufacturing Process
    b.append(H3("Manufacturing Process", "Quy trình chế tạo"))
    b.append(P(
        "Manufacturing of ceramic PZT elements begins with high-purity metal oxides (lead oxide, "
        "zirconium oxide, titanium oxide, etc.) in the form of fine powders having various colors. "
        "The powders are milled to a specific fineness, and mixed thoroughly in chemically correct "
        "proportions. In a process called 'calcining', the mixtures are then exposed to an elevated "
        "temperature, allowing the ingredients to react to form a powder, each grain of which has a "
        "chemical composition close to the desired final composition. At this stage, however, the "
        "grain does not yet have the desired crystalline structure.",
        "Chế tạo các phần tử gốm PZT bắt đầu với các oxit kim loại độ tinh khiết cao (oxit chì, oxit "
        "zircon, oxit titan, v.v.) dạng bột mịn có nhiều màu khác nhau. Các bột được nghiền đến độ "
        "mịn nhất định, và trộn kỹ theo tỉ lệ hóa học chính xác. Trong một quy trình gọi là 'nung "
        "kết', hỗn hợp sau đó được đưa vào nhiệt độ cao, cho phép các thành phần phản ứng tạo thành "
        "bột, mỗi hạt có thành phần hóa học gần với thành phần cuối mong muốn. Tuy nhiên, ở giai "
        "đoạn này hạt chưa có cấu trúc tinh thể như ý."))
    b.append(P(
        "The next step is to mix the calcined powder with solid and/or liquid organic binders "
        "(intended to burn out during firing) and mechanically form the mixture into a 'cake' that "
        "closely approximates a shape of the final sensing element. To form the 'cakes' of desired "
        "shapes, several methods can be used. Among them are pressing (under force of a "
        "hydraulic-powered piston), casting (pouring viscous liquid into molds and allowing to "
        "dry), extrusion (pressing the mixture through a die, or a pair of rolls to form thin "
        "sheets), and tape casting (pulling viscous liquid onto a smooth moving belt).",
        "Bước tiếp theo là trộn bột đã nung kết với chất kết dính hữu cơ rắn và/hoặc lỏng (nhằm "
        "cháy rụng trong lúc nung) và cơ học tạo hỗn hợp thành một 'bánh' xấp xỉ sát hình dạng của "
        "phần tử cảm biến cuối. Để tạo các 'bánh' có hình dạng mong muốn, có thể dùng nhiều phương "
        "pháp. Trong đó có ép (bằng lực của piston thủy lực), đúc (rót chất lỏng nhớt vào khuôn và "
        "để khô), đùn ép (ép hỗn hợp qua khuôn, hoặc qua cặp trục lăn để tạo tấm mỏng), và đúc "
        "băng (kéo chất lỏng nhớt lên một băng chuyền nhẵn)."))
    b.append(P(
        "After the 'cakes' have been formed, they are placed into a kiln and exposed to a very "
        "carefully controlled temperature profile. After burning out of organic binders, the "
        "material shrinks by about 15%. The 'cakes' are heated to a red glow and maintained at that "
        "state for some time, which is called the 'soak time', during which the final chemical "
        "reaction occurs. The crystalline structure is formed when the material is cooled down. "
        "Depending on the material, the entire firing may take 24 h.",
        "Sau khi tạo hình các 'bánh', chúng được đặt vào lò và chịu một phác đồ nhiệt độ được kiểm "
        "soát rất chặt chẽ. Sau khi cháy rụng chất kết dính hữu cơ, vật liệu co rút khoảng 15%. Các "
        "'bánh' được nung tới sáng đỏ và giữ trạng thái đó một thời gian, gọi là 'thời gian thấm', "
        "khi đó phản ứng hóa học cuối cùng xảy ra. Cấu trúc tinh thể hình thành khi vật liệu nguội "
        "dần. Tùy vật liệu, toàn bộ quá trình nung có thể mất 24 giờ."))
    b.append(P(
        "When the material is cold, contact electrodes are applied to its surface. This can be done "
        "by several methods. The most common are: fired-on silver (a silk-screening of "
        "silver-glass mixture and refiring), electroless plating (a chemical deposition in a "
        "special bath), and sputtering (an exposure to metal vapor in partial vacuum).",
        "Khi vật liệu nguội, các điện cực tiếp xúc được phủ lên bề mặt. Có thể thực hiện bằng nhiều "
        "cách. Phổ biến nhất là: bạc nung (in lụa hỗn hợp bạc-thủy tinh rồi nung lại), mạ không "
        "điện (lắng đọng hóa học trong bể đặc biệt), và phún xạ (phơi vào hơi kim loại trong chân "
        "không một phần)."))
    b.append(P(
        "Crystallites (crystal cells) in the material can be considered electric dipoles. In some "
        "materials, like quartz, these cells are naturally oriented along the crystal axes, thus "
        "giving the material sensitivity to stress. In other materials, the dipoles are randomly "
        "oriented and the materials need to be 'poled' to possess piezoelectric properties. To give "
        "a crystalline material pyroelectric properties, several poling techniques can be used. The "
        "most popular poling process is thermal poling, which includes the following steps:",
        "Các hạt tinh thể (tế bào tinh thể) trong vật liệu có thể xem như các lưỡng cực điện. Trong "
        "một số vật liệu như thạch anh, các tế bào này định hướng tự nhiên dọc theo trục tinh thể, "
        "nhờ đó vật liệu nhạy với ứng suất. Ở các vật liệu khác, các lưỡng cực định hướng ngẫu "
        "nhiên và vật liệu cần được 'phân cực' để có tính áp điện. Để mang lại tính áp điện cho vật "
        "liệu tinh thể, có thể dùng một số kỹ thuật phân cực. Quy trình phân cực phổ biến nhất là "
        "phân cực nhiệt, bao gồm các bước sau:"))
    b.append(P(
        "1. A crystalline material (ceramic or polymer film) that has randomly oriented dipoles "
        "(Figure 32.65A) is warmed to slightly below its Curie temperature. In some cases (for a "
        "PVDF film), the material is stressed. High temperature results in stronger agitation of "
        "dipoles and permits one to more easily orient them in a desirable direction. 2. The "
        "material is placed in a strong electric field <i>E</i> (Figure 32.65B) where dipoles align "
        "along the field lines. The alignment is not total. Many dipoles deviate from the field "
        "direction quite strongly; however, statistically predominant orientation of the dipoles is "
        "maintained. 3. The material is cooled down while the electric field across its thickness is "
        "maintained. 4. The electric field is removed and the poling process is complete. As long as "
        "the poled material is maintained below the Curie temperature, its polarization remains "
        "permanent. The dipoles stay 'frozen' in the direction that was given to them by the "
        "electric field at high temperature (Figure 32.65C). The above method is used to "
        "manufacture ceramic and plastic pyroelectric materials.",
        "1. Vật liệu tinh thể (gốm hoặc màng polymer) có các lưỡng cực định hướng ngẫu nhiên (Hình "
        "32.65A) được làm ấm đến hơi dưới nhiệt độ Curie. Trong một số trường hợp (màng PVDF), vật "
        "liệu bị ứng suất. Nhiệt độ cao khiến các lưỡng cực dao động mạnh hơn và cho phép dễ dàng "
        "định hướng chúng theo hướng mong muốn. 2. Vật liệu được đặt trong điện trường mạnh "
        "<i>E</i> (Hình 32.65B) nơi các lưỡng cực xếp hàng dọc theo đường sức điện. Sự xếp hàng "
        "không hoàn toàn. Nhiều lưỡng cực lệch khá mạnh khỏi hướng trường; tuy nhiên, định hướng "
        "chiếm ưu thế thống kê của các lưỡng cực vẫn được duy trì. 3. Vật liệu được làm nguội trong "
        "khi vẫn duy trì điện trường dọc chiều dày. 4. Ngắt điện trường và quy trình phân cực hoàn "
        "tất. Miễn là vật liệu đã phân cực được giữ dưới nhiệt độ Curie, sự phân cực của nó vẫn vĩnh "
        "viễn. Các lưỡng cực 'đóng băng' theo hướng mà điện trường nhiệt độ cao đã cho chúng (Hình "
        "32.65C). Phương pháp trên dùng để chế tạo vật liệu áp điện gốm và nhựa."))
    b.append(P(
        "Another method, called a corona discharge poling, can be used to produce polymer "
        "piezo/pyroelectric films. The film is subjected to a corona discharge from an electrode at "
        "several million volts per centimeter of film thickness for 40 s to 50 s [8, 9]. Corona "
        "polarization is uncomplicated to perform and can be easily applied before electric "
        "breakdown occurs, making this process useful at room temperature.",
        "Một phương pháp khác, gọi là phân cực phóng điện corona, có thể dùng để sản xuất các màng "
        "piezo/áp điện polymer. Màng chịu phóng điện corona từ một điện cực với vài triệu vôn trên "
        "mỗi centimet chiều dày màng trong 40 s đến 50 s [8, 9]. Phân cực corona dễ thực hiện và "
        "có thể áp dụng dễ dàng trước khi xảy ra đánh thủng điện, làm cho quy trình này hữu ích ở "
        "nhiệt độ phòng."))
    b.append(P(
        "The final operation in preparing the sensing element is shaping and finishing. This "
        "includes cutting, machining, and grinding. After the piezo (pyro) element is prepared, it "
        "is installed into a sensor's housing, where its electrodes are bonded to electrical "
        "terminals and other electronic components.",
        "Công đoạn cuối trong việc chuẩn bị phần tử cảm biến là tạo hình và hoàn thiện. Việc này "
        "bao gồm cắt, gia công cơ và mài. Sau khi phần tử piezo (pyro) được chế tạo, nó được lắp "
        "vào vỏ cảm biến, nơi các điện cực của nó được gắn vào các đầu cuối điện và linh kiện điện "
        "tử khác."))
    b.append(P(
        "After poling, the crystal remains permanently polarized; however, it remains electrically "
        "charged for a relatively short time. There is a sufficient amount of free carriers that "
        "move in the electric field setup inside the bulk material and there are plenty of charged "
        "ions in the surrounding air. The charge carriers move toward the poled dipoles and "
        "neutralize their charges (Figure 32.65C). Hence, after a while, the poled piezoelectric "
        "material becomes electrically discharged as long as it remains under steady-state "
        "conditions. When temperature changes and thermally induced stress develops, the balanced "
        "state is degraded and the pyroelectric material develops an electric charge. If the stress "
        "is maintained for a while, the charges again will be neutralized by the internal leakage. "
        "Thus, a pyroelectric material is responsive only to a changing temperature rather than to "
        "a steady level of it. In other words, a pyroelectric sensor is an ac device, rather than a "
        "dc device. Sometimes, it is called a dynamic sensor, which reflects the nature of its "
        "response.",
        "Sau khi phân cực, tinh thể vẫn giữ sự phân cực vĩnh viễn; tuy nhiên, nó chỉ mang điện "
        "trong một thời gian tương đối ngắn. Có một lượng hạt tải tự do đủ lớn di chuyển trong "
        "điện trường thiết lập bên trong khối vật liệu, và có rất nhiều ion mang điện trong không "
        "khí xung quanh. Các hạt tải di chuyển về phía các lưỡng cực đã phân cực và trung hòa điện "
        "tích của chúng (Hình 32.65C). Do đó, sau một lúc, vật liệu piezo đã phân cực bị mất điện "
        "miễn là nó duy trì điều kiện tĩnh. Khi nhiệt độ thay đổi và ứng suất cảm ứng nhiệt phát "
        "triển, trạng thái cân bằng bị phá vỡ và vật liệu áp điện sinh ra điện tích. Nếu ứng suất "
        "được duy trì một lúc, các điện tích lại bị trung hòa bởi dòng rò nội. Như vậy, vật liệu áp "
        "điện chỉ đáp ứng với nhiệt độ thay đổi chứ không phải với mức nhiệt độ không đổi. Nói cách "
        "khác, cảm biến áp điện là thiết bị xoay chiều (ac), chứ không phải một chiều (dc). Đôi khi "
        "nó được gọi là cảm biến động, phản ánh bản chất đáp ứng của nó."))
    b.append(F65(lang))

    # ====================================================== Pyroelectric Sensors
    b.append(H3("Pyroelectric Sensors", "Cảm biến áp điện"))
    b.append(P(
        "To make sensors, the pyroelectric materials are used in the form of thin slices or films "
        "with electrodes deposited on the opposite sides to collect the thermally induced charges "
        "(Figure 32.66). The pyroelectric detector is essentially a capacitor that can be charged "
        "by an influx of heat. The detector does not require any external electrical bias "
        "(excitation signal). It needs only an appropriate electronic interface circuit to measure "
        "the charge. Contrary to thermoelectrics (thermocouples), which produce a steady voltage "
        "when two dissimilar metal junctions are held at steady but different temperatures, "
        "pyroelectrics generate charge in response to a change in temperature. Since a change in "
        "temperature essentially requires propagation of heat, a pyroelectric device is a heat flow "
        "detector rather than a heat detector. Figure 32.66 shows a pyroelectric detector "
        "(pyro-sensor) connected to a resistor <i>R</i><sub>b</sub> that represents either the "
        "internal leakage resistance or a combined input resistance of the interface circuit "
        "connected to the sensor. The equivalent electrical circuit of the sensor is shown on the "
        "right. It consists of three components: (1) the current source generating a heat induced "
        "current, <i>i</i>, (remember that a current is a movement of electric charges), (2) the "
        "sensor's capacitance, <i>C</i>, and (3) the leakage resistance, <i>R</i><sub>b</sub>. "
        "Since the leakage resistance is very high and often unpredictable, an additional bias "
        "resistor is often connected in parallel with the pyroelectric material. The value of that "
        "resistor is much smaller than the leakage resistance, yet its typical value is still on "
        "the order of 10¹⁰ Ω (10 GΩ).",
        "Để làm cảm biến, vật liệu áp điện được dùng dưới dạng lát mỏng hoặc màng với các điện cực "
        "được lắng đọng ở hai mặt đối diện để thu các điện tích cảm ứng nhiệt (Hình 32.66). Bộ dò "
        "áp điện về bản chất là một tụ điện có thể được nạp bởi một luồng nhiệt đi vào. Bộ dò không "
        "cần bất kỳ phân cực điện ngoài nào (tín hiệu kích thích). Nó chỉ cần một mạch giao tiếp "
        "điện tử thích hợp để đo điện tích. Trái ngược với cặp nhiệt điện (thermocouple) sinh ra "
        "điện áp ổn định khi hai mối nối kim loại khác nhau được giữ ở các nhiệt độ khác nhau nhưng "
        "không đổi, các áp điện sinh điện tích đáp ứng với sự thay đổi nhiệt độ. Vì sự thay đổi "
        "nhiệt độ về cơ bản đòi hỏi sự lan truyền của nhiệt, thiết bị áp điện là bộ dò dòng nhiệt "
        "chứ không phải bộ dò nhiệt. Hình 32.66 trình bày một bộ dò áp điện (cảm biến pyro) nối với "
        "điện trở <i>R</i><sub>b</sub> đại diện cho điện trở rò nội hoặc điện trở đầu vào kết hợp "
        "của mạch giao tiếp nối với cảm biến. Mạch điện tương đương của cảm biến được vẽ bên phải. "
        "Nó gồm ba thành phần: (1) nguồn dòng sinh dòng cảm ứng nhiệt <i>i</i> (nhớ rằng dòng là sự "
        "vận động của các điện tích), (2) điện dung cảm biến <i>C</i>, và (3) điện trở rò "
        "<i>R</i><sub>b</sub>. Vì điện trở rò rất cao và thường khó đoán trước, người ta thường nối "
        "song song với vật liệu áp điện một điện trở phân cực bổ sung. Giá trị điện trở đó nhỏ hơn "
        "nhiều so với điện trở rò, nhưng giá trị điển hình của nó vẫn thuộc hàng 10¹⁰ Ω (10 GΩ)."))
    b.append(F66(lang))
    b.append(P(
        "The output signal from the pyroelectric sensor can be taken in the form of either charge "
        "(current) or voltage, depending on the application. Being a capacitor, the pyroelectric "
        "device is discharged when connected to a resistor, <i>R</i><sub>b</sub> (Figure 32.66). "
        "Electric current through the resistor and voltage across the resistor represent the heat "
        "flow-induced charge. It can be characterized by two pyroelectric coefficients [2]:",
        "Tín hiệu ra từ cảm biến áp điện có thể lấy dưới dạng điện tích (dòng) hoặc điện áp, tùy "
        "ứng dụng. Là một tụ điện, thiết bị áp điện bị xả khi nối với điện trở <i>R</i><sub>b</sub> "
        "(Hình 32.66). Dòng điện qua điện trở và điện áp trên điện trở biểu diễn điện tích do dòng "
        "nhiệt gây ra. Nó có thể được đặc trưng bằng hai hệ số áp điện [2]:"))
    b.append(EQ("<i>p</i><sub>Q</sub> = " + FR("d<i>P</i><sub>s</sub>", "d<i>T</i>")
                + " &nbsp;(pyroelectric charge coefficient)<br>"
                + "<i>p</i><sub>V</sub> = " + FR("d<i>P</i><sub>s</sub>", "d<i>E</i>")
                + " &nbsp;(pyroelectric voltage coefficient)", "32.123"))
    b.append(P(
        "Both coefficients are related by way of the electric permittivity, <i>ε</i><sub>r</sub>, and "
        "dielectric constant, <i>ε</i><sub>0</sub>:",
        "Cả hai hệ số liên hệ qua điện thẩm điện, <i>ε</i><sub>r</sub>, và hằng số điện môi, "
        "<i>ε</i><sub>0</sub>:"))
    b.append(EQ("<i>p</i><sub>V</sub> = " + FR("<i>p</i><sub>Q</sub>",
                "<i>ε</i><sub>r</sub> <i>ε</i><sub>0</sub>"), "32.124"))
    b.append(P(
        "If a pyroelectric material is exposed to a heat source, its temperature rises by Δ<i>T</i>, "
        "and the corresponding charge and voltage changes can be described by the following "
        "equations:",
        "Nếu vật liệu áp điện được tiếp xúc với một nguồn nhiệt, nhiệt độ của nó tăng lên Δ<i>T</i>, "
        "và sự thay đổi điện tích cũng như điện áp tương ứng có thể mô tả bằng các phương trình sau:"))
    b.append(EQ("Δ<i>Q</i> = <i>p</i><sub>Q</sub> <i>A</i> Δ<i>T</i>", "32.125"))
    b.append(EQ("Δ<i>V</i> = <i>p</i><sub>V</sub> <i>h</i> Δ<i>T</i>", "32.126"))
    b.append(P(
        "Remembering that the sensor's capacitance can be defined as:",
        "Nhớ rằng điện dung cảm biến có thể xác định bởi:"))
    b.append(EQ("<i>C</i> = " + FR("<i>ε</i><sub>r</sub> <i>ε</i><sub>0</sub> <i>A</i>", "<i>h</i>"),
                "32.127"))
    b.append(P(
        "then, from Equations 32.124, 32.126, and 32.127, it follows that:",
        "khi đó, từ các Phương trình 32.124, 32.126 và 32.127, ta có:"))
    b.append(EQ("Δ<i>V</i> = " + FR("<i>p</i><sub>Q</sub> <i>A</i> Δ<i>T</i>", "<i>C</i>")
                + " = " + FR("<i>p</i><sub>Q</sub> <i>h</i> Δ<i>T</i>",
                             "<i>ε</i><sub>r</sub> <i>ε</i><sub>0</sub>"), "32.128"))
    b.append(P(
        "It is seen that the peak output voltage is proportional to the sensor's temperature rise "
        "and pyroelectric charge coefficient and inversely proportional to its thickness.",
        "Ta thấy điện áp ra đỉnh tỉ lệ với độ tăng nhiệt độ của cảm biến và hệ số điện tích áp "
        "điện, đồng thời tỉ lệ nghịch với chiều dày của nó."))
    b.append(P(
        "Figure 32.67 shows a pyroelectric sensor whose temperature, <i>T</i><sub>0</sub>, is "
        "homogeneous over its volume. Being electrically polarized, the dipoles are oriented (poled) "
        "in such a manner as to make one side of the material positive and the opposite side "
        "negative. However, under steady-state conditions, free charge carriers (electrons and "
        "holes) neutralize the polarized charge and the capacitance between the electrodes does not "
        "appear to be charged. That is, the sensor generates zero charge. Now, assume that heat is "
        "applied to the bottom side of the sensor. Heat can enter the sensor in a form of thermal "
        "radiation that is absorbed by the bottom electrode and propagates toward the pyroelectric "
        "material via the mechanism of thermal conduction. The bottom electrode can be given a "
        "heat-absorbing coating, such as goldblack or organic paint. As a result of heat absorption, "
        "the bottom side becomes warmer (the new temperature is <i>T</i><sub>1</sub>), which causes "
        "the bottom side of the material to expand. The expansion leads to flexing of the sensor, "
        "which, in turn, produces stress and a change in dipole orientation. Being piezoelectric, "
        "stressed material generates electric charges of opposite polarities across the electrodes. "
        "Hence, one can regard secondary pyroelectricity as a sequence of events: a thermal "
        "radiation — a heat absorption — a thermally induced stress — an electric charge.",
        "Hình 32.67 trình bày một cảm biến áp điện có nhiệt độ <i>T</i><sub>0</sub> đồng nhất trên "
        "toàn bộ thể tích. Được phân cực về điện, các lưỡng cực định hướng (poled) sao cho một mặt "
        "vật liệu dương và mặt đối diện âm. Tuy nhiên, trong điều kiện tĩnh, các hạt tải tự do "
        "(electron và lỗ trống) trung hòa điện tích phân cực và điện dung giữa các điện cực dường "
        "như không được nạp. Nghĩa là cảm biến sinh điện tích bằng không. Giờ giả sử nhiệt được cấp "
        "vào mặt đáy của cảm biến. Nhiệt có thể đi vào cảm biến dưới dạng bức xạ nhiệt bị điện cực "
        "đáy hấp thụ và truyền đến vật liệu áp điện qua cơ chế dẫn nhiệt. Điện cực đáy có thể được "
        "phủ một lớp hấp thụ nhiệt, như goldblack hoặc sơn hữu cơ. Kết quả của việc hấp thụ nhiệt, "
        "mặt đáy trở nên ấm hơn (nhiệt độ mới là <i>T</i><sub>1</sub>), khiến mặt đáy vật liệu nở "
        "ra. Sự nở này dẫn đến uốn cong cảm biến, đến lượt nó sinh ứng suất và làm thay đổi định "
        "hướng lưỡng cực. Là vật liệu áp điện, vật liệu chịu ứng suất sinh ra các điện tích có cực "
        "trái dấu qua các điện cực. Do đó, có thể xem áp điện thứ cấp như một chuỗi sự kiện: bức xạ "
        "nhiệt — hấp thụ nhiệt — ứng suất cảm ứng nhiệt — điện tích điện."))
    b.append(F67(lang))
    b.append(P(
        "The temperature of the sensor <i>T</i><sub>s</sub> is a function of time. That function is "
        "dependent on the sensing element: its density, specific heat, and thickness. If the input "
        "thermal flux has the shape of a step function of time, for the sensor freely mounted in "
        "air, the output current can be approximated by an exponential function, so that:",
        "Nhiệt độ cảm biến <i>T</i><sub>s</sub> là hàm của thời gian. Hàm đó phụ thuộc vào phần tử "
        "cảm biến: khối lượng riêng, nhiệt dung riêng và chiều dày của nó. Nếu thông lượng nhiệt "
        "vào có dạng hàm bước theo thời gian, với cảm biến lắp tự do trong không khí, dòng ra có "
        "thể xấp xỉ bằng một hàm số mũ, do đó:"))
    b.append(EQ("<i>i</i> = <i>i</i><sub>0</sub> e<sup>−<i>t</i>/τ<sub>T</sub></sup>", "32.129"))
    b.append(P(
        "Figure 32.68 shows timing diagrams for a pyroelectric sensor when it is exposed to a step "
        "function of heat. It is seen that the electric charge reaches its peak value almost "
        "instantaneously, and then decays with a thermal time constant, <i>τ</i><sub>T</sub>. This "
        "time constant is a product of the sensor's thermal capacitance, <i>C</i>, and thermal "
        "resistance, <i>r</i>, which defines a thermal loss from the sensing element to its "
        "surroundings:",
        "Hình 32.68 trình bày các giản đồ thời gian cho một cảm biến áp điện khi nó chịu một hàm "
        "bước nhiệt. Ta thấy điện tích điện đạt giá trị đỉnh gần như tức thời, rồi suy giảm với "
        "hằng số thời gian nhiệt <i>τ</i><sub>T</sub>. Hằng số thời gian này là tích của điện dung "
        "nhiệt cảm biến <i>C</i> và điện trở nhiệt <i>r</i>, xác định sự thất thoát nhiệt từ phần "
        "tử cảm biến ra môi trường xung quanh:"))
    b.append(EQ("τ<sub>T</sub> = <i>C</i> <i>r</i> = <i>c</i> <i>A</i> <i>h</i> <i>r</i>", "32.130"))
    b.append(P(
        "The thermal resistance <i>r</i> is a function of all thermal losses to the surroundings "
        "through convection, conduction, and thermal radiation. For low-frequency applications, it "
        "is desirable to use sensors with <i>τ</i><sub>T</sub> as large as practical; while for the "
        "high-speed applications (e.g., to measure the power of laser pulses), a thermal time "
        "constant should be dramatically reduced. For that purpose, the pyroelectric material can "
        "be laminated with a heat sink: a piece of aluminum or copper.",
        "Điện trở nhiệt <i>r</i> là hàm của mọi thất thoát nhiệt ra môi trường qua đối lưu, dẫn "
        "nhiệt và bức xạ nhiệt. Với các ứng dụng tần số thấp, nên dùng cảm biến có <i>τ</i>"
        "<sub>T</sub> lớn thực tế càng tốt; còn với các ứng dụng tốc độ cao (ví dụ đo công suất xung "
        "laser), hằng số thời gian nhiệt phải được giảm mạnh. Với mục đích đó, vật liệu áp điện có "
        "thể được dán chồng với một tản nhiệt: một miếng nhôm hoặc đồng."))
    b.append(P(
        "When a heat flow exists inside the pyroelectric crystal, there is an outflow of heat from "
        "the opposite side of the crystal, as shown in Figure 32.67. Thermal energy enters the "
        "pyroelectric material from side a. Since the other side b of the sensor faces a cooler "
        "environment, part of the thermal energy leaves the sensor and is lost to its surroundings. "
        "Because the sides a and b face objects of different temperatures (one is the temperature of "
        "a target and the other is the temperature of the environment), a continuous heat flow exists "
        "through the pyroelectric material. As a result, in Figure 32.68, charge <i>Q</i> and "
        "voltage <i>V</i> do not completely return to zero, no matter how much time has elapsed. "
        "Electric current generated by the pyroelectric sensor has the same shape as the thermal "
        "current through its material. An accurate measurement can demonstrate that as long as the "
        "heat continues to flow, the pyroelectric sensor will generate a constant voltage <i>V</i><sub>0</sub> "
        "whose magnitude is proportional to the heat flow.",
        "Khi có dòng nhiệt bên trong tinh thể áp điện, có một dòng nhiệt thoát ra mặt đối diện của "
        "tinh thể, như thể hiện ở Hình 32.67. Năng lượng nhiệt đi vào vật liệu áp điện từ mặt a. Vì "
        "mặt b kia của cảm biến hướng về môi trường mát hơn, một phần năng lượng nhiệt rời khỏi cảm "
        "biến và thất thoát ra môi trường. Do hai mặt a và b hướng về các vật có nhiệt độ khác nhau "
        "(một là nhiệt độ của mục tiêu và kia là nhiệt độ môi trường), nên có một dòng nhiệt liên "
        "tục chảy qua vật liệu áp điện. Kết quả là, trong Hình 32.68, điện tích <i>Q</i> và điện áp "
        "<i>V</i> không hoàn toàn trở về không, bất kể bao nhiêu thời gian trôi qua. Dòng điện do "
        "cảm biến áp điện sinh ra có cùng hình dạng với dòng nhiệt qua vật liệu của nó. Đo lường "
        "chính xác có thể chứng minh rằng miễn là nhiệt tiếp tục chảy, cảm biến áp điện sẽ sinh ra "
        "một điện áp không đổi <i>V</i><sub>0</sub> có độ lớn tỉ lệ với dòng nhiệt."))
    b.append(F68(lang))

    # ============================================================ Applications
    b.append(H3("Applications", "Ứng dụng"))
    b.append(P(
        "The pyroelectric sensors are useful whenever changing thermal radiation or heat flow need "
        "to be measured. Examples are motion detectors for the security systems and light control "
        "switches [1], instant medical infrared thermometers, and laser power meters. Depending on "
        "the application, a pyroelectric sensor can be used either in current or in voltage mode. "
        "The voltage mode (Figure 32.69A) uses a voltage follower with a very high input resistance. "
        "Hence, JFET and CMOS input stages are essential. As a rule, in the voltage mode sensor, the "
        "follower is incorporated inside the same package along with the element and bias resistor. "
        "Advantages of the voltage mode are simplicity and lower noise. The disadvantages are slower "
        "speed response due to high capacitance of the sensor (typically on the order of 30 pF) and "
        "other influences of the sensor capacitance on the quality of output voltage. The output "
        "voltage of the follower is shown in Figure 32.68 (V). It is seen that it rises slowly with "
        "electric time constant <i>τ</i><sub>e</sub> and decays with thermal time constant "
        "<i>τ</i><sub>T</sub>.",
        "Cảm biến áp điện hữu ích bất cứ khi nào cần đo bức xạ nhiệt thay đổi hoặc dòng nhiệt. Ví "
        "dụ là các cảm biến chuyển động cho hệ thống an ninh và công tắc điều khiển đèn [1], các "
        "nhiệt kế hồng ngoại y tế tức thời, và các đồng hồ đo công suất laser. Tùy ứng dụng, cảm "
        "biến áp điện có thể dùng ở chế độ dòng hoặc chế độ điện áp. Chế độ điện áp (Hình 32.69A) "
        "dùng một bộ theo điện áp có điện trở đầu vào rất cao. Do đó, các tầng đầu vào JFET và CMOS "
        "là thiết yếu. Thông lệ, trong cảm biến chế độ điện áp, bộ theo được tích hợp trong cùng vỏ "
        "với phần tử và điện trở phân cực. Ưu điểm của chế độ điện áp là đơn giản và nhiễu thấp. Nhược "
        "điểm là đáp ứng chậm hơn do điện dung cao của cảm biến (điển hình thuộc hàng 30 pF) và các "
        "ảnh hưởng khác của điện dung cảm biến lên chất lượng điện áp ra. Điện áp ra của bộ theo "
        "được vẽ trong Hình 32.68 (V). Ta thấy nó tăng chậm với hằng số thời gian điện <i>τ</i>"
        "<sub>e</sub> và suy giảm với hằng số thời gian nhiệt <i>τ</i><sub>T</sub>."))
    b.append(P(
        "The current mode uses an electronic circuit having a 'virtual ground' as its input "
        "(Figure 32.69B). An advantage of this circuit is that the output signal is independent of "
        "the sensor's capacitance and, as a result, is much faster. The signal reaches its peak "
        "value relatively fast and decays with thermal time constant <i>τ</i><sub>T</sub>. The output "
        "voltage <i>V</i><sub>0</sub> has the same shape of charge <i>Q</i> in Figure 32.68. The "
        "disadvantages of the circuit are higher noise (due to wider bandwidth) and higher cost.",
        "Chế độ dòng dùng một mạch điện tử có 'nối đất ảo' làm đầu vào (Hình 32.69B). Ưu điểm của "
        "mạch này là tín hiệu ra độc lập với điện dung cảm biến và do đó nhanh hơn nhiều. Tín hiệu "
        "đạt giá trị đỉnh tương đối nhanh và suy giảm với hằng số thời gian nhiệt <i>τ</i>"
        "<sub>T</sub>. Điện áp ra <i>V</i><sub>0</sub> có cùng hình dạng với điện tích <i>Q</i> "
        "trong Hình 32.68. Nhược điểm của mạch là nhiễu cao hơn (do băng thông rộng hơn) và chi phí "
        "cao hơn."))
    b.append(P(
        "Note that Figure 32.69 shows dual pyroelectric sensors, where two sensing elements are "
        "formed on the same crystalline plate by depositing two pairs of electrodes. The electrodes "
        "are connected in a serial-opposite manner. If both sensors are exposed to the same "
        "magnitude of far-infrared radiation, they will produce nearly identical polarizations and, "
        "due to the opposite connection, the voltage applied to the input of the transistor or the "
        "current passing through resistor <i>R</i><sub>b</sub> will be nullified. This feature "
        "allows for cancellation of undesirable common-mode input signals in order to improve "
        "stability and reduce noise. Signals that arrive only to one of the elements will not be "
        "canceled.",
        "Lưu ý Hình 32.69 trình bày các cảm biến áp điện kép, trong đó hai phần tử cảm biến được "
        "tạo trên cùng một tấm tinh thể bằng cách lắng đọng hai cặp điện cực. Các điện cực được nối "
        "theo kiểu nối tiếp-ngược. Nếu cả hai cảm biến chịu cùng một cường độ bức xạ hồng ngoại xa, "
        "chúng sẽ sinh ra các phân cực gần như đồng nhất và, do nối ngược, điện áp đưa vào đầu vào "
        "của transistor hoặc dòng qua điện trở <i>R</i><sub>b</sub> sẽ bị triệt tiêu. Tính năng này "
        "cho phép loại bỏ các tín hiệu đầu vào kiểu chung không mong muốn nhằm cải thiện độ ổn định "
        "và giảm nhiễu. Các tín hiệu chỉ đến một trong hai phần tử sẽ không bị triệt tiêu."))
    b.append(F69(lang))

    b.append(refs(lang))
    return "".join(b)


def sec_vi():
    return _section("vi")


def sec_en():
    return _section("en")
