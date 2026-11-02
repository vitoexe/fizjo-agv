# Strona statusu (GitHub Pages z `docs/`)

Odświeżanie (co godzinę, rutyna):

1. Pobierz zadania z Google Tasks, lista „Fizjo AGV” (`list_tasks`, `showCompleted=true`, `showHidden=true`), tylko odczyt; zapisz surowy JSON do pliku, np. `/tmp/tasks.json`.
2. `python3 tools/tasks_to_json.py /tmp/tasks.json` → `docs/status-data.json` (bez notatek, id i linków).
3. `python3 tools/build_status.py` → `docs/index.html` (gdy zmienił się tylko czas, plik nie jest nadpisywany).
4. Commit tylko gdy `git status --porcelain docs` coś pokazuje; przed pushem `git pull --rebase`.

Status „w toku” pokazuje się tylko, gdy tytuł zadania zawiera 🔄, ⏳, 🚧 albo „[w toku]”. Ukończone zadanie w Tasks = „zrobione”.
