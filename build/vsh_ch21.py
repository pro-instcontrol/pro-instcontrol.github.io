# -*- coding: utf-8 -*-
"""Book 6, Unit 21 — Appendices (EN/VI).

Source: Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004), book
pp. 327–361 (PDF pp. 341–375): Appendix A abbreviations, Appendix B
properties of fluids, Appendix C standards pertaining to valves,
Appendix D SI units, Appendix E valve glossary.  Selections and
summaries of the source tables; not a verbatim reproduction.
"""

from vsh_common import fig, h2, h3, p, table, ul
import vshfig18 as F18

PAGES_SRC = 35         # source book pp. 327-361
BYLINE = "Peter Smith & R. W. Zappe · Valve Selection Handbook, 5th ed. (2004)"
TITLE_EN = "Appendices — Abbreviations, Standards, SI Units and Glossary"
TITLE_VI = "Phụ lục — Viết tắt, tiêu chuẩn, hệ đơn vị SI và thuật ngữ"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ đơn vị 21.</b> reduced pressure/temperature "
                "— áp suất / nhiệt độ quy đổi · compressibility factor — "
                "hệ số nén · critical pressure — áp suất tới hạn · standard "
                "— tiêu chuẩn · base unit — đơn vị cơ bản · derived unit — "
                "đơn vị dẫn xuất · conversion factor — hệ số chuyển đổi · "
                "glossary — bảng thuật ngữ · trim — cụ thể bên trong van · "
                "breakout torque — mô-men khởi động.")
    return ("<b>Key terms.</b> reduced pressure / temperature · "
            "compressibility factor · critical pressure · standard · base "
            "unit · derived unit · conversion factor · glossary · trim · "
            "breakout torque.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(items):
        b.append(ul([(i[0] if vi else i[1]) for i in items]))

    def FIG(n, fn):
        b.append(fig(n, fn))

    # ============================================================= intro
    H("Về phần phụ lục", "About the appendices")
    P("Sách kết thúc bằng năm phụ lục tra cứu: các viết tắt của tổ chức và "
      "tiêu chuẩn trong ngành van quốc tế (A), tính chất của lưu chất (B), "
      "các tiêu chuẩn liên quan đến van (C), Hệ đơn vị quốc tế SI (D) và "
      "bảng thuật ngữ van (E). Đơn vị này tóm lược nội dung các phụ lục ở "
      "mức tra cứu nhanh; số liệu đầy đủ nằm trong sách gốc.",
      "The book closes with five reference appendices: abbreviations of "
      "organizations and standards related to the international valve "
      "industry (A), properties of fluids (B), standards pertaining to "
      "valves (C), the International System of Units (D), and a valve "
      "glossary (E). This unit summarizes the appendices at quick-reference "
      "depth; the full data tables are in the source book.")

    # ============================================================= appendix A
    H("Phụ lục A — Viết tắt tổ chức và tiêu chuẩn",
      "Appendix A — Abbreviations of organizations and standards")
    P("Bảng dưới đây chọn các viết tắt hay gặp nhất khi đọc tiêu chuẩn van "
      "và tài liệu thiết kế.",
      "The table below lists the abbreviations most often met when reading "
      "valve standards and design documentation.")
    b.append(table(
        ["Viết tắt", "Tổ chức"]
        if vi else ["Abbreviation", "Organization"],
        [
            ["ANSI", "American National Standards Institute"],
            ["API", "American Petroleum Institute"],
            ["ASME", "American Society of Mechanical Engineers"],
            ["ASTM", "American Society for Testing and Materials"],
            ["AWS", "American Welding Society"],
            ["AFNOR", "Association Francaise de Normalisation (Pháp)"],
            ["BSI", "British Standards Institute"],
            ["DIN", "Deutsches Institut fur Normung (Germany)"],
            ["ISO", "International Standards Organization"],
            ["MSS", "Manufacturers Standardization Society"],
            ["NACE", "National Association of Corrosion Engineers"],
            ["NFPA", "National Fire Prevention Association"],
            ["TEMA", "Tubular Exchanger Manufacturers Association"],
            ["VMA", "Valve Manufacturers Association"],
        ],
        caption=("Chọn từ Phụ lục A, book pp. 327–328." if vi else
                 "Selected from Appendix A, book pp. 327–328."),
        cls="tbl"))

    # ============================================================= appendix B
    H("Phụ lục B — Tính chất của lưu chất", "Appendix B — Properties of fluids")
    P("Phụ lục B chứa ba biểu đồ hệ số nén Z theo áp suất quy đổi Pr "
      "(B-1 cho Pr = 0…0,5; B-2 cho Pr = 0…10; B-3 cho Pr = 0…40) và Bảng "
      "B-1 với hằng số vật lý của các khí và hơi: khối lượng phân tử, hằng "
      "số khí riêng, hệ số đẳng entropy k, nhiệt độ tới hạn Tc và áp suất "
      "tới hạn Pc. Các biểu đồ này phục vụ việc định cỡ van giải áp ở đơn "
      "vị 17: hệ số nén được dùng khi áp suất vận hành tới gần vùng tới "
      "hạn, nơi hành vi của khí khác xa khí lý tưởng.",
      "Appendix B contains three compressibility factor charts of Z "
      "against reduced pressure Pr (B-1 for Pr = 0 to 0.5, B-2 for Pr = 0 "
      "to 10, B-3 for Pr = 0 to 40) and Table B-1 with the physical "
      "constants of gases and vapors: molecular mass, individual gas "
      "constant, isentropic exponent k, critical temperature Tc and "
      "critical pressure Pc. These charts serve the sizing of pressure "
      "relief devices in Unit 17: the compressibility factor is applied "
      "when the operating pressure approaches the critical region, where "
      "real-gas behavior departs from the ideal-gas model.")
    FIG(1, F18.fig_vsh_b_1())
    P("Ví dụ các giá trị Bảng B-1 (chọn lọc):",
      "Selected values from Table B-1:")
    b.append(table(
        ["Khí / hơi", "M (kg/kmol)", "k", "Tc (K)", "Pc (MPa)"]
        if vi else ["Gas / vapor", "M (kg/kmol)", "k", "Tc (K)",
                    "Pc (MPa)"],
        [
            ["Khí trời (Air)" if vi else "Air", "28.96", "1.40", "132.4",
             "3.776"],
            ["Nito (N2)" if vi else "Nitrogen (N2)", "28.016", "1.40",
             "126.3", "3.383"],
            ["Oxy (O2)" if vi else "Oxygen (O2)", "32.000", "1.40",
             "154.77", "5.080"],
            ["Metan (CH4)" if vi else "Methane (CH4)", "16.034", "1.31",
             "190.7", "4.629"],
            ["Etan (C2H6)" if vi else "Ethane (C2H6)", "30.070", "1.20",
             "305.42", "4.884"],
            ["Propan (C3H8)" if vi else "Propane (C3H8)", "44.097", "—",
             "370.0", "4.256"],
            ["CO2", "44.011", "1.30", "304.2", "7.385"],
            ["Hơi nước (H2O, 100 °C)" if vi else "Water vapor (H2O)",
             "18.016", "1.33", "647.3", "22.129"],
        ],
        caption=("Chọn từ Bảng B-1, book pp. 333–334; nguồn VDI Blatt 4. "
                 "k — hệ số đẳng entropy ở 273 K." if vi else
                 "Selected from Table B-1, book pp. 333–334; source VDI "
                 "Blatt 4. k — isentropic coefficient at 273 K."),
        cls="tbl"))

    # ============================================================= appendix C
    H("Phụ lục C — Tiêu chuẩn liên quan đến van",
      "Appendix C — Standards pertaining to valves")
    P("Phụ lục C liệt kê các tiêu chuẩn Mỹ và Anh về van, theo chỉ mục tiêu "
      "chuẩn của các tổ chức cho năm 2003. Vì tiêu chuẩn mới liên tục được "
      "phát hành và tiêu chuẩn cũ được sửa đổi hoặc rút bỏ, tính hiệu lực "
      "phải được kiểm tra trước khi áp dụng. Bảng sau chọn các tiêu chuẩn "
      "hay gặp theo nhóm van.",
      "Appendix C lists common USA and British standards pertaining to "
      "valves, as published in the standard indexes of the various "
      "standard organizations for 2003. Because new standards are "
      "continually issued and old standards revised or withdrawn, the "
      "validity of these standards should be verified prior to application. "
      "The table below selects the most frequently met standards by valve "
      "group.")
    b.append(table(
        ["Nhóm", "Tiêu chuẩn", "Nội dung"]
        if vi else ["Group", "Standard", "Coverage"],
        [
            ["đầu nối & chung" if vi else "ends & general",
             "ASME B16.5",
             "mặt bích ống và phụ tùng mặt bích" if vi else
             "pipe flanges and flanged fittings"],
            ["đầu nối & chung" if vi else "ends & general",
             "ASME B16.34",
             "van thép, đầu mặt bích và hàn đối tiếp" if vi else
             "steel valves, flanged and butt-welding ends"],
            ["đầu nối & chung" if vi else "ends & general",
             "MSS SP-6",
             "độ nhám bề mặt tiếp xúc của mặt bích" if vi else
             "standard finishes for flange contact faces"],
            ["van cầu" if vi else "globe valves",
             "BS 1873",
             "van cầu thép và van chặn – kiểm (dầu mỏ, hóa dầu)" if vi
             else "steel globe, and stop and check valves (petroleum, "
             "petrochemical)"],
            ["van cầu" if vi else "globe valves",
             "MSS SP-80",
             "van gate, cầu, góc, kiểm đồng thau" if vi else
             "bronze gate, globe, angle, and check valves"],
            ["van gate" if vi else "gate valves",
             "API Std 600",
             "van gate thép nắp bắt bu-lông (dầu mỏ)" if vi else
             "bolted bonnet steel gate valves (petroleum)"],
            ["van gate" if vi else "gate valves",
             "BS 1414",
             "van gate nêm thép, mặt bích và hàn đối tiếp" if vi else
             "steel wedge gate valves, flanged and butt-welding"],
            ["van cắm" if vi else "plug valves",
             "BS 5353",
             "đặc tả van cắm" if vi else "specification for plug valves"],
            ["van bi" if vi else "ball valves",
             "MSS SP-72",
             "van bi mặt bích hoặc hàn đối tiếp" if vi else
             "ball valves with flanged or butt-welding ends"],
            ["van bi" if vi else "ball valves",
             "API 6D",
             "van đường ống: gate, cắm, bi, kiểm" if vi else
             "pipeline valves: gate, plug, ball and check"],
            ["van bướm" if vi else "butterfly valves",
             "API Std 609",
             "van bướm double-flanged, lug và wafer" if vi else
             "butterfly valves, double-flanged lug-type and wafer"],
            ["van kiểm" if vi else "check valves",
             "API Std 594",
             "van kiểm wafer, wafer-lug và double-flanged" if vi else
             "check valves: wafer, wafer-lug and double-flanged"],
            ["kiểm tra & thử" if vi else "inspection & test",
             "API Std 598",
             "kiểm tra và thử van" if vi else "valve inspection and test"],
            ["cháy" if vi else "fire test",
             "API RP 6FA / 607",
             "thử cháy van và van đế mềm" if vi else
             "fire test for valves and soft-seated quarter-turn valves"],
            ["van giải áp" if vi else "pressure relief",
             "ISO 6718 / ASME",
             "đĩa nứt vỡ và thiết bị giải áp" if vi else
             "bursting discs and pressure relief devices"],
            ["thông hơi bụi" if vi else "explosion venting",
             "NFPA 68 / VDI 3673",
             "xả áp vụ nổ bụi" if vi else "dust explosion venting"],
        ],
        caption=("Chọn từ Phụ lục C, book pp. 335–344. Tính hiệu lực "
                 "phải kiểm tra trước khi áp dụng." if vi else
                 "Selected from Appendix C, book pp. 335–344. Verify "
                 "validity prior to application."),
        cls="tbl wide"))

    # ============================================================= appendix D
    H("Phụ lục D — Hệ đơn vị quốc tế (SI)",
      "Appendix D — International System of Units (SI)")
    P("Hệ SI dựa trên bảy đơn vị cơ bản và hai đơn vị bổ sung; các đơn vị "
      "dẫn xuất được biểu diễn qua chúng hoặc qua các đơn vị dẫn xuất khác, "
      "và các bội/thập phân tạo bằng tiền tố. Khi làm việc với tài liệu van "
      "Mỹ, các hệ số chuyển đổi ở Bảng D-7 của sách gốc chuyển giữa đơn vị "
      "Imperial, metric và SI cho chiều dài, diện tích, thể tích, lưu lượng "
      "thể tích, khối lượng, lưu lượng khối lượng, áp suất, nhiệt độ, năng "
      "lượng và công suất.",
      "The SI system is built on seven base units and two supplementary "
      "units; derived units are expressed in terms of these or of other "
      "derived units, and decimal multiples are formed with prefixes. When "
      "working with US valve documentation, the conversion factors in Table "
      "D-7 of the source book convert between Imperial, metric, and SI "
      "units for length, area, volume, volume flow, mass, mass flow, "
      "pressure, temperature, energy, and power.")
    b.append(table(
        ["Đại lượng", "Đơn vị SI", "Ký hiệu", "Ghi chú"]
        if vi else ["Quantity", "SI unit", "Symbol", "Note"],
        [
            ["chiều dài" if vi else "length", "meter", "m",
             "đơn vị cơ bản" if vi else "base unit"],
            ["khối lượng" if vi else "mass", "kilogram", "kg",
             "đơn vị cơ bản" if vi else "base unit"],
            ["thời gian" if vi else "time", "second", "s",
             "đơn vị cơ bản" if vi else "base unit"],
            ["dòng điện" if vi else "electric current", "ampere", "A",
             "đơn vị cơ bản" if vi else "base unit"],
            ["nhiệt độ" if vi else "temperature", "kelvin", "K",
             "đơn vị cơ bản" if vi else "base unit"],
            ["cường độ sáng" if vi else "luminous intensity", "candela",
             "cd", "đơn vị cơ bản" if vi else "base unit"],
            ["lượng chất" if vi else "amount of substance", "mole", "mol",
             "đơn vị cơ bản" if vi else "base unit"],
            ["góc phẳng" if vi else "plane angle", "radian", "rad",
             "đơn vị bổ sung" if vi else "supplementary unit"],
            ["lực" if vi else "force", "newton",
             "1 N = 1 kg·m/s²",
             "đơn vị dẫn xuất có tên riêng" if vi else
             "derived unit with special name"],
            ["áp suất" if vi else "pressure", "pascal",
             "1 Pa = 1 N/m²",
             "đơn vị dẫn xuất có tên riêng" if vi else
             "derived unit with special name"],
            ["năng lượng" if vi else "energy", "joule", "1 J = 1 N·m",
             "đơn vị dẫn xuất có tên riêng" if vi else
             "derived unit with special name"],
            ["công suất" if vi else "power", "watt", "1 W = 1 J/s",
             "đơn vị dẫn xuất có tên riêng" if vi else
             "derived unit with special name"],
            ["áp suất kỹ thuật" if vi else "engineering pressure", "bar",
             "1 bar = 10⁵ Pa",
             "hay dùng trong tài liệu van" if vi else
             "common in valve documentation"],
        ],
        caption=("Chọn từ Bảng D-1…D-4, book pp. 346–347." if vi else
                 "Selected from Tables D-1…D-4, book pp. 346–347."),
        cls="tbl"))
    P("Ví dụ hệ số chuyển đổi áp suất (Bảng D-7): 1 psi = 6,8948 kPa; "
      "1 bar = 14,504 psi; 1 MPa = 145,04 psi; 1 atm = 101,325 kPa. Ví dụ "
      "chiều dài: 1 in = 25,4 mm (chính xác); 1 ft = 0,3048 m (chính xác); "
      "1 mile = 1,60934 km. Ví dụ lưu lượng: 1 US gal/min = 0,2271 m³/h; "
      "1 ft³/min = 1,699 m³/h.",
      "Sample pressure conversion factors (Table D-7): 1 psi = 6.8948 kPa; "
      "1 bar = 14.504 psi; 1 MPa = 145.04 psi; 1 atm = 101.325 kPa. Length: "
      "1 in = 25.4 mm (exact); 1 ft = 0.3048 m (exact); 1 mile = 1.60934 "
      "km. Flow: 1 US gal/min = 0.2271 m³/h; 1 ft³/min = 1.699 m³/h.")

    # ============================================================= appendix E
    H("Phụ lục E — Bảng thuật ngữ van", "Appendix E — Valve glossary")
    P("Phụ lục E giải thích các thuật ngữ hay dùng trong ngành van: kiểu "
      "van, chức năng, bộ phận, vật liệu và đặc tính thiết kế. Bảng sau "
      "chọn một số thuật ngữ gốc đã xuất hiện rải rác trong các đơn vị "
      "trước.",
      "Appendix E defines the terms used in the valve industry: valve "
      "types, functions, components, materials of construction, and design "
      "characteristics. The table below selects terms already met across "
      "the earlier units.")
    b.append(table(
        ["Thuật ngữ", "Định nghĩa rút gọn"]
        if vi else ["Term", "Short definition"],
        [
            ["accessory" if vi else "Accessory",
             "thiết bị gắn trên cơ cấu chấp hành cho chức năng thêm (vận "
             "hành tay, bộ định vị…)" if vi else
             "device attached to the actuator providing an additional "
             "function, e.g. manual operation, positioner"],
            ["áp suất ngược" if vi else "Back pressure",
             "áp suất tác dụng lên phía hạ lưu của đế van" if vi else
             "pressure exerted on the downstream side of a valve seat"],
            ["back seat" if vi else "Back seats",
             "vùng thân van kín với nắp để lưu chất không vào hộp Gioăng "
             "đệm" if vi else
             "stem area sealed to the bonnet to keep process fluid out of "
             "the packing box"],
            ["van bi" if vi else "Ball valve",
             "van quay 1/4 vòng với phần tử đóng hình cầu giữa hai đế; "
             "đóng kín tốt" if vi else
             "quarter-turn valve with a spherical closure element between "
             "two seats; good shut-off"],
            ["bubble-tight" if vi else "Bubble-tight",
             "không đo được rò rỉ qua đế ở mức nhất định" if vi else
             "no measurable seat leakage over a certain period"],
            ["mô-men khởi động" if vi else "Breakout torque",
             "mô-men cần để mở hoặc thoát đế van quay" if vi else
             "torque required to open or unseat a rotary valve"],
            ["body" if vi else "Body",
             "chi tiết chính chịu áp, chứa phần tử đóng" if vi else
             "main pressure-containing component; contains the closure "
             "device"],
            ["bonnet" if vi else "Bonnet",
             "chi tiết chịu áp chứa hộp đệm kín (packing box) và trục; bắt vít, mặt "
             "bích hoặc hàn vào thân" if vi else
             "pressure-containing component containing the packing box and "
             "stem; screwed, flanged or welded to the body"],
            ["trim" if vi else "Trim",
             "các chi tiết bên trong tiếp xúc lưu chất (đế, cổ trục, tấm "
             "đế…)" if vi else
             "internal wetted parts of the valve (seat, stem, disc…)"],
            ["trunnion" if vi else "Trunnion",
             "trục đỡ bi van bi cỡ lớn để bi không ép đế" if vi else
             "support shafts for large ball valves so the ball does not "
             "load the seats"],
            ["wafer" if vi else "Wafer design",
             "thân van kẹp giữa hai mặt bích ống, không có mặt bích riêng"
             if vi else
             "valve body clamped between pipe flanges, without its own "
             "flanges"],
            ["hiệu ứng waterhammer" if vi else "Waterhammer effect",
             "sóng áp do đóng/mở van nhanh gây xung lực đường ống" if vi
             else "pressure surge caused by rapid valve closure or "
             "opening"],
            ["WOG" if vi else "WOG rating",
             "cấp áp danh nghĩa cho dịch vụ nước – dầu – khí" if vi else
             "nominal rating for water, oil, gas service"],
            ["WSP" if vi else "WSP rating",
             "cấp áp cho hơi nước bão hòa nóng" if vi else
             "wet steam pressure rating"],
        ],
        caption=("Chọn và tóm lược từ Phụ lục E, book pp. 363–381." if vi
                 else "Selected and condensed from Appendix E, book "
                 "pp. 363–381."),
        cls="tbl wide"))

    # ============================================================= summary
    H("Tóm tắt đơn vị 21", "Unit 21 summary")
    b.append(table(
        ["Phụ lục", "Nội dung", "Dùng khi nào"]
        if vi else ["Appendix", "Contents", "Use it when"],
        [
            ["A" if vi else "A",
             "viết tắt tổ chức và tiêu chuẩn" if vi else
             "organization and standard abbreviations",
             "đọc tiêu chuẩn, bản vẽ, tài liệu mua sắm" if vi else
             "reading standards, drawings, procurement documents"],
            ["B" if vi else "B",
             "hệ số nén Z và hằng số khí (Bảng B-1)" if vi else
             "compressibility factor Z and gas constants (Table B-1)",
             "định cỡ van giải áp ở áp cao, gần vùng tới hạn" if vi else
             "sizing relief valves at high pressure near the critical "
             "region"],
            ["C" if vi else "C",
             "tiêu chuẩn Mỹ / Anh theo nhóm van" if vi else
             "USA / British standards by valve group",
             "chọn tiêu chuẩn thiết kế, thử và mua hàng" if vi else
             "selecting design, test and procurement standards"],
            ["D" if vi else "D",
             "đơn vị SI và hệ số chuyển đổi" if vi else
             "SI units and conversion factors",
             "đổi giữa Imperial, metric và SI" if vi else
             "converting between Imperial, metric and SI"],
            ["E" if vi else "E",
             "bảng thuật ngữ van" if vi else "valve glossary",
             "tra nghĩa thuật ngữ kỹ thuật" if vi else
             "looking up technical terminology"],
        ],
        caption=("Tóm tắt theo văn bản nguồn, book pp. 327–361." if vi
                 else "Summary from source text, book pp. 327–361."),
        cls="tbl"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
