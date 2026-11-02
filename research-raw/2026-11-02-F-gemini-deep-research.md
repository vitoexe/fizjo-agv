# Surowy wynik: F (wzmacnianie i stabilizacja), Gemini Deep Research (max) w AI Studio, 2.11.2026 ~14:59

Wklejone przez Tomasza. **NIEZWERYFIKOWANE** w części „surowy zapis”. Prawdopodobnie tylko **druga część** raportu (zaczyna się od sekcji o nadgarstkach i upadkach). Etykiety i statusy („CONFIRMED”, „2/2”) nadał model — traktujemy je jako niesprawdzone.

Infografika (materiał poglądowy, `{OPINIA}`): `2026-11-02-F-plyometria-5-etapow.png` — 5 etapów plyometrii: snap downs / drop freezes → box jumps → vertical jump → depth jump od 12 do 24+ cali → warianty depth jump. Źródła na grafice: The Movement System, Thirst Gym, Hospital for Special Surgery.

> Linki w odpowiedzi modelu to przekierowania `vertexaisearch.cloud.google.com` — **nie używamy ich**. Źródła odszukane po autorze, roku, tytule i DOI (PubMed, PMC, Crossref, strony wydawców).

## Streszczenie twierdzeń modelu (surowy zapis)

1. Steib 2017, Front Physiol, doi 10.3389/fphys.2017.00920, meta-analiza 16 badań: trening nerwowo-mięśniowy 10–15 min, 2–3×/tydz. (30–60 min/tydz.) zmniejsza urazy kończyn dolnych u młodzieży o ~42%. Model: 2/2.
2. „Uddin 2026”, ijoro.org (tytuł podany przez model: *Stiff Landings, Core Stability, and Dynamic Knee Valgus: A Systematic Review…*): słaba stabilizacja tułowia i boczne pochylenie zwiększają ramię dźwigni i koślawienie kolana / ryzyko ACL. Model: 2/2.
3. MDPI 2411-5142/11/1/69 (JFMK 2026): wytrzymałość odwodzicieli biodra ważniejsza niż siła maksymalna dla dynamicznego koślawienia kolana (DKV).
4. PLoS One 10.1371/journal.pone.0330140 (2026), n=20 studentek: ekscentryczny trening odwodzicieli lepszy niż koncentryczny dla DKV w jednonóżnym CMJ. „EVIDENCE:RCT”.
5. PMC10692103 (2023), meta-analiza, młodzież, n=3347: < 900 kontaktów z podłożem optymalne dla CMJ, > 1400 dla SJ. W praktyce modelu: „limituj CMJ do < 900 kontaktów w 8–10 tyg., żeby kontrolować obciążenie ścięgien”.
6. Moon 2017, Arch Phys Med Rehabil, doi 10.1016/j.apmr.2016.08.460, n=217: przewrót (martial arts rolling) przy upadku w bok g=2,70, przysiad przy upadku w tył g=1,77. Model: 2/2.
7. Moon 2017: technika „klepnięcia” (slapping) nie daje korzyści i może uszkodzić rękę/nadgarstek/łokieć na twardym podłożu. Model: 2/2.
8. ResearchGate 404263665 (2026): trening mięśni strzałkowych u tenisistów i koszykarzy zapobiega skręceniom. `ANALOGY:tennis, basketball`, model: 2/2.
9. PMC12220483 (2025), meta-analiza: zmęczenie zwiększa szczytowe koślawienie kolana głównie przy obunóżnym lądowaniu po skoku pionowym („280 studies”).
10. „Impact Forces During Skateboarding Landings” 2014, ResearchGate, n=7: średnio 4,74× masy ciała przy zeskoku.
11. NO DATA wg modelu: brak dawkowania prewencyjnego wzmacniania strzałkowych / piszczelowego tylnego u zdrowych; brak dowodów, że siła przedramienia chroni nadgarstek przy upadku.
12. Sprzeczność wg modelu: słabość odwodzicieli/rotatorów zewn. a DKV — jedne prace tak, przegląd 2026 nie; ekscentryka vs koncentryka; wytrzymałość vs 1RM.
13. Praktyka modelu: progresja plyometrii od absorpcji (snap downs) do depth jumpów = „CONSENSUS” (HSS, The Movement System, Thirst Gym, brandonsmitley.com). „Grind posture specificity” (rotatory zewn. i odwodziciele w pozycjach royale/soul) = SPECULATION. Wnioskowania: makio/sweatstance obciąża ekscentrycznie strzałkowe; core zapobiega koślawieniu przy lądowaniu ze schodów (~4,74× BW); pośladkowy wielki ekscentrycznie przy lądowaniu 360/540.

