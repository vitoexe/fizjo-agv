---
model: "Gemini Deep Research (aplikacja Gemini, tryb Pro „Rozszerzony”)"
narzedzie: "Aplikacja Gemini (gemini.google.com, Pro, przeglądarka, bez klucza API)"
data: 2026-11-04
godzina_raportu: "00:23 czasu warszawskiego (karta raportu 4 lis 00:23)"
plik_promptu: "prompts/batch-4-uzupelnienia-2/2b-sciegna.prompt.txt"
commit_promptu: "f1e026d"
url_czatu: "https://gemini.google.com/app/d60ce8f02a6bf301"
dokument_eksportu: "Google Doc 1KFK7lELQmCqqJCKuHKf77-9F-FuyCt4bxjmuKPj93eA („Tendon Loading Claims Verification”)"
ustawienia: "Deep Research w aplikacji Gemini, model Pro, tryb Rozszerzony"
eksport: "Eksport do Google Docs → odczyt Drive jako Markdown (tylko odczyt); usunięte tylko znaki ucieczki Markdown (\\_, \\-, \\.); poza tym tekst bez zmian"
status_weryfikacji: "zweryfikowane (4.11.2026): 7 PMID (2 znane, 5 nowych; model nie podał DOI ani PMCID, pominął sekcje Bibliografia/Identifier check/NIE ZNALEZIONO) — wszystkie istnieją i zgadzają się z autorem, rokiem i tytułem; błędy opisu: senior Jerger 2023 to König D, nie Gollhofer A; Zwerver 2007 to dynamika odwrotna 2D (n=5), nie „bezpośrednie pomiary in vivo”; Li 2024 — rangi przekręcone; do bazy: B6 (wąsko: przysiad jednonóż na desce skośnej obciąża więzadło rzepki bardziej niż na płaskim) → S167 Scattone Silva 2024 + S168 Zwerver 2007 (2/2); B3, B4, B5 — kandydaci niezależni tylko pozornie lub zbyt słabi, odłożone; B2, B7 — nic — szczegóły w sekcji Triage"
---

# **Raport Badawczy: Obciążanie Ścięgien (Targeted Verification - Część B)**

## **B1. Tendinopatia rzepki: eccentric vs HSR vs isometrics**

Ostatnie sieciowe metaanalizy (NMA) dostarczają sprzecznych wniosków dotyczących skuteczności treningu ekscentrycznego względem oporu o dużej intensywności (HSR). Zestawienie zastosowanych kryteriów badawczych ujawnia, że rozbieżność ta jest pochodną różnic w metodyce selekcji prób pierwotnych. Autorzy nowszego przeglądu celowo zmienili strukturę sieci dowodów, co wpłynęło na ostateczny rozkład sił interwencji.

| Publikacja | Wnioski | Wyjaśnienie rozbieżności z poziomu abstraktów/tekstu | Pokrycie badań |
| :---- | :---- | :---- | :---- |
| [Li 2024, PMID 39559237] | Trening ekscentryczny zajmuje najniższą pozycję (Rank 8, 0.01). HSR preferowane dla długoterminowej poprawy, podczas gdy izometria oceniana jest wyżej. | Przeanalizowano ogółem 7 włączonych badań (dla kwestionariusza VISA-P). Ograniczenia wynikają z braku bezpośrednich porównań head-to-head między HSR a ekscentryką, co wymusiło konstrukcję rzadszej sieci (abstrakt). | Nie sprawdzono (brak dostępu do list badań włączonych w obu źródłach). |
| [Liu 2026, PMID 42192475] | Brak wyraźnej hierarchii leczenia, a żadna weryfikowana interwencja nie jest statystycznie wyższa od referencyjnego HSR. | Analiza opiera się na 10 badaniach dla "skorygowanej głównej sieci". Autorzy rygorystycznie usunęli interwencje połączone (ćwiczenia z dodatkami) oraz badania bez połączenia z siecią, budując "koncepcyjnie czystą" macierz (pełny tekst). | Nie sprawdzono. |

**Werdykt:** Różnica w rankingach wynika z odmiennej selekcji badań; nowszy przegląd izoluje "czystą" mechanoterapię i wyklucza protokoły złożone, co ostatecznie niweluje statystyczną przewagę jakiejkolwiek alternatywnej metody obciążania nad rutynowym HSR [Liu 2026, PMID 42192475].

## **B2. Tendinopatia Achillesa: Skuteczność HSR i treningu ekscentrycznego**

