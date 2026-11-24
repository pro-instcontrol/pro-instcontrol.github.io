# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III" — final section (EN/VI bilingual).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 202-215, printed pp. 190-203,
decoded text lines 7720-8149.  Continues the level-measurement discussion
of `ipc_ch03_h.py` (differential-pressure schemes, valve manifolds, diaphragm
seals, capacitance and magnetic level gages, nucleonic level measurement),
then the chapter exercises and the printed thermocouple EMF calibration
tables.  Figures 3.62-3.72 are supplied by `ipcfig3_d.py`; equation (3.45)
is rendered with literal Unicode.  Every printed calibration value is kept,
with the deliberately wide tables split into narrower column bands.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


# ---------------------------------------------------------------------------
# Calibration data.  Each record is (row label, cell, cell, ...), one cell per
# printed temperature column; a cell is "main/diff" (diff = small difference
# printed below the main reading), "main" when no difference is printed and
# "" for a genuinely blank cell.  Values are reproduced exactly as printed,
# including such printer's quirks as "130.276", "60.64", ".17" and ".95".
# ---------------------------------------------------------------------------
_TEMP = ["0 °C", "100 °C", "200 °C", "300 °C", "400 °C", "500 °C",
         "600 °C", "700 °C", "800 °C", "900 °C", "1000 °C", "1100 °C",
         "1200 °C", "1300 °C", "1400 °C", "1500 °C", "1600 °C", "1700 °C",
         "1800 °C"]

_S = [
    ("0°", "0/.055", "0.645/.074", "1.440/.085", "2.323/.091", "3.260/.096",
     "4.234/.099", "5.237/.102", "6.274/.106", "7.345/.109", "8.448/.112",
     "9.585/.115", "10.754/.118", "11.947/.120", "13.155/.121",
     "14.368/.121", "15.576/.121", "16.771/.119", "17.942/.114"),
    ("10°", "0.055/.058", "0.719/.076", "1.525/.086", "2.414/.092",
     "3.356/.096", "4.333/.099", "5.339/.103", "6.380/.106", "7.454/.109",
     "8.560/.113", "9.700/.116", "10.872/.119", "12.067/.121",
     "130.276/.122", "14.489/.121", "15.697/.120", "16.890/.118",
     "18.056/.114"),
    ("20°", "0.113/.060", "0.795/.077", "1.611/.087", "2.506/.093",
     "3.452/.097", "4.432/.100", "5.442/.103", "6.486/.107", "7.563/.11",
     "8.673/.113", "9.816/.116", "10.991/.119", "12.188/.120",
     "13.398/.121", "14.610/.121", "15.817/.120", "17.008/.118",
     "18.170/.112"),
    ("30°", "0.173/.062", "0.872/.078", "1.698/.087", "2.599/.093",
     "3.549/.097", "4.532/.100", "5.545/.103", "6.592/.106", "7.672/.109",
     "8.786/.113", "9.932/.116", "11.110/.119", "12.308/.120",
     "13.519/.121", "14.731/.121", "15.937/.120", "17.126/.118",
     "18.282/.112"),
    ("40°", "0.235/.064", "0.950/.079", "1.785/.088", "2.692/.094",
     "3.646/.097", "4.632/.100", "5.648/.103", "6.699/.17", "7.782/.110",
     "8.899/.113", "10.048/.117", "11.229/.119", "12.429/.121",
     "13.640/.121", "14.852/.121", "16.057/.119", "17.243/.117",
     "18.394/.110"),
    ("50°", "0.299/.065", "1.029/.080", "1.873/.089", "2.786/.094",
     "3.743/.097", "4.732/.100", "5.751/.104", "6.806/.107", "7.892/.111",
     "9.012/.114", "10.165/.117", "11.348/.119", "12.550/.121",
     "13.761/.122", "14.973/.121", "16.176/.120", "17.360/.117",
     "18.504/.108"),
    ("60°", "0.364/.068", "1.109/.081", "1.962/.089", "2.880/.094",
     "3.840/.098", "4.832/.101", "5.855/.105", "6.913/.107", "8.003/.111",
     "9.126/.114", "10.282/.118", "11.467/.120", "12.671/.121",
     "13.883/.121", "15.094/.121", "16.296/.119", "17.477/.117",
     "18.612"),
    ("70°", "0.432/.070", "1.190/.083", "2.974/.090", "3.938/.95",
     "4.933/.098", "5.960/.101", "7.020/.104", "8.114/.108", "9.240/.111",
     "10.400/.115", "11.587/.117", "12.792/.120", "14.004/.121",
     "15.215/.121", "16.415/.121", "17.594/.119", "", ""),
    ("80°", "0.502/.071", "1.273/.083", "2.141/.091", "3.069/.095",
     "4.036/.099", "5.034/.102", "60.64/.105", "7.128/.108", "8.225/.111",
     "9.355/.115", "10.517/.118", "11.707/.120", "12.913/.121",
     "14.125/.122", "15.336/.120", "16.534/.119", "17.710/.116", ""),
    ("90°", "0.573/.072", "1.356/.084", "2.232/.091", "3.164/.096",
     "4.135/0.99", "5.136/.101", "6.169/.105", "7.236/.109", "8.336/.112",
     "9.470/.115", "10.635/.119", "11.827/.120", "13.034/.121",
     "14.247/.121", "15.456/.120", "16.653/.118", "17.826/.116", ""),
]

