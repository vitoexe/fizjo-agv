# F. Program wzmacniania i stabilizacji dla AGV — Gemini Pro (pogłębienie i synteza)

Rola: główny koń roboczy. Wklej poniższy prompt, a pod nim **wynik z Deep Research** (krok 1).

```
You are helping build an evidence-graded knowledge base. Below is (a) our context and (b) the raw output of a broad Deep Research pass. Your job: deepen and synthesise.

CONTEXT: We are building an open-source, Polish-language knowledge base "Fizjo AGV" for aggressive inline skaters (AGV), physiotherapists and coaches. The project has two pillars; the MAIN pillar is PREPARING THE BODY FOR GRINDS (correct body position, strength, stability, proprioception, mobility, prevention); rehabilitation is secondary. Topic: a strength, stability, proprioception and mobility programme to prepare the body for aggressive inline skating grinds and landings: ankle (inversion/eversion), calf (soleus/gastrocnemius), tibialis posterior, peroneals, hip (abductors, external rotators, glutes), core/trunk, wrist/forearm (fall tolerance); dosing, progression, frequency, and evidence for injury prevention.

What we already know (seed):
- Tibialis posterior: progressive resistance exercise improved pain/function in PTTD (S08, RCT); NHS phased programme: ball-squeeze isometric 2 min x3/day, band inversion, double-leg heel raises 3x15 with 3 s hold, then single-leg weighted (S07).
- Calf: heavy slow resistance as effective as eccentrics in Achilles tendinopathy, adherence 92% vs 78% (S09).
- Balance/neuromuscular training reduces ankle sprain risk ~40% (S16) + NATA consensus (S18).
- Practitioner opinion (skateboarding): balance + glute training 20–30 min 2–3x/week; exercises should mirror the sport (S29); AGV core workout video (S25).
- Most seed evidence comes from REHAB populations, not from prevention in healthy skaters.

Gaps (priority — pillar 1):
- Prevention-oriented strength programmes in healthy athletes (ankle, hip, core): dose, frequency, duration.
- Peroneal/eversion strengthening for ankle sprain prevention.
- Hip abductor/external rotator strength and knee valgus at landing.
- Core training and landing control.
- Wrist/forearm conditioning and fall technique for upper-limb injury prevention.
- Plyometric/landing progressions for adolescents and adults (AGV skaters are often teenagers; S01 mean age 15).
- A weekly programme structure supported by sources (not invented).

Sources we ALREADY HAVE (seed research, 2 Nov 2026):
S01 Hilgert 2004 (AGV injury pattern, n=66, PMID 15592983); S02 Major 2007 (AGV grind-rail biomechanics, n=10, PMID 17786694); S03 Dhodapkar 2023 (NEISS skating injuries, PMID 37736602); S04 Schieber 1996 (in-line skating safety gear, PMID 8929359); S05 Rodríguez-Rivadulla 2020 (skateboarding injuries Spain, PMC7082873); S06 Ben Rowles skateboard physio interview (freeskatemag 2019); S07 NHS BNSSG tibialis posterior tendinopathy programme; S08 Kulig 2009 (PTTD RCT, PMID 19022863); S09 Beyer 2015 (HSR vs eccentric, PMID 26018970); S10 Jonsson 2008 (insertional Achilles eccentric, PMID 18184750); S11 Silbernagel 2007 (pain-monitoring model RCT, PMID 17307888); S12 Silbernagel 2015 (Achilles return-to-sport, PMID 26390272); S13 Silbernagel 2020 (conservative Achilles management, PMC7249277); S14 Magnusson 2010 (tendon response to loading, PMID 20308995); S15 Clifford 2020 (isometrics meta-analysis, PMC7406028); S16 Vriend (neuromuscular training ankle sprain meta-analysis, doi 10.1136/jisakos-2016-000062); S17 Doherty 2017 (ankle sprain overview of reviews, PMID 28053200); S18 NATA 2013 ankle sprain position statement (PMC3718356); S19 PAASS 2021 (PMID 34158354); S20 Mazzella 2025 (RTS after surgical ankle fracture, PMC12558590); S21 Sinha 2022 (ankle fracture return to play, PMC9494256); S22 MGH/Boston ORIF ankle fracture rehab protocol (PDF); S23 Sanford ankle return-to-sport test (PDF).
Practitioner resources (OPINION, not evidence): S24–S27 The Blading Physio (AGV soul-grind exercise video, core workout, Skate Talks #47 podcast) and Mad Beef podcast; S28 Ben Rowles ankle sprain guide; S29 Kyle Brown interview (The Daily Push 2018); S30–S31 Jeroen Stam / SkateboardPhysio; S33 Ben Rowles CSP interview; S36 Ślęczkowska 2021 (Polish in-line skating survey, n=801, master's thesis); S38 FFRS concussion protocol.

Tasks:
1. For each claim in the Deep Research output, open the cited source and check the claim (number, population, direction). Mark: CONFIRMED / PARTIAL / NOT SUPPORTED / COULD NOT ACCESS.
2. Find a SECOND, INDEPENDENT primary source for each important claim (different research group; two AI outputs do not count). Our rule: a claim is accepted only with 2 independent primary sources.
3. Answer the open questions in depth:
- Which strength/neuromuscular programmes prevent ankle and knee injuries in healthy athletes, and at what dose?
- Is there evidence for peroneal/eversion or tibialis posterior strengthening in prevention (not only rehab)?
- Do hip and core strength programmes improve landing mechanics (valgus, trunk control)?
- What plyometric/landing progressions are recommended for adolescent athletes?
- Is there evidence that wrist/forearm conditioning or fall-technique training reduces wrist injuries?
4. Write a short practical synthesis for skaters and coaches (max 10 bullets) that keeps EVIDENCE, CONSENSUS, BIOMECH-INFERENCE, ANALOGY and SPECULATION visibly separate. Do not turn inference into prescriptions.

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

Additional columns in Claims: "Independent sources count" (1/2 or 2/2) and "Verification status" (CONFIRMED/PARTIAL/NOT SUPPORTED/COULD NOT ACCESS).

--- DEEP RESEARCH OUTPUT BELOW ---
<wklej tutaj>
```
