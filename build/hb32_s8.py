# -*- coding: utf-8 -*-
"""§32.8 Liquid-in-Glass Thermometers — J.V. Nicholas, p117-129."""
import math as _m
import hb32kit as K
R = K.R                      # lazy proxy to reader_hb_ch32 helpers

TITLE_EN = "Liquid-in-Glass Thermometers"
TITLE_VI = "Nhiệt kế chất lỏng trong thủy tinh"

# Flat (English, Vietnamese, depth) tuples — depth 0 -> h3, 1 -> h4.
# The English strings are exactly those passed to the headings; sec_index()
# builds the TOC links from #s32-8-<slug(english)>, so spelling must match.
SUBS = [
    ("General Description", "Mô tả chung", 0),
    ("Liquid Expansion", "Sự giãn nở của chất lỏng", 0),
    ("Time-Constant Effects", "Các hiệu ứng hằng số thời gian", 0),
    ("Thermal Capacity Effects", "Các hiệu ứng nhiệt dung", 0),
    ("Separated Columns", "Cột chất lỏng bị đứt gãy", 0),
    ("Immersion Errors", "Sai số do ngâm", 0),
    ("Organic Liquids", "Chất lỏng hữu cơ", 0),
    ("Storage", "Bảo quản", 0),
    ("High Accuracy", "Độ chính xác cao", 0),
]


# ---------------------------------------------------------------- references
def refs(lang):
    vi = (lang == "vi")
    items = [
        "1. ISO issue documentary standards related to the liquid-in-glass thermometer: "
        "ISO 386-1977 Liquid-in-glass laboratory thermometer — Principles of design, "
        "construction and use; ISO 651-1975 Solid-stem calorimeter thermometers; "
        "ISO 653-1980 Long solid-stem thermometers for precision use; ISO 654-1980 Short "
        "solid-stem thermometers for precision use; ISO 1770-1981 Solid-stem general "
        "purpose thermometer.",
        "2. ASTM in their standards on Temperature Measurement, Vol. 14.03 include two "
        "standards related to liquid-in-glass thermometers: E1-95 Specification for ASTM "
        "Thermometers; E77-92 Test Method for Inspection and Verification of Liquid-in-glass "
        "Thermometers.",
        "3. BSI publish a series of documentary specifications for thermometers, including: "
        "BS 593:1989 Laboratory Thermometers; BS 791:1990 Thermometers for Bomb "
        "Calorimeters; BS 1704:1985 General Thermometers; BS 1900:1976 Secondary "
        "Reference Thermometers.",
        "4. J. A. Wise, Liquid-in-glass Thermometer Calibration Service, Natl. Inst. Stand. "
        "Technol. Spec. Publ., 250-23, 1988. A good treatment of calibration practice for "
        "liquid-in-glass thermometers, with a wider coverage than given here.",
        "5. J. V. Nicholas and D. R. White, Traceable Temperatures, Chichester: John Wiley "
        "& Sons, 1990. The present chapter section was extracted and adapted from this text. "
        "The text explains how to make traceable calibrations of various temperature "
        "sensors to meet international requirements.",
    ]
    head_ = ('<h3 id="t32-tltk-8">Tài liệu tham khảo</h3>' if vi else
             '<h3 id="t32-tltk-8">References</h3>')
    return head_ + R.wl(items)


# ------------------------------------------------------------- where clauses
# (English items, Vietnamese items) keyed by equation number.
_W = {
"32.131": (["where &nbsp;<i>V</i><sub>0</sub> = volume of mercury at 0&deg;C",
            "&nbsp;<i>a</i> and <i>b</i> = coefficients of thermal expansion of mercury, "
            "with <i>a</i> = 1.8&middot;10<sup>&minus;4</sup> &deg;C<sup>&minus;1</sup> and "
            "<i>b</i> = 5&middot;10<sup>&minus;8</sup> &deg;C<sup>&minus;2</sup>"],
           ["trong đó &nbsp;<i>V</i><sub>0</sub> = thể tích thủy ngân ở 0&deg;C",
            "&nbsp;<i>a</i> và <i>b</i> = các hệ số giãn nở nhiệt của thủy ngân, với "
            "<i>a</i> = 1,8&middot;10<sup>&minus;4</sup> &deg;C<sup>&minus;1</sup> và "
            "<i>b</i> = 5&middot;10<sup>&minus;8</sup> &deg;C<sup>&minus;2</sup>"]),
"32.132": (["where &nbsp;<i>t</i><sub>i</sub> = indicated temperature",
            "&nbsp;<i>N</i> = length of emergent column expressed in degrees, as determined "
            "by the thermometer scale",
            "&nbsp;<i>t</i><sub>2</sub> = mean temperature of the emergent column when "
            "calibrated (i.e., the stem temperature on a certificate for partial immersion "
            "or the thermometer reading for a total-immersion certificate)",
            "&nbsp;<i>t</i><sub>1</sub> = mean temperature of the emergent column in use",
            "&nbsp;<i>k</i> = coefficient of apparent expansion of the thermometric liquid "
            "used in the glass of which the thermometer stem is made"],
           ["trong đó &nbsp;<i>t</i><sub>i</sub> = nhiệt độ chỉ thị",
            "&nbsp;<i>N</i> = chiều dài cột nổi tính bằng độ, xác định theo thang đo của nhiệt kế",
            "&nbsp;<i>t</i><sub>2</sub> = nhiệt độ trung bình của cột nổi khi hiệu chuẩn "
            "(tức là nhiệt độ thân trên giấy chứng nhận đối với ngâm một phần, hoặc số đọc "
            "nhiệt kế đối với giấy chứng nhận ngâm toàn phần)",
            "&nbsp;<i>t</i><sub>1</sub> = nhiệt độ trung bình của cột nổi khi sử dụng",
            "&nbsp;<i>k</i> = hệ số giãn nở biểu kiến của chất lỏng nhiệt kế dùng trong "
            "loại thủy tinh làm thân nhiệt kế"]),
}


# ------------------------------------------------------------------- helpers
class _Box(object):
    """Pixel mapping identical to hbfig.Box with K.chart's default pad, so
    `extra` annotations can be placed in data coordinates."""
    def __init__(self, W, H, xr, yr, pad=(56, 20, 18, 42)):
        l, t, r, b = pad
        self.l, self.t = l, t
        self.pw, self.ph = W - l - r, H - t - b
        self.x0, self.x1 = xr
        self.y0, self.y1 = yr

    def x(self, v):
        return self.l + (v - self.x0) * self.pw / (self.x1 - self.x0)

    def y(self, v):
        return self.t + self.ph - (v - self.y0) * self.ph / (self.y1 - self.y0)


