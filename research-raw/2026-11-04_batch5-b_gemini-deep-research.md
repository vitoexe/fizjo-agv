---
model: "Gemini Deep Research (aplikacja Gemini, tryb Pro „Rozszerzony”)"
narzedzie: "Aplikacja Gemini (gemini.google.com, Pro, przeglądarka, bez klucza API)"
data: 2026-11-04
godzina_raportu: "01:44 czasu warszawskiego (karta raportu 4 lis 01:44)"
plik_promptu: "prompts/batch-5-uzupelnienia-3/b-sciegna.prompt.txt"
commit_promptu: "692c3ce"
url_czatu: "https://gemini.google.com/app/02256e4dbbd6fdfe"
dokument_eksportu: "Google Doc 1lQxH8EmdUrhAmbJKPOFLoP_xn8bQhv-v6Yi3aMkDPNE („Tendon Loading Literature Verification”)"
ustawienia: "Deep Research w aplikacji Gemini, model Pro, tryb Rozszerzony"
eksport: "Eksport Google Docs → Markdown (Drive export, tylko odczyt); usunięte tylko znaki ucieczki Markdown (\\_, \\-, \\., \\[, \\], \\:, \\#, \\+, \\)); poza tym tekst bez zmian"
status_weryfikacji: "zweryfikowane (4.11.2026): 3 źródła × PMID/DOI/PMCID = 9 identyfikatorów (2 znane NMA + 1 nowe RCT) — wszystkie istnieją i zgadzają się z autorem, rokiem i tytułem; błędy opisu: Liu 2026 — „za wyższością ekscentryki” myli przeciążenie ekscentryczne (Frohm 2007) z klasyczną ekscentryką, autorzy Liu Y, Li C, Yang F (model: „pełna lista niedostępna”); Lee 2025 — „w przeglądzie: nie sprawdzono” (sprawdziliśmy: nie mogło być w Bischof 2024), model pominął wcześniejsze RCT tej samej grupy Lee 2023 (PMID 36776971); przypisy numerowane i blogi mimo zakazu; do bazy: nic — B3 sprzeczne między niezależnymi grupami (sztywność vs przekrój), B1 nadal sprzeczne (listy badań porównane), B2, B4–B7 bez nowych źródeł — szczegóły w sekcji Triage"
---

# **Raport badawczy: Weryfikacja doniesień dotyczących obciążania ścięgien (Fizjo AGV)**

## **1. Podsumowanie**

Przeprowadzono rygorystyczną analizę weryfikacyjną siedmiu twierdzeń z zakresu rehabilitacji i biomechanicznego obciążania ścięgien. Zidentyfikowano jedno twierdzenie poparte częściowo nowym, niezależnym badaniem pierwotnym (B3) oraz jeden przypadek istotnej sprzeczności w literaturze naukowej dotyczącej hierarchii metod (B1). Dla pozostałych pięciu twierdzeń (B2, B4, B5, B6, B7) nie znaleziono w dostępnych bazach danych drugiego, w pełni niezależnego badania pierwotnego, które spełniałoby wyśrubowane kryteria włączenia. Liczba źródeł sklasyfikowanych jako UNVERIFIED wynosi 0.

## **2. Twierdzenia**

### **B1**

| Źródło znane | Nowe źródło [Autor rok, PMID] | Skąd (punkt startowy / baza) | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Współautorzy; w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| N/A | [Li 2024, 39559237] | Baza z zapytania (NMA) | Network meta-analysis | adults with patellar tendinopathy | Brak dla całej sieci (7 badań włączonych) | "eccentric training (0.01 in Rank 1 and 0.06 in Rank 8) is the worst method for increasing VISA-P level" (Abstract) | Li Y, Sun D, Fang Y, Lu Z, Shi F, Liu G, Gu Y; nie dotyczy |
| N/A | [Liu 2026, 42192475] | Baza z zapytania (NMA) | Network meta-analysis | patellar tendinopathy | 313 (w zrewidowanej sieci głównej) | "Eccentric overload showed the most favorable point estimate versus HSR [...] Flywheel training [...] and concentric exercise [...] were estimated to perform less favorably than HSR" (Abstract/Results) | Liu (pełna lista niedostępna); nie dotyczy |