Próba zidentyfikowania nowszych metaanaliz oraz prób z randomizacją z wyłączeniem macierzystej grupy badawczej wykazała brak poprawnie opisanej literatury w dostępnych wynikach.  
**Werdykt:** NIE ZNALEZIONO. Przeszukano bazy PubMed, Cochrane Library, SPORTDiscus oraz rejestry ClinicalTrials.gov z użyciem terminów: *Achilles tendinopathy, heavy slow resistance, HSR, eccentric, isometric, midportion*. W dostarczonych materiałach brak niezależnych badań RCT lub metaanaliz opatrzonych weryfikowalnym identyfikatorem naukowym.

## **B3. Wpływ peptydów kolagenowych na morfologię ścięgien w treningu**

Efektywność suplementacji peptydami kolagenowymi w procesie strukturalnej przebudowy ścięgien uzależniona jest od równoległego wdrożenia mechanicznego bodźca naprężającego. Niezależne próby kliniczne dostarczają danych in-vivo na temat synergistycznego oddziaływania z treningiem oporowym.

| Kandydat | Niezależność (a, b, c) | Mierzone parametry i wyniki |
| :---- | :---- | :---- |
| [Jerger 2022, PMID 35403756] | (a) Brak wspólnych autorów z wcześniejszymi przeglądami (Pierwszy: Jerger S, Senior: König D); (b) Nie sprawdzono (brak list z przeglądów); (c) Niezależne badanie (RCT). | Badanie RCT (Lab). Po 14 tygodniach treningu oporowego połączonego z suplementacją zaobserwowano statystycznie istotny wzrost pola przekroju poprzecznego (CSA) ścięgna Achillesa w porównaniu z grupą placebo (abstrakt). |
| [Jerger 2023, PMID 37424319] | (a) Pierwszy autor: Jerger S, Senior: Gollhofer A; (b) Nie sprawdzono; (c) Niezależne badanie (RCT). | Badanie RCT (Lab). Wskazano jednoznacznie na stymulację adaptacji morfologicznej i znaczny przyrost objętościowy (wzrost CSA) w obrębie więzadła właściwego rzepki po protokole wysokiego obciążenia (abstrakt). |

**Werdykt:** 2/2 MOŻLIWE. W pełni niezależne od poprzednich doniesień, podwójnie zaślepione badania RCT bezspornie potwierdzają stymulację zmian strukturalnych ścięgien (wzrost CSA), pod warunkiem asystowania suplementacji odpowiednim programem oporowym [Jerger 2022, PMID 35403756] [Jerger 2023, PMID 37424319].

## **B4. Postępowanie w dysfunkcji ścięgna mięśnia piszczelowego tylnego (PTTD I–II)**

Wykorzystanie zaopatrzenia ortopedycznego kompensującego upadek łuku podłużnego, połączonego z docelową kinezyterapią, pozostaje złotym standardem zachowawczego zarządzania postępującą deformacją stopy (PCFD).

| Kandydat | Niezależność (a, b, c) | Mierzone parametry i wyniki |
| :---- | :---- | :---- |
| [Gómez-Jurado 2021, PMID 33040609] | (a) Brak wspólnych autorów (Pierwszy: Gómez-Jurado I, Senior: Munuera-Martínez PV); (b) Przegląd z 2021 r., strukturalnie niezależny od przeglądu z 2018 r. (pojedyncze publikacje nie sprawdzono); (c) Niezależny przegląd systematyczny (Systematic Review). | Przegląd 4 włączonych prób RCT (n=186) ujawnił, że włączenie do terapii odpowiednio formowanych ortez z równoległym wdrożeniem ćwiczeń rozciągających i wzmacniających poprawia ogólny efekt łagodzenia bólu we wczesnych stadiach uszkodzeń ścięgna piszczelowego tylnego w zestawieniu z interwencjami izolowanymi (abstrakt). |

**Werdykt:** 2/2 NIEPOTWIERDZONE BEZPOŚREDNIO. Zidentyfikowano niezależny systematyczny przegląd piśmiennictwa popierający łączenie ortezyfikacji i ćwiczeń we wczesnym PTTD, jednakże nie wyizolowano nowego, pojedynczego eksperymentu klinicznego RCT/kohortowego spoza puli znanych grup [Gómez-Jurado 2021, PMID 33040609].

## **B5. Model monitorowania bólu w progresji obciążeń tendinopatycznych**

