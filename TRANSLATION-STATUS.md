# Translation status — handoff for the next agent

**Last updated:** end of session 2026-10-30 · **Live site:** https://pro-instcontrol.github.io/

> **Where to start next:** Handbook **Chapter 7 — Thickness Measurement**. Chapter 6 is
> finished (twelve section pages, 123 figures). Everything you need is in §3 and §4.

This file is the single source of truth for the book-translation work on this site.
Read it before touching anything. Update the status table and append to the session log
at the end of every session.

---

## 1. What the job is

Three English books are being translated into Vietnamese, chapter by chapter, and
published as bilingual reader pages under `/books/read/<book-slug>/<chapter-slug>/`
(English) and `/vi/books/read/<book-slug>/<chapter-slug>/` (Vietnamese).

Order of work, fixed by the site owner:

1. **Measurement, Instrumentation and Sensors Handbook** (CRC Press, 1999) — finish it first.
2. **Practical Process Control for Engineers and Technicians** (Altmann, IDC).
3. **Safety Instrumented Systems — Design, Analysis, and Justification** (Gruhn & Cheddie, ISA 2006).

## 2. Where things stand

| Book | slug | Chapters | Translated | Reader generator |
|---|---|---|---|---|
| Measurement, Instrumentation and Sensors Handbook | `the-measurement-instrumentation-and-sensors-handbook` | 101 | **1–6** | `build/reader_handbook.py` + `build/reader_hb_ch06.py` |
| Safety Instrumented Systems | `safety-instrumented-systems-design-analysis-justification` | 16 | **1–2** | `build/reader_book.py` (`"sis"`) |
| Practical Process Control | `pc-process-control` | 14 | **1–2** | `build/reader_book.py` (`"pc"`) |

Chapters done, with their slugs and build scripts:

| # | Title | Slug | Script | Figures | Words (VI) |
|---|---|---|---|---|---|
| HB 1 | Characteristics of Instrumentation | `ch01-characteristics-of-instrumentation` | (session 1) | — | — |
| HB 2 | Operational Modes of Instrumentation | `ch02-operational-modes-of-instrumentation` | (session 1) | — | — |
| HB 3 | Static and Dynamic Characteristics | `ch03-static-and-dynamic-characteristics-of-instrumentation` | `reader_hb_ch03.py` | 18 | 9.7k |
| HB 4 | Measurement Accuracy | `ch04-measurement-accuracy` | `reader_hb_ch04.py` | 2 | 6.7k |
| HB 5 | Measurement Standards | `ch05-measurement-standards` | `reader_hb_ch05.py` | 3 | 6.5k |
| HB 6 | Displacement Measurement, Linear and Angular | `ch06-displacement-measurement` (landing) + 12 section pages | `reader_hb_ch06.py` (+ `hb06_common.py`, `hb06fig.py`, `hb06_s01…s12.py`) | 123 | 63k |
| PC 1 | Introduction | `ch01-introduction` | *none kept* | — | — |
| PC 2 | Process Measurement and Transducers | `ch02-process-measurement-and-transducers` | `work/build_pc_ch2_en.py` + `_vi.py` | — | — |
| SIS 1 | Introduction | `ch01-introduction` | *none kept* | — | — |
| SIS 2 | Design Lifecycle | `ch02-design-lifecycle` | *none kept* | — | — |

> **Caveat.** Only the handbook chapters have proper generator scripts. The PC and SIS
> pages were written ad-hoc, so editing them means editing the generated HTML in place.
> When you resume those two books, write a proper `reader_pc_chNN.py` / `reader_sis_chNN.py`
> first (copy `reader_hb_ch05.py`) rather than hand-editing.

Progress pills on the library cards are driven by numbers, not by the page contents:

- `build/books_site.py` → `TRANSLATED = {...}` — tuple `("progress", total_chapters, done_chapters)`.
- `build/reader_handbook.py` → `DONE = {chapter_no: "chapter-slug"}`.
- `build/reader_book.py` → per-book `"done": {chapter_no: "chapter-slug"}`.

