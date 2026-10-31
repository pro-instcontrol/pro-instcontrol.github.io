# Translation status — handoff for the next agent

**Last updated:** end of session 2026-10-30 (session 4) · **Live site:** https://pro-instcontrol.github.io/

> **Where to start next:** Handbook **Chapter 8 — Proximity Sensing for Robotics**. Chapters 1–7
> are done. Everything you need is in §3 and §4.
>
> **Chapter 7 landed this session** — 16 figures, three source tables, 6.9k words VI. It is on
> its own figure module, `build/hb7fig.py`, because the source chapter has no figures at all
> and every diagram had to be invented from the text (see §7, session 4).
>
> **Earlier this session** six chapters landed — PC 3, 4, 5 and SIS 3, 4, 5 — on the
> `vfig.py` / `pcfig.py` / `pcsis_common.py` architecture described in §3.1.

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
| Measurement, Instrumentation and Sensors Handbook | `the-measurement-instrumentation-and-sensors-handbook` | 101 | **1–7** | `build/reader_handbook.py` + `reader_hb_chNN.py` per chapter |
| Safety Instrumented Systems | `safety-instrumented-systems-design-analysis-justification` | 16 | **1–5** | `build/reader_sis.py` (+ `sis_chNN.py`, `sisfig.py`) |
| Practical Process Control | `pc-process-control` | 14 | **1–5** | `build/reader_pc.py` (+ `pc_chNN.py`, `pcfig.py`, `pc4fig.py`, `pc5fig.py`) |

Chapters done, with their slugs and build scripts:

| # | Title | Slug | Script | Figures | Words (VI) |
|---|---|---|---|---|---|
| HB 1 | Characteristics of Instrumentation | `ch01-characteristics-of-instrumentation` | (session 1) | — | — |
| HB 2 | Operational Modes of Instrumentation | `ch02-operational-modes-of-instrumentation` | (session 1) | — | — |
| HB 3 | Static and Dynamic Characteristics | `ch03-static-and-dynamic-characteristics-of-instrumentation` | `reader_hb_ch03.py` | 18 | 9.7k |
| HB 4 | Measurement Accuracy | `ch04-measurement-accuracy` | `reader_hb_ch04.py` | 2 | 6.7k |
| HB 5 | Measurement Standards | `ch05-measurement-standards` | `reader_hb_ch05.py` | 3 | 6.5k |
| HB 6 | Displacement Measurement, Linear and Angular | `ch06-displacement-measurement` (landing) + 12 section pages | `reader_hb_ch06.py` (+ `hb06_common.py`, `hb06fig.py`, `hb06_s01…s12.py`) | 123 | 63k |
| HB 7 | Thickness Measurement | `ch07-thickness-measurement` | `reader_hb_ch07.py` + `hb7fig.py` | 16 | 6.9k |
| PC 1 | Introduction | `ch01-introduction` | *none kept* | — | — |
| PC 2 | Process Measurement and Transducers | `ch02-process-measurement-and-transducers` | `work/build_pc_ch2_en.py` + `_vi.py` | — | — |
| PC 3 | Basic Principles of Control Valves and Actuators | `ch03-basic-principles-of-control-valves-and-actuators` | `reader_pc.py` → `pc_ch03.py` + `pcfig.py` | 24 | 8.0k |
| PC 4 | Fundamentals of Control Systems | `ch04-fundamentals-of-control-systems` | `reader_pc.py` → `pc_ch04.py` + `pc4fig.py` | 11 | 4.2k |
| PC 5 | Stability and Control Modes of Closed Loops | `ch05-stability-and-control-modes-of-closed-loops` | `reader_pc.py` → `pc_ch05.py` + `pc5fig.py` | 11 | 5.6k |
| SIS 1 | Introduction | `ch01-introduction` | *none kept* | — | — |
| SIS 2 | Design Lifecycle | `ch02-design-lifecycle` | *none kept* | — | — |
| SIS 3 | Process Control vs. Safety Control | `ch03-process-control-vs-safety-control` | `reader_sis.py` → `sis_ch03.py` + `sisfig.py` | 1 | 6.3k |
| SIS 4 | Protection Layers | `ch04-protection-layers` | `reader_sis.py` → `sis_ch04.py` + `sisfig.py` | 3 | 5.2k |
| SIS 5 | Developing the Safety Requirement Specifications | `ch05-developing-the-safety-requirement-specifications` | `reader_sis.py` → `sis_ch05.py` | 0 | 4.5k |

