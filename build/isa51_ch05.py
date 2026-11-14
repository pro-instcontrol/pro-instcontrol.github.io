# -*- coding: utf-8 -*-
"""ANSI/ISA-5.1 — Chapter 5: Tables 2 and 3 (§§5.3–5.4)."""
import isa51fig as F
from isa51_common import T, fig, h2, h3, lead, note, p, table, ul

PAGES_SRC = 6
BYLINE = "ANSI/ISA-5.1-1984 (R1992) · §5.3–5.4"

# Typical letter combinations (Table 2, abridged to the most-used first-letters)
COMBOS = [
    ("A", ("Phân tích", "Analysis"), "ARC  AIC  AC", "AR  AI", "ASH  ASL  ASHL",
     "ART  AIT  AT", "AE", "AV"),
    ("E", ("Điện áp", "Voltage"), "ERC  EIC  EC", "ER  EI", "ESH  ESL  ESHL",
     "ERT  EIT  ET", "EE", "EZ"),
    ("F", ("Lưu lượng", "Flow Rate"), "FRC  FIC  FC  FCV", "FR  FI",
     "FSH  FSL  FSHL", "FRT  FIT  FT", "FE  FP  FG", "FV"),
    ("FQ", ("Lượng lưu chất", "Flow Quantity"), "FQRC  FQIC", "FQR  FQI",
     "FQSH  FQSL", "FQIT  FQT", "FQE", "FQV"),
    ("FF", ("Tỷ lệ lưu lượng", "Flow Ratio"), "FFRC  FFIC  FFC", "FFR  FFI",
     "FFSH  FFSL", "—", "FE", "FFV"),
    ("H", ("Bằng tay", "Hand"), "HIC  HC", "—", "HS", "—", "—", "HV"),
    ("I", ("Dòng điện", "Current"), "IRC  IIC", "IR  II", "ISH  ISL  ISHL",
     "IRT  IIT  IT", "IE", "IZ"),
    ("J", ("Công suất", "Power"), "JRC  JIC", "JR  JI", "JSH  JSL  JSHL",
     "JRT  JIT  JT", "JE", "JV"),
    ("K", ("Thời gian", "Time"), "KRC  KIC  KC  KCV", "KR  KI",
     "KSH  KSL  KSHL", "KRT  KIT  KT", "KE", "KV"),
    ("L", ("Mức", "Level"), "LRC  LIC  LC  LCV", "LR  LI",
     "LSH  LSL  LSHL", "LRT  LIT  LT", "LE  LW  LG", "LV"),
    ("P", ("Áp suất / chân không", "Pressure / Vacuum"),
     "PRC  PIC  PC  PCV", "PR  PI", "PSH  PSL  PSHL", "PRT  PIT  PT",
     "PE  PP", "PSV  PSE  PV"),
    ("PD", ("Áp suất vi phân", "Pressure, Differential"),
     "PDRC  PDIC  PDC  PDCV", "PDR  PDI", "PDSH  PDSL",
     "PDRT  PDIT  PDT", "PE  PP", "PDV"),
    ("Q", ("Lượng", "Quantity"), "QRC  QIC", "QR  QI", "QSH  QSL  QSHL",
     "QRT  QIT  QT", "QE", "QZ"),
    ("S", ("Tốc độ / tần số", "Speed / Frequency"), "SRC  SIC  SC  SCV",
     "SR  SI", "SSH  SSL  SSHL", "SRT  SIT  ST", "SE", "SV"),
    ("T", ("Nhiệt độ", "Temperature"), "TRC  TIC  TC  TCV", "TR  TI",
     "TSH  TSL  TSHL", "TRT  TIT  TT", "TE  TP  TW", "TSE  TV"),
    ("TD", ("Nhiệt độ vi phân", "Temperature, Differential"),
     "TDRC  TDIC  TDC  TDCV", "TDR  TDI", "TDSH  TDSL",
     "TDRT  TDIT  TDT", "TE  TP  TW", "TDV"),
    ("W", ("Khối lượng / lực", "Weight / Force"), "WRC  WIC  WC  WCV",
     "WR  WI", "WSH  WSL  WSHL", "WRT  WIT  WT", "WE", "WZ"),
    ("Y", ("Sự kiện / trạng thái", "Event / State / Presence"),
     "YIC  YC", "YR  YI", "YSH  YSL", "YT", "YE", "YZ"),
    ("Z", ("Vị trí / kích thước", "Position / Dimension"),
     "ZRC  ZIC  ZC  ZCV", "ZR  ZI", "ZSH  ZSL  ZSHL",
     "ZRT  ZIT  ZT", "ZE", "ZV"),
]

