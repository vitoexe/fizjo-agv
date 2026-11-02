# A. Wzorce urazów według typu grindu — Claude (red-teaming)

Rola: krytyczna recenzja, szukanie dziur i przesadzonych twierdzeń. Wklej prompt, a pod nim **zestawienie twierdzeń z Gemini/Cursora** albo plik bazy: `filar-1-przygotowanie/wzorce-urazow-wg-grindow.md` (tabela grind → struktura) i `filar-1-przygotowanie/pozycja-przy-grindach/`.

```
Act as a sceptical sports-medicine reviewer and methodologist. Below is a draft section of an open-source physiotherapy knowledge base for aggressive inline skaters (AGV). Your job is to ATTACK it, not to improve the prose.

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
