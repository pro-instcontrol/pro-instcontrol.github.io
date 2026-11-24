# Autonomous Book Translation & Publication — Status Report

**Repository:** `github.com/pro-instcontrol/pro-instcontrol.github.io` (GitHub Pages, live at
`https://pro-instcontrol.github.io/`)
**Working copy:** `C:\Users\Phamd\WorkBuddy AI\2026-10-29-10-38-18\`
**Campaign directive (verbatim):** *"always add all figures, split chapters and TOC, links to TOC,
same standard as the last 3 books, do all autonomously"* — EN/VI only, **no Spanish**.
**Status (2026-11-23):** 11 reader books complete and live 🟢 (rows below; flagship Book 6
*Valve Selection Handbook* 🟢 21/21, Emerson `cvh6` 🟢 15/15, IIH `iih` 🟢 8/8); the remaining
campaign books are still in progress across Books 7, 9 and 10. **Live chapter HEAD `d8159c1c`**
(PPIC Ch.3 "Study of Control Strategy of the Converter in Solar Photovoltaic Power System":
10 printed pages, 8 vector figures, 13 references, no tables or numbered equations) — the prior
HEAD `128ff523` was Baumann Ch.17 "Will My Valve Be Too Noisy?" (3 printed pages, no figures,
Equation (17-1), 3 references and 5 reading items), and before that `e74d218a` was IPC Ch.2
"Transducers – II"
(58 vector figures, 20 numbered equations, Table 2.1, 12 worked examples and 11 exercise
questions, printed pp. 63–123), and before that `fed6e480` was PPIC Ch.2
"Advanced Measuring (Instrumentation) Methods for Nuclear Installations: A Review", published after
Baumann Ch.16 and the IIH/Emerson work below. The paused Emerson Ch.3 was published,
Ch.4–Ch.15 added (including the 52-page Ch.5 with 39 tables, the 30-page Ch.10 with 53 figures,
the 42-page Ch.13 with 10 data tables / 897 rows, Ch.14 "Pipe Data" with 16 data tables / 521 rows,
and the final 31-page Ch.15 "Conversions and Equivalents" with 19 data tables / 1,108 rows, Index
and Additional Resources), and a glossary-rendering bug fixed in Ch.3/Ch.4. **Emerson `cvh6` is
complete at 15/15**; no further Emerson chapters are queued. IIH Ch.4 "pH Measurement" (22 vector
figures, PDF pp. 143–180) and Ch.5 "Measurement of Flow Rate" (10 vector figures, PDF pp. 181–216)
and Ch.6 "Mechanical Flow Meters" (9 vector figures, PDF pp. 217–256) and Ch.7 "Gas and Liquid
Sampling Techniques" (19 vector figures, 13 data tables, PDF pp. 257–302) and Ch.8 "Control Valves"
(8 vector figures, 111 refs, the book's 108-entry index, PDF pp. 303–347) were then published,
**completing Book 8 at 8/8**. Baumann Ch.5 "Valve Sizing Made Easy" (printed pp. 24–46: 2 vector
figures, 7 data tables, equations 5-1–5-18, 8 references) was then published, together with a
site-wide terminology pass: valve *seat* = đế van / bệ van / mặt tựa của van, *cavitation* = xâm
thực, *flashing* = hóa hơi. Baumann Ch.6 "High-Recovery Valves" (printed pp. 47–50: 2 vector
figures, Table 6-1A/B, the cavitation-noise relation) followed, then Ch.7 "Sizing and Selection—
Let the Computer Do It All!" (no figures, Table 7-1 vendor list, valve-gain footnote). Ch.8
"What About Fail-Safe?" (2 pages, no figures, the 75–80% footnote and a 4-level severity list)
followed, then Ch.9 "Why Most People Choose 'Equal Percentage' as a Flow Characteristic" (9 pages,
4 vector figures, 4 numeric tables, 3 references). Ch.10 "Valve Positioners" (13 pages, 4 vector
figures, Table 10-1, four references) followed, with the prose split across three section modules
and the figures redrawn from the printed SAMSON, Flowserve and Emerson diagrams. Baumann Ch.11
"The Mystery of Line Pressure-Produced Valve Stem Forces" (printed pp. 81–90: 3 vector figures,
Equation 11-1, three source footnotes, 8 references, one additional reading item) followed, with
the ISA data-sheet form, the butterfly-valve dynamic-torque chart and the stall analogy sketch
redrawn from the printed source. Baumann Ch.12 "How to Install a Control Valve" (printed pp. 91–93:
no figures, five installation considerations, twelve common installation failures, three
additional-reading items) followed. Baumann Ch.13 "How Good Is the Valve I Purchased?" (printed
pp. 95–98: 2 vector figures redrawn from the printed Emerson charts, a footnote on installed gain,
2 references, 3 additional-reading items) followed. Baumann Ch.14 "When Do I Need to 'Hard Face'
the Valve Trim and Other Questions Concerning Valve Material" (printed pp. 99–102: no figures,
solid-particle and wet-steam erosion, guide and bearing materials, 1 hardness footnote, 3 refs)
followed. Baumann Ch.15 "Cavitation" (printed pp. 103–108: 5 vector figures, a material-lifetime
table, the cavitation-noise relations, 2 refs and 2 additional-reading items) followed. Baumann
Ch.16 "Concern for the Environment" (printed pp. 109–110: no figures, fugitive emissions, gasket
and bonnet sealing, extended bonnets and packing friction) followed, then Baumann Ch.17
"Will My Valve Be Too Noisy?" (printed pp. 111–113: no figures, the outlet Mach-number relation
(17-1), the 90 dBA OSHA limit, the EC worked examples, ISA-75.17 / IEC 60534-8-3, 3 references
and 5 reading items). PPIC Ch.2 "Advanced Measuring
(Instrumentation) Methods for Nuclear Installations: A Review" (printed pp. 13–38: 7 vector
figures, 76 references and a 26-page review of reactor, fuel-cycle, safeguards and accident
  instrumentation) then followed, then PPIC Ch.3 "Study of Control Strategy of the Converter in
  Solar Photovoltaic Power System" (printed pp. 39–48: 8 vector figures, 13 references, TI
  TMS320F28035 experiments, MATLAB/Simulink and SPWM/LCL-filter waveforms).

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
| `cvp` | **Book 7** — H. D. Baumann, *Control Valve Primer*, 5th ed. (ISA/Wiley 2011) | 204 pp | 32 | **17/32** 🟠 | 29 (ch1–6, ch9–11, ch13, ch15; ch17 has no figures) |
| `bcv` | **Book 7b** — Borden/Friedmann, *Control Valves* (ISA Practical Guides 1998) — Ch.5 excerpt | 12 pp scan | 1 | **1/1** 🟢 | 4 |
| `ppic` | **Book 9** — L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and Control* (Bibliotex 2019) | 308 pp | 11 | **3/11** 🟠 | 20 (ch1–3: 12 + 8) |
| `ipc` | **Book 10** — Prasad/Jayaswal/Priye, *Instrumentation and Process Control* (I.K. International 2019) | 403 pp | 8 | **2/8** 🟠 | 109 (ch1–2: 51 + 58) |

**Library catalog:** 258 works; new works this campaign: 291 (Baumann), 292 (Borden), 293
(Emerson), 294 (IIH), 295 (PPIC), 296 (IPC).

### Published chapters this campaign (EN + VI each)
- Baumann Ch.1 (3 figs) + Ch.2 "Why Not Use a Speed-Controlled Pump?" (no figs, 3 refs)
  + Ch.3 "What Valve Type Shall I Choose?" (3 figs) + Ch.4 "The Self-Acting Regulator: Why Not?"
  (1 fig, printed pp. 21–23)
  + Ch.5 "Valve Sizing Made Easy" (2 figs, 7 tables, equations 5-1–5-18, printed pp. 24–46,
  published in `68cf7511`)
  + Ch.6 "High-Recovery Valves" (2 figs, Table 6-1A/B, printed pp. 47–50, published in `f5ceb53d`)
  + Ch.7 "Sizing and Selection—Let the Computer Do It All!" (0 figs, Table 7-1, printed pp. 51–54,
  published in `d3e54069`)
  + Ch.8 "What About Fail-Safe?" (0 figs, 75–80% footnote, printed pp. 55–56, published in `7fec110f`)
  + Ch.9 "Why Most People Choose 'Equal Percentage' as a Flow Characteristic" (4 figs, 4 tables,
  printed pp. 57–65, published in `3ec4148a`)
  + Ch.10 "Valve Positioners" (4 figs, Table 10-1, 4 refs, printed pp. 67–79, published in
  `a009ad42`)
  + Ch.11 "The Mystery of Line Pressure-Produced Valve Stem Forces, or Selecting the Correct
  Actuator Size" (3 figs, Eq. 11-1, 3 footnotes, 8 refs, printed pp. 81–90, published in
  `630b7742`)
  + Ch.12 "How to Install a Control Valve" (0 figs, 5 considerations, 12 failure cases,
  3 additional-reading items, printed pp. 91–93, published in `e356728c`)
  + Ch.13 "How Good Is the Valve I Purchased?" (2 figs, 1 installed-gain footnote, 2 refs,
  3 additional-reading items, printed pp. 95–98, published in `6721deb7`)
  + Ch.14 "When Do I Need to 'Hard Face' the Valve Trim and Other Questions Concerning Valve
  Material" (0 figs, 1 Rockwell-hardness footnote, 3 refs, printed pp. 99–102, published in
  `251d3805`)
  + Ch.15 "Cavitation" (5 figs, material-lifetime table, cavitation-noise equations, 2 refs,
  2 reading items, printed pp. 103–108, published in `a387b13a`)
  + Ch.16 "Concern for the Environment" (0 figs, fugitive emissions, gasket/bonnet sealing,
  extended bonnets, packing friction and rotary stem packing, printed pp. 109–110, published in
  `21f05412`)
  + Ch.17 "Will My Valve Be Too Noisy?" (0 figs, Equation (17-1), 3 refs, 5 reading items,
  printed pp. 111–113, published in `128ff523`)
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
  + Ch.2 "Advanced Measuring (Instrumentation) Methods for Nuclear Installations: A Review"
  (7 figs, 76 refs, no tables, printed pp. 13–38, published in `fed6e480`)
  + Ch.3 "Study of Control Strategy of the Converter in Solar Photovoltaic Power System"
  (8 vector figs, 13 refs, no tables/equations, printed pp. 39–48)
- IPC Ch.1 "Transducers – I" (51 figs, 7 tables, printed pp. 1–62)
  + Ch.2 "Transducers – II" (58 vector figs, Table 2.1, 20 numbered equations, 12 worked
  examples, 11 exercise questions, PDF pp. 75–135 / printed pp. 63–123, published in `e74d218a`)

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
- Baumann Ch.5 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.5, catalog
  badge shows "Translating · 5 of 32 chapters" (VI: "Đang dịch · 5/32 chương"), live sitemap
  includes all 8 Ch.5 URL entries. Live terminology spot-check: 0 "chỗ ngồi" and 44 "đế van" on
  the Emerson VI Ch.3 page.
- Baumann Ch.6 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.6, catalog
  badge shows "Translating · 6 of 32 chapters" (VI: "Đang dịch · 6/32 chương"), live sitemap
  includes all 8 Ch.6 URL entries.
- Baumann Ch.7 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.7, catalog
  badge shows "Translating · 7 of 32 chapters" (VI: "Đang dịch · 7/32 chương"), live sitemap
  includes all 8 Ch.7 URL entries.
- Baumann Ch.8 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.8, catalog
  badge shows "Translating · 8 of 32 chapters" (VI: "Đang dịch · 8/32 chương"), live sitemap
  includes all 8 Ch.8 URL entries.
- Baumann Ch.9 EN/VI deep URLs → **HTTP 200** after Pages propagation; live TOC lists Ch.9, catalog
  badge shows "Translating · 9 of 32 chapters" (VI: "Đang dịch · 9/32 chương"), live sitemap
  includes all 8 Ch.9 URL entries.
- Baumann Ch.10 EN/VI deep URLs → **HTTP 200** after Pages propagation; live EN/VI pages each
  contain four `fig-N` figures, both live TOCs list Ch.10 ("Valve Positioners" / "Bộ định vị van"),
  catalog badge shows "Translating · 10 of 32 chapters" (VI: "Đang dịch · 10/32 chương"), and the
  live sitemap includes all 8 Ch.10 URL entries.
- Baumann Ch.11 EN/VI deep URLs → **HTTP 200** after Pages propagation (~2 min; the live site
  stayed at 10/32 briefly after push); live EN/VI pages each contain three `fig-N` figures with
  unique ids, the live TOC lists Ch.11 ("The Mystery of Line Pressure-Produced Valve Stem Forces"
  / "Ẩn số lực thân van do áp suất đường ống…"), the catalog badge shows "Translating · 11 of 32
  chapters" (VI: "Đang dịch · 11/32 chương"), and the live sitemap includes all 8 Ch.11 URL entries.
- Baumann Ch.12 EN/VI deep URLs → **HTTP 200** after Pages propagation (~3 min; the live catalog
  stayed at 11/32 briefly after push); both live pages contain all 20 list items, the live TOC lists
  Ch.12 ("How to Install a Control Valve" / "Lắp đặt van điều khiển thế nào"), the catalog badge
  shows "Translating · 12 of 32 chapters" (VI: "Đang dịch · 12/32 chương"), and the live sitemap
  includes all 8 Ch.12 URL entries.
- Baumann Ch.13 EN/VI deep URLs → **HTTP 200** after Pages propagation (~2 min); live EN/VI pages
  each contain two `fig-N` figures with unique ids, the live TOC lists Ch.13 ("How Good Is the
  Valve I Purchased?" / "Van mình mua tốt đến đâu?"), the catalog badge shows "Translating · 13 of
  32 chapters" (VI: "Đang dịch · 13/32 chương"), and the live sitemap includes all 8 Ch.13 URL
  entries.
- Baumann Ch.14 EN/VI deep URLs → **HTTP 200** after Pages propagation (~3 min); live TOC lists
  Ch.14 ("When Do I Need to 'Hard Face' the Valve Trim..." / "Khi nào cần 'phủ cứng' bộ lót van..."),
  the catalog badge shows "Translating · 14 of 32 chapters" (VI: "Đang dịch · 14/32 chương"),
  and the live sitemap includes all 8 Ch.14 URL entries.
- Baumann Ch.15 EN/VI deep URLs → **HTTP 200** immediately after push; live EN/VI pages each contain
  five unique `fig-N` figures with localized captions (`Figure 15.1…` / `Hình 15.1…`), both live
  TOCs list Ch.15 ("Cavitation" / "Xâm thực"), the catalog badge shows "Translating · 15 of 32
  chapters" (VI: "Đang dịch · 15/32 chương"), and the live sitemap includes all 8 Ch.15 URL
  entries (2 `<loc>` + 6 hreflang alternates).
- Baumann Ch.16 EN/VI deep URLs → initially 404, then **HTTP 200** after two Pages propagation
  checks; both live pages retain six equations and the two-item leakage list with 0 CJK / 2
  shell-only bare ampersands, both live TOCs list Ch.16 ("Concern for the Environment" /
  "Quan tâm đến môi trường"), the catalog badge shows "Translating · 16 of 32 chapters"
  (VI: "Đang dịch · 16/32 chương"), and the live sitemap includes all 8 Ch.16 URL entries
  (2 `<loc>` + 6 hreflang alternates).
- PPIC Ch.2 EN/VI deep URLs → initially 404, then **HTTP 200** after two Pages propagation checks;
  both live pages contain seven unique `fig-N` figures with localized captions (`Figure 2.1…` /
  `Hình 2.1…`) and all 76 references, 0 CJK / 2 shell-only bare ampersands, both live TOCs list
  Ch.2 ("Advanced Measuring (Instrumentation) Methods for Nuclear Installations: A Review" /
  "Phương pháp đo tiên tiến cho các cơ sở hạt nhân: Tổng quan"), the catalog badge shows
  "Translating · 2 of 11 chapters" (VI: "Đang dịch · 2/11 chương"), and the live sitemap includes
  all 8 Ch.2 URL entries (2 `<loc>` + 6 hreflang alternates).
- IPC Ch.2 EN/VI deep URLs → initially 404, then **HTTP 200** after Pages propagation; both live
  pages contain 58 XML-valid inline SVGs with 58 unique `fig-N` ids and localized captions
  (`Figure 2.x` / `Hình 2.x`), 21 equations, 0 CJK / 0 bare ampersands in page content, both live
  TOCs list Ch.2 ("Transducers – II" / "Bộ chuyển đổi – II"), the catalog badge shows
  "Translating · 2 of 8 chapters" (VI: "Đang dịch · 2/8 chương"), and the live sitemap includes all
  8 Ch.2 URL entries.
- Baumann Ch.17 EN/VI deep URLs → initially 404, then **HTTP 200** after Pages propagation; both
  live pages contain two equations including numbered (17-1), 8 list items (3 references + 5
  reading items), 0 figures, 0 CJK / 0 bare ampersands in page content, both live TOCs list Ch.17
  ("Will My Valve Be Too Noisy?" / "Van của tôi có quá ồn không?"), the catalog badge shows
  "Translating · 17 of 32 chapters" (VI: "Đang dịch · 17/32 chương"), and the live sitemap
  includes all 8 Ch.17 URL entries.
- PPIC Ch.3 EN/VI deep URLs → initially 404, then **HTTP 200** after Pages propagation; both live
  pages contain 8 XML-valid inline SVGs with 8 unique `fig-N` ids and localized captions
  (`Figure 3.x` / `Hình 3.x`), 13 reference items, 0 CJK / 0 bare ampersands in page content,
  0 off-canvas / 0 overlapping figure labels, both live TOCs list Ch.3 ("Study of Control Strategy
  of the Converter in Solar Photovoltaic Power System" / "Nghiên cứu chiến lược điều khiển bộ
  chuyển đổi trong hệ thống điện mặt trời quang điện"), the catalog badge shows "Translating ·
  3 of 11 chapters" (VI: "Đang dịch · 3/11 chương"), and the live sitemap includes all 8 Ch.3 URL
  entries.

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
  → `905dd942` (IIH ch8, Book 8 complete) → `68cf7511` (Baumann ch5 + site-wide seat/cavitation/
  flashing terminology pass) → `f5ceb53d` (Baumann ch6) → `d3e54069` (Baumann ch7)
  → `7fec110f` (Baumann ch8) → `3ec4148a` (Baumann ch9)
  → `a009ad42` (Baumann ch10) → `630b7742` (Baumann ch11) → `e356728c` (Baumann ch12)
  → `6721deb7` (Baumann ch13) → `251d3805` (Baumann ch14)
  → `a387b13a` (Baumann ch15) → `21f05412` (Baumann ch16)
  → `fed6e480` (PPIC ch2) → `e74d218a` (IPC ch2) → `128ff523` (Baumann ch17)
  → `d8159c1c` (PPIC ch3, **live chapter HEAD**).
- Status-document updates are committed separately from chapter pushes.
- GitHub Pages negative caching can briefly 404 deep paths; retry with cache-busting queries.

## 6. Queue (user's stated order)
1. ~~Integrate Book 10 `ipc` Chapter 1~~ — **done** in `2ca04367` (51 figs, 7 tables, broken 0);
   ~~Ch.2 "Transducers – II"~~ — **done** in `e74d218a` (58 figs, Table 2.1, 20 equations, 12
   examples, 11 exercises, broken 0); remaining Ch.3–8.
2. ~~Book 8 `iih` Ch.3 "Measurement of Level"~~ — **done** in `2d19c7d2` (21 figs)
   ~~Ch.4 "pH Measurement"~~ — **done** in `399e0cbb` (22 figs)
   ~~Ch.5 "Measurement of Flow Rate"~~ — **done** in `db6c38fb` (10 figs)
   ~~Ch.6 "Mechanical Flow Meters"~~ — **done** in `dfb266f0` (9 figs)
   ~~Ch.7 "Gas and Liquid Sampling Techniques"~~ — **done** in `675a28a7` (19 figs, 13 tables)
   ~~Ch.8 "Control Valves"~~ — **done** in `905dd942` (8 figs, 111 refs, book index);
   **Book 8 complete 8/8**.
3. ~~Baumann `cvp` Ch.3 + Ch.4~~ — **done** (`e71e3415`, `d487a9cb`);
   ~~Ch.5 "Valve Sizing Made Easy"~~ — **done** (`68cf7511`, 2 figs, 7 tables, 18 equations);
   ~~Ch.6 "High-Recovery Valves"~~ — **done** (`f5ceb53d`, 2 figs, Table 6-1A/B);
   ~~Ch.7 "Sizing and Selection—Let the Computer Do It All!"~~ — **done** (`d3e54069`, 0 figs,
   Table 7-1);
   ~~Ch.8 "What About Fail-Safe?"~~ — **done** (`7fec110f`, 0 figs, footnote + severity list);
   ~~Ch.9 "Why Most People Choose 'Equal Percentage'..."~~ — **done** (`3ec4148a`, 4 figs,
   4 tables, 3 refs);
   ~~Ch.10 "Valve Positioners"~~ — **done** (`a009ad42`, 4 figs, Table 10-1, 4 refs);
   ~~Ch.11 "The Mystery of Line Pressure-Produced Valve Stem Forces"~~ — **done** (`630b7742`,
   3 figs, Eq. 11-1, 8 refs);
   ~~Ch.12 "How to Install a Control Valve"~~ — **done** (`e356728c`, 0 figs, 5 considerations,
   12 failures, 3 reading items);
   ~~Ch.13 "How Good Is the Valve I Purchased?"~~ — **done** (`6721deb7`, 2 figs, installed-gain
   footnote, 2 refs, 3 reading items);
   ~~Ch.14 "When Do I Need to 'Hard Face' the Valve Trim..."~~ — **done** (`251d3805`, 0 figs,
   hardness footnote, 3 refs);
   ~~Ch.15 "Cavitation"~~ — **done** (`a387b13a`, 5 vector figs, material-lifetime table,
   cavitation-noise equations, 2 refs, 2 reading items);
   ~~Ch.16 "Concern for the Environment"~~ — **done** (`21f05412`, 0 figs, fugitive emissions,
   gasket/bonnet sealing, extended bonnets, packing friction);
   ~~Ch.17 "Will My Valve Be Too Noisy?"~~ — **done** (`128ff523`, 0 figs, Eq. 17-1, 3 refs,
   5 reading items); remaining Ch.18–32.
4. ~~Emerson `cvh6` Ch.3–Ch.15~~ — **done** in `8909e5fc`, `cbc667cc`, `56b8a0f9`, `d2a1da0a`,
   `9e136a59`, `dfac0c08`, `155b8c5c`, `558a8e49`, `e70bd6a7`, `8d523ae8`, `092d513d`, `67f84ff5`,
   `89e84b27` (52 + 27 + 18 + 9 + 14 + 11 + 7 + 53 + 3 + 5 figs, broken 0); Ch.13 added 10 data
   tables / 897 rows, Ch.14 added 16 / 521, and Ch.15 added 19 / 1,108 (all three 0 figs).
   **Book complete 15/15.**
5. **Register candidate Book 11** — *Fundamentals of Industrial Instrumentation* (348 pp,
   2.5 MB) — located and surveyed, not registered.
6. **Register candidate Book 12** — *A Guide to the Automation Body of Knowledge*, 2nd ed.
   (511 pp, 34 MB) — located and surveyed, not registered.
7. ~~Book 9 `ppic` Ch.2 "Advanced Measuring (Instrumentation) Methods for Nuclear Installations"~~
   — **done** in `fed6e480` (7 vector figs, 76 refs, printed pp. 13–38, broken 0);
   ~~Ch.3 "Study of Control Strategy of the Converter in Solar Photovoltaic Power System"~~ —
   **done** in `d8159c1c` (8 vector figs, 13 refs, printed pp. 39–48, broken 0); remaining Ch.4–11.

### Resume notes
- PPIC Ch.3 (10 PDF pages / printed pp. 39–48, 8 vector figures, 13 references) was split across
  four parallel writers: `ppicfig3.py` redrew the PV block diagram, Simulink model, control
  subsystem, SPWM pulse trains, stacked simulation waveforms, TMS320F28035 control card, four
  complementary gate pulses with dead time and the four-channel oscilloscope traces;
  `ppic_ch03a/b/c.py` translated Abstract/Introduction/Structure, Simulation Model, and
  Experiments/Conclusions/References respectively. `ppic_ch03.py` assembled the three streams with
  a bilingual glossary and source-note box. The figure writer's temporary path mismatch was fixed
  by creating zero-padded aliases of the pre-rendered page images. QA: 8 XML-valid SVGs per page,
  8 unique `fig-N` ids, 8/8 localized captions per page, 13 reference items, 0 CJK, 0 content bare
  ampersands, 0 off-canvas / 0 overlapping figure labels, `check_links.py` broken 0, sitemap
  1,098 URLs / 1,083 with siblings, 8 entries for Ch.3. Published in `d8159c1c`; live EN/VI 200
  after Pages propagation, TOC row and 3/11 badge verified.
- Baumann Ch.17 (3 printed pages / PDF pp. 114–116, no figures or tables) was written from scratch
  as one module `cvp_ch17.py` by a single agent: the three noise sources, plug resonance with the
  fₙ relation, the OSHA 90 dBA criterion and 130/110 dBA pipe-damage thresholds, the EC worked
  examples (16,875 and 810), ISA-75.17 versus IEC 60534-8-3, and Equation (17-1) read from the
  printed page (`M_d = 0.20 P₁ Cᵥ F_L / (D² P₂ Cᵢ / 343)`) because the OCR dump garbles it.
  The three references and five reading items are transcribed verbatim, except "Measurement &
  Control" → "Measurement and Control" to satisfy the 0-bare-ampersand gate. A QA review corrected
  one VI phrase ("áp suất âm" → "mức áp suất âm thanh"). QA: 0 CJK, 0 bare ampersands, 0 Spanish,
  2 equations, 0 figures, 3 refs + 5 reading items per page, `check_links.py` broken 0, sitemap
  1,096 URLs / 1,081 with siblings, 8 entries for Ch.17. Published in `128ff523`; live EN/VI 200
  after Pages propagation, TOC row and 17/32 badge verified.
- IPC Ch.2 (61 PDF pages / printed pp. 63–123, 58 vector figures, Table 2.1, 20 numbered
  equations, 12 worked examples, 11 exercise questions) was split across nine parallel writers:
  three figure suppliers (`ipcfig2_a/b/c.py`, 20/20/18 figures) working from `work/ipc2_pages/p075…
  p135.png` and the decoded glyph text, and six prose writers (`ipc_ch02_a…f.py`) using a shared
  `ipc_ch02_lib.py` contract. `ipcfig2.py` merges the three registries and `ipc_ch02.py` assembles
  the six sections with a bilingual glossary, source-note box and about-the-source block. QA:
  58 XML-valid SVGs per page, 58 unique `fig-N` ids, 58/58 localized captions per page, 21
  equations, 1 table, 0 CJK, 0 content bare ampersands, 0 Spanish hits ("con" excluded from the
  guard because Vietnamese "nhóm con" is legitimate), 0 off-canvas / 0 overlapping figure labels,
  `check_links.py` broken 0, sitemap 1,094 URLs / 1,079 with siblings, 8 entries for Ch.2.
  Published in `e74d218a`; live EN/VI 200 after Pages propagation, TOC row and 2/8 badge verified.
- PPIC Ch.2 (26 PDF pages / printed pp. 13–38, 7 vector figures, 76 references) was split across
  four agents: `ppicfig2.py` redrew the MMGAS detector, ATR core cross-section, SWI optical
  network, MPBR fuel loop, Cherenkov detector, probabilistic neural network and ESMADP structure
  from pypdfium2 renders of the printed figures; `ppic_ch02a/b/c.py` translated Abstract through
  Nuclear Power Reactors, Nuclear Fuel Cycle through Safeguards, and Nuclear Accident through the
  76-item reference list respectively. `ppic_ch02.py` integrated the three section streams with a
  bilingual glossary, source-note box and about-the-source block. The first reference-list draft
  included source numbering inside strings that `refs()` already numbers; the 76 leading numbers
  were stripped before build. QA: 8 XML-valid inline SVGs per page (7 content + shell), 7 unique
  `fig-N` ids, 7/7 localized captions, 76 list items, 0 CJK, 2 shell-only bare ampersands, no
  Vietnamese in EN prose, `check_links.py` broken 0, sitemap 1,092 URLs / 1,077 with siblings, 8
  entries for Ch.2. Published in `fed6e480`; live EN/VI 200 after two propagation checks, TOC row
  and 2/11 badge verified.
- Baumann Ch.16 (2 PDF pages / printed pp. 109–110, no figures) was written from scratch as one
  module `cvp_ch16.py`: fugitive emissions, the two leakage paths, flexible ring gaskets and the
  2.5× minimum bolting load, cage-trim thermal-expansion caution, extended bonnets, the
  packing-friction rule of thumb with the worked 1/2-in stem / 100 psi / 500 in² diaphragm
  example (±0.04 psi, 0.6% span), graphite packing, spring-loaded followers, and the rotary-stem
  torque example (80 lb → 40 in-lb → 0.4 psi). All numbers and the printed «longtime leakage»
  and «spring load packing followers» wording retained in EN; six equations are shown explicitly.
  Pre-build scan caught the Spanish-guard false positive «con số», changed to «các giá trị».
  The first build exposed a title mismatch with the registered VI TOC label; the page title was
  changed to "Quan tâm đến môi trường" and the chain rebuilt. QA: 0 CJK, 2 shell-only bare
  ampersands, 0 Spanish, no Vietnamese outside bilingual headings on the EN page, 6 equations,
  `check_links.py` broken 0, sitemap 1,090 URLs / 1,075 with siblings, 8 entries for Ch.16.
  Published in `21f05412`; live EN/VI 200 after two propagation checks, TOC row and 16/32 badge
  verified.
- Baumann Ch.15 (6 PDF pages / printed pp. 103–108, 5 vector figures) was written from scratch as
  the matched pair `cvpfig15.py` + `cvp_ch15.py`: theoretical sound profiles, hollow-stem air
  injection, the sharktooth anticavitation butterfly valve, laboratory sound-test data and the
  damaged plug/orifice photo, all redrawn as labeled SVG from pypdfium2 page renders. The prose
  retains the material-lifetime table, the `X`, `60 log(X/X_Fz)`, `Xy` and acoustic-efficiency
  equations, the 1000-psi worked example, two references and two reading items. Pre-build scans
  caught a missing quote in the VI glossary, the stray CJK fragment «有水» and two caption typos;
  all fixed. Figure-label QA found 0 off-canvas and 0 overlaps; page QA found 0 CJK, 0 content
  bare ampersands, 0 Spanish, 5/5 localized captions per page, `check_links.py` broken 0, sitemap
  1,088 URLs / 1,073 with siblings, 8 entries for Ch.15. Published in `a387b13a`; live EN/VI 200,
  TOC row and 15/32 badge verified immediately after push.
- Baumann Ch.14 (4 PDF pages / printed pp. 99–102, no figures) was written from scratch as one
  module `cvp_ch14.py`: solid-particle and wet-steam erosion, guide and bearing materials, a
  Rockwell-hardness footnote, three references and source notes. All printed material grades and
  numeric values retained (40–46 RC plug / 56–62 RC seat, 58 RC 440C, 38 RC 17-4 pH at 1075°F,
  1350 ft/s sonic steam, 350/450/800/1250°F bearing limits, Cv 0.001–100). Source notes record
  the OCR hyphenations, «chrome-molly», «ALO2» and the twice-printed sand question. Pre-build
  scan caught a missing quote in the VI glossary and a stray CJK fragment in the VI prose; both
  fixed. QA: 0 CJK, 0 content bare ampersands, 0 Spanish, no Vietnamese outside the intentional
  bilingual headings on the EN page, `check_links.py` broken 0, sitemap 1,086 URLs / 1,071 with
  siblings, 8 entries for Ch.14. Published in `251d3805`; live EN/VI 200 after Pages propagation.
- Baumann Ch.13 (4 PDF pages / printed pp. 95–98, 2 vector figures) was written from scratch:
  `cvpfig13.py` redraws the closed-loop variability chart (log τ, curves A/B/C plus the ideal
  line, MANUAL and minimum-variability callouts) and the static step-response chart (I/P input,
  actuator travel and flow across 0.5–10% steps) from pypdfium2 renders of source PDF pp. 99–100;
  `cvp_ch13.py` carries the bilingual prose, installed-gain footnote, 2 references and 3 reading
  items. Two pre-build defects were caught: a `B` variable collision between chart bottom and
  curve B in the figure module, and a bare `&` in the «Pulp & Paper» reference title (escaped as
  `&amp;`). A first build reported "figures 1" because Figure 13-2 had not been inserted into
  either prose body; after adding both `fig(2, …)` calls the count was 2. Figure QA 0 off-canvas
  / 0 overlaps at actual font sizes; page QA 0 CJK, 0 content bare ampersands, 0 Spanish,
  2/2 localized captions, broken 0, sitemap 1,084 URLs / 1,069 with siblings, 8 entries for Ch.13.
  Published in `6721deb7`; live EN/VI 200 after Pages propagation.
- Baumann Ch.12 (3 PDF pages / printed pp. 91–93, no figures) was written from scratch as a single
  module `cvp_ch12.py`: two opening paragraphs, a five-item installation-considerations list (the
  long "Location" item carries two nested paragraphs), a twelve-item installation-failures list,
  a safety/service-life paragraph, three additional-reading items, source notes and an
  about-the-source block. Subheadings are editorial because the source uses only bullets. QA:
  0 CJK, 0 content bare ampersands, 0 Spanish, no Vietnamese outside the intentional bilingual
  headings on the EN page, 3 lists / 20 `<li>` per page, `check_links.py` broken 0, sitemap 1,082
  URLs / 1,067 with siblings, 8 entries for Ch.12; rendered-page visual check clean. Registered
  via the standard 3 edits and published in `e356728c`; live EN/VI 200 after a longer-than-usual
  Pages propagation.
- Baumann Ch.11 (10 PDF pages / printed pp. 81–90, 3 vector figures, Equation 11-1, three source
  footnotes, eight references, one additional reading item) was found at resume as three untracked
  drafts (`cvpfig11.py`, `cvp_ch11a.py`, `cvp_ch11b.py`); a missing integration module
  (`cvp_ch11.py`) was written with the standard bilingual glossary and section concatenation.
  QA found eight duplicate form labels drawn at identical coordinates in Figure 11-1 (generic
  column labels repeated over the explicit ones); these were replaced by one label per column,
  after which all three figures were label-clean at actual per-element font sizes and visually
  checked as rendered PNGs. 0 CJK, 0 content bare ampersands (only the two shell font-URL ones),
  0 Spanish, 3/3 localized captions per page, `check_links.py` broken 0, sitemap 1,080 URLs /
  1,065 with siblings, 8 entries for Ch.11. Published in `630b7742`; live EN/VI 200 after Pages
  propagation.
- Baumann Ch.10 (13 PDF pages, 4 vector figures, one timing table, four references, one additional
  reading item) was split across four parallel agents: a figure supplier working from
  `work/cvp10_p74/p75/p79/p83.png` and three section writers using a fixed `body_vi()` /
  `body_en()` block contract. Integrated in `cvp_ch10.py` with a bilingual glossary, then QA'd:
  all inline SVGs XML-valid, four unique `fig-N` ids per page, 0 CJK, 0 content bare ampersands
  (only the two pre-existing shell font-URL ampersands), no Vietnamese in EN tables, and
  `check_links.py` broken 0. Published in `a009ad42`; sitemap regenerated to 1,078 URLs /
  1,063 with language siblings, including 8 entries for Ch.10.
- Baumann Ch.9 (9 PDF pages, 4 vector figures, 4 numeric tables, 5 equations, 3 references) was
  split across two parallel agents with the standard figure/prose contract: figure supplier
  (`cvpfig9.py`) worked from four pypdfium2 page renders, prose (`cvp_ch09.py`) reconstructed the
  worked installed-characteristic example including all pump/pipe/Cv/signal tables. Published in
  `3ec4148a`; `check_links.py` broken 0, sitemap 1,076 URLs / 1,061 with siblings, 8 entries for
  Ch.9, all SVG labels inside their viewBoxes.
- Baumann Ch.8 (2 PDF pages, no figures/tables, one 75–80% footnote, one 4-item severity list)
  was written by one agent as `cvp_ch08.py`; editorial h2 sections were added because the source
  has no subheadings. Published in `7fec110f`; `check_links.py` broken 0, sitemap 1,074 URLs /
  1,059 with siblings, 8 entries for Ch.8.
- Baumann Ch.7 (4 PDF pages, no figures, Table 7-1 with 7 vendor entries, one valve-gain footnote)
  was written by one agent as a single module (`cvp_ch07.py`), following the short-chapter recipe.
  Published in `d3e54069`; `check_links.py` broken 0, sitemap 1,072 URLs / 1,057 with siblings,
  8 entries for Ch.7. The source note records the Chapter 14 vs Chapter 15 cavitation cross-reference
  discrepancy while retaining the original citation.
- Baumann Ch.6 (4 PDF pages, 2 vector figures, Table 6-1A/B with 4 rows each, one acoustic
  relation) was written by one agent as a matched pair (`cvpfig6.py` + `cvp_ch06.py`); source
  pages were rendered to `work/cvp6_p55.png` / `cvp6_p57.png` so the patent drawing and the
  sound-level chart could be redrawn from the printed originals. Published in `f5ceb53d`;
  `check_links.py` broken 0, sitemap 1,070 URLs / 1,055 with siblings, 8 entries for Ch.6.
- Baumann Ch.5 (23 PDF pages, 2 vector figures, 7 tables / 119 + 11 rows, 18 numbered equations,
  8 references) was split across three parallel section agents (`cvp_ch05a/b/c.py`) against a
  fixed block-parity contract, integrated in `cvp_ch05.py` with a bilingual glossary and a
  source-note box, and published in `68cf7511`. Named HTML entities in the agents' equation
  markup were converted to literal Unicode to meet the 0-bare-ampersand gate. The same push
  applied the user's terminology corrections site-wide: seat → đế van / bệ van / mặt tựa của van
  (including "vật liệu chỗ ngồi" → "vật liệu đế van"), cavitation → xâm thực, flashing → hóa hơi;
  six source strings split across Python line continuations needed a second regex pass. 22 build
  modules and all affected generated pages were rebuilt; `check_links.py` broken 0, sitemap
  1,068 URLs / 1,053 with language siblings, 8 sitemap entries for Ch.5.
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
