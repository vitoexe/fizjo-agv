#!/usr/bin/env python3
"""Generuje docs/index.html (publiczna strona planu i statusu Fizjo AGV).

Wejście: docs/status-data.json (z tools/tasks_to_json.py) + stan repo (pliki, sources.md, git log).
Wyjście: docs/index.html — jeden plik, inline CSS, bez zewnętrznych zależności.
Uruchom z dowolnego katalogu:  python3 tools/build_status.py
"""
import datetime as dt, html, json, pathlib, re, subprocess
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REPO = "https://github.com/vitoexe/fizjo-agv"
TZ = ZoneInfo("Europe/Warsaw")

# Zapasowe krótkie opisy (po numerze z tytułu) — używane tylko, gdy zadanie w Tasks nie ma notatek.
OPISY = {
    1: "Jedno miejsce, które zbiera i porządkuje wiedzę o fizjoterapii w AGV.",
    2: "Szeroki research z wielu narzędzi i modeli, weryfikowany w źródłach pierwotnych.",
    3: "Krótka „pigułka wiedzy” albo biuletyn dla fizjoterapeutów prowadzących rolkarzy AGV.",
    4: "Cała baza jest otwarta i dostępna dla społeczności.",
    5: "Strona, którą rolkarz może pokazać fizjoterapeucie lub trenerowi.",
    6: "Pierwszy research o grindach jako zalążek bazy.",
    7: "Najpierw uporządkowana baza (wg tematów i części ciała), potem strona.",
    8: "Mechanizm, dzięki któremu społeczność dodaje i weryfikuje treści.",
    9: "Metodologia: role narzędzi, etykiety, min. 2 niezależne źródła pierwotne.",
    10: "Przegląd blogów, kont na Instagramie i specjalistów od rolek i AGV.",
    11: "Ta strona: plan i status projektu, odświeżana automatycznie.",
    12: "Dwa filary: przygotowanie do grindów (główny) i rehabilitacja (mniejszy).",
}
W_TOKU = re.compile(r"(🔄|⏳|🚧|\[w toku\]|\(w toku\)|^w toku[:\s])", re.I)
SKIP_DIRS = {".git", "docs", "tools", "prompts", "research-raw", "_szablon"}


URL = re.compile(r"(https?://[^\s<>\"']+[^\s<>\"'.,;:!?)\]])")


def linkify(escaped):
    """Zamienia URL-e w już zescape'owanym tekście na klikalne linki."""
    return URL.sub(lambda m: f'<a href="{m.group(1)}" rel="nofollow noopener">{m.group(1)}</a>', escaped)


MARK = re.compile(r"^(✅|☑️|\[[xX]\]|🔄|⏳|🚧|⬜|☐|\[ \])\s*")
NAGLOWEK = re.compile(r"^[A-ZĄĆĘŁŃÓŚŹŻ][A-ZĄĆĘŁŃÓŚŹŻ0-9 ,./()+–-]{2,}:?$")
IKONA = {"done": "✅", "doing": "🔄", "todo": "⬜"}


def mark_status(m):
    """Znacznik na początku podpunktu -> (status, ikona do pokazania)."""
    if not m:
        return "todo", None
    z = m.group(1)
    if z in ("✅", "☑️") or z.lower() == "[x]":
        return "done", "✅"
    if z in ("🔄", "⏳", "🚧"):
        return "doing", z
    return "todo", "⬜"


def liscie(items):
    """Podpunkty liczone do postępu: element bez dzieci albo (rekurencyjnie) jego dzieci."""
    for it in items:
        if it["kids"]:
            yield from liscie(it["kids"])
        else:
            yield it


def status_z_dzieci(it):
    if it["kids"]:
        for k in it["kids"]:
            status_z_dzieci(k)
        if it["jawny"] is None:
            st = [k["st"] for k in it["kids"]]
            it["st"] = "done" if all(s == "done" for s in st) else ("todo" if all(s == "todo" for s in st) else "doing")