**Strony sporu:** Za wyższością przeciążenia ekscentrycznego nad innymi metodami, lub przynajmniej za brakiem wyraźnej słabości tej formy, opowiada się praca Liu 2026, podczas gdy analiza Li 2024 wskazuje protokół ekscentryczny jako stanowczo najmniej skuteczną metodę poprawy wskaźników VISA-P1. Różnice wynikają z reżimu metodologicznego: sieć Li 2024 opiera się łącznie na zaledwie 7 próbach badawczych, podczas gdy zrewidowana sieć pierwotna Liu 2026 włączyła 10 prób (z 17 zidentyfikowanych jakościowo), przy czym badacze celowo wykluczyli interwencje łączone (np. ćwiczenia + terapie adiuwantowe), argumentując to dążeniem do "czystszej konceptualnie połączonej sieci". Obie metaanalizy sieciowe częściowo się pokrywają, włączając fundamentalne badania historyczne (np. Jonsson 2005, Kongsgaard 2009)1.  
Rozbieżność ta rzuca światło na systemowy problem analizowania danych w rehabilitacji sportowej. Metaanalizy sieciowe są wysoce wrażliwe na dobór węzłów (nodes), a różnorodność kliniczna w diagnozowaniu i określaniu dawki treningowej w tendinopatii rzepki drastycznie wpływa na model statystyczny1. Wykluczenie protokołów łączonych pozwala zredukować szum wynikający z nakładających się mechanizmów biologicznych, jednak podkreśla, że pozycja treningu ekscentrycznego silnie zależy od struktury grupy kontrolnej.

### **B2**

| Źródło znane | Nowe źródło [Autor rok, PMID] | Skąd (punkt startowy / baza) | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Współautorzy; w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Beyer 2015 | NIE ZNALEZIONO | Forward citations (Beyer 2015), PEDro | - | - | - | - | - |

**Werdykt:** brak drugiego źródła — nie zidentyfikowano drugiego niezależnego, randomizowanego badania klinicznego bezpośrednio i czysto porównującego skuteczność HSR z izolowanym treningiem ekscentrycznym w tendinopatii Achillesa.  
Choć podejście oparte na protokole Heavy Slow Resistance (HSR) zdobyło powszechne uznanie jako równorzędna, a często bardziej optymalna pod względem przestrzegania zaleceń (adherence) alternatywa dla klasycznego treningu ekscentrycznego3, opublikowana literatura rzadko dostarcza prób replikacji na poziomie RCT zaproponowanym oryginalnie przez Beyera i Kjaera. Mechanizmy stymulacji ścięgna zależą przede wszystkim od wielkości obciążenia mechanicznego, a nie od wyizolowanego typu skurczu mięśniowego. Z tego względu w domenie badawczej i klinicznej ugruntowało się założenie o mechanistycznej i biologicznej równoważności obu podejść dla tkanki ścięgnistej, co paradoksalnie mogło zahamować zapotrzebowanie na dalsze kosztowne replikacje dokładnie tego samego schematu badawczego6.

### **B3**

| Źródło znane | Nowe źródło [Autor rok, PMID] | Skąd (punkt startowy / baza) | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Współautorzy; w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Jerger 2022, Jerger 2023, Bischof 2024, Miyamoto 2025 | [Lee 2025, 39207908] | Forward citations (Jerger 2022) | Randomised trial | professional female soccer athletes | 11 | "percentage changes in tendon stiffness [...] and Young's modulus [...] were higher in COL vs. PLA", ale dla przekroju poprzecznego "main effect of training [...] no main effect for group" (Full text) | Lee J, Robshaw DC, Erskine RM; nie sprawdzono |

