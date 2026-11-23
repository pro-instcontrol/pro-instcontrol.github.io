# -*- coding: utf-8 -*-
"""Section 13.1 — Standard Specifications for Pressure-Retaining Valve Materials."""
from cvh13_common import T, H, P, LEAD, B, N, TB


def section(lang):
    b = []

    def add(num, vi_title, en_title, temp, comp, note_vi="", note_en="",
            nonpressure=False, temp_en=None, comp_en=None):
        """Append one material specification (heading + labeled bullet lists).

        `temp` and `comp` are the Vietnamese item lists; English defaults to the
        same list (numeric/grade data is language-neutral) and can be overridden
        for the few bullets that contain translatable prose.
        """
        if temp_en is None:
            temp_en = temp
        if comp_en is None:
            comp_en = comp
        b.append(H("%d. %s" % (num, vi_title), "%d. %s" % (num, en_title),
                   lang, lvl=3))
        if note_vi:
            b.append(P(note_vi, note_en, lang))
        if nonpressure:
            b.append(P("Dải nhiệt độ cho các bộ phận không chịu áp:",
                       "Temperature range for non-pressure-retaining components:",
                       lang))
        else:
            b.append(P("Dải nhiệt độ:", "Temperature range:", lang))
        b.append(B(temp, temp_en, lang))
        b.append(P("Thành phần (%):", "Composition (%):", lang))
        b.append(B(comp, comp_en, lang))

    b.append(H("13.1 Tiêu chuẩn kỹ thuật cho vật liệu van chịu áp",
               "13.1 Standard Specifications for Pressure-Retaining Valve Materials",
               lang, lvl=2))
    b.append(LEAD("Xem mục 13.2 để biết các thông số kỹ thuật bổ sung, được đối chiếu theo số mã vật liệu.",
                  "See section 13.2 for additional specifications, cross-referenced to Material Code numbers.",
                  lang))

    add(1, "Thép cacbon đúc ASTM A216 Grade WCC",
        "Cast Carbon Steel ASTM A216 Grade WCC",
        ["-30 to 427°C (-20 to 800°F)"],
        ["C = 0.25 max", "Mn = 1.2 max", "P = 0.035 max", "S = 0.035 max",
         "Si = 0.6 max"])

    add(2, "Thép cacbon đúc ASTM A352 Grade LCC",
        "Cast Carbon Steel ASTM A352 Grade LCC",
        ["-45 to 343°C (-50 to 650°F)"],
        ["Tương tự ASTM A216 grade WCC"],
        comp_en=["Same as ASTM A216 grade WCC"])

    add(3, "Thanh thép cacbon AISI 1018, UNS G10180",
        "Carbon Steel Bar AISI 1018, UNS G10180",
        ["-29 to 427°C (-20 to 800°F)"],
        ["C = 0.14 to 0.2", "Mn = 0.6 to 0.9", "P = 0.04 max", "S = 0.05 max"])

    add(4, "Thanh thép có chì AISI 12L14, UNS G12144",
        "Leaded Steel Bar AISI 12L14, UNS G12144",
        ["-29 to 427°C (-20 to 800°F)"],
        ["C = 0.15 max", "Mn = 0.85 to 1.15", "P = 0.04 to 0.09",
         "S = 0.26 to 0.35", "Pb = 0.15 to 0.35"])

    add(5, "Thép Cr-Mo AISI 4140", "AISI 4140 Cr-Mo Steel",
        ["-48 to 538°C (-55 to 1000°F)"],
        ["C = 0.38 to 0.43", "Mn = 0.75 to 1.0", "P = 0.035 max",
         "S = 0.040 max", "Si = 0.15 to 0.35", "Cr = 0.8 to 1.1",
         "Mo = 0.15 to 0.25", "Fe = Remainder"],
        note_vi="Tương tự vật liệu bulông ASTM A193 Grade B7.",
        note_en="Similar to ASTM A193 Grade B7 bolt material.")

    add(6, "Thép niken rèn 3-1/2% ASTM A352 Grade LC3",
        "Forged 3-1/2% Nickel Steel ASTM A352 Grade LC3",
        ["-101 to 343°C (-150 to 650°F)"],
        ["C = 0.15 max", "Mn = 0.5 to 0.8", "P = 0.04 max", "S = 0.045 max",
         "Si = 0.6 max", "Ni = 3.0 to 4.0"])

    add(7, "Thép Cr-Mo đúc ASTM A217 Grade WC6",
        "Cast Cr-Mo Steel ASTM A217 Grade WC6",
        ["-30 to 595°C (-20 to 1100°F)"],
        ["C = 0.05 to 0.2", "Mn = 0.5 to 0.8", "P = 0.035 max", "S = 0.035 max",
         "Si = 0.60 max", "Cr = 1.0 to 1.5", "Mo = 0.45 to 0.65"])

    add(8, "Thép Cr-Mo đúc ASTM A217 Grade WC9",
        "Cast Cr-Mo Steel ASTM A217 Grade WC9",
        ["-30 to 595°C (-20 to 1100°F)"],
        ["C = 0.05 to 0.18", "Mn = 0.4 to 0.7", "P = 0.035 max", "S = 0.035 max",
         "Si = 0.6 max", "Cr = 2.0 to 2.75", "Mo = 0.9 to 1.2"])

    add(9, "Thép Cr-Mo rèn ASTM A182 Grade F22",
        "Forged Cr-Mo Steel ASTM A182 Grade F22",
        ["-30 to 593°C (-20 to 1100°F)"],
        ["C = 0.05 to 0.15", "Mn = 0.3 to 0.6", "P = 0.04 max", "S = 0.04 max",
         "Si = 0.5 max", "Cr = 2.0 to 2.5", "Mo = 0.87 to 1.13"])

    add(10, "Thép Cr-Mo đúc ASTM A217 Grade C5",
        "Cast Cr-Mo Steel ASTM A217 Grade C5",
        ["-30 to 649°C (-20 to 1200°F)"],
        ["C = 0.2 max", "Mn = 0.4 to 0.7", "P = 0.04 max", "S = 0.045 max",
         "Si = 0.75 max", "Cr = 4.0 to 6.5", "Mo = 0.45 to 0.65"])

    add(11, "Thép không gỉ type 302 ASTM A479 Grade UNS S30200",
        "Type 302 Stainless Steel ASTM A479 Grade UNS S30200",
        ["-198 to 399°C (-325 to 750°F)"],
        ["C = 0.15 max", "Mn = 2.0 max", "P = 0.045 max", "S = 0.03 max",
         "Si = 1.0 max", "Cr = 17.0 to 19.0", "Ni = 8.0 to 10.0",
         "N = 0.1 max", "Fe = Remainder"])

    add(12, "Thép không gỉ type 304L ASTM A479 Grade UNS S30403",
        "Type 304L Stainless Steel ASTM A479 Grade UNS S30403",
        ["-254 to 425°C (-425 to 800°F)"],
        ["C = 0.03 max", "Mn = 2.0 max", "P = 0.045 max", "S = 0.03 max",
         "Si = 1.0 max", "Cr = 18.0 to 20.0", "Ni = 8.0 to 12.0",
         "Fe = Remainder"])

    add(13, "Thép không gỉ type 304L đúc ASTM A351 Grade CF3",
        "Cast Type 304L Stainless Steel ASTM A351 Grade CF3",
        ["-254 to 425°C (-425 to 800°F)"],
        ["C = 0.03 max", "Mn = 1.5 max", "Si = 2.0 max", "S = 0.040 max",
         "P = 0.040 max", "Cr = 17.0 to 21.0", "Ni = 8.0 to 11.0",
         "Mo = 0.50 max"])

    add(14, "Thép không gỉ type 316L ASTM A479 Grade UNS S31603",
        "Type 316L Stainless Steel ASTM A479 Grade UNS S31603",
        ["-254 to 450°C (-425 to 850°F)"],
        ["C = 0.03 max", "Mn = 2.0 max", "P = 0.045 max", "S = 0.03 max",
         "Si = 1.0 max", "Cr = 16.0 to 18.0", "Ni = 10.0 to 14.0",
         "Mo = 2.0 to 3.0", "Fe = Remainder"])

    add(15, "Thép không gỉ type 316 ASTM A479 Grade UNS S31600",
        "Type 316 Stainless Steel ASTM A479 Grade UNS S31600",
        ["-255 to 816°C (-425 to 1500°F)",
         "Trên 538°C (1000°F), yêu cầu tối thiểu 0.04 C"],
        ["C = 0.08 max", "Mn = 2.0 max", "P = 0.045 max", "S = 0.03 max",
         "Si = 1.0 max", "Cr = 16.0 to 18.0", "Ni = 10.0 to 14.0",
         "Mo = 2.0 to 3.0", "Fe = Remainder"],
        temp_en=["-255 to 816°C (-425 to 1500°F)",
                 "Above 538°C (1000°F), 0.04 C minimum required"])

    add(16, "Thép không gỉ type 316 đúc ASTM A351 Grade CF8M",
        "Cast Type 316 Stainless Steel ASTM A351 Grade CF8M",
        ["-254 to 816°C (-425 to 1500°F)",
         "Trên 538°C (1000°F), yêu cầu tối thiểu 0.04 C"],
        ["C = 0.08 max", "Mn = 1.5 max", "Si = 1.5 max", "P = 0.04 max",
         "S = 0.04 max", "Cr = 18.0 to 21.0", "Ni = 9.0 to 12.0",
         "Mo = 2.0 to 3.0"],
        temp_en=["-254 to 816°C (-425 to 1500°F)",
                 "Above 538°C (1000°F), 0.04 C minimum required"])

    add(17, "Thép không gỉ type 317 ASTM A479 Grade UNS S31700",
        "Type 317 Stainless Steel ASTM A479 Grade UNS S31700",
        ["-198 to 816°C (-325 to 1500°F)",
         "Trên 538°C (1000°F), yêu cầu tối thiểu 0.04 C"],
        ["C = 0.08 max", "Mn = 2.0 max", "P = 0.045 max", "S = 0.03 max",
         "Si = 1.0 max", "Cr = 18.0 to 20.0", "Ni = 11.0 to 15.0",
         "Mo = 3.0 to 4.0", "Fe = Remainder"],
        temp_en=["-198 to 816°C (-325 to 1500°F)",
                 "Above 538°C (1000°F), 0.04 C minimum required"])

    add(18, "Thép không gỉ type 317 đúc ASTM A351 Grade CG8M",
        "Cast Type 317 Stainless Steel ASTM A351 Grade CG8M",
        ["-198 to 538°C (-325 to 1000°F)"],
        ["C = 0.08 max", "Mn = 1.5 max", "Si = 1.5 max", "P = 0.04 max",
         "S = 0.04 max", "Cr = 18.0 to 21.0", "Ni = 9.0 to 13.0",
         "Mo = 3.0 to 4.0"])

    add(19, "Thép không gỉ type 410 ASTM A479 Grade S41000",
        "Type 410 Stainless Steel ASTM A479 Grade S41000",
        ["-29 to 538°C (-20 to 1000°F)"],
        ["C = 0.08 to 0.15", "Mn = 1.0 max", "P = 0.04 max", "S = 0.03 max",
         "Si = 1.0 max", "Cr = 11.5 to 13.5", "Fe = Remainder"])

    add(20, "Thép không gỉ type 17-4PH ASTM A564 Grade 630, UNS S17400",
        "Type 17-4PH Stainless Steel ASTM A564 Grade 630, UNS S17400",
        ["-29 to 343°C (-20 to 650°F)"],
        ["C = 0.07 max", "Mn = 1.0 max", "Si = 1.0 max", "P = 0.04 max",
         "S = 0.03 max", "Cr = 15.0 to 17.5", "Nb = 0.15 to 0.45",
         "Cu = 3.0 to 5.0", "Ni = 3.0 to 5.0", "Fe = Remainder"])

    add(21, "Thép không gỉ type 254 SMO ASTM A479 Grade UNS S31254",
        "Type 254 SMO Stainless Steel ASTM A479 Grade UNS S31254",
        ["-198 to 399°C (-325 to 750°F)"],
        ["C = 0.02 max", "Mn = 1.0 max", "P = 0.03 max", "S = 0.01 max",
         "Si = 0.8 max", "Cr = 18.5 to 20.5", "Ni = 17.5 to 18.5",
         "Mo = 6.0 to 6.5", "N = 0.18−0.22", "Fe = Remainder"])

    add(22, "Thép không gỉ type 254 SMO đúc ASTM A351 Grade CK3MCuN",
        "Cast Type 254 SMO Stainless Steel ASTM A351 Grade CK3MCuN",
        ["-198 to 399°C (-325 to 750°F)"],
        ["C = 0.025 max", "Mn = 1.2 max", "Si = 1.0 max", "P = 0.045 max",
         "S = 0.01 max", "Cr = 19.5 to 20.5", "Ni = 17.5 to 19.5",
         "Mo = 6.0 to 7.0", "N = 0.18 to 0.24"])

    add(23, "Thép không gỉ duplex type 2205, S31803 ASTM A479 Grade UNS S31803",
        "Type 2205, S31803 Duplex Stainless Steel ASTM A479 Grade UNS S31803",
        ["-50 to 316°C (-60 to 600°F)"],
        ["C = 0.03 max", "Mn = 2.0 max", "P = 0.03 max", "S = 0.02 max",
         "Si = 1.0 max", "Cr = 21.0 to 23.0", "Ni = 4.5 to 6.5",
         "Mo = 2.5 to 3.5", "N = 0.08 to 0.2", "Fe = Remainder"])

    add(24, "Thép không gỉ type 2205, S31803 đúc ASTM A890 Grade 4a, CD3MN",
        "Cast Type 2205, S31803 Stainless Steel ASTM A890 Grade 4a, CD3MN",
        ["-50 to 316°C (-60 to 600°F)"],
        ["C = 0.03 max", "Mn = 1.5 max", "Si = 1.0 max", "P = 0.04 max",
         "S = 0.02 max", "Cr = 21.0 to 23.5", "Ni = 4.5 to 6.5",
         "Mo = 2.5 to 3.5", "Cu = 1.0 max", "N = 0.1 to 0.3",
         "Fe = Remainder"])

    add(25, "Gang đúc ASTM A126 Class B, UNS F12102",
        "Cast Iron ASTM A126 Class B, UNS F12102",
        ["-29 to 232°C (-20 to 450°F)"],
        ["P = 0.75 max", "S = 0.15 max"])

    add(26, "Gang đúc ASTM A126 Class C, UNS F12802",
        "Cast Iron ASTM A126 Class C, UNS F12802",
        ["-29 to 232°C (-20 to 450°F)"],
        ["P = 0.75 max", "S = 0.15 max"])

    add(27, "Gang dẻo ASTM A395 Type 60-40-18",
        "Ductile Iron ASTM A395 Type 60-40-18",
        ["-29 to 343°C (-20 to 650°F)"],
        ["C = 3.0 min", "Si = 2.5 max", "P = 0.08 max"])

    add(28, "Gang dẻo Ni-Resist ASTM A439 Type D-2B, UNS F43001",
        "Ductile Ni-Resist Iron ASTM A439 Type D-2B, UNS F43001",
        ["-29 to 760°C (-20 to 1400°F)"],
        ["C = 3.0 max", "Si = 1.5 to 3.00", "Mn = 0.70 to 1.25",
         "P = 0.08 max", "Ni = 18.0 to 22.0", "Cr = 2.75 to 4.0"],
        nonpressure=True)

    add(29, "Đồng van ASTM B61, UNS C92200",
        "Valve Bronze ASTM B61, UNS C92200",
        ["-198 to 288°C (-325 to 550°F)"],
        ["Cu = 86.0 to 90.0", "Sn = 5.5 to 6.5", "Pb = 1.0 to 2.0",
         "Zn = 3.0 to 5.0", "Ni = 1.0 max", "Fe = 0.25 max",
         "S = 0.05 max", "P = 0.05 max"])

    add(30, "Đồng thiếc ASTM B584 Grade UNS C90500",
        "Tin Bronze ASTM B584 Grade UNS C90500",
        ["-198 to 204°C (-325 to 400°F)"],
        ["Cu = 86.0 to 89.0", "Sn = 9.0 to 11.0", "Pb = 0.30 max",
         "Zn = 1.0 to 3.0", "Ni = 1.0 max", "Fe = 0.2 max",
         "S = 0.05 max", "P = 0.05 max"])

    add(31, "Đồng mangan ASTM B584 Grade UNS C86500",
        "Manganese Bronze ASTM B584 Grade UNS C86500",
        ["-198 to 177°C (-325 to 350°F)"],
        ["Cu = 55.0 to 60.0", "Sn = 1.0 max", "Pb = 0.4 max",
         "Ni = 1.0 max", "Fe = 0.4 to 2.0", "Al = 0.5 to 1.5",
         "Mn = 0.1 to 1.5", "Zn = 36.0 to 42.0"])

    add(32, "Đồng nhôm đúc ASTM B148 Grade UNS C95400",
        "Cast Aluminum Bronze ASTM B148 Grade UNS C95400",
        ["-198 to 316°C (-325 to 600°F)"],
        ["Cu = 83.0 min", "Al = 10.0 to 11.5", "Fe = 3.0 to 5.0",
         "Mn = 0.50 max", "Ni = 1.5 max"])

    add(33, "Đồng nhôm đúc ASTM B148 Grade UNS C95800",
        "Cast Aluminum Bronze ASTM B148 Grade UNS C95800",
        ["-198 to 260°C (-325 to 500°F)"],
        ["Cu = 79.0 min", "Al = 8.5 to 9.5", "Fe = 3.5 to 4.5",
         "Mn = 0.8 to 1.5", "Ni = 4.0 to 5.0", "Si = 0.1 max"])

    add(34, "Thanh đồng vàng B16 ASTM B16 Grade UNS C36000, 1/2 Hard",
        "B16 Yellow Brass Bar ASTM B16 Grade UNS C36000, 1/2 Hard",
        ["-198 to 204°C (-325 to 400°F)"],
        ["Cu = 60.0 to 63.0", "Pb = 2.5 to 3.0", "Fe = 0.35 max",
         "Zn = Remainder"],
        nonpressure=True)

    add(35, "Rèn đồng hàng hải ASTM B283 Alloy UNS C46400",
        "Naval Brass Forgings ASTM B283 Alloy UNS C46400",
        ["-198 to 204°C (-325 to 400°F)"],
        ["Cu = 59.0 to 62.0", "Sn = 0.5 to 1.0", "Pb = 0.2 max",
         "Fe = 0.15 max", "Zn = Remainder"])

    add(36, "Thanh nhôm ASTM B211 Alloy UNS A96061-T6",
        "Aluminum Bar ASTM B211 Alloy UNS A96061-T6",
        ["-269 to 204°C (-452 to 400°F)"],
        ["Si = 0.4 to 0.8", "Fe = 0.7 max", "Cu = 0.15 to 0.4",
         "Zn = 0.25 max", "Mg = 0.8 to 1.2", "Mn = 0.15 max",
         "Cr = 0.04 to 0.35", "Ti = 0.15 max", "Other Elements = 0.15 max",
         "Al = Remainder"])

    add(37, "Hợp kim gốc coban No.6 đúc UNS R30006, Weld filler CoCr-A",
        "Cobalt-base Alloy No.6 Cast UNS R30006, Weld filler CoCr-A",
        ["-198 to 980°C (-325 to 1800°F)"],
        ["C = 0.9 to 1.4", "Mn = 1.0 max", "W = 3.5 to 6.0",
         "Ni = 3.0 max", "Cr = 26.0 to 31.0", "Mo = 1.5 max",
         "Fe = 3.0 max", "Si = 1.5 max", "Co = Remainder"],
        nonpressure=True)

    add(38, "Thanh hợp kim Ni-Cu K500 ASTM B865 Grade N05500",
        "Ni-Cu Alloy Bar K500 ASTM B865 Grade N05500",
        ["-198 to 482°C (-325 to 900°F)"],
        ["Ni = 63.0 min", "Fe = 2.0 max", "Mn = 1.5 max", "Si = 0.5 max",
         "C = 0.18 max", "S = 0.01 max", "Al = 2.3 to 3.15",
         "Ti = 0.35 to 0.85", "Cu = Remainder"],
        nonpressure=True)

    add(39, "Hợp kim Ni-Cu 400 đúc ASTM A494 Grade M35-1",
        "Cast Ni-Cu Alloy 400 ASTM A494 Grade M35-1",
        ["-198 to 475°C (-325 to 900°F)"],
        ["Cu = 27.0 to 33.0", "C = 0.35 max", "Mn = 1.5 max",
         "Fe = 3.5 max", "S = 0.02 max", "P = 0.03 max", "Si = 1.25 max",
         "Nb = 0.5 max", "Ni = Remainder"])

    add(40, "Thanh hợp kim Ni-Cr-Mo C276 ASTM B574 Grade N10276",
        "Ni-Cr-Mo Alloy C276 Bar ASTM B574 Grade N10276",
        ["-198 to 677°C (-325 to 1250°F)"],
        ["Cr = 14.5 to 16.5", "Fe = 4.0 to 7.0", "W = 3.0 to 4.5",
         "C = 0.01 max", "Si = 0.08 max", "Co = 2.5 max", "Mn = 1.0 max",
         "V = 0.35 max", "Mo = 15.0 to 17.0", "P = 0.04", "S = 0.03",
         "Ni = Remainder"])

    add(41, "Hợp kim Ni-Cr-Mo C ASTM A494 CW2M",
        "Ni-Cr-Mo Alloy C ASTM A494 CW2M",
        ["-198 to 538°C (-325 to 1000°F)"],
        ["Cr = 15.5 to 17.5", "Fe = 2.0 max", "W = 1.0 max",
         "C = 0.02 max", "Si = 0.8 max", "Mn = 1.0 max",
         "Mo = 15.0 to 17.5", "P = 0.03", "S = 0.02", "Ni = Remainder"])

    add(42, "Thanh hợp kim Ni-Mo B2 ASTM B335 Grade B2, UNS N10665",
        "Ni-Mo Alloy B2 Bar ASTM B335 Grade B2, UNS N10665",
        ["-198 to 427°C (-325 to 800°F)"],
        ["Cr = 1.0 max", "Fe = 2.0 max", "C = 0.02 max", "Si = 0.1 max",
         "Co = 1.0 max", "Mn = 1.0 max", "Mo = 26.0 to 30.0",
         "P = 0.04 max", "S = 0.03 max", "Ni = Remainder"])

    add(43, "Hợp kim Ni-Mo B2 đúc ASTM A494 N7M",
        "Cast Ni-Mo Alloy B2 ASTM A494 N7M",
        ["-198 to 538°C (-325 to 1000°F)"],
        ["Cr = 1.0 max", "Fe = 3.0 max", "C = 0.07 max", "Si = 1.0 max",
         "Mn = 1.0 max", "Mo = 30.0 to 33.0", "P = 0.03 max",
         "S = 0.02 max", "Ni = Remainder"])

    return "".join(b)
