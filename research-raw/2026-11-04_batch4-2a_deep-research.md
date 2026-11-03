---
model: "Gemini Deep Research Preview (models/deep-research-preview-04-2026)"
narzedzie: "Google AI Studio (Pro, przeglądarka, bez klucza API)"
data: 2026-11-04
plik_promptu: "prompts/batch-4-uzupelnienia-2/2a-kostka-screening-urazy.prompt.txt"
commit_promptu: "f1e026d"
url_czatu: "https://aistudio.google.com/prompts/1qwu9MrKz9-JZU8kCXOBwl2rhxpyFyj4t"
czas_trwania: "ok. 11 min (start 00:10, odpowiedź 00:20 czasu warszawskiego, 4.11.2026; wg createTime w pliku AI Studio)"
tokeny: "łącznie 1 836 539 (wejście 1 576 806, w tym cache 368 640; wyjście 22 104; myślenie 76 003; narzędzia 161 626)"
ustawienia: "temperature 1.0, topP 0.95, Google Search + Browse jako narzędzia"
eksport: "plik czatu AI Studio z Google Drive (JSON), pole odpowiedzi modelu; surowy JSON obok: 2026-11-04_batch4-2a_deep-research.json"
status_weryfikacji: "niezweryfikowane"
---

> Uwaga: Deep Research **Preview**, status czatu COMPLETED. Prompt w pliku czatu jest identyczny z plikiem promptu (commit f1e026d). Odpowiedź bez pola citations (brak linków). Ten sam prompt 2a leci też w aplikacji Gemini (Deep Research) — jego wynik zostanie dołączony później jako osobny plik. Poniżej pełna odpowiedź modelu bez zmian.

## 1. Podsumowanie
Przeanalizowano 16 twierdzeń pod kątem obecności niezależnych źródeł drugorzędnych. Uzyskano 1 werdykt częściowo potwierdzający (D3), natomiast dla pozostałych 15 twierdzeń nie znaleziono dokumentów spełniających rygorystyczne kryteria włączenia (brak niezależnego drugiego źródła). Zidentyfikowano 1 badanie oznaczone jako UNVERIFIED z uwagi na brak identyfikatora PMID.

## 2. Twierdzenia

### C1

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Picot 2023, 2024 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła — odnalezione teksty to doniesienia zespołu Picot/Fourchet (odrzucone) lub opisy nienaukowe.

### C2b

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Picot 2025 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła — zidentyfikowane badanie krzyżowe oceniające ortezy w niestabilności nie zawiera danych autorów ani PMID.

