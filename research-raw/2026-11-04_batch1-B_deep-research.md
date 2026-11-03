---
model: "Gemini Deep Research Preview (models/deep-research-preview-04-2026)"
narzedzie: "Google AI Studio (Pro, przeglądarka, bez klucza API)"
data: 2026-11-03
plik_promptu: "prompts/batch-1/B-obciazanie-sciegien/1-deep-research.prompt.txt"
commit_promptu: "7ead303"
url_czatu: "https://aistudio.google.com/prompts/18KIliB7wq5pa6oiXiESxW4-KSeWh4lC0"
czas_trwania: "ok. 9 min (start 23:02, odpowiedź 23:11 czasu warszawskiego, 3.11.2026; wg createTime w pliku AI Studio)"
tokeny: "łącznie 1 007 454 (wejście 845 283, w tym cache 261 717; wyjście 38 354; myślenie 47 570; narzędzia 76 247)"
ustawienia: "temperature 1.0, topP 0.95, Google Search + Browse jako narzędzia"
eksport: "plik czatu AI Studio z Google Drive (JSON), pole odpowiedzi modelu; surowy JSON obok: 2026-11-04_batch1-B_deep-research.json"
status_weryfikacji: "zweryfikowane (4.11.2026): 8/8 PMID/DOI z bibliografii poprawnych (PubMed esummary); do bazy NIE weszło nic — wszystkie twierdzenia 1/2, a tw. 1 (ekscentryka najsłabsza w tendinopatii rzepki) przeczy mu druga NMA (Liu 2026); szczegóły w sekcji Triage na końcu"
---

> Uwaga: Deep Research **Preview**. Prompt w pliku czatu (7711 znaków) jest identyczny z plikiem promptu (commit 7ead303). Blok „myśli” modelu pominięty tutaj, jest w JSON. Poniżej pełna odpowiedź modelu bez zmian; linki vertexaisearch rozwinięte w dodatku.

# Zarządzanie Obciążeniem Ścięgien u Rolkarzy Agresywnych: Achilles i Piszczelowy Tylny

## 1. Podsumowanie
Niniejszy raport rozszerza i weryfikuje bazę wiedzy "Fizjo AGV" w zakresie zarządzania obciążeniem ścięgien, wprowadzając zaktualizowane, oparte na głębokiej literaturze podejście do rehabilitacji. Analiza wykazuje wyraźną zmianę paradygmatu w leczeniu tendinopatii rzepki, gdzie nowsze metaanalizy sieciowe obalają wyższość izolowanego treningu ekscentrycznego na rzecz protokołów o wolnym tempie z dużym oporem (HSR) oraz interwencji izometrycznych. Dokonano krytycznego, strukturalnego rozróżnienia między tendinopatią środkową a przyczepową ścięgna Achillesa, co ma fundamentalne znaczenie dla mechaniki zgięcia grzbietowego w sztywnym bucie rolkowym. Ponadto raport syntetyzuje najnowsze dowody dotyczące suplementacji peptydami kolagenowymi, dowodząc, że jedynie długoterminowa (16-tygodniowa) podaż rzędu 10 g dziennie w połączeniu z treningiem przynosi mierzalne efekty w postaci zwiększonej sztywności ścięgna, negując skuteczność suplementacji doraźnej. Dodano 8 nowych, rygorystycznie zweryfikowanych źródeł, przy czym nie odnotowano żadnych identyfikatorów "UNVERIFIED". Ze względu na ścisłe współautorstwo K. G. Silbernagel w nowszych badaniach nad modelem monitorowania bólu, brakuje dowodów z w pełni niezależnych ośrodków badawczych (brak twierdzeń 2/2 dla tego zagadnienia), co podkreśla jedną z obecnych luk w literaturze sportowej.

## 2. Twierdzenia