Fragment praktyczny modelu (skrót): rozgrzewka nerwowo-mięśniowa 10–15 min 2–3×/tydz. „EVIDENCE:review”; „Plyometric Dosing (EVIDENCE:review): <900 kontaktów… to manage tendon load”; progresja plyometrii „CONSENSUS”; technika upadania (przewrót, przysiad) „EVIDENCE:review”; „Avoid Ground Slapping (EVIDENCE:review)… endangers the wrist and elbow”; gumy na ewersję/inwersję „ANALOGY | CONSENSUS”; core przeciw bocznemu pochyleniu „EVIDENCE:observational | BIOMECH-INFERENCE”; ekscentryka odwodzicieli „EVIDENCE:RCT”; zmęczenie a koślawienie „EVIDENCE:review”.

## Weryfikacja (Grok Bot, 2.11.2026)

Legenda: ✔ zgodne · PARTIAL częściowo (różnica opisana) · ✘ niezgodne / źródło nie nadaje się · NOT FOUND.

| # | Twierdzenie modelu | Wynik | Co faktycznie mówi źródło / różnica | Identyfikator | Tekst | ID w bazie |
|---|---|---|---|---|---|---|
| 1 | Steib 2017: NMT 10–15 min, 2–3×/tydz., 30–60 min/tydz., −42% urazów KD u młodzieży | ✔ (status ✘) | liczby zgodne: 16 badań, IRR 0,58 (95% CI 0,47–0,72); 2× IRR 0,50, 3× IRR 0,40; > 30 min/tydz. „tended to be more effective”; młodzież ≤ 21 lat; > 6 mies. nie lepsze. Autorzy: mała liczba badań, heterogeniczna jakość. **„2/2” modelu bezpodstawne** — to jedna meta-analiza. Niezależne wsparcie w bazie: [S16] (Vriend, skręcenia kostki) | PMID 29184511, PMC5694483 | abstrakt | S62 |
| 2a | „Uddin 2026” — tytuł *Stiff Landings, Core Stability…* | ✘ (pomylone prace) | Uddin SM, Murphy A 2026 (IJORO, 25.08.2026) ma tytuł *The role of jumping and landing patterns in ACL injury risk: a systematic review of assessment methods* (15 badań, dorośli). Tytuł *Stiff Landings, Core Stability, and DKV…* to **Larwa i wsp. 2021, IJERPH** (MEDLINE). IJORO (Medip Academy) deklaruje recenzję, ale **nie jest indeksowane w MEDLINE** (NLM: status „N”) → niska waga | doi 10.18203/issn.2455-4510.IntJResOrthop20262922; Larwa: PMID 33917488 | abstrakty | S66, S63 |
| 2b | Boczne pochylenie tułowia / słaba kontrola tułowia ↔ koślawienie kolana i ACL | PARTIAL, 1/2 | źródła pierwotne istnieją: **Hewett, Torg, Boden 2009** (analiza wideo urazów ACL: u kobiet większe boczne pochylenie tułowia i odwiedzenie kolana) i **Zazulak i wsp. 2007** (277 sportowców, prospektywnie: przemieszczenie tułowia, zwł. boczne, przewidywało urazy więzadeł kolana u kobiet). **Hewett jest współautorem obu → jedna grupa**. „Ramię dźwigni” — wnioskowanie biomechaniczne, nie wynik. Dingenen — nie sprawdzano (nie potrzebne) | PMID 19372088, 17468378 | abstrakty | S64, S65 |
| 3 | JFMK 2026: wytrzymałość odwodzicieli > siła maks. dla DKV | PARTIAL | Granger i wsp. 2026, **przegląd narracyjny** (metoda „snowballing”, autorzy: „cannot make causal claims”). Twierdzenie pochodzi z cytowanego **abstraktu konferencyjnego** Lagouvardou i wsp. 2023 (Gait Posture 106:S109) — nieodczytany. Ten sam przegląd przyznaje niespójność danych o sile biodra (Alzahrani 2021, Dix 2019) | doi 10.3390/jfmk11010069 | pełny tekst | S67 |
| 4 | Fésüs 2026: ekscentryka > koncentryka dla DKV w jednonóżnym CMJ | ✔ z uwagami | **badanie pilotażowe**, randomizacja, n=20 kobiet z DKV, 4 tyg., 3×/tydz., 4×10. Przewaga ekscentryki **tylko w CMJ, nie w lądowaniu z wysokości**; zmiany DKV **nie korelowały** ze wzrostem siły odwodzicieli | PMID 42085418, PMC13143104 | abstrakt | S68 |
| 5 | Chen 2023: < 900 kontaktów dla CMJ, > 1400 dla SJ; „chroni ścięgna” | PARTIAL / nadinterpretacja | liczby zgodne (38 badań, 50 RCT, 3347 uczestników; optymalny czas 400–600 min). Badanie dotyczy **wysokości skoku**, **nie urazów ani ścięgien** — „limituj do < 900, żeby chronić ścięgna” to dopisek modelu ✘. Też: < 900 to nie limit, tylko zakres z największym efektem dla CMJ | PMID 38040837, PMC10692103, doi 10.1038/s41598-023-48274-3 | abstrakt | S69 |
| 6 | Moon 2017: przewrót g=2,70 (w bok), przysiad g=1,77 (w tył); n=217 | ✔ liczby / ✘ n i 2/2 | g zgodne; też zgięcie łokci przy upadku w przód g=0,82, rotacja w przód g=0,82. **13 badań, 7 strategii**; „n=217” brak w abstrakcie. Badania na **młodych osobach i upadkach zamierzonych** (autorzy podkreślają). Jedna meta-analiza → 1/2, nie 2/2 | PMID 27592402, doi 10.1016/j.apmr.2016.08.460 | abstrakt | S70 |
| 7 | Slapping nie daje korzyści i może uszkodzić rękę/nadgarstek | PARTIAL | abstrakt: wszystkie strategie **poza „slapping”** istotnie zmniejszały obciążenie przy upadku. O **uszkodzeniu ręki/nadgarstka/łokcia abstrakt nic nie mówi** — dopisek modelu (źródła modelu: blogi medicalguardian, scienceoffalling) | jw. | abstrakt | S70 |
| 8 | Trening strzałkowych u tenisistów i koszykarzy zapobiega skręceniom | ✘ jako dowód | Jing Y 2026, *Peroneal Muscle Training Effects on Tennis Player Lateral Ankle Sprain Prevention*, Lecture Notes in Education Psychology and Public Media 133:90–97 (EWA Publishing, materiały konferencyjne); afiliacja: **Fairmont Preparatory Academy** (szkoła średnia); przegląd narracyjny bez danych własnych; koszykówki w abstrakcie brak. **Odrzucone jako dowód.** W bazie mamy lepsze: [S16] Vriend, [S17] Doherty, [S54] Stephenson (trening nerwowo-mięśniowy/równowagi, nie izolowane strzałkowe) | doi 10.54254/2753-7048/2026.32951 | abstrakt (Crossref) | S71 (odrzucone) |
| 9 | Abbasi 2025: zmęczenie ↑ koślawienie głównie w obunóżnym skoku; „280 studies” | PARTIAL | **280 rekordów znalezionych, 29 włączonych** (model: „280 studies” ✘). Wniosek: istotny wzrost tylko w **obunóżnym drop jumpie** (w wynikach: u mężczyzn); w innych zadaniach brak efektu; protokoły zmęczenia „zwinność” i „schody” ↑ DKV we wszystkich zadaniach | PMID 40605118, PMC12220483 | abstrakt | S72 |
| 10 | „Impact Forces During Skateboarding Landings” 2014, n=7, 4,74× BW | PARTIAL (korekta 15:20) | **Liczba i n istnieją**, ale w innej pracy: **Frederick, Determan, Whittlesey, Hamill 2006, J Appl Biomech** — 7 skaterów, *ollie down* z platformy 45,7 cm: szczyt VGRF 4,74 ± 0,46 BW (część 1 raportu podała to poprawnie). Tytuł i rok w części 3 błędne: *Impact forces during skateboarding landings* to abstrakt CSB 2004 (n=10, rail slide, ≈ 7,9× i 12,2× BW). Wszystkie trzy prace (2004, 2006, 2010) — ta sama grupa (Sole Technology / Frederick, Determan) → 1/2. *Pierwsza wersja tej weryfikacji (commit 4059aef) błędnie uznała 4,74 za zmyślone.* | PMID 16760565; CSB 2004 s. 27–28 | abstrakt; pełny tekst abstraktu CSB | S78; S74; S52 |
| 11 | NO DATA: dawkowanie prewencyjne strzałkowych/piszczelowego tylnego u zdrowych; siła przedramienia a złamania nadgarstka | NO DATA (wg modelu) | nie weryfikowano przeszukaniem systematycznym; zapisane jako luka | — | — | — |
| 12 | Sprzeczność: siła biodra a DKV | ✔ sprzeczność istnieje | Alzahrani 2021 (przegląd 7 badań): związek siły odwodzicieli z DKV — 2 badania ujemny, 2 dodatni, 3 brak; dla prostowników i rotatorów zewn. też niespójnie; autorzy zalecają mierzyć **siłę ekscentryczną** i zadania skokowe. „Przegląd 2026” modelu nieustalony | PMID 34300118 | abstrakt | S73 |
| 13a | Progresja plyometrii = „CONSENSUS” | ✘ etykieta → `{OPINIA}` | The Movement System (YouTube, „5 Levels”: snap downs/drop freezes → box jumps → vertical jump → depth jump 12 → 24+ cali → warianty) = źródło infografiki; Thirst Gym (brandonsmitley.com, 5-step: snap downs / depth drops 12–18 cali → box jumps → skoki z podłoża → depth drop + skok reaktywny); HSS — artykuł poradnikowy z wypowiedzią fizjologa wysiłku (drop squat → pogo → depth drop 8–12 cali → skoki → box/płotki), **nie wytyczne kliniczne** → też `{OPINIA}` | linki w sources | strony | S75–S77 |
| 13b | „Grind posture specificity” | `{SPEKULACJA}` ✔ etykieta | brak danych | — | — | — |
| 13c | Makio/sweatstance ekscentrycznie obciąża strzałkowe; core przeciw koślawieniu przy lądowaniu ze schodów | `{WNIOSKOWANIE}` | oparte na przesłankach z innych populacji; liczba 4,74× BW nieprawdziwa (zob. 10) | — | — | — |