### C3

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Salameh 2022 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła — wszystkie wyselekcjonowane statystyki (70.9 vs 39.3) pochodzą z przeglądu Salameh 2022 lub badań już w nim zawartych (np. D'Hooghe 2020).

### C4

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Sman 2014 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła — nie zidentyfikowano innych testów prognostycznych (w tym wyskoku) korelujących z czasem powrotu po urazie więzozrostu.

### D1

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Plisky 2006, Stiffler 2017, Sklempe Kokic 2023 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła — jedyne odnalezione badanie potwierdzające próg 4 cm w powiązaniu z FMS było przekrojowe (cross-sectional), a nie prospektywne.

### D2

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Powden 2015, Chisholm 2012 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła — cytowane w publikacjach wartości 1.9/1.6 cm to uśrednione dane raportowane bezpośrednio w przeglądzie Powden 2015.

### D3

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Bohannon 2022, Hébert-Losier 2017 | Schrefl 2024, UNVERIFIED | 10.36950/2024.9ciss009 | Test-retest reliability | sport students | 21 | "number of repetitions (Intraclass correlation coefficient (ICC) = 0.91" (Abstrakt) | (a) tak (b) nie sprawdzono |
**Werdykt:** częściowo potwierdzone — potwierdzono znakomitą rzetelność ustandaryzowanego protokołu, lecz zbyt mała próba nie pozwala na wyznaczenie norm, a brak PMID wymusza nadanie statusu UNVERIFIED.

### D4

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Bahr 2016 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła — odnaleziono wspominany "scoping review" 86 badań (negujący predykcję u jednostki), lecz w udostępnionych fragmentach brakuje nazwisk autorów oraz PMID.

### D5

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Alghadir 2020 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła.

### D6

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| De Ridder 2015 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła.

### D7

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Burton 2020 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła.

### D8

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Sprague 2018, Backman 2011 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła.

### D9

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| brak | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła.

### A1

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Maudot 2014, Hilgert 2004 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła — idealnie dopasowane badanie 66 skaterów AGV (wskazujące 55,5% urazów rąk) we fragmentach nie posiadało autorów i identyfikatorów, dlatego zostało odrzucone.

### A2/A3

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Schieber 1996, Cheng 1995, Giacobetti 1997, Lewis 1997, Russell 2007, Twining 2022 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła.

### A4

| Źródło znane | Nowe źródło [Autor rok, PMID] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
|---|---|---|---|---|---|---|---|
| Russell 2014 | brak | brak | brak | brak | brak | brak | brak |
**Werdykt:** brak drugiego źródła.

## 3. Bibliografia (tylko nowe źródła)

| # | Autorzy, rok, tytuł, czasopismo, tom:strony | Typ badania | n | PMID | DOI | PMCID |
|---|---|---|---|---|---|---|
| 1 | Schrefl A, Kolokythas N, Stamm M, Erlacher D, Schärli A., 2024, Reliability of a standardized protocol of the Single Leg Heel Rise Test, Current Issues in Sport Science, 9(1):009 | Test-retest reliability | 21 | UNVERIFIED | 10.36950/2024.9ciss009 | brak |

## 4. Identifier check

| Źródło | PMID | DOI | PMCID | Strona PubMed otwarta? | Zgodne? tak/nie/UNVERIFIED |
|---|---|---|---|---|---|
| Schrefl 2024 | brak | 10.36950/2024.9ciss009 | brak | nie | UNVERIFIED |

## 5. NIE ZNALEZIONO
- C1 — bazy: PubMed, Cochrane, Google Scholar; hasła: "Ankle-GO" external validation, score, re-sprain risk.
- C2b — bazy: PubMed, SPORTDiscus; hasła: ankle brace, chronic ankle instability, CAI, functional tests, confidence.
- C3 — bazy: PubMed, Cochrane; hasła: syndesmotic injury, surgery vs conservative, return to sport time, cohort.
- C4 — bazy: PubMed; hasła: syndesmotic injury return to play prognostic tests FABQ vertical jump.
- D1 — bazy: PubMed, SPORTDiscus; hasła: SEBT anterior asymmetry 4 cm prospective injury risk.
- D2 — bazy: PubMed, Cochrane; hasła: weight-bearing lunge test MDC 1.9 cm intra-rater 1.6 cm inter-rater.
- D4 — bazy: PubMed, Google Scholar; hasła: screening tests predictive accuracy systematic review sensitivity AUC.
- D5 — bazy: PubMed, SPORTDiscus; hasła: CAI proprioception dorsiflexion active ankle range.
- D6 — bazy: PubMed, Google Scholar; hasła: CAI stiffer landing sagittal ankle motion peak vertical GRF.
- D7 — bazy: PubMed, Cochrane; hasła: mobilization with movement dorsiflexion CAI.
- D8 — bazy: PubMed; hasła: reduced dorsiflexion patellar tendinopathy prospective.
- D9 — bazy: PubMed, SPORTDiscus; hasła: screening battery action landing sports injury prediction.
- A1 — bazy: PubMed, Google Scholar; hasła: aggressive inline skating injury patterns statistics mechanisms.
- A2/A3 — bazy: PubMed, SPORTDiscus; hasła: wrist guards inline roller skateboard splint-top fractures.
- A4 — bazy: PubMed, SPORTDiscus; hasła: terrain-park features injury risk.
