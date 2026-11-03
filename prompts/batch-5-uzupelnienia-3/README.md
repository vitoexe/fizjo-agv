# Batch-5 — uzupełnienia, runda 3 (Gemini Deep Research)

Trzecia runda szukania drugiego niezależnego źródła dla twierdzeń, które po triage batch-4 (2a-AIS, 2a-GEM, 2b) nadal mają status „brak drugiego źródła” albo są sprzeczne. Prompty są przeznaczone dla Gemini Deep Research. Limit dzienny AI Studio jest wyczerpany. Każdy prompt ma poniżej ok. 7 tys. znaków.

| Plik | Zakres |
|---|---|
| `a-kostka-screening-urazy.prompt.txt` | C1, C2b (sprzeczne), C3, C4, D1, D2, D3 (normy), D4, D5b – zakres ruchu w niestabilności (sprzeczne), D6, D8 (sprzeczne), D9, A1, A2 (splint-top), A4 |
| `b-sciegna.prompt.txt` | B1 (sprzeczne), B2, B3, B4, B5, B6 (pełny ranking), B7 |

## Czym strategia różni się od batch-4
1. **Tropy cytowań zamiast haseł:** przy każdym twierdzeniu podany jest punkt startowy. Model ma przejrzeć jego bibliografię (wstecz) i prace, które go cytują (w przód). Przykłady: Schrefl 2026 (PMID 41925545) dla D3/D4; Hadadi 2014 i 2019, Wikstrom 2006 i Gribble 2010 dla C2b; pozostałe tropy pochodzą z triage batch-4.
2. **Źródła spoza głównego nurtu:** Europe PMC (z preprintami), PEDro, J-STAGE, SciELO, abstrakty kongresowe (ECSS, ISBS, ACSM) i czasopisma nieanglojęzyczne. Abstrakty kongresowe i prace dyplomowe to szara literatura: same nie dają 2/2.
3. **Sprzeczności bez werdyktu:** model podaje badania pierwotne po każdej stronie sporu i różnice metod między nimi.
4. **Jawna niezależność:** przy każdej pracy model podaje wszystkich współautorów, wspólnych autorów ze źródłem znanym i to, czy praca jest włączona do znanego przeglądu.
5. **Format raportu:** krótki, jak w batch-4: tabele, etykiety {ANALOGIA:…}, bibliografia oraz osobna sekcja sprawdzenia identyfikatorów.

Wszystkie numery PMID w promptach zostały sprawdzone w PubMed (esummary) przed commitem.
Wyniki trafiają do `research-raw/` ze statusem „niezweryfikowane”. Do bazy wiedzy łączymy tylko twierdzenia, które przejdą triage: dwa niezależne źródła (2/2), sprawdzone identyfikatory, poprawne etykiety i brak nierozwiązanej sprzeczności.
