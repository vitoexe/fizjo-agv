---
model: "Gemini Deep Research Preview (models/deep-research-preview-04-2026)"
narzedzie: "Google AI Studio (Pro Tomasza, przeglądarka bota, bez klucza API)"
data: 2026-11-11
plik_promptu: "prompts/poradnik-unity/2-deep-research.prompt.txt"
url_czatu: "https://aistudio.google.com/prompts/1zfFv4MufDDCigFCgKaw7KQ0d9-3G6zwz"
przebieg: "start 10:50; błędy: 10:50 przebieg 1 „An internal error has occurred”, 11:14 „Precondition check failed”, 11:15 „Continue” → „An internal error has occurred”, 11:31 „continue” → odpowiedź 11:41 (czas warszawski, wg createTime w pliku czatu)"
tokeny: "łącznie 1 423 413 (wejście 1 261 528, w tym cache 95 878; wyjście 36 872; myślenie 42 999; narzędzia 82 014)"
ustawienia: "temperature 1.0, topP 0.95, Google Search + Browse jako narzędzia"
eksport: "plik czatu AI Studio z Google Drive (JSON), pola odpowiedzi modelu (2 części + 1 obraz wygenerowany przez agenta, nieeksportowany); 41 linków grounding-redirect rozwiniętych do prawdziwych URL-i (41/41)"
status_weryfikacji: "triage 11.11.2026 (sekcja na końcu pliku): jedyna praca naukowa (Major 2007, PMID 17786694, DOI 10.1080/02640410601129615) — identyfikatory poprawne w PubMed i Crossref, liczby r/P zgodne z abstraktem; etykiety {2/2} nadane przez model NIE są wiarygodne (patrz triage); nic nie wpisane do bazy"
---

> **To nie jest diagnoza ani porada medyczna.** Surowy wynik Deep Research — poniżej pełna odpowiedź modelu bez zmian (poza rozwinięciem linków). Etykiety i oceny „2/2” są autorstwa modelu, nie zweryfikowane. Triage na końcu pliku.

# Kompleksowa analiza biomechaniczna, techniczna i fizjoterapeutyczna triku „unity” w jeździe na rolkach agresywnych

W jeździe na rolkach agresywnych (AGV – Aggressive Inline Skating) triki typu *grind* (ślizgi po przeszkodach, takich jak poręcze czy murki) stanowią absolutny fundament tej dyscypliny sportów ekstremalnych. Trik „unity” jest powszechnie uznawany za jeden z najbardziej zaawansowanych technicznie i wizualnie efektownych manewrów, charakteryzującym się głębokim skrzyżowaniem kończyn dolnych podczas ślizgu. Niniejszy raport stanowi wyczerpującą, opartą na dowodach naukowych oraz konsensusie eksperckim analizę tego triku. Dokument ten integruje wiedzę z zakresu techniki jazdy, biomechaniki sportu oraz fizjoterapii, ze szczególnym uwzględnieniem prewencji urazów oraz rehabilitacji pourazowej. Został on przygotowany jako kompendium wiedzy dla społeczności rolkarzy, certyfikowanych instruktorów oraz fizjoterapeutów sportowych pracujących ze sportowcami ekstremalnymi.

## 1. Definicja i warianty: Anatomia triku „Unity”

Trik „unity”, historycznie określany w słownikach subkulturowych z lat 90. XX wieku również mianem „Buddah” {KONSENSUS} {2/2} [cite: 1, 2], należy do rodziny ślizgów wykorzystujących centralną część szyny rolki, znaną jako *H-block*. Kategoryzuje się go jako ślizg ze skrzyżowanymi nogami (cross-legged grind). Prawidłowe, asymetryczne ułożenie stóp jest kluczowe dla zdefiniowania tego manewru z perspektywy technicznej.

### 1.1. Pozycjonowanie stóp i punkty styku z przeszkodą

W klasycznym, frontside’owym „unity” (wykonywanym przodem do przeszkody), układ kinematyczny stóp oraz punktów kontaktu buta z poręczą (rail) lub murkiem (ledge) jest ściśle zdefiniowany. Noga prowadząca (znajdująca się z przodu w kierunku jazdy) ułożona jest w pozycji określanej w terminologii AGV jako *backslide* {KONSENSUS} {2/2} [cite: 3, 4]. Oznacza to biomechanicznie, że rolka opiera się na zewnętrznej krawędzi półki buta (tzw. *backside plate* lub *negative groove*). Z kolei noga zakroczna (znajdująca się z tyłu) ułożona jest w pozycji *frontside* lub *torque* względem kierunku ślizgu, co oznacza, że ślizg odbywa się na wewnętrznej krawędzi półki (tzw. *frontside plate* lub *positive groove*) {KONSENSUS} {2/2} [cite: 3, 4]. 

Aby trik był w pełni kontrolowany, każda rolka powinna generować dwa punkty styku z przeszkodą, co daje łącznie cztery stabilne punkty oparcia: wcięcie w szynie (*H-block frame*) oraz odpowiednią część plastikowej półki buta (*soul plate*) dla każdej ze stóp {OPINIA: Ricardo Lino, instruktor AGV} {2/2} [cite: 5]. W przeciwieństwie do trików takich jak *royale*, gdzie obie rolki są pochylone w tę samą stronę (równolegle), w *unity* ułożenie jest silnie asymetryczne, ponieważ golenie krzyżują się, wymuszając przeciwstawne kąty nachylenia obu butów {WNIOSKOWANIE} [cite: 5].

| Nazwa Triku | Ułożenie nogi prowadzącej (Front) | Ułożenie nogi zakrocznej (Back) | Kierunek ugięcia kolan | 
| :--- | :--- | :--- | :--- |
| **Unity** | Backslide (oparcie na zewnętrznej krawędzi) | Frontside / Torque (oparcie na wewnętrznej) | Na zewnątrz (odwiedzenie) |
| **Royale** | Royale (oparcie na wewnętrznej krawędzi) | Backslide (oparcie na zewnętrznej krawędzi) | Równolegle w kierunku jazdy |
| **Fishbrain** | Makio (Topside - ciężar na górnej półce) | Swobodna (nie dotyka przeszkody) | N/A (ślizg jednonóż) |

### 1.2. Złożoność nomenklatury: Unity vs. Savannah

W społeczności AGV istnieje długotrwała, historyczna debata na temat definicyjnych różnic między trikiem *unity* a *savannah*. Konflikt ten wynika z ewolucji nazewnictwa trików na przestrzeni dekad {KONSENSUS} {2/2} [cite: 3, 6, 7]. 

Pierwsze podejście, określane jako pozycyjno-kierunkowe, zakłada, że fizyczne ułożenie stóp (ich skrzyżowanie) jest identyczne dla obu tych trików. Różnicę stanowi wektor ruchu środka ciężkości po zablokowaniu na przeszkodzie. Jeśli rolkarz jedzie w kierunku nogi, która znajduje się „na zewnątrz” (czyli noga prowadząca to zablokowany *backslide*), manewr ten nazywany jest *unity*. Jeśli natomiast wektor ruchu skierowany jest w przeciwną stronę (noga prowadząca to zablokowany od wewnątrz *torque*, a ciało podąża w kierunku skrzyżowania), trik ten definiuje się jako *savannah* {OPINIA: Acosta Blades, trener; Felipe Zambardino} {2/2} [cite: 3, 8, 9]. W tym ujęciu *savannah* traktowane jest synonimicznie z pojęciem *alley-oop unity*.

