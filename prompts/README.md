# Prompty

Kolejność uruchamiania (decyzja 2.11.2026 — filar 1 „przygotowanie” jest główny):

1. `batch-2-przygotowanie/E-biomechanika-pozycja/` + `batch-2-przygotowanie/F-wzmacnianie-stabilizacja/`
2. `batch-2-przygotowanie/G-prewencja-periodyzacja/`
3. `batch-1/A-urazy-wg-grindu/` + `batch-1/B-obciazanie-sciegien/` (wspierają filar 1)
4. `batch-1/C-powrot-po-kostce/` + `batch-1/D-screening-fizjo/` (filar 2, niższy priorytet)

Argon (tylko sprzeczności): `batch-1/argon-sprzecznosci-szablon.md`.

## Linki do wklejenia modelom

Repo jest publiczne. Surowe pliki (gałąź `main`) do wklejenia w narzędzia z URL context (AI Studio, Gemini, Claude itp.):

```
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/METHODOLOGY.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/sources.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/README.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/soul-topsoul.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/makio.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/frontside-backside.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/royale.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/unity.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/inne.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/wzmacnianie.md
https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/stabilizacja-i-propriocepcja.md
```

Gotowa linijka do promptu:

> Przeczytaj te pliki przez URL context zanim zaczniesz: https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/METHODOLOGY.md https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/sources.md https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/pozycja-przy-grindach/README.md https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/wzmacnianie.md https://raw.githubusercontent.com/vitoexe/fizjo-agv/main/filar-1-przygotowanie/stabilizacja-i-propriocepcja.md — trzymaj się etykiet i zasady 2 niezależnych źródeł z METHODOLOGY.md, nie powtarzaj źródeł już obecnych w sources.md bez nowej informacji.
