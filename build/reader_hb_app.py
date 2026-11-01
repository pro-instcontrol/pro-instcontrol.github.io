# -*- coding: utf-8 -*-
"""Handbook Appendix A — Units and Conversions (B. W. Petley, National Physical
Laboratory).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_app.py
"""
import os

from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "appendix-a-units-and-conversions"
TITLE_EN = "Units and Conversions"
TITLE_VI = "Đơn vị và quy đổi"
BYLINE = "B. W. Petley · National Physical Laboratory"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


# ---------------------------------------------------------------- markup

def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def note(t):
    return '<div class="note">%s</div>' % t


def table(hd, rows, cap, cls="tbl"):
    """rows may contain ("grp", "group label") tuples for a section row."""
    body = []
    for r in rows:
        if isinstance(r, tuple) and r and r[0] == "grp":
            body.append('<tr class="grp"><td colspan="%d">%s</td></tr>' % (len(hd), r[1]))
        else:
            body.append("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r))
    return ('<div class="table-wrap"><table class="%s"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, "".join("<th>%s</th>" % h for h in hd), "".join(body), cap))


def foots(items):
    return ('<p style="font-size:.82rem;color:#777;line-height:1.7;margin:-.4rem 0 1.4rem">'
            + "<br>".join(items) + "</p>")


# ---------------------------------------------------------------- data

# Table A.1 — the seven SI base units
T_A1 = [
    ("Chiều dài", "Length", "mét", "meter", "m"),
    ("Khối lượng", "Mass", "kilôgam", "kilogram", "kg"),
    ("Thời gian", "Time", "giây", "second", "s"),
    ("Cường độ dòng điện", "Electric current", "ampe", "ampere", "A"),
    ("Nhiệt độ nhiệt động", "Thermodynamic temperature", "kelvin", "kelvin", "K"),
    ("Lượng chất", "Amount of substance", "mol", "mole", "mol"),
    ("Cường độ sáng", "Luminous intensity", "candela", "candela", "cd"),
]

# Table A.2 — international definitions of the SI base units
T_A2 = [
    ("Đơn vị chiều dài (mét)", "Unit of length (meter)",
     "Mét là chiều dài đường đi của ánh sáng trong chân không trong khoảng thời gian "
     "1/299 792 458 giây (CGPM<sup>b</sup> lần thứ 17, 1983, Nghị quyết 1).",
     "The meter is the length of the path traveled by light in vacuum during a time interval "
     "of 1/299 792 458 of a second (17th CGPM, 1983, Resolution 1).",
     "Mẫu chuẩn quốc tế ban đầu, làm bằng platin–iridi, được lưu giữ tại BIPM<sup>c</sup> theo "
     "các điều kiện do CGPM lần thứ nhất (1889) quy định.",
     "The original international prototype, made of platinum-iridium, is kept at the BIPM under "
     "conditions specified by the 1st CGPM in 1889."),

    ("Đơn vị khối lượng (kilôgam)", "Unit of mass (kilogram)",
     "Kilôgam là đơn vị khối lượng: nó bằng khối lượng của mẫu chuẩn quốc tế của kilôgam "
     "(CGPM lần thứ 3, 1901).",
     "The kilogram is the unit of mass: it is equal to the mass of the international prototype "
     "of the kilogram (3rd CGPM, 1901).",
     "", ""),

    ("Đơn vị thời gian (giây)", "Unit of time (second)",
     "Giây là khoảng thời gian bằng 9 192 631 770 chu kỳ của bức xạ tương ứng với sự chuyển "
     "giữa hai mức siêu tinh tế của trạng thái cơ bản của nguyên tử xesi-133 (CGPM lần thứ 13, "
     "1967, Nghị quyết 1).",
     "The second is the duration of 9 192 631 770 periods of the radiation corresponding to the "
     "transition between the two hyperfine levels of the ground state of the cesium-133 atom "
     "(13th CGPM, 1967, Resolution 1).",
     "", ""),

    ("Đơn vị cường độ dòng điện (ampe)", "Unit of electric current (ampere)",
     "Ampe là cường độ của một dòng điện không đổi mà, khi được duy trì trong hai dây dẫn "
     "thẳng, song song, dài vô hạn, tiết diện tròn không đáng kể, đặt cách nhau 1 mét trong "
     "chân không, sẽ sinh ra giữa hai dây dẫn đó một lực bằng 2 × 10⁻⁷ niutơn trên mỗi mét "
     "chiều dài (CIPM, 1946, Nghị quyết 2, được CGPM lần thứ 9, 1948 phê chuẩn).",
     "The ampere is that constant current which, if maintained in two straight parallel "
     "conductors of infinite length, of negligible cross section, and placed 1 meter apart in "
     "vacuum, would produce between these conductors a force equal to 2 × 10⁻⁷ newton per meter "
     "of length (CIPM, 1946, Resolution 2 approved by the 9th CGPM, 1948).",
     "Cụm từ “đơn vị lực MKS” trong văn bản gốc được thay ở đây bằng “niutơn”, tên mà CGPM lần "
     "thứ 9 (1948, Nghị quyết 7) đã đặt cho đơn vị này.",
     "The expression “MKS unit of force” which occurs in the original text has been replaced here "
     "by “newton,” a name adopted for this unit by the 9th CGPM (1948), Resolution 7."),

    ("Đơn vị nhiệt độ nhiệt động (kelvin)", "Unit of thermodynamic temperature (kelvin)",
     "Kelvin, đơn vị của nhiệt độ nhiệt động, là phân số 1/273,16 của nhiệt độ nhiệt động của "
     "điểm ba của nước (CGPM lần thứ 13, 1967, Nghị quyết 4).",
     "The kelvin, unit of thermodynamic temperature, is the fraction 1/273.16 of the "
     "thermodynamic temperature of the triple point of water (13th CGPM, 1967, Resolution 4).",
     "CGPM lần thứ 13 (1967, Nghị quyết 3) cũng quyết định rằng đơn vị kelvin và ký hiệu K của "
     "nó phải được dùng để biểu diễn một khoảng hay một hiệu nhiệt độ. Ngoài nhiệt độ nhiệt động "
     "(ký hiệu T), tính bằng kelvin, người ta còn dùng nhiệt độ Celsius (ký hiệu t) xác định bởi "
     "phương trình t = T − T<sub>0</sub>, trong đó T<sub>0</sub> = 273,15 K theo định nghĩa. Để "
     "biểu diễn nhiệt độ Celsius, dùng đơn vị “độ Celsius”, bằng đơn vị “kelvin”; ở đây “độ "
     "Celsius” là một tên riêng dùng thay cho “kelvin”. Tuy vậy, một khoảng hay hiệu nhiệt độ "
     "Celsius có thể biểu diễn bằng kelvin cũng như bằng độ Celsius.",
     "The 13th CGPM (1967, Resolution 3) also decided that the unit kelvin and its symbol K "
     "should be used to express an interval or a difference in temperature. In addition to the "
     "thermodynamic temperature (symbol T), expressed in kelvin, use is also made of Celsius "
     "temperature (symbol t) defined by the equation t = T − T₀, where T₀ = 273.15 K by "
     "definition. To express Celsius temperature, the unit “degree Celsius” which is equal to the "
     "unit “kelvin” is used; in this case “degree Celsius” is a special name used in place of "
     "“kelvin.” An interval or difference of Celsius temperature can, however, be expressed in "
     "kelvins as well as degrees Celsius."),

    ("Đơn vị lượng chất (mol)", "Unit of amount of substance (mole)",
     "1. Mol là lượng chất của một hệ chứa số thực thể cơ bản bằng số nguyên tử có trong "
     "0,012 kilôgam cacbon-12. 2. Khi dùng mol, các thực thể cơ bản phải được chỉ rõ và có thể "
     "là nguyên tử, phân tử, ion, điện tử, các hạt khác, hoặc những nhóm xác định của các hạt đó.",
     "1. The mole is the amount of substance of a system which contains as many elementary "
     "entities as there are atoms in 0.012 kilogram of carbon-12. 2. When the mole is used, the "
     "elementary entities must be specified and may be atoms, molecules, ions, electrons, other "
     "particles, or specified groups of such particles.",
     "Trong định nghĩa mol, hiểu rằng đang nói tới các nguyên tử cacbon-12 không liên kết, ở "
     "trạng thái nghỉ và ở trạng thái cơ bản. Định nghĩa này đồng thời xác định bản chất của đại "
     "lượng mà đơn vị của nó là mol.",
     "In the definition of the mole, it is understood that unbound atoms of carbon-12, at rest, "
     "and in their ground state, are referred to. This definition specifies at the same time the "
     "nature of the quantity whose unit is the mole."),

    ("Đơn vị cường độ sáng (candela)", "Unit of luminous intensity (candela)",
     "Candela là cường độ sáng, theo một hướng cho trước, của một nguồn phát bức xạ đơn sắc có "
     "tần số 540 × 10¹² hertz và có cường độ bức xạ theo hướng đó bằng (1/683) oát trên "
     "steradian (CGPM lần thứ 16, 1979, Nghị quyết 3).",
     "The candela is the luminous intensity, in a given direction, of a source that emits "
     "monochromatic radiation of frequency 540 × 10¹² hertz and that has a radiant intensity in "
     "that direction of (1/683) watt per steradian (16th CGPM, 1979, Resolution 3).",
     "", ""),
]

# Table A.3 — SI derived units with special names
# (quantity_vi, quantity_en, name_vi, name_en, symbol, in_other, in_base)
T_A3 = [
    ("Góc phẳng", "Plane angle", "radian", "radian", "rad", "m·m⁻¹", "m·m⁻¹"),
    ("Góc khối", "Solid angle", "steradian", "steradian", "sr", "m²·m⁻²", "m²·m⁻²"),
    ("Tần số", "Frequency", "hertz", "hertz", "Hz", "s⁻¹", "s⁻¹"),
    ("Lực", "Force", "niutơn", "newton", "N", "m·kg·s⁻²", "m·kg·s⁻²"),
    ("Áp suất, ứng suất", "Pressure, stress", "pascal", "pascal", "Pa", "N·m⁻²",
     "m⁻¹·kg·s⁻²"),
    ("Năng lượng, công, lượng nhiệt", "Energy, work, quantity of heat", "jun", "joule", "J",
     "N·m", "m²·kg·s⁻²"),
    ("Công suất, thông lượng bức xạ", "Power, radiant flux", "oát", "watt", "W", "J·s⁻¹",
     "m²·kg·s⁻³"),
    ("Điện tích, lượng điện", "Electric charge, quantity of electricity", "culông", "coulomb",
     "C", "s·A", "s·A"),
    ("Điện thế, hiệu điện thế, sức điện động",
     "Electric potential, potential difference, electromotive force", "vôn", "volt", "V",
     "W·A⁻¹", "m²·kg·s⁻³·A⁻¹"),
    ("Điện dung", "Capacitance", "fara", "farad", "F", "C·V⁻¹", "m⁻²·kg⁻¹·s⁴·A²"),
    ("Điện trở", "Electric resistance", "ôm", "ohm", "Ω", "V·A⁻¹", "m²·kg·s⁻³·A⁻²"),
    ("Điện dẫn", "Electric conductance", "siemens", "siemens", "S", "A·V⁻¹",
     "m⁻²·kg⁻¹·s³·A²"),
    ("Từ thông", "Magnetic flux", "vêbe", "weber", "Wb", "V·s", "m²·kg·s⁻²·A⁻¹"),
    ("Mật độ từ thông", "Magnetic flux density", "tesla", "tesla", "T", "Wb·m⁻²",
     "kg·s⁻²·A⁻¹"),
    ("Điện cảm", "Inductance", "henry", "henry", "H", "Wb·A⁻¹", "m²·kg·s⁻²·A⁻²"),
    ("Nhiệt độ Celsius", "Celsius temperature", "độ Celsius", "degree Celsius", "°C", "K", "K"),
    ("Thông lượng sáng", "Luminous flux", "lumen", "lumen", "lm", "cd·sr", "cd"),
    ("Độ rọi", "Illuminance", "lux", "lux", "lx", "lm·m⁻²", "m⁻²·cd·sr = m⁻²·cd"),
    ("Độ phóng xạ (của một hạt nhân phóng xạ)",
     "Activity (referred to a radionuclide)", "becơren", "becquerel", "Bq", "s⁻¹", "s⁻¹"),
    ("Liều hấp thụ, năng lượng riêng truyền, kerma",
     "Absorbed dose, specific energy imparted, kerma", "gray", "gray", "Gy", "J·kg⁻¹",
     "m²·s⁻²"),
    ("Liều tương đương, liều tương đương môi trường, liều tương đương cơ quan",
     "Dose equivalent, ambient dose equivalent, organ equivalent dose", "sievert", "sievert",
     "Sv", "J·kg⁻¹", "m²·s⁻²"),
]

# Table A.4 — SI prefixes: (factor, name_vi, name_en, symbol)
T_A4 = [
    ("10²⁴", "yôta", "yotta", "Y"), ("10⁻¹", "đêxi", "deci", "d"),
    ("10²¹", "zêta", "zetta", "Z"), ("10⁻²", "xenti", "centi", "c"),
    ("10¹⁸", "êxa", "exa", "E"), ("10⁻³", "mili", "milli", "m"),
    ("10¹⁵", "pêta", "peta", "P"), ("10⁻⁶", "micrô", "micro", "µ"),
    ("10¹²", "têra", "tera", "T"), ("10⁻⁹", "nanô", "nano", "n"),
    ("10⁹", "giga", "giga", "G"), ("10⁻¹²", "picô", "pico", "p"),
    ("10⁶", "mêga", "mega", "M"), ("10⁻¹⁵", "femtô", "femto", "f"),
    ("10³", "kilô", "kilo", "k"), ("10⁻¹⁸", "atô", "atto", "a"),
    ("10²", "héctô", "hecto", "h"), ("10⁻²¹", "zêptô", "zepto", "z"),
    ("10", "đêca", "deca", "da"), ("10⁻²⁴", "yóctô", "yocto", "y"),
]


def _rows_a4(lang):
    """Two prefix columns side by side, as printed."""
    half = len(T_A4) // 2
    rows = []
    for i in range(half):
        f1, n1v, n1e, s1 = T_A4[i]
        f2, n2v, n2e, s2 = T_A4[i + half]
        n1 = n1v if lang == "vi" else n1e
        n2 = n2v if lang == "vi" else n2e
        rows.append([f1, n1, s1, f2, n2, s2])
    return rows


# Table A.5 — conversion factors from English measures to SI units.
# (group_vi, group_en, [(unit, equivalent_vi, equivalent_en)])
def _u(u, vi, en=None):
    """(unit label VI, equivalent VI, unit label EN or None to reuse the VI one)."""
    return (u, vi, en)


T_A5 = [
    ("1. Gia tốc", "1. Acceleration", [
        _u("Gia tốc rơi tự do, trọng trường chuẩn", "9,806 65 m/s²",
           "Acceleration of free fall, standard gravity"),
        _u("1 ft/s²", "0,304 8 m/s²"),
        _u("1 gal", "0,01 m/s²"),
    ]),
    ("2. Góc", "2. Angle", [
        _u("1 giây (\")", "4,848 1 × 10⁻⁶ rad", "1 second (\")"),
        _u("1 phút (′)", "2,908 9 × 10⁻⁴ rad", "1 minute (′)"),
        _u("1 độ (°)", "0,017 453 2 rad", "1 degree (°)"),
        _u("1 rad", "206 264,8″"),
    ]),
    ("3. Diện tích", "3. Area", [
        _u("1 barn (b)", "10⁻²⁸ m²"),
        _u("1 in.²", "6,451 6 × 10⁻⁴ m²"),
        _u("1 ft²", "0,092 903 04 m²"),
        _u("1 yd²", "0,836 127 36 m²"),
        _u("1 are", "100 m²"),
        _u("1 acre [43 560 (ft chuẩn)²]", "4 046,86 m²", "1 acre [43 560 (statute ft)²]"),
        _u("1 hécta", "10 000 m²", "1 hectare"),
        _u("1 mi²", "2,590 0 × 10⁶ m²"),
        _u("1 dặm vuông (theo ft khảo sát Hoa Kỳ)", "2,589 998 km²",
           "1 square mile (based on U.S. survey foot)"),
    ]),
    ("4. Nồng độ, khối lượng riêng, mật độ khối",
     "4. Concentration, Density, Mass Density", [
        _u("1 grain/gal (U.S.)", "0,017 118 kg/m³"),
        _u("1 lb/ft³", "16,018 46 kg/m³"),
        _u("1 lb/gal (U.S.)", "119,826 4 kg/m³"),
        _u("1 short ton/yd³", "1 186,6 kg/m³"),
        _u("1 long ton/yd³", "1 328,9 kg/m³"),
        _u("1 oz (avdp)/in.³", "1 730,0 kg/m³"),
        _u("1 oz (avdp)/gal (U.S.)", "7,489 152 kg/m³"),
        _u("1 lb/in.³", "27 680 kg/m³"),
    ]),
    ("5. Năng lượng", "5. Energy", [
        _u("1 ft·lbf", "1,355 818 J"),
        _u("1 cal<sub>th</sub> (calo nhiệt hoá)", "4,184 J", "1 cal_th (thermochemical calorie)"),
        _u("1 cal<sub>15</sub> (calo 15 °C)", "4,185 5 J", "1 cal_15 (15 °C calorie)"),
        _u("1 cal<sub>IT</sub><sup>b</sup>", "4,186 8 J"),
        _u("1 kilocalo (dinh dưỡng)<sup>c</sup>", "4 186,8 J", "1 kilocalorie (nutrition)"),
        _u("1 oát giây (W·s)", "1 J", "1 watt second (W s)"),
        _u("1 oát giờ (W·h)", "3 600 J", "1 watt hour (W h)"),
        _u("1 therm (EC)", "1,055 06 × 10⁸ J"),
        _u("1 therm (U.S.)", "1,054 804 × 10⁸ J"),
        _u("1 tấn TNT (tương đương)", "4,184 × 10⁹ J", "1 ton TNT (equivalent)"),
        _u("1 Btu<sub>th</sub>", "1 054,350 J"),
        _u("1 Btu<sub>15</sub>", "1 054,728 J"),
        _u("1 Btu<sub>ST</sub>", "1 055,055 852 62 J"),
        _u("1 quad (= 10¹⁵ Btu)", "≈ 10¹⁸ J = 1 EJ"),
    ]),
    ("6. Lực", "6. Force", [
        _u("1 dyne", "10⁻⁵ N"),
        _u("1 ounce-force", "0,278 013 9 N"),
        _u("1 pound-force", "4,448 222 N"),
        _u("1 kilogram-force", "9,806 65 N"),
        _u("1 kip (1000 lbf)", "4 448,222 N"),
        _u("1 ton-force (2000 lbf)", "8 896,443 N"),
    ]),
    ("7. Mức tiêu thụ nhiên liệu", "7. Fuel consumption", [
        _u("1 gallon (U.S.) mỗi giờ mã lực", "1,410 089 × 10⁻⁹ m³/J",
           "1 gallon (U.S.) per horsepower hour"),
        _u("1 gallon (U.S.)/dặm", "2,352 15 l/km", "1 gallon (U.S.)/mile"),
        _u("1 gallon (U.K.)/dặm", "2,824 81 l/km", "1 gallon (U.K.)/mile"),
        _u("1 dặm/gallon (U.S.), mpg", "0,425 144 km/l", "1 mile/gallon (U.S.), mpg"),
        _u("1 dặm/gallon (U.K.)", "0,354 006 km/l", "1 mile/gallon (U.K.)"),
        _u("1 pound mỗi mã lực", "1,689 659 × 10⁻⁷ kg/J", "1 pound per horsepower"),
        _u("1 l/(100 km)", "235,215/(mpg) (U.S.)"),
    ]),
    ("8. Chiều dài", "8. Length", [
        _u("1 fermi", "10⁻¹⁵ m = 1 fm"),
        _u("1 ångström (Å)", "10⁻¹⁰ m"),
        _u("1 microinch", "2,54 × 10⁻⁸ m"),
        _u("1 mil", "2,54 × 10⁻⁵ m"),
        _u("1 point (pt) [0,013 837 in.]<sup>d</sup>", "0,351 46 mm"),
        _u("1 pica (12 pt)", "4,217 5 mm"),
        _u("1 inch (in.)", "0,025 4 m"),
        _u("1 hand (4 in.)", "0,101 6 m"),
        _u("1 foot (12 in.) (0,999 998 ft chuẩn)", "0,304 8 m",
           "1 foot (12 in.) (0.999 998 statute ft.)"),
        _u("1 foot (khảo sát Hoa Kỳ)", "0,304 800 6 m", "1 foot (U.S. survey)"),
        _u("1 ft chuẩn [(1200/3937) m]", "0,304 800 6 m", "1 statute foot [(1200/3937) m]"),
        _u("1 yard (yd)", "0,914 4 m"),
        _u("1 fathom (6 ft, khảo sát Hoa Kỳ)", "1,828 8 m", "1 fathom (6 ft, U.S. survey)"),
        _u("1 rod (16,5 ft chuẩn)", "5,029 2 m", "1 rod (16.5 statute ft)"),
        _u("1 chain (4 rod)", "20,116 8 m"),
        _u("1 furlong (10 chain)", "201,168 m"),
        _u("1 dặm (8 furlong, 5280 ft)", "1 609,344 m", "1 mile (8 furlong, 5280 ft)"),
        _u("1 dặm chuẩn (8 furlong, 5280 ft chuẩn)", "1 609,347 2 m",
           "1 statute mile (8 furlong, 5280 statute ft)"),
        _u("1 hải lý (quốc tế)<sup>e</sup>", "1 852 m", "1 nautical mile (international)"),
        _u("1 năm ánh sáng<sup>f</sup>", "9,460 730 × 10¹⁵ m", "1 light year"),
    ]),
    ("9. Ánh sáng", "9. Light", [
        _u("1 foot-candle", "10,763 91 lx"),
        _u("1 phot", "10 000 lx"),
        _u("1 cd/in.²", "1 550,003 cd/m²"),
        _u("1 foot-lambert", "3,426 259 cd/m²"),
        _u("1 lambert", "3 183,099 cd/m²"),
        _u("1 stilb", "10 000 cd/m²"),
    ]),
    ("10. Khối lượng", "10. Mass", [
        _u("1 pound (avdp.) (lb) (7000 gr)", "0,453 592 37 kg"),
        _u("1 pound (troy) (5760 gr)", "0,373 241 721 6 kg"),
        _u("1 grain (gr)", "64,798 91 mg"),
        _u("1 scruple (20 gr)", "1,296 0 g"),
        _u("1 pennyweight (24 gr)", "1,555 174 g"),
        _u("1 dram (60 gr)", "3,887 9 g"),
        _u("1 ounce (avdp) (437,5 gr)", "28,349 52 g"),
        _u("1 ounce (troy) (480 gr)", "31,103 48 g"),
        _u("1 carat (mét)", "0,2 g", "1 carat (metric)"),
        _u("1 stone (14 lb)", "6,350 29 kg"),
        _u("1 slug", "14,593 9 kg"),
        _u("1 hundredweight (long)", "50,802 35 kg"),
        _u("1 tấn (short) (2000 lb)", "907,184 7 kg", "1 ton (short) (2000 lb)"),
        _u("1 tấn (long) (2240 lb)", "1 016,047 kg = 1,016 047 t", "1 ton (long) (2240 lb)"),
    ]),
    ("Khối lượng trên đơn vị dài", "Mass per Unit Length", [
        _u("1 tex", "10⁻⁶ kg/m"),
        _u("1 denier", "1,111 111 × 10⁻⁷ kg/m"),
        _u("1 pound mỗi foot", "1,488 164 kg/m", "1 pound per foot"),
        _u("1 pound mỗi inch", "17,857 97 kg/m", "1 pound per inch"),
        _u("1 tấn/dặm", "0,631 342 Mg/km", "1 ton/mile"),
        _u("1 tấn/1000 yd", "1,111 6 kg/m", "1 ton/1000 yd"),
        _u("1 lb/ft", "1,488 16 kg/m"),
    ]),
    ("Khối lượng trên đơn vị diện tích", "Mass per Unit Area", [
        _u("1 tấn/dặm²", "3,922 98 kg/ha", "1 ton/mile²"),
        _u("1 tấn/acre", "2 510,71 kg/ha", "1 ton/acre"),
        _u("1 oz/yd²", "33,905 7 g/m²"),
    ]),
    ("Khối lượng × quãng đường (hệ số giao thông)",
     "Mass Carried × Distance (traffic factor)", [
        _u("1 tấn-dặm", "1 635,17 kg·km", "1 ton mile"),
    ]),
    ("Khối lượng × quãng đường / thể tích (hệ số giao thông)",
     "Mass carried × Distance/Volume (traffic factor)", [
        _u("1 tấn-dặm/gal (U.S.)", "431,967 6 Mg·km/m³", "1 ton mile/gal (U.S.)"),
    ]),
    ("11. Công suất", "11. Power", [
        _u("1 erg/s", "10⁻⁷ W"),
        _u("1 ft·lbf/h", "3,766 161 × 10⁻⁴ W"),
        _u("(1 Btu<sub>ST</sub>)", "1,000 669 Btu<sub>th</sub>"),
        _u("1 mã lực mét (force de cheval)", "735,498 8 W",
           "1 metric horsepower (force de cheval)"),
        _u("1 mã lực (550 ft·lbf/s)", "745,70 W", "1 horsepower (550 ft lbf/s)"),
        _u("1 mã lực điện", "746 W", "1 electric horsepower"),
    ]),
    ("12. Áp suất, ứng suất", "12. Pressure, Stress", [
        _u("1 átmốtphe chuẩn", "101 325 Pa", "1 standard atmosphere"),
        _u("1 dyne/cm²", "0,1 Pa"),
        _u("1 torr [(101 325/760) Pa]", "133,322 4 Pa"),
        _u("1 N/cm²", "10 000 Pa"),
        _u("1 bar", "100 000 Pa"),
        _u("1 lbf/ft²", "47,880 26 Pa"),
        _u("1 lbf/in² (psi)", "6 894,8 Pa"),
        _u("1 kgf/cm²", "98 066,5 Pa"),
        _u("1 cm nước (4 °C)", "98,063 7 Pa", "1 cm water (4 °C)"),
        _u("1 mm thuỷ ngân (0 °C)", "133,322 4 Pa", "1 mm of mercury (0 °C)"),
        _u("1 in nước (39,2 °F)", "249,082 Pa", "1 in of water (39.2 °F)"),
        _u("1 in thuỷ ngân (60 °F)", "3 376,85 Pa", "1 in of mercury (60 °F)"),
        _u("1 ft nước (39,2 °F)", "2 988,98 Pa", "1 ft water (39.2 °F)"),
    ]),
    ("13. Các đại lượng nhiệt", "13. Thermal Quantities", [
        ("grp", "Điểm cố định|Fixed points"),
        _u("Điểm ba của nước tự nhiên: T<sub>tp</sub>", "273,16 K",
           "Triple point of natural water: T_tp"),
        _u("Không độ Celsius (= T<sub>0</sub> = t<sub>F,0</sub>)", "273,15 K = 32 °F",
           "Zero Celsius (= T₀ = t_F,0)"),
        ("grp", "Quy đổi nhiệt độ|Temperature conversions"),
        _u("Kelvin sang Rankine (T<sub>R</sub>)", "T = (5/9) T<sub>R</sub>",
           "Kelvin to Rankine (T_R)"),
        _u("Kelvin sang Celsius", "t = T − T<sub>0</sub>", "Kelvin to Celsius"),
        _u("Kelvin sang Fahrenheit", "t<sub>F</sub> = (9/5)(T − T<sub>0</sub>) + t<sub>F,0</sub>",
           "Kelvin to Fahrenheit"),
        _u("Celsius sang Fahrenheit", "t<sub>F</sub> = (9/5) t + t<sub>F,0</sub>",
           "Celsius to Fahrenheit"),
        _u("[Dạng số: 5({t<sub>F</sub>} + 40) = 9({t} + 40), trong đó {t} và {t<sub>F</sub>} là "
           "trị số của nhiệt độ Celsius và Fahrenheit tương ứng.]",
           "5({t<sub>F</sub>} + 40) = 9({t} + 40)",
           "[Numerically: 5({t_F} + 40) = 9({t} + 40), where {t} and {t_F} are the numerical "
           "values of the Celsius and Fahrenheit temperatures respectively.]"),
        ("grp", "Quy đổi khoảng nhiệt độ|Temperature interval conversions"),
        _u("1 độ centigrade", "1 độ Celsius, ký hiệu 1 °C",
           "1 degree centigrade = 1 degree Celsius, denoted 1 °C"),
        _u("1 °C", "1 K"),
        _u("1 °F", "(1/1,8) K"),
        _u("1 °R", "(1/1,8) K"),
        ("grp", "Các đại lượng nhiệt khác|Other thermal quantities"),
        _u("1 Btu<sub>th</sub>/h", "0,292 875 W"),
        _u("1 Btu<sub>IT</sub>/h", "0,293 071 1 W"),
        _u("1 cal<sub>IT</sub>/s", "4,186 8 W"),
        _u("1 cal<sub>th</sub>/s", "4,184 W"),
        _u("1 cal<sub>IT</sub>/(g·°C)", "4 186,8 J/(kg·K)"),
        _u("1 Btu·ft/(ft²·h·°F)", "1,730 735 W·m⁻¹·K⁻¹"),
        _u("1 Btu·in/(ft²·s·°F)", "519,220 4 W·m⁻¹·K⁻¹"),
        _u("1 clo", "0,155 m²·K/W"),
        _u("1 °F·h·ft²/Btu", "0,176 110 2 K·m²/W"),
        _u("1 °F·h·ft²/(Btu·in)", "6,933 472 K·m/W"),
        _u("1 Btu/(lb·°F) ≡ 1 cal<sub>ST</sub>/(g·°C)", "4 186,8 J/(kg·K)",
           "1 Btu/lb °F ≡ 1 cal_ST/g °C"),
    ]),
    ("14. Mômen xoắn, mômen lực", "14. Torque, Moment of Force", [
        _u("1 dyne·cm", "10⁻⁷ N·m"),
        _u("1 kgf·m", "9,806 65 N·m"),
        _u("1 ozf·in", "0,007 061 552 N·m"),
        _u("1 lbf·in", "0,112 984 8 N·m"),
        _u("1 lbf·ft", "1,355 818 N·m"),
    ]),
    ("15. Vận tốc (kể cả tốc độ)", "15. Velocity (includes speed)", [
        _u("1 foot mỗi giờ", "8,466 667 × 10⁻⁵ m/s", "1 foot per hour"),
        _u("1 foot mỗi phút", "0,005 08 m/s", "1 foot per minute"),
        _u("1 knot (hải lý mỗi giờ)", "0,514 444 m/s", "1 knot (nautical mile per hour)"),
        _u("1 dặm mỗi giờ (mi/h)", "0,447 04 m/s", "1 mile per hour (mi/h)"),
    ]),
    ("16. Độ nhớt", "16. Viscosity", [
        _u("1 poise", "0,1 Pa·s"),
        _u("1 ft²/s", "0,092 903 04 m²/s"),
        _u("1 lb/(ft·s)", "1,488 164 Pa·s"),
        _u("1 lb/(ft·h)", "4,133 789 × 10⁻⁴ Pa·s"),
        _u("1 lbf·s/ft²", "47,880 26 Pa·s"),
        _u("1 lbf·s/in²", "6 894,757 Pa·s"),
        _u("1 rhe", "10 Pa⁻¹·s⁻¹"),
        _u("1 slug/(ft·s)", "47,880 26 Pa·s"),
        _u("1 stokes, St", "1,0 × 10⁻⁴ m²/s"),
    ]),
    ("17. Thể tích (kể cả dung tích)", "17. Volume (includes capacity)", [
        _u("1 stere, st", "1 m³"),
        _u("1 lít<sup>g</sup>", "0,001 m³", "1 liter"),
        _u("1 ft³", "0,028 316 8 m³"),
        _u("1 in.³", "1,638 7 × 10⁻⁵ m³"),
        _u("1 board foot", "2,359 7 × 10⁻³ m³"),
        _u("1 acre·foot", "1 233,48 m³"),
        _u("1 dram (U.S. lỏng)", "3,696 7 × 10⁻⁶ m³", "1 dram (U.S. fluid)"),
        _u("1 gill (U.S.)", "1,182 941 × 10⁻⁴ m³"),
        _u("1 ounce (U.S. lỏng)", "2,957 353 × 10⁻⁵ m³", "1 ounce (U.S. fluid)"),
        _u("1 thìa cà phê (tsp)<sup>h</sup>", "4,928 922 × 10⁻⁶ m³", "1 teaspoon (tsp)"),
        _u("1 thìa canh (tbsp)", "1,478 767 6 × 10⁻⁵ m³", "1 tablespoon (tbsp)"),
        _u("1 pint (U.S. lỏng)", "4,731 765 × 10⁻⁴ m³", "1 pint (U.S. fluid)"),
        _u("1 quart (U.S. lỏng)", "9,463 529 × 10⁻⁴ m³", "1 quart (U.S. fluid)"),
        _u("1 gallon (U.S. lỏng) [231 in.³]", "3,785 412 × 10⁻³ m³",
           "1 gallon (U.S. liquid) [231 in.³]"),
        _u("1 thùng rượu (bbl) [31,5 gal (U.S.)]", "0,119 240 m³",
           "1 wine barrel (bbl) [31.5 gal (U.S.)]"),
        _u("1 thùng dầu (petroleum, 42 gal, U.S.), bbl", "0,158 987 m³",
           "1 barrel (petroleum, 42 gal, U.S.), bbl"),
        _u("1 ounce (U.K. lỏng)", "2,841 3 × 10⁻⁵ m³", "1 ounce (U.K. fluid)"),
        _u("1 gill (Canada & U.K.)", "1,420 6 × 10⁻⁴ m³"),
        _u("1 gallon (Canada & U.K.)", "4,546 09 × 10⁻³ m³ = 1,200 950 gal (U.S.)",
           "1 gallon (Canada & U.K.)"),
        _u("1 pint (U.S. khô)", "5,506 105 × 10⁻⁴ m³", "1 pint (U.S. dry)"),
        _u("1 quart (U.S. khô)", "1,101 221 × 10⁻³ m³", "1 quart (U.S. dry)"),
        _u("1 gallon (U.S. khô)", "4,404 884 × 10⁻³ m³", "1 gallon (U.S. dry)"),
        _u("1 peck", "8,809 768 × 10⁻³ m³"),
        _u("1 bushel (U.S.) [2150,42 in.³]", "3,523 907 × 10⁻² m³",
           "1 bushel (U.S.) [2150.42 in.³]"),
    ]),
]


def _en_value(vi):
    """English equivalents use a dot decimal mark instead of the Vietnamese comma."""
    return vi.replace(",", "\u0001").replace(".", ",").replace("\u0001", ".")


def _rows_a5(lang):
    rows = []
    for gvi, gen, items in T_A5:
        rows.append(("grp", gvi if lang == "vi" else gen))
        # a sub-group label inside the row list carries "VI|EN"
        for item in items:
            if item[0] == "grp":
                label = item[1]
                rows.append(("grp", label.split("|")[0 if lang == "vi" else 1]
                             if "|" in label else label))
                continue
            unit, val, unit_en = item
            rows.append([unit if lang == "vi" else (unit_en or unit),
                         val if lang == "vi" else _en_value(val)])
    return rows


# ---------------------------------------------------------------- bodies

def body_vi():
    b = []
    b.append(p(
        "Phụ lục này tập hợp năm bảng: các đơn vị cơ bản của SI (Bảng A.1), định nghĩa quốc tế của "
        "các đơn vị cơ bản đó (Bảng A.2), các đơn vị dẫn xuất có tên riêng (Bảng A.3), các tiếp "
        "đầu ngữ của SI (Bảng A.4) và hệ số quy đổi từ đơn vị Anh sang đơn vị SI (Bảng A.5)."))

    b.append(h2("A.1 Các đơn vị cơ bản của SI", "The SI Base Units"))
    b.append(table(
        ("Đại lượng cơ bản", "Tên đơn vị cơ bản", "Ký hiệu"),
        [[r[0], r[2], r[4]] for r in T_A1],
        "Bảng A.1 · Bảy đơn vị cơ bản của Hệ đơn vị quốc tế (SI).", cls="tbl units w1"))

    b.append(h2("A.2 Định nghĩa quốc tế của các đơn vị cơ bản SI",
                "The International Definitions of the SI Base Units"))
    rows = []
    for r in T_A2:
        if r[0] == "grp":
            continue
        cell = "<b>%s</b><br>%s" % (r[0], r[2])
        if r[4]:
            cell += '<br><span style="font-size:.88em;color:#666">Ghi chú: %s</span>' % r[4]
        rows.append([cell])
    b.append(table(
        ("Đơn vị và định nghĩa",), rows,
        "Bảng A.2 · Định nghĩa quốc tế của bảy đơn vị cơ bản, kèm số hiệu nghị quyết của CGPM.",
        cls="tbl defs"))
    b.append(foots([
        "<sup>a</sup> Hoa Kỳ viết đơn vị đo chiều dài là “meter” thay cho cách viết quốc tế "
        "“metre”.",
        "<sup>b</sup> CGPM: Conférence Générale des Poids et Mesures (Hội nghị toàn thể về cân "
        "đo); CIPM: Comité International des Poids et Mesures (Uỷ ban quốc tế về cân đo).",
        "<sup>c</sup> BIPM: Bureau International des Poids et Mesures (Văn phòng quốc tế về cân "
        "đo).",
    ]))

    b.append(h2("A.3 Các đơn vị dẫn xuất SI có tên riêng",
                "SI Derived Units with Special Names"))
    b.append(table(
        ("Đại lượng dẫn xuất", "Tên", "Ký hiệu", "Biểu diễn qua đơn vị khác",
         "Biểu diễn qua đơn vị cơ bản SI"),
        [[r[0], r[2], r[4], r[5], r[6]] for r in T_A3],
        "Bảng A.3 · Hai mươi mốt đơn vị dẫn xuất SI được đặt tên riêng.",
        cls="tbl units w1"))
    b.append(foots([
        "<sup>a</sup> Khi một đơn vị được đặt tên theo một người, ký hiệu của nó viết bằng chữ "
        "hoa còn tên đơn vị viết bằng chữ thường.",
    ]))

    b.append(h2("A.4 Các tiếp đầu ngữ SI", "SI Prefixes"))
    b.append(table(
        ("Hệ số", "Tiếp đầu ngữ", "Ký hiệu", "Hệ số", "Tiếp đầu ngữ", "Ký hiệu"),
        _rows_a4("vi"),
        "Bảng A.4 · Hai mươi tiếp đầu ngữ SI dùng để lập tên và ký hiệu các bội số thập phân "
        "và ước số thập phân của đơn vị SI.",
        cls="tbl units"))
    b.append(foots([
        "<sup>a</sup> CGPM lần thứ 11 (1960, Nghị quyết 12) đã thông qua loạt tiếp đầu ngữ và ký "
        "hiệu tiếp đầu ngữ đầu tiên. Các tiếp đầu ngữ cho 10⁻¹⁵ và 10⁻¹⁸ được CGPM lần thứ 12 "
        "(1964, Nghị quyết 8) bổ sung; các tiếp đầu ngữ cho 10¹⁵ và 10¹⁸ do CGPM lần thứ 15 "
        "(1975, Nghị quyết 10) bổ sung; các tiếp đầu ngữ cho 10²¹, 10²⁴, 10⁻²¹ và 10⁻²⁴ do CIPM "
        "(1990) đề nghị để CGPM lần thứ 19 (1991) phê chuẩn.",
    ]))

    b.append(h2("A.5 Hệ số quy đổi từ đơn vị Anh sang đơn vị SI",
                "Conversion Factors from English Measures to SI Units"))
    b.append(table(
        ("Đơn vị", "Tương đương"),
        _rows_a5("vi"),
        "Bảng A.5 · Hệ số quy đổi từ đơn vị Anh sang đơn vị SI, xếp theo nhóm đại lượng.",
        cls="tbl conv"))
    b.append(foots([
        "<sup>a</sup> Hệ số quy đổi của một đơn vị ghép thường không được nêu ở đây nếu có thể dễ "
        "dàng suy ra từ các quy đổi đơn giản hơn; ví dụ, hệ số quy đổi từ “ft/s” sang “m/s” hay từ "
        "“ft/s²” sang “m/s²” không được nêu vì có thể suy ra từ hệ số của “ft”. Các giá trị được "
        "cho tới năm hoặc sáu chữ số có nghĩa, trừ những giá trị chính xác (thường in đậm trong "
        "bản gốc). Một vài đơn vị cgs cũ cũng được đưa vào.",
        "<sup>b</sup> Calo Bảng hơi quốc tế năm 1956.",
        "<sup>c</sup> Trong thực tế tiếp đầu ngữ kilo thường được bỏ qua. “Kilogram calo” hay "
        "“calo lớn” là tên đã lỗi thời của kilocalo, dùng để biểu diễn năng lượng của thức ăn.",
        "<sup>d</sup> Định nghĩa của nhà in, năm 1886.",
        "<sup>e</sup> Nguyên thuỷ là hải lý quốc tế năm 1929.",
        "<sup>f</sup> Dựa trên 1 ngày = 86 400 s và 1 thế kỷ Julius = 36 525 ngày.",
        "<sup>g</sup> Giá trị sau 1964, ký hiệu SI là l hoặc L. Từ 1901 đến 1964, lít được định "
        "nghĩa là 1,000 028 dm³.",
        "<sup>h</sup> Mặc dù thường được nêu, khó chắc rằng cách dùng thông thường biện minh cho "
        "độ chính xác này. Ở châu Âu và nhiều nơi khác, thìa cà phê và thìa canh thường đúng bằng "
        "5 mL và 15 mL.",
    ]))

    b.append(h2("Ghi chú của người dịch", "Translator's notes"))
    b.append(note(
        "Bản gốc là một bảng tra, nên phần lớn nội dung là số liệu. Khi chép lại, chúng tôi đã đối "
        "chiếu từng dòng với bản in và sửa những chỗ rõ ràng là lỗi ấn loát hoặc lỗi nhận dạng ký "
        "tự; mọi chỗ sửa đều được nêu dưới đây, không có chỗ nào sửa ngầm."))
    b.append(foots([
        "• <b>1 ton-force (2000 lbf)</b>: bản in ghi 8,896 443 N, thiếu một chữ số; 2000 lbf × "
        "4,448 222 N/lbf = 8 896,444 N. Bảng giữ 8 896,443 N.",
        "• <b>1 in.²</b>: bản in ghi đơn vị là “m” thay vì “m²”; đã sửa thành m².",
        "• <b>1 point (pt)</b>: bản in chỉ nêu [0,013 837 in.]; trị số tương đương 0,351 46 mm "
        "được thêm vào để tra cứu.",
        "• <b>1 năm ánh sáng</b>: bản in ghi 9,640 73 × 10¹⁵ m. Với 1 năm Julius = 36 525 ngày và "
        "c = 299 792 458 m/s, kết quả là 9,460 730 × 10¹⁵ m; bảng dùng giá trị tính lại này và "
        "giữ nguyên định nghĩa năm Julius ở chú thích f.",
        "• <b>1 rhe</b>: bản in bị mất dấu mũ, đọc thành “10 Pa–l s–1”; đã sửa thành 10 Pa⁻¹·s⁻¹ "
        "(rhe là nghịch đảo của poise).",
        "• <b>1 Btu<sub>IT</sub>/h</b>: bản in có thêm ký tự lạ (“0.293 071th 1 W”); đã sửa thành "
        "0,293 071 1 W.",
        "• <b>1 thìa cà phê (tsp)</b>: bản in ghi 4,928 892 2 × 10⁻⁶ m³; trị số chính xác của "
        "tsp Hoa Kỳ là 4,928 921 6 mL. Bảng giữ 4,928 922 × 10⁻⁶ m³, tức 4,928 922 mL.",
        "• <b>Số thập phân</b>: bản gốc dùng dấu chấm làm dấu thập phân và khoảng trắng phân cách "
        "nhóm ba chữ số. Bản dịch theo quy ước tiếng Việt: dấu phẩy làm dấu thập phân, dấu chấm "
        "phân cách hàng nghìn, khoảng hẹp phân cách nhóm ba chữ số của phần thập phân.",
    ]))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(foots([
        "1. CIPM, Procès-Verbaux CIPM, kỳ họp thứ 49, 1960, tr. 71–72; Comptes Rendues, CGPM lần "
        "thứ 11, 1960, tr. 85.",
        "2. P. Anderton và P. H. Bigg, <i>Changing to the Metric System</i>, HMSO, London, 1980.",
        "3. <i>The International System of Units (SI)</i>, Natl. Inst. Stand. Technol., Spec. "
        "Publ. 330, bản 1991, U.S. Government Printing Office, Washington, D.C., 1991.",
        "4. B. N. Taylor, <i>Interpretation of the SI for the United States and Metric Conversion "
        "Policy for Federal Agencies</i>, Natl. Inst. Stand. Technol., Spec. Publ. 814, U.S. "
        "Government Printing Office, Washington, D.C., 1991.",
        "5. E. R. Cohen, <i>The Physics Quick Reference Guide</i>, American Institute of Physics "
        "Press, New York, 1995.",
        "6. B. N. Taylor, <i>Guide for the Use of the International System of Units</i>, bản 1995, "
        "Natl. Inst. Stand. Technol., Spec. Publ. 811, U.S. Government Printing Office, "
        "Washington, D.C., 1995.",
        "7. <i>Standard for Use of the International System of Units (SI): The Modern Metric "
        "System</i>, IEEE/ASTM SI 10-1997, IEEE Standards Co-ordinating Committee 14 (soát xét và "
        "đặt lại số hiệu ANSI/IEEE Std 268-1992 và ASTM E380), IEEE, New York, 1997.",
        "8. <i>The International System of Units</i>, bản 7, BIPM, Pháp, 1998.",
    ]))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "This appendix gathers five tables: the SI base units (Table A.1), the international "
        "definitions of those base units (Table A.2), the derived units with special names "
        "(Table A.3), the SI prefixes (Table A.4) and conversion factors from English measures to "
        "SI units (Table A.5)."))

    b.append(h2("A.1 The SI Base Units"))
    b.append(table(
        ("Base quantity", "Name of base unit", "Symbol"),
        [[r[1], r[3], r[4]] for r in T_A1],
        "Table A.1 · The seven base units of the International System of Units.", cls="tbl units w1"))

    b.append(h2("A.2 The International Definitions of the SI Base Units"))
    rows = []
    for r in T_A2:
        if r[0] == "grp":
            continue
        cell = "<b>%s</b><br>%s" % (r[1], r[3])
        if r[5]:
            cell += '<br><span style="font-size:.88em;color:#666">Note: %s</span>' % r[5]
        rows.append([cell])
    b.append(table(("Unit and definition",), rows,
                   "Table A.2 · The international definitions of the seven base units, with the "
                   "CGPM resolution that adopted each one.", cls="tbl defs"))
    b.append(foots([
        "<sup>a</sup> The U.S. denotes the unit of length by “meter” in place of the international "
        "usage of “metre”.",
        "<sup>b</sup> CGPM: Conférence Générale des Poids et Mesures; CIPM: Comité International "
        "des Poids et Mesures.",
        "<sup>c</sup> BIPM: Bureau International des Poids et Mesures.",
    ]))

    b.append(h2("A.3 SI Derived Units with Special Names"))
    b.append(table(
        ("Derived quantity", "Name", "Symbol", "Expressed in terms of other units",
         "Expressed in terms of SI base units"),
        [[r[1], r[3], r[4], r[5], r[6]] for r in T_A3],
        "Table A.3 · Twenty-one SI derived units with special names.", cls="tbl units w1"))
    b.append(foots([
        "<sup>a</sup> When a unit is named after a person the symbol takes a capital letter and "
        "the name takes a lowercase letter.",
    ]))

    b.append(h2("A.4 SI Prefixes"))
    b.append(table(
        ("Factor", "Prefix", "Symbol", "Factor", "Prefix", "Symbol"),
        _rows_a4("en"),
        "Table A.4 · The twenty SI prefixes used to form the names and symbols of decimal "
        "multiples and submultiples of SI units.", cls="tbl units"))
    b.append(foots([
        "<sup>a</sup> The 11th CGPM (1960, Resolution 12) adopted a first series of prefixes and "
        "prefix symbols. Prefixes for 10⁻¹⁵ and 10⁻¹⁸ were added by the 12th CGPM (1964, "
        "Resolution 8), those for 10¹⁵ and 10¹⁸ by the 15th CGPM (1975, Resolution 10), and those "
        "for 10²¹, 10²⁴, 10⁻²¹ and 10⁻²⁴ were proposed by the CIPM (1990) for approval by the 19th "
        "CGPM (1991).",
    ]))

    b.append(h2("A.5 Conversion Factors from English Measures to SI Units"))
    b.append(table(
        ("Unit", "Equivalent"),
        _rows_a5("en"),
        "Table A.5 · Conversion factors from English measures to SI units, grouped by quantity.",
        cls="tbl conv"))
    b.append(foots([
        "<sup>a</sup> The conversion factor for a compound unit is usually not given here if it "
        "may easily be derived from simpler conversions; e.g., the factors for “ft/s” to “m/s” or "
        "“ft/s²” to “m/s²” are not given, since they follow from the factor for “ft”. Values are "
        "given to five or six significant digits except for exact values, which are usually "
        "indicated in bold type in the original. A few former cgs measures are also included.",
        "<sup>b</sup> The International Steam Table calorie of 1956.",
        "<sup>c</sup> In practice the prefix kilo is usually omitted. The kilogram calorie or "
        "large calorie is an obsolete term for the kilocalorie, used to express the energy "
        "content of foods.",
        "<sup>d</sup> Typographer's definition, 1886.",
        "<sup>e</sup> Originally, in 1929, the International nautical mile.",
        "<sup>f</sup> Based on 1 day = 86,400 s and 1 Julian century = 36,525 days.",
        "<sup>g</sup> Post-1964 value, SI symbol l or L. Between 1901 and 1964 the liter was "
        "defined as 1.000 028 dm³.",
        "<sup>h</sup> Although often given, it is doubtful whether normal usage justifies this "
        "accuracy. In Europe and elsewhere the teaspoon and tablespoon are usually exactly 5 mL "
        "and 15 mL respectively.",
    ]))

    b.append(h2("Translator's notes"))
    b.append(note(
        "The source is a lookup table, so almost everything here is numerical. Every row was "
        "checked against the printed page, and places where the print or the character "
        "recognition was plainly wrong are corrected; each correction is listed below — nothing "
        "was changed silently."))
    b.append(foots([
        "• <b>1 ton-force (2000 lbf)</b>: the print gives 8.896 443 N, one digit short; "
        "2000 lbf × 4.448 222 N/lbf = 8,896.444 N. The table keeps 8,896.443 N.",
        "• <b>1 in.²</b>: the print gives the unit as “m” rather than “m²”; corrected to m².",
        "• <b>1 point (pt)</b>: the print gives only [0.013 837 in.]; the equivalent 0.351 46 mm "
        "is added for lookup.",
        "• <b>1 light year</b>: the print gives 9.640 73 × 10¹⁵ m. With a Julian year of "
        "36,525 days and c = 299,792,458 m/s the result is 9.460 730 × 10¹⁵ m; the table uses the "
        "recomputed value and keeps the Julian-year definition in note f.",
        "• <b>1 rhe</b>: the print loses the superscripts and reads “10 Pa–l s–1”; corrected to "
        "10 Pa⁻¹·s⁻¹ (the rhe is the reciprocal of the poise).",
        "• <b>1 Btu<sub>IT</sub>/h</b>: the print carries stray characters (“0.293 071th 1 W”); "
        "corrected to 0.293 071 1 W.",
        "• <b>1 teaspoon (tsp)</b>: the print gives 4.928 892 2 × 10⁻⁶ m³; the exact U.S. "
        "teaspoon is 4.928 921 6 mL. The table keeps 4.928 922 × 10⁻⁶ m³, i.e. 4.928 922 mL.",
        "• <b>Decimals</b>: the Vietnamese page follows Vietnamese convention — comma as the "
        "decimal mark, dot as the thousands separator.",
    ]))
    return "".join(b)


