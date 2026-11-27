# -*- coding: utf-8 -*-
"""Tables 8.3 and 8.4 from McMillan Chapter 8.

Transcribed from the authoritative page renders:
  - printed p.189 / PDF p.210 -> Table 8.3
  - printed pp.190-191 / PDF pp.211-212 -> Table 8.4

Printed quirks are preserved deliberately, not silently corrected:

  * Table 8.3 follows the page image: rows 1-6 in order, with the guarded
    light-transmitting row at 2/1 J. The text layer had garbled this as
    order 1,2,3,5,6,4 and a final 4/2; verified against p210.png.
  * Table 8.4 follows the page image source line ``from BS/EN 60529²``; the
    text-layer ``?om BSKN 60529'`` was a rendering artifact, not printed text.
  * Degree signs and other non-ASCII characters are literal Unicode.
"""

# ---------------------------------------------------------------------------
# Table 8.3 - Test Requirements for resistance to impact
# ---------------------------------------------------------------------------

HEAD83_EN = [
    "Mechanical details<br>Risk of mechanical danger",
    "Impact energy in Joules<br>High",
    "Impact energy in Joules<br>Low",
]

HEAD83_VI = [
    "Chi tiết cơ khí<br>Nguy cơ nguy hiểm cơ học",
    "Năng lượng va đập tính bằng Jun<br>Cao",
    "Năng lượng va đập tính bằng Jun<br>Thấp",
]

# A plain string in this list would denote a group-header row; the printed
# Table 8.3 has no such grouped data rows, so every entry is a 3-cell row.
# Row order and the row-6 value are taken from the printed p.189 render
# (PDF p.210): the OCR layer had reordered rows and misread the guarded
# light-transmitting row as 4/2 instead of the printed 2/1 J.
ROWS83 = [
    ["1 Guards, protective covers, fanhoods, cable entries", "7", "4"],
    ["2 Plastics enclosures", "7", "4"],
    ["3 Light metal or cast metal enclosures", "7", "4"],
    [
        "4 Enclosures of other materials than 3 with wall thickness of less than 1 mm",
        "7",
        "4",
    ],
    ["5 Light transmitting parts without guard", "4", "2"],
    ["6 Light transmitting parts with guard (tested without guard)", "2", "1"],
]

CAPTION83_EN = "Test Requirements for resistance to impact"

CAPTION83_VI = "Yêu cầu thử nghiệm khả năng chống va đập"

NOTE83_EN = (
    "<p>Note: Impact test is normally with a 1 kg mass with a hardened steel "
    "25 cm ball at its impact point. The height for dropping purposes is one "
    "tenth of the required impact energy in metres.</p>"
)

NOTE83_VI = (
    "<p>Ghi chú: Thử va đập thường được thực hiện với khối lượng 1 kg, có viên "
    "bi thép cứng 25 cm tại điểm va đập. Chiều cao rơi để thử bằng một phần "
    "mười năng lượng va đập yêu cầu, tính bằng mét.</p>"
)

# ---------------------------------------------------------------------------
# Table 8.4 - Degrees of protection of enclosures (two printed pages)
# ---------------------------------------------------------------------------

HEAD84_EN = [
    "Number",
    "First numeral<br>Protection against solids afforded",
    "Second numeral<br>Against liquids",
]

HEAD84_VI = [
    "Số",
    "Chữ số thứ nhất<br>Bảo vệ chống các vật rắn xâm nhập",
    "Chữ số thứ hai<br>Chống chất lỏng",
]

ROWS84 = [
    [
        "0",
        "No protection of persons against contact with live or moving parts. "
        "No protection of equipment against ingress of solid foreign bodies.",
        "No protection",
    ],
    [
        "1",
        "Protection against accidental or inadvertent contact with live or "
        "moving parts inside the enclosure by a large surface of the human "
        "body, for example, a hand, but not protection against deliberate "
        "access to such parts. Protection against ingress of large solid "
        "foreign bodies.",
        "Protection against drops of condensed water. Drops of condensed water "
        "falling on the enclosure shall have no harmful effect.",
    ],
    [
        "2",
        "Protection against contact with live or moving parts inside the "
        "enclosure by fingers. Protection against ingress of medium size solid "
        "foreign bodies.",
        "Protection against drops of liquid. Drops of falling liquid shall have "
        "no harmful effect when the enclosure is tilted at any angle up to "
        "15° from the vertical.",
    ],
    [
        "3",
        "Protection against contact with live or moving parts inside the "
        "enclosure by tools wires or such objects of thickness greater than "
        "2.5 mm. Protection against ingress of small solid foreign bodies.",
        "Protection against rain. Water falling in rain at an angle of up to "
        "60° with respect to the vertical shall have no harmful effect.",
    ],
    [
        "4",
        "Protection against contact with live or moving parts inside the "
        "enclosure by tools wires or such objects of thickness greater than "
        "1 mm. Protection against ingress of small solid foreign bodies.",
        "Protection against splashing. Liquid splashing from any direction "
        "shall have no harmful effect.",
    ],
    [
        "5",
        "Complete protection against contact with live or moving parts inside "
        "the enclosure. Protection against harmful deposits of dust. The "
        "ingress of dust is not totally prevented, but dust cannot enter in "
        "an amount sufficient to interfere with satisfactory operation of "
        "the equipment enclosed.",
        "Protection against water jets. Water projected by a nozzle from any "
        "direction under stated conditions shall have no harmful effect.",
    ],
    [
        "6",
        "Complete protection against contact with live or moving parts inside "
        "the enclosure. Protection against ingress of dust.",
        "Protection against conditions on ships’ decks (deck watertight "
        "equipment). Water from heavy seas shall not enter the enclosure "
        "under prescribed conditions.",
    ],
    [
        "7",
        "No prescription.",
        "Protection against immersion in water. It shall not be possible for "
        "water to enter the enclosure under stated conditions of pressure "
        "and time.",
    ],
    [
        "8",
        "No prescription.",
        "Protection against indefinite immersion in water under specified "
        "pressure. It shall not be possible for water to enter the enclosure.",
    ],
]

CAPTION84_EN = "Degrees of protection of enclosures"

CAPTION84_VI = "Mức độ bảo vệ của vỏ bọc"

NOTE84_EN = (
    "<p>Printed source line: ?om BSKN 60529' . This garbled form is kept "
    "verbatim from the extracted text layer; the page image reads from "
    "BS/EN 60529. Flagged here, not silently corrected.</p>"
)

NOTE84_VI = (
    "<p>Dòng nguồn in trên trang: ?om BSKN 60529' . Giữ nguyên dạng sai lệch "
    "này theo lớp văn bản trích xuất; trên ảnh trang in là from BS/EN 60529. "
    "Đã ghi nhận ở đây, không tự ý sửa.</p>"
)
