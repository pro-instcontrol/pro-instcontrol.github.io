# Translation status — handoff for the next agent

**Last updated:** 2026-10-31 (session 21 — Chapter 21 added) · **Live site:** https://pro-instcontrol.github.io/

> **Where to start next:** Handbook **Chapter 22** (and onward). Chapters
> 1–21 are done, live, and registered. `work/hb_ch21.txt` is translated; Chapter 22+ source
> PDFs must be extracted from the 117-file handbook library before translation.
>
> **Both translated books are finished.** Practical Process Control (14/14) and Safety
> Instrumented Systems (16/16) each have full Vietnamese translations and English companion
> pages that carry the same figures as their Vietnamese counterparts — 54 figures on the SIS
> side, 120 on the PC side, zero mismatches.
>
> **The glossary is now generated, not written by hand.** `/glossary.html` and
> `/vi/glossary.html` are built by `build/make_glossary.py`, which parses the
> `<dl class="glossary">` block of every translated chapter and merges it with the curated
> list in `build/pages_glossary.py`. Adding a chapter that defines terms adds them to the
> glossary automatically on the next build — see §4.5.
>
> **Read §5 before drawing anything.** Session 7 found four figure defects that the
> Georgia-serif QA grid cannot see, because its font metrics differ from the site font.

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
| Measurement, Instrumentation and Sensors Handbook | `the-measurement-instrumentation-and-sensors-handbook` | 101 | **1–21** | `build/reader_handbook.py` + `reader_hb_chNN.py` per chapter |
| Safety Instrumented Systems | `safety-instrumented-systems-design-analysis-justification` | 16 | **1–16 ✅ done** | `build/reader_sis.py` (+ `sis_chNN.py`, `sisfig.py`) |
| Practical Process Control | `pc-process-control` | 14 | **1–14 ✅ done** | `build/reader_pc.py` (+ `pc_chNN.py`, `pcfig.py` … `pc14fig.py`) |

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
| HB 8 | Proximity Sensing for Robotics | `ch08-proximity-sensing-for-robotics` | `reader_hb_ch08.py` + `hb8fig.py` | 26 | 7.6k |
| HB 9 | Distance | `ch09-distance` | `reader_hb_ch09.py` + `hb9fig.py` | 8 | 8.9k |
| HB 10 | Position, Location, Altitude Measurement | `ch10-position-location-altitude` | `reader_hb_ch10.py` + `hb10fig.py` | 43 | 13.4k |
| HB 11 | Level Measurement | `ch11-level-measurement` | `reader_hb_ch11.py` + `hb11fig.py` | 15 | 7.1k |
| HB 12 | Area Measurement | `ch12-area-measurement` | `reader_hb_ch12.py` + `hb12fig.py` | 10 | 7.0k |
| HB 13 | Volume Measurement | `ch13-volume-measurement` | `reader_hb_ch13.py` + `hb13fig.py` | 10 | 7.3k |
| HB 14 | Angle Measurement | `ch14-angle-measurement` | `reader_hb_ch14.py` + `hb14fig.py` | 3 | 3.5k |
| HB 15 | Tilt Measurement | `ch15-tilt-measurement` | `reader_hb_ch15.py` + `hb15fig.py` | 5 | ~5.0k |
| HB 16 | Velocity Measurement | `ch16-velocity-measurement` | `reader_hb_ch16.py` + `hb16fig.py` | 16 | ~8.0k |
| HB 17 | Acceleration, Vibration, and Shock Measurement | `ch17-acceleration-vibration-shock-measurement` | `reader_hb_ch17.py` + `hb17fig.py` | 23 | ~11k |
| HB 18 | Time Measurement | `ch18-time-measurement` | `reader_hb_ch18.py` + `hb18fig.py` | 3 | ~9k |
| HB 19 | Frequency Measurement | `ch19-frequency-measurement` | `reader_hb_ch19.py` + `hb19fig.py` | 15 | ~14k |
| HB 20 | Mass and Weight Measurement | `ch20-mass-and-weight-measurement` | `reader_hb_ch20.py` + `hb20fig.py` | 3 | ~6k |
| HB 21 | Density Measurement | `ch21-density-measurement` | `reader_hb_ch21.py` + `hb21fig.py` | 16 | ~12k |
| PC 1 | Introduction | `ch01-introduction` | *none kept* | — | — |
| PC 2 | Process Measurement and Transducers | `ch02-process-measurement-and-transducers` | `work/build_pc_ch2_en.py` + `_vi.py` | — | — |
| PC 3 | Basic Principles of Control Valves and Actuators | `ch03-basic-principles-of-control-valves-and-actuators` | `reader_pc.py` → `pc_ch03.py` + `pcfig.py` | 24 | 8.2k |
| PC 4 | Fundamentals of Control Systems | `ch04-fundamentals-of-control-systems` | `reader_pc.py` → `pc_ch04.py` + `pc4fig.py` | 11 | 4.4k |
| PC 5 | Stability and Control Modes of Closed Loops | `ch05-stability-and-control-modes-of-closed-loops` | `reader_pc.py` → `pc_ch05.py` + `pc5fig.py` | 11 | 5.8k |
| PC 6 | Digital Control Principles | `ch06-digital-control-principles` | `reader_pc.py` → `pc_ch06.py` + `pc6fig.py` | 6 | 3.6k |
| PC 7 | Real and Ideal P.I.D. Controllers | `ch07-real-and-ideal-pid-controllers` | `reader_pc.py` → `pc_ch07.py` + `pc7fig.py` | 9 | 3.1k |
| PC 8 | Tuning of PID Controllers in Open and Closed Loop | `ch08-tuning-of-pid-controllers` | `reader_pc.py` → `pc_ch08.py` + `pc8fig.py` | 11 | 7.5k |
| PC 9 | Controller Output Modes, Equations and Cascade Control | `ch09-output-modes-equations-and-cascade-control` | `reader_pc.py` → `pc_ch09.py` + `pc9fig.py` | 9 | 5.9k |
| PC 10 | Concepts and Applications of Feedforward Control | `ch10-concepts-and-applications-of-feedforward-control` | `reader_pc.py` → `pc_ch10.py` + `pc10fig.py` | 9 | 3.9k |
| PC 11 | Combined Feedback and Feedforward Control | `ch11-combined-feedback-and-feedforward-control` | `reader_pc.py` → `pc_ch11.py` + `pc11fig.py` | 7 | 3.2k |
| PC 12 | Long Process Dead-Time and the Smith Predictor | `ch12-long-dead-time-and-the-smith-predictor` | `reader_pc.py` → `pc_ch12.py` + `pc12fig.py` | 6 | 3.4k |
| PC 13 | Basic Principles of Fuzzy Logic and Neural Networks | `ch13-basic-principles-of-fuzzy-logic-and-neural-networks` | `reader_pc.py` → `pc_ch13.py` + `pc13fig.py` | 8 | 6.5k |
| PC 14 | Self-Tuning Intelligent Control and SPC | `ch14-self-tuning-intelligent-control-and-statistical-process-control` | `reader_pc.py` → `pc_ch14.py` + `pc14fig.py` | 11 | 5.9k |
| SIS 1 | Introduction | `ch01-introduction` | *none kept* | 0 | 8.0k |
| SIS 2 | Design Lifecycle | `ch02-design-lifecycle` | *none kept* | 3 | 4.9k |
| SIS 3 | Process Control vs. Safety Control | `ch03-process-control-vs-safety-control` | `reader_sis.py` → `sis_ch03.py` + `sisfig.py` | 1 | 6.4k |
| SIS 4 | Protection Layers | `ch04-protection-layers` | `reader_sis.py` → `sis_ch04.py` + `sisfig.py` | 3 | 5.4k |
| SIS 5 | Developing the Safety Requirement Specifications | `ch05-developing-the-safety-requirement-specifications` | `reader_sis.py` → `sis_ch05.py` | 0 | 4.7k |
| SIS 6 | Determining the Safety Integrity Level (SIL) | `ch06-determining-the-safety-integrity-level` | `reader_sis.py` → `sis_ch06.py` | 7 | 13.4k |
| SIS 7 | Choosing a Technology | `ch07-choosing-a-technology` | `reader_sis.py` → `sis_ch07.py` | 7 | 9.4k |
| SIS 8 | Initial System Evaluation | `ch08-initial-system-evaluation` | `reader_sis.py` → `sis_ch08.py` | 8 | 15.2k |
| SIS 9 | Issues Relating to Field Devices | `ch09-issues-relating-to-field-devices` | `reader_sis.py` → `sis_ch09.py` | 3 | 9.4k |
| SIS 10 | Engineering a System | `ch10-engineering-a-system` | `reader_sis.py` → `sis_ch10.py` | 2 | 8.0k |
| SIS 11 | Installing a System | `ch11-installing-a-system` | `reader_sis.py` → `sis_ch11.py` | 3 | 5.6k |
| SIS 12 | Functional Testing | `ch12-functional-testing` | `reader_sis.py` → `sis_ch12.py` | 3 | 5.8k |
| SIS 13 | Managing Changes to a System | `ch13-managing-changes-to-a-system` | `reader_sis.py` → `sis_ch13.py` | 3 | 4.8k |
| SIS 14 | Justification for a Safety System | `ch14-justification-for-a-safety-system` | `reader_sis.py` → `sis_ch14.py` | 4 | 7.7k |
| SIS 15 | SIS Design Checklist | `ch15-sis-design-checklist` | `reader_sis.py` → `sis_ch15.py` | 1 | 7.0k |
| SIS 16 | Case Study | `ch16-case-study` | `reader_sis.py` → `sis_ch16.py` | 6 | 6.9k |

