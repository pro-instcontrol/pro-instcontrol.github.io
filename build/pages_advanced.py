# -*- coding: utf-8 -*-
"""Advanced practice — generated EN page at /advanced/ and VI page at /vi/advanced/.

Two real URLs rather than a client-side toggle, matching the video library: the
Vietnamese page is Vietnamese in the HTML, so it is indexable and reads correctly
with JavaScript off. The language switch is therefore a plain link between the
two directories.
"""

import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import framework  # noqa: E402

BASE = "https://pro-instcontrol.github.io"
TWIN_PATHS = {"video-library/", "books/", "advanced/"}
SITE = "Instrumentation &amp; Control"
SITE_VI = "Đo lường &amp; Điều khiển"

T = {
    "en": {
        "title": "Advanced practice — beyond the single loop | I&amp;C",
        "desc": "The layer above single-loop instrumentation: cascade and model predictive control, "
                "safety cases with numbers, and the field-connectivity standards being rewritten now.",
        "skip": "Skip to content",
        "kicker": "Advanced practice",
        "h1": "Where the fundamentals stop being enough",
        "lede": "Every other page here teaches one loop, one instrument, one drawing. This is the layer "
                "above: strategies that need more than one loop, safety cases that need numbers, and "
                "the connectivity standards that are being rewritten while you read this.",
        "toc": "On this page",
        "eb_1": "Standards watch",
        "eb_2": "Control strategy",
        "eb_3": "Safety case",
        "lang_other": "VI",
        "lang_href": "../vi/advanced/",
        "nav_active": "advanced/",
        "trends_h": "Trends &amp; standards watch",
        "trends_p": "Twelve videos on where field connectivity is actually heading. The short version: "
                    "Ethernet-APL standardised the wire, not the protocol. HART-IP, PROFINET, EtherNet/IP "
                    "and OPC UA FX now share one two-wire cable to the same devices. FOUNDATION Fieldbus "
                    "did not lose to a rival protocol — it lost to the layer underneath it.",
        "card_k": "Video library · 12 videos",
        "card_t": "Open the Trends &amp; standards watch section",
        "card_d": "Ethernet-APL, HART-IP, OPC UA FX, NOA, MTP, OT security, digital twin",
        "card_arrow": "Go to the videos",
        "video_href": "../video-library/#cat-trends",
        "themes": [
            ("Ethernet-APL",
             "10BASE-T1L over two wires: 10 Mbit/s, 1 km trunk, power on the same pair, Ex zone 0/1/2 "
             "with 2-WISE. It replaces the physical layer, nothing above it."),
            ("HART-IP",
             "The cheapest migration for most plants: the same HART devices and workflows, Ethernet "
             "transport instead of a 4–20 mA loop."),
            ("OPC UA FX",
             "Controller-to-controller exchange with a standard data model. The multi-vendor bench demos "
             "matter more than the specification text."),
            ("NOA and MTP",
             "The second channel for monitoring without touching the control network, and modular skids "
             "that integrate without custom engineering."),
            ("OT security",
             "IEC 62443 has moved from a project afterthought to a procurement gate. Segmentation "
             "vocabulary is now expected of instrument engineers."),
            ("Digital twin",
             "Useful where the model is honest about its steady-state assumptions, and quietly wrong "
             "where it is not."),
        ],
        "beyond_h": "Beyond the single loop",
        "beyond_p": "Cascade, feedforward, ratio and model predictive control: what each one buys, what "
                    "it costs to maintain, and why dead time decides whether any of them can help you. "
                    "The control page carries the full treatment, including tuning methods compared "
                    "and the dead-time problem that dominates everything else.",
        "beyond_a": "Control &amp; tuning — the advanced section",
        "paper_h": "Safety cases and the paper trail",
        "paper_p": "The documents that decide whether a plant is allowed to run: LOPA to justify the "
                   "layer, an SRS to specify it, SIL verification to prove it, a cause &amp; effect "
                   "matrix to wire it, and an alarm rationalisation to keep it usable at three in "
                   "the morning.",
        "paper_a": "Functional safety &amp; SIS",
        "paper_b": "Standards reference",
        "foot_note": "A bilingual field guide to process instrumentation and control. "
                     "Content is synthesised from ISA, IEC, API and ISO 18674 practice; "
                     "always verify against the current edition of a standard before design use.",
        "foot_built": "Static site · no build step · EN / VI",
    },
    "vi": {
        "title": "Thực hành nâng cao — vượt ra ngoài một vòng | I&amp;C",
        "desc": "Tầng phía trên của đo lường điều khiển một vòng: điều khiển cascade và dự báo mô hình, "
                "hồ sơ an toàn có con số, và các tiêu chuẩn kết nối hiện trường đang được viết lại.",
        "skip": "Chuyển đến nội dung",
        "kicker": "Thực hành nâng cao",
        "h1": "Nơi kiến thức cơ bản không còn đủ",
        "lede": "Mọi trang khác ở đây dạy một vòng điều khiển, một thiết bị, một bản vẽ. Đây là tầng "
                "phía trên: những chiến lược cần nhiều hơn một vòng, hồ sơ an toàn cần con số, và "
                "những tiêu chuẩn kết nối đang được viết lại ngay lúc này.",
        "toc": "Trong trang này",
        "eb_1": "Theo dõi tiêu chuẩn",
        "eb_2": "Chiến lược điều khiển",
        "eb_3": "Hồ sơ an toàn",
        "lang_other": "EN",
        "lang_href": "../../advanced/",
        "nav_active": "advanced/",
        "trends_h": "Xu hướng &amp; theo dõi tiêu chuẩn",
        "trends_p": "Mười hai video về hướng phát triển thực sự của kết nối hiện trường. Bản ngắn: "
                    "Ethernet-APL chuẩn hoá đường dây, không chuẩn hoá giao thức. HART-IP, PROFINET, "
                    "EtherNet/IP và OPC UA FX nay dùng chung một đôi dây tới cùng thiết bị. "
                    "FOUNDATION Fieldbus không thua một giao thức đối thủ — nó thua tầng bên dưới.",
        "card_k": "Thư viện video · 12 video",
        "card_t": "Mở mục Xu hướng &amp; theo dõi tiêu chuẩn",
        "card_d": "Ethernet-APL, HART-IP, OPC UA FX, NOA, MTP, an ninh OT, digital twin",
        "card_arrow": "Đến phần video",
        "video_href": "../../vi/video-library/#cat-trends",
        "themes": [
            ("Ethernet-APL",
             "10BASE-T1L trên hai dây: 10 Mbit/s, trục dài 1 km, cấp nguồn cùng đôi dây, vùng Ex 0/1/2 "
             "với 2-WISE. Nó thay lớp vật lý, không thay gì ở phía trên."),
            ("HART-IP",
             "Đường chuyển đổi rẻ nhất với phần lớn nhà máy: vẫn thiết bị và quy trình HART cũ, "
             "chỉ đổi sang đường truyền Ethernet thay vì vòng 4–20 mA."),
            ("OPC UA FX",
             "Trao đổi controller-với-controller theo mô hình dữ liệu chuẩn. Các demo đa hãng trên "
             "bàn thử có sức nặng hơn phần chữ của đặc tả."),
            ("NOA và MTP",
             "Kênh thứ hai để giám sát mà không đụng mạng điều khiển, và các skid mô-đun tích hợp "
             "được mà không cần lập trình riêng."),
            ("An ninh OT",
             "IEC 62443 đã từ việc làm sau cùng thành điều kiện mua sắm. Vốn từ về phân vùng nay "
             "được coi là chuẩn mực của kỹ sư đo lường."),
            ("Digital twin",
             "Hữu ích khi mô hình trung thực về giả thiết trạng thái ổn định, và âm thầm sai ở chỗ nó "
             "không trung thực."),
        ],
        "beyond_h": "Vượt ra ngoài một vòng",
        "beyond_p": "Cascade, feedforward, điều khiển tỉ lệ và điều khiển dự báo mô hình: mỗi thứ mua "
                    "được gì, tốn gì để duy trì, và vì sao thời gian trễ quyết định chúng có giúp được "
                    "hay không. Trang điều khiển trình bày đầy đủ, gồm so sánh các phương pháp hiệu "
                    "chỉnh và bài toán thời gian trễ chi phối mọi thứ còn lại.",
        "beyond_a": "Điều khiển &amp; hiệu chỉnh — phần nâng cao",
        "paper_h": "Hồ sơ an toàn và giấy tờ",
        "paper_p": "Những tài liệu quyết định nhà máy có được phép chạy hay không: LOPA để biện minh "
                   "cho lớp bảo vệ, SRS để đặc tả, kiểm chứng SIL để chứng minh, ma trận nguyên nhân "
                   "&amp; kết quả để đấu dây, và rà soát báo động để hệ thống còn dùng được lúc ba "
                   "giờ sáng.",
        "paper_a": "An toàn chức năng &amp; SIS",
        "paper_b": "Tham chiếu tiêu chuẩn",
        "foot_note": "Sổ tay song ngữ về thiết bị đo và điều khiển quá trình. "
                     "Nội dung được tổng hợp từ thực tiễn ISA, IEC, API và ISO 18674; "
                     "luôn đối chiếu với bản tiêu chuẩn hiện hành trước khi dùng cho thiết kế.",
        "foot_built": "Trang tĩnh · không cần build · EN / VI",
    },
}


