# -*- coding: utf-8 -*-
"""§32.6 Infrared Thermometers — Jacob Fraden, p88-109."""
import math as _m
import hb32kit as K
R = K.R                      # lazy proxy to reader_hb_ch32 helpers

TITLE_EN = "Infrared Thermometers"
TITLE_VI = "Nhiệt kế hồng ngoại"

# Flat (English, Vietnamese, depth) tuples — depth 0 -> h3, 1 -> h4.
# The English strings are exactly those passed to the headings; sec_index()
# builds the TOC links from #s32-6-<slug(english)>, so spelling must match.
SUBS = [
    ("Thermal Radiation: Physical Laws", "Bức xạ nhiệt: các định luật vật lý", 0),
    ("Pyrometry", "Phép đo nhiệt bức xạ (Pyrometry)", 0),
    ("Planck's Law", "Định luật Planck", 0),
    ("Wien's Law", "Định luật Wien", 0),
    ("Stefan–Boltzmann Law", "Định luật Stefan–Boltzmann", 0),
    ("Kirchhoff's Law", "Định luật Kirchhoff", 0),
    ("Emissivity", "Độ phát xạ", 0),
    ("Blackbody", "Vật đen", 0),
    ("Cavity Effect", "Hiệu ứng hốc", 0),
    ("Practical Blackbodies", "Vật đen thực hành", 0),
    ("Detectors for Thermal Radiation", "Đầu dò bức xạ nhiệt", 0),
    ("Classification", "Phân loại", 1),
    ("Quantum Detectors", "Đầu dò lượng tử", 1),
    ("Thermal Detectors", "Đầu dò nhiệt", 1),
    ("Pyrometers", "Nhiệt kế bức xạ (Pyrometer)", 0),
    ("Disappearing Filament Pyrometer", "Nhiệt kế dây tóc biến mất", 1),
    ("Two-color Pyrometer", "Nhiệt kế hai màu", 1),
    ("IR Thermometers", "Nhiệt kế hồng ngoại", 0),
    ("Operating Principle", "Nguyên lý hoạt động", 1),
    ("Continuous Monitoring of Temperature", "Giám sát nhiệt độ liên tục", 1),
    ("Intermittent Monitoring of Temperature", "Giám sát nhiệt độ gián đoạn", 1),
    ("Response Speed", "Tốc độ đáp ứng", 1),
    ("Components of IR Thermometers", "Các thành phần của nhiệt kế hồng ngoại", 1),
    ("Optical Choppers and Shutters", "Bộ chặt chùm và cửa chớp quang học", 1),
    ("Filters and Lenses", "Bộ lọc và thấu kính", 1),
    ("Waveguides", "Ống dẫn sóng", 1),
    ("Error Sources in IR Thermometry", "Nguồn sai số trong đo nhiệt hồng ngoại", 1),
    ("Semiconductor Materials", "Vật liệu bán dẫn", 1),
    ("Medical Applications", "Ứng dụng y tế", 1),
]


# ---------------------------------------------------------------- references
def refs(lang):
    vi = (lang == "vi")
    items = [
        "1. A. Völklein, A. Wiegand, and V. Baier, <i>Sensors and Actuators A</i>, 29, pp: 87-91, 1991.",
        "2. J. Schieferdecker, R. Quad, E. Holzenkämpfer, and M. Schulze, Infrared thermopile "
        "sensors with high sensitivity and very low temperature coefficient. <i>Sensors and "
        "Actuators A</i>, 46-47, 422-427, 1995.",
        "3. J. Fraden, <i>Handbook of Modern Sensors</i>. 2nd ed., Woodbury, NY: AIP Press, 1996.",
        "4. J-S. Shie and P.K. Weng, Fabrication of micro-bolometer on silicon substrate by "
        "anizotropic etching technique. <i>Transducers'91, Int. Conf. Solid-state Sensors and "
        "Actuators</i>, 627-630, 1991.",
        "5. R.A. Wood, Uncooled thermal imaging with silicon focal plane arrays. <i>Proc. SPIE "
        "2020, Infrared Technology XIX</i>, pp: 329-36, 1993.",
        "6. J. Fraden, Active far infrared detectors. In <i>Temperature, Its Measurement and "
        "Control in Science and Industry</i>, Vol. 6, Part 2, New York: American Institute of "
        "Physics, 1992, 831-836.",
        "7. C.J. Mastrangelo and R.S. Muller, Design and performance of constant-temperature "
        "circuits for microbridge-sensor applications. <i>Transducers'91, Int. Conf. Solid-state "
        "Sensors and Actuators</i>, 471-474, 1991.",
        "8. E.O. Doebelin, <i>Measurement Systems. Application and Design</i>, 4th ed., New "
        "York: McGraw-Hill Co., 1990.",
        "9. A.R. Seacord and G.E. Plambeck, Fiber optic ear thermometer. U.S. Patent No. "
        "5,167,235.",
        "10. J. Fraden, Optical system for an infrared thermometer. U.S. Patent No. 5,368,038.",
        "11. D.R. White and J.V. Nicholas, Emissivity and reflection error sources in radiation "
        "thermometry, in <i>Temperature, Its Measurement and Control in Science and Industry</i>, "
        "Vol. 6, Part 2, New York: American Institute of Physics, 1992, 917-922.",
        "12. E.S. Hellman et al., <i>J. Crystal Growth</i>, 81, 38, 1986.",
        "13. M.K. Weilmeier et al., A new optical temperature measurement technique for "
        "semiconductor substrates in molecular beam epitaxy. <i>Can. J. Phys.</i>, 69, "
        "422-426, 1991.",
        "14. J. Fraden, Medical infrared thermometry (review of modern techniques), in "
        "<i>Temperature, Its Measurement and Control in Science and Industry</i>, Vol. 6, Part "
        "2, New York: American Institute of Physics, 1992, 825-830.",
    ]
    head_ = ('<h3 id="t32-tltk-6">Tài liệu tham khảo</h3>' if vi else
             '<h3 id="t32-tltk-6">References</h3>')
    return head_ + R.wl(items)


# ------------------------------------------------------------- where clauses
# (English items, Vietnamese items) keyed by equation number.
_W = {
"32.90": (["where &nbsp;<i>ε</i>(<i>λ</i>) = emissivity of an object",
           "&nbsp;<i>C</i><sub>1</sub> = 3.74 · 10⁻¹² W cm² and <i>C</i><sub>2</sub> = 1.44 cm K are constants",
           "&nbsp;<i>e</i> = base of natural logarithms"],
          ["trong đó &nbsp;<i>ε</i>(<i>λ</i>) = độ phát xạ của vật",
           "&nbsp;<i>C</i><sub>1</sub> = 3,74 · 10⁻¹² W cm² và <i>C</i><sub>2</sub> = 1,44 cm K là các hằng số",
           "&nbsp;<i>e</i> = cơ số của logarit tự nhiên"]),
"32.91": (["where &nbsp;<i>ε</i>(<i>λ</i>), <i>C</i><sub>1</sub>, <i>C</i><sub>2</sub> and <i>e</i> are as in Equation 32.90"],
          ["trong đó &nbsp;<i>ε</i>(<i>λ</i>), <i>C</i><sub>1</sub>, <i>C</i><sub>2</sub> và <i>e</i> như trong Phương trình 32.90"]),
"32.92": (["where &nbsp;<i>λ</i><sub>m</sub> is in µm and <i>T</i> in kelvin"],
          ["trong đó &nbsp;<i>λ</i><sub>m</sub> tính bằng µm và <i>T</i> tính bằng kelvin"]),
"32.93": (["where &nbsp;<i>λ</i><sub>1</sub> and <i>λ</i><sub>2</sub> are the lower and upper bandwidth limits"],
          ["trong đó &nbsp;<i>λ</i><sub>1</sub> và <i>λ</i><sub>2</sub> là giới hạn dưới và trên của dải phổ"]),
"32.94": (["where &nbsp;<i>k</i> = constant",
           "&nbsp;<i>x</i> ≈ (12/<i>λ</i><sub>2</sub>)(1200/<i>T</i>) = 14400/(<i>λ</i><sub>2</sub><i>T</i>)"],
          ["trong đó &nbsp;<i>k</i> = hằng số",
           "&nbsp;<i>x</i> ≈ (12/<i>λ</i><sub>2</sub>)(1200/<i>T</i>) = 14400/(<i>λ</i><sub>2</sub><i>T</i>)"]),
"32.95": (["where &nbsp;σ = 5.67 · 10⁻⁸ W m⁻² K⁻⁴ (Stefan–Boltzmann constant)",
           "&nbsp;<i>A</i> = area of the emitting surface",
           "&nbsp;<i>ε</i> is assumed wavelength independent"],
          ["trong đó &nbsp;σ = 5,67 · 10⁻⁸ W m⁻² K⁻⁴ (hằng số Stefan–Boltzmann)",
           "&nbsp;<i>A</i> = diện tích bề mặt phát xạ",
           "&nbsp;<i>ε</i> được giả định không phụ thuộc bước sóng"]),
"32.96": (["where &nbsp;<i>ε</i> = emissivity, <i>γ</i> = transparency, <i>ρ</i> = reflectivity"],
          ["trong đó &nbsp;<i>ε</i> = độ phát xạ, <i>γ</i> = độ trong suốt, <i>ρ</i> = độ phản xạ"]),
"32.97": (["where &nbsp;<i>n</i> = refractive index of the material"],
          ["trong đó &nbsp;<i>n</i> = chiết suất của vật liệu"]),
"32.98": (["where &nbsp;Φ<sub>0</sub> = incident thermal flux",
           "&nbsp;Φ<sub>x</sub> = flux at thickness <i>x</i>",
           "&nbsp;<i>α</i><sub>λ</sub> = spectral coefficient of absorption"],
          ["trong đó &nbsp;Φ<sub>0</sub> = thông lượng nhiệt tới",
           "&nbsp;Φ<sub>x</sub> = thông lượng tại chiều dày <i>x</i>",
           "&nbsp;<i>α</i><sub>λ</sub> = hệ số hấp thụ phổ"]),
"32.99": (["where &nbsp;<i>ε</i><sub>λ</sub> = spectral emissivity and <i>γ</i><sub>λ</sub> = monochromatic transmissivity"],
          ["trong đó &nbsp;<i>ε</i><sub>λ</sub> = độ phát xạ phổ và <i>γ</i><sub>λ</sub> = độ truyền qua đơn sắc"]),
"32.100": (["where &nbsp;<i>ε</i><sub>b</sub> = surface emissivity of the cavity wall",
            "&nbsp;<i>F</i><sub>r</sub> = flux radiated from area <i>a</i>",
            "&nbsp;<i>F</i><sub>0</sub> = blackbody flux from area <i>a</i>"],
           ["trong đó &nbsp;<i>ε</i><sub>b</sub> = độ phát xạ bề mặt thành hốc",
            "&nbsp;<i>F</i><sub>r</sub> = thông lượng bức xạ từ diện tích <i>a</i>",
            "&nbsp;<i>F</i><sub>0</sub> = thông lượng vật đen từ diện tích <i>a</i>"]),
"32.101": (["where &nbsp;<i>F</i> = combined radiated and reflected flux leaving area <i>a</i>"],
           ["trong đó &nbsp;<i>F</i> = thông lượng tổng (bức xạ cộng phản xạ) thoát khỏi diện tích <i>a</i>"]),
"32.102": (["where &nbsp;<i>ε</i><sub>e</sub> = effective (perceived) emissivity of the cavity aperture"],
           ["trong đó &nbsp;<i>ε</i><sub>e</sub> = độ phát xạ hiệu dụng (cảm nhận) của lỗ hốc"]),
"32.103": (["where &nbsp;ν = frequency of light",
            "&nbsp;<i>h</i> = 6.63 · 10⁻³⁴ J s (or 4.13 · 10⁻¹⁵ eV s) = Planck's constant"],
           ["trong đó &nbsp;ν = tần số ánh sáng",
            "&nbsp;<i>h</i> = 6,63 · 10⁻³⁴ J s (hay 4,13 · 10⁻¹⁵ eV s) = hằng số Planck"]),
"32.104": (["where &nbsp;<i>ρ</i><sub>s</sub> = 1 − <i>ε</i><sub>s</sub> = sensor reflectivity",
            "&nbsp;<i>A</i> = area, <i>ε</i> = object emissivity, <i>T</i> = object temperature"],
           ["trong đó &nbsp;<i>ρ</i><sub>s</sub> = 1 − <i>ε</i><sub>s</sub> = độ phản xạ của cảm biến",
            "&nbsp;<i>A</i> = diện tích, <i>ε</i> = độ phát xạ vật, <i>T</i> = nhiệt độ vật"]),
"32.105": (["where &nbsp;<i>ε</i><sub>s</sub> = emissivity of the sensor surface facing the object"],
           ["trong đó &nbsp;<i>ε</i><sub>s</sub> = độ phát xạ bề mặt cảm biến hướng về vật"]),
"32.106": (["where &nbsp;<i>T</i><sub>s</sub> = sensor surface temperature"],
           ["trong đó &nbsp;<i>T</i><sub>s</sub> = nhiệt độ bề mặt cảm biến"]),
"32.107": (["where &nbsp;Φ = net thermal flux between object and sensor"],
           ["trong đó &nbsp;Φ = thông lượng nhiệt thuần giữa vật và cảm biến"]),
"32.108": (["where &nbsp;<i>P</i> = power supplied by an excitation circuit (AFIR only)",
            "&nbsp;<i>P</i><sub>L</sub> = nonradiative loss due to conduction and convection",
            "&nbsp;<i>m</i>, <i>c</i> = sensor mass and specific heat",
            "&nbsp;Φ = Φ<sub>h</sub> + Φ<sub>b</sub> = net radiative thermal flux"],
           ["trong đó &nbsp;<i>P</i> = công suất cấp từ mạch kích thích (chỉ ở cảm biến AFIR)",
            "&nbsp;<i>P</i><sub>L</sub> = tổn hao phi bức xạ do dẫn nhiệt và đối lưu",
            "&nbsp;<i>m</i>, <i>c</i> = khối lượng và nhiệt dung riêng của cảm biến",
            "&nbsp;Φ = Φ<sub>h</sub> + Φ<sub>b</sub> = thông lượng bức xạ nhiệt thuần"]),
"32.109": (["where &nbsp;<i>α</i> = (d<i>R</i>/d<i>T</i>)/<i>R</i> = temperature coefficient of resistance (TCR)",
            "&nbsp;<i>ε</i> = surface emissivity",
            "&nbsp;<i>Z</i><sub>T</sub> = bolometer thermal resistance",
            "&nbsp;<i>τ</i> = thermal time constant",
            "&nbsp;<i>ω</i> = angular frequency",
            "&nbsp;Δ<i>T</i> = temperature increase of the bolometer"],
           ["trong đó &nbsp;<i>α</i> = (d<i>R</i>/d<i>T</i>)/<i>R</i> = hệ số nhiệt độ của điện trở (TCR)",
            "&nbsp;<i>ε</i> = độ phát xạ bề mặt",
            "&nbsp;<i>Z</i><sub>T</sub> = điện trở nhiệt của bolometer",
            "&nbsp;<i>τ</i> = hằng số thời gian nhiệt",
            "&nbsp;<i>ω</i> = tần số góc",
            "&nbsp;Δ<i>T</i> = độ tăng nhiệt độ của bolometer"]),
"32.110": (["where &nbsp;<i>T</i><sub>s</sub> is held constant by the control circuit after warm-up"],
           ["trong đó &nbsp;<i>T</i><sub>s</sub> được mạch điều khiển giữ không đổi sau giai đoạn khởi động"]),
"32.111": (["where &nbsp;<i>P</i> = electrically supplied power and <i>P</i><sub>L</sub> = nonradiative loss"],
           ["trong đó &nbsp;<i>P</i> = công suất cấp bằng điện và <i>P</i><sub>L</sub> = tổn hao phi bức xạ"]),
"32.112": (["where &nbsp;<i>T</i><sub>a</sub> = ambient temperature and <i>α</i><sub>s</sub> = loss factor"],
           ["trong đó &nbsp;<i>T</i><sub>a</sub> = nhiệt độ môi trường và <i>α</i><sub>s</sub> = hệ số tổn hao"]),
"32.113": (["where &nbsp;<i>V</i> = voltage across the heating resistance <i>R</i>"],
           ["trong đó &nbsp;<i>V</i> = điện áp trên điện trở gia nhiệt <i>R</i>"]),
"32.114": (["where &nbsp;Δ<i>T</i> = constant temperature increase above ambient",
            "&nbsp;<i>α</i><sub>s</sub> = thermal conductivity from the AFIR detector to its housing"],
           ["trong đó &nbsp;Δ<i>T</i> = độ tăng nhiệt không đổi so với môi trường",
            "&nbsp;<i>α</i><sub>s</sub> = độ dẫn nhiệt từ đầu dò AFIR tới vỏ của nó"]),
"32.115": (["where &nbsp;<i>λ</i><sub>f</sub> = filter wavelength",
            "&nbsp;<i>C</i><sub>2</sub> = 1.44 cm K",
            "&nbsp;<i>ε</i><sub>bf</sub> = target emissivity at <i>λ</i><sub>f</sub>"],
           ["trong đó &nbsp;<i>λ</i><sub>f</sub> = bước sóng của kính lọc",
            "&nbsp;<i>C</i><sub>2</sub> = 1,44 cm K",
            "&nbsp;<i>ε</i><sub>bf</sub> = độ phát xạ của mục tiêu tại <i>λ</i><sub>f</sub>"]),
"32.116": (["where &nbsp;<i>γ</i><sub>x</sub>, <i>γ</i><sub>y</sub> = transmission coefficients at λ<sub>x</sub>, λ<sub>y</sub>",
            "&nbsp;<i>ε</i>(<i>λ</i><sub>x</sub>) ≈ <i>ε</i>(<i>λ</i><sub>y</sub>) = surface emissivity"],
           ["trong đó &nbsp;<i>γ</i><sub>x</sub>, <i>γ</i><sub>y</sub> = hệ số truyền qua tại λ<sub>x</sub>, λ<sub>y</sub>",
            "&nbsp;<i>ε</i>(<i>λ</i><sub>x</sub>) ≈ <i>ε</i>(<i>λ</i><sub>y</sub>) = độ phát xạ bề mặt"]),
"32.117": (["where &nbsp;φ = ratio of the thermal radiation sensor outputs at the two wavelengths",
            "&nbsp;<i>T</i><sub>c</sub> = displayed (calculated) temperature"],
           ["trong đó &nbsp;φ = tỉ số tín hiệu của cảm biến tại hai bước sóng",
            "&nbsp;<i>T</i><sub>c</sub> = nhiệt độ hiển thị (tính toán)"]),
"32.118": (["where &nbsp;<i>T</i><sub>c</sub> = calculated object temperature (K)",
            "&nbsp;<i>T</i><sub>s</sub> = sensor surface temperature",
            "&nbsp;Φ = net thermal radiation flux",
            "&nbsp;<i>ε</i>, <i>ε</i><sub>s</sub> = emissivities of object and sensor"],
           ["trong đó &nbsp;<i>T</i><sub>c</sub> = nhiệt độ vật tính được (K)",
            "&nbsp;<i>T</i><sub>s</sub> = nhiệt độ bề mặt cảm biến",
            "&nbsp;Φ = thông lượng bức xạ nhiệt thuần",
            "&nbsp;<i>ε</i>, <i>ε</i><sub>s</sub> = độ phát xạ của vật và của cảm biến"]),
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
48: ("Hình 32.48 · Mật độ phổ tính trong góc khối 1 steradian cho nguồn vật đen (ε = 1) bức xạ "
     "về phía không gian lạnh vô hạn (ở độ không tuyệt đối). Các đường cong ứng với nhiều nhiệt "
     "độ tuyệt đối; trục tung là bức xạ phổ Lλ,b(λ,T) [W m⁻² sr⁻¹ µm⁻¹].",
     "Figure 32.48 · Spectral densities calculated within a solid angle of 1 steradian for "
     "blackbody source (ε = 1) radiation toward infinitely cold space (at absolute zero). Curves "
     "are drawn for several absolute temperatures; the ordinate is the spectral radiance "
     "Lλ,b(λ,T) [W m⁻² sr⁻¹ µm⁻¹].",
     "Các đường cong bức xạ phổ vật đen trên trục log-log ở nhiều nhiệt độ",
     "Log-log blackbody spectral radiance curves at several temperatures",
     "Mật độ bức xạ phổ của vật đen theo bước sóng"),
49: ("Hình 32.49 · Sự phụ thuộc của độ phát xạ vào bước sóng đối với bạc, sắt/vonfram, đồng thau "
     "nhôm và giấy trắng. Vật liệu điện môi có độ phát xạ cao trong vùng hồng ngoại xa, còn kim "
     "loại đánh bóng phát xạ rất kém.",
     "Figure 32.49 · Wavelength dependence of emissivities for silver, iron/tungsten, aluminum "
     "bronze and white paper. Dielectrics have high emissivity in the far-infrared, while "
     "polished metals are very poor emitters.",
     "Bốn đường cong độ phát xạ theo bước sóng", "Four emissivity-vs-wavelength curves",
     "Độ phát xạ theo bước sóng của bốn vật liệu"),
50: ("Hình 32.50 · Độ phát xạ theo hướng của phi kim (A) và kim loại đánh bóng (B). Ở phi kim, ε "
     "giữ gần như không đổi tới khoảng ±70° rồi giảm nhanh về 0 khi góc tiến tới 90°; kim loại "
     "đánh bóng ngược lại có ε thấp ở hướng pháp tuyến và tăng dần ở góc lớn.",
     "Figure 32.50 · Spatial emissivities for a non-metal (A) and a polished metal (B). For "
     "non-metals ε stays nearly constant out to about ±70° and then falls rapidly to zero as the "
     "angle approaches 90°; polished metals instead have low ε along the normal and rising ε at "
     "large angles.",
     "Hai đồ thị độ phát xạ theo góc cho phi kim và kim loại",
     "Two polar-style plots of directional emissivity for a non-metal and a polished metal",
     "Độ phát xạ theo hướng của phi kim và kim loại đánh bóng"),
51: ("Hình 32.51 · Hiệu ứng hốc làm tăng độ phát xạ. Lưu ý εe > εb.",
     "Figure 32.51 · Cavity effect enhances emissivity. Note that εe > εb.",
     "Sơ đồ mặt cắt hốc với các mũi tên thông lượng bức xạ và phản xạ",
     "Cross-section of a cavity with emitted and reflected flux arrows",
     "Hiệu ứng hốc làm tăng độ phát xạ"),
52: ("Hình 32.52 · (A): Vật đen thể rắn dùng các phần tử nhiệt điện. (B): Vật đen nhúng trong bồn "
     "chất lỏng được khuấy.",
     "Figure 32.52 · (A): Solid-state blackbody with thermoelectric elements. (B): Immersed "
     "blackbody.",
     "Hai sơ đồ chế tạo vật đen thực hành", "Two practical blackbody constructions",
     "Hai dạng vật đen thực hành"),
53: ("Hình 32.53 · Dải bước sóng làm việc của một số đầu dò hồng ngoại.",
     "Figure 32.53 · Operating ranges for some infrared detectors.",
     "Các thanh ngang thể hiện dải bước sóng của từng đầu dò",
     "Horizontal bars showing the operating wavelength range of each detector",
     "Dải bước sóng làm việc của các đầu dò hồng ngoại"),
54: ("Hình 32.54 · Trao đổi nhiệt giữa vật và đầu dò bức xạ nhiệt.",
     "Figure 32.54 · Heat exchange between the object and thermal radiation detector.",
     "Hai bề mặt đối diện nhau với các mũi tên thông lượng bức xạ",
     "Two facing surfaces with the exchange fluxes drawn as arrows",
     "Trao đổi nhiệt giữa vật và đầu dò"),
55: ("Hình 32.55 · Cảm biến nhiệt điện bội (thermopile). Các mối nối 'nóng' được lắng đọng trên "
     "màng mỏng, còn các mối nối 'nguội' đặt trên vòng đỡ.",
     "Figure 32.55 · Thermopile sensor. 'Hot' junctions are deposited on a membrane and 'cold' "
     "junctions on the supporting ring.",
     "Hình nhìn từ trên xuống của thermopile với vòng đỡ và màng trung tâm",
     "Top view of a thermopile with a supporting ring and a central membrane",
     "Cấu trúc cảm biến nhiệt điện bội"),
56: ("Hình 32.56 · (A) Phần tử AFIR bức xạ thông lượng nhiệt Φh về phía vỏ và hấp thụ thông "
     "lượng Φb từ vật. (B) Giản đồ thời gian của thông lượng bức xạ, nhiệt độ bề mặt và công "
     "suất cấp.",
     "Figure 32.56 · (A) AFIR element radiates thermal flux Φh toward its housing and absorbs "
     "flux Φb from the object. (B) Timing diagrams for radiative flux, surface temperature, and "
     "supplied power.",
     "Sơ đồ khối AFIR kèm ba giản đồ thời gian",
     "AFIR block diagram with three timing traces",
     "Phần tử AFIR và giản đồ thời gian"),
57: ("Hình 32.57 · Nhiệt kế quang dây tóc biến mất: (A) bản chỉnh tay và (B) bản tự động.",
     "Figure 32.57 · Disappearing filament optical pyrometer: (A): Manual, and (B): automatic "
     "versions.",
     "Hai sơ đồ quang học của nhiệt kế dây tóc biến mất",
     "Two optical layouts of the disappearing-filament pyrometer",
     "Nhiệt kế dây tóc biến mất bản tay và bản tự động"),
58: ("Hình 32.58 · Nhiệt kế không tiếp xúc hai màu. LED và đầu dò quang dùng để đồng bộ vòng quay "
     "của đĩa với đáp ứng của cảm biến.",
     "Figure 32.58 · Two-color, non-contact thermometer. LED and photodetector are for "
     "synchronizing the disk rotation with the sensor response.",
     "Sơ đồ khối nhiệt kế hai màu với đĩa quay mang hai kính lọc",
     "Block diagram of a two-colour thermometer with a rotating two-filter disk",
     "Sơ đồ khối nhiệt kế hai màu"),
59: ("Hình 32.59 · Nhiệt kế hồng ngoại dùng cảm biến bức xạ nhiệt kiểu một chiều (dc).",
     "Figure 32.59 · Infrared thermometer with a dc type of thermal radiation sensor.",
     "Sơ đồ khối nhiệt kế hồng ngoại kiểu một chiều",
     "Block diagram of a dc infrared thermometer",
     "Nhiệt kế hồng ngoại cảm biến một chiều"),
60: ("Hình 32.60 · Nhiệt kế hồng ngoại dùng bộ chặt chùm (chopper).",
     "Figure 32.60 · Infrared thermometer with a chopper.",
     "Sơ đồ khối nhiệt kế hồng ngoại có bộ chặt chùm và đồng bộ quang",
     "Block diagram of a chopped infrared thermometer with optical synchronisation",
     "Nhiệt kế hồng ngoại dùng bộ chặt chùm"),
61: ("Hình 32.61 · (A): Nhiệt kế hồng ngoại dùng cảm biến nhiệt điện (pyroelectric). Lưu ý ống "
     "dẫn sóng được dùng như một phần của hệ quang. (B) Dòng ngõ ra từ cảm biến nhiệt điện.",
     "Figure 32.61 · (A): Infrared thermometer with a pyroelectric sensor. Note that a waveguide "
     "is used as part of an optical system. (B) Output current from a pyroelectric sensor.",
     "Sơ đồ khối nhiệt kế tức thời và đường cong dòng xung giảm dần",
     "Block diagram of an instant thermometer and the decaying output-current spike",
     "Nhiệt kế pyroelectric và dòng ngõ ra"),
62: ("Hình 32.62 · Ánh sáng truyền theo đường zigzag bên trong ống rỗng (A), thanh đặc (B) và sợi "
     "quang (C).",
     "Figure 32.62 · Light inside the barrel (A), rod (B) and fiber-optic (C) propagates on a "
     "zigzag path.",
     "Ba sơ đồ ống dẫn sóng với tia sáng zigzag",
     "Three light-pipe cross-sections with zigzag rays",
     "Ba loại ống dẫn sóng hồng ngoại"),
63: ("Hình 32.63 · Sai số đo nhiệt độ do độ bất định về giá trị độ phát xạ của vật.",
     "Figure 32.63 · Error in temperature measurement resulted from uncertainty in the value of "
     "object's emissivity.",
     "Đồ thị sai số nhiệt độ tăng nhanh khi độ phát xạ giả định lệch khỏi giá trị thực",
     "Temperature error rising steeply as the assumed emissivity departs from the true value",
     "Sai số nhiệt độ do sai độ phát xạ"),
64: ("Hình 32.64 · Nhiệt kế ánh sáng khuếch tán đo nhiệt độ tấm GaAs. (Theo [12].)",
     "Figure 32.64 · Diffused-light thermometer for measuring temperature of GaAs wafers. "
     "(After [12].)",
     "Sơ đồ quang đường đo nhiệt độ tấm bán dẫn bằng ánh sáng khuếch tán",
     "Optical layout of a diffused-light semiconductor wafer thermometer",
     "Nhiệt kế ánh sáng khuếch tán cho tấm GaAs"),
}


