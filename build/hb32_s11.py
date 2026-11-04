# -*- coding: utf-8 -*-
"""§32.11 Fiber-Optic Thermometers — Brian Culshaw, p154-163."""
import math as _m
import hb32kit as K
R = K.R                      # lazy proxy to reader_hb_ch32 helpers

TITLE_EN = "Fiber-Optic Thermometers"
TITLE_VI = "Nhiệt kế sợi quang"

# Flat (English, Vietnamese, depth) tuples — depth 0 -> h3, 1 -> h4.
# The English strings are exactly those passed to the headings; sec_index()
# builds the TOC links from #s32-11-<slug(english)>, so spelling must match.
SUBS = [
    ("Optical Fiber Sensing", "Cảm biến sợi quang", 0),
    ("Fiber Optic Temperature Sensors", "Cảm biến nhiệt sợi quang", 0),
    ("Fiber Optic Point Temperature Measurement Systems",
     "Hệ đo nhiệt điểm bằng sợi quang", 0),
    ("Fluorescence-Based Probes", "Đầu dò dựa trên huỳnh quang", 1),
    ("Dye and Bandedge Probes", "Đầu dò thuốc nhuộm và cạnh dải", 1),
    ("Fabry–Perot Interferometric Probes", "Đầu dò giao thoa Fabry–Perot", 1),
    ("Optical Fiber Pyrometry", "Đo nhiệt bức xạ bằng sợi quang", 1),
    ("Nanoprobes", "Nano đầu dò", 1),
    ("Vibrating Element Probes", "Đầu dò phần tử rung", 1),
    ("Distributed and Quasi-distributed Optical Fiber Temperature Measurement Systems",
     "Hệ đo nhiệt phân bố và bán phân bố bằng sợi quang", 0),
    ("Raman Scattering Probes", "Đầu dò tán xạ Raman", 1),
    ("Intensity-Based Distributed Alarms", "Báo động phân bố dựa trên cường độ", 1),
    ("Brillouin Scattering", "Tán xạ Brillouin", 1),
    ("Kerr Effect Probes", "Đầu dò hiệu ứng Kerr", 1),
    ("Quasi-Distributed and Multiplexed Systems",
     "Hệ bán phân bố và ghép kênh", 1),
    ("Applications for Optical Fiber Temperature Probes",
     "Ứng dụng của đầu dò nhiệt sợi quang", 0),
    ("Further Information", "Thông tin thêm", 0),
]


# ---------------------------------------------------------------- references
def refs(lang):
    vi = (lang == "vi")
    items = [
        "1. B. Culshaw and J. P. Dakin, <i>Optical Fiber Sensors</i>, Vol. I–IV, "
        "Boston: Artech House, Vol. 1, 1988; Vol. II, 1989; Vols. III and IV, 1997.",
        "2. B. Culshaw, <i>Optical Fiber Sensing and Signal Processing</i>, "
        "Stevenage, UK: IEE/Peter Peregrinus, 1983.",
        "3. International Conferences on Optical Fiber Sensors (OFS), regarded as the "
        "principal forum for the dissemination of research results — OFS(1), London, "
        "1983 to OFS(12), Williamsburg, 1997, various publishers.",
        "4. Proceedings of series of Distributed and Multiplexed Optical Fiber "
        "Sensors and of Laser and Fiber Sensors Conferences, available from SPIE, "
        "Bellingham, Washington.",
        "5. E. Udd (ed.), <i>Optical Fiber Sensors</i>, New York: John Wiley & Sons, 1991.",
    ]
    head_ = ('<h3 id="t32-tltk-11">Tài liệu tham khảo</h3>' if vi else
             '<h3 id="t32-tltk-11">References</h3>')
    return head_ + R.wl(items)


# ------------------------------------------------------------------- where clauses
# §32.11 contains no numbered equations, so the dict is empty.
_W = {}


# ------------------------------------------------------------------- figures
# num -> (cap_vi, cap_en, aria_vi, aria_en, title_vi)
_CAP = {
84: ("Hình 32.84 · Các quá trình quang tuyến tính và phi tuyến dùng cho đo lường "
     "bằng cảm biến sợi quang.",
     "Figure 32.84 · Linear and nonlinear optical processes for measurement using "
     "optical fiber sensors.",
     "Sơ đồ phân loại các quá trình quang tuyến tính và phi tuyến",
     "Classification diagram of linear and nonlinear optical processes",
     "Các quá trình quang tuyến tính và phi tuyến"),
85: ("Hình 32.85 · Đầu ra của hệ cảm biến cho (a) mảng điểm và (b) hệ cảm biến "
     "phân bố.",
     "Figure 32.85 · Sensor system outputs for (a) point array and (b) distributed "
     "sensor systems.",
     "Hai giản đồ đầu ra của mảng điểm và hệ phân bố",
     "Two output diagrams for a point array and a distributed system",
     "Đầu ra hệ cảm biến điểm và phân bố"),
86: ("Hình 32.86 · Nhiệt kế huỳnh quang sợi quang.",
     "Figure 32.86 · Optical fiber fluorescent thermometer.",
     "Sơ đồ đầu dò huỳnh quang sợi quang với nguồn UV và bộ chia tách",
     "Schematic of a fluorescent fiber probe with UV source and splitter",
     "Nhiệt kế huỳnh quang sợi quang"),
87: ("Hình 32.87 · Đo nhiệt sợi quang dùng hốc cộng hưởng Fabry–Perot "
     "nhiệt-độc bản nhỏ.",
     "Figure 32.87 · Optical fiber thermometry using a short temperature-sensitive "
     "Fabry–Perot cavity.",
     "Sơ đồ đầu dò Fabry–Perot với hốc cộng hưởng tại đầu sợi",
     "Schematic of a Fabry–Perot probe with a cavity at the fiber tip",
     "Đo nhiệt Fabry–Perot sợi quang"),
88: ("Hình 32.88 · Đầu dò cho kính hiển vi chui hầm photon và nano optrode.",
     "Figure 32.88 · Probe for photon tunneling microscope and nano optrode.",
     "Sợi quang nhọn dần với đầu mạ kim loại tạo điểm sáng nano",
     "Tapered fiber with a metal-coated tip forming a nanoscale light spot",
     "Nano đầu dò chui hầm photon"),
89: ("Hình 32.89 · Mặt cắt dọc của vi cộng hưởng silic kích thích bằng quang.",
     "Figure 32.89 · Longitudinal section of silicon optically excited "
     "microresonator.",
     "Mặt cắt dọc vi cộng hưởng cơ học kích thích quang học",
     "Longitudinal section of an optically excited mechanical microresonator",
     "Vi cộng hưởng silic kích thích quang"),
90: ("Hình 32.90 · Các quá trình tán xạ phi tuyến nhạy nhiệt trong sợi quang.",
     "Figure 32.90 · Thermally sensitive nonlinear scattering processes in optical "
     "fibers.",
     "Sơ đồ tán xạ Raman và Brillouin với các vạch Stokes và phản Stokes",
     "Diagram of Raman and Brillouin scattering with Stokes and anti-Stokes lines",
     "Các quá trình tán xạ phi tuyến nhạy nhiệt"),
91: ("Hình 32.91 · Đầu dò nhiệt phân bố Raman: sơ đồ nguyên lý cơ bản.",
     "Figure 32.91 · Raman distributed temperature probe: basic schematic.",
     "Sơ đồ khối hệ đo nhiệt phân bố Raman",
     "Block diagram of a Raman distributed temperature probe",
     "Sơ đồ đầu dò nhiệt phân bố Raman"),
92: ("Hình 32.92 · Báo động nhiệt (cháy) phân bố bằng sợi quang.",
     "Figure 32.92 · Fiber optic distributed heat (fire) alarm.",
     "Ống chứa sáp ép sợi quang gây vi uốn khi nóng",
     "A wax-filled tube pressing the fiber to cause microbend on heating",
     "Báo động nhiệt phân bố sợi quang"),
93: ("Hình 32.93 · Đầu dò hiệu ứng Kerr phân bố để đo trường nhiệt độ hoặc "
     "biến dạng.",
     "Figure 32.93 · Distributed Kerr effect probe for temperature or strain field "
     "measurements.",
     "Sơ đồ bơm/thăm dò trên sợi lưỡng chiết để đo trường",
     "Pump/probe schematic on a birefringent fiber for field measurement",
     "Đầu dò hiệu ứng Kerr phân bố"),
}


def _emit_diagram(lang, num, W, H, parts):
    cv, ce, av, ae, tv = _CAP[num]
    return K.diagram(num, W, H, parts, cv, ce, av, ae, lang, tv)


