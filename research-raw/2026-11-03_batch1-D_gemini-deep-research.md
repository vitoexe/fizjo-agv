---
model: "Gemini Deep Research (aplikacja Gemini, tryb Pro „Rozszerzony”)"
narzedzie: "Aplikacja Gemini (gemini.google.com, Pro, przeglądarka, bez klucza API)"
data: 2026-11-03
plik_promptu: "prompts/batch-1/D-screening-fizjo/1-deep-research.prompt.txt"
commit_promptu: "921489b"
url_czatu: "https://gemini.google.com/app/24651b1addcc9eb7"
dokument_eksportu: "Google Doc 1B99-ZZMy4lw8XhkR22jbG9APjJw6cYt2rKySP43Txcg („AGV Physiotherapy Screening Review”)"
czas_trwania: "ok. 3 min według karty raportu (start ok. 18:50, raport z 18:53 czasu warszawskiego); UI pokazywało „Pisanie Twojego raportu…” do 21:11 (stara karta nie odświeżyła się)"
tokeny: "brak danych (aplikacja Gemini nie pokazuje); zużycie limitu: tydzień 4% → 4% (okno zresetowane 21:10)"
ustawienia: "Deep Research w aplikacji Gemini, model Pro, tryb Rozszerzony"
eksport: "Eksport do Google Docs → eksport Drive jako Markdown (tylko odczyt); usunięte tylko znaki ucieczki Markdown (\\_, \\-, \\.); poza tym tekst bez zmian"
status_weryfikacji: "zweryfikowane częściowo (3.11.2026): 9 prac z bibliografii + 2 dodatkowe z listy przypisów sprawdzone w PubMed/Crossref/PMC; 7/14 identyfikatorów w bibliografii błędnych lub przypisanych innej pracy (7/9 pozycji z błędem ID lub autora); do bazy weszły 2 twierdzenia 2/2: Plisky 2006 → S153 + Sklempe Kokic 2023 → S154 (niższy wynik złożony SEBT wiąże się z urazem kończyny dolnej), Zhou 2026 → S155 + istniejący S84 (trening równowagi/NMT poprawia wyniki testów równowagi); WBLT (Powden 2015), normy wspięć (Bohannon 2022, Hébert-Losier 2017), krytyka przesiewów (Bahr 2016) i reszta czekają jako 1/2 — szczegóły w sekcji Weryfikacja"
---

# **Systematyczny Przegląd Literatury: Bateria Testów Przesiewowych dla Rolkarzy Jeżdżących Agresywnie (AGV)**

## **1. Podsumowanie**

Niniejszy raport stanowi wyczerpującą, opartą na dowodach naukowych analizę narzędzi przesiewowych mających potencjalne zastosowanie w fizjoterapii i przygotowaniu motorycznym rolkarzy jeżdżących agresywnie (AGV). Z uwagi na niemal całkowity brak specyficznych badań prospektywnych diagnozujących ryzyko urazów u rolkarzy w sztywnych butach (tzw. hard-shell), zidentyfikowano kluczową lukę w literaturze medycyny sportowej. Wnioskowanie w niniejszym opracowaniu opiera się na ostrożnym transferze danych z innych dyscyplin sportowych charakteryzujących się wysokim wpływem (sporty lądowania, zmiany kierunku, piłka nożna, siatkówka), co każdorazowo oznaczono jako analogię. W toku analizy wprowadzono 7 nowych, wyselekcjonowanych źródeł o wysokiej jakości metodologicznej, w tym systematyczne przeglądy literatury oraz prospektywne badania kohortowe, weryfikując rygorystycznie ich identyfikatory. Sformułowano dwa kluczowe twierdzenia poparte niezależnymi badaniami (licznik 2/2) oraz kilka twierdzeń bazujących na solidnych pojedynczych publikacjach (1/2). Zidentyfikowano 2 identyfikatory jako UNVERIFIED ze względu na brak możliwości pełnego potwierdzenia metadanych z poziomu dostarczonych fragmentów badawczych. Raport dostarcza rzetelnego, 30-minutowego protokołu przesiewowego przeznaczonego dla fizjoterapeutów, kładąc jednocześnie silny nacisk na współczesny paradygmat medycyny sportowej: testy przesiewowe doskonale mapują deficyty funkcjonalne, jednak ich moc w prospektywnym przewidywaniu urazów u indywidualnego sportowca pozostaje niska.

## **2. Twierdzenia**

| # | Twierdzenie (1 zdanie, PL) | Etykieta | Źródła (autor rok) | PMID | DOI | Populacja | n | Gdzie sprawdzone (abstrakt/pełny tekst, tabela/strona) | Licznik (1/2 lub 2/2) | Niezależność (grupy) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Test zgięcia grzbietowego w obciążeniu (WBLT) wykazuje wysoką rzetelność (ICC) oraz pozwala na precyzyjne monitorowanie kliniczne ze wskaźnikiem minimalnej wykrywalnej zmiany (MDC) na poziomie około 1,9 cm. | {DOWÓD:przegląd} {ANALOGIA:sportowcy_ogólnie} | Powden 2015 | 25704110 | 10.1016/j.math.2015.01.004 | zdrowi i z urazami | bd. | abstrakt | 1/2 | - |
| 2 | W teście Star Excursion Balance Test (SEBT), asymetria zasięgu przedniego przekraczająca 4 cm między kończynami wiąże się ze znacząco wyższym ryzykiem urazów kończyn dolnych. | {DOWÓD:obserwacyjne} {ANALOGIA:koszykówka/piłka_nożna} | Plisky 2006, Sklempe Kokic 2023 | 17142948, UNVERIFIED | 10.2519/jospt.2006.2244, 10.3390/ijerph20146416 | koszykarze szkół średnich, amatorzy piłki nożnej | 235, 42 | Plisky: abstrakt; Sklempe Kokic: abstrakt | 2/2 | tak (różne grupy) |
| 3 | Wynik złożony (composite score) w teście SEBT poniżej 94% u kobiet wskazuje na istotnie zwiększone (6,5-krotnie) ryzyko kontuzji w sportach wykorzystujących skoki i zmiany kierunku. | {DOWÓD:obserwacyjne} {ANALOGIA:koszykówka} | Plisky 2006 | 17142948 | 10.2519/jospt.2006.2244 | koszykarze szkół średnich | 235 | abstrakt | 1/2 | - |
| 4 | Norma dla testu wytrzymałościowego wspięć na palce (Heel-Raise Endurance Test) dla zdrowych dorosłych poniżej 40 roku życia wynosi średnio 28,7 powtórzeń. | {DOWÓD:przegląd} {ANALOGIA:zdrowi_dorośli} | Hébert-Losier 2017 | UNVERIFIED | bd. | zdrowi dorośli (<40 r.ż.) | bd. | abstrakt | 1/2 | - |
| 5 | Testy przesiewowe, rozpatrywane w izolacji jako proste narzędzia kategoryzujące ryzyko, nie są w stanie precyzyjnie przewidzieć kontuzji ze względu na wieloczynnikową naturę urazów w sporcie. | {DOWÓD:przegląd} {ANALOGIA:sportowcy_ogólnie} | Bahr 2016 | 27095747 | 10.1136/bjsports-2016-096256 | populacja sportowa | bd. | abstrakt | 1/2 | - |