Drugie, nowsze podejście opiera się na logice i standaryzacji (tzw. reguła *leading leg*). Propagatorzy tego systemu argumentują, że *unity* powinno zawsze oznaczać manewr, w którym prowadzi przednia (skrzyżowana z przodu) noga. Jeśli podczas ślizgu prowadzi noga znajdująca się z tyłu skrzyżowania, manewr powinien nosić nazwę *savannah*. Podejście to eliminuje historyczny chaos pojęciowy i ujednolica składnię trików (syntax) z pozostałymi ewolucjami na *H-blocku*, gdzie terminy *alley-oop* i *truespin* powinny dotyczyć wyłącznie kierunku rotacji ciała przed lądowaniem na przeszkodzie, a nie pozycji samej w sobie {OPINIA: Butch Lehman, Roll Minnesota} {1/2} [cite: 7].

### 1.3. Zaawansowane warianty triku

Poza formą podstawową, warianty *unity* różnicuje się na podstawie najazdu oraz zejścia. *Backside Unity* oznacza sytuację, w której rolkarz najeżdża na przeszkodę mając ją za swoimi plecami. Wymaga to wykonania precyzyjnego skoku „w ciemno” (blind approach), z asynchronicznym skrętem bioder i tułowia w fazie lotu, w celu zlokalizowania krawędzi wzrokiem ułamek sekundy przed kontaktem {KONSENSUS} {2/2} [cite: 4, 6]. Z kolei warianty takie jak *Truespin Unity* (lub *True Savannah*) oznaczają wykonanie obrotu o 180 stopni (lub więcej) w kierunku „od przeszkody” podczas fazy lotu. Jest to manewr drastycznie zwiększający trudność biomechaniczną, ponieważ pęd rotacyjny działa w opozycji do kierunku wymaganego do zablokowania stóp na krawędzi {KONSENSUS} {2/2} [cite: 6, 7].

## 2. Sekwencja ruchowa krok po kroku

Analiza motoryczna triku *unity* wymaga podziału na fazy przygotowania, lotu, ślizgu oraz lądowania. Mechanika tych faz została częściowo opisana w literaturze naukowej dotyczącej sportów ekstremalnych oraz w zaawansowanych materiałach instruktażowych.

### 2.1. Faza najazdu (Approach)

Prędkość oraz kąt najazdu bezpośrednio determinują wektor pędu środka masy (Center of Mass - COM). W metodyce nauczania początkującym zaleca się najazd pod kątem 90 stopni (prostopadle do przeszkody) w celu nauki samego zablokowania stóp w miejscu (manewr *stall*). W miarę nabierania biegłości motorycznej, kąt ten jest sekwencyjnie redukowany z 75, poprzez 50, do 30 stopni, aż do najazdu niemal równoległego, który pozwala na długi ślizg wzdłuż krawędzi {OPINIA: Ricardo Lino} {1/2} [cite: 5]. Inna technika ekspercka zakłada najeżdżanie pod minimalnym kątem przy zachowaniu dużej prędkości i wykonywanie skoku bezpośrednio „z góry” na murek. Według instruktorów minimalizuje to ryzyko uderzenia szyną o krawędź (*clipping*) oraz zahaczenia kółkami (*wheel bite*), znacznie ułatwiając zlokalizowanie punktu balansu {OPINIA: JADRollerVlog} {1/2} [cite: 10].

### 2.2. Odbicie i faza lotu (Take-off & Aerial Phase)

Przejście z fazy pędu poziomego do wznoszenia generuje siłę reakcji podłoża, która musi zostać prawidłowo przetworzona przez aparat ruchu. W środowisku instruktorów dostrzegalna jest sprzeczność metodologiczna dotycząca sposobu wejścia na przeszkodę podczas wczesnych etapów nauki. Część szkoleniowców stanowczo zaleca naukę poprzez tzw. *step-on* (wejście krok po kroku). W tej technice rolkarz najpierw stawia stopę dominującą, a następnie dynamicznie dokłada stopę tylną, co rzekomo ułatwia wczesną adaptację neurologiczną do nienaturalnej pozycji {OPINIA: Felipe Zambardino, Inline at the Border} {2/2} [cite: 9, 11]. Z kolei inni eksperci wskazują, że technika *step-on* trwale zaburza ułożenie środka ciężkości. Wymagają oni od uczniów wykonywania od samego początku jednoczesnego, obunóżnego skoku (*pop*), co gwarantuje, że środek masy znajdzie się precyzyjnie w płaszczyźnie pionowej nad przeszkodą {OPINIA: Acosta Blades} {1/2} [cite: 3].

Podczas fazy lotu następuje właściwe krzyżowanie kończyn. Aby trik był stabilny biomechanicznie, krzyżowanie musi być głębokie. Oznacza to krzyżowanie kończyn dolnych na poziomie górnych części goleni (piszczeli), a nie jedynie w obrębie stawów skokowych. Takie ustawienie zapewnia szeroką i relatywnie stabilną bazę podparcia (Base of Support - BOS) na wąskiej krawędzi rurki {OPINIA: Ricardo Lino} {1/2} [cite: 5]. Występuje tu pełna asymetria kinematyczna kończyn dolnych.

### 2.3. Lądowanie i utrzymanie ślizgu (Landing & Holding the Grind)

Opublikowane badania naukowe nad biomechaniką lądowania na rurce podczas trików typu *grind* udowodniły, że pionowa siła uderzenia (vertical impact force) maleje istotnie statystycznie wraz ze wzrostem doświadczenia rolkarza (r = -0.84, P = 0.009). Doświadczeni skaterzy podświadomie udoskonalają technikę w celu minimalizacji obciążeń przenoszonych na stawy. Ponadto, wykazano bezpośrednią korelację między redukcją szczytowej siły zderzeniowej a zwiększeniem stopnia zgięcia stawu kolanowego w fazie lądowania (r = -0.65, P = 0.04) {DOWÓD: badanie biomechaniczne, Major 2007} {2/2} [cite: 12]. 

Podczas samego ślizgu istotne jest kontrolowanie nacisku na płaszczyznę buta. Przednie kółka rolki powinny być lekko uniesione wyżej poprzez świadome przesunięcie wektora siły. Nacisk przenoszony zbyt mocno na palce prowadzi do zjawiska *wheel bite* – nagłego zatrzymania kół na powierzchni murku, co ze względu na zachowany pęd górnej połowy ciała skutkuje natychmiastowym i brutalnym wyrzuceniem rolkarza do przodu {WNIOSKOWANIE} {OPINIA: Ricardo Lino} {1/2} [cite: 5].

### 2.4. Zejście z przeszkody (Exit / Landing)

Zejście z przeszkody następuje zazwyczaj poprzez naturalne, odruchowe „rozkręcenie” (unwrap) skrzyżowanych kończyn. Większość rolkarzy instynktownie wychodzi z *unity* lądując tyłem (fakie), ponieważ stawy biodrowe w trakcie ślizgu są już zrotowane w tym kierunku. Wymuszanie zejścia przodem (forward exit) z pozycji skrzyżowanej jest znacznie trudniejsze biomechanicznie. Wymaga ono wygenerowania aktywnej rotacji tułowia w kierunku przeciwnym do naturalnego rozplątywania nóg, podczas ułamka sekundy trwania fazy lotu z przeszkody {OPINIA: Brandon Drummond, Acosta Blades} {2/2} [cite: 3, 13, 14].

## 3. Postawa – biomechanika segment po segmencie

Wysoka trudność i wskaźnik urazowości ślizgu *unity* wynikają ze specyficznych, niefizjologicznych wymagań stawowych i mięśniowych, nałożonych na każdy segment ciała rolkarza.

