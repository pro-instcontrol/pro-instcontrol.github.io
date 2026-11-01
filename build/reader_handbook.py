# -*- coding: utf-8 -*-
"""Reader pages for the CRC *Measurement, Instrumentation and Sensors Handbook*.

Generates two book landing pages that mirror the taichikb.github.io/books
reader structure:

    books/read/<slug>/index.html      English
    vi/books/read/<slug>/index.html   Vietnamese

The 101-chapter map comes from the front matter of the source PDF (fm.pdf),
which is the book's own table of contents — not from filenames.
"""
import datetime
import html
import os

from books_site import MARK, NAV_EN, NAV_VI, esc

SLUG = "the-measurement-instrumentation-and-sensors-handbook"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- the book's own table of contents ------------------------------------
SECTIONS = [
    ("I",    "Measurement Characteristics",
             "Đặc tính đo lường", 1, 5),
    ("II",   "Spatial Variables Measurement",
             "Đo các đại lượng không gian", 6, 17),
    ("III",  "Time and Frequency Measurement",
             "Đo thời gian và tần số", 18, 19),
    ("IV",   "Mechanical Variables Measurement — Solid",
             "Đo đại lượng cơ học — vật rắn", 20, 25),
    ("V",    "Mechanical Variables Measurement — Fluid",
             "Đo đại lượng cơ học — chất lưu", 26, 31),
    ("VI",   "Mechanical Variables Measurement — Thermal",
             "Đo đại lượng cơ học — nhiệt", 32, 36),
    ("VII",  "Electromagnetic Variables Measurement",
             "Đo đại lượng điện từ", 37, 55),
    ("VIII", "Optical Variables Measurement",
             "Đo đại lượng quang học", 56, 64),
    ("IX",   "Radiation Measurement",
             "Đo bức xạ", 65, 69),
    ("X",    "Chemical Variables Measurement",
             "Đo đại lượng hoá học", 70, 73),
    ("XI",   "Biomedical Variables Measurement",
             "Đo đại lượng y sinh", 74, 79),
    ("XII",  "Signal Processing",
             "Xử lý tín hiệu", 80, 89),
    ("XIII", "Displays",
             "Hiển thị", 90, 96),
    ("XIV",  "Control",
             "Điều khiển", 97, 101),
]

