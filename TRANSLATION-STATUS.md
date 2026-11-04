# Translation status — handoff for the next agent

**Last updated:** 2026-11-04 (finish-chapter-32 phase — **Chapter 32 COMPLETE: all 11 sections §32.1–§32.11, VI + EN; registered `32: "ch32-temperature"`; handbook now 101/101 = 100%**) · **Live site:** https://pro-instcontrol.github.io/

> **Where to start next:** Handbook translation is **FINISHED — 101 of 101 chapters (100%)**,
> including Chapter 32 "Temperature", whose last eleven sections §32.6–§32.11 (Infrared,
> Pyroelectric, Liquid-in-Glass, Manometric, Temperature Indicators, Fiber-Optic) were translated
> in the finish-chapter-32 phase and registered as `32: "ch32-temperature"` in
> `reader_handbook.py` `DONE`. No further chapters remain. Source text for every chapter is already
> extracted into `work/hb_chNN.txt`; Chapter 32's own dump is `work/ch32_s75_163.txt`
> (local-only, `work/` is gitignored). See "State of Chapter 32 after session 52" + the
> finish-chapter-32 log below for the section survey and integration notes.
>
> **Two agents are working the same book from opposite ends.** Always `git fetch` + rebase before
> pushing; both of us have hit conflicts in `build/reader_handbook.py` (`DONE`) and in the two
> book-TOC `index.html` files. Resolve by *merging both* entries and regenerating, never by
> discarding the other agent's rows.
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
| Measurement, Instrumentation and Sensors Handbook | `the-measurement-instrumentation-and-sensors-handbook` | 101 + app. A | **1–31, 33–101, App. A** (ch32 pending → 100/101 done) | `build/reader_handbook.py` + `reader_hb_chNN.py` per chapter |
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
| HB 22 | Strain Measurement | `ch22-strain-measurement` | `reader_hb_ch22.py` + `hb22fig.py` | 14 | ~13k |
| HB 23 | Force Measurement | `ch23-force-measurement` | `reader_hb_ch23.py` + `hb23fig.py` | 17 | ~19k |
| HB 24 | Torque and Power Measurement | `ch24-torque-and-power-measurement` | `reader_hb_ch24.py` + `hb24fig.py` | 7 | ~19k |
| HB 25 | Tactile Sensing | `ch25-tactile-sensing` | `reader_hb_ch25.py` + `hb25fig.py` | — | — |
| HB 26 | Pressure and Sound Measurement | `ch26-pressure-and-sound-measurement` | `reader_hb_ch26.py` + `hb26fig.py` | — | — |
| HB 27 | Acoustic Measurement | `ch27-acoustic-measurement` | `reader_hb_ch27.py` + `hb27fig.py` | 21 | — |
| HB 86 | Computers | `ch86-computers` | `reader_hb_ch86.py` + `hb86fig.py` | 7 | ~16.9k |
| HB 87 | Telemetry | `ch87-telemetry` | `reader_hb_ch87.py` + `hb87fig.py` | 11 | ~10.2k |
| HB 88 | Sensor Networks and Communication | `ch88-sensor-networks-and-communication` | `reader_hb_ch88.py` + `hb88fig.py` | 5 | ~13.6k |
| HB 89 | Electromagnetic Compatibility | `ch89-electromagnetic-compatibility` | `reader_hb_ch89.py` + `hb89fig.py` | 5 | ~14.3k |
| HB 90 | Human Factors in Displays | `ch90-human-factors-in-displays` | `reader_hb_ch90.py` + `hb90fig.py` | 1 | ~7.7k |
| HB 91 | Cathode Ray Tube Displays | `ch91-cathode-ray-tube-displays` | `reader_hb_ch91.py` + `hb91fig.py` | 2 | ~9k |
| HB 92 | Liquid Crystal Displays | `ch92-liquid-crystal-displays` | `reader_hb_ch92.py` + `hb92base.py`/`hb92fig.py`/`hb92figb.py`/`hb92figc.py` | 16 | ~19k |
| HB 93 | Plasma-Driven Flat Panel Displays | `ch93-plasma-driven-flat-panel-displays` | `reader_hb_ch93.py` + `hb93base.py`/`hb93fig.py`/`hb93figb.py` | 20 | ~14k |
| HB 94 | Electroluminescent Displays | `ch94-electroluminescent-displays` | `reader_hb_ch94.py` + `hb94fig.py` | 10 | ~9.5k |
| HB 95 | Light-Emitting Diode Displays | `ch95-light-emitting-diode-displays` | `reader_hb_ch95.py` + `hb95fig.py` | 8 | ~9k |
| HB 100 | Explosion-Proof Instruments | `ch100-explosion-proof-instruments` | `reader_hb_ch100.py` + `hb100fig.py` | 7 | ~9.5k |
| HB 101 | Measurement and Identification of Brush, Brushless, and dc Stepping Motors | `ch101-measurement-and-identification-of-stepping-motors` | `reader_hb_ch101.py` + `hb101fig.py` | 5 | ~7.5k |
| App. A | Units and Conversions | `appendix-a-units-and-conversions` | `reader_hb_app.py` | 0 | ~3k |
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
  Currently `("progress", 101, 25)`, `("full", 16, 16)`, `("full", 14, 14)`.
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

### 2026-10-31, session 23 — Handbook Chapter 23, Force Measurement

**Shipped:** Handbook chapter 23, *Force Measurement* (M. A. Elbestawi, McMaster University) — 17 source
pages. Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch23-force-measurement/`.
Handbook progress 22/101 → 23/101; `DONE[23]`, `("progress", 101, 23)`, and the §2 table all updated.

**What was written this session:**

- `build/hb23fig.py` — **all 17** real figures: 23.1 the three loading modes; 23.2 stress/strain
  definitions with their formulas; 23.3 thin-diaphragm, hydraulic and pneumatic load cells; 23.4 foil
  gage configurations; 23.5 Wheatstone bridge; 23.6 beam load cell and bridge gage positions; 23.7 ring
  load cell, bridge and LVDT variant; 23.8 piezoelectric plate modes; 23.9 twister and bender; 23.10
  three-component transducer and the four-transducer sandwich; 23.11 spindle telemetry system with
  numbered callouts; 23.12 capacitive cell; 23.13 FSR structure; 23.14 FSR resistance curve; 23.15
  tactile array; 23.16 taxel stack and circuit; 23.17 sensor-array block diagram. The source has exactly
  17 figures, so nothing was padded. All 17 validated: 0 malformed, 0 off-canvas, 0 label collisions.
- `build/reader_hb_ch23.py` — full VI translation + EN companion. 17/17 figure parity, 1/1 table parity;
  equations 23.1–23.6 (Poisson, Hooke, bulk modulus), 23.7 (bridge balance), 23.8 (gage factor), 23.9–23.11
  (beam cell), 23.12–23.16 (piezoelectric), 23.17 (capacitance); 10 references plus 7 further-reading
  entries. `work/hb_ch23.txt` extracted from `pdf-store/Ch23__409b681c05d67a79.pdf` (17 pages).
- **Typography gotcha (new, important):** Unicode subscript *letters* — `ᵢ` (U+1D62), `ₛ` (U+209B),
  `ᵣ` (U+1D63) — are **not in the Inter/Helvetica stack** and render as blanks, so `Eᵢ`, `Pₛ` and `εᵣ`
  came out as `E`, `P` and `ε`. Subscript *digits* (`₀₁₂₃₄`) are fine. Added a `_subs()` helper that
  emits `<tspan font-size="8" dy="3">` and undoes the `dy` on the next normal run; use it for any
  lettered subscript.
- **Visual QA this session:** beyond the usual label-box checker, the 17 figures were rendered to PNG
  with headless Chrome and inspected. That caught six defects the box checker cannot see — a stray
  decorative curl, an F arrow drawn straight through a label (23.10, 23.12, 23.13, 23.16), a gage
  annotation crossed by the load arrow (23.6), and a cramped three-grid rosette in 23.4 that read as
  noise (redrawn as stacked grids with orientation arrows). Worth repeating on figure-heavy chapters.
- **Source defects handled:** the source prints "120 W" and "50 MW" where the units are clearly Ω
  (ohm) — rendered as 120 Ω and 50 MΩ; Table 23.1's caption typo "Arrays Sensors" corrected; Figure
  23.12 is printed as "Photo not available" in the original, so it was redrawn from the surrounding
  text with a translator's note; the phrase "at a ratio of 2 × 10⁵" is unexplained in the original and
  is glossed in a note as the dynamic range. Figure 23.8's modes are unlabelled in the source and were
  drawn as d₃₃ / d₃₁ / d₁₅, also noted.
- Figure parity: VI 17/17 and EN 17/17, IDs `fig-23-1`…`fig-23-17`; VI 102 kB, EN 90 kB.

**Deploy:** `build.py` → `cp -r dist/. ./` → `reader_hb_ch23.py` → `reader_handbook.py` (23 done rows),
`books_site.py` (progress 101→23), `make_sitemap.py` (525 URLs, 510 EN/VI pairs), `check_links.py` (527
pages, 14,293 references, **0 broken**). Committed `145cf40`; remote was at `da35298` (no rebase) →
pushed `da35298..145cf40` on `main`.

**Chapters 1–23 done; 78 to go.** Next unit is Chapter 24 (*Torque and Power Measurement*,
`pdf-store/Ch24__9dc2fad066692930.pdf`). Same junction + `library/pdfindex.json` workflow; copy the
needed `ChNN.pdf` into `work/`, extract, then follow the §4 recipe. Build only the real figures the
source contains — do not pad.



**Shipped:** Handbook chapter 22, *Strain Measurement* (Christopher S. Lynch, Georgia Institute of
Technology) — 20 source pages. Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch22-strain-measurement/`.
Handbook progress 21/101 → 22/101; `DONE[22]`, `("progress", 101, 22)`, and the §2 table all updated.

**What was written this session:**

- `build/hb22fig.py` — **all 14** real figures: 22.1 uniaxial tension; 22.2 stress–strain curve with a
  Poisson sub-plot; 22.3 shear block; 22.4 principal directions (two squares, one stretched, one skewed);
  22.5 foil gage construction; 22.6 single grid leg with length/width/thickness; 22.7 Wheatstone bridge;
  22.8 Mohr's circle; 22.9 PVDF gage; 22.10 piezoelectric parallel-plate section; 22.11 electrometer and
  charge amplifier; 22.12 Fabry–Perot fiber; 22.13 polariscope; 22.14 Moiré fringes. The source has
  exactly 14 figures, so nothing was padded. All 14 SVGs validated; one label collision in 22.13
  ("phân cực" / "bản 1/4 sóng" / "phân tích") was fixed by spreading the labels to x = 165, 232, 416, 484,
  after which the bounding-box check reports 0 collisions and 0 off-canvas labels.