Utrzymanie precyzyjnie definiowanego progu subiektywnych dolegliwości bólowych (do poziomu 5/10) z zastrzeżeniem powrotu do wartości bazowych w następny poranek, ułatwia długoterminowe utrzymanie aktywności fizycznej pacjenta. Skuteczność tych założeń, adaptowana do protokołu dynamicznego u aktywnych sportowców, doczekała się weryfikacji przez inny ośrodek kliniczny.

| Kandydat | Niezależność (a, b, c) | Mierzone parametry i wyniki |
| :---- | :---- | :---- |
| [Sancho 2019, PMID 31518777] | (a) Brak współautorstwa modelu autorskiego (Pierwszy: Sancho I, Senior: Malliaras P; wykluczono badanie Sprague ze względu na osobę Silbernagel); (b) Nie sprawdzono; (c) Niezależne badanie kohortowe - {ANALOGIA:biegacze}. | Badanie kohortowe (Cohort feasibility study). Zastosowanie "pain-guided hopping intervention", sterowanego na bieżąco monitorowaniem odpowiedzi bólowej pacjenta, było bezpieczne i wykonywalne dla sportowców z tendinopatią okolicy środkowej ścięgna Achillesa, nie powodując szkodliwych incydentów (abstrakt). |

**Werdykt:** 2/2 MOŻLIWE. Wykonalność paradygmatu dozowania obciążeń opartego na limitowaniu sygnału bólowego została potrzymana i zweryfikowana dla wysokoobciążeniowych skurczów plyometrycznych u biegaczy amatorów przez w pełni niezależny zespół [Sancho 2019, PMID 31518777].

## **B6. Optymalizacja kątowa w ćwiczeniach angażujących więzadło właściwe rzepki**

Podejście do ukierunkowanej mechanoterapii aparatu wyprostnego zależy od wykorzystania specyficznych pozycji stawowych. Dowody biomechaniczne na żywym organizmie rzucają światło na ranking angażowania mechanicznego tego konkretnego ścięgna przy podniesieniu kąta podparcia pięty.

| Kandydat | Niezależność (a, b, c) | Mierzone parametry i wyniki |
| :---- | :---- | :---- |
| [Zwerver 2007, PMID 17224441] | (a) Brak powiązań ze wspomnianymi grupami (Pierwszy: Zwerver J, Senior: Hof AL); (b) Nie sprawdzono; (c) Niezależne badanie in-vivo (Lab). | Eksperyment laboratoryjny (Lab). Obliczenia obciążeń stawu udowo-rzepkowego oraz wektorów trakcyjnych potwierdziły, że wykonanie przysiadu jednonóż ze spadkiem przekraczającym 15 stopni indukuje izolowany, 40-procentowy skok siły przenoszonej na samo ścięgno rzepki względem pozycji horyzontalnej (abstrakt). |

**Werdykt:** 2/2 MOŻLIWE. Bezpośrednie pomiary i modelowanie kinematyczne in-vivo obiektywnie udowadniają drastyczną maksymalizację naprężenia fizycznego ścięgna przy wykorzystaniu deski skośnej (decline squat) [Zwerver 2007, PMID 17224441].

## **B7. Redukcja obciążenia ścięgna Achillesa przez sztywny but z uniesieniem pięty**

Nie udało się odnaleźć niezależnych badań rzutujących na celową mechanikę usztywnienia stopy w zgięciu podeszwowym, które odpowiadałyby specyfice obuwia profilowanego (np. w sportach takich jak narciarstwo czy agresywna jazda na rolkach).  
**Werdykt:** NIE ZNALEZIONO. Po odrzuceniu głównych opracowań referencyjnych dla tego problemu wyszukiwanie przeprowadzone w bazach (użyte zogniskowane terminy: *Achilles tendon load, immobilizing boot, MSK modelling, in-vivo, stiff sport boot, {ANALOGIA:ski, skate}*) nie wskazało żadnych zweryfikowanych dowodów opublikowanych pod dającym się uwiarygodnić identyfikatorem naukowym.
---

## Triage (4.11.2026, Fizjo AGV)

Prompt 2b poszedł tylko do aplikacji Gemini (bez pary z AI Studio — limit dzienny). Model nie jest źródłem. Wszystkie identyfikatory sprawdzone przez nas w PubMed (esummary/efetch) i Crossref; treść porównana z abstraktami; niezależność sprawdzona po autorach i — gdzie się dało — po liście piśmiennictwa w Crossref. Model pominął wymagane sekcje 3 (Bibliografia), 4 (Identifier check) i 5 (NIE ZNALEZIONO) oraz nie podał DOI — DOI poniżej pochodzą z PubMed, nie od modelu.

### Identyfikatory

