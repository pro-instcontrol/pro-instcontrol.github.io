# HANDOFF — Campaign state 2026-11-24 (Emerson + IIH complete; Books 7/9/10 in progress)

**State now (2026-11-24):** 11 reader books complete 🟢 (see `report.md`; flagship Book 6
*Valve Selection Handbook* 21/21, Emerson `cvh6` 15/15, IIH `iih` 8/8). Remaining campaign:
Baumann `cvp` **19/32**, Borden `bcv` 1/1 🟢, PPIC `ppic` **5/11**, IPC `ipc` **5/8**.
**Live chapter HEAD `64d01a87`** (IPC Ch.5 "Signal Conditioning and Data Acquisition System",
43 PDF pages / printed pp. 229–271, 43 vector figures, 78 unnumbered equations, 11 worked
examples, 18 exercise questions); live sitemap 1,112 URLs, catalog badges IIH 8/8 and Emerson
15/15 both `full`, Baumann badge 19/32, PPIC badge 5/11, IPC badge 5/8, IPC Ch.5, PPIC Ch.5,
Baumann Ch.19, IPC Ch.4, PPIC Ch.4, Baumann Ch.18, IPC Ch.3, Baumann Ch.17 and PPIC Ch.3 EN/VI
deep URLs 200, sitemap 8 entries per new chapter, `check_links.py` broken 0. Full tables in
`report.md`.

**Next unit:** none queued for Emerson, IIH, IPC Ch.3–Ch.5, Baumann Ch.18/Ch.19, PPIC Ch.3–Ch.5.
The standing remaining order is Baumann `cvp` Ch.20 → PPIC `ppic` Ch.6 → IPC `ipc` Ch.6, with
Book 11/12 registration only on confirmation.

**User's queued continuation (verbatim order):** "Book 8 Chapters 2–8, Baumann Chapters 3–32,
and Emerson Chapters 2–15 do one by one" — the Emerson leg is **complete at 15/15**; Book 8 is
complete at 8/8 (Ch.2–8 done), Baumann at 19/32 (Ch.2–19 done), PPIC at 5/11 (Ch.1–5 done) and
IPC at 5/8 (Ch.1–5 done). Also two books located but not registered
(*Fundamentals of Industrial Instrumentation*, 348 pp; *A Guide to the Automation Body of
Knowledge*, 2nd ed., 511 pp).

---

## 0. Done: Book 10 `ipc` Chapter 1 integrated (push `2ca04367`)
Redid the 3 registration edits, built chapter/TOC/site/sitemap, QA'd (51 figs XML-valid,
51 unique fig ids, 0 CJK, 0 ES, broken 0), committed and live-verified both language pages.
Continue with the queue below, one chapter per run. Note: the "bare &" count of 2–3 per page
is the shared Google Fonts URL in the page shell — pre-existing on every published page, not
chapter content.

## 0.5 Emerson Ch.3 pause resolved — published in `8909e5fc`
The earlier pause was lifted: the registered/built/QA’d Emerson Ch.3 working tree was committed
as `8909e5fc` ("Publish Emerson Ch.3: Valve and Actuator Types (EN/VI, 52 vector figures)") and
pushed. Before committing, the paused build was re-validated: 52 XML-valid SVGs, unique
`fig-1..52`, 0 CJK, 0 Spanish, only the 2 shell Google-Fonts bare `&`s, `check_links.py` broken 0,
TOC/catalog/sitemap updated. After push, EN/VI deep URLs initially 404'd (Pages negative
caching) and were verified 200 once deployment propagated; the live TOC lists Ch.3 and the live
sitemap has all 8 Ch.3 URL entries. Visual fixes from the prior session (figs 3.2, 3.6, 3.21,
3.24, 3.29, 3.31–3.34, 3.38, 3.44, 3.50, 3.52) are therefore live.

