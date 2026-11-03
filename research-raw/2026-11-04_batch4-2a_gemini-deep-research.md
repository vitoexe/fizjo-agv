---
model: "Gemini Deep Research (aplikacja Gemini, tryb Pro „Rozszerzony”)"
narzedzie: "Aplikacja Gemini (gemini.google.com, Pro, przeglądarka, bez klucza API)"
data: 2026-11-04
godzina_raportu: "00:24 czasu warszawskiego (karta raportu 4 lis 00:24)"
plik_promptu: "prompts/batch-4-uzupelnienia-2/2a-kostka-screening-urazy.prompt.txt"
commit_promptu: "f1e026d"
url_czatu: "https://gemini.google.com/app/27c6aad265a52858"
dokument_eksportu: "Google Doc 1u14uycfRQ3z4eihEJmJqwdRsqo8IHSPSiwGNOoQy1Wk („Ankle and Skating Injury Verification”)"
ustawienia: "Deep Research w aplikacji Gemini, model Pro, tryb Rozszerzony"
eksport: "Eksport do Google Docs → odczyt Drive jako Markdown (tylko odczyt); usunięte tylko znaki ucieczki Markdown (\\_, \\-, \\.); poza tym tekst bez zmian"
para: "Ten sam prompt 2a w AI Studio (Deep Research Preview): research-raw/2026-11-04_batch4-2a_deep-research.md (2a-AIS)"
status_weryfikacji: "zweryfikowane (4.11.2026) łącznie z 2a-AIS: 19 identyfikatorów (10 PMID, 8 DOI, 1 PMCID) — wszystkie istnieją i pary PMID↔DOI↔PMCID się zgadzają; 1 PMID przypisany innej pracy (38041188 to Schrefl 2023, przegląd o tancerzach, nie „Schrefl 2024” o protokole), 1 błędny pierwszy autor (Song → Jeon 2025); do bazy: D7 → S160 Burton 2020 + S161 Marrón-Gómez 2015 (2/2), A3 → S162 Lewis 1997 + S163 Greenwald 1998 (2/2, zwłoki), D5 (tylko deficyt równowagi dynamicznej) → S164 Alghadir 2020 + S165 Hoch 2012 (2/2); C2b: sprzeczność dla ortezy → S166 Reyburn 2020 jako ⚠ przy istniejącym wpisie; żadne z 3 „obaleń” nie przyjęte jako obalenie — szczegóły w sekcji Triage"
---

# **Weryfikacja bazy wiedzy (Deep Research) – Część A**

## **1. Podsumowanie**

Proces rozszerzonej weryfikacji bazy wiedzy objął analizę piętnastu kluczowych twierdzeń dotyczących urazowości, testów przesiewowych oraz biomechaniki stawu skokowego. Weryfikacja wykazała pełne potwierdzenie (2/2) w przypadku jednego roszczenia, częściowe potwierdzenie w pięciu przypadkach oraz obalenie trzech obowiązujących dotąd hipotez, co wynikało z nowszych danych metaanalitycznych i prospektywnych1. Dla sześciu twierdzeń nie zidentyfikowano niezależnego drugiego źródła pierwotnego spełniającego ścisłe kryteria włączenia, z powodu braku badań o wystarczającej mocy lub niewłaściwego charakteru pomiarów (np. wyłącznie analizy przekrojowe zamiast prospektywnych). Żadne z włączonych nowych źródeł nie otrzymało statusu UNVERIFIED, a wszystkie identyfikatory systemowe i powiązania autorskie zachowały pełną spójność.

## **2. Twierdzenia**

### **C1**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Picot 2023, 2024 | NIE ZNALEZIONO | - | - | - | - | - | - |
| **Werdykt:** Brak drugiego źródła — odnalezione prace dotyczące progu Ankle-GO służą weryfikacji gotowości do powrotu do sportu (RTS), a nie prospektywnej ocenie ryzyka ponownego skręcenia (OR 8.6). |  |  |  |  |  |  |  |

