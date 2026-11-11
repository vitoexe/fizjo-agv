# Research: poradnik „jak robić unity” — runda 1 (źródła)

> **To nie jest diagnoza ani porada medyczna.**

- Data: 2026-11-11 · Narzędzie: Claude (Claude Code) · Prompt: `prompts/poradnik-unity/1-claude-research.prompt.md`
- Status: **surowy research, nic nie wpisane do bazy.** ID `Uxx` są tymczasowe (nie kolidują z `Sxx` w `sources.md`). Odwołania `[Sxx]` to źródła już istniejące w bazie (zweryfikowane wcześniej, w tej rundzie ich nie otwierałem ponownie).
- Jak zbierano:
  - **strony WWW**: WebSearch + WebFetch (agent web-fetch), status HTTP podany w tabeli (sekcja 8);
  - **tutoriale wideo (YouTube)**: istnienie i metadane (tytuł, kanał, data) z `yt-dlp`; treść z **automatycznych napisów YouTube** (ASR), zamienionych na tekst. **Cytaty z wideo są z auto-napisów i mogą mieć błędy rozpoznawania mowy** (np. „porn star” = pornstar grind, „store” = stall, „P star” = pornstar). Obrazu nie oglądałem — nie wiem, co autor pokazuje, a czego nie mówi;
  - **badania**: NCBI E-utilities (esearch / esummary / efetch), czytane **abstrakty** (nie pełne teksty).
- Format cytatu: oryginał po angielsku w cudzysłowie + polskie streszczenie. Etykiety wg `METHODOLOGY.md`.
- **Najważniejszy wniosek z góry:** nie znaleziono żadnego badania biomechaniki unity (ani jakiegokolwiek grindu skrzyżowanego). Cała technika to {OPINIA} instruktorów z YouTube i glosariuszy; cała część fizjo to {WNIOSKOWANIE} i {ANALOGIA} z innych sportów.

---

## 1. Definicja i odmiany unity

### 1.1 Definicja

- Unity = grind w rowku (groove / H-block) obu rolek, ze skrzyżowanymi nogami. toxboe: „It is like a frontside, but your legs are crossed!” — „jak frontside, tylko z nogami skrzyżowanymi”. [U01] {OPINIA}
- Brandon Drummond: „essentially is h block grind with your legs crossed” — w zasadzie grind na H-blocku ze skrzyżowanymi nogami; można go robić frontside, backside, switch i regular. [U20] {OPINIA}
- Michael Witzemann: grind „on both your grooves” — na rowkach obu rolek; dodatkowo „boot down”, czyli dotykając rowka **i** „backside plate” (bocznej części buta przy rowku). [U17] {OPINIA}
- SkaMiDan (glosariusz) zalicza unity do „groove grinds” — grindów wyłącznie na H-blocku, w przeciwieństwie do soul plate. [U06] {OPINIA}
- H-block (Wikipedia, tabela części): „Area on frame between inner wheels that locks on obstacle and grinds” — część frame'a między środkowymi kółkami, która „zaczepia” o przeszkodę. [U07] {KONSENSUS}*(encyklopedia, nie ekspert)*
- Pochodzenie: Drummond twierdzi, że unity wymyślił „John Julio” (prawdopodobnie Jon Julio). [U20] {OPINIA} — **nie znalazłem drugiego źródła**; wyszukiwanie historii triku nie dało potwierdzenia. ⏳ 1/2.

### 1.2 Ustawienie stóp — która stopa jest skrzyżowana

To miejsce największego sporu terminologicznego (zob. sekcja 9).

- **toxboe (pozycyjnie):** w unity „your back leg's foot is put in front of the other” — stopa tylnej nogi idzie przed drugą; w savannah — za drugą („put behind the other”); savannah = „cross the front leg over the back leg - opposite of the unity”. [U01][U02] {OPINIA}
- **Acosta Blades (pozycja stóp + kierunek):** w unity stopa prowadząca jest w pozycji backslide, a tylna w pozycji torque; w savannah „the foot position is the same, all that changes is the direction in which you're going” — ustawienie stóp jest takie samo, zmienia się kierunek jazdy. [U18] {OPINIA}
- **Witzemann:** dla front unity z przeszkodą po prawej — prawa stopa prowadzi, lewa za nią. [U17] {OPINIA}
- **Drummond:** dwa „sposoby” wejścia w unity: jak z pornstara (stopę soul przenosi się do H-blocka) albo jak z top acida (stopę topside przenosi się do H-blocka); uczy wersji z pornstara, bo „much easier and I think it looks the best”. [U20] {OPINIA}
- **Acosta (back unity):** unity to „a 90 degree turn of one foot” — obrót jednej stopy o 90° względem znanego grindu (acid → torque w back unity; top star → backslide). [U19] {OPINIA}
- **AMALL (back unity):** jedna stopa w pozycji backslide (z przodu), tylna w pozycji torque (za nią). [U22] {OPINIA}

### 1.3 Która część buta / frame'a dotyka przeszkody

- Rowek H-block obu rolek. [U01][U06][U17][U20] {OPINIA} — zgodne.
- Dodatkowo bok buta („boot down”, „backside plate”):
  - Witzemann: rowek **i** backside plate na obu rolkach. [U17]
  - Drummond: „both your feet should be in your backside plates when you're grinding this”. [U20]
  - JAD: „you want to be in your grooves but at the same time you want to be on your back side a little bit” — w rowkach, ale też trochę na boku buta. [U16]
  - toxboe (royale, baza unity): „grind on the frame AND on the outside boot. This will lock the skate to the position.” [U03] {OPINIA}
- **Odmienny opis:** Inline at the Border: „sliding on both of our frames … naturally you're going to be sliding on a bit of your soul grooves” — mówi o „soul grooves”, nie o boku buta. [U15] {OPINIA} — możliwe, że to inne nazwanie tej samej strefy albo błąd ASR; **do sprawdzenia na obrazie**.
- Zbyt nisko → „flattening out on your boot” i wychodzi „more like a unity cess slide thing” (JAD). [U16] {OPINIA}

### 1.4 Odmiany