## 0.6 Terminology corrections now applied site-wide (push `68cf7511`)
- User's standing rules: **seat → đế van / bệ van / mặt tựa của van** (so "vật liệu chỗ ngồi" →
  "vật liệu đế van"), **cavitation → xâm thực**, **flashing → hóa hơi** (not "bay hơi", which stays
  for volatile/vaporization). 22 build modules and every affected generated page were rebuilt.
- Watch for strings split across adjacent Python literals (`"… chỗ "\n "ngồi …"`): a plain
  `.replace("chỗ ngồi", …)` misses them; use a regex over `chỗ\s*"\s*"ngồi`. `grep` the built HTML,
  not just `build/*.py`, to confirm zero remaining occurrences.
- Named HTML entities (`&Delta;`, `&radic;`, `&minus;`, …) fail the 0-bare-ampersand gate; chapter
  agents should emit literal Unicode (Δ, √, −, ×, °, …) in equation markup.

## 0.7 IPC Ch.3 "Transducers – III" published in `d42d37e1`
The working tree already had the chapter shell (`ipc_ch03.py`, `ipc_ch03_a.py`, `ipc_ch03_lib.py`,
`ipcfig3.py`, `ipcfig3_common.py`) and the three registration edits. Twelve parallel writers added
`ipc_ch03_b…i.py` (sections 3.1.3–3.4) and `ipcfig3_a…d.py` (18 figures each) using the shared
contract in `work/ipc3_brief.md`. Source is `work/ipc_decoded.txt` lines 4997–8149 with renders in
`work/ipc3_pages/p136…p215.png`. Integration removed a 14k-character overlap in module g that
duplicated equations (3.34)–(3.38) from module f; the printed p185–p187 relations (Q = K√F and
F = C A ρ(V²/2g)) confirm module f is correct. QA: 72 sequential unique `fig-N` ids, 72 XML-valid
SVGs, 45 equations (3.1)–(3.45), 14 tables, 0 CJK / 0 content bare `&` / 0 Spanish / 0 Vietnamese
diacritics in EN, 0 off-canvas / 0 overlapping labels, `check_links.py` broken 0, sitemap 1,100.
Live EN/VI 200 after Pages propagation, TOC row present, badge 3/8 in both languages. **IPC is
3/8 🟠; IPC `TRANSLATED` remains `("progress", 8, 3)`.**

## 0.8 Baumann Ch.18 "The ABC Method for Gases" published in `2df01e67` / `d7c9c22f`
One writer produced `cvp_ch18.py` and `cvpfig18.py` from `work/cvp_raw.txt` and six renders
`work/cvp18_p117…p122.png`. Every printed equation is garbled in the OCR text layer, so
(18-1)–(18-6), Table 18-1 and the modifier formulas were read from the p118–p120 page images.
`cvpfig18.py` redraws Figure 18-1 (dBA at 1 m against 10X, eight test points, 30 log(10X) slope).
QA: 1 XML-valid SVG with localized caption, 6 equation numbers, 1 table, 6 list items
(2 references + 4 reading items), 0 CJK / 0 content bare `&` / 0 Spanish / 0 label overlaps,
`check_links.py` broken 0, sitemap 1,102. A post-publish cross-check caught a 3→4 error in the
additional-reading count; `d7c9c22f` rebuilt both pages and corrected the source note. Live EN/VI
200 after Pages propagation, TOC row present, badge 18/32 in both languages. **Baumann is 18/32
🟠; `TRANSLATED["control valve primer"]` is `("progress", 32, 18)`.**

