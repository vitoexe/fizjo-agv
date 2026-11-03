# D. Badanie przesiewowe fizjoterapeuty dla zawodnika AGV — Deep Research (Gemini)

Odświeżone 3.11.2026 pod aktualną bazę (152 źródła) w stylu B/C. Temat z planu (METHODOLOGY.md, „Pierwsza partia tematów”, D): zakres ruchu, siła łydki i inwersji, równowaga, testy skoczne, jakość lądowania, historia urazów.

- **Narzędzie:** Deep Research w Gemini (aplikacja Gemini, Pro Rozszerzony — jak C — albo AI Studio Deep Research Preview). Jedno wklejenie.
- **Co wkleić:** dokładnie [`1-deep-research.prompt.txt`](1-deep-research.prompt.txt) (10298 znaków).
- **Wynik:** eksport do Google Docs albo „Copy as markdown” → `research-raw/RRRR-MM-DD_batch1-D_<narzędzie>.md` (front-matter: `research-raw/README.md`).
- **Dlaczego po angielsku:** literatura i hasła głównie po angielsku; raport po polsku, z etykietami bazy.
- **Nowe zasady po lekcji z C:** przypisanie każdego zdania do właściwej pracy (np. ram konsensusu tylko do pracy, która je opublikowała), typ badania dokładnie jak w pracy (crossover ≠ RCT, opinie ekspertów = {KONSENSUS}), 2/2 tylko gdy każde źródło samo popiera to samo twierdzenie, w sekcji sprzeczności wyłącznie dosłowne cytaty z naszych plików.
- **Po wyniku:** każdy PMID/DOI sprawdzamy sami (PubMed/Crossref), każde zdanie i liczbę porównujemy z abstraktem, niezależność grup po listach autorów. Model nie jest źródłem.