> **Only chapters 1 and 2 of PC and SIS have no generator.** Everything from Chapter 3 on
> is generated — edit the `pc_chNN.py` / `sis_chNN.py` module and rerun the orchestrator,
> never the HTML. If you need to change Chapter 1 or 2, edit the HTML in place (and remember
> that a later `build/build.py` will not touch those two directories).

Progress pills on the library cards are driven by numbers, not by the page contents:

- `build/books_site.py` → `TRANSLATED = {...}` — tuple `("progress", total_chapters, done_chapters)`.
  Currently `("progress", 101, 7)`, `("progress", 16, 5)`, `("progress", 14, 5)`.
- `build/reader_handbook.py` → `DONE = {chapter_no: "chapter-slug"}`.
- `build/reader_book.py` → per-book `"done": {chapter_no: "chapter-slug"}`.
- `build/reader_pc.py` / `build/reader_sis.py` → `MODULES = {chapter_no: "pc_chNN"}` — which
  chapter modules the orchestrator builds, and in which order it chains the `chapter-nav`.
- **The previous chapter's forward `chapter-nav` link** — see below.

**If you add a chapter page and forget these, the TOC will not link to it** — and the
page count on the library card will be wrong.

### The chapter-nav chain rots every time a chapter lands

Each chapter page ends with a two-slot `chapter-nav`: previous chapter on the left,
next chapter on the right. When the next chapter is added, **the previous chapter's
forward link must be rewritten** — nothing does this automatically. Chapter 1 shipped
with a greyed-out `<span class="disabled">… · chưa dịch</span>` in that slot, and it was
still saying "not translated" four chapters later.

For the PC and SIS books this is now automatic: `pcsis_common.nav()` walks the ordered
`MODULES` map, so chapter *N*'s forward slot is whatever module comes next, and the last
module gets "Book contents". Adding a chapter to `MODULES` is enough. The handbook still
needs the manual step:

When you add chapter *N*:

1. Rewrite the right-hand slot of chapter *N−1* in **both** languages.
2. If chapter *N−1* has a generator (`reader_hb_chNN.py`), edit the generator and rerun it —
   not the HTML, or the next rebuild undoes your fix.
3. If it has no generator (handbook chapters 1 and 2, PC 1–2, SIS 1–2), edit the HTML
   directly.
4. The newest chapter keeps "All chapters → / Book contents" in its right slot until
   chapter *N+1* exists.

Grep for leftovers before you commit:

```bash
grep -rn "chưa dịch\|not translated" books/read vi/books/read
grep -rln 'class="disabled"' books/read vi/books/read
```

## 3. Next unit of work

### 3.1 PC and SIS: the shared architecture (built this session)

Both books share one stack. Adding a chapter means writing one module, one figure module,
and one line in `MODULES`.

| File | Role |
|---|---|
| `build/vfig.py` | the primitives everything else builds on: `_txt`, `_line`, `_arrow`, `_rect`, `_circle`, `_axes`, `_curve`, `_finish`, `INK` / `GREY` / `BLUE` / `RED` / `GREEN` |
| `build/pcsis_common.py` | page shell, prose markup (`p / h2 / h3 / eq / quote / note / ul / refs / fig / table`), and `nav()` |
| `build/pcfig.py`, `pc4fig.py`, `pc5fig.py` | one figure module per chapter |
| `build/sisfig.py` | figures for SIS 3 and 4 (SIS 5 has none) |
| `build/pc_ch03.py`, `pc_ch04.py`, `pc_ch05.py` | one text module per chapter, exposing `body_vi()` / `body_en()` |
| `build/sis_ch03.py`, `sis_ch04.py`, `sis_ch05.py` | same, for SIS |
| `build/reader_pc.py`, `build/reader_sis.py` | orchestrators. `python reader_pc.py` builds every chapter in `MODULES`; `python reader_pc.py 4` builds one |