**Werdykt:** częściowo potwierdzone (badanie potwierdza, że suplementacja peptydami kolagenowymi znacząco zwiększa sztywność ścięgna przy połączeniu z treningiem w stosunku do samego treningu, jednak wzrost pola przekroju poprzecznego przypisano wyłącznie obciążeniu treningowemu, bez addytywnego efektu kolagenu)8.  
Wpływ hydrolizowanych peptydów kolagenowych na przebudowę macierzy zewnątrzkomórkowej podlega zjawiskom mechanotransdukcji. Dodatek kolagenu (często stymulowanego obecnością witaminy C) w odpowiednim przedziale czasowym okołotreningowym potęguje adaptacje mikroskopowe, promując ściślejszą organizację włókien, co manifestuje się wzrostem wskaźnika Young's modulus8. Wyniki uzyskane w próbie na profesjonalnych piłkarkach wskazują, że makroskopowy wzrost przekroju poprzecznego (CSA) pozostaje adaptacją zależną głównie od naprężeń ścinających i rozciągających indukowanych dużym ciężarem, na które sam profil aminokwasowy surowicy wpływa w stopniu wtórnym.

### **B4**

| Źródło znane | Nowe źródło [Autor rok, PMID] | Skąd (punkt startowy / baza) | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Współautorzy; w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Alvarez 2006, Kulig 2009, Ross 2018, Gómez-Jurado 2021 | NIE ZNALEZIONO | Forward citations (Kulig 2009), bazy hiszpańsko/portugalskojęzyczne | - | - | - | - | - |

**Werdykt:** brak drugiego źródła — pomimo intensywnych poszukiwań nie wyłoniły się nowe rygorystyczne i niezależne próby badawcze (RCT lub prospektywne kohorty) analizujące terapię skojarzoną ortezy wraz z systematycznym ćwiczeniem.  
Niewydolność ścięgna mięśnia piszczelowego tylnego, klasyfikowana szerzej jako postępująca deformacja zapadającego się łuku stopy (PCFD), stanowi wybitne wyzwanie diagnostyczne i terapeutyczne10. Mimo iż zachowawcze strategie łączące pasywne podparcie strukturalne (ortezy redukujące napięcie rozciągające na ścięgno) z aktywną modyfikacją mechaniczną (progresywne ładowanie) uznaje się za złoty standard na etapach I-II, to niezależny materiał dowodowy obarczony jest silnym szumem metodologicznym. Badacze natrafiają na fundamentalne bariery związane ze skonstruowaniem interwencji kontrolnej i oporem środowisk ortopedycznych względem ujednolicenia protokołów10.

### **B5**

| Źródło znane | Nowe źródło [Autor rok, PMID] | Skąd (punkt startowy / baza) | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Współautorzy; w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Silbernagel 2007, Sancho 2019 | NIE ZNALEZIONO | Forward citations (Silbernagel 2007, Sancho 2019) | - | - | - | - | - |

**Werdykt:** brak drugiego źródła — nie zidentyfikowano zewnętrznych walidacji opartych na nowszych badaniach pierwotnych o wysokiej sile dowodowej, rygorystycznie testujących sam model ramowy monitorowania bólu.  
Zarządzanie dozowaniem obciążenia opiera się obecnie mocno na pionierskim paradygmacie dopuszczalnego bólu i odpowiedzi w kolejnych 24 godzinach. Brak nowych badań pierwotnych nie jest efektem odrzucenia tego podejścia, lecz paradoksalnie jego absolutnej absorpcji do praktyki ogólnoklinicznej, w której wyłączenie tego elementu staje się nieetyczne dla grupy kontrolnej5. Dalsze testowanie progu na skali VAS ewoluowało bardziej w stronę analizy neuromotorycznych ubytków wywołanych nocycepcją niż ewaluacji efektywności długoterminowego podtrzymywania samej reguły.

### **B6**

| Źródło znane | Nowe źródło [Autor rok, PMID] | Skąd (punkt startowy / baza) | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Współautorzy; w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Scattone Silva 2024 | NIE ZNALEZIONO | Forward citations (Scattone Silva 2024, Zwerver 2007) | - | - | - | - | - |

