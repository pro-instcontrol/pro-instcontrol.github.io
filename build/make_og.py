# -*- coding: utf-8 -*-
"""Render assets/og-video-library.png from the live dataset.

The share card carries the headline stats, so it goes stale the moment a video is
added. This reads them straight from videos_data instead of letting someone retype
them. Requires node + playwright (same module path the rest of the checks use).

    python build/make_og.py
"""

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import videos_data  # noqa: E402

OUT = os.path.join(ROOT, "assets", "og-video-library.png")


def seconds(d):
    p = [int(x) for x in d.split(":")]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]


def stats():
    total = sum(seconds(v[3]) for v in videos_data.VIDEOS)
    cats = len({v[1] for v in videos_data.VIDEOS})
    srcs = len({v[4] for v in videos_data.VIDEOS})
    return len(videos_data.VIDEOS), cats, int(total / 3600 + 0.5), srcs


HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0}
  html,body{width:1200px;height:630px;overflow:hidden}
  body{
    background:#fff;color:#0b1725;font-family:Inter,sans-serif;
    -webkit-font-smoothing:antialiased;
    background-image:
      repeating-linear-gradient(90deg,#eef2f7 0 1px,transparent 1px 60px),
      repeating-linear-gradient(0deg,#eef2f7 0 1px,transparent 1px 60px);
    padding:64px 74px 58px;display:flex;flex-direction:column;
  }
  .brand{display:flex;align-items:center;gap:11px;color:#0d7a6f}
  .mark{width:34px;height:34px;flex:0 0 34px}
  .brand strong{display:block;font-size:15.5px;font-weight:700;letter-spacing:-.015em;color:#0b1725;line-height:1.2}
  .brand em{
    display:block;font-style:normal;font-family:"IBM Plex Mono",monospace;font-size:9px;
    letter-spacing:.19em;text-transform:uppercase;color:#66788d;margin-top:3px;
  }
  h1{font-size:71px;font-weight:800;letter-spacing:-.038em;line-height:.99;margin-top:74px}
  .sub{font-size:41px;font-weight:400;letter-spacing:-.028em;color:#5a6d82;margin-top:10px}
  .pill{
    align-self:flex-start;display:inline-flex;align-items:center;gap:8px;margin-top:34px;
    background:#e6f4f2;color:#0a5f56;border-radius:999px;padding:8px 15px;
    font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.14em;
    text-transform:uppercase;font-weight:500;
  }
  .pill i{width:5px;height:5px;border-radius:50%%;background:#0d7a6f;display:block}
  .foot{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between}
  .stats{display:flex;gap:44px}
  .stat b{display:block;font-size:31px;font-weight:700;letter-spacing:-.03em;line-height:1}
  .stat span{
    display:block;font-family:"IBM Plex Mono",monospace;font-size:9.5px;letter-spacing:.16em;
    text-transform:uppercase;color:#66788d;margin-top:7px;
  }
  .url{font-family:"IBM Plex Mono",monospace;font-size:12px;color:#8a9bad;letter-spacing:.02em}
</style></head>
<body>
  <div class="brand">
    <svg class="mark" viewBox="0 0 32 32" fill="none">
      <rect x="1" y="1" width="30" height="30" rx="8" stroke="#0d7a6f" stroke-width="1.5" opacity=".4"/>
      <path d="M7 22h6l3-12 3 12h6" stroke="#0d7a6f" stroke-width="1.9" stroke-linejoin="round" stroke-linecap="round"/>
      <circle cx="16" cy="10" r="2.2" fill="#0d7a6f"/>
    </svg>
    <span><strong>Instrumentation &amp; Control</strong><em>Field guide</em></span>
  </div>

  <h1>Process instrumentation &amp;<br>control, on video</h1>
  <div class="sub">A library that is indexed, not dumped</div>
  <div class="pill"><i></i>Video library</div>

  <div class="foot">
    <div class="stats">
      <div class="stat"><b>%d</b><span>videos</span></div>
      <div class="stat"><b>%d</b><span>topics</span></div>
      <div class="stat"><b>%d</b><span>hours</span></div>
      <div class="stat"><b>%d</b><span>sources</span></div>
    </div>
    <div class="url">pro-instcontrol.github.io/video-library</div>
  </div>
</body></html>
"""

JS = """
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  await p.goto('file:///%s', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(350);
  await p.screenshot({ path: '%s' });
  await b.close();
})();
"""


def main():
    n, cats, hours, srcs = stats()
    tmp = tempfile.mkdtemp()
    html_path = os.path.join(tmp, "og.html")
    js_path = os.path.join(tmp, "shot.js")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML % (n, cats, hours, srcs))
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(JS % (html_path.replace("\\", "/"), OUT.replace("\\", "/")))
    node = os.environ.get("NODE_BIN", "node")
    env = dict(os.environ)
    env.setdefault("NODE_PATH", r"C:\Users\Phamd\.workbuddy-ai\binaries\node\workspace\node_modules")
    subprocess.run([node, js_path], check=True, env=env)
    print("wrote %s  (%d videos, %d topics, %d hours, %d sources)" % (OUT, n, cats, hours, srcs))


if __name__ == "__main__":
    main()
