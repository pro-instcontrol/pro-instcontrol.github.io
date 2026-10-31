# -*- coding: utf-8 -*-
"""Applications of process control & instrumentation — bilingual page.

Covers the major application sectors requested by the user:
boiler control, power-plant control & instrumentation, oil refining /
hydrocarbon processing, and food & beverage. Grounded in the BCIT
course library (ISA boiler-control notes, Lindsley's power-plant C&I,
Applied Process Control Systems, Natural Gas Engineering Handbook).
"""

from framework import Page, section_open, section_close, write, render, page_intro

# ---- boiler: which loops, what they guard against ---------------------------
BOILER_LOOPS = [
    ("Drum level (feedwater)",
     "Mức nước trống (nước cấp)",
     "Three-element control (level + steam flow + feed flow) replaces single-element on variable load; "
     "corrects swell and shrink.",
     "Điều khiển ba phần tử (mức + lưu lượng hơi + lưu lượng nước cấp) thay thế đơn phần tử khi tải biến "
     "động; khắc phục hiện tượng trương và co.",
     "LT on drum, FT on steam and feed lines",
     "Cảm biến mức LT trên trống, FT trên đường hơi và đường nước cấp"),
    ("Combustion (fuel / air)",
     "Cháy (nhiên liệu / khí)",
     "Master pressure controller sets firing rate; cross-limiting keeps air ahead on increase, fuel ahead "
     "on decrease; O2 trim trims excess air.",
     "Bộ điều khiển áp suất chính đặt tốc độ đốt; giới hạn chéo giữ khí dẫn trước khi tăng, nhiên liệu dẫn "
     "trước khi giảm; O2 trim tinh chỉnh lượng dư khí.",
     "FT on fuel & air, ZrO2 O2 analyser, FD/ID fan dampers",
     "FT nhiên liệu & khí, máy phân tích O2 (ZrO2), cửa gió quạt cấp/hút"),
    ("Steam temperature",
     "Nhiệt độ hơi",
     "Desuperheater sprays water into superheated steam; single-element spray control holds superheat.",
     "Bộ giải siêu nhiệt phun nước vào hơi quá nhiệt; điều khiển phun đơn phần tử giữ độ siêu nhiệt.",
     "TT on superheater outlet, spray control valve",
     "TT tại đầu ra quá nhiệt, van điều khiển phun"),
    ("Furnace draft",
     "Áp suất lò",
     "Measured on 2oo3 transmitters per ISA-77.41; ID-fan damper holds a slight negative pressure.",
     "Đo bằng 3 truyền mức dư (2oo3) theo ISA-77.41; cửa quạt hút giữ áp suất âm nhẹ.",
     "3 pressure transmitters, ID fan damper",
     "3 bộ truyền áp suất, cửa quạt hút"),
]

# ---- power plant: what the C&I must do --------------------------------------
POWER_ITEMS = [
    ("Unit / turbine control",
     "Điều khiển tổ máy / tuabin",
     "Load, speed and extraction control of the turbo-generator producing MW onto the grid.",
     "Điều khiển tải, tốc độ và trích của tuabin-máy phát sinh MW lên lưới."),
    ("Boiler & HRSG control",
     "Điều khiển lò hơi & HRSG",
     "Drum/HRSG steam production, feedwater and combustion — the same loops as the boiler section.",
     "Sinh hơi trống/HRSG, nước cấp và cháy — các vòng như phần lò hơi."),
    ("Distributed control system (DCS)",
     "Hệ điều khiển phân tán (DCS)",
     "Thousands of I/O, advanced control and historian in one redundant architecture.",
     "Hàng ngàn I/O, điều khiển nâng cao và cơ sở dữ liệu lịch sử trong một kiến trúc dự phòng."),
    ("Turbine protection / ESD",
     "Bảo vệ tuabin / ESD",
     "Overspeed, vibration and trip systems — independent of the DCS, separate vote.",
     "Quá tốc, rung động và hệ cắt — độc lập với DCS, bỏ phiếu riêng."),
    ("SCADA & plant network",
     "SCADA & mạng nhà máy",
     "Station-to-grid and auxiliary monitoring; KKS tagging identifies every tag.",
     "Giám sát trạm–lưới và phụ trợ; mã KKS định danh mọi thẻ."),
    ("Fuel & environmental",
     "Nhiên liệu & môi trường",
     "Coal/pulveriser, gas or waste-to-energy; emissions, efficiency and heat-rate optimisation.",
     "Than/nghiền bột, khí hoặc đốt rác phát điện; phát thải, hiệu suất và tối ưu suất tiêu nhiệt."),
]

# ---- refinery / hydrocarbon: units + standards ------------------------------
REFINERY_UNITS = [
    ("Distillation",
     "Chưng cất",
     "Atmospheric and vacuum columns; temperature and pressure profiles separate crude into cuts.",
     "Tháp chưng cất thường và chân không; bình đồ nhiệt độ và áp suất tách dầu thô thành các phân đoạn."),
    ("Fluid catalytic cracking (FCC)",
     "Cracking xúc tác lưu động (FCC)",
     "Reactor–regenerator pair; catalyst circulation and strict temperature control keep yield and safety.",
     "Cặp reactor–regenerator; tuần hoàn xúc tác và điều khiển nhiệt độ chặt chẽ giữ năng suất và an toàn."),
    ("Hydrotreating / hydrogen",
     "Hydrotreating / hydro",
     "High-pressure reactors remove sulphur; hydrogen partial-pressure control is safety-critical.",
     "Reactor áp suất cao loại bỏ lưu huỳnh; điều khiển áp suất riêng phần hydro mang tính an toàn tới hạn."),
    ("Fired heaters",
     "Lò đốt",
     "Mass-flow and excess-O2 control protect tubes and efficiency; flame safeguard trips on loss of flame.",
     "Điều khiển lưu lượng khối và dư O2 bảo vệ ống và hiệu suất; bảo vệ ngọn lửa cắt khi mất lửa."),
    ("Compressors & rotating equipment",
     "Máy nén & thiết bị quay",
     "Anti-surge control protects the machine; vibration and axial-position probes feed protection.",
     "Điều khiển chống surge bảo vệ máy; đầu dò rung động và vị trí trục cấp cho bảo vệ."),
    ("Pipelines & terminals",
     "Đường ống & kho",
     "Custody-transfer metering (orifice, Coriolis), leak detection, tank gauging and overfill protection.",
     "Đo chuyển giao quyền sở hữu (lỗ khoan, Coriolis), phát hiện rò, đo mức bồn và chống tràn."),
]

REFINERY_STD = [
    ("API RP 551", "Thiết bị đo quá trình", "Installation practice for the common measuring instruments."),
    ("API RP 552", "Hệ truyền tín hiệu", "Pneumatic and electronic transmission systems."),
    ("API RP 553", "Van điều khiển", "Control-valve installation and selection."),
    ("API RP 554", "Thiết bị đo & điều khiển", "Process instrumentation and control."),
    ("API RP 555", "Máy phân tích", "Process analysers in the plant."),
    ("IEC 60079", "Vùng nguy hiểm", "Explosive atmospheres, Ex protection concepts, IP codes."),
    ("IEC 61511", "Hệ an toàn (SIS)", "Safety instrumented systems for the process industry."),
    ("API RP 2350", "Chống tràn bồn", "Independent high-high level protection for storage tanks."),
]

