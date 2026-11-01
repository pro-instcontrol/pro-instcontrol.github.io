# -*- coding: utf-8 -*-
"""Handbook Chapter 96 — Reading/Recording Devices
(96.1 Graphic Recorders, Herman Vermariën · 96.2 Data Acquisition Systems,
Edward McConnell · 96.3 Magnetic and Optical Recorders, Yufeng Li).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch96.py
"""
import os

import hb96fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch96-reading-recording-devices"
TITLE_EN = "Reading/Recording Devices"
TITLE_VI = "Thiết bị đọc và ghi"
BYLINE = ("Herman Vermariën · Vrije Universiteit Brussel — "
          "Edward McConnell · National Instruments — "
          "Yufeng Li · Samsung Information Systems America")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    return ('<figure class="figure" id="fig-96-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h4(t, en=""):
    return '<h4>%s%s</h4>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def note(t):
    return '<div class="note">%s</div>' % t


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def dt(term, definition):
    return p("<b>%s:</b> %s" % (term, definition))


def table(hd, rows, cap, cls=""):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl%s"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div><p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, "".join("<th>%s</th>" % h for h in hd), body, cap))


# ================================================================ TABLE 96.1

_T1 = [
    ("LR8100", "Test, meas.; 4,6,8 c. ch.; POC; printer; display; memory; analysis; alarm; interface",
     "Thử nghiệm, đo; 4, 6, 8 kênh liên tục; POC; máy in; màn hiển thị; bộ nhớ; phân tích; cảnh báo; giao diện",
     "Yokogawa E. C.", "11.500 (8 ch.)"),
    ("LR102", "Test, meas.; 1,2 c. ch.", "Thử nghiệm, đo; 1, 2 kênh liên tục",
     "Yokogawa E. C.", "1.800 (2 ch.)"),
    ("LR122", "Test, meas.; 1,2 c. ch.; x–y; alarm; interface",
     "Thử nghiệm, đo; 1, 2 kênh liên tục; x–y; cảnh báo; giao diện",
     "Yokogawa E. C.", "2.300 (2 ch.)"),
    ("MC1000", "Test, meas.; 4,6,8,12 c. ch.; POC; printer; waveform display; analysis; alarm; interface",
     "Thử nghiệm, đo; 4, 6, 8, 12 kênh liên tục; POC; máy in; màn hiển thị dạng sóng; phân tích; cảnh báo; giao diện",
     "Graphtec C.", "20.200 (12 ch.)"),
    ("BD112", "Test, meas.; 2 c. ch.; POC", "Thử nghiệm, đo; 2 kênh liên tục; POC",
     "Kipp Z.", "2.700 (2 ch.)"),
    ("BD200", "Test, meas.; 4,6,8 c. ch.; POC; display; x–y; alarm; interface",
     "Thử nghiệm, đo; 4, 6, 8 kênh liên tục; POC; màn hiển thị; x–y; cảnh báo; giao diện",
     "Kipp Z.", "12.200 (8 ch.)"),
    ("L250", "Test, meas.; 1,2 c. ch.; POC", "Thử nghiệm, đo; 1, 2 kênh liên tục; POC",
     "Linseis", "2.000 (2 ch.)"),
    ("L2066", "Test, meas.; 1 to 6 c. ch.; POC; x–y; interface",
     "Thử nghiệm, đo; 1 đến 6 kênh liên tục; POC; x–y; giao diện",
     "Linseis", "8.100 (6 ch.)"),
    ("MCR560", "Test, meas.; 2,4,6 c. ch.", "Thử nghiệm, đo; 2, 4, 6 kênh liên tục",
     "W+W", "3.800 (2 ch.)"),
    ("DCR540", "Test, meas.; 1 to 6 c. ch.; POC; display; x–y; interface",
     "Thử nghiệm, đo; 1 đến 6 kênh liên tục; POC; màn hiển thị; x–y; giao diện",
     "W+W", "6.600 (4 ch.)"),
    ("PCR500SP", "Test, meas.; 2,4,6,8 c. ch.; POC; display; x–y; analysis; alarm; interface; "
     "transient option",
     "Thử nghiệm, đo; 2, 4, 6, 8 kênh liên tục; POC; màn hiển thị; x–y; phân tích; cảnh báo; "
     "giao diện; tuỳ chọn ghi quá độ",
     "W+W", "15.900 (8 ch.)"),
    ("Omega640", "Test, meas.; 1,2,3 c. ch.", "Thử nghiệm, đo; 1, 2, 3 kênh liên tục",
     "Omega", "4.300 (3 ch.)"),
    ("Omega600A", "Test, meas.; 1 to 6 c. ch.; POC; printer; x–y; memory; interface",
     "Thử nghiệm, đo; 1 đến 6 kênh liên tục; POC; máy in; x–y; bộ nhớ; giao diện",
     "Omega", "23.700 (6 ch.)"),
    ("μR1000", "Process mon.; 1,2,3,4 c. ch., 6 s. ch.; POC; printer; display; analysis; alarm; "
     "interface",
     "Giám sát quá trình; 1, 2, 3, 4 kênh liên tục, 6 kênh quét; POC; máy in; màn hiển thị; "
     "phân tích; cảnh báo; giao diện",
     "Yokogawa E. C.", "4.000 (4 kênh liên tục)"),
    ("μR1800", "Process mon.; 1,2,3,4 c. ch., 6,12,18,24 s. ch.; POC; printer; display; analysis; "
     "alarm; interface",
     "Giám sát quá trình; 1, 2, 3, 4 kênh liên tục, 6, 12, 18, 24 kênh quét; POC; máy in; "
     "màn hiển thị; phân tích; cảnh báo; giao diện",
     "Yokogawa E. C.", "5.600 (4 kênh liên tục)"),
    ("DR240", "Process mon.; 30 s. ch.; printer; display; analysis; alarm; interface",
     "Giám sát quá trình; 30 kênh quét; máy in; màn hiển thị; phân tích; cảnh báo; giao diện",
     "Yokogawa E. C.", "6.500 (30 kênh quét)"),
    ("RL100", "Process mon.; 1,2 c. ch., 6 s. ch.; printer; alarm",
     "Giám sát quá trình; 1, 2 kênh liên tục, 6 kênh quét; máy in; cảnh báo",
     "Honeywell", "1.500 (2 kênh liên tục)"),
    ("DPR100C/D", "Process mon.; 1,2,3 c. ch., 6 s. ch.; POC; printer; display; alarm; interface",
     "Giám sát quá trình; 1, 2, 3 kênh liên tục, 6 kênh quét; POC; máy in; màn hiển thị; "
     "cảnh báo; giao diện",
     "Honeywell", "3.000 (6 kênh quét)"),
    ("DPR3000", "Process mon.; 4 to 32 s. ch.; printer; display; alarm; analysis; interface",
     "Giám sát quá trình; 4 đến 32 kênh quét; máy in; màn hiển thị; cảnh báo; phân tích; giao diện",
     "Honeywell", "7.700 (32 kênh quét)"),
    ("4101", "Process mon.; 1 to 4 c. ch., 6 s. ch.; POC; printer; alarm",
     "Giám sát quá trình; 1 đến 4 kênh liên tục, 6 kênh quét; POC; máy in; cảnh báo",
     "Eurotherm", "2.400 (4 kênh liên tục)"),
    ("4180 G", "Process mon.; 8,16,24,32 s. ch.; printer; waveform display; alarm; analysis; "
     "interface",
     "Giám sát quá trình; 8, 16, 24, 32 kênh quét; máy in; màn hiển thị dạng sóng; cảnh báo; "
     "phân tích; giao diện",
     "Eurotherm", "9.800 (32 kênh quét)"),
    ("Sirec L", "Process mon.; 1,2,3 c. ch.", "Giám sát quá trình; 1, 2, 3 kênh liên tục",
     "Siemens", "1.200 (3 kênh liên tục)"),
]


def _t1(lang):
    vi = lang == "vi"
    hd = (("Mã hiệu", "Mô tả", "Nhà chế tạo", "Giá tham khảo (USD)") if vi else
          ("Designation", "Description", "Manufacturer", "Approximate price (U.S.$)"))
    rows = [(r[0], r[2] if vi else r[1], r[3], r[4]) for r in _T1]
    cap = ("BẢNG 96.1 Máy ghi bút. Ghi chú: c. ch. = kênh liên tục; s. ch. = kênh quét." if vi else
           "TABLE 96.1 Pen recorders. Note: c. ch. = continuous channel; s. ch. = scanned channel.")
    return hd, rows, cap, ""


# ================================================================ TABLE 96.2

_T2A = [
    ("LR8100", "250", "1200", "10", "1,6", "—", "5", "8"),
    ("LR102", "200", "600", "10", "0,4", "0,5", "1,5", "2"),
    ("LR122", "200", "600", "10", "0,4", "0,5", "1,5", "2"),
    ("MC1000", "250", "1200", "7,5", "1,6", "—", "—", "12"),
    ("BD112", "200", "1200", "6", "—", "0,2", "—", "2"),
    ("BD200", "250", "1200", "5", "—", "0,25", "—", "8"),
    ("L250", "250", "1200", "6", "1", "0,12", "3,6", "2"),
    ("L2066", "250", "3000", "1", "1", "0,3", "2", "6"),
    ("MCR560", "250", "600", "10", "—", "0,3", "1,5", "6"),
    ("DCR540", "250", "600", "10", "—", "0,3", "1,5", "4"),
    ("PCR500SP", "250", "1200", "10", "2", "0,15", "4,5", "8"),
    ("Omega640", "250", "600", "30", "0,5", "—", "—", "3"),
    ("Omega600A", "250", "600", "10", "0,1", "—", "—", "6"),
]

_T2B = [
    ("μR1000", "100", "200", "5", "1", "10", "4 c, 6 s"),
    ("μR1800", "180", "200", "5", "1,5", "10 (6 s)", "4 c, 24 s"),
    ("DR240", "250", "25", "1", "—", "2", "30 s"),
    ("RL100", "100", "8", "10", "3,2", "5", "2 c, 6 s"),
    ("DPR100C/D", "100", "100", "1", "1", "0,6", "3 c, 6 s"),
    ("DPR3000", "250", "25", "1", "—", "5", "32 s"),
    ("4101", "100", "25", "1", "2", "5", "4 c, 6 s"),
    ("4180 G", "180", "25", "1", "—", "3", "32 s"),
    ("Sirec L", "100", "20", "1", "—", "—", "3 c"),
]


def _t2a(lang):
    vi = lang == "vi"
    hd = (("Kiểu (thử nghiệm, đo)", "Chiều rộng ghi (mm)", "Tốc độ giấy lớn nhất (mm/phút)",
           "nhỏ nhất (mm/giờ)", "Tốc độ bút lớn nhất (m/s)",
           "Thời gian đáp ứng bậc thang của bút (s)", "Băng thông (–3 dB) (Hz)",
           "Số kênh liên tục lớn nhất") if vi else
          ("Type (test, measurement)", "Recording width (mm)", "Chart velocity max. (mm/min)",
           "min. (mm/h)", "Pen velocity max. (m/s)", "Pen step response time (s)",
           "Bandwidth (–3 dB) (Hz)", "Number of continuous channels max."))
    cap = ("BẢNG 96.2 Chỉ tiêu máy ghi bút — nhóm thử nghiệm và đo." if vi else
           "TABLE 96.2 Pen recorder specifications — test and measurement group.")
    return hd, _T2A, cap, ""


def _t2b(lang):
    vi = lang == "vi"
    hd = (("Kiểu (giám sát quá trình)", "Chiều rộng ghi (mm)", "Tốc độ giấy lớn nhất (mm/phút)",
           "nhỏ nhất (mm/giờ)", "Tốc độ bút lớn nhất (m/s)",
           "Thời gian đáp ứng bậc thang của bút (s)", "Chu kỳ quét đầu in (s)",
           "Số kênh lớn nhất") if vi else
          ("Type (process monitor)", "Recording width (mm)", "Chart velocity max. (mm/min)",
           "min. (mm/h)", "Pen velocity max. (m/s)", "Pen step response time (s)",
           "Printhead scanning cycle (s)", "Number of channels (max.)"))
    cap = ("BẢNG 96.2 (tiếp) Chỉ tiêu máy ghi bút — nhóm giám sát quá trình. "
           "Ghi chú: c = liên tục; s = quét." if vi else
           "TABLE 96.2 (continued) Pen recorder specifications — process monitor group. "
           "Note: c = continuous; s = scanned.")
    return hd, _T2B, cap, ""


# ================================================================ TABLE 96.3

_T3 = [
    ("WR 5000", "8 a. ch.; memory", "8 kênh tương tự; bộ nhớ", "Graphtec C.", "17.100 (8 ch.)"),
    ("WR 9000", "4,8,16 a. ch.; monitor; memory; x–y; analysis; FFT",
     "4, 8, 16 kênh tương tự; màn theo dõi; bộ nhớ; x–y; phân tích; FFT",
     "Graphtec C.", "11.300 (4 ch.)"),
    ("Mark 12", "4 to 52 a. ch., 4 to 52 d. ch.; monitor; memory",
     "4 đến 52 kênh tương tự, 4 đến 52 kênh số; màn theo dõi; bộ nhớ",
     "W. Graphtec", "30.300 (16 kênh tương tự)"),
    ("MA 6000", "2 to 16 a. ch.; monitor; memory; x–y; analysis; FFT",
     "2 đến 16 kênh tương tự; màn theo dõi; bộ nhớ; x–y; phân tích; FFT",
     "Graphtec C.", "23.500 (8 ch.)"),
    ("ORP 1200", "4,8 a. ch., 16 d. ch.; monitor; memory; x–y",
     "4, 8 kênh tương tự, 16 kênh số; màn theo dõi; bộ nhớ; x–y",
     "Yokogawa E. C.", "11.600 (8 kênh tương tự)"),
    ("ORP 1300", "16 a. ch., 16 d. ch.; monitor; memory; x–y",
     "16 kênh tương tự, 16 kênh số; màn theo dõi; bộ nhớ; x–y",
     "Yokogawa E. C.", "18.000 (16 kênh tương tự)"),
    ("ORM 1200", "4,8 a. ch., 16 d. ch.; monitor; memory; x–y",
     "4, 8 kênh tương tự, 16 kênh số; màn theo dõi; bộ nhớ; x–y",
     "Yokogawa E. C.", "14.100 (8 kênh tương tự)"),
    ("ORM 1300", "16 a. ch., 16 d. ch.; monitor; memory; x–y",
     "16 kênh tương tự, 16 kênh số; màn theo dõi; bộ nhớ; x–y",
     "Yokogawa E. C.", "21.900 (16 kênh tương tự)"),
    ("OR 1400", "8 a. ch., 16 d. ch.; monitor; memory; x–y",
     "8 kênh tương tự, 16 kênh số; màn theo dõi; bộ nhớ; x–y",
     "Yokogawa E. C.", "16.100 (8 kênh tương tự)"),
    ("TA 240", "1 to 4 a. ch.", "1 đến 4 kênh tương tự", "Gould I. S.", "8.500 (4 ch.)"),
    ("TA 11", "4,8,16 a. ch.; monitor; memory",
     "4, 8, 16 kênh tương tự; màn theo dõi; bộ nhớ", "Gould I. S.", "18.900 (16 ch.)"),
    ("TA 6000", "8 to 64 a. ch., 8 to 32 d. ch.; monitor; memory",
     "8 đến 64 kênh tương tự, 8 đến 32 kênh số; màn theo dõi; bộ nhớ",
     "Gould I. S.", "33.900 (16 kênh tương tự)"),
    ("Windograf", "2 to 4 a. ch.; monitor", "2 đến 4 kênh tương tự; màn theo dõi",
     "Gould I. S.", "10.200 (4 ch.)"),
    ("Dash 10", "10,20,30 a. ch.; monitor; memory",
     "10, 20, 30 kênh tương tự; màn theo dõi; bộ nhớ", "Astro-Med", "22.500 (10 ch.)"),
    ("MT95K2", "8 to 32 a. ch., 32 d. ch.; monitor; memory; x–y; analysis",
     "8 đến 32 kênh tương tự, 32 kênh số; màn theo dõi; bộ nhớ; x–y; phân tích",
     "Astro-Med", "32.600 (8 kênh tương tự)"),
    ("8852", "4 a. ch., 24 d. ch.; monitor; memory; x–y; analysis; FFT",
     "4 kênh tương tự, 24 kênh số; màn theo dõi; bộ nhớ; x–y; phân tích; FFT",
     "Hioki E. E. C.", "22.300 (4 kênh tương tự)"),
    ("8815", "4 a. ch., 32 d. ch.; memory; x–y",
     "4 kênh tương tự, 32 kênh số; bộ nhớ; x–y",
     "Hioki E. E. C.", "4.500 (4 kênh tương tự)"),
    ("8825", "16 a. ch., 32 d. ch.; monitor; memory; x–y; analysis",
     "16 kênh tương tự, 32 kênh số; màn theo dõi; bộ nhớ; x–y; phân tích",
     "Hioki E. E. C.", "28.800 (8 kênh tương tự)"),
]


def _t3(lang):
    vi = lang == "vi"
    hd = (("Mã hiệu", "Mô tả", "Nhà chế tạo", "Giá tham khảo (USD)") if vi else
          ("Designation", "Description", "Manufacturer", "Approximate price (U.S.$)"))
    rows = [(r[0], r[2] if vi else r[1], r[3], r[4]) for r in _T3]
    cap = ("BẢNG 96.3 Máy ghi dãy điểm nhiệt. Ghi chú: a. ch. = kênh tương tự; "
           "d. ch. = kênh số." if vi else
           "TABLE 96.3 Thermal dot array recorders. Note: a. ch. = analog channel; "
           "d. ch. = digital channel.")
    return hd, rows, cap, ""


# ================================================================ TABLE 96.4

_T4A = [
    ("WR 5000", "384", "8", "200", "1", "1600", "64", "8"),
    ("WR 9000V", "200", "8", "100", "1", "—", "32", "—"),
    ("WR 9000M", "200", "8", "100", "1", "—", "32", "—"),
    ("Mark 12", "384", "8", "200", "1", "1600", "64", "8"),
    ("MA 6000", "205", "8", "100", "1", "—", "40", "—"),
    ("ORP 1200", "201", "8", "100", "10", "1600", "32", "16"),
    ("ORP 1300", "201", "8", "100", "10", "1600", "32", "16"),
    ("ORM 1200", "201", "8", "100", "10", "1600", "32", "16"),
    ("ORM 1300", "201", "8", "100", "10", "1600", "32", "16"),
    ("OR 1400", "201", "8", "250", "10", "6400", "32", "256"),
    ("TA 240", "104", "8", "125", "36", "1000", "32", "8"),
    ("TA 11", "264", "8", "200", "36", "1600", "16", "8"),
    ("TA 6000", "370", "8", "200", "36", "1600", "16", "8"),
    ("Windograf", "104", "8", "200", "36", "800", "32", "8"),
    ("Dash 10", "256", "12", "200", "60", "1200", "12", "6"),
    ("MT95K2", "400", "12", "500", "1", "2000", "48", "4"),
    ("8852", "100", "12", "25", "10", "200", "16", "8"),
    ("8815", "104", "6", "8", "10", "50", "12", "6"),
    ("8825", "256", "8", "20", "10", "200", "10", "10"),
]

_T4B = [
    ("WR 5000", "64", "14", "8a", "—", "—", "64", "32 k"),
    ("WR 9000V", "250", "12", "8a", "192 × 120", "640 × 400", "250", "512 k"),
    ("WR 9000M", "50", "14", "8a", "192 × 120", "640 × 400", "50", "512 k"),
    ("Mark 12", "200", "16", "52a, 52d", "97 × 77", "256 × 320", "200", "2 M"),
    ("MA 6000", "500", "16", "16a", "192 × 120", "640 × 400", "500", "512 k"),
    ("ORP 1200", "100", "14", "8a, 16d", "127ᵇ", "320 × 240", "100", "32 k"),
    ("ORP 1300", "100", "14", "16a, 16d", "127ᵇ", "320 × 240", "100", "32 k"),
    ("ORM 1200", "100", "14", "8a, 16d", "127ᵇ", "320 × 240", "100", "128 k"),
    ("ORM 1300", "100", "14", "16a, 16d", "127ᵇ", "320 × 240", "100", "128 k"),
    ("OR 1400", "100", "16", "8a, 16d", "127ᵇ", "320 × 240", "100", "256 k"),
    ("TA 240", "5", "12", "4a", "—", "—", "—", "—"),
    ("TA 11", "250", "12", "16a", "198 × 66", "640 × 200", "250", "500 k"),
    ("TA 6000", "250", "12", "64a, 32d", "224 × 96", "640 × 200", "250", "500 k"),
    ("Windograf", "10", "12", "4a", "178ᵇ", "800 × 350", "—", "—"),
    ("Dash 10", "250", "12", "30a", "256 × 64", "—", "250", "512 k"),
    ("MT95K2", "200", "12", "32a, 32d", "200", "—", "500", "512 k"),
    ("8852", "1,6", "8", "4a, 24d", "178ᵇ", "100 × 103", "1 M", "—"),
    ("8815", "12,5", "8", "4a, 32d", "—", "—", "500", "30 k"),
    ("8825", "8", "12", "16a, 32d", "254ᵇ", "640 × 480", "200", "500 k"),
]


def _t4a(lang):
    vi = lang == "vi"
    hd = (("Kiểu", "Chiều rộng ghi (mm)", "Độ phân giải dãy nhiệt (điểm/mm)",
           "Tốc độ giấy lớn nhất (mm/s)", "nhỏ nhất (mm/giờ)",
           "Tần số ghi lớn nhất (điểm/s)", "Độ phân giải trục thời gian lớn nhất (điểm/mm)",
           "nhỏ nhất (điểm/mm)") if vi else
          ("Type", "Recording width (mm)", "Thermal array resolution (dots/mm)",
           "Chart velocity max. (mm/s)", "min. (mm/h)", "Maximal writing frequency (dots/s)",
           "Time axis resolution max. (dots/mm)", "min. (dots/mm)"))
    cap = ("BẢNG 96.4 Chỉ tiêu máy ghi dãy điểm nhiệt (phần 1)." if vi else
           "TABLE 96.4 Thermal dot array recorder specifications (part 1).")
    return hd, _T4A, cap, ""


def _t4b(lang):
    vi = lang == "vi"
    hd = (("Kiểu", "Tần số lấy mẫu thời gian thực lớn nhất (kHz)", "Độ chính xác bit lớn nhất (bit)",
           "Số kênh lớn nhất", "Kích thước màn hiển thị (mm)", "Độ phân giải màn hiển thị (điểm ảnh)",
           "Tần số lấy mẫu bộ nhớ lớn nhất (kHz)",
           "Số mẫu lưu được mỗi kênh, lớn nhất") if vi else
          ("Type", "Sampling frequency real-time max. (kHz)", "Bit accuracy max. (bits)",
           "No. channels max.", "Display dimensions (mm)", "Display resolution (pixels)",
           "Sampling frequency memory max. (kHz)", "Samples stored/channel max."))
    cap = ("BẢNG 96.4 (tiếp) Chỉ tiêu máy ghi dãy điểm nhiệt (phần 2). Ghi chú: a = tương tự; "
           "d = số; b = theo đường chéo." if vi else
           "TABLE 96.4 (continued) Thermal dot array recorder specifications (part 2). "
           "Note: a = analog; d = digital; b = diagonal.")
    return hd, _T4B, cap, ""


# ================================================================ TABLE 96.5

_T5 = [
    ("Astro-Med, Inc.",
     "Astro-Med Industrial Park, West Warwick, RI 02893, Hoa Kỳ — fax (401) 822-2430 / "
     "điện thoại (401) 828-4000"),
    ("Kipp &amp; Zonen, Delft BV",
     "Mercuriusweg 1, P.O. Box 507, NL-2600 AM Delft, Hà Lan — fax 015-620351 / "
     "điện thoại 015-561000"),
    ("Eurotherm Recorders Ltd.",
     "Dominion Way, Worthing, West Sussex BN148QL, Anh — fax 01903-203767 / "
     "điện thoại 01903-205222"),
    ("Linseis GMBH",
     "Postfach 1404, Vielitzer Strasse 43, D-8672 Selb, Đức — fax 09287/70488 / "
     "điện thoại 09287/880-0"),
    ("Gould Instrument Systems, Inc.",
     "8333 Rockside Road, Valley View, OH 44125-6100, Hoa Kỳ — fax (216) 328-7400 / "
     "điện thoại (216) 328-7000"),
    ("Omega Engineering, Inc.",
     "P.O. Box 4047, Stamford, CT 06907-0047, Hoa Kỳ — fax (203) 359-7700 / "
     "điện thoại (203) 359-1660"),
    ("Graphtec Corporation",
     "503-10 Shinano-cho, Totsuka-ku, Yokohama 244, Nhật Bản — fax (045) 825-6396 / "
     "điện thoại (045) 825-6250"),
    ("Siemens AG, Bereich Automatisierungstechnik",
     "Geschäftsgebiet Processgeräte, AUT 34, D-76181 Karlsruhe, Đức — fax 0721/595-6885 / "
     "điện thoại 0721/595-2058"),
    ("Hioki E. E. Corporation",
     "81 Koizumi, Ueda, Nagano, 386-11, Nhật Bản — fax 0268-28-0568 / điện thoại 0268-28-0562"),
    ("Western Graphtec, Inc.",
     "11 Vanderbilt, Irvine, CA 92718-2067, Hoa Kỳ — fax (714) 770-6010 / điện thoại (800) 854-8385"),
    ("Honeywell Industrial Automation and Control",
     "16404 North Black Canyon Hwy., Phoenix, AZ 85023, Hoa Kỳ — điện thoại (800) 343-0228"),
    ("W+W Instruments AG",
     "Frankfurt-Strasse 78, CH-4142 Münchenstein, Thuỵ Sĩ — fax +41 (0) 6141166685 / "
     "điện thoại +41 (0) 614116477"),
    ("Yokogawa Electric Corporation",
     "Shinjuku-Nomura Bldg. 1-26-2 Nishi-Shinjuku, Shinjuku-ku, Tokyo 163-05, Nhật Bản — "
     "fax 81-3-3349-1017 / điện thoại 81-3-3349-1015"),
]


def _t5(lang):
    vi = lang == "vi"
    hd = (("Nhà chế tạo", "Địa chỉ · liên hệ") if vi else ("Manufacturer", "Address · contact"))
    cap = ("BẢNG 96.5 Các hãng chế tạo máy ghi đồ thị." if vi else
           "TABLE 96.5 Companies that make graphic recorders.")
    return hd, _T5, cap, ""


# ================================================================ 96.2 tables

_T6 = [("20", "6,0", "120"), ("16", "4,5", "96"), ("12", "3,5", "72"), ("8", "2,5", "48")]


def _t6(lang):
    vi = lang == "vi"
    hd = (("Bit", "Chữ số", "dB") if vi else ("Bits", "Digits", "dB"))
    cap = ("BẢNG 96.6 Quan hệ giữa số bit, số chữ số và dải động (dB)." if vi else
           "TABLE 96.6 Relation among bits, number of digits, and dynamic range (dB).")
    return hd, _T6, cap, " nom"


_T7 = [
    ("Xấp xỉ liên tiếp", "Successive approximation",
     "Độ phân giải cao; tốc độ cao; dễ dồn kênh",
     "High resolution; high speed; easily multiplexed",
     "Tốc độ lấy mẫu 1,25 MS/s, độ phân giải 12 bit; tốc độ 200 kS/s, độ phân giải 16 bit",
     "1.25 MS/s sampling rate, 12-bit resolution; 200 kS/s sampling rate, 16-bit resolution"),
    ("Dải con", "Subranging", "Tốc độ cao hơn", "Higher speed",
     "Tốc độ lấy mẫu 1 MHz, độ phân giải 12 bit",
     "1 MHz sampling rate, 12-bit resolution"),
    ("Sigma–delta", "Sigma–delta",
     "Độ phân giải cao; độ tuyến tính tuyệt vời; chống chồng phổ tích hợp; công nghệ tiên tiến nhất",
     "High resolution; excellent linearity; built-in antialiasing; state-of-the-art technology",
     "Tốc độ lấy mẫu 48 kHz, độ phân giải 16 bit",
     "48 kHz sampling rate, 16-bit resolution"),
    ("Tích phân", "Integrated",
     "Độ phân giải cao; loại nhiễu tốt; công nghệ đã chín muồi",
     "High resolution; good noise rejection; mature technology",
     "Tốc độ lấy mẫu 15 kHz", "15 kHz sampling rate"),
    ("Flash", "Flash", "Tốc độ cao nhất; công nghệ đã chín muồi",
     "Highest speed; mature technology", "Tốc độ lấy mẫu 125 MHz", "125 MHz sampling rate"),
]


def _t7(lang):
    vi = lang == "vi"
    hd = (("Kiểu ADC", "Ưu điểm", "Đặc trưng") if vi else
          ("Type of ADC", "Advantages", "Features"))
    rows = [(r[0] if vi else r[1], r[2] if vi else r[3], r[4] if vi else r[5]) for r in _T7]
    cap = ("BẢNG 96.7 Các kiểu ADC." if vi else "TABLE 96.7 Types of ADCs.")
    return hd, rows, cap, ""


# ================================================================ 96.3 tables

_T8 = [
    ("Dạng hạt", "Particulate", "γ-Fe₂O₃", "56–140", "23–32",
     "Đĩa mềm, băng âm thanh, video và thiết bị đo"),
    ("Dạng hạt", "Particulate", "γ-Fe₂O₃+Co", "60–140", "44–74",
     "Đĩa mềm, băng âm thanh, video và thiết bị đo"),
    ("Dạng hạt", "Particulate", "CrO₂", "110–140", "38–58",
     "Đĩa mềm, băng âm thanh, video và thiết bị đo"),
    ("Dạng hạt", "Particulate", "BaFe₁₂O₁₉", "56", "58", "Đĩa mềm"),
    ("Màng mỏng", "Thin film", "Co–Ni", "600–1100", "30–85", "Đĩa cứng"),
    ("Màng mỏng", "Thin film", "Co–Fe", "1100–1500", "60–150", "Đĩa cứng"),
    ("Màng mỏng", "Thin film", "Co–P", "600–1000", "36–120", "Đĩa cứng"),
    ("Màng mỏng", "Thin film", "Co–Ni–Pt", "600–1100", "60–175", "Đĩa cứng"),
    ("Màng mỏng", "Thin film", "Co–Cr–Ta", "350–900", "55–190", "Đĩa cứng"),
    ("Màng mỏng", "Thin film", "Co–Cr–Pt", "300–750", "56–200", "Đĩa cứng"),
]


def _t8(lang):
    vi = lang == "vi"
    hd = (("Nhóm", "Vật liệu", "M<sub>r</sub> (kA/m)", "H<sub>c</sub> (kA/m)", "Ứng dụng") if vi
          else ("Group", "Material", "M<sub>r</sub> (kA/m)", "H<sub>c</sub> (kA/m)", "Application"))
    rows = [(r[0] if vi else r[1], r[2], r[3], r[4], r[5]) for r in _T8]
    cap = ("BẢNG 96.8 Giá trị từ độ dư (M<sub>r</sub>) và lực kháng từ (H<sub>c</sub>) của một số "
           "môi trường từ thường dùng (một số giá trị lấy từ Tài liệu 5)." if vi else
           "TABLE 96.8 Remanence (M<sub>r</sub>) and coercivity (H<sub>c</sub>) values of some "
           "commonly used magnetic media (some values from Reference 5).")
    return hd, rows, cap, ""


_T9 = [
    ("Ni–Fe–Mo", "11000", "0,8", "2,0", "100", "Băng âm thanh"),
    ("Ni–Zn", "300–1500", "0,4–0,46", "11,8–27,6", "10¹¹", "Ổ đĩa mềm và đĩa cứng, băng video và thiết bị đo"),
    ("Mn–Zn", "3000–10000", "0,4–0,6", "11,8–15,8", "10⁶", "Ổ đĩa mềm và đĩa cứng, băng video và thiết bị đo"),
    ("Fe–Si–Al", "8000", "1,0", "2,0", "85", "Ổ đĩa mềm và đĩa cứng, băng video và thiết bị đo"),
    ("Ni–Fe", "2000–4000", "1,0", "&lt;10", "20", "Ổ đĩa cứng"),
]

_T9EN = [
    ("Ni–Fe–Mo", "11000", "0.8", "2.0", "100", "Audio tape"),
    ("Ni–Zn", "300–1500", "0.4–0.46", "11.8–27.6", "10¹¹",
     "Floppy and hard disk drives, video and instrumentation tapes"),
    ("Mn–Zn", "3000–10000", "0.4–0.6", "11.8–15.8", "10⁶",
     "Floppy and hard disk drives, video and instrumentation tapes"),
    ("Fe–Si–Al", "8000", "1.0", "2.0", "85",
     "Floppy and hard disk drives, video and instrumentation tapes"),
    ("Ni–Fe", "2000–4000", "1.0", "&lt;10", "20", "Hard disk drives"),
]


def _t9(lang):
    vi = lang == "vi"
    hd = (("Vật liệu", "μ", "B<sub>s</sub> (T)", "H<sub>c</sub> (A/m)", "ρ (µΩ·cm)", "Ứng dụng") if vi
          else ("Material", "μ", "B<sub>s</sub> (T)", "H<sub>c</sub> (A/m)", "ρ (µΩ·cm)", "Application"))
    cap = ("BẢNG 96.9 Giá trị độ từ thẩm tương đối (μ), cảm ứng từ bão hoà (B<sub>s</sub>), lực "
           "kháng từ (H<sub>c</sub>) và điện trở suất (ρ) của một số vật liệu làm lõi đầu từ thường "
           "dùng ở tần số thấp (một số giá trị lấy từ Tài liệu 5)." if vi else
           "TABLE 96.9 Relative permeability (μ), saturation flux density (B<sub>s</sub>), coercivity "
           "(H<sub>c</sub>) and resistivity (ρ) values of some commonly used magnetic head materials "
           "at low frequency (some values from Reference 5).")
    return hd, (_T9 if vi else _T9EN), cap, ""


_T10 = [("10", "0100"), ("11", "1000"), ("000", "000100"), ("010", "100100"),
        ("011", "001000"), ("0010", "00100100"), ("0011", "00001000")]


def _t10(lang):
    vi = lang == "vi"
    hd = (("Trước khi mã hoá", "Sau khi mã hoá") if vi else ("Before coding", "After coding"))
    cap = ("BẢNG 96.10 Mã 1/2(2,7)." if vi else "TABLE 96.10 1/2(2,7) code.")
    return hd, _T10, cap, " nom"


_T11 = [
    ("Đầu từ màng mỏng cho ổ đĩa cứng", "Thin-film head for hard disk drive",
     "AMC, Read-Rite, SAE", "6,00–9,00"),
    ("Đầu từ MR cho ổ đĩa cứng", "MR head for hard disk drive",
     "AMC, Read-Rite, SAE, Seagate", "8,00–12,00"),
    ("Đĩa cứng màng mỏng", "Thin-film hard disk", "Akashic, HMT, Komag, MCC, Stormedia",
     "7,00–10,00"),
    ("Ổ đĩa cứng", "Hard disk drive", "IBM, Maxtor, Quantum, Samsung, Seagate, WD",
     "0,02–0,20/Mbyte"),
    ("Ổ đĩa mềm", "Floppy drive", "Panasonic, Sony", "20,00–40,00"),
    ("Đĩa mềm", "Floppy disk", "3M, Fuji, Memorex, Sony", "0,15–0,50"),
    ("Ổ đĩa cứng tháo lắp", "Removable rigid disk drive", "Iomega, Syquest", "100,00–400,00"),
    ("Đĩa cứng tháo lắp", "Removable rigid disk", "Iomega, Maxell, Sony", "5,00–20,00/100 Mbyte"),
    ("Ổ băng", "Tape drive", "Exabyte, HP, Seagate", "100,00–400,00"),
    ("Băng sao lưu", "Backup tape", "3M, Sony, Verbatim", "4,00–25,00/Gbyte"),
    ("Ổ CD-ROM 8×", "8× CD-ROM drive", "Goldstar, Panasonic", "100,00–200,00"),
    ("Ổ quang ghi được", "Recordable optical drive", "JVC, Philips", "300,00–500,00"),
    ("Đĩa quang ghi được", "Recordable optical disk", "3M, Maxell, Memorex", "3,00–15,00/650 Mbyte"),
]


def _t11(lang):
    vi = lang == "vi"
    hd = (("Mô tả", "Nhà chế tạo", "Giá tham khảo, USD") if vi else
          ("Description", "Manufacturers", "Approximate price, $"))
    rows = [(r[0] if vi else r[1], r[2], r[3]) for r in _T11]
    cap = ("BẢNG 96.11 Thiết bị lưu trữ từ và quang dạng số." if vi else
           "TABLE 96.11 Digital magnetic and optical storage devices.")
    return hd, rows, cap, ""


# ================================================================ equations

_EQ = {
    "96.1": "B = μ<sub>0</sub>(H + M)",
    "96.2": "ρ<sub>θ</sub> = ρ[1 + (Δρ/ρ)cos<sup>2</sup>θ]",
    "96.3": "v = Jwρ(Δρ/ρ)(sin<sup>2</sup>θ<sub>0</sub> − sin<sup>2</sup>θ)",
    "96.4": "v = −nV dφ/dx",
    "96.5": ("H<sub>x</sub> = [ni/(π(g + lA<sub>g</sub>/(μA<sub>c</sub>)))] "
             "tan<sup>−1</sup>[yg/(x<sup>2</sup> + y<sup>2</sup> − g<sup>2</sup>/4)]"),
    "96.6": ("H<sub>y</sub> = [ni/(2π(g + lA<sub>g</sub>/(μA<sub>c</sub>)))] "
             "ln{[(x − g/2)<sup>2</sup> + y<sup>2</sup>]/[(x + g/2)<sup>2</sup> + y<sup>2</sup>]}"),
    "96.7": "M = (2/π)M<sub>r</sub> tan<sup>−1</sup>(x/a)",
    "96.8": ("a = [(1 − S*)(d + δ/2)]/(πQ) + √{[(1 − S*)(d + δ/2)]/(πQ)}<sup>2</sup> "
             "+ [M<sub>r</sub>δ(d + δ/2)]/(πQH<sub>c</sub>)"),
    "96.10": ("v(x) = −[2μ<sub>0</sub>VwM<sub>r</sub>δn/(π(g + lA<sub>g</sub>/(μA<sub>c</sub>)))] × "
              "[tan<sup>−1</sup>((g/2 + x)/(a + d)) + tan<sup>−1</sup>((g/2 − x)/(a + d))]"),
    "96.11": ("φ<sub>i</sub>(x) = [2μ<sub>0</sub>wM<sub>r</sub>δ(a + d)/(πg)] × "
              "{f[(x + (g + t)/2)/(a + d)] − f[(x + t/2)/(a + d)] + f[(x − (g + t)/2)/(a + d)] "
              "− f[(x − t/2)/(a + d)]}"),
    "96.12": "f(β) = β tan<sup>−1</sup>β − ln√(1 + β<sup>2</sup>)",
    "96.13": "φ<sub>s</sub>(y) = φ<sub>i</sub> sinh[(h − y)/l<sub>c</sub>]/sinh(h/l<sub>c</sub>)",
    "96.14": "l<sub>c</sub> = √(μgt/2)",
    "96.15": "sinθ<sub>0</sub>(y) = φ<sub>b</sub>(y)/(M<sub>s</sub>t)",
    "96.16": "sinθ(y) = [φ<sub>s</sub>(y) + φ<sub>b</sub>(y)]/(M<sub>s</sub>t)",
    "96.17": ("v = Jwρ(Δρ/ρ)(1/h)[∫<sub>0</sub><sup>h</sup> sin<sup>2</sup>θ<sub>0</sub>(y)dy "
              "− ∫<sub>0</sub><sup>h</sup> sin<sup>2</sup>θ(y)dy]"),
    "96.18": ("v<sub>p</sub> ≈ [9ΔρJwM<sub>r</sub>δ(g + t)/(8√2 tgM<sub>s</sub>)] "
              "tan<sup>−1</sup>[g/(2(a + d))]"),
    "96.19": "M(x) = M<sub>r</sub> sin(2πx/λ)",
    "96.20": ("v(x) = −[μ<sub>0</sub>VwM<sub>r</sub>ng/(g + lA<sub>g</sub>/(μA<sub>c</sub>))]"
              "(e<sup>−2πd/λ</sup>)(1 − e<sup>−2πδ/λ</sup>)[sin(πg/λ)/(πg/λ)]cos(2πx/λ)"),
    "96.21": ("v ∝ [4M<sub>r</sub>JΔρwλ/(ht)](e<sup>−2πd/λ</sup>)(1 − e<sup>−2πδ/λ</sup>)"
              "[sin(πg/λ)/(πg/λ)]sin[π(g + t)/λ]cos(2πx/λ)"),
    "96.22": "ΔV = V/2<sup>N</sup>",
    "96.23": "SNR = 12P<sub>s</sub>/ΔV<sup>2</sup>",
    "96.24": "SNR = 2<sup>2N</sup>",
    "96.25": "SNR = 1,5 × 2<sup>2N</sup>",
    "96.26": "V = kWs/H",
    "96.27": ("∂/∂X(PH<sup>3</sup>Q ∂P/∂X) + ∂/∂Y(PH<sup>3</sup>Q ∂P/∂Y) = "
              "Λ<sub>x</sub> ∂(PH)/∂X + Λ<sub>y</sub> ∂(PH)/∂Y + σ ∂(PH)/∂T"),
    "96.28": "F<sub>m</sub> = 4πRγ cosθ/[1 + y/(h − y)]",
    "96.29": "F = f(h, R, A, η, γ, θ, E, φ, σ, s)",
    "96.30": "I = I<sub>1</sub> + I<sub>2</sub> + 2√(I<sub>1</sub>I<sub>2</sub>) cos(4πh<sub>1</sub>/λ)",
    "96.32": "d<sub>1</sub> ≈ 2λ/(πθ)",
}


def _eq(lang, num):
    """Equation body, with the two language-bearing equations handled here."""
    if num == "96.9":
        if lang == "vi":
            return ("a<sub>m</sub> = M<sub>r</sub>δ/(2πH<sub>c</sub> &nbsp;nếu&nbsp; "
                    "M<sub>r</sub>δ/(4πH<sub>c</sub>d) ≥ 1; &nbsp; "
                    "√[(M<sub>r</sub>δd)/(πH<sub>c</sub>)] &nbsp;nếu&nbsp; "
                    "M<sub>r</sub>δ/(4πH<sub>c</sub>d) &lt; 1")
        return ("a<sub>m</sub> = M<sub>r</sub>δ/(2πH<sub>c</sub> &nbsp;if&nbsp; "
                "M<sub>r</sub>δ/(4πH<sub>c</sub>d) ≥ 1; &nbsp; "
                "√[(M<sub>r</sub>δd)/(πH<sub>c</sub>)] &nbsp;if&nbsp; "
                "M<sub>r</sub>δ/(4πH<sub>c</sub>d) &lt; 1")
    if num == "96.31":
        if lang == "vi":
            return ("I = I<sub>1</sub> + I<sub>2</sub> − 2√(I<sub>1</sub>I<sub>2</sub>) "
                    "&nbsp;nếu có hố (h<sub>1</sub> = λ/4); &nbsp; "
                    "I<sub>1</sub> + I<sub>2</sub> + 2√(I<sub>1</sub>I<sub>2</sub>) "
                    "&nbsp;nếu không có hố (h<sub>1</sub> = 0)")
        return ("I = I<sub>1</sub> + I<sub>2</sub> − 2√(I<sub>1</sub>I<sub>2</sub>) "
                "&nbsp;if there is a pit (h<sub>1</sub> = λ/4); &nbsp; "
                "I<sub>1</sub> + I<sub>2</sub> + 2√(I<sub>1</sub>I<sub>2</sub>) "
                "&nbsp;if there is no pit (h<sub>1</sub> = 0)")
    return _EQ[num]


# ================================================================ Vietnamese

def body_vi():
    b = []

    # ---------------------------------------------------------------- 96.1
    b.append(h2("96.1 Máy ghi đồ thị", "Graphic Recorders"))
    b.append(p(
        "Một máy ghi đồ thị xét cho cùng là một thiết bị đo có khả năng tạo ra, ngay trong thời gian "
        "thực, một bản sao cứng của một tập hàm thời gian, nhằm mục đích kiểm tra bằng mắt tức thời "
        "và/hoặc về sau. Các đường cong hầu như luôn được vẽ trên một dải giấy (dài) — xé từ cuộn "
        "hoặc gấp kiểu Z — nên thiết bị được gọi là máy ghi dải. Khi đó biến độc lập thời gian (t) "
        "ứng với trục chiều dài dải, còn các đại lượng vật lý đo được ứng với chiều rộng của giấy. "
        "Vết ghi nhận được nhờ một quá trình ghi tại các vị trí trên trục ngắn (y) của giấy, tương "
        "ứng với độ lớn của đại lượng vật lý, trong khi dải giấy chuyển động với vận tốc không đổi "
        "để tạo ra trục thời gian."))
    b.append(p(
        "Không thể diễn giải đồ thị nếu thiếu những thông tin thiết yếu; thang chia và mức chuẩn cho "
        "từng đại lượng vật lý được ghi cũng như cho thời gian đều là những thứ bắt buộc. Thông tin "
        "bổ sung về điều kiện thí nghiệm của lần ghi cũng cần thiết, và tốt nhất là do chính thiết bị "
        "in ra (ngày tháng, đối tượng khảo sát, kiểu thí nghiệm, v.v.). Năng lực của máy ghi đồ thị "
        "do đó được quyết định bởi độ chính xác đo, khả năng thuật lại thông tin bổ sung và chất "
        "lượng đồ hoạ của nó — bao gồm độ sắc nét của vết, khả năng phân biệt giữa các vết (ví dụ "
        "bằng màu khác nhau), và độ ổn định chất lượng theo thời gian lưu trữ dài hạn."))
    b.append(p(
        "Các máy ghi dải đơn giản chỉ tạo vết trên giấy đã in sẵn thang chia; những máy ghi đồ thị "
        "tiên tiến hơn thì vừa tạo vết vừa vẽ các đường chuẩn, hiển thị thông tin bổ sung dưới dạng "
        "chữ-số ngay trên giấy, lưu cài đặt thiết bị và dữ liệu đã ghi vào bộ nhớ (có thể tái tạo "
        "trên giấy theo nhiều chế độ khác nhau), có màn hình theo dõi dạng sóng gắn liền, và có thể "
        "trao đổi với PC qua giao diện nối tiếp chuẩn. Ranh giới giữa loại máy ghi đồ thị “thông "
        "minh” này với, một mặt, các máy hiện sóng lưu trữ số có gắn bộ sao cứng và, mặt khác, các "
        "hệ thu thập dữ liệu dựa trên PC có máy in laser hay máy vẽ, trở nên rất mờ nhạt. Chính khả "
        "năng tạo bản sao cứng trong thời gian thực có lẽ là yếu tố phân biệt rõ nhất giữa máy ghi "
        "đồ thị và các hệ đo khác có tạo bản sao cứng. Máy ghi đồ thị được dùng cho các ứng dụng thử "
        "nghiệm và đo lường trong phòng thí nghiệm cũng như ngoài hiện trường, và cho việc giám sát, "
        "điều khiển quá trình công nghiệp. Máy ghi đồ thị được dùng rất nhiều trong các ứng dụng đo "
        "lường y sinh [1]."))
    b.append(p(
        "Trong khi trục thời gian được tạo ra bằng cách cho giấy chạy với vận tốc không đổi, trục "
        "tung có thể được đánh dấu theo cách tương tự hoặc theo cách số. Đầu biến đổi của máy ghi "
        "tương tự tạo ra một dịch chuyển vật lý của cơ cấu ghi, ví dụ bút hoặc đầu in. Với đầu biến "
        "đổi số, không có chi tiết chuyển động: cơ cấu ghi là một dãy thẳng hàng cố định gồm các "
        "điểm ghi cách đều, phủ kín toàn bộ chiều rộng của giấy; khi đó thao tác ghi là kích hoạt "
        "điểm nằm ở vị trí tương ứng với độ lớn của tín hiệu và chấm một điểm lên giấy. Như vậy máy "
        "ghi tương tự có thể tạo ra đường liền, còn máy ghi số tạo ra đường chấm. Nếu độ phân giải "
        "theo trục tung và trục thời gian đủ lớn, bản ghi số có chất lượng đồ hoạ tuyệt vời về cảm "
        "nhận liên tục bằng mắt."))
    b.append(p(
        "Đầu biến đổi tương tự có thể được dùng ở chế độ không liên tục và như vậy đảm nhận một tập "
        "tín hiệu biến thiên chậm; trong chu kỳ quét, cơ cấu ghi đang chuyển động chấm một điểm lên "
        "giấy tại vị trí ứng với độ lớn của tín hiệu. Một đầu biến đổi số và một đầu biến đổi tương "
        "tự làm việc ở chế độ quét đều có thể đảm nhận một tập tín hiệu; còn một đầu biến đổi tương "
        "tự chỉ xử lý được một tín hiệu ở chế độ liên tục. Với đầu biến đổi số, số tín hiệu ghi được "
        "về nguyên tắc là không hạn chế; do đó nó được lập trình để vẽ các đường chuẩn cần thiết. Với "
        "đầu biến đổi tương tự thì phải dùng giấy đã in sẵn thang chia. Trong trường hợp này thường "
        "dùng cách ghi bằng mực, và các màu khác nhau bảo đảm khả năng nhận dạng vết rất tốt. Với dãy "
        "điểm số, có thể làm đậm ít nhiều việc in điểm cho các kênh khác nhau, hoặc kích hoạt nhiều "
        "hơn một điểm liền kề, khiến đường có độ đen và độ dày lớn hơn hoặc nhỏ hơn. Tuy vậy, việc "
        "nhận dạng vết thường được thực hiện bằng chú thích chữ-số."))
    b.append(p(
        "Ở máy ghi đồ thị tương tự, đầu biến đổi có thể được thiết kế theo chế độ trực tiếp hoặc chế "
        "độ servo. Ở chế độ trực tiếp, độ lớn của tín hiệu được biến đổi trực tiếp thành vị trí của "
        "cơ cấu ghi (ví dụ kiểu điện kế đơn giản). Ở chế độ servo (còn gọi là chế độ phản hồi hay "
        "bù), vị trí của cơ cấu ghi được một hệ cảm biến riêng đo lại, và hiệu giữa giá trị đo được "
        "với giá trị của tín hiệu cần ghi được đưa tới động cơ của đầu biến đổi, tạo ra một chuyển "
        "động có xu hướng triệt tiêu hiệu đó và nhờ vậy chỉnh lại vị trí [2,3]. Ở cả hai phương pháp, "
        "các chi tiết chuyển động đặt giới hạn cho dải tần của hệ. Hơn nữa, ở chế độ phản hồi có thể "
        "tồn tại những giới hạn về vận tốc và gia tốc; do đó cách mô tả hệ tuyến tính theo lý thuyết "
        "hệ thống đối với tần số tín hiệu có thể không áp dụng được. Như vậy, dải thông của hệ servo "
        "có thể phụ thuộc vào chiều rộng vùng ghi."))
    b.append(p(
        "Chuyển động của cơ cấu ghi có thể được tạo ra bằng quay hoặc bằng tịnh tiến. Ở trường hợp "
        "sau, bộ phận ghi được dẫn hướng bằng cơ khí; chủ yếu người ta dùng phương pháp servo [3]. "
        "Chuyển động quay thường đạt được nhờ kiểu động cơ điện kế [3,4]; điện kế có thể làm quay "
        "một cây bút, một tia mực, hoặc một chùm sáng. Quán tính của chi tiết chuyển động là thông số "
        "chính quyết định dải thông của hệ. Các thiết bị tịnh tiến cho dải thông vài hertz. Dải thông "
        "cao hơn đạt được với bút điện kế (khoảng 100 Hz), tia mực (tới 1 kHz) và hệ quang (tới "
        "10 kHz) [1], nhưng vì đã bị máy ghi dãy điểm hoặc hệ thu thập dữ liệu thay thế, những kiểu "
        "này đang biến mất khỏi thị trường. Những lý do chính là sai số và hạn chế cố hữu của các "
        "kiểu tương tự này, nhu cầu bảo trì chi tiết chuyển động và cơ cấu mực, giá giấy ảnh, và việc "
        "thiếu các khả năng của kiểu số."))
    b.append(p(
        "Nếu chi tiết chuyển động hạn chế dải thông của máy ghi tương tự, thì năng lực tương ứng của "
        "máy ghi đồ thị số lại do tần số lấy mẫu và tần số ghi quyết định. Theo tiêu chuẩn lấy mẫu, "
        "tần số lấy mẫu phải bằng hai lần tần số cao nhất của tín hiệu. Điều đó có nghĩa chỉ hai mẫu "
        "để thể hiện trọn một chu kỳ sin — khó có thể gọi là một biểu diễn đồ hoạ tốt. Mười mẫu có "
        "thể là mức tối thiểu. Tần số lấy mẫu thuần tuý là chuyện điện tử; trong thời gian thực thì "
        "tần số ghi cực đại của dãy điểm mới là yếu tố giới hạn. Hoặc, nếu phổ tín hiệu vượt quá dải "
        "thông thời gian thực của máy ghi, dữ liệu có thể được lưu vào bộ nhớ với tốc độ lấy mẫu đủ "
        "lớn rồi tái tạo ngoại tuyến ở tốc độ chậm hơn mà thiết bị xử lý được. Phần lớn máy ghi số có "
        "khả năng bộ nhớ này; một số máy được gọi riêng là máy ghi “bộ nhớ” khi năng lực ngoại tuyến "
        "của chúng vượt trội hẳn so với hiệu năng trực tuyến."))
    b.append(p(
        "Việc ghi trong thời gian thực chủ yếu được thực hiện như một hàm của thời gian (máy ghi "
        "t–y). Mặt khác, ghi x–y là một cách khác để biểu diễn dữ liệu. Khi đó người ta ghi quan hệ "
        "giữa hai đại lượng vật lý và loại trừ biến độc lập thời gian (ngoài việc, nếu dùng đường nét "
        "đứt, mỗi nét có thể ứng với một khoảng thời gian cố định). Ở máy ghi x–y tương tự tiêu chuẩn, "
        "giấy đứng yên (ví dụ được cố định tĩnh điện lên bàn ghi); trong máy có hai đầu biến đổi ghi "
        "tương tự giống nhau với mạch vào như nhau. Đầu biến đổi thứ nhất (y) dịch chuyển một cần dài "
        "phủ hết chiều rộng tờ giấy, trên đó đầu biến đổi thứ hai (x) mang bút di chuyển. Rõ ràng, "
        "các máy ghi có bộ nhớ và phần mềm thích hợp có thể tạo bản ghi x–y ở chế độ ngoại tuyến bằng "
        "cách chấm điểm trong khi giấy vẫn chạy."))
    b.append(p(
        "Độ chính xác ghi có thể được phát biểu theo cách tương tự như với bất kỳ dụng cụ đo nào [5]. "
        "Độ chính xác này, một mặt, do khâu điều hoà tín hiệu vào quyết định — giống nhau cho cả kiểu "
        "số lẫn kiểu tương tự — và mặt khác do độ chính xác của đầu biến đổi ghi cùng điện tử điều "
        "khiển nó. Ở kiểu số, độ chính xác bit khi số hoá, tần số lấy mẫu, độ phân giải của dãy điểm "
        "và tần số ghi điểm là những thông số chính. Ở kiểu tương tự có thể thấy những nhược điểm "
        "điển hình của hệ đầu biến đổi tương tự (như phi tuyến tĩnh, nhiễu và trôi, vùng chết và "
        "trễ, hành vi động bị hạn chế); hệ servo được biết là chính xác hơn hệ trực tiếp. Ví dụ, "
        "trôi trong ghi tương tự có thể là kết quả của một dịch nhỏ của giấy đã in thang chia dọc "
        "theo trục y; điều này bị loại trừ nếu máy ghi tự vẽ các đường chuẩn của nó."))
    b.append(p(
        "Về chất lượng đồ hoạ, độ rõ và độ sắc của vết là quan trọng (trong một phạm vi rộng các vận "
        "tốc ghi). Chất lượng vết phụ thuộc vào vận tốc ghi, tức vận tốc của cơ cấu ghi so với tờ "
        "giấy đang chạy. Rõ ràng, lưu lượng của môi chất ghi (ví dụ mực hoặc nhiệt) phải được điều "
        "chỉnh ít nhiều theo vận tốc ghi để tránh vết khó thấy ở vận tốc cao và nét dày ở vận tốc "
        "thấp. Khả năng nhận dạng tốt các đường cong chồng lên nhau là thiết yếu. Độ phân giải điểm "
        "đầy đủ (với kỹ thuật nội suy thích hợp) là quan trọng ở các kiểu không liên tục để tiện "
        "kiểm tra bằng mắt."))
    b.append(p(
        "Một máy ghi đồ thị có thể được thiết kế như thiết bị một kênh hoặc có đầu vào nhiều kênh. "
        "Đầu vào có thể là chuẩn hoá hoặc mô-đun, để người dùng chọn được bộ điều hoà tín hiệu cụ thể "
        "cho ứng dụng và số kênh. Máy ghi có thể được gọi là “vạn năng” hoặc được lắp trong một thiết "
        "bị đo chuyên dụng (ví dụ trong các ứng dụng y sinh như điện tâm đồ và điện não đồ). Máy ghi "
        "có thể xách tay để làm việc ngoài hiện trường, hoặc lắp trong giá phòng thí nghiệm hay trong "
        "bảng điều khiển. Giấy có thể chạy theo phương thẳng đứng hoặc phương nằm ngang trên một bàn "
        "ghi (máy ghi “bàn phẳng”), và có thể cấp từ cuộn hoặc gấp kiểu Z. Ngoài máy ghi dải và máy "
        "ghi x–y, còn có máy ghi giấy tròn. Ở loại này giấy quay, một vòng quay ứng với một khoảng "
        "đo trọn vẹn, và giấy được in sẵn các đường chuẩn thích hợp với chuyển động của các bút ghi "
        "trên đó."))
    b.append(p(
        "Ngoài các thiết bị bút tịnh tiến có dải thông thấp, mối quan tâm tới máy ghi đồ thị tương tự "
        "đang giảm. Chúng đang được thay bằng máy ghi dãy điểm nhiệt hoặc bằng hệ thu thập dữ liệu. "
        "Tuy vậy, vì một số kiểu có thể vẫn còn được chế tạo và nhiều thiết bị có thể vẫn đang được "
        "dùng, nên các kỹ thuật khác nhau vẫn được nhắc tới. Có thể tìm thấy mô tả về nguyên lý và "
        "hiệu năng của máy ghi tương tự trong Tài liệu 1. Máy ghi điện kế dùng đầu biến đổi kiểu "
        "quay. Cả nguyên lý trực tiếp lẫn nguyên lý servo đều được dùng. Kiểu trực tiếp sử dụng cơ "
        "cấu d’Arsonval như trong các điện kế thông thường [1, 2, 4]. Về mặt động học, điện kế hành "
        "xử như một hệ cộng hưởng cơ, và do đó dải thông do tần số cộng hưởng của nó quyết định, mà "
        "tần số này lại phụ thuộc quán tính của các chi tiết chuyển động. Rõ ràng, chuyển động quay "
        "sinh ra những sai số cố hữu trong máy ghi đồ thị. Nếu dùng ngòi bút (vuông góc với cần bút, "
        "kiểu nhiệt hoặc mực), chuyển động quay của cần bút gắn với cuộn điện kế diễn ra trong một "
        "mặt phẳng song song với mặt phẳng giấy, nên bản ghi là đường cong thay vì đường thẳng, gây "
        "sai số đối với trục thời gian và trục tung (giá trị tung độ tỉ lệ với tang của góc quay). "
        "Giấy in sẵn các đường toạ độ cong có thể giải quyết vấn đề này; tuy vậy vết vẫn bị biến dạng "
        "và điểm không rất nhạy. Có thể đạt được bản ghi thẳng bằng hệ bút, tia mực và chùm sáng. Bản "
        "ghi bút thẳng có thể xấp xỉ được với ngòi bút trong trường hợp bút “cần dài” và nhờ cơ cấu "
        "làm thẳng bằng cơ khí; hoặc cách ghi “lưỡi dao” là một giải pháp [1]. Trong trường hợp máy "
        "ghi tia mực và chùm sáng, mặt phẳng quay và mặt phẳng giấy không nhất thiết phải song song; "
        "khi đó việc ghi diễn ra tại đường giao của hai mặt phẳng và do đó về bản chất là thẳng. "
        "Trong ghi bằng tia mực, một vòi phun cỡ nhỏ mà mực được bơm qua được gắn theo phương vuông "
        "góc với trục của điện kế. Trong ghi quang, một chùm sáng hẹp được một gương nhỏ nối với cuộn "
        "dây chuyển động của điện kế phản chiếu về phía giấy cảm quang. Ở các phương pháp này, việc "
        "thu nhỏ các chi tiết chuyển động làm tăng tần số cộng hưởng và do đó tăng dải thông. Trong "
        "khi dải thông điển hình của một hệ bút điện kế là 100 Hz, dải thông của hệ tia mực có thể "
        "là 1000 Hz và của hệ quang có thể đạt 10 kHz. Trong ống tia âm cực sợi quang (FO-CRT) không "
        "có chi tiết chuyển động cơ khí nào, và do đó không có giới hạn cơ khí nào đối với dải thông. "
        "FO-CRT thực chất là một CRT một chiều. Một lớp phosphor ở mặt trong của màn hình biến tia âm "
        "cực thành ánh sáng tử ngoại (UV). Ánh sáng UV này được một tấm mặt ngoài làm từ sợi thuỷ tinh "
        "dẫn tới tờ giấy cảm quang. Như trong các máy hiện sóng thông thường, độ lệch của điểm sáng "
        "tỉ lệ trực tiếp với tín hiệu đặt vào đầu vào của khối làm lệch. Dải thông do điện tử điều "
        "khiển quyết định. Hệ có thể dùng ở chế độ quét vì cường độ chùm tia dễ điều khiển. Trong các "
        "đoạn sau sẽ nói chi tiết hơn về máy ghi bút tịnh tiến và máy ghi dãy điểm nhiệt."))

    b.append(h3("Máy ghi bút tịnh tiến", "Translational Pen Recorders"))
    b.append(p(
        "Ở máy ghi bút tịnh tiến, cơ cấu ghi thường là bút đầu sợi có hộp mực. Trong các ứng dụng "
        "không liên tục, cơ cấu ghi có thể là đầu in với các ngòi màu khác nhau hoặc với ruy-băng "
        "màu. Máy có cơ cấu nhấc bút bằng tay hoặc tự động. Trong khi ghi, cơ cấu ghi tịnh tiến dọc "
        "trục y vì nó được nối với một hệ dẫn hướng cơ khí và một hệ dây vòng kín. Một hệ động cơ và "
        "bánh xe kéo dây và do đó kéo cơ cấu ghi. Ở một số thiết kế người ta dùng hệ động cơ và trục "
        "vít. Máy ghi tịnh tiến chủ yếu được thiết kế theo kiểu servo. Vị trí của bút được đo chính "
        "xác, và điện áp hiệu giữa tín hiệu vào với độ lớn vị trí (sau khi khuếch đại và điều hoà "
        "thích hợp) điều khiển động cơ servo. Động cơ servo có thể là kiểu một chiều hoặc kiểu bước; "
        "điện tử servo có thể tương tự hoặc số. Cảm nhận vị trí có thể theo kiểu biến trở (“máy ghi "
        "biến trở”): xe trượt mang bút được trang bị một tiếp điểm trượt trên điện trở (dây quấn hoặc "
        "màng dày) phủ hết chiều rộng tờ giấy. Các phương pháp phát triển gần đây dùng nguyên lý "
        "quang hoặc siêu âm để cảm nhận vị trí; với những phương pháp này không có tiếp điểm, nên ít "
        "phải bảo trì và tuổi thọ dài hơn. Ví dụ, ở phương pháp siêu âm, vị trí bút được một cuộn cảm "
        "biến xác định từ thời gian lan truyền của một xung siêu âm do một đầu biến đổi áp điện truyền "
        "vào một dải từ giảo phủ hết chiều rộng giấy. Theo đó, một số thiết bị dùng động cơ một chiều "
        "không chổi than. Trong hệ servo, độ chính xác phần lớn do chất lượng của hệ cảm nhận quyết "
        "định. Tiếp xúc kém với điện trở có thể sinh nhiễu; có thể có độ rơ cơ khí giữa ngòi bút và "
        "tiếp điểm trượt trên biến trở. Vận tốc của xe trượt bị hạn chế, khoảng 0,5 đến 2 m/s tuỳ "
        "thiết kế động cơ và cơ khí. Điều này dẫn tới dải thông của máy ghi phụ thuộc biên độ của "
        "vết: tần số –3 dB nằm trong khoảng 1 đến 5 Hz với chiều rộng toàn thang 200 đến 250 mm. "
        "Hoặc, người ta cho thời gian đáp ứng của bút với một bậc thang toàn thang (5 đến 95% vết "
        "toàn thang): 0,1 đến 0,5 s. Độ vọt lố của đáp ứng bậc thang của bút là cực nhỏ ở những thiết "
        "kế chính xác."))
    b.append(p(
        "Ở phần lớn máy ghi bút, mỗi vết có thể phủ hết chiều rộng. Như vậy các bút phải có khả năng "
        "vượt qua nhau, dẫn tới một dịch nhỏ giữa các bút liền kề (vài milimét) dọc theo trục thời "
        "gian. Ở một số thiết bị, có thể đồng bộ hoá các vết bằng hệ POC (“bù lệch bút”): tín hiệu "
        "được số hoá, lưu vào bộ nhớ và tái tạo sau một thời gian trễ bù cho dịch chuyển vật lý của "
        "bút. Nếu cần kiểm tra bằng mắt ngay thì việc áp dụng POC có thể bất tiện vì thời gian trễ "
        "này. Trong giám sát quá trình, người ta theo dõi các tín hiệu biến thiên chậm như nhiệt độ, "
        "áp suất, lưu lượng, v.v. Những tín hiệu này có thể được một đầu biến đổi duy nhất xử lý theo "
        "cách không liên tục; mọi tín hiệu vào được quét trong chu kỳ quét và mỗi tín hiệu được in "
        "một điểm (“máy ghi đa điểm”). Thời gian quét tối thiểu phụ thuộc cơ cấu ghi đang chuyển "
        "động. Để đẩy giấy, người ta dùng động cơ một chiều và động cơ bước. Giấy đã in thang chia "
        "được kéo bằng bánh răng châm vào các lỗ cách đều ở hai bên mép giấy. Máy ghi bút tịnh tiến "
        "trải từ thiết kế tương tự thuần tuý đơn giản đến các kiểu thông minh điều khiển bằng vi xử "
        "lý, đảm nhận số lượng lớn kênh với rất nhiều tiện ích điều khiển và giám sát (ví dụ in báo "
        "cáo sau khi có cảnh báo). Bảng 96.1 trình bày một tập máy ghi bút tịnh tiến; một số trong đó "
        "có đầu in. Ở cột “Mô tả” là ứng dụng chính: thử nghiệm và đo lường, hoặc giám sát quá trình. "
        "Ngoài ra còn chỉ ra: số kênh liên tục (c. ch.) và số kênh quét (s. ch.); sự có mặt của POC, "
        "máy in (để in thông tin bổ sung hoặc in vết), màn hiển thị thông tin chữ-số (như giá trị "
        "chuẩn cho từng kênh), hoặc thậm chí màn hiển thị dạng sóng, bộ nhớ dữ liệu (cho phép hoạt "
        "động như máy ghi bộ nhớ), khả năng ghi x–y, tạo cảnh báo (khi đạt ngưỡng của các biến được "
        "ghi), và các tuỳ chọn giao diện nối tiếp chuẩn cho phép trao đổi với PC (nạp cài đặt máy "
        "ghi, lưu trữ và xử lý dữ liệu đã ghi, v.v.). Bảng 96.2 tóm tắt các chỉ tiêu của máy ghi bút "
        "(kể cả kiểu đa điểm)."))
    b.append(table(*_t1("vi")))
    b.append(table(*_t2a("vi")))
    b.append(table(*_t2b("vi")))

    b.append(h3("Máy ghi dãy điểm nhiệt", "Thermal Dot Array Recorders"))
    b.append(p(
        "Ở máy ghi dãy điểm nhiệt, ngoài hệ kéo giấy, không có chi tiết chuyển động nào; đầu biến đổi "
        "ghi thực chất là một dãy thẳng hàng gồm các điểm ghi cách đều phủ kín toàn bộ chiều rộng tờ "
        "giấy. Tuy một số thiết bị dùng phương pháp tĩnh điện [1], người ta thường dùng giấy dãy điểm "
        "nhiệt và giấy cảm nhiệt. Trong dãy này, các ngòi ghi là những điện trở cỡ nhỏ được đốt nóng "
        "bằng điện; tính chất nhiệt của các điện trở (tiếp xúc chặt với giấy) và dạng xung kích hoạt "
        "bằng điện quyết định tần số ghi cực đại. Tần số này ở các máy ghi thời gian thực nằm trong "
        "khoảng 1 đến 6,4 kHz. Việc đốt nóng giấy cảm nhiệt tạo ra một điểm đen có độ ổn định dài hạn "
        "tốt. Xung đốt nóng được điều khiển theo vận tốc giấy để đạt độ đen đủ ở vận tốc cao. Độ đen "
        "của vết hoặc độ dày nét ít khi được dùng để nhận dạng đường cong; phần lớn người ta dùng "
        "chú thích chữ-số. Với dãy điểm, về lý thuyết có thể xử lý không hạn chế số dạng sóng; do đó "
        "thiết bị được lập trình để tự vẽ các đường chuẩn của nó. Người dùng có thể chọn các kiểu "
        "lưới khác nhau. Hơn nữa, có thể in thông tin chữ-số để chỉ rõ điều kiện thí nghiệm."))
    b.append(p(
        "Độ phân giải theo trục tung do dãy điểm quyết định: chủ yếu là 8 điểm/mm; đặc biệt có loại "
        "12 điểm/mm (như ở máy in laser thông thường). Độ phân giải dọc trục hoành phụ thuộc hạn chế "
        "của dãy nhiệt và việc lập trình. Nói chung người ta dùng độ phân giải cao hơn (phần lớn "
        "32 điểm/mm, tối đa 64 điểm/mm) trừ ở những vận tốc giấy cao nhất (100, 200, 500 mm/s). Ở "
        "những vận tốc cao này, thời gian tiếp xúc với giấy ngắn, nên điểm trở nên kém sắc và kém "
        "đen. Phần lớn các thiết bị dãy điểm dành cho ứng dụng tần số tín hiệu cao: tần số lấy mẫu "
        "mỗi kênh 100, 200 và thậm chí 500 kHz được dùng trong thời gian thực. Những tần số lấy mẫu "
        "này vượt xa tần số ghi; trong chu kỳ ghi, dữ liệu được lưu vào bộ nhớ và với mỗi kênh, trong "
        "mỗi khoảng ghi, người ta in một đường thẳng đứng bằng điểm giữa giá trị nhỏ nhất và lớn "
        "nhất. Ví dụ, một sóng sin có tần số vượt xa tần số ghi được biểu diễn thành một dải đen có "
        "bề rộng bằng biên độ của sin. Theo cách đó, đồ thị chỉ ra sự có mặt của một hiện tượng có "
        "thành phần tần số vượt quá tần số ghi. Vì dữ liệu được lưu trong bộ nhớ, chúng có thể được "
        "tái tạo ở tốc độ thấp hơn, nhờ vậy phơi ra dạng sóng tần số cao thực sự đã ghi được. Một số "
        "thiết bị dùng tốc độ lấy mẫu thấp hơn nhiều trong thời gian thực và chỉ thực hiện ngoại "
        "tuyến: khi đó thiết bị được gọi là máy ghi “bộ nhớ”. Độ chính xác số hoá từ 8 đến 16 bit, "
        "còn số điểm lớn nhất trên toàn thang là 4800. Theo cách này, tín hiệu hữu ích có thể chồng "
        "lên một thành phần một chiều lớn: nó có thể được ghi hoặc tái tạo với chất lượng đồ hoạ "
        "tuyệt vời sau khi đã loại bỏ thành phần một chiều bằng số và thích ứng thang đo."))
    b.append(p(
        "Ở một máy ghi hiệu năng cao, màn hiển thị dạng sóng cực kỳ hữu ích để tránh làm hỏng giấy, "
        "cả khi ghi thời gian thực lẫn khi ghi ngoại tuyến. Màn hiển thị cũng được dùng để cài đặt "
        "thiết bị. Tín hiệu có thể được chuẩn hoá và các giá trị vật lý thực cùng đơn vị có thể được "
        "in tại các đường chuẩn. Qua bộ nhớ có thể thu được đồ thị x–y. Một số thiết bị cho phép áp "
        "dụng các hàm toán học để xử lý và phân tích dạng sóng: dạng sóng gốc và dạng sóng đã xử lý "
        "có thể được vẽ cùng nhau ở chế độ ngoại tuyến. Một vài kiểu được trang bị phần mềm FFT. Giao "
        "tiếp máy tính, một tập lớn các chế độ kích hoạt (kể cả ghi ở vận tốc tăng sau một kích hoạt "
        "cụ thể), các kênh sự kiện, v.v. là những tiện ích chuẩn. Bảng 96.3 cho thấy một tập máy ghi "
        "dãy điểm nhiệt (ở cột “Mô tả”: số kênh tương tự (a. ch.) và kênh số (d. ch.); màn theo dõi "
        "dạng sóng; bộ nhớ dữ liệu tín hiệu, khả năng x–y, phân tích toán học, FFT) và Bảng 96.4 cho "
        "các chỉ tiêu kỹ thuật."))
    b.append(table(*_t3("vi")))
    b.append(table(*_t4a("vi")))
    b.append(table(*_t4b("vi")))

    b.append(h3("Nhận xét kết luận", "Concluding Remarks"))
    b.append(p(
        "Bảng 96.5 cho địa chỉ cùng số fax và điện thoại của các nhà chế tạo máy ghi được nhắc tới "
        "trong Bảng 96.1 và 96.3. Cần lưu ý rằng giá nêu trong các bảng đó là giá mua một thiết bị "
        "hoàn chỉnh đang hoạt động (với số kênh được chỉ ra) từ các hãng ở Bỉ đại diện cho nhà chế "
        "tạo và đã cung cấp các bảng dữ liệu mà từ đó các chỉ tiêu được rút ra. Với cụm “một thiết bị "
        "hoàn chỉnh đang hoạt động” là muốn nói một hệ chuẩn, tức là bao gồm các bộ ghép đầu vào đơn "
        "giản (trong trường hợp thiết kế mô-đun), RAM chuẩn và phần mềm phân tích, không có tuỳ chọn "
        "đặc biệt. Rõ ràng danh sách nhà chế tạo là không đầy đủ. Cần nhắc rằng số nhà chế tạo máy "
        "ghi đồ thị đang giảm; một phần đáng kể và ngày càng tăng các ứng dụng đã được các máy ghi "
        "“không giấy”, tức hệ thu thập dữ liệu, đảm nhận. Tuy vậy, khả năng tạo đồ thị trong thời "
        "gian thực vẫn là một đặc tính quan trọng, ví dụ để cung cấp bằng chứng về sự có mặt của một "
        "hiện tượng cụ thể. Những năm gần đây máy ghi tương tự ít được dùng và ít được chế tạo hơn "
        "(trừ kiểu bút tịnh tiến, đặc biệt trong giám sát quá trình công nghiệp). Máy ghi dãy nhiệt "
        "trở nên quan trọng hơn: chất lượng và độ ổn định dài hạn của giấy nhiệt đã được cải thiện và "
        "mức giá so sánh được với giấy in thang chia dùng cho ghi bằng mực. Ở các thiết kế mới, máy "
        "ghi cung cấp nhiều khả năng hơn và có vẻ thông minh hơn, rõ ràng dẫn tới những phức tạp gia "
        "tăng về cài đặt thiết bị và do đó nhu cầu đào tạo, kinh nghiệm sử dụng thiết bị cũng tăng."))
    b.append(table(*_t5("vi")))

    b.append(h3("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(dt("Máy ghi đồ thị tương tự (analog graphic recorder)",
                "máy ghi đồ thị dùng một hệ đầu biến đổi tương tự (ví dụ một bút chuyển động)."))
    b.append(dt("Dải thông của máy ghi tương tự (analog recorder bandwidth)",
                "tần số lớn nhất mà máy ghi tương tự xử lý được (giới hạn –3 dB)."))
    b.append(dt("Máy ghi đồ thị số (digital graphic recorder)",
                "máy ghi đồ thị dùng một hệ đầu biến đổi số (ví dụ một dãy điểm cố định)."))
    b.append(dt("Máy ghi đồ thị (graphic recorder)",
                "thiết bị đo tạo ra trong thời gian thực một bản sao cứng của một tập biến phụ thuộc "
                "thời gian."))
    b.append(dt("Tần số lấy mẫu cực đại (maximal sampling frequency)",
                "số điểm dữ liệu lớn nhất mà máy ghi số lấy mẫu được trong một đơn vị thời gian (tổng "
                "cộng hoặc theo từng kênh)."))
    b.append(dt("Tần số ghi cực đại (maximal writing frequency)",
                "số thao tác ghi (hoặc in) lớn nhất mà máy ghi số thực hiện được trong một đơn vị "
                "thời gian."))
    b.append(dt("Máy ghi dãy điểm nhiệt (thermal dot array recorder)",
                "máy ghi số dùng một dãy điểm nhiệt cố định vuông góc với trục thời gian."))
    b.append(dt("Máy ghi bút tịnh tiến (translational pen recorder)",
                "máy ghi tương tự có một hoặc nhiều bút tịnh tiến vuông góc với trục thời gian."))

    b.append(h3("Tài liệu tham khảo (96.1)", "References"))
    b.append(refs([
        "H. Vermariën, “Recorders, graphic,” trong J. G. Webster (chủ biên), "
        "<i>Encyclopedia of Medical Devices and Instrumentation</i>, New York: John Wiley &amp; Sons, "
        "1988.",
        "D. A. Bell, <i>Electronic Instrumentation and Measurements</i>, tái bản lần 2, Englewood "
        "Cliffs, NJ: Prentice-Hall, 1994.",
        "A. Miller, O. S. Talle và C. D. Mee, “Recorders,” trong B. M. Oliver và J. M. Cage (chủ biên), "
        "<i>Electronic Measurements and Instrumentation</i>, New York: McGraw-Hill, 1975, 427–479.",
        "R. J. Smith, <i>Circuits, Devices and Systems: A First Course in Electrical Engineering</i>, "
        "New York: John Wiley &amp; Sons, 1976.",
        "W. H. Olson, “Basic concepts in instrumentation,” trong J. G. Webster (chủ biên), "
        "<i>Medical Instrumentation: Application and Design</i>, tái bản lần 3, New York: John Wiley "
        "&amp; Sons, 1998.",
    ]))

    # ---------------------------------------------------------------- 96.2
    b.append(h2("96.2 Hệ thống thu thập dữ liệu", "Data Acquisition Systems"))
    b.append(p(
        "Nhiệm vụ cơ bản của một hệ thống thu thập dữ liệu là đo hoặc tạo ra các tín hiệu vật lý của "
        "thế giới thực. Trước khi một tín hiệu vật lý có thể được một hệ thống dựa trên máy tính đo, "
        "người ta dùng một cảm biến hay đầu biến đổi để chuyển tín hiệu vật lý thành tín hiệu điện, "
        "chẳng hạn điện áp hoặc dòng điện. Thường người ta chỉ coi một bo mạch thu thập dữ liệu (DAQ) "
        "cắm trong là hệ thống thu thập dữ liệu; tuy nhiên bo mạch chỉ là một trong các thành phần "
        "của hệ. Một hệ DAQ hoàn chỉnh gồm cảm biến, điều hoà tín hiệu, phần cứng giao tiếp và phần "
        "mềm. Khác với các dụng cụ độc lập, tín hiệu thường không thể nối trực tiếp vào bo mạch DAQ. "
        "Tín hiệu có thể cần được một phụ kiện điều hoà tín hiệu xử lý trước khi được bo mạch DAQ "
        "chuyển thành thông tin số. Phần mềm điều khiển hệ thu thập dữ liệu — thu dữ liệu thô, phân "
        "tích dữ liệu và trình bày kết quả. Các thành phần này được chỉ ra trên Hình 96.1."))
    b.append(fig(1, F.fig(1)))

    b.append(h3("Tín hiệu", "Signals"))
    b.append(p(
        "Tín hiệu là những sự kiện vật lý mà độ lớn hoặc sự biến thiên theo thời gian của chúng chứa "
        "thông tin. Hệ DAQ đo nhiều khía cạnh khác nhau của một tín hiệu để giám sát và điều khiển các "
        "sự kiện vật lý. Người dùng hệ DAQ cần biết quan hệ giữa tín hiệu với sự kiện vật lý và biết "
        "tín hiệu chứa những thông tin gì. Nói chung, thông tin được tín hiệu truyền tải qua một hoặc "
        "nhiều thông số sau: trạng thái, tốc độ, mức, dạng, hoặc nội dung tần số. Các đặc tính vật lý "
        "của tín hiệu đo được cùng thông tin liên quan giúp quyết định thiết kế của một hệ DAQ."))
    b.append(p(
        "Mọi tín hiệu, về bản chất, đều là tín hiệu tương tự biến thiên theo thời gian. Để thảo luận "
        "các phương pháp đo tín hiệu bằng một bo mạch DAQ cắm trong, nên phân một tín hiệu cho trước "
        "vào một trong năm kiểu tín hiệu. Vì phương pháp đo tín hiệu do cách tín hiệu truyền tải thông "
        "tin cần thiết quyết định, một cách phân loại dựa trên tiêu chí này rất hữu ích để hiểu các "
        "khối xây dựng cơ bản của một hệ DAQ."))
    b.append(p(
        "Như trên Hình 96.2, mọi tín hiệu nói chung có thể được phân thành tương tự hoặc số. Một tín "
        "hiệu số, hay nhị phân, chỉ có hai mức rời rạc đáng quan tâm — mức cao (đóng) và mức thấp "
        "(ngắt). Hai kiểu tín hiệu số là tín hiệu đóng–ngắt và tín hiệu chuỗi xung. Ngược lại, một tín "
        "hiệu tương tự chứa thông tin trong sự biến thiên liên tục của tín hiệu theo thời gian. Tín "
        "hiệu tương tự được mô tả trong miền thời gian hoặc miền tần số tuỳ theo thông tin quan tâm. "
        "Tín hiệu kiểu một chiều là tín hiệu tần số thấp, và nếu thông tin pha của tín hiệu được trình "
        "bày cùng thông tin tần số thì không có khác biệt giữa biểu diễn miền thời gian và miền tần "
        "số. Phạm trù mà một tín hiệu thuộc về phụ thuộc đặc tính của tín hiệu cần đo. Năm kiểu tín "
        "hiệu có thể được đặt song song chặt chẽ với năm kiểu thông tin cơ bản của tín hiệu — trạng "
        "thái, tốc độ, mức, dạng và nội dung tần số. Hiểu biết cơ bản về tín hiệu biểu diễn sự kiện "
        "vật lý đang được đo và điều khiển giúp chọn đúng hệ DAQ."))
    b.append(fig(2, F.fig(2)))

    b.append(h3("Bo mạch DAQ cắm trong", "Plug-In DAQ Boards"))
    b.append(p(
        "Thành phần cơ bản của một hệ DAQ là bo mạch DAQ cắm trong. Các bo mạch này cắm trực tiếp vào "
        "một khe của PC và có sẵn các đầu vào/ra (I/O) tương tự, số và định thời. Loại đa năng nhất "
        "trong các bo mạch DAQ cắm trong là bo mạch I/O đa chức năng. Như tên gọi, bo mạch này thường "
        "chứa nhiều tổ hợp khác nhau của bộ biến đổi tương tự–số (ADC), bộ biến đổi số–tương tự (DAC), "
        "các đường I/O số và các bộ đếm/bộ định thời. ADC và DAC lần lượt đo và tạo ra tín hiệu điện "
        "áp tương tự. Các đường I/O số cảm nhận và điều khiển tín hiệu số. Bộ đếm/bộ định thời đo tốc "
        "độ xung, độ rộng xung, thời gian trễ và tạo ra tín hiệu định thời. Những tính năng phong phú "
        "này khiến bo mạch DAQ đa chức năng hữu dụng cho một phạm vi ứng dụng rộng."))
    b.append(p(
        "Bo mạch đa chức năng thường được dùng để đo tín hiệu tương tự. Việc này do ADC thực hiện: nó "
        "chuyển mức điện áp tương tự thành một số mà máy tính hiểu được. Bộ dồn kênh tương tự (MUX), "
        "bộ khuếch đại đo, mạch lấy mẫu–giữ (S/H) và ADC hợp thành phần vào tương tự của một bo mạch "
        "đa chức năng (xem Hình 96.3)."))
    b.append(fig(3, F.fig(3)))
    b.append(p(
        "Thông thường bo mạch DAQ đa chức năng chỉ có một ADC. Dồn kênh là kỹ thuật phổ biến để đo "
        "nhiều kênh (nói chung 16 kênh đơn cực hoặc 8 kênh vi sai) bằng một ADC. MUX tương tự chuyển "
        "đổi giữa các kênh và đưa tín hiệu tới bộ khuếch đại đo và mạch S/H. Kiến trúc MUX là cách "
        "tiếp cận phổ biến nhất với bo mạch DAQ cắm trong. Trong khi bo mạch cắm trong thường chỉ có "
        "tối đa 16 đầu vào đơn cực hoặc 8 đầu vào vi sai, số kênh vào tương tự có thể được mở rộng "
        "thêm bằng các phụ kiện MUX ngoài."))
    b.append(p(
        "Bộ khuếch đại đo thường cho đầu vào vi sai và hệ số khuếch đại chọn được bằng jumper hoặc "
        "bằng phần mềm. Đầu vào vi sai loại bỏ các điện áp cách chung nhỏ. Hệ số khuếch đại thường "
        "lập trình được bằng phần mềm. Ngoài ra, nhiều bo mạch DAQ còn có khả năng thay đổi hệ số "
        "khuếch đại của bộ khuếch đại trong khi quét kênh ở tốc độ cao. Do đó có thể dễ dàng giám sát "
        "các tín hiệu có dải biên độ khác nhau. Đầu ra của bộ khuếch đại được mạch S/H lấy mẫu, hay "
        "giữ ở một điện áp không đổi, tại thời điểm đo để điện áp không thay đổi trong quá trình số "
        "hoá."))
    b.append(p(
        "ADC biến tín hiệu tương tự thành một giá trị số, giá trị này cuối cùng được gửi tới bộ nhớ "
        "máy tính. Có một số thông số quan trọng của việc biến đổi A/D. Thông số cơ bản của một ADC "
        "là số bit. Số bit của một bộ A/D quyết định dải giá trị của đầu ra nhị phân của phép biến "
        "đổi ADC. Ví dụ, nhiều ADC là 12 bit, nên một điện áp trong dải vào của ADC sẽ tạo ra một giá "
        "trị nhị phân nhận một trong 2<sup>12</sup> = 4096 giá trị khác nhau. ADC càng nhiều bit thì "
        "độ phân giải của phép đo càng cao. Độ phân giải quyết định mức thay đổi nhỏ nhất mà ADC phát "
        "hiện được. Độ phân giải thường được biểu thị bằng số chữ số của một vôn kế hoặc bằng dải "
        "động tính theo decibel, chứ không bằng bit. Bảng 96.6 cho quan hệ giữa số bit, số chữ số và "
        "dải động tính theo decibel."))
    b.append(table(*_t6("vi")))
    b.append(p(
        "Độ phân giải của phép biến đổi A/D còn do dải vào của ADC và hệ số khuếch đại quyết định. Bo "
        "mạch DAQ thường có một bộ khuếch đại đo khuếch đại tín hiệu tương tự với một hệ số trước khi "
        "biến đổi. Hệ số này khuếch đại các tín hiệu mức thấp để có thể đo chính xác hơn."))
    b.append(p(
        "Gộp lại, dải vào của ADC, hệ số khuếch đại và số bit của bo mạch quyết định độ phân giải nhỏ "
        "nhất của phép đo. Ví dụ, giả sử một tín hiệu mức thấp ±30 mV được thu bằng một ADC 12 bit có "
        "dải vào ±5 V. Nếu hệ có một bộ khuếch đại với hệ số 100, độ phân giải thu được của phép đo "
        "sẽ là dải/(hệ số × 2<sup>số bit</sup>) = độ phân giải, tức 10 V/(100 × 2<sup>12</sup>) = "
        "0,0244 mV."))
    b.append(p(
        "Cuối cùng, một thông số quan trọng của việc số hoá là tốc độ thực hiện các phép biến đổi "
        "A/D, gọi là tốc độ lấy mẫu. Hệ A/D phải lấy mẫu tín hiệu vào đủ nhanh để đo chính xác các "
        "thuộc tính quan trọng của dạng sóng. Để đáp ứng tiêu chí này, ADC phải có khả năng biến tín "
        "hiệu tương tự thành dạng số đủ nhanh."))
    b.append(p(
        "Khi quét nhiều kênh bằng một hệ DAQ dồn kênh, các yếu tố khác có thể ảnh hưởng tới thông "
        "lượng của hệ. Cụ thể, bộ khuếch đại đo phải xác lập được tới độ chính xác cần thiết trước "
        "khi phép biến đổi A/D xảy ra. Với tín hiệu đã dồn kênh, nhiều tín hiệu được chuyển vào một "
        "bộ khuếch đại đo. Phần lớn bộ khuếch đại, đặc biệt khi khuếch đại tín hiệu với hệ số lớn, sẽ "
        "không xác lập được tới độ chính xác đầy đủ của ADC khi quét kênh ở tốc độ cao. Để tránh tình "
        "trạng này, hãy tham khảo thời gian xác lập danh định của bo mạch DAQ ứng với các hệ số khuếch "
        "đại và tốc độ lấy mẫu mà ứng dụng yêu cầu."))

    b.append(h3("Các kiểu ADC", "Types of ADCs"))
    b.append(p(
        "Các bo mạch DAQ khác nhau dùng các kiểu ADC khác nhau để số hoá tín hiệu. Kiểu ADC phổ biến "
        "nhất trên bo mạch DAQ cắm trong là ADC xấp xỉ liên tiếp, vì nó cho tốc độ cao và độ phân giải "
        "cao với giá vừa phải."))
    b.append(p(
        "ADC kiểu dải con (còn gọi là bán flash) cho tốc độ biến đổi rất cao, với tốc độ lấy mẫu tới "
        "vài triệu mẫu mỗi giây."))
    b.append(p(
        "Công nghệ tiên tiến nhất trong ADC là ADC điều chế sigma–delta. Các ADC này lấy mẫu ở tốc độ "
        "cao, đạt được độ phân giải cao và có độ tuyến tính tốt nhất trong mọi ADC."))
    b.append(p(
        "ADC tích phân và ADC flash là những công nghệ đã chín muồi, vẫn còn được dùng trên bo mạch "
        "DAQ ngày nay. ADC tích phân số hoá được với độ phân giải cao nhưng phải hy sinh tốc độ lấy "
        "mẫu để có được nó. ADC flash đạt được tốc độ lấy mẫu cao nhất (cỡ gigahertz) nhưng chỉ có với "
        "độ phân giải thấp. Các kiểu ADC khác nhau được tóm tắt trong Bảng 96.7."))
    b.append(table(*_t7("vi")))

    b.append(h3("Kiến trúc đầu vào tương tự", "Analog Input Architecture"))
    b.append(p(
        "Với một bo mạch DAQ điển hình, bộ dồn kênh chuyển đổi giữa các kênh vào tương tự. Tín hiệu "
        "tương tự trên kênh được bộ dồn kênh chọn sau đó đi tới bộ khuếch đại đo có hệ số khuếch đại "
        "lập trình được (PGIA) để được khuếch đại. Sau khi tín hiệu được khuếch đại, mạch lấy mẫu và "
        "giữ (S/H) giữ tín hiệu tương tự không đổi để ADC xác định biểu diễn số của tín hiệu tương tự. "
        "Một bo mạch DAQ tốt sau đó sẽ đặt tín hiệu số vào một bộ đệm vào trước ra trước (FIFO), để "
        "không mất dữ liệu nếu mẫu không thể chuyển ngay qua kênh I/O của PC tới bộ nhớ máy tính. Có "
        "FIFO trở nên đặc biệt quan trọng khi bo mạch chạy dưới các hệ điều hành có độ trễ ngắt lớn, "
        "như Microsoft Windows."))

    b.append(h3("Các chỉ tiêu tương tự cơ bản", "Basic Analog Specifications"))
    b.append(p(
        "Hầu như mọi bảng dữ liệu bo mạch DAQ đều nêu số kênh, tốc độ lấy mẫu cực đại, độ phân giải "
        "và dải vào cùng hệ số khuếch đại."))
    b.append(p(
        "Số kênh, do bộ dồn kênh quyết định, thường được nêu ở hai dạng — vi sai và đơn cực. Đầu vào "
        "vi sai là đầu vào có điểm tham chiếu khác nhau cho mỗi kênh, và không kênh nào được bo mạch "
        "nối đất. Đầu vào vi sai là cách tốt nhất để nối tín hiệu vào bo mạch DAQ vì chúng chống nhiễu "
        "tốt nhất."))
    b.append(p(
        "Đầu vào đơn cực là đầu vào được tham chiếu tới một điểm nối đất chung. Vì đầu vào đơn cực "
        "được tham chiếu tới một đất chung, chúng không loại nhiễu tốt bằng đầu vào vi sai. Tuy vậy "
        "chúng có số kênh nhiều hơn. Đầu vào đơn cực được dùng khi tín hiệu vào có mức cao (lớn hơn "
        "1 V), dây dẫn từ nguồn tín hiệu tới phần cứng vào tương tự ngắn (dưới 5 m), và mọi tín hiệu "
        "vào dùng chung một tham chiếu."))
    b.append(p(
        "Một số bo mạch có đầu vào tựa vi sai, trong đó mọi đầu vào được tham chiếu tới cùng một điểm "
        "chung — như đầu vào đơn cực — nhưng điểm chung này không được tham chiếu tới đất. Những bo "
        "mạch này có ưu điểm là số kênh vào nhiều như đầu vào đơn cực, và có khả năng loại bỏ một "
        "phần nhiễu cách chung, đặc biệt nếu nhiễu cách chung là như nhau trên mọi kênh. Tuy vậy, đầu "
        "vào vi sai vẫn tốt hơn tựa vi sai, vì vi sai chống nhiễu từ tốt hơn."))
    b.append(p(
        "Tốc độ lấy mẫu quyết định tốc độ tín hiệu tương tự được chuyển thành tín hiệu số. Khi đo tín "
        "hiệu xoay chiều, hãy lấy mẫu nhanh ít nhất hai lần tần số cao nhất của tín hiệu vào. Ngay cả "
        "khi đo tín hiệu một chiều, hãy lấy mẫu vượt và lấy trung bình dữ liệu để tăng độ chính xác "
        "của tín hiệu bằng cách giảm ảnh hưởng của nhiễu."))
    b.append(p(
        "Nếu sự kiện vật lý gồm nhiều tín hiệu kiểu một chiều, nên dùng một bo mạch DAQ có chức năng "
        "quét theo khoảng. Với quét theo khoảng, mọi kênh được quét trong một khoảng lấy mẫu (thường "
        "là tốc độ nhanh nhất của bo mạch), với khoảng thứ hai (thường chậm) quyết định thời gian "
        "trước khi lặp lại lần quét. Quét theo khoảng cho hiệu ứng lấy mẫu đồng thời đối với các tín "
        "hiệu biến thiên chậm mà không cần thêm chi phí cho mạch vào phục vụ lấy mẫu đồng thời thực "
        "sự."))
    b.append(p(
        "Độ phân giải là số bit dùng để biểu diễn tín hiệu tương tự. Độ phân giải càng cao thì dải vào "
        "càng được chia thành nhiều mức hơn, và do đó điện áp nhỏ nhất có thể phát hiện được càng nhỏ. "
        "Đáng tiếc, một số chỉ tiêu DAQ gây hiểu nhầm khi nêu độ phân giải gắn với bo mạch DAQ. Nhiều "
        "chỉ tiêu bo mạch DAQ nêu độ phân giải của ADC mà không nêu độ tuyến tính và nhiễu, và do đó "
        "không cho thông tin cần thiết để xác định độ phân giải của toàn bo mạch. Độ phân giải của "
        "ADC, kết hợp với thời gian xác lập, độ phi tuyến tích phân (INL), độ phi tuyến vi sai (DNL) "
        "và nhiễu, sẽ cho hiểu biết về độ chính xác của bo mạch."))
    b.append(p(
        "Dải vào và hệ số khuếch đại quyết định mức tín hiệu nên nối vào bo mạch. Thường dải và hệ số "
        "khuếch đại được nêu riêng, nên phải kết hợp hai thứ để xác định dải vào tín hiệu thực tế:"))
    b.append(eq("dải vào tín hiệu = dải / hệ số khuếch đại"))
    b.append(p(
        "Ví dụ, một bo mạch dùng dải vào ±10 V với hệ số khuếch đại 2 sẽ có dải vào tín hiệu ±5 V. Dải "
        "vào tín hiệu càng gần dải của tín hiệu thì kết quả đọc từ bo mạch DAQ càng chính xác. Nếu "
        "các tín hiệu có dải vào khác nhau, hãy dùng một bo mạch DAQ có tính năng hệ số khuếch đại "
        "riêng cho từng kênh."))

    b.append(h3("Phần mềm thu thập dữ liệu", "Data Acquisition Software"))
    b.append(p(
        "Phần mềm thường là thành phần then chốt nhất của hệ DAQ. Người dùng hệ DAQ thường lập trình "
        "phần cứng theo một trong hai cách — qua lập trình thanh ghi hoặc qua trình điều khiển thiết "
        "bị cấp cao."))

    b.append(h4("Lập trình bo mạch ở mức thanh ghi", "Board Register-Level Programming"))
    b.append(p(
        "Lựa chọn thứ nhất là không dùng phần mềm do nhà cung cấp và lập trình bo mạch DAQ ở mức phần "
        "cứng. Bo mạch DAQ thường dựa trên thanh ghi; nghĩa là chúng có một số thanh ghi số điều khiển "
        "hoạt động của bo mạch. Người phát triển có thể dùng bất kỳ ngôn ngữ lập trình chuẩn nào, như "
        "C, C++ hay Visual BASIC, để ghi một chuỗi mã nhị phân vào bo mạch DAQ nhằm điều khiển hoạt "
        "động của nó. Tuy phương pháp này cho mức linh hoạt cao nhất, nó cũng khó nhất và tốn thời "
        "gian nhất, đặc biệt với người lập trình thiếu kinh nghiệm. Người lập trình phải biết chi tiết "
        "việc lập trình mọi phần cứng, gồm bo mạch, bộ điều khiển ngắt của PC, bộ điều khiển DMA và "
        "bộ nhớ PC."))

    b.append(h4("Phần mềm trình điều khiển", "Driver Software"))
    b.append(p(
        "Phần mềm trình điều khiển thường gồm một thư viện các lời gọi hàm dùng được từ một ngôn ngữ "
        "lập trình chuẩn. Các lời gọi hàm này cung cấp một giao diện cấp cao để điều khiển các chức "
        "năng chuẩn của bo mạch cắm trong. Ví dụ, một hàm tên SCAN_OP có thể cấu hình, khởi phát và "
        "hoàn tất một thao tác DAQ quét nhiều kênh với số điểm định trước. Lời gọi hàm sẽ gồm các "
        "tham số chỉ ra kênh cần quét, hệ số khuếch đại cần dùng, tốc độ lấy mẫu và tổng số điểm dữ "
        "liệu cần thu. Trình điều khiển đáp ứng lời gọi hàm duy nhất này bằng cách lập trình bo mạch "
        "cắm trong, bộ điều khiển DMA, bộ điều khiển ngắt và CPU để quét các kênh như yêu cầu."))

    b.append(h3("Lấy mẫu số là gì?", "What Is Digital Sampling?"))
    b.append(p(
        "Mọi hệ DAQ đều có nhiệm vụ thu thập thông tin về các tín hiệu tương tự. Để làm việc đó, hệ "
        "ghi lại một chuỗi “ảnh chụp” tức thời — các mẫu — của tín hiệu tại những khoảng thời gian xác "
        "định. Mỗi mẫu chứa thông tin về tín hiệu tại một thời điểm cụ thể. Biết chính xác thời điểm "
        "của mỗi phép biến đổi và giá trị của mẫu, có thể tái tạo, phân tích và hiển thị dạng sóng đã "
        "số hoá."))

    b.append(h3("Kỹ thuật lấy mẫu thời gian thực", "Real-Time Sampling Techniques"))
    b.append(p(
        "Trong lấy mẫu thời gian thực, bo mạch DAQ số hoá các mẫu liên tiếp dọc theo tín hiệu (Hình "
        "96.4). Theo định lý lấy mẫu Nyquist, ADC phải lấy mẫu với tốc độ ít nhất gấp hai lần thành "
        "phần tần số lớn nhất trong tín hiệu đó để tránh chồng phổ. Chồng phổ là một thành phần tần "
        "số thấp giả tạo xuất hiện trong dữ liệu đã lấy mẫu thu được với tốc độ lấy mẫu quá thấp. Tần "
        "số bằng một nửa tần số lấy mẫu được gọi là tần số Nyquist. Về lý thuyết, có thể khôi phục "
        "thông tin về những tín hiệu có tần số bằng hoặc dưới tần số Nyquist. Các tần số trên tần số "
        "Nyquist sẽ chồng phổ để xuất hiện trong khoảng từ một chiều tới tần số Nyquist."))
    b.append(fig(4, F.fig(4)))
    b.append(p(
        "Ví dụ, giả sử tần số lấy mẫu f<sub>s</sub> là 100 Hz. Cũng giả sử tín hiệu vào cần lấy mẫu "
        "chứa các tần số sau — 25, 70, 160 và 510 Hz. Hình 96.5 cho biểu diễn phổ của tín hiệu vào."))
    b.append(fig(5, F.fig(5)))
    b.append(p(
        "Toán học của lý thuyết lấy mẫu cho ta biết rằng một tín hiệu đã lấy mẫu bị dịch trong miền "
        "tần số một lượng bằng bội số nguyên của tần số lấy mẫu f<sub>s</sub>. Hình 96.6 cho nội dung "
        "phổ của tín hiệu vào sau khi lấy mẫu. Các tần số dưới 50 Hz — tần số Nyquist "
        "(f<sub>s</sub>/2) — xuất hiện đúng. Tuy nhiên, các tần số trên Nyquist xuất hiện dưới dạng "
        "ảnh (alias) bên dưới tần số Nyquist. Ví dụ, F1 xuất hiện đúng; nhưng F2, F3 và F4 có ảnh lần "
        "lượt tại 30, 40 và 10 Hz."))
    b.append(fig(6, F.fig(6)))
    b.append(p("Tần số thu được của tín hiệu bị chồng phổ có thể tính bằng công thức sau:"))
    b.append(eq("Tần số biểu kiến (ảnh) = |Bội số nguyên gần nhất của tần số lấy mẫu − Tần số vào|"))
    b.append(p("Với ví dụ ở Hình 96.5 và 96.6:"))
    b.append(eq("Ảnh của F2 = |100 − 70| = 30 Hz"))
    b.append(eq("Ảnh của F3 = |(2)100 − 160| = 40 Hz"))
    b.append(eq("Ảnh của F4 = |(5)100 − 510| = 10 Hz"))

    b.append(h3("Chống chồng phổ", "Preventing Aliasing"))
    b.append(p(
        "Có thể chống chồng phổ bằng cách dùng bộ lọc ở đầu vào của hệ DAQ. Các bộ lọc chống chồng "
        "phổ này được đặt để cắt mọi tần số trên tần số Nyquist (một nửa tốc độ lấy mẫu). Bộ lọc lý "
        "tưởng sẽ loại mọi tần số trên Nyquist; tuy nhiên, vì bộ lọc lý tưởng chỉ có trong sách giáo "
        "khoa, người ta phải thoả hiệp giữa tốc độ lấy mẫu và việc chọn bộ lọc. Trong nhiều ứng dụng, "
        "bộ lọc thụ động một hoặc hai cực là đủ. Quy tắc kinh nghiệm là lấy mẫu vượt (5 đến 10 lần) và "
        "dùng các bộ lọc chống chồng phổ này khi thông tin tần số là then chốt."))
    b.append(p(
        "Hoặc có thể dùng bộ lọc chống chồng phổ tích cực với tần số cắt lập trình được và độ suy giảm "
        "rất dốc đối với các tần số trên tần số cắt. Vì các bộ lọc này có độ dốc rất dựng đứng, hệ DAQ "
        "có thể lấy mẫu ở hai đến ba lần tần số cắt của bộ lọc. Hình 96.7 cho hàm truyền của một bộ "
        "lọc chống chồng phổ chất lượng cao."))
    b.append(fig(7, F.fig(7)))
    b.append(p(
        "Máy tính dùng các giá trị số để tái tạo hoặc phân tích dạng sóng. Vì tín hiệu có thể là bất "
        "kỳ giá trị nào giữa hai mẫu, bo mạch DAQ có thể không biết về những thay đổi của tín hiệu "
        "giữa các mẫu. Có nhiều phương pháp lấy mẫu được tối ưu cho các lớp dữ liệu khác nhau; chúng "
        "gồm thăm dò bằng phần mềm, lấy mẫu ngoài, quét liên tục, quét đa tốc độ, lấy mẫu đồng thời, "
        "quét theo khoảng và thay đổi tốc độ lấy mẫu liên tục."))

    b.append(h3("Thăm dò bằng phần mềm", "Software Polling"))
    b.append(p(
        "Một vòng lặp phần mềm thăm dò một tín hiệu định thời và khởi phát phép biến đổi A/D bằng một "
        "lệnh phần mềm khi phát hiện sườn của tín hiệu định thời. Tín hiệu định thời có thể xuất phát "
        "từ đồng hồ trong của máy tính hoặc từ một đồng hồ trên bo mạch DAQ. Thăm dò bằng phần mềm hữu "
        "ích trong các ứng dụng đơn giản, tốc độ thấp, như đo nhiệt độ."))
    b.append(p(
        "Vòng lặp phần mềm phải đủ nhanh để phát hiện tín hiệu định thời và kích phép biến đổi. Nếu "
        "không, sẽ tồn tại một cửa sổ bất định, còn gọi là jitter, giữa hai mẫu liên tiếp. Trong cửa "
        "sổ bất định đó, dạng sóng vào có thể thay đổi đủ để làm giảm mạnh độ chính xác của ADC."))
    b.append(p(
        "Giả sử một sóng sin 100 Hz, toàn thang 10 V được số hoá (Hình 96.8). Nếu vòng lặp thăm dò mất "
        "5 ms để phát hiện tín hiệu định thời và kích phép biến đổi, thì điện áp của sóng sin vào sẽ "
        "thay đổi tới 31 mV, [ΔV = 10 sin(2π × 100 × 5 × 10<sup>–6</sup>)]. Với một ADC 12 bit làm "
        "việc trên dải vào 10 V và hệ số khuếch đại 1, một bit có nghĩa nhỏ nhất (LSB) của sai số ứng "
        "với 2,44 mV:"))
    b.append(fig(8, F.fig(8)))
    b.append(eq("dải vào/(hệ số khuếch đại × 2<sup>12</sup>) = 10/(1 × 2<sup>12</sup>) = 2,44 mV"))
    b.append(p(
        "Nhưng vì sai số điện áp do jitter là 31 mV, sai số chính xác là 13 LSB."))
    b.append(eq("31 mV / 2,44 mV = 13 LSB"))
    b.append(p(
        "Điều này thể hiện sự bất định trong 4 bit cuối của một ADC 12 bit. Như vậy độ chính xác hiệu "
        "dụng của hệ không còn là 12 bit nữa mà chỉ còn 8 bit."))

    b.append(h3("Lấy mẫu ngoài", "External Sampling"))
    b.append(p(
        "Một số ứng dụng DAQ phải thực hiện phép biến đổi dựa trên một sự kiện vật lý khác kích hoạt "
        "việc biến đổi dữ liệu. Sự kiện đó có thể là một xung từ một bộ mã hoá quang đo chuyển động "
        "quay của một xi lanh. Mỗi lần bộ mã hoá tạo ra một xung ứng với n độ quay thì lấy một mẫu. "
        "Kích hoạt ngoài có lợi khi cần đo những tín hiệu mà sự xuất hiện của chúng gắn với một hiện "
        "tượng vật lý khác."))

    b.append(h3("Quét liên tục", "Continuous Scanning"))
    b.append(p(
        "Khi một bo mạch DAQ thu dữ liệu, nhiều thành phần trên bo mạch chuyển tín hiệu tương tự thành "
        "một giá trị số. Các thành phần này gồm MUX tương tự, bộ khuếch đại đo, mạch S/H và ADC. Khi "
        "thu dữ liệu từ nhiều kênh vào, MUX tương tự nối từng tín hiệu tới ADC với tốc độ không đổi. "
        "Phương pháp này, gọi là quét liên tục, rẻ hơn đáng kể so với việc có một bộ khuếch đại và một "
        "ADC riêng cho mỗi kênh vào."))
    b.append(p(
        "Quét liên tục có lợi vì nó loại bỏ jitter và dễ thực hiện. Tuy nhiên, không thể lấy mẫu nhiều "
        "kênh đồng thời. Vì MUX chuyển đổi giữa các kênh, một độ lệch thời gian xuất hiện giữa hai "
        "mẫu kênh liên tiếp bất kỳ. Quét liên tục thích hợp cho những ứng dụng mà quan hệ thời gian "
        "giữa các điểm lấy mẫu là không quan trọng, hoặc độ lệch là tương đối không đáng kể so với "
        "tốc độ quét kênh."))
    b.append(p(
        "Nếu các mẫu từ hai tín hiệu được dùng để tạo ra một giá trị thứ ba, thì quét liên tục có thể "
        "dẫn tới sai số đáng kể nếu độ lệch thời gian lớn. Trên Hình 96.9, hai kênh được lấy mẫu liên "
        "tục và cộng lại để tạo ra một giá trị thứ ba. Vì hai sóng sin lệch pha 90°, tổng của các tín "
        "hiệu đáng lẽ luôn bằng không. Nhưng vì có thời gian lệch giữa các mẫu, kết quả là một tín "
        "hiệu răng cưa sai."))
    b.append(fig(9, F.fig(9)))

    b.append(h3("Quét đa tốc độ", "Multirate Scanning"))
    b.append(p(
        "Quét đa tốc độ, một phương pháp quét nhiều kênh ở các tốc độ quét khác nhau, là trường hợp "
        "riêng của quét liên tục. Những ứng dụng số hoá nhiều tín hiệu với nhiều tần số khác nhau dùng "
        "quét đa tốc độ để giảm thiểu dung lượng bộ đệm cần để lưu các tín hiệu đã lấy mẫu. Để thực "
        "hiện quét đa tốc độ bằng phần cứng, người ta dùng các ADC độc lập cho từng kênh; tuy nhiên "
        "phương pháp này cực kỳ đắt. Thay vì nhiều ADC, chỉ một ADC được dùng. Một thanh ghi cấu hình "
        "kênh/hệ số khuếch đại lưu tốc độ quét cho mỗi kênh và phần mềm chia nhỏ xung đồng hồ quét dựa "
        "trên tốc độ quét của từng kênh. Quét đa tốc độ điều khiển bằng phần mềm hoạt động bằng cách "
        "lấy mẫu mỗi kênh vào ở tốc độ là một phần của tốc độ quét danh định."))
    b.append(p(
        "Giả sử hệ quét các kênh 0 đến 3 ở 10 kS/s, kênh 4 ở 5 kS/s và các kênh 5 đến 7 ở 1 kS/s. Nên "
        "dùng tốc độ quét cơ sở 10 kS/s. Các kênh 0 đến 3 được thu ở tốc độ quét cơ sở. Phần mềm và "
        "phần cứng chia tốc độ quét cơ sở cho 2 để lấy mẫu kênh 4 ở 5 kS/s, và cho 10 để lấy mẫu các "
        "kênh 5 đến 7 ở 1 kS/s."))

    b.append(h3("Lấy mẫu đồng thời", "Simultaneous Sampling"))
    b.append(p(
        "Với những ứng dụng mà quan hệ thời gian giữa các tín hiệu vào là quan trọng, như phân tích "
        "pha của tín hiệu xoay chiều, phải dùng lấy mẫu đồng thời. Bo mạch DAQ có khả năng lấy mẫu "
        "đồng thời thường dùng bộ khuếch đại đo và mạch S/H độc lập cho mỗi kênh vào, cùng một MUX "
        "tương tự định tuyến các tín hiệu vào tới ADC để biến đổi (như trên Hình 96.10)."))
    b.append(fig(10, F.fig(10)))
    b.append(p(
        "Để chứng minh nhu cầu về một bo mạch DAQ lấy mẫu đồng thời, hãy xét một hệ gồm bốn tín hiệu "
        "50 kHz được lấy mẫu ở 200 kS/s. Nếu bo mạch DAQ dùng quét liên tục, độ lệch giữa mỗi kênh là "
        "5 µs (1/200 kS/s), tương ứng một dịch pha 270° [(15 µs/20 µs) × 360°] giữa kênh thứ nhất và "
        "kênh thứ tư. Ngược lại, với một bo mạch lấy mẫu đồng thời có độ lệch thời gian giữa các kênh "
        "tối đa 5 ns, dịch pha chỉ còn 0,09° [(5 ns/20 µs) × 360°]. Hiện tượng này được minh hoạ trên "
        "Hình 96.11."))
    b.append(fig(11, F.fig(11)))

    b.append(h3("Quét theo khoảng", "Interval Scanning"))
    b.append(p(
        "Với tín hiệu tần số thấp, quét theo khoảng tạo ra hiệu ứng lấy mẫu đồng thời mà vẫn giữ được "
        "lợi ích về chi phí của một hệ quét liên tục. Phương pháp này quét các kênh vào ở một tốc độ "
        "và dùng tốc độ thứ hai để điều khiển thời điểm bắt đầu lần quét tiếp theo. Nếu các kênh vào "
        "được quét ở tốc độ nhanh nhất của ADC, sẽ tạo ra hiệu ứng lấy mẫu đồng thời các kênh. Quét "
        "theo khoảng thích hợp cho các tín hiệu chuyển động chậm, như nhiệt độ và áp suất. Quét theo "
        "khoảng cho tốc độ lấy mẫu không jitter và thời gian lệch giữa các mẫu kênh là tối thiểu. Ví "
        "dụ, xét một hệ DAQ có mười tín hiệu nhiệt độ. Bằng cách dùng quét theo khoảng, có thể đặt một "
        "bo mạch DAQ quét mọi kênh với độ trễ giữa các kênh là 5 µs, rồi lặp lại lần quét mỗi giây. "
        "Phương pháp này tạo hiệu ứng lấy mẫu đồng thời mười kênh ở 1 S/s, như trên Hình 96.12."))
    b.append(fig(12, F.fig(12)))
    b.append(p(
        "Để minh hoạ khác biệt giữa quét liên tục và quét theo khoảng, hãy xét một ứng dụng giám sát "
        "mômen và tốc độ vòng quay (RPM) của động cơ ô tô và tính công suất động cơ. Hai tín hiệu, tỉ "
        "lệ với mômen và RPM, được một bo mạch DAQ lấy mẫu dễ dàng ở tốc độ 1000 S/s. Các giá trị được "
        "nhân với nhau để xác định công suất như một hàm của thời gian."))
    b.append(p(
        "Một bo mạch DAQ quét liên tục phải lấy mẫu với tổng tốc độ 2000 S/s. Thời gian giữa lúc lấy "
        "mẫu tín hiệu mômen và lúc lấy mẫu tín hiệu RPM sẽ luôn là 0,5 ms (1/2000). Nếu một trong hai "
        "tín hiệu thay đổi trong 0,5 ms đó, công suất tính được là sai. Nhưng dùng quét theo khoảng ở "
        "tốc độ 1000 S/s, bo mạch DAQ lấy mẫu tín hiệu mômen mỗi 1 ms, và tín hiệu RPM được lấy mẫu "
        "nhanh nhất có thể sau khi mômen được lấy mẫu. Nếu độ trễ giữa các kênh là 5 µs giữa mẫu mômen "
        "và mẫu RPM, thì độ lệch thời gian giảm 99% [(0,5 ms − 5 µs)/0,5 ms], và khả năng tính sai "
        "cũng giảm đi."))

    b.append(h3("Các yếu tố ảnh hưởng tới độ chính xác của phép đo",
                "Factors Influencing the Accuracy of Measurements"))
    b.append(p(
        "Làm sao xác định được một bo mạch DAQ cắm trong có cho kết quả đo cần thiết hay không? Với "
        "một thiết bị đo tinh vi như bo mạch DAQ cắm trong, độ chính xác thu được có thể khác nhau rất "
        "nhiều tuỳ kiểu bo mạch dùng. Ví dụ, có thể mua trên thị trường hôm nay những sản phẩm DAQ có "
        "ADC 16 bit mà chỉ cho dưới 12 bit dữ liệu hữu ích, hoặc mua một sản phẩm có ADC 16 bit và "
        "thực sự có 16 bit dữ liệu hữu ích. Sự khác biệt về độ chính xác này gây lúng túng trong ngành "
        "công nghiệp PC, nơi mọi người quen với việc thay PC, card đồ hoạ, máy in, v.v. và vẫn thấy "
        "kết quả tương tự giữa các thiết bị."))
    b.append(p(
        "Việc quan trọng nhất là phải xem xét kỹ nhiều chỉ tiêu hơn là chỉ độ phân giải của ADC dùng "
        "trên bo mạch DAQ. Với các phép đo kiểu một chiều, nên xét ít nhất thời gian xác lập của bộ "
        "khuếch đại đo, DNL, độ chính xác tương đối, INL và nhiễu. Nếu nhà chế tạo bo mạch đang xét "
        "không cung cấp những chỉ tiêu này trong bảng dữ liệu, hãy đề nghị nhà cung cấp cung cấp chúng "
        "hoặc chạy thử nghiệm để xác định các chỉ tiêu đó."))

    b.append(h3("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(dt("Ảnh (alias)",
                "một thành phần tần số thấp giả tạo xuất hiện trong dữ liệu đã lấy mẫu thu được với "
                "tốc độ lấy mẫu quá thấp."))
    b.append(dt("Không đồng bộ (asynchronous)",
                "(1) Phần cứng — tính chất của một sự kiện xảy ra ở thời điểm tuỳ ý, không đồng bộ "
                "với một đồng hồ tham chiếu. (2) Phần mềm — tính chất của một hàm bắt đầu một thao tác "
                "và trả về trước khi thao tác hoàn tất hoặc kết thúc."))
    b.append(dt("Thời gian biến đổi (conversion time)",
                "thời gian cần thiết, trong một hệ vào hoặc ra tương tự, từ lúc một kênh được hỏi "
                "(ví dụ bằng một lệnh đọc) tới lúc có dữ liệu chính xác."))
    b.append(dt("DAQ (thu thập dữ liệu)",
                "(1) Thu và đo các tín hiệu điện từ cảm biến, đầu biến đổi và đầu dò hay giá thử rồi "
                "đưa vào máy tính để xử lý. (2) Thu và đo cùng loại tín hiệu điện đó bằng các bo mạch "
                "ADC và/hoặc DIO cắm trong PC, và có thể tạo tín hiệu điều khiển bằng các bo mạch DAC "
                "và/hoặc DIO trong cùng PC."))
    b.append(dt("DNL (độ phi tuyến vi sai)",
                "thước đo tính bằng LSB độ lệch xấu nhất của độ rộng mã so với giá trị lý tưởng "
                "1 LSB."))
    b.append(dt("INL (độ phi tuyến tích phân)",
                "thước đo tính bằng LSB độ lệch xấu nhất so với đặc tuyến truyền A/D hoặc D/A lý "
                "tưởng của mạch vào/ra tương tự."))
    b.append(dt("Định lý lấy mẫu Nyquist",
                "một định luật của lý thuyết lấy mẫu, phát biểu rằng nếu một tín hiệu liên tục giới "
                "hạn băng tần không chứa thành phần tần số nào cao hơn một nửa tần số lấy mẫu thì tín "
                "hiệu gốc có thể được khôi phục không méo."))
    b.append(dt("Độ chính xác tương đối (relative accuracy)",
                "thước đo tính bằng LSB độ chính xác của một ADC. Nó bao gồm mọi sai số phi tuyến và "
                "lượng tử hoá. Nó không bao gồm sai số lệch không và hệ số khuếch đại của mạch cấp "
                "tín hiệu cho ADC."))

    b.append(h3("Thông tin thêm", "Further Information"))
    b.append(refs([
        "R. House, “Understanding Important DA Specifications,” <i>Sensors</i>, 10(10), tháng 6, 1993.",
        "R. House, “Understanding Inaccuracies Due to Settling Time, Linearity, and Noise,” "
        "<i>National Instruments European User Symposium Proceedings</i>, 10–11 tháng 11, 1994, "
        "11–12.",
        "E. McConnell, “PC-Based Data Acquisition Users Face Numerous Challenges,” <i>ECN</i>, "
        "tháng 8, 1994.",
        "E. McConnell, “Choosing a Data-Acquisition Method,” <i>Electronic Design</i>, 43(6), 147, "
        "1995.",
        "E. McConnell và D. Jernigan, “Data Acquisition,” trong J. C. Whitaker (chủ biên), "
        "<i>The Electronics Handbook</i>, Boca Raton, FL: CRC Press, 1996, 1795–1822.",
        "D. Potter và A. Razdan, “Fundamentals of PC-Based Data Acquisition,” <i>Sensors</i>, 11(2), "
        "12–20, tháng 2, 1994.",
        "D. Potter, “Sensor to PC — Avoiding Some Common Pitfalls,” <i>Sensors Expo Proceedings</i>, "
        "20 tháng 9, 1994.",
        "D. Potter, “Signal Conditioners Expand DAQ System Capabilities,” <i>I&amp;CS</i>, 25–33, "
        "tháng 8, 1995.",
        "G. W. Johnson, <i>LabVIEW Graphical Programming</i>, New York: McGraw-Hill, 1994.",
        "E. McConnell, “New Achievements in Counter/Timer Data Acquisition Technology,” "
        "<i>MessComp 1994 Proceedings</i>, 13–15 tháng 9, 1994, 492–498.",
        "E. McConnell, “Equivalent Time Sampling Extends DA Performance,” <i>Sensors Data "
        "Acquisition</i>, số đặc biệt, 13 tháng 6, 1995.",
    ]))

    # ---------------------------------------------------------------- 96.3
    b.append(h2("96.3 Máy ghi từ và quang", "Magnetic and Optical Recorders"))
    b.append(p(
        "Trọng tâm của công nghệ ghi là quá trình lưu trữ và truy xuất thông tin. Ngoài tầm quan trọng "
        "hiển nhiên trong nhiều ngành khoa học và kỹ thuật khác nhau, nó đã trở nên không thể thiếu "
        "trong đời sống hằng ngày của chúng ta. Khi ta thực hiện một giao dịch ngân hàng, đặt vé máy "
        "bay, dùng thẻ tín dụng, xem phim từ băng video hay nghe nhạc từ đĩa CD, ta đang dùng công nghệ "
        "ghi. Những yêu cầu chung đối với việc ghi là tính toàn vẹn thông tin, truy xuất nhanh và giá "
        "thành thấp. Trong các kỹ thuật khác nhau, những kỹ thuật được dùng phổ biến nhất là ghi từ và "
        "ghi quang."))
    b.append(p(
        "Thiết bị ghi điển hình gồm một đầu đọc/ghi, một môi trường, một hệ mã hoá/giải mã, một hệ truy "
        "xuất dữ liệu và một số thành phần cơ khí, điện tử phụ trợ. Đầu từ và môi trường dùng để lưu "
        "trữ và truy xuất dữ liệu, còn hệ mã hoá/giải mã dùng để sửa lỗi dữ liệu. Hệ truy xuất dữ liệu "
        "thay đổi vị trí tương đối giữa đầu từ và môi trường, thường bằng một cơ cấu servo bám theo "
        "rãnh dữ liệu và một cơ cấu quay để dịch chuyển trên rãnh. Tuy hệ truy xuất dữ liệu và các "
        "thành phần phụ trợ quan trọng đối với thiết bị ghi, trong chương này chúng không được coi là "
        "thiết yếu để hiểu công nghệ ghi, và sẽ không được đề cập. Bạn đọc quan tâm được giới thiệu "
        "Tài liệu 1."))

    b.append(h3("Ghi từ", "Magnetic Recording"))
    b.append(p(
        "Hiện nay công nghệ ghi từ chi phối ngành công nghiệp ghi. Nó được dùng dưới các dạng đĩa "
        "cứng, đĩa mềm, đĩa tháo lắp và băng, ở chế độ số hoặc tương tự. Ở dạng đơn giản nhất, nó gồm "
        "một đầu từ và một môi trường từ, như trên Hình 96.13. Đầu từ được làm bằng một miếng vật liệu "
        "từ hình vành khuyên (lõi), có một khe nhỏ hướng về phía môi trường và một cuộn dây ở phía xa "
        "môi trường. Đầu từ ghi và đọc lại thông tin, còn môi trường lưu giữ thông tin. Quá trình ghi "
        "dựa trên hiện tượng một dòng điện i sinh ra một từ thông φ như mô tả bởi định luật Ampère. Từ "
        "thông φ rò ra khỏi lõi từ tại khe và từ hoá môi trường từ, môi trường này chuyển động từ trái "
        "sang phải với vận tốc V bên dưới khe đầu từ. Tuỳ hướng của dòng điện i, môi trường được từ "
        "hoá với vectơ từ độ M hướng sang trái hoặc sang phải. Hình mẫu từ độ này được giữ lại trong "
        "“bộ nhớ” của môi trường ngay cả sau khi đầu từ đã đi qua."))
    b.append(fig(13, F.fig(13)))
    b.append(p(
        "Hai kiểu đầu từ có thể được dùng để đọc lại. Một kiểu, gọi là đầu từ điện cảm, cảm nhận tốc "
        "độ biến thiên từ thông; kiểu kia, gọi là đầu từ từ trở (MR), cảm nhận chính từ thông. Khi "
        "dùng đầu từ điện cảm, quá trình đọc lại chỉ là ngược của quá trình ghi. Từ thông thoát ra "
        "khỏi bề mặt môi trường đã được từ hoá được lõi đầu từ thu lấy. Vì từ độ của môi trường bên "
        "dưới khe thay đổi cả độ lớn lẫn hướng khi môi trường chuyển động, một điện áp được sinh ra "
        "trong cuộn dây. Quá trình này tuân theo định luật Faraday. Hình 96.13b trình bày sơ lược quá "
        "trình ghi/đọc số. Trước hết, toàn bộ dữ liệu người dùng được mã hoá thành dạng nhị phân — một "
        "chuỗi 1 và 0. Sau đó một dòng điện ghi i được gửi tới cuộn dây. Dòng điện này đổi hướng mỗi "
        "khi đang ghi một bit 1. Tương ứng, với mỗi bit 1 trong dữ liệu đã mã hoá, một thay đổi từ độ "
        "— gọi là một chuyển tiếp — được ghi vào môi trường. Trong quá trình đọc lại, điện áp cảm ứng "
        "trong cuộn đầu từ đạt cực đại mỗi khi có một chuyển tiếp trong môi trường. Một bộ phát hiện "
        "xung tạo ra một xung cho mỗi chuyển tiếp. Các xung này được giải mã để thu được dữ liệu người "
        "dùng."))
    b.append(p(
        "Khoảng cách nhỏ nhất giữa hai chuyển tiếp trong môi trường là độ dài biến thiên từ thông B, "
        "và khoảng cách giữa hai rãnh tín hiệu liền kề là bước rãnh W, lớn hơn chiều rộng rãnh tín "
        "hiệu w. Độ dài biến thiên từ thông có thể được chuyển trực tiếp thành độ dài bit với thông "
        "tin mã thích hợp. Nghịch đảo của độ dài bit được gọi là mật độ tuyến tính, và nghịch đảo của "
        "bước rãnh được gọi là mật độ rãnh. Mật độ diện tích lưu trữ thông tin trên môi trường là tích "
        "của mật độ tuyến tính và mật độ rãnh. Mật độ diện tích này quyết định đại khái lượng thông "
        "tin mà người dùng có thể lưu trên một đơn vị diện tích bề mặt môi trường lưu trữ, và là một "
        "chỉ tiêu chất lượng của một kỹ thuật ghi. Rất nhiều nỗ lực đã được bỏ ra để tăng mật độ diện "
        "tích. Ví dụ, nó đã tăng 50 lần trong thập kỷ qua ở ổ đĩa cứng, và được dự báo sẽ tiếp tục "
        "tăng 60% mỗi năm trong tương lai gần. Hiện nay, các sản phẩm đĩa cứng tiên tiến nhất có mật "
        "độ diện tích trên 7 Mbit/mm<sup>2</sup> (B &lt; 0,1 µm và W &lt; 1,5 µm). Điều này cho tổng "
        "dung lượng lưu trữ tới 6 Gbyte cho một đĩa đường kính 95 mm."))

    b.append(h4("Từ tính và vòng từ trễ", "Magnetism and Hysteresis Loop"))
    b.append(p(
        "Từ tính là kết quả của những chuyển động spin electron không được bù trừ trong nguyên tử. Chỉ "
        "các nguyên tố chuyển tiếp mới thể hiện tính chất này, và gần như mọi quan tâm thực tiễn về từ "
        "tính đều tập trung vào nhóm nguyên tố chuyển tiếp thứ nhất (Mn, Cr, Fe, Ni và Co) cùng các "
        "hợp kim của chúng. Độ mạnh của từ tính được biểu diễn bằng từ độ M, và liên hệ với từ trường "
        "H cùng cảm ứng từ B theo"))
    b.append(eq(_eq("vi", "96.1"), "96.1"))
    b.append(p(
        "trong đó μ<sub>0</sub> là độ từ thẩm của chân không. Vì M là tính chất của một vật liệu từ, "
        "nó không tồn tại ngoài vật liệu từ. H biểu diễn độ mạnh tác dụng lên một vật liệu từ từ một "
        "từ trường được sinh ra bởi hoặc một vật liệu từ, hoặc một dòng điện. B là cảm ứng từ, quyết "
        "định điện áp cảm ứng trong một cuộn dây. Tỉ số giữa B có và không có vật liệu từ là độ từ "
        "thẩm tương đối μ của vật liệu từ đó."))
    b.append(p(
        "Khi một từ trường H được đặt vào một mẩu vật liệu từ đã khử từ, từ độ M bắt đầu tăng theo H "
        "từ zero. Tốc độ tăng dần chậm lại và M tiệm cận một giá trị M<sub>s</sub> ở H lớn. Nếu H giảm "
        "về zero thì M giảm về một giá trị thấp hơn M<sub>r</sub>. Giảm H liên tục tới một giá trị âm "
        "rất lớn sẽ từ hoá vật liệu tới –M<sub>s</sub>. Để đưa vật liệu về trạng thái khử từ cần một "
        "từ trường dương H<sub>c</sub>. Tăng tiếp trường H sẽ đưa đường M thành một vòng kín. Vòng này "
        "là vòng từ trễ chính, như trên Hình 96.14. Vòng từ trễ cho thấy một vật liệu từ có bộ nhớ. "
        "Chính bộ nhớ này được dùng trong môi trường để lưu trữ thông tin. H<sub>c</sub> là lực kháng "
        "từ, chỉ độ mạnh từ trường cần để xoá bộ nhớ của một vật liệu từ. Vật liệu từ có H<sub>c</sub> "
        "cao là nam châm “cứng”, và thích hợp cho ứng dụng môi trường nếu chúng có M<sub>r</sub> cao. "
        "Ngược lại, vật liệu từ có H<sub>c</sub> thấp là nam châm “mềm”, và là ứng viên cho vật liệu "
        "lõi đầu từ nếu chúng có M<sub>s</sub> cao và μ cao. M<sub>r</sub> và M<sub>s</sub> lần lượt "
        "là từ độ dư và từ độ bão hoà, và tỉ số của chúng là độ vuông góc dư. Cảm ứng từ ứng với "
        "M<sub>s</sub> là B<sub>s</sub>."))
    b.append(fig(14, F.fig(14)))

    b.append(h4("Môi trường từ", "Magnetic Media"))
    b.append(p(
        "Môi trường từ được dùng để lưu trữ thông tin trong một hệ ghi từ. Để tăng mật độ diện tích, "
        "ta cần giảm độ dài biến thiên từ thông B và chiều rộng rãnh w. Vì B bị giới hạn bởi số hạng "
        "M<sub>r</sub>δ/H<sub>c</sub>, trong đó δ là bề dày lớp từ, ta có thể giảm B bằng cách giảm "
        "M<sub>r</sub>δ hoặc tăng H<sub>c</sub>. Tuy nhiên, biên độ tín hiệu từ khả dụng cho đầu đọc "
        "lại tỉ lệ với số hạng M<sub>r</sub>δw. Nếu giảm chiều rộng rãnh w để tăng mật độ diện tích, "
        "ta phải tăng M<sub>r</sub>δ để tránh tín hiệu suy giảm. Ngoài ra, nếu lớp từ quá mỏng đến mức "
        "gây không đồng đều bề dày, sẽ xuất hiện nhiều nhiễu hơn trong quá trình đọc lại. Do đó, những "
        "yêu cầu chính đối với lớp từ là H<sub>c</sub> cao, M<sub>r</sub> cao, và dễ tạo lớp mỏng đồng "
        "đều. Các yêu cầu bổ sung gồm độ ổn định từ tính và cơ học tốt."))
    b.append(p(
        "Có hai nhóm môi trường từ. Nhóm thứ nhất được gọi là môi trường dạng hạt vì vật liệu từ ở "
        "dạng hạt. Nhóm này gồm oxit sắt (γ-Fe<sub>2</sub>O<sub>3</sub>), oxit sắt biến tính coban "
        "(γ-Fe<sub>2</sub>O<sub>3</sub>+Co), đioxit crom (CrO<sub>2</sub>), hạt kim loại và ferit bari "
        "(BaFe<sub>12</sub>O<sub>19</sub>). Một số trong đó đã được dùng trong ghi từ hàng chục năm. "
        "Gần đây hơn, một nhóm môi trường khác đã được phát triển phần lớn nhờ nhu cầu ngày càng tăng "
        "về dung lượng lưu trữ cao hơn trong ngành công nghiệp máy tính. Nhóm môi trường này là môi "
        "trường màng mỏng, trong đó lớp từ có thể được tạo thành một màng mỏng liên tục. Phần lớn vật "
        "liệu trong nhóm này là hợp kim kim loại gốc coban. So với môi trường dạng hạt, môi trường "
        "màng mỏng thường có lực kháng từ H<sub>c</sub> cao hơn, từ độ dư M<sub>r</sub> cao hơn, và có "
        "thể được lắng đọng thành một màng mỏng liên tục rất mỏng. Bảng 96.8 liệt kê H<sub>c</sub> và "
        "M<sub>r</sub> của một số môi trường dạng hạt và màng mỏng được dùng phổ biến nhất. Lưu ý rằng "
        "tính chất từ chịu ảnh hưởng của quá trình chế tạo và cấu trúc màng. Do đó, giá trị của chúng "
        "có thể nằm ngoài các khoảng trong Bảng 96.8 nếu dùng quy trình khác."))
    b.append(table(*_t8("vi")))
    b.append(p(
        "Môi trường từ có thể được phân thành ba dạng ứng dụng chung. Băng là dạng lâu đời nhất và "
        "vẫn là môi trường quan trọng ngày nay. Nó là trung tâm của phần lớn việc ghi âm thanh, video "
        "và thiết bị đo, dù nó cũng được dùng trong ngành máy tính để lưu trữ dài hạn. Băng kinh tế và "
        "có thể chứa dung lượng lớn, nhưng thời gian truy xuất chậm. Đĩa cứng chủ yếu được dùng làm bộ "
        "lưu trữ bên trong máy tính, cho người dùng truy xuất dữ liệu nhanh, nhưng khả năng vận chuyển "
        "kém. Đĩa mềm được thiết kế để dễ vận chuyển dữ liệu, nhưng dung lượng hạn chế. Ngoài ba dạng "
        "ứng dụng chung này, một dạng lai giữa đĩa mềm và đĩa cứng đang dần được chấp nhận. Đó là đĩa "
        "cứng tháo lắp, có thể chứa tới vài gigabyte dữ liệu số. Ngoài ra, các dải từ đang được dùng "
        "rộng rãi trong nhiều dạng thẻ khác nhau."))
    b.append(p(
        "Chỉ riêng lớp từ không thể dùng làm môi trường. Nó cần các thành phần bổ sung để cải thiện độ "
        "bền hoá học và cơ học. Mặt cắt điển hình của một băng từ dạng hạt và của một đĩa cứng màng "
        "mỏng được trình bày trên Hình 96.15. Với ứng dụng băng, các hạt sắt có kích thước điển hình "
        "dài 0,5 µm và rộng 0,1 µm được phân tán trong một chất kết dính polymer, cùng với dung môi, "
        "chất bôi trơn và các chất độn khác để cải thiện độ ổn định từ tính và cơ học. Vật liệu đã "
        "phân tán này sau đó được phủ lên một đế polyetylen terephtalat đã được định hướng hai chiều. "
        "Một lớp phủ mặt sau tuỳ chọn cũng có thể được phủ lên mặt kia của đế. Mặt cắt của đĩa cứng "
        "phức tạp hơn. Một đế nhôm–magie độ tinh khiết cao (5% khối lượng) được tiện kim cương tới độ "
        "nhẵn bề mặt tinh, rồi được mạ hoá học không điện một lớp lót niken–photpho không từ (10% "
        "nguyên tử). Lớp này dùng để tăng độ cứng, giảm khuyết tật và cải thiện độ nhẵn của hợp kim "
        "Al–Mg, và được đánh bóng tới độ nhẵn siêu tinh. Tiếp theo, một lớp nền crom được phún xạ để "
        "điều khiển tính chất của màng từ, sau đó phún xạ màng từ. Cuối cùng, một lớp cacbon đã hydro "
        "hoá hoặc nitơ hoá được phủ lên màng từ, và một lớp cực mỏng chất bôi trơn lỏng hydrocacbon "
        "perflo được phủ lên trên cùng. Các lớp cacbon và chất bôi trơn dùng để cải thiện khả năng "
        "chống ăn mòn và chống mài mòn của đĩa. Với một đĩa 95 mm, sản phẩm hoàn chỉnh phải có độ "
        "phẳng bề mặt tốt hơn 10 µm và độ nhám bề mặt được kiểm soát chặt. Trong một số ứng dụng, yêu "
        "cầu độ nhám trung bình số học (R<sub>a</sub>) nhỏ hơn 0,5 nm."))
    b.append(fig(15, F.fig(15)))

    b.append(h4("Đầu từ", "Magnetic Heads"))
    b.append(p(
        "Đầu từ có ba chức năng: ghi, đọc lại và xoá. Thường với các ứng dụng đầu từ đứng yên như ổ "
        "băng, người ta dùng nhiều đầu từ để thực hiện các chức năng này. Với các ứng dụng đầu từ "
        "chuyển động như ổ đĩa, người ta dùng một đầu từ duy nhất vì yêu cầu về kết nối đơn giản và "
        "khối lượng đầu nhỏ để truy xuất dữ liệu nhanh. Phần lớn các đầu từ này thuộc kiểu điện cảm, "
        "với thiết kế cơ bản là một cuộn cảm và một lõi từ. Những yêu cầu chung đối với vật liệu lõi là "
        "độ từ thẩm tương đối μ cao, cảm ứng từ bão hoà B<sub>s</sub> cao, lực kháng từ H<sub>c</sub> "
        "thấp, điện trở suất ρ cao và hệ số từ giảo λ thấp. Một số tính chất của các vật liệu lõi "
        "thường dùng được liệt kê trong Bảng 96.9."))
    b.append(table(*_t9("vi")))
    b.append(p(
        "Sự tiến hoá của đầu từ đi theo việc chọn vật liệu lõi, như trên Hình 96.16. Những đầu từ đầu "
        "tiên dùng Permalloy molypđen dạng lá (Ni-Fe-Mo, 79-17-4% khối lượng). Những đầu từ này rẻ để "
        "chế tạo, và có H<sub>c</sub> thấp cùng μ và B<sub>s</sub> cao. Nhược điểm chính là giới hạn "
        "tần số, độ chính xác kích thước khe và độ mềm cơ học. Giới hạn tần số do khó làm lớp lá mỏng "
        "hơn 25 µm. Tổn hao dòng xoáy, tỉ lệ với bề dày lớp và căn bậc hai của tần số, làm giảm độ từ "
        "thẩm hiệu dụng. Kết quả là đầu từ dạng lá hiếm khi được dùng cho ứng dụng vượt quá 10 MHz. Độ "
        "chính xác kích thước khe gắn với quá trình chế tạo đầu từ, khiến nó không thích hợp cho ứng "
        "dụng mật độ diện tích cao. Thiếu độ cứng cơ học làm giảm tuổi thọ sử dụng."))
    b.append(fig(16, F.fig(16)))
    b.append(p(
        "Một cách để giảm tổn hao dòng xoáy là tăng điện trở suất của vật liệu lõi. Hai loại vật liệu "
        "ferit có điện trở suất cao (cao hơn Permalloy từ bốn đến chín bậc) và tính chất từ hợp lý: "
        "Ni–Zn và Mn–Zn. Những vật liệu này cũng rất cứng, kéo dài tuổi thọ đầu từ trong các tiếp xúc "
        "đầu từ/môi trường. Nhược điểm chính của vật liệu ferit là giá trị B<sub>s</sub> thấp. Để ghi "
        "trên môi trường có H<sub>c</sub> cao, cần cảm ứng từ B cao trong lõi đầu từ. Khi cảm ứng từ "
        "trong vật liệu lõi đạt tới bão hoà B<sub>s</sub>, nó sẽ không tăng nữa dù tăng dòng điện ghi "
        "hay số vòng dây. Sự bão hoà này bắt đầu từ các góc của khe do hình học của nó. Để khắc phục "
        "nhược điểm này, một lớp vật liệu hợp kim kim loại có B<sub>s</sub> cao hơn nhiều được lắng "
        "đọng trên các mặt khe. Kiểu đầu từ này được gọi là đầu từ kim loại trong khe (MIG). Sendust "
        "(Fe-Si-Al, 85-9,6-5,4% khối lượng) là một trong những vật liệu được dùng để lắng đọng. Đầu từ "
        "MIG có khả năng ghi tới tần số 100 MHz và lực kháng từ môi trường 180 kA/m."))
    b.append(p(
        "Đầu từ màng mỏng tận dụng công nghệ chế tạo kiểu bán dẫn để giảm các bước chế tạo riêng cho "
        "từng đầu từ. Lõi, cuộn dây, khe và các lớp cách điện đều được chế tạo bằng mạ điện, phún xạ "
        "hoặc bay hơi. Do bản chất của quy trình bán dẫn, việc chế tạo chính xác với kích thước nhỏ. "
        "Kích thước khe nhỏ thích hợp cho mật độ tuyến tính và mật độ rãnh cao, và kích thước lõi nhỏ "
        "cho phép dùng vật liệu Permalloy có B<sub>s</sub> cao (Ni-Fe, 80-20% khối lượng) làm lõi với "
        "điện cảm thấp cho ứng dụng tốc độ dữ liệu cao. Đầu từ màng mỏng được dùng cho ứng dụng có "
        "H<sub>c</sub> môi trường cao và mật độ diện tích cao. Giá thành cao của quy trình kiểu bán "
        "dẫn được bù lại bằng thông lượng cao: một phiến 150 × 150 mm có thể sản xuất 16 000 đầu từ "
        "cỡ nano. Một nhược điểm là khả năng ghi hạn chế băng tần vì chiều dài cực từ nhỏ hạn chế đáp "
        "ứng tần số thấp và gây ra các vọt lõm. Nhược điểm thứ hai là nhiễu Barkhausen, gây ra bởi số "
        "đômen từ tương đối nhỏ trong lõi. Hiện nay, đầu từ màng mỏng được dùng tới tần số 80 MHz và "
        "lực kháng từ môi trường 200 kA/m. Đầu từ màng mỏng MIG cũng đang được dùng cho các ứng dụng "
        "lực kháng từ cao."))
    b.append(p(
        "Một đầu từ điện cảm thường được dùng cho cả ghi và đọc lại. Không thể đạt hiệu năng tối ưu vì "
        "ghi và đọc lại có những yêu cầu trái ngược nhau đối với thiết kế đầu từ. Để giải quyết vấn đề "
        "này, đầu từ MR đã được phát triển. Đầu từ MR chỉ dùng để đọc lại, và một đầu từ điện cảm được "
        "dùng để ghi. Như trình bày sơ lược trên Hình 96.16, một đầu từ MR có một phần tử từ trở (MRE) "
        "và hai dây dẫn điện. MRE là một dải Permalloy (Ni-Fe, 80-20% khối lượng), có bề dày t, chiều "
        "rộng w và chiều cao h. Một dòng điện có mật độ J đi qua MRE qua các dây dẫn. Điện trở suất của "
        "MRE là một hàm của góc θ giữa J và từ độ M của MRE:"))
    b.append(eq(_eq("vi", "96.2"), "96.2"))
    b.append(p(
        "trong đó ρ<sub>θ</sub> là điện trở suất tại θ, ρ là điện trở suất tại θ = 90°, và Δρ là hiệu "
        "điện trở suất giữa θ = 0° và θ = 90°. Δρ/ρ là tỉ số từ trở dị hướng (AMR) của MRE. Thường "
        "người ta đặt một từ trường ngang lên MRE để θ = θ<sub>0</sub> khi đầu từ không đọc tín hiệu "
        "từ. Giả sử một tín hiệu từ từ môi trường làm quay M từ θ<sub>0</sub> tới θ, khi đó một thay "
        "đổi điện áp v sẽ được phát hiện trên MRE làm tín hiệu ra:"))
    b.append(eq(_eq("vi", "96.3"), "96.3"))
    b.append(p(
        "trong đó θ<sub>0</sub> là góc thiên áp và được đặt bằng 45° để có độ tuyến tính tốt. Trong "
        "thực tế, người ta còn dùng một thiên áp dọc theo chiều rộng MRE để ổn định đômen từ và giảm "
        "nhiễu Barkhausen lớn. Để so sánh đầu ra giữa đầu từ MR và đầu từ điện cảm, ta viết đầu ra của "
        "đầu từ điện cảm bằng phương trình Faraday:"))
    b.append(eq(_eq("vi", "96.4"), "96.4"))
    b.append(p(
        "trong đó n là số vòng dây của cuộn, V là vận tốc môi trường, φ là từ thông, và x là trục toạ "
        "độ gắn với bề mặt môi trường. Các phương trình 96.3 và 96.4 cho ta biết rằng trong khi đầu ra "
        "của đầu từ điện cảm tỉ lệ với vận tốc môi trường và không thích hợp cho ứng dụng vận tốc "
        "thấp, thì đầu từ MR có thể dùng cho ứng dụng vận tốc cao cũng như thấp."))

    b.append(h4("Quá trình ghi", "Recording Process"))
    b.append(p(
        "Ta có thể hình dung quá trình ghi thành hai bước. Trước hết, từ thông chảy trong lõi đầu từ "
        "sinh ra một từ trường rìa quanh khe. Sau đó từ trường này từ hoá môi trường từ và để lại một "
        "chuyển tiếp từ độ trong đó. Một phần do bản chất phi tuyến của vòng từ trễ, quá trình ghi "
        "phức tạp đến mức chưa có lời giải thích chặt chẽ nào. Tuy vậy, ta vẫn có thể thu được những "
        "hiểu biết đáng kể về quá trình ghi bằng cách dùng các mô hình đơn giản, miễn là ghi nhớ những "
        "hạn chế của chúng."))
    b.append(p(
        "Nếu đặt gốc của một hệ toạ độ tại tâm khe với trục x trên bề mặt đầu từ và trục y hướng ra "
        "xa đầu từ, thì từ trường dọc H<sub>x</sub> và từ trường vuông góc H<sub>y</sub> của đầu từ "
        "này có thể được biểu diễn bằng xấp xỉ Karlqvist [2]:"))
    b.append(eq(_eq("vi", "96.5"), "96.5"))
    b.append(eq(_eq("vi", "96.6"), "96.6"))
    b.append(p(
        "trong đó n là số vòng dây, i là dòng điện trong cuộn, g là chiều dài khe, l là chiều dài lõi, "
        "A<sub>g</sub> là diện tích tiết diện lõi, μ là độ từ thẩm tương đối của vật liệu lõi, và "
        "A<sub>c</sub> là diện tích tiết diện khe. Cả hai phương trình 96.5 và 96.6 cho kết quả chính "
        "xác với các điểm cách góc khe 0,25g. Vì chế độ ghi dọc chi phối ngành công nghiệp ghi từ, ta "
        "sẽ tập trung vào trường H<sub>x</sub>. Phương trình 96.5 cho thấy các đường đồng mức của "
        "trường H<sub>x</sub> là những vòng tròn lồng vào nhau tựa trên hai góc khe, như trên Hình "
        "96.17. Đường kính vòng tròn càng lớn thì từ trường càng yếu. Giả sử một môi trường từ chuyển "
        "động từ trái sang phải ở độ cao d trên đầu từ, có bề dày δ và từ độ M hướng sang phải. Tại "
        "một thời điểm nào đó dòng điện ghi bật và sinh ra từ trường H<sub>x</sub> trên khe như mô tả "
        "trên Hình 96.17. Trên chu vi H<sub>x</sub> = H<sub>c</sub>, một nửa vật liệu môi trường có từ "
        "độ bị đảo và một nửa giữ nguyên, nên tổng từ độ bằng không. Vì H<sub>x</sub> có gradient, môi "
        "trường gần khe hơn (bên trong vòng tròn nhỏ hơn) có từ độ bị đảo hoàn toàn hơn so với môi "
        "trường xa khe hơn (bên ngoài vòng tròn lớn hơn). Do đó, chuyển tiếp từ trong môi trường là "
        "dần dần ngay cả khi sự thay đổi của dòng điện ghi theo hàm bậc thang. Giả sử từ độ ban đầu là "
        "M<sub>r</sub> và từ độ bị đảo hoàn toàn là –M<sub>r</sub>, sự thay đổi từ độ dần dần này đối "
        "với một chuyển tiếp cô lập có thể được mô hình hoá bởi [3]:"))
    b.append(eq(_eq("vi", "96.7"), "96.7"))
    b.append(p(
        "trong đó x là khoảng cách từ tâm chuyển tiếp và a là một thông số đặc trưng cho độ sắc của "
        "chuyển tiếp như trên Hình 96.18. Giả sử môi trường là màng mỏng và dùng xấp xỉ Karlqvist cho "
        "trường đầu từ, ta tìm được a là [4–6]:"))
    b.append(fig(17, F.fig(17)))
    b.append(fig(18, F.fig(18)))
    b.append(eq(_eq("vi", "96.8"), "96.8"))
    b.append(p(
        "trong đó S* là độ vuông góc của vòng môi trường và Q là hệ số gradient trường đầu từ. Với một "
        "đầu từ được thiết kế hợp lý, Q ≈ 0,8. Rõ ràng ta muốn làm thông số a càng nhỏ càng tốt để có "
        "thể ghi được nhiều chuyển tiếp hơn trên một đơn vị chiều dài môi trường. Nếu chiều dài khe g "
        "và bề dày môi trường δ nhỏ so với khoảng cách đầu từ/môi trường d, và môi trường có độ vuông "
        "góc bằng một, thì giá trị nhỏ nhất có thể của a là [7]:"))
    b.append(eq(_eq("vi", "96.9"), "96.9"))
    b.append(p(
        "Để giảm giá trị của a và do đó tăng mật độ diện tích, ta cần giảm từ độ dư M<sub>r</sub>, bề "
        "dày δ, khoảng cách đầu từ/môi trường d, và tăng lực kháng từ H<sub>c</sub>."))

    b.append(h4("Quá trình đọc lại", "Reproducing Process"))
    b.append(p(
        "Ngược với quá trình ghi, quá trình đọc lại được hiểu rõ. Cảm ứng từ cảm ứng trong lõi đầu từ "
        "cỡ vài millitesla, cho một quá trình tuyến tính, dễ xử lý toán học hơn. Trường rìa của đầu từ "
        "là xấp xỉ Karlqvist (Pt. 96.5) và nền tảng là định lý tương hỗ. Với một chuyển tiếp cô lập "
        "(Hình 96.18) có lớp từ mỏng δ ≪ d, điện áp cảm ứng v của một đầu từ điện cảm là [7]:"))
    b.append(eq(_eq("vi", "96.10"), "96.10"))
    b.append(p(
        "trong đó μ<sub>0</sub> là độ từ thẩm của chân không, μ là độ từ thẩm tương đối của lõi, V là "
        "vận tốc môi trường, w là chiều rộng rãnh, n là số vòng dây, g là chiều dài khe đầu từ, d là "
        "khoảng cách đầu từ/môi trường, và x là khoảng cách giữa tâm chuyển tiếp môi trường và tâm "
        "khe đầu từ. Số hạng lA<sub>g</sub>/μA<sub>c</sub> liên quan chặt với g đối với hiệu suất đầu "
        "từ. Khi một chuyển tiếp đi qua bên dưới đầu từ, điện áp của nó bắt đầu với giá trị rất thấp, "
        "đạt cực đại, rồi lại giảm, như trên Hình 96.19, trong đó dùng các giá trị điển hình sau cho "
        "một ổ đĩa cứng: V = 20 m/s, w = 3,5 µm, M<sub>r</sub> = 450 kA/m, δ = 50 nm, n = 50, "
        "lA<sub>g</sub>/μA<sub>c</sub> = 0,1g. Ảnh hưởng của g và a + d được thể hiện trên Hình 96.19. "
        "Vì quá trình đọc lại mong muốn điện áp đỉnh lớn hơn và đáp ứng không gian hẹp hơn, nên các "
        "giá trị g và a + d nhỏ hơn là có lợi."))
    b.append(fig(19, F.fig(19)))
    b.append(p(
        "Khi dùng đầu từ MR để đọc lại, MRE thường được kẹp giữa hai vỏ bọc từ để tăng độ phân giải "
        "không gian đối với tín hiệu môi trường, như trên Hình 96.20. Vì đầu từ MR nhạy với từ thông, "
        "từ thông tới φ<sub>i</sub> trên mặt dưới của MRE cần được suy ra như một hàm của khoảng cách "
        "(x) giữa tâm MRE và tâm chuyển tiếp [7, 8]:"))
    b.append(fig(20, F.fig(20)))
    b.append(eq(_eq("vi", "96.11"), "96.11"))
    b.append(p(
        "trong đó g là khoảng cách giữa MRE và vỏ bọc, t là bề dày MRE, và"))
    b.append(eq(_eq("vi", "96.12"), "96.12"))
    b.append(p(
        "Góc giữa từ độ và dòng điện thay đổi dọc theo chiều cao h của MRE. Để tìm sự biến thiên đó, "
        "ta cần tính độ suy giảm từ thông tín hiệu như một hàm của y theo"))
    b.append(eq(_eq("vi", "96.13"), "96.13"))
    b.append(p("trong đó"))
    b.append(eq(_eq("vi", "96.14"), "96.14"))
    b.append(p("Khi đó góc thiên áp θ<sub>0</sub> và góc tín hiệu θ có thể được tính bằng"))
    b.append(eq(_eq("vi", "96.15"), "96.15"))
    b.append(p("và"))
    b.append(eq(_eq("vi", "96.16"), "96.16"))
    b.append(p(
        "trong đó φ<sub>b</sub> là từ thông thiên áp trong MRE và M<sub>s</sub> là từ độ bão hoà của "
        "MRE. Áp dụng các phương trình 96.15 và 96.16 vào Pt. 96.3 và lấy tích phân theo chiều cao h, "
        "ta được"))
    b.append(eq(_eq("vi", "96.17"), "96.17"))
    b.append(p(
        "Với một đầu từ MR có thiên áp 45° ở tâm và chiều cao nhỏ h ≪ l<sub>c</sub>, điện áp đỉnh là "
        "[6]"))
    b.append(eq(_eq("vi", "96.18"), "96.18"))
    b.append(p("Hình dạng chung của điện áp đọc lại từ một đầu từ MR tương tự như trên Hình 96.19."))
    b.append(p(
        "Việc nghiên cứu một chuyển tiếp cô lập phơi ra nhiều đặc trưng nội tại của quá trình đọc lại. "
        "Tuy nhiên, các chuyển tiếp thường được ghi sát nhau trong một môi trường từ để đạt mật độ "
        "tuyến tính cao. Khi đó, sự biến thiên từ độ trong môi trường tiến tới một sóng sin. Tức là"))
    b.append(eq(_eq("vi", "96.19"), "96.19"))
    b.append(p(
        "trong đó λ là bước sóng. Điện áp đọc lại ở một đầu từ điện cảm trở thành [9, 10]"))
    b.append(eq(_eq("vi", "96.20"), "96.20"))
    b.append(p(
        "Phương trình này trình bày mọi đặc trưng quan trọng của quá trình đọc lại ở mật độ tuyến tính "
        "cao. Số hạng exp(–2πd/λ) là tổn hao khoảng cách. Nó cho thấy điện áp đọc lại giảm theo hàm mũ "
        "với tỉ số giữa khoảng cách đầu từ/môi trường và bước sóng. Số hạng thứ hai 1 – exp(–2πδ/λ) là "
        "tổn hao bề dày. Tên gọi của số hạng này gây hiểu nhầm vì giá trị của nó tăng khi bề dày môi "
        "trường lớn hơn. Tuy nhiên, tốc độ tăng giảm dần với môi trường dày hơn. Thực tế, 80% giá trị "
        "lớn nhất có thể đạt được với bề dày môi trường 0,25λ. Số hạng cuối sin(πg/λ)/(πg/λ) là tổn "
        "hao khe. Số hạng này dựa trên xấp xỉ Karlqvist. Nếu dùng trường rìa đầu từ chính xác hơn, số "
        "hạng này được sửa thành sin(πg/λ)/(πg/λ)·(1,25g<sup>2</sup> – λ<sup>2</sup>)/(g<sup>2</sup> – "
        "λ<sup>2</sup>) [11]. Nó cho một điểm không của khe tại λ = 1,12g, và giới hạn bước sóng ngắn "
        "nhất có thể ghi được. Ba số hạng này được vẽ trên Hình 96.21. Tổn hao đáng kể nhất đến từ số "
        "hạng tổn hao khoảng cách, bằng 54,6 dB khi d = λ. Do đó, một trong những nỗ lực lớn nhất dành "
        "cho ghi từ là giảm khoảng cách đầu từ/môi trường càng nhiều càng tốt mà không gây vấn đề về "
        "độ tin cậy cơ học. Với một đầu từ MR, điện áp đọc lại là [11]"))
    b.append(fig(21, F.fig(21)))
    b.append(eq(_eq("vi", "96.21"), "96.21"))

    b.append(h4("Ghi số và ghi tương tự", "Digital vs. Analog Recording"))
    b.append(p(
        "Do tính phi tuyến của vòng từ trễ, ghi từ về bản chất thích hợp cho ghi số, nơi chỉ có hai "
        "trạng thái (1 và 0) cần được nhận biết. Tuy nhiên, nhiều đại lượng vật lý được nhận ở dạng "
        "tương tự trước khi có thể được ghi, như trong ghi âm thanh tiêu dùng và ghi thiết bị đo. Để "
        "thực hiện việc ghi như vậy, ta cần hoặc số hoá thông tin, hoặc dùng kỹ thuật ghi tương tự. "
        "Trong trường hợp số hoá, ta dùng một bộ biến đổi tương tự–số để chuyển một tín hiệu liên tục "
        "thành các số nhị phân. Quá trình có thể được giải thích bằng ví dụ trên Hình 96.22. Một tín "
        "hiệu điện V, được chuẩn hoá về khoảng từ 0 đến 1, cần được số hoá thành ba bit. Tín hiệu được "
        "lấy mẫu tại thời điểm t = 1, 2, …, 6. Tại mỗi điểm lấy mẫu, bit thứ nhất được gán 1 nếu giá "
        "trị của tín hiệu liên tục nằm ở nửa trên (&gt; 0,5), nếu không thì gán 0. Bit thứ hai được "
        "gán 1 nếu giá trị của tín hiệu liên tục nằm ở nửa trên của mỗi nửa (0,25 ≤ V &lt; 0,5, hoặc "
        "&gt; 0,75), nếu không thì gán 0. Bit thứ ba được gán tương tự. Bit thứ nhất là bit có nghĩa "
        "lớn nhất (MSB), và bit cuối là bit có nghĩa nhỏ nhất (LSB). Các số nhị phân đã biến đổi được "
        "liệt kê bên dưới mỗi điểm lấy mẫu trên Hình 96.22. Quá trình số hoá này được gọi là lượng tử "
        "hoá. Nói chung, khoảng lượng tử hoá cuối cùng là"))
    b.append(fig(22, F.fig(22)))
    b.append(eq(_eq("vi", "96.22"), "96.22"))
    b.append(p(
        "trong đó V là toàn dải điện áp và N là số bit. Vì ta dùng một số bit hữu hạn, về mặt thống kê "
        "có một khác biệt giữa tín hiệu liên tục và tín hiệu đã lượng tử hoá tại các điểm lấy mẫu. Đó "
        "là sai số lượng tử hoá. Nó dẫn tới một tỉ số tín hiệu trên nhiễu lượng tử hoá (SNR) [12]:"))
    b.append(eq(_eq("vi", "96.23"), "96.23"))
    b.append(p(
        "trong đó P<sub>s</sub> là công suất tín hiệu trung bình bình phương. Với một tín hiệu phân bố "
        "đều trên toàn dải, điều này cho"))
    b.append(eq(_eq("vi", "96.24"), "96.24"))
    b.append(p("Với một tín hiệu hình sin, nó trở thành"))
    b.append(eq(_eq("vi", "96.25"), "96.25"))
    b.append(p(
        "Có thể cải thiện SNR bằng cách dùng nhiều bit hơn. Tuy nhiên, sự cải thiện này bị giới hạn "
        "bởi SNR của tín hiệu liên tục tới. Tín hiệu đã lượng tử hoá sau đó được điều chế xung mã "
        "(PCM) để ghi."))
    b.append(p(
        "Với ghi tương tự, cần một quan hệ tuyến tính giữa từ độ của môi trường và tín hiệu ghi. Điều "
        "này đạt được qua quá trình từ hoá không trễ. Nếu ta đặt một từ trường xoay chiều và một từ "
        "trường một chiều lên một môi trường đã khử từ trước đó, rồi giảm biên độ của từ trường xoay "
        "chiều về zero trước khi bỏ từ trường một chiều, thì từ độ dư thể hiện một quan hệ gần như "
        "tuyến tính với cường độ từ trường một chiều H<sub>u</sub> tới một mức nào đó. Hình 96.23 cho "
        "thấy một đường cong không trễ như vậy. Độ tuyến tính suy giảm khi H<sub>u</sub> lớn hơn. "
        "Trong ứng dụng, dòng điện tín hiệu ghi được thiên áp bằng một dòng xoay chiều có biên độ lớn "
        "hơn và tần số cao hơn. Do đó nó cũng được gọi là ghi thiên áp xoay chiều. Ghi tương tự dễ "
        "thực hiện, với cái giá là SNR thấp hơn vì từ độ dư bị giới hạn ở khoảng 30% M<sub>r</sub> lớn "
        "nhất có thể để đạt độ tuyến tính tốt."))
    b.append(fig(23, F.fig(23)))

    b.append(h4("Mã ghi", "Recording Codes"))
    b.append(p(
        "PCM là một sơ đồ biến đổi dữ liệu nhị phân vào để chúng thích hợp hơn cho một kênh ghi và đọc "
        "lại. Những sơ đồ này nhằm đạt một số mục tiêu sau: (1) giảm thành phần một chiều, (2) tăng "
        "mật độ tuyến tính, (3) tự tạo xung đồng hồ, (4) hạn chế lan truyền lỗi, và (5) đạt phát hiện "
        "không lỗi. Có rất nhiều sơ đồ mã, chỉ ba trong số những sơ đồ được phát triển sớm được trình "
        "bày trên Hình 96.24. Sơ đồ sớm nhất và đơn giản nhất là mã về không (RZ). Trong sơ đồ này, "
        "một xung dương và một xung âm lần lượt biểu diễn bit 1 và bit 0 của dữ liệu. Nhược điểm chính "
        "là không thể ghi trực tiếp đè lên dữ liệu cũ do tồn tại dòng điện ghi bằng không giữa hai bit "
        "dữ liệu. Nó cũng tạo ra hai chuyển tiếp cho mỗi bit, do đó làm giảm mật độ tuyến tính. Ngoài "
        "ra, nó chỉ dùng một nửa dải dòng điện ghi khả dụng cho một chuyển tiếp. Phương pháp không về "
        "không đảo (NRZI) được phát triển để giảm bớt một số vấn đề này. Nó đổi chiều dòng điện ghi từ "
        "hướng này sang hướng kia với mỗi bit 1 của dữ liệu, trong khi không đổi với mọi bit 0. Tuy "
        "nhiên, nó có thành phần một chiều mạnh và có thể mất đồng bộ đọc lại nếu trong dữ liệu vào có "
        "một chuỗi 0 dài. Ngoài ra, các mạch đọc lại thường không được thiết kế để xử lý tín hiệu một "
        "chiều. Trong mã điều tần (FM) luôn có một chuyển tiếp tại biên của ô bit, đóng vai trò đồng "
        "hồ. Cũng có thêm một chuyển tiếp tại tâm ô bit với mỗi bit 1 và không có chuyển tiếp với bit "
        "0. Nó giảm thành phần một chiều đáng kể. Nhược điểm chính là giảm mật độ tuyến tính vì có hai "
        "chuyển tiếp cho mỗi bit 1 trong dữ liệu."))
    b.append(fig(24, F.fig(24)))
    b.append(p(
        "Các mã được dùng phổ biến nhất cho ghi từ là mã giới hạn độ dài chuỗi (RLL). Chúng có dạng "
        "tổng quát m/n(d, k). Trong các sơ đồ này, dữ liệu được mã hoá theo nhóm. Mỗi nhóm vào có m "
        "bit. Sau khi mã hoá, mỗi nhóm chứa n bit. Ở một số sơ đồ, nhiều nhóm được mã hoá cùng nhau. d "
        "và k lần lượt là số bit 0 nhỏ nhất và lớn nhất giữa hai bit 1 liên tiếp trong chuỗi đã mã "
        "hoá. Trong khi d được dùng để giới hạn mật độ chuyển tiếp cao nhất và giao thoa giữa các ký "
        "hiệu, k được dùng để bảo đảm tần số chuyển tiếp đủ cho việc đồng bộ xung đồng hồ khi đọc "
        "lại. Việc mã hoá được thực hiện bằng một bảng tra cứu, như Bảng 96.10 cho mã 1/2(2,7) [13]."))
    b.append(table(*_t10("vi")))

    b.append(h4("Ma sát học ở mặt phân cách đầu từ/môi trường",
                "Head/Medium Interface Tribology"))
    b.append(p(
        "Như đã nêu ở Pt. 96.20, cách hiệu quả nhất để tăng biên độ tín hiệu, và do đó tăng mật độ "
        "diện tích, là giảm khoảng cách đầu từ/môi trường d. Tuy nhiên, mài mòn xảy ra khi một bề mặt "
        "chuyển động ở rất gần một bề mặt khác. Lượng mài mòn được mô tả bằng phương trình Archard:"))
    b.append(eq(_eq("vi", "96.26"), "96.26"))
    b.append(p(
        "trong đó V là thể tích bị mài mòn, W là tải pháp tuyến, s là quãng trượt, H là độ cứng của "
        "bề mặt bị mài mòn, và k là hệ số mài mòn. Để tăng độ cứng H của môi trường, các hạt "
        "Al<sub>2</sub>O<sub>3</sub> cứng được phân tán trong môi trường dạng hạt và một lớp mỏng "
        "cacbon cứng (≈ 10 nm) đã hydro hoá hoặc nitơ hoá được phủ lên môi trường màng mỏng của đĩa "
        "cứng. Một lớp chất bôi trơn lỏng, điển hình là polyete perflo với các nhóm đầu và phụ gia "
        "khác nhau, được phủ lên trên màng cacbon để giảm hệ số mài mòn k. Tải được giảm thiểu để giảm "
        "mài mòn trong khi vẫn giữ độ ổn định động học đầu từ/môi trường đầy đủ. Với những ứng dụng mà "
        "quãng trượt s là khiêm tốn trong tuổi thọ sản phẩm, như ổ đĩa mềm và ổ băng tiêu dùng, đầu từ "
        "tiếp xúc vật lý với môi trường trong khi hoạt động. Với ứng dụng đĩa cứng, đầu từ được tách "
        "khỏi môi trường một cách danh định bằng một lớp đệm khí. Đầu từ được mang trên một con trượt, "
        "và con trượt dùng các mặt tựa khí (ABS) để tạo màng khí dựa trên lý thuyết bôi trơn thuỷ "
        "động. Hình 96.25 cho thấy hai kiểu ABS thường dùng. Các phần vát được dùng để giúp con trượt "
        "cất cánh và giữ ổn định khi bay. ABS tạo ra áp suất cao hơn áp suất môi trường để nâng con "
        "trượt lên trên bề mặt môi trường trong khi hoạt động. Con trượt ba đệm dùng cho ứng dụng gần "
        "tiếp xúc, còn con trượt áp suất dưới môi trường (SAP) dùng cho ứng dụng bay (như đầu từ MR). "
        "Vì vận tốc tuyến tính tương đối giữa con trượt và môi trường thay đổi khi đầu từ dịch chuyển "
        "tới các bán kính khác nhau, một vùng hốc được dùng trong con trượt SAP để tạo lực hút nhằm "
        "giảm biến thiên chiều cao bay. ABS được thiết kế dựa trên phương trình Reynolds hiệu chỉnh:"))
    b.append(fig(25, F.fig(25)))
    b.append(eq(_eq("vi", "96.27"), "96.27"))
    b.append(p(
        "trong đó X và Y là các toạ độ theo phương dọc và phương ngang của con trượt, được chuẩn hoá "
        "lần lượt bằng chiều dài và chiều rộng con trượt, P là áp suất thuỷ động được chuẩn hoá bằng "
        "áp suất môi trường, H là khoảng cách giữa ABS và bề mặt môi trường được chuẩn hoá bằng chiều "
        "cao bay nhỏ nhất, Q là hệ số trượt phân tử, T là thời gian được chuẩn hoá bằng chu kỳ ép đặc "
        "trưng, Λ<sub>x</sub> và Λ<sub>y</sub> là các số ổ đỡ theo phương x và y, và σ là số ép. Có thể "
        "tìm thấy một dẫn xuất và giải thích đầy đủ về phương trình Reynolds trong Tài liệu 14. Hiện "
        "nay, các ổ đĩa cứng cao cấp có chiều cao bay cỡ 20 đến 50 nm."))
    b.append(p(
        "Khi mất điện, con trượt trong các ổ kiểu Winchester thường dùng nằm tựa trên bề mặt môi "
        "trường. Tuy ABS và bề mặt môi trường trông phẳng và nhẵn, chúng thực sự gồm các đỉnh và đáy "
        "hiển vi. Nếu mô hình hoá tiếp xúc ABS/môi trường bằng một mặt phẳng và một đầu cầu, chất bôi "
        "trơn lỏng trên bề mặt môi trường gây ra một lực mặt khum F<sub>m</sub> như mô tả trên Hình "
        "96.26 [15]:"))
    b.append(fig(26, F.fig(26)))
    b.append(eq(_eq("vi", "96.28"), "96.28"))
    b.append(p(
        "trong đó R là bán kính của cầu, γ là sức căng bề mặt của chất bôi trơn, θ là góc tiếp xúc "
        "giữa chất bôi trơn và các bề mặt, y là khoảng cách từ cầu tới mặt phẳng, và h là bề dày chất "
        "bôi trơn. Phân tích chi tiết [16] cho thấy ma sát tĩnh F ở mặt phân cách đầu từ/môi trường là "
        "một hàm của nhiều thông số:"))
    b.append(eq(_eq("vi", "96.29"), "96.29"))
    b.append(p(
        "trong đó A là diện tích ABS, η là mật độ đỉnh, E là môđun đàn hồi hiệu dụng, φ là phân bố "
        "chiều cao đỉnh, σ là độ nhám đỉnh hiệu dụng (rms), và s là độ bền cắt vật liệu–vật liệu. Nếu "
        "ma sát F quá lớn, hoặc ổ không khởi động được, hoặc mặt phân cách đầu từ/môi trường bị hỏng. "
        "Trong khi ma sát có thể được giảm trong thực tế bằng cách giảm A, γ và tăng θ, những cách "
        "hiệu quả nhất là kiểm soát η, σ, h và φ. Lớp bôi trơn quá mỏng sẽ gây mài mòn, còn quá dày sẽ "
        "gây ma sát lớn. Điều này giới hạn h trong khoảng 1 đến 3 nm. σ được kiểm soát bằng cách tạo "
        "nhám bề mặt. Về lịch sử, nhám bề mặt được tạo bằng các kỹ thuật cơ khí dùng hạt mài tự do "
        "hoặc hạt mài cố định. Cách này để lại một bề mặt có đặc trưng ngẫu nhiên và không thích hợp "
        "để kiểm soát η và φ. Gần đây, người ta bắt đầu dùng laser [17]. Kỹ thuật này tạo ra một bề "
        "mặt nhám với η và φ được xác định rõ để cải thiện hiệu năng mài mòn và ma sát. Hình 96.27 cho "
        "thấy ảnh AFM của một bề mặt nhám cơ khí và một bề mặt nhám bằng laser."))
    b.append(fig(27, F.fig(27)))

    b.append(h3("Ghi quang", "Optical Recording"))
    b.append(p(
        "Trở ngại chính để đạt mật độ diện tích cao hơn trong ghi từ là số hạng tổn hao khoảng cách. "
        "Giữ đầu từ và môi trường ở rất gần nhau trong khi vẫn duy trì mặt phân cách đầu từ/môi trường "
        "đáng tin cậy và bền là một thách thức kỹ thuật lớn. Cũng phải cẩn thận khi xử lý môi trường "
        "từ vì ngay cả nhiễm bẩn hay vết xước nhỏ cũng có thể phá huỷ thông tin đã ghi. Ngoài ra, kỹ "
        "thuật servo dùng các hình mẫu từ giới hạn mật độ rãnh thấp hơn mật độ tuyến tính khoảng một "
        "bậc. Ngược lại, ghi quang hứa hẹn giải quyết mọi mối lo này."))
    b.append(p(
        "Ghi quang có thể được phân thành ba nhóm. Ở nhóm thứ nhất, thông tin được lưu vào môi trường "
        "trong quá trình chế tạo. Người dùng có thể đọc lại thông tin nhưng không thể thay đổi hay ghi "
        "thông tin mới. CD-ROM (đĩa compac – bộ nhớ chỉ đọc) thuộc nhóm này. Nhóm thứ hai là WORM (ghi "
        "một lần, đọc nhiều lần). Thay vì ghi thông tin trong quá trình chế tạo, nó để bước này cho "
        "người dùng. Điều này thường đạt được bằng cách tạo các lỗ hoặc bọng vật lý trong môi trường "
        "trong quá trình ghi. Tuy nhiên, một khi đã ghi, môi trường hành xử như nhóm thứ nhất: không "
        "thể ghi thêm. Nhóm thứ ba tương tự ghi từ. Có thể ghi vô hạn lần lên môi trường bằng cách "
        "thay đổi pha hoặc từ độ của môi trường. Ví dụ đáng chú ý nhất trong nhóm này là kỹ thuật từ "
        "quang (MO) [18]. Chỉ CD-ROM và ghi từ quang được mô tả dưới đây."))

    b.append(h4("CD-ROM", "CD-ROM"))
    b.append(p(
        "Hình 96.28 cho thấy nguyên lý đọc lại của CD-ROM. Dữ liệu được ép thành các hố và các vùng "
        "phẳng vật lý trên một mặt của một đế nhựa, thường là polycacbonat. Một lớp nhôm được lắng "
        "đọng trên mặt này để làm nó phản xạ. Sau đó một lớp sơn bóng được phủ để bảo vệ lớp nhôm. "
        "Trong quá trình đọc lại, một thấu kính quang học được dùng để hội tụ một chùm laser lên mặt "
        "phản xạ có các hố và vùng phẳng. Đường kính của thấu kính là D, khoảng cách giữa thấu kính và "
        "đế là h<sub>3</sub>, và bề dày đế là h<sub>2</sub>. Đường kính của chùm laser là "
        "d<sub>2</sub> khi đi vào đế, và trở thành d<sub>1</sub> khi hội tụ trên mặt phản xạ. Chiều "
        "rộng của các hố được thiết kế nhỏ hơn d<sub>1</sub>. Ánh sáng phản xạ gồm hai phần: "
        "I<sub>1</sub> từ vùng phẳng và I<sub>2</sub> từ hố. Theo lý thuyết giao thoa, cường độ của "
        "ánh sáng phản xạ là"))
    b.append(eq(_eq("vi", "96.30"), "96.30"))
    b.append(p(
        "trong đó λ là bước sóng của laser và h<sub>1</sub> ≈ λ/4 là chiều cao hố. Điều này dẫn tới"))
    b.append(eq(_eq("vi", "96.31"), "96.31"))
    b.append(p(
        "Sự thay đổi cường độ ánh sáng này được phát hiện và giải mã để thu được dữ liệu đã ghi. Ánh "
        "sáng phản xạ cũng được dùng để hội tụ và bám rãnh."))
    b.append(fig(28, F.fig(28)))
    b.append(p(
        "Giới hạn cơ bản của mật độ ghi quang là đường kính chùm tia hội tụ d<sub>1</sub>. Với một "
        "laser Gauss (TEM<sub>00</sub>), đây là đường kính giới hạn nhiễu xạ, tại đó cường độ ánh sáng "
        "giảm còn 1/e<sup>2</sup> cường độ đỉnh:"))
    b.append(eq(_eq("vi", "96.32"), "96.32"))
    b.append(p(
        "trong đó θ là góc khẩu độ. Những giá trị sau là điển hình cho một hệ CD-ROM: λ (laser arsenua "
        "gali) = 780 nm, θ = 27°, h<sub>2</sub> = 1,2 mm, D = 5 mm, h<sub>3</sub> = 4,2 mm. Điều này "
        "cho d<sub>1</sub> ≈ 1,0 µm và d<sub>2</sub> ≈ 0,7 mm, và đặt giới hạn mật độ diện tích của "
        "ghi quang (kể cả từ quang) vào khoảng 1 Mbit/mm<sup>2</sup>. Với phần lớn ứng dụng CD-ROM, mật "
        "độ diện tích nhỏ hơn giới hạn này, và một đĩa đường kính 120 mm chứa khoảng 600 Mbyte thông "
        "tin. Để tăng mật độ diện tích, ta có thể giảm bước sóng ánh sáng hoặc tăng khẩu độ số. Phần "
        "lớn nỗ lực là áp dụng một nguồn sáng mới có bước sóng ngắn như laser xanh. Tăng khẩu độ số khó "
        "hơn vì tăng đường kính thấu kính là quá đắt và giảm h<sub>2</sub> hay h<sub>3</sub> bị giới "
        "hạn bởi độ tin cậy. Lưu ý rằng tuy kích thước chùm tia trên mặt phẳng hội tụ cỡ 1 µm "
        "(d<sub>1</sub>), nó lớn hơn hai đến ba bậc tại mặt phân cách không khí/đế (d<sub>2</sub>). "
        "Điều này có nghĩa ghi quang chịu được nhiễm bẩn và vết xước trên bề mặt đĩa tốt hơn nhiều so "
        "với ghi từ. Tuy nhiên, hiệu năng của ghi quang nói chung không sánh được với ghi từ. Tốc độ "
        "truyền dữ liệu của ổ CD-ROM được biểu thị bằng bội số (×) của 150 kB/s. Ngay cả với ổ CD-ROM "
        "12×, thời gian truy xuất dữ liệu và tốc độ truyền dữ liệu vẫn cỡ 100 ms và 1,8 MB/s, trong "
        "khi với một ổ đĩa cứng hiệu năng cao các giá trị này lần lượt dưới 10 ms và trên 30 MB/s."))

    b.append(h4("Ghi từ quang", "Magnetooptic Recording"))
    b.append(p(
        "Nhược điểm chính của CD-ROM đối với người dùng cuối là không ghi được. Khiếm khuyết này được "
        "khắc phục bằng công nghệ ghi MO, như mô tả trên Hình 96.29. Một chùm laser phân cực tuyến "
        "tính được hội tụ lên một lớp vật liệu từ, và một cuộn dây cung cấp một từ trường một chiều ở "
        "phía bên kia của môi trường. Từ trường một chiều này quá yếu để ảnh hưởng tới từ độ của môi "
        "trường ở nhiệt độ thường. Quá trình ghi tận dụng tính chất từ nhiệt của môi trường, và quá "
        "trình đọc lại đạt được nhờ hiệu ứng Kerr. Trong khi ghi, môi trường ban đầu được từ hoá theo "
        "phương thẳng đứng theo một hướng, và từ trường một chiều theo hướng ngược lại. Laser đốt nóng "
        "môi trường tới nhiệt độ Curie, tại đó lực kháng từ trở nên bằng không. Trong quá trình làm "
        "nguội, từ trường một chiều sắp xếp từ độ của vùng bị đốt nóng theo hướng của từ trường. Trong "
        "quá trình đọc lại, cùng laser đó được dùng với cường độ nhỏ hơn. Môi trường được đốt nóng tới "
        "nhiệt độ bù trừ, tại đó lực kháng từ trở nên cực cao. Tuỳ hướng của từ độ, phân cực của ánh "
        "sáng phản xạ bị quay theo chiều kim đồng hồ hoặc ngược chiều kim đồng hồ (quay Kerr). Sự quay "
        "phân cực này được phát hiện và giải mã để lấy dữ liệu. Nhược điểm chính của ghi MO là cần một "
        "quá trình xoá riêng để từ hoá môi trường theo một hướng trước khi ghi. Gần đây một số công "
        "nghệ đã được phát triển để loại bỏ quá trình xoá riêng này, với cái giá là sự phức tạp."))
    b.append(p(
        "Môi trường dùng trong ghi MO phải có nhiệt độ Curie thấp hợp lý (&lt; 300 °C). Các vật liệu có "
        "tính chất này là hợp kim kim loại chuyển tiếp đất hiếm, như Tb<sub>23</sub>Fe<sub>77</sub> và "
        "Tb<sub>21</sub>Co<sub>79</sub>. Đáng tiếc, tính chất của các vật liệu này suy giảm trong môi "
        "trường có oxy và hơi ẩm. Để bảo vệ chúng khỏi không khí và độ ẩm, chúng được kẹp giữa một lớp "
        "phủ và một lớp nền, như SiO, AlN, SiN và TiO<sub>2</sub>. Một vấn đề khác với hợp kim kim loại "
        "chuyển tiếp đất hiếm là góc quay Kerr nhỏ, khoảng 0,3°. Để tăng góc quay Kerr này, người ta "
        "dùng nhiều lớp. Trong cấu trúc gọi là bốn lớp (Hình 96.29b), lớp phủ dày khoảng nửa bước sóng "
        "và lớp nền dày khoảng một phần tư bước sóng [18]. Lớp MO rất mỏng (≈ 3 nm). Ánh sáng phản xạ "
        "từ gương phản xạ lệch pha với ánh sáng phản xạ từ bề mặt lớp MO, và cùng pha với ánh sáng "
        "phản xạ từ bên trong lớp MO. Kết quả là góc quay Kerr hiệu dụng tăng lên vài lần."))
    b.append(fig(29, F.fig(29)))
    b.append(p(
        "So với ghi từ, ghi quang có những ưu điểm nội tại là độ tin cậy và tính khả chuyển vượt trội. "
        "Tuy nhiên, hiệu năng của nó kém hơn do thời gian truy xuất dữ liệu và tốc độ truyền chậm hơn. "
        "Một ưu điểm khác của ghi quang — mật độ diện tích cao hơn — đã và đang mất dần, thậm chí đảo "
        "ngược so với ghi từ. Cả ghi từ và ghi quang sẽ tiếp tục được cải thiện trong tương lai gần, "
        "có lẽ theo những hướng ứng dụng khác nhau. Hiện nay có một số kỹ thuật mới đang cố kết hợp "
        "hai kỹ thuật ghi từ và ghi quang. Bảng 96.11 là một danh sách ngắn các thiết bị từ và quang "
        "tiêu biểu cho ghi số."))
    b.append(table(*_t11("vi")))

    b.append(h3("Tài liệu tham khảo (96.3)", "References"))
    b.append(refs([
        "C. D. Mee và E. D. Daniel (chủ biên), <i>Magnetic Storage Handbook</i>, tái bản lần 2, "
        "New York: McGraw-Hill, 1996.",
        "O. Karlqvist, “Calculation of the magnetic field in the ferromagnetic layer of a magnetic "
        "drum,” <i>Trans. R. Inst. Technol. (Stockholm)</i>, 86, 3–28, 1954.",
        "J. J. Miyata và R. R. Tartel, “The recording and reproduction of signals on magnetic medium "
        "using saturation-type recording,” <i>IRE Trans. Elec. Comp.</i>, EC-8, 159–169, 1959.",
        "M. L. Williams và R. L. Comstock, “An analytical model of the write process in digital "
        "magnetic recording,” <i>A.I.P. Conf. Proc.</i>, 5, 738–742, 1972.",
        "V. A. J. Maller và B. K. Middleton, “A simplified model of the writing process in saturation "
        "magnetic recording,” <i>IERE Conf. Proc.</i>, 26, 137–147, 1973.",
        "H. N. Bertram, <i>Theory of Magnetic Recording</i>, Cambridge, Anh: Cambridge University "
        "Press, 1994.",
        "C. D. Mee và E. D. Daniel (chủ biên), <i>Magnetic Recording Technology</i>, tái bản lần 2, "
        "New York: McGraw-Hill, 1996.",
        "R. Potter, “Digital magnetic recording theory,” <i>IEEE Trans. Magn.</i>, MAG-10, 502–508, "
        "1974.",
        "W. K. Westmijze, “Studies on magnetic recording,” <i>Philips Res. Rep.</i>, 8, 161–183, 1953.",
        "G. J. Fan, “A study of the playback process of a magnetic ring head,” <i>IBM J. Res. Dev.</i>, "
        "5, 321–325, 1961.",
        "J. C. Mallinson, <i>The Foundations of Magnetic Recording</i>, tái bản lần 2, San Diego, CA: "
        "Academic Press, 1993.",
        "M. S. Roden, <i>Analog and Digital Communication Systems</i>, tái bản lần 4, Upper Saddle "
        "River, NJ: Prentice-Hall, 1996.",
        "P. A. Franaszek, “Run-length-limited variable length coding with error propagation "
        "limitation,” Bằng sáng chế Hoa Kỳ số 3 689 899, 1972.",
        "W. A. Gross, L. Matsch, V. Castelli, A. Eshel, T. Vohr và M. Wilamann, <i>Fluid Film "
        "Lubrication</i>, New York: Wiley, 1980.",
        "J. N. Israelachvili, <i>Intermolecular and Surface Forces</i>, London: Academic Press, 1985, "
        "224.",
        "Y. Li và F. E. Talke, “A model for the effect of humidity on stiction of the head/disk "
        "interface,” <i>Tribology Mech. Magn. Storage Syst.</i>, SP-27, 79–84, 1990.",
        "R. Ranjan, D. N. Lambeth, M. Tromel, P. Goglia và Y. Li, “Laser texturing for low-flying-"
        "height media,” <i>J. Appl. Phys.</i>, 68, 5745–5747, 1991.",
        "J. Watkinson, <i>The Art of Data Recording</i>, Oxford, Anh: Focal Press, 1994.",
        "G. A. N. Connell và R. Allen, “Magnetization reversal in amorphous rare-earth transition-metal "
        "alloys: TbFe,” <i>Proc. 4th Int. Conf. on Rapidly Quenched Metals</i>, Sendai, Nhật Bản, 1981.",
    ]))

    b.append(h2("Ghi chú của người dịch", "Translator's note"))
    b.append(note(
        "Bản gốc in “Reading/Recording Devices” và chia chương thành ba mục do ba tác giả khác nhau "
        "viết; mỗi mục giữ nguyên hệ quy chiếu, ký hiệu và cách đánh số hình, bảng, phương trình của "
        "riêng nó, nên ở đây cũng vậy. Mục 96.1 không có hình nào và đánh số bảng từ 96.1; mục 96.2 "
        "đánh số hình từ 96.1 và bảng từ 96.6; mục 96.3 đánh số hình từ 96.13, bảng từ 96.8 và phương "
        "trình từ 96.1 — đúng như bản gốc, không đánh số lại. Hai chỗ sai in ấn của bản gốc được giữ "
        "nguyên và ghi lại ở đây: (a) chú thích Hình 96.12 ghi 45 µs trong khi hình vẽ ghi 50 µs; "
        "(b) đoạn nói về quét liên tục khẳng định hai sóng sin lệch pha 90° luôn có tổng bằng không, "
        "điều chỉ đúng với lệch pha 180°. Ngoài ra, phần nói về lấy mẫu đồng thời trong bản in dùng "
        "đơn vị “ms” cho các khoảng 5 µs và 5 ns; bản dịch ghi đúng µs và ns theo đúng hình 96.11 và "
        "theo phép tính 1/200 kS/s. Các đơn vị độ dài trong bản gốc dùng µm ở những chỗ liên quan tới "
        "mật độ diện tích (B &lt; 0,1 µm, w = 3,5 µm) và nm cho bề dày lớp từ."))

    return "".join(b)



# ================================================================ English

def body_en():
    b = []

    # ---------------------------------------------------------------- 96.1
    b.append(h2("96.1 Graphic Recorders"))
    b.append(p(
        "A graphic recorder is essentially a measuring apparatus that is able to produce in real time a "
        "hard copy of a set of time functions with the purpose of immediate and/or later visual "
        "inspection. The curves are mostly drawn on a (long) strip of paper (from a roll or Z-fold); as "
        "such, the instrument is indicated as a strip chart recorder. The independent variable time (t) "
        "then corresponds to the strip length axis and the physical variables measured are related to "
        "the chart width. Tracings are obtained by a writing process at sites on the chart short axis "
        "(y) corresponding to the physical variable magnitudes with the strip being moved at constant "
        "velocity to generate the time axis. Graphs cannot be interpreted if essential information is "
        "absent; scales and reference levels for each physical variable recorded and for time are all a "
        "necessity."))
    b.append(p(
        "Additional information concerning the experimental conditions of the recording is also "
        "necessary and is preferably printed by the apparatus (date, investigated item, type of "
        "experiment, etc.). The capacity of the graphic recorder is thus determined by its measuring "
        "accuracy, its ability to report additional information and its graphical quality, including "
        "the sharpness of tracings, the discriminability of tracings (e.g., by different colors), and "
        "the stability of quality with respect to long-term storage."))
    b.append(p(
        "Simple chart recorders only produce tracings on calibrated paper; more-advanced graphic "
        "recorders generate tracings and calibration lines, display additional information in "
        "alphanumeric form on charts, store instrument settings and recorded data in memory (which can "
        "be reproduced on charts in diverse modes), have a built-in waveform monitor screen, and can "
        "communicate with a PC via standard serial interfacing. The borderlines between these types of "
        "intelligent graphic recorders and, on the one hand, digital storage oscilloscopes equipped "
        "with a hard copy unit and, on the other hand, PC-based data acquisition systems with a laser "
        "printer or a plotter, become very unclear. The property of producing the hard copy in real "
        "time is probably the most discriminating factor between the graphic recorder and other "
        "measuring systems that produce hard copies. Graphic recorders are used for test and "
        "measurement applications in laboratory and field conditions and for industrial process "
        "monitoring and control. Graphic recorders are intensively used in biomedical measurement "
        "applications [1]."))
    b.append(p(
        "Whereas the time axis is generated by moving the chart at constant velocity, the ordinate can "
        "be marked in an analog or a digital manner. Analog recorder transducers generate a physical "
        "displacement of the writing device, e.g., a pen or a printhead. With digital transducers, "
        "moving parts are absent and the writing device is a stationary rectilinear array of "
        "equidistant writing points covering the complete width of the chart; the writing act then "
        "consists in activating the point situated at the site corresponding to the signal magnitude and "
        "putting a dot on the paper. Analog recorders thus can produce continuous lines, whereas "
        "digital recorders generate dotted lines. If ordinate and time axis resolutions are sufficient, "
        "digital recordings have excellent graphic quality regarding visual impression of continuity."))
    b.append(p(
        "Analog transducers can be used in a discontinuous mode and thus handle a set of slowly varying "
        "signals; during the scanning cycle a dot is set on the paper by the moving writing device at "
        "the sites corresponding to the magnitudes of the signal. A single digital transducer and a "
        "single analog transducer applied in the scanning mode can handle a set of signals; a single "
        "analog transducer can process only one signal in the continuous mode. For a digital transducer "
        "the number of signals recorded is essentially unlimited; it is thus programmed to draw the "
        "necessary calibration lines. With analog transducers calibrated paper is used. In this case, "
        "generally ink writing is applied and different colors ensure excellent tracing "
        "identifiability. With the digital array, dot printing can be more or less intensified for "
        "different channels or more than one adjacent points can be activated, resulting in more or "
        "less increased line blackness and thickness. However, tracing identification is usually "
        "performed by alphanumeric annotations."))
    b.append(p(
        "In analog graphic recorders, the transducer can be designed in a direct mode or in a servo "
        "mode. In the direct mode the signal magnitude is directly transduced to a position of the "
        "writing device (e.g., the simple galvanometric type). In the servo mode (also called feedback "
        "or compensation) the position of the writing device is measured by a specific sensor system "
        "and the difference between the measured value and the value of the signal to be traced is "
        "applied to the transducer motor, resulting in a movement tending to zero the difference value "
        "and thus to correct the position [2,3]. In both methods the moving parts set a limit to the "
        "system frequency bandwidth. Moreover, in the feedback mode velocity and acceleration "
        "limitations may be present; thus linear system theory description of the apparatus behavior "
        "with respect to signal frequency may not be applicable. As such, the bandwidths of servo "
        "systems can be dependent on the writing width."))
    b.append(p(
        "Movement of the writing device can be generated by a rotation or by a translation. In the "
        "latter case the writing part is mechanically guided; primarily, the servo method is applied "
        "[3]. A rotation is generally obtained with a galvanometric motor type [3,4]; the galvanometer "
        "may rotate a pen, an ink jet, a light beam. The inertia of the moving part is the major "
        "parameter determining the bandwidth of the system. Translational devices allow a bandwidth of "
        "a few hertz. Higher bandwidths can be obtained with galvanometric pen types (about 100 Hz), "
        "ink jets (up to 1 kHz), and optical systems (up to 10 kHz) [1], but, being replaced by dot "
        "array recorders or data acquisition systems, these types are disappearing from the market. "
        "Major reasons are inherent errors and limitations of these analog types, maintenance needs of "
        "moving parts and ink devices, cost of photographic paper, and the lack of the possibilities of "
        "digital types."))
    b.append(p(
        "Whereas moving parts restrict the analog recorder bandwidth, a corresponding capacity of "
        "digital graphic recorders is determined by the sampling frequency and the writing frequency. "
        "According to the sampling criterion the sampling frequency should be twice the highest signal "
        "frequency. This implies two samples to display a complete sine wave period, which can hardly "
        "be called a good graphic representation. Ten samples may be a minimum. The sampling frequency "
        "is a pure electronic matter; the maximal writing frequency of the dot array is the limiting "
        "factor in real time. Alternatively, if the signal spectrum exceeds the real-time bandwidth of "
        "the recorder, data can be stored at a sufficient sampling rate in memory and reproduced "
        "off-line at a slower rate which can be handled by the apparatus. Most digital recorders have "
        "this memory facility; some recorders are specifically referred to as “memory” recorders when "
        "their off-line capabilities largely exceed their online performance."))
    b.append(p(
        "Real-time recording is primarily performed as a function of time (t–y recorders). On the other "
        "hand, x–y recording is another way of representing the data. In this case the relation between "
        "two physical variables is traced and the independent variable time is excluded (apart from the "
        "fact that, if a dashed line is used, each dash can represent a fixed time interval). In "
        "standard analog x–y recorders the chart is stationary (e.g., electrostatically fixed to the "
        "writing table); two similar analog writing transducers with identical input circuitry are "
        "assembled in the recorder. The first transducer (y) translates a long arm covering the width of "
        "the paper at which the second transducer (x) carrying the pen is moved. Evidently, recorders "
        "with memory facilities and appropriate software may produce an x–y recording in off-line mode "
        "by setting dots while the paper progresses."))
    b.append(p(
        "Recording accuracy can be formulated in similar terms as for any measuring instrument [5]. This "
        "accuracy is determined, on the one hand, by the input signal conditioning, similar for digital "
        "as well as for analog types and, on the other hand, by the accuracy of the recording transducer "
        "and its driver electronics. In the digital type, digitization bit accuracy, sampling frequency, "
        "dot array resolution, and dot writing frequency are major parameters. In the analog type, "
        "typical inconveniences of analog transducer systems can be found (such as static nonlinearity, "
        "noise and drift, dead zone and hysteresis, limited dynamic behavior); servo systems are known "
        "to be more accurate as compared with direct systems. For example, drift in analog recording can "
        "be the result of a small shift of the calibrated chart along the y-axis; the latter is excluded "
        "if the recorder draws its own calibration lines."))
    b.append(p(
        "With respect to graphic quality, clarity and sharpness of the tracings are important (within a "
        "large range of writing velocities). Tracing quality depends on the writing velocity, i.e., the "
        "velocity of the writing device with respect to the moving paper. Evidently, the flow of writing "
        "medium (e.g., ink or heat) should be more or less adapted to this writing velocity to prevent "
        "poorly visible tracings at high velocities and thick lines at low velocities. Good "
        "identifiability of overlapping curves is essential. Sufficient dot resolution (with adequate "
        "interpolation techniques) is important in discontinuous types for easy visual inspection."))
    b.append(p(
        "A graphic recorder can be designed as a single-channel instrument or can have a multichannel "
        "input. Inputs can be standard or modular, so that the user can choose the specific signal "
        "conditioners for the application and the number of channels. A recorder can be called “general "
        "purpose” or can be assembled in a specific measuring apparatus (e.g., in biomedical "
        "applications such as electrocardiography and electroencephalography). The recorder can be "
        "portable for operation in the field or can be mounted in a laboratory rack or in a control "
        "panel. The paper can be moved vertically or horizontally on a writing table (“flat bed” "
        "recorder) and can be supplied from a roll or in Z-fold. Besides strip chart recorders and x–y "
        "recorders, circular chart recorders exist. In this case the chart rotates, one rotation "
        "corresponds to a complete measurement interval, and the chart is provided with appropriate "
        "calibration lines adapted to movement of the pens writing on it."))
    b.append(p(
        "Apart from the low-bandwidth translational pen devices there is a decreasing interest in analog "
        "graphic recorders. They are being replaced by thermal dot array recorders or by data "
        "acquisition systems. Nevertheless, as some of them may still be manufactured and a number of "
        "apparatus may still be in use, different techniques are mentioned. A description of analog "
        "recorder principles and performances can be found in Reference 1. Galvanometric recorders apply "
        "rotational transducers. The direct as well as the servo principles are used. The direct type "
        "makes use of the d’Arsonval movement as applied in ordinary galvanometers [1, 2, 4]. "
        "Dynamically, the galvanometer acts as a mechanical resonant system and the bandwidth is thus "
        "determined by its resonant frequency, the latter being dependent on the inertia of the moving "
        "parts. Evidently, rotation gives rise to inherent errors in graphic recorders. If pen tips "
        "(perpendicular to the pen arm, thermal or ink) are used, the rotation of the pen arm fixed to "
        "the galvanometer coil occurs in a plane parallel to the chart plane, so the recording is "
        "curvilinear instead of rectilinear, introducing an error with respect to the time axis and to "
        "the ordinate axis (the ordinate value being proportional to the tangent of the rotation angle). "
        "Calibrated paper with curvilinear coordinate lines may solve this problem; nevertheless, the "
        "tracing is deformed and zero offset is critical. Rectilinear recording can be realized with pen "
        "systems, ink jets, and light beams. Rectilinear pen recording can be approximated with pen tips "
        "in case of “long-arm” pens and by mechanical rectilinearization; alternatively “knife-edge” "
        "recording is a solution [1]. In the case of ink jet and light beam recorders the rotation plane "
        "and the chart plane do not have to be parallel; writing then occurs at the intersecting line of "
        "both planes and is thus essentially rectilinear. In ink jet recording a miniature nozzle "
        "through which ink is pumped is mounted in a direction perpendicular to the axis of the "
        "galvanometer. In optical recording a sharp light beam is reflected by a small mirror connected "
        "to the galvanometric moving coil toward the photosensitive paper. In these methods "
        "miniaturization of the moving parts gives rise to higher resonant frequencies and thus higher "
        "bandwidths. Whereas a typical bandwidth for a galvanometric pen system is 100 Hz, the bandwidth "
        "for an ink jet system can be 1000 Hz and for an optical system 10 kHz may be reached. In the "
        "fiber-optic cathode ray tube (FO-CRT) no mechanical moving parts are present and thus there are "
        "no mechanical limits on bandwidth. The FO-CRT is essentially a one-dimensional CRT. A phosphor "
        "layer at the inside of the screen converts the cathode ray into ultraviolet (UV) light. This UV "
        "light is guided by an outer faceplate composed of glass fibers onto the photosensitive chart. "
        "As in ordinary oscilloscopes, the deflection of the spot is directly proportional to the signal "
        "applied at the input of the deflection unit. The bandwidth is determined by the driving "
        "electronics. The system can be used in scanning mode as the beam intensity is easily "
        "controlled. In the following paragraphs further details will be given on translational pen "
        "recorders and thermal dot array recorders."))

    b.append(h3("Translational Pen Recorders"))
    b.append(p(
        "In translational pen recorders the writing device is usually a fiber-tip pen with an ink "
        "cartridge. In discontinuous applications the writing device can be a printhead with different "
        "color styli or with a colored ribbon. A manual or automatic pen lift facility is included. "
        "During recording, the writing device is translated along the y-axis as it is linked to a "
        "mechanical guidance and a closed-loop wire system. A motor and wheels system pulls the wire and "
        "thus the writing device. In some designs a motor and screw system is applied. Translational "
        "recorders are primarily designed as a servo type. The position of the pen is accurately "
        "measured, and the difference voltage between the input signal and the position magnitude "
        "(following appropriate amplification and conditioning) drives the servomotor. Servo motors can "
        "be dc or stepper types; servo electronics can be analog or digital. Position sensing can be "
        "potentiometric (“potentiometric” recorders): the pen carriage is equipped with a sliding "
        "contact on the resistor (wire wound or thick film) which covers the complete width of the "
        "paper. More recently developed methods use optical or ultrasonic principles for position "
        "sensing; with these methods contacts are absent resulting in less maintenance and longer "
        "lifetime. For example, in the ultrasonic method the pen position is sensed by a detector coil "
        "from the propagation time of an ultrasound pulse, which is imparted by a piezoelectric "
        "transducer to a magnetostrictive strip covering the chart width. Accordingly, brushless "
        "dc-motors are used in some apparatuses. In the servo system accuracy is determined for the "
        "larger part by the quality of the sensing system. A poor contact with the resistor can give "
        "rise to noise; there may be a mechanical backlash between pen tip and the sliding contact on "
        "the potentiometer. The velocity of the pen carriage is limited, about 0.5 to 2 m/s dependent on "
        "motor and mechanics design. This results in a bandwidth of the recorder depending on the "
        "amplitude of the tracing: the –3 dB frequency fits in the range from 1 to 5 Hz for a "
        "full-scale width of 200 to 250 mm. Alternatively, the pen response time to a full-scale step "
        "input is given (5 to 95% of full-scale tracing): 0.1 to 0.5 s. Overshoot of the pen step "
        "response is extremely small in accurate designs."))
    b.append(p(
        "In most pen recorders each tracing can cover the complete width. As such, pens must have the "
        "possibility to pass each other resulting in a small shift between adjacent pens (a few "
        "millimeters) along the time axis. In some apparatus, tracings can be synchronized with a "
        "POC-system (“pen offset compensation”); signals are digitized, stored in memory, and reproduced "
        "after a time delay correcting for the physical displacement of the pen. If immediate visual "
        "inspection is required, applying POC can be inconvenient as a consequence of this time delay. "
        "In process monitoring, slowly varying signals such as temperature, pressure, flow, etc. are "
        "followed. These signals can be handled by a single transducer in a discontinuous way; all input "
        "signals are scanned during the scanning cycle and for each signal a dot is printed "
        "(“multipoint” recorder). The minimum scanning time is dependent on the moving writing device. "
        "For chart progression, dc and stepper motors are used. Calibrated paper is pulled by sprocket "
        "wheels seizing in equidistant perforations at both sides of the chart. Translational pen "
        "recorders range from simple purely analog design to intelligent microprocessor-controlled types "
        "handling a large number of channels with a broad range of control and monitor facilities (e.g., "
        "printing of a report after alarm). Table 96.1 displays a set of translational pen recorders; "
        "some of them are equipped with a printhead. Under “Description” the major application is given: "
        "test and measurement or process monitoring. Furthermore the following are indicated: the number "
        "of continuous (c. ch.) and scanned (s. ch.) channels; the availability of POC, a printer (for "
        "additional information or for trace printing), a display for alphanumeric information (such as "
        "calibration values for each channel), or even a waveform display, data memory (allowing memory "
        "recorder functioning), x–y recording facility, alarm generation (after reaching thresholds of "
        "recorded variables), and standard serial interface options allowing communication with a PC "
        "(introduction of recorder settings, storage, and processing of recorded data, etc.). Table 96.2 "
        "gives a summary of pen recorder specifications (multipoint types also included)."))
    b.append(table(*_t1("en")))
    b.append(table(*_t2a("en")))
    b.append(table(*_t2b("en")))

    b.append(h3("Thermal Dot Array Recorders"))
    b.append(p(
        "In thermal dot array recorders, apart from the chart-pulling system, no moving parts are "
        "present; the writing transducer is essentially a rectilinear array of equidistant writing "
        "points which covers the total width of the paper. Although some apparatuses apply an "
        "electrostatic method [1], the thermal dot array and thermosensitive paper are generally used. "
        "In this array the writing styli consist of miniature electrically heated resistances; thermal "
        "properties of the resistances (in close contact with the chart paper) and the electric "
        "activating pulse form determine the maximal writing frequency. The latter ranges in real-time "
        "recorders from 1 to 6.4 kHz. Heating of the thermosensitive paper results in a black dot with "
        "good long-term stability. The heating pulse is controlled in relation to the chart velocity in "
        "order to obtain sufficient blackness at high velocities. Tracing blackness or line thickness is "
        "seldom used for curve identification; alphanumeric annotation is mostly applied. With the dot "
        "array a theoretically unlimited number of waveforms can be processed; the apparatus is thus "
        "programmed to draw its own calibration lines. Different types of grid patterns can be selected "
        "by the user. Moreover, alphanumeric information can be printed for indicating experimental "
        "conditions."))
    b.append(p(
        "Ordinate axis resolution is determined by the dot array: primarily, 8 dots/mm; exceptionally, "
        "12 dots/mm (as in standard laser printers). The resolution along the abscissa depends on the "
        "thermal array limitations and programming. Generally, a higher resolution is used (mostly 32 "
        "dots/mm, maximally 64 dots/mm) except for the highest chart velocities (100, 200, 500 mm/s). At "
        "these high velocities and consequently short chart contact times, dots become less sharp and "
        "less black. Most of the dot array instruments are intended for high-signal-frequency "
        "applications: per channel sampling frequencies of 100, 200, and even 500 kHz are used in real "
        "time. These sampling frequencies largely exceed the writing frequencies; during the writing "
        "cycle, data are stored in memory and for each channel within each writing interval a dotted "
        "vertical line is printed between the minimal and the maximal value. For example, a sine wave "
        "with a frequency largely exceeding the writing frequency is represented as a black band with a "
        "width equal to the sine amplitude. In this way the graphs indicate the presence of a phenomenon "
        "with a frequency content exceeding the writing frequency. As data are stored in memory they can "
        "be reproduced at a lower rate thus revealing the actual high-frequency waveform captured. Some "
        "apparatuses use a much lower sampling rate in real time and only perform off-line: in this case "
        "the apparatus is indicated as a “memory” recorder. Digitization accuracy ranges from 8 to 16 "
        "bit, whereas the largest number of dots full scale is 4800. In this way the useful signal may "
        "be superposed on a large dc-offset: it can be written or reproduced with excellent graphic "
        "quality with the offset digitally removed and the scale adapted."))
    b.append(p(
        "In a high-performance recorder a waveform display is extremely useful to avoid paper spoiling, "
        "in real-time and in off-line recording as well. The display is also used for apparatus "
        "settings. Signals can be calibrated and real physical values and units can be printed at the "
        "calibration lines. Via memory x–y plots can be obtained. Some apparatuses allow application of "
        "mathematical functions for waveform processing and analysis: original and processed waveforms "
        "can be drawn together off-line. A few types are equipped with FFT software. Computer "
        "interfacing, a large set of triggering modes (including recording at increased velocity after a "
        "specific trigger), event channels, etc. are standard facilities. Table 96.3 shows a set of "
        "thermal dot array recorders (under “Description”: number of analog channels (a. ch.) and digital "
        "channels (d. ch.); waveform monitor; signal data memory, x–y facility, mathematical analysis, "
        "FFT) and Table 96.4 gives specifications."))
    b.append(table(*_t3("en")))
    b.append(table(*_t4a("en")))
    b.append(table(*_t4b("en")))

    b.append(h3("Concluding Remarks"))
    b.append(p(
        "Table 96.5 gives addresses and fax and phone numbers of manufacturers of recorders mentioned in "
        "Tables 96.1 and 96.3. It should be remarked that prices mentioned in these tables hold for "
        "purchasing a complete functioning apparatus (number of channels indicated) from firms in "
        "Belgium representing the manufacturers and having provided the data sheets from which "
        "specifications were derived. With the expression “a complete functioning” apparatus a standard "
        "system is meant, thus including simple input couplers (in case of a modular design), standard "
        "RAM and analysis software, no specific options. Obviously, the list of manufacturers is "
        "incomplete. It should be mentioned that the number of manufacturers of graphic recorders is "
        "decreasing; a significant and increasing amount of applications has been taken over by "
        "“paperless” recorders, i.e., data acquisition systems. Nevertheless, the possibility of "
        "generating graphs in real time remains an important feature, e.g., to provide evidence of the "
        "presence of a specific phenomenon. In recent years analog recorders have become less used and "
        "manufactured (apart from the translational pen types, especially in industrial process "
        "monitoring). Thermal array recorders have become more important: the quality and long-term "
        "stability of thermal paper have improved and cost levels are comparable with calibrated paper "
        "for ink recording. In new designs, recorders provide more capabilities and appear more "
        "intelligent, obviously leading to increased complications with respect to instrument settings "
        "and thus increased need for training and experience in the use of the instrument."))
    b.append(table(*_t5("en")))

    b.append(h3("Defining Terms"))
    b.append(dt("Analog graphic recorder",
                "a graphic recorder that makes use of an analog transducer system (e.g., a moving pen)."))
    b.append(dt("Analog recorder bandwidth",
                "the largest frequency that can be processed by the analog recorder (–3 dB limit)."))
    b.append(dt("Digital graphic recorder",
                "a graphic recorder that makes use of a digital transducer system (e.g., a fixed dot "
                "array)."))
    b.append(dt("Graphic recorder",
                "a measuring apparatus that produces in real time a hard copy of a set of time-dependent "
                "variables."))
    b.append(dt("Maximal sampling frequency",
                "maximal number of data points sampled by the digital recorder per time unit (totally "
                "or per channel)."))
    b.append(dt("Maximal writing frequency",
                "maximal number of writing (or printing) acts executed by the digital recorder per time "
                "unit."))
    b.append(dt("Thermal dot array recorder",
                "a digital recorder applying a fixed thermal dot array perpendicular to the time axis."))
    b.append(dt("Translational pen recorder",
                "an analog recorder with one or several pens being translated perpendicular to the time "
                "axis."))

    b.append(h3("References (96.1)"))
    b.append(refs([
        "H. Vermariën, “Recorders, graphic,” in J. G. Webster, Ed., <i>Encyclopedia of Medical Devices "
        "and Instrumentation</i>, New York: John Wiley &amp; Sons, 1988.",
        "D. A. Bell, <i>Electronic Instrumentation and Measurements</i>, 2nd ed., Englewood Cliffs, NJ: "
        "Prentice-Hall, 1994.",
        "A. Miller, O. S. Talle, and C. D. Mee, “Recorders,” in B. M. Oliver and J. M. Cage, Eds., "
        "<i>Electronic Measurements and Instrumentation</i>, New York: McGraw-Hill, 1975, 427–479.",
        "R. J. Smith, <i>Circuits, Devices and Systems: A First Course in Electrical Engineering</i>, "
        "New York: John Wiley &amp; Sons, 1976.",
        "W. H. Olson, “Basic concepts in instrumentation,” in J. G. Webster, Ed., <i>Medical "
        "Instrumentation: Application and Design</i>, 3rd ed., New York: John Wiley &amp; Sons, 1998.",
    ]))

    # ---------------------------------------------------------------- 96.2
    b.append(h2("96.2 Data Acquisition Systems"))
    b.append(p(
        "The fundamental task of a data acquisition system is the measurement or generation of "
        "real-world physical signals. Before a physical signal can be measured by a computer-based "
        "system, a sensor or transducer is used to convert the physical signal into an electrical "
        "signal, such as voltage or current. Often only a plug-in data acquisition (DAQ) board is "
        "considered the data acquisition system; however, a board is only one of the components in the "
        "system. A complete DAQ system consists of sensors, signal conditioning, interface hardware, and "
        "software. Unlike stand-alone instruments, signals often cannot be directly connected to the DAQ "
        "board. The signals may need to be conditioned by some signal-conditioning accessory before they "
        "are converted to digital information by the plug-in DAQ board. Software controls the data "
        "acquisition system — acquiring the raw data, analyzing the data, and presenting the results. "
        "The components are shown in Fig. 96.1."))
    b.append(fig(1, F.fig(1), "en"))

    b.append(h3("Signals"))
    b.append(p(
        "Signals are physical events whose magnitude or time variation contains information. DAQ systems "
        "measure various aspects of a signal in order to monitor and control the physical events. Users "
        "of DAQ systems need to know the relation of the signal to the physical event and what "
        "information is available in the signal. Generally, information is conveyed by a signal through "
        "one or more of the following signal parameters: state, rate, level, shape, or frequency "
        "content. The physical characteristics of the measured signals and the related information help "
        "determine the design of a DAQ system."))
    b.append(p(
        "All signals are, fundamentally, analog, time-varying signals. For the purpose of discussing the "
        "methods of signal measurement using a plug-in DAQ board, a given signal should be classified as "
        "one of five signal types. Because the method of signal measurement is determined by the way the "
        "signal conveys the needed information, a classification based on this criterion is useful in "
        "understanding the fundamental building blocks of a DAQ system."))
    b.append(p(
        "As shown in Fig. 96.2, any signal can generally be classified as analog or digital. A digital, "
        "or binary, signal has only two possible discrete levels of interest — a high (on) level and a "
        "low (off) level. The two digital signal types are on–off signals and pulse train signals. An "
        "analog signal, on the other hand, contains information in the continuous variation of the "
        "signal with time. Analog signals are described in the time or frequency domains depending upon "
        "the information of interest. A dc type signal is a low-frequency signal, and if the phase "
        "information of a signal is presented with the frequency information, then there is no "
        "difference between the time or frequency domain representations. The category to which a signal "
        "belongs depends on the characteristic of the signal to be measured. The five types of signals "
        "can be closely paralleled with the five basic types of signal information — state, rate, level, "
        "shape, and frequency content. Basic understanding of the signal representing the physical event "
        "being measured and controlled assists in the selection of the appropriate DAQ system."))
    b.append(fig(2, F.fig(2), "en"))

    b.append(h3("Plug-In DAQ Boards"))
    b.append(p(
        "The fundamental component of a DAQ system is the plug-in DAQ board. These boards plug directly "
        "into a slot in a PC and are available with analog, digital, and timing inputs and outputs (I/O). "
        "The most versatile of the plug-in DAQ boards is the multifunction I/O board. As the name "
        "implies, this board typically contains various combinations of analog-to-digital converters "
        "(ADCs), digital-to-analog converters (DACs), digital I/O lines, and counters/timers. ADCs and "
        "DACs measure and generate analog voltage signals, respectively. The digital I/O lines sense and "
        "control digital signals. Counters/timers measure pulse rates, widths, delays, and generate "
        "timing signals. These many features make the multifunction DAQ board useful for a wide range of "
        "applications."))
    b.append(p(
        "Multifunction boards are commonly used to measure analog signals. This is done by the ADC, "
        "which converts the analog voltage level into a digital number that the computer can interpret. "
        "The analog multiplexer (MUX), the instrumentation amplifier, the sample-and-hold (S/H) "
        "circuitry, and the ADC compose the analog input section of a multifunction board (see Fig. "
        "96.3)."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "Typically, multifunction DAQ boards have one ADC. Multiplexing is a common technique for "
        "measuring multiple channels (generally 16 single-ended or 8 differential) with a single ADC. "
        "The analog MUX switches between channels and passes the signal to the instrumentation amplifier "
        "and the S/H circuitry. The MUX architecture is the most common approach taken with plug-in DAQ "
        "boards. While plug-in boards typically include up to only 16 single-ended or 8 differential "
        "inputs, the number of analog input channels can be further expanded with external MUX "
        "accessories."))
    b.append(p(
        "Instrumentation amplifiers typically provide a differential input and selectable gain by "
        "jumpers or software. The differential input rejects small common-mode voltages. The gain is "
        "often software programmable. In addition, many DAQ boards also include the capability to change "
        "the amplifier gain while scanning channels at high rates. Therefore, one can easily monitor "
        "signals with different ranges of amplitudes. The output of the amplifier is sampled, or held at "
        "a constant voltage, by the S/H device at measurement time so that voltage does not change "
        "during digitization."))
    b.append(p(
        "The ADC transforms the analog signal into a digital value which is ultimately sent to computer "
        "memory. There are several important parameters of A/D conversion. The fundamental parameter of "
        "an ADC is the number of bits. The number of bits of an A/D determines the range of values for "
        "the binary output of the ADC conversion. For example, many ADCs are 12-bit, so a voltage within "
        "the input range of the ADC will produce a binary value that has one of 2<sup>12</sup> = 4096 "
        "different values. The more bits that an ADC has, the higher the resolution of the measurement. "
        "The resolution determines the smallest amount of change that can be detected by the ADC. "
        "Resolution is expressed as the number of digits of a voltmeter or dynamic range in decibels, "
        "rather than with bits. Table 96.6 shows the relation among bits, number of digits, and dynamic "
        "range in decibels."))
    b.append(table(*_t6("en")))
    b.append(p(
        "The resolution of the A/D conversion is also determined by the input range of the ADC and the "
        "gain. DAQ boards usually include an instrumentation amplifier that amplifies the analog signal "
        "by a gain factor prior to the conversion. This gain amplifies low-level signals so that more "
        "accurate measurements can be made."))
    b.append(p(
        "Together, the input range of the ADC, the gain, and the number of bits of the board determine "
        "the minimum resolution of the measurement. For example, suppose a low-level ±30 mV signal is "
        "acquired using a 12-bit ADC that has a ±5 V input range. If the system includes an amplifier "
        "with a gain of 100, the resulting resolution of the measurement will be "
        "range/(gain × 2<sup>bits</sup>) = resolution, or 10 V/(100 × 2<sup>12</sup>) = 0.0244 mV."))
    b.append(p(
        "Finally, an important parameter of digitization is the rate at which A/D conversions are made, "
        "referred to as the sampling rate. The A/D system must be able to sample the input signal fast "
        "enough to measure the important waveform attributes accurately. In order to meet this criterion, "
        "the ADC must be able to convert the analog signal to digital form quickly enough."))
    b.append(p(
        "When scanning multiple channels with a multiplexing DAQ system, other factors can affect the "
        "throughput of the system. Specifically, the instrumentation amplifier must be able to settle to "
        "the needed accuracy before the A/D conversion occurs. With multiplexed signals, multiple "
        "signals are being switched into one instrumentation amplifier. Most amplifiers, especially when "
        "amplifying the signals with larger gains, will not be able to settle to the full accuracy of the "
        "ADC when scanning channels at high rates. To avoid this situation, consult the specified "
        "settling times of the DAQ board for the gains and sampling rates required by the application."))

    b.append(h3("Types of ADCs"))
    b.append(p(
        "Different DAQ boards use different types of ADCs to digitize the signal. The most popular type "
        "of ADC on plug-in DAQ boards is the successive approximation ADC, because it offers high speed "
        "and high resolution at a modest cost."))
    b.append(p(
        "Subranging (also called half-flash) ADCs offer very high speed conversion with sampling speeds "
        "up to several million samples per second."))
    b.append(p(
        "The state-of-the-art technology in ADCs is sigma–delta modulating ADCs. These ADCs sample at "
        "high rates, are able to achieve high resolution, and offer the best linearity of all ADCs."))
    b.append(p(
        "Integrating and flash ADCs are mature technologies still used on DAQ boards today. Integrating "
        "ADCs are able to digitize with high resolution but must sacrifice sampling speed to obtain it. "
        "Flash ADCs are able to achieve the highest sampling rate (gigahertz) but are available only with "
        "low resolution. The different types of ADCs are summarized in Table 96.7."))
    b.append(table(*_t7("en")))

    b.append(h3("Analog Input Architecture"))
    b.append(p(
        "With a typical DAQ board, the multiplexer switches among analog input channels. The analog "
        "signal on the channel selected by the multiplexer then passes to the programmable gain "
        "instrumentation amplifier (PGIA), which amplifies the signal. After the signal is amplified, the "
        "sample and hold (S/H) keeps the analog signal constant so that the ADC can determine the digital "
        "representation of the analog signal. A good DAQ board will then place the digital signal in a "
        "first-in first-out (FIFO) buffer, so that no data will be lost if the sample cannot transfer "
        "immediately over the PC I/O channel to computer memory. Having a FIFO becomes especially "
        "important when the board is run under operating systems that have large interrupt latencies, "
        "such as Microsoft Windows."))

    b.append(h3("Basic Analog Specifications"))
    b.append(p(
        "Almost every DAQ board data sheet specifies the number of channels, the maximum sampling rate, "
        "the resolution, and the input range and gain."))
    b.append(p(
        "The number of channels, which is determined by the multiplexer, is usually specified in two "
        "forms — differential and single ended. Differential inputs are inputs that have different "
        "reference points for each channel, none of which is grounded by the board. Differential inputs "
        "are the best way to connect signals to the DAQ board because they provide the best noise "
        "immunity."))
    b.append(p(
        "Single-ended inputs are inputs that are referenced to a common ground point. Because "
        "single-ended inputs are referenced to a common ground, they are not as good as differential "
        "inputs for rejecting noise. They do have a larger number of channels, however. Single-ended "
        "inputs are used when the input signals are high level (greater than 1 V), the leads from the "
        "signal source to the analog input hardware are short (less than 5 m), and all input signals "
        "share a common reference."))
    b.append(p(
        "Some boards have pseudodifferential inputs which have all inputs referenced to the same common "
        "— like single-ended inputs — but the common is not referenced to ground. These boards have the "
        "benefit of a large number of input channels, like single-ended inputs, and the ability to remove "
        "some common-mode noise, especially if the common-mode noise is consistent across all channels. "
        "Differential inputs are still preferable to pseudodifferential, however, because differential "
        "is more immune to magnetic noise."))
    b.append(p(
        "Sampling rate determines how fast the analog signal is converted to a digital signal. When "
        "measuring ac signals, sample at least two times faster than the highest frequency of the input "
        "signal. Even when measuring dc signals, oversample and average the data to increase the accuracy "
        "of the signal by reducing the effects of noise."))
    b.append(p(
        "If the physical event consists of multiple dc-class signals, a DAQ board with interval scanning "
        "should be used. With interval scanning, all channels are scanned at one sample interval (usually "
        "the fastest rate of the board), with a second interval (usually slow) determining the time "
        "before repeating the scan. Interval scanning gives the effects of simultaneously sampling for "
        "slowly varying signals without requiring the additional cost of input circuitry for true "
        "simultaneous sampling."))
    b.append(p(
        "Resolution is the number of bits that are used to represent the analog signal. The higher the "
        "resolution, the higher the number of divisions the input range is broken into, and therefore the "
        "smaller the possible detectable voltage. Unfortunately, some DAQ specifications are misleading "
        "when they specify the resolution associated with the DAQ board. Many DAQ board specifications "
        "state the resolution of the ADC without stating the linearities and noise, and therefore do not "
        "give the information needed to determine the resolution of the entire board. Resolution of the "
        "ADC, combined with the settling time, integral nonlinearity (INL), differential nonlinearity "
        "(DNL), and noise will give an understanding of the accuracy of the board."))
    b.append(p(
        "Input range and gain determine the level of signal that should be connected to the board. "
        "Usually, the range and gain are specified separately, so the two must be combined to determine "
        "the actual signal input range as"))
    b.append(eq("signal input range = range/gain"))
    b.append(p(
        "For example, a board using an input range of ±10 V with a gain of 2 will have a signal input "
        "range of ±5 V. The closer the signal input range is to the range of the signal, the more "
        "accurate the readings from the DAQ board will be. If the signals have different input ranges, "
        "use a DAQ board with the feature of different gains per channel."))

    b.append(h3("Data Acquisition Software"))
    b.append(p(
        "The software is often the most critical component of the DAQ system. Users of DAQ systems "
        "usually program the hardware in one of two ways — through register programming or through "
        "high-level device drivers."))

    b.append(h4("Board Register-Level Programming"))
    b.append(p(
        "The first option is not to use vendor-supplied software and program the DAQ board at the "
        "hardware level. DAQ boards are typically register based; that is, they include a number of "
        "digital registers that control the operation of the board. The developer may use any standard "
        "programming language, such as C, C++, or Visual BASIC, to write series of binary codes to the "
        "DAQ board to control its operation. Although this method affords the highest level of "
        "flexibility, it is also the most difficult and time-consuming, especially for the inexperienced "
        "programmer. The programmer must know the details of programming all hardware, including the "
        "board, the PC interrupt controller, the DMA controller, and PC memory."))

    b.append(h4("Driver Software"))
    b.append(p(
        "Driver software typically consists of a library of function calls usable from a standard "
        "programming language. These function calls provide a high-level interface to control the "
        "standard functions of the plug-in board. For example, a function called SCAN_OP may configure, "
        "initiate, and complete a multiple-channel scanning DAQ operation of a predetermined number of "
        "points. The function call would include parameters to indicate the channels to be scanned, the "
        "amplifier gains to be used, the sampling rate, and the total number of data points to be "
        "collected. The driver responds to this one function call by programming the plug-in board, the "
        "DMA controller, the interrupt controller, and CPU to scan the channels as requested."))

    b.append(h3("What Is Digital Sampling?"))
    b.append(p(
        "Every DAQ system has the task of gathering information about analog signals. To do this, the "
        "system captures a series of instantaneous “snapshots” or samples of the signal at definite time "
        "intervals. Each sample contains information about the signal at a specific instant. Knowing the "
        "exact time of each conversion and the value of the sample, one can reconstruct, analyze, and "
        "display the digitized waveform."))

    b.append(h3("Real-Time Sampling Techniques"))
    b.append(p(
        "In real-time sampling, the DAQ board digitizes consecutive samples along the signal (Fig. "
        "96.4). According to the Nyquist sampling theorem, the ADC must sample at least twice the rate of "
        "the maximum frequency component in that signal to prevent aliasing. Aliasing is a false "
        "lower-frequency component that appears in sampled data acquired at too low a sampling rate. The "
        "frequency at one half the sampling frequency is referred to as the Nyquist frequency. "
        "Theoretically, it is possible to recover information about those signals with frequencies at or "
        "below the Nyquist frequency. Frequencies above the Nyquist frequency will alias to appear "
        "between dc and the Nyquist frequency."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "For example, assume the sampling frequency, f<sub>s</sub>, is 100 Hz. Also assume the input "
        "signal to be sampled contains the following frequencies — 25, 70, 160, and 510 Hz. Figure 96.5 "
        "shows a spectral representation of the input signal."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "The mathematics of sampling theory show us that a sampled signal is shifted in the frequency "
        "domain by an amount equal to integer multiples of the sampling frequency, f<sub>s</sub>. Figure "
        "96.6 shows the spectral content of the input signal after sampling. Frequencies below 50 Hz, "
        "the Nyquist frequency (f<sub>s</sub>/2), appear correctly. However, frequencies above the "
        "Nyquist appear as aliases below the Nyquist frequency. For example, F1 appears correctly; "
        "however, F2, F3, and F4 have aliases at 30, 40, and 10 Hz, respectively."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p("The resulting frequency of aliased signals can be calculated with the following formula:"))
    b.append(eq("Apparent (alias) freq. = ABS (closest integer multiple of sampling freq. − input freq.)"))
    b.append(p("For the example of Figs. 96.5 and 96.6:"))
    b.append(eq("Alias F2 = |100 − 70| = 30 Hz"))
    b.append(eq("Alias F3 = |(2)100 − 160| = 40 Hz"))
    b.append(eq("Alias F4 = |(5)100 − 510| = 10 Hz"))

    b.append(h3("Preventing Aliasing"))
    b.append(p(
        "Aliasing can be prevented by using filters on the front end of the DAQ system. These "
        "antialiasing filters are set to cut off any frequencies above the Nyquist frequency (half the "
        "sampling rate). The perfect filter would reject all frequencies above the Nyquist; however, "
        "because perfect filters exist only in textbooks, one must compromise between sampling rate and "
        "selecting filters. In many applications, one- or two-pole passive filters are satisfactory. The "
        "rule of thumb is to oversample (5 to 10 times) and use these antialiasing filters when frequency "
        "information is crucial."))
    b.append(p(
        "Alternatively, active antialiasing filters with programmable cutoff frequencies and very sharp "
        "attenuation of frequencies above the cutoff can be used. Because these filters exhibit a very "
        "steep roll-off, the DAQ system can sample at two to three times the filter cutoff frequency. "
        "Figure 96.7 shows a transfer function of a high-quality antialiasing filter."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p(
        "The computer uses digital values to recreate or to analyze the waveform. Because the signal "
        "could be anything between each sample, the DAQ board may be unaware of any changes in the signal "
        "between samples. There are several sampling methods optimized for the different classes of "
        "data; they include software polling, external sampling, continuous scanning, multirate "
        "scanning, simultaneous sampling, interval scanning, and seamless changing of the sample rate."))

    b.append(h3("Software Polling"))
    b.append(p(
        "A software loop polls a timing signal and starts the A/D conversion via a software command when "
        "the edge of the timing signal is detected. The timing signal may originate from the internal "
        "clock of the computer or from a clock on the DAQ board. Software polling is useful in simple, "
        "low-speed applications, such as temperature measurements."))
    b.append(p(
        "The software loop must be fast enough to detect the timing signal and trigger a conversion. "
        "Otherwise, a window of uncertainty, also known as jitter, will exist between two successive "
        "samples. Within the window of uncertainty, the input waveform could change enough to reduce the "
        "accuracy of the ADC drastically."))
    b.append(p(
        "Suppose a 100-Hz, 10-V full-scale sine wave is digitized (Fig. 96.8). If the polling loop takes "
        "5 ms to detect the timing signal and to trigger a conversion, then the voltage of the input "
        "sine wave will change as much as 31 mV, [ΔV = 10 sin(2π × 100 × 5 × 10<sup>–6</sup>)]. For a "
        "12-bit ADC operating over an input range of 10 V and a gain of 1, one least significant bit "
        "(LSB) of error represents 2.44 mV:"))
    b.append(fig(8, F.fig(8), "en"))
    b.append(eq("input range/(gain × 2<sup>12</sup>) = 10/(1 × 2<sup>12</sup>) = 2.44 mV"))
    b.append(p(
        "But because the voltage error due to jitter is 31 mV, the accuracy error is 13 LSB."))
    b.append(eq("31 mV/2.44 mV = 13 LSB"))
    b.append(p(
        "This represents uncertainty in the last 4 bits of a 12-bit ADC. Thus, the effective accuracy of "
        "the system is no longer 12 bits but rather 8 bits."))

    b.append(h3("External Sampling"))
    b.append(p(
        "Some DAQ applications must perform a conversion based on another physical event that triggers "
        "the data conversion. The event could be a pulse from an optical encoder measuring the rotation "
        "of a cylinder. A sample would be taken every time the encoder generates a pulse corresponding to "
        "n degrees of rotation. External triggering is advantageous when trying to measure signals whose "
        "occurrence is relative to another physical phenomenon."))

    b.append(h3("Continuous Scanning"))
    b.append(p(
        "When a DAQ board acquires data, several components on the board convert the analog signal to a "
        "digital value. These components include the analog MUX, the instrumentation amplifier, the S/H "
        "circuitry, and the ADC. When acquiring data from several input channels, the analog MUX connects "
        "each signal to the ADC at a constant rate. This method, known as continuous scanning, is "
        "significantly less expensive than having a separate amplifier and ADC for each input channel."))
    b.append(p(
        "Continuous scanning is advantageous because it eliminates jitter and is easy to implement. "
        "However, it is not possible to sample multiple channels simultaneously. Because the MUX "
        "switches between channels, a time skew occurs between any two successive channel samples. "
        "Continuous scanning is appropriate for applications where the time relationship between each "
        "sampled point is unimportant or where the skew is relatively negligible compared with the speed "
        "of the channel scan."))
    b.append(p(
        "If samples from two signals are used to generate a third value, then continuous scanning can "
        "lead to significant errors if the time skew is large. In Fig. 96.9, two channels are "
        "continuously sampled and added together to produce a third value. Because the two sine waves are "
        "90° out-of-phase, the sum of the signals should always be zero. But because of the skew time "
        "between the samples, an erroneous sawtooth signal results."))
    b.append(fig(9, F.fig(9), "en"))

    b.append(h3("Multirate Scanning"))
    b.append(p(
        "Multirate scanning, a method that scans multiple channels at different scan rates, is a special "
        "case of continuous scanning. Applications that digitize multiple signals with a variety of "
        "frequencies use multirate scanning to minimize the amount of buffer space needed to store the "
        "sampled signals. Channel-independent ADCs are used to implement hardware multirate scanning; "
        "however, this method is extremely expensive. Instead of multiple ADCs, only one ADC is used. A "
        "channel/gain configuration register stores the scan rate per channel and software divides down "
        "the scan clock based on the per-channel scan rate. Software-controlled multirate scanning works "
        "by sampling each input channel at a rate that is a fraction of the specified scan rate."))
    b.append(p(
        "Suppose the system scans channels 0 through 3 at 10 kS/s, channel 4 at 5 kS/s, and channels 5 "
        "through 7 at 1 kS/s. A base scan rate of 10 kS/s should be used. Channels 0 through 3 are "
        "acquired at the base scan rate. Software and hardware divide the base scan rate by 2 to sample "
        "channel 4 at 5 kS/s, and by 10 to sample channels 5 through 7 at 1 kS/s."))

    b.append(h3("Simultaneous Sampling"))
    b.append(p(
        "For applications where the time relationship between the input signals is important, such as "
        "phase analysis of ac signals, simultaneous sampling must be used. DAQ boards capable of "
        "simultaneous sampling typically use independent instrumentation amplifiers and S/H circuitry for "
        "each input channel, along with an analog MUX, which routes the input signals to the ADC for "
        "conversion (as shown in Fig. 96.10)."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "To demonstrate the need for a simultaneous-sampling DAQ board, consider a system consisting of "
        "four 50-kHz input signals sampled at 200 kS/s. If the DAQ board uses continuous scanning, the "
        "skew between each channel is 5 µs (1/200 kS/s) which represents a 270° [(15 µs/20 µs) × 360°] "
        "shift in phase between the first channel and fourth channel. Alternatively, with a "
        "simultaneous-sampling board with a maximum 5 ns interchannel time offset, the phase shift is "
        "only 0.09° [(5 ns/20 µs) × 360°]. This phenomenon is illustrated in Fig. 96.11."))
    b.append(fig(11, F.fig(11), "en"))

    b.append(h3("Interval Scanning"))
    b.append(p(
        "For low-frequency signals, interval scanning creates the effect of simultaneous sampling, yet "
        "maintains the cost benefits of a continuous-scanning system. This method scans the input "
        "channels at one rate and uses a second rate to control when the next scan begins. If the input "
        "channels are scanned at the fastest rate of the ADC, the effect of simultaneously sampling the "
        "channels is created. Interval scanning is appropriate for slow-moving signals, such as "
        "temperature and pressure. Interval scanning results in a jitter-free sample rate and minimal "
        "skew time between channel samples. For example, consider a DAQ system with ten temperature "
        "signals. By using interval scanning, a DAQ board can be set up to scan all channels with an "
        "interchannel delay of 5 µs, then repeat the scan every second. This method creates the effect of "
        "simultaneously sampling ten channels at 1 S/s, as shown in Fig. 96.12."))
    b.append(fig(12, F.fig(12), "en"))
    b.append(p(
        "To illustrate the difference between continuous and interval scanning, consider an application "
        "that monitors the torque and RPMs of an automobile engine and computes the engine horsepower. "
        "Two signals, proportional to torque and RPM, are easily sampled by a DAQ board at a rate of "
        "1000 S/s. The values are multiplied together to determine the horsepower as a function of "
        "time."))
    b.append(p(
        "A continuously scanning DAQ board must sample at an aggregate rate of 2000 S/s. The time "
        "between which the torque signal is sampled and the RPM signal is sampled will always be 0.5 ms "
        "(1/2000). If either signal changes within 0.5 ms, then the calculated horsepower is incorrect. "
        "But using interval scanning at a rate of 1000 S/s, the DAQ board samples the torque signal every "
        "1 ms, and the RPM signal is sampled as quickly as possible after the torque is sampled. If a "
        "5-µs interchannel delay exists between the torque and RPM samples, then the time skew is reduced "
        "by 99% [(0.5 ms − 5 µs)/0.5 ms], and the chance of an incorrect calculation is reduced."))

    b.append(h3("Factors Influencing the Accuracy of Measurements"))
    b.append(p(
        "How does one determine if a plug-in DAQ will deliver the required measurement results? With a "
        "sophisticated measuring device like a plug-in DAQ board, significantly different accuracies can "
        "be obtained depending on the type of board used. For example, one can purchase DAQ products on "
        "the market today with 16-bit ADCs and get less than 12 bits of useful data, or one can purchase "
        "a product with a 16-bit ADC and actually get 16 bits of useful data. This difference in "
        "accuracies causes confusion in the PC industry where everyone is used to switching out PCs, "
        "video cards, printers, and so on, and experiencing similar results between equipment."))
    b.append(p(
        "The most important thing to do is to scrutinize more specifications than the resolution of the "
        "ADC that is used on the DAQ board. For dc-class measurements, one should at least consider the "
        "settling time of the instrumentation amplifier, DNL, relative accuracy, INL, and noise. If the "
        "manufacturer of the board under consideration does not supply these specifications in the data "
        "sheets, ask the vendor to provide them or run tests to determine these specifications."))

    b.append(h3("Defining Terms"))
    b.append(dt("Alias",
                "a false lower frequency component that appears in sampled data acquired at too low a "
                "sampling rate."))
    b.append(dt("Asynchronous",
                "(1) Hardware — a property of an event that occurs at an arbitrary time, without "
                "synchronization to a reference clock. (2) Software — a property of a function that "
                "begins an operation and returns prior to the completion or termination of the "
                "operation."))
    b.append(dt("Conversion time",
                "the time required, in an analog input or output system, from the moment a channel is "
                "interrogated (such as with a read instruction) to the moment that accurate data are "
                "available."))
    b.append(dt("DAQ (data acquisition)",
                "(1) Collecting and measuring electric signals from sensors, transducers, and test "
                "probes or fixtures and inputting them to a computer for processing. (2) Collecting and "
                "measuring the same kinds of electric signals with ADC and/or DIO boards plugged into a "
                "PC, and possibly generating control signals with DAC and/or DIO boards in the same PC."))
    b.append(dt("DNL (differential nonlinearity)",
                "a measure in LSB of the worst-case deviation of code widths from their ideal value of "
                "1 LSB."))
    b.append(dt("INL (integral nonlinearity)",
                "a measure in LSB of the worst-case deviation from the ideal A/D or D/A transfer "
                "characteristic of the analog I/O circuitry."))
    b.append(dt("Nyquist sampling theorem",
                "a law of sampling theory stating that if a continuous bandwidth-limited signal "
                "contains no frequency components higher than half the frequency at which it is "
                "sampled, then the original signal can be recovered without distortion."))
    b.append(dt("Relative accuracy",
                "a measure in LSB of the accuracy of an ADC. It includes all nonlinearity and "
                "quantization errors. It does not include offset and gain errors of the circuitry "
                "feeding the ADC."))

    b.append(h3("Further Information"))
    b.append(refs([
        "R. House, “Understanding Important DA Specifications,” <i>Sensors</i>, 10(10), June 1993.",
        "R. House, “Understanding Inaccuracies Due to Settling Time, Linearity, and Noise,” "
        "<i>National Instruments European User Symposium Proceedings</i>, November 10–11, 1994, 11–12.",
        "E. McConnell, “PC-Based Data Acquisition Users Face Numerous Challenges,” <i>ECN</i>, "
        "August 1994.",
        "E. McConnell, “Choosing a Data-Acquisition Method,” <i>Electronic Design</i>, 43(6), 147, 1995.",
        "E. McConnell and D. Jernigan, “Data Acquisition,” in J. C. Whitaker, Ed., <i>The Electronics "
        "Handbook</i>, Boca Raton, FL: CRC Press, 1996, 1795–1822.",
        "D. Potter and A. Razdan, “Fundamentals of PC-Based Data Acquisition,” <i>Sensors</i>, 11(2), "
        "12–20, February 1994.",
        "D. Potter, “Sensor to PC — Avoiding Some Common Pitfalls,” <i>Sensors Expo Proceedings</i>, "
        "September 20, 1994.",
        "D. Potter, “Signal Conditioners Expand DAQ System Capabilities,” <i>I&amp;CS</i>, 25–33, "
        "August 1995.",
        "G. W. Johnson, <i>LabVIEW Graphical Programming</i>, New York: McGraw-Hill, 1994.",
        "E. McConnell, “New Achievements in Counter/Timer Data Acquisition Technology,” <i>MessComp "
        "1994 Proceedings</i>, September 13–15, 1994, 492–498.",
        "E. McConnell, “Equivalent Time Sampling Extends DA Performance,” <i>Sensors Data "
        "Acquisition</i>, Special Issue, June 13, 1995.",
    ]))

    # ---------------------------------------------------------------- 96.3
    b.append(h2("96.3 Magnetic and Optical Recorders"))
    b.append(p(
        "The heart of recording technology is the process of information storage and retrieval. In "
        "addition to its obvious importance in different branches of science and engineering, it has "
        "become indispensable to our daily life. When we make a bank transaction, reserve an airplane "
        "ticket, use a credit card, watch a movie from a video tape, or listen to music from a CD, we are "
        "using the technology of recording. The general requirements for recording are information "
        "integrity, fast access, and low cost. Among the different techniques, the most popularly used "
        "ones are magnetic and optical recording."))
    b.append(p(
        "Typical recording equipment consists of a read/write head, a medium, a coding/decoding system, a "
        "data access system, and some auxiliary mechanical and electronic components. The head and medium "
        "are for data storage and retrieval purposes, and the coding/decoding system is for data error "
        "correction. The data access system changes the relative position between the head and the "
        "medium, usually with a servo mechanism for data track following and a spinning mechanism for "
        "on-track moving. While the data access system and the auxiliary components are important to "
        "recording equipment, they are not considered essential in this chapter to the understanding of "
        "recording technology, and will not be covered. Interested readers are referred to Reference "
        "1."))

    b.append(h3("Magnetic Recording"))
    b.append(p(
        "At present, magnetic recording technology dominates the recording industry. It is used in the "
        "forms of hard disk, floppy disk, removable disk, and tape with either digital or analog mode. In "
        "its simplest form, it consists of a magnetic head and a magnetic medium, as shown in Fig. 96.13. "
        "The head is made of a piece of magnetic material in a ring shape (core), with a small gap facing "
        "the medium and a coil away from the medium. The head records (writes) and reproduces (reads) "
        "information, while the medium stores the information. The recording process is based on the "
        "phenomenon that an electric current i generates a magnetic flux φ as described by Ampère’s law. "
        "The flux φ leaks out of the head core at the gap, and magnetizes the magnetic medium which moves "
        "from left to right with a velocity V under the head gap. Depending on the direction of the "
        "electric current i, the medium is magnetized with magnetization M pointing either left or right. "
        "This pattern of magnetization is retained in the memory of the medium even after the head moves "
        "away."))
    b.append(fig(13, F.fig(13), "en"))
    b.append(p(
        "Two types of head may be used for reproducing. One, termed the inductive head, senses magnetic "
        "flux change rate, and the other, named the magnetoresistive (MR) head, senses the magnetic flux. "
        "When an inductive head is used, the reproducing process is just the reverse of the recording "
        "process. The flux coming out of the magnetized medium surface is picked up by the head core. "
        "Because the medium magnetization under the head gap changes its magnitude and direction as the "
        "medium moves, an electric voltage is generated in the coil. This process is governed by "
        "Faraday’s law. Figure 96.13b schematically shows the digital recording/reproducing process. "
        "First, all user data are encoded into a binary format — a serial of 1s and 0s. Then a write "
        "current i is sent to the coil. This current changes its direction whenever a 1 is being written. "
        "Correspondingly, a change of magnetization, termed a transition, is recorded in the medium for "
        "each 1 in the encoded data. During the reproducing process, the electric voltage induced in the "
        "head coil reaches a peak whenever there is a transition in the medium. A pulse detector "
        "generates a pulse for each transition. These pulses are decoded to yield the user data."))
    b.append(p(
        "The minimum distance between two transitions in the medium is the flux change length B, and the "
        "distance between two adjacent signal tracks is the track pitch W, which is wider than the signal "
        "track width w. The flux change length can be directly converted into bit length with the proper "
        "code information. The reciprocal of the bit length is called linear density, and the reciprocal "
        "of the track pitch is termed track density. The information storage areal density in the medium "
        "is the product of the linear density and the track density. This areal density roughly "
        "determines how much information a user can store in a unit surface area of storage medium, and "
        "is a figure of merit for a recording technique. Much effort has been expended to increase the "
        "areal density. For example, it has been increased 50 times during the last decade in hard disk "
        "drives, and is expected to continue increasing 60% per year in the foreseeable future. At "
        "present, state-of-the-art hard disk products feature areal densities of more than "
        "7 Mbits/mm<sup>2</sup> (B &lt; 0.1 µm and W &lt; 1.5 µm). This gives a total storage capacity of "
        "up to 6 Gbytes for a disk of 95 mm diameter."))

    b.append(h4("Magnetism and Hysteresis Loop"))
    b.append(p(
        "Magnetism is the result of uncompensated electron spin motions in an atom. Only transition "
        "elements exhibit this property, and nearly all practical interest in magnetism centers on the "
        "first transition group of elements (Mn, Cr, Fe, Ni, and Co) and their alloys. The strength of "
        "magnetism is represented by magnetization M, and is related to magnetic field H and magnetic "
        "flux density B by"))
    b.append(eq(_eq("en", "96.1"), "96.1"))
    b.append(p(
        "where μ<sub>0</sub> is the permeability of vacuum. Since M is a property of a magnetic material, "
        "it does not exist outside the magnetic material. H represents the strength acting on a magnetic "
        "material from a magnetic field which is generated either by a magnetic material or by an "
        "electric current. B is the flux density which determines the induced electric voltage in a coil. "
        "The ratio of B with and without a magnetic material is the relative permeability μ of that "
        "magnetic material."))
    b.append(p(
        "When a magnetic field H is applied to a piece of demagnetized magnetic material, the "
        "magnetization M starts increasing with H from zero. The rate of increase gradually slows down "
        "and M asymptotically approaches a value M<sub>s</sub> at high H. If H is reduced to zero, then M "
        "is reduced to a lower value M<sub>r</sub>. Continuous reduction of H to a very high negative "
        "value will magnetize the material to –M<sub>s</sub>. In order to bring the material to a "
        "demagnetized state, a positive field H<sub>c</sub> is required. Further increase in the H field "
        "will bring the trace of M to a closed loop. This loop is the major hysteresis loop, as shown in "
        "Fig. 96.14. The hysteresis loop shows that a magnetic material has memory. It is this memory "
        "that is used in the medium for storing information. H<sub>c</sub> is the coercivity, indicating "
        "the strength of magnetic field required to erase the memory of a magnetic material. Magnetic "
        "materials with high H<sub>c</sub> are “hard” magnets, and are suitable for medium applications if "
        "they have high M<sub>r</sub>. On the other hand, magnetic materials with low H<sub>c</sub> are "
        "“soft” magnets, and are candidates for head core materials if they have high M<sub>s</sub> and "
        "high μ. M<sub>r</sub> and M<sub>s</sub> are the remanent and saturation magnetization, "
        "respectively, and their ratio is the remanent squareness. The flux density corresponding to "
        "M<sub>s</sub> is B<sub>s</sub>."))
    b.append(fig(14, F.fig(14), "en"))

    b.append(h4("Magnetic Media"))
    b.append(p(
        "Magnetic media are used to store information in a magnetic recording system. In order to "
        "increase the areal density, we need to reduce flux change length B and track width w. Since B is "
        "limited by the term M<sub>r</sub>δ/H<sub>c</sub>, where δ is the magnetic layer thickness, we can "
        "reduce B by either decreasing M<sub>r</sub>δ or increasing H<sub>c</sub>. However, the amplitude "
        "of the magnetic signal available for the reproducing head is proportional to the term "
        "M<sub>r</sub>δw. If we reduce track width w to increase areal density, we must increase "
        "M<sub>r</sub>δ to avoid signal deterioration. In addition, if the magnetic layer is so thin that "
        "it causes thickness nonuniformity, more noise will appear in the reproducing process. Therefore, "
        "the major requirements for the magnetic layer are high H<sub>c</sub>, high M<sub>r</sub>, and "
        "ease of making a uniform thin layer. Additional requirements include good magnetic and "
        "mechanical stability."))
    b.append(p(
        "There are two groups of magnetic media. The first group is called particulate media because the "
        "magnetic materials are in the form of particles. This group includes iron oxide "
        "(γ-Fe<sub>2</sub>O<sub>3</sub>), cobalt-modified iron oxide (γ-Fe<sub>2</sub>O<sub>3</sub>+Co), "
        "chromium dioxide (CrO<sub>2</sub>), metal particles, and barium ferrite "
        "(BaFe<sub>12</sub>O<sub>19</sub>). Some of these have been used in magnetic recording for "
        "several decades. More recently, another group of media has been developed largely due to the "
        "ever-increasing demand for higher storage capacity in the computer industry. This group of media "
        "is the thin-film media, where the magnetic layer can be made as a continuous thin film. Most "
        "materials in this group are cobalt-based metal alloys. Compared with particulate media, the "
        "thin-film media usually have a higher coercivity H<sub>c</sub>, a higher remanence "
        "M<sub>r</sub>, and can be deposited in a very thin continuous film. Table 96.8 lists "
        "H<sub>c</sub> and M<sub>r</sub> for some of the most popularly used particulate and thin-film "
        "media. Note that magnetic properties are affected by the fabrication process and film structure. "
        "Therefore, their values can be out of the ranges of Table 96.8 if different processes are used."))
    b.append(table(*_t8("en")))
    b.append(p(
        "Magnetic media can be classified into three general forms of applications. Tape is the oldest "
        "form and remains an important medium today. It is central to most audio, video, and "
        "instrumentation recording, although it is also used in the computer industry for archival "
        "storage. Tape is economical and can hold a large capacity, but suffers slow access time. Hard "
        "disk is primarily used as the storage inside a computer, providing fast data access for the "
        "user, but having poor transportability. Flexible disk is designed for easy data transportation, "
        "but is limited in capacity. Besides these three general forms of applications, a hybrid of "
        "flexible and hard disk is being gradually accepted. It is a removable rigid disk capable of "
        "holding up to several gigabytes of digital data. In addition, magnetic stripes are getting wide "
        "use in different forms of cards."))
    b.append(p(
        "The magnetic layer alone cannot be used as a medium. It needs additional components to improve "
        "its chemical and mechanical durability. Typical cross sections of a particulate magnetic tape "
        "and a thin-film hard disk are shown in Fig. 96.15. In the case of tape application, iron "
        "particles with typical size of 0.5 µm long and 0.1 µm wide are dispersed in a polymeric binder, "
        "together with solvents, lubricants, and other fillers to improve magnetic and mechanical "
        "stability. This dispersed material is then coated on an abiaxially oriented polyethylene "
        "terephthalate substrate. An optional back coat may also be applied to the other side of the "
        "substrate. The cross section of a hard disk is more complex. A high-purity aluminum–magnesium "
        "(5 wt%) substrate is diamond turned to a fine surface finish, and then electrolessly plated with "
        "a nonmagnetic nickel–phosphorus (10 at%) undercoat. This layer is used to increase the hardness, "
        "reduce the defects, and improve the finish of the Al–Mg alloy, and is polished to a super surface "
        "finish. Next, an underlayer of chromium is sputtered to control the properties of the magnetic "
        "film, followed by sputtering the magnetic film. Finally, a layer of hydrogenated or nitrogenated "
        "carbon is overcoated on the magnetic film, and an ultrathin layer of perfluorinated hydrocarbon "
        "liquid lubricant is applied on top. The carbon and lubricant layers are used to improve the "
        "corrosion and mechanical resistance of the disk. For a 95-mm disk the finished product should "
        "have a surface flatness better than 10 µm and a tightly controlled surface roughness. In some "
        "applications, an arithmetic average roughness (R<sub>a</sub>) of less than 0.5 nm is required."))
    b.append(fig(15, F.fig(15), "en"))

    b.append(h4("Magnetic Heads"))
    b.append(p(
        "Magnetic heads have three functions: recording, reproducing, and erasing. Usually for stationary "
        "head applications such as tape drives, multiple heads are used to perform these functions. For "
        "moving head applications such as disk drives, a single head is employed because of the "
        "requirements of simple connections and small head mass for fast data access. Most of these heads "
        "are the inductive type, where the fundamental design is an inductive coil and a magnetic core. "
        "The general requirements for the core materials are high relative permeability μ, high "
        "saturation flux density B<sub>s</sub>, low coercivity H<sub>c</sub>, high electric resistivity "
        "ρ, and low magnetostriction coefficient λ. Some of the properties for the commonly used core "
        "materials are listed in Table 96.9."))
    b.append(table(*_t9("en")))
    b.append(p(
        "The evolution of the magnetic head follows the selection of core materials, as shown in Fig. "
        "96.16. Early heads used laminated molybdenum Permalloy (Ni-Fe-Mo, 79-17-4 wt%). These heads are "
        "inexpensive to make, and have low H<sub>c</sub> and high μ and B<sub>s</sub>. The primary "
        "drawbacks are frequency limitation, gap dimension inaccuracy, and mechanical softness. Frequency "
        "limitation is caused by the difficulty of making the lamination layer thinner than 25 µm. Eddy "
        "current loss, which is proportional to layer thickness and square root of frequency, reduces the "
        "effective permeability. As a result, laminated heads are seldom used for applications exceeding "
        "10 MHz. Gap dimension inaccuracy is associated with the head fabrication process, and makes it "
        "unsuitable for high areal density applications. Lack of mechanical hardness reduces its usable "
        "life."))
    b.append(fig(16, F.fig(16), "en"))
    b.append(p(
        "One way to reduce eddy current loss is to increase core material electric resistivity. Two types "
        "of ferrite material have high resistivity (four to nine orders higher than Permalloy) and "
        "reasonable magnetic properties: Ni–Zn and Mn–Zn. These materials are also very hard, elongating "
        "head life during head/medium contacts. The major deficiency of ferrite materials is their low "
        "B<sub>s</sub> values. In order to record in high H<sub>c</sub> media, high flux density B is "
        "needed in the head core. When the flux density in the core material reaches its saturation "
        "B<sub>s</sub>, it will not increase despite the increase of recording current or coil turns. "
        "This saturation starts from the corners of the gap due to its geometry. To remedy this "
        "deficiency, a layer of metallic alloy material with much higher B<sub>s</sub> is deposited on "
        "the gap faces. This type of head is called the metal-in-gap (MIG) head. Sendust (Fe–Si–Al, "
        "85-9.6-5.4 wt%) is one of the materials used for the deposition. MIG heads are capable of "
        "recording up to 100 MHz frequency and 180 kA/m medium coercivity."))
    b.append(p(
        "Thin-film heads capitalize on semiconductor-like processing technology to reduce the customized "
        "fabrication steps for individual heads. The core, coil, gap, and insulator layers are all "
        "fabricated by electroplating, sputtering, or evaporation. Due to the nature of the semiconductor "
        "process, the fabrication is accurate for small dimensions. Small gap dimensions are suitable for "
        "high linear and track density, and small core dimensions allow the use of high B<sub>s</sub> "
        "Permalloy material (Ni–Fe, 80-20 wt%) as core with low inductance for high data rate "
        "applications. Thin-film heads are used for high medium H<sub>c</sub>, high areal density "
        "applications. The high cost of the semiconductor-like process is offset by high throughput: a "
        "150 × 150 mm wafer can produce 16,000 nanoslider heads. One disadvantage is the limited-band "
        "recording capability because the small pole length limits low-frequency response and introduces "
        "undershoots. A second disadvantage is the Barkhausen noise, which is caused by the relatively "
        "small number of magnetic domains in the core. At present, thin-film heads are used up to "
        "frequencies of 80 MHz and medium coercivity of 200 kA/m. MIG thin-film heads are also being used "
        "for high-coercivity applications."))
    b.append(p(
        "An inductive head is often used for both recording and reproducing. The optimal performance "
        "cannot be achieved because recording and reproducing have contradictory requirements for head "
        "design. To solve this problem, the MR head has been developed. The MR head is for reproducing "
        "only, and an inductive head is used for recording. As schematically shown in Fig. 96.16, an MR "
        "head has a magnetoresistive element (MRE) and two electric leads. The MRE is a Permalloy stripe "
        "(Ni–Fe, 80-20 wt%), with thickness t, width w, and height h. An electric current, with density J, "
        "passes through the MRE through the leads. The electric resistivity of the MRE is a function of "
        "the angle θ between J and MRE magnetization M:"))
    b.append(eq(_eq("en", "96.2"), "96.2"))
    b.append(p(
        "where ρ<sub>θ</sub> is the resistivity at θ, ρ is the resistivity at θ = 90°, and Δρ is the "
        "resistivity difference between θ = 0° and θ = 90°. Δρ/ρ is the anisotropic MR ratio (AMR) of the "
        "MRE. Usually a transverse magnetic field is applied to the MRE so that θ = θ<sub>0</sub> when "
        "the head is not reading a magnetic signal. Assume that a magnetic signal from the medium rotates "
        "M from θ<sub>0</sub> to θ, then an electric voltage change v will be detected across the MRE as "
        "the output signal:"))
    b.append(eq(_eq("en", "96.3"), "96.3"))
    b.append(p(
        "where θ<sub>0</sub> is the bias angle and is set to 45° for good linearity. In practice, a "
        "longitudinal bias is also used along the MRE width direction to stabilize the magnetic domain "
        "and reduce large Barkhausen noise. To compare the output between an MR head and an inductive "
        "head, we write the inductive head output using Faraday’s equation:"))
    b.append(eq(_eq("en", "96.4"), "96.4"))
    b.append(p(
        "where n is the number of the coil turns, V is the medium velocity, φ is the magnetic flux, and x "
        "is the coordinate axis fixed on the medium surface. Equations 96.3 and 96.4 tell us that while "
        "inductive head output is proportional to medium velocity and not suitable for low-velocity "
        "applications, the MR head can be used for either high- or low-velocity applications."))

    b.append(h4("Recording Process"))
    b.append(p(
        "We can imagine the recording process in two steps. First, the magnetic flux flowing in the head "
        "core generates a fringe magnetic field around the gap. Then the magnetic field magnetizes the "
        "magnetic medium and leaves a magnetization transition in it. Partly due to the nonlinear nature "
        "of the hysteresis loop, the recording process is so complex that there has been no rigorous "
        "explanation. However, we can still obtain significant insights into the recording process by "
        "using simple models if we keep in mind the limitations."))
    b.append(p(
        "If we set the origin of a coordinate system at the center of the gap with x axis on the head "
        "surface and y axis pointing away from the head, then the longitudinal magnetic field "
        "H<sub>x</sub> and perpendicular magnetic field H<sub>y</sub> of this head can be expressed by the "
        "Karlqvist approximation [2]:"))
    b.append(eq(_eq("en", "96.5"), "96.5"))
    b.append(eq(_eq("en", "96.6"), "96.6"))
    b.append(p(
        "where n is the number of coil turns, i is the current in the coil, g is the gap length, l is the "
        "core length, A<sub>g</sub> is the core cross-sectional area, μ is the relative permeability of "
        "core material, and A<sub>c</sub> is the gap cross-sectional area. Both Eqs. 96.5 and 96.6 give "
        "accurate results for points 0.25g away from gap corners. Since longitudinal recording mode "
        "dominates the magnetic recording industry, we will focus on the field H<sub>x</sub>. Equation "
        "96.5 shows that the contours of constant H<sub>x</sub> field are circles nesting on the two gap "
        "corners, as shown in Fig. 96.17. The greater the diameter of the circle, the weaker the magnetic "
        "field. Assume a magnetic medium, moving from left to right with a distance d above the head, has "
        "a thickness δ and a magnetization M pointing to right. At some instant the recording current "
        "turns on and generates the magnetic field H<sub>x</sub> above the gap as depicted in Fig. 96.17. "
        "On the circumference of H<sub>x</sub> = H<sub>c</sub>, half of medium material has its "
        "magnetization reversed and half remains the same, resulting in a zero total magnetization. Since "
        "H<sub>x</sub> has a gradient, the medium closer to the gap (inside a smaller circle) gets its "
        "magnetization reversed more completely than the medium farther away from the gap (outside a "
        "bigger circle). Therefore, magnetic transition is gradual in the medium even if the change of "
        "recording current follows a step function. Assume the original magnetization is M<sub>r</sub> "
        "and the completely reversed magnetization is –M<sub>r</sub>, this gradual change of "
        "magnetization for an isolated transition can be modeled by [3]:"))
    b.append(eq(_eq("en", "96.7"), "96.7"))
    b.append(p(
        "where x is the distance from the center of transition and a is a parameter characterizing the "
        "sharpness of the transition as shown in Fig. 96.18. Assuming a thin-film medium and using the "
        "Karlqvist approximation for the head field, a is found to be [4–6]:"))
    b.append(fig(17, F.fig(17), "en"))
    b.append(fig(18, F.fig(18), "en"))
    b.append(eq(_eq("en", "96.8"), "96.8"))
    b.append(p(
        "where S* is the medium loop squareness and Q is the head-field gradient factor. For a reasonably "
        "well designed head, Q ≈ 0.8. It is obvious that we want to make parameter a as small as "
        "possible so that we can record more transitions for a unit medium length. If the head gap length "
        "g and medium thickness δ are small compared with head/medium separation d, and the medium has a "
        "squareness of one, then the minimum possible value of a is [7]"))
    b.append(eq(_eq("en", "96.9"), "96.9"))
    b.append(p(
        "In order to decrease the value of a and therefore increase areal density, we need to reduce "
        "medium remanence M<sub>r</sub>, thickness δ, head/medium separation d, and to increase "
        "coercivity H<sub>c</sub>."))

    b.append(h4("Reproducing Process"))
    b.append(p(
        "In contrast to the recording process, the reproducing process is well understood. The flux "
        "density induced in the head core is on the order of a few millitesla, yielding a linear process "
        "for easier mathematical treatment. The head fringe field is the Karlqvist approximation (Eq. "
        "96.5) and the foundation is the reciprocity theorem. For an isolated transition (Fig. 96.18) "
        "with a thin magnetic layer δ ≪ d, the induced electric voltage v for an inductive head is [7]:"))
    b.append(eq(_eq("en", "96.10"), "96.10"))
    b.append(p(
        "where μ<sub>0</sub> is the permeability of vacuum, μ is the relative permeability of the core, V "
        "is the medium velocity, w is the track width, n is the number of coil turns, g is the head gap "
        "length, d is the head/medium separation, and x is the distance between the center of the medium "
        "transition and the center of the head gap. The term lA<sub>g</sub>/μA<sub>c</sub> is closely "
        "related to g for head efficiency. When a transition passes under the head, its voltage starts "
        "with a very low value, reaches a peak, then falls off again, as shown in Fig. 96.19, where the "
        "following typical values for a hard disk drive are used: V = 20 m/s, w = 3.5 µm, "
        "M<sub>r</sub> = 450 kA/m, δ = 50 nm, n = 50, lA<sub>g</sub>/μA<sub>c</sub> = 0.1g. The effects of "
        "g and a + d are shown in Fig. 96.19. Since a greater peak voltage and a narrower spatial "
        "response are desired for the reproducing process, smaller g and a + d values are helpful."))
    b.append(fig(19, F.fig(19), "en"))
    b.append(p(
        "When an MR head is used for reproducing, the MRE is usually sandwiched between two magnetic "
        "shields to increase its spatial resolution to medium signals, as shown in Fig. 96.20. Since the "
        "MR head is flux sensitive, the incident flux φ<sub>i</sub> on the bottom surface of the MRE "
        "should be derived as a function of the distance (x) between the center of MRE and the center of "
        "the transition [7, 8]:"))
    b.append(fig(20, F.fig(20), "en"))
    b.append(eq(_eq("en", "96.11"), "96.11"))
    b.append(p("where g is the distance between the MRE and the shield, t is the MRE thickness, and"))
    b.append(eq(_eq("en", "96.12"), "96.12"))
    b.append(p(
        "The angle between magnetization and current varies along the MRE height h. To find out the "
        "variation, we need to calculate the signal flux decay as a function of y by"))
    b.append(eq(_eq("en", "96.13"), "96.13"))
    b.append(p("where"))
    b.append(eq(_eq("en", "96.14"), "96.14"))
    b.append(p("Then the bias angle θ<sub>0</sub> and signal angle θ can be calculated by"))
    b.append(eq(_eq("en", "96.15"), "96.15"))
    b.append(p("and"))
    b.append(eq(_eq("en", "96.16"), "96.16"))
    b.append(p(
        "where φ<sub>b</sub> is the biasing flux in the MRE and M<sub>s</sub> is the saturation "
        "magnetization of the MRE. Application of Eqs. 96.15 and 96.16 to Eq. 96.3 and integration over "
        "height h lead to"))
    b.append(eq(_eq("en", "96.17"), "96.17"))
    b.append(p(
        "For an MR head with a 45° bias at the center and small height h ≪ l<sub>c</sub>, the peak "
        "voltage is [6]"))
    b.append(eq(_eq("en", "96.18"), "96.18"))
    b.append(p(
        "The general shape of the reproducing voltage from an MR head is similar to that in Fig. 96.19."))
    b.append(p(
        "The study of an isolated transition reveals many intrinsic features of the reproducing process. "
        "However, transitions are usually recorded closely in a magnetic medium to achieve high linear "
        "density. In this case, the magnetization variation in the medium approaches a sinusoidal wave. "
        "That is,"))
    b.append(eq(_eq("en", "96.19"), "96.19"))
    b.append(p("where λ is the wavelength. The reproducing voltage in an inductive head becomes [9, 10]"))
    b.append(eq(_eq("en", "96.20"), "96.20"))
    b.append(p(
        "This equation presents all the important features of the high-linear-density reproducing "
        "process. The term exp(–2πd/λ) is the spacing loss. It shows that the reproducing voltage falls "
        "exponentially with the ratio of head/medium spacing to wavelength. The second term "
        "1 – exp(–2πδ/λ) is the thickness loss. The name of this term is misleading because its value "
        "increases with a greater medium thickness. However, the rate of increase diminishes for thicker "
        "medium. In fact, 80% of the maximum possible value is achieved by a medium thickness of 0.25λ. "
        "The last term sin(πg/λ)/(πg/λ) is the gap loss. This term is based on the Karlqvist "
        "approximation. If a more accurate head fringe field is used, this term is modified to "
        "sin(πg/λ)/(πg/λ)·(1.25g<sup>2</sup> – λ<sup>2</sup>)/(g<sup>2</sup> – λ<sup>2</sup>) [11]. It "
        "shows a gap null at λ = 1.12g, and limits the shortest wavelength producible. These three terms "
        "are plotted in Fig. 96.21. The most significant loss comes from the spacing loss term, which is "
        "54.6 dB for d = λ. Therefore, one of the biggest efforts spent on magnetic recording is to "
        "reduce the head/medium spacing as much as possible without causing mechanical reliability "
        "issues. For an MR head, the reproducing voltage is [11]"))
    b.append(fig(21, F.fig(21), "en"))
    b.append(eq(_eq("en", "96.21"), "96.21"))

    b.append(h4("Digital vs. Analog Recording"))
    b.append(p(
        "Due to the nonlinearity of the hysteresis loop, magnetic recording is intrinsically suitable for "
        "digital recording, where only two states (1 and 0) are to be recognized. Many physical "
        "quantities, however, are received in analog form before they can be recorded, such as in "
        "consumer audio and instrumentation recording. In order to perform such recording, we need to "
        "either digitize the information or use the analog recording technique. In the case of "
        "digitization, we use an analog-to-digital converter to change a continuous signal into binary "
        "numbers. The process can be explained by using the example shown in Fig. 96.22. An electric "
        "signal V, normalized to the range between 0 and 1, is to be digitized into three bits. The "
        "signal is sampled at time t = 1, 2, …, 6. At each sampling point, the first bit is assigned a 1 "
        "if the value of the continuous signal is in the top half (&gt;0.5), otherwise assigned a 0. The "
        "second bit is assigned a 1 if the value of the continuous signal is in the top half of each half "
        "(0.25 ≤ V &lt; 0.5, or &gt;0.75), otherwise assigned a 0. The third bit is assigned similarly. "
        "The first bit is the most significant bit (MSB), and the last bit is the least significant bit "
        "(LSB). The converted binary numbers are listed below each sampling point in Fig. 96.22. This "
        "process of digitization is termed quantization. In general, the final quantization interval is"))
    b.append(fig(22, F.fig(22), "en"))
    b.append(eq(_eq("en", "96.22"), "96.22"))
    b.append(p(
        "where V is the total voltage range and N is the number of bits. Because we use a finite number "
        "of bits, statistically there is a difference between the continuous signal and the quantized "
        "signal at the sampling points. This is the quantization error. It leads to a "
        "signal-to-quantization-noise ratio (SNR) [12]:"))
    b.append(eq(_eq("en", "96.23"), "96.23"))
    b.append(p(
        "where P<sub>s</sub> is the mean square average signal power. For a signal with uniform "
        "distribution over its full range, this yields"))
    b.append(eq(_eq("en", "96.24"), "96.24"))
    b.append(p("For a sinusoidal signal, it changes to"))
    b.append(eq(_eq("en", "96.25"), "96.25"))
    b.append(p(
        "The SNR can be improved by using more bits. This improvement, however, is limited by the SNR of "
        "the incoming continuous signal. The quantized signal is then pulse code modulated (PCM) for "
        "recording."))
    b.append(p(
        "For analog recording, a linear relationship between the medium magnetization and the recording "
        "signal is required. This is achieved through the anhysteretic magnetization process. If we apply "
        "an alternating magnetic field and a unidirectional magnetic field to a previously demagnetized "
        "medium, and then reduce the amplitude of the alternating field to zero before we remove the "
        "unidirectional field, the remanent magnetization shows a pseudolinear relationship with the "
        "unidirectional field strength H<sub>u</sub> up to some level. Figure 96.23 shows such an "
        "anhysteretic curve. The linearity deteriorates as H<sub>u</sub> gets greater. In applications, "
        "the recording signal current is biased with an ac current of greater amplitude and higher "
        "frequency. Therefore, it is also termed ac-biased recording. Analog recording is easy to "
        "implement, at the price of a lowered SNR because remanent magnetization is limited to about 30% "
        "of the maximum possible M<sub>r</sub> to achieve good linearity."))
    b.append(fig(23, F.fig(23), "en"))

    b.append(h4("Recording Codes"))
    b.append(p(
        "PCM is a scheme of modifying input binary data to make them more suitable for a recording and "
        "reproducing channel. These schemes are intended to achieve some of the following goals: (1) "
        "reducing the dc component, (2) increasing linear density, (3) providing self-clocking, (4) "
        "limiting error propagation, and (5) achieving error-free detection. There are numerous code "
        "schemes, only three of the ones developed early are shown in Fig. 96.24. The earliest and most "
        "straightforward one is the return-to-zero (RZ) code. In this scheme a positive and negative "
        "pulse is used to represent each 1 and 0, respectively, of the data. The main drawback is that "
        "direct recording over old data is not possible due to the existence of zero recording current "
        "between two data. It also generates two transitions for each bit, therefore reducing the linear "
        "density. In addition, it only uses half of the available recording current range for a "
        "transition. The non-return-to-zero-invert (NRZI) method was developed to alleviate some of these "
        "problems. It changes the recording current from one direction to the other for each 1 of the "
        "data, while making no changes for all 0s. However, it has a strong dc component and may lose "
        "reproducing synchronization if there is a long string of 0s in the input data. In addition, "
        "reproducing circuits are usually not designed for dc signal processing. In frequency modulation "
        "(FM) code there is always a transition at the bit–cell boundary which acts as a clock. There is "
        "also an additional transition at the bit–cell center for each 1 and no transition for 0s. It "
        "reduces the dc component significantly. The primary deficiency is the reduction of linear "
        "density since there are two transitions for each 1 in the data."))
    b.append(fig(24, F.fig(24), "en"))
    b.append(p(
        "The most popularly used codes for magnetic recording are the run-length-limited (RLL) codes. "
        "They have the general form of m/n(d, k). In these schemes, data are encoded in groups. Each input "
        "group has m bits. After encoding, each group contains n bits. In some schemes multiple groups "
        "are coded together. d and k are the minimum and maximum 0s, respectively, between two "
        "consecutive 1s in the encoded sequence. While d is used to limit the highest transition density "
        "and intersymbol interference, k is employed to ensure adequate transition frequency for "
        "reproducing clock synchronization. The encoding is carried out by using a lookup table, such as "
        "Table 96.10 for a 1/2(2,7) code [13]."))
    b.append(table(*_t10("en")))

    b.append(h4("Head/Medium Interface Tribology"))
    b.append(p(
        "As expressed in Eq. 96.20, the most effective way to increase signal amplitude, therefore areal "
        "density, is to reduce head/medium spacing d. However, wear occurs when a moving surface is in "
        "close proximity to another surface. The amount of wear is described by Archard’s equation:"))
    b.append(eq(_eq("en", "96.26"), "96.26"))
    b.append(p(
        "where V is the volume worn away, W is the normal load, s is the sliding distance, H is the "
        "hardness of the surface being worn away, and k is a wear coefficient. In order to increase "
        "medium hardness H, hard Al<sub>2</sub>O<sub>3</sub> particles are dispersed in particulate media "
        "and a thin layer of hard carbon (≈ 10 nm) with either hydrogenation or nitrogenation is coated "
        "on thin-film media of hard disks. A layer of liquid lubricant, typically perfluoropolyethers "
        "with various end groups and additives, is applied on top of the carbon film to reduce the wear "
        "coefficient k. Load is minimized to reduce wear while keeping adequate head/medium dynamic "
        "stability. For applications where the sliding distance s is modest over the lifetime of the "
        "products such as floppy disk drives and consumer tape drives, the head physically contacts the "
        "medium during operations. In the case of hard disk application, heads are separated nominally "
        "from the media by a layer of air cushion. The head is carried on a slider, and the slider uses "
        "air-bearing surfaces (ABS) to create the air film based on hydrodynamic lubrication theory. "
        "Figure 96.25 shows two commonly used ABS. Tapers are used to help the slider take off and "
        "maintain flying stability. ABS generates higher-than-ambient pressure to lift the slider above "
        "the medium surface during operations. The tripad slider is for pseudo-contact applications while "
        "the subambient-pressure (SAP) slider is for flying (such as MR head) applications. Because the "
        "relative linear velocity between the slider and the medium changes when the head moves to "
        "different radii, a cavity region is used in the SAP slider to generate suction force to reduce "
        "flying height variation. The ABS is designed based on the modified Reynolds equation:"))
    b.append(fig(25, F.fig(25), "en"))
    b.append(eq(_eq("en", "96.27"), "96.27"))
    b.append(p(
        "where X and Y are coordinates in the slider longitudinal and transverse directions normalized by "
        "the slider length and width, respectively, P is the hydrodynamic pressure normalized by the "
        "ambient pressure, H is the distance between the ABS and medium surface normalized by the minimum "
        "flying height, Q is the molecular slip factor, T is time normalized by the characteristic squeeze "
        "period, Λ<sub>x</sub> and Λ<sub>y</sub> are the bearing numbers in the x and y directions, "
        "respectively, and σ is the squeeze number. A full derivation and explanation of the Reynolds "
        "equation can be found in Reference 14. At present, high end hard disk drives feature a flying "
        "height on the order of 20 to 50 nm."))
    b.append(p(
        "When power is turned off, the slider in the popularly used Winchester-type drives rests on the "
        "medium surface. Although the ABS and medium surface look flat and smooth, they really consist of "
        "microscopic peaks and valleys. If we model an ABS/medium contact by a flat surface and a sphere "
        "tip, the liquid lubricant on the medium surface causes a meniscus force F<sub>m</sub> as "
        "depicted in Fig. 96.26 [15]:"))
    b.append(fig(26, F.fig(26), "en"))
    b.append(eq(_eq("en", "96.28"), "96.28"))
    b.append(p(
        "where R is the radius of the sphere, γ is the surface tension of the lubricant, θ is the contact "
        "angle between the lubricant and the surfaces, y is the sphere to flat surface distance, and h is "
        "the lubricant thickness. Detailed analysis [16] shows that the static friction F at a "
        "head/medium interface is a function of several parameters:"))
    b.append(eq(_eq("en", "96.29"), "96.29"))
    b.append(p(
        "where A is the ABS area, η is the peak density, E is the effective modulus of elasticity, φ is "
        "the peak height distribution, σ is the rms peak roughness, and s is the solid-to-solid shear "
        "strength. If friction F is too large, either the drive cannot be started or the head/medium "
        "interface is damaged. While friction can be reduced practically by reducing A, γ, and increasing "
        "θ, the most effective ways are to control η, σ, h, and φ. Too thin a lubricant layer will cause "
        "wear, and too thick will induce high friction. This limits h to the range of 1 to 3 nm. σ is "
        "controlled by surface texture. Historically, texture is created by mechanical techniques using "
        "either free or fixed abrasives. This leaves a surface with a random feature and is unsuitable "
        "for controlling η and φ. Recently, people started to use lasers [17]. This technique generates a "
        "surface texture with well-defined η and φ to improve wear and friction performance. Figure 96.27 "
        "shows AFM images of a mechanical and a laser texture."))
    b.append(fig(27, F.fig(27), "en"))

    b.append(h3("Optical Recording"))
    b.append(p(
        "The major obstacle to achieving higher areal density in magnetic recording is the spacing loss "
        "term. It is a great engineering challenge to keep heads and media in close proximity while "
        "maintaining the head/medium interface reliable and durable. Care must also be taken in handling "
        "magnetic media since even minute contamination or scratches can destroy the recorded "
        "information. In addition, the servo technique of using magnetic patterns limits the track "
        "density to about one order lower than the linear density. Optical recording, on the other hand, "
        "promises to address all these concerns."))
    b.append(p(
        "Optical recording can be categorized into three groups. In the first group, information is "
        "stored in the media during manufacturing. Users can reproduce the information, but cannot change "
        "or record new information. CD-ROM (compact disk–read only memory) belongs to this group. The "
        "second group is WORM (write once read many times). Instead of recording information during "
        "manufacturing, it leaves this step to the user. This is usually achieved by creating physical "
        "holes or blisters in the media during the recording process. Once it is recorded, however, the "
        "medium behaves like the first group: no further recording is possible. The third group is "
        "similar to magnetic recording. Recording can be performed infinitely on the media by changing "
        "phase or magnetization of the media. The most noticeable example in this group is the "
        "magneto-optic (MO) technique [18]. Only CD-ROM and the magneto-optic recording are described in "
        "the following."))

    b.append(h4("CD-ROM"))
    b.append(p(
        "Figure 96.28 shows the CD-ROM reproducing principle. Data are pressed as physical pits and lands "
        "on one surface of a plastic substrate, usually polycarbonate. A layer of aluminum is deposited on "
        "this surface to yield it reflective. Lacquer is then coated to protect the aluminum layer. During "
        "the reproducing process, an optical lens is used to focus a laser beam on the reflective pit and "
        "land surface. The diameter of the lens is D, the distance between the lens and the substrate is "
        "h<sub>3</sub>, and the substrate thickness is h<sub>2</sub>. The diameter of the laser beam is "
        "d<sub>2</sub> when entering the substrate, and becomes d<sub>1</sub> when focused on the "
        "reflective surface. The width of the pits are designed smaller than d<sub>1</sub>. The reflected "
        "light consists of two portions: I<sub>1</sub> from the land and I<sub>2</sub> from the pit. "
        "According to the theory of interference, the intensity of the reflected light is"))
    b.append(eq(_eq("en", "96.30"), "96.30"))
    b.append(p(
        "where λ is the wavelength of the laser and h<sub>1</sub> ≈ λ/4 is the pit height. This leads to"))
    b.append(eq(_eq("en", "96.31"), "96.31"))
    b.append(p(
        "This change of light intensity is detected and decoded to yield the recorded data. The reflected "
        "light is also used for focusing and track following."))
    b.append(fig(28, F.fig(28), "en"))
    b.append(p(
        "The fundamental limit on optical recording density is the focused beam diameter d<sub>1</sub>. "
        "For a Gaussian (TEM<sub>00</sub>) laser, this is the diffraction-limited diameter at which the "
        "light intensity is reduced to 1/e<sup>2</sup> of the peak intensity:"))
    b.append(eq(_eq("en", "96.32"), "96.32"))
    b.append(p(
        "where θ is the aperture angle. The following values are typical for a CD-ROM system: λ (gallium "
        "arsenide laser) = 780 nm, θ = 27°, h<sub>2</sub> = 1.2 mm, D = 5 mm, h<sub>3</sub> = 4.2 mm. "
        "This yields d<sub>1</sub> ≈ 1.0 µm and d<sub>2</sub> ≈ 0.7 mm, and sets the areal density limit "
        "of optical (including magneto-optic) recording to about 1 Mbit/mm<sup>2</sup>. For most CD-ROM "
        "applications, the areal density is smaller than this limit, and a disk with 120 mm diameter holds "
        "about 600 Mbyte information. In order to increase areal density, we can either reduce light "
        "wavelength or increase numerical aperture. Much of the effort has been to adopt a new light "
        "source with short wavelength such as a blue laser. Increasing numerical aperture is more "
        "difficult because increasing lens diameter is cost prohibitive and reducing h<sub>2</sub> or "
        "h<sub>3</sub> is reliability limited. Note that although the beam size on the focus plane is on "
        "the order of 1 µm (d<sub>1</sub>), it is two to three orders greater at the air/substrate "
        "interface (d<sub>2</sub>). This means that optical recording can tolerate disk surface "
        "contamination and scratches much better than magnetic recording. However, the performance of "
        "optical recording does not match magnetic recording in general. The data transfer rate of CD-ROM "
        "drives is expressed as multiple (×) of 150 kB/s. Even for a 12× CD-ROM drive, the data access "
        "time and data transfer rate are still on the order of 100 ms and 1.8 MB/s, respectively, while "
        "for a high-performance rigid disk drive these values are less than 10 ms and greater than "
        "30 MB/s, respectively."))

    b.append(h4("Magnetooptic Recording"))
    b.append(p(
        "The primary drawback of a CD-ROM to an end user is its inability to record. This deficiency is "
        "remedied by MO recording technology, as depicted in Fig. 96.29. A linearly polarized laser beam "
        "is focused on a layer of magnetic material, and a coil provides a dc magnetic field on the other "
        "side of the medium. This dc magnetic field is too weak to affect the medium magnetization at "
        "normal temperature. The recording process utilizes the thermomagnetic property of the medium, and "
        "the reproducing process is achieved by using the Kerr effect. During recording, the medium is "
        "initially magnetized vertically in one direction, and the dc magnetic field is in the opposite "
        "direction. The laser heats up the medium to its Curie temperature, at which the coercivity "
        "becomes zero. During the cooling process, the dc magnetic field aligns the medium magnetization "
        "of the heated region to the magnetic field direction. In the process of reproducing, the same "
        "laser is used with a smaller intensity. The medium is heated up to its compensation temperature, "
        "at which the coercivity becomes extremely high. Depending on the direction of the magnetization, "
        "the polarization of the reflected light is rotated either clockwise or counterclockwise (Kerr "
        "rotation). This rotation of polarization is detected and decoded to get the data. The main "
        "disadvantage of MO recording is that a separate erasing process is needed to magnetize the medium "
        "in one direction before recording. Recently some technologies have been developed to eliminate "
        "this separate erasing process at the cost of complexity."))
    b.append(p(
        "The medium used in MO recording must have a reasonably low Curie temperature (&lt;300 °C). The "
        "materials having this property are rare earth transition metal alloys, such as "
        "Tb<sub>23</sub>Fe<sub>77</sub> and Tb<sub>21</sub>Co<sub>79</sub>. Unfortunately, the properties "
        "of these materials deteriorate in an oxygen and moisture environment. To protect them from air "
        "and humidity, they are sandwiched between an overlayer and an underlayer, such as SiO, AlN, SiN, "
        "and TiO<sub>2</sub>. Another issue with the rare earth transition metal alloys is their small "
        "Kerr rotation, about 0.3°. To increase this Kerr rotation, multiple layers are used. In the "
        "so-called quadrilayer structure (Fig. 96.29b), the overlayer is about a half-wavelength thick and "
        "the underlayer is about a quarter-wavelength thick [18]. The MO layer is very thin (≈3 nm). Light "
        "reflected from the reflector is out-of-phase with the light reflected from the surface of the MO "
        "layer, and is in-phase with the light reflected from the inside of the MO layer. As a result, the "
        "effective Kerr rotation is increased several times."))
    b.append(fig(29, F.fig(29), "en"))
    b.append(p(
        "Compared with magnetic recording, optical recording has the intrinsic advantages of superior "
        "reliability and portability. However, its performance is inferior due to slower data access time "
        "and transfer rate. Another advantage of optical recording, higher areal density, has been "
        "disappearing or even reversing to magnetic recording. Both magnetic and optical recording will be "
        "continuously improved in the near future, probably toward different applications. Currently there "
        "are some emerging techniques that try to combine the magnetic and optical recording techniques. "
        "Table 96.11 is a short list of representative magnetic and optical devices for digital "
        "recording."))
    b.append(table(*_t11("en")))

    b.append(h3("References (96.3)"))
    b.append(refs([
        "C. D. Mee and E. D. Daniel, Eds., <i>Magnetic Storage Handbook</i>, 2nd ed., New York: "
        "McGraw-Hill, 1996.",
        "O. Karlqvist, “Calculation of the magnetic field in the ferromagnetic layer of a magnetic "
        "drum,” <i>Trans. R. Inst. Technol. (Stockholm)</i>, 86, 3–28, 1954.",
        "J. J. Miyata and R. R. Tartel, “The recording and reproduction of signals on magnetic medium "
        "using saturation-type recording,” <i>IRE Trans. Elec. Comp.</i>, EC-8, 159–169, 1959.",
        "M. L. Williams and R. L. Comstock, “An analytical model of the write process in digital "
        "magnetic recording,” <i>A.I.P. Conf. Proc.</i>, 5, 738–742, 1972.",
        "V. A. J. Maller and B. K. Middleton, “A simplified model of the writing process in saturation "
        "magnetic recording,” <i>IERE Conf. Proc.</i>, 26, 137–147, 1973.",
        "H. N. Bertram, <i>Theory of Magnetic Recording</i>, Cambridge, UK: Cambridge University Press, "
        "1994.",
        "C. D. Mee and E. D. Daniel, Eds., <i>Magnetic Recording Technology</i>, 2nd ed., New York: "
        "McGraw-Hill, 1996.",
        "R. Potter, “Digital magnetic recording theory,” <i>IEEE Trans. Magn.</i>, MAG-10, 502–508, 1974.",
        "W. K. Westmijze, “Studies on magnetic recording,” <i>Philips Res. Rep.</i>, 8, 161–183, 1953.",
        "G. J. Fan, “A study of the playback process of a magnetic ring head,” <i>IBM J. Res. Dev.</i>, "
        "5, 321–325, 1961.",
        "J. C. Mallinson, <i>The Foundations of Magnetic Recording</i>, 2nd ed., San Diego, CA: Academic "
        "Press, 1993.",
        "M. S. Roden, <i>Analog and Digital Communication Systems</i>, 4th ed., Upper Saddle River, NJ: "
        "Prentice-Hall, 1996.",
        "P. A. Franaszek, “Run-length-limited variable length coding with error propagation "
        "limitation,” U.S. Patent No. 3,689,899, 1972.",
        "W. A. Gross, L. Matsch, V. Castelli, A. Eshel, T. Vohr, and M. Wilamann, <i>Fluid Film "
        "Lubrication</i>, New York: Wiley, 1980.",
        "J. N. Israelachvili, <i>Intermolecular and Surface Forces</i>, London: Academic Press, 1985, "
        "224.",
        "Y. Li and F. E. Talke, “A model for the effect of humidity on stiction of the head/disk "
        "interface,” <i>Tribology Mech. Magn. Storage Syst.</i>, SP-27, 79–84, 1990.",
        "R. Ranjan, D. N. Lambeth, M. Tromel, P. Goglia, and Y. Li, “Laser texturing for "
        "low-flying-height media,” <i>J. Appl. Phys.</i>, 68, 5745–5747, 1991.",
        "J. Watkinson, <i>The Art of Data Recording</i>, Oxford, UK: Focal Press, 1994.",
        "G. A. N. Connell and R. Allen, “Magnetization reversal in amorphous rare-earth transition-metal "
        "alloys: TbFe,” <i>Proc. 4th Int. Conf. on Rapidly Quenched Metals</i>, Sendai, Japan, 1981.",
    ]))

    b.append(h2("Translator's note"))
    b.append(note(
        "The source prints “Reading/Recording Devices” and splits the chapter into three sections by "
        "three different authors; each section keeps its own frame of reference, symbols and numbering of "
        "figures, tables and equations, and so does this translation. Section 96.1 has no figures at all "
        "and numbers its tables from 96.1; Section 96.2 numbers its figures from 96.1 and its tables from "
        "96.6; Section 96.3 numbers its figures from 96.13, its tables from 96.8 and its equations from "
        "96.1 — exactly as printed, with nothing renumbered. Two defects in the printed original are "
        "reproduced and recorded here: (a) the caption of Figure 96.12 reads 45 µs while the drawing "
        "itself reads 50 µs; (b) the passage on continuous scanning asserts that two sine waves 90° out "
        "of phase always sum to zero, which holds only for 180°. In addition, the printed passage on "
        "simultaneous sampling uses “ms” for the 5 µs and 5 ns intervals; the translation gives µs and ns, "
        "which agree with Figure 96.11 and with the arithmetic of 1/200 kS/s. Lengths are given in µm "
        "where the original uses them in connection with areal density (B &lt; 0.1 µm, w = 3.5 µm) and "
        "in nm for magnetic layer thicknesses."))

    return "".join(b)


# ================================================================ build

def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 96 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 96 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 96 “Thiết bị đọc và ghi” của Herman Vermariën, Edward McConnell "
            "và Yufeng Li — máy ghi đồ thị, máy ghi dãy điểm nhiệt, hệ thu thập dữ liệu, và ghi từ cùng "
            "ghi quang, với 29 hình, 11 bảng và 32 phương trình." if vi
            else
            "Companion to Chapter 96 of the CRC Measurement Handbook — graphic recorders, thermal dot "
            "array recorders, data acquisition systems, and magnetic and optical recording, with 29 "
            "figures, 11 tables and 32 equations.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 96' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 96' % BASE_EN)
    meta = ("Chương 96 · theo Ch96.pdf (CRC Press, 1999) · 29 hình, 11 bảng, 32 phương trình" if vi else
            "Chapter 96 · 29 figures, 11 tables, 32 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 96)))
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang)


def main():
    pairs = [("en", os.path.join(ROOT, "books", "read", SLUG, CSLUG, "index.html")),
             ("vi", os.path.join(ROOT, "vi", "books", "read", SLUG, CSLUG, "index.html"))]
    for lang, path in pairs:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        page = build(lang)
        open(path, "w", encoding="utf-8").write(page)
        print("wrote %s  %d kB" % (path, len(page) // 1024))


if __name__ == "__main__":
    main()