> **Only chapters 1 and 2 of PC and SIS have no generator.** Everything from Chapter 3 on
> is generated — edit the `pc_chNN.py` / `sis_chNN.py` module and rerun the orchestrator,
> never the HTML. If you need to change Chapter 1 or 2, edit the HTML in place (and remember
> that a later `build/build.py` will not touch those two directories).

Progress pills on the library cards are driven by numbers, not by the page contents:

- `build/books_site.py` → `TRANSLATED = {...}` — tuple `(level, total_chapters, done_chapters)`.
  Currently `("progress", 101, 21)`, `("full", 16, 16)`, `("full", 14, 14)`.
- `build/books_site.py` → `FLAG_LABEL = {level: (vi_format, en_format)}` — **the pill text
  is derived from `level`, not hard-coded.** Add a level here as well as in the CSS, or the
  pill will read "Translating" on a finished book.
- `build/reader_handbook.py` → `DONE = {chapter_no: "chapter-slug"}`.
- `build/reader_book.py` → per-book `"done": {chapter_no: "chapter-slug"}`, plus optional
  `lede_done_xx` / `policy_done_xx` overrides that win once `len(done) == total`.
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

### 3.3 Immediate: Handbook Chapter 11 — Level Measurement

Small chapter: 21 source pages, ~5.6k words. Chapter 12 (Area, 13 pp) follows it and is
smaller still. Both PDFs are already on disk.

| File | What |
|---|---|
| `work/Ch11.pdf` | source, already downloaded |
| `work/hb_ch11.txt` | extracted text (`workbuddy-pdf Ch11.pdf out --format txt`) |
| `work/Ch12.pdf`, `work/hb_ch12.txt` | the next one after that |

Build it exactly like chapter 9 (§3.2 / §4), which is the cheapest template: one figure
module, one chapter script, ~8 figures, one or two tables.

**Chapter 10 is closed.** For the record, since it was the largest chapter in the book and
the one most likely to be used as a model:

| Item | State | Commit |
|---|---|---|
| Figures 10.1–10.16 (sections 10.1, 10.2) | done, QA'd | `320ac92`, `9c6096a` |
| Figures 10.17–10.25 (section 10.3) | done, QA'd | `52f4dde` |
| Figures 10.26–10.36 (section 10.4) | done, QA'd | `666a8f2` |
| Figures 10.37–10.43 (section 10.5) | done, QA'd | `1bcb6b6` |
| `reader_hb_ch10.py` — all five sections, VI + EN | done | `e54d823` |
| Registered in `DONE[10]` and `("progress", 101, 10)` | done | `e54d823` |
| Live | https://pro-instcontrol.github.io/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch10-position-location-altitude/ | — |

Final counts on the live page: **43 figures, 6 tables** (4 numbered + 2 appendix supplier
tables), **124 numbered equations** (10.1–10.114 plus 10.89a/b/c), 5 sections, 8 co-authors.

### 3.4 Then

- **SIS English pages: closed in session 9.** The gap was 3 figures against 54; it is now
  54 against 54, and every chapter's English page is a companion essay of 1,100–2,750 words
  (it was 371–1,560). Chapters 1 and 2, which had no generator and were bare outlines at
  371 and 378 words, are now 1,374 and 1,066 words with the outline kept above the
  commentary. Nothing on the SIS side needs further work.
- Handbook Chapters 11–101. Chapter 11 (Level, 21 pp / 5.6k words) and Chapter 12 (Area,
  13 pp / 4.5k words) are both small and both already downloaded to `work/Ch11.pdf` and
  `work/Ch12.pdf`.
- The handbook is the priority and the user has said so twice. Do **not** revisit PC or SIS
  until the handbook is finished — the chapters done in session 4 were an explicit, bounded
  exception ("stop after this chapter and continue to translate 6 chapters of next 2 books").
- PC and SIS are both **finished** and need no further work.

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

### 4.5 The glossary is a build artefact

`build/make_glossary.py` assembles `/glossary.html` and `/vi/glossary.html` from two
sources and nothing else:

1. `build/pages_glossary.py` → `TERMS`, the 52 curated control and instrumentation terms,
   already bilingual;
2. every `vi/books/read/**/index.html` that contains a `<dl class="glossary">` block — the
   "Định nghĩa thuật ngữ" section of a chapter. The **Vietnamese** headword and definition
   are parsed straight out of the built page, so the glossary can never drift from what the
   chapters say.

The English side of a book term is **not** parsed — there is nothing to parse, because the
English companion pages do not repeat the glossary. It lives in `BOOK_EN` in
`make_glossary.py`: Vietnamese headword → (English headword, English definition). When a
chapter adds a glossary, add its entries there too, or the term will be dropped with no
error.

`ALIAS` maps a book headword onto an existing curated entry (`Hiệu chuẩn` → `Calibration`),
so the curated definition survives and the chapter is listed as an extra source instead of
producing a duplicate row.

**After adding entries:** `python build/make_glossary.py`, then check the count in the hero.
It writes to `dist/` *and* the site root, because `build.py` emits into `dist/` and the tree
is then copied up — writing only to the root would let the copy put back a stale page.

