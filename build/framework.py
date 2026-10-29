# -*- coding: utf-8 -*-
"""Minimal static-site framework with paired EN/VI strings.

Every translatable leaf element carries data-i18n="<key>"; the paired strings
are serialised into the page as window.I18N and swapped client-side by
assets/app.js. No build step is needed at runtime - the output is plain HTML.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

_NEST_OPEN = re.compile(r"<(h[1-4]|p|li)([^>]*)><\1([^>]*)>")
_NEST_CLOSE = re.compile(r"</(h[1-4]|p|li)></\1>")


def tidy(html):
    """Collapse doubled block tags produced when a helper is used inside its own wrapper."""
    for _ in range(3):
        html = _NEST_OPEN.sub(r"<\1\3>", html)
        html = _NEST_CLOSE.sub(r"</\1>", html)
    return html

SITE_NAME_EN = "Instrumentation &amp; Control"
SITE_NAME_VI = "Đo lường &amp; Điều khiển"
TAG_EN = "Field Guide"
TAG_VI = "Sổ tay hiện trường"

NAV = [
    ("index.html", "Home", "Trang chủ"),
    ("fundamentals.html", "Fundamentals", "Cơ bản"),
    ("instruments.html", "Instruments", "Thiết bị đo"),
    ("control.html", "Control", "Điều khiển"),
    ("tools.html", "Tools", "Công cụ"),
    ("comparison.html", "Comparison", "So sánh"),
    ("geotechnical.html", "Geotech", "Địa kỹ thuật"),
    ("standards.html", "Standards", "Tiêu chuẩn"),
    ("glossary.html", "Glossary", "Thuật ngữ"),
]

SHELL = {
    "shell.skip": ("Skip to content", "Chuyển đến nội dung"),
    "shell.nav.home": ("Home", "Trang chủ"),
    "shell.nav.fundamentals": ("Fundamentals", "Cơ bản"),
    "shell.nav.instruments": ("Instruments", "Thiết bị đo"),
    "shell.nav.control": ("Control", "Điều khiển"),
    "shell.nav.tools": ("Tools", "Công cụ"),
    "shell.nav.comparison": ("Comparison", "So sánh"),
    "shell.nav.geotechnical": ("Geotech", "Địa kỹ thuật"),
    "shell.nav.standards": ("Standards", "Tiêu chuẩn"),
    "shell.nav.glossary": ("Glossary", "Thuật ngữ"),
    "shell.tag": (TAG_EN, TAG_VI),
    "shell.menu": ("Menu", "Danh mục"),
    "shell.foot.note": (
        "A bilingual field guide to process instrumentation and control. "
        "Content is synthesised from ISA, IEC, API and ISO 18674 practice; "
        "always verify against the current edition of a standard before design use.",
        "Sổ tay song ngữ về thiết bị đo và điều khiển quá trình. "
        "Nội dung được tổng hợp từ thực tiễn ISA, IEC, API và ISO 18674; "
        "luôn đối chiếu với bản tiêu chuẩn hiện hành trước khi dùng cho thiết kế.",
    ),
    "shell.foot.built": (
        "Static site · no build step · EN / VI",
        "Trang tĩnh · không cần build · EN / VI",
    ),
    "shell.foot.contact": ("Contact", "Liên hệ"),
}


def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


class Page:
    """Collects paired strings and emits markup in one language (EN default)."""

    def __init__(self, path, prefix, title_en, title_vi, desc_en, desc_vi):
        self.path = path
        self.prefix = prefix
        self.title = {"en": title_en, "vi": title_vi}
        self.desc = {"en": desc_en, "vi": desc_vi}
        self.strings = {}
        self.n = 0

    def key(self):
        self.n += 1
        return "%s.%d" % (self.prefix, self.n)

    def el(self, tag, en, vi, cls="", attrs="", key=None):
        k = key or self.key()
        self.strings[k] = {"en": en, "vi": vi}
        c = ' class="%s"' % cls if cls else ""
        return '<%s%s%s data-i18n="%s">%s</%s>' % (tag, c, attrs, k, en, tag)

    # convenience wrappers -------------------------------------------------
    def p(self, en, vi, cls=""):
        return self.el("p", en, vi, cls)

    def h1(self, en, vi, cls=""):
        return self.el("h1", en, vi, cls)

    def h2(self, en, vi, cls=""):
        return self.el("h2", en, vi, cls)

    def h3(self, en, vi, cls=""):
        return self.el("h3", en, vi, cls)

    def li(self, en, vi, cls=""):
        return self.el("li", en, vi, cls)

    def span(self, en, vi, cls=""):
        return self.el("span", en, vi, cls)

    def div(self, en, vi, cls=""):
        return self.el("div", en, vi, cls)

    def td(self, en, vi, cls=""):
        # inner content only - the surrounding <td>/<dt> is written by the template
        return self.el("span", en, vi, cls)

    def th(self, en, vi, cls=""):
        # inner content only - the surrounding <th> is written by the template
        return self.el("span", en, vi, cls)

    def a(self, href, en, vi, cls="", attrs=""):
        k = self.key()
        self.strings[k] = {"en": en, "vi": vi}
        c = ' class="%s"' % cls if cls else ""
        return '<a href="%s"%s%s data-i18n="%s">%s</a>' % (href, c, attrs, k, en)


def eyebrow(pg, num, en, vi):
    return (
        '<div class="eyebrow"><span class="num">%s</span>'
        '<span class="line"></span>%s</div>'
        % (num, pg.span(en, vi, "eyebrow-label"))
    )


def section_open(num, en, vi, pg, sid=""):
    sid_attr = ' id="%s"' % sid if sid else ""
    return (
        '<section class="sec"%s><div class="wrap">%s'
        % (sid_attr, eyebrow(pg, num, en, vi))
    )


def section_close():
    return "</div></section>"


def page_intro(pg, title_en, title_vi, lede_en, lede_vi, toc=None):
    """Page header: title + lede on the left, section index on the right."""
    left = '<div class="intro-l">%s%s</div>' % (
        pg.h1(title_en, title_vi),
        pg.p(lede_en, lede_vi, "lede"),
    )
    right = ""
    if toc:
        items = "".join(
            '<li><a href="#%s">%s</a></li>' % (anchor, pg.span(en, vi))
            for anchor, en, vi in toc
        )
        right = (
            '<aside class="toc"><span class="toc-h">%s</span><ol>%s</ol></aside>'
            % (pg.span("On this page", "Trong trang này"), items)
        )
    return (
        '<section class="sec intro"><div class="wrap intro-grid">%s%s</div></section>'
        % (left, right)
    )


def head(pg, extra_head=""):
    css_ver = os.environ.get("ASSET_VER", "1")
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v=%(ver)s">
%(extra)s
</head>
<body>
<a class="skip" href="#main" data-i18n="shell.skip">%(skip)s</a>
""" % {
        "title": pg.title["en"],
        "desc": pg.desc["en"],
        "ver": css_ver,
        "extra": extra_head,
        "skip": SHELL["shell.skip"][0],
    }


