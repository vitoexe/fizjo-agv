# research-raw — surowe wyniki modeli

Tu trafiają **surowe** wyniki narzędzi AI (Deep Research, Argon itp.) i nasze tabele weryfikacji. To nie jest baza wiedzy: do plików bazy wchodzi tylko to, co sprawdziliśmy w źródłach pierwotnych. Model nie jest źródłem.

## Nazwy plików (od 3.11.2026)

```
research-raw/RRRR-MM-DD_<batch>-<temat>_<narzędzie>.md
```

Przykłady:
- `research-raw/2026-11-03_batch1-A_deep-research-max.md`
- `research-raw/2026-11-04_audyt_argon-3-<krótki-temat>.md`

Data = dzień uruchomienia w AI Studio. Wcześniejsze pliki (`2026-11-02-E-gemini-deep-research.md`, `…-argon-1-…`, `…-argon-2-…`) zostają pod starymi nazwami, żeby nie psuć linków.

## Nagłówek (front-matter) — obowiązkowy

```yaml
---
model: "Gemini Deep Research Max"        # albo "Gemini 4 Argon", "Deep Research Preview"
narzedzie: "Google AI Studio (Pro, przeglądarka, bez klucza API)"
data: 2026-11-03
plik_promptu: "prompts/batch-1/A-urazy-wg-grindu/1-deep-research.prompt.txt"
commit_promptu: ""                        # hash commita z wersją promptu
url_czatu: ""                             # link do czatu w AI Studio (jeśli udostępniony; inaczej "prywatny")
czas_trwania: ""                          # np. "18 min"
tokeny: ""                                # jeśli AI Studio pokazuje; inaczej "brak danych"
ustawienia: ""                            # np. temp 0,2, Grounding, URL context, thinking High (Argon)
eksport: "Copy as markdown"
status_weryfikacji: "niezweryfikowane"    # → "w toku" → "zweryfikowane (hash)"
---
```

Pod nagłówkiem: pełny wynik modelu bez zmian, a pod nim sekcja `## Weryfikacja` (tabela ✔/✘/PARTIAL dla każdego PMID/DOI, błędy modelu, co weszło do bazy, hash commita).

Uwaga: wszystko w tym repo jest publiczne — w nagłówku nie wpisujemy danych prywatnych (e-maili, nazw kont).
