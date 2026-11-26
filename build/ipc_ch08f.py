# -*- coding: utf-8 -*-
"""Section 8.6 (DCS) and the thirty-question end-of-chapter exercise.

Covers decoded lines 15026-15547 (PDF pp. 385-396, printed pp. 373-384).
"""
import ipcfig8 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS

# The supplier for figures 27-34 may still be running.  Install harmless,
# non-overwriting fallbacks only for the three figures this section embeds.
_FIG_FALLBACKS = {
    32: ("Kiến trúc hệ thống điều khiển phân tán (DCS)",
         "DCS architecture overview"),
    33: ("Kết nối phần cứng DCS trên đường truyền dữ liệu nhà máy",
         "DCS hardware interconnection on the plant data highway"),
    34: ("Khe bộ điều khiển cơ bản và các tín hiệu đầu vào, đầu ra",
         "Basic controller slot with its input and output signals"),
}
for _n, (_cvi, _cen) in _FIG_FALLBACKS.items():
    if not hasattr(F, "fig_f%d" % _n):
        def _stub(_n=_n, _cvi=_cvi, _cen=_cen):
            return ("", "Hình 8.%d · %s" % (_n, _cvi),
                    "Figure 8.%d · %s" % (_n, _cen), "", "")
        setattr(F, "fig_f%d" % _n, _stub)