## 0.9 PPIC Ch.4 "Nuclear Power Plant Instrumentation Fault Detection Using Fuzzy Logic" published in `3ab39813`
Five section writers produced `ppic_ch04a…e.py` and three figure suppliers produced `ppicfig4_a…c.py`
against `work/ppic4_brief.md`; `ppicfig4.py` and `ppic_ch04.py` merged them. Source is
`work/ppic_raw.txt` lines for PDF pp. 65–94 (`work/ppic4_p065…p094.png`), printed pp. 49–78
(printed = PDF − 16). The source omits equation (3) despite discussing three fuzzy frequency
values; the printed labels (1), (2), (4) were preserved, not invented. Integration fixed a stray
`·` outside a quoted Vietnamese literal in `note_terms()` and shortened two overlapping y-axis
labels (`Temperature (°F)` → `°F`, `Pressure (psia)` → `psia`). QA: 11 sequential unique `fig-N`
ids, 11 XML-valid SVGs, 11/11 localized captions, equations `['1', '2', '4']`, 4 tables, 61 list
items, 0 CJK / 0 content bare `&` / 0 Spanish / 0 Vietnamese diacritics in EN prose, 0 off-canvas /
0 overlapping labels, `check_links.py` broken 0, sitemap 1,104. Live EN/VI 200 after Pages
propagation (EN four checks, VI one), TOC row present, badge 4/11 in both languages. **PPIC is
4/11 🟠; `TRANSLATED["handbook on power plant instrumentation and control"]` is
`("progress", 11, 4)`.**

## 0.10 IPC Ch.4 "Telemetry" published in `fb826fcb`
Seven section writers produced `ipc_ch04_a…g.py` and two figure suppliers produced
`ipcfig4_a/b.py` against `work/ipc4_brief.md`; `ipcfig4.py` and `ipc_ch04.py` merged them. Source
is `work/ipc_decoded.txt` lines 8150–9127 (PDF pp. 216–240, printed pp. 204–228) with renders in
`work/ipc4_pages/p216…p240.png`. Integration fixed a missing opening quote in the VI key-term
string. QA: 30 sequential unique `fig-N` ids, 30 XML-valid SVGs, 30/30 localized captions,
equations (4.1)–(4.4), 15 exercise items, 0 CJK / 0 content bare `&` / 0 Spanish / 0 Vietnamese
diacritics in EN prose outside the intentionally bilingual SVG strips, 0 off-canvas / 0
overlapping figure labels, `check_links.py` broken 0, sitemap 1,106. Live EN/VI 200 after Pages
propagation, TOC row present, badge 4/8 in both languages. **IPC is 4/8 🟠;
`TRANSLATED["instrumentation and process control"]` is `("progress", 8, 4)`.**

## 0.11 Baumann Ch.19 "The Graphical ABC Method for Gases" published in `34f48d9a`
Two agents worked from `work/cvp19_brief.md`: `cvpfig19.py` redraws Graphs A/B/C as computed
log curves (seven Cv/D² curves, one P₁ curve, six Fd curves), and `cvp_ch19.py` carries the
bilingual A/B/C lookup procedure, pipe-schedule modifier table and the 85 → 81 dB example.
Source is `work/cvp_raw.txt` lines 3502–3538 (PDF pp. 123–125, printed pp. 121–123) with renders
`work/cvp19_pages/p123…p125.png`. The source prose says schedule 160 subtracts 6 dB while the
printed table says −8; both are retained with a bilingual source note. QA: 3 unique `fig-N` ids,
3 XML-valid SVGs, 3/3 localized captions, 1 table, 0 CJK / 0 content bare `&` / 0 Spanish /
0 Vietnamese diacritics in EN prose, 0 off-canvas / 0 overlapping labels, `check_links.py`
broken 0, sitemap 1,108. Live EN/VI 200 after Pages propagation, TOC row present, badge 19/32
in both languages. **Baumann is 19/32 🟠; `TRANSLATED["control valve primer"]` is
`("progress", 32, 19)`.**

