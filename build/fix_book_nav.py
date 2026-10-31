"""Upgrade the book pages' top navigation to the full site nav.

The library pages were built with a shorter, older nav (9 links), so Applications,
Install, Geotech, Glossary and Education were unreachable from any book page.
This rewrites the <nav class="site-nav"> block in every page under books/ and
vi/books/ to the same link set and order as the topic pages, keeping each page's
existing "active" link and language switch intact.

Idempotent: re-running it produces the same output.

    python build/fix_book_nav.py
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LINKS = [
    ("/", "Home", "Trang chủ"),
    ("/books/", "Books", "Sách"),
    ("/fundamentals.html", "Fundamentals", "Cơ bản"),
    ("/advanced/", "Advanced", "Nâng cao"),
    ("/instruments.html", "Instruments", "Thiết bị"),
    ("/install.html", "Install", "Lắp đặt"),
    ("/control.html", "Control", "Điều khiển"),
    ("/applications.html", "Applications", "Ứng dụng"),
    ("/safety.html", "Safety", "An toàn"),
    ("/tools.html", "Tools", "Công cụ"),
    ("/comparison.html", "Comparison", "So sánh"),
    ("/geotechnical.html", "Geotech", "Địa kỹ thuật"),
    ("/standards.html", "Standards", "Tiêu chuẩn"),
    ("/glossary.html", "Glossary", "Thuật ngữ"),
    ("/education.html", "Education", "Giáo dục"),
]

NAV_RE = re.compile(r'<nav class="site-nav">.*?</nav>', re.S)
ACTIVE_RE = re.compile(r'<a href="([^"]*)" class="active">')
SWITCH_RE = re.compile(r'<a href="([^"]*)" class="lang-switch">([^<]*)</a>')

# Sections that exist twice, as real URLs. Their Vietnamese nav points at the
# /vi/ twin rather than taking a ?lang=vi hint on the English page.
VI_TWIN = {"/books/": "/vi/books/", "/advanced/": "/vi/advanced/"}


def build_nav(active, switch_href, switch_label, vi):
    parts = []
    for href, en, vi_label in LINKS:
        label = vi_label if vi else en
        if vi and href in VI_TWIN:
            target = VI_TWIN[href]
        elif vi:
            # Topic pages take a ?lang=vi hint so the i18n script starts in Vietnamese.
            target = href + ("&lang=vi" if "?" in href else "?lang=vi")
        else:
            target = href
        is_active = href == active or target == active
        if is_active and active:
            target = active  # keep the page's own spelling of its own URL
        cls = ' class="active"' if is_active else ""
        parts.append('<a href="%s"%s>%s</a>' % (target, cls, label))
    if switch_href:
        parts.append('<a href="%s" class="lang-switch">%s</a>' % (switch_href, switch_label))
    return '<nav class="site-nav">' + "".join(parts) + "</nav>"


def main():
    changed = skipped = 0
    for base in ("books", os.path.join("vi", "books")):
        for root, _dirs, files in os.walk(os.path.join(ROOT, base)):
            for name in files:
                if not name.endswith(".html"):
                    continue
                path = os.path.join(root, name)
                rel = os.path.relpath(path, ROOT).replace("\\", "/")
                vi = rel.startswith("vi/")
                src = open(path, encoding="utf-8").read()
                m = NAV_RE.search(src)
                if not m:
                    skipped += 1
                    continue
                nav = m.group(0)
                a = ACTIVE_RE.search(nav)
                active = a.group(1) if a else None
                sw = SWITCH_RE.search(nav)
                switch_href = sw.group(1) if sw else None
                switch_label = sw.group(2) if sw else None
                new = build_nav(active, switch_href, switch_label, vi)
                if new == nav:
                    continue
                open(path, "w", encoding="utf-8", newline="\n").write(src.replace(nav, new, 1))
                changed += 1
    print("nav updated on %d pages (%d without a site-nav)" % (changed, skipped))


if __name__ == "__main__":
    main()