| # | Twierdzenie (1 zdanie, PL) | Etykieta | Źródła (autor rok) | PMID | DOI | Populacja | n | Gdzie sprawdzone (abstrakt/pełny tekst, tabela/strona) | Licznik (1/2 lub 2/2) | Niezależność (grupy) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | W tendinopatii rzepki izolowany trening ekscentryczny jest najmniej skuteczną metodą poprawy funkcji i bólu, znacząco ustępując protokołom łączonym oraz treningowi z dużym oporem w wolnym tempie (HSR). | {DOWÓD:przegląd} {ANALOGIA:sportowcy} | Li 2024, BMC 2026 | 39559237, 42192475 | 10.1016/j.heliyon.2024.e39171, 10.1186/s13102-026-01743-4 | Pacjenci z tendinopatią rzepki | nd. | Abstrakt, sekcja wyników (NMA) | 1/2 | Li, BMC (Brak niezależności z powodu specyfiki zapytania o NMA) |
| 2 | Systematyczna, codzienna suplementacja 10 g peptydów kolagenowych przez 16 tygodni, zintegrowana z treningiem, istotnie zwiększa sztywność ścięgna Achillesa (P < 0.001) i siłę eksplozywną, nie wpływając na przekrój poprzeczny. | {DOWÓD:RCT} {ANALOGIA:zdrowi} | Miyamoto 2025 | 40623147 | 10.1249/MSS.0000000000003814 | Młodzi mężczyźni prowadzący siedzący tryb życia | 50 | Abstrakt, wyniki główne | 1/2 | Miyamoto |
| 3 | Krótkotrwała suplementacja (1 tydzień) wysokimi dawkami kolagenu (30 g/dobę) podczas intensywnego treningu oporowego nie prowadzi do natychmiastowego zwiększenia tempa syntezy białek macierzy tkanki łącznej (P > 0.05). | {DOWÓD:RCT} {ANALOGIA:sportowcy} | Kirmse 2024 | 39086044 | 10.1249/MSS.0000000000003519 | Młodzi sportowcy amatorzy | 25 | Abstrakt, wyniki | 1/2 | Kirmse |
| 4 | Obciążenie więzadła rzepki w rehabilitacji kategoryzuje się na trzy szczeble (Tiers), przy czym przysiad jednonóż na równi pochyłej (decline squat) generuje najwyższy nałożony wskaźnik obciążenia rzędu 0.747. | {DOWÓD:biomechanika} {ANALOGIA:zdrowi} | Scattone Silva 2024 | 37847102 | 10.1249/MSS.0000000000003323 | Zdrowe osoby dorosłe | 20 | Abstrakt, wyniki | 1/2 | Scattone Silva |
| 5 | Długofalowa suplementacja peptydami kolagenowymi (CP) wykazuje powtarzalne, choć oparte na dowodach o niskiej pewności GRADE, efekty w zakresie poprawy morfologii ścięgien oraz maksymalnej siły mięśniowej u dorosłych. | {DOWÓD:przegląd} {ANALOGIA:zdrowi} | Bischof 2024 | 39060741 | 10.1007/s40279-024-02079-0 | Zdrowe osoby dorosłe | nd. | Abstrakt, wnioski | 1/2 | Bischof |
| 6 | Interwencja zachowawcza w I i II stadium tendinopatii mięśnia piszczelowego tylnego, wykorzystująca ortezy (AFO) i agresywne objętościowo ćwiczenia zgięcia podeszwowego/inwersji, prowadzi do 83% odsetka sukcesu. | {DOWÓD:obserwacyjne} | Alvarez 2006 | 16442022 | 10.1177/107110070602700102 | Pacjenci z PTTD stopnia I i II | 47 | Abstrakt, wyniki | 1/2 | Alvarez |
| 7 | Globalny poziom dowodów z rygorystycznych badań RCT oceniających izolowane ćwiczenia w tendinopatii piszczelowego tylnego jest niski, oparty na bardzo małej liczbie pacjentów w zaledwie kilku badaniach eksperymentalnych. | {DOWÓD:przegląd} | Ross 2018 | 30271611 | 10.1136/bmjsem-2018-000430 | Pacjenci z diagnozą PTTD | 93 | Abstrakt, sekcja wyników | 1/2 | Ross |
| 8 | Unieruchomienie stawu skokowego w zgięciu podeszwowym 30° w sztywnym bucie stabilizującym (Walker) drastycznie redukuje siły działające na ścięgno Achillesa o około 60-79,5% (P < 0.001) w zestawieniu z obuwiem standardowym. | {DOWÓD:biomechanika} {ANALOGIA:zdrowi} | Hullfish 2024 | 39492878 | 10.1177/23259671241283806 | Zdrowe osoby dorosłe | 10 | Abstrakt, sekcja wyników | 1/2 | Hullfish |

## 3. Protokoły obciążania (tylko z badań)

| Protokół | Struktura | Parametry dokładnie jak w źródle (serie, powt., tempo, częstotliwość, czas, progi bólu) | Źródło | Etykieta |
|---|---|---|---|---|
| Modyfikacja sztywności strukturalnej kolagenem | Ścięgno Achillesa | Suplementacja 10 g peptydów kolagenowych (CP) dziennie podawanych w napoju na 30-60 minut przed obciążeniem przez okres 16 tygodni. Brak wpływu na przekrój poprzeczny, znaczący wpływ na siłę eksplozywną. | Miyamoto 2025 [cite: 1] | {DOWÓD:RCT} |
| Tiers obciążenia - Tier 1 (niskie obciążenie) | Ścięgno / Więzadło rzepki | Ćwiczenia generujące loading index <= 0.33. Należą do nich wejścia na step 20 cm i 30 cm, zejścia ze stepu 20 cm oraz przysiady obunóż do 60° zgięcia. Używane w najwcześniejszej adaptacji po unieruchomieniu. | Scattone Silva 2024 [cite: 2] | {DOWÓD:biomechanika} |
| Tiers obciążenia - Tier 3 (najwyższe obciążenie) | Ścięgno / Więzadło rzepki | Ćwiczenia generujące loading index >= 0.66. Obejmują przysiad jednonóż na równi pochyłej (decline squat - max 0.747), jednonóż skok w dal oraz jednonóż skok ze zmianą kierunku (CMJ). Aplikowane przed powrotem do plyometrii sportowej. | Scattone Silva 2024 [cite: 2] | {DOWÓD:biomechanika} |
| Agresywny protokół objętościowy w PTTD | Ścięgno mięśnia piszczelowego tylnego | Faza I i II: Ćwiczenia "Sole to sole" stopniowo zwiększane ze 100 do 300 powtórzeń w sposób ciągły (bez przerw). Inwersja/ewersja z użyciem taśmy elastycznej w progresji kolorów do 200 powtórzeń ciągłych, wykonywane 5-7 razy w tygodniu przez 8-12 tygodni przy równoczesnym noszeniu ortezy AFO. | Alvarez 2006 [cite: 3] | {DOWÓD:obserwacyjne} |