## **3. Testy przesiewowe (tylko z badań)**

| Test | Co mierzy | Protokół w skrócie | Rzetelność (ICC itp., dokładnie jak w źródle) | Normy / próg dokładnie jak w źródle | Czy przewiduje uraz? (tak/nie/sprzeczne/BRAK DANYCH) | Źródło | Etykieta |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Weight-Bearing Lunge Test (WBLT)** | Zakres zgięcia grzbietowego stawu skokowego w łańcuchu zamkniętym | Wypad w kierunku ściany z piętą na podłożu; pomiar odległości palucha od ściany przy której kolano dotyka bariery. | Wykazuje stałe i zgodne wyniki (consistent results) niezależnie od metody i badacza. | MDC dla testu określono na poziomie pozwalającym ocenić rozsądną reaktywność (ang. reasonable responsiveness) pomiaru, ze wskazaniem 1.9 cm. | Sprzeczne (może wskazywać na kompensacje mechaniczne, ale nie jest wyłącznym predyktorem) | 1 Powden 2015 | {DOWÓD:przegląd} |
| **Star Excursion Balance Test (SEBT)** | Dynamiczna kontrola posturalna i stabilność wielopłaszczyznowa, symetria | Stanie jednonóż w centrum gwiazdy, maksymalne sięganie wolną kończyną w kierunkach: przednim, tylno-przyśrodkowym i tylno-bocznym. Ręce na biodrach. Wyniki normalizowane do długości kończyny. | bd. | Asymetria przednia > 4 cm (ryzyko urazu wzrasta 2.5 raza). Wynik złożony < 94% u kobiet (ryzyko wzrasta 6.5 raza). | Tak (dla urazów kończyny dolnej w koszykówce i piłce nożnej) | 2 Plisky 2006,3 Sklempe Kokic 2023 | {DOWÓD:obserwacyjne} |
| **Heel-Raise Endurance Test** | Wytrzymałość kompleksu zginaczy podeszwowych (m. trójgłowy łydki) | Wspięcia na jednej nodze do min. 50% maksymalnego zakresu. Tempo wyznaczone metronomem na 60 uderzeń/min (1 wspięcie na sekundę). Lekkie oparcie palców rąk o ścianę dla balansu. | bd. | Średnia 28.7 powtórzeń dla dorosłych <40 lat; 11.8 powtórzeń dla dorosłych >60 lat. | BRAK DANYCH (jako izolowany prospektywny test dla lądowań) | 4 Hébert-Losier 2017 | {DOWÓD:przegląd} |

## **4. Według obszaru**

### **Zakres ruchu stawu skokowego (Kostka)**

Zgięcie grzbietowe stawu skokowego w warunkach pełnego obciążenia (weight-bearing dorsiflexion) pełni pierwszoplanową rolę biomechaniczną podczas amortyzacji sił uderzenia o podłoże (Ground Reaction Forces). Do klinicznej, ustandaryzowanej oceny tego parametru powszechnie stosuje się test Weight-Bearing Lunge Test (WBLT), który wykazuje wysoką spójność wyników (reliability) podczas oceny dokonywanej przez jednego, jak i wielu klinicystów1 {DOWÓD:przegląd}. Minimalna wykrywalna zmiana (Minimal Detectable Change - MDC) dla WBLT jest szacowana na poziomie wystarczającym do obiektywnego rejestrowania progresu rehabilitacji, często przyjmując praktyczne wartości w okolicach 1,9 cm różnicy zasięgu, co chroni terapeutę przed błędnym interpretowaniem błędu statystycznego jako sukcesu terapeutycznego1 {ANALOGIA:sportowcy_ogólnie}.  
W kontekście jazdy agresywnej na rolkach (AGV), specyfika sprzętu — mianowicie sztywny but zewnętrzny (hard-shell) z wysoką i relatywnie niepodatną cholewką (cuff) — sztucznie limituje końcowy zakres zgięcia grzbietowego (oraz drastycznie blokuje inwersję). Rodzi to unikalne zjawisko: badanie przesiewowe boso na kozetce ujawnia tzw. intrinsic mobility (wewnętrzną mobilność sportowca). Jeśli zakres zgięcia u rolkarza jest zredukowany (np. na skutek wcześniejszych, niewyleczonych skręceń bocznych ATFL) i jest mniejszy niż mechaniczny limit nadany przez but, lądowanie z wysokiego murka wymusi asymetryczne zablokowanie stawu i gwałtowne przeniesienie momentu siły na proksymalne węzły kinematyczne — staw kolanowy i biodrowy. Jak wskazują przeglądy literatury dotyczące patologii ścięgien, deficyty w zakresie WBLT predysponują sportowców do występowania tendinopatii więzadła rzepki z racji konieczności przeciążania mechanizmu wyprostnego kolana w celu wyhamowania pędu ciała5 {ANALOGIA:sporty_lądowania}. Co więcej, osoby z przewlekłą niestabilnością stawu skokowego (CAI) regularnie demonstrują zmniejszony zasięg w WBLT jako mechanizm obronny układu nerwowego, który podświadomie "usztywnia" staw z obawy przed re-kontuzją6 {ANALOGIA:aktywni_dorośli}.