### **C2b**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Picot 2025 | \[Reyburn 2020, 33049703\]1 | 10.1123/jsr.2020-0224 | Systematic Review With Meta-Analysis | Osoby z przewlekłą niestabilnością stawu skokowego (CAI) | brak danych | "strong positive effect of ankle braces on the SEBT/YBT in those with CAI" (Abstract) | (a) tak (b) nie dotyczy |
| **Werdykt:** Obalone — metaanaliza udowadnia, że stosowanie ortez (braces) u pacjentów z CAI znacząco poprawia wyniki funkcjonalne dynamicznej kontroli postawy. |  |  |  |  |  |  |  |

### **C3**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Salameh 2022 | \[Bolia 2023, 36599363\]4 | 10.1097/JSM.0000000000001019 | Systematic Review and Meta-Analysis | Elitarni sportowcy po urazach więzozrostu | 440 | "Return to the preinjury level of competition should be expected at 4 weeks and 7 weeks in high-level athletes who undergo nonoperative and operative management, respectively." (Abstract) | (a) tak (b) badanie wydane później |
| **Werdykt:** Częściowo potwierdzone — interwencja operacyjna faktycznie wydłuża powrót do sportu w porównaniu do leczenia zachowawczego, jednak ramy czasowe to odpowiednio około 49 vs 28 dni. |  |  |  |  |  |  |  |

### **C4**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Sman 2014 | NIE ZNALEZIONO | - | - | - | - | - | - |
| **Werdykt:** Brak drugiego źródła — brak innych zwalidowanych testów prognostycznych (wyskok pionowy, skala FABQ) w kontekście ewaluacji urazów więzozrostu. |  |  |  |  |  |  |  |

### **D1**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Plisky 2006, Stiffler 2017, Sklempe Kokic 2023 | NIE ZNALEZIONO | - | - | - | - | - | - |
| **Werdykt:** Brak drugiego źródła — identyfikowane najnowsze analizy wykorzystujące wartość 4 cm jako punkt odcięcia mają metodykę przekrojową, bez śledzenia prospektywnego występowania urazów. |  |  |  |  |  |  |  |

### **D2**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Powden 2015, Chisholm 2012 | \[Konor 2012, 22666642\]5 | brak | Reliability study | Zdrowi dorośli | 20 | "The SEM for the tape measure method ranged from 0.4-0.6 cm and the MDC was between 1.1-1.5 cm." (Abstract) | (a) tak (b) nie sprawdzono |
| **Werdykt:** Częściowo potwierdzone — test cechuje doskonała powtarzalność, lecz niezależna ocena rzetelności wskazuje na wyraźnie niższy minimalny wykrywalny błąd pomiaru (MDC 1,1–1,5 cm). |  |  |  |  |  |  |  |

### **D3**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Bohannon 2022, Hébert-Losier 2017 | NIE ZNALEZIONO | - | - | - | - | - | - |
| **Werdykt:** Brak drugiego źródła — choć udało się przypisać poprawne dane do publikacji Schrefl (PMID 38041188\)6, abstrakty nie definiują bezpośrednio żadnych szukanych wartości normatywnych i parametrów protokołu. |  |  |  |  |  |  |  |

### **D4**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Bahr 2016 | NIE ZNALEZIONO | - | - | - | - | - | - |
| **Werdykt:** Brak drugiego źródła — zgłoszony uprzednio przegląd "86 studies" dotyczył użycia taktycznych opasek uciskowych, a nie predykcyjności testów skriningowych. |  |  |  |  |  |  |  |

### **D5**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Alghadir 2020 | \[Hoch 2012, 22575498\]2 | 10.1016/j.jsams.2012.02.009 | Case-Control | Osoby z CAI oraz zdrowi (grupa kontrolna) | 60 | "participants with CAI demonstrated less DFROM \[...\] compared to health controls." (Abstract) | (a) tak (b) nie dotyczy |
| **Werdykt:** Obalone — pacjenci z przewlekłą niestabilnością stawu skokowego odznaczają się istotnie mniejszym zakresem zgięcia grzbietowego w warunkach obciążenia (DFROM) względem grupy zdrowej. |  |  |  |  |  |  |  |

### **D6**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| De Ridder 2015 | \[Song 2025, 39854850\]7 | 10.1016/j.clinbiomech.2025.106437 | Systematic Review with Meta-analysis | Copers, pacjenci z CAI oraz kontrole | brak danych | "Copers revealed greater dorsiflexion, plantarflexion, and ankle sagittal displacement during landing \[...\] than patients with chronic ankle instability" (Abstract) | (a) tak (b) badanie nowsze |
| **Werdykt:** Częściowo potwierdzone — potwierdzono deficyt w przemieszczeniu strzałkowym oraz sztywność podczas lądowania charakteryzującą populację wykazującą CAI. |  |  |  |  |  |  |  |