def parse_notes(text):
    """Notatki z Tasks -> lista bloków: ("h", tekst) | ("p", [linie]) | ("chk", [drzewo]) | ("ol", [linie]).

    Format: linie "- " to podpunkty checklisty (wcięcie co najmniej 2 spacje = pod-podpunkt);
    znacznik na początku: ✅ / [x] zrobione · 🔄 / ⏳ / 🚧 w toku · ⬜ / [ ] / brak — do zrobienia.
    Linia WERSALIKAMI (np. STATUS, DALEJ, ZASADA) = mały nagłówek. Reszta = akapity.
    """
    bloki, akapit = [], []
    stos = []  # [(wcięcie, element)]
    def flush():
        if akapit:
            bloki.append(("p", akapit[:])); akapit.clear()
    for raw in text.replace("\r\n", "\n").split("\n"):
        line = raw.rstrip().replace("\t", "    ")
        m_ul = re.match(r"^(\s*)[-*•]\s+(.*)$", line)
        m_ol = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if m_ul:
            flush()
            ind, body = len(m_ul.group(1)), m_ul.group(2)
            m = MARK.match(body)
            st, ikona = mark_status(m)
            it = dict(st=st, jawny=ikona, tekst=body[m.end():] if m else body, kids=[])
            if not bloki or bloki[-1][0] != "chk":
                bloki.append(("chk", [])); stos = []
            while stos and stos[-1][0] >= ind:
                stos.pop()
            (stos[-1][1]["kids"] if stos else bloki[-1][1]).append(it)
            stos.append((ind, it))
            continue
        stos = []
        if m_ol:
            flush()
            if not bloki or bloki[-1][0] != "ol":
                bloki.append(("ol", []))
            bloki[-1][1].append(m_ol.group(1))
        elif not line.strip():
            flush()
        elif NAGLOWEK.match(line.strip()):
            flush(); bloki.append(("h", line.strip().rstrip(":")))
        else:
            if bloki and bloki[-1][0] == "ol":
                bloki.append(("p", []))
            akapit.append(line.strip())
    flush()
    for typ, val in bloki:
        if typ == "chk":
            for it in val:
                status_z_dzieci(it)
    return bloki


def licz(bloki):
    c = dict(done=0, doing=0, todo=0)
    for typ, val in bloki:
        if typ == "chk":
            for it in liscie(val):
                c[it["st"]] += 1
    return c


def notes_html(bloki):
    esc = lambda s: linkify(html.escape(s))
    def drzewo(items):
        out = []
        for it in items:
            ik = it["jawny"] or IKONA[it["st"]]
            kids = ""
            if it["kids"]:
                c = dict(done=0, doing=0, todo=0)
                for x in liscie(it["kids"]):
                    c[x["st"]] += 1
                kids = f' <span class="cnt">{c["done"]}/{sum(c.values())}</span>' + drzewo(it["kids"])
            out.append(f'<li class="c-{it["st"]}"><span class="ic" aria-label="{ETYKIETY[it["st"]]}">{ik}</span>'
                       f'<span class="tx">{esc(it["tekst"])}</span>{kids}</li>')
        return '<ul class="chk">' + "".join(out) + "</ul>"
    out = []
    for typ, val in bloki:
        if typ == "h":
            out.append(f'<h4>{esc(val)}</h4>')
        elif typ == "p":
            if val:
                out.append("<p>" + "<br>".join(esc(x) for x in val) + "</p>")
        elif typ == "ol":
            out.append("<ol>" + "".join(f"<li>{esc(x)}</li>" for x in val) + "</ol>")
        else:
            out.append(drzewo(val))
    return "".join(out)


def mini_bar(c):
    tot = sum(c.values())
    if not tot:
        return ""
    pd, pg = 100 * c["done"] / tot, 100 * c["doing"] / tot
    return (f'<span class="mini" title="zrobione {c["done"]}, w toku {c["doing"]}, do zrobienia {c["todo"]}">'
            f'<span class="cnt">{c["done"]}/{tot}</span><span class="mb"><i style="width:{pd:.0f}%"></i>'
            f'<i class="g" style="width:{pg:.0f}%"></i></span></span>')