`MODULES` in each orchestrator is an **ordered** dict — the order is what the `nav()`
chain walks. Adding chapter 6 to PC is `MODULES = {…, 6: "pc_ch06"}` plus the module.

Figure-function contract, identical to the handbook:

```python
def fig_5_3():
    o = [...]
    return _finish("".join(o), 660, 192,
                   "caption VI", "caption EN", "aria VI", "aria EN")
```

Helper signatures that are easy to get wrong:

- `_axes(x0, y0, W, H, xlab, ylab, xt=None, yt=None)` — ticks are `[(value, label), …]` in
  **data units**; both axis titles sit on the top row.
- `_curve(fn, x0, y0, W, H, n=121, xr=(0,1), yr=(0,1), **kw)` — return `None` from `fn` to
  drop a sample; that is how a steep line gets clipped at the frame instead of escaping it.
- `_legend(x, y, rows, w=126)` — boxed key, `rows = [(colour, label, dash), …]`.
- `_legend_h(x, y, rows, gap=22)` — unboxed horizontal key, for when every corner of the
  plot is crossed by a curve. Put it at `y0 + H + 16` and raise the canvas by 6 px.
- `_circle(cx, cy, r, fill="none", sw=1.1, color=INK, dash="")` — the keyword is **`color`**,
  not `stroke`. This has bitten once.

### 3.2 Done — how Chapter 6 is built (keep this as the template for any big chapter)

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

### 3.3 Immediate: Handbook Chapter 8 — Proximity Sensing for Robotics

A normal-sized chapter. Use the ordinary single-page recipe in §4 with
`reader_handbook.py` `DONE[8]` and a `ch08-…` slug; do **not** copy Chapter 6's
twelve-page structure — it was only ever a size workaround.

The chapter number and PDF asset name come from the release listing in §4.1 —
check the real title there before choosing the slug; the Part II list in the book
TOC (`reader_handbook.py`, the `CHAPTERS` table near line 61) is authoritative.

### 3.4 Then