_R = [
    ("0°", "0/.054", "0.647/.076", "1.468/.089", "2.400/.098", "3.407/.104",
     "4.471/.109", "5.582/.114", "6.741/.106", "7.949/.119", "9.203/.123",
     "10.503/.128", "11.846/.133", "13.224/.137", "14.624/.139",
     "16.035/.141", "17.445/.140", "18.842/.139", "20.215/.135"),
    ("10°", "0.054/.057", "0.723/.077", "1.557/.090", "2.498/.098",
     "3.511/.105", "4.580/.109", "5.696/.114", "6.860/.119", "8.072/.124",
     "9.331/.129", "10.636/.132", "11.983/.136", "13.363/.139",
     "14.765/.141", "16.176/.141", "17.585/.141", "18.981/.138",
     "20.350/.133"),
    ("20°", "0.111/.060", "0.800/.079", "1.647/.091", "2.596/.099",
     "3.616/.105", "4.689/.110", "5.810/.115", "6.979/.119", "8.196/.124",
     "9.460/.129", "10.768/.134", "12.119/.137", "13.502/.140",
     "14.906/.141", "16.317/.141", "17.726/.140", "19.119/.139",
     "20.483/.133"),
    ("30°", "0.171/.061", "0.879/.080", "1.738/.092", "2.695/.100",
     "3.721/.105", "4.799/.111", "5.925/.115", "7.098/.120", "8.320/.125",
     "9.589/.129", "10.902/.133", "12.256/.138", "13.642/.140",
     "15.047/.141", "16.458/.141", "17.866/.140", "19.258/.137",
     "20.616/.132"),
    ("40°", "0.232/.064", "0.959/.082", "1.830/.093", "2.795/.101",
     "3.826/.106", "4.910/.111", "6.040/.115", "7.218/.121", "8.445/.125",
     "9.718/.130", "11.035/.135", "12.394/.138", "13.782/.140",
     "15.188/.141", "16.599/.142", "18.006/.140", "19.395/.138",
     "20.748/.130"),
    ("50°", "0.296/.067", "1.041/.083", "1.923/.094", "2.896/.101",
     "3.932/.107", "5.021/.111", "6.155/.117", "7.339/.121", "8.570/.126",
     "9.848/.130", "11.170/.134", "12.532/.138", "13.922/.140",
     "15.329/.141", "16.741/.141", "18.146/.140", "19.533/.137",
     "20.878/.128"),
    ("60°", "0.363/.068", "1.124/.084", "2.017/.094", "2.997/.102",
     "4.039/.107", "5.132/.112", "6.272/.116", "7.460/.122", "8.696/.126",
     "9.978/.131", "11.304/.135", "12.670/.138", "14.062/.140",
     "15.470/.141", "16.882/.140", "18.286/.139", "19.670/.137",
     "21.006"),
    ("70°", "0.431/.070", "1.208/.086", "2.111/.096", "3.099/.102",
     "4.146/.108", "5.244/.112", "6.388/.117", "7.582/.122", "8.822/.127",
     "10.109/.131", "11.439/.135", "12.808/.138", "14.202/.141",
     "15.611/.141", "17.022/.141", "18.425/.139", "19.807/.137", ""),
    ("80°", "0.501/.072", "1.294/.086", "2.207/.096", "3.201/.103",
     "4.254/.108", "5.356/.113", "6.505/.118", "7.704/.122", "8.949/.127",
     "10.240/.131", "11.574/.136", "12.946/.139", "14.343/.140",
     "15.752/.142", "17.163/.141", "18.564/.140", "19.944/.136", ""),
    ("90°", "0.573/.074", "1.380/.088", "2.303/.097", "3.304/.103",
     "4.362/0.109", "5.469/.113", "6.623/.118", "7.826/.123", "9.076/.127",
     "10.371/.132", "11.710/.136", "13.085/.139", "14.483/.141",
     "15.894/.141", "17.304/.141", "18.704/.138", "20.080/.135", ""),
]

_B = [
    ("0°", "0/−0.002", "0.33/.010", "0.178/.021", "0.431/.031", "0.786/.041",
     "1.241/.051", "1.791/.060", "2.430/.069", "3.154/.077", "3.957/.084",
     "4.833/.091", "5.777/.098", "6.783/.104", "7.845/.108", "8.952/.113",
     "10.094/.116", "11.257/.117", "12.426/.117", "13.58/.11"),
    ("10°", "−0.002/−0.001", "0.043/.010", "0.199/.021", "0.462/.032",
     "0.827/.043", "1.292/.052", "1.851/.061", "2.499/.070", "3.231/.077",
     "4.041/.085", "4.924/.092", "5.875/.098", "6.887/.104", "7.953/.110",
     "9.065/.113", "10.210/.115", "11.374/.117", "12.543/.116",
     "13.69/.11"),
    ("20°", "−0.003/+0.001", "0.053/.012", "0.220/.023", "0.494/.033",
     "0.807/.043", "1.344/.053", "1.912/.062", "2.569/.070", "3.308/.079",
     "4.126/.086", "5.016/.093", "5.973/.100", "6.991/.105", "8.063/.109",
     "9.178/.113", "10.325/.116", "11.491/.117", "12.659/.117", "13.81"),
    ("30°", "−0.002/+0.002", "0.065/.013", "0.243/.023", "0.527/.034",
     "0.913/.044", "1.397/.053", "1.974/.062", "2.639/.071", "3.387/.079",
     "4.212/.086", "5.109/.093", "6.073/.099", "7.096/.106", "8.172/.111",
     "9.291/.114", "10.441/.117", "11.608/.117", "12.776/.117", ""),
    ("40°", "0.000/+.002", "0.078/.014", "0.266/.025", "0.561/.035",
     "0.957/.045", "1.450/.055", "2.036/.064", "2.710/.072", "3.466/.080",
     "4.298/.088", "5.202/.095", "6.172/.101", "7.202/.106", "8.283/.110",
     "9.405/.114", "10.558/.116", "11.725/.117", "12.892/.116", ""),
    ("50°", "+0.002/.004", "0.092/.015", "0.291/.026", "0.596/.036",
     "1.002/.046", "1.505/.055", "2.100/.064", "2.782/.073", "3.546/.080",
     "4.386/.088", "5.297/.094", "6.273/.101", "7.308/.106", "8.393/.111",
     "9.519/.115", "10.674/.116", "11.842/.117", "13.008/.116", ""),
    ("60°", "0.006/.005", "0.107/.016", "0.317/.027", "0.632/.037",
     "1.048/.047", "1.560/.057", "2.164/.066", "2.855/.073", "3.626/.082",
     "4.474/.088", "5.391/.096", "6.374/.101", "7.414/.107", "8.504/.112",
     "9.634/.114", "10.790/.117", "11.959/.117", "13.124/.115", ""),
    ("70°", "0.011/.006", "0.123/.017", "0.344/.028", "0.669/.038",
     "1.095/.048", "1.617/.057", "2.230/.066", "2.928/.075", "3.708/.082",
     "4.562/.090", "5.487/.096", "6.475/.102", "7.521/.107", "8.616/.113",
     "9.748/.115", "10.907/.117", "12.076/.117", "13.239/.115", ""),
    ("80°", "0.017/.008", "0.140/.019", "0.372/.029", "0.707/.039",
     "1.143/.049", "1.674/.058", "2.296/.067", "3.003/.075", "3.790/.083",
     "4.652/.090", "5.583/.097", "6.577/.103", "7.628/.108", "8.727/.112",
     "9.863/.116", "11.024/.117", "12.193/.117", "13.354/.116", ""),
    ("90°", "0.025/.008", "0.159/.019", "0.401/.030", "0.746/.040",
     "1.192/.049", "1.732/.059", "2.363/.067", "3.078/.076", "3.873/.084",
     "4.742/.091", "5.680/.097", "6.680/.103", "7.736/.109", "8.839/.113",
     "9.979/.115", "11.141/.116", "12.310/.116", "13.470/.115", ""),
]