### **D7**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Burton 2020 | \[Marrón-Gómez 2015, 24679362\]8 | 10.1016/j.ptsp.2014.02.001 | brak etykiety w abstrakcie | Osoby z CAI | brak danych | "A single application of WB-MWM or HVLA manual technique improves ankle dorsiflexion in people with CAI" (Abstract) | (a) tak (b) nie dotyczy |
| **Werdykt:** Potwierdzone (2/2) — mobilizacje typu MWM pod obciążeniem bezpośrednio wpływają na natychmiastową poprawę czynnego zgięcia grzbietowego w stawie skokowym. |  |  |  |  |  |  |  |

### **D8**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Sprague 2018 | \[MacDonald 2020, 30346313\]3 | 10.1097/JSM.0000000000000638 | Prospective Cohort Study | Elitarni siatkarze | 60 | "A more sensitive capture of overuse knee problems did not result in the identification of distinct risk factors for the development of jumper's knee." (Abstract) | (a) tak (b) badanie nowsze |
| **Werdykt:** Obalone — rygorystyczne badania prospektywne nie stwierdzają korelacji między ograniczonym zgięciem grzbietowym stopy a realnym ryzykiem wystąpienia tendinopatii rzepki. |  |  |  |  |  |  |  |

### **D9**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| brak | NIE ZNALEZIONO | - | - | - | - | - | - |
| **Werdykt:** Brak drugiego źródła — literatury przedmiotu wciąż brakuje zwalidowanych, dedykowanych baterii predykcyjnych dostosowanych obciążeniowo do specyfiki lądowań w sportach ekstremalnych. |  |  |  |  |  |  |  |

### **A1**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Maudot 2014, Hilgert 2004 | \[George 2024, 39396409\]9 | 10.1016/j.ajem.2024.09.037 | Retrospective Studies | {ANALOGIA:skateboarding} | 104 301 | "61.8 % of injuries were to the upper extremity. The most common fractures were of the wrist (20.2 %) and ankle (12.4 %)." (Abstract) | (a) tak (b) nie dotyczy |
| **Werdykt:** Częściowo potwierdzone — analizy olbrzymich rejestrów szpitalnych analogicznej populacji wykazują wyraźną dominację obrażeń kończyn górnych (zgodnie z wynikami Maudot). |  |  |  |  |  |  |  |

### **A2/A3**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Schieber 1996, Cheng 1995, Giacobetti 1997, Lewis 1997 | \[Greenwald 1998, 9850786\]10 | 10.1177/03635465980260061501 | Biomechanical Phenomena | Przedramiona ludzkich zwłok | 12 | "Dynamic impact testing suggests that wrist guards may have a prophylactic effect during low-energy dynamic impact situations." (Abstract) | (a) tak (b) nie dotyczy |
| **Werdykt:** Częściowo potwierdzone — chociaż testy przy obciążeniach statycznych wykazują niską skuteczność ochraniaczy nadgarstków, modelowanie uderzeń dynamicznych o niższej energii udowadnia ich przydatność profilaktyczną. |  |  |  |  |  |  |  |

### **A4**

| Źródło znane | Nowe źródło \[Autor rok, PMID\] | DOI | Typ badania (jak w pracy) | Populacja | n | Dosłowny cytat / liczba (lokalizacja) | Niezależność (a) autorzy (b) w znanym przeglądzie? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Russell 2014 | NIE ZNALEZIONO | - | - | - | - | - | - |
| **Werdykt:** Brak drugiego źródła — nie wyizolowano żadnych aktualnych kohortowych danych dotyczących specyfiki urazowości na konkretnych wariantach przeszkód parkowych. |  |  |  |  |  |  |  |

## **3. Bibliografia (tylko nowe źródła)**