def section(lang):
    b = []

    H(b, lang,
      "8.6 Hệ thống điều khiển phân tán (DCS)",
      "8.6 DCS (Distributed Control System)",
      level=2)

    P(b, lang,
      ("Hệ thống điều khiển phân tán (DCS) thực hiện các chức năng điều khiển theo cách phân tán. "
       "Hệ thống gồm một số mô-đun thiết bị đo dựa trên vi xử lý làm việc cùng nhau một cách đồng "
       "bộ để giám sát và điều khiển hoạt động của một nhà máy công nghệ, như được trình bày tóm "
       "tắt trong Hình 8.32. Như có thể thấy, toàn bộ chức năng điều khiển của một đơn vị công nghệ "
       "được phân bổ cho các mô-đun thiết bị đo khác nhau dựa trên vi xử lý, và các mô-đun này lại "
       "được phân bố về mặt địa lý trên khắp khu vực nhà máy."),
      ("Distributed control system functions in distributed manner. It consists of a number of "
       "microprocessor based instrument modules that work together in synchronized manner to "
       "monitor and control the operation of process plant as shown briefly in Figure 8.32. As is "
       "seen, the entire control functions of a process unit are distributed in the different "
       "microprocessor based instrument modules and these modules are distributed geographically "
       "in the entire plant area."))

    NOTE(b, lang,
         ("Chú giải Hình 8.32 — Tx: bộ phát tín hiệu công nghệ; FCE: phần tử điều khiển cuối. "
          "Các nhãn trên sơ đồ: giao diện I/O cục bộ, xe buýt, máy tính công nghệ, thẻ truyền "
          "thông, trạm cấu hình kỹ thuật, trạm người vận hành, đường truyền dữ liệu chính của nhà "
          "máy, các tệp bộ điều khiển, mô-đun giao diện I/O, đơn vị vận hành công nghệ, máy phân "
          "tích pH và máy phân tích oxy."),
         ("Figure 8.32 legend — Tx: process transmitters; FCE: final control element. Labels on "
          "the diagram: local I/O interface, bus, process computer, communication card, "
          "engineering configuration station, operator station, main plant data highway, "
          "controller files, I/O interface module, process operation unit, pH analyzer and oxygen "
          "analyzer."))

    FIG(b, 32, F.fig_f32(), lang)

    P(b, lang,
      ("DCS về bản chất là một mạng máy tính dùng cho tự động hóa công nghệ và không hoạt động "
       "cô lập như tự động hóa văn phòng. Thực tế, nó thực hiện xử lý theo thời gian thực."),
      ("DCS is essentially a computer network for process automation and does not function in "
       "isolation like office automation. It, in fact, performs real-time processing."))

    P(b, lang,
      ("Một DCS được kết nối với các thiết bị đo, ví dụ bộ phát tín hiệu biến số công nghệ, máy "
       "phân tích công nghệ, cân băng tải và công tắc tiếp điểm, cùng các phần tử điều khiển cuối, "
       "ví dụ van điều khiển, động cơ bước, bộ khởi động và van điện từ, tất cả đều nằm ở phía hiện "
       "trường của nhà máy. Mọi tín hiệu đo công nghệ ở dạng 4 đến 20 mA một chiều; 1 đến 5 V một "
       "chiều; 0,25 đến 1,25 V một chiều và các dạng khác được bộ chuyển đổi tương tự-số (ADC) "
       "chuyển sang dạng số rồi đưa vào máy tính công nghệ. Máy tính công nghệ điều khiển các vòng "
       "điều khiển khác nhau; giám sát đầu vào và đầu ra; thực thi các điều kiện báo động liên quan "
       "đến vận hành nhà máy; thực hiện chức năng logic đặc biệt (nếu có); thực hiện xu hướng, ghi "
       "nhật ký và báo cáo dữ liệu, v.v."),
      ("A DCS is connected to measurement instrument, e.g. process variable transmitters, process "
       "analysers, belt weigher, contact switches and final control elements e.g. control valves, "
       "stepper motors, starters and solenoid valves all located in the field side of a process "
       "plant. All process measurement signals in the form of 4 to 20 mAmps D.C.; 1 to 5 volt "
       "D.C. ; 0.25 to 1.25 volt D.C. and others are converted to digital form by ADC and then fed "
       "to the process computer. The process computer controls different loops; monitors input and "
       "output; executes alarm conditions related to plant operation; executes special logical "
       "function (if any); executes trending, logging and data reporting, etc."))

    P(b, lang,
      ("Các vòng điều khiển tương tự thường liên quan đến việc duy trì biến số công nghệ ở giá trị "
       "cài đặt của nó. Ở một số vòng điều khiển còn cần thực hiện các tác động bù trước, trễ - "
       "dẫn, ghép tầng hoặc tỉ lệ. Các vòng điều khiển rời rạc liên quan đến liên khóa hoặc trình "
       "tự công nghệ như thao tác của PLC. DCS kết hợp tất cả vòng tương tự và vòng rời rạc, thực "
       "hiện trên từng vòng một cách độc lập và thành công. Vì là hệ thống dựa trên máy tính, DCS "
       "có thể tích hợp bất kỳ số lượng I/O, vòng điều khiển và liên khóa logic nào. Nó quét tất cả "
       "bộ phát tín hiệu đo đầu vào được kết nối, phân tích các biến đầu vào và báo động theo các "
       "bất thường phát hiện được; tạo tín hiệu điều khiển đầu ra và hướng chúng tới các phần tử "
       "điều khiển cuối trong toàn nhà máy một cách đồng bộ, tức là theo yêu cầu và tại nơi cần "
       "thiết. Nó liên tục đánh giá lại hiệu năng nhà máy cùng trạng thái thời gian thực và đưa ra "
       "hàng nghìn quyết định gia tăng chỉ trong một phần nhỏ của giây. Các chức năng trên được DCS "
       "thực hiện khá thoải mái vì hệ thống gồm các mô-đun thiết bị độc lập có khả năng thực hiện "
       "đồng thời, trao đổi các tín hiệu điều khiển trung gian từ mô-đun này sang mô-đun khác qua "
       "đường truyền dữ liệu thời gian thực (liên kết truyền thông). Những điều chỉnh điều khiển "
       "gia tăng nhanh và vận hành hiệu quả cho phép điều phối chặt chẽ hơn, tạo ra sự nhất quán "
       "về số lượng lẫn chất lượng sản phẩm, đồng thời duy trì mức tiêu thụ nguyên liệu tối ưu. "
       "Khi điều kiện nhà máy thay đổi, DCS theo dõi các thay đổi và thông qua truyền thông, lưu "
       "trữ và truy xuất dữ liệu phù hợp, điều khiển nhà máy theo các tập điều kiện khác nhau rất "
       "hiệu quả. Hệ thống đưa ra quyết định kịp thời và chính xác mà trí óc con người không làm "
       "được. Hệ thống quản lý báo động chuyên gia do DCS cung cấp buộc người vận hành phải phản "
       "ứng nhanh chóng."),
      ("Analog control loops generally involve maintenance of process variable at its set value. "
       "In some of the control loops feedforward, lead-lag, cascade or ratio actions are also "
       "required to be implemented. Discrete control loops involve process interlocking or "
       "sequencing like PLC operation. The DCS combines all analog loops, discrete loops and "
       "perform upon them independently and successfully. Being a computer based system, a DCS can "
       "incorporate any number of I/O, control loops and logic interlocks. It scans all the "
       "connected measurement input transmitters, analyses the input variables and alarms them "
       "according to the abnormality findings; generate control output and directs them to final "
       "control elements throughout the plant in synchronized manner, i.e. as and wherever required "
       "basis. It continuously re-evaluates the plant performance along with their real-time status "
       "and makes thousands of incremental decisions in only a fraction of a second. The above "
       "functions are performed by DCS quite comfortably because the system consists of independent "
       "instrument modules that are capable of performing their actions simultaneously by carrying "
       "out the various intermediate control signals from one module to other through real-time "
       "data highway (communication links). Fast incremental control adjustments and efficient "
       "operations allow more co-ordinated control resulting in consistency in quantity as well as "
       "quality of products in addition to maintaining optimum consumption of raw materials. In "
       "case of change in plant conditions, a DCS tracks the changes and through proper "
       "communication, data storage and retrieval, it controls the plant on different sets of "
       "conditions quite effectively. It makes timely and accurate decisions whereas human mind "
       "cannot do this. The expert alarm management system offered by DCS forces the operators to "
       "respond promptly."))

    P(b, lang,
      ("Vì DCS là hệ thống thiết bị đo dựa trên máy tính, việc triển khai phần mềm là một đặc điểm "
       "quan trọng. Để nhà máy vận hành đúng cách, DCS được lập trình phù hợp, bao gồm tải lên "
       "thông tin liên quan đến công nghệ và các thuật toán điều khiển. Máy giao diện người vận "
       "hành phải được nạp các lệnh cần thiết để vận hành nhà máy. Toàn bộ phần mềm có thể được "
       "hiểu bằng cách xếp vào ba nhóm: hệ điều hành phân tán (DOS), phần mềm hệ thống cho người "
       "dùng và phần mềm ứng dụng. Toàn bộ công việc vận hành DCS, ví dụ quản lý bộ nhớ, lập lịch "
       "và giám sát các thao tác liên quan đến I/O, do DOS thực hiện. Phần mềm hệ thống hỗ trợ các "
       "chức năng của người dùng, ví dụ dịch ngôn ngữ, biên tập và gỡ lỗi. Cuối cùng, phần mềm ứng "
       "dụng hoạt động tại lớp ranh giới của hệ thống máy tính, thực hiện đọc I/O vào bộ nhớ, tạo "
       "đầu ra điều khiển dựa trên điều kiện đầu vào, giá trị cài đặt và thuật toán đã chọn, đồng "
       "thời tính toán để gán đơn vị kỹ thuật phù hợp cho các biến."),
      ("Since the DCS is a computer based instrumentation system, software implementation is an "
       "important feature. For proper operation of the process plant, the DCS is programmed "
       "properly which constitutes uploading of process related information and control related "
       "algorithms. The operator interface machine must be loaded with required instructions for "
       "operating the plant. The complete software can be understood by putting them in three "
       "groups: Distributed operating system (DOS), system software for user and application "
       "software. Entire works of DCS operation, e.g. memory management functions, scheduling, "
       "supervision of I/O related operations are conducted by DOS. The system software support "
       "user functions, e.g. language translation, editing and debugging. And finally the "
       "application software which functions at boundary layer of the computer system performs "
       "reading operation of I/O into memory, generates control output based upon the condition "
       "of input, the set point and the selected algorithm and also does calculation for assigning "
       "proper engineering units to the variables."))

    P(b, lang,
      ("Xét về phần cứng, nói chung DCS có các phần cứng sau:"),
      ("As far as hardware is concerned, the DCS, in general, have following hardwares:"))

    L(b, lang,
      ["(i) Hệ thống truyền thông (CS)",
       "(ii) Các tệp bộ điều khiển (CF)",
       "(iii) Đơn vị giao tiếp biến số công nghệ (PVIU)",
       "(iv) Cổng đường truyền dữ liệu (DHP)",
       "(v) Thiết bị truy cập ưu tiên (PAD)"],
      ["(i) Communication System (CS)",
       "(ii) Controller Files (CF)",
       "(iii) Process Variables Interface Unit (PVIU)",
       "(iv) Data Highway Port (DHP)",
       "(v) Preferential Access Device (PAD)"],
      ordered=False)

    P(b, lang,
      ("Các phần cứng được liên kết với nhau theo cách thể hiện trong Hình 8.33, hoặc theo bất kỳ "
       "cách nào khác do thiết kế công nghệ cụ thể yêu cầu để triển khai các hệ thống điều khiển "
       "tiên tiến cho công nghệ."),
      ("The hardware are interconnected together in the manner shown in Figure 8.33 or any other "
       "manner required by the particular process design for implementing advanced control "
       "systems for the process."))

    H(b, lang, "(i) Hệ thống truyền thông (CS)", "(i) Communication System (CS)", level=3)

    P(b, lang,
      ("Hệ thống truyền thông chính gồm Đường truyền dữ liệu nhà máy (PDH), Mô-đun điều khiển "
       "lưu lượng đường truyền (HTCM), Liên kết thiết bị truy cập ưu tiên (PAD-Link), Liên kết "
       "vật lý (PL) và Liên kết bộ điều khiển logic lập trình (PLC-Link)."),
      ("The main communication system consists of Plant Data Highway (PDH); Highway Traffic "
       "Controller Module (HTCM); Preferential Access Device Link (PAD-Link), Physical Link (PL) "
       "and Programmable Logic Controller Link (PLC-Link)."))

    P(b, lang,
      ("Đường truyền dữ liệu nhà máy là kênh truyền thông chủ yếu cho phép trao đổi dữ liệu giữa "
       "tất cả thiết bị đo được phân bố trên toàn khu vực nhà máy và được nối có hệ thống với "
       "kênh này. Liên kết vật lý tạo kết nối vật lý tới mọi thiết bị về cơ bản là cáp đồng trục, "
       "gồm một số nhánh được thiết kế, chiều dài xấp xỉ của mỗi nhánh tới 5000 mét, hơn hẳn mức "
       "cần thiết cho bất kỳ nhà máy nào. Thông thường, không nên cho tổng cộng quá 25 thiết bị "
       "kết nối vào mỗi nhánh. PDH có hệ thống truyền thông dự phòng kép, tức là có hai cáp đồng "
       "trục độc lập (một chính và một dự phòng) cùng giao diện đường truyền dữ liệu riêng. Một "
       "Mô-đun điều khiển lưu lượng đường truyền (HTCM) điều khiển toàn bộ lưu lượng dữ liệu và gồm "
       "các mô-đun điện tử độc lập (PCB) cho cả cáp đồng trục chính lẫn cáp dự phòng. HTCM cũng "
       "gồm cả dây dẫn cho các Thiết bị truy cập ưu tiên."),
      ("Plant data highway is the principal communication channel which allows data communication "
       "amongst all the instrument devices distributed along the entire plant area which are "
       "systematically connected to it. The physical link which makes physical connection to all "
       "the devices is essentially coaxial cable consisting of designed number of branches, "
       "approximate length of each branch being upto 5000 metres which is more than sufficient for "
       "any plant. Normally upto 25 devices altogether should be allowed to be connected to each "
       "of the branches. PDHs have dual redundant communication system, i.e. they have two "
       "independent coaxial cables (one primary and other backup) and separate data highway "
       "interface. A Highway Traffic Controller Module (HTCM) controls the complete traffic of the "
       "data and includes independent electronics modules (PCB) for primary as well as backup "
       "coaxial cables. The HTCM includes wiring for preferential Access Devices as well."))

    P(b, lang,
      ("Giao diện đường truyền dữ liệu thực chất là một mô-đun thẻ điện tử (PCB) được cắm vào từng "
       "thiết bị. PCB có mạch điện cần thiết cho truyền thông, với chức năng đóng gói dữ liệu như "
       "gán địa chỉ, nhận diện địa chỉ, chuyển đổi dữ liệu, phát hiện lỗi, v.v. Các mô-đun còn có "
       "đầu nối cáp đồng trục cùng khớp nối chữ T để tạo điều kiện nối song song các mô-đun khác. "
       "HTCM là một PCB khác (lắp trên mặt sau) có một tập thẻ điện tử cho mỗi cáp đồng trục. Cổng "
       "kết nối được bố trí trong HTCM cho từng cáp đồng trục và cho cả các thiết bị truy cập ưu "
       "tiên. HTCM giám sát và điều phối luồng dữ liệu giữa các thiết bị nối vào đường truyền dữ "
       "liệu nhà máy."),
      ("Data highway interfaces are in fact electronic card module (PCB) to be inserted in each "
       "device. The PCB has electronic circuit required for communication having data packaging "
       "function, e.g. address assignment, address recognition, data conversion, error detection, "
       "etc. The modules shall have coaxial cable connector also with a Tee Connector joint to "
       "facilitate parallel connection of other modules. HTCM is another PCB (installed in back "
       "plane) having a set of electronic cards for each coaxial cable. The connection inlets are "
       "provided in HTCM for each coaxial cable as well as for preferential access devices. The "
       "HTCM monitors and co-ordinates data trafficking amongst devices connected to the plant "
       "data highway."))

    NOTE(b, lang,
         ("Chú giải Hình 8.33 — HTCM: Mô-đun điều khiển lưu lượng đường truyền; ECS: Trạm cấu hình "
          "kỹ thuật; OS: Trạm người vận hành; PVIU: Đơn vị giao tiếp biến số công nghệ; BC: Bộ "
          "điều khiển cơ bản; HLC: Bộ điều khiển cao cấp; PC: Máy tính công nghệ; DHP: Cổng đường "
          "truyền dữ liệu; MC: Bộ điều khiển đa chức năng; Trạm người vận hành cục bộ; PLC: "
          "Bộ điều khiển logic lập trình; PLCD: Đường truyền dữ liệu PLC; PAL: Liên kết truy cập "
          "ưu tiên."),
         ("Figure 8.33 legend — HTCM: Highway Traffic Controller Module; ECS: Engineering "
          "Configuration Station; OS: Operator Station; PVIU: Process Variables Interface Unit; "
          "BC: Basic Controller; HLC: High-level Controller; PC: Process Computer; DHP: Data "
          "Highway Port; MC: Multifunction Controller; Local Operator Station / Local Controller "
          "Station; PLC: "
          "Programmable Logic Controller; PLCD: PLC Data Highway; PAL: Preferential Access Link."))

    FIG(b, 33, F.fig_f33(), lang)

    P(b, lang,
      ("Các thiết bị khác nhau nối vào PDH được phân loại thành thiết bị truy cập ưu tiên (PAD), "
       "thiết bị được thăm dò (PD) và thiết bị chỉ trả lời (ROD). Các PAD là máy tính công nghệ, "
       "trạm người vận hành (OS) và trạm cấu hình kỹ thuật (ECS). Chúng nối với HTCM qua liên kết "
       "truy cập ưu tiên (PAL) và có quyền ưu tiên truyền thông cao hơn mọi thiết bị khác trong hệ "
       "thống. Số lượng thiết bị loại này cần nối được quyết định bởi yêu cầu thiết kế của từng "
       "hệ thống thực tế. Các thiết bị được thăm dò là đơn vị giao tiếp biến số công nghệ (PVIU) "
       "và cổng đường truyền dữ liệu (DHP). PVIU nối với các bộ chuyển đổi và bộ phát tín hiệu đo "
       "lắp gần công nghệ, còn DHP nối với mạng PLC. Các đơn vị hoặc mạng này chỉ có thể khởi tạo "
       "truyền dữ liệu khi được HTCM thăm dò. Các thiết bị chỉ trả lời gồm tất cả bộ điều khiển, "
       "ví dụ bộ điều khiển cơ bản (BC), bộ điều khiển đa chức năng (MC) và các thiết bị tương tự. "
       "Chúng không tự khởi tạo truyền dữ liệu mà chỉ trả lời tác động do thiết bị truy cập ưu tiên "
       "khởi xướng."),
      ("The various devices connected to PDH are classified as preferential access device (PAD), "
       "polled device (PD) and respond only device (ROD). The PADs are process computer, operator "
       "station (OS) and engineering configuration station (ECS). These are connected to HTCM "
       "through preferential access link (PAL) and enjoy higher priority for communication than "
       "any other devices connected to the system. The number of such devices to be connected to "
       "the system are decided by the design requirement for a particular practical system. The "
       "polled devices are process variable interface units (PVIU) and data highway port (DHP). "
       "PVIUs are connected to different measurement transducers/transmitters installed near the "
       "process whereas DHP is connected to PLC network. These units/network can initiate data "
       "transfer only when polled by the HTCM. The respond only devices consist of all the "
       "controllers, e.g. basic controllers (BC), multifunction controllers (MC) and similar other "
       "devices. They themselves cannot initiate data transfer rather they have only to respond "
       "to the action initiated by the preferential access devices."))

    P(b, lang,
      ("Truyền dữ liệu qua cáp đồng trục ở dạng nối tiếp với tốc độ nói chung là 250 kbps, hơn hẳn "
       "mức cần thiết cho các nhà máy công nghệ. Độ dài từ lệnh và từ dữ liệu được chọn theo yêu "
       "cầu thiết kế (thực tế do nhà cung cấp phối hợp với người dùng lựa chọn). Mỗi từ gồm mã để "
       "nhận dạng chức năng của thiết bị liên quan và vị trí bộ nhớ, các bit đồng bộ ở đầu và mã "
       "kiểm lỗi BCH ở cuối thông điệp. Mỗi từ được kiểm tra tính toàn vẹn dữ liệu. Mã kiểm lỗi BCH "
       "do thiết bị gửi và cả thiết bị nhận cùng tính toán; bất kỳ sai lệch nào trong dữ liệu nhận "
       "được sẽ bị loại bỏ và báo cáo tới trạm người vận hành. Trạm người vận hành chạy một chương "
       "trình chẩn đoán để lưu hồ sơ lỗi và, nếu cấu hình yêu cầu, đưa lệnh tới HTCM để chuyển kênh "
       "truyền thông từ đường truyền dữ liệu chính sang đường truyền dự phòng. Những đặc điểm quan "
       "trọng của hệ thống truyền thông DCS là cơ chế kiểm lỗi, bố trí hệ thống dự phòng (đôi khi "
       "cả dự phòng kép) và cách ly thiết bị bằng ghép biến áp tại giao diện đường truyền dữ liệu, "
       "để hỏng hóc của một thiết bị không ảnh hưởng tới các thiết bị khác."),
      ("Data transfer through coaxial cable is in serial form at the rate of 250 kbps in general "
       "and is more than sufficient for process plants. Command and data word length is selected "
       "as per design requirement (it is actually selected by the vendor in co-ordination with the "
       "user). Each word shall include codes to identify the function of the device involved and "
       "the memory location, synchronizing bits at start and BCH (Bose Chaudhuri Hocquenghem) error "
       "checking code at the end of the message. Each word is checked for data integrity. The BCH "
       "error check code is computed by the sending device and by the receiving device as well and "
       "any discrepancy in the data received shall be reported to the operator station after "
       "rejection. The operator station runs a diagnostic routine for keeping the record of errors "
       "and if configuration demands, a command is issued by the operator station to the HTCM "
       "which changes over the communication channel from primary to back-up data highway. "
       "Important features of the DCS communication system are error checking arrangement, "
       "provision of back-up (and also sometimes redundant) system and the devices isolation by "
       "transformer coupling at the data highway interface so that failure of any device shall "
       "have no effect on other devices."))

    H(b, lang, "(ii) Các tệp bộ điều khiển (CF)", "(ii) Controller Files (CF)", level=3)

    P(b, lang,
      ("Các tệp bộ điều khiển là bộ điều khiển công nghệ gồm ba loại: (a) bộ điều khiển cơ bản "
       "(BC), (b) bộ điều khiển cao cấp (HLC) và (c) bộ điều khiển đa chức năng (MC). Phần cứng "
       "chính của các bộ điều khiển này gồm các thẻ điều khiển dạng mô-đun cùng các bảng đấu dây "
       "chuyên dụng lắp bên trong tủ. Mỗi bộ điều khiển thường có vi xử lý 16 bit, ROM, RAM, giao "
       "diện đường truyền dữ liệu và mạch ổn áp. Vi xử lý thực thi lệnh từ ROM và xử lý dữ liệu có "
       "trong RAM. ROM chứa các thuật toán điều khiển định sẵn cùng các chức năng điều khiển và "
       "giám sát khác. Các bộ điều khiển thực hiện hoàn toàn tự chủ nhờ phần cứng, phần mềm cơ sở "
       "và cơ sở dữ liệu riêng. Chúng hoàn toàn không phụ thuộc vào các thiết bị khác trong hệ "
       "thống chính. Tác động điều khiển và giám sát của bộ điều khiển do người dùng cấu hình. "
       "Người dùng trước tiên chọn một thuật toán điều khiển cụ thể rồi nhập các hằng số và thông "
       "số cần thiết cho điều khiển công nghệ đã định. Có một số lượng khe điều khiển quy định "
       "(có thể là tám hoặc bội của tám); bộ điều khiển cao cấp và bộ điều khiển đa chức năng "
       "thường có số khe gấp đôi bộ điều khiển cơ bản. Mỗi khe riêng lẻ được thiết kế để thực hiện "
       "bất kỳ tác động nào theo cấu hình, ví dụ PID hoặc bất kỳ chế độ điều khiển nào, thuật toán "
       "phụ trợ (điều hòa tín hiệu, phép toán toán học, phép toán logic, bù trễ - dẫn và các tác "
       "động khác). Ngoài ra, các khe có thể được cấu hình để tạo thành vòng ghép tầng."),
      ("The controller files are process controllers which are of three different varieties: (a) "
       "Basic controller (BC), (b) High-level Controller (HLC), and (c) Multifunction controller "
       "(MC). Primary hardware of these controllers are composed of modular controller cards along "
       "with dedicated termination panels installed inside the cabinet. Each controller has "
       "normally 16-bit microprocessor, ROM, RAM, data highway interface and power regulator "
       "circuits. The microprocessor executes instructions from the ROM and operates upon the data "
       "available on the RAM. The ROM contains predefined control algorithms and other controls as "
       "well as monitoring functions. The controllers implement complete autonomous operations "
       "because of their own hardware, firmware and database system. These are completely "
       "independent of other devices present in the main system. Controller actions for control as "
       "well as monitoring functions are user configurable. The user first selects a particular "
       "control algorithm and then enters the constants and the parameters required for the "
       "specified process control. There is a specified number of control slots (may be eight or "
       "multiple of eight) and the high level as well as the multifunction controllers shall have "
       "normally twice the number available in the basic controller. An individual slot is designed "
       "to perform any action as configured, e.g. PID or any control mode, any auxiliary algorithm "
       "(signal conditions, mathematical operations, logical operations, lead/lag compensation and "
       "others). In addition to independent operations, the slots can be configured to form "
       "cascade loops as well."))

    P(b, lang,
      ("Bộ điều khiển có khả năng thực hiện thuật toán quy định và tính toán đầu ra cần thiết cho "
       "mỗi khe ít nhất ba lần trong một giây. Ngoài ra, nó còn tự chẩn đoán. Mỗi khe điều khiển có "
       "hai đầu vào và một đầu ra điều khiển cùng hai đầu ra báo động (một cao và một thấp), như "
       "trong Hình 8.34. Đầu vào PV là biến số công nghệ, còn đầu vào SP là giá trị cài đặt."),
      ("The controller is capable of performing specified algorithm and calculating required "
       "output for each slot, at least three times in a second. In addition to above, it also "
       "performs diagnostics for itself. Each control slot has two input and one control output "
       "along with two alarm outputs (one high and one low) as shown in Figure 8.34. Input PV is "
       "the process variable whereas input SP is the set point adjustment."))

    NOTE(b, lang,
         ("Chú giải Hình 8.34 — Đầu vào PV, đầu vào SP, đầu ra báo động cao, đầu ra điều khiển "
          "(CO), đầu ra báo động thấp và BC."),
         ("Figure 8.34 labels — Input PV, Input SP, High alarm output, Control output (CO), Low "
          "alarm output and BC."))

    FIG(b, 34, F.fig_f34(), lang)

    P(b, lang,
      ("Các chế độ hoạt động của khe gồm Thủ công, Tự động, Ghép tầng và Máy tính. Ở chế độ thủ "
       "công, đầu vào SP không ảnh hưởng đến đầu ra điều khiển; đầu ra do trạm người vận hành tạo "
       "ra. Ở chế độ tự động, đầu vào SP do điểm cài đặt cục bộ của chính khe đó tạo ra. Ở chế độ "
       "ghép tầng, đầu vào SP được đưa từ khe điều khiển khác, nơi nó được xử lý bằng toán học. Ở "
       "chế độ máy tính, đầu vào SP và đầu ra điều khiển do máy tính công nghệ tạo ra. Các hệ "
       "thống điều khiển này thường được gọi là Điều khiển giám sát hoặc điều khiển theo giá trị "
       "cài đặt (SPC) và Điều khiển số trực tiếp (DDC). Chúng cũng có thể triển khai độc lập. SPC "
       "thực hiện qua các bộ điều khiển lập trình một trạm, nhưng giá trị cài đặt do máy tính công "
       "nghệ tạo ra và đưa qua bộ chuyển đổi số-tương tự (DAC) cùng bộ giải ghép kênh (DEMUX). Ở "
       "chiều ngược lại, trong DDC các tệp bộ điều khiển nằm bên trong máy tính công nghệ, nơi tất "
       "cả giá trị cài đặt và đầu ra điều khiển được tạo ra. Đầu ra điều khiển được đưa đi theo "
       "cách tương tự như SPC."),
      ("Operational modes of the slots have provisions of Manual, Automatic, Cascade or Computer "
       "mode. In manual mode the input SP does not affect the control output. It is generated by "
       "the operator station. In automatic mode, the input SP is generated by the local set point "
       "of the particular slot. In cascade mode of operation, the input SP is fed from other "
       "control slot where it is manipulated mathematically. In computer mode of operation the "
       "input SP and the control output are generated by a process computer. Such systems of "
       "control are better known as Supervisory or Set Point Control (SPC) and Direct Digital "
       "Control (DDC). These controls can also be implemented independently. SPC is performed "
       "through single station programmable controllers but the set points are generated by the "
       "process computer and fed through DAC (Digital-to-Analog Converter) and DEMUX (De-"
       "Multiplexer). On the other hand in the DDC, the controller files are located inside the "
       "process computer where all the set points and the control outputs are generated. The "
       "control outputs are fed in similar way as SPC."))

    P(b, lang,
      ("Các chế độ điều khiển nêu trên có thể chuyển đổi êm từ chế độ này sang chế độ khác nhờ theo "
       "dõi PV (theo dõi biến số công nghệ). Đầu vào SP được lệnh theo dõi PV khi bộ điều khiển ở "
       "chế độ thủ công. Khi bộ điều khiển được chuyển sang chế độ tự động, giá trị cài đặt bằng "
       "PV vì phép theo dõi PV đã cân bằng hai giá trị này bên trong. Để ghép tầng hai khe, cần chế "
       "độ Khởi động thủ công. Điều này thực hiện bằng cách cho khe chính tạo ra đầu ra mà khe phụ "
       "trong vận hành ghép tầng dùng làm đầu vào SP. Nếu khe phụ được cấu hình để khởi động, bộ "
       "điều khiển sẽ thực hiện tính ngược khi khe phụ được đưa từ ghép tầng sang tự động hoặc thủ "
       "công. Trong quá trình chạy PID, đầu ra của khe chính được xử lý để dùng cho khe phụ. Việc "
       "cân bằng đầu ra này được thực hiện bên trong và giúp chuyển đổi êm giữa các chế độ."),
      ("The different control modes described above can be switched from one to another bumplessly "
       "by the help of PV-tracking (process variable tracking). The input-SP is instructed to track "
       "the PV while the controller is in manual mode. When the controller is switched to "
       "automatic mode, the set point equals the PV because the PV-tracking equalises the two "
       "internally. For the cascade operation of two slots, Initialization Manual is required. This "
       "is done by allowing a primary slot to generate an output which the secondary slot in "
       "cascade operation uses as its SP input. If the secondary slot is configured for "
       "initialization, a back calculation is performed by the controller when the secondary slot "
       "is brought from cascade to automatic or to manual operation mode. During PID operation, "
       "the output of primary slot is manipulated for use in secondary slot. These balancing of "
       "output which is performed internally helps in bumpless transfer between the modes."))

    P(b, lang,
      ("Bộ điều khiển cao cấp có năng lực chức năng gấp đôi bộ điều khiển cơ bản. Mọi thuật toán "
       "điều khiển tinh vi đều có thể triển khai qua các kỹ thuật cấu hình I/O khác nhau. Tín hiệu "
       "đầu ra trạng thái là điểm đặc biệt của bộ điều khiển này, cho phép cấu hình nhiều hệ "
       "thống điều khiển liên khóa khác nhau."),
      ("The high level controllers have double the functional capability than the basic one. Any "
       "sophisticated control algorithm can be implemented through different I/O configuration "
       "techniques. Status output signals which is the speciality of this controller can configure "
       "various interlocking control systems."))

    P(b, lang,
      ("Bộ điều khiển đa chức năng có năng lực vận hành đa chức năng và chứa rất nhiều khối logic. "
       "Ngoài chức năng điều khiển điều hòa thông thường, nó còn có các chức năng khác như giám "
       "sát và điều khiển trình tự. Cả ba chức năng điều khiển này vừa làm việc độc lập vừa hoạt "
       "động tích hợp. Các bộ điều khiển này cũng có thể truyền thông với nhóm bộ điều khiển tương "
       "tự khác nếu tất cả được nối với nhau qua liên kết truyền thông cục bộ (LCLink). Một trạm "
       "người vận hành riêng cũng nối vào LCLink để thực hiện nhiều thao tác vận hành; trạm này "
       "gọi là Trạm người vận hành cục bộ (LOS), như trên sơ đồ. Việc vận hành các khe điều khiển "
       "của những bộ điều khiển này cũng có thể được giám sát bằng tác động điều khiển trình tự "
       "trên một máy chủ riêng khác. Thực tế, chính việc lập trình giúp bộ điều khiển thực hiện "
       "trình tự vận hành công nghệ thông qua phần mềm độc quyền riêng của nhà cung cấp. Để phát "
       "triển phần mềm độc quyền này, các kỹ sư thiết kế công nghệ cùng với sơ đồ công nghệ và "
       "thiết bị đo (PI Diagram) phải phối hợp với kỹ sư thiết kế thiết bị đo của nhà cung cấp."),
      ("The multifunction controllers have multifunction operational capability and contain a large "
       "number of logic blocks. In addition to normal modulating control functions, it has other "
       "functions as well, e.g. monitoring control and sequencing control function. All these "
       "three control functions work independently and in integrated manner as well. These "
       "controllers can also communicate with other group of similar controllers if they all are "
       "interconnected through a local communication link (LCLink). A separate operator station is "
       "also connected to the LCLink for effecting multi-operation facet. This operator station is "
       "called Local Operator Station (LOS) as shown on the diagram. Operation of the control "
       "slots of these controllers can be supervised by the sequencing control actions on any "
       "other separate host computer as well. Actually, it is the programming which makes the "
       "controller to perform sequencing of process operation through vendor specific proprietary "
       "software. For development of such proprietary software, however, the process design "
       "engineers along with process and instrumentation diagram (PI Diagram) have to co-ordinate "
       "with vendors instrument design engineers."))

    P(b, lang,
      ("LCLink là cáp nhiều lõi dài tới khoảng 30 mét, cho phép truyền thông giữa các bộ điều "
       "khiển đa chức năng. LCLink cũng cho phép nhân viên vận hành giám sát và điều khiển hoạt "
       "động của MC từ LOS khi cần. Liên kết này còn cho phép các MC giao tiếp với hoạt động của "
       "nhau. Vì vậy chức năng của MC rất phức tạp, và đó là lý do cần phần mềm chuyên biệt mang "
       "tính độc quyền phù hợp với từng hệ thống vận hành công nghệ."),
      ("The LCLink which is a multicore cable of upto 30 metre or so in length enables "
       "communication amongst the multifunction controllers. The LC-Link also gives access to the "
       "operating personnel to monitor and control the operation of MC as and when required from "
       "LOS. This link also gives access to MCs to interfarce with each others operation. Thus, "
       "the functions of MC is very complex and that is why a specific software of proprietary "
       "nature is required to suit a particular process operation system."))

    P(b, lang,
      ("Trong DCS còn có một loạt tệp bộ điều khiển dự phòng (RCF), được kích hoạt khi các tệp bộ "
       "điều khiển công nghệ đang chạy gặp sự cố. Tuy nhiên, sự cố của bộ điều khiển đang chạy do "
       "chính RCF phát hiện và báo cáo tới giao diện người vận hành, sau đó mới diễn ra chuyển "
       "đổi. Việc chuyển đổi được thực hiện cùng với toàn bộ chức năng I/O, tức là mọi đầu vào và "
       "đầu ra điều khiển đều được chuyển sang RCF, đồng thời toàn bộ thông tin liên quan đến "
       "điều khiển lưu trong bộ nhớ dự phòng được tải ngay sang RCF. Điểm hay của hệ thống là các "
       "thao tác này không cần đến đường truyền dữ liệu vì chúng diễn ra ở cấp vòng điều khiển."),
      ("In DCS there are series of reserve controller files (RCF) as well which come into action in "
       "the event of malfunctioning of inline process controller files. However, the malfunctioning "
       "of inline controller is detected and reported by the RCF itself to the operator interface "
       "and thereafter the changeover takes place. The changeover is effected along with all I/O "
       "functionings, e.g. all control input and output are transferred to RCF and also all control "
       "related information stored in the back-up memory are immediately uploaded to RCF. The "
       "beauty of the system is that these operations do not require help of data highway since "
       "these changes take place at control loop level."))

    P(b, lang,
      ("Hoạt động của RCF dựa trên các chương trình chẩn đoán, kết quả được giám sát bởi thư mục "
       "bộ điều khiển dự phòng (RCD). RCF cũng tự chạy chẩn đoán cho mạch của chính nó. Nếu kết "
       "quả chẩn đoán báo lỗi bộ điều khiển đang chạy (trong khi RCF và RCD vẫn bình thường), trình "
       "tự chuyển đổi tự động sẽ bắt đầu một cách có hệ thống. Tương tự, bộ điều khiển cao cấp "
       "(HLC) và bộ điều khiển đa chức năng (MC) cũng có RCD riêng, và hoạt động của chúng về cơ "
       "bản giống như mô tả cho bộ điều khiển cơ bản."),
      ("The operation of RCF is based on diagnostic routines, the result of which is monitored by "
       "reserve controller directory (RCD). It performs diagnostic run on its own circuit as well. "
       "If the result of diagnostic run reports failure of inline controller (RCF and RCD being "
       "normal), then automatic changeover sequencing starts systematically. In the same way, the "
       "high-level controller (HLC) and the multifunction controller (MC) have also their "
       "respective RCD and the operation of these are more or less similar as described for basic "
       "controller."))

    H(b, lang, "(iii) Đơn vị giao tiếp biến số công nghệ (PVIU)",
      "(iii) Process Variables Interface Unit (PVIU)", level=3)

    P(b, lang,
      ("PVIU nối tất cả tín hiệu đầu vào của biến số công nghệ vào hệ thống. PVIU có một vi xử "
       "lý, một đơn vị bộ nhớ (gồm ROM và RAM) và thẻ giao tiếp biến số công nghệ. ROM chứa chương "
       "trình vận hành cần thiết cho hệ thống, RAM chứa dữ liệu cấu hình (do người vận hành thiết "
       "lập) cho mọi thiết bị đầu vào, ví dụ số thẻ, chi tiết bộ phát tín hiệu, chi tiết điều hòa "
       "tín hiệu, dải hiệu chuẩn và cả địa chỉ của PVIU. Chương trình vận hành của hệ thống quét "
       "tất cả thiết bị đầu vào theo trình tự và lưu vào RAM, sau đó dữ liệu được gửi tới thiết bị "
       "truy cập ưu tiên (PAD) theo yêu cầu thông qua truy cập bộ nhớ trực tiếp (DMA). Nếu HTCM "
       "phát lệnh thăm dò truyền dữ liệu, PVIU gửi dữ liệu mới nhất đã cập nhật tới PAD. Trong "
       "suốt các trình tự thao tác này, vi xử lý liên tục chạy các chương trình chẩn đoán và mọi "
       "sự cố phát sinh bên trong hệ thống được báo ngay cho PAD qua đường truyền dữ liệu."),
      ("PVIU connects all process variable input signals to the system, PVIU possess a "
       "microprocessor, a memory unit (consisting of ROM and RAM) and process variable interface "
       "card. The ROM contains required operation program for the system, RAM contains configuration "
       "data (configured by the operator) for all the input devices, e.g. tag number, transmitter "
       "details, signal conditioning details, calibration range and also the address of PVIU. The "
       "system operation program scans all the input devices in sequence and stores in RAM and "
       "thereafter data is sent to preferential access device (PAD) on demand through DMA transfer "
       "(Direct Memory Access). If HTCM issues poll for data transfer, the PVIU sends latest "
       "updated data to the PAD. During all these operation sequences, the diagnostic routines are "
       "run by the microprocessor continuously and any problem occurring inside the system is "
       "immediately reported to PAD through data highway."))

    P(b, lang,
      ("Các PVIU thường được chia thành ba nhóm để thuận tiện cho chức năng điều hòa tín hiệu: PVIU "
       "cấp cao, PVIU cấp thấp và PVIU năng lượng thấp. Cả ba loại này bao phủ gần như mọi chủng "
       "loại tín hiệu I/O công nghệ trên khắp khu vực nhà máy."),
      ("The PVIUs normally are divided in three groups for ease of signal conditioning function, "
       "e.g. High Level PVIU, Low Level PVIU and Low Energy PVIU. All these three units cover "
       "almost all varieties of process I/O signals spread all over the process plant area."))

    H(b, lang, "(iv) Cổng đường truyền dữ liệu (DHP)", "(iv) Data Highway Port (DHP)", level=3)

    P(b, lang,
      ("Như đã mô tả ở trên, DHP tạo điều kiện liên kết các PLC vào DCS. Mô-đun DHP chứa vi xử "
       "lý, bộ nhớ (ROM và RAM) và hệ thống giao diện đường truyền dữ liệu. DHP đóng vai trò mô-đun "
       "truyền thông để giám sát và điều khiển PLC. DHP quét theo trình tự tất cả PLC nối với nó và "
       "lưu hồ sơ trong đơn vị bộ nhớ. Dữ liệu ghi trong bộ nhớ của DHP được gửi theo yêu cầu tới "
       "PAD. Nhìn chung, việc giám sát và điều khiển hệ thống mà các PLC được nối vào do chính các "
       "PLC thực hiện hoàn toàn, còn DCS đảm nhiệm vai trò giám sát đối với hoạt động của PLC thông "
       "qua cơ sở dữ liệu của DHP."),
      ("As described earlier, the DHP facilitates interconnection of PLCs into the DCS. The DHP "
       "module contains microprocessor, memory (ROM and RAM) and data highway interface system. The "
       "DHP functions as communication module for monitoring and control of PLC. The DHP scans in "
       "sequence all the PLC connected to it and maintains record in its memory unit. The data "
       "recorded in memory unit of DHP is sent on demand to PAD. In general, monitoring and control "
       "of the system to which the PLCs are connected are done entirely by the PLCs themselves, but "
       "the supervisory roll is performed by the DCS for PLC operation through DHP database."))

    P(b, lang,
      ("Để trao đổi dữ liệu liên quan đến PLC, các cổng của DHP được nối với đường truyền dữ liệu "
       "cục bộ của PLC thông qua modem RS 232. Hai loại PLC nổi tiếng là MODICON và ALLEN BRADLEY "
       "gần như luôn dùng modem vì chiều dài cáp liên kết dạng cặp xoắn vượt quá 15 mét."),
      ("For inter transfer of PLC related data, the ports of DHP are connected to PLC local data "
       "highway through RS 232 modem. The two renowned PLC type e.g. MODICON and ALLEN BRADLEY use "
       "modem almost invariably because the length of interconnected cable being twisted pair type "
       "happens to be more than 15 metres."))

    H(b, lang, "(v) Thiết bị truy cập ưu tiên (PAD)", "(v) Preferential Access Device (PAD)", level=3)

    P(b, lang,
      ("PAD là tác nhân điều khiển chính cho toàn bộ hoạt động của DCS. PAD gồm trạm người vận hành "
       "(OS), Trạm cấu hình kỹ thuật (ECS) và Máy tính công nghệ (PC). Chức năng chính của DCS là "
       "giám sát và điều khiển các thông số của nhà máy công nghệ theo cách phối hợp. OS chứa màn "
       "hình, bàn phím, ổ đĩa CD, hộp thẻ và bo mạch UPS. Màn hình trình bày hiển thị đồ họa về "
       "toàn bộ hệ thống vận hành của đơn vị công nghệ theo ba cách: Tổng quan, Nhóm và Hiển thị "
       "số. Thực tế, toàn bộ DCS được chia thành nhiều nhóm, mỗi nhóm bao phủ gần như mọi vòng "
       "điều khiển riêng lẻ với hiển thị đồ họa đầy đủ về biến số công nghệ (PV) và giá trị cài đặt "
       "(SP) dưới dạng biểu đồ thanh cùng chữ số thập phân. Màn hình tổng quan cho thấy toàn bộ "
       "hệ thống được chia thành các nhóm và chỉ ra xu hướng thay đổi của PV, SP và các giá trị "
       "khác. Màn hình nhóm thể hiện một nhóm hoàn chỉnh được chọn riêng để theo dõi bằng hình ảnh "
       "và báo cáo bằng lời. Màn hình chi tiết thể hiện từng hệ thống hoặc vòng điều khiển riêng, "
       "cho thấy gần như mọi chi tiết liên quan đến hệ thống hoặc vòng điều khiển đó. Mọi biến của "
       "màn hình chi tiết đều có thể truy cập từ OS và ECS qua bàn phím, do đó mọi sửa đổi cần "
       "thiết đều có thể khởi xướng từ OS hoặc ECS. Các màn hình đặc biệt khác theo yêu cầu của "
       "người dùng cũng có thể được triển khai ngay ở giai đoạn thiết kế."),
      ("The PAD constitutes the main controlling agent for entire DCS operation. These comprise "
       "operator station (OS), Engineering Configuration Station (ECS) and Process Computer (PC). "
       "The main function of DCS is to monitor and control the process plant parameters in a co-"
       "ordinated manner. The OS contains monitor, keyboard, CD drive, card file and UPS board. The "
       "monitor presents graphic display of process unit operation system in its entirety in three "
       "different manners: Overview, Group and Digital display. In fact, the entire DCS is divided "
       "into several groups where each group covers almost all individual control loops with "
       "complete graphic display of process variables (PV) and set points (SP) in the form of bar "
       "graphs as well as decimal digits. The overview display shows entire system divided in "
       "groups and indicates trend in change of PV, SP and others. The group display shows one "
       "complete group specifically selected for visual monitoring and verbal reporting. The "
       "detail display shows individual system or control loop indicating almost all details "
       "pertaining to that system-control/loop. All variables of detail display are accessible from "
       "the OS as well as ECS through keyboard input and therefore, all modifications if required "
       "can be initiated from OS or ECS. Other special displays as per requirement of the user can "
       "also be implemented at the design stage itself."))

    P(b, lang,
      ("Ngoài những nội dung trên, DCS còn có các màn hình sau:"),
      ("In addition to the above, the following displays are also incorporated in the DCS:"))

    L(b, lang,
      ["(a) Xu hướng thời gian thực của gần như mọi biến số công nghệ, giá trị cài đặt và đầu ra "
       "điều khiển dưới dạng điểm, màn hình chi tiết và xu hướng lịch sử.",
       "(b) Ghi nhận báo động dưới dạng số thẻ, thời điểm phát sinh, loại, số nhóm, báo động gần "
       "nhất và báo động ngắt đầu tiên (nếu có). Báo động ngắt đầu tiên cho thấy nguyên nhân chính "
       "gây ngắt toàn nhà máy.",
       "(c) Chẩn đoán hệ thống và báo cáo về hệ thống là thao tác rất quan trọng xét đến độ phức "
       "tạp của phần cứng trong thiết kế hệ thống.",
       "(d) Các phép tính trung bình, hiệu suất và các phép tính do người dùng định nghĩa khác cũng "
       "được hiển thị sau khi tính toán.",
       "(e) Dữ liệu tới hạn do người dùng định nghĩa, liên quan đến một thao tác công nghệ cụ thể, "
       "cũng được ghi lại theo các khoảng thời gian quy định. Các màn hình do người dùng cấu hình "
       "này dựa trên tương tác của người vận hành và vì vậy có thể được diễn giải lại theo thời "
       "gian khi tình huống yêu cầu.",
       "(f) Một số công nghệ có tính không liên tục, ví dụ thao tác thổi bồ hóng trong nồi hơi để "
       "loại bỏ lớp bồ hóng hình thành trên bề mặt ngoài của ống nước, hoặc thao tác xả nước ngưng "
       "trong hệ thống hơi tiện ích. Một tập màn hình đặc biệt liên quan đến các thao tác này cũng "
       "được đưa vào thiết kế DCS."],
      ["(a) Real time trending of almost all process variables, set points and control output in "
       "the form of dot, detailed display and historical trending.",
       "(b) Alarm recording in the form of tag number, time of occurrence, type, group number, "
       "last alarm, first trip alarm if any. First trip alarm indicates the main reason behind "
       "initiation of trip of the plant.",
       "(c) System diagnostic and reporting thereof is a very important operation considering the "
       "hardware complications involved in the system design.",
       "(d) Averaging, efficiency and other user-defined calculations are also displayed after "
       "calculation.",
       "(e) User defined critical data, related to specific unit operation are also recorded on "
       "specified time intervals. These user-configured displays are operator interaction based "
       "and therefore, can be reinterpreted from time-to-time as situation demands.",
       "(f) Some of the processes are discontinuous in nature, e.g. soot blowing operation in "
       "boilers for removal of soot formation on the outer surface of water tubes; condensate blow "
       "down operation in utility steam system, etc. A set of special displays related to these "
       "operations is also included in the DCS design."],
      ordered=False)

    P(b, lang,
      ("ECS dùng để nhập dữ liệu cấu hình. Chương trình cấu hình được tải lên OS. Mọi dữ liệu "
       "chuẩn để vận hành các đơn vị công nghệ được cấu hình qua bàn phím của ECS."),
      ("ECS is meant for carrying out the entry of configuration data. Configuration program is "
       "uploaded into the OS. All standard data for operation of the process units are configured "
       "through the keyboard of ECS."))

    P(b, lang,
      ("Trong vận hành bình thường của các đơn vị công nghệ, giá trị cài đặt đã cấu hình và giá trị "
       "đầu ra điều khiển được tạo ra có thể được người vận hành điều chỉnh lại. Xu hướng thời gian "
       "thực, in bản cứng dữ liệu theo các khoảng thời gian quy định đều được khởi xướng từ trạm "
       "người vận hành."),
      ("In normal operation of the process units, the configured value of set point and generated "
       "value of control output can be readjusted by the operator. Real time trending, hard copy "
       "printing of data on specified intervals are all initated from the operator station."))

    P(b, lang,
      ("Các hoạt động theo trình tự trong thời gian công nghệ bị xáo trộn (đã được hình dung ngay "
       "trong giai đoạn thiết kế hệ thống và các thao tác tuần tự phù hợp đã được đưa vào hệ thống "
       "thông qua phần mềm thích hợp) được cấu hình trong trạm người vận hành. Nhưng những xáo trộn "
       "không lường trước được từ trước và vì thế không được cấu hình chỉ có thể đánh giá dựa trên "
       "chi tiết tóm tắt báo động. Trong những tình huống đó, người vận hành phải tự khởi xướng mọi "
       "hành động cần thiết ngay tại thời điểm đó."),
      ("Procedural activities during process upsets (which have been envisaged during system design "
       "itself and suitable sequential operations have been incorporated into the system through "
       "suitable software) are configured into the operator station. But the upsets that could "
       "have not been envisaged earlier and hence not configured can be evaluated only on the "
       "basis of alarm summary details. In such situations, the operators have to initiate all the "
       "necessary actions at that particular moment."))

    P(b, lang,
      ("Việc giám sát hệ thống được trạm người vận hành quan sát, ví dụ trạng thái của các thiết bị "
       "nối vào đường truyền dữ liệu. Từng thiết bị nối vào đường truyền dữ liệu liên tục tự chẩn "
       "đoán và mọi bất thường được báo cho trạm người vận hành trong lúc trạm này quét các thiết "
       "bị. Tính năng hiển thị trạng thái đường truyền của DCS cho thấy mọi chi tiết về các bất "
       "thường khi người vận hành gọi lên."),
      ("System monitoring is observed by the operator station, e.g. status of devices connected to "
       "the data highway. The individual device connected to the data highway continuously performs "
       "self-diagnostics and any abnormality is reported to the operator station during scanning "
       "operation initiated by the operator station for the devices. The highway status display "
       "feature of the DCS indicate all details pertaining to the abnormalities when called up by "
       "the operator."))

    P(b, lang,
      ("Máy tính công nghệ có khả năng thực hiện mọi thao tác mà trạm người vận hành thực hiện trực "
       "tuyến. Điều này có nghĩa máy tính công nghệ có thể được coi là dự phòng nóng. Ngoài ra, máy "
       "tính công nghệ còn được nối với hệ thống thông tin quản lý (MIS). Điều này cho phép ban quản "
       "lý thấy mọi hoạt động đang diễn ra trong nhà máy và cũng cho phép một số chỉ thị được chuyển "
       "tới người vận hành để thực hiện."),
      ("The process computer is capable of performing all operations that operator station is "
       "performing inline. This means the process computer can be treated as hot standby. In "
       "addition, the process computer is also connected to management information system (MIS). "
       "This allows management to see all activities being performed inside the plant. This also "
       "allows some instructions to pass on to the operator for implementation."))

    P(b, lang,
      ("Nhìn chung, DCS có khả năng thực hiện mọi điều khiển công nghệ tiên tiến, can thiệp quản lý "
       "trực tiếp và tối ưu hóa công nghệ. Nhờ mức độ hiệu quả cao đối với hệ thống điều khiển công "
       "nghệ cùng khả năng thích ứng với các yêu cầu công nghệ thay đổi, DCS sẽ tiếp tục giữ vai "
       "trò quan trọng trong các hệ thống thiết bị đo hiện đại. Năng lực đó của DCS có được nhờ "
       "triển khai Trí tuệ nhân tạo (AI) và các Hệ chuyên gia. Hệ thống cũng hỗ trợ người vận hành "
       "khi có sự cố hoặc xáo trộn công nghệ và giúp họ giảm căng thẳng."),
      ("In general, DCS is capable of all advanced process control and direct management "
       "intervention as well as process optimization. Because of its high degree of effectiveness "
       "for the process control system and its ability to adopt to changing process requirements, "
       "it would continue to enjoy its importance in modern instrumentation system. Such system "
       "capability, the DCS has derived by implementing Artificial Intelligence and Expert Systems. "
       "It also assist the human operators during eventualities/process upsets and relieves them "
       "from tension."))

    H(b, lang, "Bài tập", "Exercise", level=2)

    L(b, lang,
      ["Hệ thống thiết bị đo dựa trên vi xử lý là gì? Tại sao lại dùng vi xử lý trong hệ thống thiết "
       "bị đo?",
       "Hãy giải thích kèm sơ đồ cách thực hiện giao tiếp của các bộ chuyển đổi? Để cải thiện chất "
       "lượng tín hiệu của cặp nhiệt điện, người ta dùng kết nối đặc biệt nào? Hãy giải thích kèm "
       "sơ đồ.",
       "Bộ thích ứng giao tiếp song song (PIA) là gì? Hãy giải thích hoạt động của nó liên quan đến "
       "máy tính chủ và các hệ thống I/O.",
       "Hãy giải thích cách triển khai giao tiếp của phần tử điều khiển cuối? Bộ chuyển đổi điện-"
       "khí nén là gì? Làm thế nào để chuyển tín hiệu 4 đến 20 mA một chiều sang tín hiệu điện áp?",
       "Những phần cứng khác nhau được tích hợp trong một bộ vi điều khiển là gì? Hãy giải thích "
       "ngắn gọn hoạt động của bộ vi điều khiển.",
       "Bộ cấu hình cầm tay là gì? Hãy giải thích bằng sơ đồ hoạt động của hệ thống cấu hình dựa "
       "trên PC.",
       "Hãy giải thích tại sao giao tiếp DAC với vi điều khiển lại được ánh xạ bộ nhớ, trong khi hệ "
       "thống thiết bị đo thông thường dùng kỹ thuật giao tiếp ánh xạ I/O?",
       "Chức năng của UART là gì? Làm thế nào để một bộ vi điều khiển trở nên lập trình được?",
       "Hãy giải thích hoạt động của xe buýt hệ thống của vi xử lý liên quan đến hệ thống thiết bị "
       "đo. Hạn chế chính của xe buýt đồng bộ là gì? Giải pháp cho vấn đề đó là gì?",
       "Hãy giải thích tại sao ngắt là cần thiết trong bất kỳ hệ thống thiết bị đo dựa trên vi xử "
       "lý nào? Hãy giải thích cách giải quyết xung đột giữa nhiều thiết bị gây ngắt. Bộ điều "
       "khiển ngắt là gì?",
       "Chức năng của giao thức truyền thông là gì? Hãy liệt kê mười giao thức như vậy được dùng "
       "trong tự động hóa công nghệ.",
       "Sự khác biệt giữa liên kết điểm-điểm và liên kết mạng là gì? Các loại liên kết vật lý khác "
       "nhau là gì?",
       "Hãy mô tả bằng sơ đồ rõ ràng các cấu trúc mạng khác nhau được dùng trong mạng thiết bị đo. "
       "Giao tiếp ngang hàng là gì?",
       "Hãy giải thích giao thức MODBUS dùng cho hệ thống truyền thông PLC. Định dạng của thông "
       "điệp do thiết bị chủ tạo ra là gì?",
       "Sự khác biệt giữa các giao thức ABDH và MODBUS Plus là gì? Đặc điểm quan trọng nhất của "
       "MODBUS Plus khiến nó khác với các giao thức khác là gì?",
       "Hãy viết ghi chú về các nội dung sau: (a) FIP (b) PROFIBUS (c) IEEE 1118 (d) ARCNET (e) "
       "Cách ly và che lọc (f) Giao tiếp của hệ thống hiển thị.",
       "Hãy phân biệt cáp xoắn đôi loại 3 và loại 5. Giao thức truyền thông nối tiếp đa nhánh là "
       "gì? Giao thức nào là đa dụng nhất, hỗ trợ cả triển khai PLC bên cạnh các kết nối thiết bị "
       "đo khác?",
       "Hãy mô tả việc triển khai hệ thống liên khóa bằng rơ-le cơ điện thông thường và các cổng "
       "logic. Những hạn chế của chúng là gì?",
       "Các thành phần khác nhau của một sơ đồ PLC là gì? Hãy giải thích chi tiết chức năng của "
       "đơn vị vi xử lý.",
       "Chu kỳ hoạt động của PLC là gì? Những thao tác nào được hoàn thành trong một chu kỳ đầy "
       "đủ? Chức năng của WDT là gì?",
       "Các loại bộ nhớ khác nhau có trong hệ thống PLC là gì? Căn cứ lựa chọn bộ nhớ trong PLC là "
       "gì? Có sự khác biệt nào giữa bộ nhớ của PLC và bộ nhớ của máy vi tính không?",
       "Các lệnh khác nhau được sử dụng trong hệ thống PLC là gì? Hãy giải thích ngắn gọn ba trong "
       "số đó.",
       "Tính liên tục logic trong hệ thống lập trình logic bậc thang là gì? Sự khác biệt giữa lệnh "
       "LI và lệnh ONS của PLC là gì?",
       "Hệ thống điều khiển phân tán là gì? Nó khác với điều khiển giám sát và Điều khiển số trực "
       "tiếp như thế nào? Hãy giải thích kèm sơ đồ.",
       "Đường truyền dữ liệu nhà máy là gì? Các chức năng của nó trong DCS là gì? Chức năng của "
       "HTCM là gì? Hãy giải thích kèm sơ đồ.",
       "Sự khác biệt giữa PADlink và PLClink là gì? Giao diện đường truyền dữ liệu là gì và các "
       "chức năng của nó là gì?",
       "PAD là gì và chức năng của chúng là gì? Trạm người vận hành dự phòng nóng hoạt động như "
       "thế nào?",
       "Những khác biệt chính giữa bộ điều khiển cao cấp và bộ điều khiển đa chức năng là gì? Hãy "
       "giải thích chức năng của khe bộ điều khiển cơ bản bằng sơ đồ.",
       "RCF là gì? Tại sao cần có RCF như vậy trong DCS? Có vẻ không kinh tế phải không? Hãy giải "
       "thích bằng lập luận kỹ thuật.",
       "DHP là gì và nó hoạt động như thế nào? PVIU là gì và các chức năng của nó là gì? Hãy giải "
       "thích chi tiết."],
      ["What is microprocessor based instrumentation system? Why at all the microprocessor is "
       "employed in instrumentation system ?",
       "Explain with diagram how interfacing of transducers are carried out? For improving signal "
       "quality of a thermocouple, what special connection is employed? Explain with diagram.",
       "What is Parallel Interface Adaptors? Explain its functioning in relation to a host computer "
       "and I/O systems.",
       "Explain how interfacing of final control element is implemented? What is an "
       "electropneumatic converter? How a 4 to 20 mAmps D.C. signal can be converted to voltage "
       "signal?",
       "What are the different hardwares incorporated in a microcontroller? Explain the functioning "
       "of a microcontroller in brief.",
       "What is hand-held configurator? Explain with the help of a diagram the operation of a "
       "PCbased configuration system.",
       "Explain why DAC interfacing with microcontroller is memory mapped when normal "
       "instrumentation system employ I/O mapped interfacing technique?",
       "What is the function of an UART? How a microcontroller is made programmable?",
       "Explain the working of system bus of a microprocessor in relation to instrumentation "
       "system. What is the main limitation of synchronous bus? What is its solution?",
       "Explain why interrupt is essential in any microprocessor based instrumentation system? "
       "Explain how the conflict amongst several interrupting devices is resolved. What is an "
       "interrupt controller?",
       "What is the function of a communication protocol? Write ten numbers of such protocols used "
       "in process automation.",
       "What is the difference between point-to-point and network link? What are the different "
       "physical links?",
       "Describe with the help of a clear diagram the different topologies used in instrumentation "
       "networking. What is peer-to-peer communication?",
       "Explain MODBUS protocol for PLC communication system. What is the format of the message "
       "generated by the master device?",
       "What is the difference between ABDH and MODBUS Plus protocols? What is the most important "
       "characteristic of MODBUS Plus which makes it different from other protocols?",
       "Write notes on following : (a) FIP (b) PROFIBUS (c) IEEE 1118 (d) ARCNET (e) Isolation and "
       "masking (f) Interfacing of display system.",
       "Differentiate between a type 3 and type 5 twisted pair cable. What is a multidrop serial "
       "communication protocol? Which protocol is the most versatile protocol that supports PLC "
       "implementation also in addition to other instrumentation connections.",
       "Describe the implementation of interlocking system with the help of conventional "
       "electromechanical relay and logic gates. What are their limitations?",
       "What are different components of a PLC scheme? Explain the function of microprocessor unit "
       "in detail.",
       "What is operation cycle of PLC? What are the operations that are completed in one complete "
       "cycle? What are the functions of a WDT?",
       "What are the different types of memory available in a PLC system? What is the basis of "
       "memory selection in a PLC? Is there any difference between the memory unit of a PLC and the "
       "memory unit of a microcomputer?",
       "What are the different instructions followed in a PLC system? Explain three of them in "
       "brief.",
       "What is logical continuity in a ladder logic programming system? What is the difference "
       "between LI and ONS instruction of a PLC?",
       "What is distributed control system? How is it different from supervisory control and Direct "
       "Digital Control? Explain with diagrams.",
       "What is Plant Data Highway? What are its functions in a DCS? What are the functions of "
       "HTCM? Explain with diagram.",
       "What is the difference between PADlink and PLClink? What is data highway interface and what "
       "are its functions?",
       "What are PADs and what are their functions? How does a hot standby operator station "
       "function?",
       "What are the main differences between high-level controller and multifunction controller? "
       "Explain the function of basic controller slot with the help of a diagram.",
       "What is RCF? Why it is essential to have such RCF in DCS? Does not it look uneconomical? "
       "Explain with engineering justification.",
       "What is DHP and how it functions? What is PVIU and what are its functions? Explain in "
       "detail."],
      ordered=True)

    return b
