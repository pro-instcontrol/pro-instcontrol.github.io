# -*- coding: utf-8 -*-
"""Tables 14.6 and 14.7 of McMillan Chapter 14, bilingual EN/VI.

Both tables are printed on printed p. 449 (PDF p. 470). Transcribed from the
authoritative render work/mcmillan_ch14_pages/p470.png and cross-checked
against work/mcmillan_ch14_survey_c.md §4.

The OCR text layer garbles the plus/minus sign in Table 14.6 (as an
ampersand, an asterisk or 'k' in place of '+/-'); the render confirms '±'
in all three rows.

Structure follows mcmillan_tbl13_1_4.py: HEAD is one cell per column, ROWS is
a list of equal-length cell lists, and CAPTION and NOTE are localized. The
two-tier header of Table 14.7 is carried inside five flat HEAD cells with
line breaks, so HEAD147 and every row of ROWS147 still have five columns.

Both printed tables contain English connector words (14.6) or carry genuine
language-specific row lists by contract (14.7), so each table exports its own
ROWS14N_EN and ROWS14N_VI lists; the Vietnamese body must use the _VI rows.

Neither printed table has a footnote or a source line, so both NOTE pairs are
empty strings.
"""

# ---------------------------------------------------------------------------
# Table 14.6 — printed p. 449 (PDF p. 470)
# ---------------------------------------------------------------------------

HEAD146_EN = [
    "Sub-group",
    "Test gas",
]
HEAD146_VI = [
    "Phân nhóm",
    "Khí thử",
]

ROWS146 = [
    ["IIA", "5.25 ± 0.25% propane in air"],
    ["IIB", "7.8 ± 0.5% ethylene in air"],
    ["IIC", "21 ± 2% hydrogen in air"],
]
ROWS146_EN = [
    ["IIA", "5.25 ± 0.25% propane in air"],
    ["IIB", "7.8 ± 0.5% ethylene in air"],
    ["IIC", "21 ± 2% hydrogen in air"],
]
ROWS146_VI = [
    ["IIA", "5.25 ± 0.25% propan trong không khí"],
    ["IIB", "7.8 ± 0.5% ethylen trong không khí"],
    ["IIC", "21 ± 2% hydro trong không khí"],
]

CAPTION146_EN = "Table 14.6 Test gases for non-incendive sparking"
CAPTION146_VI = "Bảng 14.6 Khí thử cho tia lửa không gây cháy"

NOTE146_EN = ""
NOTE146_VI = ""

# ---------------------------------------------------------------------------
# Table 14.7 — printed p. 449 (PDF p. 470)
# ---------------------------------------------------------------------------

# Flat five-column header: each spanning tier is carried by line breaks.
HEAD147_EN = [
    "Sub-group",
    "Inductive circuits<br>Cadmium disc<br>(mA)",
    "Inductive circuits<br>Other disc<br>(mA)",
    "Resistive circuits<br>Cadmium disc<br>(A)",
    "Resistive circuits<br>Other disc<br>(A)",
]
HEAD147_VI = [
    "Phân nhóm",
    "Mạch cảm ứng<br>Đĩa cadmi<br>(mA)",
    "Mạch cảm ứng<br>Đĩa khác<br>(mA)",
    "Mạch điện trở<br>Đĩa cadmi<br>(A)",
    "Mạch điện trở<br>Đĩa khác<br>(A)",
]

ROWS147 = [
    ["IIA", "100", "125", "1.0", "2.75"],
    ["IIB", "65", "100", "0.7", "2.0"],
    ["IIC", "30", "52", "0.3", "1.65"],
]
ROWS147_EN = [
    ["IIA", "100", "125", "1.0", "2.75"],
    ["IIB", "65", "100", "0.7", "2.0"],
    ["IIC", "30", "52", "0.3", "1.65"],
]
ROWS147_VI = [
    ["IIA", "100", "125", "1.0", "2.75"],
    ["IIB", "65", "100", "0.7", "2.0"],
    ["IIC", "30", "52", "0.3", "1.65"],
]

CAPTION147_EN = "Table 14.7 Calibration currents for spark test apparatus"
CAPTION147_VI = "Bảng 14.7 Dòng điện hiệu chuẩn cho thiết bị thử tia lửa"

NOTE147_EN = ""
NOTE147_VI = ""
