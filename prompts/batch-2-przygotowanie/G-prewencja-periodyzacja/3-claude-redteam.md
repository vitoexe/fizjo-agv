# G. Prewencja i periodyzacja obciążenia sesji — Claude (red-teaming)

Rola: krytyczna recenzja, szukanie dziur i przesadzonych twierdzeń. Wklej prompt, a pod nim **zestawienie twierdzeń z Gemini/Cursora** albo plik bazy: `filar-1-przygotowanie/prewencja.md, rozgrzewka.md, obciazenie-i-periodyzacja.md`.

```
Act as a sceptical sports-medicine reviewer, biomechanist and methodologist. Below is a draft section of an open-source knowledge base on preparing the body for aggressive inline skating (AGV) grinds. Your job is to ATTACK it, not to improve the prose.

CONTEXT: We are building an open-source, Polish-language knowledge base "Fizjo AGV" for aggressive inline skaters (AGV), physiotherapists and coaches. The project has two pillars; the MAIN pillar is PREPARING THE BODY FOR GRINDS (correct body position, strength, stability, proprioception, mobility, prevention); rehabilitation is secondary. Topic: injury prevention and session load periodisation for aggressive inline skaters: warm-up content and duration, number of high-impact landings/drops per session, session frequency and rest days, fatigue and late-session injury risk, progression of trick difficulty, protective equipment (wrist guards, knee pads, helmets), concussion protocols, load-monitoring tools usable by amateur skaters.

What we already know (seed):
- Protective gear: no wrist guards -> OR 10.4 for wrist injury (S04); AGV gear use: knee pads 94%, wrist guards 41%, full set 32% (S01). Polish survey: pad users reported more injuries (correlation, likely riskier skating) (S36).
- Neuromuscular/balance training reduces ankle sprains ~40% (S16, S18).
- Tendon collagen synthesis elevated ~24 h to ~3 days after loading (S14) -> rationale for spacing hard sessions; pain-monitoring model (S11, S12) — from tendinopathy rehab.
- Opinion: >=10 min dynamic warm-up, worst injuries at session start without warm-up (S29); many injuries on simple tricks; learning new tricks faster/on harder obstacles raises risk (S33).
- FFRS concussion protocol for roller freestyle/skateboarding exists (S38, not yet read).
- No periodisation data for AGV or skateboarding at all.

Gaps (priority — pillar 1):
- Warm-up programme evidence (FIFA 11+-type neuromuscular warm-ups): effect sizes, duration. An unsourced '36% fewer lower-limb injuries in youth' figure needs a real source.
- Load monitoring in jump/landing sports (session RPE, landing counts, ACWR controversy) usable by amateurs.
- Fatigue and late-session injury risk in action/landing sports.
- Rest-day/frequency guidance for landing-heavy sports; youth-specific load guidance.
- Helmet use and concussion in inline/skateboarding; return to skating after concussion.

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
