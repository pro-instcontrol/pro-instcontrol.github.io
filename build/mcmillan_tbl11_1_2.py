# -*- coding: utf-8 -*-
"""Tables 11.1 and 11.2 of McMillan Chapter 11, bilingual EN/VI.

Transcribed from the authoritative page renders:
  - PDF p.299 / printed p.278 -> Table 11.1 + its 7 footnotes + Note
  - PDF p.313 / printed p.292 -> Table 11.2 + its source note

Cross-checked against work/ch11_survey_a.md, work/ch11_survey_c.md and
work/mcmillan_ch11_brief.md. PDF p.300 was also inspected: it carries the
body text following the table, no table. PDF p.315 and p.316 were inspected
while locating Table 11.2; the table is on p.313, not on those pages.

Structure follows mcmillan_common.table(): HEAD is one cell per column,
ROWS is a list of equal-length cell lists, CAPTION and NOTE are localized.
Full-width centred/spanning lines that precede the printed columns are
carried as a second line of CAPTION, after the printed caption text, as in
mcmillan_tbl10_1_5.py and mcmillan_tbl91_93.py.

Unlike the Chapter 10 suppliers, BOTH tables here contain English connector
words in their rows (11.1 row labels; 11.2 every data cell), so language-
specific row lists are exported in addition to the required ROWS11N:
ROWS11N_EN mirrors the printed rows and ROWS11N_VI carries the Vietnamese
row labels/cells. Prose callers must pass the matching language list.

Printed quirks retained deliberately (with bilingual translator notes):

  * 11.1 tier-1 over-header 'Type of pressurization' spans six columns;
    tier-2 prints 'Leakage' / 'Compensation' and 'Continuous' / 'Dilution'
    on two lines; tier-3 prints 'Inert²' with a superscript 2;
  * 11.1 first row label prints '(note 1)' in parentheses on its own line,
    while its cell prints 'N¹' with a superscript 1;
  * 11.1 body cells carry superscript footnote markers ¹ ³ ⁴ ⁵ ⁶ ⁷; the OCR
    text layer merged them into plain digits or apostrophes;
  * 11.1 footnotes print '%' with no space where the prose spells out
    'per cent'; the printed Note reads 'may be treated as though'
    although work/ch11_survey_a.md and the brief transcribed 'may be heated';
  * 11.2 over-header 'Necessity for spark/particle barrier' spans the two
    right-hand columns; source note prints '(from BS/EN 50016)' in italics,
    not '50026' as the OCR text layer read it.
"""

# ---------------------------------------------------------------------------
# Table 11.1 — printed p.278 (PDF p.299)
# ---------------------------------------------------------------------------

CAPTION111_EN = (
    "Table 11.1 Type of pressurization vs release conditions"
    "<br>Type of pressurization"
)
CAPTION111_VI = (
    "Bảng 11.1 Kiểu cấp áp so với điều kiện phát thải"
    "<br>Kiểu cấp áp"
)

HEAD111_EN = [
    "Release conditions",
    "Static<br>Air",
    "Static<br>Inert²",
    "Leakage<br>Compensation<br>Air",
    "Leakage<br>Compensation<br>Inert²",
    "Continuous<br>Dilution<br>Air",
    "Continuous<br>Dilution<br>Inert²",
]
HEAD111_VI = [
    "Điều kiện phát thải",
    "Tĩnh<br>Không khí",
    "Tĩnh<br>Khí trơ²",
    "Bù rò rỉ<br>Không khí",
    "Bù rò rỉ<br>Khí trơ²",
    "Pha loãng liên tục<br>Không khí",
    "Pha loãng liên tục<br>Khí trơ²",
]

# 7 cells per row: release condition + 6 pressurization values.
ROWS111 = [
    ["No release of flammable material (note 1)",
     "N¹", "Y", "Y", "Y", "Y", "Y"],
    ["Deliberate release of flammable material",
     "N¹", "N³", "N⁴", "N⁴", "Y⁶", "N⁴"],
    ["Limited release of flammable material in fault condition",
     "N¹", "N³", "N⁵", "Y⁷", "Y⁶", "Y⁷"],
    ["Unlimited release of flammable material in fault conditions",
     "N¹", "N³", "N⁵", "Y⁷", "N⁵", "Y⁷"],
]
ROWS111_EN = ROWS111
ROWS111_VI = [
    ["Không phát thải vật liệu dễ cháy (ghi chú 1)",
     "N¹", "Y", "Y", "Y", "Y", "Y"],
    ["Phát thải vật liệu dễ cháy có chủ đích",
     "N¹", "N³", "N⁴", "N⁴", "Y⁶", "N⁴"],
    ["Phát thải hạn chế vật liệu dễ cháy trong điều kiện sự cố",
     "N¹", "N³", "N⁵", "Y⁷", "Y⁶", "Y⁷"],
    ["Phát thải không hạn chế vật liệu dễ cháy trong các điều kiện sự cố",
     "N¹", "N³", "N⁵", "Y⁷", "N⁵", "Y⁷"],
]