```
Conduct a systematic literature review (Deep Research) on a PHYSIOTHERAPY SCREENING BATTERY for aggressive inline skaters (AGV): ankle dorsiflexion range (e.g. weight-bearing lunge test), hip rotation, calf and ankle inversion/eversion strength (heel-raise endurance, hand-held dynamometry), balance (single-leg stance, Star Excursion / Y-Balance Test), hop and jump tests, landing quality (e.g. LESS), and injury-history / ankle-function questionnaires (e.g. CAIT, FAAM). For each test: reliability, normative or cut-off values, and whether it predicts injury. Search in English (and German, French, Spanish, Polish where relevant), but WRITE THE WHOLE REPORT IN POLISH.

QUALITY OVER QUANTITY. Earlier runs on this project: (A) gave wrong or mismatched DOI/PMID pairs for 5 of 7 sources and labelled clinic pages as evidence; (C) had correct identifiers, but attributed a framework to the wrong paper, added details that are not in the cited paper, relabelled a crossover study as an RCT and expert opinions as evidence, called a claim 2/2 when the second source did not say the same thing, and invented "quotes" from our base in the contradictions section. We re-check every identifier, every number, every sentence against the abstract or full text, and every quote against our files. 8 correct sources are worth more than 30 doubtful ones.

CONTEXT
"Fizjo AGV" is an open-source, Polish-language, evidence-graded knowledge base for aggressive inline skaters, physiotherapists and coaches. AGV demands: landings from ledges, rails and stairs in a stiff hard-shell boot with a high cuff (ankle motion limited, inversion partly blocked), grinds on the soul plate with the foot rotated and loaded at end range (topsoul), crossed-leg grinds needing hip rotation, frequent falls onto hands. Ankle injuries are frequent in skate sports (our S01, S05); the only recent AGV injury survey (S144) found injuries mostly at obstacle contact and on landing. There is no AGV screening study; transfer from other sports must be labelled as analogy. We want a short, field-usable battery a physio can run in 20–30 minutes, and an honest statement of what screening can and cannot predict.

READ FIRST (public raw files — what we already have; extend or challenge it, do not repeat it):
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/METHODOLOGY.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/sources.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/mobilnosc.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/stabilizacja-i-propriocepcja.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/wzmacnianie.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/prewencja.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/propozycje-do-recenzji.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/czesci-ciala/kostka/skrecenie.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/czesci-ciala/kostka/niestabilnosc.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/powrot-do-grindow.md

The base has 152 sources (S01–S152). Key ones for this topic (do not re-report unless you correct them or bring an independent second source):
- Landing quality: S50 Padua 2009 (LESS validity/reliability), S51 Padua 2015 (LESS screening in youth soccer), S49 Kuenze 2015, S66 Uddin 2026 (landing assessment review); S72 Abbasi 2025 (fatigue and knee valgus); S106–S109 (hip strength vs knee valgus, knee abduction as ACL predictor), S118 Arundale 2023 (JOSPT guideline).
- Ankle: S53 Ou 2021 (ankle stability, pro vs amateur skateboarders); S16, S54, S80, S82 (balance/neuromuscular training prevents sprains); S17, S18 (sprain reviews, NATA statement); S19 PAASS and S149–S150 (no validated return-to-sport thresholds after lateral sprain); S22, S23 clinical protocols with heel-raise and hop tests (clinical material, not evidence).
Currently missing or 1/2: reliability and normative values of the weight-bearing lunge test, heel-raise test, SEBT/Y-Balance, side hop and other hop tests, inversion/eversion dynamometry in athletes; whether any of them predicts ankle or knee injury prospectively; screening batteries used in skateboarding, BMX, snowboard park, parkour, gymnastics or other landing sports; questionnaire validation (CAIT, FAAM, IdFAI).

QUESTIONS
1. Ankle dorsiflexion (weight-bearing lunge test): reliability, typical values, does reduced dorsiflexion predict ankle sprain or other lower-limb injury?
2. Calf and inversion/eversion strength: heel-raise endurance test protocols and norms; hand-held dynamometry reliability; link to injury.
3. Balance: single-leg stance, SEBT / Y-Balance — reliability, composite-reach cut-offs (e.g. anterior asymmetry), predictive value; conflicting prospective studies.
4. Hop and jump tests (side hop, figure-of-8, single/triple hop, drop jump): reliability, norms, injury prediction.
5. Landing quality (LESS, drop vertical jump, single-leg squat): predictive value for injury beyond ACL in soccer — anything for landing/action sports?
6. Questionnaires: CAIT, FAAM, IdFAI — validation, cut-offs for chronic ankle instability (e.g. International Ankle Consortium criteria).
7. Screening batteries in action/board sports or landing sports, and the general evidence on whether pre-participation screening predicts or prevents injury.
8. Contradictions with our base files listed above.

RULES (mandatory — violations make the report unusable)
1. Identifiers: for every source give PMID AND DOI COPIED FROM ITS PUBMED PAGE (pubmed.ncbi.nlm.nih.gov/<PMID>/), plus PMCID if present. Open the PubMed page and check first author, year and title match. If you did not open it or anything does not match, write "UNVERIFIED" in that cell. Never guess, reconstruct or "complete" an identifier. Sources outside PubMed: DOI from doi.org/Crossref, or the repository URL.
2. Links only to pubmed.ncbi.nlm.nih.gov, pmc.ncbi.nlm.nih.gov, doi.org or the publisher/repository. NO redirect links (vertexaisearch, google.com/url).
3. Numbers: report a number ONLY if it appears in a source listed in your bibliography (section 8), and say where (abstract / full text, table/page). No number may appear in sections 1–6 without a bibliography entry. Give n for every study.
4. Attribution: every sentence must be supported by the exact paper cited next to it. Do not attribute a framework, test, cut-off, population or detail to a paper that does not contain it (e.g. a consensus framework belongs only to the paper that published it, not to reviews that discuss it). Do not add populations, sports, equipment or mechanisms that the paper does not describe. If you cannot point to the sentence or table in that paper, drop the claim.
5. Study design exactly as the paper states it: cadaver, laboratory, biomechanics, crossover, cohort, cross-sectional and reliability studies are NOT RCTs; call something an RCT only if the paper says participants were randomised to groups. Narrative reviews are not systematic reviews. A review of expert opinions is {KONSENSUS}, not {DOWÓD}.
6. Evidence vs opinion: blogs, clinic or hospital web pages, physio interviews, forums, podcasts and commercial pages may ONLY be labelled {OPINIA} and must never support a {DOWÓD} or a 2/2 claim. Clinical guidelines/position statements = {KONSENSUS}.
7. Labels (one main label per claim): {DOWÓD:przegląd} | {DOWÓD:RCT} | {DOWÓD:obserwacyjne} | {KONSENSUS} | {WNIOSKOWANIE} | {SPEKULACJA} | {OPINIA}; add {ANALOGIA:<populacja>} whenever data is not from AGV (that is almost always).
8. 2/2 only with >= 2 INDEPENDENT primary sources (different research groups — check first and senior authors and co-authorship of shared consensus papers) that EACH support the SAME claim on their own. A review plus a study it includes is NOT two sources. Same author = not independent. Otherwise 1/2.
9. Contradictions section: quote ONLY text that is actually present in our files linked above (copy it verbatim, with the file name). If you cannot find a verbatim sentence in our files, do not list a contradiction. Never paraphrase our base as a "quote".
10. AI models, including you, are not sources. If nothing exists, write "BRAK DANYCH" with databases and terms searched.
11. Prefer sources not yet in sources.md; we especially want independent second sources for existing 1/2 claims.

OUTPUT FORMAT (Markdown, Polish, exactly these sections in this order)

## 1. Podsumowanie
5–8 zdań: co nowego, luki, ile nowych źródeł, ile twierdzeń 2/2, ile identyfikatorów UNVERIFIED.

## 2. Twierdzenia
| # | Twierdzenie (1 zdanie, PL) | Etykieta | Źródła (autor rok) | PMID | DOI | Populacja | n | Gdzie sprawdzone (abstrakt/pełny tekst, tabela/strona) | Licznik (1/2 lub 2/2) | Niezależność (grupy) |
|---|---|---|---|---|---|---|---|---|---|---|

## 3. Testy przesiewowe (tylko z badań)
| Test | Co mierzy | Protokół w skrócie | Rzetelność (ICC itp., dokładnie jak w źródle) | Normy / próg dokładnie jak w źródle | Czy przewiduje uraz? (tak/nie/sprzeczne/BRAK DANYCH) | Źródło | Etykieta |
|---|---|---|---|---|---|---|---|

## 4. Według obszaru
Krótkie akapity: zakres ruchu (kostka, biodro), siła (łydka, inwersja/ewersja), równowaga, testy skoczne, jakość lądowania, kwestionariusze, baterie w sportach akcji — każde zdanie z [źródło] i {ETYKIETA}.

## 5. Sprzeczności z naszą bazą
| Plik bazy | Nasze twierdzenie (dosłowny cytat z pliku) | Co mówi nowe źródło | PMID / DOI | Proponowana zmiana |
|---|---|---|---|---|

## 6. Wnioskowanie dla AGV (NIE dowód)
- wniosek (np. propozycja baterii 20–30 min) — na podstawie: [źródła] {WNIOSKOWANIE}

## 7. BRAK DANYCH
- pytanie — przeszukane bazy i hasła

## 8. Bibliografia (nowe źródła)
| # | Pełny opis (autorzy, rok, tytuł, czasopismo, tom:strony) | Typ badania (jak w pracy) | n | PMID | DOI | PMCID | Grupa / autor senior |
|---|---|---|---|---|---|---|---|

## 9. Identifier check
| Źródło | PMID | DOI | Otwarta strona PubMed? tak/nie | Autor+rok+tytuł zgodne? tak/nie/UNVERIFIED |
|---|---|---|---|---|

## 10. Opinie praktyków (osobno, nie dowód)
| Kto | Co twierdzi | Link | {OPINIA} |
|---|---|---|---|
```