**Werdykt:** brak drugiego źródła — brakuje innych tak obszernych analiz rankujących dziesiątki ćwiczeń naraz pod kątem dystrybucji i całkowitego szacowanego obciążenia ścięgna rzepki.  
Modelowanie biomechaniczne obciążeń struktur pasywnych dla bardzo specyficznych wariantów kinematycznych ćwiczeń rehabilitacyjnych wymaga zastosowania złożonych metod dynamiki odwrotnej5. Powszechnie badane parametry redukują się zazwyczaj do porównań dwuwymiarowych (np. przysiad w oparciu o płaszczyznę płaską vs. skośną), ponieważ kalkulacja całych hierarchii indeksu obciążeniowego (tzw. load index) angażuje niezwykle zasobochłonne architektury obliczeniowe i systemy optoelektroniczne. Brak drugiego źródła wykazuje, jak rzadkimi inicjatywami są kompleksowe rankingi inżynieryjno-kinezjologiczne.

### **B7**

| Źródło znane | Nowe źródło [Autor rok, PMID] | Skąd (punkt startowy / baza) | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Współautorzy; w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Hullfish 2024 | NIE ZNALEZIONO | Forward citations (Hullfish 2024) | - | - | - | - | - |

**Werdykt:** brak drugiego źródła — pomimo wykluczenia dorobku głównej grupy badawczej obracającej się w tych zagadnieniach (Baxter), inne zespoły nie opublikowały zbieżnych danych pomiarowych z udziałem żywych tkanek lub modeli in vivo badających wpływ takiego obuwia na odciążanie.  
Manipulacja kątem natarcia i całkowitym unieruchomieniem stawu skokowego w kierunku zgięcia podeszwowego wykorzystuje zjawisko pasywnej niewydolności struktur i relaksacji włókien kolagenowych przy zmniejszeniu ramienia siły mięśni łydek13. Pomimo szerokiego uznania tych zasad ze strony fizjologii klinicznej, bezpośrednie kwantyfikowanie tego zjawiska u zywych ludzi pozostaje trudne technicznie z racji wysoce inwazyjnego charakteru instalacji przetworników obciążenia na trzewiach ścięgna lub trudności z fuzją rezonansu magnetycznego i elastografii śledzącej.

## **3. Bibliografia (tylko nowe źródła)**

| # | Autorzy, rok, tytuł, czasopismo, tom:strony | Typ badania | n | PMID | DOI | PMCID |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Li Y, Sun D, Fang Y, Lu Z, Shi F, Liu G, Gu Y, 2024, Mixed comparison of intervention with eccentric, isometric, and heavy slow resistance for Victorian Institute of Sport Assessment Patella Questionnaire in adults with patellar tendinopathy: A systematic review and network meta-analysis, Heliyon, 10:e39171 | Network meta-analysis | Brak danych o łącznej liczbie (7 badań włączonych) | 39559237 | 10.1016/j.heliyon.2024.e39171 | PMC11570476 |
| 2 | Liu et al., 2026, [Brak nazwy czasopisma w zrzucie, praca powiązana z 10.1186/s13102-026-01743-4], [Brak tomu:stron] | Network meta-analysis | 313 (w zrewidowanej głównej sieci) | 42192475 | 10.1186/s13102-026-01743-4 | PMC13308153 |
| 3 | Lee J, Robshaw DC, Erskine RM, 2025, High-intensity resistance training and collagen supplementation improve patellar tendon adaptations in professional female soccer athletes, Exp Physiol, 110:1551-1560 | Randomised trial | 11 | 39207908 | 10.1113/EP092106 | PMC12576002 |

## **4. Identifier check**