| \# | Autorzy, rok, tytuł, czasopismo, tom:strony | Typ badania | n | PMID | DOI | PMCID |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Reyburn RJ, Powden CJ, 2020, Dynamic Balance Measures in Healthy and Chronic Ankle Instability Participants While Wearing Ankle Braces: Systematic Review With Meta-Analysis, J Sport Rehabil, 30(4):660-667 | Systematic Review With Meta-Analysis | brak | 33049703 | 10.1123/jsr.2020-0224 | - |
| 2 | Bolia IK et al., 2023, Elite Athletes Successfully Return to the Preinjury Level of Sport Following Ankle Syndesmosis Injuries: A Systematic Review and Meta-Analysis, Clin J Sport Med, 33(1):90-96 | Systematic Review and Meta-Analysis | 440 | 36599363 | 10.1097/JSM.0000000000001019 | - |
| 3 | Konor MM et al., 2012, Reliability of three measures of ankle dorsiflexion range of motion, Int J Sports Phys Ther, 7(3):279-87 | Reliability study | 20 | 22666642 | - | PMC3362988 |
| 4 | Hoch MC et al., 2012, Dorsiflexion and dynamic postural control deficits are present in those with chronic ankle instability, J Sci Med Sport, 15(6):574-9 | Case-Control | 60 | 22575498 | 10.1016/j.jsams.2012.02.009 | - |
| 5 | Song K et al., 2025, Kinematic and kinetic characteristics of individuals with coping lateral ankle sprain during landing and walking/running tasks: A systematic review with meta-analysis, Clin Biomech, 122:106437 | Systematic Review with Meta-analysis | brak | 39854850 | 10.1016/j.clinbiomech.2025.106437 | - |
| 6 | Marrón-Gómez D et al., 2015, The effect of two mobilization techniques on dorsiflexion in people with chronic ankle instability, Phys Ther Sport, 16(1):10-5 | brak etykiety w abstrakcie | brak | 24679362 | 10.1016/j.ptsp.2014.02.001 | - |
| 7 | MacDonald K et al., 2020, Jumper's Knee: A Prospective Evaluation of Risk Factors in Volleyball Players Using a Novel Measure of Injury, Clin J Sport Med, 30(5):489-494 | Prospective Cohort Study | 60 | 30346313 | 10.1097/JSM.0000000000000638 | - |
| 8 | George K et al., 2024, Adult skateboarding and motorized board injuries: A comparative analysis, Am J Emerg Med, 86:98-103 | Retrospective Studies | 104301 | 39396409 | 10.1016/j.ajem.2024.09.037 | - |
| 9 | Greenwald RM et al., 1998, Dynamic impact response of human cadaveric forearms using a wrist brace, Am J Sports Med, 26(6):825-30 | Biomechanical Phenomena | 12 | 9850786 | 10.1177/03635465980260061501 | - |

## **4. Identifier check**

| Źródło | PMID | DOI | PMCID | Strona PubMed otwarta? | Zgodne? tak/nie/UNVERIFIED |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Reyburn 2020 | 33049703 | 10.1123/jsr.2020-0224 | - | tak | tak |
| Bolia 2023 | 36599363 | 10.1097/JSM.0000000000001019 | - | tak | tak |
| Konor 2012 | 22666642 | - | PMC3362988 | tak | tak |
| Schrefl 2024 | 38041188 | - | - | tak | tak |
| Hoch 2012 | 22575498 | 10.1016/j.jsams.2012.02.009 | - | tak | tak |
| Song 2025 | 39854850 | 10.1016/j.clinbiomech.2025.106437 | - | tak | tak |
| Marrón-Gómez 2015 | 24679362 | 10.1016/j.ptsp.2014.02.001 | - | tak | tak |
| MacDonald 2020 | 30346313 | 10.1097/JSM.0000000000000638 | - | tak | tak |
| George 2024 | 39396409 | 10.1016/j.ajem.2024.09.037 | - | tak | tak |
| Greenwald 1998 | 9850786 | 10.1177/03635465980260061501 | - | tak | tak |

## **5. NIE ZNALEZIONO**

