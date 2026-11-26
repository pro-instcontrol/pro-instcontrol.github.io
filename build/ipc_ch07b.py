# -*- coding: utf-8 -*-
"""Chapter 7, fanfold recorder continuation, 7.1.3-7.1.4 and start of 7.2.

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 334-336, printed pp. 322-324, decoded
text lines 12915-13050.  Figures 7.8-7.11 are placed at the printed
references.  Printed wording oddities are preserved in the English text.

The figure supplier `ipcfig7_a` is authored in parallel.  Until it is
importable, small vector redraws of the four printed diagrams are installed
as non-overwriting fallbacks; the real `fig_f08` ... `fig_f11` callables win
once the supplier registers them.
"""

import ipcfig7 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
_DEFS = (
    '<defs><marker id="ipc7bm" viewBox="0 0 8 8" refX="7" refY="4" '
    'markerWidth="6" markerHeight="6" orient="auto">'
    '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>'
)


def _t(x, y, s, size=8.0, anchor="middle", color="#1f3a5f"):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" fill="%s">'
            '%s</text>' % (x, y, anchor, size, color, s))


def _box(x, y, w, h, label="", fill="#eef3fb"):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" fill="%s" '
         'stroke="#1f3a5f" stroke-width="1"/>' % (x, y, w, h, fill)]
    if label:
        lines = str(label).split("\n")
        y0 = y + h / 2.0 - (len(lines) - 1) * 5.0 + 3.0
        for i, ln in enumerate(lines):
            o.append(_t(x + w / 2.0, y0 + i * 10, ln, 7.6))
    return "".join(o)


def _circ(cx, cy, r=3.0, fill="#ffffff"):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="#1f3a5f" '
            'stroke-width="1"/>' % (cx, cy, r, fill))


def _ar(x1, y1, x2, y2):
    return ('<path d="M%s %s L%s %s" fill="none" stroke="#1f3a5f" '
            'stroke-width="1.2" marker-end="url(#ipc7bm)"/>' % (x1, y1, x2, y2))


def _wire(pts, color="#1f3a5f", dash=False):
    d = "M" + " L".join("%s %s" % p for p in pts)
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="1.1"%s/>'
            % (d, color, ' stroke-dasharray="4 3"' if dash else ""))