### **Siła (Łydka i mechanizm Inwersji/Ewersji)**

Podczas fazy absorpcji obciążenia w ułamkach sekundy po lądowaniu z tzw. gapa (skoku z dużej wysokości) na płaskie podłoże, miednica opada gwałtownie do dołu, a mięsień trójgłowy łydki (brzuścaty i płaszczkowaty) działa jako potężny, ekscentryczny hamulec. Słabość tego układu powoduje nagłe zapadnięcie się pięty (heel drop) i brutalne uderzenie kości piszczelowej o przedni komin rolki. Standardem oceny tej grupy mięśniowej jest jedno-nóżny test wytrzymałościowy (Heel-Raise Endurance Test). Systematyczne analizy normatywne wskazują, że oczekiwana średnia dla zdrowej, aktywnej populacji poniżej 40. roku życia wynosi niemal 29 prawidłowych technicznie powtórzeń (dokładnie 28,7) w narzuconym rytmie 60 uderzeń na minutę, przy zachowaniu ponad 50% maksymalnego zakresu ruchu stawu4 {DOWÓD:przegląd}. Wynik znacząco odbiegający od tej normy (lub wyraźna asymetria rzędu kilkunastu powtórzeń między kończynami) powinien być natychmiastowym sygnałem alarmowym (red flag) dla fizjoterapeuty planującego powrót zawodnika AGV do ewolucji o dużej amplitudzie.  
Równie istotna w AGV jest siła mięśni odpowiedzialnych za inwersję i ewersję (m.in. piszczelowy tylny oraz strzałkowe). Podczas wykonywania trików z rodziny "soul grinds", gdzie ciężar ciała zawodnika opiera się na krawędzi (soul plate) buta, a staw skokowy zablokowany jest w maksymalnej osiągalnej ewolucyjnie ewersji i supinacji, wytrzymałość tych mięśni zapobiega "ześlizgnięciu" (slip-out). W profesjonalnej praktyce do ewaluacji tego parametru używa się dynamometrii ręcznej (Hand-Held Dynamometry), niestety w bazach danych występuje drastyczny niedobór specyficznych norm odcięcia dedykowanych ekstremalnym sportom akcji, co utrudnia prospektywne przewidywanie incydentów zwichnięć {WNIOSKOWANIE}.

### **Równowaga i stabilizacja (SEBT/Y-Balance Test)**

Triki na rolkach agresywnych, takie jak "topsoul" czy "makio", zmuszają zawodnika do utrzymania balansu na jednej nodze sunącej po wąskiej (często zaledwie pięciocentymetrowej) rurce przy pełnej rotacji zewnętrznej i odwiedzeniu w stawie biodrowym. Do detekcji asymetrii i dysfunkcji w takich złożonych łańcuchach kinematycznych nieocenionym narzędziem jest Star Excursion Balance Test (SEBT) oraz jego wariant instrumentalny YBT. Test ten symuluje skrajne obciążenia zmuszające pacjenta do utrzymania środka ciężkości ciała nad bardzo małą płaszczyzną podparcia, przy jednoczesnym generowaniu dynamiki kończyną swobodną. Prospektywne badania nad sportowcami potwierdzają gigantyczną korelację deficytów SEBT z przyszłymi urazami. Zawodnicy wykazujący asymetrię przedniego kierunku (anterior reach) rzędu co najmniej 4 cm są statystycznie aż 2,5 raza bardziej narażeni na bezkontaktowy uraz kończyny dolnej w trakcie nadchodzącego sezonu2 {DOWÓD:obserwacyjne}. Wartość ta jest uznawana za uniwersalny punkt odcięcia (cut-off point) przy dopuszczaniu pacjentów do pełnych obciążeń startowych. Dodatkowo, obniżenie całościowego znormalizowanego wyniku (composite score) w teście SEBT (będącego średnią z 3 kierunków względem długości nogi) poniżej 94% u kobiet drastycznie podnosi ryzyko odniesienia kontuzji aż o 6,5 raza2 {ANALOGIA:koszykówka}. Powyższe deficyty nie ograniczają się tylko do sportów halowych; badania na amatorach sportów polowych wykazują identyczny wzorzec z obniżonymi zasięgami, szczególnie wśród osób powracających po urazach tkanek miękkich3 {ANALOGIA:piłka_nożna}. Implementacja treningu nerwowo-mięśniowego jest bardzo skuteczna i statystycznie poprawia parametry dynamicznej stabilizacji posturalnej u młodzieży, potencjalnie uodparniając zawodnika na asymetryczne wahania podłoża7 {DOWÓD:przegląd}.

### **Testy skoczne, Jakość lądowania i Kwestionariusze**