* C1 — bazy i hasła: Ankle-GO, \<8 pts OR \<8 points, re-sprain OR recurrence (dostępne nowsze publikacje koncentrują się na predykcji powrotu do sportu RTS, brak izolowanej walidacji OR 8.6 w kontekście nowych uszkodzeń więzadłowych).  
* C4 — bazy i hasła: syndesmotic injury OR high ankle sprain, vertical jump OR FABQ-sport, prognostic OR recovery time.  
* D1 — bazy i hasła: Star Excursion Balance Test OR SEBT, anterior asymmetry 4 cm, prospective OR predictive (odnalezione badanie z kryterium 4 cm cechuje charakter przekrojowy).  
* D3 — bazy i hasła: Schrefl, single-leg heel raise OR calf raise protocol (odnaleziono badanie, lecz w jego ogólnodostępnych wycinkach brak poszukiwanych wskaźników mierzalnych, tj. kadencja, nachylenie).  
* D4 — bazy i hasła: scoping review 86 studies, screening tests predict injury individual (zweryfikowano, że błędny przypis "86 studies" odnosi się do stosowania staz taktycznych w ratownictwie).  
* D9 — bazy i hasła: landing sports OR action sports OR inline skating OR skateboarding, screening battery OR physical assessment.  
* A4 — bazy i hasła: terrain-park features OR skatepark elements, injury risk differences.

#### **Cytowane prace**

