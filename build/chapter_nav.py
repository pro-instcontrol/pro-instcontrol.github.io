# -*- coding: utf-8 -*-
"""Insert / refresh the three-item bottom chapter nav on every handbook chapter page.

Left  = previous chapter, shown as "Chapter N" + its title.
Middle = the book's table of contents.
Right = next chapter, shown as "Chapter N" + its title.

Runs after the reader generators (which do not know about the next chapter).
Run:  python build/chapter_nav.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reader_handbook import SLUG, CH, DONE, APPENDIX, APP_TITLE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NCH = max(CH)
FIRST_APPENDIX = "A" if "A" in APPENDIX else None

BOOK_EN = "Measurement, Instrumentation and Sensors Handbook"
BOOK_VI = "Sổ tay Đo lường, Thiết bị đo và Cảm biến"


def nav(lang, cur):
    en = lang == "en"
    base = ("/books/read/%s/" if en else "/vi/books/read/%s/") % SLUG

    def href(n):
        return (base + DONE[n] + "/") if n in DONE else base

    out = ['<div class="chapter-nav">']

    # ---- previous
    p = cur - 1
    if p >= 1:
        title = CH[p][0] if en else CH[p][1]
        k = ("← Chapter %d" if en else "← Chương %d") % p
        out.append('<a href="%s"><span class="k">%s</span>%s</a>' % (href(p), k, title))
    else:
        out.append('<span class="disabled"><span class="k">%s</span></span>'
                   % ("← Book start" if en else "← Đầu sách"))

    # ---- home = book TOC
    out.append('<a href="%s" style="text-align:center"><span class="k">%s</span>%s</a>'
               % (base, "Home" if en else "Trang chủ",
                  "Book TOC" if en else "Mục lục sách"))

    # ---- next
    n = cur + 1
    if cur == NCH and FIRST_APPENDIX:
        title = APP_TITLE[FIRST_APPENDIX][0 if en else 1]
        k = ("Appendix %s →" if en else "Phụ lục %s →") % FIRST_APPENDIX
        out.append('<a href="%s%s/" style="text-align:right"><span class="k">%s</span>%s</a>'
                   % (base, APPENDIX[FIRST_APPENDIX], k, title))
    elif n <= NCH:
        title = CH[n][0] if en else CH[n][1]
        k = ("Chapter %d →" if en else "Chương %d →") % n
        out.append('<a href="%s" style="text-align:right"><span class="k">%s</span>%s</a>'
                   % (href(n), k, title))
    else:
        out.append('<span class="disabled" style="text-align:right"><span class="k">%s</span></span>'
                   % ("Book end →" if en else "Cuối sách →"))

    out.append("</div>")
    return "".join(out)


NAV_RE = re.compile(r'<div class="chapter-nav">.*?</div>', re.S)


def process(path, lang, cur):
    s = open(path, encoding="utf-8").read()
    block = nav(lang, cur)
    if NAV_RE.search(s):
        s2 = NAV_RE.sub(block, s, count=1)
    elif "</article>" in s:
        i = s.rfind("</article>")
        s2 = s[:i] + block + s[i:]
    elif "</main>" in s:
        i = s.rfind("</main>")
        s2 = s[:i] + block + s[i:]
    else:
        return False
    if s2 != s:
        open(path, "w", encoding="utf-8").write(s2)
    return True


def main():
    n = 0
    for cur, slug in sorted(DONE.items()):
        for lang, root in (("en", "books"), ("vi", os.path.join("vi", "books"))):
            path = os.path.join(ROOT, root, "read", SLUG, slug, "index.html")
            if os.path.exists(path) and process(path, lang, cur):
                n += 1
    print("chapter-nav: %d pages updated" % n)


if __name__ == "__main__":
    main()