**If you add a chapter page and forget these three, the TOC will not link to it.**

### The chapter-nav chain rots every time a chapter lands

Each chapter page ends with a two-slot `chapter-nav`: previous chapter on the left,
next chapter on the right. When the next chapter is added, **the previous chapter's
forward link must be rewritten** — nothing does this automatically. Chapter 1 shipped
with a greyed-out `<span class="disabled">… · chưa dịch</span>` in that slot, and it was
still saying "not translated" four chapters later.

When you add chapter *N*:

1. Rewrite the right-hand slot of chapter *N−1* in **both** languages.
2. If chapter *N−1* has a generator (`reader_hb_chNN.py`), edit the generator and rerun it —
   not the HTML, or the next rebuild undoes your fix.
3. If it has no generator (chapters 1 and 2 of the handbook, all PC/SIS chapters), edit the
   HTML directly.
4. The newest chapter keeps "All chapters → / Book contents" in its right slot until
   chapter *N+1* exists.

Grep for leftovers before you commit:

```bash
grep -rn "chưa dịch\|not translated" books/read vi/books/read
grep -rln 'class="disabled"' books/read vi/books/read
```

## 3. Next unit of work

### Done — how Chapter 6 is built (keep this as the template for any big chapter)

Chapter 6 shipped as **one landing page + twelve section pages**, and the machinery is
worth reusing if another oversized chapter turns up. Nothing here needs touching to move
on to Chapter 7; read it only if you have to change a Chapter 6 page.

| File | Role |
|---|---|
| `build/hb06_common.py` | `SECTIONS` (twelve `(n, slug, title_vi, title_en)` tuples), `LANDING`, the twelve section authors (`BYLINE`), and the PSD markup helpers `p / h2 / h3 / eq / quote / ul / note / refs / fig / table / nav / page` |
| `build/hb06fig.py` | every vector figure, `fig_6_1()` … `fig_6_123()`, ~6,000 lines. Each returns a 5-tuple `(svg, cap_vi, cap_en, aria_vi, aria_en)` via `_fig(...)` |
| `build/hb06_s01.py` … `hb06_s12.py` | one module per section, each exposing `body_vi()` and `body_en()` |
| `build/reader_hb_ch06.py` | orchestrator: `python reader_hb_ch06.py` writes the landing page and all twelve sections in both languages; `python reader_hb_ch06.py 7` writes one section |

Source word counts per section, and the slug each one was published under:

| § | Section | Slug | Words |
|---|---|---|---|
| 6.1 | Resistive Displacement Sensors | `ch06-1-resistive-displacement-sensors` | 5,563 |
| 6.2 | Inductive Displacement Sensors | `ch06-2-inductive-displacement-sensors` | 7,563 |
| 6.3 | Capacitive Sensors — Displacement | `ch06-3-capacitive-displacement-sensors` | 5,746 |
| 6.4 | Piezoelectric Transducers and Sensors | `ch06-4-piezoelectric-transducers` | 5,271 |
| 6.5 | Laser Interferometer Displacement Sensors | `ch06-5-laser-interferometer` | 5,989 |
| 6.6 | Bore Gaging Displacement Sensors | `ch06-6-bore-gaging` | 4,454 |
| 6.7 | Time-of-Flight Ultrasonic Displacement Sensors | `ch06-7-time-of-flight-ultrasonic` | 2,425 |
| 6.8 | Optical Encoder Displacement Sensors | `ch06-8-optical-encoders` | 8,449 |
| 6.9 | Magnetic Displacement Sensors | `ch06-9-magnetic-displacement-sensors` | 3,836 |
| 6.10 | Synchro/Resolver Displacement Sensors | `ch06-10-synchro-resolver` | 4,858 |
| 6.11 | Optical Fiber Displacement Sensors | `ch06-11-optical-fiber-displacement-sensors` | 6,120 |
| 6.12 | Optical Beam Deflection Sensing | `ch06-12-optical-beam-deflection` | 2,963 |