def _stub_fig(n):
    o = [_DEFS]
    if n == 8:
        o.append(_t(340, 34, "Fanfold chart stack", 12))
        for i in range(5):
            y = 62 + i * 26
            dx = i * 5
            pts = [(120 + dx, y), (520 + dx, y),
                   (500 + dx, y + 18), (100 + dx, y + 18)]
            o.append('<polygon points="%s" fill="#eef3fb" '
                     'stroke="#1f3a5f" stroke-width="1"/>'
                     % " ".join("%s,%s" % p for p in pts))
            for k in range(5):
                o.append(_circ(150 + k * 85 + dx, y + 9, 1.6))
        o.append(_t(340, 214, "Model 05150 / 05116 / 05110", 9))
    elif n == 9:
        o.append(_t(340, 26, "Magnetic tape recorder", 12))
        o.append(_circ(200, 92, 26))
        o.append(_circ(200, 92, 5, fill="#9aa7b8"))
        o.append(_circ(480, 92, 26))
        o.append(_circ(480, 92, 5, fill="#9aa7b8"))
        o.append(_wire([(174, 92), (174, 152), (290, 152)]))
        o.append(_wire([(390, 152), (506, 152), (506, 92)]))
        o.append(_box(262, 152, 56, 22, fill="#dce6f7"))
        o.append(_t(290, 186, "Write head", 8))
        o.append(_box(362, 152, 56, 22, fill="#dce6f7"))
        o.append(_t(390, 186, "Read head", 8))
        o.append(_box(58, 66, 72, 32, "Amplifier"))
        o.append(_ar(20, 82, 58, 82))
        o.append(_t(18, 98, "Input", 8, anchor="start"))
        o.append(_ar(130, 82, 174, 92))
        o.append(_box(550, 66, 72, 32, "Amplifier"))
        o.append(_ar(506, 92, 550, 82))
        o.append(_ar(622, 82, 662, 82))
        o.append(_t(662, 98, "Output", 8, anchor="end"))
        o.append(_t(340, 216, "Plastic tape coated with magnetic material", 8))
    elif n == 10:
        o.append(_t(340, 28, "Digital magnetic recording - NRZ waveform", 11))
        o.append(_wire([(70, 120), (610, 120)]))
        o.append(_t(64, 123, "O", 9, anchor="end"))
        o.append(_wire([(70, 70), (610, 70)], dash=True))
        o.append(_wire([(70, 170), (610, 170)], dash=True))
        o.append(_t(606, 62, "Positive saturation level", 8, anchor="end"))
        o.append(_t(606, 187, "Negative saturation level", 8, anchor="end"))
        bits = "11101001"
        for i, bit in enumerate(bits):
            o.append(_t(100 + i * 60, 52, bit, 9))
        o.append(_wire([(100, 70), (280, 70), (280, 170), (340, 170),
                        (340, 70), (400, 70), (400, 170), (520, 170),
                        (520, 70), (580, 70)]))
        o.append(_wire([(100, 70), (100, 120)]))
        o.append(_wire([(580, 70), (580, 120)]))
    elif n == 11:
        o.append(_t(340, 24, "X-Y plotter servo system", 12))
        o.append(_t(16, 66, "X- input", 8, anchor="start"))
        o.append(_ar(72, 62, 100, 62))
        o.append(_box(100, 46, 92, 32, "Balancing\nsystem"))
        o.append(_box(216, 46, 82, 32, "Chopper\ncircuit"))
        o.append(_box(322, 46, 84, 32, "Servo-\namplifier"))
        o.append(_ar(192, 62, 216, 62))
        o.append(_ar(298, 62, 322, 62))
        o.append(_ar(406, 62, 444, 62))
        o.append(_circ(452, 62, 5))
        o.append(_ar(457, 62, 500, 62))
        o.append(_t(452, 48, "Pen drive servo", 7.6))
        o.append(_box(100, 158, 92, 32, "Balancing\nsystem"))
        o.append(_box(216, 158, 82, 32, "Chopper\ncircuit"))
        o.append(_box(322, 158, 84, 32, "Servo-\namplifier"))
        o.append(_ar(192, 174, 216, 174))
        o.append(_ar(298, 174, 322, 174))
        o.append(_ar(406, 174, 444, 174))
        o.append(_circ(452, 174, 5))
        o.append(_ar(457, 174, 500, 174))
        o.append(_t(452, 194, "Assembly drive servo", 7.6))
        o.append(_box(100, 102, 92, 34, "Standard\nsupply"))
        o.append(_wire([(146, 102), (146, 78)]))
        o.append(_wire([(146, 136), (146, 158)]))
        o.append(_t(146, 151, "Eb", 8))
        o.append(_t(16, 178, "Y- input", 8, anchor="start"))
        o.append(_ar(72, 174, 100, 174))
        o.append(_box(500, 38, 150, 138, fill="#f7f9fc"))
        o.append(_t(575, 52, "Chart paper", 8))
        o.append(_wire([(548, 70), (548, 142)], color="#9aa7b8"))
        o.append(_wire([(602, 70), (602, 142)], color="#9aa7b8"))
        o.append(_wire([(540, 96), (610, 96)], color="#c0392b"))
        o.append(_t(566, 90, "Pen and arm", 7.6, color="#c0392b"))
        o.append(_ar(620, 78, 620, 58))
        o.append(_ar(620, 58, 620, 78))
        o.append(_t(626, 68, "Movement", 7.4, anchor="start"))
        o.append(_t(575, 166, "Complete assembly movement", 7.4))

    o.append(_t(340, 242, "Hình 7.%d   ·   Figure 7.%d" % (n, n), 6.4,
                color="#888888"))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg,
            "Hình 7.%d · %s" % (n, {
                8: "Chồng giấy biểu đồ gấp kiểu quạt",
                9: "Máy ghi băng từ với đầu ghi và đầu đọc",
                10: "Dạng sóng bão hòa số trên băng từ",
                11: "Hệ thống servo máy vẽ X-Y"}[n]),
            "Figure 7.%d · %s" % (n, {
                8: "Stack of fanfold chart paper",
                9: "Magnetic tape recorder with write and read heads",
                10: "Digital saturation waveform on magnetic tape",
                11: "X-Y plotter servo system"}[n]),
            "Sơ đồ minh họa Hình 7.%d" % n,
            "Illustration for Figure 7.%d" % n)