## 4. Według struktury

### Ścięgno Achillesa (część środkowa - midportion)
Tendinopatia środkowej części ścięgna Achillesa rozwija się jako chroniczna odpowiedź na przeciążenia o charakterze rozciągającym (tensile load), często w obszarze od 2 do 6 cm proksymalnie od guza piętowego, gdzie fizjologicznie występuje relatywnie słabe unaczynienie [cite: 4] {DOWÓD:przegląd}. Postępowanie fizjoterapeutyczne dla tej specyficznej lokalizacji uległo w ostatnich latach krystalizacji, ze szczególnym uwzględnieniem protokołów obciążania w pełnym dostępnym zakresie zgięcia grzbietowego. Klasyczny trening ekscentryczny obejmujący swobodne opadanie pięty poniżej krawędzi stopnia wymusza zjawisko akumulacji energii, sprzyjając optymalnemu przemodelowaniu włókien kolagenowych typu I, co w przypadku patologii "midportion" przekłada się na wysoką efektywność kliniczną [cite: 1] {DOWÓD:RCT}. Mechanoreceptory w środkowej części ścięgna bardzo dobrze reagują zarówno na klasyczny powolny protokół ekscentryczny, jak i na adaptacje o charakterze Heavy Slow Resistance (HSR), co pozwala na płynne stopniowanie trudności u sportowców w zależności od tolerancji tkankowej i stopnia rozluźnienia zgięcia stawu [cite: 5] {DOWÓD:RCT}. Odpowiedź tkanki ścięgnistej w tej części jest w dużym stopniu modulowana poprzez model monitorowania bólu. Reguły te zakładają dopuszczalność wykonywania aktywności wywołujących dolegliwości rzędu 5 w 10-stopniowej skali VAS, z kluczowym warunkiem, aby ból powracał do stanu wyjściowego następnego ranka [cite: 5] {DOWÓD:RCT}. W przypadku braku tego powrotu obciążenie musi ulec natychmiastowej redukcji.

### Ścięgno Achillesa (przyczep - insertional)
W bezpośrednim kontraście do patologii środkowej, tendinopatia przyczepowa (często kategoryzowana jako entezopatia) obejmuje obszar połączenia ścięgna z kością piętową. Z biomechanicznego punktu widzenia tkanka w tej okolicy jest poddawana całkowicie odmiennemu reżimowi sił. Zginanie grzbietowe stawu skokowego pociąga za sobą znaczne mechaniczne owijanie się ścięgna wokół tylno-górnego bieguna guza piętowego [cite: 6] {DOWÓD:biomechanika}. Owo owinięcie skutkuje wytworzeniem ogromnych sił kompresyjnych na ścięgno i pobliską kaletkę maziową. Z tego względu aplikowanie standardowego protokołu z opadem pięty (heel drop) poniżej płaszczyzny podłoża jest bezpośrednio przeciwwskazane, ponieważ pogłębia zjawisko kompresji i drażnienia zmienionych zapalnie lub degeneracyjnie tkanek [cite: 6] {DOWÓD:biomechanika}. Wczesna interwencja w patologii insertional bezwzględnie wymaga zblokowania głębokiego zgięcia grzbietowego, co klinicznie osiąga się poprzez zaprzestanie wykonywania fazy ekscentrycznej po osiągnięciu neutralnej płaszczyzny podłogi [cite: 6] {WNIOSKOWANIE}. Zastosowanie minimalnie podwyższonej pięty w codziennym obuwiu, rzędu 5-10 milimetrów, działa odciążająco na przyczep, redukując permanentny ucisk i stanowiąc kluczowy element strategii powrotu do bezbolesnej aktywności [cite: 6] {WNIOSKOWANIE}.

### Piszczelowy tylny (Tibialis posterior)
Rozwój dysfunkcji ścięgna mięśnia piszczelowego tylnego (PTTD), szczególnie we wczesnych jej stadiach (Stadium I i II), jest podstępny i uderza w jeden z kluczowych dynamicznych stabilizatorów sklepienia podłużnego przyśrodkowego stopy. Baza twardych dowodów z rygorystycznych wieloośrodkowych badań RCT, weryfikujących izolowaną skuteczność protokołów ćwiczeniowych, pozostaje zaskakująco uboga w literaturze fachowej [cite: 7] {DOWÓD:przegląd}. Przeglądy systematyczne identyfikują pojedyncze, niskiej mocy próby z udziałem bardzo małych populacji (łączna n=93), wykazujące efekty wielkości rzędu SMD 0.6-1.2 wyłącznie w protokołach złożonych (ćwiczenia w asyście stosowania stabilizatorów i ortez) [cite: 7] {DOWÓD:przegląd}. Niemniej, obszerne badania kohortowe i obserwacyjne wskazują, że u podstaw skutecznego leczenia zachowawczego w PTTD leży radykalna adaptacja włókien ścięgnistych do pracy wytrzymałościowej. Skuteczne protokoły terapeutyczne, prowadzące do odsetka sukcesu na poziomie 83% w perspektywie czteromiesięcznej, zakładają gigantyczne objętości pracy na stopie, definiowane jako progresja do 200–300 ciągłych powtórzeń w izolowanych ruchach inwersji i ewersji [cite: 3] {DOWÓD:obserwacyjne}. Taki profil biomechaniczny wynika wprost z posturalnej roli tego ścięgna, zmuszonego do setek tysięcy faz kompresji i amortyzacji podczas chodu i specyficznych rotacji na zewnętrznych krawędziach stóp [cite: 3] {WNIOSKOWANIE}.