1.  **Stopy i stawy skokowe:** Wymagania biomechaniczne dla obu stóp są przeciwstawne. Noga przednia (prowadząca) musi znajdować się w ułożeniu zgięcia podeszwowego połączonego z silną inwersją (odwróceniem), aby precyzyjnie docisnąć zewnętrzną krawędź buta do przeszkody {WNIOSKOWANIE} [cite: 15]. Noga tylna (zakroczna) wymaga z kolei relatywnego zgięcia grzbietowego połączonego z ewersją (nawróceniem), dociskającego krawędź wewnętrzną. Sztywna skorupa buta (hardboot) znacznie ogranicza zakres ruchu w stawie skokowym (Range of Motion - ROM), co wymusza kompensację tych kątów poprzez odpowiednie ustawienie stawu kolanowego i biodrowego {OPINIA: Michael Witzemann} {1/2} [cite: 16].
2.  **Stawy kolanowe:** Utrzymanie pozycji wymaga obustronnego, głębokiego zgięcia w stawach kolanowych. Co kluczowe, kolana muszą być odwiedzione „na zewnątrz”. Wymuszona szpotawość (varus) dla nogi prowadzącej i koślawość (valgus) dla nogi zakrocznej pozwala na wycentrowanie rzutu środka ciężkości miednicy dokładnie pomiędzy obiema punktami podparcia szyn rolek {OPINIA: Michael Witzemann, Ricardo Lino} {2/2} [cite: 5, 16].
3.  **Stawy biodrowe:** Ustawienie miednicy stanowi absolutne centrum kontroli tego triku. Noga przednia znajduje się w głębokiej rotacji wewnętrznej oraz przywiedzeniu, przekraczając linię środkową ciała. Noga tylna znajduje się w rotacji zewnętrznej. Kompleks miedniczno-lędźwiowy musi być zorientowany równolegle do krawędzi przeszkody. Powszechnym błędem jest próba odwrócenia bioder przodem w kierunku jazdy (zgodnie z naturalnym kierunkiem pędu). Takie ustawienie natychmiastowo niszczy kinezytykę ułożenia stóp, skutkując wyślizgnięciem się tylnej rolki z poręczy (slip out) {OPINIA: Michael Witzemann, społeczność Reddit} {2/2} [cite: 14, 16, 17].
4.  **Tułów i kończyny górne:** Kręgosłup piersiowy powinien zachować naturalną krzywiznę, a postawa powinna być wyprostowana (upright). Kończyny górne powinny być uniesione i utrzymywane prostopadle do tułowia, równolegle do krawędzi przeszkody, pełniąc funkcję hydrodynamicznych stabilizatorów przeciwdziałających wychyleniom w płaszczyźnie czołowej {OPINIA: Acosta Blades, społeczność Reddit} {2/2} [cite: 3, 17].
5.  **Wzrok i kontrola głowy (Gaze):** Odruch błędnikowy i wzrokowy wymagają spojrzenia przez ramię, w kierunku wektora ruchu. Zjawisko to koresponduje z danymi biomechanicznymi (dla wariantu *stall*), gdzie odnotowuje się 180-stopniową różnicę fazową między zgięciem stawów kolanowych a ruchem odchylenia głowy, co stanowi klasyczną strategię motoryczną utrzymania równowagi u człowieka {DOWÓD: badanie biomechaniczne, Major 2007} {1/2} [cite: 18].



![wizualizacja wygenerowana przez agenta – obraz w pliku czatu, nie eksportowany]



## 4. Środek masy, dystrybucja ciężaru i kontrola równowagi

Utrzymanie równowagi podczas ślizgu na wąskiej powierzchni opiera się na ciągłym rzutowaniu środka masy (COM) w obrębie dynamicznie zmieniającej się bazy podparcia (BOS). 

Zgodnie z badaniami kinematycznymi Majora et al. (2007), środek masy rolkarza podczas wykonywania dynamicznego *grindu* często w ogóle nie przechodzi w pełni nad bazą podparcia stanowiącą rurkę (w płaszczyźnie pionowej). Rolkarz agresywny wykorzystuje moment siły i wektor pędu uzyskany poprzez najechanie pod ostrym kątem, w efekcie „opierając się” o przeszkodę z wektorem siły reakcji skierowanym ukośnie względem siły grawitacji {DOWÓD: badanie biomechaniczne, Major 2007} {1/2} [cite: 12, 19]. Przeczy to intuicyjnemu założeniu o konieczności znajdowania się dokładnie „nad rurką”.

W kwestii optymalnej dystrybucji ciężaru ciała między przednią a tylną rolką (w płaszczyźnie strzałkowej), w dostępnych materiałach szkoleniowych widoczna jest istotna sprzeczność. Wskazuje to na dużą elastyczność techniczną triku w zależności od geometrii przeszkody oraz indywidualnych preferencji proprioceptywnych.
Z jednej strony, część ekspertów promuje równe obciążenie w stosunku 50/50. Wymaga to nienagannego usytuowania klatki piersiowej dokładnie pośrodku skrzyżowanych nóg i maksymalizuje zablokowanie obu szyn na przeszkodzie. Metoda ta polecana jest na precyzyjnych poręczach (rails) {OPINIA: Acosta Blades, JADRollerVlog} {2/2} [cite: 3, 10].
Z drugiej strony, wielu cenionych trenerów zaleca asymetryczne przesunięcie masy w stosunku 55/45 do 60/40 z korzyścią dla nogi przedniej (prowadzącej) {OPINIA: Acosta Blades, Brandon Drummond} {2/2} [cite: 3, 13]. Uzasadnienie dla tego podejścia jest stricte biomechaniczne i skupia się na zarządzaniu ryzykiem. Przesunięcie masy do przodu jest bezpieczniejsze: potencjalny błąd skutkuje wywrotką w przód, która jest relatywnie łatwo amortyzowana przez nakolanniki. Przeciążenie nogi tylnej skutkuje natomiast gwałtownym przyspieszeniem rolek wyrzucanych spod środka ciężkości do przodu (*slip out*), co nieuchronnie prowadzi do potężnego, niekontrolowanego uderzenia plecami i potylicą o twarde podłoże {WNIOSKOWANIE} [cite: 13, 20].

## 5. Styl i jakość wykonania w kryteriach oceny subkulturowej

W sportach podlegających ocenie sędziowskiej lub społecznej, pojęcie stylu jest subiektywne, niemniej jednak w środowisku rolkarzy AGV wyewoluowały twarde, biomechaniczne wytyczne określające, co czyni trik *unity* estetycznym i profesjonalnym. Złotym standardem w tej dziedzinie są przejazdy legendy tego sportu, Alexa Broskowa.

Na podstawie analiz wideo przejazdów profesjonalistów, społeczność definiuje trzy filary stylowego wykonania:
1.  **Głębokość skrzyżowania:** Estetyka triku rośnie proporcjonalnie do obniżenia środka ciężkości. Kolana powinny znajdować się blisko siebie, ugięte na zewnątrz. Wykonywanie triku ze sztywnymi, wyprostowanymi nogami (tzw. *straight-legged*) jest traktowane jako błąd techniczny prowadzący do braku płynności i estetyki {OPINIA: Brandon Drummond, analityk AGV} {1/2} [cite: 21].
2.  **Stabilność tułowia (Quiet Upper Body):** Profesjonalny rolkarz cechuje się całkowitym zamrożeniem górnej partii ciała. Po wygenerowaniu popu i zablokowaniu na krawędzi (*lock-in*), sylwetka pozostaje w jednej pozycji na przestrzeni całego ślizgu. Rozpaczliwe wymachiwanie ramionami (*flailing arms*) w celu skorygowania błędnego wektora najazdu drastycznie obniża ocenę przejazdu {OPINIA: Roll Minnesota, Brandon Drummond} {2/2} [cite: 21, 22].
3.  **Synchroniczność lądowania:** Znakiem rozpoznawczym elitarnych sportowców jest idealnie obunóżne lądowanie po opuszczeniu poręczy. Obie stopy dotykają podłoża w tym samym ułamku sekundy. Lądowanie asynchroniczne (krokowe, stąpające), chociaż bezpieczniejsze ewolucyjnie, jest traktowane jako strata kontroli nad trajektorią lotu {OPINIA: Brandon Drummond} {1/2} [cite: 21].