| Źródło | PMID | DOI | PMCID | Strona otwarta? | Zgodne? tak/nie/UNVERIFIED |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [Li 2024, 39559237] | 39559237 | 10.1016/j.heliyon.2024.e39171 | PMC11570476 | tak | tak |
| [Liu 2026, 42192475] | 42192475 | 10.1186/s13102-026-01743-4 | PMC13308153 | tak | tak |
| [Lee 2025, 39207908] | 39207908 | 10.1113/EP092106 | PMC12576002 | tak | tak |

## **5. NIE ZNALEZIONO**

* B2 — punkty startowe: forward citations dla Beyer 2015. Bazy: PubMed, PEDro. Hasła: Achilles tendinopathy, heavy slow resistance, eccentric, RCT.  
* B4 — punkty startowe: forward citations dla Kulig 2009. Bazy: PubMed, SciELO, bazy czasopism hiszpańskojęzycznych/portugalskojęzycznych. Hasła: adult-acquired flatfoot, progressive collapsing foot deformity, posterior tibial tendon dysfunction, orthosis, exercise.  
* B5 — punkty startowe: forward citations dla Silbernagel 2007 i Sancho 2019. Bazy: PubMed, J-STAGE, Scholar. Hasła: tendinopathy, pain-monitoring model, daily tracking.  
* B6 — punkty startowe: forward citations dla Scattone Silva 2024 i Zwerver 2007. Bazy: Europe PMC. Hasła: patellar tendon load index, biomechanical analysis, ranking rehab exercises.  
* B7 — punkty startowe: forward citations dla Hullfish 2024. Bazy: PubMed, biomechanics journals. Hasła: Achilles tendon force, immobilising boot, plantarflexion, tendon load.

#### **Cytowane prace**