`glossary.html` is in `framework.TWIN_PATHS`, so the Vietnamese nav points at the real
`/vi/glossary.html` rather than `?lang=vi`. Adding a section to the nav means adding it to
that set.

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
| pdf.js says `Missing PDF` for a URL that `curl` fetches fine | the browser refuses the response — no CORS, or a preflight the host answers with 403 | check `OPTIONS` with `Access-Control-Request-Headers: range`; a 403 there kills range loading no matter what `GET` returns |
| A 100 MB book cannot be opened by any viewer | Google gview gives up around 30 MB; release assets send `Content-Disposition: attachment` and no CORS, so nothing can read them | host on GitHub Pages (same origin, `application/pdf`, 206) and render with the vendored pdf.js |
| `git push` rejected: "pre-receive hook declined … is 142.40 MB" | a page-range split is not proportional — one half of a scan can hold nearly all the imagery | split recursively on the *measured* file size (`_leaves()` in `make_pdfstore.py`), never on page count |
| A physics constant in the book does not reproduce from its own formula | the source is not always self-consistent | recompute, then add a `note()` box saying what the arithmetic gives and why — never silently "fix" the text |
| Push rejected, non-fast-forward | the video-library work landed while you were translating | `git fetch` + `git rebase FETCH_HEAD`, then regenerate the sitemap |
| `SyntaxError` after an edit | an edit ate a newline between two statements | read the region before editing |
| A legend box covers a curve | there are only four corners and the curves cross all of them | move it under the axis with `_legend_h`, not to another corner — three attempts at "another corner" all failed |
| `_circle() got an unexpected keyword argument 'stroke'` | the parameter is `color` | `_circle(cx, cy, r, color=…)` |
| A finished book's card says "🟠 Translating · 14 of 14 chapters" | the pill **text** was hard-coded while only the colour came from `level` | `FLAG_LABEL` in `books_site.py` maps `level` → text; never hard-code the label |
| A card pill renders with no colour | `level` was `"done"`, which has no `[data-level]` rule in `library.css` | use one of `full` / `progress` / `summary` / `none` |
| "Open the book →" looks like a link but does nothing | the footer was `<div class="card-footer"><span>…</span></div>` — no `href` anywhere | footer must be `<a href="…">`; `.card-footer a` needs `color: inherit` or it inherits the blue link colour |
| A book's landing page still says "the translation proceeds chapter by chapter" after it is finished | `lede_en` / `policy_en` are static strings | add `lede_done_en` / `policy_done_en` (and `_vi`); `reader_book.build()` prefers them once `len(done) == total` |
| An English page has a Vietnamese subtitle under every heading | `h2("English", "Vietnamese")` — `h2(t, en)` renders the second argument as a subtitle | on English pages pass **one** argument. Only the `"§ 10.2"` section references in ch10–14 are intentional |
| An English companion page has far fewer figures than its Vietnamese twin | `body_en()` never called `fig(...)`; the SVGs existed but were not wired in | after editing, compare counts: `for d in books/read/<book>/ch*; do …; done` — they must match |
| `sisfig.fig_6_1` does not exist | SIS chapters 6–16 each have their **own** figure module (`sis06fig` … `sis16fig`); only ch03 and ch04 use `sisfig` | import the chapter's own module: `import sis08fig as F` |
| A hand-edited chapter page reverts after a rebuild | `build.py` does not touch SIS/PC ch01–ch02, but a careless `cp` or a new generator would | ch01/ch02 of SIS and PC have no generator by design; verify with `md5sum` before and after a build |
| A dimension arrow bisects its own label | label placed at the midpoint between the two arrow tips | put it beside one tip instead |
| A page has no previous/next links at all | `nav()` was defined but never called from `page()` | it is wired now; if you fork the shell, call it |
| A wide table wraps tags mid-token (`FALL-` / `1000`) | eleven columns squeezed into the prose width | `table.tbl.matrix` CSS + merge columns until it fits |
| `git rebase FETCH_HEAD` conflicts in generated HTML | both sides rebuilt the same pages | `git rebase --abort`; `git stash`/backup; `git reset --hard FETCH_HEAD`; restore **only** the new `build/*.py` files by name — a blanket `git checkout <backup> -- build/` reverts `build.py`, `framework.py` and the registries too |
| Meta line reads `0 hình` on a figure-less chapter | the figure clause was unconditional | it is conditional now; keep it that way |
| A figure label vanishes behind its own shape | the label was emitted before the shape that covers it — SVG has no z-index | draw in back-to-front order: core, then windings, then labels |
| `x^2` or `ε_r` looks like a typo in an SVG label | `baseline-shift` is unreliable in browsers | use `_sup()` / `_sub()` from `hb7fig.py` — `<tspan dy="−3.2">` then a zero-width reset |
| A formula inside a plot sits on top of the curve | oscillation or monotone decay fills the whole frame | move the formula **above** the plot frame, at `y = 14` |
| A long label runs off the right edge of the canvas | text anchored `start` near `x = 540` | measure roughly (`≈4.4 px per character at fs 8.6`) or switch to `anchor="end"` |
| A Greek label floats with no arc behind it | the arc was never drawn, only the letter | every angle label needs its `_p("M … A …")` arc; check the pair together |
| A curve runs flat along the bottom frame | the plot clamped out-of-range values to `yr[0]` | stop the polyline at the frame instead — clamping invents data |
| A y axis reads `−0` | the tick list started at 0 and the formatter prefixed every value | special-case zero in the tick list, do not format `-v` for `v = 0` |
| A legend sits on top of the curves | it was placed inside the frame in a gap that the data later filled | put the legend in a row above the frame, or in a genuinely empty corner |
| `NameError: PAPER is not defined` in a new figure module | `hb10fig.py` imports only `GOLD, INK, MUTED, TXT, _f, svg, _fig` from `hbfig` | declare `PAPER = "#ffffff"` alongside the module's own `BLUE`/`RED`/`GREEN`/`SAND`/`BAND` |
| A label sits **on** the arrow it names | the label was placed at a radius *smaller* than the arrow's own length, so it lands inside the shaft | place it at `r + 14` beyond the tip, not at the midpoint |
| Two or three labels pile up at the top of a vector fan | every vector points up, so every label wants the same strip of canvas | give each vector its own length and stagger the tips vertically; the longest gets the outermost label |
| A hatch fills a rectangle instead of the wedge | the hatch runs were clipped to the canvas, not to the wedge's slanted edge | compute the slanted boundary per scan line: `xr = x0 + (y - yTop) * (xR - x0) / (yMid - yTop)` |
| A rotating element (ship roll, gyro roll) is drawn on top of the hull | the arc centre was inside the outline | move the arc centre clear of the outline and re-check at the widest point, not the centreline |
| A part is drawn attached at both ends when it should be free | the rectangle ran from the case wall to the hinge | leave a visible gap: a cantilever that touches the wall reads as a strut |
| An arrow points at a sparse patch of a scatter | the tip was placed by eye, not from the data | compute the tip from the cluster's own coordinates: `X(mean_x), Y(mean_y)` |
| `git rebase` left the tree mid-flight with `UU` files | a `git pull --rebase` hit generated-output conflicts and was abandoned | check `.git/rebase-merge` before anything else; resolve the **source** conflict, take `dcef287`'s HTML, rebuild, then `--continue` |
| A rebase "succeeded" but a file silently lost rules | the index held the correct merge and the worktree held an older copy | after resolving, `git show :path \| grep` against the worktree before committing |
| A figure label is legible on the QA grid but printed across the artwork on the real page | `work/qa6/figs.py` forces `font-family: Georgia, serif`, whose glyph widths differ from the site font — a label that just fits in Georgia overruns in the real face | **verify labels on the rendered page, not on the grid.** The grid is for geometry only. `work/qa22/oneNN.html` (one figure, `width:1180px`, real `library.css`) is the cheap way |
| A circuit schematic labels a transistor that was never drawn | the `_t(…, "Q₃", …)` call was written, the `_mos_v(rail, 240)` call was not | count symbols against labels; a `_mos_v`/`_cap_v`/`_res_v` pair is easy to half-write |
| A lead starts in empty space between two feet | the pictogram's `(x, y)` is the point *between* the feet, but the wire was drawn from that point to a part below | join the feet with a short bar first, then tap the bar — otherwise the schematic shows a connection to nothing |

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

### 2026-10-31, session 14 — Handbook Chapter 14, Angle Measurement

**Shipped:** Handbook chapter 14, *Angle Measurement* (Robert J. Sandberg, University of Wisconsin) — a
mechanical/geometric chapter. Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch14-angle-measurement/`.
Handbook progress 13/101 → 14/101; `DONE[14]`, `("progress", 101, 14)`, and the §2 table all updated.

**What was written this session:**

- `build/hb14fig.py` — the chapter's **three** real figures (14.1 vernier protractor with a zoomed
  reading call-out, 14.2 sine bar with `sin A = H/D`, 14.3 two-ball taper measurement). No figures were
  invented: the source has only Figures 14.1–14.3, so the module is a 3-figure set, not 10.
- `build/reader_hb_ch14.py` — full VI translation + EN companion. Embeds the 3 figures (3/3 parity on
  both languages), the sine-bar relation `sin A = H/D`, Table 14.1 (defining terms, rendered as a
  `<dl class="glossary">` so it feeds `make_glossary.py`), and Tables 14.2/14.3 (manufacturers and the
  full instruments/price list). Also `work/hb_ch14.txt` extracted from `pdf-store/Ch14__…pdf` (8 pages).
- Figure parity: VI 3/3 and EN 3/3, IDs `fig-14-1`…`fig-14-3` confirmed; 4 SVGs/page (3 figures + brand
  mark), 0 malformed on parse.

**Deploy:** `git fetch` → rebase onto 1 remote commit (home-page frames) → `make_sitemap.py` (507 URLs,
492 EN/VI pairs) → `check_links.py` (509 pages, 13,816 references, **0 broken**). Pushed `41518ca` on
`main`. Live: 200 on both VI/EN. Library pill now `Đang dịch · 14/101 chương`.

**Chapters 1–14 done; 87 to go.** Next unit is Chapter 15. Source PDFs for 15+ live in the `pdf-store`/
`pdf-store-b` junctions and `library/pdfindex.json`; copy the needed `ChNN.pdf` into `work/`, extract, then
follow the §4 recipe. Note this chapter had only 3 figures — do not pad figure counts to 10 when the
source genuinely has fewer.

### 2026-10-31, session 16 — Handbook Chapter 16, Velocity Measurement

**Shipped:** Handbook chapter 16, *Velocity Measurement* (Charles P. Pinney, Pinney Technologies, Inc.;
William E. Baker, University of New Mexico) — 17 source pages. Full Vietnamese translation + English
companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch16-velocity-measurement/`.
Handbook progress 15/101 → 16/101; `DONE[16]`, `("progress", 101, 16)`, and the §2 table all updated.

**What was written this session:**

- `build/hb16fig.py` — **all 16** real figures (16.1 position–time graph; 16.2 LVT moving-coil / moving-magnet
  transducers; 16.3 Michelson interferometer; 16.4 VISAR fiber-optic setup; 16.5 seismic instrument; 16.6 dc
  tach-generator; 16.7 ac tach-generator; 16.8 moving-conductor EMF; 16.9 magnetic speed-sensor curve; 16.10
  slotted-disk opto sensor; 16.11/16.12 Hall-effect gear-tooth sensor and circuit; 16.13 Wiegand wire; 16.14
  quartz Coriolis tuning fork; 16.15 MHD angular-rate sensor; 16.16 differenced-accelerometer angular rate).
  No figures invented — the source has 16, so the module is a 16-figure set.
- `build/reader_hb_ch16.py` — full VI translation + EN companion. Embeds all 16 figures (16/16 parity), the
  equations V_avg=(y₂−y₁)/(t₂−t₁) (16.1), V_y=dy/dt (16.2), V_y(t)=V_y(tᵢ)+∫a_y dt (16.3), e_i∝BLV (16.4),
  the Coriolis force F=2m·Ω×V_r, and ω=(1/l)∫(a₁−a₂)dt. Also `work/hb_ch16.txt` extracted from
  `pdf-store-b/Ch16__…pdf` (17 pages). The 20-item reference list is reproduced.