BLOCKS = [
    ("1", ("Cộng", "Summing"), "M = X₁ + X₂ + … + Xₙ",
     "Tín hiệu ra bằng tổng đại số các tín hiệu vào (các ngõ vào có thể mang dấu âm).",
     "The output equals the algebraic sum of the inputs (inputs may be labelled with positive or negative signs)."),
    ("2", ("Trung bình", "Averaging"), "M = (X₁ + X₂ + … + Xₙ)/n",
     "Tín hiệu ra bằng tổng đại số các ngõ vào chia cho số ngõ vào.",
     "The output equals the algebraic sum of the inputs divided by the number of inputs."),
    ("3", ("Hiệu", "Difference"), "M = X₁ − X₂",
     "Tín hiệu ra bằng hiệu đại số của hai ngõ vào.",
     "The output equals the algebraic difference of the two inputs."),
    ("4", ("Tỷ lệ", "Proportional"), "M = KX",
     "Tín hiệu ra tỷ lệ thuận trực tiếp với ngõ vào. Với bộ khuếch đại thể tích, «K» được thay bằng 1:1; với hệ số khuếch đại nguyên 2:1, 3:1… có thể thay K bằng con số tương ứng.",
     "The output is directly proportional to the input. For a volume booster, «K» is replaced by 1:1; for integral gains 2:1, 3:1 etc. the number may be substituted for K."),
    ("5", ("Tích phân", "Integral"), "M = (1/Tᵢ) ∫ X dt",
     "Tín hiệu ra thay đổi theo cả độ lớn và thời gian duy trì của ngõ vào; tỷ lệ với tích phân theo thời gian của ngõ vào.",
     "The output varies with both the magnitude and the duration of the input; it is proportional to the time integral of the input."),
    ("6", ("Vi phân", "Derivative"), "M = Tᴅ · dX/dt",
     "Tín hiệu ra tỷ lệ với tốc độ thay đổi (đạo hàm) của ngõ vào.",
     "The output is proportional to the rate of change (derivative) of the input."),
]


def note_terms(lang):
    return note(T(
        "<b>Thuật ngữ chính của chương.</b> <em>Bảng 2</em> — tổ hợp chữ điển hình, không có "
        "tính liệt kê đầy đủ. · <em>Bảng 3 / SAMA</em> — ký hiệu khối chức năng mượn từ "
        "phương pháp sơ đồ chức năng của Scientific Apparatus Makers Association. · "
        "<em>Khối độc lập</em> — khối chức năng đứng riêng trên sơ đồ khái niệm. · "
        "<em>Cờ chức năng</em> — khối nhỏ gắn cạnh vòng tròn ký hiệu trên bản vẽ chi tiết.",
        "<b>Key terms.</b> <em>Table 2</em> — typical letter combinations, explicitly not "
        "all-inclusive. · <em>Table 3 / SAMA</em> — function-block designators adapted from "
        "the Scientific Apparatus Makers Association method of functional diagramming. · "
        "<em>Stand-alone block</em> — a function block on a conceptual diagram. · "
        "<em>Function flag</em> — a small block attached to a bubble on a detailed drawing.",
        lang))