def git(*args):
    try:
        return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def stan_bazy():
    tematy = [p for d in ("filar-1-przygotowanie", "filar-2-rehabilitacja")
              for p in (ROOT / d).rglob("*.md") if p.name.lower() != "readme.md"]
    filary = {d: len([p for p in (ROOT / d).rglob("*.md") if p.name.lower() != "readme.md"])
              for d in ("filar-1-przygotowanie", "filar-2-rehabilitacja")}
    src = ROOT / "sources.md"
    zrodla = len(re.findall(r"^\| S\d+ \|", src.read_text(encoding="utf-8"), re.M)) if src.exists() else 0
    c = dict(twierdzenia=0, sprawdzone=0, do_sprawdzenia=0, dwa=0, jedno=0)
    item = re.compile(r"^\s*[-*] ")
    for d in ("filar-1-przygotowanie", "filar-2-rehabilitacja", "zasoby"):
        for p in (ROOT / d).rglob("*.md"):
            for line in p.read_text(encoding="utf-8").splitlines():
                if not item.match(line) or not re.search(r"\{[A-ZĄĆĘŁŃÓŚŹŻ]+", line):
                    continue
                c["twierdzenia"] += 1
                c["sprawdzone"] += "✔" in line
                c["do_sprawdzenia"] += "⏳" in line
                c["dwa"] += bool(re.search(r"(✔|⏳)\s*\**\s*2/2", line))
                c["jedno"] += bool(re.search(r"(✔|⏳)\s*\**\s*1/2", line))
    # ostatni commit w samej bazie (bez docs/ i tools/), żeby odświeżanie strony nie zmieniało liczb
    excl = ("--", ".", ":(exclude)docs", ":(exclude)tools")
    last = git("log", "-1", "--format=%cI", *excl)
    commit = git("log", "-1", "--format=%h", *excl)
    last_s = dt.datetime.fromisoformat(last).astimezone(TZ).strftime("%d.%m.%Y, %H:%M") if last else "—"
    return dict(tematy=len(tematy), filary=filary, zrodla=zrodla, last=last_s, commit=commit, **c)


def plan():
    data = json.loads((DOCS / "status-data.json").read_text(encoding="utf-8"))
    out = []
    for t in data.get("tasks", []):
        title = t.get("title", "").strip()
        m = re.match(r"^\s*((?:[^\w\s]\ufe0f?\s*)*)(\d+)\.\s*(.*)$", title)
        emo, nr, tekst = (m.group(1), int(m.group(2)), m.group(3)) if m else ("", 999, title)
        if t.get("status") == "completed" or "\u2705" in emo:
            st = "done"
        elif W_TOKU.search(emo) or W_TOKU.search(tekst):
            st = "doing"
        else:
            st = "todo"
        notes = (t.get("notes") or "").strip()
        bloki = parse_notes(notes) if notes else []
        out.append(dict(nr=nr, tytul=tekst, status=st, bloki=bloki, licz=licz(bloki), opis=OPISY.get(nr, "")))
    out.sort(key=lambda x: x["nr"])
    return out


ETYKIETY = {"done": "zrobione", "doing": "w toku", "todo": "do zrobienia"}

CSS = """
:root{--bg:#fafaf7;--fg:#1d1d1b;--mut:#5c5c57;--card:#fff;--line:#e3e2dc;--acc:#c2410c;
--done:#15803d;--doing:#b45309;--todo:#64748b;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--bg:#121212;--fg:#ececea;--mut:#a3a39e;--card:#1c1c1c;
--line:#2e2e2c;--acc:#fb923c;--done:#4ade80;--doing:#fbbf24;--todo:#94a3b8}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding:20px 16px 48px}
h1{font-size:1.9rem;margin:.2em 0 .1em}h2{font-size:1.2rem;margin:2em 0 .6em;border-bottom:1px solid var(--line);padding-bottom:.3em}
p{margin:.5em 0}a{color:var(--acc)}.mut{color:var(--mut);font-size:.92rem}
.warn{border-left:4px solid var(--acc);background:var(--card);padding:10px 14px;border-radius:6px;margin:14px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:10px 0}
.pill{display:inline-block;font-size:.78rem;font-weight:600;padding:2px 9px;border-radius:99px;border:1px solid currentColor;white-space:nowrap}
.done{color:var(--done)}.doing{color:var(--doing)}.todo{color:var(--todo)}
ol.plan{list-style:none;padding:0;margin:0}ol.plan li{display:flex;gap:10px;align-items:flex-start;
background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin:8px 0}
.nr{font-weight:700;min-width:1.8em;color:var(--mut)}.body{flex:1}.t{font-weight:600}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}@media(min-width:600px){.grid{grid-template-columns:repeat(3,1fr)}}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px}
.stat b{display:block;font-size:1.6rem}.stat span{color:var(--mut);font-size:.88rem}
.bar{height:10px;border-radius:99px;background:var(--line);overflow:hidden;margin:8px 0}.bar i{display:block;height:100%;background:var(--done)}
code{font-size:.88em;background:var(--line);padding:1px 5px;border-radius:4px}
ul{padding-left:1.2em}li{margin:.25em 0}
.notes{font-size:.93rem;color:var(--mut);margin-top:4px;overflow-wrap:anywhere}.notes p{margin:.35em 0}
.notes ul,.notes ol{margin:.3em 0;padding-left:1.3em}ol.plan .notes li{display:list-item;background:none;border:0;padding:0;margin:.15em 0}
.notes h4{font-size:.74rem;letter-spacing:.06em;color:var(--fg);margin:.9em 0 .2em;font-weight:700}
ol.plan .notes ul.chk{list-style:none;padding-left:0}ol.plan .notes ul.chk ul.chk{padding-left:1.5em}
ol.plan .notes ul.chk li{display:block;position:relative;padding-left:1.6em;margin:.3em 0}
.notes .ic{position:absolute;left:0;top:0;font-size:.95em}.notes .c-done>.tx{color:var(--mut)}
.notes .c-doing>.tx{color:var(--fg)}.notes .c-todo>.tx{color:var(--fg)}
.cnt{font-size:.78rem;font-weight:600;color:var(--mut);font-variant-numeric:tabular-nums}
.row{margin:3px 0 2px}.mini{display:inline-flex;align-items:center;gap:6px}
.mb{display:inline-flex;width:90px;height:6px;border-radius:99px;background:var(--line);overflow:hidden}
.mb i{display:block;height:100%;background:var(--done)}.mb i.g{background:var(--doing);opacity:.7}
details{margin-top:4px}summary{cursor:pointer;font-size:.85rem;color:var(--mut);padding:2px 0}footer{margin-top:3em;color:var(--mut);font-size:.85rem}
"""