# num -> (cap_vi, cap_en, aria_vi, aria_en, title_vi)
_CAP = {
70: ("Hình 32.70 · Các đặc điểm chính của nhiệt kế thủy tinh thân đặc. Nhiệt kế có thể có một "
     "sự phình ở thân hoặc một bộ phận gắn ở đầu thân để hỗ trợ định vị. Các nhiệt kế sẽ có một "
     "số đặc điểm này, nhưng hiếm khi có tất cả.",
     "Figure 32.70 · The main features of a solid-stem glass thermometer. The thermometer can "
     "have an enlargement in the stem or an attachment at the end of the stem to assist in the "
     "positioning of the thermometer. Thermometers will display several of these features, but "
     "seldom all of them.",
     "Sơ đồ nhiệt kế thủy tinh thân đặc với bầu, thân mao quản, cột thủy ngân, thang chia và "
     "buồng giãn nở",
     "Diagram of a solid-stem glass thermometer with bulb, capillary stem, mercury column, "
     "scale and expansion chamber",
     "Các đặc điểm chính của nhiệt kế thân đặc"),
71: ("Hình 32.71 · Các vạch hiệu chuẩn thường được khắc ở hai đầu thang đo để định vị việc chia "
     "thang. Trái: Nhiệt kế chất lượng tốt. Vạch hiệu chuẩn ngay sát vạch 0°C. Phải: Nhiệt kế "
     "dụng cụ phổ thông. Ở đây vạch hiệu chuẩn cao hơn khoảng ¼ độ chia so với vạch 50°C. Do là "
     "nhiệt kế rẻ hơn, nhà sản xuất chỉ cần đặt thang trong ¼ độ chia, và điều này thay đổi từ "
     "nhiệt kế này sang nhiệt kế khác trong cùng một lô.",
     "Figure 32.71 · Calibration marks are usually scratched on at both ends of a thermometer's "
     "scale to locate the ruling of the scale. Left: A good quality thermometer. The calibration "
     "mark is immediately alongside the 0°C mark. Right: A general-purpose thermometer. Here, the "
     "calibration mark is about ¼ scale division above the 50°C mark. Since it is a cheaper "
     "thermometer, the manufacturer is content to locate the scale within the ¼ scale division, "
     "and this would vary from thermometer to thermometer in the same batch.",
     "Hai nhiệt kế minh họa vạch hiệu chuẩn sát vạch 0°C (trái) và cao hơn ¼ độ chia so với "
     "vạch 50°C (phải)",
     "Two thermometers illustrating the calibration mark beside the 0°C mark (left) and ¼ "
     "scale division above the 50°C mark (right)",
     "Vạch hiệu chuẩn trên thang đo"),
72: ("Hình 32.72 · Một chỗ đứt gãy điển hình trong cột thủy ngân của nhiệt kế.",
     "Figure 32.72 · A typical break in the mercury column of a thermometer.",
     "Cột thủy ngân bị đứt gãy với một bọt khí ngăn cách giữa hai đoạn",
     "A mercury column broken by a trapped gas bubble between two segments",
     "Chỗ đứt gãy cột thủy ngân"),
73: ("Hình 32.73 · Ba điều kiện ngâm được dùng cho nhiệt kế chất lỏng trong thủy tinh. Điều kiện "
     "ngâm được ưa chuộng thường được đánh dấu bằng một đường hoặc khoảng cách trên thân đối với "
     "nhiệt kế ngâm một phần, hoặc được chỉ ra bởi thông số kỹ thuật của nhiệt kế.",
     "Figure 32.73 · Three types of immersion conditions used for liquid-in-glass thermometers. "
     "The preferred immersion condition is usually marked as a line or distance on the stem for "
     "partial-immersion thermometers or is given by the thermometer specification.",
     "Ba sơ đồ nhiệt kế trong bể: ngâm hoàn toàn, ngâm toàn phần và ngâm một phần",
     "Three thermometer diagrams in a bath: complete, total and partial immersion",
     "Ba điều kiện ngâm"),
74: ("Hình 32.74 · Biểu đồ hiệu chỉnh do ngâm nổi cho nhiệt kế thủy ngân trong thủy tinh với "
     "k = 0,00016 °C⁻¹.",
     "Figure 32.74 · Chart of stem exposure corrections for mercury-in-glass thermometers with "
     "k = 0.00016 °C⁻¹.",
     "Biểu đồ đường biểu diễn hiệu chỉnh theo độ lệch nhiệt độ cho các chiều dài cột nổi khác nhau",
     "Line chart of the correction versus temperature difference for various emergent-column "
     "lengths",
     "Biểu đồ hiệu chỉnh do ngâm nổi"),
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
def F70(lang):
    W, H = 560, 380
    p = []
    bx, by = 175, 332
    p.append(K._ell(bx, by, 40, 52, K.FILL, K.E, 1.8))       # bulb outline
    p.append(K._rect(163, 72, 24, 256, K.FILL, K.E, 1.8))    # stem
    p.append(K._ell(bx, 42, 22, 18, K.FILL, K.E, 1.6))       # expansion chamber
    p.append(K._ell(bx, by, 28, 38, K.DARK, K.E, 1.2))       # mercury in bulb
    p.append(K._rect(169, 190, 12, 142, K.DARK, K.E, 0.8))   # mercury column in stem
    p.append(K._ell(bx, 190, 6, 4, K.DARK, K.E, 0.8))        # meniscus
    for yy, lab in ((92, "0"), (142, "25"), (192, "50"),
                    (242, "75"), (292, "100")):
        p.append(K._line(197, yy, 206, yy, K.E, 1.0))
        p.append(K._lbl(210, yy + 4, lab, "ts", "start", K._fs(9)))
    p.append(K._line(197, 192, 206, 192, K.S, 1.8))          # calibration mark at 50
    p.append(K._arr(224, 332, bx + 28, by, K.E, sw=1.2))
    p.append(K._lbl(230, 326, "bầu / bulb", "ts", "start", K._fs(9)))
    p.append(K._arr(224, 150, 187, 150, K.E, sw=1.2))
    p.append(K._lbl(230, 146, "thân mao quản / stem (capillary)", "ts", "start", K._fs(9)))
    p.append(K._arr(300, 250, 181, 250, K.G, sw=1.2))
    p.append(K._lbl(304, 246, "cột thủy ngân / mercury column", "ts", "start", K._fs(9)))
    p.append(K._lbl(210, 312, "thang chia / scale", "ts", "start", K._fs(9)))
    p.append(K._arr(224, 60, bx + 18, 42, K.E, sw=1.1))
    p.append(K._lbl(230, 54, "buồng giãn nở / expansion chamber", "ts", "start", K._fs(9)))
    p.append(K._lbl(300, 110, "vạch hiệu chuẩn / calibration mark", "ts", "start", K._fs(9)))
    return _emit_diagram(lang, 70, W, H, p)


def F71(lang):
    W, H = 560, 360
    p = [K._lbl(24, 26, "Minh họa vạch hiệu chuẩn / calibration-mark illustration",
                "ts", "start", K._fs(9))]
    # left: good quality
    p.append(K._ell(150, 300, 30, 40, K.FILL, K.E, 1.6))
    p.append(K._rect(140, 70, 20, 230, K.FILL, K.E, 1.6))
    p.append(K._ell(150, 300, 20, 28, K.DARK, K.E, 1.0))
    p.append(K._rect(145, 200, 10, 100, K.DARK, K.E, 0.8))
    for yy, lab in ((90, "0"), (140, "10"), (190, "20"), (240, "30"), (290, "40")):
        p.append(K._line(140, yy, 132, yy, K.E, 1.0))
        p.append(K._lbl(128, yy + 4, lab, "ts", "end", K._fs(8)))
    p.append(K._line(160, 90, 168, 90, K.S, 1.8))            # calibration mark at 0
    p.append(K._lbl(150, 330, "Trái: chất lượng tốt / left: good quality",
                    "ts", "middle", K._fs(8)))
    p.append(K._lbl(150, 348, "vạch hiệu chuẩn ngay cạnh 0°C / mark beside 0°C",
                    "ts", "middle", K._fs(8)))
    # right: general-purpose
    p.append(K._ell(410, 300, 30, 40, K.FILL, K.E, 1.6))
    p.append(K._rect(400, 70, 20, 230, K.FILL, K.E, 1.6))
    p.append(K._ell(410, 300, 20, 28, K.DARK, K.E, 1.0))
    p.append(K._rect(405, 180, 10, 120, K.DARK, K.E, 0.8))
    for yy, lab in ((90, "30"), (140, "40"), (190, "50"), (240, "60"), (290, "70")):
        p.append(K._line(420, yy, 428, yy, K.E, 1.0))
        p.append(K._lbl(432, yy + 4, lab, "ts", "start", K._fs(8)))
    p.append(K._line(400, 178, 392, 178, K.S, 1.8))          # mark ~1/4 above 50
    p.append(K._lbl(410, 330, "Phải: dụng cụ phổ thông / right: general-purpose",
                    "ts", "middle", K._fs(8)))
    p.append(K._lbl(410, 348, "vạch hiệu chuẩn ~¼ độ chia trên 50°C / ~¼ div. above 50°C",
                    "ts", "middle", K._fs(8)))
    return _emit_diagram(lang, 71, W, H, p)


def F72(lang):
    W, H = 560, 340
    p = []
    sx = 270
    p.append(K._rect(sx - 12, 50, 24, 250, K.FILL, K.E, 1.8))   # stem glass
    p.append(K._rect(sx - 6, 210, 12, 90, K.DARK, K.E, 0.6))    # lower mercury
    p.append(K._ell(sx, 210, 6, 4, K.DARK, K.E, 0.6))
    p.append(K._rect(sx - 6, 110, 12, 60, K.DARK, K.E, 0.6))    # upper mercury
    p.append(K._ell(sx, 110, 6, 4, K.DARK, K.E, 0.6))           # meniscus top
    p.append(K._circ(sx, 185, 7, "none", K.E, 1.0))             # gas bubble
    p.append(K._lbl(sx, 300, "chỗ đứt gãy cột thủy ngân / break in mercury column",
                    "ts", "middle", K._fs(9)))
    p.append(K._arr(sx + 30, 185, sx + 10, 185, K.E, sw=1.1))
    p.append(K._lbl(sx + 34, 181, "bọt khí / gas bubble", "ts", "start", K._fs(8)))
    p.append(K._lbl(sx - 110, 90, "cột trên / upper column", "ts", "start", K._fs(8)))
    p.append(K._lbl(sx - 110, 250, "cột dưới / lower column", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 72, W, H, p)


def F73(lang):
    W, H = 560, 340
    p = []
    p.append(K._rect(40, 60, 480, 220, K.FILL, K.E, 1.4))        # bath
    p.append(K._lbl(48, 84, "bể chất lỏng / liquid bath", "ts", "start", K._fs(9)))
    # (A) complete immersion
    p.append(K._ell(120, 250, 22, 30, K.FILL, K.E, 1.4))
    p.append(K._rect(112, 80, 16, 170, K.FILL, K.E, 1.4))
    p.append(K._rect(116, 120, 8, 130, K.DARK, K.E, 0.6))
    p.append(K._lbl(120, 300, "(A) ngâm hoàn toàn / complete", "ts", "middle", K._fs(8)))
    # (B) total immersion
    p.append(K._ell(280, 250, 22, 30, K.FILL, K.E, 1.4))
    p.append(K._rect(272, 40, 16, 210, K.FILL, K.E, 1.4))
    p.append(K._rect(276, 120, 8, 130, K.DARK, K.E, 0.6))
    p.append(K._lbl(280, 300, "(B) ngâm toàn phần / total", "ts", "middle", K._fs(8)))
    p.append(K._lbl(292, 36, "một phần nhỏ ở ngoài / small part out", "ts", "start", K._fs(7)))
    # (C) partial immersion
    p.append(K._ell(440, 250, 22, 30, K.FILL, K.E, 1.4))
    p.append(K._rect(432, 40, 16, 210, K.FILL, K.E, 1.4))
    p.append(K._rect(436, 235, 8, 15, K.DARK, K.E, 0.6))
    p.append(K._line(432, 220, 448, 220, K.S, 1.6))             # immersion line
    p.append(K._lbl(440, 300, "(C) ngâm một phần / partial", "ts", "middle", K._fs(8)))
    p.append(K._lbl(440, 30, "cột nổi / emergent column", "ts", "middle", K._fs(7)))
    p.append(K._arr(470, 60, 470, 205, K.G, sw=1.2))
    p.append(K._lbl(474, 130, "gradient nhiệt độ / temp. gradient", "ts", "start", K._fs(7)))
    return _emit_diagram(lang, 73, W, H, p)


def F74(lang):
    W, H = 560, 360
    xr, yr = (0, 200), (0, 10)
    xt = [(0, "0"), (50, "50"), (100, "100"), (150, "150"), (200, "200")]
    yt = [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")]
    curves = []
    b = _Box(W, H, xr, yr)
    for N, cls in [(50, "c1"), (100, "c2"), (150, "c3"),
                   (200, "d1"), (250, "c1"), (300, "c2")]:
        yend = N * 0.00016 * 200.0
        curves.append(([(0, 0.0), (200, yend)], cls))
    ex = []
    for N in (50, 100, 150, 200, 250, 300):
        yend = N * 0.00016 * 200.0
        ex.append(K._lbl(b.x(200) + 4, b.y(yend) - 2, "%d&deg;" % N,
                         "ts", "start", K._fs(8)))
    ex.append(K._circ(b.x(80), b.y(1.024), 4, "none", K.S, 1.4))
    ex.append(K._lbl(b.x(80) + 6, b.y(1.024) - 4,
                     "N=80, &Delta;=80 &rarr; 1,02&deg;C", "ts", "start", K._fs(8)))
    return _emit_chart(lang, 74, W, H, xr, yr, xt, yt, curves,
                       "độ lệch nhiệt độ &Delta; (&deg;C) / temperature difference",
                       "hiệu chỉnh (&deg;C) / correction",
                       extra="".join(ex))


# -------------------------------------------------------------------- tables
def _t3220(lang):
    vi = (lang == "vi")
    hd = (["Số hiệu<br>ASTM", "Khoảng<br>(&deg;C)", "Chiều dài tối đa<br>(mm)",
           "Chia mỗi<br>(&deg;C)", "Sai số tối đa<br>(&deg;C)"] if vi else
          ["ASTM<br>Thermometer<br>Number", "Range<br>(&deg;C)",
           "Maximum<br>length (mm)", "Graduation<br>at each (&deg;C)",
           "Maximum<br>error (&deg;C)"])
    rows = [
        ["62C", "&ndash;38 to +2", "384", "0.1", "0.1"],
        ["63C", "&ndash;8 to +32", "384", "0.1", "0.1"],
        ["64C", "&ndash;0.5 to +0.5 and 25 to 55", "384", "0.1", "0.1"],
        ["65C", "&ndash;0.5 to +0.5 and 50 to 80", "384", "0.1", "0.1"],
        ["66C", "&ndash;0.5 to +0.5 and 75 to 105", "384", "0.1", "0.1"],
        ["67C", "&ndash;0.5 to +0.5 and 95 to 155", "384", "0.2", "0.2"],
        ["68C", "&ndash;0.5 to +0.5 and 145 to 205", "384", "0.2", "0.2"],
        ["69C", "&ndash;0.5 to +0.5 and 195 to 305", "384", "0.5", "0.5"],
        ["70C", "&ndash;0.5 to +0.5 and 295 to 405", "384", "0.5", "0.5"],
    ]
    cap = ("Bảng 32.20 &middot; Tóm tắt các yêu cầu cho nhiệt kế chính xác ASTM." if vi else
           "Table 32.20 &middot; Summary of Requirements for ASTM Precision Thermometers.")
    return R.table(hd, rows, cap, small=True)


def _t3221(lang):
    vi = (lang == "vi")
    hd = (["Chất lỏng", "Hệ số giãn nở biểu kiến điển hình<br>(&deg;C<sup>&minus;1</sup>)",
           "Khoảng nhiệt độ có thể<br>(&deg;C)"] if vi else
          ["Liquid", "Typical apparent expansion coefficient<br>(&deg;C<sup>&minus;1</sup>)",
           "Possible temperature range<br>(&deg;C)"])
    rows = [
        ["Mercury" if not vi else "Thủy ngân", "0.00016", "&ndash;35 to 510"],
        ["Ethanol" if not vi else "Etanol", "0.00104", "&ndash;80 to 60"],
        ["Pentane" if not vi else "Pentan", "0.00145", "&ndash;200 to 30"],
        ["Toluene" if not vi else "Toluen", "0.00103", "&ndash;80 to 100"],
    ]
    cap = ("Bảng 32.21 &middot; Khoảng làm việc của một số chất lỏng nhiệt kế và hệ số giãn nở "
           "biểu kiến của chúng trong các loại thủy tinh nhiệt kế quanh nhiệt độ phòng." if vi else
           "Table 32.21 &middot; Working Range of Some Thermometric Liquids and Their Apparent "
           "Thermal Expansion Coefficient in Thermometer Glasses Around Room Temperature.")
    return R.table(hd, rows, cap, small=True)


def _t3222(lang):
    vi = (lang == "vi")
    hd = (["Môi trường", "Tĩnh<br>(s)", "Dòng 0,5 m s<sup>&minus;1</sup><br>(s)",
           "Vận tốc dòng vô hạn<br>(s)"] if vi else
          ["Medium", "Still<br>(s)", "0.5 m s<sup>&minus;1</sup> flow<br>(s)",
           "Infinite flow velocity<br>(s)"])
    rows = [
        ["Water" if not vi else "Nước", "10", "2.4", "2.2"],
        ["Oil" if not vi else "Dầu", "40", "4.8", "2.2"],
        ["Air" if not vi else "Không khí", "190", "71", "2.2"],
    ]
    cap = ("Bảng 32.22 &middot; Hằng số thời gian cho nhiệt kế thủy ngân trong thủy tinh có "
           "bầu đường kính 5 mm." if vi else
           "Table 32.22 &middot; Time Constants for a Mercury-In-Glass Thermometer with a "
           "5-mm Diameter Bulb.")
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

    b = [R.h2("32.8 Nhiệt kế chất lỏng trong thủy tinh" if vi else
              "32.8 Liquid-in-Glass Thermometers",
              "Liquid-in-Glass Thermometers" if vi else
              "Nhiệt kế chất lỏng trong thủy tinh")]
    b.append(R.authors("J.V. Nicholas", ""))

    # =============================================================== intro
    b.append(P(
        "The earliest form of thermometer, known as a thermoscope, was a liquid-in-glass "
        "thermometer that was open to the atmosphere and thus responded to pressure. By sealing "
        "a thermoscope so that it responded only to temperature, the modern form of a "
        "liquid-in-glass thermometer resulted. As a temperature sensor, its use dominated "
        "temperature measurement for at least 200 years. Liquid-in-glass thermometers had a "
        "profound effect on the development of thermometry and, in popular opinion, they are "
        "the only 'real' thermometers. Liquid-in-glass thermometer sensors were developed in "
        "variety to fill nearly every niche in temperature measurement from &ndash;190&deg;C to "
        "+600&deg;C, including the measurement of temperature differences to a millikelvin. In "
        "spite of the fragile nature of glass, the popularity of these thermometers continues "
        "because of the chemical inertness of the glass, as well as the self-contained nature "
        "of the thermometer.",
        "Dạng nhiệt kế sớm nhất, được gọi là nhiệt kính (thermoscope), là một nhiệt kế chất "
        "lỏng trong thủy tinh thông với khí quyển và do đó đáp ứng với áp suất. Bằng cách bịt "
        "kín nhiệt kính để nó chỉ đáp ứng với nhiệt độ, dạng nhiệt kế chất lỏng trong thủy "
        "tinh hiện đại ra đời. Với tư cách một cảm biến nhiệt độ, việc sử dụng nó đã thống trị "
        "việc đo nhiệt độ ít nhất 200 năm. Nhiệt kế chất lỏng trong thủy tinh có ảnh hưởng sâu "
        "sắc đến sự phát triển của nhiệt kế học và, theo quan điểm phổ thông, chúng là những "
        "nhiệt kế 'thực sự' duy nhất. Các cảm biến nhiệt kế chất lỏng trong thủy tinh được "
        "phát triển đa dạng để lấp gần như mọi ngóc ngách của phép đo nhiệt độ từ &ndash;190&deg;C "
        "đến +600&deg;C, kể cả việc đo độ chênh nhiệt độ tới mức milikelvin. Mặc dù thủy tinh "
        "dễ vỡ, sự phổ biến của các nhiệt kế này vẫn tiếp tục nhờ tính trơ hóa học của thủy "
        "tinh, cũng như bản chất tự chứa của nhiệt kế."))
    b.append(P(
        "Measurement-sensor designers are unlikely to develop their own liquid-in-glass "
        "thermometers, but many will use them to check the performance of a new temperature "
        "sensor. The emphasis in this chapter section will therefore be on the use of "
        "mercury-in-glass thermometers &mdash; the most successful liquid-in-glass thermometer "
        "&mdash; as calibration references. Mercury-in-glass thermometers provide a stable "
        "temperature reference to an accuracy of 0.1&deg;C, provided they are chosen and used "
        "with care. The extra requirements to achieve higher accuracy are indicated, but are "
        "beyond the scope of this section. The trend is, however, to move away from "
        "mercury-in-glass thermometers for specialized uses (in particular, where the risk "
        "from glass or mercury contamination is not acceptable; for example, in the food or "
        "aviation industries). Other forms of temperature sensors described in this handbook "
        "are more suitable.",
        "Những người thiết kế cảm biến đo lường khó có thể tự chế tạo nhiệt kế chất lỏng trong "
        "thủy tinh của riêng mình, nhưng nhiều người sẽ dùng chúng để kiểm tra hiệu năng của "
        "một cảm biến nhiệt độ mới. Vì vậy, trọng tâm của mục này sẽ là việc sử dụng nhiệt kế "
        "thủy ngân trong thủy tinh &mdash; nhiệt kế chất lỏng trong thủy tinh thành công nhất "
        "&mdash; như các chuẩn hiệu chuẩn. Nhiệt kế thủy ngân trong thủy tinh cung cấp một "
        "chuẩn nhiệt độ ổn định với độ chính xác 0,1&deg;C, miễn là được lựa chọn và sử dụng "
        "cẩn thận. Các yêu cầu bổ sung để đạt độ chính xác cao hơn được chỉ ra, nhưng nằm "
        "ngoài phạm vi của mục này. Tuy nhiên, xu hướng là chuyển dần ra khỏi nhiệt kế thủy "
        "ngân trong thủy tinh cho các mục đích chuyên biệt (đặc biệt, nơi rủi ro từ nhiễm "
        "bẩn thủy tinh hay thủy ngân là không thể chấp nhận; ví dụ, trong công nghiệp thực "
        "phẩm hay hàng không). Các dạng cảm biến nhiệt độ khác được mô tả trong cuốn sách này "
        "thích hợp hơn."))

    # ====================================================== general description
    b.append(H3("General Description", "Mô tả chung"))
    b.append(P(
        "A common form of mercury-in-glass is a solid-stem glass thermometer illustrated in "
        "Figure 32.70. The other major form of liquid-in-glass thermometer is the enclosed "
        "scale thermometer, for which the general principles discussed will also apply. There "
        "are four main parts to the liquid-in-glass thermometer:",
        "Một dạng phổ biến của nhiệt kế thủy ngân trong thủy tinh là nhiệt kế thủy tinh thân "
        "đặc được minh họa ở Hình 32.70. Dạng chính khác của nhiệt kế chất lỏng trong thủy "
        "tinh là nhiệt kế thang chia kín, và các nguyên lý chung được thảo luận cũng áp dụng "
        "cho nó. Nhiệt kế chất lỏng trong thủy tinh có bốn bộ phận chính:"))
    b.append(R.ul([
        ("The bulb is a thin glass container holding the bulk of the thermometric liquid. The "
         "glass must be of suitable type and properly annealed. The thinness is essential for "
         "good thermal contact with the medium being measured, but it can result in "
         "instabilities due to applied stress or sudden shock. Some lower-accuracy, "
         "general-purpose thermometers are made with a thicker glass bulb to lower the risk of "
         "breakage."
         if not vi else
         "Bầu là một bình chứa thủy tinh mỏng chứa phần lớn chất lỏng nhiệt kế. Thủy tinh phải "
         "thuộc loại thích hợp và được ủ đúng cách. Độ mỏng là thiết yếu để có tiếp xúc nhiệt "
         "tốt với môi trường đang đo, nhưng nó có thể gây ra sự không ổn định do ứng suất tác "
         "dụng hay va chạm đột ngột. Một số nhiệt kế dụng cụ phổ thông kém chính xác hơn được "
         "làm với bầu thủy tinh dày hơn để giảm nguy cơ vỡ."),
        ("The stem is a glass capillary. Again, a suitable glass is necessary and may differ "
         "from that of the bulb. The bore can be gas-filled or vacuous. The volume of the bore "
         "must be somewhat smaller than the volume of the bulb for good sensitivity. In "
         "addition, the bore must be smooth, with a uniform cross section."
         if not vi else
         "Thân là một mao quản thủy tinh. Một lần nữa, loại thủy tinh thích hợp là cần thiết "
         "và có thể khác với loại dùng cho bầu. Lòng mao quản có thể được nạp khí hoặc chân "
         "không. Thể tích lòng phải nhỏ hơn một chút thể tích bầu để có độ nhạy tốt. Thêm vào "
         "đó, lòng phải nhẵn, với tiết diện đồng đều."),
        ("The liquid is usually mercury for best precision, or an organic liquid for lower "
         "temperature ranges."
         if not vi else
         "Chất lỏng thường là thủy ngân để có độ chính xác tốt nhất, hoặc một chất lỏng hữu cơ "
         "cho các dải nhiệt độ thấp hơn."),
        ("The markings are usually etched or printed onto the stem. The markings include the "
         "scale, to allow direct reading of the temperature, as well as other important "
         "information."
         if not vi else
         "Các vạch thường được khắc hoặc in lên thân. Các vạch bao gồm thang chia, cho phép "
         "đọc trực tiếp nhiệt độ, cũng như các thông tin quan trọng khác."),
    ]))
    b.append(P(
        "Figure 32.70 illustrates the main parts of a mercury-in-glass thermometer, along with "
        "a nomenclature for other features commonly found. Not all of the features will be "
        "found on all thermometers. The operation of liquid-in-glass thermometers is based on "
        "the expansion of the liquid with temperature; that is, the liquid acts as a transducer "
        "to convert thermal energy into a mechanical form. As the liquid in the bulb becomes "
        "hotter, it expands and the liquid is forced up the capillary stem. The temperature of "
        "the bulb is indicated by the position of the top of the mercury column with respect to "
        "the marked scale. The flattest part of the liquid meniscus is used as the indicator: "
        "for mercury, this is the top of the curve; for organic liquids, the bottom.",
        "Hình 32.70 minh họa các bộ phận chính của một nhiệt kế thủy ngân trong thủy tinh, "
        "cùng với thuật ngữ cho các đặc điểm khác thường thấy. Không phải mọi đặc điểm đều có "
        "mặt trên tất cả các nhiệt kế. Hoạt động của nhiệt kế chất lỏng trong thủy tinh dựa "
        "trên sự giãn nở của chất lỏng theo nhiệt độ; nói cách khác, chất lỏng đóng vai trò "
        "như một bộ chuyển đổi để biến năng lượng nhiệt thành dạng cơ học. Khi chất lỏng trong "
        "bầu nóng hơn, nó giãn nở và bị ép lên mao quản thân. Nhiệt độ của bầu được chỉ thị "
        "bằng vị trí đỉnh cột thủy ngân so với thang chia đã khắc. Phần phẳng nhất của chân "
        "cong chất lỏng được dùng làm chỉ thị: với thủy ngân, đó là đỉnh của đường cong; với "
        "chất lỏng hữu cơ, là đáy."))
    b.append(P(
        "The thermometers appear to have a simplicity about them, but this is lost when "
        "accurate measurements are required. By accuracy, we mean any reading where the "
        "temperature needs to be known to within 1&deg;C or better. The chief cause of "
        "inaccuracy is that not all of the liquid is at the required temperature due to its "
        "necessary presence in the stem. Thus, the thermometer is also sensitive to the stem "
        "temperature. The main advantage of a liquid-in-glass thermometer is that it is "
        "self-contained; but this means that the thermometer stem has to be seen to read the "
        "scale. Even in a well-designed apparatus, a good part of the stem will not be at the "
        "temperature of the bulb. For example, with a bulb immersed in boiling water and the "
        "entire stem outside, an error of 1&deg;C results from the cooler stem. Correction for "
        "this error can be incorporated in the scale of a partial-immersion thermometer, or the "
        "error can be corrected with a chart of stem corrections.",
        "Các nhiệt kế dường như có vẻ đơn giản, nhưng sự đơn giản đó mất đi khi cần các phép "
        "đo chính xác. Theo độ chính xác, chúng ta muốn nói bất kỳ phép đọc nào mà nhiệt độ "
        "cần biết trong phạm vi 1&deg;C hoặc tốt hơn. Nguyên nhân chính gây không chính xác là "
        "không phải tất cả chất lỏng đều ở nhiệt độ yêu cầu do sự hiện diện tất yếu của nó "
        "trong thân. Do đó, nhiệt kế cũng nhạy với nhiệt độ thân. Ưu điểm chính của nhiệt kế "
        "chất lỏng trong thủy tinh là nó tự chứa; nhưng điều này có nghĩa là phải nhìn thấy "
        "thân nhiệt kế để đọc thang. Ngay cả trong một thiết bị thiết kế tốt, một phần đáng "
        "kể của thân sẽ không ở nhiệt độ của bầu. Ví dụ, với bầu ngâm trong nước sôi và toàn "
        "bộ thân ở ngoài, một sai số 1&deg;C phát sinh do thân mát hơn. Hiệu chỉnh cho sai số "
        "này có thể được đưa vào thang của một nhiệt kế ngâm một phần, hoặc sai số có thể được "
        "hiệu chỉnh bằng một biểu đồ các hiệu chỉnh thân."))
    b.append(P(
        "The next most significant cause of error comes from the glass, a substance with "
        "complex mechanical properties. Like mercury, it expands rapidly on heating but does "
        "not contract immediately on cooling. This produces a hysteresis which, for a good "
        "glass, is about 0.1% of the temperature change. A good, well-annealed thermometer "
        "glass will relax back over a period of days. An ordinary glass might never recover its "
        "shape. Besides this hysteresis, the glass bulb undergoes a secular contraction over "
        "time; that is, the thermometer reading increases with age, but fortunately the effect "
        "is slow and calibration checks at the ice point, 0&deg;C, can correct for it.",
        "Nguyên nhân sai số đáng kể tiếp theo bắt nguồn từ thủy tinh, một chất có tính chất cơ "
        "học phức tạp. Giống thủy ngân, nó giãn nở nhanh khi đun nóng nhưng không co lại ngay "
        "khi làm mát. Điều này sinh ra một độ trễ (hysteresis) mà, với một loại thủy tinh tốt, "
        "vào khoảng 0,1% sự thay đổi nhiệt độ. Một thủy tinh nhiệt kế được ủ kỹ và tốt sẽ thư "
        "giãn trở lại trong vài ngày. Một loại thủy tinh thường có thể không bao giờ phục hồi "
        "hình dạng. Ngoài độ trễ này, bầu thủy tinh còn trải qua một sự co ngót lâu dài theo "
        "thời gian; nói cách khác, số đọc nhiệt kế tăng theo tuổi thọ, nhưng may mắn là hiệu "
        "ứng này chậm và các kiểm tra hiệu chuẩn tại điểm nước đá, 0&deg;C, có thể hiệu chỉnh "
        "cho nó."))
    b.append(P(
        "A bewildering number of types of liquid-in-glass thermometers are available, with "
        "many of the variations being designed with different dimensions and temperature "
        "ranges to suit specific applications. For best performance, solid-stem "
        "mercury-in-glass thermometers should be restricted to operation over the maximum "
        "range &ndash;38&deg;C to 250&deg;C. The purchase should be guided by a specification "
        "as published by a recognized standards body. Such bodies include the International "
        "Standards Organisation (ISO) [1]; the American Society for Testing and Materials "
        "(ASTM) [2]; the British Standards Institute (BS) [3]; or the Institute for Petroleum "
        "(IP). Be aware that some type numbers are the same, yet may refer to different "
        "thermometers, such as in the IP and ASTM ranges. Make sure the specification body is "
        "referred to; for example, an order for a 16C thermometer could result in either an "
        "ASTM 10C, the equivalent of an IP 16C, or an IP 61C, the equivalent of ASTM 16C.",
        "Có một số lượng nhiệt kế chất lỏng trong thủy tinh dạng đến chóng mặt, với nhiều biến "
        "thể được thiết kế với các kích thước và dải nhiệt độ khác nhau để phù hợp các ứng "
        "dụng cụ thể. Để có hiệu năng tốt nhất, nhiệt kế thủy ngân trong thủy tinh thân đặc "
        "nên giới hạn hoạt động trong dải tối đa &ndash;38&deg;C đến 250&deg;C. Việc mua sắm "
        "nên được dẫn dắt bởi một đặc điểm kỹ thuật do một cơ quan tiêu chuẩn được công nhận "
        "ban hành. Các cơ quan như vậy gồm Tổ chức Tiêu chuẩn Quốc tế (ISO) [1]; Hội đồng "
        "Tiêu chuẩn và Vật liệu Hoa Kỳ (ASTM) [2]; Viện Tiêu chuẩn Anh (BS) [3]; hoặc Viện "
        "Dầu mỏ (IP). Cần lưu ý rằng một số số kiểu giống nhau, nhưng có thể chỉ các nhiệt kế "
        "khác nhau, chẳng hạn như trong các dải IP và ASTM. Hãy chắc chắn tham chiếu cơ quan "
        "ban hành đặc điểm kỹ thuật; ví dụ, một đơn hàng cho nhiệt kế 16C có thể dẫn đến hoặc "
        "là ASTM 10C, tương đương IP 16C, hoặc IP 61C, tương đương ASTM 16C."))
    b.append(P(
        "One's choice of thermometer will most probably be a compromise between the best "
        "range, scale division, and length for the purpose. If good precision is required, "
        "then the thermometer range will be constrained to avoid extremely long and unwieldy "
        "thermometers. Table 32.20 gives the specification for precision thermometers based on "
        "the compromise as seen by the ASTM [2]. The cost of these thermometers depends on the "
        "range and varies from $50 to $180 at 1996 prices. The best precision for the ASTM "
        "liquid-in-glass thermometers is a round 0.1&deg;C, with the thermometers supplied "
        "being accurate to one scale division. Consult the references at the end of this "
        "chapter section if higher-resolution thermometers are required. As a rule, choose "
        "thermometers subdivided to the accuracy desired, and do not rely on visual "
        "interpolation to increase the accuracy. If relying heavily on interpolation, then a "
        "better choice of thermometer should be made.",
        "Việc lựa chọn nhiệt kế của một người sẽ rất có thể là một thỏa hiệp giữa dải tốt nhất, "
        "độ chia thang và chiều dài cho mục đích đó. Nếu cần độ chính xác cao, thì dải nhiệt "
        "kế sẽ bị giới hạn để tránh các nhiệt kế cực kỳ dài và khó sử dụng. Bảng 32.20 đưa ra "
        "đặc điểm kỹ thuật cho các nhiệt kế chính xác dựa trên sự thỏa hiệp như ASTM thấy [2]. "
        "Giá của các nhiệt kế này tùy thuộc vào dải và dao động từ 50 đến 180 đô-la theo giá "
        "năm 1996. Độ chính xác tốt nhất cho các nhiệt kế chất lỏng trong thủy tinh ASTM là "
        "tròn 0,1&deg;C, với các nhiệt kế được cung cấp chính xác đến một độ chia thang. Hãy "
        "tham khảo các tài liệu tham khảo ở cuối mục chương này nếu cần các nhiệt kế độ phân "
        "giải cao hơn. Như một quy tắc, hãy chọn các nhiệt kế được chia nhỏ đến độ chính xác "
        "mong muốn, và đừng dựa vào nội suy trực quan để tăng độ chính xác. Nếu phụ thuộc "
        "nhiều vào nội suy, thì nên chọn một nhiệt kế tốt hơn."))
    b.append(P(
        "Table 32.20 has thermometers with an ice point either in the main scale or as an "
        "auxiliary scale. The ice point is a very convenient way to check on the on-going "
        "performance of a thermometer, and without it, more expensive time-consuming "
        "procedures may be needed.",
        "Bảng 32.20 có các nhiệt kế với điểm nước đá hoặc nằm trong thang chính hoặc là một "
        "thang phụ. Điểm nước đá là một cách rất tiện lợi để kiểm tra hiệu năng đang diễn ra "
        "của một nhiệt kế, và không có nó, các quy trình tốn kém thời gian hơn có thể cần "
        "thiết."))
    b.append(F70(lang))
    b.append(_t3220(lang))

    # ======================================================= liquid expansion
    b.append(H3("Liquid Expansion", "Sự giãn nở của chất lỏng"))
    b.append(P(
        "The equation that best describes the expansion of the mercury volume is:",
        "Phương trình mô tả tốt nhất sự giãn nở của thể tích thủy ngân là:"))
    b.append(EQ("<i>V</i><sub>t</sub> = <i>V</i><sub>0</sub> (1 + <i>a t</i> + "
                "<i>b t</i><sup>2</sup>)", "32.131"))
    b.append(P(
        "Equation 32.131 is the ideal equation for a mercury-in-glass thermometer. In "
        "practice, several factors modify the ideal behavior because of the way in which the "
        "thermometers are constructed. Because the glass of a mercury-in-glass thermometer "
        "also expands, it is the apparent expansion coefficient due to the differential "
        "expansion of the mercury with respect to the glass that is of interest. Glass used in "
        "a typical thermometer has a value of <i>a</i> = 2&middot;10<sup>&minus;5</sup> "
        "&deg;C<sup>&minus;1</sup>, about 10% that of mercury. Hence, both the glass and the "
        "mercury act as temperature transducers and thus justify the description "
        "&lsquo;mercury-in-glass.&rsquo; The mercury also serves as the temperature indicator "
        "in the stem and consequently might not be at the same temperature as the mercury in "
        "the bulb. While this effect is small for mercury, where the bulb volume is 6250 times "
        "the volume of the mercury in a 1&deg;C length of the capillary stem, thermometers "
        "used in partial immersion often need correcting. See Table 32.21 for the expansion "
        "coefficients of other liquids and their range of use.",
        "Phương trình 32.131 là phương trình lý tưởng cho một nhiệt kế thủy ngân trong thủy "
        "tinh. Trong thực tế, một số yếu tố làm thay đổi hành vi lý tưởng do cách các nhiệt kế "
        "được chế tạo. Bởi vì thủy tinh của nhiệt kế thủy ngân trong thủy tinh cũng giãn nở, "
        "nên hệ số giãn nở biểu kiến do sự giãn nở vi sai của thủy ngân so với thủy tinh mới "
        "là điều đáng quan tâm. Thủy tinh dùng trong một nhiệt kế điển hình có giá trị "
        "<i>a</i> = 2&middot;10<sup>&minus;5</sup> &deg;C<sup>&minus;1</sup>, khoảng 10% của "
        "thủy ngân. Do đó, cả thủy tinh lẫn thủy ngân đều đóng vai trò như các bộ chuyển đổi "
        "nhiệt độ và từ đó xứng đáng với tên gọi &lsquo;thủy ngân trong thủy tinh&rsquo;. "
        "Thủy ngân cũng đóng vai trò chỉ thị nhiệt độ trong thân và do đó có thể không ở cùng "
        "nhiệt độ với thủy ngân trong bầu. Mặc dù hiệu ứng này nhỏ đối với thủy ngân, nơi thể "
        "tích bầu lớn gấp 6250 lần thể tích thủy ngân trong một đoạn mao quản dài 1&deg;C, "
        "các nhiệt kế dùng ngâm một phần thường cần hiệu chỉnh. Xem Bảng 32.21 về các hệ số "
        "giãn nở của các chất lỏng khác và dải sử dụng của chúng."))
    b.append(_t3221(lang))
    b.append(P(
        "The bore in the stem needs to be smooth and uniform. An allowed departure from "
        "uniformity is a contraction chamber that, by taking up a volume of the expanding "
        "mercury, allows the overall length of the thermometer to be kept a reasonable size. "
        "The chamber shape must be very smooth to prevent bubbles of gas being trapped. An "
        "auxiliary scale is usually added for the ice point if a contraction chamber is used. "
        "The marked scale allows the user to read the column length as a temperature. For a "
        "well-made thermometer, the change in length is proportional to the change in volume "
        "and hence to the temperature, as per Equation 32.131. In order to make the scale, the "
        "manufacturer first places &lsquo;calibration&rsquo; marks on the thermometer stem, "
        "as shown in Figure 32.71. Depending on the range and accuracy, more than two "
        "calibration marks can be used and, thus, the thermometer stem is divided into "
        "segments. A ruling engine is then used to rule a scale between each pair of marks, "
        "with careful alignments between the adjacent segments if they occur. The scale rulings "
        "will be spaced to approximate Equation 32.131 to the accuracy expected for the "
        "thermometer type. A good indicator of the quality of a thermometer is how close these "
        "calibration scratches are to the scale markings.",
        "Lòng mao quản trong thân cần nhẵn và đồng đều. Một sự sai lệch cho phép so với sự "
        "đồng đều là một buồng co ngót, bằng cách thu nhận một thể tích thủy ngân giãn nở, cho "
        "phép giữ tổng chiều dài nhiệt kế ở một kích thước hợp lý. Hình dạng buồng phải rất "
        "nhẵn để ngăn bọt khí bị giữ lại. Một thang phụ thường được thêm cho điểm nước đá nếu "
        "dùng buồng co ngót. Thang chia đã khắc cho phép người dùng đọc chiều dài cột như một "
        "nhiệt độ. Đối với một nhiệt kế làm tốt, sự thay đổi chiều dài tỉ lệ với sự thay đổi "
        "thể tích và do đó tỉ lệ với nhiệt độ, theo Phương trình 32.131. Để làm thang, nhà "
        "sản xuất trước tiên đặt các vạch &lsquo;hiệu chuẩn&rsquo; trên thân nhiệt kế, như "
        "thể hiện ở Hình 32.71. Tùy thuộc vào dải và độ chính xác, có thể dùng hơn hai vạch "
        "hiệu chuẩn, và do đó thân nhiệt kế được chia thành các đoạn. Một máy khắc thang sau "
        "đó được dùng để khắc một thang giữa mỗi cặp vạch, với sự căn chỉnh cẩn thận giữa các "
        "đoạn kề nhau nếu có. Các đường khắc thang sẽ được giãn cách để xấp xỉ Phương trình "
        "32.131 đến độ chính xác kỳ vọng cho loại nhiệt kế. Một chỉ báo tốt về chất lượng của "
        "một nhiệt kế là các vết khắc hiệu chuẩn gần với các vạch thang đến mức nào."))
    b.append(P(
        "Because of the segmented ruling, it pays to check that the scale markings are uniform "
        "in appearance with no obvious glitches. Quite marked discontinuities in the scale are "
        "sometimes found. The markings are individual to each thermometer and the total scale "
        "length can vary from thermometer to thermometer. This can be an inconvenience if a "
        "thermometer has to be replaced; but fortunately, most quality thermometer "
        "specifications restrict the amount of variation permissible.",
        "Do việc khắc theo đoạn, nên kiểm tra xem các vạch thang có đồng đều về hình dáng "
        "không có các gờ rõ ràng hay không. Đôi khi người ta thấy các điểm không liên tục khá "
        "rõ rệt trên thang. Các vạch là riêng biệt cho từng nhiệt kế và tổng chiều dài thang "
        "có thể thay đổi từ nhiệt kế này sang nhiệt kế khác. Điều này có thể gây bất tiện nếu "
        "một nhiệt kế phải được thay thế; nhưng may mắn là, hầu hết các đặc điểm kỹ thuật "
        "nhiệt kế chất lượng đều giới hạn mức biến thiên cho phép."))
    b.append(F71(lang))

    # ================================================== time-constant effects
    b.append(H3("Time-Constant Effects", "Các hiệu ứng hằng số thời gian"))
    b.append(P(
        "The time constant is determined almost entirely by the diameter of the bulb because "
        "heat must be conducted from the outside to the center of the bulb. A typical bulb of "
        "diameter 5 mm has a relatively short time constant. The length of the bulb is then "
        "determined by the sensitivity required of the thermometer, given that there is a "
        "minimum useful diameter for the capillary bore. The choice of bore diameter is a "
        "compromise involving several error effects. A large-diameter bore requires a larger "
        "volume bulb to achieve a given resolution, thus increasing the thermal capacity. A "
        "small-diameter bore not only becomes difficult to read but also suffers from "
        "stiction &mdash; the mercury moving in fits and starts due to the surface tension "
        "between the mercury and the bore wall. Stiction should be kept less than 1/5 of a "
        "scale division. Table 32.22 gives the 1/<i>e</i> time constants in various media for "
        "a 5-mm diameter bulb. Time constants for other diameters can be estimated by scaling "
        "the time in proportion to the diameter. The table clearly indicates that the "
        "thermometer is best used with flowing (or stirred) fluids.",
        "Hằng số thời gian được xác định gần như hoàn toàn bởi đường kính bầu vì nhiệt phải "
        "được dẫn từ bên ngoài vào tâm bầu. Một bầu điển hình đường kính 5 mm có hằng số thời "
        "gian tương đối ngắn. Chiều dài bầu khi đó được xác định bởi độ nhạy yêu cầu của nhiệt "
        "kế, với điều kiện có một đường kính hữu dụng tối thiểu cho lòng mao quản. Việc chọn "
        "đường kính lòng là một thỏa hiệp liên quan đến một số hiệu ứng sai số. Lòng đường "
        "kính lớn đòi hỏi một bầu thể tích lớn hơn để đạt được một độ phân giải nhất định, do "
        "đó làm tăng nhiệt dung. Lòng đường kính nhỏ không chỉ khó đọc hơn mà còn chịu ảnh "
        "hưởng của sự dính (stiction) &mdash; thủy ngân di chuyển giật cục do sức căng bề "
        "mặt giữa thủy ngân và thành lòng. Sự dính nên được giữ nhỏ hơn 1/5 độ chia thang. "
        "Bảng 32.22 đưa ra các hằng số thời gian 1/<i>e</i> trong các môi trường khác nhau "
        "cho một bầu đường kính 5 mm. Các hằng số thời gian cho các đường kính khác có thể "
        "ước tính bằng cách tỉ lệ thời gian theo đường kính. Bảng cho thấy rõ nhiệt kế được "
        "dùng tốt nhất với các chất lỏng đang chảy (hoặc được khuấy)."))
    b.append(_t3222(lang))

    # ================================================= thermal capacity effects
    b.append(H3("Thermal Capacity Effects", "Các hiệu ứng nhiệt dung"))
    b.append(P(
        "Glass thermometers are bulky and have considerable mass, especially high-precision "
        "thermometers that have a long bulb. The high thermal mass or heat capacity can upset "
        "temperature measurements, making high precision difficult. Inappropriate use of "
        "liquid-in-glass thermometers occurs when the thermometer is too massive to achieve "
        "the precision required. Preheating the thermometer can alleviate the worst of the "
        "problem. For higher precision and low mass, choose a platinum resistance thermometer "
        "or thermistor instead.",
        "Nhiệt kế thủy tinh cồng kềnh và có khối lượng đáng kể, đặc biệt là các nhiệt kế độ "
        "chính xác cao có bầu dài. Nhiệt dung lớn hay nhiệt dung nhiệt cao có thể làm hỏng "
        "các phép đo nhiệt độ, khiến độ chính xác cao khó đạt được. Việc dùng không thích hợp "
        "nhiệt kế chất lỏng trong thủy tinh xảy ra khi nhiệt kế quá đồ sộ để đạt được độ "
        "chính xác yêu cầu. Làm nóng trước nhiệt kế có thể giảm bớt phần tồi tệ nhất của vấn "
        "đề. Để có độ chính xác cao và khối lượng thấp, hãy chọn một nhiệt kế điện trở bạch "
        "kim hoặc nhiệt điện trở (thermistor) thay thế."))
    b.append(P(
        "Simple estimates of the heat requirements are made by measuring the volume of "
        "thermometer immersed, and assuming that 2 J are required to raise 1 cm<sup>3</sup> "
        "of the thermometer volume (glass or mercury) by 1&deg;C.",
        "Các ước tính đơn giản về nhu cầu nhiệt được thực hiện bằng cách đo thể tích nhiệt kế "
        "được ngâm, và giả định rằng cần 2 J để nâng 1 cm<sup>3</sup> thể tích nhiệt kế "
        "(thủy tinh hoặc thủy ngân) lên 1&deg;C."))

    # ==================================================== separated columns
    b.append(H3("Separated Columns", "Cột chất lỏng bị đứt gãy"))
    b.append(P(
        "A common problem is for a part of the thermometric liquid in the stem to become "
        "separated from the main volume. While this will show as an ice point shift, it is "
        "still important to make a simple visual check when using the thermometer. With "
        "organic liquids, the problem might be more difficult to identify because liquid "
        "adheres to the surface of the capillary and may not be visible. Spirit thermometers "
        "need to be held vertically to allow the thermometric liquid to drain down. Warm the "
        "top of the thermometer to prevent condensation of any vapor. Allow time for drainage "
        "of the liquid in the thermometer if the temperature is lowered quickly (approximately "
        "3 min per centimeter). Cool the bulb first in order to keep the viscosity of the "
        "liquid in the stem low for better drainage. For mercury, the separation is usually "
        "visible. Two causes can be identified: boil-off and mechanical separation (Figure "
        "32.72). To help retard the boil-off of mercury vapor at high temperatures (e.g., "
        "above 150&deg;C), the capillary tube is filled with an inert gas when manufactured. "
        "Usually, dry nitrogen is used under pressure to prevent oxidation of the mercury. The "
        "expansion chamber must be kept cooler than the bulb to prevent a high pressure "
        "build-up. The high pressure can permanently distort the bulb even if rupture does not "
        "occur.",
        "Một vấn đề phổ biến là một phần chất lỏng nhiệt kế trong thân bị tách khỏi thể tích "
        "chính. Mặc dù điều này sẽ biểu hiện như một sự dịch chuyển điểm nước đá, nhưng việc "
        "kiểm tra trực quan đơn giản khi dùng nhiệt kế vẫn quan trọng. Với các chất lỏng hữu "
        "cơ, vấn đề có thể khó xác định hơn vì chất lỏng bám vào bề mặt mao quản và có thể "
        "không nhìn thấy. Nhiệt kế cồn cần được giữ thẳng đứng để chất lỏng nhiệt kế thoát "
        "xuống. Hãy làm ấm đỉnh nhiệt kế để ngăn ngưng tụ bất kỳ hơi nào. Cho thời gian để "
        "chất lỏng thoát ra nếu nhiệt độ hạ nhanh (khoảng 3 phút mỗi centimet). Làm mát bầu "
        "trước để giữ độ nhớt của chất lỏng trong thân thấp giúp thoát tốt hơn. Đối với thủy "
        "ngân, sự tách thường có thể nhìn thấy. Có thể xác định hai nguyên nhân: bay hơi và "
        "tách cơ học (Hình 32.72). Để giúp làm chậm sự bay hơi hơi thủy ngân ở nhiệt độ cao "
        "(ví dụ, trên 150&deg;C), ống mao quản được nạp một khí trơ khi chế tạo. Thường dùng "
        "nitơ khô dưới áp suất để ngăn oxy hóa thủy ngân. Buồng giãn nở phải được giữ mát hơn "
        "bầu để ngăn sự tích tụ áp suất cao. Áp suất cao có thể làm biến dạng vĩnh viễn bầu "
        "ngay cả khi không xảy ra vỡ."))
    b.append(F72(lang))
    b.append(P(
        "Mechanical separation of the liquid column is, unfortunately, a common occurrence, "
        "particularly after shipment. A gas fill will help prevent this separation but, "
        "conversely, the gas makes it more difficult to rejoin. There is also a risk of "
        "trapped gas bubbles in the bulb or expansion chambers and careful inspection is "
        "needed to locate them. A vacuum in the capillary tube will give rise to more breaks, "
        "but they are easily rejoined. With care, it is often possible to rejoin the column "
        "and still have a viable thermometer. However, it must be realized that attempts to "
        "join a broken column could also result in the thermometer being discarded if the "
        "procedure is not successful. Column breaks that occur only when the thermometer is "
        "heated often require that the thermometer be discarded. Various procedures for "
        "joining a broken mercury column can be tried. The procedures below are given in order "
        "of preference.",
        "Sự tách cơ học của cột chất lỏng, thật không may, là một sự cố phổ biến, đặc biệt "
        "sau khi vận chuyển. Một lớp khí nạp sẽ giúp ngăn sự tách này nhưng, ngược lại, khí "
        "làm cho việc nối lại khó hơn. Cũng có nguy cơ các bọt khí bị giữ lại trong bầu hay "
        "các buồng giãn nở và cần kiểm tra cẩn thận để xác định chúng. Chân không trong ống "
        "mao quản sẽ sinh ra nhiều chỗ đứt hơn, nhưng chúng dễ nối lại. Với sự cẩn thận, "
        "thường có thể nối lại cột và vẫn có một nhiệt kế khả dụng. Tuy nhiên, phải nhận thức "
        "rằng các nỗ lực nối một cột đứt cũng có thể dẫn đến việc nhiệt kế bị loại bỏ nếu "
        "quy trình không thành công. Các chỗ đứt cột chỉ xảy ra khi nhiệt kế được đun nóng "
        "thường đòi hỏi nhiệt kế phải bị loại bỏ. Các quy trình khác nhau để nối một cột thủy "
        "ngân đứt có thể được thử. Các quy trình dưới đây được đưa ra theo thứ tự ưu tiên."))
    b.append(R.ul([
        ("Lightly tap the thermometer while holding it vertically. This may work for a "
         "vacuous thermometer."
         if not vi else
         "Gõ nhẹ nhiệt kế khi cầm nó thẳng đứng. Cách này có thể hiệu quả với một nhiệt kế "
         "chân không."),
        ("Apply centrifugal force, but avoid a flicking action, and be careful to avoid "
         "striking anything. This can be best done by holding the bulb alongside the thumb, "
         "protecting it with the fingers, and with the stem along the arm. Raise the arm above "
         "the head and bring it down quickly to alongside the leg."
         if not vi else
         "Tạo lực ly tâm, nhưng tránh động tác quất mạnh, và cẩn thận tránh va đập vào bất "
         "cứ thứ gì. Cách tốt nhất là giữ bầu sát ngón cái, bảo vệ nó bằng các ngón tay, và "
         "đặt thân dọc theo cánh tay. Giơ cánh tay lên trên đầu và hạ nhanh xuống sát đùi."),
        ("If both the above are unsuccessful, a cooling method can be attempted. This method "
         "relies on sufficient cooling of the bulb for all the mercury to contract into the "
         "bulb, leaving none in the stem. The column should be rejoined when it has warmed to "
         "room temperature. Carry out the warming slowly so that all the mercury is at the "
         "same temperature. More than one attempt might be needed. The first two methods might "
         "also need to be applied to assist movement of the mercury. Three cooling mediums "
         "readily available are: (1) salt, ice, and water (to &ndash;18&deg;C); (2) dry ice, "
         "i.e., solid CO<sub>2</sub> (&ndash;78&deg;C); (3) liquid nitrogen "
         "(&ndash;196&deg;C)."
         if not vi else
         "Nếu cả hai cách trên không thành công, có thể thử phương pháp làm lạnh. Phương pháp "
         "này dựa vào việc làm lạnh đủ bầu để toàn bộ thủy ngân co lại vào bầu, không còn "
         "trong thân. Cột nên được nối lại khi nó đã ấm đến nhiệt độ phòng. Thực hiện việc "
         "làm ấm từ từ để toàn bộ thủy ngân ở cùng một nhiệt độ. Có thể cần hơn một lần thử. "
         "Hai phương pháp đầu cũng có thể cần áp dụng để hỗ trợ sự di chuyển của thủy ngân. "
         "Ba môi trường làm lạnh sẵn có là: (1) muối, nước đá và nước (đến &ndash;18&deg;C); "
         "(2) nước đá khô, tức là CO<sub>2</sub> rắn (&ndash;78&deg;C); (3) nitơ lỏng "
         "(&ndash;196&deg;C)."),
    ]))
    b.append(P(
        "If the broken column has been successfully rejoined, then an ice point (or other "
        "reference point) check should be made. If the reading is the same as obtained "
        "previously, then the join can be considered completely successful and the thermometer "
        "ready for use. (It is essential to keep written records here.) However, a significant "
        "ice-point shift indicates that the join was not successful and that the thermometer "
        "should be discarded. If the ice-point shift is within that specified for the "
        "thermometer type, then treat the thermometer with suspicion until there is evidence "
        "of long-term stability, i.e., no significant ice-point changes after use.",
        "Nếu cột đứt đã được nối lại thành công, thì nên thực hiện một kiểm tra điểm nước đá "
        "(hoặc điểm tham chiếu khác). Nếu số đọc giống với số đọc trước đó, thì mối nối có "
        "thể được coi là hoàn toàn thành công và nhiệt kế sẵn sàng sử dụng. (Việc lưu giữ hồ "
        "sơ bằng văn bản ở đây là thiết yếu.) Tuy nhiên, một sự dịch chuyển điểm nước đá đáng "
        "kể cho thấy mối nối không thành công và nhiệt kế nên bị loại bỏ. Nếu sự dịch chuyển "
        "điểm nước đá nằm trong giới hạn quy định cho loại nhiệt kế, thì hãy đối xử với nhiệt "
        "kế một cách nghi ngờ cho đến khi có bằng chứng về sự ổn định dài hạn, tức là không "
        "có thay đổi điểm nước đá đáng kể sau khi sử dụng."))

    # ====================================================== immersion errors
    b.append(H3("Immersion Errors", "Sai số do ngâm"))
    b.append(P(
        "It was previously mentioned that problems are expected if not all the liquid in a "
        "liquid-in-glass thermometer is at the same temperature as the bulb. Because the "
        "scale must be read visually, liquid-in-glass thermometers are used at various "
        "immersion depths, which results in different parts of the thermometric liquid being "
        "at different temperatures. In addition, the clutter around an apparatus often "
        "necessitates the thermometer being placed in a nonideal position. Three distinct "
        "immersion conditions are recognized for a liquid-in-glass thermometer, and each "
        "requires a different error treatment. Figure 32.73 illustrates the three conditions.",
        "Như đã đề cập trước đó, người ta kỳ vọng sẽ có vấn đề nếu không phải tất cả chất "
        "lỏng trong nhiệt kế chất lỏng trong thủy tinh đều ở cùng nhiệt độ với bầu. Bởi vì "
        "thang phải được đọc trực quan, nhiệt kế chất lỏng trong thủy tinh được dùng ở các "
        "độ sâu ngâm khác nhau, dẫn đến các phần khác nhau của chất lỏng nhiệt kế ở các nhiệt "
        "độ khác nhau. Thêm vào đó, sự bề bộn xung quanh một thiết bị thường đòi hỏi nhiệt kế "
        "được đặt ở một vị trí không lý tưởng. Ba điều kiện ngâm riêng biệt được công nhận "
        "cho một nhiệt kế chất lỏng trong thủy tinh, và mỗi điều kiện đòi hỏi một cách xử lý "
        "sai số khác nhau. Hình 32.73 minh họa ba điều kiện."))
    b.append(R.ul([
        ("Complete immersion: By definition, if the complete bulb and stem are immersed at "
         "the same temperature, the thermometer is completely immersed. This condition is not "
         "common, except at room temperature, and should be avoided at higher temperatures. "
         "High pressure build-up in the thermometer can cause it to rupture, spreading deadly "
         "mercury vapor throughout the laboratory. Laboratories where there is a danger of "
         "mercury exposure to high temperatures should be kept well ventilated. In other "
         "words, DO NOT put a mercury thermometer completely inside an oven to measure the "
         "temperature. Specialized applications that use complete immersion take into account "
         "pressure effects on the thermometers."
         if not vi else
         "Ngâm hoàn toàn: Theo định nghĩa, nếu toàn bộ bầu và thân được ngâm ở cùng một nhiệt "
         "độ, nhiệt kế được ngâm hoàn toàn. Điều kiện này không phổ biến, trừ ở nhiệt độ "
         "phòng, và nên tránh ở các nhiệt độ cao hơn. Sự tích tụ áp suất cao trong nhiệt kế "
         "có thể gây vỡ nó, phát tán hơi thủy ngân chết người khắp phòng thí nghiệm. Các "
         "phòng thí nghiệm nơi có nguy cơ thủy ngân tiếp xúc với nhiệt độ cao nên được thông "
         "gió tốt. Nói cách khác, ĐỪNG đặt nhiệt kế thủy ngân hoàn toàn bên trong lò nướng "
         "để đo nhiệt độ. Các ứng dụng chuyên biệt dùng ngâm hoàn toàn phải tính đến các hiệu "
         "ứng áp suất lên nhiệt kế."),
        ("Total immersion: Total immersion applies to the situation where all the "
         "thermometric liquid, i.e., all the mercury in the bulb, the contraction chamber, "
         "and the stem, is at the temperature of interest. The remaining portion of the stem "
         "will have a temperature gradient to room temperature (approximately). Especially at "
         "high temperatures, the expansion chamber should be maintained close to room "
         "temperature to avoid pressure build-up. A very small part of the mercury column can "
         "be outside the region of interest, to allow visual readings to be made. The error "
         "introduced by this can be estimated by the procedures given below for "
         "partial-immersion thermometers. Obviously, the thermometer will have to be moved to "
         "allow a range of temperatures to be measured. Total-immersion thermometers are "
         "generally calibrated at total immersion and therefore do not need additional "
         "corrections."
         if not vi else
         "Ngâm toàn phần: Ngâm toàn phần áp dụng cho tình huống mà toàn bộ chất lỏng nhiệt kế, "
         "tức là toàn bộ thủy ngân trong bầu, buồng co ngót và thân, ở nhiệt độ quan tâm. "
         "Phần còn lại của thân sẽ có một gradient nhiệt độ đến nhiệt độ phòng (xấp xỉ). Đặc "
         "biệt ở nhiệt độ cao, buồng giãn nở nên được duy trì gần nhiệt độ phòng để tránh tích "
         "tụ áp suất. Một phần rất nhỏ của cột thủy ngân có thể nằm ngoài vùng quan tâm, để "
         "cho phép đọc trực quan. Sai số do điều này gây ra có thể ước tính bằng các quy trình "
         "đưa ra dưới đây cho các nhiệt kế ngâm một phần. Rõ ràng, nhiệt kế sẽ phải được di "
         "chuyển để cho phép đo một dải nhiệt độ. Các nhiệt kế ngâm toàn phần thường được hiệu "
         "chuẩn ở ngâm toàn phần và do đó không cần các hiệu chỉnh bổ sung."),
        ("Partial immersion: One way around the problem of scale visibility and the need to "
         "move the thermometer is to immerse the thermometer to some fixed depth so that "
         "most, but not all, of the mercury is at the temperature of interest. The part of the "
         "mercury column not immersed is referred to as the emergent column. Corrections will "
         "be needed to compensate for the error arising from the emergent column not being at "
         "the same temperature as the bulb. Many thermometers are designed and calibrated for "
         "partial immersion and are marked accordingly on the stem with an immersion depth or "
         "an immersion line (see Figure 32.70)."
         if not vi else
         "Ngâm một phần: Một cách giải quyết vấn đề về tầm nhìn thang và nhu cầu di chuyển "
         "nhiệt kế là ngâm nhiệt kế đến một độ sâu cố định sao cho phần lớn, nhưng không phải "
         "toàn bộ, thủy ngân ở nhiệt độ quan tâm. Phần cột thủy ngân không được ngâm được gọi "
         "là cột nổi. Các hiệu chỉnh sẽ cần thiết để bù đắp cho sai số phát sinh do cột nổi "
         "không ở cùng nhiệt độ với bầu. Nhiều nhiệt kế được thiết kế và hiệu chuẩn cho ngâm "
         "một phần và được đánh dấu tương ứng trên thân bằng một độ sâu ngâm hoặc một đường "
         "ngâm (xem Hình 32.70)."),
    ]))
    b.append(F73(lang))
    b.append(P(
        "A partial-immersion thermometer is properly defined when the temperature profile of "
        "the emergent column is also specified. Usually, an average stem temperature is quoted "
        "to represent the temperature profile of the emergent column. Thermometer "
        "specifications can define the expected stem temperature for a set of test "
        "temperatures, but they do not usually define stem temperatures for all possible "
        "readings. A measure of the stem temperature is required if the accuracy of the "
        "thermometer reading is to be assessed. The traditional way to measure the stem "
        "temperature is with a Faden thermometer. These are mercury-in-glass thermometers with "
        "a very long bulb, and various bulb lengths available. The bulb is mounted alongside "
        "the part of the stem containing the emergent column with the bottom of the bulb in "
        "the fluid. An average stem temperature is obtained as indicated by the Faden "
        "thermometer. Other ways of measuring the temperature profile are to use thermocouples "
        "along the length of the thermometer, or even several small mercury-in-glass "
        "thermometers. The stem temperature can be calculated as a simple average; but "
        "strictly speaking, it should be a length-weighted average.",
        "Một nhiệt kế ngâm một phần được định nghĩa đúng đắn khi cũng chỉ định được hồ sơ nhiệt "
        "độ của cột nổi. Thông thường, một nhiệt độ thân trung bình được trích dẫn để biểu "
        "diễn hồ sơ nhiệt độ của cột nổi. Các đặc điểm kỹ thuật nhiệt kế có thể xác định nhiệt "
        "độ thân kỳ vọng cho một tập hợp các nhiệt độ thử, nhưng chúng thường không xác định "
        "nhiệt độ thân cho mọi số đọc có thể. Một phép đo nhiệt độ thân là cần thiết nếu độ "
        "chính xác của số đọc nhiệt kế được đánh giá. Cách truyền thống để đo nhiệt độ thân là "
        "dùng một nhiệt kế Faden. Đó là các nhiệt kế thủy ngân trong thủy tinh có một bầu rất "
        "dài, và có sẵn các chiều dài bầu khác nhau. Bầu được gắn cạnh phần thân chứa cột nổi "
        "với đáy bầu trong chất lỏng. Một nhiệt độ thân trung bình thu được như được chỉ thị "
        "bởi nhiệt kế Faden. Các cách khác để đo hồ sơ nhiệt độ là dùng các cặp nhiệt điện dọc "
        "theo chiều dài nhiệt kế, hoặc thậm chí nhiều nhiệt kế thủy ngân trong thủy tinh nhỏ. "
        "Nhiệt độ thân có thể được tính như một trung bình cộng đơn giản; nhưng nói chặt chẽ, "
        "nó nên là một trung bình có trọng số theo chiều dài."))
    b.append(P(
        "Because the measured stem temperature might not be the same as that given on the "
        "calibration certificate, it is necessary to make corrections for the difference. For "
        "partial immersion thermometers, the true temperature reading <i>t</i> is given by:",
        "Bởi vì nhiệt độ thân đo được có thể không giống với nhiệt độ ghi trên giấy chứng "
        "nhận hiệu chuẩn, nên cần thực hiện các hiệu chỉnh cho sự khác biệt. Đối với các nhiệt "
        "kế ngâm một phần, số đọc nhiệt độ thực <i>t</i> được cho bởi:"))
    b.append(EQ("<i>t</i> = <i>t</i><sub>i</sub> + <i>N k</i> "
                "(<i>t</i><sub>2</sub> &minus; <i>t</i><sub>1</sub>)", "32.132"))
    b.append(P(
        "The use of Equation 32.132 with typical <i>k</i> values from Table 32.21 is "
        "estimated to give a 10% accuracy for the correction. Consequently, the correction is "
        "a major source of uncertainty for large temperature differences. Figure 32.74 gives "
        "a chart derived from Equation 32.132 for mercury thermometers that enables the stem "
        "correction to be determined graphically. One should become familiar enough with it to "
        "make quick estimates in order to determine whether the immersion condition error is "
        "significant and therefore needs correction. Thermometers are usually calibrated at "
        "their stated immersion conditions and the actual stem temperatures during calibration "
        "are measured and quoted on the certificate. In many applications, a thermometer is "
        "used for a standard test method (such as specified by the ASTM or IP). For these "
        "instances, the expected stem temperature is specified and there is no requirement for "
        "the stem temperature to be measured. The user will, however, need to adjust the "
        "certificate correction terms to the immersion conditions of the specification in "
        "order to see that the thermometer corrections meet the appropriate quality criteria. "
        "The chart of Figure 32.74 is useful, either to find corrections or to show faults "
        "with a particular measurement method.",
        "Việc dùng Phương trình 32.132 với các giá trị <i>k</i> điển hình từ Bảng 32.21 được "
        "ước tính cho độ chính xác 10% cho hiệu chỉnh. Do đó, hiệu chỉnh là một nguồn không "
        "chắc chắn chính đối với các độ chênh nhiệt độ lớn. Hình 32.74 đưa ra một biểu đồ "
        "suy ra từ Phương trình 32.132 cho các nhiệt kế thủy ngân cho phép xác định hiệu "
        "chỉnh thân một cách đồ họa. Người dùng nên quen đủ với nó để đưa ra các ước tính "
        "nhanh nhằm xác định liệu sai số điều kiện ngâm có đáng kể và do đó cần hiệu chỉnh "
        "hay không. Các nhiệt kế thường được hiệu chuẩn ở các điều kiện ngâm đã nêu và các "
        "nhiệt độ thân thực tế trong khi hiệu chuẩn được đo và ghi trên giấy chứng nhận. "
        "Trong nhiều ứng dụng, một nhiệt kế được dùng cho một phương pháp thử tiêu chuẩn (như "
        "do ASTM hoặc IP quy định). Với những trường hợp này, nhiệt độ thân kỳ vọng được quy "
        "định và không có yêu cầu đo nhiệt độ thân. Tuy nhiên, người dùng sẽ cần điều chỉnh "
        "các số hạng hiệu chỉnh của giấy chứng nhận theo các điều kiện ngâm của đặc điểm kỹ "
        "thuật để thấy rằng các hiệu chỉnh nhiệt kế đáp ứng các tiêu chí chất lượng thích "
        "hợp. Biểu đồ của Hình 32.74 rất hữu ích, hoặc để tìm các hiệu chỉnh hoặc để chỉ ra "
        "các khuyết điểm của một phương pháp đo cụ thể."))
    b.append(F74(lang))
    b.append(P(
        "For example, consider the case of measuring boiling water in a beaker with a "
        "total-immersion thermometer. The thermometer is too long to immerse and the water "
        "level is around the 20&deg;C mark. The emergent column is therefore 80&deg;C long "
        "and one assumes that the stem is close to room temperature of 20&deg;C, resulting in "
        "an 80&deg;C temperature difference from calibration conditions. On the chart, one "
        "finds that the intersection of the 80&deg;C emergent line and the 80&deg;C "
        "difference line gives a correction value of just over 1&deg;C. If this value is "
        "unacceptable, then clearly a redesign of the measurement method is warranted. More "
        "detailed examples can be found in the text of Nicholas and White [5].",
        "Ví dụ, xét trường hợp đo nước sôi trong một cốc bécher bằng một nhiệt kế ngâm toàn "
        "phần. Nhiệt kế quá dài để ngâm và mực nước ở khoảng vạch 20&deg;C. Do đó cột nổi dài "
        "80&deg;C và người ta giả định thân gần với nhiệt độ phòng 20&deg;C, dẫn đến một độ "
        "chênh nhiệt độ 80&deg;C so với điều kiện hiệu chuẩn. Trên biểu đồ, người ta thấy "
        "rằng giao điểm của đường nổi 80&deg;C và đường độ lệch 80&deg;C cho một giá trị hiệu "
        "chỉnh vừa quá 1&deg;C. Nếu giá trị này không thể chấp nhận, thì rõ ràng cần thiết kế "
        "lại phương pháp đo. Các ví dụ chi tiết hơn có thể tìm thấy trong văn bản của Nicholas "
        "và White [5]."))

    # ======================================================= organic liquids
    b.append(H3("Organic Liquids", "Chất lỏng hữu cơ"))
    b.append(P(
        "Thermometers with organic liquids have three possible uses: to measure temperatures "
        "below &ndash;38&deg;C; in situations where mercury is to be avoided; and for "
        "inexpensive thermometers. The utility of spirit thermometers is limited because of "
        "the lower achievable accuracy, the high nonlinearities, and the volatile nature of "
        "the liquids. Organic-liquid thermometers are also difficult to read because of the "
        "very clear liquid and concave meniscus. However, the use of a suitable dye and wide "
        "bore can give them as good a readability as mercury. Follow the recommendations of "
        "the section on Separated Columns and the section on Storage to get the best result "
        "from organic-liquid thermometers.",
        "Các nhiệt kế dùng chất lỏng hữu cơ có ba công dụng có thể: đo nhiệt độ dưới "
        "&ndash;38&deg;C; trong các tình huống cần tránh thủy ngân; và cho các nhiệt kế rẻ "
        "tiền. Công dụng của nhiệt kế cồn bị hạn chế do độ chính xác đạt được thấp hơn, độ "
        "phi tuyến cao, và bản chất dễ bay hơi của các chất lỏng. Các nhiệt kế chất lỏng hữu "
        "cơ cũng khó đọc do chất lỏng rất trong và chân cong lõm. Tuy nhiên, việc dùng một "
        "loại thuốc nhuộm thích hợp và lòng rộng có thể cho chúng độ dễ đọc tốt như thủy "
        "ngân. Hãy tuân theo các khuyến nghị của mục Cột chất lỏng bị đứt gãy và mục Bảo "
        "quản để có kết quả tốt nhất từ các nhiệt kế chất lỏng hữu cơ."))

    # ============================================================== storage
    b.append(H3("Storage", "Bảo quản"))
    b.append(P(
        "Most mercury-in-glass thermometers can be stored horizontally on trays in cabinets, "
        "care being taken to avoid any weight or pressure on the bulbs (one reason for the "
        "horizontal position). Avoid vibration. Corrugated cardboard, or similar material, can "
        "be used as a liner for a tray to prevent the thermometers from rolling. Thermometers "
        "whose main range is below 0&deg;C are better stored vertically, bulb down, in a cool "
        "place, but do not rest the thermometer on its bulb. This particularly applies to "
        "organic-liquid thermometers, which also should be shielded from light sources, as "
        "ultraviolet radiation can often degrade the liquid. If the top of the bore of a "
        "spirit thermometer is kept at a slightly higher temperature than the rest of the "
        "thermometer, then the volatile liquid will not condense in the expansion chamber.",
        "Hầu hết các nhiệt kế thủy ngân trong thủy tinh có thể được bảo quản nằm ngang trên "
        "các khay trong tủ, cẩn thận tránh bất kỳ trọng lượng hay áp lực nào lên các bầu "
        "(một lý do cho vị trí nằm ngang). Tránh rung động. Các tông sóng, hoặc vật liệu tương "
        "tự, có thể được dùng làm lót khay để ngăn nhiệt kế lăn. Các nhiệt kế có dải chính "
        "dưới 0&deg;C tốt hơn khi bảo quản thẳng đứng, bầu hướng xuống, ở nơi mát, nhưng "
        "không để nhiệt kế tì lên bầu của nó. Điều này đặc biệt áp dụng cho các nhiệt kế chất "
        "lỏng hữu cơ, vốn cũng nên được che chắn khỏi các nguồn sáng, vì bức xạ tử ngoại "
        "thường có thể làm suy giảm chất lỏng. Nếu đỉnh lòng của một nhiệt kế cồn được giữ ở "
        "nhiệt độ hơi cao hơn phần còn lại của nhiệt kế, thì chất lỏng dễ bay hơi sẽ không "
        "ngưng tụ trong buồng giãn nở."))

    # ========================================================== high accuracy
    b.append(H3("High Accuracy", "Độ chính xác cao"))
    b.append(P(
        "If a higher accuracy than 0.1&deg;C is sought, the user will need to not only consult "
        "the references [4, 5], but also consult their calibration laboratory. Not all "
        "authorities give the same advice on how to achieve higher accuracy. It is important "
        "to apply very consistent procedures in line with the calibration. Below are the more "
        "important factors that will need further consideration.",
        "Nếu tìm kiếm độ chính xác cao hơn 0,1&deg;C, người dùng sẽ cần không chỉ tham khảo "
        "các tài liệu [4, 5], mà còn tham vấn phòng hiệu chuẩn của họ. Không phải mọi cơ quan "
        "đều đưa ra cùng lời khuyên về cách đạt độ chính xác cao hơn. Điều quan trọng là áp "
        "dụng các quy trình rất nhất quán phù hợp với hiệu chuẩn. Dưới đây là các yếu tố quan "
        "trọng hơn sẽ cần xem xét thêm."))
    b.append(R.ul([
        ("Control of the hysteresis effect is important. The thermometers should not be used "
         "for 3 days after being exposed to elevated temperatures. Residual effects may be "
         "detectable for many weeks. That is, temperature measurements must always be made "
         "under rising temperature conditions. Three days is needed for the glass to relax, "
         "and in some cases, prolonged conditioning at a fixed temperature is required."
         if not vi else
         "Kiểm soát hiệu ứng trễ là quan trọng. Các nhiệt kế không nên được dùng trong 3 ngày "
         "sau khi tiếp xúc với nhiệt độ cao. Các hiệu ứng dư có thể phát hiện trong nhiều "
         "tuần. Nghĩa là, các phép đo nhiệt độ luôn phải được thực hiện trong điều kiện nhiệt "
         "độ đang tăng. Cần 3 ngày để thủy tinh thư giãn, và trong một số trường hợp, cần "
         "điều kiện hóa kéo dài ở một nhiệt độ cố định."),
        ("Avoidance of parallax reading errors is important because interpolation of the "
         "finer scale is essential. Optical aids are used, but they increase the parallax "
         "error. Good mechanical alignment is therefore required to keep parallax to a "
         "minimum."
         if not vi else
         "Tránh các sai số đọc theo thị sai là quan trọng vì nội suy thang mịn hơn là thiết "
         "yếu. Các trợ giúp quang học được dùng, nhưng chúng làm tăng sai số thị sai. Do đó "
         "cần một sự căn chỉnh cơ học tốt để giữ thị sai ở mức tối thiểu."),
        ("The pressure on the bulb due to the length of mercury in the stem becomes "
         "important. Thermometers will give different readings in the horizontal and vertical "
         "positions. External pressure variations should also be considered."
         if not vi else
         "Áp suất lên bầu do chiều dài thủy ngân trong thân trở nên quan trọng. Các nhiệt kế "
         "sẽ cho các số đọc khác nhau ở vị trí nằm ngang và thẳng đứng. Các biến thiên áp "
         "suất bên ngoài cũng nên được xem xét."),
        ("In general, total immersion use of the thermometer is required to achieve the higher "
         "accuracy."
         if not vi else
         "Nói chung, cần sử dụng nhiệt kế ngâm toàn phần để đạt được độ chính xác cao hơn."),
    ]))

    # ========================================================= defining terms
    b.append(H3("Defining Terms", "Định nghĩa thuật ngữ"))
    if vi:
        items = [
            ("Cột nổi", "Chiều dài chất lỏng nhiệt kế trong mao quản không ở nhiệt độ cần đo."),
            ("Điểm nước đá", "Sự cân bằng giữa nước đá tan và nước bão hòa khí."),
            ("Chất lỏng nhiệt kế", "Chất lỏng dùng để nạp vào nhiệt kế."),
        ]
    else:
        items = [
            ("Emergent column", "The length of thermometric fluid in the capillary that is "
             "not at the temperature of interest."),
            ("Ice point", "The equilibrium between melting ice and air-saturated water."),
            ("Thermometric liquid", "The liquid used to fill the thermometer."),
        ]
    b.append(R.defs(items))

    b.append(refs(lang))
    return "".join(b)


def sec_vi():
    return _section("vi")


def sec_en():
    return _section("en")