def page_url(lang):
    return BASE + ("/vi/advanced/" if lang == "vi" else "/advanced/")


def head(lang, prefix):
    t = T[lang]
    css = prefix + "assets/style.css?v=5"
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": page_url(lang) + "#page",
                "url": page_url(lang),
                "name": html.unescape(t["title"]),
                "description": html.unescape(t["desc"]),
                "inLanguage": "vi-VN" if lang == "vi" else "en",
                "isPartOf": {"@type": "WebSite", "name": "Instrumentation & Control",
                             "url": BASE + "/"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Instrumentation & Control",
                     "item": BASE + "/"},
                    {"@type": "ListItem", "position": 2,
                     "name": "Advanced practice" if lang == "en" else "Thực hành nâng cao",
                     "item": page_url(lang)},
                ],
            },
        ],
    }
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canon)s">
<link rel="alternate" hreflang="en" href="%(base)s/advanced/">
<link rel="alternate" hreflang="vi" href="%(base)s/vi/advanced/">
<link rel="alternate" hreflang="x-default" href="%(base)s/advanced/">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Instrumentation &amp; Control">
<meta property="og:locale" content="%(locale)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="%(prefix)sassets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%(css)s">
<script type="application/ld+json">%(ld)s</script>
</head>
<body>
<a class="skip" href="#main">%(skip)s</a>
""" % {
        "lang": "vi" if lang == "vi" else "en",
        "title": t["title"],
        "desc": html.escape(html.unescape(t["desc"]), quote=True),
        "canon": page_url(lang),
        "base": BASE,
        "locale": "vi_VN" if lang == "vi" else "en_US",
        "prefix": prefix,
        "css": css,
        "ld": json.dumps(ld, ensure_ascii=False, separators=(",", ":")),
        "skip": t["skip"],
    }


def topbar(lang, prefix):
    t = T[lang]
    active = t["nav_active"]
    items = []
    for href, en, vi in framework.NAV:
        label = en if lang == "en" else vi
        cls = "nav-link active" if href == active else "nav-link"
        base = prefix + ("vi/" if lang == "vi" and href in TWIN_PATHS else "")
        items.append('<a class="%s" href="%s%s">%s</a>' % (cls, base, href, label))
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


def hero(lang):
    t = T[lang]
    return """<section class="sec adv-hero">
  <div class="wrap">
    <div class="eyebrow"><span class="num">00</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h1 class="adv-h1">%s</h1>
    <p class="lede adv-lede">%s</p>
  </div>
