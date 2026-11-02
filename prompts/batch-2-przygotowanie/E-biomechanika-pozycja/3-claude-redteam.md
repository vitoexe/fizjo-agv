# E. Biomechanika i prawidłowa pozycja przy grindach — Claude (red-teaming)

Rola: krytyczna recenzja, szukanie dziur i przesadzonych twierdzeń. Wklej prompt, a pod nim **zestawienie twierdzeń z Gemini/Cursora** albo plik bazy: `filar-1-przygotowanie/pozycja-przy-grindach/ (README.md i pliki per grind)`.

```
Act as a sceptical sports-medicine reviewer, biomechanist and methodologist. Below is a draft section of an open-source knowledge base on preparing the body for aggressive inline skating (AGV) grinds. Your job is to ATTACK it, not to improve the prose.

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

For every claim check and report:
1. Overstatement: does the claim say more than the cited source (population, effect size, causality, generalisation to AGV)?
2. Wrong label: is something labelled EVIDENCE that is really CONSENSUS, BIOMECH-INFERENCE, ANALOGY or SPECULATION? Is an analogy (skiing, snowboard, skateboarding, BMX, drop landings) presented as if it were AGV data?
3. Independence: are the "2 sources" truly independent (same authors/group, one citing the other)?
4. Missing counter-evidence: name specific studies that contradict or weaken the claim (with DOI/link). If you are not sure a study exists, say so — do not invent.
5. Unsafe advice: technique or training advice that could increase injury risk for a teenager or a returning skater.
6. Missing red flags / when to see a professional.

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