def render():
    s, p = stan_bazy(), plan()
    e = html.escape
    now = dt.datetime.now(TZ).strftime("%d.%m.%Y, %H:%M")
    n = {k: sum(1 for x in p if x["status"] == k) for k in ETYKIETY}
    pod = {k: sum(x["licz"][k] for x in p) for k in ETYKIETY}
    pod_all = sum(pod.values())
    def ulamek(x):  # punkt zrobiony = 1; inaczej udział zrobionych podpunktów (0, gdy brak checklisty)
        tot = sum(x["licz"].values())
        return 1.0 if x["status"] == "done" else (x["licz"]["done"] / tot if tot else 0.0)
    pct = round(100 * sum(ulamek(x) for x in p) / len(p)) if p else 0
    def item(x):
        tot = sum(x["licz"].values())
        head = f'<div class="t">{e(x["tytul"])}</div>' + (f'<div class="row">{mini_bar(x["licz"])}</div>' if tot else "")
        if x["bloki"]:
            otw = "" if x["status"] == "done" else " open"
            sumtxt = f"Szczegóły · {x['licz']['done']}/{tot} podpunktów" if tot else "Szczegóły"
            body = f'<details{otw}><summary>{sumtxt}</summary><div class="notes">{notes_html(x["bloki"])}</div></details>'
        else:
            body = f'<div class="mut">{e(x["opis"])}</div>' if x["opis"] else ""
        return (f'<li><span class="nr">{x["nr"]}.</span><div class="body">{head}{body}</div>'
                f'<span class="pill {x["status"]}">{ETYKIETY[x["status"]]}</span></li>')
    items = "\n".join(item(x) for x in p)
    stat = lambda v, l: f'<div class="stat"><b>{v}</b><span>{l}</span></div>'
    f = lambda path: f"{REPO}/blob/main/{path}"
    return f"""<!doctype html>
<html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fizjo AGV — plan i status</title>
<meta name="description" content="Otwarta baza wiedzy o przygotowaniu ciała do grindów i fizjoterapii w jeździe na rolkach agresywnych (AGV). Plan i status projektu.">
<style>{CSS}</style></head><body><main>
<h1>Fizjo AGV</h1>
<p class="mut">Plan i status projektu · ostatnia aktualizacja: <b>{now}</b> (czas warszawski)</p>

<h2>O projekcie</h2>
<p>Otwarta (open source) baza wiedzy o przygotowaniu ciała do jazdy na rolkach agresywnych (aggressive inline, AGV) i o fizjoterapii po urazach. Dla rolkarzy oraz dla fizjoterapeutów i trenerów, którzy prowadzą zawodnika AGV.</p>
<div class="card"><b>Filar 1 — przygotowanie do grindów</b> <span class="pill done">główny</span>
<p>Anatomicznie prawidłowa pozycja przy grindach, wzmacnianie, stabilizacja i propriocepcja, mobilność, rozgrzewka, obciążenie, prewencja.</p></div>
<div class="card"><b>Filar 2 — rehabilitacja</b> <span class="pill todo">mniejszy</span>
<p>Urazy według części ciała i powrót do grindów po urazie.</p></div>
<div class="warn"><b>To nie jest diagnoza ani porada medyczna.</b> Baza zbiera i porządkuje źródła; nie zastępuje badania przez lekarza ani fizjoterapeutę. Treści nie przeszły jeszcze recenzji fizjoterapeuty.</div>

<h2>Plan</h2>
<p class="mut">Punkty: zrobione {n["done"]} · w toku {n["doing"]} · do zrobienia {n["todo"]} (z {len(p)})<br>
Podpunkty: zrobione {pod["done"]} · w toku {pod["doing"]} · do zrobienia {pod["todo"]} (z {pod_all}) · postęp łącznie: <b>{pct}%</b></p>
<div class="bar" aria-label="postęp {pct}%"><i style="width:{pct}%"></i></div>
<p class="mut">Postęp łącznie: punkt zrobiony liczy się w całości, punkt w toku — według udziału zrobionych podpunktów.</p>
<ol class="plan">
{items}
</ol>

<h2>Stan bazy</h2>
<div class="grid">
{stat(s["tematy"], "plików tematów")}
{stat(s["zrodla"], "źródeł w bibliografii")}
{stat(s["twierdzenia"], "twierdzeń z etykietą")}
{stat(s["sprawdzone"], "sprawdzonych w źródle ✔")}
{stat(s["do_sprawdzenia"], "do sprawdzenia ⏳")}
{stat(s["dwa"], "potwierdzonych 2/2")}
</div>
<p class="mut">Filar 1: {s["filary"]["filar-1-przygotowanie"]} plików, filar 2: {s["filary"]["filar-2-rehabilitacja"]} plików. Z 1 źródłem (1/2): {s["jedno"]}. Ostatnia zmiana w bazie: {s["last"]} (commit <code>{e(s["commit"])}</code>).</p>

<h2>Metodologia w skrócie</h2>
<ul>
<li>Każde twierdzenie ma źródło i etykietę: <b>dowód</b> (badanie), <b>konsensus</b> (stanowisko ekspertów, protokół), <b>wnioskowanie</b> (biomechaniczne), <b>analogia</b> (inny sport), <b>spekulacja</b>, <b>opinia</b> (praktyk, blog, social media).</li>
<li>Pełne potwierdzenie (<b>2/2</b>) wymaga co najmniej 2 niezależnych źródeł pierwotnych. Badanie i jego cytowanie to wciąż jedno źródło.</li>
<li>✔ oznacza sprawdzone w źródle, ⏳ czeka na weryfikację.</li>
<li>Modele AI to narzędzia do szukania i syntezy, a nie źródła.</li>
</ul>

<h2>Linki</h2>
<ul>
<li><a href="{REPO}">Repozytorium na GitHubie</a> · <a href="{f('README.md')}">README</a></li>
<li><a href="{f('METHODOLOGY.md')}">Metodologia</a> · <a href="{f('CONTRIBUTING.md')}">Jak dołożyć wiedzę</a> · <a href="{f('sources.md')}">Bibliografia</a></li>
<li><a href="{REPO}/tree/main/filar-1-przygotowanie">Filar 1: przygotowanie</a> · <a href="{REPO}/tree/main/filar-1-przygotowanie/pozycja-przy-grindach">Pozycja przy grindach</a></li>
<li><a href="{REPO}/tree/main/filar-2-rehabilitacja">Filar 2: rehabilitacja</a> · <a href="{REPO}/tree/main/zasoby">Zasoby (blogi, specjaliści)</a></li>
</ul>
<footer>Fizjo AGV · open source · strona generowana automatycznie z listy zadań projektu i stanu repozytorium.</footer>
</main></body></html>
"""


if __name__ == "__main__":
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").touch()
    out, new = DOCS / "index.html", render()
    strip = lambda t: re.sub(r"ostatnia aktualizacja: <b>[^<]*</b>", "", t)
    if out.exists() and strip(out.read_text(encoding="utf-8")) == strip(new):
        print("index.html bez zmian (pominięto sam czas)")
    else:
        out.write_text(new, encoding="utf-8")
        print("zapisano", out)
