# -*- coding: utf-8 -*-
"""Book 4, Chapter 4 — Codes and Standards — Summary (EN/VI bilingual, no figures)."""

from prv_common import p, h2, h3, h4, ul, note

PAGES_SRC = 3
BYLINE = "Crosby Valve Inc. · Technical Document TP-V300"
TITLE_EN = "Codes and Standards — Summary"
TITLE_VI = "Tiêu chuẩn và quy code — Tóm tắt"


# Regulatory-body directory (proper nouns kept verbatim; addresses as printed).
_BODIES = [
    ("Allami Energetikai es Energiabiztonsagtechnikai Felugyelet (AEEF)",
     "State Authority for Energy, Management and Safety — Budapest VIII, Koztarsasag ter 7, Hungary"),
    ("American National Standards Institute (ANSI)",
     "1430 Broadway, New York, NY 10018, USA"),
    ("American Petroleum Institute (API)",
     "2101 L Street Northwest, Washington, DC 20037, USA"),
    ("The American Society of Mechanical Engineers (ASME)",
     "United Engineering Center, 345 East 47th Street, New York, NY 10017, USA"),
    ("Association Francaise de Normalisation (AFNOR)",
     "Tour Europe, Cedex 7, F-92049 Paris La Defence, France"),
    ("Australian Standards Association (SAA)",
     "No. 1 The Crescent Homebush, New South Wales 2140, Australia"),
    ("British Standards Institution (BSI)",
     "389 Chiswick High Road, London W4 4AL, England"),
    ("Canadian Standards Association (CSA)",
     "178 Rexdale Boulevard, Toronto, Ontario M9W 1R3, Canada"),
    ("Chlorine Institute Inc.",
     "2001 L Street, NW, Washington, DC 20036, USA"),
    ("CC NASTHOL",
     "Shenogina Street, 123007 Moscow, Russia"),
    ("Deutsches Institut fur Normung (DIN)",
     "Burggrafenstrasse 6, D-10787 Berlin, Germany"),
    ("Comite Europeen de Normalisation (CEN)",
     "rue de Stassart 36, B-1050 Brussels, Belgium"),
    ("Heat Exchange Institute, Inc. (HEI)",
     "1300 Sumner Avenue, Cleveland, OH 44115, USA"),
    ("International Organisation for Standardisation (ISO)",
     "Case Postale 56, CH-1211 Geneve 20, Switzerland"),
    ("I.S.C.I.R. Central",
     "Bucuresti, Frumoasa nr. 26, Romania"),
    ("Japanese Industrial Standard Committee / Japanese Standards Association (JISC/JSA)",
     "1-24, Akasaka 4-chome, Minato-ku, Tokyo 107, Japan"),
    ("Manufacturers' Standardization Society of the Valve and Fitting Industry (MSS)",
     "1815 North Fort Myer Drive, Arlington, VA 22209, USA"),
    ("Ministerie van Sociale Zaken en Werkgelegenheid — Dienst voor het Stoomwezen",
     "2517 KL Gravenhage — Eisenhowerlaan 102, Holland"),
    ("National Association of Corrosion Engineers (NACE)",
     "P.O. Box 1499, Houston, TX 77001, USA"),
    ("National Board of Boiler and Pressure Vessel Inspectors",
     "1055 Crupper Avenue, Columbus, OH 43229, USA"),
    ("National Fire Protection Association (NFPA)",
     "Batterymarch Park, Quincy, MA 02269, USA"),
    ("Schweizerischer Verein fur Druckbehalteruberwachung (SVDB)",
     "Postfach 35, 8030 Zurich, Switzerland"),
    ("Den Norske Trykkbeholderkomite (TBK)",
     "Norsk Verkstedsindustris Standardiseringssentral, Oscarsgate 20, Oslo, Norway"),
    ("Verband der Technischen Uberwachungs-Vereine e.V. (TUV)",
     "Kurfurstenstrasse 56, 4300 Essen 1, Germany"),
]


