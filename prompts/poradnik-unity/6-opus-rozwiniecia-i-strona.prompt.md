Pracujesz w repo fizjo-agv (zrób najpierw `git pull`). Odpowiadaj i pisz po polsku.

ETAP 1 — rozwinięcia w `poradniki/unity.md`
Każdy punkt techniczny w sekcjach techniki (najazd, wejście, skrzyżowanie, pozycja, balans, wyjście, styl, błędy) zostaje jako krótki pogrubiony nagłówek. Pod nim dopisz 2–3 zdania rozwinięcia: co dokładnie robisz, po czym poznasz, że dobrze, i najczęstszy błąd. Pisz prostym językiem dla rolkarza.
Zasady:
- Rozwinięcie opiera się WYŁĄCZNIE na źródłach już przypisanych do punktu (sources.md, research-raw/2026-11-11_unity_*.md). Bez nowych faktów, liczb ani źródeł.
- Etykieta, odnośnik do źródła i liczba źródeł (np. 1/2, 2/2) zostają przy punkcie bez zmian.
- Jeśli rozwinięcie jest twoim tłumaczeniem albo wnioskiem, a nie słowami źródła, oznacz je {WNIOSKOWANIE}.
- Sekcja „Wskazówki do przetestowania (niepotwierdzone)” zostaje, razem z ostrzeżeniami fizjo. Nie zmieniaj ich treści merytorycznej.
- Baner „to nie diagnoza” zostaje. Nie usuwaj żadnych plików.

ETAP 2 — nowy wygląd strony `strona/unity.html`
Zaprojektuj od nowa jeden samodzielny plik HTML, który działa offline (bez zewnętrznych CDN). Treść bierzesz tylko z `poradniki/unity.md`.
- Mobile-first, czytelny przy rampie na telefonie. Cele dotyku mają co najmniej 44 px. Tryb jasny i ciemny.
- Każda wskazówka pokazuje krótki nagłówek, a rozwinięcie jest schowane pod kliknięciem (details/summary), więc widok zwinięty działa jak ściąga. Dodaj przycisk „rozwiń wszystko / zwiń wszystko”.
- Etykiety są kolorowymi pigułkami: DOWÓD zielony, KONSENSUS niebieski, OPINIA szary, WNIOSKOWANIE żółty, ANALOGIA fioletowy, SPEKULACJA czerwony, PROPOZYCJA turkusowy. Dodaj legendę.
- Sekcja „Wskazówki do przetestowania” jest wizualnie wyróżniona jako niepotwierdzona, a ostrzeżenie fizjo przy każdej wskazówce widać od razu.
- Na górze: baner „nie diagnoza” i TL;DR. Przyklejona nawigacja sekcji, klikalne odnośniki do źródeł, oś etapów nauki i sekcja dla fizjoterapeuty lub trenera z przyciskiem druku (styl wydruku bez kolorowego tła). Na dole stopka z linkiem do repo.
- Dostępność: kontrast WCAG AA, poprawne nagłówki, obsługa klawiaturą.

Na koniec: sprawdź, że każdy odnośnik do źródła na stronie istnieje w sources.md albo w research-raw. Zrób commit „Unity: rozwinięcia wskazówek + nowy wygląd strony” i push. Podsumuj, co zmieniłeś.
