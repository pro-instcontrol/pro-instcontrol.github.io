# HANDOFF — Campaign state: FIVE BOOKS COMPLETE

**Status (2026-11-15):** ALL FIVE BOOKS ARE 100% LIVE in EN + VI:

| # | Book | Chapters | Badge |
|---|------|----------|-------|
| 1 | Bolton, *Process Control* | 7/7 | 🟢 Fully translated |
| 2 | *Safety Instrumented Systems* | 16/16 | 🟢 Fully translated |
| 3 | ISA *Instrumentation Symbols and Identification* | 7/7 | 🟢 Fully translated |
| 4 | Crosby *Pressure Relief Valve Engineering Handbook* | 8/8 | 🟢 Fully translated |
| 5 | Heikkilä, *Inherent Safety in Process Plant Design* (VTT 384) | 16/16 | 🟢 Fully translated |

Final session commits: `111db504` (Ch7), `7f1824b9` (Ch8), `ced6477d` (Ch9),
`497280a2` (Ch10), `bedd67ca` (Ch11), `5d5ec52a` (Ch12), `8465cdca` (Ch13),
`feefca8b` (Ch14–16 complete). Infra: sitemap 940 URLs, `check_links.py`
942 pages / 28,668 refs / **broken 0**.

**Next campaign step:** select the next Tier-A instrumentation/control title
(EN/VI only, NO Spanish), extract to `work/<slug>_raw.txt`, create
`<slug>_common.py` + reader + figure module following the same pattern
(see `build/isd_common.py`, `build/reader_isd.py`, `build/isdfig.py`,
`build/isd_ch01.py` as the reference implementation), then build chapters
one at a time with the QA gates below.

---

## A. Git / credentials (already configured — do not redo)
- PAT stored: `git config --global credential.helper store` + `git credential approve`
  (token `ghp_…` for `pro-instcontrol`). Pushes need **no prompt**.
- **Push-hang root cause (fixed 2026-11-15):** the system gitconfig chains `credential.helper
  = manager` (Git Credential Manager) *before* `store`; GCM tries an interactive prompt in
  this non-interactive shell and stalls every push for minutes or forever. Fixed in the repo
  local config: `git config --local credential.helper ""` (clears the chain) + `git config
  --local --add credential.helper store`. After this, `git push origin main` completes in
  seconds. **Do not remove these two local config entries.**
- **Run `git push` with `dangerouslyDisableSandbox: true`** (sandbox SIGTERMs network egress
  otherwise). If a push still returns `SIGTERM` with empty output, just retry — the commit
  is safe locally.
- Verify live after push:
  `curl -s -o /dev/null -w "%{http_code}" https://pro-instcontrol.github.io/books/read/inherent-safety-in-process-plant-design/chNN-…/`

## B. Chapter recipe (identical for every chapter)
1. Source span → read `work/isd_raw.txt` from the `=== PAGE N ===` marker of the first
   page to the marker of the next chapter's first page.
2. Add vector figure(s) to `build/isdfig.py` (5-tuple return, register in `isdfig.FIGS`);
   source figures = redraws, extra schematics must be labelled editorial
   ("Sơ đồ A/B/…" / "Figure A/B/… — not present in the original").
3. Create `build/isd_chNN.py` mirroring `isd_ch06.py`: `PAGES_SRC`, `BYLINE`,
   `TITLE_EN`, `TITLE_VI`, `note_terms(lang)`, `body_vi()`, `body_en()`;
   import `from isd_common import fig, h2, h3, note, p, table` (+ `keyterms` if needed)
   and `import isdfig as F`. VI prose is the primary text; EN mirrors it.
   - Gotcha: `isdfig._box()` has **no `dash=` kwarg** — use `_rect(..., dash="3 2")`
     plus separate `_txt` lines for dashed boxes.
   - Gotcha: stage labels may have only one line — don't `line1, line2 = s.split("\n")`.
4. Wire-up (three edits):
   - `build/isd_common.py` → `SLUGS["isd"][N] = "chNN-…"`.
   - `build/reader_book.py` → extend the `"done"` map of the `"isd"` entry.
   - `build/books_site.py` → bump `"inherent safety in process plant design":
     ("progress", 16, N)` (line ~459; also check the `"p384"` alias entry if present).
5. Build & QA: `python build/reader_isd.py N` → `reader_book.py isd` → `books_site.py`
   → `make_sitemap.py` → `check_links.py` (**broken 0**). Page QA: `grep -o
   'class="figure"' … | wc -l` matches expected figures; Spanish guard
   `grep -oP '(?i)\b(figura|capitulo|tabla|…)\b|lang="es"|/es/books/|href="/es/'`
   = **0 hits**; nav prev/next correct; VI + EN pages both written.
6. `git add -A && git commit -q -m "Book 5 Chapter N … (N/16)"`, push (see §A),
   update `TRANSLATION-STATUS.md` session log + workspace memory daily log.

## C. Remaining chapters — spans and notes
| Ch | Title (EN) | Pages (pp.) | Raw lines | Figures/notes |
|----|------------|-------------|-----------|----------------|
| 8 | Inherent Safety Index | 56–59 | 1680–1780 | index calculation method; formulae as `eq()` blocks; subindex score tables (0–5 / 0–4 scales) |
| 9 | The Weighting between Subindices | 60–61 | ~1781–1830 | weighting discussion, short |
| 10 | Subindices of Chemical Inherent Safety Index | 62–67 | ~1830–2000 | reaction heat / side reactions / interaction / flammability / explosiveness / toxicity / corrosiveness subindex tables |
| 11 | Subindices for Process Inherent Safety Index | 68–94 | ~2000–2700 | equipment safety, process structure, etc. |
| 12 | Case Study — Acetic Acid Process | 95–102 | ~2700–3170 | process comparison; **Figure 9** (heat-recovery recommendation for an exothermic reactor feed) at raw lines ~3172–3193 — this is the figure referenced from Ch6 |
| 13 | Case-Based Reasoning for Safety Evaluation | 103–… | … | see TOC, raw lines ~139–195 |
| 14 | Application of Inherent Safety Index for Computerized Process Synthesis | 103–120 | ~3300–3747 | … |
| 15/16 | Conclusions / References | 121–129 | 3748–3995 | follow the `reader_book.py` chapter list (16: "References") |

Exact page→line mapping: `grep -n "=== PAGE" work/isd_raw.txt`.
The `MODULES` dict in `build/reader_isd.py` already registers chapters 6–16.

## D. QA gates (must pass every chapter)
- `check_links.py` → **broken 0**
- Spanish guard → **0 hits** on every new page (EN + VI)
- 0 CJK characters, 0 Python artifacts in HTML
- Figures: source figures redrawn as vectors; editorial ones labelled; each page
  XML-valid SVG (`ElementTree.fromstring` if adding new figure code)
- Sitemap regenerated; TRANSLATED badge "N of 16"