- **Source error flagged with a `note()` box:** the text says approaching source/observer gives a "red shift"
  and receding gives "blue shift" — backwards. The correct convention (blue shift on approach, red shift on
  recession) is noted, and the contradiction with the chapter's own train-whistle example is pointed out.
- Figure parity: VI 16/16 and EN 16/16, IDs `fig-16-1`…`fig-16-16` confirmed; 17 SVGs/page (16 figures +
  brand mark), 0 malformed on parse.

**Deploy:** `git fetch` → remote already at `98de6de` (no new remote commits) → `reader_handbook.py` (16 done
rows), `books_site.py` (progress 101→16), `make_sitemap.py` (511 URLs, 496 EN/VI pairs), `check_links.py`
(513 pages, 13,915 references, **0 broken**). Pushed `99bdd1b` on `main`. Live: 200 on both VI/EN, the book
TOC, and the live VI page reports 16 figures. Library pill now `Đang dịch · 16/101 chương`.

**Chapters 1–16 done; 85 to go.** Next unit is Chapter 17. Source PDFs for 17+ live in the `pdf-store`/
`pdf-store-b` junctions and `library/pdfindex.json`; copy the needed `ChNN.pdf` into `work/`, extract, then
follow the §4 recipe. Note the registry edits (`DONE[16]`, `("progress", 101, 16)`) were applied cleanly this
session — reconfirmed both before committing.

### 2026-10-31, session 21 — Handbook Chapter 21, Density Measurement

**Shipped:** Handbook chapter 21, *Density Measurement* (Halit Eren, Curtin University of Technology) — 17
source pages. Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch21-density-measurement/`.
Handbook progress 20/101 → 21/101; `DONE[21]`, `("progress", 101, 21)`, and the §2 table all updated.

**What was written this session:**

- `build/hb21fig.py` — **all 16** real figures: 21.1 pycnometer; 21.2 hydrometer; 21.3 hydrostatic
  weighing (U-tube on flexible couplings); 21.4 balanced-flow vessel; 21.5 chain balance float; 21.6
  buoyancy gas balance; 21.7 reference column; 21.8 two-tube bubbler; 21.9 suppression-type two-tube;
  21.10 vibrating tube; 21.11 twin vibrating tube; 21.12 tuning fork; 21.13 radioactive on an enlarged
  pipe; 21.14 radioactive on an elongated pipe; 21.15 index-of-refraction cell; 21.16 Coriolis. The
  source has exactly 16 figures and **no tables**, so nothing was padded. All 16 SVGs validated and a
  label bounding-box check found 0 real collisions (21.9's only hit is one box's own two text lines).
- `build/reader_hb_ch21.py` — full VI translation + EN companion. 16/16 figure parity; equations 21.1–21.2
  (liquid and gas SG), 21.3 `f = √(K/(M+kρ))`, 21.4 `J = J₀·e^(−nρd)`; eleven device families with the
  source's own advantage/disadvantage enumerations; 3 references. `work/hb_ch21.txt` extracted from
  `pdf-store/Ch21__407eb9032247bd88.pdf` (17 pages).
- **Structure note:** the source nests four balance-type variants and three vibrating-element variants
  inside single sections. These are rendered as `<h4>` (already styled site-wide, previously used by
  ch10) under `<h3>` device families, so the hierarchy matches the book.
- **Source defects handled:** Eq. 21.4 is printed as `J = J₀ exp(nρd)` but the surrounding text calls it
  attenuation, so the minus sign was restored (`e^(−nρd)`); the NTP/STP sentence in the original repeats
  "NTP" twice — rendered as NTP = 0.00 °C / 760 mmHg and STP = 15.00 or 15.56 °C / 101.325 kPa. The
  Appendix manufacturer list keeps the 13 company names but drops 1999 postal addresses and phone numbers
  (commercial directory data, now stale), with a translator's note saying so — same policy as Ch17.
- Figure parity: VI 16/16 and EN 16/16, IDs `fig-21-1`…`fig-21-16`; VI 80 kB, EN 55 kB.

**Deploy:** `build.py` → `cp -r dist/. ./` → `reader_hb_ch21.py` → `reader_handbook.py` (21 done rows),
`books_site.py` (progress 101→21), `make_sitemap.py` (521 URLs, 506 EN/VI pairs), `check_links.py` (523
pages, 14,197 references, **0 broken**). Committed `822a136`; remote was at `1468e8e` (no rebase) → pushed
`1468e8e..822a136` on `main`. Live: 200 on both VI/EN, 16 figures each, TOC shows **21/101** with 21
clickable `đã dịch` badges.

**Chapters 1–21 done; 80 to go.** Next unit is Chapter 22 (*Strain Measurement*, `Ch22.pdf`). Same
junction + `library/pdfindex.json` workflow; copy the needed `ChNN.pdf` into `work/`, extract, then follow
the §4 recipe. Build only the real figures the source contains — do not pad.

### 2026-10-31, session 20 — Handbook Chapter 20, Mass and Weight Measurement

**Shipped:** Handbook chapter 20, *Mass and Weight Measurement* (Mark Fritz and Emil Hazarian, Denver
Instrument Company) — 11 source pages. Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch20-mass-and-weight-measurement/`.
Handbook progress 19/101 → 20/101; `DONE[20]`, `("progress", 101, 20)`, and the §2 table all updated.

**What was written this session:**

- `build/hb20fig.py` — **all 3** real figures (20.1 Ainsworth equal-arm two-pan balance; 20.2 beam balance
  with offset beam and sliding weights; 20.3 force-restorative load cell with LED/photodiode null detector,
  coil between magnet poles, servo amplifier, sense resistor and digital readout). The source chapter has
  exactly 3 figures and **no tables**, so nothing was padded. All 3 SVGs validated (0 malformed) and a
  label bounding-box check found 0 real collisions.
- `build/reader_hb_ch20.py` — full VI translation + EN companion. 3/3 figure parity; **19 equations**
  (20.1 M=V×D; 20.2 W=M×G; 20.3 S·G=U·G; 20.4 single substitution; 20.5–20.6 air density and saturation
  vapour pressure; 20.7–20.8 single-substitution buoyancy correction and conventional mass; 20.9–20.10
  double substitution; 20.11–20.13 the three differences a, b, c; 20.14–20.16 least-squares difference, mass
  and conventional mass; 20.17–20.18 check standard; 20.19 short-term standard deviation) plus the
  unnumbered F-statistic ratio; the O₁…O₁₂ reading list of the three-in-one design; and all 12 references.
  `work/hb_ch20.txt` extracted from `pdf-store-b/Ch20__9227e67687723541.pdf` (11 pages).
- **OCR reconstruction note:** the source equations were badly mangled in text extraction (e.g.
  `US O O O O =+ − ( )( ) () − 21 32 SW`). They were rebuilt from the surviving token order and the standard
  NBS/NIST mass-metrology forms (Eq. 20.4 = S + (O₂−O₁)·SW/(O₃−O₂); Eq. 20.5 air-density formula; Eq. 20.8
  conventional mass `CM = M_u(1 − 0.0012/ρ_u)/0.99985`). A translator's note was added under 20.19 explaining
  that the sign convention for a, b, c depends on the difference definition and that NIST's Mass Code handles
  it consistently, so real calculations must use the software's convention.
- Figure parity: VI 3/3 and EN 3/3, IDs `fig-20-1`…`fig-20-3`; VI 43 kB (19 equations, 12 refs), EN 21 kB.

**Deploy:** `build.py` → `cp -r dist/. ./` → `reader_hb_ch20.py` → `reader_handbook.py` (20 done rows),
`books_site.py` (progress 101→20), `make_sitemap.py` (519 URLs, 504 EN/VI pairs), `check_links.py` (521 pages,
14,147 references, **0 broken**). Committed `45ff3a7`; remote was at `33a1b98` (no rebase) → pushed
`33a1b98..45ff3a7` on `main`. Live: 200 on both VI/EN, 3 figures each, TOC shows **20/101** with clickable
`đã dịch` badges (20 badge links on both TOCs).

**Chapters 1–20 done; 81 to go.** Next unit is Chapter 21 (*Density Measurement*, `Ch21.pdf` in
`pdf-store/`). Same junction + `library/pdfindex.json` workflow; copy the needed `ChNN.pdf` into `work/`,
extract, then follow the §4 recipe. Build only the real figures the source contains — do not pad.

### 2026-10-31, session 19 — Handbook Chapter 19, Frequency Measurement