def _render_bodies(lang):
    out = []
    for name, addr in _BODIES:
        if lang == "vi":
            out.append("<b>%s</b> — %s" % (name, addr))
        else:
            out.append("<b>%s</b> — %s" % (name, addr))
    return ul(out)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> "
                "API — Viện Dầu khí Hoa Kỳ · ASME — Hội Kỹ sư Cơ khí Hoa Kỳ · "
                "BPVC — Quy code Thiết bị chịu áp lực · MSS-SP — Hội Tiêu chuẩn hóa "
                "của ngành Van và Phụ kiện · psig — pound trên inch vuông (theo độ gauge).")
    return ("<b>Key terms in this chapter.</b> "
            "API — American Petroleum Institute · ASME — American Society of Mechanical "
            "Engineers · BPVC — Boiler and Pressure Vessel Code · MSS-SP — Manufacturers "
            "Standardization Society · psig — pounds per square inch gauge.")


def body_vi():
    b = []
    b.append(p("Chương này tóm tắt các tiêu chuẩn và quy code (Codes and Standards) "
               "liên quan đến quy định, định cỡ, lựa chọn, lắp đặt và thử nghiệm van xả "
               "áp lực. Danh mục không nhằm thay thế các văn bản gốc mà cung cấp cho người "
               "dùng đường dẫn đến các tài liệu áp dụng."))
    b.append(h2("Viện Dầu khí Hoa Kỳ (API)", "American Petroleum Institute (API)"))
    b.append(h3("ANSI/API RP 520 Phần I — Định cỡ và Lựa chọn", "ANSI/API RP 520 Part I, Sizing and Selection"))
    b.append(p("Cẩm nang thiết kế API này được dùng rộng rãi để định cỡ van xả áp trên "
               "bình chứa chất lỏng và bình có chứa khí: (a) bình chất lỏng — các đoạn 5 và "
               "6, và (b) bình có chứa khí — Phụ lục D-3. RP này chỉ bao phủ các bình trên "
               "15 psig."))
    b.append(h3("ANSI/API RP 520 Phần II — Lắp đặt", "ANSI/API RP 520 Part II, Installation"))
    b.append(p("Bao gồm: (a) các thông lệ đường ống khuyến nghị, (b) công thức tính lực "
               "phản ứng lên van (2.4), và (c) các phòng ngừa khi xử lý trước lắp đặt và "
               "về bụi bẩn."))
    b.append(h3("ANSI/API RP 521 — Hướng dẫn Hệ thống Xả áp và Hạ áp", "ANSI/API RP 521, Guide for Pressure Relief and Depressuring Systems"))
    b.append(p("Một tài liệu xuất sắc bao quát mọi thứ từ nguyên nhân quá áp cho đến các "
               "cột đuốc xả (flare stacks)."))
    b.append(h3("ANSI/API RP 526 — Van xả áp thép mặt bích", "ANSI/API RP 526, Flanged Steel Relief Valves"))
    b.append(p("Đưa ra các tiêu chuẩn ngành về kích thước, cấp áp suất–nhiệt độ, áp suất "
               "thiết lập cực đại và vật liệu thân van."))
    b.append(h3("ANSI/API RP 527 — Độ kín đệm van xả áp", "ANSI/API RP 527, Seat Tightness of Pressure Relief Valves"))
    b.append(p("Tỷ lệ rò cho phép của van thông thường và van có bellows, cùng quy trình "
               "thử nghiệm."))
    b.append(h3("Hướng dẫn Kiểm tra Thiết bị Lọc dầu của API, Chương XVI — Thiết bị Xả áp", "API Guide for Inspection of Refinery Equipment, Chapter XVI"))
    b.append(p("Cung cấp: (a) hướng dẫn kiểm tra và lưu hồ sơ, và (b) tần suất kiểm tra, "
               "đoạn 1602.03."))
    b.append(h2("Hội Kỹ sư Cơ khí Hoa Kỳ (ASME) / ANSI", "American Society of Mechanical Engineers (ASME) / ANSI"))
    b.append(h3("ASME B31.1 — Đường ống Công suất", "ASME B31.1. Power Piping — Code 1995 Edition"))
    b.append(p("Các phần tham chiếu: Chương II, Phần 3, đoạn 107.8 — Van an toàn và van xả "
               "áp (kể cả thông tin chung, van an toàn và van xả áp trên đường ống ngoài nồi "
               "hơi, van an toàn xả trên đường ống ngoài không phải nồi hơi); và Chương II, "
               "Phần 6, đoạn 122.6 — Đường ống Xả áp."))
    b.append(h3("ASME/ANSI B16.5 — Mặt bích ống và phụ kiện mặt bích", "ASME/ANSI B16.5. Pipe flanges and flanged fittings"))
    b.append(p("Tiêu chuẩn cung cấp vật liệu cho phép, giới hạn áp suất–nhiệt độ và kích "
               "thước mặt bích chuẩn ANSI."))
    b.append(h3("ASME/ANSI B16.34 — Van mặt bích, ren và hàn", "ASME/ANSI B16.34. Valves — Flanged, Threaded and Welding End"))
    b.append(p("Tiêu chuẩn bao phủ cấp áp suất–nhiệt độ, kích thước, dung sai, vật liệu, "
               "các yêu cầu kiểm tra không phá hủy, thử nghiệm và đánh dấu cho van gang, rèn "
               "và chế tạo có đầu nối mặt bích, ren và hàn. (Kích thước và dung sai đầu nối "
               "chỉ áp dụng cho phần này.)"))
    b.append(h3("ANSI B31.8 — Hệ thống Truyền tải và Phân phối Khí", "ANSI B31.8. Gas Transmission and Distribution Systems"))
    b.append(p("Một số phần của tài liệu lớn này liên quan đến xả áp và các giới hạn của nó."))
    b.append(h2("Hội Tiêu chuẩn hóa của ngành Van và Phụ kiện (MSS-SP)", "Manufacturers Standardization Society (MSS-SP)"))
    b.append(h4("SP-25 — Hệ thống đánh dấu chuẩn cho van, phụ kiện, mặt bích và măng sông", "SP-25. Standard marking system for valves, fittings, flanges and unions"))
    b.append(p("(Không áp dụng cho van xả áp lực.) Tham khảo UG-129 của ASME Mục VIII về "
               "thông tin đánh dấu cho van xả áp lực."))
    b.append(h4("SP-55 — Tiêu chuẩn chất lượng cho đúc thép", "SP-55. Quality standards for steel castings"))
    b.append(p("Tiêu chuẩn chất lượng cho đúc thép dùng cho van, mặt bích, phụ kiện và "
               "các linh kiện đường ống khác."))
    b.append(h4("SP-61 — Thử áp suất van thép", "SP-61. Pressure testing of steel valves"))
    b.append(p("(Không áp dụng cho van xả áp lực.) Tham khảo API RP 527 cho các thử nghiệm "
               "độ kín đệm thương mại."))
    b.append(p("Các tiêu chuẩn khác cần cân nhắc: xem trang 4-2 và 4-3."))
    b.append(h2("Quy code và Tiêu chuẩn của Cơ quan Quy định", "Regulatory Body Codes and Standards"))
    b.append(p("Các cơ quan tiêu chuẩn và quy code dưới đây ban hành hoặc quản lý các tài "
               "liệu áp dụng cho van xả áp lực. Địa chỉ và danh mục được trích trực tiếp từ "
               "cẩm nang gốc (trang 4-2 và 4-3)."))
    b.append(_render_bodies("vi"))
    b.append(h3("Các họ tiêu chuẩn tiêu biểu được ban hành", "Representative families of standards issued"))
    b.append(ul([
        "<b>ASME Boiler and Pressure Vessel Code (BPVC)</b> — Mục I (Nồi hơi công suất), II (Vật liệu), IV (Nồi hơi sưởi), VII (Vận hành nồi hơi công suất), VIII (Thiết bị chịu áp lực), IX (Chứng nhận hàn và hàn thau)",
        "<b>API</b> — RP 510 (Quy code kiểm tra bình chịu áp), RP 520 (Thiết kế/lắp đặt hệ thống xả áp), RP 521 (Hệ thống xả áp/hạ áp), Standard 526 (Van an toàn xả thép mặt bích), Standard 527 (Độ kín đệm thương mại), Standard 2000 (Thông gió bình chứa áp suất thấp), Hướng dẫn Kiểm tra Chương XVI",
        "<b>ANSI/ASME PTC 25.3</b> — Quy code Thử nghiệm vận hành, Van an toàn và xả áp",
        "<b>ISO / CEN</b> — ISO-9000 (Hệ thống chất lượng), ISO-4126 (Van an toàn — Yêu cầu chung), Chỉ thị Thiết bị chịu áp lực (Pressure Equipment Directive), các tiêu chuẩn CEN cho van an toàn",
        "<b>Quốc gia</b> — JIS B8210 (Nhật Bản), BS6759 (Anh), DIN (Đức), GOST R (Nga), CSA Z299 (Canada), AS/NZS (Úc), NFE 29-410 đến 420 (Pháp), TBK / TRD 421 / AD-Merkblatt A2 (Đức)",
        "<b>Ngành</b> — NACE MR0175 (chống ăn mòn), NFPA 30 (Chất lỏng cháy và dễ cháy), HEI (Bình gia nhiệt kín), Stoomwezen A1301, NB-25 / NB-65 (National Board), MSS SP-6 / SP-9 / SP-55",
    ]))
    b.append(note("Tóm tắt: chương liệt kê các quy code và tiêu chuẩn chi phối thiết kế, định "
                  "cỡ, lắp đặt và kiểm tra van xả áp — chủ yếu API, ASME/BPVC, ANSI và MSS-SP "
                  "— cùng danh mục các cơ quan tiêu chuẩn quốc gia và quốc tế."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
               "© 1997 Crosby Valve Inc.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(p("This chapter contains a summary of the Codes and Standards applicable to the "
               "specification, sizing, selection, installation and testing of pressure relief "
               "valves. The listing is a pointer to the applicable documents, not a substitute "
               "for the source texts themselves."))
    b.append(h2("American Petroleum Institute (API)", "Viện Dầu khí Hoa Kỳ (API)"))
    b.append(h3("ANSI/API RP 520 Part I, Sizing and Selection", "ANSI/API RP 520 Phần I — Định cỡ và Lựa chọn"))
    b.append(p("This API design manual is widely used for sizing of relief valves on both "
               "liquid and gas filled vessels: (a) liquid vessels — paragraphs 5 and 6, and "
               "(b) gas filled vessels — Appendix D-3. This RP covers only vessels above "
               "15 psig."))
    b.append(h3("ANSI/API RP 520 Part II, Installation", "ANSI/API RP 520 Phần II — Lắp đặt"))
    b.append(p("This includes: (a) recommended piping practices, (b) calculation formula for "
               "reactive force on valve (2.4), and (c) precautions on preinstallation handling "
               "and dirt."))
    b.append(h3("ANSI/API RP 521, Guide for Pressure Relief and Depressuring Systems", "ANSI/API RP 521 — Hệ thống Xả áp và Hạ áp"))
    b.append(p("An excellent document on everything from causes of overpressure through flare "
               "stacks."))
    b.append(h3("ANSI/API RP 526, Flanged Steel Relief Valves", "ANSI/API RP 526 — Van xả áp thép mặt bích"))
    b.append(p("Gives industry standards as to dimensions, pressure-temperature ratings, "
               "maximum set pressures, body materials."))
    b.append(h3("ANSI/API RP 527, Seat Tightness of Pressure Relief Valves", "ANSI/API RP 527 — Độ kín đệm van xả áp"))
    b.append(p("Permissible leakage rate of conventional and bellows valves and testing "
               "procedure."))
    b.append(h3("API Guide for Inspection of Refinery Equipment, Chapter XVI — Pressure Relieving Devices", "API Hướng dẫn Kiểm tra, Chương XVI"))
    b.append(p("Gives: (a) guide for inspection and record keeping, and (b) frequency of "
               "inspection, Paragraph 1602.03."))
    b.append(h2("American Society of Mechanical Engineers (ASME) / ANSI", "Hội Kỹ sư Cơ khí Hoa Kỳ (ASME) / ANSI"))
    b.append(h3("ASME B31.1. Power Piping — Code 1995 Edition", "ASME B31.1 — Đường ống Công suất"))
    b.append(p("Reference sections: Chapter II, Part 3, Paragraph 107.8 Safety and relief "
               "valves including general information, safety and relief valves on boiler "
               "external piping, safety relief valves on non boiler external piping, and "
               "non mandatory appendices on valve installations; and Chapter II, Part 6, "
               "Paragraph 122.6 — Pressure Relief Piping."))
    b.append(h3("ASME/ANSI B16.5. Pipe flanges and flanged fittings", "ASME/ANSI B16.5 — Mặt bích ống"))
    b.append(p("This standard provides allowable materials, pressure temperature limits and "
               "flange dimensions for standard ANSI flanges."))
    b.append(h3("ASME/ANSI B16.34. Valves — Flanged, Threaded and Welding End", "ASME/ANSI B16.34 — Van mặt bích, ren và hàn"))
    b.append(p("Standard covers pressure, temperature ratings, dimensions, tolerances, "
               "materials, nondestructive examination requirements, testing and marking for "
               "cast, forged and manufactured flanged, threaded and welding end valves. (End "
               "connection dimensions and tolerances are applicable only.)"))
    b.append(h3("ANSI B31.8. Gas Transmission and Distribution Systems", "ANSI B31.8 — Hệ thống Truyền tải Khí"))
    b.append(p("Portions of this large document pertain to pressure relief and its "
               "limitations."))
    b.append(h2("Manufacturers Standardization Society (MSS-SP)", "Hội Tiêu chuẩn hóa của ngành Van và Phụ kiện (MSS-SP)"))
    b.append(h4("SP-25. Standard marking system for valves, fittings, flanges and unions", "SP-25 — Hệ thống đánh dấu chuẩn"))
    b.append(p("(Not applicable to pressure relief valves.) Refer to UG-129 of ASME Section "
               "VIII for marking information for pressure relief valves."))
    b.append(h4("SP-55. Quality standards for steel castings", "SP-55 — Tiêu chuẩn chất lượng đúc thép"))
    b.append(p("Quality standards for steel castings for valves, flanges and fittings and "
               "other piping components."))
    b.append(h4("SP-61. Pressure testing of steel valves", "SP-61 — Thử áp suất van thép"))
    b.append(p("(Not applicable to pressure relief valves.) Refer to API Recommended Practice "
               "527 for commercial seat tightness tests."))
    b.append(p("Other Standards to be considered: See pages 4-2 and 4-3."))
    b.append(h2("Regulatory Body Codes and Standards", "Quy code và Tiêu chuẩn của Cơ quan Quy định"))
    b.append(p("The standards bodies below issue or administer the documents applicable to "
               "pressure relief valves. Addresses and catalogues are taken directly from the "
               "source handbook (pages 4-2 and 4-3)."))
    b.append(_render_bodies("en"))
    b.append(h3("Representative families of standards issued", "Các họ tiêu chuẩn tiêu biểu"))
    b.append(ul([
        "<b>ASME Boiler and Pressure Vessel Code (BPVC)</b> — Section I (Power Boilers), II (Materials), IV (Heating Boilers), VII (Care of Power Boilers), VIII (Pressure Vessels), IX (Welding and Brazing Qualifications)",
        "<b>API</b> — RP 510 (Pressure Vessel Inspection Code), RP 520 (Design/Installation of Pressure Relieving Systems), RP 521 (Pressure Relief and Depressuring Systems), Standard 526 (Flanged Steel Safety Relief Valves), Standard 527 (Commercial Seat Tightness), Standard 2000 (Venting Atmospheric and Low Pressure Storage Tanks), Guide for Inspection of Refinery Equipment Chapter XVI",
        "<b>ANSI/ASME PTC 25.3</b> — Performance Test Code, Safety and Relief Valves",
        "<b>ISO / CEN</b> — ISO-9000 (Quality System), ISO-4126 (Safety Valves — General Requirements), Pressure Equipment Directive, CEN Standards for Safety Valves",
        "<b>National</b> — JIS B8210 (Japan), BS6759 (UK), DIN (Germany), GOST R (Russia), CSA Z299 (Canada), AS (Australia), NFE 29-410 to 420 (France), TBK / TRD 421 / AD-Merkblatt A2 (Germany)",
        "<b>Industry</b> — NACE MR0175 (corrosion), NFPA 30 (Flammable and Combustible Liquids), HEI (Closed Feedwater Heaters), Stoomwezen A1301, NB-25 / NB-65 (National Board), MSS SP-6 / SP-9 / SP-55",
    ]))
    b.append(note("Summary: this chapter lists the Codes and Standards that govern the design, "
                  "sizing, installation and inspection of pressure relief valves — principally "
                  "API, ASME/BPVC, ANSI and MSS-SP — together with a directory of national and "
                  "international standards bodies."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content © "
               "1997 Crosby Valve Inc.</i>"))
    return "".join(b)
