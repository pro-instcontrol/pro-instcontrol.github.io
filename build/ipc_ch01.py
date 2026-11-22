# -*- coding: utf-8 -*-
"""Chapter 1, "Transducers - I" (EN/VI bilingual).

Source: Janardan Prasad, M. N. Jayaswal and Vishnu Priye, *Instrumentation and
Process Control* (I.K. International, 2019), PDF pp. 13-74, printed pp. 1-62.
PAGES_SRC = 62 counts the assigned source span.

The source chapter has seven numbered sections, 51 numbered figures, seven
tables, 41 numbered equations, eight worked examples and a 13-question
exercise.  All figures are redrawn as vectors in `ipcfig.py`.  The PDF stores
its body text as glyph codes; the decoded text layer retains OCR artifacts,
so equations are rendered symbolically and the tables transcribed from the
printed pages.
"""

import ipc_common as C          # noqa: F401  (page shell, used by C.build)
import ipcfig as F
from ipc_common import (eq, fig, h2, h3, h4, lead, note, ol, p, table, ul)

PAGES_SRC = 62
BYLINE = ("Janardan Prasad · M. N. Jayaswal · Vishnu Priye · "
          "Instrumentation and Process Control (I.K. International, 2019)")
TITLE_EN = "Transducers – I"
TITLE_VI = "Bộ chuyển đổi – I"


# ---------------------------------------------------------------------------
# Tables transcribed from the printed pages.  Headers are localized, numeric
# bodies are shared between the two language versions.
# ---------------------------------------------------------------------------
_TBL11 = [
    ["1", "Constantan (45% Ni, 55% Cu)", "2.1", "48 × 10⁻⁸", "300"],
    ["2", "Nichrome (80% Ni, 20% Cr)", "2.1 to 2.5", "100 × 10⁻⁸", "1200"],
    ["3", "Isoelastic (36% Ni, 8% Cr, 0.5% Mo, 55.5% Fe)", "3.5", "80 × 10⁻⁸", "1200"],
    ["4", "Karma (74% Ni, 20% Cr, 3% Al, 3% Fe)", "2.1", "125 × 10⁻⁸", "1200"],
    ["5", "Pure platinum", "4.8", "10 × 10⁻⁸", "—"],
    ["6", "Pure nickel", "12", "6.5 × 10⁻⁸", "—"],
]

_TBL12 = [
    ["1", "Paper", "0 to 100 °C"],
    ["2", "Epoxy or bakelite", "0 to 150 °C"],
    ["3", "Fibre glass", "0 to 200 °C"],
]

_TBL13 = [
    ["1", "DUROFIX (nitro cellulose acetone duco)"],
    ["2", "EASTMAN 910 (cyano acrylate acrylic cement)"],
    ["3", "ARALDITE (phenolic cement)"],
    ["4", "Silicone varnish (up to 400 °C)"],
    ["5", "Ceramic cement (above 400 °C)"],
]

_TBL14 = [
    ["1", "Platinum", "−200 °C to 630.5 °C", "0.39"],
    ["2", "Copper", "0 to 160 °C", "0.43"],
    ["3", "Nickel", "−200 °C to +200 °C", "0.65"],
]

_TBL15 = [
    ["Quartz", "50 × 10⁻³", "2", "40.6 × 10⁻¹²", "9 × 10¹⁰", "4.5"],
    ["Barium titanate", "12 × 10⁻³", "150", "12.5 × 10⁻⁹", "12 × 10¹⁰", "1380"],
]

_TBL16 = [
    ["Carbon", "0.4 to 1.8", "11.76 × 10⁻⁹"],
    ["Bismuth", "0.11 to 1", "106 × 10⁻⁶"],
    ["Silicon", "2", "4.1 × 10⁻⁶"],
    ["N-type germanium", "0.001 to 0.8", "8 × 10⁻⁶"],
    ["Copper", "0.8 to 2.2", "52 × 10⁻¹²"],
]

_TBL17 = [
    ["0", "0.2", "0"],
    ["25", "0.4", "25"],
    ["50", "0.6", "50"],
    ["75", "0.8", "75"],
    ["100", "1.0", "100"],
]


def _h(vi, en, idx):
    """Localized header row for one of the seven source tables."""
    heads = {
        1: (["S. No.", "Vật liệu", "Gs", "Điện trở suất (ohm-cm)", "Giới hạn nhiệt độ (°C)"],
            ["S. No.", "Material", "Gs", "Resistivity (ohm-cm)", "Temperature limit (°C)"]),
        2: (["S. No.", "Vật liệu", "Dải nhiệt độ làm việc"],
            ["S. No.", "Material", "Working temperature range"]),
        3: (["S. No.", "Chất dán"], ["S. No.", "Adhesive"]),
        4: (["S. No.", "Vật liệu", "Dải sử dụng", "Hệ số nhiệt của điện trở (/°C)"],
            ["S. No.", "Material", "Range of use", "Resistance temperature coefficient (/°C)"]),
        5: (["Vật liệu", "Kv", "Kc", "ε", "E", "Độ bền điện môi"],
            ["Material", "Kv", "Kc", "ε", "E", "Dielectric strength"]),
        6: (["Vật liệu", "Mật độ từ thông cần (Wb/m²)", "KH"],
            ["Material", "Required flux density (Wb/m²)", "KH"]),
        7: (["Đầu vào đo (%)", "Tín hiệu đầu ra (kg/cm²)", "Chỉ thị (%)"],
            ["Measurement input (%)", "Output signal (kg/cm²)", "Indication (%)"]),
    }
    v, e = heads[idx]
    return v if vi else e


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> bộ chuyển đổi — transducer · bộ phát — transmitter · "
                "cảm biến — sensor · tín hiệu — signal · đặc tính — characteristic · độ tuyến tính — "
                "linearity · đầu ra — output · đầu vào — input · bộ điều hòa tín hiệu — conditioning "
                "system · phần tử sơ cấp — primary element · phần tử thứ cấp — secondary element · "
                "bộ chuyển đổi ngược — inverse transducer · sai số — error · độ trễ — hysteresis · "
                "căng kế — strain gage · hệ số gage — gage factor · nhiệt trở — thermistor · "
                "cặp nhiệt điện — thermocouple · áp điện — piezoelectric · Hall — Hall effect.")
    return ("<b>Key terms.</b> transducer · transmitter · sensor · signal · characteristic · "
            "linearity · output · input · conditioning system · primary element · secondary "
            "element · inverse transducer · error · hysteresis · strain gage · gage factor · "
            "thermistor · thermocouple · piezoelectric · Hall effect.")


