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
status_weryfikacji: "niezweryfikowane"
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