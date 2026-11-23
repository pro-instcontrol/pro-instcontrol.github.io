# -*- coding: utf-8 -*-
"""Sections 15.1-15.4 — Length / Whole-inch / Fractional-inch equivalents."""
from cvh15_common import T, H, P, LEAD, B, N, TB

# ---------------------------------------------------------------------------
# 15.1 — Length Equivalents.  Row label first, then the six printed columns.
# NOTE: the printed source spells the last row label "Killometers"; it is
# retained verbatim below (see the OCR note rendered in section()).
_LEN_HDR_VI = ["Đơn vị", "Meters", "Inches", "Feet", "Millimeters",
               "Miles", "Kilometers"]
_LEN_HDR_EN = ["Unit", "Meters", "Inches", "Feet", "Millimeters",
               "Miles", "Kilometers"]
_LEN_ROWS = [
    ("Meters",     "1",       "39.37",  "3.2808",  "1000",      "0.0006214",  "0.001"),
    ("Inches",     "0.0254",  "1",      "0.0833",  "25.4",      "0.00001578", "0.0000254"),
    ("Feet",       "0.3048",  "12",     "1",       "304.8",     "0.0001894",  "0.0003048"),
    ("Millimeters","0.001",   "0.03937","0.0032808","1",        "0.0000006214","0.000001"),
    ("Miles",      "1609.35", "63,360", "5,280",   "1,609,350", "1",          "1.60935"),
    ("Killometers","1,000",   "39,370", "3280.83", "1,000,000", "0.62137",    "1"),
]