def _build(lang):
    b = []
    A = lambda vi, en: T(vi, en, lang)  # noqa: E731

    b.append(lead(A(
        "Hai bảng cuối của điều 5 chuyển từ <em>chữ cái riêng lẻ</em> sang <em>cách ghép "
        "chữ</em> và <em>khối chức năng</em>. Bảng 2 giúp chọn tổ hợp chữ được chấp nhận; "
        "Bảng 3 mượn phương pháp SAMA để mô tả phép tính và logic bằng ký hiệu hộp.",
        "The last two tables of clause 5 move from <em>individual letters</em> to "
        "<em>combinations</em> and <em>function blocks</em>. Table 2 helps in choosing "
        "acceptable letter combinations; Table 3 adapts the SAMA method to depict "
        "calculations and logic with boxed designators.")))

    b.append(h2(A("5.3 · Bảng 2 — Tổ hợp chữ điển hình", "5.3 · Table 2 — Typical letter combinations"),
                A("Bảng tra cứu tổ hợp", "A combination lookup table")))
    b.append(p(A(
        "Tiêu chuẩn nhấn rõ: bảng này <b>không liệt kê đầy đủ</b>. Chữ <b>A</b> (báo động, "
        "thiết bị báo hiệu) có thể dùng theo cùng cách với <b>S</b> (công tắc, thiết bị tác "
        "động); các chữ <b>H</b> và <b>L</b> có thể bỏ trong trường hợp không xác định. Bảng "
        "cũng nêu thêm các tổ hợp khác: FO (lỗ tiết lưu), PFR (tỷ lệ), FRK và HIK (trạm điều "
        "khiển), KQI (đồng hồ thời gian chạy), FX (phụ kiện), QQI (bộ đếm chỉ thị), TJR (máy "
        "ghi quét), WKIC (bộ điều khiển tốc độ giảm khối lượng), LLH (đèn báo), HMS (công tắc "
        "tức thời bằng tay).",
        "The standard states explicitly that the table is <b>not all-inclusive</b>. Letter "
        "<b>A</b> (alarm, the annunciating device) may be used in the same fashion as "
        "<b>S</b> (switch, the actuating device); letters <b>H</b> and <b>L</b> may be "
        "omitted in the undefined case. Other listed combinations include FO (restriction "
        "orifice), PFR (ratio), FRK and HIK (control stations), KQI (running-time indicator), "
        "FX (accessories), QQI (indicating counter), TJR (scanning recorder), WKIC "
        "(rate-of-weight-loss controller), LLH (pilot light) and HMS (hand momentary "
        "switch).")))
    rows = []
    for letter, var, ctrl, readout, sw, tx, prim, final in COMBOS:
        rows.append([letter, var[0] if lang == "vi" else var[1],
                     ctrl, readout, sw, tx, prim, final])
    b.append(table(
        [A("Chữ đầu", "First-letter"), A("Biến đo / khởi tạo", "Measured / initiating variable"),
         A("Bộ điều khiển", "Controllers"), A("Thiết bị đọc", "Readout devices"),
         A("Công tắc & báo động", "Switches & alarms"), A("Bộ truyền", "Transmitters"),
         A("Phần tử sơ cấp", "Primary element"), A("Phần tử cuối", "Final element")],
        rows,
        A("Bảng 2 (trích các dòng dùng nhiều nhất). Ký hiệu giữ nguyên dạng viết hoa của tiêu "
          "chuẩn; dấu «—» thay cho ô trống.",
          "Table 2 (abridged to the most-used rows). Designations keep the standard's "
          "uppercase form; «—» replaces an empty cell.")))
    b.append(note(A(
        "<b>Đọc một ô.</b> Ở dòng <b>F</b>, cột bộ điều khiển có <b>FRC</b> (ghi + điều "
        "khiển), <b>FIC</b> (chỉ thị + điều khiển), <b>FC</b> (điều khiển «mù»), <b>FCV</b> "
        "(van tự lực); cột công tắc/báo động có <b>FSH</b> (cao), <b>FSL</b> (thấp), "
        "<b>FSHL</b> (cả hai); cột bộ truyền có <b>FT</b>, <b>FIT</b>, <b>FRT</b>; cột phần "
        "tử sơ cấp có <b>FE</b> (phần tử sơ cấp), <b>FP</b> (điểm thử), <b>FG</b> (kính "
        "quan sát); phần tử cuối là <b>FV</b>.",
        "<b>Reading one row.</b> In row <b>F</b>, controllers include <b>FRC</b> "
        "(recording + control), <b>FIC</b> (indicating + control), <b>FC</b> (blind) and "
        "<b>FCV</b> (self-actuated valve); switches/alarms include <b>FSH</b> (high), "
        "<b>FSL</b> (low), <b>FSHL</b> (both); transmitters include <b>FT</b>, <b>FIT</b>, "
        "<b>FRT</b>; primary elements <b>FE</b>, test point <b>FP</b>, viewing device "
        "<b>FG</b>; the final element is <b>FV</b>.")))

    b.append(h2(A("5.4 · Bảng 3 — Khối chức năng", "5.4 · Table 3 — Function blocks"),
                A("Phương pháp SAMA", "The SAMA method")))
    b.append(p(A(
        "Bảng 3 là bản chuyển thể phương pháp sơ đồ chức năng của SAMA (Scientific Apparatus "
        "Makers Association). Có hai cách dùng cơ bản: làm <b>khối chức năng độc lập</b> trên "
        "sơ đồ khái niệm, hoặc làm <b>cờ</b> gắn cạnh vòng tròn ký hiệu để chỉ chức năng "
        "trên bản vẽ chi tiết hơn. Cách thứ ba là kết hợp cả hai — điển hình ở hệ thống điều "
        "khiển dùng chung, khi đường tín hiệu biến đo đi vào một khối căn bậc hai vẽ ngay cạnh "
        "bộ điều khiển dùng chung.",
        "Table 3 adapts the SAMA (Scientific Apparatus Makers Association) method of "
        "functional diagramming. It has two basic uses: as <b>stand-alone function blocks</b> "
        "on conceptual diagrams, or as <b>flags</b> designating functions performed by "
        "bubbles on more detailed drawings. A third use combines the two in shared-control "
        "systems — for instance, where the measured-variable signal line enters a square-root "
        "function block drawn adjacent to a shared controller.")))
    b.append(p(A(
        "Tiêu chuẩn cố ý bỏ hai ký hiệu SAMA: <em>Transfer</em> (chuyển giao) và <em>Analog "
        "Signal Generator</em> (bộ phát tín hiệu tương tự). Vì cách dùng ISA-5.1 thường đòi "
        "hỏi ký hiệu phải có nhận dạng đi kèm, nên nên dùng vòng tròn <b>HIC</b> (trạm nạp "
        "tay) cho bộ phát tín hiệu tương tự, và <b>HS</b> (công tắc tay) — có hoặc không kèm "
        "vòng tròn relay — cho chức năng chuyển giao. Dùng hộp giúp tách ký hiệu khỏi các nét "
        "vẽ khác trên sơ đồ.",
        "Two SAMA symbols are deliberately omitted: <em>Transfer</em> and the <em>Analog "
        "Signal Generator</em>. Because ISA-5.1 symbolism usually requires identification to "
        "be associated with a symbol, the <b>HIC</b> (manual loader) bubble is recommended "
        "for an analog signal generator and an <b>HS</b> (hand switch), with or without a "
        "relay bubble, for a transfer function. A box sets the designator off from other "
        "markings on the diagram.")))

    b.append(fig(1, F.fig_sama_blocks()))
    b.append(p(A(
        "Sáu khối đầu tiên của Bảng 3 — cộng, trung bình, hiệu, tỷ lệ, tích phân, vi phân — "
        "được vẽ lại ở Hình 2 kèm biểu thức toán học. Bốn tờ tiếp theo của Bảng 3 trong tiêu "
        "chuẩn (trang 23–26) được tái tạo nguyên vẹn bên dưới dưới dạng vector; trong bản "
        "gốc chúng được in xoay 90°, ở đây đã được xoay lại cho dễ đọc.",
        "The first six blocks of Table 3 — summing, averaging, difference, proportional, "
        "integral and derivative — are redrawn in Figure 2 with their equations. The "
        "standard's four Table 3 sheets (pages 23–26) are reproduced in full as vectors "
        "below; the originals are printed rotated 90° and have been turned upright here.")))
    b.append(table(
        [A("STT", "No."), A("Chức năng", "Function"),
         A("Biểu thức", "Math equation"), A("Định nghĩa", "Definition")],
        [[n, name[0] if lang == "vi" else name[1], f,
          dvi if lang == "vi" else den]
         for n, name, f, dvi, den in BLOCKS],
        A("Sáu khối chức năng đầu tiên của Bảng 3, theo đúng thứ tự và định nghĩa của tiêu chuẩn.",
          "The first six function blocks of Table 3, in the standard's order and wording.")))

    for i, pg in enumerate((23, 24, 25, 26), start=2):
        b.append(fig(i, F.sheet(pg)))

    b.append(h2(A("Ghi nhớ khi dùng khối chức năng", "Using function blocks well"),
                A("Ba lưu ý thực hành", "Three practical cautions")))
    b.append(ul([
        A("Các ký hiệu chức năng gắn với bộ điều khiển, thiết bị tính toán, bộ chuyển đổi và "
          "relay có thể dùng <em>riêng lẻ hoặc kết hợp</em> (xem Bảng 1, chú thích 14).",
          "Function designators associated with controllers, computing devices, converters "
          "and relays may be used <em>individually or in combination</em> (see Table 1, note 14)."),
        A("Ký hiệu khối chức năng và số thẻ <b>luôn vẽ nằm ngang</b>, dù toàn bộ sơ đồ có "
          "thể xoay theo hướng khác (điều 4.4.6).",
          "Function-block designators and tag numbers are <b>always drawn horizontally</b>, "
          "even when the rest of the diagram is oriented differently (clause 4.4.6)."),
        A("Bảng 3 chỉ là công cụ biểu diễn <em>chức năng</em>; phần cứng thực tế (relay phụ, "
          "biến dòng…) có thể bị bỏ qua trên sơ đồ dòng kỹ thuật theo điều 4.4.11.",
          "Table 3 depicts <em>function</em> only; actual interlock hardware (auxiliary "
          "relays, current transformers…) may be omitted from engineering flow diagrams "
          "under clause 4.4.11."),
    ]))
    return "".join(b)


def body_vi():
    return _build("vi")


def body_en():
    return _build("en")
