# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III", section 3.3.3 continuation and the opening
of section 3.4 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 187-195, printed pp. 175-183.  Printed
equations (3.39)-(3.43) are rendered with standard notation; the garbled
relations in the decoded text (the weir and flume discharge laws) are restored from the page scans.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


def _guard_figures():
    """No-op in the integrated build.  While the parallel ipcfig3_c supplier
    is still being written, keep section() callable by supplying empty
    placeholders for figures 48-53; the real supplier always wins."""
    for _n in range(48, 54):
        _name = "fig_f%02d" % _n
        if not hasattr(F, _name):
            def _placeholder(n=_n):
                return ("", "Hình 3.%d" % n, "Figure 3.%d" % n, "", "")
            setattr(F, _name, _placeholder)


_guard_figures()


def section(lang):
    b = []

    # ------------------------------- positive displacement / oval gear
    H(b, lang,
      "(13) Đồng hồ thể tích (đồng hồ bánh răng oval)",
      "(13) Positive Displacement Meters (Oval-Gear Meter)", level=4)

    P(b, lang,
      "Đồng hồ thể tích chia dòng chảy thành các phần thể tích đã biết dựa trên "
      "hình dạng của phần tử chia. Đây là thiết bị đo cơ khí: các rôto bánh răng "
      "oval đặt ngay trên đường dòng tách chất lỏng thành từng phần nhỏ. Công "
      "suất quay rôto được lấy từ chính dòng chảy và thể hiện qua tổn thất áp "
      "suất giữa đầu vào và đầu ra. Khe hở giữa rôto và phần cố định phải nhỏ "
      "nhất có thể, trong khi đường đi của chất lỏng phải dài nhất có thể. Độ "
      "chính xác tăng dần theo kích cỡ thiết bị.",
      "Positive displacement meters split the flow passage into small packets "
      "of known volume based primarily upon the contour of the splitting "
      "element. This is essentially a mechanical type of measuring equipment. "
      "The moving parts, which are oval-shaped gear rotors, are placed just in "
      "the path of the flow stream and physically separate the flowing fluid "
      "into small increments. Drive power to move the rotor is extracted from "
      "the flow stream itself and is reflected in terms of drop in pressure "
      "between the inlet and the outlet. The clearance between the moving rotor "
      "gear and the stationary part should be minimum possible whereas the "
      "path through which the liquid passes should have maximum possible "
      "length. The accuracy of such design increases further as the size of the "
      "equipment increases.")

    P(b, lang,
      "Trong cấu tạo thực tế, hai rôto bánh răng oval được ghép với nhau để giữ "
      "vị trí tương đối cố định và quay ngược chiều nhau trong vỏ làm bằng thép "
      "đúc nặng hoặc gang đúc như Hình 3.48. Một thể tích chất lỏng cố định "
      "được dịch chuyển cho mỗi vòng quay. Cơ cấu ghi số, cũng là một hệ thống "
      "cơ khí, được nối với một trong các rôto qua bộ bánh răng riêng. Phạm vi "
      "ghi lên tới hơn 60.000 lít/phút và thiết bị có cỡ từ 50 đến 600 mm.",
      "In actual construction, two oval-geared rotors are geared together and "
      "thereby maintain a fixed position relative to each other. These two "
      "gears are allowed to rotate in opposite directions inside the housing "
      "made of heavy cast steel or cast iron as shown in Figure 3.48. A fixed "
      "volume of liquid is displaced with respect to every revolution. A "
      "registering unit, essentially a mechanical system, is connected to one "
      "of the rotor gears through another separate gear system. Registering "
      "range is available of more than 60,000 litres/minute and the instrument "
      "is available in sizes from 50 to 600 mm.")

    FIG(b, 48, F.fig_f48(), lang)

    P(b, lang,
      "Tại các nhà máy phân bón và nhà máy phát điện, người ta dùng dầu nặng có "
      "độ nhớt rất cao. Trong nhà máy phân bón, dầu được oxy hóa một phần để "
      "sản xuất hydro và carbon monoxide, tiếp tục chế biến thành amonia và "
      "urê. Trong nhà máy phát điện, dầu dùng làm nhiên liệu hỗ trợ ngọn lửa "
      "cho lò hơi. Cả hai nơi đều dùng đồng hồ bánh răng oval nêu trên. Do dầu "
      "có xu hướng đông đặc dưới 60 °C nên các hệ thống đo khác bị hỏng; vì vậy "
      "đồng hồ bánh răng oval là giải pháp hiển nhiên.",
      "In fertilizer plants as well as in power generating units, heavy oil "
      "having very high viscosity is used. In fertilizer units this oil is "
      "partially oxidised for producing hydrogen and carbon monoxide which are "
      "further processed to make ammonia and urea. In power generating units "
      "the oil is used as a flame support for boiler. In both units the fluid "
      "is metered by the oval-gear instrument described above. Due to the "
      "peculiar nature of the oil, which tends to solidify below 60 °C, other "
      "measurement systems fail and therefore the oval-gear meter is the "
      "obvious solution.")

    # --------------------------------------------- open-channel flow
    H(b, lang, "(14) Lưu lượng kế kênh hở",
      "(14) Open-Channel Flowmeter", level=4)

    P(b, lang,
      "Dòng nước tưới tiêu, dòng thải và nước thải, hay dòng nước bị hạn chế từ "
      "đập là một số ví dụ về hệ thống dòng chảy kênh hở. Phép đo dòng chảy kênh "
      "hở dùng kỹ thuật đo cột nước nhưng cấu trúc, đặc tính và cách đọc khác "
      "với các hệ thống kín.",
      "Flow of water for irrigation, flow of waste and sewage, and restricted "
      "flow of water from a dam are some examples of open-channel flow systems. "
      "Measurement of open-channel flow systems utilises head meter techniques "
      "but the structure, characteristics and readout arrangements are "
      "different.")

    P(b, lang,
      "Phần tử chính dùng cho hệ thống kênh hở là đập tràn (weir) và máng "
      "(flume). Có hai loại đập tràn: đập hình chữ V và đập hình chữ nhật, như "
      "Hình 3.49(a) và (b). Dạng kết hợp gọi là đập Cippoletti được thể hiện ở "
      "Hình 3.50; ở đây các co thắt đầu được đặt ở góc 4:1. Đập hình chữ nhật "
      "dùng cho lưu lượng lớn. Góc của đập chữ V thay đổi, các góc thiết kế "
      "thường gặp là 30°, 60° và 90°; đập chữ V dùng cho lưu lượng nhỏ.",
      "Primary elements used for open-channel flow systems are weirs and "
      "flumes. Two types of weirs are in use: V-notch and rectangular notch, as "
      "shown in Figures 3.49 (a) and (b). A combination type popularly known as "
      "cippoletti weir is shown in Figure 3.50; the end contractions have been "
      "set at a 4 : 1 angle. Rectangular weirs are used for larger flows. The "
      "angle of the V-notch varies and the most common design angles are 30°, "
      "60° and 90°; V-notch weirs are employed for lower flows.")

    FIG(b, 49, F.fig_f49(), lang)
    FIG(b, 50, F.fig_f50(), lang)

    P(b, lang,
      "Khi dùng đập tràn để đo dòng chảy kênh hở, toàn bộ hiện tượng được mô tả "
      "trong Hình 3.51. Bề mặt nước chảy qua đập gọi là Nappe có vùng chứa "
      "không khí. Đây là yêu cầu cơ bản để phép đo đạt độ chính xác; nếu thiết "
      "kế và lắp đặt không tốt thì vùng thông khí sẽ không đủ.",
      "When weirs are employed for open-channel flow measurements, the entire "
      "picture is as indicated in Figure 3.51. The profile of water over the "
      "weir, called Nappe, has an aerated area. This is the basic requirement of "
      "a weir measurement system for accuracy; if the design and installation "
      "of the weir is not perfect, the aeration area will not be sufficient.")

    FIG(b, 51, F.fig_f51(), lang)

    P(b, lang,
      "Về tính toán lưu lượng, các phương trình sau mô tả quan hệ giữa lưu lượng "
      "và cột nước đo được. Đối với đập chữ V:",
      "As far as computations of flow are concerned, the following equations "
      "govern the relationship between the flow and the measured head. For "
      "V-notch weir:")

    E(b, lang, "Q_v = 2.48 tan(0.5 α) H^(5/2)",
      "Q_v = 2.48 tan(0.5 α) H^(5/2)", num="3.39")

    P(b, lang,
      "Trong đó Q_v là lưu lượng qua đập chữ V (ft³/s), α là góc của rãnh "
      "(30°, 60° hoặc 90°) và H là cột nước đo được (feet).",
      "where Q_v is the flow rate (ft³/sec) through the V-notch, α is the angle "
      "of notch (30°, 60° or 90°) and H is the measured head (feet).")

    P(b, lang, "Tương tự, đối với đập hình chữ nhật:",
      "Similarly, for a rectangular weir:")

    E(b, lang, "Q_r = 3.33 (χ − 0.2 H) H^(3/2)",
      "Q_r = 3.33 (χ − 0.2 H) H^(3/2)", num="3.40")

    P(b, lang,
      "Trong đó Q_r là lưu lượng qua đập hình chữ nhật (ft³/s) và χ là chiều dài "
      "đỉnh đập (feet).",
      "where Q_r is the flow rate (ft³/sec) through the rectangular weir and χ "
      "is the crest length (feet).")

    P(b, lang, "Đối với đập Cippoletti:", "For a cippoletti weir:")

    E(b, lang, "Q_c = 3.367 χ H^(3/2)",
      "Q_c = 3.367 χ H^(3/2)", num="3.41")

    P(b, lang,
      "Trong đó Q_c là lưu lượng qua đập Cippoletti (ft³/s).",
      "where Q_c is the flow rate (ft³/sec) through the cippoletti weir.")

    # ----------------------------------------------------------- flumes
    H(b, lang, "Máng đo", "Flumes", level=4)

    P(b, lang,
      "Đây là dạng đặc biệt của máng venturi do Parshall thiết kế, vì vậy được "
      "gọi là máng Parshall. Hình 3.52 cho thấy máng được đặt trên mặt dòng "
      "chảy. Máng có mọi ưu điểm của phần tử đo dạng ống venturi: vận tốc cao "
      "cuốn trôi chất rắn, chất thải và các vật bị cuốn theo; máng cũng dễ chế "
      "tạo từ vật liệu sẵn có.",
      "This is a special type of venturi flume designed by Parshall and is "
      "therefore named Parshall Flume. Figure 3.52 shows it placed on the "
      "surface in the flow stream. A flume has all the advantages of a flow "
      "element that a venturi tube enjoys: the high velocity flushes the solids, "
      "wastes and other entrained materials, and it can be easily fabricated "
      "from available materials.")

    FIG(b, 52, F.fig_f52(), lang)

    P(b, lang,
      "Độ chính xác của máng đo không cao lắm (chỉ ± 2%) nhưng phép đo rất tin "
      "cậy. Đây là hệ thống đo lưu lượng lý tưởng cho nước thải và nước cống. "
      "Phương trình lưu lượng chủ yếu phụ thuộc vào bề rộng cổ hẹt L (feet) và "
      "cột nước H. Với bề rộng cổ hẹt từ 1 đến 8 feet, phương trình áp dụng là:",
      "The accuracy obtainable with flumes may not be very high (only ± 2%) but "
      "the measurement is very reliable. This is an ideal flow measurement "
      "system for waste and sewages. The equation of flow is mainly dependent "
      "upon the width of the throat L (feet) and the head H. The equation "
      "applicable for throat width 1 to 8 feet is given by:")

    E(b, lang, "Q_f = 4 L H (1.522 L)^0.026",
      "Q_f = 4 L H (1.522 L)^0.026", num="3.42")

    P(b, lang,
      "Khi bề rộng cổ hẹt lớn hơn 8 feet, phương trình thay đổi nhẹ thành:",
      "When the width of the throat is more than 8 feet the equation changes "
      "slightly and becomes:")

    E(b, lang, "Q_f = (2.5 + 3.69 L) H^1.6",
      "Q_f = (2.5 + 3.69 L) H^1.6", num="3.43")

    # ------------------------------------------------------ 3.4 opening
    H(b, lang, "3.4 Đo mức", "3.4 Measurement of Level")

    P(b, lang,
      "Mọi nhà máy chế biến đều có thùng, bình, bể và hồ chứa để cất sản phẩm "
      "hoàn chỉnh hoặc chế biến sản phẩm trung gian cho hoạt động liên tục. Vì "
      "vậy đo chính xác nội dung của các bể này rất quan trọng. Đo theo mức "
      "chất lỏng là lựa chọn hiển nhiên. Mức được định nghĩa là mặt phân cách "
      "giữa hai môi trường: một là chất lỏng cần đo, hai là không khí (bể hở) "
      "hoặc hơi của chính chất lỏng (bể kín).",
      "All processing plants have a number of drums, tanks, vessels and "
      "reservoirs to store finished products or to process intermediate "
      "products for continuous operations. Hence accurate measurement of the "
      "contents of these vessels is very important and critical. Measurement of "
      "content in terms of level is the obvious choice. Level can be defined as "
      "the interface existing between two media: one is the liquid proper whose "
      "level is to be measured and the other is air when the tank is open, or "
      "the vapour of the liquid itself when the tank is closed.")

    P(b, lang,
      "Phương pháp phổ biến nhất là kính nhìn mức (sight glass/gage glass), "
      "hoạt động theo nguyên lý ống chữ U. Hình 3.53(a) và (b) cho thấy kính "
      "dùng cho bể hở và bể kín, chịu áp. Khi mức trong bể thay đổi, mức trong "
      "ống trong suốt cũng thay đổi và được đọc trên thang chỉ thị. Van cô lập "
      "được bố trí để bảo trì kính đo.",
      "The most common industrial method is the sight glass/gage glass, which "
      "works on the principle of the U-tube manometer. Figures 3.53 (a) and (b) "
      "show the glass for open tanks as well as for closed, pressurised tanks. "
      "As the level in the process vessel changes, the level in the transparent "
      "tube also changes and is read on the indicator scale. Isolation valves "
      "are provided for carrying out maintenance work on the sight glass "
      "indicator.")

    FIG(b, 53, F.fig_f53(), lang)

    return b
