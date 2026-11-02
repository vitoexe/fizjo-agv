# A. Wzorce urazów według typu grindu — Gemini Pro (pogłębienie i synteza)

Rola: główny koń roboczy. Wklej poniższy prompt, a pod nim **wynik z Deep Research** (krok 1).

```
You are helping build an evidence-graded knowledge base. Below is (a) our context and (b) the raw output of a broad Deep Research pass. Your job: deepen and synthesise.

CONTEXT: We are building an open-source, Polish-language knowledge base "Fizjo AGV" for aggressive inline skaters (AGV), physiotherapists and coaches. Topic: injury patterns in aggressive inline skating (AGV, trick/street/park inline skating) by grind type (soul, topsoul, makio, mizou, frontside, backside, royale, unity, stalls, gaps/drops off grinds) and by structure (ankle, Achilles tendon, tibialis posterior, knee, wrist/hand).

What we already know (seed):
- No study breaks down injuries by grind type. The only AGV biomechanics study is a 10-skater pilot (S02): impact force fell with experience (r=-0.84) and with more knee flexion during stalls (r=-0.65); centre of mass never passed over the rail during grinds.
- AGV field study (S01, 66 skaters, 2004): 1 medically treated injury per 586 h; more knee/tibia/ankle injuries than fitness skating; wrist guards 41%, knee pads 94%.
- Inline skating in general (S03, S04): 53% upper-limb injuries; no wrist guards OR 10.4 for wrist injury.
- Skateboarding analogy (S05): ankle 39.3% of injuries, ankle sprain most recurrent (70.1%).
- Our grind→structure mapping (soul/makio → tibialis posterior/peroneals/Achilles insertion; topside → end-range ankle; H-block → knees/hips; royale/unity → combined knee+ankle rotation) is BIOMECH-INFERENCE only.

Gaps we want filled:
- Any AGV / trick-skating injury epidemiology after 2007 (competitions e.g. WRS, surveys, case series, theses).
- Any kinematic/kinetic measurements of specific grinds (soul, topsoul, makio, royale, unity) — including engineering/master's theses.
- Acute vs overuse injuries in AGV; equipment effects (hard boot, soul plate, frame).
- Second independent sources for each S01–S05 claim; analogies from skateboarding, BMX, snowboard/ski park.

Sources we ALREADY HAVE (seed research, 2 Nov 2026):
S01 Hilgert 2004 (AGV injury pattern, n=66, PMID 15592983); S02 Major 2007 (AGV grind-rail biomechanics, n=10, PMID 17786694); S03 Dhodapkar 2023 (NEISS skating injuries, PMID 37736602); S04 Schieber 1996 (in-line skating safety gear, PMID 8929359); S05 Rodríguez-Rivadulla 2020 (skateboarding injuries Spain, PMC7082873); S06 Ben Rowles skateboard physio interview (freeskatemag 2019); S07 NHS BNSSG tibialis posterior tendinopathy programme; S08 Kulig 2009 (PTTD RCT, PMID 19022863); S09 Beyer 2015 (HSR vs eccentric, PMID 26018970); S10 Jonsson 2008 (insertional Achilles eccentric, PMID 18184750); S11 Silbernagel 2007 (pain-monitoring model RCT, PMID 17307888); S12 Silbernagel 2015 (Achilles return-to-sport, PMID 26390272); S13 Silbernagel 2020 (conservative Achilles management, PMC7249277); S14 Magnusson 2010 (tendon response to loading, PMID 20308995); S15 Clifford 2020 (isometrics meta-analysis, PMC7406028); S16 Vriend (neuromuscular training ankle sprain meta-analysis, doi 10.1136/jisakos-2016-000062); S17 Doherty 2017 (ankle sprain overview of reviews, PMID 28053200); S18 NATA 2013 ankle sprain position statement (PMC3718356); S19 PAASS 2021 (PMID 34158354); S20 Mazzella 2025 (RTS after surgical ankle fracture, PMC12558590); S21 Sinha 2022 (ankle fracture return to play, PMC9494256); S22 MGH/Boston ORIF ankle fracture rehab protocol (PDF); S23 Sanford ankle return-to-sport test (PDF).

Tasks:
1. For each claim in the Deep Research output, open the cited source and check the claim (number, population, direction). Mark: CONFIRMED / PARTIAL / NOT SUPPORTED / COULD NOT ACCESS.
2. Find a SECOND, INDEPENDENT primary source for each important claim (different research group; two AI outputs do not count). Our rule: a claim is accepted only with 2 independent primary sources.
3. Answer the open questions in depth:
- Is there any injury data per grind/trick type in AGV or skateboarding?
- What are the most common acute and overuse injuries in AGV after 2007?
- Has anyone measured ankle/knee loads or kinematics during soul-plate grinds?
- Is 'sliding onto knees/shins' really the typical AGV fall?
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
