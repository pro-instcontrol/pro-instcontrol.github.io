# -*- coding: utf-8 -*-
"""Shared helpers + page renderer for handbook chapter generators (Ch. 37+).

Each chapter file (reader_hb_chNN.py) defines metadata, an optional FIGS dict
of inline SVG, and body_vi()/body_en() prose, then calls ``page(...)`` (or
``write_chapter(...)``) to emit the two bilingual HTML pages. This keeps the
generated markup identical to the hand-written chapters 1–31.
"""
import os
import re

from reader_handbook import SLUG, head, header, footer

BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG

# --- Bottom Previous / Home / Next navigation (ch02 style) -------------------
# Built in correct reading order so sub-sections (ch06-1..12) thread in
# sequence, and the final chapter links to Appendix A.

APPENDIX = "appendix-a-units-and-conversions"
_ORDER_VI = None
_ORDER_EN = None


def _scan(lang):
    global _ORDER_VI, _ORDER_EN
    cache = _ORDER_VI if lang == "vi" else _ORDER_EN
    if cache is not None:
        return cache
    base = _base_dir(lang)
    out = []
    if os.path.isdir(base):
        for d in sorted(os.listdir(base)):
            m = re.match(r"^ch(\d+)(?:-(\d+))?", d)
            if m and os.path.isdir(os.path.join(base, d)):
                out.append((int(m.group(1)), int(m.group(2)) if m.group(2) else 0, d))
        out.sort()
    if lang == "vi":
        _ORDER_VI = out
    else:
        _ORDER_EN = out
    return out


def _base_dir(lang):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if lang == "vi":
        return os.path.join(root, "vi", "books", "read", SLUG)
    return os.path.join(root, "books", "read", SLUG)


def _h1(lang, slug):
    p = os.path.join(_base_dir(lang), slug, "index.html")
    if not os.path.isfile(p):
        return slug
    h = open(p, encoding="utf-8").read()
    m = re.search(r"<h1>(.*?)</h1>", h, re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else slug


def _strip_prefix(t):
    for pre in ("Phụ lục A — ", "Appendix A — ", "Phụ lục A - ", "Appendix A - "):
        if t.startswith(pre):
            return t[len(pre):].strip()
    return t


def _disp(main, sub):
    return "%d.%d" % (main, sub) if sub else str(main)


def chapter_nav(cslug, lang):
    """Return the canonical <div class="chapter-nav">… for chapter `cslug`."""
    order = _scan(lang)
    slugs = [o[2] for o in order]
    if cslug not in slugs:
        return ""
    i = slugs.index(cslug)
    main, sub, _ = order[i]
    vi = lang == "vi"
    base_url = BASE_VI if vi else BASE_EN
    home = ('<a href="%s" style="text-align:center"><span class="k">%s</span>%s</a>'
            % (base_url, "Trang chủ" if vi else "Home", "Mục lục sách" if vi else "Book TOC"))
    if i == 0:
        prev = ('<span class="disabled"><span class="k">← %s</span></span>'
                % ("Đầu sách" if vi else "Book start"))
    else:
        pm, ps, pslug = order[i - 1]
        pt = _h1(lang, pslug)
        label = ("Chương %s" if vi else "Chapter %s") % _disp(pm, ps)
        prev = ('<a href="%s%s/"><span class="k">← %s</span>%s</a>' % (base_url, pslug, label, pt))
    if i == len(order) - 1:
        at = _strip_prefix(_h1(lang, APPENDIX))
        label = "Phụ lục A" if vi else "Appendix A"
        nxt = ('<a href="%s%s/" style="text-align:right"><span class="k">%s →</span>%s</a>'
               % (base_url, APPENDIX, label, at))
    else:
        nm, ns, nslug = order[i + 1]
        nt = _h1(lang, nslug)
        label = ("Chương %s" if vi else "Chapter %s") % _disp(nm, ns)
        nxt = ('<a href="%s%s/" style="text-align:right"><span class="k">%s →</span>%s</a>'
               % (base_url, nslug, label, nt))
    return '<div class="chapter-nav">' + prev + home + nxt + '</div>'


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def table(head, rows, cap):
    th = "".join("<th>%s</th>" % c for c in head)
    tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>' % (th, tr, cap))


def make_fig(figs, ch_no):
    def fig(n, lang="vi"):
        if n not in figs:
            return ""
        svg, cap_vi, cap_en, _av, _ae = figs[n]
        cap = cap_vi if lang == "vi" else cap_en
        return ('<figure class="figure" id="fig-%d-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
                % (ch_no, n, svg, cap))
    return fig


def _count_tables(s):
    return s.count("<table")


def page(lang, cslug, ch_no, title_en, title_vi, byline, body_vi, body_en,
         figs, extra_vi="", extra_en=""):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, cslug)) if vi else ("%s%s/" % (BASE_VI, cslug))
    title = ("Chương %d — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % (ch_no, title_vi) if vi
             else "Chapter %d — %s · Measurement, Instrumentation and Sensors Handbook" % (ch_no, title_en))
    fn = body_vi if vi else body_en
    nfig = len(figs)
    ntab = _count_tables(fn)
    desc = ("Bản dịch tiếng Việt Chương %d “%s” — %s%s" % (ch_no, title_vi, title_en, (" · " + extra_vi) if extra_vi else "")) if vi \
        else ("Companion to Chapter %d of the CRC Measurement Handbook — %s%s" % (ch_no, title_en, (" · " + extra_en) if extra_en else ""))
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương %d' % (BASE_VI, ch_no) if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter %d' % (BASE_EN, ch_no))
    meta = ("Chương %d · %s · %d hình, %d bảng" % (ch_no, title_vi, nfig, ntab) if vi
            else "Chapter %d · %s · %d figures, %d tables" % (ch_no, title_en, nfig, ntab))
    nav = chapter_nav(cslug, lang)
    if nav:
        fn = re.sub(r'<div class="chapter-nav">.*?</div>', '', fn, flags=re.S)
        fn = fn.rstrip() + nav
    body_html = ('<main><article class="intranet-content reader"><div class="reader-hero">'
                 '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
                 '<div class="meta-line">%s</div></div><div class="prose">%s</div></article></main>'
                 % (crumb, title_vi if vi else title_en, byline, meta, fn))
    return head(lang, title, desc) + header(lang, switch) + body_html + footer(lang)


def write_chapter(ch_no, cslug, title_en, title_vi, byline, body_vi, body_en,
                  figs, extra_vi="", extra_en=""):
    """Render and write both EN + VI pages; return list of written paths."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = []
    for lang, sub in (("en", "books"), ("vi", "vi/books")):
        path = os.path.join(root, sub, "read", SLUG, cslug, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        html = page(lang, cslug, ch_no, title_en, title_vi, byline, body_vi, body_en,
                    figs, extra_vi, extra_en)
        open(path, "w", encoding="utf-8").write(html)
        out.append(path)
    return out