</section>
""" % (t["kicker"], t["h1"], t["lede"])


def trends(lang, prefix):
    t = T[lang]
    items = "".join(
        '<li><b>%s</b><span>%s</span></li>' % (html.escape(k), d) for k, d in t["themes"]
    )
    return """<section class="sec adv-sec" id="trends">
  <div class="wrap">
    <div class="eyebrow"><span class="num">01</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <a class="adv-card" href="%s">
      <span class="adv-card-k">%s</span>
      <span class="adv-card-t">%s</span>
      <span class="adv-card-d">%s</span>
      <span class="adv-card-go">%s <span aria-hidden="true">&rarr;</span></span>
    </a>
    <ul class="adv-themes">%s</ul>
  </div>
</section>
""" % (t["eb_1"], t["trends_h"], t["trends_p"], t["video_href"],
       t["card_k"], t["card_t"], t["card_d"], t["card_arrow"], items)


def beyond(lang, prefix):
    t = T[lang]
    return """<section class="sec adv-sec" id="beyond">
  <div class="wrap">
    <div class="eyebrow"><span class="num">02</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <p class="adv-link"><a href="%scontrol.html#advanced">%s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % (t["eb_2"], t["beyond_h"], t["beyond_p"], prefix, t["beyond_a"])


def paper(lang, prefix):
    t = T[lang]
    return """<section class="sec adv-sec" id="paper">
  <div class="wrap">
    <div class="eyebrow"><span class="num">03</span><span class="line"></span><span class="eyebrow-label">%s</span></div>
    <h2 class="adv-h2">%s</h2>
    <p class="adv-p">%s</p>
    <p class="adv-link"><a href="%ssafety.html">%s <span aria-hidden="true">&rarr;</span></a>
      <a href="%sstandards.html">%s <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>
""" % (t["eb_3"], t["paper_h"], t["paper_p"], prefix, t["paper_a"], prefix, t["paper_b"])


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
<script>
(function(){var b=document.getElementById("burger");if(!b)return;
b.addEventListener("click",function(){var o=document.body.classList.toggle("menu-open");
b.setAttribute("aria-expanded",o?"true":"false");});})();
</script>
</body>
</html>
""" % (brand, t["foot_note"], t["foot_built"])


def build_lang(lang, path, prefix):
    body = head(lang, prefix)
    body += topbar(lang, prefix)
    body += hero(lang)
    body += trends(lang, prefix)
    body += beyond(lang, prefix)
    body += paper(lang, prefix)
    body += footer(lang, prefix)
    framework.write(path, framework.tidy(body))
    return path


def main():
    a = build_lang("en", os.path.join("advanced", "index.html"), "../")
    b = build_lang("vi", os.path.join("vi", "advanced", "index.html"), "../../")
    print("  %-28s advanced page (en)" % a)
    print("  %-28s advanced page (vi)" % b)


if __name__ == "__main__":
    main()