CH = {
    1: ("Characteristics of Instrumentation", "Đặc tính của thiết bị đo"),
    2: ("Operational Modes of Instrumentation", "Các chế độ vận hành của thiết bị đo"),
    3: ("Static and Dynamic Characteristics of Instrumentation", "Đặc tính tĩnh và động của thiết bị đo"),
    4: ("Measurement Accuracy", "Độ chính xác của phép đo"),
    5: ("Measurement Standards", "Chuẩn đo lường"),
    6: ("Displacement Measurement, Linear and Angular", "Đo dịch chuyển thẳng và góc"),
    7: ("Thickness Measurement", "Đo chiều dày"),
    8: ("Proximity Sensing for Robotics", "Cảm biến tiệm cận cho robot"),
    9: ("Distance", "Khoảng cách"),
    10: ("Position, Location, Altitude Measurement", "Đo vị trí, định vị và độ cao"),
    11: ("Level Measurement", "Đo mức"),
    12: ("Area Measurement", "Đo diện tích"),
    13: ("Volume Measurement", "Đo thể tích"),
    14: ("Angle Measurement", "Đo góc"),
    15: ("Tilt Measurement", "Đo độ nghiêng"),
    16: ("Velocity Measurement", "Đo vận tốc"),
    17: ("Acceleration, Vibration, and Shock Measurement", "Đo gia tốc, rung và xung kích"),
    18: ("Time Measurement", "Đo thời gian"),
    19: ("Frequency Measurement", "Đo tần số"),
    20: ("Mass and Weight Measurement", "Đo khối lượng và trọng lượng"),
    21: ("Density Measurement", "Đo khối lượng riêng"),
    22: ("Strain Measurement", "Đo biến dạng"),
    23: ("Force Measurement", "Đo lực"),
    24: ("Torque and Power Measurement", "Đo mômen xoắn và công suất"),
    25: ("Tactile Sensing", "Cảm biến xúc giác"),
    26: ("Pressure and Sound Measurement", "Đo áp suất và âm thanh"),
    27: ("Acoustic Measurement", "Đo âm học"),
    28: ("Flow Measurement", "Đo lưu lượng"),
    29: ("Point Velocity Measurement", "Đo vận tốc tại một điểm"),
    30: ("Viscosity Measurement", "Đo độ nhớt"),
    31: ("Surface Tension Measurement", "Đo sức căng bề mặt"),
    32: ("Temperature Measurement", "Đo nhiệt độ"),
    33: ("Thermal Conductivity Measurement", "Đo độ dẫn nhiệt"),
    34: ("Heat Flux", "Thông lượng nhiệt"),
    35: ("Thermal Imaging", "Ảnh nhiệt"),
    36: ("Calorimetry Measurement", "Đo nhiệt lượng"),
    37: ("Voltage", "Điện áp"),
    38: ("Current Measurement", "Đo dòng điện"),
    39: ("Power Measurement", "Đo công suất điện"),
    40: ("Power Factor Measurement", "Đo hệ số công suất"),
    41: ("Phase Measurement", "Đo pha"),
    42: ("Energy Measurement", "Đo điện năng"),
    43: ("Electrical Conductivity and Resistivity", "Độ dẫn điện và điện trở suất"),
    44: ("Charge Measurement", "Đo điện tích"),
    45: ("Capacitance and Capacitance Measurements", "Điện dung và phép đo điện dung"),
    46: ("Permittivity Measurement", "Đo hằng số điện môi"),
    47: ("Electric Field Strength", "Cường độ điện trường"),
    48: ("Magnetic Field Measurement", "Đo từ trường"),
    49: ("Permeability and Hysteresis Measurement", "Đo độ từ thẩm và hiện tượng trễ"),
    50: ("Inductance Measurement", "Đo điện cảm"),
    51: ("Immittance Measurement", "Đo trở kháng phức"),
    52: ("Q Factor Measurement", "Đo hệ số Q"),
    53: ("Distortion Measurement", "Đo méo"),
    54: ("Noise Measurement", "Đo nhiễu"),
    55: ("Microwave Measurement", "Đo vi ba"),
    56: ("Photometry and Radiometry", "Trắc quang và đo bức xạ"),
    57: ("Densitometry Measurement", "Đo mật độ quang"),
    58: ("Colorimetry", "Đo màu"),
    59: ("Optical Loss", "Tổn hao quang"),
    60: ("Polarization Measurement", "Đo phân cực"),
    61: ("Refractive Index Measurement", "Đo chiết suất"),
    62: ("Turbidity Measurement", "Đo độ đục"),
    63: ("Laser Output Measurement", "Đo đầu ra laser"),
    64: ("Vision and Image Sensors", "Cảm biến thị giác và hình ảnh"),
    65: ("Radioactivity Measurement", "Đo phóng xạ"),
    66: ("Radioactivity Measurement (part 2)", "Đo phóng xạ (phần 2)"),
    67: ("Charged Particle Measurement", "Đo hạt tích điện"),
    68: ("Neutron Measurement", "Đo nơ tron"),
    69: ("Dosimetry Measurement", "Đo liều bức xạ"),
    70: ("Composition Measurement", "Đo thành phần"),
    71: ("pH Measurement", "Đo pH"),
    72: ("Humidity and Moisture Measurement", "Đo độ ẩm"),
    73: ("Environmental Measurement", "Đo môi trường"),
    74: ("Biopotentials and Electrophysiology Measurement", "Đo điện thế sinh học và điện sinh lý"),
    75: ("Blood Pressure Measurement", "Đo huyết áp"),
    76: ("Blood Flow Measurements", "Đo lưu lượng máu"),
    77: ("Ventilation Measurement", "Đo thông khí"),
    78: ("Blood Chemistry Measurement", "Đo hoá học máu"),
    79: ("Medical Imaging", "Chẩn đoán hình ảnh"),
    80: ("Amplifiers and Signal Conditioners", "Bộ khuếch đại và điều hoà tín hiệu"),
    81: ("Modulation", "Điều chế"),
    82: ("Filters", "Bộ lọc"),
    83: ("Spectrum Analysis and Correlation", "Phân tích phổ và tương quan"),
    84: ("Applied Intelligence Processing", "Xử lý thông minh ứng dụng"),
    85: ("Analog-to-Digital Converters", "Bộ chuyển đổi tương tự – số"),
    86: ("Computers", "Máy tính"),
    87: ("Telemetry", "Đo từ xa"),
    88: ("Sensor Networks and Communication", "Mạng cảm biến và truyền thông"),
    89: ("Electromagnetic Compatibility", "Tương thích điện từ"),
    90: ("Human Factors in Displays", "Yếu tố con người trong hiển thị"),
    91: ("Cathode Ray Tube Displays", "Hiển thị ống tia điện tử"),
    92: ("Liquid Crystal Displays", "Hiển thị tinh thể lỏng"),
    93: ("Plasma-Driven Flat Panel Displays", "Hiển thị phẳng plasma"),
    94: ("Electroluminescent Displays", "Hiển thị điện phát quang"),
    95: ("Light-Emitting Diode Displays", "Hiển thị LED"),
    96: ("Reading/Recording Devices", "Thiết bị đọc và ghi"),
    97: ("PID Control", "Điều khiển PID"),
    98: ("Optimal Control", "Điều khiển tối ưu"),
    99: ("Electropneumatic and Electrohydraulic Instruments",
         "Thiết bị điện – khí nén và điện – thuỷ lực"),
    100: ("Explosion-Proof Instruments", "Thiết bị phòng nổ"),
    101: ("Measurement and Identification of Brush, Brushless, and dc Stepping Motors",
          "Đo và nhận diện động cơ bước chổi than, không chổi than và một chiều"),
}

