# -*- coding: utf-8 -*-
"""Video library — generated EN page at /video-library/ and VI page at /vi/video-library/.

Both pages are static: every card is written at build time so the library works
without JavaScript. assets/videos.js only adds search, level and source filters.
"""

import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import framework  # noqa: E402
import videos_data  # noqa: E402

SITE = "Instrumentation &amp; Control"
SITE_VI = "Đo lường &amp; Điều khiển"

NAV = [
    ("index.html", "Home", "Trang chủ"),
    ("books/", "Books", "Sách"),
    ("video-library/", "Videos", "Video"),
    ("fundamentals.html", "Fundamentals", "Cơ bản"),
    ("instruments.html", "Instruments", "Thiết bị đo"),
    ("install.html", "Install", "Lắp đặt"),
    ("control.html", "Control", "Điều khiển"),
    ("applications.html", "Applications", "Ứng dụng"),
    ("safety.html", "Safety", "An toàn"),
    ("tools.html", "Tools", "Công cụ"),
    ("comparison.html", "Comparison", "So sánh"),
    ("geotechnical.html", "Geotech", "Địa kỹ thuật"),
    ("standards.html", "Standards", "Tiêu chuẩn"),
    ("glossary.html", "Glossary", "Thuật ngữ"),
    ("education.html", "Education", "Giáo dục"),
]

LEVEL = {
    "en": {"B": "Beginner", "I": "Intermediate", "A": "Advanced"},
    "vi": {"B": "Cơ bản", "I": "Trung cấp", "A": "Nâng cao"},
}