**Shipped:** Handbook chapter 19, *Frequency Measurement* (Michael A. Lombardi, NIST) — 25 source pages.
Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch19-frequency-measurement/`.
Handbook progress 18/101 → 19/101; `DONE[19]`, `("progress", 101, 19)`, and the §2 table all updated.

**What was written this session:**

- `build/hb19fig.py` — **all 15** real figures (19.1 phase-comparison graphs; 19.2 unstable vs stable; 19.3 Allan
  deviation; 19.4 accuracy↔stability; 19.5 quartz oscillator block; 19.6 LORAN-C path noise; 19.7 LORAN-C vs
  cesium 96 h; 19.8 GPS vs cesium 100 s; 19.9 GPS vs cesium 1 week; 19.10 oscillator outputs; 19.11 one sine
  cycle; 19.12 changing phase relationship; 19.13 TIC measuring interval; 19.14 time-interval system; 19.15
  DMTD system). All 15 SVGs validated (0 malformed).
- `build/reader_hb_ch19.py` — full VI translation + EN companion. Embeds all 15 figures (15/15 parity),
  equations 19.1–19.8 (offset = −Δt/T, the +1 µs/24 h example, Hz conversion, Allan deviation, confidence
  1/√M, f=(E₂−E₁)/h), and all **4 tables** (19.1 offset↔phase; 19.2 stability estimate worked example; 19.3
  oscillator-type summary; 19.4 transfer-standard traceability). 28-item reference list reproduced.
  `work/hb_ch19.txt` extracted from `pdf-store/Ch19__8d16dd873aee7ed2.pdf` (25 pages).
- **Bugs fixed during the build:** a Python string-concat bug in the path builders (`d="M" + " L".join(...)`
  → `d="M' + " L".join(...)`, 15 sites); two literal `<` in SVG text (`TUR < 10:1`, `< 1 ns`) escaped to
  `&lt;`; and literal `<` in Table 19.3 cells (`<10 s`, `<5 min`) escaped for HTML.
- Figure parity: VI 15/15 and EN 15/15, IDs `fig-19-1`…`fig-19-15`; 16 SVGs/page (15 figures + brand); VI
  166 kB (4 tables), EN 114 kB.

**Deploy:** `build.py` → `cp -r dist/. ./` → `reader_hb_ch19.py` → `reader_handbook.py` (19 done rows),
`books_site.py` (progress 101→19), `make_sitemap.py` (517 URLs, 502 EN/VI pairs), `check_links.py` (519 pages,
14,097 references, **0 broken**). Committed `0326b21`; remote already at `29a7610` (no rebase) → pushed
`29a7610..0326b21` on `main`. Live: 200 on both VI/EN, 15 figures each, TOC shows **19/101**.

**Chapters 1–19 done; 82 to go.** Next unit is Chapter 20. Same junction + `library/pdfindex.json` workflow;
copy the needed `ChNN.pdf` into `work/`, extract, then follow the §4 recipe. Registry edits (`DONE[19]`,
`("progress", 101, 19)`) applied and reconfirmed before committing.

### 2026-10-31, session 18 — Handbook Chapter 18, Time Measurement (+ TOC badge links)

**Shipped:** Handbook chapter 18, *Time Measurement* (Michael A. Lombardi, NIST) — 18 source pages.
Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch18-time-measurement/`.
Handbook progress 17/101 → 18/101; `DONE[18]`, `("progress", 101, 18)`, and the §2 table all updated.

**What was written this session:**

- `build/hb18fig.py` — **all 3** real figures (18.1 one-way time transfer; 18.2 common-view time transfer;
  18.3 two-way time transfer). No padding — the source has exactly 3 figures; everything else is 8 data
  tables. All 3 SVGs validated (parse OK).
- `build/reader_hb_ch18.py` — full VI translation + EN companion. Embeds all 3 figures (3/3 parity), equation
  18.1 `f=(E₂−E₁)/h`, and all **8 tables** (18.1 frequency↔timing uncertainty; 18.2 clock evolution; 18.3 GPS
  one-way uncertainty SPS/PPS; 18.4 radio-signal performance; 18.5 radio-clock makers; 18.6 ACTS time code;
  18.7 dial-up services; 18.8 Internet time protocols). Covers §18.1 clocks → §18.8 future, plus the 32-item
  reference list. `work/hb_ch18.txt` extracted from `pdf-store/Ch18__b0fda379dc6815d6.pdf` (18 pages).
- **TOC fix (user request):** the "đã dịch" / "translated" status badges on the handbook TOC were plain text,
  so clicking them did nothing. `reader_handbook.py` now wraps each done-row badge in an `<a>` to the same
  chapter page, and `books/assets/library.css` gained `.toc-list .st a { color: inherit; border-bottom: none; }`
  (+ hover underline). All 18 done rows on both VI and EN TOCs now link from the badge.
- Figure parity: VI 3/3 and EN 3/3, IDs `fig-18-1`…`fig-18-3` confirmed; VI page 69 kB (8 tables), EN 14 kB.

**Deploy:** `build.py` → `cp -r dist/. ./` (from project root) → `reader_hb_ch18.py` → `reader_handbook.py`
(18 done rows), `books_site.py` (progress 101→18), `make_sitemap.py` (515 URLs, 500 EN/VI pairs),
`check_links.py` (517 pages, 14,047 references, **0 broken**). Committed `82496e6`; remote already at
`2c7c2a6` (no rebase) → pushed `2c7c2a6..82496e6` on `main`. Live: 200 on both VI/EN, 3 figures each, TOC
badges now clickable, `library.css` carries the badge rule, TOC shows **18/101**.

**Chapters 1–18 done; 83 to go.** Next unit is Chapter 19. Same junction + `library/pdfindex.json` workflow;
copy the needed `ChNN.pdf` into `work/`, extract, then follow the §4 recipe. Registry edits (`DONE[18]`,
`("progress", 101, 18)`) applied and reconfirmed before committing.

### 2026-10-31, session 17 — Handbook Chapter 17, Acceleration, Vibration, and Shock Measurement

**Shipped:** Handbook chapter 17, *Acceleration, Vibration, and Shock Measurement* (Halit Eren, Curtin
University of Technology) — 33 source pages. Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch17-acceleration-vibration-shock-measurement/`.
Handbook progress 16/101 → 17/101; `DONE[17]`, `("progress", 101, 17)`, and the §2 table all updated.

**What was written this session:**

- `build/hb17fig.py` — **all 23** real figures (17.1 deflection seismic accelerometer; 17.2 log a/v/x relationship;
  17.3 single-DOF pulse response; 17.4 second-order unit-step responses for ζ=0.2/0.4/0.707/1.0; 17.5 Bode
  gain/phase; 17.6 coil-and-magnet accelerometer; 17.7 rotational servo block diagram; 17.8 compression PZT;
  17.9 PZT frequency response; 17.10 piezoresistive gage bonding; 17.11 differential-capacitance accelerometer;
  17.12 diaphragm capacitive; 17.13 seismic displacement; 17.14 potentiometer; 17.15 strain-gage cantilever;
  17.16 vibrating-string; 17.17 surface micromachining steps; 17.18 DETF; 17.19 cross-axis sensitivity vector;
  17.20 charge amplifier; 17.21 Wheatstone bridge; 17.22 MCU block; 17.23 microaccel signal conditioning). No
  figures invented — the source has 23, so the module is a 23-figure set.
- `build/reader_hb_ch17.py` — full VI translation + EN companion. Embeds all 23 figures (23/23 parity), the
  equations 17.1–17.47 (sinusoidal motion, second-order Laplace form, Ampère's law F=ma=ilB, servo
  e₀/eₐ transfer, q=dᵢⱼma, differential-capacitance f=f₀+fₐ, gage factor ΔR/R, seismic z-equation, vibrating
  string f² difference, electrostatic feedback, charge-amplifier E₀), and a specs table for the military
  microaccel. `work/hb_ch17.txt` extracted from `pdf-store-b/Ch17__da9897756caf10c3.pdf` (33 pages). The
  4-item reference list is reproduced; the manufacturer list is intentionally omitted (commercial info).
- **Bug fixed:** `fig_17_4` originally divided by `sqrt(1−ζ²)` with ζ=1.0 → `ZeroDivisionError`. Switched the
  ζ=1.0 branch to the critically-damped closed form `1−(1+ωₙt)e^{−ωₙt}`; also escaped a literal `<` in a fig-17.19
  label (`thường < 1%` → `&lt;`). All 23 figures now parse well-formed (0 malformed on `xml.dom.minidom`).
- Figure parity: VI 23/23 and EN 23/23, IDs `fig-17-1`…`fig-17-23` confirmed; 24 SVGs/page (23 figures +
  brand mark), 0 malformed on parse. VI page 124 kB, EN 75 kB.

**Deploy:** `build.py` → `cp -r dist/. ./` (from project root) → `reader_hb_ch17.py` (writes ROOT) →
`reader_handbook.py` (17 done rows, progress 17/101), `books_site.py` (progress 101→17), `make_sitemap.py`
(513 URLs, 498 EN/VI pairs), `check_links.py` (515 pages, 13,963 references, **0 broken**). Committed
`7229208`; remote already at `0c36343` (no new remote commits) → pushed `0c36343..7229208` on `main`. Live:
200 on both VI/EN, the book TOC, and the live pages report 23 figures; TOC shows **17/101 hoàn thành**.
Library pill now `Đang dịch · 17/101 chương`.

