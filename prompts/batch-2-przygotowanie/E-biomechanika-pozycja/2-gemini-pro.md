# E. Biomechanika i prawidłowa pozycja przy grindach — Gemini Pro (pogłębienie i synteza)

Rola: główny koń roboczy. Wklej poniższy prompt, a pod nim **wynik z Deep Research** (krok 1).

```
You are helping build an evidence-graded knowledge base. Below is (a) our context and (b) the raw output of a broad Deep Research pass. Your job: deepen and synthesise.

CONTEXT: We are building an open-source, Polish-language knowledge base "Fizjo AGV" for aggressive inline skaters (AGV), physiotherapists and coaches. The project has two pillars; the MAIN pillar is PREPARING THE BODY FOR GRINDS (correct body position, strength, stability, proprioception, mobility, prevention); rehabilitation is secondary. Topic: biomechanics and anatomically sound body position during grinds in aggressive inline skating (AGV): ankle (inversion/eversion, plantar/dorsiflexion on soul plate and H-block), knee (flexion, valgus), hip (rotation, flexion), trunk; approach angle, mounting the obstacle, balance on the rail/ledge, dismount and landing from height. Include analogies from skateboarding, freestyle skiing, snowboarding (park/rails), BMX, parkour, and drop-landing research.

What we already know (seed):
- Only one AGV biomechanics study: Major 2007 (S02), pilot, 10 male skaters, stall and frontside grind on an instrumented rail. Peak impact force decreased with more knee flexion during stalls (r=-0.65) and with skater experience in stalls and grinds (r=-0.84). Centre of mass never passed over the rail base during grinds -> balance from momentum of an oblique approach. Stalls used ankle, hip or multi-joint balance strategies depending on trick length. Obstacles are often >1 m high.
- No measurement exists for soul, topsoul, makio, royale, unity. Our grind->structure table is BIOMECH-INFERENCE only: soul/makio -> foot rotation control (tibialis posterior, peroneals, Achilles insertion); topside -> ankle at end range; H-block (frontside/backside) -> knees/hips, ankle near neutral; royale/unity -> combined knee+ankle rotation; drops -> knee and Achilles.
- No coach or physio opinion on correct grind position found yet.

Gaps we want filled (priority — pillar 1, preparation):
- Drop-landing evidence: knee/hip flexion, soft landing, knee valgus and ACL risk, landing from >1 m; trunk position.
- Ankle frontal-plane loading (inversion/eversion) in board/skate sports and its injury relevance.
- Analogies: skateboarding (ollie landings, grinds), freestyle ski/snowboard rails and jumps, BMX landings, parkour landings — kinematic data or coaching consensus.
- Coaching/technique descriptions of correct AGV grind position (as OPINION, separate from evidence).
- Any engineering/master's theses measuring grinds.

Sources we ALREADY HAVE (seed research, 2 Nov 2026):
S01 Hilgert 2004 (AGV injury pattern, n=66, PMID 15592983); S02 Major 2007 (AGV grind-rail biomechanics, n=10, PMID 17786694); S03 Dhodapkar 2023 (NEISS skating injuries, PMID 37736602); S04 Schieber 1996 (in-line skating safety gear, PMID 8929359); S05 Rodríguez-Rivadulla 2020 (skateboarding injuries Spain, PMC7082873); S06 Ben Rowles skateboard physio interview (freeskatemag 2019); S07 NHS BNSSG tibialis posterior tendinopathy programme; S08 Kulig 2009 (PTTD RCT, PMID 19022863); S09 Beyer 2015 (HSR vs eccentric, PMID 26018970); S10 Jonsson 2008 (insertional Achilles eccentric, PMID 18184750); S11 Silbernagel 2007 (pain-monitoring model RCT, PMID 17307888); S12 Silbernagel 2015 (Achilles return-to-sport, PMID 26390272); S13 Silbernagel 2020 (conservative Achilles management, PMC7249277); S14 Magnusson 2010 (tendon response to loading, PMID 20308995); S15 Clifford 2020 (isometrics meta-analysis, PMC7406028); S16 Vriend (neuromuscular training ankle sprain meta-analysis, doi 10.1136/jisakos-2016-000062); S17 Doherty 2017 (ankle sprain overview of reviews, PMID 28053200); S18 NATA 2013 ankle sprain position statement (PMC3718356); S19 PAASS 2021 (PMID 34158354); S20 Mazzella 2025 (RTS after surgical ankle fracture, PMC12558590); S21 Sinha 2022 (ankle fracture return to play, PMC9494256); S22 MGH/Boston ORIF ankle fracture rehab protocol (PDF); S23 Sanford ankle return-to-sport test (PDF).
Practitioner resources (OPINION, not evidence): S24–S27 The Blading Physio (AGV soul-grind exercise video, core workout, Skate Talks #47 podcast) and Mad Beef podcast; S28 Ben Rowles ankle sprain guide; S29 Kyle Brown interview (The Daily Push 2018); S30–S31 Jeroen Stam / SkateboardPhysio; S33 Ben Rowles CSP interview; S36 Ślęczkowska 2021 (Polish in-line skating survey, n=801, master's thesis); S38 FFRS concussion protocol.

Tasks:
1. For each claim in the Deep Research output, open the cited source and check the claim (number, population, direction). Mark: CONFIRMED / PARTIAL / NOT SUPPORTED / COULD NOT ACCESS.
2. Find a SECOND, INDEPENDENT primary source for each important claim (different research group; two AI outputs do not count). Our rule: a claim is accepted only with 2 independent primary sources.
3. Answer the open questions in depth:
- What does drop-landing research say about knee/hip flexion and knee valgus for reducing load and injury risk?
- Are there kinematic studies of skateboard grinds/landings or freestyle ski/snowboard rail tricks?
- How are ankle inversion/eversion loads controlled in landing sports and what is the injury relevance?
- What do coaches recommend for body position on rails/ledges in AGV, skateboarding, ski/snowboard park (label as OPINION)?
- Has anyone measured trunk position or centre-of-mass control on a rail beyond Major 2007?
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
