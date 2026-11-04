# -*- coding: utf-8 -*-
"""§32.10 Temperature Indicators — Jan Stasiek, Tolestyn Madaj, and Jaroslaw
Mikielewicz, p137-152."""
import math as _m
import hb32kit as K
R = K.R                      # lazy proxy to reader_hb_ch32 helpers

TITLE_EN = "Temperature Indicators"
TITLE_VI = "Chất chỉ thị nhiệt độ"

# Flat (English, Vietnamese, depth) tuples — depth 0 -> h3, 1 -> h4.
# The English strings are exactly those passed to the headings; sec_index()
# builds the TOC links from #s32-10-<slug(english)>, so spelling must match.
SUBS = [
    ("Melting and Shape/Size Changing Temperature Indicators",
     "Chất chỉ thị nóng chảy và biến dạng hình dạng/kích thước", 0),
    ("Seger Cones", "Nón Seger", 0),
    ("Thermoscope Bars", "Thanh thermoscope", 0),
    ("Bullers Rings", "Vòng Bullers", 0),
    ("Temperature-Indicating Pellets, Liquids, Crayons, and Monitors",
     "Hạt, chất lỏng, sáp màu và nhãn chỉ thị nhiệt độ", 0),
    ("Temperature-Indicating Pellets", "Hạt chỉ thị nhiệt độ", 1),
    ("Temperature-Indicating Liquids", "Chất lỏng chỉ thị nhiệt độ", 1),
    ("Temperature-Indicating Crayons", "Sáp màu chỉ thị nhiệt độ", 1),
    ("Temperature Monitors (Labels)", "Nhãn chỉ thị nhiệt độ (Monitors)", 1),
    ("Color-Change Temperature Indicators",
     "Chất chỉ thị đổi màu theo nhiệt độ", 0),
    ("Temperature-Indicating Paints and Crayons",
     "Sơn và sáp màu chỉ thị nhiệt độ", 1),
    ("Irreversible Color-Change Paints", "Sơn đổi màu không hồi phục", 1),
    ("Color-Change Crayons", "Sáp màu đổi màu", 1),
    ("Reversible Color-Change Indicators", "Chất chỉ thị đổi màu hồi phục", 1),
    ("Thermochromic Liquid Crystals", "Tinh thể lỏng nhiệt sắc", 1),
    ("Temperature-Sensitive and Shear-Sensitive Formulations",
     "Công thức nhạy cảm với nhiệt độ và trượt", 1),
    ("Color-Play Properties and Resolution",
     "Đặc tính dải màu và độ phân giải", 1),
]


# ---------------------------------------------------------------- references
def refs(lang):
    vi = (lang == "vi")
    items = [
        "1. BS 1041: Part 7. Temperature Measurement.",
        "2. DIN 51063: Part 1. Testing of Ceramic Raw and Finished Materials, "
        "Pyrometric cone of Seger. Part 2. Testing of Ceramic Materials.",
        "3. OMEGA International Corp. P.O. Box 2721, Stanford, CT 06906 "
        "(The Temperature Handbook).",
        "4. TEMPIL Division, Big Three Industries, Inc. South Plainfield, NJ "
        "07080 (Catalog GC-75).",
        "5. HALLCREST Products Inc. 1820 Pickwick Lane, Glenview, IL 60025.",
        "6. MERC Industrial Chemicals, Merc House, Poole Dorset, BH15 1TD, U.K.",
        "7. Moffat, R.J., Experimental heat transfer, Proc. 9th Int. Heat "
        "Transfer Conf., Jerusalem, Israel, 1990.",
    ]
    head_ = ('<h3 id="t32-tltk-10">Tài liệu tham khảo</h3>' if vi else
             '<h3 id="t32-tltk-10">References</h3>')
    return head_ + R.wl(items)


# ----------------------------------------------------------------- where clause
# (English items, Vietnamese items) keyed by equation number.
_W = {
"32.1": (["where &nbsp;<i>X</i> is a mass unit",
          "&nbsp;the pyramids for higher rated temperatures are prepared "
          "from similar equations"],
         ["trong đó &nbsp;<i>X</i> là một đơn vị khối lượng",
          "&nbsp;các kim tự tháp cho nhiệt độ định mức cao hơn được pha chế "
          "từ các phương trình tương tự"]),
}


# ------------------------------------------------------------------- figures
# num -> (cap_vi, cap_en, aria_vi, aria_en, title_vi).
# Note: the book prints TWO figures as 32.77 — the first in §32.9, this one in
# §32.10.  Its <i>number here is the string "77a"</i> so the DOM id becomes
# "fig-32-77a" and stays unique; the caption text still reads "Figure 32.77".
_CAP = {
"77a": ("Hình 32.77 · Nón nhiệt (a) trong mặt cắt ngang; (b) trên tấm đế khi nung.",
        "Figure 32.77 · Pyrometric cones (a) in cross-sections; (b) on a "
        "plaque during firing.",
        "Hai bảng: mặt cắt nón và nón trên tấm đế",
        "Two panels: cone cross-sections and cones on a plaque",
        "Nón nhiệt (pyrometric cones)"),
48: ("", "", "", "", ""),   # placeholder, unused
78: ("Hình 32.78 · Các thanh thermoscope trên giá trước và sau khi nung.",
     "Figure 32.78 · Thermoscope bars on a stand before and after firing.",
     "Hai bảng thanh thẳng và thanh cong",
     "Two panels: straight and bent bars",
     "Thanh thermoscope trên giá"),
79: ("Hình 32.79 · Thước đo độ co ngót của vòng Bullers.",
     "Figure 32.79 · Contraction gage for Bullers rings.",
     "Sơ đồ thước đo co ngót",
     "Schematic of the contraction gage",
     "Thước đo độ co ngót"),
80: ("Hình 32.80 · Sáp màu và hạt chỉ thị nhiệt độ.",
     "Figure 32.80 · Temperature-indicating crayon and pellets.",
     "Sáp màu và các hạt chỉ thị",
     "Crayon and indicator pellets",
     "Sáp và hạt chỉ thị nhiệt độ"),
81: ("Hình 32.81 · Nhãn bốn chấm.",
     "Figure 32.81 · Four-dot label.",
     "Nhãn bốn ô cửa sổ tròn",
     "Label with four circular windows",
     "Nhãn bốn chấm"),
82: ("Hình 32.82 · Đặc tuyến bước xoắn theo nhiệt độ của tinh thể lỏng nhiệt "
     "sắc điển hình.",
     "Figure 32.82 · Typical pitch vs. temperature response of thermochromic "
     "liquid crystals.",
     "Đồ thị bước xoắn theo nhiệt độ",
     "Pitch-vs-temperature curve",
     "Đáp ứng bước xoắn theo nhiệt độ"),
83: ("Hình 32.83 · Cấu trúc tinh thể lỏng (a) nematic; (b) cholesteric; "
     "(c) smectic A; (d) smectic B.",
     "Figure 32.83 · Structures of liquid crystals (a) nematic; (b) cholesteric; "
     "(c) smectic A; (d) smectic B.",
     "Bốn bảng cấu trúc tinh thể lỏng",
     "Four panels of liquid-crystal structures",
     "Cấu trúc tinh thể lỏng"),
}


def _emit_diagram(lang, num, W, H, parts):
    cv, ce, av, ae, tv = _CAP[num]
    return K.diagram(num, W, H, parts, cv, ce, av, ae, lang, tv)


def _emit_chart(lang, num, W, H, xr, yr, xt, yt, curves, xlab, ylab,
                extra="", pad=(56, 20, 18, 42)):
    cv, ce, av, ae, tv = _CAP[num]
    return K.chart(num, W, H, xr, yr, xt, yt, curves, xlab, ylab,
                   cv, ce, av, ae, lang, tv, extra=extra, pad=pad)


def F77a(lang):
    W, H = 560, 300
    p = [K._lbl(24, 24, "(a) Mặt cắt ngang / cross-sections", "ts", "start")]
    for i, cx in enumerate([80, 150, 220]):
        p.append(K._poly([(cx - 22, 250), (cx + 22, 250), (cx, 150)],
                         K.FILL, K.E, 1.4))
        p.append(K._lbl(cx, 268, "nón %d" % (i + 1), "ts", "middle", K._fs(8)))
    p.append(K._lbl(300, 24, "(b) Trên tấm đế / on a plaque", "ts", "start"))
    p.append(K._rect(300, 230, 232, 16, K.FILL, K.E, 1.4))
    for i, cx in enumerate([340, 410, 480]):
        p.append(K._poly([(cx - 16, 230), (cx + 16, 230), (cx, 168)],
                         "none", K.E, 1.4))
        p.append(K._lbl(cx, 252, "%d" % (i + 1), "ts", "middle", K._fs(8)))
    return _emit_diagram(lang, "77a", W, H, p)


