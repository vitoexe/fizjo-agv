# Claude/Opus — red-team całej bazy po E, F, G, Argon 1 i Argon 2 — część 2 (1b)

Ustawienia: claude.ai, model **Claude Opus** (najnowszy dostępny), włączone **Web search** (i przeglądanie/fetch URL), **Extended thinking: ON**. Nowa rozmowa na każdą część. Wklej blok poniżej w całości. Jeśli Claude nie otworzy któregoś linku raw, wklej treść pliku ręcznie pod promptem.

Baza jest za duża na jeden kontekst, dlatego są 2 części: `claude-redteam-1a.md` (stabilizacja, wzmacnianie, prewencja, pozycja, wzorce urazów, propozycje) i `claude-redteam-1b.md` (obciążenie, rozgrzewka, technika upadania, mobilność, filar 2: wstrząśnienie, nadgarstek). Wynik zapisujemy do `research-raw/` i weryfikujemy jak Argona (PMID/DOI, niezależność grup).

```
Act as a sceptical sports-medicine reviewer, biomechanist and research methodologist. Your job is to ATTACK this knowledge base (red-team), not to improve its prose.

CONTEXT: "Fizjo AGV" is an open-source, Polish-language, evidence-graded knowledge base for aggressive inline skaters (AGV), physiotherapists and coaches. Pillar 1 (main): preparing the body for grinds and landings — body position, strength, stability, proprioception, mobility, warm-up, load management, prevention. Pillar 2 (secondary): rehabilitation. The author is not a clinician; that is why labels, the rule of 2 independent sources (METHODOLOGY.md) and external review matter. Almost no AGV-specific research exists (S01 Hilgert 2004, n=66; S02 Major 2007, n=10), so most claims are transferred from other sports.

THIS IS PART 2 OF 2 (obciążenie i periodyzacja, rozgrzewka, technika upadania, mobilność, wstrząśnienie mózgu, nadgarstek). Scope: the files listed below. In propozycje-do-recenzji.md attack only the section "Prewencja i periodyzacja sesji (Deep Research G)". Concussion (wstrzasnienie.md) and wrist injuries are safety-critical: check red flags and return-to-skate steps against current consensus (e.g. Amsterdam 2022 statement) and say what is missing. Ignore files not listed (part 1 covers them).

Read these files first (public, raw Markdown). Use your web fetch / browsing tool on each URL:
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/METHODOLOGY.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/sources.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/obciazenie-i-periodyzacja.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/rozgrzewka.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/technika-upadania.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/mobilnosc.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/czesci-ciala/glowa/wstrzasnienie.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-2-rehabilitacja/czesci-ciala/nadgarstek-reka/urazy.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/propozycje-do-recenzji.md

Supporting raw model outputs and our verification tables (read the "Weryfikacja" sections at the end if you need to know what we already checked; do NOT treat the model text in them as a source):
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/research-raw/2026-11-02-G-gemini-deep-research.md

WHAT TO ATTACK (in this order)
1. Every claim marked 2/2: are the two (or more) sources really from INDEPENDENT research groups (check authors and senior authors; same lab, same consortium, a review that includes the other primary study = not independent)? Is each number actually in the cited source? Do the sources measure the same outcome as the claim?
2. Claims marked 1/2 and ⏳: overstated? wrong direction of effect (e.g. "increased" vs "decreased", protective vs risk)? wrong population?
3. Labels: should a {DOWÓD:...} be {ANALOGIA:...}, {WNIOSKOWANIE} or {SPEKULACJA}? Is lab biomechanics (drop landings, team sports, skateboarding, parkour, dance) presented as if it were AGV data? Is the transfer to AGV justified (hard boots restricting the ankle, grinding on ledges/rails, sliding falls, mostly teenage skaters)?
4. propozycje-do-recenzji.md: practical recommendations that go beyond the evidence, or could be unsafe for a teenager or a returning skater.
5. Safety-critical gaps: missing red flags, missing "see a professional" criteria, missing contraindications, missing evidence that would change a recommendation.
6. Internal contradictions between files (the same topic stated differently in two files, or the same source cited with different numbers/labels).

Already known and fixed (do not re-report unless still wrong in the files): wrong PMIDs from Argon 1 (Bathe, Wang, Cronström 2020, Sugimoto), wrong DOI of Lagouvardou 2026 (now 10.1016/j.jbmt.2025.11.019), Fésüs correction, reversed Vermeulen interpretation from Deep Research G.

RULES (mandatory):
1. Every objection must quote the knowledge-base file: file path + section heading + an exact quoted fragment (the raw files have no line numbers — quote enough words to find the line with Ctrl+F).
2. Every objection must be backed by a primary source (study, guideline, position statement) with DOI and/or PMID. Only doi.org, pubmed.ncbi.nlm.nih.gov or pmc.ncbi.nlm.nih.gov links — never redirect links (vertexaisearch, google.com/url, etc.).
3. Never invent PMIDs, DOIs, authors, titles or numbers. Before citing an identifier, open it and check that first author, year and title match. If you cannot confirm it, write "PMID UNVERIFIED" / "DOI UNVERIFIED". (Previous model audits of this base had up to 5 wrong PMIDs per report — we re-check every one.)
4. Only report a number if you saw it in the cited source; say whether you saw it in the abstract or the full text.
5. AI models (including you) are not sources. An objection based only on your reasoning must be labelled BIOMECH-INFERENCE or SPECULATION and ranked lower.
6. Use the base's label vocabulary when proposing fixes: {DOWÓD:przegląd|RCT|obserwacyjne}, {KONSENSUS}, {WNIOSKOWANIE}, {ANALOGIA:<sport/populacja>}, {SPEKULACJA}, {OPINIA}, {PROPOZYCJA}; counters ✔/⏳ and 1/2 / 2/2.
7. Do NOT add new positive claims or rewrite sections. You are attacking, not editing.
8. Prioritise: KRYTYCZNE (could harm a skater or reverses an effect) > WAŻNE (wrong label, false 2/2, number not in source, overgeneralisation) > DROBNE (wording, missing caveat). Max ~25 objections, most important first. Quality over quantity: if fewer real problems exist, report fewer.
9. If a file or link does not open, say so explicitly — do not guess its content.

OUTPUT FORMAT (Markdown, in Polish; keep quotes from files in the original Polish)
### Podsumowanie
3–6 sentences: overall reliability, the most serious problems, how many objections in each priority.

### Tabela zarzutów
| ID | Plik (+ sekcja) | Twierdzenie (dokładny cytat) | Typ błędu (fałszywe 2/2 / liczba spoza źródła / zła etykieta / nieuprawniona analogia / odwrócony kierunek / przesada / niebezpieczne / brak red flag / sprzeczność wewnętrzna) | Waga (KRYTYCZNE/WAŻNE/DROBNE) | Dowód (źródło pierwotne: autor, rok, DOI, PMID; abstract/full text) | Proponowana poprawka (relabel / weaken / remove / add caveat — exact new label or counter) |
|---|---|---|---|---|---|---|

### Twierdzenia, które wytrzymały atak
- quote + file + why it holds (briefly; especially 2/2 claims you checked and found sound)

### Luki krytyczne dla bezpieczeństwa
- what is missing, why it matters for AGV, best source you found (DOI/PMID) or "NO DATA FOUND"

### Sprzeczności wewnętrzne
- file A quote vs file B quote

### Identifier check
| Źródło | DOI | PMID | Otworzone i zgodne (autor+rok+tytuł) tak/nie |
|---|---|---|---|
```