### Błędy i nadużycia modelu (podsumowanie)

- „2/2” dla pojedynczych prac (Steib, Moon ×2, Jing) — jedna praca to 1/2.
- Pomylone prace: tytuł Larwa 2021 przypisany „Uddin 2026”; IJORO poza MEDLINE.
- Źródło #8 to przegląd ucznia szkoły średniej w materiałach konferencyjnych — oznaczone jako „CONFIRMED 2/2”.
- #10: zły tytuł i rok (liczba 4,74× BW i n=7 są prawdziwe, ale z Frederick 2006, *ollie down* z 45,7 cm — korekta po części 1).
- Nadinterpretacje: „< 900 kontaktów chroni ścięgna” (badanie o wysokości skoku); „slapping uszkadza nadgarstek” (brak w abstrakcie); „n=217” (brak); „280 studies” (to rekordy, włączono 29).
- Fésüs: pominięte, że to pilotaż i że efekt dotyczył tylko CMJ, nie lądowania.
- JFMK: twierdzenie z abstraktu konferencyjnego podane jako wynik przeglądu.
- „CONSENSUS” dla blogów i filmów trenerów → `{OPINIA}`; „EVIDENCE” dla praktycznych zaleceń (dawki plyometrii, upadki na beton, rolki AGV) → `{WNIOSKOWANIE}`/`{ANALOGIA}`.

