# -*- coding: utf-8 -*-
"""Shared markup and page shell for the Process Control / SIS reader pages.

Both books are normal-sized chapters, so unlike handbook Chapter 6 they get
one page each, built by `reader_pc.py` and `reader_sis.py`.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reader_book import BOOKS, footer, head, header   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOK = {
    "pc": {"spec": BOOKS["pc"], "base": "/books/read/pc-process-control/",
           "base_vi": "/vi/books/read/pc-process-control/"},
    "sis": {"spec": BOOKS["sis"],
            "base": "/books/read/safety-instrumented-systems-design-analysis-justification/",
            "base_vi": "/vi/books/read/safety-instrumented-systems-design-analysis-justification/"},
}

# chapter number -> published slug, for the previous/next chain
SLUGS = {
    "pc": {
        1: "ch01-introduction",
        2: "ch02-process-measurement-and-transducers",
        3: "ch03-basic-principles-of-control-valves-and-actuators",
        4: "ch04-fundamentals-of-control-systems",
        5: "ch05-stability-and-control-modes-of-closed-loops",
        6: "ch06-digital-control-principles",
        7: "ch07-real-and-ideal-pid-controllers",
        8: "ch08-tuning-of-pid-controllers",
        9: "ch09-output-modes-equations-and-cascade-control",
        10: "ch10-concepts-and-applications-of-feedforward-control",
        11: "ch11-combined-feedback-and-feedforward-control",
        12: "ch12-long-dead-time-and-the-smith-predictor",
        13: "ch13-basic-principles-of-fuzzy-logic-and-neural-networks",
        14: "ch14-self-tuning-intelligent-control-and-statistical-process-control",
    },
    "sis": {
        1: "ch01-introduction",
        2: "ch02-design-lifecycle",
        3: "ch03-process-control-vs-safety-control",
        4: "ch04-protection-layers",
        5: "ch05-developing-the-safety-requirement-specifications",
        6: "ch06-determining-the-safety-integrity-level",
        7: "ch07-choosing-a-technology",
        8: "ch08-initial-system-evaluation",
        9: "ch09-issues-relating-to-field-devices",
        10: "ch10-engineering-a-system",
        11: "ch11-installing-a-system",
    },
}


# ------------------------------------------------------------------ markup
def p(t):
    return "<p>%s</p>" % t


def lead(t):
    return '<p class="lead">%s</p>' % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h4(t):
    return "<h4>%s</h4>" % t


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def quote(text, src):
    return '<div class="pullquote"><p>%s</p><span class="src">%s</span></div>' % (text, src)


def ul(items, cls=""):
    c = (' class="%s"' % cls) if cls else ""
    return "<ul%s>%s</ul>" % (c, "".join("<li>%s</li>" % i for i in items))


def ol(items, start=1):
    st = (' start="%d"' % start) if start != 1 else ""
    return "<ol%s>%s</ol>" % (st, "".join("<li>%s</li>" % i for i in items))


def note(t):
    return '<div class="note">%s</div>' % t


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def table(header_row, rows, caption="", cls="tbl"):
    th = "".join("<th>%s</th>" % h for h in header_row)
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    cap = ('<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>' % caption) if caption else ""
    return ('<div class="table-wrap"><table class="%s"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>%s' % (cls, th, body, cap))


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


def keyterms(items, title_vi="Thuật ngữ chính của chương.",
             title_en="Key terms in this chapter."):
    """A one-line glossary box at the top of the page."""
    t = title_vi if _CUR_LANG[0] == "vi" else title_en
    body = " · ".join("<em>%s</em> — %s" % (k, v) for k, v in items)
    return '<div class="note"><b>%s</b> %s</div>' % (t, body)


_CUR_LANG = ["vi"]


# -------------------------------------------------------------------- nav
def nav(book, num, lang):
    vi = lang == "vi"
    spec = BOOK[book]["spec"]
    base = BOOK[book]["base_vi"] if vi else BOOK[book]["base"]
    slugs = SLUGS[book]
    titles = spec["chapters"]
    book_title = spec["title_vi"] if vi else spec["title_en"]

    prev_n = max([n for n in slugs if n < num], default=None)
    next_n = min([n for n in slugs if n > num], default=None)

    if prev_n is None:
        left = ('<a href="%s"><span class="k">%s</span>%s</a>'
                % (base, "← Mục lục sách" if vi else "← Book contents", book_title))
    else:
        left = ('<a href="%s%s/"><span class="k">%s</span>%s</a>'
                % (base, slugs[prev_n],
                   ("← Chương %d" if vi else "← Chapter %d") % prev_n,
                   titles[prev_n][1] if vi else titles[prev_n][0]))
    if next_n is None:
        right = ('<a href="%s" style="text-align:right;"><span class="k">%s</span>%s</a>'
                 % (base, "Mục lục →" if vi else "All chapters →", book_title))
    else:
        right = ('<a href="%s%s/" style="text-align:right;"><span class="k">%s</span>%s</a>'
                 % (base, slugs[next_n],
                    ("Chương %d →" if vi else "Chapter %d →") % next_n,
                    titles[next_n][1] if vi else titles[next_n][0]))
    return '<div class="chapter-nav">%s%s</div>' % (left, right)


# ------------------------------------------------------------------- page
def page(book, num, lang, body, figs, words, pages_src, byline, note_terms=""):
    """Assemble a whole chapter page and return the HTML string."""
    vi = lang == "vi"
    _CUR_LANG[0] = lang
    spec = BOOK[book]["spec"]
    slug = SLUGS[book][num]
    base = BOOK[book]["base_vi"] if vi else BOOK[book]["base"]
    other = BOOK[book]["base"] if vi else BOOK[book]["base_vi"]
    title_vi, title_en = spec["chapters"][num][1], spec["chapters"][num][0]
    title = title_vi if vi else title_en

    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">%s</a> · Chương %d'
             % (base, spec["title_vi"], num) if vi else
             '<a href="/books/">Books</a> · <a href="%s">%s</a> · Chapter %d'
             % (base, spec["title_en"], num))
    fig_vi = (" · %d hình" % figs) if figs else ""
    fig_en = (" · %d figures" % figs) if figs else ""
    meta = ("Chương %d · %d trang gốc · %s từ%s · bản dịch tiếng Việt"
            % (num, pages_src, "{:,}".format(words).replace(",", "."), fig_vi) if vi else
            "Chapter %d · %d source pages%s · companion notes"
            % (num, pages_src, fig_en))

    html_body = (
        '<main><article class="intranet-content reader">'
        '<div class="reader-hero">'
        '<div class="breadcrumb">%s</div>'
        '<h1>%s</h1>'
        '<p class="byline">%s</p>'
        '<div class="meta-line">%s</div>'
        '</div>'
        '<div class="prose">%s%s%s</div>'
        '</article></main>'
        % (crumb, title, byline, meta, note_terms, body, nav(book, num, lang)))

    desc = ("Bản dịch tiếng Việt Chương %d của %s." % (num, spec["title_vi"]) if vi else
            "Chapter %d of %s — figures redrawn, with commentary." % (num, spec["title_en"]))
    return (head(lang, "%s · %s" % (title, spec["title_vi"] if vi else spec["title_en"]), desc)
            + header(lang, other + slug + "/") + html_body + footer(lang, spec))


def write(book, num, lang, html):
    slug = SLUGS[book][num]
    pair = ("vi/books/read/%s/%s/index.html" if lang == "vi"
            else "books/read/%s/%s/index.html") % (BOOK[book]["spec"]["slug"], slug)
    path = os.path.join(ROOT, *pair.split("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(html)
    print("wrote %s  %d kB" % (os.path.relpath(path, ROOT), len(html) // 1024))


def build(book, num, modname):
    """Import one chapter module and write both language versions."""
    import importlib
    mod = importlib.import_module(modname)
    for lang in ("vi", "en"):
        body = mod.body_vi() if lang == "vi" else mod.body_en()
        figs = body.count('class="figure"')
        # count words of the prose only: the markup and the SVG would triple it
        text = re.sub(r"<[^>]+>", " ", body)
        words = len(text.split())
        html = page(book, num, lang, body, figs, words, mod.PAGES_SRC, mod.BYLINE,
                    mod.note_terms(lang))
        write(book, num, lang, html)
    return mod