# ---- food & beverage: what is special ---------------------------------------
FOOD_ITEMS = [
    ("Heat treatment",
     "Xử lý nhiệt",
     "Pasteurisation, UHT and aseptic hold; temperature is a micro-critical variable with full traceability.",
     "Thanh trùng, UHT và giữ vô trùng; nhiệt độ là biến vi-sinh tới hạn, truy xuất đầy đủ."),
    ("Clean-in-place (CIP) / SIP",
     "CIP / SIP",
     "Automated cleaning/sterilising of the process without dismantling; conductivity or turbidity confirms "
     "rinses.",
     "Làm sạch/khử trùng tự động mà không tháo rời; độ dẫn hoặc độ đục xác nhận các lần xả."),
    ("Batch & recipe control",
     "Điều khiển mẻ & công thức",
     "ISA-88 / IEC 61512 recipe model: procedural control, units, phases and equipment states.",
     "Mô hình công thức ISA-88 / IEC 61512: điều khiển thủ tục, đơn vị, pha và trạng thái thiết bị."),
    ("Hygienic instrumentation",
     "Thiết bị vệ sinh",
     "3-A / EHEDG design, tri-clamp, polished welds, diaphragm seals; magmeters dominate clean flows.",
     "Thiết kế 3-A / EHEDG, tri-clamp, mối hàn bóng, phớt màng; từ kế chiếm ưu thế dòng sạch."),
    ("Cold chain & refrigeration",
     "Chuỗi lạnh & lạnh",
     "Temperature and pressure control of ammonia/CO2 plants; loss of cooling is a product-safety event.",
     "Điều khiển nhiệt độ và áp suất thiết bị amoniac/CO2; mất lạnh là sự cố an toàn sản phẩm."),
    ("Fill, pack & line monitoring",
     "Chiết, đóng gói & giám sát line",
     "Flow, weight and vision check; the operator screens in the BCIT Wonderware set are food-industry "
     "examples.",
     "Lưu lượng, cân và thị giác; các màn hình vận hành trong bộ Wonderware BCIT là ví dụ ngành thực phẩm."),
]


# ---- food & beverage: what the industry actually measures ------------------
# Each row follows a chapter of "Instrumentation and Sensors for the Food
# Industry" (Kress-Rogers & Brimelow, 2nd ed., Woodbury 2001), now in the library.
FOOD_MEASURES = [
    ("Temperature &amp; pressure",
     "Nhiệt độ &amp; áp suất",
     "The base variables of every process step: pasteurisation hold, evaporation, sterilisation, "
     "chilling. Sensors must survive CIP at 80–90 °C and stay hygienic.",
     "Biến cơ bản của mọi công đoạn: giữ thanh trùng, bay hơi, tiệt trùng, làm lạnh. Cảm biến phải chịu "
     "được CIP 80–90 °C và vẫn hợp vệ sinh.",
     "Pt100 in hygienic pockets, diaphragm-seal gauges, remote IR thermometry",
     "Pt100 trong vỏ vệ sinh, áp kế phớt màng, đo nhiệt hồng ngoại từ xa"),
    ("Level &amp; flow",
     "Mức &amp; lưu lượng",
     "Batching, dosing and mass balance. Flow is the usual manipulated variable; level protects tanks "
     "from overfill and pumps from running dry.",
     "Phối liệu, định lượng và cân bằng vật chất. Lưu lượng thường là biến thao tác; mức bảo vệ bồn "
     "khỏi tràn và bơm khỏi chạy khô.",
     "Coriolis or electromagnetic flowmeters, radar/ultrasonic level",
     "Lưu lượng kế Coriolis hoặc điện từ, đo mức radar/siêu âm"),
    ("Colour",
     "Màu sắc",
     "Consumers judge quality by colour before taste. Reflectance measurement in L*a*b* replaces the "
     "inspector's eye and drives optical sorting.",
     "Người tiêu dùng đánh giá chất lượng bằng màu trước khi nếm. Đo phản xạ theo L*a*b* thay mắt "
     "người kiểm và điều khiển máy phân loại quang học.",
     "Colour reflectance spectrophotometer, in-line colour cameras, sorters",
     "Quang phổ kế phản xạ màu, camera màu in-line, máy phân loại"),
    ("Composition — NIR / FTIR",
     "Thành phần — NIR / FTIR",
     "Fat, protein, moisture and sugar measured without reagents, through a window or a probe, in "
     "seconds. NIR handles at-line and in-line; FTIR resolves the mid-infrared fingerprints.",
     "Đo béo, đạm, ẩm và đường không cần thuốc thử, qua cửa sổ hoặc đầu dò, trong vài giây. NIR dùng "
     "at-line và in-line; FTIR phân giải dấu vân tay hồng ngoại trung.",
     "NIR spectrometer with fibre probe, ATR-FTIR, microwave moisture gauge",
     "Quang phổ kế NIR đầu dò sợi quang, ATR-FTIR, máy đo ẩm vi sóng"),
    ("Water activity",
     "Hoạt độ nước",
     "Not water content but available water — the variable that decides whether micro-organisms can "
     "grow. It sets shelf life for dried, baked and intermediate-moisture foods.",
     "Không phải hàm ẩm mà là nước khả dụng — biến quyết định vi sinh vật có phát triển được hay "
     "không. Nó quyết định hạn dùng của thực phẩm khô, nướng và ẩm trung gian.",
     "Chilled-mirror or capacitive aw meter, equilibrium RH sensor",
     "Máy đo aw gương lạnh hoặc điện dung, cảm biến RH cân bằng"),
    ("Ultrasound",
     "Siêu âm",
     "Non-invasive and non-destructive: thickness, level, flow and — through attenuation and velocity — "
     "composition and texture of solid foods.",
     "Không xâm nhập và không phá hủy: độ dày, mức, lưu lượng và — qua suy giảm và vận tốc — thành phần "
     "và cấu trúc của thực phẩm rắn.",
     "Clamp-on ultrasonic flowmeter, pulse-echo probes, air-coupled transducers",
     "Lưu lượng kế siêu âm kẹp ngoài, đầu dò xung-dội, đầu dò ghép không khí"),
    ("Rheology &amp; texture",
     "Lưu biến &amp; cấu trúc",
     "How the product flows and how it feels in the mouth. Viscosity, yield stress and texture are "
     "quality attributes and also line-hydraulics inputs.",
     "Sản phẩm chảy thế nào và cảm giác trong miệng ra sao. Độ nhớt, ứng suất chảy và cấu trúc là thuộc "
     "tính chất lượng, đồng thời là đầu vào thủy lực đường ống.",
     "In-line viscometer, oscillatory rheometer, texture analyser",
     "Nhớt kế in-line, lưu biến kế dao động, máy phân tích cấu trúc"),
    ("Microbial &amp; biosensors",
     "Vi sinh &amp; cảm biến sinh học",
     "Contamination is the one failure that reaches the consumer. Conductance/impedance, immunosensors "
     "and DNA probes shorten a two-day plate count to hours.",
     "Nhiễm khuẩn là sự cố duy nhất tới tay người tiêu dùng. Độ dẫn/trở kháng, cảm biến miễn dịch và "
     "đầu dò DNA rút ngắn 2 ngày cấy đĩa xuống còn vài giờ.",
     "Impedance microbiology system, ELISA/immunosensor, PCR/DNA probe",
     "Hệ vi sinh trở kháng, ELISA/cảm biến miễn dịch, PCR/đầu dò DNA"),
    ("Flavour &amp; freshness",
     "Hương vị &amp; độ tươi",
     "Electronic noses and tongues compare a volatiles or taste fingerprint against a trained model — "
     "fast screening where a sensory panel is too slow.",
     "Mũi và lưỡi điện tử so sánh dấu vân tay bay hơi hoặc vị với mô hình đã huấn luyện — sàng lọc "
     "nhanh nơi hội đồng cảm quan quá chậm.",
     "Metal-oxide or conducting-polymer e-nose, potentiometric e-tongue",
     "Mũi điện tử oxit kim loại hoặc polymer dẫn, lưỡi điện tử điện thế"),
    ("Foreign bodies",
     "Dị vật",
     "Metal, glass and stone detection is a legal and brand-protection requirement, checked at the end "
     "of the line on every pack.",
     "Phát hiện kim loại, thủy tinh và sỏi là yêu cầu pháp lý và bảo vệ thương hiệu, kiểm ở cuối line "
     "trên từng gói.",
     "Metal detector (balanced coil), X-ray inspection, checkweigher",
     "Máy dò kim loại (cuộn cân bằng), kiểm tra X-quang, cân kiểm"),
]


