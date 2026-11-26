# -*- coding: utf-8 -*-
"""Chapter 7, section d (PDF pp. 342-347; printed pp. 330-335).

LED construction and symbol, seven-segment / dot-matrix / bar-graph LED
displays, LED advantages and disadvantages, liquid-crystal structures,
7.3.2 dynamic-scattering LCD and the start of 7.3.3 field-effect LCD.
Figures 7.17 - 7.27 are embedded in source order.
"""
import ipcfig7 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS

# The three figure suppliers may not have landed yet. Install *non-overwriting*
# fallbacks so section() can be compiled and QA-checked in isolation; a real
# supplier callable always wins because these are only set when absent.
_STUB_CAPTIONS = {
    17: ("Hình 7.17 · Cấu trúc LED: lớp P, lớp N, ánh sáng phát ra, "
         "cực dương và cực âm",
         "Figure 7.17 · LED construction: P and N layers, emitted light, "
         "anode and cathode"),
    18: ("Hình 7.18 · LED phủ lớp phốt pho và ký hiệu biểu diễn (a, b)",
         "Figure 7.18 · Phosphor-coated LED construction and its "
         "representative symbol (a, b)"),
    19: ("Hình 7.19 · Màn hình LED bảy đoạn với các đoạn a đến g",
         "Figure 7.19 · Seven-segment LED display with segments a to g"),
    20: ("Hình 7.20 · Ma trận điểm LED với các dây X và Y",
         "Figure 7.20 · LED dot matrix with X and Y wires"),
    21: ("Hình 7.21 · Các điểm LED sáng để hiển thị chữ số 4",
         "Figure 7.21 · Illuminated LED dots for displaying digit 4"),
    22: ("Hình 7.22 · Biểu đồ cột mười LED từ 0 đến 10",
         "Figure 7.22 · Ten-LED bar graph from 0 to 10"),
    23: ("Hình 7.23 · Cấu trúc tinh thể lỏng smectic",
         "Figure 7.23 · Smectic liquid crystal structure"),
    24: ("Hình 7.24 · Cấu trúc tinh thể lỏng nematic",
         "Figure 7.24 · Nematic liquid crystal structure"),
    25: ("Hình 7.25 · Cấu trúc tinh thể lỏng cholesteric",
         "Figure 7.25 · Cholesteric liquid crystal structure"),
    26: ("Hình 7.26 · Tinh thể lỏng khi chưa có điện áp",
         "Figure 7.26 · Liquid crystal cell with no voltage applied"),
    27: ("Hình 7.27 · Tinh thể lỏng khi có điện áp, trạng thái mờ đục",
         "Figure 7.27 · Liquid crystal cell with voltage applied, "
         "opaque state"),
}


def _make_stub(n, cvi, cen):
    def _fig_stub():
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" '
               'height="250" viewBox="0 0 680 250" role="img"></svg>')
        return (svg, cvi, cen, "", "")
    return _fig_stub


for _n, _caps in _STUB_CAPTIONS.items():
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, _make_stub(_n, _caps[0], _caps[1]))