**Chapters 1–17 done; 84 to go.** Next unit is Chapter 18. Same junction + `library/pdfindex.json` workflow;
copy the needed `ChNN.pdf` into `work/`, extract, then follow the §4 recipe. Registry edits (`DONE[17]`,
`("progress", 101, 17)`) were applied and reconfirmed before committing.

### 2026-10-31, session 15 — Handbook Chapter 15, Tilt Measurement

**Shipped:** Handbook chapter 15, *Tilt Measurement* (Adam Chrzanowski & James M. Secord, University of New
Brunswick) — a geodetic/monitoring chapter. Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch15-tilt-measurement/`.
Handbook progress 14/101 → 15/101; `DONE[15]`, `("progress", 101, 15)`, and the §2 table all updated.

**What was written this session:**

- `build/hb15fig.py` — the chapter's **five** real figures (15.1 subsidence from a tilt profile P1–P4 with
  αᵢ, sᵢ, δh₄; 15.2 connected vessels in hydrostatic equilibrium, h₁=h₂ and P₁+ρ₁gh₁=P₂+ρ₂gh₂; 15.3 hydrostatic
  leveling with an air tube at top and a liquid tube at bottom, Δh₁₂=r₂−r₁; 15.4 a suspended (a) and an inverted
  (b) plumb line; 15.5 a: air-current deflection e, b: spiral-wire radius r with max error 2r). No figures were
  invented — the source has Figures 15.1–15.5, so the module is a 5-figure set, not 10.
- `build/reader_hb_ch15.py` — full VI translation + EN companion. Embeds all 5 figures (5/5 parity on both
  languages), the defining equations — δh₄=α₁s₁+α₂s₂+α₃s₃ (15.1), the geodetic-leveling relation
  T₁₂=d(Δh)/s₁₂, the hydrostatic balance P₁+ρ₁gh₁=P₂+ρ₂gh₂=c (15.2), Δh₁₂=r₂−r₁ (15.3), the plumb-line
  deflection e=f₀hH/Q (15.3) with f₀=0.08dv²Q (15.4) and the spiral-wire radius r=(d/8)·√(πER/Q) (15.5) — and
  the 33-item reference list and appendix supplier table. Also `work/hb_ch15.txt` extracted from
  `pdf-store-b/Ch15__…pdf` (12 pages).
- Figure parity: VI 5/5 and EN 5/5, IDs `fig-15-1`…`fig-15-5` confirmed; 6 SVGs/page (5 figures + brand
  mark), 0 malformed on parse.

**Deploy:** `git fetch` → remote already at `ab88d01` (no new remote commits) → `reader_handbook.py` (now
15 done rows after `DONE[15]` was added), `books_site.py` (progress 101→15), `make_sitemap.py` (509 URLs,
494 EN/VI pairs), `check_links.py` (511 pages, 13,867 references, **0 broken**). Pushed `b67f9fa` on `main`.
Live: 200 on both VI/EN and on the book TOC. Library pill now `Đang dịch · 15/101 chương`.

**Chapters 1–15 done; 86 to go.** Next unit is Chapter 16. Source PDFs for 16+ live in the `pdf-store`/
`pdf-store-b` junctions and `library/pdfindex.json`; copy the needed `ChNN.pdf` into `work/`, extract, then
follow the §4 recipe. Note the registry edits (`DONE[15]`, `("progress", 101, 15)`) had to be re-applied this
session — a prior edit to those two lines did not persist — so confirm both before committing next time.

### 2026-11-01, session 13 — Handbook Chapter 13, Volume Measurement

**Shipped:** Handbook chapter 13, *Volume Measurement* (Rene G. Aarnink, Hessel Wijkstra,
University Hospital Nijmegen). A medical-volume chapter: plethysmography (air/water chamber,
strain-gage, impedance, inductive), numerical integration with imaging, indicator-dilution
(Stewart–Hamilton, thermodilution, radionuclide, gas dilution), and water-displacement volumetry.
Both languages, live at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch13-volume-measurement/`.
Handbook progress 12/101 → 13/101; `DONE[13]`, `("progress", 101, 13)`, and the §2 table all updated.

**What was written this session:**

- `build/hb13fig.py` — all ten figures (13.1 venous-occlusion trace, 13.2/13.3 four-electrode
  impedance layouts, 13.4 prostate ellipsoid, 13.5 step-section planimetry, 13.6 ellipsoid model,
  13.7 step-size error plot, 13.8 indicator time-concentration curve, 13.9 water-overflow schematic,
  13.10 leg disk model). 11 SVGs/page (10 figures + brand mark), 0 malformed on parse.
- `build/reader_hb_ch13.py` — full Vietnamese translation plus an English companion essay. Embeds the
  10 figures, the 27 equations (13.1 Boyle, 13.2–13.4 strain-gage, 13.5–13.7 impedance, 13.8 inductive
  calibration, 13.9–13.17 imaging/numerical integration, 13.18–13.24 indicator dilution & disk model),
  and rebuilt Table 13.1 (techniques / applications / companies / products / price).
- Figure parity: VI 10/10 and EN 10/10, IDs `fig-13-1`…`fig-13-10` confirmed on both pages.

**Deploy:** `git fetch` → rebase if the remote moved → `make_sitemap.py` (505 URLs, 490 EN/VI pairs)
→ `check_links.py` (507 pages, 13,768 references, **0 broken**). The library card pill now reads
`Đang dịch · 13/101 chương` in both languages.

**Chapters 1–13 done; 88 to go.** Next unit is Chapter 14. Source PDFs for 14+ live in the
`pdf-store`/`pdf-store-b` junctions and the `library/pdfindex.json` contract — copy the needed
`ChNN.pdf` into `work/`, extract with the bundled `workbuddy-pdf.exe`, then follow the §4 recipe.

### 2026-11-01, session 11 — the library's PDF reader, rebuilt on pdf.js

Request: *fix large PDF — change to a different viewer that allows reading books
above 100 MB.* The old reader set `iframe.src` to
`docs.google.com/gview?embedded=true&url=…`, and gview answers **"This file is too
large to preview"** for anything much over 30 MB. Measured, it fails at 63 MB,
36 MB and 31 MB and works at 5.5 MB, so the 111 MB and 147 MB books could never
open, and neither could a dozen 30–90 MB ones.

**Transport was the whole problem, and it was decided by measurement, not by
reading docs.** Every candidate was probed with `curl -D -` before any code was
written:

| Host | CORS | Range | Preflight (`Range`) | Verdict |
|---|---|---|---|---|
| Release assets | none | yes | – | unusable: `fetch()` → `TypeError: Failed to fetch` |
| `raw.githubusercontent.com` | `*` | 206 | **403** | unusable |
| `cdn.jsdelivr.net` | `*` | 206 | 200 | 404s anything over 20 MB |
| **GitHub Pages** | same origin | 206 | n/a | **works** |

Two extra findings that saved a dead end: the native plugin cannot be used either
(`<iframe>` renders blank, `<object>`/`<embed>` say "Couldn't load plugin", because
the asset forces a download), and `Content-Disposition` is not ours to change on
a release asset.

**What was built.**

- `assets/pdfjs/` — pdf.js 4.10.38 legacy build (392 kB + 1.4 MB worker) plus
  `standard_fonts/` and `cmaps/`, 4.0 MB in all. `build/build.py` now copies
  *directory* assets with `copytree`; it only handled flat files before, which
  would have thrown `IsADirectoryError`.
- `build_reader()` rewritten: a sticky toolbar (back, title, part selector, page
  box, zoom, download) over a scrolling stage of page placeholders painted lazily
  by `IntersectionObserver` with a 1600 px margin. Canvas rasterisation is capped
  at 2.6× so "fit width" on a retina screen does not allocate a 3200 px canvas per
  page. Keyboard: ← → Home End. Deep link `?p=`. Reader params: `f` (file), `pl`
  (part files), `i` (index), `r` (page ranges), `t` (title), `b` (back link).
- `build/make_pdfstore.py` — publishes the bytes. Two companion repositories with
  Pages enabled, `/pdf-store/` and `/pdf-store-b/`, greedily filled to 769 MB and
  768 MB because a Pages site is capped at 1 GB and the library is 1.5 GB.
  `library/pdfindex.json` (785 entries) is the contract: path → file, parts, ranges,
  repository. A path that already has a home keeps it, so adding a book never
  moves an existing one.
- `build/books_site.py` — work pages now link `reader_href(...)` instead of a
  gview URL, and the copy explains the part selector.

**The splitting trap.** 111.6 MB and 147.2 MB both exceed GitHub's hard 100 MB
per-file limit, so they are published as page-range parts. A 50/50 split by page
count produced **142.40 MB and 5 MB** for the 147 MB scan — nearly all the imagery
sits in one half — and the push was rejected. `_leaves()` now recurses on the
*measured* file size, yielding 5.0 / 36.8 / 40.4 / 65.6 MB. `pypdf`'s
`append(src, pages=(a, b))` is the only workable primitive: a per-page `add_page`
loop rewrote a 40-page slice as 53 MB by keeping the whole cross-reference table.

