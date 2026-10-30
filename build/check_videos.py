# -*- coding: utf-8 -*-
"""Verify the video library dataset and every YouTube link in it.

    python build/check_videos.py            # dataset checks + link check
    python build/check_videos.py --offline  # dataset checks only, no network

Dataset checks catch the mistakes a rebuild would silently publish: duplicate
ids, an unknown category, a malformed duration, a category with no videos.
The link check uses YouTube's oEmbed endpoint, which returns 200 only for
public, embeddable videos — the same condition the library needs.

Exit code is 1 if anything fails, so it can be dropped into CI or a pre-push hook.
"""

import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import videos_data  # noqa: E402

OEMBED = "https://www.youtube.com/oembed?format=json&url="
DUR = re.compile(r"^\d+:\d{2}(:\d{2})?$")
LEVELS = {"B", "I", "A"}


def check_dataset():
    problems = []
    seen = {}
    cat_ids = {c[0] for c in videos_data.CATS}

    for i, v in enumerate(videos_data.VIDEOS):
        if len(v) != 8:
            problems.append("entry %d has %d fields, expected 8" % (i, len(v)))
            continue
        vid, cat, lvl, dur, src, title, note_en, note_vi = v
        if vid in seen:
            problems.append("duplicate id %s (also at entry %d)" % (vid, seen[vid]))
        seen[vid] = i
        if cat not in cat_ids:
            problems.append("%s: unknown category %r" % (vid, cat))
        if lvl not in LEVELS:
            problems.append("%s: level %r not in B/I/A" % (vid, lvl))
        if not DUR.match(dur):
            problems.append("%s: duration %r is not m:ss or h:mm:ss" % (vid, dur))
        for field, name in ((title, "title"), (note_en, "note_en"), (note_vi, "note_vi"), (src, "source")):
            if not (field or "").strip():
                problems.append("%s: empty %s" % (vid, name))
        if re.search(r"\s{2,}", title) and "  " not in title:
            problems.append("%s: odd whitespace in title" % vid)

    counts = {}
    for v in videos_data.VIDEOS:
        counts[v[1]] = counts.get(v[1], 0) + 1
    for cid in cat_ids:
        if not counts.get(cid):
            problems.append("category %r has no videos" % cid)

    total = 0
    for v in videos_data.VIDEOS:
        parts = [int(p) for p in v[3].split(":")]
        while len(parts) < 3:
            parts.insert(0, 0)
        total += parts[0] * 3600 + parts[1] * 60 + parts[2]

    print("dataset: %d videos, %d categories, %d sources, %.1f hours"
          % (len(videos_data.VIDEOS), len(counts),
             len({v[4] for v in videos_data.VIDEOS}), total / 3600.0))
    thinnest = sorted(counts.items(), key=lambda kv: kv[1])[:5]
    print("thinnest: " + ", ".join("%s=%d" % kv for kv in thinnest))
    return problems


def check_links(pause=0.05):
    dead = []
    ids = [v[0] for v in videos_data.VIDEOS]
    for i, vid in enumerate(ids, 1):
        url = OEMBED + urllib.parse.quote("https://www.youtube.com/watch?v=" + vid)
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                if r.status != 200:
                    dead.append((vid, "HTTP %d" % r.status))
        except urllib.error.HTTPError as e:
            dead.append((vid, "HTTP %d (private, removed or not embeddable)" % e.code))
        except Exception as e:  # network hiccup, not necessarily dead
            dead.append((vid, "error: %s" % str(e)[:60]))
        if i % 25 == 0:
            print("  checked %d/%d" % (i, len(ids)))
        time.sleep(pause)
    print("links: %d checked, %d unavailable" % (len(ids), len(dead)))
    return dead


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="skip the network link check")
    args = ap.parse_args()

    problems = check_dataset()
    if args.offline:
        print("link check skipped (--offline)")
        dead = []
    else:
        dead = check_links()

    if problems:
        print("\ndataset problems:")
        for p in problems:
            print("  - " + p)
    if dead:
        print("\nunavailable videos (replace or drop these):")
        for vid, why in dead:
            title = next((v[5] for v in videos_data.VIDEOS if v[0] == vid), "")
            print("  - %s  %s  %s" % (vid, why, title[:60]))

    if problems or dead:
        sys.exit(1)
    print("\nok — dataset clean, all links public and embeddable")


if __name__ == "__main__":
    main()