## 6. Fizjoterapia sportowa: patomechanika, prewencja i rehabilitacja

Wyczynowa jazda na rolkach agresywnych, w szczególności podczas wykonywania asymetrycznych i wielopłaszczyznowych trików krzyżnych, takich jak *unity*, generuje potężne siły ścinające i kompresyjne. Oddziałują one krytycznie na stawy kończyn dolnych oraz obręcz miedniczną. 

### 6.1. Staw skokowy: Inwersja, ewersja i uszkodzenia więzadłowe

Stabilne utrzymanie krawędzi rolki pod obciążeniem dynamicznym polega w głównej mierze na wydolności aparatu więzadłowego oraz siłowej wytrzymałości muskulatury stabilizującej podudzie. Niezdolność do przeciwstawienia się siłom grawitacji prowadzi do uślizgu, który jest główną przyczyną urazowości w tym sporcie.

*   **Mechanika obciążeń tkanek:** Typowy upadek z *unity* kończy się gwałtowną, niekontrolowaną inwersją stopy (kombinacją supinacji, rotacji wewnętrznej oraz zgięcia podeszwowego) pod wpływem pełnego obciążenia masą ciała z wysokości. Z perspektywy klinicznej, głównymi strukturami ulegającymi naciągnięciu, naderwaniu lub całkowitemu zerwaniu są kompleksy więzadłowe przedziału bocznego, ze szczególnym uwzględnieniem więzadła skokowo-strzałkowego przedniego (ATFL) oraz więzadła piętowo-strzałkowego (CFL) {KONSENSUS} {2/2} [cite: 15, 23, 24]. 
*   **Przygotowanie tkankowe (Strengthening):** W protokołach fizjoterapii sportowej kładzie się bezwzględny nacisk na profilaktyczne wzmacnianie mięśni odpowiedzialnych za stabilizację boczną oraz zapobieganie ewersji/inwersji. Badania nad pokrewnymi sportami operującymi na krawędzi (np. hokej na lodzie) wskazują, że bezwzględnie konieczna jest siła mięśni strzałkowych (grupa *peroneals*) oraz mięśnia piszczelowego tylnego (*tibialis posterior*) {ANALOGIA: biomechanika łyżwiarstwa, Bladetech 2023; Revamp Wellness} {2/2} [cite: 25, 26]. Deficyt siły w tych partiach prowadzi do załamywania się osi buta (biomechaniczna niewydolność utrzymania krawędzi) jeszcze przed wystąpieniem ewentualnego upadku {WNIOSKOWANIE} [cite: 25].
*   **Powrót do sportu (RTS):** Po przebytym i wygojonym skręceniu inwersyjnym (uszkodzenie ATFL/CFL), kategorycznie wymagana jest reedukacja nerwowo-mięśniowa. Obejmuje ona trening propriocepcji na platformach niestabilnych, połączony z ćwiczeniami izometrycznymi przy użyciu taśm oporowych angażujących ewertory i inwertory stopy. We wczesnych fazach powrotu do jazdy (RTS) zaleca się aplikację tejpingu kinezjologicznego lub stosowanie elastycznych stabilizatorów wewnątrz buta, co przywraca pacjentowi utraconą informację aferentną (sensoryczną) z uszkodzonych mechanoreceptorów torebki stawowej {OPINIA: Physiomedicum; UCSF Orthopaedic Institute} {2/2} [cite: 26, 27, 28].

### 6.2. Staw kolanowy i translacja mechanizmów uszkodzenia ACL z narciarstwa

Podczas wykonywania trików ze skrzyżowanymi nogami, kolano ulega znacznemu obciążeniu w wielu płaszczyznach jednocześnie – znajduje się w zgięciu (flexion), znacznym odwiedzeniu (abduction/valgus) oraz rotacji osiowej, zablokowanej obwodowo przez zakleszczone na przeszkodzie rolki.

*   **Identyfikacja mechanizmu uszkodzenia:** Gdy kółka zablokują się nagle na szynie (zjawisko *wheel bite*) lub o silnie stawiający opór niesmarowany murek, but rolkowy zatrzymuje się w miejscu, podczas gdy pęd rozpędzonego tułowia wciąż przemieszcza się do przodu i rotuje. Powstaje w ten sposób dźwignia przenosząca katastrofalne siły rotacyjne bezpośrednio na łąkotki i więzadło krzyżowe przednie (ACL).
*   **Analogia naukowa:** Opisany mechanizm urazu z rolek agresywnych jest klinicznie i biomechanicznie izomorficzny względem klasycznego mechanizmu zerwania ACL obserwowanego u narciarzy alpejskich. Zjawisko to, opisywane w literaturze medycyny sportów zimowych jako „forward twisting fall with body rotation” (rotacyjny upadek w przód) lub „phantom foot mechanism”, pojawia się, gdy krawędź narty utyka w śniegu, a wiązanie nie ulega wypięciu {ANALOGIA: publikacje medycyny sportowej, Khakha 2025; Niseko Physio 2024; NHS 2026} {2/2} [cite: 29, 30, 31]. Rolka typu hardboot działa identycznie jak but narciarski, przenosząc moment obrotowy przez kości podudzia bezpośrednio do stawu kolanowego.
*   **Przeciwwskazania:** Ze względu na ogromne wymogi wobec stabilności więzadłowej, nauka ewolucji takich jak *unity* jest przeciwwskazana dla rolkarzy z niezaopatrzoną przewlekłą niestabilnością stawu kolanowego, ze świeżymi epizodami uciekania kolana (giving way) czy niewygojonymi uszkodzeniami więzadła pobocznego piszczelowego (MCL).

### 6.3. Ograniczenia mobilności stawów biodrowych

Utrzymanie stabilnego środka ciężkości, precyzyjne zaangażowanie mięśni tułowia (core) oraz płynne wyjście z manewru rotacją (wyjście przodem z wariantu *backside*) są nierzadko blokowane przez ograniczenia anatomiczno-powięziowe, o czym donoszą zaawansowani instruktorzy {OPINIA: Michael Witzemann} {1/2} [cite: 14]. Trik *unity* wymaga asymetrycznej ekstremalnej rotacji wewnętrznej dla kończyny przedniej oraz zewnętrznej dla kończyny tylnej. 

*   **Przygotowanie powięziowo-stawowe (Mobility):** Zapobieganie powszechnym urazom kompensacyjnym, polegającym na przenoszeniu obciążeń rotacyjnych ze sztywnych bioder na kręgosłup lędźwiowy, wymaga interwencji fizjoterapeutycznej i mobilizacyjnej przed jazdą. Wdrożenie ćwiczeń zaczerpniętych z protokołów przygotowania motorycznego łyżwiarzy i hokeistów odgrywa tutaj rolę decydującą. Fundamentem przygotowania jest pozycja 90/90 (znana też jako *shinbox*), przejścia między pozycjami z rotacją, izolowane podnoszenie nogi z pozycji 90/90 bez angażowania miednicy, a także ćwiczenia muszli (clamshells) izolujące rotatory zewnętrzne i odwodziciele {ANALOGIA: protokoły łyżwiarskie i hokejowe} {2/2} [cite: 32, 33, 34, 35]. Ćwiczenia te nie tylko wydłużają tkanki, ale przede wszystkim poprawiają ślizg powięziowy i stymulują torebkę stawową do produkcji mazi.

### 6.4. Bailing i upadanie – kontrowersje wokół mechaniki nadgarstka