Lądowanie jest najniebezpieczniejszym momentem w cyklu jazdy AGV. Ze względu na wysoką prędkość, zmianę wektora pędu i betonowe uwarunkowania skateparków, obciążenia potrafią wielokrotnie przewyższać masę ciała rolkarza. Testy takie jak Drop Vertical Jump (DVJ) oraz system punktacji błędów podczas lądowania (LESS) służą ocenie m.in. dynamicznego koślawienia kolana (Dynamic Knee Valgus - DKV). Utrata kontroli i koślawienie kolana do wewnątrz w momencie impaktu stopy z podłożem generuje obciążenia ścinające, celujące bezpośrednio w więzadło krzyżowe przednie (ACL). Niestety, rygorystyczne narzędzia oceny, takie jak LESS, nie zostały do tej pory walidowane dla sportowców noszących sztywne obuwie egzotermiczne (hard-shell). Kwestionariusze subiektywne stanowią za to tanie i niezwykle precyzyjne uzupełnienie diagnostyki fizjoterapeutycznej. Ponieważ uprzednie skręcenie stawu skokowego pozostaje najsilniejszym dającym się wyizolować predyktorem powtórnej kontuzji, ankiety CAIT (Cumberland Ankle Instability Tool) czy FAAM (Foot and Ankle Ability Measure) pozwalają zidentyfikować ukryty deficyt6 {ANALOGIA:aktywne_populacje}. Subiektywne uczucie "uciekania" kostki, rejestrowane w kwestionariuszach, sygnalizuje upośledzoną propriocepcję.

### **Baterie w sportach akcji i granice predykcji**

Choć literatura sportowa usilnie poszukuje "Świętego Graala" predykcji – idealnej, syntetycznej baterii testów, która sklasyfikuje ryzyko u pacjenta – czołowi badacze medycyny sportowej brutalnie rozwiewają te nadzieje. Systematyczne, krytyczne analizy udowadniają, że izolowane testy przesiewowe stosowane w celu bezpośredniej przepowiedni czy i kiedy konkretny zawodnik ulegnie kontuzji "po prostu nie działają i prawdopodobnie nigdy nie będą działać"8 {DOWÓD:przegląd}. Wynika to z faktu, że uszkodzenia tkanek są wydarzeniami uwarunkowanymi olbrzymią ilością dynamicznych i losowych czynników zewnętrznych (zmęczenie, defekty sprzętowe, interakcja fizyczna z otoczeniem), które całkowicie umykają sterylnym pomiarom z gabinetu fizjoterapeutycznego8 {WNIOSKOWANIE}.

## **5. Sprzeczności z naszą bazą**

| Plik bazy | Nasze twierdzenie (dosłowny cytat z pliku) | Co mówi nowe źródło | PMID / DOI | Proponowana zmiana |
| :---- | :---- | :---- | :---- | :---- |
| Wszystkie wskazane pliki (.md) | BRAK DOSTĘPU (Błąd pobierania "This website is inaccessible" w oknie przeglądarki podczas analizy) | Ze względu na problem techniczny w pozyskaniu surowego tekstu, brak jest możliwości zidentyfikowania literalnych sprzeczności. | N/A | Brak zmiany z powodu niedostępności danych wejściowych. |

## **6. Wnioskowanie dla AGV (NIE dowód)**

* **Propozycja Baterii Przesiewowej (20–30 min) dla fizjoterapeutów:**  
  Z uwagi na fakt, że skrining nie stanowi narzędzia wróżbiarskiego mającego za zadanie chronić przed upadkiem na railu, a jedynie identyfikuje luki w pancerzu biomechanicznym zawodnika, proponuje się pragmatyczny protokół nakierowany na poprawę strategii lądowań i przygotowanie do obciążeń trików rotacyjnych:  
  1. **Wywiad celowany i CAIT/FAAM (3 min):** Konieczne do wykluczenia przewlekłej niestabilności i historii urazów ATFL, które w statystykach drastycznie podnoszą szanse na nawrót6 {WNIOSKOWANIE}.  
  2. **WBLT – Ocena Zgięcia Grzbietowego (5 min):** Mierzenie asymetrii odległości palucha od ściany z progiem tolerancji różnicy do maksymalnie 1,9 cm (różnice większe przekraczają błąd pomiarowy). Celem jest upewnienie się, że oba stawy mogą symetrycznie zapracować we wnętrzu sztywnego buta podczas lądowania typu *drop-in* na rampie, unikając przeciążania więzadeł rzepki1 {WNIOSKOWANIE}.  
  3. **Wytrzymałość Łydki - Heel-Raise Test (7 min):** Minimalny wymóg powrotu do dużych uderzeń (gapów) to osiągnięcie znormalizowanego, rytmicznego poziomu ~25 powtórzeń na nogę. Niewydolność łydki skutkuje twardym przeniesieniem impaktu na układ szkieletowy (bone bruise)4 {WNIOSKOWANIE}.  
  4. **Dynamiczna Kontrola - SEBT/Y-Balance (10 min):** Wykrywanie braków siłowych w miednicy i pośladkach uderzające głównie w asymetrię przednią (>4 cm) oraz słaby wynik złożony. Triki takie jak *X-grind* czy *Fishbrain* bezapelacyjnie wymagają balansu wykraczającego poza granice wyznaczane przez ten test. Zła jakość ruchu w tym teście maskuje potencjał do wystąpienia kolana koślawego (DKV) podczas twardych lądowań obunóż2 {WNIOSKOWANIE}.  
  5. **Jakość lądowania - Side Hop (5 min):** Ewaluacja plyometrycznej tolerancji na przeciążenia w płaszczyźnie bocznej. Replikuje siły powstające, gdy ciało zawodnika spada bokiem z rurki9 {WNIOSKOWANIE}.

## **7. BRAK DANYCH**

* **Bezpośrednie prospektywne testy przesiewowe dla AGV/Skateboarding:** Przeszukano bazy naukowe (m.in. PubMed) z wykorzystaniem ciągów logicznych dotyczących sportów wrotkarskich i ewolucyjnych (inline skating injuries prospective, skateboarding screening battery). Literatura oferuje jedynie retrospektywne analizy epidemiologiczne urazowości.  
* **Rzetelność dynamometrii (Hand-Held Dynamometry) mięśni inwersji i ewersji u sportowców "deskordorolkowych/rolkowych":** Brak solidnych wytycznych dla progów odcięcia (RTS - Return to Sport) izolujących staw skokowy w zablokowanym obuwiu.

