"""Rewrite the library pages' top navigation to the one site nav.

The library sub-site has its own stylesheet and header, but it must not have its
own idea of what the site contains: it used to carry a 15-link list that omitted
Videos and Hot topics, so those two sections were unreachable from any of the
400-odd book pages. The link set now comes from framework.NAV, via books_site,
so it is the same seventeen links in the same order as the rest of the site.

This tool exists for pages already on disk: regenerating the whole library to
change one block would rewrite 400 files. It is idempotent — re-running produces
byte-identical output.

    python build/fix_book_nav.py
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import books_site  # noqa: E402

NAV_RE = re.compile(r'<nav class="site-nav">.*?</nav>', re.S)
ACTIVE_RE = re.compile(r'<a href="([^"]*)" class="active">')
SWITCH_RE = re.compile(r'<a href="([^"]*)" class="lang-switch">([^<]*)</a>')


def build_nav(active, switch_href, switch_label, vi):
    links = books_site.NAV_VI if vi else books_site.NAV_EN
    parts = []
    for target, label in links:
        cls = ' class="active"' if active is not None and target == active else ""
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
                with open(path, encoding="utf-8") as fh:
                    src = fh.read()
                m = NAV_RE.search(src)
                if not m:
                    skipped += 1
                    continue
                nav = m.group(0)
                a = ACTIVE_RE.search(nav)
                # Every page in this tree is a library page, so Books is always
                # the current section. Fall back to that rather than inheriting
                # nothing: eight pages had lost their marker, and a nav with no
                # current item looks broken even though every link is right.
                active = a.group(1) if a else ("/vi/books/" if vi else "/books/")
                sw = SWITCH_RE.search(nav)
                switch_href = sw.group(1) if sw else None
                switch_label = sw.group(2) if sw else None
                new = build_nav(active, switch_href, switch_label, vi)
                if new == nav:
                    continue
                with open(path, "w", encoding="utf-8", newline="\r\n") as fh:
                    fh.write(src.replace(nav, new, 1))
                changed += 1
    print("nav updated on %d pages (%d without a site-nav)" % (changed, skipped))


if __name__ == "__main__":
    main()
