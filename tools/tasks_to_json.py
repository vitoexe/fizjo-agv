#!/usr/bin/env python3
"""Zamienia surowy wynik list_tasks (Google Tasks, JSON) na docs/status-data.json.

Zapisuje TYLKO tytuł, status, daty i pozycję. Notatki (notes), id i linki są pomijane,
bo strona jest publiczna.

Użycie:  python3 tools/tasks_to_json.py surowe_tasks.json [docs/status-data.json]
"""
import json, re, sys, pathlib

def main():
    src = pathlib.Path(sys.argv[1])
    dst = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else
                       pathlib.Path(__file__).resolve().parent.parent / "docs" / "status-data.json")
    text = src.read_text(encoding="utf-8")
    # toleruj otoczkę wokół JSON-a: weź od pierwszego '[' do ostatniego ']'
    m = re.search(r"\[.*\]", text, re.S)
    raw = json.loads(m.group(0) if m else text)
    if isinstance(raw, dict):
        raw = raw.get("items", [])
    tasks = []
    for t in raw:
        if t.get("deleted") or t.get("parent"):
            continue
        tasks.append({k: t[k] for k in ("title", "status", "updated", "completed", "due", "position") if k in t})
    out = {"source": "Google Tasks: lista „Fizjo AGV” (tylko tytuły i statusy)", "tasks": tasks}
    new = json.dumps(out, ensure_ascii=False, indent=2) + "\n"
    if dst.exists() and dst.read_text(encoding="utf-8") == new:
        print("status-data.json bez zmian")
        return
    dst.write_text(new, encoding="utf-8")
    print(f"zapisano {dst} ({len(tasks)} zadań)")

if __name__ == "__main__":
    main()