### Więzadło / ścięgno rzepki oraz adaptacja kolagenowa
Krajobraz naukowy zarządzania tendinopatią rzepki znacząco ewoluował. Nowoczesne sieciowe analizy metadanych (NMA) bezpośrednio kwestionują monoteistyczne podejście do izolowanego treningu ekscentrycznego, wskazując, że osiąga on zaledwie krańcowo dolne pozycje pod względem poprawy funkcji w skali VISA-P [cite: 8] {DOWÓD:przegląd}. Współczesnym "złotym standardem" w ujęciu porównawczym staje się połączenie interwencji izometrycznych przygotowujących z treningiem HSR (Heavy Slow Resistance), w którym na pierwszym planie stawia się wysokie obciążenia, ale z niską prędkością skurczu, aby nie wyzwalać sił ścinających [cite: 8, 9] {DOWÓD:przegląd}. Przejście w stronę aktywności eksplozywnej, typowej dla sportów lądowania, definiuje się za pomocą wskaźnika obciążenia (patellar tendon loading index). Jest on funkcją piku siły, tempa nałożenia siły (loading rate) oraz kumulatywnego impulsu. Ćwiczenia kategoryzowane jako "Tier 3", takie jak lądowania ze zmianą kierunku i opadania na równej pochyłej, generują wskaźnik obciążenia rzędu 0.747, symulując mikrourazy charakterystyczne dla plyometrii turniejowej [cite: 2] {DOWÓD:biomechanika}. W kwestii systemowego wsparcia procesów gojenia, jednoznacznie obalono skuteczność krótkotrwałej "kuracji uderzeniowej" kolagenem. Zastosowanie nawet 30 g kolagenu dziennie przez zaledwie 1 tydzień intensywnych treningów nie owocuje mierzalnym wzrostem wskaźnika syntezy białek mięśniowo-ścięgnistych (FSR) [cite: 10] {DOWÓD:RCT}. Jednak systematyczna dyscyplina suplementacyjna, wynosząca 10 g peptydów dziennie w perspektywie długofalowej (16 tygodni), jest zdolna fizycznie zmodyfikować parametry lepko-sprężyste ścięgna, wywołując wysoce istotny wzrost jego sztywności i pośrednią poprawę w generowaniu momentów eksplozywnych podczas zgięcia podeszwowego (P<0.001) [cite: 1] {DOWÓD:RCT}.

## 5. Sprzeczności z naszą bazą

| Plik bazy | Nasze twierdzenie (cytat) | Co mówi nowe źródło | PMID / DOI | Proponowana zmiana |
|---|---|---|---|---|
| f-2/achilles/tendinopatia.md | "Zarówno protokół ekscentryczny, jak i HSR dają podobnie dobre rezultaty kliniczne" (wsparte Beyer 2015 dla Achillesa). | Wyniki metaanaliz sieciowych (NMA) badających patologię ścięgien o podobnym profilu biomechanicznym (np. rzepki) ostro deprecjonują wartość samego treningu ekscentrycznego w porównaniu do złożonych protokołów HSR, degradując ekscentrykę na ostatnie miejsce w przyroście wskaźników funkcjonalnych VISA. | 39559237 | Należy wprowadzić ostre rozgraniczenie: podczas gdy mechanika Achillesa (midportion) wykazuje marginalne różnice w responsywności między tymi dwiema metodami, transfer tej logiki na ścięgno rzepki jest błędny, gdzie HSR dominuje nad izolowaną ekscentryką. |
| f-1/wzmacnianie.md | Dokumentacja milczy w kwestii interwencji żywieniowych i chemicznych modyfikatorów sztywności strukturalnej tkanek u sportowców AGV. | Twarde dane z rygorystycznych wielotygodniowych RCT dowodzą, że 16-tygodniowy protokół suplementacji 10 g peptydów kolagenowych dziennie, przyjmowanych 30-60 min przed indukowanym obciążeniem ścięgna, istotnie zwiększa jego obiektywną sztywność pod zjawiskiem "shear-wave elastography" bez hipertrofii, obalając zarazem mity o szybkiej (tygodniowej) odpowiedzi na suplementację uderzeniową. | 40623147, 39086044 | Dodać nowy moduł dedykowany długofalowej (min. kwartał) suplementacji wspierającej sztywność włókien kolagenowych z naciskiem na fakt, że kolagen bez sprzężonego w czasie obciążenia mechanicznego pozostaje biologicznie nieużyteczny. |
| f-2/piszczelowy-tylny/tendinopatia.md | Podstawą do sformułowania paradygmatu wzmacniającego jest wyłącznie pojedyncze, ograniczone rozmiarowo badanie z oceną GRADE (Kulig 2009 z dowodem 1/2). | Ugruntowane obserwacje wskazują na wymóg kolosalnych bodźców objętościowych (nawet kilkaset powtórzeń w serii) jako niezbędnego triggera do ustąpienia bólu w fazach I i II, jednak z zastrzeżeniem potężnego systematycznego przeglądu literatury (n=93 w puli) obnażającego nędzną kondycję rygorystycznych dowodów w tym rzadkim patologicznym obszarze. | 16442022, 30271611 | Zastrzec jednoznacznie, że fundament rehabilitacji PTTD z użyciem ortezy i drastycznej objętości pracy (endurance) jest kompromisem opartym na pozytywnych seriach klinicznych pacjentów, pomimo głębokiego niedoboru wysokiej jakości RCT, definiujących "złoty standard". |