def _emit_diagram(lang, num, W, H, parts):
    cv, ce, av, ae, tv = _CAP[num]
    return K.diagram(num, W, H, parts, cv, ce, av, ae, lang, tv)


def _emit_chart(lang, num, W, H, xr, yr, xt, yt, curves, xlab, ylab,
                extra="", pad=(56, 20, 18, 42)):
    cv, ce, av, ae, tv = _CAP[num]
    return K.chart(num, W, H, xr, yr, xt, yt, curves, xlab, ylab,
                   cv, ce, av, ae, lang, tv, extra=extra, pad=pad)


def _planck(lam, T):
    """Spectral radiance in W m⁻² sr⁻¹ µm⁻¹, λ in µm, T in K."""
    try:
        e = _m.exp(14388.0 / (lam * T))
        L = 1.191e8 / (lam ** 5 * (e - 1.0))
        return _m.log10(L) if L > 0 else -4.0
    except OverflowError:
        return -4.0


# ------------------------------------------------------------------- figures
def F48(lang):
    W, H = 560, 330
    xr, yr = (-0.35, 2.05), (-4, 8)
    xt = [(-0.3, "0.5"), (0, "1"), (1, "10"), (2, "100")]
    yt = [(-4, "10⁻⁴"), (-2, "10⁻²"), (0, "1"), (2, "10²"),
          (4, "10⁴"), (6, "10⁶"), (8, "10⁸")]
    temps = [6000, 4000, 2000, 1000, 500, 300]
    classes = ["c1", "c2", "c3", "d1", "c2", "c1"]
    curves, marks = [], []
    for T, cls in zip(temps, classes):
        pts = []
        for i in range(64):
            lg = -0.3 + 2.3 * i / 63.0
            ly = _planck(10 ** lg, T)
            pts.append((lg, max(-4.0, min(8.0, ly))))
        curves.append((pts, cls))
        lp = min(max(2898.0 / T, 0.5), 100.0)
        ly = _planck(lp, T)
        marks.append((_m.log10(lp), ly, "%d K" % T))
    b = _Box(W, H, xr, yr)
    ex = []
    for lx, ly, t in marks:
        if -3.5 < ly < 7.6:
            ex.append(K._lbl(b.x(lx) + 5, b.y(min(ly + 0.5, 8.0)) - 2,
                             t, "ts", "start", K._fs(8)))
    return _emit_chart(lang, 48, W, H, xr, yr, xt, yt, curves,
                       "bước sóng λ (µm, thang log) / wavelength",
                       "Lλ,b (W m⁻² sr⁻¹ µm⁻¹, log)", extra="".join(ex))


def F49(lang):
    W, H = 560, 300
    xr, yr = (0, 16), (0, 1.05)
    xt = [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"),
          (10, "10"), (12, "12"), (14, "14"), (16, "16")]
    yt = [(0.2, "0.2"), (0.4, "0.4"), (0.6, "0.6"), (0.8, "0.8"), (1.0, "1.0")]
    curves = [
        ([(0, .02), (2, .02), (4, .025), (6, .03), (8, .03),
          (10, .035), (12, .04), (14, .04), (16, .045)], "c1"),
        ([(0, .30), (2, .32), (4, .35), (6, .38), (8, .40),
          (10, .42), (12, .44), (14, .45), (16, .46)], "c2"),
        ([(0, .55), (2, .58), (4, .60), (6, .62), (8, .63),
          (10, .64), (12, .65), (14, .66), (16, .66)], "c3"),
        ([(0, .15), (1, .30), (2, .60), (4, .85), (6, .90),
          (8, .92), (10, .92), (12, .92), (14, .92), (16, .92)], "d1"),
    ]
    b = _Box(W, H, xr, yr)
    ex = [
        K._lbl(b.x(13), b.y(.07) - 4, "Bạc / Silver", "ts", "end", K._fs(8)),
        K._lbl(b.x(13), b.y(.49) - 6, "Sắt, vonfram / Iron, tungsten", "ts", "end", K._fs(8)),
        K._lbl(b.x(13), b.y(.69) - 6, "Đồng thau nhôm / Aluminum bronze", "ts", "end", K._fs(8)),
        K._lbl(b.x(7.0), b.y(.97) - 8, "Giấy trắng / White paper", "ts", "middle", K._fs(8)),
    ]
    return _emit_chart(lang, 49, W, H, xr, yr, xt, yt, curves,
                       "bước sóng (µm) / wavelength",
                       "độ phát xạ ε(λ) / emissivity", extra="".join(ex))


