# B. Obciążanie ścięgien — Gemini Pro (pogłębienie i synteza)

Rola: główny koń roboczy. Wklej poniższy prompt, a pod nim **wynik z Deep Research** (krok 1).

```
You are helping build an evidence-graded knowledge base. Below is (a) our context and (b) the raw output of a broad Deep Research pass. Your job: deepen and synthesise.

CONTEXT: We are building an open-source, Polish-language knowledge base "Fizjo AGV" for aggressive inline skaters (AGV), physiotherapists and coaches. Topic: tendon load management relevant to aggressive inline skaters (Achilles and tibialis posterior): isometrics, heavy slow resistance (HSR), eccentric training, pain-monitoring model (pain thresholds during and 24 h after), 24–48 h monitoring, collagen/gelatin with vitamin C before loading.

What we already know (seed):
- HSR = eccentric for Achilles tendinopathy at 12/52 weeks, better adherence 92% vs 78% (S09).
- Pain-monitoring model: continued running/jumping did not worsen outcomes (S11, n=38); model table up to 5/10 if settled by next morning (S12, S13 — same author, not independent).
- Insertional Achilles: eccentrics to floor level only (S10, pilot n=27).
- Isometrics not superior to isotonic exercise immediately or ≤12 weeks (S15 meta-analysis).
- Collagen synthesis up ~24 h post-exercise, elevated ~3 days (S14, narrative review).
- Tibialis posterior: progressive resistance added to orthoses reduced pain (S08 RCT); NHS phased programme (S07).
- NOTHING yet on collagen/gelatin + vitamin C.

Gaps:
- Collagen/gelatin + vitamin C timing and dose before tendon loading: RCTs, quality of evidence, effect on tendon outcomes (not only biomarkers).
- Pain-monitoring model evidence from authors OTHER than Silbernagel; use in tibialis posterior or post-fracture contexts.
- Load monitoring for jump/landing sports (ACWR controversy), applicable to skaters.
- Isometric vs isotonic for in-season athletes (analgesia, performance).

Sources we ALREADY HAVE (seed research, 2 Nov 2026):
S01 Hilgert 2004 (AGV injury pattern, n=66, PMID 15592983); S02 Major 2007 (AGV grind-rail biomechanics, n=10, PMID 17786694); S03 Dhodapkar 2023 (NEISS skating injuries, PMID 37736602); S04 Schieber 1996 (in-line skating safety gear, PMID 8929359); S05 Rodríguez-Rivadulla 2020 (skateboarding injuries Spain, PMC7082873); S06 Ben Rowles skateboard physio interview (freeskatemag 2019); S07 NHS BNSSG tibialis posterior tendinopathy programme; S08 Kulig 2009 (PTTD RCT, PMID 19022863); S09 Beyer 2015 (HSR vs eccentric, PMID 26018970); S10 Jonsson 2008 (insertional Achilles eccentric, PMID 18184750); S11 Silbernagel 2007 (pain-monitoring model RCT, PMID 17307888); S12 Silbernagel 2015 (Achilles return-to-sport, PMID 26390272); S13 Silbernagel 2020 (conservative Achilles management, PMC7249277); S14 Magnusson 2010 (tendon response to loading, PMID 20308995); S15 Clifford 2020 (isometrics meta-analysis, PMC7406028); S16 Vriend (neuromuscular training ankle sprain meta-analysis, doi 10.1136/jisakos-2016-000062); S17 Doherty 2017 (ankle sprain overview of reviews, PMID 28053200); S18 NATA 2013 ankle sprain position statement (PMC3718356); S19 PAASS 2021 (PMID 34158354); S20 Mazzella 2025 (RTS after surgical ankle fracture, PMC12558590); S21 Sinha 2022 (ankle fracture return to play, PMC9494256); S22 MGH/Boston ORIF ankle fracture rehab protocol (PDF); S23 Sanford ankle return-to-sport test (PDF).

Tasks:
1. For each claim in the Deep Research output, open the cited source and check the claim (number, population, direction). Mark: CONFIRMED / PARTIAL / NOT SUPPORTED / COULD NOT ACCESS.
2. Find a SECOND, INDEPENDENT primary source for each important claim (different research group; two AI outputs do not count). Our rule: a claim is accepted only with 2 independent primary sources.
3. Answer the open questions in depth:
- What is the evidence for collagen/gelatin + vitamin C before exercise on tendon outcomes?
- Is there independent (non-Silbernagel) support for the pain-monitoring model?
- How should tendon load be progressed in landing-heavy sports?
- Do isometrics have any role pre-session for athletes with tendinopathy?
4. Write a short synthesis (max 10 bullets) that keeps EVIDENCE, CONSENSUS, BIOMECH-INFERENCE, ANALOGY and SPECULATION visibly separate.

RULES (mandatory):
1. Every claim must cite a primary source with a working link or DOI (prefer DOI / PubMed / PMC). No source = do not state the claim.
2. Label every claim with exactly one of: EVIDENCE:review | EVIDENCE:RCT | EVIDENCE:observational | CONSENSUS | BIOMECH-INFERENCE | ANALOGY:<sport/population> (add to another label) | SPECULATION.
3. Keep evidence strictly separate from biomechanical inference and from practitioner opinion.
4. Never invent numbers, authors, titles or DOIs. Only report a number if it appears in the cited source; say whether you saw it in the abstract or full text.
5. If no data exists, write "NO DATA FOUND" for that question instead of guessing. A clear "nothing found" is a valid result.
6. AI models (including you) are not sources. Cite what you found, not your own knowledge without a source.
7. Do not repeat the sources we already have (listed below) unless you found something that contradicts or corrects them; we especially want SECOND, INDEPENDENT sources for existing claims.

OUTPUT FORMAT (Markdown, ready to paste into our knowledge base):

### Claims
| # | Claim (1 sentence) | Label | Source (first author, year, title) | DOI / link | Population / sport | n | Where verified (abstract/full text, page/table) | Confidence (high/med/low) |
|---|---|---|---|---|---|---|---|---|

### Biomechanical inference (clearly NOT evidence)
- <inference> — based on: <which cited facts>

### Contradictions between sources
- <claim> — source X says ..., source Y says ...

### NO DATA FOUND
- <question> — what was searched (databases, terms)

### New sources (bibliography)
| Source | Type (study/review/consensus/clinical material/physio blog/opinion) | DOI / link |
|---|---|---|

Additional column in Claims: "Independent sources count" (1/2 or 2/2) and "Verification status" (CONFIRMED/PARTIAL/NOT SUPPORTED/COULD NOT ACCESS).

--- DEEP RESEARCH OUTPUT BELOW ---
<wklej tutaj>
```