TOTAL = 101
PAGES = 2617
FILES = 117

# chapters that already exist as reader pages: num -> (slug, title-vi)
DONE = {1: "ch01-characteristics-of-instrumentation",
        2: "ch02-operational-modes-of-instrumentation",
        3: "ch03-static-and-dynamic-characteristics-of-instrumentation",
        4: "ch04-measurement-accuracy",
        5: "ch05-measurement-standards",
        6: "ch06-displacement-measurement",
        7: "ch07-thickness-measurement",
        8: "ch08-proximity-sensing-for-robotics",
        9: "ch09-distance",
        10: "ch10-position-location-altitude",
        11: "ch11-level-measurement",
        12: "ch12-area-measurement",
        13: "ch13-volume-measurement",
        14: "ch14-angle-measurement",
        15: "ch15-tilt-measurement",
        16: "ch16-velocity-measurement",
        17: "ch17-acceleration-vibration-shock-measurement",
        18: "ch18-time-measurement",
        19: "ch19-frequency-measurement",
        20: "ch20-mass-and-weight-measurement",
        21: "ch21-density-measurement",
       22: "ch22-strain-measurement",
       23: "ch23-force-measurement",
       24: "ch24-torque-and-power-measurement",
       25: "ch25-tactile-sensing",
       26: "ch26-pressure-and-sound-measurement",
       27: "ch27-acoustic-measurement",
       101: "ch101-measurement-and-identification-of-stepping-motors"}

# appendices that already exist as reader pages (letter -> slug)
APPENDIX = {
    "A": "appendix-a-units-and-conversions",
}

APP_TITLE = {
    "A": ("Units and Conversions", "Đơn vị và quy đổi"),
}


def num(n, lang):
    return format(n, ",d").replace(",", "." if lang == "vi" else ",")


def header(lang, switch_href):
    nav = NAV_EN if lang == "en" else NAV_VI
    links = []
    for href, label in nav:
        cls = ' class="active"' if href.endswith("books/") else ""
        links.append('<a href="%s"%s>%s</a>' % (href, cls, esc(label)))
    if lang == "en":
        links.append('<a href="%s" class="lang-switch">VI</a>' % switch_href)
    else:
        links.append('<a href="%s" class="lang-switch">EN</a>' % switch_href)
    brand_home = "/" if lang == "en" else "/?lang=vi"
    return ('<header class="site-header"><a href="%s" class="brand">%s'
            '<span>Pro InstControl</span></a><nav class="site-nav">%s</nav></header>'
            % (brand_home, MARK, "".join(links)))


def head(lang, title, desc):
    return ('<!doctype html><html lang="%s"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><meta name="description" content="%s">'
            '<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,'
            'wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" '
            'rel="stylesheet"><link rel="stylesheet" href="/books/assets/library.css">'
            '</head><body>' % (lang, esc(title), esc(desc)))


def footer(lang):
    if lang == "vi":
        txt = ("Thư viện Pro InstControl · Bản dịch không chính thức, dùng cho mục đích học tập · "
               "Bản gốc © 1999 CRC Press LLC")
    else:
        txt = ("Pro InstControl Library · Unofficial study copy · "
               "Original text © 1999 CRC Press LLC")
    return '<footer class="site-footer"><p>%s</p></footer></body></html>' % esc(txt)


