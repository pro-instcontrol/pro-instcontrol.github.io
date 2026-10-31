# -*- coding: utf-8 -*-
"""Generic reader landing-page generator for any book in the library.

Usage:
    python reader_book.py            # renders every BOOKS entry below
    python reader_book.py sis        # renders only the 'sis' book

Each book is a SPEC dict (see BOOKS).  The generator mirrors the
taichikb.github.io/books reader structure and the styling in
books/assets/library.css.  Chapter 1 (and any other translated chapter)
must already exist as a reader page under:

    vi/books/read/<slug>/<chap-slug>/index.html
    books/read/<slug>/<chap-slug>/index.html
"""
import os

from books_site import MARK, NAV_EN, NAV_VI, esc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Book specifications
# ---------------------------------------------------------------------------
BOOKS = {
    "sis": {
        "slug": "safety-instrumented-systems-design-analysis-justification",
        "title_en": "Safety Instrumented Systems — Design, Analysis, and Justification",
        "title_vi": "Hệ thống đo lường an toàn — Thiết kế, phân tích và biện minh",
        "byline_en": "Paul Gruhn, P.E., CFSE & Harry L. Cheddie, P.Eng., CFSE · ISA, 2006 (2nd ed.)",
        "byline_vi": "Paul Gruhn, P.E., CFSE & Harry L. Cheddie, P.Eng., CFSE · ISA, 2006 (bản 2)",
        "pages": 320,
        "files": 19,
        "first_en": ("ch01-introduction",
                     "Introduction"),
        "first_vi": ("ch01-introduction",
                     "Giới thiệu"),
        "chapters": {
            1: ("Introduction", "Giới thiệu"),
            2: ("Design Lifecycle", "Vòng đời thiết kế"),
            3: ("Process Control vs. Safety Control", "Điều khiển quá trình so với điều khiển an toàn"),
            4: ("Protection Layers", "Các lớp bảo vệ"),
            5: ("Developing the Safety Requirement Specifications", "Xây dựng đặc tả yêu cầu an toàn"),
            6: ("Determining the Safety Integrity Level (SIL)", "Xác định mức độ toàn vẹn an toàn (SIL)"),
            7: ("Choosing a Technology", "Lựa chọn công nghệ"),
            8: ("Initial System Evaluation", "Đánh giá hệ thống ban đầu"),
            9: ("Issues Relating to Field Devices", "Các vấn đề liên quan đến thiết bị trường"),
            10: ("Engineering a System", "Thiết kế kỹ thuật một hệ thống"),
            11: ("Installing a System", "Lắp đặt hệ thống"),
            12: ("Functional Testing", "Thử nghiệm chức năng"),
            13: ("Managing Changes to a System", "Quản lý thay đổi hệ thống"),
            14: ("Justification for a Safety System", "Biện minh cho hệ thống an toàn"),
            15: ("SIS Design Checklist", "Danh mục kiểm tra thiết kế SIS"),
            16: ("Case Study", "Nghiên cứu tình huống"),
        },
        "done": {1: "ch01-introduction", 2: "ch02-design-lifecycle",
                 3: "ch03-process-control-vs-safety-control",
                 4: "ch04-protection-layers",
                 5: "ch05-developing-the-safety-requirement-specifications"},
        "copyright_en": "Original text © 2006 ISA — The Instrumentation, Systems, and Automation Society",
        "copyright_vi": "Bản gốc © 2006 ISA — Hiệp hội Đo lường, Hệ thống và Tự động hóa",
        "lede_en": ("The practical “how-to” on specifying, analysing, designing, installing and "
                    "justifying safety instrumented systems — from the difference between process "
                    "control and safety control through to lifecycle management. The Vietnamese "
                    "translation proceeds chapter by chapter."),
        "lede_vi": ("Cuốn sách thực hành “cách làm” về xác định, phân tích, thiết kế, lắp đặt và "
                    "biện minh cho các hệ thống đo lường an toàn — từ sự khác biệt giữa điều khiển "
                    "quá trình và điều khiển an toàn cho đến quản lý vòng đời. Bản dịch tiếng Việt "
                    "thực hiện theo từng chương."),
        "policy_en": ("<b>About this copy.</b> The 19 PDF files are held in the local library "
                      "catalogue and are not republished here. This page is the online contents "
                      "map: what each chapter covers and which chapters already have a Vietnamese "
                      "translation."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> 19 tệp PDF được lưu trong thư viện cục bộ và "
                      "không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội "
                      "dung từng chương và những chương nào đã có bản dịch tiếng Việt."),
        "note_en": "Figures follow the original numbering where the source chapter contains them.",
        "note_vi": "Hình ảnh giữ nguyên số hiệu của bản gốc tại những chương có hình.",
    },

    "pc": {
        "slug": "pc-process-control",
        "title_en": "Practical Process Control for Engineers and Technicians",
        "title_vi": "Điều khiển quá trình thực hành dành cho kỹ sư và kỹ thuật viên",
        "byline_en": "Wolfgang Altmann · IDC Technologies (Version 3.02)",
        "byline_vi": "Wolfgang Altmann · IDC Technologies (Phiên bản 3.02)",
        "pages": 1008,
        "files": 35,
        "first_en": ("ch01-introduction",
                     "Introduction"),
        "first_vi": ("ch01-introduction",
                     "Giới thiệu"),
        "chapters": {
            1: ("Introduction", "Giới thiệu"),
            2: ("Process Measurement and Transducers", "Đo lường quá trình và cảm biến"),
            3: ("Basic Principles of Control Valves and Actuators", "Nguyên lý cơ bản của van điều khiển và cơ cấu chấp hành"),
            4: ("Fundamentals of Control Systems", "Các nguyên lý cơ bản của hệ thống điều khiển"),
            5: ("Stability and Control Modes of Closed Loops", "Ổn định và các mode điều khiển vòng kín"),
            6: ("Digital Control Principles", "Các nguyên lý điều khiển số"),
            7: ("Real and Ideal P.I.D. Controllers", "Bộ điều khiển PID thực và lý tưởng"),
            8: ("Tuning of PID Controllers in Open and Closed Loop", "Tìm điểm làm việc bộ điều khiển PID"),
            9: ("Controller Output Modes, Equations and Cascade Control", "Các mode đầu ra, phương trình và điều khiển bậc thang"),
            10: ("Concepts and Applications of Feedforward Control", "Khái niệm và ứng dụng điều khiển theo hướng"),
            11: ("Combined Feedback and Feedforward Control", "Kết hợp phản hồi và theo hướng"),
            12: ("Long Process Dead-Time and the Smith Predictor", "Trễ chết dài và bộ dự đoán Smith"),
            13: ("Basic Principles of Fuzzy Logic and Neural Networks", "Nguyên lý cơ bản mạng mờ và mạng nơ-ron"),
            14: ("Self-Tuning Intelligent Control and SPC", "Tự chỉnh, điều khiển thông minh và SPC"),
        },
        "appendices": [
            ("A", "Some Laplace Transform Pairs", "Một số cặp biến đổi Laplace"),
            ("B", "Block Diagram Transformation Theorems", "Các định lý biến đổi sơ đồ khối"),
            ("C", "Detail Display", "Hiển thị chi tiết"),
            ("D", "Auxiliary Display", "Hiển thị phụ trợ"),
            ("E", "Configuring a Tuning Exercise in a Controller", "Cấu hình bài tập tìm điểm trong bộ điều khiển"),
            ("F", "Installation of Simulation Software", "Cài đặt phần mềm mô phỏng"),
            ("G", "Operation of Simulation Software", "Vận hành phần mềm mô phỏng"),
            ("H", "Configuration", "Cấu hình"),
            ("I", "General Syntax of Configuration Commands", "Cú pháp chung của lệnh cấu hình"),
            ("J", "Configuration Commands", "Các lệnh cấu hình"),
            ("K", "Algorithms", "Các thuật toán"),
            ("L", "Background Graphics Design", "Thiết kế đồ họa nền"),
            ("M", "Configuration Example", "Ví dụ cấu hình"),
        ],
        "done": {1: "ch01-introduction",
                 2: "ch02-process-measurement-and-transducers",
                 3: "ch03-basic-principles-of-control-valves-and-actuators",
                 4: "ch04-fundamentals-of-control-systems",
                 5: "ch05-stability-and-control-modes-of-closed-loops"},
        "copyright_en": "Original text © IDC Technologies Pty Ltd",
        "copyright_vi": "Bản gốc © IDC Technologies Pty Ltd",
        "lede_en": ("A hands-on training manual covering process dynamics, measurement, valves, "
                    "control modes, PID tuning, feedforward, fuzzy logic and statistical process "
                    "control. The Vietnamese translation proceeds chapter by chapter; figures are "
                    "redrawn as vectors so they stay legible on a phone."),
        "lede_vi": ("Giáo trình thực hành về động học quá trình, đo lường, van, các mode điều khiển, "
                    "tìm điểm PID, theo hướng, mạng mờ và điều khiển thống kê quá trình. Bản dịch "
                    "tiếng Việt thực hiện theo từng chương; hình được vẽ lại bằng vector để rõ nét "
                    "trên điện thoại."),
        "policy_en": ("<b>About this copy.</b> The 35 PDF files are held in the local library "
                      "catalogue and are not republished here. This page is the online contents "
                      "map: what each chapter covers and which chapters already have a Vietnamese "
                      "translation."),
        "policy_vi": ("<b>Cách đọc bản dịch.</b> 35 tệp PDF được lưu trong thư viện cục bộ và "
                      "không được đăng lại tại đây. Trang này là bản đồ mục lục trực tuyến: nội "
                      "dung từng chương và những chương nào đã có bản dịch tiếng Việt."),
        "note_en": "Figures follow the original numbering (Ch.1 alone has Figures 1.1–1.12).",
        "note_vi": "Hình ảnh giữ nguyên số hiệu bản gốc (riêng Chương 1 có Hình 1.1–1.12).",
    },
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


def footer(lang, spec):
    txt = (("Thư viện Pro InstControl · Bản dịch không chính thức, dùng cho mục đích học tập · "
            if lang == "vi" else
            "Pro InstControl Library · Unofficial study copy · ")
           + (spec["copyright_vi"] if lang == "vi" else spec["copyright_en"]))
    return '<footer class="site-footer"><p>%s</p></footer></body></html>' % esc(txt)


def done_for(lang, spec):
    """Per-language 'done' map; falls back to the shared 'done' map.

    Used so a chapter can be marked translated in one language (e.g. the
    Vietnamese translation-in-progress) without claiming it exists in the
    other language where the reader page has not been built yet.
    """
    return spec.get("done_%s" % lang) or spec.get("done", {})


def toc(lang, spec):
    out = []
    base = ("/books/read/%s/" if lang == "en" else "/vi/books/read/%s/") % spec["slug"]
    chapters = spec["chapters"]
    done = done_for(lang, spec)
    total = len(chapters)
    ndone = len(done)
    rows = []
    for c in sorted(chapters):
        cen, cvi = chapters[c]
        label = cen if lang == "en" else cvi
        if c in done:
            rows.append(
                '<li class="done"><span class="n">%d</span>'
                '<span class="t"><a href="%s%s/">%s</a></span>'
                '<span class="st">%s</span></li>'
                % (c, base, done[c], esc(label),
                   "translated" if lang == "en" else "đã dịch"))
        else:
            rows.append('<li><span class="n">%d</span>'
                        '<span class="t">%s</span><span class="st">%s</span></li>'
                        % (c, esc(label),
                           "pending" if lang == "en" else "chờ dịch"))
    meta = ("%d chapters · %d translated" % (total, ndone)) if lang == "en" \
        else ("%d chương · %d đã dịch" % (total, ndone))
    out.append('<h3>%s</h3>'
               '<div style="font-size:.76rem;letter-spacing:.08em;text-transform:uppercase;'
               'color:#888;margin:-.2rem 0 .2rem;">%s</div>'
               '<ul class="toc-list">%s</ul>'
               % (("Chapters" if lang == "en" else "Các chương"),
                  esc(meta), "".join(rows)))
    # appendices
    if "appendices" in spec:
        arows = []
        for letter, en, vi in spec["appendices"]:
            label = en if lang == "en" else vi
            arows.append('<li><span class="n">%s</span><span class="t">%s</span>'
                         '<span class="st">%s</span></li>'
                         % (esc(letter), esc(label),
                            "pending" if lang == "en" else "chờ dịch"))
        out.append('<h3>%s</h3><ul class="toc-list">%s</ul>'
                   % (("Appendices" if lang == "en" else "Phụ lục"),
                      "".join(arows)))
    return "".join(out)


def build(lang, spec):
    vi = lang == "vi"
    slug = spec["slug"]
    switch = ("/books/read/%s/" if vi else "/vi/books/read/%s/") % slug
    title = spec["title_vi"] if vi else spec["title_en"]
    desc = (spec["lede_vi"] if vi else spec["lede_en"])[0:160]
    crumb = ("<a href=\"/vi/books/\">Sách</a> · Mục lục sách" if vi
             else "<a href=\"/books/\">Books</a> · Book contents")
    byline = spec["byline_vi"] if vi else spec["byline_en"]
    total = len(spec["chapters"])
    ndone = len(done_for(lang, spec))
    meta = ("%s chương · %s trang · %s tệp PDF"
            % (num(total, lang), num(spec["pages"], lang), spec["files"])) if vi \
        else ("%s chapters · %s pages · %s PDF files"
              % (num(total, lang), num(spec["pages"], lang), spec["files"]))
    flag = ('<span class="translated-flag" data-level="progress">🟠 Đang dịch · %d/%d chương</span>'
            % (ndone, total) if vi else
            '<span class="translated-flag" data-level="progress">🟠 Translating · %d of %d chapters</span>'
            % (ndone, total))
    lede = spec["lede_vi"] if vi else spec["lede_en"]
    policy = spec["policy_vi"] if vi else spec["policy_en"]
    read = ("Đọc Chương 1 →" if vi else "Read the Vietnamese Chapter 1 →")
    h2 = "Bản đồ chương" if vi else "Chapter map"
    note2 = spec["note_vi"] if vi else spec["note_en"]
    pct = "%.0f%% hoàn thành" % (100.0 * ndone / total) if vi \
        else "%.0f%% complete" % (100.0 * ndone / total)

    chap_slug, chap_title = (spec["first_vi"] if vi else spec["first_en"])
    chap_href_vi = "/vi/books/read/%s/%s/" % (slug, spec["done"][1])
    chap_href_en = "/books/read/%s/%s/" % (slug, spec["done"][1])

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
           flag, max(1, round(100.0 * ndone / total)), pct,
           lede, policy,
           (chap_href_vi if vi else chap_href_en), read,
           h2, toc(lang, spec), note2,
           "/vi/books/" if vi else "/books/",
           "Thư viện" if vi else "Library",
           esc("Tất cả sách" if vi else "All books"),
           chap_href_vi if vi else chap_href_en,
           "Chương 1 →" if vi else "Chapter 1 →",
           esc(chap_title))
    )
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang, spec)


def main():
    import sys
    wanted = sys.argv[1:] or list(BOOKS)
    for key in wanted:
        spec = BOOKS[key]
        for lang in ("en", "vi"):
            pair = ("vi/books/read/%s/index.html" if lang == "vi"
                    else "books/read/%s/index.html") % spec["slug"]
            path = os.path.join(ROOT, *pair.split("/"))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            page = build(lang, spec)
            open(path, "w", encoding="utf-8").write(page)
            print("wrote %s  %d kB" % (path, len(page) // 1024))
        # quick checks on the vi page
        page = build("vi", spec)
        print("--- %s checks ---" % key)
        print("toc rows:", page.count('<li class="done"') + page.count('<li><span class="n"'))
        print("done rows:", page.count('class="done"'))
        print("chapters:", len(spec["chapters"]))


if __name__ == "__main__":
    main()