| Odmiana | Opis ze źródeł | Źródło |
|---|---|---|
| (frontside) unity | domyślne znaczenie słowa „unity” — „If you simply say "Unity", … the frontside variant is usually meant” | [U06] |
| backside unity | ta sama pozycja nóg, palce skierowane **od** przeszkody (Witzemann: „you're facing your toes away from the spot”) | [U17][U06] |
| „neutral unity” | trzecia odmiana podejścia w komentarzu Seana Michaelsona: „frontside unity, neutral unity, and backside unity” | [U10] (komentarz czytelnika) |
| alley-oop unity / savannah | spór: część osób = to samo; SkaMiDan: „Savannah Grind (Alleyoop Unity Grind)”, „Backside Savannah Grind (Alleyoop Backside Unity Grind)” — poziom **zaawansowany** | [U05][U08][U09][U10][U24] |
| true(spin) unity | **BRAK ŹRÓDŁA** z definicją „true unity”. Pojawia się tylko jako hasło w liście czytelnika („True spin unity”) [U08] i w komentarzu Cherry-Garrarda („true front unity”) [U10]. Roll Minnesota proponuje, by „alley-oop” i „true spin” oznaczały wyłącznie obroty 180° do/od przeszkody [U24]. | [U08][U10][U24] |
| channel unity | unity w kanale przeszkody („Unity Grind → Channel Unity Grind”) | [U06] |
| „disaster” unity | toxboe: „do a unity grab and landing a unity” (air z grabem przed grindem) | [U04] |

- Poziom trudności: SkaMiDan — unity i backside unity w kategorii **Intermediate**; savannah/alley-oop unity w **Advanced**. [U05] {OPINIA}
- Witzemann: „basic trick, but … not … your very first grind”. toxboe: „looks hard, but it really isn't”. [U17][U01] {OPINIA}

---

## 2. Motoryka krok po kroku

> Wszystko poniżej to {OPINIA} instruktorów (wideo/strony). Brak badań.

### 2.1 Najazd

- **Kąt:** Witzemann — „slight angle, not fully parallel”; lekki kąt pomaga mieć biodra nad przeszkodą. Wjazd bardziej równoległy na back unity nazywa „common mistake”. [U17]
- Acosta: „you're going to want to have a nice angle at it”. [U18]
- AMALL (back unity, długi murek): „come at it a little more parallel than you normally do” — bardziej równolegle niż zwykle, żeby zachować prędkość. [U22]
- AMALL (alley-oop unity): „go more of an angle than usual”. [U23]
- JAD: „I approach the ledge pretty straight on … you don't have to turn as much as you think”. [U16]
- → **sprzeczność** co do kąta (sekcja 9). Jedyny dowód o kącie najazdu dotyczy frontside grindu: Major 2007 — środek masy nie przechodził nad rurą, autorzy sugerują równowagę z pędu przy **ukośnym** najeździe. [S02] {DOWÓD:obserwacyjne} — inny grind, n=10.
- **Prędkość:** toxboe — umiarkowana; „you can just slow down, if you do not feel comfortable” [U01]; Witzemann — „as slow or fast as you feel comfortable with” [U17]; Inline at the Border — w kroku 3 „as much speed as we feel comfortable with” [U15].
- **Stopy przy najeździe:** Witzemann — równolegle, równy ciężar na obu. [U17]

### 2.2 Wybicie i skrzyżowanie

- Witzemann: wybicie z obu nóg; obie stopy mają pokonać mniej więcej taką samą drogę do pozycji (zamiast jedną „wyrzucać” przed drugą); „crossing midair”; skok „instantly into the pose” — od razu do docelowej pozycji, nie najpierw wyprostowany. [U17]
- AMALL (back unity): w locie lekki obrót od przeszkody, stopy ustawione w docelowej pozycji **przed** kontaktem; „lock in both your feet at the same time”. [U22]
- Drummond: „cross your legs at your ankles … more than at your knees you'll be a lot more stable”. [U20]
- toxboe: „jump, and cross the legs on landing” (parafraza agenta) [U01].
- Acosta (back unity): wyskoczyć jak do acida/top stara i „switch on the way down” — zmienić stopę w trakcie opadania. [U19]
- **Wejście krokiem vs. skokiem — sprzeczność:**
  - Inline at the Border, krok 1: „step on with our dominant foot and our other foot will swing back around into the stall” (z miejsca, po kroku). [U15]
  - Back to Blading: „leading with my front foot and then sliding that back foot on is probably the safest bet” (relacja z własnej nauki, nie instruktaż). [U21]
  - JAD: „I don't think there's any way you can step onto this grind safely … definitely don't try stepping onto it” — przy wchodzeniu krokiem przednia stopa jest w backslide, „much harder than a unity”. [U16]
  - Baza: na forum wejście po kolei jedną, potem drugą stopą to zły nawyk. [S57] {OPINIA}

### 2.3 Lądowanie na przeszkodzie („lock”)

- Obie stopy zablokowane jednocześnie w rowkach. [U16][U22]
- „It is easier if you land in the groove.” [U02] (savannah, ta sama strona i autor co [U01])
- Kolana ugięte; prosto wyprostowane nogi = utrata równowagi w przód lub w tył i zaczepianie kółek (AMALL). [U22]
- Witzemann: ćwiczyć pozę na ziemi (na linii), potem „copy it onto the spot”. [U17]

### 2.4 Jazda w grindzie

- Stall przed slajdem: wszystkie tutoriale każą najpierw stallować (Inline at the Border ≥3 s; Drummond 3×; JAD „just keep stalling … over and over”; Acosta). [U15][U16][U18][U20]
- Rozkład ciężaru — **sprzeczność** (sekcja 4).
- Na końcu przeszkody: Drummond — wzrok na koniec rury („look towards the end of the rail”) — „biggest balance tip”. [U20]
- Wosk: brak wosku = brak ślizgu (Acosta, AMALL, Back to Blading, Drummond przy wheel bite). [U18][U21][U23][U20]

### 2.5 Wyjście / zeskok

- **Fakie (do tyłu)** dla front unity jako naturalne wyjście, wynikające z obrotu bioder: Witzemann [U17]; Drummond — „you'll naturally unwrap and come out fakie … don't fight it” [U20]; JAD — „my body wants to naturally 180 out” albo pochylenie w przód [U16]; Back to Blading — wyjście fakie pomogło mu ustawić barki równolegle do murka [U21].
- Acosta: wyjście w przód, 270 out albo fakie. [U18]
- AMALL (back unity): najpierw zdjąć stopę backside (na chwilę „back torque”), co rozplątuje nogi, potem obrót w tę samą stronę → fakie. [U22]
- Witzemann (back unity): lądowanie w przód lub z obrotem w drugą stronę sugeruje, że biodra „are not fully locked”; im bliżej i równolegle do przeszkody lądujesz, tym lepiej był zablokowany trik. [U17]
- Drummond: nie rozplątywać nóg w trakcie grindu na etapie nauki („more of an advanced step”). [U20]

### 2.6 Typowe błędy (zebrane)

| Błąd | Skutek wg źródła | Źródło |
|---|---|---|
| obracanie bioder przodem do kierunku jazdy | wykręca stopy z pozycji, zwykle tylna stopa spada górą | [U17]; podobnie [U16] |
| za nisko | rolki wysuwają się z rowka [U01]; „spłaszczenie” na bucie → „unity cess slide” [U16] | [U01][U16] |
| za wysoko / wyprostowane nogi | utrata równowagi, zaczepianie kółek | [U22][U16] |
| odchylanie się do tyłu | „leaning back slipped out and fell” | [U18][U20] |
| przednia stopa ześlizguje się (wychodzi pornstar) | — poprawka: ustawić barki równolegle do murka | [U21] |
| za głęboko „na” murku | przednie kółka szorują o górę | [U16]; Acosta: zostać na wewnętrznej krawędzi, inaczej wheel bite [U19] |
| stopy za blisko | wheel bite, „won't look great”, upadek „hurt a lot” | [U16] |
| stopy za daleko | „you're just gonna flop off” | [U16] |
| wjazd zbyt równoległy (back unity) | biodra nie wchodzą nad przeszkodę | [U17] (sprzeczne z [U22]) |
| wejście krokiem | przednia stopa w backslide, trudniej | [U16] (sprzeczne z [U15]) |
| płaski setup na murku | trudniej, wheel bite; uczyć się na anti-rockerze lub na rurze/copingu | [U16][U18] |

---

## 3. Postawa (segment po segmencie)

> {OPINIA} instruktorów, chyba że zaznaczono inaczej.

- **Stopy:** w rowkach, „boot down” [U16][U17][U20]; odstęp — JAD: „about a foot in between your feet” (~30 cm) [U16]; Drummond: „keep your knees further apart … cross at the ankles” [U20].
- **Kostka:** BRAK ŹRÓDŁA z opisem kostki w unity. Pośrednio: royale (baza unity) — „push your ankle over, so that you ride on the outside frame” [U03] — czyli przechylenie rolki na zewnętrzną krawędź. Co to znaczy dla stawu w sztywnym bucie — {WNIOSKOWANIE} w sekcji 6.
- **Kolana:** ugięte (wszystkie źródła). Witzemann: „bend your knees forward as if you were not crossing your legs at all”. [U17] Drummond: na murku niżej niż na rurze. [U20] Głębokość — sprzeczność (sekcja 9).
- **Biodra:** Witzemann — biodra „95% fully towards the spot”, nie obracać ich aktywnie w przód. [U17] Acosta (back unity) — „nice turn in your hips”, w odróżnieniu od acid soul, gdzie się patrzy w przód. [U19] AMALL (alley-oop unity) — „your hips are going to be parallel with the rail or ledge” [U23] (bez obrazu nie wiem, czy to ta sama pozycja co u Witzemanna).
- **Tułów / barki:** Drummond — „shoulders above your feet … facing into the rail” [U20]; Back to Blading — „square my shoulders more with the ledge” [U21]; JAD — ciało „turned a little bit”, nie na wprost [U16].
- **Ręce:** Acosta — ręce jako punkt balansu, „keeping your hands up so … you stay centered”; w back unity „hands to be out” [U18][U19]. Drummond — przy upadku złapać rurę [U20].
- **Wzrok:** Drummond — na koniec przeszkody [U20]; Witzemann — w kierunku jazdy, „only looking over your shoulder” przy biodrach skierowanych do przeszkody [U17]; AMALL (alley-oop unity) — w dół albo trochę za pierwszy bark [U23]; toxboe (royale) — tylna stopa „a little behind the spot you're looking at” [U03].

---

## 4. Balans / środek ciężkości / korekty

- **Rozkład ciężaru — różnice między instruktorami:**
  - Acosta (front unity): 60% na przedniej stopie (backslide), 40% na tylnej; „50/50 is even better”; zależy od długości i rodzaju przeszkody. [U18]
  - Acosta (back unity): „try to distribute your weight evenly; I kind of sit around like 60/40”. [U19]
  - Drummond: ok. 55% na stopie dominującej (przedniej), 45% na drugiej. [U20]
  - Witzemann: równy ciężar na obu stopach przy najeździe i wejściu. [U17]
  - AMALL (back unity): „most of my weight directly in the middle”; ale masz wybór: lepiej czujesz backslide — więcej na przedniej, torque — na tylnej. [U22]
  - AMALL (alley-oop unity): „most your weight and balance is going to be on your torque foot”, druga stopa tylko do stabilizacji. [U23]
  - Back to Blading: „like a backslide but your back foot is bracing yourself”; z czasem ciężar po równo. [U21]
  - toxboe (royale): ciężar jak najbardziej z przodu, „otherwise your momentum will sweep you away”. [U03]
  - toxboe: w unity „you are perfectly balanced – even more than in a frontside”. [U01]
- **Pochylenie w przód / w tył:** Drummond — pochylać się na przednią stopę, „the bail for sticking forward is much safer than the bail for slipping back”; „don't lean back … you still got to stay on top of your feet”. [U20] Na quarterze/copingu — odwrotnie: „lean back into the quarter … think about landing back in the transition”. [U20]
- **Środek masy względem przeszkody:**
  - AMALL: „you're going to be on top of it … that's where … your center of gravity [has] to be”. [U22]
  - Drummond: barki nad stopami na rurze. [U20]
  - JAD: na murku „leaned over a little bit but not too much”; za bardzo nad murkiem → przednie kółka szorują. [U16]
  - Acosta (back unity): „get on that inside edge of your obstacle”. [U19]
  - **Jedyny pomiar** (frontside grind, nie unity): środek masy nigdy nie przechodził nad podstawą podparcia na rurze. [S02] {DOWÓD:obserwacyjne} ✔ 1/2. Rada „bądź nad przeszkodą” może więc opisywać **odczucie**, a nie faktyczne położenie środka masy — {WNIOSKOWANIE}, nie sprawdzone dla unity.
- **Strategie balansu:** w stallach (nie grindach) skaterzy używali strategii kostkowej, biodrowej lub wielostawowej. [S02] {DOWÓD:obserwacyjne} 1/2. Przy skrzyżowanych nogach i stopach zablokowanych w rowkach strategia kostkowa jest prawdopodobnie ograniczona, więc korekty idą z bioder i tułowia (ręce, pochylenie) — {WNIOSKOWANIE}, zgodne z radami o rękach [U18][U19].
- **Korekty z tutoriali:** problem z dojechaniem do końca → barki nad stopy + wzrok na koniec [U20]; zsuwa się przednia stopa → barki równolegle do murka, ćwiczyć wyjście fakie [U21]; wheel bite → niżej, kolana szerzej, wosk [U20].

---

## 5. Styl

> {OPINIA}; brak „oficjalnych” kryteriów. Nie znalazłem tekstu o tym, co sędziowie zawodów uważają za czyste unity — **BRAK ŹRÓDŁA**.

- Skrzyżowane stopy robią wrażenie także na osobach, które nie jeżdżą (Ricardo Lino: „watching someone grinding with their feet crossed is always impressing”). [U11]
- Obrót bioder „opens up that trick … makes it look better” (Acosta, back unity). [U19]
- Odstęp stóp: za blisko „it's not gonna look great” (JAD). [U16]
- „Boot down” na obu rolkach jako wzorzec poprawnego unity; lądowanie blisko i równolegle do przeszkody = trik dobrze zablokowany („if you're trying to be a perfectionist”, Witzemann). [U17]
- Wersja „z pornstara” wg Drummonda „looks the best”. [U20]
- AMALL: back unity „a lot more stylish to do”. [U22]
- Unity otwiera wiele switch-upów i wariantów (JAD, Witzemann). [U16][U17]
- Nazewnictwo samo w sobie jest elementem kultury: „It's True Front Sav, and it can only be called that” (komentarz) [U10]; ankieta One Blade (285 osób): >70% uważa, że savannah nie musi być backside (parafraza agenta) [U08]. Ten spór nie zmienia techniki — Neil Bates: „Just make sure you land it whatever you're calling it”. [U10]

---

## 6. Fizjo

> Nie znaleziono **żadnego** badania obciążeń, kinematyki ani urazów w unity lub innych grindach skrzyżowanych (stan 11.11.2026; wyszukiwanie PubMed: „aggressive inline skating” → 3 rekordy: S01, S02 i przegląd Tan 2001 o rolkach ogólnie). Poniżej: dowody z innych zadań i sportów + wnioskowanie. Nic tu nie jest 2/2 **dla unity**.

### 6.1 Obciążenia — co prawdopodobnie pracuje

- **Pozycja:** nogi skrzyżowane, kolana ugięte, biodra skręcone do przeszkody, rolki przechylone na bok buta („boot down”, „push your ankle over” [U03]). [U03][U16][U17][U20] {OPINIA} → stąd:
  - biodro: rotacja i przywiedzenie (noga skrzyżowana) pod obciążeniem — {WNIOSKOWANIE};
  - kolano: zgięcie + moment rotacyjny, gdy stopa jest zablokowana w rowku, a tułów się obraca — {WNIOSKOWANIE};
  - kostka: przechylenie rolki na bok przy zablokowanym frame'ie — w sztywnym bucie część ruchu przejmuje but, ale ile — **BRAK ŹRÓDŁA** (brak pomiarów kostki w płaszczyźnie czołowej w AGV, zob. [S02]) — {WNIOSKOWANIE}.
- **Mechanizm skręcenia kostki (inne sporty):**
  - Analiza wideo 5 skręceń w tenisie: nagła inwersja (szczyt 48°–126°) i rotacja wewnętrzna (35°–99°); autorzy: lekko odwrócona (inverted) kostka przy lądowaniu jako zdarzenie wyzwalające. [U30] {DOWÓD:obserwacyjne (seria przypadków)}{ANALOGIA:tenis} ✔ abstrakt
  - Analiza 445 nagrań skręceń bocznych w sportach halowych: główne ruchy inwersja (65%) i rotacja wewnętrzna (33%), punktem obrotu boczna część przodostopia (53%) lub śródstopia (40%). [U31] {DOWÓD:obserwacyjne}{ANALOGIA:sporty halowe} ✔ abstrakt — U30 i U31 mają wspólnego autora (D. Fong) → nie w pełni niezależne.
  - Dla unity: zsunięcie rolki z krawędzi przy przechylonej stopie może przypominać ten mechanizm — {WNIOSKOWANIE}{ANALOGIA}; czy sztywny but AGV go blokuje — **BRAK ŹRÓDŁA**.
- **Kolano — rotacja + koślawienie (inne sporty):**
  - 10 zerwań ACL (piłka ręczna, koszykówka, kobiety): w ciągu 40 ms po kontakcie koślawienie +12° i rotacja wewnętrzna piszczeli +8°; szczyt siły pionowej 3,2× masy ciała ok. 40 ms. [U32] {DOWÓD:obserwacyjne (seria przypadków)}{ANALOGIA:sporty drużynowe} ✔ abstrakt
  - Lądowanie na jednej nodze ze stopą skręconą na zewnątrz zwiększało moment koślawiący kolana (efekt mały). [S48] {DOWÓD:obserwacyjne}{ANALOGIA:zeskoki} (w bazie)
  - Narciarstwo alpejskie (20 zerwań ACL w Pucharze Świata, sztywny but): „slip-catch” — krawędź narty łapie nagle, wymuszając rotację wewnętrzną i koślawienie kolana; „landing back-weighted” — lądowanie z ciężarem do tyłu na prawie wyprostowanych kolanach (m.in. „boot-induced anterior drawer”). [U33] {DOWÓD:obserwacyjne (seria przypadków)}{ANALOGIA:narciarstwo} ✔ abstrakt
  - Dla unity: (a) nagłe zatrzymanie rolki (wheel bite, zaczepienie kółek [U16][U22]) przy skręconym tułowiu przypomina „slip-catch”; (b) rada „don't lean back” [U18][U20] pokrywa się z mechanizmem „back-weighted” — {WNIOSKOWANIE}{ANALOGIA:narciarstwo}. Nie badane w AGV.
- **Biodro — zakres rotacji:**
  - Badanie na kolanach ze zwłok (symulacja lądowania z obrotem, 20 preparatów): im mniejszy dostępny zakres rotacji wewnętrznej uda, tym większe odkształcenie pęczka przednio-przyśrodkowego ACL (+1,3% na każde 10° mniej). [U34] {DOWÓD:eksperyment laboratoryjny}{ANALOGIA:lądowanie z obrotem} ✔ abstrakt
  - Metaanaliza 23 badań: mniejszy bierny zakres rotacji wewnętrznej biodra wiązał się z historią zerwania ACL (MD −5,02°), ale duża heterogeniczność „precludes generalizability”; brak związku dla rotacji zewnętrznej. [U35] {DOWÓD:przegląd} ✔ abstrakt
  - Taniec — „compensated turnout” (rotacja zewnętrzna wymuszona poza biodrem, kosztem kolana/stopy): związek z liczbą urazów u 22 tancerzy (r = 0,45) [U36] i w kohorcie 47 studentek tańca (każdy 1% więcej kompensacji → +9% szans na ≥2 urazy) [U37]. {DOWÓD:obserwacyjne}{ANALOGIA:taniec} ✔ abstrakt — dwie różne uczelnie w Londynie (Trinity Laban, London Met) → **2/2 dla tancerzy**, małe próby, nie AGV.
  - Dla unity: jeśli biodro nie ma zakresu rotacji, by ustawić skrzyżowaną nogę, kompensacja może iść na kolano i stopę — {WNIOSKOWANIE}{ANALOGIA:taniec}. Rady „nie obracaj bioder w przód” [U17] i „krzyżuj w kostkach, nie w kolanach” [U20] mogą być — {SPEKULACJA} — praktycznym sposobem na zmniejszenie skrętu w kolanie; nikt tego nie mierzył.
- **Sztywny but jako „stabilizator” kostki — wyniki niejednoznaczne (analogia ze stabilizatorami):**
  - Stabilizator kostki przy lądowaniu na pochyłą powierzchnię (n=24): większy moment ewersji w kostce, **większy moment rotacji zewnętrznej w kolanie**; moment koślawiący mniejszy (nieistotnie). [U38] {DOWÓD:obserwacyjne}
  - Sznurowany stabilizator (n=37): mniejszy zakres zgięcia grzbietowego, ale więcej zgięcia kolana przy kontakcie i bez zmiany siły pionowej. [U39] {DOWÓD:obserwacyjne}
  - Stabilizator typu „boot” (n=11): mniej pracy kostki przy lądowaniu jednonóż, bez istotnej zmiany pracy kolana i biodra. [U40] {DOWÓD:obserwacyjne}
  - Dla AGV: sztywny but może przenosić część obciążenia rotacyjnego z kostki na kolano, ale dane ze stabilizatorów są sprzeczne i dotyczą zupełnie innego sprzętu — {SPEKULACJA}. Kandydat na pytanie do fizjoterapeuty / Argona.

### 6.2 Przygotowanie (mobilność, siła, stabilizacja)

> Brak programu „pod unity” w żadnym źródle — **BRAK ŹRÓDŁA**. Poniżej mapowanie istniejących treści bazy na wymagania pozycji; całość = {PROPOZYCJA} do recenzji fizjo.

- **Mobilność biodra (rotacja wewnętrzna i zewnętrzna, przywiedzenie):** uzasadnienie [U34][U35][U36][U37] (analogie). Test: bierna rotacja biodra w leżeniu, porównanie stron. {PROPOZYCJA}
- **Mobilność kostki (zgięcie grzbietowe):** potrzebna do głębokiego ugięcia kolan „boot down” [U17]; w bazie {SPEKULACJA} w `mobilnosc.md` ([S02] — ugięcie kolana zmniejsza siłę). Test WBLT (w bazie jako TODO).
- **Siła i kontrola kostki (ewertory/inwertory):** [S79] (deficyty w CAI), program w `wzmacnianie.md`. Uzasadnienie dla unity: przechylenie rolki na bok [U03] — {WNIOSKOWANIE}.
- **Biodro i tułów — kontrola koślawienia:** samo wzmacnianie biodra słabo zmienia koślawienie; programy łączone (technika lądowania + plyometria + core) poprawiają mechanikę [S113][S114][S115] {DOWÓD:przegląd} 2/2 (w bazie).
- **Równowaga na jednej nodze / wąskiej podstawie:** [S16][S18] (w bazie). Specyficznie: pozycja unity „na linii” na podłodze, bez rolek i w rolkach (Witzemann: „mimic this pose on the ground … find like a line”) [U17] {OPINIA} → ćwiczenie przygotowawcze {PROPOZYCJA}.
- **Ugięcie kolan i pochylenie tułowia przy zeskoku:** [S02][S44][S45][S124] (w bazie, 2/2 dla zeskoków).

### 6.3 Rozgrzewka pod unity

- Ogólne: rozgrzewka nerwowo-mięśniowa zmniejsza urazy kończyn dolnych o ok. 30–40% (inne sporty). [S62][S83][S87] {DOWÓD:przegląd}{ANALOGIA} 2/2 (w bazie).
- Specyficzne dla unity — **BRAK ŹRÓDŁA** z protokołem. Elementy z tutoriali (opinie): najpierw zwykłe grindy na rozgrzewkę [U21]; stall z miejsca, potem z wyskoku, potem z prędkością [U15]; triki „bazowe” jako wejście — front royale i pornstar dla front unity, acid i (niezrozumiałe w ASR „back FRV”) dla back unity [U17]; acid/top star z obrotem stopy [U19]. AMALL „Coping Grinds” (2011) w opisie wspomina „From stretching, stalling to falling” [U25] — napisów nie udało się pobrać (HTTP 429), treść nieznana.
- Propozycja kolejności ({PROPOZYCJA}): ogólna rozgrzewka z `rozgrzewka.md` → krążenia i rotacje bioder → poza unity na linii (obie strony) → frontside, royale/pornstar → stall unity → unity.

### 6.4 Przeciwwskazania

- **BRAK ŹRÓDŁA** z przeciwwskazaniami dla unity.
- W bazie (`powrot-do-grindow.md`) unity jest w etapie 5 (razem z topside, royale, zeskokami): testy skoków ≥90% zdrowej strony, gotowość psychiczna, zgoda lekarza — {PROPOZYCJA} oparta na protokołach [S22][S23], nie na badaniach grindów; po skręceniu kostki **brak zwalidowanych progów** [S149][S150] {DOWÓD:przegląd} 2/2.
- {WNIOSKOWANIE} do recenzji: ostrożność przy (a) świeżym skręceniu/niestabilności kostki (mechanizm inwersja + rotacja [U30][U31]), (b) po urazie/rekonstrukcji ACL (rotacja + koślawienie [U32][U33]), (c) ograniczonej rotacji biodra [U34][U35], (d) bólu przyśrodkowej części kolana przy skręcie — wszystko bez danych z AGV.

### 6.5 Powrót po urazie

- Brak źródeł specyficznych dla unity — **BRAK ŹRÓDŁA**. Kryteria ogólne — `powrot-do-grindow.md` [S19][S22][S23][S149][S150].
- Kolejność z tutoriali, którą można wykorzystać jako stopniowanie ({PROPOZYCJA}): poza na ziemi [U17] → stall z miejsca/kroku [U15] → stall z wyskoku [U15][U20] → „tap” na końcu rury [U20] → krótki grind → pełny grind, wyższa przeszkoda, backside, wyjścia z obrotem.
- Specyficzność ćwiczeń poprawia pewność przy powrocie (fizjo skaterów). [S29] {OPINIA}{ANALOGIA:skateboarding} (w bazie).

### 6.6 Wyjście przy zsunięciu (bail) i upadanie

- Tutoriale (opinie):
  - Drummond: pochylać się w przód, bo upadek w przód jest bezpieczniejszy niż ześlizg do tyłu; „if you have the chance grab the rail … you'll save yourself from any kind of whack slip out”. [U20]
  - Acosta (pokazując własny upadek po odchyleniu do tyłu): „kick your legs out put your hand down sit down”. [U18]
  - Back to Blading: na backside unity „if you miss you sit on your butt”. [U21]
  - JAD: przy stopach za blisko „when you fall it's gonna hurt a lot”. [U16]
  - Witzemann: lądowanie daleko od przeszkody = „sketchy”. [U17]
  - Acosta: „if you're just learning … throw pads on”. [U19]
- **Sprzeczność do zaznaczenia:** Acosta pokazuje upadek z podparciem ręką („put your hand down”) [U18], a baza ma dane, że „klepnięcie” dłonią (slapping) nie zmniejszało obciążenia przy upadku, a przewrót i przysiad przy upadku w tył — zmniejszały. [S70] {DOWÓD:przegląd}{ANALOGIA:upadki zamierzone}. Ochraniacze nadgarstków: OR 10,4 dla urazu nadgarstka bez ochraniaczy (rolki rekreacyjne). [S04] {DOWÓD:obserwacyjne}.
- {WNIOSKOWANIE}: przy skrzyżowanych nogach rozplątanie przed lądowaniem jest trudniejsze (Drummond: nie rozplątywać nóg w trakcie, to „advanced” [U20]) → ćwiczyć „wyjście na siad” i chwytanie rury na niskiej przeszkodzie; brak danych.
- Ryzyko a wysokość: w parku snowboardowym urazy rzadsze na railach niż na skoczniach [S145] {ANALOGIA:snowboard} — unity na niskiej przeszkodzie przy nauce jest zgodne z tą obserwacją, {WNIOSKOWANIE}.

---

## 7. Progresja nauki

> {OPINIA}; zestawienie z tutoriali, z zaznaczeniem rozbieżności.

**Warunki wstępne (różne u różnych autorów):**
- frontside + royale — toxboe [U01], Acosta [U18];
- front royale + pornstar (front unity); acid + „back FRV”? (back unity) — Witzemann [U17];
- pornstar — Drummond [U20];
- front unity, acid soul, top star (back unity) — Acosta [U19];
- „couple of basic tricks”, nie jako pierwszy grind — Witzemann [U17]; SkaMiDan: poziom średni [U05].

**Przeszkoda i sprzęt:**
- niska rura / coping, jeśli jeździsz na płaskim setupie; murek łatwiejszy na anti-rockerze — Acosta [U18], JAD [U16];
- Drummond: polecam rurę, ale „the obstacle you feel more comfortable with” [U20];
- Rollerblade (ogólny poradnik grindów): przeszkoda „approximately shin height” [U26 — strona Rollerblade, dotyczy frontside/soul] {OPINIA};
- wosk na przeszkodzie [U18][U21][U23].

**Kroki (synteza):**
1. Poza unity na ziemi, na linii, ugięcie kolan „boot down” [U17].
2. Grind bazowy (royale / pornstar / acid) z dociążaniem stopy, która w unity zostaje w H-blocku [U20][U19].
3. Stall z miejsca: krokiem [U15] **albo** — wg JAD — nigdy krokiem, tylko z wyskoku [U16] (sprzeczność).
4. Stall z wyskoku, trzymanie ≥3 s [U15], 3 udane [U20].
5. „Unity tap” na końcu rury — poczuć ślizg bez ryzyka długiego grindu [U20].
6. Pełny grind z rosnącą prędkością („add a little bit of speed … little by little”) [U16][U15].
7. Kryterium Drummonda: „land it three times … you've officially learned” [U20].
8. Dalej: back unity (Back to Blading: nauka od frontside „was smart” [U21]; Witzemann: wiele osób zaczyna od back unity i robi ją „incorrectly” [U17]), wyjścia 180/270, switch-upy, savannah/alley-oop unity (poziom zaawansowany [U05]).

---

## 8. Tabela źródeł

Weryfikacja: „✔ 200” = otwarte WebFetch, HTTP 200; „✔ yt-dlp” = metadane wideo pobrane (wideo istnieje), treść z auto-napisów; „✔ E-utils” = rekord i abstrakt pobrane z NCBI; „✘” = nie udało się.

| ID | Źródło | Typ | URL | PMID / DOI | Zweryfikowane |
|---|---|---|---|---|---|
| U01 | toxboe.net — Trickguide: *Unity* (bez autora i daty) | glosariusz/poradnik | https://toxboe.net/tricks/grind/unity | — | ✔ 200 |
| U02 | toxboe.net — *Savannah* | glosariusz/poradnik | https://toxboe.net/tricks/grind/savannah | — | ✔ 200 |
| U03 | toxboe.net — *Royale* | glosariusz/poradnik | https://toxboe.net/tricks/grind/royale | — | ✔ 200 |
| U04 | toxboe.net — *Variations* | glosariusz | https://toxboe.net/tricks/grind/variations | — | ✔ 200 |
| U05 | SkaMiDan — *Grinds trick list … difficulty levels* | lista trików (sklep/szkoła) | https://www.skamidan.com/en/blogs/aggressive-inline-skating-tutorials-and-learning/grinds-trick-list-of-aggressive-inline-skating-tricks-and-difficulty-levels-stunt-skating-rollerblading-rollerblades-slides-grind-how-to | — | ✔ 200 (wpisy jednozdaniowe, bez tutoriali) |
| U06 | SkaMiDan — *Technical terms and vocabulary* | glosariusz | https://www.skamidan.com/en/blogs/aggressive-inline-skating-tutorials-and-learning/technical-terms-and-vocabulary-aggressive-inline-skating-slang-expressions-rollerblading-stunt-skating | — | ✔ 200 |
| U07 | Wikipedia — *Aggressive inline skating* (sekcja Hardware) | encyklopedia | https://en.wikipedia.org/wiki/Aggressive_inline_skating | — | ✔ 200 (brak hasła „unity”) |
| U08 | Alan Hughes, ONE blademag, 12.11.2018 — *Let's Argue About Trick Terminology!* | blog/magazyn + komentarze | https://www.oneblademag.com/?p=19587 | — | ✔ 200 |
| U09 | Alan Hughes, ONE blademag, 18.09.2019 — *The Truespin On "Alley-Oop" History* | blog/magazyn | https://www.oneblademag.com/?p=20559 | — | ✔ 200 |
| U10 | Alan Hughes, ONE blademag, 18.10.2025 — *The Savannah Compromise of 2025* (+ komentarze: S. Michaelson, A. Cherry-Garrard, N. Bates) | blog/magazyn + komentarze | https://www.oneblademag.com/blogs/the-savannah-compromise-of-2025 | — | ✔ 200 |
| U11 | Ricardo Lino, Rollernews 12.08.2017 — *Trick Tips with Ricardo Lino: How to Unity Grind* + wideo „AGGRESSIVE INLINE SKATING TUTORIAL - HOW TO UNITY GRIND // VLOG 139” | tutorial wideo (opis) | https://rollernews.com/2017/08/12/aggressive-inline-skating-tutorial-how-to-unity-grind · https://www.youtube.com/watch?v=5VHFkOCtVcE | — | ✔ 200; ✔ yt-dlp; **✘ napisy (HTTP 429)** — treść wideo nieznana |
| U12 | Becci Sotelo, Rollernews 20.09.2021 — *How to Grind a Ramp on Rollerblades* (backside, 270 backside, back unity na rampie) | tutorial wideo (opis) | https://www.rollernews.com/2021/09/20/how-to-grind-a-ramp-on-rollerblades | — | ✔ 200; wideo nieobejrzane |
| U13 | *Basic Blading Tricks* (dghent.github.io) | lista trików | https://dghent.github.io/blading-tricks | — | ✔ 200 — wpisy unity to tylko GIF + „coming soon”; **nie używane** |
| U14 | ONE blademag 6.11.2012 — *The Science of Swag* (omówienie Major 2007 = [S02]) | blog | https://www.oneblademag.com/blogs/the-science-of-swag/ | — | ✔ 200 (źródło wtórne wobec S02) |
| U15 | In-line at the Border (Jacob), 17.02.2022 — *HOW TO GRIND // 3 EASY STEPS // UNITY GRIND* | tutorial wideo | https://www.youtube.com/watch?v=pZKUjRK_2B8 | — | ✔ yt-dlp + auto-napisy |
| U16 | JADRollerVlog, 12.02.2022 — *HOW TO UNITY JAD Rollerblading* | tutorial wideo | https://www.youtube.com/watch?v=4w_qjj8oN-s | — | ✔ yt-dlp + auto-napisy |
| U17 | Michael Witzemann, 4.06.2025 — *Learn to Grind on Inline Skates - Unity* (front i back unity) | tutorial wideo | https://www.youtube.com/watch?v=ARn-gkWejBo | — | ✔ yt-dlp + auto-napisy |
| U18 | Acosta Blades, 3.01.2020 — *Aggressive Inline: How to Unity Grind* | tutorial wideo | https://www.youtube.com/watch?v=l0VWrEX4E-Q | — | ✔ yt-dlp + auto-napisy |
| U19 | Acosta Blades, 13.05.2021 — *Aggressive Inline Quick Tips On Back Unity* | tutorial wideo | https://www.youtube.com/watch?v=Gy9TYEdzlBQ | — | ✔ yt-dlp + auto-napisy |
| U20 | Brandon Drummond, 8.03.2019 — *How to Unity Grind on Rollerblades - Tip Trick* | tutorial wideo | https://www.youtube.com/watch?v=WR3YDmzrXsY | — | ✔ yt-dlp + auto-napisy |
| U21 | Back to Blading, 20.07.2018 — *Learning Unities - Aggressive Inline Skating How To* (vlog z nauki, nie instruktaż) | vlog | https://www.youtube.com/watch?v=ADNrf6N5y2Y | — | ✔ yt-dlp + auto-napisy |
| U22 | aggressivemall, 4.09.2009 — *Amall Trick Tips: Back Unity* | tutorial wideo (sklep) | https://www.youtube.com/watch?v=vAmIIEaDVHM | — | ✔ yt-dlp + auto-napisy |
| U23 | aggressivemall, 5.06.2009 — *Amall Trick Tips: Ally Oop Unity* | tutorial wideo (sklep) | https://www.youtube.com/watch?v=Ly4YNAiBQDY | — | ✔ yt-dlp + auto-napisy |
| U24 | Roll Minnesota, 9.07.2024 — *How One Trick BROKE Rollerblading… Unity vs. Savannah Explained!* | wideo-esej (terminologia) | https://www.youtube.com/watch?v=UosCCqHaYp8 | — | ✔ yt-dlp + auto-napisy |
| U25 | aggressivemall (Kyle Nolte), 3.06.2011 — *AMALL Trick Tips: Coping Grinds* | tutorial wideo | https://www.youtube.com/watch?v=PaCWWYGKOhY | — | ✔ yt-dlp (tylko opis); **✘ napisy (429)** |
| U26 | Rollerblade — *Danny's Point: How to Grind* (20.04.2022; frontside/soul, nie unity) | poradnik marki | https://www.rollerblade.com/uk/en/the-rollerblade-experience/street/danny-s-point-how-to-grind | — | ✔ 200 (tekst szczątkowy, wideo nieobejrzane) |
| U30 | Fong DT i wsp. 2012. *Kinematics analysis of ankle inversion ligamentous sprain injuries in sports: five cases from televised tennis competitions*. Am J Sports Med 40(11):2627–32 | seria przypadków (wideo), n=5 | https://pubmed.ncbi.nlm.nih.gov/22967824/ | PMID 22967824 · doi 10.1177/0363546512458259 | ✔ E-utils (abstrakt) |
| U31 | Bagehorn T i wsp. 2024. *Lateral Ankle Joint Injuries in Indoor and Court Sports: A Systematic Video Analysis of 445 Nonconsecutive Case Series*. Am J Sports Med 52(6):1572–1584 (współautor Fong — jak U30) | przekrojowe (wideo), n=445 | https://pubmed.ncbi.nlm.nih.gov/38634630/ | PMID 38634630 · doi 10.1177/03635465241241760 | ✔ E-utils (abstrakt) |
| U32 | Koga H i wsp. 2010. *Mechanisms for noncontact ACL injuries: knee joint kinematics in 10 injury situations from female team handball and basketball*. Am J Sports Med 38(11):2218–25 | seria przypadków (wideo), n=10 | https://pubmed.ncbi.nlm.nih.gov/20595545/ | PMID 20595545 · doi 10.1177/0363546510373570 | ✔ E-utils (abstrakt) |
| U33 | Bere T i wsp. 2011. *Mechanisms of ACL injury in World Cup alpine skiing: a systematic video analysis of 20 cases*. Am J Sports Med 39(7):1421–9 (ta sama grupa OSTRC co U32) | seria przypadków (wideo), n=20 | https://pubmed.ncbi.nlm.nih.gov/21515807/ | PMID 21515807 · doi 10.1177/0363546511405147 | ✔ E-utils (abstrakt) |
| U34 | Beaulieu ML i wsp. 2014. *Does limited internal femoral rotation increase peak ACL strain during a simulated pivot landing?* Am J Sports Med 42(12):2955–63 | eksperyment na preparatach, n=20 | https://pubmed.ncbi.nlm.nih.gov/25245132/ | PMID 25245132 · doi 10.1177/0363546514549446 · PMC6380493 | ✔ E-utils (abstrakt) |
| U35 | Hogg JA, Waxman JP, Shultz SJ 2022. *Examining the effects of femoral anteversion and passive hip rotation on ACL injury and knee biomechanics: a systematic review and meta-analysis*. J Exp Orthop 9(1):40 | przegląd + metaanaliza, 23 badania | https://pubmed.ncbi.nlm.nih.gov/35513749/ | PMID 35513749 · doi 10.1186/s40634-022-00479-7 | ✔ E-utils (abstrakt) |
| U36 | van Merkensteijn GG, Quin E 2015. *Assessment of Compensated Turnout Characteristics and their Relationship to Injuries in University Level Modern Dancers*. J Dance Med Sci 19(2):57–62 | obserwacyjne, n=22 | https://pubmed.ncbi.nlm.nih.gov/26045396/ | PMID 26045396 · doi 10.12678/1089-313X.19.2.57 | ✔ E-utils (abstrakt) |
| U37 | Jenkins JB, Wyon M, Nevill A 2013. *Can turnout measurements be used to predict physiotherapist-reported injury rates in dancers?* Med Probl Perform Art 28(4):230–5 | kohorta prospektywna, n=47 | https://pubmed.ncbi.nlm.nih.gov/24337035/ | PMID 24337035 (DOI brak w rekordzie) | ✔ E-utils (abstrakt) |
| U38 | Venesky K i wsp. 2006. *Prophylactic ankle braces and knee varus-valgus and internal-external rotation torque*. J Athl Train 41(3):239–44 | eksperyment, n=24 | https://pubmed.ncbi.nlm.nih.gov/17043690/ | PMID 17043690 · PMC1569548 | ✔ E-utils (abstrakt) |
| U39 | DiStefano LJ i wsp. 2008. *Lower extremity kinematics and ground reaction forces after prophylactic lace-up ankle bracing*. J Athl Train 43(3):234–41 | eksperyment z randomizacją grup, n=37 | https://pubmed.ncbi.nlm.nih.gov/18523572/ | PMID 18523572 · doi 10.4085/1062-6050-43.3.234 | ✔ E-utils (abstrakt) |
| U40 | Gardner JK i wsp. 2012. *Effect of ankle braces on lower extremity joint energetics in single-leg landings*. Med Sci Sports Exerc 44(6):1116–22 | eksperyment, n=11 | https://pubmed.ncbi.nlm.nih.gov/22157878/ | PMID 22157878 · doi 10.1249/MSS.0b013e318240d564 | ✔ E-utils (abstrakt) |

Źródła już w bazie, użyte w tym pliku (nie otwierane ponownie): [S02] [S04] [S16] [S18] [S19] [S22] [S23] [S29] [S44] [S45] [S48] [S57] [S62] [S70] [S79] [S83] [S87] [S113] [S114] [S115] [S124] [S145] [S149] [S150] — opisy i linki w `sources.md`.

Sprawdzone i odrzucone / bez treści: Wikipedia *Grind (sport)* (brak unity; ✔ 200); Skate Fantom *WHATCHAMACALLIT?* (brak unity; ✔ 200); Tan V 2001, *In-line skating injuries*, Sports Med, PMID 11508524 (rolki ogólnie, nieużyty); Dickson 2021, PMID 33384220 (trendy urazów w narciarstwie — nie wnosi nic o butach, nieużyty).

---

## 9. Luki i sprzeczności

### Sprzeczności (opisane, bez rozstrzygania)

1. **Co to jest unity, a co savannah.** Pozycyjnie (która noga się krzyżuje: toxboe [U01][U02], propozycja Roll Minnesota [U24], komentarz Cherry-Garrarda [U10]) vs. kierunkowo (te same stopy, inny kierunek: Acosta [U18]; „alley-oop unity = savannah”: SkaMiDan [U05], część czytelników One Blade [U08][U10]). Michaelson: unity nigdy nie jest „do tyłu” [U10]. W poradniku trzeba wybrać jedną konwencję i jawnie zaznaczyć drugą.
2. **Rozkład ciężaru:** 60/40 na przednią (Acosta [U18]), 55/45 (Drummond [U20]), 50/50 (Witzemann [U17], AMALL [U22], Acosta „even better” [U18]), przewaga na stopie torque (AMALL, alley-oop unity [U23]), przednia + tylna jako „podpórka” (Back to Blading [U21]).
3. **Kąt najazdu:** lekki kąt, nie równolegle (Witzemann [U17], Acosta [U18]) vs. bardziej równolegle na długim murku (AMALL back unity [U22]) vs. większy kąt (AMALL alley-oop unity [U23]) vs. prawie na wprost (JAD [U16]).
4. **Wejście krokiem czy skokiem:** krok jako etap nauki (Inline at the Border [U15], Back to Blading [U21]) vs. „definitely don't try stepping onto it” (JAD [U16]) i „obie stopy naraz” (Witzemann [U17], AMALL [U22], [S57]).
5. **Głębokość przysiadu:** „bend down” gdy rolki nie wchodzą w rowek [U01][U02], niżej na murku [U20] vs. za nisko = wysuwanie z rowka [U01] / „spłaszczenie” na bucie [U16]. To nie musi być sprzeczność (istnieje zakres optymalny), ale nikt go nie opisuje liczbowo.
6. **Gdzie krzyżować:** „at your ankles … more than at your knees” (Drummond [U20]) — inni nie mówią; Witzemann: kolana „forward as if you were not crossing” [U17].
7. **Środek ciężkości:** „na przeszkodzie” (AMALL [U22], Drummond [U20]) vs. nie za bardzo nad murkiem (JAD [U16]) / wewnętrzna krawędź (Acosta [U19]) vs. pomiar we frontside: środek masy nigdy nad rurą [S02].
8. **Kontakt buta:** rowek + bok buta („boot down”, [U16][U17][U20]) vs. „a bit of your soul grooves” (Inline at the Border [U15], być może błąd ASR).
9. **Kolejność front/back:** od front unity (Back to Blading [U21], Witzemann [U17]) vs. wiele osób zaczyna od back (Witzemann, jako obserwacja [U17]); co jest „łatwiejsze” — różne opinie [U21].
10. **Upadek z podparciem ręką** (Acosta [U18]) vs. dane, że „klepnięcie” nie zmniejsza obciążenia, a przewrót/przysiad tak [S70].
11. **Sztywny but / stabilizator a kolano:** stabilizator zwiększał moment rotacji zewnętrznej kolana [U38] vs. brak zmian w kolanie i sile [U39][U40]. Różne zadania i sprzęt; przeniesienie na but AGV niepewne.

### Luki (BRAK ŹRÓDŁA)

- Brak **jakiegokolwiek** pomiaru biomechaniki unity / grindów skrzyżowanych (siły, kąty kolana i biodra, kostka w płaszczyźnie czołowej, EMG).
- Brak danych o urazach w unity (żadne badanie nie rozbija urazów AGV na grindy — zob. `wzorce-urazow-wg-grindow.md`).
- Brak definicji „true unity” w źródle o sensownej randze.
- Brak opisu ruchu kostki w sztywnym bucie przy „boot down”.
- Brak programu przygotowania, rozgrzewki i przeciwwskazań „pod unity” od fizjoterapeuty AGV (The Blading Physio — nie znaleziono materiału o unity/royale).
- Brak źródła o technice „bezpiecznego wyjścia” ze skrzyżowanych nóg poza pojedynczymi wskazówkami z wideo.
- Brak kryteriów stylu z zawodów/sędziowania.
- Nie pobrano treści: wideo Ricardo Lino [U11] i AMALL Coping Grinds [U25] (HTTP 429 przy napisach) oraz Becci Sotelo [U12] (nie próbowano). **Do zrobienia w rundzie 2.**
- Fora (r/AggressiveInline) — wyszukiwarka nie ma dostępu do reddit.com; **nie przeszukane** w tej rundzie.
- Historia: kto wymyślił unity (Jon Julio wg [U20]) — 1 źródło.

### Uwagi o jakości

- Wszystkie cytaty z wideo pochodzą z automatycznych napisów i z jednej odsłony. Przed wpisaniem do bazy warto obejrzeć fragmenty (szczególnie [U15] „soul grooves”, [U17] „back FRV”, [U23] „hips parallel”).
- U30/U31 (wspólny autor Fong) i U32/U33 (grupa OSTRC Oslo) nie są w pełni niezależne.
- U36/U37 to małe próby tancerek i tancerzy; przeniesienie na AGV = {ANALOGIA}.
- Nic z tego pliku nie spełnia zasady 2/2 **dla unity**; najlepiej udokumentowane są opinie zgodne u wielu instruktorów: kolana ugięte, oba rowki + bok buta, najpierw stall, wosk, wyjście fakie z front unity jako naturalne, nie odchylać się do tyłu.