def toc(lang):
    """Section map + chapter list, 101 rows."""
    out = []
    base = ("/books/read/%s/" if lang == "en" else "/vi/books/read/%s/") % SLUG
    for roman, en, vi, lo, hi in SECTIONS:
        title = en if lang == "en" else vi
        sub = en if lang == "vi" else vi
        ndone = sum(1 for c in DONE if lo <= c <= hi)
        meta = ("%d chapters · %d translated" % (hi - lo + 1, ndone)) if lang == "en" \
            else ("%d chương · %d đã dịch" % (hi - lo + 1, ndone))
        if ndone == 0:
            meta = ("%d chapters · not started" % (hi - lo + 1)) if lang == "en" \
                else ("%d chương · chưa bắt đầu" % (hi - lo + 1))
        rows = []
        for c in range(lo, hi + 1):
            cen, cvi = CH[c]
            label = cen if lang == "en" else cvi
            if c in DONE:
                rows.append(
                    '<li class="done"><span class="n">%d</span>'
                    '<span class="t"><a href="%s%s/">%s</a></span>'
                    '<span class="st"><a href="%s%s/">%s</a></span></li>'
                    % (c, base, DONE[c], esc(label),
                       base, DONE[c],
                       "translated" if lang == "en" else "đã dịch"))
            else:
                rows.append('<li><span class="n">%d</span>'
                            '<span class="t">%s</span><span class="st">%s</span></li>'
                            % (c, esc(label),
                               "pending" if lang == "en" else "chờ dịch"))
        out.append(
            '<h3>%s %s · %s <span class="en">%s</span></h3>'
            '<div style="font-size:.76rem;letter-spacing:.08em;text-transform:uppercase;'
            'color:#888;margin:-.2rem 0 .2rem;">%s</div>'
            '<ul class="toc-list">%s</ul>'
            % ("Section" if lang == "en" else "Mục", roman, esc(title), esc(sub),
               esc(meta), "".join(rows)))
    app = ("Appendix · Units and Conversions" if lang == "en"
           else "Phụ lục · Đơn vị và quy đổi")
    appst = "pending" if lang == "en" else "chờ dịch"
    arows = []
    for letter in ("A",):
        ten, tvi = APP_TITLE[letter]
        label = ten if lang == "en" else tvi
        if letter in APPENDIX:
            url = "%s%s/" % (base, APPENDIX[letter])
            arows.append('<li class="done"><span class="n">%s</span>'
                         '<span class="t"><a href="%s">%s</a></span>'
                         '<span class="st"><a href="%s">%s</a></span></li>'
                         % (letter, url, esc(label), url,
                            "translated" if lang == "en" else "đã dịch"))
        else:
            arows.append('<li><span class="n">%s</span><span class="t">%s</span>'
                         '<span class="st">%s</span></li>'
                         % (letter, esc(label), appst))
    out.append('<h3>%s</h3><ul class="toc-list">%s</ul>'
               % ("Appendix" if lang == "en" else "Phụ lục", "".join(arows)))
    return "".join(out)