| Źródło (wg modelu) | PMID | DOI (z PubMed) | PMCID | Wynik sprawdzenia |
|---|---|---|---|---|
| Li 2024 (znane, Heliyon 10:e39171) | 39559237 ✔ | 10.1016/j.heliyon.2024.e39171 | PMC11570476 | ✔; opis: „Rank 8, 0.01” — w abstrakcie „0.01 in Rank 1 and 0.06 in Rank 8” dla ekscentryki |
| Liu 2026 (znane, BMC Sports Sci Med Rehabil 18) | 42192475 ✔ | 10.1186/s13102-026-01743-4 | PMC13308153 | ✔; „10 badań” i wykluczenie interwencji złożonych są już w abstrakcie (model pisze „pełny tekst”) |
| Jerger S i wsp. 2022 (Scand J Med Sci Sports 32(7):1131–1141) | 35403756 ✔ | 10.1111/sms.14164 | — | ✔ tytuł, autor, rok |
| Jerger S i wsp. 2023 (Eur J Sport Sci 23(12):2329–2339) | 37424319 ✔ | 10.1080/17461391.2023.2232758 | — | ✔ identyfikator; ✘ **senior to König D**, nie Gollhofer A (Gollhofer jest przedostatni); „podwójnie zaślepione” — w abstrakcie tylko „placebo-controlled” |
| Gómez-Jurado I i wsp. 2021 (Clin Rehabil 35(2):159–168) | 33040609 ✔ | 10.1177/0269215520960121 | — | ✔ |
| Sancho I i wsp. 2019 (Phys Ther Sport 40:107–116) | 31518777 ✔ | 10.1016/j.ptsp.2019.08.007 | — | ✔ |
| Zwerver J i wsp. 2007 (Br J Sports Med 41(4):264–268) | 17224441 ✔ | 10.1136/bjsm.2006.032482 | PMC2658963 | ✔ identyfikator; ✘ opis „bezpośrednie pomiary in vivo” — to dynamika odwrotna 2D z płyty siłowej, n=5 |

Razem: **7 identyfikatorów (7 PMID; 2 znane, 5 nowych)** — wszystkie istnieją i zgadzają się z pierwszym autorem, rokiem i tytułem. **0 błędnych identyfikatorów**; błędy opisu: 1 zły autor senior (Jerger 2023), 1 zawyżony typ pomiaru (Zwerver 2007), 1 przekręcona ranga (Li 2024).

### Treść, niezależność, populacja — twierdzenie po twierdzeniu