> 1. Comparative effectiveness of exercise interventions for patellar, [https://pmc.ncbi.nlm.nih.gov/articles/PMC13308153/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13308153/)  
> 2. Mixed comparison of intervention with eccentric, isometric ... - PMC, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11570476/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11570476/)  
> 3. Achilles Tendon Exercises to Avoid—and What to Do Instead, [https://www.theachillesdoc.com/post/best-exercises-for-achilles-tendon-pain-and-which-ones-to-avoid-an-evidence-based-guide](https://www.theachillesdoc.com/post/best-exercises-for-achilles-tendon-pain-and-which-ones-to-avoid-an-evidence-based-guide)  
> 4. The Tendinopathy Ultimate Guide 2026 \| Achilles, Patellar, Gluteal, [https://upwellhealth.com.au/upwell-blog/tendinopathy-ultimate-guide-2026](https://upwellhealth.com.au/upwell-blog/tendinopathy-ultimate-guide-2026)  
> 5. Heavy Slow Resistance Training for Tendinopathy: Achilles - Embodia, [https://embodiaapp.com/blog/488-heavy-slow-resistance-training-for-tendinopathy-achilles-patellar-elbow](https://embodiaapp.com/blog/488-heavy-slow-resistance-training-for-tendinopathy-achilles-patellar-elbow)  
> 6. (PDF) Putting “Heavy” into Heavy Slow Resistance - ResearchGate, [https://www.researchgate.net/publication/358147392_Putting_Heavy_into_Heavy_Slow_Resistance](https://www.researchgate.net/publication/358147392_Putting_Heavy_into_Heavy_Slow_Resistance)  
> 7. Exercise-induced adaptations in tendon tissue, [https://www.physoc.org/magazine-articles/exercise-induced-adaptations-in-tendon-tissue/](https://www.physoc.org/magazine-articles/exercise-induced-adaptations-in-tendon-tissue/)  
> 8. High‐intensity resistance training and collagen supplementation, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12576002/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12576002/)  
> 9. Hydrolyzed Collagen Supplementation Enhances Patellar Tendon, [https://research.setu.ie/en/publications/hydrolyzed-collagen-supplementation-enhances-patellar-tendon-adap/](https://research.setu.ie/en/publications/hydrolyzed-collagen-supplementation-enhances-patellar-tendon-adap/)  
> 10. Adult Acquired Flatfoot Deformity \| Ankleinfo - Foot and Ankle, [https://www.ankleinfo.net/adult-acquired-flatfoot-deformity](https://www.ankleinfo.net/adult-acquired-flatfoot-deformity)  
> 11. Adult-Acquired Flatfoot Deformity - PMC, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8696898/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8696898/)  
> 12. (PDF) Adult-Acquired Flatfoot Deformity - ResearchGate, [https://www.researchgate.net/publication/330447900_Adult-Acquired_Flatfoot_Deformity](https://www.researchgate.net/publication/330447900_Adult-Acquired_Flatfoot_Deformity)  
> 13. Achilles Tendinopathy Toolkit: Section A - Clinical Evaluation, [https://www.physio-pedia.com/Achilles_Tendinopathy_Toolkit:_Section_B_-_Clinical_Assessment](https://www.physio-pedia.com/Achilles_Tendinopathy_Toolkit:_Section_B_-_Clinical_Assessment)
---

## Triage (4.11.2026, Fizjo AGV)

Runda 3 dla twierdzeń B1–B7 z batch-4 2b. Prompt b poszedł tylko do aplikacji Gemini. Model nie jest źródłem. Wszystkie identyfikatory sprawdziliśmy w PubMed (esummary/efetch) i Crossref. Treść porównaliśmy z abstraktami, a dla B1 i B3 z pełnymi tekstami PMC (tabele badań włączonych do obu NMA, wyniki Lee 2025). Niezależność sprawdziliśmy po autorach i po liście piśmiennictwa Bischof 2024 w Crossref. Model oddał wszystkie 5 sekcji, ale mimo zakazu użył numerowanych przypisów i stron typu blog/klinika (przypisy 3–7, 9–13 = `{OPINIA}`, nie sprawdzaliśmy). Akapity „wyjaśniające” przy B2, B4, B5, B6 i B7 (np. „paradoksalnie mogło zahamować…”, „absolutnej absorpcji do praktyki”) nie mają źródeł i nie wchodzą.

### Identyfikatory

| Źródło (wg modelu) | PMID | DOI | PMCID | Wynik sprawdzenia |
|---|---|---|---|---|
| Li 2024 (znane, Heliyon 10(21):e39171) | 39559237 ✔ | 10.1016/j.heliyon.2024.e39171 ✔ | PMC11570476 ✔ | ✔ autorzy, rok, tytuł; cytat „0.01 in Rank 1 and 0.06 in Rank 8” dosłownie z abstraktu. Model podał je jako „nowe źródło”, a to źródło znane |
| Liu 2026 (znane, BMC Sports Sci Med Rehabil 18(1):296) | 42192475 ✔ | 10.1186/s13102-026-01743-4 ✔ | PMC13308153 ✔ | ✔ identyfikatory; ✘ model: autorzy „pełna lista niedostępna”, czasopismo „brak nazwy”. W rzeczywistości Liu Y, Li C, Yang F (Kunming, Kanton). Cytat dosłowny z abstraktu ✔ |
| Lee J, Robshaw DC, Erskine RM 2025 (Exp Physiol 110(11):1551–1560; epub 29.08.2024) | 39207908 ✔ | 10.1113/EP092106 ✔ | PMC12576002 ✔ | ✔ autorzy, rok, tytuł, n=11; oba cytaty zgodne z pełnym tekstem (3.4.1 i post hoc). W pracy: „single-blind, single-centre, randomized controlled trial” |

Razem: **9 identyfikatorów (3 PMID, 3 DOI, 3 PMCID; 2 źródła znane, 1 nowe)**. Wszystkie istnieją i zgadzają się z pierwszym autorem, rokiem i tytułem. **0 błędnych identyfikatorów.** Błędy opisu: brak autorów i czasopisma przy Liu 2026, źródła znane podane jako „nowe”, niezależność Lee 2025 niesprawdzona („nie sprawdzono”), pominięte wcześniejsze RCT tej samej grupy (Lee 2023), błędna interpretacja „ekscentryki” w B1 (niżej).

### Treść, niezależność, populacja — twierdzenie po twierdzeniu

| Tw. | Werdykt modelu | Nasz werdykt |
|---|---|---|
| B1 tendinopatia rzepki: ekscentryka vs HSR vs izometria (sprzeczne) | strony sporu; pokrycie „np. Jonsson 2005, Kongsgaard 2009” | **Nadal sprzeczne. Bez werdyktu, ale z porównaniem list badań (pełne teksty PMC).** Li 2024 (tab. 3) włączyło 7 badań: Jonsson 2005, Kongsgaard 2009, Gual 2016, Agergaard 2021, Breda 2021, Ruffino 2021, Knez 2023. Liu 2026: 17 RCT w syntezie jakościowej, 14 w szerszej analizie, 10 w głównej sieci (tab. 2–3): Jonsson 2005, Visnes 2005, Young 2005, Frohm 2007, Kongsgaard 2009, Agergaard 2021, Breda 2021, Ruffino 2021, Rieder 2022, Hjortshoej 2025. **Wspólne w głównych analizach: 5** (Jonsson, Kongsgaard, Agergaard, Breda, Ruffino). Tylko w Li: Gual 2016, czyli zawodnicy „not currently injured” z populacji „at risk” (opis w tab. 3 Li, tytuł Gual), a nie pacjenci z tendinopatią, oraz Knez 2023 (u Liu tylko w syntezie jakościowej). Tylko w głównej sieci Liu: Visnes, Young, Frohm, Rieder, Hjortshoej. Różnice metod według prac: Li szereguje metody prawdopodobieństwem rang (3 bazy). Liu: 11 baz do XII 2025, HSR jako odniesienie, wykluczone interwencje złożone, a rangi „exploratory”. **Błąd modelu:** Liu nie stwierdza „wyższości przeciążenia ekscentrycznego”. To węzeł *eccentric overload* (Frohm 2007), inny niż klasyczna ekscentryka na desce, z SMD 0,33 (95% CI −0,87 do 1,52) wobec HSR, czyli bez istotności. Klasyczna ekscentryka wobec HSR: SMD −0,23 (95% CI −1,02 do 0,56) (pełny tekst Liu, wyniki). Spór dotyczy więc rankingu (Li), a nie różnicy istotnej statystycznie (Liu). Do bazy nic — obie prace to NMA (przeglądy), nie źródła pierwotne. |
| B2 Achilles: HSR ≈ ekscentryka | NIE ZNALEZIONO | **1/2** (S09) — bez zmian. |
| B3 kolagen + trening a ścięgna | „częściowo potwierdzone” (Lee 2025) | **Sprzeczne między niezależnymi grupami. Nie 2/2.** Lee 2025 (Liverpool John Moores / UCL; Lee, Robshaw, Erskine) nie ma wspólnych autorów z Jerger 2022/2023 ani z Bischof 2024 i ukazało się po wyszukiwaniu Bischof 2024 (XII 2023), więc nie mogło być w nim włączone. **Jest niezależne.** Wynik jest jednak odwrotny niż u Jergera: u Lee 30 g kolagenu + 500 mg wit. C, 10 tyg. przedsezonowego treningu, 11 zawodowych piłkarek (6 vs 5). Sztywność więzadła rzepki +15,4% vs +4,6% i moduł Younga +14,2% vs +3,4% wzrosły bardziej niż przy placebo, a dla przekroju (CSA) był tylko efekt treningu, bez interakcji (P=0,934) (abstrakt, pełny tekst 3.4.1). U Jergera 2022/2023 (5 g/d, 14 tyg., aktywni mężczyźni) większy przyrost CSA przy kolagenie, a sztywność bez różnic. Model pominął wcześniejsze RCT tej samej grupy: **Lee J, Bridge JE, Clark DR, Stewart CE, Erskine RM 2023**, Front Physiol 14:1089971, PMID 36776971, doi:10.3389/fphys.2023.1089971, PMC9910607. To 17 piłkarek U21, a wynik jest ten sam co w Lee 2025 (sztywność +18,0% vs +5,1%, CSA bez zmian). Lee 2023 jest w piśmiennictwie Bischof 2024 (Crossref). Lee 2023 i Lee 2025 to jedna grupa, więc nie są od siebie niezależne. **Bilans:** sztywność ↑ — 1 grupa (Erskine, 2 RCT), przy zerowym wyniku drugiej grupy (König). CSA ↑ — 1 grupa (König, 2 RCT), przy zerowym wyniku drugiej (Erskine). Różnice według prac: dawka (30 g vs 5 g), płeć, poziom sportowy, rodzaj treningu (piłka + siła vs trening oporowy), czas (10 vs 14 tyg.). Bardzo małe grupy (n=11, 17). Etykieta populacji: `{ANALOGIA:piłkarki}` / `{ANALOGIA:aktywni mężczyźni}`, zdrowi, nie tendinopatia. **Odłożone jako sprzeczne.** |
| B4 PTTD I–II: orteza + ćwiczenia | NIE ZNALEZIONO | **1/2** (S08) — bez zmian. Przypisy 10–12 to strony kliniczne i przegląd narracyjny (PMC8696898, nie sprawdzaliśmy), `{OPINIA}` / nie pierwotne. |
| B5 model monitorowania bólu | NIE ZNALEZIONO | **1/2** (S11) — bez zmian. Kandydat Sancho 2019 z rundy 2 nadal czeka na sprawdzenie progu w pełnym tekście. |
| B6 pełny ranking obciążenia więzadła rzepki | NIE ZNALEZIONO | **1/2** (S167) — bez zmian. Wąska część (deska skośna vs płasko) już 2/2 (S167 + S168). |
| B7 but w zgięciu podeszwowym a obciążenie Achillesa | NIE ZNALEZIONO | **1/2** (Hullfish 2024) — bez zmian. Akapit o „przetwornikach obciążenia” i MRI bez źródła. |

### Co weszło do bazy

Nic. Żadne twierdzenie nie spełniło reguły 2/2 (dwa niezależne źródła pierwotne zgodne co do tego samego wyniku).

### Co odłożono

- **B3** — sprzeczne: Lee 2025 (+ Lee 2023, ta sama grupa) i Jerger 2022/2023 to niezależne grupy, ale z różnymi wynikami (sztywność vs przekrój). Potrzebne RCT trzeciej grupy, mierzące oba parametry. W bazie tylko dopisek przy TODO w `filar-1-przygotowanie/obciazenie-i-periodyzacja.md` (bez nowego twierdzenia).
- **B1** — sprzeczne. Opisane listy badań i różnice metod. Rozstrzygnąć może tylko recenzja fizjoterapeuty albo nowe RCT, nie kolejna runda wyszukiwania.
- B2, B4, B5, B6 (pełny ranking), B7 — **brak drugiego źródła** po 3 rundach (batch-1 B, batch-4 2b, batch-5 b; różne strategie: słowa kluczowe, a potem cytowania wstecz/w przód i bazy spoza głównego nurtu).

### Sprzeczności z bazą

Brak. Kolagenu nie ma w bazie jako twierdzenia (tylko TODO). B1 nie dotyczy żadnego wpisu w bazie (brak pliku tendinopatii rzepki). Dane o rzepce nie przenoszą się na `achilles/tendinopatia.md` (S09).

### Czy runda dodała coś nowego

Tak, ale nic do bazy. Jedno nowe niezależne RCT (Lee 2025) i jedno pominięte przez model (Lee 2023, ta sama grupa) zmieniły B3 z „jedna linia badań” na „sprzeczne między grupami”. Dla B1 mamy teraz porównanie list włączonych badań: 5 wspólnych, a różnice to Gual 2016 (osoby bez tendinopatii) u Li oraz 5 innych RCT u Liu. Model błędnie odczytał wynik Liu. B2, B4–B7: runda nic nie dołożyła, więc zgodnie z zasadą kończenia rund twierdzenia zostają w research-raw jako „brak drugiego źródła”.