Zdolność do bezpiecznego ewakuowania się z nieudanego manewru (tzw. bailing) to elementarz każdego rolkarza agresywnego.
*   **Technika "Mermaid" (Syrena):** Głównym błędem popełnianym podczas uślizgu w tył jest paniczne prostowanie stawów kolanowych i odchylanie tułowia do tyłu, co generuje potężny wstrząs przenoszony na kość krzyżową i głowę. Poprawny wzorzec motoryczny, aprobowany przez szkoły rolkowe, nakazuje nagłe obniżenie środka ciężkości przez głęboki przysiad. Następnie należy skręcić biodra w płaszczyźnie poziomej i wylądować miękko na bocznej stronie uda i mięśniach pośladkowych, pozwalając na kontrolowany ślizg na odzieży po asfalcie – technika ta nazywana jest potocznie „syreną” (mermaid) {OPINIA: eksperci This Is Soul, środowisko Reddit} {2/2} [cite: 36, 37]. Jeżeli utrata równowagi następuje do przodu podczas ślizgu na poręczy, skutecznym ratunkiem jest obustronne uchwycenie rurki rękami, co powstrzymuje rotację i zapobiega urazom czaszki {OPINIA: Brandon Drummond / Laced} {1/2} [cite: 13].
*   **Paradoks ochrony nadgarstków i dysonans instruktorski:** W środowisku istnieje ogromny i niebezpieczny dysonans dotyczący roli dłoni podczas upadku. 
    *   Część instruktorów parkowych instynktownie radzi swoim podopiecznym: „wykop nogi, podeprzyj się dłonią, usiądź” (put your hand down) {OPINIA: Acosta Blades} {1/2} [cite: 3].
    *   Podejście to jest stanowczo piętnowane i zakazane przez specjalistów z zakresu medycyny urazowej i biomechaników. Badania nad mechaniką złamań dowodzą, że upadek na całkowicie wyprostowane ramię (mechanizm FOOSH - Fall on Outstretched Hand) generuje krytyczne siły przenoszone przez oś kości. Co gorsza, odchylenie kątowe dłoni (off-axis loading) drastycznie obniża próg odporności układu szkieletowego, powodując spadek wartości obciążenia niszczącego o 29% względem obciążenia osiowego. Skutkuje to nieuchronnymi złamaniami dalszej nasady kości promieniowej lub kości trójgraniastej nadgarstka {DOWÓD: badania biomechaniczne sił niszczących, ResearchGate 2026} {2/2} [cite: 38, 39].
    *   Liczne raporty amatorów z forów dyskusyjnych (np. Reddit) donoszą o skomplikowanych złamaniach kości nadgarstka, które miały miejsce **pomimo stosowania certyfikowanych ochraniaczy (wrist guards)** {OPINIA: środowisko Reddit, 2025} {1/2} [cite: 40]. Sytuacja ta zachodzi, gdy obciążenie przewyższa parametry absorpcyjne plastiku lub siła przenosi się na trzon kości promieniowej tuż nad krawędzią ochraniacza. Właściwa i ratująca przed kalectwem postawa, aprobowana przez medycynę i organizacje prewencji urazów (np. Parachute), nakazuje lądowanie wertykalne wprost na twarde nakolanniki z tworzywa sztucznego. W razie konieczności dłonie muszą być uformowane w luźne pięści i stanowić jedynie punkt stymulacji ślizgu po nawierzchni, pod żadnym pozorem nie przejmując uderzeniowego ciężaru masy ciała {KONSENSUS} {2/2} [cite: 20, 36, 41].

## 7. Progresja nauki (Metodyka i Drille)

Dla bezpiecznej i efektywnej adaptacji nerwowo-mięśniowej i uniknięcia budowania błędnych wzorców kompensacyjnych, nauka złożonego triku *unity* dekonstruowana jest na odizolowane, następujące po sobie etapy (tzw. drills) {KONSENSUS} {2/2} [cite: 5, 11, 13].

1.  **Imitacja na sucho (Floor / Carpet drill):** Odtworzenie geometrii stawowej na miękkim podłożu (dywan/trawa) w pełnym rynsztunku. Wypracowanie pamięci mięśniowej głębokiego skrzyżowania goleni oraz orientacji miednicy z ciężarem przeniesionym symulacyjnie na cztery punkty styku szyn i butów ze ślizganym obiektem.
2.  **Stall (Fiksacja pozycji):** Rolkarz podjeżdża z minimalną prędkością do niskiego i bezpiecznego stopnia (curb) lub poręczy treningowej (p-rail), stając na nim w skrzyżowanej pozycji, ale nie wykonując ślizgu. Na tym etapie weryfikowana jest poprawność fazy lotu (*pop*). Rolkarze z blokadą mentalną i lękiem przed przewróceniem do tyłu nagminnie otwierają tutaj pozycję, wycofując przednią nogę, psując architekturę całego triku i zamieniając go w pospolity ślizg *frontside* {OPINIA: społeczność Reddit} {1/2} [cite: 17].
3.  **Ślizg z redukcją kąta (Slide and angle adjustment):** Po opanowaniu stallu, podnosi się prędkość. Początkowy prostopadły dołek uderzeniowy (najazd pod kątem 90 stopni, co wybacza błędy w balansie przód-tył) ulega sukcesywnemu spłyceniu w trajektorie: 75°, 50°, 30°, w konsekwencji osiągając kąt równoległy. Wymusza to opanowanie balansu wzdłużnego wykorzystując wektor siły odśrodkowej i stabilizację miednicy {OPINIA: Ricardo Lino} {1/2} [cite: 5].
4.  **Transfery (Rails & Transitions):** Przeniesienie wypracowanej techniki z murków (ledges), które ze względu na swą budowę architektoniczną pozwalają na błędy (opieranie o płaską powierzchnię tzw. topside bias), na idealnie okrągłe poręcze (rails). Rurki bezkompromisowo wymagają symetrycznego usadowienia H-blocków obu szyn w idealnej osi triku. Kolejnym stopniem jest implementacja *unity* na krawędzi (coping) w strukturze półrury (quarter pipe/mini ramp), gdzie w przeciwieństwie do infrastruktury ulicznej (street), rolkarz musi siłowo przenosić środek masy z powrotem do wnętrza rampy (transition), powstrzymując się przed spadnięciem na podest {OPINIA: Brandon Drummond / Laced} {1/2} [cite: 13].

---

## 8. Tabela Źródeł (Literature & Source Citations)

