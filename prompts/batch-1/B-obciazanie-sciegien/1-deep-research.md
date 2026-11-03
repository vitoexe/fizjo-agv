# B. Obciążanie ścięgien (Achilles, piszczelowy tylny) — Deep Research Max/Preview (Gemini, AI Studio)

Odświeżone 3.11.2026 pod aktualną bazę (148 źródeł, S01–S148) i po lekcjach z batch-1 A.

- **Narzędzie:** Google AI Studio (Pro, przeglądarka, bez klucza API) → Deep Research Max (albo Preview). Jedno wklejenie.
- **Co wkleić:** dokładnie [`1-deep-research.prompt.txt`](1-deep-research.prompt.txt) (7712 znaków).
- **Wynik:** „Copy as markdown” albo plik czatu z Drive → `research-raw/RRRR-MM-DD_batch1-B_deep-research-max.md` (front-matter: `research-raw/README.md`).
- **Dlaczego po angielsku:** literatura i hasła wyszukiwania są głównie po angielsku; odpowiedź ma być po polsku, z etykietami bazy.
- **Co zmieniono po batch-1 A** (model podał błędne pary DOI/PMID w 5 z 7 źródeł): PMID i DOI mają być skopiowane ze strony PubMed, a przy braku pewności „UNVERIFIED”; blogi i strony klinik tylko jako {OPINIA} (osobna sekcja 10); liczby tylko ze źródeł w bibliografii; poprawny typ badania (zwłoki/laboratorium ≠ RCT); „mniej, ale poprawnie”.
- **Po wyniku:** każdy PMID/DOI sprawdzamy sami (PubMed efetch / Crossref) i sprawdzamy niezależność grup. Model nie jest źródłem.

```
Conduct a systematic literature review (Deep Research) on TENDON LOAD MANAGEMENT for aggressive inline skaters (AGV): Achilles tendon and tibialis posterior — prevention, rehabilitation and return to skating. Search in English (and German, French, Spanish, Polish where relevant), but WRITE THE WHOLE REPORT IN POLISH.

QUALITY OVER QUANTITY. A previous run on this project gave wrong or mismatched DOI/PMID pairs for 5 of 7 sources, attributed a number to a paper that does not contain it, and labelled clinic web pages as evidence. We re-check every identifier and every number. 8 correct sources are worth more than 30 doubtful ones.

CONTEXT
"Fizjo AGV" is an open-source, Polish-language, evidence-graded knowledge base for aggressive inline skaters, physiotherapists and coaches. AGV loads: repeated landings from ledges, rails and stairs in a stiff hard-shell boot (limited ankle motion), grinds on the soul plate (one foot often loaded longer, foot rotated/inverted), long sessions. There is no AGV-specific tendon research; transfer from other populations must be labelled as analogy.

READ FIRST (public raw files — what we already have; extend or challenge it, do not repeat it):
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/METHODOLOGY.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/sources.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/czesci-ciala/achilles/tendinopatia.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/czesci-ciala/piszczelowy-tylny/tendinopatia.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/obciazenie-i-periodyzacja.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/wzmacnianie.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/wzorce-urazow-wg-grindow.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/soul-topsoul.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/propozycje-do-recenzji.md

The base has 148 sources (S01–S148). Key ones for this topic (do not re-report unless you correct them or bring an independent second source):
- Achilles: S09 Beyer 2015 (HSR vs eccentric RCT, PMID 26018970); S10 Jonsson 2008 (insertional, eccentric to floor level, pilot, PMID 18184750); S11 Silbernagel 2007 (pain-monitoring model RCT, PMID 17307888); S12 Silbernagel 2015 and S13 Silbernagel 2020 (same author — NOT independent of S11).
- Tendon biology/isometrics: S14 Magnusson 2010 (narrative review); S15 Clifford 2020 (isometrics meta-analysis, not superior to isotonic); S101 Miller 2005 (collagen synthesis after exercise, patellar tendon).
- Tibialis posterior: S07 NHS BNSSG programme (clinical material); S08 Kulig 2009 (orthoses + resistive exercise RCT, PMID 19022863); S39 practitioner post ({OPINIA}).
- Load monitoring: S92–S94 (ACWR critique, e.g. S93 Impellizzeri 2021); S89 Moran 2023 (plyometrics and stiffness).
Currently 1/2 or missing: pain-monitoring model from authors other than Silbernagel; any tibialis posterior evidence beyond S08; collagen/gelatin + vitamin C (nothing in base).

QUESTIONS
1. Pain-monitoring model / pain-guided loading: evidence from research groups OTHER than Silbernagel (Achilles, patellar, tibialis posterior). Thresholds used (pain during and next morning)?
2. HSR vs eccentric vs isometric vs isotonic: newest RCTs and meta-analyses (2020 onward), including in-season athletes and pre-session analgesia.
3. Insertional vs midportion Achilles: different loading rules (dorsiflexion range, heel drop, footwear/heel lift)? Relevance to a stiff boot.
4. Tibialis posterior tendinopathy / PTTD stage I–II: exercise RCTs, orthoses, return to sport; anything in athletes.
5. Collagen/gelatin + vitamin C before loading: RCTs with TENDON outcomes (pain, function, structure), not only blood biomarkers. Doses and timing exactly as reported.
6. Landing/jumping sports: how tendon load is progressed and monitored (jump counts, session RPE, morning stiffness); prospective data linking load to tendinopathy.
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

## 3. Protokoły obciążania (tylko z badań)
| Protokół | Struktura | Parametry dokładnie jak w źródle (serie, powt., tempo, częstotliwość, czas, progi bólu) | Źródło | Etykieta |
|---|---|---|---|---|

## 4. Według struktury
Krótkie akapity: Achilles (środkowa część), Achilles (przyczep), piszczelowy tylny, inne ścięgna istotne dla AGV — każde zdanie z [źródło] i {ETYKIETA}.

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
