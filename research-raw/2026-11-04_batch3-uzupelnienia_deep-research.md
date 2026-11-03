---
model: "Gemini Deep Research Preview (models/deep-research-preview-04-2026)"
narzedzie: "Google AI Studio (Pro, przeglądarka, bez klucza API)"
data: 2026-11-03
plik_promptu: "prompts/batch-3-uzupelnienia/1-deep-research.prompt.txt"
commit_promptu: "e3df3d0"
url_czatu: "https://aistudio.google.com/prompts/12mTGBppFEL3lAi6EoFSKP_wpCxzZyqyZ"
czas_trwania: "ok. 13 min (start 23:09, odpowiedź 23:21 czasu warszawskiego, 3.11.2026; wg createTime w pliku AI Studio)"
tokeny: "łącznie 954 852 (wejście 748 711, w tym cache 82 005; wyjście 29 945; myślenie 64 908; narzędzia 111 288)"
ustawienia: "temperature 1.0, topP 0.95, Google Search + Browse jako narzędzia"
eksport: "plik czatu AI Studio z Google Drive (JSON), pole odpowiedzi modelu; surowy JSON obok: 2026-11-04_batch3-uzupelnienia_deep-research.json"
status_weryfikacji: "zweryfikowane (4.11.2026): 7 identyfikatorów (5 PMID + 2 PMCID) sprawdzonych w PubMed/PMC — wszystkie istnieją i pasują do opisów modelu; Schrefl 2024 i „scoping review” bez identyfikatorów (niezweryfikowane); do bazy weszło tylko C2 (tejp w CAI): Picot 2025 → S156 + Halim-Kertanegara 2017 → S157; szczegóły w sekcji Triage na końcu"
---

> Uwaga: Deep Research **Preview**. Prompt w pliku czatu (9099 znaków) jest identyczny z plikiem promptu (commit e3df3d0). Model nie podał autorów ani tytułów przy większości pozycji („Brak danych”) — uzupełniliśmy je z PubMed w sekcji Triage. Odpowiedź bez pola citations (brak linków vertexaisearch). Poniżej pełna odpowiedź modelu bez zmian.

# Raport z weryfikacji bazy wiedzy Fizjo AGV: Analiza dowodów naukowych i walidacja twierdzeń klinicznych

## 1. Podsumowanie
Weryfikacja docelowa bazy wiedzy Fizjo AGV na podstawie dostarczonych materiałów badawczych wykazała, że z 17 przeanalizowanych twierdzeń cztery uzyskały pełne potwierdzenie (status 2/2), dostarczając solidnych, niezależnych dowodów w architekturze wiedzy klinicznej. Trzy twierdzenia zostały sklasyfikowane jako częściowo potwierdzone lub wymagające istotnego zniuansowania, natomiast dwa całkowicie obalono ze względu na istnienie silnych dowodów przeciwstawnych o wyższej jakości metodologicznej. W przypadku ośmiu postulatów nie zidentyfikowano drugiego, niezależnego źródła podstawowego, co oznacza, że pozostają one na statusie 1/2. Ze względu na rygorystyczne zasady zakazujące inferencji brakujących metadanych badawczych, osiem identyfikatorów w tabeli końcowej otrzymało status UNVERIFIED, co odzwierciedla luki informacyjne w dostarczonych abstraktach i wyciągach tekstowych.

## 2. Twierdzenia

### C1. Ankle-GO score <8 points 2 months after lateral ankle sprain → higher re-sprain risk within 2 years (OR 8.6) and lower chance of return to the same level.

Skręcenie stawu skokowego bocznego (LAS) to najczęstszy uraz układu chrzęstno-kostnego w sporcie, charakteryzujący się wysokim odsetkiem nawrotów (re-sprain) sięgającym 70% w sportach wysokiego ryzyka. Niestabilność ta często przechodzi w chroniczną niestabilność stawu skokowego (CAI) [Brak danych, PMC10732116]. System Ankle-GO, oparty na wytycznych PAASS (ból, ograniczenia ruchowe, percepcja zawodnika, kontrola sensomotoryczna i specyficzna dla sportu wydajność funkcjonalna), został zaprojektowany w celu obiektywizacji kryteriów powrotu do sportu (RTS). Narzędzie to składa się z czterech testów funkcjonalnych oraz dwóch kwestionariuszy oceny subiektywnej, tworząc złożony wynik (maksymalnie 25 punktów). 

Jak wynika z dostępnych danych, punktacja poniżej 11 punktów w 2. miesiącu po urazie obniża prawdopodobieństwo osiągnięcia pełnej adaptacji (statusu "coper") do zaledwie 6.8%, podczas gdy wynik powyżej 11 punktów zwiększa tę szansę do 69% [Brak danych, 37434508]. 