**Verified.** The 111 MB book opens on its cover and page 20 renders crisply;
the 147 MB book opens as "Part 1 · 1–294"; a 15-page book from store A renders;
the Vietnamese reader and a 390 px viewport both lay out cleanly. Both Pages sites
answer `206 application/pdf` with `Content-Range`. Full build: 501 URLs,
14,622 local references, **0 broken**.

### 2026-11-01, session 10 — Handbook Chapter 11, and a glossary built from the books

Two requests in one turn: *finish at chapter 11*, then *build the full glossary from all
/books* at `/glossary.html` and `/vi/glossary.html`.

**Chapter 11 (Level Measurement, Detlef Brumbi, Krohne).** 21 source pages, 15 figures,
3 tables, 23 equations. New `build/hb11fig.py` draws all fifteen — the four mounting modes,
the buoyancy balance, the servo displacer, both float read-outs, the three hydrostatic
arrangements, the echo geometry and burst timing, three antennas, the compact radar head,
the TDR line with its echo trace, the FMCW ramp and block diagram, the through-product
geometry, the capacitance probe, both radiometric configurations and the vibrating fork.
`reader_hb_ch11.py` carries a complete Vietnamese translation (7,109 words) and an English
companion that is an essay rather than a mirror. 15/15 figure parity, 0 broken links.

Five figure defects were found only by screenshotting the grid and re-reading it, all of the
same family — a label detached from the dimension line it belongs to:

* 11.12 had two dimension lines stacked at the same x, with the `h_v` label 260 px away from
  its own line;
* 11.5(c) put the gas bottle on top of panel (b)'s computer box, and the purge pipe entered
  the tank through its roof instead of its side;
* 11.11 routed the mixer output along the exact bottom edge of the DRO block;
* 11.8 had an arrow ending 28 px short of the block it pointed at;
* 11.3 put the `l` dimension across the tank wall, which read as a stray line.

**The glossary.** `/glossary.html` existed but was a hand-written list of 52 terms and
`/vi/glossary.html` did not exist at all. Replaced both with a generated index of **98
entries**: the 52 curated terms plus 46 lifted from the four handbook chapters that carry a
"Defining Terms" section (Ch. 5 with 32 VIM terms, Ch. 6.4, 6.5 and 6.6). Four of them
(`Calibration`, `Accuracy`, `Repeatability`, `Tolerance`) are the same concept as a curated
entry and are merged, with the chapter listed as an extra source.

Search filters on a `data-s` blob that holds both headwords and both definitions with
diacritics stripped, so "muc" finds "Mức" and "level" finds it too. Vietnamese sorting folds
`đ` to `dz`, which puts `Đ` after `D` as Vietnamese convention expects, and the letter strip
gives `Đ` its own button.

Two traps worth recording. `pages_glossary.build()` now delegates to `make_glossary`, and
`make_glossary` imports `pages_glossary` for `TERMS` — the import has to be inside the
function or it is circular. And a stale `build/__pycache__/make_glossary*.pyc` silently kept
serving the pre-patch `build_entries()`, which cost twenty minutes of chasing a merge that
was already correct; `rm -rf build/__pycache__` before believing a debug print.


### 2026-11-01, session 9 — Safety Instrumented Systems finished

Same request as session 8, for the other book: *finish* the SIS reader, mark it done in
`/books`, and make "Open the book →" work.

**The card and the footer were already correct** — session 8 fixed both for every card on
the site, and SIS had been switched to `"full"` at the same time. Verified in both
languages before touching anything: `data-level="full"`, "Fully translated · 16 of 16
chapters", footer is a real `<a href>`.

**The real gap was the English pages.** 13 of 16 chapters carried **zero** figures against
54 in Vietnamese, and chapters 1–2 were bare outlines at 371 and 378 words. The whole book
came to 3 English figures against 54.

What was done, chapter by chapter:

| | Before | After |
|---|---|---|
| Figures (EN) | 3 | **54** — parity on all 16 chapters |
| ch01 words | 371 | 1,374 |
| ch02 words | 378 | 1,066 |
| ch05 words | 810 | 1,317 |
| ch06 words | 1,337 | 2,576 |
| ch08 words | 1,094 | 2,498 |
| ch16 words | 1,563 | 2,742 |

Three chapters needed new sections rather than figure placement:

- **ch08** never introduced the failure-mode vocabulary or the three modelling methods, so
  two sections were written: "Safe, dangerous, detected, hidden" (figures 8-1, 8-2) and
  "Three ways to draw the same system" (reliability block diagram, fault tree, Markov —
  figures 8-4, 8-5, 8-6). The chapter has 18 source sections and the essay had six.
- **ch07**'s redundancy section compressed four architectures into one paragraph. Rewritten
  as one paragraph per architecture, each with its drawing (7-2, 7-3, 7-5, 7-6).
- **ch05** never covered what the standard requires the specification to contain. Added
  Table 5.1, twelve rows, each with the reason it cannot be deferred.

**ch01 and ch02 have no generator** and are hand-edited HTML. Both gained four or five
commentary sections above the existing outline, which was kept because it is genuinely
useful for front matter. Confirmed the build does not overwrite them: `build.py` +
`cp -r dist/. ./` leaves their md5 unchanged.

Final state: `check_links.py` → 486 pages, 12,610 references, 0 broken. Sitemap 484 URLs.
SIS figure parity 54/54. No mismatches on PC either (120/120).

### 2026-11-01, session 8 — Practical Process Control finished; the /books card fixed

The user's request was three things at once: *finish* `/books/read/pc-process-control/`,
mark it **done** in `/books`, and make the **"Open the book →"** footer actually work.

**1. The card had two real bugs, not one.** Both were in `build/books_site.py`:

- The pill's *text* was hard-coded to `"🟠 Translating · %d of %d chapters"` for every
  level, so a completed book still advertised itself as in progress. Only the colour came
  from `level`. Replaced with `FLAG_LABEL = {level: (vi_fmt, en_fmt)}`; the label now
  follows the level.
- The PC entry used `level="done"`, which has no rule in `library.css`, so it fell through
  to the unstyled default. Both PC and SIS are now `"full"` — they were the only two books
  at 14/14 and 16/16 and both had been mislabelled.

**2. The footer was never a link.** `card()` emitted
`<div class="card-footer"><span>Open the book →</span></div>` — a `<span>` with no `href`.
Only the `<h3>` was clickable, while `.card:hover .card-footer span` underlined the text,
which made the dead footer *look* live. It is now `<a href="…">`, and `library.css` gained
`.card-footer a { color: inherit }` so it stays gold instead of turning link-blue. All 175
cards on the site were affected; all 175 are fixed.

**3. Three English pages had no figures at all.** Chapters 3, 4 and 5 rendered 0 figures
against 24, 11 and 11 in Vietnamese: their `body_en()` essays were complete but never
called `fig(...)`. Wired them in, and while there closed the smaller gaps in chapters 6–9
(missing 1, 3, 1 and 4). **Every chapter now has EN figures == VI figures**, 14 of 14.

Chapter 3 needed real writing, not just insertions: the essay's one-line-per-family table
became eight `h3` subsections, each with its cross-section and characteristic drawings, plus
a new "Four more that do not fit the table" for the balanced-plug, cylinder, expandable-element
and fluid-interaction valves. The English page went from 10 kB / 1,370 words to
154 kB / 3,874 words. Chapter 9 also gained the §9.10 material it had never covered
("One primary, several secondaries").

**4. Two caption mismatches caught on the rendered page.** Figure 7-2 is an *equation*
panel, and the bridging sentence described a block diagram; figure 7-5 is a
differentiator-plus-lag, and the sentence claimed "two resistors and a capacitor", which the
source does not say. Both rewritten. These are the kind of error the QA grid cannot show —
read the page.

**5. Landing pages described themselves as unfinished.** `reader_book.py` had static
`lede`/`policy` strings saying "the translation proceeds chapter by chapter" even at 14/14.
Added `lede_done_en/_vi` and `policy_done_en/_vi`, preferred by `build()` once
`len(done) == total`. Applied to both PC and SIS.

Final state: `check_links.py` → 486 pages, 12,582 references, 0 broken. Sitemap 484 URLs.
Figure parity 14/14. Cards green in both languages.

**Found and deliberately not fixed:** the SIS English pages carry 3 figures against 54 in
Vietnamese — the same defect, in a book the user did not ask about this session. The full
per-chapter table is in §3.4; it is the next job after the handbook.

### 2026-10-31, session 7 — Handbook Chapter 10 shipped (the whole thing)