---

## Część 1 raportu F (dosłana przez Tomasza ~15:18) — surowe streszczenie, NIEZWERYFIKOWANE

Tytuł raportu: *Physical Preparation and Injury Prevention for Aggressive Inline Skating: A Comprehensive Biomechanical and Evidence-Based Analysis*. Raport = część 1 (poniżej) + infografika + część 3 (zweryfikowana wyżej).

Executive summary modelu: NMT 10–15 min, 2–3×/tydz., −42% urazów KD u młodzieży; prewencyjne dawkowanie strzałkowych/piszczelowego tylnego — tylko ekstrapolacja z koszykówki i tenisa; core i wytrzymałość/ekscentryka odwodzicieli przeciw DKV; młodzież: < 900 kontaktów CMJ w bloku 8–10 tyg.; brak dowodów, że wzmacnianie przedramienia chroni przed złamaniem — liczy się technika upadania.

Nowe twierdzenia (cytowania modelu w nawiasach):
1. Steib 2017: okres < 6 mies. wystarcza, dłuższe nie lepsze (cite 1, 2); u wytrenowanych NMT w rozgrzewce poprawia też skoki, sprint i równowagę (cite 3).
2. Po skręceniu kostki — deficyty siły koncentrycznej i ekscentrycznej ewertorów, inwertorów i zginaczy podeszwowych (cite 4).
3. Trening propriocepcji / balance board: prawie 50% mniej nawrotów skręceń u osób po skręceniu; rozgrzewka NMT do 36% mniej urazów KD u koszykarzy (cite 7).
4. vGRF 3,5–4,3× masy ciała w typowych skokach, do 6,8× w niektórych drop landingach (cite 9, 10).
5. Skateboarding, *ollie down* z 45,7 cm: średnio 4,74× BW (cite 11).
6. DKV (przywiedzenie i rotacja wewn. biodra, odwiedzenie kolana, rotacja zewn. piszczeli) jako główny mechanizm ACL (cite 12, 13).
7. Indeks stabilności core i indeks łuku stopy przewidują DKV w przysiadzie jednonóż (cite 16).
8. Prostowniki biodra minimalizują przywiedzenie przy lądowaniu jednonóż; 4-tygodniowy program siłowy zmienił mechanikę lądowania (cite 18, „Source 4”).
9. Chen 2023: łączny czas 400–600 min, programy 8–10 tygodni najbardziej skuteczne (cite 21, 23, 24).
10. Przykładowy plan tygodnia (pon. NMT 15 min + jazda; wt. core/biodro 15 min; śr. NMT 15 min; czw. odpoczynek/mobilność łydki; pt. NMT 10 min + upadki; weekend bez plyometrii) oraz 5-krokowa progresja: snap downs/drop freezes → box jumps → skoki pionowe/pogo → depth jumps ze skrzyni **8–12 cali** → skoki reaktywne/kierunkowe („sports conditioning consensus”, cite 25–27).
11. Kostka w AGV „stale w ekstremalnej inwersji i ewersji”, szczególnie przy soul i royale.

