# -*- coding: utf-8 -*-
"""Book 7, Chapter 32 - Pipe Vibration Due to Sound / Rung đường ống do âm thanh (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
185-189 (PDF pp. 178-182; printed = PDF + 7). Five printed pages: the Exxon
refinery survey, two worked field examples, a log-log correlation graph, an
angle-valve jet schematic, six displayed equations, a Summary and one
additional-reading item. The PDF text layer garbles every equation; the
printed forms were read from pypdfium2 renders of the five source pages.
"""
from cvp_common import eq, fig, h2, h3, note, p, ul

import cvpfig32 as F

PAGES_SRC = 5
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Pipe Vibration Due to Sound"
TITLE_VI = "Rung đường ống do âm thanh"

_READING = ("V. A. Carucci and R. T. Mueller, “Acoustically Induced Piping "
            "Vibration in High Capacity Pressure-Reducing Systems,” ASME "
            "paper 82-WA/PVP-8 (1982).")


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 32.</b> mức công suất âm thanh bên trong (Lwi) · "
                "công suất âm thanh bên trong (Wa) · mức áp suất âm thanh (SPL) · "
                "độ giảm áp bị chokes · vận tốc tới hạn / vận tốc âm thanh · tia phun "
                "(sonic jet) · chân co thắt (vena contracta) · đường kính tia (Dj) · "
                "hệ số lưu lượng thực tế (Cv) · hệ số phục hồi áp suất (FL) · vận tốc "
                "tại chân co thắt (Uvc) · tần số đỉnh bên trong (fp) · gia tốc (m/s², G) "
                "· tần số trùng (coincident frequency) · mỏi thành ống · rung cộng "
                "hưởng · van chống ồn đặc biệt (low-noise valve) · hệ số hiệu suất âm "
                "thanh (acoustic efficiency factor)")
    return ("<b>Key terms.</b> internal sound power level (Lwi) · internal sound "
            "power (Wa) · sound pressure level (SPL) · choked pressure drop · "
            "sonic jet · vena contracta · jet diameter (Dj) · actual flow "
            "coefficient (Cv) · pressure recovery factor (FL) · jet velocity at "
            "the vena contracta (Uvc) · internal peak frequency (fp) · "
            "acceleration (m/s², G) · coincident frequency · pipe-wall fatigue · "
            "resonant vibration · special low-noise valve · acoustic efficiency "
            "factor")