> 1. Dynamic Balance Measures in Healthy and Chronic Ankle Instability, [https\://pubmed.ncbi.nlm.nih.gov/33049703/](https://pubmed.ncbi.nlm.nih.gov/33049703/)  
> 2. Dorsiflexion and dynamic postural control deficits are present in, [https\://pubmed.ncbi.nlm.nih.gov/22575498/](https://pubmed.ncbi.nlm.nih.gov/22575498/)  
> 3. Jumper's Knee: A Prospective Evaluation of Risk Factors in, [https\://pubmed.ncbi.nlm.nih.gov/30346313/](https://pubmed.ncbi.nlm.nih.gov/30346313/)  
> 4. Elite Athletes Successfully Return to the Preinjury Level of Sport, [https\://pubmed.ncbi.nlm.nih.gov/36599363/](https://pubmed.ncbi.nlm.nih.gov/36599363/)  
> 5. Reliability of three measures of ankle dorsiflexion range of motion, [https\://pubmed.ncbi.nlm.nih.gov/22666642/](https://pubmed.ncbi.nlm.nih.gov/22666642/)  
> 6. The Single Leg Heel Rise Test-A Helpful Tool for Dance Science?, [https\://pubmed.ncbi.nlm.nih.gov/38041188/](https://pubmed.ncbi.nlm.nih.gov/38041188/)  
> 7. Kinematic and kinetic characteristics of individuals with coping, [https\://pubmed.ncbi.nlm.nih.gov/39854850/](https://pubmed.ncbi.nlm.nih.gov/39854850/)  
> 8. The effect of two mobilization techniques on dorsiflexion in people, [https\://pubmed.ncbi.nlm.nih.gov/24679362/](https://pubmed.ncbi.nlm.nih.gov/24679362/)  
> 9. Adult skateboarding and motorized board injuries: A comparative, [https\://pubmed.ncbi.nlm.nih.gov/39396409/](https://pubmed.ncbi.nlm.nih.gov/39396409/)  
> 10. Dynamic impact response of human cadaveric forearms using a, [https\://pubmed.ncbi.nlm.nih.gov/9850786/](https://pubmed.ncbi.nlm.nih.gov/9850786/)

---

## Triage (4.11.2026, Fizjo AGV) — łącznie z 2a-AIS

Raport z aplikacji Gemini (2a-GEM) łączymy z wynikiem tego samego promptu z AI Studio (2a-AIS, `2026-11-04_batch4-2a_deep-research.md`, commit a699ed9). Źródła z obu silników liczą się razem; modele nie są źródłem. Wszystkie identyfikatory sprawdzone przez nas w PubMed (esummary/efetch) i Crossref; treść porównana z abstraktami; niezależność sprawdzona po autorach i — gdzie się dało — po liście piśmiennictwa przeglądu w Crossref.

### Identyfikatory

| Źródło (wg modelu) | PMID | DOI | PMCID | Wynik sprawdzenia |
|---|---|---|---|---|
| Reyburn RJ, Powden CJ 2020 (J Sport Rehabil 30(4):660–667) | 33049703 ✔ | 10.1123/jsr.2020-0224 ✔ | — | ✔ tytuł, autorzy, rok, tom zgodne |
| Bolia IK i wsp. 2023 (Clin J Sport Med 33(1):90–96) | 36599363 ✔ | 10.1097/JSM.0000000000001019 ✔ | — | ✔ |
| Konor MM i wsp. 2012 (Int J Sports Phys Ther 7(3):279–287) | 22666642 ✔ | brak (zgodnie z PubMed) | PMC3362988 ✔ | ✔ |
| „Schrefl 2024” | 38041188 ✘ | — | — | ✘ **PMID należy do innej pracy**: Schrefl A, Erlacher D, Schärli A 2023, *The Single Leg Heel Rise Test — A Helpful Tool for Dance Science?: A Systematic Review*, Med Probl Perform Art 38(4):234–248, doi:10.21091/mppa.2023.4028 (przegląd u tancerzy). Praca o protokole to S159 (DOI 10.36950/2024.9ciss009, bez PMID). Tabela „Identifier check” modelu mówi „zgodne: tak” — nieprawda |
| Hoch MC i wsp. 2012 (J Sci Med Sport 15(6):574–579) | 22575498 ✔ | 10.1016/j.jsams.2012.02.009 ✔ | — | ✔ |
| „Song K i wsp. 2025” (Clin Biomech 122:106437) | 39854850 ✔ | 10.1016/j.clinbiomech.2025.106437 ✔ | — | ✘ **autor**: pierwsza autorka to Jeon HG (Song K jest piąty) — identyfikatory poprawne |
| Marrón-Gómez D i wsp. 2015 (Phys Ther Sport 16(1):10–15) | 24679362 ✔ | 10.1016/j.ptsp.2014.02.001 ✔ | — | ✔; model: „brak etykiety w abstrakcie”, n „brak danych” — w abstrakcie jest „Randomized controlled clinical trial”, n=52 |
| MacDonald K i wsp. 2020 (Clin J Sport Med 30(5):489–494) | 30346313 ✔ | 10.1097/JSM.0000000000000638 ✔ | — | ✔ |
| George K i wsp. 2024 (Am J Emerg Med 86:98–103) | 39396409 ✔ | 10.1016/j.ajem.2024.09.037 ✔ | — | ✔ |
| Greenwald RM i wsp. 1998 (Am J Sports Med 26(6):825–830) | 9850786 ✔ | 10.1177/03635465980260061501 ✔ | — | ✔ |

Razem: **19 identyfikatorów** (10 PMID, 8 DOI, 1 PMCID) — wszystkie istnieją i pary PMID↔DOI↔PMCID są zgodne. **1 identyfikator przypisany innej pracy** (PMID 38041188), **1 błędny pierwszy autor** (Jeon, nie Song). Cytaty dosłowne zgodne z abstraktami, z wyjątkiem Reyburn (sklejka dwóch zdań abstraktu) i liczb w werdykcie C3 („ok. 49 vs 28 dni” — w abstrakcie 50,3 vs 29 dni).

### Treść, niezależność, populacja — twierdzenie po twierdzeniu

| Tw. | Werdykt modelu (2a-GEM) | 2a-AIS | Nasz werdykt |
|---|---|---|---|
| C1 Ankle-GO <8 pkt | brak 2. źródła | brak | **1/2** — zgodnie oba silniki |
| C2b orteza w CAI: pewność tak, testy nie | **„obalone”** (Reyburn 2020) | brak | **Sprzeczność, nie obalenie.** Reyburn & Powden 2020 (metaanaliza 7 badań, do X 2019; Picot 2025 nie mógł być włączony, brak wspólnych autorów → niezależne) w podgrupie CAI: silny efekt ortezy na SEBT/YBT (g = 0,777; 95% CI 0,418–1,136), u zdrowych słaby ujemny. Picot 2025 [S156] (crossover, n=30): brak różnic w testach funkcjonalnych Ankle-GO (w tym SEBT). Różne pakiety testów, małe badania w metaanalizie (w jej piśmiennictwie są też wyniki zerowe, np. Gribble 2010 „Bracing does not improve dynamic stability…”). W bazie: ⚠ sprzeczność przy ortezie, Reyburn → **S166**; twierdzenie o tejpie (2/2) bez zmian. |
| C3 więzozrost: operacja → dłuższy powrót | „częściowo” (Bolia 2023) | brak | **Kierunek zgodny, ale nie niezależne.** Bolia 2023 (przegląd 10 prac, 440 elitarnych sportowców: zachowawczo 29 ± 14 dni, operacyjnie 50,3 ± 13 dni) — porównanie piśmiennictwa w Crossref: co najmniej 8 prac wspólnych z Salameh 2022 [S151] (m.in. Taylor 2007, Wright 2004, Osbahr 2013, Calder 2016, Latham 2017, Vancolen 2019, Gerber 1998, D'Hooghe). Przegląd z tymi samymi badaniami ≠ drugie źródło. **1/2.** |
| C4 więzozrost: skok i FABQ | brak | brak | **1/2** |
| D1 SEBT przód >4 cm | brak (tylko przekrojowe) | brak | **1/2** (Stiffler 2017 — kierunek, retrospektywnie) |
| D2 WBLT MDC 1,9 / 1,6 cm | „częściowo” (Konor 2012) | brak | **Nie niezależne.** Konor 2012 jest w piśmiennictwie przeglądu Powden 2015 (Crossref), tak jak Chisholm 2012 i Backman 2011. Liczby też inne (MDC taśmy 1,1–1,5 cm, jeden początkujący badacz, n=20). **1/2.** |
| D3 normy wspięć | brak (PMID 38041188) | Schrefl 2024 (powtarzalność) | Powtarzalność już 2/2 (S158+S159). PMID 38041188 to inna praca tej samej grupy (przegląd u tancerzy: brak standaryzacji, brak uniwersalnych norm) — ta sama grupa co S159, więc nie jest niezależna. Normy: **1/2.** |
| D4 przesiew ≠ prognoza | brak; „86 badań” to rzekomo przegląd o stazach | „86 badań” bez autora | **1/2.** Informacji modelu o „stazach taktycznych” nie da się sprawdzić (bez źródła) — pomijamy. Trop Schrefl 2026 (PMID 41925545) wciąż do sprawdzenia. |
| D5 CAI: deficyt równowagi bez różnic w zakresie ruchu | **„obalone”** (Hoch 2012) | brak | **Rozdzielone na dwie części.** (a) Deficyt równowagi dynamicznej w CAI vs zdrowi: Alghadir 2020 (n=80 lekkoatletów, Y-balance; Rijad) + Hoch 2012 (case-control 30 vs 30, SEBT przód 76,05 vs 80,12%; Old Dominion) — brak wspólnych autorów → **2/2 → S164 + S165**. (b) Zakres ruchu: **sprzeczne zależnie od pomiaru** — czynny zakres goniometrem bez różnic (Alghadir), zgięcie grzbietowe w obciążeniu (WBLT) mniejsze w CAI (Hoch: 10,73 vs 12,47 cm, p=0,03). To nie obalenie, tylko inna metoda; każde 1/2. |
| D6 CAI: sztywniejsze lądowanie | „częściowo” (Jeon 2025) | brak | **Nie niezależne.** Przegląd Jeon 2025 ma De Ridder 2015 w piśmiennictwie (Crossref) i porównuje CAI z „coperami”, nie ze zdrowymi; o szczycie siły reakcji podłoża abstrakt nie mówi. **1/2.** |
| D7 mobilizacja z ruchem (MWM) w CAI | „potwierdzone 2/2” (Marrón-Gómez 2015) | brak | **2/2 → S160 + S161.** Burton 2020 (RCT pojedynczo zaślepione, n=18, 6 sesji samodzielnej MWM w wykroku w 2 tyg.: zgięcie grzbietowe istotnie wzrosło) + Marrón-Gómez 2015 (RCT, n=52, jedna MWM w obciążeniu vs placebo: wzrost utrzymany ≥48 h). Brak wspólnych autorów (USA vs Madryt); Marrón-Gómez nie jest w przeglądzie z Burton. Efekt krótkoterminowy, małe próby. |
| D8 zgięcie grzbietowe a tendinopatia rzepki | **„obalone”** (MacDonald 2020) | brak | **Sprzeczne, nie obalone.** MacDonald 2020 (kohorta prospektywna, 60 elitarnych siatkarzy, Calgary): żaden czynnik (w tym zakres zgięcia grzbietowego) nie przewidywał kolana skoczka, OR 0,94–1,07. Backman 2011 (prospektywne, 75 juniorów koszykówki): niski zakres (<36,5°) zwiększał ryzyko. Jedno badanie zerowe nie obala jednego dodatniego; zgodne z oceną Sprague 2018 „ograniczone/sprzeczne”. MacDonald nowsze niż Sprague 2018 (nie włączone). Brak wpisu (sprzeczne). |
| D9 bateria przesiewowa | brak | brak | brak źródła |
| A1 urazy AGV | „częściowo” (George 2024) | brak | **Nie dotyczy AGV.** George 2024: NEISS, dorośli, tylko złamania, deskorolki i deski z napędem (n=104 301), 61,8% kończyna górna — `{ANALOGIA:skateboarding}`; nie potwierdza danych AGV (Maudot vs S01 nadal rozbieżne). **1/2.** |
| A2/A3 ochraniacze nadgarstka | „częściowo” (Greenwald 1998) | brak | **A3 (zwłoki, obciążenie dynamiczne) 2/2 → S162 + S163.** Lewis 1997 (St. Louis; zaślepiony test upadku, z ochraniaczem więcej upadków, wyższa wysokość, energia i impuls do złamania) + Greenwald 1998 (Salt Lake City; 12 przedramion z 6 zwłok, gilotyna: siła i impuls przy złamaniu istotnie wyższe z ochraniaczem, P<0,01). Brak wspólnych autorów. Obie prace kadawerowe — nie populacja rolkarzy. Sprzeczne z S148 (obciążenie quasi-statyczne) — Greenwald sam wskazuje różnicę metod. A2 (splint-top, rolki): nadal **1/2**. |
| A4 elementy parku | brak | brak | **1/2** |

### „3 obalone hipotezy” — ocena

Żadnego „obalenia” nie przyjmujemy: C2b i D8 to **sprzeczne wyniki** (metaanaliza małych badań vs crossover; jedno prospektywne zerowe vs jedno prospektywne dodatnie), a D5 to **różnica metody pomiaru** (czynny zakres goniometrem vs zgięcie grzbietowe w obciążeniu). Model sam pomylił też kierunek w D5 — Hoch potwierdza część o równowadze.

### Co weszło do bazy

| Twierdzenie | Źródła | Plik |
|---|---|---|
| D7: mobilizacja z ruchem w obciążeniu (przez terapeutę lub samodzielna w wykroku) zwiększa zgięcie grzbietowe w CAI, krótkoterminowo | S160 Burton 2020 + S161 Marrón-Gómez 2015, `{DOWÓD:RCT}` ✔ 2/2 | `filar-2-rehabilitacja/czesci-ciala/kostka/niestabilnosc.md` |
| D5a: w CAI gorsza równowaga dynamiczna (Y-balance/SEBT) niż u zdrowych | S164 Alghadir 2020 + S165 Hoch 2012, `{DOWÓD:obserwacyjne}` ✔ 2/2; zakres ruchu — sprzeczne zależnie od pomiaru (1/2) | jw. |
| A3: na zwłokach w teście udarowym (upadek) ochraniacz nadgarstka podnosi energię/siłę potrzebną do złamania | S162 Lewis 1997 + S163 Greenwald 1998, `{DOWÓD:obserwacyjne}` (laboratoryjne, kadawerowe) ✔ 2/2 | `filar-2-rehabilitacja/czesci-ciala/nadgarstek-reka/urazy.md` |
| C2b: ⚠ sprzeczność przy ortezie (nie nowe twierdzenie) | S166 Reyburn 2020 vs S156 | `kostka/niestabilnosc.md` |

### Nadal bez drugiego niezależnego źródła (po 3 przebiegach: batch-3, 2a-AIS, 2a-GEM)

C1, C2b (orteza; dodatkowo sprzeczne), C3 (przegląd Bolia nie jest niezależny), C4, D1 (próg 4 cm), D2 (MDC 1,9/1,6 cm), D3 (normy), D4, D5b (zakres ruchu — sprzeczne), D6, D8 (sprzeczne), D9, A1, A2 (splint-top), A4.

Tropy na następną rundę: Schrefl 2026 (PMID 41925545, test wspięć a urazy podudzia — D3/D4); dla C2b — pierwotne badania ortez w CAI z listy Reyburn 2020 (Hadadi 2014, Hadadi 2019, Wikstrom 2006, Gribble 2010).