def build(lang):
    vi = lang == "vi"
    switch = "/books/read/%s/" % SLUG if vi else "/vi/books/read/%s/" % SLUG
    title = ("Sổ tay Đo lường, Thiết bị đo và Cảm biến" if vi
             else "The Measurement, Instrumentation and Sensors Handbook")
    desc = ("Bản dịch tiếng Việt từng chương của sổ tay CRC về đo lường, thiết bị đo và cảm biến "
            "(Webster, 1999) — 101 chương, 14 mục." if vi else
            "CRC handbook on measurement, instrumentation and sensors (Webster, 1999) — "
            "101 chapters in 14 sections, with a Vietnamese translation in progress.")
    crumb = ("<a href=\"/vi/books/\">Sách</a> · Mục lục sách" if vi
             else "<a href=\"/books/\">Books</a> · Book contents")
    byline = ("Chủ biên: John G. Webster · CRC Press, 1999" if vi
              else "Editor-in-Chief: John G. Webster · CRC Press, 1999")
    meta = ("%s chương · 14 mục · %s trang · %s tệp PDF" % (num(TOTAL, lang), num(PAGES, lang), FILES)
            if vi else
            "%s chapters · 14 sections · %s pages · %s PDF files"
            % (num(TOTAL, lang), num(PAGES, lang), FILES))
    flag = ('<span class="translated-flag" data-level="progress">🟠 Đang dịch · %d/%d chương</span>'
            % (len(DONE), TOTAL) if vi else
            '<span class="translated-flag" data-level="progress">🟠 Translating · %d of %d chapters</span>'
            % (len(DONE), TOTAL))

    if vi:
        lede = ("Sổ tay tham chiếu của ngành: 101 chương do nhiều tác giả viết, đi từ đặc tính của "
                "thiết bị đo qua từng đại lượng được đo, đến xử lý tín hiệu và hiển thị. Bản dịch "
                "tiếng Việt thực hiện theo từng chương, giữ nguyên thuật ngữ gốc trong ngoặc và "
                "giữ nguyên ký hiệu, hình và bảng của bản gốc.")
        policy = ("<b>Cách đọc bản dịch.</b> Mỗi chương được dịch trọn vẹn, không lược bớt, và được "
                  "đặt trên một trang riêng. Tiêu đề mục giữ kèm tên tiếng Anh để đối chiếu với bản "
                  "gốc. Các hình được vẽ lại bằng vector để đọc rõ trên màn hình nhỏ; số hiệu hình, "
                  "bảng và ký hiệu trùng với bản gốc. Đây là bản dịch không chính thức, dùng cho "
                  "mục đích học tập.")
        read = "Đọc Chương 1 →"
        h2 = "Bản đồ chương"
        note2 = ("Bản gốc chỉ đánh số mục 1.1 trong Chương 1; các mục còn lại được đánh số "
                 "1.2–1.6 trong bản dịch để tiện tra cứu.")
        pct = "%.0f%% hoàn thành" % (100.0 * len(DONE) / TOTAL)
    else:
        lede = ("The reference work of the field: 101 chapters by different authors, from the "
                "characteristics of instrumentation through every measured variable to signal "
                "processing and displays. The Vietnamese translation proceeds chapter by chapter; "
                "figures are redrawn as vectors so they stay legible on a phone.")
        policy = ("<b>About this copy.</b> The 117 PDF files are held in the local library "
                  "catalogue and are not republished here. This page is the online contents "
                  "map: what each chapter covers, and which ones already have a Vietnamese "
                  "translation. Figures and terminology follow the original numbering.")
        read = "Read the Vietnamese Chapter 1 →"
        h2 = "Chapter map"
        note2 = "The original numbers only section 1.1 in Chapter 1; sections 1.2–1.6 are numbered here for reference."
        pct = "%.0f%% complete" % (100.0 * len(DONE) / TOTAL)

    ch1 = ("/vi/books/read/%s/ch01-characteristics-of-instrumentation/" % SLUG if vi
           else "/books/read/%s/ch01-characteristics-of-instrumentation/" % SLUG)
    last = max(DONE)
    last_href = ("/vi/books/read/%s/%s/" if vi else "/books/read/%s/%s/") % (SLUG, DONE[last])
    last_label = ("Chương %d →" if vi else "Chapter %d →") % last
    last_title = CH[last][1] if vi else CH[last][0]

    body = (
        '<main><article class="intranet-content reader">'
        '<div class="reader-hero">'
        '<div class="breadcrumb">%s</div>'
        '<h1>%s</h1>'
        '<p class="byline">%s</p>'
        '<div class="meta-line">%s</div>'
        '</div>'
        '<div class="prose">'
        '%s'
        '<div class="progress-bar"><i style="width:%d%%"></i></div>'
        '<p style="font-size:.78rem;color:#888;letter-spacing:.06em;text-transform:uppercase;'
        'margin:-.8rem 0 1.6rem;">%s</p>'
        '<p class="lead">%s</p>'
        '<div class="note">%s</div>'
        '<p><a href="%s"><strong>%s</strong></a></p>'
        '<h2>%s</h2>'
        '%s'
        '<div class="note">%s</div>'
        '<div class="chapter-nav">'
        '<a href="%s"><span class="k">← %s</span>%s</a>'
        '<a href="%s" style="text-align:right;"><span class="k">%s</span>%s</a>'
        '</div>'
        '</div></article></main>'
        % (crumb, esc(title), esc(byline), esc(meta),
           flag, max(1, round(100.0 * len(DONE) / TOTAL)), pct,
           lede, policy, ch1, read, h2, toc(lang), note2,
           "/vi/books/" if vi else "/books/",
           "Thư viện" if vi else "Library",
           esc("Tất cả sách" if vi else "All books"),
           last_href, last_label, esc(last_title))
    )
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang)


def main():
    pairs = [("en", os.path.join(ROOT, "books", "read", SLUG, "index.html")),
             ("vi", os.path.join(ROOT, "vi", "books", "read", SLUG, "index.html"))]
    for lang, path in pairs:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        page = build(lang)
        open(path, "w", encoding="utf-8").write(page)
        print("wrote %s  %d kB" % (path, len(page) // 1024))
    # checks
    page = build("vi")
    print("--- checks ---")
    print("toc rows:", page.count("<li class=\"done\"") + page.count("<li><span class=\"n\""))
    print("done rows:", page.count("class=\"done\""))
    print("sections:", len(SECTIONS))
    print("chapters:", len(CH))


if __name__ == "__main__":
    main()
