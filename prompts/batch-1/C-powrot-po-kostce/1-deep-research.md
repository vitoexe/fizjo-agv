# C. Powrót do sportu po urazie kostki — Deep Research (Gemini, AI Studio)

Odświeżone 3.11.2026 pod aktualną bazę (148 źródeł) i w stylu B (zaostrzone zasady identyfikatorów po lekcji z batch-1 A).

- **Narzędzie:** Google AI Studio (Pro, przeglądarka) → Deep Research Preview (Max dziś nie kończył uruchomień). Jedno wklejenie.
- **Co wkleić:** dokładnie [`1-deep-research.prompt.txt`](1-deep-research.prompt.txt) (8361 znaków).
- **Wynik:** plik czatu z Drive albo „Copy as markdown” → `research-raw/RRRR-MM-DD_batch1-C_deep-research.md` (front-matter: `research-raw/README.md`).
- **Dlaczego po angielsku:** literatura i hasła głównie po angielsku; raport po polsku, z etykietami bazy.
- **Po wyniku:** każdy PMID/DOI sprawdzamy sami (PubMed/Crossref), niezależność grup, liczby tylko ze źródeł. Model nie jest źródłem.

```
Conduct a systematic literature review (Deep Research) on RETURN TO SPORT AFTER ANKLE INJURY for aggressive inline skaters (AGV): lateral ankle sprain, high ankle (syndesmotic) sprain, chronic ankle instability, ankle fracture (conservative and surgical/ORIF) and immobilisation — return-to-sport criteria, tests and thresholds, staged return, re-injury risk. Search in English (and German, French, Spanish, Polish where relevant), but WRITE THE WHOLE REPORT IN POLISH.

QUALITY OVER QUANTITY. A previous run on this project gave wrong or mismatched DOI/PMID pairs for 5 of 7 sources, attributed a number to a paper that does not contain it, and labelled clinic web pages as evidence. We re-check every identifier and every number. 8 correct sources are worth more than 30 doubtful ones.

CONTEXT
"Fizjo AGV" is an open-source, Polish-language, evidence-graded knowledge base for aggressive inline skaters, physiotherapists and coaches. AGV demands on the ankle: landings from ledges, rails and stairs in a stiff hard-shell boot with a high cuff (limited ankle motion, inversion partly blocked), grinds on the soul plate with the foot rotated and loaded at end range (topsoul), sudden stops when a wheel or plate catches. Ankle sprain is the most common and most recurrent injury in skateboarding (our S05); the only AGV injury survey (S144) found injuries mostly at obstacle contact and on landing. There are no AGV return-to-sport studies; transfer from other sports must be labelled as analogy.

READ FIRST (public raw files — what we already have; extend or challenge it, do not repeat it):
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/METHODOLOGY.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/sources.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/czesci-ciala/kostka/skrecenie.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/czesci-ciala/kostka/niestabilnosc.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/stabilizacja-i-propriocepcja.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/prewencja.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/wzorce-urazow-wg-grindow.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/soul-topsoul.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/propozycje-do-recenzji.md

The base has 148 sources (S01–S148). Key ones for this topic (do not re-report unless you correct them or bring an independent second source):
- Return to sport: S19 Smith 2021 (PAASS framework after lateral sprain, consensus); S20 Mazzella 2025 and S21 Sinha 2022 (return after ankle fracture, systematic reviews); S22, S23 hospital protocols (clinical material).
- Sprain treatment/prevention: S17 Doherty 2017 (overview of reviews); S18 NATA 2013 position statement; S16 Vriend (neuromuscular training meta-analysis); S80 Verhagen 2004, S82 McGuine 2006 (balance training, 2/2); S81 Hupperets 2009 (home training, recurrences); S83 Emery 2022.
- Context: S05 skateboarding survey; S53 Ou 2021 (ankle stability, pro vs amateur skateboarders); S141 de Noronha 2019 (sprains later in matches); S144 Maudot 2014 (AGV survey); S28 practitioner guide ({OPINIA}).
Currently 1/2 or missing: validated return-to-sport test batteries and thresholds (LSI ≥ 90% is a convention — is it validated for the ankle?); return after high ankle sprain; return after ORIF to jumping/landing sports; criteria-based vs time-based return; any data in skateboarding, BMX, snowboard or other boot sports.

QUESTIONS
1. Which return-to-sport criteria and test batteries after lateral ankle sprain have been studied (e.g. PAASS components, hop tests, Y-balance/SEBT, side hop, figure-of-8, strength by dynamometry, patient-reported scales such as CAIT/FAAM, ALR-RSI)? Which thresholds are used and are any validated against re-injury?
2. Limb symmetry index: is ≥ 90% supported for the ankle, or only borrowed from ACL literature? Problems of LSI (bilateral deficits).
3. Time-based vs criteria-based return: re-injury and chronic ankle instability rates; what share of athletes return before meeting criteria.
4. High ankle (syndesmotic) sprain: time to return, grading, criteria; anything in boot sports (ice hockey, skiing).
5. Ankle fracture (conservative vs ORIF) and immobilisation: return rates and times, criteria, return to jumping/landing sports; hardware and stiff boots.
6. Braces, taping and boots after return: effect on re-injury; relevance of a stiff skate boot as external support.
7. Contradictions with our base files listed above.

RULES (mandatory — violations make the report unusable)
1. Identifiers: for every source give PMID AND DOI COPIED FROM ITS PUBMED PAGE (pubmed.ncbi.nlm.nih.gov/<PMID>/), plus PMCID if present. Open the PubMed page and check first author, year and title match. If you did not open it or anything does not match, write "UNVERIFIED" in that cell. Never guess, reconstruct or "complete" an identifier. Sources outside PubMed: DOI from doi.org/Crossref, or the repository URL.
2. Links only to pubmed.ncbi.nlm.nih.gov, pmc.ncbi.nlm.nih.gov, doi.org or the publisher/repository. NO redirect links (vertexaisearch, google.com/url).
3. Numbers: report a number ONLY if it appears in a source listed in your bibliography (section 8), and say where (abstract / full text, table/page). No number may appear in sections 1–6 without a bibliography entry. Give n for every study.
4. Evidence vs opinion: blogs, clinic or hospital web pages, physio interviews, forums, podcasts and commercial pages may ONLY be labelled {OPINIA} and must never support a {DOWÓD} or a 2/2 claim. Clinical guidelines/position statements = {KONSENSUS}.
5. Correct study type: cadaver, laboratory or biomechanics studies are NOT RCTs; narrative reviews are not systematic reviews.
6. Labels (one main label per claim): {DOWÓD:przegląd} | {DOWÓD:RCT} | {DOWÓD:obserwacyjne} | {KONSENSUS} | {WNIOSKOWANIE} | {SPEKULACJA} | {OPINIA}; add {ANALOGIA:<populacja>} whenever data is not from AGV (that is almost always).
7. 2/2 only with >= 2 INDEPENDENT primary sources (different research groups — check first and senior authors). A review plus a study it includes is NOT two sources. Same author = not independent. Otherwise 1/2.
8. AI models, including you, are not sources. If nothing exists, write "BRAK DANYCH" with databases and terms searched.
9. Prefer sources not yet in sources.md; we especially want independent second sources for existing 1/2 claims.

OUTPUT FORMAT (Markdown, Polish, exactly these sections in this order)

## 1. Podsumowanie
5–8 zdań: co nowego, luki, ile nowych źródeł, ile twierdzeń 2/2, ile identyfikatorów UNVERIFIED.

## 2. Twierdzenia
| # | Twierdzenie (1 zdanie, PL) | Etykieta | Źródła (autor rok) | PMID | DOI | Populacja | n | Gdzie sprawdzone (abstrakt/pełny tekst, tabela/strona) | Licznik (1/2 lub 2/2) | Niezależność (grupy) |
|---|---|---|---|---|---|---|---|---|---|---|

## 3. Testy i kryteria powrotu (tylko z badań)
| Test / kryterium | Uraz | Próg dokładnie jak w źródle (np. LSI %, czas, liczba powtórzeń) | Czy próg zwalidowano wobec nawrotu urazu? (tak/nie/BRAK DANYCH) | Źródło | Etykieta |
|---|---|---|---|---|---|

## 4. Według urazu
Krótkie akapity: skręcenie boczne, skręcenie wysokie (więzozrost), przewlekła niestabilność, złamanie kostki (zachowawczo / ORIF), unieruchomienie — dla każdego: etapy, testy, czas powrotu, ryzyko nawrotu; każde zdanie z [źródło] i {ETYKIETA}.

## 5. Sprzeczności z naszą bazą
| Plik bazy | Nasze twierdzenie (cytat) | Co mówi nowe źródło | PMID / DOI | Proponowana zmiana |
|---|---|---|---|---|

## 6. Wnioskowanie dla AGV (NIE dowód)
- wniosek — na podstawie: [źródła] {WNIOSKOWANIE}

## 7. BRAK DANYCH
- pytanie — przeszukane bazy i hasła

## 8. Bibliografia (nowe źródła)
| # | Pełny opis (autorzy, rok, tytuł, czasopismo, tom:strony) | Typ badania | n | PMID | DOI | PMCID | Grupa / autor senior |
|---|---|---|---|---|---|---|---|

## 9. Identifier check
| Źródło | PMID | DOI | Otwarta strona PubMed? tak/nie | Autor+rok+tytuł zgodne? tak/nie/UNVERIFIED |
|---|---|---|---|---|

## 10. Opinie praktyków (osobno, nie dowód)
| Kto | Co twierdzi | Link | {OPINIA} |
|---|---|---|---|
```