## Weryfikacja części 1 (Grok Bot, 2.11.2026)

| # | Twierdzenie | Wynik | Co mówi źródło / różnica | Identyfikator | ID w bazie |
|---|---|---|---|---|---|
| 1a | Steib: < 6 mies. wystarcza, dłużej nie lepiej | ✔ | „Interventions lasting more than 6 months were not superior”; efekt osiągalny w 20–60 sesjach i < 6 mies. | PMID 29184511 | S62 |
| 1b | NMT u wytrenowanych poprawia skoki, sprint, równowagę (cite 3) | PARTIAL / cite nieustalone | Zech 2010 (przegląd 20 RCT, trening równowagi): poprawa kontroli posturalnej ✔; skoki, zwinność — „indications”, wyniki sprzeczne; siła i sprint — sprzeczne lub brak efektu; niska jakość badań. „Significantly enhances” — przesadzone. Zech jest współautorką Steib 2017 (ta sama grupa) | PMID 20617915 | S84 |
| 2 | Po skręceniu: deficyty siły ewertorów, inwertorów, zginaczy podeszwowych | PARTIAL | Khalaj 2020 (meta-analiza, 20 badań) dotyczy **przewlekłej niestabilności kostki (CAI)**, nie każdego skręcenia: niższa siła ekscentryczna i koncentryczna ewertorów, ekscentryczna i koncentryczna inwertorów, koncentryczna prostowników kolana. **Zginaczy podeszwowych abstrakt nie wymienia**; ekscentryczne zginacze grzbietowe bez różnicy | PMID 31937576 | S79 |
| 3a | Balance board: ~50% mniej nawrotów u osób po skręceniu | PARTIAL | Hupperets 2009 (RCT, 522 sportowców po skręceniu, 8 tyg. w domu): **−35%** nawrotów (RR 0,63; 22% vs 33%; NNT 9). McGuine & Keene 2006 (RCT, 765 licealistów, piłka nożna i koszykówka): ryzyko skręcenia **o połowę** (RR 0,56) — u wszystkich ćwiczących, u osób bez wcześniejszego skręcenia różnica nieistotna. Verhagen 2004 (siatkówka, 116 drużyn): mniej skręceń tylko u osób z wcześniejszym skręceniem; u osób po urazie kolana więcej przeciążeń kolana. „~50% mniej nawrotów” — zawyżone/zlane | PMID 19589822, 16476915, 15310562 | S81, S82, S80 |
| 3b | Rozgrzewka NMT: do 36% mniej urazów KD u koszykarzy | PARTIAL | Emery 2022 (SHRed, 11–18 lat): **−36% urazów kolana i kostki** (IRR 0,64), nie wszystkich KD; badanie quasi-eksperymentalne; 10-min program | PMID 34972488 | S83 |
| 4 | vGRF 3,5–4,3× BW w skokach, do 6,8× w drop landing | NOT FOUND | nie znaleziono źródła z tymi liczbami (PubMed, wyszukiwanie po frazach) → nie wchodzi | — | — |
| 5 | *Ollie down* 45,7 cm = 4,74× BW | ✔ | Frederick, Determan, Whittlesey, Hamill 2006: 7 skaterów, 4,74 ± 0,46 BW w 30–80 ms; celowo „twarde” lądowanie. Koryguje wcześniejsze ✘ w części 3 (zły tytuł i rok, liczba prawdziwa). Ta sama grupa co S52/S74 | PMID 16760565 | S78 |
| 6 | DKV jako mechanizm ACL | ✔ (istniejące źródła) | [S64] Hewett 2009 (wideo urazów), [S63] Larwa 2021 (przegląd). Nowych źródeł nie dodawano | — | S63, S64 |
| 7 | Indeks stabilności core i łuku stopy przewidują DKV | PARTIAL | Mozafaripour 2021: 30 zdrowych mężczyzn, przysiad jednonóż; indeks stabilności core — istotny predyktor (p = 0,001); **indeks łuku stopy p = 0,09 (nieistotny przy 0,05)**, choć autorzy piszą „associated” | PMID 34391258 | S85 |
| 8 | Prostowniki biodra minimalizują przywiedzenie; 4-tyg. program siłowy zmienił lądowanie | PARTIAL | Stearns & Powers 2014: 21 kobiet, 4 tyg. **plyometrii i ćwiczeń z perturbacją ukierunkowanych na biodro** (nie „program siłowy”), 3×30 min/tydz.: ↑ siła prostowników i odwodzicieli biodra, ↑ zgięcie kolana i biodra, ↓ odwiedzenie kolana (6,8° → 5,6°), więcej pracy prostowników biodra. „Minimalizują przywiedzenie” — brak w abstrakcie; brak grupy kontrolnej | PMID 24464929 | S86 |
| 9 | Chen 2023: 400–600 min; 8–10 tygodni | PARTIAL | 400–600 min ✔ (CMJ 500–600, SJ 400–500); **„8–10 tygodni” — brak w abstrakcie** | PMID 38040837 | S69 |
| 10 | Plan tygodnia; 5 kroków z depth jumpem 8–12 cali | `{PROPOZYCJA}` modelu / `{OPINIA}` | Plan tygodnia — **propozycja modelu**, nie dowód (zapisany do `propozycje-do-recenzji.md`). Progresja: **rozbieżność wysokości** — tekst 8–12 cali (20–30 cm, jak „depth drop” w poradniku HSS [S75], tylko lądowanie), infografika i The Movement System [S76] 12 → 24+ cali (30–60+ cm, depth jump z odbiciem). Model zlał dwa źródła; „consensus” → `{OPINIA}` | — | S75, S76 |
| 11 | Kostka w AGV w ekstremalnej inwersji/ewersji przy soul i royale | `{WNIOSKOWANIE}` | brak pomiarów w AGV ([S02] nie mierzył kostki w płaszczyźnie czołowej) | — | — |

### Nowe błędy modelu (część 1)
- Mieszanie populacji i wyników: „nawroty” vs wszystkie skręcenia (McGuine), CAI vs każde skręcenie (Khalaj), „urazy KD” vs kolano + kostka (Emery).
- Dopisane szczegóły: zginacze podeszwowe, „8–10 tygodni”, „program siłowy”, „minimalizują przywiedzenie”.
- Indeks łuku stopy podany jako predyktor mimo p = 0,09.
- Zlanie wysokości depth jumpów z dwóch źródeł (8–12 vs 12–24+ cali).
- Moja korekta: liczba 4,74× BW z części 3 jest prawdziwa (Frederick 2006); błędny był tylko tytuł i rok.