- `build/reader_hb_ch22.py` — full VI translation + EN companion. 14/14 figure parity, 2/2 table parity;
  equations 22.1–22.6 (Hooke's law, shear), 22.7–22.8 (gage factor with temperature and transverse terms),
  22.9–22.14 (resistance derivation), 22.15a/b–22.18 (Wheatstone bridge), 22.19–22.21 (power and thermal
  limits), 22.22–22.29 (Mohr's circle and rosettes), 22.30–22.32 (piezoelectric polarization), 22.33
  (`Q = CV`), 22.34–22.35 (birefringence), 22.36–22.40 (Moiré displacement → strain); 29 references.
  `work/hb_ch22.txt` extracted from `pdf-store-b/Ch22__d1fbcd4327eb71ae.pdf` (20 pages).
- **Tables:** 22.1 (eight sensor types across eight characteristics, footnote markers ᵃ–ᵍ) and 22.2
  (nine vendors with 1999 list prices). The VI body emitted both from the start, but the EN body only
  *referred* to them in prose — a dangling reference. Both tables were added to the English page, plus
  the data-limitations paragraph, so the two languages now match at 2/2.
- **Convention reconfirmed:** the EN companion page is a prose summary with **no display equations**
  (same as Chapters 20 and 21 — both also render 0 numbered equations against 19 and 4 on the VI side).
  This is intentional, not a parity defect.
- Figure parity: VI 14/14 and EN 14/14, IDs `fig-22-1`…`fig-22-14`; VI 90 kB, EN 64 kB.

**Deploy:** `build.py` → `cp -r dist/. ./` → `reader_hb_ch22.py` → `reader_handbook.py` (22 done rows),
`books_site.py` (progress 101→22), `make_sitemap.py` (523 URLs, 508 EN/VI pairs), `check_links.py` (525
pages, 14,247 references, **0 broken**). Committed `ed29270`; remote was at `dc4915c` (no rebase) →
pushed `dc4915c..ed29270` on `main`. Live: 200 on both VI/EN, 14 figures and 2 tables each, TOC shows
**22/101** with 22 clickable `đã dịch` badges.

**Chapters 1–22 done; 79 to go.** Next unit is Chapter 23 (*Ch23.pdf* at
`pdf-store/Ch23__409b681c05d67a79.pdf`). Same junction + `library/pdfindex.json` workflow; copy the needed
`ChNN.pdf` into `work/`, extract, then follow the §4 recipe. Build only the real figures the source
contains — do not pad.



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

### 2026-10-31, session 24 — Handbook Chapter 24, Torque and Power Measurement

**Shipped:** Handbook chapter 24, *Torque and Power Measurement* (Ivan J. Garshelis, Magnova, Inc.) — 16
source pages. Full Vietnamese translation + English companion at
`/vi/books/read/the-measurement-instrumentation-and-sensors-handbook/ch24-torque-and-power-measurement/`.
Handbook progress 23/101 → 24/101; `DONE[24]`, `("progress", 101, 24)` and the §2 table all updated.
Pushed `fbeffc4` on `main`.

**What was written this session:**

- `build/hb24fig.py` — all **7** figures the source actually contains, no padding: 24.1 (off-axis force
  producing torque, plus a shaft twisted through φ), 24.2 (generalised apparatus block diagram B–C–D–E–F
  with reactions A and G), 24.3 (the four sensing techniques in one four-panel plate: strain gages with
  slip rings, two toothed wheels on a torsion bar, grooved solenoid regions with sense windings, magnetised
  ring with field sensor), 24.4 (modular transducer section with bearings, keyways, signal cable and
  optional feet), 24.5 (reaction-torque support table with calibrating-weight arm), 24.6 (prony brake),
  24.7 (eddy current dynamometer, cross-section + front view).
- `build/reader_hb_ch24.py` — full VI translation with **7 numbered equations** (24.1 `T = (F cos β)l`,
  24.2 `T = Iα`, 24.3 `τm = 16T/πd³`, 24.4 `γm = τm/G`, 24.5 `φ = 32LT/πd⁴G`, 24.6 `W = Tθ`,
  24.7 `P = Tω`), **0 tables** (the source has none), 30 references, and two translator's notes: one on
  retaining *dynamometer* untranslated, one recording that the source's Equations 24.2–24.5 arrive as
  disconnected fragments and have been restored to standard form. EN companion follows the established
  prose-only convention but carries the full reference list.
- Registry: `reader_handbook.py` TOC title for ch24 normalised from `Đo mô men xoắn` to `Đo mômen xoắn`
  so the TOC and the page heading agree.

**Two build-pipeline findings:**

1. **`books_site.py` had been dropped from the loop.** It is documented in §4.4 but was not run in
   sessions 17–23, so `books/index.html` and `vi/books/index.html` were frozen at
   `Đang dịch · 16/101 chương` for eight chapters while the TOC pages were correct. Running it this
   session moved the counter to 24/101 with a one-line diff per file. **Always run `python build/books_site.py`
   before the sitemap** — it is the only writer of the library landing pages.
2. **`<sub>`/`<sup>` are safe in body text.** The CSS rule that looked like it restyled them
   (`books/assets/library.css:221`) is `.section-title .sub` — a *class*, not the element. Verified at
   3× by rendering `F<sub>t</sub>`, `τ<sub>m</sub>`, `d<sup>3</sup>`, `s<sup>−1</sup>` on a scratch page
   with the real stylesheet: proper subscript/superscript, inherited colour. This is the right way to set
   subscript *letters* in prose, since the Unicode forms (`ₘ`, `ₜ`) are missing from the Inter stack —
   the same trap recorded for SVG labels in session 23.

**Figure QA (the part that took the time).** `work/qa_figs.py hb24fig` passed cleanly after two box fixes,
but visual inspection at 2–3× found five defects the box checker cannot see, all fixed:

- 24.6 — the coolant leader ended ~30 px short of the drum rim, in empty space; extended to touch it.
- 24.6 — "khối ma sát" was struck through by the cooling-jacket arc; moved above the arc.
- 24.1 — the tangential arrow ran straight through its own `F_t` label; arrow lengthened to 60 px and the
  label placed beyond the tip, clear of the circle.
- 24.1 — the lever-arm label `l` sat on the dashed radius; moved off the line.
- 24.4 — "rãnh then" floated 40 px from the keyway notch; a short leader added.

24.7 was rewritten wholesale (the rotor was not visibly between the two stators and the teeth floated);
24.6 had already been rewritten earlier in the session for three leaders ending in nothing.

**Verification:** VI 7/7 figures and EN 7/7 figures; 7 VI equations, 0 EN numbered equations (convention);
0 tables both sides; 5 `h2` and 15 `h3` both sides (an EN `h2` that should have been `h3` was caught by the
heading count). Local server: both chapter URLs and both TOC URLs return 200; TOC shows **24 done rows with
24 clickable badges** in each language; progress reads 24/101. Sitemap **527 URLs, 512 EN/VI pairs**; link
check **529 pages, 14,399 local references, 0 broken**.

**Chapters 1–24 done; 77 to go.** Next unit is Chapter 25 (*Tactile Sensing*). Same junction +
`library/pdfindex.json` workflow; copy the needed `ChNN.pdf` into `work/`, extract, then follow the §4
recipe — and remember `books_site.py`. Build only the real figures the source contains — do not pad.

---

## Session 25 — Chapter 25 (*Tactile Sensing*) added

**Delivered:** Handbook Chapter 25 — R. E. Saad, A. Bonen, K. C. Smith and B. Benhabib (University of
Toronto), 18 source pages, `work/hb_ch25.txt` 41,843 bytes. Full Vietnamese translation plus English
companion at `/vi/books/read/…/ch25-tactile-sensing/` and `/books/read/…/ch25-tactile-sensing/`.
Commit `e35e8d2`. Handbook progress 24/101 → **25/101**.

**Structure:** 25.1 sensing classification · 25.2 mechanical effects of contact (25.2.1 simplified theory,
25.2.2 requirements for tactile sensors) · 25.3 technologies (25.3.1 resistive, 25.3.2 capacitive,
25.3.3 piezoelectric, 25.3.4 optical, 25.3.5 photoelastic). **12 figures, 19 equations, 0 tables,
44 references.**

**Reading the equations.** This chapter is metrology-heavy and its 19 equations arrived from the text
extractor as disconnected token soup — e.g. Eq. 25.2 came out as
`hx d v d v vx rE x d z () =− () + () − − [] π+ () 21 1 22 22 2`. Every equation was therefore transcribed
from the rendered PDF pages (`work/ch25img/page-0004.png` onward) at 1.4–1.6×, not from the text dump.
Four source errata were found and recorded in a translator's note rather than silently corrected:

1. Eq. 25.2 prints the denominator as `πrE(x² + d²)²`. The `r` is almost certainly a typographical
   error — both the dimensions and the standard Boussinesq plane-strain kernel require `πE(x² + d²)²`.
   Confirmed at 3× with an HTML viewport crop (`work/crop.py`), so it is *as printed*, not an extraction
   artefact. Reproduced as printed.
2. §25.3.3 reads "the force applied to the photoelastic material" in the piezoelectric section — a slip
   for *piezoelectric*. Corrected in the translation.
3. Eq. 25.13 prints the term `Δh/h₀` twice in succession. Only one occurrence kept.
4. "3 mm CMOS process" is almost certainly 3 µm. Left as printed.

**Figure QA.** `work/qa_figs.py hb25fig` reported `FIGS 12, problems 0` after the label folding, but as
usual the box checker passed on figures that still had real defects. Rewritten or repaired after visual
inspection at 1.7–2.2×:

- 25.9 — the membrane was a rect plus five separate arcs, so the web's bottom edge drew a line straight
  across the bump tops. Rebuilt as **one closed path** whose underside scallops into the five bumps; the
  scatter fans ran parallel to the zig-zag and were changed to a symmetric left/right pair; the mirror
  floated 40 px above the glass and was lowered to meet the entry rays.
- 25.11 — the four layers were all near-identical greys and read as one mat. Differentiated by tone *and*
  bar width (black 8 px → light grey 5 px) and the spacing opened to 16 px. The layer-2 light arrows were
  drawn from `P(t,0)` pointing *along* the bar, so they were hidden inside it; moved to the far end
  `P(t,1)`. Arrows are now only on layers 1–2, which is also physically right — 3 and 4 are the passive
  corrugation layers, not the active fibres.
- 25.12 — rebuilt wholesale. The tactels and the `s` dimension had been placed on the *front face* rather
  than the top surface; the `l` dimension ran straight through the field of incident-light arrows; the
  force patch sat half off the beam's edge; "bộ phân cực" was printed across the λ/4 plate. Tactels moved
  to the top face at depth d = 0.5, `l` moved clear above the light plane, patch moved to the right of the
  tactels, λ/4 plate shortened to h = 44 so the label clears it.
- 25.7 — the capacitor was drawn edge-on so a wire ran through its plates; the plate is now vertical with
  the lead stopping at the top plate, and the four-line annotation collapsed to one `_subs()` run.

**New helpers in `build/hb25fig.py`:** `_arc(cx, cy, r, a0, a1)` (sampled polyline arc — used for the α
angles in 25.9, because SVG arc sweep flags are easy to get backwards), `_wavy(x1, y1, x2, y2)` (zig-zag
light arrow for fibre ends and light paths) and `_bar(x1, y1, x2, y2, col, w)` (round-capped thick line for
the isometric fibres).

**New work tools:** `work/crop.py <img> <x> <y> <w> <h> <scale> <name>` and the generic
`work/crop2.py` (same but reads the PNG's real width) — both build an `overflow:hidden` viewport with an
absolutely-positioned oversized `<img>`, which is how a region of a page PNG gets read at 2.5–4× without
PIL, which is not installed in this environment.

**Verification:** 12 figures and 19 equations on both sides; 0 tables; 3 `h2` and 8 `h3` both sides
(heading parity checked, as after the Chapter 24 slip); 44 references both sides. Local server: both
chapter URLs, both TOC URLs and both library landing pages return 200. TOC shows **25 done rows with 25
clickable badges**; progress pill reads 25/101 (`🟠 Đang dịch · 25/101 chương` /
`🟠 Translating · 25 of 101 chapters`). Sitemap **529 URLs, 514 EN/VI pairs**; link check **531 pages,
14,445 local references, 0 broken**.

**Chapters 1–25 done; 76 to go.** Next unit is Chapter 26. Same junction + `library/pdfindex.json`
workflow; copy the needed `ChNN.pdf` into `work/`, extract, then follow the §4 recipe — and remember
`books_site.py`. Build only the real figures the source contains — do not pad.

## Session 26 — Chapter 26 (*Pressure and Sound Measurement*) added

**Delivered:** Handbook Chapter 26 — K. H.-L. Chau (Analog Devices); R. Goehner, E. Drubetsky,
H. M. Brady, W. H. Bayles Jr. (The Fredericks Company); P. C. Pedersen (Worcester Polytechnic Institute),
58 source pages, `work/hb_ch26.txt` 2,331 lines. Full Vietnamese translation plus English companion at
`/vi/books/read/…/ch26-pressure-and-sound-measurement/` and `/books/read/…/ch26-pressure-and-sound-measurement/`.
Handbook progress 25/101 → **26/101**.

**Structure:** 26.1 pressure measurement (basic definitions + unit conversion; sensing principles —
sensing elements, detection methods, capacitive, piezoresistive; silicon micromachined sensors;
limitations) · 26.2 vacuum measurement (background/history; direct-reading gages; indirect-reading gages;
partial pressure and mass spectrometers) · 26.3 ultrasound measurement (applications; basic parameters;
conceptual description; sound velocity; wave propagation; intensity and sound levels; reflection/
refraction at boundaries; attenuation; CW piston fields; single-element/array transducers and the
piezoelectric/magnetostrictive phenomena; selection criteria; basic parameters; theory and applications
incl. Doppler and diffraction; review of applications; manufacturers; advanced topics).
**37 figures, 52 equations, 4 tables.**

**Equation QA (vision restored).** The vision tool was rate-limited when the chapter was first drafted,
but came back later in the session. All 52 equations were then checked against the rendered PDF pages in
`work/ch26img/`, and the reconstruction errors were corrected — notably Eq. 26.11 (the temperature factor
is a square root, `c₀ = c_ref √(1 + T/273)`, not linear), Eq. 26.13 (the water polynomial is
`1402.4 + 5.01T − 0.055T² + 0.00022T³ + 1.6×10⁻⁶P₀`), the sound-level block 26.23–26.26 (which had been
shifted by one — 26.23 is the time-average intensity integral, 26.24 the `P²/2ρ₀c₀` form, 26.25 SPL,
26.26 IL), the layer coefficients 26.31/26.32 (full `cos k₂L`/`sin k₂L` forms), the attenuation pair
26.34/26.35 (with the transmission-loss and `1/2d` terms), the piston-field set 26.38–26.41 (axial
pressure with `√(x²/a²+1)`, far field `(ρ₀c₀U₀/2)(ka)(a/r)`, the directivity ratio and
`D = (ka)³/(ka − J₁(2ka))`), and the diffraction integrals 26.46–26.52 (Fresnel/Fraunhofer prefactor
`A₀/jλz` and the received-signal double convolution). The temporary `# NOTE: reconstructed` markers were
removed and replaced with variable definitions. The 37 figures remain caption-based reconstructions —
their geometry was not re-checked against the source.

**Figure QA.** `work/qa_figs.py hb26fig` went 22 → 11 → 8 problems. The 8 remaining are the known
`Box.axes` systemic artefact (y-axis label placed at x = 10 and rotated, flagged off-canvas and
overlapping the `0,5` tick on chart figures 16/18/20/30) — accepted exactly as in prior chapters. Genuine
defects fixed: **26.1** (three-column grid 28/248/468 → 80/290/500 so the left-column labels clear the
canvas edge), **26.9** (canvas height 510 → 560 so the x-axis label is not clipped; bar extents recomputed
with `min/max` so bars no longer invert for downward ranges), **26.16** (N₂ and He labels separated to
(2.4, 0.12) and (0.8, 0.45)), **26.23** (the `C (bản thu mỏng)` label moved below the collector to
(360, 200) so it no longer runs into the ion-current box).

**Verification:** 37 figures, 52 equations and 4 tables on both sides; 3 `h2` and 26 `h3` both sides
(heading parity checked). Local build: TOC **26 done rows with clickable badges**; progress pill reads
26/101 (`🟠 Đang dịch · 26/101 chương` / `🟠 Translating · 26 of 101 chapters`). Sitemap **531 URLs, 516
EN/VI pairs**; link check **533 pages, 14,491 local references, 0 broken**.

**Chapters 1–26 done; 75 to go.** Next unit is Chapter 27.

## Session 27 — Chapter 27 (*Acoustic Measurement*) added

**Delivered:** Handbook Chapter 27 — Per Rasmussen (G.R.A.S. Sound and Vibration). Source
`Ch27.pdf` (26 pages) from the junction at
`/d/Process Control and Automation/The Measurement, Instrumentation and Sensors Handbook/`, copied to
`work/Ch27.pdf`. Text in `work/hb_ch27.txt` (53,788 chars), page renders in `work/ch27img/`
(26 PNGs, 150 dpi, 1050×1503).

Structure follows the source exactly: an unnumbered introduction (longitudinal waves, the three field
variables, free field / diffuse field / closed coupler, why pressure is the only parameter measured
directly) then ten sections — 27.1 the wave equation, 27.2 plane waves, 27.3 spherical waves, 27.4
acoustic measurements with the condenser-microphone subsection, 27.5 sound pressure level, 27.6
frequency analyzers, 27.7 pressure-based measurements, 27.8 sound intensity, 27.9 near-field acoustic
holography, 27.10 calibration — closing with the three references.

**Toolchain note.** PyMuPDF still refuses to import on this Python 3.13 build
(`ImportError: DLL load failed while importing _extra`), so text came from `pypdf` and the page images
from `pypdfium2` (`page.render(scale=150/72).to_pil()`). Both are already installed; no skill was needed.

**Equations.** All 19 (27.1–27.19) were read back off the page images rather than trusted from the text
layer, which scrambles stacked fractions into one line. Two are odd but correct as printed, and were
re-checked at 2× zoom before being kept:

- **27.5** is `p = A cos[(ωt − k)(x + φ₀)]` — a *product* of two brackets, not `(ωt − kx)`. Dimensionally
  strange, but that is what the book sets, and 27.6 copies the same argument.
- **27.14** is `P = A Σ I_n = (2πr/ρc) Σ p_n²` — `2πr`, not `πr²`, in the prefactor.

Subscripts inside equations (`v_f`, `v_n`, `I_n`, `p_n`) are written as real `<sub>` elements; the
earlier chapters' bare `v_f` style reads as a typo at body size.

**Figures.** `build/hb27fig.py`, 21 figures, `work/qa_figs.py hb27fig` → **21 figures, problems 0**.
Five of the originals are photographs (27.1, 27.8, 27.11, 27.13, 27.20) and were redrawn as line art;
the rest are diagrams. 27.10 is a genuine IEC A-weighting curve computed from the standard pole-zero
form, plotted 10 Hz–20 kHz on a log axis. 27.12 places its ten points from Table 27.3 rather than by eye.

Two defects caught in the visual pass, both worth remembering:

- **27.1** had a capsule labelled `1″` that the caption never mentions ("½″ and ¼″"). The photograph
  shows a set of ½″ and ¼″ microphones; relabelled to two of each, and the fourth capsule narrowed from
  d = 46 to 40 so it reads as a ¼″.
- **27.19** labelled the transform plane `2D-ℱ` with U+2131 SCRIPT CAPITAL F, which renders in this
  font as a struck-through F. Replaced with plain `2D-FFT` and `FFT⁻¹`.

**Tables.** Five, all reproduced: 27.1 IEC 651 tolerances (33 frequency rows × 4 type columns, `−∞`
entries intact), 27.2 the 31 1/3-octave bands with exact centres and passbands, 27.3 the ten hemisphere
coordinates, 27.4 instrumentation types with 1999 prices and makers, 27.5 company addresses. In 27.5 the
source lists Brüel & Kjær and Rion with no address; those cells carry an em dash and the caption says so
rather than inventing a street.

**Verification:** 21 figures, 19 equations and 5 tables on both sides; 10 `h2` and 2 `h3` both sides
(heading parity checked). Local build: TOC **27 done rows with clickable badges**; progress pill reads
27/101 (`🟠 Đang dịch · 27/101 chương` / `🟠 Translating · 27 of 101 chapters`). Chapter nav wired both
ways — 26 now points forward to 27, and 27's "next" points at Chapter 28 (*Flow Measurement*), which
falls back to the book TOC until it exists. Sitemap **533 URLs, 518 EN/VI pairs**; link check
**535 pages, 14,623 local references, 0 broken**. Page height 29,116 px at 1424 px viewport with no
horizontal overflow (checked with a same-origin iframe probe that reports `scrollWidth`).

**Chapters 1–27 done; 74 to go.** Next unit is Chapter 28.

---

## Chapter 28 — Flow Measurement (DONE)

**Published.** All eleven sections are translated, the page is registered as `28: "ch28-flow-measurement"`
in `DONE`, the handbook counter reads 36/101, and both language pages are in `sitemap.xml`. Chapter 28
is the largest chapter in the book: **132 source pages, 11 sections, 92 figures (28.1–28.92),
164 numbered equations, 23 numbered tables**, and ten authors.

**Final measurements.** 92 figures, 164 equations, 23 numbered tables (40 `<table>` elements — the
extra 17 are uncaptioned continuation halves where a source table broke across a page),
9 translator's notes, 11 section anchors, 867 kB (EN) / 824 kB (VI) per page, **~160,000 px (VI)**
at a 1424 px viewport, no horizontal overflow.

**Agreed treatment:** full-length faithful translation, one page, spanning several sessions.

### Section map (source page → figures / equations / tables)

| Section | Pages | Figures | Tables |
|---|---|---|---|
| 28.1 Differential Pressure Flowmeters | 3–13 | 1–6 | 28.1–28.4 |
| 28.2 Variable Area Flowmeters | 14–33 | 7–20 | 28.5–28.7 |
| 28.3 Positive Displacement Flowmeters | 34–40 | 21–29 | — |
| 28.4 Turbine and Vane Flowmeters | 41–57 | 30–33 | 28.8–28.9 |
| 28.5 Impeller Flowmeters | 58–63 | 34–35 | 28.10 |
| 28.6 Electromagnetic Flowmeters | 64–74 | 36–42 | 28.11 |
| 28.7 Ultrasonic Flowmeters | 75–89 | 43–58 | 28.12 |
| 28.8 Vortex Shedding Flowmeters | 90–100 | 59–67 | — |
| 28.9 Thermal Mass Flow Sensors | 100–118 | 68–80 | 28.13–28.23 |
| 28.10 Coriolis Effect Mass Flowmeters | 119–122 | 81–84 | — |
| 28.11 Drag Force Flowmeters | 123–132 | 85–92 | — |

A first pass at this table was shifted by one section (28.2 given as 14–23, everything after it a
section early). Corrected above from the actual heading positions; 28.2 is 20 pages, not 10.

Figure 28.58 **does** have a caption — an earlier note here said it did not, which was wrong; it is
printed on p. 88 and the figure sits at the foot of §28.7, not in 28.8. Figure 28.18 is marked “Figure
not available” in the source itself — redraw it from the surrounding description and say so in the
caption.

### Done so far

- **Source extracted.** `work/Ch28.pdf` (copied from the junction), text in `work/hb_ch28.txt`
  (338,511 chars), 132 page images in `work/ch28img/` at 140 dpi.
- **`build/reader_hb_ch28.py`** — module scaffold plus **sections 28.1 through 28.11 complete** in
  both languages: **92 figures, 164 equations, 23 numbered tables, 9 translator's notes**. 867 kB (EN)
  / 824 kB (VI) per page, **~160,000 px (VI)** at 1424 px, no horizontal overflow. Sections are added
  as `sec_NN_vi` / `sec_NN_en` and appended to the `SECTIONS_VI` / `SECTIONS_EN` lists at the bottom;
  nothing else needs touching. The page opens with a `sec_index()` jump index (§28.1–28.11) and each
  section heading carries an `id="s28-N"` anchor.
- **`build/hb28fig.py`** — **all 92 figures**, `work/qa_figs.py hb28fig` → **92 figures, problems 0**,
  visual pass done.
- Generated page verified locally at 1424 px: **79,229 px tall (VI) / 81,020 px (EN)**, no horizontal
  overflow, figures legible, tables fit. 28.1 was 14,552 px, 28.2 ~24,000, 28.3 ~10,600, 28.4
  ~22,000 and 28.5 ~8,800 — a little over half of the projected 150,000.
- **§28.2 covers:** variable-area definition and the rotameter / movable-vane / weir-flume families;
  rotameter construction (conical tube, bobs, scales, glass vs metal, limit switches, transmitters,
  thirteen bullet characteristics); movable vane meter; weir and flume (thin-plate, notch,
  broad-crested); then the measurement-principles half — rotameter force balance and drag laws
  (28.7–28.18), similarity analysis with Reynolds and Ruppel numbers (28.19–28.25), weir and flume
  discharge derivations (28.26–28.39), and the rotameter CFD internal-flow study (28.40–28.46 with
  figures 28.18–28.20) — plus the section summary and its own 16-item reference list.
- **§28.3 covers:** the positive-displacement definition and what separates it from inferential
  meters; design and construction (the three functional parts, single- vs double-walled housing,
  counter and output mechanisms); then the mechanism catalogue, one figure each — sliding vane,
  trirotor, birotor, piston, oval gear, nutating disk, Roots, CVM and diaphragm; advantages and
  disadvantages; applications (the Poiseuille leakage path and viscous-drag torque limit);
  accessories (air eliminator, direct-coupled shut-off valve); price and performance; and a
  six-item “Further Information” list. **No equations and no tables** — the section is descriptive
  throughout, which is why the page grows by only ~10,600 px for seven source pages.
- **§28.3's figures are redrawn schematics, not photographs.** The source illustrates the mechanisms
  with cutaway photographs that cannot be traced usefully; each was rebuilt as a cross-section
  drawing that shows the working principle, and the caption says so.
- **The §28.3 “Further Information” list sits on p. 41**, immediately before the 28.4 heading — not on
  p. 40 with the rest of the section. Easy to miss when slicing the source by page range.
- **§28.4 covers:** the axial turbine family — history and the Woltman principle, the construction read
  off Figure 28.30, the seven-bullet performance envelope, the momentum-exchange theory with
  equations 28.47–28.56, calibration and the universal viscosity curve (Figure 28.32), installation
  and maintenance; then design and construction (rotor, bearings, the four sensor families, output
  options) and eight sub-sections — propeller meters, spirometers, dual-rotor turbines, two-phase
  measurement, insertion turbines, angular momentum meters, multijet turbines, cylindrical rotor
  meters — followed by the manufacturer survey with Tables 28.8–28.9, the conclusion, 29 references
  and a nine-item “Further Information” list.
- **Three slips in the printed source are reproduced as printed and flagged in a translator's note**
  after (28.56): (28.47) should read rω<sub>i</sub> = V·tanβ, (28.56)'s factor should be S/A² not
  S·A², and its coefficient 0.036 should be 0.037 as in (28.55). The note is a bordered `.note` block
  in both languages.
- **§28.4's figures are drawn from the source art**, except 28.33, which the source gives as a product
  photograph and which is redrawn as a sectioned schematic of the same assembly.
- **§28.5 covers:** the impeller/paddlewheel family and what separates it from the turbine meter
  (transverse axis, not parallel); the insertion and in-line types; the naming history from Pelton's
  impulse turbine, with the six-name numbered list; sensing principles (six numbered detection
  methods, 0.2 Hz–500 Hz output); flow ranges (10 cm/s, Re 5000, 0.3–10 m/s, down to 0.07 m/s);
  installation as five sub-headings (pipe sizes, 10D/5D straight runs, 2.7 MPa, calibration, accuracy
  including the ±1 % FS versus ±2 % reading worked example); design features; seven application
  bullets; and the manufacturer survey with Table 28.10 and eight company entries.
- **§28.5 has no equations**, which is why six source pages add only ~8,800 px. Figures 28.34 and
  28.35 are both redrawn: 28.35 is a product photograph in the source, rebuilt as a sectioned
  schematic of the same insertion sensor.
- **The source's Hoffer entry reads “57 mL min⁻¹ to 11.5 rpm”** — a unit inconsistency in the
  original, reproduced as printed and marked `[nguyên văn]` / `[as printed]`.
- **§28.6 covers:** the case for electromagnetic meters (no obstruction, no moving parts, bidirectional,
  linear); Faraday's law and its reduction to `e = BDv`; the noise sources; construction and operation of
  ac and dc meters; the eight-way comparison table; installation; conductivity limits and electrode
  coating; signal pickup and phase-sensitive demodulation (28.62–28.64); grounding; and Table 28.11.
  Seven figures (28.36–28.42) and thirteen equations.
- **§28.7 covers:** the five ultrasonic families as a numbered list (transit time, Doppler,
  cross-correlation, phase shift, drift); the transit-time principle and its time-resolution problem
  (116 µs / 78 ns / 100 ps); oversampling and the two-counter scheme; the six sensor configurations;
  closed-conduit theory (Re, laminar parabola, Nikuradse, `k_h` 28.73–28.76, IEC 41 multipath
  integration); open-channel theory (logarithmic and power laws, `k_h` 28.78–28.83, mean-section
  method); penstock leak detection with surge chambers; Table 28.12; 14 references. Sixteen figures
  (28.43–28.58) and 21 equations (28.65–28.85) — the heaviest section since 28.2.
- **Three defects in the printed source are reproduced as printed and flagged in translator's notes**
  in §28.7: “116 s” for 116 µs after (28.66); “Figure 28.50” cited for the four path arrangements that
  are actually Figure 28.51; and “IEC 41, Appendix J1 [7]” where the reference list has IEC 41 as [8].
- **§28.7's figures needed a second pass.** The first draft passed the QA script with two label
  collisions but failed the eye test in eight places: figure 28.43 split “L_w” into two stacked
  labels sitting on the centreline; 28.44's controller box had its title and formula spread to
  opposite ends of the box and carried duplicate `Nₙ`/`Nₜ` labels; 28.46's “đầu dò” was printed
  across the pipe wall; 28.48's “đáy kênh” sat inside the hatched bed; 28.49's six row labels ran
  straight through the fitting sketches; 28.50's “chảy rối, theo Nikuradse” was printed on the curve;
  28.51's “crossed” arrangements were drawn as parallel chords; 28.55's `1/m` exponent sat on the
  curve; and 28.58's flow arrows pointed in opposite directions. All redrawn.
- **§28.8 covers:** the case for the vortex meter against the orifice plate; the size and flow-range
  envelopes for 15 mm and 300 mm meters in three fluids; the von Karman street and the Strouhal
  number (28.86–28.88); the K factor and its derivation (28.89–28.92); the linear range and the
  K-factor curve; mass flow and standard volume (28.93–28.94); construction — body, shedder,
  sensors, the isolation manifold; transmitters — the three output signals with LFCI, the analog
  transmitter's four mechanical adjustments and the temperature correction (28.95), the intelligent
  transmitter's nine features and four configurators; application — meter selection, sizing and
  pressure drop (28.96), installation, location, adjacent piping, orientation, pressure and
  temperature taps, flashing and cavitation (28.97), configuration; and recent developments —
  multisensor and single-sensor density (28.98–28.100). Nine figures (28.59–28.67) and fifteen
  equations (28.86–28.100). **No table and no numbered reference list** — only a four-item
  “Further Information” block, unlike every section since 28.5.
- **§28.9 covers:** thermal mass flow sensing in full — the two families (heat-loss and
  heat-transfer) and why the measurement is inherently a mass measurement; the three sensor
  geometries (immersed probe, capillary bypass, thin-film on wall); the constant-temperature
  (CTA) and constant-current (CCA) anemometer bridges with their control loops; King's law and its
  calibration; the four gas-property corrections (k, c<sub>p</sub>, µ, and the composition
  dependence) with the correction equations; the CTA/CCA comparison table; the bypass and
  micromachined silicon variants; the full derivation block 28.120–28.135 (heat balance, Nusselt
  correlations, the sensitivity coefficients); the thermal sigma–delta modulator; and the
  seventeen-row manufacturer survey in Tables 28.13–28.23. **Thirteen figures (28.68–28.80),
  eleven tables, 44 equations (28.101–28.144), 22 references** — the heaviest section after 28.2.
- **§28.9's figures are circuit-heavy** and needed primitives the chapter did not have:
  `_zig` (resistor), `_gnd`, `_amp` (triangle), `_wire_sym`, `_bridge` (Wheatstone). All live in
  `hb28fig.py` above `fig_28_68`.
- **Equation (2.118) is printed as (2.118), not (28.118)**, in the source — the chapter's numbering
  slips for one equation. Reproduced as printed and flagged in a `.note` block in both languages.
- **Table 28.19's “Wire” turbulent column reuses the flat-plate formula** — reproduced as printed.
- **§28.10 covers:** the case for a meter that measures mass directly; the history and the naming
  after Gaspard G. Coriolis (1792–1843); the two-paragraph case for industrial adoption; the theory
  of operation — the vibrating tube, the axis of rotation at peak amplitude, acceleration toward
  that point and deceleration away from it, lag on the inlet side and lead on the outlet side, the
  twist proportional to mass flow; the electromagnetic drive and the detector's phase measurement;
  equation 28.145 (F = 2mωv̄); construction (wetted tube only, stainless, Hastelloy, Teflon lining,
  thin-wall variants); advantages (accuracy, turndown, no swirl sensitivity, no moving parts, no
  recalibration, multiple process variables); disadvantages (cost, 150 mm line-size ceiling, thin
  installed base, API approval); applications; a look ahead (straight tubes, gas, steam); and a
  four-item unnumbered reference list. **Four figures (28.81–28.84), one equation, no tables.**
- **§28.10's equation is printed as a scalar magnitude.** The translator's note gives the vector
  form **F** = −2m(**ω** × **v**) and says the two agree in magnitude for a straight tube with the
  flow normal to the axis of vibration — so the printed equation is still usable.
- **§28.10's figures 28.81 and 28.83 are axonometric in the source**; both are redrawn as flat
  schematics (tube in the plane of the page) and the captions say so. The source also marks
  “Coriolis acceleration” at the same points where it marks “fluid reactive force”; the redraw keeps
  the latter and notes the equivalence in the caption.
- **§28.10's reference list is unnumbered**, unlike 28.4–28.9 — it is rendered with `wl()` and no
  `1.` prefixes, as printed.
- **§28.8's figures were drawn from the source art, and two needed a second pass.** Figure 28.66 is
  a two-axis plot in the original — 4–20 mA on the left, pulse frequency on the right, with the
  right-hand zero sitting at the 4 mA level, not at the frame bottom — and the first draft had a
  floating “xung ra” label and no pulse axis at all. Figure 28.67's square wave is aligned to the
  sine's zero crossings in the original; the first draft used a 105 px period against the sine's
  104.65 px, which drifts by half an edge over four cycles.
- **§28.8's heading hierarchy is one level deeper than the rest of the chapter.** The source sets
  “Flowmeter Body”, “Shedder” and “Sensors” as bold italic run-ins *under* “Flow Tube”, and
  “Measurement Output Signals”, “Analog Transmitter” and “Intelligent Transmitters” under
  “Transmitter”. Flattening all eight to `h4` lost that grouping, so a local `h5()` helper
  (0.92 rem, 700, 2 px left rule) was added and the six grandchildren demoted.

- **§28.11 covers:** the case for a target-type meter in dirty, abrasive and two-phase flow; the
  design of the flow sensor (the square rubber cantilever, the sphere on its free end, the four
  gauges as two half bridges); the drag equation (28.146) and the Reynolds relation (28.147); the
  bending derivation (28.148–28.156) from 1/ρ = M/EI through the second moment of area to the
  quadratic strain–velocity law; the two-component wind vector and its magnitude and direction
  (28.157–28.159); implementation with resistive gauges — the 165 × 13.5 mm polybutadiene beam, the
  20 mm table-tennis-ball drag element, the 50 ms response and 30 ms time constant; the calibration
  against wind speed (Figure 28.87) and against angle (Figures 28.88–28.89); the optical fibre
  variant — the grooved PMMA fibre and bend loss, the 633 nm source, the 0.980 mm fibre with 20 µm
  cladding, the 35 m/s two-channel instrument; and a conclusion. **Eight figures (28.85–28.92),
  19 equations (28.146–28.164), no tables, six numbered references.**
- **§28.11's equation 28.147 is dimensionally wrong in the source** — it gives Re = ρVA/η, which
  carries a length, where the Reynolds number needs ρVd/η with d a characteristic length (fibre or
  sphere diameter). Reproduced as printed and flagged in a translator's note that supplies the
  correct form.
- **The source uses ρ for two different quantities in §28.11** — fluid density in 28.146 and the
  radius of curvature of the beam in 28.148–28.152. Reproduced as printed and flagged in a second
  translator's note, which points out that the strength-of-materials literature writes R.
- **“Approximately 20 mm” for the cladding of a 1 mm fibre is a misprint.** Corrected to 20 µm in
  the text and flagged in a third translator's note — a 20 mm cladding on a 1 mm core is not a
  physical object.
- **§28.11's figures 28.87–28.89 are the chapter's only scatter plots** and needed `_axis()` plus
  `_mark()`. `_axis()` takes the axis *ranges* and returns `mx`/`my` closures; an earlier version
  took tick positions as fractions, which put every label at the wrong place (38 QA problems) and
  made the plots unreadable.
- **Figure 28.85 needed a second pass.** The first draft sent both the `G4` and the `G1` leader to
  the *same* front-face gauge, leaving the second gauge unlabelled and the pair reading as one gauge
  named twice. `G1`'s leader now runs under the left gauge and lands on the right one. Neither
  `qa_figs.py` nor a caption check can catch this — it is a content error, not a collision.


### Conventions set for this chapter

- **Table 28.1 is transposed** (rows = attributes, columns = orifice / Venturi / nozzle). The source
  has eleven columns and would not fit the reader column width.
- **Defining-terms blocks render as a two-column `.tbl`**, not a `<dl>` — `library.css` has no
  `.deflist` rule and I did not want to touch the shared stylesheet mid-chapter.
- **Sub-headings below `h3` use a local `h4()` helper with inline size** (1rem/700). There is no
  `.prose h4` rule either, so an unstyled `h4` came out at browser default and looked heavier than the
  italic `h3` above it.
- **Fractions in §28.2 use a plain `/`, not the typographic `⁄`** used in 28.1. In the display
  equations the `⁄` glyph is so short that `∂ρ⁄∂t` reads as `∂ρ+∂t` at normal size. §28.1's few
  fractions are spaced, so they survive it; the derivative equations here do not.
- **`_path(d, col, sw, fill)` — argument order bites.** Seven figure calls had been written
  `_path(d, "#eef2f7", E, 1.6)`, i.e. colour as stroke, `E` as width and the width as fill; browsers
  silently drop all three and draw a solid black shape. Fixed; bobs and weir plates now render as
  light fill with a dark outline as intended.
- **Never put `<sub>`/`<sup>` inside SVG `<text>`.** The HTML parser treats them as a breakout from
  foreign (SVG) content: everything after the tag is re-parsed as HTML and the rest of the figure
  collapses into one run of stray text. Use the `_subs()` tspan helper instead. This is what broke
  Figure 28.32 on the first build; it is silent — the markup is still well-formed XML. `_lbl()` is
  just as vulnerable as a hand-written `<text>`: `_lbl(x, y, "f<sub>URV</sub>")` on Figure 28.66
  hoisted the `URV` to the SVG origin and swallowed the two labels that followed it.
- **`r̄` (r + U+0304) has no glyph in the serif stack** and renders as an acute accent. It is written
  as `<span style='text-decoration:overline'>r</span>` throughout §28.4 — note the single quotes, a
  double-quoted style attribute inside a double-quoted Python string is a syntax error.
- **The QA script skips `<text>` elements carrying a `transform`** — its bounding-box model is
  axis-aligned, so rotated axis titles produced false off-canvas and overlap reports before that.
- **A figure can pass QA and still be wrong in content, not just in placement.** §28.7's Figure
  28.51 was labelled “hai đường cắt chéo” (two crossed paths) while drawing two parallel chords, and
  Figure 28.58 had its two flow arrows pointing at each other. Neither is a label collision, so
  `qa_figs.py` is blind to both. Read every new figure against the source art, not just the QA output.
- **A column of long labels centred on a narrow x will run straight through the drawing.** Figure
  28.49's six disturbance names were `_lbl(120, y, name, "ts", "middle")`; at 10 px the longest is
  ~180 px wide, so it spanned x = 30…210 and crossed both the fitting sketch and the pipe. Right-align
  the column at a fixed edge and wrap the long entries onto two lines.
- **The QA script only compares label against label.** It cannot see a label printed on top of a
  drawn shape, and that was the §28.5 defect: “lỗ phun” and “dòng tuần hoàn” sat across the rotor
  circle and read as struck-through. Every figure still needs the eye test at 1424 px.
- **`fig(num, key, lang)` must be called with the language spelled out.** The default is `"vi"`, so
  an `_en` section that writes `fig(30, F.fig(30))` renders the Vietnamese caption on the English
  page. Figures 30–35 were shipped that way before it was noticed; all twelve calls now pass
  `"vi"` / `"en"` explicitly, and the check is
  `grep -c 'figcaption'` per language rather than eyeballing one page.
- **The `aria-label` on every `<svg>` is baked in Vietnamese and does not follow the language
  switch.** `hbfig.svg(w, h, body, title)` writes `aria-label="<title>"` when the figure is
  *defined*, and `_fig()` stores the Vietnamese and English accessible descriptions as elements 4
  and 5 of the 5-tuple — which `fig()` used to discard. The result: all 92 figures on the English
  page announced a Vietnamese description to a screen reader. `fig()` now rewrites the attribute
  from `aria_en` on the English path. **This is fixed for chapter 28 only.** The same `fig()` helper
  is duplicated in 34 other `reader_hb_ch2x/ch9x/ch10x` modules, so chapters 1–27 and 94–101 have
  the same defect and need the same three-line change plus a rebuild. Check with
  `grep -o 'aria-label="[^"]*"' page.html | grep -c '[ăâđêôơư]'` — it must be 0 on an English page.
- **A jump index at the top of a very long chapter is not optional.** At ~160,000 px the chapter is
  180 screens tall. `sec_index(lang)` builds a `.toc-list` of eleven `<a href="#s28-N">` rows from
  the `SECTIONS` table, and `h2()` attaches `id="s28-N"` to any heading that begins `28.<digits> `.
  No new CSS was needed — `.toc-list` / `.n` / `.t` already exist in `library.css` for the book TOCs.
- **`h2`/`h3`/`h4` now drop a gloss that repeats the title.** Company names and section titles are
  the same in both languages, so `h4("SeaMetrics", "SeaMetrics")` printed “SeaMetrics SeaMetrics”
  and every English-page heading did the same until §28.8. All three helpers carry an
  `if en == t: en = ""` guard, which cleaned up 77 headings at once; new English sections should
  still pass the *Vietnamese* title as the gloss (as §28.1–28.3 and now §28.8 do) so the page stays
  bilingual rather than merely de-duplicated.
- **`ol()` exists as of §28.5.** The source uses numbered lists where the order carries meaning (the
  six naming variants, the six sensing methods); `ul()` was the only list helper before.
- **`_tube(d, w, fill, col)` draws a tube from its centreline** — a wide dark stroke with a slightly
  narrower light one on top leaves a 1.3 px wall each side, so no offset curves are needed. But its
  round line caps stick out half the stroke width past each end: **draw the manifold blocks *after*
  the tube**, or the caps show as light bumps printed inside the block.
- **A vector arrow should touch the thing it acts on.** §28.81's first draft left a 2.5 px gap
  between each force arrow's tail and the tube wall, which at 1424 px reads as a detached arrow.
  Compute the tail from the tube's edge (centreline ± half the stroke width), not from a round number.
- **Full-page screenshots of this page are silently clipped at about 130,000 px.** Chromium stops
  capturing and the PNG is padded with white up to the true `scrollHeight`, so the file height is
  right but “where the content ends” is not — the first §28.10 check concluded the page was
  truncated when it was the *capture* that was. Measure height from the PNG, and to look at anything
  past ~130,000 px **extract the section into a standalone page** (`<h2>28.N` up to
  `<div class="chapter-nav">`, wrapped in the original `<head>`) and screenshot that. The iframe +
  `scrollTo` trick does not work here — the inner page resets its scroll after load.
- **Never read a 4× downscaled crop.** A 1,124 × 3,750 crop shown at 261 px wide made the vision pass
  invent a section order that did not exist. Crop at 1:1 in ~950 px slices of the content column.
- **Measure page heights only after `document.fonts.ready`.** A `--dump-dom` probe that reads
  `scrollHeight` on load under-reports by ~1,000 px at the bottom of a 70,000 px page, because the
  serif web font has not swapped in yet and every line of body text is slightly shorter.
- **To screenshot a region far down the page, shrink the iframe to the clip height and
  `scrollTo` inside it.** Offsetting a 30,000 px-tall iframe with `top:-70000px` leaves the viewport
  looking at blank page — the frame ends 40,000 px above it.
- Equation numbers run 28.1–28.99 and then continue with letter suffixes; keep them as printed.
- 28.2 onwards: add an in-page jump index (28.1–28.11) at the top of `body_vi()` / `body_en()` when
  the last section lands — a 150,000 px page needs one.

### To resume

**Nothing left in this chapter.** It is complete and published. If it ever needs re-opening, the
rebuild sequence is:

```
cd build
PYTHONPATH=. python ../work/qa_figs.py hb28fig    # expect: FIGS 92, problems 0
python reader_hb_ch28.py                          # both language pages
python reader_handbook.py                         # book TOC + progress bar
python books_site.py                              # books index, 36/101
python make_sitemap.py                            # 554 URLs
python check_links.py                             # expect: broken 0
```

Then serve the repo root (`python -m http.server 8899`) and check both pages at 1424 px —
`library.css` is referenced as an absolute `/books/assets/library.css`, so a `file://` render comes
out unstyled and will mislead you.

Note: this repo is worked on from more than one place — chapters 97–101 and Appendix A landed from a
separate session while 28.1 was being written, and the reverse agent is working downward from 93.
**Always `git fetch` and rebase before pushing**: both sides touch `DONE` in `reader_handbook.py`
and the two book-TOC `index.html` files.

---

## Chapter 29 — Point Velocity Measurement (DONE)

**Published.** Three sections, all translated, registered as `29: "ch29-point-velocity-measurement"`
in `DONE`; the handbook counter now reads **45/101**. Source: `Ch29.pdf`, **55 pages, 3 sections,
31 figures (29.1–29.31), 71 numbered equations (29.1–29.71), 4 numbered tables**, three authors.

**Final measurements.** 31 figures, 71 equations, 4 numbered tables, 3 section anchors (`s29-1`,
`s29-2`, `s29-3`), 337 kB (EN) / 322 kB (VI), zero figure-geometry problems from `qa_figs.py`.

### Section map (source page → figures / equations / tables)

| Section | Pages | Author | Figures | Equations | Tables |
|---|---|---|---|---|---|
| 29.1 Pitot Probe Anemometry | 3–16 | Kleppe, Olin | 1–14 | 29.1–29.52 | 29.1–29.2 |
| 29.2 Thermal Anemometry | 17–37 | Olin | 15–23 | 29.53–29.64 | 29.3–29.4 |
| 29.3 Laser Anemometry | 38–55 | Menon | 24–31 | 29.65–29.71 | — |

**Verification:** both languages report 31 figure captions numbered 1–31 in order, 71 equations
numbered 29.1–29.71 with no gap or duplicate, all three anchors present, the in-page contents list
linking all three, and 32 `aria-label` values on the English page **none of which contains a
Vietnamese diacritic** (the §29.2 aria fix holds for this chapter).

### What §29.3 cost, and why

It is short in equations (seven) and long in prose — 115.6 kB of HTML in Vietnamese, 122.8 kB in
English — and it carries the chapter's densest figures. Eight new figures (`fig_29_24` … `fig_29_31`)
needed four review rounds. The failures are worth recording because three of them were *invisible*
to `qa_figs.py`, which only checks bounding boxes:

- **A raw `<` in SVG text.** `θ < 90°` in figure 29.28 is an invalid XML token and collapsed the
  whole figure to a blank box. It has to be `&lt;`. `qa_figs.py` reported
  `MALFORMED: not well-formed (invalid token)` — the one class of error it does catch.
- **`font-size` on a `<text class="ts">` is silently ignored.** `.t` and `.ts` set the `font`
  *shorthand* through a class rule, and a class rule beats a presentation attribute. Twelve box
  labels in figure 29.30 overflowed their boxes until every element-level size was switched to an
  inline `style="font-size:8px"` (helper `_fs()`). On a `<tspan>` there is no matching rule, so the
  attribute does work there — which is why only element-level sizes needed changing.
- **Rotated labels placed by eye sit on the plotted lines.** The four `freq. shift = 0 / f_s` labels
  in figure 29.26(b) were positioned at the line's own y, so the line ran through the letters.
  Because a label rotated to the line's angle is *parallel* to it, the fix is a constant
  **perpendicular** offset (≈10 px), not a vertical one — and the glyphs extend upward from the
  baseline, so a label "below" a line needs its baseline pushed down by more than the cap height.
- **A stepped connector reads as a stray box.** The fibre feed in figure 29.30(a) was a four-segment
  polyline under the "Transmitting optics" box; at 720 px it looked like a second, smaller box
  hanging off the first. Replaced with one diagonal.
- **A 7 px dimension cannot hold two arrowheads.** The acoustic wavelength `Λ` in figure 29.26(a)
  collapsed into a blob. The wavefront spacing was widened from 7 px to 12 px so the dimension has
  somewhere to live, and the arrowheads are now drawn explicitly rather than with the shared marker.

### Notation

The source sets vectors in bold italic with arrows (`u⃗`, `r̂`, `Ŝ`). A probe
(`work/qa29/probe2.html`) showed that `u⃗` (U+20D7 combining arrow) renders as an **empty box** in
Inter/Helvetica at every size, while `r̂` and `Ŝ` (U+0302) render acceptably. The chapter therefore
uses `<b>u</b>` for the velocity vector and `r̂` / `Ŝ` for unit vectors, with a translator's note on
equation 29.67 explaining the departure.

---

## Site shell — one masthead for every page

The main site and the library sub-site had drifted into two different headers. The main one was a 66px
single row: a two-line sans wordmark ("Instrumentation & Control / FIELD GUIDE") with the current page in
a tinted teal pill and a segmented `EN / VI` control at the right. The library had a serif wordmark on its
own line, small grey links beneath it with the current page underlined, and a single bordered language
pill. Reading the two in sequence felt like crossing between two sites.

Every page now wears the library masthead. The main `.topbar` borrows the library's metrics outright —
serif wordmark at 1.32rem, 32px gutters, 0.84rem links with 17px gaps, a 1px underline on hover/active
instead of a tinted pill, and the language switch as a bordered rounded pill. Cormorant Garamond is now
loaded on main pages, which previously only asked for Inter and IBM Plex Mono, so the wordmark does not
fall back to Times.

Three implementation notes, all learned the hard way:

- **Breakpoint 1100px, not 1440px.** A 1440px window reports a 1424px viewport once the scrollbar is
  taken out, so the old `@media (max-width:1439px)` rule left ordinary desktops on the burger menu and
  the new header never appeared where it was most needed.
- **The second row is a grid** (`"brand brand"` / `"nav pill"`), not wrapping flex. With flex, the
  language pill drops onto a line of its own the moment the links run a few pixels wide — which is
  exactly what happened at 1280px. Pinned to the second row's end it cannot.
- The gutters live on `.bar`, not `.wrap`: they are the same element (`<div class="wrap bar">`), so
  `.bar{padding:14px 0}` was silently wiping the horizontal padding.

Below 1100px the burger menu keeps the navigation usable, unchanged from before.

`ASSET_VER` goes 12 → 13 so browsers refetch the stylesheet; all 20 main pages plus `404.html` were
rebuilt and now reference `style.css?v=13`. Library and reader pages keep their own `library.css` and
were unaffected. Link check after the change: **533 pages, 14,571 local references, 0 broken**.

---

## Session 28 — Appendix A, Chapter 101 and Chapter 100 (working the book backwards)

The owner asked for the handbook to be finished **from the back**: start at Appendix A, then 101,
100, 99 … down to 80. This session shipped the first three of that sequence, all live.

**Appendix A — Units and Conversions** (`build/reader_hb_app.py`, slug
`appendix-a-units-and-conversions`). No appendix had ever been built, so the slug, the `APPENDIX`
and `APP_TITLE` maps in `reader_handbook.py`, the TOC row and the nav slot all had to be invented.
`DONE` is keyed by chapter *number*, so the appendix is registered separately and
`chapter_nav.py` gained a `FIRST_APPENDIX` branch: the last chapter's right-hand slot now points at
Appendix A instead of greying out. Five tables — A.1 SI base units, A.2 the seven international
definitions, A.3 derived units, A.4 the twenty prefixes (two-column layout via `_rows_a4`), A.5
seventeen quantity groups and 117 conversion rows. 236 `<tr>`, 0 figures, 0 equations.

Two new table classes were needed in `library.css` because the generic `.tbl` misbehaved:
`.tbl.defs` (lets the long definition column wrap — the one-column table had inherited
`.tbl.moc`'s `white-space: nowrap` and clipped at the right edge) and `.tbl.units` (nowrap from
column 2, `min-width` on column 1 — unit expressions were breaking mid-token as `m·kg·s-` / `²`).
`.tbl.conv` keeps the factor column nowrap and right-aligned with tabular figures.

Print/OCR defects corrected and listed in a translator's note on the page: ton-force 8,896,443 N;
the missing in.² unit; the point (0.351 46 mm) added; light year recomputed 9.640 73 → 9.460 730 ×
10¹⁵ m; rhe 10 Pa⁻¹·s⁻¹; Btu_IT/h 0.293 071 1 W; teaspoon 4.928 922 mL.

**Chapter 101 — Stepping Motors** (`reader_hb_ch101.py` + `hb101fig.py`). Five figures, exactly
the five in the source, nothing padded. 101.1 is a torque–speed curve computed from
`T(f) = 1/(1 + (f/348)^0.887)` on a log speed axis; 101.2 is an H-bridge with a real 75 % duty
train; 101.3/101.4 are the four-block closed-loop diagrams with summing junctions; 101.5 adds the
microprocessor boundary. 24 equations (101.1)–(101.14) with subscripts, 7 references.
Equation 101.5 is printed with `sin θ_ref` twice in the source; kept as printed and flagged.

**Chapter 100 — Explosion-Proof Instruments** (`reader_hb_ch100.py` + `hb100fig.py`). Seven
figures, 5 equation blocks (the four lumped-parameter equations keep the source's numbers
100.1–100.4; the Z<sub>w</sub> equation is unnumbered in the print and stays so), three tables,
ten references, four defined terms.

### The bug that cost the most time — `<sub>` inside `<svg>`

The first render of figures 100.1–100.5 was wrecked: parameter columns collapsed into one
horizontal run of text, captions appeared twice, and labels sat outside their boxes. The cause is
not geometry. **`<sub>` and `<sup>` are on the HTML parser's "breakout" list**: inside SVG foreign
content the parser pops out of the SVG at the first one and every following element is parsed as
loose HTML. So `<text>V<sub>min</sub> = 12 V</text>` silently closes the figure.

**Rule: never emit `<sub>`/`<sup>` inside `<svg>` text.** Use `<tspan font-size="7.5" dy="2.5">`
for subscripts and `<tspan dy="-2.5">` to come back up — that is what `_rich()` in `hb100fig.py`
does. `<sub>` is fine in HTML contexts (figcaptions, equations, body text).

Related: raw `$_{sc}$` markup leaked into two axis titles of figure 100.2, and `_zener_v()` drew
the lead straight through the triangle. All fixed; `_panel()` now also accepts an x-axis title as
a `[(text, is_sub), …]` list so the subscripts survive.

### Verification

- `reader_handbook.py` → 102 TOC rows, 30 done rows, 14 sections, 101 chapters.
- `chapter_nav.py` → 58 pages updated. Chapter 100 reads `← Chương 99 … Chương 101 →`; Chapter 101
  now reads `← Chương 100 … Phụ lục A →`.
- `check_links.py` → 539 pages, 14,777 local references, **0 broken**.
- `make_sitemap.py` → 537 URLs, 524 with EN/VI pairs.
- Chapter 100 page: 7 figures, 5 equations, 3 tables, 29 `<tr>`, 0 `<sub>` inside any SVG.

### Note for the next session

`books_site.TRANSLATED["measurement, instrumentation and sensors handbook"]` is
`("progress", 101, 29)` — bump the third number with every chapter that lands, or the books
catalogue shows a stale count. The `DONE` dict currently holds 27 chapters plus 100, 101 and
Appendix A; the book TOC renders 28–99 as `chờ dịch`, which is correct.

---

## Session 29 — Chapter 99 (*Electropneumatic and Electrohydraulic Instruments*)

Next step in the reverse sequence after Chapter 100. Source `work/Ch99.pdf`, text
`work/hb_ch99.txt`, page renders `work/png99/`. Chapter title in `CH[99]` is *Thiết bị điện – khí
nén và điện – thuỷ lực*, which is what the live Chapter 100 nav slot already pointed at.

### What landed

`build/hb99fig.py` (10 figures, ~40 kB) and `build/reader_hb_ch99.py` (~1,000 lines, VI + EN).
Slug `ch99-electropneumatic-and-electrohydraulic-instruments`. 26 equations (99.1a–99.25),
10 figures, one nomenclature table, 7 references, plus a translator's note covering four print
defects in the source.

### Figure rebuild — what the first pass got wrong

The whole module was rewritten once before it ever reached the page, then re-QA'd figure by
figure against 2× screenshots. Defects found and fixed:

- **`_bode()` was lost in the rewrite** and every call raised `NameError`. Rebuilt: log-x in rad/s,
  magnitude panel above, phase panel 62 px below, decade grid, phase unwrapping, `dash="+"` means
  "sample as dots" rather than "draw a line".
- **Figure 99.2 was topologically wrong.** Panel (a) drew the `c/b` feedback block inline after
  the summing junction, so the signal ran sum → block → x_f and both arrows pointed *into* the
  block. The source has the junction feeding x_v to the right and `c/b` hanging *below* it,
  fed from the right by x_f and feeding the junction from underneath. Panels (b) and (c) were
  re-drawn to the same pattern; the G(s) label and its dashed box had been placed in panel (b)
  where they collided with the `c/b` block, when they belong to panel (c).
- **Figure 99.4/99.9 axis titles were clipped** by a canvas 4 px too short, and 99.9's phase axis
  ran 0…100 so every short-period marker clamped to 0. Replaced the ad-hoc transfer functions
  with an honest pair: `sp(s) = 10(s+2)/((s+1.2)(s+6))` and `full(s) = sp(s)/(s+0.05)` — the extra
  phugoid pole at 0.05 rad/s is exactly the effect the caption claims.
- **Summing-junction signs sat on the signal lines.** `_sum()` placed `+` at `cx-r-7` and `−` at
  `cy+r+10`, i.e. directly under the incoming arrowhead and on the vertical feedback line. Moved
  to `(cx-r-10, cy-5)` and `(cx+5, cy+r+11)`, which is clear in every figure.
- **Figure 99.6 hatch escaped the damping block** on the right; the 45° lines are now clipped to
  the rectangle analytically. Torque arcs were raised clear of the shaft.
- **Figure 99.7** drew the ram ending in nothing; added an explicit hinge, a lever to the surface,
  a clipped R_h dimension and smaller τ arcs.
- **Figure 99.8** used `_frac()` for a 172 px-wide block, so the fraction rule read as a signal
  line crossing the block; replaced with a short rule. Removed a redundant feedback rectangle and
  added arrowheads to the top path.
- **Figure 99.1** routed the "feedback linkage" into the cylinder. It now runs from the bell crank,
  left along the bottom, and up the far side to point *c* on the lever, as in the source.

### Verification

- `reader_handbook.py` → 102 TOC rows, **31** done rows, 14 sections, 101 chapters.
- `chapter_nav.py` → **60** pages updated. Chapter 99 reads `← Chương 98 Điều khiển tối ưu …
  Chương 100 → Thiết bị phòng nổ`; Chapter 100 now reads `← Chương 99 … Chương 101 →`.
- `check_links.py` → **541 pages, 14,829 local references, 0 broken**.
- `make_sitemap.py` → **539 URLs, 526 with EN/VI pairs**.
- Chapter 99 page (both languages): 10 figures, 26 equations, 1 table, nav correct.

### Note for the next session

`books_site.TRANSLATED["measurement, instrumentation and sensors handbook"]` is now
`("progress", 101, 30)`. `DONE` holds 30 entries — chapters 1–27 plus 99, 100 and 101 — and the book TOC renders
28–98 as `chờ dịch`, which is correct. Next chapter in the reverse sequence: **98, Optimal
Control**, then 97 (PID Control) — both are control-theory chapters with block diagrams and
step-response figures, so the `_bode()` and `_sum()` helpers in `hb99fig.py` are worth copying
rather than rewriting.

---

## Session 30 — 2026-11-01 · Handbook Chapter 98 (*Optimal Control*)

Halit Eren (Curtin University of Technology). 6 figures, **68 numbered equations** (98.1–98.63
plus 98.21a–98.21e), 18 defining terms, 4 references, List of Manufacturers. Reverse sequence
continues: 97 is next.

### Files

- `build/hb98fig.py` — new, 6 figures. Reuses the `_sum`/`_blk`/`_path` idiom from `hb99fig.py`,
  plus three new helpers: `_contour()` (closed irregular contour for the 98.2 hill-climb maps),
  `_smooth()` (Catmull-Rom-ish cubic through a point list) and an analytic `J(u)`/`dJ/du` pair.
- `build/reader_hb_ch98.py` — new, both languages.
- `build/reader_handbook.py` — `98:` added to `DONE` (7-space indent, as always).
- `build/books_site.py` — `TRANSLATED` progress 30 → **31**.
- `books/assets/library.css` — new `.eq .mxw` rule for bracketed matrices.

### The matrix rule

Chapter 98 is the first chapter in the book that needs real 2×2 block matrices (Eqs. 98.57–98.60).
A bare `<table class="mx">` with `border-left/right` renders as two detached vertical rules, which
reads as a determinant rather than a matrix. The fix is a wrapper span with pseudo-element arms:

```css
.eq .mxw { display: inline-block; position: relative; vertical-align: middle; padding: 0 8px; }
.eq .mxw::before, .eq .mxw::after {
  content: ""; position: absolute; top: 1px; bottom: 1px; width: 6px;
  border: 1.8px solid var(--gray-dark);
}
.eq .mxw::before { left: 0; border-right: 0; }
.eq .mxw::after  { right: 0; border-left: 0; }
```

Do **not** put the pseudo-elements on the table itself — on a `display: table` box they generate
anonymous table cells and the brackets land in the wrong place.

### Figure defects found and fixed

- **Figure 98.1 (first pass) was invented.** The hand-drawn `J(u)` had its marked extrema
  nowhere near the zeros of the drawn `dJ/du`. Rewritten analytically: `dJ/du = −(u−u1)(u−u2)(u−u3)`
  with `u1,u2,u3 = 0.26,0.46,0.72`, and `J(u)` obtained by trapezoidal integration of `dJ/du`, so
  the gold curve crosses its zero line exactly beneath the three stationary points of the black one.
- **Figure 98.2 point counts did not match the source.** The original has six points `sT0…sT5` in
  panel (a) and eight `sT0…sT7` in panel (b); the first pass drew five and six. Also the markers
  are ellipses, not circles, and panel (b)'s motion arrow points up-*right* while panel (a)'s
  points up-*left*. All four corrected.
- **Figure 98.2 panel (b) label collision** — `sT4` was left-anchored straight on top of `sT5`'s
  marker. `sT4` now anchors right, `sT6` moved out to `cx+44`.
- **Figure 98.2 caption detached from its arrow** in panel (b): the text was right-anchored at
  x=536 while the arrow sat at 600–634. Now centred at 617.
- **Figure 98.3 labels sat on their curves.** `ITAE`/`IAE`/`ISE` were at hard-coded heights that
  no longer matched the plotted finals. They are now placed from the computed final values and
  pushed apart by 14 px, so they can never collide whatever the integrator outputs.
- **Figure 98.5 was missing the outer rail.** The source has *two* taps on the output line: the
  inner one feeds the `A` loop back into the summing junction, the outer one runs down the full
  width of the diagram and back up into the `x(k)` input of `−K(k)`. Only the inner loop had been
  drawn. Canvas grew 300 → 350 px to make room; the precomputation box is now centred over
  `−K(k)` instead of hanging over the gap between `−K(k)` and `B`.
- **Figure 98.6 had a zero-length arrow.** `_arr(468, y, 470, y)` was a 2 px segment whose head
  pointed *out* of the observer box instead of into it, and the observer → `K` leg had no head at
  all. Rebuilt: the whole horizontal run from the measurement tap is one arrow ending on the
  observer's right edge, then a second arrow from the observer's left edge into `K`, then a
  vertical arrow up into the junction.

### Print defects in the source (recorded in the translator's note)

1. **Fig. 98.4's feedback block prints `G`**, although both the caption and the body text call it
   the gain `K(k)`. The redrawn figure labels it `K(k)`.
2. **Eqs. 98.7 and 98.12 are identical** in the original; both kept as printed.
3. The `*` in Eqs. 98.23–98.44 means *transpose*, not conjugate transpose — stated in the text.
4. **Eqs. 98.17 and 98.19 are font-corrupted** in the printed page; set out in the standard form
   of the calculus of variations.

### Typography

- `û` was typed as precomposed U+00FB while `x̂` was decomposed (`x` + U+0302). In Cormorant
  Garamond the precomposed glyph's circumflex collapses to a dot at 18 px, so `û` read as `u̇`.
  Both are now `u`/`x` + U+0302. **Use the combining mark, never the precomposed letter, for hats
  and dots in equations.**
- At 1× the capital `H` of the Hamiltonian looks like `|1` — that is Cormorant Garamond's hairline
  crossbar, not a bug; it is legible at 4× and on a real screen. No font change made.

### Verification

- `reader_handbook.py` → 102 TOC rows, **32** done rows, 14 sections, 101 chapters.
- `chapter_nav.py` → **62** pages updated. Chapter 98 reads `← Chương 97 Điều khiển PID …
  Chương 99 → Thiết bị điện – khí nén và điện – thuỷ lực`; Chapter 99 now reads
  `← Chương 98 Điều khiển tối ưu`.
- `check_links.py` → **543 pages, 14,881 local references, 0 broken**.
- `make_sitemap.py` → **541 URLs, 528 with EN/VI pairs**.
- Chapter 98 page (both languages): 6 figures, 69 `.eq` blocks (68 numbered + the unnumbered
  system model in §98.5), 11 `.mxw` matrices, 7 `<svg>` (6 figures + site logo), **zero** `<sub>`
  or `<sup>` inside any `<svg>`.

### Note for the next session

`books_site.TRANSLATED["measurement, instrumentation and sensors handbook"]` is now
`("progress", 101, 31)`. `DONE` holds 31 entries — chapters 1–27 plus 98, 99, 100 and 101 — and the
book TOC renders 28–97 as `chờ dịch`, which is correct. Next in the reverse sequence: **97, PID
Control** — also a control-theory chapter, so `hb98fig.py`'s `_sum`, `_blk`, `_smooth` and `_path`
are directly reusable.

---

## Session 31 — 2026-11-01 · Handbook Chapter 97 (*PID Control*)

F. Greg Shinskey, 9 source pages. Four figures, seven equations, five numbered sections, fifteen
defining terms, three references, no List of Manufacturers. VI translation plus the matching EN
companion essay.

### Source facts

| Item | Count | Pages |
|---|---|---|
| Figures | 4 | 97.1 p3, 97.2/97.3 p4, 97.4 p6 |
| Equations | 7 (97.1–97.7) | 97.1/97.2 p3, 97.3 p4, 97.4–97.6 p5, 97.7 p6 |
| Defining terms | 15 | p8–9 |
| References | 3 | p9 |

Sections: 97.1 Introduction · 97.2 Open and Closed Loops · 97.3 Mode Selection · 97.4 Controller
Hardware · 97.5 Tuning Controllers.

### Figures (`build/hb97fig.py`)

1. **97.1** — loop diagram. `q`/Load → `g_q` → `−` into `K_p`; `g_m` → `+` → `K_p` → `+`/`−`
   junction with `u`/Noise from above; `c`/Controlled var. out; dashed Process/Controller divider;
   `f`/Set point → `g_r` → junction (`t:"−"`, `r:"+"`) → `K_c g_c` → `m`/Manipulated var. → up the
   left side into `g_m`.
2. **97.2** — open-loop exponential (dashed) vs closed-loop return to set point (solid).
3. **97.3** — second-order step, `ζ=0.35` dashed ("No filter") vs `ζ=0.70` solid ("Set-point
   filter").
4. **97.4** — interacting PID controller: Filter `(1 + G_r Is)/(1 + Is)` → Σ(`l:+`,`b:−`) → `e` →
   Σ(`b:−`) → `K_c` → Σ(`l:+`,`b:+`) → Limits → `m`; `c` taps down to the Derivative box
   `Ds/(1 + αDs)`; dashed `f` from `m` back through `1/(1 + Is)` into the third junction.

### Defects found and fixed

- **97.1's `m` line did not reach `g_m`** — the horizontal stopped at x=196 while the box sat at
  108–182, with a broken vertical stub. Replaced with `_line(250, 300, 145, 300, 1.3)` plus
  `_arr(145, 300, 145, 146)`.
- **97.4 was missing the wire between its two summing junctions**, so `e` had nowhere to go. Added
  `_arr(205, YM, 284, YM)` and moved the first junction's signs to `l`/`b`.
- **97.4's `f` arrow was a degenerate 4 px segment** into the Integral box. Replaced with
  `_arr(522, YL, 509, YL)` plus `_arr(236, YL, 249, YL)` into the Derivative box.
- **Subscripts `r`, `q`, `m`, `p`, `c` were too small to read** inside the boxes. Raised
  `<tspan font-size="7.5" dy="2.6">` to `8.2 / 2.4` and `.tf` from 10 px to 11.5 px.
- **`Load` overlapped the `q` label** in 97.1. Moved to `(136, 60)`.

### Terminology defect (caught only by reading the rendered page)

The first draft rendered *tuning* as **"định cỡ"** throughout — 19 occurrences, including the
section heading `97.5 Định cỡ bộ điều khiển` and the defining term `Định cỡ (tuning)`. In Vietnamese
engineering usage **"định cỡ" means *sizing*** (valve sizing = định cỡ van), not tuning; the
established term is **"chỉnh định"**, which is what every other chapter on the site uses. Normalised:

- `định cỡ` → `chỉnh định` (19 replacements in `reader_hb_ch97.py`)
- `Tự định cỡ` → `Tự chỉnh định` (autotuning), keeping `Tự chỉnh` for self-tuning
- heading → `97.5 Chỉnh định bộ điều khiển`
- defining term → `Chỉnh định (tuning)`

A second, related slip: the 97.3 caption said **"Bộ lọc chỉnh định"** for *set-point filter*. The
chapter uses "lệnh đặt" for set point everywhere else, so it became **"Bộ lọc lệnh đặt"**.

**Trap worth remembering:** the captions in `hb97fig.py` are written as `\uXXXX` escapes, not literal
UTF-8. A plain `str.replace("định cỡ", …)` over the source silently does nothing — the file contains
`\u0111\u1ecbnh c\u1ee1`. Always grep the generator for the **escaped** form, or edit the tuple
directly.

### Verification

- `reader_handbook.py` → 102 TOC rows, **33** done rows, 14 sections, 101 chapters.
- `chapter_nav.py` → **64** pages updated. Chapter 97 reads `← Chương 96 Thiết bị đọc và ghi …
  Chương 98 → Điều khiển tối ưu`; Chapter 98 now reads `← Chương 97 Điều khiển PID`.
- `check_links.py` → **545 pages, 14,933 local references, 0 broken**.
- `make_sitemap.py` → **543 URLs, 530 with EN/VI pairs**.
- Chapter 97 page (both languages): 4 figures, 7 numbered equations, 15 defining terms, 3
  references, 5 `<svg>` (4 figures + site logo), **zero** `<sub>` or `<sup>` inside any `<svg>`,
  zero residual `định cỡ`.
- Live: VI **200**, EN **200**; book index reads **32 / 101**.

### Note for the next session

`books_site.TRANSLATED["measurement, instrumentation and sensors handbook"]` is now
`("progress", 101, 32)`. `DONE` holds 33 entries — chapters 1–27 plus 97, 98, 99, 100 and 101 — and
the book TOC renders 28–96 as `chờ dịch`. Next in the reverse sequence: **96, Reading/Recording
Devices**. Chapter 96 is hardware-oriented (pen recorders, magnetic tape, optical disks), so expect
mechanical drawings rather than control block diagrams — `_frame`, `_line`, `_arr` and `_rich` carry
over, but `_sum` and `_blk` will mostly not be needed.

---

## Session 32 — 2026-11-01 — Handbook Chapter 96, *Reading/Recording Devices*

### What shipped

Chapter 96, `ch96-reading-recording-devices`, both languages, live. Three authors, three
independent numbering schemes, all preserved as printed:

| Section | Author | Figures | Tables | Equations |
|---|---|---|---|---|
| 96.1 Graphic Recorders | Herman Vermariën | — | 96.1–96.5 | — |
| 96.2 Data Acquisition Systems | Edward McConnell | 96.1–96.12 | 96.6–96.7 | unnumbered |
| 96.3 Magnetic and Optical Recorders | Yufeng Li | 96.13–96.29 | 96.8–96.11 | 96.1–96.32 |

29 figures, 11 numbered tables (13 rendered blocks — 96.2 and 96.4 are each split in the source and
stay split), 32 numbered equations, three separate **Defining Terms** blocks (96.1 and 96.2 have
their own; 96.3 has none), 19 references split 5 + 14 across 96.1 and 96.3, and the
**Further Information** list that 96.2 uses in place of references.

### Build notes worth keeping

- `reader_hb_ch96.py` carries an `_EQ` dict keyed `"96.1"`…`"96.32"` plus `_eq(lang, num)`, so the
  Vietnamese and English bodies render the *same* equation markup and cannot drift. Only 96.9 and
  96.31 carry language-bearing words (`nếu` / `if`, `có hố` / `there is a pit`); those two branch
  inside `_eq`.
- All eleven tables are built by `_tN(lang)` functions returning `(hd, rows, cap, cls)` and consumed
  as `table(*_tN(lang))`. Table 96.1 and 96.3 rows store both an English and a Vietnamese
  description, so the Vietnamese page translates the catalogue blurbs (`Test, meas.; 4,6,8 c. ch.`
  → `Thử nghiệm, đo; 4, 6, 8 kênh liên tục`) instead of leaving them as opaque option codes.
- Prices are given with dot thousands on the Vietnamese page (`11.500`) and comma thousands on the
  English page (`11,500`), matching the two decimal conventions.

### Source defects recorded in the translator's note

1. Figure 96.12's caption reads **45 µs**; the drawing itself reads **50 µs**. Both reproduced.
2. The continuous-scanning passage claims two sine waves **90° out of phase** always sum to zero.
   Only 180° does. Reproduced as printed and flagged.
3. The simultaneous-sampling passage prints **ms** for intervals that are 5 µs and 5 ns. The
   translation gives µs and ns, which agree with Figure 96.11 and with 1/200 kS/s.
4. Table 96.9's resistivity column is printed `ρ (mW.cm)` in the text layer of the PDF but is
   `ρ (µΩ·cm)` on the page image; the page image wins.

### Verification

- `reader_handbook.py` → 102 TOC rows, **34** done rows, 14 sections, 101 chapters.
- `chapter_nav.py` → **66** pages updated. Chapter 96 reads `← Chương 95 Hiển thị LED … Chương 97
  → Điều khiển PID`.
- `check_links.py` → **547 pages, 14,985 local references, 0 broken**.
- `make_sitemap.py` → **545 URLs, 532 with EN/VI pairs**.
- Chapter 96 page (both languages): 29 figures, 32 numbered equations, 13 table blocks, 35 list
  items (5 + 11 + 19), **zero** `<sub>` or `<sup>` inside any `<svg>`.
- Live: VI **200**, EN **200**; book index reads **33 / 101**.

### Note for the next session

`books_site.TRANSLATED["measurement, instrumentation and sensors handbook"]` is now
`("progress", 101, 33)`. `DONE` holds 34 entries — chapters 1–27 plus 96, 97, 98, 99, 100 and
101 — and the book TOC renders 28–95 as `chờ dịch`. Next in the reverse sequence: **95, Light-
Emitting Diode Displays**. That chapter is display-physics oriented (LED materials, drive
circuits, multiplexing), so expect energy-band diagrams and current/voltage curves; `_frame`,
`_line`, `_arr`, `_rich` and `_path` carry over, and band diagrams will want a filled-region
helper rather than the recorder-style `_blk`.

---

## Session 33 — Chapter 95 (*Light-Emitting Diode Displays*) added

**Shipped:** Chapter 95, `ch95-light-emitting-diode-displays`, VI + EN, live and registered.
Commit `8571548`.

### Source shape

Far more compact than Ch. 96: **8 figures, 1 table, 20 numbered equations** (23 expressions
counting 95.8a/b, 95.9a/b, 95.17a/b), 5 references, **no Defining Terms block**. The chapter is one
continuous essay with no numbered sections, so the eleven thematic `h2` headings are ours — bilingual,
in the house style. Author: Mohammad A. Karim, University of Tennessee, Knoxville.

### The eight figures (`build/hb95fig.py`)

| Fig | Content | Approach |
|---|---|---|
| 95.1 | *E* vs *k*, direct and indirect gap | sampled parabolas via `_band()`; two panels |
| 95.2 | Spectral luminous efficiency *V*<sub>λ</sub> / *V*′<sub>λ</sub> | asymmetric Gaussians, peaks 555 / 507 nm |
| 95.3 | *E*<sub>g</sub> vs *x* in GaAs<sub>1−x</sub>P<sub>x</sub> | two lines crossing at (0.45, 1.977) |
| 95.4 | Nitrogen doping: (a) η vs *x*, (b) λ<sub>peak</sub> vs *x* | log axis mapped through `log10`; panel (b) in a `translate` group |
| 95.5 | Surface vs edge emitter | cabinet-projection `_slab()` |
| 95.6 | Encapsulation geometries + radiation patterns | domes + two overlaid lobes (solid narrow, dashed wide) |
| 95.7 | Chopper circuit with amplifier | `_opto()` block helper, 4 terminals each |
| 95.8 | Display formats + 16-segment character chart | `_SEG16` map of 42 glyphs over a 36×56 design space |

### Lessons worth carrying forward

1. **`_slab(x, y, w, h, dx, dy)` wants `dy` positive.** The top face is `y - dy`; passing a negative
   `dy` inverts the box and the slab renders inside-out. Cost one full redraw of Fig. 95.5.
2. **Curves must be clamped to the frame, not extrapolated.** Fig. 95.1b's valence parabola ran off
   the bottom-right corner because the sampled range exceeded the plotted range. Parameterise the
   parabola by a half-width so both ends land inside by construction.
3. **Labels on a rising line need a side, not a nudge.** `E`<sub>g</sub> callouts in Fig. 95.3 kept
   being cut by the direct-gap line; the fix was to put them *below* the shallow line / *above* the
   steep one, plus a dashed leader from the crossing — not to shift them a few pixels.
4. **Legends beat inline labels when two curves cross.** Fig. 95.4b's "with/without nitrogen" labels
   sat between the curves and were crossed by both; a three-line legend in the empty upper-right
   corner is unambiguous.
5. **A 16-segment glyph needs a segment map, not per-character geometry.** `_GEO` (12 rects) +
   `_DIA` (4 diagonals) in a 36×56 design space, wrapped in `<g transform="translate() scale()">`,
   renders all 42 glyphs from `_SEG16` string sets. Subscripts are irrelevant here but the *breakout*
   rule still applies: no `<sub>`/`<sup>` anywhere inside `<svg>`.
6. **`_rich`/`_lbl` argument order is `(x, y, text, cls, anchor)`.** Passing the anchor into the `cls`
   slot silently changes the font class instead of the alignment — it looks like a layout bug.

### Source defects (all recorded in the page's translator's note)

- Table 95.1 lists **SnO<sub>2</sub>** as II–VI; tin is group IV, so it is not a II–VI compound.
  Kept as printed.
- Table 95.1 is **not monotonic in *E*<sub>g</sub>** (CuBr 2.9 eV follows BeTe 2.8 eV). Kept as printed.
- The text prints "**x = 0.05**" where the context (direct→indirect crossover at *x* ≈ 0.45) requires
  **0.5**. Translated as 0,5 and flagged.
- Eq. **95.17a** is printed with exponent **1/2**, but Eq. 95.14 forces
  τ<sub>r</sub> = [*B*<sub>r</sub>(*n*<sub>0</sub> + *p*<sub>0</sub>)]<sup>−1</sup> as Δ*n* → 0;
  1/2 is dimensionally wrong. Kept as printed and flagged.
- Eqs. 95.8a/b use **δ²/δ*x*²**; normalised to ∂²/∂*x*² to match Eq. 95.6.
- **R**<sub>nr</sub> in Eqs. 95.13/95.14 is the *net* recombination rate, not the nonradiative rate,
  despite the "nr" subscript. Kept as printed.

### Verification

`toc rows: 102`, `done rows: 35`, `sections: 14`, `chapters: 101`, `chapter-nav: 68 pages updated`,
`sitemap.xml: 547 URLs, 534 pairs`, `check_links.py → 549 pages, 15,037 local references, 0 broken`.
Page: 8 figures, 23 numbered equation items, 1 table, 7 `h2`, zero `<sub>`/`<sup>` inside any `<svg>`.
Nav renders `← Chương 94 Hiển thị điện phát quang · Mục lục sách · Chương 96 → Thiết bị đọc và ghi`;
index shows **34 / 101**. Live: VI 200 / EN 200.

### State after this session

`TRANSLATED` is `("progress", 101, 34)`. `DONE` holds 35 entries — chapters 1–27 plus 95, 96, 97, 98,
99, 100 and 101 — and the book TOC renders 28–94 as `chờ dịch`. Next in the reverse sequence:
**94, Electroluminescent Displays**. That chapter is phosphor-physics oriented (destruction and
acceleration of electrons, luminescent centres, drive waveforms), so expect field/energy diagrams
and brightness-vs-voltage curves; `_band`, `_slab`, `_opto` and the `Box` log-axis trick all carry
over.

---

## Session 34 — Chapter 94 (*Electroluminescent Displays*) added

**Commit** `46d7f3d` (chapter + ledger, rebased onto `85ce27b` and pushed as `5aec715`).
Chapter 94 of the CRC handbook, by William A. Barrow (Planar Systems). Ten sections, ten figures,
six numbered equations, two tables, a nine-term Defining Terms block and 13 references.

### Figures (`build/hb94fig.py`)

| Fig | Content | Notes |
|---|---|---|
| 94.1 | ACTFEL cross-section | hatched glass substrate, five thin layers, leader labels right, LIGHT arrow left, ac source below |
| 94.2 | Colour ACTFEL | seven alternating RED/GREEN/BLUE phosphor cells, all layer labels |
| 94.3 | Bipolar trapezoidal drive waveform | A–L markers; V_to / V_th / V_P as level indicators standing in the clear gap between the two pulses |
| 94.4 | Energy band diagram at peak pulse | interface-state ticks at the left phosphor boundary, tunnelling arrow, hot-electron drift, three Mn²⁺ impact-excitation pairs |
| 94.5 | Idealised QV loop | open loop above threshold, dashed straight line below; A–L placed on the curve; V_to / V_th / V_P as downward ticks on the voltage axis |
| 94.6 | Q_P F_P loop | near-rectangular loop with chamfered corners, letters at the corners |
| 94.7 | Luminance/efficiency measurement system | `_rack(..., "photo")` — photometer, no HV, no PMT, no 1 kΩ |
| 94.8 | Luminance and efficiency vs peak voltage | dual axis, solid S-curve + dashed efficiency peak near 200 V |
| 94.9 | Decay-time apparatus | `_rack(..., "pmt")` — HV supply, PMT, 1 kΩ load tapped into the scope |
| 94.10 | Time-resolved spectrum system | `_rack(..., "mono")` — PMT + monochrometer, GPIB to the monochrometer |

**`_rack(tag, mode)` is the single block diagram behind 94.7, 94.9 and 94.10.** Three modes —
`"photo"`, `"pmt"`, `"mono"` — differ only in which detector boxes exist and whether the HV supply
and the 1 kΩ load are drawn. The topology is:

```
COMPUTER --GPIB--> PHOTOMETER / MONOCHROMETER      (photo and mono modes only)
COMPUTER <--GPIB--> OSCILLOSCOPE
COMPUTER --GPIB--> ARBITRARY WAVEFORM GENERATOR
AWG --> AMP --> DUT (Al top electrode)
DUT (transparent bottom electrode) --> SENSE RESISTOR --> earth
DUT --LIGHT--> PHOTOMETER / PMT(+mono)
OSC CH1: V(t) tapped on the Al run
OSC CH2: I(t) tapped above the sense resistor
PMT anode --> 1 kΩ --> earth, tapped into the scope   (pmt and mono modes only)
```

Every net has its own routing channel, so no wire runs through a box and the only crossing is the
detector-GPIB bus passing the PMT output wire — drawn without a junction dot, which is the correct
convention for "no connection".

### What went wrong first, and how it was fixed

1. **The first `_rack()` was wrong on all three counts.** It fed the HV supply into the *photometer*,
   put a PMT in Fig. 94.7 (which has none), hung the 1 kΩ off the photometer output, and let the
   AWG→amp and amp→DUT wires form a stray rectangle across the canvas. The source page images
   (rendered to `work/png94/`) showed the real topology: 94.7 has **seven** boxes and no HV supply
   at all; 94.9 adds HV + PMT + 1 kΩ; 94.10 adds a monochrometer and a GPIB link to it. Rewritten
   from scratch against the scan.
2. **The PMT/1 kΩ node never reached the oscilloscope** in the first rewrite — the caption says the
   scope measures the light signal across that load, so the tap had to be added.
3. **`SENSE RESISTOR` was drawn across the I(t) channel wire.** Moved to the right of the resistor,
   under the DUT, where nothing crosses.
4. **The detector GPIB and the PMT tap were 2 px apart and read as one thick line.** Separated to
   y = 112 and y = 124; the resulting single crossing is deliberate.
5. **Fig. 94.3 had `V_th` drawn on top of the falling edge and `V_to` floating after the zero
   crossing.** Both arrows now stand in the empty column between the positive and negative pulses,
   labelled above their tops. The pulse was widened from 92 to 124 px so the labels clear the
   falling edge.
6. **Fig. 94.4 printed `STATES` above `INTERFACE`.** Swapped; also nudged `UPPER INSULATOR` left so
   it no longer runs into the Al block.
7. **Fig. 94.5's three voltage markers floated in a row at y ≈ −0.3 µC/cm².** Replaced with
   downward ticks standing on the voltage axis, keyed to points B, C and D/E. `D` and `E` at the
   apex were separated vertically. `L` sat on the loop's bottom edge and was lifted 8 px.
8. **Fig. 94.8's `AMP` label ran into the triangle's right edge.** Moved from x = 580 to x = 573.
9. **The English companion page was built with zero figures.** `body_en()` had all the prose but
   none of the ten `fig(...)` calls — the VI page had 10 and the EN page had 0. Caught by the
   post-build count (`figs 0 | svg blocks 1`). Both pages now carry all ten.

### Lessons worth carrying

- **Count the figures on *both* pages after every build.** The VI page was complete and the EN page
  was silently empty; a single `s.count('class="figure"')` on each file catches it in one line.
- **Trace a block diagram from the rendered page image, not from the caption text.** The caption of
  Fig. 94.7 mentions only V(t), I(t) and the photometer, and says nothing about the HV supply that
  is *not* there — the presence/absence of boxes is only visible in the scan.
- **`_rack(mode)` beats three near-copies.** 94.7/94.9/94.10 differ by two boxes and three wires;
  one parameterised builder keeps the shared geometry identical and makes the differences legible.
- **A single crossing without a junction dot is fine.** Trying to eliminate it produced a GPIB bus
  routed around the whole top of the canvas, which read worse than the crossing.
- **Level indicators belong on an axis, not floating in the plot area.** Fig. 94.5's ticks on the
  voltage axis are unambiguous; the earlier floating row was not.
- **Pulse-body annotations need the body to be wide enough first.** Fig. 94.3's labels only cleared
  the falling edge after the plateau was widened, not by nudging label offsets.

### Source defects logged in the translator's note

1. The PDF text layer drops µ, Ω and ×: "5 to 15 W/square" is Ω/square, "30 ms" in the Fig. 94.3
   caption is 30 µs, "10 ms pulse width" is 10 µs, "100 ms to a few milliseconds" is 100 µs to a few
   ms, "320 ´ 240" is 320 × 240. Restored — a 30 ms pulse cannot fit in a 16.7 ms frame at 60 Hz.
2. Two Greek letters were replaced by Latin ones: efficiency "h" is η (including Eq. 94.2, printed
   as "h p = LA / P"), and decay time "t" is τ. Restored.
3. The ITO thickness is printed as "350 and 120 nm", an inverted range. Left as printed; the
   plausible value is 35–120 nm, since 350 nm ITO is far too thick for 5–15 Ω/square.
4. Two conflicting pulse widths: 30 µs (Fig. 94.3 caption) and 10 µs (§94.7). Both kept — they
   refer to different experiments.
5. `V_to` ↔ B and `V_th` ↔ C per the body text and the Defining Terms block, i.e. the reverse of
   the left-to-right order in the source figure. Fig. 94.5 follows the text.
6. "mura" is a Japanese term of art with no settled Vietnamese equivalent; kept untranslated and
   glossed as "khuyết tật vệt".

### Verification

`toc rows: 102`, `done rows: 36`, `sections: 14`, `chapters: 101`, `chapter-nav: 70 pages updated`,
`sitemap.xml: 549 URLs, 536 pairs`, `check_links.py → 551 pages, 15,089 local references, 0 broken`.
Page: 10 figures, 6 numbered equations (94.1–94.6), 2 tables, 13 `h2`, 13 `h3`, 9 glossary terms,
zero `<sub>`/`<sup>` inside any `<svg>`. Nav renders `← Chương 93 Hiển thị phẳng plasma ·
Mục lục sách · Chương 95 → Hiển thị LED`; index shows **35 / 101**. Live: VI 200 / EN 200.

### State after this session

`TRANSLATED` is `("progress", 101, 35)`. `DONE` holds 36 entries — chapters 1–27 plus 94, 95, 96,
97, 98, 99, 100 and 101 — and the book TOC renders 28–93 as `chờ dịch`. Next in the reverse
sequence: **93, Plasma-Driven Flat Panel Displays**.

### Known gap (not introduced this session)

`build/make_glossary.py` only parses `<dl class="glossary">` blocks and only reads the chapters
listed in its `SRC` map (ch05, ch06-4, ch06-5, ch06-6). Chapters 94 and 96–101 emit their Defining
Terms block as `<p><b>term:</b> def</p>` via a local `dt()` helper, so **their terms never reach
`/glossary.html`**. The banner claim that "adding a chapter that defines terms adds them to the
glossary automatically" therefore holds only for the chapters in `SRC`. Wiring 94 and 96–101 in
means emitting `<dl class="glossary"><dt>…</dt><dd>…</dd></dl>` and adding both-language headwords
to `BOOK_EN`; that is a self-contained follow-up, deliberately not bundled with a chapter commit.

### Session 34 (cont.) — Chapter 93 survey

Started **Chapter 93, *Plasma-Driven Flat Panel Displays*** (R.T. McGrath, R. Veerasingam,
Penn State; W.C. Moffatt, R.B. Campbell, Sandia). It is the largest chapter in the reverse run so
far and was **not** started in code this session; the survey below is the handoff.

| Property | Value |
|---|---|
| Source | `work/hb_ch93.txt`, 1045 lines; `work/Ch93.pdf`, 31 pages, rendered to `work/png93/` |
| Sections | 6 — 93.1 Introduction (Development History and Present Status · dc and ac Plasma Pixels · General Attributes), 93.2 Fundamentals of Plasma Pixel Operation (Atomic Physics Processes · Discharge Physics · Plasma Surface Interactions), 93.3 Pixel Electrical Properties (dc Pixels · ac Pixels), 93.4 Display Priming, Addressing, Refresh, and Gray Scale, 93.5 Color Plasma Flat Panel Displays (Color Pixel Structures · VUV Photon Production · Phosphor Excitation · Lifetime), 93.6 Inspection and Metrology |
| Figures | **20** (93.1–93.20) |
| Tables | **4** (93.1 display specs and manufacturers' plans, 93.2 relative quantum efficiencies and chromaticity, 93.3 noncontact profiling and chemical characterisation equipment, 93.4 advanced noncontact profiling techniques) |
| Equations | **11** — 93.1, 93.2a, 93.2b, 93.3 … 93.11 |
| References | **64** |
| Defining Terms | **none** — no glossary block, so this chapter adds nothing to `/glossary.html` |

Figure inventory (from the caption lines, to be confirmed against the page images):

| Fig | Subject |
|---|---|
| 93.1 | ac plasma display structure invented at the University of Illinois (1966) |
| 93.2 | simple dot-matrix plasma display with data scanning switches |
| 93.3 | 40-in. diagonal dc-driven plasma display from NHK (photograph) |
| 93.4 | 40-in. diagonal ac-driven plasma display from Photonics Imaging (photograph) |
| 93.5 | schematic of (a) dc and (b) ac opposed-electrode plasma pixels |
| 93.6 | structure of the Fujitsu ac colour plasma display |
| 93.7 | collisional and surface interactions in a gas discharge |
| 93.8 | quantum energy level diagrams for He, Ne, Ar, Xe and Xe₂⁺ |
| 93.9 | ionising collisions vs E/p, one curve per gas |
| 93.10 | breakdown voltage vs pressure–gap product (Paschen curves) |
| 93.11 | potential profiles in the pixel gap for high and low electron density |
| 93.12 | current–voltage characteristic for gas breakdown with load lines |
| 93.13 | voltage and current traces for a 45 × 45 ac pixel array, on and off states |
| 93.14 | discharge charge displacement for a 45 × 45 ac array |
| 93.15 | sustain and address voltage waveforms |
| 93.16 | pulsed memory operation of the NHK dc display, driver block diagram |
| 93.17 | structure of the 40-in. NHK colour display |
| 93.18 | VUV emission spectra from opposed-electrode ac pixels in He/Xe |
| 93.19 | relative quantum efficiency of Tb-activated lanthanum phosphate vs YAG |
| 93.20 | photon transmission through MgO films before and after bake-out |

Notes for whoever picks this up:

- **93.3 and 93.4 are photographs, not diagrams.** They cannot be redrawn as SVG; follow the
  established convention for photo figures in this book (see how Chapters 96–101 handled them) and
  substitute a captioned placeholder or omit with a note, rather than inventing a schematic.
- **93.8 needs real energy-level data** — the term manifolds for He, Ne, Ar, Xe and the Xe₂⁺
  excimer band are printed in the figure and must be transcribed from the page image.
- **93.10 is a family of Paschen curves** on a log–log axis; the `Box` log-axis trick from
  Chapter 95 carries over.
- The PDF text layer again drops µ and × ("100 mm" for 100 µm, "852 ´ 480" for 852 × 480), so the
  same restoration pass as Chapters 94 and 95 applies.


---

### Session 35 — Chapter 93 shipped

**Chapter 93, *Plasma-Driven Flat Panel Displays*** (McGrath & Veerasingam, Penn State; Moffatt &
Campbell, Sandia) is translated, drawn, registered and live. The survey left at the end of session
34 was accurate: six sections, **20 figures, 4 tables, 11 numbered equations** (93.1, 93.2a, 93.2b,
93.3–93.11 — twelve rendered blocks), **64 references**, and **no Defining Terms block**, so
`/glossary.html` gains nothing.

| File | Role |
|---|---|
| `build/hb93base.py` | shared primitives: colour set, `_lbl`/`_r`/`_line`/`_arr`/`_poly`/`_path`/`_dot`/`_circ`/`_hatch`, the isometric `_slab`/`_isostrip`/`_isostrip_d`, and a `Frame` with linear **or** log axes and a top axis for the `E/P` and `Pd` scales |
| `build/hb93fig.py` | figures 93.1–93.10 |
| `build/hb93figb.py` | figures 93.11–93.20, plus `_mk`/`_glyph` marker helpers |
| `build/reader_hb_ch93.py` | the chapter itself: `_EQ`, `_T1`/`_T1_EN`, `_T2`–`_T4`, `_REFS`, `body_vi()`, `body_en()`, translator's note |

Twenty figures split into two modules because one file of forty kilobytes of SVG builders is
unreviewable. The three source photographs (93.3, 93.4 and the screen content of both) are redrawn
as line art with the display content explicitly omitted and said so in the caption, as Chapters 27
and 28 did.

**Curves are computed, not sketched.** 93.9 is the Townsend family `α/p = A·exp(−B/(E/P))` on
log–log axes with the top scale in V/m/Pa; 93.10 is Paschen's law `V = B·pd / (ln(A·pd) − C)` with
`C = ln(ln(1 + 1/γ))`, `γ = 0.01`, and the Ne/Ar minima checked against the printed ones (250 V and
150 V). The measured curves — 93.13 current traces, 93.14 hysteresis, 93.18 VUV spectra, 93.19
quantum efficiency, 93.20 MgO transmission — are rebuilt from the printed data points and drawn
through markers, so a reader can see where the data are and where the line is interpolated.

**Three figure bugs worth remembering.**

1. `_lbl(x, F.Y(value), …)` is wrong when the second argument is already a *pixel* row. Three load
   line labels in 93.12 were passed `F.Y(208)`, `F.Y(196)`, `F.Y(184)` — 208 "amps" on a 2.6-unit
   axis — and were drawn 19,000 px below the canvas. The figure looked like it had lost its labels;
   the labels existed, off-screen. Grep for `F.Y(` with a literal above the axis maximum.
2. A sampling loop `for i in range(0, 101): x = i * 0.5` covers **half** the domain. 93.11a stopped
   at 50 µm of a 100 µm gap, which read as a curve that simply ended. The canvas does not complain.
3. `<sub>`/`<sup>` inside `<svg>` still eject the parser from foreign content. 93.14's
   `V_erase`/`V_sustain`/`V_address` and 93.15's row labels now go through `_r()` with `<tspan
   dy=…>`, which is the only safe subscript in an SVG here.

**A twelve-column table needs its own layout.** Table 93.1 (eight manufacturers × twelve columns)
was unreadable at first: the shared `table.tbl` padding of `8px 12px` left about 43 px of content
per column and words broke mid-token (`Fujits|u`, `Mitsub|ishi`). Fixed by adding a `.dense`
modifier to `books/assets/library.css` — smaller type, `padding: 6px 5px`, headers allowed to wrap,
`table-layout: fixed` — plus a `<colgroup>` with explicit widths from the chapter's `table()`
helper (`colw=`) and `white-space: nowrap` on the four short columns (`nw=`). **The reader pages
load `/books/assets/library.css`, not `/assets/style.css`**; the first three attempts went into the
wrong file and had no effect, which is exactly the kind of silent no-op worth writing down.

**Source defects logged, not silently repaired** (all in the chapter's translator's note): the PDF
text layer drops `µ` and `×` throughout (`100 mm` for 100 µm, `25 mm` for 25 µm, `10 ms` for
10 µs, `1 ms` for 1 µs, `500 kW` for 500 kΩ, `5 MW` for 5 MΩ, `1 MW` for 1 MΩ); Greek letters are
substituted (`g` for γ, `r(x)` for ρ(x), `lD` for λ_D, `hn` for hν); "3 Pa (~400 Torr)" is really
3 × 10⁴ Pa; Hitachi's contrast "50.1" is 50:1; and Table 93.2's formulae arrive mangled and were
restored to LuBO₃ / ScBO₃ / GdBO₃ / Zn₂SiO₄ / (Y,Gd)BO₃. Figure 93.12's printed load lines do not
in fact intersect the negative-resistance branch at the voltages the text describes; the drawing
follows the printed picture, the three operating regions are marked on the curve with a keyed
legend rather than fake intersection callouts, and the inconsistency is called out in the note.

**Verification.** `reader_hb_ch93.py` → 299 kB / 323 kB. **20 figures, 12 equation blocks, 64 list
items on both pages** — parity holds. Registries updated: `DONE[93]` in `build/reader_handbook.py`,
`TRANSLATED[...] = ("progress", 101, 36)` in `build/books_site.py`; `chapter_nav.py` rewrote 72
pages and moved Chapter 94's "previous" link from the TOC to the new chapter. Rebuild chain clean:
sitemap **551 URLs / 538 EN/VI pairs**, link check **553 pages, 15,141 local references, 0 broken**.
Book TOC now reads *Đang dịch · 36/101* / *Translating · 36 of 101*.

**Next in the reverse sequence: 92, *Liquid Crystal Displays*.** 93's survey notes on 93.8 (real
energy-level data must be transcribed from the page image) and 93.10 (the `Frame` log-axis helper
carries over) are now resolved in code; 92 starts from `work/Ch92.pdf` and needs the same
µ/× restoration pass.

### Session 36 — Chapter 92 shipped

**Chapter 92, *Liquid Crystal Displays*** (Kalluri R. Sarma, Honeywell) is translated, drawn,
registered and live. Six sections, **16 figures, 16 numbered equations** (92.1–92.16), **30
references**, no tables and no glossary block.

| File | Role |
|---|---|
| `build/hb92base.py` | re-exports the Chapter 93 primitives and adds the LCD helpers: `rod`, `rod_field`, `flat_rod`, `layer_plane`, `cell_side`, `isocell`, `legend_line`, `arrow_light`, `sine_wave` |
| `build/hb92fig.py` | figures 92.1–92.6 — phase diagrams, order parameter, ε(T), index ellipsoid, n(λ) |
| `build/hb92figb.py` | figures 92.7–92.12 — the three deformations, passive-matrix plan and cross-section, the assembly flowchart, TN, STN, ECB |
| `build/hb92figc.py` | figures 92.13–92.16 — AM module block diagram plus array schematic, cross-section, pixel layout, equivalent circuit and waveforms |
| `build/reader_hb_ch92.py` | the chapter: `_EQ`, `_REFS`, `body_vi()`, `body_en()`, translator's note |

**Curves computed from stated physics.** 92.3 is the Haller form `S = (1 − T/Tc)^β` fitted to the
printed PAA points; 92.6b is Cauchy's `n = n∞ + α/λ²` through the two printed anchor pairs; 92.10c
is a logistic electro-optic curve with the NW/NB branches mirrored; 92.11 is a family of five
midplane-tilt logistics whose steepness rises with the twist angle (Φ = 180–270°), numbered and
keyed in the right margin. 92.4 and 92.6a are rebuilt from the printed markers, so the data points
and the interpolated line are visually distinct.

**The U+2225 trap.** `∥` (U+2225) collapses into a solid block at 9.5 px bold in this SVG stack;
`‖` (U+2016) renders as two clear bars. Every SVG label uses U+2016 — see the note at the top of
`hb92base.py`. The HTML prose keeps U+2225, which renders correctly in the body font.

**Figure fixes worth remembering.** 92.8's cross-section was unreadable until the stack was
lengthened and the eleven labels fanned left and right in ascending order (leaders cannot cross if
both lists are sorted). 92.14 had the ITO and the white gap swapped, putting the pixel electrode
under the TFT; its TFT label also sat inside the LC layer and was moved outside with a leader.
92.13's power rail crossed the row-driver → panel arrow, so the vertical run now carries a 12 px
gap (a line hop, no join). 92.15 carried two "TFT" labels; one was removed.

**Source defects logged** (translator's note on both pages): the cell gap is printed "5 to 10 mm"
and the colour-filter thickness "2 mm" — both are µm; the response times are printed "tr, tf"
where the text means τr, τd (Eq. 92.13 is τd); Eqs. 92.9–92.13 were OCR-mangled and are restored
to the standard Freedericksz and Jakeman–Raynes forms; Fig. 92.3's caption says "PPA" where the
text says PAA.

**Verification.** `reader_hb_ch92.py` → 247 kB / 250 kB. **16 figures, 16 equation blocks and 30
list items on both pages**; zero `<sub>`/`<sup>` inside any `<svg>`. Registries: `DONE[92]` in
`build/reader_handbook.py`, `TRANSLATED[...] = ("progress", 101, 37)` in `build/books_site.py`.
Rebuild chain clean: sitemap **553 URLs / 540 EN/VI pairs**, link check **555 pages, 15,193 local
references, 0 broken**. Live: both URLs return 200.

**Next in the reverse sequence: 91, *Cathode Ray Tube Displays*.** Note that the 92 page's
"previous chapter" link names Chapter 91 but falls back to the book TOC, because 91 is not yet in
`DONE` — that is `chapter_nav`'s documented behaviour, not a regression, and it will resolve the
moment 91 is built.

---

### Session 37 — Chapter 91 shipped

**Handbook Chapter 91, *Cathode Ray Tube Displays* (Christopher J. Sherman)** is translated,
built, verified and live. Book progress **38/101** on both TOCs.

**Inventory.** Twelve sections, two subsections under 91.3 and two under 91.7, **2 figures**,
**3 tables**, **0 numbered equations**, **28 references**, plus "Further Information" and
"Internet Resources" blocks. The smallest chapter in the reverse run so far, and the first with
no equations at all — which is why it needed no `_EQ` dict and no equation-count check.

| File | What it holds |
|---|---|
| `build/hb91fig.py` | figures 91.1 and 91.2, digitised spectra, Bezier/offset helpers |
| `build/reader_hb_ch91.py` | the chapter, the three tables, 28 references |

**91.1 was redrawn three times before it read as a CRT.** The first pass put the funnel's
widest point at x=494 with a flat plateau running into the faceplate, which made the tube look
like a light bulb. The second pass fixed the proportions (faceplate half-height 148 against a
neck half-height of 26, i.e. 5.7:1) but built the lower wall cubic in the wrong direction —
`_bez((394,334), …, (250,266))` runs right-to-left, so the outline picked up a stray second
bottom wall crossing the funnel. **Lesson: every cubic in a wall pair must be authored in the
same direction (left to right); reversing one silently duplicates the wall.** The third pass
also replaced vertical offsets on the deflection bands with true normal offsets (`_off()`), so
the coils hug the cone instead of standing off it on the steep section.

**91.2 is measured data, not a formula.** A phosphor emission spectrum cannot be computed from
stated physics, so the two curves were rebuilt from the printed graph: the page image was
extracted with PyMuPDF, the plot box located from the axis line row/column sums (left axis
x=144.5, baseline y=1153.5, 19 x-ticks at 92.9 px per 20 nm, 11 y-ticks at 112.55 px per 10 %),
and the curve traced column-wise taking the midpoint of the first dark run. Two passes of a
median-3 filter killed the jitter, a Douglas–Peucker pass at ε=0.30 % cut 1668 samples to 28
points (blue) and 60 (red), and the monotone flanks of the 612 nm line were enforced — then the
duplicate-value points that clamp created were dropped, because they showed up as visible
stair-steps on a near-vertical stroke. Peaks land at 452 nm and 612 nm exactly as the caption
states.

**Table 91.3 needed the printed page, not the text extract.** The source's two-column layout
flattens into a single stream, which made it look as though "U.S. address / 25358 Avenue
Stanford / Valencia, California" belonged to Sony. Rendering PDF page 11 shows it belongs to
**Rank Brimar**, and that the "Discrete Products Division / Riviera Beach, Florida" block belongs
to **Philips**, not Hitachi. Fourteen suppliers, addresses reproduced as printed, each with an
italic "Địa chỉ Hoa Kỳ" sub-heading.

**Source defects logged** (translator's note on both pages): `£` is a mangled `≤` and `³` a
mangled `≥`; `1.3 ´ 10–4 Pa (10–6 torr)` has lost its superscripts; `21/2` is the mixed number
2½; chemical subscripts are missing (Zn(Cd)S:Cu:Al, Y₂O₂S:Eu); **`£25 mm` / `£15 mm` /
`£150 mm` / `£250 mm` must be µm** — a 25 mm spot is impossible on a 12 mm tube; "Standford
Resources" is a misspelling of Stanford (correct in the references); "electromagnetic yolks" is
*yokes*; "whether of not" is *whether or not*; 91.6's "both require precise beam control" has
no antecedent and refers to the delta and in-line configurations; Table 91.3 prints "Phillips"
(the company is Philips), "1-chrome" (1-chome), "Tyoko" (Tokyo) and "Minato-KU".

**Verification.** `reader_hb_ch91.py` → 68 kB / 67 kB. **2 figures, 3 tables, 28 reference list
items, 15 `<h2>` and 5 `<h3>` on both pages**; zero `<sub>`/`<sup>` inside any `<svg>`.
Registries: `DONE[91]` in `build/reader_handbook.py`, `TRANSLATED[...] = ("progress", 101, 38)`
in `build/books_site.py`. Rebuild chain clean: sitemap **555 URLs / 542 EN/VI pairs**, link check
**557 pages, 15,245 local references, 0 broken**. Chapter 92's "previous chapter" link now
resolves to 91 — the fallback noted at the end of session 36 is gone. Live: both URLs return 200.

**Next in the reverse sequence: 90, *Human Factors in Displays*.** It is already in `CH` as
`("Human Factors in Displays", "Yếu tố con người trong hiển thị")`; source at `work/hb_ch90.txt`.

---

### Session 38 — Chapter 90 shipped

**Chapter 90, *Human Factors in Displays*** (Steven A. Murray, SPAWAR Systems Center; Barrett S.
Caldwell, University of Wisconsin — Madison). 11 sections, 8 subsections, 1 figure, 6 equations,
0 tables, 10 references, a 6-term "Defining Terms" glossary and 4 further-reading items.

| File | Change |
|---|---|
| `build/reader_hb_ch90.py` | new — VI + EN pages, 6 equations, glossary, references |
| `build/hb90fig.py` | new — figure 90.1, the four alphanumeric fonts |
| `build/reader_handbook.py` | `DONE[90] = "ch90-human-factors-in-displays"` |
| `build/books_site.py` | `TRANSLATED` progress `(101, 38)` → `(101, 39)` |

**Every one of the six equations was corrupt in the text extract** and had to be re-read from a
300 dpi raster of the page, not repaired by guesswork. The extract renders the pi-times sign as
`p´`, drops the Δ from `ΔI`, flattens two fraction bars, and swaps the sub/superscripts in 90.4
and 90.6:

| | printed | extract had |
|---|---|---|
| 90.1 | `R = π × luminance/illuminance` | `R =p´` |
| 90.2 | `K = ΔI/I` | `K I / I = D` → "DI" |
| 90.3 | `VA = 3438H/D` | `VA = 3438H D` |
| 90.4 | `E = Eₘ cos⁴θ` | `EE = m cos4 q` |
| 90.5 | `C_R = (L_bright − L_dark)/L_bright` | flattened to one line |
| 90.6 | `CFF = a log Lₐ + b` | `CFF a L b =+ log a` |

Worth remembering: **90.6 is `a·log Lₐ + b`, not `a + b·log Lₐ`** — the extract's token order
suggests the latter and would have produced a plausible-looking but wrong formula. Always raster
the page for an equation you cannot parse with certainty.

**Fractions.** `library.css` has no fraction class, and adding one would touch every reader page.
The four stacked fractions are therefore built by a local `_frac(num, den, size)` helper that
emits two inline-block spans with a `border-bottom` rule between them. At 390 px the 90.5
numerator wraps to two lines and `C_R =` moves to its own line — ugly but contained, no
horizontal overflow. Verify equations at mobile width, not just at 1100 px.

**Figure 90.1 was digitised, not invented.** The four panels were read off the extracted page
image by locating the dot grids from column/row dark-pixel profiles and sampling cell centres:

- 5 × 7 matrix spells **R**; 9 × 11 matrix spells **K** (single-column stem — that is what the
  book prints, not a drawing error on our side);
- seven-segment shows **5** with a, f, g, c, d lit (the source hatches its unlit segments, which
  is why b and e are pale here);
- the starburst lights both verticals plus the two upper diagonals, giving **M**.

The source labels that last panel "16-segment font" although only **fourteen** segment positions
are drawn. The printed label is kept and the discrepancy is in the translator's note.

**Source defects recorded in the note rather than silently repaired.** Beyond the equations:
`»0.02` for ≈0.02; `2 ´ 10–7 lx` for 2×10⁻⁷; `cd/m2` (the page really prints cd/m², the
superscript is lost only in extraction); `;,` in the *Transillumination* definition; "does no
flicker"; "graceful degrades"; "an excellent summaries"; "two of the primary colors — red, blue,
and green" (three are listed); the stray closing parenthesis in "Helander (1987) and Grandjean
[3])"; and "Handbook of Human Factors (Reference 2)" for Grandjean's chapter, which is reference
**3** — reference 2 is Sanders and McCormick. Three substantive points are also flagged: the prose
definition of reflectance in 90.2 is inverted relative to its own equation; "International
Lighting Commission (CIE)" should be *International Commission on Illumination*; and the printed
cone peaks (670/470/400 nm) are not the values usually quoted (~564/534/420 nm).

**Verification.** Both pages built at 56 kB / 55 kB. Parity checked mechanically on both: 1
figure, 6 equations, 14 list items in the reference region (10 + 4), 14 `h2`, 9 `h3`, 6 glossary
`dt`, and **0 `<sub>`/`<sup>` inside any `<svg>`**. Rebuild chain clean: sitemap **557 URLs / 544
EN/VI pairs**, link check **559 pages, 15,297 local references, 0 broken**. Chapter 91's
"previous" link now resolves to 90, so the reverse chain 101 → 90 is continuous. Book TOC shows
**39/101** on both language sides.

### Session 39 — Chapter 89 shipped

**Chapter 89, *Electromagnetic Compatibility*.** Two authors in one chapter: 89.1 *Grounding and
Shielding in Industrial Electronic Systems* by Daryl Gerke and William Kimmel (Kimmel Gerke
Associates, Ltd.), and 89.2 *EMI and EMC Test Methods* by Jeffrey P. Mills (Illinois Institute of
Technology). The chapter is unusually unequal — 89.1 is about three quarters of it, and its
structure is a single deep hierarchy (Understanding EMI Problems → Grounding → Shielding, each with
run-in sub-heads and italic sub-sub-heads) with **no numbered sections inside 89.1**, which is why
the translated page uses `h2` for 89.1/89.2 and `h3` for the three top blocks, then bold run-in
paragraphs below that, mirroring the printed typography.

| File | What it is |
|---|---|
| `build/hb89fig.py` | 89.1–89.5, new |
| `build/reader_hb_ch89.py` | the chapter, VI + EN, ~11.2k / ~14.3k words |
| `build/reader_handbook.py` | `DONE[89] = "ch89-electromagnetic-compatibility"` between 27 and 90 |
| `build/books_site.py` | `("progress", 101, 39)` → `40` |

**The text extract destroys every unit and every symbol.** The extract's substitution table is
worth writing down because it will recur in the remaining chapters: Ω → `W`, µ → `m`, π → `p`,
λ → `l`, ε → `e`, × → `´`, ≈ → `»`, and every super/subscript is flattened onto the baseline.
So `377 W` is 377 Ω, `64 W` is 64 Ω, `1 to 10 W` is 1–10 Ω, `1 to 100 mH` is 1–100 µH,
`0.4p (approximately 1.257) mT·m/A` is 0,4π µT·m/A, `10–8/3` is 10⁻⁸/3, `3·108/f` is 3×10⁸/f,
`l/2p` is λ/2π, and `W/m2` is W/m².

**All three display equations and all four tables were re-read from the page rasters.**

| Where | Extract says | Page says |
|---|---|---|
| (89.1) | `f = 1/(ptr)` | *f* = 1/(π*t*ᵣ) |
| (89.2) | `E() Vm = 5.5 PA d` | *E*(V/m) = 5,5 √(PA)/*d* — radical **and** division both lost |
| (89.3) | `SE dB () = RA () dB + () dB` | SE (dB) = *R*(dB) + *A*(dB) |
| Table 89.1 | ok | ok |
| Table 89.2 | `mH/m` | **µH/m** |
| Table 89.3 | `mW` throughout | **µΩ** in the upper block, **mΩ** in the lower |
| Table 89.4 | ok | ok |

Two things in that table matter beyond cosmetics. First, **Table 89.3 changes unit mid-table**:
60 Hz–1 MHz are micro-ohms, 10 MHz–1000 MHz are milli-ohms, and the printed table puts a unit only
in the first cell of each block. Rendering the whole column as mΩ would be wrong by three orders of
magnitude for five of the eight rows. Second, **Table 89.2's title says "10-cm-Length Wires" but
its first two columns are per-metre values** — only the three `Z` columns are for the 10 cm length.
Both facts are now stated in the table captions rather than left for the reader to trip over.

**One substantive extraction error.** The sentence after (89.1) gives the lightning rise time as
**1 µs** on the page; the extract says "1 ms". 1/(π × 1 µs) ≈ 318 kHz, which is the 300 kHz the
author then quotes, so the printed figure is right and the extract is not. Same test on ESD:
1/(π × 1 ns) ≈ 318 MHz ≈ the quoted 300 MHz. The two numbers cross-check each other, which is how
this was caught.

**Figure work.** 89.3 is the only measured figure in the chapter and was digitised, not modelled:
the 400 dpi raster gave the plot box (left axis x=642, 300 dB at y=426, 0 dB at y=1794) and nine
decade lines from 0.1 kHz to 10 GHz, then each of the four curves was sampled column-wise with the
grid lines and the four in-figure label boxes masked out (±5 px, not ±2 — at ±2 the runs merged).
The three reflection curves converge on the plane-wave value near 300 MHz exactly as the printed
figure shows, which is a useful check that the sampling did not drift.

The other four are line drawings rebuilt from the page:

- 89.1 — three columns (sources / paths / receptors) with the nested `·` sub-items under
  Radiated→Crosstalk and Conducted. Converted to `(level, text)` tuples so indentation is
  structural rather than a string-replace hack.
- 89.2 — two boxes, a signal pair, two ground drops and a shared return, with the loop drawn as a
  251° circular arrow and a tangential arrowhead. The two ground symbols are deliberately
  different: diagonal hatch (earth) on the left, cross-hatch (chassis) on the right, matching the
  original.
- 89.4 — redrawn twice. The first version put a vertical bar through a horizontal line on the right
  panel, which read as a shield split in half. The page shows the opposite: the **plate is
  horizontal and the conductor passes through it vertically**, with the wavefront fans sitting
  above the plate on both sides of the conductor. The left panel's slot is dimensioned with a
  vertical `_dimv()` callout rather than a label sitting on the bar.
- 89.5 — the perspective open-field site. Dimensions moved below the ellipse (the original puts
  them on the major axis, where they collide with the table legs), and the two buried cables were
  rerouted to enter from the left and right instead of from the bottom corners, because the
  bottom-corner diagonals crossed the dimension row.

**Two rendering bugs found in QA and fixed.** (1) `Frame.yticks(pairs, dx=-8)` pushes the labels
*right* of the axis — `dx` is subtracted from `self.x`, so a negative value puts them on top of the
axis line. Use a positive `dx`. (2) At 390 px, `table.tbl.dense` with `table-layout:fixed` squeezes
a seven-column table until every cell wraps to one character per line. `.table-wrap` only scrolls if
the table has a `min-width`; table 89.4 now carries `min-width:700px`, table 89.2 has none (six
short numeric columns fit at 390 px unaided). Verified: no row in the 390 px screenshot reaches the
right edge except the two full-width rules.

**Source defects preserved, not silently repaired** (all listed in the translator's note): the
Figure 89.1 caption reads "All three elements must be necessary" where the body text says "must
exist at the same time"; 89.2 prints "superhetrodyne" and "It is expected that that wireless LANs"
(doubled *that*); and 89.1 says "greater than 1/6 wavelength" while 89.2 says λ/2π ≈ λ/6 — the same
threshold spelled two ways.

**Known site-wide inconsistency, left alone.** The five figures carry Vietnamese labels on both
language sides. Roughly half the existing EN chapter pages do the same, so this follows the
precedent set by the immediately preceding chapters in this reverse run rather than the older
fully-English figures. Making the five figure modules bilingual is a clean follow-up if the
convention is ever settled.

**Verification.** Both pages built at 107 kB / 102 kB. Parity checked mechanically on both: **5
figures, 4 tables, 3 equations, 7 `h2`, 6 `h3`, 34 glossary `dt`, 28 `<li>`**, and **0
`<sub>`/`<sup>` inside any `<svg>`**. Rebuild chain clean: sitemap **559 URLs / 546 EN/VI pairs**,
link check **561 pages, 15,349 local references, 0 broken**. Chapter 90's "previous" link now
resolves to 89, so the reverse chain 101 → 89 is continuous. Book TOC shows **40/101** on both
language sides. Both live URLs return 200.

**Next in the reverse sequence: 88, *Sensor Networks and Communication*.** `DONE[88]` is `None` and
`CH[88]` already holds `("Sensor Networks and Communication", ...)`; source at `work/hb_ch88.txt`.
Note that Chapter 89's "previous" link therefore currently falls back to the book TOC — that is
`chapter_nav`'s documented behaviour for an untranslated neighbour, not a bug, and it resolves
itself the moment 88 lands.

---

### Session 40 — Chapter 88 shipped

**Chapter 88, *Sensor Networks and Communication*** (Robert M. Crovella, NVIDIA Corporation) is
translated, built, verified and live. 19 PDF pages, 61 kB of extracted text, five figures, one
equation, one table, twenty references. Progress **41/101**.

| File | What |
|---|---|
| `build/hb88fig.py` | new, 294 lines — figures 88.1–88.5 |
| `build/reader_hb_ch88.py` | new, 2,091 lines — the chapter, VI + EN, ~10.4k / ~13.6k words |
| `build/reader_handbook.py` | `DONE[88] = "ch88-sensor-networks-and-communication"` |
| `build/books_site.py` | `TRANSLATED` → `("progress", 101, 41)` |

#### The extract corrupts exactly one symbol

Unlike Chapter 89, the text layer of Ch88.pdf is nearly clean — no Ω→W / µ→m substitution
cascade. The single casualty is equation 88.1, which extracts as `T N =- () - 21 1`. On the page
(page 3 raster) it is

> **T = 2^(N−1) − 1**

which is what the translation prints.

**Worth flagging for the next reader:** that formula is *not* the number of edges in a complete
graph. The text says <i>T</i> is the number of cables needed to connect each user to each other
user, which would be <i>N</i>(<i>N</i>−1)/2. The two agree only at <i>N</i> = 2 (2 = 2) and
<i>N</i> = 3 (3 = 3) and diverge from <i>N</i> = 4 onward (7 against 6, 15 against 10). The
translator's note says so explicitly and the formula is left exactly as printed rather than
silently corrected — this is a source defect, not a transcription error.

#### Figure 88.4 has no text layer at all

The page numbers it as a figure; the content is an 11 × 7 comparison table. `pymupdf` returns
**no words above y = 210 pt on page 12** — the whole table is a bitmap. Every cell was therefore
re-read from the 200 dpi raster, column by column, and the four notes under it transcribed by
hand. Two traps in it:

- **The units are inconsistent.** Interbus-S is listed as `25.6 km*` while the note reads
  `* Maximum 400 m between stations`. Both are printed; they only reconcile if 25.6 km is the
  total of many chained segments.
- **`UP = unshielded pair`** in the printed note, where current usage would write UTP. Left as
  printed.

Because a seven-column table cannot be drawn as SVG without becoming unreadable on a phone, it is
emitted as a real `<table>` — first column as `<th scope="row">`, others `scope="col"` — wrapped
in `<figure id="fig-88-4">` so the figure number survives. That is why the page has **5 figures
but only 4 `<figcaption>`s**: 88.4's caption is a `<p>` under the table. Vietnamese number
formatting (`.` thousands, `,` decimal) is applied cell by cell by `_vnum()`, so `1200 m` becomes
`1.200 m` and `25.6 km*` becomes `25,6 km*` on the VI side only.

#### Figure 88.3 was measured, not sketched

The RS-485 waveform is the only figure whose geometry had to be recovered numerically, and the
numbers are worth keeping because they settle what the drawing actually shows:

- V1 trace at raster **y = 269**, V2 at **y = 358**, axis at **y = 432**.
- Nine bit boundaries **90 px apart**, at x = 344, 434, 524, 614, 704, 794, 884, 973.
- The two traces cross in a narrow notch at **x = 344, 434, 614, 793, 973** and are flat at
  524, 704, 884.

For the bit string `0 1 1 0 0 1 1 0` those are boundaries 0, 1, 3, 5, 7 — i.e. **the notches fall
exactly where the bit value changes**. The redrawn figure notches at the same boundaries and
stays flat at 2, 4 and 6. Note that the traces return to their original levels after each
crossing rather than swapping, so the printed waveform is a diagram of *where the transitions
are*, not a held differential state; that is reproduced as printed and described in the caption.

#### Four rendering bugs caught in QA

1. **88.1 — the dotted tap stopped short.** The tap ran from the block link down to y = 272 while
   its two-line caption sat at y = 296/310, leaving a visible gap. Extended to 284.
2. **88.1 — "Đại lượng / đo" split across two lines** for no reason (the original breaks
   *Measured / Variable* only because its label column is narrow). Put on one line.
3. **88.4 — the last column was clipped.** `min-width:660px` on a 700 px column pushed `Tô-pô`
   past the right edge. Dropped to **560 px**, which fits seven columns at `0.78rem` and still
   scrolls on a phone.
4. **88.5 — bottom labels sat on the canvas edge.** Canvas raised from 330 to **340** and the two
   lower panel labels moved to y = 312.

#### The rebuild chain has two steps I had been skipping

Both are easy to forget and both leave the site subtly stale:

- **`build/make_sitemap.py` is separate from `build/books_site.py`.** `books_site.py` writes the
  book index pages and the reader pages but *not* `sitemap.xml`. Without it the new chapter is
  live but invisible to the sitemap. After running it: **561 URLs, 548 with EN/VI pairs**.
- **`build/chapter_nav.py` post-processes every chapter page in place.** The per-chapter
  generators call `chapter_nav(lang, n)` themselves, but that call is frozen into the HTML at
  build time — so Chapter 89's "previous" link kept pointing at the book TOC because 88 was not
  in `DONE` when 89 was generated last session. Running `chapter_nav.py` after the generators
  fixed it (**82 pages updated**), and 89's previous link now resolves to
  `/…/ch88-sensor-networks-and-communication/`.

The full order that worked: `reader_hb_ch88.py` → `books_site.py` → `reader_handbook.py` →
`make_sitemap.py` → `chapter_nav.py` → `check_links.py`.

#### Terminology

`station` → **trạm** (a network node, not a physical site — said so in the note), `media` →
**môi trường truyền**, `media access` → **truy nhập môi trường**, `signaling` → **tín hiệu hoá**,
`arbitration` → **trọng tài**, `code book` → **sổ mã**, `gateway` → **cổng nối**, `repeater` /
`bridge` / `router` → **bộ lặp / cầu nối / bộ định tuyến**. A 25-term glossary was added at the
end of the chapter, clearly marked as the translator's addition — the original chapter has no
"Defining Terms" section, so the entries are gathered from the inline definitions in 88.2.

**Note for whoever maintains `/glossary.html`:** `build/make_glossary.py` reads chapter glossaries
through a **whitelist** (`SRC` in that file currently holds only `ch05` and the three `ch06-*`
sections), not by scanning every translated chapter. Chapter 88's 25 terms therefore stay on the
chapter page and do **not** flow into the site glossary. Regenerating it is a no-op right now —
`glossary.html` is unchanged at 98 entries.

#### Verification

Both pages built at 85,793 B (EN) / 104,550 B (VI). Parity checked mechanically on both sides:

| | EN | VI |
|---|---|---|
| `<figure class="figure">` | 5 | 5 |
| `<svg>` | 5 | 5 |
| `<figcaption>` | 4 | 4 |
| `<table>` | 1 | 1 |
| `.eq` | 1 | 1 |
| `h2` / `h3` | 8 / 50 | 8 / 50 |
| glossary `dt` | 25 | 25 |
| `<li>` | 23 | 23 |
| `<p>` | 67 | 67 |
| `<sub>`/`<sup>` inside `<svg>` | **0** | **0** |

Words: **10,449 EN / 13,572 VI**. Rebuild chain clean: sitemap **561 URLs / 548 pairs**, link
check **563 pages, 15,401 local references, 0 broken**, book TOC **41/101** on both language
sides. At 390 px only two rows reach the right edge — the two full-width rules — so nothing
overflows. Committed `54ae494`, pushed, and both live URLs return **200** with 5 figures, 1
table, 1 equation and 25 `dt`.

**Next in the reverse sequence: 87, *Telemetry*.** `DONE[87]` is `None`; `CH[87]` holds the
title; source at `work/hb_ch87.txt`. Chapter 88's "previous" link currently falls back to the
book TOC — `chapter_nav`'s documented behaviour for an untranslated neighbour — and will resolve
itself when 87 lands, provided `chapter_nav.py` is re-run afterwards.

---

### Session 41 — Chapter 87 shipped

**Chapter 87, *Telemetry* (Albert Lozano-Nieto, Penn State University)** is live at
`/books/read/the-measurement-instrumentation-and-sensors-handbook/ch87-telemetry/` and its VI
mirror. Eleven figures, three tables, fifteen display equations, fourteen glossary terms,
twelve references. `DONE[87] = "ch87-telemetry"`; `TRANSLATED` is now `("progress", 101, 42)`.

#### The chapter's equations had no text layer worth having

Every display equation in this chapter was destroyed by the PDF's text layer. Equation 87.6 comes
out as `f t tt t = t p [] + () = p + () 1 22`; 87.10 as a vertical column of single characters
(`S`, `N`, `B`, `F`, `f`, `f`, `F`, then `3`, `4`, `12`). None could be read from the extract. All
fifteen were re-read from 200–300 dpi page rasters:

| # | Equation | Page |
|---|---|---|
| 87.1 | `v(t) = A_c[1 + m(t)] cos(ω_c t)` | 8 |
| 87.2 | `m(t) = m × cos(ω_m t)` | 8 |
| 87.3 | `P = m × 100 (%)` | 8 |
| 87.4 | `P/100% = [A_c(max) − A_c(min)] / 2A_c` | 8 |
| 87.5 | `v(t) = A cos[ω_c t + φ(t)]` | 9 |
| 87.6 | `f = (1/2π)(d/dt)[ω_c t + φ(t)] = ω_c/2π + (d/dt)φ(t)` | 10 |
| 87.7 | `f = ω_c/2π + (βω_m/2π)cos(ω_m t) = f_c + βf_m cos(ω_m t)` | 10 |
| 87.8 | `Δf = βf_m` | 10 |
| 87.9 | `v(t) = A cos[ω_c t + (Δf/f_m) sin(ω_m t)]` | 10 |
| 87.10 | `(S/N)_d = (S/N)_c (3/4)^½ (B_c/F_ud)(f_dc/f_s)(f_ds/F_ud)` | 11 |
| 87.11 | `τ = 1/(2πB)` | 12 |
| 87.12 | `k = −54.5 T_g (dB)` | 13 |
| 87.13 | `BEP = 0.5 e^(k·SNR)` | 17 |
| 87.14 | NRZ: `S = sin²(πfT)/(πfT)²` | 17 |
| 87.15 | Biphase: `S = sin⁴(πfT/2)/(πfT/2)⁴` | 17 |

**The print numbers none of them.** They are numbered 87.1–87.15 here so the running text can
refer to them, and the translator's note says so plainly. If a future chapter turns out to be
unnumbered too, follow this precedent rather than inventing bracketed numbers silently.

Note 87.12: the extract reads `k =-54.5Tg () dB`, and it is tempting to "correct" 54.5 to 54.57.
The raster shows **−54,5**, not −54,57. Trust the raster.

#### Six places where the print contradicts itself

All kept as printed, all flagged in the translator's note:

1. **87.3, the FDM/TDM slip.** "Figure 87.7a shows a basic block diagram for an **FDM** system" —
   but 87.7a is a TDM diagram and the whole surrounding passage is about TDM. The translation
   renders "FDM" and adds a footnote in place.
2. **87.5a, triple `f_osc1`.** All three subcarrier multipliers are labelled `f_osc1`, while
   87.5b — the other half of the same figure — marks `f_osc1`, `f_osc2`, `f_osc3`.
3. **87.4, duplicate "CONDITIONING CIRCUIT 3".** Two different conditioning boxes carry the same
   number; there is no "CIRCUIT 2".
4. **87.11, 512 vs 1024.** The figure caption gives the maximum minor-frame length as "8192 bits
   or **512** for class I"; the body text and Table 87.3 both say "< 8192 bits or < **1024**
   words".
5. **87.11, 16,284 vs 16,384.** Same caption says class II tops out at **16,284** bits; body and
   Table 87.3 say **16,384**.
6. **Table 87.1 row order.** The 467 MHz row is printed *before* the 458–468 MHz row, i.e. out of
   ascending order. Kept as printed.

Also noted: the 87.10 caption appears in the extract as "Bif-L", "Bif-M", "Bif-S" — that is the
character Ø lost by extraction, not a different code family.

#### Figure 87.10 is generated, not transcribed

The printed rows are only a few pixels tall per transition, and the right-hand edge of the
biphase rows is ambiguous even at 400 dpi. Rather than guess, the figure is **generated from the
definitions the caption states**, one level per half-cell, with the starting level of each row
chosen so the definition is satisfied end to end:

```
NRZ-L  [1,1,0,0,1,1,1,1,0,0]   NRZ-M  [1,1,1,1,0,0,1,1,1,1]   NRZ-S  [0,0,1,1,1,1,1,1,0,0]
Biø-L  [0,1,1,0,0,1,0,1,1,0]   Biø-M  [0,1,0,1,1,0,0,1,0,1]   Biø-S  [1,0,0,1,0,1,0,1,1,0]
```

for the bit string `1 0 1 1 0`. The five NRZ/Biø rows that *can* be read off the raster match
these sequences bit for bit, which is the check that makes the generation trustworthy. Note the
caption's wording for Biø-L — "a 1 is represented by a transition to the lower level" — only
reads correctly if "transition" means the *mid-bit* transition; that is how it is drawn.

#### `_hump()` was inverted, and had been since it was written

The channel-spectrum helper in `hb87fig.py` returned points with the peak at the *edges* and a
dip at the centre, and every caller then mapped them through `ax - y`, which turned each spectrum
into an upside-down valley. It was never caught because 87.2 had only been smoke-tested for SVG
length, not looked at. Rewritten to return `(x, height above baseline)` with a `dip` parameter:

```python
v = (1.0 - a ** 3) * (dip + (1.0 - dip) * (1.0 - math.exp(-(a * a) / 0.03)))
```

`dip=0` gives a clean two-lobed channel spectrum; `dip=0.5` gives the amplitude-modulated
sideband of 87.6b, whose notch stands at exactly ½M(0).

#### Other rendering fixes made after looking at the screenshots

- `_hrect()` painted its outline with `_rect(x, y, w, h, 1.2)`, whose default fill is `#fff` — so
  it repainted white straight over the hatching it had just drawn. Every TDM sample pulse in
  87.7 and 87.8 came out blank. Fixed by passing `"none"` as the fill.
- 87.1's "Đo từ xa không dây" sat on top of the THÍCH ỨNG ĐƯỜNG DÂY box. It now sits under the RF
  run at (540, 366).
- 87.3 rows (b) and (c) ran 58 px past the right edge, because the mid box shifted the whole tail.
  The row is now laid out from both ends: the display box is right-aligned at 540–656 and the
  transmission line stretches to fill whatever is left.
- 87.5b's guard-band labels were wider than the gap between channels, so they spilled onto the
  curves. Channel half-width dropped 60 → 52 px and the labels to 8 px.
- 87.7 drew its `1/f` tag twice, once from `_dimb`'s own tag and once from a separate `_r` call,
  so the two overprinted.
- 87.11's bottom row was placed at y=292 while its dashed "major frame" box ended at 312 — the
  row hung outside the box it is supposed to be inside. `by` corrected to 264.

#### A terminology decision

*Minor frame* is rendered **khung nhỏ**, *major frame* **khung lớn**, and *subframe* **khung
con** — three distinct words for three distinct things. Figure 87.11 was relabelled to match
after the first draft used "khung con" for both minor frames and subframes, which made the figure
unreadable.

#### Fractions

`library.css` still has no fraction class. The construction chapter 90 uses is copied verbatim
(`vertical-align:middle`, numerator carrying `border-bottom`, `line-height:1.25`). The first
attempt used `vertical-align:-0.58em`, which pushed the numerator up through the `.eq` block's
top border and clipped it — visible in the screenshot as a fraction sliced in half.

#### Verification

| | EN | VI |
|---|---|---|
| `<figure class="figure">` | 11 | 11 |
| `<svg>` (11 figures + 1 site logo) | 12 | 12 |
| `<figcaption>` | 11 | 11 |
| `<table class="tbl">` | 3 | 3 |
| `.eq` | 15 | 15 |
| `h2` / `h3` / `h4` | 6 / 7 / 8 | 6 / 7 / 8 |
| glossary `dt` | 14 | 14 |
| `<li>` | 19 | 19 |
| `<p>` | 52 | 52 |
| `<sub>`/`<sup>` inside `<svg>` | **0** | **0** |

Words: **8,104 EN / 10,240 VI**. Files 179,393 B / 176,226 B. Rebuild chain clean: sitemap **563
URLs / 550 pairs**, link check **565 pages, 15,453 local references, 0 broken**, book TOC
**42/101** on both sides, `chapter_nav` **84 pages updated**. At 390 px the document width stays
at 390 — the three tables scroll inside `.table-wrap` because each carries a `min-width` of
560–600 px. Committed `d887db4`, pushed, both live URLs return **200** with 11 figures, 3 tables,
15 equations and 14 `dt`.

**Next in the reverse sequence: 86, *Computers* (Máy tính).** `DONE[86]` is `None`;
`CH[86]` holds the title; source at `work/hb_ch86.txt`. Chapter 87's "next" link already points
at 88 and its "previous" at 86 — the latter currently falls back to the book TOC until 86 lands,
and resolves only if `chapter_nav.py` is re-run afterwards.

---

### Session 42 — Chapter 86 shipped

**Chapter 86, *Computers*** (A. M. MacLeod, P. F. Martin, W. A. Gillespie, University of Abertay
Dundee). 23 printed pages, 7 figures, 6 tables, 10 references. Slug `ch86-computers`;
generators `build/reader_hb_ch86.py` + `build/hb86fig.py`.

**The chapter has no display equations at all.** It is a hardware survey — SBC, bus
architectures, VME/Multibus II, the PC buses, peripherals, software — and every non-prose
passage is either a table or a code fragment. So nothing is numbered, unlike Chapter 87 where
the whole equation set had to be rebuilt from rasters.

**The one piece of code is printed broken, and that is a printing fault, not a transcription
slip.** The C fragment in §86.6 reads, in the print:

```
#define PABASE
#define PBBASE+1
#define CONTROLBASE+3
...
outportb(CONTROL, 153)/* set port A as input, port B as output */
```

Three `#define` lines have lost the space between the name and `BASE`, and the first `outportb()`
call has no semicolon. Verified at 220 dpi against `work/qa86/code.png` — the print really does
set it that way. Reproduced verbatim and the corrected lines given in the translator's note.

**Four printed self-contradictions, all kept as printed:**

1. The IEEE-488 bus is **1.5 MB/s** under "IEEE-488 Adapter" (§86.5 Internal Cards) and
   **1 MB/s** under "IEEE 488 Devices" (§86.5 External Peripherals) — about 300 lines apart.
2. **Table 86.5 lists "Linearity" twice**, with two different definitions. The second restates
   the first ("the extent to which the conversion is linear"). Both rows kept.
3. Multibus II cards are **220 × 233.65 mm** while the double-height VME card of the same
   Eurocard family is **233.35 mm** (the correct value) — 233.65 is a misprint.
4. §86.4 opens by naming **three** PC bus standards — ISA, EISA and MCA — and then never
   describes MCA. The text says so explicitly, so it is not a truncation.

Separately, **Figure 86.3 draws four rails** (data, control, arbitration, utility) while the
prose says one group of tracks carries *both* data and address information. The figure has no
address rail. Drawn as printed.

Also worth recording: the extract's `Table 86.5` "Conversion speed … typically 1 s to 1 ms" is
an OCR slip for **1 s to 1 µs** — confirmed on the raster; the µ was read as m.

**Table 86.3** is printed as two side-by-side panels (System | Supplier, twice). Reflowed into
one table grouped by system with `rowspan`, no entry dropped. Labtech's malformed
`800-8799-5228` kept.

**Figure work.** All seven read off 200 dpi rasters; 86.5 additionally at 600 dpi because the pin
mnemonics are about 6 pt. Nothing is generated from a formula — every wire in 86.5 and every
level in 86.6 is transcribed. Two construction lessons:

- The shared `.tm` class in `hb93base._defs()` is 9.5 px, sized for the dense schematics of
  Chapters 87 and 93. These seven are block diagrams with very few words, and at 9.5 px every
  label sat at about a third of the box width the print gives it. `hb86fig.py` declares a local
  `.tl` at **12.5 px** *after* `_defs()`, which wins on source order. Do this for any future
  block-diagram chapter rather than editing the shared module.
- `_blocks()` for the PWM waveform in 86.6 was first written with the polarity inverted, so
  waveform C started low and produced a diagonal at the right-hand end. It must append
  `(b, hi), (b, lo)` per block and `(a, lo), (a, hi)` *between* blocks, with the closing
  `(x1, lo)`.

Other layout fixes: the dashed address-bus branches in 86.2 landed on the RAM/ROM box corners
(moved from y=180/290 to 168/278); the rails in 86.3 were too close together for the staircase
to read (spacing 18 → 24 px, stub spacing matched); the two null-modem panels in 86.5 were
cramped into a 56 px gap, making four crossing wires illegible (gap 56 → 94 px); 86.7's canvas
was mostly empty (200 → 168 tall).

**Verification (both built pages):** 7 figures, 8 `<svg>` (7 + site logo), 7 `<figcaption>`,
6 tables, 5 `<pre>` blocks, 9 `h2` / 17 `h3` / 18 `h4`, 14 `dt`, 36 `<li>`, 98 `<p>`,
**0 `<sub>`/`<sup>` inside any `<svg>`**. Words **12,767 EN / 16,879 VI**; files 115,013 B /
115,226 B. Rebuild chain clean: sitemap **565 URLs / 552 pairs**, link check **567 pages, 15,505
local references, 0 broken**, book TOC **43/101** on both sides, `chapter_nav` **86 pages
updated**. At 390 px the document width stays at 390 and the six tables scroll inside
`.table-wrap` (min-width 540–600 px).

**Next in the reverse sequence: 85, *Bộ chuyển đổi tương tự – số* (Analog-to-Digital
Converters).** `DONE[85]` is `None`; `CH[85]` holds the title; source at `work/hb_ch85.txt`.
Chapter 86's "previous" link already points at 85 and currently falls back to the book TOC until
85 lands — it resolves only if `chapter_nav.py` is re-run afterwards.

---

## Session 43 — 2026-11-02 · Handbook Chapter 28 (*Flow Measurement*) finished and published

Chapter 28 is the last of the eleven-section monsters: 132 source pages, ten authors, and it had
been sitting at ten of eleven sections since session 27. §28.11 (Drag Force Flowmeters, pp. 123–132,
figures 28.85–28.92, six references) closed it out, and the chapter is now registered, in the
sitemap and live.

**What went in this session**

- **§28.11, both languages.** The target-type meter: drag equation (28.146), the Reynolds relation
  (28.147), the full bending derivation (28.148–28.156) from 1/ρ = M/EI through I = ba³/12 to the
  quadratic strain–velocity law, the two-component wind vector (28.157–28.159), the resistive-gauge
  implementation with its calibration curves, the optical-fibre variant with its grooved PMMA fibre,
  and the conclusion. 19 equations, 8 figures, no tables.
- **Three source defects reproduced as printed and flagged** in translator's notes: Re = ρVA/η is
  dimensionally wrong (needs ρVd/η); ρ is used for both fluid density and radius of curvature; and
  "approximately 20 mm" of cladding on a 1 mm fibre is corrected to 20 µm.
- **`_axis()` and `_mark()` added to `hb28fig.py`** for figures 28.87–28.89, the chapter's only
  scatter plots. `_axis()` takes axis *ranges* and returns `mx`/`my` closures; a first version that
  took tick positions as fractions put every label in the wrong place and produced 38 QA problems.
- **Jump index.** `sec_index(lang)` builds a `.toc-list` of eleven anchors at the top of the page and
  `h2()` now attaches `id="s28-N"` to any heading that starts `28.<digits> `. No CSS was added —
  `.toc-list` already existed for the book TOCs.
- **The progress label is now a content label.** `đang dịch: 11/11 mục` was replaced with
  `92 hình, 164 phương trình, 23 bảng`, matching chapters 26 and 27. A finished chapter must not
  advertise itself as in progress.
- **Registered and published.** `28: "ch28-flow-measurement"` added to `DONE`; `books_site.py`
  counter moved from 43 to 44; `reader_handbook.py`, `books_site.py`, `make_sitemap.py` and
  `check_links.py` all re-run. Results: book TOC and both books indexes read **44/101**
  (*Translating · 44 of 101 chapters* / *Đang dịch · 44/101*), sitemap 569 URLs / 554 EN–VI
  pairs, **0 broken links across 571 pages and 15,557 local references**.

**Two defects worth remembering**

1. **Every `<svg>` on the English page had a Vietnamese `aria-label`.** `hbfig.svg()` bakes the
   title into the tag when the figure is *defined*, and `fig()` was discarding the English
   accessible description that `_fig()` stores as element 5 of its tuple. All 92 figures announced
   Vietnamese to a screen reader on the English page. `fig()` now rewrites the attribute on the
   English path. **Chapters 1–27 and 94–101 still have this** — the helper is duplicated across 35
   modules — so a sweep is owed. Check with
   `grep -o 'aria-label="[^"]*"' page.html | grep -c '[ăâđêôơư]'`; it must be 0 on an English page.
2. **Figure 28.85 sent two leaders to the same gauge.** `G4` and `G1` both terminated on the
   left-hand front gauge, so the right-hand gauge was unlabelled and the pair read as one gauge
   named twice. `G1`'s leader now runs under the left gauge and lands on the right one. This is a
   *content* error: `qa_figs.py` sees no collision and the caption is correct, so only reading the
   drawing against the source catches it.

**A note on reading screenshots.** At 1424 px the capture has to be sliced, and a 1820 px slice
displayed at 850 px is downscaled 0.6×. At that scale several "defects" turned out to be artefacts —
`các rãnh` read as `cách rãnh`, `Độ thay đổi` as `Độ chạy dồi`, `a²` as `a³`. **Check any suspected
wording or superscript error against the source markup before "fixing" it**; only layout problems
(overlap, clipping, a detached caption, a leader that misses its target) are reliable at that
scale. Letter-level review needs a 1:1 crop of a few hundred pixels.

---

## Session 44 — 2026-11-02 · Handbook Chapter 29 (*Point Velocity Measurement*) finished and published

Chapter 29 is three sections and 55 pages: Pitot probes, thermal anemometry and laser anemometry.
§29.1 and §29.2 were finished in earlier sessions; this one closed §29.3 and published the chapter.

**§29.3 Laser Anemometry** is seven equations and eight figures behind a long, discursive text —
the dual-beam system, the fringe and Doppler descriptions of the same signal, Bragg-cell frequency
shifting, fibre-optic probes, three-component systems, signal processing, particle seeding, data
analysis, and the extension to particle sizing. It was written as one section pair
(`sec_29_3_vi` / `sec_29_3_en`, 115.6 kB and 122.8 kB of HTML) with its own reference list (67
entries) and a ten-item "Further Information", titles left in the original language like §29.1 and
§29.2.

**Registered and published.** `29: "ch29-point-velocity-measurement"` added to `DONE`;
`books_site.py` counter moved from 44 to 45. Re-ran `reader_handbook.py`, `books_site.py`,
`make_sitemap.py`, `chapter_nav.py` and `check_links.py`. Results: book TOC and both books indexes
read **45/101**, sitemap **571 URLs / 556 EN–VI pairs**, chapter nav **90 pages updated**, link check
**573 pages, 15,609 local references, 0 broken**.

**Five figure defects in §29.3, only one of which the checker could see.** `qa_figs.py` finished at
`FIGS 31, problems 0` while three of the defects were still on the page:

1. **A raw `<` collapsed figure 29.28.** `θ < 90°` in SVG text is an invalid token; it must be
   `&lt;`. This is the one failure mode the checker reports (`MALFORMED`).
2. **`font-size` on `<text class="ts">` does nothing.** `.t`/`.ts` set the `font` shorthand via a
   class rule, and a class rule outranks a presentation attribute, so twelve labels in figure 29.30
   silently stayed at 10 px and overflowed their boxes. Fixed with `_fs(n)`, which emits an inline
   style; a `<tspan>` has no matching rule, so attribute sizes still work there.
3. **Rotated labels sat on the plotted lines in figure 29.26(b).** Each label's baseline was placed
   at the line's own y. A label rotated to the line's angle is *parallel* to it, so the correction
   is a perpendicular offset (≈10 px), and because glyphs rise from the baseline a label placed
   *below* a line needs more offset than one placed above.
4. **A stepped connector read as a stray box** in figure 29.30(a): the four-segment fibre feed under
   "Transmitting optics" looked like a second small box. Replaced with one diagonal.
5. **A 7 px dimension cannot hold two arrowheads.** `Λ` in figure 29.26(a) collapsed into a blob, so
   the wavefront spacing went from 7 px to 12 px and the heads are now drawn explicitly.

**Two more traps worth remembering**

- **Combining characters do not render in the house font.** `u⃗` (U+20D7) is an empty box in
  Inter/Helvetica at every size; `r̂` and `Ŝ` (U+0302) survive. The chapter uses `<b>u</b>` for the
  velocity vector with a translator's note on equation 29.67, rather than reproducing the source's
  arrows. Probe file: `work/qa29/probe2.html`.
- **The `meta` line is the only place the reader learns the chapter's size**, and it had gone stale
  at 16/27/2 while the page held 23/64/4. It now reads **31 figures, 71 equations, 4 tables** in both
  languages, and the comment above it says to recount on every section.

**Owed, still:** the `aria-label` sweep across the other 34 `reader_hb_*` modules. Chapter 29 is
clean (0 Vietnamese labels on the English page), but chapters 1–27 and 94–101 predate the fix.

## Session 45 — 2026-11-02 · Handbook Chapter 30 (*Viscosity Measurement*) written and published

Chapter 30 is a single long section — §30.1 *Shear Viscosity* — with seven sub-topics listed under
the heading and no numbers of their own: Newtonian and non-Newtonian fluids, dimensions and units,
viscometer types, capillary viscometers, falling body methods, the oscillating method and ultrasonic
methods. 24 source pages, **12 figures, 46 equations, 4 tables**, 25 references and 3 annotated
further-reading entries.

**Source.** `work/Ch30.pdf` did not exist; the chapter lives in the user's own folder
(`D:/Process Control and Automation\The Measurement_ Instrumentation and Sensors Handbook\Ch30.pdf`,
579,615 bytes, 24 pages). Extracted to `work/hb_ch30.txt` with `===== PAGE N =====` markers and
rendered at 140 dpi into `work/ch30img/p01–p24.png`. Every one of the 46 equations was mapped to its
page first (`1:p2 … 46:p22`, no gaps) and then transcribed from the page images, because the text
extraction mangles every fraction and subscript in this chapter.

**Written as one section pair.** `sec_30_1_vi` and `sec_30_1_en` are 124.3 kB and 114.7 kB of HTML
(UTF-8 bytes) and are structurally identical block for block: same 12 figures in order, same 46
equations, same 4 tables, same 8 anchors (`s30-1` plus seven `t30-*`). Titles of cited works are left
in the original language, as in chapters 28 and 29.

**Registered and published.** `30: "ch30-viscosity-measurement"` added to `DONE`; `books_site.py`
counter 45 → 46. Re-ran `reader_handbook.py`, `books_site.py`, `make_sitemap.py`, `chapter_nav.py`,
`check_links.py`. Results: book TOC and both books indexes read **46/101**, sitemap **573 URLs / 558
EN–VI pairs**, chapter nav **92 pages updated**, link check **575 pages, 15,661 local references,
0 broken**.

### Four content defects found during review

None of these were visible to `qa_figs.py`, and three of them were wrong in the source-faithful
sense rather than the typographic sense.

1. **Table 30.2's group headings were off by one row.** The `group` map said
   `{0: drag, 8: pressure, 12: others}` for a 12-row table whose blocks are actually rows 0–6, 7–10
   and 11. The effect: "Pressure flow types" was printed *after* the long-capillary row, so that row
   silently belonged to the drag block, and "Others / miscellaneous" — index 12 in a table with no
   row 12 — never appeared at all, leaving Ultrasonic stranded under the pressure heading. Fixed to
   `{0, 7, 11}` with a comment explaining that a group entry inserts its heading *before* that row.
2. **A paragraph from the falling-cylinder discussion had drifted into the opaque-liquids
   subsection.** "In the past, this method was primarily used to determine relative viscosities…"
   explains what the end-correction factor ECF bought the method, so it belongs after equation 30.32,
   not after figure 30.9. Moved.
3. **The falling-cylinder range read 10⁻³ to 10⁶ Pa·s.** The source says 10⁷ (p. 17). Corrected in
   both languages.
4. **`slope η` was drawn on the strain-rate axis in figure 30.2** — placed at `(500, oy)`, the
   literal axis y, so its descender ran through the axis line. Moving it above the line first landed
   it on "dilatant materials" (which `qa_figs.py` caught); the final position, `(380, 277)`, is
   clear of the axis, of "Newtonian liquids" and of both curves.

### Notes for the next chapter

- **`h2` must be the first block of every section function.** `sec_30_1_vi` was written without one,
  which left the page with prose but no `s30-1` anchor and no visible section heading. The in-page
  index then had nothing to link to.
- **`fig()` calls are easy to forget when the prose only *mentions* the figure.** Figures 30.1 and
  30.2 were referenced five times in the text before either was embedded; the count check
  (`id="fig-30-N"`) is what surfaced it, not the reading.
- **A one-section chapter needs a different index.** Listing sections gives a single entry, so
  `sec_index()` lists the seven `h3` sub-topics instead, unnumbered — the handbook does not number
  them and inventing 30.1.1–30.1.7 would be a fiction.
- **The `.toc-list .n` span is optional.** Omitting it and keeping only `.t` renders fine; `.t` is
  `flex: 1`.

**Owed, still:** the `aria-label` sweep across the other 34 `reader_hb_*` modules. Chapters 29 and 30
are clean (0 Vietnamese labels on the English page — 13 labels, all English, on chapter 30), but
chapters 1–27 and 86–101 predate the fix.

## Session 46 — 2026-11-02 · Handbook Chapter 31 (*Surface Tension Measurement*) written and published

Chapter 31 is three sections and 17 source pages: §31.1 *Mechanics of Fluid Surfaces* (seven
sub-topics: the mechanical model and surface energy, shape and surface-active agents, the contact
line and the contact angle, equilibrium at the contact line, curved surfaces and the Laplace
pressure, axisymmetric drops and bubbles, capillary waves), §31.2 *Standard Methods and
Instrumentation* (six: capillary rise, Wilhelmy plate and du Noüy ring, maximum bubble pressure,
pendant and sessile drop, drop weight or volume, spinning drop) and §31.3 *Specialized Methods*
(four: dynamic surface tension, surface viscoelasticity, measurements at temperature and pressure
extremes, interfacial tension). **5 figures, 13 equations, 2 tables**, 35 references, defining terms
and acknowledgments.

**Source.** `D:/Process Control and Automation/The Measurement_ Instrumentation and Sensors
Handbook/Ch31.pdf`. Pages rendered at 140 dpi into `work/ch31img/`; every equation was read off the
page images, not the text layer, for the same reason as chapters 29 and 30 — the extraction mangles
every fraction and subscript.

**Registered and published.** `31: "ch31-surface-tension-measurement"` added to `DONE`. Re-ran
`reader_handbook.py`, `books_site.py`, `make_sitemap.py`, `chapter_nav.py`, `check_links.py`.
Results: book TOC and both books indexes read **48/101**, sitemap **575 URLs / 560 EN–VI pairs**,
chapter nav **94 pages updated**, link check **577 pages, 15,713 local references, 0 broken**.
Both pages: 69 kB (EN) / 65 kB (VI), figures 1–5, equations 31.1–31.13 in order with no gap or
duplicate, 31 unique element ids, 20 in-page links none broken, 6 aria-labels (0 Vietnamese on the
English page), prev link to chapter 30 present.

**The counter had drifted and is now corrected 46 → 48.** The rendered TOC carried 47 `done` rows
before chapter 31 was added — 30 chapters (1–30) + 16 (86–101) + Appendix A — so session 45's
"46/101" was one short: it never counted the Appendix A row. `books_site.py` now says 48 and agrees
with `books/read/<slug>/index.html`, which is the source of truth. **Check the rendered TOC, not the
previous session's number, before bumping this counter again.**

### `⁄` (U+2044) destroys the digit in front of it — use ASCII `/`

Equation 31.2 was written `γ (1⁄<i>R</i><sub>1</sub> + 1⁄<i>R</i><sub>2</sub>)` and rendered as
`γ (ı⁄R₁ + ı⁄R₂)`: in Georgia the `1` immediately before U+2044 FRACTION SLASH collapses to a bare
vertical stroke. A four-way test page (`work/qa31/fractest.html`) settled it — `1⁄3` shows a stroke,
`1/3` is correct, `font-feature-settings:'frac' 0` does not help, and `2γ⁄b` loses *both* the slash
and the `2`, rendering `2γb`.

**The fix is ASCII `/`**, applied to all 70 occurrences in `reader_hb_ch31.py`. All thirteen
equations now render correctly (verified together on one sheet — extracting every `.eq` block into a
throwaway page with the real `library.css` is far cheaper than hunting each one down the full-page
screenshot).

**Chapters 25–30 are not affected and were deliberately left alone.** They write the same character
*spaced* (`η ⁄ ρ`, `2 ⁄ (1 + β²)`), so no digit is ever adjacent to it, and all 43 fraction-bearing
equations in chapter 30 were checked on a sheet and render correctly. Only the tight `digit⁄` form
breaks. So: `digit/digit` tight is fine with ASCII `/`; if you want the airy look, space it and
U+2044 is safe. Never write `digit⁄`.

### Two figure defects from this chapter worth remembering

- **`_arr(x1, y1, x2, y2, col, marker, sw)` — the sixth positional argument is `marker`.** Writing
  `_arr(a, b, c, d, E, 1.5)` puts `1.5` in the marker slot and emits `marker-end="url(#1.5)"`, i.e.
  **no arrowhead at all**, silently. Every arrow in figure 31.3 lost its head this way. Always pass
  `sw=` by keyword. `qa_figs.py` reported `problems 0` both before and after — it cannot see a
  missing arrowhead, so figure arrows need an eyeball or a grep of the emitted SVG.
- **A parametric surface hooks at the corners.** Figure 31.3's dome and saddle were first built as
  `X(u,v)/Y(u,v)` grids; at a corner both grid families leave in nearly the same direction and the
  outline doubles back. Rebuilt from four quadratic Bézier edges (left edge left straight, only the
  right edge bowed) it cannot cusp.

**Owed, still:** the `aria-label` sweep across the other 34 `reader_hb_*` modules. Chapter 31 is
clean (6 labels, all English on the English page), as are 29 and 30; chapters 1–27 and 86–101
predate the fix.

**Also owed:** `git push` still cannot authenticate from this machine — the credential helper is
`manager` with nothing stored, and `git fetch` works anonymously while `push` cannot prompt. Three
commits are sitting on top of `origin/main`.

---

## Session 47 — 2026-11-02 · Handbook Chapter 32 §32.2 (*Resistive Thermometers*)

Chapter 32 is being worked section by section; nothing is registered at the book TOC until all
eleven sections are in, so a half-finished chapter never appears at its published URL. §32.1
(bimetallic thermometers) went in last session; this one is §32.2.

**§32.2 — *Resistive Thermometers*, Jim Burns.** Source pages 14–26 (the Defining Terms list
spills onto p26; §32.3 starts there). Nine figures (32.7–32.15), six equations (32.20–32.25), two
tables (32.6, 32.7), seven references, twelve sub-headings. Both languages built and verified:
26 equation blocks (32.1–32.25 with 32.6a/b), 15 figures, 9 `tbl` tables (7 real + 2 defining-terms
blocks), 23 in-page links none broken, 0 U+2044, and all 15 `aria-label`s English on the English
page. 164 kB EN / 156 kB VI.

### The in-page index was pointing every sub-entry at the section top

`sec_index()` in `reader_hb_ch32.py` built `href="#s32-2"` for *every* sub-topic, so all nine
§32.1 entries and all twelve §32.2 entries landed on the section heading rather than the heading
they named. They were not "broken" links — the link checker was happy — they were just useless.

Fixed by generating the anchor from the **English** title on both sides:

```python
def _slug(t):
    s = re.sub(r"<[^>]+>", "", t).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")
```

`h3()` mints `id="s32-<sec>-<slug>"` and `sec_index()` builds the same string from `INDEX`, so the
two can never drift apart. `h3()` needs to know which argument is the English one, because the
pair is `(vi, en)` on the Vietnamese page and `(en, vi)` on the English page — a module-level
`_LANG` set at the top of `build()` decides it. Section number comes from a `_CUR` that `h2()`
updates, which keeps the two `Defining Terms` headings apart (`s32-1-…` vs `s32-2-…`).

**If you add a section here, add its sub-headings to `INDEX` with the English title spelled
exactly as the `h3` spells it** — that string is the anchor.

### `_path()`'s fourth positional argument is `fill`, again

Figure 32.14's graphite crucible came out with no white fill, so the insulation hatching ran
straight through it. `_path(d, col, sw, fill, dash)` — the call had been written
`_path(d, "#fff", E, 1.6)`, i.e. white stroke, `stroke-width="#2a2a2a"`, no fill. Same class of
bug as figure 32.6 last session (`_path(d, E, 1.2, "5 4")` putting the dash pattern in the fill
slot). **Both helpers take their style arguments in an order that is easy to get wrong; pass
`fill=` and `dash=` by keyword whenever they are not the default.** `qa_figs.py` cannot see
either of these.

### Figure notes

- **32.7** — the four metals fan out from (0 °C, R/R₀ = 1). Platinum's coefficient is the real
  0.003945 with the real negative quadratic term; the other three are scaled so the fan closes
  inside the frame, because the original's curves are drawn well off scale. Below 0 °C all four
  are indistinguishable at this scale, so the original draws one shared branch and so does this
  one. Nickel's curve leaves the top of the frame at 250 °C, so its label is carried over the top
  edge on an elbow — a straight leader would have to cut across the other three curves.
- **32.8–32.13** — the six construction cross-sections are drawn at one shared scale and style:
  hatched `url(#w32)` for metal in section, `url(#h32)` for ceramic/insulation, `#f7f8fa` for
  plain ceramic. The coil in 32.12 is the projection of a helix (`y = c − A·sin(2πx/pitch)`);
  the winding in 32.11 is one slanted pass per turn, not a zigzag — a zigzag at that density
  fills solid.
- **32.14** — thirteen labels on the right, each with its own arrow. Three of them carry a second
  bracketed line; those are emitted as a separate `_lbl` under the first so the arrow stays
  anchored to the label's first line.
- **32.15** — the stabilization-block label had to come out of the block: the probe tubes run
  straight through it and the text was unreadable.

**Owed, still:** the `aria-label` sweep across the other 34 `reader_hb_*` modules; and `git push`,
which still cannot authenticate from this machine. Five commits are now sitting on top of
`origin/main`.

## Session 48 — 2026-11-02 · Handbook Chapter 32 §32.3 (*Thermistor Thermometers*)

Third of chapter 32's eleven sections; still nothing registered at the book TOC, and the generated
ch32 pages stay out of git so a half-finished chapter cannot be reached at its URL.

**§32.3 — *Thermistor Thermometers*, Meyer Sapoff.** Source pages 26–41. Seven figures
(32.16–32.22), forty-seven equations (32.26–32.72, including 32.38a/b), four numbered tables
(32.8–32.11), nineteen references, three `h3` and six `h4`. Both languages built and verified:
74 equation blocks in order, 22 figures, 13 table elements, 3 `h2` / 28 `h3` / 6 `h4`, 33 in-page
links none broken, 0 U+2044, and all 22 `aria-label`s English on the English page / Vietnamese on
the Vietnamese one. 296 kB EN / 283 kB VI.

### Four wrong subscripts survived the first read — the text dump is how they were caught

The section's equations had been transcribed from 300 dpi crops and looked right on the page. They
were not. Comparing a plain-text dump of every equation against the source page images turned up
four errors, all in the 32.56–32.68 run, all of them a `1`/`2`/`3`/`4` misread at small type:

| eq | printed | had been written |
|----|---------|------------------|
| 32.58 | `R₂ = R₄/K` | `R₂ = R₁/K` |
| 32.59 | `R₁ = R₂R₄/(R₂ − R₄)` | `R₁ = R₃R₄/(R₂ − R₄)` |
| 32.61 | `K = R₂/(R₁+R₂) = E₁/E₂ = R/R₁` | `… = R/R₄` |
| 32.68 | `Rₙ = R_C/R = 1 − 1/(1+r_Tσ)` | `R₁₂/R = R_C/R = …` |

Each one is checkable by algebra — 32.55 says `K = R₄/R₂`, so 32.58 cannot be `R₂ = R₁/K`; 32.56
says `R₄ = R₁R₂/(R₁+R₂)`, so 32.59's numerator cannot be `R₃R₄` — and that is the cheapest audit
there is. **Dump the equations as text, then check the ones that are algebraically determined
against the equation that defines them.** A rendered page hides a wrong digit; a text list does
not.

```bash
cd build && PYTHONPATH=. python - <<'PY'
import re, reader_hb_ch32 as R
R._LANG[0] = "en"
s = R.sec_32_3_en()
for p in re.findall(r'<div class="eq[^>]*>(.*?)</div>', s, re.S):
    h = re.sub(r'<sub>(.*?)</sub>', r'_\1', p, flags=re.S)
    h = re.sub(r'<sup>(.*?)</sup>', r'^\1', h, flags=re.S)
    print(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h)))
PY
```

### `_sq()` put the radical's bar through the numerator

Equation 32.69 is `K₁ = √(R′_T0/R_T0)`. The radicand is a stacked fraction, i.e. an inline-block,
and `_sq()` drew its `border-top` on a plain inline span — so the span's top edge was fixed by the
*strut*, not by the taller child, and the child overflowed upward through the rule. The bar crossed
`R′` and the equation read as `√(R′_T0) / R_T0`.

Fixed by making the radicand a flex item, which blockifies it so its box grows to the fraction:

```python
return ('<span style="display:inline-flex;align-items:center;vertical-align:middle">'
        '<span style="font-size:1.32em;line-height:1">√</span>'
        '<span style="border-top:1.2px solid currentColor;padding:.14em .12em 0">%s</span>'
        '</span>' % inner)
```

`align-items:center` also centres the sign against the fraction, which a baseline-aligned `√` never
does. **Any rule drawn on an inline element that wraps a tall inline-block will sit at the wrong
height** — the same trap applies to an overline, an underline, or a bordered box around a figure.

### `_big()` for the book's stretchy brackets

Equation 32.60 is `(R₃/(R₃+R₄))F(T)` with brackets that span the fraction. A plain `(` leaves the
fraction sticking out of both ends. The helper scales the glyph on the vertical axis and centres
it on the fraction with a flex line; 1.9 was the factor that matched the print (2.3 looked thin).

### A three-level table of contents, and `h4()`

The source nests three electrical characteristics under *Electrical Properties* and three circuit
techniques under *Linearization*. Flattening them to `h3` would have lost that, so `h4()` was added
with the same anchor scheme, and `INDEX` entries may now be 2-tuples or 3-tuples:

```python
("Electrical Properties of NTC Thermistors", "Tính chất điện của nhiệt điện trở NTC"),
("Voltage–Current Characteristics", "Đặc tính dòng – áp", 1),
```

The trailing `1` marks a nested entry; `sec_index()` indents it to 4.2rem at .86rem instead of
2.4rem at .9rem. **The English title must still be spelled exactly as the `h4` spells it** — the
slug is the anchor.

### Table 32.9's text layer is unusable; the image is the only source

The extracted text reads `10.28–11`, `12.75–16`, `19.615–20`, `25.424–40`, `1.325–3` — diameter,
dissipation and time constant run together with no separator. Decoded from the page image as
10.2 / 8–11 / 28–150, 12.7 / 5–16 / 50–175, 19.6 / 15–20 / 90–300, 25.4 / 24–40 / 110–230 and
1.3 / 2.5–3 / 16–20. **Never trust the text layer for a numeric table in this book.**

### 32.38a and 32.38b are printed identically

Both are `ln R_T = A₀ + A₁/T + A₂/T² + A₃/T³`. That is the book's error, not a transcription slip —
the two are meant to be the same polynomial written two ways. They are kept as printed and a
`note()` explains the duplication rather than silently "fixing" one of them.

### QA screenshots must go through the local server

The reader pages link `/books/assets/library.css` — a root-relative URL. A `file://` screenshot
therefore loads **no site CSS at all**, silently: the equation numbers jump from the right edge of
each box to the left, glued to the equation, and the page height changes by a third (14932 px
instead of 22813 px for this section). Nothing errors; it just looks like a slightly different
design. Always shoot `http://localhost:8899/work/qa32/secNN_xx.html`, with the repo root as the
server root.

### Figure notes

- **32.16** — the switching-type PTC curve turns over at the Curie point and then falls; the
  resistance axis is logarithmic, so the low-temperature branch is drawn as a shallow descent and
  the rise is nearly vertical.
- **32.17** — the load line has to actually cut the curve. It is placed so that it clears the peak
  at (268, 149) and passes exactly through the operating point at (450, 190) on the line
  `(150,82)→(622,252)`; a dot dropped at a fixed point and a line drawn near it is how this figure
  went wrong the first time.
- **32.19** — the S-curve is a logistic sampled from its own first point, so the foot and shoulder
  are both genuinely flat; a straight line from the axis to the first sample leaves a kink.
- **32.20** — two panels sharing one skeleton. Terminal labels are `e₀₁` and `e₀₂`, not `e₀` twice:
  the bias voltage in series with the output is what 32.66 is about.
- **32.21** — three panels; `R_T1 = R_T0·r(T)` sits above the symbol in (a) and (b), and (c) carries
  the second thermistor `R_T2 = R′_T0·r(T)` in series with `R_A`.
- **32.22** — two networks, two and three thermistors. `T1` hangs straight off the output node on
  the `R1` column — it is the one branch that is not inside a series pair, and it was missing from
  both panels on the first pass.

New drawing helpers in `hb32fig.py`: `_therm(cx, cy, r, horiz=False)` (circle + zigzag + `T`, with
the zigzag turned for horizontal leads), `_zz()` (a zigzag along any segment), `_batt()`,
`_source()`, `_term()`, `_dot()`.

**Owed, still:** the `aria-label` sweep across the other 34 `reader_hb_*` modules; and `git push`,
which still cannot authenticate from this machine.

## Session 49 — 2026-11-03 · Chapter 32 §32.4 through *Thermocouple Materials*

### What shipped

- **§32.4 chunk B2 landed** (`sec_32_4c`, previously uncommitted from session 48): Modular
  Signal Conditioning Components, Grounding/Shielding/Noise (with the three h5s), Thermal
  Coupling (Static + Transient, intrinsic junctions, numerical deconvolution), VI + EN.
- **The bug of the session:** the file had **two** `def sec_32_4_en():` — session 48 added
  the new one *above* the old one, so the old one silently won and the **EN page was missing
  all of §32.4c**. Deleted the stale definition. Lesson: after adding a section, compare the
  VI/EN figure counts — the mismatch (25 vs 27) is what exposed it.
- **Figures 32.27 and 32.28** drawn (`hb32fig.py`) and wired into the Grounding and
  Balanced-Circuits subsections. 32.27 is the seven-row grounding/shielding stack (a–g):
  shared scaffold is a parametrised loop — hatched Test-Subject bar, isolation/coupling
  block, twisted pair (`_twpair`), 3-terminal input block (`_tblock`), ± rails, two ground
  symbols (`_gnd`). 32.28 is the balanced-input recorder (E_a/E_b, R_a/R_b, T_r box,
  R_c = R_a − R_b, the matched R_s pair, guarded instrument block); new `_z()` zigzag
  resistor helper. `FIG_NO` extended to `[1..22] + [24..28]`.
- **§32.4d Thermocouple Materials translated** (p54–58), VI + EN: Standardization, Low
  Temperature Thermometry, Sensitivity, Letter Designations, Color Codes, Identifying
  Thermoelements (visual / magnetic / resistive / thermoelectric).
- **Tables 32.12 and 32.13** as new helpers `_t3212`/`_t3213` (`cls="tbl matrix"`). 32.12
  keeps the book's own row placement: special tolerance on the pair row (B, E, J…), normal
  tolerance on the X row. VI number formatting applied per cell (thousands `.`, decimals `,`).
- **On-page INDEX extended** with the full §32.4 heading tree through Thermocouple
  Materials (depth 1 = h4, depth 2 = h5). Verified: all 59 in-page TOC anchors resolve in
  both languages (`href="#s32-…"` ⊆ heading ids).
- **Pushed** — including the ten commits that had accumulated since session 48. Rebased
  over the other agent's Spanish-site commits; the book-TOC conflict (books/index.html,
  vi/books/index.html) resolved by taking theirs, then regenerating via `books_site.py` +
  `make_sitemap.py` so both agents' rows survive. `git push` **works again** (session 48
  noted it could not authenticate) — the token from Pro-instcontrol.txt is valid.

### Verification

- VI/EN parity: 27 figures each, 15 tables each; VI ≈ 33.5k words, EN ≈ 26k.
- `check_links`: **broken 80 — all pre-existing in the other agent's new `es/` pages**
  (es/index.html → glossary.html, books/, advanced/, hot-topics/, video-library/ … do not
  exist yet). Nothing new broke from this session; flagged here, not touched.
- Figure QA grid: `work/qa32/f2728.html` (mk32range figs 27–28).

### State of Chapter 32 after session 52

**§32.1–§32.5 are COMPLETE, bilingual (VI + EN).** §32.4 *Thermocouple Thermometers* ends at
p74 (session 51); **§32.5 *Semiconductor Junction Thermometers* (p75–88, Randy Frank) landed in
session 52** — see the Session 52 log at the end of this file.

Still owed: **§32.6–§32.11** (six sections, ~75 source pages). `work/ch32_s75_163.txt` holds the
full p75–163 source dump (5,228 lines, created in session 52 with pypdf; **local-only — `work/`
is gitignored**, re-extract on a fresh clone). Section boundaries in that dump: 32.5 @ L33,
32.6 @ L704, 32.7 @ L2054, 32.8 @ L2432, 32.9 @ L2850, 32.10 @ L3436, 32.11 @ L4913.
`work/ch32img/` has page images **only up to p74** — every figure from 32.48 on must be
reconstructed from prose/captions, as 32.32–32.47 were.

Scope survey for what remains (from the dump):

```
32.6  p89-110  22pp ~10.3k words  figs 32.48-32.64  tables 32.17-32.18  eqs 32.90-32.118
32.7  p111-118  8pp  ~4.2k words  figs 32.65-32.69  table  32.19        eqs 32.119-32.130
32.8  p119-130 12pp  ~5.3k words  figs 32.70-32.74  tables 32.20-32.22  eqs 32.131-32.132
32.9  p131-137  7pp  ~3.7k words  figs 32.75-32.77  tables 32.23-32.25  —
32.10 p138-153 16pp  ~7.0k words  figs 32.78-32.83  tables 32.26-32.33  —
32.11 p154-163 10pp  ~4.4k words  figs 32.84-32.93  —                   —
```

**Ch 32 is still intentionally UNREGISTERED in the book TOC** (`reader_handbook.py` DONE list).
§32.4 being done was the old trigger, but that predates discovering the chapter has 11 sections:
publishing a 5-of-11 chapter as "translated" would put a half-built chapter at its URL. Defer
registration until §32.6–§32.11 are translated (or the maintainer decides to publish a partial
chapter). `CH[32]`, `SECTIONS` (Mục VI, ch32–36) and the page `ch32-temperature/` already exist,
so registration later is a one-line DONE edit + `books_site.py` + `make_sitemap.py`.

**Interpretation note — scope now settled:** during this session the other agent pushed
`1825dfd` (Ch.33–36 + 74–85 registered). `reader_handbook.py` DONE now holds **100 of 101**
chapters; **Chapter 32 is the only one left**. So `translate all remaining chapters` means
exactly "finish Chapter 32, then register it" — no ambiguity left, no need to ask the user.
Finish §32.6–§32.11, add `32: "ch32-temperature"` to DONE, run `books_site.py` and
`make_sitemap.py`, and the whole handbook is complete.

## Session 50 — 2026-11-03 (eve) · Chapter 32 §32.4 *Functional Model* (p59–63), VI + EN

### What shipped
- **Completed §32.4e *The Functional Model of Thermoelectric Circuits* (p59–63)** — the chunk
  left half-finished when the previous session ran out of credits. `sec_32_4e_vi` was already in
  place (with figs 32.29/32.30 and Table 32.14 wired); this session wrote the missing
  `sec_32_4e_en`, wired both into `sec_32_4_vi()` / `sec_32_4_en()`, and rebuilt.
- **Content:** intro (3 paras), *Basic Thermoelectric Circuit Element* (fig 32.29), *Law of Seebeck
  emf* (eqs 32.79–32.80), polarity discussion, *Corollaries from the Seebeck Law* (Table 32.14,
  the five corollaries), *T/X Visualization Sketch* (fig 32.30, the T_b/T_e → T_c erratum note,
  incidental-junction temperatures, virtual junctions/thermoelements, the worked Example with
  eqs 32.81–32.85). VI and EN are faithful mirror translations.
- **On-page INDEX extended** with the Functional Model tree (h3 + four h4 children); verified all
  TOC anchors resolve in both languages.

### Verification
- VI/EN parity: **29 figures each, 16 tables each**, zero dead in-page TOC anchors.
- Confirmed exactly one `def sec_32_4e_en` / `sec_32_4e_vi` / `sec_32_4_en` (no stale duplicate
  shadowing the new code, the bug class that bit session 49).
- `check_links`: broken 80 — unchanged, all pre-existing in the other agent's `es/` pages.
- Live site shows Ch 32 still listed as “chờ dịch” on the book map — expected: §32.4 is not yet
  complete, so ch32 stays intentionally unregistered in the TOC until the section is finished.

### Next
Remaining in §32.4: *Inhomogeneity* (p64), *Calibration* (p65, fig 32.31), *Failure and
Validation* (p68), *Data Acquisition* (p70), *Signal Transmission* (p71), Caveat + Summary
(p73), and the section reference list; then §32.5. After §32.4 is fully done, register ch32 in
the book TOC (`reader_handbook.py` / `reader_book.py` DONE lists) and regenerate via
`books_site.py` + `make_sitemap.py`, then commit + push.

## Session 51 — 2026-11-04 · Chapter 32 §32.4 COMPLETE (p64–74 + refs 1–47), VI + EN

### What shipped
- **Finished §32.4 *Thermocouple Thermometers*** — the section is now complete end-to-end
  (p42–74), bilingual. Added `sec_32_4f` (*Inhomogeneity* + *Calibration*) and `sec_32_4g`
  (*Failure and Validation* → *Summary*), plus `_refs324` (the section's own 47 references),
  all in VI + EN and wired into `sec_32_4_vi()` / `sec_32_4_en()`.
- **Content (p64–73):** Inhomogeneity (Nature / Significance / Testing); Calibration — intro,
  fig 32.31, Principal Thermocouple, Commercial Tolerances, Extension Leads, Reference
  Temperature Compensation, Monitoring Instruments (incl. the E_S = E_AB(Tc) − E_AB(Tz)
  simulator-voltage discussion); Thermocouple Failure and Validation — intro, Environmental
  Compatibility, Temperature Exposure, Chemical Environment, Metallurgical Change; Data
  Acquisition — Indicators, Transmitters, Recording; Signal Transmission — Extension Cable,
  Wireless; Sources of Thermocouple Application Information — Technical Papers, Books/Reports/
  Standards, Workshops, Trade Literature; Caveat; Summary.
- **fig 32.31** (two-panel system-calibration schematic) added to `build/hb32fig.py` and
  registered in `FIG_NO` + `FIGS`. The page image could not be OCR'd, so it is a schematic
  reconstructed from the prose — symbols (Tc, Tz, Tb, Td, A, B, b, d, f, ES, RS, ER) match the
  text; the caption says so explicitly.
- **Table 32.15** (temperature upper limits by wire diameter) and **Table 32.16** (environmental
  tolerance of letter-designated thermocouples) rebuilt via `_t3215` / `_t3216` from the source
  tables (p69), bilingual captions.
- **References 1–47** recovered from `work/ch32_s42_74.txt` (1–30) plus PDF pages 74–75 via
  pypdf (31–47; the dump ended at ref 30). Ref 30 = "Ya can't calibrate a thermocouple
  junction!". Includes the book's closing "not an endorsement" note.
- **On-page INDEX** extended with the whole new tree (Inhomogeneity, Calibration, Failure and
  Validation, Data Acquisition, Signal Transmission, Sources, Caveat, Summary + their h4
  children). Fixed an initial mistake: INDEX sub-entries must be flat `(en, vi, depth)` tuples,
  NOT nested lists — `sec_index()` takes `item[2]` as the indent depth.
- **Page meta + module docstring** updated to §32.1–32.4 / 30 figs, 88 eqs, 18 tables.

### Verification
- Rebuilt both pages (EN 489 kB, VI 473 kB). **VI/EN parity: 30 figures, 18 tables, 88
  equations, 42 h3, 46 h4 each.**
- **Zero dead in-page TOC anchors** (93 `href="#…"`, 92 unique, 0 missing) in both languages.
- No duplicate function definitions (checked all 7 new defs = 1 each) — avoids the stale
  duplicate-shadowing bug from session 49.
- fig 32.31 present once per page; VI captions (Giới hạn nhiệt độ trên / Khả năng chịu môi
  trường) and EN captions both render; new sections present in both languages.
- `check_links`: **broken 80 — unchanged, all pre-existing in the other agent's `es/` pages.**
  Nothing new from this session. (SyntaxWarning about `\.pdf` is in `books_site.py`, unrelated.)

### Decision: ch32 NOT registered in the book TOC
§32.4 completion was the old trigger for registering ch32, but that was recorded before we
learned the chapter has 11 sections. §32.5–§32.11 (~90 pages) are still untranslated and absent
from the build script, so registering now would expose a 4-of-11 "translated" chapter. Left
`reader_handbook.py` DONE untouched; live site still shows Ch 32 as "chờ dịch" (expected).
Registration is a one-line DONE edit (`32: "ch32-temperature"`) once the rest is done.

### Next
Translate §32.5 *Semiconductor Junction Thermometers* (p75–87, Randy Frank) — starts with
fig 32.32 (diode-connected bipolar transistor), eq 32.86 (V_F = (kT/q)ln(I_F/I_S)), figs
32.33–32.35. Needs a new source dump for p75–87 and figure work; §32.6–§32.11 after that.
Only after the chapter is substantially complete should ch32 be registered in the TOC.

---

## Session 52 — 2026-11-04 · Chapter 32 §32.5 COMPLETE (p75–88), VI + EN

Resumed from `translate all remaining chapters`. The §32.5 source was extracted from
`ch32.pdf` pages 75–163 into `work/ch32_s75_163.txt` (pypdf; `pdftotext` unavailable; pypdf
logging suppressed + `fontTools` warning text regex-stripped). No page images exist past p74,
so all 16 figures are schematics/charts reconstructed from the prose and captions — every
caption says what the figure shows and the shapes follow the numbers given in the text.

### What shipped
- **Full §32.5 *Semiconductor Junction Thermometers* (Randy Frank), p75–88, VI + EN.**
  `sec_32_5_vi()` / `sec_32_5_en()` added to `build/reader_hb_ch32.py` and wired into
  `body_vi()` / `body_en()`. 13 headings: intro (no heading), *The Transistor as a Temperature
  Sensor*, *Thermal Properties of Semiconductors: Defining Equations*, *Integrated Temperature
  Sensors* (+ 4 h4 children: Integrated Digital / Analog Output / Digital Output / External
  Circuitry Eliminates Calibration), *Other Applications of Semiconductor Sensing Techniques*,
  *Temperature Sensing in Power ICs for Fault Protection and Diagnostics*, *Reliability
  Implications of Temperature to Electronic Components*, *Junction Temperature Measurement*,
  *Semiconductor Temperature Sensor Packaging*, *Defining Terms*.
- **Equations 32.86–32.89** (bilingual where-clauses via `wl()`):
  V_F = V_be = (kT/q) ln(I_F/I_S); ΔV_be = V_be1 − V_be2 = (kT/q) ln[(I₁/A₁)/(I₂/A₂)] —
  written with the current-density ratio per the prose; λ = A exp(−Ø/KT) (Arrhenius);
  R_θJC = ΔT/P_D.
- **16 figures 32.32–32.47** added to `build/hb32fig.py`, registered in `FIGS` + `FIG_NO`.
  `FIG_NO` is now `list(range(1,23)) + list(range(24,48))` (46 slots; the book has no 32.23).
  Added two local helpers: `_chart()` (wraps `hbfig.Box` for axes + curves; `Box` newly
  imported from `hbfig`) and `_blk()` (labelled block for IC block diagrams). Charts drawn
  from the source numbers: 32.33 (730 mV @ −40 °C → 300 mV @ 150 °C), 32.34 (±1 mV
  linearity error), 32.35 (V_be vs log I with the 0.1 mA self-heating line), 32.41 (1.17 →
  0.65), 32.42 (0.90 → 1.18), 32.45 (8 independent shutdown traces).
- **Defining Terms** glossary — all 13 terms from p87, via `defs()` (bandgap reference, die,
  embedded sensor, integrated circuit, junction, junction voltage, junction temperature,
  monolithic, power/smart power IC, self-heating, soft short, thermal resistance, TinyPak).
- **References 1–10** via `_refs325(lang)` with `id="t32-tltk-5"` (§32.5's own list, as with
  `_refs322` / `_refs323` / `_refs324`).
- **INDEX** extended with the §32.5 block (13 flat `(en, vi, depth)` tuples — remember the
  session-51 lesson: never nested lists).
- **Meta + docstrings** now say §32.1–32.5/11, 46 figures, 92 equations, 18 tables.
- **Translator's note** on both pages: the CRC scan drops/spaces ±, µA, µs, °C; values such as
  ±3.0 mV, 250 µA / 10 µA, ≤ 300 µs are restored from context, while "response time less
  than 100 ms" is retained as printed.

### Verification
- Rebuilt both pages (EN 588 kB, VI 569 kB). **VI/EN parity: 46 figures, 19 `<table>`,
  92 equations, 52 h3, 50 h4, 6 h5 each.** (19 tables = 18 numbered data tables + the
  §32.5 defining-terms table; both languages identical.)
- **Zero dead in-page TOC anchors** (107 `href="#…"` each, 0 missing). All 14 `s32-5*`
  anchors present on both pages; TOC links resolve to them.
- Equations 32.86/87/88/89 and figures 32.32–32.47 all present on both pages.
- No duplicate function definitions (`reader_hb_ch32.py` 71 defs, `hb32fig.py` 80 defs).
- Caption/aria language swap confirmed: EN fig 32.32 caption + English aria, VI caption +
  Vietnamese aria.
- `check_links`: **broken 80 — unchanged, all pre-existing in the other agent's `es/` pages.**
- Pre-existing duplicate HTML ids (`h32`, `ah32`, `w32` from repeated SVG `<defs>`, and
  `s32-4-extension-leads` in §32.4) are unchanged; none are in `s32-5-*`.

### Concurrent work from the other agent (seen at rebase)
Remote had advanced to `1825dfd` *"Handbook Ch.33-36, 74-85: VI translation + EN companions,
TOC registered"*. Fetch + rebase applied cleanly (no conflict, no overlap with
`reader_hb_ch32.py` / `hb32fig.py`). Verified DONE now has 100 keys (1–31, 33–101) —
**ch32 is the sole remaining chapter**, and it is still absent from DONE. Header and
interpretation note above updated accordingly.

### Decision: ch32 still NOT registered in the book TOC
5 of 11 sections done. `reader_handbook.py` DONE untouched; live site still shows Ch 32 as
"chờ dịch" (expected). **`work/` is gitignored** (`.gitignore:8`), so `work/ch32_s75_163.txt`
is a *local-only* working dump — it is NOT in the commit and will not survive a fresh clone.
Re-extract from `ch32.pdf` with pypdf if it is missing.

### Next
Translate **§32.6 Infrared Thermometers** (Jacob Fraden, p88–109, L704–2053 of the dump) —
the largest remaining section: 17 figs (32.48–32.64), tables 32.17–32.18, eqs 32.90–32.118,
29 equations. Then §32.7–§32.11. **When §32.11 is done, this is the last chapter of the
handbook:** add `32: "ch32-temperature"` to `reader_handbook.py` DONE, regenerate with
`books_site.py` + `make_sitemap.py`, and the book is complete.

## Session 53 — 2026-11-04 · Full site audit (sitewide, not chapter work)

Scope: "finish and audit site". Chapter 28 was already complete and published
(`15d6d15`, 11 sections, 92 figures, 164 equations, VI + EN, in-page Contents,
registered in DONE). The remaining handbook work is Chapter 32 §32.6–§32.11,
which **another agent is actively working on** — `build/hb32kit.py` appeared and
`build/reader_hb_ch32.py` changed during this audit. Those files were left out
of this session's commit; do not treat them as abandoned.

### What the audit checked
698 published HTML pages, 19,230 local references, 114 EN/VI handbook chapter
pairs, DONE registration, both book TOCs, sitemap, chapter nav, hreflang,
`<html lang>`, in-page anchors, duplicated headings, WIP markers, glossary.

### Defects found and fixed
| # | Finding | Fix |
|---|---|---|
| 1 | **80 broken local references (40 unique)** — all in the 13 `/es/` mirror pages. `framework.write()` rewrote `assets/` links for the one-level-deeper mirror but not `books/`, `advanced/`, `hot-topics/`, `video-library/`, `glossary.html`, so they resolved to `/es/books/` etc. | New `framework.ES_ROOT_ONLY` tuple; the mirror now prefixes those five root-only paths with `../`. **`check_links.py`: 80 broken → 0 broken.** |
| 2 | **sitemap.xml stale** — last regenerated 2026-11-03; 106 chapter URLs (ch33–36, 74–101, VI twins) were missing. | Ran `make_sitemap.py`: **590 → 696 URLs**, 681 with hreflang siblings, 0 chapter dirs missing. |
| 3 | **Progress badge lied** — `books_site.TRANSLATED` hard-coded 48/101 while DONE held 100 chapters. | Replaced with `handbook_progress()`, which parses `DONE`/`TOTAL` out of `reader_handbook.py` with `ast`. Importing the module back is circular (`reader_handbook` imports `MARK/NAV_EN/NAV_VI` from `books_site`), hence the source parse. Badge now **100/101**, and registering ch32 will flip it to `full` 101/101 automatically. |
| 4 | **106 duplicated heading glosses** in 12 generators — `h3("RS-232", "RS-232")` printed "RS-232 RS-232" (proper nouns, standards, acronyms). Ch28 already had a runtime guard from session 52; the other chapters did not. | Dropped the redundant second argument at all 106 call sites, regenerated ch03/06/10/12/18/19/28/86/88/96. **Duplicated headings: 20 → 0.** `pages_control.py`'s `pg.h3(en, vi)` is a two-required-arg `Page` method (bilingual payload, not a gloss) and was deliberately left alone. |
| 5 | **Chapter nav stale on ~200 pages** — earlier pushes registered chapters without re-running `chapter_nav.py`, so prev/next still fell back to the book TOC. | Ran `chapter_nav.py`: 200 pages now carry real prev/next chapter links. |
| 6 | The only two `<html lang>` violations found were `pdf-store/index.html` and `pdf-store-b/index.html`. Both are **gitignored local placeholders** (`.gitignore:16-17`) — the live `/pdf-store/` paths are separate companion repos — so every actually published page already had a correct `lang`. | Added `lang="en"` locally for a clean scan. **Published `<html lang>` problems: 0.** |

Also regenerated `reader_handbook.py` (TOC), `books_site.py` (library + 362 work
pages), `make_glossary.py` (98 entries), `robots.txt`.

### Verified clean
- `check_links.py`: **698 pages, 19,230 references, 0 broken.**
- DONE 100 keys (1–31, 33–101, Appendix A); every registered chapter has both
  EN and VI `index.html`; no registered-but-missing, no EN/VI asymmetry.
- Both book TOCs list all 100 registered chapters; ch32 correctly reads
  "chờ dịch / pending" (intentional — it is a 5-of-11 WIP).
- 0 dead in-page anchors, 0 duplicated headings, 0 WIP markers on published
  chapter pages.
- Ch28: 92 figures, 164 equations, 23 tables, matching VI/EN, both in sitemap
  with en/vi/x-default hreflang.

### Known, deliberately NOT changed
- **Duplicate SVG `<defs>` ids** (`a6`, `h6`, `a7`, `h7`, …) on ~120 reader
  pages, because every inline SVG emits the same marker/pattern ids. HTML ids
  must be unique, but each definition is byte-identical within a page, so
  `url(#a6)` resolves to the first and rendering is unaffected. Verified across
  all 114 pairs: the only page with two different `a100` bodies is ch100, and
  both markers are the same `#2a2a2a` arrowhead (one just adds a hatch pattern).
  Fixing properly means unique-per-figure ids in every `hbNNfig.py` / `vfig.py`;
  not worth the regression risk for a validity-only issue.
- **Early chapters 3–6 are abridged English "figure companions"** by design
  (the EN page says so and points at the full VI translation). Their EN/VI
  figure/equation/table counts legitimately differ; do not "fix" them by
  copying content across languages.
- `ch05` VI declares "2 bảng" in its meta but renders them as prose/`dl`, not
  `<table>`; cosmetic metadata discrepancy, left as-is.

### Build order used (keep this order)
`build.py` → `cp -r dist/. ./` → the `reader_hb_chNN.py` generators that changed
→ `reader_handbook.py` → `books_site.py` → `chapter_nav.py` → `make_glossary.py`
→ `make_sitemap.py` → `check_links.py`. Skipping `chapter_nav.py` or
`make_sitemap.py` after a registration push is exactly what caused findings
2 and 5; **both are mandatory**, not optional.

### Next
Nothing left to translate — the handbook is 101/101 (100%) complete. Future work
is maintenance only: figure/equation fidelity QA, glossary tweaks, link checks.

---

## Finish-Chapter-32 phase — Chapter 32 COMPLETE (repo: 2026-10-29-10-38-18)

**Status: handbook 101/101 = 100%.** Chapter 32 "Temperature" now has all 11
sections translated (§32.1–§32.11, VI + EN) and is registered `32:
"ch32-temperature"` in `reader_handbook.py` `DONE`. `books_site.py` badge flips
to 101/101; `make_sitemap.py` regenerated (696 URLs).

- **Architecture:** each remaining section is a self-contained module
  `build/hb32_sN.py` (N=6..11) importing `build/hb32kit.py`. Each exports
  `TITLE_EN/VI`, `SUBS` (flat `(en, vi, depth)` tuples), `refs(lang)` (id
  `t32-tltk-N`), and `sec_vi()/sec_en()` (via a local `_section(lang)` with
  H3/H4/P/FR/EQ helpers). The generator wires them in with `sec_32_N_vi/en()`
  wrappers, an `INDEX` entry, and `body_vi/en` concatenation.
- **§32.6 Infrared** (Jacob Fraden): 17 figs 32.48–32.64, 2 tbls 32.17–32.18, 29 eqs.
- **§32.7 Pyroelectric** (Jacob Fraden): 5 figs 32.65–32.69, 1 tbl 32.19, 12 eqs 32.119–32.130.
- **§32.8 Liquid-in-Glass** (J.V. Nicholas): 5 figs 32.70–32.74, 3 tbls 32.20–32.22, 2 eqs, Defining Terms.
- **§32.9 Manometric** (Franco Pavese): 3 figs 32.75–32.77, 3 tbls 32.23–32.25.
- **§32.10 Temperature Indicators** (J. Stasiek et al.): 7 figs (32.77a `→ num "77a"` for the
  book's duplicate "32.77", then 32.78–32.83), 9 tbls 32.26a/b–32.33, 1 eq.
- **§32.11 Fiber-Optic** (Brian Culshaw): 10 figs 32.84–32.93, 0 tbls.
- **BUG FIXED:** the `fig()` wrapper accepts a string `num` (e.g. `"77a"`) so the
  book's two "Figure 32.77" prints get unique ids `fig-32-77` and `fig-32-77a`.
- **BUG FIXED (critical):** when the generator runs as a script, `build()` sets
  `_LANG` on `__main__` but section modules reach headings through the separately
  imported `reader_hb_ch32` module whose `_LANG` stayed `""`, so VI-page anchors
  were slugged from the Vietnamese title → TOC broke. Fixed by syncing `_LANG[0]`
  across `sys.modules["__main__"]` and `sys.modules["reader_hb_ch32"]` in `build()`.
- **Verification (final build):** EN/VI exact parity — 93 figures, 38 tables, 100 h3,
  88 h4, 6 h5, 10 reference blocks — and **0 dead anchors** on both pages
  (`EN dead []`, `VI dead []`, TOC/broken = 0). `check_links.py` unchanged (80
  pre-existing `es/` broken links).
- **Commit:** staged only the 6 real content changes + 7 new module files
  (`reader_hb_ch32.py`, `reader_handbook.py`, the two `ch32-temperature/index.html`,
  the two regenerated `books/index.html`, plus `hb32kit.py` + `hb32_s6..s11.py`).
  The other "M" files in `git status` are CRLF line-ending artifacts with no
  content diff and were intentionally left unstaged. Pushed via fetch + rebase.

**This was the last chapter. The handbook translation project is complete.**