T = {
    "en": {
        "title": "Video library — process instrumentation &amp; control",
        "desc": "A curated, classified video library for process instrumentation and control: "
                "%d videos across %d topics, from a supplied Instrumentation & Control playlist, "
                "@InstruNexus, manufacturer channels and Vietnamese-language sources.",
        "skip": "Skip to content",
        "kicker": "Video library",
        "h1": "Process instrumentation &amp; control, on video",
        "h1b": "A library that is indexed, not dumped",
        "lede": "Every clip here was picked for one topic, classified once, and given a one-line note "
                "on why it earns its place. Start with the supplied Instrumentation &amp; Control playlist "
                "and the @InstruNexus channel, then use the manufacturer and Vietnamese-language "
                "sources to close the gaps those two leave.",
        "stat_videos": "videos",
        "stat_topics": "topics",
        "stat_hours": "hours of material",
        "stat_src": "source channels",
        "search": "Search a title or a note…",
        "all": "All",
        "all_src": "All sources",
        "count": "%d of %d videos",
        "empty": "Nothing matches that filter. Clear the search and try again.",
        "top": "Back to top",
        "note": "Links open on YouTube in a new tab. Videos remain the property of their creators; "
                "the notes here are editorial, and a link is not an endorsement of every claim in a clip.",
        "prov_h": "Where these come from",
        "prov_p": "Two supplied sources carry most of the load — the Instrumentation &amp; Control "
                  "playlist and the InstruNexus channel — and the rest fill the topics they do not cover.",
        "prov_a": "Playlist: Instrumentation &amp; Control",
        "prov_b": "@InstruNexus channel",
        "prov_c": "Manufacturers &amp; standards bodies",
        "prov_d": "Vietnamese-language channels",
        "prov_m": "RealPars, Endress+Hauser, Fluke, Rosemount, Fisher, SAMSON, Siemens, ABB, DwyerOmega, "
                  "Kimray, Phoenix Contact, Precision Digital, exida, TÜV Rheinland, ISA, Hazcon, eFIXX, "
                  "Lesman, Lakeside Process Controls, The Engineering Mindset, Brian Douglas, BCIT.",
        "prov_v": "Học Nghề Kỹ Sư Điện &amp; Điện Tử, Tâm Lửa, P&amp;ID Oil and Gas, NK Engineering.",
        "lang_other": "VI",
        "lang_href": "../vi/video-library/",
        "nav_active": "Videos",
        "level_lbl": "Level",
        "src_lbl": "Source",
        "foot_note": "A bilingual field guide to process instrumentation and control. "
                     "Content is synthesised from ISA, IEC, API and ISO 18674 practice; "
                     "always verify against the current edition of a standard before design use.",
        "foot_built": "Static site · no build step · EN / VI",
    },
    "vi": {
        "title": "Thư viện video — đo lường &amp; điều khiển quá trình",
        "desc": "Thư viện video có tuyển chọn và phân loại cho ngành đo lường – điều khiển quá trình: "
                "%d video thuộc %d chủ đề, từ playlist Instrumentation & Control, kênh @InstruNexus, "
                "kênh của các hãng và nguồn tiếng Việt.",
        "skip": "Chuyển đến nội dung",
        "kicker": "Thư viện video",
        "h1": "Đo lường &amp; điều khiển quá trình, qua video",
        "h1b": "Thư viện được phân loại, không phải danh sách dán",
        "lede": "Mỗi video ở đây được chọn cho một chủ đề, phân loại một lần và ghi chú một dòng vì sao "
                "nó đáng xem. Bắt đầu với playlist Instrumentation &amp; Control và kênh @InstruNexus, "
                "rồi dùng nguồn của các hãng và nguồn tiếng Việt để lấp những chỗ hai nguồn kia bỏ trống.",
        "stat_videos": "video",
        "stat_topics": "chủ đề",
        "stat_hours": "giờ nội dung",
        "stat_src": "kênh nguồn",
        "search": "Tìm theo tiêu đề hoặc ghi chú…",
        "all": "Tất cả",
        "all_src": "Tất cả nguồn",
        "count": "%d trên %d video",
        "empty": "Không có video nào khớp bộ lọc. Hãy xoá từ khoá và thử lại.",
        "top": "Lên đầu trang",
        "note": "Liên kết mở trên YouTube ở tab mới. Video thuộc quyền tác giả của người tạo; "
                "phần ghi chú ở đây là ý kiến biên tập, và một liên kết không có nghĩa là bảo chứng "
                "cho mọi khẳng định trong video.",
        "prov_h": "Nguồn của thư viện",
        "prov_p": "Hai nguồn được cung cấp chiếm phần lớn nội dung — playlist Instrumentation &amp; Control "
                  "và kênh InstruNexus — phần còn lại lấp những chủ đề hai nguồn này chưa có.",
        "prov_a": "Playlist: Instrumentation &amp; Control",
        "prov_b": "Kênh @InstruNexus",
        "prov_c": "Hãng sản xuất &amp; tổ chức tiêu chuẩn",
        "prov_d": "Kênh tiếng Việt",
        "prov_m": "RealPars, Endress+Hauser, Fluke, Rosemount, Fisher, SAMSON, Siemens, ABB, DwyerOmega, "
                  "Kimray, Phoenix Contact, Precision Digital, exida, TÜV Rheinland, ISA, Hazcon, eFIXX, "
                  "Lesman, Lakeside Process Controls, The Engineering Mindset, Brian Douglas, BCIT.",
        "prov_v": "Học Nghề Kỹ Sư Điện &amp; Điện Tử, Tâm Lửa, P&amp;ID Oil and Gas, NK Engineering.",
        "lang_other": "EN",
        "lang_href": "../../video-library/",
        "nav_active": "Video",
        "level_lbl": "Mức",
        "src_lbl": "Nguồn",
        "foot_note": "Sổ tay song ngữ về thiết bị đo và điều khiển quá trình. "
                     "Nội dung được tổng hợp từ thực tiễn ISA, IEC, API và ISO 18674; "
                     "luôn đối chiếu với bản tiêu chuẩn hiện hành trước khi dùng cho thiết kế.",
        "foot_built": "Trang tĩnh · không cần build · EN / VI",
    },
}

YT = "https://www.youtube.com/watch?v="