# ---- the sectors the four deep dives leave out -------------------------------
# One dominant variable per sector, and the reason that variable is hard.
SECTORS = [
    ("Water &amp; wastewater",
     "Nước &amp; nước thải",
     "Flow, level, pH, residual chlorine",
     "Lưu lượng, mức, pH, clo dư",
     "The sensor sits <em>in</em> the process, not beside it: fouling, biofouling and exhausted reagent "
     "drift the reading long before the instrument fails outright. Turndown from storm flow to night "
     "flow can reach 20:1.",
     "Cảm biến nằm <em>trong</em> chính quá trình: bám cặn, bám sinh học và cạn thuốc thử làm trôi kết "
     "quả rất lâu trước khi thiết bị hỏng hẳn. Dải biến thiên từ lưu lượng mưa bão đến lưu lượng ban "
     "đêm có thể tới 20:1."),
    ("Mining &amp; metals",
     "Khai khoáng &amp; luyện kim",
     "Slurry density, flow, particle size",
     "Tỷ trọng bùn, lưu lượng, cỡ hạt",
     "Abrasion eats liners and electrodes. A magnetic flowmeter needs a full pipe and a conductive "
     "fluid, and density usually comes from a nuclear gauge that carries its own licensing burden.",
     "Mài mòn ăn lớp lót và điện cực. Lưu lượng kế điện từ cần đầy ống và chất lỏng dẫn điện, còn tỷ "
     "trọng thường lấy từ đồng vị phóng xạ — kèm theo nghĩa vụ cấp phép riêng."),
    ("Pulp &amp; paper",
     "Bột giấy &amp; giấy",
     "Consistency, kappa number, basis weight",
     "Độ đặc, chỉ số kappa, định lượng giấy",
     "Consistency is measured through the flowing stock, not sampled from it. Basis weight comes from a "
     "frame that traverses the sheet, so the measurement is a profile across the web, not a point.",
     "Độ đặc được đo xuyên qua dòng bột đang chảy, không lấy mẫu. Định lượng giấy đến từ khung quét "
     "chạy ngang tờ giấy, nên phép đo là một biên dạng theo chiều rộng chứ không phải một điểm."),
    ("Pharmaceutical &amp; life sciences",
     "Dược phẩm &amp; khoa học đời sống",
     "Conductivity, pressure, temperature, particle count",
     "Độ dẫn, áp suất, nhiệt độ, số hạt",
     "The instrument must be cleanable <em>and provable</em>: CIP/SIP cycles, surface finish, and a "
     "calibration record that survives an audit. Data integrity — ALCOA+, 21 CFR Part 11 — is part of "
     "the specification, not an afterthought.",
     "Thiết bị phải làm sạch được <em>và chứng minh được</em>: chu trình CIP/SIP, độ nhẵn bề mặt, và hồ "
     "sơ hiệu chuẩn sống sót qua kỳ thanh tra. Tính toàn vẹn dữ liệu — ALCOA+, 21 CFR Part 11 — là một "
     "phần của bản chỉ định, không phải việc làm sau."),
    ("Cement &amp; minerals",
     "Xi măng &amp; khoáng sản",
     "Kiln shell temperature, gas analysis, feed rate",
     "Nhiệt độ vỏ lò, phân tích khí, lưu lượng liệu",
     "The kiln is a rotating reactor tens of metres long with a residence time in tens of minutes, so "
     "most loops are feedforward: by the time feedback arrives the product has already left the hot zone.",
     "Lò là một thiết bị phản ứng quay dài hàng chục mét với thời gian lưu tính bằng chục phút, nên "
     "phần lớn vòng là feedforward: lúc hồi tiếp đến thì sản phẩm đã ra khỏi vùng nhiệt rồi."),
    ("Hydrogen &amp; the energy transition",
     "Hydro &amp; chuyển dịch năng lượng",
     "Mass flow, purity, pressure",
     "Lưu lượng khối, độ tinh khiết, áp suất",
     "Hydrogen embrittles steel and escapes through the smallest gap, so mass flow (Coriolis) beats "
     "volumetric, and purity needs an analyser that is itself a process instrument. An electrolyser adds "
     "a fast pressure loop that couples the plant to the gas grid.",
     "Hydro làm giòn thép và lọt qua khe nhỏ nhất, nên lưu lượng khối (Coriolis) đáng tin hơn lưu lượng "
     "thể tích, và độ tinh khiết cần máy phân tích mà bản thân nó cũng là thiết bị quá trình. Điện phân "
     "thêm một vòng áp suất nhanh nối nhà máy với lưới khí."),
    ("Biomass &amp; waste-to-energy",
     "Sinh khối &amp; điện từ chất thải",
     "Moisture, calorific value, combustion O<sub>2</sub>",
     "Độ ẩm, nhiệt trị, O<sub>2</sub> cháy",
     "Fuel properties change hourly, so the controller chases a moving target. Moisture is the largest "
     "disturbance and the hardest to measure online — which is why so much of the loop is still run on "
     "operator judgement.",
     "Tính chất nhiên liệu đổi theo giờ, nên bộ điều khiển đuổi theo một mục tiêu di động. Độ ẩm là "
     "nhiễu lớn nhất và khó đo trực tuyến nhất — vì thế phần lớn vòng vẫn chạy theo phán đoán của vận "
     "hành."),
]


