# Fizjo AGV

Otwarta baza wiedzy o fizjoterapii w jeździe na rolkach agresywnych (aggressive inline, AGV): urazy, prewencja, rozgrzewka, wzmacnianie, obciążanie ścięgien i powrót do grindów po kontuzji.

Dla kogo:
- **rolkarzy**, którzy chcą zrozumieć swój uraz i pokazać materiał fizjoterapeucie lub trenerowi,
- **fizjoterapeutów i trenerów**, którzy prowadzą zawodnika AGV i nie znają specyfiki grindów.

> ⚠️ **To nie jest diagnoza ani porada medyczna.** Baza zbiera i porządkuje źródła. Nie zastępuje badania przez lekarza ani fizjoterapeutę. Obrzęk, ból nocny, ból narastający mimo odpoczynku, niemożność wspięcia się na palce jednej nogi, zniekształcenie lub drętwienie = wizyta u specjalisty, nie lektura.

## Stan projektu

Wersja 0.1 (2.11.2026): szkielet + treść przeniesiona z pierwszego researchu o grindach. **Nic tu nie przeszło jeszcze review fizjoterapeuty.** Wszystkie pliki mają `status: szkic`.

## Struktura

```
czesci-ciala/            # wg części ciała i kontuzji
  kostka/                skrecenie.md, niestabilnosc.md
  achilles/              tendinopatia.md
  piszczelowy-tylny/     tendinopatia.md
  kolano/                urazy.md
  nadgarstek-reka/       urazy.md
przekrojowe/             # tematy wspólne
  wzorce-urazow-wg-grindow.md
  rozgrzewka.md
  wzmacnianie.md
  obciazenie-sciegien.md
  powrot-do-grindow.md
_szablon/temat.md        # szablon nowego pliku
zasoby/                  # blogi, Instagram, specjaliści (opinie praktyków, nie dowody)
sources.md               # bibliografia (S01, S02, ...)
CONTRIBUTING.md          # jak dodawać i weryfikować treści
METHODOLOGY.md           # jak zbieramy wiedzę: narzędzia, zasada 2 źródeł, etykiety
prompts/batch-1/         # gotowe prompty dla pierwszej partii tematów
```

## Jak czytać poziomy dowodów

Każde twierdzenie kończy się znacznikiem źródła `[S07]` (lista w `sources.md`), etykietą w nawiasach klamrowych i statusem weryfikacji, np.:

`Ciężki, wolny trening łydki dał po roku takie same efekty jak ekscentryka. [S09] {DOWÓD:RCT} ✔ 1/2`

Etykiety (zgodnie z `METHODOLOGY.md`):

| Etykieta | Co oznacza | Jak ufać |
|---|---|---|
| `{DOWÓD:przegląd}` | przegląd systematyczny / metaanaliza | najmocniejsze, ale zwykle nie o AGV |
| `{DOWÓD:RCT}` | badanie randomizowane | mocne dla badanej grupy |
| `{DOWÓD:obserwacyjne}` | badanie obserwacyjne, ankietowe, laboratoryjne, pilotażowe | kierunek, nie pewnik; często małe próby |
| `{KONSENSUS}` | stanowisko towarzystwa, konsensus ekspertów, protokół kliniczny | praktyka kliniczna, nie zawsze testowana |
| `{WNIOSKOWANIE}` | wnioskowanie biomechaniczne z anatomii/fizjologii, bez bezpośredniego badania | hipoteza do sprawdzenia |
| `{ANALOGIA}` | wynik z innego sportu (np. skateboarding) lub innej populacji — dopisywane obok, np. `{DOWÓD:obserwacyjne}{ANALOGIA:skateboarding}` | przeniesienie na AGV to założenie |
| `{SPEKULACJA}` | luźna hipoteza, brak wsparcia w źródłach | tylko jako pytanie do researchu |
| `{OPINIA}` *(rozszerzenie)* | pojedyncza opinia praktyka, blog fizjo, materiał dla pacjentów | doświadczenie, nie dowód; słabsze niż konsensus |
| `{PROPOZYCJA}` *(rozszerzenie)* | propozycja projektu, np. przypisanie etapów powrotu do konkretnych grindów | do dyskusji, nie z badań |

Status weryfikacji:
- ✔ — liczba/teza sprawdzona w abstrakcie źródła; ⏳ — przeniesione z researchu, do sprawdzenia w pełnym tekście,
- `1/2` / `2/2` — liczba niezależnych źródeł pierwotnych. **Twierdzenie jest „przyjęte” dopiero przy 2/2** (zasada z METHODOLOGY.md). Wersja 0.1 ma prawie wszędzie 1/2.

W każdym pliku sekcje są rozdzielone: **Co wiemy z badań** → **Wnioskowanie biomechaniczne** → **Praktyka i opinie fizjo** → **Dla fizjoterapeuty** → **TODO** → **Źródła**.

## Ważne o AGV

Badań stricte o AGV jest bardzo mało i są stare (Hilgert 2004, Major 2007). Żadna znaleziona praca nie rozbija urazów na typy grindów. Duża część bazy to analogie ze skateboardingu, z ogólnej rehabilitacji kostki i ścięgien, oznaczone `[A]`.

## Do biuletynu: lista ekspertów

Kandydaci do recenzji treści i do kontaktu przy „pigułce wiedzy”/biuletynie dla fizjoterapeutów (szczegóły i źródła: `zasoby/specjalisci.md`, `zasoby/instagram.md`, materiały: `zasoby/blogi-i-artykuly.md`). Kontakt tylko przez kanały z ich publicznych stron.

- **AGV:** The Blading Physio (nazwisko nieznane; publikował 2020–2021) — jedyny znaleziony fizjo piszący stricte o AGV.
- **Polska:** Michał Popowski (Warszawa, AvePark; sporty ekstremalne, głównie BMX). Specjalisty od AGV/rolek w PL nie znaleziono.
- **Skateboarding (zagranica):** dr Kyle Brown (USA), Jeroen Stam i Alex Vos (Holandia), Ben Rowles (UK), Matti Hänninen (Finlandia).

TODO: ustalić, kto mógłby zrecenzować pliki `czesci-ciala/kostka/` i `przekrojowe/powrot-do-grindow.md`.

## Licencja

TODO: wybrać licencję treści (propozycja: CC BY-SA 4.0) i kodu strony (MIT).
