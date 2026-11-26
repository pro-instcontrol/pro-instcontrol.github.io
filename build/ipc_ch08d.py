# -*- coding: utf-8 -*-
"""Chapter 8, section d (PDF pp. 366-375; printed pp. 354-363).

The system bus and its synchronous/asynchronous protocols, interrupt services
(IRQ/INTA, polled and vectored interrupts), communication protocols and network
topologies, followed by Modbus, ABDH, ARCNET, IEEE 1118, PROFIBUS and FIP.
Figures 8.15 - 8.20 are embedded in source order.
"""
import ipcfig8 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS

# Figure suppliers 10-18 and 19-26 may not have landed yet. Install
# *non-overwriting* fallbacks so section() can be compiled and QA-checked in
# isolation; a real supplier callable always wins.
_STUB_CAPTIONS = {
    15: ("Hình 8.15 · Vi xử lý với nhiều thiết bị tạo ngắt qua đường IRQ và INTA",
         "Figure 8.15 · Microprocessor with multiple interrupting devices "
         "through IRQ and INTA lines"),
    16: ("Hình 8.16 · Cấu trúc mạng bus với bốn thiết bị trên đường bus chung",
         "Figure 8.16 · Bus network topology with four devices on a common bus"),
    17: ("Hình 8.17 · Cấu trúc mạng vòng với bốn thiết bị trên vòng kín",
         "Figure 8.17 · Ring network topology with four devices on a closed loop"),
    18: ("Hình 8.18 · Cấu trúc mạng sao với bốn thiết bị quanh thiết bị chủ",
         "Figure 8.18 · Star network topology with four devices around a "
         "master device"),
    19: ("Hình 8.19 · Mạng Modbus đa nhánh với một thiết bị chủ và các thiết bị "
         "tớ qua modem",
         "Figure 8.19 · Modbus multi-drop network with one master and slave "
         "devices through modems"),
    20: ("Hình 8.20 · Khung thông điệp Modbus: địa chỉ thiết bị tớ, mã chức "
         "năng, thanh ghi bắt đầu, số thanh ghi và mã kiểm tra",
         "Figure 8.20 · Modbus message frame: slave address, function code, "
         "starting register, number of registers and check code"),
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

    H(b, lang, "8.4 Hệ thống bus, dịch vụ ngắt và giao thức truyền thông",
      "8.4 Bus System, Interrupt Services and Communication Protocols", level=2)
    H(b, lang, "Hệ thống bus", "Bus System", level=3)

    P(b, lang,
      "Truyền dữ liệu đã được thảo luận khá kỹ trong chương Đo từ xa, nhưng đối "
      "với các ứng dụng thiết bị đo dựa trên vi xử lý, truyền dữ liệu song song "
      "và nối tiếp giữa các giao tiếp của chúng, cũng như giữa sơ đồ thiết bị "
      "đầu dò-bộ thu, cần được bàn thêm. Về vấn đề này, chúng ta muốn nhắc lại "
      "sơ đồ kiến trúc vi xử lý hướng bus trong Hình 8.2, trong đó vi xử lý được "
      "nối với bộ nhớ (chứa cả chương trình lẫn dữ liệu) và với các thiết bị I/O "
      "qua các bus địa chỉ, điều khiển và dữ liệu. Các bus này về bản chất là "
      "bus song song, có ít nhất tám dây song song cho tín hiệu số tám bit. Đối "
      "với sơ đồ tương tự dùng mười sáu bit, sẽ có mười sáu dây song song, và cứ "
      "thế. Như trong hình, bus dữ liệu và các đường điều khiển đều hai chiều "
      "cho cả ba đơn vị được nối, nhưng bus địa chỉ thì một chiều vì vi xử lý là "
      "nguồn duy nhất thực hiện chức năng tạo địa chỉ. Ba bus kể trên là bus ở "
      "cấp hệ thống. Các bus ở cấp linh kiện nằm bên trong vi xử lý và không "
      "thuộc phạm vi thảo luận ở giai đoạn này. Còn một loại bus khác gọi là bus "
      "liên hệ thống, hỗ trợ kết nối nhiều hệ thống bất kỳ qua vi xử lý để truyền "
      "thông bằng các giao thức thích hợp.",
      "Data transmission has been discussed at length in the Telemetry chapter "
      "but, for microprocessor-based instrumentation applications, parallel as "
      "well as serial data transmission amongst their interfaces and between "
      "the transducer-receiver instrument scheme need more discussion. For "
      "this, we would like to refer once again to the diagram on Figure 8.2 of "
      "the bus-oriented microprocessor architecture system, wherein the "
      "microprocessor has been connected to the memory unit (having stored "
      "program as well as data) and to I/O devices through address, control and "
      "data buses. These buses are essentially parallel buses having a minimum "
      "of eight parallel wires for eight-bit digital signalling. For a similar "
      "scheme having sixteen bits, there shall be sixteen parallel wires, and "
      "so on. As shown, the data bus as well as the control lines are "
      "bidirectional for all three connected units but the address bus is "
      "unidirectional since the microprocessor is the only source of address "
      "generation function. The three buses mentioned above are system-level "
      "buses. The component-level buses are placed inside the microprocessor "
      "and does not constitute topic of our discussion at this stage. There is "
      "another type of bus which is called inter-system bus which supports "
      "connection of any multiple system through the microprocessor for "
      "communication by means of suitable protocols.")

    P(b, lang,
      "Bus hệ thống gồm ba vấn đề rất quan trọng: giao tiếp vào (tạo đệm giữa "
      "nguồn và bus dữ liệu), giao tiếp ra (chốt các bit thông tin có trên bus "
      "dữ liệu), và quan trọng nhất là chức năng giải mã địa chỉ, cuối cùng "
      "quyết định lựa chọn trong hai giao tiếp trên giao tiếp nào được nối vào "
      "bus dữ liệu và vào thời điểm nào. Tuy nhiên, các việc này được vi xử lý "
      "thực hiện rất thuận tiện nhờ cổng ba trạng thái (một giao tiếp vào), mạch "
      "chốt (một giao tiếp ra) và mạch giải mã địa chỉ kết hợp với các tín hiệu "
      "điều khiển thích hợp, ví dụ IOW (ghi I/O), IOR (đọc I/O), MEMR (đọc bộ "
      "nhớ), MEMW (ghi bộ nhớ) và CS (đường chọn chip). Những tín hiệu điều "
      "khiển này rất quan trọng, vì chính chúng hoàn thành thành công các thao "
      "tác truyền dữ liệu. Thao tác truyền dữ liệu thường chiếm một chu kỳ thời "
      "gian của vi xử lý, và yêu cầu đặt ra là mọi thiết bị được nối đều phải "
      "hoàn thành thao tác của mình trong chu kỳ thời gian này. Đây được gọi là "
      "giao thức bus đồng bộ, có tần số về cơ bản phụ thuộc vào tốc độ của "
      "thiết bị chậm nhất trong hệ thống. Sự khác biệt về thời gian đáp ứng "
      "giữa các thiết bị được nối là hạn chế của giao thức bus đồng bộ. Giải "
      "pháp rõ ràng được áp dụng ở đây trong các phương pháp ứng dụng vi xử lý "
      "là hệ thống tín hiệu điều khiển I/O bắt tay, gồm tín hiệu Yêu cầu dữ liệu "
      "(do giao tiếp I/O của thiết bị chậm hơn tạo ra) rồi đến tín hiệu Chờ (do "
      "thiết bị chậm tạo ra để báo cho vi xử lý).",
      "The system bus constitutes three very important considerations: input "
      "interface (providing buffering between source and data bus), output "
      "interface (providing latching of information bits available from data "
      "bus) and above all is the address decoding function which ultimately "
      "finalises the selection of the above two as to which input or the output "
      "interface shall be connected to data bus and at what timing. These are, "
      "however, performed by the microprocessor very conveniently by the help "
      "of a three-state gate (an input interface), a latch circuit (an output "
      "interface) and an address decoder circuit in combination with "
      "appropriate control signal, e.g. IOW (I/O Write); IOR (I/O Read); MEMR "
      "(memory read); MEMW (memory write) and CS (chip select line). These "
      "control signals are very important which ultimately accomplish "
      "successful data transfer operations. The data transfer operation usually "
      "takes one microprocessor cycle time and the requirement imposed by the "
      "microprocessor is that all the connected devices should complete their "
      "operations within this time cycle. This is called synchronous bus "
      "protocol, frequency of which is essentially dependent upon the speed of "
      "the slowest device present in the system. The difference in response "
      "time amongst various connected devices constitutes limitation for "
      "synchronous bus protocol. A handshake I/O control signalling system "
      "consisting of Data-Request (generated within the I/O interface of slower "
      "device) followed by Wait (generated by slower device to signal the "
      "microprocessor) is the obvious solution which is applied in this case by "
      "the microprocessor application methodologies.")

    P(b, lang,
      "Vi xử lý tạo ra các trạng thái chờ cần thiết nếu chu kỳ thời gian đã "
      "phân bổ cho một lần truyền dữ liệu là không đủ. Mặt khác, trong giao thức "
      "bus không đồng bộ, tín hiệu Yêu cầu dữ liệu là một phần của bus điều "
      "khiển và các thiết bị đáp ứng bằng tín hiệu Chờ để truyền dữ liệu.",
      "The microprocessor generates necessary wait states if the allotted time "
      "cycle for a data transfer is not sufficient. On the other hand, in "
      "asynchronous bus protocol the Data-Request signal is part of control bus "
      "and devices respond with a Wait signal for transfer of data.")

    # ---------------------------------------------------------- 8.4.1
    H(b, lang, "8.4.1 Dịch vụ ngắt", "8.4.1 Interrupt Services", level=3)

    P(b, lang,
      "Trong trường hợp bình thường, vi xử lý thường chạy tuần tự các chương "
      "trình đã định mà không bị gián đoạn. Trong khi đó, nếu một biến quá trình "
      "nào đó đạt giá trị bất thường đòi hỏi vi xử lý phải thực hiện hành động "
      "thích hợp để giữ biến ở giá trị bình thường ban đầu, thì cần có một sự "
      "gián đoạn ở phía vi xử lý. Sự gián đoạn đột ngột nhưng quan trọng này là "
      "một phần của thiết kế hệ thống thời gian thực và được gọi là dịch vụ "
      "ngắt. Ngắt được triển khai trên thực tế thông qua các chương trình con "
      "phục vụ ngắt. Chương trình con phục vụ ngắt hỗ trợ mọi ngắt do các nguồn "
      "khác nhau tạo ra, được thiết kế cho các quá trình thời gian thực.",
      "In normal case, a microprocessor usually runs through defined programs "
      "in sequence uninterruptively. In the meanwhile, if any process variable "
      "attains abnormal value which requires suitable action to be taken by the "
      "microprocessor for keeping the variable at its original normal value, an "
      "interruption on the part of microprocessor is necessary. Such sudden but "
      "important interruption is part of the real-time system design and is "
      "called interrupt services. The interrupt is implemented practically "
      "through interrupt service routines. Interrupt services routine supports "
      "all interrupts generated by various sources designed for the real time "
      "processes.")

    P(b, lang,
      "Tuy nhiên, việc xác định một ngắt cụ thể (nếu chỉ có một ngắt được khởi "
      "phát) hoặc giải quyết xung đột khi có nhiều ngắt được khởi phát cùng lúc "
      "(dựa trên sơ đồ ưu tiên) là rất quan trọng. Hai sơ đồ ngắt nổi tiếng "
      "được áp dụng để đạt mục đích này: ngắt thăm dò và ngắt vectơ. Sơ đồ khối "
      "của nhiều thiết bị tạo ngắt được trình bày trong Hình 8.15, cùng với IRQ "
      "(ngắt) và INTA (xác nhận ngắt). Vi xử lý đáp ứng IRQ thông qua INTA.",
      "However, identification of a particular interrupt (if only one has been "
      "initiated) or resolving conflict in the event of multiple interrupt "
      "initiation, (based on a priority scheme) is important. Two well-known "
      "interrupt schemes are applied to accomplish the purpose: polled "
      "interrupt and vectored interrupt. A block diagram representation of "
      "multiple interrupting devices has been shown in Figure 8.15 alongwith "
      "IRQ (interrupt) and INTA (interrupt acknowledge). The microprocessor "
      "responds to IRQ through INTA.")
    FIG(b, 15, F.fig_f15(), lang)

    P(b, lang,
      "Nhìn chung, các thiết bị tạo ngắt được trang bị đơn vị logic cần thiết "
      "để tạo IRQ. Bit trạng thái cũng được đặt tương ứng nhằm xác định thiết "
      "bị tạo ngắt. Bit này được vi xử lý đọc, và sau khi thao tác đọc kết thúc, "
      "bit trạng thái được đưa về trạng thái bình thường để chuẩn bị cho một "
      "lần khởi phát ngắt khác.",
      "In general, the interrupting devices are equipped with necessary logic "
      "unit for generating an IRQ. The status bit also accordingly is set for "
      "identifying the interrupting device. This is read by the microprocessor "
      "and after the read operation is over, the status bit is normalised for "
      "another interrupt initiation.")

    P(b, lang,
      "Thăm dò về cơ bản là quá trình do phần mềm điều khiển, trong đó vi xử lý "
      "đọc lần lượt từng bit trạng thái của các thiết bị tạo ngắt được nối. "
      "Trước hết, IRQ kích hoạt bộ điều khiển trình tự để khởi động chương trình "
      "con phục vụ ngắt, chương trình này bắt đầu thăm dò các thiết bị. Các vi "
      "xử lý có vectơ được chỉ định để biết vị trí của chương trình con phục vụ "
      "ngắt. Bộ điều khiển trình tự cung cấp địa chỉ của chương trình con phục "
      "vụ ngắt từ vị trí vectơ, sau đó tự động nhảy đến chương trình con đó.",
      "Polling is essentially a software operated process where the "
      "microprocessor reads one-by-one the connected interrupting devices "
      "status bit. First the IRQ enables the sequence controller for initiating "
      "the interrupt services routine which starts polling the devices. The "
      "microprocessors have designated vector to know the location of the "
      "interrupt services routine. The sequence controller provides the address "
      "of interrupt services routine from the vectored location and then "
      "automatically branches to the routine.")

    P(b, lang,
      "Một cách khác để giải quyết xung đột giữa nhiều thiết bị tạo ngắt là hệ "
      "thống ngắt vectơ. Thực chất, vectơ là một vị trí địa chỉ của chương trình "
      "con phục vụ ngắt sẽ được thực thi. Các thiết bị tạo ngắt đặt các địa chỉ "
      "vectơ lên bus dữ liệu bằng INTA. Đây là cách thông thường để nhận diện "
      "một IRQ vectơ. Trong một phiên bản khác của IRQ vectơ, vi xử lý cung cấp "
      "nhiều đầu vào IRQ và có các vị trí bộ nhớ cụ thể dành riêng cho từng IRQ "
      "vectơ. Thiết kế này đã được triển khai khá thành công trong các bộ điều "
      "khiển lập trình đa chức năng hiện đại tại một trạm, trong đó nhiều tính "
      "năng I/O đã được tích hợp vào bộ điều khiển. IRQ vectơ linh hoạt và tác "
      "động nhanh, nhưng đòi hỏi phần cứng bổ sung nên trở nên đắt đỏ và phức "
      "tạp.",
      "Another way to resolve the conflict amongst several interrupting devices "
      "is vectored interrupt system. Vector is in fact an address location of "
      "interrupt services routine which is to be executed actually. The "
      "interrupting devices place the vector addresses onto the Data bus using "
      "INTA. This is a normal way of recognizing a vectored IRQ. In another "
      "version of vectored IRQ, the microprocessor provides multiple IRQ input "
      "connection and have specific memory locations dedicated to each of the "
      "vectored IRQ. This design has been implemented quite successfully in "
      "modern single station, multifunction programmable controller wherein "
      "several I/O features have been integrated into the controller. The "
      "vectored IRQ is flexible and is fast acting but requires additional "
      "hardware and therefore, becomes expensive as well as complicated.")

    P(b, lang,
      "Để hỗ trợ hoạt động của dịch vụ ngắt, một bộ điều khiển ngắt lập trình "
      "cũng được giao tiếp với vi xử lý. Bộ điều khiển này giải quyết ưu tiên "
      "của nhiều thiết bị tạo ngắt bằng kỹ thuật giải quyết ưu tiên phần mềm "
      "(trong trường hợp hệ thống ngắt thăm dò) hoặc bằng kỹ thuật giải quyết "
      "ưu tiên phần cứng (trong trường hợp hệ thống ngắt vectơ). Nhờ cách này, "
      "vi xử lý có thể nhận được địa chỉ đúng của chương trình con phục vụ "
      "ngắt, và trước khi bắt đầu thực thi, nó lưu địa chỉ của tác vụ trước đó "
      "đang thực hiện vào PCB (Khối điều khiển tiến trình) để sau đó quay lại "
      "địa chỉ đó. Đây là cách hoạt động thường gặp của vi xử lý, trong đó một "
      "tiến trình đang chạy được nhận dạng bằng PCB của nó, được tạo ra khi "
      "tiến trình sắp bắt đầu.",
      "To assist the operation of interrupt services, a programmable interrupt "
      "controller is also interfaced with the microprocessor. This controller "
      "resolves priorities of several interrupting devices by software priority "
      "resolving technique (in case of polled interrupt system) or by hardware "
      "priority resolving technique (in case of vectored interrupt system). In "
      "this way the microprocessor is able to obtain the correct address of "
      "interrupt services routine and before starting the execution it saves "
      "and returns the address of the previous task it was performing into its "
      "PCB (Process Control Block). This is an usual method of operation of "
      "microprocessor wherein a running process is recognized by its PCB which "
      "is generated at the time when a process is about to start.")

    # ---------------------------------------------------------- 8.4.2
    H(b, lang, "8.4.2 Giao thức truyền thông",
      "8.4.2 Communication Protocols", level=3)

    P(b, lang,
      "Nhìn chung, hệ thống thiết bị đo dựa trên vi xử lý không dùng kỹ thuật "
      "truyền dữ liệu I/O song song vì lý do chi phí. Hơn nữa, cáp dùng để truyền "
      "dữ liệu trở nên cồng kềnh và gây khó khăn trong thao tác. Vì vậy, kỹ thuật "
      "truyền dữ liệu I/O nối tiếp gần như luôn được dùng trong các ứng dụng "
      "thiết bị đo dựa trên vi xử lý. Trong sơ đồ I/O nối tiếp, dữ liệu được "
      "truyền nối tiếp từng bit một. Vì dữ liệu đầu ra từ thiết bị dựa trên vi "
      "xử lý ở dạng song song, dữ liệu song song được bộ chuyển đổi "
      "song song-sang-nối tiếp đổi sang dạng nối tiếp ở đầu phát, rồi lại được "
      "đổi về dạng song song ở đầu thu.",
      "In general, a microprocessor instrumentation system does not use "
      "parallel I/O data transfer technique because of cost consideration. "
      "Moreover, the cable for transmission of data becomes bulky and presents "
      "handling problems. Therefore, serial I/O data transfer technique is "
      "almost invariably used for microprocessor based instrumentation "
      "applications. In serial I/O scheme, the data is transferred serially "
      "bit-by-bit (one-by-one). Since the data output from microprocessor based "
      "equipment is in parallel form, the parallel data is converted to serial "
      "form by a parallel-to-serial converter at the transmitting end and again "
      "back to parallel form at the receiving end.")

    P(b, lang,
      "Để cách sắp xếp như vậy có hiệu quả, cần mã hóa dữ liệu đúng cách, đồng "
      "bộ bộ thu và bộ phát, lựa chọn tốc độ truyền, lựa chọn giá trị tín hiệu "
      "logic, bố trí tín hiệu bắt tay, v.v. Những yêu cầu này được xác định rõ "
      "bởi các giao thức truyền thông khác nhau được thiết kế cho sơ đồ thiết "
      "bị đo dựa trên vi xử lý. Các giao thức truyền thông cũng xác định cả chi "
      "tiết của liên kết vật lý. Như vậy, chi tiết giao thức kết hợp với liên "
      "kết vật lý được gọi là liên kết truyền thông số. Liên kết vật lý có thể "
      "là một trong nhiều lựa chọn sẵn có, ví dụ cáp xoắn đôi, cáp đồng trục, "
      "modem trên đường dây điện thoại, liên kết vệ tinh, liên kết cáp quang, "
      "v.v.",
      "The requirements for such an arrangement to be effective are proper "
      "coding of data, synchronization of receiver and transmitter, selection "
      "of transmission rate, selection of logical signal values, provision of "
      "hand shaking signal, etc. These requirements are well defined by "
      "different communication protocols designed for microprocessor based "
      "instrumentation scheme. The communication protocols define the details "
      "of physical link as well. In this way, the protocol details combined "
      "with physical link is called digital communication link. Physical link "
      "may be one out of several available options e.g. twisted pair cable, "
      "coaxial cable, modem on telephone link, satellite link, fibre optic "
      "link, etc.")

    P(b, lang,
      "Giao thức có nghĩa là đóng gói dữ liệu cũng như các hướng dẫn mang tính "
      "chỉ đạo mà liên kết truyền thông phải tuân theo để thực hiện đúng chức "
      "năng truyền dữ liệu. Các giao thức truyền thông cũng cho phép tích hợp "
      "nhiều nhà cung cấp trong sơ đồ thiết bị đo dựa trên vi xử lý. Khi chỉ có "
      "hai hệ thống thiết bị đo số được nối với nhau và giao thức không có liên "
      "kết nào khác, đó được gọi là liên kết truyền thông điểm-điểm. Nhưng khi "
      "nhiều hệ thống thiết bị đo số được nối vào một liên kết truyền thông "
      "chung, liên kết đó được gọi là liên kết truyền thông mạng. Giao thức cũng "
      "khác nhau giữa hai kiểu liên kết này: đơn giản hơn đối với liên kết "
      "điểm-điểm và phức tạp hơn đối với liên kết mạng. Việc kết nối các thiết "
      "bị trong mạng tạo nên cấu trúc vật lý và được gọi là cấu trúc mạng.",
      "Protocol means data packaging as well as directed guidelines which the "
      "communication link must follow for effecting the data transmission "
      "functions properly. Communication protocols also allow multi-vendor "
      "integration in microprocessor based instrumentation scheme. When only "
      "two digital instrumentation systems are attached to each other and the "
      "protocol does not have any other link, it is called point-to-point "
      "communication link. But when many digital instrumentation systems are "
      "attached to a common communication link, the link is called network "
      "communication link. The protocols also differ between these two "
      "communication link being simpler for point-to-point link and "
      "sophisticated for network link. The interconnection of devices on a "
      "network constitutes physical structure and is called topology.")

    P(b, lang,
      "Trong liên kết mạng, nhiều cấu trúc mạng đang được sử dụng. Cấu trúc mạng "
      "bus (xem Hình 8.16), cấu trúc mạng vòng (xem Hình 8.17) và cấu trúc mạng "
      "sao (xem Hình 8.18) là những cấu trúc phổ biến hơn cho sơ đồ thiết bị đo "
      "dựa trên vi xử lý.",
      "In network link many topologies are in use. Bus network topology (Refer "
      "Figure 8.16); ring network topology (Refer Figure 8.17) and star network "
      "topology (Refer Figure 8.18) are more popular topologies for "
      "microprocessor based instrumentation scheme.")
    FIG(b, 16, F.fig_f16(), lang)
    FIG(b, 17, F.fig_f17(), lang)
    FIG(b, 18, F.fig_f18(), lang)

    P(b, lang,
      "Trong sắp xếp cấu trúc bus, dữ liệu được mọi thiết bị nhìn thấy nhưng chỉ "
      "được thiết bị cụ thể mà dữ liệu gửi tới xác nhận. Hệ thống này rất hữu "
      "ích cho mạng thiết bị đo đa nhánh. Cấu trúc này hỗ trợ truyền thông ngang "
      "hàng, điều rất cần thiết cho sơ đồ thiết bị đo quá trình trong phòng "
      "điều khiển.",
      "In bus topology arrangement, the data is seen by all devices but is "
      "acknowledged by the particular device for which it is meant. This system "
      "is very useful for multi-drop instrumentation network. This topology "
      "supports peer-to-peer communication which is very much required by the "
      "process instrumentation scheme inside the control room.")

    P(b, lang,
      "Mặt khác, trong sắp xếp cấu trúc vòng, các thiết bị được nối thành một "
      "vòng tròn, nơi dữ liệu phải đi qua từng thiết bị một. Nếu dữ liệu không "
      "dành cho một thiết bị cụ thể nào, thiết bị đó tái tạo tín hiệu và dữ liệu "
      "được chuyển sang thiết bị tiếp theo. Quá trình này tiếp diễn cho đến khi "
      "thiết bị thực sự nhận được dữ liệu. Cấu trúc này cũng hỗ trợ truyền thông "
      "ngang hàng.",
      "In ring topology arrangement, on the other hand, the devices are "
      "connected in a circle where the data have to pass through each and every "
      "device. If the data is not meant for a particular device, the device "
      "regenerates the signal and the data is tranferred to the next device. "
      "This process goes on until the actual device receives the data. This "
      "topology also supports peer-to-peer communication.")

    P(b, lang,
      "Sắp xếp cấu trúc sao là một cấu hình rất cũ, được thiết kế để hỗ trợ kiểu "
      "giao thức mạng thăm dò. Ở đây, thiết bị chủ (còn gọi là thiết bị máy chủ) "
      "nằm ở vị trí trung tâm và mọi thiết bị khác được nối riêng với thiết bị "
      "chủ này. Thiết bị chủ điều khiển mọi truyền thông tới các thiết bị được "
      "nối. Tuy nhiên, nhược điểm của cấu trúc này là không hỗ trợ truyền thông "
      "ngang hàng, điều rất cần thiết cho sơ đồ thiết bị đo.",
      "The star topology arrangement is a very old configuration and was "
      "designed to support polling type of network protocol. Here the master "
      "device (also called server device) is centrally located and all other "
      "devices are connected to this master device separately. The master "
      "device controls all communications to the connected devices. The "
      "disadvantage of this topology however is that it does not support "
      "peer-to-peer communication which is very much required by the "
      "instrumentation scheme.")

    P(b, lang,
      "Việc phát triển các tiêu chuẩn và đặc tả truyền thông do hai tổ chức quốc "
      "tế quản lý. Một là Viện Kỹ sư Điện và Điện tử (IEEE), tổ chức kia là Tổ "
      "chức Tiêu chuẩn Quốc tế (ISO). Ba tiêu chuẩn quan trọng nhất được dùng "
      "trong nhiều sơ đồ thiết bị đo là 802.3 Ethernet CSMA/CD (truy cập đa lần "
      "cảm nhận sóng mang và phát hiện va chạm), 802.4 Token Bus (hệ thống "
      "chuyền token trên sơ đồ cấu trúc bus) và 802.5 Token Ring (hệ thống "
      "chuyền token trên sơ đồ cấu trúc vòng).",
      "The development of communication standards and specifications are "
      "governed by two international organizations. One is Institute of "
      "Electrical and Electronics Engineers (IEEE) and the other one is "
      "International Standards Organizations (ISO). The standards 802.3 "
      "Ethernet CSMA/CD (Carrier Sence Multiple Access/Collision Detection); "
      "802.4 Token Bus (Token passing system on bus topology scheme) and 802.5 "
      "Token Ring (Token passing system on ring topology scheme) are three most "
      "important which are employed in various instrumentation schemes.")

    P(b, lang,
      "ISO đã phát triển mô hình mạng 7 tầng: tầng vật lý, tầng liên kết dữ "
      "liệu, tầng mạng, tầng vận chuyển, tầng phiên, tầng trình bày và tầng ứng "
      "dụng. Mô hình này không ủng hộ bất kỳ giao thức độc quyền nào nhưng cung "
      "cấp kết nối và truyền thông thích hợp giữa mọi mạng nói chung. Mô hình 7 "
      "tầng có tài liệu chức năng chi tiết phù hợp cho từng tầng nhằm tạo điều "
      "kiện thuận lợi cho truyền thông.",
      "The ISO developed a 7-layer network model: physical layer, data link "
      "layer, network layer, transport layer, session layer, presentation layer "
      "and application layer. This model does not support any proprietary "
      "protocol but provides proper connection as well as communication amongst "
      "all networks whatsoever. The 7-layer model possesses proper functional "
      "documentation details for every layer to facilitate ease of "
      "communications.")

    P(b, lang,
      "Với các kiến thức nền trên, giờ đây chúng ta có thể thảo luận các giao "
      "thức truyền thông thực tế khác nhau, những giao thức quan trọng về mặt "
      "thiết bị đo. Dù có rất nhiều giao thức truyền thông được thiết kế, "
      "chúng ta chỉ xét 13 giao thức được dùng trong hệ thống thiết bị đo:",
      "With the above background, we are in a position now to discuss various "
      "practical communication protocols which are important from "
      "instrumentation point of view. Although there are numerous communication "
      "protocols designed, but we shall consider only 13 of them which are used "
      "in instrumentation system:")
    L(b, lang,
      ["(1) EIA RS 232C (Tiêu chuẩn khuyến nghị của Hiệp hội Công nghiệp Điện tử)",
       "(2) RS-422",
       "(3) RS-485",
       "(4) Ethernet",
       "(5) GPIB",
       "(6) CAN",
       "(7) HART",
       "(8) Modbus",
       "(9) ABDH",
       "(10) ARCNET",
       "(11) IEEE 1118",
       "(12) PROFIBUS",
       "(13) FIP"],
      ["(1) EIA RS 232C (Electronic Industries Association Recommended "
       "Standard",
       "(2) RS-422",
       "(3) RS-485",
       "(4) Ethernet",
       "(5) GPIB",
       "(6) CAN",
       "(7) HART",
       "(8) MODBUS",
       "(9) ABDH",
       "(10) ARCNET",
       "(11) IEEE 118",
       "(12) PROFIBUS",
       "(13) FIP"],
      ordered=True)

    P(b, lang,
      "Trong khi chúng ta đã thảo luận các đặc điểm nổi bật của bảy giao thức "
      "đầu tiên trong số các giao thức trên ở các chương trước, chúng ta sẽ "
      "giới hạn thảo luận ở sáu giao thức còn lại từ đây về sau.",
      "While we have already discussed salient features of the first seven of "
      "the above communication protocols in earlier chapters, we shall restrict "
      "our discussion for the remaining six of the protocols hereafter.")

    # ---------------------------------------------------------- 8.4.3
    H(b, lang, "8.4.3 Modbus", "8.4.3 Modbus", level=3)

    P(b, lang,
      "Giao thức mạng Modbus hỗ trợ truyền thông tiêu chuẩn giữa các bộ điều "
      "khiển logic lập trình (PLC) do MODICON chế tạo và các thiết bị khác (tới "
      "247 thiết bị) được nối vào hệ thống. Chúng ta sẽ thảo luận về PLC sau "
      "một chút. Giao thức Modbus truy cập mạng thông qua thăm dò. Nó không hỗ "
      "trợ truyền thông ngang hàng. Phiên bản cải tiến gọi là Modbus Plus, phiên "
      "bản này tất nhiên hỗ trợ truyền thông ngang hàng nhưng không phổ biến "
      "lắm.",
      "Modbus network protocol supports standard communication between MODICON "
      "make Programmable Logic Controllers (PLC) and other devices (upto 247 in "
      "numbers) connected to the system. We shall discuss PLC a little later. "
      "Modbus protocol access the network through polling. It does not support "
      "peer-to-peer communications. The improved version is called Modbus Plus "
      "which of course supports peer-to-peer communication but is not so "
      "popular.")

    P(b, lang,
      "Liên kết truyền thông điểm-điểm (kỹ thuật lưu rồi chuyển tiếp) dùng giao "
      "thức Modbus vì đặc tính thăm dò chủ-tớ đơn giản của nó. Nhưng tiếc là mạng "
      "Modbus chỉ hỗ trợ một thiết bị chủ, như trong Hình 8.19 (mạng Modbus dựa "
      "trên bus). Nếu nhất thiết phải nối nhiều hơn một thiết bị chủ (một yêu "
      "cầu thường gặp trong nhiều sơ đồ thiết bị đo), điều đó chỉ có thể thực "
      "hiện bằng cách tạo một mạng Modbus riêng cho từng thiết bị chủ cần nối. "
      "Tuy nhiên, trong cách sắp xếp này, các thiết bị tớ phải được ghép kênh.",
      "The point-to-point (store and then forward technique) communication link "
      "uses Modbus protocol because of its simple master-slave polling "
      "characteristic. But unfortunately the Modbus network supports only one "
      "master as shown in Figure 8.19 (the bus based Modbus network). If it "
      "becomes absolutely necessary to attach more than one master (an usual "
      "requirement in many instrumentation schemes), it can only be implemented "
      "by creating separate Modbus network for each master to be attached. The "
      "slave devices, however, have to be multiplexed in this arrangement.")
    FIG(b, 19, F.fig_f19(), lang)

    P(b, lang,
      "Một vấn đề đáng lưu ý khác của hệ thống Modbus là thiết bị tớ không thể "
      "đáp ứng nếu chưa được thiết bị chủ thăm dò. Đôi khi điều này gây hạn chế "
      "vì một số điều kiện quan trọng khởi phát báo động có thể không được xử lý "
      "đúng lúc cần xử lý.",
      "Another matter of concern with Modbus system is that the slave is not "
      "capable of responding unless polled by the master. Sometimes this poses "
      "limitations because certain important alarm initiating conditions can go "
      "unattended when it is actually required to be attended.")

    P(b, lang,
      "Vì vậy, một độ trễ thời gian được dự tính trong kiểu báo cáo này, vì "
      "thiết bị tớ phải đợi được đáp ứng cho đến khi nó được thăm dò trong chu "
      "kỳ quét tới. Thiết bị chủ gửi một thông điệp (dưới dạng gói dữ liệu) với "
      "địa chỉ duy nhất dành cho một thiết bị tớ. Thiết bị tớ gửi thông điệp "
      "đáp ứng trở lại cho thiết bị chủ. Đôi khi thiết bị chủ cũng thực hiện "
      "truyền thông toàn cục (nếu cần cho thao tác) tới các thiết bị tớ, mà "
      "thực tế không mong đợi phản hồi nào từ chúng.",
      "Therefore, a time delay is envisaged in such a reporting scheme because "
      "the slave has to wait for the response till it is polled in the coming "
      "scan. The master device sends message (in a data package format) with "
      "unique address for a slave device. The slave device sends back the "
      "response message to the master device. The master device also sometimes "
      "does global messaging (if so required for the operation) for the slave "
      "devices to which no response is expected in fact.")

    P(b, lang,
      "Thông điệp do thiết bị chủ tạo ra và gửi đi gồm mã địa chỉ, mã chức năng, "
      "dữ liệu và mã kiểm tra, như trong Hình 8.20. Mã địa chỉ có phạm vi tới "
      "247 địa chỉ thiết bị tớ. Mã chức năng là các lệnh khác nhau do thiết bị "
      "chủ tạo ra để thực hiện các chức năng khác nhau. Một số mã quan trọng "
      "cùng chức năng của chúng được cho trong Bảng 8.1. Mã kiểm tra do thiết bị "
      "chủ tính toán dựa trên các mã của định dạng thông điệp, sau đó được tính "
      "lại ở thiết bị tớ để so sánh. Nếu khớp nhau, dữ liệu được chấp nhận; nếu "
      "không, dữ liệu bị loại bỏ hoàn toàn và một thông điệp ngoại lệ được gửi "
      "tới thiết bị chủ.",
      "The message generated and sent by the master device consists of address "
      "code, function code, data and check code as shown Figure 8.20. The "
      "address code ranges upto 247 slave addresses. Function code is different "
      "commands generated by the master device for implementing different "
      "functions. A few of the important codes along with their functions have "
      "been shown in the Table 8.1. The check code is calculated by the master "
      "device based in the message format codes and then it is recalculated in "
      "the slave device for comparison. If match is found, data is accepted, if "
      "not, the data is discarded outright and an exception message is passed "
      "on to the master device.")
    FIG(b, 20, F.fig_f20(), lang)

    P(b, lang,
      "Để mã hóa thông điệp, người ta dùng hai định dạng: Modbus ASCII và "
      "Modbus RTU. Modbus ASCII dùng các ký tự ASCII để mã hóa thông điệp, trong "
      "khi Modbus RTU dùng các chữ số nhị phân 8 bit. Mã hóa thông điệp bằng "
      "ASCII thì dễ nhưng chậm và kém hiệu quả, còn mã hóa bằng RTU thì phức "
      "tạp nhưng hiệu quả và nhanh.",
      "For message coding two formats are employed: Modbus ASCII and Modbus "
      "RTU. Modbus ASCII uses ASCII characters for message coding whereas "
      "Modbus RTU uses 8-bit binary digits. Message coding with ASCII is easy "
      "but slow and inefficient whereas coding with RTU is complicated but "
      "efficient and fast.")

    P(b, lang, "Các mã và chức năng tương ứng như sau:",
      "The codes and their functions are as follows:")
    L(b, lang,
      ["01 — Đọc trạng thái cuộn dây,",
       "02 — Đọc trạng thái đầu vào",
       "03 — Đọc thanh ghi lưu giữ,",
       "04 — Đọc thanh ghi đầu vào,",
       "07 — Đọc trạng thái ngoại lệ",
       "09 — Lập trình",
       "10 — Thăm dò hoàn tất lập trình",
       "17 — Báo cáo mã nhận dạng thiết bị tớ,",
       "19 — Đặt lại liên kết truyền thông,",
       "20 — Đọc tham chiếu chung,",
       "21 — Ghi tham chiếu chung,"],
      ["01 — Read coil status,",
       "02 — Read input status",
       "03 — Read holding resister,",
       "04 — Read input register,",
       "07 — Read exception status",
       "09 — Program",
       "10 — Poll program complete",
       "17 — Report Slave I/D,",
       "19 — Reset communication link,",
       "20 — Read general reference,",
       "21 — W rite general reference,"])

    P(b, lang,
      "Một phiên bản cải tiến của giao thức Modbus hiện có là giao thức Modbus "
      "Plus, được phát triển để có tốc độ dữ liệu cao hơn và truyền thông ngang "
      "hàng nhằm hỗ trợ các hệ thống thiết bị đo dựa trên vi xử lý tiên tiến. "
      "Đây là một loại dịch vụ giao thức mạng hai dây độc quyền của MODICON, "
      "dùng hệ thống chuyền token. Tốc độ dữ liệu tới 1 megabit mỗi giây (Mbps). "
      "Đặc điểm quan trọng nhất của giao thức Modbus Plus là tuân thủ các tiêu "
      "chuẩn ISO, do đó mọi kiểu kết nối mạng đều có sẵn thông qua các cổng kết "
      "nối phù hợp. Đặc điểm này làm cho giao thức rất hữu ích cho các hệ thống "
      "thiết bị đo tiên tiến, ví dụ SCADA (Hệ thống giám sát điều khiển và thu "
      "thập dữ liệu) và DCS (Hệ thống điều khiển phân tán), v.v. Mô tả về SCADA "
      "và DCS sẽ được đưa ra ở nơi thích hợp.",
      "An improved version to existing Modbus protocol is Modbus Plus protocol "
      "which has been developed for higher data rate and peer-to-peer "
      "communication to support advanced microprocessor based instrumentation "
      "system. This is a type of proprietary two-wire network protocol service "
      "from MODICON which employs token passing system. The data rate is upto 1 "
      "Megabits per second (Mbps). The most important characteristic of a Modbus "
      "plus protocol is that it conforms to ISO standards and therefore, any "
      "type of network connectivity is available through proper gateways. This "
      "characteristic makes this protocol very useful for advanced "
      "instrumentation system, e.g. SCADA (Supervisory Control and Data "
      "Acquisition System) and DCS (Distributed Control System) etc. A "
      "description of SCADA and DCS shall be given at appropriate place.")

    # ---------------------------------------------------------- 8.4.4
    H(b, lang, "8.4.4 ABDH", "8.4.4 ABDH", level=3)

    P(b, lang,
      "Đây thực chất là giao thức đường truyền dữ liệu Allen Bradley. Ban đầu "
      "đây là giao thức độc quyền được thiết kế để truyền thông qua hệ thống "
      "PLC Allen Bradley, nhưng cũng được các nhà chế tạo thiết bị đo khác hỗ "
      "trợ và chấp nhận rộng rãi. Mọi kiểu kết nối mạng đều có sẵn thông qua các "
      "cổng kết nối phù hợp do Allen Bradley thiết kế và cung cấp. Giao thức này "
      "cũng hỗ trợ truyền thông ngang hàng. Khi đối chiếu với mô hình ISO, nó "
      "chỉ gồm hai tầng: tầng liên kết dữ liệu và tầng ứng dụng. Tầng liên kết "
      "dữ liệu định dạng việc đánh địa chỉ thiết bị, đóng khung ký tự, mã hóa "
      "kiểm lỗi và truyền mạng. Tầng ứng dụng thực hiện truyền thông giữa các "
      "thiết bị mạng, bao gồm đóng gói lệnh thiết bị và tạo phản hồi.",
      "This is actually Allen Bradley Data Highway protocol. This was originally "
      "a proprietary protocol designed for communication through AllenBradley "
      "PLC system, but is supported and well accepted by other instrument "
      "manufacturers as well. All types of network connectivity is available "
      "through suitable gateways designed and supplied by Allen Bradley. This "
      "protocol supports peer-to-peer communication as well. When referred to "
      "ISO model, it consists of only two layers: Data link layer and "
      "Application layer. Data link layer formats for device addressing, "
      "character framing, error check coding and network transmission. "
      "Application layer executes communication between network devices "
      "including packaging of device command and response generation.")

    # ---------------------------------------------------------- 8.4.5
    H(b, lang, "8.4.5 ARCNET", "8.4.5 ARCNET", level=3)

    P(b, lang,
      "Giao thức ARCNET ban đầu được phát triển cho tự động hóa văn phòng "
      "nhưng về sau được sửa đổi để phù hợp cả với yêu cầu của tự động hóa công "
      "nghiệp. ARCNET được thiết kế cho tốc độ dữ liệu từ 156 kbps đến 5 Mbps "
      "với gói dữ liệu tối đa 512 byte. Đây là giao thức chuyền token và có thể "
      "truy cập tới 255 thiết bị được nối. Nó có thể dùng cho cả hệ thống cấu "
      "trúc sao lẫn cấu trúc bus. Trong cấu trúc sao, bộ tập trung đặt ở trung "
      "tâm được nối với các thiết bị từ xa theo kiểu điểm-điểm. Thực chất bộ "
      "tập trung hoạt động như một bộ lặp và giới hạn thao tác của mình chỉ là "
      "chuyển tín hiệu dữ liệu đến tới các thiết bị từ xa.",
      "ARCNET protocol was originally developed for office automation but later "
      "on it was modified to suit the requirement of industrial automation as "
      "well. ARCNET has been designed for data rate between 156 kbps and 5 Mbps "
      "with a data packet of 512 bytes maximum. It is a token passing protocol "
      "and can access upto 255 connected devices. It can be used for star as "
      "well as bus topology system. In star topology, the centrally located hub "
      "is connected to remote devices in point-to-point fashion. The hub "
      "actually functions like a repeater and limits its operation only for "
      "signalling the incoming data towards remote devices.")

    P(b, lang,
      "Theo mô hình ISO, ARCNET có ba tầng nổi bật: tầng vật lý, tầng liên kết "
      "dữ liệu và tầng mạng. Tầng liên kết dữ liệu gồm điều khiển truy cập môi "
      "trường và điều khiển liên kết logic. Điều khiển truy cập môi trường cho "
      "phép truy cập tuần tự vào hệ thống bus dùng chung thông qua sơ đồ chuyền "
      "token. Khi một thiết bị nhận được token, nó bắt đầu truyền thông điệp. "
      "Sau khi hoàn tất, nó trả token lại cho môi trường. Nếu một thiết bị cụ "
      "thể không có thông điệp nào để truyền, nó chuyển token ngay lập tức.",
      "With reference to ISO model, three layers are prominent in ARCNET. The "
      "physical, data link layer and the network layer. The data link layer is "
      "consisting of media access control and logical link control. The media "
      "access control allows sequential access to shared bus system through "
      "token passing scheme. When the device receives a token, it starts "
      "transmitting the message. After completion it releases the token to the "
      "medium. If at all a particular device has no message to be transmitted, "
      "it transfers the token immediately.")

    P(b, lang,
      "Một đặc điểm rất tốt của ARCNET là hệ thống chuyền token được cấu hình "
      "tự động và ngay lập tức khi mạng bắt đầu hoạt động, và tiếp tục được "
      "cấu hình lại một cách động bất cứ khi nào một thiết bị hoặc trạm mới "
      "tham gia hoặc rời khỏi hệ thống mạng. Nếu đôi khi token bị mất, quá trình "
      "cấu hình lại bắt đầu gần như ngay lập tức sau khi tự tạo ra một token "
      "mới.",
      "A very good characteristic of ARCNET is that the token passing system is "
      "configured automatically and immediately when the network comes into "
      "action and goes on reconfiguring dynamically as and when a new device or "
      "station joins or leaves the network system. If sometimes a token is lost "
      "the reconfiguration process starts almost immediately after generating a "
      "new token by itself.")

    P(b, lang,
      "ARCNET đã được sửa đổi là một loại giao thức tổng quát. Trong một sơ đồ "
      "thiết bị đo, các đầu dò, thiết bị hiển thị hoặc bộ điều khiển quá trình "
      "mới gần như luôn có thể được thêm vào hoặc lấy ra khỏi hệ thống. ARCNET "
      "thích ứng gần như ngay lập tức với các lần thêm hoặc bớt này. Thay đổi "
      "duy nhất là mạng cần thời gian để cấu hình lại nhằm tiếp nhận sự thay "
      "đổi. Bộ điều khiển lập trình tại một trạm dùng hệ thống mạng bus token "
      "ARCNET làm giải pháp tạo mạng thiết bị đo công nghiệp.",
      "The modified ARCNET is a generalized type of protocol. In instrumentation "
      "scheme new transducers or display devices or process controllers can be "
      "added or removed from the system almost invariably. ARCNET adapts to new "
      "addition or removal almost immediately. Only changes come is that the "
      "network takes time to reconfigure to take up the change. The single "
      "station programmable controller uses ARCNET token bus network system for "
      "industrial instrumentation networking solution.")

    # ---------------------------------------------------------- 8.4.6
    H(b, lang, "8.4.6 IEEE 1118", "8.4.6 IEEE 1118", level=3)

    P(b, lang,
      "Đây cũng là một giao thức rất quan trọng và phổ biến cho bus nối tiếp, "
      "kết nối các bộ vi điều khiển lập trình, các thiết bị I/O phân tán, thiết "
      "bị ngoại vi RS 232, thiết bị hiển thị, đầu dò, phần tử điều khiển cuối "
      "cùng và các thiết bị điều khiển và thiết bị đo khác. Đây là giao thức "
      "truyền thông nối tiếp đa nhánh, rất phù hợp cho hầu hết mọi công việc "
      "liên quan đến thiết bị đo. Thông điệp gồm 128 byte, được hỗ trợ bởi tốc "
      "độ truyền dữ liệu từ 50 đến 500 kbps.",
      "This is also a very important and popular protocol for serial bus, "
      "interconnected programmable microcontrollers, distributed I/O devices, "
      "RS 232 peripherals, display devices, transducers, final control elements "
      "and other control and instrumentation devices. This is a multidrop serial "
      "communication protocol most suitable for almost all instrumentation "
      "related works. The message consists of 128 bytes supported by a data "
      "transfer rate ranging between 50 and 500 kbps.")

    P(b, lang,
      "Giao thức hỗ trợ hai loại kết nối vật lý khác nhau: cáp xoắn đôi Loại 3 và "
      "cáp xoắn đôi Loại 5. Loại trước gồm hai dây được xoắn nhẹ với nhau, được "
      "dùng khi cần tương thích với các thiết bị đo hiện có. Tốc độ dữ liệu cho "
      "loại này nằm trong khoảng từ 62 Kbps (với chiều dài cáp tối ưu 300 mét) "
      "đến 375 Kbps (với chiều dài cáp tối ưu 1200 mét). Cáp Loại 5 có số lần "
      "xoắn nhiều hơn trên mỗi centimet chiều dài cáp, được dùng khi môi trường "
      "truyền dẫn có nhiều nhiễu và nhiễu xuyên âm làm suy giảm tín hiệu chính. "
      "Loại cáp này hoạt động ở tốc độ dữ liệu từ 76,8 Kbps đến 268,8 Kbps. "
      "Phương pháp mã hóa được dùng là NRZI (mã hóa không trở về không đảo "
      "ngược).",
      "The protocol supports two different types of physical connections: Type "
      "3 twisted pair cable and Type 5 twisted pair cable. The former which "
      "consists of two wires gently twisted together, is employed when "
      "compatibility with existing instruments is required. Data rate for this "
      "range between 62 Kbps (for an optimum cable length of 300 metres) and "
      "375 Kbps (for an optimum cable length of 1200 metres). Type 5 cable, "
      "which has more twists per centimetre length of cable, is employed when "
      "the transmission media is noisy and cross talks degrades the main signal. "
      "This cable operates between 76.8 Kbps and 268.8 Kbps data rate. The "
      "coding method employed is Non-Return-to-Zero Inverted (NRZI).")

    P(b, lang,
      "Tầng liên kết dữ liệu dùng giao thức HDLC (Giao thức điều khiển liên kết "
      "dữ liệu mức cao, một giao thức rất cũ nhưng vẫn được dùng với các sửa "
      "đổi), cung cấp ba lớp dịch vụ truyền dữ liệu: hướng kết nối, không kết "
      "nối và điều khiển thiết bị. Trong dịch vụ hướng kết nối, trước tiên một "
      "kết nối được thiết lập giữa hai thiết bị, rồi mới bắt đầu truyền dữ liệu "
      "(giống như trong truyền thông điện thoại). Trong dịch vụ truyền không "
      "kết nối, xác nhận được gửi sau khi hoàn tất truyền dữ liệu, nếu không thì "
      "sẽ yêu cầu truyền lại (giống như trong hệ thống thư điện tử). Dịch vụ "
      "điều khiển thiết bị cung cấp cơ chế cần thiết để nhận dạng và thử nghiệm "
      "đúng cách các thiết bị được nối vào bus. Ngoài ba dịch vụ trên, hệ thống "
      "còn có thể cung cấp dịch vụ phát tin tới tất cả thiết bị và dịch vụ đánh "
      "địa chỉ nhóm.",
      "The data link layer used HDLC protocol (High level Data Link Control "
      "Protocol, a very old protocol but still in use with modifications) which "
      "provides three classes of data transmission services: "
      "connection-oriented, connectionless and device control services. In "
      "connection-oriented services, first a connection is established between "
      "the two devices and then only data transmission is initiated (just like "
      "in telephonic messaging). In a connectionless transmission services, "
      "acknowledgement follows on completion of data transmission, else a "
      "retransmission is invoked (just like in electronic mailing system). The "
      "device control services provides necessary mechanism for proper "
      "identification as well as testing of the devices connected to the bus. "
      "In addition to above three services, broadcasting to all devices and "
      "group addressing services can also be made available by the system.")

    P(b, lang,
      "Các dịch vụ khác do tầng ứng dụng của giao thức cung cấp, cũng hỗ trợ "
      "triển khai bộ điều khiển lập trình, được phân loại như sau:",
      "Other services provided by the application layer of the protocol which "
      "support programmable controller implementation also, are categorized as "
      "follows:")
    L(b, lang,
      ["Dịch vụ điều khiển thiết bị,",
       "Dịch vụ bộ nhớ,",
       "Dịch vụ I/O,",
       "Dịch vụ truy cập quá trình,",
       "Dịch vụ điều khiển bus,",
       "Dịch vụ giám sát quá trình,",
       "Dịch vụ phát hiện/phục hồi lỗi, v.v."],
      ["Device Control Services,",
       "Memory Services,",
       "I/O Services,",
       "Process Access Services,",
       "Bus control Services,",
       "Process Monitoring Services,",
       "Error Detection/Recovery Services, etc."])

    P(b, lang,
      "Tóm lại, giao thức này đa năng hơn và hiệu quả hơn cho một sơ đồ thiết bị "
      "đo.",
      "In short, this protocol is more versatile and more effective for "
      "instrumentation scheme.")

    # ---------------------------------------------------------- 8.4.7
    H(b, lang, "8.4.7 PROFIBUS", "8.4.7 PROFIBUS", level=3)

    P(b, lang,
      "PROFIBUS (một giao thức fieldbus) được thiết kế theo tiêu chuẩn Đức và "
      "thực tế chỉ phù hợp với ba tầng của ISO, ví dụ tầng vật lý, tầng liên kết "
      "dữ liệu và tầng ứng dụng. Tầng vật lý quy định cáp xoắn đôi dài 1200 mét "
      "với tốc độ truyền dữ liệu từ 9,6 đến 500 Kbps. Số địa chỉ thiết bị tối đa "
      "bị giới hạn ở 127.",
      "The PROFIBUS (a fieldbus protocol) was designed according to German "
      "standards and conforms practically to only three of the ISO layers, e.g. "
      "physical, Data link layer and the application layers. The physical layer "
      "specifies twisted pair cable of 1200 meter length with data transfer rate "
      "between 9.6 and 500 Kbps. The maximum number of devices address is "
      "limited to 127.")

    P(b, lang,
      "Tầng liên kết dữ liệu của PROFIBUS khác với các giao thức khác. Ở đây, "
      "truy cập bus là chủ-tớ kết hợp với chuyền token. Mọi thiết bị chủ động "
      "đều được coi là thiết bị chủ, và một token được thiết lập giữa các thiết "
      "bị chủ động này. Các thiết bị có token truyền thông theo phương pháp chủ-"
      "tớ. Đối với các quá trình thời gian thực của thiết bị đo, việc chuyền "
      "token từ thiết bị chủ này sang thiết bị chủ khác phải hoàn thành trong "
      "thời gian đã phân bổ.",
      "Data link layer of PROFIBUS is different from other protocol. Here bus "
      "accessing is master-slave combined with token passing. All active devices "
      "are considered to be master devices and a token is established amongst "
      "these active devices. The devices with token communicate through "
      "master-slave communication method. For real time processes of "
      "instrumentation, token passing from one master device to another have to "
      "be completed within a time allotted for.")

    P(b, lang,
      "Trong giao thức PROFIBUS có tới bốn chế độ truyền dữ liệu khác nhau:",
      "As many as four different data transfer modes are found in PROFIBUS "
      "protocol:")
    L(b, lang,
      ["SDN (gửi không yêu cầu xác nhận),",
       "SDA (gửi có xác nhận thích hợp),",
       "RDR (yêu cầu có phản hồi thích hợp), và",
       "SRD (gửi và yêu cầu dữ liệu)."],
      ["SDN (Send with no acknowledgement required),",
       "SDA (Send with proper acknowledgement),",
       "RDR (Request with proper reply), and",
       "SRD (Send and request for data)."])

    P(b, lang,
      "Cả bốn chế độ đều quan trọng và cần thiết để thực hiện các tác vụ cụ "
      "thể. Ví dụ, SDN được dùng để phát tin, SDA và RDR dùng cho giao thức "
      "chủ-tớ, còn SRD giúp giảm tải cho bus khi SDA và RDR kết hợp thực hiện "
      "thành công.",
      "All four modes are important and are required for carrying out specific "
      "tasks. For instance, SDN is employed for broadcasting purpose, SDA and "
      "RDR are for master-slave protocol and SRD is to reduce the bus load when "
      "SDA and RDR in combination performs successfully.")

    P(b, lang,
      "Tầng ứng dụng gồm hai tầng con: LLI (Giao diện tầng dưới) và FMS (Đặc tả "
      "thông điệp fieldbus). LLI thực hiện điều khiển luồng, thiết lập/kết thúc "
      "kết nối và chuyển đổi tầng liên kết dữ liệu sang FMS. Các tiến trình ứng "
      "dụng giữa các thiết bị có thể được truy cập thông qua các dịch vụ FMS.",
      "The application layer is composed of two sublayers: LLI (Lower Layer "
      "Interface) and FMS (Fieldbus Message Specification). The LLI performs "
      "flow control, establishes/terminates connections and converts data link "
      "layer to FMS. Application process amongst devices can be accessed through "
      "FMS services.")

    # ---------------------------------------------------------- 8.4.8
    H(b, lang, "8.4.8 FIP (Giao thức thiết bị đo nhà máy)",
      "8.4.8 FIP (Factory Instrumentation Protocol)", level=3)

    P(b, lang,
      "FIP là giao thức fieldbus mở, được thiết kế theo tiêu chuẩn Pháp và thực "
      "tế chỉ phù hợp với ba tầng của ISO, ví dụ tầng vật lý, tầng liên kết dữ "
      "liệu và tầng ứng dụng. Ngoài việc tạo mạng nối tiếp cho các bộ phát lắp "
      "tại hiện trường và các van điều khiển, FIP còn quản lý các cơ sở dữ liệu "
      "phân tán. Tầng vật lý được quy định với chiều dài cáp xoắn đôi hoặc cáp "
      "quang tới 2000 mét và nối được tới 256 thiết bị với tốc độ truyền dữ liệu "
      "từ 31,25 Kbps đến 2,5 Mbps.",
      "FIP being an open fieldbus protocol has been designed according to French "
      "standards and conforms practically to only three of the ISO layers, e.g. "
      "physical, data link and the application layer. In addition to performing "
      "serial networking for field mounted transmitters and control valves, FIP "
      "also manages distributed databases. Physical layer is specified to be "
      "upto 2000 metre of twisted pair or fiber optic cable length and connects "
      "upto 256 devices having data transmission rate between 31.25 Kbps and "
      "2.5 Mbps.")

    P(b, lang,
      "Tầng liên kết dữ liệu quy định một phương pháp đặc biệt để truy cập môi "
      "trường, dựa trên mô hình PDU (Người tạo - Người phân phối - Người dùng). "
      "Mô hình PDU hoạt động theo kỹ thuật phát tin giống như chủ-tớ nhưng "
      "không có kiến trúc địa chỉ cho thiết bị tớ. Theo yêu cầu của các thiết bị "
      "phân phối, các thiết bị tạo phát các biến thông điệp mà không cần biết "
      "người dùng đích là ai. Một người dùng chỉ lấy những biến thông điệp mà "
      "nó được cấu hình để nhận. Một bộ trọng tài bus đảm nhiệm vai trò người "
      "phân phối. Bất kỳ thiết bị FIP nào cũng có thể đảm nhiệm vai trò trọng "
      "tài bus, nhưng tại một thời điểm cụ thể chỉ có một thiết bị hoạt động "
      "như trọng tài bus. Nếu thiết bị trọng tài bus đã chọn bị lỗi trong thao "
      "tác của mình, hệ thống sẽ ngay lập tức chọn một thiết bị khác để hoạt "
      "động như trọng tài bus.",
      "Data link layer specifies a special method for media access which is "
      "based on PDU (Producer Distributor User) model. PDU model functions on "
      "broadcasting techniques like master-slave but have no address "
      "architecture for the slave. On request from distributor devices, "
      "producer devices broadcast the message variables without knowing the "
      "destination user. A user takes up only those message variables for which "
      "it has been configured. A bus arbitrator performs the job of "
      "distributor. Any FIP device can perform the job of bus arbitrator but at "
      "one particular time, only one device can be active as bus arbitrator. If "
      "a particular selected bus arbitrator device fails in its operation, "
      "another device is selected immediately by the system to operate as bus "
      "arbitrator.")

    P(b, lang,
      "Tầng ứng dụng cung cấp hệ thống để đọc/ghi các giá trị biến ở bất kỳ dạng "
      "nào chúng có thể có. Việc lựa chọn chu kỳ quét theo thời gian thực và sự "
      "phối hợp thích hợp giữa các phần tử khác nhau của các cơ sở dữ liệu phân "
      "tán cũng do tầng ứng dụng thực hiện. Ngoài các chức năng trên, tầng ứng "
      "dụng còn thực hiện lấy mẫu đúng cách các bộ phát sẽ được nối vào hệ "
      "thống và các phần tử điều khiển cuối cùng cần được lệnh hoạt động.",
      "The application layer provides system for reading/writing the variable "
      "values in whatever form it be may available. Real time selection of "
      "scanning cycles and proper co-operation amongst the different elements "
      "of the distributed databases are also performed by the application "
      "layer. In addition to the above, the proper sampling of transmitters, to "
      "be connected to the system and the final control elements to be "
      "commanded for operation are also performed by the application layer.")

    return b