# ---- process response type decides the controller ---------------------------
# Taxonomy per Control Engineering's PID Spotlight series (parts 10, 11, 15)
# and Control Global / Rhinehart on matching strategy to process characteristics.
PROCESS_TYPES = [
    ("Self-limiting, lag-dominant",
     "Tự ổn định, quán tính chi phối",
     "Settles at a new value; the lag is long compared with the dead time.",
     "Về một giá trị mới; quán tính dài hơn nhiều so với thời gian trễ.",
     "PID. Gain above the baseline, derivative may help. This is the default case, and the one "
     "every tuning guide is written for.",
     "PID. Hệ số khuếch đại trên mức cơ sở, đạo hàm có thể có ích. Đây là trường hợp mặc định, và "
     "cũng là trường hợp mọi tài liệu hiệu chỉnh viết cho.",
     "Steam temperature, most pressure and flow loops.",
     "Nhiệt độ hơi, phần lớn vòng áp suất và lưu lượng."),
    ("Self-limiting, deadtime-dominant",
     "Tự ổn định, trễ chi phối",
     "Also settles, but the dead time dominates the response.",
     "Cũng về một giá trị, nhưng thời gian trễ chi phối đáp ứng.",
     "PI with <strong>derivative off</strong> and gain <strong>below</strong> the baseline, tuned "
     "critically damped. Overshoot is expensive: the next correction waits a full dead time.",
     "PI, <strong>tắt đạo hàm</strong> và hệ số khuếch đại <strong>dưới</strong> mức cơ sở, hiệu "
     "chỉnh tới tắt dần tới hạn. Vọt lố rất đắt: lần sửa tiếp theo phải chờ hết một thời gian trễ.",
     "On-line composition analysers, moisture, sheet properties, kiln exit gas.",
     "Máy phân tích thành phần trực tuyến, độ ẩm, tính chất tờ giấy, khí ra khỏi lò."),
    ("Integrating",
     "Tích phân",
     "Ramps. It never settles on its own — the valve position sets the slope.",
     "Tăng dốc. Tự nó không bao giờ dừng — vị trí van quyết định độ dốc.",
     "P-only, or PI with a narrow band and minimal integral. A level loop is a buffer, not a "
     "setpoint tracker; the inventory is what absorbs the disturbance.",
     "Chỉ P, hoặc PI với dải hẹp và tích phân tối thiểu. Vòng mức là bộ đệm, không phải bộ bám giá "
     "trị đặt; chính lượng tồn chứa mới là thứ hấp thụ nhiễu.",
     "Drum level, gas-header pressure, accumulators and surge drums.",
     "Mức nước trống, áp suất header khí, bình tích áp và bình đệm."),
    ("Near-integrating / high order",
     "Gần tích phân / bậc cao",
     "Ramps slowly, then bends towards a value it takes a long time to reach.",
     "Tăng dốc chậm rồi cong dần về một giá trị mất rất lâu mới tới.",
     "PI, detuned. If you cannot tell which of the two it is, treat it as integrating and accept "
     "the slower response.",
     "PI, hiệu chỉnh chậm. Nếu không phân biệt được là dạng nào, hãy coi như tích phân và chấp "
     "nhận đáp ứng chậm hơn.",
     "Large mixing vessels, long pipelines, some furnace passes.",
     "Bình trộn lớn, tuyến ống dài, một số pass của lò."),
]


