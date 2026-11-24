# HANDOFF — Campaign state 2026-11-23 (Emerson + IIH complete; Books 7/9/10 in progress)

**State now (2026-11-23):** 11 reader books complete 🟢 (see `report.md`; flagship Book 6
*Valve Selection Handbook* 21/21, Emerson `cvh6` 15/15, IIH `iih` 8/8). Remaining campaign:
Baumann `cvp` **10/32**, Borden `bcv` 1/1 🟢, PPIC `ppic` 1/11, IPC `ipc` 1/8.
**Live chapter HEAD `a009ad42`** (Baumann Ch.10); live sitemap 1,078 URLs, catalog badges IIH 8/8
and Emerson 15/15 both `full`, Baumann badge 10/32, Ch.10 EN/VI deep URLs 200, sitemap 8 Ch.10
entries, `check_links.py` broken 0. Full tables in `report.md`.

**Next unit:** none queued for Emerson or IIH. Awaiting the user's next instruction; the standing
remaining order is Baumann `cvp` Ch.11 → PPIC `ppic` Ch.2 → IPC `ipc` Ch.2, with Book 11/12
registration only on confirmation.

**User's queued continuation (verbatim order):** "Book 8 Chapters 2–8, Baumann Chapters 3–32,
and Emerson Chapters 2–15 do one by one" — the Emerson leg is **complete at 15/15**; Book 8 is
complete at 8/8 (Ch.2–8 done) and Baumann at 10/32 (Ch.2–10 done). Also two books located but not registered
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
2. ~~Baumann `cvp` ch3–10~~ — **done** (`e71e3415`, `d487a9cb`, `68cf7511`, `f5ceb53d`, `d3e54069`,
   `7fec110f`, `3ec4148a`, `a009ad42`); remaining ch11–32, source `work/cvp_raw.txt`. Short chapters
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
4. Book 9 `ppic` ch2–11 — source `work/ppic_raw.txt`; printed = PDF − 16.
5. Book 10 `ipc` ch2–8 — source **`work/ipc_decoded.txt`** (NOT the raw dump — glyph codes).
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
- Image-only sources (Borden) need `pypdfium2` rendering to `work/*.png` (QA libs in `work/qalib`).
- `p()` takes exactly one argument — no second positional argument.
- When inserting a new `BOOKS` spec before `def num(n, lang):`, don't duplicate the closing
  brace of the dict (bit us twice).
- `books_site.py` `SyntaxWarning` (invalid escape sequence, line ~980) is pre-existing noise.