def topbar(active):
    items = []
    for href, en, _vi in NAV:
        cls = "nav-link active" if href == active else "nav-link"
        items.append(
            '<a class="%s" href="%s" data-i18n="shell.nav.%s">%s</a>'
            % (cls, href, href.replace(".html", "").replace("index", "home"), en)
        )
    nav_html = "\n      ".join(items)
    return """<header class="topbar">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="Home">
      <span class="mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="30" height="30" fill="none">
          <rect x="1" y="1" width="30" height="30" rx="8" stroke="currentColor" stroke-width="1.5" opacity=".35"/>
          <path d="M7 22h6l3-12 3 12h6" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
          <circle cx="16" cy="10" r="2.2" fill="currentColor"/>
        </svg>
      </span>
      <span class="brand-txt"><strong>%s</strong><em data-i18n="shell.tag">%s</em></span>
    </a>
    <nav class="nav" id="nav">
      %s
    </nav>
    <div class="bar-right">
      <button class="lang" id="lang" type="button" aria-label="Switch language">
        <span class="lang-opt on">EN</span><span class="lang-sep">/</span><span class="lang-opt">VI</span>
      </button>
      <button class="burger" id="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav">
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>
<main id="main">
""" % (SITE_NAME_EN, SHELL["shell.tag"][0], nav_html)


def footer():
    return """</main>
<footer class="foot">
  <div class="wrap foot-in">
    <div class="foot-l">
      <span class="brand-mini">%s</span>
      <p data-i18n="shell.foot.note">%s</p>
    </div>
    <div class="foot-r">
      <span class="mono" data-i18n="shell.foot.built">%s</span>
      <a class="mono" href="https://github.com/pro-instcontrol" rel="noopener">github.com/pro-instcontrol</a>
    </div>
  </div>
</footer>
""" % (SITE_NAME_EN, SHELL["shell.foot.note"][0], SHELL["shell.foot.built"][0])


def render(pg, body, active):
    strings = {k: {"en": v[0], "vi": v[1]} for k, v in SHELL.items()}
    strings.update(pg.strings)
    payload = json.dumps(strings, ensure_ascii=False, separators=(",", ":"))
    meta = json.dumps(
        {"title": pg.title, "desc": pg.desc}, ensure_ascii=False, separators=(",", ":")
    )
    out = head(pg)
    out += topbar(active)
    out += body
    out += footer()
    out += "<script>window.I18N=%s;window.I18N_META=%s;</script>\n" % (payload, meta)
    out += '<script src="assets/app.js?v=%s"></script>\n</body>\n</html>\n' % os.environ.get(
        "ASSET_VER", "1"
    )
    return tidy(out)


def write(path, content):
    os.makedirs(DIST, exist_ok=True)
    full = os.path.join(DIST, path)
    os.makedirs(os.path.dirname(full), exist_ok=True) if os.path.dirname(full) else None
    with open(full, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
    return full
