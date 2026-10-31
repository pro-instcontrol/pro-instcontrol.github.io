# -*- coding: utf-8 -*-
"""Shared helpers for the Chapter 6 section pages.

Chapter 6 of the handbook is 167 pages / 63k words, so it is published as one
page per section.  Each section module (hb06_sNN.py) exposes body_vi() and
body_en(); reader_hb_ch06.py assembles the pages.
"""
import os

from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
LANDING = "ch06-displacement-measurement"

# (number, slug, title VI, title EN)
SECTIONS = [
    (1, "ch06-1-resistive-displacement-sensors",
     "Cảm biến dịch chuyển điện trở", "Resistive Displacement Sensors"),
    (2, "ch06-2-inductive-displacement-sensors",
     "Cảm biến dịch chuyển cảm ứng", "Inductive Displacement Sensors"),
    (3, "ch06-3-capacitive-displacement-sensors",
     "Cảm biến điện dung", "Capacitive Sensors — Displacement"),
    (4, "ch06-4-piezoelectric-transducers",
     "Đầu đo và cảm biến áp điện", "Piezoelectric Transducers and Sensors"),
    (5, "ch06-5-laser-interferometer",
     "Cảm biến dịch chuyển giao thoa laser", "Laser Interferometer Displacement Sensors"),
    (6, "ch06-6-bore-gaging",
     "Cảm biến đo lỗ", "Bore Gaging Displacement Sensors"),
    (7, "ch06-7-time-of-flight-ultrasonic",
     "Cảm biến dịch chuyển siêu âm thời gian bay", "Time-of-Flight Ultrasonic Displacement Sensors"),
    (8, "ch06-8-optical-encoders",
     "Cảm biến quang học dạng mã hoá", "Optical Encoder Displacement Sensors"),
    (9, "ch06-9-magnetic-displacement-sensors",
     "Cảm biến dịch chuyển từ tính", "Magnetic Displacement Sensors"),
    (10, "ch06-10-synchro-resolver",
     "Cảm biến synchro và resolver", "Synchro/Resolver Displacement Sensors"),
    (11, "ch06-11-optical-fiber-displacement-sensors",
     "Cảm biến dịch chuyển sợi quang", "Optical Fiber Displacement Sensors"),
    (12, "ch06-12-optical-beam-deflection",
     "Cảm biến lệch chùm tia quang", "Optical Beam Deflection Sensing"),
]

SLUG_OF = {n: s for n, s, _vi, _en in SECTIONS}
TITLE_VI = {n: t for n, _s, t, _e in SECTIONS}
TITLE_EN = {n: t for n, _s, _t, t in SECTIONS}


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


def quote(text, src):
    return '<div class="pullquote"><p>%s</p><span class="src">%s</span></div>' % (text, src)


def ul(items, cls=""):
    c = (' class="%s"' % cls) if cls else ""
    return "<ul%s>%s</ul>" % (c, "".join("<li>%s</li>" % i for i in items))


def note(t):
    return '<div class="note">%s</div>' % t


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def fig(num, key, lang="vi"):
    """key is the 5-tuple returned by an hb06fig function."""
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-6-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


def table(header, rows, caption="", cls="tbl"):
    th = "".join("<th>%s</th>" % h for h in header)
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    cap = ('<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>' % caption) if caption else ""
    return ('<div class="table-wrap"><table class="%s"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>%s' % (cls, th, body, cap))


def nav(num, lang):
    """Prev / next across the twelve sections, falling back to the landing page."""
    vi = lang == "vi"
    base = BASE_VI if vi else BASE_EN
    prev_lab = ("← Mục %d" if vi else "← Section %d")
    next_lab = ("Mục %d →" if vi else "Section %d →")
    left = ('<a href="%s%s/"><span class="k">%s</span>%s</a>'
            % (base, LANDING, "← Chương 6" if vi else "← Chapter 6",
               "Dịch chuyển: đo tuyến tính và góc" if vi else "Displacement Measurement"))
    if num > 1:
        left = ('<a href="%s%s/"><span class="k">%s</span>%s</a>'
                % (base, SLUG_OF[num - 1], prev_lab % (num - 1), TITLE_VI[num - 1] if vi else TITLE_EN[num - 1]))
    if num < 12:
        right = ('<a href="%s%s/" style="text-align:right;"><span class="k">%s</span>%s</a>'
                 % (base, SLUG_OF[num + 1], next_lab % (num + 1),
                    TITLE_VI[num + 1] if vi else TITLE_EN[num + 1]))
    else:
        right = ('<a href="%s" style="text-align:right;"><span class="k">%s</span>%s</a>'
                 % (base, "Mục lục →" if vi else "All chapters →",
                    "Nội dung sách" if vi else "Book contents"))
    return '<div class="chapter-nav">%s%s</div>' % (left, right)


def page(num, lang, body, figs, words):
    """Wrap a section body in the shared reader shell."""
    vi = lang == "vi"
    slug = SLUG_OF[num]
    other = (BASE_EN if vi else BASE_VI) + slug + "/"
    title = ("Chương 6.%d — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % (num, TITLE_VI[num]) if vi
             else "Chapter 6.%d — %s · Measurement, Instrumentation and Sensors Handbook"
             % (num, TITLE_EN[num]))
    desc = ("Bản dịch tiếng Việt mục 6.%d “%s” của Sổ tay Đo lường, Thiết bị đo và Cảm biến (CRC Press, 1999)."
            % (num, TITLE_EN[num]) if vi else
            "Companion to section 6.%d of the CRC Measurement Handbook, with the full Vietnamese translation."
            % num)
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             '<a href="%s%s/">Chương 6</a> · Mục 6.%d' % (BASE_VI, BASE_VI, LANDING, num) if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             '<a href="%s%s/">Chapter 6</a> · Section 6.%d' % (BASE_EN, BASE_EN, LANDING, num))
    meta = ("Mục 6.%d · %d hình · khoảng %s từ" % (num, figs, format(words, ",d").replace(",", ".")) if vi
            else "Section 6.%d · %d figures · about %s words" % (num, figs, format(words, ",d")))
    html = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div></article></main>'
            % (crumb, TITLE_VI[num] if vi else TITLE_EN[num], BYLINE[num], meta, body))
    return head(lang, title, desc) + header(lang, other) + html + footer(lang)


BYLINE = {
    1: "Keith Antonelli, James Ko &amp; Shyan Ku · Kinetic Sciences Inc.",
    2: "Halit Eren · Curtin University of Technology",
    3: "Halit Eren &amp; Wei Ling Kong",
    4: "Ahmad Safari, Victor F. Janas, Amit Bandyopadhyay &amp; Andrei Kholkine · Rutgers University",
    5: "Bernhard Günther Zagar · Technical University Graz",
    6: "Viktor P. Astakhov · Concordia University",
    7: "Teklic Ole Pedersen &amp; Nils Karlsson · Linköpings Universitet",
    8: "J. R. René Mayer · École Polytechnique de Montréal",
    9: "David S. Nyce · MTS Systems Corp.",
    10: "Robert M. Hyatt, Jr. &amp; David Dayton · ILC Data Device Corp.",
    11: "Richard O. Claus, Vikram Bhatia &amp; Anbo Wang · Virginia Tech",
    12: "Grover C. Wetsel · University of Texas at Dallas",
}
