# D. Badanie przesiewowe fizjoterapeuty dla zawodnika AGV — Claude (red-teaming)

Rola: krytyczna recenzja, szukanie dziur i przesadzonych twierdzeń. Wklej prompt, a pod nim **zestawienie twierdzeń z Gemini/Cursora** albo plik bazy: `(nowy plik) screening — gdy powstanie z wyników Deep Research/Gemini`.

```
Act as a sceptical sports-medicine reviewer and methodologist. Below is a draft section of an open-source physiotherapy knowledge base for aggressive inline skaters (AGV). Your job is to ATTACK it, not to improve the prose.

CONTEXT: We are building an open-source, Polish-language knowledge base "Fizjo AGV" for aggressive inline skaters (AGV), physiotherapists and coaches. Topic: a physiotherapy screening battery for an aggressive inline skater: ankle dorsiflexion ROM (e.g. weight-bearing lunge test), calf and inversion strength (heel-raise endurance, dynamometry), balance (e.g. Y-balance, single-leg stance), hop/jump tests, landing quality, injury history questionnaire.

What we already know (seed):
- Only two AGV studies exist (S01, S02); no screening protocol for AGV found.
- Single-leg heel-raise test and hop tests appear in clinical protocols (S22, S23).
- Balance training prevents ankle sprains (S16, S18).
- Knee flexion at landing lowers impact (S02) → landing quality may be worth screening (BIOMECH-INFERENCE).

Gaps (everything substantive is missing):
- Reliability/validity and normative values for: weight-bearing lunge test, heel-raise test, Y-balance/SEBT, hop tests, inversion/eversion dynamometry.
- Screening batteries used in other action sports (skateboarding, BMX, snowboard park, parkour) or in landing sports.
- Predictive value of screening for injury (evidence is often weak — report honestly).
- Injury history questionnaires (e.g. CAIT, FAAM) — validation.

Sources we ALREADY HAVE (seed research, 2 Nov 2026):
S01 Hilgert 2004 (AGV injury pattern, n=66, PMID 15592983); S02 Major 2007 (AGV grind-rail biomechanics, n=10, PMID 17786694); S03 Dhodapkar 2023 (NEISS skating injuries, PMID 37736602); S04 Schieber 1996 (in-line skating safety gear, PMID 8929359); S05 Rodríguez-Rivadulla 2020 (skateboarding injuries Spain, PMC7082873); S06 Ben Rowles skateboard physio interview (freeskatemag 2019); S07 NHS BNSSG tibialis posterior tendinopathy programme; S08 Kulig 2009 (PTTD RCT, PMID 19022863); S09 Beyer 2015 (HSR vs eccentric, PMID 26018970); S10 Jonsson 2008 (insertional Achilles eccentric, PMID 18184750); S11 Silbernagel 2007 (pain-monitoring model RCT, PMID 17307888); S12 Silbernagel 2015 (Achilles return-to-sport, PMID 26390272); S13 Silbernagel 2020 (conservative Achilles management, PMC7249277); S14 Magnusson 2010 (tendon response to loading, PMID 20308995); S15 Clifford 2020 (isometrics meta-analysis, PMC7406028); S16 Vriend (neuromuscular training ankle sprain meta-analysis, doi 10.1136/jisakos-2016-000062); S17 Doherty 2017 (ankle sprain overview of reviews, PMID 28053200); S18 NATA 2013 ankle sprain position statement (PMC3718356); S19 PAASS 2021 (PMID 34158354); S20 Mazzella 2025 (RTS after surgical ankle fracture, PMC12558590); S21 Sinha 2022 (ankle fracture return to play, PMC9494256); S22 MGH/Boston ORIF ankle fracture rehab protocol (PDF); S23 Sanford ankle return-to-sport test (PDF).

For every claim check and report:
1. Overstatement: does the claim say more than the cited source (population, effect size, causality, generalisation to AGV)?
2. Wrong label: is something labelled EVIDENCE that is really CONSENSUS, BIOMECH-INFERENCE, ANALOGY or SPECULATION?
3. Independence: are the "2 sources" truly independent (same authors/group, one citing the other)?
4. Missing counter-evidence: name specific studies that contradict or weaken the claim (with DOI/link). If you are not sure a study exists, say so — do not invent.
5. Unsafe advice: anything a skater could misread as permission to load an injured structure too early.
6. Missing red flags / when to see a doctor.

Do NOT add new positive claims. Do NOT rewrite the section. You are a tool, not a source: every counter-claim needs a citation or must be marked SPECULATION.

OUTPUT FORMAT (Markdown):
| # | Claim (quote) | Problem type (overstatement/wrong label/not independent/counter-evidence/unsafe/missing red flag) | Explanation | Suggested fix (relabel / weaken / remove / add caveat) | Counter-source DOI/link (or "none") |
|---|---|---|---|---|---|

### Verdict
- Claims safe to keep as is: #...
- Claims to relabel: #...
- Claims to remove until better sourced: #...

--- DRAFT BELOW ---
<wklej tutaj>
```
