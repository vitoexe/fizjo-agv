#!/usr/bin/env python3
"""Generuje STATUS.md (katalog główny repo) z JSON-a od tools/tasks_to_json.py.

Jedyne źródło prawdy: Google Tasks, lista „Fizjo AGV”. Notatki zadań są publiczne.

Użycie:  python3 tools/build_status_md.py [tools/status-data.json] [STATUS.md]

Postęp punktu liczony z podpunktów checklisty w notatkach (liście drzewa):
✅ = 1, 🔄/⏳/🚧 = 0,5, ⬜/⏸/brak znacznika = 0. Punkt bez podpunktów: 100% gdy tytuł ma ✅
(albo zadanie jest ukończone w Tasks), 50% gdy 🔄, inaczej 0%. Postęp łączny = średnia punktów.
"""
import datetime as dt, json, pathlib, re, sys
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "tools" / "status-data.json"
DST = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "STATUS.md"

MARK = re.compile(r"^(✅|☑️|\[[xX]\]|🔄|⏳|🚧|⬜|☐|\[ \]|⏸️?)\s*")
NAGLOWEK = re.compile(r"^[A-ZĄĆĘŁŃÓŚŹŻ][A-ZĄĆĘŁŃÓŚŹŻ0-9 ,./()+–-]{2,}:?$")
W_TOKU = re.compile(r"(🔄|⏳|🚧|\[w toku\])", re.I)
IKONA = {"done": "✅", "doing": "🔄", "todo": "⬜", "paused": "⏸️"}
WAGA = {"done": 1.0, "doing": 0.5, "todo": 0.0, "paused": 0.0}


def znacznik(z):
    if z is None:
        return None
    if z in ("✅", "☑️") or z.lower() == "[x]":
        return "done"
    if z in ("🔄", "⏳", "🚧"):
        return "doing"
    if z.startswith("⏸"):
        return "paused"
    return "todo"


def parse(notes):
    """-> lista bloków ("h", tekst) | ("p", tekst) | ("li", drzewo) | ("ol", tekst)."""
    bloki, stos = [], []
    for raw in (notes or "").replace("\r\n", "\n").split("\n"):
        line = raw.rstrip().replace("\t", "    ")
        m_ul = re.match(r"^(\s*)[-*•]\s+(.*)$", line)
        if m_ul:
            ind, body = len(m_ul.group(1)), m_ul.group(2)
            m = MARK.match(body)
            it = dict(jawny=znacznik(m.group(1)) if m else None,
                      tekst=body[m.end():] if m else body, kids=[])
            if not bloki or bloki[-1][0] != "li":
                bloki.append(("li", [])); stos = []
            while stos and stos[-1][0] >= ind:
                stos.pop()
            (stos[-1][1]["kids"] if stos else bloki[-1][1]).append(it)
            stos.append((ind, it))
            continue
        stos = []
        s = line.strip()
        if not s:
            continue
        if re.match(r"^\d+[.)]\s+", s):
            bloki.append(("ol", s))
        elif NAGLOWEK.match(s):
            bloki.append(("h", s.rstrip(":")))
        else:
            bloki.append(("p", s))
    for typ, val in bloki:
        if typ == "li":
            for it in val:
                ustal(it)
    return bloki


def ustal(it):
    for k in it["kids"]:
        ustal(k)
    if it["jawny"]:
        it["st"] = it["jawny"]
    elif it["kids"]:
        st = [k["st"] for k in it["kids"]]
        it["st"] = "done" if all(s == "done" for s in st) else (
            "todo" if all(s in ("todo", "paused") for s in st) else "doing")
    else:
        it["st"] = "todo"


def liscie(items):
    for it in items:
        if it["kids"]:
            yield from liscie(it["kids"])
        else:
            yield it


def status_tytulu(t):
    if t.get("status") == "completed" or t["title"].lstrip().startswith("✅"):
        return "done"
    if W_TOKU.search(t["title"]):
        return "doing"
    return "todo"


def udzialy(t, bloki):
    """-> (udział zrobionych, udział w toku, liczba podpunktów) w skali 0–1."""
    ls = [l for typ, v in bloki if typ == "li" for l in liscie(v)]
    if not ls:
        st = status_tytulu(t)
        return (1.0, 0.0, 0) if st == "done" else ((0.0, 1.0, 0) if st == "doing" else (0.0, 0.0, 0))
    n = len(ls)
    return (sum(l["st"] == "done" for l in ls) / n, sum(l["st"] == "doing" for l in ls) / n, n)