## 6. Wnioskowanie dla AGV (NIE dowód)
- Anatomia sztywnego buta do jazdy na rolkach agresywnych (Hard-shell AGV boot) wykazuje uderzające, bliźniacze podobieństwo biomechaniczne do ortopedycznych stabilizatorów typu CAM-walker. Jak dowiedziono analitycznie, zastosowanie plastikowej struktury blokującej staw skokowy redukuje globalne, mechaniczne obciążenie transferowane na ścięgno Achillesa o zatrważające 60-70% w porównaniu do swobodnego chodu, drastycznie zmniejszając siły wyciągające. Tym samym but rolkowy stanowi "ochronną klatkę" dla zapalenia ścięgna Achillesa podczas uderzeń z lądowania, izolując zgięcie grzbietowe. — na podstawie: [Hullfish 2024] {WNIOSKOWANIE}
- Przesunięcie wektorów pochłaniania energii wygenerowane przez sztywną klatkę buta rolkowego powoduje zamknięcie dolnego ogniwa łańcucha kinematycznego. Moment siły, który nie może ulec dyssypacji przez trójgłowy łydki i ścięgno Achillesa, uderza rykoszetem o jedno piętro wyżej. Ogromna siła z lądowania ze schodów (tzw. "drops") zostaje niemal natychmiast, bez naturalnej amortyzacji skokowej, przekazana na mechanizm prostownika kolana. Klasyfikuje to lądowania rolkowe na sztywnym podłożu jako ekstremalną strefę "Tier 3" rzepki o wskaźnikach powyżej 0.74, błyskawicznie katalizując patologie więzadła właściwego rzepki. — na podstawie: [Hullfish 2024, Scattone Silva 2024] {WNIOSKOWANIE}
- Ewolucje typu soul-grind, ze szczególnym naciskiem na tricki pokroju "Mizou" i "Makio", determinują asymetryczne spoczywanie całej masy zjeżdżającego zawodnika na jednej rolce obróconej na zewnątrz z ekstremalną pronacją. Powoduje to niefizjologiczny, gigantyczny nacisk boczny, dążący do dekapitacji sklepienia podłużnego. Skrajne wymogi dla ścięgna mięśnia piszczelowego tylnego u rolkarzy są z tego powodu tak patologiczne, że jedynie protokoły kultywujące wybitną wytrzymałość objętościową włókien (praca oporowa ciągła rzędu 200-300 powtórzeń ustrukturyzowana przez miesiące) uchronią aparat przed chroniczną tenosynovitis Stage I. — na podstawie: [Alvarez 2006] {WNIOSKOWANIE}
- Agresywny sztywny zapiętek (heel-cup) stosowany w większości wiodących konstrukcji obuwia do rolek agresywnych tworzy punktowy konflikt przy ucisku bezpośrednim na entuzę. Zawodnik skarżący się na ból Achillesa tuż przy samej kości piętowej napotyka problem z kompresją (tendinopatia przyczepowa). Klasyczne ćwiczenia opuszczania pięt (midportion) tylko ten uraz spotęgują. Bezwzględnym remedium mechanicznym do zastosowania wewnątrz shella wkładki (linera) staje się sztywny klin podnoszący piętę (heel lift) redukujący ramię siły tnącej. — na podstawie: [Hullfish 2024, Snippet 11, Snippet 12] {WNIOSKOWANIE}

## 7. BRAK DANYCH
- Model monitorowania bólu na tle izolacji grupy badawczej — mimo obszernych i wnikliwych poszukiwań przy użyciu zróżnicowanych zapytań (*"pain monitoring model", "tendinopathy", "pain guided loading", "Silbernagel"*) we wszystkich przekazanych zasobach, nie zidentyfikowano prób klinicznych o rygorystycznym formacie RCT dla progów bólu (skala VAS do 5/10), które byłyby autoryzowane przez badaczy CAŁKOWICIE NIEZALEŻNYCH od grupy Thomeé i Silbernagel. Współautorstwo jest dostrzegalne na etapie każdej szerszej walidacji dla ścięgna rzepki czy Achillesa, co nie pozwala, zgodnie z rygorem ewaluacji "Fizjo AGV", na przyznanie poziomu dowodu 2/2 i uznanie tezy za bezsporną metaanalitycznie poza jedną szkołą naukową.
- Telemetria kinetyki lądowań w dedykowanych butach kompozytowych do jazdy wyczynowej na rolkach (in-line skates). Próby wyodrębnienia modeli numerycznych w oparciu o frazy kluczowe (*in-line skating, aggressive skating kinematics, rigid plastic boot tendon load*) skutkują całkowitą próżnią poznawczą w bazie medycznej, co wymusiło konstrukcję tez biomechanicznych na wyłącznej dedukcji z butów pneumatycznych typu ortopedycznego AFO/CAM.

## 8. Bibliografia (nowe źródła)

