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
import pages_control  # noqa: E402
import pages_compare  # noqa: E402
import pages_ref  # noqa: E402
import pages_glossary  # noqa: E402

DIST = framework.DIST
ASSETS = os.path.join(ROOT, "assets")

NOT_FOUND = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found — Instrumentation &amp; Control</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<main class="sec" style="padding-top:90px">
  <div class="wrap">
    <div class="eyebrow"><span class="num">404</span><span class="line"></span><span class="eyebrow-label">Not found</span></div>
    <h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">This loop is open.</h1>
    <p class="lede">The page you asked for does not exist. Return to the index and pick a branch.</p>
    <div class="hero-cta"><a class="btn btn-p" href="index.html">Back to home &rarr;</a></div>
  </div>
</main>
</body>
</html>
"""


def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST, exist_ok=True)

    pages_home.build()
    pages_core.build_fundamentals()
    pages_core.build_instruments()
    pages_control.build()
    pages_compare.build()
    pages_ref.build_geotechnical()
    pages_ref.build_standards()
    pages_glossary.build()

    # static assets
    dst = os.path.join(DIST, "assets")
    os.makedirs(dst, exist_ok=True)
    for name in os.listdir(ASSETS):
        shutil.copy2(os.path.join(ASSETS, name), os.path.join(dst, name))

    with open(os.path.join(DIST, "404.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(NOT_FOUND)
    with open(os.path.join(DIST, ".nojekyll"), "w", encoding="utf-8") as fh:
        fh.write("")

    files = sorted(os.listdir(DIST))
    print("built %d entries in dist/" % len(files))
    for f in files:
        p = os.path.join(DIST, f)
        if os.path.isfile(p):
            print("  %-24s %6.1f kB" % (f, os.path.getsize(p) / 1024.0))
    print("glossary terms: %d" % len(pages_glossary.TERMS))
    print("instrument rows: %d" % len(pages_core.ROWS))


if __name__ == "__main__":
    main()