def build():
    pg = Page(
        "applications.html",
        "app",
        "Applications of process control & instrumentation | I&amp;C Field Guide",
        "Ứng dụng của điều khiển và thiết bị đo quá trình | Sổ tay I&amp;C",
        "Where the measurement chain meets the real plant: boiler control, power-plant C&I, oil refining, "
        "food & beverage — plus the dominant variable in the seven sectors those four leave out.",
        "Nơi chuỗi đo lường gặp nhà máy thực tế: điều khiển lò hơi, C&I nhà máy điện, lọc dầu, thực phẩm "
        "&amp; đồ uống — cộng với đại lượng chi phối ở bảy ngành còn lại.",
    )

    body = page_intro(
        pg,
        "Process control in the real plant",
        "Điều khiển quá trình trong nhà máy thực tế",
        "The instruments on the Fundamentals and Instruments pages are generic. Here they are put to work: "
        "the same transmitter, the same PID loop, the same valve — applied where the stakes are physical.",
        "Các thiết bị ở trang Cơ bản và Thiết bị là chung chung. Ở đây chúng được dùng thực tế: cùng một bộ "
        "truyền, cùng một vòng PID, cùng một van — áp dụng nơi hậu quả là vật lý.",
        [
            ("why", "Why these industries", "Vì sao những ngành này"),
            ("boiler", "Boiler control", "Điều khiển lò hơi"),
            ("power", "Power-plant C&I", "C&I nhà máy điện"),
            ("refinery", "Oil refining", "Lọc dầu"),
            ("food", "Food & beverage", "Thực phẩm &amp; đồ uống"),
            ("sectors", "The other seven", "Bảy ngành còn lại"),
            ("response", "Process response", "Dạng đáp ứng"),
            ("thread", "The common thread", "Sợi dây chung"),
        ],
    )

    # 01 why
    body += section_open("01", "Why these industries", "Vì sao những ngành này", pg, "why")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Five reasons a plant automates", "Năm lý do một nhà máy tự động hóa")
    body += pg.p(
        "Process-control theory is the same everywhere; what changes is the consequence of getting it wrong. "
        "The Applied Process Control Systems lecture opens with the objectives every plant is built around.",
        "Lý thuyết điều khiển quá trình ở đâu cũng giống nhau; điều khác là hậu quả khi làm sai. Bài giảng "
        "Applied Process Control Systems mở đầu bằng những mục tiêu mọi nhà máy đều xoay quanh.")
    body += "</div><div class=\"grid c3\">"
    for en, vi in [
        ("Safety of equipment &amp; personnel",
         "An toàn thiết bị &amp; nhân sự"),
        ("Production specification (quality &amp; quantity)",
         "Chỉ tiêu sản xuất (chất lượng &amp; số lượng)"),
        ("Operational constraints",
         "Các ràng buộc vận hành"),
        ("Environmental &amp; regulatory compliance",
         "Tuân thủ môi trường &amp; quy định"),
        ("Economics — smooth, optimised rate",
         "Kinh tế — tốc độ êm, tối ưu"),
        ("Never release hydrocarbons to atmosphere",
         "Không bao giờ xả hydrocarbon ra khí quyển"),
    ]:
        body += "<div class=\"card\"><h3>%s</h3></div>" % (pg.span(en, vi))
    body += "</div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("The control objective list", "Danh sách mục tiêu điều khiển"),
        pg.p(
            "Safety and environmental compliance sit first for a reason: a smooth, optimised rate is worth "
            "nothing if the plant is on fire or the neighbourhood is contaminated. Every application below "
            "is an exercise in balancing all five.",
            "An toàn và tuân thủ môi trường đứng đầu có lý do: tốc độ êm và tối ưu chẳng giá trị gì nếu nhà "
            "máy đang cháy hoặc khu dân cư bị ô nhiễm. Mọi ứng dụng dưới đây là bài toán cân bằng cả năm "
            "mục tiêu."))
    body += section_close()

    # 02 boiler
    body += section_open("02", "Boiler control", "Điều khiển lò hơi", pg, "boiler")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Four interlocking loops", "Bốn vòng đan nhau")
    body += pg.p(
        "An ISA boiler-control seminar reduces the whole problem to four basic control functions: furnace "
        "draft, drum-level feedwater, fuel-air (combustion) and steam temperature. Fuels may be gas, oil, "
        "coal or a combination — the loops are the same.",
        "Một hội thảo điều khiển lò hơi của ISA thu gọn toàn bộ vấn đề về bốn hàm điều khiển cơ bản: áp "
        "suất lò, mức nước trống (nước cấp), nhiên liệu–không khí (cháy) và nhiệt độ hơi. Nhiên liệu có "
        "thể là khí, dầu, than hay phối hợp — các vòng thì như nhau.")
    body += "</div>"
    body += "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>%s</th><th>%s</th>" \
            "<th>%s</th></tr></thead><tbody>" % (
        pg.th("Loop", "Vòng"), pg.th("What it does", "Tác dụng"),
        pg.th("Typical instruments", "Thiết bị điển hình"))
    for n_en, n_vi, d_en, d_vi, i_en, i_vi in BOILER_LOOPS:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>" % (
            pg.span(n_en, n_vi), pg.span(d_en, d_vi), pg.span(i_en, i_vi))
    body += "</tbody></table></div>"

    # three-element explainer + svg
    body += "<div class=\"g-2-1\"><div>"
    body += pg.h3("From one element to three", "Từ một đến ba phần tử")
    body += pg.p(
        "A single-element controller (drum level only) is acceptable on small, steady boilers. On variable "
        "load it is fooled by swell and shrink — a sudden load increase makes the level momentarily rise "
        "(swell) as bubbles expand, then fall. Adding steam flow gives a two-element loop that anticipates "
        "the swell; adding feedwater flow gives the three-element loop that also rejects disturbances on "
        "the feed side. Drum pressure is used to compensate level for the density change with pressure.",
        "Bộ điều khiển đơn phần tử (chỉ mức trống) chấp nhận được ở lò nhỏ, tải ổn định. Với tải biến động "
        "nó bị đánh lừa bởi trương và co — tăng tải đột ngột làm mức trồi lên thoáng chốc (trương) do bọt "
        "giãn nở, rồi lại xuống. Thêm lưu lượng hơi thành hai phần tử dự báo trước trương; thêm lưu lượng "
        "nước cấp thành ba phần tử cũng triệt nhiễu phía nước cấp. Áp suất trống dùng bù mức do đổi tỷ "
        "trọng theo áp.")
    body += "</div><div class=\"card\">"
    body += ("<svg viewBox=\"0 0 320 220\" role=\"img\" aria-label=\"Boiler three-element feedwater control\">"
             "<style>.bx{fill:#fafafa;stroke:#2a2a2a;stroke-width:1.4}"
             ".t{font:11px Inter,sans-serif;fill:#111;text-anchor:middle}"
             ".w{stroke:#2a2a2a;stroke-width:1.6;fill:none}.dot{fill:#2a2a2a}</style>"
             "<rect x=\"20\" y=\"70\" width=\"70\" height=\"80\" rx=\"8\" class=\"bx\"/>"
             "<text x=\"55\" y=\"100\" class=\"t\">Trống</text><text x=\"55\" y=\"116\" class=\"t\">hơi</text>"
             "<rect x=\"210\" y=\"30\" width=\"90\" height=\"40\" rx=\"6\" class=\"bx\"/>"
             "<text x=\"255\" y=\"54\" class=\"t\">Bộ điều khiển</text>"
             "<rect x=\"210\" y=\"140\" width=\"90\" height=\"40\" rx=\"6\" class=\"bx\"/>"
             "<text x=\"255\" y=\"164\" class=\"t\">Van nước cấp</text>"
             "<path class=\"w\" d=\"M90 100 H210 V70\"/>"
             "<circle cx=\"150\" cy=\"100\" r=\"4\" class=\"dot\"/><text x=\"150\" y=\"92\" class=\"t\" "
             "font-size=\"9\">LT mức</text>"
             "<path class=\"w\" d=\"M90 75 H255 V70\"/>"
             "<circle cx=\"150\" cy=\"75\" r=\"4\" class=\"dot\"/><text x=\"150\" y=\"67\" class=\"t\" "
             "font-size=\"9\">FT hơi</text>"
             "<path class=\"w\" d=\"M90 125 H255 V140\"/>"
             "<circle cx=\"150\" cy=\"125\" r=\"4\" class=\"dot\"/><text x=\"150\" y=\"138\" class=\"t\" "
             "font-size=\"9\">FT nước cấp</text>"
             "</svg>")
    body += ("<p class=\"figcap\">%s</p>" % pg.span(
        "Three-element feedwater: level, steam flow and feed flow into one controller.",
        "Nước cấp ba phần tử: mức, lưu lượng hơi và lưu lượng nước cấp vào một bộ điều khiển."))
    body += "</div></div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Reliability by design", "Tin cậy nhờ thiết kế"),
        pg.p(
            "ISA-77.41 calls for redundant furnace-pressure transmitters — two with deviation alarm and "
            "manual transfer, or three with a transmitter-select (2oo3) scheme. Symbols follow ANSI/ISA-5.1.",
            "ISA-77.41 yêu cầu truyền áp suất lò dự phòng — hai cái có báo lệch và chuyển tay, hoặc ba cái "
            "theo sơ đồ chọn truyền (2oo3). Ký hiệu theo ANSI/ISA-5.1."))
    body += section_close()

    # 03 power plant
    body += section_open("03", "Power-plant control &amp; instrumentation",
                         "Điều khiển &amp; thiết bị đo nhà máy điện", pg, "power")
    body += "<div class=\"sec-head\">"
    body += pg.h2("One integrated, interdependent machine", "Một cỗ máy tích hợp, phụ thuộc lẫn nhau")
    body += pg.p(
        "Lindsley's power-plant C&I text describes a station as a highly interdependent system: "
        "thermodynamics, chemistry, metallurgy and high-voltage electrical engineering held together by "
        "control technology. A small mistake can be severe, expensive or tragic — so the C&I is designed, "
        "not bolted on.",
        "Sách C&I nhà máy điện của Lindsley mô tả trạm điện là một hệ rất phụ thuộc lẫn nhau: nhiệt động "
        "học, hóa học, luyện kim và điện cao áp được gắn kết bởi công nghệ điều khiển. Một sai sót nhỏ có "
        "thể nghiêm trọng, tốn kém hoặc thảm khốc — nên C&I được thiết kế, không phải gắn thêm.")
    body += "</div><div class=\"grid c3\">"
    for n_en, n_vi, d_en, d_vi in POWER_ITEMS:
        body += "<div class=\"card\"><h3>%s</h3><p>%s</p></div>" % (
            pg.span(n_en, n_vi), pg.span(d_en, d_vi))
    body += "</div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Plant types", "Các loại nhà máy"),
        pg.p(
            "The same C&I serves the drum boiler, the heat-recovery steam generator (HRSG) of a combined-"
            "cycle gas turbine (CCGT), combined heat and power (CHP) and waste-to-energy — the general "
            "principles are identical; only the balance of plant differs.",
            "Cùng một C&I phục vụ lò hơi trống, bộ sinh hơi thu hồi nhiệt (HRSG) của tổ hợp tuabin khí "
            "chu trình hỗn hợp (CCGT), nhiệt-điện kết hợp (CHP) và đốt rác phát điện — nguyên lý chung "
            "như nhau; chỉ khác cân bằng thiết bị."))
    body += section_close()

    # 04 refinery
    body += section_open("04", "Oil refining &amp; hydrocarbon processing",
                         "Lọc dầu &amp; chế biến hydrocarbon", pg, "refinery")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Many units, one safety culture", "Nhiều phân xưởng, một văn hóa an toàn")
    body += pg.p(
        "A refinery is a chain of unit operations — each with its own control problem and its own hazards. "
        "Natural-gas processing adds separation, dehydration (glycol), compression and orifice metering. "
        "What unifies them is the hazard: flammable, toxic or high-pressure fluid that must never escape.",
        "Nhà máy lọc dầu là một chuỗi các công đoạn — mỗi cái một bài toán điều khiển và một rủi ro riêng. "
        "Chế biến khí thiên nhiên thêm tách, làm khô (glycol), nén và đo lỗ khoan. Điều gắn kết chúng là "
        "nguy hiểm: chất dễ cháy, độc hoặc áp suất cao không được phép thoát ra.")
    body += "</div><div class=\"grid c3\">"
    for n_en, n_vi, d_en, d_vi in REFINERY_UNITS:
        body += "<div class=\"card\"><h3>%s</h3><p>%s</p></div>" % (
            pg.span(n_en, n_vi), pg.span(d_en, d_vi))
    body += "</div>"
    body += "<div class=\"tbl-wrap mt24\"><table class=\"tbl\"><thead><tr><th>%s</th><th>%s</th>" \
            "<th>%s</th></tr></thead><tbody>" % (
        pg.th("Standard", "Tiêu chuẩn"), pg.th("Topic", "Chủ đề"),
        pg.th("Scope", "Phạm vi"))
    for num, topic, scope in REFINERY_STD:
        body += "<tr><td><code>%s</code></td><td>%s</td><td>%s</td></tr>" % (
            num, pg.span(topic, topic), pg.span(scope, scope))
    body += "</tbody></table></div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Independent protection", "Bảo vệ độc lập"),
        pg.p(
            "In hydrocarbon service the basic process control system (BPCS) is backed by a separate safety "
            "instrumented system (SIS) per IEC 61511, and storage tanks by independent high-high level "
            "protection per API 2350. Hazardous areas are classified to IEC 60079 with Ex protection "
            "concepts and IP codes.",
            "Trong dịch vụ hydrocarbon, hệ điều khiển quá trình cơ bản (BPCS) được hậu thuẫn bởi một hệ "
            "đo lường an toàn (SIS) độc lập theo IEC 61511, và bồn chứa bởi bảo vệ mức cao-cao độc lập "
            "theo API 2350. Vùng nguy hiểm được phân loại theo IEC 60079 với các khái niệm bảo vệ Ex và "
            "mã IP."))
    body += section_close()

    # 05 food & beverage
    body += section_open("05", "Food &amp; beverage", "Thực phẩm &amp; đồ uống", pg, "food")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Clean, safe, repeatable — in batches", "Sạch, an toàn, lặp lại — theo mẻ")
    body += pg.p(
        "Food and beverage shares the same sensors and loops as every other sector, but adds two demands: "
        "hygienic, cleanable hardware and recipe-driven batch control. The BCIT Wonderware InTouch demo "
        "screens are built around a food-industry line.",
        "Thực phẩm và đồ uống dùng cùng cảm biến và vòng như mọi ngành, nhưng thêm hai yêu cầu: phần cứng "
        "vệ sinh, dễ làm sạch và điều khiển mẻ theo công thức. Các màn hình demo InTouch Wonderware của "
        "BCIT được xây dựng quanh một line công nghiệp thực phẩm.")
    body += "</div><div class=\"grid c3\">"
    for n_en, n_vi, d_en, d_vi in FOOD_ITEMS:
        body += "<div class=\"card\"><h3>%s</h3><p>%s</p></div>" % (
            pg.span(n_en, n_vi), pg.span(d_en, d_vi))
    body += "</div>"
    body += "<div class=\"sec-head mt24\">"
    body += pg.h3("Ten measurements that decide product quality",
                  "Mười phép đo quyết định chất lượng sản phẩm")
    body += pg.p(
        "Food instrumentation is not exotic — it is the standard measurement chain pushed to meet hygiene, "
        "speed and traceability. This table follows the chapters of the sector's reference work.",
        "Thiết bị đo trong thực phẩm không hề lạ — đó là chuỗi đo tiêu chuẩn được đẩy tới mức đáp ứng vệ "
        "sinh, tốc độ và truy xuất. Bảng này đi theo các chương của sách tham chiếu của ngành.")
    body += "</div>"
    body += "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>%s</th><th>%s</th>" \
            "<th>%s</th></tr></thead><tbody>" % (
        pg.th("Quantity", "Đại lượng"), pg.th("Why it matters", "Vì sao quan trọng"),
        pg.th("Typical instruments", "Thiết bị điển hình"))
    for n_en, n_vi, d_en, d_vi, i_en, i_vi in FOOD_MEASURES:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>" % (
            pg.span(n_en, n_vi), pg.span(d_en, d_vi), pg.span(i_en, i_vi))
    body += "</tbody></table></div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Where to read more", "Đọc thêm ở đâu"),
        pg.p(
            "The whole sector is covered chapter by chapter in "
            "<a href=\"/books/work/100/\">Instrumentation and Sensors for the Food Industry "
            "(2nd Edition)</a> — Kress-Rogers &amp; Brimelow, Woodhead, 2001 — now in the library, with "
            "all 23 chapters readable and downloadable individually.",
            "Toàn bộ ngành được trình bày theo từng chương trong "
            "<a href=\"/books/work/100/\">Instrumentation and Sensors for the Food Industry "
            "(2nd Edition)</a> — Kress-Rogers &amp; Brimelow, Woodhead, 2001 — nay đã có trong thư viện, "
            "cả 23 chương đọc và tải riêng được."))
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("ISA-88 / IEC 61512", "ISA-88 / IEC 61512"),
        pg.p(
            "Batch plants model production as a recipe (procedural control) executed across units and "
            "phases, with equipment states such as idle, running, held and complete. This is the structure "
            "behind every automated brew, dairy and soft-drink line.",
            "Nhà máy mẻ mô hình sản xuất thành công thức (điều khiển thủ tục) thực thi trên các đơn vị và "
            "pha, với trạng thái thiết bị như rỗi, chạy, giữ và hoàn thành. Đây là cấu trúc đằng sau mọi "
            "line bia, sữa và nước giải khát tự động."))
    body += section_close()

    # 06 the other seven sectors
    body += section_open("06", "The other seven", "Bảy ngành còn lại", pg, "sectors")
    body += "<div class=\"sec-head\">"
    body += pg.h2("One dominant variable each", "Mỗi ngành một đại lượng chi phối")
    body += pg.p(
        "The four sectors above are where the textbooks spend their time. Most instrument engineers "
        "actually work in the rest, and in each of those one variable decides the design: it sets the "
        "technology, the calibration interval and the failure mode you will spend your weekends on.",
        "Bốn ngành trên là nơi sách giáo khoa dành thời gian. Phần lớn kỹ sư đo lường thực tế làm việc ở "
        "những ngành còn lại, và ở mỗi ngành ấy có một đại lượng quyết định thiết kế: nó chọn công nghệ, "
        "chọn chu kỳ hiệu chuẩn, và chọn kiểu hỏng mà bạn sẽ dành những ngày cuối tuần để xử lý.")
    body += "</div>"
    body += "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>%s</th><th>%s</th>" \
            "<th>%s</th></tr></thead><tbody>" % (
        pg.th("Sector", "Ngành"), pg.th("The variable that dominates", "Đại lượng chi phối"),
        pg.th("What makes it hard", "Vì sao khó"))
    for s_en, s_vi, v_en, v_vi, h_en, h_vi in SECTORS:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>" % (
            pg.span(s_en, s_vi), pg.span(v_en, v_vi), pg.span(h_en, h_vi))
    body += "</tbody></table></div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Where sector knowledge actually lives", "Kiến thức ngành thực sự nằm ở đâu"),
        pg.p(
            "Very little of this is in a standard. It lives in trade press, in forums and in vendor "
            "application notes — <a href=\"https://www.processindustryforum.com/\" rel=\"noopener\">Process "
            "Industry Forum</a> is one of the larger English-language collections, with application "
            "write-ups, tutorials, a panel of named experts and a partner directory. Note the business "
            "model: the same portal that publishes a genuinely useful commissioning tip also publishes "
            "its partners' efficiency claims. Read it for the mechanism, and treat the percentage as an "
            "advertisement until you have measured your own plant. The <a href=\"advanced/#plant\">total-"
            "plant section</a> takes that argument apart in detail.",
            "Rất ít điều trong số này nằm trong một tiêu chuẩn. Nó sống trong báo ngành, trong các diễn "
            "đàn và trong ghi chú ứng dụng của nhà cung cấp — <a href=\"https://www.processindustryforum.com/\" "
            "rel=\"noopener\">Process Industry Forum</a> là một trong những nơi tập hợp lớn nhất bằng tiếng "
            "Anh, với bài viết ứng dụng, hướng dẫn, một hội đồng chuyên gia có tên và danh bạ đối tác. Hãy "
            "để ý mô hình kinh doanh: chính cổng thông tin đăng một mẹo chạy thử rất hữu ích cũng đăng "
            "tuyên bố hiệu quả của các đối tác. Đọc để lấy cơ chế, và coi phần trăm là quảng cáo cho đến "
            "khi bạn tự đo được nhà máy của mình. Phần <a href=\"advanced/#plant\">toàn nhà máy</a> mổ xẻ "
            "lập luận đó chi tiết."))
    body += section_close()

    # 07 process response decides the controller
    body += section_open("07", "The process decides", "Quá trình quyết định", pg, "response")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Four responses, four controllers", "Bốn dạng đáp ứng, bốn cách điều khiển")
    body += pg.p(
        "Before the question of which controller comes the question of which process. A level loop and "
        "a composition loop can carry identical PIDs and need opposite tuning, because one integrates "
        "and the other is deadtime-dominated. Control Global's R. Russell Rhinehart puts the order "
        "bluntly — fix the process before you tune the controller — and the trade press keeps returning "
        "to the same taxonomy.",
        "Trước câu hỏi dùng bộ điều khiển nào là câu hỏi quá trình thuộc dạng nào. Một vòng mức và một "
        "vòng thành phần có thể mang cùng một PID nhưng cần hiệu chỉnh ngược nhau, vì một cái là quá "
        "trình tích phân còn cái kia bị chi phối bởi thời gian trễ. R. Russell Rhinehart trên Control "
        "Global nói thẳng thứ tự: sửa quá trình trước khi hiệu chỉnh bộ điều khiển. Và báo ngành cứ "
        "quay lại cùng một cách phân loại.")
    body += "</div>"
    body += "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>%s</th><th>%s</th>" \
            "<th>%s</th><th>%s</th></tr></thead><tbody>" % (
        pg.th("Response", "Dạng đáp ứng"), pg.th("What a step does", "Đáp ứng với bậc thang"),
        pg.th("What the controller should do", "Bộ điều khiển nên làm gì"),
        pg.th("Where it shows up here", "Gặp ở đâu trong trang này"))
    for n_en, n_vi, s_en, s_vi, c_en, c_vi, w_en, w_vi in PROCESS_TYPES:
        body += "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            pg.span(n_en, n_vi), pg.span(s_en, s_vi), pg.span(c_en, c_vi), pg.span(w_en, w_vi))
    body += "</tbody></table></div>"
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Why overshoot is expensive when the dead time dominates",
                "Vì sao vọt lố lại đắt khi thời gian trễ chi phối"),
        pg.p(
            "On a deadtime-dominant loop the controller gets one correction, then must wait out the "
            "dead time to see what happened. Overshoot is therefore not a cosmetic defect — it is a "
            "second error that has to be fixed with the same handicap. Control Engineering's PID "
            "Spotlight series works the arithmetic on a 1:10 lag-to-deadtime process: good tuning is "
            "about K&nbsp;=&nbsp;0.33 with Ti&nbsp;=&nbsp;1&nbsp;min/repeat and derivative at zero, "
            "while K&nbsp;=&nbsp;0.60 produces the characteristic sharp reversal at the first peak. "
            "The series' rules are blunt — for a deadtime-dominant process the derivative should "
            "always be zero, and the gain belongs below the baseline, not above it.",
            "Với vòng có thời gian trễ chi phối, bộ điều khiển chỉ được sửa một lần, rồi phải chờ hết "
            "thời gian trễ mới biết chuyện gì xảy ra. Vì thế vọt lố không phải lỗi thẩm mỹ — nó là sai "
            "số thứ hai phải sửa với đúng bất lợi ấy. Loạt bài PID Spotlight của Control Engineering "
            "tính cụ thể trên một quá trình có tỷ lệ quán tính/trễ 1:10: hiệu chỉnh tốt là khoảng "
            "K&nbsp;=&nbsp;0,33 với Ti&nbsp;=&nbsp;1&nbsp;phút/lần lặp và đạo hàm bằng 0, còn "
            "K&nbsp;=&nbsp;0,60 cho ra đặc trưng đảo chiều nhọn tại đỉnh đầu tiên. Quy tắc của loạt "
            "bài rất thẳng: với quá trình trễ chi phối, đạo hàm luôn phải bằng 0, và hệ số khuếch đại "
            "nằm dưới mức cơ sở chứ không phải trên."))
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("The analyser is the slowest instrument in the plant",
                "Máy phân tích là thiết bị chậm nhất trong nhà máy"),
        pg.p(
            "Composition loops are usually cascaded for the same reason: the primary composition "
            "controller sets the setpoint of a fast secondary loop — tray temperature, in a column — "
            "instead of stroking the valve itself. And in-line analysis keeps moving closer to the "
            "reactor. Yokogawa's ACOMP, presented at YNOW2026, pulls a sample from a polymer reactor, "
            "conditions it, and measures molecular weight, viscosity and conversion continuously: "
            "process-to-detector delay of 30&nbsp;seconds to five minutes, then one point per second, "
            "against up to five hours for a laboratory result. Controlling monomer concentration along "
            "a deliberately chosen trajectory held 2&nbsp;% error, and discharging on measurement "
            "rather than on a lab certificate added a batch per day on some reactors. The analyser did "
            "not get more accurate. It got faster — which, for a control loop, is the same thing.",
            "Vòng thành phần thường được cascade cũng vì lý do đó: bộ điều khiển thành phần chính đặt "
            "giá trị đặt cho một vòng thứ cấp nhanh — nhiệt độ đĩa, trong tháp chưng — thay vì tự "
            "đánh van. Và phân tích trực tuyến cứ tiến dần lại gần thiết bị phản ứng. ACOMP của "
            "Yokogawa, trình bày tại YNOW2026, lấy mẫu từ lò phản ứng polymer, xử lý mẫu rồi đo liên "
            "tục khối lượng phân tử, độ nhớt và độ chuyển hoá: trễ từ quá trình tới đầu dò 30 giây "
            "đến năm phút, sau đó một điểm dữ liệu mỗi giây, so với tới năm giờ cho một kết quả phòng "
            "thí nghiệm. Điều khiển nồng độ monomer theo một quỹ đạo chọn trước giữ sai số 2&nbsp;%, "
            "và xả sản phẩm theo kết quả đo thay vì theo phiếu phòng lab thêm được một mẻ mỗi ngày ở "
            "một số lò. Máy phân tích không chính xác hơn. Nó nhanh hơn — và với một vòng điều khiển, "
            "đó là cùng một điều."))
    body += "<div class=\"note mt24\"><span class=\"lbl\">%s</span>%s</div>" % (
        pg.span("Where these rules come from", "Những quy tắc này đến từ đâu"),
        pg.p(
            "Control Global, R. Russell Rhinehart, <a href=\"https://www.controlglobal.com/control/"
            "multivariable-control/article/55411596/effective-process-control-matching-strategies-to-"
            "process-characteristics-and-overcoming-challenges\" rel=\"noopener\">How to fix poor "
            "control and choose the right strategy</a> (Oct 2026) — fix the process first, P-only for "
            "integrating processes, PI for fast stable ones, cascade where the primary measurement "
            "lags. Control Engineering's <a href=\"https://www.controleng.com/control-systems/pid-apc/\" "
            "rel=\"noopener\">PID Spotlight</a> series — part&nbsp;10 deadtime-dominant, part&nbsp;11 "
            "integrating, part&nbsp;13 dead time, part&nbsp;19 tuning best practice, parts&nbsp;29–33 "
            "shaping the response, noise and gap control. And Control Global on <a href=\"https://www."
            "controlglobal.com/show-coverage/ynow-a-yokogawa-users-conference/article/55403109/"
            "yokogawa-yokogawa-closes-the-loop-on-polymerization-control\" rel=\"noopener\">Yokogawa's "
            "ACOMP</a> polymerisation work.",
            "Control Global, R. Russell Rhinehart, <a href=\"https://www.controlglobal.com/control/"
            "multivariable-control/article/55411596/effective-process-control-matching-strategies-to-"
            "process-characteristics-and-overcoming-challenges\" rel=\"noopener\">How to fix poor "
            "control and choose the right strategy</a> (10/2026) — sửa quá trình trước, chỉ P cho quá "
            "trình tích phân, PI cho quá trình ổn định nhanh, cascade khi phép đo sơ cấp bị trễ. Loạt "
            "<a href=\"https://www.controleng.com/control-systems/pid-apc/\" rel=\"noopener\">PID "
            "Spotlight</a> của Control Engineering — phần&nbsp;10 trễ chi phối, phần&nbsp;11 tích "
            "phân, phần&nbsp;13 thời gian trễ, phần&nbsp;19 thực hành hiệu chỉnh tốt nhất, "
            "phần&nbsp;29–33 tạo dạng đáp ứng, nhiễu và điều khiển khoảng. Và Control Global về "
            "<a href=\"https://www.controlglobal.com/show-coverage/ynow-a-yokogawa-users-conference/"
            "article/55403109/yokogawa-yokogawa-closes-the-loop-on-polymerization-control\" "
            "rel=\"noopener\">ACOMP của Yokogawa</a>."))
    body += section_close()

    # 08 common thread
    body += section_open("08", "The common thread", "Sợi dây chung", pg, "thread")
    body += "<div class=\"sec-head\">"
    body += pg.h2("Same chain, different consequences", "Cùng một chuỗi, hậu quả khác nhau")
    body += pg.p(
        "Strip away the sector and every application above is the measurement-and-control loop from the "
        "Fundamentals page: a sensor turns a physical quantity into a signal, a transmitter scales it to "
        "4–20 mA or a fieldbus, a controller (PID) compares it to setpoint, and a final element (valve or "
        "drive) acts on the process — with the safety layer standing apart.",
        "Bóc tách ngành nghề, mọi ứng dụng trên đều là vòng đo lường và điều khiển ở trang Cơ bản: cảm "
        "biến biến đại lượng vật lý thành tín hiệu, bộ truyền quy đổi ra 4–20 mA hoặc fieldbus, bộ điều "
        "khiển (PID) so sánh với giá trị đặt, và phần tử cuối (van hay truyền động) tác động lên quá "
        "trình — với lớp an toàn đứng riêng.")
    body += "</div>"
    body += "<div class=\"nextprev\">"
    body += "<a href=\"control.html\"><span class=\"k\">%s</span>%s</a>" % (
        pg.span("Back", "Quay lại"), pg.span("Control", "Điều khiển"))
    body += "<a href=\"safety.html\" style=\"text-align:right\"><span class=\"k\">%s</span>%s</a>" % (
        pg.span("Next", "Tiếp"), pg.span("Safety", "An toàn"))
    body += "</div>"
    body += section_close()

    write("applications.html", render(pg, body, "applications.html"))