def _cal(data, lo, hi):
    """Build one table's rows for temperature columns lo..hi (inclusive)."""
    rows = []
    for rec in data:
        cells = [c.split("/", 1) for c in rec[1:]][lo:hi + 1]
        rows.append([rec[0]] + [c[0] for c in cells])
        rows.append(["Δ"] + [(c[1] if len(c) > 1 else "") for c in cells])
    return rows


def section(lang):
    b = []

    # ------------------------------- continuation of (v) differential pressure
    P(b, lang,
      "Do đó, phép đo mức thực chất trở thành phép đo áp suất chênh do cột áp "
      "của mức chất lỏng tạo ra. Vì vậy, bộ phát chênh áp (D.P. cell) phải được "
      "nối vào hệ thống sao cho phía áp suất thấp (L.P.) hở ra khí quyển còn "
      "phía áp suất cao (H.P.) nối vào đầu vào ở đáy bình hở. Với bình kín, "
      "phía H.P. nối vào phần trên cùng, tức không gian hơi, còn phía L.P. nối "
      "vào phần dưới của bình có chứa chất lỏng ở pha thích hợp.",
      "Therefore, a differential pressure transmitter (D.P. cell) shall be "
      "connected to the system in such a way that its low pressure side (L.P.) "
      "shall be left open to atmosphere and the high pressure side (H.P.) shall "
      "be connected to bottom entry to the open tank. In case with closed tank, "
      "the H.P. side shall be connected to the upper portion i.e. vapour space "
      "in the closed tank whereas the L.P. side shall be connected to the lower "
      "portion of the tank having liquid in its proper phase.")

    P(b, lang,
      "Phép đo chỉ chính xác khi không có sự thay đổi tỷ trọng của chất lỏng. "
      "Nếu tỷ trọng thay đổi, có thể hiệu chỉnh bằng cách nhân độ thay đổi tỷ "
      "trọng đã đo/tính toán với chiều cao cột áp.",
      "The measurement is accurate provided there is no density variation in "
      "the liquid. In case density changes, correction can be applied by "
      "multiplying the measured/calculated density change by the head.")

    P(b, lang,
      "Bộ phát chênh áp có đặc điểm thiết kế giống như bộ phát áp suất đã thảo "
      "luận ở chương này. Tuy nhiên, dạng đơn giản nhất của nó được trình bày "
      "trong Hình 3.62. Dụng cụ được hiệu chuẩn theo dải đo của mức chất lỏng.",
      "The differential pressure transmitter has the same design feature as "
      "the pressure transmitter, we have already discussed earlier in this "
      "chapter. Even then, it has been shown in its simplest form in Figure "
      "3.62. The instrument is calibrated with respect to the span of the level "
      "measurement.")

    FIG(b, 62, F.fig_f62(), lang)

    P(b, lang,
      "Cách bố trí lắp đặt cho cả sơ đồ đo mức bình hở và bình kín được trình "
      "bày trong Hình 3.63. Manifold ba van được dùng để đưa bộ phát chênh áp "
      "vào hoạt động một cách có hệ thống.",
      "The installation arrangement for open tank as well as closed tank level "
      "measurement schemes have been shown in Figure 3.63. The 3-valve "
      "manifold is used for putting the D.P. transmitter into operation "
      "systematically.")

    FIG(b, 63, F.fig_f63(), lang)

    P(b, lang,
      "Trước hết, van cân bằng được mở, sau đó mới mở lần lượt phía H.P. và "
      "phía L.P. Van cân bằng giữ cho màng của bộ phát chịu áp suất bằng nhau "
      "ở cả hai mặt, tránh hư hỏng màng do áp suất đặt vào đột ngột gây mất "
      "cân bằng. Sau khi mở hoàn toàn van H.P. và L.P., van cân bằng được đóng "
      "từ từ và như vậy bộ phát bắt đầu hoạt động. Hai van xả được lắp để xả "
      "sạch các đường dẫn xung tại điểm lấy tín hiệu đo mức, nhằm loại bỏ "
      "tình trạng tắc nghẽn.",
      "First the equalizer valve is kept open and then H.P. and L.P. sides are "
      "open one-by-one. Equalizer valve keeps the diaphragm of the transmitter "
      "at equal pressure from both sides and avoids damage of diaphragm due to "
      "unbalance of suddenly applied pressure. After opening H.P. and L.P. "
      "valves fully, equalizer valve is closed slowly and in this way the "
      "transmitter comes into operation. Two drain valves have been installed "
      "for flushing the impulse lines of the level instrument tapping for "
      "removal of any choking.")

    P(b, lang,
      "Trong một số ứng dụng, chất lỏng có thể có tính độc hại và không được "
      "phép tiếp xúc trực tiếp với bộ phận bên trong của bộ phát. Khi đó nên "
      "dùng chất lỏng làm kín, nhưng chất lỏng chọn phải có trọng lực riêng "
      "lớn hơn chất lỏng cần đo và cũng phải không trộn lẫn. Ví dụ, với dầu "
      "nhiên liệu có độ nhớt cao có thể dùng glycerin làm chất lỏng làm kín. "
      "Giải pháp tốt hơn là tự cải tiến bộ phát chênh áp cho phù hợp với ứng "
      "dụng. Phần tiếp xúc trực tiếp với chất lỏng có màng kim loại để cách "
      "ly. Với cải tiến thiết kế này, có thể dùng hai loại màng: màng mở rộng "
      "và màng phẳng như trong Hình 3.64. Cấu tạo bên trong được trình bày "
      "trong Hình 3.65.",
      "In some applications it is required that the liquid which may be of "
      "toxic nature may not be allowed to come into the direct contact of the "
      "transmitter internals. In that case a sealing liquid is advised to be "
      "used, but the liquid to be selected must have specific gravity greater "
      "than that of the liquid under measurement. It should be immiscible as "
      "well. For instance, in case of fuel oil of high viscosity, glycerene may "
      "be used as sealing liquid. A better solution is that the D.P. "
      "transmitter is itself modified and made suitable for the application. "
      "The portion which comes into direct contact with the liquid is having "
      "metallic diaphragm for isolation. For such a design refinement, two "
      "types of diaphragm can be applied. One is called extended diaphragm and "
      "the other one is called flat diaphragm as shown in Figure 3.64. The "
      "internal arrangements have been shown in Figure 3.65.")

    FIG(b, 64, F.fig_f64(), lang)

    FIG(b, 65, F.fig_f65(), lang)

    P(b, lang,
      "Màng mở rộng được lắp vào buben (nozzle) làm ở đáy bình. Kiểu thiết kế "
      "này loại bỏ các khoảng rỗng chết và phù hợp với chất lỏng dễ thay đổi "
      "pha khi nhiệt độ thay đổi. Kiểu thiết kế phẳng, tức màng phẳng, được "
      "lắp trực tiếp vào van cô lập của bình. Với cách lắp này, kết nối áp "
      "suất thấp (L.P.) được dùng hay không tùy theo việc lắp đặt là cho bình "
      "hở hay bình kín.",
      "The extended diaphragm is installed on to the nozzle made on the tank "
      "bottom. This type of design removes dead cavities. This design is "
      "suitable for liquid which changes its phase due to change in temperature "
      "very easily. The flush design that is flat diaphragm design is installed "
      "directly to the tank isolation valve. In this installation, the low "
      "pressure (L.P.) connection is used as the case may be depending upon "
      "whether the installation is for open tank or closed tank.")

    # ------------------------------------------------------------- (vi) capacitance
    H(b, lang, "(vi) Kiểu điện dung", "(vi) Capacitance type", level=3)

    P(b, lang,
      "Hệ thống đo mức kiểu điện dung được dùng trong hầu hết mọi ngành công "
      "nghệ quy trình hoặc kho chứa. Một số ứng dụng có thể kể đến đo mức trong "
      "silô than, đo mức dung dịch urê (phân bón) cũng như urê dạng hạt (trạng "
      "thái rắn) trong silô, đo mức ngũ cốc trong kho chứa. Điều quan trọng "
      "nhất là hiệu năng của hệ thống hoàn toàn không bị ảnh hưởng bởi tính "
      "chất của vật liệu cần đo cũng như các biến số công nghệ.",
      "Capacitance type level measurement systems are in use in almost every "
      "process industry or in any storage depot. Some of the applications are "
      "enumerated like level measurement of a coal bunker, level measurement of "
      "urea solution (fertilizer) as well as prilled urea (solid state) placed "
      "in silo, level measurement of food grains in grain storage depots. The "
      "most important fact is that the performance of the system is not at all "
      "affected by either the properties of the material under measurement or "
      "the process variables.")

    P(b, lang,
      "Nguyên lý làm việc cơ bản dựa trên sự thay đổi giá trị điện dung khi "
      "vật liệu được nạp dần vào bình. Để đo điện dung thực tế, một đầu dò "
      "được lắp trên bình khi bình còn rỗng như trong Hình 3.66. Khi đó tồn tại "
      "giá trị điện dung ban đầu giữa đầu dò và thành bình (gọi là C0), gồm "
      "điện dung của đầu dò (gọi là Cp) và điện dung giữa đầu dò và bình rỗng "
      "(gọi là Ct).",
      "The basic working of the system depends upon the variation in capacitance "
      "value when the material is filled up slowly into the tank. For actual "
      "measurement of capacitance, a probe is installed on the tank when the "
      "tank is empty as shown in Figure 3.66. In this condition there will be "
      "an initial capacitance value between the capacitance probe and the tank "
      "wall (say C0) which shall be consisting of capacitance of the probe (say "
      "Cp) and capacitance between probe and empty tank (say Ct).")

    FIG(b, 66, F.fig_f66(), lang)

    P(b, lang,
      "Giá trị Cp phụ thuộc vào vật liệu của đầu dò (có thể là teflon hoặc vật "
      "liệu khác) và không đổi đối với một thiết kế đầu dò nhất định. Mặt "
      "khác, giá trị Ct được xác định theo phương trình sau:",
      "The value of Cp depends upon the material of the probe (may be teflon "
      "or others) and remains constant for a particular design of probe. On the "
      "other hand, the value of Ct is governed by following equation:")

    E(b, lang, "Ct = lρ / d₀", "Ct = lρ / d₀", num="3.45")

    P(b, lang,
      "trong đó l là chiều dài hiệu dụng của đầu dò, ρ là hằng số điện môi của "
      "vật liệu giữa đầu dò và thành bình, còn d0 là khoảng cách đo được giữa "
      "đầu dò và thành bình.",
      "where l is the effective length of the probe, ρ is the dielectric "
      "constant of the material between the probe and the tank wall, and d0 is "
      "the distance measured between the probe and the tank wall.")

    P(b, lang,
      "Vì chiều dài đầu dò và khoảng cách giữa đầu dò với thành bình gần như "
      "không đổi đối với một ứng dụng cụ thể, giá trị điện dung Ct tỷ lệ thuận "
      "trực tiếp với hằng số điện môi, tức Ct αρ.",
      "As we observe here that the length of the probe and the distance between "
      "the probe and the tank wall are almost constant for a particular "
      "application, the capacitance value Ct is directly proportional to the "
      "dielectric constant, i.e. Ct αρ.")

    P(b, lang,
      "Để giữ d0 không đổi, đầu dò điện dung được lắp cứng trên đỉnh bình. Khi "
      "vật liệu được nạp vào bình, nó chạm vào phần dưới của đầu dò rồi bắt đầu "
      "bao phủ đầu dò. Do vật liệu lấp đầy khoảng không khí trong bình, giá trị "
      "Ct bắt đầu tăng. Khi độ tăng của Ct lớn hơn giá trị Cp (thực tế chỉ "
      "chiếm 1% của Ct), mạch điện tử bắt đầu hoạt động. Mạch điện tử có thể "
      "loại chỉ thị hoặc loại công tắc bật tắt tùy theo yêu cầu của ứng dụng.",
      "For keeping the d0 constant, the capacitance probe is installed rigidly "
      "on top of the tank. As the material is filled up in the tank, slowly it "
      "touches the lower part of the probe and thereafter it starts covering "
      "the probe. Due to covering of the material in the air gap of the tank "
      "the value of Ct starts increasing. When the increase in Ct becomes more "
      "than the value of Cp (which is practically 1% of Ct), the electronic "
      "circuit starts its operation. The electronic circuit may be of "
      "indicating type or an on-off switch type depending upon the requirement "
      "of the application.")

    P(b, lang,
      "Đầu dò là phần tử chủ động trong toàn bộ hệ thống. Khi mức vật liệu "
      "trong bình tăng, tín hiệu chỉ thị mức được mạch điện tử nhận biết thông "
      "qua sự thay đổi của Ct. Thanh đầu dò và bạc (bush) làm bằng thép không "
      "gỉ và được cách ly hoàn toàn bằng teflon (PTFE). Sợi dây mềm giữ đầu dò "
      "làm bằng thép mạ kẽm có lớp phủ polyethelene. Rõ ràng vật liệu đầu dò, "
      "vật liệu cách ly cũng như chiều dài đầu dò phải được chọn riêng cho từng "
      "ứng dụng.",
      "The probe is an active element in the entire system. As the level of the "
      "material inside the tank increases, the indication of the level is "
      "detected by the electronic circuit by the help of change in Ct. The "
      "probe rod and the bush are made of stainless steel and are fully "
      "insulated with teflon (PTFE). The flexible rope which fastens the probe "
      "is made of galvanized steel with a coating of polyethelene. It is "
      "obvious that the probe material, insulation material and also the "
      "probe-length shall be selected for individual application as the case "
      "may be.")

    P(b, lang,
      "Mạch điện tử gồm chủ yếu hai phần: (a) đầu dò có mạch dao động nối với "
      "đầu dò điện dung, và (b) khối điều khiển có máy biến áp nguồn, bộ chỉnh "
      "lưu, bộ khuếch đại cảm biến và rơ le (đối với đồng hồ mức bật tắt) hoặc "
      "bộ chuyển đổi (đối với đồng hồ mức loại chỉ thị). Toàn bộ hệ thống được "
      "thể hiện trong Hình 3.67.",
      "The electronic circuit consists of mainly of parts: (a) probe head "
      "having oscillator connected to capacitance probe, and (b) control unit "
      "having mains transformer, rectifier, sensing amplifier and relay (for "
      "on-off level meter) or transducer (for indicating type level meter) the "
      "entire system has been indicated in Figure 3.67.")

    FIG(b, 67, F.fig_f67(), lang)

    P(b, lang,
      "Mạch dao động được đặt trong vỏ bằng hợp kim nhôm và được vặn vào phần "
      "trên của đầu dò. Vì lắp ở môi trường khắc nghiệt trong nhà máy, mạch phải "
      "được bảo vệ khỏi bụi, nhiệt, độ ẩm và các tác nhân gây nhiễu khác. Do đó "
      "mạch được chế tạo trên tấm epoxy thủy tinh rồi được bọc kín trong bình "
      "nhựa đổ đầy nhựa thông. Thiết kế này chịu được nhiệt độ 100 °C. Nếu "
      "nhiệt độ vượt quá 100 °C, phần dao động phải được lắp xa đầu dò, nơi "
      "nhiệt độ môi trường nằm trong giới hạn cho phép. Đầu ra tần số của cụm "
      "là tín hiệu 100 kHz, thu được do sự thay đổi điện dung khi mức thay đổi. "
      "Bộ khuếch đại cảm biến khuếch đại tín hiệu này và gửi tới điều khiển rơ "
      "le hoặc bộ chuyển đổi. Khối nguồn cấp 10 V một chiều cho từng cụm để "
      "hoạt động.",
      "Oscillator is boxed in a housing made of aluminium casting and is "
      "screwed on the top portion of the probe. Since this is installed in "
      "adverse environment in the plant, it has to be protected from dust, "
      "heat, moisture and other disturbing agents. Therefore, the circuit is "
      "fabricated on glass epoxy board and then encapsulated in a plastic pot "
      "filled with resin. This type of design shall waithstand temperature of "
      "100C. If the temperature is more than 100C, the oscillator portion has "
      "to be installed away from the probe head where the temperature of the "
      "environment is within the limit. The frequency output of the unit is "
      "100 kHz signal which is obtained as a result of change in capacitance "
      "due to change in level. The sensing amplifier amplifies this output and "
      "sends to operate the relay unit or transducer unit. The power supply "
      "unit supplies 10V D.C. power to all the individual unit for its "
      "operation.")

    # ------------------------------------------------------- (vii) magnetic gage
    H(b, lang, "(vii) Thước mức từ tính", "(vii) Magnetic level gage", level=3)

    P(b, lang,
      "Thước mức từ tính thực chất thuộc dòng dụng cụ đo mức chỉ thị trực quan "
      "trực tiếp. Trong các ứng dụng công nghệ xử lý chất lỏng độc hại, ăn mòn "
      "hoặc khó xử lý, không thể dùng ống kính đo mức thông thường. Khi đó "
      "thước mức từ tính trở thành lựa chọn tất yếu.",
      "Magnetic level gage is in fact from the series of direct visual "
      "indicating type of level instrument. In process applications where "
      "toxic, corrosive or otherwise difficult liquid is handled, normal type "
      "of level gage glass is not acceptable. Magnetic level gage becomes "
      "obvious choice in such application.")

    P(b, lang,
      "Thiết kế cơ bản gồm một phao không từ tính dạng hình trụ có tỷ trọng "
      "lớn hơn chất lỏng, như trong Hình 3.68. Một nam châm nhỏ có cùng hình "
      "dạng được gắn bên trong phao để toàn bộ cụm nổi trên chất lỏng và chuyển "
      "động lên xuống theo sự thay đổi của mức.",
      "The basic design consists of a non-magnetic denser float (cylindrical "
      "shape) as shown in Figure 3.68. A small magnet of the same shape is "
      "embedded inside the float so that the entire combination floats on the "
      "liquid and moves up and down according to the change in level as shown.")

    FIG(b, 68, F.fig_f68(), lang)

    P(b, lang,
      "Để có chỉ thị trực quan bên ngoài buồng phao, người ta dùng hai thiết "
      "kế thực tế như Hình 3.69 và Hình 3.70. Trong thiết kế thứ nhất, nam châm "
      "bên trong gắn với phao chuyển động theo mức chất lỏng, còn nam châm bên "
      "ngoài chỉ thị mức khi chuyển động cùng với phao. Thiết kế kia có bộ "
      "chỉ thị dạng thẻ (wafer) gắn bên ngoài buồng phao.",
      "For obtaining visual indication outside the float chamber two types of "
      "designs are in practical use as shown in Figure 3.69 and 3.70. In the "
      "first design, the inner magnet imbedded with the float moves with the "
      "level of the liquid while the outer magnet of the float indicates the "
      "level when it moves along with the float. The other design possesses a "
      "wafer indicator which is attached outside the float chamber as shown.")

    FIG(b, 69, F.fig_f69(), lang)

    P(b, lang,
      "Bộ chỉ thị dạng thẻ chứa các thẻ nhỏ có hai màu, một mặt màu đen và mặt "
      "kia màu vàng. Các thẻ được bố trí sao cho khi phao từ tính di chuyển, "
      "thẻ sẽ lật 180° và đổi màu từ vàng sang đen. Mặt đen chỉ mức chất lỏng, "
      "còn mặt vàng chỉ không gian hơi. Áp suất và nhiệt độ định mức của các "
      "hệ thống đo mức này lần lượt tới 250 kg/cm² và 400 °C. Chúng cũng có "
      "thể dùng ở nhiệt độ đông lạnh nếu cần.",
      "The wafer indicator contains twin colour small wafers, one side of which "
      "is black and the other side is yellow. These wafers are so located that "
      "when the magnetic float moves, the wafers flips over 180 and in this way "
      "it changes the colour from yellow to black. For indication purpose, the "
      "black wafer indicates liquid level and yellow wafer indicates vapour "
      "space. Pressure and temperature ratings of these level measurement "
      "systems are upto 250 kg/cm2 and 400C respectively. These can be used "
      "cryogenic temperature also if required.")

    FIG(b, 70, F.fig_f70(), lang)

    # ------------------------------------------------------ (viii) nucleonic type
    H(b, lang, "(viii) Kiểu hạt nhân", "(viii) Nucleonic type", level=3)

    P(b, lang,
      "Kỹ thuật đo mức kiểu hạt nhân dựa trên hiện tượng bức xạ của nguyên tố "
      "phóng xạ. Nguyên tố phóng xạ phân rã dần và phát ra các tia α, β và γ. "
      "Trong ba loại bức xạ này, tia γ gồm các sóng điện từ và là loại được "
      "quan tâm chủ yếu cho đo mức. Khả năng xuyên của tia γ lớn hơn tia α "
      "10.000 lần và lớn hơn tia β 100 lần; mặt khác tia γ không bị lệch bởi "
      "điện trường hay từ trường như tia α và β, nên γ là tia phù hợp nhất cho "
      "hệ thống đo mức.",
      "Nucleonic type of level measurement technique depends upon the radiation "
      "phenomena of radioactive element. The radioactive element disintegrates "
      "in due course and emits α, β and γ (Alpha, Beta and Gamma) rays. Out of "
      "these three radiations, γ consists of electromagnetic waves and is of "
      "prime concern for use in level measurement technique. The penetration "
      "power of γ is 10,000 times more than that of α and 100 times more than β "
      "and since γ rays cannot be deflected by electric or magnetic field as is "
      "the case with α and β rays, γ is the most suitable ray for level "
      "measurement system.")

    P(b, lang,
      "Hai nguồn tia γ quan trọng nhất là coban (Co 60) và xêzi (Cs 137). Chu "
      "kỳ bán rã của Co 60 là 5,3 năm (tốc độ phân rã 12,3% mỗi năm), còn chu "
      "kỳ bán rã của Cs 137 là 30 năm nhưng tốc độ phân rã chỉ 2,3% mỗi năm; "
      "do đó Co 60 được chọn làm nguồn cho đo mức. Lý do là với công việc đo "
      "mức, tốc độ phân rã cao có nghĩa là tốc độ phát xạ cao, cần thiết cho "
      "mức độ xuyên lớn.",
      "The two most important γ ray sources are cobalt (Co 60) and cesium "
      "(Cs 137). The half life of Co 60 is 5.3 years (rate of decay is 12.3% "
      "per year) and the half life of Cs 137 is 30 years but rate of decay is "
      "only 2.3% per year and therefore Co 60 is selected for level measurement "
      "source unit. This is because for level measurement works, high rate of "
      "decay indicates high emission rate which is required for high degree of "
      "penetration.")

    P(b, lang,
      "Phương pháp hạt nhân vượt trội hơn các phương pháp khác trong những "
      "điều kiện dịch vụ mà chất lỏng không thể tiếp cận hoặc thiết bị quá "
      "phức tạp không cho phép lắp dụng cụ khác, hoặc khi độ chính xác không "
      "quan trọng lắm. Những tình huống như vậy tồn tại trong hầu hết các ngành "
      "hóa chất, ví dụ bình nóng, silô cấp than, thiết bị bay hơi đặt ở vị trí "
      "cao, xe bồn (tĩnh hoặc di chuyển trong nhà máy). Phương pháp này hoàn "
      "toàn không bị ảnh hưởng bởi môi trường ăn mòn, phản ứng hóa học với "
      "chất khác, cấu trúc hạt thay đổi hay khoảng rỗng có sẵn trong chất lỏng "
      "nhiều pha.",
      "Nucleonic method of level measurement technique proves superior with "
      "respect to other methods where the service conditions are such that the "
      "liquid is not approachable or the equipment is of complicated nature not "
      "allowing other instruments to be installed or accurate measurement is "
      "not that important. Such situations prevail in almost all chemical "
      "industries. Some of the examples are hot tanks, feed coal or other "
      "bunkers, evaporators located at higher elevation, tankers (static or "
      "moving inside the plant). This method of measurement is not at all "
      "affected by corrosive atmosphere, reactivity to other chemicals, "
      "variable grain structures or voids present naturally in mixed phase "
      "liquids.")

    P(b, lang,
      "Bức xạ hạt nhân từ bình nguồn khi đi xuyên qua vật liệu (chất rắn hoặc "
      "chất lỏng cần đo mức) sẽ bị suy giảm. Sự thay đổi cường độ bức xạ do suy "
      "giảm được cụm đầu dò ở phía đối diện của bình phát hiện. Khối điều "
      "khiển cấp nguồn và nhận tín hiệu đầu ra tỷ lệ với mức để chỉ thị.",
      "The neuclic radiation from source flask when allowed to traverse through "
      "the material (solid or liquid of which level is to be measured) gets "
      "attenuated. The change in radiation strength due to attenuation is "
      "detected by detector unit located on the opposite side of the level "
      "measurement tank. The control unit supplies power and receives the "
      "signal output proportional to level for indication.")

    P(b, lang,
      "Bình nguồn chứa nguồn Co 60 được thiết kế theo khuyến cáo của Trung tâm "
      "Nghiên cứu Nguyên tử Bhabha hoặc cơ quan quản lý quốc tế khác được "
      "chính phủ công nhận. Tất cả bộ phận bên trong, kể cả collimator, đều làm "
      "bằng thép không gỉ. Vỏ ngoài làm bằng thép mềm và được đổ đầy chì (thực "
      "tế chì gần như không bị ảnh hưởng bởi bức xạ) để che chắn. Nguồn bức xạ "
      "được đặt trong một nang chế tạo riêng; khi hoạt động, một chùm tia sắc "
      "như bút chì thoát ra, đi qua vật liệu trong bình và được đầu dò thu "
      "nhận.",
      "The source flask in which Co 60 source is kept for radiation is designed "
      "as recommended by Bhabha Atomic Research Centre or other international "
      "regulatory authority recognized by the government. All inner parts "
      "including collimator are made of stainless steel. The outer casing is "
      "made of mild steel and is completely filled with lead (practically no "
      "effect of radiation on lead) for shielding the effect of radiations. The "
      "radiation source is put in an especially fabricated capsule and when in "
      "operation, a sharp pencil-type ray comes out and after attenuation "
      "through the tank content is detected at detector unit.")

    P(b, lang,
      "Cụm đầu dò gồm ống Geiger-Mueller dập tắt bằng halogen, hoạt động ở "
      "500 V một chiều. Bộ khuếch đại tín hiệu thu được đặt ngay trong đầu dò. "
      "Cụm đầu dò được bọc trong áo kim loại để nước làm mát lưu thông như "
      "trong Hình 3.71. Đầu ra của cụm đầu dò nối tới khối điều khiển có sắp "
      "xếp chỉ thị rời rạc hoặc liên tục. Khối điều khiển đặt ở vị trí thuận "
      "tiện, cách xa nguồn và đầu dò.",
      "The detector unit consists of halogen quenched Geiger-Mueller tube which "
      "operates at 500 volt D.C. The amplifier unit for amplifying the signal "
      "received at the detector unit is located inside the detector itself. The "
      "detector unit is enclosed in a metal jacket for circulating the cooling "
      "water as shown in Figure 3.71. The output from the detector unit is "
      "connected to control unit having arrangement for discrete or continuous "
      "indication. The control unit is located at convenient place away from "
      "the source and detector unit.")

    FIG(b, 71, F.fig_f71(), lang)

    P(b, lang,
      "Vấn đề an toàn cho kiểu lắp đặt này rất quan trọng. Tác động bức xạ nguy "
      "hại cho con người và các sinh vật khác, vì vậy thời gian phơi nhiễm dài "
      "hạn của nhân viên phải được người sử dụng xác định từ trước, sau khi "
      "tham vấn cơ quan quản lý có thẩm quyền. Khu vực được cô lập và cấm vào "
      "bằng biển báo NGUY HIỂM như trong Hình 3.72.",
      "Safety consideration for this type of installation is important. The "
      "radiation effect is hazardous for human beings and other living beings "
      "and therefore, long term exposure for the personnel is decided before "
      "hand by the user in consultation with the appropriate regulatory "
      "authority. The area is cordoned off and entry is prohibited by providing "
      "a DANGER mark as shown in Figure 3.72.")

    FIG(b, 72, F.fig_f72(), lang)

    # ---------------------------------------------------------------- exercises
    H(b, lang, "Bài tập", "Exercise", level=2)

    L(b, lang,
      ["Mô tả ngắn gọn các phương pháp cơ học khác nhau để đo nhiệt độ. Nhiệt "
       "kế thủy ngân trong ống thép khác gì với nhiệt kế hơi? Giải thích kèm "
       "hình vẽ.",
       "Bộ phát nhiệt độ có thể được thực hiện như thế nào bằng cơ khí từ "
       "nhiệt kế thủy ngân trong ống thép? Giải thích kèm hình vẽ gọn gàng.",
       "Mô tả cấu tạo chi tiết của đầu dò nhiệt độ điện trở platin kèm hình vẽ "
       "gọn gàng.",
       "Quy trình hiệu chuẩn nhiệt kế điện trở platin là gì? Giải thích chi "
       "tiết.",
       "Vì sao hệ ba dây được dùng để nối nhiệt kế điện trở? Giải thích kèm "
       "hình vẽ.",
       "Mô tả cấu tạo của cặp nhiệt điện. Giải thích kèm hình vẽ.",
       "Cặp nhiệt điện được hiệu chuẩn như thế nào?",
       "Các loại cặp nhiệt điện đặc biệt là gì? Giải thích chi tiết một loại "
       "bất kỳ.",
       "Phép đo áp suất có thể liên hệ với phép đo mức như thế nào? Giải thích "
       "bằng phương trình toán học.",
       "Giải thích phương pháp đo mức bằng ống xoắn mô-men với hình vẽ gọn "
       "gàng.",
       "Suy ra phương trình lưu lượng kế chênh áp cho một đường ống thẳng.",
       "Suy ra phương trình dòng chảy qua lưu lượng kế diện tích thay đổi.",
       "Có bao nhiêu loại phần tử đo lưu lượng? Nêu chi tiết cấu tạo và các "
       "thông tin liên quan của bất kỳ hai loại nào.",
       "Mô tả cấu tạo và nguyên lý làm việc của lưu lượng kế tuabin.",
       "Lưu lượng kế kiểu rụng xoáy hoạt động như thế nào? Mô tả đầy đủ kèm "
       "hình vẽ gọn gàng.",
       "Nêu nguyên lý cơ bản của lưu lượng kế khối lượng. Đồng hồ bánh răng "
       "oval hoạt động ra sao?",
       "Giải thích hoạt động của dụng cụ đo mức kiểu dẫn điện. Dụng cụ đó được "
       "hiệu chuẩn như thế nào?",
       "Lưu lượng kế kiểu mục tiêu hoạt động thế nào? Nó có thể dùng thành "
       "công trong những dịch vụ nào?",
       "Sự bù nhiệt độ môi trường được thực hiện như thế nào trong máy ghi "
       "nhiệt độ tiềm kế dựa trên cặp nhiệt điện?"],
      ["Describe different mechanical methods for temperature measurement in "
       "brief. How a mercury-in-steel thermometer is different from a vapour "
       "thermometer? Explain with sketches.",
       "How a temperature transmitter can be implemented by using "
       "mercury-in-steel thermometer mechanically? Explain with neat sketch.",
       "Describe the constructional details of a platinum resistance temperature "
       "detector with a neat sketch.",
       "What is the calibration procedure of a platinum resistance thermometer? "
       "Explain in detail.",
       "Why 3-wire system is used for connecting resistance thermometer? "
       "Explain with sketch.",
       "Describe constructional detail of a thermocouple. Explain with sketch.",
       "How a thermocouple can be calibrated?",
       "What are the special type of thermocouples? Explain any one of them in "
       "detail.",
       "How pressure measurement can be related to level measurement? Explain "
       "with mathematical equation.",
       "Explain the torque tube method of level measurement with the help of "
       "neat sketch.",
       "Derive flow meter equation of differential pressure type for a straight "
       "pipeline.",
       "Derive the equation of flow through variable area meter.",
       "How many types of flow elements are there? Give constructional and "
       "other related details of any two of them.",
       "Describe constructional details and working principle of turbine "
       "flowmeter.",
       "How votex shedding flowmeter works? Describe in complete detail with "
       "the help of a neat sketch.",
       "Describe the basic principle of mass flowmeter. How an ovalgear meter "
       "functions?",
       "Describe the working of a conducting type of level measuring "
       "instrument. How is it calibrated?",
       "How does a target type flowmeter work? In what service it can be "
       "applied successfully?",
       "How does ambient temperature compensation is affected in a "
       "thermocouple based potentiometric temperature recorder."],
      ordered=True)

    # ------------------------------------------------- thermocouple calibration
    H(b, lang, "Bảng hiệu chuẩn cặp nhiệt điện",
      "Thermocouple calibration tables", level=2)

    P(b, lang,
      "Bảng hiệu chuẩn chuẩn cho cặp nhiệt điện platin: 10% rhodi-platin "
      "(loại S) và platin: 13% rhodi-platin (loại R), được hiệu chuẩn theo "
      "BS4937 phần 1 và 2:1973 và tài liệu NBS monograph 125 dựa trên IPTS-68. "
      "Giá trị suất điện động (e.m.f.) tính bằng milivôn, nhiệt độ tính bằng "
      "độ C, điểm nối lạnh ở 0 °C. Để hỗ trợ nội suy giữa hai giá trị đã cho, "
      "hiệu số giữa các lần đọc e.m.f. liên tiếp được thể hiện bên dưới giá "
      "trị chính.",
      "Standard calibration table for platinum: 10% rhodium-platinum (Type S) "
      "and platinum: 13% rhodium-platinum (type R) thermocouples calibrated in "
      "accordance with BS4937 parts 1 and 2:1973 and NBS monograph 125 based on "
      "IPTS-68. E.m.f. values are given in millivolts and temperature in "
      "degrees C. Cold junction is at 0°C. To assist in interpolating between "
      "two given values, the difference between successive e.m.f. readings is "
      "shown below the main reading.")

    P(b, lang, "Platin: 10% rhodi-platin.", "Platinum: 10 per cent Rhodium-Platinum.")

    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[0:6], ["Temperature"] + _TEMP[0:6],
        _cal(_S, 0, 5),
        caption_vi="Bảng hiệu chuẩn loại S — 0 °C đến 500 °C",
        caption_en="Calibration table, Type S — 0 °C to 500 °C")
    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[6:12], ["Temperature"] + _TEMP[6:12],
        _cal(_S, 6, 11),
        caption_vi="Bảng hiệu chuẩn loại S — 600 °C đến 1100 °C",
        caption_en="Calibration table, Type S — 600 °C to 1100 °C")
    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[12:18], ["Temperature"] + _TEMP[12:18],
        _cal(_S, 12, 17),
        caption_vi="Bảng hiệu chuẩn loại S — 1200 °C đến 1700 °C",
        caption_en="Calibration table, Type S — 1200 °C to 1700 °C")

    P(b, lang, "Platin: 13% rhodi-platin.", "Platinum: 13 per cent Rhodium-Platinum.")

    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[0:6], ["Temperature"] + _TEMP[0:6],
        _cal(_R, 0, 5),
        caption_vi="Bảng hiệu chuẩn loại R — 0 °C đến 500 °C",
        caption_en="Calibration table, Type R — 0 °C to 500 °C")
    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[6:12], ["Temperature"] + _TEMP[6:12],
        _cal(_R, 6, 11),
        caption_vi="Bảng hiệu chuẩn loại R — 600 °C đến 1100 °C",
        caption_en="Calibration table, Type R — 600 °C to 1100 °C")
    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[12:18], ["Temperature"] + _TEMP[12:18],
        _cal(_R, 12, 17),
        caption_vi="Bảng hiệu chuẩn loại R — 1200 °C đến 1700 °C",
        caption_en="Calibration table, Type R — 1200 °C to 1700 °C")

    P(b, lang,
      "Bảng hiệu chuẩn chuẩn cho cặp nhiệt điện 6% rhodi-platin: 30% "
      "rhodi-platin (loại B), được hiệu chuẩn theo BS4937 phần 7 và tài liệu "
      "NBS monograph 125 dựa trên IPTS-68. Giá trị e.m.f. tính bằng milivôn, "
      "nhiệt độ tính bằng độ C, điểm nối lạnh ở 0 °C. Để hỗ trợ nội suy giữa "
      "hai giá trị đã cho, hiệu số giữa các lần đọc e.m.f. liên tiếp được thể "
      "hiện bên dưới giá trị chính.",
      "Standard calibration table for 6% rhodium-platinum: 30% "
      "rhodium-platinum (Type B) thermocouples calibrated in accordance with "
      "BS4937 part 7 and NBS monograph 125 based on IPTS-68. E.m.f. values are "
      "given in millivolts and temperature in degrees C. Cold junction is at "
      "0C. to assist in interpolating between two given values, the differences "
      "between successive e.m.f readings is shown below the main reading.")

    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[0:6], ["Temperature"] + _TEMP[0:6],
        _cal(_B, 0, 5),
        caption_vi="Bảng hiệu chuẩn loại B — 0 °C đến 500 °C",
        caption_en="Calibration table, Type B — 0 °C to 500 °C")
    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[6:12], ["Temperature"] + _TEMP[6:12],
        _cal(_B, 6, 11),
        caption_vi="Bảng hiệu chuẩn loại B — 600 °C đến 1100 °C",
        caption_en="Calibration table, Type B — 600 °C to 1100 °C")
    TBL(b, lang,
        ["Nhiệt độ"] + _TEMP[12:19], ["Temperature"] + _TEMP[12:19],
        _cal(_B, 12, 18),
        caption_vi="Bảng hiệu chuẩn loại B — 1200 °C đến 1800 °C",
        caption_en="Calibration table, Type B — 1200 °C to 1800 °C")

    NOTE(b, lang,
      "Cặp nhiệt điện 6% rhodi-platin: 30% rhodi-platin được đảm bảo có sai số "
      "trong các giới hạn sau: ±3 °C trong khoảng 0 °C đến 1100 °C. ±4 °C "
      "trong khoảng 1100 °C đến 1800 °C",
      "6% rhodium-platinum: 30% rhodium-platinum thermocouples are guaranteed "
      "to be accurate within the following tolerances: ±3C over the range "
      "0C to 1100C. ±4C over the range 1100C to 1800C")

    return b