def pasek(done, doing):
    z = round(done * 10)
    y = min(10, round((done + doing) * 10)) - z
    return "🟩" * z + "🟨" * y + "⬜" * (10 - z - y)


def procent(done, doing):
    return round(100 * (done + 0.5 * doing))


def numer(t):
    m = re.search(r"(\d+)\.", t["title"])
    return int(m.group(1)) if m else 999


def czysty_tytul(t):
    return re.sub(r"^\s*(✅|🔄|⏳|🚧|⬜|\[w toku\])\s*", "", t["title"]).strip()


def md_esc(s):
    return s.replace("|", "\\|")


def drzewo(items, poziom=0):
    out = []
    for it in items:
        out.append("  " * poziom + f"- {IKONA[it['st']]} {it['tekst']}")
        out.extend(drzewo(it["kids"], poziom + 1))
    return out


def render(tasks):
    wiersze, sekcje, sum_d, sum_y = [], [], 0.0, 0.0
    for t in sorted(tasks, key=numer):
        bloki = parse(t.get("notes", ""))
        d, y, n = udzialy(t, bloki)
        sum_d += d; sum_y += y
        ik = IKONA[status_tytulu(t)]
        tyt = czysty_tytul(t)
        pod = f"{n} podp." if n else "—"
        wiersze.append(f"| {ik} | [{md_esc(tyt)}](#{kotwica(tyt)}) | {pasek(d, y)} | {procent(d, y)}% | {pod} |")
        sek = [f"### {ik} {tyt}", "", f"`{pasek(d, y)}` **{procent(d, y)}%**", ""]
        for typ, val in bloki:
            if typ == "h":
                sek += [f"**{val.capitalize()}**", ""]
            elif typ == "p":
                sek += [val, ""]
            elif typ == "ol":
                sek += [val, ""]
            else:
                sek += drzewo(val) + [""]
        sekcje.append("\n".join(sek).rstrip() + "\n")
    k = len(tasks) or 1
    D, Y = sum_d / k, sum_y / k
    teraz = dt.datetime.now(ZoneInfo("Europe/Warsaw")).strftime("%Y-%m-%d %H:%M")
    head = [
        "# Status projektu Fizjo AGV",
        "",
        f"Ostatnia aktualizacja: {teraz} (czas warszawski). Źródło: Google Tasks, lista „Fizjo AGV” — plik generowany przez `tools/build_status_md.py`, nie edytuj ręcznie.",
        "",
        f"**Postęp łącznie:** `{pasek(D, Y)}` **{procent(D, Y)}%** ({len(tasks)} punktów planu)",
        "",
        "| | Punkt planu | Postęp | % | Podpunkty |",
        "|---|---|---|---|---|",
        *wiersze,
        "",
        "## Szczegóły",
        "",
    ]
    legenda = [
        "## Legenda",
        "",
        "- ✅ zrobione · 🔄 w toku · ⬜ do zrobienia · ⏸️ wstrzymane (liczone jak 0)",
        "- Pasek (10 pól): 🟩 zrobione · 🟨 w toku · ⬜ do zrobienia",
        "- Procent punktu: podpunkty z notatek w Tasks (✅ = 1, 🔄 = 0,5, ⬜/⏸️ = 0; liczone są najniższe poziomy listy). Punkt bez podpunktów: ✅ = 100%, 🔄 = 50%, inaczej 0%.",
        "- Procent łączny: średnia procentów wszystkich punktów.",
        "- Status punktu (ikona przy nazwie) pochodzi z tytułu zadania w Tasks.",
        "",
    ]
    return "\n".join(head) + "\n" + "\n".join(sekcje) + "\n" + "\n".join(legenda)


def kotwica(tyt):
    # przybliżenie kotwic GitHuba: małe litery, bez interpunkcji, spacje -> "-"
    s = tyt.lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return "-" + s.replace(" ", "-")  # nagłówek zaczyna się od emoji -> GitHub daje wiodący "-"


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    nowy = render(data["tasks"])
    bez_daty = lambda s: re.sub(r"^Ostatnia aktualizacja: .*$", "", s, flags=re.M)
    if DST.exists() and bez_daty(DST.read_text(encoding="utf-8")) == bez_daty(nowy):
        print("STATUS.md bez zmian")
        return
    DST.write_text(nowy, encoding="utf-8")
    print(f"zapisano {DST}")


if __name__ == "__main__":
    main()