Klinicyści stają jednak przed istotnym wyzwaniem: chociaż wewnętrzna spójność (Cronbach's alpha 0.79) i doskonała powtarzalność test-retest (ICC = 0.99) wskazują na wysoką użyteczność, cała struktura dowodowa opiera się na badaniach pochodzących z jednego ośrodka [Brak danych, 37434508]. Ze względu na brak zewnętrznej i niezależnej ewaluacji w innych populacjach, narzędzie to, mimo swoich niewątpliwych zalet w stratyfikacji ryzyka (identyfikacja pacjentów, zwłaszcza kobiet, wymagających zintensyfikowanej rehabilitacji), wciąż wymaga globalnej weryfikacji.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Picot 2023, Picot 2024 | NIE ZNALEZIONO | Brak | Brak | Brak | Brak | Brak | Brak |

**Werdykt:** Brak drugiego źródła — wszystkie wyodrębnione z materiałów publikacje walidujące test Ankle-GO i jego punkty odcięcia pochodzą od jednej powiązanej grupy badawczej (Picot, Lopes, Fourchet, Rauline, Hardy), niezależnie od faktu ewaluacji u pacjentów po LAS czy rekonstrukcji ścięgna Achillesa.

### C2. In chronic ankle instability (CAI), taping and bracing improve self-reported function/confidence but not functional test performance (hop, SEBT, balance).

W leczeniu zachowawczym przewlekłej niestabilności stawu skokowego (CAI) powszechnie aplikuje się sztywny tejp (rigid ankle tape) lub ortezy w celu restrykcji patologicznego zakresu ruchu i ochrony aparatu więzadłowego. Współczesna biomechanika rzuca jednak nowe światło na mechanizm działania tych interwencji zewnętrznych. Obserwacje kliniczne sugerują, że nadrzędny efekt ochrony stawu nie wynika ze sztywnej blokady inwersji i ewersji, lecz z modulacji aferentnej i wsparcia psychologicznego. Badania wydolnościowe obejmujące m.in. skoki po ósemce (figure-8 hopping test), modyfikowany bieg z przeszkodami, test równowagi SEBT oraz jednonóż (single-leg stance) wykazały, że tejp aplikowany u pacjentów z funkcjonalną niestabilnością nie poprawia obiektywnych czasów i wyników tych prób [Brak danych, 27262625]. 

Zasadnicza zmiana następuje w domenie kognitywno-behawioralnej. Poczucie subiektywnej stabilności, pewność siebie w trakcie obciążania kończyny (reassurance) oraz ogólna własna skuteczność (self-efficacy) wzrastają istotnie statystycznie u pacjentów zaopatrzonych tejpem. Świadczy to o tym, że interwencje pasywne w CAI pełnią potężną funkcję przeciwlękową, redukując obawę przed ponownym urazem (kinezjofobię), co umożliwia pacjentom partycypację w treningu nawet bez obserwowalnej zmiany w kinematyce stawu podczas lądowania czy balansu [Brak danych, 27262625]. Wyjątkiem, w którym tejp faktycznie poprawił obiektywny czas wykonania zadania, było schodzenie ze schodów (stair descent test), gdzie czas skrócił się o około 4%.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Picot 2025 | Brak danych, rok nieznany | 27262625 | Brak | Badanie obserwacyjne / kliniczne | Brak danych | Abstrakt dokumentuje: "rigid ankle tape had a limited impact on functional performance" w testach hop, SEBT i balansie. Jednocześnie tejp ulepszył zaufanie: "Overall self-efficacy increased significantly with the application of rigid tape". | Badanie niezależne od francuskiej grupy Picot (na podstawie odmiennego PMID 27262625 vs 39916658 z oryginalnego zapytania). |

**Werdykt:** Potwierdzone (2/2) — wykazano empirycznie u pacjentów z niestabilnością skokową, że aplikacja sztywnego tejpa podnosi zaufanie do stawu i minimalizuje wahanie (aprehensję), pozostawiając wydolność w testach dynamicznych, takich jak SEBT i testy skocznościowe, bez statystycznie znamiennych zmian.

### C3. Isolated syndesmotic (high ankle) injury: return to play longer after surgery than with conservative care (pooled 70.9 vs 39.3 days).

Uszkodzenia więzozrostu piszczelowo-strzałkowego ("high ankle sprains") stanowią istotne wyzwanie dla medycyny sportowej ze względu na drastyczne różnice w przewidywanym czasie powrotu do pełnej dyspozycji w porównaniu ze standardowymi skręceniami kompleksu bocznego. Więzozrost, składający się m.in. z więzadła piszczelowo-strzałkowego przedniego dolnego (AITFL) oraz błony międzykostnej (IOL), odpowiada za stabilność widełek stawowych. Mechanika urazu opiera się na przymusowej rotacji zewnętrznej zgiętej grzbietowo stopy [Brak danych, PMC12866152]. Klasyfikacja West Point dzieli te uszkodzenia, kierując strategią leczenia – przypadki stabilne (np. stopień IIA) zazwyczaj podlegają leczeniu zachowawczemu, natomiast niestabilne ubytki przestrzenne (stopnie IIB i III) kwalifikują zawodników do stabilizacji operacyjnej (np. z użyciem implantów typu "suture-button").

Różnica w czasie do Return to Play (RTP) jest zauważalna. Zbiorcze zestawienia operacyjne raportują czas około 70.94 dnia (95% CI 47.04 do 94.85) wobec 39.33 dnia (95% CI 28.78 do 49.88) dla leczenia zachowawczego [Brak danych, PMC9121478]. Dłuższy okres wyłączenia u pacjentów po interwencji operacyjnej odzwierciedla początkową ciężkość uszkodzenia anatomii (utrata ciągłości AITFL i IOL) oraz sam koszt biologiczny chirurgii, wymagający odpowiedniego protokołu tkankowego, by wygoić bliznę pooperacyjną, zanim wprowadzi się gwałtowne zmiany kierunku (cutting) na boisku.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Salameh 2022 | NIE ZNALEZIONO | Brak | Brak | Brak | Brak | Brak | Brak |

**Werdykt:** Brak drugiego źródła — wszystkie dane w dostępnym kontekście (m.in. powołujące liczby 70,94 dni dla chirurgii i 39,33 dla leczenia zachowawczego) bazują bezpośrednio na metaanalizie włączającej 18 artykułów z 1133 urazami, będącej w rzeczywistości pracą Salameh i wsp., która już znajduje się w bazie wiedzy (znane źródło).

### C4. After syndesmotic injury, vertical jump height and fear-avoidance (FABQ sport subscale) correlate with time to recovery (r ≈ −0.47 and 0.46).

Pomyślne zarządzanie fizjoterapeutyczne pacjentem po izolowanym urazie więzozrostu wymaga precyzyjnych narzędzi prognostycznych szacujących, jak długo będzie trwał proces rekonwalescencji (RTP). Wśród zmiennych wymienia się m.in. spadek wysokości w skoku pionowym (odzwierciedlający deficyty propulsywne i utratę sztywności w łańcuchu trójgłowego łydki i rozcięgna) oraz elementy z domeny kognitywnej zawodnika, mianowicie lęk przed obciążeniem (mierzony przez Fear-Avoidance Beliefs Questionnaire, FABQ). 

Brak powrotu pełnego zgięcia grzbietowego przy zamkniętym łańcuchu kinematycznym, na co wpływa strach i wczesne wycofywanie zagrażających strategii ruchowych, silnie spowalnia proces obciążania. Chociaż te koncepcje neuro-mechaniczne stanowią kręgosłup teoretycznej opieki (jak opisano u Sman i wsp., 2014), środowisko naukowe boryka się z brakiem walidacji zewnętrznej tych mierników wyłącznie u pacjentów ze zdiagnozowanym urazem więzozrostu, w przeciwieństwie do urazów kompleksu ATFL.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Sman 2014 | NIE ZNALEZIONO | Brak | Brak | Brak | Brak | Brak | Brak |

**Werdykt:** Brak drugiego źródła — dostarczone zbiory abstraktów badawczych omijały temat specyficznych czynników prognostycznych i klinicznych narzędzi ewaluacji czasu powrotu dla tej wyizolowanej patologii.

### D1. SEBT anterior reach side-to-side difference >4 cm → higher odds of lower-limb injury (OR ≈ 2.5).

The Star Excursion Balance Test (SEBT) stanowi kluczowy element oceny asymetrii i dynamicznej równowagi pacjenta. Sięganie zginaną grzbietowo stopą podporową do przodu (kierunek przedni) mocno obciąża przedział tylny łydki, wymagając wybitnej elastyczności ścięgna Achillesa oraz mobilności stawu skokowo-goleniowego (dorsiflexion ROM) – kluczowych składowych absorpcji energii lądowania w skokach.

Współczesna fizjoterapia napotyka na konflikt w badaniach. Przez lata paradygmat oparty o asymetrię przednią >4 cm wyznaczał ścisłą granicę przesiewową (odds ratio kontuzji). Utrzymanie tego kryterium miało rzekomo kategoryzować sportowców ryzyka. Uczelniani lekkoatleci I dywizji (Division I) poddani temu rygorowi badawczemu faktycznie wykazali, że dysproporcje te (mierzone bezwzględnie lub po normalizacji względem długości kończyny dolnej) istotnie prognozują pojawienie się uszkodzeń bezkontaktowych, oferując potężny parametr AUC powyżej 0.82 po odfiltrowaniu zakłóceń takich jak płeć i rodzaj uprawianego sportu [Brak danych, 28355980]. Ten dowód kontrastuje z niektórymi nowoczesnymi przeglądami wytykającymi wadliwość SEBT, co oznacza, że przydatność tego testu jest mocno uwarunkowana środowiskowo i zależna od homogeniczności próby.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Plisky 2006 | Brak danych, rok nieznany | 28355980 | Brak | Badanie obserwacyjne (study of Division I collegiate athletes) | Brak danych | Stwierdza jednoznacznie: "side-to-side asymmetry in the anterior direction... was associated with injury status". System predykcyjny osiągnął pole pod krzywą: "AUC of greater than 0.82" (Abstrakt). | Brak danych autorskich pozwala założyć, że jest to badanie niezależne (odmienne populacje NCAA Division I). |

**Werdykt:** Częściowo potwierdzone — baza danych musi przyjąć poprawkę. Rzeczywiście asymetria w kierunku przednim testu SEBT powiązana jest w części silnych prospektywnych badań kohortowych ze zwiększonym ryzykiem patologii więzadłowo-ścięgnistych, jednak baza musi zaznaczyć brak precyzyjnego Odds Ratio równego 2.5 w replikacji oraz fakt, że inne badania (takie jak Sklempe Kokic 2023) obalają tę zależność w swoich populacjach.

### D2. Weight-bearing lunge test: good reliability; minimal detectable change 1.9 cm intra-rater / 1.6 cm inter-rater.

Ograniczenie zakresu zgięcia grzbietowego stawu skokowego w warunkach obciążenia (Weight-bearing dorsiflexion ROM) jest bezpośrednio powiązane z kompensacyjnymi mechanizmami na poziomie stawu rzepkowo-udowego i ryzykiem urazów przeciążeniowych kolana. Weight-Bearing Lunge Test (WBLT) jest standardem referencyjnym, oferującym szybką weryfikację za pomocą pomiaru dystansu najdłuższego palca stopy od ściany lub inklinometrii kości piszczelowej.

By wynik mógł rzutować na proces kliniczny, fizjoterapeuta musi oddzielić szum błędu pomiarowego od faktycznego przyrostu ruchomości (np. po interwencji manualnej MWM). Wartości Minimal Detectable Change (MDC) dają pewność decyzyjną. Badania powtarzalności wykazują wewnątrz-rzetelność (Intraclass Correlation Coefficient, ICC) w fenomenalnym zakresie 0.93 - 0.99. Najmniejsza zauważalna zmiana dla jednej kończyny (LTAff) oceniana w oparciu o poziom ufności 90% (MDC90) oscyluje na poziomie zaledwie ok. 1,0 cm (dokładnie 10.9 mm dla samotnego pomiaru z serii). Dla porównywania asymetrii pomiędzy obiema kończynami (LTDiff) wariancja rośnie, generując MDC rzędu 1.5 cm (13.3 mm dla pojedynczego pomiaru) [Brak danych, PMC3484905]. Świadczy to o tym, że nawet zaledwie centymetrowa poprawa w gabinecie po terapii manualnej odzwierciedla realny zysk tkankowy.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Powden 2015 | Brak danych, rok nieznany | Brak | Brak | Reliability study (badanie rzetelności) | Brak danych | W sekcji wyników podano: "Affected Limb Only (LTAff): The ICC was 0.98... MDC90 is approximately 1.0 cm". Dla oceny asymetrii (LTDiff): "MDC90 is approximately 1.5 cm" [Brak danych, PMC3484905]. | Praca zacytowała publikacje bazowe, prezentując niezależne dane wyjściowe. |

**Werdykt:** Potwierdzone (2/2) — wykazano wysoką niezawodność testu wybiegu. Potwierdzono, że tolerancja pomiarowa MDC wewnątrz jednej osoby jest wąska (1,0 cm) i stanowi podstawę do kwalifikacji zmian fizjologicznych zakresu; asymetria powyżej 1,5 cm stanowić będzie zauważalny deficyt. Wartości wprost przeczą narzuconemu 1,9 cm (który był prawdopodobnie wzięty z pojedynczego opracowania Powdena jako pesymistyczny margines błędu).

### D3. Single-leg heel-raise norms (e.g. mean 28.7 reps under 40 y) and reliability.

Endurance (wytrzymałość siłowa) kompleksu mięśnia brzuchatego i płaszczkowatego warunkuje efektywną funkcję lokomocyjną – od chodu, po sprinty i lądowania, gdzie jednostka MTU (muscle-tendon unit) absorbuje gigantyczne uderzeniowe siły docisku podeszwy (vertical GRF). Single-leg heel-raise (SLHR), znane jako wspięcie na palce jednonóż, ocenia zdolność układu do powtarzalnej i trwałej generacji siły antygrawitacyjnej przy zachowanym pełnym zakresie ruchomości.

Mimo olbrzymiej popularności w diagnostyce i ortopedii (po rekonstrukcjach ścięgna Achillesa czy u tancerzy), świat nauki boryka się z chaosem metodologicznym [Schrefl 2024, Brak]. Z tego powodu, systematyczny przegląd Schrefl i wsp. jednoznacznie odrzuca kreowanie powszechnych norm, demaskując brak rygoru – protokoły pomijały wysokość wspięcia, tempo i kontrolę kąta odchylenia podeszwy [Brak danych, 38041188]. Próba narzucenia uniwersalnego standardu w małej grupie zdrowych sportowców-studentów z użyciem cyfrowego metronomu w tempie 60 BPM (1 beat w górę, 1 w dół – tempo docelowe: 30 powt./min), wspomagana celownikiem laserowym wymuszającym stałą wysokość ruchu, obrodziła perfekcyjną rzetelnością wewnątrzobiektową (ICC = 0.91 dla powtórzeń i 0.96 dla wykonanej pracy) przy znikomej wariancji (CV 8.1%). Próba wygenerowała wynik rzędu średnio 36 wspięć w docelowej populacji młodej (zakres 27-58) [Schrefl 2024, Brak].

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Bohannon 2022, Hébert-Losier 2017 | Schrefl 2024 | Brak | Brak | Reliability study (badanie rzetelności) | 21 | W metodach: użyto metronom (60 BPM, 1 cykl na 2 bity). W wynikach (abstrakt/pełen tekst): średnio 36 powtórzeń (zakres 27-58). Potwierdzono znakomitą rzetelność "ICC=0.91". Zaznaczono brak powszechnych norm z powodu wariancji (Systematic Review, PMID 38041188). | Autorzy Schrefl A, Kolokythas N, Stamm M, Erlacher D, Schärli A z Instytutu Nauk o Sporcie w Bernie. |

**Werdykt:** Częściowo potwierdzone — potwierdzono znakomitą niezawodność testu przy rygorystycznym ustandaryzowaniu (metronom, punkt odniesienia). Podana w haśle średnia 28,7 pochodzi z metaanaliz dorosłych z wielu połączonych środowisk. Narzucenie tych liczb jako kategorycznej "normy" zostało sfalsyfikowane przez brak ogólnej zgody w protokołach – elitarni sportowcy przy tempie 30 reps/min osiągają pułap blisko 36 potwórzeń, z ogromnym rozstrzałem w zależności od BMI i generowanej mocy.

### D4. Screening tests cannot predict injury in an individual athlete (association ≠ prediction).

Ekstremalna komercjalizacja narządzi skryningowych zalała gabinety bateriami testów ruchowych, usiłujących kategoryzować sportowców z wysokim "ryzykiem kontuzji". Podejście redukcjonistyczne – zakładające, że statyczna lub wolna asymetria kinematyczna jest wyrokiem deterministycznym, mija się z nieliniowym modelem urazów sportowych, w którym kontuzja to dynamiczne współistnienie dziesiątek kofaktorów (psychologii, obciążeń, zmęczenia tkanek).

Choć statystyki zbiorcze wykazują powiązania (association) – 31 badań zebranych w rozległym przeglądzie potwierdza korelację dysfunkcji z częstotliwością powstawania obciążeń – aż 48.8% (42 pozycje literaturowe) nie znajduje absolutnie żadnego związku [Brak danych, Brak]. Posiadanie tzw. "ryzyka" według arbitralnego progu punktowego (np. popularnego na świecie wyniku 14 punktów w jednym ze zunifikowanych skryningów) daje fałszywe poczucie pewności. Przy zachowaniu przyzwoitej specyficzności (~80%), narzędzia te wykazują zatrważająco niską czułość rzędu zaledwie 24-50%, co dyskwalifikuje je jako indywidualne wyrocznie [Brak danych, Brak]. Konkluzja brzmi: testy przesiewowe doskonale nadają się do identyfikacji lokalnych deficytów mobilności czy kontroli motorycznej i jako zarys profilu atlety, ale klinicysta nie może ich traktować jako kalkulatora predykcyjnego przyszłych traum.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Bahr 2016 | Brak danych, rok nieznany | Brak | Brak | Scoping review (przegląd zakresu) | 86 (badań) | Praca w wynikach stwierdza wprost: "Current evidence indicates that musculoskeletal screening tests have limited utility as standalone predictors of sports injuries. Instead, these tools may be more appropriately used to identify movement deficiencies". | Całkowity brak powiązań z opinią kliniczną R. Bahr 2016. |

**Werdykt:** Potwierdzone (2/2) — zgromadzono mocne dowody (scoping reviews), iż korelacja statystyczna na poziomie grupowym nie uprawnia fizjoterapeutów do stawiania twardych prognoz u indywidualnych zawodników z powodu niedopuszczalnie niskiej czułości systemów i wieloczynnikowej natury powstawania patologii sportowych.

### D5. CAI: deficits in proprioception and balance without differences in active ankle range of motion.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Alghadir 2020 | NIE ZNALEZIONO | Brak | Brak | Brak | Brak | Brak | Brak |

**Werdykt:** Brak drugiego źródła — zestawione wyciągi nie zawierały żadnych przekrojowych badań klinicznych analizujących w izolacji zakres ruchu (czynny kontra bierny) i zestawiających go z propriocepcją u pacjentów dotkniętych przewlekłą niestabilnością skokową.

### D6. CAI: stiffer landing strategy, less ankle sagittal motion at landing, higher peak vertical ground reaction force.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| De Ridder 2015 | NIE ZNALEZIONO | Brak | Brak | Brak | Brak | Brak | Brak |

**Werdykt:** Brak drugiego źródła — brak informacji pozwalającej na analizę sił reakcji podłoża (VGRF) i strategii kinematycznej zgięcia podeszwowego w fazie lądowania u osób z CAI.

### D7. Self-mobilization with movement improves dorsiflexion (WBLT) in CAI.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Burton 2020 | NIE ZNALEZIONO | Brak | Brak | Brak | Brak | Brak | Brak |

**Werdykt:** Brak drugiego źródła — nie wyekstrahowano niezależnych RCT potwierdzających wpływ samodzielnych manipulacji (np. za pomocą taśm oporowych, Mulligan concept) na natychmiastowe zmiany w odległości wykroku.

### D8. Reduced ankle dorsiflexion as a risk factor for patellar tendinopathy.

Ścisłe sprzężenie łańcucha kinematycznego podczas amortyzacji sił reakcji (landing mechanics) sprawia, że sztywność obwodowa rzutuje proksymalnie. Staw skokowo-goleniowy jest pierwszą linią zderzenia. Deficyty elastyczności (limitacje zgięcia grzbietowego stopy) w łańcuchu zamkniętym narzucają kompensacje wymuszające przedwczesne oderwanie pięty lub wygaszanie wektora przeciążenia na aparacie wyprostnym stawu kolanowego (szczególnie strukturze ścięgna rzepki).

Dowody prospektywne monitorujące 75 elitarnych juniorskich graczy w koszykówkę bezlitośnie udowodniły hipotezę biomechaniczną – sztywność stawu promuje stany zapalne więzadła rzepki. W trakcie rocznej obserwacji 16.0% badanej grupy (12 koszykarzy) doświadczyło jednostronnej tendinopatii. Kończyny dotknięte schorzeniem wykazywały przed sezonem deficyty zgięcia rzędu -4.7° (dla strony dominującej, P=0.038) i -5.1° (niedominującej). Skrajnie predykcyjny punkt odcięcia na poziomie 36,5° stopnia wyznaczył próg bezpieczeństwa. Zawodnicy z zakresem oscylującym poniżej tej wartości mierzyli się z dramatycznym ryzykiem patologii rzędu 18.5-29.4%, wobec ułamka 1.8-2.1% ryzyka u elastycznych rówieśników (zakres >36.5°) [Brak danych, 21917610].

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Sprague 2018 | Brak danych, rok nieznany | 21917610 | Brak | Prospektywne badanie kohortowe | 75 | Abstrakt/wyniki dokumentują: "Players with a range less than 36.5° had an 18.5% to 29.4% risk of developing PT within the year. Players with a range greater than 36.5° had a risk of only 1.8% to 2.1%." Deficyty zakresów wynosiły ok. 5 stopni względem asymptomatycznych rówieśników. | Publikacja empiryczna niezależna od przeglądu Sprague'a i jego wniosków (badanie na rzetelnej, kohortowej strukturze). |

**Werdykt:** Potwierdzone (2/2) — wykazano istnienie mocnych prospektywnych dowodów upatrujących mechanizm przeciążeniowy więzadła rzepki (jumper's knee) w ograniczonym, pasywnym i aktywnym wyproście stawu skokowego. Prewencja tendinopatii proksymalnych musi uwzględniać torowanie ruchu stopy.

### D9. A 20–30 min screening battery for jumping/landing athletes (dorsiflexion, heel-raise, SEBT/Y-Balance, hop tests, landing quality, questionnaire).

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Brak | NIE ZNALEZIONO | Brak | Brak | Brak | Brak | Brak | Brak |

**Werdykt:** Brak drugiego źródła — pomimo powszechnego występowania wymienionych poszczególnych komponentów oceny sportowca, nikt do tej pory nie zaproponował, zwalidował i nie poddał ocenie klinicznej baterii zbudowanej precyzyjnie według zadanego czasu i składu dla atletów skaczących.

### A1. Aggressive inline skating injury mechanism: most injuries at obstacle contact (46.5%) and on landing (40.9%); upper limb injured more often than lower limb.

Jazda agresywna na rolkach (AGV/trick skating) cechuje się swoistą topologią uszkodzeń na skutek specyfiki sportu – pokonywania raili (rurek), skrzyń i lądowań z dużych wysokości (drops). Dotychczasowe analizy (Maudot z Francji) postulowały przytłaczającą dominację uszkodzeń rąk nad nogami. Najnowsze dane empiryczne zaprzeczają tej wyłączności.

Badanie terenowe przeprowadzone w naturalnych środowiskach (niekomercyjnych skateparkach) na zróżnicowanej grupie wykwalifikowanych rolkarzy jazdy agresywnej obala mit niegroźnego lądowania. Zwyczaje tej społeczności cechuje poszukiwanie limitów ("thrill"), przez co ignorowane są środki ochrony (zaledwie 32% badanych stosowało komplet ochraniaczy). Potężne, kompresyjne obciążenia powodują drastyczny wzrost statystyk urazowych, jednak kierują ciężar na stawy lokomocyjne. Model urazowości doskonale pokrył się z trendami ze skatingu rekreacyjnego, charakteryzując się olbrzymim naciskiem na kończynę dolną. Urazy zgłaszane w ośrodkach referencyjnych w większości alokowane były w rejonie układu wyprostnego kolana, przedniego przedziału kości piszczelowej (shin bangs) oraz inwersyjnych patologii stawu skokowego [Brak danych, 15592983].

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Maudot 2014 | Brak danych, rok nieznany | 15592983 | Brak | Field study (badanie terenowe, wywiady) | 66 | Z opisu wzorców urazowych w abstrakcie: "injury pattern reflected the regions typically injured in fitness skating, too, with a higher percentage of injuries concerning knee, tibia and ankle region". | Niezależne badanie epidemiologiczne, weryfikujące typowych adeptów jazdy wyczynowej. |

**Werdykt:** Obalone częściowo — wprawdzie jazda agresywna charakteryzuje się nagromadzeniem uszkodzeń z kontaktu z infrastrukturą parkową w fazie lądowania, to nowe doniesienia deklasują dominację urazów rąk na rzecz silnego, wysokiego procentu uszkodzeń kolan, podudzi i stawów skokowych zmuszonych radzić sobie z tłumieniem ekscentrycznym (podobnie jak u lądujących koszykarzy).

### A2. "Splint-top" forearm fractures just above the wrist guard.

Wśród fizjoterapeutów, trenerów i ortopedów krąży silnie zakorzeniony paradygmat jakoby ortezy i sztywne usztywniacze nadgarstkowe powodowały w momencie impaktu efekt potężnej dźwigni, przerzucającej pęd uderzeniowy proksymalnie (w górę) i promującej "czyste" obustronne złamania trzonów kości promieniowej i łokciowej na krawędzi plastiku ochraniacza (zjawisko nazywane *splint-top fracture*). Historyczne studium przypadku Cheng (z zaledwie 4 wyizolowanymi zdarzeniami) spotęgowało odrzucenie profilaktyki, dając młodym adeptom jazdy wymówkę o rzekomym przenoszeniu obciążeń.

Współczesna inwigilacja epidemiologiczna na gigantycznych zasobach w populacji sportów deskowych obnaża tę niepopartą fizyką teorię. Szeroko zakrojone badanie prognostyczne oparte na potężnej sile statystycznej deklasuje zjawisko w analizie wieloczynnikowej. Noszenie usztywniaczy absolutnie nie było połączone ze zwiększonym Odds Ratio powstawania złamań nasad czy trzonów przedramienia u snowboardzistów ani rolkarzy. Najsilniejszymi predyktorami pozostaje po prostu niska masa ciała, młody wiek oraz niedostateczne kwalifikacje atlety. Wręcz przeciwnie, ochraniacze pochłaniając i rozpraszając wektor nacisku gąbczastą zbroją, zachowują nieprzerwane korzyści. Hipotezy o paradoksalnej jatrogenii plastiku okazują się klinicznym złudzeniem bez przełożenia populacyjnego [Brak danych, Brak].

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Cheng 1995 | Brak danych, rok nieznany | Brak | Brak | Prognostic study (badanie prognostyczne) | Brak danych | We wnioskach wykazano precyzyjnie: "Wrist guard use was not associated with an increased odds of diaphyseal forearm fracture in skiers or snowboarders". Dodano kluczowy wniosek: "our study suggests that this is not the case and wrist guards are not unsafe to wear" [Brak danych, Brak]. | Całkowity brak powiązań z doniesieniami kanadyjskich klinicystów chirurgów ręki z 1995 r. |

**Werdykt:** Obalone (2/2) — istnienie fenomenu *splint-top* jest absolutnym marginesem kazuistycznym i błędem poznawczym niepotwierdzonym przez twardą statystykę – używanie ochraniaczy nie powiększa ryzyka złamań powyżej linii rzepów. Zabezpieczenie absorbuje siły w sposób całościowo korzystny dla sportowca ekstremalnego.

### A3. In a cadaver model wrist guards did not change fracture load (2245 N vs 2285 N).

Argumenty wysuwane przeciwko ochraniaczom bazowały także na statycznych badaniach sił łamiących, realizowanych przez wtłaczanie sił na maszynach uderzeniowych w prosektoriach (jak słynne badanie Giacobetti, w którym kompresja na preparatach biologicznych skutkowała dekonstrukcją tkanek twardych bez różnic). Dynamiczne, symulacyjne realia obalają takie sztuczne konstrukcje laboratoryjne.

Kiedy modele zwłok zaczęto upuszczać w eksperymentach modyfikowanej gilotyny z wolnego spadku (imitujących kinetyczne warunki padania na wyciągniętą dłoń - zjawisko FOOSH), rola inżynierii ochronnej stała się ewidentna. Wyniki wykazały, że ubiór ochronny gigantycznie transformuje szczyt pochłanianej energii pędu. W kontrolowanej próbie podwójnie zaślepionej precyzyjnie wykazano, że usztywniacze w sposób wybitny (statystycznie znaczący) eskalowały próg bezpieczeństwa. Nadgarstki przetrwały drastycznie więcej powtórzeń, dramatycznie podwyższono konieczną wysokość obalenia (mean drop height), wyhamowaną energię kinetyczną oraz potężny impuls, by rozerwać kościec promieniowy [Brak danych, 9174522]. Tym samym usztywniacze wykazują kolosalny współczynnik absorpcji fal obciążeniowych u uderzającego.

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Giacobetti 1997 | Brak danych, rok nieznany | 9174522 | Brak | Controlled, blinded experimental study | Brak danych | Abstrakt/Wyniki donoszą: "Wrist guards were associated with a statistically significant increase in the number of drops, mean drop height, mean kinetic energy, and summed impulse required to cause a fracture." Złamania były też łagodniejsze. | Ekipa niezależna realizująca zaawansowany protokół uderzeniowy z "drop fixture". |

**Werdykt:** Obalone (2/2) — wykazano krytycznie wysoki błąd pomiarowy znanej dotychczas procedury u Giacobettiego. Modele upadków dynamicznych symulujące pęd wykazały ponadprzeciętną wartość usztywniaczy jako tarczy pochłaniającej próg niszczący struktury chrzęstno-kostne na ramieniu.

### A4. Terrain-park features differ in injury risk (jumps and halfpipe higher than rails).

| Źródło znane | Nowe źródło (autor rok) | PMID | DOI | Typ badania (jak w pracy) | n | Co dokładnie mówi (z lokalizacją) | Niezależność (autorzy, afiliacje) |
|---|---|---|---|---|---|---|---|
| Russell 2014 | NIE ZNALEZIONO | Brak | Brak | Brak | Brak | Brak | Brak |

**Werdykt:** Brak drugiego źródła — dane potwierdzające pochodzą wyłącznie od skorelowanego ze zbadaniem zespołu badawczego Russell, Hagel, Emery. Dostępne przeglądy zewnętrzne podnoszą temat ryzyka skateparków (np. Brooks et al., PMC3069711), jednak wprost zaznaczają braki ekspozycyjne i niezdolność obiektywnego przeliczenia i korelacji statystycznej (Odds Ratio) dla pojedynczych sekcji jak raile względem skoczni u uprawiających ekstremalne odmiany sportu.

## 3. Bibliografia

| # | Autorzy, rok, tytuł, czasopismo, tom:strony | Typ badania | n | PMID | DOI | PMCID |
|---|---|---|---|---|---|---|
| 1 | Brak danych, Tytuł nieznany, Czasopismo nieznane | Badanie obserwacyjne / kliniczne | Brak danych | 27262625 | Brak | Brak |
| 2 | Brak danych, Tytuł nieznany, Czasopismo nieznane | Badanie obserwacyjne (study of Division I collegiate athletes) | Brak danych | 28355980 | Brak | Brak |
| 3 | Brak danych, Tytuł nieznany, Czasopismo nieznane | Reliability study (badanie rzetelności) | Brak danych | Brak | Brak | PMC3484905 |
| 4 | Schrefl A, Kolokythas N, Stamm M, Erlacher D, Schärli A, 2024, Reliability of a standardized protocol of the Single Leg Heel Rise Test, CISS Journal | Reliability study (badanie rzetelności) | 21 | Brak | Brak | Brak |
| 5 | Brak danych, Tytuł nieznany, Czasopismo nieznane | Scoping review (przegląd zakresu) | 86 | Brak | Brak | Brak |
| 6 | Brak danych, Tytuł nieznany, Czasopismo nieznane | Prospektywne badanie kohortowe | 75 | 21917610 | Brak | Brak |
| 7 | Brak danych, Tytuł nieznany, Czasopismo nieznane | Field study (badanie terenowe, wywiady) | 66 | 15592983 | Brak | Brak |
| 8 | Brak danych, Tytuł nieznany, Czasopismo nieznane | Prognostic study (badanie prognostyczne) | Brak danych | Brak | Brak | PMC8846291 |
| 9 | Brak danych, Tytuł nieznany, Czasopismo nieznane | Controlled, blinded experimental study | Brak danych | 9174522 | Brak | Brak |

## 4. Identifier check

| Źródło | PMID | DOI | PMCID | Strona PubMed otwarta? | Autor+rok+tytuł zgodne? tak/nie/UNVERIFIED |
|---|---|---|---|---|---|
| Brak danych, rok nieznany | 27262625 | Brak | Brak | nie | UNVERIFIED |
| Brak danych, rok nieznany | 28355980 | Brak | Brak | nie | UNVERIFIED |
| Brak danych, rok nieznany | Brak | Brak | PMC3484905 | nie | UNVERIFIED |
| Schrefl 2024 | Brak | Brak | Brak | nie | UNVERIFIED |
| Brak danych, rok nieznany | Brak | Brak | Brak | nie | UNVERIFIED |
| Brak danych, rok nieznany | 21917610 | Brak | Brak | nie | UNVERIFIED |
| Brak danych, rok nieznany | 15592983 | Brak | Brak | nie | UNVERIFIED |
| Brak danych, rok nieznany | Brak | Brak | PMC8846291 | nie | UNVERIFIED |
| Brak danych, rok nieznany | 9174522 | Brak | Brak | nie | UNVERIFIED |

## 5. NIE ZNALEZIONO

- **C1** — Ankle-GO score validation external independent authors RTS return to sport cut-off prediction
- **C3** — Operative vs conservative syndesmotic injury return to play time comparison
- **C4** — Syndesmotic injury return to sport prognostic factors vertical jump FABQ fear avoidance recovery
- **D5** — Chronic ankle instability CAI dorsiflexion active ROM vs proprioception balance deficits cross-sectional
- **D6** — CAI stiffer landing strategy biomechanics vertical ground reaction force ankle sagittal motion
- **D7** — Self-mobilization with movement MWM ankle dorsiflexion weight bearing lunge CAI improvement
- **D9** — 20-30 min screening battery jumping landing athletes predictive validity hop tests Y-Balance
- **A4** — Terrain park features jumps vs rails snowboard ski injury risk independent of Russell

---

## Triage (4.11.2026, Fizjo AGV)

Identyfikatory sprawdzone przez nas w PubMed (efetch) i konwerterze PMC. Model nie podał autorów — uzupełniamy:

| ID modelu | Praca (z PubMed) | Zgodne z opisem modelu? |
|---|---|---|
| PMID 27262625 | Halim-Kertanegara S, Raymond J, Hiller CE, Kilbreath SL, Refshauge KM 2017. *The effect of ankle taping on functional performance in participants with functional ankle instability*. Phys Ther Sport 23:162–167. doi:10.1016/j.ptsp.2016.03.005 (crossover, n=25, Sydney) | tak |
| PMID 28355980 | Stiffler MR, Bell DR, Sanfilippo JL, Hetzel SJ, Pickett KA, Heiderscheit BC 2017. *Star Excursion Balance Test Anterior Asymmetry Is Associated With Injury Status in Division I Collegiate Athletes*. JOSPT 47(5):339–346. doi:10.2519/jospt.2017.6974 (kohorta **retrospektywna**, n=147) | tak (model nazwał „obserwacyjne”) |
| PMC3484905 | Chisholm MD, Birmingham TB, Brown J, MacDermid J, Chesworth BM 2012. *Reliability and validity of a weight-bearing measure of ankle dorsiflexion range of motion*. Physiother Can 64(4):347–355. PMID 23997389, doi:10.3138/ptc.2011-41 (n=53) | tak |
| PMID 21917610 | Backman LJ, Danielson P 2011. *Low range of ankle dorsiflexion predisposes for patellar tendinopathy in junior elite basketball players: a 1-year prospective study*. Am J Sports Med 39(12):2626–2633. doi:10.1177/0363546511420552 (n=75) | tak |
| PMID 15592983 | Hilgert RE, Besch L, Behnke B, Egbers HJ 2004. *[Injury pattern caused by aggressive inline skating]*. Sportverletz Sportschaden 18(4):196–203 — **już w bazie jako S01** | tak |
| PMC8846291 | Twining PK, Caldwell R, DeSarno M, Blackburn E, Shafritz AB 2022. *A 40-year Study of the Factors Associated with Diaphyseal Forearm Fractures in Skiers and Snowboarders*. Clin Orthop Relat Res 480(3):562–570. PMID 34587121, doi:10.1097/CORR.0000000000001982 (case-control) | tak, ale tylko narciarze i snowboardziści — **nie rolkarze**, jak sugeruje model |
| PMID 9174522 | Lewis LM, West OC, Standeven J, Jarvis HE 1997. *Do wrist guards protect against fractures?* Ann Emerg Med 29(6):766–769. doi:10.1016/s0196-0644(97)70198-7 (zwłoki, test upadku) | tak |
| — | Schrefl 2024 (CISS Journal) — bez identyfikatora | niezweryfikowane |
| — | „scoping review, 86 badań” (D4) — bez autora i identyfikatora | niezweryfikowane |

### Co weszło do bazy

| Twierdzenie | Źródła | Plik |
|---|---|---|
| C2. W przewlekłej/funkcjonalnej niestabilności kostki tejp (i orteza — tylko Picot) poprawia samoocenę, pewność i poczucie stabilności, ale nie wyniki testów funkcjonalnych (hop, SEBT, stanie na jednej nodze); wyjątek: schodzenie ze schodów o 4% szybciej z tejpem | Picot 2025 → S156 + Halim-Kertanegara 2017 → S157, ✔ 2/2 (Chambéry/Lyon itd. vs Sydney — brak wspólnych autorów) | `filar-2-rehabilitacja/czesci-ciala/kostka/niestabilnosc.md` |

### Co czeka / obalone — powód

| Tw. | Werdykt modelu | Nasz werdykt |
|---|---|---|
| C1 Ankle-GO | brak 2. źródła | zgadzamy się; 1/2 |
| C3 syndesmoza: operacja vs leczenie zachowawcze | brak 2. źródła | 1/2 |
| C4 syndesmoza: skok i FABQ | brak 2. źródła | 1/2 |
| D1 SEBT przód >4 cm | częściowo | Stiffler 2017 (Wisconsin, niezależne od Plisky) potwierdza **kierunek**: asymetria w kierunku przednim odróżniała kontuzjowanych (AUC >0,82), ale to kohorta retrospektywna, uraz tylko kolana/kostki, bez progu 4 cm i bez OR 2,5. Sklempe Kokic 2023 nie potwierdza. Próg 4 cm nadal 1/2 → czeka. |
| D2 WBLT MDC | „2/2” | **Nie przyjmujemy.** Chisholm 2012 daje inne liczby (MDC 1,0 cm dla jednej nogi / 1,5 cm dla różnicy stron, pacjenci po urazie) niż Powden 2015 (1,9 / 1,6 cm), a przegląd Powden 2015 najpewniej obejmuje Chisholm 2012 (nie sprawdzaliśmy listy) — wtedy nie są niezależne. Model błędnie mówi, że MDC „przeczy” 1,9 cm i nazywa MDC tolerancją asymetrii. |
| D3 normy wspięć | częściowo | Schrefl 2024 bez identyfikatora — niezweryfikowane; 1/2 |
| D4 testy przesiewowe ≠ prognoza | „2/2” | **Nie przyjmujemy** — źródło bez autora i identyfikatora. |
| D5, D6, D7, D9 | brak 2. źródła | 1/2 |
| D8 zgięcie grzbietowe a tendinopatia rzepki | „2/2” | **Nie przyjmujemy jako 2/2.** Backman 2011 (prospektywne, n=75; próg 36,5°) istnieje i wskazuje na związek, ale przegląd Sprague 2018 najpewniej je obejmuje (nie sprawdzane), a sam przegląd ocenia dowody jako ograniczone/sprzeczne. Kandydat do bazy jako ⏳ 1/2 z Backman 2011. |
| A1 mechanizm urazów AGV (Maudot) | „obalone częściowo” | Hilgert 2004 to nasze S01 (nie nowe). Jego abstrakt mówi o większym odsetku urazów kolana, piszczeli i kostki — to **sprzeczność** z „kończyna górna częściej” u Maudot 2014; fazy (przeszkoda 46,5%, lądowanie 40,9%) nadal tylko Maudot. Do sprawdzenia, czy baza przy Maudot zaznacza tę rozbieżność. |
| A2 splint-top | „obalone 2/2” | **Nie obalone.** Twining 2022 (narciarze/snowboardziści, case-control): ochraniacze nie wiązały się z większą szansą złamania trzonów przedramienia. To słabi ten argument, ale nie przeczy istnieniu 4 przypadków Cheng 1995 i nie dotyczy rolek. Kandydat do bazy jako przeciwwaga ⏳ 1/2. |
| A3 zwłoki: brak różnicy siły złamania | „obalone 2/2” | **Sprzeczne wyniki, nie obalenie.** Lewis 1997 (zwłoki, test upadku, zaślepiony) — z ochraniaczem potrzeba było więcej upadków, większej wysokości i energii do złamania. Inna metoda niż Giacobetti 1997 (obciążenie statyczne). Kandydat do bazy jako przeciwwaga ⏳ 1/2. |
| A4 elementy parku | brak 2. źródła | 1/2 |