## 0.12 PPIC Ch.5 "Analysis of the Spatial Separation Effects of Thorium/Uranium Fuels in Block-Type HTRs" published in `1065ce57`
Seven section writers (`ppic_ch05a…g.py`) and three figure suppliers (`ppicfig5_a/b/c.py`) worked
against `work/ppic5_brief.md`; `ppicfig5.py` and `ppic_ch05.py` merged them. Source is
`work/ppic_raw.txt` lines 2478–3213 (PDF pp. 95–121, printed pp. 79–105) with renders
`work/ppic5_pages/p095…p121.png`. Equations (1)–(5) were transcribed from printed p110/p115 and
all five numeric tables checked against page images. Prose writers installed non-overwriting
`hasattr` figure stubs; the merged registry supplied all 17 real vectors at build time. QA: 17
sequential unique `fig-N` ids, 17 XML-valid SVGs, 17/17 localized captions, 5 tables, equations
(1)–(5), 18 refs, 0 CJK / 0 content bare `&` / 0 Spanish / 0 Vietnamese diacritics in EN prose,
0 off-canvas / 0 overlapping labels, `check_links.py` broken 0, sitemap 1,110. Live EN/VI 200
after Pages propagation, TOC row present, badge 5/11 in both languages. **PPIC is 5/11 🟠;
`TRANSLATED["handbook on power plant instrumentation and control"]` is `("progress", 11, 5)`.**

## 0.13 IPC Ch.5 "Signal Conditioning and Data Acquisition System" published in `64d01a87`
Eight section writers (`ipc_ch05a…h.py`) and four figure suppliers (`ipcfig5_a…d.py`) worked
against `work/ipc5_brief.md`; `ipcfig5.py` and `ipc_ch05.py` merged them. Source is
`work/ipc_decoded.txt` lines 9128–10907 (PDF pp. 241–283, printed pp. 229–271) with renders
`work/ipc5_pages/p241…p283.png`. Content: 43 vector figures, 78 unnumbered printed formulas,
eleven worked Examples 5.1–5.11 and the 18-question exercise. Three brief labels conflicted with
the printed diagrams (5.28 weighted-resistor DAC, 5.36 RS-232 pin table, 5.39 Ethernet frame);
both prose and captions follow print. Integration fixed a missing default argument in
`ipcfig5_c.py`'s `node()` helper. QA: 43 sequential unique `fig-N` ids, 43 XML-valid SVGs,
43/43 localized captions, 78 equations, 11 examples, 18 exercise items, 0 CJK / 0 content bare
`&` / 0 Spanish / 0 Vietnamese diacritics in EN prose, 0 off-canvas / 0 overlapping labels,
`check_links.py` broken 0, sitemap 1,112. Live EN/VI 200 after Pages propagation, TOC row
present, badge 5/8 in both languages. **IPC is 5/8 🟠; `TRANSLATED["instrumentation and process
control"]` is `("progress", 8, 5)`.**

## A. Continuation queue (user's order)
0. ~~IIH Ch.8 "Control Valves" — final chapter~~ — **published** in `905dd942` (8 figs, 111 refs,
   4 tables incl. the 108-entry book index, 45 source pages). Two parallel agents (figure supplier
   + prose); independent QA 0 layout problems, 0 CJK/bare ampersands, 8/8 captions, broken 0,
   sitemap 1,066. One stray CJK full stop fixed. `TRANSLATED` flipped to `("full", 8, 8)`;
   live badge "🟢 Fully translated · 8 of 8 chapters" both languages. **Book 8 complete.**
0. ~~IIH Ch.7 "Gas and Liquid Sampling Techniques"~~ — **published** in `675a28a7` (19 figs, 13
   tables, 44 refs, 46 source pages). Largest IIH chapter: two parallel agents (figure supplier
   + prose) with fixed `F.fig_fNN()` contract; independent QA 0 layout problems, 0 CJK, 0 bare
   ampersands, 13 tables per page, broken 0, sitemap 1,064; live EN/VI 200, badge 7/8.
0. ~~IIH Ch.6 "Mechanical Flow Meters"~~ — **published** in `dfb266f0` (9 figs, 46 refs, 40
   source pages). One background agent wrote both modules; independent QA 0 layout problems,
   0 CJK, 0 bare ampersands, broken 0, sitemap 1,062. Fixed one Vietnamese word leaked into a
   shared EN equation ("với" → "with" in EN). Live EN/VI 200, badge 6/8.
