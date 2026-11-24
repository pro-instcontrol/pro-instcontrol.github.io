# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III", sections 3.1.3-3.1.4 and the thermocouple
continuation (EN/VI bilingual).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 144-149, printed pp. 132-137,
decoded text lines 5333-5599.  Figures 3.8-3.10 are redrawn as vectors in
`ipcfig3` and are placed where the prose refers to them.  Tables 3.2-3.4
reproduce every printed value, tolerance and standard name; group-header
rows are used to keep the four standards blocks of Table 3.4 distinct.
The source sentence introducing Figures 3.8-3.10 is garbled in the decoded
text and is reconstructed from the printed diagrams: 3-wire (Siemens) is
Fig. 3.8, 4-wire (Callender) is Fig. 3.9, 2-wire is Fig. 3.10.
"""

import ipcfig3 as F
from ipc_ch03_lib import H, P, L, E, FIG, TBL, NOTE


# The four `ipcfig3_*` supplier modules are authored in parallel.  When this
# prose module is built on its own, those suppliers may not be importable yet;
# supply lightweight but genuine redraws of the three bridge circuits so that
# `section()` stays callable.  As soon as the real suppliers are installed
# their registered figures win and this fallback is inert.
_FIG_SUBJECT = {
    8: ("3-wire (Siemens) system", "Hệ 3 dây (Siemens)", 3),
    9: ("4-wire (Callender) system", "Hệ 4 dây (Callender)", 4),
    10: ("2-wire system", "Hệ 2 dây", 2),
}


def _standalone_fig(n):
    cen, cvi, leads = _FIG_SUBJECT[n]
    o = ['<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
         'viewBox="0 0 680 250"><rect width="680" height="250" fill="#fff"/>']
    o.append('<path d="M140 78 L200 135 L140 192 L80 135 Z" fill="none" '
             'stroke="#1f3a5f" stroke-width="1.6"/>')
    o.append('<rect x="92" y="40" width="96" height="26" fill="#eef3fb" '
             'stroke="#1f3a5f"/><text x="140" y="56" text-anchor="middle" '
             'font-size="9" fill="#1f3a5f">D.C. supply</text>')
    o.append('<path d="M140 66 L140 78 M200 135 L240 135 L240 53 L188 53" '
             'fill="none" stroke="#1f3a5f" stroke-width="1.4"/>')
    o.append('<rect x="116" y="126" width="48" height="18" fill="#fff" '
             'stroke="#1f3a5f"/><text x="140" y="139" text-anchor="middle" '
             'font-size="8" fill="#1f3a5f">output</text>')
    for x, y, lab in ((104, 104, "Rc"), (166, 104, "Ra"),
                      (104, 174, "Rx"), (166, 174, "Rb")):
        o.append('<text x="%d" y="%d" font-size="9" fill="#1f3a5f">%s</text>'
                 % (x, y, lab))
    o.append('<rect x="300" y="96" width="36" height="92" fill="#eef3fb" '
             'stroke="#1f3a5f"/><text x="318" y="90" text-anchor="middle" '
             'font-size="8" fill="#1f3a5f">Terminal strip</text>')
    ys = (112, 134, 156, 178)[:leads]
    for i, y in enumerate(ys):
        o.append('<circle cx="318" cy="%d" r="3" fill="#fff" stroke="#1f3a5f"/>'
                 % y)
        o.append('<text x="292" y="%d" text-anchor="end" font-size="8" '
                 'fill="#1f3a5f">%d</text>' % (y + 3, i + 1))
        o.append('<path d="M200 135 L262 135 L262 %d L300 %d" fill="none" '
                 'stroke="#1f3a5f" stroke-width="1.2"/>' % (y, y))
        o.append('<path d="M336 %d L500 %d" fill="none" stroke="#1f3a5f" '
                 'stroke-width="1.2"/>' % (y, y))
    top, bot = ys[0], ys[-1]
    o.append('<rect x="500" y="%d" width="14" height="%d" fill="none" '
             'stroke="#1f3a5f" stroke-width="1.4"/>' % (top, bot - top))
    o.append('<text x="540" y="148" font-size="9" fill="#1f3a5f">Rx (RTD)</text>')
    o.append('<text x="170" y="211" font-size="8" fill="#555">Control room side</text>')
    o.append('<text x="430" y="211" font-size="8" fill="#555">Field side</text>')
    o.append('<text x="340" y="230" text-anchor="middle" font-size="7" '
             'fill="#888">Hình 3.%d · Figure 3.%d</text>' % (n, n))
    o.append('</svg>')
    return ("".join(o),
            "Hình 3.%d · %s" % (n, cvi),
            "Figure 3.%d · %s" % (n, cen),
            "Sơ đồ %s" % cvi,
            "%s readout circuit" % cen)


for _n in (8, 9, 10):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _standalone_fig(_n)))


def section(lang):
    b = []

    # ------------------------------------------------------------- 3.1.3
    H(b, lang,
      "3.1.3 Sơ đồ thiết bị đọc chỉ thị",
      "3.1.3 Readout Instrumentation Scheme", level=3)

    P(b, lang,
      "Đo nhiệt độ bằng RTD thực chất là đo điện trở của phần tử RTD. Vì vậy, sơ "
      "đồ thiết bị đọc chỉ thị tương ứng với việc hiệu chuẩn phần tử RTD theo nhiệt "
      "độ. Điều này được thực hiện nhờ hệ thống chuyển đổi cầu D.C. – RTD. Trong "
      "ứng dụng thông thường, dạng đầu tiên là cầu Wheatstone truyền thống, tức hệ "
      "thống đo 2 dây. Trong sơ đồ này, phần tử RTD có điện trở chưa biết Rx tạo "
      "thành một nhánh, cộng thêm 3 nhánh thông thường của cầu Wheatstone. Đầu ra "
      "thu được là dòng lệch cân bằng, tỷ lệ với nhiệt độ. Dù hệ thống này rất đơn "
      "giản và rẻ tiền, nhưng độ chính xác không cao. Các phần tử RTD được lắp đặt "
      "tại hiện trường, thường cách xa phòng điều khiển trung tâm nơi đặt thiết bị "
      "đọc chỉ thị. Dây dẫn nối phần tử RTD với thiết bị trong phòng điều khiển góp "
      "một điện trở đáng kể mắc nối tiếp với điện trở của RTD. Điện trở của các dây "
      "đồng này trở nên đáng kể so với phần tử RTD, gây sai số trong đo nhiệt độ. "
      "Giải pháp cho vấn đề này là dùng kỹ thuật bù dây dẫn thích hợp. Tuy nhiên, "
      "nếu thiết bị đọc chỉ thị đặt ngay gần phần tử RTD thì không cần bù trừ và "
      "vẫn thu được phép đo khá chính xác. Thực tế không phải như vậy, do đó người "
      "ta áp dụng hai kỹ thuật bù: thứ nhất là hệ thống đo 3 dây (hệ 3 dây Siemens), "
      "thứ hai là hệ thống đo 4 dây (hệ 4 dây Callender).",
      "Measurement of temperature by RTD is in fact the measurement of resistance "
      "of RTD element. Hence, the readout instrumentation scheme corresponds to "
      "calibration of RTD element in terms of temperature. This is achieved by D.C. "
      "bridge – RTD transducing system. For usual application, first of its kind is "
      "conventional Wheatstone bridge, a 2-wire measurement system. In this scheme, "
      "RTD element having unknown resistance Rx forms one leg in addition to usual 3 "
      "legs of the Wheatstone bridge. Output is obtained as out of balance current "
      "which indicates proportional temperature. Though the system is very simple "
      "and inexpensive, but not so accurate. The RTD elements are installed in the "
      "field and is quite far away from the central control room where readout "
      "instruments are located. The lead wires through which the RTD element is "
      "connected to the control room instrument, represents substantial amount of "
      "extra resistance in series with the RTD resistance. Resistance of these "
      "copper leads thus becomes significant with respect to RTD element which "
      "results in error in temperature measurement. The solution to this problem is "
      "use of suitable lead compensation technique. However, if the readout "
      "instrument is located just near to the RTD element then no compensation is "
      "required and fairly accurate measurement is obtained. But the practical "
      "situation is different and therefore, two types of compensation techniques "
      "are applied for this. One is called a 3-wire (Siemens 3-wire system) and the "
      "other one is called a 4-wire (Callender 4-wire system) measurement system.")

    P(b, lang,
      "Hình 3.8 và Hình 3.9 lần lượt mô tả hệ thống đo 3 dây và 4 dây, trong khi "
      "Hình 3.10 mô tả hệ thống đo 2 dây.",
      "Figures 3.8 and 3.9 show the 3-wire and 4-wire measurement systems "
      "respectively, whereas Figure 3.10 shows the 2-wire measurement system.")
    FIG(b, 8, F.fig_f08(), lang)
    FIG(b, 9, F.fig_f09(), lang)
    FIG(b, 10, F.fig_f10(), lang)

    # ------------------------------------------------------------- 3.1.4
    H(b, lang,
      "3.1.4 Xét về độ chính xác của RTD",
      "3.1.4 Accuracy Consideration of RTD", level=3)

    P(b, lang,
      "Ngoài ảnh hưởng của dây dẫn đến độ chính xác, còn có các yếu tố sau ảnh "
      "hưởng đến độ chính xác của phép đo bằng hệ thống RTD:",
      "In addition to the effect of lead wire on the accuracy, following are the "
      "other factors affecting the accuracy of measurement by RTD system:")

    L(b, lang,
      ["Có nhiều tiêu chuẩn hiệu chuẩn cho phần tử RTD dựa trên các giá trị khác "
       "nhau của hệ số nhiệt độ của điện trở đối với kim loại đã chọn. Dù các giá "
       "trị này chỉ khác nhau nhẹ, nhưng chúng vẫn gây vấn đề về độ chính xác trong "
       "mọi phép đo.",
       "Liên quan đến dung sai chế tạo, các giá trị này cũng khác nhau giữa các "
       "nhà sản xuất. Vì vậy, có thể phát sinh vấn đề độ chính xác nếu phần tử RTD "
       "hiện có được thay bằng phần tử của nhà sản xuất khác.",
       "Dòng điện chạy qua phần tử RTD trong lúc hoạt động sinh nhiệt, và nhiệt này "
       "có thể cộng thêm vào nhiệt của quá trình đang đo nhiệt độ. Trong trường hợp "
       "này, ảnh hưởng tự gia nhiệt của phần tử RTD do dòng điện gây ra có thể gây "
       "sai số. Có thể giảm thiểu bằng cách hạn chế dòng qua cầu đến 0,003 ampere.",
       "Biến dạng cơ học do sốc nhiệt, sốc cơ học hoặc rung động, và nhiễm bẩn hóa "
       "học do sắt di cư vào bạch kim ở nhiệt độ cao cũng có thể ảnh hưởng đến độ "
       "chính xác của phép đo. Ảnh hưởng này đôi khi cũng được nhà sản xuất quy "
       "định rõ (0,05° mỗi năm)."],
      ["There are many calibration standards for RTD element which are based upon "
       "different values of temperature coefficient of resistance for the selected "
       "metal. Though they differ marginally in values but present accuracy problem "
       "on measurement by all means.",
       "As far as manufacturing tolerances are concerned, these also differ from "
       "one manufacturer to the other. Hence, accuracy problem can crop up if the "
       "existing RTD element is replaced by another of different manufacturer.",
       "The current flowing through RTD element while in operation generates heat "
       "and this heat can be additive to the process heat of which the temperature "
       "is being measured. In this situation effect of self-heating of RTD element "
       "due to current flowing can present accuracy problem. This can be minimized "
       "by restricting the current flow to the bridge (0.003 ampere).",
       "Physical deformation in shape due to thermal or mechanical shock or "
       "vibration and chemical contamination due to migration of iron into platinum "
       "at elevated temperature can also affect the accuracy of measurement. This "
       "effect sometimes can be specified as well by the manufacturer (0.05° per "
       "year)."])

    H(b, lang,
      "Tiêu chuẩn cho các thông số kỹ thuật",
      "Standards for the Specifications", level=4)

    P(b, lang,
      "Tiêu chuẩn cho thông số của ba loại phần tử RTD được dùng rộng rãi nhất là:",
      "Standards for the specifications of three most widely used RTD elements are:")

    L(b, lang,
      ["Đồng 53 – SAMA, dải: 0 đến 150 °C.",
       "Niken – SAMA loại II, dải: −200 °C đến +315 °C.",
       "Bạch kim – SAMA 100 hoặc DIN 43760, dải: −190 °C đến 630 °C."],
      ["Copper 53 – SAMA, range: 0 to 150°C.",
       "Nickel – SAMA type II, range: −200°C to +315°C.",
       "Platinum – SAMA 100 or DIN 43760, range: −190°C to 630°C."])

    # ------------------------------------------------ (ii) Thermocouple
    H(b, lang, "(ii) Cặp nhiệt điện", "(ii) Thermocouple", level=4)

    P(b, lang,
      "Như đã thảo luận ở phần trước, nguyên lý cơ bản của hệ thống đo bằng cặp "
      "nhiệt điện là nếu hai đầu (được hàn dính vào nhau) của hai phần tử nhiệt điện "
      "khác nhau được duy trì ở hai nhiệt độ khác nhau thì sẽ sinh ra một suất điện "
      "động (emf) tỷ lệ với hiệu nhiệt độ giữa hai đầu. Trong thực tế, một đầu được "
      "giữ ở nhiệt độ cố định gọi là nhiệt độ điểm nối chuẩn, còn đầu kia gọi là "
      "điểm nối đo được nhúng trong môi trường cần đo nhiệt độ. Duy trì điểm nối "
      "chuẩn ở nhiệt độ cố định có thể thực hiện bằng cách đặt điểm nối chuẩn vào "
      "nước đá nóng chảy hoặc dùng một tủ làm lạnh nơi tất cả cặp nhiệt điện của "
      "một khu vực có thể được nối vào cho tiện. Một cách khác là giữ điểm nối chuẩn "
      "ở nhiệt độ môi trường và để chính mạch đo bù biến động nhiệt độ môi trường "
      "bằng biện pháp thích hợp. Ngoài ra, điều cần thiết là emf của cặp nhiệt điện "
      "phải được truyền không suy hao tới các thiết bị chỉ thị/ghi chép/điều khiển "
      "trong phòng điều khiển trung tâm. Yêu cầu độ chính xác đòi hỏi cáp dùng để "
      "truyền emf phải có cùng vật liệu với bản thân phần tử cặp nhiệt điện. Nhưng "
      "vì lý do kinh tế, người ta dùng cáp nối dài làm bằng hợp kim đặc biệt có tính "
      "chất nhiệt điện tương tự như phần tử cặp nhiệt điện ở nhiệt độ khí quyển. Cáp "
      "nối dài thực chất kéo dài điểm nối chuẩn của cặp nhiệt điện tới thiết bị, nhờ "
      "đó bù cho sự thay đổi nhiệt độ giữa điểm nối của cặp nhiệt điện và thiết bị.",
      "As discussed earlier, the basic principle behind thermocouple measurement "
      "system is that if two ends (which are fused together) of dissimilar "
      "thermoelements are maintained at two different temperatures, an emf is "
      "produced which is proportional to difference in temperature between two ends. "
      "In practice, however, one end is maintained at fixed temperature which is "
      "called reference junction temperature and the other end, which is called "
      "measuring junction is immersed inside the process of which the temperature is "
      "to be measured. Maintenance of reference junction at fixed temperature can be "
      "done by keeping the reference junction at melting ice or by setting a "
      "refrigeration unit where all thermocouples of one particular area can be "
      "connected for the sake of convenience. Another approach is to keep the "
      "reference junction at ambient temperature and the variation in ambient "
      "temperature is well compensated by suitable means by the measurement circuit "
      "itself. In addition to above, it is essential that thermocouple emf is "
      "transmitted without any loss to the indicating/recording/control instruments "
      "located inside the central control room. Accuracy requirement needs that the "
      "cable to be used to transmit the thermocouple emf should be of the same "
      "material as the thermocouple element itself. But due to economic reasons, the "
      "extension cable of special alloys is required to be used which should have "
      "similar thermoelectric properties as the thermocouple element at atmospheric "
      "temperature. The extension cable virtually extends the reference junction of "
      "the thermocouple to the instrument and thus compensates for the temperature "
      "variation between the thermocouple junction and the instrument.")

    P(b, lang,
      "Khi cáp nối dài quá đắt, người ta dùng vật liệu rẻ hơn thuộc các loại khác "
      "với tổ hợp phần tử nhiệt điện. Những vật liệu này cần có đặc tính thermo-emf "
      "tương đương. Các cáp này gọi là cáp bù và thường bù đầy đủ cho emf sinh ra tại "
      "điểm nối. Cáp nối dài/cáp bù có cực tính khác nhau nên được phân biệt màu riêng "
      "để nhận biết đúng cực. Để nhận biết loại cáp, người ta cũng mã màu tổng thể. "
      "Mã màu ANSI tiêu chuẩn của một số cặp nhiệt điện thông dụng được chỉ ra trong "
      "Bảng 3.2, còn đặc tính chi tiết của chúng được thể hiện trong Bảng 3.3.",
      "When extension cables are found to be expensive, other less expensive "
      "material of different types from the thermoelement combinations are used. "
      "These materials need to have equivalent thermo-emf characteristics. These "
      "cables are known as compensating cables and normally give adequate "
      "compensation for generated emf at the junction. The extension/compensating "
      "cables being of different polarity are colour coded individually for correct "
      "polarity identification. For identification of the type of cable, the overall "
      "colour coding is also done. The standard ANSI colour coding of some of the "
      "very popular thermocouples have been indicated in the Table 3.2 while the "
      "characteristic details of these have been shown in Table 3.3.")

    TBL(b, lang,
      ["Loại cặp nhiệt điện", "Vật liệu cáp nối dài", "Mã màu cực tính",
       "Mã màu tổng thể"],
      ["Thermocouple type", "Extension cable material", "Polarity colour code",
       "Overall colour code"],
      [["S và R", "Đồng-đồng / Hợp kim niken", "+ Đen − Đỏ", "Xanh lá"],
       ["K", "Chromel-Alumel", "+ Vàng − Đỏ", "Vàng"],
       ["J", "Iron-Constantan", "+ Trắng − Đỏ", "Đen"],
       ["B", "Dây dẫn đồng", "+ Xám − Đỏ", "Xám"]]
      if lang == "vi" else
      [["S and R", "Copper-copper / Nickel Alloy", "+ Black − Red", "Green"],
       ["K", "Chromel-Alumel", "+ Yellow − Red", "Yellow"],
       ["J", "Iron-Constantan", "+ White − Red", "Black"],
       ["B", "Copper Conductor", "+ Grey − Red", "Grey"]],
      caption_vi="Bảng 3.2", caption_en="Table 3.2")

    P(b, lang,
      "Thông thường cặp nhiệt điện loại K và J dùng cáp nối dài, còn loại S, R và B "
      "dùng cáp bù.",
      "Normally the thermocouples type K and J use extension cable whereas type S, "
      "R and B use compensating cable.")

    TBL(b, lang,
      ["Loại và chi tiết khác", "Thành phần",
       "Điện áp sinh ra trên mỗi độ tăng nhiệt", "Đo liên tục", "Đo ngắt quãng"],
      ["Type and other detail", "Composition details",
       "Voltage produced per degree temperature rise", "Continuous measurement",
       "Intermittent measurement"],
      [["• Loại S (đường kính đầu 0,5 mm)",
        "Bạch kim 100% / Bạch kim 90% + Rhodium 10%",
        "5 đến 10 microvolt", "1400 °C", "1600 °C"],
       ["• Loại R (đường kính đầu 0,5 mm)",
        "Bạch kim 100% / Bạch kim 87% + Rhodium 13%",
        "5 đến 12 microvolt", "1400 °C", "1700 °C"],
       ["• Loại K (đường kính đầu 1,5 đến 3 mm) Chromel-Alumel",
        "Niken 90% + Chromium 10% / Niken 94% + Nhôm 2% + Silicon và Mangan 4%",
        "40 đến 55 microvolt", "1100 °C", "1300 °C"],
       ["• Loại B (đường kính đầu 0,5 mm)",
        "Bạch kim 94% + Rhodium 6% / Bạch kim 70% + Rhodium 30%",
        "5 đến 7 microvolt", "1800 °C", "2100 °C"],
       ["• LOẠI J (đường kính đầu 2 mm) Iron-Constantan",
        "Sắt 100% / Niken 40% + Đồng 6%",
        "45 đến 57 microvolt", "800 °C", "1100 °C"]]
      if lang == "vi" else
      [["• Type S (tip diameter 0.5 mm)",
        "Platinum 100% / Platinum 90% + Rhodium 10%",
        "5 to 10 microvolt", "1400°C", "1600°C"],
       ["• Type R (tip diameter 0.5 mm)",
        "Platinum 100% / Platinum 87% + Rhodium 13%",
        "5 to 12 microvolt", "1400°C", "1700°C"],
       ["• Type K (tip diameter 1.5 to 3 mm) Chromel-Alumel",
        "Nickel 90% + Chromium 10% / Nickel 94% + Aluminum 2% + "
        "Silicon and Manganese 4%",
        "40 to 55 microvolt", "1100°C", "1300°C"],
       ["• Type B (tip diameter 0.5 mm)",
        "Platinum 94% + Rhodium 6% / Platinum 70% + Rhodium 30%",
        "5 to 7 microvolt", "1800°C", "2100°C"],
       ["• TYPE J (tip diameter 2 mm) Iron-Constantan",
        "Iron 100% / Nickel 40% + Copper 6%",
        "45 to 57 microvolt", "800°C", "1100°C"]],
      caption_vi="Bảng 3.3", caption_en="Table 3.3")

    P(b, lang,
      "Giống như phần tử RTD, ở đây cũng có nhiều tiêu chuẩn hiệu chuẩn khác nhau. "
      "Một số tiêu chuẩn được liệt kê trong Bảng 3.4 cùng với nhiệt độ đại diện "
      "(100 °C và 200 °C), suất điện động tương đương và dung sai tiêu chuẩn.",
      "Like RTD element, here also there are different calibration standards in "
      "use. Some of the standards have been indicated on the Table 3.4 along with "
      "representative temperature (100°C and 200°C), equivalent emf and standard "
      "tolerances.")

    _t34 = [
      ("Tiêu chuẩn Hoa Kỳ – ANSI MC 96.1",
       "American Standards – ANSI MC 96.1",
       [("Loại S", "S-type", "100°C", "0.645", "± 5°C"),
        ("Loại S", "S-type", "200°C", "1.440", "± 5°C"),
        ("Loại R", "R-type", "100°C", "0.647", "± 5°C"),
        ("Loại R", "R-type", "200°C", "1.468", "± 5°C"),
        ("Loại K", "K-type", "100°C", "4.095", "± 2.2°C"),
        ("Loại K", "K-type", "200°C", "8.137", "± 2.2°C"),
        ("Loại J", "J-type", "100°C", "5.268", "± 2.2°C"),
        ("Loại J", "J-type", "200°C", "10.777", "± 2.2°C"),
        ("Loại B", "B-type", "100°C", "0.033", "± 3°C"),
        ("Loại B", "B-type", "200°C", "0.178", "± 3°C")]),
      ("Tiêu chuẩn Đức – DIN43714 và 43710",
       "German Standards – DIN43714 and 43710",
       [("Loại S", "S-type", "100°C", "0.645", "± 3°C"),
        ("Loại S", "S-type", "200°C", "0.440", "± 3°C"),
        ("Loại R", "R-type", "100°C", "0.645", "± 3°C"),
        ("Loại R", "R-type", "200°C", "1.440", "± 3°C"),
        ("Loại K", "K-type", "100°C", "4.095", "± 3°C"),
        ("Loại K", "K-type", "200°C", "8.137", "± 3°C"),
        ("Loại J", "J-type", "100°C", "5.370", "± 3°C"),
        ("Loại J", "J-type", "200°C", "10.950", "± 3°C"),
        ("Loại B", "B-type", "...", "...", "..."),
        ("Loại B", "B-type", "...", "...", "...")]),
      ("Tiêu chuẩn Ấn Độ – IS 8784 – 1987",
       "Indian Standards – IS 8784 – 1987",
       [("Loại S", "S-type", "100°C", "0.644", "± 3°C"),
        ("Loại S", "S-type", "200°C", "1.463", "± 3°C"),
        ("Loại R", "R-type", "100°C", "0.644", "± 3°C"),
        ("Loại R", "R-type", "200°C", "1.463", "± 3°C"),
        ("Loại K", "K-type", "100°C", "4.095", "± 2.2°C"),
        ("Loại K", "K-type", "200°C", "8.137", "± 2.2°C"),
        ("Loại J", "J-type", "100°C", "5.268", "± 2.2°C"),
        ("Loại J", "J-type", "200°C", "10.777", "± 2.2°C"),
        ("Loại B", "B-type", "...", "...", "..."),
        ("Loại B", "B-type", "...", "...", "...")]),
      ("Tiêu chuẩn Anh – BS 1843 và BS 4937",
       "British Standards – BS 1843 and BS 4937",
       [("Loại S", "S-type", "100°C", "0.645", "± 5°C"),
        ("Loại S", "S-type", "200°C", "1.440", "± 5°C"),
        ("Loại R", "R-type", "100°C", "0.645", "± 5°C"),
        ("Loại R", "R-type", "200°C", "1.440", "± 5°C"),
        ("Loại K", "K-type", "100°C", "4.095", "± 2.2°C"),
        ("Loại K", "K-type", "200°C", "8.137", "± 2.2°C"),
        ("Loại J", "J-type", "100°C", "5.268", "± 2.2°C"),
        ("Loại J", "J-type", "200°C", "10.777", "± 2.2°C"),
        ("Loại B", "B-type", "...", "...", "..."),
        ("Loại B", "B-type", "...", "...", "...")]),
    ]
    _rows_vi, _rows_en = [], []
    for _gvi, _gen, _items in _t34:
        _rows_vi.append(_gvi)
        _rows_en.append(_gen)
        for _vi, _en, _t, _e, _tol in _items:
            _rows_vi.append([_vi, _t, _e, _tol])
            _rows_en.append([_en, _t, _e, _tol])

    TBL(b, lang,
      ["Cặp nhiệt điện", "Nhiệt độ", "emf (mV)", "Dung sai"],
      ["Thermocouple", "Temperature", "emf (mV)", "Tolerances"],
      _rows_vi if lang == "vi" else _rows_en,
      caption_vi="Bảng 3.4", caption_en="Table 3.4")

    P(b, lang,
      "Khảo sát các tiêu chuẩn khác nhau cho thấy sự khác biệt giữa hai tiêu chuẩn "
      "đối với cùng một dữ liệu cặp nhiệt điện là rất nhỏ, đôi khi hoàn toàn không "
      "có. Do đó, sai số do lựa chọn tiêu chuẩn hiệu chuẩn có thể không đáng báo "
      "động đối với sử dụng thông thường.",
      "A study of different standards reveals that the difference between the two "
      "standards for a particular thermocouple data is marginal and sometimes not "
      "at all. Therefore, error introduced due to choice of calibration standards "
      "may not be alarming for general use.")

    return b
