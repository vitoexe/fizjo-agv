# Strona statusu (GitHub Pages z `docs/`)

Odświeżanie (co godzinę, rutyna):

1. Pobierz zadania z Google Tasks, lista „Fizjo AGV” (`list_tasks`, `showCompleted=true`, `showHidden=true`), tylko odczyt; zapisz surowy JSON do pliku, np. `/tmp/tasks.json`.
2. `python3 tools/tasks_to_json.py /tmp/tasks.json` → `docs/status-data.json` (tytuł, pełne notatki, status, daty; bez id i linków API).
3. `python3 tools/build_status.py` → `docs/index.html` (gdy zmienił się tylko czas, plik nie jest nadpisywany).
4. Commit tylko gdy `git status --porcelain docs` coś pokazuje; przed pushem `git pull --rebase`.

Status „w toku” pokazuje się tylko, gdy tytuł zadania zawiera 🔄, ⏳, 🚧 albo „[w toku]”. Ukończone zadanie w Tasks = „zrobione”.

Pod tytułem każdego punktu strona pokazuje **pełne notatki (notes) z Tasks** (decyzja Tomasza, 2.11.2026): HTML jest escapowany, nowe linie i listy (`-`, `*`, `•`, `1.`) zachowane, URL-e klikalne. Gdy zadanie nie ma notatek, pokazuje się krótki opis zapasowy z `OPISY` w `build_status.py`. **Wszystko, co wpiszesz w notatkach zadań listy „Fizjo AGV”, staje się publiczne.**