NOTE111_EN = (
    "<p>1 Static pressurization with air is not permitted by BS/EN 50016.</p>"
    "<p>2 Inert gas must contain less than 1% oxygen</p>"
    "<p>3 Static pressurization cannot be used where there is any release of "
    "flammable material either deliberate or in fault conditions</p>"
    "<p>4 Pressurization with leakage compensation cannot be used with "
    "either air or inert gas when the release is deliberate. Pressurization "
    "with dilution must use air in these circumstances</p>"
    "<p>5 Pressurization with leakage compensation using air is not "
    "permitted where there is either a limited or an unlimited release in "
    "fault conditions. Pressurization with dilution using air is not "
    "permitted where the release is unlimited</p>"
    "<p>6 When dilution with air is used the airflow must be sufficient to "
    "dilute the flammable gas concentration to less than 25% of its lower "
    "explosive limit in all but the dilution area of the enclosure, whether "
    "the release is a limited release in fault conditions or a specified "
    "normal release.</p>"
    "<p>7 The protective gas in the enclosure must be such that the oxygen "
    "concentration is less than 2% by volume and the use of inert gas is not "
    "permitted when the flammable material has an upper explosive limit "
    "(UEL) of more than 80%</p>"
    "<p>Note: In cases where the flammable material is contained in an "
    "infallible containment the enclosure may be treated as though it does "
    "not contain a flammable material.</p>"
    "<p>Translator note: the printed tier-1 over-header 'Type of "
    "pressurization' spans the six right-hand columns and is carried in the "
    "caption (second line) so the flat HEAD/ROWS shape stays intact; tier 2 "
    "prints 'Leakage' / 'Compensation' and 'Continuous' / 'Dilution' on two "
    "lines, reproduced with line breaks.</p>"
    "<p>Translator note: the first row label prints '(note 1)' in "
    "parentheses on its own line, not as a superscript, while its cell "
    "prints 'N¹'. The header 'Inert²' and the body markers ¹ ³ ⁴ ⁵ ⁶ ⁷ are "
    "printed as superscripts; the OCR text layer merged them into plain "
    "digits or apostrophes.</p>"
    "<p>Translator note: the table and its footnotes print '%' (1%, 25%, "
    "2%, 80%) where the surrounding prose spells out 'per cent'; the "
    "distinction is preserved.</p>"
    "<p>Translator note: the printed Note reads 'may be treated as though'; "
    "work/ch11_survey_a.md and the brief transcribed 'may be heated'. The "
    "page image governs and the printed word is retained.</p>"
)

NOTE111_VI = (
    "<p>1 Áp lực tĩnh bằng không khí không được phép theo BS/EN 50016.</p>"
    "<p>2 Khí trơ phải chứa ít hơn 1% oxy</p>"
    "<p>3 Không thể dùng áp lực tĩnh khi có bất kỳ sự phát thải vật liệu dễ "
    "cháy nào, dù là có chủ đích hay trong điều kiện sự cố</p>"
    "<p>4 Không thể dùng cấp áp với bù rò rỉ bằng cả không khí lẫn khí trơ "
    "khi việc phát thải là có chủ đích. Trong những trường hợp này, cấp áp "
    "bằng pha loãng phải dùng không khí</p>"
    "<p>5 Không cho phép dùng cấp áp với bù rò rỉ bằng không khí khi có sự "
    "phát thải hạn chế hoặc không hạn chế trong điều kiện sự cố. Không cho "
    "phép dùng cấp áp bằng pha loãng với không khí khi sự phát thải là không "
    "hạn chế</p>"
    "<p>6 Khi dùng pha loãng bằng không khí, lưu lượng khí phải đủ để pha "
    "loãng nồng độ khí dễ cháy xuống dưới 25% giới hạn cháy thấp hơn ở mọi "
    "nơi trong vỏ bọc, trừ vùng pha loãng, dù sự phát thải là phát thải hạn "
    "chế trong điều kiện sự cố hay phát thải bình thường đã được quy định.</p>"
    "<p>7 Khí bảo vệ trong vỏ bọc phải có nồng độ oxy nhỏ hơn 2% theo thể "
    "tích và không được phép dùng khí trơ khi vật liệu dễ cháy có giới hạn "
    "cháy cao hơn (UEL) lớn hơn 80%</p>"
    "<p>Ghi chú: Trong trường hợp vật liệu dễ cháy được chứa trong một vùng "
    "chứa không thể hỏng, có thể coi vỏ bọc như thể nó không chứa vật liệu "
    "dễ cháy.</p>"
    "<p>Ghi chú của người dịch: tiêu đề tầng trên cùng in 'Type of "
    "pressurization' trải rộng trên sáu cột bên phải được đưa vào dòng thứ "
    "hai của CAPTION để giữ cấu trúc HEAD/ROWS dạng phẳng; tầng hai in "
    "'Leakage' / 'Compensation' và 'Continuous' / 'Dilution' trên hai dòng, "
    "được giữ bằng ngắt dòng.</p>"
    "<p>Ghi chú của người dịch: nhãn hàng đầu tiên in '(note 1)' trong "
    "ngoặc đơn trên một dòng riêng, không phải chỉ số trên, trong khi ô "
    "của nó in 'N¹'. Tiêu đề 'Inert²' và các chỉ số trên ¹ ³ ⁴ ⁵ ⁶ ⁷ trong "
    "bảng được in dạng chỉ số trên; lớp văn bản OCR gộp chúng thành chữ số "
    "hoặc dấu nháy thường.</p>"
    "<p>Ghi chú của người dịch: bảng và các ghi chú in dấu '%' (1%, 25%, "
    "2%, 80%), trong khi văn bản prose viết 'per cent'; giữ nguyên sự "
    "khác biệt này.</p>"
    "<p>Ghi chú của người dịch: dòng Ghi chú in 'may be treated as though'; "
    "work/ch11_survey_a.md và bản tóm tắt chép là 'may be heated'. Ảnh "
    "trang in là nguồn quyết định và được giữ nguyên.</p>"
)