# ---------------------------------------------------------------------------
# 15.2 — Whole Inch to Millimeter Equivalents.  Header: super-label "Inch"
# over the column numbers 0..9; row labels are 0,10,...,100.
_WHOLE_HDR_VI = ["Inch / Inch", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
_WHOLE_HDR_EN = ["Inch / Inch", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
_WHOLE_ROWS = [
    ("0",   "0.0",    "25.4",   "50.8",   "76.2",   "101.6",  "127.0",  "152.4",  "177.8",  "203.2",  "228.6"),
    ("10",  "254.0",  "279.4",  "304.8",  "330.2",  "355.6",  "381.0",  "406.4",  "431.8",  "457.2",  "482.6"),
    ("20",  "508.0",  "533.4",  "558.8",  "584.2",  "609.6",  "635.0",  "660.4",  "685.8",  "711.2",  "736.6"),
    ("30",  "762.0",  "787.4",  "812.8",  "838.2",  "863.6",  "889.0",  "914.4",  "939.8",  "965.2",  "990.6"),
    ("40",  "1016.0", "1041.4", "1066.8", "1092.2", "1117.6", "1143.0", "1168.4", "1193.8", "1219.2", "1244.6"),
    ("50",  "1270.0", "1295.4", "1320.8", "1346.2", "1371.6", "1397.0", "1422.4", "1447.8", "1473.2", "1498.6"),
    ("60",  "1524.0", "1549.4", "1574.8", "1600.2", "1625.6", "1651.0", "1676.4", "1701.8", "1727.2", "1752.6"),
    ("70",  "1778.0", "1803.4", "1828.8", "1854.2", "1879.6", "1905.0", "1930.4", "1955.8", "1981.2", "2006.6"),
    ("80",  "2032.0", "2057.4", "2082.8", "2108.2", "2133.6", "2159.0", "2184.4", "2209.8", "2235.2", "2260.6"),
    ("90",  "2286.0", "2311.4", "2336.8", "2362.2", "2387.6", "2413.0", "2438.4", "2463.8", "2489.2", "2514.6"),
    ("100", "2540.0", "2565.4", "2590.8", "2616.2", "2641.6", "2667.0", "2692.4", "2717.8", "2743.2", "2768.6"),
]

# ---------------------------------------------------------------------------
# 15.3 — Fractional Inch to Millimeter Equivalents, two side-by-side grids.
_FRAC1_HDR_VI = ["Inch / Inch", "0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16"]
_FRAC1_HDR_EN = ["Inch / Inch", "0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16"]
_FRAC1_ROWS = [
    ("0",  "0.0",   "1.6",   "3.2",   "4.8",   "6.4",   "7.9",   "9.5",   "11.1"),
    ("1",  "25.4",  "27.0",  "28.6",  "30.2",  "31.8",  "33.3",  "34.9",  "36.5"),
    ("2",  "50.8",  "52.4",  "54.0",  "55.6",  "57.2",  "58.7",  "60.3",  "61.9"),
    ("3",  "76.2",  "77.8",  "79.4",  "81.0",  "82.6",  "84.1",  "85.7",  "87.3"),
    ("4",  "101.6", "103.2", "104.8", "106.4", "108.0", "109.5", "111.1", "112.7"),
    ("5",  "127.0", "128.6", "130.2", "131.8", "133.4", "134.9", "136.5", "138.1"),
    ("6",  "152.4", "154.0", "155.6", "157.2", "158.8", "160.3", "161.9", "163.5"),
    ("7",  "177.8", "179.4", "181.0", "182.6", "184.2", "185.7", "187.3", "188.9"),
    ("8",  "203.2", "204.8", "206.4", "208.0", "209.6", "211.1", "212.7", "214.3"),
    ("9",  "228.6", "230.2", "231.8", "233.4", "235.0", "236.5", "238.1", "239.7"),
    ("10", "254.0", "255.6", "257.2", "258.8", "260.4", "261.9", "263.5", "265.1"),
]
_FRAC2_HDR_VI = ["Inch / Inch", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"]
_FRAC2_HDR_EN = ["Inch / Inch", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"]
_FRAC2_ROWS = [
    ("0",  "12.7",  "14.3",  "15.9",  "17.5",  "19.1",  "20.6",  "22.2",  "23.8"),
    ("1",  "38.1",  "39.7",  "41.3",  "42.9",  "44.5",  "46.0",  "47.6",  "49.2"),
    ("2",  "63.5",  "65.1",  "66.7",  "68.3",  "69.9",  "71.4",  "73.0",  "74.6"),
    ("3",  "88.9",  "90.5",  "92.1",  "93.7",  "95.3",  "96.8",  "98.4",  "100.0"),
    ("4",  "114.3", "115.9", "117.5", "119.1", "120.7", "122.2", "123.8", "125.4"),
    ("5",  "139.7", "141.3", "142.9", "144.5", "146.1", "147.6", "149.2", "150.8"),
    ("6",  "165.1", "166.7", "168.3", "169.9", "171.5", "173.0", "174.6", "176.2"),
    ("7",  "190.5", "192.1", "193.7", "195.3", "196.9", "198.4", "200.0", "201.6"),
    ("8",  "215.9", "217.5", "219.1", "220.7", "222.3", "223.8", "225.4", "227.0"),
    ("9",  "241.3", "242.9", "244.5", "246.1", "247.7", "249.2", "250.8", "252.4"),
    ("10", "266.7", "268.3", "269.9", "271.5", "273.1", "274.6", "276.2", "277.8"),
]

# ---------------------------------------------------------------------------
# 15.4 — Additional Fractional Inch to Millimeter Equivalents.  Six printed
# columns, in three (Inches, Millimeters) groups; each fraction token is
# followed in the print by its decimal-inch equivalent, which shares the
# cell.  Source lines are kept verbatim and split into table cells below.
_ADD_FRAC_HDR_VI = [
    "Inches / Phân số", "Millimeters / Thập phân",
    "Inches / Phân số", "Millimeters / Thập phân",
    "Inches / Phân số", "Millimeters / Thập phân",
]
_ADD_FRAC_HDR_EN = [
    "Inches / Fractions", "Millimeters / Decimals",
    "Inches / Fractions", "Millimeters / Decimals",
    "Inches / Fractions", "Millimeters / Decimals",
]

_ADD_FRAC_LINES_1 = [
    ".00394 .1 .2 5.08 .44 11.176",
    ".00787 .2 13/64 .203125 5.1594 .45 11.430",
    ".01 .254 .21 5.334 29/64 .453125 11.5094",
    ".01181 .3 7/32 .21875 5.5562 .46 11.684",
    "1/64 .015625 .3969 .22 5.588 15/32 .46875 11.9062",
    ".01575 .4 .23 5.842 .47 11.938",
    ".01969 .5 15/64 .234375 5.9531 .47244 12.0",
    ".02 .508 .23622 6.0 .48 12.192",
    ".02362 .6 .24 6.096 31/64 .484375 12.3031",
    ".02756 .7 1/4 .25 6.35 .49 12.446",
    ".03 .762 .26 6.604 1/2 .50 12.7",
    "1/32 .03125 .7938 17/64 .265625 6.7469 .51 12.954",
    ".0315 .8 .27 6.858 .51181 13.0",
    ".03543 .9 .27559 7.0 33/64 .515625 13.0969",
    ".03937 1.0 .28 7.112 .52 13.208",
    ".04 1.016 9/32 .28125 7.1438 .53 13.462",
    "3/64 .046875 1.1906 .29 7.366 17/32 .53125 13.4938",
    ".05 1.27 19/64 .296875 7.5406 .54 13.716",
    ".06 1.524 .30 7.62 35/64 .546875 13.8906",
    "1/16 .0625 1.5875 .31 7.874 .55 13.970",
    ".07 1.778 5/16 .3125 7.9375 .55118 14.0",
    "5/64 .078125 1.9844 .31496 8.0 .56 14.224",
    ".07874 2.0 .32 8.128 9/16 .5625 14.2875",
    ".08 2.032 21/64 .328125 8.3344 .57 14.478",
    ".09 2.286 .33 8.382 37/64 .578125 14.6844",
    "3/32 .09375 2.3812 .34 8.636 .58 14.732",
    ".1 2.54 11/32 .34375 8.7312 .59 14.986",
    "7/64 .109375 2.7781 .35 8.89 .59055 15.0",
    ".11 2.794 .35433 9.0 19/32 .59375 15.0812",
    ".11811 3.0 23/64 .359375 9.1281 .60 15.24",
    ".12 3.048 .36 9.144 39/64 .609375 15.4781",
    "1/8 .125 3.175 .37 9.398 .61 15.494",
    ".13 3.302 3/8 .375 9.525 .62 15.748",
    ".14 3.556 .38 9.652 5/8 .625 15.875",
    "9/64 .140625 3.5719 .39 9.906 .62992 16.0",
]
_ADD_FRAC_LINES_2 = [
    ".15 3.810 25/64 .390625 9.9219 .63 16.002",
    "5/32 .15625 3.9688 .39370 10.0 .64 16.256",
    ".15748 4.0 .40 10.16 41/64 .640625 16.2719",
    ".16 4.064 13/32 .40625 10.3188 .65 16.510",
    ".17 4.318 .41 10.414 21/32 .65625 16.6688",
    "11/64 .171875 4.3656 .42 10.668 .66 16.764",
    ".18 4.572 27/64 .421875 10.7156 .66929 17.0",
    "3/16 .1875 4.7625 .43 10.922 .67 17.018",
    ".19 4.826 .43307 11.0 43/64 .671875 17.0656",
    ".19685 5.0 7/16 .4375 11.1125 .68 17.272",
    "11/16 .6875 17.4625 51/64 .796875 20.2406 .90551 23.0",
    ".69 17.526 .80 20.320 29/32 .90625 23.0188",
    ".70 17.78 .81 20.574 .91 23.114",
    "45/64 .703125 17.8594 13/16 .8125 20.6375 .92 23.368",
    ".70866 18.0 .82 20.828 59/64 .921875 23.4156",
    ".71 18.034 .82677 21.0 .93 23.622",
    "23/32 .71875 18.2562 53/64 .828125 21.0344 15/16 .9375 23.8125",
    ".72 18.288 .83 21.082 .94 23.876",
    ".73 18.542 .84 21.336 .94488 24.0",
    "47/64 .734375 18.6531 27/32 .84375 21.4312 .95 24.130",
    ".74 18.796 .85 21.590 61/64 .953125 24.2094",
    ".74803 19.0 55/64 .859375 21.8281 .96 24.384",
    "3/4 .75 19.050 .86 21.844 31/32 .96875 24.6062",
    ".76 19.304 .86614 22.0 .97 24.638",
    "49/64 .765625 19.4469 .87 22.098 .98 24.892",
    ".77 19.558 7/8 .875 22.225 .98425 25.0",
    ".78 19.812 .88 22.352 63/64 .984375 25.0031",
    "25/32 .78125 19.8438 .89 22.606 .99 25.146",
    ".78740 20.0 57/64 .890625 22.6219",
    "1 1.00000 25.4000",
    ".79 20.066 .90 22.860",
]


def _cells(line):
    """Split one verbatim source line into table cells.

    In the printed 15.4 a fraction is immediately followed by its decimal
    inch equivalent in the same cell; keep those two tokens together.
    """
    toks = line.split()
    out = []
    i = 0
    while i < len(toks):
        if "/" in toks[i] and i + 1 < len(toks):
            out.append(toks[i] + " " + toks[i + 1])
            i += 2
        else:
            out.append(toks[i])
            i += 1
    return tuple(out)


_ADD_FRAC_ROWS_1 = [_cells(_line) for _line in _ADD_FRAC_LINES_1]
_ADD_FRAC_ROWS_2 = [_cells(_line) for _line in _ADD_FRAC_LINES_2]


def section(lang):
    b = []

    # ---- 15.1 ------------------------------------------------------------
    b.append(H("15.1 Tương đương chiều dài",
               "15.1 Length Equivalents", lang))
    b.append(N("Lưu ý: Dùng hệ số nhân tại giao điểm của hàng và cột.",
               "Note: Use the multiplier at the convergence of the row and the column.",
               lang))
    b.append(TB(_LEN_HDR_VI, _LEN_HDR_EN, _LEN_ROWS, lang,
                cap_vi="Bảng 15.1 · Ma trận hệ số chuyển đổi đơn vị chiều dài.",
                cap_en="Table 15.1 · Length conversion-factor matrix."))
    b.append(P("Tương đương chiều dài: 1 meter = 100 centimeters = 1000 millimeters "
               "= 0.001 kilometers = 1,000,000 micrometers",
               "Length equivalents: 1 meter = 100 centimeters = 1000 millimeters "
               "= 0.001 kilometers = 1,000,000 micrometers", lang))
    b.append(P("Để đổi đơn vị hệ mét, chỉ cần dịch dấu thập phân: "
               "1 millimeter = 1000 microns = 0.03937 inches = 39.37 mils.",
               "To convert metric units, merely adjust the decimal point: "
               "1 millimeter = 1000 microns = 0.03937 inches = 39.37 mils.", lang))
    b.append(N("Ghi chú về bản in: bản gốc viết “Killometers” và “convergemce”; "
               "nhãn hàng “Killometers” được giữ nguyên, còn “convergemce” được đọc là "
               "“convergence” ở ghi chú trên.",
               "Note on the printed source: the original spells “Killometers” and "
               "“convergemce”; the row label “Killometers” is retained verbatim, and "
               "“convergemce” is rendered as “convergence” in the note above.", lang))

    # ---- 15.2 ------------------------------------------------------------
    b.append(H("15.2 Tương đương inch nguyên sang milimét",
               "15.2 Whole Inch to Millimeter Equivalents", lang))
    b.append(TB(_WHOLE_HDR_VI, _WHOLE_HDR_EN, _WHOLE_ROWS, lang,
                cap_vi="Bảng 15.2 · Tương đương giữa inch nguyên và milimét.",
                cap_en="Table 15.2 · Whole inch to millimeter equivalents."))
    b.append(N("Lưu ý: Tất cả giá trị trong bảng này đều chính xác, dựa trên hệ thức "
               "1 in = 25.4 mm. Bằng cách dịch dấu thập phân, mọi giá trị thập phân hay "
               "bội số của inch đều có thể chuyển sang giá trị tương đương chính xác "
               "bằng milimét.",
               "Note: All values in this table are exact, based on the relation "
               "1 in = 25.4 mm. By manipulation of the decimal point any decimal value "
               "or multiple of an inch may be converted to its exact equivalent in "
               "millimeters.", lang))

    # ---- 15.3 ------------------------------------------------------------
    b.append(H("15.3 Tương đương inch phân số sang milimét",
               "15.3 Fractional Inch to Millimeter Equivalents", lang))
    b.append(TB(_FRAC1_HDR_VI, _FRAC1_HDR_EN, _FRAC1_ROWS, lang,
                cap_vi="Bảng 15.3 · Tương đương inch phân số (0 đến 7/16) sang milimét.",
                cap_en="Table 15.3 · Fractional inch (0 to 7/16) to millimeter equivalents."))
    b.append(P("Tương đương: 1 inch = 25.4 Millimeters",
               "Equivalent: 1 inch = 25.4 Millimeters", lang))
    b.append(P("Tiếp theo: Tương đương inch phân số sang milimét...",
               "Fractional Inch to Millimeter Equivalents continued...", lang))
    b.append(TB(_FRAC2_HDR_VI, _FRAC2_HDR_EN, _FRAC2_ROWS, lang,
                cap_vi="Bảng 15.4 · Tương đương inch phân số (1/2 đến 15/16) sang milimét.",
                cap_en="Table 15.4 · Fractional inch (1/2 to 15/16) to millimeter equivalents."))
    b.append(P("Tương đương: 1 inch = 25.4 Millimeters",
               "Equivalent: 1 inch = 25.4 Millimeters", lang))

    # ---- 15.4 ------------------------------------------------------------
    b.append(H("15.4 Bảng bổ sung: tương đương inch phân số sang milimét",
               "15.4 Additional Fractional Inch to Millimeter Equivalents", lang))
    b.append(TB(_ADD_FRAC_HDR_VI, _ADD_FRAC_HDR_EN, _ADD_FRAC_ROWS_1, lang,
                cap_vi="Bảng 15.5 · Bảng bổ sung tương đương inch phân số sang milimét.",
                cap_en="Table 15.5 · Additional fractional inch to millimeter equivalents."))
    b.append(P("Tiếp theo: Bảng bổ sung tương đương inch phân số sang milimét...",
               "Additional Fractional Inch to Millimeter Equivalents continued...", lang))
    b.append(TB(_ADD_FRAC_HDR_VI, _ADD_FRAC_HDR_EN, _ADD_FRAC_ROWS_2, lang,
                cap_vi="Bảng 15.6 · Bảng bổ sung tương đương inch phân số sang milimét (tiếp theo).",
                cap_en="Table 15.6 · Additional fractional inch to millimeter equivalents (continued)."))
    b.append(P("Làm tròn các chữ số thập phân để độ chính xác không vượt quá mức mong muốn.",
               "Round off decimal points to provide no more than the desired degree of accuracy.",
               lang))

    return "".join(b)
