# -*- coding: utf-8 -*-
"""Book 4, Chapter 1 — Introduction (EN/VI bilingual)."""

PAGES_SRC = 4
BYLINE = "Crosby Valve Inc. · Technical Document TP-V300"
TITLE_EN = "Introduction to the Crosby Engineering Handbook"
TITLE_VI = "Giới thiệu Cẩm nang kỹ thuật Crosby"


def note_terms(lang):
    return ""


def body_vi():
    from prv_common import p, h2, lead
    b = []
    b.append(lead("Cẩm nang Kỹ thuật Van xả áp lực của Crosby chứa đựng những thông tin "
                  "kỹ thuật quan trọng liên quan đến van xả áp lực."))
    b.append(p("Mục đích chính của một van xả áp lực là bảo vệ tính mạng và tài sản bằng "
               "cách xả chất lưu ra khỏi một bình chịu áp lực đang quá áp. Thông tin trong "
               "cẩm nang này áp dụng cho việc bảo vệ quá áp của các bình áp lực, đường ống "
               "và hệ thống."))
    b.append(p("Cẩm nang có tham chiếu đến <i>ASME Boiler and Pressure Vessel Code</i>, "
               "Mục VIII — Thiết bị chịu áp lực (Pressure Vessels). Thông tin trong cẩm nang "
               "<b>không</b> được dùng để áp dụng bảo vệ quá áp cho nồi hơi công suất và thiết "
               "bị nhà máy điện hạt nhân, vốn được quy định riêng tại Mục I (Nồi hơi công suất) "
               "và Mục III (Thiết bị nhà máy điện hạt nhân) của cùng bộ tiêu chuẩn ASME."))
    b.append(p("Việc định cỡ, lựa chọn, chế tạo, lắp ráp, thử nghiệm, lắp đặt và bảo dưỡng "
               "đúng cách van xả áp lực đều mang tính chất quyết định để đạt được mức độ bảo "
               "vệ tối đa."))
    b.append(h2("Mục đích của cẩm nang", "Purpose of this handbook"))
    b.append(p("Cẩm nang được biên soạn nhằm phục vụ khách hàng của Crosby, trình bày các dữ "
               "liệu tham khảo và khuyến nghị kỹ thuật dựa trên nhiều năm kinh nghiệm định cỡ, "
               "lựa chọn, thử nghiệm, lắp đặt và vận hành van xả áp lực. Đủ dữ liệu được cung "
               "cấp để người dùng có thể định cỡ và lựa chọn đúng các van xả áp lực Crosby cho "
               "những ứng dụng cụ thể. Các nội dung về thuật ngữ, tiêu chuẩn, quy code, thiết "
               "kế cơ bản, định cỡ và lựa chọn được bao quát trong các chương tiếp theo."))
    b.append(h2("Một lưu ý về chương trình CROSBY-SIZE", "A note on CROSBY-SIZE"))
    b.append(p("Crosby cũng cung cấp chương trình định cỡ trên máy tính <i>CROSBY-SIZE</i>. "
               "Việc điều khiển chương trình qua cửa sổ pop-up, phím chức năng và trợ giúp trực "
               "tuyến giúp người dùng dễ hiểu và thao tác. Chương trình giả định người dùng đã "
               "có hiểu biết cơ bản về tính toán định cỡ van xả áp, và chính người dùng chịu "
               "trách nhiệm xác định đúng điều kiện vận hành cũng như tính phù hợp của chương "
               "trình cho từng ứng dụng cụ thể. Cả CROSBY-SIZE và cẩm nang kỹ thuật này đều là "
               "những công cụ hữu ích trong việc định cỡ van xả áp lực; nếu cần làm rõ thêm, "
               "xin liên hệ Crosby."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
               "© 1997 Crosby Valve Inc.</i>"))
    return "".join(b)


def body_en():
    from prv_common import p, h2, lead
    b = []
    b.append(lead("The Crosby Pressure Relief Valve Engineering Handbook contains important "
                  "technical information relating to pressure relief valves."))
    b.append(p("The primary purpose of a pressure relief valve is protection of life and "
               "property by venting fluid from an overpressurized vessel. The information in "
               "this handbook applies to the overpressure protection of pressure vessels, lines "
               "and systems."))
    b.append(p("Reference is made to the ASME Boiler and Pressure Vessel Code, Section VIII, "
               "Pressure Vessels. The information in this handbook is <b>not</b> to be used for "
               "the application of overpressure protection to power boilers and nuclear power "
               "plant components, which are addressed in the ASME Boiler and Pressure Vessel "
               "Code, Section I (Power Boilers) and Section III (Nuclear Power Plant "
               "Components), respectively."))
    b.append(p("Proper sizing, selection, manufacture, assembly, test, installation and "
               "maintenance of a pressure relief valve are all critical to obtaining maximum "
               "protection."))
    b.append(h2("Purpose of this handbook", "Mục đích của cẩm nang"))
    b.append(p("This handbook has been designed to provide a service to Crosby's customers by "
               "presenting reference data and technical recommendations based on many years of "
               "experience in sizing, selecting, testing, installing and operating pressure "
               "relief valves. Sufficient data is supplied to properly size and select Crosby "
               "pressure relief valves for specific applications. Terminology, standards, codes, "
               "basic design, sizing and selection are covered in the following chapters."))
    b.append(h2("A note on CROSBY-SIZE", "Một lưu ý về chương trình CROSBY-SIZE"))
    b.append(p("Crosby also offers the CROSBY-SIZE computer sizing program. Program control via "
               "pop-up windows, function keys and extensive on-line help makes it easy to "
               "understand and operate. It is assumed that the user has a basic understanding "
               "of relief valve sizing calculations and is responsible for correct determination "
               "of service conditions and the suitability of the program for a specific "
               "application. Both CROSBY-SIZE and this Engineering Handbook are useful tools in "
               "sizing pressure relief valves; should additional clarification be required, "
               "contact Crosby."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content © "
               "1997 Crosby Valve Inc.</i>"))
    return "".join(b)