Two known cosmetic compromises, both chapter-wide and both deliberate:

- **In-figure text is Vietnamese on the English pages too.** Every SVG label is drawn once,
  in Vietnamese; the English section pages reuse the same SVG with an English `figcaption`.
  Fixing it means generating each figure twice — not worth it unless a reader complains.
- **Section 6.12's English page is a companion essay**, not a translation: five `h2`
  sections of commentary, with the eleven figures but only one re-stated equation.

### Immediate: Handbook Chapter 7 — Thickness Measurement

A normal-sized chapter (`Ch07__53d649615a6315cf.pdf`, 222 kB). Use the ordinary
single-page recipe in §4 with `reader_handbook.py` `DONE[7]` and a `ch07-…` slug;
do **not** copy the twelve-page structure — it was only ever a size workaround.

### Then

- Handbook Chapters 8–101, one per sitting.
- After the handbook is finished: Process Control from Chapter 3 (Basic Principles of
  Control Valves and Actuators), then Safety Instrumented Systems from Chapter 3
  (Process Control vs. Safety Control).

## 4. How to translate the next chapter — the recipe

### 4.1 Get the source text

Chapter PDFs live as release assets on `library-pdfs`, named `ChNN__<hash>.pdf`.
Find the one you need and download it:

```bash
TOKEN=$(head -n 1 "C:/Users/Phamd/Documents/Pro-instcontrol.txt" | tr -d '[:space:]')
curl -s -H "Authorization: token $TOKEN" \
  "https://api.github.com/repos/pro-instcontrol/pro-instcontrol.github.io/releases/tags/library-pdfs" \
  | python -c "import json,sys;[print(a['name'],a['browser_download_url']) for a in json.load(sys.stdin)['assets'] if a['name'].startswith('Ch0')]"
```

Extract the text — **use the bundled CLI, not pypdf** (pypdf inserts intra-word spaces
like `de velop` and floods stderr with fontTools warnings):

```bash
"C:/Users/Phamd/.workbuddy-ai/external-packages/pdf-cli/workbuddy-pdf.exe" \
  work/Ch07.pdf work/hb_ch07.txt --format txt
```

To *see* a figure, render pages to PNG and look at them:

```bash
"C:/Users/Phamd/.workbuddy-ai/external-packages/pdf-cli/workbuddy-pdf.exe" \
  work/Ch07.pdf work/ch07png --format png
```

### 4.2 Redraw the figures as vectors

Every figure is an inline SVG, never a raster crop. Put the drawing functions in
**`build/hbfig.py`** (one module holds all handbook figures; keep it that way).
Each function returns a 5-tuple:

```python
def fig_7_1():
    ...
    return _fig(svg(W, H, "".join(o), "<aria-label in Vietnamese>"),
                "<caption VI>", "<caption EN>",
                "<aria VI>", "<aria EN>")
```

Helpers already in `hbfig.py`: `_box(x, y, w, h, lines, fs=, fill=)` for a labelled
rectangle, `_vlink(x, y1, y2)` for a vertical connector, `_f()` for number formatting,
`svg(w, h, body, title)`, `_fig(...)`. `Box` (for plotted curves) is used by the
Chapter 3 step-response figures.

**Layout discipline — this is where the time goes.** Every figure so far has needed at
least one collision fix. Rules that saved time:

- Give each column of a diagram an explicit centre and width, and compute box edges
  from them; never hand-place a box by eyeballing the previous one.
- A horizontal "bus" line must be drawn *between* rows, never at the same y as a box
  top — that is what produced the doubled-border look in the first draft of Fig 5.1.
- Leave ≥ 8 px between a box edge and any text baseline inside it.
- After writing the function, screenshot it before wiring it into the page.

### 4.3 Write the chapter script

Copy `build/reader_hb_ch05.py` as the template. It has the whole pattern:

- `CSLUG`, `TITLE_EN/VI`, `BYLINE`, `BASE_EN`, `BASE_VI`
- local `fig(num, key, lang)`, `p()`, `h2(t, en)`, `h3(t, en)`, `eq(body, num)`,
  `quote(text, src)`, `term(name, body, vim, note)`, `glossary(entries)`