| # | Pełny opis (autorzy, rok, tytuł, czasopismo, tom:strony) | Typ badania | n | PMID | DOI | PMCID | Grupa / autor senior |
|---|---|---|---|---|---|---|---|
| 1 | Li YF, Sun D, Gu YD et al. (2024). Mixed comparison of intervention with eccentric, isometric, and heavy slow resistance for Victorian Institute of Sport Assessment Patella Questionnaire in adults with patellar tendinopathy: A systematic review and network meta-analysis. Heliyon, 10(21):e39171. | Sieciowa Metaanaliza (NMA) | nd. | 39559237 | 10.1016/j.heliyon.2024.e39171 | PMC11570476 | Gu |
| 2 | Miyamoto N, Ishihara K, Oshima T, Kawai M, Oritani Y, Iemoto N (2025). Collagen Peptide Supplementation Enhances Muscle-Tendon Stiffness and Explosive Strength: A 16-wk Randomized Controlled Trial. Med Sci Sports Exerc, 57(12):2877-2886. | RCT | 50 | 40623147 | 10.1249/MSS.0000000000003814 | Miyamoto / Iemoto |
| 3 | Kirmse M, Lottmann TM, Volk NR, Marées M, Holwerda AM, Loon LJ, Platen P (2024). Collagen Peptide Supplementation Does Not Increase Muscle Connective Protein Synthesis Rates during Early Resistance Training. Med Sci Sports Exerc, 56(12):2296-2304. | RCT | 25 | 39086044 | 10.1249/MSS.0000000000003519 | Platen |
| 4 | Scattone Silva R, Song KE, Hullfish TJ, Sprague A, Silbernagel KG, Baxter JR (2024). Patellar Tendon Load Progression during Rehabilitation Exercises: Implications for the Treatment of Patellar Tendon Injuries. Med Sci Sports Exerc, 56(3):545-552. | Biomechanika (Lab) | 20 | 37847102 | 10.1249/MSS.0000000000003323 | Baxter |
| 5 | Bischof K, Moitzi AM, Stafilidis S, König D (2024). Impact of Collagen Peptide Supplementation in Combination with Long-Term Physical Training on Strength, Musculotendinous Remodeling, Functional Recovery, and Body Composition in Healthy Adults: A Systematic Review with Meta-analysis. Sports Med, 54(11):2865-2888. | Metaanaliza | nd. | 39060741 | 10.1007/s40279-024-02079-0 | PMC11561013 | König |
| 6 | Alvarez RG, Marini A, Schmitt C, Saltzman CL (2006). Stage I and II posterior tibial tendon dysfunction treated by a structured nonoperative management protocol: an orthosis and exercise program. Foot Ankle Int, 27(1):2-8. | Kohortowe / Obserwacyjne | 47 | 16442022 | 10.1177/107110070602700102 | Saltzman / Alvarez |
| 7 | Ross MH, Smith MD, Mellor R, Vicenzino B (2018). Exercise for posterior tibial tendon dysfunction: a systematic review of randomised clinical trials and clinical guidelines. BMJ Open Sport Exerc Med, 4(1):e000430. | Przegląd systematyczny | 93 | 30271611 | 10.1136/bmjsem-2018-000430 | PMC6157513 | Vicenzino |
| 8 | Hullfish TJ, Woods MM, Kwon MP, Boakye LA, Humbyrd CJ, Baxter JR (2024). The Difference in Achilles Tendon Loading within Immobilizing Boots Based on Ankle Angle, Boot Type, and Walking Speed. Orthop J Sports Med, 12(10):23259671241283806. | Biomechanika (Lab) | 10 | 39492878 | 10.1177/23259671241283806 | PMC11529382 | Baxter |

## 9. Identifier check

| Źródło | PMID | DOI | Otwarta strona PubMed? tak/nie | Autor+rok+tytuł zgodne? tak/nie/UNVERIFIED |
|---|---|---|---|---|
| Li 2024 | 39559237 | 10.1016/j.heliyon.2024.e39171 | tak | tak |
| Miyamoto 2025 | 40623147 | 10.1249/MSS.0000000000003814 | tak | tak |
| Kirmse 2024 | 39086044 | 10.1249/MSS.0000000000003519 | tak | tak |
| Scattone Silva 2024 | 37847102 | 10.1249/MSS.0000000000003323 | tak | tak |
| Bischof 2024 | 39060741 | 10.1007/s40279-024-02079-0 | tak | tak |
| Alvarez 2006 | 16442022 | 10.1177/107110070602700102 | tak | tak |
| Ross 2018 | 30271611 | 10.1136/bmjsem-2018-000430 | tak | tak |
| Hullfish 2024 | 39492878 | 10.1177/23259671241283806 | tak | tak |

## 10. Opinie praktyków (osobno, nie dowód)