def F78(lang):
    W, H = 560, 310
    p = [K._lbl(24, 24, "(a) Trước nung / before firing", "ts", "start")]
    p.append(K._line(60, 60, 60, 250, K.E, 2))
    for i, y in enumerate([80, 120, 160, 200]):
        p.append(K._rect(60, y, 170, 12, K.FILL, K.E, 1.2))
        p.append(K._lbl(238, y + 10, "%d" % (i + 1), "ts", "start", K._fs(8)))
    p.append(K._lbl(300, 24, "(b) Sau nung / after firing", "ts", "start"))
    p.append(K._line(300, 60, 300, 250, K.E, 2))
    for i, y in enumerate([80, 120, 160, 200]):
        pts = [(300, y), (430, y), (450, y + 12), (470, y + 34)]
        p.append(K._pl(pts, K.E, 3))
        p.append(K._lbl(478, y + 18, "%d" % (i + 1), "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 78, W, H, p)


def F79(lang):
    W, H = 560, 300
    p = [K._rect(60, 210, 440, 30, K.DARK, K.E, 1.4),
         K._lbl(60, 204, "đế đồng thau / brass base", "ts", "start", K._fs(8)),
         K._circ(280, 160, 42, K.FILL, K.E, 1.4),
         K._lbl(280, 164, "vòng / ring", "ts", "middle", K._fs(8)),
         K._circ(228, 160, 6, K.DARK, K.E, 1.2),
         K._circ(332, 160, 6, K.DARK, K.E, 1.2),
         K._lbl(228, 184, "chốt / pins", "ts", "middle", K._fs(8)),
         K._line(280, 160, 430, 96, K.E, 2),
         K._poly([(430, 96), (422, 104), (438, 104)], K.E, K.E, 1),
         K._lbl(436, 90, "kim / pointer", "ts", "start", K._fs(8)),
         K._line(360, 120, 410, 90, K.S, 1.4),
         K._line(410, 90, 450, 120, K.S, 1.4),
         K._lbl(360, 138, "thước / scale", "ts", "start", K._fs(8))]
    return _emit_diagram(lang, 79, W, H, p)


def F80(lang):
    W, H = 560, 260
    p = [K._lbl(24, 24, "Sáp màu / crayon", "ts", "start"),
         K._rect(60, 60, 30, 150, K.FILL, K.E, 1.4),
         K._lbl(60, 222, "sáp / crayon", "ts", "start", K._fs(8)),
         K._lbl(300, 24, "Hạt / pellets", "ts", "start")]
    for cx, cy in [(330, 110), (380, 110), (430, 110), (480, 110),
                  (355, 165), (405, 165), (455, 165)]:
        p.append(K._circ(cx, cy, 16, K.FILL, K.E, 1.3))
    p.append(K._lbl(330, 210, "các hạt chỉ thị / pellets", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 80, W, H, p)


def F81(lang):
    W, H = 560, 200
    p = [K._rect(120, 50, 320, 100, K.FILL, K.E, 1.6)]
    for i, cx in enumerate([180, 260, 320, 400]):
        p.append(K._circ(cx, 100, 22, "none", K.E, 1.4))
        p.append(K._lbl(cx, 104, "%d" % (i + 1), "ts", "middle", K._fs(8)))
    p.append(K._lbl(120, 170, "nhãn bốn chấm / 4-dot label", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 81, W, H, p)


def F82(lang):
    W, H = 560, 320
    xr, yr = (20, 120), (0, 1)
    xt = [(20, "20"), (40, "40"), (60, "60"), (80, "80"),
          (100, "100"), (120, "120")]
    yt = [(0, "0"), (0.5, "0.5"), (1.0, "1.0")]
    curves = [([(20, 1.0), (40, 0.82), (60, 0.62), (80, 0.46),
                (100, 0.36), (120, 0.28)], "c1")]
    return _emit_chart(lang, 82, W, H, xr, yr, xt, yt, curves,
                       "nhiệt độ (°C) / temperature",
                       "bước xoắn / pitch")


def F83(lang):
    W, H = 560, 300
    p = []
    panels = [(0, "(a) nematic", 30, 60),
              (1, "(b) cholesteric", 300, 60),
              (2, "(c) smectic A", 30, 180),
              (3, "(d) smectic B", 300, 180)]
    for idx, lab, px, py in panels:
        p.append(K._lbl(px, py - 6, lab, "ts", "start", K._fs(8)))
        p.append(K._rect(px, py, 240, 90, K.FILL, K.E, 1.0))
        if idx in (0, 1):
            for j in range(5):
                yy = py + 15 + j * 15
                p.append(K._line(px + 30, yy, px + 90, yy, K.E, 2))
            if idx == 1:
                for j in range(5):
                    yy = py + 15 + j * 15
                    p.append(K._line(px + 120, yy, px + 180, yy + 8, K.E, 2))
        else:
            for j in range(4):
                yy = py + 20 + j * 20
                p.append(K._line(px + 20, yy, px + 220, yy, K.S, 1.5))
                for k in range(6):
                    p.append(K._circ(px + 30 + k * 36, yy, 4, K.DARK, K.E, 1))
    return _emit_diagram(lang, 83, W, H, p)


# ----------------------------------------------------------------- tables
def _t3226a(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["Số nón", "Nhiệt độ (°C)"] * 4
    else:
        hd = ["Cone no.", "Temperature (°C)"] * 4
    C1 = [("022", 600), ("021", 650), ("020", 670), ("019", 690), ("018", 710),
          ("017", 730), ("016", 750), ("015a", 790), ("014a", 815), ("013a", 835),
          ("012a", 855), ("011a", 880), ("010a", 900), ("09a", 920), ("08a", 940)]
    C2 = [("07a", 960), ("06a", 980), ("05a", 1000), ("04a", 1020), ("03a", 1040),
          ("02a", 1060), ("01a", 1080), ("1a", 1100), ("2a", 1120), ("3a", 1140),
          ("4a", 1160), ("5a", 1180), ("6a", 1200), ("7", 1230), ("8", 1250)]
    C3 = [("9", 1280), ("10", 1300), ("11", 1320), ("12", 1350), ("13", 1380),
          ("14", 1410), ("15", 1435), ("16", 1460), ("17", 1480), ("18", 1500),
          ("19", 1520), ("20", 1530), ("26", 1580), ("27", 1610), ("28", 1630)]
    C4 = [("29", 1650), ("30", 1670), ("31", 1690), ("32", 1710), ("33", 1730),
          ("34", 1750), ("35", 1770), ("36", 1790), ("37", 1825), ("38", 1850),
          ("39", 1880), ("40", 1920), ("41", 1960), ("42", 2000)]
    rows = []
    for r in range(15):
        row = [C1[r][0], C1[r][1], C2[r][0], C2[r][1], C3[r][0], C3[r][1]]
        row += list(C4[r]) if r < len(C4) else ["", ""]
        rows.append(row)
    cap = ("Bảng 32.26a · Nhiệt độ chạm đất xấp xỉ của các nón nhiệt (DIN 51063). "
           "Ghi chú: 1. Mỗi nhiệt độ là giá trị tại đó đầu nón uốn đủ để chạm "
           "vào đế trong lò điện với tốc độ nung 60 °C/h. 2. Nhiệt độ chạm đất "
           "phụ thuộc tốc độ nung; báo cáo nên ghi số nón, không lấy nhiệt độ từ "
           "bảng. 3. Mức uốn trung gian có thể quy chiếu theo kim đồng hồ, ví dụ "
           "3 giờ là nón uốn nửa chừng về giá." if vi else
           "Table 32.26a · Approximate touch-down temperatures of pyrometric cones "
           "(DIN 51063). Note: 1. Each temperature is that at which the tip of a "
           "cone will bend sufficiently to touch the base in an electric kiln at a "
           "heating rate of 60 °C h⁻¹. 2. The touch-down temperature depends on the "
           "rate of heating: reports should quote the cone number, not the "
           "temperature from the table. 3. Intermediate bending may be referred to "
           "the hands of a clock, e.g. 3 o'clock = a cone bent halfway to the stand.")
    return R.table(hd, rows, cap, small=True)


def _t3226b(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["Số nón", "Nhiệt độ (°C)"] * 4
    else:
        hd = ["Cone no.", "Temperature (°C)"] * 4
    C1 = [("022", 600), ("021", 615), ("020", 630), ("019", 665), ("018", 700),
          ("017", 730), ("016", 760), ("015", 790), ("014", 810), ("013", 830),
          ("012", 860)]
    C2 = [("011", 880), ("010", 900), ("09", 925), ("08", 950), ("07", 975),
          ("06", 1000), ("05", 1030), ("04", 1060), ("03", 1085), ("02", 1105),
          ("01", 1120)]
    C3 = [("1", 1135), ("2", 1150), ("3", 1165), ("4", 1180), ("5", 1195),
          ("6", 1210), ("7", 1230), ("8", 1250), ("9", 1270), ("10", 1290)]
    C4 = [("11", 1310), ("12", 1330), ("13", 1350), ("14", 1380), ("15", 1410),
          ("16", 1435), ("17", 1460), ("18", 1485), ("19", 1510), ("20", 1535)]
    rows = []
    for r in range(11):
        row = [C1[r][0], C1[r][1], C2[r][0], C2[r][1]]
        if r < len(C3):
            row += [C3[r][0], C3[r][1]]
        else:
            row += ["", ""]
        if r < len(C4):
            row += [C4[r][0], C4[r][1]]
        else:
            row += ["", ""]
        rows.append(row)
    cap = ("Bảng 32.26b · Nhiệt độ chạm đất xấp xỉ của các nón nhiệt (BS 1041). "
           "Các ghi chú tương tự Bảng 32.26a." if vi else
           "Table 32.26b · Approximate touch-down temperatures of pyrometric cones "
           "(BS 1041). Notes as for Table 32.26a.")
    return R.table(hd, rows, cap, small=True)


def _t3227(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["Số thanh", "Nhiệt độ (°C)"] * 4
    else:
        hd = ["Bar no.", "Temperature (°C)"] * 4
    C1 = [("1", 590), ("2", 610), ("3", 625), ("4", 650), ("5", 685), ("6", 715),
          ("7", 745), ("8", 775), ("9", 800), ("10", 820), ("11", 845)]
    C2 = [("12", 870), ("13", 890), ("14", 915), ("15", 940), ("16", 965),
          ("17", 990), ("18", 1015), ("19", 1045), ("20", 1075), ("21", 1095),
          ("22", 1115)]
    C3 = [("23", 1130), ("24", 1145), ("25", 1160), ("26", 1175), ("27", 1190),
          ("28", 1205), ("29", 1220), ("30", 1240), ("31", 1260), ("32", 1280),
          ("33", 1300)]
    C4 = [("34", 1320), ("35", 1340), ("36", 1365), ("37", 1395), ("38", 1425),
          ("39", 1450), ("40", 1475), ("41", 1500), ("42", 1525)]
    rows = []
    for r in range(11):
        row = [C1[r][0], C1[r][1], C2[r][0], C2[r][1], C3[r][0], C3[r][1]]
        row += list(C4[r]) if r < len(C4) else ["", ""]
        rows.append(row)
    cap = ("Bảng 32.27 · Nhiệt độ uốn xấp xỉ của các thanh thermoscope (BS 1041). "
           "Ghi chú: 1. Mỗi nhiệt độ là giá trị tại đó thanh bắt đầu uốn trong lò "
           "điện ở tốc độ nung 60 °C/h. 2. Nhiệt độ uốn phụ thuộc tốc độ nung. "
           "3. Thanh có thể uốn đủ để chạm giá ở nhiệt độ cao hơn 10–30 °C so với "
           "bảng, tùy thành phần." if vi else
           "Table 32.27 · Approximate bending temperatures of thermoscope bars "
           "(BS 1041). Note: 1. Each temperature is that at which the bar starts "
           "to bend in an electric kiln at 60 °C h⁻¹. 2. The bending temperature "
           "depends on the rate of heating. 3. The bar may bend sufficiently to "
           "touch the stand at 10–30 °C above the tabulated values, depending on "
           "composition.")
    return R.table(hd, rows, cap, small=True)


def _t3228(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["Nhiệt độ (°C)", "Vòng 55", "Vòng 27/84", "Vòng 75/84", "Vòng 73"]
    else:
        hd = ["Temperature (°C)", "Ring no. 55", "Ring no. 27/84",
              "Ring no. 75/84", "Ring no. 73"]
    temps = [960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070,
             1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180,
             1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290,
             1300, 1320, 1340, 1360, 1380, 1400, 1420, 1440]
    g55 = [3, 7, 11, 15, 18, 21, 24, 27, 30, 32, 34, 36, 37, 38, 39, 0, 1, 2.5,
           4, 5.5, 7, 8.5, 10, 11.5, 13, 14, 15.5, 17, 18.5, 20, 21.5, 23, 24.5,
           26, 27, 28.5, 30, 31.5, 33, 34.5, 36, ""]
    g2784 = [0, 1, 2, 3, 4, 5, 6, 7, 8.5, 10, 11, 12.5, 14, 15.5, 17, 18, 20, 21,
             22, 23, 24.5, 26, 27, 28, 29, 30, 31, 32, 33, 34.5, 36.5, 38.5, 40,
             42, 44, 46, "", "", "", "", "", "", ""]
    g7584 = [29.5, 30, 31, 34, 37, 40.5, 44, 48, 51, 54] + [""] * 32
    g73 = [29.5, 30, 31, 34, 37, 40.5, 44, 48, 51, 54] + [""] * 32
    rows = []
    for i, t in enumerate(temps):
        rows.append([t, g55[i], g2784[i], g7584[i], g73[i]])
    cap = ("Bảng 32.28 · Nhiệt độ định mức xấp xỉ cho các vòng Bullers và chỉ số "
           "thước đo tương ứng (BS 1041). Các giá trị này phải dùng thận trọng vì "
           "phụ thuộc chu trình nung." if vi else
           "Table 32.28 · Approximate rated temperatures for Bullers rings and the "
           "corresponding contraction-gage readings (BS 1041). Use with caution — "
           "values depend on the firing cycle.")
    return R.table(hd, rows, cap, small=True)


def _t3229(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["°F", "°C", "°F", "°C", "°F", "°C"]
    else:
        hd = ["°F", "°C", "°F", "°C", "°F", "°C"]
    f1 = [100, 103, 106, 109, 113, 119, 125, 131, 138, 144, 150, 156, 163, 169,
          175, 182, 188, 194, 200, 206, 213, 219, 225, 231, 238, 244, 250, 256,
          263, 269, 275, 282, 288, 294, 300, 306, 313, 319]
    c1 = [38, 39, 41, 43, 45, 48, 52, 55, 59, 62, 66, 69, 73, 76, 79, 83, 87, 90,
          93, 97, 101, 104, 107, 111, 114, 118, 121, 124, 128, 132, 135, 139, 142,
          146, 149, 152, 156, 159]
    f2 = [325, 331, 338, 344, 350, 363, 375, 388, 400, 413, 425, 438, 450, 463,
          475, 488, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775,
          800, 850, 900, 932, 950, 977, 1000, 1022, 1050]
    c2 = [163, 166, 170, 173, 177, 184, 191, 198, 204, 212, 218, 226, 232, 239,
          246, 253, 260, 274, 288, 302, 316, 329, 343, 357, 371, 385, 399, 427,
          454, 482, 500, 510, 525, 538, 550, 566, 593, 621]
    f3 = [1200, 1250, 1300, 1350, 1400, 1425, 1450, 1480, 1500, 1550, 1600, 1650,
          1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250,
          2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2800, 2900, 3000]
    c3 = [649, 677, 704, 732, 760, 774, 788, 804, 816, 843, 871, 899, 927, 954,
          982, 1010, 1032, 1066, 1093, 1121, 1149, 1177, 1204, 1232, 1260, 1288,
          1316, 1343, 1371, 1390, 1427, 1454, 1482, 1538, 1593, 1649]
    n = max(len(f1), len(f2), len(f3))
    rows = []
    for i in range(n):
        rows.append([f1[i] if i < len(f1) else "", c1[i] if i < len(c1) else "",
                     f2[i] if i < len(f2) else "", c2[i] if i < len(c2) else "",
                     f3[i] if i < len(f3) else "", c3[i] if i < len(c3) else ""])
    cap = ("Bảng 32.29 · Nhiệt độ định mức cho hạt, chất lỏng và sáp chỉ thị nhiệt "
           "độ. a: dãy “R” dùng trong khí quyển khử mạnh. b: chỉ có dạng hạt." if vi
           else "Table 32.29 · Rated temperatures for temperature-indicating "
           "pellets, liquids, and crayons. a: Series “R” pellets for strongly "
           "reducing atmospheres. b: available in pellets only.")
    return R.table(hd, rows, cap, small=True)


def _t3230(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["Mã", "°F", "°C", "°F", "°C", "°F", "°C", "°F", "°C"]
    else:
        hd = ["Model no.", "°F", "°C", "°F", "°C", "°F", "°C", "°F", "°C"]
    models = ["4A-100", "4A-110", "4A-120", "4A-130", "4A-140", "4A-150",
              "4A-160", "4A-170", "4A-180", "4A-190", "4A-200", "4A-210",
              "4A-220", "4A-230", "4A-240", "4A-250", "4A-260", "4A-270"]
    A = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230,
         240, 250, 260, 270]
    B = [38, 43, 49, 54, 60, 66, 71, 77, 82, 88, 93, 99, 104, 110, 116, 121, 127,
         132]
    C = [110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240,
         250, 260, 270, 280]
    D = [43, 49, 54, 60, 66, 71, 77, 82, 88, 93, 99, 104, 110, 116, 121, 127, 132,
         138]
    E = [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250,
         260, 270, 280, 290]
    F = [49, 54, 60, 66, 71, 77, 82, 88, 93, 99, 104, 110, 116, 121, 127, 132, 138,
         143]
    G = [130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260,
         270, 280, 290, 300]
    H = [54, 60, 66, 71, 77, 82, 88, 93, 99, 104, 110, 116, 121, 127, 132, 138,
         143, 149]
    rows = []
    for i, m in enumerate(models):
        rows.append([m, A[i], B[i], C[i], D[i], E[i], F[i], G[i], H[i]])
    cap = ("Bảng 32.30 · Nhiệt độ định mức cho nhãn 4-nhiệt-độ (4 chấm)." if vi
           else "Table 32.30 · Rated temperatures for 4-temperature (4-dot) labels.")
    return R.table(hd, rows, cap, small=True)


def _t3231(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["Màu gốc", "Màu tín hiệu", "Nhiệt kích hoạt ban đầu (°C)",
              "Nhiệt cắt (°C)"]
    else:
        hd = ["Original color", "Signal color",
              "Initial trigger temp. (°C)", "Cut-off temp. (°C)"]
    rows = [
        ["Pink", "Pink", 48, 30],
        ["Pink", "Pink", 135, 110],
        ["Mauve pink", "Mauve red", 148, 120],
        ["Blue", "Blue", 155, 46],
        ["Yellow", "Blue", 235, 180],
        ["Blue", "Blue", 275, 150],
        ["Mauve red", "Blue", 350, 220],
        ["Mauve", "Dark green", 386, 290],
        ["Green", "Red", 447, 312],
        ["Green", "Fawn", 458, 312],
        ["Orange", "Grey", 555, 482],
        ["Red", "White", 630, 450],
    ]
    cap = ("Bảng 32.31 · Sơn đổi màu một lần. a: nhiệt độ đổi màu ở thời gian nung "
           "10 phút." if vi else
           "Table 32.31 · Single-change paints. a: color-change temperature for "
           "10-min heating.")
    return R.table(hd, rows, cap, small=True)


def _t3232(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["Màu gốc", "Màu tín hiệu", "Nhiệt kích hoạt ban đầu (°C)",
              "Nhiệt cắt (°C)"]
    else:
        hd = ["Original color", "Signal color",
              "Initial trigger temp. (°C)", "Cut-off temp. (°C)"]
    rows = [
        ["Light tan", "Bronze green", "160 / 230", "150 / 210"],
        ["Reddish orange",
         "Dark gray / Medium gray / Dirty white",
         "242 / 255 / 338", "193 / 211 / 228"],
        ["Purple", "Pink / Fawn / Blue",
         "395 / 500 / 580", "355 / 386 / 408"],
        ["Red",
         "Dusty gray / Yellow / Orange / Green / Brown / Green-gray",
         "420 / 555 / 610 / 690 / 820 / 1050",
         "310 / 328 / 450 / 535 / 621 / 945"],
    ]
    cap = ("Bảng 32.32 · Sơn đổi màu nhiều lần. a: nhiệt độ đổi màu ở thời gian "
           "nung 10 phút." if vi else
           "Table 32.32 · Multichange paints. a: color-change temperature for "
           "10-min heating.")
    return R.table(hd, rows, cap, small=True)


def _t3233(lang):
    vi = (lang == "vi")
    if vi:
        hd = ["Màu gốc", "Màu tín hiệu", "Nhiệt kích hoạt ban đầu (°C)"]
    else:
        hd = ["Original color", "Signal color",
              "Initial trigger temp. (°C)"]
    orig = ["Ivory", "Light pink", "Light ivory", "Green", "Blue", "White",
            "Ochre", "Green", "Light green", "Blue", "Light blue", "Pink"]
    sig = ["Yellow & green", "Gray & white", "Light blue", "Light green", "Brown",
           "Light pink", "Blue", "Green", "Light green", "Blue", "Pink", "Black"]
    temp = [65, 75, 100, 120, 150, 200, 280, 300, 320, 350, 410, 450]
    rows = [[orig[i], sig[i], temp[i]] for i in range(12)]
    cap = ("Bảng 32.33 · Sáp màu đổi màu một lần." if vi else
           "Table 32.33 · Single-change crayons.")
    return R.table(hd, rows, cap, small=True)


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

    b = [R.h2("32.10 Chất chỉ thị nhiệt độ" if vi else "32.10 Temperature Indicators",
              "Temperature Indicators" if vi else "Chất chỉ thị nhiệt độ")]
    b.append(R.authors("Jan Stasiek, Tolestyn Madaj, and Jaroslaw Mikielewicz", ""))

    # ============================================ overview / melting indicators
    b.append(H3("Melting and Shape/Size Changing Temperature Indicators",
                "Chất chỉ thị nóng chảy và biến dạng hình dạng/kích thước"))
    b.append(P(
        "Temperature indicators serve for approximate determination of bodies' "
        "temperatures and are used to control a variety of temperature treatment "
        "processes. The temperatures are determined based on knowledge of "
        "characteristic rated temperatures, which are mean critical temperatures of "
        "the indicator. However, it should be stressed that the accuracy of these "
        "measurements is satisfactory only if the measurement conditions are similar "
        "to the standard conditions for which the temperature indicators were "
        "calibrated. Otherwise, the critical temperatures of the indicators can be "
        "different from their rated temperatures listed in the standards and the "
        "measurements can have considerable errors.",
        "Chất chỉ thị nhiệt độ dùng để xác định gần đúng nhiệt độ của vật thể và "
        "được dùng kiểm soát nhiều quá trình xử lý nhiệt. Nhiệt độ được xác định "
        "dựa trên các nhiệt độ định mức đặc trưng — tức là nhiệt độ tới hạn trung "
        "bình của chất chỉ thị. Tuy nhiên, cần nhấn mạnh rằng độ chính xác của các "
        "phép đo này chỉ thoả đáng khi điều kiện đo tương tự điều kiện chuẩn mà theo "
        "đó chất chỉ thị được hiệu chuẩn. Nếu không, nhiệt độ tới hạn của chất chỉ "
        "thị có thể khác với nhiệt độ định mức ghi trong các tiêu chuẩn và phép đo "
        "sẽ sai lệch đáng kể."))
    b.append(P(
        "The temperature indicators can be classified into two groups, each group "
        "using different physical properties for the determination of the "
        "temperature. The indicators belonging to the first group melt at certain "
        "temperatures. For some of these indicators, such as pyrometric cones, "
        "thermoscope bars and rings, the process of melting manifests itself as a "
        "shape/size deformation for which the temperature is determined by measuring "
        "the degree/rate of deformation of the indicator. For others, such as melting "
        "pellets, liquids, crayons, and monitors, the melting means turning entirely "
        "into a liquid smear. This can also be accompanied by color changing. The "
        "second group consists of color-change indicators containing pigments that at "
        "different temperatures, show different colors by selectively reflecting "
        "incident white light. Among this group are reversible and irreversible "
        "paints, color-change crayons, and liquid-crystal indicators.",
        "Chất chỉ thị nhiệt độ có thể chia thành hai nhóm, mỗi nhóm dùng một tính "
        "chất vật lý khác nhau để xác định nhiệt độ. Nhóm thứ nhất nóng chảy ở "
        "những nhiệt độ nhất định. Ở một số chất chỉ thị như nón nhiệt, thanh "
        "thermoscope và vòng, quá trình nóng chảy biểu hiện như một biến dạng hình "
        "dạng/kích thước, và nhiệt độ được xác định bằng cách đo mức độ/tốc độ biến "
        "dạng của chất chỉ thị. Ở các loại khác như hạt nóng chảy, chất lỏng, sáp "
        "màu và nhãn, nóng chảy nghĩa là chuyển hoàn toàn thành một lớp màng lỏng; "
        "điều này cũng có thể kèm theo đổi màu. Nhóm thứ hai gồm các chất chỉ thị "
        "đổi màu chứa pigment ở các nhiệt độ khác nhau sẽ phản chiếu có chọn lọc ánh "
        "sáng trắng tới, tạo ra các màu khác nhau. Thuộc nhóm này có sơn hồi phục và "
        "không hồi phục, sáp màu đổi màu và chất chỉ thị tinh thể lỏng."))
    b.append(P(
        "The latest British Standard BS 1041, Part 7, 1988 [1] lists the following "
        "temperature indicators: Seger cones, thermoscope bars, and Bullers rings. "
        "Some temperature indicators used in the past — such as Watkin cylinders and "
        "Holcdorft bars — are no longer used and are of historical value only. In the "
        "U.S., melting pellets, crayons, liquids and monitors are available on the "
        "market and widely used.",
        "Tiêu chuẩn Anh mới nhất BS 1041, Phần 7, 1988 [1] liệt kê các chất chỉ thị "
        "nhiệt độ sau: nón Seger, thanh thermoscope và vòng Bullers. Một số chất chỉ "
        "thị dùng trong quá khứ — như xi lanh Watkin và thanh Holcdorft — không còn "
        "được dùng và chỉ còn giá trị lịch sử. Tại Mỹ, hạt nóng chảy, sáp, chất lỏng "
        "và nhãn có bán rộng rãi và được dùng phổ biến."))

    # ============================================================ Seger cones
    b.append(H3("Seger Cones", "Nón Seger"))
    b.append(P(
        "The rated temperature for Seger cones (pyrometric cones) and thermoscope "
        "bars is defined by appropriate shape deformation resulting from the "
        "transformation of a certain amount of the indicator substance from the "
        "solid to liquid state. For chemically pure elements and compounds at a "
        "constant pressure, the temperature during the entire process of phase "
        "change remains constant. If the pressure changes within the range of "
        "changes for atmospheric pressure, then the temperature changes are "
        "insignificant and can be neglected even during precise measurements. The "
        "pyrometric cones and thermoscope bars are prepared from complex mixes of "
        "frits, fluxes, clays, calcium and magnesium compounds, silica, etc. The "
        "melting temperatures of the indicators, also referred to as the critical or "
        "rated temperatures, vary with the proportions of the above compounds. "
        "Therefore, a set of indicators differing in the proportions of the "
        "compounds is capable of covering a required range of rated temperatures. "
        "The melting temperatures can also change, to a degree, with the proportion "
        "of phases. For mixes that constitute pyrometric cones and thermoscope bars, "
        "the temperature difference between the beginning and the end of the melting "
        "process can be as large as 25 to 40 °C.",
        "Nhiệt độ định mức của nón Seger (nón nhiệt) và thanh thermoscope được định "
        "nghĩa bằng biến dạng hình dạng thích hợp do sự biến đổi một lượng nhất định "
        "chất chỉ thị từ thể rắn sang thể lỏng. Với các nguyên tố và hợp chất hóa học "
        "tinh khiết ở áp suất không đổi, nhiệt độ trong toàn bộ quá trình chuyển "
        "pha không đổi. Nếu áp suất thay đổi trong dải biến thiên của áp suất khí "
        "quyển thì sự thay đổi nhiệt độ không đáng kể và có thể bỏ qua ngay cả trong "
        "đo chính xác. Nón nhiệt và thanh thermoscope được chế từ hỗn hợp phức tạp "
        "của các loại frit, chất trợ chảy, đất sét, hợp chất canxi và magiê, silica, "
        "v.v. Nhiệt độ nóng chảy của chất chỉ thị — còn gọi là nhiệt độ tới hạn hay "
        "định mức — thay đổi theo tỉ lệ các hợp chất nói trên. Do đó, một bộ chất chỉ "
        "thị khác nhau về tỉ lệ hợp chất có thể phủ một dải nhiệt độ định mức yêu "
        "cầu. Nhiệt độ nóng chảy cũng có thể thay đổi một phần theo tỉ lệ pha. Với "
        "các hỗn hợp tạo nên nón nhiệt và thanh thermoscope, chênh lệch nhiệt độ giữa "
        "lúc bắt đầu và kết thúc quá trình nóng chảy có thể lên tới 25–40 °C."))
    b.append(P(
        "The pyrometric cones are typically slender, truncated, trihedral pyramids, "
        "about 25 mm to 60 mm in height. The base of the pyramid is a regular "
        "triangle of side 7 mm to 16 mm. One edge of the pyramid is vertical or "
        "slightly leaned outward (see Figure 32.77a). The recommended height of the "
        "standard cones is 60 mm; the laboratory cones are 30 mm high.",
        "Nón nhiệt thường là các chóp tam diện thon, cụt, cao khoảng 25–60 mm. Đáy "
        "chóp là tam giác đều cạnh 7–16 mm. Một cạnh của chóp thẳng đứng hoặc hơi "
        "nghiêng ra ngoài (xem Hình 32.77a). Chiều cao khuyến nghị của nón chuẩn là "
        "60 mm; nón phòng thí nghiệm cao 30 mm."))
    b.append(P(
        "The pyramids are manufactured by pressing a powder mixture of a number of "
        "minerals mixed in different proportions throughout the required range of "
        "rated temperatures. The main components are silicon oxide (SiO₂), aluminium "
        "oxide (Al₂O₃) with additives in the form of oxides (MgO, K₂O, Na₂O, CaO, "
        "B₂O₃, PbO), and an organic binder. The following equation is an example of "
        "chemical constitution of the pyrometric cone for the temperature range of "
        "600 °C to 900 °C:",
        "Các chóp được chế bằng cách ép hỗn hợp bột của một số khoáng chất trộn theo "
        "tỉ lệ khác nhau trên toàn dải nhiệt độ định mức yêu cầu. Thành phần chính là "
        "silic điôxít (SiO₂), nhôm ôxít (Al₂O₃) với các phụ gia dạng ôxít (MgO, "
        "K₂O, Na₂O, CaO, B₂O₃, PbO) và một chất kết dính hữu cơ. Phương trình sau là "
        "một ví dụ về thành phần hóa học của nón nhiệt cho dải nhiệt độ 600–900 °C:"))
    b.append(EQ("X·SiO<sub>2</sub> + (1 − 0.5X)·Al<sub>2</sub>O<sub>3</sub> + "
                "X·Na<sub>2</sub>O + PbO + B<sub>2</sub>O<sub>3</sub> + "
                "(2 + 2X)·SiO<sub>2</sub>", "32.1"))
    b.append(F77a(lang))
    b.append(P(
        "Touch-down Temperatures for Seger Cones. As the heating progresses, the "
        "cone used for the measurement begins to soften and bends until its tip "
        "touches down on the surface on which it was placed. The rated temperature "
        "referring to this deformation is called the touch-down temperature. The "
        "touch-down temperatures for the Seger cones are determined in an electric "
        "kiln with clean atmospheric air at a heating rate of 60 °C h⁻¹.",
        "Nhiệt độ chạm đất của nón Seger. Khi nung tiếp diễn, nón dùng đo bắt đầu "
        "mềm và uốn cong cho đến khi đầu nón chạm xuống mặt đặt nó. Nhiệt độ định "
        "mức ứng với biến dạng này gọi là nhiệt độ chạm đất. Nhiệt độ chạm đất của "
        "nón Seger được xác định trong lò điện với không khí sạch ở tốc độ nung "
        "60 °C/h."))
    b.append(P(
        "According to the earlier German standard DIN 51063 [2], the range of "
        "touch-down temperatures from 600 °C to 2000 °C at 10 to 50 °C steps is "
        "covered by a series of Seger cones denoted traditionally by numbers from 022 "
        "to 42 (see Table 32.26a). According to the latest British Standard BS 1041, "
        "Part 7, 1988, the touch-down temperatures within the range of 600 °C to "
        "1535 °C at temperature intervals of 15 to 35 °C are realized by a series of "
        "Seger cones numbered from 022 to 20 (see Table 32.26b).",
        "Theo tiêu chuẩn Đức cũ DIN 51063 [2], dải nhiệt độ chạm đất từ 600–2000 °C "
        "với bước 10–50 °C được phủ bởi một dãy nón Seger ký hiệu truyền thống từ 022 "
        "đến 42 (xem Bảng 32.26a). Theo tiêu chuẩn Anh mới nhất BS 1041, Phần 7, "
        "1988, các nhiệt độ chạm đất trong dải 600–1535 °C với bước 15–35 °C được "
        "thực hiện bởi dãy nón Seger đánh số từ 022 đến 20 (xem Bảng 32.26b)."))
    b.append(_t3226a(lang))
    b.append(_t3226b(lang))
    b.append(P(
        "The precision of determination of the touch-down temperatures for the "
        "industrial cones should be better than ±15 °C; for the laboratory cones, "
        "better than ±10 °C. If the heating rate undergoes change within the range of "
        "20 to 150 °C h⁻¹, then the rated temperatures can change by −40 °C for the "
        "above lower limiting value of the heating rate up to 60 °C for the upper "
        "value. A 0.35 % content of SO₂ in the atmosphere increases the rated "
        "temperatures by about 35 °C. Also, the presence of soot in the atmosphere "
        "slightly raises the rated temperatures.",
        "Độ chính xác xác định nhiệt độ chạm đất cho nón công nghiệp nên tốt hơn "
        "±15 °C; với nón phòng thí nghiệm tốt hơn ±10 °C. Nếu tốc độ nung thay đổi "
        "trong dải 20–150 °C/h thì nhiệt độ định mức có thể đổi −40 °C ở giới hạn "
        "dưới tới 60 °C ở giới hạn trên. Hàm lượng 0,35 % SO₂ trong khí quyển làm "
        "tăng nhiệt độ định mức khoảng 35 °C. Mặt khác, sự hiện diện của muội than "
        "trong khí quyển cũng làm nhiệt độ định mức tăng nhẹ."))
    b.append(P(
        "How to Use the Materials. While single cones are sometimes used, usually "
        "three or four consecutively numbered cones, including a cone whose rated "
        "temperature is equal to the required temperature of the heat treatment and "
        "two cones of neighboring numbers (one less and one more) are employed for "
        "the temperature determination (see Figure 32.77b). They are installed into "
        "specially unfired plaques with tapered holes and protrusions that hold the "
        "cones firmly. The plaques are mounted to a workpiece surface to allow "
        "observations. A cone can be set up in other ways, such as inserting its base "
        "into refractory clay. However, it is necessary to assure a correct angle and "
        "firm hold of the cones during the firing cycle.",
        "Cách dùng vật liệu. Dù đôi khi dùng đơn nón, thường người ta dùng ba hoặc "
        "bốn nón đánh số liên tiếp, gồm một nón có nhiệt độ định mức bằng nhiệt độ "
        "xử lý nhiệt yêu cầu và hai nón số lân cận (một thấp hơn, một cao hơn) để xác "
        "định nhiệt độ (xem Hình 32.77b). Chúng được lắp vào các tấm đế chưa nung "
        "đặc biệt có lỗ côn và gờ giữ nón chắc chắn. Tấm đế gắn vào bề mặt chi tiết "
        "để quan sát. Nón cũng có thể đặt theo cách khác, như cắm đáy vào đất sét "
        "chịu lửa. Tuy nhiên, cần đảm bảo góc đúng và giữ chắc nón trong suốt chu "
        "trình nung."))
    b.append(P(
        "If the process of heating takes place with a standard heating rate, then "
        "the rated temperature is reached when the tip of the central cone touches "
        "the base of the plaque. With further prolongation of the firing cycle, the "
        "cone will melt completely to form a blob on the plaque. The process of "
        "reaching the rated temperature is signaled in advance by the cone of "
        "one-less number. The cone of one-more number is there to prove that the "
        "required temperature value is not exceeded. Placing a series of cones with "
        "lower numbers (lower rated temperatures) provides the opportunity to carry "
        "out the process of heating at a required rate.",
        "Nếu nung với tốc độ chuẩn, nhiệt độ định mức đạt được khi đầu nón giữa chạm "
        "vào đáy tấm đế. Nung tiếp, nón sẽ nóng chảy hoàn toàn thành một khối trên "
        "tấm đế. Quá trình đạt nhiệt độ định mức được báo trước bởi nón số thấp hơn "
        "một. Nón số cao hơn một dùng để chứng tỏ nhiệt độ yêu cầu không bị vượt quá. "
        "Việc đặt dãy nón số thấp hơn (nhiệt độ định mức thấp hơn) cho phép tiến hành "
        "nung với tốc độ yêu cầu."))
    b.append(P(
        "Typical Application. Seger cones are used for the control of firing "
        "processes in the ceramics industry and artistry.",
        "Ứng dụng điển hình. Nón Seger dùng kiểm soát quá trình nung trong công "
        "nghiệp và nghệ thuật gốm sứ."))

    # ============================================================ thermoscope
    b.append(H3("Thermoscope Bars", "Thanh thermoscope"))
    b.append(P(
        "These indicators have the shape of bars of rectangular cross-sections. The "
        "typical dimensions of the bars are: length, 57 mm; width, 8 mm; and height, "
        "6 mm. Bars of consecutive numbers (rated temperatures) are placed "
        "horizontally on a refractory stand as in Figure 32.78. The set of "
        "thermoscope bars is a more convenient and slightly modified form of "
        "Holcdorft bars. The bars are made of the same composites (mineral mixes and "
        "organic binder) as the pyrometric cones. The mixed powders are pressed and "
        "can be hardened by prefiring at relatively low temperatures, below those at "
        "which bending should occur.",
        "Các chất chỉ thị này có dạng thanh mặt cắt chữ nhật. Kích thước điển hình: "
        "dài 57 mm, rộng 8 mm, cao 6 mm. Các thanh đánh số liên tiếp (nhiệt độ định "
        "mức) đặt nằm ngang trên giá chịu lửa như ở Hình 32.78. Bộ thanh thermoscope "
        "là dạng tiện lợi và hơi biến đổi của thanh Holcdorft. Thanh làm từ cùng hỗn "
        "hợp (khoáng trộn và chất kết dính hữu cơ) như nón nhiệt. Bột trộn được ép và "
        "có thể tôi cứng bằng nung sơ ở nhiệt độ thấp, dưới ngưỡng uốn."))
    b.append(F78(lang))
    b.append(P(
        "Bending Temperatures of Thermoscope Bars. The rated temperatures of "
        "thermoscope bars, referred to as the bending temperatures, are found during "
        "the calibration in an electric kiln with a heating rate of 60 °C h⁻¹ when "
        "the bars start to exhibit deformation (i.e., begin to bend). According to "
        "the British Standard BS 1041, the range of rated temperatures from 590 °C to "
        "1525 °C at temperature intervals of 15 to 35 °C is covered by 42 thermoscope "
        "bars (see Table 32.27). The precision of determination of the bending is "
        "about ±15 °C; the other properties of the thermoscope bars referring to "
        "changes of the standard conditions are the same as for the pyrometric cones.",
        "Nhiệt độ uốn của thanh thermoscope. Nhiệt độ định mức của thanh thermoscope, "
        "gọi là nhiệt độ uốn, được tìm khi hiệu chuẩn trong lò điện ở tốc độ nung "
        "60 °C/h, khi thanh bắt đầu biến dạng (tức là uốn). Theo tiêu chuẩn Anh BS "
        "1041, dải nhiệt độ định mức 590–1525 °C với bước 15–35 °C được phủ bởi 42 "
        "thanh thermoscope (xem Bảng 32.27). Độ chính xác xác định nhiệt độ uốn khoảng "
        "±15 °C; các tính chất khác của thanh thermoscope khi đổi điều kiện chuẩn giống "
        "như nón nhiệt."))
    b.append(_t3227(lang))
    b.append(P(
        "How to Use the Materials. Four thermoscope bars of consecutive numbers — the "
        "first two having lower bending temperatures, the third one having the bending "
        "temperature equal or close to the required temperature, the fourth one having "
        "a higher bending temperature — are placed in sequence on a special refractory "
        "stand as in Figure 32.78a. The set is mounted to the workpiece surface where "
        "observations take place. If the process of heating takes place with a standard "
        "heating rate, then the beginning of deformation (bending) of the third bar "
        "indicates that the required temperature is reached. The process of reaching "
        "the rated temperature for the third bar is signaled in advance by the "
        "deformation of the proceeding bars whose behavior allows the evaluation of the "
        "heating rate. The unbent fourth bar testifies that the required temperature is "
        "not exceeded (see Figure 32.78b).",
        "Cách dùng vật liệu. Bốn thanh thermoscope số liên tiếp — hai thanh đầu có nhiệt "
        "độ uốn thấp hơn, thanh thứ ba có nhiệt độ uốn bằng hoặc gần nhiệt độ yêu cầu, "
        "thanh thứ tư có nhiệt độ uốn cao hơn — được đặt nối tiếp trên giá chịu lửa đặc "
        "biệt như Hình 32.78a. Bộ được gắn vào bề mặt chi tiết để quan sát. Nếu nung "
        "với tốc độ chuẩn, sự bắt đầu biến dạng (uốn) của thanh thứ ba báo hiệu nhiệt "
        "độ yêu cầu đạt được. Quá trình đạt nhiệt độ định mức của thanh thứ ba được báo "
        "trước bởi biến dạng của các thanh trước, cho phép đánh giá tốc độ nung. Thanh "
        "thứ tư không uốn chứng tỏ nhiệt độ yêu cầu chưa bị vượt quá (xem Hình 32.78b)."))
    b.append(P(
        "Typical Application. The application of the thermoscope bars is identical to "
        "that of the Seger cones.",
        "Ứng dụng điển hình. Ứng dụng của thanh thermoscope giống hệt nón Seger."))

    # ============================================================ Bullers rings
    b.append(H3("Bullers Rings", "Vòng Bullers"))
    b.append(P(
        "These temperature indicators in the form of rings have the following "
        "dimensions: outer diameter, 63 mm; inner diameter, 22 mm; and width, 8 mm. "
        "The appropriate measuring unit consists of a Bullers ring and a specially "
        "prescaled device for measurement of the temperature shrinkage of the ring. "
        "This contraction gage measures the outer diameter of the heated ring, based "
        "on which the heating work is assessed. The full measuring range of rated "
        "temperatures from 960 °C to 1440 °C is covered by four types of rings "
        "manufactured by pressing powders of ceramics mixes, with a binder, and "
        "without prefiring.",
        "Các chất chỉ thị dạng vòng này có kích thước: đường kính ngoài 63 mm, đường "
        "kính trong 22 mm, rộng 8 mm. Bộ đo thích hợp gồm một vòng Bullers và một thiết "
        "bị thu nhỏ đặc biệt để đo độ co ngót nhiệt của vòng. Thước đo co ngót này đo "
        "đường kính ngoài của vòng đã nung, từ đó đánh giá mức nung. Toàn dải đo nhiệt "
        "độ định mức 960–1440 °C được phủ bởi bốn loại vòng chế bằng ép bột hỗn hợp gốm "
        "với chất kết dính, không nung sơ."))
    b.append(F79(lang))
    b.append(P(
        "1. Rings denoted as 55 of brown color, suitable for temperatures from 960 °C "
        "to 1100 °C are used in the firing of glost ware and common building bricks "
        "where the finishing temperatures are relatively low. 2. Rings numbered "
        "27/84, colored green, suitable for temperatures from 960 °C to 1250 °C are "
        "used for firing earthenware at the medium finishing temperatures, as well as "
        "tiles and bricks refractory with respect to low temperatures. 3. Rings "
        "numbered 75/84, colored natural, recommended for firing temperatures from "
        "960 °C to 1320 °C, allow for higher finishing temperatures and are used for "
        "firing electrical porcelain, china, grinding wheels, and bricks refractory "
        "with respect to higher temperatures. 4. Rings numbered 73, colored yellow, "
        "recommended for temperatures from 1280 °C to 1440 °C for slow firing "
        "conditions as used in the manufacture of high-temperature ceramics and heavy "
        "refractories.",
        "1. Vòng ký hiệu 55 màu nâu, dùng cho 960–1100 °C, dùng nung đồ sành tráng "
        "men và gạch xây dựng thường có nhiệt độ kết thúc thấp. 2. Vòng 27/84 màu "
        "xanh lục, dùng cho 960–1250 °C, nung đồ gốm đất ở nhiệt độ kết thúc trung "
        "bình, cũng như gạch lát và gạch chịu lửa ở nhiệt độ thấp. 3. Vòng 75/84 màu "
        "tự nhiên, khuyên dùng 960–1320 °C, cho phép nhiệt độ kết thúc cao hơn, dùng "
        "nung sứ điện, đồ sứ, bánh mài và gạch chịu lửa ở nhiệt độ cao hơn. 4. Vòng 73 "
        "màu vàng, khuyên dùng 1280–1440 °C cho điều kiện nung chậm trong sản xuất gốm "
        "sứ nhiệt độ cao và vật liệu chịu lửa nặng."))
    b.append(P(
        "Approximate rated temperatures for the Bullers rings and corresponding "
        "readings of the contraction gage according to the British Standard BS 1041 "
        "are presented in Table 32.28.",
        "Nhiệt độ định mức xấp xỉ cho vòng Bullers và chỉ số thước đo co ngót tương "
        "ứng theo tiêu chuẩn Anh BS 1041 được trình bày trong Bảng 32.28."))
    b.append(_t3228(lang))
    b.append(P(
        "How to Use the Materials. One or more rings of the same type are placed "
        "vertically in a prefired stand and mounted to a workpiece surface. To "
        "determine the temperature as the firing progresses, the heated rings are "
        "withdrawn from their stands, cooled to the ambient temperature, and then "
        "measured for contraction. This measurement is carried out on a gage "
        "consisting of a brass base plate on which a radial arm with a pointer moving "
        "over a scale and two steel dowel pins, against which the ring is pressed by "
        "the movable arm, are mounted (see Figure 32.79). A contraction of the ring "
        "gives rise to an amplified movement of the pointer over the scale. The "
        "divisions on the scale are numbered from −5 to 60. More heavily fired rings "
        "contract more and give higher readings on the gage. The divisions below 0 "
        "indicate expansion of the ring; above 0 indicates contraction. Rings should "
        "be measured across several diameters by turning them around in the gage so as "
        "to find the mean value to which the temperature can be assigned with the help "
        "of Table 32.28. Placing several rings in the stand in a manner that allows "
        "their easy withdrawal gives the possibility of measuring the heating rate. In "
        "a similar way, distribution of a number of rings throughout the furnace enables "
        "the determination of the temperature field in the furnace.",
        "Cách dùng vật liệu. Một hoặc nhiều vòng cùng loại đặt thẳng đứng trong giá đã "
        "nung sơ và gắn vào bề mặt chi tiết. Để xác định nhiệt độ khi nung tiến triển, "
        "các vòng đã nung được rút khỏi giá, làm nguội đến nhiệt độ môi trường, rồi đo "
        "độ co ngót. Phép đo thực hiện trên thước gồm tấm đế đồng thau có cánh tay hướng "
        "tâm mang kim trượt trên thang chia và hai chốt thép, vòng được ép vào bởi tay "
        "ngắn di động (xem Hình 32.79). Độ co của vòng làm kim di chuyển khuếch đại "
        "trên thang. Vạch thang đánh số từ −5 đến 60. Vòng nung kỹ hơn co nhiều hơn và "
        "cho chỉ số cao hơn. Vạch dưới 0 biểu thị giãn nở; trên 0 biểu thị co ngót. Vòng "
        "nên đo qua nhiều đường kính bằng cách xoay trong thước để tìm giá trị trung "
        "bình, từ đó tra nhiệt độ theo Bảng 32.28. Đặt nhiều vòng trong giá sao dễ rút "
        "cho phép đo tốc độ nung. Tương tự, phân bố nhiều vòng trong lò cho phép xác "
        "định trường nhiệt độ trong lò."))
    b.append(P(
        "Usually, one or more test pieces from a series of rings are picked out for "
        "the sake of calibration so as to compare the obtained readings with the "
        "standard values enclosed in Table 32.28. Intermediate measurements are also "
        "carried out to evaluate the effect of the heating rate on the temperature "
        "shrinkage of the rings. The accuracy of the temperature determination for the "
        "standard heating conditions is ±0.5 of a single division of the scale.",
        "Thường người ta chọn một hoặc nhiều mẫu thử từ dãy vòng để hiệu chuẩn, so sánh "
        "chỉ số thu được với giá trị chuẩn trong Bảng 32.28. Các phép đo trung gian "
        "cũng được thực hiện để đánh giá ảnh hưởng của tốc độ nung đến độ co ngót nhiệt "
        "của vòng. Độ chính xác xác định nhiệt độ ở điều kiện nung chuẩn là ±0,5 một "
        "vạch thang."))
    b.append(P(
        "Typical Application. The application of the Bullers rings is similar to the "
        "Seger cones and thermoscope bars. An inconvenience is the fact that the "
        "Bullers rings require gage measurements and the temperature cannot be solely "
        "determined based on naked-eye observations.",
        "Ứng dụng điển hình. Ứng dụng vòng Bullers tương tự nón Seger và thanh "
        "thermoscope. Bất tiện là vòng Bullers cần đo bằng thước và nhiệt độ không "
        "thể xác định chỉ bằng quan sát thường."))

    # ============================ pellets, liquids, crayons, monitors
    b.append(H3("Temperature-Indicating Pellets, Liquids, Crayons, and Monitors",
                "Hạt, chất lỏng, sáp màu và nhãn chỉ thị nhiệt độ"))
    b.append(P(
        "Temperature-indicating pellets are manufactured by pressing powders of "
        "mineral mixes of certain melting temperatures and an indifferent binder. "
        "Melting pellets are recommended as standard tablets 7/16 · 1/8 and miniature "
        "tablets 1/8 · 1/8 (see Figure 32.80). There are 112 different pellets which "
        "cover the temperature range from 40 °C (100 °F) to 1650 °C (3000 °F); see "
        "Table 32.29. The accuracy of the temperature determination is ±1 % of the "
        "rated temperature. There are also available pellets for temperature control "
        "in strongly reducing atmospheres.",
        "Hạt chỉ thị nhiệt độ được chế bằng ép bột hỗn hợp khoáng có nhiệt độ nóng "
        "chảy nhất định và chất kết dính trơ. Hạt nóng chảy được khuyên dùng dạng viên "
        "chuẩn 7/16 · 1/8 và viên thu nhỏ 1/8 · 1/8 (xem Hình 32.80). Có 112 loại hạt "
        "khác nhau phủ dải 40 °C (100 °F) đến 1650 °C (3000 °F); xem Bảng 32.29. Độ "
        "chính xác xác định nhiệt độ là ±1 % nhiệt độ định mức. Cũng có hạt dùng kiểm "
        "soát nhiệt độ trong khí quyển khử mạnh."))
    b.append(H4("Temperature-Indicating Pellets", "Hạt chỉ thị nhiệt độ"))
    b.append(P(
        "How to Use the Materials. A pellet of the rated temperature equal to the "
        "required temperature of heat treatment is placed on the investigated surface "
        "before the heating starts. When the heating progresses, the beginning of "
        "melting signals that the rated temperature is reached. Placing more pellets "
        "with the rated temperatures lower and higher than the required temperature "
        "enables more precise control of the heating process. Typical applications are "
        "checking furnace temperatures, control of heat treating of large units, as "
        "well as other applications involving long-duration heating.",
        "Cách dùng vật liệu. Đặt một hạt có nhiệt độ định mức bằng nhiệt độ xử lý nhiệt "
        "yêu cầu lên bề mặt cần khảo sát trước khi nung. Khi nung tiến triển, sự bắt "
        "đầu nóng chảy báo hiệu nhiệt độ định mức đạt được. Đặt thêm các hạt có nhiệt "
        "độ định mức thấp hơn và cao hơn nhiệt độ yêu cầu cho phép kiểm soát chính xác "
        "hơn. Ứng dụng điển hình: kiểm tra nhiệt độ lò, kiểm soát xử lý nhiệt các chi "
        "tiết lớn, cùng các ứng dụng nung dài hạn khác."))
    b.append(F80(lang))
    b.append(_t3229(lang))
    b.append(H4("Temperature-Indicating Liquids", "Chất lỏng chỉ thị nhiệt độ"))
    b.append(P(
        "Temperature-indicating liquids are solutions of powdered mineral mixes in "
        "indifferent highly volatile solvents. They are available for use by brushing "
        "or spraying. There are over 100 different liquids with the rated temperatures "
        "from 40 °C (100 °F) to 1371 °C (2500 °F); see Table 32.29. The accuracy of "
        "the temperature determination is ±1 % of the rated temperature. A thin coating "
        "of the liquid is put on the clean and dry surface by brushing or spraying "
        "before the heating starts. It dries almost instantly to a dull opaque mark. "
        "When the required temperature is reached, this mark liquefies. The melted "
        "coating does not revert to its original opaque appearance but remains "
        "glossy-transparent on cooling. It should be noted that color changes do not "
        "signal the required temperature. The melting, not the color change, is the "
        "temperature signal. They are recommended for temperature control on fabrics, "
        "rubber, plastics, on smooth surfaces such as glass or polished metals, as "
        "well as for monitoring critical temperatures in electronic fields.",
        "Chất lỏng chỉ thị nhiệt độ là dung dịch bột khoáng trong dung môi dễ bay hơi "
        "trơ. Dùng bằng chổi hoặc phun. Có hơn 100 loại chất lỏng với nhiệt độ định "
        "mức 40 °C (100 °F) đến 1371 °C (2500 °F); xem Bảng 32.29. Độ chính xác là "
        "±1 % nhiệt độ định mức. Phủ một lớp mỏng lên bề mặt sạch khô bằng chổi hoặc "
        "phun trước khi nung. Nó khô hầu như ngay thành vết mờ đục. Khi nhiệt độ yêu "
        "cầu đạt được, vết này hoá lỏng. Lớp đã nóng chảy không trở lại trạng thái đục "
        "ban đầu mà trong suốt bóng khi nguội. Cần lưu ý đổi màu không báo hiệu nhiệt "
        "độ yêu cầu — chính sự nóng chảy mới là tín hiệu nhiệt độ. Chất lỏng được khuyên "
        "dùng kiểm soát nhiệt độ trên vải, cao su, nhựa, trên bề mặt nhẵn như thủy tinh "
        "hay kim loại đánh bóng, cũng như giám sát nhiệt độ tới hạn trong điện tử."))
    b.append(H4("Temperature-Indicating Crayons", "Sáp màu chỉ thị nhiệt độ"))
    b.append(P(
        "Temperature-indicating crayons are sticks manufactured from powders of "
        "mineral mixes of certain melting temperatures and an indifferent binder. The "
        "crayons are put in specially adjustable metal holders with labels saying their "
        "rated temperatures; see Figure 32.80. Similar to the temperature-indicating "
        "liquids, there are over 100 different crayons that cover the temperature range "
        "from 40 °C (100 °F) to 1371 °C (2500 °F); see Table 32.29. The accuracy of "
        "the temperature determination is also ±1 % of the rated temperature. During "
        "heating, the workpiece should be struck repeatedly by the crayon. Below its "
        "rated temperature, the crayon leaves a dry opaque mark. When the rated "
        "temperature is reached, the crayon leaves a liquid smear. On cooling, the "
        "liquid mark will solidify with a transparent or translucent appearance. The "
        "moment of melting, not any change in color, is the temperature signal. The "
        "crayons can be applied in welding, forging, heat treating and fabrication of "
        "metals, molding of rubber and plastics, wherever the workpiece is accessible "
        "during the heating process. Very smooth surfaces are excluded.",
        "Sáp màu chỉ thị nhiệt độ là các que chế từ bột khoáng có nhiệt độ nóng chảy "
        "nhất định và chất kết dính trơ. Sáp đặt trong các giá kim loại điều chỉnh được "
        "có nhãn ghi nhiệt độ định mức; xem Hình 32.80. Giống chất lỏng chỉ thị, có "
        "hơn 100 loại sáp phủ dải 40 °C (100 °F) đến 1371 °C (2500 °F); xem Bảng "
        "32.29. Độ chính xác cũng ±1 % nhiệt độ định mức. Khi nung, gõ nhắc lại chi "
        "tiết bằng sáp. Dưới nhiệt độ định mức, sáp để lại vết khô đục. Khi đạt nhiệt "
        "độ định mức, sáp để lại vết màng lỏng. Khi nguội, vết lỏng đông lại trong suốt "
        "hoặc bán trong suốt. Khoảnh khắc nóng chảy, không phải đổi màu, mới là tín "
        "hiệu nhiệt độ. Sáp dùng trong hàn, rèn, xử lý nhiệt và chế tạo kim loại, ép "
        "cao su và nhựa, bất cứ đâu chi tiết tiếp cận được khi nung. Bề mặt rất nhẵn bị "
        "loại trừ."))
    b.append(H4("Temperature Monitors (Labels)", "Nhãn chỉ thị nhiệt độ (Monitors)"))
    b.append(P(
        "These temperature indicators are adhesive-backed labels with one or more "
        "heat-sensitive indicators under transparent circular windows. The indicators "
        "turn black (show black paper backing) when the rated temperature is reached. "
        "The rated temperatures are from 40 °C (100 °F) to 320 °C (600 °F). They are "
        "available as single temperature or multi-temperature indicators with 10°, 25°, "
        "or 50° steps. The tolerance of the temperature determination is ±1 °C "
        "(±1.8 °F) below 100 °C, and ±1 % of the rated temperature above 100 °C. "
        "Exemplary rated temperatures for a series of 4-temperature (4-dot) indicators "
        "are presented in Table 32.30. A 4-dot temperature monitor is displayed in "
        "Figure 32.81.",
        "Các chất chỉ thị này là nhãn có keo mặt sau với một hoặc nhiều chỉ thị nhạy "
        "nhiệt dưới các cửa sổ tròn trong suốt. Chỉ thị chuyển đen (lộ nền giấy đen) "
        "khi đạt nhiệt độ định mức. Nhiệt độ định mức từ 40 °C (100 °F) đến 320 °C "
        "(600 °F). Có loại đơn nhiệt độ hoặc đa nhiệt độ với bước 10°, 25° hay 50°. "
        "Sai số xác định nhiệt độ là ±1 °C (±1,8 °F) dưới 100 °C, và ±1 % nhiệt độ "
        "định mức trên 100 °C. Nhiệt độ định mức mẫu cho dãy chỉ thị 4-nhiệt-độ (4 "
        "chấm) trình bày trong Bảng 32.30. Nhãn 4 chấm thể hiện ở Hình 32.81."))
    b.append(F81(lang))
    b.append(_t3230(lang))
    b.append(P(
        "How to Use the Materials. After removing the backing, the label is pressed "
        "firmly to the dry and clean workpiece surface. A change in color to black is "
        "the temperature signal. Application of multitemperature-indicating labels "
        "allows more precise temperature determination. They are especially applied "
        "for monitoring the safe operating temperature of equipment and processes, "
        "safeguarding temperature-sensitive materials during storage and transport. "
        "The melting temperature indicators are described in the catalogs of their "
        "manufacturers [3, 4]. As the melting indicators are widely used in the U.S., "
        "temperatures in Fahrenheit are also given.",
        "Cách dùng vật liệu. Sau khi bóc lớp lót, dán chặt nhãn vào bề mặt chi tiết "
        "khô sạch. Sự đổi màu thành đen là tín hiệu nhiệt độ. Dùng nhãn đa nhiệt độ "
        "cho phép xác định nhiệt độ chính xác hơn. Chúng đặc biệt dùng giám sát nhiệt "
        "độ vận hành an toàn của thiết bị và quy trình, bảo vệ vật liệu nhạy nhiệt khi "
        "lưu kho và vận chuyển. Chất chỉ thị nóng chảy được mô tả trong catalog của "
        "nhà sản xuất [3, 4]. Vì chỉ thị nóng chảy dùng phổ biến ở Mỹ nên nhiệt độ "
        "Fahrenheit cũng được cho."))

    # ============================ color-change indicators
    b.append(H3("Color-Change Temperature Indicators",
                "Chất chỉ thị đổi màu theo nhiệt độ"))
    b.append(P(
        "Color-change indicators comprise temperature-indicating paints, crayons, as "
        "well as liquid crystal indicators.",
        "Chất chỉ thị đổi màu gồm sơn, sáp màu chỉ thị nhiệt độ, cũng như chất chỉ thị "
        "tinh thể lỏng."))
    b.append(H4("Temperature-Indicating Paints and Crayons",
                "Sơn và sáp màu chỉ thị nhiệt độ"))
    b.append(P(
        "Temperature-indicating paints are basically acrylic lacquers containing finely "
        "dispersed temperature-sensitive inorganic pigments. The principle of operation "
        "of these indicators draws on the change in color of incident light reflected "
        "from the surface of the paint due to chemical reactions which the dispersed "
        "pigments undergo and creation of new compounds at specific transition "
        "temperatures. The color-change temperatures are also determined by the heating "
        "time. According to the British Standard, it is assumed that the rated "
        "temperatures of the paints correspond to the change in color at a heating "
        "interval of 10 min. To make the characteristics of temperature-indicating "
        "paints complete, the manufacturers also provide, together with the paints, "
        "graphs of trigger temperature vs. heating time relationships. "
        "Temperature-indicating paints and crayons can be divided into two groups: "
        "irreversible indicators, where the change of color becomes permanent; and "
        "reversible indicators, which after cooling and some time revert to previous "
        "colors.",
        "Sơn chỉ thị nhiệt độ về cơ bản là sơn mài acrilic chứa pigment vô cơ nhạy "
        "nhiệt phân tán mịn. Nguyên lý hoạt động dựa trên sự đổi màu của ánh sáng tới "
        "phản chiếu từ bề mặt sơn do các phản ứng hóa học của pigment phân tán và sự "
        "tạo hợp chất mới ở các nhiệt độ chuyển tiếp xác định. Nhiệt độ đổi màu cũng "
        "phụ thuộc thời gian nung. Theo tiêu chuẩn Anh, nhiệt độ định mức của sơn ứng "
        "với đổi màu ở khoảng nung 10 phút. Để đặc tả đầy đủ, nhà sản xuất còn cung "
        "cấp đồ thị nhiệt độ kích hoạt theo thời gian nung. Sơn và sáp màu chỉ thị "
        "nhiệt độ chia hai nhóm: chất chỉ thị không hồi phục (đổi màu vĩnh viễn) và "
        "chất chỉ thị hồi phục (sau nguội và một thời gian trở lại màu cũ)."))
    b.append(H4("Irreversible Color-Change Paints", "Sơn đổi màu không hồi phục"))
    b.append(P(
        "Irreversible color-change indicators are complex compounds containing various "
        "metals, including cobalt, chromium, molybdenum, nickel, copper, vanadium, or "
        "uranium. However, they are lead- and sulfur-free. They are available on the "
        "market in the form of paints and crayons. The irreversible paints can change "
        "color once or several times during the heating process. Thus, another division "
        "can be made on single-change and multichange paints. The range of rated "
        "temperatures is from 40 °C to 1350 °C at 10 to 200 °C steps. At the standard "
        "conditions, the tolerance of measurements is ±5 °C for lower temperature values "
        "and ±1 % for higher temperatures. Exemplary single-change paints with two "
        "critical temperatures — the initial trigger temperature for which the paint "
        "changes color after 10 min heating, and the cut-off temperature being the "
        "lowest temperature for which the color change is achieved for long-duration "
        "heating — are collected in Table 32.31. Color changes and critical temperatures "
        "for some multichange paints (changing color 2, 3, 3 or 6 times throughout the "
        "heating cycle) are presented in Table 32.32.",
        "Chất chỉ thị đổi màu không hồi phục là hợp chất phức tạp chứa nhiều kim loại "
        "như côban, crom, molypđen, niken, đồng, vanadi hay urani. Tuy nhiên, chúng "
        "không chì và không lưu huỳnh. Có dạng sơn và sáp màu. Sơn không hồi phục có "
        "thể đổi màu một hoặc vài lần trong quá trình nung, nên chia thành sơn đổi một "
        "lần và sơn đổi nhiều lần. Dải nhiệt độ định mức từ 40 °C đến 1350 °C với bước "
        "10–200 °C. Ở điều kiện chuẩn, sai số ±5 °C với nhiệt độ thấp và ±1 % với nhiệt "
        "độ cao. Các sơn đổi một lần mẫu với hai nhiệt độ tới hạn — nhiệt độ kích hoạt "
        "ban đầu (đổi màu sau nung 10 phút) và nhiệt độ cắt (nhiệt độ thấp nhất đạt đổi "
        "màu khi nung dài) — tập hợp trong Bảng 32.31. Đổi màu và nhiệt độ tới hạn của "
        "một số sơn đổi nhiều lần (đổi 2, 3, 3 hoặc 6 lần) trình bày trong Bảng 32.32."))
    b.append(_t3231(lang))
    b.append(_t3232(lang))
    b.append(P(
        "How to Use the Materials. A thin layer of the paint is applied to a workpiece "
        "surface by brushing or spraying like an ordinary paint and allowed to dry "
        "before the heating starts. During the heating, when a point of the surface "
        "reaches or exceeds the critical temperature, a color change will take place. "
        "To determine the distribution of temperature, a multichange paint can be "
        "applied. With a nonuniform temperature rise, a number of colored bands "
        "separated by isothermal lines will appear on the workpiece surface, allowing "
        "the thermal record to be made of the temperature gradient across the surface. "
        "The temperature-indicating paints are widely used in industrial applications "
        "for observing heat patterns, detecting high and low temperature points on "
        "surfaces of heat engines, pipelines, and refrigeration fins. They can be also "
        "used for controlling temperatures of powered elements and surfaces that are "
        "inaccessible or revolve at high speeds.",
        "Cách dùng vật liệu. Phủ một lớp mỏng sơn lên bề mặt chi tiết bằng chổi hoặc "
        "phun như sơn thường và để khô trước khi nung. Khi nung, tại điểm bề mặt đạt "
        "hoặc vượt nhiệt độ tới hạn, màu sẽ đổi. Để xác định phân bố nhiệt độ, dùng sơn "
        "đổi nhiều lần. Khi nhiệt độ tăng không đều, các dải màu ngăn bởi đường đẳng "
        "nhiệt xuất hiện trên bề mặt, cho phép ghi lại gradient nhiệt độ trên bề mặt. "
        "Sơn chỉ thị nhiệt độ dùng rộng rãi trong công nghiệp để quan sát hình thái "
        "nhiệt, phát hiện điểm nóng/lạnh trên bề mặt động cơ nhiệt, đường ống và cánh "
        "tản lạnh. Chúng cũng kiểm soát nhiệt độ các phần tử mang điện và bề mặt không "
        "tiếp cận được hoặc quay tốc độ cao."))
    b.append(H4("Color-Change Crayons", "Sáp màu đổi màu"))
    b.append(P(
        "Color-change crayons, available in more than 10 distinct colors, similar in "
        "shape to regular crayons for drawing, cover the temperature range from 65 °C "
        "to 670 °C at 10 to 100 °C temperature intervals. Exemplary single-change "
        "crayons are presented in Table 32.33. The accuracy of the temperature "
        "determination is the same as for the temperature-sensitive paints. They can be "
        "used for evaluating the temperature on already heated surfaces. They change "
        "color 2 min after reaching the rated temperature. Easy to use and inexpensive, "
        "they are invaluable for occasional temperature control in auto repairs, "
        "soldering, welding, electrical wiring, enameling, and for any operation "
        "involving boiling, baking, and other forms of heating.",
        "Sáp màu đổi màu, có hơn 10 màu khác biệt, hình dạng như sáp màu vẽ thông "
        "thường, phủ dải 65–670 °C với bước 10–100 °C. Các sáp đổi một lần mẫu trình "
        "bày trong Bảng 32.33. Độ chính xác xác định nhiệt độ giống sơn nhạy nhiệt. "
        "Chúng dùng đánh giá nhiệt độ trên bề mặt đã nung sẵn, đổi màu 2 phút sau khi "
        "đạt nhiệt độ định mức. Dễ dùng và rẻ, rất hữu ích cho kiểm soát nhiệt độ thỉnh "
        "thoảng trong sửa xe, hàn thiếc, hàn, đi dây điện, tráng men và mọi thao tác "
        "liên quan đun sôi, nướng và các hình thức nung khác."))
    b.append(_t3233(lang))
    b.append(H4("Reversible Color-Change Indicators", "Chất chỉ thị đổi màu hồi phục"))
    b.append(P(
        "Reversible color-change indicators are available on the market as paints and "
        "in label form. The thermal pigments of these temperature indicators are "
        "mercury-based complexes. Therefore, they cannot be applied directly to metal "
        "surfaces as this causes decomposition. They also tend to decompose after long "
        "exposure to heat, but the decomposition can be retarded by using a clear "
        "over-lacquer. The pigments find their most successful application when "
        "encapsulated into labels. The rated temperatures for the reversible "
        "color-change paints do not exceed 170 °C. For temperatures up to 70 °C under "
        "standard conditions, the tolerance of measurements is ±1 °C; for 70 to 150 °C, "
        "±2 °C; and for 150 to 170 °C, ±3 °C.",
        "Chất chỉ thị đổi màu hồi phục có dạng sơn và nhãn. Pigment nhiệt của chúng là "
        "phức hợp based thủy ngân, nên không thể bôi trực tiếp lên bề mặt kim loại vì "
        "gây phân hủy. Chúng cũng có xu hướng phân hủy sau phơi nhiệt lâu, nhưng có "
        "thể làm chậm bằng lớp sơn phủ trong suốt. Pigment phát huy tốt nhất khi được "
        "bao vi nang trong nhãn. Nhiệt độ định mức của sơn đổi màu hồi phục không vượt "
        "170 °C. Dưới 70 °C ở điều kiện chuẩn sai số ±1 °C; 70–150 °C là ±2 °C; "
        "150–170 °C là ±3 °C."))
    b.append(P(
        "How to Use the Materials. A thin layer of a reversible paint is applied to a "
        "workpiece surface by brushing or spraying, or a label is pressed to the "
        "surface. During the heating, a color change will take place when the "
        "temperature of the surface reaches or exceeds the critical temperature. The "
        "reversible color-change paints are widely used in the electrical industry, "
        "especially on busbars, live conductors, and connectors in high-current "
        "switches and in electronic fault-finding. They also find application as "
        "warning and indicating devices of domestic appliances. They are invaluable for "
        "controlling lower temperatures when it is necessary to detect undesirable "
        "temperature excursions, correct faults, and revert to normal conditions.",
        "Cách dùng vật liệu. Phủ lớp mỏng sơn hồi phục lên bề mặt chi tiết bằng chổi "
        "hoặc phun, hoặc dán nhãn vào bề mặt. Khi nung, màu đổi khi nhiệt độ bề mặt đạt "
        "hoặc vượt nhiệt độ tới hạn. Sơn đổi màu hồi phục dùng rộng rãi trong công "
        "nghiệp điện, đặc biệt trên thanh cái, dây dẫn mang điện và đầu nối trong công "
        "tắc dòng lớn, cũng như tìm lỗi điện tử. Chúng cũng là thiết bị cảnh báo và chỉ "
        "thị trong đồ gia dụng, rất quý để kiểm soát nhiệt độ thấp khi cần phát hiện "
        "những vượt nhiệt không mong muốn, sửa lỗi và trở về trạng thái bình thường."))

    # ============================ thermochromic liquid crystals
    b.append(H4("Thermochromic Liquid Crystals", "Tinh thể lỏng nhiệt sắc"))
    b.append(P(
        "Liquid crystals constitute a class of matter unique in exhibiting mechanical "
        "properties of liquids (fluidity and surface tension) and optical properties "
        "of solids (anisotropy to light, birefringence). Certain liquid crystals are "
        "thermochromic and react to changes in temperature by changing color. They can "
        "be painted on a surface or suspended in a fluid and used to make the "
        "distribution of temperature visible. Normally clear, or slightly milky in "
        "appearance, liquid crystals change in appearance over a narrow range of "
        "temperatures called the color-play bandwidth (the temperature interval "
        "between first red and last blue), centered around the nominal event "
        "temperature (midgreen temperature). The displayed color is red at the low "
        "temperature margin of the color-play interval and blue at the high end. Within "
        "the color-play interval, the colors range smoothly from red to blue as a "
        "function of temperature; see Figure 32.82. Liquid crystals or mesophases have "
        "been classified as smectic, chiral nematic, cholesteric, and blue. The "
        "structure of liquid crystals is shown schematically in Figure 32.83.",
        "Tinh thể lỏng là một dạng vật chất độc đáo với tính chất cơ học của chất lỏng "
        "(trôi chảy, sức căng bề mặt) và tính chất quang học của chất rắn (dị hướng "
        "ánh sáng, lưỡng chiết). Một số tinh thể lỏng nhiệt sắc phản ứng với đổi nhiệt "
        "độ bằng cách đổi màu. Chúng có thể sơn lên bề mặt hoặc lơ lửng trong chất lưu "
        "để làm hiển thị phân bố nhiệt độ. Thường trong suốt hoặc hơi đục sữa, tinh thể "
        "lỏng đổi trạng thái trong một dải nhiệt hẹp gọi là băng thông dải màu (khoảng "
        "nhiệt độ từ đỏ đầu đến xanh cuối), lấy tâm là nhiệt độ sự kiện danh định (nhiệt "
        "độ xanh lục giữa). Màu hiển thị đỏ ở mé thấp và xanh ở mé cao của dải. Trong "
        "dải, màu chuyển mượt từ đỏ sang xanh theo nhiệt độ; xem Hình 32.82. Tinh thể "
        "lỏng hay mesophase được phân loại thành smectic, nematic chirality, "
        "cholesteric và blue. Cấu trúc tinh thể lỏng thể hiện sơ đồ ở Hình 32.83."))
    b.append(F82(lang))
    b.append(F83(lang))
    b.append(H4("Temperature-Sensitive and Shear-Sensitive Formulations",
                "Công thức nhạy cảm với nhiệt độ và trượt"))
    b.append(P(
        "Temperature-sensitive liquid crystals show colors by selectively reflecting "
        "incident white light. Conventional temperature-sensitive mixtures turn from "
        "colorless (or black against a black background) to red at a given temperature "
        "and, as the temperature is increased, pass smoothly through the other colors "
        "of the visible spectrum in sequence (orange, yellow, green, blue, violet) "
        "before turning colorless (or black) again in the ultraviolet at a higher "
        "temperature. The color changes are reversible and on cooling the color change "
        "sequence is reversed. Temperature-insensitive (sometimes called "
        "shear-sensitive) formulations can also be made. These mixtures show just a "
        "single color below a given transition temperature (called the clearing point) "
        "and change to colorless (black) above it. The working temperature range is "
        "thus below the clearing point. Both reversible and hysteretic (memory) "
        "formulations can be made. All liquid crystal mixtures should be viewed against "
        "non-reflecting backgrounds (ideally black, totally absorbing) for best "
        "visualization of the colors.",
        "Tinh thể lỏng nhạy nhiệt tạo màu bằng phản chiếu có chọn lọc ánh sáng trắng "
        "tới. Các hỗn hợp nhạy nhiệt thông thường chuyển từ không màu (hay đen trên nền "
        "đen) sang đỏ ở một nhiệt độ cho trước và, khi tăng nhiệt, đi mượt qua các màu "
        "khác của phổ nhìn thấy theo thứ tự (cam, vàng, xanh lục, xanh lam, tím) trước "
        "khi trở lại không màu (hay đen) ở vùng tử ngoại ở nhiệt độ cao hơn. Đổi màu "
        "hồi phục và khi nguội trình tự ngược lại. Cũng có thể làm công thức không nhạy "
        "nhiệt (thỉnh thoảng gọi là nhạy trượt): chỉ một màu dưới nhiệt độ chuyển tiếp "
        "(điểm tách) và chuyển không màu (đen) ở trên. Vì vậy dải làm việc nằm dưới điểm "
        "tách. Cả công thức hồi phục và trễ (bộ nhớ) đều làm được. Mọi hỗn hợp tinh thể "
        "lỏng nên quan sát trên nền không phản xạ (tốt nhất là đen, hấp thụ hoàn toàn) "
        "để thấy màu tốt nhất."))
    b.append(H4("Color-Play Properties and Resolution",
                "Đặc tính dải màu và độ phân giải"))
    b.append(P(
        "Temperature-sensitive thermochromic mixtures have a characteristic red start "
        "or midgreen temperature and color-play bandwidth. The bandwidth is defined as "
        "the blue start temperature minus the red start temperature. The color play is "
        "defined by specifying either the red start or midgreen temperature and the "
        "bandwidth. For example, R35C1W describes a liquid crystal with a red start at "
        "35 °C and a bandwidth of 1 °C, i.e., a blue start 1 °C higher, at 36 °C; "
        "G100F2W describes a liquid crystal with a midgreen temperature at 100 °F and a "
        "bandwidth of 2 °F. Both the color-play bandwidth and the event temperature of "
        "a liquid crystal can be selected by its proper chemical composition. The event "
        "temperatures of liquid crystals range from −30 °C to 115 °C with color-play "
        "bands from 0.5 °C to 20 °C, although not all combinations of event temperature "
        "and color-play bandwidth are available. Liquid crystals with color-play "
        "bandwidths of 1 °C or less are called narrow-band materials, while those whose "
        "bandwidth exceeds 5 °C are referred to as wide-band. The type of material to be "
        "specified for temperature indicating should depend very much on the type of "
        "available image interpretation technique — human observers, intensity-based "
        "image processing, or true-color image processing systems (see [7]). The "
        "uncertainty associated with direct visual inspection is about 1/3 the "
        "color-play bandwidth, given an observer with normal color vision — about "
        "±0.2 °C to 0.5 °C. The uncertainty of true-color image processing interpreters "
        "using wide-band liquid crystals is of the same order as the uncertainty "
        "assigned to human observers using narrow-band materials, and depends on the "
        "pixel-to-pixel uniformity of the applied paint and the size of the area "
        "averaged by the interpreter (about ±0.05 °C can be achieved). Using a "
        "multiply filtered, intensity-based system, the resolution is better than "
        "±0.1 °C.",
        "Hỗn hợp nhiệt sắc nhạy nhiệt có nhiệt độ đỏ đầu hay xanh lục giữa và băng "
        "thông dải màu đặc trưng. Băng thông định nghĩa bằng nhiệt độ xanh đầu trừ nhiệt "
        "độ đỏ đầu. Dải màu định nghĩa bởi nhiệt độ đỏ đầu hoặc xanh lục giữa cùng băng "
        "thông. Ví dụ, R35C1W chỉ tinh thể lỏng có đỏ đầu ở 35 °C và băng thông 1 °C, "
        "tức xanh đầu cao hơn 1 °C, ở 36 °C; G100F2W chỉ tinh thể có xanh lục giữa ở "
        "100 °F và băng thông 2 °F. Cả băng thông dải màu và nhiệt độ sự kiện của tinh "
        "thể lỏng đều chọn được bằng thành phần hóa học phù hợp. Nhiệt độ sự kiện từ "
        "−30 °C đến 115 °C với dải 0,5–20 °C, dù không mọi tổ hợp đều có sẵn. Tinh thể "
        "lỏng có băng thông ≤1 °C gọi là vật liệu dải hẹp; >5 °C gọi là dải rộng. Loại "
        "vật liệu chọn cho chỉ thị nhiệt phụ thuộc nhiều vào kỹ thuật giải ảnh — quan "
        "sát mắt người, xử lý ảnh theo cường độ hay theo màu thực (xem [7]). Độ không "
        "đắc quan sát trực tiếp khoảng 1/3 băng thông dải màu với người có thị lực màu "
        "bình thường — khoảng ±0,2–0,5 °C. Độ không đắc của hệ giải ảnh màu thực dùng "
        "tinh thể dải rộng cùng bậc với người quan sát dùng vật liệu dải hẹp, và phụ "
        "thuộc tính đồng nhất pixel của sơn và kích thước vùng trung bình (có thể đạt "
        "±0,05 °C). Dùng hệ lọc kép theo cường độ, độ phân giải tốt hơn ±0,1 °C."))
    b.append(P(
        "How to Use the Materials. Liquid-crystal indicators can be used in a number "
        "of different forms: as unsealed liquids (also in solutions), in the "
        "microencapsulated form (as aqueous slurries or coating formulations), and as "
        "coated (printed) sheets. The different forms of the materials have selective "
        "advantages and suit different temperatures and flow visualization "
        "applications. Individual products are described in more detail in relevant "
        "booklets issued by the manufacturers of liquid crystals [5, 6]. Typical "
        "Application. Liquid-crystal indicators are ideal for monitoring temperatures "
        "of electronic parts, transformers, relays, and motors. They are invaluable for "
        "a fast visual indication of temperatures.",
        "Cách dùng vật liệu. Chất chỉ thị tinh thể lỏng dùng nhiều dạng: chất lỏng không "
        "bao kín (cả trong dung dịch), dạng vi nang (hồ nước hoặc chế phẩm phủ), và dạng "
        "tấm phủ (in). Các dạng có ưu điểm riêng và thích ứng nhiệt độ và trực quan hóa "
        "dòng chảy khác nhau. Sản phẩm cụ thể mô tả chi tiết trong các tài liệu của nhà "
        "sản xuất tinh thể lỏng [5, 6]. Ứng dụng điển hình: chất chỉ thị tinh thể lỏng "
        "lý tưởng giám sát nhiệt độ linh kiện điện tử, máy biến áp, rơle và động cơ; "
        "rất quý cho chỉ thị trực quan nhanh các nhiệt độ."))

    b.append(refs(lang))
    return "".join(b)


def sec_vi():
    return _section("vi")


def sec_en():
    return _section("en")