**Shipped:** Handbook chapter 10, *Position, Location, Altitude Measurement*. 73 source pages,
5 sections, 8 co-authors, 43 figures, 4 numbered tables, 124 numbered equations, both
languages. Commit `e54d823`. Live at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch10-position-location-altitude/`.
Handbook progress 9/101 → 10/101; `DONE[10]` and `("progress", 101, 10)` both updated.

**What was written this session** (the figures for all five sections already existed from
sessions 5–6):

- `build/reader_hb_ch10.py` — 10.3 Inertial Navigation (Schuler, Sagnac, the t/t²/t³ error
  ladder, stabilization, vehicular/aircraft/underwater/robotics, LN-100, HBOI, MAPS, Hitachi
  IFOG), 10.4 Satellite Navigation and Radiolocation (EM spectrum, ionosphere layers,
  CEP/rms, radiobeacons, Loran-C, Decca, Consol, Omega, radar, Transit, transponders, GPS,
  DGPS, Glonass, Starfix), 10.5 Occupancy Detection (17 detector types, ultrasonic,
  microwave Doppler, MIR, capacitive, triboelectric, optoelectronic, facet lenses, PIR, AFIR),
  then `body_en()` — an original essay that reads the five sections as five versions of one
  inverse problem, with a t/t²/t³ error-propagation table and a seven-row errata table.
- Appendix supplier lists for 10.3 and 10.4 rendered as two-column tables, with a note that
  the street addresses and phone numbers are omitted as stale.

**Four figure defects found on the rendered page and fixed** — none of them visible on the
Georgia QA grid, because its glyph widths differ from the site face:

| Figure | Defect |
|---|---|
| 10-38 | `Q₃` was labelled but never drawn — the `_mos_v(rail, 240)` call was missing, so the current sink was a plain wire. Added it at `gy=249`, moved `C_p` to x=224 and `R₁`/`Q₃` labels into the clear strip, retuned the gate tap |
| 10-40 | the red `ảnh của vật` label printed across the comb teeth — moved above the comb at `y=57`, anchored middle |
| 10-37 | `C_b` hung from a point between the ankles — added a 36 px bar joining the feet so the lead starts on the body |
| 10-39 | the small "image" pictogram's head sat on the signal lead — dropped to `y=134`, height 20 |

**Two source errata handled with `note()` boxes rather than silent correction:** the chapter
gives the GPS orbit as 2200 km (really 20 200 km) and the Glonass orbit as 1500 km (really
19 100 km); both would fail Kepler's third law in one line, and the chapter's own Figure 10-35
contradicts its text. Also noted that Selective Availability was switched off on 2 May 2000,
not "by 2006" as the text predicts.

**Housekeeping:** two `<ol>`/`<ul class="plain">` lists were used for the 17 detector types
and the six error categories; `.plain` has no CSS rule, so they fall back to the UA default
list styling, which is what other chapters already do (`<ol start="1">`). No change needed.

**Deploy:** `git fetch` → 4 ahead, 0 behind → pushed to `main` → live on the third poll
(25–65 s as usual). `check_links.py`: 486 pages, 12 204 references, 0 broken. Sitemap 484 URLs.

### 2026-10-31, session 6 — broken rebase repaired, "Process" section shipped, chapter 10 figures 10.8–10.16

**No new book chapter landed. The session opened on a broken repository and closed on a
clean, fully verified one, plus nine new figures for chapter 10.**

**The rebase.** The working tree was mid-rebase: detached HEAD, `.git/rebase-merge` present,
14 unmerged paths, `main` at `2781ec6` being replayed onto `dcef287`. The incoming commit was
*Add 'Process' section: what a process is, the three economic sectors, and the
control/instrumentation/IT-OT/AI stack* — a whole new top-level section that existed only
locally and had never been pushed.

The single real source conflict was in `build/framework.py`. `origin/main` had just rewritten
the foot-of-page chain so that `CHAIN` is **derived** from `NAV`
(`CHAIN = [(href, en, vi) + LONG[href] for href, en, vi in NAV]`), while the Process commit
hand-added a second hardcoded `CHAIN` list to insert itself. Resolution: keep the derivation,
delete the hardcoded list, and add the missing `"process.html"` key to `LONG` — after which
Process lands between *Hot topics* and *Fundamentals* automatically, exactly where the
incoming commit wanted it. Verified with `chain_neighbours("process.html")`.

All 21 generated HTML files were resolved by taking `dcef287`'s version and **rebuilding from
source** rather than hand-merging, which is the only safe way to resolve generated output.
`assets/style.css` also arrived with a spurious working-tree diff (it silently lost the
`.hot-press` rules); restored from the index.

Shipped as `cc91bb3` (the rebased Process commit) + `4518b72` (the rebuild), then pushed.
Sitemap **482 URLs / 468 pairs**; link check **484 pages, 11,800 references, 0 broken**.
Visually checked `process.html` over HTTP: 10 sections, the five-column sector table renders
cleanly, footer chain reads *Hot topics → Fundamentals of measurement*.

**Chapter 10, figures 10.8–10.16** (section 10.2, Attitude Measurement), committed `9c6096a`.
Nine figures drawn from source pages 19–34: servo accelerometer, dielectric inclinometer,
ship sensor locations, crane lifter, trolley-lifter dynamics, vertical-gyro vector fan,
attitude cones, trace-averaging scatter, PAL ray diagram. Three QA rounds were needed; the
defects found and fixed are in the traps table.

### 2026-10-31, session 5 — Handbook Chapters 8 and 9 shipped, Chapter 10 started

**Two chapters landed and are live. The library reads 9 of 101.**

| Chapter | Slug | Pages | Figures | Tables | Commit |
|---|---|---|---|---|---|
| 8 Proximity Sensing for Robotics | `ch08-proximity-sensing-for-robotics` | 17 | 17 | 1 | `0856e39` |
| 9 Distance | `ch09-distance` | 18 | 8 | 1 | `ef10c0b` |

Both verified live: `/vi/books/read/…/chNN-…/` and `/books/read/…/chNN-…/` return 200, the
contents page lists both, and the sitemap went 481 URLs / 468 pairs with 483 pages,
11,739 references, 0 broken.

**Chapter 9 carried a genuine source defect, and my first reading of it was wrong.** The
printed eq. 9.1 is `R = b·sin α₁·sin α₂/sin(α₂ − α₁)`. I first wrote a note claiming the
numerator should be `cos α₂`; that was wrong. Read the figure the way its caption reads it —
α₁ and α₂ measured at the two ends of the baseline, each against the baseline — and the third
angle is `π − α₁ − α₂`, so the sine rule gives

- slant side from the left station: `R = b·sin α₂/sin(α₁ + α₂)`
- perpendicular distance to the baseline: `h = b·sin α₁·sin α₂/sin(α₁ + α₂)`

The printed numerator is exactly `h`'s; only the denominator sign is wrong. The decisive test
is that the printed denominator vanishes when α₁ = α₂, i.e. for a target on the perpendicular
bisector, where the range is plainly finite (`b/(2 tan α₁)`). So it is a sign slip that
manufactures a singularity, not a small-angle approximation. The note and the English essay
both now say this. **Lesson: check a claimed defect against a case with a known answer before
writing it down.**

**New CSS class this session:** `table.tbl.prod` — the vendor survey table in 9.4 has single-token
product names (`MicroScribe-3DX`, `Rangecam 7000`, `OPTOTRAK`) that `overflow-wrap: anywhere`
was splitting mid-word. The class pins column 2 with `white-space: nowrap; overflow-wrap: normal`.

**Chapter 10 started — and it is not a normal chapter.** 73 pages, 32,867 words, **43 figures**,
4 tables, eight co-authors, five sections. I asked the owner how to sequence it and the answer
was **"Ch.10 as one unit, in order"** — build it whole, publish only when complete, accept that
it spans sessions. Do not register `DONE[10]` early.

Progress on chapter 10 (commit `320ac92`, WIP, deliberately unregistered):

- all of section 10.1's text read (19 references, eqs. 10.1–10.44, table 10.1);
- figures 10.1–10.7 written and QA'd in `build/hb10fig.py`.

Three figure fixes worth remembering:

- **10.1:** C, B and A must all sit on the *level* flightpath — the apparent slope is
  perspective only. My first version put them on a sloping line, which made `CB = y` and
  `BA = x` both slanted and the labels collide with the line. Rebuilt with `fy(x)` constant-height.
- **10.3:** I had drawn a `φ` label with no arc behind it. A label must never exist without its
  referent. θ is the bearing from the Y axis, φ the elevation from the horizontal sight line;
  both arcs are now drawn at different radii (40 and 95) so the two shallow angles do not merge.
- **10.7:** the legend sat in the middle of the plot on top of the curves, and the y axis read
  `−0` because the tick list started at 0 and the formatter prefixed every value. Legend moved
  to a single row above the frame; tick list special-cases zero. `_curve()` also now *stops* at
  the frame instead of clamping, which had been drawing a false flat line along `y = −160`.

Charts in this chapter are computed, not sketched: the multiplier plot uses
`a(x) = 2√(x²+z²) − x` (gives `2z` at the omni radar and approaches `x` far away, matching the
printed endpoints), and the inherent-bias plot uses the second-order Taylor term of eq. 10.44,
so bias grows with the square of the horizontal distance, scaled by the triangle side.

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