- `body_vi()` — the real translation, `body_en()` — the English companion
- `build(lang)` wraps the body in the shared `head/header/footer` from `reader_handbook.py`
- `main()` writes both languages

Bilingual heading convention: `<h2>Tiếng Việt <span class="en">English</span></h2>`.

The Vietnamese body ends with a chained `chapter-nav`:

```python
b.append('<div class="chapter-nav">'
         '<a href="%sch05-.../"><span class="k">← Chương 5</span>Title</a>'
         '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Nội dung sách</a></div>'
         % (BASE_VI, BASE_VI))
```

The English body is a **companion**, not a stub: it carries the figures, a table or two,
and prose that explains the argument of the chapter. It is not a translation of the
translation.

### 4.4 Register, build, verify, ship

```bash
cd build
python reader_hb_ch06.py            # writes both languages
```

Then edit **all three** registries (`reader_handbook.py` `DONE`, `books_site.py`
`TRANSLATED`) and rebuild the landing pages:

```bash
python reader_handbook.py           # book TOC, both languages
python books_site.py                # library index, both languages
cd ..
python build/make_sitemap.py        # 357 URLs at last run
python build/check_links.py         # must print "broken 0"
```

### 4.5 Visual QA

```bash
# serve the repo (must be a background process)
python -m http.server 8899 --bind 127.0.0.1

# full page
npx -y playwright@latest screenshot --full-page --viewport-size=1280,900 \
  --wait-for-timeout=1800 "http://127.0.0.1:8899/vi/books/read/<slug>/<ch>/" out.png
```

Playwright is not installed locally — always call it through `npx -y playwright@latest`.
A full-page shot of a 6,000 px page is unreadable, so use the two helper scripts in
`work/qa5/` (copy them, they still work):

- `work/qa5/slice.py <url> <top> <height> <out.html>` — a fixed window into the page.
- `work/qa5/at.py <url> <css-selector> <height> <out.html>` — scrolls the page so the
  element matching the selector sits 60 px from the top. **Serve the wrapper over HTTP
  from the same origin** (`http://127.0.0.1:8899/work/qa5/at.html`), not via `file://`,
  or `contentDocument` is cross-origin and the script silently does nothing. The iframe
  height in `at.py` is 20000 px for a reason: a chapter page is taller than 9000 px.

To inspect one SVG at natural size, pull it out of the built page and wrap it:

```python
svg = re.search(r"<svg.*?</svg>", open(page, encoding="utf-8").read(), re.S).group(0)
open("work/qa5/svg.html", "w", encoding="utf-8").write(
    '<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#fff}'
    'svg{width:900px;height:auto;display:block}</style></head><body>%s</body></html>' % svg)
```

### 4.6 Deploy

```bash
TOKEN=$(head -n 1 "C:/Users/Phamd/Documents/Pro-instcontrol.txt" | tr -d '[:space:]')
git add -A
git -c user.name="Pro InstControl" -c user.email="pro.instcontrol@outlook.com" \
    commit -m "Add Handbook Chapter N (Title) in both languages"
git fetch "https://$TOKEN@github.com/pro-instcontrol/pro-instcontrol.github.io.git" HEAD
git log --oneline HEAD..FETCH_HEAD        # if the remote moved, rebase first
git rebase FETCH_HEAD
python build/make_sitemap.py              # regenerate AFTER the rebase
git add -A && git commit -m "Regenerate sitemap"   # only if it changed
git push "https://$TOKEN@github.com/pro-instcontrol/pro-instcontrol.github.io.git" HEAD:main
```

Pages publishes about 40 s later. Verify:

```bash
curl -s -o /dev/null -w "%{http_code}\n" "https://pro-instcontrol.github.io/vi/books/read/<slug>/<ch>/"
```

## 5. Traps that have already bitten