- Handbook Chapters 8–101, one per sitting.
- The handbook is the priority and the user has said so twice. Do **not** resume PC or SIS
  until the handbook is finished — the six chapters done this session were an explicit,
  bounded exception ("stop after this chapter and continue to translate 6 chapters of
  next 2 books").
- When the handbook is done: PC from Chapter 6, then SIS from Chapter 6. Both are now on
  the same architecture, so each is one `pc_chNN.py` / `sis_chNN.py` plus a figure module.

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

Every figure is an inline SVG, never a raster crop. Drawing functions go in a
**per-chapter module**: `build/hbfig.py` holds Chapters 3–5, `build/hb06fig.py` holds
Chapter 6, `build/hb7fig.py` holds Chapter 7. `hbfig.py` also exports the primitives the
later modules import — `Box`, `_f`, `_box`, `_vlink`, `svg`, `_fig`, and the `INK` /
`MUTED` / `GOLD` colours. Do not keep appending to `hbfig.py`; a chapter of any size gets
its own module and imports from it.
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

Then edit **all four** registries (`reader_handbook.py` `DONE`, `books_site.py`
`TRANSLATED`, `reader_book.py` `"done"`, and the previous chapter's forward nav) and
rebuild the landing pages:

```bash
python reader_handbook.py           # book TOC, both languages
python books_site.py                # library index, both languages
cd ..
python build/make_sitemap.py        # 437 URLs at last run
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
| A legend box covers a curve | there are only four corners and the curves cross all of them | move it under the axis with `_legend_h`, not to another corner — three attempts at "another corner" all failed |
| `_circle() got an unexpected keyword argument 'stroke'` | the parameter is `color` | `_circle(cx, cy, r, color=…)` |
| A dimension arrow bisects its own label | label placed at the midpoint between the two arrow tips | put it beside one tip instead |
| A page has no previous/next links at all | `nav()` was defined but never called from `page()` | it is wired now; if you fork the shell, call it |
| A wide table wraps tags mid-token (`FALL-` / `1000`) | eleven columns squeezed into the prose width | `table.tbl.matrix` CSS + merge columns until it fits |
| `git rebase FETCH_HEAD` conflicts in generated HTML | both sides rebuilt the same pages | `git rebase --abort`; `git stash`/backup; `git reset --hard FETCH_HEAD`; restore **only** the new `build/*.py` files by name — a blanket `git checkout <backup> -- build/` reverts `build.py`, `framework.py` and the registries too |
| Meta line reads `0 hình` on a figure-less chapter | the figure clause was unconditional | it is conditional now; keep it that way |
| A figure label vanishes behind its own shape | the label was emitted before the shape that covers it — SVG has no z-index | draw in back-to-front order: core, then windings, then labels |
| `x^2` or `ε_r` looks like a typo in an SVG label | `baseline-shift` is unreliable in browsers | use `_sup()` / `_sub()` from `hb7fig.py` — `<tspan dy="−3.2">` then a zero-width reset |
| A formula inside a plot sits on top of the curve | oscillation or monotone decay fills the whole frame | move the formula **above** the plot frame, at `y = 14` |
| A long label runs off the right edge of the canvas | text anchored `start` near `x = 540` | measure roughly (`≈4.4 px per character at fs 8.6`) or switch to `anchor="end"` |

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
- **Translate chapters, not book sections.** A "chapter" with nothing but an Introduction
  is skipped rather than padded.
- **Translate the whole chapter.** Every section, never abridged. If the source is
  unusable, say so — put `<b>là bản scan bị lỗi</b>` in a translator's note and explain
  exactly which part could not be read (SIS Chapter 5 does this for its cause-and-effect
  table).
- Do not delete `.workbuddy-ai/`.
- **Write this file's session log before you stop.**

## 7. Session log

### 2026-10-30, session 4 — Handbook Chapter 7, Thickness Measurement

**Chapter 7 is complete and live:** `ch07-thickness-measurement`, 10 source pages,
**16 figures, 3 tables, 6.9k words VI / 1.8k EN**, 192 kB / 216 kB. Commit `8eba02e`.

The chapter's difficulty is unusual and worth recording: **the source has no figures at
all** — only Tables 7.1, 7.2 and 7.3. Every one of the sixteen diagrams is invented from
the prose, which means the normal "redraw the source figure" loop did not apply and each
figure had to justify itself from a stated relation. They are:

| # | Subject | What was computed |
|---|---|---|
| 7-1 | The thickness scale | log10 positions of seven objects from 10²⁰ m to 10⁻⁷ m |
| 7-2 | Why a caliper fails | decision tree, no curve |
| 7-3 | Micrometer reading | 0.5 mm pitch ÷ 50 divisions = 0.01 mm; 7.5 + 28×0.01 = 7.78 mm |
| 7-4 | LVDT | V = exp(−((x−d)/w)²) − exp(−((x+d)/w)²), the differential S-curve |
| 7-5 | Pneumatic backpressure | P/P_s = 1/(1+(g/g₀)²); peak sensitivity at g₀/√3 |
| 7-6 | Capacitance | C/C₀ = d₀/d |
| 7-7 | Eddy-current lift-off | S = S₀·exp(−z/zc) |
| 7-8 | Magnetic pull-off | F/F₀ = 1/(1+z/a)⁴ on a log axis |
| 7-9 | Hall gauge | schematic + dimension |
| 7-10 | Pulse-echo A-scan | three Gaussian echoes at 0.3 / 2 / 4 µs; d = c·Δt/2 = 5.9 mm in steel |
| 7-11 | Channeled spectrum | T = 1/(1+F sin²(2πndν̄)), d = 20 and 40 µm |
| 7-12 | Newton's rings | r_m = √((m+½)λR); I = sin²(πr²/λR) |
| 7-13 | Beta backscatter / transmission | 1−e^(−µx) against e^(−µx) |
| 7-14 | AFM force–distance | F = −A/z² + B/z⁸, zero at z₀ = 0.6 nm, well at 0.76 nm |
| 7-15 | STM tunnelling | κ = √(2mφ)/ħ from φ = 4 eV → 1.02 Å⁻¹, a decade per 1.1 Å |
| 7-16 | THz transient | Gaussian-derivative pulse (τ = 100 fs) and its spectrum, peak 2.25 THz |

A translator's note at the head of the chapter states this openly, and says that where the
text is only qualitative the figure had to pick a functional form — named in the figure.

Figure defects caught by QA this round, all real:

- **`fig_7_3` labelled every half-millimetre tick "0,5"** instead of 1,5 / 2,5 / 3,5, and its
  red pointer ran straight through the number ring on the thimble. Fixed both.
- **`fig_7_4` painted the core bar over its own S₁ / P / S₂ labels** — the labels were drawn
  before the rect that covered them. Core now drawn first, windings as open frames.
- **`fig_7_5` had two annotations in the same corner** ("vùng làm việc" and "độ nhạy cực
  đại"). The curve leaves no room for a working-range band at all, so the band was dropped
  and the peak annotation moved clear.
- **`fig_7_7`'s lift-off dimension floated at x=206 with no coil above it** — now on the
  left with guide lines to the coil and the coating.
- **`fig_7_10`'s Δt arrow ended inside the third pulse** — rebuilt as a proper dimension
  with dashed construction verticals at both echo positions.
- **`fig_7-11` and `7-12` put their formulas on top of their own curves** (both plots are
  oscillation from edge to edge). Both formulas moved above the plot frame.
- **`fig_7_13`'s saturation label was clipped by the canvas edge** — shortened to "bão hoà".
- **`fig_7_14`'s "lực hút cực đại" sat on the x-axis** — moved right of the well.
- **`fig_7_15`'s formula block was bisected by its own 1 Å marker** — the marker was removed
  and the block moved into the empty lower-left triangle under the curve.

Two new CSS rules in `books/assets/library.css` for table patterns this chapter needed:
`table.tbl tr.grp td` (a group-header row inside a reference table — Table 7.1 uses six of
them) and `p.tblcap` (the italic grey caption line under a table, matching `.figcap`).

New helpers in `hb7fig.py` worth reusing: `_sup()` / `_sub()` (reliable super/subscripts via
`<tspan dy>`, because `baseline-shift` is not dependable), `_panel()` (titled box with
left-aligned lines, bold lines as `(text, "b")` tuples), `_dim()` (double-headed dimension
line), `_plot()` (samples a function, breaks the path outside the frame), `_key()`
(horizontal colour key above the plot).

Also fixed: `reader_hb_ch06.py`'s landing-page nav pointed its forward slot at the book
contents; it now points at Chapter 7 in both languages. The book TOC title for chapter 7 was
"Đo độ dày" while the page H1 said "Đo chiều dày" — the TOC now matches the page.

Verification: sitemap **437 URLs / 424 pairs**; link check **439 pages, 10,647 local
references, 0 broken**; library pill `7/101`; book TOC `done rows: 7`; Part II reads
`12 chương · 2 đã dịch`; both chapter-7 URLs and the chapter-6 landing return 200 live.

### 2026-10-30, session 3 — six chapters across PC and SIS

The user's instruction was "stop after this chapter and continue to translate 6 chapters
of next 2 books": finish Handbook 6 (already shipped at the start of the session), then
**PC 3, 4, 5 and SIS 3, 4, 5**. All six are done, built, QA'd, committed (`1cad1b3`) and
pushed to `main`.

| # | Chapter | Source pp | Figures | Words VI | HTML VI / EN |
|---|---|---|---|---|---|
| PC 3 | Basic Principles of Control Valves and Actuators | 40 | 24 | 7.992 | 171 kB / 10 kB |
| PC 4 | Fundamentals of Control Systems | 17 | 11 | 4.194 | 113 kB / 8 kB |
| PC 5 | Stability and Control Modes of Closed Loops | 23 | 11 | 5.645 | 119 kB / 9 kB |
| SIS 3 | Process Control vs. Safety Control | 15 | 1 | 6.289 | 36 kB / 9 kB |
| SIS 4 | Protection Layers | 13 | 3 | 5.223 | 40 kB / 8 kB |
| SIS 5 | Developing the Safety Requirement Specifications | 14 | 0 | 4.534 | 27 kB / 8 kB |

**Architecture built this session** (described in §3.1): `vfig.py` primitives,
`pcsis_common.py` shell + markup, per-chapter figure and text modules, and
`reader_pc.py` / `reader_sis.py` orchestrators. This replaces the ad-hoc hand-written
HTML that PC 1–2 and SIS 1–2 were built with.

Content notes worth keeping:

- **PC 3** carries equations 3.x for valve sizing, the `Cv`/`Kv` conversion, cavitation
  and flashing limits, and actuator thrust balancing — 24 figures, the most of any
  chapter this session.
- **PC 5** carries equations 5.1–5.9, Table 5-1 (five mode combinations) and a
  translator's note that Exercises 2–6 are simulation-harness work and were not
  translated.
- **SIS 3** puts each verbatim ANSI/ISA-91.00.01 clause in a `quote()` and works the
  beta-factor arithmetic explicitly (10⁻⁶ → 10 %). It also keeps the ISA SP84 audit
  story: a third of the safety functions deleted, a third bypassed, a third dead.
- **SIS 4** is the Bhopal chapter — the ten protection layers are counted in a `note()`,
  and the de-energize-vs-energize-to-trip argument and the IEC cap of 10 are both kept.
- **SIS 5** is the only figure-less chapter so far; `page()` had to be taught not to
  print `0 hình`. Table 5-3 is a nine-column cause-and-effect matrix (see below).

Defects found and fixed by visual QA — each one was real, not cosmetic:

- **`pcsis_common.page()` never called `nav()`.** Every chapter page shipped with no
  previous/next links at all, in either language. Now wired.
- **`fig_5_3`'s legend crossed the K=1 line at top-right**, then the K=0.2 line at
  bottom-right; it ended up in the empty upper-left. This is what prompted `_legend_h`.
- **Four PC Ch.5 legends covered curves** (5-4, 5-6, 5-7, 5-9). All four moved below the
  axis with `_legend_h(x0, y0 + H + 16, …)`, canvas raised 186 → 192.
- **`fig_5_11` drew the set point through a different value mapping than the curves**, so
  the PI response appeared never to reach it. Rebuilt so both use `y0 + H * (1 - value)`;
  the static-offset dimension arrow was then added between the two.
- **`fig_5_4` / `fig_5_7`'s "lệch 90°" labels sat on the wave peaks** — amplitude 0.34 →
  0.30 and the labels lifted to `y0 + 9`.
- **`fig_4_1` (Swiss cheese) had its holes off the dashed path** — only two of four were
  crossed. Holes re-centred on 100/108/102/106 against a path at y=104.
- **`fig_3_1`'s quote box overlapped the plant box**, and the dashed control/protection
  divider ran straight through the plant; the divider now stops above it.
- **`fig_4_2` (onion) was taller than its canvas** and its footnotes collided with the
  outer ring — rebuilt at radii 18…98 around `(320, 132)`.
- **SIS Ch.5's cause-and-effect matrix wrapped every tag mid-token.** Eleven columns do
  not fit the prose width; added `table.tbl.matrix` to `library.css` and cut the table to
  nine columns. Tags now sit on one line and the X marks are centred.

**Rebase conflict.** The remote had moved. `git rebase FETCH_HEAD` conflicted in three
generated pages (`vi/books/index.html`, the PC index, the SIS index). Aborted, saved a
`pre-rebase-backup` branch, `git reset --hard FETCH_HEAD`, then restored **only** the new
`build/*.py` files by name. A blanket `git checkout pre-rebase-backup -- build/` also
reverted `build.py`, `framework.py`, `books_site.py` and `reader_book.py`, which then had
to be restored separately — the six registry edits and the CSS were re-applied by hand.
Lesson recorded in §5.

**Verification:** sitemap **435 URLs / 422 EN/VI pairs**; link check **437 pages, 10,599
local references, 0 broken**. Library pills read `6/101`, `5/16`, `5/14`. Both book TOCs
show five done rows. The `ch02 → ch03 → ch04 → ch05 → book index` chain was walked
end-to-end in both languages for both books. The sitewide nav standardisation from
`2f9b72b` is intact on all six new pages (18 site-nav links, `/vi/books/` marked active).

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