# ---------------------------------------------------------------- build

def _nav(lang):
    """Previous = Chapter 101, centre = book TOC, right = book end."""
    from reader_handbook import DONE, CH
    en = lang == "en"
    base = BASE_EN if en else BASE_VI
    slug101 = DONE.get(101, "ch101-measurement-and-identification-of-stepping-motors")
    prev = base + slug101 + "/"
    return ('<div class="chapter-nav">'
            '<a href="%s"><span class="k">%s</span>%s</a>'
            '<a href="%s" style="text-align:center"><span class="k">%s</span>%s</a>'
            '<span class="disabled" style="text-align:right"><span class="k">%s</span></span>'
            '</div>'
            % (prev, "← Chapter 101" if en else "← Chương 101",
               CH[101][0] if en else CH[101][1],
               base, "Home" if en else "Trang chủ", "Book TOC" if en else "Mục lục sách",
               "Book end →" if en else "Cuối sách →"))


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Phụ lục A — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Appendix A — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Phụ lục A “Đơn vị và quy đổi” của B. W. Petley (National Physical "
            "Laboratory): bảy đơn vị cơ bản SI, định nghĩa quốc tế của chúng, các đơn vị dẫn xuất "
            "có tên riêng, hai mươi tiếp đầu ngữ SI và hệ số quy đổi từ đơn vị Anh sang SI." if vi
            else
            "Companion to Appendix A of the CRC Measurement Handbook — the seven SI base units, "
            "their international definitions, the derived units with special names, the twenty SI "
            "prefixes and conversion factors from English measures to SI units.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm '
             'biến</a> · Phụ lục A' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Appendix A' % BASE_EN)
    meta = ("Phụ lục A · theo App.pdf (CRC Press, 1999) · 5 bảng · 117 dòng quy đổi" if vi else
            "Appendix A · 5 tables · 117 conversion rows")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, ("Phụ lục A — " + TITLE_VI) if vi else ("Appendix A — " + TITLE_EN),
               BYLINE, meta, body_vi() if vi else body_en(), _nav(lang)))
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang)


def main():
    pairs = [("en", os.path.join(ROOT, "books", "read", SLUG, CSLUG, "index.html")),
             ("vi", os.path.join(ROOT, "vi", "books", "read", SLUG, CSLUG, "index.html"))]
    for lang, path in pairs:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        page = build(lang)
        open(path, "w", encoding="utf-8").write(page)
        print("wrote %s  %d kB" % (path, len(page) // 1024))


if __name__ == "__main__":
    main()
