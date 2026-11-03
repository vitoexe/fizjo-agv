# Status projektu → `STATUS.md`

Od 3.11.2026 (decyzja Tomasza) status projektu jest w pliku [`STATUS.md`](../STATUS.md) w katalogu głównym repo. Dawna strona GitHub Pages (`docs/`) jest wycofana: `docs/index.html` tylko przekierowuje do `STATUS.md`, stary generator `build_status.py` usunięty (jest w historii git). Wyłączenie Pages w ustawieniach repo to decyzja Tomasza.

Jedyne źródło prawdy: Google Tasks, lista „Fizjo AGV”. **Wszystko, co wpiszesz w notatkach zadań tej listy, staje się publiczne.**

Odświeżanie:

1. Pobierz zadania z Google Tasks, lista „Fizjo AGV” (`list_tasks`, `showCompleted=true`, `showHidden=true`), tylko odczyt; zapisz surowy JSON do pliku, np. `/tmp/tasks.json`.
2. `python3 tools/tasks_to_json.py /tmp/tasks.json` → `tools/status-data.json` (tytuł, pełne notatki, status, daty; bez id i linków API).
3. `python3 tools/build_status_md.py` → `STATUS.md` oraz blok statusu w `README.md` między `<!-- STATUS:START -->` i `<!-- STATUS:END -->` (pasek łączny, tabela 13 punktów, data, link do STATUS.md; reszta README bez zmian). Gdy zmieniła się tylko data, pliki nie są nadpisywane. Znaczników w README nie usuwaj.
4. Commit tylko gdy `git status --porcelain STATUS.md README.md tools/status-data.json` coś pokazuje; przed pushem `git pull --rebase`.

Status punktu (ikona przy nazwie) pochodzi z tytułu zadania: ✅ zrobione, 🔄 / ⏳ / 🚧 / „[w toku]” w toku, brak — do zrobienia; ukończone zadanie w Tasks = zrobione.

Postęp punktu (pasek 10 pól 🟩/🟨/⬜ + %): z podpunktów checklisty w notatkach — ✅ = 1, 🔄 = 0,5, ⬜ / ⏸️ / brak = 0 (liczone najniższe poziomy listy). Punkt bez podpunktów: ✅ = 100%, 🔄 = 50%, inaczej 0%. Postęp łączny = średnia punktów.

## Format notatek w Tasks (checklista)

Notatki zadania są parsowane przez `build_status_md.py` i pokazywane w `STATUS.md` w sekcji „Szczegóły” pod paskiem punktu:

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
- Znacznik statusu na początku podpunktu: `✅` lub `[x]` = zrobione; `🔄`, `⏳`, `🚧` = w toku; `⏸️` / `⏸` = wstrzymane (liczone jak 0); `⬜`, `[ ]` albo brak znacznika = do zrobienia.
- Podpunkt z pod-podpunktami bez własnego znacznika dostaje status wyliczony z dzieci (wszystkie ✅ → zrobione, żadne → do zrobienia, inaczej w toku).
- Linia napisana WERSALIKAMI w osobnej linii (np. `STATUS`, `DALEJ`, `ZASADA`, `DECYZJE 2.11.2026`) = mały nagłówek sekcji; dwukropek na końcu jest pomijany.
- Linie `1. …` bez myślnika = zwykła lista numerowana (nie liczy się do postępu). Pozostały tekst = akapity (Markdown; GitHub sam robi linki z URL-i).
- Pasek punktu i % liczą **liście** checklisty: podpunkt bez dzieci albo pod-podpunkty (rodzic z dziećmi nie jest liczony osobno); ✅ = 1, 🔄 = 0,5, ⬜/⏸️ = 0. W pasku: 🟩 zrobione, 🟨 w toku, ⬜ reszta.
- Postęp łączny: średnia procentów wszystkich punktów (punkt bez checklisty: ✅ = 100%, 🔄 = 50%, inaczej 0%).
- Status samego punktu nadal pochodzi z tytułu (✅ / 🔄 …) albo statusu „completed” w Tasks — podpunkty go nie zmieniają.
