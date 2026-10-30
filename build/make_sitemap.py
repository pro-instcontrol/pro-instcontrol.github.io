"""Generate sitemap.xml and robots.txt from the published HTML pages.

Run from the repository root after every build/deploy:

    python build/make_sitemap.py

Every index.html becomes a directory URL, and each English page is paired with
its Vietnamese counterpart through <xhtml:link rel="alternate" hreflang="...">.
Pages marked noindex (the legacy /library/ redirect) are skipped.
"""

import os
import re

BASE = "https://pro-instcontrol.github.io"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "dist", "work", "shots", "kb", ".workbuddy-ai"}


def page_url(rel):
    """'books/index.html' -> '/books/', 'index.html' -> '/'."""
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def collect():
    urls = {}
    for root, dirs, files in os.walk(ROOT):
        rel_root = os.path.relpath(root, ROOT).replace("\\", "/")
        if rel_root == ".":
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if not name.endswith(".html"):
                continue
            rel = name if rel_root == "." else rel_root + "/" + name
            full = os.path.join(root, name)
            try:
                head = open(full, encoding="utf-8", errors="replace").read(2048)
            except OSError:
                continue
            if re.search(r'name="robots"[^>]*noindex', head):
                continue
            if rel == "404.html":
                continue
            urls[page_url(rel)] = True
    return urls


def pair(url, urls):
    """Return (en, vi) for a page, or (None, None) when it has no sibling."""
    if url.startswith("/vi/"):
        en, vi = url[3:], url
    else:
        en, vi = url, "/vi" + url
    if en in urls and vi in urls:
        return en, vi
    return None, None


def main():
    urls = collect()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url in sorted(urls):
        en, vi = pair(url, urls)
        out.append("  <url>")
        out.append("    <loc>%s%s</loc>" % (BASE, url))
        if en:
            out.append('    <xhtml:link rel="alternate" hreflang="en" href="%s%s"/>' % (BASE, en))
            out.append('    <xhtml:link rel="alternate" hreflang="vi" href="%s%s"/>' % (BASE, vi))
            out.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>' % (BASE, en))
        out.append("  </url>")
    out.append("</urlset>")
    out.append("")

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out))

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("User-agent: *\n")
        fh.write("Allow: /\n")
        fh.write("Disallow: /shots/\n")
        fh.write("\n")
        fh.write("Sitemap: %s/sitemap.xml\n" % BASE)

    print("sitemap.xml: %d URLs, %d with EN/VI pairs"
          % (len(urls), sum(1 for u in urls if pair(u, urls)[0])))


if __name__ == "__main__":
    main()