# ----- Figure 32.84 --------------------------------------------------------
def F84(lang):
    W, H = 560, 320
    p = [K._lbl(24, 24, "Các quá trình quang / optical processes", "ts", "start",
                K._fs(9)),
         K._lbl(60, 52, "Tuyến tính / Linear", "tb", "start"),
         K._lbl(360, 52, "Phi tuyến / Nonlinear", "tb", "start")]
    p.append(K._line(280, 70, 280, 280, K.E, 2.0))
    p.append(K._lbl(284, 296, "sợi quang / optical fiber", "ts", "start", K._fs(8)))
    lin = [("Điều biến pha", "Phase"), ("Phân cực", "Polarization"),
           ("Cường độ", "Intensity"), ("Màu (bước sóng)", "Color")]
    nln = [("Huỳnh quang", "Fluorescence"), ("Tán xạ Raman", "Raman scatter"),
           ("Tán xạ Brillouin", "Brillouin")]
    for i, (vn, en) in enumerate(lin):
        y = 70 + i * 52
        p.append(K._blk(40, y, 150, 42, [vn, en], fs=8))
        p.append(K._arr(190, y + 21, 280, y + 21, K.E, sw=1.3))
    for i, (vn, en) in enumerate(nln):
        y = 70 + i * 60
        p.append(K._blk(370, y, 160, 42, [vn, en], fs=8))
        p.append(K._arr(370, y + 21, 280, y + 21, K.E, sw=1.3))
    p.append(K._lbl(24, 312, "hiệu ứng tuyến tính: tần số ra = tần số vào / linear: "
                            "f_out = f_in", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 84, W, H, p)


# ----- Figure 32.85 --------------------------------------------------------
def F85(lang):
    W, H = 560, 300
    p = [K._lbl(24, 26, "(a) Mảng điểm / point array", "tb", "start"),
         K._lbl(300, 26, "(b) Hệ phân bố / distributed", "tb", "start")]
    p.append(K._line(40, 90, 250, 90, K.E, 2.0))
    p.append(K._lbl(40, 78, "sợi / fiber", "ts", "start", K._fs(8)))
    for i, x in enumerate((70, 120, 170, 220)):
        p.append(K._circ(x, 90, 7, K.DARK, K.E, 1.2))
    for i, x in enumerate((70, 120, 170, 220)):
        h = 30 + 42 * (i % 2)
        p.append(K._line(x, 130, x, 130 + h, K.G, 2.0))
        p.append(K._line(x - 6, 130 + h, x + 6, 130 + h, K.G, 2.0))
    p.append(K._lbl(40, 212, "đầu ra rời rạc / discrete outputs", "ts", "start",
                    K._fs(8)))
    p.append(K._line(300, 90, 520, 90, K.E, 2.0))
    p.append(K._lbl(300, 78, "sợi thăm dò / interrogation fiber", "ts", "start",
                    K._fs(8)))
    pts = [(300, 200), (330, 200), (370, 170), (410, 210), (450, 150),
           (490, 190), (520, 200)]
    p.append(K._pl(pts, K.G, 2.0))
    p.append(K._line(300, 230, 520, 230, K.E, 1.0))
    p.append(K._lbl(300, 226, "T(x)", "ts", "start", K._fs(8)))
    p.append(K._lbl(300, 262, "đầu ra liên tục theo vị trí / continuous output vs "
                            "position", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 85, W, H, p)


# ----- Figure 32.86 --------------------------------------------------------
def F86(lang):
    W, H = 560, 250
    p = [K._lbl(24, 22, "Nhiệt kế huỳnh quang / fluorescent thermometer", "tb",
                "start")]
    p.append(K._blk(24, 100, 70, 44, ["Nguồn UV", "UV"], fs=8))
    p.append(K._line(94, 122, 150, 122, K.E, 2.0))
    p.append(K._line(150, 122, 150, 140, K.E, 2.0))
    p.append(K._line(150, 140, 380, 140, K.E, 3.0))
    p.append(K._circ(150, 140, 14, K.FILL, K.E, 1.4))
    p.append(K._lbl(150, 176, "bộ chia / splitter", "ts", "middle", K._fs(8)))
    p.append(K._circ(380, 140, 16, K.DARK, K.E, 1.4))
    p.append(K._lbl(382, 168, "đầu dò huỳnh quang / probe tip", "ts", "middle",
                    K._fs(8)))
    p.append(K._line(150, 126, 150, 70, K.G, 2.0))
    p.append(K._blk(108, 36, 64, 32, ["đỏ / red", "detector"], fs=7))
    p.append(K._blk(190, 36, 64, 32, ["xanh / green", "detector"], fs=7))
    p.append(K._arr(170, 140, 140, 70, K.G, sw=1.2))
    p.append(K._lbl(300, 222, "tỉ số đỏ/xanh ∝ nhiệt độ / red:green ratio ∝ T",
                    "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 86, W, H, p)


# ----- Figure 32.87 --------------------------------------------------------
def F87(lang):
    W, H = 560, 240
    p = [K._lbl(24, 22, "Đo nhiệt Fabry–Perot / FP thermometry", "tb", "start")]
    p.append(K._blk(24, 90, 70, 44, ["Nguồn", "Source"], fs=8))
    p.append(K._line(94, 112, 150, 112, K.E, 2.0))
    p.append(K._line(150, 112, 150, 140, K.E, 2.0))
    p.append(K._line(150, 140, 360, 140, K.E, 3.0))
    p.append(K._line(360, 120, 360, 160, K.E, 2.0))
    p.append(K._line(376, 122, 376, 158, K.E, 2.0))
    p.append(K._lbl(368, 178, "hốc FP / FP cavity", "ts", "middle", K._fs(8)))
    p.append(K._circ(150, 140, 13, K.FILL, K.E, 1.4))
    p.append(K._line(150, 127, 150, 70, K.G, 2.0))
    p.append(K._blk(108, 36, 84, 32, ["Phân tích phổ", "Spectral"], fs=7))
    p.append(K._lbl(300, 215, "độ dài hốc thay đổi theo nhiệt độ / cavity length "
                            "varies with T", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 87, W, H, p)


# ----- Figure 32.88 --------------------------------------------------------
def F88(lang):
    W, H = 560, 240
    p = [K._lbl(24, 22, "Nano đầu dò / nanoprobe", "tb", "start")]
    p.append(K._rect(40, 100, 200, 40, K.FILL, K.E, 1.5))
    p.append(K._poly([(240, 100), (420, 118), (420, 122), (240, 140)], K.FILL,
                      K.E, 1.5))
    p.append(K._poly([(360, 110), (420, 118), (420, 122), (360, 130)], K.DARK,
                      K.E, 1.2))
    p.append(K._lbl(120, 92, "sợi mạ kim loại / metal-coated fiber", "ts", "middle",
                    K._fs(8)))
    p.append(K._circ(420, 120, 10, "none", K.G, 1.6))
    p.append(K._lbl(420, 150, "điểm sáng nano / nano light spot", "ts", "middle",
                    K._fs(8)))
    p.append(K._lbl(24, 210, "đầu nhọn dần tới hàng chục nm / tip tapered to tens "
                            "of nm", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 88, W, H, p)


# ----- Figure 32.89 --------------------------------------------------------
def F89(lang):
    W, H = 560, 250
    p = [K._lbl(24, 22, "Vi cộng hưởng rung kích thích quang / microresonator",
                "tb", "start")]
    p.append(K._rect(40, 150, 480, 60, K.FILL, K.E, 1.5))
    p.append(K._rect(180, 70, 200, 14, K.DARK, K.E, 1.3))
    p.append(K._line(180, 70, 180, 150, K.E, 1.5))
    p.append(K._line(380, 70, 380, 150, K.E, 1.5))
    p.append(K._lbl(280, 60, "phần tử rung / resonator", "ts", "middle", K._fs(8)))
    p.append(K._arr(280, 20, 280, 54, K.E, sw=1.4))
    p.append(K._lbl(290, 30, "kích thích quang / optical drive", "ts", "start",
                    K._fs(8)))
    p.append(K._lbl(40, 232, "tần số cộng hưởng ∝ nhiệt độ / resonant frequency "
                            "∝ T", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 89, W, H, p)


# ----- Figure 32.90 --------------------------------------------------------
def F90(lang):
    W, H = 560, 280
    p = [K._lbl(24, 22, "Các quá trình tán xạ phi tuyến / nonlinear scattering",
                "tb", "start")]
    p.append(K._line(40, 200, 520, 200, K.E, 2.0))
    p.append(K._lbl(40, 190, "sợi quang / fiber", "ts", "start", K._fs(8)))
    p.append(K._blk(24, 80, 70, 40, ["Xung bơm", "Pump"], fs=8))
    p.append(K._arr(94, 100, 200, 200, K.E, sw=1.3))
    p.append(K._arr(300, 200, 300, 110, K.G, sw=1.3))
    p.append(K._arr(360, 200, 360, 80, K.G, sw=1.3))
    p.append(K._lbl(300, 104, "Stokes", "ts", "middle", K._fs(8)))
    p.append(K._lbl(360, 74, "phản Stokes / anti-Stokes", "ts", "middle", K._fs(8)))
    p.append(K._lbl(24, 252, "biên độ tỉ lệ exp(−ΔE/kT) / amplitudes scale as "
                            "exp(−ΔE/kT)", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 90, W, H, p)


# ----- Figure 32.91 --------------------------------------------------------
def F91(lang):
    W, H = 560, 260
    p = [K._lbl(24, 22, "Sơ đồ nhiệt phân bố Raman / Raman DTS schematic", "tb",
                "start")]
    p.append(K._blk(24, 90, 90, 50, ["Laser", "bơm"], fs=8))
    p.append(K._blk(150, 90, 90, 50, ["Bộ ghép", "Coupler"], fs=8))
    p.append(K._blk(290, 90, 120, 50, ["Sợi cần đo", "Fiber under test"], fs=7))
    p.append(K._blk(150, 180, 90, 44, ["OTDR /", "bộ thu"], fs=8))
    p.append(K._blk(290, 180, 120, 44, ["Xử lý", "Processor"], fs=8))
    p.append(K._arr(114, 115, 150, 115, K.E, sw=1.4))
    p.append(K._arr(240, 115, 290, 115, K.E, sw=1.4))
    p.append(K._arr(195, 140, 195, 180, K.G, sw=1.3))
    p.append(K._arr(240, 202, 290, 202, K.G, sw=1.3))
    p.append(K._lbl(24, 240, "nhiệt độ suy ra từ tỉ số Stokes/phản-Stokes / T from "
                            "Stokes/anti-Stokes ratio", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 91, W, H, p)


# ----- Figure 32.92 --------------------------------------------------------
def F92(lang):
    W, H = 560, 250
    p = [K._lbl(24, 22, "Báo động nhiệt phân bố / distributed heat alarm", "tb",
                "start")]
    p.append(K._rect(40, 90, 480, 80, "none", K.E, 1.5))
    p.append(K._rect(44, 94, 472, 72, K.DARK, K.E, 0))
    p.append(K._lbl(50, 86, "sáp / wax", "ts", "start", K._fs(8)))
    p.append(K._line(30, 130, 530, 130, K.E, 2.5))
    p.append(K._lbl(30, 122, "sợi / fiber", "ts", "start", K._fs(8)))
    pts = [(60, 100), (80, 160), (100, 100), (120, 160), (140, 100), (160, 160),
           (180, 100)]
    p.append(K._pl(pts, K.G, 1.6))
    p.append(K._lbl(60, 182, "lõi xoắn / helical binding", "ts", "start", K._fs(8)))
    p.append(K._lbl(300, 222, "khi nóng, sáp nở ép sợi gây vi uốn / heat expands "
                            "wax, microbend", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 92, W, H, p)


# ----- Figure 32.93 --------------------------------------------------------
def F93(lang):
    W, H = 560, 250
    p = [K._lbl(24, 22, "Đầu dò hiệu ứng Kerr / Kerr effect probe", "tb", "start")]
    p.append(K._blk(24, 90, 80, 44, ["Bơm", "Pump"], fs=8))
    p.append(K._blk(120, 90, 80, 44, ["Thăm dò", "Probe"], fs=8))
    p.append(K._blk(240, 90, 160, 44, ["Sợi lưỡng chiết", "Birefringent fiber"],
                    fs=8))
    p.append(K._blk(430, 90, 100, 44, ["Tần số lệch", "Beat freq."], fs=8))
    p.append(K._arr(104, 112, 120, 112, K.E, sw=1.4))
    p.append(K._arr(200, 112, 240, 112, K.E, sw=1.4))
    p.append(K._arr(400, 112, 430, 112, K.G, sw=1.4))
    p.append(K._lbl(24, 172, "chiều dài đập phụ thuộc T và biến dạng / beat length "
                            "depends on T and strain", "ts", "start", K._fs(8)))
    p.append(K._lbl(24, 202, "tần số lệch ∝ nhiệt độ (vắng biến dạng) / offset ∝ T "
                            "when strain-free", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 93, W, H, p)


FIGS = [F84, F85, F86, F87, F88, F89, F90, F91, F92, F93]


# ------------------------------------------------------------------- section
def _section(lang):
    vi = (lang == "vi")
    # Mirror reader_hb_ch32.build(): pin the renderer's language flag so that
    # h3/h4 anchors are derived from the English title on both pages (matching
    # sec_index's TOC links). Without this, calling sec_vi() directly would
    # anchor VI headings on the Vietnamese text.
    R._LANG[0] = lang

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

    b = [R.h2("32.11 Nhiệt kế sợi quang" if vi else "32.11 Fiber-Optic Thermometers",
              "Fiber-Optic Thermometers" if vi else "Nhiệt kế sợi quang")]
    b.append(R.authors("Brian Culshaw", ""))

    # ============================================= Optical fiber sensing
    b.append(H3("Optical Fiber Sensing", "Cảm biến sợi quang"))
    b.append(P(
        "Optical fiber sensing is a remarkably versatile approach to measurement. A "
        "fiber sensor guides light to and from a measurement zone where the light "
        "is modulated by the measurand of interest and returned along the same or a "
        "different optical fiber to a detector at which the optical signal is "
        "interpreted. The measurement zone can be intrinsic within the fiber that "
        "transports the optical signal, or can be extrinsic to the optical waveguide. "
        "The versatility of the fiber sensing medium arises in part because of the "
        "range of optical parameters that can be modulated and in part because of the "
        "diversity of physical phenomena that involve environmentally sensitive "
        "interactions with light.",
        "Cảm biến sợi quang là một phương pháp đo lường cực kỳ đa dụng. Một cảm biến "
        "sợi quang dẫn ánh sáng tới và từ một vùng đo, nơi ánh sáng bị điều biến bởi "
        "đại lượng cần đo và được truyền ngược lại qua cùng một hoặc một sợi quang "
        "khác tới một bộ dò, tại đó tín hiệu quang được giải mã. Vùng đo có thể nội "
        "tại bên trong sợi dẫn tín hiệu quang, hoặc có thể nằm ngoài sóng dẫn quang. "
        "Tính đa dụng của môi trường cảm biến sợi quang bắt nguồn một phần từ dải các "
        "tham số quang có thể điều biến, và một phần từ sự đa dạng của các hiện tượng "
        "vật lý liên quan đến tương tác nhạy cảm với ánh sáng theo môi trường."))
    b.append(P(
        "For example, highly coherent light from a laser source can be introduced "
        "into a fiber and its phase modulated by a parameter of interest. The "
        "resulting phase changes can then be detected interferometrically. The phase "
        "change is simply a modification to the optical path length within the fiber, "
        "and can be modulated by shifts in temperature, strain, external pressure "
        "field or inertial rotation. A well-designed interferometer can detect 10⁻⁷ "
        "radians — equivalent to 10⁻¹⁴ m! The laser light could also be Doppler "
        "shifted through reflection from a moving object. Its state of polarization "
        "can be changed. Its throughput intensity can be modified or the light can be "
        "used to stimulate some secondary emissions, which in turn can be monitored "
        "to produce the relevant optical signal. If the light is incoherent, then its "
        "wavelength distribution (color) can be modified, in addition, of course, to "
        "the possibilities for polarization changes and intensity changes.",
        "Chẳng hạn, ánh sáng kết tính cao từ một nguồn laser có thể được đưa vào sợi "
        "quang và pha của nó bị điều biến bởi một tham số cần quan tâm. Các thay đổi "
        "pha kết quả sau đó có thể được phát hiện bằng phương pháp giao thoa. Sự thay "
        "đổi pha đơn giản chỉ là một sự sửa đổi chiều dài đường truyền quang bên trong "
        "sợi, và có thể bị điều biến bởi sự dịch chuyển nhiệt độ, biến dạng, trường áp "
        "suất ngoài hay sự quay quán tính. Một giao thoa kế thiết kế tốt có thể phát "
        "hiện tới 10⁻⁷ radian — tương đương 10⁻¹⁴ m! Ánh sáng laser cũng có thể bị "
        "dịch Doppler qua phản xạ từ một vật chuyển động. Trạng thái phân cực của nó "
        "có thể thay đổi. Cường độ thông qua có thể bị sửa đổi, hoặc ánh sáng có thể "
        "được dùng để kích thích một số bức xạ thứ cấp, mà sau đó có thể được theo "
        "dõi để tạo ra tín hiệu quang liên quan. Nếu ánh sáng không kết tính, thì phân "
        "bố bước sóng (màu sắc) của nó có thể bị thay đổi, ngoài ra, tất nhiên, còn "
        "có khả năng thay đổi phân cực và cường độ."))
    b.append(P(
        "The physical phenomena capable of imposing this modulation are again many "
        "and varied. They include, for example, periodically bending an optical fiber "
        "to introduce a localized loss that depends on the sharpness of the bend "
        "(usually referred to as microbend loss); changing the relative refractive "
        "indices of the core and the cladding of the optical fiber and thereby "
        "changing the guiding properties and again introducing a loss; modifying an "
        "optical phase delay by introducing a change in refractive index or a change "
        "in physical length; examining changes in birefringence introduced through "
        "modifications to physical stress and/or temperature; using external "
        "indicators to color modulate a broadband source and relate the color "
        "distribution to temperature, chemical activity, etc. These are all linear "
        "effects where the input optical frequency is the same as the output optical "
        "frequency (regarding Doppler shift as a rate of change of phase of an "
        "optical carrier) and where, for a given system setting, the output at all "
        "frequencies is directly proportional to the input.",
        "Các hiện tượng vật lý có khả năng gây ra sự điều biến này cũng rất nhiều và "
        "đa dạng. Chúng bao gồm, thí dụ, uốn định kỳ một sợi quang để tạo ra một tổn "
        "hao cục bộ phụ thuộc vào độ cong (thường gọi là tổn hao vi uốn); thay đổi "
        "chiết suất tương đối của lõi và vỏ bọc của sợi quang từ đó thay đổi tính dẫn "
        "hướng và lại tạo ra tổn hao; sửa đổi một độ trễ pha quang bằng cách gây ra "
        "sự thay đổi chiết suất hoặc sự thay đổi chiều dài vật lý; khảo sát các thay "
        "đổi lưỡng chiết suất gây ra bởi sự biến đổi ứng suất vật lý và/hoặc nhiệt độ; "
        "dùng các chỉ thị bên ngoài để điều biến màu của một nguồn băng rộng và liên "
        "hệ phân bố màu với nhiệt độ, hoạt tính hóa học, v.v. Tất cả những điều này "
        "đều là các hiệu ứng tuyến tính, trong đó tần số quang đầu vào bằng tần số "
        "quang đầu ra (xem dịch Doppler như một tốc độ thay đổi pha của sóng mang "
        "quang) và trong đó, với một cài đặt hệ thống cho trước, đầu ra ở mọi tần số "
        "tỉ lệ thuận trực tiếp với đầu vào."))
    b.append(P(
        "Nonlinear effects are also widely exploited. Of these, the most important "
        "are fluorescence, observed usually in fluorophores external to the optical "
        "fiber, and Raman and Brillouin scattering, usually observed within the fiber "
        "itself. In all these phenomena, the light is absorbed within a material and "
        "re-emitted as a different optical wavelength from the one that was observed. "
        "The difference in optical wavelengths depends on the material and usually on "
        "strain and temperature fields to which the material is subjected. These "
        "major features of optical fiber sensors are encapsulated in Figure 32.84.",
        "Các hiệu ứng phi tuyến cũng được khai thác rộng rãi. Trong số đó, quan trọng "
        "nhất là huỳnh quang, thường được quan sát ở các chất huỳnh quang nằm ngoài "
        "sợi quang, và tán xạ Raman cùng Brillouin, thường được quan sát ngay trong "
        "bản thân sợi. Trong tất cả các hiện tượng này, ánh sáng bị hấp thụ trong một "
        "vật liệu và được phát lại ở một bước sóng quang khác với bước sóng đã quan "
        "sát. Độ lệch bước sóng phụ thuộc vào vật liệu và thường phụ thuộc vào các "
        "trường biến dạng và nhiệt độ mà vật liệu đó chịu tác động. Những đặc điểm "
        "chính của cảm biến sợi quang được tóm tắt trong Hình 32.84."))
    b.append(F84(lang))
    b.append(P(
        "Optical fiber sensors have an additional feature that is unique to the "
        "medium — namely, the ability for intrinsic networking in either distributed, "
        "quasi-distributed/multiplexed, or discrete (point) configurations. The "
        "essential features of these architectures are sketched in Figure 32.85. For "
        "intrinsic sensors, the fiber responds to the measurand throughout its length, "
        "and the output in transmission is an integral of this linear response.",
        "Cảm biến sợi quang có một đặc điểm bổ sung độc đáo của môi trường này — đó là "
        "khả năng kết nối nội tại theo các cấu hình phân bố, bán phân bố/ghép kênh, "
        "hoặc rời rạc (điểm). Các đặc điểm thiết yếu của các kiến trúc này được phác "
        "họa trong Hình 32.85. Đối với cảm biến nội tại, sợi đáp ứng với đại lượng đo "
        "suốt chiều dài của nó, và đầu ra truyền đi là một tích phân của đáp ứng "
        "tuyến tính này."))
    b.append(F85(lang))
    b.append(P(
        "However, using an interrogation scheme in reflection that incorporates a "
        "delay proportional to distance along the fiber enables the system to retrieve "
        "the measurand as a function of position. These are distributed sensors. The "
        "quasi-distributed architecture examines separately identified individual "
        "(usually adjacent) lengths of fiber and extracts the integral of the "
        "measurand along each of these individual lengths. Distributed and "
        "quasi-distributed sensors effectively convolve the measurand field along the "
        "interrogation fiber with a window determined by either the time resolution of "
        "the interrogating electronics (distributed architectures) or the defined "
        "lengths of the individual fiber sections (quasi-distributed systems). Point "
        "and multiplexed systems address the measurement as essentially a point sample "
        "located at a specific distance along the interrogating fiber. All these "
        "architectures can be realized in all optical fiber form and have been "
        "demonstrated to address a very wide range of measurements, often within a "
        "single network.",
        "Tuy nhiên, dùng một sơ đồ thăm dò theo phản xạ có tích hợp một độ trễ tỉ lệ "
        "với khoảng cách dọc theo sợi cho phép hệ thống truy xuất đại lượng đo như một "
        "hàm của vị trí. Đó là các cảm biến phân bố. Kiến trúc bán phân bố khảo sát "
        "riêng rẽ từng đoạn sợi (thường kề nhau) được xác định và trích xuất tích phân "
        "của đại lượng đo dọc theo từng đoạn đó. Cảm biến phân bố và bán phân bố về "
        "hiệu quả thực hiện phép tích chập trường đại lượng đo dọc theo sợi thăm dò "
        "với một cửa sổ được xác định bởi độ phân giải thời gian của điện tử thăm dò "
        "(kiến trúc phân bố) hoặc bởi chiều dài định trước của từng đoạn sợi (hệ bán "
        "phân bố). Các hệ điểm và ghép kênh xem phép đo về cơ bản như một mẫu điểm "
        "nằm ở một khoảng cách xác định dọc theo sợi thăm dò. Tất cả các kiến trúc này "
        "đều có thể được hiện thực hóa hoàn toàn bằng sợi quang và đã được chứng minh "
        "là đáp ứng một dải đo rất rộng, thường trong một mạng đơn."))
    b.append(P(
        "In summary, the optical fiber approach to measurement has the demonstrated "
        "capability to address a wide range of physical, chemical, and biological "
        "parameters. It must take its place alongside other competing technologies "
        "against which its merits must be assessed. The principal benefits of using "
        "fiber optics include:<br>"
        "• Immunity to electromagnetic interference within the sensor system and "
        "within the optical feed and return leads<br>"
        "• The capacity for intrinsic distributed measurements<br>"
        "• Chemical passivity within the sensor system itself and inherent immunity "
        "to corrosion<br>"
        "• Small size, providing a physically, chemically, and electrically "
        "noninvasive measurement system<br>"
        "• Mechanical ruggedness and flexibility: optical fibers are exceptionally "
        "strong and elastic — they can withstand strains of several percent<br>"
        "• High temperature capability — silica melts at over 1500 °C<br>"
        "There remain cost and user acceptability deterrents within the exploitation "
        "of optical fiber sensor technology. Consequently, the majority of field "
        "experience in optical fiber sensors is targeted at addressing the specialized "
        "problems where these aforementioned benefits are paramount. Many of these lie "
        "in the area of temperature measurement.",
        "Tóm lại, phương pháp sợi quang trong đo lường có năng lực đã được chứng minh "
        "để đáp ứng một dải rộng các tham số vật lý, hóa học và sinh học. Nó phải sánh "
        "vai cùng các công nghệ cạnh tranh khác, mà trước chúng những ưu điểm của nó "
        "phải được đánh giá. Các lợi ích chính của việc dùng sợi quang bao gồm:<br>"
        "• Miễn nhiễm với nhiễu điện từ trong hệ cảm biến và trong các dây dẫn cấp và "
        "hoàn lại quang<br>"
        "• Khả năng thực hiện các phép đo phân bố nội tại<br>"
        "• Tính thụ động hóa học trong bản thân hệ cảm biến và miễn nhiễm ăn mòn tự "
        "thân<br>"
        "• Kích thước nhỏ, tạo ra một hệ đo không xâm lấn về mặt vật lý, hóa học và "
        "điện<br>"
        "• Sự bền bỉ và linh hoạt cơ học: sợi quang cực kỳ bền và đàn hồi — chúng chịu "
        "được biến dạng vài phần trăm<br>"
        "• Khả năng chịu nhiệt độ cao — thạch anh nóng chảy trên 1500 °C<br>"
        "Vẫn còn những rào cản về chi phí và sự chấp nhận của người dùng trong việc "
        "khai thác công nghệ cảm biến sợi quang. Do đó, phần lớn kinh nghiệm thực địa "
        "về cảm biến sợi quang nhắm vào giải quyết các bài toán chuyên biệt, nơi những "
        "lợi ích kể trên là tối quan trọng. Nhiều trong số đó thuộc lĩnh vực đo nhiệt "
        "độ."))

    # ============================================= temperature sensor phenomena
    b.append(H3("Fiber Optic Temperature Sensors", "Cảm biến nhiệt sợi quang"))
    b.append(P(
        "The important phenomena that have been exploited in the optical techniques "
        "for temperature measurement include:<br>"
        "• Collection and detection of blackbody radiation<br>"
        "• Changes in refractive index of external media with temperature<br>"
        "• Changes in fluorescence spectra and/or fluorescence rise times with "
        "temperature<br>"
        "• Changes in Raman or Brillouin scatter with temperature<br>"
        "• Phase transitions in carefully selected materials imposing mechanical "
        "modulation on optical fiber transmission properties<br>"
        "• Changes within an optical path length with temperature, either within the "
        "fiber or an external interferometer element<br>"
        "Within these phenomena, Brillouin and Raman scatter and mechanical phase "
        "transitions have been primarily used in distributed measurement systems. Some "
        "distributed measurement/quasi distributed measurement systems based on "
        "modulated phase delay have also been evaluated, although they have yet to "
        "reach commercial reality. The remaining phenomena are almost exclusively used "
        "in point sensor systems.",
        "Các hiện tượng quan trọng đã được khai thác trong các kỹ thuật quang để đo "
        "nhiệt độ bao gồm:<br>"
        "• Thu thập và phát hiện bức xạ vật đen<br>"
        "• Sự thay đổi chiết suất của môi trường bên ngoài theo nhiệt độ<br>"
        "• Sự thay đổi phổ huỳnh quang và/hoặc thời gian trỗi huỳnh quang theo nhiệt "
        "độ<br>"
        "• Sự thay đổi tán xạ Raman hoặc Brillouin theo nhiệt độ<br>"
        "• Sự chuyển pha trong các vật liệu được chọn kỹ lưỡng gây điều biến cơ học "
        "lên tính truyền dẫn của sợi quang<br>"
        "• Sự thay đổi chiều dài đường truyền quang theo nhiệt độ, dù nằm trong sợi "
        "hay trong một phần tử giao thoa ngoài<br>"
        "Trong các hiện tượng này, tán xạ Brillouin và Raman cùng các chuyển pha cơ "
        "học chủ yếu được dùng trong các hệ đo phân bố. Một số hệ đo phân bố/bán phân "
        "bố dựa trên độ trễ pha được điều biến cũng đã được thử nghiệm, dù chúng chưa "
        "đạt đến thực tế thương mại. Các hiện tượng còn lại hầu như chỉ được dùng "
        "trong các hệ cảm biến điểm."))

    # ============================================= point systems
    b.append(H3("Fiber Optic Point Temperature Measurement Systems",
                "Hệ đo nhiệt điểm bằng sợi quang"))
    b.append(P(
        "Point (discrete) fiber-optic thermometers were among the earliest commercial "
        "fiber sensors and remain the most mature segment of the technology. The "
        "techniques below each exploit one of the phenomena listed above — most often "
        "fluorescence, a refractive-index change, or optical phase — within a "
        "localized measurement zone.",
        "Các nhiệt kế sợi quang điểm (rời rạc) thuộc số những cảm biến sợi quang "
        "thương mại sớm nhất và vẫn là phân đoạn trưởng thành nhất của công nghệ. Các "
        "kỹ thuật dưới đây đều khai thác một trong các hiện tượng kể trên — thường là "
        "huỳnh quang, thay đổi chiết suất, hoặc pha quang — trong một vùng đo cục bộ."))

    b.append(H4("Fluorescence-Based Probes", "Đầu dò dựa trên huỳnh quang"))
    b.append(P(
        "One of the first commercial optical fiber sensors was a fluorescence-based "
        "temperature probe introduced in the early 1980s by the Luxtron Corporation "
        "of Mountain View, CA. Successors to these early sensors are still "
        "commercially available and are a very effective, but expensive, approach to "
        "solving specific measurement problems. These include monitoring temperature "
        "profiles in both domestic and industrial microwave ovens, examining "
        "temperatures in power transformer oils, motor/generator windings, and similar "
        "areas where (primarily) the issue is the operation of a reasonably precise "
        "temperature probe within very high electromagnetic fields. In such "
        "circumstances, a metallic probe either distorts the electromagnetic field "
        "significantly (e.g., in microwave ovens) or is subjected to very high levels "
        "of interference, producing spurious readings. Other applications sectors "
        "exploit the small size or chemical passivity of the device, including "
        "operation within corrosive solvents or examination of extremely localized "
        "phenomena such as laser heating or in determining the selectivity of "
        "radiation and diathermy treatments.",
        "Một trong những cảm biến sợi quang thương mại đầu tiên là đầu dò nhiệt dựa "
        "trên huỳnh quang được Luxtron Corporation (Mountain View, CA) giới thiệu vào "
        "đầu thập niên 1980. Các thế hệ kế thừa của những cảm biến sớm này vẫn có bán "
        "thương mại và là một cách tiếp cận rất hiệu quả, nhưng đắt đỏ, để giải quyết "
        "các bài toán đo cụ thể. Chúng bao gồm theo dõi hồ sơ nhiệt độ trong lò vi "
        "sóng gia dụng và công nghiệp, khảo sát nhiệt độ trong dầu máy biến áp, cuộn "
        "dây động cơ/máy phát, và các khu vực tương tự, nơi (chủ yếu) vấn đề là vận "
        "hành một đầu dò nhiệt đủ chính xác trong các trường điện từ rất cao. Trong "
        "hoàn cảnh như vậy, một đầu dò kim loại hoặc làm méo đáng kể trường điện từ "
        "(thí dụ trong lò vi sóng) hoặc bị tác động bởi mức nhiễu rất cao, gây ra các "
        "kết quả đo sai. Các lĩnh vực ứng dụng khác khai thác kích thước nhỏ hoặc tính "
        "thụ động hóa học của thiết bị, kể cả vận hành trong các dung môi ăn mòn hoặc "
        "khảo sát các hiện tượng cực kỳ cục bộ như gia nhiệt bằng laser hay xác định "
        "độ chọn lọc của các phương pháp bức xạ và điều trị nhiệt điện."))
    b.append(P(
        "The principles of the probe are quite simple and are shown in Figure 32.86. "
        "The rare earth phosphor is excited by an ultraviolet light source (which "
        "limits the length of the silica-based feed fiber to a few tens of meters) and "
        "the return spectrum is divided into “red” and “green” components, the "
        "intensity ratios of which are a simple single-valued function of phosphor "
        "temperature. For precision measurement, the detectors and feed fiber require "
        "calibration and, especially for the detectors, the calibration is a function "
        "of ambient temperature. However, this can be resolved through curve fitting "
        "and interrogation of a thermal reference. The instrument, which has now gone "
        "through several generations to improve upon the basic concept, is capable of "
        "accuracies of about ±0.1 °C within subsecond integration times over a "
        "temperature range extending from approximately −50 °C to +200 °C. Since its "
        "introduction, this particular probe has accumulated extensive field "
        "experience in a wide variety of applications and remains among the most "
        "widely exploited fiber optic sensor concepts.",
        "Nguyên lý của đầu dò khá đơn giản và được trình bày trong Hình 32.86. Chất "
        "huỳnh quang đất hiếm được kích thích bởi một nguồn sáng tử ngoại (điều này "
        "giới hạn chiều dài sợi cấp bằng thạch anh ở mức vài chục mét) và phổ phản hồi "
        "được chia thành hai thành phần “đỏ” và “xanh lá”, tỉ lệ cường độ của chúng là "
        "một hàm đơn trị đơn giản của nhiệt độ chất huỳnh quang. Để đo chính xác, các "
        "bộ dò và sợi cấp cần được hiệu chuẩn và, đặc biệt đối với bộ dò, hiệu chuẩn là "
        "một hàm của nhiệt độ môi trường. Tuy nhiên, điều này có thể được giải quyết "
        "qua khớp đường cong và thăm dò một mốc nhiệt. Thiết bị, nay đã trải qua vài "
        "thế hệ để cải tiến khái niệm cơ bản, đạt độ chính xác khoảng ±0,1 °C trong "
        "thời gian tích phân dưới một giây trên dải nhiệt độ từ xấp xỉ −50 °C đến "
        "+200 °C. Kể từ khi ra mắt, đầu dò này đã tích lũy kinh nghiệm thực địa sâu "
        "rộng trong nhiều ứng dụng và vẫn thuộc số những khái niệm cảm biến sợi quang "
        "được khai thác phổ biến nhất."))
    b.append(F86(lang))
    b.append(P(
        "A number of temperature probes based on fluorescence decay time measurements "
        "have also been demonstrated. The level of commercial activity exploiting "
        "these concepts has, to date, been very modest, partly because the accurate "
        "measurement of decay times can be problematic.",
        "Một số đầu dò nhiệt dựa trên đo thời gian suy giảm huỳnh quang cũng đã được "
        "trình diễn. Mức độ hoạt động thương mại khai thác các khái niệm này cho đến "
        "nay vẫn rất khiêm tốn, một phần vì việc đo chính xác thời gian suy giảm có "
        "thể gặp nhiều khó khăn."))

    b.append(H4("Dye and Bandedge Probes", "Đầu dò thuốc nhuộm và cạnh dải"))
    b.append(P(
        "Measuring the temperature response of dyes and other thermally sensitive "
        "color-selective materials can afford a very simple approach to temperature "
        "measurements. Among the most successful of these has been the temperature "
        "probe examining the bandedge of gallium arsenide introduced by ASEA (now "
        "ABB), again in the early 1980s and now transferred to Takaoka. The bandedge "
        "can either be monitored through examining the spectra of induced fluorescence "
        "or through interrogating the absorption characteristics of the material when "
        "subjected to a constant spectrum excitation. The accuracy and temperature "
        "range of this probe are comparable with those of the Luxtron system, and this "
        "particular version of the bandedge probe has the additional benefit of "
        "operating primarily in the near-infrared range of the spectrum, thereby "
        "accessing the best transmission characteristics of the optical fiber medium. "
        "The probe was originally conceived to address ASEA's internal needs in "
        "monitoring electrical power system components. Similar bandedge probes have "
        "also been demonstrated based on absorption edge detection in materials such "
        "as ruby.",
        "Đo đáp ứng nhiệt độ của các thuốc nhuộm và vật liệu chọn lọc màu nhạy nhiệt "
        "khác có thể mang lại một cách tiếp cận rất đơn giản cho phép đo nhiệt độ. "
        "Trong số những cách thành công nhất có đầu dò nhiệt khảo sát cạnh dải của "
        "gali asenua (gallium arsenide) do ASEA (nay là ABB) giới thiệu, cũng vào "
        "đầu thập niên 1980 và nay chuyển giao cho Takaoka. Cạnh dải có thể được theo "
        "dõi qua khảo sát phổ huỳnh quang cảm ứng, hoặc qua thăm dò đặc tính hấp thụ "
        "của vật liệu khi chịu một kích thích phổ không đổi. Độ chính xác và dải "
        "nhiệt độ của đầu dò này tương đương với hệ Luxtron, và phiên bản cạnh dải "
        "này có thêm lợi ích là hoạt động chủ yếu trong vùng hồng ngoại gần của phổ, "
        "nhờ đó tiếp cận đặc tính truyền dẫn tốt nhất của môi trường sợi quang. Đầu dò "
        "ban đầu được hình thành để đáp ứng nhu cầu nội bộ của ASEA trong giám sát các "
        "thành phần hệ thống điện. Các đầu dò cạnh dải tương tự cũng đã được trình diễn "
        "dựa trên phát hiện cạnh hấp thụ trong các vật liệu như ruby."))

    b.append(H4("Fabry–Perot Interferometric Probes",
                "Đầu dò giao thoa Fabry–Perot"))
    b.append(P(
        "Refractometry and interferometry are potential extremely sensitive thermal "
        "probes. Several have been demonstrated, some of which achieve microkelvin "
        "resolution. Interferometric detection or exploitation of sensitive mode "
        "coupling phenomena is the source of this very high sensitivity, although "
        "rarely is such high sensitivity required in practice. The relatively simple "
        "Fabry–Perot probe shown in Figure 32.87 has been introduced commercially with "
        "simplified spectral analysis and a semiconductor source, although as yet its "
        "market penetration has been relatively modest.",
        "Phương pháp đo chiết suất và giao thoa là những đầu dò nhiệt tiềm năng cực "
        "nhạy. Một số đã được trình diễn, trong đó vài cái đạt độ phân giải microkelvin. "
        "Phát hiện giao thoa hoặc khai thác các hiện tượng ghép mode nhạy cảm là nguồn "
        "của độ nhạy rất cao này, dù trong thực tế hiếm khi cần đến độ nhạy cao như "
        "vậy. Đầu dò Fabry–Perot tương đối đơn giản trong Hình 32.87 đã được thương mại "
        "hóa với phân tích phổ đơn giản hóa và một nguồn bán dẫn, dù thị phần của nó "
        "cho đến nay vẫn khá khiêm tốn."))
    b.append(F87(lang))

    b.append(H4("Optical Fiber Pyrometry", "Đo nhiệt bức xạ bằng sợi quang"))
    b.append(P(
        "Optical pyrometry is a well-established approach to measuring temperatures in "
        "the hundreds to thousands of degrees Centigrade. The disappearing filament "
        "pyrometer has been used in this fashion for over half a century. The optical "
        "fiber equivalent has also found a few niche applications. The general form of "
        "such a sensor is to place the blackbody at the end of the fiber and place it "
        "with the fiber into the hot zone. The consequent radiation within the "
        "transmission spectrum of the fiber is then monitored using a semiconductor "
        "photodetector that can be based on III–V materials or silicon. The received "
        "radiation is then primarily within the red and near-infrared from about 600 nm "
        "to, depending on the detector, 1.8 mm. Blackbodies radiate significantly in "
        "this range at temperatures in the hundreds of degrees Centigrade and above. "
        "The most significant success of this approach has been in the fabrication of "
        "the reference standard temperature probe at NIST for temperatures above "
        "1200 °C. This uses a sapphire rather than silica collection fiber because of "
        "its superior optical and thermal properties within the temperature and the "
        "wavelength ranges of interest. It defines these high temperatures with "
        "subdegree precision.",
        "Đo nhiệt bức xạ quang học là một cách tiếp cận đã được thiết lập vững chắc để "
        "đo các nhiệt độ từ hàng trăm đến hàng nghìn độ C. Nhiệt kế dây tóc biến mất "
        "đã được dùng theo cách này hơn nửa thế kỷ. Phương pháp tương đương sợi quang "
        "cũng đã tìm được một vài ứng dụng ngách. Dạng chung của cảm biến như vậy là "
        "đặt vật đen ở đầu sợi và đưa nó cùng sợi vào vùng nóng. Bức xạ kết quả nằm "
        "trong phổ truyền dẫn của sợi sau đó được theo dõi bằng một bộ dò quang bán "
        "dẫn có thể dựa trên vật liệu III–V hoặc silic. Bức xạ thu được khi đó chủ yếu "
        "nằm trong vùng đỏ và hồng ngoại gần từ khoảng 600 nm đến, tùy bộ dò, 1,8 mm. "
        "Vật đen bức xạ đáng kể trong dải này ở các nhiệt độ hàng trăm độ C trở lên. "
        "Thành công quan trọng nhất của cách tiếp cận này là việc chế tạo đầu dò nhiệt "
        "chuẩn tham chiếu tại NIST cho các nhiệt độ trên 1200 °C. Nó dùng một sợi thu "
        "bằng sapphire thay vì thạch anh nhờ các tính chất quang và nhiệt ưu việt hơn "
        "trong dải nhiệt độ và bước sóng quan tâm. Nó xác định các nhiệt độ cao này "
        "với độ chính xác dưới một độ."))

    b.append(H4("Nanoprobes", "Nano đầu dò"))
    b.append(P(
        "Optical fibers also have the capacity to make unique nanoprobes — the "
        "opposite end of the scale by orders of ten from the distributed sensors "
        "discussed below. These (Figure 32.88) are tapered optical fibers with the end "
        "reduced in diameter to tens of nanometers. The tapered region is coated with a "
        "metal, often aluminium or silver, to confine the optical field. This produces "
        "an intense spot of light at the fiber tip which irradiates an area nanometers "
        "in dimensions. The tip can be coated with the dye or the fluorescent thermally "
        "sensitive material and used to monitor temperature over extremely small areas. "
        "This enables thermal profiles within cellular dimensions to be assessed. In "
        "other formats, the same probe can also be used to address chemical activity "
        "and chemical composition.",
        "Sợi quang còn có khả năng tạo ra những nano đầu dò độc đáo — đầu mút trái "
        "ngược của thang đo, chênh nhau hàng chục bậc so với các cảm biến phân bố thảo "
        "luận dưới đây. Chúng (Hình 32.88) là các sợi quang nhọn dần với đầu được thu "
        "nhỏ đường kính xuống hàng chục nanomet. Vùng nhọn dần được phủ một lớp kim "
        "loại, thường là nhôm hoặc bạc, để giam trường quang. Điều này tạo ra một điểm "
        "sáng cường độ cao tại đầu sợi, chiếu sáng một vùng có kích thước nanomet. Đầu "
        "sợi có thể được phủ thuốc nhuộm hoặc vật liệu huỳnh quang nhạy nhiệt và dùng "
        "để theo dõi nhiệt độ trên những vùng cực nhỏ. Điều này cho phép đánh giá các "
        "hồ sơ nhiệt ở kích thước tế bào. Trong các dạng khác, cùng đầu dò này cũng có "
        "thể dùng để tiếp cận hoạt tính hóa học và thành phần hóa học."))
    b.append(F88(lang))

    b.append(H4("Vibrating Element Probes", "Đầu dò phần tử rung"))
    b.append(P(
        "Fiber optic temperature sensing can be realized using a wide variety of "
        "techniques primarily, but not exclusively, based on the variation of optical "
        "properties of materials with temperature. An example of the exceptions is the "
        "optical excited vibrating element probe shown in Figure 32.89. This probe has "
        "been primarily used for pressure measurement and is now available "
        "commercially for pressure assessment down-hole in oil wells. It can also be "
        "configured to exhibit extremely high temperature sensitivity with accuracies "
        "and resolutions in the millikelvin region. It uses the beneficial features of "
        "mechanical resonators and the consequential frequency read-out in parallel "
        "with optomechanical excitation and direct optical interrogation to produce a "
        "probe that can be reliably exploited over interrogation lengths of tens of "
        "kilometers.",
        "Cảm biến nhiệt sợi quang có thể được thực hiện bằng nhiều kỹ thuật đa dạng, "
        "chủ yếu nhưng không hoàn toàn, dựa trên sự biến thiên của các tính chất quang "
        "của vật liệu theo nhiệt độ. Một ví dụ ngoại lệ là đầu dò phần tử rung kích "
        "thích quang trong Hình 32.89. Đầu dò này chủ yếu được dùng để đo áp suất và "
        "nay có bán thương mại cho việc đánh giá áp suất trong giếng dầu (down-hole). "
        "Nó cũng có thể được cấu hình để thể hiện độ nhạy nhiệt cực cao với độ chính "
        "xác và độ phân giải ở mức millikelvin. Nó sử dụng những đặc tính có lợi của "
        "các cộng hưởng cơ học cùng sự đọc tần số hệ quả song song với kích thích cơ-"
        "quang và thăm dò quang trực tiếp, tạo ra một đầu dò có thể khai thác tin cậy "
        "trên các chiều dài thăm dò hàng chục kilomet."))
    b.append(F89(lang))
    b.append(P(
        "Fiber optic point sensors for temperature measurement are now a relatively "
        "mature technology. Most of the devices mentioned above were first introduced "
        "and characterized 10 or more years ago and have since been refined to address "
        "specific applications sectors. They remain expensive, especially when compared "
        "to the ubiquitous thermocouple, but their unique capability for noninvasive "
        "electrically passive interference-immune measurement give them a very specific "
        "market address that cannot be accessed using alternative technologies. Within "
        "these market areas, the probes have been extremely successful.",
        "Các cảm biến điểm sợi quang để đo nhiệt độ nay là một công nghệ tương đối "
        "trưởng thành. Hầu hết các thiết bị kể trên được giới thiệu và đặc trưng hóa "
        "lần đầu hơn 10 năm trước và từ đó đã được tinh chỉnh để đáp ứng các lĩnh vực "
        "ứng dụng cụ thể. Chúng vẫn đắt đỏ, đặc biệt so với cặp nhiệt điện phổ biến, "
        "nhưng khả năng độc đáo của chúng — đo không xâm lấn, thụ động về điện và miễn "
        "nhiễm nhiễu — mang lại một thị trường rất riêng biệt mà không công nghệ thay "
        "thế nào tiếp cận được. Trong các thị trường đó, các đầu dò đã cực kỳ thành "
        "công."))

    # ============================================= distributed systems
    b.append(H3(
        "Distributed and Quasi-distributed Optical Fiber Temperature Measurement "
        "Systems",
        "Hệ đo nhiệt phân bố và bán phân bố bằng sợi quang"))
    b.append(P(
        "These systems all exploit the unique capability for optical fibers to measure "
        "and resolve environmental parameters as a function of position along the "
        "fiber length. This generic technology is unique to optical fiber systems and, "
        "while there are a few commercial distributed temperature sensor systems "
        "available, the research in this sector continues.",
        "Các hệ này đều khai thác khả năng độc đáo của sợi quang để đo và phân giải các "
        "thông số môi trường như một hàm của vị trí dọc theo chiều dài sợi. Công nghệ "
        "tổng quát này là độc nhất của các hệ sợi quang và, dù đã có một vài hệ cảm "
        "biến nhiệt phân bố thương mại, nghiên cứu trong lĩnh vực này vẫn tiếp tục."))

    b.append(H4("Raman Scattering Probes", "Đầu dò tán xạ Raman"))
    b.append(P(
        "The stimulated Raman scatter (SRS) distributed temperature probe is the most "
        "well established of these and, in common with many of the point sensors, was "
        "originally introduced commercially in the late 1980s. The principle "
        "(Figure 32.90) is quite simple. Within the Raman backscatter process (and "
        "also within the spontaneous Brillouin backscatter process), the amplitudes of "
        "the Stokes and anti-Stokes lines are related to the energy gap between these "
        "lines by a simple exp(−ΔE/kT) relationship. Therefore, measuring this ratio "
        "immediately produces the temperature. Furthermore, this ratio is uniquely "
        "related to temperature and cannot be interfered with by the influence of "
        "other external parameters. The system block diagram is shown in Figure 32.91. "
        "The currently available performance from such systems enables resolutions of "
        "around 1 K in integration times of the order of 1 min, with resolution "
        "lengths of one to a few meters over total interrogation lengths of kilometers. "
        "The interrogation can extend to tens of kilometers if either the interrogation "
        "times are increased or the temperature and/or spatial resolutions are relaxed. "
        "The system is available from both European and Japanese manufacturers. The "
        "applications are very specific, as indeed they must be to accommodate an "
        "instrument price that is typically in tens of thousands of dollars. The "
        "instruments have been used in a variety of highly specific areas, ranging "
        "from monitoring temperature profiles in long process ovens to observing the "
        "thermal characteristics within large volumes of concrete during the curing "
        "process.",
        "Đầu dò nhiệt phân bố dựa trên tán xạ Raman kích thích (SRS) là thiết bị được "
        "thiết lập vững chắc nhất trong số này và, cũng như nhiều cảm biến điểm, ban "
        "đầu được thương mại hóa vào cuối thập niên 1980. Nguyên lý (Hình 32.90) khá "
        "đơn giản. Trong quá trình tán xạ ngược Raman (và cả trong quá trình tán xạ "
        "ngược Brillouin tự phát), biên độ của các vạch Stokes và phản Stokes liên hệ "
        "với khe năng lượng giữa chúng bởi một hệ thức exp(−ΔE/kT) đơn giản. Do đó, đo "
        "tỉ số này lập tức cho ra nhiệt độ. Hơn nữa, tỉ số này liên hệ một cách duy "
        "nhất với nhiệt độ và không thể bị nhiễu bởi ảnh hưởng của các tham số ngoại "
        "lai khác. Sơ đồ khối hệ thống được trình bày trong Hình 32.91. Hiệu năng hiện "
        "có của các hệ như vậy cho phép đạt độ phân giải khoảng 1 K trong thời gian tích "
        "phân cỡ 1 phút, với chiều dài phân giải từ một đến vài mét trên tổng chiều dài "
        "thăm dò hàng kilomet. Việc thăm dò có thể mở rộng tới hàng chục kilomet nếu "
        "tăng thời gian thăm dò hoặc nới lỏng độ phân giải nhiệt độ và/hoặc không gian. "
        "Hệ này có bán từ cả nhà sản xuất châu Âu và Nhật Bản. Các ứng dụng rất cụ thể, "
        "và đúng là phải như vậy để gánh được mức giá thường vào khoảng vài chục nghìn "
        "đô-la. Các thiết bị đã được dùng trong nhiều lĩnh vực cực kỳ chuyên biệt, từ "
        "theo dõi hồ sơ nhiệt độ trong các lò nung dài đến quan sát đặc tính nhiệt "
        "trong các khối bê tông lớn trong quá trình ninh kết."))
    b.append(F90(lang))
    b.append(F91(lang))

    b.append(H4("Intensity-Based Distributed Alarms",
                "Báo động phân bố dựa trên cường độ"))
    b.append(P(
        "Distributed temperature alarms triggering on and locating the presence of "
        "either hot or cold spots along the fiber can be realized at significantly "
        "lower costs and have been modestly successful as commercial systems. The "
        "first of these — and probably the simplest — was originally conceived in the "
        "1970s. This uses a simple step index fiber in which the refractive index of "
        "the core material has a different temperature coefficient than that of the "
        "cladding material. The temperature coefficient is designed such that at a "
        "particular threshold temperature, the two indices become equal and thereafter "
        "that of the cladding exceeds that of the core. Within this section, light is "
        "no longer guided. Simple intensity transmittance measurement is then very "
        "sensitive to the occurrence of this threshold temperature at a particular "
        "point along the fiber. If used with an optical time domain reflectometer, the "
        "position at which this first event occurs can be located. This system is now "
        "in use as a temperature alarm on liquefied natural gas storage tanks. Here, "
        "the core and cladding indices for a plastic-clad silica fiber cross at a "
        "temperature in the region of 50 °C. Such temperatures can only be achieved "
        "when a leak occurs. Further, the system has the obvious benefit of intrinsic "
        "safety and total compatibility with use within potentially explosive "
        "atmospheres.",
        "Các báo động nhiệt phân bố kích hoạt và định vị sự xuất hiện của các điểm "
        "nóng hoặc lạnh dọc theo sợi có thể được thực hiện với chi phí thấp hơn đáng "
        "kể và đã đạt thành công khiêm tốn như các hệ thương mại. Thiết bị đầu tiên "
        "trong số đó — và có lẽ đơn giản nhất — được hình thành vào thập niên 1970. Nó "
        "dùng một sợi chỉ số bước đơn giản, trong đó chiết suất của vật liệu lõi có "
        "hệ số nhiệt độ khác với của vật liệu vỏ bọc. Hệ số nhiệt độ được thiết kế sao "
        "cho tại một nhiệt độ ngưỡng xác định, hai chiết suất trở nên bằng nhau và sau "
        "đó chiết suất của vỏ bọc vượt quá của lõi. Trong đoạn này, ánh sáng không còn "
        "được dẫn nữa. Phép đo truyền qua cường độ đơn giản khi đó rất nhạy với sự xuất "
        "hiện nhiệt độ ngưỡng này tại một điểm dọc theo sợi. Nếu dùng cùng một máy phản "
        "xạ miền thời gian quang (OTDR), vị trí xảy ra sự kiện đầu tiên có thể được "
        "định vị. Hệ này nay đang được dùng làm báo động nhiệt trên các bồn chứa khí "
        "thiên nhiên hóa lỏng. Ở đây, các chiết suất lõi và vỏ của một sợi thạch anh "
        "bọc nhựa cắt nhau tại nhiệt độ vùng 50 °C. Nhiệt độ như vậy chỉ có thể đạt "
        "được khi xảy ra rò rỉ. Hơn nữa, hệ có lợi ích hiển nhiên là an toàn nội tại "
        "và hoàn toàn tương thích với sử dụng trong các môi trường có khả năng nổ."))
    b.append(P(
        "A heat — as opposed to cold — alarm system that has also been introduced "
        "commercially is shown in Figure 32.92. In this system, the central tube is "
        "filled with a wax that expands by typically 20% when passing through its "
        "melting point. This expansion in turn forces the optical fiber against the "
        "helical binding, introducing a periodic microbend and thereby increasing the "
        "local loss within the fiber. The wax transition temperatures can be defined "
        "over a relatively wide range (say 30 to 70 °C) and a low-cost OTDR system "
        "enables location of the hot spot to within a few meters. This system presents "
        "a very cost-effective over-heat or fire alarm when such systems are required "
        "and are in intrinsically safe areas or in regions of very high electromagnetic "
        "interference. Again, it is the unique properties of the optical fiber sensing "
        "medium — especially intrinsic safety and electromagnetic immunity — which "
        "provide this system with its market address.",
        "Một hệ báo động nóng — trái ngược với lạnh — cũng đã được thương mại hóa được "
        "trình bày trong Hình 32.92. Trong hệ này, ống trung tâm được đổ đầy sáp, thứ "
        "khi vượt qua điểm nóng chảy thì nở ra khoảng 20%. Sự nở này lần lượt ép sợi "
        "quang vào lõi xoắn, tạo ra một vi uốn định kỳ và nhờ đó làm tăng tổn hao cục "
        "bộ trong sợi. Nhiệt độ chuyển pha của sáp có thể được định nghĩa trong một dải "
        "khá rộng (thí dụ 30 đến 70 °C) và một hệ OTDR giá rẻ cho phép định vị điểm "
        "nóng trong phạm vi vài mét. Hệ này là một báo động quá nhiệt hoặc cháy rất "
        "hiệu quả về chi phí khi cần đến các hệ như vậy và chúng nằm trong các khu vực "
        "an toàn nội tại hoặc vùng nhiễu điện từ rất cao. Một lần nữa, chính những tính "
        "chất độc đáo của môi trường cảm biến sợi quang — đặc biệt là an toàn nội tại "
        "và miễn nhiễm điện từ — mang lại thị trường cho hệ này."))
    b.append(F92(lang))

    b.append(H4("Brillouin Scattering", "Tán xạ Brillouin"))
    b.append(P(
        "Brillouin scatter is very similar in character to Raman scatter except that "
        "in Brillouin scatter the interaction is with an acoustic phonon rather than "
        "an optical phonon. The frequency shifts are then correspondingly "
        "significantly smaller (typically 10 to 15 GHz). Additionally in Brillouin "
        "scatter, the frequency of the scattered light depends on the acoustic "
        "velocities in the medium within which the light is scattering. Consequently, "
        "the Brillouin scatter spectrum is a function of both temperature (through "
        "variations of modulus and density) and strain applied to the optical fiber. "
        "Usually this is exploited as a complex but very effective means for measuring "
        "strain distributions along an optical fiber. The Brillouin scatter "
        "cross-section is much higher than that for Raman scatter so that distributed "
        "strain distributions can be measured over distances well in excess of 100 km. "
        "This measurement is particularly effective when exploiting stimulated "
        "Brillouin scatter that guides the scattered light back toward the source. "
        "However, since the apparent value of strain depends on temperature through "
        "the variation of acoustic velocity with temperature, temperature correction "
        "is required in most practical situations and, in principle, this correction "
        "can be implemented by measuring spontaneous Brillouin scatter and "
        "specifically the intensity ratio of this in the upper and lower sidebands. "
        "This particular correction technique is currently in its infancy, and "
        "accuracies in the degree kelvin range are the current state of the art. The "
        "difficulty in temperature measurement is that the energy gap between the two "
        "sidebands is very small so that the ratio of the amplitudes is close to unity "
        "but must be measured very accurately in order to invert the exponential.",
        "Tán xạ Brillouin rất giống về bản chất với tán xạ Raman, ngoại trừ việc trong "
        "tán xạ Brillouin sự tương tác là với một phonon âm thanh thay vì phonon quang. "
        "Các dịch chuyển tần số khi đó tương ứng nhỏ hơn đáng kể (điển hình 10 đến 15 "
        "GHz). Thêm vào đó, trong tán xạ Brillouin, tần số của ánh sáng tán xạ phụ "
        "thuộc vào vận tốc âm thanh trong môi trường mà ánh sáng đang tán xạ. Do đó, "
        "phổ tán xạ Brillouin là một hàm của cả nhiệt độ (qua sự biến thiên của môđun "
        "và mật độ) và biến dạng tác dụng lên sợi quang. Thông thường điều này được "
        "khai thác như một phương tiện phức tạp nhưng rất hiệu quả để đo phân bố biến "
        "dạng dọc theo sợi quang. Tiết diện tán xạ Brillouin lớn hơn nhiều so với của "
        "Raman, nhờ đó các phân bố biến dạng phân bố có thể được đo trên những khoảng "
        "cách vượt xa 100 km. Phép đo này đặc biệt hiệu quả khi khai thác tán xạ "
        "Brillouin kích thích, vốn dẫn ánh sáng tán xạ ngược trở lại về phía nguồn. Tuy "
        "nhiên, vì giá trị biến dạng biểu kiến phụ thuộc vào nhiệt độ qua sự biến thiên "
        "vận tốc âm thanh theo nhiệt độ, nên trong hầu hết các tình huống thực tế cần "
        "đến hiệu chỉnh nhiệt độ, và về nguyên tắc, hiệu chỉnh này có thể thực hiện "
        "bằng cách đo tán xạ Brillouin tự phát và cụ thể là tỉ số cường độ của nó ở "
        "dải bên trên và dải bên dưới. Kỹ thuật hiệu chỉnh cụ thể này hiện còn ở giai "
        "đoạn sơ khai, và độ chính xác ở mức độ kelvin là trình độ hiện tại. Khó khăn "
        "trong đo nhiệt độ là khe năng lượng giữa hai dải bên rất nhỏ, nên tỉ số biên "
        "độ gần bằng đơn vị nhưng phải được đo cực chính xác để đảo được hàm mũ."))

    b.append(H4("Kerr Effect Probes", "Đầu dò hiệu ứng Kerr"))
    b.append(P(
        "The optical Kerr effect manifests itself as an intensity-dependent "
        "refractive index. Consequently, this nonlinearity gives rise to either second "
        "harmonic generation or sum and difference frequencies. It has been "
        "investigated for distributed temperature sensing using pump:probe "
        "configurations and birefringent fiber from which the beat length is a "
        "function of temperature and strain. This beat length in turn determines the "
        "frequency offset through phase matching conditions of the mixed pump and "
        "probe signal (Figure 32.93). The overall situation is conceptually similar — "
        "this offset frequency depends on temperature and strain although in "
        "principle, dual measurements and adequate calibration can retrieve both, or "
        "alternatively the probe can measure a temperature field in the absence of "
        "strain. Again, the actual experimental results that have been achieved remain "
        "in the laboratory and the accuracies and resolutions are modest.",
        "Hiệu ứng Kerr quang thể hiện như một chiết suất phụ thuộc cường độ. Do đó, "
        "tính phi tuyến này sinh ra hoặc là tạo sóng hài bậc hai, hoặc là các tần số "
        "tổng và hiệu. Nó đã được nghiên cứu cho cảm biến nhiệt phân bố dùng cấu hình "
        "bơm:thăm dò và sợi lưỡng chiết, mà từ đó chiều dài đập là một hàm của nhiệt "
        "độ và biến dạng. Chiều dài đập này lần lượt xác định tần số lệch qua các điều "
        "kiện ghép pha của tín hiệu bơm và thăm dò trộn lẫn (Hình 32.93). Tình huống "
        "tổng thể về mặt khái niệm là tương tự — tần số lệch này phụ thuộc vào nhiệt "
        "độ và biến dạng, dù về nguyên tắc các phép đo kép và hiệu chuẩn thỏa đáng có "
        "thể truy xuất cả hai, hoặc ngược lại đầu dò có thể đo một trường nhiệt độ khi "
        "vắng mặt biến dạng. Một lần nữa, các kết quả thực nghiệm thực tế đạt được vẫn "
        "nằm trong phòng thí nghiệm và độ chính xác cũng như độ phân giải còn khiêm "
        "tốn."))
    b.append(F93(lang))

    b.append(H4("Quasi-Distributed and Multiplexed Systems",
                "Hệ bán phân bố và ghép kênh"))
    b.append(P(
        "In quasi-distributed sensing and point multiplexed systems, temperature "
        "probes have, as yet, been but little exploited. There are many variations on "
        "the basic theme of a marked optical fiber within which the optical "
        "interrogation system measures the optical path length between the marks. "
        "These marks can be introduced using partially reflective gratings, mode "
        "coupling Bragg gratings, partially reflective splices or connectors, low "
        "reflectivity directional couplers, or a multitude of other arrangements. "
        "Similarly, the optical delay between the markings can be measured directly as "
        "an optical or subcarrier phase or indirectly through monitoring dispersion "
        "between adjacent modes typically in low moded or birefringent fibers. Yet "
        "again, the different delays depend on both temperature and strain so that for "
        "temperature measurement, a strain-free mounting is ideal. The context within "
        "which most, if not all, of this class of system has been evaluated is that of "
        "smart structures and here the technique does offer some promise as a means "
        "for deconvolving strain, mechanical, and thermal effects, and assessing "
        "structural integrity. It could also function as a temperature measurement "
        "probe, but to date has been minimally addressed in this application.",
        "Trong cảm biến bán phân bố và các hệ ghép kênh điểm, các đầu dò nhiệt cho "
        "đến nay vẫn ít được khai thác. Có nhiều biến thể của chủ đề cơ bản là một sợi "
        "quang có đánh dấu, trong đó hệ thăm dò quang đo chiều dài đường truyền quang "
        "giữa các dấu. Các dấu này có thể được tạo ra bằng các cách tử phản xạ từng "
        "phần, các cách tử Bragg ghép mode, các mối nối hoặc đầu nối phản xạ từng "
        "phần, các bộ ghép hướng có độ phản xạ thấp, hoặc rất nhiều sắp đặt khác. Tương "
        "tự, độ trễ quang giữa các dấu có thể được đo trực tiếp như một pha quang hoặc "
        "tín hiệu mang phụ, hoặc gián tiếp qua theo dõi tán sắc giữa các mode kề "
        "nhau, thường trong các sợi ít mode hoặc sợi lưỡng chiết. Một lần nữa, các độ "
        "trễ khác nhau phụ thuộc vào cả nhiệt độ và biến dạng, nên để đo nhiệt độ, một "
        "giá lắp không biến dạng là lý tưởng. Bối cảnh mà hầu hết, nếu không nói là "
        "tất cả, lớp hệ này được đánh giá là các kết cấu thông minh, và ở đây kỹ thuật "
        "thực sự hứa hẹn như một phương tiện để tách biệt các hiệu ứng biến dạng, cơ "
        "học và nhiệt, cũng như đánh giá tính toàn vẹn kết cấu. Nó cũng có thể hoạt "
        "động như một đầu dò đo nhiệt, nhưng cho đến nay chỉ được tiếp cận tối thiểu "
        "trong ứng dụng này."))
    b.append(P(
        "In multiplexed systems, the current fashion, again primarily for combined "
        "strain and temperature measurement, is to incorporate arrays of Bragg "
        "gratings used here as wavelength filters rather than as broadband "
        "reflectors. In this configuration, the Bragg grating presents a combined "
        "temperature/strain field at its location encoded within the reflection "
        "wavelength. Multiple addressing schemes can deconvolve temperature and strain "
        "sensitivities. There have also been a few demonstrations of discrete "
        "temperature-sensitive elements inserted at strategic points along an optical "
        "fiber. Of these the use of bandedge shifting in ruby crystals interrogated "
        "using a pulsed source observed in reflection has probably been the most "
        "successful. In this arrangement, the reflectors are replaced by the crystals "
        "and sample the temperature field at these points. The receiver then "
        "determines the return to spectrum as a function of time.",
        "Trong các hệ ghép kênh, trào lưu hiện nay, cũng chủ yếu cho đo đồng thời biến "
        "dạng và nhiệt độ, là tích hợp các mảng cách tử Bragg được dùng ở đây như các "
        "bộ lọc bước sóng thay vì như các bộ phản xạ băng rộng. Trong cấu hình này, "
        "cách tử Bragg thể hiện một trường nhiệt độ/biến dạng kết hợp tại vị trí của nó "
        "được mã hóa trong bước sóng phản xạ. Nhiều sơ đồ định địa chỉ khác nhau có "
        "thể tách biệt các độ nhạy nhiệt độ và biến dạng. Cũng đã có một vài trình diễn "
        "về các phần tử nhạy nhiệt rời rạc được chèn tại các điểm chiến lược dọc theo "
        "một sợi quang. Trong số đó, việc dùng sự dịch chuyển cạnh dải trong các tinh "
        "thể ruby được thăm dò bằng một nguồn xung quan sát theo phản xạ có lẽ là thành "
        "công nhất. Trong sắp đặt này, các bộ phản xạ được thay bằng các tinh thể và "
        "lấy mẫu trường nhiệt độ tại những điểm đó. Bộ thu sau đó xác định phổ phản hồi "
        "như một hàm của thời gian."))

    # ============================================= applications
    b.append(H3("Applications for Optical Fiber Temperature Probes",
                "Ứng dụng của đầu dò nhiệt sợi quang"))
    b.append(P(
        "Instrumentation is a very applications-specific discipline and, in particular "
        "for sensors, a particular technology is usually only relevant in a limited "
        "number of application sectors. As the technology becomes more and more "
        "specialized and expensive, these applications niches become much more tightly "
        "defined.",
        "Chế tạo dụng cụ là một lĩnh vực rất đặc thù theo ứng dụng và, đặc biệt đối với "
        "cảm biến, một công nghệ cụ thể thường chỉ liên quan trong một số lượng hữu hạn "
        "các lĩnh vực ứng dụng. Khi công nghệ trở nên chuyên biệt và đắt đỏ hơn, những "
        "ngách ứng dụng này được xác định chặt chẽ hơn nhiều."))
    b.append(P(
        "For optical fiber sensors and their use in temperature probes, the more "
        "conventional approaches (thermocouples, thermistors, platinum resistance "
        "thermometers, etc.) are always easier and simpler. The fiber optic technology "
        "must exploit one or more of electromagnetic immunity, small size, "
        "noninvasiveness, chemical immunity, or the capacity for distributed "
        "measurement.",
        "Đối với cảm biến sợi quang và việc dùng chúng trong các đầu dò nhiệt, những "
        "cách tiếp cận truyền thống hơn (cặp nhiệt điện, nhiệt điện trở, nhiệt kế điện "
        "trở bạch kim, v.v.) luôn dễ dàng và đơn giản hơn. Công nghệ sợi quang phải "
        "khai thác một hoặc nhiều trong số: miễn nhiễm điện từ, kích thước nhỏ, không "
        "xâm lấn, miễn nhiễm hóa học, hoặc khả năng đo phân bố."))
    b.append(P(
        "Point optical sensors are therefore primarily used as measurement probes in "
        "regions of very high electromagnetic fields, in zone zero intrinsically safe "
        "areas, and as in vivo medical probes. The distributed capability of fiber "
        "sensors is especially relevant in structural monitoring and in other "
        "specialized areas such as measuring the temperature distribution along "
        "underground power lines, tunnels or similar structures or in experimental "
        "circumstances such as the measurement of curing processes in large volumes of "
        "concrete.",
        "Do đó, các cảm biến quang điểm chủ yếu được dùng làm đầu dò đo trong các vùng "
        "trường điện từ rất cao, trong các khu vực an toàn nội tại zone zero, và như "
        "những đầu dò y tế in vivo. Khả năng phân bố của cảm biến sợi quang đặc biệt "
        "liên quan trong giám sát kết cấu và trong các lĩnh vực chuyên biệt khác như "
        "đo phân bố nhiệt độ dọc theo các đường dây điện ngầm, đường hầm hay các kết "
        "cấu tương tự, hoặc trong các tình huống thực nghiệm như đo các quá trình ninh "
        "kết trong những khối bê tông lớn."))
    b.append(P(
        "Fiber optics then is exactly similar to all other sensing techniques — it is "
        "an inappropriate temperature probe for the majority of applications; but for "
        "those for which it is appropriate, it offers a unique and effective solution "
        "to frequently otherwise intractable measurement challenges. As a technology "
        "evolves and becomes both more widely accepted and readily available, the "
        "applications address will no doubt expand.",
        "Sợi quang khi đó hoàn toàn giống với mọi kỹ thuật cảm biến khác — nó là một "
        "đầu dò nhiệt không thích hợp cho đa số các ứng dụng; nhưng đối với những ứng "
        "dụng mà nó thích hợp, nó mang lại một giải pháp độc đáo và hiệu quả cho những "
        "thách thức đo lường thường không thể giải quyết bằng cách khác. Khi một công "
        "nghệ phát triển và trở nên được chấp nhận rộng rãi hơn cũng như dễ tiếp cận "
        "hơn, các ứng dụng mà nó hướng tới chắc chắn sẽ mở rộng."))

    # ============================================= further information
    b.append(H3("Further Information", "Thông tin thêm"))
    b.append(P(
        "Additional information on optical fiber temperature measurements can be "
        "obtained from the following.",
        "Thông tin thêm về các phép đo nhiệt độ bằng sợi quang có thể tìm được từ các "
        "nguồn sau."))

    b.append(refs(lang))
    return "".join(b)


def sec_vi():
    return _section("vi")


def sec_en():
    return _section("en")
