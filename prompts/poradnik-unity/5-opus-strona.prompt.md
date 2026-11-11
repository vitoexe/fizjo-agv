Pracujesz w repo fizjo-agv (~/Documents/pro/com/fizjo-agv). Zrób stronę z poradnika `poradniki/unity.md` — tak, żeby rolkarz z kontuzją mógł ją otworzyć na telefonie i pokazać fizjoterapeucie lub trenerowi.

Wynik: JEDEN samodzielny plik `strona/unity.html` (HTML + CSS + minimalny JS w jednym pliku, bez frameworków, bez zewnętrznych CDN i fontów, działa offline po otwarciu z dysku). Nie zmieniaj innych plików.

Treść:
- Bierz WYŁĄCZNIE z `poradniki/unity.md`. Nie dopisuj, nie skracaj sensu, nie zmieniaj liczb, źródeł ani etykiet. Jeśli coś jest niejasne, zostaw jak w źródle.
- Na samej górze widoczny baner: „To nie jest diagnoza ani porada medyczna.”
- Pod nim TL;DR jako karta.

Układ i UX (mobile-first):
- Sekcje jako rozwijane panele (details/summary): Czym jest unity, Motoryka, Postawa, Balans, Styl, Fizjo, Progresja, Dla fizjo/trenera, Sprzeczności i luki, Źródła.
- Przyklejony spis treści / pasek nawigacji, przycisk „do góry”.
- Etykiety dowodu jako kolorowe „pigułki” z legendą: DOWÓD (zielony), KONSENSUS (niebieski), OPINIA (szary), WNIOSKOWANIE (żółty), ANALOGIA (fioletowy), SPEKULACJA (czerwony); obok „2/2” lub „1/2”. Kolory dostępne (kontrast WCAG AA), nie tylko kolor — też tekst.
- Odnośniki [Uxx]/[Dxx]/[Sxx] klikalne do listy źródeł; linki zewnętrzne otwierają się w nowej karcie.
- Motoryka jako oś etapów (najazd → wejście → skrzyżowanie → grind → wyjście), przy każdym „typowe błędy”.
- Sekcja „Dla fizjoterapeuty / trenera” wyróżniona i z przyciskiem „Drukuj / PDF” (styl @media print: bez nawigacji, wszystkie panele rozwinięte).
- Tryb jasny i ciemny wg ustawień systemu. Czytelna typografia, duże cele dotyku (min. 44 px).
- Stopka: „Fizjo AGV — open source, github.com/vitoexe/fizjo-agv. Treść do recenzji fizjoterapeuty.” + data wygenerowania.

Na koniec: otwórz plik, sprawdź, że wszystkie sekcje i źródła z markdowna są na stronie (porównaj liczbę źródeł), i wypisz krótkie podsumowanie, co zrobiłeś.