0. ~~IIH Ch.5 "Measurement of Flow Rate"~~ — **published** in `db6c38fb` (10 figs, 57 refs, 36
   source pages). One background agent wrote both modules; independent QA found 0 layout
   problems, 0 CJK, 0 bare ampersands, broken 0; sitemap 1,060. Two accented SVG labels
   normalized to the module's romanized convention; live EN/VI 200, badge 5/8.
0. ~~IIH Ch.4 "pH Measurement" draft found in the working tree~~ — **published** in `399e0cbb`
   (22 figs, 38 source pages, printed pp. 130–166). Fixed 10 label off-canvas/overlap defects in
   `iihfig4.py` before rebuild; QA 0 CJK, 0 malformed SVGs, unique fig ids, broken 0, sitemap 1,058;
   live EN/VI 200, TOC row present, badge 4/8.
1. ~~Book 8 `iih` ch2–8~~ — **done, book complete 8/8**; source `work/ihii_raw.txt`;
   printed = PDF − 14.
2. ~~Baumann `cvp` ch3–16~~ — **done** (`e71e3415`, `d487a9cb`, `68cf7511`, `f5ceb53d`, `d3e54069`,
   `7fec110f`, `3ec4148a`, `a009ad42`, `630b7742`, `e356728c`, `6721deb7`, `251d3805`,
   `a387b13a`, `21f05412`); ~~Ch.17 "Will My Valve Be Too Noisy?"~~ — **done** in `128ff523`
   (0 figs, Eq. 17-1, 3 refs, 5 reading items, 3 printed pages);
   ~~Ch.18 "The ABC Method for Gases"~~ — **done** in `2df01e67`, corrected in `d7c9c22f`
   (1 fig, Table 18-1, Eqs. 18-1–18-6, 2 refs, 4 reading items, 6 printed pages);
   ~~Ch.19 "The Graphical ABC Method for Gases"~~ — **done** in `34f48d9a` (3 vector graphs,
   1 table, 1 example, 3 printed pages); remaining ch20–32, source `work/cvp_raw.txt`.
   Short chapters
   (≤6 pages, ≤2 figures) go to one agent for both figure and prose modules; mid-size chapters with
   3–4 charts split into figure supplier + prose with a fixed `fig_fNN` contract, both working from
   pypdfium2 page renders. Long data-heavy chapters can use one figure supplier plus several
   section writers against a fixed `body_vi()` / `body_en()` block contract (as in Ch.10:
   `cvpfig10.py` + `cvp_ch10a/b/c.py`, integrated by `cvp_ch10.py`).
3. ~~Emerson `cvh6` ch3–ch15~~ — **done** in `8909e5fc`, `cbc667cc`, `56b8a0f9`, `d2a1da0a`,
   `9e136a59`, `dfac0c08`, `155b8c5c`, `558a8e49`, `e70bd6a7`, `8d523ae8`, `092d513d`, `67f84ff5`,
   `89e84b27`. **Book complete 15/15**; no further Emerson chapters are queued. Source
   `work/cvh6_raw.txt`; printed = PDF page (dump pages match).
   **Data-chapter recipe (worked for Ch.13–Ch.15, reuse for future data chapters):** ZERO-figure
   data chapters are split across parallel section agents with a shared helper (`cvh13_common.py`:
   `T/H/P/B/N/TB` where `TB` takes language-neutral numeric rows + localized headers/captions;
   re-exported as `cvh14_common.py` and `cvh15_common.py`). Each section module exposes
   `section(lang)`; the main chapter module just iterates them. Ch.13 used 6 agents / 9 sections
   (100% of 5,650 decimals), Ch.14 used 4 agents / 4 sections (100% of 1,665 decimals), Ch.15 used
   6 agents (five conversion sections + Index/back matter; 19 tables / 1,108 rows, 1,737/1,737
   decimals) and required flipping `TRANSLATED` from `progress` to `full` at 15/15. For figure
   chapters: separate figure modules (`cvh6fig5.py`…`cvh6fig12.py`). Large chapters (30+ pages,
   40+ figures) split across two parallel agents — figure supplier and prose — with a fixed
   function-name contract (`fig_f10_01`…`fig_f10_53`, `F10` alias), then integrate, fix bare `&` in
   captions centrally, and QA. Small/mid-size chapters (≤10 figures) go to one agent.
   **Watch for the glossary-shadowing bug:** a module-level `def note(lang)` shadows the shared
   note markup helper and makes both glossary boxes render as the English source-note text.
   Name that function `source_notes(lang)` instead; fixed in Ch.3 and Ch.4.