| Symptom | Cause | Fix |
|---|---|---|
| `TypeError: cannot unpack non-iterable function object` | passed `hbfig.fig_5_1` instead of `hbfig.fig_5_1()` | call the function |
| TOC still says `1/101` | the pill number was hard-coded | derive it from `len(DONE)` / the `TRANSLATED` tuple |
| `MODULE_NOT_FOUND` for playwright | `node script.js` with no local install | `npx -y playwright@latest screenshot …` |
| `ERR_CONNECTION_REFUSED` | `(python -m http.server &)` in a subshell dies | launch it as a background task |
| Link checker reports hundreds of broken links | regex `(?:href\|src)=` also matches `data-src=` | require a `(?<![\w-])` boundary — `build/check_links.py` does this |
| Link checker under-counts pages | directory pruning applied at every level | prune only at the root (already handled in `check_links.py`) |
| Every `.toc-list` row shows title and description run together | the landing template uses `.d`, which had no CSS rule | `.toc-list a .t { display:block }` + `.toc-list a .d { display:block … }` in `library.css` |
| A figure's curve has the wrong symmetry (bump instead of S-curve) | sign error inside `erf` — `erf(a+u) − erf(−(a−u))` collapses to an even function | write the difference exactly as the equation reads: `erf(y₁+u) − erf(y₁−u)` |
| Labels sit on top of the curve in a `_measured()` plot | annotation placed at a fixed `y0 + 24` | put the label in the empty half of the plot, not the top strip |
| `grep -c` reports 1 figure on a page that has twelve | generated HTML is a single long line | count with `re.findall` in Python |
| A physics constant in the book does not reproduce from its own formula | the source is not always self-consistent | recompute, then add a `note()` box saying what the arithmetic gives and why — never silently "fix" the text |
| Push rejected, non-fast-forward | the video-library work landed while you were translating | `git fetch` + `git rebase FETCH_HEAD`, then regenerate the sitemap |
| `SyntaxError` after an edit | an edit ate a newline between two statements | read the region before editing |

## 6. House rules

- **Vietnamese is the content; English is the companion.** Never leave the English page
  as a one-line stub.
- Numbers use `.` as the thousands separator and `,` as the decimal mark in Vietnamese
  (`1.300`, `0,442 °F`).
- Every figure gets `role="img"` and a Vietnamese `aria-label`.
- Curves must be computed from the stated formula, never sketched by hand.
- Keep the source's own numbering for equations and figures (`(4.21)`, `Hình 5-3`).
- The glossary in Chapter 5 keeps the VIM clause numbers in `[brackets]` — do the same
  for any VIM-sourced definition.
- Do not delete `.workbuddy-ai/`.

## 7. Session log

### 2026-10-30, session 2 — Chapter 6 finished

- **Handbook Chapter 6 — Displacement Measurement, Linear and Angular is complete:**
  twelve section pages plus a landing page, in both languages. 63,237 source words,
  **123 vector figures**, 138 numbered equations, 8 tables, ~700 kB of HTML.
- Built the reusable Chapter 6 machinery described in §3: `hb06_common.py` (shared
  markup + the twelve section tuples), `hb06fig.py` (all figures), twelve `hb06_sNN.py`
  modules, and `reader_hb_ch06.py` as orchestrator.
- This session finished sections **6.9–6.12**:
  - **6.9 Magnetic Displacement Sensors** — replaced a wrong "Table 6.26 could not be
    extracted" note with the real four-column table of sensors, manufacturers and 1999
    prices, in both languages.
  - **6.10 Synchro/Resolver Displacement Sensors** — 10 figures, equations 6.113–6.116,
    the seventeen-step test procedure, Table 6.27 (15 suppliers), 10 kB EN / 104 kB VI.
  - **6.11 Optical Fiber Displacement Sensors** — 14 figures, equations 6.117–6.125,
    Tables 6.28 and 6.29, all 24 references, 8 kB EN / 102 kB VI.
  - **6.12 Optical Beam Deflection Sensing** — 11 figures, equations 6.126–6.138,
    11 references, 70 kB EN / 79 kB VI.