# ---------------------------------------------------------------------------
# Table 11.2 — printed p.292 (PDF p.313)
# ---------------------------------------------------------------------------

CAPTION112_EN = (
    "Table 11.2 Requirements for spark and particle barriers"
    "<br>Necessity for spark/particle barrier"
)
CAPTION112_VI = (
    "Bảng 11.2 Yêu cầu đối với rào chắn tia lửa và hạt"
    "<br>Sự cần thiết của rào chắn tia lửa/hạt"
)

HEAD112_EN = [
    "Zone into which purge gas exhausts",
    "Apparatus sparks in normal operation",
    "Apparatus does not spark in normal operation",
]
HEAD112_VI = [
    "Vùng mà khí thổi sạch xả vào",
    "Thiết bị phát tia lửa trong điều kiện vận hành bình thường",
    "Thiết bị không phát tia lửa trong điều kiện vận hành bình thường",
]

# 3 cells per row: exhaust zone plus the two apparatus conditions.
ROWS112 = [
    ["Zone 0", "Exhaust not permitted", "Exhaust not permitted"],
    ["Zone 1", "Barrier required", "Barrier required"],
    ["Zone 2", "Barrier required", "Barrier not required"],
    ["Non-hazardous", "Barrier not required", "Barrier not required"],
]
ROWS112_EN = ROWS112
ROWS112_VI = [
    ["Vùng 0", "Không cho phép xả thải", "Không cho phép xả thải"],
    ["Vùng 1", "Cần rào chắn", "Cần rào chắn"],
    ["Vùng 2", "Cần rào chắn", "Không cần rào chắn"],
    ["Không nguy hiểm", "Không cần rào chắn", "Không cần rào chắn"],
]

NOTE112_EN = (
    "<p>(from BS/EN 50016)</p>"
    "<p>Translator note: the printed over-header 'Necessity for "
    "spark/particle barrier' spans the two right-hand columns and is "
    "carried in the caption (second line) so the flat HEAD/ROWS shape "
    "stays intact. The slash in 'spark/particle' and the hyphen in "
    "'Non-hazardous' are printed forms and are retained.</p>"
    "<p>Translator note: the source note prints '(from BS/EN 50016)' in "
    "italics; the OCR text layer read '50026'. Retained as printed.</p>"
)

NOTE112_VI = (
    "<p>(theo BS/EN 50016)</p>"
    "<p>Ghi chú của người dịch: tiêu đề phía trên in 'Necessity for "
    "spark/particle barrier' trải rộng trên hai cột bên phải được đưa vào "
    "dòng thứ hai của CAPTION để giữ cấu trúc HEAD/ROWS dạng phẳng. Dấu "
    "gạch chéo trong 'spark/particle' và dấu gạch nối trong 'Non-hazardous' "
    "là dạng in và được giữ nguyên.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn in '(from BS/EN 50016)' dạng "
    "nghiêng; lớp văn bản OCR đọc là '50026'. Giữ nguyên theo bản in.</p>"
)