def seconds(dur):
    parts = [int(p) for p in dur.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def head(lang, prefix, n_videos, n_cats):
    t = T[lang]
    css = prefix + "assets/style.css?v=2"
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="%(prefix)sassets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%(css)s">
</head>
<body>
<a class="skip" href="#main">%(skip)s</a>
""" % {
        "lang": lang,
        "title": t["title"],
        "desc": t["desc"] % (n_videos, n_cats),
        "prefix": prefix,
        "css": css,
        "skip": t["skip"],
    }


def topbar(lang, prefix):
    t = T[lang]
    items = []
    for href, en, vi in NAV:
        label = en if lang == "en" else vi
        active = href == "video-library/"
        cls = "nav-link active" if active else "nav-link"
        items.append('<a class="%s" href="%s%s">%s</a>' % (cls, prefix, href, label))
    nav_html = "\n      ".join(items)
    brand = SITE if lang == "en" else SITE_VI
    tag = "Field Guide" if lang == "en" else "Sổ tay hiện trường"
    return """<header class="topbar">
  <div class="wrap bar">
    <a class="brand" href="%(prefix)sindex.html" aria-label="Home">
      <span class="mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="30" height="30" fill="none">
          <rect x="1" y="1" width="30" height="30" rx="8" stroke="currentColor" stroke-width="1.5" opacity=".35"/>
          <path d="M7 22h6l3-12 3 12h6" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
          <circle cx="16" cy="10" r="2.2" fill="currentColor"/>
        </svg>
      </span>
      <span class="brand-txt"><strong>%(brand)s</strong><em>%(tag)s</em></span>
    </a>
    <nav class="nav" id="nav">
      %(nav)s
    </nav>
    <div class="bar-right">
      <a class="lang" href="%(other)s" aria-label="Switch language">
        <span class="lang-opt on">%(cur)s</span><span class="lang-sep">/</span><span class="lang-opt">%(oth)s</span>
      </a>
      <button class="burger" id="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav">
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>
<main id="main">
""" % {
        "prefix": prefix,
        "brand": brand,
        "tag": tag,
        "nav": nav_html,
        "other": t["lang_href"],
        "cur": "EN" if lang == "en" else "VI",
        "oth": t["lang_other"],
    }


def hero(lang, n_videos, n_cats, hours, n_src):
    t = T[lang]
    return """<section class="vid-hero" id="top">
  <div class="wrap">
    <span class="kicker"><span class="dot"></span>%s</span>
    <h1>%s<span class="thin">%s</span></h1>
    <p class="lede wide">%s</p>
    <div class="vid-stats">
      <div><b>%d</b><span>%s</span></div>
      <div><b>%d</b><span>%s</span></div>
      <div><b>%d</b><span>%s</span></div>
      <div><b>%d</b><span>%s</span></div>
    </div>
  </div>
</section>
""" % (t["kicker"], t["h1"], t["h1b"], t["lede"], n_videos, t["stat_videos"], n_cats, t["stat_topics"],
       hours, t["stat_hours"], n_src, t["stat_src"])


def tools(lang, sources):
    t = T[lang]
    opts = "".join('<option value="%s">%s</option>' % (html.escape(s), html.escape(s)) for s in sources)
    return """<div class="vid-tools" id="tools">
  <div class="wrap">
    <div class="vid-tools-row">
      <label class="searchbar vid-search" for="vsearch">
        <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="8.5" cy="8.5" r="5.5"/><path d="M13 13l4 4"/></svg>
        <input id="vsearch" type="search" placeholder="%s" autocomplete="off" aria-label="%s">
      </label>
      <div class="pills vid-levels" role="group" aria-label="%s">
        <button class="pill on" type="button" data-level="all">%s</button>
        <button class="pill" type="button" data-level="B">%s</button>
        <button class="pill" type="button" data-level="I">%s</button>
        <button class="pill" type="button" data-level="A">%s</button>
      </div>
      <label class="vid-select" for="vsrc">
        <span>%s</span>
        <select id="vsrc"><option value="all">%s</option>%s</select>
      </label>
      <span class="count" id="vcount" data-tpl="%s"></span>
    </div>
    <nav class="vchips" id="vchips" aria-label="%s">%s</nav>
  </div>
</div>
""" % (
        t["search"], t["search"], t["level_lbl"], t["all"],
        LEVEL[lang]["B"], LEVEL[lang]["I"], LEVEL[lang]["A"],
        t["src_lbl"], t["all_src"], opts, t["count"], t["kicker"], "".join(
            '<a class="vchip" href="#cat-%s"><span>%s</span>%s<em>%d</em></a>'
            % (cid, emo, name, count)
            for cid, emo, name, count in _chip_data(lang)
        ),
    )


_CHIPS = []


def _chip_data(lang):
    return _CHIPS


def card(lang, v):
    vid, cat, lvl, dur, src, title, note_en, note_vi = v
    note = note_en if lang == "en" else note_vi
    url = YT + vid
    t = html.escape(title)
    return """<article class="vcard" data-cat="%s" data-level="%s" data-src="%s" data-q="%s">
  <a class="vthumb" href="%s" target="_blank" rel="noopener" aria-label="%s">
    <img src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="" loading="lazy" width="480" height="270">
    <span class="vplay" aria-hidden="true"><svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M8 5.5v13l11-6.5z"/></svg></span>
    <span class="vdur">%s</span>
  </a>
  <div class="vbody">
    <div class="vmeta"><span class="vsrc">%s</span><span class="vlev lvl-%s">%s</span></div>
    <h4 class="vtitle"><a href="%s" target="_blank" rel="noopener">%s</a></h4>
    <p class="vnote">%s</p>
  </div>
</article>
""" % (
        cat, lvl, html.escape(src), html.escape((title + " " + note).lower()),
        url, t, vid, dur, html.escape(src), lvl, LEVEL[lang][lvl],
        url, t, html.escape(note),
    )


def sections(lang, by_cat):
    t = T[lang]
    out = []
    for cid, emo, en, vi, de, dv in videos_data.CATS:
        items = by_cat[cid]
        name = en if lang == "en" else vi
        desc = de if lang == "en" else dv
        cards = "".join(card(lang, v) for v in items)
        out.append("""<section class="vid-sec" id="cat-%s">
  <div class="vid-sec-head">
    <h2><span class="vemoji" aria-hidden="true">%s</span>%s<span class="vcount">%d</span></h2>
    <p>%s</p>
    <a class="totop" href="#top">↑ %s</a>
  </div>
  <div class="vgrid">%s</div>
</section>
""" % (cid, emo, html.escape(name), len(items), html.escape(desc), t["top"], cards))
    return "".join(out)


def provenance(lang):
    t = T[lang]
    return """<section class="vid-prov">
  <h2>%s</h2>
  <p>%s</p>
  <dl class="vid-prov-list">
    <div><dt>%s</dt><dd><a href="https://www.youtube.com/playlist?list=PLhJQWRdDvATi97j2VmTYNA_iVf3h2P6fF" target="_blank" rel="noopener">playlist</a> · <a href="https://www.youtube.com/watch?v=UbJ0ZBk2NM8" target="_blank" rel="noopener">BCIT program overview</a></dd></div>
    <div><dt>%s</dt><dd><a href="https://www.youtube.com/@InstruNexus" target="_blank" rel="noopener">youtube.com/@InstruNexus</a></dd></div>
    <div><dt>%s</dt><dd>%s</dd></div>
    <div><dt>%s</dt><dd>%s</dd></div>
  </dl>
  <p class="vid-disclaim">%s</p>
</section>
""" % (t["prov_h"], t["prov_p"], t["prov_a"], t["prov_b"], t["prov_c"], t["prov_m"],
       t["prov_d"], t["prov_v"], t["note"])


def footer(lang, prefix):
    t = T[lang]
    brand = SITE if lang == "en" else SITE_VI
    return """</main>
<footer class="foot">
  <div class="wrap foot-in">
    <div class="foot-l">
      <span class="brand-mini">%s</span>
      <p>%s</p>
    </div>
    <div class="foot-r">
      <span class="mono">%s</span>
      <a class="mono" href="https://github.com/pro-instcontrol" rel="noopener">github.com/pro-instcontrol</a>
    </div>
  </div>
</footer>
<script src="%sassets/videos.js?v=1" defer></script>
</body>
</html>
""" % (brand, t["foot_note"], t["foot_built"], prefix)


def build_lang(lang, path, prefix):
    t = T[lang]
    by_cat = {c[0]: [] for c in videos_data.CATS}
    for v in videos_data.VIDEOS:
        by_cat[v[1]].append(v)

    global _CHIPS
    _CHIPS[:] = [
        (c[0], c[1], (c[2] if lang == "en" else c[3]), len(by_cat[c[0]]))
        for c in videos_data.CATS
    ]

    n_videos = len(videos_data.VIDEOS)
    n_cats = len([c for c in videos_data.CATS if by_cat[c[0]]])
    total_s = sum(seconds(v[3]) for v in videos_data.VIDEOS)
    hours = int(round(total_s / 3600.0))
    sources = sorted({v[4] for v in videos_data.VIDEOS}, key=lambda s: s.lower())

    body = head(lang, prefix, n_videos, n_cats)
    body += topbar(lang, prefix)
    body += hero(lang, n_videos, n_cats, hours, len(sources))
    body += tools(lang, sources)
    body += '<div class="wrap vid-body">'
    body += sections(lang, by_cat)
    body += '<p class="vempty" id="vempty" hidden>%s</p>' % html.escape(t["empty"])
    body += provenance(lang)
    body += "</div>"
    body += footer(lang, prefix)
    return framework.write(path, body)


def main():
    a = build_lang("en", "video-library/index.html", "../")
    b = build_lang("vi", "vi/video-library/index.html", "../../")
    print("  video-library/index.html      %.1f kB" % (os.path.getsize(a) / 1024))
    print("  vi/video-library/index.html   %.1f kB" % (os.path.getsize(b) / 1024))


if __name__ == "__main__":
    main()
