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

## Lekcje

- **3.11.2026, batch-1 A (Deep Research Preview):** model podał błędne lub niedopasowane DOI/PMID w **5 z 7 par** (identyfikatory prowadziły do zupełnie innych prac), a jego tabela „Identifier check” wszędzie miała „Tak”. Do tego przypisał pracy liczbę, której w niej nie ma (Giacobetti 1997: „−31,8% siły” — w rzeczywistości brak różnicy), oznaczył badanie na zwłokach jako RCT, a blogi i strony klinik jako {DOWÓD}. **Zasada: każdy PMID i DOI sprawdzamy w PubMed (efetch/esummary) i Crossref, zanim wejdzie do bazy; liczby tylko z abstraktu/pełnego tekstu, który sami przeczytaliśmy.** Self-check modelu nie jest weryfikacją.
- **3.11.2026, batch-1 C (Gemini app Deep Research, Pro Rozszerzony):** po zaostrzeniu promptu (PMID+DOI ze strony PubMed, „UNVERIFIED” zamiast zgadywania) **wszystkie 8 źródeł i ich PMID/DOI/PMC były poprawne** (0/8 błędów; PMID jednego źródła brakował — uzupełniony po DOI). Błędy przeniosły się z identyfikatorów na **treść**: zdania przypisane pracom, w których ich nie ma (PAASS przypisany innej pracy, „hokeiści” i „sztywny but” w pracy o australijskiej kohorcie), zawyżone etykiety (crossover jako RCT, opinie ekspertów jako {DOWÓD}), „2/2” z drugim źródłem, które nie mówi tego samego, i sekcja „sprzeczności” ze zmyślonymi cytatami z naszej bazy. **Zasada: poprawny PMID ≠ poprawne twierdzenie — każde zdanie i liczbę porównujemy z abstraktem; „sprzeczności z bazą” sprawdzamy w naszych plikach, a niezależność grup — po listach autorów (tu: autorzy przeglądów okazali się współautorami PAASS [S19]).**
- **3.11.2026, batch-1 D (Gemini app Deep Research, Pro Rozszerzony, screening):** mimo promptu zaostrzonego o lekcje z C, **7 z 14 identyfikatorów w bibliografii było błędnych lub należało do innej pracy** (błędny PMID przy poprawnym DOI, DOI innej pracy przy poprawnym PMC, nieistniejący DOI, PMC przypisane innym autorom), a przypisy w tekście wskazywały inne prace niż bibliografia (np. przypis przy Plisky 2006 = Chang 2020 z wynikiem odwrotnym). Model nie otworzył plików bazy, więc sekcja „sprzeczności” była pusta. **Zasada: identyfikatory weryfikujemy niezależnie od siebie (PMID, DOI, PMC osobno) i sprawdzamy, czy przypis w tekście wskazuje tę samą pracę co bibliografia; „UNVERIFIED” od modelu nie oznacza, że pozostałe pozycje są pewne.**
