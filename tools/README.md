# Strona statusu (GitHub Pages z `docs/`)

Odświeżanie (co godzinę, rutyna):

1. Pobierz zadania z Google Tasks, lista „Fizjo AGV” (`list_tasks`, `showCompleted=true`, `showHidden=true`), tylko odczyt; zapisz surowy JSON do pliku, np. `/tmp/tasks.json`.
2. `python3 tools/tasks_to_json.py /tmp/tasks.json` → `docs/status-data.json` (tytuł, pełne notatki, status, daty; bez id i linków API).
3. `python3 tools/build_status.py` → `docs/index.html` (gdy zmienił się tylko czas, plik nie jest nadpisywany).
4. Commit tylko gdy `git status --porcelain docs` coś pokazuje; przed pushem `git pull --rebase`.

Status „w toku” pokazuje się tylko, gdy tytuł zadania zawiera 🔄, ⏳, 🚧 albo „[w toku]”. Ukończone zadanie w Tasks = „zrobione”.

Pod tytułem każdego punktu strona pokazuje **pełne notatki (notes) z Tasks** (decyzja Tomasza, 2.11.2026): HTML jest escapowany, nowe linie i listy (`-`, `*`, `•`, `1.`) zachowane, URL-e klikalne. Gdy zadanie nie ma notatek, pokazuje się krótki opis zapasowy z `OPISY` w `build_status.py`. **Wszystko, co wpiszesz w notatkach zadań listy „Fizjo AGV”, staje się publiczne.**

## Format notatek w Tasks (checklista)

Notatki zadania są parsowane przez `build_status.py` i renderowane w rozwijanym bloku „Szczegóły” (otwarty dla punktów w toku i do zrobienia, zwinięty dla zrobionych):

```
Krótki opis punktu (zwykły tekst = akapit).

STATUS
- ✅ Krok zrobiony
- 🔄 Krok w toku
  - ✅ Pod-podpunkt zrobiony (wcięcie min. 2 spacje)
  - ⬜ Pod-podpunkt do zrobienia
- ⬜ Krok do zrobienia

ZASADA
Zwykły tekst pod nagłówkiem.
```

- Linia zaczynająca się od `- ` (także `* `, `• `) = podpunkt checklisty; wcięcie (co najmniej 2 spacje względem rodzica) = pod-podpunkt.
- Znacznik statusu na początku podpunktu: `✅` lub `[x]` = zrobione; `🔄`, `⏳`, `🚧` = w toku; `⬜`, `[ ]` albo brak znacznika = do zrobienia.
- Podpunkt z pod-podpunktami bez własnego znacznika dostaje status wyliczony z dzieci (wszystkie ✅ → zrobione, żadne → do zrobienia, inaczej w toku).
- Linia napisana WERSALIKAMI w osobnej linii (np. `STATUS`, `DALEJ`, `ZASADA`, `DECYZJE 2.11.2026`) = mały nagłówek sekcji; dwukropek na końcu jest pomijany.
- Linie `1. …` bez myślnika = zwykła lista numerowana (nie liczy się do postępu). Pozostały tekst = akapity; URL-e są klikalne, HTML jest escapowany.
- Licznik przy punkcie (np. `3/7`) i mały pasek liczą **liście** checklisty: podpunkt bez dzieci albo pod-podpunkty (rodzic z dziećmi nie jest liczony osobno). Zielony = zrobione, pomarańczowy = w toku.
- Pasek ogólny „postęp łącznie”: punkt oznaczony jako zrobiony liczy się jako 100%; pozostałe punkty — jako udział zrobionych podpunktów (punkt bez checklisty = 0%); wynik to średnia ze wszystkich punktów. Obok liczby punktów i podpunktów wg statusu.
- Status samego punktu nadal pochodzi z tytułu (✅ / 🔄 …) albo statusu „completed” w Tasks — podpunkty go nie zmieniają.