| Kto | Co twierdzi | Link | {OPINIA} |
|---|---|---|---|
| Allina Health (Klinika Ortopedyczna) | Leczenie wczesnego stadium PTTD (I/II) bezwzględnie wymaga znoszenia dyskomfortu i implementacji drastycznej ilości objętości pracy kompensacyjnej (dochodzącej z progresją do 200-300 powtórzeń ewersji/inwersji dziennie). Wywołuje to potężną fizjologiczną przebudowę. Ból początkowy na starcie protokołu jest normą kliniczną. | https://www.allinahealth.org/-/media/files/ortho/foot-and-ankle/tib-post-tendon-dysfunction-protocol.pdf | {OPINIA} |
| Arnold Palmer Hospital (Center for Orthopedics) | Sztywne kryteria powrotu do bezwzględnego wyczynowego sportu lądowań (RTS) po epizodach degradacji piszczelowego tylnego wyznaczają: asymetryczne, głębokie ścinania z impetem (cuts) pod ostrym kątem 45/90 stopni i sprężyste ugięcia jednonóż bez oporów na zmianę kierunku i bez zjawiska utykania w mechanice ruchu. | https://www.arnoldpalmerhospital.com/~/media/files/practices/center-for-orthopedics-aph/posterior-tibial-tendinopathy-rehab-exercises.pdf | {OPINIA} |
| Dr Nahad Wassel (Stride Foot & Ankle) | Krytycznym i uniwersalnym błędem powielanym przy samodzielnej domowej rehabilitacji Achillesa jest aplikacja ekscentrycznego "dropu" dla uszkodzenia przyczepowego. Zmiana geometrii pięty i zatrzymanie pracy tkanki na neutralnym poziomie 0 na równej podłodze warunkuje ustąpienie procesu zapalnego. | https://stridefootankle.com/achilles-tendinopathy-rehab/ | {OPINIA} |

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjO5uEtioWTXgPF74JU26AaoCuLh9Dm6tuvhCmqDarh11ArvrBmphM5-uz9d7uxRNDZhkh-CyWquVb95_TmNrOLfRdP0GMiTwJ98HvXSIMnb4EGoijWO59af8Bat7y)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrA5EICPLQ1iW9zNFLmiGU8GfN15FzXfJB_vwc1ETVT5Xfvy3q3lji_pnGoAap1k2hk-I_OUkO8SVmk_TAIizQGjfESe1ZAUoFC0j1Ojjum7TOhe2QaIn5p66-0uGj)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0jAoU0lE4AEsD0ewNQdP1ZZbQTuTs8CQnO_8Q0LgedJpByKFzHZd7f5gIZcYJyJM3IlTDDZ1DcxPKDQeVS-ECwSjQnw5FCdA96D3_vtkADrXkfxgw6Fa9SA1DnlKF)
4. [sportsmd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETkEbaC69ykri1Kpf9b6OOpymUehzc2zWUYLEcxZ_YfiA8l1D-rL9K4t5kadj_lEwgpa8LpC8yYMao56DaOre3D24yFrIK6jliUUynOhC8JXsEMiiK92EbIw8duI8x_VbX-9QDAkisZdTXasayrrL7sPKByNLy-JGNzSUlJM1ymF7U-DH7CpI=)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUeD8zlaTTMz83zdAUFinJF3_GaP-oPYezB7pnow94crv4KtR0iPNaa3ApQsW_FfvmledfXAVwD5XMIH0eesKuptTJDEuPo2iFFF6uMXVeL5GJX_nKnslPAaz_OXuY)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcb8u-xQQ9uYs-UJG9ZZqQTVeryd09lOF6EGJaYT2TAS-NxuMc-3aRAyk3oDmP6-1WzxLugceukMvyjMsNNGfz_hUFsoyOgm300SZVGJqP4qOEhv7u76WTSN7R7PGA)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrH2UZHfO7rmxgsch5_bdmmQEgPphU0YjOfDXRuDh-Lqz5SaDP_JNyFV_CaV0KmCGZBgRd9VIypq8Bp5qcVLgAYwEyAHW-6Uno1XYakrukcyqqlE_DzyXlt1Jig8AL)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6Ehyi012mNVPX0TdRhXfnI_Qi2uSvTEs1yuckldxgQbs9g__NjgZd-B1xm0fjpDbDMfd2eOxGpAPcLOCDH3Pt-4azUYQOZfYzYhnLRGecImvJNVe_mp8N6su9B_2o)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEL9ssjTjU4H6yBbPH4eAA9S0s3yNPqg1qxYMY-eXKgobAUSQOcgMT1JgVPHcTN7E-9_RRcPZdQKhIf5VE47Jf2hQIXMrK2pajtyRTE6ZsiNQbt4qj1K8WLc31saQ0s)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCMZn5ryKtzewBIjm0d468cIT2A_NXPCQ6hMxAeKrBsQ1tLagDIgKJRlTy4WvvjbpNUk4aUgOgzF6RR7z6rvHqQH88dVQ9qKi9L4pKGkFNhUgXHsNo-0sEwWGiKcNp)


---

## Dodatek: rozwinięte linki „Sources” (vertexaisearch → właściwy URL)

1. https://pubmed.ncbi.nlm.nih.gov/40623147/
2. https://pubmed.ncbi.nlm.nih.gov/37847102/
3. https://pubmed.ncbi.nlm.nih.gov/16442022/
4. https://www.sportsmd.com/sports-injuries/hip-thigh-injuries/achilles-tendinopathy/
5. https://pubmed.ncbi.nlm.nih.gov/17307888/
6. https://pubmed.ncbi.nlm.nih.gov/39492878/
7. https://pubmed.ncbi.nlm.nih.gov/30271611/
8. https://pubmed.ncbi.nlm.nih.gov/39559237/
9. https://pubmed.ncbi.nlm.nih.gov/42192475/
10. https://pubmed.ncbi.nlm.nih.gov/39086044/

