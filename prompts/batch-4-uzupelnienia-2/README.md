# Batch 4 — uzupełnienia, runda 2

Cel: drugie niezależne źródło pierwotne — albo obalenie — dla twierdzeń, które po triage batch-3 i batch-1 B (`research-raw/2026-11-04_*`) nadal są 1/2, sporne albo mają źródło tylko pozornie niezależne.

## Pliki

- [`1-deep-research.prompt.txt`](1-deep-research.prompt.txt) — pełna wersja (~10 tys. znaków). **Przebieg w AI Studio (Deep Research Preview) 4.11.2026 padł** („An internal error has occurred” tuż przed raportem końcowym; prawdopodobnie za duży zakres). Zostaje jako archiwum.
- [`2a-kostka-screening-urazy.prompt.txt`](2a-kostka-screening-urazy.prompt.txt) — część A, grupy 1 i 2: C1, C2b, C3, C4 (kostka), D1–D9 (screening), A1, A2/A3, A4 (urazy, ochraniacze nadgarstka — rolki osobno od nart/snowboardu).
- [`2b-sciegna.prompt.txt`](2b-sciegna.prompt.txt) — część B, grupa 3: B1 (rzepka: ekscentryka vs HSR vs izometria, Li 2024 vs Liu 2026), B2 (Achilles), B3 (kolagen + trening), B4 (piszczelowy tylny), B5 (model monitorowania bólu), B6 (obciążenie ścięgna rzepki), B7 (but unieruchamiający).

Oba prompty są samodzielne (jedno wklejenie, można puścić równolegle) i mają te same zasady: test niezależności (autorzy + czy kandydat nie jest włączony do znanego przeglądu), rozdzielanie populacji, PMID/DOI ze strony PubMed, dosłowne cytaty, typ badania jak w pracy, „NIE ZNALEZIONO”, cytowanie [Autor rok, PMID]. Nowe w 2a/2b: zmieniona strategia wyszukiwania (synonimy i MeSH, PubMed + Cochrane + SPORTDiscus + Google Scholar + rejestry badań + repozytoria prac dyplomowych, inne typy badań, analogie tylko z etykietą {ANALOGIA}) i krótki raport końcowy (tabele, werdykty w jednym zdaniu, bez prozy) — żeby zmniejszyć ryzyko błędu przy pisaniu raportu.

Wynik → `research-raw/RRRR-MM-DD_batch4a_<narzędzie>.md` i `…_batch4b_…`, potem weryfikacja jak zawsze; do bazy tylko to, co sprawdzimy sami.