def body_vi():
    b = []
    b.append(h2("Rung đường ống do âm thanh", "Pipe Vibration Due to Sound"))
    b.append(p("Khoảng 40 năm trước, Công ty Exxon đã tiến hành một cuộc khảo sát dựa "
               "trên kinh nghiệm của mình tại các nhà máy lọc dầu để xác định mức âm "
               "thanh nào có thể làm vỡ đường ống. Giới hạn dường như là mức công "
               "suất âm thanh (Lwi) 160 dB. Đồ thị trong Hình 32-1 cho thấy ngay cả "
               "ở mức rung tần số thấp 100 Hz (cps), gia tốc đã vượt quá 60 G. "
               "Tiện thể, Lwi 160 dB tương đương với mức áp suất âm thanh (SPL) "
               "148 dB và tiếng ồn tương tự tiếng máy bay phản lực cất cánh. Từ "
               "Hình 32-1 cũng thấy rằng ở mức công suất 160 dB và tần số chỉ 400 Hz, "
               "gia tốc đạt 100 G."))
    b.append(p("Rung quá mức trên đường ống và các thiết bị gắn liền có thể gây hư "
               "hỏng nghiêm trọng, vì gia tốc do rung có thể làm gãy các đường dẫn "
               "tín hiệu (sensing lines) gắn vào ống, thậm chí cả kết cấu đỡ ống. "
               "Rung cộng hưởng, khi tần số bên trong gần với tần số trùng "
               "(coincident frequency) của ống, có thể dẫn đến mỏi thành ống về lâu "
               "dài, tạo ra các vết nứt trên thành ống."))
    b.append(p("Mối tương quan giữa mức công suất âm thanh và gia tốc được thể hiện "
               "trong Hình 32-1. Như thấy, gia tốc tỷ lệ thuận trực tiếp với tần số."))
    b.append(p("Để tính mức gia tốc, trước hết phải chuyển mức áp suất âm thanh "
               "thành mức công suất âm thanh. Đây là phương trình:"))
    b.append(eq("L<sub>wi</sub> = 10 log(W<sub>a</sub> / 10<sup>−12</sup>)"))
    b.append(fig(1, F.fig_f321()))
    b.append(p("Hoặc:"))
    b.append(eq("L<sub>wi</sub> = 120 + 10 log(M × c<sub>i</sub><sup>2</sup> / 2) + η  "
                "tính bằng dB"))
    b.append(p("trong đó<br>"
               "L<sub>wi</sub> = mức công suất âm thanh bên trong, tính bằng dB<br>"
               "W<sub>a</sub> = công suất âm thanh bên trong, tính bằng watt<br>"
               "M = lưu lượng khối, tính bằng kg/s<br>"
               "c<sub>i</sub> = vận tốc âm thanh trong khí, tính bằng m/s<br>"
               "SPL = mức áp suất âm thanh bên ngoài"))
    b.append(eq("η = 10 log (hệ số hiệu suất âm thanh) = −40 dB với vận tốc âm thanh "
                "của khí"))
    b.append(p("Tần số đỉnh bên trong f<sub>p</sub> = 0.2 × U<sub>vc</sub> / D<sub>j</sub>, "
               "trong đó"))
    b.append(eq("f<sub>p</sub> = 0.2 × U<sub>vc</sub> / D<sub>j</sub>,  với  "
                "D<sub>j</sub> = 0.046 × F<sub>d</sub> × (F<sub>L</sub> × "
                "C<sub>v</sub>)<sup>0.5</sup>"))
    b.append(p("D<sub>j</sub> = đường kính tia phun (m); C<sub>v</sub> = hệ số lưu "
               "lượng thực tế. Đối với van góc và van quay xả trực tiếp vào đường "
               "ống hạ lưu:"))
    b.append(eq("f<sub>p</sub> = U<sub>vc</sub> / d<sub>i</sub>"))
    b.append(p("Mức L<sub>wi</sub> ứng với mức áp suất âm thanh (SPL) 111 dBA được "
               "cho trong ví dụ sau là 120 dBA."))
    b.append(p("Trong Hình 32, hãy xác định giao điểm giữa tần số và đường cong biểu "
               "diễn mức L<sub>wi</sub> 120 dB rồi đọc mức gia tốc ở bên trái. Giá trị "
               "gia tốc được cho bằng m/s². (Lưu ý 10 m/s² = 1 G, gia tốc của "
               "trọng lực.)"))
    b.append(p("Để thấy rõ cách áp dụng, hãy xem một trường hợp thử nghiệm thực địa. "
               "Giả sử có một van điều khiển góc 2-inch giảm 4 triệu SCFH khí thiên "
               "nhiên từ 4000 psia xuống 2300 psia. Cửa ra của van nối với một ống "
               "4-inch schedule 80. Mức áp suất âm thanh bên ngoài đo được là 111 dBA "
               "ở tần số đỉnh 4000 Hz; mức L<sub>wi</sub> đo được tại hiện trường là "
               "120 dB. Dùng 4000 Hz làm tần số và 120 làm mức công suất âm thanh, "
               "ta xác định được gia tốc 140 m/s² (14 G) từ Hình 32-1 (xem đường "
               "chấm). Điều này khớp với số liệu hiện trường là 120 dB L<sub>wi</sub> "
               "và 14 G. Người quan sát mô tả tiếng ồn tương tự như đứng cạnh một "
               "máy đập bê tông."))
    b.append(p("Mức gia tốc như vậy có thể gây mỏi lâu dài. Về sau, sự cố được giải "
               "quyết bằng cách lắp một van chống ồn đặc biệt (do chính tác giả "
               "thiết kế), đưa mức áp suất âm thanh xuống 78 dBA."))
    b.append(p("Có thể thấy thú vị khi truy nguyên nguồn gốc của tần số đỉnh 4000 Hz. "
               "Như thể hiện trong Hình 32-2, một tia phun âm thanh (ở đây là độ giảm "
               "áp bị chokes) thoát ra từ lỗ của van và đi vào đường ống hạ lưu, nơi "
               "nó tan vào rối loạn dữ dội và chuyển hóa thành động năng. Chính "
               "sự rối loạn này bên trong ống tạo ra tần số quan sát được. Đây là "
               "minh chứng:"))
    b.append(fig(2, F.fig_f322()))
    b.append(eq("f<sub>p</sub> = U<sub>vc</sub> / D<sub>i</sub> = 386 m/s / 0.097 m = "
                "3980 Hz ≈ 4000 Hz"))
    b.append(p("Ở đây, U<sub>vc</sub> là vận tốc tới hạn (vận tốc âm thanh) của khí "
               "thiên nhiên ở 70°F; D<sub>i</sub> là đường kính trong thực tế của ống "
               "4-inch schedule 80."))
    b.append(p("Ước tính áp suất âm thanh đã trở thành công việc thường quy khi lựa "
               "chọn van điều khiển cho các dịch vụ áp suất cao. Thế nhưng, mức rung "
               "liên quan vẫn thường bị bỏ qua, dù nó có thể gây hư hỏng đường ống "
               "và các phụ kiện gắn vào ống. Chương này chỉ ra một cách lấp đầy "
               "khoảng trống kiến thức đó."))
    b.append(h3("Tóm tắt", "Summary"))
    b.append(p("Các nhà máy điện hoặc cơ sở sản xuất khí thiên nhiên, chẳng hạn, cần "
               "mức giảm áp rất cao, thường với áp suất trên 1000 psi. Vì vậy, van "
               "thông thường dùng cho mục đích này có thể phát ra mức áp suất âm "
               "thanh cao và do đó cần được triệt tiêu bằng van chống ồn đặc biệt. "
               "Tuy nhiên, có những trường hợp vẫn dùng van thông thường (ví dụ, vì "
               "lý do chi phí) nếu tiếng ồn lớn chỉ kéo dài trong thời gian ngắn. "
               "Công suất âm thanh sinh ra vẫn có thể gây vấn đề cho đường ống hạ "
               "lưu. Ví dụ, một van điều khiển 2-inch lắp trong ống 4-inch, giảm "
               "20,000 lb/h hơi bão hòa từ 500 psia xuống 250 psia, có mức áp suất "
               "âm thanh bên ngoài 98 dB và mức công suất âm thanh 136 dB; với tần "
               "số đỉnh bên trong giả định 2200 Hz, nó tác động lên đường ống hạ "
               "lưu với gia tốc khoảng 100 m/s² (10 G)."))
    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([_READING]))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm năm trang in (185–189; "
                  "trang in = trang PDF + 7). Lớp văn bản của PDF làm sai lệch "
                  "(garbled) tất cả các phương trình; cả sáu phương trình đều được "
                  "chuyển chép từ các trang in được render. Các con số và tên tài "
                  "liệu gốc được giữ nguyên, gồm khảo sát Exxon (160 dB, 148 dB, "
                  "100 Hz → 60 G, 400 Hz → 100 G), ví dụ hiện trường (4 million "
                  "SCFH, 4000 → 2300 psia, 111 dBA, 140 m/s² (14 G), 78 dBA), "
                  "386 m/s / 0.097 m = 3980 Hz ≈ 4000 Hz và ví dụ hơi nước "
                  "(20,000 lb/h, 500 → 250 psia, 98 dB, 136 dB, 2200 Hz, "
                  "100 m/s² (10 G))."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. "
               "Nội dung gốc © 2011 Hans D. Baumann, xuất bản bởi ISA / "
               "John Wiley &amp; Sons.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Pipe Vibration Due to Sound", "Pipe Vibration Due to Sound"))
    b.append(p("About 40 years ago, Exxon Company conducted a survey based on its "
               "experience in refineries to determine at what sound level pipes "
               "could break. The limit seems to be a sound power level (Lwi) of "
               "160 dB. The graph in Figure 32-1 indicates that even at low "
               "vibration levels of 100 Hz (cps), one would exceed an acceleration "
               "of 60 G. Incidentally, an Lwi of 160 dB is equivalent to a sound "
               "pressure level (SPL) of 148 dB and a noise equivalent of a jet "
               "plane taking off. From Figure 32-1, one can see that at an Lwi of "
               "160 dB and a frequency of only 400 Hz, the acceleration reaches "
               "100 G."))
    b.append(p("Excessive vibration on pipes and attached equipment can cause "
               "serious problems because vibration-related acceleration can break "
               "pipe-attached sensing lines or even pipe support structures. "
               "Resonant vibration, when the internal frequency is close to the "
               "pipe’s coincident frequency, may lead to long-term fatigue of the "
               "pipe wall, resulting in cracks in the wall."))
    b.append(p("The correlation between sound power level and acceleration is "
               "shown in Figure 32-1. As shown, acceleration is directly "
               "proportional to frequency."))
    b.append(p("To calculate the acceleration level, one must convert the sound "
               "pressure level into a sound power level. Here is the equation:"))
    b.append(eq("L<sub>wi</sub> = 10 log(W<sub>a</sub> / 10<sup>−12</sup>)"))
    b.append(fig(1, F.fig_f321()))
    b.append(p("or"))
    b.append(eq("L<sub>wi</sub> = 120 + 10 log(M × c<sub>i</sub><sup>2</sup> / 2) + η  "
                "in dB"))
    b.append(p("where<br>"
               "L<sub>wi</sub> = internal sound power level, in dB<br>"
               "W<sub>a</sub> = internal sound power, in watts<br>"
               "M = mass flow in kg/s<br>"
               "c<sub>i</sub> = speed of sound of gas, m/s<br>"
               "SPL = external sound pressure level"))
    b.append(eq("η = 10 log (acoustic efficiency factor) = −40 dB for sonic speed "
                "of gases"))
    b.append(p("The internal peak frequency f<sub>p</sub> = 0.2 × U<sub>vc</sub> / "
               "D<sub>j</sub>, where"))
    b.append(eq("f<sub>p</sub> = 0.2 × U<sub>vc</sub> / D<sub>j</sub>,  where  "
                "D<sub>j</sub> = 0.046 × F<sub>d</sub> × (F<sub>L</sub> × "
                "C<sub>v</sub>)<sup>0.5</sup>"))
    b.append(p("D<sub>j</sub> = jet diameter (m); C<sub>v</sub> = actual flow "
               "coefficient. For angle valves and rotary valves charging directly "
               "into a downstream pipe,"))
    b.append(eq("f<sub>p</sub> = U<sub>vc</sub> / d<sub>i</sub>"))
    b.append(p("The L<sub>wi</sub> for a sound pressure level (SPL) of 111 dBA is "
               "given in the following example as 120 dBA."))
    b.append(p("In Figure 32, locate the intersection between the frequency and the "
               "curve representing 120 dB L<sub>wi</sub> and read the acceleration "
               "level at the left. Acceleration values are given in m/s². (Note "
               "that 10 m/s² = 1 G, the acceleration of gravity.)"))
    b.append(p("To better understand how this plays out, let us look at an actual "
               "field test case. Assume we have a 2-inch angle-type control valve "
               "reducing 4 million standard cubic feet per hour (SCFH) of natural "
               "gas from 4000 psia to 2300 psia. The valve outlet is attached to a "
               "4-inch schedule 80 pipe. The external sound pressure level was "
               "measured as 111 dBA at a peak frequency of 4000 Hz. The L<sub>wi</sub> "
               "from field measurements is 120 dB. Using 4000 Hz as frequency and "
               "120 as the sound power level, we identify an acceleration of "
               "140 m/s² (14 G) from Figure 32-1 (see the dotted line). This "
               "corresponds to field data of 120 dB L<sub>wi</sub> and 14 G. "
               "Observers reported a noise comparable to being next to a "
               "jackhammer."))
    b.append(p("Such acceleration levels could cause long-term fatigue. Later, the "
               "problem was solved by installing a special low-noise valve "
               "(designed by the author), dropping the sound pressure level to "
               "78 dBA."))
    b.append(p("It might be of interest to determine where the 4000 Hz peak "
               "frequency came from. As shown in Figure 32-2, a sonic jet (here we "
               "have a choked pressure drop) exits from the valve’s orifice and "
               "enters the downstream pipe, where it dissolves into violent "
               "turbulence and converts to kinetic energy. This turbulence inside "
               "the pipe creates the observed frequency. Here is the proof:"))
    b.append(fig(2, F.fig_f322()))
    b.append(eq("f<sub>p</sub> = U<sub>vc</sub> / D<sub>i</sub> = 386 m/s / 0.097 m = "
                "3980 Hz ≈ 4000 Hz"))
    b.append(p("Here, U<sub>vc</sub> is the sonic velocity of natural gas at 70°F; "
               "D<sub>i</sub> is the actual inside diameter of a 4-inch schedule 80 "
               "pipe."))
    b.append(p("Estimating sound pressure has become a routine effort when "
               "selecting control valves for high-pressure services. Yet, "
               "associated vibration levels are typically ignored despite the "
               "fact that they can lead to damage to the pipe and pipe-attached "
               "accessories. This chapter shows a way to fill this void in "
               "knowledge."))
    b.append(h3("Summary", "Summary"))
    b.append(p("Power plants or natural gas production facilities, for example, "
               "require high levels of pressure reduction, often involving "
               "pressures above 1000 psi. As a result, conventional valves used "
               "for this purpose can exhibit high sound pressure levels and, "
               "therefore, require suppression using special low-noise valves. "
               "Yet, there are some cases where conventional valves are used "
               "(e.g., for cost reasons) if the high sound is of short duration. "
               "The resultant sound power still may pose problems with the "
               "downstream pipe. For example, a 2-inch control valve installed in "
               "a 4-inch pipe reducing 20,000 lb/h saturated steam from 500 psia to "
               "250 psia has an external sound pressure level of 98 dB and a sound "
               "power level of 136 dB and, with an assumed internal peak frequency "
               "of 2200 Hz, will affect the downstream pipe with an acceleration "
               "level of about 100 m/s² (10 G)."))
    b.append(h3("Additional Reading", "Additional Reading"))
    b.append(ul([_READING]))
    b.append(note("<b>Source quirks.</b> The chapter spans five printed pages "
                  "(185–189; printed = PDF + 7). The PDF text layer garbled every "
                  "equation; all six displayed equations were transcribed directly "
                  "from the rendered page images. Original numbers and the "
                  "bibliographic reading item are retained, including the Exxon "
                  "survey (160 dB, 148 dB, 100 Hz → 60 G, 400 Hz → 100 G), the "
                  "field case (4 million SCFH, 4000 → 2300 psia, 111 dBA, "
                  "140 m/s² (14 G), 78 dBA), 386 m/s / 0.097 m = 3980 Hz ≈ "
                  "4000 Hz, and the steam example (20,000 lb/h, 500 → 250 psia, "
                  "98 dB, 136 dB, 2200 Hz, 100 m/s² (10 G))."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original "
               "content © 2011 Hans D. Baumann, published by ISA / John Wiley "
               "&amp; Sons.</i>"))
    return "".join(b)
