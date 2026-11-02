# Jak dodawać i weryfikować treści

Najpierw przeczytaj `METHODOLOGY.md` (narzędzia, zasada 2 źródeł, etykiety).

## Zasady twarde

1. **Każde twierdzenie ma źródło z linkiem.** Na końcu zdania znacznik `[Sxx]` z `sources.md`. Nowe źródło dopisz do `sources.md` z typem i linkiem (preferuj DOI/PubMed).
2. **Min. 2 niezależne źródła pierwotne**, żeby twierdzenie było przyjęte (`2/2`). Dwa modele AI powtarzające to samo to nie dwa źródła. Twierdzenie z jednym źródłem może wejść jako `1/2`, ale plik nie dostanie statusu `zweryfikowany`.
3. **AI to narzędzie, nie źródło.** Nigdy nie cytuj „wg Gemini/Claude/ChatGPT”. Cytuj badanie/stronę, które model znalazł — po otwarciu i sprawdzeniu.
4. **Każde twierdzenie ma etykietę**: `{DOWÓD:przegląd|RCT|obserwacyjne}`, `{KONSENSUS}`, `{WNIOSKOWANIE}`, `{ANALOGIA:...}`, `{SPEKULACJA}`, rozszerzenia `{OPINIA}`, `{PROPOZYCJA}` (opis w README).
5. **Nie wymyślaj liczb.** Liczba musi być w cytowanym źródle. Czytałeś tylko abstrakt → ✔ tylko dla tego, co jest w abstrakcie; resztę ⏳.
6. **Oddziel dowody od domysłów.** `{DOWÓD}` i `{KONSENSUS}` tylko w „Co wiemy z badań”; `{WNIOSKOWANIE}`/`{SPEKULACJA}` w „Wnioskowanie biomechaniczne”; `{OPINIA}` w „Praktyka i opinie fizjo”.
7. **Analogie oznaczaj `{ANALOGIA:dyscyplina/populacja}`.**
8. **Żadnych historii konkretnych osób** ani danych zdrowotnych bez zgody.
9. **Link musi działać.** `curl -sIL -o /dev/null -w '%{http_code}' URL`: 404 = nie dodajemy; 403/timeout (blokada botów) = uwaga w `sources.md` + sprawdzenie w przeglądarce.

## Jak dodać temat

1. Skopiuj `_szablon/temat.md` do właściwego katalogu.
2. Wypełnij frontmatter (`status: szkic`).
3. Braki zostaw jako `TODO` z listą pytań do researchu — to też wkład.
4. Pull request: co dodano, jakie źródła, czy czytałeś pełny tekst, którym narzędziem szukałeś (dla śladu, nie jako źródło).

## Review (zasada dwóch osób)

- Każda zmiana merytoryczna wymaga **review drugiej osoby** (nie autora).
- Status `zweryfikowany` wymaga review **fizjoterapeuty lub lekarza** (`recenzent:` we frontmatter), który sprawdził źródła w pełnym tekście, i 2/2 dla kluczowych twierdzeń.
- Recenzent sprawdza: czy źródło mówi to, co napisano; czy etykieta jest właściwa; czy analogia/wnioskowanie są oznaczone; czy link działa; czy źródła są naprawdę niezależne.
- Statusy: `szkic` → `do-review` → `zweryfikowany`. Istotna zmiana treści cofa do `do-review`.

## Spory

Gdy źródła sobie przeczą, nie wybieramy zwycięzcy — opisujemy obie strony z etykietami. Nierozstrzygnięte sprzeczności idą do `prompts/batch-1/argon-sprzecznosci-szablon.md`.
