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


def siblings(url, urls):
    """The root EN url of a page plus the /vi/ and /es/ twins that exist.

    'books/' -> [('en','/books/')]; '/vi/glossary.html' with an /es/ twin
    present -> [('en','/glossary.html'), ('vi','/vi/glossary.html'),
    ('es','/es/glossary.html')].
    """
    if url.startswith("/vi/"):
        en = url[3:]
    elif url.startswith("/es/"):
        en = url[4:]
    else:
        en = url
    out = [("en", en)]
    if "/vi" + en in urls:
        out.append(("vi", "/vi" + en))
    if "/es" + en in urls:
        out.append(("es", "/es" + en))
    return out


def main():
    urls = collect()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url in sorted(urls):
        sibs = siblings(url, urls)
        out.append("  <url>")
        out.append("    <loc>%s%s</loc>" % (BASE, url))
        if len(sibs) > 1:
            for lang, u in sibs:
                out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>'
                           % (lang, BASE, u))
            out.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>'
                       % (BASE, sibs[0][1]))
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

    print("sitemap.xml: %d URLs, %d with language siblings"
          % (len(urls), sum(1 for u in urls if len(siblings(u, urls)) > 1)))


if __name__ == "__main__":
    main()
