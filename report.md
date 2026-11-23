# Autonomous Book Translation & Publication — Status Report

**Repository:** `github.com/pro-instcontrol/pro-instcontrol.github.io` (GitHub Pages, live at
`https://pro-instcontrol.github.io/`)
**Working copy:** `C:\Users\Phamd\WorkBuddy AI\2026-10-29-10-38-18\`
**Campaign directive (verbatim):** *"always add all figures, split chapters and TOC, links to TOC,
same standard as the last 3 books, do all autonomously"* — EN/VI only, **no Spanish**.
**Status (2026-11-23):** 11 reader books complete and live 🟢 (rows below; flagship Book 6
*Valve Selection Handbook* 🟢 21/21, Emerson `cvh6` 🟢 15/15, IIH `iih` 🟢 8/8); the remaining
campaign books are still in progress across Books 7, 9 and 10. **Live chapter HEAD `905dd942`**
(IIH Ch.8, completing Book 8) — the paused Emerson Ch.3 was published,
Ch.4–Ch.15 added (including the 52-page Ch.5 with 39 tables, the 30-page Ch.10 with 53 figures,
the 42-page Ch.13 with 10 data tables / 897 rows, Ch.14 "Pipe Data" with 16 data tables / 521 rows,
and the final 31-page Ch.15 "Conversions and Equivalents" with 19 data tables / 1,108 rows, Index
and Additional Resources), and a glossary-rendering bug fixed in Ch.3/Ch.4. **Emerson `cvh6` is
complete at 15/15**; no further Emerson chapters are queued. IIH Ch.4 "pH Measurement" (22 vector
figures, PDF pp. 143–180) and Ch.5 "Measurement of Flow Rate" (10 vector figures, PDF pp. 181–216)
and Ch.6 "Mechanical Flow Meters" (9 vector figures, PDF pp. 217–256) and Ch.7 "Gas and Liquid
Sampling Techniques" (19 vector figures, 13 data tables, PDF pp. 257–302) and Ch.8 "Control Valves"
(8 vector figures, 111 refs, the book's 108-entry index, PDF pp. 303–347) were then published,
**completing Book 8 at 8/8**.

---

## 1. What is live right now

### Fully published reader books (all EN + VI, 🟢 complete)
| # | Book | Units | Figures | Status |
|---|------|-------|---------|--------|
| 1 | *The Measurement, Instrumentation and Sensors Handbook* (summary tier) | 113 | redrawn | ✅ live |
| 2 | PC *Process Control* (summary tier) | 14 | 50 redrawn | ✅ live |
| 3 | *Safety Instrumented Systems — Design, Analysis, and Justification* (2nd ed.) | 16 | redrawn | ✅ live |
| 4 | W. Bolton, *Control Systems* (Newnes 2002) | 7 | 19 redrawn | ✅ live |
| 5 | *Inherent Safety in Process Plant Design* (VTT 384) | 16 | redrawn | ✅ live |
| 6 | Crosby *Pressure Relief Valve Engineering Handbook* (TP-V300) | 8 | redrawn | ✅ live |
| 7 | ISA-5.1 *Instrumentation Symbols and Identification* | 7 | redrawn | ✅ live |
| 8 | CSIA *Working with an Integrator Guide* | 9 | 35 redrawn | ✅ live |
| 9 | **Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004) — flagship** | **21** | **235 redrawn** | ✅ **live, 🟢 21/21** |
| 10 | **Emerson, *Control Valve Handbook*, 6th ed. (2020)** | **15** | **228 redrawn** (ch1–12) + 45 data tables (ch13–15) | ✅ **live, 🟢 15/15** |
| 11 | **3G E-learning, *Illustrated Handbook of Industrial Instrumentation & Control* (2018)** | **8** | **108 redrawn** (ch1–8) + 17 data tables (ch4/ch7/ch8) + 108-entry book index | ✅ **live, 🟢 8/8** |

### Remaining campaign books (registered, translated chapter by chapter)
| Key | Book | Source | Chapters | Done | Figures so far |
|-----|------|--------|----------|------|----------------|
| `cvp` | **Book 7** — H. D. Baumann, *Control Valve Primer*, 5th ed. (ISA/Wiley 2011) | 204 pp | 32 | **4/32** 🟠 | 7 (ch1–4) |
| `bcv` | **Book 7b** — Borden/Friedmann, *Control Valves* (ISA Practical Guides 1998) — Ch.5 excerpt | 12 pp scan | 1 | **1/1** 🟢 | 4 |
| `ppic` | **Book 9** — L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and Control* (Bibliotex 2019) | 308 pp | 11 | **1/11** 🟠 | 5 (ch1) |
| `ipc` | **Book 10** — Prasad/Jayaswal/Priye, *Instrumentation and Process Control* (I.K. International 2019) | 403 pp | 8 | **1/8** 🟠 | 51 (ch1) |

**Library catalog:** 258 works; new works this campaign: 291 (Baumann), 292 (Borden), 293
(Emerson), 294 (IIH), 295 (PPIC), 296 (IPC).

### Published chapters this campaign (EN + VI each)
- Baumann Ch.1 (3 figs) + Ch.2 "Why Not Use a Speed-Controlled Pump?" (no figs, 3 refs)
  + Ch.3 "What Valve Type Shall I Choose?" (3 figs) + Ch.4 "The Self-Acting Regulator: Why Not?"
  (1 fig, printed pp. 21–23)
- Borden Ch.5 "Control Valve Actuators" (4 figs) — book complete
- Emerson Ch.1 "Introduction to Control Valves" (19 figs, printed pp. 16–33)
  + Ch.2 "Control Valve Performance" (10 figs, printed pp. 34–53)
  + Ch.3 "Valve and Actuator Types" (52 figs, printed pp. 54–81, published in `8909e5fc`)
  + Ch.4 "Control Valve Accessories" (27 figs, printed pp. 82–97, published in `cbc667cc`)
  + Ch.5 "Control Valve Sizing" (18 figs, 39 tables, 13 symbolic equations, printed pp. 98–149,
  published in `56b8a0f9`)
  + Ch.6 "Special and Severe Service Control Valves" (9 figs, 2 tables, printed pp. 150–161,
  published in `d2a1da0a`)
  + Ch.7 "Steam Conditioning" (14 figs, 4 symbolic equations, printed pp. 162–175, published in
  `9e136a59`)
  + Ch.8 "Installation and Maintenance" (11 figs, printed pp. 176–191, published in `dfac0c08`)
  + Ch.9 "Standards and Approvals" (7 figs, printed pp. 192–209, published in `155b8c5c`)
  + Ch.10 "Isolation Valves" (53 figs, printed pp. 210–239, published in `558a8e49`)
  + Ch.11 "Sustainability" (3 figs, printed pp. 240–249, published in `e70bd6a7`)
  + Ch.12 "Safety Instrumented Systems" (5 figs, printed pp. 250–259, published in `8d523ae8`)
  + Ch.13 "Engineering Data" (0 figs, 10 data tables / 897 rows, printed pp. 260–301, published in
  `092d513d`)
  + Ch.14 "Pipe Data" (0 figs, 16 data tables / 521 rows, printed pp. 302–324, published in
  `67f84ff5`)
  + Ch.15 "Conversions and Equivalents" (0 figs, 19 data tables / 1,108 rows, printed pp. 324–355,
  including the 712-row printed index and Additional Resources, published in `89e84b27`) —
  **book complete 15/15**
- IIH Ch.1 "Measurement of Temperature" (6 figs, printed pp. 1–45, 77 refs)
  + Ch.2 "Measurement of Pressure" (21 figs) + Ch.3 "Measurement of Level" (21 figs,
  PDF pp. 97–142 / printed 83–128, 55 refs)
  + Ch.4 "pH Measurement" (22 figs, PDF pp. 143–180 / printed 130–166, published in `399e0cbb`)
  + Ch.5 "Measurement of Flow Rate" (10 figs, 57 refs, PDF pp. 181–216 / printed 167–202,
  published in `db6c38fb`)
  + Ch.6 "Mechanical Flow Meters" (9 figs, 46 refs, PDF pp. 217–256 / printed 203–242,
  published in `dfb266f0`)
  + Ch.7 "Gas and Liquid Sampling Techniques in Process Industry" (19 figs, 13 tables,
  44 refs, PDF pp. 257–302 / printed 243–288, published in `675a28a7`)
  + Ch.8 "Control Valves" (8 figs, 4 tables incl. the 108-entry / 20-band book index, 111 refs,
  PDF pp. 303–347 / printed 289–333, published in `905dd942`) — **book complete 8/8**
- PPIC Ch.1 "Catalytic Reduction of Dissolved Oxygen" (5 figs, 4 tables)
- IPC Ch.1 "Transducers – I" (51 figs, 7 tables, printed pp. 1–62)

### Live verification (2026-11-22, after resuming)
- Emerson Ch.3 EN/VI deep URLs → **HTTP 200** (after Pages negative caching cleared); live TOC
  listed Ch.3, catalog badge showed "Translating · 3 of 15 chapters", live sitemap included all
  8 Ch.3 URL entries.
- Ch.4 EN/VI deep URLs → **HTTP 200** after Pages negative caching cleared; live TOC lists Ch.4,
  catalog badge shows "Translating · 4 of 15 chapters", live sitemap includes all 8 Ch.4 URL
  entries. The Ch.3 fix is live: EN shows the English glossary and one source-note box, VI shows
  the Vietnamese glossary and no English source-note box.
- Ch.5 and Ch.6 EN/VI deep URLs → **HTTP 200** after Pages negative caching cleared; live TOC lists
  both units, catalog badge shows "Translating · 6 of 15 chapters" (VI: "Đang dịch · 6/15 chương"),
  live sitemap includes all 8 URL entries per unit.
- Ch.7 and Ch.8 EN/VI deep URLs → **HTTP 200** after Pages negative caching cleared; live TOC lists
  both units, catalog badge shows "Translating · 8 of 15 chapters" (VI: "Đang dịch · 8/15 chương"),
  live sitemap includes all 8 URL entries per unit.
- Ch.9 EN/VI deep URLs → **HTTP 200** after Pages propagation (~45 s); live TOC lists Ch.9, catalog
  badge shows "Translating · 9 of 15 chapters" (VI: "Đang dịch · 9/15 chương"), live sitemap includes
  all 8 Ch.9 URL entries.
- Ch.10 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.10, catalog badge
  shows "Translating · 10 of 15 chapters" (VI: "Đang dịch · 10/15 chương"), live sitemap includes all
  8 Ch.10 URL entries.
- Ch.11 EN/VI deep URLs → **HTTP 200** after Pages propagation (~45 s); live TOC lists Ch.11, catalog
  badge shows "Translating · 11 of 15 chapters" (VI: "Đang dịch · 11/15 chương"), live sitemap includes
  all 8 Ch.11 URL entries.
- Ch.12 EN/VI deep URLs → **HTTP 200** after Pages propagation (~45 s); live TOC lists Ch.12, catalog
  badge shows "Translating · 12 of 15 chapters" (VI: "Đang dịch · 12/15 chương"), live sitemap includes
  all 8 Ch.12 URL entries.
- Ch.13 EN/VI deep URLs → **HTTP 200** after Pages propagation (~45 s); live TOC lists Ch.13, catalog
  badge shows "Translating · 13 of 15 chapters" (VI: "Đang dịch · 13/15 chương"), live sitemap includes
  all 8 Ch.13 URL entries.
- Ch.14 EN/VI deep URLs → **HTTP 200** after Pages propagation (~45 s); live TOC lists Ch.14, catalog
  badge shows "Translating · 14 of 15 chapters" (VI: "Đang dịch · 14/15 chương"), live sitemap includes
  all 8 Ch.14 URL entries.
- Ch.15 EN/VI deep URLs → **HTTP 200** after Pages propagation (~45 s); live TOC lists Ch.15, catalog
  badge now shows "🟢 Fully translated · 15 of 15 chapters" (VI: "🟢 Đã dịch đầy đủ · 15/15 chương"),
  live sitemap includes all 8 Ch.15 URL entries (2 `<loc>` + 6 hreflang alternates).
- Local build at `905dd942`: sitemap **1,066 URLs** (1,051 with language siblings);
  `check_links.py` **broken 0**; 1,068 pages / 31,814 local references.
- IIH Ch.4 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.4
  ("pH Measurement", translated), catalog badge shows "Translating · 4 of 8 chapters"
  (VI: "Đang dịch · 4/8 chương"), live sitemap includes all 8 Ch.4 URL entries.
- IIH Ch.5 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.5
  ("Measurement of Flow Rate", translated), catalog badge shows "Translating · 5 of 8 chapters"
  (VI: "Đang dịch · 5/8 chương"), live sitemap includes all 8 Ch.5 URL entries.
- IIH Ch.6 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.6
  ("Mechanical Flow Meters", translated), catalog badge shows "Translating · 6 of 8 chapters"
  (VI: "Đang dịch · 6/8 chương"), live sitemap includes all 8 Ch.6 URL entries.
- IIH Ch.7 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.7
  ("Gas and Liquid Sampling Techniques", translated), catalog badge shows "Translating · 7 of 8
  chapters" (VI: "Đang dịch · 7/8 chương"), live sitemap includes all 8 Ch.7 URL entries.
- IIH Ch.8 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.8
  ("Control Valves", translated), catalog badge now shows "🟢 Fully translated · 8 of 8 chapters"
  (VI: "🟢 Đã dịch đầy đủ · 8/8 chương"), live sitemap includes all 8 Ch.8 URL entries.

---

## 2. Build standard (applied uniformly to all books)
- **Every source figure redrawn as a vector** (no raster scans). Figures return the standard
  5-tuple `(svg, caption_vi, caption_en, aria_vi, aria_en)`; bilingual captions
  (`Hình …` / `Figure …`), numbered callouts where the source has them.
- **Each chapter = its own standalone page**; book TOC links every built unit (EN + VI).
- **Full bilingual EN/VI prose**; per-language tables (no cross-language leakage).
- QA gates: SVGs XML-valid, unique `fig-N` ids, **0 CJK, 0 bare ampersands**, `check_links.py`
  broken 0, sitemap regenerated, live 200 checks after push.
- Source OCR typos are preserved in EN with VI following intended meaning; end-of-chapter
  `note()` documents source quirks.

## 3. Shared architecture (don't reinvent)
- `build/bolton_common.py` — page shell, markup helpers, central `BOOK`/`SLUGS` tables.
- Per-book shells: `<key>_common.py` (re-import bolton_common, one `BOOK`/`SLUGS` entry +
  `T(vi,en,lang)`) and runners `reader_<key>.py` (`MODULES = {chapter: module}`).
- `build/reader_book.py` — `BOOKS` registry + TOC generator (`chapters` + `done` slug map;
  `done` must contain ONLY built chapters; empty-`done` fallback
  `spec["done"].get(1, spec["first_en"][0])` creates the 4 transient links).
- `build/vfig.py` — vector primitives; per-book figure modules `<key>fig.py`.
- `build/books_site.py` (`DESC`/`TRANSLATED`/`BOOK_SLUG`/`DROP_WORK_IDS={186}`),
  `make_sitemap.py`, `check_links.py`.
- **Chapter registration = 3 edits:** `<key>_common.SLUGS[key][n]`, `reader_book.py` `done[n]`,
  `books_site.py` `TRANSLATED[...]` progress; then rebuild chapter → TOC → site → sitemap →
  check_links → commit → push → live verify.

## 4. Source material map (all under `D:/Ebooks/Process Control and Automation/`)
| Key | PDF | Text dump | Notes |
|-----|-----|-----------|-------|
| cvp | Control-valve-primer-a-users-guide-fifth-edition.pdf | `work/cvp_raw.txt` | 204 pp, 32 ch |
| bcv | Control Valves Selection Handbook - Borden Friedmann.pdf | image-only | rendered `work/borden_p01..12.png` |
| cvh6 | Emerson-control-valve-handbook-en-3661206.pdf | `work/cvh6_raw.txt` | 355 pp, 15 ch |
| iih | Illustrated-handbook-of-industrial-instrumentation-and-process-control.pdf | `work/ihii_raw.txt` | 348 pp, 8 ch |
| ppic | Handbook-on-power-plant-instrumentation-and-control.pdf | `work/ppic_raw.txt` | 308 pp, 11 ch; printed = PDF−16 |
| ipc | Instrumentation-and-process-control.pdf | `work/ipc_raw.txt` → **decoded `work/ipc_decoded.txt`** | 403 pp, 8 ch; body text stored as glyph codes `/Gnn` → `chr(nn)`; printed = PDF−12 |

## 5. Git / credentials (configured — do not redo)
- PAT via credential-helper store; repo-local config clears the GCM chain — **do not remove**.
- Push pattern: `GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never git -c credential.helper= -c
  credential.helper=store push --progress origin main`.
- Session pushes: `0ed011b7` (registration) → `bad2d686` (Baumann ch2 + Emerson ch1) →
  `b370e6f3` (Book 8 registration) → `98bb7d26` (IIH ch1) → `066862d2` (Book 9 registration) →
  `7b60e440` (PPIC ch1) → `671ae45b` (Book 10 registration) → `a15f1de8` (pause/report) →
  `2ca04367` (IPC ch1) → `de891681` (IIH ch2) → `e71e3415` (Baumann ch3) → `fd86e439` (Emerson ch2)
  → `2d19c7d2` (IIH ch3) → `d487a9cb` (Baumann ch4) → `8909e5fc` (Emerson ch3)
  → `cbc667cc` (Emerson ch4 + Ch.3 note fix) → `56b8a0f9` (Emerson ch5)
  → `d2a1da0a` (Emerson ch6)   → `9e136a59` (Emerson ch7) → `dfac0c08` (Emerson ch8) → `155b8c5c` (Emerson ch9) → `558a8e49`
  (Emerson ch10) → `e70bd6a7` (Emerson ch11) → `8d523ae8` (Emerson ch12) → `092d513d`
  (Emerson ch13)   → `67f84ff5` (Emerson ch14) → `89e84b27` (Emerson ch15) → `399e0cbb` (IIH ch4)
  → `db6c38fb` (IIH ch5) → `dfb266f0` (IIH ch6) → `675a28a7` (IIH ch7)
  → `905dd942` (IIH ch8, **live chapter HEAD**, Book 8 complete).
- Status-document updates are committed separately from chapter pushes.
- GitHub Pages negative caching can briefly 404 deep paths; retry with cache-busting queries.

## 6. Queue (user's stated order)
1. ~~Integrate Book 10 `ipc` Chapter 1~~ — **done** in `2ca04367` (51 figs, 7 tables, broken 0).
2. ~~Book 8 `iih` Ch.3 "Measurement of Level"~~ — **done** in `2d19c7d2` (21 figs)
   ~~Ch.4 "pH Measurement"~~ — **done** in `399e0cbb` (22 figs)
   ~~Ch.5 "Measurement of Flow Rate"~~ — **done** in `db6c38fb` (10 figs)
   ~~Ch.6 "Mechanical Flow Meters"~~ — **done** in `dfb266f0` (9 figs)
   ~~Ch.7 "Gas and Liquid Sampling Techniques"~~ — **done** in `675a28a7` (19 figs, 13 tables)
   ~~Ch.8 "Control Valves"~~ — **done** in `905dd942` (8 figs, 111 refs, book index);
   **Book 8 complete 8/8**.
3. ~~Baumann `cvp` Ch.3 + Ch.4~~ — **done** (`e71e3415`, `d487a9cb`); remaining Ch.5–32.
4. ~~Emerson `cvh6` Ch.3–Ch.15~~ — **done** in `8909e5fc`, `cbc667cc`, `56b8a0f9`, `d2a1da0a`,
   `9e136a59`, `dfac0c08`, `155b8c5c`, `558a8e49`, `e70bd6a7`, `8d523ae8`, `092d513d`, `67f84ff5`,
   `89e84b27` (52 + 27 + 18 + 9 + 14 + 11 + 7 + 53 + 3 + 5 figs, broken 0); Ch.13 added 10 data
   tables / 897 rows, Ch.14 added 16 / 521, and Ch.15 added 19 / 1,108 (all three 0 figs).
   **Book complete 15/15.**
5. **Register candidate Book 11** — *Fundamentals of Industrial Instrumentation* (348 pp,
   2.5 MB) — located and surveyed, not registered.
6. **Register candidate Book 12** — *A Guide to the Automation Body of Knowledge*, 2nd ed.
   (511 pp, 34 MB) — located and surveyed, not registered.
7. Book 9 `ppic` Chapters 2–11 after the user's named queues.

### Resume notes
- IIH Ch.8 (final chapter, 42 prose pages + 3 index pages, 8 vector figures, 111 refs, 108-entry
  book index in 20 letter bands) was split across two parallel agents with the same figure/prose
  contract as Ch.7; independent QA 0 layout problems, 0 CJK/bare ampersands, 8/8 captions, 4
  tables, broken 0, sitemap 1,066. Fixed one stray CJK full stop in a VI label. Published in
  `905dd942` with `TRANSLATED["illustrated handbook of industrial instrumentation"]` flipped from
  `("progress", 8, 7)` to `("full", 8, 8)`; **Book 8 is complete**.
- IIH Ch.7 (largest IIH chapter: 46 source pages, 19 vector figures, 13 data tables, 44 refs) was
  split across two parallel agents — figure supplier (`iihfig7.py`, 19 functions) and prose
  (`iih_ch07.py`, 1,828 lines) — with a fixed `F.fig_fNN()` contract. Independent QA: 0 layout
  problems, 0 CJK/bare ampersands, 13 tables on each page, 19/19 localized captions, broken 0;
  published in `675a28a7`.
- IIH Ch.6 modules (`iihfig6.py` 9 figures, `iih_ch06.py` 1,541 lines, 46 refs, 40 source pages)
  were written by one background agent, verified independently (0 layout problems, 0 CJK/bare
  ampersands), registered, built, QA'd and published in `dfb266f0`. Fixed one Vietnamese word
  ("với") that had leaked into a shared EN equation by making that fragment language-aware.
- IIH Ch.5 modules (`iihfig5.py` 10 figures, `iih_ch05.py` 1,377 lines, 57 refs, 36 source pages)
  were written by one background agent against the Ch.4 contract, verified independently
  (0 layout problems with actual per-element font sizes, 0 CJK/bare ampersands), registered,
  built, QA'd and published in `db6c38fb`; two inconsistent accented SVG labels were normalized.
- The in-progress IIH Ch.4 draft found in the working tree (22 figure functions, EN/VI prose,
  3 registration edits) was validated, corrected (10 figure-label position/overlap fixes in
  `iihfig4.py`), rebuilt, QA'd and published in `399e0cbb`; it is live.
- The previously paused Emerson Ch.3 working tree was committed in full (`8909e5fc`) and is live.
- The in-progress Ch.9 draft found at resume was validated, built, committed (`155b8c5c`) and is live.
- Ch.10 was written by two parallel agents (figure supplier + prose), integrated and QA'd in one run,
  committed in `558a8e49` and is live.
- Ch.11 and Ch.12 were each written by a single agent (both modules), QA'd and committed in
  `e70bd6a7` and `8d523ae8` respectively, and are live.
- Ch.13 (42 pp. data chapter, 0 figs) was written by six parallel section agents against a shared
  `cvh13_common` table helper, integrated, QA'd (100% of 5,650 source decimal values present),
  committed in `092d513d` and is live.
- Ch.14 (22 pp. data chapter, 0 figs) was written by four parallel section agents using the same
  recipe (via `cvh14_common`), integrated, QA'd (100% of 1,665 source decimal values present),
  committed in `67f84ff5` and is live.
- Ch.15 (31 pp. final data chapter, 0 figs) was written by six parallel section agents (five
  conversion sections plus Index/back matter) via `cvh15_common`, integrated, QA'd (100% of 1,737
  source decimal values present; 712 index rows / 23 letter bands), fixed for a Vietnamese-string
  syntax error and an EN index-header leak, committed in `89e84b27` and is live.
- Emerson `cvh6` is now **complete at 15/15**: 228 vector figures through Ch.12 plus 45 data tables /
  2,526 rows in Ch.13–15. No chapter/site changes are pending for this book.
- Before editing status docs again, check `git status --short` to see what is already committed.

See `HANDOFF.md` for the step-by-step continuation recipe and QA gates.