- **Three physics corrections found while checking the arithmetic**, all documented in
  `note()` boxes so the reader sees them rather than a silent fix:
  - 6.12: the text says the bicell optimum is at `r₁ = 2y₁` **and** that the peak
    sensitivity is `0.484/y₁`; those two statements disagree. Differentiating 6.137 gives
    `r₁ = √2·y₁`, and that value reproduces 0.484/y₁ exactly (`r₁ = 2y₁` gives 0.439/y₁).
  - 6.12: the printed "calculated sensitivity 3.8 × 10³ m⁻¹" cannot be reproduced from
    `r₁ = 0.4 mm` and `y₁ = 63.5 µm` — that gives 2.75 × 10³. The 3.8 × 10³ figure
    reappears if the 1/e radius (0.283 mm) is used instead of the 1/e² radius, which is
    the classic beam-radius mix-up. The measured value (4.1 × 10³ m⁻¹) is unaffected.
  - 6.12: figure 6.117's curve had a sign error (`erf(y₁+u) − erf(−(y₁−u))`), which
    turned the odd difference response into an even bump. Now `erf(y₁+u) − erf(y₁−u)`.
- **Figure QA passes this session** (each caught a real defect): 6.114's y-axis had
  `y = 0` at the arrow tip instead of at the blade edge and its beam ticks were drawn
  over the hatching; 6.115's "linear range" label pointed at a horizontal guide line
  rather than at the tangent, so the tangent was redrawn inside the plot and the range
  moved to a bracket on the u axis; 6.116 was rebuilt (dimension arrows, `y = 0` centre
  line, legible `y₁/y₂`); 6.120's annotation sat on the flat sum-voltage curve.
- **Fixed a CSS gap:** the chapter landing pages used `<span class="t">` / `<span class="d">`
  in `.toc-list`, but `.d` had no rule, so every section title ran into its description.
  Added `.toc-list a .t { display:block }` and `.toc-list a .d { … }` to
  `books/assets/library.css`. This affected both language versions of the landing page.
- Registered Chapter 6 in `DONE[6]` and bumped the library card to **6/101**.
  Book TOC now reads `Đang dịch · 6/101 chương`, and Part II reads `12 chương · 1 đã dịch`.
- Sitemap regenerated: **385 URLs, 372 EN/VI pairs**. Link check: **387 pages,
  8,216 local references, 0 broken**.
- Removed two leftover `build/_head.tmp` / `_tail.tmp` scratch files before committing.

### 2026-10-30, session 1 — Chapter 5

- Translated **Handbook Chapter 5 — Measurement Standards** (DeWayne B. Sharp) in full:
  6,490 words of Vietnamese, 3 figures, 2 tables, 32 VIM glossary entries, 2 pull quotes,
  7 references. English companion written with a four-kinds-of-standards table and a
  glossary index keyed to VIM clause numbers.
- Drew figures 5.1 (organisation fan), 5.2 (quality chain) and 5.3 (three-branch
  measurement assurance system). **All three were re-laid out after visual QA**:
  5.3 originally had the international column overlapping the national column and
  three clipped labels; 5.1 had a 1 px "bus" rectangle drawn across the top of the
  national-bodies row; 5.2 had cramped labels.
- Added `.pullquote`, `.glossary` and `.gloss-aside` styles to `books/assets/library.css`.
- Registered Chapter 5 in `DONE` and bumped the library card to 5/101.
- Added `build/check_links.py` (reusable, exit-code driven).
- Sitemap regenerated: 357 URLs, 344 EN/VI pairs. Link check: 359 pages,
  7,556 local references, **0 broken**.
- Rebased onto two video-library commits from the remote; pushed as `4d338c8`.
- Live verification: `ch05` VI page → 6,490 words / 3 figures / 32 glossary entries;
  book TOC reads `Đang dịch · 5/101 chương`; all four URLs return 200.
- Downloaded and extracted **Chapter 6** for the next session (`work/hb_ch06.txt`,
  167 pages, 63,446 words) and worked out the per-section split described in §3.