for _n in (8, 9, 10, 11):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _stub_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------- (iii) Fanfold chart, cont.
    P(b, lang,
      "cả hai kích thước máy ghi đã mô tả ở trên, được xếp đều đặn lớp này "
      "chồng lên lớp kia và ép chặt để tạo thành hình dáng hoàn chỉnh. "
      "Việc lắp đặt loại giấy biểu đồ này rất dễ dàng. Giấy được đặt trực "
      "tiếp vào đúng phần của máy ghi dành cho nó. Các rãnh được đục ở cả "
      "hai góc ngoài cùng của giấy biểu đồ, dùng để cố định các góc của "
      "giấy vào răng của con lăn như minh họa trong Hình 7.8. Con lăn được "
      "nối với mô tơ dẫn giấy thông qua hệ thống bánh răng. Khi bắt đầu "
      "ghi, giấy biểu đồ đi qua các răng của con lăn và sau khi in xong "
      "sẽ mở ra ở phần bên kia của máy ghi.",
      "the sizes of recorder described earlier and arranged systematically "
      "one fold on the other and pressed hard to give the perfect shape. "
      "The installation of such chart is easy. It is placed physically on "
      "the section of the recorder meant for it. Grooves are punched on "
      "both the extreme corners of the chart paper which are used for "
      "fixing the corners of the chart on the roller teeth as shown in "
      "Figure 7.8. The roller is connected to the chart drive motor through "
      "gear system. When recording starts, chart moves through the teeth "
      "of the roller and unwinds on other section of the recorder after "
      "printing.")
    FIG(b, 8, F.fig_f08(), lang)

    # ------------------------------------------------------------- 7.1.3
    H(b, lang, "7.1.3 Hệ thống ghi từ tính",
      "7.1.3 Magnetic Recording System", level=3)
    P(b, lang,
      "Trong khi các máy ghi mô tả ở trên đều là loại dẫn động bằng chuyển "
      "động cơ học, hệ thống ghi từ tính lại khai thác đặc tính từ của vật "
      "liệu từ tính. Một dải băng nhựa mỏng có độ rộng thích hợp được phủ "
      "một lớp vật liệu từ tính, tốt nhất là oxit sắt. Toàn bộ cuộn băng "
      "nhựa này được di chuyển tuyến tính giữa hai con lăn. Trong lúc "
      "chuyển động, băng đi ngang qua một đầu từ hóa, đầu này tạo lên bề "
      "mặt từ tính những vết từ dư. Tín hiệu đầu vào cần ghi được khuếch "
      "đại bởi một bộ khuếch đại ghi. Khi tín hiệu này được đưa tới đầu "
      "ghi, nó tạo ra sự thay đổi độ từ hóa của các hạt từ tính trên băng. "
      "Ở chiều ngược lại, để đọc nội dung tín hiệu, đầu đọc bắt lấy sự "
      "thay đổi từ trở của mạch từ của nó và cảm ứng một điện áp tỷ lệ "
      "trong cuộn dây đặt trên đầu đọc. Vì điện áp cảm ứng tỷ lệ với tốc độ "
      "thay đổi của từ thông, hệ thống không thể làm việc với điện áp một "
      "chiều (D.C.). Bộ khuếch đại đầu đọc khuếch đại tín hiệu đọc và đưa "
      "ra đầu ra. Hệ thống được biểu diễn dưới dạng sơ đồ khối trong Hình "
      "7.9. Hệ thống này có thể làm việc trong dải tần từ 100 Hz đến 2 MHz.",
      "Whereas the recorders described above are of physical motion drive "
      "recorder, the magnetic recording system utilizes the magnetic "
      "property of magnetic material. A thin sheet of plastic tape of "
      "sufficient width is coated with magnetic material preferably with "
      "oxides of iron. The complete reel of this plastic tape is moved "
      "linearly between the two rollers. While moving, it passes across a "
      "magnetization head that puts a residual magnetic dot upon the "
      "magnetic surface. The input signal which has to be recorded is "
      "amplified by a write/record amplifier. This signal when applied to "
      "the write head creates a change in magnetization of the magnetic "
      "particles on the tape. For reading the signal content, on the other "
      "hand, the read head captures reluctance-change of its magnetic "
      "circuitry and induces a proportional voltage in the winding located "
      "on the read head. Since the induced voltage is proportional to the "
      "rate of change of magnetic flux, the system cannot work on D.C. The "
      "read head amplifier amplifies the read signal and gives output. The "
      "system has been shown in block diagram representation in Figure "
      "7.9. This system can work between frequency range 100 Hz and 2 "
      "Mega Hz.")
    FIG(b, 9, F.fig_f09(), lang)
    P(b, lang,
      "Hệ thống ghi này có hai công dụng rất lớn. Một là có thể dùng để ghi "
      "phổ thông tin dao động của các máy tốc độ cao, với mối quan hệ giữa "
      "tần số dao động và biên độ dao động. Công dụng quan trọng khác là nó "
      "có thể ghi các tín hiệu âm thanh rất hiệu quả.",
      "There is two great usefulness of this recording system. One is that "
      "it can be used to record spectrum of vibration information of "
      "high-speed machines contained in between the relation of frequency "
      "of vibration and amplitude of vibration. Another important "
      "usefulness is that it can record audio signals quite efficiently.")

    # ------------------------------------ Frequency Modulation Recording
    H(b, lang, "Hệ thống ghi điều chế tần số",
      "Frequency Modulation Recording System", level=4)
    P(b, lang,
      "Hệ thống này về bản chất cũng là một hệ thống từ tính, nhưng việc "
      "điều chế cho phép dải tần làm việc ở mức thấp mở rộng cả xuống đến "
      "điện áp một chiều (D.C.). Tần số điều khiển fc được chọn dựa trên "
      "tốc độ băng, và độ lệch dự kiến của băng là ± 40% quanh tần số sóng "
      "mang. Các thành phần khác của hệ thống vẫn giữ nguyên như đầu ghi, "
      "đầu đọc, v.v. Trước hết, tần số sóng mang fc do một bộ dao động tạo "
      "ra được điều chế theo mức tín hiệu đầu vào. Khi tín hiệu đầu vào "
      "hoàn toàn vắng mặt (miền vào bằng không), quá trình điều chế diễn "
      "ra ở tần số điều khiển. Nếu tín hiệu đầu vào là một chiều (D.C.), "
      "đầu ra đã điều chế sẽ có tần số không đổi, nhưng đối với tín hiệu "
      "xoay chiều (A.C.), đầu ra đã điều chế sẽ có dải tần thay đổi. Ở "
      "chiều ngược lại, bộ giải điều chế chuyển đổi tần số chênh lệch giữa "
      "tần số trung tâm và tần số của băng thành một điện áp tỷ lệ với "
      "tần số chênh lệch đó.",
      "This system is also essentially a magnetic system but modulation "
      "allows the lower frequency range of operation to extend upto D.C. "
      "as well. Control frequency fc is chosen in comparison to tape speed "
      "and the deviation expected for the tape is ± 40% around the carrier "
      "frequency. Other things in the system remains the same as write "
      "head or read head, etc. First of all carrier frequency fc generated "
      "by an oscillator is modulated according to the input signal level. "
      "When the input signal is completely absent (zero input range), "
      "modulation shall be at the control frequency. If the input signal "
      "is D.C., the modulated output shall have constant frequency but for "
      "an A.C. input signal the modulated output shall have variable "
      "frequency range. The demodulator, on the other hand, converts the "
      "differential frequency of the central and that of the tape to a "
      "voltage which is proportional to the differential frequency.")

    # ------------------------------------------------------------- 7.1.4
    H(b, lang, "7.1.4 Hệ thống ghi từ tính kỹ thuật số",
      "7.1.4 Digital Magnetic Recording System", level=3)
    P(b, lang,
      "Hệ thống ghi từ tính kỹ thuật số ban đầu được thiết kế cho các công "
      "việc xử lý dữ liệu số của máy tính. Hiện nay, vì hầu hết các hệ "
      "thống đo lường đều dựa trên dữ liệu số hoặc trên máy tính, hệ "
      "thống ghi này cũng được dùng để ghi các tín hiệu số của thiết bị "
      "đo. Trong phương pháp ghi này, băng luôn được giữ ở trạng thái bão "
      "hòa từ tính hoàn toàn theo một trong hai chiều (dương hoặc âm). "
      "Dữ liệu số dưới dạng ký tự được mã hóa trên băng, trên đúng rãnh, "
      "theo sự kết hợp của các bit 1. Một định dạng ghi chuẩn công nghiệp "
      "do IBM thiết kế được dùng để ghi dữ liệu số liên quan đến đo "
      "lường. Định dạng này được gọi là NRZ (không trở về 0). NRZ dùng sự "
      "thay đổi hướng của từ thông tại một vị trí xác định trên băng để "
      "biểu thị bit 1 và ngược lại, dùng từ thông không đổi để biểu thị "
      "bit 0. Dựa trên định dạng này, số nhị phân 11101001 đã được mã hóa "
      "bằng mẫu từ thông của hệ thống NRZ trong Hình 7.10.",
      "Digital magnetic recording system has been originally designed for "
      "computer digital data processing works. Now since most of the "
      "instrumentation systems are digital data based or computer based, "
      "this recording system is being used for recording of instrumentation "
      "digital signal as well. In this system of recording, a tape is kept "
      "under complete magnetic saturation in either direction (positive or "
      "negative). The digital data in character form is coded on the tape "
      "in the right track in combination of 1-bit. Industry standard IBM "
      "designed recording format is used for recording of instrumentation "
      "related digital data. This format is known as NRZ (Non-Return Zero). "
      "The NRZ uses the change of direction of flux on the particular "
      "location on the tape for indicating 1-bit and in opposite to that a "
      "constant flux for indicating 0 bit. Based on this format, a binary "
      "number 11101001 has been coded by the flux pattern of NRZ system in "
      "Figure 7.10.")
    FIG(b, 10, F.fig_f10(), lang)
    P(b, lang,
      "Việc ghi số trên băng hoạt động theo hai cách: một là cách ghi gia "
      "tăng, hai là cách ghi đồng bộ. Ở dạng ghi gia tăng, hệ thống tiến "
      "thêm một bước sau mỗi lần ghi một ký tự. Nhờ cách này, ngay cả khi "
      "dữ liệu đến không liên tục hoặc tốc độ đến chậm, hệ thống vẫn đặt "
      "mỗi ký tự dọc theo băng ghi với khoảng cách đều nhau.",
      "Digital recording on tapes functions in two ways, one in "
      "incremental way and the other in synchronous way. In incremental "
      "form of recording, the system increments each step after recording "
      "one character at a time. In this way if the data is in discontinuous "
      "form or even slow in arrival speed, the system places each character "
      "along the recording tape in equal space.")
    P(b, lang,
      "Ở dạng ghi đồng bộ, ngược lại, băng của máy ghi được cho di chuyển "
      "với tốc độ không đổi và dữ liệu được ghi theo từng khối. Hai khối "
      "được ngăn cách bởi một khe hở (khoảng trống). Nhờ cách này, các "
      "khối dữ liệu lớn được ghi trong thời gian rất ngắn vì băng ghi "
      "khởi động tức thì và cũng dừng lại ngay lập tức.",
      "In synchronous form of recording, on the other hand, the recorder "
      "tape is allowed to move at a constant speed and data is recorded in "
      "blocks. Two blocks are separated by a gap (empty space). In this "
      "way large blocks of data are recorded within no time because the "
      "recorder tape takes instant start and is stopped also instantly.")
    P(b, lang,
      "Điều quan trọng nhất về ghi từ tính là các vấn đề méo dạng và phi "
      "tuyến tính hoàn toàn không xuất hiện ở đây. Lý do là ghi từ tính "
      "chỉ cần cực tính đúng của dòng điện để có độ từ hóa đúng. Hai loại "
      "sai số có thể gặp trong hệ thống ghi từ tính là mất một xung và "
      "xuất hiện thêm một xung giả trong khối dữ liệu bình thường. Để "
      "kiểm tra các loại sai số này, người ta dùng hệ thống kiểm tra bit "
      "chẵn lẻ.",
      "The most important facts about magnetic recording are that the "
      "problems of distortion and non-linearity are completely absent "
      "here. This is because the magnetic recording needs only correct "
      "polarity of current for correct magnetization. Two kinds of error "
      "that can be expected from magnetic recording system are loss of a "
      "pulse and addition of a spurious pulse in the normal data block. To "
      "have a check on these types of error parity bit checker system is "
      "used.")

    # --------------------------------------------------------------- 7.2
    H(b, lang, "7.2 Máy vẽ X-Y", "7.2 X-Y PLOTTER", level=3)
    P(b, lang,
      "Ngoài công tác nghiên cứu và phát triển, các ngành công nghiệp quá "
      "trình cũng cần ghi lại biến số dưới dạng Y = f (x). Đồ thị kết hợp "
      "của hai biến phụ thuộc thời gian được gọi là đồ thị X-Y. Ví dụ, "
      "trong hệ thống điều khiển đón đầu, đồ thị lưu lượng nước – lưu "
      "lượng hơi là một đồ thị X-Y. Tương tự, trong hệ thống giám sát dao "
      "động của máy tốc độ cao, đồ thị kết hợp tần số dao động – biên độ "
      "dao động là một ví dụ khác về đồ thị X-Y. Các đồ thị này cho thấy "
      "sự biến đổi trực tiếp của đại lượng này đối với đại lượng kia và "
      "là một thông số quan trọng cho việc phân tích và ra quyết định "
      "thiết kế ở cấp cao hơn.",
      "In addition to research and development work, process industries "
      "also need to have record of variable in the form of Y = f (x). The "
      "combined plot of two-time dependent variables is called an X-Y "
      "plot. For example, in feedforward control system, water flow-steam "
      "flow plot is an X-Y plot. Similarly, in vibration monitoring system "
      "of high-speed machines, the combined plot of vibration "
      "frequency-vibration amplitude is another example of an X-Y plot. "
      "These plots give direct variation with respect to one another and "
      "is an important parameter for higher level of analysis and design "
      "decisions.")
    P(b, lang,
      "Trong một thiết kế máy vẽ X-Y loại tương tự như vậy, cụm tay viết "
      "và bút được dẫn chuyển động thẳng theo hướng X trên một tờ giấy "
      "biểu đồ cố định dạng ô kẻ. Tờ biểu đồ được giữ đúng vị trí bằng tĩnh "
      "điện hoặc dưới tác dụng của chân không. Cụm này có hai kiểu chuyển "
      "động. Tay cùng với bút di chuyển theo hướng X và được điều khiển "
      "bởi động cơ servo theo biến đầu vào X. Chuyển động kia của hệ "
      "thống là theo hướng Y, nơi đặt toàn bộ cụm mang tay và bút. "
      "Chuyển động này được điều khiển bởi một động cơ servo khác theo "
      "biến đầu vào Y. Như vậy, sự kết hợp hai chuyển động cho ra đồ thị "
      "X-Y, tức là đồ thị của Y theo X của hệ thống, như sơ đồ khối trong "
      "Hình 7.11.",
      "In one such design of X-Y plotter of Analog type, the writting arm "
      "and pen assembly is directed to move linearly in X-direction on a "
      "fixed graph-like chart paper. The chart is held in its proper place "
      "electrostatically or under the influence of vacuum. There are two "
      "types of movement of the assembly. The arm along with the pen moves "
      "in X-direction and is controlled by the servomotor with respect to "
      "X-input variable. The other movement of the system is in Y-direction "
      "where the complete assembly upon which the arm and pen are "
      "installed. This movement is controlled by another servomotor with "
      "respect to Y-input variable. Thus, the combined movement gives X-Y "
      "plot, i.e. the plot of Y with respect to X of the system as shown in "
      "the block diagram in Figure 7.11.")
    FIG(b, 11, F.fig_f11(), lang)

    return b