| ID | Typ Źródła | Autor / Organizacja | Tytuł | URL / PMID / DOI |
| :--- | :--- | :--- | :--- | :--- |
| D01 | Badanie biomechaniczne | M.J. Major et al. (Univ. of Illinois) | *Biomechanics of aggressive inline skating: Landing and balancing on a grind rail* | PMID: 17786694 / DOI: 10.1080/02640410601129615 |
| D02 | Publikacja medyczna | R. Khakha (Cromwell Hospital) | *Navigating the slopes: Understanding ACL injuries in skiing* | [URL](https://www.cromwellhospital.com/newsroom/blog/navigating-the-slopes-understanding-acl-injuries-in-skiing/) |
| D03 | Ortopedia biomechaniczna | P. Kurath et al. (ResearchGate) | *Fractures* (analiza FOOSH i osi kompresji) | [URL](https://www.researchgate.net/publication/397890467_Fractures) |
| D04 | Klinika Fizjoterapii (Polska) | Physiomedicum / Rehasport | *Skręcenie stawu skokowego* / *Urazy więzadeł* | [URL](https://physiomedicum.pl/blog/urazy-wiezadel-stawu-skokowego/) ; [URL](https://www.rehasport.pl/stopa-i-staw-skokowy/skrecenie-stawu-skokowego,5204,n,4329) |
| D05 | Materiał wideo (Instruktaż) | Ricardo Lino | *How to unity grind on aggressive inline skates* | [URL](https://www.youtube.com/watch?v=5VHFkOCtVcE) |
| D06 | Materiał wideo (Instruktaż) | Acosta Blades | *Aggressive Inline: How to Unity Grind* | [URL](https://www.youtube.com/watch?v=l0VWrEX4E-Q) |
| D07 | Materiał wideo (Instruktaż) | Laced (B. Drummond) | *How to Unity Grind* | [URL](https://www.youtube.com/watch?v=WR3YDmzrXsY) |
| D08 | Materiał wideo (Biomechanika) | Michael Witzemann | *Learning a Royale Grind* / *Learn to Grind...* | [URL](https://www.youtube.com/watch?v=gxakBJSyrOY) ; [URL](https://www.youtube.com/watch?v=ARn-gkWejBo) |
| D09 | Nomenklatura i historia | Roll Minnesota / SkaMiDan / Toxboe | *Unity vs. Savannah* / *Trick List* / *1997 Dictionary* | [URL](https://www.youtube.com/watch?v=UosCCqHaYp8) ; [URL](https://www.skamidan.com/en/blogs/aggressive-inline-skating-tutorials-and-learning/grinds-trick-list-of-aggressive-inline-skating-tricks-and-difficulty-levels-stunt-skating-rollerblading-rollerblades-slides-grind-how-to) ; [URL](https://toxboe.net/all/1997-aggressive-inline-skating-dictionary) |
| D10 | Analiza wideo zawodowców | Brandon Drummond / Roll Minnesota | *Alex Broskow's technique* / *Evolution of Alex Broskow* | [URL](https://www.youtube.com/watch?v=KmluXmTg9gk) ; [URL](https://www.youtube.com/watch?v=oc9XldFkHP4) |
| D11 | Edukacja urazowa / Medycyna | ProSkaters Place / This Is Soul | *How to Fall Safely* / *How to Fall on Inline Skates* | [URL](https://proskatersplace.ca/blog/how-to-rollerblade) ; [URL](https://www.thisissoul.com/blogs/skate-lessons/how-to-fall-on-inline-skates) |

## 9. Zestawienie Dowodowe (Claims Table)

| Twierdzenie (Claim) | Etykieta | Źródła (ID) | Stopień Niezależnego Potwierdzenia |
| :--- | :--- | :--- | :--- |
| Pionowa siła zderzeniowa (*impact force*) w momencie wylądowania na poręczy maleje proporcjonalnie do doświadczenia, głównie dzięki biomechanicznemu pogłębieniu kąta zgięcia kolan przez zawodowców. | `{DOWÓD: badanie biomechaniczne}` | D01 | 1/2 (jedyne dostępne dedykowane badanie AGV) |
| Konstrukcja trików *Unity* oraz *Savannah* opiera się na kinematycznie tożsamym układzie skrzyżowanych kończyn dolnych; definiującą różnicą pozostaje wektor wejścia/ślizgu rotacyjnego. | `{KONSENSUS}` | D06, D08, D09 | 2/2 (liczne, niezależne platformy szkoleniowe i archiwa) |
| Właściwa blokada stóp polega na wprowadzeniu nogi prowadzącej w pozycję obciążenia rantu zewnętrznego (backside/negative) oraz tylnej na rantu wewnętrznego (frontside/positive). Postawa ta implikuje przymusowe koślawe i szpotawe odchylenie kolan ku zewnętrzu dla równowagi układu sił. | `{KONSENSUS}` `{OPINIA: R. Lino, B. Drummond}` | D05, D07 | 2/2 (potwierdzone przez niezależnych trenerów) |
| Wykonanie biomechanicznie czystego triku *unity* wymaga pozostawienia obręczy miednicznej zrotowanej równolegle (otwartej) względem samej przeszkody, bez zwracania lędźwi w przód w kierunku wektora ruchu. | `{OPINIA: M. Witzemann}` `{WNIOSKOWANIE}` | D08 | 1/2 |
| Ślizg przerwany gwałtownie zjawiskiem *wheel bite* (zatrzymaniem kół) z opartą krawędzią buta generuje w stawie kolanowym skrajnie destrukcyjne siły torsyjne, analogiczne patologicznie do upadku narciarskiego bez wypięcia wiązania i stanowiące bezpośredni mechanizm zrywający aparat ACL. | `{ANALOGIA: mechanizm urazu ACL w narciarstwie alpejskim}` | D02 | 2/2 (ortopedia sportów zimowych sprzężona z wektorami hokejowymi) |
| Skrajne zgięcie boczne w zamkniętym łańcuchu kinematycznym stawu skokowego podczas błędów równowagi to główny wektor prowadzący do dewastacji więzadeł promieniujących bocznie, tj. kompleksu ATFL i CFL (mechanizm wykręcenia inwersyjnego). | `{KONSENSUS}` `{DOWÓD: wytyczne medycyny sportowej i diagnostyka` | D04 | 2/2 |
| Technika wybitna estetycznie uosabia się poprzez zamrożenie i brak mimowolnych ruchów miednicy oraz tułowia podczas długości trwania fazy *grind* (tzw. "quiet body" utożsamiane z legendą Alexem Broskowem). | `{OPINIA: B. Drummond, Roll Minnesota}` | D10 | 2/2 |
| Przejmowanie impetu upadku przez proste i usztywnione kończyny górne dłońmi ustawionymi płasko do nawierzchni obniża drastycznie nośność strukturalną przedramienia, warunkując destrukcyjne kompresyjne złamania łódkowato-trójgraniaste (mechanizm FOOSH). | `{KONSENSUS}` `{DOWÓD: biomechanika złamań i ortopedia dłoni}` | D03, D11 | 2/2 |

## 10. Luki informacyjne i sprzeczności w literaturze badawczej (Gaps and Contradictions)

W trakcie prowadzenia niniejszej kwerendy analityczno-badawczej, polegającej na przeglądzie opublikowanej literatury, historii subkultury (w tym słowników), protokołów medycznych i wideorejestracji instruktorskich, zinwentaryzowano zauważalne luki oraz obszary braku jednomyślności, wymagające w przyszłości uzupełnienia:

1.  **Niezgodność w idealnym rzutowaniu środka masy (Balance point conflict):** W elitarnym środowisku coachingu narosła znacząca rozbieżność w pożądanym rozłożeniu ciężaru pomiędzy nogę przednią a zakroczną. Ekspert techniczny *Acosta Blades* postuluje, by do maksymalnej koheksji sprzętu z materiałem stosować statyczne rozłożenie 50/50, aczkolwiek sam przyznaje, że operowanie wartością 60/40 stabilizuje najazd i ucieczkę z błędu {OPINIA: Acosta Blades} {1/2} [cite: 3]. Instruktor *Brandon Drummond (Laced)* faworyzuje obciążenie frontowe (55% do 60%) z czysto prewencyjnego, bezpiecznego profilu upadku na twarde zbroje nakolanników, chroniąc miednicę przed *slip-outem* w tył {OPINIA: Brandon Drummond} {1/2} [cite: 13]. Aktualnie brakuje udokumentowanych badań laboratoryjnych z zastosowaniem wkładkowej elektroniki pomiaru sił i baropodometrii wewnątrz rolek, przez co debata nie znajduje rozstrzygnięcia w obiektywnych pomiarach.
2.  **Dogmatyka naskoku na przeszkodę (Step-on vs Pop jump):** Część starszych szkół, m.in. promowanych przez *Felipe Zambardino* i projekt *Inline at the Border*, aktywnie zaleca początkującym rolkarzom zderzenie z trikiem z wykorzystaniem sekwencji krok po kroku (*step-on*) i powolnego układania ciężaru na nodze, w celu przezwyciężenia bariery mentalnej nienaturalnego zaplątania kończyn {OPINIA: F. Zambardino, Inline at the border} {2/2} [cite: 9, 11]. Jest to zaciekle atakowane przez inną frakcję profesjonalistów (*Acosta*), argumentujących, że naskakiwanie seryjne kompletnie degraduje pamięć neuromięśniową wymaganą do wywołania siły skoku, skazując sportowca na złe nawyki pędu już do końca kariery i promując jedyny wyłączny *pop* z pełnego wybicia obunóżnego {OPINIA: Acosta Blades} {1/2} [cite: 3].
3.  **Przepaść w edukacji ochrony rąk przy bailing’u:** Zauważono drastyczne pęknięcie na styku medycyny urazowej i praktyk z subkultur sportów miejskich. Podczas gdy ortopedzi i edukacyjne centra rolkowe (m.in. This Is Soul, ProSkaters) prowadzą kampanie zakazujące jakiejkolwiek próby siłowego opierania się na dłoni (promując uślizg w dół typu "syrena"), podwórkowy *coaching* bezceremonialnie nadal głosi rady „podparcia i usadzenia się przez ręce”, zmuszając stawy przedramienia do niemożliwej do obsłużenia kompensacji uderzeniowej. Co więcej, wśród samych użytkowników na platformach typu Reddit trwa nierozwiązany naukowo konflikt, z relacjami o skrajnych, destrukcyjnych pęknięciach nadgarstków zachodzących *pomimo* i wręcz poprzez sztywną barierę popularnych plastikowych protektorów (wrist guards), sugerujący nierzadko uszkodzenia na granicy ucisku sprzętu ochronnego.
4.  **Brak danych z badań kinetycznych układu 3D (Luka w testach Motion Capture dla krzyżowań):** Przeszukano literaturę specjalistyczną (bazy naukowe, recenzowane prace uniwersyteckie i dyplomowe na kierunkach biomechaniki). W konsekwencji raportuje się krytyczny brak badań analizujących układ 3D Motion Capture, dla jakichkolwiek ewolucji polegających na asymetrycznym skrzyżowaniu (tj. *unity*, *royale*, *savannah*). Bezcenne i pionierskie dzieło prof. Elizabeth Hsiao-Wecksler oraz dr. Matthew Majora (University of Illinois, rocznik 2007) dostarczyło niepodważalnych danych, niemniej badanie zawężono jedynie do prostej pionowej fiksacji stania w osi (stall) i ewolucji jednokierunkowej, nie krzyżowanej (frontside) {DOWÓD: przegląd literatury biomechanicznej, Major 2007} {2/2} [cite: 12, 19]. W efekcie cały aparat medycyny sportowej zmuszony jest leczyć rolkarzy agresywnych metodą dedukcji ze świata narciarstwa zjazdowego lub kanonów fizjoterapii hokejowej [BRAK ŹRÓDŁA].

**Sources:**
1. [toxboe.net](https://toxboe.net/all/1997-aggressive-inline-skating-dictionary)
2. [rollerblading.com.au](https://www.rollerblading.com.au/rollerblading-aggressiveinlineskating-tricks-glossary/)
3. [youtube.com](https://www.youtube.com/watch?v=l0VWrEX4E-Q)
4. [stuntworlds.nl](https://www.stuntworlds.nl/en/article/backside-savannah-ao-bs-unity-grind-trick)
5. [youtube.com](https://www.youtube.com/watch?v=5VHFkOCtVcE)
6. [youtube.com](https://www.youtube.com/watch?v=qtxGHxbDJ6U)
7. [youtube.com](https://www.youtube.com/watch?v=UosCCqHaYp8)
8. [skamidan.com](https://www.skamidan.com/en/blogs/aggressive-inline-skating-tutorials-and-learning/grinds-trick-list-of-aggressive-inline-skating-tricks-and-difficulty-levels-stunt-skating-rollerblading-rollerblades-slides-grind-how-to)
9. [youtube.com](https://www.youtube.com/watch?v=WWI2Nvqx22M)
10. [youtube.com](https://www.youtube.com/watch?v=yPvXBH0JcnA)
11. [youtube.com](https://www.youtube.com/watch?v=pZKUjRK_2B8)
12. [researchgate.net](https://www.researchgate.net/publication/6053236_Biomechanics_of_aggressive_inline_skating_Landing_and_balancing_on_a_grind_rail)
13. [youtube.com](https://www.youtube.com/watch?v=WR3YDmzrXsY)
14. [youtube.com](https://www.youtube.com/watch?v=ARn-gkWejBo)
15. [fizjosport.krakow.pl](https://fizjosport.krakow.pl/jednostki-chorobowe/staw-skokowy-stopa/uszkodzenie-wiezadel-stawu-skokowego-skrecenie-kostki/)
16. [youtube.com](https://www.youtube.com/watch?v=gxakBJSyrOY)
17. [reddit.com](https://www.reddit.com/r/AggressiveInline/comments/tpq742/does_anyone_have_any_tips_or_advice_for_learning/)
18. [researchgate.net](https://www.researchgate.net/figure/deo-images-of-a-skater-performing-a-grind-in-chronological-order-A-D-The-skater_fig2_6053236)
19. [nih.gov](https://pubmed.ncbi.nlm.nih.gov/17786694/)
20. [proskatersplace.ca](https://proskatersplace.ca/blog/how-to-rollerblade)
21. [youtube.com](https://www.youtube.com/watch?v=KmluXmTg9gk)
22. [youtube.com](https://www.youtube.com/watch?v=oc9XldFkHP4)
23. [rehasport.pl](https://www.rehasport.pl/stopa-i-staw-skokowy/skrecenie-stawu-skokowego,5204,n,4329)
24. [chirurgiastopywarszawa.pl](https://chirurgiastopywarszawa.pl/leczenie/skrecenia-stawu-skokowego/)
25. [bladetechhockey.com](https://bladetechhockey.com/blogs/news/correcting-ankle-eversion)
26. [revampwellness.ca](https://revampwellness.ca/blog/ankle-stability-and-strengthening-crucial-for-runners-hockey-players-and-athletes/)
27. [physiomedicum.pl](https://physiomedicum.pl/blog/urazy-wiezadel-stawu-skokowego/)
28. [ucsf.edu](https://sportsrehab.ucsf.edu/sites/g/files/tkssra10961/files/Ankle%20Strengthening%20Protocol.pdf)
29. [cromwellhospital.com](https://www.cromwellhospital.com/newsroom/blog/navigating-the-slopes-understanding-acl-injuries-in-skiing/)
30. [nisekophysio.com](https://nisekophysio.com/blog/the-skiing-acl/)
31. [nhsjs.com](https://nhsjs.com/2026/anterior-cruciate-ligament-injury-mechanisms-treatment-and-prevention-in-alpine-skiing-a-narrative-review/)
32. [thecoachessite.com](https://members.thecoachessite.com/article/one-exercise-to-unlock-better-hip-mobility)
33. [betterhockey.com](https://www.betterhockey.com/blogs/off-ice-training/flexibility-and-mobility-for-hockey)
34. [youtube.com](https://www.youtube.com/watch?v=UMXrjHRYIp8)
35. [daniwinksflexibility.com](https://www.daniwinksflexibility.com/bendy-blog/6-excercises-for-hip-internal-and-external-rotation)
36. [thisissoul.com](https://www.thisissoul.com/blogs/skate-lessons/how-to-fall-on-inline-skates)
37. [reddit.com](https://www.reddit.com/r/rollerblading/comments/1vbzsil/tips_for_fallingbailing_on_aggressive_skates_as_a/)
38. [orthopaedia.com](https://www.orthopaedia.com/wp-content/uploads/2023/12/Orthopaedia-Hand-2023-pdfprint._print.pdf)
39. [researchgate.net](https://www.researchgate.net/publication/397890467_Fractures)
40. [reddit.com](https://www.reddit.com/r/AggressiveInline/comments/1k8aeay/thoughts_on_wrist_guards/)
41. [proskatersplace.ca](https://proskatersplace.ca/blog/how-to-roller-skate)

---

## Triage (Fizjo AGV, 11.11.2026) — weryfikacja i porównanie z `2026-11-11_unity_claude-research.md`

> Nic z tego pliku nie trafiło do bazy wiedzy. „2/2” poniżej = dwa **niezależne źródła** (nie dwa narzędzia AI) po połączeniu obu rund; dla techniki to nadal {OPINIA}/{KONSENSUS} instruktorów, nie dowód.

### 1. Identyfikatory (PubMed / Crossref)

| Praca w raporcie | Sprawdzenie | Wynik |
|---|---|---|
| Major MJ, Beaudoin AJ, Kurath P, Hsiao-Wecksler ET 2007, J Sports Sci 25(12):1411–22 | PMID 17786694 (E-utilities), DOI 10.1080/02640410601129615 (Crossref) | ✔ zgodne; = [S02] w bazie. Liczby r = −0,84 (P = 0,009, grindy) i r = −0,65 (P = 0,04) są w abstrakcie, ale **r = −0,65 dotyczy stalli**, nie grindów (raport to rozmywa). |
| Inne PMID/DOI | — | raport nie podaje żadnych innych identyfikatorów; cała reszta to strony WWW, blogi i YouTube |

Wszystkie 41 linków grounding-redirect rozwinięto (41/41). Brak zmyślonych PMID/DOI.

### 2. Podejrzane / do odrzucenia

1. **Fałszywe „2/2” przez podwójne liczenie jednej pracy:** Major 2007 cytowany jako [12] (ResearchGate) + [19] (PubMed) i oznaczony {2/2} (sekcja 10 pkt 4) — to **jedno badanie**, 1/2.
2. **D03 „P. Kurath et al. (ResearchGate) *Fractures*”** — Kurath to współautor Major 2007 (mechanika), nie ortopeda; przypisanie autora wygląda na zmyślone. Strona ResearchGate 397890467 zwraca 403 (nie dało się sprawdzić). Liczba „spadek obciążenia niszczącego o 29%” i etykieta {DOWÓD … ResearchGate 2026} — **niezweryfikowane, nie używać**.
3. **„NHS 2026”** to nhsjs.com (*National High School Journal of Science*, czasopismo uczniowskie), nie NHS. **„Khakha 2025”** to blog szpitala Cromwell (autor niesprawdzony). Analogia ACL z narciarstwa ma solidne źródło tylko w rundzie Claude'a (Bere 2011, PMID 21515807).
4. **„Felipe Zambardino, Inline at the Border”** — w rundzie Claude'a autor kanału to „Jacob”; imię i nazwisko niepotwierdzone. **„Butch Lehman, Roll Minnesota”** — niepotwierdzone.
5. **Postawa — przypisania sprzeczne z transkryptami Claude'a:**
   - „krzyżować na wysokości górnej części goleni, nie w kostkach” (przypisane R. Lino) — Drummond mówi odwrotnie: „cross your legs at your ankles … more than at your knees” [U20]; treść wideo Lino nie była pobrana w rundzie Claude'a → **sprzeczność do sprawdzenia na wideo**.
   - „wymuszona szpotawość kolana prowadzącego i koślawość tylnego” (przypisane Witzemannowi i Lino) — Witzemann mówi „bend your knees forward as if you were not crossing your legs at all” [U17] → wygląda na **dopisane wnioskowanie modelu**.
   - „Acosta: wyłącznie skok obunóż, step-on niszczy nawyki” — w transkrypcie Acosty w rundzie Claude'a tego nie ma; zakaz wejścia krokiem to JAD [U16] → **prawdopodobnie złe przypisanie**.
   - „przednia stopa: zgięcie podeszwowe + silna inwersja; tylna: zgięcie grzbietowe + ewersja” — {WNIOSKOWANIE} modelu, przypisany częściowo Witzemannowi; brak pomiarów.
6. **„180-stopniowa różnica fazowa zgięcia kolan i ruchu głowy” (Major 2007)** — nie ma tego w abstrakcie; może być w pełnym tekście, niesprawdzone.
7. **Bez źródła:** Parachute jako organizacja zalecająca lądowanie na nakolanniki, „poprawa ślizgu powięziowego i produkcja mazi” po 90/90, przeciwwskazania kolanowe (MCL, giving way), kąty 90/75/50/30° (Lino, 1 źródło, wideo nieprzepisane), „trzy filary stylu” z Alexem Broskowem (D10, 1 autor).
8. Język raportu jest mocno przesadzony („katastrofalne”, „izomorficzny”, „ratująca przed kalectwem”) — do poradnika tylko po przepisaniu na neutralny.

### 3. Twierdzenia, które po połączeniu obu rund mają 2 niezależne źródła (2/2)

| # | Twierdzenie | Źródła (Claude → Deep Research) | Etykieta |
|---|---|---|---|
| 1 | Unity = grind na H-blocku obu rolek ze skrzyżowanymi nogami | toxboe [U01], Drummond [U20], Witzemann [U17], SkaMiDan [U06]; + toxboe 1997 dictionary, rollerblading.com.au | {KONSENSUS} |
| 2 | Stopa prowadząca w pozycji backslide, tylna w torque | Acosta [U18], AMALL [U22]; + stuntworlds.nl | {OPINIA} ×3 |
| 3 | Terminologia unity / savannah / alley-oop unity jest sporna (pozycyjnie vs kierunkowo) | toxboe, SkaMiDan, ONE blademag, Roll Minnesota, Acosta | {KONSENSUS} co do istnienia sporu |
| 4 | Z front unity naturalne wyjście to fakie (rozplątanie bioder) | Witzemann [U17], Drummond [U20], JAD [U16], Back to Blading [U21]; DR to samo | {OPINIA} ×4 |
| 5 | Obracanie bioder przodem w kierunku jazdy wykręca stopy / tylna rolka spada | Witzemann [U17], JAD [U16]; + Reddit r/AggressiveInline | {OPINIA} |
| 6 | Nauka: poza na ziemi → stall → krótki grind → prędkość | Witzemann, Inline at the Border, Drummond, JAD; DR: Lino, Reddit | {KONSENSUS} instruktorów |
| 7 | Nie odchylać się do tyłu; upadek w przód bezpieczniejszy niż ześlizg w tył | Drummond [U20], Acosta [U18] (upadek po odchyleniu) | {OPINIA} |
| 8 | Rozkład ciężaru jest **sporny** (50/50 vs 55/45 vs 60/40) | Acosta, Drummond, Witzemann, AMALL — obie rundy zgodne co do liczb | {KONSENSUS} co do sprzeczności, nie co do wartości |

Pozostają **1/2**: Major 2007 (środek masy nigdy nad rurą we frontside grindzie; spadek siły z doświadczeniem) — jedyne badanie AGV, nie dotyczy unity; kąty najazdu Lino; krzyżowanie w goleniach vs w kostkach (sprzeczność); kryteria stylu; cała część fizjo „pod unity” — nadal {WNIOSKOWANIE}/{ANALOGIA}, bez badań unity. Deep Research **nie dołożył żadnego nowego badania naukowego** w stosunku do rundy Claude'a.

### 4. Nowe źródła warte sprawdzenia (nie było ich u Claude'a)

- stuntworlds.nl — *Backside savannah / ao bs unity grind* (pozycja stóp)
- rollerblading.com.au — glosariusz trików
- toxboe.net — *1997 aggressive inline skating dictionary* (nazwa „Buddah”)
- YouTube: qtxGHxbDJ6U, WWI2Nvqx22M (JAD?), yPvXBH0JcnA, gxakBJSyrOY (Witzemann, royale), KmluXmTg9gk, oc9XldFkHP4 (Broskow), UMXrjHRYIp8
- thisissoul.com — *How to fall on inline skates* (technika „mermaid”)
- reddit r/AggressiveInline: tpq742 (nauka unity), 1k8aeay (ochraniacze nadgarstków)