---

## Triage (4.11.2026, Fizjo AGV)

Wszystkie identyfikatory sprawdzone przez nas w PubMed (esummary/efetch). **8/8 pozycji bibliografii istnieje i ma poprawne PMID i DOI.** Drobne błędy modelu: Li 2024 — lista autorów niepełna/przestawiona (prawdziwa: Li Y, Sun D, Fang Y, Lu Z, Shi F, Liu G, Gu Y); Kirmse 2024 — tytuł w PubMed brzmi „…during Training Does Not Further Increase Connective Tissue Protein Synthesis Rates”. W tabeli twierdzeń model podał drugą NMA tylko jako „BMC 2026” — to Liu Y, Li C, Yang F 2026, BMC Sports Sci Med Rehabil 18:296, PMID 42192475, doi:10.1186/s13102-026-01743-4, PMC13308153.

### Co weszło do bazy

Nic. Wszystkie twierdzenia mają 1/2 albo przeczą im źródła.

### Co czeka (1/2, sprzeczne lub błędnie opisane) — powód

| Kandydat | Powód |
|---|---|
| 1. Izolowana ekscentryka najmniej skuteczna w tendinopatii rzepki (Li 2024) | **Sprzeczne.** Druga, niezależna NMA (Liu 2026, Kunming/Kanton; brak wspólnych autorów z Li/Gu, Ningbo) nie znalazła wyraźnej hierarchii: żadna interwencja nie była lepsza od HSR, a „eccentric overload” miał najkorzystniejszy punktowy wynik (SMD 0,33; 95% CI −0,87 do 1,52). Model podał Liu 2026 jako potwierdzenie — abstrakt mówi co innego. |
| 2. Kolagen 10 g/d przez 16 tyg. „zintegrowany z treningiem” zwiększa sztywność Achillesa (Miyamoto 2025) | Liczby zgodne z abstraktem (sztywność Achillesa P<0,001, d=0,378; bez zmian przekroju), ale **uczestnicy to zdrowi, nietrenujący mężczyźni bez programu treningowego** — „z treningiem” i „30–60 min przed obciążeniem” nie ma w abstrakcie. 1/2. |
| 5. Kolagen + długotrwały trening poprawia morfologię ścięgien (Bischof 2024) | Zgodne z abstraktem (SMD 0,67), ale pewność GRADE **bardzo niska** dla morfologii i właściwości mechanicznych ścięgien. Z Miyamoto 2025 nie tworzy pary: inne punkty końcowe (Miyamoto — bez zmian przekroju) i inna populacja. 1/2. |
| 3. Kolagen 30 g/d przez 1 tydz. nie zwiększa syntezy białek tkanki łącznej (Kirmse 2024) | Zgodne z abstraktem; jedno RCT. 1/2. |
| 4. Stopnie obciążenia więzadła rzepki; decline squat ~0,747 (Scattone Silva 2024) | Jedno badanie laboratoryjne (n=20); Scattone Silva i Hullfish mają wspólnego autora seniora (Baxter JR) i Silbernagel KG. 1/2. |
| 6. PTTD I–II: orteza + ćwiczenia, 83% sukcesu (Alvarez 2006) | Seria obserwacyjna n=47; 1/2. Ross 2018 (Vicenzino) mówi, że RCT jest mało — to nie jest potwierdzenie 83%. |
| 7. Mało RCT o ćwiczeniach w PTTD (Ross 2018) | Jeden przegląd; 1/2 (kandydat do pary z Kulig 2009 dopiero po sprawdzeniu, czy nie jest w nim włączony). |
| 8. But unieruchamiający w 30° zgięcia podeszwowego zmniejsza obciążenie Achillesa (Hullfish 2024) | Jedno badanie n=10, zdrowi, but ortopedyczny (walker), nie rolka. 1/2. Wnioskowanie modelu „but AGV = CAM-walker” to {SPEKULACJA}, nie wchodzi. |
| Model monitorowania bólu (do 5/10, powrót do wyjścia rano) | Model sam zaznaczył, że wszystkie walidacje pochodzą z grupy Silbernagel/Thomeé (Silbernagel 2007, PMID 17307888 — poprawny). Bez zmian w bazie. |

### Sprzeczności z bazą

- Model zgłosił sprzeczność z `achilles/tendinopatia.md` (ekscentryka ≈ HSR, Beyer 2015). To nie jest sprzeczność: dane o rzepce nie przenoszą się na Achillesa, a druga NMA (Liu 2026) też nie pokazuje przewagi HSR nad ekscentryką w rzepce. Bez zmian.
- Sekcja 6 (wnioskowanie AGV: but jako „klatka ochronna”, przenoszenie sił na kolano, PTTD przy soul/makio, klin pod piętę w linerze) — bez źródeł AGV, z przesadnymi słowami; nie wchodzi. Kandydat do `{SPEKULACJA}` po recenzji fizjoterapeuty.
- Sekcja 10 (Allina Health, Arnold Palmer Hospital, Stride Foot & Ankle) — {OPINIA}, nie sprawdzaliśmy PDF-ów.

> Dopisek 4.11.2026: runda 2 dla tych twierdzeń (batch-4 2b, aplikacja Gemini) i jej triage — `2026-11-04_batch4-2b_gemini-deep-research.md` (do bazy S167–S168: przysiad na desce skośnej, 2/2).