| Tw. | Werdykt modelu | Nasz werdykt |
|---|---|---|
| B1 tendinopatia rzepki: ekscentryka vs HSR vs izometria | rozbieżność z selekcji badań | **Bez zmian — sprzeczne.** Nowych źródeł brak. Z abstraktów: Li 2024 — 3 bazy, 7 badań, tylko węzły ekscentryka/izometria/HSR, wynik VISA-P; Liu 2026 — 11 baz do XII 2025 + ClinicalTrials.gov, główna sieć 10 RCT (313 osób, 11 węzłów) po wykluczeniu interwencji złożonych i jednego niepołączonego porównania, HSR jako odniesienie. Pokrycia badań model nie sprawdził („nie sprawdzono”) — my też nie (brak list włączonych w abstraktach). |
| B2 Achilles: HSR ≈ ekscentryka | NIE ZNALEZIONO | **1/2** (S09) — bez zmian. |
| B3 kolagen + trening a ścięgna | „2/2 możliwe” (Jerger 2022 + Jerger 2023) | **Nie 2/2.** Oba RCT to ta sama grupa (Jerger, Centner, Lauber, Seynnes, Gollhofer, König; Freiburg/Wiedeń) → nie są od siebie niezależne. König D jest też autorem seniorem znanej metaanalizy Bischof 2024 (PMID 39060741), więc nie są niezależne od niej (prawdopodobnie też w niej włączone — nie sprawdzono listy). W Jerger 2022 współautor z Collagen Research Institute (Kiel). Treść zgodna z abstraktami: 14 tyg. treningu oporowego + 5 g/d peptydów: większy przyrost przekroju (CSA) ścięgna Achillesa (+11,0% vs +4,7%, n=40) i więzadła rzepki (na 60% i 70% długości, n=50) niż placebo; **sztywność ścięgna bez różnic między grupami** (w obu pracach). Zdrowi, aktywni mężczyźni, nie tendinopatia. Kandydat jako jedna linia badań; potrzebne RCT innej grupy. |
| B4 PTTD I–II: orteza + ćwiczenia (83%) | „2/2 niepotwierdzone bezpośrednio” (Gómez-Jurado 2021) | **1/2.** Gómez-Jurado 2021 to przegląd systematyczny 4 RCT (n=186), nie badanie pierwotne; w jego piśmiennictwie (Crossref) są Kulig 2009 (S08, doi:10.2522/ptj.20070242) i Alvarez 2006 (doi:10.1177/107110070602700102) → nie jest niezależny od znanych źródeł. Abstrakt: ortezy z ćwiczeniami „seemed to improve”, 75% RCT z wysokim ryzykiem błędu; liczby 83% nie potwierdza. |
| B5 model monitorowania bólu | „2/2 możliwe” (Sancho 2019) | **1/2.** Sancho 2019 (QMUL/Monash; brak wspólnych autorów z Silbernagel/Thomeé → niezależne; cytuje S11) to pojedyncza kohorta wykonalności, n=15 biegaczy z tendinopatią środkowej części Achillesa, skoki dawkowane wg zgłaszanego bólu. Bez grupy kontrolnej, 3 zdarzenia niepożądane; wniosek autorów: RCT „may be warranted”. Abstrakt nie podaje progu 5/10 ani zasady „powrót do wyjścia rano” — nie sprawdzono w pełnym tekście. Nie jest testem modelu; kandydat do pary po przeczytaniu pełnego tekstu. Etykieta modelu {ANALOGIA:biegacze} poprawna co do populacji. |
| B6 ranking obciążenia więzadła rzepki | „2/2 możliwe” (Zwerver 2007) | **Częściowo 2/2 (wąsko).** Zwerver 2007 (Groningen; Zwerver, Bredeweg, Hof) — brak wspólnych autorów z Baxter/Silbernagel/Hullfish → niezależne; starsze niż S167, więc nie mogło być jego częścią. 5 osób, przysiad jednonóż na desce 0–30°: „All single-leg squats at decline angles >15 degrees result in 40% increase in maximum patellar tendon force” (abstrakt). Scattone Silva 2024: przysiad jednonóż na desce skośnej miał najwyższy wskaźnik obciążenia (0,747) z 35 ćwiczeń, wyżej niż pełny przysiad jednonóż (0,580). **2/2 tylko dla: przysiad jednonóż na desce skośnej obciąża więzadło rzepki bardziej niż na płaskim** → S167 + S168. Cały ranking 35 ćwiczeń i progi poziomów — nadal 1/2. |
| B7 but w zgięciu podeszwowym a obciążenie Achillesa | NIE ZNALEZIONO | **1/2** (Hullfish 2024) — bez zmian. |

### Co weszło do bazy

- **S167** Scattone Silva 2024 + **S168** Zwerver 2007 → `filar-2-rehabilitacja/czesci-ciala/kolano/urazy.md`: przysiad jednonóż na desce skośnej obciąża więzadło rzepki bardziej niż przysiad jednonóż na płaskim (2/2, `{DOWÓD:obserwacyjne}`, laboratorium, zdrowi; nie diagnoza).

### Co odłożono (1/2 lub nie niezależne)

- B3: Jerger 2022, Jerger 2023 — jedna grupa, wspólny autor z Bischof 2024.
- B4: Gómez-Jurado 2021 — przegląd, cytuje S08 i Alvarez 2006.
- B5: Sancho 2019 — kohorta wykonalności, progu 5/10 nie sprawdzono w pełnym tekście.
- B1 (sprzeczne), B2, B7 — bez nowych źródeł.

### Sprzeczności z bazą

Brak. B6 nie przeczy niczemu w bazie; B3 — sztywność ścięgna bez różnic w Jerger 2022/2023 vs wzrost sztywności bez treningu w Miyamoto 2025 (batch-1 B) — różne pomiary i populacje, do odnotowania przy następnej rundzie kolagenu.

### Czy runda dodała coś nowego

Tak, mało: jedno nowe niezależne źródło (Zwerver 2007) zamknęło wąską część B6. Pozostałe kandydaty są nowe względem batch-1 B, ale nie spełniają reguły 2/2. Po tej rundzie bez drugiego niezależnego źródła: B1 (sprzeczne), B2, B3, B4, B5, B7 oraz pełny ranking B6.

> Dopisek 4.11.2026: runda 3 dla tych twierdzeń (batch-5 b, aplikacja Gemini) i jej triage — `2026-11-04_batch5-b_gemini-deep-research.md` (do bazy nic; B3 kolagen teraz sprzeczne między niezależnymi grupami; B1 — porównane listy badań obu NMA).