# ===========================================================================
def _body(lang):
    vi = lang == "vi"
    en = not vi
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(v, e):
        b.append(ul(v if vi else e))

    def E(vi_s, en_s):
        b.append(eq(vi_s if vi else en_s))

    def FIG(n, fn):
        b.append(fig(n, fn, lang))

    def TB(header, rows):
        b.append(table(header, rows))

    # ---------------------------------------------------------------- lead
    b.append(lead(
        "Chương này định nghĩa và phân loại bộ chuyển đổi, phân biệt bộ chuyển đổi với bộ phát và "
        "bộ chuyển đổi ngược, trình bày ba nhóm đặc tính (đầu vào, đầu ra và truyền đạt) và khảo "
        "sát kỹ các phần tử chuyển đổi cơ khí, điện và quang cùng các hệ thống chuyển đổi thứ cấp."
        if vi else
        "This chapter defines and classifies transducers, distinguishes a transducer from a "
        "transmitter and from an inverse transducer, sets out the three groups of characteristics "
        "(input, output and transfer), and surveys the mechanical, electrical and optical "
        "conversion elements together with the secondary transducing systems."))

    # ---------------------------------------------------------------- 1.1
    H("1.1 Mở đầu", "1.1 Introduction")
    P("Nguồn gốc của cảm nhận và chuyển đổi có thể truy về ngay từ khởi đầu của sự sống trên "
      "Trái Đất. Chẳng hạn, các giác quan của chúng ta liên tục tương tác với môi trường và biến "
      "đầu vào cảm giác thành các kích thích cho não. Điều đó lại thúc đẩy chúng ta hành xử như "
      "cách chúng ta hành xử. Đôi khi điều này gây ngạc nhiên về việc chúng ta thực hiện một cách "
      "vô ý những gì mà thực tế chúng ta được yêu cầu làm. Ở đây chúng ta nhận ra rằng con người "
      "là hệ thống điều khiển tối thượng. Hệ thống điều khiển do tạo hóa thiết kế dường như rất "
      "đơn giản. Nhưng sự phức tạp thực sự bắt đầu hiện rõ khi chúng ta nghĩ đến việc thiết kế và "
      "triển khai hệ thống điều khiển của riêng mình. Ví dụ, một máy cơ học nhận dạng mẫu hoặc một "
      "máy nhận dạng giọng nói. Những thiết bị này đòi hỏi vô số giờ lập trình máy tính phức tạp "
      "và khả năng cảm nhận cực kỳ tinh vi. Sự kết hợp đó cho phép một thiết bị quang học trước hết "
      "phân biệt mẫu này với mẫu kia, rồi chọn mẫu thích hợp. Trường hợp nhận dạng giọng nói cũng "
      "tương tự. Dù phức tạp đến đâu, cảm biến và bộ chuyển đổi vẫn là những thành phần quan trọng "
      "nhất trong mọi tổ chức hệ thống điều khiển.",
      "The origin of sensing and transducing can be traced to the very start of life on the earth "
      "itself. For instance, our sensory organs every time interact with the environments and "
      "transform the sensory input into brain stimuli. This in turn compels us to act the way we "
      "act. Sometimes this seems surprising as to how unconsciously we perform the way we "
      "actually are required to. Here we realize that the human beings are the ultimate control "
      "system. The control system devised by the Almighty seems to be very simple. But the real "
      "complexity, we start realizing when we think of designing and implementing our own control "
      "system. For instance, a mechanical machine for recognizing patterns or a machine for "
      "recognizing different voices. These would involve countless hours of complex computer "
      "programming and very sophisticated sensing capabilities. Such combination allows an "
      "optical device to first differentiate one pattern from the other and then select the "
      "proper one. Similar is the case with the voice recognition system. Whatever may be the "
      "complexities the sensor and the transducer combinations are the components of prime "
      "importance for any control system organization.")
    P("Thực chất, bộ chuyển đổi là phần tử đầu vào cơ bản của hệ thống thiết bị do con người tạo "
      "ra. Hiệu quả mà nói, bộ chuyển đổi là một gói hoàn chỉnh gồm cả cảm biến lẫn hệ thống điều "
      "hòa. Cảm biến tương tác với môi trường theo cách sao cho đo được một sự thay đổi trong môi "
      "trường. Chẳng hạn, sự thay đổi nhiệt lượng bên trong một ranh giới nhất định làm thay đổi "
      "điện trở của một vật liệu được chọn đặt bên trong. Sự thay đổi điện trở này, khi được nối "
      "vào cầu Wheatstone, cho ra dòng mất cân bằng có cỡ vi ampe. Dòng mất cân bằng này tỉ lệ với "
      "sự thay đổi điện trở. Sau khi được khuếch đại và bù thích hợp (trong đơn vị điều hòa tín "
      "hiệu), dòng này có thể dùng làm đầu vào cho hệ thống thiết bị.",
      "Transducer is in fact the basic input element to the man-made instrumentation system. In "
      "effect a transducer is a complete package consisting of sensor as well as conditioning "
      "system. A sensor interacts with its environments in such a way as to measure something "
      "changing in the environment. For instance, change in heat content inside a particular "
      "boundary changes the resistance of a selected material immersed inside it. This change in "
      "resistance when connected to a wheatstone bridge results in an out of balance current of "
      "the order of microampere. This out of balance current is proportional to the resistance "
      "change. This current after suitable amplification and compensation (to be carried out in "
      "the signal conditioning unit) can be used as input to instrumentation system.")

    # ---------------------------------------------------------------- 1.2
    H("1.2 Định nghĩa bộ chuyển đổi", "1.2 Definition of Transducer")
    P("Bộ chuyển đổi có thể được định nghĩa là một thiết bị hoàn chỉnh. Nó nhận sự thay đổi của "
      "quá trình làm đầu input và biến đổi những thay đổi đó thành dạng đầu ra thích hợp sao cho "
      "đầu ra là biểu diễn tỉ lệ của đầu vào. Một bố trí bộ chuyển đổi tổng quát được thể hiện "
      "trong sơ đồ khối Hình 1.1. Đôi khi bộ chuyển đổi cũng được hiểu là bộ phát. Về bản chất, "
      "bộ phát là thiết bị đáp ứng với biến quá trình thay đổi và tạo ra một tín hiệu tỉ lệ. Tín "
      "hiệu này được đưa tới thiết bị thu để chỉ thị hoặc điều khiển như trong sơ đồ khối Hình "
      "1.2. Tuy nhiên, bộ chuyển đổi tiếp xúc vật lý với quá trình và tạo ra phản ứng dưới dạng "
      "chuyển động hoặc lực khi biến quá trình thay đổi. Khi phản ứng này được dùng để tạo ra tín "
      "hiệu theo một thang đo xác định dùng cho đo lường hoặc điều khiển, bộ chuyển đổi được coi "
      "là đang hoạt động như một bộ phát. Theo cách này, mọi bộ phát về bản chất đều là bộ chuyển "
      "đổi, nhưng không phải mọi bộ chuyển đổi đều là bộ phát.",
      "A transducer can be defined as a complete device in itself. It takes changes in process as "
      "input and transforms these into suitable output form in such a way that the output is the "
      "proportionate representation of the input. A general transducer arrangement has been shown "
      "in the block diagram (Figure 1.1). Sometimes transducers are understood to be a "
      "transmitters as well. A transmitter essentially is a device that responds to a changing "
      "process variable and produces a proportional signal. This signal is fed to a receiver "
      "instrument for indication or control purposes as shown in the block diagram in Figure "
      "1.2. A transducer, however, is in physical contact with the process and produces a "
      "response in terms of motion or force when the process variable changes. When this response "
      "is used to generate a signal with respect to a particular scale used for measurement or "
      "control, the transducer is said to be performing as a transmitter. In this way, all "
      "transmitters are essentially transducers, but all transducers are not necessarily "
      "transmitters.")
    FIG(1, F.fig_f01())
    FIG(2, F.fig_f02())

    # ---------------------------------------------------------------- 1.3
    H("1.3 Phân loại bộ chuyển đổi", "1.3 Classification of Transducer")
    P("Sau đây là các loại bộ chuyển đổi khác nhau.", "Following are the various transducers.")

    H("1.3.1 Bộ chuyển đổi sơ cấp và thứ cấp", "1.3.1 Primary and Secondary Transducers", h3)
    P("Bộ phát hiện chuyển động hoặc lực tạo ra phản ứng dưới dạng dịch chuyển có cỡ 0,001 inch từ "
      "các bộ chuyển đổi đầu vào. Những bộ chuyển đổi sơ cấp này còn gọi là Phần tử đo sơ cấp. Các "
      "phần tử cảm nhận này được dùng để tạo tín hiệu theo một thang đo xác định, tương ứng với "
      "biến được đo. Đơn vị tạo tín hiệu được điều khiển chủ yếu bởi bộ chuyển đổi đầu vào hoặc sơ "
      "cấp được gọi là bộ chuyển đổi thứ cấp hay bộ chuyển đổi đầu ra. Các bộ chuyển đổi thứ cấp "
      "tạo ra tín hiệu chuẩn là 4 đến 20 mA hoặc 1 đến 5 V đối với tín hiệu điện, và/hoặc 0,2 đến "
      "1,0 kg/cm² đối với tín hiệu khí nén.",
      "Motion or force detectors produce response in terms of displacement of the order of 0.001 "
      "inch from the input transducers. These primary transducers are also called Primary Measuring "
      "Elements. These sensing elements are used to generate a signal with respect to a particular "
      "scale, relative to a measured variable. The signal-generating unit that is actuated "
      "essentially by the input or primary transducer is hereafter called secondary transducer or "
      "output transducer. The secondary transducers generate a standard signal that is 4 to 20 mA "
      "or 1 to 5 volt in terms of electrical signal and/or 0.2 to 1.0 kg/cm2 in terms of pneumatic "
      "signal.")
    P("Đôi khi một tín hiệu điện sẵn có phải được đổi sang tín hiệu khí nén tương đương và ngược "
      "lại. Những bộ đổi này cũng được gọi là bộ chuyển đổi. Chẳng hạn, Bộ chuyển đổi điện-khí nén "
      "thường được dùng để vận hành các van điều khiển khí nén trong điều khiển quá trình. Tương "
      "tự, bộ chuyển đổi khí nén-điện được dùng để thu chỉ thị khí nén dưới dạng chỉ thị điện.",
      "Sometimes an available electrical signal may have to be converted to equivalent pneumatic "
      "signal and vice-versa. Such converters are also called transducers. For instance, "
      "Electro-pneumatic Transducer which is normally used for operation of pneumatic control "
      "valves in process control. Similarly, a pneumatic-to-electrical transducer which is used "
      "for obtaining the pneumatic indication in terms of electrical indication.")
    P("Điều quan trọng cần lưu ý là tín hiệu đầu ra không bắt đầu từ zero. Nghĩa là vẫn có một đầu "
      "ra nhất định ngay khi biến quá trình bằng zero, đó là 4 mA điện. Đây gọi là Hệ thống zero "
      "sống (Live Zero System), bởi tín hiệu 4 mA vẫn có ngay cả khi biến quá trình ở giới hạn "
      "thấp nhất. Ưu điểm của hệ thống này là cung cấp cách phát hiện hở mạch trong hệ thống tín "
      "hiệu.",
      "It is important to note that the output signal does not start from zero. This means that "
      "some output is available at zero process variable as well, that is 4 mA electrical. This "
      "is known as Live Zero System, because the output signal of 4 mA is available even when the "
      "process variable is at its lowest limit. The advantage of this system is that it provides "
      "a means of detecting an open circuit fault in the signal system.")

    H("1.3.2 Bộ chuyển đổi chủ động và thụ động", "1.3.2 Active and Passive Transducer", h3)
    P("Bộ chuyển đổi chủ động, như tên gọi, hoạt động mà không cần nguồn cung cấp bên ngoài. Chúng "
      "là bộ chuyển đổi tự sinh (điện áp hoặc dòng). Vì vậy, bản thân chúng có khả năng tạo đầu ra "
      "để điều khiển hệ thống đo thứ cấp. Năng lượng cần để tạo đầu ra vốn có trong chính quá "
      "trình đang được đo. Chẳng hạn, phần tử cặp nhiệt điện là phần tử đo nhiệt độ. Nguyên lý làm "
      "việc của cặp nhiệt rất đơn giản. Khi hai kim loại khác nhau (ví dụ bạch kim và rhodium) có "
      "đặc tính phù hợp được hàn nóng chảy lại với nhau, ta có một cặp nhiệt điện như Hình 1.3. "
      "Đầu hàn được gọi là mối nóng vì nó phải được nhúng trong môi trường nóng. Để đo, đầu này "
      "được đặt bên trong môi trường nóng cần đo nhiệt độ. Hai đầu kia được nối vào mạch đo tạo "
      "thành mối lạnh. Do chênh nhiệt độ giữa mối nóng và mối lạnh, một thermo-emf được sinh ra, "
      "gây ra dòng điện chạy qua mạch đo. Emf này có cỡ vài milivôn và có thể được tiền khuếch đại "
      "để có chỉ thị tỉ lệ cho hệ thống đo. Các ví dụ khác về bộ chuyển đổi chủ động là máy phát "
      "tốc độ (tachogenerator), pin quang điện (photovoltaic) và mọi bộ chuyển đổi chế tạo theo "
      "nguyên lý hiệu ứng áp điện.",
      "Active transducers, as the name suggests, are active without the help of any outside supply "
      "source. They are self-generating (voltage or current) transducers. Thus, they are themselves "
      "capable of producing output for actuation of the secondary measurement system. The energy "
      "required for production of output is inherent in the process itself which is being "
      "measured. For instance, a thermocouple element which is a temperature measurement element. "
      "The principle of working of thermocouple is very simple. When two dissimilar metals (say "
      "platinum and rhodium) of appropriate characteristics are fused together it becomes a "
      "thermocouple, as shown in the Figure 1.3. The fused tip is called hot junction since this "
      "has to be immersed in the hot medium. For measurement purposes, this end is placed inside a "
      "hot medium whose temperature has to be measured. The other ends are connected to the "
      "measurement circuit to form a cold junction. Due to difference in temperature of the hot "
      "and cold junction, thermo-emf is induced which is responsible for a current flow through "
      "the measurement circuit. This emf is of the order of several millivolts which can be "
      "preamplified for obtaining a proportional indication for the measurement system. Other "
      "examples of active transducers are tachogenerator, photovoltaic cells and all transducers "
      "fabricated on the principle of piezoelectric effects.")
    FIG(3, F.fig_f03())
    P("Mặt khác, bộ chuyển đổi thụ động là bộ chuyển đổi được cung cấp năng lượng từ bên ngoài. "
      "Chúng tạo tín hiệu đầu ra tương ứng với công suất cấp cho nó. Chẳng hạn, Đầu dò nhiệt độ "
      "điện trở (RTD) là phần tử thay đổi điện trở do thay đổi nhiệt độ. Vì vậy, khi RTD được nhúng "
      "trong môi trường nóng, điện trở của nó sẽ thay đổi. Tuy nhiên, sự thay đổi này không cảm "
      "nhận được trừ khi nó được nối vào một nguồn. Thường thì hệ thống này được nối vào cầu "
      "Wheatstone do pin nguồn cấp. Dòng mất cân bằng của cầu, khi đi qua phần tử phát hiện (DE), "
      "sẽ chỉ ra sự thay đổi điện trở do thay đổi nhiệt độ. Hệ thống được thể hiện trong Hình 1.4. "
      "Đây là ví dụ về bộ chuyển đổi thụ động. Các ví dụ khác là bộ chuyển đổi áp suất khí nén "
      "được cấp nguồn khí nén (áp suất cấp là 1,4 kg/cm² không khí khô và tín hiệu đầu ra tương ứng "
      "là 0,2 đến 1,0 kg/cm² không khí).",
      "The passive transducers on the other hand are externally powered transducers. These "
      "generate output signals with respect to power supplied to it. For instance, a Resistance "
      "Temperature Detector (RTD) is an element which changes its resistance due to change of "
      "temperature. Hence, when this RTD is immersed in a hot medium, its resistance will change. "
      "This change, however, cannot be felt unless it is connected to some source. Usually, such "
      "a system is connected to wheatstone bridge powered by a supply battery. The out of balance "
      "current of the bridge when passed through the detecting element (DE) shall indicate the "
      "change in resistance brought about by the change in temperature. The system has been shown "
      "in the Figure 1.4. This is an example of passive transducer. Other examples are pneumatic "
      "pressure transducers which are powered pneumatically (supply pressure being 1.4 kg/cm2 dry "
      "air and corresponding output signal being 0.2 to 1.0 kg/cm2 air).")
    FIG(4, F.fig_f04())

    H("1.3.3 Bộ chuyển đổi tương tự và số", "1.3.3 Analog and Digital Transducers", h3)
    P("Bộ chuyển đổi tương tự biến biến đầu vào thành đầu ra tương tự. Đầu ra tương tự thay đổi theo "
      "thời gian một cách liên tục. Do đó đầu ra là hàm liên tục của thời gian. Hầu hết mọi loại "
      "bộ chuyển đổi truyền thống đều là tương tự vì đầu ra của chúng là hàm liên tục của thời "
      "gian. Tuy nhiên, hiện nay một loại bộ chuyển đổi mới đã xuất hiện trong lĩnh vực thiết bị "
      "gọi là bộ chuyển đổi số. Chúng biến biến đầu vào thành đầu ra điện ở dạng xung. Theo cách "
      "đó, đầu ra của hai điểm tiếp điểm có trạng thái NO và NC (normally open và normally closed) "
      "của rơ le điện từ cũng được coi là bộ chuyển đổi số. Điều này là do nó cung cấp hai vị trí "
      "rời rạc của hệ thống giống như công tắc bật-tắt. Tiếp điểm NO và NC được thể hiện trong "
      "Hình 1.5.",
      "The analog transducers convert the input variable into an analog output. The analog output "
      "varies with respect to time in continuous fashion. Thus, the output is a continuous "
      "function of time. Almost all types of conventional transducers are analog because their "
      "output is a continuous function of time. However, nowadays a new class of transducers has "
      "appeared in the instrumentation field called digital transducers. They convert the input "
      "variable into an electrical output which is in pulse form. In that way an output of NO and "
      "NC (normally open and normally closed) contacts of electromagnetic relay two position "
      "contact points are also considered to be a digital transducer. This is due to the fact that "
      "it provides two distinct positions of the system similar to an on-off switch. The NO and "
      "NC contacts have been shown in the Figure 1.5.")
    FIG(5, F.fig_f05())
    P("Đôi khi bộ chuyển đổi sơ cấp có dạng tương tự và cho đầu ra tương tự, nhưng nhờ bổ sung một "
      "bộ chuyển đổi thứ cấp nên sau đó được đổi sang dạng số. Những bộ chuyển đổi như vậy cũng "
      "có thể được coi là bộ chuyển đổi số. Đáng chú ý là bộ chuyển đổi số trình bày tín hiệu đo "
      "ở dạng số để chỉ thị. Hình 1.6 cho thấy sự kết hợp của bộ chuyển đổi áp suất (là bộ chuyển "
      "đổi sơ cấp) và bộ đổi tương tự-số (là bộ chuyển đổi thứ cấp) được nối giữa đầu vào và đầu ra.",
      "Sometimes the primary transducer is in the form of analog itself and provides output in "
      "the analog form but by providing a secondary transducer, it is later on converted to "
      "digital form. Such transducers, can also be regarded as digital transducers. It is worth "
      "mentioning that a digital transducer presents the measurement signal output in digital "
      "form for indication. Figure 1.6 shows a combination of pressure transducer (as primary "
      "transducer) and analog to digital converter (as secondary transducer) connected in between "
      "the input and the output.")
    FIG(6, F.fig_f06())

    # ---------------------------------------------------------------- 1.4
    H("1.4 Bộ chuyển đổi ngược", "1.4 Inverse Transducer")
    P("Điều chúng ta đã thảo luận cho đến nay là bộ chuyển đổi biến biến quá trình đầu vào thành "
      "đầu ra điện hoặc đầu ra khí nén tỉ lệ. Đầu ra này chủ yếu được dùng làm đầu vào để chỉ thị, "
      "ghi hoặc điều khiển. Bộ điều khiển cũng đưa ra tín hiệu đầu ra gọi là đầu ra điều khiển. "
      "Đầu ra điều khiển này được dùng để tác động trở lại đầu vào thông qua phần tử điều khiển "
      "cuối xác định nhằm đưa biến quá trình về mức mong muốn. Người ta mong muốn đầu ra điều "
      "khiển phải thích ứng được với phần tử điều khiển cuối. Điều này thường gọi là chuyển đổi "
      "ngược. Vì vậy, bộ chuyển đổi ngược là phần tử chuyển đổi biến đầu ra điều khiển (đặc biệt "
      "là đầu ra điện) thành dạng thích hợp để điều khiển phần tử điều khiển cuối.",
      "Whatever we have discussed till now is that a transducer converts the input process "
      "variable into proportional electrical output or pneumatic output. This output is "
      "essentially used as input for indication, recording or controlling. The controller also "
      "presents an output signal, which is called control output. This control output is used for "
      "manipulating the input through specified final control element to bring back the process "
      "variable to the desired level. It is desirable that control output should be adaptable to "
      "the final control element. This is usually called inverse transduction. Hence, the inverse "
      "transducer is a transducer element that converts the control output (electrical output in "
      "particular) into suitable form for actuation of the final control element.")
    FIG(7, F.fig_f07())
    P("Hình 1.7 cho thấy một vòng điều khiển áp suất điển hình thường dùng trong công nghiệp quá "
      "trình để đo lường cũng như điều khiển. Vị trí của bộ chuyển đổi ngược trong vòng điều khiển "
      "này là trước phần tử điều khiển cuối. Bộ chuyển đổi này biến đầu ra từ bộ điều khiển chỉ thị "
      "áp suất (PIC) thành tín hiệu phù hợp để vận hành phần tử điều khiển cuối, trong trường hợp "
      "này là van điều khiển vận hành bằng khí nén. Một tên gọi khác của bộ chuyển đổi ngược ở đây "
      "là bộ chuyển đổi điện-khí nén.",
      "Figure 1.7 shows a typical pressure control loop usually employed in the process industry "
      "for measurement as well as control. The location of the inverse transducer in this control "
      "loop is before the final control element. This transducer converts the output from pressure "
      "indicator controller into appropriate signal suitable for operation of the final control "
      "element, the final control element in this case being a pneumatically operated control "
      "valve. Another name for the inverse transducer here shall be electro-pneumatic transducer.")

    # ---------------------------------------------------------------- 1.5
    H("1.5 Đặc tính của bộ chuyển đổi", "1.5 Characteristics of Transducers")
    P("Khi hoạt động, bộ chuyển đổi trải qua nhiều giai đoạn thay đổi về hành vi. Sự thay đổi hành "
      "vi đầu ra và giữa chúng là một hành vi truyền đạt. Dựa trên những thay đổi hành vi mà bộ "
      "chuyển đổi trải qua, nhìn chung người ta quan sát thấy ba đặc tính khác nhau: đặc tính đầu "
      "vào, đặc tính đầu ra và đặc tính truyền đạt.",
      "While in operation, a transducer goes through several stages of changes in its behaviour. "
      "Changes in output behaviour and in between them lies a transfer behaviour. Based on these "
      "behavioural changes a transducer experiences, three different characteristics are observed, "
      "in general, which are input characteristics, output characteristics and transfer "
      "characteristics.")

    H("1.5.1 Đặc tính đầu vào", "1.5.1 Input Characteristics", h3)
    P("Như chúng ta biết, phần sơ cấp của bộ chuyển đổi thay đổi do những thay đổi của biến quá "
      "trình cần đo. Những thay đổi này tuân theo đặc tính của chính quá trình và được gọi là đặc "
      "tính đầu vào. Trong trường hợp cụ thể này, dải thay đổi, tức từ mức tối thiểu (trạng thái "
      "ban đầu) đến mức tối đa (trạng thái cuối), phải tương ứng với dải hoạt động của chính bộ "
      "chuyển đổi đầu vào. Độ phân giải của bộ chuyển đổi đầu vào cho những thay đổi này phải "
      "như nhau trong toàn bộ dải thay đổi của biến quá trình cần đo.",
      "As we know, the primary portion of transducer changes are due to changes in process "
      "variable to be measured. The changes follow strictly the characteristics of the process "
      "itself and is termed input characteristics. In this particular case, the range of changes, "
      "i.e. from a minimum (initial state) to a maximum (final state) must correspond to the "
      "operating range of the input transducer itself. The resolution of the input transducer for "
      "these changes must be the same through the entire range of the changes of the process "
      "variable to be measured.")
    P("Đôi khi hiệu ứng tải trở nên rõ rệt và làm dịch chuyển đặc tính đầu vào sang một vị trí mới. "
      "Nạp về bản chất là chiết xuất năng lượng từ hệ thống để vận hành bộ chuyển đổi. Trong điều "
      "kiện này, chức năng đo của bộ chuyển đổi không thể thực hiện chính xác, vì vậy người ta "
      "dùng các biện pháp thích hợp để giảm thiểu ảnh hưởng này.",
      "Sometimes loading effect becomes prominent and that shifts the input characteristic to a "
      "new position. Loading essentially means extracting energy from the system for the operation "
      "of the transducer. In this condition measurement functions by the transducers cannot be "
      "carried out accurately and therefore, suitable means are employed to minimize the effect.")

    H("1.5.2 Đặc tính đầu ra", "1.5.2 Output Characteristics", h3)
    P("Đặc tính đầu ra gồm bốn mục tiêu:", "Output characteristics constitute four objectives:")
    U(["Lựa chọn loại tín hiệu đầu ra.",
       "Lựa chọn mức tín hiệu và dải tín hiệu.",
       "Mức trở kháng đầu ra.",
       "Xem xét nhiễu."],
      ["Choice of signal output type.",
       "Choice of signal level and range.",
       "Output impedance level.",
       "Noise consideration."])

    H("(i) Loại đầu ra", "(i) Output type", h4)
    P("Đặc tính đầu ra liên quan đến loại tín hiệu đầu ra, tức là A.C. hay D.C. và mức điện áp hay "
      "dòng điện.",
      "Output characteristics, as we know are related to types of output signal, i.e. A.C. or D.C. "
      "and also voltage or current level.")
    P("D.C. so với A.C.: Thông thường đầu ra của bộ chuyển đổi phải đi một quãng đường dài trong "
      "sơ đồ thiết bị thực tế, vì vậy không nên dùng đầu ra A.C. mức thấp, tần số thấp vì từ trường "
      "lạc 50 Hz sẽ ảnh hưởng đến nó. Tuy nhiên có thể dùng đầu ra D.C. mức cao, vì thực tế nó "
      "miễn nhiễm với ảnh hưởng của nhiễu hoặc tín hiệu bắt bên ngoài.",
      "D.C. versus A.C.: Usually the transducer output has to travel upto a long distance in "
      "practical instrumentation scheme, therefore low level, low frequency A.C. output is not "
      "advisable to be used because 50 Hz stray fields will affect it. High level D.C. output can "
      "be considered, however, which practically is immune to the effect of outside "
      "interferences or pick-ups.")
    P("Trong hệ thống đầu ra A.C. có thể xảy ra dịch pha và điều này phải được tính đến trong hệ "
      "thống đo. Hệ thống đầu ra D.C. không gặp vấn đề này.",
      "In A.C. output system, phase shift may occur and that has to be taken into consideration "
      "in measurement system. D.C. output systems do not face such problem.")
    P("Hệ thống đầu ra D.C. (đặc biệt ở mức thấp) cần bộ khuếch đại thiết bị chất lượng cao. Mặt "
      "khác, hệ thống đầu ra A.C. không cần khuếch đại phức tạp như vậy.",
      "D.C. output system (especially at low level) requires high grade instrumentation amplifier. "
      "On the other hand, A.C. output systems do not require such complicated amplification.")
    P("Đầu ra D.C. (dưới dạng dòng) có thể được biến thành lực bằng cách cho dòng D.C. chạy qua một "
      "cuộn dây đặt trong từ trường. Vì vậy hệ thống đầu ra D.C. loại bỏ được nhu cầu chỉnh lưu nếu "
      "dùng hệ thống đầu ra A.C. Do đó, hệ thống đầu ra D.C. mức thấp cần khuếch đại, còn hệ thống "
      "đầu ra A.C. mức thấp cần cả khuếch đại lẫn chỉnh lưu.",
      "D.C. output (in terms of current) can be converted into force by passing D.C. current "
      "through a coil placed in a magnetic field. Hence D.C. output system eliminates the need of "
      "rectification if A.C. output system is used. Thus, low-level D.C. output system shall "
      "require amplification while low-level A.C. output system shall require both amplification "
      "as well as rectification.")
    P("Nếu hệ thống thiết bị đặt ở vị trí nguy hiểm, nên dùng hệ thống đầu ra D.C. có mức năng "
      "lượng thấp vì lý do an toàn.",
      "If the instrumentation system is located in hazardous locations, it is advisable to use "
      "D.C. output system with low energy level for safety considerations.")
    P("Điện áp so với dòng điện: Hệ thống đầu ra dòng có thể dễ dàng tạo điện áp cao hơn, do đó có "
      "thể miễn nhiễm hơn với ảnh hưởng của điện áp nhiệt và điện áp cảm ứng. Bộ chuyển đổi dòng "
      "đắt hơn bộ chuyển đổi áp, nhưng có thể dùng hiệu quả thiết bị thu rẻ hơn cùng với bộ chuyển "
      "đổi dòng.",
      "Voltage versus current: Current output system can develop higher voltages very easily and "
      "hence can be made more immune to the effect of thermal and inductive voltages. Current "
      "transducers are more expensive than voltage transducers but inexpensive receiver "
      "instrumentation system can be employed effectively in conjunction with current "
      "transducers.")
    P("Hệ thống đầu ra dòng được ưu tiên hơn hệ thống đầu ra áp vì mọi thiết bị thu có thể được nối "
      "nối tiếp mà không có tương tác đáng kể. Mặt khác, hệ thống đầu ra áp cần xem xét cẩn thận "
      "trở kháng đầu ra để tránh hiệu ứng tải.",
      "Current output systems are preferable to voltage output system since all receiver "
      "instruments can be connected in series without significant interactions. On the other "
      "hand, voltage output systems require careful consideration of output impedances to avoid "
      "loading effect.")
    P("Trên thực tế, nhiều thiết bị thu hoạt động bằng điện áp. Điện áp cần thiết được tạo ra bằng "
      "cách cho dòng đầu ra đi qua một điện trở chính xác. Bộ chuyển đổi điện-khí nén hoạt động "
      "bằng điện áp cần cuộn dây được bù nhiệt độ. Trong khi đó, hệ thống đầu ra dòng không cần "
      "sự bù cuộn dây đó.",
      "Practically, many receiver instruments are voltage operated. The required voltage is "
      "developed by passing the current output through a precision register. Voltage operated "
      "electro-pneumatic transducers shall require temperature compensated coil for its "
      "operation. A current output system, however, shall not require such coil compensation.")

    H("(ii) Mức tín hiệu và dải", "(ii) Signal level and range", h4)
    P("Thông lệ là dùng đầu ra chuẩn được chấp nhận rộng rãi là 4 đến 20 mA D.C. cho bộ chuyển đổi. "
      "Đây gọi là hệ thống zero sống vì nó cung cấp cách phát hiện hở mạch.",
      "Normal practice is to use commonly accepted standard output of 4 to 20 mA D.C. for "
      "transducers. This is known as the live zero system because it provides a means of "
      "detecting on open circuit fault.")
    P("Thiết bị thu hoạt động trong dải 0,25 V đến 1,25 V D.C. được tạo ra trên điện trở chính xác "
      "62,5 ôm mắc nối tiếp với đầu ra dòng.",
      "The receiver instruments are operated in the range of 0.25 V to 1.25 V D.C. which is "
      "developed across a 62.5 ohms precision resistor placed in series with the current output.")

    H("(iii) Mức trở kháng đầu ra", "(iii) Output impedance level", h4)
    P("Trở kháng đầu ra là đặc tính của mạch đầu ra bộ chuyển đổi. Việc nạp của các tầng kế tiếp "
      "trong bất kỳ sơ đồ thiết bị nào chủ yếu do trở kháng đầu ra của bộ chuyển đổi quyết định. Để "
      "giảm thiểu hiệu ứng tải, trở kháng đầu ra phải có giá trị nhỏ nhất có thể.",
      "Output impedance is the characteristic of transducer output circuit. Loading of successive "
      "stages in any instrumentation scheme is determined primarily by output impedances of the "
      "transducers. To minimize loading effect, the output impedance should have minimum possible "
      "value.")
    P("Nếu trở kháng đầu ra của bộ chuyển đổi thấp hơn trở kháng tải của các tầng kế tiếp, hệ thống "
      "thể hiện đặc tính của nguồn điện áp không đổi (bộ chuyển đổi đầu ra áp). Nhưng nếu trở kháng "
      "đầu ra cao hơn, nó giống đặc tính của nguồn dòng không đổi (bộ chuyển đổi đầu ra dòng). "
      "Trường hợp thứ ba là khi hai trở kháng này có giá trị tương đương, tức trường hợp truyền "
      "công suất cực đại từ đầu ra bộ chuyển đổi tới hệ thống thiết bị kế tiếp. Tuy nhiên hiệu suất "
      "trong điều kiện này chỉ là 50%.",
      "If the output impedance of a transducer is lower with respect to load impedance of "
      "successive stages, the system exhibits the characteristics of a constant voltage source "
      "(a voltage output transducer). But if the output impedance of transducer is higher, it "
      "resembles the characteristics of a constant current source (a current output transducer). "
      "The third case is when these impendances are of comparable values, i.e. a case of maximum "
      "power transfer from the output of the transducer to the successive instrumentation system. "
      "The efficiency in such condition is, however, only 50%.")

    H("(iv) Xem xét nhiễu", "(iv) Noise considerations", h4)
    P("Dải hữu ích của đầu ra bộ chuyển đổi do nhiễu quyết định. Nhiễu trong bất kỳ hệ thống thiết "
      "bị nào cũng giới hạn độ chính xác của phép đo tín hiệu đầu ra. Bắt, nhiễu xuyên âm, giao thoa "
      "và tạp âm là những tên gọi khác của các dạng nhiễu. Tín hiệu đầu ra bộ chuyển đổi có mức "
      "thấp, do đó hệ thống thiết bị trở nên nhạy hơn với nhiễu. Đường dây điện, máy biến áp, động "
      "cơ, rơ le, bộ nghịch lưu, v.v. là các nguồn nhiễu chính trong môi trường công nghiệp. Thiết "
      "kế tốt sơ đồ thiết bị đòi hỏi bảo vệ đầy đủ khỏi nhiễu.",
      "The useful range of output of a transducer is decided by noise consideration. Noise in any "
      "instrumentation system limits the precision of transducer output signal measurement. "
      "Pickups, crosstalk, interference and hash are the other names of different forms of noise. "
      "The transducer output signal is of low level and, therefore, the instrumentation system "
      "becomes more sensitive to noise. Power lines, transformers, motors, relays, inverters, etc. "
      "are the main sources of noise in industrial environment. A good design of instrumentation "
      "scheme calls for adequate protection from noise.")
    P("Khi hệ thống tín hiệu bộ chuyển đổi đi qua vùng có từ trường thay đổi do đường dây điện, máy "
      "biến áp, v.v., một điện áp thừa được chồng lên nó. Đây gọi là nhiễu điện từ. Khi cáp tín "
      "hiệu bộ chuyển đổi ở gần cáp điện, một tín hiệu A.C. 50 Hz được chồng lên do hiệu điện thế "
      "trên điện dung ghép. Đây gọi là nhiễu tĩnh điện. Nếu trong một bó cặp dây, một cặp mang dòng "
      "xung thì một điện áp được chồng lên cặp kề cận do ghép điện dung. Đây gọi là nhiễu xuyên âm.",
      "When transducer signal system passes through the area of varying magnetic fields due to "
      "powerlines, transformers, etc. a superfluous voltage is superimposed on it. This is known "
      "as electromagnetic noise. When the transducer signal carrying cable is in the vicinity of "
      "power cable, a 50 Hz A.C. signal superimposed due to potential difference across coupling "
      "capacitance. This is known as electrostatic noise. If in a bunch of cable pairs, one pair "
      "of cable carries a pulsating current, then a voltage is superimposed on adjacent pair due "
      "to capacitive coupling. This is known as crosstalk.")
    P("Nhiễu điện từ, nhiễu tĩnh điện và nhiễu xuyên âm thuộc loại Nhiễu chế độ thường (Normal Mode "
      "Noise). Loại nhiễu này còn gọi là Nhiễu chế độ nối tiếp (Series Mode Noise) hoặc Nhiễu ngang "
      "(Transverse Noise). Nó trực tiếp đặt một điện áp lên đầu ra bộ chuyển đổi như một tín hiệu "
      "hợp lệ và xuất hiện như một phần của đầu ra, gây sai số.",
      "Electromagnetic, electrostatic and crosstalk come under the category of Normal Mode Noise. "
      "This type of noise is also known as Series Mode Noise or Transverse Noise. It directly "
      "impresses a voltage upon the transducer output as legitimate signal and appears as part of "
      "transducer output constituting error.")
    P("Mức nhiễu chế độ thường có thể cỡ 10 mV ở 50 Hz trong một lắp đặt công nghiệp điển hình. Đầu "
      "ra của bộ chuyển đổi cặp nhiệt mức thấp xử lý tín hiệu khoảng 5 mV có thể bị ảnh hưởng đáng "
      "kể bởi nhiễu chế độ thường.",
      "The level of normal mode noise can be of the order of 10 mV at 50 Hz in a typical "
      "industrial installation. Output of low-level thermocouple transducer, which handles "
      "signals of around 5 mV, can be significantly affected by the normal mode noise.")
    P("Mặt khác, Nhiễu chế độ chung (Common Mode Noise) làm thay đổi mức điện áp một lượng như nhau "
      "so với đất ở cả hai đầu ra của bộ chuyển đổi. Đây gọi là Nhiễu dọc (Longitudinal Noise). Nó "
      "được đưa vào hệ thống đầu ra bởi các nguồn có một đầu nối đất và đầu kia ghép với mạch thu "
      "bằng điện dung hoặc cảm ứng. Điện áp do máy phát nhiễu tạo ra khi có hai điểm nối đất khác "
      "điện thế trong cùng một vòng là ví dụ về nhiễu chế độ chung.",
      "The Common Mode Noise, on the other hand, changes the voltage level by the same amount "
      "with respect to earth on both the output terminals of the transducer. This is called "
      "Longitudinal Noise. It is injected in the transducer output system by sources having one "
      "terminal grounded and other coupled to the receiver circuit capacitively or inductively. "
      "Voltage produced by a noise generator as the result of having two different potential "
      "grounds in the same loop is an example of common mode noise.")
    P("Trong lắp đặt công nghiệp, dây không nối đất thường có mức nhiễu chế độ chung 4 đến 5 V ở 50 "
      "Hz. Những ảnh hưởng này có thể được loại bỏ bằng cách dùng thiết bị thu có đầu vào vi sai "
      "cung cấp trở kháng lớn giữa các đầu và đất. Tuy nhiên hiện nay, hệ thống thiết bị được thiết "
      "kế để chịu mức nhiễu chế độ chung rất cao khoảng 100 V.",
      "In industrial installation, ungrounded wires often have common mode noise level at 4 to 5 "
      "volt at 50 Hz. These effects can be eliminated by using receiver instrument with "
      "differential input which provides high impedance between the terminals and the ground. "
      "Nowadays, however, instrumentation systems are designed to withstand a very high level of "
      "common mode noise of around 100V.")
    P("Nhiễu chế độ chung chuyển thành nhiễu chế độ thường khi dây tín hiệu có trở kháng khác nhau. "
      "Vấn đề này xuất hiện khi cặp nhiệt được nối vào bộ chuyển đổi qua dây nối dài có trở kháng "
      "khác nhau do kim loại khác nhau. Ảnh hưởng được giảm thiểu bằng cách nối đất cặp nhiệt.",
      "Common mode noise gets converted to normal mode when signal wires have different "
      "impedances. Such problem appears when thermocouple is connected to the transducer through "
      "extension wire having different impedances due to different metals. The effect is "
      "minimized by grounding the thermocouple.")

    H("1.5.3 Đặc tính truyền đạt", "1.5.3 Transfer Characteristics", h3)
    P("Đặc tính truyền đạt xác định phần hoạt động của bộ chuyển đổi mà tại đó sự thay đổi thực tế "
      "từ đầu vào sang đầu ra diễn ra. Đặc tính truyền đạt bao gồm ba tiêu chuẩn hiệu năng có hại "
      "cho hoạt động của bộ chuyển đổi:",
      "Transfer characteristics define that portion of the transducer operation where actual "
      "change from input to output takes place. The transfer characteristic encapsulates three "
      "performance criteria, which are detrimental for transducer operation:")
    U(["Hàm truyền đạt.", "Sai số.", "Ảnh hưởng do thay đổi môi trường."],
      ["Transfer function.", "Error.", "Effects due to environmental changes."])

    H("(i) Hàm truyền đạt", "(i) Transfer function", h4)
    P("Hàm truyền đạt của một đơn vị truyền đạt được định nghĩa là f = po / pi, trong đó po và pi "
      "là mức tín hiệu đầu ra và đầu vào của bộ chuyển đổi.",
      "Transfer function of a transfer unit is defined as f = po / pi, where po and pi are output "
      "and input signal level of the transducer.")
    P("Tương tự, Độ khuếch đại của đơn vị truyền đạt được định nghĩa là sự thay đổi gia tăng của đầu "
      "ra đối với sự thay đổi gia tăng của đầu vào, tức G = Δpo / Δpi. Điều này còn gọi là độ nhạy.",
      "Similarly, Gain of the transfer unit is defined as incremental change in the output with "
      "respect to incremental change in input, i.e. G = Δpo / Δpi. This is also called "
      "sensitivity.")
    E("Hệ số tỉ lệ (S) là nghịch đảo của độ nhạy: S = (Δpi / Δpo) / pi = 1 / G",
      "Scale factor (S) is inverse of sensitivity and is given by S = (Δpi / Δpo) / pi = 1 / G")

    H("(ii) Sai số", "(ii) Error", h4)
    P("Đôi khi các đơn vị bộ chuyển đổi không tuân theo quan hệ hàm truyền đạt như yêu cầu, dẫn đến "
      "sai số. Chẳng hạn, nếu ở một số bộ chuyển đổi đầu ra thu được là po′ thay vì po thì sai số e "
      "được cho bởi e = po′ − po.",
      "Sometimes the transducer units do not obey the transfer function relationship the way it "
      "is required, resulting in error. For instance, if in some transducers, the output obtained "
      "is po′ in place of po then the error e shall be given by e = po′ − po.")
    P("Sai số bộ chuyển đổi có thể được xem theo các cách sau:",
      "Transducer error can be looked upon in following ways:")
    U(["(a) Sai số thang đo,", "(b) Sai số động,", "(c) Sai số do nhiễu và trôi,",
       "(d) Sai số do thay đổi tần số."],
      ["(a) Scale error,", "(b) Dynamic error,", "(c) Error due to noise and drift;",
       "(d) Error due to frequency change."])

    H("(a) Sai số thang đo", "(a) Scale error", h4)
    P("Sai số thang đo được chia thành bốn nhóm.", "Scale error can be divided into four groups:")
    P("<b>Sai số zero:</b> Trong sai số zero, đầu ra lệch khỏi giá trị bình thường một lượng cố định "
      "trong toàn bộ dải thang đo như Hình 1.8.",
      "<b>Zero error:</b> In zero error, the output deviates from its normal value by a fixed "
      "amount throughout the scale range as shown in the Figure 1.8.")
    FIG(8, F.fig_f08())
    P("<b>Sai số độ nhạy:</b> Nếu đầu ra là k po thay vì po trong toàn bộ dải thang đo (với k là "
      "hằng số) thì loại sai số này gọi là sai số độ nhạy như Hình 1.9.",
      "<b>Sensitivity error:</b> If the output is k po in place of po throughout the scale range "
      "(where k is a constant), then this type of error is called sensitivity error as shown in "
      "the Figure 1.9.")
    FIG(9, F.fig_f09())
    P("<b>Sai số không phù hợp:</b> Khi hàm bộ chuyển đổi thực tế khác với hàm bộ chuyển đổi mong "
      "muốn ở hầu hết mọi giá trị đầu vào thì gọi là sai số không phù hợp như Hình 1.10.",
      "<b>Non-conformity error:</b> When the actual transducer function is different from the "
      "desired transducer function for almost all values of input then this type of error is "
      "called non-conformity error as shown in the Figure 1.10.")
    FIG(10, F.fig_f10())
    P("<b>Sai số trễ:</b> Khi có sự khác biệt rõ rệt giữa chiều tăng và chiều giảm của đầu ra bộ "
      "chuyển đổi thì phát sinh sai số trễ. Như Hình 1.11, các giá trị giảm cao hơn các giá trị tăng.",
      "<b>Hysteresis error:</b> When there is a marked difference in increasing order of "
      "transducer output with respect to decreasing order, hysteresis error results. As shown in "
      "the Figure 1.11, the decreasing values are higher than that of the increasing values.")
    FIG(11, F.fig_f11())

    H("(b) Sai số động", "(b) Dynamic error", h4)
    P("Trong hệ thống bộ chuyển đổi mà biến đầu vào liên tục thay đổi theo thời gian, đầu ra không "
      "theo kịp những thay đổi một cách chính xác. Do đó phát sinh độ trễ giữa sự thay đổi đầu vào "
      "và sự thay đổi đầu ra tương ứng. Sai số thu được gọi là sai số động.",
      "In transducer systems where input variable constantly changes with respect to time, the "
      "output becomes incapable of following the changes exactly. Therefore, a lag between the "
      "input change and the corresponding transducer output change results. Error so obtained is "
      "known as dynamic error.")
    P("Bất kỳ mạch bộ chuyển đổi nào chứa phần tử tích lũy năng lượng mắc nối tiếp với điện trở đều "
      "là ví dụ thể hiện loại sai số trên. Nếu một điện áp bước Vi được đặt vào mạch R-C nối tiếp, "
      "điện áp Vt trên tụ sau thời gian T được cho bởi:",
      "Any transducer circuit containing a combination of energy storing element in series with "
      "resistor is an example, exhibiting the type of error described above. If, a step voltage "
      "input Vi is applied to a R-C series circuit, the potential Vt across capacitor after time "
      "T shall be given by:")
    E("Vt = Vi (1 − e^(−T/RC))    ...(1.1)", "Vt = Vi (1 − e^(−T/RC))    ...(1.1)")
    P("trong đó RC là hằng số thời gian.", "where RC is time constant.")
    E("λ = Vi − Vt = Vi · e^(−T/RC)    ...(1.2)",
      "The dynamic error λ = Vi − Vt = Vi · e^(−T/RC).    ...(1.2)")
    P("Khi T nhỏ thì λ nhỏ nhất vì λ là hàm của thời gian.",
      "When T is small, λ is minimum because λ is function of time.")

    H("(c) Sai số do nhiễu và trôi", "(c) Error due to noise and drift", h4)
    P("Mô tả về sai số do nhiễu trong trường hợp đặc tính đầu ra cũng áp dụng cho trường hợp này. "
      "Về trôi, nó có đặc tính dịch chuyển dần đầu ra bộ chuyển đổi khỏi vị trí ban đầu theo thời "
      "gian. Sai số gây ra gọi là sai số do trôi. Vì sai số này chỉ liên quan đến đầu ra của bộ "
      "chuyển đổi nên nó không phụ thuộc vào điều kiện đầu vào.",
      "The description regarding error due to noise outlined in case of output characteristic "
      "apply to this case as well. As far as drift is concerned, it has the characteristic of "
      "gradual shift in transducer output from its original position with respect to time. The "
      "resulting error is called error due to drift. This error being related to the output of "
      "the transducer only, it does not depend upon the input condition.")

    H("(d) Sai số do thay đổi tần số", "(d) Error due to frequency change", h4)
    P("Nhìn chung, bộ chuyển đổi tuyến tính khi đặt đầu vào hình sin cho đầu ra hình sin. Nhưng nếu "
      "tăng tần số đầu vào thì vượt quá một giá trị nhất định, đầu ra bộ chuyển đổi bắt đầu giảm. "
      "Dịch pha giữa đầu vào và đầu ra cũng tăng. Đáp ứng này được thể hiện trong Hình 1.12.",
      "In general, a linear transducer when applied with a sinusoidal input results in sinusoidal "
      "output. But if the frequency of the input is increased, then beyond a particular value, the "
      "transducer output starts dropping. Phase shift between input and output also increases. "
      "This response has been shown in the Figure 1.12.")
    FIG(12, F.fig_f12())

    H("(iii) Ảnh hưởng do thay đổi môi trường", "(iii) Effect due to environmental changes", h4)
    P("Tiêu chuẩn hiệu năng nói chung được chấp nhận cho bộ chuyển đổi thay đổi nhiều do thay đổi "
      "môi trường. Bộ chuyển đổi cần một môi trường ổn định. Nhiễu loạn như trường tĩnh điện và "
      "điện từ lạc ảnh hưởng lớn đến hiệu năng. Tương tự, va đập cơ học và rung, thay đổi nhiệt độ, "
      "áp suất và độ ẩm cũng ảnh hưởng đến hiệu năng. Đôi khi lắp đặt cơ học không ổn định cũng "
      "ảnh hưởng đến hiệu năng. Tuy nhiên, người ta áp dụng các biện pháp phòng ngừa thích hợp để "
      "giảm thiểu những nhiễu loạn không mong muốn trên.",
      "Performance criteria generally accepted for a transducer changes greatly due to "
      "environmental changes. A transducer needs a stable environment. Disturbance like "
      "electrostatic as well as electromagnetic field of stray nature affects the performance to "
      "a great extent. Similarly, mechanical shocks and vibration, temperature, pressure and "
      "humidity changes also affect the performance. Sometimes unstable mechanical mounting also "
      "affects the performance. However, suitable precautions are applied for minimizing the "
      "above unwanted disturbances.")

    # ---------------------------------------------------------------- 1.6
    H("1.6 Phần tử bộ chuyển đổi", "1.6 Transducer Elements")
    P("Phần tử bộ chuyển đổi có thể được mô tả gồm hai phần:",
      "Transducer elements may be described in two parts:")
    U(["(i) Phần tử bộ chuyển đổi sơ cấp và", "(ii) Phần tử bộ chuyển đổi thứ cấp."],
      ["(i) Primary transducer element and", "(ii) Secondary transducer element."])
    P("Phần tử bộ chuyển đổi sơ cấp về bản chất là phần tử cảm biến cơ bản, tiếp xúc trực tiếp với "
      "quá trình cần đo. Phần tử bộ chuyển đổi thứ cấp mặt khác biến những thay đổi của biến do "
      "phần tử sơ cấp cung cấp thành dạng đầu ra thích hợp. Đầu ra này sau đó được dùng để xử lý "
      "tiếp trong sơ đồ thiết bị yêu cầu.",
      "Primary transducer element is essentially the basic sensor element, which is directly in "
      "contact with the process to be measured. Secondary transducer element, on the other hand, "
      "converts the changes in variable, made available by the primary transducer element into a "
      "suitable output form. This output is then used for further processing in the required "
      "instrumentation scheme.")
    P("Phần tử bộ chuyển đổi sơ cấp có thể được chia tiếp thành ba loại chung:",
      "Primary transducer element can be further divided into three general categories:")
    U(["(i) Phần tử chuyển đổi cơ khí,", "(ii) Phần tử chuyển đổi điện,",
       "(iii) Phần tử chuyển đổi quang."],
      ["(i) Mechanical conversion element,", "(ii) Electrical conversion element,",
       "(iii) Optical conversion element."])

    H("1.6.1 Phần tử chuyển đổi cơ khí", "1.6.1 Mechanical Conversion Element", h3)
    P("Trong loại này, một vật thể cơ học là thiết bị có đặc tính lò xo đóng vai trò cảm biến sơ "
      "cấp. Nguồn dẫn động về bản chất là lực cơ học tác dụng theo hướng thẳng và/hoặc hướng tròn. "
      "Có năm loại chính của vật thể cơ học cơ bản có thể dùng làm phần tử cảm nhận sơ cấp, đó là:",
      "In this category, a mechanical object which is a device having spring characteristics "
      "works as primary sensor. The driving source is essentially a mechanical force acting in "
      "linear and/or in circular direction. There are as many as five major types of basic "
      "mechanical objects that can be used as primary sensing element. These are:")
    U(["(i) Lò xo (springs),", "(ii) Thanh xoắn (torsion bar),",
       "(iii) Vòng đo (proving ring),", "(iv) Cánh uốn (flexure arm) và",
       "(v) Dầm công xôn (cantilever beam)."],
      ["(i) Springs,", "(ii) Torsion bar,", "(iii) Proving ring,",
       "(iv) Flexure arm and", "(v) Cantilever beam."])
    P("Ngoài năm phần tử trên, còn có các phần tử khác đang được sử dụng, chủ yếu là phần tử bộ "
      "chuyển đổi áp suất và được xếp cùng loại:",
      "In addition to the above five elements, other elements are also in use which are primarily "
      "pressure transducer elements and are placed in the same category.")
    U(["(vi) Ống Bourdon (Bourdon tube),", "(vii) Màng ngăn (diaphragm),",
       "(viii) Nang (capsule),", "(ix) Ống sóng (bellows)."],
      ["(vi) Bourdon tube,", "(vii) Diaphragm,", "(viii) Capsule,", "(ix) Bellows."])
    P("Bây giờ chúng ta sẽ nghiên cứu lần lượt từng phần tử nêu trên.",
      "Now we shall study the above-mentioned elements in some detail one by one.")

    H("(i) Lò xo", "(i) Springs", h4)
    P("Lò xo được coi là loại phần tử cảm nhận sơ cấp phổ dụng nhất. Nhìn chung, khi một lực được "
      "áp dụng vào lò xo, nó thay đổi hình dạng tùy theo đường tác dụng của lực. Nếu lực áp dụng là "
      "lực nén thì lò xo bị nén. Nếu lực có tính kéo thì lò xo bị kéo dài. Dù đường tác dụng của lực "
      "như thế nào, lò xo luôn chịu một dịch chuyển xác định, và đó là thước đo của lực áp dụng. "
      "Bên cạnh đó, lò xo còn tạo lực phục hồi, là đặc tính của mọi lò xo.",
      "Springs are supposed to be the most universal type of primary sensing elements. In general, "
      "when a force is applied to a spring, it changes its shape depending upon the line of action "
      "of force. If the applied force is compressive, compression in the spring takes place. If "
      "the force is of tensile type, elongation takes place. Whatever may be the line of action "
      "of force; there is a definite displacement experienced in the spring, which is the measure "
      "of the applied force. In addition to that the spring provides restoring force as well, "
      "which is characteristic of any spring.")
    P("Lò xo có hai dạng: xoắn ốc (spiral) và xoắn ống (helical) như Hình 1.13 và Hình 1.14.",
      "Springs may be found in two shapes: spiral and helical as shown in the Figures 1.13 and "
      "1.14.")
    FIG(13, F.fig_f13())
    FIG(14, F.fig_f14())
    P("Độ lệch góc Q trong lò xo hình xoắn ốc có thể thu được từ biểu thức toán học:",
      "Deflection Q in spiral-shaped spring can be obtained by mathematical expression:")
    E("Q = 12 · Td · L / (E · b · t³)    ...(1.3)",
      "Q = 12 · Td · L / (E · b · t³)    ...(1.3)")
    P("trong đó E là mô-đun đàn hồi Young (N/m²), b là chiều rộng lò xo (mét), t là chiều dày lò "
      "xo (mét), L là chiều dài lò xo (mét), Td là mô-men xung lực (N·m).",
      "where E is Youngs modulus of elasticity (N/m2), b is width of spring (metre), t is "
      "thickness of spring (metre), L is length of spring (metre), Td is torque (N m).")
    P("Tương tự, dịch chuyển D trong lò xo hình xoắn ống thu được từ biểu thức:",
      "Similarly, displacement D in helical-shaped spring can be obtained from mathematical "
      "expression:")
    E("D = 8 · Fa · d1³ · n / (Gs · d2⁴)    ...(1.4)",
      "D = 8 · Fa · d1³ · n / (Gs · d2⁴)    ...(1.4)")
    P("trong đó Fa là lực áp dụng (N), d1 là đường kính trung bình của vòng xoắn (mét), d2 là đường "
      "kính dây lò xo (mét), n là số vòng dây và Gs là mô-đun trượt (N/m²).",
      "where Fa is force applied, (N), d1 is mean diameter of coiled spring (metre), d2 is "
      "diameter of spring wire (metre), n is number of wires, Gs is shear modulus (N/m2).")

    H("(ii) Thanh xoắn", "(ii) Torsion bar", h4)
    P("Như tên gọi, thanh xoắn thực chất là phần tử cảm nhận mô-men. Khi một mô-men T = Iδ (trong đó "
      "I là mô-men quán tính và δ là gia tốc góc) được áp dụng vào thanh xoắn, một mô-men xoắn được "
      "tạo ra trong thanh. Mô-men này có xu hướng xoắn thanh và giữ nó ở trạng thái ứng suất xoắn. "
      "Khi mô-men áp dụng được nhả dần, một mô-men phục hồi xuất hiện đưa thanh về trạng thái bình "
      "thường, giải phóng ứng suất. Nguyên lý này được dùng trong thiết kế và chế tạo Ống mô-men "
      "(Torque Tube), bộ phận thiết yếu của bộ chuyển đổi mức dạng vật thể dịch chuyển (Displacer "
      "Type level measuring transducers).",
      "As the name suggests, a torsion bar is in fact a torque-sensing element. When a torque T = "
      "Iδ, (where I is moment of inertia and δ is angular acceleration) is applied to a torsion "
      "bar, a torsional/twisting moment is generated in the torsion bar. This twisting moment "
      "tends to twist the torsion bar and keeps it in twisting stress. When the applied torque is "
      "released slowly, a restoring torque comes into existence, which brings back the torsion bar "
      "to its normal state, thereby releasing the stress. This principle is utilized in design and "
      "fabrication of Torque Tube, which is an essential part of Displacer Type level measuring "
      "transducers.")
    E("Q = 16 · Ta · L / (π · Gs · d³)  radian    ...(1.5)",
      "Q = 16 · Ta · L / (π · Gs · d³) radians    ...(1.5)")
    P("trong đó Ta là mô-men áp dụng (N·m), Gs là mô-đun trượt (N/m²), d là đường kính thanh xoắn "
      "(mét).",
      "where Ta is the torque applied (N m), Gs is the shear modulus (N/m2), d is the diameter of "
      "torsion bar (metre).")

    H("(iii) Vòng đo", "(iii) Proving ring", h4)
    P("Vòng đo hay lực kế vòng là thiết bị cảm nhận lực (một dạng load cell) như Hình 1.15.",
      "Proving ring or a ring dynamometer is a force measuring sensing device (a kind of load "
      "cell) shown in the Figure 1.15.")
    FIG(15, F.fig_f15())
    P("Thực chất đây là phiên bản hiện đại, phát triển của thiết kế ban đầu vốn là load cell dạng "
      "cột. Khi các lực Fa được áp dụng như trong hình, một ứng suất chu vi được sinh ra. Ứng suất "
      "này lại tạo biến dạng nén trên bề mặt trong và biến dạng kéo trên bề mặt ngoài. Căng kế được "
      "dùng để đo các biến dạng này.",
      "This is in fact a modern and developed version of the original design, which has been a "
      "column type load cell. When the forces Fa are applied as indicated in the diagram, a "
      "circumferential stress is generated. This stress in turn creates compressive strains on "
      "the inner surfaces and tensile strains on the outer surfaces. Strain gauges are employed "
      "for measurement of these strains.")
    E("Q = 0.244 · Fa · d³ / (E · b · t²)    ...(1.6)",
      "Q = 0.244 · Fa · d³ / (E · b · t²)    ...(1.6)")
    P("trong đó Fa là lực áp dụng, d là đường kính trung bình, t là chiều dày thành, b là chiều rộng "
      "vòng và E là mô-đun đàn hồi Young.",
      "where Fa is applied force, d is the mean diameter, t is the thickness of wall, b is the "
      "width of the ring, E is Youngs modulus of elasticity.")

    H("(iv) Cánh uốn", "(iv) Flexure arm", h4)
    P("Cánh uốn là một dải thép mỏng, dẻo được bắt bằng hàn vào một vật tự do mà lực áp dụng sẽ tác "
      "dụng lên để gây biến dạng như Hình 1.16.",
      "Flexure arm is a flexible thin steel strip pivoted by brazing onto a free body upon which "
      "the applied force will act for deflection as shown in the Figure 1.16.")
    FIG(16, F.fig_f16())
    P("Phần cơ bản nhất của cánh uốn là nó tạo ra biến dạng bị kìm hãm một cách rất hệ thống. Cánh "
      "uốn được bắt ở cả hai đầu vào vật tự do như hình. Do cánh uốn có kích thước rất nhỏ so với "
      "vật tự do, cuối cùng chính nó nhận lấy biến dạng. Tuy nhiên khi lực được rút đi, cánh uốn "
      "phục hồi trạng thái ban đầu. Ưu điểm đáng chú ý nhất của cánh uốn là chuyển động của nó gần "
      "như không ma sát.",
      "The most fundamental part of a flexure arm is that it creates restrained deflection in a "
      "very systematic manner. The flexure arm is pivoted at both ends to the free body as shown. "
      "The flexure arm being of very very smaller size in comparison to free body shall ultimately "
      "take up the deflection. When the force is withdrawn, however, the flexure restores its "
      "original state. The most notable advantage of a flexure arm is that its movement is more "
      "or less frictionless.")

    H("(v) Dầm công xôn", "(v) Cantilever beam", h4)
    P("Dầm công xôn là kết cấu được cố định cứng ở một đầu, đầu kia tự do dịch chuyển dưới ảnh "
      "hưởng của lực áp dụng. Lực phản ứng sinh ra từ điểm được cố định cứng như Hình 1.17.",
      "A cantilever beam is such a structure, which is rigidly fixed at one end, the other end "
      "being free to move under the influence of an applied force. The resulting reactive force "
      "is generated from the point where it is rigidly fixed as shown in the Figure 1.17.")
    FIG(17, F.fig_f17())
    P("Khi lực Fa được áp dụng như hình ở đầu tự do, một mô-men uốn được phát triển. Độ lớn của mô-"
      "men uốn này tỉ lệ với lực áp dụng Fa. Do mô-men uốn này, đầu cố định của dầm chịu ứng suất ở "
      "cả phần trên và phần dưới của kết cấu. Căng kế có thể được dùng để đo biến dạng kéo ở mặt "
      "trên và biến dạng nén ở mặt dưới. Tuy nhiên, độ lệch lớn nhất quan sát được ở đầu tự do trong "
      "khi biến dạng lớn nhất xảy ra ở đầu cố định. Độ lệch d ở đầu tự do được cho bởi:",
      "When a force Fa is applied (as shown) at the free end, a bending moment is developed. The "
      "magnitude of this bending moment is proportional to the applied force Fa. Due to this "
      "bending moment, the fixed end of the cantilever beam experiences stress on top as well as "
      "bottom portion of the structure. Strain gages may be employed to measure the tensile strain "
      "on top and the compressive strain on bottom of the surfaces. The maximum deflection, "
      "however, shall be observed at the free end while maximum strain shall be experienced at "
      "the fixed end. The deflection d at the free end shall be given by the expression:")
    E("d = 4 · Fa · L³ / (E · b · t³)    ...(1.7)",
      "d = 4 · Fa · L³ / (E · b · t³)    ...(1.7)")
    P("trong đó E là mô-đun đàn hồi Young, Fa là lực áp dụng, b là chiều rộng dầm, t là chiều dày "
      "dầm và L là chiều dài tổng của dầm.",
      "where E is Youngs modulus of elasticity, Fa is the force applied, b is the width of the "
      "cantilever, t is thickness of the cantilever, and L is the overall length of the "
      "cantilever.")
    E("ε = 6 · Fa · L / (E · b · t²)    ...(1.8)",
      "ε = 6 · Fa · L / (E · b · t²)    ...(1.8)")
    P("Nếu muốn có một giá trị ứng suất nhất định ứng với một lực áp dụng Fa cố định, các giá trị L, "
      "b và t có thể được tối ưu bằng kỹ thuật tối ưu thông thường. Điều này cho hiệu năng tốt "
      "nhất có thể.",
      "If it is desired to have a particular value of stress with respect to a fixed applied "
      "force Fa, the value of L, b and t may be optimized by usual optimization techniques. This "
      "will result in the best possible performance.")

    H("(vi) Ống Bourdon", "(vi) Bourdon tube", h4)
    P("Ống Bourdon là phần tử đàn hồi. Chúng được chế tạo từ ống đồng phosphor hoặc thép không gỉ "
      "dẹt hình elíp. Các vật liệu khác đang dùng là monel, đồng thau, đồng beryllium, v.v. Việc "
      "chọn vật liệu phụ thuộc vào dải áp suất, môi trường quá trình, nhiệt độ, tính ăn mòn, độ nhớt, "
      "v.v.",
      "The bourdon tubes are elastic elements. These are fabricated by elliptically flattened tube "
      "of phosphor bronze or stainless steel material. Other materials in use are monel, brass, "
      "beryllium copper, etc. Selection of material depends upon pressure range, process medium, "
      "temperature, corrosive nature, viscosity, etc.")
    P("Một đầu của ống Bourdon được bịt kín, đầu kia hở để chất lỏng đi vào cảm nhận áp suất. Sự đi "
      "vào của chất lỏng có xu hướng chỉnh lại hình dạng của ống. Hiệu quả là đầu bịt kín bị dịch "
      "chuyển. Độ dịch chuyển này tỉ lệ với áp suất do chất lỏng đi vào tác dụng. Vì độ dịch "
      "chuyển quá nhỏ, nó được khuếch đại thêm bằng cơ cấu liên kết và bánh răng để dẫn động tổ "
      "hợp cung và bánh răng nhỏ (sector and pinion). Tổ hợp này nối với kim chỉ thị thích hợp để "
      "chỉ thị áp suất áp dụng.",
      "One end of the bourdon tube is sealed and the other one is open for allowing the fluid to "
      "enter for pressure sensing. Entry of the fluid tends to realign the shape of the bourdon "
      "tube. In effect the tip of the sealed end is displaced. This displacement is proportional "
      "to the pressure exerted by the fluid that entered the bourdon tube. The displacement being "
      "too small, is amplified further by mechanical linkages and gears to drive a sector and "
      "pinion combination. This combination is connected to a suitable pointer for indication of "
      "the applied pressure.")
    P("Ống Bourdon có nhiều ưu điểm so với các phần tử khác, ví dụ rẻ tiền, thiết kế đơn giản và độ "
      "chính xác hợp lý, chấp nhận được. Nhược điểm duy nhất là không đo chính xác được do trễ.",
      "Bourdon tube elements have several advantages over other elements, e.g. they are "
      "inexpensive, have simple design, have reasonable and acceptable accuracy. The only "
      "disadvantage is its inability for precise measurement due to hysteresis.")
    P("Nhìn chung, ống Bourdon có ba dạng: chữ C, xoắn ốc và xoắn ống. Tất cả các dạng này được thể "
      "hiện trong Hình 1.18(a), (b), (c) và (d).",
      "In general, bourdon tubes are available in three different shapes: C-shape, spiral shape "
      "and helical shape. All these shapes have been shown in the Figure 1.18(a), (b), (c) and "
      "(d).")
    FIG(18, F.fig_f18())
    P("<b>Ống Bourdon chữ C.</b> Đây là loại phần tử bộ chuyển đổi ống Bourdon phổ dụng nhất dùng "
      "cho thiết bị cảm nhận áp suất. Tổng góc chắn của cung chữ C có thể tới khoảng 225 °C.",
      "<b>C shape bourdon tube.</b> This is the most universal type of bourdon tube transducer "
      "element used for pressure sensing devices. The total angle subtended by the arc of C shape "
      "may be up to 225C or so.")
    P("Độ dịch chuyển đầu d có thể thu được từ phương trình thực nghiệm:",
      "Tip displacement d may be obtained by use of an empirical equation:")
    E("d = 0.33 · (Pa · L³ / E · t) · (W2 / W1)^0.33 · (D / t)²    ...(1.9)",
      "d = 0.33 · (Pa · L³ / E · t) · (W2 / W1)^0.33 · (D / t)²    ...(1.9)")
    P("trong đó W1 và W2 là chiều dài và chiều rộng tiết diện của ống Bourdon, t là chiều dày vật "
      "liệu, D là đường kính cung của ống, L là chiều dài chu vi, E là mô-đun đàn hồi Young và Pa "
      "là áp suất áp dụng.",
      "where W1 and W2 are the cross-sectional length and breadth of the bourdon tube, t is the "
      "thickness of the material, D is the diameter of the arc of bourdon tube, L is the "
      "circumferential length, E is the Youngs modulus of elasticity and Pa is the applied "
      "pressure.")
    P("Như thấy rõ, biểu thức dịch chuyển đầu là phi tuyến. Trong trường hợp này tuyến tính hóa có "
      "thể thực hiện bằng cơ khí. Độ chính xác của ống Bourdon chữ C dao động từ ± 0,5% đến ± 2,0%.",
      "As is seen clearly, the expression of tip displacement is non-linear. Linearization may be "
      "done by mechanical means in this case. The accuracy of measurement resulted by C shape "
      "bourdon tube ranges from ± 0.5% to ± 2.0%.")
    P("<b>Ống Bourdon xoắn ốc.</b> Phân tích biểu thức 1.9 cho thấy dịch chuyển đầu có thể tăng "
      "bằng cách tăng chiều dài cung L. Giữ tiết diện ống nhỏ và tăng cung thêm vài vòng tạo thành "
      "dạng thường gọi là xoắn ốc. Do đó không cần khuếch đại dịch chuyển đầu vì chính dạng xoắn "
      "ốc đã phóng đại chuyển động. Cách này tránh dùng cơ cấu liên kết và bánh răng dẫn động tổ "
      "hợp cung-bánh răng nhỏ, loại bỏ ảnh hưởng của độ hở do mòn và rách bánh răng.",
      "<b>Spiral shape bourdon tube.</b> An analysis of expression 1.9 reveals that the tip "
      "displacement may be increased by simply increasing the length L of the arc. By keeping the "
      "cross-section of the tube smaller and increasing the arc by a few turns results in a shape "
      "commonly known as spiral. Therefore, the amplification of tip displacement is not required "
      "at all since the spiral shape itself magnifies the movement. In this way use of mechanical "
      "linkages and gears to drive the sector and pinion combination is avoided. This eliminates "
      "the effect of backless that results due to wear and tear of the gears.")
    P("Khi áp suất chất lỏng áp dụng đi vào vòng xoắn, ống mở ra tạo dịch chuyển đầu lớn. Chuyển "
      "động đầu này có thể dùng trực tiếp để chỉ thị mà không cần khuếch đại. Rõ ràng độ chính xác "
      "của thiết kế xoắn ốc cao hơn loại chữ C, khoảng ± 0,5%. Thiết kế này luôn được dùng chế tạo "
      "thiết bị tinh vi có dải đo cực thấp.",
      "When the applied fluid pressure enters the spiral, it uncoils producing large tip "
      "movement. This tip movement may be directly used for indication without any "
      "amplification. As is obvious, the accuracy of spiral type design is superior to that of C "
      "type and is about ± 0.5%. This design is invariably used for manufacturing delicate "
      "instruments of extremely low range.")
    P("<b>Ống Bourdon xoắn ống.</b> Thiết kế xoắn ống tương tự loại xoắn ốc nhưng bền chắc hơn. "
      "Độ dịch chuyển đầu của nó dài hơn loại xoắn ốc. Thiết kế này dùng cho dải áp suất cao hơn. "
      "Khả năng chịu quá tải cực cao nhờ độ bền. Do thể tích lớn có sẵn, không gian bên trong hoạt "
      "động như buồng điện dung. Nếu áp suất chất lỏng cần đo dao động, thiết kế này hấp thụ toàn "
      "bộ dao động và cho dịch chuyển đầu ổn định.",
      "<b>Helical shape bourdon tube.</b> Helical type design is similar to spiral type but is "
      "more robust. The tip displacement for this is longer than that of spiral type. This design "
      "is applicable for higher ranges of pressure. Its over-range capability is extremely high "
      "due to its robustness. Due to higher volumetric space available with the helical shape, "
      "the internal space functions as capacitive chamber. If the fluid pressure under "
      "measurement is fluctuating, this design shall absorb entire fluctuations and will result "
      "is stable tip movement.")
    P("Số vòng xoắn được chọn tùy theo độ lớn áp suất cần đo. Độ chính xác của thiết kế này dao "
      "động từ ± 0,5% đến ± 1%.",
      "The number of turns of the helix is selected depending upon the magnitude of pressure to "
      "be measured. The accuracy of this design ranges from ± 0.5% to ± 1%.")
    P("Nhìn chung, vật liệu chế tạo được chọn tùy theo loại chất lỏng đo và dải áp suất cần đo. Với "
      "môi trường không ăn mòn và ứng dụng áp suất thấp dùng đồng phosphor và đồng beryllium. Với "
      "môi trường ăn mòn và áp suất cao dùng thép không gỉ hoặc monel. Dải tới 40 kg/cm² được coi "
      "là áp suất thấp trong công nghiệp, trong khi dải từ 60 kg/cm² đến 600 kg/cm² hoặc hơn được "
      "coi là áp suất cao.",
      "In general, material of construction selected depends upon the type of measurement fluid "
      "as well as range of pressure to be measured. For non-corrosive atmosphere and low-pressure "
      "application phosphor bronze and beryllium copper are used. For corrosive atmosphere and "
      "high-pressure application, stainless steel or monel are used. Range up to 40 kg/cm2 is "
      "considered to be low pressure in industrial application whereas range from 60 kg/cm2 to "
      "600 kg/cm2 or more is considered to be high pressure.")

    H("(vii) Phần tử màng ngăn", "(vii) Diaphragm element", h4)
    P("Đây là một màng mỏng làm bằng dải tròn kim loại được kẹp chặt ở chu vi. Việc lắp đặt được "
      "thực hiện bằng cách hàn chu vi của màng vào một mặt bích tròn đặc có lỗ có kích thước phù "
      "hợp ở chính giữa. Khi áp suất chất lỏng được áp dụng giữa mặt bích và dải tròn, người ta "
      "quan sát thấy dịch chuyển đo được trong dải, tỉ lệ với áp suất áp dụng. Bố trí dịch chuyển "
      "tuyến tính chủ yếu là do ứng suất uốn phát triển trong miếng phẳng.",
      "It is a thin membrane made of metallic circular strip clamped securely at the periphery. "
      "The installation is performed by welding its periphery on to a solid circular flange with "
      "a hole of appropriate size at the centre of the flange. When the fluid pressure is applied "
      "in between the flange and the circular strip, measurable displacement in the strip is "
      "observed which is proportional to applied pressure. The linear displacement arrangement "
      "is mainly due to bending stress developed in the flat piece.")
    P("Màng ngăn có hai dạng: phẳng và gờ sóng như Hình 1.19. Thiết kế gờ sóng có thể dạng răng "
      "cưa, hình thang hoặc hình sin.",
      "The shape of diaphragm is of two types: flat and corrugated as shown in the Figure 1.19. "
      "The design of corrugation may be of sawtooth, trapezoidal or sinusoidal from.")
    FIG(19, F.fig_f19())
    P("Gờ sóng làm tăng diện tích bề mặt, cho dịch chuyển tổng lớn hơn so với màng phẳng. Thiết kế "
      "chế tạo đúng gờ sóng, hệ thống kẹp và bản đế là tối quan trọng trong thiết bị cảm nhận màng "
      "đơn. Độ dịch chuyển d tại tâm của màng phẳng do áp suất Pa được cho bởi:",
      "The corrugation in the diaphragm increases the surface area, which results in greater "
      "overall displacement in comparison to flat diaphragm. The design accuracy in manufacturing "
      "of correct corrugation, clamping system and the base plate are paramount in a single "
      "diaphragm sensing devices. The displacement d of flat diaphragm at the centre due to "
      "applied pressure Pa is given by:")
    E("d = 0.1875 · Pa · r⁴ · (1 − υ²) / (E · t³)    ...(1.10)",
      "d = 0.1875 · Pa · r⁴ · (1 − υ²) / (E · t³)    ...(1.10)")
    P("trong đó υ là hệ số Poisson, t là chiều dày vật liệu màng và E là mô-đun đàn hồi Young của "
      "vật liệu màng.",
      "where υ is the Poissons ratio, t is the thickness of the diaphragm material and E is "
      "Youngs modulus of elasticity of the material of diaphragm.")
    P("Biểu thức cho độ dịch chuyển tại điểm tâm của màng, giá trị này giảm dần về phía chu vi và "
      "bằng zero ngay sát chu vi màng.",
      "The expression gives the displacement at the centre point of the diaphragm, which goes on "
      "decreasing in magnitude towards the periphery and becomes zero just near the periphery of "
      "the diaphragm.")
    P("Việc dùng màng phẳng bị giới hạn ở độ dịch chuyển nhỏ hơn một nửa chiều dày màng (tới 30% của "
      "t). Quan hệ tuyến tính giữa dịch chuyển và áp suất áp dụng bị giới hạn bởi điều kiện này đối "
      "với màng phẳng. Xét trường hợp dịch chuyển lớn, d được cho bởi biểu thức:",
      "The use of flat diaphragm is limited to a displacement less than the half (upto 30% of t) "
      "of the thickness of the diaphragm. The linear relationship between displacement and the "
      "applied pressure is limited to this restriction for flat diaphragm. Considering the case "
      "of large displacement, d shall be given by expression:")
    E("d³ = 0.648 · Pa · r⁴ / (E · t)    ...(1.11)",
      "d³ = 0.648 · Pa · r⁴ / (E · t)    ...(1.11)")
    P("Biểu thức trên với giá trị υ được lấy là 0,3 cho dịch chuyển lớn, cho thấy rõ tính phi tuyến "
      "giữa áp suất áp dụng Pa và dịch chuyển d sinh ra.",
      "The above expression where the value of υ has been considered 0.3 for larger displacement, "
      "clearly indicates non-linearity between applied pressure Pa and resulting displacement d.")
    P("Để có dịch chuyển lớn hơn (lớn hơn một nửa chiều dày), nên dùng gờ sóng. Các dạng gờ sóng "
      "khác nhau được thể hiện trong Hình 1.20. Màng gờ sóng chỉ dùng cho đo tĩnh vì dễ bị rung do "
      "độ đàn hồi lớn.",
      "For obtaining higher displacement (greater than half of thickness), use of corrugation is "
      "recommended. Various shapes of corrugation have been shown in the Figure 1.20. The "
      "corrugated diaphragms are used for static measurement only. This is because of its "
      "susceptibility to vibration due to large reselience.")
    FIG(20, F.fig_f20())
    P("Nhìn chung, vật liệu dùng chế tạo màng ngăn cũng là vật liệu dùng cho ống Bourdon. Tuy nhiên "
      "trong công nghiệp, cao su neoprene (tẩm nylon) và vật liệu Teflon cũng được dùng. Với dịch "
      "vụ ăn mòn và áp suất cao, vật liệu như SS316 L, Hastelloy C, Monel, v.v. cũng được sử dụng.",
      "In general, the materials used for manufacture of diaphragms are those used for bourdon "
      "tubes as well. In industrial application, however, neoprene rubber (nylon impregnated) and "
      "Teflon materials are also used. For corrosive and high-pressure services, materials like "
      "SS316 L, Haslelloy c, Monel, etc. are also in use.")

    H("(viii) Phần tử nang", "(viii) Capsule element", h4)
    P("Hai màng gờ sóng giống hệt nhau được hàn kín với nhau ở chu vi tạo thành phần tử nang màng. "
      "Rõ ràng cấu trúc này nhân đôi dịch chuyển so với màng đơn. Một đầu được giữ hở để áp dụng "
      "áp suất chất lỏng. Đầu kia được nối thích hợp để lấy dịch chuyển.",
      "Two identical corrugated diaphragms sealed together at the periphery form a diaphragm "
      "capsule element. Obviously, this construction doubles the displacement with respect to "
      "single diaphragm. One end is kept open for applying the fluid pressure. The other end is "
      "connected suitably for taking up the displacement.")
    P("Cấu trúc được thể hiện trong Hình 1.21. Độ dịch chuyển tỉ lệ với hiệu giữa áp suất áp dụng "
      "Pa và áp suất bên ngoài tác dụng lên nang. Tùy theo áp suất áp dụng cần đo, việc hàn kín chu "
      "vi được thực hiện bằng hàn thiếc, hàn cứng hoặc hàn. Sau khi chế tạo, người ta ủ giảm ứng "
      "suất để ổn định.",
      "The construction has been shown in the Figure 1.21. The displacement is proportional to "
      "difference of applied pressure Pa and the outside pressure acting on the capsule element. "
      "Depending upon the applied pressure to be measured, the sealing on the periphery is done "
      "by soldering, brazing or welding. After fabrication stress relieving is carried out for "
      "stability.")
    FIG(21, F.fig_f21())
    P("Để tăng thêm dịch chuyển, hai hoặc nhiều nang có thể được nối với nhau bằng các vòng đệm.",
      "To further enhance the displacement, two or more capsules may be joined together by means "
      "of spacers.")

    H("(ix) Phần tử ống sóng", "(ix) Bellows element", h4)
    P("Nhìn sơ qua, ống sóng trông như các phần tử nang xếp chồng lên nhau như Hình 1.22. Nhưng cấu "
      "trúc bên trong của ống sóng hoàn toàn khác. Đây là những vỏ mỏng, dẻo có các nếp gấp như "
      "Hình 1.22. Một đầu được bịt kín để lấy dịch chuyển. Đầu kia hở ra khí quyển để nhận áp suất "
      "chất lỏng áp dụng.",
      "At one glance, the bellows look like staggered capsule elements put on one after another "
      "as shown in the Figure 1.22. But the internal construction of the bellows are quite "
      "different. These are thin flexible shells with convolutions as shown in the Figure 1.22. "
      "One end has been sealed for taking up the displacement. The other end is open to "
      "atmosphere for taking up the fluid pressure applied.")
    FIG(22, F.fig_f22())
    P("Việc chọn số nếp gấp rất quan trọng vì nó phụ thuộc hoàn toàn vào dải áp suất áp dụng. Độ "
      "dịch chuyển d do ống sóng tạo ra khi áp suất Pa được áp dụng được cho bởi biểu thức:",
      "The choice of number of convolutions is important in the sense that it is entirely "
      "dependent upon the range of pressure applied. The displacement d generated by the bellows "
      "when a pressure Pa is applied shall be given by the expression:")
    E("d = N · Ae · Pa · ra³ / (E · t³)    ...(1.12)",
      "d = N · Ae · Pa · ra³ / (E · t³)    ...(1.12)")
    P("trong đó N là số nếp gấp, Ae là diện tích tổng hiệu dụng của ống sóng, ra là bán kính trung "
      "bình, E là mô-đun đàn hồi Young của vật liệu và t là chiều dày trung bình của vật liệu chế "
      "tạo ống.",
      "where N is the number of convolutions on the bellows, Ae is the effective overall area of "
      "the bellows, ra is the average radius, E is Youngs modulus of elasticity of material of "
      "bellows and t is the average thickness of the material of which the bellows have been "
      "constructed.")
    P("Rõ ràng từ cấu trúc, ống sóng có thể tạo dịch chuyển lớn nhưng nhạy với rung. Dịch chuyển "
      "lớn có thể bị kìm bằng lò xo hiệu chuẩn để chỉ dùng một dải dịch chuyển mong muốn.",
      "As is obvious from the construction of the bellows element, it can generate large "
      "displacement but is sensitive to vibration. The larger displacement can be restrained by "
      "use of a calibrated spring so that only a desired range of displacement may be utilized.")
    P("Hai ống sóng giống hệt nhau khi nối cơ học với nhau, dịch chuyển tương đối sinh ra tỉ lệ với "
      "hiệu của hai áp suất áp dụng riêng biệt. Bố trí này hữu ích trong đo áp suất tuyệt đối, áp "
      "suất đo hoặc cả áp suất chênh.",
      "Two identical bellows when connected together mechanically, the resultant relative "
      "displacement produced by them shall be proportional to the difference in the two pressures "
      "applied separately to the two respective bellows. Such an arrangement may be useful in "
      "measurement of absolute pressure, or gage pressure or even differential pressure.")
    P("Ưu điểm của phần tử ống sóng:", "The advantages of bellows element are:")
    U(["(i) Cấu trúc đơn giản,", "(ii) Rẻ tiền,",
       "(iii) Ứng dụng rộng (đo áp suất thấp, trung bình và cao, áp suất tuyệt đối lẫn áp suất đo),",
       "(iv) Độ chính xác khoảng 0,5% và giảm cả trôi lẫn trễ."],
      ["(i) Simple construction,", "(ii) Inexpensive,",
       "(iii) Wide application (to measure low, medium and high pressure, absolute pressure as "
       "well as gage pressure),",
       "(iv) Accuracy accounts to 0.5% and reduction in drift as well as hysteresis."])
    P("Nhược điểm gồm:", "The disadvantages include:")
    U(["(i) Không phù hợp cho đo động,",
       "(ii) Cần bù nhiệt độ để giảm sai số do thay đổi môi trường."],
      ["(i) Unsuitable for dynamic measurement,",
       "(ii) Temperature compensation is required to minimize error in measurement due to "
       "ambient changes."])

    H("1.6.2 Phần tử chuyển đổi điện", "1.6.2 Electrical Conversion Element", h3)
    P("Trong hệ thống này, sự biến đổi đặc tính của chất do năng lượng cơ hoặc nhiệt gây ra được "
      "phản ánh lại dưới dạng thay đổi của tính chất điện. Những thay đổi này thực chất là thay đổi "
      "điện trở, cảm ứng hoặc điện dung của hệ thống điện. Ngoài những thay đổi chính này, trong "
      "một số trường hợp một lượng điện áp nhỏ (cỡ mV) cũng có thể được sinh ra khi thay đổi xảy ra "
      "do thay đổi năng lượng nhiệt, tức thay đổi nhiệt độ. Dựa trên nguyên lý rộng này, nhiều cơ "
      "chế bộ chuyển đổi thực tế đã được phát triển. Các cơ chế này cũng thuộc phần tử cảm nhận sơ "
      "cấp và có thể kể ra:",
      "In this system, variation in the features of substances brought about by mechanical or "
      "thermal energy may be reflected back in terms of changes in electrical property. These "
      "changes in effect are the changes in resistance, inductance or capacitance of the "
      "electrical system. Leaving aside these major changes, in some cases, small amount of "
      "voltages (of the order of mV) may also be induced when the changes take place due to change "
      "in thermal energy, i.e. change in temperature. Based on this broad principle, several "
      "practical transducer mechanisms have been developed. These mechanisms also come under "
      "primary sensing elements and can be enumerated as:")
    U(["(i) Phần tử căng kế (strain gage),",
       "(ii) Đầu dò nhiệt độ điện trở (RTD),",
       "(iii) Phần tử cặp nhiệt điện (thermocouple),",
       "(iv) Phần tử nhiệt trở (thermistor),",
       "(v) Hệ thống cảm ứng biến đổi,",
       "(vi) Hệ thống điện dung biến đổi,",
       "(vii) Hệ thống áp điện,",
       "(viii) Phần tử bộ chuyển đổi hiệu ứng Hall."],
      ["(i) Strain gage elements,",
       "(ii) Resistance temperature detectors (RTD),",
       "(iii) Thermocouple elements,",
       "(iv) Thermistor elements,",
       "(v) Variable inductance system,",
       "(vi) Variable capacitance system,",
       "(vii) Piezoelectric system,",
       "(viii) Hall effect transducer element."])

    H("1.6.3 Phần tử căng kế", "1.6.3 Strain Gage Element", h3)
    P("Như tên gọi, căng kế nghĩa là đo qua biến dạng. Quan hệ giữa lực/trọng lượng áp dụng và độ "
      "giãn dài được đặc trưng bằng biến dạng sinh ra. Biến dạng được định nghĩa là sự thay đổi "
      "(ΔL) quan sát được trên chiều dài ban đầu L cho mỗi đơn vị chiều dài tổng của chất. Vì vậy "
      "biến dạng có thể biểu diễn là ε = ΔL / L microstrain (một microstrain bằng một micromet trên "
      "mét).",
      "As the name suggests, strain gage means gaging through strain. The relation between "
      "applied force/weight and elongation is characterized in terms of resultant strain. The "
      "strain is defined as the change (ΔL) observed in original length L per unit of overall "
      "length of the substance. Hence, strain can be expressed as ε = ΔL / L microstrains (one "
      "microstrain being equal to one micrometre/metre).")
    P("Biểu thức thông thường của ứng suất và biến dạng khi thực hiện thử kéo và/hoặc nén đơn giản "
      "về độ bền vật liệu là:",
      "The usual expression of stress and strain while performing simple tension and/or "
      "compression test for strength of material is given by:")
    E("ε = σ / E    ...(1.13)", "ε = σ / E    ...(1.13)")
    P("trong đó ε là biến dạng, σ là ứng suất và E là mô-đun đàn hồi Young. Quan hệ này gần như "
      "tuyến tính dưới giới hạn đàn hồi.",
      "where ε is strain, σ is stress and E is Youngs modulus of elasticity. This relation is "
      "more or less linear below elastic limit.")
    P("Do áp dụng lực/trọng lượng, tiết diện của chất thay đổi. Tác động này gây thay đổi điện trở, "
      "cảm ứng và điện dung. Đối với hệ thống căng kế, thay đổi điện trở quan trọng hơn. Vì vậy "
      "người ta xét tỉ số thay đổi điện trở trên đơn vị điện trở tổng so với thay đổi chiều dài "
      "trên đơn vị chiều dài tổng, tức (ΔR/R)/(ΔL/L).",
      "Due to application of force/weight, change in cross-section takes place in the substance. "
      "This action brings about changes in resistance, inductance and capacitance. For strain "
      "gaging system, change in resistance is more important. Therefore, ratio of change in "
      "resistance per unit overall resistance with respect to change in length per unit overall "
      "length is observed and represented by the expression (ΔR/R)/(ΔL/L); where ΔR is change in "
      "resistance, R is overall resistance, ΔL is change in length, L is overall length.")
    P("Tỉ số này gọi là Hệ số gage (Gs) và được biểu diễn bởi:",
      "This ratio is called Gage factor (Gs) and is represented by the expression:")
    E("Gs = (ΔR/R)/(ΔL/L) = 1 + 2υ + (Δρ/ρ)/(ΔL/L)    ...(1.14)",
      "Gs = (ΔR/R)/(ΔL/L) = 1 + 2υ + (Δρ/ρ)/(ΔL/L)    ...(1.14)")
    P("trong đó υ là hệ số Poisson và ρ là điện trở suất riêng của vật liệu dây (ohm-mét). Biểu "
      "thức này được suy từ phương trình gốc R = ρ L/A, với các thay đổi gia tăng trở thành:",
      "where υ is the Poissons ratio, ρ is the specific resistance of wire material (ohm-mt). "
      "This expression has been deduced from original equation R = ρ L/A which for incremental "
      "changes reduces to:")
    E("ΔR/R = Δρ/ρ + ΔL/L − ΔA/A    ...(1.15)",
      "ΔR/R = Δρ/ρ + ΔL/L − ΔA/A    ...(1.15)")
    P("Biểu thức này nói rằng với một thay đổi ứng suất nhất định, sự thay đổi hiệu dụng của R được "
      "bổ sung bởi thay đổi tỉ lệ của chiều dài L, diện tích tiết diện A và cả điện trở suất ρ. Với "
      "tiết diện tròn, thay đổi diện tích A có thể biểu diễn qua thay đổi đường kính D là ΔA/A = "
      "2 ΔD/D nếu các thay đổi rất nhỏ. Theo lập luận tương tự, ΔD/D = −υ ΔL/L.",
      "This expression states that for a particular change in stress, the effective change in R "
      "is supplemented by proportionate change in length L, cross-sectional area A and also "
      "resistivity ρ. For a circular cross-sectional shape, the change in area A may be "
      "represented in terms of change in its diameter D by the following expression if the "
      "changes are extremely small: ΔA/A = 2 ΔD/D. On similar argument, ΔD/D = −υ ΔL/L.")
    E("(ΔR/R)/(ΔL/L) = 1 + 2υ + (Δρ/ρ)/(ΔL/L)    ...(1.16)",
      "(ΔR/R)/(ΔL/L) = 1 + 2υ + (Δρ/ρ)/(ΔL/L)    ...(1.16)")
    P("Trong biểu thức trên, số hạng 2υ biểu diễn ảnh hưởng của thay đổi kích thước còn số hạng "
      "(Δρ/ρ)/(ΔL/L) biểu diễn hiệu ứng áp điện trở. Hiệu ứng áp điện trở được định nghĩa là thay "
      "đổi điện trở suất theo biến dạng. Phương trình (1.16) cho thấy thay đổi điện trở do biến "
      "dạng không chỉ do thay đổi kích thước mà còn do thay đổi điện trở suất. Thực tế giá trị hệ "
      "số Poisson gần như cố định (0,3) với hầu hết vật liệu làm căng kế. Nếu hiệu ứng áp điện trở "
      "rất nhỏ có thể bỏ qua, biểu thức hệ số gage rút gọn còn:",
      "In the above expression, the term 2υ represents the effect of dimensional changes whereas "
      "the term (Δρ/ρ)/(ΔL/L) represents piezoresistive effect. Piezoresistive effect is defined "
      "as change in resistivity with respect to strain. The equation (1.16) signifies that "
      "changes in resistances (due to strain) is not only because of changes in dimension but "
      "also due to change in resistivity. In fact, value of Poissons ratio is more or less fixed "
      "(being 0.3) for most of the materials used for the strain gage. In this light, if the "
      "piezoresistive effect can be considered exceptionally small then it can be neglected. "
      "Eventually, the expression for gage factor would be reduced to:")
    E("Gs = 1 + 2υ    ...(1.17)", "Gs = 1 + 2υ    ...(1.17)")
    P("Bảng dưới đây cho giá trị Gs của một số vật liệu chọn lọc.",
      "The table below indicates value of Gs for some of the selected materials.")
    P("<b>Bảng 1.1.</b> Hệ số gage của một số vật liệu.",
      "<b>Table 1.1.</b> Gage factor of selected materials.")
    TB(_h(vi, en, 1), _TBL11)
    P("Hệ số gage xác định độ nhạy của căng kế. Hình 1.23(b) (biến dạng nén) và 1.23(c) (biến dạng "
      "kéo) cho thấy hai điều kiện khác nhau của vật liệu do biến dạng so với điều kiện ban đầu "
      "không biến dạng Hình 1.23(a). Ta thấy dưới áp lực chiều dài L1 giảm còn dưới lực kéo chiều "
      "dài L1 tăng. Ngược lại, kết quả ngược lại xảy ra với diện tích tiết diện A1.",
      "Gage factor specifies sensitivity of a strain gage. Figure 1.23(b) (strain under "
      "compression) and 1.23(c) (strain under tension) show two different conditions of material "
      "changes due to strain with respect to the original condition unstrained as shown in Figure "
      "1.23(a). We observe that under compression there is decrease in length L1 whereas under "
      "tension there is an increase in length L1. On the other hand, opposite result is obtained "
      "in case of changes in cross-sectional area A1.")
    FIG(23, F.fig_f23())

    H("Các loại phần tử căng kế", "Types of strain gage elements", h4)
    U(["(a) Căng kế dây (wire strain gages): (i) loại dây dán (bonded wire), (ii) loại lá dán "
       "(bonded foil), (iii) loại không dán (unbonded).",
       "(b) Căng kế màng kim loại mỏng (thin metal film strain gage).",
       "(c) Căng kế bán dẫn (semiconductor type strain gage)."],
      ["(a) Wire strain gages: (i) Bonded wire type, (ii) Bonded foil type, (iii) Unbonded type.",
       "(b) Thin metal film strain gage.",
       "(c) Semiconductor type strain gage."])

    H("(a) Căng kế dây", "(a) Wire strain gage", h4)
    P("Căng kế dây được chế tạo từ dây điện trở mịn hoặc lá gọi là lưới. Các tính chất mong muốn "
      "của dây điện trở để dùng làm phần tử căng kế là:",
      "Wire strain gages are made of fine resistance wire or foil called grid. The desirable "
      "properties for a resistance wire to be able to be used as a strain gage element are:")
    U(["Phải cho hệ số gage cao, dẫn đến độ nhạy tăng.",
       "Giá trị điện trở chọn đủ lớn để át ảnh hưởng không mong muốn do thay đổi điện trở ở các "
       "phần khác của mạch. Tuy nhiên xét đến độ nhạy thì cần sự thỏa hiệp.",
       "Có hệ số nhiệt của điện trở thấp, cho sai số nhỏ do thay đổi nhiệt độ.",
       "Có ảnh hưởng trễ nhỏ nhất trong đáp ứng.",
       "Có sự thay đổi điện trở tuyến tính theo biến dạng sinh ra.",
       "Đáp ứng tần số nằm trong dải chấp nhận được vì căng kế cũng dùng cho đo động."],
      ["It should provide high gage factor which ultimately results in increased sensitivity.",
       "The value of resistance selected should be high enough in order to swamp out the "
       "undesirable effects due to variations in resistance in different parts of the circuit. "
       "However, this consideration decreases the sensitivity and therefore, a compromise is "
       "called for.",
       "It should have low resistance temperature coefficient. This results in lower error due "
       "to temperature changes.",
       "It should have minimum possible hysteresis effect in its response.",
       "It should have linear variations in resistance with respect to strain developed.",
       "Its frequency response should be in the acceptable range since strain gages are employed "
       "for dynamic measurement as well."])
    P("<b>Vật liệu nền.</b> Nơi gắn cấu trúc lưới của căng kế gọi là vật liệu nền (backing "
      "material). Vật liệu nền vừa cách điện vừa bảo vệ khỏi hư hỏng vật lý. Việc chọn vật liệu "
      "nền liên quan đến nhiệt độ làm việc của căng kế. Bảng 1.2 cho các vật liệu dùng trong công "
      "nghiệp ứng với nhiệt độ làm việc khác nhau.",
      "<b>Backing material.</b> The base where the grid structure of the strain gage is attached, "
      "called backing material. Backing material provides insulation as well as protection "
      "against physical damage. The selection of backing material is related to working "
      "temperature of the strain gage. Table 1.2 indicates different material used in industrial "
      "application for backing against different working temperature.")
    P("<b>Bảng 1.2.</b> Vật liệu nền và dải nhiệt độ làm việc.",
      "<b>Table 1.2.</b> Backing materials and working temperature ranges.")
    TB(_h(vi, en, 2), _TBL12)
    P("Phân loại căng kế dây dựa trên phương pháp chế tạo và được mô tả dưới đây. Hình 1.24 cho các "
      "dạng khác nhau của căng kế dây.",
      "The classification of wire strain gages are based on the method of fabrication and is "
      "described below. Figure 1.24 shows different forms of wire strain gages.")
    FIG(24, F.fig_f24())
    P("<b>(i) Căng kế dây dán.</b> Khi phần tử dây được dán lên bề mặt mẫu thử, bố trí này gọi là "
      "căng kế dây dán. Việc dán được thực hiện bằng vật liệu dán. Vật liệu dán là chất keo giữ "
      "căng kế chắc chắn lên mẫu thử. Việc chọn và dùng keo cụ thể rất quan trọng. Chức năng của "
      "keo là truyền biến dạng sinh ra trong mẫu thử tới phần tử cảm nhận. Bảng 1.3 liệt kê một số "
      "keo dùng trong công nghiệp.",
      "<b>(i) Bonded wire type strain gage.</b> When the gage element in the form of wire is "
      "bonded on to the surface of the specimen being tested, the arrangement is called bonded "
      "wire type strain gage. Bonding is carried out by means of bonding materials. The bonding "
      "materials are adhesives to fix the strain gage securely on to the testing specimen. The "
      "selection and application of particular adhesive is critical. The function of adhesive is "
      "to transmit the strain developed in the testing specimen to the sensing element. Hence the "
      "selection of particular adhesive for particular application is critical. Table 1.3 "
      "indicates some of the adhesives, which are in industrial use.")
    P("<b>Bảng 1.3.</b> Keo dùng trong công nghiệp.",
      "<b>Table 1.3.</b> Adhesives used in industry.")
    TB(_h(vi, en, 3), _TBL13)
    P("<b>(ii) Căng kế lá dán.</b> Khi dùng phần tử lá kim loại thay cho dây, bố trí gọi là căng kế "
      "lá kim loại dán. Ưu điểm của loại lá dán so với dây dán là:",
      "<b>(ii) Bonded foil type strain gage.</b> When the element in the form of metal foil is "
      "used in place of wire, the arrangement is called bonded metal foil strain gage. The "
      "advantages of bonded foil type over bonded wire type are:")
    U(["Nhờ diện tích bề mặt tăng, cấu trúc này tản nhiệt tốt hơn.",
       "Việc dán chắc chắn hơn.",
       "Chế tạo thuận tiện hơn.",
       "Căng kế cùng kỹ thuật dán hiện có bao phủ dải nhiệt độ rộng, từ −269 đến +816 °C."],
      ["Due to increased surface area, this construction has greater heat dissipation capacity.",
       "Bonding is more superior.",
       "Manufacturing is more convenient.",
       "Strain gages along with available bonding techniques cover a wide temperature range, "
       "i.e. from -269 to + 816C."])
    P("<b>(iii) Căng kế không dán.</b> Như tên gọi, loại này không cần keo dán. Thực chất có hai bộ "
      "gồm bốn cuộn dây làm bằng vật liệu căng kế có độ bền kéo cao. Chúng được quấn quanh bốn trụ "
      "được bố trí sao cho một bộ cố định và bộ kia di động. Nhờ bố trí này, các cuộn dây chịu ứng "
      "suất khác nhau khi có trọng lực/lực áp dụng. Toàn hệ thống nối vào cầu Wheatstone. Cầu được "
      "cân bằng ở biến dạng ban đầu vì chưa có thay đổi điện trở. Khi có lực/áp suất/trọng lượng "
      "tác dụng lên các trụ, điện trở tăng ở hai dây và giảm tương ứng ở hai dây kia. Cầu mất cân "
      "bằng, cho điện áp lệch tỉ lệ với áp suất/lực/trọng lượng áp dụng. Điện áp lệch điển hình từ "
      "20 đến 50 mV thu được khi điện áp cấp cho cầu từ 5 đến 10 V, điện trở các trụ từ 120 đến "
      "1000 ôm.",
      "<b>(iii) Unbonded type strain gages.</b> As the name suggests, it does not need any "
      "bonding. In fact there are two sets of four windings made of strain gage material having "
      "high tensile strength. These are wound around on four posts arranged in such a way that "
      "one set is stationary and the other set is movable. Due to this arrangement, the windings "
      "experience a difference in stress for an applied weight/force. The whole system is then "
      "connected to a Wheatstone bridge. The bridge is balanced under initial strain because "
      "there is no resistance change under applied weight/force/pressure on the posts, there is "
      "an increase in resistance in two wires and a corresponding decrease in the remaining two "
      "wires. This results in unbalance of bridge and hence an out of balance voltage "
      "proportional to applied pressure/force/weight is obtained. A typical out of balance "
      "voltage between 20 and 50 mV is practically obtained when the supply voltage to the bridge "
      "is in between 5 and 10 volt, the resistance of the posts being from 120 to 1000 ohm.")
    P("<b>Ưu điểm.</b> (i) Cấu trúc đặc biệt của căng kế dây không dán không cho lực ngang ảnh hưởng "
      "đến đầu ra nên sai số đo được giảm thiểu. (ii) Trễ vàcreep thấp vì không dùng nền và keo.",
      "<b>Advantages.</b> (i) The special constructional features of the unbonded wire strain "
      "gage do not allow transverse forces to affect the output and hence the error of measurement "
      "in minimized. (ii) It has low hysteresis and creep since no backing and bonding techniques "
      "are applied.")

    H("(b) Căng kế màng kim loại mỏng", "(b) Thin metal film strain gage", h4)
    P("Căng kế màng kim loại mỏng là đổi mới công nghệ mới nhất. Trong công nghệ này, màng mỏng "
      "của kim loại chất lượng cao như vàng, bạch kim, niken hoặc cả nhôm được tạo trên nền cách "
      "điện. Việc tạo màng được thực hiện trong chân không bằng phương pháp bay hơi nhiệt. Sau đó "
      "nền được gắn vào mẫu đàn hồi. Quá trình bay hơi và ngưng tụ được điều khiển để cho hình dạng "
      "mong muốn.",
      "Thin metal film strain gage is the latest technological innovation. In this technology, "
      "thin films of high-grade metals such as gold, platinum, nickel or even aluminium are formed "
      "onto an insulating substrate. The formation is carried out in vacuum by thermal "
      "evaporation process. The substrate is then attached to the elastic specimen. The process "
      "of vaporization and condensation are controlled to give desired shape.")
    P("Trong phương pháp này, điện trở suất riêng của màng RF là tính chất cơ bản quan trọng để tính "
      "hệ số gage. RF liên hệ với điện trở màng RG qua RF = RG · b/l, trong đó b và l là chiều rộng "
      "và chiều dài màng. RG cũng được cho bởi RG = ρF · l/A, với ρF và A là điện trở suất và diện "
      "tích tiết diện của màng. Do đó RF = ρF/t (với t là chiều dày).",
      "In this metal film gaging, the specific resistance of the film RF is a basic property of "
      "the film and is important for gage factor calculation. The RF is related to the resistance "
      "of the film RG by the relation RF = RG · b/l, where b and l are the width and the length of "
      "the film respectively. RG is also given by the conventional relation RG = ρF · l/A where "
      "ρF and A as usual the resistivity and the cross-sectional area of the thin film. Hence the "
      "expression for RF takes the form RF = ρF/t [t is thickness].")
    E("RF = ρF / t    ...(1.19)", "RF = ρF / t    ...(1.19)")
    P("Quan hệ này cho thấy có thể thiết kế căng kế điện trở cao bằng cách chọn kích thước màng "
      "nhỏ hơn. Kết quả là độ nhạy cải thiện và công suất tiêu thụ giảm. Nhờ vậy công nghệ thiết "
      "kế này là giải pháp thay thế tốt nhất cho căng kế lá dán.",
      "This relation indicates that high resistance gages can be designed by selecting smaller "
      "dimension of film. The result of such design shall be improved sensitivity and reduced "
      "power consumption. In this way, this design technology is the best alternative to bonded "
      "foil strain gages.")
    P("Ưu điểm: (i) hoạt động rất ổn định trong dải nhiệt độ từ −200 đến +400 °C; (ii) điện trở "
      "gage cao, hệ số gage cao, độ nhạy cao và độ chính xác cao; (iii) cấu trúc bền chắc; (iv) trễ "
      "vàcreep nhỏ nhất.",
      "Advantages: (i) The thin film gage has very stable operation over temperature range from "
      "-200 to + 400C. (ii) This has higher gage resistance, higher gage factor, higher "
      "sensitivity and higher accuracy. (iii) Its construction is rugged. (iv) It shows minimum "
      "possible hysteresis and creep.")
    FIG(25, F.fig_f25())

    H("(c) Căng kế bán dẫn", "(c) Semiconductor strain gage", h4)
    P("Nguyên lý thiết kế căng kế bán dẫn hoàn toàn khác căng kế điện trở kim loại. Nó dùng tính "
      "chất áp điện trở của vật liệu bán dẫn. Ở căng kế kim loại, thay đổi biến dạng phát sinh do "
      "thay đổi kích thước chứ không do thay đổi điện trở suất. Nhưng ở căng kế bán dẫn, chính điện "
      "ở suất của vật liệu bán dẫn chịu trách nhiệm thay đổi biến dạng. Sự thay đổi điện trở do "
      "biến dạng lớn hơn nhiều so với căng kế kim loại, có khi tới 100 lần.",
      "The principle behind the design of semiconductor strain gages is completely different from "
      "the metal resistance strain gages. It employs the piezoresistive property of the "
      "semiconductor material. In metal resistance strain gages, change in strain is developed due "
      "to change in dimension and not due to change in resistivity of the material. But in "
      "semiconductor strain gage, it is the resistivity of the semiconductor material which is "
      "responsible for change in strain. The change in resistance due to strain is quite large "
      "with respect to metal resistance strain gage. In some cases the change is even 100 times "
      "more.")
    E("Gs = (ΔR/R)/(ΔL/L) = 1 + 2υ + M    ...(1.20)",
      "Gs = (ΔR/R)/(ΔL/L) = 1 + 2υ + M    ...(1.20)")
    P("trong đó M là tích của hệ số áp điện trở dọc theo trục căng kế và mô-đun đàn hồi Young của "
      "căng kế theo chiều dài. Hình 1.26 cho thấy nhiều dạng chế tạo của loại căng kế này.",
      "where M is the product of coefficient of piezo-resistance along the axis of gage and "
      "Young's modulus of elasticity of the gage along its length. Figure 1.26 shows a variety of "
      "construction of this type of gage.")
    FIG(26, F.fig_f26())
    P("Vật liệu thường dùng chế tạo căng kế bán dẫn là silic pha tạp có điện trở suất 2 × 10⁻⁴ "
      "ohm-mét. Tiếp điểm điện làm bằng dây vàng. Kỹ thuật nền giống như căng kế dây hoặc lá "
      "thông thường. Vì căng kế bán dẫn rất dễ vỡ nên phải cẩn thận khi xử lý.",
      "The common material used for manufacture of semiconductor strain gage is silica doped with "
      "impurity having resistivity of 2 × 10⁻⁴ ohm-metre. The electrical contacts are made of gold "
      "wires. The backing technique is same as employed for conventional wire or foil strain "
      "gages. Since the semiconductor strain gages are delicate in nature, these are handled with "
      "care.")
    P("Ưu điểm: (i) thay đổi điện trở do biến dạng lớn gần 100 lần căng kế thông thường; (ii) trơ "
      "về hóa học; (iii) hệ số gage cao; (iv) không trễ và khôngcreep; (v) không mỏi.",
      "Advantages: (i) With semiconductor strain gages, changes in resistance due to strain is "
      "nearly 100 times greater than conventional strain gage. (ii) It is chemically inert. (iii) "
      "It has high gage factor. (iv) It is free from hysteresis and creep. (v) It is immune to "
      "fatigue.")
    P("Nhược điểm: (i) rất nhạy với thay đổi nhiệt độ; (ii) độ tuyến tính kém; (iii) đắt hơn.",
      "Disadvantages: (i) Semiconductor strain gages are very sensitive to temperature changes. "
      "(ii) It has poor linearity. (iii) It is more expensive.")

    H("1.6.4 Phần tử đầu dò nhiệt độ điện trở (RTD)",
      "1.6.4 Resistance Temperature Detector Element (RTD)", h3)
    P("Phần tử đầu dò nhiệt độ điện trở là phần tử bộ chuyển đổi cơ bản quan trọng để đo nhiệt độ. "
      "Đặc tính cơ bản của sự thay đổi điện trở của kim loại do thay đổi nhiệt độ được khai thác "
      "trong phát triển phần tử RTD.",
      "Resistance temperature detector element is an important basic transducer element for "
      "measurement of temperature. The basic characteristic of change in resistance of a metal "
      "due to change in temperature has been utilized in the development of RTD element.")
    P("Như chúng ta biết, cấu trúc tinh thể của kim loại có nhiều electron tự do. Khi đặt điện áp, "
      "các electron này bắt đầu chạy theo một hướng xác định một cách tập thể. Các va chạm của "
      "chính các electron với nhau và với các ion trong kim loại tạo ra cản trở tự nhiên đối với "
      "dòng electron. Thực tế điều này được quan sát như điện trở đặc trưng của kim loại. Nếu ta "
      "thêm nhiều nhiệt vào kim loại, biên độ va chạm tăng lên, làm tăng điện trở kim loại. Ngoài "
      "các yếu tố khác, thay đổi điện trở do thay đổi nhiệt độ chủ yếu phụ thuộc hệ số nhiệt của "
      "điện trở.",
      "As we know, the crystalline structure of a metal has plenty of free electrons. When a "
      "voltage is applied, these electrons start flowing in a particular direction in a combined "
      "fashion. Resultant collisions of these electrons amongst themselves and with other ions "
      "present in the metal create natural restriction to the flow of electrons. In effect, it is "
      "observed as characteristic resistance of the metal. If we add substantial amount of heat "
      "to the metal, an increase in amplitude of collision is observed. This in effect results in "
      "an increase in resistance of the metal. Apart from the other factors, change in resistance "
      "due to change in temperature is dependent mainly upon temperature coefficient of "
      "resistance.")
    P("Sự biến đổi điện trở Rt ở nhiệt độ t °C của kim loại được chi phối bởi phương trình chung:",
      "Variation of resistance Rt at temperature tC of the metal is however, governed by general "
      "equation:")
    E("Rt = Ro (1 + At + Bt² + Ct³ + ...)    ...(1.21)",
      "Rt = Ro (1 + At + Bt² + Ct³ + ...)    ...(1.21)")
    P("trong đó Ro là điện trở của kim loại ở 0 °C và A, B, C, D là các hằng số xác định bằng thí "
      "nghiệm tùy theo dải đo nhiệt độ cụ thể.",
      "Where Ro is the resistance of metal at 0C and A, B, C, D are constants to be determined "
      "experimentally depending upon the particular range of measurement of temperature.")
    P("Yêu cầu đối với kim loại dùng chế tạo phần tử RTD:",
      "Requirement of a metal for use in manufacture of RTD element are:")
    U(["Thay đổi điện trở trên mỗi đơn vị thay đổi nhiệt độ phải lớn để độ chính xác tốt hơn.",
       "RTD được chế tạo nhỏ, vì vậy vật liệu dẫn phải có điện trở suất cao.",
       "Quan hệ giữa điện trở kim loại và nhiệt độ phải ổn định."],
      ["Change in resistance due to per unit change in temperature should be large for better "
       "accuracy.",
       "RTD is made small and for that the conducting material used should have high resistivity.",
       "Relation between resistance of metal and temperature should be stable."])
    P("Bảng 1.4 cho các vật liệu dẫn dùng chế tạo phần tử RTD.",
      "Table 1.4 shows these conducting materials for manufacture of RTD element.")
    P("<b>Bảng 1.4.</b> Vật liệu chế tạo RTD.",
      "<b>Table 1.4.</b> Materials for RTD construction.")
    TB(_h(vi, en, 4), _TBL14)
    P("Đồ thị Hình 1.27 cho đặc tính của ba vật liệu dẫn được dùng rộng rãi nhất làm RTD. Ba vật "
      "liệu này có độ nhạy và khả năng lặp lại xuất sắc để chế tạo bộ chuyển đổi nhiệt độ.",
      "The graph shown in Figure 1.27 indicates the characteristics of three most widely used "
      "conducting materials for RTD. These three exhibit excellent sensitivity and "
      "reproducibility for making temperature transducer.")
    FIG(27, F.fig_f27())
    P("Đồng có hệ số nhiệt điện trở hợp lý với quan hệ tuyến tính giữa nhiệt độ và thay đổi điện "
      "trở. Nhưng do điện trở suất thấp, kích thước RTD phải tăng để đạt độ nhạy chấp nhận được. "
      "Phần tử này được dùng chế tạo bộ chuyển đổi nhiệt độ đo nhiệt độ cuộn dây của động cơ "
      "điện H.T. Đến 120 °C, phần tử đồng là giải pháp rẻ nhất. Ở 0 °C, đồng được chuẩn hóa có điện "
      "trở 53 ôm.",
      "Copper has reasonable value of resistance temperature coefficient with linear relationship "
      "between temperature and change in resistance. But due to lower resistivity, size of RTD "
      "has to be increased to attain acceptable sensitivity. This element is used in making "
      "temperature transducer for measuring winding temperature of electrical H.T. motors. Upto "
      "a value of 120C, the copper element is the most inexpensive alternative. At 0C the copper "
      "is standardized to have 53 ohms of resistance value.")
    P("Hiệu năng của phần tử niken rất phi tuyến sau 50 °C, do đó việc sử dụng chỉ giới hạn trong "
      "giám sát nhiệt độ môi trường và nhiệt độ nước làm mát.",
      "The performance of nickel temperature element is very much non-linear beyond 50C. "
      "Therefore, its use is limited for monitoring of ambient temperature and cooling water "
      "temperature only.")
    P("Ưu điểm: (i) độ chính xác cao; (ii) dải đo hẹp; (iii) khả năng lặp lại tốt; (iv) đáp ứng "
      "nhanh. Nhược điểm: (i) đắt hơn tương đối so với cặp nhiệt điện; (ii) rung cản trở phép đo.",
      "Advantages: (i) High accuracy. (ii) Narrow spans of measurement. (iii) Good "
      "reproducibility. (iv) Fast response. Disadvantages: (i) Relatively expensive with respect "
      "to thermocouple. (ii) Vibration creates hindrance in measurement.")

    H("1.6.5 Phần tử cặp nhiệt điện (T-C)", "1.6.5 Thermocouple Element (T-C)", h3)
    P("Đây là phần tử bộ chuyển đổi đa dụng khác để đo nhiệt độ. Phần tử này gồm hai thermoelement "
      "khác nhau sinh thermo-electric emf khi được đốt nóng. Emf e sinh ra được chi phối bởi "
      "phương trình e = a + bt + ct², trong đó a, b, c là hằng số.",
      "This is yet another most versatile transducer element for measurement of temperature. This "
      "element is made up of two dissimilar thermoelements which produce thermo-electric emf when "
      "heated. The emf e produced is governed by the equation e = a + bt + ct² where a, b, c, are "
      "constants.")
    E("e = a + bt + ct²    ...(1.22)", "e = a + bt + ct²    ...(1.22)")
    P("Giá trị các hằng số phụ thuộc vào đặc tính của thermoelement và được xác định bằng thí "
      "nghiệm. Giá trị a cho biết độ cao của dải đo. Một điểm của cặp nhiệt được giữ ở 0 °C và điểm "
      "kia ở nhiệt độ t °C.",
      "The value of these constants depends upon the characteristics of the thermoelements and "
      "are found experimentally. The value of a indicates the elevation of the range. One point "
      "of the thermocouple is kept at 0C condition and the other one at temperature tC.")
    P("<b>Lý thuyết cơ bản của cặp nhiệt điện.</b> Seebeck phát hiện rằng nếu một đường kín được "
      "tạo bởi hai kim loại khác nhau và hai mối nối tạo ra được giữ ở nhiệt độ khác nhau thì một "
      "dòng điện chạy trong đường đó như Hình 1.28. Ông đã thử chọn tới 25 kim loại như vậy, trong "
      "đó có niken, bạch kim, đồng, mangan, crom, molypden, bạc, cadmi, kẽm, sắt, v.v.",
      "<b>Basic theory of thermocouple.</b> Seebeck found that if a closed path is formed by two "
      "different metals and the two junctions so formed are maintained at the different "
      "temperatures an electric current flow through the path as shown in Figure 1.28. He tried "
      "to select as many as 25-numbers of such metals. A few of them are Nickel, Platinum, Copper, "
      "Manganese, Chromium, Molybdenum, Silver, Cadmium, Zinc, Iron, etc.")
    FIG(28, F.fig_f28())
    P("Sau đó Peltier nhận thấy nhiệt được hấp thụ ở mối nóng và giải phóng ở mối lạnh, chiều dòng "
      "khác nhau. Nhận xét này dẫn đến giả thiết rằng mối nối của các kim loại có thể là nguồn của "
      "emf found trong hiệu ứng Seebeck. Nghĩa là nói chung có một emf tồn tại trên mối nối của "
      "hai kim loại khác nhau, độ lớn tỉ lệ với nhiệt độ các mối nối. Khi cả hai mối nối ở cùng "
      "nhiệt độ thì emf hiệu dụng bằng zero.",
      "Later on Peltier observed that heat was absorbed at hot junction while liberated at cold "
      "junction, the direction of current flow being different from one another. This observation "
      "led to the assumption that the junction of the metals may be a seat of emf found in "
      "seebeck effect. That means an emf exists across the junction of dissimilar metals in "
      "general, the magnitude being proportional to the temperature of the junctions. When both "
      "junctions happen to be at the same temperature the effective emf becomes zero.")
    P("Thí nghiệm tiếp của Kelvin cho thấy độ lớn emf sinh ra không hoàn toàn tỉ lệ với hiệu nhiệt "
      "độ. Emf trước tăng do thay đổi hiệu nhiệt độ nhưng thay đổi thêm nữa lại làm emf giảm, vượt "
      "qua đường zero và thực sự đảo chiều. Người ta thấy ở một số kim loại (như đồng) nhiệt được "
      "giải phóng tại một điểm dọc dây dẫn bị đốt nóng khi dòng chạy cùng chiều với dòng nhiệt, "
      "còn nhiệt được hấp thụ khi dòng chạy ngược chiều. Ở kim loại khác (như sắt) thì ngược lại: "
      "nhiệt hấp thụ khi dòng cùng chiều dòng nhiệt và giải phóng khi ngược chiều. Vì vậy có thể "
      "kết luận rằng Seebeck emf là tổ hợp của hiệu ứng Peltier và Kelvin, phụ thuộc vào chênh "
      "nhiệt độ giữa các mối nối và kim loại chọn để tạo cặp. Emf này có thể thu từ giản đồ nhiệt "
      "điện Hình 1.29.",
      "Further experiment made by Kelvin in this direction revealed that the magnitude of emf "
      "produced was not exactly proportional to the difference of temperature. The emf first "
      "increased due to change in differential temperature, but further change in differential "
      "temperature decreased the emf and passing through zero line, it actually got reversed. It "
      "was found that in some metal (say copper) heat is liberated at a particular point along "
      "the heated conductor when current flows in the direction of heat flow. While heat is "
      "absorbed at that point when the current flows in the opposite direction. But in the other "
      "metal (say iron) the heat shall be absorbed when the current flows in the direction of "
      "heat flow while heat is liberated when the current flows in the opposite direction of heat "
      "flow. Hence, it can be concluded that the Seebeck emf which is a combination of Peltier as "
      "well as Kelvin effect is dependent upon temperature difference between the junctions and "
      "the metals selected for the formation of the couple. This type of emf, produced by any "
      "couple can be obtained from a thermoelectric diagram shown in the Figure 1.29.")
    FIG(29, F.fig_f29())
    P("Trong giản đồ này, trục y biểu diễn nhiệt điện thế. Emf do kim loại 1 và 2 sinh ra khi các "
      "mối nối được giữ ở nhiệt độ T1 và T2 (tuyệt đối), cho bởi diện tích ABCD:",
      "In this diagram the y-axis represents thermoelectric power. The emf produced by the metals "
      "1 and 2 when the junctions are maintained at temperatures T1 and T2 (abs.), given by the "
      "area ABCD is:")
    E("Diện tích ABCD = (AD + BC)/2 × (T2 − T1)    ...(1.23)",
      "Area ABCD = (AD + BC)/2 × (T2 − T1)    ...(1.23)")
    P("Hình 1.30 cho đồ thị emf trên mỗi độ theo nhiệt độ của một số kim loại, trong đó chọn hai "
      "kim loại phù hợp để chế tạo cặp nhiệt.",
      "Figure 1.30 shows the emf per degree vs. temperature graph for a few metals out of which "
      "any two suitable metals are selected for fabricating a thermocouple.")
    FIG(30, F.fig_f30())
    P("Trong giản đồ, đường sắt và đồng cắt nhau ở 270 °C. Do đó với cặp nhiệt đồng-sắt, nếu mối "
      "lạnh được giữ dưới 270 °C và nhiệt độ mối nóng tăng lên thì emf sinh ra tiếp tục tăng tới "
      "270 °C. Nhiệt độ cố định này gọi là nhiệt độ trung tính của cặp đồng-sắt. Nếu tăng nhiệt độ "
      "cao hơn nữa (từ nhiệt độ trung tính), emf tăng từ sắt sang đồng và vì thế gọi là cặp sắt-đồng.",
      "In the diagram, iron and copper lines cross each other at 270C. Therefore, for a "
      "copper-iron thermocouple, if cold junction is maintained at bellow 270C and the "
      "temperature of hot junction is increased, the emf generated shall go on increasing till it "
      "reaches 270C. This fixed temperature is called neutral temperature for copper-iron "
      "thermocouple. If we increase the temperature further (from neutral temperature), increase "
      "in emf shall be observed from iron to copper and hence that will be called iron-copper "
      "thermocouple.")
    P("<b>Tiêu chuẩn chọn vật liệu cặp nhiệt.</b>", "<b>Selection criteria for thermocouple material.</b>")
    U(["Vật liệu chọn có emf lớn trên mỗi độ Celsius.",
       "Khi hoạt động, emf sinh ra không được thay đổi so với giá trị hiệu chuẩn.",
       "Thành phần vật liệu không thay đổi ở nhiệt độ cao.",
       "Nếu dự kiến có nhiễm bẩn và ứng suất cơ học khi sử dụng, cần chọn biện pháp bảo vệ phù hợp.",
       "Vật liệu chọn có đặc tính nhiệt đàn hồi ổn định để các lô cặp nhiệt tương tự có thể chế tạo "
       "liên tiếp.",
       "Vật liệu chọn được ủ già hóa thích hợp đến mức nhiệt độ tối đa đang dùng."],
      ["Materials selected should have high emf per degree centigrade temperature.",
       "While in operation, the generated emf should not vary with respect to calibrated value.",
       "Composition of the materials should not change at elevated temperature.",
       "If contamination and mechanical strains are envisaged while in use, suitable protective "
       "arrangement should also be selected.",
       "The selected material should have stable thermo-elastic characteristic so that successive "
       "batches of similar thermocouples can be manufactured.",
       "Proper ageing of the selected material should be done upto a value of maximum temperature "
       "in use."])
    P("Ưu điểm: (i) rẻ tiền; (ii) rất phù hợp làm hệ thống ghi nhiệt độ từ xa. Nhược điểm: (i) kém "
      "chính xác nên không dùng cho công việc đo chính xác; (ii) cặp nhiệt thường bị nhiễm bẩn nên "
      "cần bảo vệ cẩn thận; (iii) với hệ thống đo/ghi từ xa, cặp nhiệt phải nối qua cáp bù có đặc "
      "tính giống cặp nhiệt.",
      "Advantages: (i) It is inexpensive. (ii) This is perfectly suitable for making remote "
      "temperature recording system. Disadvantages: (i) This is less accurate and therefore, "
      "cannot be used for precision measurement work. (ii) Thermocouples become contaminated "
      "quite often and therefore, should be protected properly. (iii) For remote "
      "measurement/recording system, thermocouples are to be connected through compensating cable "
      "having the same characteristic as thermocouple.")

    H("1.6.6 Nhiệt trở", "1.6.6 Thermistors", h3)
    P("Có một số thermo-element chế tạo tốt có đặc tính nhiệt âm. Chúng thường là hỗn hợp oxit của "
      "niken, đồng, sắt, mangan và urani. Chúng gọi là điện trở nhiệt hay nhiệt trở (thermistor). "
      "Điện trở của phần tử nhiệt trở giảm khi nhiệt độ tăng. Trong một số trường hợp sự thay đổi "
      "rất lớn làm nhiệt trở rất nhạy, nhạy hơn cả RTD hay thậm chí cặp nhiệt điện. Chúng được dùng "
      "trong đo nhiệt độ chính xác trong dải −60 °C đến +15 °C. Điện trở nhiệt trở dao động từ vài "
      "ôm đến 1 mega ôm. Đặc tính rất phi tuyến.",
      "There are certain well-constructed thermo-elements which have negative temperature "
      "characteristics. These are usually mixtures of oxides of nickel, copper, iron, manganese "
      "and uranium. These are called thermal resistors or thermistor. The resistance of "
      "thermistor element decreases with respect to increase in temperature. In certain cases "
      "this change is very large making the thermistor very sensitive, higher than RTD or even "
      "thermocouple. These are used in precision temperature measurement in the range of -60C to "
      "+ 15C. Resistance of thermistor range for a few ohms to as high as 1 Mega ohm. The "
      "characteristic is highly non-linear.")
    P("Có ba đặc tính quan trọng của nhiệt trở:", "There are three important characteristics of "
      "thermistors:")
    U(["(i) Đặc tính điện trở suất theo nhiệt độ.",
       "(ii) Đặc tính điện áp theo dòng điện.",
       "(iii) Đặc tính dòng điện theo thời gian."],
      ["(i) Resistivity vs temperature characteristic.",
       "(ii) Voltage vs current characteristic.",
       "(iii) Current vs time characteristic."])
    P("<b>(i) Đặc tính điện trở suất theo nhiệt độ.</b> Đường đặc tính này thể hiện Hình 1.31. "
      "Quan hệ giữa điện trở suất và nhiệt độ được biểu diễn bằng:",
      "<b>(i) Resistivity vs temperature characteristic.</b> This characteristic curve has been "
      "shown on the Figure 1.31. The relation between resistivity and temperature can be "
      "expressed by the expression:")
    E("R1 = R2 · exp[β (1/T1 − 1/T2)]    ...(1.24)",
      "R1 = R2 · exp[β (1/T1 − 1/T2)]    ...(1.24)")
    P("trong đó R1 và R2 là điện trở ở nhiệt độ T1 và T2 Kelvin, β là hằng số phụ thuộc vào đặc "
      "tính của thermo-element. Như thấy trong hình, đường cong có thể xấp xỉ thành đường thẳng "
      "trong một dải hoạt động hạn chế.",
      "where R1 and R2 are the resistances at temperatures T1 and T2 Kelvin. β is a constant "
      "which depends upon the characteristic of the thermo-element. As is seen in the diagram, "
      "the curve can be approximated to a linear one over a limited range of operation.")
    FIG(31, F.fig_f31())
    P("<b>(ii) Đặc tính điện áp theo dòng điện.</b> Đường đặc tính này thể hiện Hình 1.32. Hai "
      "đường vẽ cho nhiệt độ môi trường ta và nhiệt độ khác t1 (ví dụ 50 °C) là các đường điển "
      "hình chỉ đặc tính điện trở âm. Đặt điện áp nhỏ cho dòng microampere (μA), do đó chưa đủ "
      "nhiệt làm tăng nhiệt độ nhiệt trở. Khi đủ nhiệt sinh ra ở dòng lớn hơn, tăng nhiệt độ thêm "
      "nữa làm giảm điện trở và kết quả là nhiều dòng chạy qua hơn. Hiện tượng này tiếp diễn tới "
      "khi công suất đặt bằng nhiệt hấp thụ. Đặc tính này rất đặc trưng và có thể dùng chế tạo bộ "
      "chuyển đổi đo biến quá trình trong công nghiệp hóa chất.",
      "<b>(ii) Voltage vs current characteristic.</b> This characteristic curve has been shown "
      "in Figure 1.32. The two curves drawn for ambient temperature ta and for any other "
      "temperature t1 (say 50C) are typical curves indicating negative resistance "
      "characteristic. Application of small voltage results in microampere (μA) current and "
      "therefore, no sufficient heat is evolved to raise the temperature of the thermistor. Once "
      "enough heat is evolved on higher current, further increase in temperature decreases the "
      "resistance of thermistor and as a result more current passes through. This phenomenon "
      "continues till the applied power equals the heat absorbed. This characteristic of "
      "thermistor is typical and can be used to manufacture transducer for measurement of "
      "process variables in chemical industries.")
    FIG(32, F.fig_f32())
    P("<b>(iii) Đặc tính dòng theo thời gian.</b> Đây là đặc tính đặc trưng khác cho phép dùng "
      "nhiệt trở chế tạo rơ le ngắt trễ thời gian. Như Hình 1.33, cần một khoảng thời gian xác định "
      "để nhiệt độ nhiệt trở tăng và dòng ổn định tăng lên. Khoảng thời gian này có thể thay đổi "
      "bằng cách đổi điện áp áp dụng.",
      "<b>(iii) Current vs time characteristics.</b> This is another typical characteristic of a "
      "thermistor which allows the thermistor to be used in manufacturing of time delay relay "
      "cut-outs. As seen from the Figure 1.33, specified time interval is required to be elapsed "
      "for raising the temperature of the thermistor and resultant increase in steady state "
      "current to take place. This time interval can, however, be changed by changing applied "
      "voltage.")
    FIG(33, F.fig_f33())
    P("Ưu điểm: (i) dải thời gian đáp ứng rộng, thường từ một phần giây đến vài phút; (ii) rẻ tiền; "
      "(iii) ổn định tốt; (iv) dù dải đo dùng là −60 °C đến +15 °C, có thể tăng tới khoảng 400 °C "
      "bằng cách nối phù hợp chịu được nhiệt độ đó. Nhược điểm: (i) vì có đặc tính nhiệt âm, dòng "
      "phải duy trì thấp nhất có thể để tránh sai số do tự đốt nóng phần tử.",
      "Advantages: (i) It has wide range of response time, typically from a fraction of a second "
      "to a few minutes. (ii) This is inexpensive. (iii) It has good stability. (iv) Though the "
      "used range of measurement is -60C to +15C, the range of measurement can be increased upto "
      "400C or so by proper connection to withstand this much temperature. Disadvantages: (i) "
      "Since the thermistor has negative temperature characteristic, the current should be "
      "maintained as low as practicable to avoid error caused by self-heating of the element.")

    H("1.6.7 Bộ chuyển đổi cảm ứng", "1.6.7 Inductive Transducer", h3)
    P("Cuộn cảm ở dạng ban đầu là phần tử bộ chuyển đổi rất quan trọng và phổ biến. Trong thực tế "
      "có ba đặc tính liên quan đến cuộn cảm mà cấu trúc bộ chuyển đổi cảm ứng dựa trên đó:",
      "Inductor coil, in its original form, is another very important as well as popular "
      "transducer element. In practice, however, there are three characteristics connected to an "
      "inductor coil upon which the construction of inductive transducers are based. They are:")
    U(["(i) Tự cảm L của cuộn dây,",
       "(ii) Hỗ cảm M khi hai cuộn cảm đặt cạnh nhau,",
       "(iii) Dòng xoáy sinh ra khi đưa vật dẫn lại gần cuộn cảm mang dòng A.C."],
      ["(i) Self-inductance of the coil L,",
       "(ii) Mutual inductance M, when two inductive coils are placed together and,",
       "(iii) Eddy current which is produced when a conducting material is brought near the "
       "inductor coil carrying A.C."])
    P("<b>(a) Bộ chuyển đổi cảm ứng dựa trên tự cảm L.</b> Tự cảm L của cuộn N vòng được cho bởi:",
      "<b>(a) Inductive transducer based on self-inductance L.</b> Self-inductance L of a coil of "
      "N turns is given by:")
    E("L = μ · N² · A / l    ...(1.25)", "L = μ · N² · A / l    ...(1.25)")
    P("trong đó l và A là chiều dài và diện tích tiết diện của dây làm cuộn, μ là độ thấm của môi "
      "trường. Biểu thức trên cho thấy bằng cách thay đổi hình dạng học A/l của dây cuộn, có thể "
      "thay đổi L và thiết kế bộ chuyển đổi tương ứng.",
      "where l and A are length and cross-sectional area of conductor of which the coil is made. "
      "μ is the permeability of the medium. The above expression indicates that by varying the "
      "geometric shape, A/l, of the conductor coil, the L can be varied and the transducer can be "
      "designed accordingly.")
    P("<b>(b) Bộ chuyển đổi cảm ứng dựa trên hỗ cảm M.</b> Hỗ cảm M giữa hai cuộn có tự cảm L1 và "
      "L2 được cho bởi M = Kc √(L1 L2), với Kc là hằng số ghép.",
      "<b>(b) Inductive transducer based on mutual inductance M.</b> Mutual inductance M between "
      "two inductor coils of self-inductances L1 and L2 is given by M = Kc √(L1 L2), where Kc is "
      "the coupling constant.")
    E("M = Kc · √(L1 · L2)    ...(1.26)", "M = Kc · √(L1 · L2)    ...(1.26)")
    P("Giá trị Kc phụ thuộc vào hướng của hai cuộn và môi trường đặt cuộn. Khi hai cuộn mắc nối "
      "tiếp, một cuộn cố định và cuộn kia chuyển động, cảm ứng của bố trí này thay đổi giữa (L1 + "
      "L2 − 2M) và (L1 + L2 + 2M). Tuy nhiên M thay đổi theo chuyển động của cuộn di động.",
      "The value of Kc depends upon the orientation of two inductor coils and the medium in which "
      "the coils are placed. When the two inductor coils are connected in series with one coil "
      "being stationary and other in motion, the inductance of such an arrangement varies between "
      "(L1 + L2 − 2M) and (L1 + L2 + 2M). However, mutual inductance M varies with the movement "
      "of coil in motion.")
    P("Hai loại cuộn có thể dùng thiết kế bộ chuyển đổi cảm ứng: (i) cuộn lõi sắt và (ii) cuộn lõi "
      "không khí.",
      "Two types of coils can be used for designing a inductive transducer: (i) Iron-cored coil "
      "and (ii) Air-cored coil.")
    P("<b>(i) Cuộn lõi sắt.</b> Cuộn được quấn trên lõi làm bằng sắt. Ưu điểm: (i) vì độ thấm của "
      "sắt cao, kích thước kinh tế và tổn thất cường độ từ trường không đáng kể; (ii) từ trường lạc "
      "bên ngoài không ảnh hưởng đến từ trường tạo ra vì từ trường này mạnh hơn. Nhược điểm: (i) "
      "cảm ứng không const mà phụ thuộc dòng chạy trong cuộn; (ii) ở tần số cao tổn hao dòng xoáy "
      "đáng kể, cần giữ tần số nguồn trong giới hạn để giảm tổn hao.",
      "<b>(i) Iron-cored coil.</b> In iron-cored coil, the coil is wound on a core made of iron. "
      "Advantages: (i) Since the permeability of iron is high, the size becomes economical and "
      "loss of magnetic field strength is ineffective. (ii) Stray/external magnetic field does "
      "not affect the magnetic field produced since the field produced is stronger. "
      "Disadvantages: (i) Inductance is not constant but dependent upon the current flow in the "
      "coil. (ii) At higher frequency, eddy current loss is significant. Supply frequency should "
      "be kept under limit to minimize such losses.")
    P("<b>(ii) Cuộn lõi không khí.</b> Đây thực chất là cuộn không lõi, nghĩa là không gian trước đây "
      "đặt lõi sắt trước đây được để trống và cuộn đặt trong không khí. Ưu điểm: (i) có thể hoạt động ở "
      "tần số cao hơn vì không có tổn hao dòng xoáy; (ii) độ thấm của môi trường là không khí, "
      "không đổi và không thay đổi theo dòng trong cuộn. Nhược điểm: kích thước lớn hơn.",
      "<b>(ii) Air-cored coils.</b> This coil is in fact core-less coil. This means that the "
      "space where iron was located in case of iron-cored coil is free here and the coil is "
      "located in air. Advantages: (i) This can be operated at higher frequency because there is "
      "no eddy current loss. (ii) The permeability of the medium, i.e. air is constant and does "
      "not change according to current flow in the coil. Disadvantage: (i) The size becomes "
      "larger.")
    P("<b>(c) Bộ chuyển đổi dựa trên dòng xoáy sinh ra.</b> Bộ chuyển đổi cảm ứng theo nguyên lý "
      "này về bản chất có một tấm dẫn đặt trước cuộn có dòng xoay chiều chạy qua. Dòng xoáy sinh ra "
      "trong tấm tạo từ trường cộng thêm vào từ trường của cuộn. Hai từ thông này tác động ngược "
      "nhau, làm tổng từ thông và cảm ứng giảm. Sự giảm cảm ứng thay đổi theo khoảng cách giữa tấm "
      "và cuộn dẫn dòng.",
      "<b>(c) Transducers based on eddy current produced.</b> Inductive transducer based upon "
      "this principle has essentially a conducting plate placed before a coil in which an "
      "alternating current is flowing. The eddy current so produced in the plate is responsible "
      "for a magnetic filed in addition to the magnetic field produced by the current carrying "
      "coil. These two magnetic fluxes act against each other. As a result the net flux as well "
      "as inductance get reduced. Reduction in inductance varies according to the variation of "
      "space between the plate and the current carrying coil.")

    H("1.6.8 Bộ chuyển đổi điện dung", "1.6.8 Capacitive Transducer", h3)
    P("Điện dung được tạo thành khi một chất cách điện được kẹp giữa hai bề mặt dẫn. Giá trị điện "
      "dung của bố trí này phụ thuộc vào đặc tính môi trường và hướng vật lý của các bề mặt dẫn. "
      "Trong thực tế thường dùng tụ phẳng song song để chế tạo bộ chuyển đổi. Giá trị điện dung C "
      "trong trường hợp này được cho bởi C = ε A/D, trong đó A là diện tích tiết diện của bề mặt "
      "dẫn, D là khoảng cách giữa hai bề mặt dẫn và ε là độ thấmđiện của môi trường giữa chúng.",
      "A capacitance is formed when an insulated substance is sandwiched between two conducting "
      "surfaces. The value of capacitance of such an arrangement shall depend upon the "
      "characteristics of the medium and the physical orientation of the conducting surfaces. In "
      "practice, generally parallel plate capacitors are used for realization of transducer. The "
      "value of capacitance C in such case is given by C = ε A/D where A is the cross-sectional "
      "area of the conducting surface and D is gap length between the two conducting surfaces. ε "
      "is permittivity of the medium located between the two conducting surfaces.")
    E("C = ε · A / D    ...(1.27)", "C = ε · A / D    ...(1.27)")
    P("Nguyên lý hoạt động của bộ chuyển đổi điện dung dựa trên ba biến ảnh hưởng đến giá trị điện "
      "dung:",
      "The principle of operation of capacitive transducer is based on three variables which in "
      "fact influence the value of capacitance:")
    U(["(i) Thay đổi chiều dài khe hở D,",
       "(ii) Thay đổi diện tích tiết diện tương đối giữa các bề mặt dẫn,",
       "(iii) Thay đổi độ bền điện môi của môi trường giữa các bề mặt."],
      ["(i) Change in gap length.",
       "(ii) Change in relative cross-sectional area between the conducting surfaces.",
       "(iii) Change in dielectric strength of the medium between the surfaces."])
    P("<b>(i) Dựa trên thay đổi chiều dài khe hở D.</b> Trong bố trí này, một bề mặt dẫn được giữ cố "
      "định trong khi bề mặt kia được phép dịch chuyển tương đối. Sự thay đổi điện dung C là hàm "
      "của D như Hình 1.34. Quan hệ là phi tuyến, nhưng có thể giảm thiểu bằng môi trường có hằng "
      "số điện môi cao, khi đó phi tuyến gần với tuyến tính.",
      "<b>(i) Capacitive transducer based on change in gap length D.</b> In this arrangement, one "
      "conducting surface is kept stationary while the other one is allowed is move relative to "
      "the previous one. The resulting change in capacitance C shall be function of D as shown in "
      "the Figure 1.34. The relation is non-linear. However, non-linearity can be minimized by "
      "utilizing medium having high dielectric constant. In this way the non-linearity can be "
      "approximated to linear one.")
    FIG(34, F.fig_f34())
    P("<b>(ii) Dựa trên thay đổi diện tích tiết diện A.</b> Thiết kế này phù hợp nhất khi dùng hai "
      "ống kim loại rỗng làm bề mặt dẫn song song. Điện dung thay đổi khi một ống được quấn vào "
      "hoặc tháo ra khỏi ống kia. Cũng ở đây một ống cố định, ống kia dịch chuyển tương đối. Có "
      "thể dùng cả bề mặt chữ nhật xếp lên nhau với khe chứa vật liệu điện môi. Cả hai bố trí được "
      "thể hiện trong Hình 1.35 và 1.36. Biến thiên điện dung C theo diện tích A là tuyến tính như "
      "Hình 1.37.",
      "<b>(ii) Capacitive transducer based on change in cross-sectional area A.</b> The design of "
      "capacitive transducer, based on this principle is best suited when two hollow metallic "
      "tubes are employed for parallel conducting surfaces. The capacitance of the arrangement "
      "shall change when one tube is wound on the other or unwound from the other. In this case "
      "also, one tube is kept stationary while the other is allowed to displace relative to the "
      "stationary one. The rectangular conducting surfaces can also be employed, arranged one "
      "upon the other and the gap filled with dielectric material. Both the arrangements have "
      "been shown in the Figures 1.35 and 1.36. The variation of capacitance C with respect to "
      "cross-sectional area A is linear as shown in the Figure 1.37.")
    FIG(35, F.fig_f35())
    FIG(36, F.fig_f36())
    FIG(37, F.fig_f37())
    P("<b>(iii) Dựa trên thay đổi độ bền điện môi của môi trường.</b> Biến thiên độ bền điện môi "
      "chỉ thực hiện được khi đặc tính của vật liệu điền giữa các bề mặt dẫn trở thành một biến. "
      "Chẳng hạn khi đưa vật liệu không dẫn như than vào phễu, độ bền điện môi của hệ thống thay "
      "đổi khi than lấp đầy phễu. Nhờ đó đo được lượng than theo mức trong phễu.",
      "<b>(iii) Capacitive transducer based on change in dielectric strength of the medium.</b> "
      "Variation in dielectric strength can be realized in practice only when the characteristic "
      "of the material to be filled in between the conducting surfaces becomes one variable. For "
      "instance, when a non-conducting material like coal is put into a hopper, the dielectric "
      "strength of the system changes as the coal fills up the hopper. In this way, measurement of "
      "coal quantity in terms of level of the hopper can be done.")
    P("<b>Ưu điểm.</b> (i) Rất nhạy; (ii) nhờ trở kháng đầu vào cao, hiệu ứng tải được giảm thiểu; "
      "(iii) độ phân giải cao; (iv) tiêu thụ ít công suất; (v) hiệu năng đáng tin cậy hơn ở những "
      "nơi bộ chuyển đổi cảm ứng không hiệu quả do nhiễu từ trường lạc quá mức.",
      "<b>Advantages.</b> (i) Capacitive transducer is very sensitive. (ii) In this case, due to "
      "high input impedance, loading effect is minimized. (iii) Resolution is high. (iv) It "
      "consumes less power. (v) Its performance is more reliable where inductive transducers are "
      "ineffective due to excessive interference of stray magnetic field.")
    P("<b>Nhược điểm.</b> (i) Trở kháng đầu ra rất cao gây hiệu ứng tải; giảm bằng cách giữ điện trở "
      "cách điện của cáp rất cao. (ii) Điện dung bề mặt góp phần gây phi tuyến, giảm bằng vòng bảo "
      "vệ (guard ring). (iii) Điện dung lạc cũng ảnh hưởng đến phép đo, giảm bằng nối đất thích "
      "hợp. (iv) Mọi cáp đều có điện dung; trong bộ chuyển đổi điện dung ảnh hưởng này rất rõ và "
      "gây sai số đáng kể do tải, cần dùng cáp có điện dung thấp. (v) Đặc điểm riêng là hiệu năng "
      "bị ảnh hưởng bởi bụi, độ ẩm, nhiệt độ cao, làm hệ thống rất phức tạp.",
      "<b>Disadvantages.</b> (i) Output impedance of a capacitive transducer is very high which "
      "results in loading effect. The effect of this can be minimized by keeping the insulation "
      "resistance of the cable very high. (ii) Surface capacitance contributes to the non-"
      "linearity, however, use of guard rings can minimize this effect. (iii) Stray capacitance "
      "also affects the measurement. This, however, can be minimized by proper earthing. (iv) All "
      "cables have capacitance. The effect of cable capacitance is not so alarming in other "
      "systems. But in capacitive transducer, effect of cable capacitance becomes pronounced and "
      "contributes to the measurement error significantly due to loading effect. To minimize this "
      "effect, cable having lower capacitance value should be employed. (v) The most peculiar "
      "thing of capacitive transducer is that its performance is affected by dust, moisture, "
      "elevated temperature, etc. That is why, the system becomes very complicated.")

    H("1.6.9 Phần tử bộ chuyển đổi áp điện", "1.6.9 Piezoelectric Transducer Element", h3)
    P("Có một số vật liệu tinh thể trong tự nhiên có đặc tính sinh điện tích khi chịu lực cơ học. "
      "Thực chất chúng bị biến dạng dưới lực tác dụng. Trong số vật liệu này, thạch anh (quartz) và "
      "muối Rochelle là hai vật liệu áp điện tự nhiên rất quan trọng. Một số vật liệu nhân tạo như "
      "lithium sulphate, ethylene diamine tartarate cũng có tính áp điện.",
      "There are certain crystalline materials available in nature, which exhibits the property "
      "of inducing electric charges on application of mechanical force on them. They actually get "
      "deformed under applied forces. In this line of materials, quartz and Rochelle salt are two "
      "very important naturally occurring piezoelectric materials. Certain artificial materials, "
      "e.g., lithium sulphate, ethylene diamine tartarate also have piezoelectric property.")
    P("Sự sinh điện tích do biến dạng của vật liệu áp điện dưới lực Fa xuất hiện dưới dạng điện áp "
      "trên điện cực như Hình 1.38. Điện áp sinh ra Ve được cho bởi Ve = qe/C, trong đó qe là điện "
      "tích sinh ra và C là điện dung của vật liệu áp điện giữa hai điện cực.",
      "Induction of electric charge, as a result of deformation of piezoelectric material under "
      "applied forces Fa appears as voltage across the electrode as shown in Figure 1.38. The "
      "induced voltage Ve is given by Ve = qe/C, where qe is the charge induced and C is the "
      "capacitance of the piezoelectric material placed between the electrodes.")
    E("Ve = qe / C    ...(1.28)", "Ve = qe / C    ...(1.28)")
    FIG(38, F.fig_f38())
    P("Hiệu ứng áp điện có hướng. Nghĩa là nếu đổi hướng lực Fa thì cực tính của điện áp sinh ra "
      "cũng đổi. Do đó nếu lực kéo sinh điện áp có cực tính này thì lực nén sẽ sinh điện áp cực tính "
      "ngược lại. Vì vậy kết luận rằng độ lớn và cực tính của Ve do điện tích qe sinh ra tỉ lệ với "
      "độ lớn và cực tính của lực Fa áp dụng.",
      "The piezoelectric effect is directional. This means if direction of applied force Fa "
      "changes, the polarity of induced voltage also gets changed. Therefore, if a tensile force "
      "induces a voltage of one particular polarity then a compressive force shall induce voltage "
      "of opposite polarity. Thus it is concluded that the magnitude and polarity of voltage Ve "
      "produced by electric charge qe shall be proportional to magnitude and polarity of applied "
      "force Fa.")
    P("Quan hệ giữa lực Fa và biến dạng Δy được cho bởi Fa = (E S/y) Δy, trong đó E là mô-đun đàn "
      "hồi Young, S và y là diện tích bề mặt và chiều dày của vật liệu áp điện.",
      "The relation between applied force Fa and deformation Δy can be given by Fa = (E S/y) "
      "Δy, where E is Youngs modulus of elasticity, S and y are surface area and thickness "
      "respectively of the piezoelectric substance.")
    E("Fa = (E · S / y) · Δy    ...(1.29)", "Fa = (E · S / y) · Δy    ...(1.29)")
    P("Vì E = (Fa/S)/(Δy/y) = Fa·y/(Δy·S), và qe = Kc Fa với Kc là hằng số độ nhạy điện tích của "
      "phần đang xét, dùng các biểu thức trên ta thu được qe = (Kc E S/y) Δy. Áp dụng (1.28) cho "
      "Ve = Kc E S Δy / (y C) = Kc E Δy / ε, với C = ε S/y và ε = εo εr.",
      "Since E = (Fa/S)/(Δy/y) = Fa·y/(Δy·S), and qe = Kc Fa where Kc is charge sensitivity "
      "constant of a particular portion under discussion of the piezoelectric substance. By "
      "using expressions 1.29, 1.30 and 1.31, we obtain a general relation of qe given by qe = "
      "(Kc E S/y) Δy and by applying expression (1.28), we get the relation for Ve as Ve = Kc E "
      "S Δy / (y C) = Kc E Δy / ε, where C = ε S/y and ε = εo εr.")
    E("Ve = Kc · E · Δy / ε    ...(1.33)", "Ve = Kc · E · Δy / ε    ...(1.33)")
    P("Từ (1.28) ta cũng có Ve = qe/C = Kc Fa /(ε S/y) = (Kc/ε) σ = Kv σ, với σ = Fa/S và Kv = "
      "Kc/ε. Vì vậy Ve = Kv σ y hay Kv = Ve/(σ y) = Ea/σ, trong đó Ea là cường độ điện trường.",
      "Now from (1.28), we have Ve = qe/C = Kc Fa /(ε S/y) = (Kc/ε) σ = Kv σ, since σ = Fa/S "
      "where Kv = Kc/ε. Again Ve = Kv σ y or Kv = Ve/(σ y) = Ea/σ, where Ea is electric field "
      "strength. Or Kc = ε Ve/(σ y) = ε Kv.")
    E("Kv = Ea / σ    ...(1.36)", "Kv = Ea / σ    ...(1.36)")
    E("Kc = ε · Kv    ...(1.37)", "Kc = ε · Kv    ...(1.37)")
    P("<b>Bảng 1.5.</b> Đặc tính của hai vật liệu áp điện phổ biến.",
      "<b>Table 1.5.</b> Characteristics of two popular piezoelectric materials.")
    TB(_h(vi, en, 5), _TBL15)
    P("Bảng 1.5 cho đặc tính của hai vật liệu áp điện phổ biến nhất.",
      "Table 1.5 indicates the characteristics of two most popular piezoelectric materials.")
    P("<b>Tính chất yêu cầu của vật liệu áp điện.</b> (a) Ổn định như thạch anh; (b) cho đầu ra "
      "cao như muối Rochelle; (c) không nhạy với thay đổi nhiệt độ và độ ẩm; (d) có thể tạo thành "
      "nhiều hình dạng theo yêu cầu như titanat bari.",
      "<b>Required properties of a piezoelectric material.</b> (a) It should be stable like "
      "quartz. (b) It should give higher output like Rochelle salt. (c) It should be insensitive "
      "to temperature and humidity changes. (d) It should be capable of getting transformed into "
      "variety of shapes as per requirement like barium titanate.")
    P("Rõ ràng từ Bảng 1.5, vật liệu áp điện tự nhiên có độ bền cơ học và độ ổn định nhiệt cao "
      "hơn. Mặt khác vật liệu tổng hợp nhân tạo có Kv cao hơn.",
      "As is obvious from the Table 1.5 that naturally available piezoelectric materials shall "
      "have higher mechanical strength and thermal stability. On the other hand, artificial "
      "synthetic piezoelectric materials shall have higher Kv as shown.")
    P("Mạch tương đương của bộ chuyển đổi áp điện có thể coi là một máy phát điện tích mắc song "
      "song với điện dung C và điện trở rò R của vật liệu như Hình 1.39. Máy phát điện tích ở Hình "
      "1.39(a) có thể thay bằng nguồn điện áp tương đương ở Hình 1.39(b).",
      "The equivalent circuit of piezoelectric transducer can be approximated as an electric "
      "charge generator placed across the capacitance C and the leakage resistance R (both "
      "connected in parallel) of the piezoelectric material as shown as in Figure 1.39. The "
      "equivalent circuit in the from of electric charge generator as shown in the Figure 1.39(a) "
      "can be replaced by equivalent voltage source as shown in Figure 1.39(b).")
    FIG(39, F.fig_f39())

    H("1.6.10 Phần tử bộ chuyển đổi hiệu ứng Hall", "1.6.10 Hall Effect Transducer Element", h3)
    P("Đặc tính của một số vật liệu là khi áp từ trường ngang vào và cho dòng chạy qua theo hướng "
      "vuông góc với hướng từ trường thì một emf Vh được sinh ra. Hướng của emf sinh ra vuông góc "
      "với cả hướng từ trường lẫn dòng điện như Hình 1.40. Độ lớn của hall emf tỉ lệ với tích mật "
      "độ từ thông B và dòng i, và tỉ nghịch với chiều dày t của vật liệu (mét):",
      "It is the nature of some of the materials that if transverse magnetic field is applied to "
      "it and a current is passed through it in the perpendicular direction with respect to the "
      "direction of field, an emf Vh shall be induced. The direction of the induced emf shall be "
      "perpendicular to the direction of the field as well as current as shown in Figure 1.40. "
      "The magnitude of this induced hall emf shall be proportional to the product of magnetic "
      "flux density B and the current i. Also it shall be inversely proportional to the thickness "
      "of the material t used (in metre). The relation is expressed as:")
    E("Vh ∝ i · B / t,  hay Vh = KH · i · B / t    ...(1.38)",
      "Vh ∝ i · B / t, or Vh = KH · i · B / t    ...(1.38)")
    P("trong đó KH là hằng số tỉ lệ gọi là hệ số hiệu ứng Hall. Giá trị KH của một số vật liệu "
      "thường dùng được cho trong Bảng 1.6.",
      "where KH is the proportionality constant and is known as Hall effect coefficient. KH of "
      "some of the commonly used materials for the purpose are indicated in the Table 1.6.")
    FIG(40, F.fig_f40())
    P("<b>Bảng 1.6.</b> Hệ số Hall của một số vật liệu.",
      "<b>Table 1.6.</b> Hall coefficient of selected materials.")
    TB(_h(vi, en, 6), _TBL16)
    P("Hall emf do vật liệu dẫn sinh ra thấp hơn do vật liệu bán dẫn sinh ra. Emf có dạng D.C. nên "
      "có thể đo bằng thiết bị nam châm vĩnh cửu cuộn dây di động (PMMC).",
      "The Hall emf produced by conducting material is lower than those produced by "
      "semiconductor material. The emf being D.C. type can be measured by permanent magnet moving "
      "coil (PMMC) instrument.")

    H("1.6.11 Phần tử chuyển đổi quang", "1.6.11 Optical Conversion Element", h3)
    P("Loại phần tử bộ chuyển đổi này gọi là phần tử optoelectric hoặc bộ chuyển đổi quang. Bộ "
      "chuyển đổi quang biến năng lượng ánh sáng thành dòng điện tỉ lệ. Các photon ánh sáng chiếu "
      "vào bề mặt bán dẫn p và dẫn điện tương ứng với bề mặt bán dẫn n đặt đối diện. Dựa trên nguyên "
      "lý cơ bản này có bốn loại phần tử bộ chuyển đổi quang được dùng phổ biến:",
      "This type of transducer element is called optoelectric transducer element or optical "
      "transducer. The optical transducer converts light energy into proportional electric "
      "current. The light photons fall onto the p-type semiconductor surface and conduction takes "
      "place with respect to the n-type semiconductor surface placed opposite to each other. On "
      "this basic principle, there are four types of optical transducer elements that are "
      "popularly in use:")
    U(["(i) Pin quang điện (photovoltaic cell),", "(ii) Tế bào quang (photocell),",
       "(iii) Photodiode,", "(iv) Phototransistor."],
      ["(i) Photovoltaic cell,", "(ii) Photocell", "(iii) Photodiode",
       "(iv) Phototransistor"])

    H("(i) Pin quang điện", "(i) Photovoltaic cell", h4)
    P("Năng lượng ánh sáng đặc biệt trong dải bước sóng 0,4 đến 0,8 micron khi chiếu vào pin quang "
      "điện được thiết kế chế tạo phù hợp sẽ sinh dòng điện. Hình 1.41(a) cho thấy thiết kế của pin "
      "quang điện điển hình chế tạo từ tổ hợp vật liệu bán dẫn p và n.",
      "Light energy particularly in the range of 0.4 to 0.8 micron wavelength when incident upon "
      "a properly designed and fabricated photovoltaic cell, electric current is produced. Figure "
      "1.41(a) shows a design of typical photovoltaic cell fabricated from a combination of "
      "p-type and n-type semiconductor material.")
    FIG(41, F.fig_f41())
    P("Lớp trên cùng của pin là nắp kính bảo vệ pin khỏi bụi và độ ẩm. Lớp kế là keo trong suốt giữ "
      "nắp kính. Lớp phủ chống phản xạ ngăn phản xạ ánh sáng. Các lớp bán dẫn p và n được đặt giữa "
      "các tiếp điểm kim loại như Hình 1.41(a). Hai tiếp điểm kim loại này thu đầu ra. Khi ánh sáng "
      "chiếu vào, các photon sinh hạt tải thiểu số, tức electron trong lớp p và lỗ trong lớp n. Các "
      "hạt tải này tự do đi qua mối nối.",
      "The top layer of the cell is a glass cover to protect the cell from dust and moisture. The "
      "next layer is a transparent adhesive for holding the glass cover. The layer of "
      "anti-reflection coating prevents the reflection of light. The p-type and n-type "
      "semiconductor layers are placed in between metallic contacts as shown in Figure 1.41(a). "
      "These two metallic contacts collect the output. When the light is incident, the photons "
      "generate minority carriers, i.e. electrons in p-type layer and holes in n-type layers. "
      "These carriers freely cross the junction.")
    P("Trong mạch tương đương Hình 1.41(b), Ie là thành phần chính của dòng do ánh sáng tới sinh ra. "
      "Ic là dòng tối chảy ngay cả khi không có sáng và liên quan đến dòng It sinh nhiệt có xu "
      "hướng chảy ngược. Với Vt là điện áp đầu cuối sẵn có, dòng Il chạy qua tải:",
      "In the circuit model Figure 1.41(b) Ie is the major component of the current generated by "
      "the incident light. Ic is the dark current that flows even in the absence of any incident "
      "light and is related to an invisible current It generated thermally which tends to flow in "
      "the reverse direction. With Vt taken as available terminal voltage, the current Il is "
      "established through load, which is given by:")
    E("Il = Ie − Ic − It · [exp(e·Vt/λ) − 1]    ...(1.39)",
      "Il = Ie − Ic − It · [exp(e·Vt/λ) − 1]    ...(1.39)")
    P("trong đó e là điện tích electron và λ là bước sóng. Khi Vt = 0 (đoản mạch) Isc = Ie. Khi Il "
      "= 0 (hở mạch), ta có Voc = (λ/e) log(1 + Ie/It).",
      "where e is the charge on electron and λ is the wavelength. When Vt = 0 (a short circuit "
      "condition) Isc = Ie. When Il = 0 (an open circuit condition), Voc = (λ/e) log(1 + Ie/It).")
    E("Isc = Ie    ...(1.40)", "Isc = Ie    ...(1.40)")
    E("Voc = (λ/e) · log(1 + Ie/It)    ...(1.41)",
      "Voc = (λ/e) · log(1 + Ie/It)    ...(1.41)")
    P("Hình 1.41(c) cho dòng đầu ra theo cường độ ánh sáng tới với các điện trở trong khác nhau của "
      "pin. Pin quang điện chỉ đáp ứng hiệu quả tới tối đa 125 °C. Hai phần tử pin quang điện quan "
      "trọng nhất là selen và silic.",
      "Figure 1.41(c) shows output current with respect to intensity of incident light of "
      "different internal resistances of cells. The photovoltaic cells are effectively responsive "
      "upto a maximum of 125 Celcius only. The two most important photovoltaic cell elements are "
      "selenium and silicon.")
    P("Công dụng: Ngoài việc dùng làm phần tử bộ chuyển đổi, chúng có thể dùng trong ứng dụng mà "
      "pin hoặc các nguồn cấp khác không thuận lợi. Ví dụ cung cấp nguồn cho tàu vũ trụ nơi ánh "
      "sáng mặt trời rất dồi dào, do đó pin mặt trời dùng để đổi năng lượng mặt trời thành điện.",
      "Use: In addition to be used as transducer elements, these can be used in application where "
      "battery or other forms of supply systems are not advantageous to use. For instance "
      "provision of supply system for spacecraft where sun rays are available in abundance and "
      "therefore, solar cell is used to convert solar energy to electrical one.")

    H("(ii) Photocell hay tế bào quang dẫn", "(ii) Photocell or photoconductive cell", h4)
    P("Nguyên lý cơ bản của photocell là khi ánh sáng chiếu vào một số vật liệu bán dẫn điển hình "
      "như cadmium sulphide hoặc cadmium selenide, điện trở của chúng giảm khi cường độ sáng tăng. "
      "Một nguồn D.C. luôn được dùng cùng tế bào quang dẫn để làm nó dẫn điện, vì thế chúng còn gọi "
      "là tế bào quang dẫn.",
      "The basic principle of photocell is that when light is incident upon some typical "
      "semiconductor materials like cadmium sulphide or cadmium selenide, their resistance "
      "decreases as the intensity of light increases. A D.C. supply system is invariably employed "
      "in conjunction with photoconductive cell to make it conductive and that is why these are "
      "called photoconductive cells as well.")
    P("Có một đặc điểm riêng ở photocell là nếu giữ nó trong tối, điện trở đạt giá trị cực cao cỡ "
      "10¹² ôm. Sau đó khi đưa lại gần ánh sáng, điện trở giảm dần. Sự giảm điện trở phụ thuộc vào "
      "kích thước vật lý và hình dạng học ngoài cường độ sáng. Trong khi dẫn, dòng chạy chỉ vài "
      "miliampe.",
      "There is a peculiarity found with the photocell that if the photocell is kept in dark, the "
      "resistance attains a tremendously high value of the order of 10¹² ohms. Afterwards when "
      "the same is put in the vicinity of light, the resistance goes on decreasing. The decrease "
      "of resistance depends upon physical dimension as well as geometric shape in addition to "
      "the intensity of light. During conduction, the current flowing is only a few milliampere.")
    P("Độ nhạy của photocell được định nghĩa là thay đổi điện trở trên mỗi đơn vị thay đổi ánh sáng "
      "tới. Khi so sánh từ tối tới sáng bình thường, sự thay đổi điện trở từ tối tới sáng quan sát "
      "cao tới 1000:1. Nhược điểm của photocell là không dùng trong ứng dụng tương tự.",
      "Sensitivity of a photocell can be defined as the change in resistance per unit change in "
      "incident light. When it is compared from dark to normal incident light, the resistance "
      "change for dark to light has been observed as high as 1000 : 1. The disadvantage of the "
      "photo cells is that these are not used in analog application.")

    H("(iii) Photodiode", "(iii) Photodiode", h4)
    P("Hành vi đặc biệt của diode phân cực ngược khi có ánh sáng tới tăng đã sinh ra loại diode mới "
      "gọi là photodiode. Khi không có sáng, photodiode cho một lượng nhỏ dòng bão hòa ngược do cặp "
      "electron-lỗ sinh nhiệt. Số hạt tải thiểu số này phụ thuộc vào cường độ sáng tới trên mối nối "
      "PN. Hình 1.42 cho photodiode mắc trong mạch. Khi cường độ sáng tăng, dòng tăng như các đường "
      "đặc tính Hình 1.43.",
      "The peculiar behaviour of a reverse biased diode in the presence of increased incident "
      "light gave birth to a new type of diode called photodiode. When there is no light, the "
      "photodiode allows a small amount of reverse saturation current due to thermally generated "
      "electron-hole pairs. The number of these minority carriers depends upon the intensity of "
      "incident light on the PN junction. Figure 1.42 shows a photodiode connected to a circuit. "
      "When the intensity of incident light is increased, the current increases as shown by the "
      "characteristic curves in Figure 1.43.")
    FIG(42, F.fig_f42())
    FIG(43, F.fig_f43())
    P("Như vậy chính cường độ sáng làm photodiode dẫn nhiều hơn dù điện trở ngược của mối nối rất "
      "cao. Dòng tối chảy liên tục khi không có sáng gọi là dòng rò.",
      "Therefore, it is the light intensity that makes the photodiode more conductive even if the "
      "reverse resistance of the junction is very high. The dark current that continuously flows "
      "whenever there is no light in the vicinity of the photodiode is called leakage current.")
    P("Ưu điểm: (i) tuyến tính đạt được thành công trong dải hoạt động thực tế; (ii) do nhiễu bắt "
      "ít, tỉ số tín hiệu/nhiễu (SNR) cao hơn; (iii) đáp ứng tần số tốt hơn. Nhược điểm: (i) nếu "
      "nhiệt độ môi trường tăng, dòng tối tăng; (ii) rất cần nguồn pin để hoạt động; (iii) khi sáng "
      "yếu, dòng giảm nên cần bộ khuếch đại.",
      "Advantages of (i) Linearity is achieved successfully over practical region of operation. "
      "(ii) Since the noise-pickup is less, SNR (signal to noise ratio) is higher. (iii) Better "
      "frequency response is achieved. Disadvantages (i) If temperature of the environment is "
      "increased by any means, the value of dark current increases. (ii) Supply battery power is "
      "very much required for its operation. (iii) In case of poor intensity of incident light, "
      "current flow is lowered and as a result amplifier shall be needed for suitable "
      "amplification.")

    H("(iv) Phototransistor", "(iv) Phototransistor", h4)
    P("Phototransistor chỉ là một transistor nối trong đó mối nối base-emitter (P-N) được để hở "
      "chiếu sáng như Hình 1.44. Mối nối được phủ kính để ánh sáng chiếu vào. Khi sáng chiếu vào mối "
      "nối, một lượng lớn photon sinh nhiều cặp electron-lỗ. Electron đi về phía collector và lỗ "
      "đi về phía emitter. Dòng electron tạo dòng phototransistor. Dòng base cho mạch base-emitter "
      "do năng lượng ánh sáng tới cung cấp.",
      "Phototransistor is just a junction transistor in which base-emitter junction (P-N) is "
      "allowed to be exposed to incident light as shown in Figure 1.44. The junction is covered "
      "with glass to allow light to incident upon. When the light is incident upon the junction, "
      "large amount of photons generate large amount of electrons hole pairs. The electrons move "
      "toward collector and the holes move towards the emitter. The electron flow constitutes "
      "phototransistor current. The base current to the base-emitter circuit is supplied by "
      "incident light energy.")
    P("Về hình thức phototransistor giống photodiode nhưng khác nhau ở độ nhạy; độ nhạy của "
      "phototransistor lớn hơn photodiode.",
      "Physically, phototransistor seems just like photodiode, but they differ in sensitivity. The "
      "sensitivity of the phototransistor is larger than photodiode.")
    FIG(44, F.fig_f44())
    FIG(45, F.fig_f45())
    P("Ưu điểm: (i) công suất tiêu thụ thấp; (ii) đáp ứng nhanh hơn; (iii) tuổi thọ hoạt động dài "
      "hơn; (iv) hệ số khuếch đại cao hơn; (v) dùng được trong ứng dụng số. Nhược điểm duy nhất là "
      "khác nhau giữa thời gian tăng (tối sang sáng) và thời gian giảm (sáng sang tối), trong đó "
      "thời gian tăng bằng 1/10 thời gian giảm.",
      "Advantages (i) Power consumption is low. (ii) Response is faster. (iii) Operation life is "
      "longer. (iv) Higher gain is achievable. (v) These can be used in digital application. "
      "Disadvantages The only disadvantage of photo-transistor is the difference between rise-time "
      "(dark-to-light) and fall-time (light-to-dark) in the response, the rise-time being 1/10 of "
      "the fall time.")

    H("1.6.12 Cảm biến nhiệt độ sợi quang", "1.6.12 Fiber Optic Sensor Element for Temperature", h3)
    P("Công nghệ hệ thống cảm nhận nhiệt độ bằng sợi quang là sự kết hợp của hệ thống truyền sợi "
      "quang và hệ thống phát hiện quang. Tuy nhiên nhiệt kế dựa trên lý thuyết bức xạ vật đen của "
      "Planck. Để thực hiện, buồng vật đen được tạo bằng cách phún xạ một màng mỏng iridi lên một "
      "tinh thể sapphire mỏng. Năng lượng bức xạ theo cách này là đặc trưng của nhiệt độ mà buồng "
      "tiếp xúc. Năng lượng bức xạ dưới dạng ánh sáng được truyền qua cáp sợi quang tới hệ thống "
      "phát hiện quang.",
      "The technology of optical fibre temperature sensing system is a combination of fibre optic "
      "transmission system and photo detection system. However, thermometry is based upon "
      "Plancks theory of black body radiation. For this, the black body cavity is formed by "
      "sputtering a thin film of iridium onto a thin crystal of sapphire. The energy radiated in "
      "this way shall be the characteristics of the temperature to which the cavity is exposed. "
      "This radiant energy in the form of light is transmitted through the fibre optic cabling to "
      "a photo detection system.")
    P("Kỹ thuật trên đã được dùng thành công cho dải đo từ 500 °C đến 2000 °C.",
      "The above technique has been successfully used for the range of measurement from 500C to "
      "2000C.")
    P("Ưu điểm: (i) hệ thống đo này tốt hơn hệ thống đo cặp nhiệt; (ii) độ chính xác đạt tới "
      "0,0025%; (iii) đo biến thiên nhiệt độ chính xác hơn; (iv) không nhạy với nhiễu điện từ; (v) "
      "tuổi thọ dài hơn vì không có lão hóa nhiệt.",
      "Advantages (i) This measurement system is better than thermocouple measurement system. "
      "(ii) Achievable accuracy is as high as 0.0025%. (iii) By this method temperature variations "
      "can be measured more accurately. (iv) It is insensitive to electromagnetic interferences. "
      "(v) Longer life since there is no thermal ageing.")
    P("<b>Tính thương mại.</b> Có sẵn thiết bị hoàn chỉnh gồm cảm biến nhiệt độ, đầu dò quang và bộ "
      "xử lý tín hiệu. Hệ thống cũng có thể nối giao tiếp với máy tính quá trình qua bus IEEE488 "
      "hoặc RS232C.",
      "<b>Commercial availability.</b> Commercial units complete with temperature sensor, optical "
      "detector and signal processor is available. The system can be interfaced to a process "
      "computer through IEEE488 or RS232C buses as well.")

    # ---------------------------------------------------------------- 1.7
    H("1.7 Phần tử bộ chuyển đổi thứ cấp", "1.7 Secondary Transducer Element", h3)
    P("Như đã nêu ở các phần trước, phần tử chuyển đổi thứ cấp là phần tử biến đầu ra trung gian "
      "nhận được từ phần tử chuyển đổi sơ cấp thành dạng thích hợp để chỉ thị, ghi hoặc điều khiển "
      "ở phía thiết bị thu. Theo đó có năm loại hệ thống chuyển đổi thứ cấp:",
      "As we have indicated on earlier references, the secondary transducing elements are those "
      "that convert the intermediate output available from the primary transducing elements into "
      "suitable form for indication/recording/control purposes on receiver side. As such there "
      "can be five different categories of secondary transducing systems:")
    U(["(i) Hệ thống vòi phun-cánh van khí nén,",
       "(ii) Hệ thống đổi khí nén-điện,",
       "(iii) Hệ thống đổi điện-khí nén,",
       "(iv) Hệ thống cầu Wheatstone-RTD,",
       "(v) Hệ thống chiết áp-thermocouple."],
      ["(i) Pneumatic flapper-nozzle system",
       "(ii) Pneumatic-electric conversion system",
       "(iii) Electro-pneumatic conversion system",
       "(iv) Wheatstone bridge-RTD system",
       "(v) Potentiometer-thermocouple system."])

    H("1.7.1 Hệ thống vòi phun-cánh van", "1.7.1 Flapper-nozzle System", h4)
    P("Hình 1.46 cho thấy hệ thống vòi phun-cánh van thông thường, về bản chất vận hành bằng khí "
      "nén. Lực do đầu vào đo tác dụng qua ống sóng đo bị cân bằng bởi lực do áp suất không khí qua "
      "ống sóng phản hồi. Chuyển động tổng của cánh van rất nhỏ (0,0254 mm). Áp suất khí nén 1,4 "
      "kg/cm² được áp dụng cho vòi phun qua bộ hạn chế lỗ nhỏ như hình. Không khí này liên tục thoát "
      "qua vòi phun. Đầu vào đo áp lực lên cánh van bịt vòi phun. Hành động này sinh áp suất ngược "
      "qua bộ hạn chế, là đầu ra của hệ thống, tỉ lệ với đầu vào đo và có thể dùng để vận hành thiết "
      "bị chỉ thị hoặc hệ thống khác. Đồng thời đầu ra này cũng được đưa vào hệ thống phản hồi để "
      "khôi phục cân bằng.",
      "Figure 1.46 shows a conventional flapper-nozzle system, which is essentially "
      "pneumatic-operated. The force applied by the measurement input through process/measurement "
      "bellow is restrained by the force generated by air pressure through feedback bellow. The "
      "overall motion of the flapper being required in this system is very little (0.0254 "
      "millimetre). The 1.4 kg/cm2 pneumatic pressure is applied to the nozzle through orifice "
      "restrictor as shown. This air constantly bleeds through the nozzle. The measurement input "
      "applies force to the flapper, which caps the nozzle. This action generates back-pressure "
      "through the office restrictor. This is the resulting output of the flapper-nozzle system, "
      "which is proportional to measurement input and can be applied to operate an indication or "
      "other systems. Simultaneously, this output is fed to feedback system as well to restore "
      "the balance of the flapper-nozzle system.")
    FIG(46, F.fig_f46())
    P("Đường kính vòi phun lớn hơn 1,5 đến 2,5 lần kích thước bộ hạn chế lỗ, giúp tạo áp suất ngược "
      "đủ lớn. Với nguồn 1,4 kg/cm², đầu ra 0,2 đến 1,0 kg/cm² dễ dàng tạo ra. Hình cho đồ thị đầu "
      "ra theo khe hở vòi phun: tuyến tính hoàn hảo giữa 0,5 và 1,0 kg/cm² và gần tuyến tính giữa "
      "0,2 và 1,0 kg/cm². Dải đầu ra này được chấp nhận cho mọi mục đích thực tế. Độ rộng dải theo "
      "đầu ra khí nén là 1,0 − 0,2 = 0,8 kg/cm².",
      "The diameter of the nozzle happens to be from 1.5 to 2.5 times greater than the size of "
      "orifice restrictor, which helps in generating sufficient back pressure. With 1.4 kg/cm2 "
      "pneumatic supply, an output of 0.2 to 1.0 kg/cm2 can be easily generated through the "
      "flapper-nozzle system. The diagram shows the graph of output vs. flapper-nozzle gap. It is "
      "clear that perfect linearity is achieved between 0.5 kg/cm2 and 1.0 kg/cm2 and an "
      "approximate linearity is obtained between 0.2 and 1.0 kg/cm2. That is why, this range of "
      "output can be accepted for all practical purposes. Range of span in terms of pneumatic "
      "output shall be 1.0 − 0.2 = 0.8 kg/cm2.")
    FIG(47, F.fig_f47())
    P("Giá trị này được phân bổ tỉ lệ theo 0 đến 100% đầu vào đo như Bảng 1.7.",
      "This has to be distributed proportionally with respect to 0 to 100% of the measurement "
      "input as indicated in the table below:")
    P("<b>Bảng 1.7.</b> Quan hệ đầu vào đo và đầu ra.",
      "<b>Table 1.7.</b> Measurement input versus output signal.")
    TB(_h(vi, en, 7), _TBL17)

    H("1.7.2 Hệ thống đổi khí nén-điện", "1.7.2 Pneumatic-electric Conversion System", h4)
    P("Bộ chuyển đổi này biến đầu vào đo dạng 0,2 đến 1,0 kg/cm² (khí nén) thành đầu ra điện (4 đến "
      "20 mA D.C.). Dù yêu cầu này rất hiếm khi cần, vẫn cần thảo luận về mặt học thuật.",
      "This transducer converts the measurement input which is in the form of 0.2 to 1.0 kg/cm2 "
      "(pneumatic) to electrical output (in the form of 4 to 20 mAmps. D.C.). Though this "
      "requirement of the instrument is on very rare occasions, yet it needs discussion on "
      "academic grounds.")
    P("Sơ đồ cho một trong các bộ chuyển đổi thứ cấp này. Thay đổi tín hiệu đầu vào khí nén (0,2 đến "
      "1,0 kg/cm²) làm thay đổi khe hở không khí của cụm đầu dò. Cụm đầu dò gồm hai miếng vật liệu "
      "ferrite như Hình 1.48. Thay đổi khe hở làm thay đổi cảm ứng của mạch dao động, dẫn đến thay "
      "đổi dòng đầu ra (4 đến 20 mA D.C.). Ngoài đầu ra đưa đi chỉ thị, dòng này cũng đưa vào hệ "
      "thống phản hồi để khôi phục cân bằng của dầm lực ở điều kiện làm việc mới. Hệ thống dùng để "
      "thu tín hiệu điện tỉ lệ thay cho tín hiệu khí nén 0,2 đến 1,0 kg/cm² sẵn có.",
      "The diagram shows one of such secondary transducers. A change in pneumatic input signal "
      "(0.2 to 1.0 kg/cm2) brings change in air gap of the detector assembly. The detector "
      "assembly is made of two pieces of ferrite material as shown in the Figure 1.48. The "
      "changes in the air gap of the detector assembly change the inductance of the oscillator "
      "circuit resulting in change of output current (4 to 20 mAmps. D.C.). In addition to the "
      "output to be fed for indication, this current is fed to feedback system as well to restore "
      "the equilibrium of the force beam at new operating condition. This system is used to "
      "obtain proportional electrical signal in place of available pneumatic signal which is in "
      "the form of 0.2 to 1.0 kg/cm2.")
    FIG(48, F.fig_f48())

    H("1.7.3 Hệ thống đổi điện-khí nén", "1.7.3 Electro-pneumatic Conversion System", h4)
    P("Như đã thấy trong thảo luận trước, tín hiệu D.C. 4 đến 20 mA có thể biến thành lực bằng cách "
      "cho dòng chạy qua cuộn dây đặt trong từ trường. Nguyên lý này được dùng để đổi tín hiệu điện "
      "sang dạng khí nén.",
      "As we have observed during earlier discussion that a 4 to 20 mAmps. D.C signal can be "
      "converted into force by passing the current signal through a coil placed in a magnetic "
      "field. This principle is utilized in converting the electrical signal to pneumatic form.")
    P("Như Hình 1.49, cuộn dẫn dòng được đặt để chuyển động trong hệ nam châm vĩnh cửu. Khi dòng 4 "
      "đến 20 mA chạy qua cuộn, cuộn bị dịch chuyển. Toàn hệ thống nối qua hệ vòi phun-cánh van khí "
      "nén, tạo đầu ra 0,2 đến 1,0 kg/cm². Tín hiệu này thường dùng để vận hành phần tử điều khiển "
      "cuối trong vòng điều khiển kín.",
      "As shown in Figure 1.49, the current carrying coil is placed to move within a permanent "
      "magnet system. When a 4 to 20 mAmps. current signal is passed through the coil, a "
      "displacement in the coil is experienced. The entire system is connected through a "
      "pneumatic flapper-nozzle system, which generates output in terms of 0.2 to 1.0 kg/cm2. "
      "This output signal is used generally for operating final control element placed in a closed "
      "loop control system.")
    FIG(49, F.fig_f49())

    H("1.7.4 Hệ thống cầu Wheatstone-RTD", "1.7.4 Wheatsone Bridge-RTD System", h4)
    P("Như mô tả trước, sự thay đổi điện trở trong RTD do thay đổi nhiệt độ được cầu Wheatstone cảm "
      "nhận. Dòng mất cân bằng của hệ thống kết hợp cầu-RTD được khuếch đại thích hợp, thu được tín "
      "hiệu đo 4 đến 20 mA D.C. tỉ lệ với thay đổi điện trở của RTD do nhiệt độ.",
      "As described earlier, a change in resistance in RTD (resistance temperature detector) due "
      "to temperature change is sensed by Wheatstone bridge. The out of balance current of a "
      "Wheatstone bridge-RTD combined system is suitably amplified and a measurement signal in "
      "terms of 4 to 20 mAmps. D.C. can be obtained. This current shall be proportional to change "
      "in resistance experienced in RTD due to temperature change.")
    FIG(50, F.fig_f50())
    P("Tín hiệu đầu ra có thể dùng để cân bằng cầu nhờ cơ cấu servo. Servo thay đổi điện trở Rb để "
      "cân bằng cầu khi hệ thống trượt đặt trên Rb được nối cơ học với servo. Nguyên lý chuyển đổi "
      "thứ cấp này được dùng trong hệ thống ghi và điều khiển nhiệt độ dựa trên đầu vào RTD.",
      "The output signal can be used to balance the bridge by means of a servomotor arrangement. "
      "The servomotor shall vary the resistance Rb for balancing the bridge when the "
      "moving/sliding system placed onto Rb is linked mechanically with the servomotor. This "
      "principle of secondary transducing is utilized in temperaturing recording as well as "
      "controlling system based on RTD input.")

    H("1.7.5 Hệ thống chiết áp-thermocouple", "1.7.5 Potentiometer-Thermocouple System", h4)
    P("Hệ thống này khác đôi chút với hệ thống cầu Wheatstone-RTD. Ở đây dùng chiết áp thay cho cầu "
      "Wheatstone làm mạch đo. Milivôn đầu vào do cặp nhiệt sinh ra theo thay đổi nhiệt độ được đưa "
      "vào mạch đo chiết áp. Điện áp D.C. mất cân bằng sinh ra được đổi sang điện áp A.C. bằng mạch "
      "đổi như Hình 1.51.",
      "This system is somewhat different from the Wheartstone-bridge-RTD system. Here "
      "potentiometer is employed in place of Wheatstone bridge for measurement circuit. The input "
      "millivolt generated by thermocouple with respect to changes in temperature is fed to "
      "potentiometer measuring circuit. The out of balance D.C. voltage so produced is converted "
      "to A.C. voltage by means of converter circuit as shown in Figure 1.51.")
    FIG(51, F.fig_f51())
    P("Điện áp A.C. từ bộ đổi dùng để dẫn động servo cho cân bằng chiết áp. Như vậy hệ thống này "
      "giống hệ thống chiết áp tự cân bằng. Vì cần mức điện áp cao để dẫn động servo, hệ thống cần "
      "khuếch đại hai cấp (tiền khuếch đại và khuếch đại servo). Cơ cấu chuyển động dùng cân bằng "
      "chiết áp cũng dùng để ghi nhiệt độ. Chi tiết hơn sẽ trình bày ở chỗ thích hợp.",
      "The A.C. voltage obtained from the converter shall be used for driving the servomotor for "
      "balancing the potentiometer. In this way this system is just like self-balancing "
      "potentiometer system. Since higher voltage level is required to drive the servomotor, a "
      "two-stage amplification system (preamplification and servo-amplification) is the basic "
      "requirement of the system. The moving mechanism which has been used for balancing the "
      "potentiometer shall be used for recording the temperature as well. More details of this "
      "system shall be described at proper place.")

    # ---------------------------------------------------------------- examples
    H("Ví dụ", "Examples", h3)
    P("<b>Ví dụ 1.1.</b> Một căng kế điện trở có hệ số gage bằng 2 được dán vào thanh thép chịu ứng "
      "suất 500 kg/cm². Nếu mô-đun đàn hồi của thép là 2 × 10⁶ kg/cm², hãy tìm thay đổi điện trở của "
      "phần tử căng kế do ứng suất áp dụng.",
      "<b>Example 1.1.</b> A resistance strain gage with a gage factor of 2 is fastened to a steel "
      "rod, subjected to a stress of 500 kg/cm2. If modulus of elasticity of steel is 2 × 10⁶ "
      "kg/cm2, find the change in resistance of the strain gage element due to the applied "
      "stress.")
    P("<b>Lời giải.</b> Ở đây Gf = 2, ứng suất σ = 500 kg/cm², E = 2 × 10⁶ kg/cm². Vì E = σ/ε nên "
      "ε = σ/E = 500/(2 × 10⁶) = 2,5 × 10⁻⁴. Do Gf = (ΔR/R)/(ΔL/L) = (ΔR/R)/ε, suy ra ΔR/R = Gf "
      "· ε = 2 × 2,5 × 10⁻⁴ = 5 × 10⁻⁴.",
      "<b>Solution.</b> Here gage factor Gf = 2, Stress σ = 500 kg/cm2, Modulus of elasticity E = "
      "2 × 10⁶ kg/cm2. Now E = σ/ε [where ε is strain] or ε = σ/E = 500/(2 × 10⁶) = 2.5 × 10⁻⁴. "
      "Since Gf = (ΔR/R)/(ΔL/L) = (ΔR/R)/ε or ΔR/R = Gf · ε = 2 × 2.5 × 10⁻⁴ = 5 × 10⁻⁴.")
    P("<b>Ví dụ 1.2.</b> Một căng kế được dán vào dầm để đo biến dạng. Hệ thống đo là cầu căng kế. "
      "Điện trở biến đổi R4 là 121 Ω ở biến dạng zero và 121,6 Ω khi có biến dạng ε. Nếu hệ số "
      "gage là 2, hãy tìm biến dạng trong dầm.",
      "<b>Example 1.2.</b> A strain gage is fastened to a beam to measure the strain experienced "
      "by the beam. The system of measurement is a strain gage bridge as shown on the diagram. "
      "The variable resistance R4 is of 121 Ω at zero strain and 121.6 Ω with strain ε. If the "
      "gage factor is 2, find the strain in the beam.")
    P("<b>Lời giải.</b> Ở đây Rs = R2·R4/R3 = R4 = 121 Ω. Khi dầm chịu biến dạng, Rs + ΔRs = "
      "121,6 Ω nên ΔRs = 0,6 Ω, hay ΔR4/R4 = 0,6/121. Hệ số gage Gf = (ΔR4/R4)/ε, suy ra ε = "
      "ΔR4/(R4·Gf) = (0,6/121)/2 = 2,48 × 10⁻³.",
      "<b>Solution.</b> Here, Rs = R2·R4/R3 = R4 = 121 Ω. When the beam is under strain, the new "
      "resistance value shall be given by Rs + ΔRs = R2·R4/R3 = R4 = 121.6 Ω. ∴ΔRs = 0.6 Ω or "
      "ΔR4/R4 = 0.6/121. Now the gage factor Gt = (ΔR4/R4)/ε ∴ε = ΔR4/(R4·Gt) = (0.6/121)/2 = "
      "2.48 × 10⁻³.")
    P("<b>Ví dụ 1.3.</b> Bộ chuyển đổi điện dung có hai bản diện tích 400 mm² (20 × 20 mm). Khoảng "
      "cách giữa hai bản là 2 mm. Điện dung là 10 picofarad khi không có áp suất. Tìm thay đổi điện "
      "dung khi áp suất 2 × 10⁵ N/m² làm khoảng cách giảm còn 1,5 mm.",
      "<b>Example 1.3.</b> A capacitance type transducer has two plates of surface area 400 mm2 "
      "(20 × 20 mm) each. The distance between the plates is 2 mm. The value of capacitance of the "
      "set-up is 10 picofarad without any external pressure on the plate. Find out the change in "
      "capacitance when a pressure of 2 × 10⁵ Newton per square metre is applied on the plate due "
      "to which the distance between the plates is reduced to 1.5 mm.")
    P("<b>Lời giải.</b> A = 400 mm² = 4 × 10⁻⁴ m², d = 2 mm = 2 × 10⁻³ m, C = 10 × 10⁻¹² F. Từ C "
      "= ε A/d suy ra ε = C d/A = (10 × 10⁻¹² × 2 × 10⁻³)/(4 × 10⁻⁴) = 0,5 × 10⁻¹⁰ F/m. Khi d′ = "
      "1,5 × 10⁻³ m, C′ = ε A/d′ = 1,33 × 10⁻¹¹ F = 13,3 pF. Vậy điện dung mới là 13,3 pF và thay "
      "đổi điện dung là 3,3 pF.",
      "<b>Solution.</b> Here area of plate A = 400 mm2 = 4 × 10⁻⁴ metre2, distance d = 2mm = 2 × "
      "10⁻³ metre, Capacitance C = 10 × 10⁻¹². Now C = ε A/d [where ε is dielectric strength] or "
      "ε = C d/A = (10 × 10⁻¹² × 2 × 10⁻³)/(4 × 10⁻⁴) = 0.5 × 10⁻¹⁰ F/m. On application of "
      "external pressure, d′ = 1.5 × 10⁻³ metre. Hence the changed capacitance C′ = ε A/d′ = "
      "(0.5 × 10⁻¹⁰ × 4 × 10⁻⁴)/(1.5 × 10⁻³) = 1.33 × 10⁻¹¹ F. Hence, the new value of "
      "capacitance = 13.3 pf and Change in capacitance = 13.3 pf − 10 pf = 3.3 pf.")
    P("<b>Ví dụ 1.4.</b> Nhiệt trở 5 kΩ dùng đo nhiệt độ cùng ampe kế dải 0 đến 60 mA, điện trở "
      "trong 5 Ω. Điện trở biến đổi Rr đặt ở 20 Ω và nguồn Eb là 16 V. Hãy tìm số đọc ampe kế ở 25 "
      "°C và 75 °C. [Cho điện trở ở 25 °C là 4 kΩ và ở 75 °C là 950 Ω.]",
      "<b>Example 1.4.</b> A thermistor of 5 KΩ is used to measure the temperature along with a "
      "metre of range 0 to 60 milliampere and internal resistance of 5 Ω as shown in the diagram. "
      "The variable resistance Rr is set at 20 Ω and power Eb is of 16 volt. What is the reading "
      "of ammeter at 25C and at 75C? [Given resistance at 25C is 4 KΩ and resistance at 75C is 950 Ω.]")
    P("<b>Lời giải.</b> Ở 25 °C: I = Eb/Req = 16/(4000 + 20 + 5) = 4 mA. Ở 75 °C: I = 16/(950 + "
      "20 + 5) = 16,4 mA.",
      "<b>Solution.</b> Here current indicated in ammeter at 25C = Eb/Req = 16/(4000 + 20 + 5) = "
      "4 mA. Similarly, current indicated in ammeter at 75C = Eb/(950 + 20 + 5) = 16/975 = 16.4 mA.")
    P("<b>Ví dụ 1.5.</b> LDR điện trở thấp 20 ô hoạt động ở một cường độ sáng nhất định cần được bảo "
      "vệ bằng điện trở mắc nối tiếp sao cho dòng tối đa 12 mA chạy khi điện áp nguồn 10 V. Tìm giá "
      "trị điện trở bảo vệ.",
      "<b>Example 1.5.</b> A low resistance LDR of 20 ohms operated at certain intensity of light "
      "is to be protected by applying a series resistance in such a way that upto 12 milliampere "
      "current is to flow at a supply voltage of 10 volt. Find the value of protective "
      "resistance.")
    P("<b>Lời giải.</b> Dòng qua LDR = 0,012 A. Điện áp trên LDR = 0,012 × 20 = 0,24 V. Điện áp trên "
      "điện trở bảo vệ = 10 − 0,24 = 9,76 V. Vậy điện trở bảo vệ = 9,76/0,012 = 813,33 ôm.",
      "<b>Solution.</b> Current passing through LDR = 0.012 ampere. Voltage across LDR = 0.012 × "
      "20 = 0.24 volt. Voltage across the series protective resistance = 10 − 0.24 = 9.76 volt. "
      "Hence, the value of protective resistance = 9.76/0.012 = 813.33 ohms.")
    P("<b>Ví dụ 1.6.</b> Rơ le điện cơ được điều khiển bằng tế bào quang dẫn. Chiết áp đo đưa "
      "12 mA ở mức 36 V khi tế bào được chiếu 600 lumen/m² và cần ngắt khi tế bào tối. Tìm điện trở "
      "nối tiếp và dòng tối. [Cho điện trở tế bào 1,2 kΩ ở 600 lumen/m² và điện trở tối 100 kΩ.]",
      "<b>Example 1.6.</b> An electromechanical relay is to be controlled by a photoconductive "
      "cell. The measuring potentiometer delivers 12 milliampere current at 36 volt setting when "
      "the photo conductive cell is illuminated at 600 lumens/m2 and is required to be "
      "de-energized when the photo cell is dark. Find out the series resistance and dark current. "
      "[Given the photocell resistance equal to 1.2 KΩ at 600 lumens/metre2 and dark resistance "
      "of photocell 100 KΩ.]")
    P("<b>Lời giải.</b> Ở 600 lumen/m², I = 36/(Rs + 1,2 kΩ + 3 kΩ?) = 0,012 A, suy ra Rs = "
      "36/0,012 − 1,2 kΩ − 3 kΩ? = 2 kΩ. Với điện trở tối 100 kΩ: dòng tối = 36 V/(2 kΩ + 100 "
      "kΩ) = 36/102 kΩ = 0,353 mA.",
      "<b>Solution.</b> At 600 lumens/m2, resistance of photocell is 1.2 KΩ, hence current through "
      "the relay is equal to 36/(Rs + 1.2K + 3K) = 0.012 Amp. or Rs = 36/0.012 − 1.2K − 3K = "
      "2 KΩ. Now dark resistance = 100 KΩ ∴ Dark current = 36V/(2K + 100K) = 36V/102K = 0.353 mA.")
    P("<b>Ví dụ 1.7.</b> Màng ngăn tròn phẳng kim loại có đường kính 15 mm. Tìm chiều dày nếu ứng "
      "suất cực đại không vượt 300 MN/m². Nếu áp suất áp dụng là 300 kN/m², hãy tìm độ võng tại tâm "
      "cho áp suất 150 kN/m². E = 300 GN/m² và hệ số Poisson 0,28.",
      "<b>Example 1.7.</b> A flat circular diaphragm of a metal has a diameter of 15 millimetre. "
      "Find the thickness of the diaphragm if the maximum stress is not to exceed 300 MN/m2 If "
      "pressure applied is 300 KN/m2, find the deflection at the centre for a pressure of 150 "
      "KN/m2. Youngs modulus of elasticity of the metal is 300 GN/m2 and Poissons ratio is 0.28.")
    P("<b>Lời giải.</b> Dùng σm = 16 Pa d²/(3 t²), suy ra t = √[3 Pa d²/(16 σm)] = "
      "√[(3 × 300 × 10³ × (15 × 10⁻³)²)/(16 × 300 × 10⁶)] = 0,205 mm. Độ võng tại tâm do 150 "
      "kN/m²: Y = Pa d⁴ (1 − μ³)/(256 Y t³) = 4,74 × 10⁻⁵ m = 0,0476 mm.",
      "<b>Solution.</b> Applying equation σm = 16 Pa d²/(3 t²) where σm is circumferential maximum "
      "stress, d is diameter, Pa is applied pressure and t is thickness, we get t = "
      "√[3 Pa d²/(16 σm)] = √[(3 × 300 × 10³ × (15 × 10⁻³)²)/(16 × 300 × 10⁶)] = 0.205 × 10⁻³ "
      "metre = 0.205 millimetre. Deflection at the centre due to pressure 150 KN/m2 = Pa d⁴ "
      "(1 − μ³)/(256 Y t³) = 4.74 × 10⁻⁵ metre = 0.0476 millimetre.")
    P("<b>Ví dụ 1.8.</b> Bộ chuyển đổi điện dung có khoảng cách bản 0,1 mm trong điều kiện tĩnh, "
      "điện dung 10 pF. Nếu thay đổi điện dung do dịch chuyển đo được là +1 pF, hãy tìm dịch chuyển.",
      "<b>Example 1.8.</b> A capacitive transducer with its plate separation of 0.1 millimetre "
      "under static conditions has a capacitance of 10 picofarad. If the change in capacitance due "
      "to displacement is measured to be + 1 picofarad, find the displacement.")
    P("<b>Lời giải.</b> C = K A/d. Với C = 10 pF, d = 0,1 mm: 10 × 10⁻¹² = K A/(0,1 × 10⁻³). Với "
      "trường hợp hai C = 1 pF: 1 × 10⁻¹² = K A/d. Chia hai phương trình: (10 × 10⁻¹²)/(1 × 10⁻¹²) "
      "= d/(0,1 × 10⁻³), suy ra d = 1 × 10⁻³ m = 1 mm.",
      "<b>Solution.</b> We know that C = K A/d where C is capacitance, K is dielectric constant, "
      "A is area of plate and d is the separation between the plates. Now when C = 10 picofarad "
      "and d = 0.1 millimetre, we get 10 × 10⁻¹² = K A/(0.1 × 10⁻³) ...(i). In second case when, C "
      "is 1 picofarad, we get 1 × 10⁻¹² = K A/d ...(ii). Dividing (i) by (ii), we get (10 × 10⁻¹²)/"
      "(1 × 10⁻¹²) = d/(0.1 × 10⁻³) ∴ d = 1 × 10⁻³ metre = 1 millimetre.")

    # ---------------------------------------------------------------- exercise
    H("Bài tập", "Exercise", h3)
    P("1. Định nghĩa bộ chuyển đổi kèm ví dụ. Phân biệt bộ chuyển đổi sơ cấp và thứ cấp.",
      "1. Define transducer with examples. Differentiate between primary and the secondary "
      "transducer.")
    P("2. Các đặc tính thứ cấp của bộ chuyển đổi là gì? Mô tả chi tiết. Bộ chuyển đổi ngược là gì?",
      "2. What are the secondary characteristics of a transducer? Describe in detail. What is an "
      "inverse transducer?")
    P("3. Phân biệt: (a) bộ chuyển đổi chủ động và thụ động, (b) bộ chuyển đổi tương tự và số.",
      "3. Differentiate between: (a) Active and Passive transducer, (b) Analog and Digital "
      "transducer.")
    P("4. Nêu tên các dạng cơ khí của phần tử bộ chuyển đổi. Mô tả chi tiết bất kỳ hai dạng nào.",
      "4. Mention the names of mechanical form of transducer elements. Describe any two of them "
      "in detail.")
    P("5. Hệ số gage của căng kế là gì? Suy ra biểu thức hệ số gage theo hệ số Poisson cho phần tử "
      "căng kế có chiều dài L và đường kính tiết diện D.",
      "5. What is gage factor of a strain gage? Derive the expression of gage factor in terms of "
      "Poissons ratio for a strain gage element of length L and diameter of cross-section D.")
    P("6. Nêu tên các dạng điện của phần tử bộ chuyển đổi. Mô tả chi tiết bất kỳ hai dạng nào.",
      "6. Mention the names of electrical form of transducer elements. Describe any two of them "
      "in detail.")
    P("7. Phân biệt phần tử cặp nhiệt điện, phần tử nhiệt độ điện trở và phần tử nhiệt trở theo "
      "hành vi đo của chúng.",
      "7. Differentiate amongst a thermocouple element, a resistance temperature element and a "
      "thermistor element in respect to their measurement behaviour.")
    P("8. Nêu sơ đồ hiệu chuẩn để hiệu chuẩn phần tử nhiệt trở kèm hình vẽ.",
      "8. Mention a calibration set-up for calibration of a thermistor element with diagram.")
    P("9. Nêu tên năm loại phần tử cặp nhiệt điện phổ biến nhất trong công nghiệp và dải ứng dụng "
      "của chúng.",
      "9. Mention the names of five types of most popular thermocouple element in industries. "
      "Mention their range of application as well.")
    P("10. Phân biệt phần tử nang và phần tử ống sóng. Chúng dùng ở đâu và dải ứng dụng là gì?",
      "10. Differentiate between a capsule element and a bellows element. Where these are used "
      "and what are the range of applications?")
    P("11. Rosette là gì? Công dụng của cấu hình căng kế dạng rosette là gì?",
      "11. What is a rossete? What is the use of a rossete type of configuration of strain gage?")
    P("12. Bộ chuyển đổi điện dung là gì? Mô tả hoạt động của nó so với bộ chuyển đổi cảm ứng.",
      "12. What is a capacitive transducer? Describe its functioning in comparison to an "
      "inductive transducer.")
    P("13. Phân biệt bộ chuyển đổi áp điện và quang điện. Có bao nhiêu loại phần tử bộ chuyển đổi "
      "quang điện? Mô tả ngắn gọn.",
      "13. Differentiate between piezoelectric and photoelectric transducer. How many types of "
      "photoelectric transducer elements are there? Describe them in brief.")

    # ---------------------------------------------------------------- about
    H("Về nguồn tài liệu", "About the source", h3)
    P("Chương 1 chiếm PDF tr. 13-74, tương ứng tr. 1-62 của bản in; PAGES_SRC = 62 đếm toàn bộ "
      "phân đoạn nguồn này. Các mục theo mục lục là Introduction, Definition of Transducer, "
      "Classification of Transducer, Inverse Transducer, Characteristics of Transducers, "
      "Transducer Elements và Secondary Transducer Element, tiếp theo là Examples và Exercise. "
      "Nguyên bản có 51 hình đánh số Fig. 1.1 - Fig. 1.51, bảy bảng đánh số Table 1.1 - Table 1.7, "
      "41 phương trình đánh số (1.1) - (1.41), tám ví dụ và 13 câu hỏi; tất cả được dựng lại dạng "
      "vector hoặc chép lại từ trang in ở đây.",
      "Chapter 1 occupies PDF pp. 13-74, corresponding to printed pp. 1-62; PAGES_SRC = 62 counts "
      "this whole source span. Its sections are Introduction, Definition of Transducer, "
      "Classification of Transducer, Inverse Transducer, Characteristics of Transducers, "
      "Transducer Elements and Secondary Transducer Element, followed by Examples and Exercise. "
      "The source contains 51 numbered figures (Fig. 1.1 - Fig. 1.51), seven numbered tables "
      "(Table 1.1 - Table 1.7), 41 numbered equations (1.1) - (1.41), eight examples and 13 "
      "questions; all are redrawn as vectors or transcribed from the printed pages here.")
    b.append(note(
        ("<b>Đặc điểm của nguyên bản.</b> PDF lưu phần lớn văn bản dưới dạng mã glyph (/G84, "
         "/G114, ...); bản giải mã work/ipc_decoded.txt đã đổi mỗi /Gnn thành chr(nn), nhưng vẫn "
         "giữ nhiều lỗi OCR và lỗi chính tả. Các phương trình chỉ tồn tại dưới dạng ký tự rời rạc "
         "nên được viết lại bằng ký hiệu toán học chuẩn tại chỗ; thứ tự một số hệ số trong công "
         "thức thực nghiệm (như 1.9, 1.11, 1.12) được trình bày theo nghĩa vật lý hợp lý nhất. Các "
         "hình trong PDF là ảnh, chỉ phần chú thích còn lại trong lớp văn bản, vì vậy mọi hình được "
         "vẽ lại đơn giản hóa theo đúng nội dung chú thích và văn bản lân cận. Một số lỗi của nguồn "
         "được giữ nguyên trong bản Anh (ví dụ 'transducers are understood to be a transmitters', "
         "'to be a transmitter', 'at zero process variable', 'impendances', 'the from of electric "
         "charge generator', 'temperaturing recording', 'Wheartstone', 'rossete', 'no more "
         "possible'), còn bản Việt dùng nghĩa đúng. Các bảng 1.5 và 1.6 có số mũ bị rời rạc trong "
         "nguồn, được ghi lại theo cách đọc hợp lý nhất."
         if vi else
         "<b>Source quirks.</b> The PDF stores most body text as glyph codes (/G84, /G114, ...); "
         "the decoded file work/ipc_decoded.txt converts each /Gnn to chr(nn) but retains many OCR "
         "artifacts and typos. The equations survive only as scattered glyphs and are rendered "
         "with standard mathematical notation in place; the ordering of some coefficients in "
         "empirical formulas (e.g. 1.9, 1.11, 1.12) follows the most plausible physical meaning. "
         "The figures are images in the PDF and only their captions remain in the text layer, so "
         "every figure is redrawn in simplified form consistent with its caption and surrounding "
         "prose. A number of source quirks are kept in the English text (e.g. 'transducers are "
         "understood to be a transmitters', 'at zero process variable', 'impendances', 'the from "
         "of electric charge generator', 'temperaturing recording', 'Wheartstone', 'rossete', "
         "'no more possible'), while the Vietnamese uses the intended meaning. Exponents in "
         "Tables 1.5 and 1.6 are scattered in the source and are transcribed with the most "
         "plausible reading.")))
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2019 I.K. "
      "International; các chương của sách phát hành theo giấy phép Creative Commons.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2019 I.K. "
      "International; the individual chapters are released under Creative Commons.</i>")

    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