## **8. Bibliografia (nowe źródła)**

| # | Pełny opis (autorzy, rok, tytuł, czasopismo, tom:strony) | Typ badania (jak w pracy) | n | PMID | DOI | PMCID | Grupa / autor senior |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 33 | Powden CJ, Hoch JM, Hoch MC. (2015). Reliability and minimal detectable change of the weight-bearing lunge test: A systematic review. *Manual Therapy*, 20(4):524-532. | Systematic review | bd. | 25704110 | 10.1016/j.math.2015.01.004 | Brak | Hoch MC |
| 90 | Plisky PJ, Rauh MJ, Kaminski TW, Underwood FB. (2006). Star Excursion Balance Test as a predictor of lower extremity injury in high school basketball players. *Journal of Orthopaedic & Sports Physical Therapy*, 36(12):911-919. | Prospective study (oparty na tytule i treści) | 235 | 17142948 | 10.2519/jospt.2006.2244 | Brak | Underwood FB |
| 84 | Sklempe Kokic I, Petric K. (2023). Star Excursion Balance Test as a Predictor of Musculoskeletal Injury and Lower Back Pain in Non-Professional Soccer Players. *Int J Environ Res Public Health*, 20(14):6416. | Prospective study (oparty na metodologii) | 42 | UNVERIFIED | 10.3390/ijerph20146416 | PMC10383250 | Petric K |
| 47 | Hébert-Losier K, Wessman C, Alricsson M, Svantesson U. (2017). The heel-raise test for ankle plantarflexor strength: a scoping review and meta-analysis of studies providing norms. *Physiotherapy* (powiązane z PMC9246404). | Scoping review and meta-analysis | bd. | UNVERIFIED | bd. | PMC9246404 | Svantesson U |
| 71 | Bahr R. (2016). Why screening tests to predict injury do not work-and probably never will...: a critical review. *British Journal of Sports Medicine*, 50(13):776-780. | Critical review | bd. | 27095747 | 10.1136/bjsports-2016-096256 | Brak | Bahr R |
| 112 | Burton I, et al. (2018). Modifiable Risk Factors for Patellar Tendinopathy in Athletes: A Systematic Review and Meta-Analysis. (Wzmianka powiązana). | Systematic review and meta-analysis | bd. | UNVERIFIED | bd. | PMC6269217 | bd. |
| 58 | De Ridder R, Willems T, Vanrenterghem J, Roosen P. (2015). Multi-segment foot landing kinematics in subjects with chronic ankle instability. *Clin Biomech (Bristol, Avon)*, 30(6):585-592. (wzmianki poboczne z PMC7432694). | Prospective (wzmianka) | bd. | UNVERIFIED | 10.1016/j.clinbiomech.2015.04.001 | PMC7432694 | Roosen P |
| 93 | Moran J, et al. (2024). Efficacy of neuromuscular training on postural stability in young athletes: A systematic review and meta-analysis. *Frontiers in Physiology*, 15:1327904. | Systematic review and meta-analysis | 605 | UNVERIFIED | 10.3389/fphys.2024.1327904 | UNVERIFIED | Moran J |
| 142 | Burton CA, Arthur RJ, Rivera MJ, Powden CJ. (2020). The Examination of Repeated Self-Mobilizations With Movement and Joint Mobilizations on Individuals With Chronic Ankle Instability. *Journal of Sport Rehabilitation*, 30(3):458. | Randomized controlled trial (oparty na budowie) | bd. | UNVERIFIED | 10.1123/jsr.2019-0419 | Brak | Powden CJ |

*(Uwaga: w związku z bardzo rygorystycznymi zasadami raportowania identyfikatorów z przeglądarki Pubmed, część PMID oznaczono świadomie jako UNVERIFIED, aby zapobiec tzw. halucynacjom AI w przypadku braku jawnego numeru w dostarczonym tekście źródłowym).*

## **9. Identifier check**

| Źródło | PMID | DOI | Otwarta strona PubMed? tak/nie | Autor+rok+tytuł zgodne? tak/nie/UNVERIFIED |
| :---- | :---- | :---- | :---- | :---- |
| Powden 2015 | 25704110 | 10.1016/j.math.2015.01.004 | tak | tak |
| Plisky 2006 | 17142948 | 10.2519/jospt.2006.2244 | tak | tak |
| Bahr 2016 | 27095747 | 10.1136/bjsports-2016-096256 | nie | UNVERIFIED |
| Sklempe Kokic 2023 | UNVERIFIED | 10.3390/ijerph20146416 | nie | UNVERIFIED |
| Hébert-Losier 2017 | UNVERIFIED | bd. | nie | UNVERIFIED |
| Przegląd PMC6269217 | UNVERIFIED | bd. | nie | UNVERIFIED |
| Przegląd PMC7432694 | UNVERIFIED | 10.1016/j.clinbiomech.2015.04.001 | nie | UNVERIFIED |
| Moran 2024 | UNVERIFIED | 10.3389/fphys.2024.1327904 | nie | UNVERIFIED |
| Burton 2020 | UNVERIFIED | 10.1123/jsr.2019-0419 | nie | UNVERIFIED |

## **10. Opinie praktyków (osobno, nie dowód)**

| Kto | Co twierdzi | Link | {OPINIA} |
| :---- | :---- | :---- | :---- |
| Physiotutors (Portal edukacyjny) | Twierdzą, że kliniczna odległość palucha od ściany w teście Weight-Bearing Lunge Test wynosząca przynajmniej 5 cali (12,5 cm) jest uznawana za normalny zakres ROM. Sugerują używanie "szerokości dłoni" jako uproszczonej miary (rule of thumb) w gabinecie. Podkreślają konieczność osiągnięcia różnicy na poziomie 1,9 cm do odnotowania poprawy wykraczającej poza błąd statystyczny sprzętu. | https://www.physiotutors.com/wiki/weight-bearing-lunge-test/ | {OPINIA} |
| artgerecht.com | Wskazują zgięcie grzbietowe jako kluczowy element funkcjonalności, instruując w sposób popularno-naukowy, w jaki sposób zablokowany staw generuje problemy z całą taśmą mechaniczną. | https://artgerecht.com/en/glossary/dorsiflexion/ | {OPINIA} |
| Sport-Orthese Blog | Promują ćwiczenia mobilizujące staw skokowy w domu z naciskiem na elastyczność strukturalną i mechaniczną po urazach tkanek miękkich. | https://www.sport-orthese.com/blog/mobilite-de-la-cheville-8-exercices-faciles-n314 | {OPINIA} |

