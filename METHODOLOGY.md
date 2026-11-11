# Metodologia zbierania wiedzy

Źródło: punkt 7 trackera projektu („Plan zbierania wiedzy z wielu źródeł”, Google Tasks „Fizjo AGV”, 2.11.2026).

## Dwa filary i priorytet (decyzja z 2.11.2026, punkt 2 trackera)

- **Filar 1 — Przygotowanie do grindów: GŁÓWNY.** Anatomicznie prawidłowa pozycja przy grindach (kostka, kolano, biodro, tułów, ugięcie, najazd, lądowanie), wzmacnianie, stabilizacja, propriocepcja, mobilność, rozgrzewka, obciążenie i periodyzacja, prewencja. **Większość researchu ma dotyczyć tego filaru.**
- **Filar 2 — Rehabilitacja po urazach: mniejszy.** Urazy wg części ciała, powrót do grindów. Rozwijany wolniej, z recenzją fizjoterapeuty.
- Autor projektu nie jest specjalistą — dlatego tym ważniejsze są etykiety, zasada 2 źródeł i recenzja ekspertów (`zasoby/specjalisci.md`).

## Zasada nadrzędna: AI to narzędzie, nie źródło

Modele AI służą do **szukania i syntezy**. W bazie nigdy nie cytujemy modelu. Cytujemy badanie, stanowisko lub stronę, które model wskazał — po otwarciu i sprawdzeniu, że mówi to, co model twierdzi.

## Role narzędzi

| Narzędzie | Do czego | Czego NIE robi |
|---|---|---|
| **Deep Research (Google)** | szerokie przeglądy literatury i internetu na start każdego tematu | nie jest ostatnim słowem; wynik idzie do pogłębienia i weryfikacji |
| **Gemini Pro (AI Pro)** | główny koń roboczy: pogłębienia i synteza, lista twierdzeń ze źródłami; używać dużo | nie rozstrzyga sporów samodzielnie |
| **Claude** | krytyczna recenzja i szukanie dziur we wnioskach (red-teaming), wyłapywanie przesadzonych twierdzeń | nie dopisuje nowych twierdzeń bez źródeł |
| **Modele w Cursorze** | strukturyzacja bazy, krzyżowe sprawdzanie twierdzeń i źródeł (zgodne/sprzeczne), formatowanie pod stronę, sprawdzanie linków | nie są źródłem |
| **Aplikacja Health** | szybkie, wąskie pytania w trakcie; Tomasz wkleja prompt i odsyła wynik | nie do szerokich przeglądów |
| **Google AI Studio** | eksperymenty z promptami i szablonami (np. prompt do ekstrakcji twierdzeń ze źródłem) | nie do produkcji treści bazy |
| **Argon** | drogi — tylko najtrudniejsze pytania, gdy inne źródła się nie zgadzają | nie do rutynowego researchu |

Punkt odniesienia: research z 2.11.2026 (23 źródła o grindach) — zob. `sources.md`.

## Zasady

1. **Min. 2 niezależne źródła pierwotne** na twierdzenie, zanim zostanie przyjęte (`2/2`). Dwa modele powtarzające to samo ≠ dwa źródła. Dwie prace tego samego zespołu też nie są w pełni niezależne (zaznacz w `sources.md`).
   **Poradniki a baza (decyzja 11.11.2026).** Poradniki (`poradniki/`) mogą zawierać sekcję „Wskazówki do przetestowania (niepotwierdzone)” z radami technicznymi, które mają tylko jedno źródło, przekaz ustny albo niesprawdzone jeszcze wideo. Każda taka rada ma etykietę, liczbę źródeł i ocenę fizjo (albo „brak danych”). Do bazy wiedzy (`filar-*`, `sources.md`) twierdzenie wchodzi dopiero po 2 niezależnych źródłach pierwotnych (`2/2`).
2. **Każde twierdzenie z cytowanym źródłem i linkiem** (DOI/PubMed preferowane).
3. **Etykiety** (pełny opis w README):
   - `{DOWÓD:przegląd|RCT|obserwacyjne}` — dowód z badania,
   - `{KONSENSUS}` — konsensus ekspertów, stanowisko, protokół kliniczny,
   - `{WNIOSKOWANIE}` — wnioskowanie biomechaniczne,
   - `{ANALOGIA:sport/populacja}` — analogia z innego sportu lub populacji,
   - `{SPEKULACJA}` — spekulacja,
   - rozszerzenia bazy: `{OPINIA}` (pojedynczy praktyk/blog), `{PROPOZYCJA}` (propozycja projektu).
4. **Brak danych zgłaszamy, nie zgadujemy.** „Nie znaleziono badań” jest pełnoprawnym wynikiem.

## Kolejność pracy nad tematem

1. **Deep Research**: szeroki przegląd tematu.
2. **Gemini Pro**: pogłębienie i synteza, lista twierdzeń ze źródłami.
3. **Cursor**: zestawienie twierdzeń ze wszystkich źródeł, oznaczenie zgodnych i sprzecznych, sprawdzenie linków i liczb w abstraktach.
4. **Claude**: recenzja i atak na wnioski, szukanie przesadzonych twierdzeń.
5. **Argon**: tylko nierozstrzygnięte sprzeczności.
6. **Health**: szybkie dopytania w trakcie.
7. **Zapis do bazy** według kontuzji i części ciała, z etykietami → review (CONTRIBUTING.md).

## Kolejność partii researchu

1. **`prompts/batch-2-przygotowanie/` E i F** — biomechanika i pozycja przy grindach; program wzmacniania i stabilizacji (filar 1, najwyższy priorytet).
2. **batch-2 G** — prewencja i periodyzacja sesji.
3. **batch-1 A i B** — wzorce urazów wg grindu; obciążanie ścięgien (wspierają filar 1).
4. **batch-1 C i D** — powrót po kostce; screening fizjo (filar 2, niższy priorytet).

## Druga partia tematów (prompty w `prompts/batch-2-przygotowanie/`)

- **E.** Biomechanika i prawidłowa pozycja przy grindach; analogie (skateboarding, narciarstwo freestyle, snowboard, BMX); lądowania z wysokości, kolano w valgus, kostka w inwersji/ewersji.
- **F.** Program wzmacniania i stabilizacji dla AGV: kostka, łydka, piszczelowy tylny, biodro, core, nadgarstek.
- **G.** Prewencja i periodyzacja obciążenia sesji.

## Pierwsza partia tematów (prompty w `prompts/batch-1/`)

- **A.** Wzorce kontuzji według typu grindu (soul, topsoul, makio, frontside, backside, royale, unity, stalle); kostka, Achilles, piszczelowy tylny, kolano, nadgarstki.
- **B.** Obciążanie ścięgien: izometria, ciężki wolny trening, zasada bólu, monitoring 24 h, kolagen z witaminą C.
- **C.** Kryteria powrotu do sportu po urazie lub unieruchomieniu kostki: testy, progi 90% symetrii, etapy powrotu do grindów.
- **D.** Badanie przesiewowe fizjoterapeuty dla zawodnika AGV: zakres ruchu, siła łydki i inwersji, równowaga, testy skoczne, historia urazów.
