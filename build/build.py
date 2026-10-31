# -*- coding: utf-8 -*-
"""Build the whole site into dist/."""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import framework  # noqa: E402
import pages_home  # noqa: E402
import pages_core  # noqa: E402
import pages_install  # noqa: E402
import pages_control  # noqa: E402
import pages_advanced  # noqa: E402
import pages_safety  # noqa: E402
import pages_tools  # noqa: E402
import pages_compare  # noqa: E402
import pages_ref  # noqa: E402
import pages_glossary  # noqa: E402
import pages_applications  # noqa: E402
import pages_education  # noqa: E402
import pages_process  # noqa: E402
import pages_videos  # noqa: E402
import pages_hot  # noqa: E402

DIST = framework.DIST
ASSETS = os.path.join(ROOT, "assets")

def not_found():
    """404 with the same nav as every other page.

    Absolute hrefs (prefix "/"), because GitHub Pages serves this one file for
    a miss at any depth: a relative link would resolve against /foo/bar/.
    """
    nav = "\n      ".join(
        '<a class="%s" href="%s">%s</a>' % (cls, href, label)
        for cls, href, label in framework.nav_links("en", "/", "")
    )
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found — Instrumentation &amp; Control</title>
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css?v=%s">
</head>
<body>
<header class="topbar">
  <div class="wrap bar">
    <a class="brand" href="/index.html" aria-label="Home">
      <span class="mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="30" height="30" fill="none">
          <rect x="1" y="1" width="30" height="30" rx="8" stroke="currentColor" stroke-width="1.5" opacity=".35"/>
          <path d="M7 22h6l3-12 3 12h6" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
          <circle cx="16" cy="10" r="2.2" fill="currentColor"/>
        </svg>
      </span>
      <span class="brand-txt"><strong>Instrumentation &amp; Control</strong><em>Field Guide</em></span>
    </a>
    <nav class="nav" id="nav">
      %s
    </nav>
    <div class="bar-right">
      <a class="lang" href="/?lang=vi"><span class="lang-opt on">EN</span><span class="lang-sep">/</span><span class="lang-opt">VI</span></a>
    </div>
  </div>
</header>
<main class="sec" style="padding-top:90px">
  <div class="wrap">
    <div class="eyebrow"><span class="num">404</span><span class="line"></span><span class="eyebrow-label">Not found</span></div>
    <h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">This loop is open.</h1>
    <p class="lede">The page you asked for does not exist. Return to the index and pick a branch.</p>
    <div class="hero-cta"><a class="btn btn-p" href="/index.html">Back to home &rarr;</a></div>
  </div>
</main>
</body>
</html>
""" % (framework.ASSET_VER, nav)


NOT_FOUND = not_found()


def stale(dist):
    """Files under dist/ that this run did not write.

    The build used to wipe dist/ first. It no longer does: a bulk delete of the
    tree trips the workspace safety guard, and overwriting is enough because
    every path the build owns is rewritten in full on each run. What is left
    behind is a file whose page was removed from the build — rare, and reported
    here rather than deleted silently.
    """
    keep = set()
    for path in framework.WRITTEN:
        keep.add(os.path.normcase(os.path.abspath(path)))
    out = []
    for root, _dirs, files in os.walk(dist):
        for name in files:
            full = os.path.normcase(os.path.abspath(os.path.join(root, name)))
            if full not in keep:
                out.append(os.path.join(root, name))
    return out


def main():
    os.makedirs(DIST, exist_ok=True)

    pages_home.build()
    pages_core.build_fundamentals()
    pages_core.build_instruments()
    pages_install.build()
    pages_control.build()
    pages_advanced.main()
    pages_safety.build()
    pages_tools.build()
    pages_compare.build()
    pages_ref.build_geotechnical()
    pages_ref.build_standards()
    pages_applications.build()
    pages_education.build()
    pages_process.build()
    pages_videos.main()
    pages_glossary.build()
    pages_hot.main()

    # static assets (assets/pdfjs/ is a tree: pdf.js plus its cmaps and fonts)
    dst = os.path.join(DIST, "assets")
    os.makedirs(dst, exist_ok=True)
    for name in os.listdir(ASSETS):
        src = os.path.join(ASSETS, name)
        target = os.path.join(dst, name)
        if os.path.isdir(src):
            if os.path.isdir(target):
                shutil.rmtree(target)
            shutil.copytree(src, target)
            for dp, _dn, fn in os.walk(target):
                for f in fn:
                    framework.WRITTEN.append(os.path.join(dp, f))
        else:
            shutil.copy2(src, target)
            framework.WRITTEN.append(target)

    for name, body in (("404.html", NOT_FOUND), (".nojekyll", "")):
        target = os.path.join(DIST, name)
        with open(target, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(body)
        framework.WRITTEN.append(target)

    files = sorted(os.listdir(DIST))
    print("built %d entries in dist/" % len(files))
    for f in files:
        p = os.path.join(DIST, f)
        if os.path.isfile(p):
            print("  %-24s %6.1f kB" % (f, os.path.getsize(p) / 1024.0))
    left = stale(DIST)
    if left:
        print("stale in dist/ (not written by this run, left in place):")
        for path in left:
            print("  %s" % os.path.relpath(path, DIST))
    print("glossary terms: %d" % len(pages_glossary.TERMS))
    print("instrument rows: %d" % len(pages_core.ROWS))


if __name__ == "__main__":
    main()