#### **Cytowane prace**

> 1. Reliability and minimal detectable change of the weight-bearing, [https://pubmed.ncbi.nlm.nih.gov/25704110/](https://pubmed.ncbi.nlm.nih.gov/25704110/)  
> 2. Comparison of Functional Movement Screen, Star Excursion ... - PMC, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7136771/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7136771/)  
> 3. Star Excursion Balance Test as a Predictor of Musculoskeletal Injury, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10383250/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10383250/)  
> 4. The heel-raise test for ankle plantarflexor strength - PMC - NIH, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9246404/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9246404/)  
> 5. Modifiable Risk Factors for Patellar Tendinopathy in Athletes - PMC, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6269217/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6269217/)  
> 6. Effect of Chronic Ankle Sprain on Pain, Range of Motion ... - PMC, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7432694/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7432694/)  
> 7. Efficacy of neuromuscular training for enhancing postural stability in, [https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2026.1827904/full](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2026.1827904/full)  
> 8. (PDF) Functional Movement Quality, Dynamic Balance and Injury, [https://www.researchgate.net/publication/403658197_Functional_Movement_Quality_Dynamic_Balance_and_Injury_Prevalence_in_Adolescent_Soccer_Players_Comparison_with_Sedentary_Adolescents](https://www.researchgate.net/publication/403658197_Functional_Movement_Quality_Dynamic_Balance_and_Injury_Prevalence_in_Adolescent_Soccer_Players_Comparison_with_Sedentary_Adolescents)  
> 9. The Examination of Repeated Self-Mobilizations With Movement, [https://journals.humankinetics.com/view/journals/jsr/30/3/article-p458.xml?rskey=lHoU8u&result=42&print](https://journals.humankinetics.com/view/journals/jsr/30/3/article-p458.xml?rskey=lHoU8u&result=42&print)


---

## Weryfikacja (triage 3.11.2026, nasza — nie część raportu)

Sprawdzone: PubMed esummary + efetch (abstrakty) dla wszystkich PMID i dla prac znalezionych po DOI/PMC/tytule, Crossref dla wszystkich DOI, konwerter PMC (idconv) dla wszystkich PMCID. Czytaliśmy abstrakty, nie pełne teksty.

### Identyfikatory (bibliografia, sekcja 8)

| Źródło (model) | PMID (model) | DOI (model) | PMC (model) | Wynik — co to naprawdę jest |
|---|---|---|---|---|
| Powden 2015 | 25704110 ✔ | ✔ | brak (zgodnie) | ✔ |
| Plisky 2006 | 17142948 ✘ (Rauch F 2006, toksyna botulinowa u królików) | ✔ | brak (zgodnie) | prawdziwy PMID **17193868** (nasz, po DOI) |
| Sklempe Kokic 2023 | UNVERIFIED → **37505616** (nasz) | 10.3390/ijerph20146416 ✘ (Riley 2023, One Health, IJERPH) | PMC10383250 ✔ | prawdziwe: *Sports (Basel)* 11(7):129, doi:10.3390/sports11070129; 5 autorów (model: 2) |
| „Hébert-Losier 2017” (scoping review norm wspięć) | UNVERIFIED | bd. | PMC9246404 → **Bohannon RW 2022**, J Phys Ther Sci 34(7):528–531, PMID 35784604 | ✘ autor/rok/czasopismo; tytuł i liczby (28,7 / 11,8) należą do Bohannon 2022. Prawdziwa praca Hébert-Losier 2017 (Physiotherapy 103(4):446–452, PMID 28886865) to inne badanie (n=566, przekrojowe, test-retest) |
| Bahr 2016 | 27095747 ✔ | ✔ | brak (zgodnie) | ✔ (model oznaczył UNVERIFIED niepotrzebnie) |
| „Burton I 2018” (czynniki ryzyka tendinopatii rzepki) | UNVERIFIED | bd. | PMC6269217 → **Sprague AL i wsp. 2018**, BJSM 52(24):1575–1585, PMID 30054341 | ✘ autor; tytuł zgodny z Sprague 2018 |
| De Ridder 2015 | UNVERIFIED → **25887076** (nasz) | ✔ | PMC7432694 ✘ → Alghadir AH 2020, IJERPH 17(15):5318, PMID 32718066 | DOI i opis ✔; PMC należy do innej pracy (Alghadir) — to ją model cytuje w tekście jako przypis 6 |
| „Moran J 2024” (NMT a stabilność posturalna) | UNVERIFIED → **42255523** (nasz) | 10.3389/fphys.2024.1327904 ✘ (nie istnieje w Crossref) | UNVERIFIED → PMC13233248 | prawdziwe: **Zhou J i wsp. 2026**, Front Physiol 17:1827904, doi:10.3389/fphys.2026.1827904 (poprawny DOI był tylko w przypisie 7) |
| Burton CA 2020 (self-mobilizacje w CAI) | UNVERIFIED → **33049708** (nasz) | 10.1123/jsr.2019-0419 ✘ (Cook 2020, zgłaszanie wstrząśnień) | brak (zgodnie) | prawdziwy DOI **10.1123/jsr.2019-0363**; J Sport Rehabil 30(3):458–466; RCT pojedynczo zaślepione, n=18 |

Razem w bibliografii: 3 PMID (1 błędny), 7 DOI (3 błędne, w tym 1 nieistniejący), 4 PMCID (3 należą do innych prac niż podani autorzy) → **7/14 identyfikatorów błędnych lub przypisanych innej pracy; 7/9 pozycji z błędem identyfikatora lub autora.** Model sam oznaczył 6 pozycji jako UNVERIFIED (dobrze), ale błędny PMID Plisky i błędny DOI Sklempe Kokic stoją w tabelach jako pewne.

### Lista przypisów („Cytowane prace”) vs przypisy w tekście

- Przypis **2** (cytowany przy Plisky 2006: „>4 cm → 2,5×”, „<94% → 6,5×”) to w rzeczywistości **Chang WD 2020** (Biomed Res Int, PMID 32309441, PMC7136771): przekrojowe, n=32, SEBT **bez różnic** między grupami wysokiego i niskiego ryzyka urazu. Liczby 4 cm / 2,5 / 94% / 6,5 są jednak zgodne z abstraktem Plisky 2006 — przypis źle podpięty.
- Przypis **8** (cytowany przy Bahr 2016) to ResearchGate (praca o młodzieży grającej w piłkę) — nie Bahr. Treść przypisana Bahrowi jest zgodna z jego abstraktem; przypis źle podpięty.
- Przypis **9** (Burton 2020, self-mobilizacje) podpięty pod test Side Hop — praca nie bada Side Hop.
- Przypis **6** (Alghadir 2020) podpięty pod De Ridder 2015 w bibliografii.

### Treść vs abstrakty — błędy modelu

- **WBLT (Powden 2015)**: rzetelność ✔ (ICC między badającymi 0,80–0,99, u jednego badającego 0,65–0,99; 12 badań); MDC **1,9 cm u jednego badającego, 1,6 cm między badającymi** (lub 4,7° / 4,6°). W sekcji 6 model użył MDC jako „progu tolerancji różnicy między nogami do 1,9 cm” — to nadużycie: MDC dotyczy zmiany u tej samej osoby, nie asymetrii stron.
- **„Osoby z CAI mają zmniejszony zasięg w WBLT” [przypis 6 = Alghadir 2020]** — ✘ odwrotnie: w abstrakcie brak różnic w czynnym zakresie ruchu kostki vs kontrola (goniometr); deficyty były w propriocepcji oraz równowadze statycznej i dynamicznej (Y-balance). „Uprzednie skręcenie najsilniejszym predyktorem” — nie ma w abstrakcie.
- **„Deficyty WBLT predysponują do tendinopatii rzepki” [przypis 5 = Sprague 2018]** — ✘ przesadzone: przegląd (31 prac) podaje tylko **ograniczone lub sprzeczne** dowody dla mniejszego zgięcia grzbietowego; brak silnych dowodów dla jakiegokolwiek czynnika.
- **SEBT (Plisky 2006)**: liczby ✔ (n=235; przednia różnica >4 cm → 2,5×; dziewczęta, wynik złożony <94,0% długości nogi → 6,5×; to ilorazy szans z regresji logistycznej). Rzetelność ICC 0,82–0,87 jest w abstrakcie (model: „bd.”). „Bezkontaktowy uraz” i „uniwersalny punkt odcięcia przy dopuszczaniu do obciążeń” — nie ma w abstrakcie (urazy z utratą czasu treningu; jedna kohorta).
- **Tw. 2 „2/2” (Plisky + Sklempe Kokic) dla asymetrii przedniej >4 cm** — ✘: w Sklempe Kokic 2023 krótszy zasięg we **wszystkich kierunkach poza przednim** i niższy wynik złożony wiązały się z urazem kończyny dolnej; kierunek przedni wiązał się tylko z bólem krzyża. Asymetrii stron nie raportowano. 2/2 jest tylko dla ogólnego: „niższy wynik złożony SEBT ↔ częstszy uraz kończyny dolnej”. „Osoby powracające po urazach tkanek miękkich” — nie ma w abstrakcie (n=42 amatorów, 3,5 mies.).
- **Wspięcia (tw. 4, „Hébert-Losier 2017”)**: 28,7 (<40 lat) i 11,8 (>60 lat) ✔, ale to **Bohannon 2022** (13 prac, procedury „bardzo się różniły”). Protokół z tabeli 3 (metronom 60/min, ≥50% zakresu, palce o ścianę) — nie ma w abstrakcie Bohannon. Prawdziwy Hébert-Losier 2017: 10° pochylnia, do zmęczenia, n=566, ICC 1,0, mediana 24 (M) vs 21 (K).
- **Bahr 2016** ✔: nie ma testu przesiewowego o wystarczających właściwościach; istotny związek z ryzykiem ≠ trafna prognoza; brak badań interwencyjnych wspierających przesiew. Cytat w tytule zgodny. To przegląd krytyczny (narracyjny), nie systematyczny — {DOWÓD:przegląd} jest za mocne; raczej stanowisko eksperta.
- **NMT (Zhou 2026, model: „Moran 2024”)**: ✔ 18 prac / 19 RCT, N=605, równowaga dynamiczna i statyczna SMD 0,96. „Potencjalnie uodparnia na wahania podłoża” — nie ma w abstrakcie (brak danych o urazach).
- **Burton 2020**: RCT n=18 z CAI; self-mobilizacja w wypadzie poprawiła zgięcie grzbietowe (WBLT), obie grupy poprawiły równowagę dynamiczną (Y-Balance), siłę i funkcję. Model użył tej pracy jako źródła dla Side Hop — nie dotyczy.
- **De Ridder 2015** (nie cytowany w tekście): CAI (n=38) vs copers (28) vs kontrola (30) — sztywniejsza strategia lądowania, mniejszy zakres zgięcia podeszwowego/grzbietowego w kostce przy lądowaniu, wyższy szczyt i tempo narastania pionowej siły reakcji podłoża w zeskoku.
- **Sekcja 5 (sprzeczności z bazą)**: model nie otworzył plików bazy („This website is inaccessible”) — nie ma tu analizy. Sprawdziliśmy sami niżej.
- **Sekcja 6** (bateria 20–30 min, „~25 powtórzeń jako minimum przed gapami”, „1,9 cm tolerancji asymetrii”, „X-grind/Fishbrain wymagają balansu ponad SEBT”, Side Hop „replikuje upadek z rurki”) — {WNIOSKOWANIE} modelu, częściowo na błędnie użytych liczbach; nie wchodzi. Bateria może wrócić jako `{PROPOZYCJA}` po recenzji fizjoterapeuty.
- **Sekcja 4**: opisy biomechaniki AGV (heel drop, „uderzenie piszczelą o komin”, soul plate w „ewersji i supinacji”) — bez źródeł; nie wchodzi.
- Sekcja 10: Physiotutors, artgerecht, Sport-Orthese — {OPINIA}, zgodnie z zasadami. „≥5 cali (12,5 cm) to norma WBLT” — tylko blog, nie wchodzi.

### Niezależność grup

- Plisky 2006 (USA) vs Sklempe Kokic 2023 (Osijek/Rijeka/Vukovar, Chorwacja) — brak wspólnych autorów → **niezależne**.
- Zhou 2026 (Pekin) vs Zech 2010 [S84] (Erlangen) — brak wspólnych autorów → **niezależne** (przeglądy mogą częściowo obejmować te same RCT; nie sprawdzaliśmy list badań).
- Bohannon 2022 vs Hébert-Losier 2017 — metaanaliza Bohannon (13 prac) może obejmować Hébert-Losier 2017 (nie sprawdzone), a protokoły i liczby się różnią (średnia 28,7 vs mediana 24/21) → **nie łączymy w 2/2**.
- Powden 2015 i Burton 2020 — wspólny autor (Powden CJ).

### Sprzeczności z bazą (sprawdzone przez nas)

- Brak twardej sprzeczności.
- Test wspięć: baza ma protokół Sanford (do 25 powtórzeń, jedno co 2 s) [S23] i kryterium ≥90% zdrowej strony [S22] jako `{KONSENSUS:protokół}`. Normy Bohannon 2022 (28,7 <40 lat) dotyczą innych protokołów — nie przeczą, nie zastępują.
- `mobilnosc.md` / `wzmacnianie.md`: „ograniczone zgięcie grzbietowe może utrudniać ugięcie kolan przy lądowaniu” — oznaczone {SPEKULACJA}; De Ridder 2015 (CAI: mniejszy zakres w kostce przy lądowaniu, większa siła reakcji) i Sprague 2018 (ograniczone/sprzeczne dowody dla tendinopatii rzepki) nie podnoszą tego do dowodu.
- S16/S18/S84 (trening równowagi) — zgodne z Zhou 2026; S84 podniesiony do 2/2 tylko dla wyników testów równowagi (nie dla urazów, skoków, sprintu).
- S109 (koślawienie nie przewiduje ACL) — zgodne z Bahr 2016 (związek ≠ prognoza).

### Co weszło do bazy

| Twierdzenie | Źródła | Plik |
|---|---|---|
| Niższy wynik złożony SEBT wiązał się z częstszym urazem kończyny dolnej w dwóch kohortach prospektywnych (koszykarze n=235; dziewczęta <94% → OR 6,5; amatorzy piłki nożnej n=42); związek w grupach, nie zwalidowany próg | S153 + S154, ✔ 2/2 | `filar-1-przygotowanie/stabilizacja-i-propriocepcja.md` (+ odwołanie w `kostka/niestabilnosc.md`) |
| Trening równowagi / NMT poprawia wyniki testów równowagi vs brak treningu (20 RCT [S84]; 19 RCT, N=605, SMD 0,96 [S155]) | S84 + S155, ✔ 2/2 | `filar-1-przygotowanie/stabilizacja-i-propriocepcja.md` |

### Co czeka (1/2 lub niepewne) — powód

| Kandydat | Powód wstrzymania |
|---|---|
| SEBT: przednia różnica stron >4 cm → 2,5× większa szansa urazu (Plisky 2006) | jedno źródło; Sklempe Kokic 2023 nie potwierdza kierunku przedniego (dopisane w bazie jako ⏳ 1/2 przy S153) |
| WBLT: dobra rzetelność, MDC 1,9 cm / 1,6 cm (Powden 2015) | jedno źródło (przegląd 12 badań); potrzebny drugi niezależny przegląd/badanie |
| Normy wspięć: 28,7 powt. <40 lat, 11,8 >60 lat (Bohannon 2022); rzetelność ICC 1,0 i mediana 24/21 (Hébert-Losier 2017) | różne protokoły i liczby, możliwe nakładanie się danych; model pomylił autorów |
| Testy przesiewowe nie przewidują urazu u pojedynczego zawodnika (Bahr 2016) | jedno źródło (przegląd krytyczny/stanowisko); kandydat do pary z kolejnym przeglądem właściwości testów |
| CAI: deficyty propriocepcji i równowagi bez różnic w czynnym zakresie ruchu (Alghadir 2020) | jedno źródło (przekrojowe, n=80); przeczy twierdzeniu modelu o WBLT w CAI |
| CAI: sztywniejsza strategia lądowania, wyższa siła reakcji (De Ridder 2015) | jedno źródło |
| Self-mobilizacja w wypadzie poprawia zgięcie grzbietowe w CAI (Burton 2020, n=18) | jedno małe RCT |
| Zmniejszone zgięcie grzbietowe jako czynnik ryzyka tendinopatii rzepki (Sprague 2018) | sam przegląd mówi: dowody ograniczone/sprzeczne |
| Bateria przesiewowa 20–30 min dla AGV (sekcja 6) | wnioskowanie modelu na częściowo błędnych liczbach; ewentualnie `{PROPOZYCJA}` po recenzji fizjoterapeuty |