4. ~~Book 9 `ppic` ch2~~ — **published** in `fed6e480` (7 vector figs, 76 refs, printed pp. 13–38,
   26 source pages, broken 0). ~~Ch.3 "Study of Control Strategy of the Converter in Solar
   Photovoltaic Power System"~~ — **published** in `d8159c1c` (8 vector figs, 13 refs, 10 source
   pages, broken 0); ~~Ch.4 "Nuclear Power Plant Instrumentation Fault Detection Using Fuzzy
   Logic"~~ — **published** in `3ab39813` (11 vector figs, 4 tables, equations (1)/(2)/(4),
   51 refs, 30 source pages, broken 0); ~~Ch.5 "Analysis of the Spatial Separation Effects of
   Thorium/Uranium Fuels in Block-Type HTRs"~~ — **published** in `1065ce57` (17 vector figs,
   5 tables, equations (1)–(5), 18 refs, 27 source pages, broken 0). Remaining ch6–11; source
   `work/ppic_raw.txt`; printed = PDF − 16.
5. ~~Book 10 `ipc` ch2 "Transducers – II"~~ — **published** in `e74d218a` (58 vector figs,
   Table 2.1, 20 numbered equations, 12 worked examples, 11 exercises, 61 source pages, broken 0).
   Nine parallel writers: `ipcfig2_a/b/c.py` (20/20/18 figs) + `ipc_ch02_a…f.py` through a shared
   `ipc_ch02_lib.py` contract, merged by `ipcfig2.py` and `ipc_ch02.py`; pre-rendered pages in
   `work/ipc2_pages/p075…p135.png`. ~~Ch.3 "Transducers – III"~~ — **published** in `d42d37e1`
   (72 vector figs, 45 equations, 14 tables, 80 source pages, broken 0); twelve parallel writers
   against `work/ipc3_brief.md`, merged by `ipcfig3.py` and `ipc_ch03.py`.
   ~~Ch.4 "Telemetry"~~ — **published** in `fb826fcb` (30 vector figs, 4 equations, 4 examples,
   15 exercises, 25 source pages, broken 0); seven section writers and two figure suppliers
   against `work/ipc4_brief.md`, merged by `ipcfig4.py` and `ipc_ch04.py`.
   ~~Ch.5 "Signal Conditioning and Data Acquisition System"~~ — **published** in `64d01a87`
   (43 vector figs, 78 unnumbered equations, 11 examples, 18 exercises, 43 source pages, broken 0);
   eight section writers and four figure suppliers against `work/ipc5_brief.md`, merged by
   `ipcfig5.py` and `ipc_ch05.py`. Remaining ch6–8 — source **`work/ipc_decoded.txt`** (NOT the raw
   dump — glyph codes). The Spanish guard must exclude "con" (Vietnamese "nhóm con").
6. Register Book 11 / Book 12 from the two located PDFs when the user confirms.

Per-chapter flow: survey source span + figures → delegate writing to a background agent with a
brief modeled on the IIH/PPIC/IPC briefs (architecture pointers, constants, QA commands) →
validate output (SVG XML, CJK, bare `&`, unique fig ids) → 3 registration edits → build chain →
QA → commit/push → live verify → update `TRANSLATION-STATUS.md` + memory log.

