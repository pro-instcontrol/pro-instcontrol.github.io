# -*- coding: utf-8 -*-
"""Tables 8.5 and 8.6 from McMillan Chapter 8.

Transcribed from the authoritative page renders:
  - printed p.198 / PDF p.219 -> Table 8.5
  - printed p.199 / PDF p.220 -> Table 8.6

Printed quirks are preserved deliberately, not silently corrected:

  * Table 8.5 source line reads ``(from BS/EN 50014¹)`` on p219.png. The PDF
    text layer garbled this as ``(from BSEN 50024l)``; the brief and task
    note carried that OCR form forward as ``BSEN 50024¹``. The page image is
    authoritative (brief section 6 / section 10), so the printed standard
    number is transcribed here and the discrepancy is flagged, not hidden.
  * Table 8.5 note uses the printed word "extrapolated" (not "extended").
  * Table 8.6 has no printed note, so NOTE86_EN/NOTE86_VI are empty and the
    writer should emit no note after that table.
  * Degree signs, superscript and multiplication signs are literal Unicode.
"""

# ---------------------------------------------------------------------------
# Table 8.5 - Test Torque to be applied to bushings
# ---------------------------------------------------------------------------

HEAD85_EN = [
    "Diameter of the stem of the bushing<br>(metric thread size)",
    "Torque<br>Newton metres",
]

HEAD85_VI = [
    "Đường kính thân của bạc cách điện<br>(kích cỡ ren hệ mét)",
    "Mô-men xoắn<br>Newton mét",
]

# One 2-cell row per printed stem diameter, in printed order M4 -> M24.
# Verified against p219.png; the torque column is headed "Newton metres".
ROWS85 = [
    ["M4", "2.0"],
    ["M5", "3.2"],
    ["M6", "5.0"],
    ["M8", "10.0"],
    ["M10", "16.0"],
    ["M12", "25.0"],
    ["M16", "50.0"],
    ["M20", "85.0"],
    ["M24", "130.0"],
]

CAPTION85_EN = "Test Torque to be applied to bushings used for connection facilities"

CAPTION85_VI = (
    "Mô-men xoắn thử nghiệm cần áp dụng cho các bạc cách điện dùng cho "
    "thiết bị kết nối"
)

NOTE85_EN = (
    "<p>(from BS/EN 50014¹)</p>"
    "<p>Note: Torque values for sizes other than those specified above may "
    "be determined from a graph plotted using these values. In addition, "
    "the graph may be extrapolated to allow torque values to be determined "
    "for bushings larger than those specified.</p>"
)

NOTE85_VI = (
    "<p>(theo BS/EN 50014¹)</p>"
    "<p>Ghi chú: Các giá trị mô-men xoắn cho các kích cỡ khác với các kích cỡ "
    "nêu trên có thể được xác định từ một đồ thị được vẽ dựa trên các giá trị "
    "này. Ngoài ra, có thể ngoại suy đồ thị để xác định các giá trị mô-men "
    "xoắn cho các bạc cách điện lớn hơn các kích cỡ đã nêu.</p>"
)

# ---------------------------------------------------------------------------
# Table 8.6 - Minimum cross-sectional area of protective conductor
# ---------------------------------------------------------------------------

HEAD86_EN = [
    "Cross-sectional area of phase conductors of the installation<br>(mm²)",
    "Minimum cross-sectional area of corresponding protective conductor<br>(mm²)",
]

HEAD86_VI = [
    "Tiết diện của dây dẫn pha của lắp đặt<br>(mm²)",
    "Tiết diện nhỏ nhất của dây dẫn bảo vệ tương ứng<br>(mm²)",
]

# Verified against p220.png. The printed third row uses a multiplication
# sign before "phase conductor" (the text layer read it as a plain "x").
ROWS86 = [
    ["up to 16", "16"],
    ["16 to 35", "16"],
    ["over 35", "0.5 × phase conductor"],
]

CAPTION86_EN = "Minimum cross-sectional area of protective conductor"

CAPTION86_VI = "Tiết diện nhỏ nhất của dây dẫn bảo vệ"

# No source line and no note are printed beneath Table 8.6 on p220.png.
NOTE86_EN = ""

NOTE86_VI = ""
