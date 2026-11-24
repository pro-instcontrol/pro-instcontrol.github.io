# -*- coding: utf-8 -*-
"""Book 7, Chapter 10, Section C - Valve Positioners (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), the final prose
sections "Accessories and Software", "Connecting It All to the Control System"
and the repeated "Accessories", plus References and Additional Reading,
printed pp. 76-79 (source lines 2424-2496 of work/cvp_raw.txt). Figure 10-4 is
redrawn in cvpfig10.py. The integration module supplies the title, byline,
glossary and page shell.
"""
from cvp_common import fig, h2, h3, note, p, refs, ul
import cvpfig10 as F


def body_vi():
    b = []
    b.append(h2("Phụ kiện và phần mềm", "Accessories and Software"))
    b.append(p("Các phụ kiện thường gặp của bộ định vị số gồm công tắc vi mô (microswitch) tích hợp. Các công tắc này thường hoạt động ở điện áp thấp (24 V). Chúng có thể thực hiện việc đóng van an toàn, được khởi phát độc lập với bộ điều khiển. Ngoài ra còn có các thiết bị chỉ thị vị trí hành trình dạng số hoặc tương tự. Những bộ định vị này cần phần mềm để thực hiện các chức năng chẩn đoán hoặc hiệu chỉnh từ xa. Dưới đây là một số khả năng mà gói phần mềm như vậy nên hỗ trợ [3]:"))
    b.append(ul([
        "Đọc dữ liệu chẩn đoán của van",
        "Hỗ trợ cửa sổ xu hướng chẩn đoán dạng đồ họa",
        "Cấu hình van và cơ sở dữ liệu cấu hình van",
        "Giám sát khả năng của thiết bị",
        "Cấu hình đặc tính van",
        "Các quy trình chung và cơ sở dữ liệu van",
        "Cấp quyền người dùng (security levels)",
        "Cơ sở dữ liệu chẩn đoán",
    ]))

    b.append(h2("Kết nối mọi thứ vào hệ điều khiển",
                "Connecting It All to the Control System"))
    b.append(p("Để phối hợp hoạt động đúng cách, hệ điều khiển của nhà máy cần một «kiến trúc» trong đó các bộ phát, bộ định vị, bộ điều khiển, bộ báo động (annunciator), máy tính và các phần mềm liên quan được tích hợp vào một cấu trúc sao cho các thiết bị này có thể truyền thông hiệu quả với nhau và vận hành với hiệu suất cao."))
    b.append(p("Một kiến trúc dựa trên trường (field-based architecture) hiệu quả có thể xây dựng các giải pháp quản lý quá trình bằng cách kết nối các thiết bị trường thông minh, các nền tảng điều khiển có khả năng mở rộng và phần mềm. Bên cạnh các thiết bị trường thông minh (ví dụ bộ định vị thông minh), điều này đòi hỏi phần mềm hiệu năng dạng mô-đun. Nếu làm đúng cách, phần mềm như vậy có thể định nghĩa lại công tác quản lý, mở rộng điều khiển quá trình và giải quyết các vấn đề quản lý tài sản. Phần mềm nên:"))
    b.append(ul([
        "giảm chi phí lắp đặt;",
        "cải thiện hiệu năng;",
        "tương thích với các thiết bị hiện có;",
        "giảm các độ lệch quá trình;",
        "có khả năng mở rộng;",
        "giảm chi phí bảo trì;",
        "cải thiện độ tin cậy của nhà máy;",
        "giảm thời gian đào tạo; và",
        "thích ứng với các quá trình thay đổi.",
    ]))
    b.append(p("Như Hình 10-4 cho thấy, kiến trúc như vậy sẽ chuyển hệ thống điển hình trước đây dựa trên tín hiệu tương tự 4 đến 20 mA, «lấy hệ điều khiển phân tán (DCS) làm trung tâm», thành một kiến trúc dựa trên trường mới. Điều này thực chất đưa người vận hành ra khỏi phòng điều khiển xuống chính hiện trường của nhà máy."))
    b.append(fig(4, F.fig_f104()))
    b.append(p("Các thiết bị trường thông minh như bộ định vị van thông minh có chức năng điều khiển (PID) có thể thực hiện tại chỗ tất cả các tác vụ sau: điều khiển vòng lặp, xử lý tín hiệu, thu thập dữ liệu, phân tích, phát hiện báo động, thu thập xu hướng và ghi chép bảo trì."))

    b.append(h2("Phụ kiện", "Accessories"))
    b.append(p("Theo Bud Keyes [4], việc chuyển chức năng từ phòng điều khiển tập trung xuống các thiết bị trường cũng giống như ngành máy tính chuyển từ máy tính lớn (mainframe) sang các mạng máy tính cá nhân (PC)."))
    b.append(p("Mục tiêu tổng thể là tạo ra một hệ điều khiển quản lý thời gian thực, tích hợp mọi khía cạnh của quản lý nhà máy, kiểm soát sản xuất, điều khiển quá trình, hiệu suất nhà máy và bảo trì."))
    b.append(p("Chương trình bảo trì van điều khiển có thể bao gồm, ví dụ, chẩn đoán trực tuyến, hiệu chỉnh từ xa, các kế hoạch bảo trì phòng ngừa và kiểm soát tồn kho phụ tùng thay thế."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "S. G. Lloyd, “Guidelines for the Application of Valve Positioners,” Proceedings of the Texas A&amp;M Instrumentation Symposium, January (1969).",
        "D. W. St. Clair, Controller Tuning and Control Loop Performance, 2nd ed. (Newark, DE: Straight-Line Control Company, 1993).",
        "Béla G. Lipták, Process Control and Optimization, 4th ed., Vol. 2 (New York: Taylor &amp; Francis, 2006): 1197.",
        "M. A. Keyes, “Field-based Distributed Control Opens Door to Performance Improvements,” I&amp;CS (January 1997): 25–35.",
    ]))

    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "Hans-Josef Schneider, “Digitale Feldgerate: Vorteile, Probleme und Anforderungen aus Anwendersicht,” atp-Automatisierungstechnische Praxis 37, no. 4 (April 1995): 50–54.",
    ]))

    b.append(note("<b>Ghi chú về nguồn.</b> (1) Lớp văn bản OCR có nhiều dấu gạch nối khi xuống dòng («typ-ically», «perfor-mance», «mainte-nance», «diag-nosis») và một số hư hỏng rõ ràng khác; bản dịch ghép từ lại thành từ hoàn chỉnh. Ở mục này, nguồn in «build-in microswitches» mà ý là «built-in», và một số tên tài liệu tham khảo bị tách dòng («Performance Improvements», «Anforde-rungen» trong mục Đọc thêm); tất cả đều được khôi phục. (Chữ «Coand ă» bị lỗi trong văn bản chương thuộc mục trước, nơi ghi là «Coandă».) (2) Nguồn lặp lại tiêu đề «Accessories»; cả hai lần xuất hiện đều được giữ lại. (3) Cả bốn hình (10-1 đến 10-4) là bản vẽ lại dạng vector đã đơn giản hóa, không phải bản sao facsimile; chi tiết phương trình/khí lý tưởng của Hình 10-2 được trình bày ở dạng đơn giản. (4) Nguồn ghi công SAMSON AG, Flowserve Inc. và Emerson Process Control trên các hình tương ứng. (5) «21/4 in» trong Bảng 10-1 được trình bày là «2 1/4 in». (6) Các trang in 67–79 tương ứng với các trang PDF 72–84."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("Phần văn bản kết thúc này của Chương 10 chiếm các trang in 76–79 của ấn bản in (PDF tr. 81–84); toàn chương trải dài từ tr. 67–79 (PDF tr. 72–84). Cả bốn hình (10-1 đến 10-4) được vẽ lại dạng vector đã đơn giản hóa."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("Phụ kiện và phần mềm", "Accessories and Software"))
    b.append(p("Common accessories for digital positioners include built-in microswitches. These typically operate at low voltage (24 V). Such switches can provide a safety shutdown of the valve, initiated independently of the controller. Digital or analog travel-position indicating devices are also available. These positioners require software to perform the required diagnostic or remote calibration functions. Here are some capabilities that such a software package should support [3]:"))
    b.append(ul([
        "Reading the valve's diagnostic data",
        "Supporting a graphical diagnostic trend window display",
        "Valve configuration and a valve configuration database",
        "Monitoring device capabilities",
        "Configuration of valve characteristics",
        "General processes and a valve database",
        "Security levels for users",
        "A diagnostic database",
    ]))

    b.append(h2("Kết nối mọi thứ vào hệ điều khiển",
                "Connecting It All to the Control System"))
    b.append(p("To interact properly, the plant's control system needs an architecture in which transmitters, positioners, controllers, annunciators, computers, and so on, together with their associated software, are integrated into a structure that lets these devices communicate effectively with one another and perform in an efficient manner."))
    b.append(p("An efficient, field-based architecture can build process management solutions by networking intelligent field devices, scalable control system platforms, and software. Besides intelligent field devices (for example, smart positioners), this requires modular performance software. Done properly, such software can redefine management, expand process control, and provide solutions to asset-management problems. The software should:"))
    b.append(ul([
        "reduce installed cost;",
        "improve performance;",
        "be compatible with existing devices;",
        "reduce process offsets;",
        "be scalable;",
        "reduce maintenance cost;",
        "improve plant reliability;",
        "reduce training time; and",
        "be adaptable to changing processes.",
    ]))
    b.append(p("As shown in Figure 10-4, such an architecture will effectively change the previous typical 4 to 20 mA analog-signal-based “distributed control system (DCS)-centric” system into a new field-based architecture. This will effectively send the operator from the control room to the plant level."))
    b.append(fig(4, F.fig_f104()))
    b.append(p("Smart field devices such as smart valve positioners with control functions (PID) can do all of the following on a local level: loop control, signal processing, data acquisition, analyses, alarm detection, trend collection, and maintenance recording."))

    b.append(h2("Phụ kiện", "Accessories"))
    b.append(p("According to Bud Keyes [4], the process of transferring functionality out of the central control room and into the field devices is analogous to the computer industry's move from mainframe computing to PC-based networks."))
    b.append(p("The overall aim is to create a real-time management control system integrating all aspects of plant management, production control, process control, plant efficiency, and maintenance."))
    b.append(p("The maintenance program for control valves could include, for example, online diagnosis, remote calibration, preventive maintenance plans, and control of spare-parts inventory."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs([
        "S. G. Lloyd, “Guidelines for the Application of Valve Positioners,” Proceedings of the Texas A&amp;M Instrumentation Symposium, January (1969).",
        "D. W. St. Clair, Controller Tuning and Control Loop Performance, 2nd ed. (Newark, DE: Straight-Line Control Company, 1993).",
        "Béla G. Lipták, Process Control and Optimization, 4th ed., Vol. 2 (New York: Taylor &amp; Francis, 2006): 1197.",
        "M. A. Keyes, “Field-based Distributed Control Opens Door to Performance Improvements,” I&amp;CS (January 1997): 25–35.",
    ]))

    b.append(h3("Đọc thêm", "Additional Reading"))
    b.append(ul([
        "Hans-Josef Schneider, “Digitale Feldgerate: Vorteile, Probleme und Anforderungen aus Anwendersicht,” atp-Automatisierungstechnische Praxis 37, no. 4 (April 1995): 50–54.",
    ]))

    b.append(note("<b>Source notes.</b> (1) The OCR text layer contains line-break hyphenations («typ-ically», «perfor-mance», «mainte-nance», «diag-nosis») and other obvious damage; these were rejoined into whole words. In this section the source prints «build-in microswitches» where «built-in» is intended, and several reference titles are split across lines («Performance Improvements», «Anforde-rungen» in the Additional Reading item); all are restored. (The garbled «Coand ă» in the chapter prose belongs to the preceding section, where it is rendered as «Coandă».) (2) The source repeats the heading «Accessories»; both occurrences are retained. (3) All four figures (10-1 to 10-4) are simplified vector redrawings, not facsimiles; the equation/ideal-gas detail of Figure 10-2 is represented in simplified form. (4) The source credits SAMSON AG, Flowserve Inc., and Emerson Process Control on the relevant figures. (5) Table 10-1's «21/4 in» is presented as «2 1/4 in». (6) Printed pp. 67–79 correspond to PDF pp. 72–84."))
    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p("This final prose section of Chapter 10 occupies printed pp. 76–79 of the book (PDF pp. 81–84); the full chapter spans printed pp. 67–79 (PDF pp. 72–84). All four figures (10-1 to 10-4) are redrawn as simplified vectors."))
    return "".join(b)