## B. Git / credentials (already configured — do not redo)
- PAT stored via credential helper `store`; repo-local config clears the GCM chain
  (`credential.helper ""` + `store`). **Do not remove these two local config entries.**
- Push: `GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never git -c credential.helper= -c
  credential.helper=store push --progress origin main` — completes in seconds.
- **Pages propagation:** deep paths can 404 for minutes after a push (negative caching).
  Retry with cache-busting query strings until 200.

## C. Unit recipe (per chapter)
1. Map the source span from the text dump (`===PDFPAGE N===` markers; check the printed-page
   offset per book, see `report.md` §4) and list figure captions.
2. Vector figure module `<key>fig.py`: each figure function returns
   `(svg, caption_vi, caption_en, aria_vi, aria_en)` via `_fig(...)`; captions `Hình …` / `Figure …`;
   register in `FIGS` (mirror `ppicfig.py`/`iihfig.py`). Escape raw `&` as `&amp;`.
3. Chapter module `<key>_chNN.py` mirroring `ppic_ch01.py`: `PAGES_SRC`, `BYLINE`, `TITLE_EN`,
   `TITLE_VI`, optional `note_terms()`, `body_vi()`, `body_en()`; use `import <key>_common as C`
   helpers; `C.fig(num, key)` embeds figures; `refs([...])` for references; per-language tables.
4. Wire-up (3 edits) — see §0 step 1–3, substituting the book key and chapter number.
5. Build & QA: `python build/reader_<key>.py N` → `reader_book.py <key>` → `books_site.py` →
   `make_sitemap.py` → `check_links.py` (**broken 0**). Page QA: every inline SVG XML-valid;
   unique `fig-N` ids; 0 CJK; 0 bare ampersands; no cross-language leakage; aria labels complete.
6. `git add -A && git commit`, push (§B), update `TRANSLATION-STATUS.md` session log + workspace
   memory daily log, verify live (unit pages EN + VI = 200, TOC lists the unit, badge correct).

## D. QA gates (must pass every chapter)
- `check_links.py` → **broken 0**
- Every inline SVG XML-valid (`ET.fromstring`); unique `fig-N` ids per page
- 0 CJK characters, 0 bare ampersands (`&(?!amp;|lt;|gt;|quot;|apos;|#)`)
- Spanish guard → 0 hits; EN tables contain no Vietnamese; captions match page language
- Sitemap regenerated; `TRANSLATED` badge updated (`progress` → `full` when book completes)
- Live verification after push: chapter pages EN + VI = 200, TOC row present, catalog badge correct

## E. Known gotchas
- `done` maps must contain ONLY built chapters; empty-`done` books get 4 transient TOC links
  (fallback `spec["done"].get(1, spec["first_en"][0])`) that clear when Ch.1 lands.
- IPC PDF: body text is glyph codes; always use `work/ipc_decoded.txt`.
- Baumann PDF: the text dump garbles printed equations (all six in Ch.18 were wrong); render the
  source pages with pypdfium2 and read coefficients and subscripts from the images before
  translating. Cross-check list-item counts against the printed references/reading lists too.
- Image-only sources (Borden) need `pypdfium2` rendering to `work/*.png` (QA libs in `work/qalib`).
- `p()` takes exactly one argument — no second positional argument.
- When inserting a new `BOOKS` spec before `def num(n, lang):`, don't duplicate the closing
  brace of the dict (bit us twice).
- `books_site.py` `SyntaxWarning` (invalid escape sequence, line ~980) is pre-existing noise.
- Parallel prose writers may add `hasattr(F, "fig_fNN")` stand-ins so they can be QA'd before the
  figure suppliers land; these are inert once the real registry is imported, but still verify the
  built page's figure ids are sequential and that every figure is a real vector redraw.
- When several writers split one chapter, give each an exact decoded-line range and check the
  equation numbers at the boundaries: IPC Ch.3 initially duplicated (3.34)–(3.38) across modules
  f and g because g's range started one source page too early.
