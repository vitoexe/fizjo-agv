# Prompty

## Jak teraz robimy research (decyzja 3.11.2026): tylko Gemini

- **Tylko Gemini.** Red-team Claude/Opus jest wstrzymany (pliki `3-claude-redteam.md` i `audyt/claude-redteam-1a/1b.md` zostają jako archiwum).
- **Gdzie:** Google AI Studio w przeglądarce (plan Pro, bez kluczy API). Prompt wklejamy jednym wklejeniem w pole tekstowe; wynik kopiujemy przyciskiem „Copy as markdown”.
- **Deep Research Max** — szerokie przeglądy literatury na temat batcha (pliki `1-deep-research.md` + gotowy do wklejenia `1-deep-research.prompt.txt`). Pilot: `batch-1/A-urazy-wg-grindu/` (w toku).
- **Gemini 4 Argon** — tylko sprzeczności, jedna sprzeczność na prompt (temp 0,2, Grounding + URL context, thinking High): `batch-1/argon-sprzecznosci-szablon.md`, `audyt/argon-*.md`.
- **Zapis wyniku:** `research-raw/RRRR-MM-DD_batch1-A_deep-research-max.md` z nagłówkiem front-matter (model, data, plik promptu, URL czatu AI Studio, czas, tokeny) — zob. `research-raw/README.md`.
- **Weryfikacja zawsze po naszej stronie:** każdy PMID/DOI w PubMed/Crossref/PMC, niezależność grup badawczych, liczby tylko ze źródła. Model nie jest źródłem.

Kolejność uruchamiania (decyzja 2.11.2026 — filar 1 „przygotowanie” jest główny):

1. `batch-2-przygotowanie/E-biomechanika-pozycja/` + `batch-2-przygotowanie/F-wzmacnianie-stabilizacja/`
2. `batch-2-przygotowanie/G-prewencja-periodyzacja/`
3. `batch-1/A-urazy-wg-grindu/` + `batch-1/B-obciazanie-sciegien/` (wspierają filar 1)
4. `batch-1/C-powrot-po-kostce/` + `batch-1/D-screening-fizjo/` (filar 2, niższy priorytet)

Argon (tylko sprzeczności): `batch-1/argon-sprzecznosci-szablon.md`.

Audyt sprzeczności (Argon, jedna sprzeczność na prompt):
- `audyt/argon-1-sila-biodra-koslawienie.md` — siła biodra a koślawienie kolana (zrobione, wynik: `research-raw/2026-11-02-argon-1-sila-biodra-koslawienie.md`).
- `audyt/argon-2-zmeczenie-tulow.md` — zmęczenie a lądowanie: zgięcie tułowia (adaptacja czy ryzyko), Carcia vs Patrek (zmęczenie a koślawienie), wytrzymałość a siła. Wymaga DOI + PMID i podwójnego sprawdzenia identyfikatorów.

Red-team całej bazy (Claude/Opus w claude.ai) — **WSTRZYMANY 3.11.2026** (tylko Gemini), pliki zostają jako archiwum:
- `audyt/claude-redteam-1a.md` — część 1: stabilizacja, wzmacnianie, prewencja, pozycja przy grindach, wzorce urazów, propozycje (F, Argon 1, Argon 2).
- `audyt/claude-redteam-1b.md` — część 2: obciążenie i periodyzacja, rozgrzewka, technika upadania, mobilność, wstrząśnienie, nadgarstek, propozycje (G).

## Linki do wklejenia modelom

Repo jest publiczne. Surowe pliki (gałąź `main`) do wklejenia w narzędzia z URL context (AI Studio, Gemini, Claude itp.):

```
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/METHODOLOGY.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/sources.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/README.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/soul-topsoul.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/makio.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/frontside-backside.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/royale.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/unity.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/inne.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/wzmacnianie.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/stabilizacja-i-propriocepcja.md
```

Gotowa linijka do promptu:

> Przeczytaj te pliki przez URL context zanim zaczniesz: https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/METHODOLOGY.md https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/sources.md https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/README.md https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/wzmacnianie.md https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/stabilizacja-i-propriocepcja.md — trzymaj się etykiet i zasady 2 niezależnych źródeł z METHODOLOGY.md, nie powtarzaj źródeł już obecnych w sources.md bez nowej informacji.