def section(lang):
    b = []

    P(b, lang,
      "Trong quá trình chế tạo LED, lớp bán dẫn loại N thực chất được mọc trên "
      "đế. Ở chiều ngược lại, lớp loại P được lắng đọng lên lớp loại N bằng "
      "phương pháp khuếch tán. Tiếp điểm kim loại ở cực dương chỉ được chế tạo "
      "trên một vùng nhỏ, nhờ đó nhiều ánh sáng thoát ra khỏi bề mặt hơn. "
      "Ngược lại, một cực âm lớn làm bằng màng vàng, được ưu tiên sử dụng, có "
      "khả năng cung cấp diện tích phản xạ lớn nhất. Toàn bộ cụm linh kiện được đặt "
      "trong vỏ bọc để bảo vệ. Kiểu thiết kế này được trình bày trong Hình 7.17.",
      "During manufacturing of LED, the N-type layer is in fact grown upon the "
      "substrate. On the other hand, the P-type layer is deposited upon the "
      "N-type layer by diffusion method. The metallic connection on the anode "
      "is made on small region. This allows more light to escape out of the "
      "surface. In contrast a large cathode made of preferably gold film is "
      "capable of providing maximum possible reflecting area. The complete unit "
      "is sealed in an enclosure for protection. This type of design has been "
      "shown in Figure 7.17.")
    FIG(b, 17, F.fig_f17(), lang)

    P(b, lang,
      "Một cấu trúc điển hình khác được trình bày trong Hình 7.18(a), trong đó "
      "lớp phốt pho được dùng làm lớp phủ trên bề mặt LED để tăng độ rõ của "
      "ánh sáng. Hình 7.18(a) cho thấy cấu trúc bên trong của loại LED này, còn "
      "ký hiệu biểu diễn của nó được cho trong Hình 7.18(b).",
      "Another typical construction has been shown in Figure 7.18(a) in which "
      "phosphor layer is used as coating on the LED surface to increase the "
      "visibility. Figure 7.18(a) shows the internal construction of such LED "
      "and its representative symbol is on figure 7.18(b).")
    FIG(b, 18, F.fig_f18(), lang)

    P(b, lang,
      "Hệ thống hiển thị dựa trên LED phổ biến nhất là màn hình bảy đoạn. Lý do "
      "là cần ít nhất bảy LED để biểu diễn đầy đủ mọi chữ số từ 0 đến 9. Các "
      "LED này được đánh số là a, b, c, d, e, f và g như trong Hình 7.19.",
      "The most popular LED based display system is the seven-segment display "
      "system. This is because minimum seven LEDs are required to cover all the "
      "digits from 0 to 9. These are numbered as a, b, c, d, e, f and g as shown "
      "in Figure 7.19.")
    FIG(b, 19, F.fig_f19(), lang)

    P(b, lang,
      "Sơ đồ cho thấy cấu trúc đầy đủ của cụm hiển thị bảy đoạn theo kiểu cực "
      "dương chung. Bảy công tắc được nối qua các điện trở sẽ tạo ra những chữ "
      "số khác nhau bằng cách đóng lại theo chữ số đầu vào. Ví dụ, để biểu diễn "
      "0, tất cả công tắc phải đóng trừ đoạn g; còn để biểu diễn 9, tất cả công "
      "tắc phải đóng trừ đoạn e. Các chữ số khác tuân theo quy luật tương tự. "
      "Cấu hình trên cũng có thể đổi sang kiểu cực âm chung.",
      "The diagram shows complete scheme of seven-segment display unit in "
      "common anode configuration style. The seven number of switches connected "
      "through resistors create different digits by closing themselves according "
      "to the input digits. For example, to indicate 0, all switches should close "
      "except g and to indicate 9 all switches should close except, e. Other "
      "digits follows similar pattern. The above configuration can be changed to "
      "common cathode configuration also.")

    P(b, lang,
      "Một loại màn hình hiển thị dữ liệu số khác dựa trên LED được gọi là màn "
      "hình ma trận điểm. Nhiều điểm được sắp xếp theo dạng ma trận và mỗi điểm "
      "được nối với một LED. Như vậy mỗi điểm đại diện cho một LED dùng để thắp "
      "sáng chính điểm đó. Cách sắp xếp ma trận điểm dạng này có thể có nhiều tổ "
      "hợp, ví dụ 5 và 7, 5 và 8, hoặc 7 và 9. Tổ hợp ma trận 5 và 7 điểm với "
      "LED lắp trên từng điểm được trình bày trong Hình 7.20. Việc nối điện cho "
      "cấu trúc này có thể thực hiện theo ba cách:",
      "Another digital data display based on LEDs is called Dot Matrix Displays. "
      "Several dots are arranged in a matrix format and a LED is connected on "
      "every dot. This means every dot represents one LED for lighting that "
      "particular dot. The matrix arrangement of dots of this kind can be of "
      "several combination, e.g. 5 and 7 or 5 and 8 or 7 and 9. A combination of "
      "5 and 7 dot matrix with LED installed on each dot has been shown in Figure "
      "7.20. Electrical connection to this arrangement can be done in three "
      "different ways:")
    FIG(b, 20, F.fig_f20(), lang)

    L(b, lang,
      ["(a) Nối cực âm chung,",
       "(b) Nối cực dương chung, và",
       "(c) Nối mảng XY."],
      ["(a) Common cathode connection,",
       "(b) Common anode connection, and",
       "(c) XY array connection."])

    P(b, lang,
      "Cách nối mảng XY vì kinh tế và phổ biến hơn đã được dùng trong sơ đồ trên "
      "hình. Để hiển thị số 4, những LED cần ở trạng thái SÁNG đã được chỉ ra "
      "trong Hình 7.21.",
      "The XY array connection being economical and more popular has been used "
      "in the diagram in figure. For displaying 4 the LEDs which are required to "
      "be in ON state has been shown in Figure 7.21.")
    FIG(b, 21, F.fig_f21(), lang)

    P(b, lang,
      "Cách nối cực dương chung hoặc cực âm chung cho màn hình ma trận điểm "
      "không kinh tế, vì số dây dẫn tăng lên rất nhiều và các mối nối trở nên "
      "phức tạp.",
      "The common anode or cathode connection for dot matrix display is not "
      "economical because number of wires are tremendously increased and "
      "connections become complicated.")

    P(b, lang,
      "Loại màn hình thứ ba làm từ LED được gọi là màn hình biểu đồ cột. Đây "
      "thực chất là một màn hình số, nhưng được dùng trên các bộ điều khiển công "
      "nghiệp để biểu thị giá trị của quá trình và giá trị cài đặt. Trong loại "
      "này, các LED được bật sáng lần lượt từ 0 đến 10 để biểu diễn giá trị dưới "
      "dạng cột như trong Hình 7.22. LED dùng ở đây có dạng điểm và rất nhỏ (LED "
      "thu nhỏ). Những LED này được điều khiển độc lập và xếp thẳng hàng, sát "
      "nhau để biểu diễn giá trị theo chiều dọc hoặc chiều ngang. Thường thì "
      "tín hiệu tương tự được dùng để biểu diễn giá trị trong hệ thống hiển thị "
      "này.",
      "A third type of display can be made out of LEDs called Bar Graph Displays "
      "which is exactly a digital display, but are used on process controllers "
      "for indication of process values and set values. In this, LEDs are allowed "
      "to be ON one-by-one starting from 0 upto 10 for indicating the values in "
      "bar graph shape as shown in Figure 7.22. The LEDs used in this are of dot "
      "shape and are very small (miniature LEDs). These LEDs are independently "
      "driven and are arranged linearly and closely for indicating the values in "
      "vertical way or horizontal way. For indicating the values in this display "
      "system analog signal is normally employed.")
    FIG(b, 22, F.fig_f22(), lang)

    H(b, lang, "Ưu điểm của LED", "Advantages of LED", level=4)
    L(b, lang,
      ["(i) LED có kích thước rất nhỏ, do đó rất hữu ích trong việc chế tạo các "
       "thiết bị thu nhỏ.",
       "(ii) Vì là thiết bị hoạt động ở điện áp thấp (đến 2 volt) và dòng điện "
       "nhỏ (đến 20 mA), đầu ra ánh sáng có thể được điều khiển rất hiệu quả "
       "bằng cách điều chỉnh dòng điện.",
       "(iii) LED là thiết bị hoạt động nhanh so với các thiết bị chỉ thị khác. "
       "Nó hoạt động trong vòng một nano giây.",
       "(iv) Ánh sáng màu do LED phát ra có kết cấu bền chắc và có tuổi thọ rất "
       "dài nếu vận hành đúng quy chuẩn.",
       "(v) Nhiệt độ hoạt động của LED nằm trong khoảng từ 0 đến 70 °C."],
      ["(i) It is very small in size, therefore, very useful in fabrication of "
       "miniature instrument.",
       "(ii) Since it is a low voltage (upto 2 volt) and low current (upto 20 "
       "millampere) operated device, the light output can be very effectively "
       "controlled by controlling the current.",
       "(iii) LED is a fast operating device in comparison to other indicating "
       "device. It operates within a nanosecond.",
       "(iv) LED produced coloured light is rugged in constructional feature and "
       "have very long life if operated within norms.",
       "(v) Its operating temperature ranges from 0 to 70C."])

    H(b, lang, "Nhược điểm", "Disadvantages", level=4)
    L(b, lang,
      ["(i) LED rất nhạy với quá điện áp, quá dòng và nhiệt độ cao.",
       "(ii) Trong ánh sáng môi trường mạnh, LED trở nên không nhìn thấy được."],
      ["(i) LED is very sensitive to over-voltage, over-current and higher "
       "temperature.",
       "(ii) In strong ambient light, LED becomes invisible."])

    H(b, lang, "(ii) Màn hình dựa trên tinh thể lỏng (LCD)",
      "(ii) LCD-based display", level=3)

    P(b, lang,
      "Tinh thể lỏng là một vật liệu đặc biệt, vừa có cấu trúc tinh thể như chất "
      "rắn, vừa có đặc tính chảy như chất lỏng. Chúng không phát sáng như LED mà "
      "điều chế ánh sáng khi có tín hiệu dạng điện tác động lên. Những tinh thể "
      "lỏng này được tạo thành từ các phân tử hữu cơ có hình elip với trục ngắn "
      "tương đối nhỏ, như trong Hình 7.23.",
      "Liquid crystal is a peculiar material having crystalline structure like "
      "solids and at the same time having characteristics of fluidity like a "
      "liquid. They do not emit light like LED but modulate the light when signal "
      "in electrical form is applied to them. These liquid crystals are made of "
      "organic molecules having elliptical shape of comparatively smaller minor "
      "axis as shown in Figure 7.23.")

    P(b, lang,
      "Cách sắp xếp phân tử của tinh thể lỏng tạo ra ba loại tinh thể khác nhau. "
      "Trong ba loại đó chỉ có hai loại hữu ích cho việc chế tạo hệ thống hiển "
      "thị. Cấu trúc tinh thể SMECTIC được xếp thành các lớp có hệ thống nhưng "
      "không dùng được cho hệ thống hiển thị. Hai loại còn lại, tức là cấu trúc "
      "NEMATIC và CHOLESTERIC, dù không được xếp lớp có hệ thống vẫn hữu ích cho "
      "hệ thống hiển thị.",
      "The molecular arrangement of the liquid crystal, define three different "
      "types of these crystals. Out of these three only two are useful for "
      "fabricating the display system. The SMECTIC crystal structure is "
      "systematically layered to one another but is of no use for display "
      "system. The other two, i.e. NEMATIC and the CHOLESTERIC structures though "
      "are not layered systematically but are useful for display system.")
    FIG(b, 23, F.fig_f23(), lang)
    FIG(b, 24, F.fig_f24(), lang)
    FIG(b, 25, F.fig_f25(), lang)

    P(b, lang,
      "Tinh thể lỏng nematic được dùng phổ biến hơn trong chế tạo thiết bị hiển "
      "thị. Thông thường tinh thể này trong suốt, nhưng khi có điện trường tác "
      "động, cấu trúc tinh thể bị xáo trộn và tinh thể trở nên mờ đục. Màn hình "
      "tinh thể lỏng có hai loại: loại tán xạ động và loại hiệu ứng trường.",
      "Nematic liquid crystal is more popular in fabricating display devices. "
      "Normally this crystal is transparent but when electric field is applied, "
      "the crystal structures get disturbed and the crystal become opaque. Liquid "
      "crystal displays are of two types, one is dynamic scattering type and "
      "another is field effect type.")

    H(b, lang, "7.3.2 LCD dạng tán xạ động",
      "7.3.2 Dynamic Scattering Type LCD", level=3)

    P(b, lang,
      "Tinh thể lỏng nematic là loại được biết đến phổ biến nhất trong LCD dạng "
      "tán xạ động. Trong loại này, một lớp mỏng của tinh thể, thường chỉ vài "
      "micron, được đặt giữa hai tấm kính. Một tấm kính trong suốt, tấm kia có "
      "khả năng phản xạ như một gương phẳng. Hai tấm kính được trang bị các điện "
      "cực cần thiết để nối điện. Lớp dẫn điện được làm bằng lớp phủ oxit thiếc. "
      "Bề mặt chỉ thị có lớp oxit được khắc để tạo thành các chữ số cách ly điện "
      "với nhau. Hình 7.26 cho thấy tinh thể khi chưa có điện áp. Trong trạng "
      "thái này, ánh sáng đi xuyên hoàn toàn qua hệ thống và hệ thống hoạt động "
      "như một vật trong suốt như đã chỉ ra.",
      "The nematic liquid crystal is the most popularly known dynamic scattering "
      "type LCD. In this a thin layer usually of a few microns of the crystal is "
      "placed between the two glass plates. One glass is transparent and the "
      "other one is reflective like a plane mirror. The glass plates are equipped "
      "with required electrodes for electrical connections. The conducting layer "
      "is made of tin oxide coating. The indicating surface with oxide coating is "
      "etched to produce pattern of digits which are effectively insulated to "
      "each other. Figure 7.26 shows the crystal when no voltage is applied. In "
      "this condition, the light passes completely through the system and behaves "
      "as transparent object as indicated.")
    FIG(b, 26, F.fig_f26(), lang)

    P(b, lang,
      "Khi một điện áp (từ 6 đến 20 volt) được đặt lên lớp oxit kim loại như "
      "trong Hình 7.27, cấu trúc bình thường của tinh thể bị xáo trộn. Lý do là "
      "các vùng mới có chiết suất thay đổi được hình thành giữa các bề mặt dẫn "
      "điện của hệ thống. Ánh sáng thông thường sau khi chiếu tới bề mặt sẽ bị "
      "tán xạ theo các hướng khác nhau tại giao diện giữa các vùng có chiết suất "
      "khác nhau. Sự tán xạ ánh sáng theo cách này được gọi là tán xạ động.",
      "When a voltage (between 6 and 20 volt) is applied across the metal oxide "
      "coating as shown in Figure 7.27, the usual structure of the crystal get "
      "disturbed. Because new areas are formed having varying refractive index in "
      "between the conducting surfaces of the system. The normal light after "
      "being incident upon the surface is scattered in different directions at "
      "the interface between the areas of varying refractive index. Scattering of "
      "light in this way is called dynamic scattering.")
    FIG(b, 27, F.fig_f27(), lang)

    H(b, lang, "7.3.3 LCD dạng hiệu ứng trường",
      "7.3.3 Field Effect Type LCD", level=3)

    P(b, lang,
      "Trong LCD dạng hiệu ứng trường, người ta dùng thêm một linh kiện gọi là "
      "bộ cực hóa ánh sáng. Các bộ cực hóa làm bằng loại kính đặc biệt được đặt "
      "trên bề mặt của hai tấm kính song song, giữa đó đặt tinh thể lỏng loại "
      "nematic xoắn. Hai tấm kính song song này được cố định với lớp làm kín phù "
      "hợp ở giữa. Các dẫn điện trong suốt được đặt ngay bên dưới hai tấm kính "
      "song song. Hai bộ cực hóa ánh sáng được đặt lệch nhau 90°. Khi các dẫn "
      "điện trong suốt không được cấp điện áp, tức là trong trạng thái điện áp "
      "bằng không, tinh thể lỏng nematic xoắn xoay hoàn toàn ánh sáng đi qua hệ "
      "thống và các bộ cực hóa cho toàn bộ ánh sáng đi xuyên qua. Trong trạng "
      "thái này, hệ thống cho thấy một mô hình tối trên toàn bộ bề mặt thiết bị "
      "hiển thị.",
      "In field effect type of LCD, an additional component called light "
      "polarizer is used. The polarizers made of typical glass are placed on the "
      "surface of the parallel glass plates in between which the liquid crystal "
      "of twisted nematic type are placed. These parallel glass plates are fixed "
      "with proper sealing in between them. The transparent conductors are placed "
      "just below the two parallel glass plates. The light polarizers are placed "
      "90 out of position to each other. When the transparent conductors are not "
      "energized by the applied voltage that means in the condition of zero "
      "voltage the twisted nematic type liquid crystal completely twists the "
      "light passing through the system and the polarizers allow all the light to "
      "cross through. In this condition, the system shows dark pattern across the "
      "entire display device.")

    P(b, lang,
      "Ở chiều ngược lại, khi điện áp giữa 2 và 8 được đặt lên các dẫn điện, cấu "
      "trúc tinh thể tự sắp xếp lại với nhau theo điện trường. Ánh sáng phân cực "
      "thu được làm các chữ số hiện ra trên nền.",
      "On the other hand, when the voltage between 2 and 8 is applied across the "
      "conductors, the crystal structures align amongst themselves with respect "
      "to the electric field. The resulting polarized light causes the digits to "
      "appear on the background.")

    return b