def F50(lang):
    W, H = 560, 290
    p = [K._lbl(24, 26, "(A) Phi kim / non-metal", "tb", "start"),
         K._lbl(300, 26, "(B) Kim loại đánh bóng / polished metal", "tb", "start")]
    for x0, kind in ((24, "a"), (300, "b")):
        L, R = x0 + 24, x0 + 244
        top, base = 52, 208
        mid = (L + R) / 2.0
        p.append(K._line(L, 130, R, 130, K.E, 1.2))
        p.append(K._line(mid, top, mid, base, K.E, 1.2))
        for a, lab in ((-90, "-90°"), (-45, "-45°"), (0, "0°"), (45, "45°"), (90, "90°")):
            xx = L + (a + 90) / 180.0 * (R - L)
            p.append(K._line(xx, 126, xx, 134, K.E, 1.0))
            p.append(K._lbl(xx, 148, lab, "ts", "middle", K._fs(7)))
        for e, lab in ((0.5, "0.5"), (1.0, "1.0")):
            p.append(K._lbl(mid - 6, 130 - e * 88 + 3, lab, "ts", "end", K._fs(7)))
        if kind == "a":
            pts = [(-90, .02), (-85, .45), (-70, .88), (-45, .92), (0, .93),
                   (45, .92), (70, .88), (85, .45), (90, .02)]
        else:
            pts = [(-90, .42), (-85, .30), (-70, .16), (-45, .09), (0, .05),
                   (45, .09), (70, .16), (85, .30), (90, .42)]
        pl = [(L + (a + 90) / 180.0 * (R - L), 130 - e * 88) for a, e in pts]
        p.append(K._pl(pl, K.G if kind == "b" else K.E, 2.0))
        p.append(K._lbl(mid, 236, "góc / angle", "ts", "middle", K._fs(8)))
    p.append(K._lbl(24, 272, "ε dao động mạnh theo hướng; ±70° là giới hạn của vùng phát xạ "
                            "khuếch tán / directional emissivity, ±70° diffuse limit",
                     "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 50, W, H, p)


def F51(lang):
    W, H = 560, 300
    p = []
    p.append(K._poly([(70, 80), (70, 250), (490, 250), (490, 80),
                      (340, 80), (280, 232), (220, 80)], K.FILL, K.E, 1.6))
    p.append(K._lbl(280, 66, "lỗ hốc / aperture a", "ts", "middle", K._fs(9)))
    p.append(K._darr(220, 70, 340, 70, K.E, 1.0))
    p.append(K._lbl(120, 196, "Tb, εb", "t", "start", K._fs(11)))
    p.append(K._arr(280, 222, 280, 96, K.E, sw=1.6))
    p.append(K._lbl(290, 140, "εb F0  bức xạ / emitted", "ts", "start", K._fs(8)))
    p.append(K._arr(236, 118, 296, 196, K.G, sw=1.2))
    p.append(K._lbl(150, 128, "(1 − εb) εb F0", "ts", "start", K._fs(8)))
    p.append(K._lbl(24, 280, "εe = εb(2 − εb) > εb  ·  hiệu ứng hốc / cavity effect",
                     "t", "start", K._fs(10)))
    return _emit_diagram(lang, 51, W, H, p)


def F52(lang):
    W, H = 560, 300
    p = [K._lbl(24, 26, "(A) Vật đen thể rắn / solid-state blackbody", "tb", "start")]
    # (A): copper body with conical cavity, thermoelectric pumps, gas ducts
    p.append(K._rect(40, 60, 230, 190, K.FILL, K.E, 1.5))
    p.append(K._poly([(96, 60), (214, 60), (176, 210), (134, 210)], "none", K.E, 1.4))
    p.append(K._lbl(155, 50, "lỗ hốc / aperture", "ts", "middle", K._fs(8)))
    for yy in (86, 130, 174):
        p.append(K._rect(40, yy, 26, 26, K.DARK, K.E, 1.0))
        p.append(K._rect(244, yy, 26, 26, K.DARK, K.E, 1.0))
    p.append(K._lbl(53, 232, "bơm nhiệt điện / thermoelectric heat pumps", "ts", "start", K._fs(7)))
    p.append(K._arr(155, 60, 155, 34, K.G, sw=1.2))
    p.append(K._lbl(160, 40, "khí khô / N2", "ts", "start", K._fs(8)))
    p.append(K._lbl(40, 274, "cảm biến nhiệt độ nhúng / embedded sensors", "ts", "start", K._fs(8)))
    # (B): immersed blackbody
    p.append(K._lbl(300, 26, "(B) Vật đen nhúng / immersed blackbody", "tb", "start"))
    p.append(K._rect(300, 60, 230, 190, K.FILL, K.E, 1.5))
    p.append(K._poly([(360, 60), (470, 60), (440, 214), (390, 214)], "none", K.E, 1.4))
    p.append(K._lbl(415, 50, "lỗ hốc nhỏ / small aperture", "ts", "middle", K._fs(8)))
    p.append(K._rect(312, 72, 206, 30, K.DARK, K.E, 1.0))
    p.append(K._rect(312, 208, 206, 30, K.DARK, K.E, 1.0))
    p.append(K._lbl(415, 91, "bồn chất lỏng khuấy / stirred liquid bath", "ts", "middle", K._fs(8)))
    p.append(K._lbl(415, 227, "gia nhiệt / làm lạnh · ±0,02 °C", "ts", "middle", K._fs(8)))
    p.append(K._lbl(300, 274, "thành mỏng, sơn phát xạ cao / thin walls, high-ε paint",
                     "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 52, W, H, p)


def F53(lang):
    W, H = 560, 300
    p = [K._lbl(24, 26, "Dải bước sóng làm việc / operating wavelength (µm)",
                "ts", "start", K._fs(9))]
    L, R = 150, 520
    # log-ish axis 0.8 .. 40 µm
    def ax(lam):
        return L + (_m.log10(lam) - _m.log10(0.8)) / (_m.log10(40) - _m.log10(0.8)) * (R - L)
    for lam, lab in ((1, "1"), (2, "2"), (5, "5"), (10, "10"), (20, "20"), (40, "40")):
        x = ax(lam)
        p.append(K._line(x, 48, x, 250, K.S, 0.8))
        p.append(K._lbl(x, 42, lab, "ts", "middle", K._fs(8)))
    rows = [
        ("Ge", 0.8, 1.8, "c1"),
        ("PbS", 1.0, 3.0, "c2"),
        ("InAs", 1.0, 3.6, "c3"),
        ("PbSe", 1.5, 5.5, "c1"),
        ("HgCdTe", 2.0, 14.0, "c2"),
        ("PIR (nhiệt / thermal)", 0.8, 40.0, "c3"),
    ]
    for i, (name, a, b, cls) in enumerate(rows):
        y = 66 + i * 34
        col = {"c1": K.E, "c2": K.G, "c3": K.S}[cls]
        p.append(K._rect(ax(a), y, ax(b) - ax(a), 18, col, col, 1.0))
        p.append(K._lbl(L - 8, y + 13, name, "ts", "end", K._fs(9)))
    p.append(K._lbl(24, 282, "cảm biến lượng tử làm lạnh / cryogenic quantum detectors; "
                            "PIR đáp ứng toàn dải / PIR covers the whole band",
                     "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 53, W, H, p)


def F54(lang):
    W, H = 560, 300
    p = []
    p.append(K._rect(60, 60, 90, 200, K.FILL, K.E, 1.6))
    p.append(K._rect(410, 60, 90, 200, K.FILL, K.E, 1.6))
    p.append(K._lbl(105, 50, "vật / object", "tb", "middle"))
    p.append(K._lbl(455, 50, "cảm biến / sensor", "tb", "middle"))
    p.append(K._lbl(105, 150, "Tb, ε", "t", "middle", K._fs(11)))
    p.append(K._lbl(455, 150, "Ts, εs", "t", "middle", K._fs(11)))
    p.append(K._arr(155, 108, 405, 108, K.E, sw=1.6))
    p.append(K._lbl(280, 100, "Φbo = A ε σ T⁴", "ts", "middle", K._fs(9)))
    p.append(K._arr(405, 150, 155, 150, K.G, sw=1.4))
    p.append(K._lbl(280, 144, "Φbr = −(1 − εs) Φbo", "ts", "middle", K._fs(9)))
    p.append(K._arr(405, 200, 155, 200, K.S, sw=1.4))
    p.append(K._lbl(280, 194, "Φs = −A ε εs σ Ts⁴", "ts", "middle", K._fs(9)))
    p.append(K._lbl(24, 282, "Φ = A ε εs σ (T⁴ − Ts⁴) · 100% coupling, không vật thứ ba / no third body",
                     "t", "start", K._fs(9)))
    return _emit_diagram(lang, 54, W, H, p)


def F55(lang):
    W, H = 560, 300
    p = []
    cx, cy = 280, 150
    p.append(K._circ(cx, cy, 116, K.FILL, K.E, 1.6))
    p.append(K._circ(cx, cy, 92, "none", K.E, 1.3))
    p.append(K._circ(cx, cy, 52, K.DARK, K.E, 1.4))
    p.append(K._circ(cx, cy, 30, K.E, K.E, 1.0))
    p.append(K._lbl(cx, cy + 4, "hấp thụ", "ts", "middle", K._fs(8)))
    for i in range(12):
        a = 2 * _m.pi * i / 12.0
        x0, y0 = cx + 56 * _m.cos(a), cy + 56 * _m.sin(a)
        x1, y1 = cx + 104 * _m.cos(a), cy + 104 * _m.sin(a)
        p.append(K._line(x0, y0, x1, y1, K.G, 1.4))
    p.append(K._lbl(cx, 36, "màng mỏng / membrane — mối nối nóng / hot junctions",
                     "ts", "middle", K._fs(8)))
    p.append(K._lbl(cx, 276, "vòng đỡ có khối lượng nhiệt lớn / supporting ring (cold junctions)",
                     "ts", "middle", K._fs(8)))
    p.append(K._arr(500, 80, 366, 80, K.E, sw=1.4))
    p.append(K._lbl(504, 74, "bức xạ IR", "ts", "end", K._fs(8)))
    p.append(K._lbl(24, 282, "Vs tỉ lệ thông lượng tới / output voltage follows incident flux",
                     "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 55, W, H, p)


def F56(lang):
    W, H = 560, 310
    p = [K._lbl(24, 26, "(A) Sơ đồ khối / block diagram", "tb", "start")]
    p.append(K._blk(24, 60, 96, 56, ["Vật /", "Object"], fs=8))
    p.append(K._blk(168, 60, 118, 56, ["Cảm biến", "AFIR"], fs=8))
    p.append(K._blk(168, 150, 118, 56, ["Mạch điều", "khiển / Control"], fs=8))
    p.append(K._blk(336, 60, 118, 56, ["Vỏ /", "Housing"], fs=8))
    p.append(K._arr(120, 88, 168, 88, K.E, sw=1.5))
    p.append(K._lbl(126, 82, "Φb", "ts", "start", K._fs(8)))
    p.append(K._arr(286, 88, 336, 88, K.G, sw=1.5))
    p.append(K._lbl(292, 82, "Φh", "ts", "start", K._fs(8)))
    p.append(K._arr(227, 116, 227, 150, K.E, sw=1.3))
    p.append(K._arr(286, 178, 470, 178, K.E, sw=1.5))
    p.append(K._lbl(474, 172, "tín hiệu ra / output", "ts", "end", K._fs(8)))
    p.append(K._lbl(292, 166, "P, Ts feedback", "ts", "start", K._fs(8)))
    p.append(K._lbl(24, 224, "(B) Giản đồ thời gian / timing diagrams", "tb", "start"))
    x0 = 150
    # flux step
    p.append(K._pl([(x0, 246), (x0 + 60, 246), (x0 + 60, 262),
                    (x0 + 200, 262)], K.E, 1.8))
    p.append(K._lbl(x0 - 6, 254, "Φ", "ts", "end", K._fs(8)))
    p.append(K._lbl(x0 + 210, 262, "Φ → Φ'", "ts", "start", K._fs(7)))
    # constant Ts
    p.append(K._pl([(x0, 274), (x0 + 200, 274)], K.G, 1.8))
    p.append(K._lbl(x0 - 6, 278, "Ts = const", "ts", "end", K._fs(7)))
    # supplied power step
    p.append(K._pl([(x0, 296), (x0 + 60, 296), (x0 + 60, 286),
                    (x0 + 200, 286)], K.S, 1.8))
    p.append(K._lbl(x0 - 6, 296, "P", "ts", "end", K._fs(8)))
    return _emit_diagram(lang, 56, W, H, p)


def F57(lang):
    W, H = 560, 300
    p = [K._lbl(24, 26, "(A) Bản chỉnh tay / manual", "tb", "start")]
    p.append(K._blk(24, 90, 80, 60, ["Mục tiêu", "target"], fs=8))
    p.append(K._rect(150, 84, 12, 72, K.FILL, K.E, 1.3))
    p.append(K._lbl(156, 78, "thấu kính / lens", "ts", "middle", K._fs(7)))
    p.append(K._rect(214, 104, 60, 32, K.DARK, K.E, 1.2))
    p.append(K._lbl(244, 124, "dây tóc W", "ts", "middle", K._fs(7)))
    p.append(K._rect(318, 84, 12, 72, K.FILL, K.G, 1.3))
    p.append(K._lbl(324, 78, "lọc đỏ λf = 0,65 µm", "ts", "middle", K._fs(7)))
    p.append(K._circ(430, 120, 22, "none", K.E, 1.4))
    p.append(K._lbl(430, 124, "mắt", "ts", "middle", K._fs(8)))
    p.append(K._arr(104, 120, 150, 120, K.E, sw=1.3))
    p.append(K._arr(162, 120, 214, 120, K.E, sw=1.3))
    p.append(K._arr(274, 120, 318, 120, K.E, sw=1.3))
    p.append(K._arr(330, 120, 408, 120, K.E, sw=1.3))
    p.append(K._blk(214, 176, 60, 40, ["ắc quy +", "biến trở"], fs=7))
    p.append(K._arr(244, 176, 244, 136, K.G, sw=1.2))
    p.append(K._lbl(24, 240, "cân bằng độ sáng: dây tóc biến mất / balance brightness until the "
                            "filament disappears", "ts", "start", K._fs(8)))
    # (B) automatic
    p.append(K._lbl(300, 26, "(B) Bản tự động / automatic", "tb", "start"))
    for x, y, w, h, lines in ((300, 90, 84, 56, ["Mục tiêu", "target"]),
                              (410, 90, 84, 56, ["Gương quay", "45° chopper"]),
                              (410, 186, 84, 56, ["Cảm biến", "quang"])):
        p.append(K._blk(x, y, w, h, lines, fs=7))
    p.append(K._blk(300, 186, 84, 56, ["µP + dòng", "dây tóc"], fs=7))
    p.append(K._arr(384, 118, 410, 118, K.E, sw=1.3))
    p.append(K._arr(452, 146, 452, 186, K.E, sw=1.3))
    p.append(K._arr(410, 214, 384, 214, K.E, sw=1.3))
    p.append(K._arr(342, 186, 342, 146, K.G, sw=1.2))
    p.append(K._lbl(24, 282, "optocoupler đồng bộ bộ chặt chùm với µP / optocoupler sync",
                     "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 57, W, H, p)


def F58(lang):
    W, H = 560, 280
    p = [K._lbl(24, 26, "Nhiệt kế hai màu / two-colour thermometer", "tb", "start")]
    p.append(K._blk(24, 84, 82, 56, ["Vật /", "Object"], fs=8))
    p.append(K._blk(140, 84, 82, 56, ["Thấu kính", "lens"], fs=8))
    # rotating disk with two filters
    p.append(K._circ(292, 112, 40, K.FILL, K.E, 1.5))
    p.append(K._path("M 292,72 A 40,40 0 0 1 332,112 L 292,112 Z", K.G, 1.2, K.DARK))
    p.append(K._path("M 292,112 L 252,112 A 40,40 0 0 0 292,152 Z", K.G, 1.2, "none"))
    p.append(K._lbl(310, 92, "λx", "ts", "middle", K._fs(8)))
    p.append(K._lbl(272, 138, "λy", "ts", "middle", K._fs(8)))
    p.append(K._lbl(292, 60, "đĩa quay / rotating disk", "ts", "middle", K._fs(8)))
    p.append(K._blk(366, 84, 82, 56, ["Đầu dò", "detector"], fs=8))
    p.append(K._blk(470, 84, 66, 56, ["Tỉ số /", "Tc"], fs=8))
    p.append(K._arr(106, 112, 140, 112, K.E, sw=1.4))
    p.append(K._arr(222, 112, 252, 112, K.E, sw=1.4))
    p.append(K._arr(332, 112, 366, 112, K.E, sw=1.4))
    p.append(K._arr(448, 112, 470, 112, K.E, sw=1.4))
    p.append(K._blk(366, 186, 82, 46, ["LED +", "photodetector"], fs=7))
    p.append(K._arr(407, 186, 407, 144, K.G, sw=1.2))
    p.append(K._lbl(24, 250, "φ = γx ε(λx) Wλx / γy ε(λy) Wλy  ·  Tc không phụ thuộc ε / "
                            "Tc independent of emissivity", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 58, W, H, p)


def F59(lang):
    W, H = 560, 260
    p = [K._lbl(24, 26, "Cảm biến kiểu dc / dc-type sensor", "tb", "start")]
    blocks = [(24, "Thấu kính / lens"), (150, "Thermopile\nIR sensor"),
               (288, "Khuếch đại / amp"), (410, "Thu thập DL /\nDAQ + Tc")]
    for i, (x, lab) in enumerate(blocks):
        p.append(K._blk(x, 90, 104, 60, lab.split("\n"), fs=8))
        if i:
            px = blocks[i - 1][0] + 104
            p.append(K._arr(px, 120, x, 120, K.E, sw=1.5))
    p.append(K._blk(288, 186, 104, 46, ["Cảm biến môi", "trường / ambient"], fs=7))
    p.append(K._arr(340, 186, 340, 152, K.G, sw=1.2))
    p.append(K._lbl(24, 244, "tham chiếu nhiệt độ môi trường / ambient reference; không cần "
                            "chặt chùm / no chopper required", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 59, W, H, p)


def F60(lang):
    W, H = 560, 260
    p = [K._lbl(24, 26, "Cảm biến kiểu ac / ac-type (pyroelectric) sensor", "tb", "start")]
    for x, lab in ((24, "Thấu kính / lens"), (140, "Chopper\n50% duty"),
                   (268, "Pyroelectric\nsensor"), (396, "Amp + µP\n→ Tc")):
        p.append(K._blk(x, 84, 104, 60, lab.split("\n"), fs=8))
    for x1, x2 in ((128, 140), (244, 268), (372, 396)):
        p.append(K._arr(x1, 114, x2, 114, K.E, sw=1.5))
    p.append(K._blk(140, 186, 104, 46, ["optocoupler", "LED + PD"], fs=7))
    p.append(K._arr(192, 186, 192, 146, K.G, sw=1.2))
    p.append(K._lbl(24, 244, "chopper vừa tạo tín hiệu xoay chiều vừa làm mục tiêu tham chiếu / "
                            "chopper doubles as reference target", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 60, W, H, p)


def F61(lang):
    W, H = 560, 290
    p = [K._lbl(24, 26, "(A) Nhiệt kế tức thời / instant thermometer", "tb", "start")]
    for x, lab in ((24, "Ống dẫn sóng /\nwaveguide"), (150, "Cửa chớp /\nshutter"),
                   (276, "Pyroelectric\nsensor"), (402, "Q→V + peak\n→ Tc")):
        p.append(K._blk(x, 76, 108, 58, lab.split("\n"), fs=8))
    for x1, x2 in ((132, 150), (258, 276), (384, 402)):
        p.append(K._arr(x1, 105, x2, 105, K.E, sw=1.4))
    p.append(K._lbl(24, 158, "(B) Dòng ngõ ra / output current", "tb", "start"))
    # exponential spike
    pts = [(60, 250), (78, 250), (86, 190), (98, 214), (116, 232),
           (150, 243), (200, 249), (250, 250)]
    p.append(K._pl(pts, K.E, 1.8))
    p.append(K._line(60, 250, 280, 250, K.E, 1.0))
    p.append(K._lbl(86, 184, "mở cửa chớp / shutter opens", "ts", "start", K._fs(8)))
    p.append(K._lbl(24, 278, "biên độ xung ∝ Φ lúc mở / spike amplitude ∝ flux at opening",
                     "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 61, W, H, p)


def F62(lang):
    W, H = 560, 270
    p = []
    panels = [(24, "(A) Ống rỗng / barrel", "vỏ mạ vàng / gold-plated"),
              (200, "(B) Thanh đặc / rod", "phản xạ toàn phần / TIR"),
              (376, "(C) Sợi quang / fiber", "lõi + vỏ bọc / core + clad")]
    for x0, title, note in panels:
        p.append(K._lbl(x0, 26, title, "tb", "start"))
        p.append(K._rect(x0, 60, 160, 150, K.FILL, K.E, 1.5))
        p.append(K._rect(x0 + 10, 70, 140, 130, "none", K.G, 1.1))
    # zigzag rays for each panel
    for x0 in (24, 200, 376):
        pts = [(x0 + 14, 196), (x0 + 60, 84), (x0 + 106, 196),
               (x0 + 150, 84)]
        p.append(K._pl(pts, K.E, 1.5))
        p.append(K._arr(x0 + 150, 84, x0 + 156, 72, K.E, sw=1.2))
    p.append(K._lbl(24, 232, "(A) ống rỗng đánh bóng, mạ vàng / hollow polished gold-plated tube",
                     "ts", "start", K._fs(8)))
    p.append(K._lbl(200, 232, "(B) thanh ZnSe/AMTIR / solid ZnSe or AMTIR rod",
                     "ts", "start", K._fs(8)))
    p.append(K._lbl(376, 232, "(C) sợi quang / optical fiber", "ts", "start", K._fs(8)))
    p.append(K._lbl(24, 258, "góc vào và góc ra rộng / wide entry and exit angles; không hội tụ / "
                            "not focusing", "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 62, W, H, p)


def F63(lang):
    W, H = 560, 300
    xr, yr = (0.5, 1.0), (0, 180)
    xt = [(0.5, "0.5"), (0.6, "0.6"), (0.7, "0.7"), (0.8, "0.8"),
          (0.9, "0.9"), (1.0, "1.0")]
    yt = [(0, "0"), (40, "40"), (80, "80"), (120, "120"), (160, "160")]
    c1, c2 = [], []
    for i in range(26):
        ea = 0.5 + 0.5 * i / 25.0
        if ea < 0.9:
            err1 = 1000 * ((0.9 / ea) ** 0.25 - 1.0)
            err2 = 500 * ((0.9 / ea) ** 0.25 - 1.0)
        else:
            err1 = err2 = 0.0
        c1.append((ea, err1))
        c2.append((ea, err2))
    b = _Box(W, H, xr, yr)
    ex = [K._line(b.x(0.9), b.y(0), b.x(0.9), b.y(180), K.G, 1.1, "5 4"),
          K._lbl(b.x(0.9) + 6, b.y(170), "ε thực = 0.9 / true ε", "ts", "start", K._fs(8)),
          K._lbl(b.x(0.56), b.y(150), "Tb = 1000 K", "ts", "start", K._fs(8)),
          K._lbl(b.x(0.56), b.y(74), "Tb = 500 K", "ts", "start", K._fs(8))]
    return _emit_chart(lang, 63, W, H, xr, yr, xt, yt,
                       [(c1, "c1"), (c2, "c2")],
                       "độ phát xạ giả định / assumed emissivity εa",
                       "sai số nhiệt độ (K) / temperature error (K)",
                       extra="".join(ex))


def F64(lang):
    W, H = 560, 280
    p = [K._lbl(24, 26, "Nhiệt kế ánh sáng khuếch tán / diffused-light thermometer",
                "tb", "start")]
    p.append(K._blk(24, 90, 92, 56, ["Đèn ngoài", "external lamp"], fs=7))
    p.append(K._blk(150, 90, 110, 56, ["Đơn sắc kế", "monochromator"], fs=7))
    p.append(K._rect(300, 76, 90, 84, K.FILL, K.E, 1.5))
    p.append(K._lbl(345, 112, "tấm GaAs", "ts", "middle", K._fs(8)))
    p.append(K._lbl(345, 130, "mặt trước bóng", "ts", "middle", K._fs(7)))
    p.append(K._lbl(345, 146, "mặt sau nhám", "ts", "middle", K._fs(7)))
    p.append(K._blk(430, 90, 104, 56, ["Đầu dò lượng", "tử làm lạnh"], fs=7))
    p.append(K._arr(116, 118, 150, 118, K.E, sw=1.4))
    p.append(K._arr(260, 118, 300, 118, K.E, sw=1.4))
    p.append(K._arr(390, 118, 430, 118, K.G, sw=1.4))
    p.append(K._lbl(392, 112, "ánh sáng khuếch tán", "ts", "start", K._fs(7)))
    p.append(K._blk(300, 186, 90, 42, ["Bếp gia nhiệt", "heater"], fs=7))
    p.append(K._arr(345, 186, 345, 162, K.S, sw=1.2))
    p.append(K._lbl(24, 248, "độ phân giải 3 nm, quét 100 nm/s / resolution 3 nm, scan 100 nm/s "
                            "· ngưỡng bước sóng suy ra T / threshold wavelength gives T",
                     "ts", "start", K._fs(8)))
    return _emit_diagram(lang, 64, W, H, p)


FIGS = [F48, F49, F50, F51, F52, F53, F54, F55, F56, F57, F58,
        F59, F60, F61, F62, F63, F64]


# -------------------------------------------------------------------- tables
def _t3217(lang):
    vi = (lang == "vi")
    hd = (["Vật liệu", "ε", "Vật liệu", "ε"] if vi else
          ["Material", "Emissivity", "Material", "Emissivity"])
    rows = [
        ["Blackbody (ideal)" if not vi else "Vật đen (lý tưởng)", "1.00",
         "Green leaves" if not vi else "Lá xanh", "0.88"],
        ["Cavity radiator" if not vi else "Bộ phát xạ hốc", "0.99–1.00",
         "Ice" if not vi else "Nước đá", "0.96"],
        ["Aluminum (anodized)" if not vi else "Nhôm (anod hóa)", "0.70",
         "Iron or steel (rusted)" if not vi else "Sắt hoặc thép (gỉ)", "0.70"],
        ["Aluminum (oxidized)" if not vi else "Nhôm (oxit hóa)", "0.11",
         "Nickel (oxidized)" if not vi else "Niken (oxit hóa)", "0.40"],
        ["Aluminum (polished)" if not vi else "Nhôm (đánh bóng)", "0.05",
         "Nickel (unoxidized)" if not vi else "Niken (không oxit)", "0.04"],
        ["Aluminum (rough surface)" if not vi else "Nhôm (bề mặt nhám)", "0.06–0.07",
         "Nichrome (80Ni-20Cr), oxidized" if not vi else "Nichrome (80Ni-20Cr), oxit hóa", "0.97"],
        ["Asbestos" if not vi else "Amiăng", "0.96",
         "Nichrome (80Ni-20Cr), polished" if not vi else "Nichrome (80Ni-20Cr), đánh bóng", "0.87"],
        ["Brass (dull tarnished)" if not vi else "Đồng thau (xỉn)", "0.61",
         "Oil" if not vi else "Dầu", "0.80"],
        ["Brass (polished)" if not vi else "Đồng thau (đánh bóng)", "0.05",
         "Silicon" if not vi else "Silic", "0.64"],
        ["Brick" if not vi else "Gạch", "0.90",
         "Silicone rubber" if not vi else "Cao su silicone", "0.94"],
        ["Bronze (polished)" if not vi else "Đồng điếu (đánh bóng)", "0.10",
         "Silver (polished)" if not vi else "Bạc (đánh bóng)", "0.02"],
        ["Carbon-filled latex paint" if not vi else "Sơn latex pha than", "0.96",
         "Skin (human)" if not vi else "Da (người)", "0.93–0.96"],
        ["Carbon lamp black" if not vi else "Muội đèn than", "0.96",
         "Snow" if not vi else "Tuyết", "0.85"],
        ["Chromium (polished)" if not vi else "Crom (đánh bóng)", "0.10",
         "Soil" if not vi else "Đất", "0.90"],
        ["Copper (oxidized)" if not vi else "Đồng (oxit hóa)", "0.6–0.7",
         "Stainless steel (buffed)" if not vi else "Thép không gỉ (đánh bóng)", "0.20"],
        ["Copper (polished)" if not vi else "Đồng (đánh bóng)", "0.02",
         "Steel (flat rough surface)" if not vi else "Thép (mặt phẳng nhám)", "0.95–0.98"],
        ["Cotton cloth" if not vi else "Vải bông", "0.80",
         "Steel (ground)" if not vi else "Thép (mài)", "0.56"],
        ["Epoxy resin" if not vi else "Nhựa epoxy", "0.95",
         "Tin plate" if not vi else "Tấm thiếc", "0.10"],
        ["Glass" if not vi else "Thủy tinh", "0.95",
         "Water" if not vi else "Nước", "0.96"],
        ["Gold" if not vi else "Vàng", "0.02",
         "White paper" if not vi else "Giấy trắng", "0.92"],
        ["Gold-black" if not vi else "Vàng đen", "0.98–0.99",
         "Wood" if not vi else "Gỗ", "0.93"],
        ["Graphite" if not vi else "Than chì", "0.7–0.8",
         "Zinc (polished)" if not vi else "Kẽm (đánh bóng)", "0.04"],
    ]
    cap = ("Bảng 32.17 · Độ phát xạ điển hình của các vật liệu khác nhau (từ 0 đến 100 °C). "
           "Giá trị của vật đục (γ = 0)." if vi else
           "Table 32.17 · Typical Emissivities of Different Materials (from 0 to 100 °C). "
           "Values are for opaque materials (γ = 0).")
    return R.table(hd, rows, cap, small=True)


def _t3218(lang):
    vi = (lang == "vi")
    hd = (["Vật liệu", "n", "r", "Bước sóng (µm)", "Ghi chú"] if vi else
          ["Material", "n", "r", "Wavelength (µm)", "Note"])
    mat = [
        ("AMTIR-1 (Ge33As12Se55)", "AMTIR-1 (Ge33As12Se55)"),
        ("AMTIR-1 (Ge33As12Se55)", "AMTIR-1 (Ge33As12Se55)"),
        ("AMTIR-3 (Ge28Sb12Se60)", "AMTIR-3 (Ge28Sb12Se60)"),
        ("As2S3", "As2S3"),
        ("CdTe", "CdTe"),
        ("Diamond", "Kim cương"),
        ("Fused silica (SiO2)", "Thạch anh nóng chảy (SiO2)"),
        ("GaAs", "GaAs"),
        ("Germanium", "Gecmani"),
        ("Irtran 2 (ZnS)", "Irtran 2 (ZnS)"),
        ("KRS-6", "KRS-6"),
        ("Polyethylene", "Polyetylen"),
        ("Quartz", "Thạch anh"),
        ("Sapphire (Al2O3)", "Sapphire (Al2O3)"),
        ("Silicon", "Silic"),
        ("ZnSe", "ZnSe"),
    ]
    nums = [
        ("2.6", "0.330", "1"),
        ("2.5", "0.310", "10"),
        ("2.6", "0.330", "10"),
        ("2.4", "0.290", "8.0"),
        ("2.67", "0.342", "10.6"),
        ("2.42", "0.292", "0.54"),
        ("1.46", "0.067", "3.5"),
        ("3.13", "0.420", "10.6"),
        ("4.00", "0.529", "12.0"),
        ("2.25", "0.258", "4.3"),
        ("2.1", "0.224", "24"),
        ("1.54", "0.087", "8.0"),
        ("1.54", "0.088", "—"),
        ("1.59", "0.100", "5.58"),
        ("3.42", "0.462", "5.0"),
        ("2.4", "0.290", "10.6"),
    ]
    notes = [
        ("Amorphous glass", "Thủy tinh vô định hình"),
        ("Amorphous glass", "Thủy tinh vô định hình"),
        ("Amorphous glass", "Thủy tinh vô định hình"),
        ("Amorphous glass", "Thủy tinh vô định hình"),
        ("—", "—"),
        ("Best IR material", "Vật liệu IR tốt nhất"),
        ("Near-IR range", "Vùng hồng ngoại gần"),
        ("—", "—"),
        ("Windows and lenses", "Cửa sổ và thấu kính"),
        ("—", "—"),
        ("Toxic", "Độc"),
        ("Low-cost IR windows; lenses", "Cửa sổ IR giá rẻ; thấu kính"),
        ("Near-IR range", "Vùng hồng ngoại gần"),
        ("Chemically resistant. Near- and mid-IR ranges",
         "Bền hóa học. Vùng hồng ngoại gần và trung"),
        ("Windows in IR sensors", "Cửa sổ trong cảm biến IR"),
        ("IR windows; brittle", "Cửa sổ IR; giòn"),
    ]
    rows = []
    for i in range(len(mat)):
        m = mat[i][1] if vi else mat[i][0]
        n, r, w = nums[i]
        note = notes[i][1] if vi else notes[i][0]
        rows.append([m, n, r, w, note])
    cap = ("Bảng 32.18 · Vật liệu dùng cho cửa sổ và thấu kính hồng ngoại. n là chiết suất, r là "
           "hệ số phản xạ từ hai mặt trong không khí." if vi else
           "Table 32.18 · Materials Useful for Infrared Windows and Lenses. n is the refractive "
           "index and r is the coefficient of reflection from two surfaces in air.")
    return R.table(hd, rows, cap, small=True,
                   widths=["34%", "10%", "12%", "16%", "28%"])


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

    b = [R.h2("32.6 Nhiệt kế hồng ngoại" if vi else "32.6 Infrared Thermometers",
              "Infrared Thermometers" if vi else "Nhiệt kế hồng ngoại")]
    b.append(R.authors("Jacob Fraden", ""))

    # ============================================= physical laws / pyrometry
    b.append(H3("Thermal Radiation: Physical Laws", "Bức xạ nhiệt: các định luật vật lý"))
    b.append(P(
        "In any material object, every atom and every molecule exist in perpetual motion. When an "
        "atom moves, it collides with other atoms and transfers to them part of its kinetic energy, "
        "thus losing some of its own energy in this perpetual bouncing. An atom having a smaller "
        "kinetic energy, after a collision, gains some energy. Afterward, the material body "
        "consisting of such agitated atoms reaches an energetic equilibrium where all atoms, while "
        "not vibrating with exactly the same intensity, can still be described by an average "
        "kinetic energy. That average kinetic energy of the agitated particles is represented by "
        "the absolute temperature, measured in degrees kelvin. In other words, what is commonly "
        "called temperature is a measure of atomic motion.",
        "Trong bất kỳ vật thể nào, mọi nguyên tử và phân tử đều chuyển động không ngừng. Khi một "
        "nguyên tử dịch chuyển, nó va chạm với các nguyên tử khác và truyền cho chúng một phần "
        "động năng, vì thế tự nó mất đi một phần năng lượng trong chuỗi va chạm vĩnh cửu này. "
        "Ngược lại, một nguyên tử có động năng nhỏ hơn sau va chạm sẽ nhận thêm năng lượng. Dần "
        "dà, vật thể cấu thành từ các hạt dao động ấy đạt tới cân bằng năng lượng, trong đó mọi "
        "nguyên tử — dù không dao động với cường độ hoàn toàn như nhau — vẫn được mô tả bằng một "
        "động năng trung bình. Động năng trung bình của các hạt dao động được biểu diễn bằng "
        "<i>nhiệt độ tuyệt đối</i>, đo bằng độ kelvin. Nói cách khác, cái thường gọi là nhiệt độ "
        "chính là thước đo của chuyển động nguyên tử."))
    b.append(P(
        "According to the laws of electrodynamics, a moving electric charge (all atoms are made "
        "of electric charges) is associated with a variable electric field. The field, in turn, "
        "produces an alternating magnetic field, and when the magnetic field changes it results "
        "in a coupled variable electric field, and so on. Thus a moving particle becomes a source "
        "of an electromagnetic field that propagates outward at the speed of light and is called "
        "thermal radiation. This radiation is governed by the laws of optics — it can be "
        "reflected, filtered, focused, etc. — and it can be used to measure the object's "
        "temperature. Electromagnetic waves originating from the mechanical movement of particles "
        "are characterized by their intensities and wavelengths; both relate to temperature, so "
        "the hotter the object, the shorter the wavelength.",
        "Theo các định luật điện động lực học, một điện tích chuyển động (mọi nguyên tử đều cấu "
        "thành từ điện tích) gắn với một điện trường biến thiên. Điện trường lại sinh ra từ "
        "trường xoay chiều, và khi từ trường thay đổi nó lại sinh ra điện trường biến thiên ghép "
        "cặp, cứ thế tiếp diễn. Vì vậy một hạt chuyển động trở thành nguồn của trường điện từ "
        "lan truyền ra ngoài với tốc độ ánh sáng, gọi là <i>bức xạ nhiệt</i>. Bức xạ này tuân "
        "theo các định luật quang học — có thể phản xạ, lọc, hội tụ, v.v. — và có thể dùng để đo "
        "nhiệt độ của vật. Các sóng điện từ bắt nguồn từ chuyển động cơ học của hạt được đặc "
        "trưng bởi cường độ và bước sóng; cả hai đều liên hệ với nhiệt độ, nên vật càng nóng thì "
        "bước sóng càng ngắn."))
    b.append(P(
        "Very hot objects radiate electromagnetic energy in the visible portion of the spectrum — "
        "wavelengths between 0.4 µm (blue) and 0.7 µm (red). For example, the filament of an "
        "incandescent lamp is so hot that it radiates bright visible light. If such a lamp is "
        "controlled by a dimmer, reducing the light intensity makes the dimmed light more "
        "yellowish, then reddish, and finally invisible. Near the end of the dimmer control the "
        "filament is still quite hot, yet one cannot see it because it emanates light in the "
        "invisible infrared spectral range — wavelengths greater than 0.8 µm. Cooler objects "
        "radiate in the near-, mid- and far-infrared ranges, which the eye cannot see. For "
        "example, electromagnetic radiation from human skin lies primarily between 5 µm and "
        "15 µm — in the mid- and far-infrared and invisible to human eyes; otherwise we would "
        "all glow in the dark (and sick people with fever would look even brighter). If all "
        "atomic vibration were to stop for some mysterious reason, no electromagnetic radiation "
        "would be emanated: that imaginable but impossible event is characterized by infinitely "
        "cold temperature, called absolute zero.",
        "Những vật rất nóng bức xạ năng lượng điện từ trong vùng nhìn thấy của phổ — bước sóng "
        "từ 0,4 µm (xanh lam) đến 0,7 µm (đỏ). Chẳng hạn, dây tóc của đèn sợi đốt nóng đến mức "
        "phát ra ánh sáng nhìn thấy chói lóa. Nếu đèn được điều khiển bằng dimmer, vặn giảm độ "
        "sáng sẽ thấy ánh sáng ngả vàng, rồi đỏ, rồi biến mất hẳn. Ở cuối dải điều chỉnh, dây "
        "tóc vẫn còn rất nóng nhưng ta không thấy nó, vì nó phát ra ánh sáng ở vùng phổ hồng "
        "ngoại không nhìn thấy — bước sóng lớn hơn 0,8 µm. Các vật nguội hơn bức xạ trong các "
        "vùng hồng ngoại gần, trung và xa, đều không nhìn thấy được. Thí dụ, bức xạ điện từ từ "
        "da người chủ yếu nằm trong khoảng 5 µm đến 15 µm — thuộc hồng ngoại trung và xa, không "
        "thấy được bằng mắt; nếu không thì tất cả chúng ta đều phát sáng trong bóng tối (và người "
        "bệnh sốt còn sáng hơn). Nếu vì một lý do bí ẩn nào đó mọi dao động nguyên tử ngừng lại, "
        "sẽ không còn bức xạ điện từ nào được phát ra: sự kiện có thể tưởng tượng nhưng không thể "
        "xảy ra ấy được đặc trưng bởi nhiệt độ lạnh vô hạn, gọi là <i>độ không tuyệt đối</i>."))
    b.append(P(
        "Because temperature is a measure of the average atomic kinetic energy, it is logical to "
        "assume that the object's temperature can be determined by measuring the intensity of the "
        "emanated electromagnetic radiation or its spectral characteristics. This presumption is "
        "the basis for noncontact temperature measurements, known by various names depending on "
        "the application: infrared thermometry, optical pyrometry, radiation thermometry, and so "
        "on.",
        "Vì nhiệt độ là thước đo động năng trung bình của nguyên tử, hoàn toàn hợp lý khi cho "
        "rằng có thể xác định nhiệt độ của vật bằng cách đo cường độ bức xạ điện từ phát ra, hoặc "
        "các đặc trưng phổ của nó. Giả định này là nền tảng của các phép đo nhiệt độ không tiếp "
        "xúc, được gọi bằng nhiều tên tùy ứng dụng: đo nhiệt hồng ngoại, đo nhiệt quang học "
        "(pyrometry), đo nhiệt bức xạ, v.v."))

    b.append(H3("Pyrometry", "Phép đo nhiệt bức xạ (Pyrometry)"))
    b.append(P(
        "Pyrometry is derived from the Greek word <i>pyr</i>, which means fire, and thus is more "
        "appropriate for measuring hot temperatures. For lower temperatures, infrared "
        "thermometry is used interchangeably with the term radiation thermometry.",
        "Thuật ngữ <i>pyrometry</i> bắt nguồn từ tiếng Hy Lạp <i>pyr</i>, nghĩa là lửa, vì thế "
        "thích hợp hơn cho việc đo các nhiệt độ cao. Đối với nhiệt độ thấp hơn, thuật ngữ đo "
        "nhiệt hồng ngoại được dùng thay thế cho đo nhiệt bức xạ."))

    # ============================================================ Planck
    b.append(H3("Planck's Law", "Định luật Planck"))
    b.append(P(
        "A relationship between the magnitude of radiation at a particular wavelength λ and "
        "absolute temperature T is rather complex and is governed by Planck's law, discovered in "
        "1901. It establishes the radiant flux density W<sub>λ</sub> as the power of "
        "electromagnetic radiation per unit wavelength:",
        "Quan hệ giữa cường độ bức xạ tại một bước sóng λ xác định và nhiệt độ tuyệt đối T khá "
        "phức tạp, được chi phối bởi định luật Planck, phát hiện năm 1901. Định luật thiết lập "
        "mật độ thông lượng bức xạ W<sub>λ</sub> là công suất bức xạ điện từ trên một đơn vị "
        "bước sóng:"))
    b.append(EQ("<i>W</i><sub>λ</sub> = " + FR("<i>ε</i>(<i>λ</i>) <i>C</i><sub>1</sub>",
                "π <i>λ</i><sup>5</sup> (e<sup><i>C</i><sub>2</sub>/(<i>λ T</i>)</sup> − 1)"),
                "32.90"))
    b.append(P(
        "Spectral densities for different temperatures are shown in Figure 32.48. Note that the "
        "curves never cross: a hotter blackbody emits more radiation at every wavelength, and "
        "its peak shifts steadily toward shorter wavelengths.",
        "Mật độ phổ ứng với các nhiệt độ khác nhau được nêu ở Hình 32.48. Lưu ý các đường cong "
        "không bao giờ cắt nhau: vật đen nóng hơn phát xạ mạnh hơn ở mọi bước sóng, và đỉnh của "
        "nó dịch dần về phía bước sóng ngắn hơn."))
    b.append(F48(lang))

    # ============================================================== Wien
    b.append(H3("Wien's Law", "Định luật Wien"))
    b.append(P(
        "Equation 32.90 does not lend itself to a simple mathematical analysis and thus is "
        "approximated by a simplified version known as Wien's law:",
        "Phương trình 32.90 không dễ phân tích toán học đơn giản, vì thế được xấp xỉ bằng một "
        "dạng rút gọi là định luật Wien:"))
    b.append(EQ("<i>W</i><sub>λ</sub> = " + FR("<i>ε</i>(<i>λ</i>) <i>C</i><sub>1</sub>",
                "π <i>λ</i><sup>5</sup> e<sup><i>C</i><sub>2</sub>/(<i>λ T</i>)</sup>"),
                "32.91"))
    b.append(P(
        "Because temperature is a statistical representation of an average kinetic energy, it "
        "determines the highest probability for the particles to vibrate with a specific "
        "frequency and to have a specific wavelength. That most probable wavelength follows from "
        "Wien's law by equating to zero the first derivative of Equation 32.91. The result is a "
        "wavelength near which most of the radiant power is concentrated when light is emanated "
        "toward infinitely cold space at absolute zero:",
        "Vì nhiệt độ là biểu diễn thống kê của một động năng trung bình, nó xác định xác suất "
        "cao nhất để các hạt dao động với một tần số xác định và có một bước sóng xác định. Bước "
        "sóng có xác suất cao nhất suy ra từ định luật Wien bằng cách cho đạo hàm bậc nhất của "
        "Phương trình 32.91 bằng không. Kết quả là bước sóng mà tại đó phần lớn công suất bức "
        "xạ tập trung khi ánh sáng phát về phía không gian lạnh vô hạn ở độ không tuyệt đối:"))
    b.append(EQ("<i>λ</i><sub>m</sub> = " + FR("2898", "<i>T</i>"), "32.92"))
    b.append(P(
        "Wien's law states that the higher the temperature, the shorter the wavelength. This "
        "formula also defines the midpoint of the spectral response of a pyrometer or infrared "
        "thermometer. At 300 K the peak lies near 10 µm, which is why most instruments aimed at "
        "near-ambient targets work in the far-infrared.",
        "Định luật Wien phát biểu rằng nhiệt độ càng cao thì bước sóng càng ngắn. Công thức này "
        "cũng xác định điểm giữa của dải đáp ứng phổ của một nhiệt kế bức xạ hay nhiệt kế hồng "
        "ngoại. Ở 300 K đỉnh nằm gần 10 µm, đó là lý do hầu hết dụng cụ hướng tới mục tiêu ở "
        "nhiệt độ gần môi trường làm việc trong vùng hồng ngoại xa."))

    # ================================================= Stefan–Boltzmann
    b.append(H3("Stefan–Boltzmann Law", "Định luật Stefan–Boltzmann"))
    b.append(P(
        "Theoretically, a thermal radiation bandwidth is infinitely wide. Yet most of the "
        "emanated power is situated within a quite limited bandwidth, and one must also account "
        "for the filtering properties of the real windows used in instruments. To determine the "
        "total radiated power limited within a particular bandwidth, Equation 32.90 or 32.91 "
        "must be integrated within the limits from λ<sub>1</sub> to λ<sub>2</sub>:",
        "Về lý thuyết, dải bức xạ nhiệt rộng vô hạn. Thế nhưng phần lớn công suất phát ra lại "
        "nằm trong một dải khá hẹp, và còn phải tính đến tính lọc của các cửa sổ thực dùng trong "
        "dụng cụ. Để xác định tổng công suất bức xạ giới hạn trong một dải nhất định, phải tích "
        "phân Phương trình 32.90 hay 32.91 trong giới hạn từ λ<sub>1</sub> đến λ<sub>2</sub>:"))
    b.append(EQ("Φ<sub>bo</sub> = π ∫<sub>λ1</sub><sup>λ2</sup> "
                + FR("<i>ε</i>(<i>λ</i>) <i>C</i><sub>1</sub>",
                     "<i>λ</i><sup>5</sup> (e<sup><i>C</i><sub>2</sub>/(<i>λ T</i>)</sup> − 1)")
                + " d<i>λ</i>", "32.93"))
    b.append(P(
        "This integral can be resolved only numerically or by approximation. For a narrow "
        "bandwidth (λ<sub>1</sub> and λ<sub>2</sub> close to one another), the solution can be "
        "approximated by a power law:",
        "Tích phân này chỉ giải được bằng số hoặc bằng xấp xỉ. Với dải hẹp (λ<sub>1</sub> và "
        "λ<sub>2</sub> gần nhau), nghiệm có thể xấp xỉ bằng một hàm lũy thừa:"))
    b.append(EQ("Φ<sub>bo</sub> = <i>k</i> <i>T</i><sup><i>x</i></sup>", "32.94"))
    b.append(P(
        "For example, in the visible portion of the spectrum at λ<sub>2</sub> ≈ 0.7 µm and for "
        "temperatures near 2000 K, the approximation is a 10th-order parabola. An approximation "
        "for a very broad bandwidth (λ<sub>2</sub> → ∞, or practically when the range between "
        "λ<sub>1</sub> and λ<sub>2</sub> embraces well over 50% of the total radiated power) is "
        "a 4th-order parabola known as the Stefan–Boltzmann law:",
        "Thí dụ, trong vùng nhìn thấy của phổ tại λ<sub>2</sub> ≈ 0,7 µm và nhiệt độ gần "
        "2000 K, xấp xỉ là một parabol bậc 10. Xấp xỉ cho dải rất rộng (λ<sub>2</sub> → ∞, hay "
        "thực tế khi khoảng giữa λ<sub>1</sub> và λ<sub>2</sub> bao trùm quá 50% tổng công suất "
        "bức xạ) là một parabol bậc 4, gọi là định luật Stefan–Boltzmann:"))
    b.append(EQ("Φ<sub>bo</sub> = <i>A</i> <i>ε</i> σ <i>T</i><sup>4</sup>", "32.95"))
    b.append(P(
        "It is seen that with an increase in temperature the intensity of electromagnetic "
        "radiation Φ<sub>bo</sub> grows very fast due to the fourth power of T. Doubling the "
        "absolute temperature raises the radiated power sixteenfold — the reason radiation "
        "thermometry is so effective at high temperatures.",
        "Ta thấy khi nhiệt độ tăng, cường độ bức xạ điện từ Φ<sub>bo</sub> tăng rất nhanh do lũy "
        "thừa bậc bốn của T. Tăng gấp đôi nhiệt độ tuyệt đối làm công suất bức xạ tăng mười sáu "
        "lần — đó là lý do đo nhiệt bức xạ hiệu quả đến vậy ở nhiệt độ cao."))

    # ======================================================== Kirchhoff
    b.append(H3("Kirchhoff's Law", "Định luật Kirchhoff"))
    b.append(P(
        "While the wavelengths of the radiated light are temperature dependent, the magnitude of "
        "radiation is also a function of a surface property called emissivity, ε. Emissivity is "
        "measured on a scale from 0 to 1: it is the ratio of the electromagnetic flux emanated "
        "from a surface to the flux that would be emanated from an ideal emitter at the same "
        "temperature. Reflectivity, ρ, and transparency, γ, also on a scale from 0 to 1, show "
        "what portion of incident light is reflected and passed through, respectively. A "
        "fundamental equation connects these three characteristics:",
        "Trong khi bước sóng của ánh sáng phát ra phụ thuộc nhiệt độ, thì cường độ bức xạ còn là "
        "hàm của một thuộc tính bề mặt gọi là <i>độ phát xạ</i>, ε. Độ phát xạ đo trên thang từ "
        "0 đến 1: đó là tỉ số giữa thông lượng điện từ phát ra từ một bề mặt với thông lượng sẽ "
        "phát ra từ một bộ phát lý tưởng ở cùng nhiệt độ. <i>Độ phản xạ</i> ρ và <i>độ trong "
        "suốt</i> γ, cũng trên thang 0 đến 1, cho biết phần ánh sáng tới bị phản xạ và phần "
        "truyền qua. Một phương trình cơ bản liên kết ba đặc trưng này:"))
    b.append(EQ("<i>ε</i> + <i>γ</i> + <i>ρ</i> = 1", "32.96"))
    b.append(P(
        "Equation 32.96 indicates that any one of the three properties of a material can be "
        "changed only at the expense of the others. As a result, for an opaque object (γ = 0), "
        "reflectivity ρ and emissivity ε are connected by the simple relationship ρ = 1 − ε, "
        "which, for example, makes a mirror a good reflector but a poor emitter.",
        "Phương trình 32.96 cho thấy bất kỳ một trong ba thuộc tính của vật liệu chỉ có thể thay "
        "đổi bằng cách làm thay đổi các thuộc tính kia. Hệ quả là, với vật đục (γ = 0), độ phản "
        "xạ ρ và độ phát xạ ε liên hệ qua quan hệ đơn giản ρ = 1 − ε — chẳng hạn, chính quan hệ "
        "này khiến gương phản xạ tốt nhưng phát xạ kém."))

    # ========================================================= Emissivity
    b.append(H3("Emissivity", "Độ phát xạ"))
    b.append(P(
        "The emissivity of a material is a function of its dielectric constant and, "
        "subsequently, of its refractive index n. It should be noted, however, that emissivity is "
        "generally wavelength dependent (Figure 32.49). For example, a white sheet of paper is "
        "very reflective in the visible range and emits no visible light, yet in the far-infrared "
        "its reflectivity is low and its emissivity is high (about 0.92), making paper a good "
        "emitter of thermal radiation. For many practical purposes in infrared thermometry, "
        "however, emissivity can be considered constant. For nonpolarized far-infrared light in "
        "the normal direction, emissivity can be expressed as:",
        "Độ phát xạ của vật liệu là hàm của hằng số điện môi, và vì thế là hàm của chiết suất n. "
        "Tuy nhiên cần lưu ý rằng độ phát xạ nói chung phụ thuộc bước sóng (Hình 32.49). Thí dụ, "
        "một tờ giấy trắng phản xạ rất mạnh trong vùng nhìn thấy và không phát ra ánh sáng nhìn "
        "thấy, nhưng trong vùng hồng ngoại xa độ phản xạ của nó thấp còn độ phát xạ cao (khoảng "
        "0,92), khiến giấy trở thành bộ phát bức xạ nhiệt tốt. Dẫu vậy, với nhiều mục đích thực "
        "hành trong đo nhiệt hồng ngoại, có thể coi độ phát xạ là hằng số. Đối với ánh sáng hồng "
        "ngoại xa không phân cực theo hướng pháp tuyến, độ phát xạ được biểu diễn là:"))
    b.append(EQ("<i>ε</i> = " + FR("4<i>n</i>", "(<i>n</i> + 1)<sup>2</sup>"), "32.97"))
    b.append(P(
        "As a rule, emissivities of dielectrics are high and those of metals are low. Thanks to "
        "the high emissivity of dielectrics, they lend themselves to easy and accurate "
        "noncontact temperature measurement. On the other hand, such measurements on "
        "nonoxidized metals are difficult because of the small amount of emanated infrared flux. "
        "Table 32.17 gives typical emissivities of some opaque materials in the temperature "
        "range between 0 °C and 100 °C.",
        "Theo quy luật, độ phát xạ của chất điện môi cao, còn của kim loại thấp. Nhờ độ phát xạ "
        "cao của chất điện môi, chúng rất thuận lợi cho phép đo nhiệt độ không tiếp xúc dễ dàng "
        "và chính xác. Ngược lại, đo trên kim loại chưa oxit hóa rất khó vì thông lượng hồng "
        "ngoại phát ra quá nhỏ. Bảng 32.17 cho độ phát xạ điển hình của một số vật đục trong "
        "dải nhiệt độ từ 0 °C đến 100 °C."))
    b.append(_t3217(lang))
    b.append(F49(lang))
    b.append(P(
        "Unlike most solid bodies, gases in many cases are transparent to thermal radiation. "
        "When they absorb and emit radiation, they usually do so only in certain narrow spectral "
        "bands. Some gases, such as N<sub>2</sub>, O<sub>2</sub> and others of nonpolar "
        "symmetrical molecular structure, are essentially transparent at low temperatures, "
        "whereas CO<sub>2</sub>, H<sub>2</sub>O and various hydrocarbon gases radiate and absorb "
        "to an appreciable extent. When infrared light enters a layer of gas, its absorption has "
        "an exponential decay profile governed by Beer's law:",
        "Khác với hầu hết vật rắn, chất khí trong nhiều trường hợp trong suốt đối với bức xạ "
        "nhiệt. Khi hấp thụ và phát xạ, chúng thường chỉ làm vậy trong một số dải phổ hẹp nhất "
        "định. Một số khí như N<sub>2</sub>, O<sub>2</sub> và các khí có cấu trúc phân tử đối "
        "xứng không phân cực khác hầu như trong suốt ở nhiệt độ thấp, trong khi CO<sub>2</sub>, "
        "H<sub>2</sub>O và nhiều khí hydrocarbon bức xạ và hấp thụ đáng kể. Khi ánh sáng hồng "
        "ngoại đi vào một lớp khí, sự hấp thụ có dạng suy giảm hàm mũ theo định luật Beer:"))
    b.append(EQ(FR("Φ<sub>x</sub>", "Φ<sub>0</sub>")
                + " = e<sup>−<i>α</i><sub>λ</sub><i>x</i></sup>", "32.98"))
    b.append(P(
        "The above ratio is called the monochromatic transmissivity γ<sub>λ</sub> at a specific "
        "wavelength λ. If the gas is nonreflecting, then its emissivity is defined as:",
        "Tỉ số trên gọi là độ truyền qua đơn sắc γ<sub>λ</sub> tại một bước sóng λ xác định. Nếu "
        "khí không phản xạ, độ phát xạ của nó được định nghĩa là:"))
    b.append(EQ("<i>ε</i><sub>λ</sub> = 1 − <i>γ</i><sub>λ</sub> = "
                "1 − e<sup>−<i>α</i><sub>λ</sub><i>x</i></sup>", "32.99"))
    b.append(P(
        "It should be emphasized that since gases absorb only in narrow bands, emissivity and "
        "transmissivity (transparency) must be specified separately for any particular "
        "wavelength. For example, water vapor is highly absorptive at wavelengths of 1.4, 1.8 "
        "and 2.7 µm and is very transparent at 1.6, 2.2 and 4 µm.",
        "Cần nhấn mạnh rằng vì chất khí chỉ hấp thụ trong các dải hẹp, độ phát xạ và độ truyền "
        "qua (độ trong suốt) phải được nêu riêng cho từng bước sóng cụ thể. Thí dụ, hơi nước "
        "hấp thụ mạnh tại các bước sóng 1,4; 1,8 và 2,7 µm, nhưng rất trong suốt tại 1,6; 2,2 "
        "và 4 µm."))
    b.append(P(
        "All non-metals are very good diffusive emitters of thermal radiation with a remarkably "
        "constant emissivity defined by Equation 32.97 within a solid angle of about ±70°. "
        "Beyond that angle emissivity begins to decrease rapidly to zero as the angle approaches "
        "90°, and near 90° it is very low. A typical calculated graph of the directional "
        "emissivity of non-metals into air is shown in Figure 32.50A. These considerations apply "
        "only to wavelengths in the far-infrared and are not true for visible light, since "
        "emissivity of thermal radiation is the result of electromagnetic effects occurring at "
        "an appreciable depth. Metals behave quite differently: their emissivities depend greatly "
        "on surface finish. Generally, polished metals are poor emitters within the solid angle "
        "of ±70°, while their emissivity increases at larger angles (Figure 32.50B). Oxidized "
        "metals start behaving more and more like dielectrics as the thickness of the oxide "
        "increases.",
        "Mọi phi kim đều là bộ phát khuếch tán bức xạ nhiệt rất tốt, với độ phát xạ ổn định đáng "
        "kể theo Phương trình 32.97 trong góc khối khoảng ±70°. Vượt quá góc đó, độ phát xạ bắt "
        "đầu giảm nhanh về 0 khi góc tiến tới 90°, và ở gần 90° nó rất thấp. Đồ thị tính điển "
        "hình của độ phát xạ theo hướng của phi kim vào không khí được nêu ở Hình 32.50A. Các "
        "xem xét trên chỉ áp dụng cho bước sóng thuộc vùng hồng ngoại xa, không đúng với ánh "
        "sáng nhìn thấy, vì độ phát xạ của bức xạ nhiệt là kết quả của các hiệu ứng điện từ xảy "
        "ra ở độ sâu đáng kể. Kim loại cư xử rất khác: độ phát xạ của chúng phụ thuộc mạnh vào "
        "độ hoàn thiện bề mặt. Nhìn chung, kim loại đánh bóng phát xạ kém trong góc khối ±70°, "
        "nhưng độ phát xạ tăng lên ở góc lớn hơn (Hình 32.50B). Kim loại bị oxit hóa càng cư xử "
        "giống chất điện môi khi lớp oxit càng dày."))
    b.append(F50(lang))

    # ========================================================== Blackbody
    b.append(H3("Blackbody", "Vật đen"))
    b.append(P(
        "By definition, the highest possible emissivity is unity. It is attributed to the "
        "so-called blackbody — an ideal emitter of electromagnetic radiation. If the object is "
        "opaque (γ = 0) and nonreflective (ρ = 0), then according to Equation 32.96 it becomes "
        "an ideal emitter and absorber of electromagnetic radiation. The name blackbody implies "
        "its appearance at normal room temperatures: indeed it looks black, because it is "
        "neither transparent nor reflective at any wavelength. In reality a blackbody does not "
        "exist, and any object with a nonunity emissivity is often called a graybody. A practical "
        "blackbody (ε about 0.99 or higher) is an essential tool for calibrating and verifying "
        "the accuracy of infrared thermometers.",
        "Theo định nghĩa, độ phát xạ lớn nhất có thể là đơn vị. Nó được gán cho cái gọi là "
        "<i>vật đen</i> — bộ phát lý tưởng của bức xạ điện từ. Nếu vật đục (γ = 0) và không "
        "phản xạ (ρ = 0) thì theo Phương trình 32.96 nó trở thành bộ phát và bộ hấp thụ lý "
        "tưởng của bức xạ điện từ. Cái tên vật đen gợi nên diện mạo của nó ở nhiệt độ phòng "
        "thường: quả thực nó trông đen, vì không trong suốt cũng không phản xạ ở bất kỳ bước "
        "sóng nào. Trên thực tế vật đen không tồn tại, và mọi vật có độ phát xạ khác đơn vị "
        "thường được gọi là <i>vật xám</i> (graybody). Một vật đen thực hành (ε khoảng 0,99 trở "
        "lên) là dụng cụ thiết yếu để hiệu chuẩn và kiểm tra độ chính xác của nhiệt kế hồng "
        "ngoại."))

    # ====================================================== Cavity Effect
    b.append(H3("Cavity Effect", "Hiệu ứng hốc"))
    b.append(P(
        "To make a practical blackbody, the cavity effect is put to work. The effect appears "
        "when electromagnetic radiation is measured from a cavity of an object. Here a cavity "
        "means an opening in a concave void of generally irregular shape whose inner wall "
        "temperature is uniform over its entire surface. The emissivity of a cavity opening "
        "dramatically increases, approaching unity at any wavelength, compared with a flat "
        "surface. The effect is especially pronounced when the inner walls have relatively high "
        "emissivity. Consider a non-metal cavity: all non-metals are diffuse emitters and also "
        "diffuse reflectors, and the temperature and surface emissivity of the cavity are "
        "assumed homogeneous over the entire area. The ideal emitter (blackbody) would emanate "
        "from area a the infrared photon flux F<sub>0</sub> = a σ T<sub>b</sub><sup>4</sup>. "
        "However, the object has actual emissivity ε<sub>b</sub>, so the flux radiated from that "
        "area is smaller: F<sub>r</sub> = ε<sub>b</sub> F<sub>0</sub> (Figure 32.51). The flux "
        "emitted by other parts of the object toward area a is also equal to F<sub>r</sub> "
        "(because the object is thermally homogeneous, the spatial distribution of flux can be "
        "disregarded). A substantial portion of that incident flux F<sub>r</sub> is absorbed by "
        "the surface of area a, while a smaller part is diffusely reflected:",
        "Để chế tạo một vật đen thực hành, người ta khai thác <i>hiệu ứng hốc</i>. Hiệu ứng xuất "
        "hiện khi bức xạ điện từ được đo từ một hốc của vật thể. Ở đây hốc là một lỗ mở vào một "
        "khoảng rỗng lõm, thường có dạng không đều, có nhiệt độ thành trong đồng đều trên toàn "
        "bộ bề mặt. Độ phát xạ của lỗ hốc tăng vọt, tiến tới đơn vị ở mọi bước sóng, so với một "
        "mặt phẳng. Hiệu ứng đặc biệt rõ khi thành trong có độ phát xạ tương đối cao. Xét một "
        "hốc phi kim: mọi phi kim đều là bộ phát khuếch tán và cũng là bộ phản xạ khuếch tán, "
        "giả thiết nhiệt độ và độ phát xạ bề mặt của hốc đồng nhất trên toàn diện tích. Bộ phát "
        "lý tưởng (vật đen) sẽ phát từ diện tích a thông lượng photon hồng ngoại "
        "F<sub>0</sub> = a σ T<sub>b</sub><sup>4</sup>. Tuy nhiên vật có độ phát xạ thực "
        "ε<sub>b</sub>, nên thông lượng bức xạ từ diện tích đó nhỏ hơn: "
        "F<sub>r</sub> = ε<sub>b</sub> F<sub>0</sub> (Hình 32.51). Thông lượng do các phần khác "
        "của vật phát về phía diện tích a cũng bằng F<sub>r</sub> (vì vật đồng nhất về nhiệt, có "
        "thể bỏ qua phân bố không gian của thông lượng). Một phần đáng kể của thông lượng tới "
        "F<sub>r</sub> bị bề mặt diện tích a hấp thụ, phần nhỏ hơn được phản xạ khuếch tán:"))
    b.append(EQ("<i>F</i><sub>rr</sub> = (1 − <i>ε</i><sub>b</sub>) <i>F</i><sub>r</sub> "
                "= (1 − <i>ε</i><sub>b</sub>) <i>ε</i><sub>b</sub> <i>F</i><sub>0</sub>",
                "32.100"))
    b.append(P(
        "and the combined radiated and reflected flux from area a is:",
        "còn thông lượng tổng (bức xạ cộng phản xạ) thoát khỏi diện tích a là:"))
    b.append(EQ("<i>F</i> = <i>F</i><sub>r</sub> + <i>F</i><sub>rr</sub> "
                "= <i>ε</i><sub>b</sub> <i>F</i><sub>0</sub> "
                "+ (1 − <i>ε</i><sub>b</sub>)<i>ε</i><sub>b</sub> <i>F</i><sub>0</sub> "
                "= <i>ε</i><sub>b</sub>(2 − <i>ε</i><sub>b</sub>) <i>F</i><sub>0</sub>",
                "32.101"))
    b.append(P(
        "As a result, for a single reflection, the effective emissivity can be expressed as:",
        "Kết quả là, với một lần phản xạ, <i>độ phát xạ hiệu dụng</i> được biểu diễn là:"))
    b.append(EQ("<i>ε</i><sub>e</sub> = " + FR("<i>F</i>", "<i>F</i><sub>0</sub>")
                + " = <i>ε</i><sub>b</sub>(2 − <i>ε</i><sub>b</sub>)", "32.102"))
    b.append(P(
        "It follows that due to a single reflection, the perceived (effective) emissivity of a "
        "cavity at its opening (aperture) is equal to the surface emissivity magnified by a "
        "factor of (2 − ε<sub>b</sub>). Of course there may be more than one reflection of "
        "radiation before it exits the cavity; the flux incident on area a could already be the "
        "result of a combined effect of reflectance and emittance at other parts of the cavity "
        "surface. For a cavity effect to work, the effective emissivity must be attributed only "
        "to the cavity opening from which radiation escapes. If a sensor is inserted into the "
        "cavity facing its wall directly, the cavity effect could disappear and the emissivity "
        "would be close to that of the wall surface.",
        "Từ đó suy ra, chỉ với một lần phản xạ, độ phát xạ cảm nhận (hiệu dụng) của hốc tại lỗ "
        "mở đã bằng độ phát xạ bề mặt nhân với hệ số (2 − ε<sub>b</sub>). Dĩ nhiên có thể có "
        "nhiều hơn một lần phản xạ trước khi bức xạ thoát khỏi hốc; thông lượng tới diện tích a "
        "đã có thể là kết quả tổng hợp của phản xạ và phát xạ tại những phần khác của thành hốc. "
        "Để hiệu ứng hốc có tác dụng, độ phát xạ hiệu dụng phải chỉ được gán cho lỗ hốc nơi bức "
        "xạ thoát ra. Nếu đưa cảm biến vào trong hốc, hướng thẳng vào thành, hiệu ứng hốc có thể "
        "biến mất và độ phát xạ sẽ xấp xỉ độ phát xạ của bề mặt thành."))
    b.append(F51(lang))

    # ================================================ Practical Blackbodies
    b.append(H3("Practical Blackbodies", "Vật đen thực hành"))
    b.append(P(
        "A practical blackbody can be fabricated in several ways. Copper is the best choice for "
        "the cavity body material, thanks to its high thermal conductivity, which helps "
        "equalize the temperatures of the cavity walls. As an example, Figure 32.52 shows two "
        "practical blackbodies. One is a solid-state blackbody having thermoelectric elements "
        "(heat pumps) that provide either heating or cooling to the cavity body. The embedded "
        "temperature sensors are connected to a control circuit (not shown); their function is "
        "to monitor the thermal distribution over the length of the cavity. The inner shape of "
        "the cavity is partly conical to increase the number of reflections, and the entire "
        "surface is treated to give it as high an emissivity as possible, typically over 0.9. "
        "This type has a relatively wide aperture that can act as an entry for undesirable "
        "ambient air, disturbing the thermal uniformity inside the cavity and resulting in "
        "excessively high uncertainty of the radiated flux. To reduce this problem, the cavity "
        "is filled with dry air or nitrogen continuously pumped in through gas ducts; before "
        "entering the cavity the gas passes through narrow channels inside the cavity and "
        "acquires the temperature of the blackbody.",
        "Vật đen thực hành có thể chế tạo bằng nhiều cách. Đồng là lựa chọn tốt nhất cho thân "
        "hốc nhờ độ dẫn nhiệt cao, giúp san bằng nhiệt độ giữa các thành hốc. Thí dụ, Hình 32.52 "
        "nêu hai vật đen thực hành. Một là vật đen thể rắn dùng các phần tử nhiệt điện (bơm "
        "nhiệt) để gia nhiệt hoặc làm lạnh thân hốc. Các cảm biến nhiệt độ nhúng được nối với "
        "mạch điều khiển (không vẽ); chức năng của nhiều cảm biến là theo dõi phân bố nhiệt dọc "
        "chiều dài hốc. Dạng trong của hốc một phần là hình nón để tăng số lần phản xạ, và toàn "
        "bộ bề mặt được xử lý để đạt độ phát xạ cao nhất có thể, điển hình trên 0,9. Kiểu này "
        "có lỗ mở tương đối rộng, có thể trở thành đường cho không khí môi trường không mong "
        "muốn xâm nhập, làm xáo trộn tính đồng nhất nhiệt bên trong hốc và gây độ bất định quá "
        "lớn cho thông lượng bức xạ. Để giảm vấn đề này, hốc được nạp đầy khí khô hoặc nitơ "
        "được bơm liên tục qua các ống dẫn khí; trước khi vào hốc, khí đi qua các kênh hẹp bên "
        "trong thân hốc và đạt tới nhiệt độ của vật đen."))
    b.append(P(
        "Another example is an immersed blackbody. The cavity is fabricated of copper or "
        "aluminum and has relatively thin walls (a few millimeters). The entire cavity body is "
        "immersed in a stirred liquid bath whose temperature is precisely controlled by "
        "heating/cooling devices. The liquid assures uniform temperature distribution around "
        "the cavity with a typical thermal instability on the order of ±0.02 °C. The inner "
        "surface of the cavity is coated with high-emissivity paint and the aperture is "
        "relatively small. The ratio of the inner surface area of the cavity to the aperture "
        "area should be at least 100, and preferably close to 1000.",
        "Một ví dụ khác là vật đen nhúng. Hốc được chế tạo từ đồng hoặc nhôm với thành tương đối "
        "mỏng (vài milimét). Toàn bộ thân hốc được nhúng trong bồn chất lỏng được khuấy, nhiệt "
        "độ được điều khiển chính xác bằng các thiết bị gia nhiệt/làm lạnh. Chất lỏng bảo đảm "
        "phân bố nhiệt độ đồng đều quanh hốc, với độ bất định nhiệt điển hình cỡ ±0,02 °C. Bề "
        "mặt trong của hốc được phủ sơn có độ phát xạ cao, và lỗ mở tương đối nhỏ. Tỉ số giữa "
        "diện tích bề mặt trong của hốc với diện tích lỗ mở nên đạt ít nhất 100, và tốt hơn là "
        "gần 1000."))
    b.append(F52(lang))

    # ============================================ Detectors for Thermal Radiation
    b.append(H3("Detectors for Thermal Radiation", "Đầu dò bức xạ nhiệt"))
    b.append(P(
        "Generally speaking, there are two types of sensors (detectors) known for their ability "
        "to respond to thermal radiation within the spectral range from the near-infrared to the "
        "far-infrared, that is, from approximately 0.8 µm to 40 µm. The first type is quantum "
        "detectors and the second is thermal detectors. The latter, in turn, can be subdivided "
        "into passive (PIR) and active (AFIR) detectors.",
        "Nhìn chung có hai loại cảm biến (đầu dò) có khả năng đáp ứng bức xạ nhiệt trong dải phổ "
        "từ hồng ngoại gần đến hồng ngoại xa, tức khoảng 0,8 µm đến 40 µm. Loại thứ nhất là đầu "
        "dò lượng tử, loại thứ hai là đầu dò nhiệt. Loại sau lại được chia thành đầu dò thụ động "
        "(PIR) và đầu dò chủ động (AFIR)."))

    b.append(H4("Classification", "Phân loại"))
    b.append(P(
        "The classification follows the physical mechanism of detection. Quantum detectors "
        "respond to individual photons; thermal detectors respond to the heat produced when "
        "radiation is absorbed by a sensing element. A PIR (passive infrared) sensing element "
        "receives no external excitation power, whereas an AFIR (active far-infrared) element "
        "is held at a controlled temperature by a dedicated circuit. The distinction matters "
        "because it determines the dynamic response, the need for chopping, and the way the "
        "object temperature is finally computed.",
        "Việc phân loại dựa trên cơ chế vật lý của phép dò. Đầu dò lượng tử đáp ứng với từng "
        "photon; đầu dò nhiệt đáp ứng với nhiệt sinh ra khi bức xạ bị hấp thụ trên bề mặt phần "
        "tử cảm biến. Phần tử PIR (hồng ngoại thụ động) không nhận công suất kích thích từ "
        "ngoài, trong khi phần tử AFIR (hồng ngoại xa chủ động) được giữ ở nhiệt độ điều khiển "
        "bằng một mạch chuyên dụng. Sự phân biệt này quan trọng vì nó quyết định đáp ứng động, "
        "nhu cầu chặt chùm và cách tính nhiệt độ vật cuối cùng."))

    b.append(H4("Quantum Detectors", "Đầu dò lượng tử"))
    b.append(P(
        "Quantum detectors (photovoltaic and photoconductive devices) rely on the interaction "
        "of individual photons with the crystalline lattice of semiconductor materials. Their "
        "operation is based on the photoeffect discovered by Einstein, which brought him the "
        "Nobel Prize. In 1905 he made the remarkable assumption that, at least under certain "
        "circumstances, the energy of light is concentrated into localized bundles later named "
        "photons. The energy of a single photon is given by:",
        "Đầu dò lượng tử (linh kiện quang điện áp và quang dẫn) dựa trên tương tác của từng "
        "photon riêng lẻ với mạng tinh thể của vật liệu bán dẫn. Hoạt động của chúng dựa trên "
        "hiệu ứng quang điện do Einstein phát hiện, mang lại cho ông giải Nobel. Năm 1905 ông "
        "đưa ra giả định đáng chú ý rằng, ít nhất trong một số điều kiện, năng lượng ánh sáng "
        "tập trung thành các gói định xứ, về sau gọi là photon. Năng lượng của một photon là:"))
    b.append(EQ("<i>E</i> = <i>h</i> ν", "32.103"))
    b.append(P(
        "When a photon strikes the surface of a conductor, it can result in the generation of a "
        "free electron. The periodic lattice of crystalline materials establishes allowed "
        "energy bands for electrons within that solid, separated by gaps or ranges of forbidden "
        "energies. In insulators and semiconductors an electron must first cross the bandgap to "
        "reach the conduction band, so conductivity is many orders of magnitude lower. For "
        "insulators the bandgap is usually 5 eV or more, whereas for semiconductors the gap is "
        "considerably less. When a photon of frequency ν<sub>1</sub> strikes a semiconductive "
        "crystal, its energy may be high enough to separate an electron from its site in the "
        "valence band and push it through the bandgap into a conduction band at a higher energy "
        "level, where it is free to serve as a current carrier. The deficiency of an electron in "
        "the valence band creates a hole that is also a current carrier. This is manifested as "
        "a reduction of the specific resistivity of the material. The energy gap thus serves as "
        "a photon energy threshold below which the material is not light sensitive.",
        "Khi một photon đập vào bề mặt chất dẫn, nó có thể sinh ra một electron tự do. Mạng tuần "
        "hoàn của vật liệu tinh thể thiết lập các vùng năng lượng cho phép đối với electron trong "
        "chất rắn, bị ngăn cách bởi các vùng cấm. Trong chất cách điện và chất bán dẫn, electron "
        "phải vượt qua vùng cấm để tới được vùng dẫn, nên độ dẫn điện thấp hơn nhiều bậc. Với "
        "chất cách điện, vùng cấm thường từ 5 eV trở lên; với chất bán dẫn, vùng cấm nhỏ hơn "
        "đáng kể. Khi photon tần số ν<sub>1</sub> đập vào tinh thể bán dẫn, năng lượng của nó "
        "có thể đủ lớn để tách electron khỏi vị trí trong vùng hóa trị và đẩy qua vùng cấm lên "
        "vùng dẫn ở mức năng lượng cao hơn, nơi electron tự do làm hạt tải dòng. Sự thiếu hụt "
        "electron trong vùng hóa trị tạo ra một lỗ trống, cũng là hạt tải dòng. Điều này thể "
        "hiện ở sự giảm điện trở suất riêng của vật liệu. Vì thế vùng cấm đóng vai trò ngưỡng "
        "năng lượng photon, dưới ngưỡng đó vật liệu không nhạy sáng."))
    b.append(P(
        "For measurements of objects emanating photons in the range of 2 eV or greater, quantum "
        "detectors at room temperature are generally used. For smaller energies (longer "
        "wavelengths), narrower-bandgap semiconductors are required. However, even if a quantum "
        "detector has a sufficiently small energy bandgap, at room temperature its own intrinsic "
        "noise is much greater than the photoconductive signal. Noise level is temperature "
        "dependent; therefore, when detecting long-wavelength photons, the signal-to-noise "
        "ratio can become so small that accurate measurement becomes impossible. This is why, "
        "for operation in the near- and far-infrared ranges, a detector must not only have a "
        "sufficiently narrow energy gap but its temperature must be lowered to the level where "
        "intrinsic noise is reduced to an acceptable value. Depending on the required "
        "sensitivity and operating wavelength, the following crystals are typically used for "
        "cryogenically cooled sensors (Figure 32.53): lead sulfide (PbS), indium arsenide "
        "(InAs), germanium (Ge), lead selenide (PbSe), and mercury-cadmium-telluride "
        "(HgCdTe). Sensor cooling allows responses to longer wavelengths and increases "
        "sensitivity; however, the response speeds of PbS and PbSe become slower with cooling. "
        "Methods of cooling include dewar cooling using dry ice, liquid nitrogen, liquid helium, "
        "or thermoelectric coolers operating on the Peltier effect.",
        "Đối với phép đo các vật phát photon có năng lượng từ 2 eV trở lên, thường dùng đầu dò "
        "lượng tử ở nhiệt độ phòng. Với năng lượng nhỏ hơn (bước sóng dài hơn), cần bán dẫn có "
        "vùng cấm hẹp hơn. Tuy nhiên, dù đầu dò lượng tử có vùng cấm đủ hẹp, ở nhiệt độ phòng "
        "nhiễu nội tại của chính nó vẫn lớn hơn nhiều tín hiệu quang dẫn. Mức nhiễu phụ thuộc "
        "nhiệt độ; vì thế khi dò photon bước sóng dài, tỉ số tín hiệu trên nhiễu có thể nhỏ đến "
        "mức không đo chính xác được. Đó là lý do, để làm việc trong vùng hồng ngoại gần và xa, "
        "đầu dò không chỉ cần vùng cấm đủ hẹp mà nhiệt độ của nó còn phải hạ xuống mức mà nhiễu "
        "nội tại giảm tới giá trị chấp nhận được. Tùy độ nhạy và bước sóng làm việc cần thiết, "
        "các tinh thể điển hình dùng cho cảm biến làm lạnh sâu (Hình 32.53) là: chì sunfua "
        "(PbS), asenua indi (InAs), gecmani (Ge), chì selenua (PbSe) và thủy ngân–cadmi–"
        "telurua (HgCdTe). Làm lạnh cảm biến cho phép đáp ứng tới bước sóng dài hơn và tăng độ "
        "nhạy; tuy nhiên tốc độ đáp ứng của PbS và PbSe lại chậm đi khi làm lạnh. Các phương "
        "pháp làm lạnh gồm bình dewar dùng đá khô, nitơ lỏng, heli lỏng, hoặc bộ làm lạnh nhiệt "
        "điện hoạt động theo hiệu ứng Peltier."))
    b.append(F53(lang))

    b.append(H4("Thermal Detectors", "Đầu dò nhiệt"))
    b.append(P(
        "Another class of infrared radiation detectors is called thermal detectors. Contrary to "
        "quantum detectors, which respond to individual photons, thermal detectors respond to "
        "the heat resulting from absorption of thermal radiation by the surface of a sensing "
        "element. The heat raises the temperature of the surface, and this temperature increase "
        "becomes a measure of the net thermal radiation.",
        "Một lớp đầu dò bức xạ hồng ngoại khác gọi là đầu dò nhiệt. Ngược với đầu dò lượng tử "
        "đáp ứng từng photon, đầu dò nhiệt đáp ứng nhiệt sinh ra do bức xạ nhiệt bị hấp thụ trên "
        "bề mặt phần tử cảm biến. Nhiệt làm tăng nhiệt độ bề mặt, và độ tăng nhiệt độ này trở "
        "thành thước đo của thông lượng bức xạ nhiệt thuần."))
    b.append(P(
        "The Stefan–Boltzmann law (Equation 32.95) specifies the radiant power (flux) that "
        "would emanate from a surface of temperature T toward an infinitely cold space (at "
        "absolute zero). When thermal radiation is detected by a thermal sensor, the opposite "
        "radiation from the sensor toward the object must also be taken into account: a thermal "
        "sensor responds only to a net thermal flux, i.e. the flux from the object minus the "
        "flux from itself. The surface of the sensor that faces the object has emissivity "
        "ε<sub>s</sub> (and, subsequently, reflectivity ρ<sub>s</sub> = 1 − ε<sub>s</sub>). "
        "Because the sensor is only partly absorptive, the entire flux Φ<sub>bo</sub> is not "
        "absorbed and utilized; a part Φ<sub>ba</sub> is absorbed while another part Φ<sub>br</sub> "
        "is reflected back toward the object (Figure 32.54). Here it is assumed that there is "
        "100% coupling between the object and the sensor and that no other objects lie in the "
        "sensor's field of view. The reflected flux is proportional to the sensor's coefficient "
        "of reflectivity, with a negative sign indicating the opposite direction with respect "
        "to Φ<sub>bo</sub>:",
        "Định luật Stefan–Boltzmann (Phương trình 32.95) xác định công suất bức xạ (thông "
        "lượng) sẽ phát ra từ một bề mặt có nhiệt độ T về phía không gian lạnh vô hạn (ở độ "
        "không tuyệt đối). Khi bức xạ nhiệt được dò bằng cảm biến nhiệt, phải tính cả bức xạ "
        "ngược chiều từ cảm biến về phía vật: cảm biến nhiệt chỉ đáp ứng <i>thông lượng "
        "thuần</i>, tức thông lượng từ vật trừ đi thông lượng từ chính nó. Bề mặt cảm biến "
        "hướng về vật có độ phát xạ ε<sub>s</sub> (và vì thế độ phản xạ "
        "ρ<sub>s</sub> = 1 − ε<sub>s</sub>). Vì cảm biến chỉ hấp thụ một phần, toàn bộ thông "
        "lượng Φ<sub>bo</sub> không được hấp thụ và sử dụng; một phần Φ<sub>ba</sub> bị hấp "
        "thụ, phần khác Φ<sub>br</sub> bị phản xạ ngược về phía vật (Hình 32.54). Ở đây giả "
        "thiết có ghép nối 100% giữa vật và cảm biến, và không có vật nào khác trong trường "
        "nhìn của cảm biến. Thông lượng phản xạ tỉ lệ với hệ số phản xạ của cảm biến, với dấu "
        "âm chỉ hướng ngược lại so với Φ<sub>bo</sub>:"))
    b.append(EQ("Φ<sub>br</sub> = −<i>ρ</i><sub>s</sub> Φ<sub>bo</sub> "
                "= −(1 − <i>ε</i><sub>s</sub>) <i>A</i> <i>ε</i> σ <i>T</i><sup>4</sup>",
                "32.104"))
    b.append(P(
        "As a result, the net flux originated from the object is:",
        "Hệ quả là, thông lượng thuần bắt nguồn từ vật là:"))
    b.append(EQ("Φ<sub>b</sub> = Φ<sub>bo</sub> + Φ<sub>br</sub> "
                "= <i>ε</i><sub>s</sub> <i>A</i> <i>ε</i> σ <i>T</i><sup>4</sup>",
                "32.105"))
    b.append(P(
        "Depending on its temperature T<sub>s</sub>, the sensor's surface radiates its own net "
        "thermal flux toward the object in a similar way:",
        "Tùy theo nhiệt độ T<sub>s</sub> của nó, bề mặt cảm biến cũng bức xạ thông lượng nhiệt "
        "thuần riêng về phía vật theo cách tương tự:"))
    b.append(EQ("Φ<sub>s</sub> = −<i>ε</i><sub>s</sub> <i>A</i> <i>ε</i> σ "
                "<i>T</i><sub>s</sub><sup>4</sup>", "32.106"))
    b.append(P(
        "Two fluxes propagate in opposite directions and are combined into a final net flux "
        "existing between the two surfaces:",
        "Hai thông lượng truyền ngược chiều nhau và được tổng hợp thành thông lượng thuần cuối "
        "cùng tồn tại giữa hai bề mặt:"))
    b.append(EQ("Φ = Φ<sub>b</sub> + Φ<sub>s</sub> "
                "= <i>A</i> <i>ε</i> <i>ε</i><sub>s</sub> σ "
                "(<i>T</i><sup>4</sup> − <i>T</i><sub>s</sub><sup>4</sup>)", "32.107"))
    b.append(F54(lang))
    b.append(P(
        "This is a mathematical model of a net thermal flux that is converted by a thermal "
        "sensor into the output signal. It establishes a connection between the thermal power "
        "Φ absorbed by the sensor and the absolute temperatures of the object and the sensor. "
        "It should be noted that since the net radiation exists between the two bodies, the "
        "spectral density will have a maximum not described by Equation 32.92; depending on "
        "the temperature gradient, it will be somewhat shifted toward shorter wavelengths. "
        "Dynamically, the temperature T<sub>s</sub> of a thermal element in a sensor can, in "
        "general terms, be described by a first-order differential equation:",
        "Đây là mô hình toán học của thông lượng nhiệt thuần được cảm biến nhiệt biến đổi thành "
        "tín hiệu ngõ ra. Nó thiết lập liên hệ giữa công suất nhiệt Φ bị cảm biến hấp thụ với "
        "nhiệt độ tuyệt đối của vật và của cảm biến. Cần lưu ý rằng vì bức xạ thuần tồn tại giữa "
        "hai vật, mật độ phổ sẽ có cực đại không được mô tả bằng Phương trình 32.92; tùy theo "
        "gradient nhiệt độ, nó sẽ dịch đôi chút về phía bước sóng ngắn hơn. Về mặt động, nhiệt "
        "độ T<sub>s</sub> của phần tử nhiệt trong cảm biến, một cách tổng quát, được mô tả bằng "
        "phương trình vi phân bậc nhất:"))
    b.append(EQ("<i>m</i> <i>c</i> " + FR("d<i>T</i><sub>s</sub>", "d<i>t</i>")
                + " = <i>P</i> − <i>P</i><sub>L</sub> − Φ", "32.108"))
    b.append(P(
        "We select a positive sign for power P when it is directed toward the element. In the "
        "PIR detector (thermopiles, pyroelectrics and bolometers) no external power is supplied "
        "(P = 0); hence the speed of response depends only on the sensor's thermal capacity and "
        "heat loss, and is a first-order function characterized by a thermal time constant "
        "τ<sub>T</sub>.",
        "Ta chọn dấu dương cho công suất P khi nó hướng vào phần tử. Ở đầu dò PIR (nhiệt điện "
        "bội, nhiệt điện và bolometer), không có công suất ngoài nào được cấp (P = 0); vì thế "
        "tốc độ đáp ứng chỉ phụ thuộc dung lượng nhiệt và tổn hao nhiệt của cảm biến, và là hàm "
        "bậc nhất đặc trưng bởi hằng số thời gian nhiệt τ<sub>T</sub>."))
    b.append(P(
        "Thermopiles belong to the class of PIR detectors, and their operating principle is the "
        "same as that of thermocouples. In effect a thermopile can be defined as serially "
        "connected thermocouples. Originally invented by Joule to increase the output signal of "
        "a thermoelectric sensor, he connected several thermocouples in series and thermally "
        "joined their hot junctions. Presently thermopiles have a different configuration, their "
        "prime application being the detection of thermal radiation. A cut-out view is shown "
        "in Figure 32.55: the sensor consists of a base having a relatively large thermal mass, "
        "where the cold junctions are positioned; the base can be thermally coupled with a "
        "reference temperature sensor or attached to a thermostat at a known temperature. The "
        "base supports a thin membrane whose thermal capacity and thermal conductivity are "
        "small, and the membrane is the surface where the hot junctions are positioned.",
        "Nhiệt điện bội (thermopile) thuộc lớp đầu dò PIR, nguyên lý hoạt động giống hệt cặp "
        "nhiệt điện. Thực chất có thể định nghĩa thermopile là các cặp nhiệt điện mắc nối tiếp. "
        "Ban đầu Joule phát minh ra nó để tăng tín hiệu ngõ ra của cảm biến nhiệt điện: ông mắc "
        "nối tiếp vài cặp nhiệt điện và ghép nhiệt các mối nối nóng lại với nhau. Ngày nay "
        "thermopile có cấu hình khác, với ứng dụng chính là dò bức xạ nhiệt. Hình 32.55 là mặt "
        "cắt: cảm biến gồm một đế có khối lượng nhiệt tương đối lớn, nơi đặt các mối nối "
        "'nguội'; đế có thể ghép nhiệt với cảm biến nhiệt độ tham chiếu hoặc gắn vào bộ ổn nhiệt "
        "ở nhiệt độ đã biết. Đế đỡ một màng mỏng có dung lượng nhiệt và độ dẫn nhiệt nhỏ, và "
        "chính màng này là bề mặt đặt các mối nối 'nóng'."))
    b.append(P(
        "The best performance of a thermopile — high sensitivity and low noise — is achieved "
        "with junction materials having a high thermoelectric coefficient, low thermal "
        "conductivity and low volume resistivity; besides, the junction pairs should have "
        "thermoelectric coefficients of opposite signs. This dictates the choice of materials. "
        "Unfortunately, most metals having low resistivity (gold, copper, silver) have very poor "
        "thermoelectric coefficients, whereas the higher-resistivity metals — especially "
        "bismuth and antimony — possess high thermoelectric coefficients and are the prime "
        "selection for designing thermopiles. By doping these materials with Se and Te the "
        "thermoelectric coefficient has been improved up to 230 µV K⁻¹ [1]. Methods of "
        "construction differ in detail, but all incorporate vacuum deposition techniques and "
        "evaporation masks to apply thermoelectric materials such as bismuth and antimony on "
        "thin substrates (membranes). The number of junctions varies from 20 to several "
        "hundred. The hot junctions are often blackened (e.g. with gold-black or organic paint) "
        "to improve their absorptivity of infrared radiation. A thermopile is a dc device whose "
        "output voltage follows its hot-junction temperature quite well; it can be modeled as a "
        "thermal-flux-controlled voltage source connected in series with a fixed resistor, and "
        "the output voltage V<sub>s</sub> is nearly proportional to the incident radiation. An "
        "efficient thermopile can also be designed from semiconductor rather than double-metal "
        "junctions [2]: crystalline and polycrystalline silicon have very large thermoelectric "
        "coefficients and relatively low volume resistivity, with the advantage that standard "
        "IC processes can be employed. Resistivity and thermoelectric coefficients can be "
        "adjusted by doping concentration; however, resistivity increases much faster, so the "
        "doping must be carefully optimized for high sensitivity-to-noise ratios. Semiconductor "
        "thermopile sensors are produced by micromachining at EG&amp;G Heimann Optoelectronics "
        "GmbH (Wiesbaden, Germany) and Honeywell (Minneapolis, MN).",
        "Hiệu năng tốt nhất của thermopile — độ nhạy cao, nhiễu thấp — đạt được với vật liệu mối "
        "nối có hệ số nhiệt điện cao, độ dẫn nhiệt thấp và điện trở suất khối nhỏ; hơn nữa các "
        "cặp mối nối nên có hệ số nhiệt điện trái dấu. Điều đó chi phối việc chọn vật liệu. "
        "Tiếc là hầu hết kim loại có điện trở suất thấp (vàng, đồng, bạc) lại có hệ số nhiệt "
        "điện rất kém, trong khi các kim loại có điện trở suất cao hơn — đặc biệt là bitmut và "
        "antimon — sở hữu hệ số nhiệt điện cao và là lựa chọn hàng đầu để thiết kế thermopile. "
        "Bằng cách pha tạp các vật liệu này với Se và Te, hệ số nhiệt điện đã được nâng tới "
        "230 µV K⁻¹ [1]. Phương pháp chế tạo khác nhau đôi chút, nhưng đều dùng kỹ thuật lắng "
        "đọng chân không và mặt nạ bốc hơi để đặt vật liệu nhiệt điện như bitmut, antimon lên "
        "đế mỏng (màng). Số mối nối dao động từ 20 đến vài trăm. Các mối nối nóng thường được "
        "bôi đen (bằng vàng đen hay sơn hữu cơ) để tăng độ hấp thụ bức xạ hồng ngoại. "
        "Thermopile là linh kiện một chiều có điện áp ngõ ra bám khá sát nhiệt độ mối nối nóng; "
        "có thể mô hình hóa nó như nguồn áp điều khiển bằng thông lượng nhiệt mắc nối tiếp với "
        "một điện trở cố định, và điện áp ngõ ra V<sub>s</sub> gần như tỉ lệ với bức xạ tới. "
        "Cũng có thể thiết kế thermopile hiệu suất cao từ chất bán dẫn thay vì mối nối kim loại "
        "kép [2]: silic tinh thể và đa tinh thể có hệ số nhiệt điện rất lớn cùng điện trở suất "
        "khối tương đối thấp, với ưu điểm là dùng được quy trình IC chuẩn. Điện trở suất và hệ "
        "số nhiệt điện chỉnh được bằng nồng độ pha tạp; tuy nhiên điện trở suất tăng nhanh hơn "
        "nhiều, nên nồng độ pha tạp phải được tối ưu cẩn thận để đạt tỉ số độ nhạy trên nhiễu "
        "cao. Cảm biến thermopile bán dẫn được chế tạo bằng công nghệ gia công vi cơ tại "
        "EG&amp;G Heimann Optoelectronics GmbH (Wiesbaden, Đức) và Honeywell (Minneapolis, MN)."))
    b.append(F55(lang))
    b.append(P(
        "Pyroelectric sensors (see Chapter 6) also belong to the class of PIR detectors. A "
        "typical pyroelectric sensor is housed in a metal TO-5 or TO-39 can for better "
        "shielding and is protected from the environment by a silicon or other suitable window; "
        "the inner space of the can is often filled with dry air or nitrogen. Usually two "
        "sensing elements are oppositely connected, in series or in parallel, for better "
        "compensation of rapid thermal changes and of mechanical stresses resulting from "
        "acoustic noise and vibrations [3]. Bolometers are miniature RTDs or thermistors used "
        "mainly for measuring rms values of electromagnetic signals over a very broad spectral "
        "range, from microwaves to the near-infrared. An external bias power is applied to "
        "convert resistance changes into voltage changes. For infrared thermometers, bolometers "
        "are often fabricated as thin films of relatively large area, and their operating "
        "principle is based on the fundamental relationship between the absorbed "
        "electromagnetic signal and the dissipated power [3]. The sensitivity of a bolometer "
        "to incoming electromagnetic radiation can be defined as [4]:",
        "Cảm biến nhiệt điện (pyroelectric, xem Chương 6) cũng thuộc lớp đầu dò PIR. Cảm biến "
        "điển hình được đặt trong vỏ kim loại TO-5 hoặc TO-39 để che chắn tốt hơn và được bảo vệ "
        "khỏi môi trường bằng cửa sổ silic hay vật liệu phù hợp khác; khoảng bên trong vỏ thường "
        "nạp khí khô hoặc nitơ. Thường có hai phần tử cảm biến được mắc ngược chiều, nối tiếp "
        "hoặc song song, để bù tốt hơn các thay đổi nhiệt nhanh và ứng suất cơ học do nhiễu âm "
        "thanh và rung động [3]. Bolometer là RTD hay nhiệt điện trở thu nhỏ, chủ yếu dùng để đo "
        "giá trị hiệu dụng của tín hiệu điện từ trên dải phổ rất rộng, từ vi ba tới hồng ngoại "
        "gần. Một công suất phân cực ngoài được đặt vào để biến đổi thay đổi điện trở thành "
        "thay đổi điện áp. Đối với nhiệt kế hồng ngoại, bolometer thường chế thành màng mỏng có "
        "diện tích tương đối lớn, và nguyên lý hoạt động dựa trên quan hệ cơ bản giữa tín hiệu "
        "điện từ hấp thụ được và công suất tiêu tán [3]. Độ nhạy của bolometer với bức xạ điện "
        "từ tới có thể định nghĩa là [4]:"))
    b.append(EQ("<i>β</i> = "
                + FR("<i>ε</i> <i>α</i> <i>R</i><sub>0</sub> Δ<i>T</i><sub>0</sub>",
                     "(1 + <i>ω</i><sup>2</sup><i>τ</i><sup>2</sup>)<sup>1/2</sup>")
                + " = <i>α</i> <i>R</i><sub>0</sub> Δ<i>T</i>", "32.109"))
    b.append(P(
        "Bolometers are relatively slow sensors and are used primarily when no fast response is "
        "required. For thermal imaging, bolometers are available as two-dimensional arrays of "
        "about 80,000 sensors [5].",
        "Bolometer là cảm biến tương đối chậm, dùng chủ yếu khi không cần đáp ứng nhanh. Đối với "
        "tạo ảnh nhiệt, bolometer có dạng mảng hai chiều khoảng 80.000 phần tử [5]."))
    b.append(P(
        "In the active far-infrared (AFIR) sensor, the process of measuring thermal radiation "
        "flux differs from the passive (PIR) detectors described above. Contrary to a PIR "
        "sensing element, whose temperature depends on both ambient and object temperatures, "
        "the AFIR sensor's surface is actively controlled by a special circuit to have a "
        "defined temperature T<sub>s</sub> that, in most applications, is held constant during "
        "the entire measurement process [6]. To control the sensor's surface temperature, "
        "electric power P is provided by a control (or excitation) circuit (Figure 32.56). To "
        "regulate T<sub>s</sub>, the circuit measures the element's surface temperature and "
        "compares it with an internal reference. Obviously, the incoming power maintains "
        "T<sub>s</sub> higher than ambient, practically by just several tenths of a degree "
        "Celsius. Since the element's temperature is above ambient, the sensing element loses "
        "thermal energy toward its surroundings rather than passively absorbing it, as a PIR "
        "detector does. Part of the heat loss is thermal conduction, part thermal convection, "
        "and the rest thermal radiation — the third part being the one that must be measured. "
        "The net thermal flow (conductive + convective + radiative) must always come out of the "
        "sensor, i.e. it must have a negative sign.",
        "Ở cảm biến hồng ngoại xa chủ động (AFIR), quy trình đo thông lượng bức xạ nhiệt khác "
        "với các đầu dò thụ động (PIR) kể trên. Ngược với phần tử PIR có nhiệt độ phụ thuộc cả "
        "nhiệt độ môi trường lẫn nhiệt độ vật, bề mặt cảm biến AFIR được một mạch chuyên dụng "
        "điều khiển tích cực để có nhiệt độ T<sub>s</sub> xác định, và trong hầu hết ứng dụng "
        "được giữ không đổi suốt quá trình đo [6]. Để điều khiển nhiệt độ bề mặt, công suất "
        "điện P được cấp bởi mạch điều khiển (hay mạch kích thích) (Hình 32.56). Muốn điều chỉnh "
        "T<sub>s</sub>, mạch đo nhiệt độ bề mặt phần tử và so sánh với một tham chiếu nội. Rõ "
        "ràng công suất tới giữ T<sub>s</sub> cao hơn môi trường, thực tế chỉ vài phần mười độ "
        "Celsius. Vì nhiệt độ phần tử cao hơn môi trường, phần tử cảm biến mất năng lượng nhiệt "
        "về phía môi trường xung quanh thay vì hấp thụ thụ động như đầu dò PIR. Một phần tổn "
        "hao là dẫn nhiệt, một phần đối lưu nhiệt, phần còn lại là bức xạ nhiệt — chính phần thứ "
        "ba này cần được đo. Dòng nhiệt thuần (dẫn + đối lưu + bức xạ) luôn phải đi ra khỏi cảm "
        "biến, tức mang dấu âm."))
    b.append(P(
        "In the AFIR element, after a warm-up period the control circuit forces the element's "
        "surface temperature T<sub>s</sub> to stay constant; thus,",
        "Trong phần tử AFIR, sau giai đoạn khởi động, mạch điều khiển ép nhiệt độ bề mặt "
        "T<sub>s</sub> giữ không đổi; vì thế,"))
    b.append(EQ(FR("d<i>T</i><sub>s</sub>", "d<i>t</i>") + " = 0", "32.110"))
    b.append(P(
        "and Equation 32.108 becomes algebraic:",
        "và Phương trình 32.108 trở thành phương trình đại số:"))
    b.append(EQ("<i>P</i> = <i>P</i><sub>L</sub> + Φ", "32.111"))
    b.append(P(
        "It follows that, under idealized conditions, the response does not depend on thermal "
        "mass and is not a function of time, meaning practical AFIR sensors are quite fast. If "
        "the control circuit is highly efficient, since P<sub>L</sub> is constant at given "
        "ambient conditions, the electronically supplied power P should track changes in the "
        "radiated flux Φ with high fidelity. Nonradiative loss P<sub>L</sub> is a function of "
        "ambient temperature T<sub>a</sub> and a loss factor α<sub>s</sub>:",
        "Từ đó suy ra, trong điều kiện lý tưởng, đáp ứng không phụ thuộc khối lượng nhiệt và "
        "không là hàm của thời gian, nghĩa là cảm biến AFIR thực hành khá nhanh. Nếu mạch điều "
        "khiển có hiệu suất cao, vì P<sub>L</sub> không đổi ở điều kiện môi trường cho trước, "
        "công suất cấp bằng điện P sẽ bám sát mọi thay đổi của thông lượng bức xạ Φ. Tổn hao "
        "phi bức xạ P<sub>L</sub> là hàm của nhiệt độ môi trường T<sub>a</sub> và hệ số tổn hao "
        "α<sub>s</sub>:"))
    b.append(EQ("<i>P</i><sub>L</sub> = <i>α</i><sub>s</sub>"
                "(<i>T</i><sub>s</sub> − <i>T</i><sub>a</sub>)", "32.112"))
    b.append(P(
        "To generate heat in the AFIR sensor it may be provided with a heating element having "
        "electrical resistance R. During operation, the electric power dissipated by the "
        "heating element is a function of the voltage V across that resistance:",
        "Để sinh nhiệt trong cảm biến AFIR, người ta có thể bố trí một phần tử gia nhiệt có "
        "điện trở R. Trong khi hoạt động, công suất điện tiêu tán trên phần tử gia nhiệt là hàm "
        "của điện áp V trên điện trở ấy:"))
    b.append(EQ("<i>P</i> = " + FR("<i>V</i><sup>2</sup>", "<i>R</i>"), "32.113"))
    b.append(P(
        "Substituting Equations 32.107, 32.112 and 32.113 into Equation 32.111, assuming that "
        "T = T<sub>b</sub> and T<sub>s</sub> &gt; T<sub>a</sub>, and after simple "
        "manipulations, the object's temperature can be presented as a function of the voltage "
        "V across the heating element:",
        "Thay các Phương trình 32.107, 32.112 và 32.113 vào Phương trình 32.111, giả thiết "
        "T = T<sub>b</sub> và T<sub>s</sub> &gt; T<sub>a</sub>, sau vài biến đổi đơn giản, "
        "nhiệt độ của vật có thể biểu diễn như hàm của điện áp V trên phần tử gia nhiệt:"))
    b.append(EQ("<i>T</i><sub>b</sub> = [ <i>T</i><sub>s</sub><sup>4</sup> + "
                + FR("(<i>V</i><sup>2</sup>/<i>R</i>) − <i>α</i><sub>s</sub> Δ<i>T</i>",
                     "<i>A</i> σ <i>ε</i><sub>s</sub> <i>ε</i>")
                + " ]<sup>1/4</sup>", "32.114"))
    b.append(P(
        "One way to fabricate an AFIR element is to use a discrete thermistor having a "
        "relatively large surface area (3 mm² to 10 mm²) operated in a self-heating mode: the "
        "electric current passing through it raises its temperature above ambient, so the "
        "thermistor works as both heater and temperature sensor. Contrary to a PIR detector, an "
        "AFIR sensor is active and can generate a signal only when it works together with a "
        "control circuit. That circuit must include a reference to preset the controlled "
        "temperature, an error amplifier, and a driver stage for the heater; it may also "
        "include an RC network to correct the loop response function and stabilize operation, "
        "otherwise the whole system could be prone to oscillations [7]. It can be noted that an "
        "AFIR sensor together with its control circuit is a direct converter of thermal "
        "radiative power into electric voltage, and quite an efficient one: its typical "
        "responsivity is in the range of 3000 V W⁻¹, much higher than a thermopile, whose "
        "typical responsivity is around 100 V W⁻¹. A more detailed description can be found in "
        "[3, 6].",
        "Một cách chế tạo phần tử AFIR là dùng một nhiệt điện trở rời có diện tích bề mặt tương "
        "đối lớn (3 mm² đến 10 mm²) làm việc ở chế độ tự đốt nóng: dòng điện chạy qua làm nhiệt "
        "độ của nó tăng trên môi trường, nên nhiệt điện trở đảm nhiệm cả vai trò gia nhiệt lẫn "
        "cảm biến nhiệt độ. Ngược với đầu dò PIR, cảm biến AFIR là chủ động và chỉ sinh tín "
        "hiệu khi hoạt động cùng một mạch điều khiển. Mạch đó phải có: một tham chiếu để đặt "
        "nhiệt độ điều khiển, một khuếch đại sai số và một tầng lái cho phần tử gia nhiệt; "
        "ngoài ra có thể có mạng RC để chỉnh hàm đáp ứng vòng và ổn định hoạt động, nếu không "
        "toàn hệ dễ bị dao động [7]. Có thể thấy cảm biến AFIR cùng mạch điều khiển là bộ biến "
        "đổi trực tiếp công suất bức xạ nhiệt thành điện áp, và khá hiệu quả: độ đáp ứng điển "
        "hình cỡ 3000 V W⁻¹, cao hơn nhiều so với thermopile có độ đáp ứng điển hình khoảng "
        "100 V W⁻¹. Mô tả chi tiết hơn xem [3, 6]."))
    b.append(F56(lang))

    # ============================================================= Pyrometers
    b.append(H3("Pyrometers", "Nhiệt kế bức xạ (Pyrometer)"))
    b.append(H4("Disappearing Filament Pyrometer", "Nhiệt kế dây tóc biến mất"))
    b.append(P(
        "Additional names for the disappearing filament pyrometer include optical pyrometer and "
        "monochromatic-brightness radiation thermometer. This type is considered the most "
        "accurate radiation thermometer for temperatures over 700 °C. That limitation is a "
        "result of human-eye sensitivity within a specific wavelength. The operating principle "
        "is based on Planck's law (Equation 32.90 and Figure 32.48), which states that the "
        "intensity and color of a surface change with temperature. The idea behind the design "
        "is to balance radiation from an object of known temperature against the unknown "
        "temperature of a target. The pyrometer has a lens through which the operator views the "
        "target (Figure 32.57A), and an image of a tungsten filament is superimposed on the "
        "image of the target.",
        "Nhiệt kế dây tóc biến mất còn được gọi là nhiệt kế quang học hay nhiệt kế bức xạ độ sáng "
        "đơn sắc. Đây được coi là nhiệt kế bức xạ chính xác nhất cho nhiệt độ trên 700 °C. Giới "
        "hạn đó bắt nguồn từ độ nhạy của mắt người trong một vùng bước sóng hẹp. Nguyên lý hoạt "
        "động dựa trên định luật Planck (Phương trình 32.90 và Hình 32.48), theo đó cường độ và "
        "màu của bề mặt thay đổi theo nhiệt độ. Ý tưởng của thiết kế là cân bằng bức xạ từ một "
        "vật có nhiệt độ đã biết với nhiệt độ chưa biết của mục tiêu. Nhiệt kế có một thấu kính "
        "để người vận hành nhìn mục tiêu (Hình 32.57A), và ảnh của một dây tóc vonfram được "
        "chồng lên ảnh của mục tiêu."))
    b.append(P(
        "The filament is warmed by electric current to glow. During calibration the "
        "relationship between the current and the filament temperature was established by "
        "measuring the brightness of a blackbody of known temperature. The operator views the "
        "target through the eyepiece and manually adjusts the heating current until the image "
        "of the glowing filament visible in the foreground disappears — that is, when both "
        "target and filament have the same brightness and color. A color component complicates "
        "the measurement somewhat, so to remove this difficulty a narrow-band red filter "
        "(λ<sub>f</sub> = 0.65 µm) is inserted in front of the eyepiece; the operator then has "
        "to balance only the brightness of an image seen in red. Another advantage of the "
        "filter is that the emissivity ε<sub>bf</sub> of the target needs to be known only at "
        "λ<sub>f</sub>. The error in temperature measurement is given by [8]:",
        "Dây tóc được đốt nóng bằng dòng điện để phát sáng. Khi hiệu chuẩn, quan hệ giữa dòng "
        "và nhiệt độ dây tóc được thiết lập bằng cách đo độ sáng của một vật đen có nhiệt độ "
        "đã biết. Người vận hành nhìn mục tiêu qua thị kính và chỉnh tay dòng đốt đến mức ảnh "
        "dây tóc phát sáng ở tiền cảnh biến mất — tức khi mục tiêu và dây tóc có cùng độ sáng "
        "và màu. Thành phần màu làm phép đo phức tạp đôi chút; để khắc phục, một kính lọc đỏ "
        "dải hẹp (λ<sub>f</sub> = 0,65 µm) được đặt trước thị kính, nhờ đó người vận hành chỉ "
        "cần cân bằng độ sáng của ảnh nhìn thấy trong màu đỏ. Một lợi ích nữa của kính lọc là "
        "độ phát xạ ε<sub>bf</sub> của mục tiêu chỉ cần biết tại λ<sub>f</sub>. Sai số đo nhiệt "
        "độ được cho bởi [8]:"))
    b.append(EQ(FR("d<i>T</i><sub>b</sub>", "<i>T</i><sub>b</sub>")
                + " = − " + FR("<i>λ</i><sub>f</sub> <i>T</i><sub>b</sub>", "<i>C</i><sub>2</sub>")
                + FR("d<i>ε</i><sub>bf</sub>", "<i>ε</i><sub>bf</sub>"), "32.115"))
    b.append(P(
        "Thus, for a target at T<sub>b</sub> = 1000 K, a 10% uncertainty in knowing the "
        "emissivity of the target at the filter's wavelength results in only −0.45% (−4.5 K) "
        "uncertainty in measured temperature. The instrument can be further improved by "
        "removing the operator from the measurement loop. Figure 32.57B shows an automatic "
        "version where a rotating mirror tilted by 45° has a removed sector that allows light "
        "from the target to pass through to the photosensor. Such a mirror serves as a chopper, "
        "alternately sending light to the photosensor either from the target or from the "
        "filament. The microprocessor (µP) adjusts the current through the filament to bring "
        "the optical contrast to zero, and an optocoupler synchronizes the chopper with the "
        "microprocessor.",
        "Như vậy, với mục tiêu ở T<sub>b</sub> = 1000 K, độ bất định 10% khi biết độ phát xạ "
        "của mục tiêu tại bước sóng của kính lọc chỉ gây độ bất định −0,45% (−4,5 K) trong "
        "nhiệt độ đo được. Dụng cụ có thể cải tiến thêm bằng cách loại người vận hành khỏi vòng "
        "đo. Hình 32.57B là bản tự động, trong đó một gương quay nghiêng 45° có một cung bị cắt "
        "bỏ để ánh sáng từ mục tiêu đi qua tới cảm biến quang. Gương đó đóng vai trò bộ chặt "
        "chùm, lần lượt đưa ánh sáng từ mục tiêu hoặc từ dây tóc tới cảm biến quang. Vi xử lý "
        "(µP) chỉnh dòng qua dây tóc để đưa độ tương phản quang về không, còn một optocoupler "
        "đồng bộ bộ chặt chùm với vi xử lý."))
    b.append(F57(lang))

    b.append(H4("Two-color Pyrometer", "Nhiệt kế hai màu"))
    b.append(P(
        "Since emissivities of many materials are not known, measurement of a surface "
        "temperature can become impractical unless emissivity is excluded from the calculation. "
        "This can be accomplished by a ratiometric technique: the so-called two-color radiation "
        "thermometer, or ratio thermometer. In such a thermometer the radiation is detected at "
        "two separate wavelengths λ<sub>x</sub> and λ<sub>y</sub> for which the emissivities of "
        "the surface can be considered nearly the same. If the transmission coefficients of "
        "the optical system at each wavelength are respectively γ<sub>x</sub> and γ<sub>y</sub>, "
        "then the ratio of two Planck equations calculated for the two wavelengths is:",
        "Vì độ phát xạ của nhiều vật liệu không được biết, phép đo nhiệt độ bề mặt có thể trở "
        "nên không khả thi trừ khi loại được độ phát xạ khỏi phép tính. Điều đó thực hiện được "
        "bằng kỹ thuật tỉ lệ: cái gọi là nhiệt kế bức xạ hai màu, hay nhiệt kế tỉ số. Ở nhiệt "
        "kế này, bức xạ được dò tại hai bước sóng riêng biệt λ<sub>x</sub> và λ<sub>y</sub> mà "
        "ở đó độ phát xạ của bề mặt có thể coi là gần như bằng nhau. Nếu hệ số truyền qua của hệ "
        "quang tại mỗi bước sóng lần lượt là γ<sub>x</sub> và γ<sub>y</sub>, thì tỉ số của hai "
        "phương trình Planck tính cho hai bước sóng là:"))
    b.append(EQ("φ = "
                + FR("<i>γ</i><sub>x</sub> <i>ε</i>(<i>λ</i><sub>x</sub>) <i>W</i><sub>λx</sub>",
                     "<i>γ</i><sub>y</sub> <i>ε</i>(<i>λ</i><sub>y</sub>) <i>W</i><sub>λy</sub>")
                + " = "
                + FR("<i>γ</i><sub>x</sub> <i>ε</i>(<i>λ</i><sub>x</sub>) <i>λ</i><sub>y</sub><sup>5</sup> "
                     "(e<sup><i>C</i><sub>2</sub>/(<i>λ</i><sub>y</sub><i>T</i>)</sup> − 1)",
                     "<i>γ</i><sub>y</sub> <i>ε</i>(<i>λ</i><sub>y</sub>) <i>λ</i><sub>x</sub><sup>5</sup> "
                     "(e<sup><i>C</i><sub>2</sub>/(<i>λ</i><sub>x</sub><i>T</i>)</sup> − 1)"),
                "32.116"))
    b.append(P(
        "Because the emissivities ε(λ<sub>x</sub>) ≈ ε(λ<sub>y</sub>), after manipulation "
        "Equation 32.116 can be rewritten for the displayed temperature T<sub>c</sub>, where φ "
        "represents the ratio of the thermal radiation sensor outputs at the two wavelengths:",
        "Vì các độ phát xạ ε(λ<sub>x</sub>) ≈ ε(λ<sub>y</sub>), sau biến đổi, Phương trình "
        "32.116 có thể viết lại cho nhiệt độ hiển thị T<sub>c</sub>, với φ là tỉ số tín hiệu "
        "của cảm biến bức xạ nhiệt tại hai bước sóng:"))
    b.append(EQ("<i>T</i><sub>c</sub> ≈ "
                + FR("<i>C</i><sub>2</sub> (1/<i>λ</i><sub>y</sub> − 1/<i>λ</i><sub>x</sub>)",
                     "ln(φ <i>γ</i><sub>y</sub>/<i>γ</i><sub>x</sub>) − 5 ln(<i>λ</i><sub>y</sub>/<i>λ</i><sub>x</sub>)"),
                "32.117"))
    b.append(P(
        "It is seen that the equation for calculating temperature does not depend on the "
        "emissivity of the surface. Equation 32.117 is the basis for calculating temperature by "
        "taking the ratio of sensor outputs at two different wavelengths. Figure 32.58 shows a "
        "block diagram of an IR thermometer where an optical modulator is designed in the form "
        "of a disk with two filters.",
        "Ta thấy phương trình tính nhiệt độ không phụ thuộc vào độ phát xạ của bề mặt. Phương "
        "trình 32.117 là nền tảng để tính nhiệt độ bằng cách lấy tỉ số tín hiệu cảm biến tại "
        "hai bước sóng khác nhau. Hình 32.58 là sơ đồ khối của một nhiệt kế IR trong đó bộ "
        "điều chế quang được chế dưới dạng đĩa mang hai kính lọc."))
    b.append(F58(lang))

    # ========================================================== IR Thermometers
    b.append(H3("IR Thermometers", "Nhiệt kế hồng ngoại"))
    b.append(H4("Operating Principle", "Nguyên lý hoạt động"))
    b.append(P(
        "The operating principle of a noncontact infrared (IR) thermometer is based on the "
        "fundamental Stefan–Boltzmann law (Equation 32.95). For the purpose of calculating the "
        "object's temperature, when using a PIR sensor (thermopile, bolometer or pyroelectric), "
        "the equation can be manipulated as:",
        "Nguyên lý hoạt động của nhiệt kế hồng ngoại (IR) không tiếp xúc dựa trên định luật "
        "Stefan–Boltzmann nền tảng (Phương trình 32.95). Để tính nhiệt độ của vật khi dùng cảm "
        "biến PIR (thermopile, bolometer hay pyroelectric), phương trình được biến đổi thành:"))
    b.append(EQ("<i>T</i><sub>c</sub> = [ <i>T</i><sub>s</sub><sup>4</sup> + "
                + FR("Φ", "<i>A</i> σ <i>ε</i> <i>ε</i><sub>s</sub>")
                + " ]<sup>1/4</sup>", "32.118"))
    b.append(P(
        "where T<sub>c</sub> is the calculated object's temperature in kelvin. Hence, to "
        "calculate the temperature of an object one should first determine the magnitude of the "
        "net thermal radiation flux Φ and the sensor's surface temperature T<sub>s</sub>. The "
        "other parts of Equation 32.118 are treated as constants and must be determined during "
        "calibration of the instrument from a blackbody; the emissivity ε of the object must "
        "also be known before the calculation. In practice it is sometimes difficult to "
        "determine the exact temperature T<sub>s</sub> of the sensor's surface because of "
        "changing ambient conditions, drifts, handling of the instrument, and so on. In such "
        "cases the IR thermometer can be supplied with a reference target. The calculation can "
        "still be done with Equation 32.118; however, Φ will then mean a flux differential "
        "between the object and the reference target, and T<sub>s</sub> will represent the "
        "reference target temperature.",
        "trong đó T<sub>c</sub> là nhiệt độ vật tính được, tính bằng kelvin. Vì thế, muốn tính "
        "nhiệt độ của một vật, trước hết phải xác định độ lớn của thông lượng bức xạ nhiệt "
        "thuần Φ và nhiệt độ bề mặt T<sub>s</sub> của cảm biến. Các thành phần khác của Phương "
        "trình 32.118 được coi là hằng số và phải xác định khi hiệu chuẩn dụng cụ từ một vật "
        "đen; độ phát xạ ε của vật cũng phải biết trước khi tính. Thực hành đôi khi khó xác định "
        "chính xác nhiệt độ T<sub>s</sub> của bề mặt cảm biến vì điều kiện môi trường thay đổi, "
        "sự trôi, cách cầm dụng cụ, v.v. Trong những trường hợp đó, nhiệt kế IR có thể được "
        "trang bị một mục tiêu tham chiếu. Phép tính vẫn thực hiện được với Phương trình 32.118; "
        "tuy nhiên lúc này Φ mang nghĩa là hiệu thông lượng giữa vật và mục tiêu tham chiếu, còn "
        "T<sub>s</sub> biểu diễn nhiệt độ của mục tiêu tham chiếu."))
    b.append(P(
        "The object's temperature can also be calculated from Equation 32.118 with an AFIR "
        "sensor, but first the sensing element's surface temperature should be determined by "
        "measuring the temperature of the sensor's housing: T<sub>s</sub> = T<sub>a</sub> + ΔT, "
        "where ΔT is a constant. In addition, the value of V must be measured. The AFIR sensor "
        "allows continuous monitoring of temperature in a manner similar to thermopile "
        "sensors; its prime advantage is simplicity and low cost.",
        "Nhiệt độ của vật cũng có thể tính từ Phương trình 32.118 với cảm biến AFIR, nhưng trước "
        "hết phải xác định nhiệt độ bề mặt phần tử cảm biến bằng cách đo nhiệt độ vỏ cảm biến: "
        "T<sub>s</sub> = T<sub>a</sub> + ΔT, với ΔT là hằng số. Ngoài ra phải đo giá trị V. Cảm "
        "biến AFIR cho phép giám sát nhiệt độ liên tục tương tự cảm biến thermopile; ưu điểm "
        "chính của nó là đơn giản và giá rẻ."))

    b.append(H4("Continuous Monitoring of Temperature", "Giám sát nhiệt độ liên tục"))
    b.append(P(
        "Depending on the type of thermal radiation sensor employed, a noncontact infrared "
        "thermometer for continuous monitoring can incorporate different components. Thus, if "
        "a sensor with a dc response is used, the circuit might look like the one shown in "
        "Figure 32.59. It has the following essential components: the optical system (the "
        "lens), the IR sensor (a thermopile in this example), the reference (ambient) sensor, "
        "and a conventional data acquisition circuit. The dc-type sensors are thermopiles, "
        "bolometers and AFIR; when an AFIR sensor is used it should be supplied with an "
        "additional control circuit, as described above.",
        "Tùy loại cảm biến bức xạ nhiệt dùng, một nhiệt kế hồng ngoại không tiếp xúc để giám sát "
        "liên tục có thể gồm các thành phần khác nhau. Chẳng hạn, nếu dùng cảm biến có đáp ứng "
        "một chiều, mạch có thể như Hình 32.59, với các thành phần thiết yếu: hệ quang (thấu "
        "kính), cảm biến IR (ở đây là thermopile), cảm biến tham chiếu (môi trường) và mạch thu "
        "thập dữ liệu thông thường. Cảm biến kiểu một chiều gồm thermopile, bolometer và AFIR; "
        "khi dùng cảm biến AFIR phải cấp thêm mạch điều khiển như mô tả ở trên."))
    b.append(F59(lang))
    b.append(P(
        "In the case when an ac-type IR sensor is used (pyroelectric), the thermometer needs a "
        "chopper that breaks the IR radiation into a series of pulses, usually with a 50% duty "
        "cycle (Figure 32.60). The output of the amplifier is an alternating signal whose "
        "magnitude depends on both the chopping rate and the net IR radiation. The rotation of "
        "the chopper is synchronized with the data processing by the microprocessor by means "
        "of an optocoupler (LED and photodetector). It should be noted that the chopper not "
        "only converts the IR flux into an ac signal but also serves as a reference target, as "
        "described above. Use of a reference target can significantly improve IR thermometer "
        "accuracy; thus the chopper is often employed even with dc-type sensors, although it "
        "is not essential for operation. Naturally, the chopper's surface emissivity will be "
        "high and known.",
        "Trong trường hợp dùng cảm biến IR kiểu xoay chiều (pyroelectric), nhiệt kế cần một bộ "
        "chặt chùm cắt bức xạ IR thành chuỗi xung, thường với chu kỳ làm việc 50% (Hình "
        "32.60). Ngõ ra của khuếch đại là tín hiệu xoay chiều có biên độ phụ thuộc cả tần số "
        "chặt chùm lẫn bức xạ IR thuần. Vòng quay của bộ chặt chùm được đồng bộ với xử lý dữ "
        "liệu của vi xử lý nhờ một optocoupler (LED và đầu dò quang). Cần lưu ý bộ chặt chùm "
        "không chỉ biến thông lượng IR thành tín hiệu xoay chiều mà còn đóng vai trò mục tiêu "
        "tham chiếu như mô tả ở trên. Dùng mục tiêu tham chiếu có thể cải thiện đáng kể độ "
        "chính xác của nhiệt kế IR; vì thế bộ chặt chùm thường được dùng cả với cảm biến kiểu "
        "một chiều, dù không bắt buộc cho hoạt động. Dĩ nhiên độ phát xạ bề mặt của bộ chặt "
        "chùm sẽ cao và đã biết."))
    b.append(F60(lang))

    b.append(H4("Intermittent Monitoring of Temperature", "Giám sát nhiệt độ gián đoạn"))
    b.append(P(
        "Obviously, any infrared thermometer capable of continuous monitoring of temperature "
        "can be made operational in the intermittent mode: the continuous temperature can be "
        "processed to extract a single value of interest to the user, for example a maximum, "
        "a minimum, or a time-averaged temperature. Yet it is also possible to design a "
        "low-cost IR thermometer that takes only a 'snapshot' of the temperature at any "
        "specific moment. Such a thermometer can be designed with a pyroelectric sensor that "
        "produces electric charge virtually instantaneously upon receiving the IR radiation. "
        "Figure 32.61A shows a block diagram: a mechanical or electromechanical shutter is "
        "positioned in front of the pyroelectric sensor, and the shutter surface serves as a "
        "reference target. When the shutter is closed the sensor produces no output; "
        "immediately upon shutter actuation the pyroelectric current flows from the sensor into "
        "an amplifier containing a charge-to-voltage converter. The sensor's current response "
        "has a shape close to an exponential function (Figure 32.61B), and the magnitude of "
        "the spike is nearly proportional to the IR flux at the moment of shutter opening. "
        "The pyroelectric thermometer is widely used for medical purposes and is dubbed the "
        "'instant thermometer.'",
        "Rõ ràng bất kỳ nhiệt kế hồng ngoại nào có khả năng giám sát liên tục cũng có thể chuyển "
        "sang chế độ gián đoạn: nhiệt độ liên tục được xử lý để trích ra một giá trị duy nhất "
        "mà người dùng quan tâm, chẳng hạn giá trị cực đại, cực tiểu hay nhiệt độ trung bình "
        "theo thời gian. Tuy nhiên cũng có thể thiết kế một nhiệt kế IR giá rẻ chỉ 'chụp' nhiệt "
        "độ tại một thời điểm bất kỳ. Nhiệt kế như vậy dùng cảm biến pyroelectric sinh ra điện "
        "tích gần như tức thời khi nhận bức xạ IR. Hình 32.61A là sơ đồ khối: một cửa chớp cơ "
        "hoặc cơ điện đặt trước cảm biến pyroelectric, và bề mặt cửa chớp đóng vai trò mục tiêu "
        "tham chiếu. Khi cửa chớp đóng, cảm biến không có ngõ ra; ngay khi cửa chớp mở, dòng "
        "pyroelectric chảy từ cảm biến vào khuếch đại có bộ biến đổi điện tích thành điện áp. "
        "Đáp ứng dòng của cảm biến có dạng gần hàm e mũ (Hình 32.61B), và biên độ xung gần như "
        "tỉ lệ với thông lượng IR ở thời điểm cửa chớp mở. Nhiệt kế pyroelectric được dùng rộng "
        "rãi trong y tế và được mệnh danh là 'nhiệt kế tức thời'."))
    b.append(F61(lang))

    b.append(H4("Response Speed", "Tốc độ đáp ứng"))
    b.append(P(
        "All infrared thermometers are relatively fast; their typical response time is on the "
        "order of a second. Along with the noncontact way of taking temperature, this makes "
        "them very convenient whenever fast tracking of temperature is essential. However, an "
        "IR thermometer, while being very fast, can still require a relatively long warm-up "
        "time and may not be accurate whenever it is moved from one environment to another "
        "without having enough time to adapt to the new ambient temperature. The reason is "
        "that the reference and IR sensors (or the IR sensor and the shutter or chopper) must "
        "be in thermal equilibrium with one another; otherwise the calculated temperature is "
        "erroneous.",
        "Mọi nhiệt kế hồng ngoại đều tương đối nhanh; thời gian đáp ứng điển hình cỡ một giây. "
        "Cùng với cách lấy nhiệt độ không tiếp xúc, điều này khiến chúng rất tiện khi cần theo "
        "dõi nhiệt độ nhanh. Tuy nhiên, dù rất nhanh, nhiệt kế IR vẫn có thể cần thời gian khởi "
        "động tương đối lâu và có thể không chính xác khi chuyển từ môi trường này sang môi "
        "trường khác mà không có đủ thời gian thích nghi với nhiệt độ môi trường mới. Lý do là "
        "cảm biến tham chiếu và cảm biến IR (hoặc cảm biến IR với cửa chớp/bộ chặt chùm) phải "
        "ở trạng thái cân bằng nhiệt với nhau; nếu không, nhiệt độ tính ra sẽ sai."))

    b.append(H4("Components of IR Thermometers", "Các thành phần của nhiệt kế hồng ngoại"))
    b.append(P(
        "A practical instrument combines an optical system that gathers and selects the "
        "radiation, a thermal radiation detector that converts the net flux into an electrical "
        "signal, a reference or chopper that defines the baseline, signal-conditioning "
        "electronics, and a computation stage that solves Equation 32.118. The following "
        "subsections examine the optical and mechanical components that most strongly affect "
        "accuracy: shutters and choppers, filters and lenses, and waveguides.",
        "Một dụng cụ thực hành kết hợp hệ quang thu gom và chọn lọc bức xạ, một đầu dò bức xạ "
        "nhiệt biến thông lượng thuần thành tín hiệu điện, một mục tiêu tham chiếu hay bộ chặt "
        "chùm xác định đường nền, mạch điều hòa tín hiệu, và một tầng tính toán giải Phương "
        "trình 32.118. Các mục dưới đây khảo sát những thành phần quang và cơ khí ảnh hưởng "
        "mạnh nhất tới độ chính xác: cửa chớp và bộ chặt chùm, bộ lọc và thấu kính, cùng ống "
        "dẫn sóng."))

    b.append(H4("Optical Choppers and Shutters", "Bộ chặt chùm và cửa chớp quang học"))
    b.append(P(
        "The shutters or choppers must possess the following properties: (1) they should have "
        "a high surface emissivity that does not change with time; (2) the opening and closing "
        "speed must be high; (3) the thermal conductivity between the front and back sides of "
        "the blade should be as small as possible; (4) the blade should be in good thermal "
        "contact with the reference sensor; and (5) while operating, the blade should not wear "
        "off or produce microscopic particles of dust that could contaminate the optical "
        "components of the IR thermometer. For operation in the visible and near-infrared "
        "portions of the spectrum, when measured temperatures are over 800 K, the shutter can "
        "be fabricated as a solid-state device without moving components (e.g. employing "
        "liquid crystals). However, for longer wavelengths only mechanical blades are useful. "
        "Special attention should be paid to preventing the shutter or chopper from reflecting "
        "any spurious thermal radiation originating from within the IR thermometer housing.",
        "Cửa chớp hay bộ chặt chùm phải có các tính chất sau: (1) độ phát xạ bề mặt cao và không "
        "đổi theo thời gian; (2) tốc độ đóng mở cao; (3) độ dẫn nhiệt giữa mặt trước và mặt sau "
        "cánh càng nhỏ càng tốt; (4) cánh phải tiếp xúc nhiệt tốt với cảm biến tham chiếu; và "
        "(5) khi hoạt động, cánh không được mài mòn hay sinh hạt bụi vi mô có thể làm bẩn các "
        "thành phần quang của nhiệt kế IR. Đối với vùng nhìn thấy và hồng ngoại gần, khi nhiệt "
        "độ đo trên 800 K, cửa chớp có thể chế dạng linh kiện thể rắn không có bộ phận chuyển "
        "động (thí dụ dùng tinh thể lỏng). Tuy nhiên với bước sóng dài hơn, chỉ cánh cơ khí mới "
        "dùng được. Cần đặc biệt lưu ý ngăn cửa chớp hay bộ chặt chùm phản xạ bất kỳ bức xạ "
        "nhiệt giả nào phát sinh từ bên trong vỏ nhiệt kế IR."))

    b.append(H4("Filters and Lenses", "Bộ lọc và thấu kính"))
    b.append(P(
        "The IR filters and lenses serve two purposes: they selectively pass specific "
        "wavelengths to the sensing components, and they protect the interior of the "
        "instrument from contamination by outside pollutants. In addition, lenses — due to "
        "their refractive properties — divert light rays into a specific direction [3]. In "
        "IR thermometry the selection of filters and lenses is limited to a relatively short "
        "list. Table 32.18 lists some materials that are transparent in the infrared range. "
        "Note that most of these materials have a relatively high refractive index, which "
        "means they have high surface-reflection loss. For example, silicon (the cheapest "
        "material for IR windows) reflects over 46% of incoming radiation which, along with "
        "the absorptive loss, amounts to an even higher combined loss. To a certain degree "
        "this problem can be solved by applying special antireflective (AR) coatings on both "
        "surfaces of the window or lens. These coatings are geared to specific wavelengths, so "
        "for a broad bandwidth a multilayer coating may need to be deposited by sputtering.",
        "Bộ lọc và thấu kính IR phục vụ hai mục đích: chọn lọc cho các bước sóng xác định đi "
        "tới bộ phận cảm biến, và bảo vệ bên trong dụng cụ khỏi nhiễm bẩn từ các chất ô nhiễm "
        "bên ngoài. Thêm vào đó, thấu kính — nhờ tính chất khúc xạ — làm lệch tia sáng theo một "
        "hướng xác định [3]. Trong đo nhiệt hồng ngoại, danh sách vật liệu làm bộ lọc và thấu "
        "kính khá ngắn. Bảng 32.18 liệt kê một số vật liệu trong suốt trong vùng hồng ngoại. "
        "Lưu ý hầu hết các vật liệu này có chiết suất tương đối cao, nghĩa là tổn hao phản xạ "
        "bề mặt lớn. Thí dụ, silic (vật liệu rẻ nhất làm cửa sổ IR) phản xạ hơn 46% bức xạ tới, "
        "cộng với tổn hao hấp thụ nên tổn hao tổng còn cao hơn. Ở mức độ nào đó, có thể khắc "
        "phục bằng cách phủ lớp chống phản xạ (AR) chuyên biệt trên cả hai mặt của cửa sổ hay "
        "thấu kính. Các lớp phủ này gắn với bước sóng cụ thể, nên với dải rộng có thể cần phủ "
        "đa lớp bằng quy trình phún xạ."))
    b.append(_t3218(lang))
    b.append(P(
        "Another problem with IR refractive materials is the relatively high absorption of "
        "light. This becomes a serious limitation for lenses, as they need to be produced "
        "with appreciable thickness. The solution is to select materials with low absorption "
        "in the spectral range of interest — examples are zinc selenide (ZnSe) and AMTIR. "
        "Another solution is the use of polyethylene Fresnel lenses, which are much thinner "
        "and less expensive [3]. Any window or lens that is absorptive will also emanate "
        "thermal radiation according to its own temperature; hence, to minimize this effect "
        "on the overall accuracy of an IR thermometer, the refractive devices should be kept "
        "at the same temperature as the IR sensor, the shutter (chopper), and the reference "
        "sensor.",
        "Một vấn đề nữa với vật liệu khúc xạ IR là độ hấp thụ ánh sáng tương đối cao. Đây là "
        "hạn chế nghiêm trọng đối với thấu kính vì chúng cần được chế với chiều dày đáng kể. "
        "Cách giải quyết là chọn vật liệu có độ hấp thụ thấp trong dải phổ quan tâm — thí dụ "
        "kẽm selenua (ZnSe) và AMTIR. Một cách khác là dùng thấu kính Fresnel bằng polyetylen, "
        "mỏng hơn nhiều và rẻ hơn [3]. Bất kỳ cửa sổ hay thấu kính nào có hấp thụ cũng sẽ tự "
        "phát bức xạ nhiệt theo nhiệt độ của chính nó; vì thế, để giảm thiểu ảnh hưởng này lên "
        "độ chính xác tổng thể của nhiệt kế IR, các linh kiện khúc xạ nên được giữ ở cùng nhiệt "
        "độ với cảm biến IR, cửa chớp (bộ chặt chùm) và cảm biến tham chiếu."))

    b.append(H4("Waveguides", "Ống dẫn sóng"))
    b.append(P(
        "Waveguides are optical components intended for channeling IR radiation from one "
        "point to another. Usually they are used when an IR sensor cannot be positioned close "
        "to the source of thermal radiation, yet must have a wide field of view. These "
        "components employ light reflection and are not focusing, even if they are designed "
        "with refractive materials. If focusing is required, waveguides can be combined with "
        "lenses and curved or tilted mirrors. A waveguide has relatively wide entry and exit "
        "angles; a typical application is in a medical IR thermometer, where the waveguide is "
        "inserted into an ear canal (Figure 32.61).",
        "Ống dẫn sóng là thành phần quang dùng để dẫn bức xạ IR từ điểm này tới điểm khác. "
        "Thường dùng khi không thể đặt cảm biến IR gần nguồn bức xạ nhiệt, nhưng vẫn cần trường "
        "nhìn rộng. Các thành phần này dùng sự phản xạ ánh sáng và không hội tụ, dù có chế từ "
        "vật liệu khúc xạ. Nếu cần hội tụ, có thể kết hợp ống dẫn sóng với thấu kính và gương "
        "cong hoặc gương nghiêng. Ống dẫn sóng có góc vào và góc ra tương đối rộng; ứng dụng "
        "điển hình là nhiệt kế IR y tế, trong đó ống dẫn sóng được đưa vào ống tai (Hình "
        "32.61)."))
    b.append(P(
        "There are three types of waveguides: hollow tubes (barrels), optical fibers, and rods "
        "[3, 9, 10]. The latter two are made of IR-transparent materials such as ZnSe or "
        "AMTIR and use the angle of total internal reflection to propagate light inside in a "
        "zigzag pattern (Figure 32.62). The barrels are hollow tubes, polished and "
        "gold-plated on the inner surface.",
        "Có ba loại ống dẫn sóng: ống rỗng (barrel), sợi quang và thanh đặc [3, 9, 10]. Hai "
        "loại sau làm từ vật liệu trong suốt với IR như ZnSe hay AMTIR, dùng góc phản xạ toàn "
        "phần để truyền ánh sáng bên trong theo đường zigzag (Hình 32.62). Các barrel là ống "
        "rỗng, được đánh bóng và mạ vàng ở mặt trong."))
    b.append(F62(lang))

    b.append(H4("Error Sources in IR Thermometry", "Nguồn sai số trong đo nhiệt hồng ngoại"))
    b.append(P(
        "Any error in detection of either radiated flux Φ or reference temperature "
        "T<sub>a</sub> will result in inaccuracy in the displayed temperature. According to "
        "Equation 32.118, the emissivities of both the sensor (ε<sub>s</sub>) and the object "
        "(ε) must be known for accurate detection of thermal flux. Emissivity of the sensor "
        "usually remains constant and is taken care of during calibration. However, "
        "uncertainty in the value of the object's emissivity can result in significant "
        "uncertainty in temperatures measured by noncontact infrared thermometers "
        "(Figure 32.63).",
        "Bất kỳ sai số nào khi xác định thông lượng bức xạ Φ hay nhiệt độ tham chiếu "
        "T<sub>a</sub> đều gây sai số cho nhiệt độ hiển thị. Theo Phương trình 32.118, muốn xác "
        "định chính xác thông lượng nhiệt phải biết độ phát xạ của cả cảm biến "
        "(ε<sub>s</sub>) lẫn của vật (ε). Độ phát xạ của cảm biến thường không đổi và được tính "
        "đến khi hiệu chuẩn. Tuy nhiên, độ bất định về giá trị độ phát xạ của vật có thể gây độ "
        "bất định đáng kể cho nhiệt độ đo bằng nhiệt kế hồng ngoại không tiếp xúc (Hình "
        "32.63)."))
    b.append(F63(lang))
    b.append(P(
        "Another source of error is spurious heat sources, which can emanate their thermal "
        "radiation either directly into the optical system of an IR thermometer, or by "
        "reflection from the measured surface [11]. Since no surface is an ideal emitter "
        "(absorber), its reflectivity may have a significant value. For example, an opaque "
        "object with emissivity 0.9 has reflectivity 0.1 (Equation 32.96); thus about 10% of "
        "the radiation from a hot object in the vicinity of the measured surface is reflected "
        "and can greatly disturb the measurement. Since emissivities of metals are quite small "
        "and one never can be sure about their actual values, it is advisable, whenever "
        "practical, to coat a portion of a metal surface with a dielectric material, such as "
        "a metal oxide or an organic paint of known emissivity. Alternatively, temperatures "
        "should not be taken from a flat surface but rather from a hole or cavity that has a "
        "nonmetallic surface inside.",
        "Một nguồn sai số khác là các nguồn nhiệt giả, có thể phát bức xạ nhiệt thẳng vào hệ "
        "quang của nhiệt kế IR, hoặc qua phản xạ từ bề mặt cần đo [11]. Vì không bề mặt nào là "
        "bộ phát (bộ hấp thụ) lý tưởng, độ phản xạ của nó có thể đáng kể. Thí dụ, một vật đục "
        "có độ phát xạ 0,9 thì có độ phản xạ 0,1 (Phương trình 32.96); vì thế khoảng 10% bức "
        "xạ từ một vật nóng ở gần bề mặt đo bị phản xạ và có thể làm nhiễu phép đo nghiêm "
        "trọng. Vì độ phát xạ của kim loại khá nhỏ và không bao giờ chắc chắn về giá trị thực "
        "của nó, nên khi có thể, tốt nhất là phủ một phần bề mặt kim loại bằng vật liệu điện "
        "môi như oxit kim loại hay sơn hữu cơ có độ phát xạ đã biết. Hoặc không đo trên mặt "
        "phẳng mà đo từ một lỗ hay hốc có bề mặt phi kim bên trong."))
    b.append(P(
        "Another source of error is thermal instability of the thermal sensing element. For "
        "example, in a thermopile or pyroelectric sensor, upon exposure to thermal radiation "
        "the element's temperature might increase above ambient by just a few millidegrees. "
        "Hence, if for some reason the element's temperature varies by the same amount, the "
        "output signal becomes indistinguishable from that produced by the thermal flux. To "
        "minimize these errors, infrared sensors are encapsulated into metal bodies having "
        "high thermal capacity and poor coupling to the environment (high thermal "
        "resistance), which helps stabilize the temperature of the sensor. Another powerful "
        "technique is to fabricate the IR sensor in a dual form, that is, with two identical "
        "sensing elements: one is subjected to an IR signal while the other is shielded from "
        "it, and the signals from the elements are subtracted, thus canceling the drifts that "
        "affect both elements [3].",
        "Một nguồn sai số nữa là sự bất ổn nhiệt của phần tử cảm biến nhiệt. Thí dụ, trong cảm "
        "biến thermopile hay pyroelectric, khi chiếu bức xạ nhiệt, nhiệt độ phần tử có thể chỉ "
        "tăng trên môi trường vài phần nghìn độ. Vì thế, nếu vì lý do nào đó nhiệt độ phần tử "
        "dao động đúng chừng ấy, tín hiệu ngõ ra trở nên không phân biệt được với tín hiệu do "
        "thông lượng nhiệt sinh ra. Để giảm các sai số này, cảm biến hồng ngoại được bọc trong "
        "thân kim loại có dung lượng nhiệt lớn và ghép nối kém với môi trường (điện trở nhiệt "
        "cao), giúp ổn định nhiệt độ cảm biến. Một kỹ thuật hữu hiệu khác là chế cảm biến IR "
        "dạng kép, tức gồm hai phần tử cảm biến giống hệt nhau: một nhận tín hiệu IR, một được "
        "che chắn; tín hiệu của hai phần tử được trừ đi, nhờ đó triệt tiêu các độ trôi ảnh "
        "hưởng đồng thời lên cả hai [3]."))

    b.append(H4("Semiconductor Materials", "Vật liệu bán dẫn"))
    b.append(P(
        "Some special applications deserve separate mention. Temperature measurement of "
        "semiconductor material during processing, such as growth of epitaxial films in "
        "vacuum chambers, has always been a difficult problem. Various process controls "
        "require accurate temperature monitoring, often without physical contact with the "
        "substrates. As a rule, heating of a substrate is provided by resistive heaters, and "
        "the substrates are often loaded into the chambers through various locks and rotated "
        "during processing. It is therefore very difficult to attach a contact sensor such as "
        "a thermocouple to the wafer; and even if one does, the thermal gradient between the "
        "sensor and the substrate may be so large that the result should never be trusted. "
        "The attractive alternative is optical pyrometry, but this presents another set of "
        "difficulties: semiconductors are substantially transparent in the spectral region "
        "where thermal radiation would be emanated, so their emissivity is negligibly small "
        "and the amount of thermal radiation is not only small but, because of wafer "
        "transparency, radiation from underlying devices (e.g. the heater) passes through to "
        "the IR thermometer.",
        "Một số ứng dụng đặc biệt đáng được nhắc riêng. Đo nhiệt độ vật liệu bán dẫn trong quá "
        "trình gia công, chẳng hạn mọc màng epitaxy trong buồng chân không, luôn là bài toán "
        "khó. Nhiều quy trình điều khiển đòi hỏi giám sát nhiệt độ chính xác, thường không được "
        "tiếp xúc vật lý với đế. Theo lệ, đế được gia nhiệt bằng điện trở đốt nóng, và thường "
        "được nạp vào buồng qua các khóa nạp khác nhau rồi quay trong suốt quá trình. Vì thế "
        "rất khó gắn cảm biến tiếp xúc như cặp nhiệt điện lên tấm wafer; và dù có gắn được, "
        "gradient nhiệt giữa cảm biến và đế có thể lớn đến mức không bao giờ nên tin vào kết "
        "quả. Giải pháp hấp dẫn là đo nhiệt quang học, nhưng lại nảy sinh khó khăn khác: chất "
        "bán dẫn trong suốt đáng kể trong vùng phổ nơi bức xạ nhiệt sẽ phát ra, nên độ phát xạ "
        "của chúng nhỏ không đáng kể và lượng bức xạ nhiệt không chỉ ít mà — do wafer trong "
        "suốt — bức xạ từ các thiết bị bên dưới (như bếp gia nhiệt) còn xuyên qua tới nhiệt kế "
        "IR."))
    b.append(P(
        "One relatively simple method is to coat a small portion of the semiconductor with a "
        "material having high emissivity in the IR spectral range, then measure the thermal "
        "radiation from that patch; an example of such a material is nichrome (see Table "
        "32.17). An attractive method of temperature monitoring, when no emissive patch can "
        "be deposited, uses the temperature dependence of the bandgaps of common "
        "semiconductors: the bandgap is determined from the threshold wavelength at which "
        "radiation from the heaters behind the substrate is transmitted through the substrate "
        "[12]. Another method is based on the temperature dependence of diffuse reflection of "
        "a semiconductor. In effect this method is similar to the former, but relies on "
        "reflection rather than transmission of the semiconductor. An external lamp is used "
        "for measuring a threshold wavelength from a front-polished and backside-textured "
        "substrate [13]. The temperature measurement arrangement is shown in Figure 32.64, "
        "where the diffused light is detected by a cryogenically cooled quantum detector. The "
        "monochromator has a resolution of 3 nm and scans through the threshold area at a "
        "rate of 100 nm/s.",
        "Một phương pháp tương đối đơn giản là phủ một phần nhỏ của bán dẫn bằng vật liệu có độ "
        "phát xạ cao trong vùng phổ IR, rồi đo bức xạ nhiệt từ miếng vá đó; thí dụ vật liệu như "
        "vậy là nichrome (xem Bảng 32.17). Một phương pháp giám sát nhiệt độ hấp dẫn, khi không "
        "thể tạo miếng vá phát xạ, dùng sự phụ thuộc nhiệt độ của vùng cấm các chất bán dẫn "
        "thông dụng: vùng cấm được xác định từ bước sóng ngưỡng mà tại đó bức xạ từ bếp gia "
        "nhiệt phía sau đế truyền xuyên qua đế [12]. Một phương pháp khác dựa trên sự phụ thuộc "
        "nhiệt độ của phản xạ khuếch tán của bán dẫn. Thực chất phương pháp này giống phương "
        "pháp trước, nhưng dựa vào phản xạ thay vì truyền qua của bán dẫn. Một đèn ngoài được "
        "dùng để đo bước sóng ngưỡng từ đế có mặt trước đánh bóng và mặt sau nhám [13]. Bố trí "
        "đo nhiệt độ được nêu ở Hình 32.64, trong đó ánh sáng khuếch tán được dò bằng đầu dò "
        "lượng tử làm lạnh sâu. Đơn sắc kế có độ phân giải 3 nm và quét qua vùng ngưỡng với tốc "
        "độ 100 nm/s."))
    b.append(F64(lang))

    b.append(H4("Medical Applications", "Ứng dụng y tế"))
    b.append(P(
        "Medical infrared thermometry has two distinct types of measurements: body "
        "temperature measurement and skin surface temperature measurement. Skin temperature "
        "measurements have specific applications in determining the surface temperature of a "
        "human body, but that temperature depends greatly on both skin blood perfusion and "
        "environmental conditions; therefore skin temperature cannot be independently "
        "correlated with the internal body temperature. Now it is customary to measure "
        "internal body temperature by placing the probe of an IR thermometer into the ear "
        "canal aiming it at the tympanic membrane [14], whose temperature is close to that of "
        "the blood. As a rule the probe is designed with a gold-plated waveguide (Figure "
        "32.61), protected either by a semiconductor or polymer window.",
        "Đo nhiệt hồng ngoại y tế có hai dạng phép đo riêng biệt: đo nhiệt độ cơ thể và đo nhiệt "
        "độ bề mặt da. Đo nhiệt độ da có ứng dụng cụ thể trong xác định nhiệt độ bề mặt cơ thể "
        "người, nhưng nhiệt độ đó phụ thuộc rất nhiều vào tưới máu da lẫn điều kiện môi trường; "
        "vì thế không thể liên hệ độc lập nhiệt độ da với nhiệt độ bên trong cơ thể. Ngày nay "
        "thường đo nhiệt độ bên trong cơ thể bằng cách đưa đầu dò của nhiệt kế IR vào ống tai, "
        "hướng về màng nhĩ [14], vì màng nhĩ có nhiệt độ gần với nhiệt độ máu. Theo lệ, đầu dò "
        "được thiết kế với ống dẫn sóng mạ vàng (Hình 32.61), được bảo vệ bằng cửa sổ bán dẫn "
        "hoặc polymer."))
    b.append(P(
        "Because a medical IR thermometer is used in direct contact with patient tissues, it "
        "is imperative to protect the probe from becoming a carrier of soiling compounds and a "
        "transmitter of infection from one patient to another (cross-contamination), or even "
        "from re-infecting the same patient (recontamination). Thus a probe of a medical IR "
        "thermometer is protected by a special probe cover made of a polymer film "
        "(polyethylene, polypropylene, etc.) transparent in the spectrum range of thermal "
        "radiation. In effect the probe cover becomes part of the optical system, which "
        "demands that covers be produced with very tight tolerances so that they will not "
        "significantly affect transmission of the IR signal.",
        "Vì nhiệt kế IR y tế dùng tiếp xúc trực tiếp với mô bệnh nhân, bắt buộc phải bảo vệ đầu "
        "dò không trở thành vật mang chất bẩn và trung gian truyền nhiễm từ bệnh nhân này sang "
        "bệnh nhân khác (nhiễm chéo), hay thậm chí tái nhiễm chính bệnh nhân đó. Vì thế đầu dò "
        "nhiệt kế IR y tế được bảo vệ bằng một nắp chuyên dụng làm từ màng polymer "
        "(polyetylen, polypropylen, v.v.) trong suốt trong dải phổ của bức xạ nhiệt. Thực chất "
        "nắp đầu dò trở thành một phần của hệ quang, đòi hỏi nắp phải được sản xuất với dung "
        "sai rất chặt để không ảnh hưởng đáng kể tới sự truyền tín hiệu IR."))

    b.append(refs(lang))
    return "".join(b)


def sec_vi():
    return _section("vi")


def sec_en():
    return _section("en")
